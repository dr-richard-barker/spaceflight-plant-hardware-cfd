#!/usr/bin/env python3
"""
Figure 10: Science Sample Carrier Microenvironments:
CARA Square Petri Dishes (+/- Light) vs. BRIC / BRIC-LED Round Petri Dishes (+/- Light) in Spaceflight Hardware
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
plt.rcParams['xtick.labelsize'] = 6.5
plt.rcParams['ytick.labelsize'] = 7
plt.rcParams['legend.fontsize'] = 6.5

fig = plt.figure(figsize=(7.2, 7.5), dpi=300)
gs = fig.add_gridspec(3, 3, height_ratios=[1.1, 1.0, 1.0], hspace=0.45, wspace=0.35)

c_cara_lit = '#7570b3'  # Purple (CARA +Light)
c_cara_dark = '#514d7a' # Dark Purple (CARA -Dark)
c_bric_lit = '#e7298a'  # Magenta (BRIC-LED +Light)
c_bric_dark = '#980043' # Deep Red/Plum (BRIC -Dark)

# Row 1: Schematics
ax_a = fig.add_subplot(gs[0, 0])
ax_a.set_title('a  CARA Square Dish (100×100 mm)', loc='left', fontweight='bold')
rect_dish = patches.Rectangle((0.15, 0.15), 0.7, 0.65, linewidth=1.5, edgecolor='#5e35b1', facecolor='#ede7f6')
ax_a.add_patch(rect_dish)
rect_agar = patches.Rectangle((0.18, 0.18), 0.64, 0.22, linewidth=1.0, edgecolor='#7cb342', facecolor='#dcedc8')
ax_a.add_patch(rect_agar)
ax_a.text(0.5, 0.28, 'Nutrient Agar Slab', ha='center', fontsize=6, fontweight='bold', color='#33691e')
for i in range(4):
    ax_a.plot([0.28 + i*0.15, 0.28 + i*0.15], [0.40, 0.55], color='#2e7d32', lw=1.5)
    ax_a.plot([0.28 + i*0.15 - 0.03, 0.28 + i*0.15], [0.55, 0.58], color='#2e7d32', lw=1.2)
    ax_a.plot([0.28 + i*0.15 + 0.03, 0.28 + i*0.15], [0.55, 0.58], color='#2e7d32', lw=1.2)
ax_a.text(0.5, 0.62, 'Arabidopsis Seedlings', ha='center', fontsize=6, fontweight='bold', color='#1b5e20')
rect_tape = patches.Rectangle((0.12, 0.12), 0.76, 0.71, linewidth=1.4, edgecolor='#ba68c8', facecolor='none', linestyle='--')
ax_a.add_patch(rect_tape)
ax_a.text(0.5, 0.88, 'Micropore Surgical Tape Seam\n($P = 400$ mm, $r_{tape} = 650$ s/m)', ha='center', fontsize=5.5, fontweight='bold', color='#6a1b9a')
ax_a.annotate('', xy=(0.3, 0.75), xytext=(0.3, 0.98), arrowprops=dict(arrowstyle="->", color='#fbc02d', lw=1.5))
ax_a.annotate('', xy=(0.7, 0.75), xytext=(0.7, 0.98), arrowprops=dict(arrowstyle="->", color='#fbc02d', lw=1.5))
ax_a.text(0.5, 1.02, '± Light (VEGGIE LED vs Black Cloth)', ha='center', fontsize=5.5, fontweight='bold', color='#f57f17')
ax_a.set_xlim(0, 1)
ax_a.set_ylim(0, 1.15)
ax_a.axis('off')

ax_b = fig.add_subplot(gs[0, 1])
ax_b.set_title('b  BRIC-LED Round Dish (Ø60 mm)', loc='left', fontweight='bold')
rect_can = patches.Rectangle((0.15, 0.08), 0.7, 0.85, linewidth=1.5, edgecolor='#880e4f', facecolor='#fce4ec')
ax_b.add_patch(rect_can)
circ_dish = patches.Circle((0.5, 0.45), 0.26, linewidth=1.2, edgecolor='#c2185b', facecolor='#f8bbd0')
ax_b.add_patch(circ_dish)
ax_b.text(0.5, 0.42, 'Round Petri Dish\n(Ø60 mm in PDFU)', ha='center', fontsize=6, fontweight='bold', color='#880e4f')
rect_led = patches.Rectangle((0.25, 0.78), 0.5, 0.08, linewidth=1.0, edgecolor='#333333', facecolor='#ff80ab')
ax_b.add_patch(rect_led)
ax_b.text(0.5, 0.82, 'Integrated LED Cap', ha='center', fontsize=5.5, fontweight='bold', color='#4a148c')
ax_b.text(0.5, 0.15, 'Sealed Septum Barrier\n($r_{barrier} > 100$k s/m)', ha='center', fontsize=5.5, fontweight='bold', color='#b71c1c')
ax_b.set_xlim(0, 1)
ax_b.set_ylim(0, 1.15)
ax_b.axis('off')

ax_c = fig.add_subplot(gs[0, 2])
ax_c.set_title('c  Three-Tier Resistance Network', loc='left', fontweight='bold')
ax_c.text(0.5, 1.05, '1D Coupled Series Resistance', ha='center', fontsize=6.5, fontweight='bold')
resistors = [r'External Boundary: $r_{ext} = \delta_{ext} / D$',
             r'Porous Seam: $r_{tape} = \delta / (D_{eff} \cdot \epsilon)$',
             r'Internal Headspace: $r_{int} = h / D$']
r_colors = ['#4575b4', '#9970ab', '#fee08b']
for i in range(3):
    r = patches.Rectangle((0.15, 0.68 - i*0.28), 0.7, 0.18, linewidth=1.2, edgecolor='#333333', facecolor=r_colors[i])
    ax_c.add_patch(r)
    ax_c.text(0.5, 0.77 - i*0.28, resistors[i], ha='center', va='center', fontsize=5.5, fontweight='bold')
    if i < 2:
        ax_c.plot([0.5, 0.5], [0.68 - i*0.28, 0.68 - i*0.28 - 0.10], color='#111111', lw=1.5)
ax_c.set_xlim(0, 1)
ax_c.set_ylim(0, 1.15)
ax_c.axis('off')

# Labels
dishes = ['CARA (+L) 1g', 'CARA (+L) Moon', 'CARA (+L) 0g', 'CARA (-D) 0g', 'BRIC-LED 0g', 'BRIC (-D) 0g']

# Panel d: External Boundary Layer Thickness
ax_d = fig.add_subplot(gs[1, 0])
ax_d.set_title('d  External Boundary Layer ($\delta_{ext}$)', loc='left', fontweight='bold')
delta_ext = [4.8, 6.2, 8.5, 9.8, 20.0, 25.0]
c_bars_d = [c_cara_lit, c_cara_lit, c_cara_lit, c_cara_dark, c_bric_lit, c_bric_dark]
bars_d = ax_d.bar(range(6), delta_ext, color=c_bars_d, edgecolor='#333333', linewidth=0.6, width=0.55)
ax_d.set_xticks(range(6))
ax_d.set_xticklabels(dishes, rotation=30, ha='right')
ax_d.set_ylabel('Boundary Layer $\delta_{ext}$ (mm)')
ax_d.set_ylim(0, 30)
ax_d.grid(axis='y', linestyle=':', alpha=0.6)
for b, val in zip(bars_d, delta_ext):
    ax_d.text(b.get_x() + b.get_width()/2, val + 0.8, f'{val:.1f}', ha='center', va='bottom', fontsize=5.5, fontweight='bold')

# Panel e: Resistance Breakdown
ax_e = fig.add_subplot(gs[1, 1])
ax_e.set_title('e  Series Resistance Breakdown ($r_{tot}$)', loc='left', fontweight='bold')
r_ext = np.array([120, 210, 380, 420, 1500, 2000])
r_tape = np.array([650, 650, 650, 650, 10000, 10000])
r_int = np.array([450, 450, 450, 450, 450, 450])
x = np.arange(6)
w = 0.55
ax_e.bar(x, r_ext, width=w, label='External $r_{ext}$', color='#4575b4')
ax_e.bar(x, r_tape, width=w, bottom=r_ext, label='Seam $r_{tape}$', color='#9970ab')
ax_e.bar(x, r_int, width=w, bottom=r_ext+r_tape, label='Internal $r_{int}$', color='#fdae61')
ax_e.set_yscale('log')
ax_e.set_xticks(x)
ax_e.set_xticklabels(dishes, rotation=30, ha='right')
ax_e.set_ylabel('Diffusive Resistance (s/m, log)')
ax_e.legend(loc='upper left', fontsize=5.5)
ax_e.grid(axis='y', linestyle=':', alpha=0.6)

# Panel f: Headspace Equilibrium Oxygen
ax_f = fig.add_subplot(gs[1, 2])
ax_f.set_title('f  Equilibrium Headspace $O_2$ (%)', loc='left', fontweight='bold')
o2_eq = [18.4, 16.8, 14.2, 12.5, 1.8, 1.2]
bars_f = ax_f.bar(range(6), o2_eq, color=['#1a9850', '#91cf60', '#fee08b', '#fc8d59', '#d73027', '#a50026'], edgecolor='#333333', linewidth=0.6, width=0.55)
ax_f.axhline(5.0, color='#c70039', linestyle='--', label='Hypoxia (5% $O_2$)')
ax_f.set_xticks(range(6))
ax_f.set_xticklabels(dishes, rotation=30, ha='right')
ax_f.set_ylabel('Headspace $O_2$ (%)')
ax_f.set_ylim(0, 22)
ax_f.grid(axis='y', linestyle=':', alpha=0.6)
ax_f.legend(loc='upper right', fontsize=5.5)
for b, val in zip(bars_f, o2_eq):
    ax_f.text(b.get_x() + b.get_width()/2, val + 0.6, f'{val:.1f}%', ha='center', va='bottom', fontsize=5.5, fontweight='bold')

# Row 3: Transient Dynamics
t_hours = np.linspace(0, 48, 150)

# Panel g: Toxic Ethylene Accumulation
ax_g = fig.add_subplot(gs[2, 0])
ax_g.set_title('g  Ethylene ($C_2H_4$) Accumulation', loc='left', fontweight='bold')
c2h4_cara_lit_0g = 0.85 * (1 - np.exp(-t_hours / 8.5))
c2h4_cara_dark_0g = 1.10 * (1 - np.exp(-t_hours / 10.0))
c2h4_bric_lit_0g = 3.80 * (1 - np.exp(-t_hours / 3.2))
c2h4_bric_dark_0g = 4.50 * (1 - np.exp(-t_hours / 4.5))

ax_g.plot(t_hours, c2h4_bric_dark_0g, label='BRIC (-Dark, 0g)', color=c_bric_dark, lw=1.8)
ax_g.plot(t_hours, c2h4_bric_lit_0g, label='BRIC-LED (+Light, 0g)', color=c_bric_lit, lw=1.6)
ax_g.plot(t_hours, c2h4_cara_dark_0g, label='CARA (-Dark, 0g)', color=c_cara_dark, lw=1.6)
ax_g.plot(t_hours, c2h4_cara_lit_0g, label='CARA (+Light, 0g)', color=c_cara_lit, lw=1.8)
ax_g.axhline(0.50, color='#c70039', linestyle='--', label='Epinasty (0.5 ppm)')
ax_g.set_xlabel('Time Post-Inoculation (hours)')
ax_g.set_ylabel('Headspace $C_2H_4$ (ppm)')
ax_g.grid(True, linestyle=':', alpha=0.6)
ax_g.legend(loc='center right', fontsize=5.5)

# Panel h: Condensation Onset
ax_h = fig.add_subplot(gs[2, 1])
ax_h.set_title('h  Lid Condensation Onset ($RH>98\%$)', loc='left', fontweight='bold')
cond_hours = [18.5, 12.0, 6.5, 14.0, 1.5, 2.8]
bars_h = ax_h.bar(range(6), cond_hours, color=['#1a9850', '#91cf60', '#fc8d59', '#fee08b', '#d73027', '#a50026'], edgecolor='#333333', linewidth=0.6, width=0.55)
ax_h.set_xticks(range(6))
ax_h.set_xticklabels(dishes, rotation=30, ha='right')
ax_h.set_ylabel('Hours to Condensation (h)')
ax_h.set_ylim(0, 22)
ax_h.grid(axis='y', linestyle=':', alpha=0.6)
for b, val in zip(bars_h, cond_hours):
    ax_h.text(b.get_x() + b.get_width()/2, val + 0.6, f'{val:.1f}h', ha='center', va='bottom', fontsize=5.5, fontweight='bold')

# Panel i: Microclimate Decision Space
ax_i = fig.add_subplot(gs[2, 2])
ax_i.set_title('i  Sample Carrier Suitability Space', loc='left', fontweight='bold')
x_scat = [0.38, 0.35, 0.326, 0.260, 0.046, 0.025]
y_scat = [0.32, 0.52, 0.85, 1.10, 3.80, 4.50]
ax_i.scatter(x_scat[:3], y_scat[:3], color=c_cara_lit, s=55, marker='s', label='CARA (+Light)', zorder=5)
ax_i.scatter([x_scat[3]], [y_scat[3]], color=c_cara_dark, s=55, marker='^', label='CARA (-Dark)', zorder=5)
ax_i.scatter([x_scat[4]], [y_scat[4]], color=c_bric_lit, s=55, marker='o', label='BRIC-LED (+Light)', zorder=5)
ax_i.scatter([x_scat[5]], [y_scat[5]], color=c_bric_dark, s=55, marker='D', label='BRIC (-Dark)', zorder=5)
ax_i.axhline(0.50, color='#c70039', linestyle=':', label='Max Safe $C_2H_4$')
ax_i.axvline(0.25, color='#1a9850', linestyle='--', label='Min Conductance $g_{bl}$')
ax_i.set_xlabel('Conductance $g_{bl}$ (mol m⁻² s⁻¹)')
ax_i.set_ylabel('Equilibrium $C_2H_4$ (ppm)')
ax_i.grid(True, linestyle=':', alpha=0.6)
ax_i.legend(loc='upper right', fontsize=5.5)

out_dir = Path(__file__).resolve().parent / 'output'
plt.savefig(out_dir / 'Fig10_cara_bric_dishes.pdf', bbox_inches='tight')
plt.savefig(out_dir / 'Fig10_cara_bric_dishes.png', bbox_inches='tight', dpi=300)
print("Fig10 generated successfully!")
