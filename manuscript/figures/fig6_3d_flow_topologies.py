#!/usr/bin/env python3
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
plt.rcParams['legend.fontsize'] = 6.2

fig, axs = plt.subplots(2, 2, figsize=(7.2, 6.0), dpi=300)
plt.subplots_adjust(hspace=0.42, wspace=0.32)

# Panel a: VEGGIE Suction Recirculation
ax = axs[0, 0]
ax.set_title('a  VEGGIE Suction Recirculation Vortex', loc='left', fontweight='bold')
ax.add_patch(patches.Rectangle((0.1, 0.1), 0.8, 0.8, fill=True, color='#f0f9e8', ec='#008080', lw=1.5))
for y in np.linspace(0.15, 0.35, 3):
    ax.annotate('', xy=(0.5, 0.85), xytext=(0.2, y), arrowprops=dict(arrowstyle="->", color='#008080', lw=1.5))
    ax.annotate('', xy=(0.5, 0.85), xytext=(0.8, y), arrowprops=dict(arrowstyle="->", color='#008080', lw=1.5))
ax.add_patch(patches.Circle((0.5, 0.88), 0.08, color='#c70039'))
ax.text(0.5, 0.88, 'FAN', color='white', ha='center', va='center', fontweight='bold', fontsize=6)
ax.text(0.5, 0.40, 'Stagnant Dead Zones\nin Lower Outer Corners', ha='center', color='#d73027', fontsize=6.2, fontweight='bold')
ax.axis('off')

# Panel b: APH Opposing Jets Updraft
ax = axs[0, 1]
ax.set_title('b  APH Opposing Cross-Jets Updraft', loc='left', fontweight='bold')
ax.add_patch(patches.Rectangle((0.1, 0.1), 0.8, 0.8, fill=True, color='#eff3ff', ec='#005696', lw=1.5))
ax.annotate('', xy=(0.45, 0.25), xytext=(0.12, 0.25), arrowprops=dict(arrowstyle="->", color='#005696', lw=2.5))
ax.annotate('', xy=(0.55, 0.25), xytext=(0.88, 0.25), arrowprops=dict(arrowstyle="->", color='#005696', lw=2.5))
ax.annotate('', xy=(0.5, 0.85), xytext=(0.5, 0.30), arrowprops=dict(arrowstyle="->", color='#005696', lw=3.0))
ax.text(0.5, 0.55, 'Sagittal Collision &\nUniform Upward Sweep', ha='center', color='#084594', fontsize=6.2, fontweight='bold')
ax.axis('off')

# Panel c: Wall Shear PDF
ax = axs[1, 0]
ax.set_title('c  Canopy Wall Shear Stress PDF', loc='left', fontweight='bold')
tau = np.linspace(0, 60, 200)
pdf_aph = np.exp(-((tau - 28.6)/8)**2)
pdf_veg = np.exp(-((tau - 12.0)/6)**2)
pdf_cara = np.exp(-((tau - 5.0)/3)**2)
ax.plot(tau, pdf_aph, label='APH (Mean 28.6 mPa)', color='#005696', lw=1.8)
ax.plot(tau, pdf_veg, label='VEGGIE (Mean 12.0 mPa)', color='#008080', lw=1.6)
ax.plot(tau, pdf_cara, label='CARA Dish (Mean 5.0 mPa)', color='#7570b3', lw=1.6)
ax.axvline(50, color='#c70039', linestyle='--', label='Leaf Damage Limit')
ax.set_xlabel('Wall Shear Stress $\\tau_w$ (mPa)')
ax.set_ylabel('Probability Density')
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='upper right', framealpha=0.9)

# Panel d: Spatial Uniformity
ax = axs[1, 1]
ax.set_title('d  Spatial Velocity Uniformity ($\\gamma_u$)', loc='left', fontweight='bold')
sys = ['VEGGIE (Low)', 'VEGGIE (High)', 'APH (Nominal)', 'CARA Dish', 'CHROMEX']
unif = [0.42, 0.68, 0.88, 0.55, 0.22]
bars_u = ax.bar(range(5), unif, color=['#d73027', '#fee08b', '#1a9850', '#fee08b', '#d73027'], edgecolor='#333333', linewidth=0.6, width=0.55)
ax.set_xticks(range(5))
ax.set_xticklabels(sys, rotation=20, ha='right', fontsize=6.5)
ax.set_ylabel('Uniformity Index $\\gamma_u$ (0-1)')
ax.set_ylim(0, 1.1)
ax.grid(axis='y', linestyle=':', alpha=0.6)
for b, val in zip(bars_u, unif):
    ax.text(b.get_x() + b.get_width()/2, val + 0.03, f'{val:.2f}', ha='center', va='bottom', fontsize=5.8, fontweight='bold')

out_dir = Path(__file__).resolve().parent / 'output'
plt.savefig(out_dir / 'Fig6_3d_flow_topologies.pdf', bbox_inches='tight')
plt.savefig(out_dir / 'Fig6_3d_flow_topologies.png', bbox_inches='tight', dpi=300)
plt.close()
print("Fig6 regenerated clean.")
