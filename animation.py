from manim import *
import numpy as np

class JarvisMarch(Scene):
    def construct(self):
        a = Axes(x_range=[-1, 101], y_range=[-1, 101], )
        # self.add(a)

        dots = VGroup()

        sample_dots = VGroup(
            Dot(point=(a.coords_to_point(42, 89))),
            Dot(point=(a.coords_to_point(62, 72))),
            Dot(point=(a.coords_to_point(52, 60))),
            Dot(point=(a.coords_to_point(30, 35))),
            Dot(point=(a.coords_to_point(47, 41))),
            Dot(point=(a.coords_to_point(29, 59))),
            Dot(point=(a.coords_to_point(37, 86))),
            Dot(point=(a.coords_to_point(65, 29))),
            Dot(point=(a.coords_to_point(17, 54))),
            Dot(point=(a.coords_to_point(50, 74))),
            Dot(point=(a.coords_to_point(61, 56))),
            Dot(point=(a.coords_to_point(66, 42))),
            Dot(point=(a.coords_to_point(34, 5))),
            )

        # for _ in range(10):
        #     x = np.random.randint(0, 100)
        #     y = np.random.randint(0, 100)
        #     dot_location = a.c2p(x, y)
        #     dot = Dot(point=dot_location, radius=0.08, color=BLUE, fill_opacity=0.1, stroke_width=2)
        #     dots.add(dot)

        # self.add(dots)
        self.add(sample_dots)
    

        
