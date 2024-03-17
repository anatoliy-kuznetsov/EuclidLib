# NLP written by GAMS Convert at 03/17/24 14:48:09
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#        33        0       33        0        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        13       13        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       117       42       75
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
@variable(m, 0 <= x9 <= 1, start=0)
@variable(m, 0 <= x10 <= 1, start=0)
@variable(m, 0 <= x11 <= 1, start=0)
@variable(m, 0 <= x12 <= 1, start=0)
@variable(m, x13, start=0)

@objective(m, Max, x13)

@NLconstraint(m, e1, (x1 - x2)^2 + (x7 - x8)^2 - (2 * x13)^2 >= 0)
@NLconstraint(m, e2, (x1 - x3)^2 + (x7 - x9)^2 - (2 * x13)^2 >= 0)
@NLconstraint(m, e3, (x1 - x4)^2 + (x7 - x10)^2 - (2 * x13)^2 >= 0)
@NLconstraint(m, e4, (x1 - x5)^2 + (x7 - x11)^2 - (2 * x13)^2 >= 0)
@NLconstraint(m, e5, (x1 - x6)^2 + (x7 - x12)^2 - (2 * x13)^2 >= 0)
@NLconstraint(m, e6, (x2 - x3)^2 + (x8 - x9)^2 - (2 * x13)^2 >= 0)
@NLconstraint(m, e7, (x2 - x4)^2 + (x8 - x10)^2 - (2 * x13)^2 >= 0)
@NLconstraint(m, e8, (x2 - x5)^2 + (x8 - x11)^2 - (2 * x13)^2 >= 0)
@NLconstraint(m, e9, (x2 - x6)^2 + (x8 - x12)^2 - (2 * x13)^2 >= 0)
@NLconstraint(m, e10, (x3 - x4)^2 + (x9 - x10)^2 - (2 * x13)^2 >= 0)
@NLconstraint(m, e11, (x3 - x5)^2 + (x9 - x11)^2 - (2 * x13)^2 >= 0)
@NLconstraint(m, e12, (x3 - x6)^2 + (x9 - x12)^2 - (2 * x13)^2 >= 0)
@NLconstraint(m, e13, (x4 - x5)^2 + (x10 - x11)^2 - (2 * x13)^2 >= 0)
@NLconstraint(m, e14, (x4 - x6)^2 + (x10 - x12)^2 - (2 * x13)^2 >= 0)
@NLconstraint(m, e15, (x5 - x6)^2 + (x11 - x12)^2 - (2 * x13)^2 >= 0)
@constraint(m, e16, x1 - x13 >= 0)
@constraint(m, e17, x2 - x13 >= 0)
@constraint(m, e18, x3 - x13 >= 0)
@constraint(m, e19, x4 - x13 >= 0)
@constraint(m, e20, x5 - x13 >= 0)
@constraint(m, e21, x6 - x13 >= 0)
@constraint(m, e22, x7 - x13 >= 0)
@constraint(m, e23, x8 - x13 >= 0)
@constraint(m, e24, x9 - x13 >= 0)
@constraint(m, e25, x10 - x13 >= 0)
@constraint(m, e26, x11 - x13 >= 0)
@constraint(m, e27, x12 - x13 >= 0)
@constraint(m, e28, -0.7071067811865475 * x1 - 0.7071067811865475 * x7 - x13
    >= -0.7071067811865475)
@constraint(m, e29, -0.7071067811865475 * x2 - 0.7071067811865475 * x8 - x13
    >= -0.7071067811865475)
@constraint(m, e30, -0.7071067811865475 * x3 - 0.7071067811865475 * x9 - x13
    >= -0.7071067811865475)
@constraint(m, e31, -0.7071067811865475 * x4 - 0.7071067811865475 * x10 - x13
    >= -0.7071067811865475)
@constraint(m, e32, -0.7071067811865475 * x5 - 0.7071067811865475 * x11 - x13
    >= -0.7071067811865475)
@constraint(m, e33, -0.7071067811865475 * x6 - 0.7071067811865475 * x12 - x13
    >= -0.7071067811865475)
