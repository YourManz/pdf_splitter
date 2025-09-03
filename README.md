# pdf_splitter

Split a multi-page PDF into named one-page PDFs that sum to the original.

## Requirements
- Python 3
- [PyPDF2](https://pypi.org/project/PyPDF2/)

Install the dependency:

```bash
pip install PyPDF2
```

## Usage

```bash
python split_pdf.py path/to/input.pdf            # outputs to ./input_pages/
python split_pdf.py path/to/input.pdf -o outdir  # specify output directory
```
