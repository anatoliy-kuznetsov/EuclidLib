# NLP written by GAMS Convert at 03/17/24 14:47:57
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#        20        0       15        5        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        18       18        0        0        0        0        0        0
# FX      6
#
# Nonzero counts
#     Total    const       NL
#       100       10       90
#
# Reformulation has removed 1 variable and 1 equation

using JuMP
using MathOptInterface
const MOI = MathOptInterface

model = m = Model()

@variable(m, 0 <= x1 <= 0, start=0)
@variable(m, 0 <= x2 <= 0, start=0)
@variable(m, 0 <= x3 <= 0, start=0)
@variable(m, 0 <= x4 <= 5, start=0)
@variable(m, 0 <= x5 <= 5, start=0)
@variable(m, 0 <= x6 <= 5, start=0)
@variable(m, 0 <= x7 <= 0, start=0)
@variable(m, 0 <= x8 <= 0, start=0)
@variable(m, -5 <= x9 <= 5, start=0)
@variable(m, -5 <= x10 <= 5, start=0)
@variable(m, -5 <= x11 <= 5, start=0)
@variable(m, -5 <= x12 <= 5, start=0)
@variable(m, 0 <= x13 <= 0, start=0)
@variable(m, -5 <= x14 <= 5, start=0)
@variable(m, -5 <= x15 <= 5, start=0)
@variable(m, -5 <= x16 <= 5, start=0)
@variable(m, -5 <= x17 <= 5, start=0)
@variable(m, -5 <= x18 <= 5, start=0)

@NLobjective(m, Min, exp(-10 * sqrt((x1 - x2)^2 + (x7 - x8)^2 + (x13 - x14)^2)
    + 10) * (exp(-10 * sqrt((x1 - x2)^2 + (x7 - x8)^2 + (x13 - x14)^2) + 10)
    - 2) + exp(-10 * sqrt((x1 - x3)^2 + (x7 - x9)^2 + (x13 - x15)^2) + 10) * (
    exp(-10 * sqrt((x1 - x3)^2 + (x7 - x9)^2 + (x13 - x15)^2) + 10) - 2) + exp(
    -10 * sqrt((x1 - x4)^2 + (x7 - x10)^2 + (x13 - x16)^2) + 10) * (exp(-10 *
    sqrt((x1 - x4)^2 + (x7 - x10)^2 + (x13 - x16)^2) + 10) - 2) + exp(-10 *
    sqrt((x1 - x5)^2 + (x7 - x11)^2 + (x13 - x17)^2) + 10) * (exp(-10 * sqrt((
    x1 - x5)^2 + (x7 - x11)^2 + (x13 - x17)^2) + 10) - 2) + exp(-10 * sqrt((x1
    - x6)^2 + (x7 - x12)^2 + (x13 - x18)^2) + 10) * (exp(-10 * sqrt((x1 - x6)^
    2 + (x7 - x12)^2 + (x13 - x18)^2) + 10) - 2) + exp(-10 * sqrt((x2 - x3)^2
    + (x8 - x9)^2 + (x14 - x15)^2) + 10) * (exp(-10 * sqrt((x2 - x3)^2 + (x8
    - x9)^2 + (x14 - x15)^2) + 10) - 2) + exp(-10 * sqrt((x2 - x4)^2 + (x8 -
    x10)^2 + (x14 - x16)^2) + 10) * (exp(-10 * sqrt((x2 - x4)^2 + (x8 - x10)^2
    + (x14 - x16)^2) + 10) - 2) + exp(-10 * sqrt((x2 - x5)^2 + (x8 - x11)^2 +
    (x14 - x17)^2) + 10) * (exp(-10 * sqrt((x2 - x5)^2 + (x8 - x11)^2 + (x14 -
    x17)^2) + 10) - 2) + exp(-10 * sqrt((x2 - x6)^2 + (x8 - x12)^2 + (x14 - x18)
    ^2) + 10) * (exp(-10 * sqrt((x2 - x6)^2 + (x8 - x12)^2 + (x14 - x18)^2) +
    10) - 2) + exp(-10 * sqrt((x3 - x4)^2 + (x9 - x10)^2 + (x15 - x16)^2) + 10)
    * (exp(-10 * sqrt((x3 - x4)^2 + (x9 - x10)^2 + (x15 - x16)^2) + 10) - 2)
    + exp(-10 * sqrt((x3 - x5)^2 + (x9 - x11)^2 + (x15 - x17)^2) + 10) * (exp(
    -10 * sqrt((x3 - x5)^2 + (x9 - x11)^2 + (x15 - x17)^2) + 10) - 2) + exp(-10
    * sqrt((x3 - x6)^2 + (x9 - x12)^2 + (x15 - x18)^2) + 10) * (exp(-10 * sqrt
    ((x3 - x6)^2 + (x9 - x12)^2 + (x15 - x18)^2) + 10) - 2) + exp(-10 * sqrt((
    x4 - x5)^2 + (x10 - x11)^2 + (x16 - x17)^2) + 10) * (exp(-10 * sqrt((x4 -
    x5)^2 + (x10 - x11)^2 + (x16 - x17)^2) + 10) - 2) + exp(-10 * sqrt((x4 - x6)
    ^2 + (x10 - x12)^2 + (x16 - x18)^2) + 10) * (exp(-10 * sqrt((x4 - x6)^2 + (
    x10 - x12)^2 + (x16 - x18)^2) + 10) - 2) + exp(-10 * sqrt((x5 - x6)^2 + (
    x11 - x12)^2 + (x17 - x18)^2) + 10) * (exp(-10 * sqrt((x5 - x6)^2 + (x11 -
    x12)^2 + (x17 - x18)^2) + 10) - 2))

@NLconstraint(m, e1, (x1 - x2)^2 + (x7 - x8)^2 + (x13 - x14)^2 >= 0.6144835321)
@NLconstraint(m, e2, (x1 - x3)^2 + (x7 - x9)^2 + (x13 - x15)^2 >= 0.6144835321)
@NLconstraint(m, e3, (x1 - x4)^2 + (x7 - x10)^2 + (x13 - x16)^2
    >= 0.6144835321)
@NLconstraint(m, e4, (x1 - x5)^2 + (x7 - x11)^2 + (x13 - x17)^2
    >= 0.6144835321)
@NLconstraint(m, e5, (x1 - x6)^2 + (x7 - x12)^2 + (x13 - x18)^2
    >= 0.6144835321)
@NLconstraint(m, e6, (x2 - x3)^2 + (x8 - x9)^2 + (x14 - x15)^2 >= 0.6144835321)
@NLconstraint(m, e7, (x2 - x4)^2 + (x8 - x10)^2 + (x14 - x16)^2
    >= 0.6144835321)
@NLconstraint(m, e8, (x2 - x5)^2 + (x8 - x11)^2 + (x14 - x17)^2
    >= 0.6144835321)
@NLconstraint(m, e9, (x2 - x6)^2 + (x8 - x12)^2 + (x14 - x18)^2
    >= 0.6144835321)
@NLconstraint(m, e10, (x3 - x4)^2 + (x9 - x10)^2 + (x15 - x16)^2
    >= 0.6144835321)
@NLconstraint(m, e11, (x3 - x5)^2 + (x9 - x11)^2 + (x15 - x17)^2
    >= 0.6144835321)
@NLconstraint(m, e12, (x3 - x6)^2 + (x9 - x12)^2 + (x15 - x18)^2
    >= 0.6144835321)
@NLconstraint(m, e13, (x4 - x5)^2 + (x10 - x11)^2 + (x16 - x17)^2
    >= 0.6144835321)
@NLconstraint(m, e14, (x4 - x6)^2 + (x10 - x12)^2 + (x16 - x18)^2
    >= 0.6144835321)
@NLconstraint(m, e15, (x5 - x6)^2 + (x11 - x12)^2 + (x17 - x18)^2
    >= 0.6144835321)
@constraint(m, e16, x1 - x2 <= 0)
@constraint(m, e17, x2 - x3 <= 0)
@constraint(m, e18, x3 - x4 <= 0)
@constraint(m, e19, x4 - x5 <= 0)
@constraint(m, e20, x5 - x6 <= 0)
