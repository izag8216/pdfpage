# pdfpage

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![PyPI](https://img.shields.io/badge/PyPI-v0.1.0-blue?style=for-the-badge&logo=pypi&logoColor=white)](https://pypi.org/project/pdfpage/)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen?style=for-the-badge)](tests/)

**PDFページ抽出・分割・結合・ローテーションCLIツール** — パイプライン対応、スクリプト可能、GUI不要。

---

<p align="center">
  <a href="https://github.com/izag8216/pdfpage">
    <img src="assets/header.svg" alt="pdfpage header" width="100%">
  </a>
</p>

<div align="center">

**[English](README.md) | [日本語](README.ja.md)**

</div>

---

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