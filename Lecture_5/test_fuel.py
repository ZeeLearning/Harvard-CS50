import pytest
from fuel import convert, gauge

# Test cases for the convert function
def test_convert_valid_fraction():
    assert convert("1/2") == 50  # 50% for 1/2
    assert convert("1/4") == 25  # 25% for 1/4
    assert convert("3/4") == 75  # 75% for 3/4
    assert convert("99/100") == 99  # 99% for 99/100
    assert convert("1/100") == 1   # 1% for 1/100

def test_convert_invalid_fraction():
    with pytest.raises(ValueError):
        convert("3/2")  # ValueError because x > y
    with pytest.raises(ValueError):
        convert("a/b")  # ValueError because of invalid characters
    with pytest.raises(ZeroDivisionError):
        convert("1/0")  # ZeroDivisionError because denominator is 0

# Test cases for the gauge function
def test_gauge():
    assert gauge(1) == "E"  # 1% or less should return "E"
    assert gauge(99) == "F"  # 99% or more should return "F"
    assert gauge(50) == "50%"  # Anything between should return percentage with %

