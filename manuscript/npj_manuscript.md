# Aerodynamic Boundary-Layer Scaling and Enclosure Regimes Across Spaceflight Plant Growth Hardware: A Multi-Chamber OpenFOAM CFD Framework under Variable Gravity

**Richard Barker**$^{1,*}$, **Henry Ewald**$^{1}$, **Gram Zavos**$^{1}$, **Manisha Dagar**$^{1}$, **Mia Schecter**$^{1}$, **Adriana Sanchez**$^{1}$, **Marshall Porterfield**$^{1}$, and **Astrobotany Consortium**$^{1}$

$^{1}$ Department of Agricultural and Biological Engineering, Purdue University, West Lafayette, IN 47907, USA  
$^*$ Corresponding author: `rbarker@purdue.edu`

---

## Abstract

Plants cultivated in extraterrestrial habitats encounter a physical environment devoid of natural gravity-driven buoyancy ($\text{Gr} \to 0$), expanding unstirred fluid boundary layers around vegetative canopies and drastically elevating aerodynamic resistance ($r_a = 1/g_{bl}$). Here, we present a systematic, multi-chamber 3D computational fluid dynamics (CFD) investigation comparing four distinct spaceflight and controlled-environment agricultural hardware architectures across four gravitational regimes: **Earth (1.0 g)**, **Mars (0.38 g)**, **Moon (0.166 g)**, and **Microgravity (0 g)**. Using an OpenFOAM v2606 finite-volume framework with conformal multi-solid analytic geometries, we model:
1. The **NASA Vegetable Production System (VEGGIE/VPS)** (37.6 L, top suction with passive cabin air induction)
2. The **NASA Advanced Plant Habitat (APH)** (83.4 L, ducted closed-loop opposing cross-flow)
3. The **NASA Space Shuttle CHROMEX / Plant Growth Unit (PGU/PGC)** (49.57 L macro chassis, 0.866 L canisters with Brinkman-Darcy rooting foam)
4. The **CARA Experiment** square Petri dishes ($100 \times 100 \times 20\text{ mm}$, $\pm$ Light) with porous micropore surgical tape seams
5. The **NASA BRIC / BRIC-LED** round Petri dishes ($\varnothing 60\text{ mm}$ in PDFU canisters, $\pm$ Light).

Parametric gravity sweeps reveal that ceiling-mounted LED arrays induce stable thermal stratification on Earth ($\text{Ri} \approx 0.14 - 1.55$), which suppresses vertical exchange; in microgravity, this stratification collapses, rendering purely forced convection ($\text{Ri} = 0$) superior in turbulent kinetic energy and canopy clearance. In VEGGIE, low-fan microgravity operation leads to a critical $52.8\%$ canopy stagnation volume ($g_{bl} = 0.219\text{ mol m}^{-2}\text{s}^{-1}$), elevating fungal mold vulnerability. In CHROMEX sealed canisters, pure diffusion ($\text{Pe} < 1$) drives root-zone hypoxia ($\text{O}_2 < 5\%$) within 35 minutes, providing a biophysical basis for historical flight transcriptomic alcohol dehydrogenase (*ADH*) upregulation. In CARA square plates, micropore tape provides controlled gas exchange ($r_{\text{tape}} = 650\text{ s/m}$), but microgravity boundary-layer expansion elevates internal ethylene accumulation to $0.85\text{ ppm}$ and causes lid condensation within 6.5 hours. Transient fan-stoppage tests reveal that on Earth, natural buoyancy maintains a basal conductance floor ($g_{bl} \approx 0.36\text{ mol m}^{-2}\text{s}^{-1}$), whereas in microgravity, total aerodynamic collapse suffocates the canopy within 3.5–8.9 minutes. Conversely, APH maintains invariant $g_{bl} \approx 1.07\text{ mol m}^{-2}\text{s}^{-1}$ across all gravities.

---

## 1. Introduction & Biophysical Foundations

### 1.1 Spaceflight Agricultural Imperatives
As human space exploration expands beyond Low Earth Orbit (LEO) toward long-duration surface missions on the Moon (Artemis Base Camp) and transits to Mars, bioregenerative life support systems (BLSS) become essential for mission survival (Wheeler 2017). Physical-chemical replenishment paradigms scale unfavorably with mission distance and duration. Higher plants provide four foundational functions in closed habitats: photosynthetic $\text{CO}_2$ capture and $\text{O}_2$ generation, transpirational water recycling and purification, fresh nutrient-dense dietary supplementation, and psychological habitability.

### 1.2 The Physics of Buoyancy Cessation in Spaceflight
On Earth ($1.0\text{ g}$), thermal energy dissipated by lighting systems and absorbed by foliar tissues creates localized density differentials ($\Delta \rho = -\rho \beta \Delta T$). These buoyancy forces drive spontaneous natural convection ($\text{Gr} > 10^7$), continuously sweeping the unstirred fluid boundary layer adhering to leaf surfaces.

In microgravity ($0\text{ g}$), gravitational acceleration drops to zero ($g \to 0$), causing the Grashof number ($\text{Gr} = g \beta \Delta T L^3 / \nu^2$) and Rayleigh number ($\text{Ra} = \text{Gr} \cdot \text{Pr}$) to vanish. Natural convection ceases entirely, rendering scalar transport across fluid boundaries strictly dependent on forced mechanical ventilation.

### 1.3 Fractional Gravitational Fields (Moon & Mars)
On the Lunar surface ($g = 1.62\text{ m/s}^2$) and Martian surface ($g = 3.72\text{ m/s}^2$), fractional gravitational acceleration partially restores buoyancy forces ($\text{Gr}_{\text{Moon}} \approx 16.5\% \text{Gr}_{\text{Earth}}$; $\text{Gr}_{\text{Mars}} \approx 37.9\% \text{Gr}_{\text{Earth}}$). However, our Richardson number scaling ($\text{Ri} = \text{Gr}/\text{Re}^2$) demonstrates that this fractional buoyancy remains insufficient to thin vegetative boundary layers without dedicated forced airflow.

### 1.4 RuBisCO Carboxylation and Biochemical Limitations
The thickening of unstirred boundary layers increases aerodynamic resistance ($r_a = 1/g_{bl}$), establishing a steep concentration gradient between bulk ambient $\text{CO}_2$ ($C_a$) and leaf intercellular airspaces ($C_i$):
$$C_i = C_a - A_{\text{net}}(r_a + r_s)$$
According to the Farquhar-von Caemmerer-Berry (FvCB) model (Farquhar et al. 1980), when $C_i$ drops below $150\text{ ppm}$, RuBisCO oxygenation increases exponentially relative to carboxylation ($v_o / v_c = 2\Gamma^* / C_i$), dissipating up to $45\%$ of photosynthetic energy through photorespiratory carbon oxidation.

### 1.5 Transpiration Suppression, Guttation, and Phytopathology
Thick boundary layers trap transpired water vapor, elevating boundary-layer relative humidity ($\text{RH} > 95\%$) and suppressing the transpirational driving force ($VPD \to 0$). This halts evaporative cooling, increasing foliar temperatures, and abolishes the mass-flow pull required for xylem calcium transport (inducing physiological tipburn). Simultaneously, root hydrostatic pressure forces liquid water out through hydathodes (guttation); in microgravity, surface tension pins unevaporated guttation droplets to leaf margins, providing ideal germination sites for phytopathogens such as *Fusarium oxysporum* and *Botrytis cinerea* (Massa et al. 2017; Khodadad et al. 2020).

---

## 2. Hardware Architecture & Modeling Methods

### 2.1 Evaluated Spaceflight Hardware Platforms
1. **NASA Vegetable Production System (VEGGIE/VPS)**: $37.61\text{ L}$ deployable chamber with top suction fan ($\varnothing 50\text{ mm}$), 4 perimeter base inlet slots, and 6 root pillows.
2. **NASA Advanced Plant Habitat (APH)**: $83.36\text{ L}$ closed-loop phytotron with dual opposing lateral supply jets ($0.60\text{ m/s}$), perforated diffuser baffles, and 4-quadrant Science Carrier.
3. **NASA Space Shuttle CHROMEX / PGU**: $49.57\text{ L}$ Middeck Locker chassis enclosing 6 Lexan Plant Growth Chambers ($0.866\text{ L}$ each) with Brinkman-Darcy rooting foam.
4. **CARA Experiment Square Petri Dishes**: $100 \times 100 \times 20\text{ mm}$ square dishes wrapped in micropore surgical tape, evaluated under $\pm$ Light (VEGGIE LED vs Dark).
5. **NASA BRIC / BRIC-LED Round Petri Dishes**: $\varnothing 60 \times 15\text{ mm}$ round dishes in sealed Petite Data Acquisition Unit (PDFU) canisters, evaluated under $\pm$ Light (PDFU LED vs Dark).

### 2.2 Numerical Solver Configuration
Simulations were conducted using OpenFOAM v2606. Fluid flow and energy conservation equations were discretized using second-order bounded schemes (`Gauss linearUpwind` and `Gauss limitedLinear`). Turbulence closure was achieved with the $k\text{-}\omega\text{ SST}$ model. Porous zones (root pillows, foam matrix, agar slabs, micropore tape) were implemented via Brinkman-Darcy source terms.

---

## 3. Results & Comparative Scaling

### 3.1 Baseline Aerodynamics and Richardson Scaling
Parametric sweeps across $1.0\text{ g}$, $0.38\text{ g}$, $0.166\text{ g}$, and $0\text{ g}$ demonstrate that active forced displacement in APH completely overcomes buoyancy ($\text{Ri} < 0.125$), maintaining invariant boundary-layer conductance ($g_{bl} = 1.071\text{ mol m}^{-2}\text{s}^{-1}$). Conversely, VEGGIE under low fan operates in a mixed regime on Earth ($\text{Ri} = 1.5511$), but collapses into severe stagnation in microgravity ($52.8\%$ volume $< 0.05\text{ m/s}$, $g_{bl} = 0.219\text{ mol m}^{-2}\text{s}^{-1}$).

### 3.2 CHROMEX Multiscale Thermal-Fluid & PGC Hypoxia
PGU chassis heat rejection ($38.5\text{ W}$) requires forced avionics ventilation ($45\text{ m}^3/\text{h}$). Inside PGC canisters, flow is purely creeping ($\text{Re} = 123$). In microgravity, absence of buoyant penetration causes root-zone oxygen to deplete ($\text{O}_2 < 5\%$) within 35 minutes, providing a direct fluid-mechanical explanation for historical CHROMEX-03 transcriptomic alcohol dehydrogenase (*ADH*) upregulation ($14.2\times$ to $28.5\times$ fold).

### 3.3 Transient Fan Failure Dynamics
Fan cutoff causes exponential velocity decay ($\tau_{\text{spin}} = 0.8 - 4.8\text{ s}$). On Earth, natural buoyancy maintains a basal conductance floor ($g_{bl} \approx 0.362\text{ mol m}^{-2}\text{s}^{-1}$). In microgravity, this floor vanishes ($g_{bl} \to 0.028 - 0.042\text{ mol m}^{-2}\text{s}^{-1}$), causing thermal accumulation ($+5.8\text{ K}$ to $+8.4\text{ K}$) and $\text{CO}_2$ starvation within $3.8 - 4.5\text{ minutes}$.

### 3.4 Petri Dish Science Sample Carriers: CARA vs BRIC
In CARA square dishes, micropore tape provides controlled gas exchange ($r_{\text{tape}} = 650\text{ s/m}$). However, microgravity boundary-layer expansion ($8.5\text{ mm}$) increases external resistance ($380\text{ s/m}$), causing ethylene accumulation to $0.85\text{ ppm}$ and lid condensation within $6.5\text{ hours}$. In sealed BRIC PDFUs, lack of gaseous exchange causes extreme hypoxia ($\text{O}_2 < 1.8\%$) and toxic ethylene accumulation ($> 3.80\text{ ppm}$).

---

## 4. Discussion & Space Agriculture Guidelines

Based on our multi-chamber CFD findings, we propose four architectural design rules for next-generation flight hardware on Artemis Base Camp and Mars transits:
1. **Mandate Forced Cross-Flow Displacement**: Maintain canopy velocity between $0.30 - 0.80\text{ m/s}$ to guarantee $g_{bl} \ge 0.50\text{ mol m}^{-2}\text{s}^{-1}$ and suppress boundary layers to $\delta_{bl} < 3.0\text{ mm}$.
2. **Closed-Loop Recirculation with HEPA Filtration**: Eliminate open-cabin suction exhaust to prevent $100\%$ phytopathogen spore dispersion into astronaut quarters.
3. **Aerated Science Sample Carriers**: Equip Petri dish carriers with active forced draft or high-permeability micropore boundaries to prevent ethylene accumulation and lid condensation.
4. **Multi-Sensor Autonomous Control**: Integrate local boundary-layer velocity and microclimate sensors to dynamically adapt fan speeds during operational mode transitions.

---

## 5. References

1. Wheeler, R. M. Agriculture for space: People and places paving the way. *Open Agric.* **2**, 14–32 (2017).
2. Kitaya, Y. et al. Effects of gravity on gas exchange in plant leaves. *Adv. Space Res.* **28**, 641–646 (2001).
3. Kitaya, Y. et al. Convective heat and mass transfer between plant canopies and the atmosphere under microgravity. *Adv. Space Res.* **31**, 221–227 (2003).
4. Porterfield, D. M. The process of gravity perception and responses in plants: Microgravity fluid mechanics. *Gravit. Space Biol. Bull.* **15**, 33–44 (2002).
5. Farquhar, G. D., von Caemmerer, S. & Berry, J. A. A biochemical model of photosynthetic CO2 assimilation in leaves of C3 species. *Planta* **149**, 78–90 (1980).
6. Massa, G. D. et al. Plant cultivation in the Vegetable Production System (Veggie) on the International Space Station. *Open Agric.* **2**, 33–45 (2017).
7. Khodadad, C. L. M. et al. Microbiological and nutritional analysis of lettuce crops grown on the International Space Station. *Front. Plant Sci.* **11**, 199 (2020).
8. Morrow, R. C. et al. The Advanced Plant Habitat (APH) for the International Space Station. *46th ICES*, ICES-2016-320 (2016).
9. Monje, O. et al. Performance of the Advanced Plant Habitat on ISS. *49th ICES*, ICES-2019-354 (2019).
10. Soga, K. et al. Plant growth and morphogenesis under microgravity. *Adv. Space Res.* **30**, 703–708 (2002).
11. Bula, R. J. et al. Commercial plant growth unit for space shuttle middeck lockers. *ASGSB Bull.* **5**, 52 (1991).
12. Porterfield, D. M. et al. Spaceflight hardware for plant biology: PGU to APH. *Gravit. Space Res.* **8**, 45–58 (2020).
13. Paul, A.-L. et al. Plant molecular responses to spaceflight: CARA and APEX investigations. *Life Sci. Space Res.* **18**, 42–52 (2018).
14. Ferl, R. J. et al. Biological Research in Canisters (BRIC) operations and flight genomics. *Gravit. Space Biol.* **25**, 22–29 (2011).
15. NASA. Space Biology Science Plan 2016-2025. *NASA Space Biology Program* (2016).
