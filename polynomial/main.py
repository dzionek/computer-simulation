from polynomial.poly import Poly

def main() -> None:
    """
    Main function doing all that was needed for the checkpoint:
    print given polynomials, find an order of a polynomial,
    sum of two polynomials, the derivative and the antiderivative of the derivative.
    """
    poly_a = Poly([2, 0, 4, -1, 0, 6])
    poly_b = Poly([-1, -3, 0, 4.5])

    print(f"""Polynomials are:
P_a(x) = {poly_a},
P_b(x) = {poly_b}.

The order of P_a(x) is {poly_a.order()}.
The sum of two polynomials is {poly_a + poly_b}.
The first derivative of P_a(x) is {poly_a.derivative()}.
The antiderivative of d(P_a(x))/dx is {poly_a.derivative().antiderivative(2)}
"""
          )


if __name__ == "__main__":
    main()