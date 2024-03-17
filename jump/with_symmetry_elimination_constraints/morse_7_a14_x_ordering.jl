# NLP written by GAMS Convert at 03/17/24 14:47:55
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#        27        0       21        6        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        21       21        0        0        0        0        0        0
# FX      6
#
# Nonzero counts
#     Total    const       NL
#       138       12      126
#
# Reformulation has removed 1 variable and 1 equation

using JuMP
using MathOptInterface
const MOI = MathOptInterface

model = m = Model()

@variable(m, 0 <= x1 <= 0, start=0)
@variable(m, 0 <= x2 <= 0, start=0)
@variable(m, 0 <= x3 <= 0, start=0)
@variable(m, 0 <= x4 <= 6, start=0)
@variable(m, 0 <= x5 <= 6, start=0)
@variable(m, 0 <= x6 <= 6, start=0)
@variable(m, 0 <= x7 <= 6, start=0)
@variable(m, 0 <= x8 <= 0, start=0)
@variable(m, 0 <= x9 <= 0, start=0)
@variable(m, -6 <= x10 <= 6, start=0)
@variable(m, -6 <= x11 <= 6, start=0)
@variable(m, -6 <= x12 <= 6, start=0)
@variable(m, -6 <= x13 <= 6, start=0)
@variable(m, -6 <= x14 <= 6, start=0)
@variable(m, 0 <= x15 <= 0, start=0)
@variable(m, -6 <= x16 <= 6, start=0)
@variable(m, -6 <= x17 <= 6, start=0)
@variable(m, -6 <= x18 <= 6, start=0)
@variable(m, -6 <= x19 <= 6, start=0)
@variable(m, -6 <= x20 <= 6, start=0)
@variable(m, -6 <= x21 <= 6, start=0)

@NLobjective(m, Min, exp(-14 * sqrt((x1 - x2)^2 + (x8 - x9)^2 + (x15 - x16)^2)
    + 14) * (exp(-14 * sqrt((x1 - x2)^2 + (x8 - x9)^2 + (x15 - x16)^2) + 14)
    - 2) + exp(-14 * sqrt((x1 - x3)^2 + (x8 - x10)^2 + (x15 - x17)^2) + 14) *
    (exp(-14 * sqrt((x1 - x3)^2 + (x8 - x10)^2 + (x15 - x17)^2) + 14) - 2) +
    exp(-14 * sqrt((x1 - x4)^2 + (x8 - x11)^2 + (x15 - x18)^2) + 14) * (exp(-14
    * sqrt((x1 - x4)^2 + (x8 - x11)^2 + (x15 - x18)^2) + 14) - 2) + exp(-14 *
    sqrt((x1 - x5)^2 + (x8 - x12)^2 + (x15 - x19)^2) + 14) * (exp(-14 * sqrt((
    x1 - x5)^2 + (x8 - x12)^2 + (x15 - x19)^2) + 14) - 2) + exp(-14 * sqrt((x1
    - x6)^2 + (x8 - x13)^2 + (x15 - x20)^2) + 14) * (exp(-14 * sqrt((x1 - x6)^
    2 + (x8 - x13)^2 + (x15 - x20)^2) + 14) - 2) + exp(-14 * sqrt((x1 - x7)^2
    + (x8 - x14)^2 + (x15 - x21)^2) + 14) * (exp(-14 * sqrt((x1 - x7)^2 + (x8
    - x14)^2 + (x15 - x21)^2) + 14) - 2) + exp(-14 * sqrt((x2 - x3)^2 + (x9 -
    x10)^2 + (x16 - x17)^2) + 14) * (exp(-14 * sqrt((x2 - x3)^2 + (x9 - x10)^2
    + (x16 - x17)^2) + 14) - 2) + exp(-14 * sqrt((x2 - x4)^2 + (x9 - x11)^2 +
    (x16 - x18)^2) + 14) * (exp(-14 * sqrt((x2 - x4)^2 + (x9 - x11)^2 + (x16 -
    x18)^2) + 14) - 2) + exp(-14 * sqrt((x2 - x5)^2 + (x9 - x12)^2 + (x16 - x19)
    ^2) + 14) * (exp(-14 * sqrt((x2 - x5)^2 + (x9 - x12)^2 + (x16 - x19)^2) +
    14) - 2) + exp(-14 * sqrt((x2 - x6)^2 + (x9 - x13)^2 + (x16 - x20)^2) + 14)
    * (exp(-14 * sqrt((x2 - x6)^2 + (x9 - x13)^2 + (x16 - x20)^2) + 14) - 2)
    + exp(-14 * sqrt((x2 - x7)^2 + (x9 - x14)^2 + (x16 - x21)^2) + 14) * (exp(
    -14 * sqrt((x2 - x7)^2 + (x9 - x14)^2 + (x16 - x21)^2) + 14) - 2) + exp(-14
    * sqrt((x3 - x4)^2 + (x10 - x11)^2 + (x17 - x18)^2) + 14) * (exp(-14 *
    sqrt((x3 - x4)^2 + (x10 - x11)^2 + (x17 - x18)^2) + 14) - 2) + exp(-14 *
    sqrt((x3 - x5)^2 + (x10 - x12)^2 + (x17 - x19)^2) + 14) * (exp(-14 * sqrt((
    x3 - x5)^2 + (x10 - x12)^2 + (x17 - x19)^2) + 14) - 2) + exp(-14 * sqrt((x3
    - x6)^2 + (x10 - x13)^2 + (x17 - x20)^2) + 14) * (exp(-14 * sqrt((x3 - x6)
    ^2 + (x10 - x13)^2 + (x17 - x20)^2) + 14) - 2) + exp(-14 * sqrt((x3 - x7)^2
    + (x10 - x14)^2 + (x17 - x21)^2) + 14) * (exp(-14 * sqrt((x3 - x7)^2 + (
    x10 - x14)^2 + (x17 - x21)^2) + 14) - 2) + exp(-14 * sqrt((x4 - x5)^2 + (
    x11 - x12)^2 + (x18 - x19)^2) + 14) * (exp(-14 * sqrt((x4 - x5)^2 + (x11 -
    x12)^2 + (x18 - x19)^2) + 14) - 2) + exp(-14 * sqrt((x4 - x6)^2 + (x11 -
    x13)^2 + (x18 - x20)^2) + 14) * (exp(-14 * sqrt((x4 - x6)^2 + (x11 - x13)^2
    + (x18 - x20)^2) + 14) - 2) + exp(-14 * sqrt((x4 - x7)^2 + (x11 - x14)^2
    + (x18 - x21)^2) + 14) * (exp(-14 * sqrt((x4 - x7)^2 + (x11 - x14)^2 + (
    x18 - x21)^2) + 14) - 2) + exp(-14 * sqrt((x5 - x6)^2 + (x12 - x13)^2 + (
    x19 - x20)^2) + 14) * (exp(-14 * sqrt((x5 - x6)^2 + (x12 - x13)^2 + (x19 -
    x20)^2) + 14) - 2) + exp(-14 * sqrt((x5 - x7)^2 + (x12 - x14)^2 + (x19 -
    x21)^2) + 14) * (exp(-14 * sqrt((x5 - x7)^2 + (x12 - x14)^2 + (x19 - x21)^2)
    + 14) - 2) + exp(-14 * sqrt((x6 - x7)^2 + (x13 - x14)^2 + (x20 - x21)^2)
    + 14) * (exp(-14 * sqrt((x6 - x7)^2 + (x13 - x14)^2 + (x20 - x21)^2) + 14)
    - 2))

@NLconstraint(m, e1, (x1 - x2)^2 + (x8 - x9)^2 + (x15 - x16)^2
    >= 0.7298336158090001)
@NLconstraint(m, e2, (x1 - x3)^2 + (x8 - x10)^2 + (x15 - x17)^2
    >= 0.7298336158090001)
@NLconstraint(m, e3, (x1 - x4)^2 + (x8 - x11)^2 + (x15 - x18)^2
    >= 0.7298336158090001)
@NLconstraint(m, e4, (x1 - x5)^2 + (x8 - x12)^2 + (x15 - x19)^2
    >= 0.7298336158090001)
@NLconstraint(m, e5, (x1 - x6)^2 + (x8 - x13)^2 + (x15 - x20)^2
    >= 0.7298336158090001)
@NLconstraint(m, e6, (x1 - x7)^2 + (x8 - x14)^2 + (x15 - x21)^2
    >= 0.7298336158090001)
@NLconstraint(m, e7, (x2 - x3)^2 + (x9 - x10)^2 + (x16 - x17)^2
    >= 0.7298336158090001)
@NLconstraint(m, e8, (x2 - x4)^2 + (x9 - x11)^2 + (x16 - x18)^2
    >= 0.7298336158090001)
@NLconstraint(m, e9, (x2 - x5)^2 + (x9 - x12)^2 + (x16 - x19)^2
    >= 0.7298336158090001)
@NLconstraint(m, e10, (x2 - x6)^2 + (x9 - x13)^2 + (x16 - x20)^2
    >= 0.7298336158090001)
@NLconstraint(m, e11, (x2 - x7)^2 + (x9 - x14)^2 + (x16 - x21)^2
    >= 0.7298336158090001)
@NLconstraint(m, e12, (x3 - x4)^2 + (x10 - x11)^2 + (x17 - x18)^2
    >= 0.7298336158090001)
@NLconstraint(m, e13, (x3 - x5)^2 + (x10 - x12)^2 + (x17 - x19)^2
    >= 0.7298336158090001)
@NLconstraint(m, e14, (x3 - x6)^2 + (x10 - x13)^2 + (x17 - x20)^2
    >= 0.7298336158090001)
@NLconstraint(m, e15, (x3 - x7)^2 + (x10 - x14)^2 + (x17 - x21)^2
    >= 0.7298336158090001)
@NLconstraint(m, e16, (x4 - x5)^2 + (x11 - x12)^2 + (x18 - x19)^2
    >= 0.7298336158090001)
@NLconstraint(m, e17, (x4 - x6)^2 + (x11 - x13)^2 + (x18 - x20)^2
    >= 0.7298336158090001)
@NLconstraint(m, e18, (x4 - x7)^2 + (x11 - x14)^2 + (x18 - x21)^2
    >= 0.7298336158090001)
@NLconstraint(m, e19, (x5 - x6)^2 + (x12 - x13)^2 + (x19 - x20)^2
    >= 0.7298336158090001)
@NLconstraint(m, e20, (x5 - x7)^2 + (x12 - x14)^2 + (x19 - x21)^2
    >= 0.7298336158090001)
@NLconstraint(m, e21, (x6 - x7)^2 + (x13 - x14)^2 + (x20 - x21)^2
    >= 0.7298336158090001)
@constraint(m, e22, x1 - x2 <= 0)
@constraint(m, e23, x2 - x3 <= 0)
@constraint(m, e24, x3 - x4 <= 0)
@constraint(m, e25, x4 - x5 <= 0)
@constraint(m, e26, x5 - x6 <= 0)
@constraint(m, e27, x6 - x7 <= 0)
