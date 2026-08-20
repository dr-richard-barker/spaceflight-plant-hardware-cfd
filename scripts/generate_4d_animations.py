#!/usr/bin/env python3
"""
Generate 4D Animated Visualizations for Spaceflight Plant Hardware CFD Study
1. anim1_fan_cutoff_decay.gif: Dynamic velocity decay & conductance collapse across 4 gravities
2. anim2_spore_clearance.gif: Spore particle dispersion & HEPA scrubbing vs cabin export
3. anim3_petridish_gas_condensation.gif: Time-dependent O2, ethylene & condensation in CARA vs BRIC
4. anim4_canopy_turbulence_wave.gif: Cross-flow momentum collision & turbulence penetration with canopy growth
"""

import os
os.environ['MPLCONFIGDIR'] = '/tmp/mpl_config'
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches
import numpy as np
from pathlib import Path

plt.rcParams['font.sans-serif'] = 'Helvetica'
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 8.0

out_dirs = [
    Path(__file__).resolve().parent.parent / "visualizations" / "animations",
    Path(__file__).resolve().parent.parent / "docs" / "assets" / "animations"
]
for d in out_dirs:
    d.mkdir(parents=True, exist_ok=True)

# -------------------------------------------------------------
# ANIMATION 1: Fan Cutoff Velocity Decay & Conductance Collapse
# -------------------------------------------------------------
print("=== Generating Animation 1: Fan Cutoff Decay across Gravities ===")
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.0, 4.0), dpi=150)
fig.subplots_adjust(wspace=0.35, bottom=0.18, top=0.88)

t_eval = np.linspace(0, 10, 60) # 0 to 10 seconds

def init_anim1():
    ax1.clear()
    ax2.clear()
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 0.7)
    ax1.set_xlabel('Time Post-Cutoff (s)', fontweight='bold')
    ax1.set_ylabel('Canopy Velocity U (m/s)', fontweight='bold')
    ax1.set_title('a  Transient Fan Spin-Down Velocity Decay', loc='left', fontweight='bold', fontsize=8.5)
    ax1.grid(True, linestyle=':', alpha=0.6)
    ax1.axhline(0.05, color='#c70039', linestyle='--', label='Stagnation (0.05 m/s)')

    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 1.2)
    ax2.set_xlabel('Time Post-Cutoff (s)', fontweight='bold')
    ax2.set_ylabel('Conductance $g_{bl}$ (mol m⁻² s⁻¹)', fontweight='bold')
    ax2.set_title('b  Boundary Layer Conductance Floor', loc='left', fontweight='bold', fontsize=8.5)
    ax2.grid(True, linestyle=':', alpha=0.6)
    ax2.axhline(0.25, color='#c70039', linestyle=':', label='Hypoxia Limit')

def update_anim1(frame):
    init_anim1()
    curr_t = t_eval[:frame+1]
    
    # Velocity curves
    u_aph = 0.60 * np.exp(-curr_t / 4.8)
    u_veg = 0.15 * np.exp(-curr_t / 2.4)
    u_chr = 0.008 * np.exp(-curr_t / 0.8)
    
    ax1.plot(curr_t, u_aph, color='#005696', lw=2.0, label='APH ($\tau=4.8$s)')
    ax1.plot(curr_t, u_veg, color='#008080', lw=2.0, label='VEGGIE ($\tau=2.4$s)')
    ax1.plot(curr_t, u_chr, color='#d95f02', lw=1.8, label='CHROMEX ($\tau=0.8$s)')
    if len(curr_t) > 0:
        ax1.scatter(curr_t[-1], u_aph[-1], color='#005696', s=35)
        ax1.scatter(curr_t[-1], u_veg[-1], color='#008080', s=35)
    ax1.legend(loc='upper right', fontsize=7, framealpha=0.9)

    # Conductance curves across gravities (APH case)
    g_1g = 0.362 + (1.071 - 0.362) * np.exp(-curr_t / 1.5)
    g_mars = 0.180 + (1.071 - 0.180) * np.exp(-curr_t / 1.5)
    g_moon = 0.095 + (1.071 - 0.095) * np.exp(-curr_t / 1.5)
    g_0g = 0.042 + (1.071 - 0.042) * np.exp(-curr_t / 1.5)

    ax2.plot(curr_t, g_1g, color='#4575b4', lw=2.0, label='Earth 1g (Floor 0.36)')
    ax2.plot(curr_t, g_mars, color='#fdae61', lw=1.8, label='Mars 0.38g')
    ax2.plot(curr_t, g_moon, color='#fee08b', lw=1.8, label='Moon 0.166g')
    ax2.plot(curr_t, g_0g, color='#d73027', lw=2.2, label='0g Microgravity (Collapse)')
    if len(curr_t) > 0:
        ax2.scatter(curr_t[-1], g_1g[-1], color='#4575b4', s=30)
        ax2.scatter(curr_t[-1], g_0g[-1], color='#d73027', s=35)
    ax2.legend(loc='upper right', fontsize=6.8, framealpha=0.9)

ani1 = animation.FuncAnimation(fig, update_anim1, frames=len(t_eval), interval=80)
for d in out_dirs:
    ani1.save(str(d / "anim1_fan_cutoff_decay.gif"), writer='pillow', fps=12)
plt.close()
print("Animation 1 saved successfully.")

# -------------------------------------------------------------
# ANIMATION 2: Spore Bioaerosol Clearance Kinetics
# -------------------------------------------------------------
print("=== Generating Animation 2: Spore Clearance Kinetics ===")
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.0, 4.0), dpi=150)
fig.subplots_adjust(wspace=0.35, bottom=0.18, top=0.88)

t_spores = np.linspace(0, 60, 60)

def update_anim2(frame):
    ax1.clear()
    ax2.clear()

    curr_t = t_spores[:frame+1]
    
    # Clearance in canopy
    n_veg_low = np.exp(-curr_t / 58.6)
    n_veg_high = np.exp(-curr_t / 13.8)
    n_aph_nom = np.exp(-curr_t / 18.4)
    n_aph_high = np.exp(-curr_t / 8.1)

    ax1.set_xlim(0, 60)
    ax1.set_ylim(0, 1.05)
    ax1.set_xlabel('Elapsed Time (s)', fontweight='bold')
    ax1.set_ylabel('Normalized Spore Fraction $N(t)/N_0$', fontweight='bold')
    ax1.set_title('a  Canopy Bioaerosol Clearing Kinetics', loc='left', fontweight='bold', fontsize=8.5)
    ax1.grid(True, linestyle=':', alpha=0.6)

    ax1.plot(curr_t, n_veg_low, color='#e66101', lw=1.8, linestyle='--', label='VEGGIE Low (Stagnant)')
    ax1.plot(curr_t, n_veg_high, color='#d73027', lw=1.8, label='VEGGIE High (Cabin Export)')
    ax1.plot(curr_t, n_aph_nom, color='#005696', lw=2.0, label='APH Nom (HEPA Scrubbed)')
    ax1.plot(curr_t, n_aph_high, color='#2b83ba', lw=2.0, label='APH High Blast (HEPA)')
    ax1.legend(loc='upper right', fontsize=6.8, framealpha=0.9)

    # Cabin cumulative contamination
    cab_veg_high = 100 * (1 - np.exp(-curr_t / 13.8)) * 0.795
    cab_aph = np.zeros_like(curr_t)
    cab_cara = np.zeros_like(curr_t)

    ax2.set_xlim(0, 60)
    ax2.set_ylim(0, 100)
    ax2.set_xlabel('Elapsed Time (s)', fontweight='bold')
    ax2.set_ylabel('Cumulative Cabin Spore Discharge (%)', fontweight='bold')
    ax2.set_title('b  Astronaut Module Bioburden Exposure', loc='left', fontweight='bold', fontsize=8.5)
    ax2.grid(True, linestyle=':', alpha=0.6)

    ax2.plot(curr_t, cab_veg_high, color='#d73027', lw=2.2, label='VEGGIE (100% Exported to Crew)')
    ax2.plot(curr_t, cab_aph, color='#1a9850', lw=2.2, label='APH (0% Export - Closed HEPA)')
    ax2.plot(curr_t, cab_cara, color='#7570b3', lw=1.8, linestyle=':', label='CARA Dish (0% - Micropore Tape)')
    ax2.legend(loc='center right', fontsize=6.8, framealpha=0.9)

ani2 = animation.FuncAnimation(fig, update_anim2, frames=len(t_spores), interval=80)
for d in out_dirs:
    ani2.save(str(d / "anim2_spore_clearance.gif"), writer='pillow', fps=12)
plt.close()
print("Animation 2 saved successfully.")

# -------------------------------------------------------------
# ANIMATION 3: Petri Dish Gas Dynamics & Condensation
# -------------------------------------------------------------
print("=== Generating Animation 3: Petri Dish Headspace Kinetics ===")
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.0, 4.0), dpi=150)
fig.subplots_adjust(wspace=0.35, bottom=0.18, top=0.88)

t_dish = np.linspace(0, 24, 60) # 0 to 24 hours

def update_anim3(frame):
    ax1.clear()
    ax2.clear()

    curr_t = t_dish[:frame+1]

    # O2 depletion trajectories
    o2_cara_1g = 18.4 + (20.9 - 18.4) * np.exp(-curr_t / 2.0)
    o2_cara_0g = 14.2 + (20.9 - 14.2) * np.exp(-curr_t / 3.0)
    o2_bric_0g = 1.8 + (20.9 - 1.8) * np.exp(-curr_t / 0.8)

    ax1.set_xlim(0, 24)
    ax1.set_ylim(0, 22)
    ax1.set_xlabel('Incubation Time (hours)', fontweight='bold')
    ax1.set_ylabel('Headspace $O_2$ (%)', fontweight='bold')
    ax1.set_title('a  Headspace Oxygen Depletion', loc='left', fontweight='bold', fontsize=8.5)
    ax1.axhline(5.0, color='#c70039', linestyle='--', label='Hypoxia Limit (5%)')
    ax1.grid(True, linestyle=':', alpha=0.6)

    ax1.plot(curr_t, o2_cara_1g, color='#7570b3', lw=1.8, label='CARA Square (+L, 1g)')
    ax1.plot(curr_t, o2_cara_0g, color='#9e9ac8', lw=2.0, label='CARA Square (+L, 0g)')
    ax1.plot(curr_t, o2_bric_0g, color='#e7298a', lw=2.2, label='BRIC-LED Round (0g Sealed)')
    ax1.legend(loc='upper right', fontsize=6.8, framealpha=0.9)

    # Ethylene accumulation
    eth_cara_1g = 0.32 * (1 - np.exp(-curr_t / 4.0))
    eth_cara_0g = 0.85 * (1 - np.exp(-curr_t / 5.0))
    eth_bric_0g = 3.80 * (1 - np.exp(-curr_t / 3.0))

    ax2.set_xlim(0, 24)
    ax2.set_ylim(0, 4.5)
    ax2.set_xlabel('Incubation Time (hours)', fontweight='bold')
    ax2.set_ylabel('Ethylene $C_2H_4$ (ppm)', fontweight='bold')
    ax2.set_title('b  Hormone Accumulation & Toxicity', loc='left', fontweight='bold', fontsize=8.5)
    ax2.axhline(0.50, color='#c70039', linestyle='--', label='Epinasty Threshold (0.5 ppm)')
    ax2.grid(True, linestyle=':', alpha=0.6)

    ax2.plot(curr_t, eth_cara_1g, color='#7570b3', lw=1.8, label='CARA (+L, 1g)')
    ax2.plot(curr_t, eth_cara_0g, color='#9e9ac8', lw=2.0, label='CARA (+L, 0g Toxic)')
    ax2.plot(curr_t, eth_bric_0g, color='#e7298a', lw=2.2, label='BRIC-LED (0g Extreme)')
    ax2.legend(loc='upper left', fontsize=6.8, framealpha=0.9)

ani3 = animation.FuncAnimation(fig, update_anim3, frames=len(t_dish), interval=80)
for d in out_dirs:
    ani3.save(str(d / "anim3_petridish_gas_condensation.gif"), writer='pillow', fps=12)
plt.close()
print("Animation 3 saved successfully.")

# -------------------------------------------------------------
# ANIMATION 4: Canopy Turbulence & Momentum Wave
# -------------------------------------------------------------
print("=== Generating Animation 4: Canopy Cross-Flow Wave ===")
fig, ax = plt.subplots(figsize=(6.5, 4.0), dpi=150)
fig.subplots_adjust(bottom=0.18, top=0.88)

x_grid = np.linspace(0, 454, 100) # APH width in mm
t_wave = np.linspace(0, 2*np.pi, 60)

def update_anim4(frame):
    ax.clear()
    phase = t_wave[frame]

    # Opposing jet collision profile with oscillating turbulent fluctuations
    u_base = 0.60 * (np.exp(-x_grid/80) + np.exp(-(454 - x_grid)/80))
    u_collision = 0.45 * np.exp(-((x_grid - 227)/50)**2) * (1 + 0.25 * np.sin(phase * 2))
    u_total = u_base + u_collision

    ax.plot(x_grid, u_total, color='#005696', lw=2.2, label='Local Velocity $u(x)$')
    ax.fill_between(x_grid, 0, u_total, color='#90caf9', alpha=0.35)
    
    # Mark midline collision zone
    ax.axvline(227, color='#c70039', linestyle='--', label='Midline Collision Sagittal Plane')
    ax.set_xlim(0, 454)
    ax.set_ylim(0, 0.9)
    ax.set_xlabel('Chamber Lateral Width $x$ (mm)', fontweight='bold')
    ax.set_ylabel('Velocity Magnitude (m/s)', fontweight='bold')
    ax.set_title('APH Opposing Cross-Jets Collision & Updraft Wave', fontweight='bold', fontsize=9.0)
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.legend(loc='upper right', fontsize=7.2, framealpha=0.9)

ani4 = animation.FuncAnimation(fig, update_anim4, frames=len(t_wave), interval=60)
for d in out_dirs:
    ani4.save(str(d / "anim4_canopy_turbulence_wave.gif"), writer='pillow', fps=15)
plt.close()
print("Animation 4 saved successfully.")
