import matplotlib; matplotlib.use("TkAgg")
from julia import Julia
from math import e, pi
import numpy as np
from matplotlib.animation import ArtistAnimation
import matplotlib.pyplot as plt
from typing import Tuple, List, Generator

"""
This module shows my extra work on animations and Julia sets
"""

class AnimatedJulia:
    """
    Class responsible for animating Julia sets
    Attributes:
        anim_constant: float - constant common for all julia sets in animation,
            unique points of Julia sets are of the form anim_const * e^(i*a)
    See Also:
        fractal.py for other attributes
    """
    def __init__(self, anim_constant: float = 0.8, iteration_limit: int = 24, accuracy: int = 500,
                 real_domain: Tuple[float, float] = (-2, 2), imaginary_domain: Tuple[float, float] = (-2, 2)) -> None:
        """Initialize Julia Set animation instance."""
        self.anim_constant = anim_constant
        self.iteration_limit = iteration_limit
        self.accuracy = accuracy
        self.real_domain = real_domain
        self.imaginary_domain = imaginary_domain
        self.iter = self._generate_fractal_sequence()

    def _determine_point(self, angle: float) -> complex:
        """Determine a unique point of Julia set for a given angle."""
        return self.anim_constant * e ** (1j * angle)

    def _generate_fractal_sequence(self) -> Generator[Julia, None, None]:
        """Generate all Julia sets that will be used in the animation."""
        for angle in np.arange(0, 2 * pi, 0.1):
            yield Julia(self._determine_point(angle),
                        self.iteration_limit, self.accuracy,
                        self.real_domain, self.imaginary_domain)

    def _give_image(self, julia: Julia) -> plt.imshow:
        """Find a matplotlib image corresponding to a given Julia set."""
        last_convergent_array = np.array(julia.last_convergent_array())
        plt.xlabel("Real part")
        plt.ylabel("Imaginary part")
        return plt.imshow(last_convergent_array.T, cmap='RdGy', interpolation='bilinear',
                          extent=self.real_domain + self.imaginary_domain, animated=True)

    def _generate_images(self) -> List[plt.imshow]:
        """Generates the sequence of images of the animation."""
        ims = []
        for julia in self._generate_fractal_sequence():
            ims.append([self._give_image(julia)])
        return ims

    def show_animation(self) -> None:
        """Displays the animation in a pop-up. Optionally saves the animation."""
        fig = plt.figure()
        ims = self._generate_images()
        ani = ArtistAnimation(fig, ims, interval=50, blit=True)

        # should_save = input('Press 1 to save the animation.')
        # if should_save == '1':
        #     ani.save('julia_sets.mp4', writer="ffmpeg")

        plt.title(f'Animated Julia sets with c = {self.anim_constant}*e^(i*a)')
        plt.show()