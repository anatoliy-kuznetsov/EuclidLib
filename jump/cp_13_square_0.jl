# NLP written by GAMS Convert at 05/15/24 11:33:37
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       143       13      104       26        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        40       40        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       598      130      468
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
@variable(m, -0.5 <= x23 <= 0.5, start=0)
@variable(m, -0.5 <= x24 <= 0.5, start=0)
@variable(m, -0.5 <= x25 <= 0.5, start=0)
@variable(m, -0.5 <= x26 <= 0.5, start=0)
@variable(m, x27, start=0)
@variable(m, x28, start=0)
@variable(m, x29, start=0)
@variable(m, x30, start=0)
@variable(m, x31, start=0)
@variable(m, x32, start=0)
@variable(m, x33, start=0)
@variable(m, x34, start=0)
@variable(m, x35, start=0)
@variable(m, x36, start=0)
@variable(m, x37, start=0)
@variable(m, x38, start=0)
@variable(m, x39, start=0)
@variable(m, x40, start=0)

@objective(m, Max, x40)

@NLconstraint(m, e1, (x1 - x2)^2 + (x14 - x15)^2 - (x27 + x28)^2 >= 0)
@NLconstraint(m, e2, (x1 - x3)^2 + (x14 - x16)^2 - (x27 + x29)^2 >= 0)
@NLconstraint(m, e3, (x1 - x4)^2 + (x14 - x17)^2 - (x27 + x30)^2 >= 0)
@NLconstraint(m, e4, (x1 - x5)^2 + (x14 - x18)^2 - (x27 + x31)^2 >= 0)
@NLconstraint(m, e5, (x1 - x6)^2 + (x14 - x19)^2 - (x27 + x32)^2 >= 0)
@NLconstraint(m, e6, (x1 - x7)^2 + (x14 - x20)^2 - (x27 + x33)^2 >= 0)
@NLconstraint(m, e7, (x1 - x8)^2 + (x14 - x21)^2 - (x27 + x34)^2 >= 0)
@NLconstraint(m, e8, (x1 - x9)^2 + (x14 - x22)^2 - (x27 + x35)^2 >= 0)
@NLconstraint(m, e9, (x1 - x10)^2 + (x14 - x23)^2 - (x27 + x36)^2 >= 0)
@NLconstraint(m, e10, (x1 - x11)^2 + (x14 - x24)^2 - (x27 + x37)^2 >= 0)
@NLconstraint(m, e11, (x1 - x12)^2 + (x14 - x25)^2 - (x27 + x38)^2 >= 0)
@NLconstraint(m, e12, (x1 - x13)^2 + (x14 - x26)^2 - (x27 + x39)^2 >= 0)
@NLconstraint(m, e13, (x2 - x3)^2 + (x15 - x16)^2 - (x28 + x29)^2 >= 0)
@NLconstraint(m, e14, (x2 - x4)^2 + (x15 - x17)^2 - (x28 + x30)^2 >= 0)
@NLconstraint(m, e15, (x2 - x5)^2 + (x15 - x18)^2 - (x28 + x31)^2 >= 0)
@NLconstraint(m, e16, (x2 - x6)^2 + (x15 - x19)^2 - (x28 + x32)^2 >= 0)
@NLconstraint(m, e17, (x2 - x7)^2 + (x15 - x20)^2 - (x28 + x33)^2 >= 0)
@NLconstraint(m, e18, (x2 - x8)^2 + (x15 - x21)^2 - (x28 + x34)^2 >= 0)
@NLconstraint(m, e19, (x2 - x9)^2 + (x15 - x22)^2 - (x28 + x35)^2 >= 0)
@NLconstraint(m, e20, (x2 - x10)^2 + (x15 - x23)^2 - (x28 + x36)^2 >= 0)
@NLconstraint(m, e21, (x2 - x11)^2 + (x15 - x24)^2 - (x28 + x37)^2 >= 0)
@NLconstraint(m, e22, (x2 - x12)^2 + (x15 - x25)^2 - (x28 + x38)^2 >= 0)
@NLconstraint(m, e23, (x2 - x13)^2 + (x15 - x26)^2 - (x28 + x39)^2 >= 0)
@NLconstraint(m, e24, (x3 - x4)^2 + (x16 - x17)^2 - (x29 + x30)^2 >= 0)
@NLconstraint(m, e25, (x3 - x5)^2 + (x16 - x18)^2 - (x29 + x31)^2 >= 0)
@NLconstraint(m, e26, (x3 - x6)^2 + (x16 - x19)^2 - (x29 + x32)^2 >= 0)
@NLconstraint(m, e27, (x3 - x7)^2 + (x16 - x20)^2 - (x29 + x33)^2 >= 0)
@NLconstraint(m, e28, (x3 - x8)^2 + (x16 - x21)^2 - (x29 + x34)^2 >= 0)
@NLconstraint(m, e29, (x3 - x9)^2 + (x16 - x22)^2 - (x29 + x35)^2 >= 0)
@NLconstraint(m, e30, (x3 - x10)^2 + (x16 - x23)^2 - (x29 + x36)^2 >= 0)
@NLconstraint(m, e31, (x3 - x11)^2 + (x16 - x24)^2 - (x29 + x37)^2 >= 0)
@NLconstraint(m, e32, (x3 - x12)^2 + (x16 - x25)^2 - (x29 + x38)^2 >= 0)
@NLconstraint(m, e33, (x3 - x13)^2 + (x16 - x26)^2 - (x29 + x39)^2 >= 0)
@NLconstraint(m, e34, (x4 - x5)^2 + (x17 - x18)^2 - (x30 + x31)^2 >= 0)
@NLconstraint(m, e35, (x4 - x6)^2 + (x17 - x19)^2 - (x30 + x32)^2 >= 0)
@NLconstraint(m, e36, (x4 - x7)^2 + (x17 - x20)^2 - (x30 + x33)^2 >= 0)
@NLconstraint(m, e37, (x4 - x8)^2 + (x17 - x21)^2 - (x30 + x34)^2 >= 0)
@NLconstraint(m, e38, (x4 - x9)^2 + (x17 - x22)^2 - (x30 + x35)^2 >= 0)
@NLconstraint(m, e39, (x4 - x10)^2 + (x17 - x23)^2 - (x30 + x36)^2 >= 0)
@NLconstraint(m, e40, (x4 - x11)^2 + (x17 - x24)^2 - (x30 + x37)^2 >= 0)
@NLconstraint(m, e41, (x4 - x12)^2 + (x17 - x25)^2 - (x30 + x38)^2 >= 0)
@NLconstraint(m, e42, (x4 - x13)^2 + (x17 - x26)^2 - (x30 + x39)^2 >= 0)
@NLconstraint(m, e43, (x5 - x6)^2 + (x18 - x19)^2 - (x31 + x32)^2 >= 0)
@NLconstraint(m, e44, (x5 - x7)^2 + (x18 - x20)^2 - (x31 + x33)^2 >= 0)
@NLconstraint(m, e45, (x5 - x8)^2 + (x18 - x21)^2 - (x31 + x34)^2 >= 0)
@NLconstraint(m, e46, (x5 - x9)^2 + (x18 - x22)^2 - (x31 + x35)^2 >= 0)
@NLconstraint(m, e47, (x5 - x10)^2 + (x18 - x23)^2 - (x31 + x36)^2 >= 0)
@NLconstraint(m, e48, (x5 - x11)^2 + (x18 - x24)^2 - (x31 + x37)^2 >= 0)
@NLconstraint(m, e49, (x5 - x12)^2 + (x18 - x25)^2 - (x31 + x38)^2 >= 0)
@NLconstraint(m, e50, (x5 - x13)^2 + (x18 - x26)^2 - (x31 + x39)^2 >= 0)
@NLconstraint(m, e51, (x6 - x7)^2 + (x19 - x20)^2 - (x32 + x33)^2 >= 0)
@NLconstraint(m, e52, (x6 - x8)^2 + (x19 - x21)^2 - (x32 + x34)^2 >= 0)
@NLconstraint(m, e53, (x6 - x9)^2 + (x19 - x22)^2 - (x32 + x35)^2 >= 0)
@NLconstraint(m, e54, (x6 - x10)^2 + (x19 - x23)^2 - (x32 + x36)^2 >= 0)
@NLconstraint(m, e55, (x6 - x11)^2 + (x19 - x24)^2 - (x32 + x37)^2 >= 0)
@NLconstraint(m, e56, (x6 - x12)^2 + (x19 - x25)^2 - (x32 + x38)^2 >= 0)
@NLconstraint(m, e57, (x6 - x13)^2 + (x19 - x26)^2 - (x32 + x39)^2 >= 0)
@NLconstraint(m, e58, (x7 - x8)^2 + (x20 - x21)^2 - (x33 + x34)^2 >= 0)
@NLconstraint(m, e59, (x7 - x9)^2 + (x20 - x22)^2 - (x33 + x35)^2 >= 0)
@NLconstraint(m, e60, (x7 - x10)^2 + (x20 - x23)^2 - (x33 + x36)^2 >= 0)
@NLconstraint(m, e61, (x7 - x11)^2 + (x20 - x24)^2 - (x33 + x37)^2 >= 0)
@NLconstraint(m, e62, (x7 - x12)^2 + (x20 - x25)^2 - (x33 + x38)^2 >= 0)
@NLconstraint(m, e63, (x7 - x13)^2 + (x20 - x26)^2 - (x33 + x39)^2 >= 0)
@NLconstraint(m, e64, (x8 - x9)^2 + (x21 - x22)^2 - (x34 + x35)^2 >= 0)
@NLconstraint(m, e65, (x8 - x10)^2 + (x21 - x23)^2 - (x34 + x36)^2 >= 0)
@NLconstraint(m, e66, (x8 - x11)^2 + (x21 - x24)^2 - (x34 + x37)^2 >= 0)
@NLconstraint(m, e67, (x8 - x12)^2 + (x21 - x25)^2 - (x34 + x38)^2 >= 0)
@NLconstraint(m, e68, (x8 - x13)^2 + (x21 - x26)^2 - (x34 + x39)^2 >= 0)
@NLconstraint(m, e69, (x9 - x10)^2 + (x22 - x23)^2 - (x35 + x36)^2 >= 0)
@NLconstraint(m, e70, (x9 - x11)^2 + (x22 - x24)^2 - (x35 + x37)^2 >= 0)
@NLconstraint(m, e71, (x9 - x12)^2 + (x22 - x25)^2 - (x35 + x38)^2 >= 0)
@NLconstraint(m, e72, (x9 - x13)^2 + (x22 - x26)^2 - (x35 + x39)^2 >= 0)
@NLconstraint(m, e73, (x10 - x11)^2 + (x23 - x24)^2 - (x36 + x37)^2 >= 0)
@NLconstraint(m, e74, (x10 - x12)^2 + (x23 - x25)^2 - (x36 + x38)^2 >= 0)
@NLconstraint(m, e75, (x10 - x13)^2 + (x23 - x26)^2 - (x36 + x39)^2 >= 0)
@NLconstraint(m, e76, (x11 - x12)^2 + (x24 - x25)^2 - (x37 + x38)^2 >= 0)
@NLconstraint(m, e77, (x11 - x13)^2 + (x24 - x26)^2 - (x37 + x39)^2 >= 0)
@NLconstraint(m, e78, (x12 - x13)^2 + (x25 - x26)^2 - (x38 + x39)^2 >= 0)
@constraint(m, e79, x27 - x40 == 0)
@constraint(m, e80, x28 - x40 == 0)
@constraint(m, e81, x29 - x40 == 0)
@constraint(m, e82, x30 - x40 == 0)
@constraint(m, e83, x31 - x40 == 0)
@constraint(m, e84, x32 - x40 == 0)
@constraint(m, e85, x33 - x40 == 0)
@constraint(m, e86, x34 - x40 == 0)
@constraint(m, e87, x35 - x40 == 0)
@constraint(m, e88, x36 - x40 == 0)
@constraint(m, e89, x37 - x40 == 0)
@constraint(m, e90, x38 - x40 == 0)
@constraint(m, e91, x39 - x40 == 0)
@constraint(m, e92, x1 + x27 <= 0.5)
@constraint(m, e93, x2 + x28 <= 0.5)
@constraint(m, e94, x3 + x29 <= 0.5)
@constraint(m, e95, x4 + x30 <= 0.5)
@constraint(m, e96, x5 + x31 <= 0.5)
@constraint(m, e97, x6 + x32 <= 0.5)
@constraint(m, e98, x7 + x33 <= 0.5)
@constraint(m, e99, x8 + x34 <= 0.5)
@constraint(m, e100, x9 + x35 <= 0.5)
@constraint(m, e101, x10 + x36 <= 0.5)
@constraint(m, e102, x11 + x37 <= 0.5)
@constraint(m, e103, x12 + x38 <= 0.5)
@constraint(m, e104, x13 + x39 <= 0.5)
@constraint(m, e105, x1 - x27 >= -0.5)
@constraint(m, e106, x2 - x28 >= -0.5)
@constraint(m, e107, x3 - x29 >= -0.5)
@constraint(m, e108, x4 - x30 >= -0.5)
@constraint(m, e109, x5 - x31 >= -0.5)
@constraint(m, e110, x6 - x32 >= -0.5)
@constraint(m, e111, x7 - x33 >= -0.5)
@constraint(m, e112, x8 - x34 >= -0.5)
@constraint(m, e113, x9 - x35 >= -0.5)
@constraint(m, e114, x10 - x36 >= -0.5)
@constraint(m, e115, x11 - x37 >= -0.5)
@constraint(m, e116, x12 - x38 >= -0.5)
@constraint(m, e117, x13 - x39 >= -0.5)
@constraint(m, e118, x14 + x27 <= 0.5)
@constraint(m, e119, x15 + x28 <= 0.5)
@constraint(m, e120, x16 + x29 <= 0.5)
@constraint(m, e121, x17 + x30 <= 0.5)
@constraint(m, e122, x18 + x31 <= 0.5)
@constraint(m, e123, x19 + x32 <= 0.5)
@constraint(m, e124, x20 + x33 <= 0.5)
@constraint(m, e125, x21 + x34 <= 0.5)
@constraint(m, e126, x22 + x35 <= 0.5)
@constraint(m, e127, x23 + x36 <= 0.5)
@constraint(m, e128, x24 + x37 <= 0.5)
@constraint(m, e129, x25 + x38 <= 0.5)
@constraint(m, e130, x26 + x39 <= 0.5)
@constraint(m, e131, x14 - x27 >= -0.5)
@constraint(m, e132, x15 - x28 >= -0.5)
@constraint(m, e133, x16 - x29 >= -0.5)
@constraint(m, e134, x17 - x30 >= -0.5)
@constraint(m, e135, x18 - x31 >= -0.5)
@constraint(m, e136, x19 - x32 >= -0.5)
@constraint(m, e137, x20 - x33 >= -0.5)
@constraint(m, e138, x21 - x34 >= -0.5)
@constraint(m, e139, x22 - x35 >= -0.5)
@constraint(m, e140, x23 - x36 >= -0.5)
@constraint(m, e141, x24 - x37 >= -0.5)
@constraint(m, e142, x25 - x38 >= -0.5)
@constraint(m, e143, x26 - x39 >= -0.5)