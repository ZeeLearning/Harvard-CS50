import pytest
from working import convert

def test_correct_format():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"

def test_invalid_minutes():
    with pytest.raises(ValueError):
        convert("8:60 AM to 4:00 PM")

def test_invalid_input_format():
    with pytest.raises(ValueError):
        convert("9:00 AM - 5:00 PM")
