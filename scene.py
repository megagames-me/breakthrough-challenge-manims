from manim import *

# Help from https://gitlab.com/cw-manim/koch-curve/-/blob/main/koch_curve.py

# n is which iteration of the koch curve

# 3.464102
def KochCurve(n: int, unit=-1, length=12, stroke_width=8, color=("#0A68EF", "#4AF1F2", "#0A68EF")):
    l = length / (3 ** n)

    LineGroup = Line().set_length(l)

    def NextIteration(LineGroup):
        return VGroup(
            *[LineGroup.copy().rotate(i) for i in [0, PI / 3, -PI / 3, 0]]
        ).arrange(RIGHT, buff=0, aligned_edge=DOWN)

    for _ in range(n):
        LineGroup = NextIteration(LineGroup)

    KC = VGroup()

    KC.add(
        VMobject(stroke_width=stroke_width)
        .set_points(LineGroup.get_all_points())
        .set_color(color)
    )

    return KC


class Koch(Scene):
    def construct(self):
        level = Variable(
            0, Tex("level"), var_type=Integer).set_color("#4AF1F2")
        unit = Variable(3**4, Tex("unit"),
                        var_type=Integer).set_color("#28C73D")
        length = Variable(1, Tex("\\# of units"),
                          var_type=Integer).set_color("#28C73D")
        
        # unit.font_size = 48
        # length.font_size = 48

        txt = (
            VGroup(Tex("Koch Curve", font_size=60), level, unit, length)
            .arrange(DOWN, aligned_edge=LEFT)
            .to_corner(UL)
        )
        kc = KochCurve(0, stroke_width=12).to_edge(DOWN, buff=2.5)

        self.add(kc, txt[0], txt[1])
        self.wait()

        for i in range(1, 6):
            self.play(
                level.tracker.animate.set_value(i),
                kc.animate.become(
                    KochCurve(i, stroke_width=12 - (2 * i)
                              ).to_edge(DOWN, buff=2.5)
                ),
            )
            self.wait()

        self.wait(2)
        
        self.play(Write(unit), Write(length))   

    
        for i in range(0, 6):
            self.play(
                unit.tracker.animate.set_value(3 ** (5-i)),
                length.tracker.animate.set_value(4 ** (i)),
                kc.animate.become(
                    (KochCurve(5, stroke_width=2) +
                     KochCurve(i , stroke_width=12 - (2*i), color="#28C73D").move_to(kc[0].get_center() - [0, ((4.134102 / 2) if i == 0 else 0), 0]))
                )
            )
            self.wait()

        txt.remove(unit, length)
        self.play(FadeOut(unit), FadeOut(length))
        
        
        nTex = Tex("$N = 4$").set_color("#CFEB1A")
        epTex = Tex("$\\varepsilon = \\frac13$").set_color("#CFEB1A")
        
        txt.add(nTex, epTex).arrange(DOWN, aligned_edge=LEFT).to_corner(UL)
        
        self.play(Write(nTex), Write(epTex))
        self.wait()
        
        self.play(Uncreate(kc))
        
        equation = Tex("""\\begin{align*}
N &= \\varepsilon^{-D} \\\\
D &= -\log_{\\varepsilon}N \\\\
D &= -\dfrac{\log N}{\log \\varepsilon} \\\\
D &\\approx 1.26186
\end{align*}""")
        equation.font_size = 72
        
        self.play(Write(equation).set_run_time(3))
        

class GrapeExample(Scene):
    def construct(self):
        self.camera.background_color = PURE_GREEN
        dimension = Variable(
            3, Tex("D"), var_type=Integer).set_color("#0f0f0f").to_corner(UL)
        length = Variable(
            1, Tex("side length"), var_type=Integer).set_color("#0f0f0f").next_to(dimension, DOWN, aligned_edge=LEFT)
        volume = Variable(
            1, Tex("volume"), var_type=Integer).set_color("#0f0f0f").next_to(length, DOWN, aligned_edge=LEFT)
        
        self.play(Write(dimension))
        self.wait(5)
        self.play(Write(length))
        self.wait(3)
        self.play(Write(volume))
        self.wait(5)
        
        equation = Tex("""\\begin{align*}
N &= \\varepsilon^{-D}\\\\
N &= \\left(\dfrac12\\right)^{-3}\\\\
N &= 8
\end{align*}""").set_color("#0f0f0f").to_corner(UR)
        
        self.play(Write(equation))
        self.play(
            length.tracker.animate.set_value(2),
            volume.tracker.animate.set_value(8)
        )
        self.wait(3)
        self.play(FadeOut(dimension), FadeOut(length), FadeOut(volume), Unwrite(equation))