from fractals.basic.fractal import Fractal

"""
This module was an assignment for Computer Simulation 2020.
"""

class Mandelbrot(Fractal):
    """Child class with the method checking whether a point belongs to the Mandelbrot set."""
    def last_convergent(self, point: complex) -> int:
        """
        Return the last element of a sequence before it turned out to be diverging.
        If the given iteration_limit was exceeded, it returns this limit.
        """
        z = 0
        for iterator in range(self.iteration_limit):
            z = z*z + point
            if abs(z) > 2:
                return iterator
        return self.iteration_limit


def main() -> None:
    """Plot the Mandelbrot set."""
    mandelbrot = Mandelbrot(iteration_limit=255, accuracy=500,
                            real_domain=[-2.025, 0.6], imaginary_domain=[-1.125, 1.125])
    mandelbrot.plot()


if __name__ == "__main__":
    main()