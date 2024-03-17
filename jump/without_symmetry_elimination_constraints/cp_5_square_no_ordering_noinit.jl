# NLP written by GAMS Convert at 03/17/24 14:48:08
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#        30        0       20       10        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        11       11        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#        90       40       50
#
# Reformulation has removed 1 variable and 1 equation

using JuMP
using MathOptInterface
const MOI = MathOptInterface

model = m = Model()

@variable(m, -0.5 <= x1 <= 0.5, start=0)
@variable(m, -0.5 <= x2 <= 0.5, start=0)
@variable(m, -0.5 <= x3 <= 0.5, start=0)
@variable(m, -0.5 <= x4 <= 0.5, start=0)
@variable(m, -0.5 <= x5 <= 0.5, start=0)
@variable(m, -0.5 <= x6 <= 0.5, start=0)
@variable(m, -0.5 <= x7 <= 0.5, start=0)
@variable(m, -0.5 <= x8 <= 0.5, start=0)
@variable(m, -0.5 <= x9 <= 0.5, start=0)
@variable(m, -0.5 <= x10 <= 0.5, start=0)
@variable(m, x11, start=0)

@objective(m, Max, x11)

@NLconstraint(m, e1, (x1 - x2)^2 + (x6 - x7)^2 - (2 * x11)^2 >= 0)
@NLconstraint(m, e2, (x1 - x3)^2 + (x6 - x8)^2 - (2 * x11)^2 >= 0)
@NLconstraint(m, e3, (x1 - x4)^2 + (x6 - x9)^2 - (2 * x11)^2 >= 0)
@NLconstraint(m, e4, (x1 - x5)^2 + (x6 - x10)^2 - (2 * x11)^2 >= 0)
@NLconstraint(m, e5, (x2 - x3)^2 + (x7 - x8)^2 - (2 * x11)^2 >= 0)
@NLconstraint(m, e6, (x2 - x4)^2 + (x7 - x9)^2 - (2 * x11)^2 >= 0)
@NLconstraint(m, e7, (x2 - x5)^2 + (x7 - x10)^2 - (2 * x11)^2 >= 0)
@NLconstraint(m, e8, (x3 - x4)^2 + (x8 - x9)^2 - (2 * x11)^2 >= 0)
@NLconstraint(m, e9, (x3 - x5)^2 + (x8 - x10)^2 - (2 * x11)^2 >= 0)
@NLconstraint(m, e10, (x4 - x5)^2 + (x9 - x10)^2 - (2 * x11)^2 >= 0)
@constraint(m, e11, x1 + x11 <= 0.5)
@constraint(m, e12, x2 + x11 <= 0.5)
@constraint(m, e13, x3 + x11 <= 0.5)
@constraint(m, e14, x4 + x11 <= 0.5)
@constraint(m, e15, x5 + x11 <= 0.5)
@constraint(m, e16, x1 - x11 >= -0.5)
@constraint(m, e17, x2 - x11 >= -0.5)
@constraint(m, e18, x3 - x11 >= -0.5)
@constraint(m, e19, x4 - x11 >= -0.5)
@constraint(m, e20, x5 - x11 >= -0.5)
@constraint(m, e21, x6 + x11 <= 0.5)
@constraint(m, e22, x7 + x11 <= 0.5)
@constraint(m, e23, x8 + x11 <= 0.5)
@constraint(m, e24, x9 + x11 <= 0.5)
@constraint(m, e25, x10 + x11 <= 0.5)
@constraint(m, e26, x6 - x11 >= -0.5)
@constraint(m, e27, x7 - x11 >= -0.5)
@constraint(m, e28, x8 - x11 >= -0.5)
@constraint(m, e29, x9 - x11 >= -0.5)
@constraint(m, e30, x10 - x11 >= -0.5)
