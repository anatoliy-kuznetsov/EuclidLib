# NLP written by GAMS Convert at 03/17/24 14:47:58
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#        14        0       10        4        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        15       15        0        0        0        0        0        0
# FX      6
#
# Nonzero counts
#     Total    const       NL
#        68        8       60
#
# Reformulation has removed 1 variable and 1 equation

using JuMP
using MathOptInterface
const MOI = MathOptInterface

model = m = Model()

@variable(m, 0 <= x1 <= 0, start=0)
@variable(m, 0 <= x2 <= 0, start=0)
@variable(m, 0 <= x3 <= 0, start=0)
@variable(m, 0 <= x4 <= 4, start=0)
@variable(m, 0 <= x5 <= 4, start=0)
@variable(m, 0 <= x6 <= 0, start=0)
@variable(m, 0 <= x7 <= 0, start=0)
@variable(m, -4 <= x8 <= 4, start=0)
@variable(m, -4 <= x9 <= 4, start=0)
@variable(m, -4 <= x10 <= 4, start=0)
@variable(m, 0 <= x11 <= 0, start=0)
@variable(m, -4 <= x12 <= 4, start=0)
@variable(m, -4 <= x13 <= 4, start=0)
@variable(m, -4 <= x14 <= 4, start=0)
@variable(m, -4 <= x15 <= 4, start=0)

@NLobjective(m, Min, exp(-14 * sqrt((x1 - x2)^2 + (x6 - x7)^2 + (x11 - x12)^2)
    + 14) * (exp(-14 * sqrt((x1 - x2)^2 + (x6 - x7)^2 + (x11 - x12)^2) + 14)
    - 2) + exp(-14 * sqrt((x1 - x3)^2 + (x6 - x8)^2 + (x11 - x13)^2) + 14) * (
    exp(-14 * sqrt((x1 - x3)^2 + (x6 - x8)^2 + (x11 - x13)^2) + 14) - 2) + exp(
    -14 * sqrt((x1 - x4)^2 + (x6 - x9)^2 + (x11 - x14)^2) + 14) * (exp(-14 *
    sqrt((x1 - x4)^2 + (x6 - x9)^2 + (x11 - x14)^2) + 14) - 2) + exp(-14 * sqrt
    ((x1 - x5)^2 + (x6 - x10)^2 + (x11 - x15)^2) + 14) * (exp(-14 * sqrt((x1 -
    x5)^2 + (x6 - x10)^2 + (x11 - x15)^2) + 14) - 2) + exp(-14 * sqrt((x2 - x3)
    ^2 + (x7 - x8)^2 + (x12 - x13)^2) + 14) * (exp(-14 * sqrt((x2 - x3)^2 + (x7
    - x8)^2 + (x12 - x13)^2) + 14) - 2) + exp(-14 * sqrt((x2 - x4)^2 + (x7 -
    x9)^2 + (x12 - x14)^2) + 14) * (exp(-14 * sqrt((x2 - x4)^2 + (x7 - x9)^2 +
    (x12 - x14)^2) + 14) - 2) + exp(-14 * sqrt((x2 - x5)^2 + (x7 - x10)^2 + (
    x12 - x15)^2) + 14) * (exp(-14 * sqrt((x2 - x5)^2 + (x7 - x10)^2 + (x12 -
    x15)^2) + 14) - 2) + exp(-14 * sqrt((x3 - x4)^2 + (x8 - x9)^2 + (x13 - x14)
    ^2) + 14) * (exp(-14 * sqrt((x3 - x4)^2 + (x8 - x9)^2 + (x13 - x14)^2) + 14)
    - 2) + exp(-14 * sqrt((x3 - x5)^2 + (x8 - x10)^2 + (x13 - x15)^2) + 14) *
    (exp(-14 * sqrt((x3 - x5)^2 + (x8 - x10)^2 + (x13 - x15)^2) + 14) - 2) +
    exp(-14 * sqrt((x4 - x5)^2 + (x9 - x10)^2 + (x14 - x15)^2) + 14) * (exp(-14
    * sqrt((x4 - x5)^2 + (x9 - x10)^2 + (x14 - x15)^2) + 14) - 2))

@NLconstraint(m, e1, (x1 - x2)^2 + (x6 - x7)^2 + (x11 - x12)^2
    >= 0.7298336158090001)
@NLconstraint(m, e2, (x1 - x3)^2 + (x6 - x8)^2 + (x11 - x13)^2
    >= 0.7298336158090001)
@NLconstraint(m, e3, (x1 - x4)^2 + (x6 - x9)^2 + (x11 - x14)^2
    >= 0.7298336158090001)
@NLconstraint(m, e4, (x1 - x5)^2 + (x6 - x10)^2 + (x11 - x15)^2
    >= 0.7298336158090001)
@NLconstraint(m, e5, (x2 - x3)^2 + (x7 - x8)^2 + (x12 - x13)^2
    >= 0.7298336158090001)
@NLconstraint(m, e6, (x2 - x4)^2 + (x7 - x9)^2 + (x12 - x14)^2
    >= 0.7298336158090001)
@NLconstraint(m, e7, (x2 - x5)^2 + (x7 - x10)^2 + (x12 - x15)^2
    >= 0.7298336158090001)
@NLconstraint(m, e8, (x3 - x4)^2 + (x8 - x9)^2 + (x13 - x14)^2
    >= 0.7298336158090001)
@NLconstraint(m, e9, (x3 - x5)^2 + (x8 - x10)^2 + (x13 - x15)^2
    >= 0.7298336158090001)
@NLconstraint(m, e10, (x4 - x5)^2 + (x9 - x10)^2 + (x14 - x15)^2
    >= 0.7298336158090001)
@constraint(m, e11, x1 - x2 <= 0)
@constraint(m, e12, x2 - x3 <= 0)
@constraint(m, e13, x3 - x4 <= 0)
@constraint(m, e14, x4 - x5 <= 0)
