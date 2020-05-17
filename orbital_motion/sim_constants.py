from math import sqrt
from numpy import ndarray
from typing import List, Tuple, Final, Union

"""
Module with all constants for the simulation.
"""

# ----- FUNCTIONS -----
GRAVITY: Final[float] = 6.6743e-11

def _find_moon_total_velocity(mass: float, radius: float) -> float:
    """Get total velocity of a moon."""
    return sqrt(GRAVITY * mass / radius)


# ----- TYPING -----
Vector: Final = Union[List[float], Tuple[float, ...], ndarray]

# ----- BODY DATA -----
#   POS - position, VEL - velocity, ACC - acceleration, INIT - initial

# Parameters for Mars.
M_MASS: Final[float] = 6.4185e23
M_COLOR: Final[str] = 'r'
M_INIT_POS: Final[Vector] = (0.0, 0.0)
M_INIT_VEL: Final[Vector] = (0.0, 0.0)
M_INIT_ACC: Final[Vector] = (0.0, 0.0)
M_INIT_FORCE: Final[Vector] = (0.0, 0.0)

# Parameters for Phobos
P_MASS: Final[float] = 1.06e16
P_COLOR: Final[str] = 'y'
P_RADIUS: Final[float] = 9.3773e6
P_INIT_POS: Final[Vector] = (P_RADIUS, 0.0)
P_INIT_VEL: Final[Vector] = (0.0, _find_moon_total_velocity(M_MASS, P_RADIUS))
P_INIT_ACC: Final[Vector] = (0.0, 0.0)
P_INIT_FORCE: Final[Vector] = (0.0, 0.0)

# ----- PLOT -----
X_LIMITS: Final[Vector] = (-2e7, 2e7)  # range of x values on the plot.
Y_LIMITS: Final[Vector] = (-1.2e7, 1.2e7)  # range of y values on the plot.
BACKGROUND_COLOR: Final[str] = '#071a38'
PLOT_TITLE: Final[str] = 'Simulation of the given system.'

# ----- OTHER -----
TIME_STEP: Final[float] = 100.0
