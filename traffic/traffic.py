from matplotlib import use
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import numpy as np
from random import randint
from typing import Union

"""
This module shows my Traffic Simulation coursework
for Computer Simulation 2020.
"""

Num = Union[int, float]

class Traffic:
    """
    Class containing all functions connected to traffic simulation.
    It creates a model of one line road, and searches for steady state average speed.
    Attributes:
        road_length: int - length of the road.
        param car_density: float - ratio of the number of cars to road_length.
        param iterations: int - how many iterations are to be performed.
    """
    def __init__(self, road_length: Num, car_density: Num, iterations: Num) -> None:
        """Initialize traffic model."""

        self.road = np.zeros(Traffic._validate_int(road_length), dtype=int)
        self.car_density = Traffic._validate_density(car_density)
        self.iterations = Traffic._validate_int(iterations)
        self.cars_number = int(car_density * road_length)
        self._allocate_cars()

    @staticmethod
    def _validate_density(density: Num) -> Num:
        """Validate if density is a real number between 0 and 1. If not, raise an error."""

        if not (isinstance(density, float) or isinstance(density, int)):
            raise TypeError("Density must be a real number.")
        elif density > 1 or density < 0:
            raise ValueError("Density should be between 0 and 1.")
        else:
            return density

    @staticmethod
    def _validate_int(arg: Num) -> Num:
        """
        Check if the given parameter is of type int. If it is float, it is converted to int.
        If it is int it returns the argument. If not, raises an error.
        """
        if isinstance(arg, float):
            if arg.is_integer():
                arg = int(arg)

        if not isinstance(arg, int):
            raise TypeError("The parameter should be an integer.")
        return arg

    def _allocate_cars(self) -> None:
        """On an empty road, allocate cars to places on the road according to cars_number."""

        for _ in range(self.cars_number):
            occupied = True

            while occupied:
                random_road_place = randint(0, len(self.road) - 1)

                if self.road[random_road_place] == 0:
                    occupied = False
                    self.road[random_road_place] = 1

    def _one_iteration(self) -> float:
        """Perform one iteration of a traffic move, return average speed in the iteration."""

        moving_cars = 0

        # temp is a copy of array, because of its reference type
        temp_road = np.array(self.road)

        road_length = len(self.road)

        for road_place in range(road_length):
            # After last element of the array, we have the first element.
            if road_place == road_length - 1:
                if self.road[road_place] == 1 and self.road[0] == 0:
                    temp_road[road_place] = 0
                    temp_road[0] = 1
                    moving_cars += 1
            # For places on the road different than the last.
            else:
                if self.road[road_place] == 1 and self.road[road_place + 1] == 0:
                    temp_road[road_place] = 0
                    temp_road[road_place + 1] = 1
                    moving_cars += 1

        self.road = temp_road

        # Check whether number of cars is 0.
        try:
            average_velocity = moving_cars / self.cars_number
        except ZeroDivisionError:
            # this value fits best to the data.
            average_velocity = 1

        return average_velocity

    def find_equilibrium(self) -> float:
        """Find the steady state average speed."""
        speed = None
        for _ in range(len(self.road)):
            speed = self._one_iteration()

        return speed

    @staticmethod
    def density_graph(road_length: Num, iterations: Num) -> None:
        """Plot a graph of steady state average speed against car density."""

        road_length = Traffic._validate_int(road_length)
        iterations = Traffic._validate_int(iterations)

        densities = np.linspace(0, 1, 100)
        steady_average_speeds = [
            Traffic(road_length, density, iterations).find_equilibrium()
            for density in densities
        ]

        plt.plot(densities, steady_average_speeds)
        plt.xlabel("Congestion of the road")
        plt.ylabel("Steady state average speed")
        plt.title("Optimal speed for a different congestion of the road.")
        plt.show()

    def visualize_traffic(self) -> None:
        """Show animation of a traffic for the given model."""
        use("TkAgg")

        fig = plt.figure(2)

        # The animation will have dimension 10xroad_length
        traffic_array = np.array([self.road, ] * 10)
        im = plt.imshow(traffic_array, animated=True, cmap='Blues', interpolation='none')

        def update_fig(*args):
            self._one_iteration()
            traffic_array = np.array([self.road, ] * 10)
            im.set_array(traffic_array)
            return im,

        ani = FuncAnimation(fig, update_fig, self.iterations, repeat=False, interval=500, blit=True)
        plt.xlabel('The road')
        plt.title('Traffic animation (cars are blue)')
        plt.show()
