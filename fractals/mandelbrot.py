from fractal import Fractal

"""
This module shows my Mandelbrot Set coursework
for Computer Simulation 2020.
"""

class Mandelbrot(Fractal):
    """
    Fractal child class of the Mandelbrot set.
    See Also:
        fractal.py for attributes
    """

    def last_convergent(self, point: complex) -> int:
        """
        Return the last element of a sequence before it has turned out to be diverging.
        If the given iteration_limit has been exceeded, it returns this limit.
        """
        z = 0
        for iterator in range(self.iteration_limit):
            z = z * z + point
            if abs(z) > 2:
                return iterator
        return self.iteration_limit
