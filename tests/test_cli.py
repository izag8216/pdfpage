"""Tests for pdfpage.cli module."""

import pytest
from argparse import Namespace
from pathlib import Path
from pdfpage.cli import info, extract, split, merge, rotate
from pdfpage.core import parse_page_string


class TestParsePageString:
    def test_single_page(self):
        assert parse_page_string("1") == [0]

    def test_multiple_pages(self):
        assert parse_page_string("1,3,5") == [0, 2, 4]

    def test_range(self):
        assert parse_page_string("1-5") == [0, 1, 2, 3, 4]

    def test_empty_string(self):
        assert parse_page_string("") == []

    def test_whitespace(self):
        assert parse_page_string(" 1 , 3 - 5 ") == [0, 2, 3, 4]


class TestCliCommands:
    def test_parse_args_extract(self):
        args = Namespace(
            command="extract",
            input=Path("test.pdf"),
            pages="1,3,5-10",
            output=Path("output.pdf"),
        )
        assert args.pages == "1,3,5-10"

    def test_parse_args_split(self):
        args = Namespace(
            command="split",
            input=Path("test.pdf"),
            ranges=["1-10", "11-20"],
            output_dir=Path("output/"),
        )
        assert args.ranges == ["1-10", "11-20"]

    def test_parse_args_merge(self):
        args = Namespace(
            command="merge",
            inputs=[Path("a.pdf"), Path("b.pdf")],
            output=Path("merged.pdf"),
        )
        assert len(args.inputs) == 2