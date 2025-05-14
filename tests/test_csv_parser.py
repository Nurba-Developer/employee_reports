import pytest
from parsers.csv_parser import parse_csv_file
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def test_parse_csv_file(tmp_path):
    csv_content = "name,department,hours_worked,salary\nJohn,IT,160,50"
    test_file = tmp_path / "test.csv"
    test_file.write_text(csv_content)

    data = parse_csv_file(str(test_file))
    assert len(data) == 1
    assert data[0]["name"] == "John"
    assert data[0]["rate"] == 50
    assert data[0]["hours_worked"] == 160
