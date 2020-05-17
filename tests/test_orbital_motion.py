import unittest

from sim_constants import *
from body import Body
from simulated_system import SimulatedSystem

def e_round(num: float, n: int) -> float:
    """
    Rounds to n places after dot in exponential notation.

    >>> e_round(1.45425245245e213, 3)
    1.454e+213
    """

    formatter = '{' + f':0.{n}e' + '}'
    return float(formatter.format(num))


class BodyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.mars = Body(M_MASS, M_COLOR, M_INIT_POS, M_INIT_VEL, M_INIT_ACC, M_INIT_FORCE)
        self.phobos = Body(P_MASS, P_COLOR, P_INIT_POS, P_INIT_VEL, P_INIT_ACC, P_INIT_FORCE)
        self.deimos = Body(D_MASS, D_COLOR, D_INIT_POS, D_INIT_VEL, D_INIT_ACC, D_INIT_FORCE)

    def test_kinetic_energy(self) -> None:
        self.assertEqual(self.mars.kinetic_energy, 0)
        self.assertEqual(e_round(self.phobos.kinetic_energy, 2), 2.42e22)
        self.assertEqual(e_round(self.deimos.kinetic_energy, 2), 1.64e21)


class SimulatedSystemTestCase(unittest.TestCase):
    def setUp(self) -> None:
        mars = Body(M_MASS, M_COLOR, M_INIT_POS, M_INIT_VEL, M_INIT_ACC, M_INIT_FORCE)
        phobos = Body(P_MASS, P_COLOR, P_INIT_POS, P_INIT_VEL, P_INIT_ACC, P_INIT_FORCE)
        deimos = Body(D_MASS, D_COLOR, D_INIT_POS, D_INIT_VEL, D_INIT_ACC, D_INIT_FORCE)
        self.system = SimulatedSystem(mars, phobos, deimos)

    def test_preserved_energy(self) -> None:
        init_energy = self.system.total_kinetic_energy
        upper_bound = 1.03 * init_energy
        lower_bound = 0.97 * init_energy
        for _ in range(1000):
            self.system.next_iteration()
            self.assertLessEqual(self.system.total_kinetic_energy, upper_bound)
            self.assertGreaterEqual(self.system.total_kinetic_energy, lower_bound)


if __name__ == '__main__':
    unittest.main()
