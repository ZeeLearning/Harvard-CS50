from numb3rs import validate

def test_IPV4_not_number():
    assert validate("cat") == False

def test_IPV4():
    assert validate("1.2.3.4") == True

def test_IPV4_not_255():
    assert validate("275.3.6.28") == False