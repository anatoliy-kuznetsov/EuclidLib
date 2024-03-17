# NLP written by GAMS Convert at 03/17/24 14:47:54
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#        54        0       45        9        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        30       30        0        0        0        0        0        0
# FX      6
#
# Nonzero counts
#     Total    const       NL
#       288       18      270
#
# Reformulation has removed 1 variable and 1 equation

using JuMP
using MathOptInterface
const MOI = MathOptInterface

model = m = Model()

@variable(m, 0 <= x1 <= 0, start=0)
@variable(m, 0 <= x2 <= 0, start=0)
@variable(m, 0 <= x3 <= 0, start=0)
@variable(m, 0 <= x4 <= 9, start=0)
@variable(m, 0 <= x5 <= 9, start=0)
@variable(m, 0 <= x6 <= 9, start=0)
@variable(m, 0 <= x7 <= 9, start=0)
@variable(m, 0 <= x8 <= 9, start=0)
@variable(m, 0 <= x9 <= 9, start=0)
@variable(m, 0 <= x10 <= 9, start=0)
@variable(m, 0 <= x11 <= 0, start=0)
@variable(m, 0 <= x12 <= 0, start=0)
@variable(m, -9 <= x13 <= 9, start=0)
@variable(m, -9 <= x14 <= 9, start=0)
@variable(m, -9 <= x15 <= 9, start=0)
@variable(m, -9 <= x16 <= 9, start=0)
@variable(m, -9 <= x17 <= 9, start=0)
@variable(m, -9 <= x18 <= 9, start=0)
@variable(m, -9 <= x19 <= 9, start=0)
@variable(m, -9 <= x20 <= 9, start=0)
@variable(m, 0 <= x21 <= 0, start=0)
@variable(m, -9 <= x22 <= 9, start=0)
@variable(m, -9 <= x23 <= 9, start=0)
@variable(m, -9 <= x24 <= 9, start=0)
@variable(m, -9 <= x25 <= 9, start=0)
@variable(m, -9 <= x26 <= 9, start=0)
@variable(m, -9 <= x27 <= 9, start=0)
@variable(m, -9 <= x28 <= 9, start=0)
@variable(m, -9 <= x29 <= 9, start=0)
@variable(m, -9 <= x30 <= 9, start=0)

@NLobjective(m, Min, exp(-6 * sqrt((x1 - x2)^2 + (x11 - x12)^2 + (x21 - x22)^2)
    + 6) * (exp(-6 * sqrt((x1 - x2)^2 + (x11 - x12)^2 + (x21 - x22)^2) + 6) -
    2) + exp(-6 * sqrt((x1 - x3)^2 + (x11 - x13)^2 + (x21 - x23)^2) + 6) * (exp
    (-6 * sqrt((x1 - x3)^2 + (x11 - x13)^2 + (x21 - x23)^2) + 6) - 2) + exp(-6
    * sqrt((x1 - x4)^2 + (x11 - x14)^2 + (x21 - x24)^2) + 6) * (exp(-6 * sqrt(
    (x1 - x4)^2 + (x11 - x14)^2 + (x21 - x24)^2) + 6) - 2) + exp(-6 * sqrt((x1
    - x5)^2 + (x11 - x15)^2 + (x21 - x25)^2) + 6) * (exp(-6 * sqrt((x1 - x5)^2
    + (x11 - x15)^2 + (x21 - x25)^2) + 6) - 2) + exp(-6 * sqrt((x1 - x6)^2 + (
    x11 - x16)^2 + (x21 - x26)^2) + 6) * (exp(-6 * sqrt((x1 - x6)^2 + (x11 -
    x16)^2 + (x21 - x26)^2) + 6) - 2) + exp(-6 * sqrt((x1 - x7)^2 + (x11 - x17)
    ^2 + (x21 - x27)^2) + 6) * (exp(-6 * sqrt((x1 - x7)^2 + (x11 - x17)^2 + (
    x21 - x27)^2) + 6) - 2) + exp(-6 * sqrt((x1 - x8)^2 + (x11 - x18)^2 + (x21
    - x28)^2) + 6) * (exp(-6 * sqrt((x1 - x8)^2 + (x11 - x18)^2 + (x21 - x28)^
    2) + 6) - 2) + exp(-6 * sqrt((x1 - x9)^2 + (x11 - x19)^2 + (x21 - x29)^2)
    + 6) * (exp(-6 * sqrt((x1 - x9)^2 + (x11 - x19)^2 + (x21 - x29)^2) + 6) -
    2) + exp(-6 * sqrt((x1 - x10)^2 + (x11 - x20)^2 + (x21 - x30)^2) + 6) * (
    exp(-6 * sqrt((x1 - x10)^2 + (x11 - x20)^2 + (x21 - x30)^2) + 6) - 2) + exp
    (-6 * sqrt((x2 - x3)^2 + (x12 - x13)^2 + (x22 - x23)^2) + 6) * (exp(-6 *
    sqrt((x2 - x3)^2 + (x12 - x13)^2 + (x22 - x23)^2) + 6) - 2) + exp(-6 * sqrt
    ((x2 - x4)^2 + (x12 - x14)^2 + (x22 - x24)^2) + 6) * (exp(-6 * sqrt((x2 -
    x4)^2 + (x12 - x14)^2 + (x22 - x24)^2) + 6) - 2) + exp(-6 * sqrt((x2 - x5)^
    2 + (x12 - x15)^2 + (x22 - x25)^2) + 6) * (exp(-6 * sqrt((x2 - x5)^2 + (x12
    - x15)^2 + (x22 - x25)^2) + 6) - 2) + exp(-6 * sqrt((x2 - x6)^2 + (x12 -
    x16)^2 + (x22 - x26)^2) + 6) * (exp(-6 * sqrt((x2 - x6)^2 + (x12 - x16)^2
    + (x22 - x26)^2) + 6) - 2) + exp(-6 * sqrt((x2 - x7)^2 + (x12 - x17)^2 + (
    x22 - x27)^2) + 6) * (exp(-6 * sqrt((x2 - x7)^2 + (x12 - x17)^2 + (x22 -
    x27)^2) + 6) - 2) + exp(-6 * sqrt((x2 - x8)^2 + (x12 - x18)^2 + (x22 - x28)
    ^2) + 6) * (exp(-6 * sqrt((x2 - x8)^2 + (x12 - x18)^2 + (x22 - x28)^2) + 6)
    - 2) + exp(-6 * sqrt((x2 - x9)^2 + (x12 - x19)^2 + (x22 - x29)^2) + 6) * (
    exp(-6 * sqrt((x2 - x9)^2 + (x12 - x19)^2 + (x22 - x29)^2) + 6) - 2) + exp(
    -6 * sqrt((x2 - x10)^2 + (x12 - x20)^2 + (x22 - x30)^2) + 6) * (exp(-6 *
    sqrt((x2 - x10)^2 + (x12 - x20)^2 + (x22 - x30)^2) + 6) - 2) + exp(-6 *
    sqrt((x3 - x4)^2 + (x13 - x14)^2 + (x23 - x24)^2) + 6) * (exp(-6 * sqrt((x3
    - x4)^2 + (x13 - x14)^2 + (x23 - x24)^2) + 6) - 2) + exp(-6 * sqrt((x3 -
    x5)^2 + (x13 - x15)^2 + (x23 - x25)^2) + 6) * (exp(-6 * sqrt((x3 - x5)^2 +
    (x13 - x15)^2 + (x23 - x25)^2) + 6) - 2) + exp(-6 * sqrt((x3 - x6)^2 + (x13
    - x16)^2 + (x23 - x26)^2) + 6) * (exp(-6 * sqrt((x3 - x6)^2 + (x13 - x16)^
    2 + (x23 - x26)^2) + 6) - 2) + exp(-6 * sqrt((x3 - x7)^2 + (x13 - x17)^2 +
    (x23 - x27)^2) + 6) * (exp(-6 * sqrt((x3 - x7)^2 + (x13 - x17)^2 + (x23 -
    x27)^2) + 6) - 2) + exp(-6 * sqrt((x3 - x8)^2 + (x13 - x18)^2 + (x23 - x28)
    ^2) + 6) * (exp(-6 * sqrt((x3 - x8)^2 + (x13 - x18)^2 + (x23 - x28)^2) + 6)
    - 2) + exp(-6 * sqrt((x3 - x9)^2 + (x13 - x19)^2 + (x23 - x29)^2) + 6) * (
    exp(-6 * sqrt((x3 - x9)^2 + (x13 - x19)^2 + (x23 - x29)^2) + 6) - 2) + exp(
    -6 * sqrt((x3 - x10)^2 + (x13 - x20)^2 + (x23 - x30)^2) + 6) * (exp(-6 *
    sqrt((x3 - x10)^2 + (x13 - x20)^2 + (x23 - x30)^2) + 6) - 2) + exp(-6 *
    sqrt((x4 - x5)^2 + (x14 - x15)^2 + (x24 - x25)^2) + 6) * (exp(-6 * sqrt((x4
    - x5)^2 + (x14 - x15)^2 + (x24 - x25)^2) + 6) - 2) + exp(-6 * sqrt((x4 -
    x6)^2 + (x14 - x16)^2 + (x24 - x26)^2) + 6) * (exp(-6 * sqrt((x4 - x6)^2 +
    (x14 - x16)^2 + (x24 - x26)^2) + 6) - 2) + exp(-6 * sqrt((x4 - x7)^2 + (x14
    - x17)^2 + (x24 - x27)^2) + 6) * (exp(-6 * sqrt((x4 - x7)^2 + (x14 - x17)^
    2 + (x24 - x27)^2) + 6) - 2) + exp(-6 * sqrt((x4 - x8)^2 + (x14 - x18)^2 +
    (x24 - x28)^2) + 6) * (exp(-6 * sqrt((x4 - x8)^2 + (x14 - x18)^2 + (x24 -
    x28)^2) + 6) - 2) + exp(-6 * sqrt((x4 - x9)^2 + (x14 - x19)^2 + (x24 - x29)
    ^2) + 6) * (exp(-6 * sqrt((x4 - x9)^2 + (x14 - x19)^2 + (x24 - x29)^2) + 6)
    - 2) + exp(-6 * sqrt((x4 - x10)^2 + (x14 - x20)^2 + (x24 - x30)^2) + 6) *
    (exp(-6 * sqrt((x4 - x10)^2 + (x14 - x20)^2 + (x24 - x30)^2) + 6) - 2) +
    exp(-6 * sqrt((x5 - x6)^2 + (x15 - x16)^2 + (x25 - x26)^2) + 6) * (exp(-6
    * sqrt((x5 - x6)^2 + (x15 - x16)^2 + (x25 - x26)^2) + 6) - 2) + exp(-6 *
    sqrt((x5 - x7)^2 + (x15 - x17)^2 + (x25 - x27)^2) + 6) * (exp(-6 * sqrt((x5
    - x7)^2 + (x15 - x17)^2 + (x25 - x27)^2) + 6) - 2) + exp(-6 * sqrt((x5 -
    x8)^2 + (x15 - x18)^2 + (x25 - x28)^2) + 6) * (exp(-6 * sqrt((x5 - x8)^2 +
    (x15 - x18)^2 + (x25 - x28)^2) + 6) - 2) + exp(-6 * sqrt((x5 - x9)^2 + (x15
    - x19)^2 + (x25 - x29)^2) + 6) * (exp(-6 * sqrt((x5 - x9)^2 + (x15 - x19)^
    2 + (x25 - x29)^2) + 6) - 2) + exp(-6 * sqrt((x5 - x10)^2 + (x15 - x20)^2
    + (x25 - x30)^2) + 6) * (exp(-6 * sqrt((x5 - x10)^2 + (x15 - x20)^2 + (x25
    - x30)^2) + 6) - 2) + exp(-6 * sqrt((x6 - x7)^2 + (x16 - x17)^2 + (x26 -
    x27)^2) + 6) * (exp(-6 * sqrt((x6 - x7)^2 + (x16 - x17)^2 + (x26 - x27)^2)
    + 6) - 2) + exp(-6 * sqrt((x6 - x8)^2 + (x16 - x18)^2 + (x26 - x28)^2) + 6)
    * (exp(-6 * sqrt((x6 - x8)^2 + (x16 - x18)^2 + (x26 - x28)^2) + 6) - 2) +
    exp(-6 * sqrt((x6 - x9)^2 + (x16 - x19)^2 + (x26 - x29)^2) + 6) * (exp(-6
    * sqrt((x6 - x9)^2 + (x16 - x19)^2 + (x26 - x29)^2) + 6) - 2) + exp(-6 *
    sqrt((x6 - x10)^2 + (x16 - x20)^2 + (x26 - x30)^2) + 6) * (exp(-6 * sqrt((
    x6 - x10)^2 + (x16 - x20)^2 + (x26 - x30)^2) + 6) - 2) + exp(-6 * sqrt((x7
    - x8)^2 + (x17 - x18)^2 + (x27 - x28)^2) + 6) * (exp(-6 * sqrt((x7 - x8)^2
    + (x17 - x18)^2 + (x27 - x28)^2) + 6) - 2) + exp(-6 * sqrt((x7 - x9)^2 + (
    x17 - x19)^2 + (x27 - x29)^2) + 6) * (exp(-6 * sqrt((x7 - x9)^2 + (x17 -
    x19)^2 + (x27 - x29)^2) + 6) - 2) + exp(-6 * sqrt((x7 - x10)^2 + (x17 - x20)
    ^2 + (x27 - x30)^2) + 6) * (exp(-6 * sqrt((x7 - x10)^2 + (x17 - x20)^2 + (
    x27 - x30)^2) + 6) - 2) + exp(-6 * sqrt((x8 - x9)^2 + (x18 - x19)^2 + (x28
    - x29)^2) + 6) * (exp(-6 * sqrt((x8 - x9)^2 + (x18 - x19)^2 + (x28 - x29)^
    2) + 6) - 2) + exp(-6 * sqrt((x8 - x10)^2 + (x18 - x20)^2 + (x28 - x30)^2)
    + 6) * (exp(-6 * sqrt((x8 - x10)^2 + (x18 - x20)^2 + (x28 - x30)^2) + 6)
    - 2) + exp(-6 * sqrt((x9 - x10)^2 + (x19 - x20)^2 + (x29 - x30)^2) + 6) *
    (exp(-6 * sqrt((x9 - x10)^2 + (x19 - x20)^2 + (x29 - x30)^2) + 6) - 2))

@NLconstraint(m, e1, (x1 - x2)^2 + (x11 - x12)^2 + (x21 - x22)^2
    >= 0.32159900740899994)
@NLconstraint(m, e2, (x1 - x3)^2 + (x11 - x13)^2 + (x21 - x23)^2
    >= 0.32159900740899994)
@NLconstraint(m, e3, (x1 - x4)^2 + (x11 - x14)^2 + (x21 - x24)^2
    >= 0.32159900740899994)
@NLconstraint(m, e4, (x1 - x5)^2 + (x11 - x15)^2 + (x21 - x25)^2
    >= 0.32159900740899994)
@NLconstraint(m, e5, (x1 - x6)^2 + (x11 - x16)^2 + (x21 - x26)^2
    >= 0.32159900740899994)
@NLconstraint(m, e6, (x1 - x7)^2 + (x11 - x17)^2 + (x21 - x27)^2
    >= 0.32159900740899994)
@NLconstraint(m, e7, (x1 - x8)^2 + (x11 - x18)^2 + (x21 - x28)^2
    >= 0.32159900740899994)
@NLconstraint(m, e8, (x1 - x9)^2 + (x11 - x19)^2 + (x21 - x29)^2
    >= 0.32159900740899994)
@NLconstraint(m, e9, (x1 - x10)^2 + (x11 - x20)^2 + (x21 - x30)^2
    >= 0.32159900740899994)
@NLconstraint(m, e10, (x2 - x3)^2 + (x12 - x13)^2 + (x22 - x23)^2
    >= 0.32159900740899994)
@NLconstraint(m, e11, (x2 - x4)^2 + (x12 - x14)^2 + (x22 - x24)^2
    >= 0.32159900740899994)
@NLconstraint(m, e12, (x2 - x5)^2 + (x12 - x15)^2 + (x22 - x25)^2
    >= 0.32159900740899994)
@NLconstraint(m, e13, (x2 - x6)^2 + (x12 - x16)^2 + (x22 - x26)^2
    >= 0.32159900740899994)
@NLconstraint(m, e14, (x2 - x7)^2 + (x12 - x17)^2 + (x22 - x27)^2
    >= 0.32159900740899994)
@NLconstraint(m, e15, (x2 - x8)^2 + (x12 - x18)^2 + (x22 - x28)^2
    >= 0.32159900740899994)
@NLconstraint(m, e16, (x2 - x9)^2 + (x12 - x19)^2 + (x22 - x29)^2
    >= 0.32159900740899994)
@NLconstraint(m, e17, (x2 - x10)^2 + (x12 - x20)^2 + (x22 - x30)^2
    >= 0.32159900740899994)
@NLconstraint(m, e18, (x3 - x4)^2 + (x13 - x14)^2 + (x23 - x24)^2
    >= 0.32159900740899994)
@NLconstraint(m, e19, (x3 - x5)^2 + (x13 - x15)^2 + (x23 - x25)^2
    >= 0.32159900740899994)
@NLconstraint(m, e20, (x3 - x6)^2 + (x13 - x16)^2 + (x23 - x26)^2
    >= 0.32159900740899994)
@NLconstraint(m, e21, (x3 - x7)^2 + (x13 - x17)^2 + (x23 - x27)^2
    >= 0.32159900740899994)
@NLconstraint(m, e22, (x3 - x8)^2 + (x13 - x18)^2 + (x23 - x28)^2
    >= 0.32159900740899994)
@NLconstraint(m, e23, (x3 - x9)^2 + (x13 - x19)^2 + (x23 - x29)^2
    >= 0.32159900740899994)
@NLconstraint(m, e24, (x3 - x10)^2 + (x13 - x20)^2 + (x23 - x30)^2
    >= 0.32159900740899994)
@NLconstraint(m, e25, (x4 - x5)^2 + (x14 - x15)^2 + (x24 - x25)^2
    >= 0.32159900740899994)
@NLconstraint(m, e26, (x4 - x6)^2 + (x14 - x16)^2 + (x24 - x26)^2
    >= 0.32159900740899994)
@NLconstraint(m, e27, (x4 - x7)^2 + (x14 - x17)^2 + (x24 - x27)^2
    >= 0.32159900740899994)
@NLconstraint(m, e28, (x4 - x8)^2 + (x14 - x18)^2 + (x24 - x28)^2
    >= 0.32159900740899994)
@NLconstraint(m, e29, (x4 - x9)^2 + (x14 - x19)^2 + (x24 - x29)^2
    >= 0.32159900740899994)
@NLconstraint(m, e30, (x4 - x10)^2 + (x14 - x20)^2 + (x24 - x30)^2
    >= 0.32159900740899994)
@NLconstraint(m, e31, (x5 - x6)^2 + (x15 - x16)^2 + (x25 - x26)^2
    >= 0.32159900740899994)
@NLconstraint(m, e32, (x5 - x7)^2 + (x15 - x17)^2 + (x25 - x27)^2
    >= 0.32159900740899994)
@NLconstraint(m, e33, (x5 - x8)^2 + (x15 - x18)^2 + (x25 - x28)^2
    >= 0.32159900740899994)
@NLconstraint(m, e34, (x5 - x9)^2 + (x15 - x19)^2 + (x25 - x29)^2
    >= 0.32159900740899994)
@NLconstraint(m, e35, (x5 - x10)^2 + (x15 - x20)^2 + (x25 - x30)^2
    >= 0.32159900740899994)
@NLconstraint(m, e36, (x6 - x7)^2 + (x16 - x17)^2 + (x26 - x27)^2
    >= 0.32159900740899994)
@NLconstraint(m, e37, (x6 - x8)^2 + (x16 - x18)^2 + (x26 - x28)^2
    >= 0.32159900740899994)
@NLconstraint(m, e38, (x6 - x9)^2 + (x16 - x19)^2 + (x26 - x29)^2
    >= 0.32159900740899994)
@NLconstraint(m, e39, (x6 - x10)^2 + (x16 - x20)^2 + (x26 - x30)^2
    >= 0.32159900740899994)
@NLconstraint(m, e40, (x7 - x8)^2 + (x17 - x18)^2 + (x27 - x28)^2
    >= 0.32159900740899994)
@NLconstraint(m, e41, (x7 - x9)^2 + (x17 - x19)^2 + (x27 - x29)^2
    >= 0.32159900740899994)
@NLconstraint(m, e42, (x7 - x10)^2 + (x17 - x20)^2 + (x27 - x30)^2
    >= 0.32159900740899994)
@NLconstraint(m, e43, (x8 - x9)^2 + (x18 - x19)^2 + (x28 - x29)^2
    >= 0.32159900740899994)
@NLconstraint(m, e44, (x8 - x10)^2 + (x18 - x20)^2 + (x28 - x30)^2
    >= 0.32159900740899994)
@NLconstraint(m, e45, (x9 - x10)^2 + (x19 - x20)^2 + (x29 - x30)^2
    >= 0.32159900740899994)
@constraint(m, e46, x1 - x2 <= 0)
@constraint(m, e47, x2 - x3 <= 0)
@constraint(m, e48, x3 - x4 <= 0)
@constraint(m, e49, x4 - x5 <= 0)
@constraint(m, e50, x5 - x6 <= 0)
@constraint(m, e51, x6 - x7 <= 0)
@constraint(m, e52, x7 - x8 <= 0)
@constraint(m, e53, x8 - x9 <= 0)
@constraint(m, e54, x9 - x10 <= 0)
