# pdfpage

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![PyPI](https://img.shields.io/badge/PyPI-v0.1.0-blue?style=for-the-badge&logo=pypi&logoColor=white)](https://pypi.org/project/pdfpage/)

**PDFページ抽出・分割・結合・ローテーションCLIツール** — パイプライン対応、スクリプト可能、GUI不要。

---

<p align="center">
<svg width="640" height="220" viewBox="0 0 640 220" xmlns="http://www.w3.org/2000/svg">
<defs>
<linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
<stop offset="0%" stop-color="#1a1a2e"/>
<stop offset="50%" stop-color="#16213e"/>
<stop offset="100%" stop-color="#0f0f23"/>
</linearGradient>
<linearGradient id="docRed" x1="0%" y1="0%" x2="100%" y2="100%">
<stop offset="0%" stop-color="#e74c3c"/>
<stop offset="100%" stop-color="#c0392b"/>
</linearGradient>
<linearGradient id="docBlue" x1="0%" y1="0%" x2="100%" y2="100%">
<stop offset="0%" stop-color="#3498db"/>
<stop offset="100%" stop-color="#2980b9"/>
</linearGradient>
<linearGradient id="docGreen" x1="0%" y1="0%" x2="100%" y2="100%">
<stop offset="0%" stop-color="#2ecc71"/>
<stop offset="100%" stop-color="#27ae60"/>
</linearGradient>
<linearGradient id="pageWhite" x1="0%" y1="0%" x2="0%" y2="100%">
<stop offset="0%" stop-color="#ffffff"/>
<stop offset="100%" stop-color="#ecf0f1"/>
</linearGradient>
<filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
<feGaussianBlur stdDeviation="2" result="blur"/>
<feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
</filter>
</defs>

<rect width="640" height="220" rx="12" fill="url(#bg)"/>

<g fill="none" stroke="#2d2d44" stroke-width="0.5">
<line x1="0" y1="55" x2="640" y2="55"/>
<line x1="0" y1="110" x2="640" y2="110"/>
<line x1="0" y1="165" x2="640" y2="165"/>
<line x1="160" y1="0" x2="160" y2="220"/>
<line x1="320" y1="0" x2="320" y2="220"/>
<line x1="480" y1="0" x2="480" y2="220"/>
</g>

<g transform="translate(40, 50)">
<rect width="90" height="120" rx="6" fill="url(#docRed)"/>
<rect x="8" y="15" width="60" height="8" rx="2" fill="#fff" opacity="0.95"/>
<rect x="8" y="30" width="74" height="5" rx="1.5" fill="#fff" opacity="0.5"/>
<rect x="8" y="42" width="55" height="5" rx="1.5" fill="#fff" opacity="0.4"/>
<rect x="8" y="54" width="65" height="5" rx="1.5" fill="#fff" opacity="0.4"/>
<rect x="8" y="66" width="40" height="5" rx="1.5" fill="#fff" opacity="0.3"/>
<path d="M 78 0 L 90 0 L 90 12 Z" fill="#922b21"/>
</g>

<path d="M 155 110 L 215 110" stroke="#3498db" stroke-width="3" stroke-linecap="round" filter="url(#glow)"/>
<polygon points="225,110 205,95 205,125" fill="#3498db" filter="url(#glow)"/>

<g transform="translate(245, 50)">
<rect width="75" height="50" rx="4" fill="url(#pageWhite)"/>
<rect x="8" y="10" width="40" height="4" rx="1" fill="#bdc3c7"/>
<rect x="8" y="20" width="30" height="3" rx="1" fill="#d0d5d9"/>
<rect x="8" y="28" width="35" height="3" rx="1" fill="#d0d5d9"/>
<rect x="8" y="36" width="25" height="3" rx="1" fill="#d0d5d9"/>

<rect y="60" width="75" height="50" rx="4" fill="url(#pageWhite)" opacity="0.85"/>
<rect x="8" y="10" width="40" height="4" rx="1" fill="#bdc3c7"/>
<rect x="8" y="20" width="30" height="3" rx="1" fill="#d0d5d9"/>
<rect x="8" y="28" width="35" height="3" rx="1" fill="#d0d5d9"/>
<rect x="8" y="36" width="25" height="3" rx="1" fill="#d0d5d9"/>
</g>

<path d="M 345 110 L 405 110" stroke="#2ecc71" stroke-width="3" stroke-linecap="round" filter="url(#glow)"/>
<polygon points="415,110 395,95 395,125" fill="#2ecc71" filter="url(#glow)"/>

<g transform="translate(435, 50)">
<rect width="90" height="120" rx="6" fill="url(#docGreen)"/>
<rect x="8" y="15" width="60" height="8" rx="2" fill="#fff" opacity="0.95"/>
<rect x="8" y="30" width="74" height="5" rx="1.5" fill="#fff" opacity="0.5"/>
<rect x="8" y="42" width="55" height="5" rx="1.5" fill="#fff" opacity="0.4"/>
<rect x="8" y="54" width="65" height="5" rx="1.5" fill="#fff" opacity="0.4"/>
<rect x="8" y="66" width="40" height="5" rx="1.5" fill="#fff" opacity="0.3"/>
<path d="M 78 0 L 90 0 L 90 12 Z" fill="#1e8449"/>
</g>

<g transform="translate(545, 80)">
<text x="0" y="0" font-family="monospace" font-size="10" fill="#e74c3c" font-weight="bold">PDF</text>
<text x="0" y="15" font-family="monospace" font-size="9" fill="#3498db">抽出</text>
<text x="0" y="28" font-family="monospace" font-size="9" fill="#2ecc71">分割</text>
<text x="0" y="41" font-family="monospace" font-size="9" fill="#9b59b6">結合</text>
<text x="0" y="54" font-family="monospace" font-size="9" fill="#f39c12">回転</text>
</g>

<rect x="0" y="210" width="640" height="10" rx="0" fill="#e74c3c" opacity="0.6"/>
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