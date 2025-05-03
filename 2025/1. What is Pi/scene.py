from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

ELECTRIC_CYAN = "#00FFFF"
LIME_GREEN = "#00FF00"
FUCHSIA_FLASH = "#FF00FF"
BRIGHT_YELLOW = "#FFFF00"
CRIMSON_BLAZE = "#DC143C"
LAVENDER_LIGHT = "#E6E6FA"


class PiExplained(VoiceoverScene):
    def construct(self):
        self.camera.background_color = BLACK
        self.set_speech_service(GTTSService(transcription_model='base'))

        self.wait(1)

        top_left = LEFT * config.frame_width / 2 + UP * config.frame_height / 2

        number_plane = NumberPlane(
            background_line_style={
                "stroke_color": FUCHSIA_FLASH ,
                "stroke_width": 2,
                "stroke_opacity": 0.2,
            },
            axis_config={"color": LAVENDER_LIGHT},
            x_range=(-3, 11, 1),
            y_range=(-4, 4, 1),
        )

        number_plane.z_index = -1
       

        pi_equation = MathTex(r"\pi", r"\approx ", r"\frac{22}{7}", r"\approx ", r"3.14")
        pi, approx1, frac, approx2, approx314 = pi_equation
        pi_equation.move_to(ORIGIN)

        self.add(pi_equation)
        pi_equation.set_opacity(0)

        extra_digits = MathTex(r"15926535\ldots").set_color(ELECTRIC_CYAN)
        extra_digits.next_to(approx314, RIGHT, buff=0.05)

        with self.voiceover(
            text="""You probably learned at school, that <bookmark mark='pi'/> π, 
                    has an approximate value of <bookmark mark='frac'/>22 divided by 7
                    or <bookmark mark='approx'/> 3.14. 
                    Well, it goes much <bookmark mark='extend'/>beyond 3.14. But <bookmark mark='shrink'/> we will get to that in another video."""
        ) as tracker:
            self.wait_until_bookmark("pi")
            self.play(pi.animate.set_opacity(1))

            self.wait_until_bookmark("frac")
            self.play(approx1.animate.set_opacity(1), frac.animate.set_opacity(1))

            self.wait_until_bookmark("approx")
            self.play(approx2.animate.set_opacity(1), approx314.animate.set_opacity(1))

            self.wait_until_bookmark("extend")
            self.play(Write(extra_digits))
            
            self.wait_until_bookmark("shrink")
            self.play(FadeOut(extra_digits))

        with self.voiceover(text="Have you ever realized where <bookmark mark='indicate' /> these values came from?") as tracker:
            self.wait_until_bookmark("indicate")
            self.play(Indicate(frac, color=BRIGHT_YELLOW))
            self.play(Indicate(approx314, color=BRIGHT_YELLOW))

        with self.voiceover(text="First, I will add a coordinate system to make things easier to understand.") as tracker:     
            self.play(FadeOut(pi_equation))    
            self.play(FadeIn(number_plane))

        with self.voiceover(text="Now let's make a <bookmark mark='circle' /> circle.") as tracker:
            circle = Circle(radius=1.2).shift(LEFT, 2 * UP).set_color(ELECTRIC_CYAN).set_stroke(width=2)
            self.wait_until_bookmark("circle")
            self.play(Create(circle))

        with self.voiceover(text="And place a <bookmark mark='point' /> point at the circumference.") as tracker:
            dot = Dot(color=CRIMSON_BLAZE)
            initial_angle = 3 * PI / 2 
            angle_tracker = ValueTracker(initial_angle)

            def update_dot(mob):
                angle = angle_tracker.get_value()
                mob.move_to(circle.get_center() + circle.radius * RIGHT * np.cos(angle) + circle.radius * UP * np.sin(angle))

            dot.add_updater(update_dot)

            self.wait_until_bookmark("point")
            self.play(Create(dot))

        with self.voiceover(text="I will move the circle <bookmark mark='move_to_origin' /> so that the point aligns with the origin of the coordinate system.") as tracker:
            self.wait_until_bookmark("move_to_origin")
            self.play(circle.animate.move_to(number_plane.get_origin() + circle.radius * UP))
        
        with self.voiceover(text="Now I will <bookmark mark='rotate_right' /> rotate the circle till we hit the point again.") as tracker:
             self.wait_until_bookmark("rotate_right")
            
             self.play(
                circle.animate.shift(RIGHT *  2 * PI * circle.radius),
                angle_tracker.animate.set_value(initial_angle - 2 * PI),
                rate_func=linear,
                run_time = tracker.duration
            )
        
        with self.voiceover(text="This is the circumference of the circle.") as tracker:
            line = Line(
                start=number_plane.c2p(0, 0),
                end=number_plane.c2p(number_plane.p2c(dot.get_center())[0], 0),
                color=BRIGHT_YELLOW,
                stroke_width=2
            )

            self.play(Create(line))
        
        with self.voiceover(text="Now let's see how much diameter the same distance covers.") as tracker:
            self.play(FadeOut(dot))
            self.play(circle.animate.shift(LEFT * (2 * PI * circle.radius - circle.radius) + UP * 0.1))
            diameter_line = Line(
                start=circle.point_at_angle(0),        
                end=circle.point_at_angle(PI),         
                color=LIME_GREEN,
                stroke_width=2
            )

            self.play(Create(diameter_line))
        
            
        circle_and_dia = VGroup(circle, diameter_line)

        with self.voiceover(text="1") as tracker:
            d1 = diameter_line.copy()
            self.play(d1.animate.shift(DOWN * (circle.radius + 0.1)), run_time=0.5)

            dot_1 = Dot(point = d1.get_right())
            label_1 = Text("1").scale(0.5)
            label_1.add_updater(lambda x: x.next_to(dot_1.get_center(), DOWN, buff=0.15))
            dot_1.z_index = 10

            self.play(Create(dot_1), run_time=0.5)
            self.play(Write(label_1), run_time=0.5)
            self.play(circle_and_dia.animate.shift(RIGHT * 2 * circle.radius), run_time=0.5)
         


        with self.voiceover(text="2") as tracker:
            d2 = diameter_line.copy()
            self.play(d2.animate.shift(DOWN * (circle.radius + 0.1)), run_time=0.5)

            dot_2 = Dot(point = d2.get_right())
            label_2 = Text("2").scale(0.5)
            label_2.add_updater(lambda x: x.next_to(dot_2.get_center(), DOWN, buff=0.15))
            dot_2.z_index = 10

            self.play(Create(dot_2), run_time=0.5)
            self.play(Write(label_2), run_time=0.5)

            self.play(circle_and_dia.animate.shift(RIGHT * 2 * circle.radius), run_time=0.5)

        with self.voiceover(text="3") as tracker:
            d3 = diameter_line.copy()
            self.play(d3.animate.shift(DOWN * (circle.radius + 0.1)), run_time=0.5)

            dot_3 = Dot(point = d3.get_right())
            label_3 = Text("3").scale(0.5)
            label_3.add_updater(lambda x: x.next_to(dot_3.get_center(), DOWN, buff=0.15))
            dot_3.z_index = 10

            self.play(Create(dot_3), run_time=0.5)
            self.play(Write(label_3), run_time=0.5)

            self.play(circle_and_dia.animate.shift(RIGHT * 2 * circle.radius), run_time=0.5)

        with self.voiceover(text="And the final bit remaining is <bookmark mark='14' /> .14, making the total <bookmark mark='314' /> 3.14.") as tracker:
            self.wait_until_bookmark("14")

            d14 = diameter_line.copy()
            self.play(d14.animate
                    .scale(0.14, about_point=diameter_line.get_end())
                    .shift(DOWN * (circle.radius + 0.1))
            )

            self.wait_until_bookmark("314")
            dot_14 = Dot(point = d14.get_right())
            label_14 = Text("3.14").scale(0.5)
            label_14.add_updater(lambda x: x.next_to(dot_14.get_center(), np.array([1,-1,0]), buff=0.15))
            dot_14.z_index = 10
            self.play(Create(dot_14))
            self.play(Write(label_14))
        
        with self.voiceover(text="Now, this remains the same regardless of the <bookmark mark='size' /> size of the circle.") as tracker:
            self.remove(line)
            self.play(circle_and_dia.animate.shift(UP))
            self.wait_until_bookmark('size')

            dot_1_copy = dot_1.copy().set_opacity(0)
            dot_2_copy = dot_2.copy().set_opacity(0)
            dot_3_copy = dot_3.copy().set_opacity(0)
            dot_14_copy = dot_14.copy().set_opacity(0)

            dot_1.add_updater(lambda m: m.move_to(dot_1_copy.get_center()))
            dot_2.add_updater(lambda m: m.move_to(dot_2_copy.get_center()))
            dot_3.add_updater(lambda m: m.move_to(dot_3_copy.get_center()))
            dot_14.add_updater(lambda m: m.move_to(dot_14_copy.get_center()))

            dia_group = VGroup(dot_1_copy, dot_2_copy, dot_3_copy, dot_14_copy, d1, d2, d3, d14)
            label_group = VGroup(label_1, label_2, label_3, label_14)

            self.play(
                circle_and_dia.animate.scale(1.2),
                dia_group.animate.scale(1.2, about_point=number_plane.get_origin()),
            )

            self.play(
                circle_and_dia.animate.scale(0.5),
                dia_group.animate.scale(0.5, about_point=number_plane.get_origin()),
            )


            with self.voiceover(text="So, you could say π, <bookmark mark='quote' /> is the number of diameters it takes to reach the circumference.") as tracker:

                        self.wait_until_bookmark("quote")
                        self.clear()

                        part1 = Text("“", slant=ITALIC).scale(0.5)
                        part2 = Text("π", slant=ITALIC).scale(0.5).set_color(CRIMSON_BLAZE)  
                        part3 = Text(" is the number of ", slant=ITALIC).scale(0.5)
                        part4 = Text("diameters", slant=ITALIC).scale(0.5).set_color(ELECTRIC_CYAN)  
                        part5 = Text(" it takes to reach the ", slant=ITALIC).scale(0.5)
                        part6 = Text("circumference", slant=ITALIC).scale(0.5).set_color(LIME_GREEN) 
                        part7 = Text("”", slant=ITALIC).scale(0.5)

                        quote = VGroup(part1, part2, part3, part4, part5, part6, part7)

                        quote.arrange(RIGHT, buff=0.1)
                        quote.align_to(part1, DOWN) 
                        quote.move_to(ORIGIN)

                        self.play(Write(quote))

        self.wait(1)


        






     

