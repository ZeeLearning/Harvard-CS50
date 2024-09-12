from bank import value

def test_value_hello():
    assert value("hello") == 0

def test_value_start_with_h():
    assert value("h") == 20 

def test_value():
    assert value("Whatsup") == 100

def test_value_upper_hello():
    assert value("HELLO") == 0 

def test_value_upper_start_with_h():
    assert value("H") == 20 

def test_value_phrase():
    assert value("hello, newman") == 0