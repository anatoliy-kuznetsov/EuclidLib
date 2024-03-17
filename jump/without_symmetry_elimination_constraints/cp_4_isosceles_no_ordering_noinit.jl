# NLP written by GAMS Convert at 03/17/24 14:48:05
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#        18        0       18        0        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#         9        9        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#        58       28       30
#
# Reformulation has removed 1 variable and 1 equation

using JuMP
using MathOptInterface
const MOI = MathOptInterface

model = m = Model()

@variable(m, 0 <= x1 <= 1, start=0)
@variable(m, 0 <= x2 <= 1, start=0)
@variable(m, 0 <= x3 <= 1, start=0)
@variable(m, 0 <= x4 <= 1, start=0)
@variable(m, 0 <= x5 <= 1, start=0)
@variable(m, 0 <= x6 <= 1, start=0)
@variable(m, 0 <= x7 <= 1, start=0)
@variable(m, 0 <= x8 <= 1, start=0)
@variable(m, x9, start=0)

@objective(m, Max, x9)

@NLconstraint(m, e1, (x1 - x2)^2 + (x5 - x6)^2 - (2 * x9)^2 >= 0)
@NLconstraint(m, e2, (x1 - x3)^2 + (x5 - x7)^2 - (2 * x9)^2 >= 0)
@NLconstraint(m, e3, (x1 - x4)^2 + (x5 - x8)^2 - (2 * x9)^2 >= 0)
@NLconstraint(m, e4, (x2 - x3)^2 + (x6 - x7)^2 - (2 * x9)^2 >= 0)
@NLconstraint(m, e5, (x2 - x4)^2 + (x6 - x8)^2 - (2 * x9)^2 >= 0)
@NLconstraint(m, e6, (x3 - x4)^2 + (x7 - x8)^2 - (2 * x9)^2 >= 0)
@constraint(m, e7, x1 - x9 >= 0)
@constraint(m, e8, x2 - x9 >= 0)
@constraint(m, e9, x3 - x9 >= 0)
@constraint(m, e10, x4 - x9 >= 0)
@constraint(m, e11, x5 - x9 >= 0)
@constraint(m, e12, x6 - x9 >= 0)
@constraint(m, e13, x7 - x9 >= 0)
@constraint(m, e14, x8 - x9 >= 0)
@constraint(m, e15, -0.7071067811865475 * x1 - 0.7071067811865475 * x5 - x9
    >= -0.7071067811865475)
@constraint(m, e16, -0.7071067811865475 * x2 - 0.7071067811865475 * x6 - x9
    >= -0.7071067811865475)
@constraint(m, e17, -0.7071067811865475 * x3 - 0.7071067811865475 * x7 - x9
    >= -0.7071067811865475)
@constraint(m, e18, -0.7071067811865475 * x4 - 0.7071067811865475 * x8 - x9
    >= -0.7071067811865475)
