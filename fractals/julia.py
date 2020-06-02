from typing import Tuple

from fractal import Fractal

"""
This module shows my extra work with fractals.
"""

class Julia(Fractal):
    """Fractal child class of a Julia set.
    Attributes:
        constant: complex - point of the complex plain unique for each Julia set.
    See Also:
        fractal.py for other attributes
    """
    def __init__(self, constant: complex, iteration_limit: int, accuracy: int,
                 real_domain: Tuple[float, float], imaginary_domain: Tuple[float, float]) -> None:
        """Initializes a Julia set"""

        self.constant = constant
        super().__init__(iteration_limit, accuracy, real_domain, imaginary_domain)

    def last_convergent(self, point: complex) -> int:
        """
        Return the last element of a sequence before it has turned out to be diverging.
        If the given iteration_limit has been exceeded, it returns this limit.
        """
        z = point
        for iterator in range(self.iteration_limit):
            z = z * z + self.constant
            if abs(z) > 2:
                return iterator
        return self.iteration_limit
