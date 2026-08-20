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

modes = ['Zero Airflow\n(Fan Stop)', 'Low Draft\n(Flight Min)', 'Nominal\n(Baseline)', 'High Blast\n(Max Blower)']
x = np.arange(4)

# Panel a: Operational Canopy Velocity
ax = axs[0, 0]
ax.set_title('a  Operational Canopy Velocities (m/s)', loc='left', fontweight='bold')
ax.plot(x, [0.0, 0.065, 0.150, 0.320], 'o-', label='VEGGIE (VPS)', color='#008080', lw=1.8)
ax.plot(x, [0.0, 0.300, 0.600, 1.500], 's-', label='APH Phytotron', color='#005696', lw=1.8)
ax.plot(x, [0.0, 0.015, 0.082, 0.120], '^-', label='CARA Dish', color='#7570b3', lw=1.6)
ax.set_xticks(x)
ax.set_xticklabels(modes, rotation=15, ha='right', fontsize=6.5)
ax.set_ylabel('Velocity $U$ (m/s)')
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='upper left', framealpha=0.9)

# Panel b: Stagnant Volume Reduction
ax = axs[0, 1]
ax.set_title('b  Stagnant Volume Reduction (%)', loc='left', fontweight='bold')
ax.plot(x, [100.0, 52.8, 15.4, 4.2], 'o-', label='VEGGIE', color='#008080', lw=1.8)
ax.plot(x, [100.0, 12.5, 2.6, 0.4], 's-', label='APH', color='#005696', lw=1.8)
ax.plot(x, [100.0, 65.0, 38.2, 18.5], '^-', label='CARA', color='#7570b3', lw=1.6)
ax.set_xticks(x)
ax.set_xticklabels(modes, rotation=15, ha='right', fontsize=6.5)
ax.set_ylabel('Canopy Stagnant Volume (%)')
ax.set_ylim(0, 110)
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='upper right', framealpha=0.9)

# Panel c: Conductance Dynamic Range
ax = axs[1, 0]
ax.set_title('c  Conductance $g_{bl}$ Dynamic Range', loc='left', fontweight='bold')
ax.plot(x, [0.028, 0.219, 0.515, 0.820], 'o-', label='VEGGIE', color='#008080', lw=1.8)
ax.plot(x, [0.042, 0.720, 1.071, 1.745], 's-', label='APH', color='#005696', lw=1.8)
ax.plot(x, [0.015, 0.120, 0.326, 0.450], '^-', label='CARA', color='#7570b3', lw=1.6)
ax.axhline(0.25, color='#c70039', linestyle='--', label='Hypoxia Limit')
ax.set_xticks(x)
ax.set_xticklabels(modes, rotation=15, ha='right', fontsize=6.5)
ax.set_ylabel('$g_{bl}$ (mol m⁻² s⁻¹)')
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='upper left', framealpha=0.9)

# Panel d: Electrical Power vs Conductance
ax = axs[1, 1]
ax.set_title('d  Electrical Power vs $g_{bl}$', loc='left', fontweight='bold')
pwr_aph = [0, 4.5, 12.0, 48.0]
pwr_veg = [0, 1.2, 3.5, 8.5]
ax.plot(pwr_aph, [0.042, 0.720, 1.071, 1.745], 's-', label='APH', color='#005696', lw=1.8)
ax.plot(pwr_veg, [0.028, 0.219, 0.515, 0.820], 'o-', label='VEGGIE', color='#008080', lw=1.8)
ax.set_xlabel('Blower / Fan Electrical Power (W)')
ax.set_ylabel('$g_{bl}$ (mol m⁻² s⁻¹)')
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='lower right', framealpha=0.9)

out_dir = Path(__file__).resolve().parent / 'output'
plt.savefig(out_dir / 'Fig7_airflow_extremes.pdf', bbox_inches='tight')
plt.savefig(out_dir / 'Fig7_airflow_extremes.png', bbox_inches='tight', dpi=300)
plt.close()
print("Fig7 regenerated clean.")
