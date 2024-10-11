from um import count

def test_um():
    assert count("hello, um") == 1
    assert count("um, how are um you") == 2

def test_um_insubstring():
    assert count("yummy") == 0

def test_case_insensitivity():
    assert count("UM Um uM") == 3

def test_no_um():
    assert count("hello world") == 0