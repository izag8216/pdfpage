"""Core PDF operations: extract, split, merge, rotate."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Sequence


class PdfReader:
    def __init__(self, filepath: str | Path) -> None:
        from pypdf import PdfReader as _PdfReader

        self._reader = _PdfReader(str(filepath))
        self.filepath = Path(filepath)

    @property
    def page_count(self) -> int:
        return len(self._reader.pages)

    def extract_pages(self, pages: Sequence[int]) -> list:
        return [self._reader.pages[i] for i in pages]

    @property
    def metadata(self) -> dict:
        info = self._reader.metadata
        return {
            "title": info.get("/Title", ""),
            "author": info.get("/Author", ""),
            "subject": info.get("/Subject", ""),
            "creator": info.get("/Creator", ""),
            "producer": info.get("/Producer", ""),
        } if info else {}


class PdfWriter:
    def __init__(self) -> None:
        from pypdf import PdfWriter as _PdfWriter

        self._writer = _PdfWriter()

    def add_pages(self, pages: list) -> None:
        for page in pages:
            self._writer.add_page(page)

    def write(self, output_path: str | Path) -> None:
        with open(str(output_path), "wb") as f:
            self._writer.write(f)


def parse_page_string(page_string: str) -> list[int]:
    if not page_string.strip():
        return []

    pages: set[int] = set()
    parts = page_string.split(",")

    for part in parts:
        part = part.strip()
        if not part:
            continue

        if "-" in part:
            range_match = re.match(r"(\d+)-(\d+)", part)
            if range_match:
                start = int(range_match.group(1)) - 1
                end = int(range_match.group(2))
                pages.update(range(start, end))
        else:
            pages.add(int(part) - 1)

    return sorted(pages)


def extract_pages(input_path: str | Path, output_path: str | Path, pages: list[int], info_only: bool = False) -> dict:
    reader = PdfReader(input_path)
    total = reader.page_count

    if info_only:
        return {
            "total_pages": total,
            "metadata": reader.metadata,
        }

    valid_pages = [p for p in pages if 0 <= p < total]

    if not valid_pages:
        raise ValueError(f"No valid pages in range 1-{total}")

    extracted = reader.extract_pages(valid_pages)

    writer = PdfWriter()
    writer.add_pages(extracted)
    writer.write(output_path)

    return {
        "extracted": len(valid_pages),
        "total_pages": total,
        "output": str(output_path),
    }


def split_pdf(input_path: str | Path, output_dir: str | Path, ranges: list[list[int]]) -> list[dict]:
    reader = PdfReader(input_path)
    total = reader.page_count
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    results = []

    for i, page_range in enumerate(ranges):
        valid = [p for p in page_range if 0 <= p < total]

        if not valid:
            continue

        pages = reader.extract_pages(valid)
        writer = PdfWriter()
        writer.add_pages(pages)

        output_file = output_dir / f"part_{i + 1:03d}.pdf"
        writer.write(output_file)

        results.append({
            "part": i + 1,
            "pages": len(valid),
            "output": str(output_file),
        })

    return results


def merge_pdfs(input_paths: list[str | Path], output_path: str | Path) -> dict:
    writer = PdfWriter()

    for path in input_paths:
        reader = PdfReader(path)
        pages = reader.extract_pages(range(reader.page_count))
        writer.add_pages(pages)

    writer.write(output_path)

    return {
        "merged": len(input_paths),
        "output": str(output_path),
    }


def rotate_pages(input_path: str | Path, output_path: str | Path, degrees: int, pages: list[int]) -> dict:
    reader = PdfReader(input_path)
    total = reader.page_count

    valid_pages = [p for p in pages if 0 <= p < total]

    if not valid_pages:
        raise ValueError(f"No valid pages in range 1-{total}")

    writer = PdfWriter()

    for idx in range(total):
        page = reader._reader.pages[idx]
        if idx in valid_pages:
            page.rotate(degrees)
        writer.add_page(page)

    writer.write(output_path)

    return {
        "rotated": len(valid_pages),
        "total_pages": total,
        "degrees": degrees,
        "output": str(output_path),
    }