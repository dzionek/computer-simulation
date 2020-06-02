from traffic import Traffic

"""
This module runs Traffic simulation.
"""

def main() -> None:
    """
    Main method prompting for iterations and road length for plotting the steady state
    average speed graph, and also prompting for car density to show animation of the
    particular traffic model.
    """
    road_length = float(input('Provide the length of the road: '))
    car_density = float(input('Provide the density of the cars: '))
    iterations = float(input('Provide the number of iterations: '))

    Traffic.density_graph(road_length, iterations)

    model = Traffic(road_length, car_density, iterations)
    model.visualize_traffic()


if __name__ == '__main__':
    main()