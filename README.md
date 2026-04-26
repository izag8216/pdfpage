# pdfpage

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![PyPI](https://img.shields.io/badge/PyPI-v0.1.0-blue?style=for-the-badge&logo=pypi&logoColor=white)](https://pypi.org/project/pdfpage/)

**PDF page extraction, splitting, merging, and rotation CLI tool.** Pipe-friendly, scriptable, no GUI required.

---

<!-- Original SVG header for pdfpage -->
<p align="center">
  <svg width="600" height="200" viewBox="0 0 600 200" xmlns="http://www.w3.org/2000/svg">
    <!-- Background -->
    <rect width="600" height="200" fill="#1e2433"/>

    <!-- Grid pattern -->
    <defs>
      <pattern id="grid" width="25" height="25" patternUnits="userSpaceOnUse">
        <path d="M 25 0 L 0 0 0 25" fill="none" stroke="#2a3245" stroke-width="0.5"/>
      </pattern>
      <linearGradient id="docGrad" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" style="stop-color:#e74c3c"/>
        <stop offset="100%" style="stop-color:#c0392b"/>
      </linearGradient>
      <linearGradient id="pageGrad" x1="0%" y1="0%" x2="0%" y2="100%">
        <stop offset="0%" style="stop-color:#ecf0f1"/>
        <stop offset="100%" style="stop-color:#bdc3c7"/>
      </linearGradient>
    </defs>
    <rect width="600" height="200" fill="url(#grid)"/>

    <!-- PDF document icon (left) -->
    <rect x="80" y="40" width="100" height="130" rx="8" fill="url(#docGrad)"/>
    <rect x="90" y="55" width="80" height="12" rx="2" fill="#fff" opacity="0.9"/>
    <rect x="90" y="75" width="60" height="8" rx="2" fill="#fff" opacity="0.6"/>
    <rect x="90" y="90" width="70" height="8" rx="2" fill="#fff" opacity="0.6"/>
    <rect x="90" y="105" width="50" height="8" rx="2" fill="#fff" opacity="0.6"/>
    <!-- Folded corner -->
    <path d="M 160 40 L 180 40 L 180 60 Z" fill="#922b21"/>
    <path d="M 160 40 L 180 60 L 160 60 Z" fill="#c0392b"/>

    <!-- Arrow transformation (center) -->
    <path d="M 200 100 L 280 100" stroke="#3498db" stroke-width="4" stroke-linecap="round" stroke-dasharray="8 4"/>
    <polygon points="290,100 270,90 270,110" fill="#3498db"/>

    <!-- Split pages icon (right) -->
    <rect x="310" y="50" width="55" height="110" rx="6" fill="url(#pageGrad)"/>
    <rect x="320" y="65" width="35" height="6" rx="1" fill="#95a5a6"/>
    <rect x="320" y="78" width="25" height="4" rx="1" fill="#bdc3c7"/>
    <rect x="320" y="88" width="30" height="4" rx="1" fill="#bdc3c7"/>

    <rect x="365" y="50" width="55" height="110" rx="6" fill="url(#pageGrad)" opacity="0.8"/>
    <rect x="375" y="65" width="35" height="6" rx="1" fill="#95a5a6"/>
    <rect x="375" y="78" width="25" height="4" rx="1" fill="#bdc3c7"/>
    <rect x="375" y="88" width="30" height="4" rx="1" fill="#bdc3c7"/>

    <!-- Tool indicators (right side) -->
    <g transform="translate(470, 60)">
      <!-- Scissors icon for split -->
      <circle cx="20" cy="30" r="18" fill="none" stroke="#2ecc71" stroke-width="2"/>
      <path d="M 10 20 Q 20 35 30 20" stroke="#2ecc71" stroke-width="2" fill="none"/>
      <text x="20" y="35" font-family="sans-serif" font-size="10" fill="#2ecc71" text-anchor="middle">SPLIT</text>
    </g>

    <g transform="translate(470, 100)">
      <!-- Merge icon -->
      <rect x="5" y="15" width="30" height="20" rx="3" fill="#9b59b6" opacity="0.8"/>
      <rect x="15" y="15" width="30" height="20" rx="3" fill="#9b59b6"/>
      <text x="25" y="50" font-family="sans-serif" font-size="10" fill="#9b59b6" text-anchor="middle">MERGE</text>
    </g>

    <!-- Bottom accent -->
    <rect x="0" y="195" width="600" height="5" fill="#e74c3c" opacity="0.7"/>
  </svg>
</p>

---

## Installation

### Method 1: pip (recommended)

```bash
pip install pdfpage
```

### Method 2: From source

```bash
git clone https://github.com/izag8216/pdfpage.git
cd pdfpage
pip install -e .
```

## Quick Start

```bash
# Extract specific pages
pdfpage extract report.pdf --pages 1,3,5-10 --output extracted.pdf

# Split into page ranges
pdfpage split large.pdf --ranges 1-10 11-20 21-30 --output-dir ./parts

# Merge multiple PDFs
pdfpage merge part1.pdf part2.pdf --output combined.pdf

# Rotate pages
pdfpage rotate scan.pdf --degrees 90 --pages 2,4 --output rotated.pdf

# Get PDF info
pdfpage info document.pdf
```

## Features

| Feature | Description |
|---------|-------------|
| **Extract** | Pull specific pages from a PDF using page numbers or ranges |
| **Split** | Divide a PDF into multiple parts by page ranges |
| **Merge** | Combine multiple PDF files into one |
| **Rotate** | Rotate specific pages (90, 180, 270 degrees) |
| **Info** | Display PDF metadata and page count |
| **Pipe-friendly** | Works with shell pipes and scripts |

## Commands

| Command | Description |
|---------|-------------|
| `extract` | Extract pages to new PDF |
| `split` | Split PDF into multiple files |
| `merge` | Merge multiple PDFs into one |
| `rotate` | Rotate pages in PDF |
| `info` | Show PDF information |

## Page Specification

Pages are specified as 1-indexed numbers or ranges:

| Format | Example | Description |
|--------|---------|-------------|
| Single | `1` | Page 1 |
| Multiple | `1,3,5` | Pages 1, 3, and 5 |
| Range | `1-10` | Pages 1 through 10 |
| Mixed | `1,3,5-10` | Pages 1, 3, and 5 through 10 |

## Examples

### Extract first 5 pages

```bash
pdfpage extract input.pdf --pages 1-5 --output output.pdf
```

### Extract non-contiguous pages

```bash
pdfpage extract input.pdf --pages 1,3,7,10-15 --output output.pdf
```

### Split into 3 equal parts

```bash
pdfpage split big.pdf --ranges 1-33 34-66 67-99 --output-dir ./split
```

### Merge in order

```bash
pdfpage merge chapter1.pdf chapter2.pdf chapter3.pdf --output book.pdf
```

### Rotate scanned pages

```bash
pdfpage rotate scan.pdf --degrees 90 --pages 2,4,6 --output corrected.pdf
```

## Python API

```python
from pdfpage import extract_pages, merge_pdfs, rotate_pages

# Extract pages
result = extract_pages("input.pdf", "output.pdf", [0, 2, 4])

# Merge PDFs
result = merge_pdfs(["a.pdf", "b.pdf"], "merged.pdf")

# Rotate pages
result = rotate_pages("input.pdf", "output.pdf", 90, [1, 3])
```

## License

MIT License — see [LICENSE](LICENSE) for details.

## Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for setup instructions.

---

*pdfpage — PDF manipulation made simple.*