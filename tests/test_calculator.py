from src.calculator import add, subtract, multiply, divide, power, average

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 2) == 3

def test_multiply():
    assert multiply(3, 4) == 12

def test_divide():
    assert divide(10, 2) == 5

def test_power():
    assert power(2, 3) == 8

def test_average():
    assert average([10, 20, 30]) == 20
