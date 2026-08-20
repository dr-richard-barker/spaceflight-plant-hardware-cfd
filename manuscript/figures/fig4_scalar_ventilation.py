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

# Panel a: Local Mean Age of Air (LMA) distributions
ax = axs[0, 0]
ax.set_title('a  Canopy Mean Age of Air (LMA)', loc='left', fontweight='bold')
sys = ['VEGGIE (Low)', 'VEGGIE (High)', 'APH (0.6 m/s)', 'APH (1.5 m/s)', 'CARA (+Light)']
lma = [12.4, 3.8, 12.6, 5.1, 45.0]
bars = ax.bar(range(5), lma, color=['#d73027', '#fee08b', '#4575b4', '#313695', '#7570b3'], edgecolor='#333333', linewidth=0.6, width=0.55)
ax.set_xticks(range(5))
ax.set_xticklabels(sys, rotation=20, ha='right', fontsize=6.5)
ax.set_ylabel('Mean Age of Air $\\tau_{LMA}$ (s)')
ax.grid(axis='y', linestyle=':', alpha=0.6)
for b, val in zip(bars, lma):
    ax.text(b.get_x() + b.get_width()/2, val + 1, f'{val:.1f}s', ha='center', va='bottom', fontsize=6, fontweight='bold')

# Panel b: Transient Chamber Flushing Curves
ax = axs[0, 1]
ax.set_title('b  Transient Scalar Flushing Kinetics', loc='left', fontweight='bold')
t = np.linspace(0, 60, 150)
c_aph_nom = np.exp(-t / 11.35)
c_aph_high = np.exp(-t / 4.5)
c_veg_high = np.exp(-t / 1.6)
c_veg_low = 0.472 * np.exp(-t / 3.5) + 0.528 * np.exp(-t / 45.0) # Dead zone retention
ax.plot(t, c_aph_nom, label='APH Nominal ($\tau = 11.4$s)', color='#005696', lw=1.8)
ax.plot(t, c_aph_high, label='APH High Blast ($\tau = 4.5$s)', color='#313695', lw=1.6)
ax.plot(t, c_veg_high, label='VEGGIE High ($\tau = 1.6$s)', color='#008080', lw=1.6)
ax.plot(t, c_veg_low, label='VEGGIE Low (52.8% Stagnation)', color='#d73027', lw=1.8, linestyle='--')
ax.set_xlabel('Time $t$ (s)')
ax.set_ylabel('Normalized Canopy Tracer $C(t)/C_0$')
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='upper right')

# Panel c: Air Exchange Efficiency (epsilon_a)
ax = axs[1, 0]
ax.set_title('c  Air Exchange Efficiency ($\epsilon_a$)', loc='left', fontweight='bold')
eff = [14.2, 26.2, 45.0, 47.3, 18.5]
bars_e = ax.bar(range(5), eff, color=['#d73027', '#fee08b', '#4575b4', '#313695', '#7570b3'], edgecolor='#333333', linewidth=0.6, width=0.55)
ax.axhline(50.0, color='gray', linestyle='--', label='Ideal Piston Displacement (50%)')
ax.set_xticks(range(5))
ax.set_xticklabels(sys, rotation=20, ha='right', fontsize=6.5)
ax.set_ylabel('Air Exchange Efficiency $\epsilon_a$ (%)')
ax.set_ylim(0, 60)
ax.grid(axis='y', linestyle=':', alpha=0.6)
ax.legend(loc='upper left')
for b, val in zip(bars_e, eff):
    ax.text(b.get_x() + b.get_width()/2, val + 1.5, f'{val:.1f}%', ha='center', va='bottom', fontsize=6, fontweight='bold')

# Panel d: Flushing Half-Life (t_50)
ax = axs[1, 1]
ax.set_title('d  Canopy Clearing Half-Life ($t_{50}$)', loc='left', fontweight='bold')
t50 = [28.5, 1.1, 7.9, 3.1, 31.2]
bars_t = ax.bar(range(5), t50, color=['#d73027', '#fee08b', '#4575b4', '#313695', '#7570b3'], edgecolor='#333333', linewidth=0.6, width=0.55)
ax.set_xticks(range(5))
ax.set_xticklabels(sys, rotation=20, ha='right', fontsize=6.5)
ax.set_ylabel('Canopy $t_{50}$ Clearance Time (s)')
ax.grid(axis='y', linestyle=':', alpha=0.6)
for b, val in zip(bars_t, t50):
    ax.text(b.get_x() + b.get_width()/2, val + 1, f'{val:.1f}s', ha='center', va='bottom', fontsize=6, fontweight='bold')

out_dir = Path(__file__).resolve().parent / 'output'
plt.savefig(out_dir / 'Fig4_scalar_ventilation.pdf', bbox_inches='tight')
plt.savefig(out_dir / 'Fig4_scalar_ventilation.png', bbox_inches='tight', dpi=300)
print("Fig4 generated successfully!")
