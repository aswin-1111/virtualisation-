from manim import *
import numpy as np

class JarvisMarch(Scene):
    def construct(self):
        a = Axes(x_range=[-1, 101], y_range=[-1, 101], )
        # self.add(a)

        for _ in range(10):
            x = np.random.randint(0, 100)
            y = np.random.randint(0, 100)
            dot_location = a.c2p(x, y)
            dot = Dot(point=dot_location, radius=0.08, color=BLUE, fill_opacity=0.1, stroke_width=2, )
            self.add(dot)

        
