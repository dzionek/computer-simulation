# Computer Simulation
This repository shows my courserwork for Computer Simulation course at the Univeristy of Edinburgh.
It consits of 5 independent physics projects. For each of them I added a couple of extra feautres, type annotations and Unittest tests.

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
cd computer-simulation
pip install -r requirements.txt
```

## Run
To run one of the 5 projects go to its directory and run its *main.py*. For instance, for fractals do the following:

```bash
cd fractals
python main.py
```

# Table of projects

1. [Polynomial](#polynomial)
2. [Radioactive Decay](#radioactive-decay)
3. [Fractals](#fractals)
4. [Traffic Simulation](#traffic-simulation)
5. [Orbital Motion](#orbital-motion)

## Polynomial
Polynomial mathematics in Python.

### Uni-required features
Storing polynomial coefficients, finding its order, adding two polynomials, finding polynomial's derivative and antiderivative.

### Extra features
Type annotations, documentation, validation of all parameters, subtracting, multiplication,
finding polynomial's value at a given point, coefficients' sum and product, matplotlib visualization, and unit tests.

## Radioactive Decay

### Uni-required features
Monte Carlo simulation, finding half-time, text representation of a nucleide.

### Extra features
Type annotations, documentation, validation of all parameters, and unit tests.

## Fractals

### Uni-required features
Generating the Mandelbrot Set.

### Extra features
* Generating Julia Sets of a given complex constant.

* Generating an animation of Julia Sets of the form  
![f1],  
where alpha is an angle that changes throughout the animation.

* Better architecture with fractal abstract class.

* Type annotations, documentation.

### Instruction

To generate a different Julia Sets than the default ones, go to *main.py* and change the constants:

```python
# Edit these constants to generate different Julia sets.
STATIC_JULIA_CONSTANT = complex(-0.1, 0.8)
ANIMATED_JULIA_CONSTANT = 0.8
```

## Traffic Simulation

### Uni-required features
Animation of the traffic iterations, graph of steady state average speed against car density.

### Extra features
Type annotations, documentation, validation of all parameters.

## Orbital Motion

### Uni-required features
Finding velocity, acceleration, position vectors with the vectorized Euler-Cromer algorithm,
computing kinetic energy of a system and ensuring it is preserved throughout the simulation.

### Extra features
Type annotations, documentation, better visualization and unit tests.

### Instruction
The script was primary to visualize a planet and its moons. However, it can be used to simulate any celestial system. If you want to add your bodies to the system:
1) Add necessary constants in *sim_constants.py*
```python
# Parameters for body X
X_MASS: Final[float] = 4e18
X_COLOR: Final[str] = 'b'
X_INIT_POS: Final[Vector] = (2e7, -1e7)
X_INIT_VEL: Final[Vector] = (1e3, 1e3)
X_INIT_ACC: Final[Vector] = (0.0, 0.0)
X_INIT_FORCE: Final[Vector] = (0.0, 0.0)
```

2) Alternatively, if your body is a moon of a planet (let's say planet X), you can find necessary parameters with
```python
# Parameters for moon Y
Y_MASS: Final[float] = 1.8e15
Y_COLOR: Final[str] = 'w'
Y_RADIUS: Final[float] = 23.463e6
Y_INIT_POS: Final[Vector] = (Y_RADIUS, 0.0)
Y_INIT_VEL: Final[Vector] = (0.0, _find_moon_total_velocity(X_MASS, Y_RADIUS))
Y_INIT_ACC: Final[Vector] = (0.0, 0.0)
Y_INIT_FORCE: Final[Vector] = (0.0, 0.0)
```
where Y_RADIUS is the orbital radius of Y on the orbit around X.

3) Create a Body instance of your body in *main.py* in function *main()* and pass it as an argument to *display_simulation()*:
```python
def main() -> None:
    """Initialize celestial bodies and display their simulation."""
    (...)
    body_x = Body(X_MASS, X_COLOR, X_INIT_POS, X_INIT_VEL, X_INIT_ACC, X_INIT_FORCE)
    display_simulation((...), body_x)
```

4) Voilà! You can run your simulation and see the result.

[f1]: http://chart.apis.google.com/chart?cht=tx&chl=m=Ce^{i\alpha}
