from numpy import array, ndarray
from body import Body

"""
Module with self-contained class of a celestial system.
"""

class System:
    """
    Class representing celestial systems. Container of the Body class.
    Attributes
    ----------
    bodies : ndarray[Body]
        Bodies that belong to the system.
    """
    def __init__(self, *bodies: Body) -> None:
        """Initialize the system."""
        self.bodies = array(bodies)

    @property
    def total_kinetic_energy(self) -> float:
        """Total kinetic energy of the system."""
        return sum(body.kinetic_energy for body in self.bodies)