from matplotlib import use
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt

from typing import List
import numpy as np
from copy import copy
from math import log

from body import Body
from system import System
from sim_constants import TIME_STEP, GRAVITY

"""
Module with self-contained class of a celestial system which will be simulated.
"""

class SimulatedSystem(System):
    """
    Simulate a celestial system. Container for Body class. Inherit from System.
    In the simulation next attributes of each body are counted using numerical integration
    with the Euler-Cromer algorithm:
        v(t + dt) = v(t) + a(t)  dt
        r(t + dt) = r(t) + v(t + dt) dt

    Attributes
    ----------
    bodies : ndarray[Body]
        Bodies that belong to the system.
    """
    def __init__(self, *bodies: Body):
        """Initialize the animated system."""
        super().__init__(*bodies)

    def _euler_cromer(self, body: Body) -> None:
        """Find new attributes after TIME_STEP using the Euler-Cromer algorithm."""
        body.force = np.array([0.0, 0.0])
        for other in self.bodies:
            if body != other:
                relative_position = other.position - body.position
                body.force += (body.mass * other.mass * relative_position
                               / np.linalg.norm(relative_position)**3)
        body.force *= GRAVITY
        body.acceleration = body.force / body.mass
        body.velocity += body.acceleration * TIME_STEP
        body.position += body.velocity * TIME_STEP

    def next_iteration(self) -> None:
        """Set new parameter to each body after numerical integration."""
        new_bodies: List[Body] = []
        for new_body in map(copy, self.bodies):
            self._euler_cromer(new_body)
            new_bodies.append(new_body)
        self.bodies = np.array(new_bodies)

    @staticmethod
    def _find_radius(body: Body):
        """Find a convenient radius that suits best for the animation."""
        return log(body.mass, 1.00007) + body.mass ** 0.25

    def _update_plot(self, _, circles: List[plt.Circle]) -> List[plt.Circle]:
        """Update the plot after each iteration."""
        self.next_iteration()

        for circle, body in zip(circles, self.bodies):
            circle.center = body.position

        return circles

    def show_simulation(self) -> None:
        """Show the simulation of the system."""
        use('TkAgg')
        fig = plt.figure()
        ax = plt.axes()

        circles = [
            plt.Circle(xy=body.position, radius=self._find_radius(body), color=body.color, animated=True)
            for body in self.bodies
        ]

        for circle in circles:
            ax.add_patch(circle)

        ax.axis('scaled')
        ax.set_xlim(-2e7, 2e7)
        ax.set_ylim(-1.2e7, 1.2e7)
        ax.set_facecolor('#071a38')
        plt.title('Simulation of the given system.')

        ani = FuncAnimation(fig, self._update_plot, interval=10, blit=True, fargs=(circles,))
        plt.show()