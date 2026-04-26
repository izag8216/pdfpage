# API Reference — pdfpage

## Installation

```bash
pip install pdfpage
```

## CLI Usage

```bash
pdfpage --help
pdfpage extract input.pdf --pages 1,3,5-10 --output output.pdf
pdfpage split large.pdf --ranges 1-10 11-20 --output-dir ./parts
pdfpage merge a.pdf b.pdf --output merged.pdf
pdfpage rotate scan.pdf --degrees 90 --pages 2,4 --output rotated.pdf
pdfpage info document.pdf
```

## Python API

### extract_pages(input_path, output_path, pages) -> dict

Extract specific pages from a PDF.

```python
from pdfpage import extract_pages

result = extract_pages(
    "input.pdf",
    "output.pdf",
    [0, 2, 4]  # 0-indexed page numbers
)
# result = {"extracted": 3, "total_pages": 10, "output": "output.pdf"}
```

### split_pdf(input_path, output_dir, ranges) -> list[dict]

Split PDF into multiple parts.

```python
from pdfpage import split_pdf

results = split_pdf(
    "large.pdf",
    "./parts",
    [[0, 1, 2], [3, 4, 5], [6, 7, 8, 9]]  # page ranges (0-indexed)
)
# results = [{"part": 1, "pages": 3, "output": "parts/part_001.pdf"}, ...]
```

### merge_pdfs(input_paths, output_path) -> dict

Merge multiple PDFs into one.

```python
from pdfpage import merge_pdfs

result = merge_pdfs(
    ["a.pdf", "b.pdf", "c.pdf"],
    "merged.pdf"
)
# result = {"merged": 3, "output": "merged.pdf"}
```

### rotate_pages(input_path, output_path, degrees, pages) -> dict

Rotate specific pages in a PDF.

```python
from pdfpage import rotate_pages

result = rotate_pages(
    "scan.pdf",
    "rotated.pdf",
    90,  # degrees: 90, 180, or 270
    [1, 3]  # 0-indexed pages to rotate
)
# result = {"rotated": 2, "total_pages": 10, "degrees": 90, "output": "rotated.pdf"}
```

## Page Specification

Pages are specified as 0-indexed numbers (internal) but CLI uses 1-indexed.

| CLI Format | Python Format | Description |
|------------|---------------|-------------|
| `1` | `0` | First page |
| `1,3,5` | `[0, 2, 4]` | Pages 1, 3, 5 |
| `1-5` | `[0, 1, 2, 3, 4]` | Pages 1 through 5 |
| `1,3,5-10` | `[0, 2, 4, 5, 6, 7, 8, 9]` | Mixed specification |