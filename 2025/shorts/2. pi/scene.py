from manim import *

class PiRevealScene(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        self.wait(0.5)

        base_radius = 0.5
        circle = Circle(radius=base_radius, color=WHITE)
        diameter = Line(LEFT * base_radius, RIGHT * base_radius, color=WHITE)
        self.play(Create(circle), Create(diameter))
        self.wait(0.5)

        circ_length = PI * base_radius
        circ_line = Line(
            LEFT * circ_length, RIGHT * circ_length,
            color=WHITE
        ).shift(UP * 0.4)
        self.play(
            Transform(circle, circ_line),
            diameter.animate.shift(UP * (base_radius + 0.4))
        )
        self.wait(0.5)

        new_diam = diameter.copy().move_to(DOWN * (base_radius))
        divide = MathTex("\\div", color=WHITE).move_to(ORIGIN)
        self.play(
            Transform(diameter, new_diam),
            FadeIn(divide)
        )
        self.wait(0.3)

        group = VGroup(circle, diameter, divide, circ_line)
        self.play(group.animate.shift(UP * 0.5))
        result = Text("3.14", font_size=32)
        result.next_to(group, DOWN, buff=0.8)
        self.play(FadeIn(result))
        self.wait(1)

        self.clear()
        self.wait(0.3)
        radii = [0.3, 0.4, 0.5]
        positions = [LEFT * 0 + UP * 1,
                     RIGHT * 0 + UP * 0,
                     DOWN * 1.2]
        circles = VGroup(*[
            Circle(radius=r, color=WHITE).move_to(pos)
            for r, pos in zip(radii, positions)
        ])
        self.play(Create(circles))
        self.wait(0.5)

        circ_lines = []
        diam_lines = []
        div_signs = []

        for circle_obj, r, pos in zip(circles, radii, positions):
            target_circ = Line(
                pos + LEFT * PI * r,
                pos + RIGHT * PI * r,
                color=WHITE
            ).shift(UP * 0.3)

            diam = Line(
                pos + LEFT * r,
                pos + RIGHT * r,
                color=WHITE
            ).shift(DOWN * 0.3)

            div_sign = MathTex("\\div", color=WHITE).move_to(pos)

            self.play(Transform(circle_obj, target_circ))
            self.wait(0.1)

            self.play(Create(diam), FadeIn(div_sign))
            self.wait(0.1)

            circ_lines.append(circle_obj) 
            diam_lines.append(diam)
            div_signs.append(div_sign)

        everything = VGroup(*circ_lines, *diam_lines, *div_signs)
        self.play(everything.animate.shift(LEFT * 0.7))
        self.wait(0.5)


        eqs = VGroup(*[
            Text("= 3.14", font_size=24)
            .move_to(pos + RIGHT * 1.2)
            for r, pos in zip(radii, positions)
        ])
        self.play(*[FadeIn(eq) for eq in eqs])
        self.wait(1)

        self.clear()
        pi_text = MathTex("\\pi", font_size=144, color=WHITE)
        self.play(FadeIn(pi_text, scale=0.5))
        self.wait(2)
