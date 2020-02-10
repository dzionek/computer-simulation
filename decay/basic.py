import random
import numpy as np

"""
This module was an assignment for Computer Simulation 2020.
"""

class Decay:
    """
    Class simulating a radioactive decay of nuclei.
    Instance attributes:
        decay_const: float - constant of nuclear decay, determines probability of decay
        matrix: np.array([[int]]) - matrix representation of nuclei
        timestep: float - interval of time between next iterations of decaying loop
        decayed_nuclei: int - number of decayed nuclei
        undecayed_nuclei: int - number of nuclei which haven't decayed yet
    """
    def __init__(self, decay_const: float, size: int, timestep: float) -> None:
        self.decay_const = decay_const
        self.matrix = np.ones((size, size), dtype=int)
        self.timestep = timestep
        self.decayed_nuclei = 0
        self.undecayed_nuclei = size * size

    def should_decay(self) -> bool:
        """Return True if a nucleus should decay, otherwise return False."""
        probability = self.decay_const * self.timestep
        random_number = random.random()  # random float in range [0,1)
        if random_number <= probability:  # if the random number is withing the "probability range"
            return True
        else:
            return False

    def decay_iteration(self) -> None:
        """Perform one iteration of the decay"""
        for row in range(len(self.matrix)):
            for column in range(len(self.matrix)):
                # if it is undecayed
                if self.matrix[row][column] == 1:
                    if self.should_decay():
                        self.matrix[row][column] = 0
                        self.decayed_nuclei += 1
                        self.undecayed_nuclei -= 1

    def find_half_time(self) -> float:
        """Perform decay iterations until half-time is found, then return half-time."""
        timestep = self.timestep
        half_time = 0

        while self.decayed_nuclei < self.undecayed_nuclei:
            self.decay_iteration()
            half_time += timestep
        return half_time

    def __str__(self) -> str:
        """Return string representation of an instance's matrix; show its nuclei."""
        str_nucleide = ""
        for matrix_row in range(len(self.matrix)):
            str_row = ""
            for matrix_column in range(len(self.matrix)):
                str_row += str(self.matrix[matrix_row][matrix_column])
            str_nucleide += str_row + "\n"
        return str_nucleide


def main() -> None:
    """Main function doing what was needed for the assignment:
    1) Ask for input decay_const, size and timestep (suggested values for the given
        actual constant are decay_const = 0.02775, size = 50, timestep = 0.1
    2) Find the half-time, and print the matrix with data about decayed nuclei.
    3) Compare the simulated half-time with the actual half-time.
    """
    ACTUAL_CONSTANT = 24.98
    decay_const = float(input("Provide the decay constant [min^-1]: "))
    size = int(input("Provide the size of the NxN array: "))
    timestep = float(input("Provide the timestep of the decay [min]: "))

    nucleide = Decay(decay_const, size, timestep)
    initial_undecayed = nucleide.undecayed_nuclei
    half_time = round(nucleide.find_half_time(), 2)
    final_undecayed = nucleide.undecayed_nuclei

    print("\n----------------------------------")
    print("The final report of the simulation")
    print("----------------------------------\n")
    print("The visualization of the nucleide after the decay:")
    print("\nLegend: 0 - decayed; 1 - undecayed\n")
    print(nucleide)
    print(f"The model started with {initial_undecayed} nuclei. After the decay {final_undecayed} of them remained.")
    print(f"The simulation found that the half-time of this nucleide is approximately {half_time}min.")
    print(f"The actual half-time is {ACTUAL_CONSTANT}min.")


if __name__ == "__main__":
    main()
