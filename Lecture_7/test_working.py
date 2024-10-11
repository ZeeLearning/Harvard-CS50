from working import convert

def test_correct_format():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"

def test_invalid_start_time():
    try:
        convert("0 AM to 12:00 PM")
    except ValueError as e:
        assert str(e) == "Invalid start time"

def test_invalid_end_time():
    try:
        convert("12:00 PM to 12:00 AM")
    except ValueError as e:
        assert str(e) == "Invalid end time"

def test_invalid_input_format():
    try:
        convert("9 AM - 5 PM")
    except ValueError as e:
        assert str(e) == "Invalid input format"
