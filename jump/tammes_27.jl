# NLP written by GAMS Convert at 05/15/24 11:25:02
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       378       27        0      351        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        82       82        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#      2538      351     2187
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
@variable(m, -1 <= x43 <= 1, start=0)
@variable(m, -1 <= x44 <= 1, start=0)
@variable(m, -1 <= x45 <= 1, start=0)
@variable(m, -1 <= x46 <= 1, start=0)
@variable(m, -1 <= x47 <= 1, start=0)
@variable(m, -1 <= x48 <= 1, start=0)
@variable(m, -1 <= x49 <= 1, start=0)
@variable(m, -1 <= x50 <= 1, start=0)
@variable(m, -1 <= x51 <= 1, start=0)
@variable(m, -1 <= x52 <= 1, start=0)
@variable(m, -1 <= x53 <= 1, start=0)
@variable(m, -1 <= x54 <= 1, start=0)
@variable(m, -1 <= x55 <= 1, start=0)
@variable(m, -1 <= x56 <= 1, start=0)
@variable(m, -1 <= x57 <= 1, start=0)
@variable(m, -1 <= x58 <= 1, start=0)
@variable(m, -1 <= x59 <= 1, start=0)
@variable(m, -1 <= x60 <= 1, start=0)
@variable(m, -1 <= x61 <= 1, start=0)
@variable(m, -1 <= x62 <= 1, start=0)
@variable(m, -1 <= x63 <= 1, start=0)
@variable(m, -1 <= x64 <= 1, start=0)
@variable(m, -1 <= x65 <= 1, start=0)
@variable(m, -1 <= x66 <= 1, start=0)
@variable(m, -1 <= x67 <= 1, start=0)
@variable(m, -1 <= x68 <= 1, start=0)
@variable(m, -1 <= x69 <= 1, start=0)
@variable(m, -1 <= x70 <= 1, start=0)
@variable(m, -1 <= x71 <= 1, start=0)
@variable(m, -1 <= x72 <= 1, start=0)
@variable(m, -1 <= x73 <= 1, start=0)
@variable(m, -1 <= x74 <= 1, start=0)
@variable(m, -1 <= x75 <= 1, start=0)
@variable(m, -1 <= x76 <= 1, start=0)
@variable(m, -1 <= x77 <= 1, start=0)
@variable(m, -1 <= x78 <= 1, start=0)
@variable(m, -1 <= x79 <= 1, start=0)
@variable(m, -1 <= x80 <= 1, start=0)
@variable(m, -1 <= x81 <= 1, start=0)
@variable(m, x82, start=0)

@objective(m, Max, x82)

@NLconstraint(m, e1, x1^2 + x28^2 + x55^2 == 1)
@NLconstraint(m, e2, x2^2 + x29^2 + x56^2 == 1)
@NLconstraint(m, e3, x3^2 + x30^2 + x57^2 == 1)
@NLconstraint(m, e4, x4^2 + x31^2 + x58^2 == 1)
@NLconstraint(m, e5, x5^2 + x32^2 + x59^2 == 1)
@NLconstraint(m, e6, x6^2 + x33^2 + x60^2 == 1)
@NLconstraint(m, e7, x7^2 + x34^2 + x61^2 == 1)
@NLconstraint(m, e8, x8^2 + x35^2 + x62^2 == 1)
@NLconstraint(m, e9, x9^2 + x36^2 + x63^2 == 1)
@NLconstraint(m, e10, x10^2 + x37^2 + x64^2 == 1)
@NLconstraint(m, e11, x11^2 + x38^2 + x65^2 == 1)
@NLconstraint(m, e12, x12^2 + x39^2 + x66^2 == 1)
@NLconstraint(m, e13, x13^2 + x40^2 + x67^2 == 1)
@NLconstraint(m, e14, x14^2 + x41^2 + x68^2 == 1)
@NLconstraint(m, e15, x15^2 + x42^2 + x69^2 == 1)
@NLconstraint(m, e16, x16^2 + x43^2 + x70^2 == 1)
@NLconstraint(m, e17, x17^2 + x44^2 + x71^2 == 1)
@NLconstraint(m, e18, x18^2 + x45^2 + x72^2 == 1)
@NLconstraint(m, e19, x19^2 + x46^2 + x73^2 == 1)
@NLconstraint(m, e20, x20^2 + x47^2 + x74^2 == 1)
@NLconstraint(m, e21, x21^2 + x48^2 + x75^2 == 1)
@NLconstraint(m, e22, x22^2 + x49^2 + x76^2 == 1)
@NLconstraint(m, e23, x23^2 + x50^2 + x77^2 == 1)
@NLconstraint(m, e24, x24^2 + x51^2 + x78^2 == 1)
@NLconstraint(m, e25, x25^2 + x52^2 + x79^2 == 1)
@NLconstraint(m, e26, x26^2 + x53^2 + x80^2 == 1)
@NLconstraint(m, e27, x27^2 + x54^2 + x81^2 == 1)
@NLconstraint(m, e28, -sqrt((x1 - x2)^2 + (x28 - x29)^2 + (x55 - x56)^2) + x82
    <= 0)
@NLconstraint(m, e29, -sqrt((x1 - x3)^2 + (x28 - x30)^2 + (x55 - x57)^2) + x82
    <= 0)
@NLconstraint(m, e30, -sqrt((x1 - x4)^2 + (x28 - x31)^2 + (x55 - x58)^2) + x82
    <= 0)
@NLconstraint(m, e31, -sqrt((x1 - x5)^2 + (x28 - x32)^2 + (x55 - x59)^2) + x82
    <= 0)
@NLconstraint(m, e32, -sqrt((x1 - x6)^2 + (x28 - x33)^2 + (x55 - x60)^2) + x82
    <= 0)
@NLconstraint(m, e33, -sqrt((x1 - x7)^2 + (x28 - x34)^2 + (x55 - x61)^2) + x82
    <= 0)
@NLconstraint(m, e34, -sqrt((x1 - x8)^2 + (x28 - x35)^2 + (x55 - x62)^2) + x82
    <= 0)
@NLconstraint(m, e35, -sqrt((x1 - x9)^2 + (x28 - x36)^2 + (x55 - x63)^2) + x82
    <= 0)
@NLconstraint(m, e36, -sqrt((x1 - x10)^2 + (x28 - x37)^2 + (x55 - x64)^2) + x82
    <= 0)
@NLconstraint(m, e37, -sqrt((x1 - x11)^2 + (x28 - x38)^2 + (x55 - x65)^2) + x82
    <= 0)
@NLconstraint(m, e38, -sqrt((x1 - x12)^2 + (x28 - x39)^2 + (x55 - x66)^2) + x82
    <= 0)
@NLconstraint(m, e39, -sqrt((x1 - x13)^2 + (x28 - x40)^2 + (x55 - x67)^2) + x82
    <= 0)
@NLconstraint(m, e40, -sqrt((x1 - x14)^2 + (x28 - x41)^2 + (x55 - x68)^2) + x82
    <= 0)
@NLconstraint(m, e41, -sqrt((x1 - x15)^2 + (x28 - x42)^2 + (x55 - x69)^2) + x82
    <= 0)
@NLconstraint(m, e42, -sqrt((x1 - x16)^2 + (x28 - x43)^2 + (x55 - x70)^2) + x82
    <= 0)
@NLconstraint(m, e43, -sqrt((x1 - x17)^2 + (x28 - x44)^2 + (x55 - x71)^2) + x82
    <= 0)
@NLconstraint(m, e44, -sqrt((x1 - x18)^2 + (x28 - x45)^2 + (x55 - x72)^2) + x82
    <= 0)
@NLconstraint(m, e45, -sqrt((x1 - x19)^2 + (x28 - x46)^2 + (x55 - x73)^2) + x82
    <= 0)
@NLconstraint(m, e46, -sqrt((x1 - x20)^2 + (x28 - x47)^2 + (x55 - x74)^2) + x82
    <= 0)
@NLconstraint(m, e47, -sqrt((x1 - x21)^2 + (x28 - x48)^2 + (x55 - x75)^2) + x82
    <= 0)
@NLconstraint(m, e48, -sqrt((x1 - x22)^2 + (x28 - x49)^2 + (x55 - x76)^2) + x82
    <= 0)
@NLconstraint(m, e49, -sqrt((x1 - x23)^2 + (x28 - x50)^2 + (x55 - x77)^2) + x82
    <= 0)
@NLconstraint(m, e50, -sqrt((x1 - x24)^2 + (x28 - x51)^2 + (x55 - x78)^2) + x82
    <= 0)
@NLconstraint(m, e51, -sqrt((x1 - x25)^2 + (x28 - x52)^2 + (x55 - x79)^2) + x82
    <= 0)
@NLconstraint(m, e52, -sqrt((x1 - x26)^2 + (x28 - x53)^2 + (x55 - x80)^2) + x82
    <= 0)
@NLconstraint(m, e53, -sqrt((x1 - x27)^2 + (x28 - x54)^2 + (x55 - x81)^2) + x82
    <= 0)
@NLconstraint(m, e54, -sqrt((x2 - x3)^2 + (x29 - x30)^2 + (x56 - x57)^2) + x82
    <= 0)
@NLconstraint(m, e55, -sqrt((x2 - x4)^2 + (x29 - x31)^2 + (x56 - x58)^2) + x82
    <= 0)
@NLconstraint(m, e56, -sqrt((x2 - x5)^2 + (x29 - x32)^2 + (x56 - x59)^2) + x82
    <= 0)
@NLconstraint(m, e57, -sqrt((x2 - x6)^2 + (x29 - x33)^2 + (x56 - x60)^2) + x82
    <= 0)
@NLconstraint(m, e58, -sqrt((x2 - x7)^2 + (x29 - x34)^2 + (x56 - x61)^2) + x82
    <= 0)
@NLconstraint(m, e59, -sqrt((x2 - x8)^2 + (x29 - x35)^2 + (x56 - x62)^2) + x82
    <= 0)
@NLconstraint(m, e60, -sqrt((x2 - x9)^2 + (x29 - x36)^2 + (x56 - x63)^2) + x82
    <= 0)
@NLconstraint(m, e61, -sqrt((x2 - x10)^2 + (x29 - x37)^2 + (x56 - x64)^2) + x82
    <= 0)
@NLconstraint(m, e62, -sqrt((x2 - x11)^2 + (x29 - x38)^2 + (x56 - x65)^2) + x82
    <= 0)
@NLconstraint(m, e63, -sqrt((x2 - x12)^2 + (x29 - x39)^2 + (x56 - x66)^2) + x82
    <= 0)
@NLconstraint(m, e64, -sqrt((x2 - x13)^2 + (x29 - x40)^2 + (x56 - x67)^2) + x82
    <= 0)
@NLconstraint(m, e65, -sqrt((x2 - x14)^2 + (x29 - x41)^2 + (x56 - x68)^2) + x82
    <= 0)
@NLconstraint(m, e66, -sqrt((x2 - x15)^2 + (x29 - x42)^2 + (x56 - x69)^2) + x82
    <= 0)
@NLconstraint(m, e67, -sqrt((x2 - x16)^2 + (x29 - x43)^2 + (x56 - x70)^2) + x82
    <= 0)
@NLconstraint(m, e68, -sqrt((x2 - x17)^2 + (x29 - x44)^2 + (x56 - x71)^2) + x82
    <= 0)
@NLconstraint(m, e69, -sqrt((x2 - x18)^2 + (x29 - x45)^2 + (x56 - x72)^2) + x82
    <= 0)
@NLconstraint(m, e70, -sqrt((x2 - x19)^2 + (x29 - x46)^2 + (x56 - x73)^2) + x82
    <= 0)
@NLconstraint(m, e71, -sqrt((x2 - x20)^2 + (x29 - x47)^2 + (x56 - x74)^2) + x82
    <= 0)
@NLconstraint(m, e72, -sqrt((x2 - x21)^2 + (x29 - x48)^2 + (x56 - x75)^2) + x82
    <= 0)
@NLconstraint(m, e73, -sqrt((x2 - x22)^2 + (x29 - x49)^2 + (x56 - x76)^2) + x82
    <= 0)
@NLconstraint(m, e74, -sqrt((x2 - x23)^2 + (x29 - x50)^2 + (x56 - x77)^2) + x82
    <= 0)
@NLconstraint(m, e75, -sqrt((x2 - x24)^2 + (x29 - x51)^2 + (x56 - x78)^2) + x82
    <= 0)
@NLconstraint(m, e76, -sqrt((x2 - x25)^2 + (x29 - x52)^2 + (x56 - x79)^2) + x82
    <= 0)
@NLconstraint(m, e77, -sqrt((x2 - x26)^2 + (x29 - x53)^2 + (x56 - x80)^2) + x82
    <= 0)
@NLconstraint(m, e78, -sqrt((x2 - x27)^2 + (x29 - x54)^2 + (x56 - x81)^2) + x82
    <= 0)
@NLconstraint(m, e79, -sqrt((x3 - x4)^2 + (x30 - x31)^2 + (x57 - x58)^2) + x82
    <= 0)
@NLconstraint(m, e80, -sqrt((x3 - x5)^2 + (x30 - x32)^2 + (x57 - x59)^2) + x82
    <= 0)
@NLconstraint(m, e81, -sqrt((x3 - x6)^2 + (x30 - x33)^2 + (x57 - x60)^2) + x82
    <= 0)
@NLconstraint(m, e82, -sqrt((x3 - x7)^2 + (x30 - x34)^2 + (x57 - x61)^2) + x82
    <= 0)
@NLconstraint(m, e83, -sqrt((x3 - x8)^2 + (x30 - x35)^2 + (x57 - x62)^2) + x82
    <= 0)
@NLconstraint(m, e84, -sqrt((x3 - x9)^2 + (x30 - x36)^2 + (x57 - x63)^2) + x82
    <= 0)
@NLconstraint(m, e85, -sqrt((x3 - x10)^2 + (x30 - x37)^2 + (x57 - x64)^2) + x82
    <= 0)
@NLconstraint(m, e86, -sqrt((x3 - x11)^2 + (x30 - x38)^2 + (x57 - x65)^2) + x82
    <= 0)
@NLconstraint(m, e87, -sqrt((x3 - x12)^2 + (x30 - x39)^2 + (x57 - x66)^2) + x82
    <= 0)
@NLconstraint(m, e88, -sqrt((x3 - x13)^2 + (x30 - x40)^2 + (x57 - x67)^2) + x82
    <= 0)
@NLconstraint(m, e89, -sqrt((x3 - x14)^2 + (x30 - x41)^2 + (x57 - x68)^2) + x82
    <= 0)
@NLconstraint(m, e90, -sqrt((x3 - x15)^2 + (x30 - x42)^2 + (x57 - x69)^2) + x82
    <= 0)
@NLconstraint(m, e91, -sqrt((x3 - x16)^2 + (x30 - x43)^2 + (x57 - x70)^2) + x82
    <= 0)
@NLconstraint(m, e92, -sqrt((x3 - x17)^2 + (x30 - x44)^2 + (x57 - x71)^2) + x82
    <= 0)
@NLconstraint(m, e93, -sqrt((x3 - x18)^2 + (x30 - x45)^2 + (x57 - x72)^2) + x82
    <= 0)
@NLconstraint(m, e94, -sqrt((x3 - x19)^2 + (x30 - x46)^2 + (x57 - x73)^2) + x82
    <= 0)
@NLconstraint(m, e95, -sqrt((x3 - x20)^2 + (x30 - x47)^2 + (x57 - x74)^2) + x82
    <= 0)
@NLconstraint(m, e96, -sqrt((x3 - x21)^2 + (x30 - x48)^2 + (x57 - x75)^2) + x82
    <= 0)
@NLconstraint(m, e97, -sqrt((x3 - x22)^2 + (x30 - x49)^2 + (x57 - x76)^2) + x82
    <= 0)
@NLconstraint(m, e98, -sqrt((x3 - x23)^2 + (x30 - x50)^2 + (x57 - x77)^2) + x82
    <= 0)
@NLconstraint(m, e99, -sqrt((x3 - x24)^2 + (x30 - x51)^2 + (x57 - x78)^2) + x82
    <= 0)
@NLconstraint(m, e100, -sqrt((x3 - x25)^2 + (x30 - x52)^2 + (x57 - x79)^2) +
    x82 <= 0)
@NLconstraint(m, e101, -sqrt((x3 - x26)^2 + (x30 - x53)^2 + (x57 - x80)^2) +
    x82 <= 0)
@NLconstraint(m, e102, -sqrt((x3 - x27)^2 + (x30 - x54)^2 + (x57 - x81)^2) +
    x82 <= 0)
@NLconstraint(m, e103, -sqrt((x4 - x5)^2 + (x31 - x32)^2 + (x58 - x59)^2) + x82
    <= 0)
@NLconstraint(m, e104, -sqrt((x4 - x6)^2 + (x31 - x33)^2 + (x58 - x60)^2) + x82
    <= 0)
@NLconstraint(m, e105, -sqrt((x4 - x7)^2 + (x31 - x34)^2 + (x58 - x61)^2) + x82
    <= 0)
@NLconstraint(m, e106, -sqrt((x4 - x8)^2 + (x31 - x35)^2 + (x58 - x62)^2) + x82
    <= 0)
@NLconstraint(m, e107, -sqrt((x4 - x9)^2 + (x31 - x36)^2 + (x58 - x63)^2) + x82
    <= 0)
@NLconstraint(m, e108, -sqrt((x4 - x10)^2 + (x31 - x37)^2 + (x58 - x64)^2) +
    x82 <= 0)
@NLconstraint(m, e109, -sqrt((x4 - x11)^2 + (x31 - x38)^2 + (x58 - x65)^2) +
    x82 <= 0)
@NLconstraint(m, e110, -sqrt((x4 - x12)^2 + (x31 - x39)^2 + (x58 - x66)^2) +
    x82 <= 0)
@NLconstraint(m, e111, -sqrt((x4 - x13)^2 + (x31 - x40)^2 + (x58 - x67)^2) +
    x82 <= 0)
@NLconstraint(m, e112, -sqrt((x4 - x14)^2 + (x31 - x41)^2 + (x58 - x68)^2) +
    x82 <= 0)
@NLconstraint(m, e113, -sqrt((x4 - x15)^2 + (x31 - x42)^2 + (x58 - x69)^2) +
    x82 <= 0)
@NLconstraint(m, e114, -sqrt((x4 - x16)^2 + (x31 - x43)^2 + (x58 - x70)^2) +
    x82 <= 0)
@NLconstraint(m, e115, -sqrt((x4 - x17)^2 + (x31 - x44)^2 + (x58 - x71)^2) +
    x82 <= 0)
@NLconstraint(m, e116, -sqrt((x4 - x18)^2 + (x31 - x45)^2 + (x58 - x72)^2) +
    x82 <= 0)
@NLconstraint(m, e117, -sqrt((x4 - x19)^2 + (x31 - x46)^2 + (x58 - x73)^2) +
    x82 <= 0)
@NLconstraint(m, e118, -sqrt((x4 - x20)^2 + (x31 - x47)^2 + (x58 - x74)^2) +
    x82 <= 0)
@NLconstraint(m, e119, -sqrt((x4 - x21)^2 + (x31 - x48)^2 + (x58 - x75)^2) +
    x82 <= 0)
@NLconstraint(m, e120, -sqrt((x4 - x22)^2 + (x31 - x49)^2 + (x58 - x76)^2) +
    x82 <= 0)
@NLconstraint(m, e121, -sqrt((x4 - x23)^2 + (x31 - x50)^2 + (x58 - x77)^2) +
    x82 <= 0)
@NLconstraint(m, e122, -sqrt((x4 - x24)^2 + (x31 - x51)^2 + (x58 - x78)^2) +
    x82 <= 0)
@NLconstraint(m, e123, -sqrt((x4 - x25)^2 + (x31 - x52)^2 + (x58 - x79)^2) +
    x82 <= 0)
@NLconstraint(m, e124, -sqrt((x4 - x26)^2 + (x31 - x53)^2 + (x58 - x80)^2) +
    x82 <= 0)
@NLconstraint(m, e125, -sqrt((x4 - x27)^2 + (x31 - x54)^2 + (x58 - x81)^2) +
    x82 <= 0)
@NLconstraint(m, e126, -sqrt((x5 - x6)^2 + (x32 - x33)^2 + (x59 - x60)^2) + x82
    <= 0)
@NLconstraint(m, e127, -sqrt((x5 - x7)^2 + (x32 - x34)^2 + (x59 - x61)^2) + x82
    <= 0)
@NLconstraint(m, e128, -sqrt((x5 - x8)^2 + (x32 - x35)^2 + (x59 - x62)^2) + x82
    <= 0)
@NLconstraint(m, e129, -sqrt((x5 - x9)^2 + (x32 - x36)^2 + (x59 - x63)^2) + x82
    <= 0)
@NLconstraint(m, e130, -sqrt((x5 - x10)^2 + (x32 - x37)^2 + (x59 - x64)^2) +
    x82 <= 0)
@NLconstraint(m, e131, -sqrt((x5 - x11)^2 + (x32 - x38)^2 + (x59 - x65)^2) +
    x82 <= 0)
@NLconstraint(m, e132, -sqrt((x5 - x12)^2 + (x32 - x39)^2 + (x59 - x66)^2) +
    x82 <= 0)
@NLconstraint(m, e133, -sqrt((x5 - x13)^2 + (x32 - x40)^2 + (x59 - x67)^2) +
    x82 <= 0)
@NLconstraint(m, e134, -sqrt((x5 - x14)^2 + (x32 - x41)^2 + (x59 - x68)^2) +
    x82 <= 0)
@NLconstraint(m, e135, -sqrt((x5 - x15)^2 + (x32 - x42)^2 + (x59 - x69)^2) +
    x82 <= 0)
@NLconstraint(m, e136, -sqrt((x5 - x16)^2 + (x32 - x43)^2 + (x59 - x70)^2) +
    x82 <= 0)
@NLconstraint(m, e137, -sqrt((x5 - x17)^2 + (x32 - x44)^2 + (x59 - x71)^2) +
    x82 <= 0)
@NLconstraint(m, e138, -sqrt((x5 - x18)^2 + (x32 - x45)^2 + (x59 - x72)^2) +
    x82 <= 0)
@NLconstraint(m, e139, -sqrt((x5 - x19)^2 + (x32 - x46)^2 + (x59 - x73)^2) +
    x82 <= 0)
@NLconstraint(m, e140, -sqrt((x5 - x20)^2 + (x32 - x47)^2 + (x59 - x74)^2) +
    x82 <= 0)
@NLconstraint(m, e141, -sqrt((x5 - x21)^2 + (x32 - x48)^2 + (x59 - x75)^2) +
    x82 <= 0)
@NLconstraint(m, e142, -sqrt((x5 - x22)^2 + (x32 - x49)^2 + (x59 - x76)^2) +
    x82 <= 0)
@NLconstraint(m, e143, -sqrt((x5 - x23)^2 + (x32 - x50)^2 + (x59 - x77)^2) +
    x82 <= 0)
@NLconstraint(m, e144, -sqrt((x5 - x24)^2 + (x32 - x51)^2 + (x59 - x78)^2) +
    x82 <= 0)
@NLconstraint(m, e145, -sqrt((x5 - x25)^2 + (x32 - x52)^2 + (x59 - x79)^2) +
    x82 <= 0)
@NLconstraint(m, e146, -sqrt((x5 - x26)^2 + (x32 - x53)^2 + (x59 - x80)^2) +
    x82 <= 0)
@NLconstraint(m, e147, -sqrt((x5 - x27)^2 + (x32 - x54)^2 + (x59 - x81)^2) +
    x82 <= 0)
@NLconstraint(m, e148, -sqrt((x6 - x7)^2 + (x33 - x34)^2 + (x60 - x61)^2) + x82
    <= 0)
@NLconstraint(m, e149, -sqrt((x6 - x8)^2 + (x33 - x35)^2 + (x60 - x62)^2) + x82
    <= 0)
@NLconstraint(m, e150, -sqrt((x6 - x9)^2 + (x33 - x36)^2 + (x60 - x63)^2) + x82
    <= 0)
@NLconstraint(m, e151, -sqrt((x6 - x10)^2 + (x33 - x37)^2 + (x60 - x64)^2) +
    x82 <= 0)
@NLconstraint(m, e152, -sqrt((x6 - x11)^2 + (x33 - x38)^2 + (x60 - x65)^2) +
    x82 <= 0)
@NLconstraint(m, e153, -sqrt((x6 - x12)^2 + (x33 - x39)^2 + (x60 - x66)^2) +
    x82 <= 0)
@NLconstraint(m, e154, -sqrt((x6 - x13)^2 + (x33 - x40)^2 + (x60 - x67)^2) +
    x82 <= 0)
@NLconstraint(m, e155, -sqrt((x6 - x14)^2 + (x33 - x41)^2 + (x60 - x68)^2) +
    x82 <= 0)
@NLconstraint(m, e156, -sqrt((x6 - x15)^2 + (x33 - x42)^2 + (x60 - x69)^2) +
    x82 <= 0)
@NLconstraint(m, e157, -sqrt((x6 - x16)^2 + (x33 - x43)^2 + (x60 - x70)^2) +
    x82 <= 0)
@NLconstraint(m, e158, -sqrt((x6 - x17)^2 + (x33 - x44)^2 + (x60 - x71)^2) +
    x82 <= 0)
@NLconstraint(m, e159, -sqrt((x6 - x18)^2 + (x33 - x45)^2 + (x60 - x72)^2) +
    x82 <= 0)
@NLconstraint(m, e160, -sqrt((x6 - x19)^2 + (x33 - x46)^2 + (x60 - x73)^2) +
    x82 <= 0)
@NLconstraint(m, e161, -sqrt((x6 - x20)^2 + (x33 - x47)^2 + (x60 - x74)^2) +
    x82 <= 0)
@NLconstraint(m, e162, -sqrt((x6 - x21)^2 + (x33 - x48)^2 + (x60 - x75)^2) +
    x82 <= 0)
@NLconstraint(m, e163, -sqrt((x6 - x22)^2 + (x33 - x49)^2 + (x60 - x76)^2) +
    x82 <= 0)
@NLconstraint(m, e164, -sqrt((x6 - x23)^2 + (x33 - x50)^2 + (x60 - x77)^2) +
    x82 <= 0)
@NLconstraint(m, e165, -sqrt((x6 - x24)^2 + (x33 - x51)^2 + (x60 - x78)^2) +
    x82 <= 0)
@NLconstraint(m, e166, -sqrt((x6 - x25)^2 + (x33 - x52)^2 + (x60 - x79)^2) +
    x82 <= 0)
@NLconstraint(m, e167, -sqrt((x6 - x26)^2 + (x33 - x53)^2 + (x60 - x80)^2) +
    x82 <= 0)
@NLconstraint(m, e168, -sqrt((x6 - x27)^2 + (x33 - x54)^2 + (x60 - x81)^2) +
    x82 <= 0)
@NLconstraint(m, e169, -sqrt((x7 - x8)^2 + (x34 - x35)^2 + (x61 - x62)^2) + x82
    <= 0)
@NLconstraint(m, e170, -sqrt((x7 - x9)^2 + (x34 - x36)^2 + (x61 - x63)^2) + x82
    <= 0)
@NLconstraint(m, e171, -sqrt((x7 - x10)^2 + (x34 - x37)^2 + (x61 - x64)^2) +
    x82 <= 0)
@NLconstraint(m, e172, -sqrt((x7 - x11)^2 + (x34 - x38)^2 + (x61 - x65)^2) +
    x82 <= 0)
@NLconstraint(m, e173, -sqrt((x7 - x12)^2 + (x34 - x39)^2 + (x61 - x66)^2) +
    x82 <= 0)
@NLconstraint(m, e174, -sqrt((x7 - x13)^2 + (x34 - x40)^2 + (x61 - x67)^2) +
    x82 <= 0)
@NLconstraint(m, e175, -sqrt((x7 - x14)^2 + (x34 - x41)^2 + (x61 - x68)^2) +
    x82 <= 0)
@NLconstraint(m, e176, -sqrt((x7 - x15)^2 + (x34 - x42)^2 + (x61 - x69)^2) +
    x82 <= 0)
@NLconstraint(m, e177, -sqrt((x7 - x16)^2 + (x34 - x43)^2 + (x61 - x70)^2) +
    x82 <= 0)
@NLconstraint(m, e178, -sqrt((x7 - x17)^2 + (x34 - x44)^2 + (x61 - x71)^2) +
    x82 <= 0)
@NLconstraint(m, e179, -sqrt((x7 - x18)^2 + (x34 - x45)^2 + (x61 - x72)^2) +
    x82 <= 0)
@NLconstraint(m, e180, -sqrt((x7 - x19)^2 + (x34 - x46)^2 + (x61 - x73)^2) +
    x82 <= 0)
@NLconstraint(m, e181, -sqrt((x7 - x20)^2 + (x34 - x47)^2 + (x61 - x74)^2) +
    x82 <= 0)
@NLconstraint(m, e182, -sqrt((x7 - x21)^2 + (x34 - x48)^2 + (x61 - x75)^2) +
    x82 <= 0)
@NLconstraint(m, e183, -sqrt((x7 - x22)^2 + (x34 - x49)^2 + (x61 - x76)^2) +
    x82 <= 0)
@NLconstraint(m, e184, -sqrt((x7 - x23)^2 + (x34 - x50)^2 + (x61 - x77)^2) +
    x82 <= 0)
@NLconstraint(m, e185, -sqrt((x7 - x24)^2 + (x34 - x51)^2 + (x61 - x78)^2) +
    x82 <= 0)
@NLconstraint(m, e186, -sqrt((x7 - x25)^2 + (x34 - x52)^2 + (x61 - x79)^2) +
    x82 <= 0)
@NLconstraint(m, e187, -sqrt((x7 - x26)^2 + (x34 - x53)^2 + (x61 - x80)^2) +
    x82 <= 0)
@NLconstraint(m, e188, -sqrt((x7 - x27)^2 + (x34 - x54)^2 + (x61 - x81)^2) +
    x82 <= 0)
@NLconstraint(m, e189, -sqrt((x8 - x9)^2 + (x35 - x36)^2 + (x62 - x63)^2) + x82
    <= 0)
@NLconstraint(m, e190, -sqrt((x8 - x10)^2 + (x35 - x37)^2 + (x62 - x64)^2) +
    x82 <= 0)
@NLconstraint(m, e191, -sqrt((x8 - x11)^2 + (x35 - x38)^2 + (x62 - x65)^2) +
    x82 <= 0)
@NLconstraint(m, e192, -sqrt((x8 - x12)^2 + (x35 - x39)^2 + (x62 - x66)^2) +
    x82 <= 0)
@NLconstraint(m, e193, -sqrt((x8 - x13)^2 + (x35 - x40)^2 + (x62 - x67)^2) +
    x82 <= 0)
@NLconstraint(m, e194, -sqrt((x8 - x14)^2 + (x35 - x41)^2 + (x62 - x68)^2) +
    x82 <= 0)
@NLconstraint(m, e195, -sqrt((x8 - x15)^2 + (x35 - x42)^2 + (x62 - x69)^2) +
    x82 <= 0)
@NLconstraint(m, e196, -sqrt((x8 - x16)^2 + (x35 - x43)^2 + (x62 - x70)^2) +
    x82 <= 0)
@NLconstraint(m, e197, -sqrt((x8 - x17)^2 + (x35 - x44)^2 + (x62 - x71)^2) +
    x82 <= 0)
@NLconstraint(m, e198, -sqrt((x8 - x18)^2 + (x35 - x45)^2 + (x62 - x72)^2) +
    x82 <= 0)
@NLconstraint(m, e199, -sqrt((x8 - x19)^2 + (x35 - x46)^2 + (x62 - x73)^2) +
    x82 <= 0)
@NLconstraint(m, e200, -sqrt((x8 - x20)^2 + (x35 - x47)^2 + (x62 - x74)^2) +
    x82 <= 0)
@NLconstraint(m, e201, -sqrt((x8 - x21)^2 + (x35 - x48)^2 + (x62 - x75)^2) +
    x82 <= 0)
@NLconstraint(m, e202, -sqrt((x8 - x22)^2 + (x35 - x49)^2 + (x62 - x76)^2) +
    x82 <= 0)
@NLconstraint(m, e203, -sqrt((x8 - x23)^2 + (x35 - x50)^2 + (x62 - x77)^2) +
    x82 <= 0)
@NLconstraint(m, e204, -sqrt((x8 - x24)^2 + (x35 - x51)^2 + (x62 - x78)^2) +
    x82 <= 0)
@NLconstraint(m, e205, -sqrt((x8 - x25)^2 + (x35 - x52)^2 + (x62 - x79)^2) +
    x82 <= 0)
@NLconstraint(m, e206, -sqrt((x8 - x26)^2 + (x35 - x53)^2 + (x62 - x80)^2) +
    x82 <= 0)
@NLconstraint(m, e207, -sqrt((x8 - x27)^2 + (x35 - x54)^2 + (x62 - x81)^2) +
    x82 <= 0)
@NLconstraint(m, e208, -sqrt((x9 - x10)^2 + (x36 - x37)^2 + (x63 - x64)^2) +
    x82 <= 0)
@NLconstraint(m, e209, -sqrt((x9 - x11)^2 + (x36 - x38)^2 + (x63 - x65)^2) +
    x82 <= 0)
@NLconstraint(m, e210, -sqrt((x9 - x12)^2 + (x36 - x39)^2 + (x63 - x66)^2) +
    x82 <= 0)
@NLconstraint(m, e211, -sqrt((x9 - x13)^2 + (x36 - x40)^2 + (x63 - x67)^2) +
    x82 <= 0)
@NLconstraint(m, e212, -sqrt((x9 - x14)^2 + (x36 - x41)^2 + (x63 - x68)^2) +
    x82 <= 0)
@NLconstraint(m, e213, -sqrt((x9 - x15)^2 + (x36 - x42)^2 + (x63 - x69)^2) +
    x82 <= 0)
@NLconstraint(m, e214, -sqrt((x9 - x16)^2 + (x36 - x43)^2 + (x63 - x70)^2) +
    x82 <= 0)
@NLconstraint(m, e215, -sqrt((x9 - x17)^2 + (x36 - x44)^2 + (x63 - x71)^2) +
    x82 <= 0)
@NLconstraint(m, e216, -sqrt((x9 - x18)^2 + (x36 - x45)^2 + (x63 - x72)^2) +
    x82 <= 0)
@NLconstraint(m, e217, -sqrt((x9 - x19)^2 + (x36 - x46)^2 + (x63 - x73)^2) +
    x82 <= 0)
@NLconstraint(m, e218, -sqrt((x9 - x20)^2 + (x36 - x47)^2 + (x63 - x74)^2) +
    x82 <= 0)
@NLconstraint(m, e219, -sqrt((x9 - x21)^2 + (x36 - x48)^2 + (x63 - x75)^2) +
    x82 <= 0)
@NLconstraint(m, e220, -sqrt((x9 - x22)^2 + (x36 - x49)^2 + (x63 - x76)^2) +
    x82 <= 0)
@NLconstraint(m, e221, -sqrt((x9 - x23)^2 + (x36 - x50)^2 + (x63 - x77)^2) +
    x82 <= 0)
@NLconstraint(m, e222, -sqrt((x9 - x24)^2 + (x36 - x51)^2 + (x63 - x78)^2) +
    x82 <= 0)
@NLconstraint(m, e223, -sqrt((x9 - x25)^2 + (x36 - x52)^2 + (x63 - x79)^2) +
    x82 <= 0)
@NLconstraint(m, e224, -sqrt((x9 - x26)^2 + (x36 - x53)^2 + (x63 - x80)^2) +
    x82 <= 0)
@NLconstraint(m, e225, -sqrt((x9 - x27)^2 + (x36 - x54)^2 + (x63 - x81)^2) +
    x82 <= 0)
@NLconstraint(m, e226, -sqrt((x10 - x11)^2 + (x37 - x38)^2 + (x64 - x65)^2) +
    x82 <= 0)
@NLconstraint(m, e227, -sqrt((x10 - x12)^2 + (x37 - x39)^2 + (x64 - x66)^2) +
    x82 <= 0)
@NLconstraint(m, e228, -sqrt((x10 - x13)^2 + (x37 - x40)^2 + (x64 - x67)^2) +
    x82 <= 0)
@NLconstraint(m, e229, -sqrt((x10 - x14)^2 + (x37 - x41)^2 + (x64 - x68)^2) +
    x82 <= 0)
@NLconstraint(m, e230, -sqrt((x10 - x15)^2 + (x37 - x42)^2 + (x64 - x69)^2) +
    x82 <= 0)
@NLconstraint(m, e231, -sqrt((x10 - x16)^2 + (x37 - x43)^2 + (x64 - x70)^2) +
    x82 <= 0)
@NLconstraint(m, e232, -sqrt((x10 - x17)^2 + (x37 - x44)^2 + (x64 - x71)^2) +
    x82 <= 0)
@NLconstraint(m, e233, -sqrt((x10 - x18)^2 + (x37 - x45)^2 + (x64 - x72)^2) +
    x82 <= 0)
@NLconstraint(m, e234, -sqrt((x10 - x19)^2 + (x37 - x46)^2 + (x64 - x73)^2) +
    x82 <= 0)
@NLconstraint(m, e235, -sqrt((x10 - x20)^2 + (x37 - x47)^2 + (x64 - x74)^2) +
    x82 <= 0)
@NLconstraint(m, e236, -sqrt((x10 - x21)^2 + (x37 - x48)^2 + (x64 - x75)^2) +
    x82 <= 0)
@NLconstraint(m, e237, -sqrt((x10 - x22)^2 + (x37 - x49)^2 + (x64 - x76)^2) +
    x82 <= 0)
@NLconstraint(m, e238, -sqrt((x10 - x23)^2 + (x37 - x50)^2 + (x64 - x77)^2) +
    x82 <= 0)
@NLconstraint(m, e239, -sqrt((x10 - x24)^2 + (x37 - x51)^2 + (x64 - x78)^2) +
    x82 <= 0)
@NLconstraint(m, e240, -sqrt((x10 - x25)^2 + (x37 - x52)^2 + (x64 - x79)^2) +
    x82 <= 0)
@NLconstraint(m, e241, -sqrt((x10 - x26)^2 + (x37 - x53)^2 + (x64 - x80)^2) +
    x82 <= 0)
@NLconstraint(m, e242, -sqrt((x10 - x27)^2 + (x37 - x54)^2 + (x64 - x81)^2) +
    x82 <= 0)
@NLconstraint(m, e243, -sqrt((x11 - x12)^2 + (x38 - x39)^2 + (x65 - x66)^2) +
    x82 <= 0)
@NLconstraint(m, e244, -sqrt((x11 - x13)^2 + (x38 - x40)^2 + (x65 - x67)^2) +
    x82 <= 0)
@NLconstraint(m, e245, -sqrt((x11 - x14)^2 + (x38 - x41)^2 + (x65 - x68)^2) +
    x82 <= 0)
@NLconstraint(m, e246, -sqrt((x11 - x15)^2 + (x38 - x42)^2 + (x65 - x69)^2) +
    x82 <= 0)
@NLconstraint(m, e247, -sqrt((x11 - x16)^2 + (x38 - x43)^2 + (x65 - x70)^2) +
    x82 <= 0)
@NLconstraint(m, e248, -sqrt((x11 - x17)^2 + (x38 - x44)^2 + (x65 - x71)^2) +
    x82 <= 0)
@NLconstraint(m, e249, -sqrt((x11 - x18)^2 + (x38 - x45)^2 + (x65 - x72)^2) +
    x82 <= 0)
@NLconstraint(m, e250, -sqrt((x11 - x19)^2 + (x38 - x46)^2 + (x65 - x73)^2) +
    x82 <= 0)
@NLconstraint(m, e251, -sqrt((x11 - x20)^2 + (x38 - x47)^2 + (x65 - x74)^2) +
    x82 <= 0)
@NLconstraint(m, e252, -sqrt((x11 - x21)^2 + (x38 - x48)^2 + (x65 - x75)^2) +
    x82 <= 0)
@NLconstraint(m, e253, -sqrt((x11 - x22)^2 + (x38 - x49)^2 + (x65 - x76)^2) +
    x82 <= 0)
@NLconstraint(m, e254, -sqrt((x11 - x23)^2 + (x38 - x50)^2 + (x65 - x77)^2) +
    x82 <= 0)
@NLconstraint(m, e255, -sqrt((x11 - x24)^2 + (x38 - x51)^2 + (x65 - x78)^2) +
    x82 <= 0)
@NLconstraint(m, e256, -sqrt((x11 - x25)^2 + (x38 - x52)^2 + (x65 - x79)^2) +
    x82 <= 0)
@NLconstraint(m, e257, -sqrt((x11 - x26)^2 + (x38 - x53)^2 + (x65 - x80)^2) +
    x82 <= 0)
@NLconstraint(m, e258, -sqrt((x11 - x27)^2 + (x38 - x54)^2 + (x65 - x81)^2) +
    x82 <= 0)
@NLconstraint(m, e259, -sqrt((x12 - x13)^2 + (x39 - x40)^2 + (x66 - x67)^2) +
    x82 <= 0)
@NLconstraint(m, e260, -sqrt((x12 - x14)^2 + (x39 - x41)^2 + (x66 - x68)^2) +
    x82 <= 0)
@NLconstraint(m, e261, -sqrt((x12 - x15)^2 + (x39 - x42)^2 + (x66 - x69)^2) +
    x82 <= 0)
@NLconstraint(m, e262, -sqrt((x12 - x16)^2 + (x39 - x43)^2 + (x66 - x70)^2) +
    x82 <= 0)
@NLconstraint(m, e263, -sqrt((x12 - x17)^2 + (x39 - x44)^2 + (x66 - x71)^2) +
    x82 <= 0)
@NLconstraint(m, e264, -sqrt((x12 - x18)^2 + (x39 - x45)^2 + (x66 - x72)^2) +
    x82 <= 0)
@NLconstraint(m, e265, -sqrt((x12 - x19)^2 + (x39 - x46)^2 + (x66 - x73)^2) +
    x82 <= 0)
@NLconstraint(m, e266, -sqrt((x12 - x20)^2 + (x39 - x47)^2 + (x66 - x74)^2) +
    x82 <= 0)
@NLconstraint(m, e267, -sqrt((x12 - x21)^2 + (x39 - x48)^2 + (x66 - x75)^2) +
    x82 <= 0)
@NLconstraint(m, e268, -sqrt((x12 - x22)^2 + (x39 - x49)^2 + (x66 - x76)^2) +
    x82 <= 0)
@NLconstraint(m, e269, -sqrt((x12 - x23)^2 + (x39 - x50)^2 + (x66 - x77)^2) +
    x82 <= 0)
@NLconstraint(m, e270, -sqrt((x12 - x24)^2 + (x39 - x51)^2 + (x66 - x78)^2) +
    x82 <= 0)
@NLconstraint(m, e271, -sqrt((x12 - x25)^2 + (x39 - x52)^2 + (x66 - x79)^2) +
    x82 <= 0)
@NLconstraint(m, e272, -sqrt((x12 - x26)^2 + (x39 - x53)^2 + (x66 - x80)^2) +
    x82 <= 0)
@NLconstraint(m, e273, -sqrt((x12 - x27)^2 + (x39 - x54)^2 + (x66 - x81)^2) +
    x82 <= 0)
@NLconstraint(m, e274, -sqrt((x13 - x14)^2 + (x40 - x41)^2 + (x67 - x68)^2) +
    x82 <= 0)
@NLconstraint(m, e275, -sqrt((x13 - x15)^2 + (x40 - x42)^2 + (x67 - x69)^2) +
    x82 <= 0)
@NLconstraint(m, e276, -sqrt((x13 - x16)^2 + (x40 - x43)^2 + (x67 - x70)^2) +
    x82 <= 0)
@NLconstraint(m, e277, -sqrt((x13 - x17)^2 + (x40 - x44)^2 + (x67 - x71)^2) +
    x82 <= 0)
@NLconstraint(m, e278, -sqrt((x13 - x18)^2 + (x40 - x45)^2 + (x67 - x72)^2) +
    x82 <= 0)
@NLconstraint(m, e279, -sqrt((x13 - x19)^2 + (x40 - x46)^2 + (x67 - x73)^2) +
    x82 <= 0)
@NLconstraint(m, e280, -sqrt((x13 - x20)^2 + (x40 - x47)^2 + (x67 - x74)^2) +
    x82 <= 0)
@NLconstraint(m, e281, -sqrt((x13 - x21)^2 + (x40 - x48)^2 + (x67 - x75)^2) +
    x82 <= 0)
@NLconstraint(m, e282, -sqrt((x13 - x22)^2 + (x40 - x49)^2 + (x67 - x76)^2) +
    x82 <= 0)
@NLconstraint(m, e283, -sqrt((x13 - x23)^2 + (x40 - x50)^2 + (x67 - x77)^2) +
    x82 <= 0)
@NLconstraint(m, e284, -sqrt((x13 - x24)^2 + (x40 - x51)^2 + (x67 - x78)^2) +
    x82 <= 0)
@NLconstraint(m, e285, -sqrt((x13 - x25)^2 + (x40 - x52)^2 + (x67 - x79)^2) +
    x82 <= 0)
@NLconstraint(m, e286, -sqrt((x13 - x26)^2 + (x40 - x53)^2 + (x67 - x80)^2) +
    x82 <= 0)
@NLconstraint(m, e287, -sqrt((x13 - x27)^2 + (x40 - x54)^2 + (x67 - x81)^2) +
    x82 <= 0)
@NLconstraint(m, e288, -sqrt((x14 - x15)^2 + (x41 - x42)^2 + (x68 - x69)^2) +
    x82 <= 0)
@NLconstraint(m, e289, -sqrt((x14 - x16)^2 + (x41 - x43)^2 + (x68 - x70)^2) +
    x82 <= 0)
@NLconstraint(m, e290, -sqrt((x14 - x17)^2 + (x41 - x44)^2 + (x68 - x71)^2) +
    x82 <= 0)
@NLconstraint(m, e291, -sqrt((x14 - x18)^2 + (x41 - x45)^2 + (x68 - x72)^2) +
    x82 <= 0)
@NLconstraint(m, e292, -sqrt((x14 - x19)^2 + (x41 - x46)^2 + (x68 - x73)^2) +
    x82 <= 0)
@NLconstraint(m, e293, -sqrt((x14 - x20)^2 + (x41 - x47)^2 + (x68 - x74)^2) +
    x82 <= 0)
@NLconstraint(m, e294, -sqrt((x14 - x21)^2 + (x41 - x48)^2 + (x68 - x75)^2) +
    x82 <= 0)
@NLconstraint(m, e295, -sqrt((x14 - x22)^2 + (x41 - x49)^2 + (x68 - x76)^2) +
    x82 <= 0)
@NLconstraint(m, e296, -sqrt((x14 - x23)^2 + (x41 - x50)^2 + (x68 - x77)^2) +
    x82 <= 0)
@NLconstraint(m, e297, -sqrt((x14 - x24)^2 + (x41 - x51)^2 + (x68 - x78)^2) +
    x82 <= 0)
@NLconstraint(m, e298, -sqrt((x14 - x25)^2 + (x41 - x52)^2 + (x68 - x79)^2) +
    x82 <= 0)
@NLconstraint(m, e299, -sqrt((x14 - x26)^2 + (x41 - x53)^2 + (x68 - x80)^2) +
    x82 <= 0)
@NLconstraint(m, e300, -sqrt((x14 - x27)^2 + (x41 - x54)^2 + (x68 - x81)^2) +
    x82 <= 0)
@NLconstraint(m, e301, -sqrt((x15 - x16)^2 + (x42 - x43)^2 + (x69 - x70)^2) +
    x82 <= 0)
@NLconstraint(m, e302, -sqrt((x15 - x17)^2 + (x42 - x44)^2 + (x69 - x71)^2) +
    x82 <= 0)
@NLconstraint(m, e303, -sqrt((x15 - x18)^2 + (x42 - x45)^2 + (x69 - x72)^2) +
    x82 <= 0)
@NLconstraint(m, e304, -sqrt((x15 - x19)^2 + (x42 - x46)^2 + (x69 - x73)^2) +
    x82 <= 0)
@NLconstraint(m, e305, -sqrt((x15 - x20)^2 + (x42 - x47)^2 + (x69 - x74)^2) +
    x82 <= 0)
@NLconstraint(m, e306, -sqrt((x15 - x21)^2 + (x42 - x48)^2 + (x69 - x75)^2) +
    x82 <= 0)
@NLconstraint(m, e307, -sqrt((x15 - x22)^2 + (x42 - x49)^2 + (x69 - x76)^2) +
    x82 <= 0)
@NLconstraint(m, e308, -sqrt((x15 - x23)^2 + (x42 - x50)^2 + (x69 - x77)^2) +
    x82 <= 0)
@NLconstraint(m, e309, -sqrt((x15 - x24)^2 + (x42 - x51)^2 + (x69 - x78)^2) +
    x82 <= 0)
@NLconstraint(m, e310, -sqrt((x15 - x25)^2 + (x42 - x52)^2 + (x69 - x79)^2) +
    x82 <= 0)
@NLconstraint(m, e311, -sqrt((x15 - x26)^2 + (x42 - x53)^2 + (x69 - x80)^2) +
    x82 <= 0)
@NLconstraint(m, e312, -sqrt((x15 - x27)^2 + (x42 - x54)^2 + (x69 - x81)^2) +
    x82 <= 0)
@NLconstraint(m, e313, -sqrt((x16 - x17)^2 + (x43 - x44)^2 + (x70 - x71)^2) +
    x82 <= 0)
@NLconstraint(m, e314, -sqrt((x16 - x18)^2 + (x43 - x45)^2 + (x70 - x72)^2) +
    x82 <= 0)
@NLconstraint(m, e315, -sqrt((x16 - x19)^2 + (x43 - x46)^2 + (x70 - x73)^2) +
    x82 <= 0)
@NLconstraint(m, e316, -sqrt((x16 - x20)^2 + (x43 - x47)^2 + (x70 - x74)^2) +
    x82 <= 0)
@NLconstraint(m, e317, -sqrt((x16 - x21)^2 + (x43 - x48)^2 + (x70 - x75)^2) +
    x82 <= 0)
@NLconstraint(m, e318, -sqrt((x16 - x22)^2 + (x43 - x49)^2 + (x70 - x76)^2) +
    x82 <= 0)
@NLconstraint(m, e319, -sqrt((x16 - x23)^2 + (x43 - x50)^2 + (x70 - x77)^2) +
    x82 <= 0)
@NLconstraint(m, e320, -sqrt((x16 - x24)^2 + (x43 - x51)^2 + (x70 - x78)^2) +
    x82 <= 0)
@NLconstraint(m, e321, -sqrt((x16 - x25)^2 + (x43 - x52)^2 + (x70 - x79)^2) +
    x82 <= 0)
@NLconstraint(m, e322, -sqrt((x16 - x26)^2 + (x43 - x53)^2 + (x70 - x80)^2) +
    x82 <= 0)
@NLconstraint(m, e323, -sqrt((x16 - x27)^2 + (x43 - x54)^2 + (x70 - x81)^2) +
    x82 <= 0)
@NLconstraint(m, e324, -sqrt((x17 - x18)^2 + (x44 - x45)^2 + (x71 - x72)^2) +
    x82 <= 0)
@NLconstraint(m, e325, -sqrt((x17 - x19)^2 + (x44 - x46)^2 + (x71 - x73)^2) +
    x82 <= 0)
@NLconstraint(m, e326, -sqrt((x17 - x20)^2 + (x44 - x47)^2 + (x71 - x74)^2) +
    x82 <= 0)
@NLconstraint(m, e327, -sqrt((x17 - x21)^2 + (x44 - x48)^2 + (x71 - x75)^2) +
    x82 <= 0)
@NLconstraint(m, e328, -sqrt((x17 - x22)^2 + (x44 - x49)^2 + (x71 - x76)^2) +
    x82 <= 0)
@NLconstraint(m, e329, -sqrt((x17 - x23)^2 + (x44 - x50)^2 + (x71 - x77)^2) +
    x82 <= 0)
@NLconstraint(m, e330, -sqrt((x17 - x24)^2 + (x44 - x51)^2 + (x71 - x78)^2) +
    x82 <= 0)
@NLconstraint(m, e331, -sqrt((x17 - x25)^2 + (x44 - x52)^2 + (x71 - x79)^2) +
    x82 <= 0)
@NLconstraint(m, e332, -sqrt((x17 - x26)^2 + (x44 - x53)^2 + (x71 - x80)^2) +
    x82 <= 0)
@NLconstraint(m, e333, -sqrt((x17 - x27)^2 + (x44 - x54)^2 + (x71 - x81)^2) +
    x82 <= 0)
@NLconstraint(m, e334, -sqrt((x18 - x19)^2 + (x45 - x46)^2 + (x72 - x73)^2) +
    x82 <= 0)
@NLconstraint(m, e335, -sqrt((x18 - x20)^2 + (x45 - x47)^2 + (x72 - x74)^2) +
    x82 <= 0)
@NLconstraint(m, e336, -sqrt((x18 - x21)^2 + (x45 - x48)^2 + (x72 - x75)^2) +
    x82 <= 0)
@NLconstraint(m, e337, -sqrt((x18 - x22)^2 + (x45 - x49)^2 + (x72 - x76)^2) +
    x82 <= 0)
@NLconstraint(m, e338, -sqrt((x18 - x23)^2 + (x45 - x50)^2 + (x72 - x77)^2) +
    x82 <= 0)
@NLconstraint(m, e339, -sqrt((x18 - x24)^2 + (x45 - x51)^2 + (x72 - x78)^2) +
    x82 <= 0)
@NLconstraint(m, e340, -sqrt((x18 - x25)^2 + (x45 - x52)^2 + (x72 - x79)^2) +
    x82 <= 0)
@NLconstraint(m, e341, -sqrt((x18 - x26)^2 + (x45 - x53)^2 + (x72 - x80)^2) +
    x82 <= 0)
@NLconstraint(m, e342, -sqrt((x18 - x27)^2 + (x45 - x54)^2 + (x72 - x81)^2) +
    x82 <= 0)
@NLconstraint(m, e343, -sqrt((x19 - x20)^2 + (x46 - x47)^2 + (x73 - x74)^2) +
    x82 <= 0)
@NLconstraint(m, e344, -sqrt((x19 - x21)^2 + (x46 - x48)^2 + (x73 - x75)^2) +
    x82 <= 0)
@NLconstraint(m, e345, -sqrt((x19 - x22)^2 + (x46 - x49)^2 + (x73 - x76)^2) +
    x82 <= 0)
@NLconstraint(m, e346, -sqrt((x19 - x23)^2 + (x46 - x50)^2 + (x73 - x77)^2) +
    x82 <= 0)
@NLconstraint(m, e347, -sqrt((x19 - x24)^2 + (x46 - x51)^2 + (x73 - x78)^2) +
    x82 <= 0)
@NLconstraint(m, e348, -sqrt((x19 - x25)^2 + (x46 - x52)^2 + (x73 - x79)^2) +
    x82 <= 0)
@NLconstraint(m, e349, -sqrt((x19 - x26)^2 + (x46 - x53)^2 + (x73 - x80)^2) +
    x82 <= 0)
@NLconstraint(m, e350, -sqrt((x19 - x27)^2 + (x46 - x54)^2 + (x73 - x81)^2) +
    x82 <= 0)
@NLconstraint(m, e351, -sqrt((x20 - x21)^2 + (x47 - x48)^2 + (x74 - x75)^2) +
    x82 <= 0)
@NLconstraint(m, e352, -sqrt((x20 - x22)^2 + (x47 - x49)^2 + (x74 - x76)^2) +
    x82 <= 0)
@NLconstraint(m, e353, -sqrt((x20 - x23)^2 + (x47 - x50)^2 + (x74 - x77)^2) +
    x82 <= 0)
@NLconstraint(m, e354, -sqrt((x20 - x24)^2 + (x47 - x51)^2 + (x74 - x78)^2) +
    x82 <= 0)
@NLconstraint(m, e355, -sqrt((x20 - x25)^2 + (x47 - x52)^2 + (x74 - x79)^2) +
    x82 <= 0)
@NLconstraint(m, e356, -sqrt((x20 - x26)^2 + (x47 - x53)^2 + (x74 - x80)^2) +
    x82 <= 0)
@NLconstraint(m, e357, -sqrt((x20 - x27)^2 + (x47 - x54)^2 + (x74 - x81)^2) +
    x82 <= 0)
@NLconstraint(m, e358, -sqrt((x21 - x22)^2 + (x48 - x49)^2 + (x75 - x76)^2) +
    x82 <= 0)
@NLconstraint(m, e359, -sqrt((x21 - x23)^2 + (x48 - x50)^2 + (x75 - x77)^2) +
    x82 <= 0)
@NLconstraint(m, e360, -sqrt((x21 - x24)^2 + (x48 - x51)^2 + (x75 - x78)^2) +
    x82 <= 0)
@NLconstraint(m, e361, -sqrt((x21 - x25)^2 + (x48 - x52)^2 + (x75 - x79)^2) +
    x82 <= 0)
@NLconstraint(m, e362, -sqrt((x21 - x26)^2 + (x48 - x53)^2 + (x75 - x80)^2) +
    x82 <= 0)
@NLconstraint(m, e363, -sqrt((x21 - x27)^2 + (x48 - x54)^2 + (x75 - x81)^2) +
    x82 <= 0)
@NLconstraint(m, e364, -sqrt((x22 - x23)^2 + (x49 - x50)^2 + (x76 - x77)^2) +
    x82 <= 0)
@NLconstraint(m, e365, -sqrt((x22 - x24)^2 + (x49 - x51)^2 + (x76 - x78)^2) +
    x82 <= 0)
@NLconstraint(m, e366, -sqrt((x22 - x25)^2 + (x49 - x52)^2 + (x76 - x79)^2) +
    x82 <= 0)
@NLconstraint(m, e367, -sqrt((x22 - x26)^2 + (x49 - x53)^2 + (x76 - x80)^2) +
    x82 <= 0)
@NLconstraint(m, e368, -sqrt((x22 - x27)^2 + (x49 - x54)^2 + (x76 - x81)^2) +
    x82 <= 0)
@NLconstraint(m, e369, -sqrt((x23 - x24)^2 + (x50 - x51)^2 + (x77 - x78)^2) +
    x82 <= 0)
@NLconstraint(m, e370, -sqrt((x23 - x25)^2 + (x50 - x52)^2 + (x77 - x79)^2) +
    x82 <= 0)
@NLconstraint(m, e371, -sqrt((x23 - x26)^2 + (x50 - x53)^2 + (x77 - x80)^2) +
    x82 <= 0)
@NLconstraint(m, e372, -sqrt((x23 - x27)^2 + (x50 - x54)^2 + (x77 - x81)^2) +
    x82 <= 0)
@NLconstraint(m, e373, -sqrt((x24 - x25)^2 + (x51 - x52)^2 + (x78 - x79)^2) +
    x82 <= 0)
@NLconstraint(m, e374, -sqrt((x24 - x26)^2 + (x51 - x53)^2 + (x78 - x80)^2) +
    x82 <= 0)
@NLconstraint(m, e375, -sqrt((x24 - x27)^2 + (x51 - x54)^2 + (x78 - x81)^2) +
    x82 <= 0)
@NLconstraint(m, e376, -sqrt((x25 - x26)^2 + (x52 - x53)^2 + (x79 - x80)^2) +
    x82 <= 0)
@NLconstraint(m, e377, -sqrt((x25 - x27)^2 + (x52 - x54)^2 + (x79 - x81)^2) +
    x82 <= 0)
@NLconstraint(m, e378, -sqrt((x26 - x27)^2 + (x53 - x54)^2 + (x80 - x81)^2) +
    x82 <= 0)
