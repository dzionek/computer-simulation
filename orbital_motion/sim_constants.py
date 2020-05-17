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

# Parameters for Deimos
D_MASS: Final[float] = 1.8e15
D_COLOR: Final[str] = 'w'
D_RADIUS: Final[float] = 23.463e6
D_INIT_POS: Final[Vector] = (D_RADIUS, 0.0)
D_INIT_VEL: Final[Vector] = (0.0, _find_moon_total_velocity(M_MASS, D_RADIUS))
D_INIT_ACC: Final[Vector] = (0.0, 0.0)
D_INIT_FORCE: Final[Vector] = (0.0, 0.0)

# ----- PLOT -----
X_LIMITS: Final[Vector] = (-5e7, 5e7)  # range of x values on the plot.
Y_LIMITS: Final[Vector] = (-3e7, 3e7)  # range of y values on the plot.
BACKGROUND_COLOR: Final[str] = '#071a38'
PLOT_TITLE: Final[str] = 'Simulation of Mars with its moons - Phobos and Deimos.'

# ----- OTHER -----
TIME_STEP: Final[float] = 100.0
