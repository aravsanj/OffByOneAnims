from manim import *

class BinarySearchScene1(Scene):
    def construct(self):
        values = list(range(1, 11))
        boxes = VGroup()
        spacing = 0.7

        for i, val in enumerate(values):
            box = Square(side_length=0.5, color=WHITE)
            text = Text(str(val), font_size=20).move_to(box.get_center())
            boxes.add(VGroup(box, text).move_to(DOWN * i * spacing))
        boxes.arrange(DOWN, buff=0.2).move_to(LEFT * 1.5)

        middle_index = 4
        middle_box, middle_text = boxes[middle_index]

        target_number = Text("5", font_size=36, color=BLUE)
        target_label = VGroup(Text("Target: ", font_size=36, color=BLUE),
                              target_number).arrange(RIGHT, buff=0.2)
        target_label.to_corner(UR).shift(DOWN * 1)

        arrow = Arrow(
            start=target_label.get_bottom() + DOWN * 0.2,
            end=middle_box.get_right()   + RIGHT * 0.2,
            color=BLUE, buff=0.1
        )

        self.play(
            LaggedStart(*[FadeIn(g, shift=LEFT*0.5) for g in boxes], lag_ratio=0.1),
            run_time=1.5
        )
        self.play(middle_box.animate.set_fill(YELLOW, opacity=0.5).set_stroke(YELLOW, width=3), run_time=0.3)
        self.play(FadeIn(target_label), GrowArrow(arrow), run_time=1)
        self.wait(0.5)

        self.play(Indicate(target_number, scale_factor=1.1), Indicate(middle_text, scale_factor=1.2), run_time=0.8)
        self.play(Transform(target_number, Text("9", font_size=36, color=BLUE).move_to(target_number)), run_time=0.5)
        self.wait(0.2)

        to_remove = boxes[: middle_index+1]
        self.play(
            *[g[0].animate.set_fill(GRAY_A, opacity=0.3) for g in to_remove],
            *[g[1].animate.set_color(GRAY_A) for g in to_remove],
            run_time=0.4
        )
        self.play(*[FadeOut(g) for g in to_remove], run_time=0.4)

        remaining = boxes[middle_index+1:]
        shift_up = UP * (spacing * (middle_index+1) / 2)
        self.play(*[g.animate.shift(shift_up) for g in remaining], run_time=0.6)
        self.wait(0.5)

        mid2 = 2
        box8, txt8 = remaining[mid2]
        self.play(box8.animate.set_fill(YELLOW, opacity=0.5).set_stroke(YELLOW, width=3), run_time=0.3)
        self.play(
            target_number.animate.set_color(RED),
            txt8.animate.set_color(RED),
            run_time=0.2
        )
        self.play(Indicate(target_number), Indicate(txt8), run_time=0.6)
        self.play(
            target_number.animate.set_color(BLUE),
            txt8.animate.set_color(WHITE),
            run_time=0.2
        )
        self.wait(0.2)

        to_remove2 = remaining[: mid2+1]
        self.play(
            *[g[0].animate.set_fill(GRAY_A, opacity=0.3) for g in to_remove2],
            *[g[1].animate.set_color(GRAY_A) for g in to_remove2],
            run_time=0.4
        )
        self.play(*[FadeOut(g) for g in to_remove2], run_time=0.4)

        remaining2 = remaining[mid2+1:]
        shift_up2 = UP * (spacing * (mid2+1) / 2)
        self.play(*[g.animate.shift(shift_up2) for g in remaining2], run_time=0.6)
        self.wait(0.5)

        box9, txt9 = remaining2[0]
        self.play(box9.animate.set_fill(YELLOW, opacity=0.5).set_stroke(YELLOW, width=3), run_time=0.3)
        self.play(
            target_number.animate.set_color(GREEN),
            txt9.animate.set_color(GREEN),
            run_time=0.2
        )
        self.play(Indicate(target_number), Indicate(txt9), run_time=0.6)
        self.wait(1)



class BinarySearchScene2(Scene):
    def construct(self):
        array_text = Tex("[1][2]\\dots[1~billion]")

        steps_1b = Text("30 steps", font_size=48).set_color(YELLOW)
        steps_group = VGroup(array_text, steps_1b).arrange(DOWN, buff=1).move_to(ORIGIN)

        self.play(Write(array_text))
        self.play(FadeIn(steps_1b, shift=DOWN))
        self.wait(1)

        array_text_2b = Tex("[1][2]\\dots[2~billion]")
        steps_2b = Text("31 steps", font_size=48).set_color(YELLOW)
        steps_group_2 = VGroup(array_text_2b, steps_2b).arrange(DOWN, buff=1).move_to(ORIGIN)

        self.play(Transform(array_text, array_text_2b))
        self.play(Transform(steps_1b, steps_2b))
        self.wait(1)

        array_text_back = Tex("[1][2]\\dots[1~billion]")
        steps_text_back = Text("30 steps", font_size=48).set_color(YELLOW)
        steps_group_back = VGroup(array_text_back, steps_text_back).arrange(DOWN, buff=1).move_to(ORIGIN)

        self.play(Transform(array_text, array_text_back))
        self.play(Transform(steps_1b, steps_text_back))


class BinarySearchScene3(Scene):
    def construct(self):
        array = MathTex("[1][2]...[n]").scale(1.2).to_edge(UP)
        self.play(FadeIn(array))
        self.wait(0.5)

        n_orig = MathTex("n").scale(1.5)
        self.play(FadeIn(n_orig))
        self.wait(0.5)

        n_div_2 = MathTex(r"\frac{n}{2}").scale(1.5).move_to(n_orig)
        self.play(Transform(n_orig, n_div_2))
        self.wait(0.5)

        n_div_4 = MathTex(r"\frac{n}{4}").scale(1.5).move_to(n_orig)
        self.play(Transform(n_orig, n_div_4))
        self.wait(0.5)

        left_frac = MathTex(r"\frac{n}{4}").scale(1.5).shift(LEFT * 1)
        eq_sign  = MathTex("=").scale(1.5).next_to(left_frac, RIGHT, buff=0.2)
        pow2     = MathTex(r"\frac{n}{2^2}").scale(1.5).next_to(eq_sign, RIGHT, buff=0.2)

        self.play(Transform(n_orig, left_frac))
        self.wait(0.3)
        self.play(Write(eq_sign), Write(pow2))
        self.wait(0.7)

        self.play(
            FadeOut(n_orig), 
            FadeOut(eq_sign)
        )
        self.wait(0.3)

        self.play(pow2.animate.move_to(ORIGIN))
        self.wait(0.5)

        frac_k = MathTex(r"\frac{n}{2^k}").scale(1.5)
        self.play(TransformMatchingTex(pow2, frac_k))
        self.wait(0.7)

        self.play(frac_k.animate.shift(LEFT * 1))
        eq_one = MathTex("= 1").scale(1.5).next_to(frac_k, RIGHT, buff=0.2)
        self.play(Write(eq_one))
        self.wait(0.7)

        combined = VGroup(frac_k, eq_one)
        target1  = MathTex("n = 2^k").scale(1.5)
        self.play(
            TransformMatchingShapes(
                combined, 
                target1, 
                path_arc=30 * DEGREES
            )
        )
        self.wait(0.8)

        final_eq = MathTex(r"\log_2\bigl(n\bigr) = k").scale(1.5)
        self.play(
            TransformMatchingShapes(
                target1, 
                final_eq, 
                path_arc=-30 * DEGREES
            )
        )
        self.wait(1.2)





