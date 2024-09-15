from plates import is_valid

def test_starts_with_two_letters():
    assert is_valid("AA1234") == True  
    assert is_valid("A12345") == False 
    assert is_valid("123456") == False  

def test_length_limits():
    assert is_valid("AA") == True  
    assert is_valid("AAAAAA") == True  
    assert is_valid("A") == False  
    assert is_valid("AAAAAAA") == False  

def test_no_punctuation():
    assert is_valid("ABC123") == True  
    assert is_valid("ABC 123") == False 
    assert is_valid("ABC.123") == False  

def test_numbers_placement():
    assert is_valid("ABC123") == True  
    assert is_valid("AB12C3") == False  
    assert is_valid("ABC12A") == False  

def test_no_leading_zero():
    assert is_valid("ABC123") == True  
    assert is_valid("ABC012") == False 

def test_alphanumeric():
    assert is_valid("ABC123") == True  
    assert is_valid("ABC!123") == False  
    assert is_valid("AB@CD") == False  
    assert is_valid("12345") == False 


