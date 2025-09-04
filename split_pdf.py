#!/usr/bin/env python3
"""
Split a multi-page PDF into individual one-page PDF files.

Usage:
    python split_pdf.py input.pdf [-o OUTPUT_DIR]
"""
from pathlib import Path
import argparse
try:
    from PyPDF2 import PdfReader, PdfWriter
except ModuleNotFoundError:  # PyPDF2 is the old package name
    from pypdf import PdfReader, PdfWriter


def split_pdf(pdf_path: Path, output_dir: Path) -> None:
    """Split ``pdf_path`` into separate pages in ``output_dir``."""
    reader = PdfReader(str(pdf_path))
    for idx, page in enumerate(reader.pages, start=1):
        writer = PdfWriter()
        writer.add_page(page)
        out_file = output_dir / f"{pdf_path.stem}_page_{idx}.pdf"
        with open(out_file, "wb") as fh:
            writer.write(fh)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Split a multi-page PDF into one-page PDFs."
    )
    parser.add_argument("pdf", type=Path, help="Path to the input PDF file")
    parser.add_argument(
        "-o", "--output", type=Path, help="Directory to place split PDFs"
    )
    args = parser.parse_args()

    input_pdf = args.pdf.resolve()
    output_dir = args.output or input_pdf.parent / f"{input_pdf.stem}_pages"
    output_dir.mkdir(parents=True, exist_ok=True)

    split_pdf(input_pdf, output_dir)


if __name__ == "__main__":
    main()
