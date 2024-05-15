# MINLP written by GAMS Convert at 05/15/24 11:56:34
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#        28       10       18        0        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        45       27       18        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       138       75       63
#
# Reformulation has removed 1 variable and 1 equation

using JuMP
using MathOptInterface
const MOI = MathOptInterface

model = m = Model()

@variable(m, 0 <= x1 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x2 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x3 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x4 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x5 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x6 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x7 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x8 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x9 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x10 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x11 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x12 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x13 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x14 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x15 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x16 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x17 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x18 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x19 <= 1, start=0)
@variable(m, 0 <= x20 <= 1, start=0)
@variable(m, 0 <= x21 <= 1, start=0)
@variable(m, 0 <= x22 <= 1, start=0)
@variable(m, 0 <= x23 <= 1, start=0)
@variable(m, 0 <= x24 <= 1, start=0)
@variable(m, 0 <= x25 <= 1, start=0)
@variable(m, 0 <= x26 <= 1, start=0)
@variable(m, 0 <= x27 <= 1, start=0)
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
@variable(m, 0 <= b43 <= 1, binary=true, start=0)
@variable(m, 0 <= b44 <= 1, binary=true, start=0)
@variable(m, 0 <= b45 <= 1, binary=true, start=0)

@objective(m, Min, x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x10 + x11 + x12
    + x13 + x14 + x15 + x16 + x17 + x18)

@NLconstraint(m, e1, -sqrt((x19 - x22)^2 + (x20 - x23)^2 + (x21 - x24)^2) + x1
    - 1.7320508075688772 * b28 >= -1.7320508075688772)
@NLconstraint(m, e2, -sqrt((x19 - x25)^2 + (x20 - x26)^2 + (x21 - x27)^2) + x2
    - 1.7320508075688772 * b29 >= -1.7320508075688772)
@NLconstraint(m, e3, -sqrt((x22 - x25)^2 + (x23 - x26)^2 + (x24 - x27)^2) + x3
    - 1.7320508075688772 * b30 >= -1.7320508075688772)
@NLconstraint(m, e4, -sqrt((-0.965242141552123 + x19)^2 + (
    -0.011654693792141124 + x20)^2 + (-0.7359916197968754 + x21)^2) + x4 -
    1.7320508075688772 * b31 >= -1.7320508075688772)
@NLconstraint(m, e5, -sqrt((-0.15801272476474815 + x19)^2 + (
    -0.9863394516628233 + x20)^2 + (-0.016880654207976242 + x21)^2) + x5 -
    1.7320508075688772 * b32 >= -1.7320508075688772)
@NLconstraint(m, e6, -sqrt((-0.8794912681346712 + x19)^2 + (-0.6813506644014146
    + x20)^2 + (-0.8573423824815248 + x21)^2) + x6 - 1.7320508075688772 * b33
    >= -1.7320508075688772)
@NLconstraint(m, e7, -sqrt((-0.9998162341661194 + x19)^2 + (
    -0.23971518216378862 + x20)^2 + (-0.33807775725669986 + x21)^2) + x7 -
    1.7320508075688772 * b34 >= -1.7320508075688772)
@NLconstraint(m, e8, -sqrt((-0.7081943329851277 + x19)^2 + (
    -0.28058168584313725 + x20)^2 + (-0.2633142571474607 + x21)^2) + x8 -
    1.7320508075688772 * b35 >= -1.7320508075688772)
@NLconstraint(m, e9, -sqrt((-0.965242141552123 + x22)^2 + (
    -0.011654693792141124 + x23)^2 + (-0.7359916197968754 + x24)^2) + x9 -
    1.7320508075688772 * b36 >= -1.7320508075688772)
@NLconstraint(m, e10, -sqrt((-0.15801272476474815 + x22)^2 + (
    -0.9863394516628233 + x23)^2 + (-0.016880654207976242 + x24)^2) + x10 -
    1.7320508075688772 * b37 >= -1.7320508075688772)
@NLconstraint(m, e11, -sqrt((-0.8794912681346712 + x22)^2 + (
    -0.6813506644014146 + x23)^2 + (-0.8573423824815248 + x24)^2) + x11 -
    1.7320508075688772 * b38 >= -1.7320508075688772)
@NLconstraint(m, e12, -sqrt((-0.9998162341661194 + x22)^2 + (
    -0.23971518216378862 + x23)^2 + (-0.33807775725669986 + x24)^2) + x12 -
    1.7320508075688772 * b39 >= -1.7320508075688772)
@NLconstraint(m, e13, -sqrt((-0.7081943329851277 + x22)^2 + (
    -0.28058168584313725 + x23)^2 + (-0.2633142571474607 + x24)^2) + x13 -
    1.7320508075688772 * b40 >= -1.7320508075688772)
@NLconstraint(m, e14, -sqrt((-0.965242141552123 + x25)^2 + (
    -0.011654693792141124 + x26)^2 + (-0.7359916197968754 + x27)^2) + x14 -
    1.7320508075688772 * b41 >= -1.7320508075688772)
@NLconstraint(m, e15, -sqrt((-0.15801272476474815 + x25)^2 + (
    -0.9863394516628233 + x26)^2 + (-0.016880654207976242 + x27)^2) + x15 -
    1.7320508075688772 * b42 >= -1.7320508075688772)
@NLconstraint(m, e16, -sqrt((-0.8794912681346712 + x25)^2 + (
    -0.6813506644014146 + x26)^2 + (-0.8573423824815248 + x27)^2) + x16 -
    1.7320508075688772 * b43 >= -1.7320508075688772)
@NLconstraint(m, e17, -sqrt((-0.9998162341661194 + x25)^2 + (
    -0.23971518216378862 + x26)^2 + (-0.33807775725669986 + x27)^2) + x17 -
    1.7320508075688772 * b44 >= -1.7320508075688772)
@NLconstraint(m, e18, -sqrt((-0.7081943329851277 + x25)^2 + (
    -0.28058168584313725 + x26)^2 + (-0.2633142571474607 + x27)^2) + x18 -
    1.7320508075688772 * b45 >= -1.7320508075688772)
@constraint(m, e19, b31 + b36 + b41 == 1)
@constraint(m, e20, b32 + b37 + b42 == 1)
@constraint(m, e21, b33 + b38 + b43 == 1)
@constraint(m, e22, b34 + b39 + b44 == 1)
@constraint(m, e23, b35 + b40 + b45 == 1)
@constraint(m, e24, b28 + b29 + b31 + b32 + b33 + b34 + b35 == 3)
@constraint(m, e25, b28 + b30 + b36 + b37 + b38 + b39 + b40 == 3)
@constraint(m, e26, b29 + b30 + b41 + b42 + b43 + b44 + b45 == 3)
@constraint(m, e27, b28 == 1)
@constraint(m, e28, b29 + b30 == 1)
