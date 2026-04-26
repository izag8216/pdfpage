#!/usr/bin/env python3
"""Basic example: extract pages from a PDF."""

from pdfpage import extract_pages, parse_page_string

def main():
    input_file = "sample.pdf"
    output_file = "extracted.pdf"

    # Extract pages 1, 3, and 5 through 10
    pages = parse_page_string("1,3,5-10")
    print(f"Extracting pages: {[p+1 for p in pages]}")

    try:
        result = extract_pages(input_file, output_file, pages)
        print(f"Success! Extracted {result['extracted']} pages to {result['output']}")
    except FileNotFoundError:
        print(f"Error: {input_file} not found")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()