#!/usr/bin/env python3
"""
make_cara_dish_geometry.py
Analytic 3D STL geometry generator for CARA Experiment Square Petri Dishes (100x100x20 mm)
with micropore surgical tape perimeter seam and nutrient agar layer.
"""

import os
import argparse
from pathlib import Path

def facet(p1, p2, p3):
    # Compute normal vector
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
    parser = argparse.ArgumentParser(description="Generate CARA Square Petri Dish STLs")
    parser.add_argument('--case', type=str, default='cases/cara_dish', help='Case directory')
    args = parser.parse_args()

    out_dir = Path(args.case) / 'constant' / 'triSurface'
    out_dir.mkdir(parents=True, exist_ok=True)

    # Dish: 100 x 100 x 20 mm
    dish_stl = make_box_stl('dish_headspace', 0, 0.100, 0, 0.100, 0.005, 0.020)
    agar_stl = make_box_stl('agar_slab', 0, 0.100, 0, 0.100, 0.000, 0.005)
    seam_stl = make_box_stl('micropore_tape_seam', -0.001, 0.101, -0.001, 0.101, 0.018, 0.020)

    with open(out_dir / 'cara_dish.stl', 'w') as f:
        f.write(dish_stl + agar_stl + seam_stl)

    print(f"CARA Dish STLs generated at {out_dir / 'cara_dish.stl'}")

if __name__ == '__main__':
    main()
