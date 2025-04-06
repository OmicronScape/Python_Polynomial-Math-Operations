# Python_Polynomial-Math-Operations
Polynomial Class in Python: A Python implementation of a Polynomial class that supports addition, subtraction, multiplication by a number, evaluation for specific values, and a human-readable string representation. This program demonstrates object-oriented programming (OOP) principles by performing polynomial operations.


Polynomial Class Implementation
Overview

This repository contains a Python implementation of a Polynomial Class that models polynomials and supports basic polynomial operations such as addition, subtraction, multiplication, and evaluation. It demonstrates object-oriented programming (OOP) concepts in Python, such as class definition, method overloading, and string representation.

The Polynomial class allows you to:

    Add, subtract, and multiply polynomials.

    Multiply a polynomial by a scalar.

    Evaluate the polynomial for a specific value of x.

    Display the polynomial in a human-readable format.

Features

    Polynomial Representation: Polynomials are represented as a list of coefficients, with each index corresponding to the degree of the term.

    Operations: The class supports:

        Addition (+)

        Subtraction (-)

        Multiplication by a scalar (*)

        Evaluation at a specific value of x

    String Representation: The class includes a __str__ method to print the polynomial in a readable form (e.g., 3x^2 + 2x + 1).

Installation

To use this code, simply clone the repository:

git clone https://github.com/yourusername/polynomial-class.git

Then, navigate to the directory and run the script:

cd polynomial-class
python polynomial.py

Usage Example

# Create polynomial objects
P1 = Polynomial([1, 2, 3, 2, 1])
P2 = Polynomial([5, 4, 3])

# Display polynomials
print(f"P1 = {P1}")
print(f"P2 = {P2}")

# Polynomial operations
print(f"P1 + P2 = {P1 + P2}")
print(f"P1 - P2 = {P1 - P2}")
print(f"2 * P1 = {2 * P1}")
print(f"P1(3) = {P1.evaluate(3)}")

Example Output:

P1 = 1x^4 + 2x^3 + 3x^2 + 2x + 1
P2 = 5x^2 + 4x + 3
P1 + P2 = 1x^4 + 2x^3 + 8x^2 + 6x + 4
P1 - P2 = 1x^4 + 2x^3 - 2x^2 - 2x - 2
2 * P1 = 2x^4 + 4x^3 + 6x^2 + 4x + 2
P1(3) = 246

Classes and Methods
Polynomial Class

The Polynomial class is initialized with a list of coefficients, where each coefficient corresponds to a term in the polynomial, starting with the lowest degree.
Methods:

    __init__(self, coefficients): Initializes the polynomial with the given coefficients.

    __add__(self, other): Adds two polynomials.

    __sub__(self, other): Subtracts one polynomial from another.

    __mul__(self, num): Multiplies the polynomial by a scalar.

    __rmul__(self, num): Right multiplication by a scalar.

    evaluate(self, x): Evaluates the polynomial for a given value of x.

    __str__(self): Returns a string representation of the polynomial.

Contributing

Feel free to fork this project and submit pull requests. Contributions are welcome, and issues and suggestions can be raised in the GitHub Issues section.

