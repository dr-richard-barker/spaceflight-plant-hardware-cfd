#!/usr/bin/env python3
"""Build script for compiling npj Microgravity Typst manuscript to PDF."""
import os
import glob
from pathlib import Path
import typst

def main():
    root = Path(__file__).resolve().parent
    typst_path = root / "manuscript.typ"
    pdf_path = root / "npj_manuscript.pdf"
    
    print(f"Compiling {typst_path} -> {pdf_path}...")
    typst.compile(str(typst_path), output=str(pdf_path))
    
    # Export PNG page previews
    proofs_dir = root / "figures" / "output"
    for old_png in glob.glob(str(proofs_dir / "page_*.png")):
        os.remove(old_png)
    typst.compile(str(typst_path), output=str(proofs_dir / "page_{n}.png"), format="png", ppi=150)
    pages = sorted(glob.glob(str(proofs_dir / "page_*.png")))
    print(f"Successfully generated {pdf_path} ({len(pages)} pages).")

if __name__ == "__main__":
    main()
