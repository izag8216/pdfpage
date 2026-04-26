# pdfpage

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![PyPI](https://img.shields.io/badge/PyPI-v0.1.0-blue?style=for-the-badge&logo=pypi&logoColor=white)](https://pypi.org/project/pdfpage/)

**PDFページ抽出・分割・結合・ローテーションCLIツール** — パイプライン対応、スクリプト可能、GUI不要。

---

<!-- Japanese README — Original SVG header for pdfpage -->
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
      <circle cx="20" cy="30" r="18" fill="none" stroke="#2ecc71" stroke-width="2"/>
      <path d="M 10 20 Q 20 35 30 20" stroke="#2ecc71" stroke-width="2" fill="none"/>
      <text x="20" y="35" font-family="sans-serif" font-size="10" fill="#2ecc71" text-anchor="middle">分割</text>
    </g>

    <g transform="translate(470, 100)">
      <rect x="5" y="15" width="30" height="20" rx="3" fill="#9b59b6" opacity="0.8"/>
      <rect x="15" y="15" width="30" height="20" rx="3" fill="#9b59b6"/>
      <text x="25" y="50" font-family="sans-serif" font-size="10" fill="#9b59b6" text-anchor="middle">結合</text>
    </g>

    <!-- Bottom accent -->
    <rect x="0" y="195" width="600" height="5" fill="#e74c3c" opacity="0.7"/>
  </svg>
</p>

---

## インストール

### 方法1: pip（推奨）

```bash
pip install pdfpage
```

### 方法2: ソースから

```bash
git clone https://github.com/izag8216/pdfpage.git
cd pdfpage
pip install -e .
```

## クイックスタート

```bash
# 特定ページを抽出
pdfpage extract report.pdf --pages 1,3,5-10 --output extracted.pdf

# ページ範囲で分割
pdfpage split large.pdf --ranges 1-10 11-20 21-30 --output-dir ./parts

# 複数PDFを結合
pdfpage merge part1.pdf part2.pdf --output combined.pdf

# ページをローテート
pdfpage rotate scan.pdf --degrees 90 --pages 2,4 --output rotated.pdf

# PDF情報を表示
pdfpage info document.pdf
```

## 機能

| 機能 | 説明 |
|------|------|
| **抽出** | ページ番号または範囲でPDFから特定ページを抽出 |
| **分割** | ページ範囲でPDFを複数ファイルに分割 |
| **結合** | 複数のPDFファイルを1つに結合 |
| **ローテート** | 特定ページを回転（90, 180, 270度） |
| **情報表示** | PDFメタデータとページ数を表示 |
| **パイプライン対応** | シェルパイプライトスクリプトと連携 |

## コマンド

| コマンド | 説明 |
|----------|------|
| `extract` | ページを新しいPDFに抽出 |
| `split` | PDFを複数ファイルに分割 |
| `merge` | 複数のPDFを1つに結合 |
| `rotate` | PDF内のページを回転 |
| `info` | PDF情報を表示 |

## ページ指定方法

ページは1起始の番号または範囲で指定：

| 形式 | 例 | 説明 |
|------|-----|------|
| 単一 | `1` | 1ページ |
| 複数 | `1,3,5` | 1ページ、3ページ、5ページ |
| 範囲 | `1-10` | 1ページから10ページ |
| 混合 | `1,3,5-10` | 1ページ、3ページ、5ページから10ページ |

## 使用例

### 最初の5ページを抽出

```bash
pdfpage extract input.pdf --pages 1-5 --output output.pdf
```

### 非連続ページを抽出

```bash
pdfpage extract input.pdf --pages 1,3,7,10-15 --output output.pdf
```

### 3等分に分割

```bash
pdfpage split big.pdf --ranges 1-33 34-66 67-99 --output-dir ./split
```

### 順番に結合

```bash
pdfpage merge chapter1.pdf chapter2.pdf chapter3.pdf --output book.pdf
```

### スキャンページを回転

```bash
pdfpage rotate scan.pdf --degrees 90 --pages 2,4,6 --output corrected.pdf
```

## Python API

```python
from pdfpage import extract_pages, merge_pdfs, rotate_pages

# ページを抽出
result = extract_pages("input.pdf", "output.pdf", [0, 2, 4])

# PDFを結合
result = merge_pdfs(["a.pdf", "b.pdf"], "merged.pdf")

# ページを回転
result = rotate_pages("input.pdf", "output.pdf", 90, [1, 3])
```

## ライセンス

MITライセンス — 詳細は [LICENSE](LICENSE) を参照。

## コントリビュート

コントリビュート大歓迎！設定手順は [CONTRIBUTING.md](CONTRIBUTING.md) を参照。

---

*pdfpage — PDF操作をシンプルに。*