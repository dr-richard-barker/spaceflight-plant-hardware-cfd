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
plt.rcParams['legend.fontsize'] = 6.5

fig, axs = plt.subplots(2, 2, figsize=(7.2, 5.8), dpi=300)
plt.subplots_adjust(hspace=0.35, wspace=0.3)

# Panel a: Bioaerosol Clearance Kinetics
ax = axs[0, 0]
ax.set_title('a  Bioaerosol Clearance Dynamics ($d_p=3\mu$m)', loc='left', fontweight='bold')
t = np.linspace(0, 100, 150)
c_veg_high = np.exp(-t / 13.8)
c_veg_low = np.exp(-t / 58.6)
c_aph_nom = np.exp(-t / 18.4)
c_aph_high = np.exp(-t / 8.1)
ax.plot(t, c_veg_high, label='VEGGIE High (Exhaust to Cabin)', color='#d73027', lw=1.6)
ax.plot(t, c_veg_low, label='VEGGIE Low (Stagnant Plume)', color='#e66101', linestyle='--', lw=1.6)
ax.plot(t, c_aph_nom, label='APH Nom (HEPA Recirc)', color='#005696', lw=1.8)
ax.plot(t, c_aph_high, label='APH High Blast (HEPA)', color='#2b83ba', lw=1.6)
ax.set_xlabel('Time $t$ (s)')
ax.set_ylabel('Normalized Bioaerosol Fraction $N(t)/N_0$')
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='upper right')

# Panel b: Spore Export vs Containment
ax = axs[0, 1]
ax.set_title('b  Cabin Bioburden vs HEPA Containment', loc='left', fontweight='bold')
sys = ['VEGGIE\n(Open)', 'APH\n(Closed)', 'CHROMEX\n(Canister)', 'CARA\n(Micropore)', 'BRIC-LED\n(PDFU)']
export = [100, 0, 0, 0, 0]
contain = [0, 100, 100, 100, 100]
x = np.arange(5)
w = 0.35
ax.bar(x - w/2, export, width=w, color='#d73027', label='Cabin Spore Export (%)')
ax.bar(x + w/2, contain, width=w, color='#1a9850', label='Chamber / Tape Containment (%)')
ax.set_xticks(x)
ax.set_xticklabels(sys, rotation=15, ha='right', fontsize=6.5)
ax.set_ylabel('Fraction of Bioaerosols (%)')
ax.set_ylim(0, 120)
ax.legend(loc='upper right')
ax.grid(axis='y', linestyle=':', alpha=0.6)

# Panel c: Deposition vs Filtration Fate
ax = axs[1, 0]
ax.set_title('c  Aerosolized Particle Fate Matrix', loc='left', fontweight='bold')
hepa = [0, 94.2, 0, 0, 0]
wall = [8.5, 5.8, 45.0, 12.0, 98.0]
leaf = [12.0, 0.0, 55.0, 88.0, 2.0]
cabin = [79.5, 0.0, 0.0, 0.0, 0.0]
ax.bar(x, cabin, width=0.55, label='Exported to Cabin', color='#d73027')
ax.bar(x, leaf, width=0.55, bottom=cabin, label='Leaf / Dish Deposition', color='#fdae61')
ax.bar(x, wall, width=0.55, bottom=np.array(cabin)+np.array(leaf), label='Wall Deposition', color='#abd9e9')
ax.bar(x, hepa, width=0.55, bottom=np.array(cabin)+np.array(leaf)+np.array(wall), label='HEPA Scrubbed', color='#2c7bb6')
ax.set_xticks(x)
ax.set_xticklabels(sys, rotation=15, ha='right', fontsize=6.5)
ax.set_ylabel('Particle Fate Distribution (%)')
ax.set_ylim(0, 110)
ax.legend(loc='upper right', fontsize=6)
ax.grid(axis='y', linestyle=':', alpha=0.6)

# Panel d: Pathogen Infection Vulnerability Score
ax = axs[1, 1]
ax.set_title('d  Phytopathogen Vulnerability Score', loc='left', fontweight='bold')
# Stagnation + humidity + contact score (0-100)
vuln = [88.5, 8.2, 75.0, 32.5, 45.0]
c_bar = ['#d73027', '#1a9850', '#d73027', '#fee08b', '#fdae61']
bars_v = ax.bar(range(5), vuln, color=c_bar, edgecolor='#333333', linewidth=0.6, width=0.55)
ax.set_xticks(range(5))
ax.set_xticklabels(sys, rotation=15, ha='right', fontsize=6.5)
ax.set_ylabel('Mold / Hypoxia Vulnerability (0-100)')
ax.set_ylim(0, 105)
ax.grid(axis='y', linestyle=':', alpha=0.6)
for b, val in zip(bars_v, vuln):
    ax.text(b.get_x() + b.get_width()/2, val + 2, f'{val:.1f}', ha='center', va='bottom', fontsize=6, fontweight='bold')

out_dir = Path(__file__).resolve().parent / 'output'
plt.savefig(out_dir / 'Fig5_biosecurity_trades.pdf', bbox_inches='tight')
plt.savefig(out_dir / 'Fig5_biosecurity_trades.png', bbox_inches='tight', dpi=300)
print("Fig5 generated successfully!")
