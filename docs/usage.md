# Usage Guide — pdfpage

## Basic Workflow

### 1. Extract Pages

Extract specific pages from a PDF:

```bash
pdfpage extract report.pdf --pages 1,3,5-10 --output extracted.pdf
```

### 2. Split PDF

Split a large PDF into multiple parts:

```bash
pdfpage split large.pdf --ranges 1-10 11-20 21-30 --output-dir ./parts
```

### 3. Merge PDFs

Combine multiple PDFs:

```bash
pdfpage merge chapter1.pdf chapter2.pdf chapter3.pdf --output book.pdf
```

### 4. Rotate Pages

Fix scanned documents:

```bash
pdfpage rotate scan.pdf --degrees 90 --pages 2,4 --output corrected.pdf
```

## Page Specification Format

Pages can be specified in multiple ways:

| Format | Example | Description |
|--------|---------|-------------|
| Single | `1` | Page 1 |
| Comma-separated | `1,3,5` | Pages 1, 3, and 5 |
| Range | `1-10` | Pages 1 through 10 |
| Mixed | `1,3,5-10` | Pages 1, 3, and 5 through 10 |

## Common Use Cases

### Extract first 10 pages

```bash
pdfpage extract document.pdf --pages 1-10 --output first_part.pdf
```

### Extract non-consecutive pages

```bash
pdfpage extract document.pdf --pages 1,5,10,15,20 --output selected.pdf
```

### Split into equal chunks

For a 30-page PDF, split into 3 parts of 10 pages each:

```bash
pdfpage split document.pdf --ranges 1-10 11-20 21-30 --output-dir split/
```

### Merge in specific order

```bash
pdfpage merge intro.pdf chapter1.pdf chapter2.pdf appendix.pdf --output book.pdf
```

### Rotate all pages 180 degrees

```bash
pdfpage rotate scanned.pdf --degrees 180 --output flipped.pdf
```

### Rotate only odd pages

```bash
pdfpage rotate scan.pdf --degrees 90 --pages 1,3,5,7,9 --output corrected.pdf
```

## Python Script Integration

```python
from pdfpage import extract_pages, merge_pdfs, rotate_pages

# Extract pages
extract_pages("input.pdf", "output.pdf", [0, 2, 4])

# Merge PDFs
merge_pdfs(["a.pdf", "b.pdf"], "merged.pdf")

# Rotate specific pages
rotate_pages("input.pdf", "output.pdf", 90, [1, 3])
```

## Error Handling

```python
from pdfpage import extract_pages

try:
    result = extract_pages("input.pdf", "output.pdf", [0, 100])
except ValueError as e:
    print(f"Error: {e}")
```

## Examples

See `examples/basic/` for runnable examples.