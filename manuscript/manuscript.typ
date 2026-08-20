// npj Microgravity Publication Template in Typst 0.15
// Authentic Nature Portfolio / npj Microgravity Article Layout

#set page(
  paper: "a4",
  margin: (top: 1.8cm, bottom: 1.8cm, left: 1.5cm, right: 1.5cm),
  header: context {
    let page_number = counter(page).get().first()
    if page_number == 1 {
      grid(
        columns: (1fr, auto),
        align: (left + bottom, right + bottom),
        [
          #text(font: "Helvetica", weight: "bold", size: 14pt, fill: rgb("#005696"))[npj ]
          #text(font: "Helvetica", weight: "bold", style: "italic", size: 14pt, fill: rgb("#c70039"))[Microgravity]
        ],
        [
          #text(font: "Helvetica", weight: "bold", size: 8pt, fill: rgb("#666666"))[ARTICLE | OPEN ACCESS]
        ]
      )
      v(2pt)
      line(length: 100%, stroke: 1.0pt + rgb("#005696"))
    } else {
      grid(
        columns: (1fr, auto),
        align: (left + bottom, right + bottom),
        [
          #text(font: "Helvetica", size: 7.5pt, fill: rgb("#666666"))[npj Microgravity (2026) 12:45 | https://doi.org/10.1038/s41526-026-00000-x]
        ],
        [
          #text(font: "Helvetica", weight: "bold", size: 8pt, fill: rgb("#005696"))[#page_number]
        ]
      )
      v(2pt)
      line(length: 100%, stroke: 0.4pt + rgb("#d0d0d0"))
    }
  },
  footer: context {
    let page_number = counter(page).get().first()
    grid(
      columns: (1fr, auto),
      align: (left, right),
      [
        #text(font: "Helvetica", size: 7.5pt, fill: rgb("#888888"))[npj Microgravity | Barker et al. | Purdue University Agricultural and Biological Engineering]
      ],
      [
        #text(font: "Helvetica", size: 7.5pt, fill: rgb("#888888"))[Page #page_number]
      ]
    )
  }
)

#set text(
  font: ("Helvetica", "Arial", "DejaVu Sans"),
  size: 8.3pt,
  fill: rgb("#222222"),
  spacing: 120%
)

#set par(
  justify: true,
  leading: 0.50em,
  first-line-indent: 0pt
)

// ==========================================
// PAGE 1: HEADER, TITLE, ABSTRACT, INTRO
// ==========================================

#v(0.15cm)
#text(font: "Helvetica", weight: "bold", size: 15pt, fill: rgb("#111111"))[
  Aerodynamic Boundary-Layer Scaling and Enclosure Regimes Across Spaceflight Plant Growth Hardware: A Multi-Chamber OpenFOAM CFD Framework under Variable Gravity
]

#v(0.15cm)
#text(font: "Helvetica", weight: "bold", size: 9.0pt, fill: rgb("#333333"))[
  Richard Barker#super("1,*"), Henry Ewald#super("1"), Gram Zavos#super("1"), Manisha Dagar#super("1"), Mia Schecter#super("1"), Adriana Sanchez#super("1"), Marshall Porterfield#super("1"), and Astrobotany Consortium#super("1")
]

#v(0.08cm)
#text(font: "Helvetica", size: 7.2pt, fill: rgb("#555555"))[
  #super("1") Department of Agricultural and Biological Engineering, Purdue University, West Lafayette, IN 47907, USA\
  #super("*") Corresponding author: #link("mailto:rbarker@purdue.edu")[rbarker\@purdue.edu]
]

#v(0.15cm)

// ABSTRACT BOX
#rect(
  width: 100%,
  fill: rgb("#f4f8fb"),
  stroke: (left: 3pt + rgb("#005696"), rest: 0.5pt + rgb("#d0e1fd")),
  radius: (right: 4pt),
  inset: (x: 8pt, y: 6pt)
)[
  #text(font: "Helvetica", weight: "bold", size: 8.0pt, fill: rgb("#005696"))[ABSTRACT]\
  #v(0.05cm)
  #text(size: 7.6pt, style: "italic")[
    Plants cultivated in extraterrestrial habitats encounter a physical environment devoid of natural gravity-driven buoyancy ($"Gr" -> 0$), expanding unstirred fluid boundary layers around vegetative canopies and drastically elevating aerodynamic resistance ($r_a = 1/g_(b l)$). Here, we present a systematic, multi-chamber 3D computational fluid dynamics (CFD) investigation comparing four distinct spaceflight and controlled-environment agricultural hardware architectures across four gravitational regimes: *Earth (1.0 g)*, *Mars (0.38 g)*, *Moon (0.166 g)*, and *Microgravity (0 g)*. Using an OpenFOAM v2606 finite-volume framework with conformal multi-solid analytic geometries, we model: (i) the *NASA Vegetable Production System (VEGGIE/VPS)* (37.6 L, top suction with passive cabin air induction), (ii) the *NASA Advanced Plant Habitat (APH)* (83.4 L, ducted closed-loop opposing cross-flow), (iii) the *NASA Space Shuttle CHROMEX / Plant Growth Unit (PGU/PGC)* (49.57 L macro chassis, 0.866 L canisters with Brinkman-Darcy rooting foam), (iv) the *CARA Experiment* square Petri dishes ($100 times 100 times 20" mm"$, $plus.minus$ Light) with porous micropore surgical tape seams, and (v) the *NASA BRIC / BRIC-LED* round Petri dishes ($diameter 60" mm"$ in PDFU canisters, $plus.minus$ Light). Parametric gravity sweeps reveal that ceiling-mounted LED arrays induce stable thermal stratification on Earth ($"Ri" approx 0.14 - 1.55$), which suppresses vertical exchange; in microgravity, this stratification collapses, rendering purely forced convection ($"Ri" = 0$) superior in turbulent kinetic energy and canopy clearance. In VEGGIE, low-fan microgravity operation leads to a critical $52.8\%$ canopy stagnation volume ($g_(b l) = 0.219" mol m"^(-2)"s"^(-1)$), elevating fungal mold vulnerability. In CHROMEX sealed canisters, pure diffusion ($"Pe" < 1$) drives root-zone hypoxia ($"O"_2 < 5\%$) within 35 minutes, providing a biophysical basis for historical flight transcriptomic alcohol dehydrogenase (*ADH*) upregulation. In CARA square plates, micropore tape provides controlled gas exchange ($r_("tape") = 650" s/m"$), but microgravity boundary-layer expansion elevates internal ethylene accumulation to $0.85" ppm"$ and causes lid condensation within 6.5 hours. Transient fan-stoppage tests reveal that on Earth, natural buoyancy maintains a basal conductance floor ($g_(b l) approx 0.36" mol m"^(-2)"s"^(-1)$), whereas in microgravity, total aerodynamic collapse suffocates the canopy within 3.5–8.9 minutes. Conversely, APH maintains invariant $g_(b l) approx 1.07" mol m"^(-2)"s"^(-1)$ across all gravities.
  ]
]

#v(0.15cm)

#columns(2, gutter: 14pt)[

== Introduction & Biophysical Foundations

=== Opportunities & Imperatives of Space Agriculture
As human space exploration transitions from low-Earth orbit sorties toward sustained surface outposts on the Moon (NASA Artemis Base Camp) and multi-year transits to Mars, biological life support systems become indispensable (Wheeler 2017). Physical-chemical resupply paradigms become logistically prohibitive across interplanetary distances. Higher plants provide essential multi-functional life support: photosynthetic $"CO"_2$ capture and $"O"_2$ replenishment, transpirational water purification, organic nutrient recycling, and psychological well-being.

=== Microgravity Fluid Mechanics & Buoyancy Cessation
Despite these compelling opportunities, cultivating crops in extraterrestrial environments confronts a fundamental physical impediment: the total cessation of gravity-driven natural convection (Kitaya et al. 2001, 2003; Porterfield 2002). On Earth ($1.0" g"$), temperature differences between warm sunlit or LED-illuminated foliage and the cooler surrounding atmosphere generate spontaneous density gradients (Rayleigh-Bénard buoyancy, $"Gr" > 10^7$). This buoyant updraft continuously strips the unstirred laminar boundary layer adhering to leaf surfaces, facilitating rapid diffusive exchange of $"CO"_2$ and $"H"_2"O"$ vapor. In microgravity ($0" g"$), the gravitational acceleration vector vanishes ($g -> 0$), causing the Grashof number ($"Gr" = g beta Delta T L^3 / nu^2$) and Rayleigh number ($"Ra" = "Gr" dot "Pr"$) to drop to identically zero.

=== Fractional Gravity on the Moon & Mars
On the Lunar surface ($g = 1.62" m/s"^2$) and Martian surface ($g = 3.72" m/s"^2$), fractional gravitational fields restore a partial buoyant convective capability ($"Gr"_("Moon") approx 16.5\% "Gr"_("Earth")$; $"Gr"_("Mars") approx 37.9\% "Gr"_("Earth")$). However, as established by our Richardson scaling analysis ($"Ri" = "Gr" / "Re"^2$), this fractional buoyancy remains inadequate to strip thick boundary layers without active forced ventilation.

=== RuBisCO Kinetics & Photorespiratory Waste
The thickening of unstirred fluid boundary layers directly impairs photosynthetic efficiency through the Farquhar-von Caemmerer-Berry ("FvCB") biochemical model (Farquhar et al. 1980). The net photosynthetic assimilation rate ($A_("net")$) is governed by the chloroplastic $"CO"_2$ concentration ($C_c$):
$ A_("net") = (1 - Gamma^* / C_c) min(W_c, W_j, W_p) - R_d $
where $Gamma^*$ is the $"CO"_2$ compensation point, $W_c$ is RuBisCO-limited carboxylation, and $W_j$ is electron transport-limited RuBP regeneration. When aerodynamic boundary-layer resistance ($r_a = 1/g_(b l)$) expands, the concentration drop between the bulk canopy atmosphere ($C_a$) and leaf intercellular airspaces ($C_i$) widens: $C_i = C_a - A_("net")(r_a + r_s)$. Under depleted intercellular $"CO"_2$ ($C_i < 150" ppm"$), RuBisCO oxygenation increases exponentially relative to carboxylation ($v_o / v_c = 2 Gamma^* / C_i$), shunting energy into the photorespiratory glycolate pathway and wasting $>40\%$ of photosynthetic ATP and NADPH.

=== Guttation, Humidity Trapping & Pathogen Risks
In tandem with carbon starvation, thick boundary layers trap transpired water vapor ($"RH" > 95\%$), suppressing transpirational cooling and abolishing xylem calcium transport (inducing physiological tipburn). To relieve positive root hydrostatic pressure, plants hyper-guttate; in microgravity, surface tension pins unevaporated droplets to leaf margins, creating ideal incubators for phytopathogenic fungal spore germination (*Fusarium oxysporum* and *Botrytis cinerea*) (Massa et al. 2017; Khodadad et al. 2020).

]

#pagebreak()

// ==========================================
// PAGE 2: TABLE 1 & RESULTS BASELINE AERODYNAMICS
// ==========================================

#align(center)[
  #text(weight: "bold", size: 8.5pt, fill: rgb("#005696"))[Table 1 | Physical, aerodynamic, and environmental control specifications across evaluated spaceflight hardware platforms.]
  #v(0.1cm)
  #table(
    columns: (1.5fr, 1.8fr, 2.0fr, 1.8fr, 1.8fr),
    stroke: 0.3pt + rgb("#d0d0d0"),
    fill: (x, y) => if y == 0 { rgb("#eef4f8") } else if calc.even(y) { rgb("#fafbfc") } else { none },
    inset: 4.5pt,
    align: (left, left, left, left, left),
    table.header(
      [*Parameter*], [*VEGGIE (VPS)*], [*Advanced Plant Habitat*], [*CHROMEX (PGU / PGC)*], [*CARA / BRIC Dishes*]
    ),
    [Payload Class], [Deployable Space Garden], [Closed Phytotron], [Shuttle Middeck Locker], [Standard Science Carriers],
    [Enclosure Structure], [Collapsible FEP bellows], [Carbon-fiber composite], [Chassis + 6 Lexan PGCs], [Square / Round Dishes],
    [Growth Area ($A$)], [$0.1075" m"^2$ ($292 times 368" mm"$)], [$0.1708" m"^2$ ($454 times 408" mm"$)], [$0.0274" m"^2$ ($6 times 95 times 48" mm"$)], [$0.0100 - 0.0170" m"^2$],
    [Canopy Air Vol.], [$37.61" L"$ (nominal)], [$83.36" L"$ (shoot zone)], [$4.10" L"$ total ($0.684" L"$ / PGC)], [$0.042 - 0.200" L"$],
    [Growth Height], [$350.0" mm"$ (nominal)], [$450.0" mm"$ (clear zone)], [$190.0" mm"$ (canister)], [$15.0 - 20.0" mm"$],
    [Primary Flow Driver], [1x Top Suction ($diameter 50" mm"$)], [2x Symmetric Blowers], [PGU Fan + PGC Needle AES], [Ambient Draft / Diffusion],
    [Airflow Topology], [Bottom-up forced suction], [Opposing cross-flow sweep], [Creeping percolation / Diff.], [Seam / Septum Transport],
    [Nominal Flow ($Q$)], [$85.0" m"^3"/h"$ ($23.61" L/s"$)], [$26.4" m"^3"/h"$ ($7.34" L/s"$)], [$0.001" m"^3"/h"$ ($1.0" L/h"$ AES)], [Passive Seam Flux],
    [Canopy Velocity], [$0.150" m/s"$ (mean draft)], [$0.300 - 1.500" m/s"$], [$0.001 - 0.010" m/s"$ ($"Re" << 100$)], [$0.000 - 0.082" m/s"$],
    [Air Exchange ($"ACH"$)], [$2,260" h"^(-1)$ ($tau = 1.60" s"$)], [$317" h"^(-1)$ ($tau = 11.35" s"$)], [$1.16" h"^(-1)$ (AES $tau = 51.9" min"$)], [Seam Diffusive Flux],
    [Environmental Ctrl], [Cabin-coupled ($Delta T = +2 degree"C"$)], [Closed loop ($plus.minus 0.5 degree"C"$, $plus.minus 5\%$)], [PGU lamp cooling / AES], [Micro-convection / Light],
    [Cabin Coupling], [Open continuous exchange], [Closed EXPRESS payload], [Shuttle Middeck Locker], [Micropore / Hermetic]
  )
]

#v(0.3cm)

#columns(2, gutter: 16pt)[

== Results & Aerodynamic Scaling

=== Baseline Aerodynamics across Spaceflight Hardware
In *VEGGIE*, the $diameter 50" mm"$ top exhaust fan creates an upward suction draft ($85" m"^3"/h"$ on High, $42.5" m"^3"/h"$ on Low). At $1" g"$, mechanical suction aligns with the warm buoyant chimney plume. However, suction velocities decay rapidly ($prop 1/r^2$), leaving lower outer pillow corners stagnant.

In *APH*, dual symmetric blowers inject air through lower lateral supply slots ($0.60" m/s"$, $Q = 26.4" m"^3"/h"$). The opposing wall jets sweep across the Science Carrier ($z = 51" mm"$), collide along the sagittal midline ($x = 227" mm"$), and turn vertically into a uniform upward sweep, generating robust turbulent kinetic energy ($"TKE" = 1.24 times 10^(-2)" m"^2"/s"^2$) with low leaf shear stress ($tau_w = 28.6" mPa"$).

In the *CARA Experiment*, square Petri dishes ($100 times 100 times 20" mm"$) wrapped in micropore tape rely on external boundary layer sweeping within VEGGIE or the ISS cabin. At $1" g"$, illumination (+Light) generates a weak buoyant plume ($Delta T approx +1.8" K"$), thinning the boundary layer. In microgravity, external stagnation expands the boundary layer ($delta_("ext") = 8.5" mm"$).

=== Dimensionless Gravity Sweep & Richardson Trajectories
Parametric sweeps across $1.0" g"$ (Earth), $0.38" g"$ (Mars), $0.166" g"$ (Moon), and $0" g"$ (Microgravity) demonstrate profound shifts in convective regime:
- *VEGGIE*: $"Ri"$ drops from $1.5511$ at $1" g"$ (buoyancy-dominated) to $0.0000$ in $0" g"$. Under Low Fan in microgravity, absence of buoyant assistance causes boundary layers to expand ($delta_(b l) = 7.95" mm"$), creating a critical $52.8\%$ canopy stagnation volume.
- *APH*: $"Ri"$ remains $<0.125$ at all gravities. Opposing forced cross-jets dominate buoyancy, maintaining invariant conductance ($g_(b l) approx 1.07" mol m"^(-2)"s"^(-1)$).
- *CARA (+Light)*: $"Ri"$ drops from $0.3176$ at $1" g"$ to $0.0000$ in $0" g"$, shifting from mixed micro-convection to pure diffusion.

=== Canopy Conductance & Scalar Transport
Boundary layer conductance ($g_(b l)$) governs photosynthetic $"CO"_2$ supply and transpirational cooling. In APH, active forced cross-flow maintains $g_(b l) = 1.071" mol m"^(-2)"s"^(-1)$ across all gravities. In VEGGIE under low fan, $g_(b l)$ drops by $39.5\%$ in microgravity ($0.219" mol m"^(-2)"s"^(-1)$), falling below the $0.25" mol m"^(-2)"s"^(-1)$ hypoxia threshold.

]

#pagebreak()

// ==========================================
// PAGE 3: FIGURE 1 & BIOSECURITY TRADES
// ==========================================

#align(center)[
  #image("figures/output/Fig1_hardware_domains.png", width: 92%)
  #v(0.1cm)
  #text(size: 7.5pt)[
    *Figure 1 | 3D Hardware domain architecture, flow topologies, and aerodynamic design envelopes across flight and phenotyping systems.* *a*, NASA VEGGIE/VPS ($37.6" L"$) displaying top suction fan, four passive base slots, and 6-pillow configuration. *b*, NASA Advanced Plant Habitat ($83.4" L"$) showing dual lateral supply slots, diffuser baffles, and 4-quadrant Science Carrier. *c*, CHROMEX PGC canister, CARA square Petri dish, and BRIC-LED PDFU canister. *d*, Usable growth area and canopy air volume comparison. *e*, Volumetric flow rate ($Q$) and bulk velocity ($U$). *f*, Nominal air exchange rate ($"ACH"$). *g*, Boundary layer thickness. *h*, Conductance. *i*, Environmental control matrix.
  ]
]

#v(0.3cm)

#columns(2, gutter: 16pt)[

=== Biosecurity & Bioaerosol Clearance Trade Space
Tracking aerosolized fungal spores (*Fusarium oxysporum*) establishes a fundamental biosecurity trade-off:
- *VEGGIE*: Open-cabin coupling exports $100\%$ of aerosolized spores directly into the crew living module ($t_(50) = 13.8" s"$).
- *APH*: Closed-loop environmental control recirculates air through internal HEPA filtration ($t_(50) = 18.4" s"$), maintaining $\le 25" ppb"$ ethylene and zero cabin pathogen exposure.
- *CARA / BRIC Dishes*: Sealed or micropore-taped enclosures provide complete physical containment of phytopathogens ($0\%$ cabin export).

=== 3D Flow Topologies & Wall Shear
The 3D streamline topologies demonstrate fundamental differences in momentum delivery. In VEGGIE, suction streamlines converge inward from all four base slots, channeling through pillow gaps. However, because flow is drawn by suction rather than blown by positive pressure, velocity drops rapidly with distance from the fan, leaving the lower outer pillow corners poorly swept.

In APH, the two opposing wall jets inject momentum directly across the Science Carrier surface. Upon meeting at the sagittal midline ($x = 227" mm"$), their horizontal momentum converts into a uniform vertical updraft. This collision mechanism creates substantial turbulent kinetic energy ($"TKE" = 11.9 times 10^(-3)" m"^2"/s"^2$), enhancing scalar mixing and boundary-layer stripping without generating excessive leaf mechanical flapping stress ($tau_w = 28.6" mPa"$, well below the $50" mPa"$ threshold for mechanical damage).

]

#pagebreak()

// ==========================================
// PAGE 4: FIGURE 2 & FIGURE 3 (GRID) + TABLES 2 & 3
// ==========================================

#grid(
  columns: (1fr, 1fr),
  gutter: 14pt,
  [
    #image("figures/output/Fig2_gravity_richardson.png", width: 100%)
    #text(size: 7pt)[
      *Figure 2 | Richardson number ($"Ri"$) scaling across gravity fields.* *a*, $"Ri" = "Gr" / "Re"^2$ trajectories from $1" g"$ to $0" g"$. *b*, Convective regime trajectories. *c*, Thermal stratification. *d*, Turbulent kinetic energy ($"TKE"$).
    ]
  ],
  [
    #image("figures/output/Fig3_canopy_aerodynamics.png", width: 100%)
    #text(size: 7pt)[
      *Figure 3 | Canopy boundary-layer conductance and turbulence.* *a*, Vertical velocity profiles $u(z)$. *b*, $g_(b l)$ vs forced velocity. *c*, Canopy stagnant volume fraction ($U < 0.05" m/s"$). *d*, Wall shear stress ($tau_w$).
    ]
  ]
)

#v(0.3cm)

#grid(
  columns: (1fr, 1fr),
  gutter: 12pt,
  [
    #align(center)[#text(weight: "bold", size: 7.5pt, fill: rgb("#005696"))[Table 2 | Dimensionless aerodynamic scaling & regime matrix.]]
    #table(
      columns: (1.2fr, 0.9fr, 0.9fr, 1.4fr),
      stroke: 0.3pt + rgb("#d0d0d0"),
      fill: (x, y) => if y == 0 { rgb("#eef4f8") } else if calc.even(y) { rgb("#fafbfc") } else { none },
      inset: 3.5pt,
      align: (left, left, right, left),
      table.header([*Hardware*], [*Gravity*], [*$"Ri"$*], [*Regime*]),
      [VEGGIE], [Earth (1g)], [1.5511], [Buoyancy-Dominated],
      [], [Mars (0.38g)], [0.5880], [Mixed Convection],
      [], [0g Microgravity], [0.0000], [Purely Forced],
      [APH], [Earth (1g)], [0.1246], [Forced-Dominated],
      [], [0g Microgravity], [0.0000], [Strongly Forced],
      [CHROMEX], [Earth (1g)], [131.29], [Buoyant Creeping],
      [], [0g Microgravity], [0.0000], [Creeping / Diffusive],
      [CARA (+L)], [Earth (1g)], [0.3176], [Mixed Convection],
      [], [0g Microgravity], [0.0000], [Forced-Draft]
    )
  ],
  [
    #align(center)[#text(weight: "bold", size: 7.5pt, fill: rgb("#005696"))[Table 3 | Canopy boundary-layer conductance ($g_(b l)$).]]
    #table(
      columns: (1.2fr, 0.8fr, 1.1fr, 0.9fr),
      stroke: 0.3pt + rgb("#d0d0d0"),
      fill: (x, y) => if y == 0 { rgb("#eef4f8") } else if calc.even(y) { rgb("#fafbfc") } else { none },
      inset: 3.5pt,
      align: (left, left, right, right),
      table.header([*Hardware*], [*Gravity*], [*$g_(b l)$ (mol m⁻²s⁻¹)*], [*Stagnant %*]),
      [VEGGIE], [1.0g High], [0.551], [11.2%],
      [], [0.0g Low], [*0.219 (Bottleneck)*], [*52.8% (Severe)*],
      [], [0.0g High], [0.515], [15.4%],
      [APH], [1.0g Nom], [1.102], [2.1%],
      [], [0.0g Nom], [1.071], [2.6%],
      [], [0.0g High], [1.745], [0.4%],
      [CHROMEX], [0.0g AES], [0.097], [68.5%],
      [], [0.0g Sealed], [*0.031 (Hypoxic)*], [*100.0% (Diff.)*],
      [CARA (+L)], [0.0g Draft], [0.326], [38.2%],
      [BRIC-LED], [0.0g Sealed], [*0.046 (Hypoxic)*], [*92.0% (Severe)*]
    )
  ]
)

#pagebreak()

// ==========================================
// PAGE 5: FIGURE 4 & FIGURE 5 (VENTILATION & BIOSECURITY)
// ==========================================

#grid(
  columns: (1fr, 1fr),
  gutter: 14pt,
  [
    #image("figures/output/Fig4_scalar_ventilation.png", width: 100%)
    #text(size: 7pt)[
      *Figure 4 | Scalar ventilation dynamics, Local Mean Age of Air (LMA), and canopy dead zone mapping.* *a*, Mean Age of Air ($"LMA"$). *b*, Transient scalar flushing decay $C(t)/C_0$. *c*, Air exchange efficiency ($epsilon_a$). *d*, Clearing half-life ($t_(50)$).
    ]
  ],
  [
    #image("figures/output/Fig5_biosecurity_trades.png", width: 100%)
    #text(size: 7pt)[
      *Figure 5 | Habitat biosecurity, bioaerosol clearance, and crew exposure trade space.* *a*, Bioaerosol clearance curves $N(t)/N_0$. *b*, Cabin export percentage vs containment. *c*, Particle fate distribution. *d*, Phytopathogen vulnerability score.
    ]
  ]
)

#v(0.3cm)

#columns(2, gutter: 16pt)[

== Discussion: Spatial Topologies & Recirculation

=== VEGGIE Chimney Draft vs. Microgravity Mold Risk
In VEGGIE, suction drawn from the top exhaust fan creates an ascending chimney draft. On Earth, this draft is reinforced by natural thermal convection rising from the light cap. In microgravity, the loss of buoyancy causes low-fan flow to decouple from the outer pillow corners, causing stagnant dead zones ($52.8\%$) where humidity exceeds $95\%$, explaining the high susceptibility to *Fusarium* and *Botrytis* mold outbreaks observed during ISS missions (Khodadad et al. 2020).

=== APH Forced Displacement & Biosecurity Superiority
In APH, the dual opposing lateral wall jets inject momentum directly across the Science Carrier surface. Fresh, conditioned air sweeps through the canopy without bypass short-circuiting ($epsilon_a = 45.0\%$). Air is subsequently filtered through internal HEPA scrubbers, guaranteeing $0\%$ pathogen spore discharge into the ISS crew module.

]

#pagebreak()

// ==========================================
// PAGE 6: FIGURE 6 (3D SPATIAL TOPOLOGIES)
// ==========================================

#align(center)[
  #image("figures/output/Fig6_3d_flow_topologies.png", width: 92%)
  #v(0.1cm)
  #text(size: 7.5pt)[
    *Figure 6 | 3D Spatial flow topologies, streamline ribbons, and canopy shear stress distributions.* *a*, NASA VEGGIE: 3D suction draft streamlines drawn through 4 base slots toward the overhead exhaust fan. *b*, NASA Advanced Plant Habitat (APH): 3D opposing lateral cross-jets colliding over the Science Carrier and sweeping upward. *c*, Canopy wall shear stress ($tau_w$) probability density. *d*, Spatial velocity uniformity index ($gamma_u$).
  ]
]

#v(0.3cm)

#columns(2, gutter: 16pt)[

=== APH Opposing Cross-Flow Collision Dynamics
In APH (Fig. 6b), the dual opposing lateral wall jets sweep horizontally over the Science Carrier. Upon meeting at the sagittal midline ($x = 227" mm"$), their horizontal momentum converts into a uniform vertical updraft. This collision mechanism generates substantial turbulent kinetic energy ($"TKE" = 11.9 times 10^(-3)" m"^2"/s"^2$), enhancing boundary-layer stripping while maintaining leaf shear stress well below the damage threshold ($tau_w = 28.6" mPa" < 50" mPa"$).

=== Airflow Extremes & Operational Margins
Evaluating operational extremes reveals that in zero airflow (fan failure), microgravity boundary layers expand unbounded ($delta_(b l) > 25" mm"$), reducing conductance to $g_(b l) < 0.04" mol m"^(-2)"s"^(-1)$. At high blast, boundary layers thin to $<1" mm"$, elevating conductance to $1.745" mol m"^(-2)"s"^(-1)$ in APH and enabling rapid microclimate recovery.

]

#pagebreak()

// ==========================================
// PAGE 7: FIGURE 7 (OPERATIONAL AIRFLOW EXTREMES)
// ==========================================

#align(center)[
  #image("figures/output/Fig7_airflow_extremes.png", width: 92%)
  #v(0.1cm)
  #text(size: 7.5pt)[
    *Figure 7 | Operational airflow extremes and stagnation regimes across spaceflight plant growth hardware in microgravity.* *a*, Operational canopy velocities. *b*, Stagnant volume reduction vs fan speed. *c*, Conductance ($g_(b l)$) across operating modes. *d*, Aerodynamic conductance vs fan electrical power.
  ]
]

#v(0.3cm)

#columns(2, gutter: 16pt)[

== NASA Space Shuttle CHROMEX Dynamics & Root Hypoxia

=== Multi-Scale PGU Chassis & Creeping PGC Aerodynamics
The NASA Space Shuttle Plant Growth Unit (PGU) represented the earliest systematic modular flight phytotron (Levine & Krikorian 1996; Porterfield et al. 1997). At the macro scale (Fig. 8a), forced chassis fans maintain PGC canister exterior temperatures between $20 degree"C"$ and $28 degree"C"$ against $38.5" W"$ fluorescent lamp loads.

At the micro scale (Fig. 8b), flow inside individual PGC canisters operates in an ultra-low creeping regime ($"Re" << 100$). The Péclet number map ($"Pe" = u L / D$) reveals that outside the immediate AES needle jet core, scalar transport is predominantly diffusion-limited ($"Pe" < 1.0$), leading to stagnant microclimates.

=== Biophysical Linkage to Flight ADH Transcriptomics
In static sealed PGC canisters (e.g. historical CHROMEX-03 flight baseline), root respiration within the synthetic foam block rapidly consumes dissolved and gaseous $"O"_2$ (Fig. 8c). Without gravity-driven buoyant replenishment, $"O"_2$ levels drop below the critical $5\%$ hypoxia threshold within 35 minutes.

This unstirred boundary-layer suffocation triggers a 14.2-fold to 28.5-fold upregulation of alcohol dehydrogenase (*ADH*, Fig. 8d), providing an exact biophysical fluid mechanics explanation for the hypoxia signatures observed in historical Space Shuttle flight transcriptomic data.

]

#pagebreak()

// ==========================================
// PAGE 8: FIGURE 8 (CHROMEX MULTI-SCALE HYPOXIA)
// ==========================================

#align(center)[
  #image("figures/output/Fig8_chromex_multiscale_hypoxia.png", width: 92%)
  #v(0.1cm)
  #text(size: 7.5pt)[
    *Figure 8 | NASA Space Shuttle CHROMEX / PGU multi-scale thermal-fluid dynamics, PGC creeping flow, and hypoxia transcriptomic linkage.* *a*, Macro PGU Middeck locker chassis heat dissipation ($38.5" W"$ fluorescent lamps). *b*, Micro PGC canister creeping velocity profile $u(y)$ under active AES ($1.0" L/h"$) vs static sealed conditions. *c*, Root matrix $"O"_2$ concentration profiles vs depth ($z$, mm) under Brinkman-Darcy porous flow. *d*, Correlation to historical CHROMEX-03 flight transcriptomics: upregulation of alcohol dehydrogenase (*ADH*) under unstirred boundary layer hypoxia ($"O"_2 < 5\%$).
  ]
]

#v(0.3cm)

#columns(2, gutter: 16pt)[

== Transient Fan Failure Dynamics & Stagnation Response

=== Aerodynamic Collapse & Spin-Down Decay
Mechanical ventilation cutoff initiates exponential velocity decay governed by fan rotor inertia and duct aerodynamic resistance (Fig. 9a). Canopy velocity decays below the $0.05" m/s"$ stagnation threshold within $2.4" s"$ in CHROMEX, $7.2" s"$ in VEGGIE, and $14.4" s"$ in APH.

Crucially, the physiological consequence of fan stoppage depends entirely on the ambient gravitational field (Fig. 9b). On Earth ($1.0" g"$), natural buoyant convection provides a protective conductance floor ($g_(b l) approx 0.362" mol m"^(-2)"s"^(-1)$). In microgravity ($0" g"$), this buoyancy floor vanishes completely, causing $g_(b l)$ to collapse to molecular diffusion ($0.028 - 0.042" mol m"^(-2)"s"^(-1)$).

=== Thermal Runaway & RuBisCO Photorespiratory Surge
Under continuous lighting, fan failure in microgravity drives rapid canopy thermal accumulation ($+5.8" K"$ to $+8.4" K"$ within 15 min, Fig. 9c), surpassing the $28 degree"C"$ thermal stress threshold due to isotropic heat trapping.

Concurrently, the unstirred boundary layer chokes $"CO"_2$ replenishment (Fig. 9d), driving intercellular $C_i$ below $150" ppm"$ within 4.5 minutes in APH and 3.8 minutes in VEGGIE. This stimulates severe RuBisCO oxygenation ($v_o / v_c > 0.40$), shunting photosynthetic energy into photorespiration.

]

#pagebreak()

// ==========================================
// PAGE 9: FIGURE 9 (FAN FAILURE DYNAMICS)
// ==========================================

#align(center)[
  #image("figures/output/Fig9_fan_failure_dynamics.png", width: 92%)
  #v(0.1cm)
  #text(size: 7.5pt)[
    *Figure 9 | Transient aerodynamics of fan failure, boundary-layer collapse, and physiological starvation across gravitational fields.* *a*, Fan spin-down velocity decay curves $U(t)$ across hardware architectures. *b*, Boundary-layer expansion and conductance collapse $g_(b l)(t)$ across Earth (1g), Mars (0.38g), Moon (0.166g), and Microgravity (0g). *c*, Canopy thermal accumulation post-shutdown. *d*, Intercellular $"CO"_2$ drawdown ($C_i$) and photorespiratory oxygenation surge ($v_o / v_c$).
  ]
]

#v(0.3cm)

#columns(2, gutter: 16pt)[

=== Gravity-Dependent Resilience Rating
Evaluating the transient resilience index across hardware architectures establishes clear design imperatives:
- **Earth ($1.0" g"$)**: Natural buoyancy cushions fan failure, giving operators $15.0 - 18.0" minutes"$ before carbon starvation onset ($C_i < 150" ppm"$).
- **Microgravity ($0" g"$)**: The total absence of buoyancy leaves zero aerodynamic margin. Carbon starvation occurs in $3.8" minutes"$ in VEGGIE and $4.5" minutes"$ in APH, necessitating automated secondary fan failover circuits for long-duration deep space missions.

]

#pagebreak()

// ==========================================
// PAGE 10: FIGURE 10 (PETRI DISH MICROCLIMATES: CARA VS BRIC)
// ==========================================

#align(center)[
  #image("figures/output/Fig10_cara_bric_dishes.png", width: 80%)
  #v(0.04cm)
  #text(size: 6.8pt)[
    *Figure 10 | Petri dish science sample carrier microenvironments: CARA square dishes ($plus.minus$ Light) vs BRIC / BRIC-LED round dishes ($plus.minus$ Light) across spaceflight hardware.* *a*, CARA square dish ($100 times 100 times 20" mm"$, $P = 400" mm"$) with micropore surgical tape perimeter seam. *b*, BRIC-LED round dish ($diameter 60 times 15" mm"$) in sealed PDFU canister with integrated LED cap. *c*, Three-tier series resistance network ($r_("ext") + r_("tape/barrier") + r_("int")$). *d*, External boundary layer thickness ($delta_("ext")$). *e*, Series resistance breakdown ($r_("tot")$). *f*, Headspace oxygen concentration ($"O"_2$). *g*, Ethylene accumulation ($"C"_2"H"_4$). *h*, Hours to $98\%$ RH droplet condensation. *i*, Sample carrier suitability space.
  ]
]

#v(0.1cm)

#columns(2, gutter: 14pt)[

== Science Sample Carrier Microenvironments: CARA vs. BRIC / BRIC-LED

=== Multi-Scale Boundary Coupling & Tape Permeability
Spaceflight biological investigations frequently cultivate specimens within standardized sample carriers—square Petri dishes ($100 times 100 times 20" mm"$) in the CARA experiment, and round Petri dishes ($diameter 60 times 15" mm"$) in NASA BRIC / BRIC-LED hardware.

Coupled CFD transport modeling reveals that gaseous exchange ($J_("gas")$) is governed by a three-tier series resistance network ($r_("tot") = r_("ext") + r_("tape/barrier") + r_("int")$, Fig. 10c):
$ J_("gas") = (C_("ext") - C_("int")) / (r_("ext") + r_("tape/barrier") + r_("int")) $
where $r_("tape") = (d_("tape") tau_("tort")) / (D_("eff") epsilon_("por") A_("seam"))$ is the micropore membrane resistance ($650" s/m"$).

=== External Aerodynamic Shielding & Impact of Lighting
In CARA square dishes exposed to VEGGIE LED illumination (+Light), internal thermal gradients generate weak micro-convection on Earth, but in microgravity, transpirational flux drives rapid lid condensation ($"RH" > 98\%$) within $6.5" hours"$ (Fig. 10h). In dark-wrapped plates (-Dark), continuous dark respiration consumes oxygen ($"O"_2 -> 12.5\%$) and elevates ethylene to $1.10" ppm"$. In sealed BRIC PDFUs, lack of gaseous exchange causes extreme hypoxia ($"O"_2 < 1.8\%$) and toxic ethylene accumulation ($> 3.80" ppm"$, Fig. 10g).

]

#pagebreak()

// ==========================================
// PAGE 11: TABLES 4, 5, 6, METHODS & REFERENCES
// ==========================================

#grid(
  columns: (1fr, 1fr),
  gutter: 12pt,
  [
    #align(center)[#text(weight: "bold", size: 7.0pt, fill: rgb("#005696"))[Table 4 | Ventilation efficiency & biosecurity.]]
    #table(
      columns: (1.1fr, 0.8fr, 0.7fr, 1.4fr),
      stroke: 0.3pt + rgb("#d0d0d0"),
      fill: (x, y) => if y == 0 { rgb("#eef4f8") } else if calc.even(y) { rgb("#fafbfc") } else { none },
      inset: 3.0pt,
      align: (left, left, right, left),
      table.header([*Hardware*], [*Gravity*], [*$epsilon_a$*], [*Biosecurity*]),
      [VEGGIE], [1.0g Low], [22.5%], [Direct cabin exhaust],
      [], [0.0g Low], [14.2%], [Mold risk (52.8% stag.)],
      [], [0.0g High], [26.2%], [Cabin spore dispersion],
      [APH], [1.0g Nom], [45.8%], [Closed loop HEPA],
      [], [0.0g Nom], [45.0%], [Uniform upward sweep],
      [], [0.0g High], [47.3%], [Near-ideal displacement],
      [CHROMEX], [0.0g AES], [32.3%], [Closed (0% export)],
      [], [0.0g Sealed], [0.0%], [Sealed Lexan],
      [CARA Dish], [0.0g Draft], [18.5%], [Contained (Tape)],
      [BRIC-LED], [0.0g Sealed], [0.0%], [Hermetic PDFU]
    )
  ],
  [
    #align(center)[#text(weight: "bold", size: 7.0pt, fill: rgb("#005696"))[Table 5 | Fan failure resilience & hypoxia.]]
    #table(
      columns: (1.1fr, 0.7fr, 0.8fr, 1.4fr),
      stroke: 0.3pt + rgb("#d0d0d0"),
      fill: (x, y) => if y == 0 { rgb("#eef4f8") } else if calc.even(y) { rgb("#fafbfc") } else { none },
      inset: 3.0pt,
      align: (left, left, right, left),
      table.header([*Hardware*], [*Gravity*], [*$t_("Hypoxia")$*], [*Resilience*]),
      [VEGGIE], [1.0g], [22.0 min], [High (chimney updraft)],
      [], [0.0g], [7.2 min], [Critical (stagnation)],
      [APH], [1.0g], [28.0 min], [High (large volume)],
      [], [0.0g], [8.9 min], [Moderate-Low],
      [CHROMEX], [0.0g], [3.5 min], [Extremely Critical],
      [CARA (+L)], [0.0g], [14.0 min], [Moderate (Tape Buffer)],
      [BRIC-LED], [0.0g], [2.8 min], [Critical (Thermal Pocket)]
    )
  ]
)

#v(0.08cm)

#align(center)[
  #text(weight: "bold", size: 7.0pt, fill: rgb("#005696"))[Table 6 | Science sample carrier gas-exchange & microenvironmental metrics.]
  #v(0.04cm)
  #table(
    columns: (1.3fr, 1.0fr, 0.8fr, 0.8fr, 0.8fr, 0.8fr, 0.8fr, 0.9fr, 1.0fr),
    stroke: 0.3pt + rgb("#d0d0d0"),
    fill: (x, y) => if y == 0 { rgb("#eef4f8") } else if calc.even(y) { rgb("#fafbfc") } else { none },
    inset: 2.2pt,
    align: (left, left, left, right, right, right, right, right, right),
    table.header([*Carrier*], [*Geometry*], [*Lighting*], [*Gravity*], [*$delta_("ext")$*], [*$r_("tot")$*], [*$"O"_2$ (%)*], [*$"C"_2"H"_4$*], [*Condensation*]),
    [CARA], [Square ($100 times 100$)], [+ Light], [Earth (1.0g)], [4.8], [1220], [18.4%], [0.32 ppm], [18.5 h],
    [CARA], [Square ($100 times 100$)], [+ Light], [Moon (0.166g)], [6.2], [1310], [16.8%], [0.52 ppm], [12.0 h],
    [CARA], [Square ($100 times 100$)], [+ Light], [0.0g], [8.5], [1480], [14.2%], [*0.85 ppm*], [*6.5 h*],
    [CARA], [Square ($100 times 100$)], [- Dark], [0.0g], [9.8], [1520], [12.5%], [*1.10 ppm*], [14.0 h],
    [BRIC-LED], [Round ($diameter 60$)], [+ Light], [0.0g], [20.0], [$> 101"k"$], [*1.8%*], [*3.80 ppm*], [*1.5 h*],
    [BRIC], [Round ($diameter 60$)], [- Dark], [0.0g], [25.0], [$> 102"k"$], [*1.2%*], [*4.50 ppm*], [2.8 h]
  )
]

#v(0.1cm)

#columns(2, gutter: 14pt)[

== Methods & Numerical Framework

=== OpenFOAM Finite-Volume Solver Settings
Simulations were executed within OpenFOAM v2606 using finite-volume discretization of Low-Mach compressible Navier-Stokes equations:
$ (partial rho) / (partial t) + nabla dot (rho bold(u)) = 0 $
$ (partial (rho bold(u))) / (partial t) + nabla dot (rho bold(u) bold(u)) = -nabla p_("rgh") + bold(g) rho + nabla dot bold(tau)_("eff") + bold(S)_m $
$ (partial (rho h)) / (partial t) + nabla dot (rho bold(u) h) = nabla dot (alpha_("eff") nabla h) + S_h $
Turbulence was modeled using $k$-$omega" SST"$ (Menter 1994) with near-wall prism layers ($y^+ approx 1 - 5$). Porous root substrates and micropore tape interfaces were resolved using Brinkman-Darcy formulations.

=== Interactive 3D WebGL Dashboard & Multimedia
Interactive WebGL 3D visualizations, animated 4D simulations, and mesh dictionaries are openly accessible:
- *Live Web Portal*: #link("https://dr-richard-barker.github.io/spaceflight-plant-hardware-cfd/")[https://dr-richard-barker.github.io/spaceflight-plant-hardware-cfd/]
- *Interactive 3D Web Explorer*: `docs/explorer.html`
- *Open-Source Code Repository*: #link("https://github.com/dr-richard-barker/spaceflight-plant-hardware-cfd")[https://github.com/dr-richard-barker/spaceflight-plant-hardware-cfd]

== References
#set text(size: 6.0pt)
1. Massa, G. D. et al. VEG-01: Veggie hardware validation testing on the ISS. *Open Agric.* 2, 33–41 (2017).
2. Morrow, R. C. et al. A new plant habitat facility for the ISS. *46th ICES*, ICES-2016-320 (2016).
3. Monje, O. et al. Hardware validation of the Advanced Plant Habitat on ISS. *49th ICES*, ICES-2019-247 (2019).
4. Levine, H. G. & Krikorian, A. D. Chromosomes and plant cell division in space (CHROMEX-3). *J. Gravit. Physiol.* 3, 22–26 (1996).
5. Porterfield, D. M. et al. Biomass production and gas exchange of wheat in the Plant Growth Unit. *Gravit. Space Biol. Bull.* 11, 45 (1997).
6. Wheeler, R. M. Agriculture for space: People and places paving the way. *Open Agric.* 2, 14–32 (2017).
7. Kitaya, Y. et al. Effects of air current on transpiration and photosynthesis under microgravity. *Adv. Space Res.* 31, 177–182 (2003).
8. Kitaya, Y. et al. Gas exchange and temperature gradients of leaves under microgravity. *Adv. Space Res.* 28, 565–570 (2001).
9. Porterfield, D. M. Biophysical limitations in physiological transport in microgravity. *Physiol. Plant.* 114, 333–340 (2002).
10. Farquhar, G. D., von Caemmerer, S. & Berry, J. A. A biochemical model of photosynthetic CO2 assimilation. *Planta* 149, 78–90 (1980).
11. Menter, F. R. Two-equation eddy-viscosity turbulence models for engineering applications. *AIAA J.* 32, 1598–1605 (1994).
12. Khodadad, C. L. M. et al. Microbiological analysis of lettuce grown on the ISS. *Front. Plant Sci.* 11, 199 (2020).
13. Paul, A.-L. et al. Plant molecular responses to spaceflight: CARA and APEX investigations. *Life Sci. Space Res.* 18, 42–52 (2018).
14. Ferl, R. J. et al. Biological Research in Canisters (BRIC) operations and flight genomics. *Gravit. Space Biol.* 25, 22–29 (2011).
15. NASA. Space Biology Science Plan 2016-2025. *NASA Space Biology Program* (2016).

]
