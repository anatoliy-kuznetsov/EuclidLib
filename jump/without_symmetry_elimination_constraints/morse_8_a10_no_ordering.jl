# NLP written by GAMS Convert at 03/17/24 14:48:08
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#        28        0       28        0        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        24       24        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       168        0      168
#
# Reformulation has removed 1 variable and 1 equation

using JuMP
using MathOptInterface
const MOI = MathOptInterface

model = m = Model()

@variable(m, 0 <= x1 <= 7, start=0)
@variable(m, 0 <= x2 <= 7, start=0)
@variable(m, 0 <= x3 <= 7, start=0)
@variable(m, 0 <= x4 <= 7, start=0)
@variable(m, 0 <= x5 <= 7, start=0)
@variable(m, 0 <= x6 <= 7, start=0)
@variable(m, 0 <= x7 <= 7, start=0)
@variable(m, 0 <= x8 <= 7, start=0)
@variable(m, -7 <= x9 <= 7, start=0)
@variable(m, -7 <= x10 <= 7, start=0)
@variable(m, -7 <= x11 <= 7, start=0)
@variable(m, -7 <= x12 <= 7, start=0)
@variable(m, -7 <= x13 <= 7, start=0)
@variable(m, -7 <= x14 <= 7, start=0)
@variable(m, -7 <= x15 <= 7, start=0)
@variable(m, -7 <= x16 <= 7, start=0)
@variable(m, -7 <= x17 <= 7, start=0)
@variable(m, -7 <= x18 <= 7, start=0)
@variable(m, -7 <= x19 <= 7, start=0)
@variable(m, -7 <= x20 <= 7, start=0)
@variable(m, -7 <= x21 <= 7, start=0)
@variable(m, -7 <= x22 <= 7, start=0)
@variable(m, -7 <= x23 <= 7, start=0)
@variable(m, -7 <= x24 <= 7, start=0)

@NLobjective(m, Min, exp(-10 * sqrt((x1 - x2)^2 + (x9 - x10)^2 + (x17 - x18)^2)
    + 10) * (exp(-10 * sqrt((x1 - x2)^2 + (x9 - x10)^2 + (x17 - x18)^2) + 10)
    - 2) + exp(-10 * sqrt((x1 - x3)^2 + (x9 - x11)^2 + (x17 - x19)^2) + 10) *
    (exp(-10 * sqrt((x1 - x3)^2 + (x9 - x11)^2 + (x17 - x19)^2) + 10) - 2) +
    exp(-10 * sqrt((x1 - x4)^2 + (x9 - x12)^2 + (x17 - x20)^2) + 10) * (exp(-10
    * sqrt((x1 - x4)^2 + (x9 - x12)^2 + (x17 - x20)^2) + 10) - 2) + exp(-10 *
    sqrt((x1 - x5)^2 + (x9 - x13)^2 + (x17 - x21)^2) + 10) * (exp(-10 * sqrt((
    x1 - x5)^2 + (x9 - x13)^2 + (x17 - x21)^2) + 10) - 2) + exp(-10 * sqrt((x1
    - x6)^2 + (x9 - x14)^2 + (x17 - x22)^2) + 10) * (exp(-10 * sqrt((x1 - x6)^
    2 + (x9 - x14)^2 + (x17 - x22)^2) + 10) - 2) + exp(-10 * sqrt((x1 - x7)^2
    + (x9 - x15)^2 + (x17 - x23)^2) + 10) * (exp(-10 * sqrt((x1 - x7)^2 + (x9
    - x15)^2 + (x17 - x23)^2) + 10) - 2) + exp(-10 * sqrt((x1 - x8)^2 + (x9 -
    x16)^2 + (x17 - x24)^2) + 10) * (exp(-10 * sqrt((x1 - x8)^2 + (x9 - x16)^2
    + (x17 - x24)^2) + 10) - 2) + exp(-10 * sqrt((x2 - x3)^2 + (x10 - x11)^2
    + (x18 - x19)^2) + 10) * (exp(-10 * sqrt((x2 - x3)^2 + (x10 - x11)^2 + (
    x18 - x19)^2) + 10) - 2) + exp(-10 * sqrt((x2 - x4)^2 + (x10 - x12)^2 + (
    x18 - x20)^2) + 10) * (exp(-10 * sqrt((x2 - x4)^2 + (x10 - x12)^2 + (x18 -
    x20)^2) + 10) - 2) + exp(-10 * sqrt((x2 - x5)^2 + (x10 - x13)^2 + (x18 -
    x21)^2) + 10) * (exp(-10 * sqrt((x2 - x5)^2 + (x10 - x13)^2 + (x18 - x21)^2)
    + 10) - 2) + exp(-10 * sqrt((x2 - x6)^2 + (x10 - x14)^2 + (x18 - x22)^2)
    + 10) * (exp(-10 * sqrt((x2 - x6)^2 + (x10 - x14)^2 + (x18 - x22)^2) + 10)
    - 2) + exp(-10 * sqrt((x2 - x7)^2 + (x10 - x15)^2 + (x18 - x23)^2) + 10)
    * (exp(-10 * sqrt((x2 - x7)^2 + (x10 - x15)^2 + (x18 - x23)^2) + 10) - 2)
    + exp(-10 * sqrt((x2 - x8)^2 + (x10 - x16)^2 + (x18 - x24)^2) + 10) * (exp
    (-10 * sqrt((x2 - x8)^2 + (x10 - x16)^2 + (x18 - x24)^2) + 10) - 2) + exp(-
    10 * sqrt((x3 - x4)^2 + (x11 - x12)^2 + (x19 - x20)^2) + 10) * (exp(-10 *
    sqrt((x3 - x4)^2 + (x11 - x12)^2 + (x19 - x20)^2) + 10) - 2) + exp(-10 *
    sqrt((x3 - x5)^2 + (x11 - x13)^2 + (x19 - x21)^2) + 10) * (exp(-10 * sqrt((
    x3 - x5)^2 + (x11 - x13)^2 + (x19 - x21)^2) + 10) - 2) + exp(-10 * sqrt((x3
    - x6)^2 + (x11 - x14)^2 + (x19 - x22)^2) + 10) * (exp(-10 * sqrt((x3 - x6)
    ^2 + (x11 - x14)^2 + (x19 - x22)^2) + 10) - 2) + exp(-10 * sqrt((x3 - x7)^2
    + (x11 - x15)^2 + (x19 - x23)^2) + 10) * (exp(-10 * sqrt((x3 - x7)^2 + (
    x11 - x15)^2 + (x19 - x23)^2) + 10) - 2) + exp(-10 * sqrt((x3 - x8)^2 + (
    x11 - x16)^2 + (x19 - x24)^2) + 10) * (exp(-10 * sqrt((x3 - x8)^2 + (x11 -
    x16)^2 + (x19 - x24)^2) + 10) - 2) + exp(-10 * sqrt((x4 - x5)^2 + (x12 -
    x13)^2 + (x20 - x21)^2) + 10) * (exp(-10 * sqrt((x4 - x5)^2 + (x12 - x13)^2
    + (x20 - x21)^2) + 10) - 2) + exp(-10 * sqrt((x4 - x6)^2 + (x12 - x14)^2
    + (x20 - x22)^2) + 10) * (exp(-10 * sqrt((x4 - x6)^2 + (x12 - x14)^2 + (
    x20 - x22)^2) + 10) - 2) + exp(-10 * sqrt((x4 - x7)^2 + (x12 - x15)^2 + (
    x20 - x23)^2) + 10) * (exp(-10 * sqrt((x4 - x7)^2 + (x12 - x15)^2 + (x20 -
    x23)^2) + 10) - 2) + exp(-10 * sqrt((x4 - x8)^2 + (x12 - x16)^2 + (x20 -
    x24)^2) + 10) * (exp(-10 * sqrt((x4 - x8)^2 + (x12 - x16)^2 + (x20 - x24)^2)
    + 10) - 2) + exp(-10 * sqrt((x5 - x6)^2 + (x13 - x14)^2 + (x21 - x22)^2)
    + 10) * (exp(-10 * sqrt((x5 - x6)^2 + (x13 - x14)^2 + (x21 - x22)^2) + 10)
    - 2) + exp(-10 * sqrt((x5 - x7)^2 + (x13 - x15)^2 + (x21 - x23)^2) + 10)
    * (exp(-10 * sqrt((x5 - x7)^2 + (x13 - x15)^2 + (x21 - x23)^2) + 10) - 2)
    + exp(-10 * sqrt((x5 - x8)^2 + (x13 - x16)^2 + (x21 - x24)^2) + 10) * (exp
    (-10 * sqrt((x5 - x8)^2 + (x13 - x16)^2 + (x21 - x24)^2) + 10) - 2) + exp(-
    10 * sqrt((x6 - x7)^2 + (x14 - x15)^2 + (x22 - x23)^2) + 10) * (exp(-10 *
    sqrt((x6 - x7)^2 + (x14 - x15)^2 + (x22 - x23)^2) + 10) - 2) + exp(-10 *
    sqrt((x6 - x8)^2 + (x14 - x16)^2 + (x22 - x24)^2) + 10) * (exp(-10 * sqrt((
    x6 - x8)^2 + (x14 - x16)^2 + (x22 - x24)^2) + 10) - 2) + exp(-10 * sqrt((x7
    - x8)^2 + (x15 - x16)^2 + (x23 - x24)^2) + 10) * (exp(-10 * sqrt((x7 - x8)
    ^2 + (x15 - x16)^2 + (x23 - x24)^2) + 10) - 2))

@NLconstraint(m, e1, (x1 - x2)^2 + (x9 - x10)^2 + (x17 - x18)^2
    >= 0.6144835321)
@NLconstraint(m, e2, (x1 - x3)^2 + (x9 - x11)^2 + (x17 - x19)^2
    >= 0.6144835321)
@NLconstraint(m, e3, (x1 - x4)^2 + (x9 - x12)^2 + (x17 - x20)^2
    >= 0.6144835321)
@NLconstraint(m, e4, (x1 - x5)^2 + (x9 - x13)^2 + (x17 - x21)^2
    >= 0.6144835321)
@NLconstraint(m, e5, (x1 - x6)^2 + (x9 - x14)^2 + (x17 - x22)^2
    >= 0.6144835321)
@NLconstraint(m, e6, (x1 - x7)^2 + (x9 - x15)^2 + (x17 - x23)^2
    >= 0.6144835321)
@NLconstraint(m, e7, (x1 - x8)^2 + (x9 - x16)^2 + (x17 - x24)^2
    >= 0.6144835321)
@NLconstraint(m, e8, (x2 - x3)^2 + (x10 - x11)^2 + (x18 - x19)^2
    >= 0.6144835321)
@NLconstraint(m, e9, (x2 - x4)^2 + (x10 - x12)^2 + (x18 - x20)^2
    >= 0.6144835321)
@NLconstraint(m, e10, (x2 - x5)^2 + (x10 - x13)^2 + (x18 - x21)^2
    >= 0.6144835321)
@NLconstraint(m, e11, (x2 - x6)^2 + (x10 - x14)^2 + (x18 - x22)^2
    >= 0.6144835321)
@NLconstraint(m, e12, (x2 - x7)^2 + (x10 - x15)^2 + (x18 - x23)^2
    >= 0.6144835321)
@NLconstraint(m, e13, (x2 - x8)^2 + (x10 - x16)^2 + (x18 - x24)^2
    >= 0.6144835321)
@NLconstraint(m, e14, (x3 - x4)^2 + (x11 - x12)^2 + (x19 - x20)^2
    >= 0.6144835321)
@NLconstraint(m, e15, (x3 - x5)^2 + (x11 - x13)^2 + (x19 - x21)^2
    >= 0.6144835321)
@NLconstraint(m, e16, (x3 - x6)^2 + (x11 - x14)^2 + (x19 - x22)^2
    >= 0.6144835321)
@NLconstraint(m, e17, (x3 - x7)^2 + (x11 - x15)^2 + (x19 - x23)^2
    >= 0.6144835321)
@NLconstraint(m, e18, (x3 - x8)^2 + (x11 - x16)^2 + (x19 - x24)^2
    >= 0.6144835321)
@NLconstraint(m, e19, (x4 - x5)^2 + (x12 - x13)^2 + (x20 - x21)^2
    >= 0.6144835321)
@NLconstraint(m, e20, (x4 - x6)^2 + (x12 - x14)^2 + (x20 - x22)^2
    >= 0.6144835321)
@NLconstraint(m, e21, (x4 - x7)^2 + (x12 - x15)^2 + (x20 - x23)^2
    >= 0.6144835321)
@NLconstraint(m, e22, (x4 - x8)^2 + (x12 - x16)^2 + (x20 - x24)^2
    >= 0.6144835321)
@NLconstraint(m, e23, (x5 - x6)^2 + (x13 - x14)^2 + (x21 - x22)^2
    >= 0.6144835321)
@NLconstraint(m, e24, (x5 - x7)^2 + (x13 - x15)^2 + (x21 - x23)^2
    >= 0.6144835321)
@NLconstraint(m, e25, (x5 - x8)^2 + (x13 - x16)^2 + (x21 - x24)^2
    >= 0.6144835321)
@NLconstraint(m, e26, (x6 - x7)^2 + (x14 - x15)^2 + (x22 - x23)^2
    >= 0.6144835321)
@NLconstraint(m, e27, (x6 - x8)^2 + (x14 - x16)^2 + (x22 - x24)^2
    >= 0.6144835321)
@NLconstraint(m, e28, (x7 - x8)^2 + (x15 - x16)^2 + (x23 - x24)^2
    >= 0.6144835321)
