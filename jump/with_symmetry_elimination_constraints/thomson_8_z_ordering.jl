# NLP written by GAMS Convert at 03/17/24 14:47:55
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#        15        8        7        0        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        24       24        0        0        0        0        0        0
# FX      4
#
# Nonzero counts
#     Total    const       NL
#        38       14       24
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
@variable(m, 0 <= x9 <= 0, start=0)
@variable(m, 0 <= x10 <= 0, start=0)
@variable(m, -1 <= x11 <= 1, start=0)
@variable(m, -1 <= x12 <= 1, start=0)
@variable(m, -1 <= x13 <= 1, start=0)
@variable(m, -1 <= x14 <= 1, start=0)
@variable(m, -1 <= x15 <= 1, start=0)
@variable(m, -1 <= x16 <= 1, start=0)
@variable(m, 1 <= x17 <= 1, start=1)
@variable(m, -1 <= x18 <= 1, start=0)
@variable(m, -1 <= x19 <= 1, start=0)
@variable(m, -1 <= x20 <= 1, start=0)
@variable(m, -1 <= x21 <= 1, start=0)
@variable(m, -1 <= x22 <= 1, start=0)
@variable(m, -1 <= x23 <= 1, start=0)
@variable(m, -1 <= x24 <= 1, start=0)

@NLobjective(m, Min, 1 / sqrt((x1 - x2)^2 + (x9 - x10)^2 + (x17 - x18)^2) + 1
    / sqrt((x1 - x3)^2 + (x9 - x11)^2 + (x17 - x19)^2) + 1 / sqrt((x1 - x4)^2
    + (x9 - x12)^2 + (x17 - x20)^2) + 1 / sqrt((x1 - x5)^2 + (x9 - x13)^2 + (
    x17 - x21)^2) + 1 / sqrt((x1 - x6)^2 + (x9 - x14)^2 + (x17 - x22)^2) + 1 /
    sqrt((x1 - x7)^2 + (x9 - x15)^2 + (x17 - x23)^2) + 1 / sqrt((x1 - x8)^2 + (
    x9 - x16)^2 + (x17 - x24)^2) + 1 / sqrt((x2 - x3)^2 + (x10 - x11)^2 + (x18
    - x19)^2) + 1 / sqrt((x2 - x4)^2 + (x10 - x12)^2 + (x18 - x20)^2) + 1 /
    sqrt((x2 - x5)^2 + (x10 - x13)^2 + (x18 - x21)^2) + 1 / sqrt((x2 - x6)^2 +
    (x10 - x14)^2 + (x18 - x22)^2) + 1 / sqrt((x2 - x7)^2 + (x10 - x15)^2 + (
    x18 - x23)^2) + 1 / sqrt((x2 - x8)^2 + (x10 - x16)^2 + (x18 - x24)^2) + 1
    / sqrt((x3 - x4)^2 + (x11 - x12)^2 + (x19 - x20)^2) + 1 / sqrt((x3 - x5)^2
    + (x11 - x13)^2 + (x19 - x21)^2) + 1 / sqrt((x3 - x6)^2 + (x11 - x14)^2 +
    (x19 - x22)^2) + 1 / sqrt((x3 - x7)^2 + (x11 - x15)^2 + (x19 - x23)^2) + 1
    / sqrt((x3 - x8)^2 + (x11 - x16)^2 + (x19 - x24)^2) + 1 / sqrt((x4 - x5)^2
    + (x12 - x13)^2 + (x20 - x21)^2) + 1 / sqrt((x4 - x6)^2 + (x12 - x14)^2 +
    (x20 - x22)^2) + 1 / sqrt((x4 - x7)^2 + (x12 - x15)^2 + (x20 - x23)^2) + 1
    / sqrt((x4 - x8)^2 + (x12 - x16)^2 + (x20 - x24)^2) + 1 / sqrt((x5 - x6)^2
    + (x13 - x14)^2 + (x21 - x22)^2) + 1 / sqrt((x5 - x7)^2 + (x13 - x15)^2 +
    (x21 - x23)^2) + 1 / sqrt((x5 - x8)^2 + (x13 - x16)^2 + (x21 - x24)^2) + 1
    / sqrt((x6 - x7)^2 + (x14 - x15)^2 + (x22 - x23)^2) + 1 / sqrt((x6 - x8)^2
    + (x14 - x16)^2 + (x22 - x24)^2) + 1 / sqrt((x7 - x8)^2 + (x15 - x16)^2 +
    (x23 - x24)^2))

@NLconstraint(m, e1, x1^2 + x9^2 + x17^2 == 1)
@NLconstraint(m, e2, x2^2 + x10^2 + x18^2 == 1)
@NLconstraint(m, e3, x3^2 + x11^2 + x19^2 == 1)
@NLconstraint(m, e4, x4^2 + x12^2 + x20^2 == 1)
@NLconstraint(m, e5, x5^2 + x13^2 + x21^2 == 1)
@NLconstraint(m, e6, x6^2 + x14^2 + x22^2 == 1)
@NLconstraint(m, e7, x7^2 + x15^2 + x23^2 == 1)
@NLconstraint(m, e8, x8^2 + x16^2 + x24^2 == 1)
@constraint(m, e9, x17 - x18 >= 0)
@constraint(m, e10, x18 - x19 >= 0)
@constraint(m, e11, x19 - x20 >= 0)
@constraint(m, e12, x20 - x21 >= 0)
@constraint(m, e13, x21 - x22 >= 0)
@constraint(m, e14, x22 - x23 >= 0)
@constraint(m, e15, x23 - x24 >= 0)