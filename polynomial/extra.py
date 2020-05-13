from functools import reduce
from itertools import zip_longest
from typing import List

from polynomial.poly import Poly

"""
This module shows my extra work with Polynomial exercise.
"""

class PolyExtra(Poly):
    """Class adds extra features to the basic polynomial class."""
    def __init__(self, coefs: List[float]) -> None:
        """Initialize polynomial with extra methods."""
        super().__init__(coefs)

    def __sub__(self, other: Poly) -> Poly:
        """Return the difference of two polynomials."""
        other_negative_coefs = list(map(lambda x: -x, other.coefs))
        zipped_list = list(zip_longest(self.coefs, other_negative_coefs, fillvalue=0))
        new_coefs = list(map(sum, zipped_list))
        return Poly(new_coefs)

    def coefs_sum(self) -> float:
        """Return the sum of polynomial's coefficients"""
        return sum(self.coefs)

    def coefs_product(self) -> float:
        """Return the product of polynomial's coefficients"""
        return reduce(lambda x, y: x * y, self.coefs)