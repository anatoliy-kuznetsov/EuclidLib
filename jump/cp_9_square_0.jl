# NLP written by GAMS Convert at 05/15/24 11:28:55
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#        81        9       54       18        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        28       28        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       306       90      216
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
@variable(m, -0.5 <= x17 <= 0.5, start=0)
@variable(m, -0.5 <= x18 <= 0.5, start=0)
@variable(m, x19, start=0)
@variable(m, x20, start=0)
@variable(m, x21, start=0)
@variable(m, x22, start=0)
@variable(m, x23, start=0)
@variable(m, x24, start=0)
@variable(m, x25, start=0)
@variable(m, x26, start=0)
@variable(m, x27, start=0)
@variable(m, x28, start=0)

@objective(m, Max, x28)

@NLconstraint(m, e1, (x1 - x2)^2 + (x10 - x11)^2 - (x19 + x20)^2 >= 0)
@NLconstraint(m, e2, (x1 - x3)^2 + (x10 - x12)^2 - (x19 + x21)^2 >= 0)
@NLconstraint(m, e3, (x1 - x4)^2 + (x10 - x13)^2 - (x19 + x22)^2 >= 0)
@NLconstraint(m, e4, (x1 - x5)^2 + (x10 - x14)^2 - (x19 + x23)^2 >= 0)
@NLconstraint(m, e5, (x1 - x6)^2 + (x10 - x15)^2 - (x19 + x24)^2 >= 0)
@NLconstraint(m, e6, (x1 - x7)^2 + (x10 - x16)^2 - (x19 + x25)^2 >= 0)
@NLconstraint(m, e7, (x1 - x8)^2 + (x10 - x17)^2 - (x19 + x26)^2 >= 0)
@NLconstraint(m, e8, (x1 - x9)^2 + (x10 - x18)^2 - (x19 + x27)^2 >= 0)
@NLconstraint(m, e9, (x2 - x3)^2 + (x11 - x12)^2 - (x20 + x21)^2 >= 0)
@NLconstraint(m, e10, (x2 - x4)^2 + (x11 - x13)^2 - (x20 + x22)^2 >= 0)
@NLconstraint(m, e11, (x2 - x5)^2 + (x11 - x14)^2 - (x20 + x23)^2 >= 0)
@NLconstraint(m, e12, (x2 - x6)^2 + (x11 - x15)^2 - (x20 + x24)^2 >= 0)
@NLconstraint(m, e13, (x2 - x7)^2 + (x11 - x16)^2 - (x20 + x25)^2 >= 0)
@NLconstraint(m, e14, (x2 - x8)^2 + (x11 - x17)^2 - (x20 + x26)^2 >= 0)
@NLconstraint(m, e15, (x2 - x9)^2 + (x11 - x18)^2 - (x20 + x27)^2 >= 0)
@NLconstraint(m, e16, (x3 - x4)^2 + (x12 - x13)^2 - (x21 + x22)^2 >= 0)
@NLconstraint(m, e17, (x3 - x5)^2 + (x12 - x14)^2 - (x21 + x23)^2 >= 0)
@NLconstraint(m, e18, (x3 - x6)^2 + (x12 - x15)^2 - (x21 + x24)^2 >= 0)
@NLconstraint(m, e19, (x3 - x7)^2 + (x12 - x16)^2 - (x21 + x25)^2 >= 0)
@NLconstraint(m, e20, (x3 - x8)^2 + (x12 - x17)^2 - (x21 + x26)^2 >= 0)
@NLconstraint(m, e21, (x3 - x9)^2 + (x12 - x18)^2 - (x21 + x27)^2 >= 0)
@NLconstraint(m, e22, (x4 - x5)^2 + (x13 - x14)^2 - (x22 + x23)^2 >= 0)
@NLconstraint(m, e23, (x4 - x6)^2 + (x13 - x15)^2 - (x22 + x24)^2 >= 0)
@NLconstraint(m, e24, (x4 - x7)^2 + (x13 - x16)^2 - (x22 + x25)^2 >= 0)
@NLconstraint(m, e25, (x4 - x8)^2 + (x13 - x17)^2 - (x22 + x26)^2 >= 0)
@NLconstraint(m, e26, (x4 - x9)^2 + (x13 - x18)^2 - (x22 + x27)^2 >= 0)
@NLconstraint(m, e27, (x5 - x6)^2 + (x14 - x15)^2 - (x23 + x24)^2 >= 0)
@NLconstraint(m, e28, (x5 - x7)^2 + (x14 - x16)^2 - (x23 + x25)^2 >= 0)
@NLconstraint(m, e29, (x5 - x8)^2 + (x14 - x17)^2 - (x23 + x26)^2 >= 0)
@NLconstraint(m, e30, (x5 - x9)^2 + (x14 - x18)^2 - (x23 + x27)^2 >= 0)
@NLconstraint(m, e31, (x6 - x7)^2 + (x15 - x16)^2 - (x24 + x25)^2 >= 0)
@NLconstraint(m, e32, (x6 - x8)^2 + (x15 - x17)^2 - (x24 + x26)^2 >= 0)
@NLconstraint(m, e33, (x6 - x9)^2 + (x15 - x18)^2 - (x24 + x27)^2 >= 0)
@NLconstraint(m, e34, (x7 - x8)^2 + (x16 - x17)^2 - (x25 + x26)^2 >= 0)
@NLconstraint(m, e35, (x7 - x9)^2 + (x16 - x18)^2 - (x25 + x27)^2 >= 0)
@NLconstraint(m, e36, (x8 - x9)^2 + (x17 - x18)^2 - (x26 + x27)^2 >= 0)
@constraint(m, e37, x19 - x28 == 0)
@constraint(m, e38, x20 - x28 == 0)
@constraint(m, e39, x21 - x28 == 0)
@constraint(m, e40, x22 - x28 == 0)
@constraint(m, e41, x23 - x28 == 0)
@constraint(m, e42, x24 - x28 == 0)
@constraint(m, e43, x25 - x28 == 0)
@constraint(m, e44, x26 - x28 == 0)
@constraint(m, e45, x27 - x28 == 0)
@constraint(m, e46, x1 + x19 <= 0.5)
@constraint(m, e47, x2 + x20 <= 0.5)
@constraint(m, e48, x3 + x21 <= 0.5)
@constraint(m, e49, x4 + x22 <= 0.5)
@constraint(m, e50, x5 + x23 <= 0.5)
@constraint(m, e51, x6 + x24 <= 0.5)
@constraint(m, e52, x7 + x25 <= 0.5)
@constraint(m, e53, x8 + x26 <= 0.5)
@constraint(m, e54, x9 + x27 <= 0.5)
@constraint(m, e55, x1 - x19 >= -0.5)
@constraint(m, e56, x2 - x20 >= -0.5)
@constraint(m, e57, x3 - x21 >= -0.5)
@constraint(m, e58, x4 - x22 >= -0.5)
@constraint(m, e59, x5 - x23 >= -0.5)
@constraint(m, e60, x6 - x24 >= -0.5)
@constraint(m, e61, x7 - x25 >= -0.5)
@constraint(m, e62, x8 - x26 >= -0.5)
@constraint(m, e63, x9 - x27 >= -0.5)
@constraint(m, e64, x10 + x19 <= 0.5)
@constraint(m, e65, x11 + x20 <= 0.5)
@constraint(m, e66, x12 + x21 <= 0.5)
@constraint(m, e67, x13 + x22 <= 0.5)
@constraint(m, e68, x14 + x23 <= 0.5)
@constraint(m, e69, x15 + x24 <= 0.5)
@constraint(m, e70, x16 + x25 <= 0.5)
@constraint(m, e71, x17 + x26 <= 0.5)
@constraint(m, e72, x18 + x27 <= 0.5)
@constraint(m, e73, x10 - x19 >= -0.5)
@constraint(m, e74, x11 - x20 >= -0.5)
@constraint(m, e75, x12 - x21 >= -0.5)
@constraint(m, e76, x13 - x22 >= -0.5)
@constraint(m, e77, x14 - x23 >= -0.5)
@constraint(m, e78, x15 - x24 >= -0.5)
@constraint(m, e79, x16 - x25 >= -0.5)
@constraint(m, e80, x17 - x26 >= -0.5)
@constraint(m, e81, x18 - x27 >= -0.5)
