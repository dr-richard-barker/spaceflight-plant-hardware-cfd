#!/usr/bin/env python3
"""
Figure 1: 3D Hardware Domain Architecture, Mesh Layout, and Flow Topologies
Comparing NASA VEGGIE, NASA APH, NASA ABRS (TAGES OSD-7/16), NASA Space Shuttle CHROMEX, CARA Square Dishes (+/- Light), and BRIC / BRIC-LED Round Dishes.
"""

import os
os.environ['MPLCONFIGDIR'] = '/tmp/mpl_config'
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from pathlib import Path

plt.rcParams['font.sans-serif'] = 'Helvetica'
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 7.5
plt.rcParams['axes.labelsize'] = 8
plt.rcParams['axes.titlesize'] = 8.5
plt.rcParams['xtick.labelsize'] = 7
plt.rcParams['ytick.labelsize'] = 7
plt.rcParams['legend.fontsize'] = 6.0
plt.rcParams['figure.titlesize'] = 9.5

fig = plt.figure(figsize=(7.4, 8.0), dpi=300)
gs = fig.add_gridspec(3, 3, height_ratios=[1.3, 1.0, 1.0], hspace=0.60, wspace=0.52)

c_veg = '#008080'  # Teal (VEGGIE)
c_aph = '#005696'  # Blue (APH)
c_abrs = '#2ca02c' # Green (ABRS / TAGES)
c_chr = '#d95f02'  # Orange (CHROMEX)
c_cara = '#7570b3' # Purple (CARA)
c_bric = '#e7298a' # Pink/Magenta (BRIC-LED)

# Row 1: Schematics
ax_a = fig.add_subplot(gs[0, 0])
ax_a.set_title('a  VEGGIE & ABRS (TAGES)', loc='left', fontweight='bold', color='#111111', pad=4)
# VEGGIE
rect_veg = patches.Rectangle((0.02, 0.1), 0.44, 0.68, linewidth=1.2, edgecolor=c_veg, facecolor='#e6f2f2')
ax_a.add_patch(rect_veg)
rect_led = patches.Rectangle((0.02, 0.72), 0.44, 0.06, linewidth=1.0, edgecolor='#333333', facecolor='#ffeb3b', alpha=0.9)
ax_a.add_patch(rect_led)
fan = patches.Circle((0.24, 0.84), 0.05, facecolor='#333333', edgecolor=c_veg, linewidth=1.0)
ax_a.add_patch(fan)
ax_a.annotate('', xy=(0.24, 1.02), xytext=(0.24, 0.90), arrowprops=dict(arrowstyle="->", color='#c70039', lw=1.6))
ax_a.text(0.24, 1.05, 'VEGGIE\n(37.6 L)', ha='center', fontsize=5.0, fontweight='bold', color=c_veg)
ax_a.text(0.24, 0.42, 'Top Suction\n6 Pillows', ha='center', fontsize=4.8, color=c_veg, fontweight='bold')

# ABRS (Single Middeck Locker with 6 square Petri dishes)
rect_abrs = patches.Rectangle((0.52, 0.1), 0.46, 0.68, linewidth=1.2, edgecolor=c_abrs, facecolor='#e8f5e9')
ax_a.add_patch(rect_abrs)
# 6 square Petri dishes in 2 tiers of 3
for row in [0.48, 0.22]:
    for col in [0.55, 0.68, 0.81]:
        d = patches.Rectangle((col, row), 0.10, 0.18, linewidth=0.8, edgecolor='#388e3c', facecolor='#c8e6c9')
        ax_a.add_patch(d)
ax_a.annotate('', xy=(0.75, 0.15), xytext=(0.75, 0.75), arrowprops=dict(arrowstyle="->", color=c_abrs, lw=1.6))
ax_a.text(0.75, 1.05, 'ABRS / TAGES\n(26.8 L / 6 Dishes)', ha='center', fontsize=5.0, fontweight='bold', color=c_abrs)
ax_a.text(0.75, 0.04, 'Forced Sweep + Scrubber', ha='center', fontsize=4.6, color=c_abrs, fontweight='bold')
ax_a.set_xlim(0, 1)
ax_a.set_ylim(0, 1.16)
ax_a.axis('off')

ax_b = fig.add_subplot(gs[0, 1])
ax_b.set_title('b  APH Phytotron (83.4 L)', loc='left', fontweight='bold', color='#111111', pad=4)
rect_aph = patches.Rectangle((0.1, 0.1), 0.8, 0.72, linewidth=1.5, edgecolor=c_aph, facecolor='#e6edf4')
ax_b.add_patch(rect_aph)
rect_sc = patches.Rectangle((0.1, 0.1), 0.8, 0.12, linewidth=1.0, edgecolor='#1b3858', facecolor='#90caf9')
ax_b.add_patch(rect_sc)
ax_b.text(0.5, 0.15, 'Science Carrier (4 Quads)', ha='center', color='#0d47a1', fontsize=5.6, fontweight='bold')
rect_gla = patches.Rectangle((0.1, 0.76), 0.8, 0.06, linewidth=1.0, edgecolor='#333333', facecolor='#ffe082')
ax_b.add_patch(rect_gla)
ax_b.annotate('', xy=(0.32, 0.25), xytext=(0.05, 0.25), arrowprops=dict(arrowstyle="->", color=c_aph, lw=2.0))
ax_b.annotate('', xy=(0.68, 0.25), xytext=(0.95, 0.25), arrowprops=dict(arrowstyle="->", color=c_aph, lw=2.0))
ax_b.annotate('', xy=(0.5, 0.72), xytext=(0.5, 0.58), arrowprops=dict(arrowstyle="->", color=c_aph, lw=2.2))
callout = patches.Rectangle((0.16, 0.32), 0.68, 0.22, linewidth=0.8, edgecolor='#90caf9', facecolor='#ffffff', alpha=0.9)
ax_b.add_patch(callout)
ax_b.text(0.5, 0.43, 'Sagittal Midline Collision\n& Upward Displacement\n(0.60 m/s Inlets)', ha='center', va='center', fontsize=5.5, color=c_aph, fontweight='bold')
ax_b.set_xlim(0, 1)
ax_b.set_ylim(0, 1.16)
ax_b.axis('off')

ax_c = fig.add_subplot(gs[0, 2])
ax_c.set_title('c  CHROMEX, CARA & BRIC', loc='left', fontweight='bold', color='#111111', pad=4)
# CHROMEX Box
rect_chr = patches.Rectangle((0.02, 0.12), 0.28, 0.72, linewidth=1.2, edgecolor=c_chr, facecolor='#fbe9e7')
ax_c.add_patch(rect_chr)
ax_c.text(0.16, 0.48, 'CHROMEX\nPGC\n(0.87 L)', ha='center', va='center', fontsize=5.3, color=c_chr, fontweight='bold')

# CARA Box
rect_cara = patches.Rectangle((0.36, 0.18), 0.29, 0.60, linewidth=1.2, edgecolor=c_cara, facecolor='#ede7f6')
ax_c.add_patch(rect_cara)
rect_tape = patches.Rectangle((0.34, 0.16), 0.33, 0.64, linewidth=1.0, edgecolor='#ba68c8', facecolor='none', linestyle='--')
ax_c.add_patch(rect_tape)
ax_c.text(0.505, 0.48, 'CARA Dish\n(100×100)\nMicropore', ha='center', va='center', fontsize=5.2, color=c_cara, fontweight='bold')

# BRIC-LED Box
circ_bric = patches.Circle((0.83, 0.48), 0.15, linewidth=1.2, edgecolor=c_bric, facecolor='#fce4ec')
ax_c.add_patch(circ_bric)
ax_c.text(0.83, 0.48, 'BRIC-LED\n(Ø60 mm)\nSealed', ha='center', va='center', fontsize=5.1, color=c_bric, fontweight='bold')
ax_c.set_xlim(0, 1)
ax_c.set_ylim(0, 1.16)
ax_c.axis('off')

# Row 2: Metrics
systems = ['VEGGIE', 'APH', 'ABRS', 'CHROMEX', 'CARA', 'BRIC-LED']
colors = [c_veg, c_aph, c_abrs, c_chr, c_cara, c_bric]
xx = np.arange(len(systems))

ax_d = fig.add_subplot(gs[1, 0])
ax_d.set_title('d  Usable Growth Area (m²)', loc='left', fontweight='bold')
areas = [0.1075, 0.1708, 0.0530, 0.0274, 0.0400, 0.0170]
ax_d.bar(xx, areas, color=colors, edgecolor='#333333', linewidth=0.6, width=0.55)
ax_d.set_xticks(xx)
ax_d.set_xticklabels(systems, rotation=25, ha='right', fontsize=5.8)
ax_d.set_ylabel('Growth Area (m²)', labelpad=6)
ax_d.grid(axis='y', linestyle=':', alpha=0.6)

ax_e = fig.add_subplot(gs[1, 1])
ax_e.set_title('e  Volumetric Flow Rate (m³/h)', loc='left', fontweight='bold')
flows = [85.0, 26.4, 12.0, 0.001, 0.0001, 0.0]
ax_e.bar(xx, flows, color=colors, edgecolor='#333333', linewidth=0.6, width=0.55)
ax_e.set_yscale('log')
ax_e.set_ylim(1e-4, 200)
ax_e.set_xticks(xx)
ax_e.set_xticklabels(systems, rotation=25, ha='right', fontsize=5.8)
ax_e.set_ylabel('Flow Rate $Q$ (m³/h)', labelpad=6)
ax_e.grid(axis='y', linestyle=':', alpha=0.6)

ax_f = fig.add_subplot(gs[1, 2])
ax_f.set_title('f  Air Exchange Rate (ACH)', loc='left', fontweight='bold')
ach = [2260, 317, 828, 1.16, 0.05, 0.0]
ax_f.bar(xx, ach, color=colors, edgecolor='#333333', linewidth=0.6, width=0.55)
ax_f.set_yscale('log')
ax_f.set_ylim(1e-2, 5000)
ax_f.set_xticks(xx)
ax_f.set_xticklabels(systems, rotation=25, ha='right', fontsize=5.8)
ax_f.set_ylabel('Air Exchange Rate (h⁻¹)', labelpad=6)
ax_f.grid(axis='y', linestyle=':', alpha=0.6)

# Row 3: Conductance, Boundary Layer, Biosecurity
ax_g = fig.add_subplot(gs[2, 0])
ax_g.set_title('g  0g Boundary Layer δ_bl (mm)', loc='left', fontweight='bold')
deltas = [7.95, 1.63, 2.40, 14.2, 8.50, 20.0]
ax_g.bar(xx, deltas, color=colors, edgecolor='#333333', linewidth=0.6, width=0.55)
ax_g.set_xticks(xx)
ax_g.set_xticklabels(systems, rotation=25, ha='right', fontsize=5.8)
ax_g.set_ylabel('Boundary Layer $\delta_{bl}$ (mm)', labelpad=6)
ax_g.grid(axis='y', linestyle=':', alpha=0.6)

ax_h = fig.add_subplot(gs[2, 1])
ax_h.set_title('h  0g Conductance g_bl', loc='left', fontweight='bold')
gbl = [0.219, 1.071, 0.650, 0.031, 0.326, 0.046]
ax_h.bar(xx, gbl, color=colors, edgecolor='#333333', linewidth=0.6, width=0.55)
ax_h.axhline(0.25, color='#c70039', linestyle='--', linewidth=1.0, label='Hypoxia Limit')
ax_h.set_xticks(xx)
ax_h.set_xticklabels(systems, rotation=25, ha='right', fontsize=5.8)
ax_h.set_ylabel('Conductance $g_{bl}$ (mol m⁻² s⁻¹)', labelpad=6)
ax_h.legend(loc='upper right', framealpha=0.9)
ax_h.grid(axis='y', linestyle=':', alpha=0.6)

ax_i = fig.add_subplot(gs[2, 2])
ax_i.set_title('i  Environmental Control', loc='left', fontweight='bold')
params = ['Temp', 'RH', 'CO2', 'C2H4', 'HEPA']
scores_aph = [5, 5, 5, 5, 5]
scores_abrs = [4, 4, 4, 5, 4]
scores_veg = [2, 2, 2, 1, 1]
x_p = np.arange(len(params))
w = 0.25
ax_i.bar(x_p - w, scores_veg, width=w, color=c_veg, label='VEGGIE')
ax_i.bar(x_p, scores_aph, width=w, color=c_aph, label='APH')
ax_i.bar(x_p + w, scores_abrs, width=w, color=c_abrs, label='ABRS')
ax_i.set_xticks(x_p)
ax_i.set_xticklabels(params, fontsize=6.2)
ax_i.set_ylabel('Control Fidelity (1-5)', labelpad=6)
ax_i.set_ylim(0, 6)
ax_i.legend(loc='upper left', fontsize=5.2, ncol=1, framealpha=0.9)
ax_i.grid(axis='y', linestyle=':', alpha=0.6)

out_dir = Path(__file__).resolve().parent / "output"
out_dir.mkdir(exist_ok=True, parents=True)
pdf_path = out_dir / "Fig1_hardware_domains.pdf"
png_path = out_dir / "Fig1_hardware_domains.png"

plt.savefig(pdf_path, dpi=300, bbox_inches='tight')
plt.savefig(png_path, dpi=300, bbox_inches='tight')
plt.close()
print("Fig1 regenerated successfully with ABRS / TAGES integration.")
