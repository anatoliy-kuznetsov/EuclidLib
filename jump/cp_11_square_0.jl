# NLP written by GAMS Convert at 05/15/24 11:25:27
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       110       11       77       22        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        34       34        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       440      110      330
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
@variable(m, -0.5 <= x19 <= 0.5, start=0)
@variable(m, -0.5 <= x20 <= 0.5, start=0)
@variable(m, -0.5 <= x21 <= 0.5, start=0)
@variable(m, -0.5 <= x22 <= 0.5, start=0)
@variable(m, x23, start=0)
@variable(m, x24, start=0)
@variable(m, x25, start=0)
@variable(m, x26, start=0)
@variable(m, x27, start=0)
@variable(m, x28, start=0)
@variable(m, x29, start=0)
@variable(m, x30, start=0)
@variable(m, x31, start=0)
@variable(m, x32, start=0)
@variable(m, x33, start=0)
@variable(m, x34, start=0)

@objective(m, Max, x34)

@NLconstraint(m, e1, (x1 - x2)^2 + (x12 - x13)^2 - (x23 + x24)^2 >= 0)
@NLconstraint(m, e2, (x1 - x3)^2 + (x12 - x14)^2 - (x23 + x25)^2 >= 0)
@NLconstraint(m, e3, (x1 - x4)^2 + (x12 - x15)^2 - (x23 + x26)^2 >= 0)
@NLconstraint(m, e4, (x1 - x5)^2 + (x12 - x16)^2 - (x23 + x27)^2 >= 0)
@NLconstraint(m, e5, (x1 - x6)^2 + (x12 - x17)^2 - (x23 + x28)^2 >= 0)
@NLconstraint(m, e6, (x1 - x7)^2 + (x12 - x18)^2 - (x23 + x29)^2 >= 0)
@NLconstraint(m, e7, (x1 - x8)^2 + (x12 - x19)^2 - (x23 + x30)^2 >= 0)
@NLconstraint(m, e8, (x1 - x9)^2 + (x12 - x20)^2 - (x23 + x31)^2 >= 0)
@NLconstraint(m, e9, (x1 - x10)^2 + (x12 - x21)^2 - (x23 + x32)^2 >= 0)
@NLconstraint(m, e10, (x1 - x11)^2 + (x12 - x22)^2 - (x23 + x33)^2 >= 0)
@NLconstraint(m, e11, (x2 - x3)^2 + (x13 - x14)^2 - (x24 + x25)^2 >= 0)
@NLconstraint(m, e12, (x2 - x4)^2 + (x13 - x15)^2 - (x24 + x26)^2 >= 0)
@NLconstraint(m, e13, (x2 - x5)^2 + (x13 - x16)^2 - (x24 + x27)^2 >= 0)
@NLconstraint(m, e14, (x2 - x6)^2 + (x13 - x17)^2 - (x24 + x28)^2 >= 0)
@NLconstraint(m, e15, (x2 - x7)^2 + (x13 - x18)^2 - (x24 + x29)^2 >= 0)
@NLconstraint(m, e16, (x2 - x8)^2 + (x13 - x19)^2 - (x24 + x30)^2 >= 0)
@NLconstraint(m, e17, (x2 - x9)^2 + (x13 - x20)^2 - (x24 + x31)^2 >= 0)
@NLconstraint(m, e18, (x2 - x10)^2 + (x13 - x21)^2 - (x24 + x32)^2 >= 0)
@NLconstraint(m, e19, (x2 - x11)^2 + (x13 - x22)^2 - (x24 + x33)^2 >= 0)
@NLconstraint(m, e20, (x3 - x4)^2 + (x14 - x15)^2 - (x25 + x26)^2 >= 0)
@NLconstraint(m, e21, (x3 - x5)^2 + (x14 - x16)^2 - (x25 + x27)^2 >= 0)
@NLconstraint(m, e22, (x3 - x6)^2 + (x14 - x17)^2 - (x25 + x28)^2 >= 0)
@NLconstraint(m, e23, (x3 - x7)^2 + (x14 - x18)^2 - (x25 + x29)^2 >= 0)
@NLconstraint(m, e24, (x3 - x8)^2 + (x14 - x19)^2 - (x25 + x30)^2 >= 0)
@NLconstraint(m, e25, (x3 - x9)^2 + (x14 - x20)^2 - (x25 + x31)^2 >= 0)
@NLconstraint(m, e26, (x3 - x10)^2 + (x14 - x21)^2 - (x25 + x32)^2 >= 0)
@NLconstraint(m, e27, (x3 - x11)^2 + (x14 - x22)^2 - (x25 + x33)^2 >= 0)
@NLconstraint(m, e28, (x4 - x5)^2 + (x15 - x16)^2 - (x26 + x27)^2 >= 0)
@NLconstraint(m, e29, (x4 - x6)^2 + (x15 - x17)^2 - (x26 + x28)^2 >= 0)
@NLconstraint(m, e30, (x4 - x7)^2 + (x15 - x18)^2 - (x26 + x29)^2 >= 0)
@NLconstraint(m, e31, (x4 - x8)^2 + (x15 - x19)^2 - (x26 + x30)^2 >= 0)
@NLconstraint(m, e32, (x4 - x9)^2 + (x15 - x20)^2 - (x26 + x31)^2 >= 0)
@NLconstraint(m, e33, (x4 - x10)^2 + (x15 - x21)^2 - (x26 + x32)^2 >= 0)
@NLconstraint(m, e34, (x4 - x11)^2 + (x15 - x22)^2 - (x26 + x33)^2 >= 0)
@NLconstraint(m, e35, (x5 - x6)^2 + (x16 - x17)^2 - (x27 + x28)^2 >= 0)
@NLconstraint(m, e36, (x5 - x7)^2 + (x16 - x18)^2 - (x27 + x29)^2 >= 0)
@NLconstraint(m, e37, (x5 - x8)^2 + (x16 - x19)^2 - (x27 + x30)^2 >= 0)
@NLconstraint(m, e38, (x5 - x9)^2 + (x16 - x20)^2 - (x27 + x31)^2 >= 0)
@NLconstraint(m, e39, (x5 - x10)^2 + (x16 - x21)^2 - (x27 + x32)^2 >= 0)
@NLconstraint(m, e40, (x5 - x11)^2 + (x16 - x22)^2 - (x27 + x33)^2 >= 0)
@NLconstraint(m, e41, (x6 - x7)^2 + (x17 - x18)^2 - (x28 + x29)^2 >= 0)
@NLconstraint(m, e42, (x6 - x8)^2 + (x17 - x19)^2 - (x28 + x30)^2 >= 0)
@NLconstraint(m, e43, (x6 - x9)^2 + (x17 - x20)^2 - (x28 + x31)^2 >= 0)
@NLconstraint(m, e44, (x6 - x10)^2 + (x17 - x21)^2 - (x28 + x32)^2 >= 0)
@NLconstraint(m, e45, (x6 - x11)^2 + (x17 - x22)^2 - (x28 + x33)^2 >= 0)
@NLconstraint(m, e46, (x7 - x8)^2 + (x18 - x19)^2 - (x29 + x30)^2 >= 0)
@NLconstraint(m, e47, (x7 - x9)^2 + (x18 - x20)^2 - (x29 + x31)^2 >= 0)
@NLconstraint(m, e48, (x7 - x10)^2 + (x18 - x21)^2 - (x29 + x32)^2 >= 0)
@NLconstraint(m, e49, (x7 - x11)^2 + (x18 - x22)^2 - (x29 + x33)^2 >= 0)
@NLconstraint(m, e50, (x8 - x9)^2 + (x19 - x20)^2 - (x30 + x31)^2 >= 0)
@NLconstraint(m, e51, (x8 - x10)^2 + (x19 - x21)^2 - (x30 + x32)^2 >= 0)
@NLconstraint(m, e52, (x8 - x11)^2 + (x19 - x22)^2 - (x30 + x33)^2 >= 0)
@NLconstraint(m, e53, (x9 - x10)^2 + (x20 - x21)^2 - (x31 + x32)^2 >= 0)
@NLconstraint(m, e54, (x9 - x11)^2 + (x20 - x22)^2 - (x31 + x33)^2 >= 0)
@NLconstraint(m, e55, (x10 - x11)^2 + (x21 - x22)^2 - (x32 + x33)^2 >= 0)
@constraint(m, e56, x23 - x34 == 0)
@constraint(m, e57, x24 - x34 == 0)
@constraint(m, e58, x25 - x34 == 0)
@constraint(m, e59, x26 - x34 == 0)
@constraint(m, e60, x27 - x34 == 0)
@constraint(m, e61, x28 - x34 == 0)
@constraint(m, e62, x29 - x34 == 0)
@constraint(m, e63, x30 - x34 == 0)
@constraint(m, e64, x31 - x34 == 0)
@constraint(m, e65, x32 - x34 == 0)
@constraint(m, e66, x33 - x34 == 0)
@constraint(m, e67, x1 + x23 <= 0.5)
@constraint(m, e68, x2 + x24 <= 0.5)
@constraint(m, e69, x3 + x25 <= 0.5)
@constraint(m, e70, x4 + x26 <= 0.5)
@constraint(m, e71, x5 + x27 <= 0.5)
@constraint(m, e72, x6 + x28 <= 0.5)
@constraint(m, e73, x7 + x29 <= 0.5)
@constraint(m, e74, x8 + x30 <= 0.5)
@constraint(m, e75, x9 + x31 <= 0.5)
@constraint(m, e76, x10 + x32 <= 0.5)
@constraint(m, e77, x11 + x33 <= 0.5)
@constraint(m, e78, x1 - x23 >= -0.5)
@constraint(m, e79, x2 - x24 >= -0.5)
@constraint(m, e80, x3 - x25 >= -0.5)
@constraint(m, e81, x4 - x26 >= -0.5)
@constraint(m, e82, x5 - x27 >= -0.5)
@constraint(m, e83, x6 - x28 >= -0.5)
@constraint(m, e84, x7 - x29 >= -0.5)
@constraint(m, e85, x8 - x30 >= -0.5)
@constraint(m, e86, x9 - x31 >= -0.5)
@constraint(m, e87, x10 - x32 >= -0.5)
@constraint(m, e88, x11 - x33 >= -0.5)
@constraint(m, e89, x12 + x23 <= 0.5)
@constraint(m, e90, x13 + x24 <= 0.5)
@constraint(m, e91, x14 + x25 <= 0.5)
@constraint(m, e92, x15 + x26 <= 0.5)
@constraint(m, e93, x16 + x27 <= 0.5)
@constraint(m, e94, x17 + x28 <= 0.5)
@constraint(m, e95, x18 + x29 <= 0.5)
@constraint(m, e96, x19 + x30 <= 0.5)
@constraint(m, e97, x20 + x31 <= 0.5)
@constraint(m, e98, x21 + x32 <= 0.5)
@constraint(m, e99, x22 + x33 <= 0.5)
@constraint(m, e100, x12 - x23 >= -0.5)
@constraint(m, e101, x13 - x24 >= -0.5)
@constraint(m, e102, x14 - x25 >= -0.5)
@constraint(m, e103, x15 - x26 >= -0.5)
@constraint(m, e104, x16 - x27 >= -0.5)
@constraint(m, e105, x17 - x28 >= -0.5)
@constraint(m, e106, x18 - x29 >= -0.5)
@constraint(m, e107, x19 - x30 >= -0.5)
@constraint(m, e108, x20 - x31 >= -0.5)
@constraint(m, e109, x21 - x32 >= -0.5)
@constraint(m, e110, x22 - x33 >= -0.5)
