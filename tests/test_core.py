"""Tests for pdfpage.core module."""

import pytest
from pdfpage.core import parse_page_string


class TestParsePageString:
    def test_single_page(self):
        assert parse_page_string("1") == [0]

    def test_multiple_pages(self):
        assert parse_page_string("1,3,5") == [0, 2, 4]

    def test_range(self):
        assert parse_page_string("1-5") == [0, 1, 2, 3, 4]

    def test_mixed(self):
        result = parse_page_string("1,3,5-10")
        assert 0 in result
        assert 2 in result
        assert 4 in result
        assert list(range(4, 10)) == [4, 5, 6, 7, 8, 9]

    def test_empty_string(self):
        assert parse_page_string("") == []

    def test_whitespace(self):
        assert parse_page_string(" 1 , 3 - 5 ") == [0, 2, 3, 4]

    def test_large_page_numbers(self):
        result = parse_page_string("100-105")
        assert result == [99, 100, 101, 102, 103, 104]