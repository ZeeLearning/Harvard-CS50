from bank import value

def test_value_hello():
    assert value("hello") == 0

def test_value_start_with_h():
    assert value("h") == 20 

def test_value():
    assert value("Whatsup") == 100