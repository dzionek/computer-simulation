import numpy as np
from sim_constants import Vector

"""
Module with self-contained class of a celestial body.
"""

class Body:
    """
    Class representing a celestial body. Stores its position in the space.

    Attributes
    ----------
    mass : float
        The mass of the body.
    color : str
        The color of the body that will be shown when it is displayed.
    position Vector
        The position vector of the body.
    velocity : Vector
        The speed vector of the body.
    acceleration : Vector
        The acceleration vector of the body.
    force : Vector
        The force vector of the body.
    """

    def __init__(self, mass: float, color: str, position: Vector, velocity: Vector,
                 acceleration: Vector, force: Vector) -> None:
        """Initialize celestial body within positioning system."""
        self.mass = mass
        self.color = color
        self.position = np.array(position)
        self.velocity = np.array(velocity)

        self.acceleration = np.array(acceleration)
        self.force = np.array(force)

    @property
    def kinetic_energy(self) -> float:
        """Kinetic energy of the body."""
        velocity: float = np.linalg.norm(self.velocity)
        return 0.5 * self.mass * velocity**2

    def __repr__(self) -> str:
        """Visual representation of a body instance."""
        return f'Body with mass {self.mass}, position {self.position}, and velocity {self.velocity}'

    def __eq__(self, other: object) -> bool:
        """
        Two bodies are equal when they have the same mass.
        This condition is sufficient in our simulation.
        """
        return self.mass == other.mass if isinstance(other, Body) else False

    def __ne__(self, other: object) -> bool:
        """Opposite of __eq__."""
        return self.mass != other.mass if isinstance(other, Body) else False
