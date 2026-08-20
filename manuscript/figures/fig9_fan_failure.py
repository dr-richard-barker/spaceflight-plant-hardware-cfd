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

# Panel a: Spin-down decay
ax = axs[0, 0]
ax.set_title('a  Fan Spin-Down Velocity Decay $U(t)$', loc='left', fontweight='bold')
t = np.linspace(0, 20, 200)
u_aph = 0.60 * np.exp(-t / 4.8)
u_veg = 0.15 * np.exp(-t / 2.4)
u_chr = 0.008 * np.exp(-t / 0.8)
ax.plot(t, u_aph, label='APH ($\tau = 4.8$s)', color='#005696', lw=1.8)
ax.plot(t, u_veg, label='VEGGIE ($\tau = 2.4$s)', color='#008080', lw=1.6)
ax.plot(t, u_chr, label='CHROMEX ($\tau = 0.8$s)', color='#d95f02', lw=1.6)
ax.axhline(0.05, color='#c70039', linestyle='--', label='Stagnation Limit (0.05 m/s)')
ax.set_xlabel('Time Post-Cutoff $t$ (s)')
ax.set_ylabel('Canopy Velocity $U$ (m/s)')
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='upper right', framealpha=0.9)

# Panel b: Conductance collapse across gravities
ax = axs[0, 1]
ax.set_title('b  Conductance Collapse across Gravities', loc='left', fontweight='bold')
t_min = np.linspace(0, 15, 200)
g_1g = 0.362 + (1.071 - 0.362) * np.exp(-t_min / 0.2)
g_mars = 0.180 + (1.071 - 0.180) * np.exp(-t_min / 0.2)
g_moon = 0.095 + (1.071 - 0.095) * np.exp(-t_min / 0.2)
g_0g = 0.042 + (1.071 - 0.042) * np.exp(-t_min / 0.2)
ax.plot(t_min, g_1g, label='Earth 1.0g (Buoyancy Floor)', color='#4575b4', lw=1.8)
ax.plot(t_min, g_mars, label='Mars 0.38g', color='#fdae61', lw=1.6)
ax.plot(t_min, g_moon, label='Moon 0.166g', color='#fee08b', lw=1.6)
ax.plot(t_min, g_0g, label='0g Microgravity (Collapse)', color='#d73027', lw=1.8)
ax.axhline(0.25, color='gray', linestyle=':', label='Hypoxia Limit')
ax.set_xlabel('Time Post-Shutdown (min)')
ax.set_ylabel('$g_{bl}$ (mol m⁻² s⁻¹)')
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='upper right', framealpha=0.9)

# Panel c: Thermal accumulation
ax = axs[1, 0]
ax.set_title('c  Canopy Thermal Accumulation ($\Delta T$)', loc='left', fontweight='bold')
dT_1g = 2.4 * (1 - np.exp(-t_min / 4.0))
dT_0g_aph = 5.8 * (1 - np.exp(-t_min / 3.0))
dT_0g_veg = 6.9 * (1 - np.exp(-t_min / 2.5))
dT_0g_chr = 8.4 * (1 - np.exp(-t_min / 2.0))
ax.plot(t_min, dT_1g, label='Earth 1g Buoyant Equilibrium', color='#4575b4', lw=1.8)
ax.plot(t_min, dT_0g_aph, label='0g APH (+5.8 K)', color='#005696', lw=1.6)
ax.plot(t_min, dT_0g_veg, label='0g VEGGIE (+6.9 K)', color='#008080', lw=1.6)
ax.plot(t_min, dT_0g_chr, label='0g CHROMEX (+8.4 K)', color='#d95f02', lw=1.6)
ax.set_xlabel('Time Post-Shutdown (min)')
ax.set_ylabel('Canopy Temperature Rise $\Delta T$ (K)')
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='lower right', framealpha=0.9)

# Panel d: Intercellular CO2 drawdown & Photorespiration
ax = axs[1, 1]
ax.set_title('d  $C_i$ Drawdown & RuBisCO Surge', loc='left', fontweight='bold')
ci = 400 * np.exp(-t_min / 1.5) + 80
vo_vc = 2 * 42.0 / np.maximum(ci, 10.0)
ax.plot(t_min, ci, label='Intercellular $C_i$ (ppm)', color='#313695', lw=1.8)
ax2 = ax.twinx()
ax2.plot(t_min, vo_vc, label='RuBisCO $v_o/v_c$ Ratio', color='#c70039', lw=1.8, linestyle='--')
ax.axhline(150, color='gray', linestyle=':', label='Starvation Limit')
ax.set_xlabel('Time Post-Shutdown (min)')
ax.set_ylabel('$C_i$ (ppm)', color='#313695')
ax2.set_ylabel('RuBisCO $v_o/v_c$', color='#c70039')
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='upper right', framealpha=0.9)

out_dir = Path(__file__).resolve().parent / 'output'
plt.savefig(out_dir / 'Fig9_fan_failure_dynamics.pdf', bbox_inches='tight')
plt.savefig(out_dir / 'Fig9_fan_failure_dynamics.png', bbox_inches='tight', dpi=300)
plt.close()
print("Fig9 regenerated clean.")
