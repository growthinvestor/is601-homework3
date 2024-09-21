'''My Calculator Test'''
from calculator.operations import add, exponentiate, modulus, multiply, subtract, divide

def test_addition():
    '''Test that addition function works '''    
    assert add(2,2) == 4

def test_subtraction():
    '''Test that addition function works '''    
    assert subtract(2,2) == 0

def test_multiplication():
    '''Test that multiply works'''
    assert multiply(2,2) == 4

def test_division():
    '''Test division'''
    assert divide(2,2) == 1

def test_exponentiation():
    '''Test that exponentiation function works'''
    assert exponentiate(2, 3) == 8  # 2^3 = 8

def test_modulus():
    '''Test that modulus function works'''
    assert modulus(5, 3) == 2
    