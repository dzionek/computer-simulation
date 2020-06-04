from math import sqrt
from numpy import ndarray
from typing import List, Tuple, Final, Union

"""
Module with all constants for the simulation.
"""

# ----- FUNCTIONS -----
GRAVITY: Final = 6.6743e-11

def _find_moon_total_velocity(mass: float, radius: float) -> float:
    """Get total velocity of a moon."""
    return sqrt(GRAVITY * mass / radius)


# ----- TYPING -----
Vector = Union[List[float], Tuple[float, ...], ndarray]

# ----- BODY DATA -----
#   POS - position, VEL - velocity, ACC - acceleration, INIT - initial

# Parameters for Mars.
M_MASS: Final = 6.4185e23
M_COLOR: Final = 'r'
M_INIT_POS: Final = (0.0, 0.0)
M_INIT_VEL: Final = (0.0, 0.0)
M_INIT_ACC: Final = (0.0, 0.0)
M_INIT_FORCE: Final = (0.0, 0.0)

# Parameters for Phobos
P_MASS: Final = 1.06e16
P_COLOR: Final = 'y'
P_RADIUS: Final = 9.3773e6
P_INIT_POS: Final = (P_RADIUS, 0.0)
P_INIT_VEL: Final = (0.0, _find_moon_total_velocity(M_MASS, P_RADIUS))
P_INIT_ACC: Final = (0.0, 0.0)
P_INIT_FORCE: Final = (0.0, 0.0)

# Parameters for Deimos
D_MASS: Final = 1.8e15
D_COLOR: Final = 'w'
D_RADIUS: Final = 23.463e6
D_INIT_POS: Final = (D_RADIUS, 0.0)
D_INIT_VEL: Final = (0.0, _find_moon_total_velocity(M_MASS, D_RADIUS))
D_INIT_ACC: Final = (0.0, 0.0)
D_INIT_FORCE: Final = (0.0, 0.0)

# ----- PLOT -----
X_LIMITS: Final = (-5e7, 5e7)  # range of x values on the plot.
Y_LIMITS: Final = (-3e7, 3e7)  # range of y values on the plot.
BACKGROUND_COLOR: Final = '#071a38'
PLOT_TITLE: Final = 'Simulation of Mars with its moons - Phobos and Deimos.'

# ----- OTHER -----
TIME_STEP: Final = 100.0
