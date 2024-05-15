# NLP written by GAMS Convert at 05/15/24 11:27:27
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       253       22        0      231        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        67       67        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#      1683      231     1452
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
@variable(m, x67, start=0)

@objective(m, Max, x67)

@NLconstraint(m, e1, x1^2 + x23^2 + x45^2 == 1)
@NLconstraint(m, e2, x2^2 + x24^2 + x46^2 == 1)
@NLconstraint(m, e3, x3^2 + x25^2 + x47^2 == 1)
@NLconstraint(m, e4, x4^2 + x26^2 + x48^2 == 1)
@NLconstraint(m, e5, x5^2 + x27^2 + x49^2 == 1)
@NLconstraint(m, e6, x6^2 + x28^2 + x50^2 == 1)
@NLconstraint(m, e7, x7^2 + x29^2 + x51^2 == 1)
@NLconstraint(m, e8, x8^2 + x30^2 + x52^2 == 1)
@NLconstraint(m, e9, x9^2 + x31^2 + x53^2 == 1)
@NLconstraint(m, e10, x10^2 + x32^2 + x54^2 == 1)
@NLconstraint(m, e11, x11^2 + x33^2 + x55^2 == 1)
@NLconstraint(m, e12, x12^2 + x34^2 + x56^2 == 1)
@NLconstraint(m, e13, x13^2 + x35^2 + x57^2 == 1)
@NLconstraint(m, e14, x14^2 + x36^2 + x58^2 == 1)
@NLconstraint(m, e15, x15^2 + x37^2 + x59^2 == 1)
@NLconstraint(m, e16, x16^2 + x38^2 + x60^2 == 1)
@NLconstraint(m, e17, x17^2 + x39^2 + x61^2 == 1)
@NLconstraint(m, e18, x18^2 + x40^2 + x62^2 == 1)
@NLconstraint(m, e19, x19^2 + x41^2 + x63^2 == 1)
@NLconstraint(m, e20, x20^2 + x42^2 + x64^2 == 1)
@NLconstraint(m, e21, x21^2 + x43^2 + x65^2 == 1)
@NLconstraint(m, e22, x22^2 + x44^2 + x66^2 == 1)
@NLconstraint(m, e23, -sqrt((x1 - x2)^2 + (x23 - x24)^2 + (x45 - x46)^2) + x67
    <= 0)
@NLconstraint(m, e24, -sqrt((x1 - x3)^2 + (x23 - x25)^2 + (x45 - x47)^2) + x67
    <= 0)
@NLconstraint(m, e25, -sqrt((x1 - x4)^2 + (x23 - x26)^2 + (x45 - x48)^2) + x67
    <= 0)
@NLconstraint(m, e26, -sqrt((x1 - x5)^2 + (x23 - x27)^2 + (x45 - x49)^2) + x67
    <= 0)
@NLconstraint(m, e27, -sqrt((x1 - x6)^2 + (x23 - x28)^2 + (x45 - x50)^2) + x67
    <= 0)
@NLconstraint(m, e28, -sqrt((x1 - x7)^2 + (x23 - x29)^2 + (x45 - x51)^2) + x67
    <= 0)
@NLconstraint(m, e29, -sqrt((x1 - x8)^2 + (x23 - x30)^2 + (x45 - x52)^2) + x67
    <= 0)
@NLconstraint(m, e30, -sqrt((x1 - x9)^2 + (x23 - x31)^2 + (x45 - x53)^2) + x67
    <= 0)
@NLconstraint(m, e31, -sqrt((x1 - x10)^2 + (x23 - x32)^2 + (x45 - x54)^2) + x67
    <= 0)
@NLconstraint(m, e32, -sqrt((x1 - x11)^2 + (x23 - x33)^2 + (x45 - x55)^2) + x67
    <= 0)
@NLconstraint(m, e33, -sqrt((x1 - x12)^2 + (x23 - x34)^2 + (x45 - x56)^2) + x67
    <= 0)
@NLconstraint(m, e34, -sqrt((x1 - x13)^2 + (x23 - x35)^2 + (x45 - x57)^2) + x67
    <= 0)
@NLconstraint(m, e35, -sqrt((x1 - x14)^2 + (x23 - x36)^2 + (x45 - x58)^2) + x67
    <= 0)
@NLconstraint(m, e36, -sqrt((x1 - x15)^2 + (x23 - x37)^2 + (x45 - x59)^2) + x67
    <= 0)
@NLconstraint(m, e37, -sqrt((x1 - x16)^2 + (x23 - x38)^2 + (x45 - x60)^2) + x67
    <= 0)
@NLconstraint(m, e38, -sqrt((x1 - x17)^2 + (x23 - x39)^2 + (x45 - x61)^2) + x67
    <= 0)
@NLconstraint(m, e39, -sqrt((x1 - x18)^2 + (x23 - x40)^2 + (x45 - x62)^2) + x67
    <= 0)
@NLconstraint(m, e40, -sqrt((x1 - x19)^2 + (x23 - x41)^2 + (x45 - x63)^2) + x67
    <= 0)
@NLconstraint(m, e41, -sqrt((x1 - x20)^2 + (x23 - x42)^2 + (x45 - x64)^2) + x67
    <= 0)
@NLconstraint(m, e42, -sqrt((x1 - x21)^2 + (x23 - x43)^2 + (x45 - x65)^2) + x67
    <= 0)
@NLconstraint(m, e43, -sqrt((x1 - x22)^2 + (x23 - x44)^2 + (x45 - x66)^2) + x67
    <= 0)
@NLconstraint(m, e44, -sqrt((x2 - x3)^2 + (x24 - x25)^2 + (x46 - x47)^2) + x67
    <= 0)
@NLconstraint(m, e45, -sqrt((x2 - x4)^2 + (x24 - x26)^2 + (x46 - x48)^2) + x67
    <= 0)
@NLconstraint(m, e46, -sqrt((x2 - x5)^2 + (x24 - x27)^2 + (x46 - x49)^2) + x67
    <= 0)
@NLconstraint(m, e47, -sqrt((x2 - x6)^2 + (x24 - x28)^2 + (x46 - x50)^2) + x67
    <= 0)
@NLconstraint(m, e48, -sqrt((x2 - x7)^2 + (x24 - x29)^2 + (x46 - x51)^2) + x67
    <= 0)
@NLconstraint(m, e49, -sqrt((x2 - x8)^2 + (x24 - x30)^2 + (x46 - x52)^2) + x67
    <= 0)
@NLconstraint(m, e50, -sqrt((x2 - x9)^2 + (x24 - x31)^2 + (x46 - x53)^2) + x67
    <= 0)
@NLconstraint(m, e51, -sqrt((x2 - x10)^2 + (x24 - x32)^2 + (x46 - x54)^2) + x67
    <= 0)
@NLconstraint(m, e52, -sqrt((x2 - x11)^2 + (x24 - x33)^2 + (x46 - x55)^2) + x67
    <= 0)
@NLconstraint(m, e53, -sqrt((x2 - x12)^2 + (x24 - x34)^2 + (x46 - x56)^2) + x67
    <= 0)
@NLconstraint(m, e54, -sqrt((x2 - x13)^2 + (x24 - x35)^2 + (x46 - x57)^2) + x67
    <= 0)
@NLconstraint(m, e55, -sqrt((x2 - x14)^2 + (x24 - x36)^2 + (x46 - x58)^2) + x67
    <= 0)
@NLconstraint(m, e56, -sqrt((x2 - x15)^2 + (x24 - x37)^2 + (x46 - x59)^2) + x67
    <= 0)
@NLconstraint(m, e57, -sqrt((x2 - x16)^2 + (x24 - x38)^2 + (x46 - x60)^2) + x67
    <= 0)
@NLconstraint(m, e58, -sqrt((x2 - x17)^2 + (x24 - x39)^2 + (x46 - x61)^2) + x67
    <= 0)
@NLconstraint(m, e59, -sqrt((x2 - x18)^2 + (x24 - x40)^2 + (x46 - x62)^2) + x67
    <= 0)
@NLconstraint(m, e60, -sqrt((x2 - x19)^2 + (x24 - x41)^2 + (x46 - x63)^2) + x67
    <= 0)
@NLconstraint(m, e61, -sqrt((x2 - x20)^2 + (x24 - x42)^2 + (x46 - x64)^2) + x67
    <= 0)
@NLconstraint(m, e62, -sqrt((x2 - x21)^2 + (x24 - x43)^2 + (x46 - x65)^2) + x67
    <= 0)
@NLconstraint(m, e63, -sqrt((x2 - x22)^2 + (x24 - x44)^2 + (x46 - x66)^2) + x67
    <= 0)
@NLconstraint(m, e64, -sqrt((x3 - x4)^2 + (x25 - x26)^2 + (x47 - x48)^2) + x67
    <= 0)
@NLconstraint(m, e65, -sqrt((x3 - x5)^2 + (x25 - x27)^2 + (x47 - x49)^2) + x67
    <= 0)
@NLconstraint(m, e66, -sqrt((x3 - x6)^2 + (x25 - x28)^2 + (x47 - x50)^2) + x67
    <= 0)
@NLconstraint(m, e67, -sqrt((x3 - x7)^2 + (x25 - x29)^2 + (x47 - x51)^2) + x67
    <= 0)
@NLconstraint(m, e68, -sqrt((x3 - x8)^2 + (x25 - x30)^2 + (x47 - x52)^2) + x67
    <= 0)
@NLconstraint(m, e69, -sqrt((x3 - x9)^2 + (x25 - x31)^2 + (x47 - x53)^2) + x67
    <= 0)
@NLconstraint(m, e70, -sqrt((x3 - x10)^2 + (x25 - x32)^2 + (x47 - x54)^2) + x67
    <= 0)
@NLconstraint(m, e71, -sqrt((x3 - x11)^2 + (x25 - x33)^2 + (x47 - x55)^2) + x67
    <= 0)
@NLconstraint(m, e72, -sqrt((x3 - x12)^2 + (x25 - x34)^2 + (x47 - x56)^2) + x67
    <= 0)
@NLconstraint(m, e73, -sqrt((x3 - x13)^2 + (x25 - x35)^2 + (x47 - x57)^2) + x67
    <= 0)
@NLconstraint(m, e74, -sqrt((x3 - x14)^2 + (x25 - x36)^2 + (x47 - x58)^2) + x67
    <= 0)
@NLconstraint(m, e75, -sqrt((x3 - x15)^2 + (x25 - x37)^2 + (x47 - x59)^2) + x67
    <= 0)
@NLconstraint(m, e76, -sqrt((x3 - x16)^2 + (x25 - x38)^2 + (x47 - x60)^2) + x67
    <= 0)
@NLconstraint(m, e77, -sqrt((x3 - x17)^2 + (x25 - x39)^2 + (x47 - x61)^2) + x67
    <= 0)
@NLconstraint(m, e78, -sqrt((x3 - x18)^2 + (x25 - x40)^2 + (x47 - x62)^2) + x67
    <= 0)
@NLconstraint(m, e79, -sqrt((x3 - x19)^2 + (x25 - x41)^2 + (x47 - x63)^2) + x67
    <= 0)
@NLconstraint(m, e80, -sqrt((x3 - x20)^2 + (x25 - x42)^2 + (x47 - x64)^2) + x67
    <= 0)
@NLconstraint(m, e81, -sqrt((x3 - x21)^2 + (x25 - x43)^2 + (x47 - x65)^2) + x67
    <= 0)
@NLconstraint(m, e82, -sqrt((x3 - x22)^2 + (x25 - x44)^2 + (x47 - x66)^2) + x67
    <= 0)
@NLconstraint(m, e83, -sqrt((x4 - x5)^2 + (x26 - x27)^2 + (x48 - x49)^2) + x67
    <= 0)
@NLconstraint(m, e84, -sqrt((x4 - x6)^2 + (x26 - x28)^2 + (x48 - x50)^2) + x67
    <= 0)
@NLconstraint(m, e85, -sqrt((x4 - x7)^2 + (x26 - x29)^2 + (x48 - x51)^2) + x67
    <= 0)
@NLconstraint(m, e86, -sqrt((x4 - x8)^2 + (x26 - x30)^2 + (x48 - x52)^2) + x67
    <= 0)
@NLconstraint(m, e87, -sqrt((x4 - x9)^2 + (x26 - x31)^2 + (x48 - x53)^2) + x67
    <= 0)
@NLconstraint(m, e88, -sqrt((x4 - x10)^2 + (x26 - x32)^2 + (x48 - x54)^2) + x67
    <= 0)
@NLconstraint(m, e89, -sqrt((x4 - x11)^2 + (x26 - x33)^2 + (x48 - x55)^2) + x67
    <= 0)
@NLconstraint(m, e90, -sqrt((x4 - x12)^2 + (x26 - x34)^2 + (x48 - x56)^2) + x67
    <= 0)
@NLconstraint(m, e91, -sqrt((x4 - x13)^2 + (x26 - x35)^2 + (x48 - x57)^2) + x67
    <= 0)
@NLconstraint(m, e92, -sqrt((x4 - x14)^2 + (x26 - x36)^2 + (x48 - x58)^2) + x67
    <= 0)
@NLconstraint(m, e93, -sqrt((x4 - x15)^2 + (x26 - x37)^2 + (x48 - x59)^2) + x67
    <= 0)
@NLconstraint(m, e94, -sqrt((x4 - x16)^2 + (x26 - x38)^2 + (x48 - x60)^2) + x67
    <= 0)
@NLconstraint(m, e95, -sqrt((x4 - x17)^2 + (x26 - x39)^2 + (x48 - x61)^2) + x67
    <= 0)
@NLconstraint(m, e96, -sqrt((x4 - x18)^2 + (x26 - x40)^2 + (x48 - x62)^2) + x67
    <= 0)
@NLconstraint(m, e97, -sqrt((x4 - x19)^2 + (x26 - x41)^2 + (x48 - x63)^2) + x67
    <= 0)
@NLconstraint(m, e98, -sqrt((x4 - x20)^2 + (x26 - x42)^2 + (x48 - x64)^2) + x67
    <= 0)
@NLconstraint(m, e99, -sqrt((x4 - x21)^2 + (x26 - x43)^2 + (x48 - x65)^2) + x67
    <= 0)
@NLconstraint(m, e100, -sqrt((x4 - x22)^2 + (x26 - x44)^2 + (x48 - x66)^2) +
    x67 <= 0)
@NLconstraint(m, e101, -sqrt((x5 - x6)^2 + (x27 - x28)^2 + (x49 - x50)^2) + x67
    <= 0)
@NLconstraint(m, e102, -sqrt((x5 - x7)^2 + (x27 - x29)^2 + (x49 - x51)^2) + x67
    <= 0)
@NLconstraint(m, e103, -sqrt((x5 - x8)^2 + (x27 - x30)^2 + (x49 - x52)^2) + x67
    <= 0)
@NLconstraint(m, e104, -sqrt((x5 - x9)^2 + (x27 - x31)^2 + (x49 - x53)^2) + x67
    <= 0)
@NLconstraint(m, e105, -sqrt((x5 - x10)^2 + (x27 - x32)^2 + (x49 - x54)^2) +
    x67 <= 0)
@NLconstraint(m, e106, -sqrt((x5 - x11)^2 + (x27 - x33)^2 + (x49 - x55)^2) +
    x67 <= 0)
@NLconstraint(m, e107, -sqrt((x5 - x12)^2 + (x27 - x34)^2 + (x49 - x56)^2) +
    x67 <= 0)
@NLconstraint(m, e108, -sqrt((x5 - x13)^2 + (x27 - x35)^2 + (x49 - x57)^2) +
    x67 <= 0)
@NLconstraint(m, e109, -sqrt((x5 - x14)^2 + (x27 - x36)^2 + (x49 - x58)^2) +
    x67 <= 0)
@NLconstraint(m, e110, -sqrt((x5 - x15)^2 + (x27 - x37)^2 + (x49 - x59)^2) +
    x67 <= 0)
@NLconstraint(m, e111, -sqrt((x5 - x16)^2 + (x27 - x38)^2 + (x49 - x60)^2) +
    x67 <= 0)
@NLconstraint(m, e112, -sqrt((x5 - x17)^2 + (x27 - x39)^2 + (x49 - x61)^2) +
    x67 <= 0)
@NLconstraint(m, e113, -sqrt((x5 - x18)^2 + (x27 - x40)^2 + (x49 - x62)^2) +
    x67 <= 0)
@NLconstraint(m, e114, -sqrt((x5 - x19)^2 + (x27 - x41)^2 + (x49 - x63)^2) +
    x67 <= 0)
@NLconstraint(m, e115, -sqrt((x5 - x20)^2 + (x27 - x42)^2 + (x49 - x64)^2) +
    x67 <= 0)
@NLconstraint(m, e116, -sqrt((x5 - x21)^2 + (x27 - x43)^2 + (x49 - x65)^2) +
    x67 <= 0)
@NLconstraint(m, e117, -sqrt((x5 - x22)^2 + (x27 - x44)^2 + (x49 - x66)^2) +
    x67 <= 0)
@NLconstraint(m, e118, -sqrt((x6 - x7)^2 + (x28 - x29)^2 + (x50 - x51)^2) + x67
    <= 0)
@NLconstraint(m, e119, -sqrt((x6 - x8)^2 + (x28 - x30)^2 + (x50 - x52)^2) + x67
    <= 0)
@NLconstraint(m, e120, -sqrt((x6 - x9)^2 + (x28 - x31)^2 + (x50 - x53)^2) + x67
    <= 0)
@NLconstraint(m, e121, -sqrt((x6 - x10)^2 + (x28 - x32)^2 + (x50 - x54)^2) +
    x67 <= 0)
@NLconstraint(m, e122, -sqrt((x6 - x11)^2 + (x28 - x33)^2 + (x50 - x55)^2) +
    x67 <= 0)
@NLconstraint(m, e123, -sqrt((x6 - x12)^2 + (x28 - x34)^2 + (x50 - x56)^2) +
    x67 <= 0)
@NLconstraint(m, e124, -sqrt((x6 - x13)^2 + (x28 - x35)^2 + (x50 - x57)^2) +
    x67 <= 0)
@NLconstraint(m, e125, -sqrt((x6 - x14)^2 + (x28 - x36)^2 + (x50 - x58)^2) +
    x67 <= 0)
@NLconstraint(m, e126, -sqrt((x6 - x15)^2 + (x28 - x37)^2 + (x50 - x59)^2) +
    x67 <= 0)
@NLconstraint(m, e127, -sqrt((x6 - x16)^2 + (x28 - x38)^2 + (x50 - x60)^2) +
    x67 <= 0)
@NLconstraint(m, e128, -sqrt((x6 - x17)^2 + (x28 - x39)^2 + (x50 - x61)^2) +
    x67 <= 0)
@NLconstraint(m, e129, -sqrt((x6 - x18)^2 + (x28 - x40)^2 + (x50 - x62)^2) +
    x67 <= 0)
@NLconstraint(m, e130, -sqrt((x6 - x19)^2 + (x28 - x41)^2 + (x50 - x63)^2) +
    x67 <= 0)
@NLconstraint(m, e131, -sqrt((x6 - x20)^2 + (x28 - x42)^2 + (x50 - x64)^2) +
    x67 <= 0)
@NLconstraint(m, e132, -sqrt((x6 - x21)^2 + (x28 - x43)^2 + (x50 - x65)^2) +
    x67 <= 0)
@NLconstraint(m, e133, -sqrt((x6 - x22)^2 + (x28 - x44)^2 + (x50 - x66)^2) +
    x67 <= 0)
@NLconstraint(m, e134, -sqrt((x7 - x8)^2 + (x29 - x30)^2 + (x51 - x52)^2) + x67
    <= 0)
@NLconstraint(m, e135, -sqrt((x7 - x9)^2 + (x29 - x31)^2 + (x51 - x53)^2) + x67
    <= 0)
@NLconstraint(m, e136, -sqrt((x7 - x10)^2 + (x29 - x32)^2 + (x51 - x54)^2) +
    x67 <= 0)
@NLconstraint(m, e137, -sqrt((x7 - x11)^2 + (x29 - x33)^2 + (x51 - x55)^2) +
    x67 <= 0)
@NLconstraint(m, e138, -sqrt((x7 - x12)^2 + (x29 - x34)^2 + (x51 - x56)^2) +
    x67 <= 0)
@NLconstraint(m, e139, -sqrt((x7 - x13)^2 + (x29 - x35)^2 + (x51 - x57)^2) +
    x67 <= 0)
@NLconstraint(m, e140, -sqrt((x7 - x14)^2 + (x29 - x36)^2 + (x51 - x58)^2) +
    x67 <= 0)
@NLconstraint(m, e141, -sqrt((x7 - x15)^2 + (x29 - x37)^2 + (x51 - x59)^2) +
    x67 <= 0)
@NLconstraint(m, e142, -sqrt((x7 - x16)^2 + (x29 - x38)^2 + (x51 - x60)^2) +
    x67 <= 0)
@NLconstraint(m, e143, -sqrt((x7 - x17)^2 + (x29 - x39)^2 + (x51 - x61)^2) +
    x67 <= 0)
@NLconstraint(m, e144, -sqrt((x7 - x18)^2 + (x29 - x40)^2 + (x51 - x62)^2) +
    x67 <= 0)
@NLconstraint(m, e145, -sqrt((x7 - x19)^2 + (x29 - x41)^2 + (x51 - x63)^2) +
    x67 <= 0)
@NLconstraint(m, e146, -sqrt((x7 - x20)^2 + (x29 - x42)^2 + (x51 - x64)^2) +
    x67 <= 0)
@NLconstraint(m, e147, -sqrt((x7 - x21)^2 + (x29 - x43)^2 + (x51 - x65)^2) +
    x67 <= 0)
@NLconstraint(m, e148, -sqrt((x7 - x22)^2 + (x29 - x44)^2 + (x51 - x66)^2) +
    x67 <= 0)
@NLconstraint(m, e149, -sqrt((x8 - x9)^2 + (x30 - x31)^2 + (x52 - x53)^2) + x67
    <= 0)
@NLconstraint(m, e150, -sqrt((x8 - x10)^2 + (x30 - x32)^2 + (x52 - x54)^2) +
    x67 <= 0)
@NLconstraint(m, e151, -sqrt((x8 - x11)^2 + (x30 - x33)^2 + (x52 - x55)^2) +
    x67 <= 0)
@NLconstraint(m, e152, -sqrt((x8 - x12)^2 + (x30 - x34)^2 + (x52 - x56)^2) +
    x67 <= 0)
@NLconstraint(m, e153, -sqrt((x8 - x13)^2 + (x30 - x35)^2 + (x52 - x57)^2) +
    x67 <= 0)
@NLconstraint(m, e154, -sqrt((x8 - x14)^2 + (x30 - x36)^2 + (x52 - x58)^2) +
    x67 <= 0)
@NLconstraint(m, e155, -sqrt((x8 - x15)^2 + (x30 - x37)^2 + (x52 - x59)^2) +
    x67 <= 0)
@NLconstraint(m, e156, -sqrt((x8 - x16)^2 + (x30 - x38)^2 + (x52 - x60)^2) +
    x67 <= 0)
@NLconstraint(m, e157, -sqrt((x8 - x17)^2 + (x30 - x39)^2 + (x52 - x61)^2) +
    x67 <= 0)
@NLconstraint(m, e158, -sqrt((x8 - x18)^2 + (x30 - x40)^2 + (x52 - x62)^2) +
    x67 <= 0)
@NLconstraint(m, e159, -sqrt((x8 - x19)^2 + (x30 - x41)^2 + (x52 - x63)^2) +
    x67 <= 0)
@NLconstraint(m, e160, -sqrt((x8 - x20)^2 + (x30 - x42)^2 + (x52 - x64)^2) +
    x67 <= 0)
@NLconstraint(m, e161, -sqrt((x8 - x21)^2 + (x30 - x43)^2 + (x52 - x65)^2) +
    x67 <= 0)
@NLconstraint(m, e162, -sqrt((x8 - x22)^2 + (x30 - x44)^2 + (x52 - x66)^2) +
    x67 <= 0)
@NLconstraint(m, e163, -sqrt((x9 - x10)^2 + (x31 - x32)^2 + (x53 - x54)^2) +
    x67 <= 0)
@NLconstraint(m, e164, -sqrt((x9 - x11)^2 + (x31 - x33)^2 + (x53 - x55)^2) +
    x67 <= 0)
@NLconstraint(m, e165, -sqrt((x9 - x12)^2 + (x31 - x34)^2 + (x53 - x56)^2) +
    x67 <= 0)
@NLconstraint(m, e166, -sqrt((x9 - x13)^2 + (x31 - x35)^2 + (x53 - x57)^2) +
    x67 <= 0)
@NLconstraint(m, e167, -sqrt((x9 - x14)^2 + (x31 - x36)^2 + (x53 - x58)^2) +
    x67 <= 0)
@NLconstraint(m, e168, -sqrt((x9 - x15)^2 + (x31 - x37)^2 + (x53 - x59)^2) +
    x67 <= 0)
@NLconstraint(m, e169, -sqrt((x9 - x16)^2 + (x31 - x38)^2 + (x53 - x60)^2) +
    x67 <= 0)
@NLconstraint(m, e170, -sqrt((x9 - x17)^2 + (x31 - x39)^2 + (x53 - x61)^2) +
    x67 <= 0)
@NLconstraint(m, e171, -sqrt((x9 - x18)^2 + (x31 - x40)^2 + (x53 - x62)^2) +
    x67 <= 0)
@NLconstraint(m, e172, -sqrt((x9 - x19)^2 + (x31 - x41)^2 + (x53 - x63)^2) +
    x67 <= 0)
@NLconstraint(m, e173, -sqrt((x9 - x20)^2 + (x31 - x42)^2 + (x53 - x64)^2) +
    x67 <= 0)
@NLconstraint(m, e174, -sqrt((x9 - x21)^2 + (x31 - x43)^2 + (x53 - x65)^2) +
    x67 <= 0)
@NLconstraint(m, e175, -sqrt((x9 - x22)^2 + (x31 - x44)^2 + (x53 - x66)^2) +
    x67 <= 0)
@NLconstraint(m, e176, -sqrt((x10 - x11)^2 + (x32 - x33)^2 + (x54 - x55)^2) +
    x67 <= 0)
@NLconstraint(m, e177, -sqrt((x10 - x12)^2 + (x32 - x34)^2 + (x54 - x56)^2) +
    x67 <= 0)
@NLconstraint(m, e178, -sqrt((x10 - x13)^2 + (x32 - x35)^2 + (x54 - x57)^2) +
    x67 <= 0)
@NLconstraint(m, e179, -sqrt((x10 - x14)^2 + (x32 - x36)^2 + (x54 - x58)^2) +
    x67 <= 0)
@NLconstraint(m, e180, -sqrt((x10 - x15)^2 + (x32 - x37)^2 + (x54 - x59)^2) +
    x67 <= 0)
@NLconstraint(m, e181, -sqrt((x10 - x16)^2 + (x32 - x38)^2 + (x54 - x60)^2) +
    x67 <= 0)
@NLconstraint(m, e182, -sqrt((x10 - x17)^2 + (x32 - x39)^2 + (x54 - x61)^2) +
    x67 <= 0)
@NLconstraint(m, e183, -sqrt((x10 - x18)^2 + (x32 - x40)^2 + (x54 - x62)^2) +
    x67 <= 0)
@NLconstraint(m, e184, -sqrt((x10 - x19)^2 + (x32 - x41)^2 + (x54 - x63)^2) +
    x67 <= 0)
@NLconstraint(m, e185, -sqrt((x10 - x20)^2 + (x32 - x42)^2 + (x54 - x64)^2) +
    x67 <= 0)
@NLconstraint(m, e186, -sqrt((x10 - x21)^2 + (x32 - x43)^2 + (x54 - x65)^2) +
    x67 <= 0)
@NLconstraint(m, e187, -sqrt((x10 - x22)^2 + (x32 - x44)^2 + (x54 - x66)^2) +
    x67 <= 0)
@NLconstraint(m, e188, -sqrt((x11 - x12)^2 + (x33 - x34)^2 + (x55 - x56)^2) +
    x67 <= 0)
@NLconstraint(m, e189, -sqrt((x11 - x13)^2 + (x33 - x35)^2 + (x55 - x57)^2) +
    x67 <= 0)
@NLconstraint(m, e190, -sqrt((x11 - x14)^2 + (x33 - x36)^2 + (x55 - x58)^2) +
    x67 <= 0)
@NLconstraint(m, e191, -sqrt((x11 - x15)^2 + (x33 - x37)^2 + (x55 - x59)^2) +
    x67 <= 0)
@NLconstraint(m, e192, -sqrt((x11 - x16)^2 + (x33 - x38)^2 + (x55 - x60)^2) +
    x67 <= 0)
@NLconstraint(m, e193, -sqrt((x11 - x17)^2 + (x33 - x39)^2 + (x55 - x61)^2) +
    x67 <= 0)
@NLconstraint(m, e194, -sqrt((x11 - x18)^2 + (x33 - x40)^2 + (x55 - x62)^2) +
    x67 <= 0)
@NLconstraint(m, e195, -sqrt((x11 - x19)^2 + (x33 - x41)^2 + (x55 - x63)^2) +
    x67 <= 0)
@NLconstraint(m, e196, -sqrt((x11 - x20)^2 + (x33 - x42)^2 + (x55 - x64)^2) +
    x67 <= 0)
@NLconstraint(m, e197, -sqrt((x11 - x21)^2 + (x33 - x43)^2 + (x55 - x65)^2) +
    x67 <= 0)
@NLconstraint(m, e198, -sqrt((x11 - x22)^2 + (x33 - x44)^2 + (x55 - x66)^2) +
    x67 <= 0)
@NLconstraint(m, e199, -sqrt((x12 - x13)^2 + (x34 - x35)^2 + (x56 - x57)^2) +
    x67 <= 0)
@NLconstraint(m, e200, -sqrt((x12 - x14)^2 + (x34 - x36)^2 + (x56 - x58)^2) +
    x67 <= 0)
@NLconstraint(m, e201, -sqrt((x12 - x15)^2 + (x34 - x37)^2 + (x56 - x59)^2) +
    x67 <= 0)
@NLconstraint(m, e202, -sqrt((x12 - x16)^2 + (x34 - x38)^2 + (x56 - x60)^2) +
    x67 <= 0)
@NLconstraint(m, e203, -sqrt((x12 - x17)^2 + (x34 - x39)^2 + (x56 - x61)^2) +
    x67 <= 0)
@NLconstraint(m, e204, -sqrt((x12 - x18)^2 + (x34 - x40)^2 + (x56 - x62)^2) +
    x67 <= 0)
@NLconstraint(m, e205, -sqrt((x12 - x19)^2 + (x34 - x41)^2 + (x56 - x63)^2) +
    x67 <= 0)
@NLconstraint(m, e206, -sqrt((x12 - x20)^2 + (x34 - x42)^2 + (x56 - x64)^2) +
    x67 <= 0)
@NLconstraint(m, e207, -sqrt((x12 - x21)^2 + (x34 - x43)^2 + (x56 - x65)^2) +
    x67 <= 0)
@NLconstraint(m, e208, -sqrt((x12 - x22)^2 + (x34 - x44)^2 + (x56 - x66)^2) +
    x67 <= 0)
@NLconstraint(m, e209, -sqrt((x13 - x14)^2 + (x35 - x36)^2 + (x57 - x58)^2) +
    x67 <= 0)
@NLconstraint(m, e210, -sqrt((x13 - x15)^2 + (x35 - x37)^2 + (x57 - x59)^2) +
    x67 <= 0)
@NLconstraint(m, e211, -sqrt((x13 - x16)^2 + (x35 - x38)^2 + (x57 - x60)^2) +
    x67 <= 0)
@NLconstraint(m, e212, -sqrt((x13 - x17)^2 + (x35 - x39)^2 + (x57 - x61)^2) +
    x67 <= 0)
@NLconstraint(m, e213, -sqrt((x13 - x18)^2 + (x35 - x40)^2 + (x57 - x62)^2) +
    x67 <= 0)
@NLconstraint(m, e214, -sqrt((x13 - x19)^2 + (x35 - x41)^2 + (x57 - x63)^2) +
    x67 <= 0)
@NLconstraint(m, e215, -sqrt((x13 - x20)^2 + (x35 - x42)^2 + (x57 - x64)^2) +
    x67 <= 0)
@NLconstraint(m, e216, -sqrt((x13 - x21)^2 + (x35 - x43)^2 + (x57 - x65)^2) +
    x67 <= 0)
@NLconstraint(m, e217, -sqrt((x13 - x22)^2 + (x35 - x44)^2 + (x57 - x66)^2) +
    x67 <= 0)
@NLconstraint(m, e218, -sqrt((x14 - x15)^2 + (x36 - x37)^2 + (x58 - x59)^2) +
    x67 <= 0)
@NLconstraint(m, e219, -sqrt((x14 - x16)^2 + (x36 - x38)^2 + (x58 - x60)^2) +
    x67 <= 0)
@NLconstraint(m, e220, -sqrt((x14 - x17)^2 + (x36 - x39)^2 + (x58 - x61)^2) +
    x67 <= 0)
@NLconstraint(m, e221, -sqrt((x14 - x18)^2 + (x36 - x40)^2 + (x58 - x62)^2) +
    x67 <= 0)
@NLconstraint(m, e222, -sqrt((x14 - x19)^2 + (x36 - x41)^2 + (x58 - x63)^2) +
    x67 <= 0)
@NLconstraint(m, e223, -sqrt((x14 - x20)^2 + (x36 - x42)^2 + (x58 - x64)^2) +
    x67 <= 0)
@NLconstraint(m, e224, -sqrt((x14 - x21)^2 + (x36 - x43)^2 + (x58 - x65)^2) +
    x67 <= 0)
@NLconstraint(m, e225, -sqrt((x14 - x22)^2 + (x36 - x44)^2 + (x58 - x66)^2) +
    x67 <= 0)
@NLconstraint(m, e226, -sqrt((x15 - x16)^2 + (x37 - x38)^2 + (x59 - x60)^2) +
    x67 <= 0)
@NLconstraint(m, e227, -sqrt((x15 - x17)^2 + (x37 - x39)^2 + (x59 - x61)^2) +
    x67 <= 0)
@NLconstraint(m, e228, -sqrt((x15 - x18)^2 + (x37 - x40)^2 + (x59 - x62)^2) +
    x67 <= 0)
@NLconstraint(m, e229, -sqrt((x15 - x19)^2 + (x37 - x41)^2 + (x59 - x63)^2) +
    x67 <= 0)
@NLconstraint(m, e230, -sqrt((x15 - x20)^2 + (x37 - x42)^2 + (x59 - x64)^2) +
    x67 <= 0)
@NLconstraint(m, e231, -sqrt((x15 - x21)^2 + (x37 - x43)^2 + (x59 - x65)^2) +
    x67 <= 0)
@NLconstraint(m, e232, -sqrt((x15 - x22)^2 + (x37 - x44)^2 + (x59 - x66)^2) +
    x67 <= 0)
@NLconstraint(m, e233, -sqrt((x16 - x17)^2 + (x38 - x39)^2 + (x60 - x61)^2) +
    x67 <= 0)
@NLconstraint(m, e234, -sqrt((x16 - x18)^2 + (x38 - x40)^2 + (x60 - x62)^2) +
    x67 <= 0)
@NLconstraint(m, e235, -sqrt((x16 - x19)^2 + (x38 - x41)^2 + (x60 - x63)^2) +
    x67 <= 0)
@NLconstraint(m, e236, -sqrt((x16 - x20)^2 + (x38 - x42)^2 + (x60 - x64)^2) +
    x67 <= 0)
@NLconstraint(m, e237, -sqrt((x16 - x21)^2 + (x38 - x43)^2 + (x60 - x65)^2) +
    x67 <= 0)
@NLconstraint(m, e238, -sqrt((x16 - x22)^2 + (x38 - x44)^2 + (x60 - x66)^2) +
    x67 <= 0)
@NLconstraint(m, e239, -sqrt((x17 - x18)^2 + (x39 - x40)^2 + (x61 - x62)^2) +
    x67 <= 0)
@NLconstraint(m, e240, -sqrt((x17 - x19)^2 + (x39 - x41)^2 + (x61 - x63)^2) +
    x67 <= 0)
@NLconstraint(m, e241, -sqrt((x17 - x20)^2 + (x39 - x42)^2 + (x61 - x64)^2) +
    x67 <= 0)
@NLconstraint(m, e242, -sqrt((x17 - x21)^2 + (x39 - x43)^2 + (x61 - x65)^2) +
    x67 <= 0)
@NLconstraint(m, e243, -sqrt((x17 - x22)^2 + (x39 - x44)^2 + (x61 - x66)^2) +
    x67 <= 0)
@NLconstraint(m, e244, -sqrt((x18 - x19)^2 + (x40 - x41)^2 + (x62 - x63)^2) +
    x67 <= 0)
@NLconstraint(m, e245, -sqrt((x18 - x20)^2 + (x40 - x42)^2 + (x62 - x64)^2) +
    x67 <= 0)
@NLconstraint(m, e246, -sqrt((x18 - x21)^2 + (x40 - x43)^2 + (x62 - x65)^2) +
    x67 <= 0)
@NLconstraint(m, e247, -sqrt((x18 - x22)^2 + (x40 - x44)^2 + (x62 - x66)^2) +
    x67 <= 0)
@NLconstraint(m, e248, -sqrt((x19 - x20)^2 + (x41 - x42)^2 + (x63 - x64)^2) +
    x67 <= 0)
@NLconstraint(m, e249, -sqrt((x19 - x21)^2 + (x41 - x43)^2 + (x63 - x65)^2) +
    x67 <= 0)
@NLconstraint(m, e250, -sqrt((x19 - x22)^2 + (x41 - x44)^2 + (x63 - x66)^2) +
    x67 <= 0)
@NLconstraint(m, e251, -sqrt((x20 - x21)^2 + (x42 - x43)^2 + (x64 - x65)^2) +
    x67 <= 0)
@NLconstraint(m, e252, -sqrt((x20 - x22)^2 + (x42 - x44)^2 + (x64 - x66)^2) +
    x67 <= 0)
@NLconstraint(m, e253, -sqrt((x21 - x22)^2 + (x43 - x44)^2 + (x65 - x66)^2) +
    x67 <= 0)
