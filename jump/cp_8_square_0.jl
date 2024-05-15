# NLP written by GAMS Convert at 05/15/24 11:27:03
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#        68        8       44       16        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        25       25        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       248       80      168
#
# Reformulation has removed 1 variable and 1 equation

using JuMP
using MathOptInterface
const MOI = MathOptInterface

model = m = Model()

@variable(m, -0.5 <= x1 <= 0.5, start=0)
@variable(m, -0.5 <= x2 <= 0.5, start=0)
@variable(m, -0.5 <= x3 <= 0.5, start=0)
@variable(m, -0.5 <= x4 <= 0.5, start=0)
@variable(m, -0.5 <= x5 <= 0.5, start=0)
@variable(m, -0.5 <= x6 <= 0.5, start=0)
@variable(m, -0.5 <= x7 <= 0.5, start=0)
@variable(m, -0.5 <= x8 <= 0.5, start=0)
@variable(m, -0.5 <= x9 <= 0.5, start=0)
@variable(m, -0.5 <= x10 <= 0.5, start=0)
@variable(m, -0.5 <= x11 <= 0.5, start=0)
@variable(m, -0.5 <= x12 <= 0.5, start=0)
@variable(m, -0.5 <= x13 <= 0.5, start=0)
@variable(m, -0.5 <= x14 <= 0.5, start=0)
@variable(m, -0.5 <= x15 <= 0.5, start=0)
@variable(m, -0.5 <= x16 <= 0.5, start=0)
@variable(m, x17, start=0)
@variable(m, x18, start=0)
@variable(m, x19, start=0)
@variable(m, x20, start=0)
@variable(m, x21, start=0)
@variable(m, x22, start=0)
@variable(m, x23, start=0)
@variable(m, x24, start=0)
@variable(m, x25, start=0)

@objective(m, Max, x25)

@NLconstraint(m, e1, (x1 - x2)^2 + (x9 - x10)^2 - (x17 + x18)^2 >= 0)
@NLconstraint(m, e2, (x1 - x3)^2 + (x9 - x11)^2 - (x17 + x19)^2 >= 0)
@NLconstraint(m, e3, (x1 - x4)^2 + (x9 - x12)^2 - (x17 + x20)^2 >= 0)
@NLconstraint(m, e4, (x1 - x5)^2 + (x9 - x13)^2 - (x17 + x21)^2 >= 0)
@NLconstraint(m, e5, (x1 - x6)^2 + (x9 - x14)^2 - (x17 + x22)^2 >= 0)
@NLconstraint(m, e6, (x1 - x7)^2 + (x9 - x15)^2 - (x17 + x23)^2 >= 0)
@NLconstraint(m, e7, (x1 - x8)^2 + (x9 - x16)^2 - (x17 + x24)^2 >= 0)
@NLconstraint(m, e8, (x2 - x3)^2 + (x10 - x11)^2 - (x18 + x19)^2 >= 0)
@NLconstraint(m, e9, (x2 - x4)^2 + (x10 - x12)^2 - (x18 + x20)^2 >= 0)
@NLconstraint(m, e10, (x2 - x5)^2 + (x10 - x13)^2 - (x18 + x21)^2 >= 0)
@NLconstraint(m, e11, (x2 - x6)^2 + (x10 - x14)^2 - (x18 + x22)^2 >= 0)
@NLconstraint(m, e12, (x2 - x7)^2 + (x10 - x15)^2 - (x18 + x23)^2 >= 0)
@NLconstraint(m, e13, (x2 - x8)^2 + (x10 - x16)^2 - (x18 + x24)^2 >= 0)
@NLconstraint(m, e14, (x3 - x4)^2 + (x11 - x12)^2 - (x19 + x20)^2 >= 0)
@NLconstraint(m, e15, (x3 - x5)^2 + (x11 - x13)^2 - (x19 + x21)^2 >= 0)
@NLconstraint(m, e16, (x3 - x6)^2 + (x11 - x14)^2 - (x19 + x22)^2 >= 0)
@NLconstraint(m, e17, (x3 - x7)^2 + (x11 - x15)^2 - (x19 + x23)^2 >= 0)
@NLconstraint(m, e18, (x3 - x8)^2 + (x11 - x16)^2 - (x19 + x24)^2 >= 0)
@NLconstraint(m, e19, (x4 - x5)^2 + (x12 - x13)^2 - (x20 + x21)^2 >= 0)
@NLconstraint(m, e20, (x4 - x6)^2 + (x12 - x14)^2 - (x20 + x22)^2 >= 0)
@NLconstraint(m, e21, (x4 - x7)^2 + (x12 - x15)^2 - (x20 + x23)^2 >= 0)
@NLconstraint(m, e22, (x4 - x8)^2 + (x12 - x16)^2 - (x20 + x24)^2 >= 0)
@NLconstraint(m, e23, (x5 - x6)^2 + (x13 - x14)^2 - (x21 + x22)^2 >= 0)
@NLconstraint(m, e24, (x5 - x7)^2 + (x13 - x15)^2 - (x21 + x23)^2 >= 0)
@NLconstraint(m, e25, (x5 - x8)^2 + (x13 - x16)^2 - (x21 + x24)^2 >= 0)
@NLconstraint(m, e26, (x6 - x7)^2 + (x14 - x15)^2 - (x22 + x23)^2 >= 0)
@NLconstraint(m, e27, (x6 - x8)^2 + (x14 - x16)^2 - (x22 + x24)^2 >= 0)
@NLconstraint(m, e28, (x7 - x8)^2 + (x15 - x16)^2 - (x23 + x24)^2 >= 0)
@constraint(m, e29, x17 - x25 == 0)
@constraint(m, e30, x18 - x25 == 0)
@constraint(m, e31, x19 - x25 == 0)
@constraint(m, e32, x20 - x25 == 0)
@constraint(m, e33, x21 - x25 == 0)
@constraint(m, e34, x22 - x25 == 0)
@constraint(m, e35, x23 - x25 == 0)
@constraint(m, e36, x24 - x25 == 0)
@constraint(m, e37, x1 + x17 <= 0.5)
@constraint(m, e38, x2 + x18 <= 0.5)
@constraint(m, e39, x3 + x19 <= 0.5)
@constraint(m, e40, x4 + x20 <= 0.5)
@constraint(m, e41, x5 + x21 <= 0.5)
@constraint(m, e42, x6 + x22 <= 0.5)
@constraint(m, e43, x7 + x23 <= 0.5)
@constraint(m, e44, x8 + x24 <= 0.5)
@constraint(m, e45, x1 - x17 >= -0.5)
@constraint(m, e46, x2 - x18 >= -0.5)
@constraint(m, e47, x3 - x19 >= -0.5)
@constraint(m, e48, x4 - x20 >= -0.5)
@constraint(m, e49, x5 - x21 >= -0.5)
@constraint(m, e50, x6 - x22 >= -0.5)
@constraint(m, e51, x7 - x23 >= -0.5)
@constraint(m, e52, x8 - x24 >= -0.5)
@constraint(m, e53, x9 + x17 <= 0.5)
@constraint(m, e54, x10 + x18 <= 0.5)
@constraint(m, e55, x11 + x19 <= 0.5)
@constraint(m, e56, x12 + x20 <= 0.5)
@constraint(m, e57, x13 + x21 <= 0.5)
@constraint(m, e58, x14 + x22 <= 0.5)
@constraint(m, e59, x15 + x23 <= 0.5)
@constraint(m, e60, x16 + x24 <= 0.5)
@constraint(m, e61, x9 - x17 >= -0.5)
@constraint(m, e62, x10 - x18 >= -0.5)
@constraint(m, e63, x11 - x19 >= -0.5)
@constraint(m, e64, x12 - x20 >= -0.5)
@constraint(m, e65, x13 - x21 >= -0.5)
@constraint(m, e66, x14 - x22 >= -0.5)
@constraint(m, e67, x15 - x23 >= -0.5)
@constraint(m, e68, x16 - x24 >= -0.5)
