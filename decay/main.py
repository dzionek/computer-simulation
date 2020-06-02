from decay import Decay

"""
Module runs the simulation.
"""

# Decay constant of the nucleide in the assignment
ACTUAL_CONSTANT = 24.98

def main() -> None:
    """Main function printing basic and extra decay scripts"""
    print_basic()

def print_basic() -> None:
    """Main function doing what was needed for the assignment:
    1) Ask for input decay_const, size and timestep (suggested values for the given
        actual constant are decay_const = 0.02775, size = 50, timestep = 0.1
    2) Find the half-time, and print the matrix with data about decayed nuclei.
    3) Compare the simulated half-time with the actual half-time.
    """
    print("""This is Monte Carlo simulation of a radioactive decay.
    
Provide the necessary constants. For example, for Iodine-128 they are:
* decay const := 0.02775 min^-1
* size := 50
* timestep := 0.01 min
""")

    decay_const = float(input("Provide the decay constant [min^-1]: "))
    size = int(input("Provide the size of the NxN array: "))
    timestep = float(input("Provide the timestep of the decay [min]: "))

    nucleide = Decay(decay_const, size, timestep)
    initial_undecayed = nucleide.undecayed_nuclei
    half_time = round(nucleide.find_half_time(), 2)
    final_undecayed = nucleide.undecayed_nuclei

    print(f"""{'-' * 20}
{'Basic report'.center(20, '-')}
{'-' * 20}
The visualization of the nucleide after the decay:
Legend: 0 - decayed; 1 - undecayed
{nucleide}
The model started with {initial_undecayed} nuclei. After the decay {final_undecayed} of them remained.
The simulation found that the half-time of this nucleide is approximately {half_time}min.
The actual half-time of Iodine-128 is {ACTUAL_CONSTANT}min.
""")


if __name__ == '__main__':
    main()