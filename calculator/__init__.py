# Import necessary modules and classes
from calculator.calculations import Calculations  # Manages history of calculations
from calculator.operations import add, subtract, multiply, divide, modulus, exponentiate  # Arithmetic operations
from calculator.calculation import Calculation  # Represents a single calculation
from decimal import Decimal  # For high-precision arithmetic
from typing import Callable  # For type hinting callable objects

# Definition of the Calculator class
class Calculator:
    @staticmethod
    def _perform_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        """Create and perform a calculation, then return the result."""
        
        calculation = Calculation.create(a, b, operation)
       
        Calculations.add_calculation(calculation)
        
        return calculation.perform()

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, add)

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, subtract)

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, multiply)

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, divide)
    
    @staticmethod
    def modulus(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, modulus)

    @staticmethod
    def exponentiate(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, exponentiate)

