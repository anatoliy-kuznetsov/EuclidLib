# NLP written by GAMS Convert at 03/17/24 14:47:57
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#         7        4        3        0        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        12       12        0        0        0        0        0        0
# FX      4
#
# Nonzero counts
#     Total    const       NL
#        18        6       12
#
# Reformulation has removed 1 variable and 1 equation

using JuMP
using MathOptInterface
const MOI = MathOptInterface

model = m = Model()

@variable(m, 0 <= x1 <= 0, start=0)
@variable(m, 0 <= x2 <= 1, start=0)
@variable(m, -1 <= x3 <= 1, start=0)
@variable(m, -1 <= x4 <= 1, start=0)
@variable(m, 0 <= x5 <= 0, start=0)
@variable(m, 0 <= x6 <= 0, start=0)
@variable(m, -1 <= x7 <= 1, start=0)
@variable(m, -1 <= x8 <= 1, start=0)
@variable(m, 1 <= x9 <= 1, start=1)
@variable(m, -1 <= x10 <= 1, start=0)
@variable(m, -1 <= x11 <= 1, start=0)
@variable(m, -1 <= x12 <= 1, start=0)

@NLobjective(m, Min, 1 / sqrt((x1 - x2)^2 + (x5 - x6)^2 + (x9 - x10)^2) + 1 /
    sqrt((x1 - x3)^2 + (x5 - x7)^2 + (x9 - x11)^2) + 1 / sqrt((x1 - x4)^2 + (x5
    - x8)^2 + (x9 - x12)^2) + 1 / sqrt((x2 - x3)^2 + (x6 - x7)^2 + (x10 - x11)
    ^2) + 1 / sqrt((x2 - x4)^2 + (x6 - x8)^2 + (x10 - x12)^2) + 1 / sqrt((x3 -
    x4)^2 + (x7 - x8)^2 + (x11 - x12)^2))

@NLconstraint(m, e1, x1^2 + x5^2 + x9^2 == 1)
@NLconstraint(m, e2, x2^2 + x6^2 + x10^2 == 1)
@NLconstraint(m, e3, x3^2 + x7^2 + x11^2 == 1)
@NLconstraint(m, e4, x4^2 + x8^2 + x12^2 == 1)
@constraint(m, e5, x9 - x10 >= 0)
@constraint(m, e6, x10 - x11 >= 0)
@constraint(m, e7, x11 - x12 >= 0)