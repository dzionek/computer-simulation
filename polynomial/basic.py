from itertools import zip_longest  # used in __add__ magic method

"""
This module was an assignment for Computer Simulation 2020.
Mark: 5/5 points    Feedback: Excellent!
"""

class Poly:
    """
    Class representing polynomials.
    Attributes:
        coefs [float]: list with coefficients of a polynomial starting from the right.
            e.g. 1.3 - 2x^2 + 3x^3 has the list coefficient [1.3, 0, -2, 3].
    """

    def __init__(self, coefs: [float]) -> None:
        # Check if coefs is a nonempty list of numbers.
        if Poly.validate_input(coefs):
            self.coefs = coefs
        else:
            raise TypeError("Invalid input")

    @staticmethod
    def validate_input(args: [float]) -> bool:
        """Check if the argument is a nonempty list of numbers."""
        if (args and isinstance(args, list) and
                all([isinstance(arg, int) or isinstance(arg, float) for arg in args])):
            return True
        else:
            return False

    def order(self) -> int:
        """Return the order of a polynomial."""
        if self.coefs != [0]:
            return len(self.coefs) - 1
        else:
            raise Exception("Zero polynomial.")

    def __add__(self, other: 'Poly instance') -> 'Poly instance':
        """Return the sum of two polynomials."""
        zipped_list = list(zip_longest(self.coefs, other.coefs, fillvalue=0))
        new_coefs = list(map(sum, zipped_list))
        return Poly(new_coefs)

    def derivative(self) -> 'Poly instance':
        """Return the derivative of a polynomial."""
        coefs = self.coefs
        if len(coefs) == 1:
            return Poly([0])
        else:
            for i in range(len(coefs)):
                coefs[i] *= i
            return Poly(coefs[1:])

    def antiderivative(self, const: float) -> 'Poly instance':
        """Return the antiderivative of a polynomial with the given integration constant."""
        coefs = self.coefs
        for i in range(len(coefs)):
            coefs[i] /= i + 1
        return Poly([const] + coefs)

    def __repr__(self) -> str:
        """Return the representation of a polynomial."""
        coefs = [int(coef) if float(coef).is_integer() else coef for coef in self.coefs]  # 1.0 -> 1, 5.73 -> 5.73

        coefs_string = list(map(str, coefs))  # ['-1', '1', '0', '9.3']

        coefs_enumerated = list(enumerate(coefs_string))  # [(0, '-1'), (1, '1'), (2, '0'), (3, '9.3')]

        coefs_with_x = [coef + 'x^' + str(num)
                        for (num, coef) in coefs_enumerated if coef != '0']  # ['-1x^0', '1x^1', '9.3x^3']

        exp_with_pluses = ' + '.join(coefs_with_x)  # '-1x^0 + 1x^1 + 9.3x^3'

        exp_zero_exponent = exp_with_pluses.replace('x^0', '')  # '-1 + 1x^1 + 9.3x^3'
        exp_one_exponent = exp_zero_exponent.replace('x^1 ', 'x ')  # '-1 + 1x + 9.3x^3'
        exp_better_minuses = exp_one_exponent.replace('+ -', '- ')  # '-1 + 1x + 9.3x^3'
        exp_one_coefs = exp_better_minuses.replace(' 1x', ' x')  # '-1 + x + 9.3x^3'

        return exp_one_coefs


def main() -> None:
    """
    Main function doing all that was needed for the checkpoint:
    print given polynomials, find an order of a polynomial,
    sum of two polynomials, the derivative and the antiderivative of the derivative.
    """
    poly_a = Poly([2, 0, 4, -1, 0, 6])
    poly_b = Poly([-1, -3, 0, 4.5])

    print("Polynomials are:")
    print("P_a(x) = " + str(poly_a) + ",")
    print("P_b(x) = " + str(poly_b) + ".")

    print("The order of P_a(x) is " + str(poly_a.order()) + ".")
    print("The sum of the two polynomials is " + str(poly_a + poly_b) + ".")

    first_derivative = poly_a.derivative()

    print("The first derivative of P_a(x) is " + str(first_derivative) + ".")
    print("The antiderivative of d(P_a(x))/dx is " + str(first_derivative.antiderivative(2)) + ".")


if __name__ == "__main__":
    main()