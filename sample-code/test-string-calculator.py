import pytest
from string_calculator import string_calculator

def test_empty_string():
    assert string_calculator("") == 0

def test_single_number():
    assert string_calculator("1") == 1

def test_two_numbers():
    assert string_calculator("1,2") == 3

def test_multiple_numbers():
    assert string_calculator("1,2,3,4,5") == 15

def test_newline_between_numbers():
    assert string_calculator("1\n2,3") == 6

def test_negative_numbers():
    with pytest.raises(ValueError, match="Negatives not allowed: -1, -2"):
        string_calculator("-1,2,-2")

def test_numbers_greater_than_1000():
    assert string_calculator("2,1001,6") == 8

def test_custom_delimiter():
    assert string_calculator("//;\n1;2") == 3