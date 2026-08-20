#!/usr/bin/env python3
"""
make_bric_led_geometry.py
Analytic 3D STL geometry generator for NASA BRIC-LED Petri Dish Fixation Units (PDFU)
with 60 mm diameter round Petri dishes and integrated LED cap.
"""

import os
import argparse
import numpy as np
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

def make_cylinder_stl(name, radius, z0, z1, n_segments=36):
    out = [f"solid {name}\n"]
    angles = np.linspace(0, 2*np.pi, n_segments, endpoint=False)
    # Bottom circle (z0)
    for i in range(n_segments):
        a1, a2 = angles[i], angles[(i+1)%n_segments]
        p0 = (0, 0, z0)
        p1 = (radius*np.cos(a2), radius*np.sin(a2), z0)
        p2 = (radius*np.cos(a1), radius*np.sin(a1), z0)
        out.append(facet(p0, p1, p2))
    # Top circle (z1)
    for i in range(n_segments):
        a1, a2 = angles[i], angles[(i+1)%n_segments]
        p0 = (0, 0, z1)
        p1 = (radius*np.cos(a1), radius*np.sin(a1), z1)
        p2 = (radius*np.cos(a2), radius*np.sin(a2), z1)
        out.append(facet(p0, p1, p2))
    # Side walls
    for i in range(n_segments):
        a1, a2 = angles[i], angles[(i+1)%n_segments]
        p1 = (radius*np.cos(a1), radius*np.sin(a1), z0)
        p2 = (radius*np.cos(a2), radius*np.sin(a2), z0)
        p3 = (radius*np.cos(a2), radius*np.sin(a2), z1)
        p4 = (radius*np.cos(a1), radius*np.sin(a1), z1)
        out.append(facet(p1, p2, p3))
        out.append(facet(p1, p3, p4))
    out.append(f"endsolid {name}\n")
    return "".join(out)

def main():
    parser = argparse.ArgumentParser(description="Generate BRIC-LED PDFU Round Petri Dish STLs")
    parser.add_argument('--case', type=str, default='cases/bric_pdfu', help='Case directory')
    args = parser.parse_args()

    out_dir = Path(args.case) / 'constant' / 'triSurface'
    out_dir.mkdir(parents=True, exist_ok=True)

    # Round dish: Ø60 mm (r = 30 mm), height = 15 mm
    dish_stl = make_cylinder_stl('dish_headspace', 0.030, 0.005, 0.015)
    agar_stl = make_cylinder_stl('agar_layer', 0.030, 0.000, 0.005)
    led_cap = make_cylinder_stl('led_light_cap', 0.032, 0.015, 0.018)

    with open(out_dir / 'bric_pdfu.stl', 'w') as f:
        f.write(dish_stl + agar_stl + led_cap)

    print(f"BRIC-LED STLs generated at {out_dir / 'bric_pdfu.stl'}")

if __name__ == '__main__':
    main()
