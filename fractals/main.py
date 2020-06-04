from mandelbrot import Mandelbrot
from julia import Julia
from animated_julia import AnimatedJulia

def main() -> None:
    i = prompt()
    if i == 1:
        plot_mandelbrot()
    elif i == 2:
        plot_julia()
    elif i == 3:
        plot_animation()

def prompt() -> int:
    print("""Menu:
1 - Display Mandelbrot set.
2 - Display Julia Set
3 - Animated Julia Sets.
""")
    while 1:
        i = input('Type a number: ')
        if i not in ('1', '2', '3'):
            print('Incorrect option.')
        else:
            return int(i)

def plot_mandelbrot() -> None:
    """Plot the Mandelbrot set."""
    print('Please wait, the Mandelbrot set is being loaded.')
    mandelbrot = Mandelbrot(iteration_limit=255, accuracy=300,
                            real_domain=(-2.025, 0.6), imaginary_domain=(-1.125, 1.125))
    mandelbrot.plot()

def plot_julia() -> None:
    """Plot the Julia set."""
    print('Please wait, a Julia set is being loaded.')
    julia = Julia(constant=complex(-0.1, 0.8), iteration_limit=24, accuracy=500,
                  real_domain=(-2.0, 2.0), imaginary_domain=(-2.0, 2.0))
    julia.plot()

def plot_animation() -> None:
    """Shows the animation of Julia sets."""
    print('Please wait, animation is being loaded.')
    animation = AnimatedJulia()
    animation.show_animation()


if __name__ == '__main__':
    main()