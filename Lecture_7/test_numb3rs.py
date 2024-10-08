from numb3rs import validate

def test_IPV4_not_number():
    assert validate("cat") == False

def test_IPV4():
    assert validate("1.2.3.4") == True
    assert validate("192.168.1.1") == True
    assert validate("0.255.255.255") == True
    assert validate("255.0.0.1") == True

def test_IPV4_out_of_range():
    assert validate("300.100.50.25") == False
    assert validate("1.300.299.298") == False

