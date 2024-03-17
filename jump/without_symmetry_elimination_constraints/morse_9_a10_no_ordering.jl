# NLP written by GAMS Convert at 03/17/24 14:48:09
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#        36        0       36        0        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        27       27        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       216        0      216
#
# Reformulation has removed 1 variable and 1 equation

using JuMP
using MathOptInterface
const MOI = MathOptInterface

model = m = Model()

@variable(m, 0 <= x1 <= 8, start=0)
@variable(m, 0 <= x2 <= 8, start=0)
@variable(m, 0 <= x3 <= 8, start=0)
@variable(m, 0 <= x4 <= 8, start=0)
@variable(m, 0 <= x5 <= 8, start=0)
@variable(m, 0 <= x6 <= 8, start=0)
@variable(m, 0 <= x7 <= 8, start=0)
@variable(m, 0 <= x8 <= 8, start=0)
@variable(m, 0 <= x9 <= 8, start=0)
@variable(m, -8 <= x10 <= 8, start=0)
@variable(m, -8 <= x11 <= 8, start=0)
@variable(m, -8 <= x12 <= 8, start=0)
@variable(m, -8 <= x13 <= 8, start=0)
@variable(m, -8 <= x14 <= 8, start=0)
@variable(m, -8 <= x15 <= 8, start=0)
@variable(m, -8 <= x16 <= 8, start=0)
@variable(m, -8 <= x17 <= 8, start=0)
@variable(m, -8 <= x18 <= 8, start=0)
@variable(m, -8 <= x19 <= 8, start=0)
@variable(m, -8 <= x20 <= 8, start=0)
@variable(m, -8 <= x21 <= 8, start=0)
@variable(m, -8 <= x22 <= 8, start=0)
@variable(m, -8 <= x23 <= 8, start=0)
@variable(m, -8 <= x24 <= 8, start=0)
@variable(m, -8 <= x25 <= 8, start=0)
@variable(m, -8 <= x26 <= 8, start=0)
@variable(m, -8 <= x27 <= 8, start=0)

@NLobjective(m, Min, exp(-10 * sqrt((x1 - x2)^2 + (x10 - x11)^2 + (x19 - x20)^2)
    + 10) * (exp(-10 * sqrt((x1 - x2)^2 + (x10 - x11)^2 + (x19 - x20)^2) + 10)
    - 2) + exp(-10 * sqrt((x1 - x3)^2 + (x10 - x12)^2 + (x19 - x21)^2) + 10)
    * (exp(-10 * sqrt((x1 - x3)^2 + (x10 - x12)^2 + (x19 - x21)^2) + 10) - 2)
    + exp(-10 * sqrt((x1 - x4)^2 + (x10 - x13)^2 + (x19 - x22)^2) + 10) * (exp
    (-10 * sqrt((x1 - x4)^2 + (x10 - x13)^2 + (x19 - x22)^2) + 10) - 2) + exp(-
    10 * sqrt((x1 - x5)^2 + (x10 - x14)^2 + (x19 - x23)^2) + 10) * (exp(-10 *
    sqrt((x1 - x5)^2 + (x10 - x14)^2 + (x19 - x23)^2) + 10) - 2) + exp(-10 *
    sqrt((x1 - x6)^2 + (x10 - x15)^2 + (x19 - x24)^2) + 10) * (exp(-10 * sqrt((
    x1 - x6)^2 + (x10 - x15)^2 + (x19 - x24)^2) + 10) - 2) + exp(-10 * sqrt((x1
    - x7)^2 + (x10 - x16)^2 + (x19 - x25)^2) + 10) * (exp(-10 * sqrt((x1 - x7)
    ^2 + (x10 - x16)^2 + (x19 - x25)^2) + 10) - 2) + exp(-10 * sqrt((x1 - x8)^2
    + (x10 - x17)^2 + (x19 - x26)^2) + 10) * (exp(-10 * sqrt((x1 - x8)^2 + (
    x10 - x17)^2 + (x19 - x26)^2) + 10) - 2) + exp(-10 * sqrt((x1 - x9)^2 + (
    x10 - x18)^2 + (x19 - x27)^2) + 10) * (exp(-10 * sqrt((x1 - x9)^2 + (x10 -
    x18)^2 + (x19 - x27)^2) + 10) - 2) + exp(-10 * sqrt((x2 - x3)^2 + (x11 -
    x12)^2 + (x20 - x21)^2) + 10) * (exp(-10 * sqrt((x2 - x3)^2 + (x11 - x12)^2
    + (x20 - x21)^2) + 10) - 2) + exp(-10 * sqrt((x2 - x4)^2 + (x11 - x13)^2
    + (x20 - x22)^2) + 10) * (exp(-10 * sqrt((x2 - x4)^2 + (x11 - x13)^2 + (
    x20 - x22)^2) + 10) - 2) + exp(-10 * sqrt((x2 - x5)^2 + (x11 - x14)^2 + (
    x20 - x23)^2) + 10) * (exp(-10 * sqrt((x2 - x5)^2 + (x11 - x14)^2 + (x20 -
    x23)^2) + 10) - 2) + exp(-10 * sqrt((x2 - x6)^2 + (x11 - x15)^2 + (x20 -
    x24)^2) + 10) * (exp(-10 * sqrt((x2 - x6)^2 + (x11 - x15)^2 + (x20 - x24)^2)
    + 10) - 2) + exp(-10 * sqrt((x2 - x7)^2 + (x11 - x16)^2 + (x20 - x25)^2)
    + 10) * (exp(-10 * sqrt((x2 - x7)^2 + (x11 - x16)^2 + (x20 - x25)^2) + 10)
    - 2) + exp(-10 * sqrt((x2 - x8)^2 + (x11 - x17)^2 + (x20 - x26)^2) + 10)
    * (exp(-10 * sqrt((x2 - x8)^2 + (x11 - x17)^2 + (x20 - x26)^2) + 10) - 2)
    + exp(-10 * sqrt((x2 - x9)^2 + (x11 - x18)^2 + (x20 - x27)^2) + 10) * (exp
    (-10 * sqrt((x2 - x9)^2 + (x11 - x18)^2 + (x20 - x27)^2) + 10) - 2) + exp(-
    10 * sqrt((x3 - x4)^2 + (x12 - x13)^2 + (x21 - x22)^2) + 10) * (exp(-10 *
    sqrt((x3 - x4)^2 + (x12 - x13)^2 + (x21 - x22)^2) + 10) - 2) + exp(-10 *
    sqrt((x3 - x5)^2 + (x12 - x14)^2 + (x21 - x23)^2) + 10) * (exp(-10 * sqrt((
    x3 - x5)^2 + (x12 - x14)^2 + (x21 - x23)^2) + 10) - 2) + exp(-10 * sqrt((x3
    - x6)^2 + (x12 - x15)^2 + (x21 - x24)^2) + 10) * (exp(-10 * sqrt((x3 - x6)
    ^2 + (x12 - x15)^2 + (x21 - x24)^2) + 10) - 2) + exp(-10 * sqrt((x3 - x7)^2
    + (x12 - x16)^2 + (x21 - x25)^2) + 10) * (exp(-10 * sqrt((x3 - x7)^2 + (
    x12 - x16)^2 + (x21 - x25)^2) + 10) - 2) + exp(-10 * sqrt((x3 - x8)^2 + (
    x12 - x17)^2 + (x21 - x26)^2) + 10) * (exp(-10 * sqrt((x3 - x8)^2 + (x12 -
    x17)^2 + (x21 - x26)^2) + 10) - 2) + exp(-10 * sqrt((x3 - x9)^2 + (x12 -
    x18)^2 + (x21 - x27)^2) + 10) * (exp(-10 * sqrt((x3 - x9)^2 + (x12 - x18)^2
    + (x21 - x27)^2) + 10) - 2) + exp(-10 * sqrt((x4 - x5)^2 + (x13 - x14)^2
    + (x22 - x23)^2) + 10) * (exp(-10 * sqrt((x4 - x5)^2 + (x13 - x14)^2 + (
    x22 - x23)^2) + 10) - 2) + exp(-10 * sqrt((x4 - x6)^2 + (x13 - x15)^2 + (
    x22 - x24)^2) + 10) * (exp(-10 * sqrt((x4 - x6)^2 + (x13 - x15)^2 + (x22 -
    x24)^2) + 10) - 2) + exp(-10 * sqrt((x4 - x7)^2 + (x13 - x16)^2 + (x22 -
    x25)^2) + 10) * (exp(-10 * sqrt((x4 - x7)^2 + (x13 - x16)^2 + (x22 - x25)^2)
    + 10) - 2) + exp(-10 * sqrt((x4 - x8)^2 + (x13 - x17)^2 + (x22 - x26)^2)
    + 10) * (exp(-10 * sqrt((x4 - x8)^2 + (x13 - x17)^2 + (x22 - x26)^2) + 10)
    - 2) + exp(-10 * sqrt((x4 - x9)^2 + (x13 - x18)^2 + (x22 - x27)^2) + 10)
    * (exp(-10 * sqrt((x4 - x9)^2 + (x13 - x18)^2 + (x22 - x27)^2) + 10) - 2)
    + exp(-10 * sqrt((x5 - x6)^2 + (x14 - x15)^2 + (x23 - x24)^2) + 10) * (exp
    (-10 * sqrt((x5 - x6)^2 + (x14 - x15)^2 + (x23 - x24)^2) + 10) - 2) + exp(-
    10 * sqrt((x5 - x7)^2 + (x14 - x16)^2 + (x23 - x25)^2) + 10) * (exp(-10 *
    sqrt((x5 - x7)^2 + (x14 - x16)^2 + (x23 - x25)^2) + 10) - 2) + exp(-10 *
    sqrt((x5 - x8)^2 + (x14 - x17)^2 + (x23 - x26)^2) + 10) * (exp(-10 * sqrt((
    x5 - x8)^2 + (x14 - x17)^2 + (x23 - x26)^2) + 10) - 2) + exp(-10 * sqrt((x5
    - x9)^2 + (x14 - x18)^2 + (x23 - x27)^2) + 10) * (exp(-10 * sqrt((x5 - x9)
    ^2 + (x14 - x18)^2 + (x23 - x27)^2) + 10) - 2) + exp(-10 * sqrt((x6 - x7)^2
    + (x15 - x16)^2 + (x24 - x25)^2) + 10) * (exp(-10 * sqrt((x6 - x7)^2 + (
    x15 - x16)^2 + (x24 - x25)^2) + 10) - 2) + exp(-10 * sqrt((x6 - x8)^2 + (
    x15 - x17)^2 + (x24 - x26)^2) + 10) * (exp(-10 * sqrt((x6 - x8)^2 + (x15 -
    x17)^2 + (x24 - x26)^2) + 10) - 2) + exp(-10 * sqrt((x6 - x9)^2 + (x15 -
    x18)^2 + (x24 - x27)^2) + 10) * (exp(-10 * sqrt((x6 - x9)^2 + (x15 - x18)^2
    + (x24 - x27)^2) + 10) - 2) + exp(-10 * sqrt((x7 - x8)^2 + (x16 - x17)^2
    + (x25 - x26)^2) + 10) * (exp(-10 * sqrt((x7 - x8)^2 + (x16 - x17)^2 + (
    x25 - x26)^2) + 10) - 2) + exp(-10 * sqrt((x7 - x9)^2 + (x16 - x18)^2 + (
    x25 - x27)^2) + 10) * (exp(-10 * sqrt((x7 - x9)^2 + (x16 - x18)^2 + (x25 -
    x27)^2) + 10) - 2) + exp(-10 * sqrt((x8 - x9)^2 + (x17 - x18)^2 + (x26 -
    x27)^2) + 10) * (exp(-10 * sqrt((x8 - x9)^2 + (x17 - x18)^2 + (x26 - x27)^2)
    + 10) - 2))

@NLconstraint(m, e1, (x1 - x2)^2 + (x10 - x11)^2 + (x19 - x20)^2
    >= 0.6144835321)
@NLconstraint(m, e2, (x1 - x3)^2 + (x10 - x12)^2 + (x19 - x21)^2
    >= 0.6144835321)
@NLconstraint(m, e3, (x1 - x4)^2 + (x10 - x13)^2 + (x19 - x22)^2
    >= 0.6144835321)
@NLconstraint(m, e4, (x1 - x5)^2 + (x10 - x14)^2 + (x19 - x23)^2
    >= 0.6144835321)
@NLconstraint(m, e5, (x1 - x6)^2 + (x10 - x15)^2 + (x19 - x24)^2
    >= 0.6144835321)
@NLconstraint(m, e6, (x1 - x7)^2 + (x10 - x16)^2 + (x19 - x25)^2
    >= 0.6144835321)
@NLconstraint(m, e7, (x1 - x8)^2 + (x10 - x17)^2 + (x19 - x26)^2
    >= 0.6144835321)
@NLconstraint(m, e8, (x1 - x9)^2 + (x10 - x18)^2 + (x19 - x27)^2
    >= 0.6144835321)
@NLconstraint(m, e9, (x2 - x3)^2 + (x11 - x12)^2 + (x20 - x21)^2
    >= 0.6144835321)
@NLconstraint(m, e10, (x2 - x4)^2 + (x11 - x13)^2 + (x20 - x22)^2
    >= 0.6144835321)
@NLconstraint(m, e11, (x2 - x5)^2 + (x11 - x14)^2 + (x20 - x23)^2
    >= 0.6144835321)
@NLconstraint(m, e12, (x2 - x6)^2 + (x11 - x15)^2 + (x20 - x24)^2
    >= 0.6144835321)
@NLconstraint(m, e13, (x2 - x7)^2 + (x11 - x16)^2 + (x20 - x25)^2
    >= 0.6144835321)
@NLconstraint(m, e14, (x2 - x8)^2 + (x11 - x17)^2 + (x20 - x26)^2
    >= 0.6144835321)
@NLconstraint(m, e15, (x2 - x9)^2 + (x11 - x18)^2 + (x20 - x27)^2
    >= 0.6144835321)
@NLconstraint(m, e16, (x3 - x4)^2 + (x12 - x13)^2 + (x21 - x22)^2
    >= 0.6144835321)
@NLconstraint(m, e17, (x3 - x5)^2 + (x12 - x14)^2 + (x21 - x23)^2
    >= 0.6144835321)
@NLconstraint(m, e18, (x3 - x6)^2 + (x12 - x15)^2 + (x21 - x24)^2
    >= 0.6144835321)
@NLconstraint(m, e19, (x3 - x7)^2 + (x12 - x16)^2 + (x21 - x25)^2
    >= 0.6144835321)
@NLconstraint(m, e20, (x3 - x8)^2 + (x12 - x17)^2 + (x21 - x26)^2
    >= 0.6144835321)
@NLconstraint(m, e21, (x3 - x9)^2 + (x12 - x18)^2 + (x21 - x27)^2
    >= 0.6144835321)
@NLconstraint(m, e22, (x4 - x5)^2 + (x13 - x14)^2 + (x22 - x23)^2
    >= 0.6144835321)
@NLconstraint(m, e23, (x4 - x6)^2 + (x13 - x15)^2 + (x22 - x24)^2
    >= 0.6144835321)
@NLconstraint(m, e24, (x4 - x7)^2 + (x13 - x16)^2 + (x22 - x25)^2
    >= 0.6144835321)
@NLconstraint(m, e25, (x4 - x8)^2 + (x13 - x17)^2 + (x22 - x26)^2
    >= 0.6144835321)
@NLconstraint(m, e26, (x4 - x9)^2 + (x13 - x18)^2 + (x22 - x27)^2
    >= 0.6144835321)
@NLconstraint(m, e27, (x5 - x6)^2 + (x14 - x15)^2 + (x23 - x24)^2
    >= 0.6144835321)
@NLconstraint(m, e28, (x5 - x7)^2 + (x14 - x16)^2 + (x23 - x25)^2
    >= 0.6144835321)
@NLconstraint(m, e29, (x5 - x8)^2 + (x14 - x17)^2 + (x23 - x26)^2
    >= 0.6144835321)
@NLconstraint(m, e30, (x5 - x9)^2 + (x14 - x18)^2 + (x23 - x27)^2
    >= 0.6144835321)
@NLconstraint(m, e31, (x6 - x7)^2 + (x15 - x16)^2 + (x24 - x25)^2
    >= 0.6144835321)
@NLconstraint(m, e32, (x6 - x8)^2 + (x15 - x17)^2 + (x24 - x26)^2
    >= 0.6144835321)
@NLconstraint(m, e33, (x6 - x9)^2 + (x15 - x18)^2 + (x24 - x27)^2
    >= 0.6144835321)
@NLconstraint(m, e34, (x7 - x8)^2 + (x16 - x17)^2 + (x25 - x26)^2
    >= 0.6144835321)
@NLconstraint(m, e35, (x7 - x9)^2 + (x16 - x18)^2 + (x25 - x27)^2
    >= 0.6144835321)
@NLconstraint(m, e36, (x8 - x9)^2 + (x17 - x18)^2 + (x26 - x27)^2
    >= 0.6144835321)
