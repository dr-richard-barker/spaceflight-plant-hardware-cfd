#!/usr/bin/env python3
"""
Figure 1: 3D Hardware Domain Architecture, Mesh Layout, and Flow Topologies
Comparing NASA VEGGIE, NASA APH, NASA Space Shuttle CHROMEX, CARA Square Dishes (+/- Light), and BRIC / BRIC-LED Round Dishes (+/- Light).
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
plt.rcParams['legend.fontsize'] = 6.5
plt.rcParams['figure.titlesize'] = 9.5

fig = plt.figure(figsize=(7.2, 7.5), dpi=300)
gs = fig.add_gridspec(3, 3, height_ratios=[1.1, 1.0, 1.0], hspace=0.40, wspace=0.35)

c_veg = '#008080'  # Teal (VEGGIE)
c_aph = '#005696'  # Blue (APH)
c_chr = '#d95f02'  # Orange (CHROMEX)
c_cara = '#7570b3' # Purple (CARA)
c_bric = '#e7298a' # Pink/Magenta (BRIC-LED)

# Row 1: Schematics
ax_a = fig.add_subplot(gs[0, 0])
ax_a.set_title('a  VEGGIE / VPS (37.6 L)', loc='left', fontweight='bold', color='#111111')
rect_veg = patches.Rectangle((0.15, 0.1), 0.7, 0.7, linewidth=1.5, edgecolor=c_veg, facecolor='#e6f2f2')
ax_a.add_patch(rect_veg)
rect_led = patches.Rectangle((0.15, 0.75), 0.7, 0.07, linewidth=1.0, edgecolor='#333333', facecolor='#ffeb3b', alpha=0.8)
ax_a.add_patch(rect_led)
fan = patches.Circle((0.5, 0.85), 0.07, facecolor='#333333', edgecolor=c_veg, linewidth=1.2)
ax_a.add_patch(fan)
ax_a.annotate('', xy=(0.5, 1.02), xytext=(0.5, 0.88), arrowprops=dict(arrowstyle="->", color='#c70039', lw=2.0))
ax_a.text(0.5, 1.05, 'Suction Exhaust (85 m³/h)', ha='center', fontsize=6, fontweight='bold', color='#c70039')
for i in range(3):
    p = patches.Rectangle((0.2 + i*0.22, 0.12), 0.16, 0.08, facecolor='#8d6e63', edgecolor='#4e342e')
    ax_a.add_patch(p)
ax_a.text(0.5, 0.23, '6 Plant Pillows', ha='center', color='#3e2723', fontsize=6, fontweight='bold')
ax_a.annotate('', xy=(0.22, 0.35), xytext=(0.05, 0.12), arrowprops=dict(arrowstyle="->", color=c_veg, lw=1.5))
ax_a.annotate('', xy=(0.78, 0.35), xytext=(0.95, 0.12), arrowprops=dict(arrowstyle="->", color=c_veg, lw=1.5))
ax_a.text(0.5, 0.50, 'Bottom-Up Suction Wash\n(Open Cabin Exchange)', ha='center', fontsize=6.5, color=c_veg, fontweight='bold')
ax_a.set_xlim(0, 1)
ax_a.set_ylim(0, 1.15)
ax_a.axis('off')

ax_b = fig.add_subplot(gs[0, 1])
ax_b.set_title('b  APH Phytotron (83.4 L)', loc='left', fontweight='bold', color='#111111')
rect_aph = patches.Rectangle((0.1, 0.1), 0.8, 0.75, linewidth=1.5, edgecolor=c_aph, facecolor='#e6edf4')
ax_b.add_patch(rect_aph)
rect_sc = patches.Rectangle((0.1, 0.1), 0.8, 0.12, linewidth=1.0, edgecolor='#1b3858', facecolor='#90caf9')
ax_b.add_patch(rect_sc)
ax_b.text(0.5, 0.15, 'Science Carrier (4 Quadrants)', ha='center', color='#0d47a1', fontsize=6, fontweight='bold')
rect_gla = patches.Rectangle((0.1, 0.8), 0.8, 0.06, linewidth=1.0, edgecolor='#333333', facecolor='#ffe082')
ax_b.add_patch(rect_gla)
ax_b.annotate('', xy=(0.35, 0.25), xytext=(0.1, 0.25), arrowprops=dict(arrowstyle="->", color=c_aph, lw=2.0))
ax_b.annotate('', xy=(0.65, 0.25), xytext=(0.9, 0.25), arrowprops=dict(arrowstyle="->", color=c_aph, lw=2.0))
ax_b.annotate('', xy=(0.5, 0.7), xytext=(0.5, 0.3), arrowprops=dict(arrowstyle="->", color=c_aph, lw=2.5))
ax_b.text(0.5, 0.48, 'Midline Collision &\nUniform Updraft (0.6 m/s)', ha='center', fontsize=6.5, color=c_aph, fontweight='bold')
ax_b.set_xlim(0, 1)
ax_b.set_ylim(0, 1.15)
ax_b.axis('off')

ax_c = fig.add_subplot(gs[0, 2])
ax_c.set_title('c  CHROMEX, CARA & BRIC', loc='left', fontweight='bold', color='#111111')
# CHROMEX
rect_chr = patches.Rectangle((0.02, 0.1), 0.26, 0.75, linewidth=1.2, edgecolor=c_chr, facecolor='#fbe9e7')
ax_c.add_patch(rect_chr)
ax_c.text(0.15, 0.45, 'CHROMEX\nPGC\n(0.87 L)', ha='center', fontsize=5.5, color=c_chr, fontweight='bold')
# CARA
rect_cara = patches.Rectangle((0.36, 0.25), 0.28, 0.55, linewidth=1.2, edgecolor=c_cara, facecolor='#ede7f6')
ax_c.add_patch(rect_cara)
rect_tape = patches.Rectangle((0.34, 0.23), 0.32, 0.59, linewidth=1.0, edgecolor='#ba68c8', facecolor='none', linestyle='--')
ax_c.add_patch(rect_tape)
ax_c.text(0.50, 0.50, 'CARA\n(100×100)\n± Light Tape', ha='center', fontsize=5.5, color=c_cara, fontweight='bold')
# BRIC
circ_bric = patches.Circle((0.84, 0.52), 0.14, linewidth=1.2, edgecolor=c_bric, facecolor='#fce4ec')
ax_c.add_patch(circ_bric)
ax_c.text(0.84, 0.50, 'BRIC-LED\n(Ø60 mm)\nPDFU Canister', ha='center', fontsize=5.0, color=c_bric, fontweight='bold')
ax_c.set_xlim(0, 1)
ax_c.set_ylim(0, 1.15)
ax_c.axis('off')

# Row 2: Metrics
systems = ['VEGGIE', 'APH', 'CHROMEX\n(6 PGCs)', 'CARA\n(4 Dishes)', 'BRIC-LED\n(6 PDFUs)']
colors = [c_veg, c_aph, c_chr, c_cara, c_bric]

ax_d = fig.add_subplot(gs[1, 0])
ax_d.set_title('d  Usable Growth Area (m²)', loc='left', fontweight='bold')
areas = [0.1075, 0.1708, 0.0274, 0.0400, 0.0170]
bars_d = ax_d.bar(range(5), areas, color=colors, edgecolor='#333333', linewidth=0.6, width=0.6)
ax_d.set_xticks(range(5))
ax_d.set_xticklabels(systems, rotation=25, ha='right', fontsize=6.5)
ax_d.set_ylabel('Growth Area ($A$, m²)')
ax_d.set_ylim(0, 0.20)
ax_d.grid(axis='y', linestyle=':', alpha=0.6)
for b, val in zip(bars_d, areas):
    ax_d.text(b.get_x() + b.get_width()/2, val + 0.005, f'{val:.3f}', ha='center', va='bottom', fontsize=6, fontweight='bold')

ax_e = fig.add_subplot(gs[1, 1])
ax_e.set_title('e  Volumetric Flow & Velocity', loc='left', fontweight='bold')
flows = [85.0, 26.4, 0.001, 1.2, 0.0001]
vels = [0.150, 0.600, 0.005, 0.082, 0.002]
x = np.arange(5)
w = 0.35
ax_e.bar(x - w/2, flows, width=w, color=colors, alpha=0.7, edgecolor='#333333', linewidth=0.6, label='Flow $Q$')
ax_e.set_yscale('log')
ax_e.set_ylabel('Flow Rate $Q$ (m³/h, log)')
ax_e.set_xticks(x)
ax_e.set_xticklabels(systems, rotation=25, ha='right', fontsize=6.5)
ax_e.grid(axis='y', linestyle=':', alpha=0.6)

ax_e2 = ax_e.twinx()
ax_e2.plot(x + w/2, vels, color='#d95f02', marker='s', markersize=4, linewidth=1.5, label='Velocity $U$')
ax_e2.set_ylabel('Bulk Velocity $U$ (m/s)', color='#d95f02')
ax_e2.tick_params(axis='y', labelcolor='#d95f02')
ax_e2.set_ylim(0, 0.7)

ax_f = fig.add_subplot(gs[1, 2])
ax_f.set_title('f  Air Exchange Rate (ACH)', loc='left', fontweight='bold')
ach = [2260, 317, 1.16, 6.0, 0.01]
bars_f = ax_f.bar(range(5), ach, color=colors, edgecolor='#333333', linewidth=0.6, width=0.6)
ax_f.set_yscale('log')
ax_f.set_xticks(range(5))
ax_f.set_xticklabels(systems, rotation=25, ha='right', fontsize=6.5)
ax_f.set_ylabel('Air Exchange Rate (h⁻¹)')
ax_f.grid(axis='y', linestyle=':', alpha=0.6)
for b, val in zip(bars_f, ach):
    ax_f.text(b.get_x() + b.get_width()/2, val * 1.3, f'{val:.1f}' if val < 100 else f'{int(val)}', ha='center', va='bottom', fontsize=6, fontweight='bold')

# Row 3: Boundary Layer & Environmental Control Regimes
ax_g = fig.add_subplot(gs[2, 0])
ax_g.set_title('g  Boundary Layer Thickness (δ_bl)', loc='left', fontweight='bold')
delta_1g = [4.82, 1.58, 6.5, 4.8, 3.5]
delta_0g = [7.95, 1.63, 25.0, 8.5, 20.0]
ax_g.bar(x - w/2, delta_1g, width=w, color='#4575b4', edgecolor='#333333', linewidth=0.6, label='Earth 1.0g')
ax_g.bar(x + w/2, delta_0g, width=w, color='#d73027', edgecolor='#333333', linewidth=0.6, label='Microgravity 0g')
ax_g.set_xticks(x)
ax_g.set_xticklabels(systems, rotation=25, ha='right', fontsize=6.5)
ax_g.set_ylabel('Boundary Layer $\delta_{bl}$ (mm)')
ax_g.legend(frameon=True, facecolor='white', framealpha=0.9, loc='upper left')
ax_g.grid(axis='y', linestyle=':', alpha=0.6)

ax_h = fig.add_subplot(gs[2, 1])
ax_h.set_title('h  Conductance Floor (g_bl)', loc='left', fontweight='bold')
g_bl_1g = [0.362, 1.102, 0.280, 0.380, 0.120]
g_bl_0g = [0.219, 1.071, 0.031, 0.326, 0.046]
ax_h.bar(x - w/2, g_bl_1g, width=w, color='#4575b4', edgecolor='#333333', linewidth=0.6, label='Earth 1.0g')
ax_h.bar(x + w/2, g_bl_0g, width=w, color='#d73027', edgecolor='#333333', linewidth=0.6, label='Microgravity 0g')
ax_h.axhline(0.25, color='#c70039', linestyle='--', linewidth=1.0, label='Hypoxia Limit')
ax_h.set_xticks(x)
ax_h.set_xticklabels(systems, rotation=25, ha='right', fontsize=6.5)
ax_h.set_ylabel('$g_{bl}$ (mol m⁻² s⁻¹)')
ax_h.legend(frameon=True, facecolor='white', framealpha=0.9, loc='upper right')
ax_h.grid(axis='y', linestyle=':', alpha=0.6)

ax_i = fig.add_subplot(gs[2, 2])
ax_i.set_title('i  Environmental Control Matrix', loc='left', fontweight='bold')
matrix = np.array([
    [1, 1, 0, 0], # VEGGIE
    [2, 2, 2, 2], # APH
    [1, 0, 0, 0], # CHROMEX
    [1, 0, 0, 0], # CARA
    [0, 0, 0, 0], # BRIC
])
im = ax_i.imshow(matrix, cmap='YlGnBu', aspect='auto')
ax_i.set_yticks(range(5))
ax_i.set_yticklabels(['VEGGIE', 'APH', 'CHROMEX', 'CARA', 'BRIC-LED'], fontsize=6.5)
ax_i.set_xticks(range(4))
ax_i.set_xticklabels(['Temp', 'RH', 'CO₂', 'C₂H₄'], fontsize=7)
labels = [['Cabin', 'Cabin', 'Open', 'None'],
          ['±0.5°C', '±5%', '±50ppm', 'Catalytic'],
          ['Lamps', 'None', 'None', 'None'],
          ['Ambient', 'Ambient', 'Open', 'None'],
          ['Passive', 'Passive', 'Sealed', 'Sealed']]
for i in range(5):
    for j in range(4):
        ax_i.text(j, i, labels[i][j], ha='center', va='center', fontsize=5.5, fontweight='bold', color='#111111' if matrix[i, j] < 2 else 'white')

out_dir = Path(__file__).resolve().parent / 'output'
out_dir.mkdir(parents=True, exist_ok=True)
pdf_path = out_dir / 'Fig1_hardware_domains.pdf'
png_path = out_dir / 'Fig1_hardware_domains.png'
plt.savefig(pdf_path, bbox_inches='tight')
plt.savefig(png_path, bbox_inches='tight', dpi=300)
print(f"Generated: {pdf_path} and {png_path}")
