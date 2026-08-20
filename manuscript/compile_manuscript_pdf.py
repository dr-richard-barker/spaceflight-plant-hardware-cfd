#!/usr/bin/env python3
import os
import glob
from pathlib import Path
import typst

def compile_pdf():
    manuscript_dir = Path(__file__).resolve().parent
    typst_file = manuscript_dir / "manuscript.typ"
    pdf_out = manuscript_dir / "npj_manuscript.pdf"
    
    print(f"=== Compiling npj Microgravity Manuscript via Typst: {typst_file} ===")
    typst.compile(str(typst_file), output=str(pdf_out))
    print(f"=== Successfully Compiled Publication PDF: {pdf_out} ===")
    
    # Export PNG page previews
    proofs_dir = manuscript_dir / "figures" / "output"
    for old_png in glob.glob(str(proofs_dir / "page_*.png")):
        os.remove(old_png)
    typst.compile(str(typst_file), output=str(proofs_dir / "page_{n}.png"), format="png", ppi=150)
    pages = sorted(glob.glob(str(proofs_dir / "page_*.png")))
    print(f"Compiled clean: {len(pages)} pages")

if __name__ == "__main__":
    compile_pdf()
