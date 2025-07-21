from manim import *
import numpy as np


class JarvisMarch(Scene):
    def construct(self):
        a = Axes(x_range=[-1, 101], y_range=[-1, 101])
        # self.add(a)

        def x(dot): return a.point_to_coords(dot.get_center())[0]
        def y(dot): return a.point_to_coords(dot.get_center())[1]
        def point_coords(dot): return np.array([x(dot), y(dot)])

        def orientation(p, q, r):
            """Return cross product of vectors pq x qr"""
            p, q, r = point_coords(p), point_coords(q), point_coords(r)
            return np.cross(q - p, r - q)

        def find_left_point(dots):
            minn = 0
            for i in range(1, len(dots)):
                if x(dots[i]) < x(dots[minn]) or (x(dots[i]) == x(dots[minn]) and y(dots[i]) < y(dots[minn])):
                    minn = i
            return minn

        dots = VGroup(
            Dot(point=a.c2p(42, 89)),
            Dot(point=a.c2p(62, 72)),
            Dot(point=a.c2p(52, 60)),
            Dot(point=a.c2p(30, 35)),
            Dot(point=a.c2p(47, 41)),
            Dot(point=a.c2p(29, 59)),
            Dot(point=a.c2p(37, 86)),
            Dot(point=a.c2p(65, 29)),
            Dot(point=a.c2p(17, 54)),
            Dot(point=a.c2p(50, 74)),
            Dot(point=a.c2p(61, 56)),
            Dot(point=a.c2p(66, 42)),
            Dot(point=a.c2p(34, 5)),
        )
        self.add(dots)

        n = len(dots)
        hull = []
        l = find_left_point(dots)
        p = l

        while True:
            hull.append(p)
            q = (p + 1) % n

            self.play(dots[p].animate.set_color(RED), run_time=0.2)

            for r in range(n):
                if r == p or r == q:
                    continue

                check_line = Line(
                    dots[p].get_center(), dots[r].get_center(), color=BLUE, stroke_opacity=0.4
                )
                self.add(check_line)
                self.wait(0.05)
                self.remove(check_line)

                if orientation(dots[p], dots[q], dots[r]) < 0:
                    q = r

            edge = Line(dots[p].get_center(), dots[q].get_center(), color=YELLOW)
            self.play(Create(edge), run_time=0.3)

            p = q
            if p == l:
                break

        self.wait(1)
