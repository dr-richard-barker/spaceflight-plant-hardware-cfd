# Aerodynamic Boundary-Layer Scaling and Enclosure Regimes Across Spaceflight Plant Growth Hardware: A Multi-Chamber OpenFOAM CFD Framework under Variable Gravity

[![GitHub Pages](https://img.shields.io/badge/Web%20Portal-Live%20Explorer-0284c7)](https://dr-richard-barker.github.io/spaceflight-plant-hardware-cfd/)
[![OpenFOAM](https://img.shields.io/badge/OpenFOAM-v2606-blue.svg)](https://openfoam.com)
[![Manuscript](https://img.shields.io/badge/Manuscript-Nature%20npj%20Microgravity-c70039.svg)](docs/assets/pdf/npj_manuscript.pdf)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 👥 Authors
**Richard Barker**$^{1,*}$, **Henry Ewald**$^{1}$, **Gram Zavos**$^{1}$, **Manisha Dagar**$^{1}$, **Mia Schecter**$^{1}$, **Adriana Sanchez**$^{1}$, **Marshall Porterfield**$^{1}$, and **Astrobotany Consortium**$^{1}$  
$^{1}$ Department of Agricultural and Biological Engineering, Purdue University, West Lafayette, IN 47907, USA  
$^*$ Corresponding author: `rbarker@purdue.edu`

---

## 🚀 Overview

This repository provides the complete, open-source 3D Computational Fluid Dynamics (CFD) simulation framework, analytic geometry generators, scientific datasets, and publication manuscript for our multi-chamber spaceflight plant hardware study under variable gravity.

### Evaluated Spaceflight Hardware Platforms:
1. **NASA Vegetable Production System (VEGGIE/VPS)** ($37.61\text{ L}$)
2. **NASA Advanced Plant Habitat (APH)** ($83.36\text{ L}$ shoot / $9.44\text{ L}$ Science Carrier)
3. **NASA Space Shuttle CHROMEX / Plant Growth Unit (PGU/PGC)** ($49.57\text{ L}$ chassis / $0.866\text{ L}$ canisters)
4. **CARA Experiment Square Petri Dishes** ($100 \times 100 \times 20\text{ mm}$, $\pm$ Light) with porous micropore surgical tape seams
5. **NASA BRIC / BRIC-LED Round Petri Dishes** ($\varnothing 60 \times 15\text{ mm}$ in PDFU canisters, $\pm$ Light).

### Gravitational Environments:
- **Earth ($1.0\text{ g}$)**: Ground baseline and natural thermal convection ($\text{Gr} > 10^7$).
- **Mars ($0.38\text{ g}$)**: Fractional Martian surface gravity.
- **Moon ($0.166\text{ g}$)**: Fractional Lunar surface gravity (Artemis Base Camp).
- **Microgravity ($0\text{ g}$)**: International Space Station (ISS) and transit flight.

---

## 📊 Scientific Figures & Datasets

- **10 Publication Figures** in high-resolution PDF and PNG formats (`manuscript/figures/output/` and `docs/assets/figures/`).
- **6 Quantitative Data Tables** (`manuscript/tables/data/` and `docs/assets/tables/`).
- **3D Analytic STL Generators** (`scripts/make_*.py`).
- **OpenFOAM Finite-Volume Templates** (`templates/`).
- **Interactive 3D WebGL Flow Explorer** (`docs/explorer.html`).

---

## 🛠️ Quickstart

### Compile Manuscript PDF
```bash
python manuscript/build_pdf.py
```

### Run 3D Geometry Generators
```bash
python scripts/make_cara_dish_geometry.py --case runs/cara_case --verify
python scripts/make_bric_led_geometry.py --case runs/bric_case --verify
python scripts/make_veggie_geometry.py --case runs/veggie_case --verify
python scripts/make_aph_geometry.py --case runs/aph_case --verify
python scripts/make_chromex_geometry.py --case runs/chromex_case --verify
```

---

## 📜 Citation

```bibtex
@article{barker2026aerodynamic,
  title={Aerodynamic Boundary-Layer Scaling and Enclosure Regimes Across Spaceflight Plant Growth Hardware: A Multi-Chamber OpenFOAM CFD Framework under Variable Gravity},
  author={Barker, Richard and Ewald, Henry and Zavos, Gram and Dagar, Manisha and Schecter, Mia and Sanchez, Adriana and Porterfield, Marshall and Astrobotany Consortium},
  journal={npj Microgravity},
  volume={12},
  pages={45},
  year={2026},
  publisher={Nature Portfolio}
}
```
