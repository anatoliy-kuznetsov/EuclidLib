# NLP written by GAMS Convert at 05/15/24 11:36:17
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#         5        5        0        0        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        15       15        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#        15        0       15
#
# Reformulation has removed 1 variable and 1 equation

using JuMP
using MathOptInterface
const MOI = MathOptInterface

model = m = Model()

@variable(m, -1 <= x1 <= 1, start=0)
@variable(m, -1 <= x2 <= 1, start=0)
@variable(m, -1 <= x3 <= 1, start=0)
@variable(m, -1 <= x4 <= 1, start=0)
@variable(m, -1 <= x5 <= 1, start=0)
@variable(m, -1 <= x6 <= 1, start=0)
@variable(m, -1 <= x7 <= 1, start=0)
@variable(m, -1 <= x8 <= 1, start=0)
@variable(m, -1 <= x9 <= 1, start=0)
@variable(m, -1 <= x10 <= 1, start=0)
@variable(m, -1 <= x11 <= 1, start=0)
@variable(m, -1 <= x12 <= 1, start=0)
@variable(m, -1 <= x13 <= 1, start=0)
@variable(m, -1 <= x14 <= 1, start=0)
@variable(m, -1 <= x15 <= 1, start=0)

@NLobjective(m, Min, 1 / sqrt((x1 - x2)^2 + (x6 - x7)^2 + (x11 - x12)^2) + 1 /
    sqrt((x1 - x3)^2 + (x6 - x8)^2 + (x11 - x13)^2) + 1 / sqrt((x1 - x4)^2 + (
    x6 - x9)^2 + (x11 - x14)^2) + 1 / sqrt((x1 - x5)^2 + (x6 - x10)^2 + (x11 -
    x15)^2) + 1 / sqrt((x2 - x3)^2 + (x7 - x8)^2 + (x12 - x13)^2) + 1 / sqrt((
    x2 - x4)^2 + (x7 - x9)^2 + (x12 - x14)^2) + 1 / sqrt((x2 - x5)^2 + (x7 -
    x10)^2 + (x12 - x15)^2) + 1 / sqrt((x3 - x4)^2 + (x8 - x9)^2 + (x13 - x14)^
    2) + 1 / sqrt((x3 - x5)^2 + (x8 - x10)^2 + (x13 - x15)^2) + 1 / sqrt((x4 -
    x5)^2 + (x9 - x10)^2 + (x14 - x15)^2))

@NLconstraint(m, e1, x1^2 + x6^2 + x11^2 == 1)
@NLconstraint(m, e2, x2^2 + x7^2 + x12^2 == 1)
@NLconstraint(m, e3, x3^2 + x8^2 + x13^2 == 1)
@NLconstraint(m, e4, x4^2 + x9^2 + x14^2 == 1)
@NLconstraint(m, e5, x5^2 + x10^2 + x15^2 == 1)
