# NLP written by GAMS Convert at 05/15/24 11:33:25
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       299       23      253       23        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        70       70        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#      1633       46     1587
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
@variable(m, x47, start=0)
@variable(m, x48, start=0)
@variable(m, x49, start=0)
@variable(m, x50, start=0)
@variable(m, x51, start=0)
@variable(m, x52, start=0)
@variable(m, x53, start=0)
@variable(m, x54, start=0)
@variable(m, x55, start=0)
@variable(m, x56, start=0)
@variable(m, x57, start=0)
@variable(m, x58, start=0)
@variable(m, x59, start=0)
@variable(m, x60, start=0)
@variable(m, x61, start=0)
@variable(m, x62, start=0)
@variable(m, x63, start=0)
@variable(m, x64, start=0)
@variable(m, x65, start=0)
@variable(m, x66, start=0)
@variable(m, x67, start=0)
@variable(m, x68, start=0)
@variable(m, x69, start=0)
@variable(m, x70, start=0)

@objective(m, Max, x70)

@NLconstraint(m, e1, (x1 - x2)^2 + (x24 - x25)^2 - (x47 + x48)^2 >= 0)
@NLconstraint(m, e2, (x1 - x3)^2 + (x24 - x26)^2 - (x47 + x49)^2 >= 0)
@NLconstraint(m, e3, (x1 - x4)^2 + (x24 - x27)^2 - (x47 + x50)^2 >= 0)
@NLconstraint(m, e4, (x1 - x5)^2 + (x24 - x28)^2 - (x47 + x51)^2 >= 0)
@NLconstraint(m, e5, (x1 - x6)^2 + (x24 - x29)^2 - (x47 + x52)^2 >= 0)
@NLconstraint(m, e6, (x1 - x7)^2 + (x24 - x30)^2 - (x47 + x53)^2 >= 0)
@NLconstraint(m, e7, (x1 - x8)^2 + (x24 - x31)^2 - (x47 + x54)^2 >= 0)
@NLconstraint(m, e8, (x1 - x9)^2 + (x24 - x32)^2 - (x47 + x55)^2 >= 0)
@NLconstraint(m, e9, (x1 - x10)^2 + (x24 - x33)^2 - (x47 + x56)^2 >= 0)
@NLconstraint(m, e10, (x1 - x11)^2 + (x24 - x34)^2 - (x47 + x57)^2 >= 0)
@NLconstraint(m, e11, (x1 - x12)^2 + (x24 - x35)^2 - (x47 + x58)^2 >= 0)
@NLconstraint(m, e12, (x1 - x13)^2 + (x24 - x36)^2 - (x47 + x59)^2 >= 0)
@NLconstraint(m, e13, (x1 - x14)^2 + (x24 - x37)^2 - (x47 + x60)^2 >= 0)
@NLconstraint(m, e14, (x1 - x15)^2 + (x24 - x38)^2 - (x47 + x61)^2 >= 0)
@NLconstraint(m, e15, (x1 - x16)^2 + (x24 - x39)^2 - (x47 + x62)^2 >= 0)
@NLconstraint(m, e16, (x1 - x17)^2 + (x24 - x40)^2 - (x47 + x63)^2 >= 0)
@NLconstraint(m, e17, (x1 - x18)^2 + (x24 - x41)^2 - (x47 + x64)^2 >= 0)
@NLconstraint(m, e18, (x1 - x19)^2 + (x24 - x42)^2 - (x47 + x65)^2 >= 0)
@NLconstraint(m, e19, (x1 - x20)^2 + (x24 - x43)^2 - (x47 + x66)^2 >= 0)
@NLconstraint(m, e20, (x1 - x21)^2 + (x24 - x44)^2 - (x47 + x67)^2 >= 0)
@NLconstraint(m, e21, (x1 - x22)^2 + (x24 - x45)^2 - (x47 + x68)^2 >= 0)
@NLconstraint(m, e22, (x1 - x23)^2 + (x24 - x46)^2 - (x47 + x69)^2 >= 0)
@NLconstraint(m, e23, (x2 - x3)^2 + (x25 - x26)^2 - (x48 + x49)^2 >= 0)
@NLconstraint(m, e24, (x2 - x4)^2 + (x25 - x27)^2 - (x48 + x50)^2 >= 0)
@NLconstraint(m, e25, (x2 - x5)^2 + (x25 - x28)^2 - (x48 + x51)^2 >= 0)
@NLconstraint(m, e26, (x2 - x6)^2 + (x25 - x29)^2 - (x48 + x52)^2 >= 0)
@NLconstraint(m, e27, (x2 - x7)^2 + (x25 - x30)^2 - (x48 + x53)^2 >= 0)
@NLconstraint(m, e28, (x2 - x8)^2 + (x25 - x31)^2 - (x48 + x54)^2 >= 0)
@NLconstraint(m, e29, (x2 - x9)^2 + (x25 - x32)^2 - (x48 + x55)^2 >= 0)
@NLconstraint(m, e30, (x2 - x10)^2 + (x25 - x33)^2 - (x48 + x56)^2 >= 0)
@NLconstraint(m, e31, (x2 - x11)^2 + (x25 - x34)^2 - (x48 + x57)^2 >= 0)
@NLconstraint(m, e32, (x2 - x12)^2 + (x25 - x35)^2 - (x48 + x58)^2 >= 0)
@NLconstraint(m, e33, (x2 - x13)^2 + (x25 - x36)^2 - (x48 + x59)^2 >= 0)
@NLconstraint(m, e34, (x2 - x14)^2 + (x25 - x37)^2 - (x48 + x60)^2 >= 0)
@NLconstraint(m, e35, (x2 - x15)^2 + (x25 - x38)^2 - (x48 + x61)^2 >= 0)
@NLconstraint(m, e36, (x2 - x16)^2 + (x25 - x39)^2 - (x48 + x62)^2 >= 0)
@NLconstraint(m, e37, (x2 - x17)^2 + (x25 - x40)^2 - (x48 + x63)^2 >= 0)
@NLconstraint(m, e38, (x2 - x18)^2 + (x25 - x41)^2 - (x48 + x64)^2 >= 0)
@NLconstraint(m, e39, (x2 - x19)^2 + (x25 - x42)^2 - (x48 + x65)^2 >= 0)
@NLconstraint(m, e40, (x2 - x20)^2 + (x25 - x43)^2 - (x48 + x66)^2 >= 0)
@NLconstraint(m, e41, (x2 - x21)^2 + (x25 - x44)^2 - (x48 + x67)^2 >= 0)
@NLconstraint(m, e42, (x2 - x22)^2 + (x25 - x45)^2 - (x48 + x68)^2 >= 0)
@NLconstraint(m, e43, (x2 - x23)^2 + (x25 - x46)^2 - (x48 + x69)^2 >= 0)
@NLconstraint(m, e44, (x3 - x4)^2 + (x26 - x27)^2 - (x49 + x50)^2 >= 0)
@NLconstraint(m, e45, (x3 - x5)^2 + (x26 - x28)^2 - (x49 + x51)^2 >= 0)
@NLconstraint(m, e46, (x3 - x6)^2 + (x26 - x29)^2 - (x49 + x52)^2 >= 0)
@NLconstraint(m, e47, (x3 - x7)^2 + (x26 - x30)^2 - (x49 + x53)^2 >= 0)
@NLconstraint(m, e48, (x3 - x8)^2 + (x26 - x31)^2 - (x49 + x54)^2 >= 0)
@NLconstraint(m, e49, (x3 - x9)^2 + (x26 - x32)^2 - (x49 + x55)^2 >= 0)
@NLconstraint(m, e50, (x3 - x10)^2 + (x26 - x33)^2 - (x49 + x56)^2 >= 0)
@NLconstraint(m, e51, (x3 - x11)^2 + (x26 - x34)^2 - (x49 + x57)^2 >= 0)
@NLconstraint(m, e52, (x3 - x12)^2 + (x26 - x35)^2 - (x49 + x58)^2 >= 0)
@NLconstraint(m, e53, (x3 - x13)^2 + (x26 - x36)^2 - (x49 + x59)^2 >= 0)
@NLconstraint(m, e54, (x3 - x14)^2 + (x26 - x37)^2 - (x49 + x60)^2 >= 0)
@NLconstraint(m, e55, (x3 - x15)^2 + (x26 - x38)^2 - (x49 + x61)^2 >= 0)
@NLconstraint(m, e56, (x3 - x16)^2 + (x26 - x39)^2 - (x49 + x62)^2 >= 0)
@NLconstraint(m, e57, (x3 - x17)^2 + (x26 - x40)^2 - (x49 + x63)^2 >= 0)
@NLconstraint(m, e58, (x3 - x18)^2 + (x26 - x41)^2 - (x49 + x64)^2 >= 0)
@NLconstraint(m, e59, (x3 - x19)^2 + (x26 - x42)^2 - (x49 + x65)^2 >= 0)
@NLconstraint(m, e60, (x3 - x20)^2 + (x26 - x43)^2 - (x49 + x66)^2 >= 0)
@NLconstraint(m, e61, (x3 - x21)^2 + (x26 - x44)^2 - (x49 + x67)^2 >= 0)
@NLconstraint(m, e62, (x3 - x22)^2 + (x26 - x45)^2 - (x49 + x68)^2 >= 0)
@NLconstraint(m, e63, (x3 - x23)^2 + (x26 - x46)^2 - (x49 + x69)^2 >= 0)
@NLconstraint(m, e64, (x4 - x5)^2 + (x27 - x28)^2 - (x50 + x51)^2 >= 0)
@NLconstraint(m, e65, (x4 - x6)^2 + (x27 - x29)^2 - (x50 + x52)^2 >= 0)
@NLconstraint(m, e66, (x4 - x7)^2 + (x27 - x30)^2 - (x50 + x53)^2 >= 0)
@NLconstraint(m, e67, (x4 - x8)^2 + (x27 - x31)^2 - (x50 + x54)^2 >= 0)
@NLconstraint(m, e68, (x4 - x9)^2 + (x27 - x32)^2 - (x50 + x55)^2 >= 0)
@NLconstraint(m, e69, (x4 - x10)^2 + (x27 - x33)^2 - (x50 + x56)^2 >= 0)
@NLconstraint(m, e70, (x4 - x11)^2 + (x27 - x34)^2 - (x50 + x57)^2 >= 0)
@NLconstraint(m, e71, (x4 - x12)^2 + (x27 - x35)^2 - (x50 + x58)^2 >= 0)
@NLconstraint(m, e72, (x4 - x13)^2 + (x27 - x36)^2 - (x50 + x59)^2 >= 0)
@NLconstraint(m, e73, (x4 - x14)^2 + (x27 - x37)^2 - (x50 + x60)^2 >= 0)
@NLconstraint(m, e74, (x4 - x15)^2 + (x27 - x38)^2 - (x50 + x61)^2 >= 0)
@NLconstraint(m, e75, (x4 - x16)^2 + (x27 - x39)^2 - (x50 + x62)^2 >= 0)
@NLconstraint(m, e76, (x4 - x17)^2 + (x27 - x40)^2 - (x50 + x63)^2 >= 0)
@NLconstraint(m, e77, (x4 - x18)^2 + (x27 - x41)^2 - (x50 + x64)^2 >= 0)
@NLconstraint(m, e78, (x4 - x19)^2 + (x27 - x42)^2 - (x50 + x65)^2 >= 0)
@NLconstraint(m, e79, (x4 - x20)^2 + (x27 - x43)^2 - (x50 + x66)^2 >= 0)
@NLconstraint(m, e80, (x4 - x21)^2 + (x27 - x44)^2 - (x50 + x67)^2 >= 0)
@NLconstraint(m, e81, (x4 - x22)^2 + (x27 - x45)^2 - (x50 + x68)^2 >= 0)
@NLconstraint(m, e82, (x4 - x23)^2 + (x27 - x46)^2 - (x50 + x69)^2 >= 0)
@NLconstraint(m, e83, (x5 - x6)^2 + (x28 - x29)^2 - (x51 + x52)^2 >= 0)
@NLconstraint(m, e84, (x5 - x7)^2 + (x28 - x30)^2 - (x51 + x53)^2 >= 0)
@NLconstraint(m, e85, (x5 - x8)^2 + (x28 - x31)^2 - (x51 + x54)^2 >= 0)
@NLconstraint(m, e86, (x5 - x9)^2 + (x28 - x32)^2 - (x51 + x55)^2 >= 0)
@NLconstraint(m, e87, (x5 - x10)^2 + (x28 - x33)^2 - (x51 + x56)^2 >= 0)
@NLconstraint(m, e88, (x5 - x11)^2 + (x28 - x34)^2 - (x51 + x57)^2 >= 0)
@NLconstraint(m, e89, (x5 - x12)^2 + (x28 - x35)^2 - (x51 + x58)^2 >= 0)
@NLconstraint(m, e90, (x5 - x13)^2 + (x28 - x36)^2 - (x51 + x59)^2 >= 0)
@NLconstraint(m, e91, (x5 - x14)^2 + (x28 - x37)^2 - (x51 + x60)^2 >= 0)
@NLconstraint(m, e92, (x5 - x15)^2 + (x28 - x38)^2 - (x51 + x61)^2 >= 0)
@NLconstraint(m, e93, (x5 - x16)^2 + (x28 - x39)^2 - (x51 + x62)^2 >= 0)
@NLconstraint(m, e94, (x5 - x17)^2 + (x28 - x40)^2 - (x51 + x63)^2 >= 0)
@NLconstraint(m, e95, (x5 - x18)^2 + (x28 - x41)^2 - (x51 + x64)^2 >= 0)
@NLconstraint(m, e96, (x5 - x19)^2 + (x28 - x42)^2 - (x51 + x65)^2 >= 0)
@NLconstraint(m, e97, (x5 - x20)^2 + (x28 - x43)^2 - (x51 + x66)^2 >= 0)
@NLconstraint(m, e98, (x5 - x21)^2 + (x28 - x44)^2 - (x51 + x67)^2 >= 0)
@NLconstraint(m, e99, (x5 - x22)^2 + (x28 - x45)^2 - (x51 + x68)^2 >= 0)
@NLconstraint(m, e100, (x5 - x23)^2 + (x28 - x46)^2 - (x51 + x69)^2 >= 0)
@NLconstraint(m, e101, (x6 - x7)^2 + (x29 - x30)^2 - (x52 + x53)^2 >= 0)
@NLconstraint(m, e102, (x6 - x8)^2 + (x29 - x31)^2 - (x52 + x54)^2 >= 0)
@NLconstraint(m, e103, (x6 - x9)^2 + (x29 - x32)^2 - (x52 + x55)^2 >= 0)
@NLconstraint(m, e104, (x6 - x10)^2 + (x29 - x33)^2 - (x52 + x56)^2 >= 0)
@NLconstraint(m, e105, (x6 - x11)^2 + (x29 - x34)^2 - (x52 + x57)^2 >= 0)
@NLconstraint(m, e106, (x6 - x12)^2 + (x29 - x35)^2 - (x52 + x58)^2 >= 0)
@NLconstraint(m, e107, (x6 - x13)^2 + (x29 - x36)^2 - (x52 + x59)^2 >= 0)
@NLconstraint(m, e108, (x6 - x14)^2 + (x29 - x37)^2 - (x52 + x60)^2 >= 0)
@NLconstraint(m, e109, (x6 - x15)^2 + (x29 - x38)^2 - (x52 + x61)^2 >= 0)
@NLconstraint(m, e110, (x6 - x16)^2 + (x29 - x39)^2 - (x52 + x62)^2 >= 0)
@NLconstraint(m, e111, (x6 - x17)^2 + (x29 - x40)^2 - (x52 + x63)^2 >= 0)
@NLconstraint(m, e112, (x6 - x18)^2 + (x29 - x41)^2 - (x52 + x64)^2 >= 0)
@NLconstraint(m, e113, (x6 - x19)^2 + (x29 - x42)^2 - (x52 + x65)^2 >= 0)
@NLconstraint(m, e114, (x6 - x20)^2 + (x29 - x43)^2 - (x52 + x66)^2 >= 0)
@NLconstraint(m, e115, (x6 - x21)^2 + (x29 - x44)^2 - (x52 + x67)^2 >= 0)
@NLconstraint(m, e116, (x6 - x22)^2 + (x29 - x45)^2 - (x52 + x68)^2 >= 0)
@NLconstraint(m, e117, (x6 - x23)^2 + (x29 - x46)^2 - (x52 + x69)^2 >= 0)
@NLconstraint(m, e118, (x7 - x8)^2 + (x30 - x31)^2 - (x53 + x54)^2 >= 0)
@NLconstraint(m, e119, (x7 - x9)^2 + (x30 - x32)^2 - (x53 + x55)^2 >= 0)
@NLconstraint(m, e120, (x7 - x10)^2 + (x30 - x33)^2 - (x53 + x56)^2 >= 0)
@NLconstraint(m, e121, (x7 - x11)^2 + (x30 - x34)^2 - (x53 + x57)^2 >= 0)
@NLconstraint(m, e122, (x7 - x12)^2 + (x30 - x35)^2 - (x53 + x58)^2 >= 0)
@NLconstraint(m, e123, (x7 - x13)^2 + (x30 - x36)^2 - (x53 + x59)^2 >= 0)
@NLconstraint(m, e124, (x7 - x14)^2 + (x30 - x37)^2 - (x53 + x60)^2 >= 0)
@NLconstraint(m, e125, (x7 - x15)^2 + (x30 - x38)^2 - (x53 + x61)^2 >= 0)
@NLconstraint(m, e126, (x7 - x16)^2 + (x30 - x39)^2 - (x53 + x62)^2 >= 0)
@NLconstraint(m, e127, (x7 - x17)^2 + (x30 - x40)^2 - (x53 + x63)^2 >= 0)
@NLconstraint(m, e128, (x7 - x18)^2 + (x30 - x41)^2 - (x53 + x64)^2 >= 0)
@NLconstraint(m, e129, (x7 - x19)^2 + (x30 - x42)^2 - (x53 + x65)^2 >= 0)
@NLconstraint(m, e130, (x7 - x20)^2 + (x30 - x43)^2 - (x53 + x66)^2 >= 0)
@NLconstraint(m, e131, (x7 - x21)^2 + (x30 - x44)^2 - (x53 + x67)^2 >= 0)
@NLconstraint(m, e132, (x7 - x22)^2 + (x30 - x45)^2 - (x53 + x68)^2 >= 0)
@NLconstraint(m, e133, (x7 - x23)^2 + (x30 - x46)^2 - (x53 + x69)^2 >= 0)
@NLconstraint(m, e134, (x8 - x9)^2 + (x31 - x32)^2 - (x54 + x55)^2 >= 0)
@NLconstraint(m, e135, (x8 - x10)^2 + (x31 - x33)^2 - (x54 + x56)^2 >= 0)
@NLconstraint(m, e136, (x8 - x11)^2 + (x31 - x34)^2 - (x54 + x57)^2 >= 0)
@NLconstraint(m, e137, (x8 - x12)^2 + (x31 - x35)^2 - (x54 + x58)^2 >= 0)
@NLconstraint(m, e138, (x8 - x13)^2 + (x31 - x36)^2 - (x54 + x59)^2 >= 0)
@NLconstraint(m, e139, (x8 - x14)^2 + (x31 - x37)^2 - (x54 + x60)^2 >= 0)
@NLconstraint(m, e140, (x8 - x15)^2 + (x31 - x38)^2 - (x54 + x61)^2 >= 0)
@NLconstraint(m, e141, (x8 - x16)^2 + (x31 - x39)^2 - (x54 + x62)^2 >= 0)
@NLconstraint(m, e142, (x8 - x17)^2 + (x31 - x40)^2 - (x54 + x63)^2 >= 0)
@NLconstraint(m, e143, (x8 - x18)^2 + (x31 - x41)^2 - (x54 + x64)^2 >= 0)
@NLconstraint(m, e144, (x8 - x19)^2 + (x31 - x42)^2 - (x54 + x65)^2 >= 0)
@NLconstraint(m, e145, (x8 - x20)^2 + (x31 - x43)^2 - (x54 + x66)^2 >= 0)
@NLconstraint(m, e146, (x8 - x21)^2 + (x31 - x44)^2 - (x54 + x67)^2 >= 0)
@NLconstraint(m, e147, (x8 - x22)^2 + (x31 - x45)^2 - (x54 + x68)^2 >= 0)
@NLconstraint(m, e148, (x8 - x23)^2 + (x31 - x46)^2 - (x54 + x69)^2 >= 0)
@NLconstraint(m, e149, (x9 - x10)^2 + (x32 - x33)^2 - (x55 + x56)^2 >= 0)
@NLconstraint(m, e150, (x9 - x11)^2 + (x32 - x34)^2 - (x55 + x57)^2 >= 0)
@NLconstraint(m, e151, (x9 - x12)^2 + (x32 - x35)^2 - (x55 + x58)^2 >= 0)
@NLconstraint(m, e152, (x9 - x13)^2 + (x32 - x36)^2 - (x55 + x59)^2 >= 0)
@NLconstraint(m, e153, (x9 - x14)^2 + (x32 - x37)^2 - (x55 + x60)^2 >= 0)
@NLconstraint(m, e154, (x9 - x15)^2 + (x32 - x38)^2 - (x55 + x61)^2 >= 0)
@NLconstraint(m, e155, (x9 - x16)^2 + (x32 - x39)^2 - (x55 + x62)^2 >= 0)
@NLconstraint(m, e156, (x9 - x17)^2 + (x32 - x40)^2 - (x55 + x63)^2 >= 0)
@NLconstraint(m, e157, (x9 - x18)^2 + (x32 - x41)^2 - (x55 + x64)^2 >= 0)
@NLconstraint(m, e158, (x9 - x19)^2 + (x32 - x42)^2 - (x55 + x65)^2 >= 0)
@NLconstraint(m, e159, (x9 - x20)^2 + (x32 - x43)^2 - (x55 + x66)^2 >= 0)
@NLconstraint(m, e160, (x9 - x21)^2 + (x32 - x44)^2 - (x55 + x67)^2 >= 0)
@NLconstraint(m, e161, (x9 - x22)^2 + (x32 - x45)^2 - (x55 + x68)^2 >= 0)
@NLconstraint(m, e162, (x9 - x23)^2 + (x32 - x46)^2 - (x55 + x69)^2 >= 0)
@NLconstraint(m, e163, (x10 - x11)^2 + (x33 - x34)^2 - (x56 + x57)^2 >= 0)
@NLconstraint(m, e164, (x10 - x12)^2 + (x33 - x35)^2 - (x56 + x58)^2 >= 0)
@NLconstraint(m, e165, (x10 - x13)^2 + (x33 - x36)^2 - (x56 + x59)^2 >= 0)
@NLconstraint(m, e166, (x10 - x14)^2 + (x33 - x37)^2 - (x56 + x60)^2 >= 0)
@NLconstraint(m, e167, (x10 - x15)^2 + (x33 - x38)^2 - (x56 + x61)^2 >= 0)
@NLconstraint(m, e168, (x10 - x16)^2 + (x33 - x39)^2 - (x56 + x62)^2 >= 0)
@NLconstraint(m, e169, (x10 - x17)^2 + (x33 - x40)^2 - (x56 + x63)^2 >= 0)
@NLconstraint(m, e170, (x10 - x18)^2 + (x33 - x41)^2 - (x56 + x64)^2 >= 0)
@NLconstraint(m, e171, (x10 - x19)^2 + (x33 - x42)^2 - (x56 + x65)^2 >= 0)
@NLconstraint(m, e172, (x10 - x20)^2 + (x33 - x43)^2 - (x56 + x66)^2 >= 0)
@NLconstraint(m, e173, (x10 - x21)^2 + (x33 - x44)^2 - (x56 + x67)^2 >= 0)
@NLconstraint(m, e174, (x10 - x22)^2 + (x33 - x45)^2 - (x56 + x68)^2 >= 0)
@NLconstraint(m, e175, (x10 - x23)^2 + (x33 - x46)^2 - (x56 + x69)^2 >= 0)
@NLconstraint(m, e176, (x11 - x12)^2 + (x34 - x35)^2 - (x57 + x58)^2 >= 0)
@NLconstraint(m, e177, (x11 - x13)^2 + (x34 - x36)^2 - (x57 + x59)^2 >= 0)
@NLconstraint(m, e178, (x11 - x14)^2 + (x34 - x37)^2 - (x57 + x60)^2 >= 0)
@NLconstraint(m, e179, (x11 - x15)^2 + (x34 - x38)^2 - (x57 + x61)^2 >= 0)
@NLconstraint(m, e180, (x11 - x16)^2 + (x34 - x39)^2 - (x57 + x62)^2 >= 0)
@NLconstraint(m, e181, (x11 - x17)^2 + (x34 - x40)^2 - (x57 + x63)^2 >= 0)
@NLconstraint(m, e182, (x11 - x18)^2 + (x34 - x41)^2 - (x57 + x64)^2 >= 0)
@NLconstraint(m, e183, (x11 - x19)^2 + (x34 - x42)^2 - (x57 + x65)^2 >= 0)
@NLconstraint(m, e184, (x11 - x20)^2 + (x34 - x43)^2 - (x57 + x66)^2 >= 0)
@NLconstraint(m, e185, (x11 - x21)^2 + (x34 - x44)^2 - (x57 + x67)^2 >= 0)
@NLconstraint(m, e186, (x11 - x22)^2 + (x34 - x45)^2 - (x57 + x68)^2 >= 0)
@NLconstraint(m, e187, (x11 - x23)^2 + (x34 - x46)^2 - (x57 + x69)^2 >= 0)
@NLconstraint(m, e188, (x12 - x13)^2 + (x35 - x36)^2 - (x58 + x59)^2 >= 0)
@NLconstraint(m, e189, (x12 - x14)^2 + (x35 - x37)^2 - (x58 + x60)^2 >= 0)
@NLconstraint(m, e190, (x12 - x15)^2 + (x35 - x38)^2 - (x58 + x61)^2 >= 0)
@NLconstraint(m, e191, (x12 - x16)^2 + (x35 - x39)^2 - (x58 + x62)^2 >= 0)
@NLconstraint(m, e192, (x12 - x17)^2 + (x35 - x40)^2 - (x58 + x63)^2 >= 0)
@NLconstraint(m, e193, (x12 - x18)^2 + (x35 - x41)^2 - (x58 + x64)^2 >= 0)
@NLconstraint(m, e194, (x12 - x19)^2 + (x35 - x42)^2 - (x58 + x65)^2 >= 0)
@NLconstraint(m, e195, (x12 - x20)^2 + (x35 - x43)^2 - (x58 + x66)^2 >= 0)
@NLconstraint(m, e196, (x12 - x21)^2 + (x35 - x44)^2 - (x58 + x67)^2 >= 0)
@NLconstraint(m, e197, (x12 - x22)^2 + (x35 - x45)^2 - (x58 + x68)^2 >= 0)
@NLconstraint(m, e198, (x12 - x23)^2 + (x35 - x46)^2 - (x58 + x69)^2 >= 0)
@NLconstraint(m, e199, (x13 - x14)^2 + (x36 - x37)^2 - (x59 + x60)^2 >= 0)
@NLconstraint(m, e200, (x13 - x15)^2 + (x36 - x38)^2 - (x59 + x61)^2 >= 0)
@NLconstraint(m, e201, (x13 - x16)^2 + (x36 - x39)^2 - (x59 + x62)^2 >= 0)
@NLconstraint(m, e202, (x13 - x17)^2 + (x36 - x40)^2 - (x59 + x63)^2 >= 0)
@NLconstraint(m, e203, (x13 - x18)^2 + (x36 - x41)^2 - (x59 + x64)^2 >= 0)
@NLconstraint(m, e204, (x13 - x19)^2 + (x36 - x42)^2 - (x59 + x65)^2 >= 0)
@NLconstraint(m, e205, (x13 - x20)^2 + (x36 - x43)^2 - (x59 + x66)^2 >= 0)
@NLconstraint(m, e206, (x13 - x21)^2 + (x36 - x44)^2 - (x59 + x67)^2 >= 0)
@NLconstraint(m, e207, (x13 - x22)^2 + (x36 - x45)^2 - (x59 + x68)^2 >= 0)
@NLconstraint(m, e208, (x13 - x23)^2 + (x36 - x46)^2 - (x59 + x69)^2 >= 0)
@NLconstraint(m, e209, (x14 - x15)^2 + (x37 - x38)^2 - (x60 + x61)^2 >= 0)
@NLconstraint(m, e210, (x14 - x16)^2 + (x37 - x39)^2 - (x60 + x62)^2 >= 0)
@NLconstraint(m, e211, (x14 - x17)^2 + (x37 - x40)^2 - (x60 + x63)^2 >= 0)
@NLconstraint(m, e212, (x14 - x18)^2 + (x37 - x41)^2 - (x60 + x64)^2 >= 0)
@NLconstraint(m, e213, (x14 - x19)^2 + (x37 - x42)^2 - (x60 + x65)^2 >= 0)
@NLconstraint(m, e214, (x14 - x20)^2 + (x37 - x43)^2 - (x60 + x66)^2 >= 0)
@NLconstraint(m, e215, (x14 - x21)^2 + (x37 - x44)^2 - (x60 + x67)^2 >= 0)
@NLconstraint(m, e216, (x14 - x22)^2 + (x37 - x45)^2 - (x60 + x68)^2 >= 0)
@NLconstraint(m, e217, (x14 - x23)^2 + (x37 - x46)^2 - (x60 + x69)^2 >= 0)
@NLconstraint(m, e218, (x15 - x16)^2 + (x38 - x39)^2 - (x61 + x62)^2 >= 0)
@NLconstraint(m, e219, (x15 - x17)^2 + (x38 - x40)^2 - (x61 + x63)^2 >= 0)
@NLconstraint(m, e220, (x15 - x18)^2 + (x38 - x41)^2 - (x61 + x64)^2 >= 0)
@NLconstraint(m, e221, (x15 - x19)^2 + (x38 - x42)^2 - (x61 + x65)^2 >= 0)
@NLconstraint(m, e222, (x15 - x20)^2 + (x38 - x43)^2 - (x61 + x66)^2 >= 0)
@NLconstraint(m, e223, (x15 - x21)^2 + (x38 - x44)^2 - (x61 + x67)^2 >= 0)
@NLconstraint(m, e224, (x15 - x22)^2 + (x38 - x45)^2 - (x61 + x68)^2 >= 0)
@NLconstraint(m, e225, (x15 - x23)^2 + (x38 - x46)^2 - (x61 + x69)^2 >= 0)
@NLconstraint(m, e226, (x16 - x17)^2 + (x39 - x40)^2 - (x62 + x63)^2 >= 0)
@NLconstraint(m, e227, (x16 - x18)^2 + (x39 - x41)^2 - (x62 + x64)^2 >= 0)
@NLconstraint(m, e228, (x16 - x19)^2 + (x39 - x42)^2 - (x62 + x65)^2 >= 0)
@NLconstraint(m, e229, (x16 - x20)^2 + (x39 - x43)^2 - (x62 + x66)^2 >= 0)
@NLconstraint(m, e230, (x16 - x21)^2 + (x39 - x44)^2 - (x62 + x67)^2 >= 0)
@NLconstraint(m, e231, (x16 - x22)^2 + (x39 - x45)^2 - (x62 + x68)^2 >= 0)
@NLconstraint(m, e232, (x16 - x23)^2 + (x39 - x46)^2 - (x62 + x69)^2 >= 0)
@NLconstraint(m, e233, (x17 - x18)^2 + (x40 - x41)^2 - (x63 + x64)^2 >= 0)
@NLconstraint(m, e234, (x17 - x19)^2 + (x40 - x42)^2 - (x63 + x65)^2 >= 0)
@NLconstraint(m, e235, (x17 - x20)^2 + (x40 - x43)^2 - (x63 + x66)^2 >= 0)
@NLconstraint(m, e236, (x17 - x21)^2 + (x40 - x44)^2 - (x63 + x67)^2 >= 0)
@NLconstraint(m, e237, (x17 - x22)^2 + (x40 - x45)^2 - (x63 + x68)^2 >= 0)
@NLconstraint(m, e238, (x17 - x23)^2 + (x40 - x46)^2 - (x63 + x69)^2 >= 0)
@NLconstraint(m, e239, (x18 - x19)^2 + (x41 - x42)^2 - (x64 + x65)^2 >= 0)
@NLconstraint(m, e240, (x18 - x20)^2 + (x41 - x43)^2 - (x64 + x66)^2 >= 0)
@NLconstraint(m, e241, (x18 - x21)^2 + (x41 - x44)^2 - (x64 + x67)^2 >= 0)
@NLconstraint(m, e242, (x18 - x22)^2 + (x41 - x45)^2 - (x64 + x68)^2 >= 0)
@NLconstraint(m, e243, (x18 - x23)^2 + (x41 - x46)^2 - (x64 + x69)^2 >= 0)
@NLconstraint(m, e244, (x19 - x20)^2 + (x42 - x43)^2 - (x65 + x66)^2 >= 0)
@NLconstraint(m, e245, (x19 - x21)^2 + (x42 - x44)^2 - (x65 + x67)^2 >= 0)
@NLconstraint(m, e246, (x19 - x22)^2 + (x42 - x45)^2 - (x65 + x68)^2 >= 0)
@NLconstraint(m, e247, (x19 - x23)^2 + (x42 - x46)^2 - (x65 + x69)^2 >= 0)
@NLconstraint(m, e248, (x20 - x21)^2 + (x43 - x44)^2 - (x66 + x67)^2 >= 0)
@NLconstraint(m, e249, (x20 - x22)^2 + (x43 - x45)^2 - (x66 + x68)^2 >= 0)
@NLconstraint(m, e250, (x20 - x23)^2 + (x43 - x46)^2 - (x66 + x69)^2 >= 0)
@NLconstraint(m, e251, (x21 - x22)^2 + (x44 - x45)^2 - (x67 + x68)^2 >= 0)
@NLconstraint(m, e252, (x21 - x23)^2 + (x44 - x46)^2 - (x67 + x69)^2 >= 0)
@NLconstraint(m, e253, (x22 - x23)^2 + (x45 - x46)^2 - (x68 + x69)^2 >= 0)
@constraint(m, e254, x47 - x70 == 0)
@constraint(m, e255, x48 - x70 == 0)
@constraint(m, e256, x49 - x70 == 0)
@constraint(m, e257, x50 - x70 == 0)
@constraint(m, e258, x51 - x70 == 0)
@constraint(m, e259, x52 - x70 == 0)
@constraint(m, e260, x53 - x70 == 0)
@constraint(m, e261, x54 - x70 == 0)
@constraint(m, e262, x55 - x70 == 0)
@constraint(m, e263, x56 - x70 == 0)
@constraint(m, e264, x57 - x70 == 0)
@constraint(m, e265, x58 - x70 == 0)
@constraint(m, e266, x59 - x70 == 0)
@constraint(m, e267, x60 - x70 == 0)
@constraint(m, e268, x61 - x70 == 0)
@constraint(m, e269, x62 - x70 == 0)
@constraint(m, e270, x63 - x70 == 0)
@constraint(m, e271, x64 - x70 == 0)
@constraint(m, e272, x65 - x70 == 0)
@constraint(m, e273, x66 - x70 == 0)
@constraint(m, e274, x67 - x70 == 0)
@constraint(m, e275, x68 - x70 == 0)
@constraint(m, e276, x69 - x70 == 0)
@NLconstraint(m, e277, x1^2 + x24^2 - (1 - x47)^2 <= 0)
@NLconstraint(m, e278, x2^2 + x25^2 - (1 - x48)^2 <= 0)
@NLconstraint(m, e279, x3^2 + x26^2 - (1 - x49)^2 <= 0)
@NLconstraint(m, e280, x4^2 + x27^2 - (1 - x50)^2 <= 0)
@NLconstraint(m, e281, x5^2 + x28^2 - (1 - x51)^2 <= 0)
@NLconstraint(m, e282, x6^2 + x29^2 - (1 - x52)^2 <= 0)
@NLconstraint(m, e283, x7^2 + x30^2 - (1 - x53)^2 <= 0)
@NLconstraint(m, e284, x8^2 + x31^2 - (1 - x54)^2 <= 0)
@NLconstraint(m, e285, x9^2 + x32^2 - (1 - x55)^2 <= 0)
@NLconstraint(m, e286, x10^2 + x33^2 - (1 - x56)^2 <= 0)
@NLconstraint(m, e287, x11^2 + x34^2 - (1 - x57)^2 <= 0)
@NLconstraint(m, e288, x12^2 + x35^2 - (1 - x58)^2 <= 0)
@NLconstraint(m, e289, x13^2 + x36^2 - (1 - x59)^2 <= 0)
@NLconstraint(m, e290, x14^2 + x37^2 - (1 - x60)^2 <= 0)
@NLconstraint(m, e291, x15^2 + x38^2 - (1 - x61)^2 <= 0)
@NLconstraint(m, e292, x16^2 + x39^2 - (1 - x62)^2 <= 0)
@NLconstraint(m, e293, x17^2 + x40^2 - (1 - x63)^2 <= 0)
@NLconstraint(m, e294, x18^2 + x41^2 - (1 - x64)^2 <= 0)
@NLconstraint(m, e295, x19^2 + x42^2 - (1 - x65)^2 <= 0)
@NLconstraint(m, e296, x20^2 + x43^2 - (1 - x66)^2 <= 0)
@NLconstraint(m, e297, x21^2 + x44^2 - (1 - x67)^2 <= 0)
@NLconstraint(m, e298, x22^2 + x45^2 - (1 - x68)^2 <= 0)
@NLconstraint(m, e299, x23^2 + x46^2 - (1 - x69)^2 <= 0)
