# NLP written by GAMS Convert at 03/17/24 14:47:57
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#        19       10        9        0        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        30       30        0        0        0        0        0        0
# FX      4
#
# Nonzero counts
#     Total    const       NL
#        48       18       30
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
@variable(m, -1 <= x5 <= 1, start=0)
@variable(m, -1 <= x6 <= 1, start=0)
@variable(m, -1 <= x7 <= 1, start=0)
@variable(m, -1 <= x8 <= 1, start=0)
@variable(m, -1 <= x9 <= 1, start=0)
@variable(m, -1 <= x10 <= 1, start=0)
@variable(m, 0 <= x11 <= 0, start=0)
@variable(m, 0 <= x12 <= 0, start=0)
@variable(m, -1 <= x13 <= 1, start=0)
@variable(m, -1 <= x14 <= 1, start=0)
@variable(m, -1 <= x15 <= 1, start=0)
@variable(m, -1 <= x16 <= 1, start=0)
@variable(m, -1 <= x17 <= 1, start=0)
@variable(m, -1 <= x18 <= 1, start=0)
@variable(m, -1 <= x19 <= 1, start=0)
@variable(m, -1 <= x20 <= 1, start=0)
@variable(m, 1 <= x21 <= 1, start=1)
@variable(m, -1 <= x22 <= 1, start=0)
@variable(m, -1 <= x23 <= 1, start=0)
@variable(m, -1 <= x24 <= 1, start=0)
@variable(m, -1 <= x25 <= 1, start=0)
@variable(m, -1 <= x26 <= 1, start=0)
@variable(m, -1 <= x27 <= 1, start=0)
@variable(m, -1 <= x28 <= 1, start=0)
@variable(m, -1 <= x29 <= 1, start=0)
@variable(m, -1 <= x30 <= 1, start=0)

@NLobjective(m, Min, 1 / sqrt((x1 - x2)^2 + (x11 - x12)^2 + (x21 - x22)^2) + 1
    / sqrt((x1 - x3)^2 + (x11 - x13)^2 + (x21 - x23)^2) + 1 / sqrt((x1 - x4)^2
    + (x11 - x14)^2 + (x21 - x24)^2) + 1 / sqrt((x1 - x5)^2 + (x11 - x15)^2 +
    (x21 - x25)^2) + 1 / sqrt((x1 - x6)^2 + (x11 - x16)^2 + (x21 - x26)^2) + 1
    / sqrt((x1 - x7)^2 + (x11 - x17)^2 + (x21 - x27)^2) + 1 / sqrt((x1 - x8)^2
    + (x11 - x18)^2 + (x21 - x28)^2) + 1 / sqrt((x1 - x9)^2 + (x11 - x19)^2 +
    (x21 - x29)^2) + 1 / sqrt((x1 - x10)^2 + (x11 - x20)^2 + (x21 - x30)^2) + 1
    / sqrt((x2 - x3)^2 + (x12 - x13)^2 + (x22 - x23)^2) + 1 / sqrt((x2 - x4)^2
    + (x12 - x14)^2 + (x22 - x24)^2) + 1 / sqrt((x2 - x5)^2 + (x12 - x15)^2 +
    (x22 - x25)^2) + 1 / sqrt((x2 - x6)^2 + (x12 - x16)^2 + (x22 - x26)^2) + 1
    / sqrt((x2 - x7)^2 + (x12 - x17)^2 + (x22 - x27)^2) + 1 / sqrt((x2 - x8)^2
    + (x12 - x18)^2 + (x22 - x28)^2) + 1 / sqrt((x2 - x9)^2 + (x12 - x19)^2 +
    (x22 - x29)^2) + 1 / sqrt((x2 - x10)^2 + (x12 - x20)^2 + (x22 - x30)^2) + 1
    / sqrt((x3 - x4)^2 + (x13 - x14)^2 + (x23 - x24)^2) + 1 / sqrt((x3 - x5)^2
    + (x13 - x15)^2 + (x23 - x25)^2) + 1 / sqrt((x3 - x6)^2 + (x13 - x16)^2 +
    (x23 - x26)^2) + 1 / sqrt((x3 - x7)^2 + (x13 - x17)^2 + (x23 - x27)^2) + 1
    / sqrt((x3 - x8)^2 + (x13 - x18)^2 + (x23 - x28)^2) + 1 / sqrt((x3 - x9)^2
    + (x13 - x19)^2 + (x23 - x29)^2) + 1 / sqrt((x3 - x10)^2 + (x13 - x20)^2
    + (x23 - x30)^2) + 1 / sqrt((x4 - x5)^2 + (x14 - x15)^2 + (x24 - x25)^2)
    + 1 / sqrt((x4 - x6)^2 + (x14 - x16)^2 + (x24 - x26)^2) + 1 / sqrt((x4 -
    x7)^2 + (x14 - x17)^2 + (x24 - x27)^2) + 1 / sqrt((x4 - x8)^2 + (x14 - x18)
    ^2 + (x24 - x28)^2) + 1 / sqrt((x4 - x9)^2 + (x14 - x19)^2 + (x24 - x29)^2)
    + 1 / sqrt((x4 - x10)^2 + (x14 - x20)^2 + (x24 - x30)^2) + 1 / sqrt((x5 -
    x6)^2 + (x15 - x16)^2 + (x25 - x26)^2) + 1 / sqrt((x5 - x7)^2 + (x15 - x17)
    ^2 + (x25 - x27)^2) + 1 / sqrt((x5 - x8)^2 + (x15 - x18)^2 + (x25 - x28)^2)
    + 1 / sqrt((x5 - x9)^2 + (x15 - x19)^2 + (x25 - x29)^2) + 1 / sqrt((x5 -
    x10)^2 + (x15 - x20)^2 + (x25 - x30)^2) + 1 / sqrt((x6 - x7)^2 + (x16 - x17)
    ^2 + (x26 - x27)^2) + 1 / sqrt((x6 - x8)^2 + (x16 - x18)^2 + (x26 - x28)^2)
    + 1 / sqrt((x6 - x9)^2 + (x16 - x19)^2 + (x26 - x29)^2) + 1 / sqrt((x6 -
    x10)^2 + (x16 - x20)^2 + (x26 - x30)^2) + 1 / sqrt((x7 - x8)^2 + (x17 - x18)
    ^2 + (x27 - x28)^2) + 1 / sqrt((x7 - x9)^2 + (x17 - x19)^2 + (x27 - x29)^2)
    + 1 / sqrt((x7 - x10)^2 + (x17 - x20)^2 + (x27 - x30)^2) + 1 / sqrt((x8 -
    x9)^2 + (x18 - x19)^2 + (x28 - x29)^2) + 1 / sqrt((x8 - x10)^2 + (x18 - x20)
    ^2 + (x28 - x30)^2) + 1 / sqrt((x9 - x10)^2 + (x19 - x20)^2 + (x29 - x30)^2))


    @NLconstraint(m, e1, x1^2 + x11^2 + x21^2 == 1)
@NLconstraint(m, e2, x2^2 + x12^2 + x22^2 == 1)
@NLconstraint(m, e3, x3^2 + x13^2 + x23^2 == 1)
@NLconstraint(m, e4, x4^2 + x14^2 + x24^2 == 1)
@NLconstraint(m, e5, x5^2 + x15^2 + x25^2 == 1)
@NLconstraint(m, e6, x6^2 + x16^2 + x26^2 == 1)
@NLconstraint(m, e7, x7^2 + x17^2 + x27^2 == 1)
@NLconstraint(m, e8, x8^2 + x18^2 + x28^2 == 1)
@NLconstraint(m, e9, x9^2 + x19^2 + x29^2 == 1)
@NLconstraint(m, e10, x10^2 + x20^2 + x30^2 == 1)
@constraint(m, e11, x21 - x22 >= 0)
@constraint(m, e12, x22 - x23 >= 0)
@constraint(m, e13, x23 - x24 >= 0)
@constraint(m, e14, x24 - x25 >= 0)
@constraint(m, e15, x25 - x26 >= 0)
@constraint(m, e16, x26 - x27 >= 0)
@constraint(m, e17, x27 - x28 >= 0)
@constraint(m, e18, x28 - x29 >= 0)
@constraint(m, e19, x29 - x30 >= 0)