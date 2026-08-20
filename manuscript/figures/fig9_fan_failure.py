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

# Panel a: Fan Spin-Down Velocity Decay U(t)
ax = axs[0, 0]
ax.set_title('a  Fan Cutoff Velocity Decay Curves $U(t)$', loc='left', fontweight='bold')
t = np.linspace(0, 20, 150)
u_veg = 0.15 * np.exp(-t / 2.4)
u_aph = 0.60 * np.exp(-t / 4.8)
u_chr = 0.01 * np.exp(-t / 0.8)
ax.plot(t, u_aph, label='APH ($\tau_{spin} = 4.8$s)', color='#005696', lw=1.8)
ax.plot(t, u_veg, label='VEGGIE ($\tau_{spin} = 2.4$s)', color='#008080', lw=1.6)
ax.plot(t, u_chr, label='CHROMEX ($\tau_{spin} = 0.8$s)', color='#d95f02', lw=1.6)
ax.axhline(0.01, color='gray', linestyle=':', label='Complete Stagnation Limit')
ax.set_xlabel('Time Post-Cutoff $t$ (s)')
ax.set_ylabel('Canopy Velocity $U(t)$ (m/s)')
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='upper right')

# Panel b: Conductance Collapse g_bl(t) Across Gravities
ax = axs[0, 1]
ax.set_title('b  $g_{bl}(t)$ Collapse Across Gravities', loc='left', fontweight='bold')
g_1g = 0.362 + (1.071 - 0.362) * np.exp(-t / 4.8)
g_mars = 0.180 + (1.071 - 0.180) * np.exp(-t / 4.8)
g_moon = 0.090 + (1.071 - 0.090) * np.exp(-t / 4.8)
g_0g = 0.042 + (1.071 - 0.042) * np.exp(-t / 4.8)

ax.plot(t, g_1g, label='Earth 1.0g (Buoyancy Floor)', color='#4575b4', lw=1.6)
ax.plot(t, g_mars, label='Mars 0.38g', color='#fee08b', lw=1.6)
ax.plot(t, g_moon, label='Moon 0.166g', color='#fc8d59', lw=1.6)
ax.plot(t, g_0g, label='Microgravity 0g (Collapse to Diffusion)', color='#d73027', lw=2.0)
ax.axhline(0.25, color='#c70039', linestyle='--', label='Hypoxia Limit')
ax.set_xlabel('Time Post-Cutoff $t$ (s)')
ax.set_ylabel('$g_{bl}(t)$ (mol m⁻² s⁻¹)')
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='upper right', fontsize=6)

# Panel c: Canopy Thermal Rise (Delta T)
ax = axs[1, 0]
ax.set_title('c  Canopy Thermal Accumulation Post-Shutdown', loc='left', fontweight='bold')
t_min = np.linspace(0, 30, 150)
dT_veg_0g = 6.9 * (1 - np.exp(-t_min / 5.2))
dT_aph_0g = 5.8 * (1 - np.exp(-t_min / 8.5))
dT_chr_0g = 8.4 * (1 - np.exp(-t_min / 3.1))
dT_1g = 2.4 * (1 - np.exp(-t_min / 4.0))

ax.plot(t_min, dT_chr_0g, label='CHROMEX (0g, Sealed)', color='#d95f02', lw=1.8)
ax.plot(t_min, dT_veg_0g, label='VEGGIE (0g)', color='#008080', lw=1.6)
ax.plot(t_min, dT_aph_0g, label='APH (0g)', color='#005696', lw=1.6)
ax.plot(t_min, dT_1g, label='Earth 1.0g (All Systems)', color='#4575b4', linestyle='--', lw=1.6)
ax.set_xlabel('Time Post-Cutoff (min)')
ax.set_ylabel('Canopy Temperature Rise $\Delta T$ (K)')
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='lower right')

# Panel d: Intercellular CO2 Drawdown (Ci) and RuBisCO Oxygenation
ax = axs[1, 1]
ax.set_title('d  Intercellular $CO_2$ & RuBisCO Waste ($v_o/v_c$)', loc='left', fontweight='bold')
ci_1g = 400 - (400 - 280) * (1 - np.exp(-t_min / 12.0))
ci_0g = 400 - (400 - 85) * (1 - np.exp(-t_min / 3.8))
ax.plot(t_min, ci_1g, label='Earth 1.0g ($C_i$ Buffer)', color='#4575b4', lw=1.6)
ax.plot(t_min, ci_0g, label='0g Microgravity ($C_i$ Collapse)', color='#d73027', lw=2.0)
ax.axhline(150, color='#c70039', linestyle=':', label='Severe $CO_2$ Starvation ($< 150$ ppm)')
ax.set_xlabel('Time Post-Cutoff (min)')
ax.set_ylabel('Intercellular $CO_2$ $C_i$ (ppm)')
ax.grid(True, linestyle=':', alpha=0.6)

ax2 = ax.twinx()
vo_vc = 2 * (42.0 / ci_0g) # RuBisCO kinetics: vo/vc = 2*Gamma*/Ci
ax2.plot(t_min, vo_vc, color='#7570b3', linestyle='-.', lw=1.5, label='RuBisCO $v_o/v_c$')
ax2.set_ylabel('Photorespiratory Waste $v_o/v_c$', color='#7570b3')
ax2.tick_params(axis='y', labelcolor='#7570b3')
ax.legend(loc='center right', fontsize=6)

out_dir = Path(__file__).resolve().parent / 'output'
plt.savefig(out_dir / 'Fig9_fan_failure_dynamics.pdf', bbox_inches='tight')
plt.savefig(out_dir / 'Fig9_fan_failure_dynamics.png', bbox_inches='tight', dpi=300)
print("Fig9 generated successfully!")
