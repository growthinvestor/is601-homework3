from calculator.calculation import Calculation
from calculator.operations import add, exponentiate, modulus, subtract, multiply, divide

class Calculator:
    @staticmethod
    def add(a,b):
        calculation = Calculation(a, b, add)  # Pass the add function from calculator.operations
        return calculation.get_result()
    @staticmethod
    def subtract(a,b):
        calculation = Calculation(a, b, subtract)  # Pass the add function from calculator.operations
        return calculation.get_result()
    @staticmethod
    def multiply (a,b):
        calculation = Calculation(a, b, multiply)  # Pass the add function from calculator.operations
        return calculation.get_result()
    @staticmethod
    def divide(a,b):
        calculation = Calculation(a, b, divide)  # Pass the add function from calculator.operations
        return calculation.get_result()
    @staticmethod
    def exponentiate(a, b):
        calculation = Calculation(a, b, exponentiate) # Pass the add function from calculator.operations
        return calculation.get_result()
    @staticmethod
    def modulus(a, b):
        calculation = Calculation(a, b, modulus)
        return calculation.get_result()
