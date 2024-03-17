# NLP written by GAMS Convert at 03/17/24 14:48:04
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#        10        0       10        0        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        15       15        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#        60        0       60
#
# Reformulation has removed 1 variable and 1 equation

using JuMP
using MathOptInterface
const MOI = MathOptInterface

model = m = Model()

@variable(m, 0 <= x1 <= 4, start=0)
@variable(m, 0 <= x2 <= 4, start=0)
@variable(m, 0 <= x3 <= 4, start=0)
@variable(m, 0 <= x4 <= 4, start=0)
@variable(m, 0 <= x5 <= 4, start=0)
@variable(m, -4 <= x6 <= 4, start=0)
@variable(m, -4 <= x7 <= 4, start=0)
@variable(m, -4 <= x8 <= 4, start=0)
@variable(m, -4 <= x9 <= 4, start=0)
@variable(m, -4 <= x10 <= 4, start=0)
@variable(m, -4 <= x11 <= 4, start=0)
@variable(m, -4 <= x12 <= 4, start=0)
@variable(m, -4 <= x13 <= 4, start=0)
@variable(m, -4 <= x14 <= 4, start=0)
@variable(m, -4 <= x15 <= 4, start=0)

@NLobjective(m, Min, ((x1 - x2)^2 + (x6 - x7)^2 + (x11 - x12)^2)^(-3) * (((x1
    - x2)^2 + (x6 - x7)^2 + (x11 - x12)^2)^(-3) - 2) + ((x1 - x3)^2 + (x6 - x8)
    ^2 + (x11 - x13)^2)^(-3) * (((x1 - x3)^2 + (x6 - x8)^2 + (x11 - x13)^2)^(-3)
    - 2) + ((x1 - x4)^2 + (x6 - x9)^2 + (x11 - x14)^2)^(-3) * (((x1 - x4)^2 +
    (x6 - x9)^2 + (x11 - x14)^2)^(-3) - 2) + ((x1 - x5)^2 + (x6 - x10)^2 + (x11
    - x15)^2)^(-3) * (((x1 - x5)^2 + (x6 - x10)^2 + (x11 - x15)^2)^(-3) - 2)
    + ((x2 - x3)^2 + (x7 - x8)^2 + (x12 - x13)^2)^(-3) * (((x2 - x3)^2 + (x7
    - x8)^2 + (x12 - x13)^2)^(-3) - 2) + ((x2 - x4)^2 + (x7 - x9)^2 + (x12 -
    x14)^2)^(-3) * (((x2 - x4)^2 + (x7 - x9)^2 + (x12 - x14)^2)^(-3) - 2) + ((
    x2 - x5)^2 + (x7 - x10)^2 + (x12 - x15)^2)^(-3) * (((x2 - x5)^2 + (x7 - x10)
    ^2 + (x12 - x15)^2)^(-3) - 2) + ((x3 - x4)^2 + (x8 - x9)^2 + (x13 - x14)^2)
    ^(-3) * (((x3 - x4)^2 + (x8 - x9)^2 + (x13 - x14)^2)^(-3) - 2) + ((x3 - x5)
    ^2 + (x8 - x10)^2 + (x13 - x15)^2)^(-3) * (((x3 - x5)^2 + (x8 - x10)^2 + (
    x13 - x15)^2)^(-3) - 2) + ((x4 - x5)^2 + (x9 - x10)^2 + (x14 - x15)^2)^(-3)
    * (((x4 - x5)^2 + (x9 - x10)^2 + (x14 - x15)^2)^(-3) - 2))

@NLconstraint(m, e1, (x1 - x2)^2 + (x6 - x7)^2 + (x11 - x12)^2
    >= 0.46785600000000005)
@NLconstraint(m, e2, (x1 - x3)^2 + (x6 - x8)^2 + (x11 - x13)^2
    >= 0.46785600000000005)
@NLconstraint(m, e3, (x1 - x4)^2 + (x6 - x9)^2 + (x11 - x14)^2
    >= 0.46785600000000005)
@NLconstraint(m, e4, (x1 - x5)^2 + (x6 - x10)^2 + (x11 - x15)^2
    >= 0.46785600000000005)
@NLconstraint(m, e5, (x2 - x3)^2 + (x7 - x8)^2 + (x12 - x13)^2
    >= 0.46785600000000005)
@NLconstraint(m, e6, (x2 - x4)^2 + (x7 - x9)^2 + (x12 - x14)^2
    >= 0.46785600000000005)
@NLconstraint(m, e7, (x2 - x5)^2 + (x7 - x10)^2 + (x12 - x15)^2
    >= 0.46785600000000005)
@NLconstraint(m, e8, (x3 - x4)^2 + (x8 - x9)^2 + (x13 - x14)^2
    >= 0.46785600000000005)
@NLconstraint(m, e9, (x3 - x5)^2 + (x8 - x10)^2 + (x13 - x15)^2
    >= 0.46785600000000005)
@NLconstraint(m, e10, (x4 - x5)^2 + (x9 - x10)^2 + (x14 - x15)^2
    >= 0.46785600000000005)
