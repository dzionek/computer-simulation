import unittest
from collections import Counter

from decay import Decay

class DecayTestCase(unittest.TestCase):

    MINUTES_IN_YEAR = 365 * 24 * 60

    def setUp(self) -> None:
        self.lithium = Decay(decay_const=49.5, size=50, timestep=0.01)  # lithium-8
        self.radon = Decay(decay_const=0.798, size=50, timestep=0.01)  # radon-220
        self.plutonium = Decay(decay_const=5.5e-11, size=50, timestep=1e7)  # plutonium-239
        self.small = Decay(decay_const=1, size=5, timestep=0.01)

    def test_half_time(self) -> None:
        self.assertLessEqual(self.lithium.find_half_time(), 0.02)  # actual 0.014 min

        radon_half_time = self.radon.find_half_time()

        self.assertGreaterEqual(radon_half_time, 0.8)  # actual 0.867 min
        self.assertLessEqual(radon_half_time, 0.95)

        plutonium_half_time = self.plutonium.find_half_time()

        self.assertGreaterEqual(plutonium_half_time, 2e4 * DecayTestCase.MINUTES_IN_YEAR)  # 2.4 * 10^4 years
        self.assertLessEqual(plutonium_half_time, 3e4 * DecayTestCase.MINUTES_IN_YEAR)

    def test_str(self) -> None:
        self.assertEqual(str(self.small), '11111\n11111\n11111\n11111\n11111\n')
        self.small.find_half_time()
        counter = Counter(self.small.matrix.flatten())
        self.assertLessEqual(counter[1], counter[0])  # less undecayed than decayed


if __name__ == '__main__':
    unittest.main()
