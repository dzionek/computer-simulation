import unittest

from polynomial.extra import PolyExtra


class PolynomialTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.poly_a = PolyExtra([1, 0, 2, -3, 4, 0])
        self.poly_b = PolyExtra([-1, -3, 0, 4, 5/6, 6, 34, -99.5])
        self.poly_c = PolyExtra([-5, -32, 0, 0, 0, 3, 2, 1, 3, -2.123, 3, 5, 6, 9])

    def test_constructor(self) -> None:
        self.assertRaises(TypeError, lambda _: PolyExtra(['foo', 'bar', 1, 2, 3]))
        self.assertRaises(TypeError, lambda _: PolyExtra([3, 4, 5, complex(1, 2)]))
        self.assertRaises(TypeError, lambda _: PolyExtra([]))
        try:
            _ = PolyExtra([2, 0, 0, -1, 9999999, 0.00000, -3/7])
        except TypeError:
            raise AssertionError

        from polynomial.poly import Poly
        self.assertEqual(Poly([1, 0, -1, 0]), PolyExtra([1, 0, -1, 0]))

    def test_trailing_zeros(self) -> None:
        self.assertRaises(TypeError, lambda _: PolyExtra([0, 0, 0, 0, 0, 0]))
        self.assertEqual(PolyExtra([0, 0, 0, 0, 0, 0, 0, 1]), PolyExtra([0, 0, 0, 0, 0, 0, 0, 1]))
        self.assertEqual(PolyExtra([0, 1, -1, 0, 0, 0, 0, 0]), PolyExtra([0, 1, -1]))

    def test_order(self) -> None:
        self.assertEqual(self.poly_a.order(), 4)
        self.assertEqual(self.poly_b.order(), 7)
        self.assertEqual(self.poly_c.order(), 13)

    def test_add(self) -> None:
        self.assertEqual(self.poly_a + self.poly_b,
                         PolyExtra([0, -3, 2, 1, 4 + 5/6, 6, 34, -99.5]))
        self.assertEqual(self.poly_b + self.poly_c,
                         PolyExtra([-6, -35, 0, 4, 5/6, 9, 36, -98.5, 3, -2.123, 3, 5, 6, 9]))

    def test_subtract(self) -> None:
        self.assertEqual(self.poly_a - self.poly_c,
                         self.poly_a + PolyExtra([-coef for coef in self.poly_c.coefs]))
        self.assertEqual(self.poly_a - self.poly_b,
                         PolyExtra([2, 3, 2, -7, 3 + 1/6, -6, -34, 99.5]))

    def test_derivative(self) -> None:
        self.assertEqual(self.poly_a.derivative(), PolyExtra([0, 4, -9, 16]))
        self.assertEqual(self.poly_a.derivative().derivative().derivative(), PolyExtra([-18, 96]))
        self.assertEqual(self.poly_c.derivative(),
                         PolyExtra([-32, 0, 0, 0, 15, 12, 7, 24, -2.123 * 9, 30, 55, 72, 117]))

    def test_antiderivative(self) -> None:
        self.assertEqual(self.poly_a.derivative().antiderivative(1), self.poly_a)
        self.assertEqual(self.poly_b.derivative().antiderivative(-1), self.poly_b)
        self.assertEqual(self.poly_c.derivative().antiderivative(-5), self.poly_c)
        self.assertEqual(self.poly_b.antiderivative(10), PolyExtra([10, -1, -1.5, 0, 1, 5/6/5, 1, 34 / 7, -99.5/8]))

    def test_rep(self) -> None:
        self.assertEqual(str(self.poly_a), '1 + 2x^2 - 3x^3 + 4x^4')
        self.assertEqual(str(self.poly_b), f'-1 - 3x + 4x^3 + {5/6}x^4 + 6x^5 + 34x^6 - 99.5x^7')
        self.assertEqual(str(self.poly_c),
                         '-5 - 32x + 3x^5 + 2x^6 + x^7 + 3x^8 - 2.123x^9 + 3x^10 + 5x^11 + 6x^12 + 9x^13')
        self.assertEqual(str(PolyExtra([0, -1])), '-x')
        self.assertEqual(str(PolyExtra([0, 0, 1])), 'x^2')
        self.assertEqual(str(PolyExtra([0, -1, 2, 3, 5.5, -7])), '-x + 2x^2 + 3x^3 + 5.5x^4 - 7x^5')

    def test_coefs_sum(self) -> None:
        self.assertEqual(self.poly_a.coefs_sum(), 4)
        self.assertEqual(self.poly_b.coefs_sum(), -59.5 + 5/6)
        self.assertAlmostEqual(self.poly_c.coefs_sum(), -7.123)

    def test_coefs_product(self) -> None:
        self.assertEqual(self.poly_a.coefs_product(), 0)
        self.assertEqual(self.poly_b.coefs_product(), 0)
        self.assertEqual(self.poly_c.coefs_product(), 0)
        self.assertEqual(PolyExtra([-1, 1, -1, 1]).coefs_product(), 1)

        from math import factorial
        self.assertEqual(PolyExtra([x for x in range(1, 101)]).coefs_product(), factorial(100))

    def test_mul(self) -> None:
        self.assertEqual(PolyExtra([1, 2, 3]) * PolyExtra([4, 5, 6, 0, 7]),
                         PolyExtra([4, 13, 28, 27, 25, 14, 21]))
        self.assertEqual(self.poly_a * self.poly_a,
                         PolyExtra([1, 0, 4, -6, 12, -12, 25, -24, 16]))

    def test_call(self) -> None:
        self.assertEqual(self.poly_c(0), -5)
        self.assertEqual(self.poly_a(-1), 10)

        self.assertRaises(TypeError, lambda _: self.poly_b('foo'))


if __name__ == '__main__':
    unittest.main()
