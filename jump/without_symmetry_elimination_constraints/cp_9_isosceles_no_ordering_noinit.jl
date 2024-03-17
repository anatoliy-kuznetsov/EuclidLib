# NLP written by GAMS Convert at 03/17/24 14:48:05
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#        63        0       63        0        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        19       19        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       243       63      180
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
@variable(m, x19, start=0)

@objective(m, Max, x19)

@NLconstraint(m, e1, (x1 - x2)^2 + (x10 - x11)^2 - (2 * x19)^2 >= 0)
@NLconstraint(m, e2, (x1 - x3)^2 + (x10 - x12)^2 - (2 * x19)^2 >= 0)
@NLconstraint(m, e3, (x1 - x4)^2 + (x10 - x13)^2 - (2 * x19)^2 >= 0)
@NLconstraint(m, e4, (x1 - x5)^2 + (x10 - x14)^2 - (2 * x19)^2 >= 0)
@NLconstraint(m, e5, (x1 - x6)^2 + (x10 - x15)^2 - (2 * x19)^2 >= 0)
@NLconstraint(m, e6, (x1 - x7)^2 + (x10 - x16)^2 - (2 * x19)^2 >= 0)
@NLconstraint(m, e7, (x1 - x8)^2 + (x10 - x17)^2 - (2 * x19)^2 >= 0)
@NLconstraint(m, e8, (x1 - x9)^2 + (x10 - x18)^2 - (2 * x19)^2 >= 0)
@NLconstraint(m, e9, (x2 - x3)^2 + (x11 - x12)^2 - (2 * x19)^2 >= 0)
@NLconstraint(m, e10, (x2 - x4)^2 + (x11 - x13)^2 - (2 * x19)^2 >= 0)
@NLconstraint(m, e11, (x2 - x5)^2 + (x11 - x14)^2 - (2 * x19)^2 >= 0)
@NLconstraint(m, e12, (x2 - x6)^2 + (x11 - x15)^2 - (2 * x19)^2 >= 0)
@NLconstraint(m, e13, (x2 - x7)^2 + (x11 - x16)^2 - (2 * x19)^2 >= 0)
@NLconstraint(m, e14, (x2 - x8)^2 + (x11 - x17)^2 - (2 * x19)^2 >= 0)
@NLconstraint(m, e15, (x2 - x9)^2 + (x11 - x18)^2 - (2 * x19)^2 >= 0)
@NLconstraint(m, e16, (x3 - x4)^2 + (x12 - x13)^2 - (2 * x19)^2 >= 0)
@NLconstraint(m, e17, (x3 - x5)^2 + (x12 - x14)^2 - (2 * x19)^2 >= 0)
@NLconstraint(m, e18, (x3 - x6)^2 + (x12 - x15)^2 - (2 * x19)^2 >= 0)
@NLconstraint(m, e19, (x3 - x7)^2 + (x12 - x16)^2 - (2 * x19)^2 >= 0)
@NLconstraint(m, e20, (x3 - x8)^2 + (x12 - x17)^2 - (2 * x19)^2 >= 0)
@NLconstraint(m, e21, (x3 - x9)^2 + (x12 - x18)^2 - (2 * x19)^2 >= 0)
@NLconstraint(m, e22, (x4 - x5)^2 + (x13 - x14)^2 - (2 * x19)^2 >= 0)
@NLconstraint(m, e23, (x4 - x6)^2 + (x13 - x15)^2 - (2 * x19)^2 >= 0)
@NLconstraint(m, e24, (x4 - x7)^2 + (x13 - x16)^2 - (2 * x19)^2 >= 0)
@NLconstraint(m, e25, (x4 - x8)^2 + (x13 - x17)^2 - (2 * x19)^2 >= 0)
@NLconstraint(m, e26, (x4 - x9)^2 + (x13 - x18)^2 - (2 * x19)^2 >= 0)
@NLconstraint(m, e27, (x5 - x6)^2 + (x14 - x15)^2 - (2 * x19)^2 >= 0)
@NLconstraint(m, e28, (x5 - x7)^2 + (x14 - x16)^2 - (2 * x19)^2 >= 0)
@NLconstraint(m, e29, (x5 - x8)^2 + (x14 - x17)^2 - (2 * x19)^2 >= 0)
@NLconstraint(m, e30, (x5 - x9)^2 + (x14 - x18)^2 - (2 * x19)^2 >= 0)
@NLconstraint(m, e31, (x6 - x7)^2 + (x15 - x16)^2 - (2 * x19)^2 >= 0)
@NLconstraint(m, e32, (x6 - x8)^2 + (x15 - x17)^2 - (2 * x19)^2 >= 0)
@NLconstraint(m, e33, (x6 - x9)^2 + (x15 - x18)^2 - (2 * x19)^2 >= 0)
@NLconstraint(m, e34, (x7 - x8)^2 + (x16 - x17)^2 - (2 * x19)^2 >= 0)
@NLconstraint(m, e35, (x7 - x9)^2 + (x16 - x18)^2 - (2 * x19)^2 >= 0)
@NLconstraint(m, e36, (x8 - x9)^2 + (x17 - x18)^2 - (2 * x19)^2 >= 0)
@constraint(m, e37, x1 - x19 >= 0)
@constraint(m, e38, x2 - x19 >= 0)
@constraint(m, e39, x3 - x19 >= 0)
@constraint(m, e40, x4 - x19 >= 0)
@constraint(m, e41, x5 - x19 >= 0)
@constraint(m, e42, x6 - x19 >= 0)
@constraint(m, e43, x7 - x19 >= 0)
@constraint(m, e44, x8 - x19 >= 0)
@constraint(m, e45, x9 - x19 >= 0)
@constraint(m, e46, x10 - x19 >= 0)
@constraint(m, e47, x11 - x19 >= 0)
@constraint(m, e48, x12 - x19 >= 0)
@constraint(m, e49, x13 - x19 >= 0)
@constraint(m, e50, x14 - x19 >= 0)
@constraint(m, e51, x15 - x19 >= 0)
@constraint(m, e52, x16 - x19 >= 0)
@constraint(m, e53, x17 - x19 >= 0)
@constraint(m, e54, x18 - x19 >= 0)
@constraint(m, e55, -0.7071067811865475 * x1 - 0.7071067811865475 * x10 - x19
    >= -0.7071067811865475)
@constraint(m, e56, -0.7071067811865475 * x2 - 0.7071067811865475 * x11 - x19
    >= -0.7071067811865475)
@constraint(m, e57, -0.7071067811865475 * x3 - 0.7071067811865475 * x12 - x19
    >= -0.7071067811865475)
@constraint(m, e58, -0.7071067811865475 * x4 - 0.7071067811865475 * x13 - x19
    >= -0.7071067811865475)
@constraint(m, e59, -0.7071067811865475 * x5 - 0.7071067811865475 * x14 - x19
    >= -0.7071067811865475)
@constraint(m, e60, -0.7071067811865475 * x6 - 0.7071067811865475 * x15 - x19
    >= -0.7071067811865475)
@constraint(m, e61, -0.7071067811865475 * x7 - 0.7071067811865475 * x16 - x19
    >= -0.7071067811865475)
@constraint(m, e62, -0.7071067811865475 * x8 - 0.7071067811865475 * x17 - x19
    >= -0.7071067811865475)
@constraint(m, e63, -0.7071067811865475 * x9 - 0.7071067811865475 * x18 - x19
    >= -0.7071067811865475)
