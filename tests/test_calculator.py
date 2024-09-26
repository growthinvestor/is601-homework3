'''My Calculator Test'''
from calculator import Calculator

def test_addition():
    '''Test that addition function works '''    
    assert Calculator.add(2,2) == 4

def test_subtraction():
    '''Test that addition function works '''    
    assert Calculator.subtract(2,2) == 0

def test_multiply():
    '''Test that addition function works '''    
    assert Calculator.multiply(2,2) == 4

def test_divide():
    '''Test that addition function works '''    
    assert Calculator.divide(2,2) == 1

def test_exponentiation():
    '''Test that exponentiation function works'''
    assert Calculator.exponentiate(2, 3) == 8  # 2^3 = 8

def test_modulus():
    '''Test that modulus function works'''
    assert Calculator.modulus(5, 3) == 2
