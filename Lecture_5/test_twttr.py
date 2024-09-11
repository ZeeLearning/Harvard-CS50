from twttr import shorten 

def test_shorten_uppercase_vowels():
    assert shorten("HELLO") == "HLL"
    assert shorten("INSTAGRAM") == "NSTGRM"

def test_shorten_lowercase_vowels():
    assert shorten("hello") == "hll"