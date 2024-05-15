# MINLP written by GAMS Convert at 05/15/24 11:55:36
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#        28       10       18        0        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        48       30       18        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       159       75       84
#
# Reformulation has removed 1 variable and 1 equation

using JuMP
using MathOptInterface
const MOI = MathOptInterface

model = m = Model()

@variable(m, 0 <= x1 <= 2, start=0)
@variable(m, 0 <= x2 <= 2, start=0)
@variable(m, 0 <= x3 <= 2, start=0)
@variable(m, 0 <= x4 <= 2, start=0)
@variable(m, 0 <= x5 <= 2, start=0)
@variable(m, 0 <= x6 <= 2, start=0)
@variable(m, 0 <= x7 <= 2, start=0)
@variable(m, 0 <= x8 <= 2, start=0)
@variable(m, 0 <= x9 <= 2, start=0)
@variable(m, 0 <= x10 <= 2, start=0)
@variable(m, 0 <= x11 <= 2, start=0)
@variable(m, 0 <= x12 <= 2, start=0)
@variable(m, 0 <= x13 <= 2, start=0)
@variable(m, 0 <= x14 <= 2, start=0)
@variable(m, 0 <= x15 <= 2, start=0)
@variable(m, 0 <= x16 <= 2, start=0)
@variable(m, 0 <= x17 <= 2, start=0)
@variable(m, 0 <= x18 <= 2, start=0)
@variable(m, 0 <= x19 <= 1, start=0)
@variable(m, 0 <= x20 <= 1, start=0)
@variable(m, 0 <= x21 <= 1, start=0)
@variable(m, 0 <= x22 <= 1, start=0)
@variable(m, 0 <= x23 <= 1, start=0)
@variable(m, 0 <= x24 <= 1, start=0)
@variable(m, 0 <= x25 <= 1, start=0)
@variable(m, 0 <= x26 <= 1, start=0)
@variable(m, 0 <= x27 <= 1, start=0)
@variable(m, 0 <= x28 <= 1, start=0)
@variable(m, 0 <= x29 <= 1, start=0)
@variable(m, 0 <= x30 <= 1, start=0)
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
@variable(m, 0 <= b43 <= 1, binary=true, start=0)
@variable(m, 0 <= b44 <= 1, binary=true, start=0)
@variable(m, 0 <= b45 <= 1, binary=true, start=0)
@variable(m, 0 <= b46 <= 1, binary=true, start=0)
@variable(m, 0 <= b47 <= 1, binary=true, start=0)
@variable(m, 0 <= b48 <= 1, binary=true, start=0)

@objective(m, Min, x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x10 + x11 + x12
    + x13 + x14 + x15 + x16 + x17 + x18)

@NLconstraint(m, e1, -sqrt((x19 - x23)^2 + (x20 - x24)^2 + (x21 - x25)^2 + (x22
    - x26)^2) + x1 - 2 * b31 >= -2)
@NLconstraint(m, e2, -sqrt((x19 - x27)^2 + (x20 - x28)^2 + (x21 - x29)^2 + (x22
    - x30)^2) + x2 - 2 * b32 >= -2)
@NLconstraint(m, e3, -sqrt((x23 - x27)^2 + (x24 - x28)^2 + (x25 - x29)^2 + (x26
    - x30)^2) + x3 - 2 * b33 >= -2)
@NLconstraint(m, e4, -sqrt((-0.9056396761745207 + x19)^2 + (-0.6862541570267026
    + x20)^2 + (-0.7665092563626442 + x21)^2 + (-0.9046162378132736 + x22)^2)
    + x4 - 2 * b34 >= -2)
@NLconstraint(m, e5, -sqrt((-0.2598274474889769 + x19)^2 + (-0.6357258696059892
    + x20)^2 + (-0.9049456946664788 + x21)^2 + (-0.8721303740697106 + x22)^2)
    + x5 - 2 * b35 >= -2)
@NLconstraint(m, e6, -sqrt((-0.5729406692492218 + x19)^2 + (-0.1693780871255699
    + x20)^2 + (-0.4115230620409567 + x21)^2 + (-0.9938380127773296 + x22)^2)
    + x6 - 2 * b36 >= -2)
@NLconstraint(m, e7, -sqrt((-0.10324779991117994 + x19)^2 + (
    -0.31913914884928973 + x20)^2 + (-0.9500391079535002 + x21)^2 + (
    -0.4494007558523254 + x22)^2) + x7 - 2 * b37 >= -2)
@NLconstraint(m, e8, -sqrt((-0.20865257233244294 + x19)^2 + (-0.316903983245593
    + x20)^2 + (-0.9086358448961127 + x21)^2 + (-0.33556881046847387 + x22)^2)
    + x8 - 2 * b38 >= -2)
@NLconstraint(m, e9, -sqrt((-0.9056396761745207 + x23)^2 + (-0.6862541570267026
    + x24)^2 + (-0.7665092563626442 + x25)^2 + (-0.9046162378132736 + x26)^2)
    + x9 - 2 * b39 >= -2)
@NLconstraint(m, e10, -sqrt((-0.2598274474889769 + x23)^2 + (
    -0.6357258696059892 + x24)^2 + (-0.9049456946664788 + x25)^2 + (
    -0.8721303740697106 + x26)^2) + x10 - 2 * b40 >= -2)
@NLconstraint(m, e11, -sqrt((-0.5729406692492218 + x23)^2 + (
    -0.1693780871255699 + x24)^2 + (-0.4115230620409567 + x25)^2 + (
    -0.9938380127773296 + x26)^2) + x11 - 2 * b41 >= -2)
@NLconstraint(m, e12, -sqrt((-0.10324779991117994 + x23)^2 + (
    -0.31913914884928973 + x24)^2 + (-0.9500391079535002 + x25)^2 + (
    -0.4494007558523254 + x26)^2) + x12 - 2 * b42 >= -2)
@NLconstraint(m, e13, -sqrt((-0.20865257233244294 + x23)^2 + (
    -0.316903983245593 + x24)^2 + (-0.9086358448961127 + x25)^2 + (
    -0.33556881046847387 + x26)^2) + x13 - 2 * b43 >= -2)
@NLconstraint(m, e14, -sqrt((-0.9056396761745207 + x27)^2 + (
    -0.6862541570267026 + x28)^2 + (-0.7665092563626442 + x29)^2 + (
    -0.9046162378132736 + x30)^2) + x14 - 2 * b44 >= -2)
@NLconstraint(m, e15, -sqrt((-0.2598274474889769 + x27)^2 + (
    -0.6357258696059892 + x28)^2 + (-0.9049456946664788 + x29)^2 + (
    -0.8721303740697106 + x30)^2) + x15 - 2 * b45 >= -2)
@NLconstraint(m, e16, -sqrt((-0.5729406692492218 + x27)^2 + (
    -0.1693780871255699 + x28)^2 + (-0.4115230620409567 + x29)^2 + (
    -0.9938380127773296 + x30)^2) + x16 - 2 * b46 >= -2)
@NLconstraint(m, e17, -sqrt((-0.10324779991117994 + x27)^2 + (
    -0.31913914884928973 + x28)^2 + (-0.9500391079535002 + x29)^2 + (
    -0.4494007558523254 + x30)^2) + x17 - 2 * b47 >= -2)
@NLconstraint(m, e18, -sqrt((-0.20865257233244294 + x27)^2 + (
    -0.316903983245593 + x28)^2 + (-0.9086358448961127 + x29)^2 + (
    -0.33556881046847387 + x30)^2) + x18 - 2 * b48 >= -2)
@constraint(m, e19, b34 + b39 + b44 == 1)
@constraint(m, e20, b35 + b40 + b45 == 1)
@constraint(m, e21, b36 + b41 + b46 == 1)
@constraint(m, e22, b37 + b42 + b47 == 1)
@constraint(m, e23, b38 + b43 + b48 == 1)
@constraint(m, e24, b31 + b32 + b34 + b35 + b36 + b37 + b38 == 3)
@constraint(m, e25, b31 + b33 + b39 + b40 + b41 + b42 + b43 == 3)
@constraint(m, e26, b32 + b33 + b44 + b45 + b46 + b47 + b48 == 3)
@constraint(m, e27, b31 == 1)
@constraint(m, e28, b32 + b33 == 1)
