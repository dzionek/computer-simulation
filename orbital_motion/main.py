from body import Body
from simulated_system import SimulatedSystem

from sim_constants import *

"""
Main module to display the simulation.
"""

def main() -> None:
    """Initialize celestial bodies and display their simulation."""
    mars = Body(M_MASS, M_COLOR, M_INIT_POS, M_INIT_VEL, M_INIT_ACC, M_INIT_FORCE)
    phobos = Body(P_MASS, P_COLOR, P_INIT_POS, P_INIT_VEL, P_INIT_ACC, P_INIT_FORCE)

    display_simulation(mars, phobos)


def display_simulation(*bodies: Body) -> None:
    """Display the simulation of the given system."""
    system = SimulatedSystem(*bodies)
    system.show_simulation()


if __name__ == '__main__':
    main()