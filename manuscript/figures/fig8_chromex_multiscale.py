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
plt.rcParams['legend.fontsize'] = 6.2

fig, axs = plt.subplots(2, 2, figsize=(7.2, 6.0), dpi=300)
plt.subplots_adjust(hspace=0.42, wspace=0.32)

# Panel a: PGU Chassis Thermal Budget
ax = axs[0, 0]
ax.set_title('a  PGU Chassis Thermal Budget', loc='left', fontweight='bold')
comps = ['Lamps\n(Fluorescent)', 'Ballasts', 'Avionics\nElectronics', 'PGC\nConduction', 'Fan Reject']
q_vals = [25.0, 8.5, 5.0, 4.2, 38.5]
c_bars = ['#d95f02', '#fdae61', '#fee08b', '#abd9e9', '#2c7bb6']
bars_a = ax.bar(range(5), q_vals, color=c_bars, edgecolor='#333333', linewidth=0.6, width=0.55)
ax.set_xticks(range(5))
ax.set_xticklabels(comps, rotation=20, ha='right', fontsize=6.5)
ax.set_ylabel('Thermal Power (W)')
ax.set_ylim(0, 45)
ax.grid(axis='y', linestyle=':', alpha=0.6)
for b, val in zip(bars_a, q_vals):
    ax.text(b.get_x() + b.get_width()/2, val + 1, f'{val:.1f}W', ha='center', va='bottom', fontsize=5.8, fontweight='bold')

# Panel b: PGC Canister Velocity Profile
ax = axs[0, 1]
ax.set_title('b  PGC Creeping Velocity Profile $u(y)$', loc='left', fontweight='bold')
y = np.linspace(0, 48, 100)
u_aes = 0.008 * np.sin(np.pi * y / 48)
u_static = 0.0005 * np.sin(np.pi * y / 48)
ax.plot(u_aes * 1000, y, label='Active AES (1.0 L/h)', color='#d95f02', lw=1.8)
ax.plot(u_static * 1000, y, label='Static Sealed Canister', color='#333333', linestyle='--', lw=1.5)
ax.set_xlabel('Velocity Magnitude (mm/s)')
ax.set_ylabel('Canister Lateral Width $y$ (mm)')
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='upper right', framealpha=0.9)

# Panel c: Root Matrix O2 vs Depth
ax = axs[1, 0]
ax.set_title('c  Root Matrix $O_2$ Concentration vs Depth', loc='left', fontweight='bold')
depth = np.linspace(0, 30, 100)
o2_1g = 20.9 - 4.5 * (depth / 30)**1.2
o2_0g_aes = 20.9 - 14.0 * (depth / 30)**0.9
o2_0g_sealed = 20.9 - 19.5 * (depth / 30)**0.6
ax.plot(o2_1g, depth, label='1g Earth Control', color='#4575b4', lw=1.8)
ax.plot(o2_0g_aes, depth, label='0g AES Active', color='#d95f02', lw=1.8)
ax.plot(o2_0g_sealed, depth, label='0g Static Sealed', color='#c70039', linestyle='--', lw=1.8)
ax.axvline(5.0, color='gray', linestyle=':', label='Hypoxia Limit (5% $O_2$)')
ax.set_xlabel('$O_2$ Concentration (%)')
ax.set_ylabel('Root Matrix Depth $z$ (mm)')
ax.set_ylim(30, 0)
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='lower left', framealpha=0.9)

# Panel d: CHROMEX-03 Flight ADH Transcriptomics
ax = axs[1, 1]
ax.set_title('d  CHROMEX-03 Flight $ADH$ Induction', loc='left', fontweight='bold')
genes = ['1g Ground\nBaseline', 'Flight AES\n(Active)', 'Flight Sealed\n(Historical)']
adh_fold = [1.0, 14.2, 28.5]
c_adh = ['#4575b4', '#d95f02', '#c70039']
bars_d = ax.bar(range(3), adh_fold, color=c_adh, edgecolor='#333333', linewidth=0.6, width=0.55)
ax.set_xticks(range(3))
ax.set_xticklabels(genes, rotation=15, ha='right', fontsize=6.5)
ax.set_ylabel('ADH Transcript Fold Induction')
ax.set_ylim(0, 35)
ax.grid(axis='y', linestyle=':', alpha=0.6)
for b, val in zip(bars_d, adh_fold):
    ax.text(b.get_x() + b.get_width()/2, val + 1, f'{val:.1f}x', ha='center', va='bottom', fontsize=6, fontweight='bold')

out_dir = Path(__file__).resolve().parent / 'output'
plt.savefig(out_dir / 'Fig8_chromex_multiscale_hypoxia.pdf', bbox_inches='tight')
plt.savefig(out_dir / 'Fig8_chromex_multiscale_hypoxia.png', bbox_inches='tight', dpi=300)
plt.close()
print("Fig8 regenerated clean.")
