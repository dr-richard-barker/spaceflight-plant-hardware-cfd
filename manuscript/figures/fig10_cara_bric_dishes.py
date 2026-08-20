#!/usr/bin/env python3
import os
os.environ['MPLCONFIGDIR'] = '/tmp/mpl_config'
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

plt.rcParams['font.sans-serif'] = 'Helvetica'
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 7.5
plt.rcParams['axes.labelsize'] = 8
plt.rcParams['axes.titlesize'] = 8.5
plt.rcParams['xtick.labelsize'] = 7
plt.rcParams['ytick.labelsize'] = 7
plt.rcParams['legend.fontsize'] = 5.8

fig, axs = plt.subplots(3, 2, figsize=(7.2, 7.6), dpi=300)
plt.subplots_adjust(hspace=0.48, wspace=0.35)

carriers = ['CARA\n(+L, 1g)', 'CARA\n(+L, 0g)', 'CARA\n(-D, 0g)', 'BRIC-LED\n(+L, 0g)', 'BRIC\n(-D, 0g)']
x = np.arange(5)

# Panel a: External Boundary Layer Thickness
ax = axs[0, 0]
ax.set_title('a  External Boundary Layer $\delta_{ext}$ (mm)', loc='left', fontweight='bold')
delta = [4.8, 8.5, 9.8, 20.0, 25.0]
c_d = ['#7570b3', '#7570b3', '#9e9ac8', '#e7298a', '#c51b7d']
bars_a = ax.bar(x, delta, color=c_d, edgecolor='#333333', linewidth=0.6, width=0.55)
ax.set_xticks(x)
ax.set_xticklabels(carriers, rotation=15, ha='right', fontsize=6.2)
ax.set_ylabel('Thickness $\delta_{ext}$ (mm)')
ax.set_ylim(0, 30)
ax.grid(axis='y', linestyle=':', alpha=0.6)
for b, val in zip(bars_a, delta):
    ax.text(b.get_x() + b.get_width()/2, val + 0.8, f'{val:.1f}', ha='center', va='bottom', fontsize=5.8, fontweight='bold')

# Panel b: Three-Tier Series Resistance Breakdown
ax = axs[0, 1]
ax.set_title('b  Series Resistance $r_{tot} = r_{ext} + r_{tape} + r_{int}$', loc='left', fontweight='bold')
r_ext = np.array([120, 380, 420, 2000, 2500])
r_tape = np.array([650, 650, 650, 95000, 95000])
r_int = np.array([450, 450, 450, 4000, 4500])
ax.bar(x, r_ext, width=0.55, label='External $r_{ext}$', color='#abd9e9')
ax.bar(x, r_tape, width=0.55, bottom=r_ext, label='Tape/Wall $r_{tape}$', color='#fdae61')
ax.bar(x, r_int, width=0.55, bottom=r_ext+r_tape, label='Headspace $r_{int}$', color='#2c7bb6')
ax.set_yscale('log')
ax.set_ylim(1e2, 3e5)
ax.set_xticks(x)
ax.set_xticklabels(carriers, rotation=15, ha='right', fontsize=6.2)
ax.set_ylabel('Resistance (s/m, log)')
ax.legend(loc='upper left', framealpha=0.9)
ax.grid(axis='y', linestyle=':', alpha=0.6)

# Panel c: Headspace Oxygen Concentration
ax = axs[1, 0]
ax.set_title('c  Headspace Equilibrium $O_2$ (%)', loc='left', fontweight='bold')
o2 = [18.4, 14.2, 12.5, 1.8, 1.2]
c_o2 = ['#1a9850', '#fee08b', '#fdae61', '#d73027', '#d73027']
bars_c = ax.bar(x, o2, color=c_o2, edgecolor='#333333', linewidth=0.6, width=0.55)
ax.axhline(5.0, color='#c70039', linestyle='--', label='Hypoxia (5%)')
ax.set_xticks(x)
ax.set_xticklabels(carriers, rotation=15, ha='right', fontsize=6.2)
ax.set_ylabel('Headspace $O_2$ (%)')
ax.set_ylim(0, 24)
ax.grid(axis='y', linestyle=':', alpha=0.6)
ax.legend(loc='upper right', framealpha=0.9)
for b, val in zip(bars_c, o2):
    ax.text(b.get_x() + b.get_width()/2, val + 0.6, f'{val:.1f}%', ha='center', va='bottom', fontsize=5.8, fontweight='bold')

# Panel d: Ethylene Accumulation
ax = axs[1, 1]
ax.set_title('d  Headspace Ethylene $C_2H_4$ (ppm)', loc='left', fontweight='bold')
eth = [0.32, 0.85, 1.10, 3.80, 4.50]
c_eth = ['#1a9850', '#fee08b', '#fdae61', '#d73027', '#d73027']
bars_d = ax.bar(x, eth, color=c_eth, edgecolor='#333333', linewidth=0.6, width=0.55)
ax.axhline(0.50, color='#c70039', linestyle='--', label='Epinasty (0.5 ppm)')
ax.set_xticks(x)
ax.set_xticklabels(carriers, rotation=15, ha='right', fontsize=6.2)
ax.set_ylabel('Ethylene $C_2H_4$ (ppm)')
ax.set_ylim(0, 5.5)
ax.grid(axis='y', linestyle=':', alpha=0.6)
ax.legend(loc='upper left', framealpha=0.9)
for b, val in zip(bars_d, eth):
    y_pos = val + 0.15 if val > 0.4 else val + 0.25
    ax.text(b.get_x() + b.get_width()/2, y_pos, f'{val:.2f}', ha='center', va='bottom', fontsize=5.8, fontweight='bold')

# Panel e: Hours to 98% RH Droplet Condensation
ax = axs[2, 0]
ax.set_title('e  Hours to 98% RH Condensation', loc='left', fontweight='bold')
cond = [18.5, 6.5, 14.0, 1.5, 2.8]
c_cond = ['#1a9850', '#d73027', '#fee08b', '#d73027', '#d73027']
bars_e = ax.bar(x, cond, color=c_cond, edgecolor='#333333', linewidth=0.6, width=0.55)
ax.set_xticks(x)
ax.set_xticklabels(carriers, rotation=15, ha='right', fontsize=6.2)
ax.set_ylabel('Hours to Condensation (h)')
ax.set_ylim(0, 22)
ax.grid(axis='y', linestyle=':', alpha=0.6)
for b, val in zip(bars_e, cond):
    ax.text(b.get_x() + b.get_width()/2, val + 0.6, f'{val:.1f}h', ha='center', va='bottom', fontsize=5.8, fontweight='bold')

# Panel f: Suitability Space Matrix
ax = axs[2, 1]
ax.set_title('f  Sample Carrier Suitability Matrix', loc='left', fontweight='bold')
categories = ['Gas Exch.', 'Biosecurity', 'Optics/LED', 'Ethylene', 'No Condens.']
scores_cara_light = [4, 4, 4, 3, 3]
scores_bric_led = [1, 5, 4, 1, 1]
xx = np.arange(len(categories))
w = 0.35
ax.bar(xx - w/2, scores_cara_light, width=w, color='#7570b3', label='CARA (+Light)')
ax.bar(xx + w/2, scores_bric_led, width=w, color='#e7298a', label='BRIC-LED (+Light)')
ax.set_xticks(xx)
ax.set_xticklabels(categories, rotation=15, ha='right', fontsize=5.8)
ax.set_ylabel('Rating (1-5)')
ax.set_ylim(0, 6)
ax.grid(axis='y', linestyle=':', alpha=0.6)
ax.legend(loc='upper right', framealpha=0.9)

out_dir = Path(__file__).resolve().parent / 'output'
plt.savefig(out_dir / 'Fig10_cara_bric_dishes.pdf', bbox_inches='tight')
plt.savefig(out_dir / 'Fig10_cara_bric_dishes.png', bbox_inches='tight', dpi=300)
plt.close()
print("Fig10 regenerated clean.")
