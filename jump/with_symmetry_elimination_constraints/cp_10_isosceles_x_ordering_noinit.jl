# NLP written by GAMS Convert at 03/17/24 14:47:57
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#        84        0       75        9        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        21       21        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       313       88      225
#
# Reformulation has removed 1 variable and 1 equation

using JuMP
using MathOptInterface
const MOI = MathOptInterface

model = m = Model()

@variable(m, 0 <= x1 <= 1, start=0)
@variable(m, 0 <= x2 <= 1, start=0)
@variable(m, 0 <= x3 <= 1, start=0)
@variable(m, 0 <= x4 <= 1, start=0)
@variable(m, 0 <= x5 <= 1, start=0)
@variable(m, 0 <= x6 <= 1, start=0)
@variable(m, 0 <= x7 <= 1, start=0)
@variable(m, 0 <= x8 <= 1, start=0)
@variable(m, 0 <= x9 <= 1, start=0)
@variable(m, 0 <= x10 <= 1, start=0)
@variable(m, 0 <= x11 <= 1, start=0)
@variable(m, 0 <= x12 <= 1, start=0)
@variable(m, 0 <= x13 <= 1, start=0)
@variable(m, 0 <= x14 <= 1, start=0)
@variable(m, 0 <= x15 <= 1, start=0)
@variable(m, 0 <= x16 <= 1, start=0)
@variable(m, 0 <= x17 <= 1, start=0)
@variable(m, 0 <= x18 <= 1, start=0)
@variable(m, 0 <= x19 <= 1, start=0)
@variable(m, 0 <= x20 <= 1, start=0)
@variable(m, x21, start=0)

@objective(m, Max, x21)

@NLconstraint(m, e1, (x1 - x2)^2 + (x11 - x12)^2 - (2 * x21)^2 >= 0)
@NLconstraint(m, e2, (x1 - x3)^2 + (x11 - x13)^2 - (2 * x21)^2 >= 0)
@NLconstraint(m, e3, (x1 - x4)^2 + (x11 - x14)^2 - (2 * x21)^2 >= 0)
@NLconstraint(m, e4, (x1 - x5)^2 + (x11 - x15)^2 - (2 * x21)^2 >= 0)
@NLconstraint(m, e5, (x1 - x6)^2 + (x11 - x16)^2 - (2 * x21)^2 >= 0)
@NLconstraint(m, e6, (x1 - x7)^2 + (x11 - x17)^2 - (2 * x21)^2 >= 0)
@NLconstraint(m, e7, (x1 - x8)^2 + (x11 - x18)^2 - (2 * x21)^2 >= 0)
@NLconstraint(m, e8, (x1 - x9)^2 + (x11 - x19)^2 - (2 * x21)^2 >= 0)
@NLconstraint(m, e9, (x1 - x10)^2 + (x11 - x20)^2 - (2 * x21)^2 >= 0)
@NLconstraint(m, e10, (x2 - x3)^2 + (x12 - x13)^2 - (2 * x21)^2 >= 0)
@NLconstraint(m, e11, (x2 - x4)^2 + (x12 - x14)^2 - (2 * x21)^2 >= 0)
@NLconstraint(m, e12, (x2 - x5)^2 + (x12 - x15)^2 - (2 * x21)^2 >= 0)
@NLconstraint(m, e13, (x2 - x6)^2 + (x12 - x16)^2 - (2 * x21)^2 >= 0)
@NLconstraint(m, e14, (x2 - x7)^2 + (x12 - x17)^2 - (2 * x21)^2 >= 0)
@NLconstraint(m, e15, (x2 - x8)^2 + (x12 - x18)^2 - (2 * x21)^2 >= 0)
@NLconstraint(m, e16, (x2 - x9)^2 + (x12 - x19)^2 - (2 * x21)^2 >= 0)
@NLconstraint(m, e17, (x2 - x10)^2 + (x12 - x20)^2 - (2 * x21)^2 >= 0)
@NLconstraint(m, e18, (x3 - x4)^2 + (x13 - x14)^2 - (2 * x21)^2 >= 0)
@NLconstraint(m, e19, (x3 - x5)^2 + (x13 - x15)^2 - (2 * x21)^2 >= 0)
@NLconstraint(m, e20, (x3 - x6)^2 + (x13 - x16)^2 - (2 * x21)^2 >= 0)
@NLconstraint(m, e21, (x3 - x7)^2 + (x13 - x17)^2 - (2 * x21)^2 >= 0)
@NLconstraint(m, e22, (x3 - x8)^2 + (x13 - x18)^2 - (2 * x21)^2 >= 0)
@NLconstraint(m, e23, (x3 - x9)^2 + (x13 - x19)^2 - (2 * x21)^2 >= 0)
@NLconstraint(m, e24, (x3 - x10)^2 + (x13 - x20)^2 - (2 * x21)^2 >= 0)
@NLconstraint(m, e25, (x4 - x5)^2 + (x14 - x15)^2 - (2 * x21)^2 >= 0)
@NLconstraint(m, e26, (x4 - x6)^2 + (x14 - x16)^2 - (2 * x21)^2 >= 0)
@NLconstraint(m, e27, (x4 - x7)^2 + (x14 - x17)^2 - (2 * x21)^2 >= 0)
@NLconstraint(m, e28, (x4 - x8)^2 + (x14 - x18)^2 - (2 * x21)^2 >= 0)
@NLconstraint(m, e29, (x4 - x9)^2 + (x14 - x19)^2 - (2 * x21)^2 >= 0)
@NLconstraint(m, e30, (x4 - x10)^2 + (x14 - x20)^2 - (2 * x21)^2 >= 0)
@NLconstraint(m, e31, (x5 - x6)^2 + (x15 - x16)^2 - (2 * x21)^2 >= 0)
@NLconstraint(m, e32, (x5 - x7)^2 + (x15 - x17)^2 - (2 * x21)^2 >= 0)
@NLconstraint(m, e33, (x5 - x8)^2 + (x15 - x18)^2 - (2 * x21)^2 >= 0)
@NLconstraint(m, e34, (x5 - x9)^2 + (x15 - x19)^2 - (2 * x21)^2 >= 0)
@NLconstraint(m, e35, (x5 - x10)^2 + (x15 - x20)^2 - (2 * x21)^2 >= 0)
@NLconstraint(m, e36, (x6 - x7)^2 + (x16 - x17)^2 - (2 * x21)^2 >= 0)
@NLconstraint(m, e37, (x6 - x8)^2 + (x16 - x18)^2 - (2 * x21)^2 >= 0)
@NLconstraint(m, e38, (x6 - x9)^2 + (x16 - x19)^2 - (2 * x21)^2 >= 0)
@NLconstraint(m, e39, (x6 - x10)^2 + (x16 - x20)^2 - (2 * x21)^2 >= 0)
@NLconstraint(m, e40, (x7 - x8)^2 + (x17 - x18)^2 - (2 * x21)^2 >= 0)
@NLconstraint(m, e41, (x7 - x9)^2 + (x17 - x19)^2 - (2 * x21)^2 >= 0)
@NLconstraint(m, e42, (x7 - x10)^2 + (x17 - x20)^2 - (2 * x21)^2 >= 0)
@NLconstraint(m, e43, (x8 - x9)^2 + (x18 - x19)^2 - (2 * x21)^2 >= 0)
@NLconstraint(m, e44, (x8 - x10)^2 + (x18 - x20)^2 - (2 * x21)^2 >= 0)
@NLconstraint(m, e45, (x9 - x10)^2 + (x19 - x20)^2 - (2 * x21)^2 >= 0)
@constraint(m, e46, x1 - x2 <= 0)
@constraint(m, e47, x2 - x3 <= 0)
@constraint(m, e48, x3 - x4 <= 0)
@constraint(m, e49, x4 - x5 <= 0)
@constraint(m, e50, x5 - x6 <= 0)
@constraint(m, e51, x6 - x7 <= 0)
@constraint(m, e52, x7 - x8 <= 0)
@constraint(m, e53, x8 - x9 <= 0)
@constraint(m, e54, x9 - x10 <= 0)
@constraint(m, e55, x1 - x21 >= 0)
@constraint(m, e56, x2 - x21 >= 0)
@constraint(m, e57, x3 - x21 >= 0)
@constraint(m, e58, x4 - x21 >= 0)
@constraint(m, e59, x5 - x21 >= 0)
@constraint(m, e60, x6 - x21 >= 0)
@constraint(m, e61, x7 - x21 >= 0)
@constraint(m, e62, x8 - x21 >= 0)
@constraint(m, e63, x9 - x21 >= 0)
@constraint(m, e64, x10 - x21 >= 0)
@constraint(m, e65, x11 - x21 >= 0)
@constraint(m, e66, x12 - x21 >= 0)
@constraint(m, e67, x13 - x21 >= 0)
@constraint(m, e68, x14 - x21 >= 0)
@constraint(m, e69, x15 - x21 >= 0)
@constraint(m, e70, x16 - x21 >= 0)
@constraint(m, e71, x17 - x21 >= 0)
@constraint(m, e72, x18 - x21 >= 0)
@constraint(m, e73, x19 - x21 >= 0)
@constraint(m, e74, x20 - x21 >= 0)
@constraint(m, e75, -0.7071067811865475 * x1 - 0.7071067811865475 * x11 - x21
    >= -0.7071067811865475)
@constraint(m, e76, -0.7071067811865475 * x2 - 0.7071067811865475 * x12 - x21
    >= -0.7071067811865475)
@constraint(m, e77, -0.7071067811865475 * x3 - 0.7071067811865475 * x13 - x21
    >= -0.7071067811865475)
@constraint(m, e78, -0.7071067811865475 * x4 - 0.7071067811865475 * x14 - x21
    >= -0.7071067811865475)
@constraint(m, e79, -0.7071067811865475 * x5 - 0.7071067811865475 * x15 - x21
    >= -0.7071067811865475)
@constraint(m, e80, -0.7071067811865475 * x6 - 0.7071067811865475 * x16 - x21
    >= -0.7071067811865475)
@constraint(m, e81, -0.7071067811865475 * x7 - 0.7071067811865475 * x17 - x21
    >= -0.7071067811865475)
@constraint(m, e82, -0.7071067811865475 * x8 - 0.7071067811865475 * x18 - x21
    >= -0.7071067811865475)
@constraint(m, e83, -0.7071067811865475 * x9 - 0.7071067811865475 * x19 - x21
    >= -0.7071067811865475)
@constraint(m, e84, -0.7071067811865475 * x10 - 0.7071067811865475 * x20 - x21
    >= -0.7071067811865475)
