from fractals.basic.fractal import Fractal

"""
This module shows my extra work with fractals.
"""

class Julia(Fractal):
    """Child class with the method checking whether a point belong to a Julia set."""
    def __init__(self, constant: complex, iteration_limit: int, accuracy: int,
                 real_domain: [float], imaginary_domain: [float]) -> None:

        self.constant = constant
        super().__init__(iteration_limit, accuracy, real_domain, imaginary_domain)

    def last_convergent(self, point: complex) -> int:
        """
        Return the last element of a sequence before it turned out to be diverging.
        If the given iteration_limit was exceeded, it returns this limit.
        """
        z = point
        for iterator in range(self.iteration_limit):
            z = z*z + self.constant
            if abs(z) > 2:
                return iterator
        return self.iteration_limit


def main() -> None:
    """Plot the Julia set."""
    julia = Julia(constant=complex(-0.1, 0.8), iteration_limit=24, accuracy=500,
                  real_domain=[-2, 2], imaginary_domain=[-2, 2])
    julia.plot()


if __name__ == "__main__":
    main()