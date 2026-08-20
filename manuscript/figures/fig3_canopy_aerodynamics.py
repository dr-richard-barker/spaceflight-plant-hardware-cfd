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
plt.rcParams['legend.fontsize'] = 6.0

fig, axs = plt.subplots(2, 2, figsize=(7.2, 6.0), dpi=300)
plt.subplots_adjust(hspace=0.42, wspace=0.32)

# Panel a: Velocity profiles u(z)
ax = axs[0, 0]
ax.set_title('a  Canopy Velocity Profiles $u(z)$', loc='left', fontweight='bold')
z = np.linspace(0, 50, 100)
u_aph = 0.60 * (1 - np.exp(-z/5))
u_veg_high = 0.15 * (1 - np.exp(-z/8))
u_veg_low = 0.065 * (1 - np.exp(-z/12))
u_cara = 0.082 * (1 - np.exp(-z/7))

ax.plot(u_aph, z, label='APH (0.6 m/s)', color='#005696', lw=1.8)
ax.plot(u_veg_high, z, label='VEGGIE High', color='#008080', lw=1.6)
ax.plot(u_veg_low, z, label='VEGGIE Low', color='#008080', linestyle='--', lw=1.6)
ax.plot(u_cara, z, label='CARA Draft', color='#7570b3', lw=1.6)
ax.set_xlabel('Velocity Magnitude (m/s)')
ax.set_ylabel('Height Above Root Matrix $z$ (mm)')
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='lower right', framealpha=0.9)

# Panel b: g_bl vs forced velocity
ax = axs[0, 1]
ax.set_title('b  Boundary Layer Conductance ($g_{bl}$)', loc='left', fontweight='bold')
u_sweep = np.linspace(0.01, 1.5, 100)
g_bl_model = 0.04 + 1.4 * np.sqrt(u_sweep)
ax.plot(u_sweep, g_bl_model, color='#111111', lw=1.5, label='Model ($g_{bl} \propto \sqrt{U}$)')
ax.scatter([0.60, 1.50], [1.071, 1.745], color='#005696', s=35, label='APH (Nom/High)', zorder=5)
ax.scatter([0.065, 0.150], [0.219, 0.515], color='#008080', s=35, label='VEGGIE (Low/High)', zorder=5)
ax.scatter([0.082], [0.326], color='#7570b3', s=35, label='CARA (+Light)', zorder=5)
ax.scatter([0.005], [0.031], color='#d95f02', s=35, label='CHROMEX', zorder=5)
ax.axhline(0.25, color='#c70039', linestyle='--', lw=1.0, label='Hypoxia Limit')
ax.set_xlabel('Forced Canopy Velocity $U$ (m/s)')
ax.set_ylabel('$g_{bl}$ (mol m⁻² s⁻¹)')
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='upper left', fontsize=5.5, ncol=2, framealpha=0.9)

# Panel c: Canopy Stagnant Volume Fraction (%)
ax = axs[1, 0]
ax.set_title('c  Canopy Stagnant Volume ($U < 0.05$ m/s)', loc='left', fontweight='bold')
sys_short = ['VEG-L', 'VEG-H', 'APH', 'CARA', 'CHR', 'BRIC']
stag = [52.8, 15.4, 2.6, 38.2, 100.0, 92.0]
c_list = ['#d73027', '#fee08b', '#1a9850', '#fee08b', '#d73027', '#d73027']
bars = ax.bar(range(6), stag, color=c_list, edgecolor='#333333', linewidth=0.6, width=0.55)
ax.set_xticks(range(6))
ax.set_xticklabels(sys_short, rotation=0, fontsize=6.5)
ax.set_ylabel('Stagnant Fraction (%)')
ax.set_ylim(0, 120)
ax.grid(axis='y', linestyle=':', alpha=0.6)
for b, val in zip(bars, stag):
    ax.text(b.get_x() + b.get_width()/2, val + 2, f'{val:.1f}%', ha='center', va='bottom', fontsize=5.8, fontweight='bold')

# Panel d: Wall Shear Stress (tau_w)
ax = axs[1, 1]
ax.set_title('d  Vegetative Surface Shear Stress ($\tau_w$)', loc='left', fontweight='bold')
tau = [5.4, 18.2, 28.6, 12.4, 0.2, 0.05]
bars_t = ax.bar(range(6), tau, color=['#008080', '#008080', '#005696', '#7570b3', '#d95f02', '#e7298a'], edgecolor='#333333', linewidth=0.6, width=0.55)
ax.axhline(50.0, color='#c70039', linestyle='--', label='Damage Limit (50 mPa)')
ax.set_xticks(range(6))
ax.set_xticklabels(sys_short, rotation=0, fontsize=6.5)
ax.set_ylabel('Wall Shear $\tau_w$ (mPa)')
ax.set_ylim(0, 60)
ax.grid(axis='y', linestyle=':', alpha=0.6)
ax.legend(loc='upper right', framealpha=0.9)
for b, val in zip(bars_t, tau):
    ax.text(b.get_x() + b.get_width()/2, val + 1.2, f'{val:.1f}', ha='center', va='bottom', fontsize=5.8, fontweight='bold')

out_dir = Path(__file__).resolve().parent / 'output'
plt.savefig(out_dir / 'Fig3_canopy_aerodynamics.pdf', bbox_inches='tight')
plt.savefig(out_dir / 'Fig3_canopy_aerodynamics.png', bbox_inches='tight', dpi=300)
plt.close()
print("Fig3 regenerated clean.")
