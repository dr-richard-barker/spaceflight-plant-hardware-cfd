#!/usr/bin/env python3
"""
make_abrs_geometry.py
Analytic 3D STL geometry generator for NASA's Advanced Biological Research System (ABRS)
and TAGES flight investigation (Paul et al. 2013, BMC Plant Biol 13:112, Fig 1; NASA OSDR OSD-7/16).

Structural Architecture:
- EXPRESS Rack single middeck locker replacement volume: 440 mm (W) x 253 mm (D) x 516 mm (H)
- Green Fluorescent Protein Imaging System (GIS) payload carrier featuring a 3-faceted frame:
  * Right Column (x = 0.32 m): Position 1 (Bottom Tier, Primary Camera Axis) & Position 2 (Top Tier)
  * Rear Column  (y = 0.18 m): Position 3 (Bottom Tier) & Position 4 (Top Tier)
  * Left Column  (x = 0.12 m): Position 5 (Bottom Tier) & Position 6 (Top Tier) + Lateral LED Driver Board
- All 6 plates are 100 x 100 x 20 mm square Petri dishes wrapped with 3M Micropore surgical tape.
- Top supply air distribution slots and bottom return catalytic scrubber plenum.
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
    parser = argparse.ArgumentParser(description="Generate NASA ABRS / TAGES GIS Carrier Geometry STLs")
    parser.add_argument('--case', type=str, default='cases/abrs_tages', help='Case directory')
    args = parser.parse_args()

    out_dir = Path(args.case) / 'constant' / 'triSurface'
    out_dir.mkdir(parents=True, exist_ok=True)

    # 1. ABRS Locker Chassis: 440 x 253 x 516 mm
    chassis = make_box_stl('abrs_chassis', 0.0, 0.440, 0.0, 0.253, 0.0, 0.516)
    
    # 2. Supply Inlets (Top plenum slots) & Exhaust Outlet (Bottom return scrubber)
    inlet_top = make_box_stl('supply_inlet_top', 0.050, 0.390, 0.030, 0.220, 0.490, 0.510)
    exhaust = make_box_stl('exhaust_scrubber_duct', 0.050, 0.390, 0.030, 0.220, 0.010, 0.035)

    # 3. GIS 3-Column Structural Frame (Right, Rear, Left Facets)
    # Right Column: x = 0.30 to 0.34 m (Holds Plate 1 Bot, Plate 2 Top)
    # Rear Column:  y = 0.16 to 0.20 m (Holds Plate 3 Bot, Plate 4 Top)
    # Left Column:  x = 0.10 to 0.14 m (Holds Plate 5 Bot, Plate 6 Top)
    frame_r = make_box_stl('gis_frame_right', 0.300, 0.340, 0.050, 0.200, 0.060, 0.420)
    frame_b = make_box_stl('gis_frame_rear',  0.100, 0.340, 0.180, 0.220, 0.060, 0.420)
    frame_l = make_box_stl('gis_frame_left',  0.100, 0.140, 0.050, 0.200, 0.060, 0.420)
    
    # LED Driver Board on Outer Left Wall
    led_board = make_box_stl('gis_led_board', 0.060, 0.080, 0.060, 0.190, 0.100, 0.380)

    # 4. 6 Square Petri Dishes (100 x 100 x 20 mm) in 3 columns & 2 tiers:
    # Tier 1 (Bottom): z = 0.080 to 0.180 m
    # Tier 2 (Top):    z = 0.260 to 0.360 m
    dishes = []
    tapes = []

    # Position 1: Right Column, Bottom Tier (Faces Camera)
    dishes.append(make_box_stl('plate_pos_1_bot', 0.310, 0.330, 0.070, 0.170, 0.080, 0.180))
    tapes.append(make_box_stl('tape_seam_1',      0.308, 0.332, 0.068, 0.172, 0.078, 0.182))

    # Position 2: Right Column, Top Tier
    dishes.append(make_box_stl('plate_pos_2_top', 0.310, 0.330, 0.070, 0.170, 0.260, 0.360))
    tapes.append(make_box_stl('tape_seam_2',      0.308, 0.332, 0.068, 0.172, 0.258, 0.362))

    # Position 3: Rear Column, Bottom Tier
    dishes.append(make_box_stl('plate_pos_3_bot', 0.170, 0.270, 0.170, 0.190, 0.080, 0.180))
    tapes.append(make_box_stl('tape_seam_3',      0.168, 0.272, 0.168, 0.192, 0.078, 0.182))

    # Position 4: Rear Column, Top Tier
    dishes.append(make_box_stl('plate_pos_4_top', 0.170, 0.270, 0.170, 0.190, 0.260, 0.360))
    tapes.append(make_box_stl('tape_seam_4',      0.168, 0.272, 0.168, 0.192, 0.258, 0.362))

    # Position 5: Left Column, Bottom Tier
    dishes.append(make_box_stl('plate_pos_5_bot', 0.110, 0.130, 0.070, 0.170, 0.080, 0.180))
    tapes.append(make_box_stl('tape_seam_5',      0.108, 0.132, 0.068, 0.172, 0.078, 0.182))

    # Position 6: Left Column, Top Tier
    dishes.append(make_box_stl('plate_pos_6_top', 0.110, 0.130, 0.070, 0.170, 0.260, 0.360))
    tapes.append(make_box_stl('tape_seam_6',      0.108, 0.132, 0.068, 0.172, 0.258, 0.362))

    with open(out_dir / 'abrs_chamber.stl', 'w') as f:
        f.write(chassis + inlet_top + exhaust + frame_r + frame_b + frame_l + led_board)

    with open(out_dir / 'abrs_dishes.stl', 'w') as f:
        f.write("".join(dishes) + "".join(tapes))

    print(f"ABRS GIS STLs successfully generated in {out_dir}: 3-column, 2-tier carousel (Plates 1-6 with micropore seams).")

if __name__ == '__main__':
    main()
