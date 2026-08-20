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

g_vals = np.linspace(0, 9.81, 100)

# Grashof & Reynolds
# VEGGIE
Gr_veg = 1.83e7 * (g_vals / 9.81)
Re_veg = 3463
Ri_veg = Gr_veg / (Re_veg**2)

# APH
Gr_aph = 3.90e7 * (g_vals / 9.81)
Re_aph = 17810
Ri_aph = Gr_aph / (Re_aph**2)

# CHROMEX
Gr_chr = 1.98e6 * (g_vals / 9.81)
Re_chr = 123
Ri_chr = Gr_chr / (Re_chr**2)

# CARA (+Light)
Gr_cara = 4.20e5 * (g_vals / 9.81)
Re_cara = 1150
Ri_cara = Gr_cara / (Re_cara**2)

# Panel a: Ri vs g
ax = axs[0, 0]
ax.set_title('a  Richardson Number ($Ri$) vs Gravity', loc='left', fontweight='bold')
ax.plot(g_vals, Ri_veg, label='VEGGIE (VPS)', color='#008080', lw=1.8)
ax.plot(g_vals, Ri_aph, label='APH (0.6 m/s)', color='#005696', lw=1.8)
ax.plot(g_vals, Ri_cara, label='CARA (+Light)', color='#7570b3', lw=1.8)
ax.axhline(0.1, color='gray', linestyle=':', label='Forced Limit ($Ri=0.1$)')
ax.axhline(1.0, color='gray', linestyle='--', label='Mixed Crossover ($Ri=1$)')
ax.set_xlabel('Gravitational Acceleration $g$ (m/s²)')
ax.set_ylabel('Richardson Number $Ri = Gr/Re^2$')
ax.set_yscale('log')
ax.set_ylim(1e-4, 10)
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='lower right', framealpha=0.9)

# Panel b: Convective Regime Trajectories
ax = axs[0, 1]
ax.set_title('b  Convective Regime Trajectories', loc='left', fontweight='bold')
gravs = ['0g (Microgravity)', '0.166g (Moon)', '0.38g (Mars)', '1.0g (Earth)']
x = np.arange(4)
ax.plot(x, [0, 0.256, 0.588, 1.551], 'o-', label='VEGGIE', color='#008080', lw=1.6)
ax.plot(x, [0, 0.021, 0.047, 0.125], 's-', label='APH', color='#005696', lw=1.6)
ax.plot(x, [0, 0.052, 0.120, 0.318], '^-', label='CARA (+Light)', color='#7570b3', lw=1.6)
ax.axhspan(0, 0.1, color='#e8f5e9', alpha=0.6, label='Purely Forced')
ax.axhspan(0.1, 1.0, color='#fff9c4', alpha=0.6, label='Mixed Convection')
ax.axhspan(1.0, 2.0, color='#ffebee', alpha=0.6, label='Buoyancy Dominated')
ax.set_xticks(x)
ax.set_xticklabels(gravs, rotation=15, ha='right', fontsize=6.5)
ax.set_ylabel('Richardson Number $Ri$')
ax.set_ylim(0, 1.8)
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='upper left', fontsize=6)

# Panel c: Thermal Stratification Collapse
ax = axs[1, 0]
ax.set_title('c  Thermal Stratification ($\Delta T_{vert}$)', loc='left', fontweight='bold')
dT_1g = [2.4, 0.4, 6.5, 1.8, 5.4]
dT_0g = [0.8, 0.2, 8.4, 0.5, 6.8]
sys = ['VEGGIE', 'APH', 'CHROMEX', 'CARA', 'BRIC-LED']
xx = np.arange(5)
w = 0.35
ax.bar(xx - w/2, dT_1g, width=w, color='#4575b4', label='Earth 1.0g')
ax.bar(xx + w/2, dT_0g, width=w, color='#d73027', label='Microgravity 0g')
ax.set_xticks(xx)
ax.set_xticklabels(sys, rotation=20, ha='right', fontsize=6.5)
ax.set_ylabel('Vertical $\Delta T$ (K)')
ax.legend(loc='upper left')
ax.grid(axis='y', linestyle=':', alpha=0.6)

# Panel d: TKE Enhancement in 0g
ax = axs[1, 1]
ax.set_title('d  Canopy Turbulent Kinetic Energy', loc='left', fontweight='bold')
tke_1g = [1.12e-3, 1.24e-2, 2.5e-5, 1.20e-3, 1.1e-6]
tke_0g = [0.68e-3, 1.19e-2, 1.0e-5, 0.95e-3, 1.0e-7]
ax.bar(xx - w/2, tke_1g, width=w, color='#4575b4', label='Earth 1.0g')
ax.bar(xx + w/2, tke_0g, width=w, color='#d73027', label='Microgravity 0g')
ax.set_yscale('log')
ax.set_xticks(xx)
ax.set_xticklabels(sys, rotation=20, ha='right', fontsize=6.5)
ax.set_ylabel('TKE (m²/s², log scale)')
ax.legend(loc='upper right')
ax.grid(axis='y', linestyle=':', alpha=0.6)

out_dir = Path(__file__).resolve().parent / 'output'
plt.savefig(out_dir / 'Fig2_gravity_richardson.pdf', bbox_inches='tight')
plt.savefig(out_dir / 'Fig2_gravity_richardson.png', bbox_inches='tight', dpi=300)
print("Fig2 generated successfully!")
