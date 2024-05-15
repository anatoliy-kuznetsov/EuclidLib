# NLP written by GAMS Convert at 05/15/24 11:27:22
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       105       14        0       91        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        43       43        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       679       91      588
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
@variable(m, -1 <= x37 <= 1, start=0)
@variable(m, -1 <= x38 <= 1, start=0)
@variable(m, -1 <= x39 <= 1, start=0)
@variable(m, -1 <= x40 <= 1, start=0)
@variable(m, -1 <= x41 <= 1, start=0)
@variable(m, -1 <= x42 <= 1, start=0)
@variable(m, x43, start=0)

@objective(m, Max, x43)

@NLconstraint(m, e1, x1^2 + x15^2 + x29^2 == 1)
@NLconstraint(m, e2, x2^2 + x16^2 + x30^2 == 1)
@NLconstraint(m, e3, x3^2 + x17^2 + x31^2 == 1)
@NLconstraint(m, e4, x4^2 + x18^2 + x32^2 == 1)
@NLconstraint(m, e5, x5^2 + x19^2 + x33^2 == 1)
@NLconstraint(m, e6, x6^2 + x20^2 + x34^2 == 1)
@NLconstraint(m, e7, x7^2 + x21^2 + x35^2 == 1)
@NLconstraint(m, e8, x8^2 + x22^2 + x36^2 == 1)
@NLconstraint(m, e9, x9^2 + x23^2 + x37^2 == 1)
@NLconstraint(m, e10, x10^2 + x24^2 + x38^2 == 1)
@NLconstraint(m, e11, x11^2 + x25^2 + x39^2 == 1)
@NLconstraint(m, e12, x12^2 + x26^2 + x40^2 == 1)
@NLconstraint(m, e13, x13^2 + x27^2 + x41^2 == 1)
@NLconstraint(m, e14, x14^2 + x28^2 + x42^2 == 1)
@NLconstraint(m, e15, -sqrt((x1 - x2)^2 + (x15 - x16)^2 + (x29 - x30)^2) + x43
    <= 0)
@NLconstraint(m, e16, -sqrt((x1 - x3)^2 + (x15 - x17)^2 + (x29 - x31)^2) + x43
    <= 0)
@NLconstraint(m, e17, -sqrt((x1 - x4)^2 + (x15 - x18)^2 + (x29 - x32)^2) + x43
    <= 0)
@NLconstraint(m, e18, -sqrt((x1 - x5)^2 + (x15 - x19)^2 + (x29 - x33)^2) + x43
    <= 0)
@NLconstraint(m, e19, -sqrt((x1 - x6)^2 + (x15 - x20)^2 + (x29 - x34)^2) + x43
    <= 0)
@NLconstraint(m, e20, -sqrt((x1 - x7)^2 + (x15 - x21)^2 + (x29 - x35)^2) + x43
    <= 0)
@NLconstraint(m, e21, -sqrt((x1 - x8)^2 + (x15 - x22)^2 + (x29 - x36)^2) + x43
    <= 0)
@NLconstraint(m, e22, -sqrt((x1 - x9)^2 + (x15 - x23)^2 + (x29 - x37)^2) + x43
    <= 0)
@NLconstraint(m, e23, -sqrt((x1 - x10)^2 + (x15 - x24)^2 + (x29 - x38)^2) + x43
    <= 0)
@NLconstraint(m, e24, -sqrt((x1 - x11)^2 + (x15 - x25)^2 + (x29 - x39)^2) + x43
    <= 0)
@NLconstraint(m, e25, -sqrt((x1 - x12)^2 + (x15 - x26)^2 + (x29 - x40)^2) + x43
    <= 0)
@NLconstraint(m, e26, -sqrt((x1 - x13)^2 + (x15 - x27)^2 + (x29 - x41)^2) + x43
    <= 0)
@NLconstraint(m, e27, -sqrt((x1 - x14)^2 + (x15 - x28)^2 + (x29 - x42)^2) + x43
    <= 0)
@NLconstraint(m, e28, -sqrt((x2 - x3)^2 + (x16 - x17)^2 + (x30 - x31)^2) + x43
    <= 0)
@NLconstraint(m, e29, -sqrt((x2 - x4)^2 + (x16 - x18)^2 + (x30 - x32)^2) + x43
    <= 0)
@NLconstraint(m, e30, -sqrt((x2 - x5)^2 + (x16 - x19)^2 + (x30 - x33)^2) + x43
    <= 0)
@NLconstraint(m, e31, -sqrt((x2 - x6)^2 + (x16 - x20)^2 + (x30 - x34)^2) + x43
    <= 0)
@NLconstraint(m, e32, -sqrt((x2 - x7)^2 + (x16 - x21)^2 + (x30 - x35)^2) + x43
    <= 0)
@NLconstraint(m, e33, -sqrt((x2 - x8)^2 + (x16 - x22)^2 + (x30 - x36)^2) + x43
    <= 0)
@NLconstraint(m, e34, -sqrt((x2 - x9)^2 + (x16 - x23)^2 + (x30 - x37)^2) + x43
    <= 0)
@NLconstraint(m, e35, -sqrt((x2 - x10)^2 + (x16 - x24)^2 + (x30 - x38)^2) + x43
    <= 0)
@NLconstraint(m, e36, -sqrt((x2 - x11)^2 + (x16 - x25)^2 + (x30 - x39)^2) + x43
    <= 0)
@NLconstraint(m, e37, -sqrt((x2 - x12)^2 + (x16 - x26)^2 + (x30 - x40)^2) + x43
    <= 0)
@NLconstraint(m, e38, -sqrt((x2 - x13)^2 + (x16 - x27)^2 + (x30 - x41)^2) + x43
    <= 0)
@NLconstraint(m, e39, -sqrt((x2 - x14)^2 + (x16 - x28)^2 + (x30 - x42)^2) + x43
    <= 0)
@NLconstraint(m, e40, -sqrt((x3 - x4)^2 + (x17 - x18)^2 + (x31 - x32)^2) + x43
    <= 0)
@NLconstraint(m, e41, -sqrt((x3 - x5)^2 + (x17 - x19)^2 + (x31 - x33)^2) + x43
    <= 0)
@NLconstraint(m, e42, -sqrt((x3 - x6)^2 + (x17 - x20)^2 + (x31 - x34)^2) + x43
    <= 0)
@NLconstraint(m, e43, -sqrt((x3 - x7)^2 + (x17 - x21)^2 + (x31 - x35)^2) + x43
    <= 0)
@NLconstraint(m, e44, -sqrt((x3 - x8)^2 + (x17 - x22)^2 + (x31 - x36)^2) + x43
    <= 0)
@NLconstraint(m, e45, -sqrt((x3 - x9)^2 + (x17 - x23)^2 + (x31 - x37)^2) + x43
    <= 0)
@NLconstraint(m, e46, -sqrt((x3 - x10)^2 + (x17 - x24)^2 + (x31 - x38)^2) + x43
    <= 0)
@NLconstraint(m, e47, -sqrt((x3 - x11)^2 + (x17 - x25)^2 + (x31 - x39)^2) + x43
    <= 0)
@NLconstraint(m, e48, -sqrt((x3 - x12)^2 + (x17 - x26)^2 + (x31 - x40)^2) + x43
    <= 0)
@NLconstraint(m, e49, -sqrt((x3 - x13)^2 + (x17 - x27)^2 + (x31 - x41)^2) + x43
    <= 0)
@NLconstraint(m, e50, -sqrt((x3 - x14)^2 + (x17 - x28)^2 + (x31 - x42)^2) + x43
    <= 0)
@NLconstraint(m, e51, -sqrt((x4 - x5)^2 + (x18 - x19)^2 + (x32 - x33)^2) + x43
    <= 0)
@NLconstraint(m, e52, -sqrt((x4 - x6)^2 + (x18 - x20)^2 + (x32 - x34)^2) + x43
    <= 0)
@NLconstraint(m, e53, -sqrt((x4 - x7)^2 + (x18 - x21)^2 + (x32 - x35)^2) + x43
    <= 0)
@NLconstraint(m, e54, -sqrt((x4 - x8)^2 + (x18 - x22)^2 + (x32 - x36)^2) + x43
    <= 0)
@NLconstraint(m, e55, -sqrt((x4 - x9)^2 + (x18 - x23)^2 + (x32 - x37)^2) + x43
    <= 0)
@NLconstraint(m, e56, -sqrt((x4 - x10)^2 + (x18 - x24)^2 + (x32 - x38)^2) + x43
    <= 0)
@NLconstraint(m, e57, -sqrt((x4 - x11)^2 + (x18 - x25)^2 + (x32 - x39)^2) + x43
    <= 0)
@NLconstraint(m, e58, -sqrt((x4 - x12)^2 + (x18 - x26)^2 + (x32 - x40)^2) + x43
    <= 0)
@NLconstraint(m, e59, -sqrt((x4 - x13)^2 + (x18 - x27)^2 + (x32 - x41)^2) + x43
    <= 0)
@NLconstraint(m, e60, -sqrt((x4 - x14)^2 + (x18 - x28)^2 + (x32 - x42)^2) + x43
    <= 0)
@NLconstraint(m, e61, -sqrt((x5 - x6)^2 + (x19 - x20)^2 + (x33 - x34)^2) + x43
    <= 0)
@NLconstraint(m, e62, -sqrt((x5 - x7)^2 + (x19 - x21)^2 + (x33 - x35)^2) + x43
    <= 0)
@NLconstraint(m, e63, -sqrt((x5 - x8)^2 + (x19 - x22)^2 + (x33 - x36)^2) + x43
    <= 0)
@NLconstraint(m, e64, -sqrt((x5 - x9)^2 + (x19 - x23)^2 + (x33 - x37)^2) + x43
    <= 0)
@NLconstraint(m, e65, -sqrt((x5 - x10)^2 + (x19 - x24)^2 + (x33 - x38)^2) + x43
    <= 0)
@NLconstraint(m, e66, -sqrt((x5 - x11)^2 + (x19 - x25)^2 + (x33 - x39)^2) + x43
    <= 0)
@NLconstraint(m, e67, -sqrt((x5 - x12)^2 + (x19 - x26)^2 + (x33 - x40)^2) + x43
    <= 0)
@NLconstraint(m, e68, -sqrt((x5 - x13)^2 + (x19 - x27)^2 + (x33 - x41)^2) + x43
    <= 0)
@NLconstraint(m, e69, -sqrt((x5 - x14)^2 + (x19 - x28)^2 + (x33 - x42)^2) + x43
    <= 0)
@NLconstraint(m, e70, -sqrt((x6 - x7)^2 + (x20 - x21)^2 + (x34 - x35)^2) + x43
    <= 0)
@NLconstraint(m, e71, -sqrt((x6 - x8)^2 + (x20 - x22)^2 + (x34 - x36)^2) + x43
    <= 0)
@NLconstraint(m, e72, -sqrt((x6 - x9)^2 + (x20 - x23)^2 + (x34 - x37)^2) + x43
    <= 0)
@NLconstraint(m, e73, -sqrt((x6 - x10)^2 + (x20 - x24)^2 + (x34 - x38)^2) + x43
    <= 0)
@NLconstraint(m, e74, -sqrt((x6 - x11)^2 + (x20 - x25)^2 + (x34 - x39)^2) + x43
    <= 0)
@NLconstraint(m, e75, -sqrt((x6 - x12)^2 + (x20 - x26)^2 + (x34 - x40)^2) + x43
    <= 0)
@NLconstraint(m, e76, -sqrt((x6 - x13)^2 + (x20 - x27)^2 + (x34 - x41)^2) + x43
    <= 0)
@NLconstraint(m, e77, -sqrt((x6 - x14)^2 + (x20 - x28)^2 + (x34 - x42)^2) + x43
    <= 0)
@NLconstraint(m, e78, -sqrt((x7 - x8)^2 + (x21 - x22)^2 + (x35 - x36)^2) + x43
    <= 0)
@NLconstraint(m, e79, -sqrt((x7 - x9)^2 + (x21 - x23)^2 + (x35 - x37)^2) + x43
    <= 0)
@NLconstraint(m, e80, -sqrt((x7 - x10)^2 + (x21 - x24)^2 + (x35 - x38)^2) + x43
    <= 0)
@NLconstraint(m, e81, -sqrt((x7 - x11)^2 + (x21 - x25)^2 + (x35 - x39)^2) + x43
    <= 0)
@NLconstraint(m, e82, -sqrt((x7 - x12)^2 + (x21 - x26)^2 + (x35 - x40)^2) + x43
    <= 0)
@NLconstraint(m, e83, -sqrt((x7 - x13)^2 + (x21 - x27)^2 + (x35 - x41)^2) + x43
    <= 0)
@NLconstraint(m, e84, -sqrt((x7 - x14)^2 + (x21 - x28)^2 + (x35 - x42)^2) + x43
    <= 0)
@NLconstraint(m, e85, -sqrt((x8 - x9)^2 + (x22 - x23)^2 + (x36 - x37)^2) + x43
    <= 0)
@NLconstraint(m, e86, -sqrt((x8 - x10)^2 + (x22 - x24)^2 + (x36 - x38)^2) + x43
    <= 0)
@NLconstraint(m, e87, -sqrt((x8 - x11)^2 + (x22 - x25)^2 + (x36 - x39)^2) + x43
    <= 0)
@NLconstraint(m, e88, -sqrt((x8 - x12)^2 + (x22 - x26)^2 + (x36 - x40)^2) + x43
    <= 0)
@NLconstraint(m, e89, -sqrt((x8 - x13)^2 + (x22 - x27)^2 + (x36 - x41)^2) + x43
    <= 0)
@NLconstraint(m, e90, -sqrt((x8 - x14)^2 + (x22 - x28)^2 + (x36 - x42)^2) + x43
    <= 0)
@NLconstraint(m, e91, -sqrt((x9 - x10)^2 + (x23 - x24)^2 + (x37 - x38)^2) + x43
    <= 0)
@NLconstraint(m, e92, -sqrt((x9 - x11)^2 + (x23 - x25)^2 + (x37 - x39)^2) + x43
    <= 0)
@NLconstraint(m, e93, -sqrt((x9 - x12)^2 + (x23 - x26)^2 + (x37 - x40)^2) + x43
    <= 0)
@NLconstraint(m, e94, -sqrt((x9 - x13)^2 + (x23 - x27)^2 + (x37 - x41)^2) + x43
    <= 0)
@NLconstraint(m, e95, -sqrt((x9 - x14)^2 + (x23 - x28)^2 + (x37 - x42)^2) + x43
    <= 0)
@NLconstraint(m, e96, -sqrt((x10 - x11)^2 + (x24 - x25)^2 + (x38 - x39)^2) +
    x43 <= 0)
@NLconstraint(m, e97, -sqrt((x10 - x12)^2 + (x24 - x26)^2 + (x38 - x40)^2) +
    x43 <= 0)
@NLconstraint(m, e98, -sqrt((x10 - x13)^2 + (x24 - x27)^2 + (x38 - x41)^2) +
    x43 <= 0)
@NLconstraint(m, e99, -sqrt((x10 - x14)^2 + (x24 - x28)^2 + (x38 - x42)^2) +
    x43 <= 0)
@NLconstraint(m, e100, -sqrt((x11 - x12)^2 + (x25 - x26)^2 + (x39 - x40)^2) +
    x43 <= 0)
@NLconstraint(m, e101, -sqrt((x11 - x13)^2 + (x25 - x27)^2 + (x39 - x41)^2) +
    x43 <= 0)
@NLconstraint(m, e102, -sqrt((x11 - x14)^2 + (x25 - x28)^2 + (x39 - x42)^2) +
    x43 <= 0)
@NLconstraint(m, e103, -sqrt((x12 - x13)^2 + (x26 - x27)^2 + (x40 - x41)^2) +
    x43 <= 0)
@NLconstraint(m, e104, -sqrt((x12 - x14)^2 + (x26 - x28)^2 + (x40 - x42)^2) +
    x43 <= 0)
@NLconstraint(m, e105, -sqrt((x13 - x14)^2 + (x27 - x28)^2 + (x41 - x42)^2) +
    x43 <= 0)
