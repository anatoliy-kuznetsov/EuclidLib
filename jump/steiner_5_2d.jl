# MINLP written by GAMS Convert at 05/15/24 11:57:55
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#        28       10       18        0        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        42       24       18        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       117       75       42
#
# Reformulation has removed 1 variable and 1 equation

using JuMP
using MathOptInterface
const MOI = MathOptInterface

model = m = Model()

@variable(m, 0 <= x1 <= 1.4142135623730951, start=0)
@variable(m, 0 <= x2 <= 1.4142135623730951, start=0)
@variable(m, 0 <= x3 <= 1.4142135623730951, start=0)
@variable(m, 0 <= x4 <= 1.4142135623730951, start=0)
@variable(m, 0 <= x5 <= 1.4142135623730951, start=0)
@variable(m, 0 <= x6 <= 1.4142135623730951, start=0)
@variable(m, 0 <= x7 <= 1.4142135623730951, start=0)
@variable(m, 0 <= x8 <= 1.4142135623730951, start=0)
@variable(m, 0 <= x9 <= 1.4142135623730951, start=0)
@variable(m, 0 <= x10 <= 1.4142135623730951, start=0)
@variable(m, 0 <= x11 <= 1.4142135623730951, start=0)
@variable(m, 0 <= x12 <= 1.4142135623730951, start=0)
@variable(m, 0 <= x13 <= 1.4142135623730951, start=0)
@variable(m, 0 <= x14 <= 1.4142135623730951, start=0)
@variable(m, 0 <= x15 <= 1.4142135623730951, start=0)
@variable(m, 0 <= x16 <= 1.4142135623730951, start=0)
@variable(m, 0 <= x17 <= 1.4142135623730951, start=0)
@variable(m, 0 <= x18 <= 1.4142135623730951, start=0)
@variable(m, 0 <= x19 <= 1, start=0)
@variable(m, 0 <= x20 <= 1, start=0)
@variable(m, 0 <= x21 <= 1, start=0)
@variable(m, 0 <= x22 <= 1, start=0)
@variable(m, 0 <= x23 <= 1, start=0)
@variable(m, 0 <= x24 <= 1, start=0)
@variable(m, 0 <= b25 <= 1, binary=true, start=0)
@variable(m, 0 <= b26 <= 1, binary=true, start=0)
@variable(m, 0 <= b27 <= 1, binary=true, start=0)
@variable(m, 0 <= b28 <= 1, binary=true, start=0)
@variable(m, 0 <= b29 <= 1, binary=true, start=0)
@variable(m, 0 <= b30 <= 1, binary=true, start=0)
@variable(m, 0 <= b31 <= 1, binary=true, start=0)
@variable(m, 0 <= b32 <= 1, binary=true, start=0)
@variable(m, 0 <= b33 <= 1, binary=true, start=0)
@variable(m, 0 <= b34 <= 1, binary=true, start=0)
@variable(m, 0 <= b35 <= 1, binary=true, start=0)
@variable(m, 0 <= b36 <= 1, binary=true, start=0)
@variable(m, 0 <= b37 <= 1, binary=true, start=0)
@variable(m, 0 <= b38 <= 1, binary=true, start=0)
@variable(m, 0 <= b39 <= 1, binary=true, start=0)
@variable(m, 0 <= b40 <= 1, binary=true, start=0)
@variable(m, 0 <= b41 <= 1, binary=true, start=0)
@variable(m, 0 <= b42 <= 1, binary=true, start=0)

@objective(m, Min, x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x10 + x11 + x12
    + x13 + x14 + x15 + x16 + x17 + x18)

@NLconstraint(m, e1, -sqrt((x19 - x21)^2 + (x20 - x22)^2) + x1 -
    1.4142135623730951 * b25 >= -1.4142135623730951)
@NLconstraint(m, e2, -sqrt((x19 - x23)^2 + (x20 - x24)^2) + x2 -
    1.4142135623730951 * b26 >= -1.4142135623730951)
@NLconstraint(m, e3, -sqrt((x21 - x23)^2 + (x22 - x24)^2) + x3 -
    1.4142135623730951 * b27 >= -1.4142135623730951)
@NLconstraint(m, e4, -sqrt((-0.5714025946899135 + x19)^2 + (-0.4288890546751146
    + x20)^2) + x4 - 1.4142135623730951 * b28 >= -1.4142135623730951)
@NLconstraint(m, e5, -sqrt((-0.5780913011344704 + x19)^2 + (
    -0.20609823213950174 + x20)^2) + x5 - 1.4142135623730951 * b29
    >= -1.4142135623730951)
@NLconstraint(m, e6, -sqrt((-0.81332125135732 + x19)^2 + (-0.8235888725334455
    + x20)^2) + x6 - 1.4142135623730951 * b30 >= -1.4142135623730951)
@NLconstraint(m, e7, -sqrt((-0.6534725339011758 + x19)^2 + (
    -0.16022955651881965 + x20)^2) + x7 - 1.4142135623730951 * b31
    >= -1.4142135623730951)
@NLconstraint(m, e8, -sqrt((-0.5206693596399246 + x19)^2 + (
    -0.32777281162209315 + x20)^2) + x8 - 1.4142135623730951 * b32
    >= -1.4142135623730951)
@NLconstraint(m, e9, -sqrt((-0.5714025946899135 + x21)^2 + (-0.4288890546751146
    + x22)^2) + x9 - 1.4142135623730951 * b33 >= -1.4142135623730951)
@NLconstraint(m, e10, -sqrt((-0.5780913011344704 + x21)^2 + (
    -0.20609823213950174 + x22)^2) + x10 - 1.4142135623730951 * b34
    >= -1.4142135623730951)
@NLconstraint(m, e11, -sqrt((-0.81332125135732 + x21)^2 + (-0.8235888725334455
    + x22)^2) + x11 - 1.4142135623730951 * b35 >= -1.4142135623730951)
@NLconstraint(m, e12, -sqrt((-0.6534725339011758 + x21)^2 + (
    -0.16022955651881965 + x22)^2) + x12 - 1.4142135623730951 * b36
    >= -1.4142135623730951)
@NLconstraint(m, e13, -sqrt((-0.5206693596399246 + x21)^2 + (
    -0.32777281162209315 + x22)^2) + x13 - 1.4142135623730951 * b37
    >= -1.4142135623730951)
@NLconstraint(m, e14, -sqrt((-0.5714025946899135 + x23)^2 + (
    -0.4288890546751146 + x24)^2) + x14 - 1.4142135623730951 * b38
    >= -1.4142135623730951)
@NLconstraint(m, e15, -sqrt((-0.5780913011344704 + x23)^2 + (
    -0.20609823213950174 + x24)^2) + x15 - 1.4142135623730951 * b39
    >= -1.4142135623730951)
@NLconstraint(m, e16, -sqrt((-0.81332125135732 + x23)^2 + (-0.8235888725334455
    + x24)^2) + x16 - 1.4142135623730951 * b40 >= -1.4142135623730951)
@NLconstraint(m, e17, -sqrt((-0.6534725339011758 + x23)^2 + (
    -0.16022955651881965 + x24)^2) + x17 - 1.4142135623730951 * b41
    >= -1.4142135623730951)
@NLconstraint(m, e18, -sqrt((-0.5206693596399246 + x23)^2 + (
    -0.32777281162209315 + x24)^2) + x18 - 1.4142135623730951 * b42
    >= -1.4142135623730951)
@constraint(m, e19, b28 + b33 + b38 == 1)
@constraint(m, e20, b29 + b34 + b39 == 1)
@constraint(m, e21, b30 + b35 + b40 == 1)
@constraint(m, e22, b31 + b36 + b41 == 1)
@constraint(m, e23, b32 + b37 + b42 == 1)
@constraint(m, e24, b25 + b26 + b28 + b29 + b30 + b31 + b32 == 3)
@constraint(m, e25, b25 + b27 + b33 + b34 + b35 + b36 + b37 == 3)
@constraint(m, e26, b26 + b27 + b38 + b39 + b40 + b41 + b42 == 3)
@constraint(m, e27, b25 == 1)
@constraint(m, e28, b26 + b27 == 1)
