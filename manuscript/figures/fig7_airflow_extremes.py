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

# Panel a: Operational Velocities Across Fan Regimes
ax = axs[0, 0]
ax.set_title('a  Operational Regimes & Canopy Velocities', loc='left', fontweight='bold')
modes = ['Stagnation (0 rpm)', 'Low Draft (30%)', 'Nominal (100%)', 'High Blast (150%)']
u_veg = [0.0, 0.065, 0.150, 0.220]
u_aph = [0.0, 0.300, 0.600, 1.500]
x = np.arange(4)
w = 0.35
ax.bar(x - w/2, u_veg, width=w, color='#008080', label='VEGGIE (VPS)')
ax.bar(x + w/2, u_aph, width=w, color='#005696', label='APH Phytotron')
ax.axhline(0.05, color='#d73027', linestyle=':', label='Stagnation Limit (0.05 m/s)')
ax.axhline(0.50, color='#1a9850', linestyle='--', label='Ideal Agronomic Window (0.3-0.8 m/s)')
ax.set_xticks(x)
ax.set_xticklabels(modes, rotation=15, ha='right', fontsize=6.5)
ax.set_ylabel('Canopy Velocity $U$ (m/s)')
ax.grid(axis='y', linestyle=':', alpha=0.6)
ax.legend(loc='upper left', fontsize=6)

# Panel b: Stagnant Volume Reduction with Fan Speed
ax = axs[0, 1]
ax.set_title('b  Stagnant Volume vs Fan Speed', loc='left', fontweight='bold')
rpm_pct = np.linspace(0, 150, 100)
stag_veg = 100.0 / (1.0 + (rpm_pct / 32.0)**2.2)
stag_aph = 100.0 / (1.0 + (rpm_pct / 15.0)**3.0)
ax.plot(rpm_pct, stag_veg, label='VEGGIE', color='#008080', lw=1.8)
ax.plot(rpm_pct, stag_aph, label='APH', color='#005696', lw=1.8)
ax.axhline(10.0, color='#1a9850', linestyle='--', label='Acceptable Zone (< 10%)')
ax.set_xlabel('Fan Speed Setting (% Nominal)')
ax.set_ylabel('Stagnant Volume Fraction (%)')
ax.set_ylim(0, 105)
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='upper right')

# Panel c: CO2 Conductance Response (g_bl)
ax = axs[1, 0]
ax.set_title('c  Conductance ($g_{bl}$) Across Operating Modes', loc='left', fontweight='bold')
g_veg = [0.028, 0.219, 0.515, 0.680]
g_aph = [0.042, 0.720, 1.071, 1.745]
ax.bar(x - w/2, g_veg, width=w, color='#008080', label='VEGGIE')
ax.bar(x + w/2, g_aph, width=w, color='#005696', label='APH')
ax.axhline(0.25, color='#d73027', linestyle='--', label='Hypoxia Limit')
ax.set_xticks(x)
ax.set_xticklabels(modes, rotation=15, ha='right', fontsize=6.5)
ax.set_ylabel('$g_{bl}$ (mol m⁻² s⁻¹)')
ax.grid(axis='y', linestyle=':', alpha=0.6)
ax.legend(loc='upper left', fontsize=6)

# Panel d: Electrical Fan Power vs Conductance Return
ax = axs[1, 1]
ax.set_title('d  Aerodynamic Conductance vs Fan Power', loc='left', fontweight='bold')
power_veg = [0.0, 1.8, 8.5, 22.0]
power_aph = [0.0, 4.5, 18.0, 55.0]
ax.plot(power_veg, g_veg, 'o-', label='VEGGIE', color='#008080', lw=1.6)
ax.plot(power_aph, g_aph, 's-', label='APH', color='#005696', lw=1.6)
ax.set_xlabel('Fan Power Consumption (W)')
ax.set_ylabel('Boundary Layer $g_{bl}$ (mol m⁻² s⁻¹)')
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='lower right')

out_dir = Path(__file__).resolve().parent / 'output'
plt.savefig(out_dir / 'Fig7_airflow_extremes.pdf', bbox_inches='tight')
plt.savefig(out_dir / 'Fig7_airflow_extremes.png', bbox_inches='tight', dpi=300)
print("Fig7 generated successfully!")
