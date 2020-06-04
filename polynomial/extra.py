from functools import reduce
from itertools import zip_longest
from typing import List
import matplotlib.pyplot as plt
import numpy as np

from poly import Poly, Coefficients

"""
This module shows my extra work with Polynomial exercise.
"""

class PolyExtra(Poly):
    """Class adds extra features to the basic polynomial class."""
    def __init__(self, coefs: Coefficients) -> None:
        """Initialize polynomial with extra methods."""
        super().__init__(coefs)

    def __sub__(self, other: Poly) -> Poly:
        """Return the difference of two polynomials."""
        other_negative_coefs = list(map(lambda x: -x, other.coefs))
        zipped_list = list(zip_longest(self.coefs, other_negative_coefs, fillvalue=0.0))
        new_coefs: Coefficients = list(map(sum, zipped_list))
        return Poly(new_coefs)

    def __mul__(self, other: Poly) -> Poly:
        """Multiply two polynomials."""
        res: Coefficients = [0] * (self.order() * other.order())

        for i, self_coef in enumerate(self.coefs):
            for j, other_coef in enumerate(other.coefs):
                res[i + j] += self_coef * other_coef

        return PolyExtra(res)

    def coefs_sum(self) -> float:
        """Return the sum of polynomial's coefficients"""
        return sum(self.coefs)

    def coefs_product(self) -> float:
        """Return the product of polynomial's coefficients"""
        return reduce(lambda x, y: x * y, self.coefs)

    def __call__(self, val: float) -> float:
        """Evaluate polynomial using a given value of x."""
        if not (isinstance(val, float) or isinstance(val, int)):
            raise TypeError('The given value is not a real number.')

        res = 0.0
        for i in range(len(self.coefs)):
            res += self.coefs[i] * val ** i  # in python 0 ** 0 := 1
        return res

    def visualize(self) -> None:
        """Prints the graph of a polynomial"""
        xs = np.linspace(start=-20, stop=20, num=1000)
        ys = np.array([self(x) for x in xs])
        plt.plot(xs, ys)
        plt.title(str(self))
        plt.show()