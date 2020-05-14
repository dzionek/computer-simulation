from itertools import zip_longest
from typing import List

"""
This module contains my polynomial coursework
for Computer Simulation 2020.
"""

class Poly:
    """
    Class representing polynomials.
    Attributes:
        coefs List[float]: list with coefficients of a polynomial starting from the right.
            e.g. 1.3 - 2x^2 + 3x^3 has the list coefficient [1.3, 0, -2, 3].
    """

    def __init__(self, coefs: List[float]) -> None:
        """Instantiate poly instance, validates the given parameter."""
        if self._validate_input(coefs):
            coefs = self._remove_leading_zeros(coefs)
            self.coefs = coefs
        else:
            raise TypeError("Invalid input")

    @staticmethod
    def _validate_input(args: List[float]) -> bool:
        """Check if the argument is a nonempty list of real numbers."""
        return (args and isinstance(args, list)
                and all([
                    isinstance(arg, int)
                    or isinstance(arg, float)
                    for arg in args
                ]))

    @staticmethod
    def _remove_leading_zeros(lst: List[float]) -> List[float]:
        """Removes all leading zeros of the list"""
        if not any(map(bool, lst)):
            raise TypeError('Zero polynomial')
        else:
            while not lst[-1]:
                del lst[-1]

        return lst

    def order(self) -> int:
        """Return the order of a polynomial."""
        return len(self.coefs) - 1

    def __add__(self, other: 'Poly') -> 'Poly':
        """Return the sum of two polynomials."""
        zipped_list = list(zip_longest(self.coefs, other.coefs, fillvalue=0))
        new_coefs = list(map(sum, zipped_list))
        return Poly(new_coefs)

    def derivative(self) -> 'Poly':
        """Return the derivative of a polynomial."""
        coefs = list(self.coefs)
        if len(coefs) == 1:
            return Poly([0])
        else:
            for i in range(len(coefs)):
                coefs[i] *= i
            return Poly(coefs[1:])

    def antiderivative(self, const: float) -> 'Poly':
        """Return the antiderivative of a polynomial with the given integration constant."""
        coefs = list(self.coefs)
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

        # We add one whitespace at the beginning and end and remove them afterwards,
        # it fix the issue when we have for instance '1x^1'

        exp_with_pluses = ' ' + ' + '.join(coefs_with_x) + ' '  # ' -1x^0 + 1x^1 + 9.3x^3 '

        exp_zero_exponent = exp_with_pluses.replace('x^0', '')  # ' -1 + 1x^1 + 9.3x^3 '
        exp_one_exponent = exp_zero_exponent.replace('x^1 ', 'x ')  # ' -1 + 1x + 9.3x^3 '
        exp_better_minuses = exp_one_exponent.replace('+ -', '- ')  # ' -1 + 1x + 9.3x^3 '
        exp_one_coefs = exp_better_minuses.replace(' 1x', ' x').replace(' -1x', ' -x')  # ' -1 + x + 9.3x^3 '

        return exp_one_coefs[1:-1]

    def __eq__(self, o: 'Poly') -> bool:
        """Two polynomials are equal if their coefficients are equal."""
        return self.coefs == o.coefs
