#!/usr/bin/env python3
"""
make_abrs_geometry.py
Analytic 3D STL geometry generator for NASA's Advanced Biological Research System (ABRS)
and TAGES flight investigation (OSD-7 / OSD-16).

Hardware Specifications:
- EXPRESS Rack single middeck locker replacement volume: 440 mm (W) x 253 mm (D) x 516 mm (H)
- Dual growth chambers (Chamber A & B) or single GIS imaging payload configuration: ~24-28 L
- Green Fluorescent Protein Imaging System (GIS) payload carrier holding 6 square Petri dishes
  (100 x 100 x 20 mm) in 2 tiers of 3, wrapped in 3M Micropore surgical tape along perimeter.
- Active closed-loop recirculating airflow (2.5 - 10 CFM ~ 4.25 - 17.0 m³/h).
- Ducted top/side supply slots and bottom return scrubber plenum.
"""

import os
import argparse
from pathlib import Path

def facet(p1, p2, p3):
    u = [p2[i] - p1[i] for i in range(3)]
    v = [p3[i] - p1[i] for i in range(3)]
    nx = u[1]*v[2] - u[2]*v[1]
    ny = u[2]*v[0] - u[0]*v[2]
    nz = u[0]*v[1] - u[1]*v[0]
    mag = (nx**2 + ny**2 + nz**2)**0.5
    if mag > 1e-12:
        nx, ny, nz = nx/mag, ny/mag, nz/mag
    else:
        nx, ny, nz = 0.0, 0.0, 1.0
    return f"  facet normal {nx:.6e} {ny:.6e} {nz:.6e}\n    outer loop\n      vertex {p1[0]:.6e} {p1[1]:.6e} {p1[2]:.6e}\n      vertex {p2[0]:.6e} {p2[1]:.6e} {p2[2]:.6e}\n      vertex {p3[0]:.6e} {p3[1]:.6e} {p3[2]:.6e}\n    endloop\n  endfacet\n"

def quad(p1, p2, p3, p4):
    return facet(p1, p2, p3) + facet(p1, p3, p4)

def make_box_stl(name, x0, x1, y0, y1, z0, z1):
    out = [f"solid {name}\n"]
    p000 = (x0, y0, z0); p100 = (x1, y0, z0); p110 = (x1, y1, z0); p010 = (x0, y1, z0)
    p001 = (x0, y0, z1); p101 = (x1, y0, z1); p111 = (x1, y1, z1); p011 = (x0, y1, z1)
    out.append(quad(p000, p010, p110, p100)) # bottom (-z)
    out.append(quad(p001, p101, p111, p011)) # top (+z)
    out.append(quad(p000, p100, p101, p001)) # front (-y)
    out.append(quad(p110, p010, p011, p111)) # back (+y)
    out.append(quad(p010, p000, p001, p011)) # left (-x)
    out.append(quad(p100, p110, p111, p101)) # right (+x)
    out.append(f"endsolid {name}\n")
    return "".join(out)

def main():
    parser = argparse.ArgumentParser(description="Generate NASA ABRS / TAGES Geometry STLs")
    parser.add_argument('--case', type=str, default='cases/abrs_tages', help='Case directory')
    args = parser.parse_args()

    out_dir = Path(args.case) / 'constant' / 'triSurface'
    out_dir.mkdir(parents=True, exist_ok=True)

    # 1. ABRS Locker Chassis: 440 x 253 x 516 mm (in meters)
    chassis = make_box_stl('abrs_chassis', 0.0, 0.440, 0.0, 0.253, 0.0, 0.516)
    
    # 2. Supply Inlets: Top plenum slots at z = 0.500 to 0.516 m
    inlet_left = make_box_stl('supply_inlet_left', 0.020, 0.200, 0.020, 0.040, 0.490, 0.510)
    inlet_right = make_box_stl('supply_inlet_right', 0.240, 0.420, 0.020, 0.040, 0.490, 0.510)

    # 3. Exhaust Outlets: Bottom return scrubber plenum at z = 0.000 to 0.025 m
    exhaust = make_box_stl('exhaust_scrubber_duct', 0.050, 0.390, 0.200, 0.233, 0.010, 0.035)

    # 4. TAGES 6-Plate Science Carrier (2 tiers of 3 square Petri dishes: 100 x 100 x 20 mm)
    dishes = []
    tapes = []
    x_offsets = [0.035, 0.170, 0.305]
    z_offsets = [0.080, 0.260]

    plate_id = 1
    for z_off in z_offsets:
        for x_off in x_offsets:
            d_name = f'petri_dish_{plate_id}'
            t_name = f'micropore_tape_seam_{plate_id}'
            # Dish body (y = 0.080 to 0.100 m)
            dishes.append(make_box_stl(d_name, x_off, x_off + 0.100, 0.080, 0.100, z_off, z_off + 0.100))
            # Micropore tape seam around perimeter
            tapes.append(make_box_stl(t_name, x_off - 0.001, x_off + 0.101, 0.098, 0.101, z_off - 0.001, z_off + 0.101))
            plate_id += 1

    with open(out_dir / 'abrs_chamber.stl', 'w') as f:
        f.write(chassis + inlet_left + inlet_right + exhaust)

    with open(out_dir / 'abrs_dishes.stl', 'w') as f:
        f.write("".join(dishes) + "".join(tapes))

    print(f"ABRS & TAGES STLs generated in {out_dir}: abrs_chamber.stl and abrs_dishes.stl (6 square plates with micropore tape boundaries).")

if __name__ == '__main__':
    main()
