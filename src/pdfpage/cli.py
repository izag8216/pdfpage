"""PDFPage CLI — PDF extraction, split, merge, and rotation tool."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from pdfpage import __version__
from pdfpage.core import (
    extract_pages,
    merge_pdfs,
    rotate_pages,
    split_pdf,
    parse_page_string,
)


def info(args: argparse.Namespace) -> int:
    from pypdf import PdfReader

    try:
        reader = PdfReader(str(args.input))
        print(f"Pages: {len(reader.pages)}")

        meta = reader.metadata
        if meta:
            for key in ["/Title", "/Author", "/Creator", "/Producer"]:
                val = meta.get(key)
                if val:
                    print(f"{key.strip('/')}: {val}")
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def extract(args: argparse.Namespace) -> int:
    try:
        pages = parse_page_string(args.pages)
        if not pages:
            print("Error: No valid pages specified", file=sys.stderr)
            return 1

        result = extract_pages(args.input, args.output, pages)
        print(f"Extracted {result['extracted']} pages to {result['output']}")
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def split(args: argparse.Namespace) -> int:
    try:
        all_ranges = []
        for r in args.ranges:
            parts = r.split(",")
            pages = parse_page_string(",".join(parts))
            all_ranges.append(pages)

        results = split_pdf(args.input, args.output_dir, all_ranges)
        print(f"Split into {len(results)} parts:")
        for r in results:
            print(f"  part_{r['part']:03d}.pdf — {r['pages']} pages")
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def merge(args: argparse.Namespace) -> int:
    try:
        input_paths = list(args.inputs)
        result = merge_pdfs(input_paths, args.output)
        print(f"Merged {result['merged']} PDFs to {result['output']}")
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def rotate(args: argparse.Namespace) -> int:
    try:
        pages = parse_page_string(args.pages) if args.pages else list(range(1000))
        result = rotate_pages(args.input, args.output, args.degrees, pages)
        print(f"Rotated {result['rotated']} pages by {args.degrees}° to {result['output']}")
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="pdfpage",
        description="PDF page extraction, split, merge, and rotation CLI tool",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    info_parser = subparsers.add_parser("info", help="Show PDF info")
    info_parser.add_argument("input", type=Path, help="Input PDF file")
    info_parser.set_defaults(func=info)

    extract_parser = subparsers.add_parser("extract", help="Extract pages")
    extract_parser.add_argument("input", type=Path, help="Input PDF file")
    extract_parser.add_argument("--pages", required=True, help="Pages to extract (e.g., 1,3,5-10)")
    extract_parser.add_argument("--output", required=True, type=Path, help="Output PDF file")
    extract_parser.set_defaults(func=extract)

    split_parser = subparsers.add_parser("split", help="Split PDF into parts")
    split_parser.add_argument("input", type=Path, help="Input PDF file")
    split_parser.add_argument("--ranges", required=True, nargs="+", help="Page ranges (e.g., 1-10 11-20)")
    split_parser.add_argument("--output-dir", required=True, type=Path, help="Output directory")
    split_parser.set_defaults(func=split)

    merge_parser = subparsers.add_parser("merge", help="Merge multiple PDFs")
    merge_parser.add_argument("inputs", nargs="+", type=Path, help="Input PDF files")
    merge_parser.add_argument("--output", required=True, type=Path, help="Output PDF file")
    merge_parser.set_defaults(func=merge)

    rotate_parser = subparsers.add_parser("rotate", help="Rotate pages")
    rotate_parser.add_argument("input", type=Path, help="Input PDF file")
    rotate_parser.add_argument("--degrees", type=int, required=True, help="Rotation degrees (90, 180, 270)")
    rotate_parser.add_argument("--pages", help="Pages to rotate (default: all)")
    rotate_parser.add_argument("--output", required=True, type=Path, help="Output PDF file")
    rotate_parser.set_defaults(func=rotate)

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        return 0

    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())