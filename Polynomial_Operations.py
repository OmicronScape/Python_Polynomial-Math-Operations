# OBJECT ORIENTED PROGRAMMING, POLYNOMIAL CLASS

"""
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                    |-------> PROGRAM INSTRUCTIONS <-------|                                                                           |                                
|---> Step 1: The Polynomial class represents polynomials with a list of coefficients. (Class: Polynomial)                                                                 |
|---> Step 2: Create polynomial objects using the Polynomial class. (Class: Polynomial)                                                                                     |
|---> Step 3: Implement the addition operator (+) to sum two polynomials. (Class: Polynomial, Method: __add__)                                                           |
|---> Step 4: Implement the subtraction operator (-) to subtract two polynomials. (Class: Polynomial, Method: __sub__, Sub-question B)                                     |
|---> Step 5: Implement the multiplication operator (*) to multiply a polynomial by a number. (Class: Polynomial, Method: __mul__, Sub-question A)                      |
|---> Step 6: Implement the method evaluate(x), which calculates the polynomial value for a given x value. (Class: Polynomial, Method: evaluate, Sub-question C)        |
|---> Step 7: Implement the method __str__(), which displays the polynomial in a readable form. (Class: Polynomial, Method: __str__, Sub-question D)                    |
|---> Step 8: Example usage of the class, performing operations between polynomials and displaying the results. (Class: Polynomial, Main program: __main__)              |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
"""

#---------------------------------------------------PROGRAM START------------------------------------------------------

class Polynomial:
    # Step 1
    # Constructor of the Polynomial Class
    # coefficients: the list of coefficients where the index represents the power of x
    def __init__(self, coefficients):
        self.coefficients = coefficients  # List of coefficients, from the smallest to the largest degree

    # Overload the addition operator for polynomials
    def __add__(self, other):
        if isinstance(other, Polynomial):
            max_len = max(len(self.coefficients), len(other.coefficients))  # Maximum length of polynomials
            self_coeffs = self.coefficients + [0] * (max_len - len(self.coefficients))
            other_coeffs = other.coefficients + [0] * (max_len - len(other.coefficients))
            result_coeffs = []
            for a, b in zip(self_coeffs, other_coeffs):
                result_coeffs.append(a + b)
            return Polynomial(result_coeffs)
        else:
            return NotImplemented

    # Overload the multiplication operator to multiply a polynomial by a number
    # Step 5
    # Sub-question A
    def __mul__(self, num):
        result = [coeff * num for coeff in self.coefficients]
        return Polynomial(result)

    # Multiplication from the right
    def __rmul__(self, num):
        return self.__mul__(num)

    # Sub-question B
    def __sub__(self, other):
        # Subtract two polynomials
        negated_other = Polynomial([-coeff for coeff in other.coefficients])
        return self.__add__(negated_other)
    
    # Step 6
    # Sub-question C
    def evaluate(self, x):
        # Calculate the value of the polynomial for a given value of the independent variable x
        result = 0
        for i, coeff in enumerate(self.coefficients):
            result += coeff * (x ** i)
        return result
    
    # Step 7 
    # Sub-question D
    def __str__(self):
        # String representation for polynomial objects
        terms = []
        for i in range(len(self.coefficients) - 1, -1, -1):
            coeff = self.coefficients[i]
            if coeff != 0:
                if i == 0:
                    terms.append(f"{coeff}")
                elif i == 1:
                    terms.append(f"{coeff}x")
                else:
                    terms.append(f"{coeff}x^{i}")
        return " + ".join(terms) if terms else "0"
    
# Step 8
# Example usage of the Polynomial class
if __name__ == "__main__":
    P1 = Polynomial([1, 2, 3, 2, 1])
    P2 = Polynomial([5, 4, 3])

    print(f"P1 = {P1}")
    print(f"P2 = {P2}")
    print(f"2*P1 = {2 * P1}")
    print(f"P2*2 = {P2 * 2}")
    print(f"P1 + P2 = {P1 + P2}")
    print(f"P1 - P2 = {P1 - P2}")
    print(f"P2 - P1 = {P2 - P1}")
    print(f"P1(3) = {P1.evaluate(3)}")
    print(f"P2(3) = {P2.evaluate(3)}")


#---------------------------------------------------PROGRAM END------------------------------------------------------
