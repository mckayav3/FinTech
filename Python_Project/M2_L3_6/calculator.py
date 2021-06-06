
from calculations.add import add
from calculations.sub import sub
from calculations.mul import mul

from calculations.mean.arithmetic import arithmetic_mean
from calculations.mean.harmonic import harmonic_mean

def calculator():

    # Define calculator values
    a = 2
    b = 7
    c = 20

    # Test Addition
    result = add(a, b)
    print(f"Addition: {result}")

    # Test Subtraction
    result = sub(a, b)
    print(f"Subtraction: {result}")

    # Test Multiplication
    result = mul(a, b)
    print(f"Multiplication: {result}")

    # Test Mean
    result = arithmetic_mean([a, b, c])
    print(f"Arithmetic Mean: {result}")


calculator()