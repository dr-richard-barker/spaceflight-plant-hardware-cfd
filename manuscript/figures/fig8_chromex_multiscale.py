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

# Panel a: CHROMEX PGU Macro Thermal-Fluid Balance
ax = axs[0, 0]
ax.set_title('a  CHROMEX PGU Chassis Heat Dissipation', loc='left', fontweight='bold')
components = ['Lamp Bank\n(Fluorescent)', 'Ballast &\nAvionics', '6 PGC Canister\nHeadspaces', 'Root Foam\nMatrices']
q_watts = [38.5, 18.2, 8.4, 2.1]
c_bars = ['#d73027', '#fc8d59', '#fee08b', '#91bfdb']
bars_a = ax.bar(range(4), q_watts, color=c_bars, edgecolor='#333333', linewidth=0.6, width=0.55)
ax.set_xticks(range(4))
ax.set_xticklabels(components, rotation=15, ha='right', fontsize=6.5)
ax.set_ylabel('Thermal Load (W)')
ax.set_ylim(0, 45)
ax.grid(axis='y', linestyle=':', alpha=0.6)
for b, val in zip(bars_a, q_watts):
    ax.text(b.get_x() + b.get_width()/2, val + 1, f'{val:.1f}W', ha='center', va='bottom', fontsize=6, fontweight='bold')

# Panel b: Micro-Scale PGC Creeping Velocity Profile u(y)
ax = axs[0, 1]
ax.set_title('b  PGC Micro-Scale Flow ($Q = 1.0$ L/h AES)', loc='left', fontweight='bold')
y = np.linspace(-24, 24, 100)
u_aes = 0.0098 * (1 - (y/24)**2) # Poiseuille creeping profile
u_diff = np.zeros_like(y)
ax.plot(u_aes * 1000, y, label='Active AES ($1.0$ L/h)', color='#d95f02', lw=1.8)
ax.plot(u_diff * 1000, y, label='Static Sealed ($0$ L/h)', color='#7570b3', linestyle='--', lw=1.5)
ax.set_xlabel('Creeping Velocity $u$ (mm/s)')
ax.set_ylabel('Canister Lateral Position $y$ (mm)')
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='upper right')

# Panel c: Root-Zone O2 Depletion vs Depth (Brinkman-Darcy)
ax = axs[1, 0]
ax.set_title('c  Root Matrix $O_2$ Concentration vs Depth', loc='left', fontweight='bold')
z_depth = np.linspace(0, 40, 100)
# Diffusion-reaction in porous foam: C(z) = C0 * cosh(k*(L-z)) / cosh(k*L)
k_diff = 0.065
o2_1g = 20.9 * np.cosh(k_diff * (40 - z_depth)) / np.cosh(k_diff * 40)
o2_0g_aes = 12.4 * np.cosh(k_diff * 1.4 * (40 - z_depth)) / np.cosh(k_diff * 1.4 * 40)
o2_0g_sealed = 4.5 * np.cosh(k_diff * 2.0 * (40 - z_depth)) / np.cosh(k_diff * 2.0 * 40)

ax.plot(o2_1g, z_depth, label='1.0g Buoyant Convection', color='#4575b4', lw=1.6)
ax.plot(o2_0g_aes, z_depth, label='0g AES Creeping ($1.0$ L/h)', color='#d95f02', lw=1.8)
ax.plot(o2_0g_sealed, z_depth, label='0g Static Sealed Canister', color='#d73027', linestyle='--', lw=1.8)
ax.axvline(2.0, color='#c70039', linestyle=':', label='Acute Hypoxia Limit (2% $O_2$)')
ax.set_xlabel('Intercellular $O_2$ Concentration (%)')
ax.set_ylabel('Root Matrix Depth $z$ (mm)')
ax.invert_yaxis()
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='lower right', fontsize=6)

# Panel d: Transcriptomic ADH Induction Linkage
ax = axs[1, 1]
ax.set_title('d  Historical Flight ADH Transcript Upregulation', loc='left', fontweight='bold')
flight_conds = ['Ground Control\n(1.0g)', '0g Flight AES\n(Active Flow)', '0g Flight Sealed\n(Static)', '0g High Hypoxia\n(Anoxia)']
adh_fold = [1.0, 3.8, 14.2, 28.5]
bars_d = ax.bar(range(4), adh_fold, color=['#4575b4', '#fee08b', '#fc8d59', '#d73027'], edgecolor='#333333', linewidth=0.6, width=0.55)
ax.set_xticks(range(4))
ax.set_xticklabels(flight_conds, rotation=15, ha='right', fontsize=6.5)
ax.set_ylabel('Alcohol Dehydrogenase (ADH) Fold Induction')
ax.grid(axis='y', linestyle=':', alpha=0.6)
for b, val in zip(bars_d, adh_fold):
    ax.text(b.get_x() + b.get_width()/2, val + 0.8, f'{val:.1f}x', ha='center', va='bottom', fontsize=6, fontweight='bold')

out_dir = Path(__file__).resolve().parent / 'output'
plt.savefig(out_dir / 'Fig8_chromex_multiscale_hypoxia.pdf', bbox_inches='tight')
plt.savefig(out_dir / 'Fig8_chromex_multiscale_hypoxia.png', bbox_inches='tight', dpi=300)
print("Fig8 generated successfully!")
