import random
import numpy as np

"""
This module contains my decay coursework
for Computer Simulation 2020.
"""

class Decay:
    """
    Class simulating a Monte Carlo simulation of a radioactive decay of nuclei.
    Instance attributes:
        decay_const: float - constant of nuclear decay, determines probability of decay
        matrix: np.array([[int]]) - matrix representation of nuclei
        timestep: float - interval of time between next iterations of decaying loop
        decayed_nuclei: int - number of decayed nuclei
        undecayed_nuclei: int - number of nuclei which haven't decayed yet
    """
    def __init__(self, decay_const: float, size: int, timestep: float) -> None:
        """Initialize a Decay instance."""
        self.decay_const = decay_const
        self.matrix = np.ones((size, size), dtype=int)
        self.timestep = timestep
        self.decayed_nuclei = 0
        self.undecayed_nuclei = size * size

    def _should_decay(self) -> bool:
        """Return True if a nucleus should decay, otherwise return False."""
        probability = self.decay_const * self.timestep
        random_number = random.random()  # random float in range [0,1)
        if random_number <= probability:  # if the random number is withing the "probability range"
            return True
        else:
            return False

    def _decay_iteration(self) -> None:
        """Perform one iteration of the decay"""
        for row in range(len(self.matrix)):
            for column in range(len(self.matrix)):
                # if it is undecayed
                if self.matrix[row, column] == 1:
                    if self._should_decay():
                        self.matrix[row, column] = 0
                        self.decayed_nuclei += 1
                        self.undecayed_nuclei -= 1

    def find_half_time(self) -> float:
        """Perform decay iterations until half-time is found, then return half-time."""
        timestep = self.timestep
        half_time = 0.0

        while self.decayed_nuclei < self.undecayed_nuclei:
            self._decay_iteration()
            half_time += timestep
        return half_time

    def __str__(self) -> str:
        """Return string representation of an instance's matrix; show its nuclei."""
        str_nucleide = ""
        for matrix_row in range(len(self.matrix)):
            str_row = ""
            for matrix_column in range(len(self.matrix)):
                str_row += str(self.matrix[matrix_row, matrix_column])
            str_nucleide += str_row + "\n"
        return str_nucleide
