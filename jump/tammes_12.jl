# NLP written by GAMS Convert at 05/15/24 11:33:54
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#        78       12        0       66        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        37       37        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       498       66      432
#
# Reformulation has removed 1 variable and 1 equation

using JuMP
using MathOptInterface
const MOI = MathOptInterface

model = m = Model()

@variable(m, -1 <= x1 <= 1, start=0)
@variable(m, -1 <= x2 <= 1, start=0)
@variable(m, -1 <= x3 <= 1, start=0)
@variable(m, -1 <= x4 <= 1, start=0)
@variable(m, -1 <= x5 <= 1, start=0)
@variable(m, -1 <= x6 <= 1, start=0)
@variable(m, -1 <= x7 <= 1, start=0)
@variable(m, -1 <= x8 <= 1, start=0)
@variable(m, -1 <= x9 <= 1, start=0)
@variable(m, -1 <= x10 <= 1, start=0)
@variable(m, -1 <= x11 <= 1, start=0)
@variable(m, -1 <= x12 <= 1, start=0)
@variable(m, -1 <= x13 <= 1, start=0)
@variable(m, -1 <= x14 <= 1, start=0)
@variable(m, -1 <= x15 <= 1, start=0)
@variable(m, -1 <= x16 <= 1, start=0)
@variable(m, -1 <= x17 <= 1, start=0)
@variable(m, -1 <= x18 <= 1, start=0)
@variable(m, -1 <= x19 <= 1, start=0)
@variable(m, -1 <= x20 <= 1, start=0)
@variable(m, -1 <= x21 <= 1, start=0)
@variable(m, -1 <= x22 <= 1, start=0)
@variable(m, -1 <= x23 <= 1, start=0)
@variable(m, -1 <= x24 <= 1, start=0)
@variable(m, -1 <= x25 <= 1, start=0)
@variable(m, -1 <= x26 <= 1, start=0)
@variable(m, -1 <= x27 <= 1, start=0)
@variable(m, -1 <= x28 <= 1, start=0)
@variable(m, -1 <= x29 <= 1, start=0)
@variable(m, -1 <= x30 <= 1, start=0)
@variable(m, -1 <= x31 <= 1, start=0)
@variable(m, -1 <= x32 <= 1, start=0)
@variable(m, -1 <= x33 <= 1, start=0)
@variable(m, -1 <= x34 <= 1, start=0)
@variable(m, -1 <= x35 <= 1, start=0)
@variable(m, -1 <= x36 <= 1, start=0)
@variable(m, x37, start=0)

@objective(m, Max, x37)

@NLconstraint(m, e1, x1^2 + x13^2 + x25^2 == 1)
@NLconstraint(m, e2, x2^2 + x14^2 + x26^2 == 1)
@NLconstraint(m, e3, x3^2 + x15^2 + x27^2 == 1)
@NLconstraint(m, e4, x4^2 + x16^2 + x28^2 == 1)
@NLconstraint(m, e5, x5^2 + x17^2 + x29^2 == 1)
@NLconstraint(m, e6, x6^2 + x18^2 + x30^2 == 1)
@NLconstraint(m, e7, x7^2 + x19^2 + x31^2 == 1)
@NLconstraint(m, e8, x8^2 + x20^2 + x32^2 == 1)
@NLconstraint(m, e9, x9^2 + x21^2 + x33^2 == 1)
@NLconstraint(m, e10, x10^2 + x22^2 + x34^2 == 1)
@NLconstraint(m, e11, x11^2 + x23^2 + x35^2 == 1)
@NLconstraint(m, e12, x12^2 + x24^2 + x36^2 == 1)
@NLconstraint(m, e13, -sqrt((x1 - x2)^2 + (x13 - x14)^2 + (x25 - x26)^2) + x37
    <= 0)
@NLconstraint(m, e14, -sqrt((x1 - x3)^2 + (x13 - x15)^2 + (x25 - x27)^2) + x37
    <= 0)
@NLconstraint(m, e15, -sqrt((x1 - x4)^2 + (x13 - x16)^2 + (x25 - x28)^2) + x37
    <= 0)
@NLconstraint(m, e16, -sqrt((x1 - x5)^2 + (x13 - x17)^2 + (x25 - x29)^2) + x37
    <= 0)
@NLconstraint(m, e17, -sqrt((x1 - x6)^2 + (x13 - x18)^2 + (x25 - x30)^2) + x37
    <= 0)
@NLconstraint(m, e18, -sqrt((x1 - x7)^2 + (x13 - x19)^2 + (x25 - x31)^2) + x37
    <= 0)
@NLconstraint(m, e19, -sqrt((x1 - x8)^2 + (x13 - x20)^2 + (x25 - x32)^2) + x37
    <= 0)
@NLconstraint(m, e20, -sqrt((x1 - x9)^2 + (x13 - x21)^2 + (x25 - x33)^2) + x37
    <= 0)
@NLconstraint(m, e21, -sqrt((x1 - x10)^2 + (x13 - x22)^2 + (x25 - x34)^2) + x37
    <= 0)
@NLconstraint(m, e22, -sqrt((x1 - x11)^2 + (x13 - x23)^2 + (x25 - x35)^2) + x37
    <= 0)
@NLconstraint(m, e23, -sqrt((x1 - x12)^2 + (x13 - x24)^2 + (x25 - x36)^2) + x37
    <= 0)
@NLconstraint(m, e24, -sqrt((x2 - x3)^2 + (x14 - x15)^2 + (x26 - x27)^2) + x37
    <= 0)
@NLconstraint(m, e25, -sqrt((x2 - x4)^2 + (x14 - x16)^2 + (x26 - x28)^2) + x37
    <= 0)
@NLconstraint(m, e26, -sqrt((x2 - x5)^2 + (x14 - x17)^2 + (x26 - x29)^2) + x37
    <= 0)
@NLconstraint(m, e27, -sqrt((x2 - x6)^2 + (x14 - x18)^2 + (x26 - x30)^2) + x37
    <= 0)
@NLconstraint(m, e28, -sqrt((x2 - x7)^2 + (x14 - x19)^2 + (x26 - x31)^2) + x37
    <= 0)
@NLconstraint(m, e29, -sqrt((x2 - x8)^2 + (x14 - x20)^2 + (x26 - x32)^2) + x37
    <= 0)
@NLconstraint(m, e30, -sqrt((x2 - x9)^2 + (x14 - x21)^2 + (x26 - x33)^2) + x37
    <= 0)
@NLconstraint(m, e31, -sqrt((x2 - x10)^2 + (x14 - x22)^2 + (x26 - x34)^2) + x37
    <= 0)
@NLconstraint(m, e32, -sqrt((x2 - x11)^2 + (x14 - x23)^2 + (x26 - x35)^2) + x37
    <= 0)
@NLconstraint(m, e33, -sqrt((x2 - x12)^2 + (x14 - x24)^2 + (x26 - x36)^2) + x37
    <= 0)
@NLconstraint(m, e34, -sqrt((x3 - x4)^2 + (x15 - x16)^2 + (x27 - x28)^2) + x37
    <= 0)
@NLconstraint(m, e35, -sqrt((x3 - x5)^2 + (x15 - x17)^2 + (x27 - x29)^2) + x37
    <= 0)
@NLconstraint(m, e36, -sqrt((x3 - x6)^2 + (x15 - x18)^2 + (x27 - x30)^2) + x37
    <= 0)
@NLconstraint(m, e37, -sqrt((x3 - x7)^2 + (x15 - x19)^2 + (x27 - x31)^2) + x37
    <= 0)
@NLconstraint(m, e38, -sqrt((x3 - x8)^2 + (x15 - x20)^2 + (x27 - x32)^2) + x37
    <= 0)
@NLconstraint(m, e39, -sqrt((x3 - x9)^2 + (x15 - x21)^2 + (x27 - x33)^2) + x37
    <= 0)
@NLconstraint(m, e40, -sqrt((x3 - x10)^2 + (x15 - x22)^2 + (x27 - x34)^2) + x37
    <= 0)
@NLconstraint(m, e41, -sqrt((x3 - x11)^2 + (x15 - x23)^2 + (x27 - x35)^2) + x37
    <= 0)
@NLconstraint(m, e42, -sqrt((x3 - x12)^2 + (x15 - x24)^2 + (x27 - x36)^2) + x37
    <= 0)
@NLconstraint(m, e43, -sqrt((x4 - x5)^2 + (x16 - x17)^2 + (x28 - x29)^2) + x37
    <= 0)
@NLconstraint(m, e44, -sqrt((x4 - x6)^2 + (x16 - x18)^2 + (x28 - x30)^2) + x37
    <= 0)
@NLconstraint(m, e45, -sqrt((x4 - x7)^2 + (x16 - x19)^2 + (x28 - x31)^2) + x37
    <= 0)
@NLconstraint(m, e46, -sqrt((x4 - x8)^2 + (x16 - x20)^2 + (x28 - x32)^2) + x37
    <= 0)
@NLconstraint(m, e47, -sqrt((x4 - x9)^2 + (x16 - x21)^2 + (x28 - x33)^2) + x37
    <= 0)
@NLconstraint(m, e48, -sqrt((x4 - x10)^2 + (x16 - x22)^2 + (x28 - x34)^2) + x37
    <= 0)
@NLconstraint(m, e49, -sqrt((x4 - x11)^2 + (x16 - x23)^2 + (x28 - x35)^2) + x37
    <= 0)
@NLconstraint(m, e50, -sqrt((x4 - x12)^2 + (x16 - x24)^2 + (x28 - x36)^2) + x37
    <= 0)
@NLconstraint(m, e51, -sqrt((x5 - x6)^2 + (x17 - x18)^2 + (x29 - x30)^2) + x37
    <= 0)
@NLconstraint(m, e52, -sqrt((x5 - x7)^2 + (x17 - x19)^2 + (x29 - x31)^2) + x37
    <= 0)
@NLconstraint(m, e53, -sqrt((x5 - x8)^2 + (x17 - x20)^2 + (x29 - x32)^2) + x37
    <= 0)
@NLconstraint(m, e54, -sqrt((x5 - x9)^2 + (x17 - x21)^2 + (x29 - x33)^2) + x37
    <= 0)
@NLconstraint(m, e55, -sqrt((x5 - x10)^2 + (x17 - x22)^2 + (x29 - x34)^2) + x37
    <= 0)
@NLconstraint(m, e56, -sqrt((x5 - x11)^2 + (x17 - x23)^2 + (x29 - x35)^2) + x37
    <= 0)
@NLconstraint(m, e57, -sqrt((x5 - x12)^2 + (x17 - x24)^2 + (x29 - x36)^2) + x37
    <= 0)
@NLconstraint(m, e58, -sqrt((x6 - x7)^2 + (x18 - x19)^2 + (x30 - x31)^2) + x37
    <= 0)
@NLconstraint(m, e59, -sqrt((x6 - x8)^2 + (x18 - x20)^2 + (x30 - x32)^2) + x37
    <= 0)
@NLconstraint(m, e60, -sqrt((x6 - x9)^2 + (x18 - x21)^2 + (x30 - x33)^2) + x37
    <= 0)
@NLconstraint(m, e61, -sqrt((x6 - x10)^2 + (x18 - x22)^2 + (x30 - x34)^2) + x37
    <= 0)
@NLconstraint(m, e62, -sqrt((x6 - x11)^2 + (x18 - x23)^2 + (x30 - x35)^2) + x37
    <= 0)
@NLconstraint(m, e63, -sqrt((x6 - x12)^2 + (x18 - x24)^2 + (x30 - x36)^2) + x37
    <= 0)
@NLconstraint(m, e64, -sqrt((x7 - x8)^2 + (x19 - x20)^2 + (x31 - x32)^2) + x37
    <= 0)
@NLconstraint(m, e65, -sqrt((x7 - x9)^2 + (x19 - x21)^2 + (x31 - x33)^2) + x37
    <= 0)
@NLconstraint(m, e66, -sqrt((x7 - x10)^2 + (x19 - x22)^2 + (x31 - x34)^2) + x37
    <= 0)
@NLconstraint(m, e67, -sqrt((x7 - x11)^2 + (x19 - x23)^2 + (x31 - x35)^2) + x37
    <= 0)
@NLconstraint(m, e68, -sqrt((x7 - x12)^2 + (x19 - x24)^2 + (x31 - x36)^2) + x37
    <= 0)
@NLconstraint(m, e69, -sqrt((x8 - x9)^2 + (x20 - x21)^2 + (x32 - x33)^2) + x37
    <= 0)
@NLconstraint(m, e70, -sqrt((x8 - x10)^2 + (x20 - x22)^2 + (x32 - x34)^2) + x37
    <= 0)
@NLconstraint(m, e71, -sqrt((x8 - x11)^2 + (x20 - x23)^2 + (x32 - x35)^2) + x37
    <= 0)
@NLconstraint(m, e72, -sqrt((x8 - x12)^2 + (x20 - x24)^2 + (x32 - x36)^2) + x37
    <= 0)
@NLconstraint(m, e73, -sqrt((x9 - x10)^2 + (x21 - x22)^2 + (x33 - x34)^2) + x37
    <= 0)
@NLconstraint(m, e74, -sqrt((x9 - x11)^2 + (x21 - x23)^2 + (x33 - x35)^2) + x37
    <= 0)
@NLconstraint(m, e75, -sqrt((x9 - x12)^2 + (x21 - x24)^2 + (x33 - x36)^2) + x37
    <= 0)
@NLconstraint(m, e76, -sqrt((x10 - x11)^2 + (x22 - x23)^2 + (x34 - x35)^2) +
    x37 <= 0)
@NLconstraint(m, e77, -sqrt((x10 - x12)^2 + (x22 - x24)^2 + (x34 - x36)^2) +
    x37 <= 0)
@NLconstraint(m, e78, -sqrt((x11 - x12)^2 + (x23 - x24)^2 + (x35 - x36)^2) +
    x37 <= 0)