# NLP written by GAMS Convert at 05/15/24 11:35:56
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       119       14       91       14        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        43       43        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       616       28      588
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
@variable(m, x41, start=0)
@variable(m, x42, start=0)
@variable(m, x43, start=0)

@objective(m, Max, x43)

@NLconstraint(m, e1, (x1 - x2)^2 + (x15 - x16)^2 - (x29 + x30)^2 >= 0)
@NLconstraint(m, e2, (x1 - x3)^2 + (x15 - x17)^2 - (x29 + x31)^2 >= 0)
@NLconstraint(m, e3, (x1 - x4)^2 + (x15 - x18)^2 - (x29 + x32)^2 >= 0)
@NLconstraint(m, e4, (x1 - x5)^2 + (x15 - x19)^2 - (x29 + x33)^2 >= 0)
@NLconstraint(m, e5, (x1 - x6)^2 + (x15 - x20)^2 - (x29 + x34)^2 >= 0)
@NLconstraint(m, e6, (x1 - x7)^2 + (x15 - x21)^2 - (x29 + x35)^2 >= 0)
@NLconstraint(m, e7, (x1 - x8)^2 + (x15 - x22)^2 - (x29 + x36)^2 >= 0)
@NLconstraint(m, e8, (x1 - x9)^2 + (x15 - x23)^2 - (x29 + x37)^2 >= 0)
@NLconstraint(m, e9, (x1 - x10)^2 + (x15 - x24)^2 - (x29 + x38)^2 >= 0)
@NLconstraint(m, e10, (x1 - x11)^2 + (x15 - x25)^2 - (x29 + x39)^2 >= 0)
@NLconstraint(m, e11, (x1 - x12)^2 + (x15 - x26)^2 - (x29 + x40)^2 >= 0)
@NLconstraint(m, e12, (x1 - x13)^2 + (x15 - x27)^2 - (x29 + x41)^2 >= 0)
@NLconstraint(m, e13, (x1 - x14)^2 + (x15 - x28)^2 - (x29 + x42)^2 >= 0)
@NLconstraint(m, e14, (x2 - x3)^2 + (x16 - x17)^2 - (x30 + x31)^2 >= 0)
@NLconstraint(m, e15, (x2 - x4)^2 + (x16 - x18)^2 - (x30 + x32)^2 >= 0)
@NLconstraint(m, e16, (x2 - x5)^2 + (x16 - x19)^2 - (x30 + x33)^2 >= 0)
@NLconstraint(m, e17, (x2 - x6)^2 + (x16 - x20)^2 - (x30 + x34)^2 >= 0)
@NLconstraint(m, e18, (x2 - x7)^2 + (x16 - x21)^2 - (x30 + x35)^2 >= 0)
@NLconstraint(m, e19, (x2 - x8)^2 + (x16 - x22)^2 - (x30 + x36)^2 >= 0)
@NLconstraint(m, e20, (x2 - x9)^2 + (x16 - x23)^2 - (x30 + x37)^2 >= 0)
@NLconstraint(m, e21, (x2 - x10)^2 + (x16 - x24)^2 - (x30 + x38)^2 >= 0)
@NLconstraint(m, e22, (x2 - x11)^2 + (x16 - x25)^2 - (x30 + x39)^2 >= 0)
@NLconstraint(m, e23, (x2 - x12)^2 + (x16 - x26)^2 - (x30 + x40)^2 >= 0)
@NLconstraint(m, e24, (x2 - x13)^2 + (x16 - x27)^2 - (x30 + x41)^2 >= 0)
@NLconstraint(m, e25, (x2 - x14)^2 + (x16 - x28)^2 - (x30 + x42)^2 >= 0)
@NLconstraint(m, e26, (x3 - x4)^2 + (x17 - x18)^2 - (x31 + x32)^2 >= 0)
@NLconstraint(m, e27, (x3 - x5)^2 + (x17 - x19)^2 - (x31 + x33)^2 >= 0)
@NLconstraint(m, e28, (x3 - x6)^2 + (x17 - x20)^2 - (x31 + x34)^2 >= 0)
@NLconstraint(m, e29, (x3 - x7)^2 + (x17 - x21)^2 - (x31 + x35)^2 >= 0)
@NLconstraint(m, e30, (x3 - x8)^2 + (x17 - x22)^2 - (x31 + x36)^2 >= 0)
@NLconstraint(m, e31, (x3 - x9)^2 + (x17 - x23)^2 - (x31 + x37)^2 >= 0)
@NLconstraint(m, e32, (x3 - x10)^2 + (x17 - x24)^2 - (x31 + x38)^2 >= 0)
@NLconstraint(m, e33, (x3 - x11)^2 + (x17 - x25)^2 - (x31 + x39)^2 >= 0)
@NLconstraint(m, e34, (x3 - x12)^2 + (x17 - x26)^2 - (x31 + x40)^2 >= 0)
@NLconstraint(m, e35, (x3 - x13)^2 + (x17 - x27)^2 - (x31 + x41)^2 >= 0)
@NLconstraint(m, e36, (x3 - x14)^2 + (x17 - x28)^2 - (x31 + x42)^2 >= 0)
@NLconstraint(m, e37, (x4 - x5)^2 + (x18 - x19)^2 - (x32 + x33)^2 >= 0)
@NLconstraint(m, e38, (x4 - x6)^2 + (x18 - x20)^2 - (x32 + x34)^2 >= 0)
@NLconstraint(m, e39, (x4 - x7)^2 + (x18 - x21)^2 - (x32 + x35)^2 >= 0)
@NLconstraint(m, e40, (x4 - x8)^2 + (x18 - x22)^2 - (x32 + x36)^2 >= 0)
@NLconstraint(m, e41, (x4 - x9)^2 + (x18 - x23)^2 - (x32 + x37)^2 >= 0)
@NLconstraint(m, e42, (x4 - x10)^2 + (x18 - x24)^2 - (x32 + x38)^2 >= 0)
@NLconstraint(m, e43, (x4 - x11)^2 + (x18 - x25)^2 - (x32 + x39)^2 >= 0)
@NLconstraint(m, e44, (x4 - x12)^2 + (x18 - x26)^2 - (x32 + x40)^2 >= 0)
@NLconstraint(m, e45, (x4 - x13)^2 + (x18 - x27)^2 - (x32 + x41)^2 >= 0)
@NLconstraint(m, e46, (x4 - x14)^2 + (x18 - x28)^2 - (x32 + x42)^2 >= 0)
@NLconstraint(m, e47, (x5 - x6)^2 + (x19 - x20)^2 - (x33 + x34)^2 >= 0)
@NLconstraint(m, e48, (x5 - x7)^2 + (x19 - x21)^2 - (x33 + x35)^2 >= 0)
@NLconstraint(m, e49, (x5 - x8)^2 + (x19 - x22)^2 - (x33 + x36)^2 >= 0)
@NLconstraint(m, e50, (x5 - x9)^2 + (x19 - x23)^2 - (x33 + x37)^2 >= 0)
@NLconstraint(m, e51, (x5 - x10)^2 + (x19 - x24)^2 - (x33 + x38)^2 >= 0)
@NLconstraint(m, e52, (x5 - x11)^2 + (x19 - x25)^2 - (x33 + x39)^2 >= 0)
@NLconstraint(m, e53, (x5 - x12)^2 + (x19 - x26)^2 - (x33 + x40)^2 >= 0)
@NLconstraint(m, e54, (x5 - x13)^2 + (x19 - x27)^2 - (x33 + x41)^2 >= 0)
@NLconstraint(m, e55, (x5 - x14)^2 + (x19 - x28)^2 - (x33 + x42)^2 >= 0)
@NLconstraint(m, e56, (x6 - x7)^2 + (x20 - x21)^2 - (x34 + x35)^2 >= 0)
@NLconstraint(m, e57, (x6 - x8)^2 + (x20 - x22)^2 - (x34 + x36)^2 >= 0)
@NLconstraint(m, e58, (x6 - x9)^2 + (x20 - x23)^2 - (x34 + x37)^2 >= 0)
@NLconstraint(m, e59, (x6 - x10)^2 + (x20 - x24)^2 - (x34 + x38)^2 >= 0)
@NLconstraint(m, e60, (x6 - x11)^2 + (x20 - x25)^2 - (x34 + x39)^2 >= 0)
@NLconstraint(m, e61, (x6 - x12)^2 + (x20 - x26)^2 - (x34 + x40)^2 >= 0)
@NLconstraint(m, e62, (x6 - x13)^2 + (x20 - x27)^2 - (x34 + x41)^2 >= 0)
@NLconstraint(m, e63, (x6 - x14)^2 + (x20 - x28)^2 - (x34 + x42)^2 >= 0)
@NLconstraint(m, e64, (x7 - x8)^2 + (x21 - x22)^2 - (x35 + x36)^2 >= 0)
@NLconstraint(m, e65, (x7 - x9)^2 + (x21 - x23)^2 - (x35 + x37)^2 >= 0)
@NLconstraint(m, e66, (x7 - x10)^2 + (x21 - x24)^2 - (x35 + x38)^2 >= 0)
@NLconstraint(m, e67, (x7 - x11)^2 + (x21 - x25)^2 - (x35 + x39)^2 >= 0)
@NLconstraint(m, e68, (x7 - x12)^2 + (x21 - x26)^2 - (x35 + x40)^2 >= 0)
@NLconstraint(m, e69, (x7 - x13)^2 + (x21 - x27)^2 - (x35 + x41)^2 >= 0)
@NLconstraint(m, e70, (x7 - x14)^2 + (x21 - x28)^2 - (x35 + x42)^2 >= 0)
@NLconstraint(m, e71, (x8 - x9)^2 + (x22 - x23)^2 - (x36 + x37)^2 >= 0)
@NLconstraint(m, e72, (x8 - x10)^2 + (x22 - x24)^2 - (x36 + x38)^2 >= 0)
@NLconstraint(m, e73, (x8 - x11)^2 + (x22 - x25)^2 - (x36 + x39)^2 >= 0)
@NLconstraint(m, e74, (x8 - x12)^2 + (x22 - x26)^2 - (x36 + x40)^2 >= 0)
@NLconstraint(m, e75, (x8 - x13)^2 + (x22 - x27)^2 - (x36 + x41)^2 >= 0)
@NLconstraint(m, e76, (x8 - x14)^2 + (x22 - x28)^2 - (x36 + x42)^2 >= 0)
@NLconstraint(m, e77, (x9 - x10)^2 + (x23 - x24)^2 - (x37 + x38)^2 >= 0)
@NLconstraint(m, e78, (x9 - x11)^2 + (x23 - x25)^2 - (x37 + x39)^2 >= 0)
@NLconstraint(m, e79, (x9 - x12)^2 + (x23 - x26)^2 - (x37 + x40)^2 >= 0)
@NLconstraint(m, e80, (x9 - x13)^2 + (x23 - x27)^2 - (x37 + x41)^2 >= 0)
@NLconstraint(m, e81, (x9 - x14)^2 + (x23 - x28)^2 - (x37 + x42)^2 >= 0)
@NLconstraint(m, e82, (x10 - x11)^2 + (x24 - x25)^2 - (x38 + x39)^2 >= 0)
@NLconstraint(m, e83, (x10 - x12)^2 + (x24 - x26)^2 - (x38 + x40)^2 >= 0)
@NLconstraint(m, e84, (x10 - x13)^2 + (x24 - x27)^2 - (x38 + x41)^2 >= 0)
@NLconstraint(m, e85, (x10 - x14)^2 + (x24 - x28)^2 - (x38 + x42)^2 >= 0)
@NLconstraint(m, e86, (x11 - x12)^2 + (x25 - x26)^2 - (x39 + x40)^2 >= 0)
@NLconstraint(m, e87, (x11 - x13)^2 + (x25 - x27)^2 - (x39 + x41)^2 >= 0)
@NLconstraint(m, e88, (x11 - x14)^2 + (x25 - x28)^2 - (x39 + x42)^2 >= 0)
@NLconstraint(m, e89, (x12 - x13)^2 + (x26 - x27)^2 - (x40 + x41)^2 >= 0)
@NLconstraint(m, e90, (x12 - x14)^2 + (x26 - x28)^2 - (x40 + x42)^2 >= 0)
@NLconstraint(m, e91, (x13 - x14)^2 + (x27 - x28)^2 - (x41 + x42)^2 >= 0)
@constraint(m, e92, x29 - x43 == 0)
@constraint(m, e93, x30 - 0.7071067811865476 * x43 == 0)
@constraint(m, e94, x31 - 0.5773502691896257 * x43 == 0)
@constraint(m, e95, x32 - 0.5 * x43 == 0)
@constraint(m, e96, x33 - 0.447213595499958 * x43 == 0)
@constraint(m, e97, x34 - 0.408248290463863 * x43 == 0)
@constraint(m, e98, x35 - 0.37796447300922725 * x43 == 0)
@constraint(m, e99, x36 - 0.3535533905932738 * x43 == 0)
@constraint(m, e100, x37 - 0.3333333333333333 * x43 == 0)
@constraint(m, e101, x38 - 0.3162277660168379 * x43 == 0)
@constraint(m, e102, x39 - 0.30151134457776363 * x43 == 0)
@constraint(m, e103, x40 - 0.28867513459481287 * x43 == 0)
@constraint(m, e104, x41 - 0.2773500981126146 * x43 == 0)
@constraint(m, e105, x42 - 0.2672612419124244 * x43 == 0)
@NLconstraint(m, e106, x1^2 + x15^2 - (1 - x29)^2 <= 0)
@NLconstraint(m, e107, x2^2 + x16^2 - (1 - x30)^2 <= 0)
@NLconstraint(m, e108, x3^2 + x17^2 - (1 - x31)^2 <= 0)
@NLconstraint(m, e109, x4^2 + x18^2 - (1 - x32)^2 <= 0)
@NLconstraint(m, e110, x5^2 + x19^2 - (1 - x33)^2 <= 0)
@NLconstraint(m, e111, x6^2 + x20^2 - (1 - x34)^2 <= 0)
@NLconstraint(m, e112, x7^2 + x21^2 - (1 - x35)^2 <= 0)
@NLconstraint(m, e113, x8^2 + x22^2 - (1 - x36)^2 <= 0)
@NLconstraint(m, e114, x9^2 + x23^2 - (1 - x37)^2 <= 0)
@NLconstraint(m, e115, x10^2 + x24^2 - (1 - x38)^2 <= 0)
@NLconstraint(m, e116, x11^2 + x25^2 - (1 - x39)^2 <= 0)
@NLconstraint(m, e117, x12^2 + x26^2 - (1 - x40)^2 <= 0)
@NLconstraint(m, e118, x13^2 + x27^2 - (1 - x41)^2 <= 0)
@NLconstraint(m, e119, x14^2 + x28^2 - (1 - x42)^2 <= 0)
