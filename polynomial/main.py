from poly import Poly
from extra import PolyExtra


def main() -> None:
    """Main function printing basic and extra features."""
    print_basic()
    print_extra()


def print_basic() -> None:
    """
    Function doing all that was needed for the checkpoint:
    print given polynomials, find an order of a polynomial,
    sum of two polynomials, the derivative and the antiderivative of the derivative.
    """
    poly_a = Poly([2, 0, 4, -1, 0, 6])
    poly_b = Poly([-1, -3, 0, 4.5])

    print('BASIC'.center(20, '-'))

    print(f"""Polynomials are:
P_a(x) = {poly_a},
P_b(x) = {poly_b}.

The order of P_a(x) is {poly_a.order()}.
The sum of two polynomials is {poly_a + poly_b}.
The first derivative of P_a(x) is {poly_a.derivative()}.
The antiderivative of d(P_a(x))/dx is {poly_a.derivative().antiderivative(2)}.
""")


def print_extra() -> None:
    """Function printing extra features I have implemented."""
    input('Press a key to see extra features')

    poly_a = PolyExtra([2, 0, 4, -1, 0, 6])
    poly_b = PolyExtra([-1, -3, 0, 4.5])

    print('EXTRA'.center(20, '-'))

    print(f"""The difference P_a(x) - P_b(x) is {poly_a - poly_b}.
The product P_a(x) * P_b(x) is {poly_a * poly_b}.
The sum of coefficients of P_a(x) is {poly_a.coefs_sum()}.
The product of coefficients of P_a(x) is {poly_a.coefs_product()}.
The value of P_a(10) is {poly_a(10)}
Matplotlib has plotted the graph of P_a(x) on domain [-20, 20].
""")


if __name__ == "__main__":
    main()