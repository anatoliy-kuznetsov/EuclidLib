# NLP written by GAMS Convert at 05/15/24 11:27:03
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       153       17        0      136        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        52       52        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#      1003      136      867
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
@variable(m, x52, start=0)

@objective(m, Max, x52)

@NLconstraint(m, e1, x1^2 + x18^2 + x35^2 == 1)
@NLconstraint(m, e2, x2^2 + x19^2 + x36^2 == 1)
@NLconstraint(m, e3, x3^2 + x20^2 + x37^2 == 1)
@NLconstraint(m, e4, x4^2 + x21^2 + x38^2 == 1)
@NLconstraint(m, e5, x5^2 + x22^2 + x39^2 == 1)
@NLconstraint(m, e6, x6^2 + x23^2 + x40^2 == 1)
@NLconstraint(m, e7, x7^2 + x24^2 + x41^2 == 1)
@NLconstraint(m, e8, x8^2 + x25^2 + x42^2 == 1)
@NLconstraint(m, e9, x9^2 + x26^2 + x43^2 == 1)
@NLconstraint(m, e10, x10^2 + x27^2 + x44^2 == 1)
@NLconstraint(m, e11, x11^2 + x28^2 + x45^2 == 1)
@NLconstraint(m, e12, x12^2 + x29^2 + x46^2 == 1)
@NLconstraint(m, e13, x13^2 + x30^2 + x47^2 == 1)
@NLconstraint(m, e14, x14^2 + x31^2 + x48^2 == 1)
@NLconstraint(m, e15, x15^2 + x32^2 + x49^2 == 1)
@NLconstraint(m, e16, x16^2 + x33^2 + x50^2 == 1)
@NLconstraint(m, e17, x17^2 + x34^2 + x51^2 == 1)
@NLconstraint(m, e18, -sqrt((x1 - x2)^2 + (x18 - x19)^2 + (x35 - x36)^2) + x52
    <= 0)
@NLconstraint(m, e19, -sqrt((x1 - x3)^2 + (x18 - x20)^2 + (x35 - x37)^2) + x52
    <= 0)
@NLconstraint(m, e20, -sqrt((x1 - x4)^2 + (x18 - x21)^2 + (x35 - x38)^2) + x52
    <= 0)
@NLconstraint(m, e21, -sqrt((x1 - x5)^2 + (x18 - x22)^2 + (x35 - x39)^2) + x52
    <= 0)
@NLconstraint(m, e22, -sqrt((x1 - x6)^2 + (x18 - x23)^2 + (x35 - x40)^2) + x52
    <= 0)
@NLconstraint(m, e23, -sqrt((x1 - x7)^2 + (x18 - x24)^2 + (x35 - x41)^2) + x52
    <= 0)
@NLconstraint(m, e24, -sqrt((x1 - x8)^2 + (x18 - x25)^2 + (x35 - x42)^2) + x52
    <= 0)
@NLconstraint(m, e25, -sqrt((x1 - x9)^2 + (x18 - x26)^2 + (x35 - x43)^2) + x52
    <= 0)
@NLconstraint(m, e26, -sqrt((x1 - x10)^2 + (x18 - x27)^2 + (x35 - x44)^2) + x52
    <= 0)
@NLconstraint(m, e27, -sqrt((x1 - x11)^2 + (x18 - x28)^2 + (x35 - x45)^2) + x52
    <= 0)
@NLconstraint(m, e28, -sqrt((x1 - x12)^2 + (x18 - x29)^2 + (x35 - x46)^2) + x52
    <= 0)
@NLconstraint(m, e29, -sqrt((x1 - x13)^2 + (x18 - x30)^2 + (x35 - x47)^2) + x52
    <= 0)
@NLconstraint(m, e30, -sqrt((x1 - x14)^2 + (x18 - x31)^2 + (x35 - x48)^2) + x52
    <= 0)
@NLconstraint(m, e31, -sqrt((x1 - x15)^2 + (x18 - x32)^2 + (x35 - x49)^2) + x52
    <= 0)
@NLconstraint(m, e32, -sqrt((x1 - x16)^2 + (x18 - x33)^2 + (x35 - x50)^2) + x52
    <= 0)
@NLconstraint(m, e33, -sqrt((x1 - x17)^2 + (x18 - x34)^2 + (x35 - x51)^2) + x52
    <= 0)
@NLconstraint(m, e34, -sqrt((x2 - x3)^2 + (x19 - x20)^2 + (x36 - x37)^2) + x52
    <= 0)
@NLconstraint(m, e35, -sqrt((x2 - x4)^2 + (x19 - x21)^2 + (x36 - x38)^2) + x52
    <= 0)
@NLconstraint(m, e36, -sqrt((x2 - x5)^2 + (x19 - x22)^2 + (x36 - x39)^2) + x52
    <= 0)
@NLconstraint(m, e37, -sqrt((x2 - x6)^2 + (x19 - x23)^2 + (x36 - x40)^2) + x52
    <= 0)
@NLconstraint(m, e38, -sqrt((x2 - x7)^2 + (x19 - x24)^2 + (x36 - x41)^2) + x52
    <= 0)
@NLconstraint(m, e39, -sqrt((x2 - x8)^2 + (x19 - x25)^2 + (x36 - x42)^2) + x52
    <= 0)
@NLconstraint(m, e40, -sqrt((x2 - x9)^2 + (x19 - x26)^2 + (x36 - x43)^2) + x52
    <= 0)
@NLconstraint(m, e41, -sqrt((x2 - x10)^2 + (x19 - x27)^2 + (x36 - x44)^2) + x52
    <= 0)
@NLconstraint(m, e42, -sqrt((x2 - x11)^2 + (x19 - x28)^2 + (x36 - x45)^2) + x52
    <= 0)
@NLconstraint(m, e43, -sqrt((x2 - x12)^2 + (x19 - x29)^2 + (x36 - x46)^2) + x52
    <= 0)
@NLconstraint(m, e44, -sqrt((x2 - x13)^2 + (x19 - x30)^2 + (x36 - x47)^2) + x52
    <= 0)
@NLconstraint(m, e45, -sqrt((x2 - x14)^2 + (x19 - x31)^2 + (x36 - x48)^2) + x52
    <= 0)
@NLconstraint(m, e46, -sqrt((x2 - x15)^2 + (x19 - x32)^2 + (x36 - x49)^2) + x52
    <= 0)
@NLconstraint(m, e47, -sqrt((x2 - x16)^2 + (x19 - x33)^2 + (x36 - x50)^2) + x52
    <= 0)
@NLconstraint(m, e48, -sqrt((x2 - x17)^2 + (x19 - x34)^2 + (x36 - x51)^2) + x52
    <= 0)
@NLconstraint(m, e49, -sqrt((x3 - x4)^2 + (x20 - x21)^2 + (x37 - x38)^2) + x52
    <= 0)
@NLconstraint(m, e50, -sqrt((x3 - x5)^2 + (x20 - x22)^2 + (x37 - x39)^2) + x52
    <= 0)
@NLconstraint(m, e51, -sqrt((x3 - x6)^2 + (x20 - x23)^2 + (x37 - x40)^2) + x52
    <= 0)
@NLconstraint(m, e52, -sqrt((x3 - x7)^2 + (x20 - x24)^2 + (x37 - x41)^2) + x52
    <= 0)
@NLconstraint(m, e53, -sqrt((x3 - x8)^2 + (x20 - x25)^2 + (x37 - x42)^2) + x52
    <= 0)
@NLconstraint(m, e54, -sqrt((x3 - x9)^2 + (x20 - x26)^2 + (x37 - x43)^2) + x52
    <= 0)
@NLconstraint(m, e55, -sqrt((x3 - x10)^2 + (x20 - x27)^2 + (x37 - x44)^2) + x52
    <= 0)
@NLconstraint(m, e56, -sqrt((x3 - x11)^2 + (x20 - x28)^2 + (x37 - x45)^2) + x52
    <= 0)
@NLconstraint(m, e57, -sqrt((x3 - x12)^2 + (x20 - x29)^2 + (x37 - x46)^2) + x52
    <= 0)
@NLconstraint(m, e58, -sqrt((x3 - x13)^2 + (x20 - x30)^2 + (x37 - x47)^2) + x52
    <= 0)
@NLconstraint(m, e59, -sqrt((x3 - x14)^2 + (x20 - x31)^2 + (x37 - x48)^2) + x52
    <= 0)
@NLconstraint(m, e60, -sqrt((x3 - x15)^2 + (x20 - x32)^2 + (x37 - x49)^2) + x52
    <= 0)
@NLconstraint(m, e61, -sqrt((x3 - x16)^2 + (x20 - x33)^2 + (x37 - x50)^2) + x52
    <= 0)
@NLconstraint(m, e62, -sqrt((x3 - x17)^2 + (x20 - x34)^2 + (x37 - x51)^2) + x52
    <= 0)
@NLconstraint(m, e63, -sqrt((x4 - x5)^2 + (x21 - x22)^2 + (x38 - x39)^2) + x52
    <= 0)
@NLconstraint(m, e64, -sqrt((x4 - x6)^2 + (x21 - x23)^2 + (x38 - x40)^2) + x52
    <= 0)
@NLconstraint(m, e65, -sqrt((x4 - x7)^2 + (x21 - x24)^2 + (x38 - x41)^2) + x52
    <= 0)
@NLconstraint(m, e66, -sqrt((x4 - x8)^2 + (x21 - x25)^2 + (x38 - x42)^2) + x52
    <= 0)
@NLconstraint(m, e67, -sqrt((x4 - x9)^2 + (x21 - x26)^2 + (x38 - x43)^2) + x52
    <= 0)
@NLconstraint(m, e68, -sqrt((x4 - x10)^2 + (x21 - x27)^2 + (x38 - x44)^2) + x52
    <= 0)
@NLconstraint(m, e69, -sqrt((x4 - x11)^2 + (x21 - x28)^2 + (x38 - x45)^2) + x52
    <= 0)
@NLconstraint(m, e70, -sqrt((x4 - x12)^2 + (x21 - x29)^2 + (x38 - x46)^2) + x52
    <= 0)
@NLconstraint(m, e71, -sqrt((x4 - x13)^2 + (x21 - x30)^2 + (x38 - x47)^2) + x52
    <= 0)
@NLconstraint(m, e72, -sqrt((x4 - x14)^2 + (x21 - x31)^2 + (x38 - x48)^2) + x52
    <= 0)
@NLconstraint(m, e73, -sqrt((x4 - x15)^2 + (x21 - x32)^2 + (x38 - x49)^2) + x52
    <= 0)
@NLconstraint(m, e74, -sqrt((x4 - x16)^2 + (x21 - x33)^2 + (x38 - x50)^2) + x52
    <= 0)
@NLconstraint(m, e75, -sqrt((x4 - x17)^2 + (x21 - x34)^2 + (x38 - x51)^2) + x52
    <= 0)
@NLconstraint(m, e76, -sqrt((x5 - x6)^2 + (x22 - x23)^2 + (x39 - x40)^2) + x52
    <= 0)
@NLconstraint(m, e77, -sqrt((x5 - x7)^2 + (x22 - x24)^2 + (x39 - x41)^2) + x52
    <= 0)
@NLconstraint(m, e78, -sqrt((x5 - x8)^2 + (x22 - x25)^2 + (x39 - x42)^2) + x52
    <= 0)
@NLconstraint(m, e79, -sqrt((x5 - x9)^2 + (x22 - x26)^2 + (x39 - x43)^2) + x52
    <= 0)
@NLconstraint(m, e80, -sqrt((x5 - x10)^2 + (x22 - x27)^2 + (x39 - x44)^2) + x52
    <= 0)
@NLconstraint(m, e81, -sqrt((x5 - x11)^2 + (x22 - x28)^2 + (x39 - x45)^2) + x52
    <= 0)
@NLconstraint(m, e82, -sqrt((x5 - x12)^2 + (x22 - x29)^2 + (x39 - x46)^2) + x52
    <= 0)
@NLconstraint(m, e83, -sqrt((x5 - x13)^2 + (x22 - x30)^2 + (x39 - x47)^2) + x52
    <= 0)
@NLconstraint(m, e84, -sqrt((x5 - x14)^2 + (x22 - x31)^2 + (x39 - x48)^2) + x52
    <= 0)
@NLconstraint(m, e85, -sqrt((x5 - x15)^2 + (x22 - x32)^2 + (x39 - x49)^2) + x52
    <= 0)
@NLconstraint(m, e86, -sqrt((x5 - x16)^2 + (x22 - x33)^2 + (x39 - x50)^2) + x52
    <= 0)
@NLconstraint(m, e87, -sqrt((x5 - x17)^2 + (x22 - x34)^2 + (x39 - x51)^2) + x52
    <= 0)
@NLconstraint(m, e88, -sqrt((x6 - x7)^2 + (x23 - x24)^2 + (x40 - x41)^2) + x52
    <= 0)
@NLconstraint(m, e89, -sqrt((x6 - x8)^2 + (x23 - x25)^2 + (x40 - x42)^2) + x52
    <= 0)
@NLconstraint(m, e90, -sqrt((x6 - x9)^2 + (x23 - x26)^2 + (x40 - x43)^2) + x52
    <= 0)
@NLconstraint(m, e91, -sqrt((x6 - x10)^2 + (x23 - x27)^2 + (x40 - x44)^2) + x52
    <= 0)
@NLconstraint(m, e92, -sqrt((x6 - x11)^2 + (x23 - x28)^2 + (x40 - x45)^2) + x52
    <= 0)
@NLconstraint(m, e93, -sqrt((x6 - x12)^2 + (x23 - x29)^2 + (x40 - x46)^2) + x52
    <= 0)
@NLconstraint(m, e94, -sqrt((x6 - x13)^2 + (x23 - x30)^2 + (x40 - x47)^2) + x52
    <= 0)
@NLconstraint(m, e95, -sqrt((x6 - x14)^2 + (x23 - x31)^2 + (x40 - x48)^2) + x52
    <= 0)
@NLconstraint(m, e96, -sqrt((x6 - x15)^2 + (x23 - x32)^2 + (x40 - x49)^2) + x52
    <= 0)
@NLconstraint(m, e97, -sqrt((x6 - x16)^2 + (x23 - x33)^2 + (x40 - x50)^2) + x52
    <= 0)
@NLconstraint(m, e98, -sqrt((x6 - x17)^2 + (x23 - x34)^2 + (x40 - x51)^2) + x52
    <= 0)
@NLconstraint(m, e99, -sqrt((x7 - x8)^2 + (x24 - x25)^2 + (x41 - x42)^2) + x52
    <= 0)
@NLconstraint(m, e100, -sqrt((x7 - x9)^2 + (x24 - x26)^2 + (x41 - x43)^2) + x52
    <= 0)
@NLconstraint(m, e101, -sqrt((x7 - x10)^2 + (x24 - x27)^2 + (x41 - x44)^2) +
    x52 <= 0)
@NLconstraint(m, e102, -sqrt((x7 - x11)^2 + (x24 - x28)^2 + (x41 - x45)^2) +
    x52 <= 0)
@NLconstraint(m, e103, -sqrt((x7 - x12)^2 + (x24 - x29)^2 + (x41 - x46)^2) +
    x52 <= 0)
@NLconstraint(m, e104, -sqrt((x7 - x13)^2 + (x24 - x30)^2 + (x41 - x47)^2) +
    x52 <= 0)
@NLconstraint(m, e105, -sqrt((x7 - x14)^2 + (x24 - x31)^2 + (x41 - x48)^2) +
    x52 <= 0)
@NLconstraint(m, e106, -sqrt((x7 - x15)^2 + (x24 - x32)^2 + (x41 - x49)^2) +
    x52 <= 0)
@NLconstraint(m, e107, -sqrt((x7 - x16)^2 + (x24 - x33)^2 + (x41 - x50)^2) +
    x52 <= 0)
@NLconstraint(m, e108, -sqrt((x7 - x17)^2 + (x24 - x34)^2 + (x41 - x51)^2) +
    x52 <= 0)
@NLconstraint(m, e109, -sqrt((x8 - x9)^2 + (x25 - x26)^2 + (x42 - x43)^2) + x52
    <= 0)
@NLconstraint(m, e110, -sqrt((x8 - x10)^2 + (x25 - x27)^2 + (x42 - x44)^2) +
    x52 <= 0)
@NLconstraint(m, e111, -sqrt((x8 - x11)^2 + (x25 - x28)^2 + (x42 - x45)^2) +
    x52 <= 0)
@NLconstraint(m, e112, -sqrt((x8 - x12)^2 + (x25 - x29)^2 + (x42 - x46)^2) +
    x52 <= 0)
@NLconstraint(m, e113, -sqrt((x8 - x13)^2 + (x25 - x30)^2 + (x42 - x47)^2) +
    x52 <= 0)
@NLconstraint(m, e114, -sqrt((x8 - x14)^2 + (x25 - x31)^2 + (x42 - x48)^2) +
    x52 <= 0)
@NLconstraint(m, e115, -sqrt((x8 - x15)^2 + (x25 - x32)^2 + (x42 - x49)^2) +
    x52 <= 0)
@NLconstraint(m, e116, -sqrt((x8 - x16)^2 + (x25 - x33)^2 + (x42 - x50)^2) +
    x52 <= 0)
@NLconstraint(m, e117, -sqrt((x8 - x17)^2 + (x25 - x34)^2 + (x42 - x51)^2) +
    x52 <= 0)
@NLconstraint(m, e118, -sqrt((x9 - x10)^2 + (x26 - x27)^2 + (x43 - x44)^2) +
    x52 <= 0)
@NLconstraint(m, e119, -sqrt((x9 - x11)^2 + (x26 - x28)^2 + (x43 - x45)^2) +
    x52 <= 0)
@NLconstraint(m, e120, -sqrt((x9 - x12)^2 + (x26 - x29)^2 + (x43 - x46)^2) +
    x52 <= 0)
@NLconstraint(m, e121, -sqrt((x9 - x13)^2 + (x26 - x30)^2 + (x43 - x47)^2) +
    x52 <= 0)
@NLconstraint(m, e122, -sqrt((x9 - x14)^2 + (x26 - x31)^2 + (x43 - x48)^2) +
    x52 <= 0)
@NLconstraint(m, e123, -sqrt((x9 - x15)^2 + (x26 - x32)^2 + (x43 - x49)^2) +
    x52 <= 0)
@NLconstraint(m, e124, -sqrt((x9 - x16)^2 + (x26 - x33)^2 + (x43 - x50)^2) +
    x52 <= 0)
@NLconstraint(m, e125, -sqrt((x9 - x17)^2 + (x26 - x34)^2 + (x43 - x51)^2) +
    x52 <= 0)
@NLconstraint(m, e126, -sqrt((x10 - x11)^2 + (x27 - x28)^2 + (x44 - x45)^2) +
    x52 <= 0)
@NLconstraint(m, e127, -sqrt((x10 - x12)^2 + (x27 - x29)^2 + (x44 - x46)^2) +
    x52 <= 0)
@NLconstraint(m, e128, -sqrt((x10 - x13)^2 + (x27 - x30)^2 + (x44 - x47)^2) +
    x52 <= 0)
@NLconstraint(m, e129, -sqrt((x10 - x14)^2 + (x27 - x31)^2 + (x44 - x48)^2) +
    x52 <= 0)
@NLconstraint(m, e130, -sqrt((x10 - x15)^2 + (x27 - x32)^2 + (x44 - x49)^2) +
    x52 <= 0)
@NLconstraint(m, e131, -sqrt((x10 - x16)^2 + (x27 - x33)^2 + (x44 - x50)^2) +
    x52 <= 0)
@NLconstraint(m, e132, -sqrt((x10 - x17)^2 + (x27 - x34)^2 + (x44 - x51)^2) +
    x52 <= 0)
@NLconstraint(m, e133, -sqrt((x11 - x12)^2 + (x28 - x29)^2 + (x45 - x46)^2) +
    x52 <= 0)
@NLconstraint(m, e134, -sqrt((x11 - x13)^2 + (x28 - x30)^2 + (x45 - x47)^2) +
    x52 <= 0)
@NLconstraint(m, e135, -sqrt((x11 - x14)^2 + (x28 - x31)^2 + (x45 - x48)^2) +
    x52 <= 0)
@NLconstraint(m, e136, -sqrt((x11 - x15)^2 + (x28 - x32)^2 + (x45 - x49)^2) +
    x52 <= 0)
@NLconstraint(m, e137, -sqrt((x11 - x16)^2 + (x28 - x33)^2 + (x45 - x50)^2) +
    x52 <= 0)
@NLconstraint(m, e138, -sqrt((x11 - x17)^2 + (x28 - x34)^2 + (x45 - x51)^2) +
    x52 <= 0)
@NLconstraint(m, e139, -sqrt((x12 - x13)^2 + (x29 - x30)^2 + (x46 - x47)^2) +
    x52 <= 0)
@NLconstraint(m, e140, -sqrt((x12 - x14)^2 + (x29 - x31)^2 + (x46 - x48)^2) +
    x52 <= 0)
@NLconstraint(m, e141, -sqrt((x12 - x15)^2 + (x29 - x32)^2 + (x46 - x49)^2) +
    x52 <= 0)
@NLconstraint(m, e142, -sqrt((x12 - x16)^2 + (x29 - x33)^2 + (x46 - x50)^2) +
    x52 <= 0)
@NLconstraint(m, e143, -sqrt((x12 - x17)^2 + (x29 - x34)^2 + (x46 - x51)^2) +
    x52 <= 0)
@NLconstraint(m, e144, -sqrt((x13 - x14)^2 + (x30 - x31)^2 + (x47 - x48)^2) +
    x52 <= 0)
@NLconstraint(m, e145, -sqrt((x13 - x15)^2 + (x30 - x32)^2 + (x47 - x49)^2) +
    x52 <= 0)
@NLconstraint(m, e146, -sqrt((x13 - x16)^2 + (x30 - x33)^2 + (x47 - x50)^2) +
    x52 <= 0)
@NLconstraint(m, e147, -sqrt((x13 - x17)^2 + (x30 - x34)^2 + (x47 - x51)^2) +
    x52 <= 0)
@NLconstraint(m, e148, -sqrt((x14 - x15)^2 + (x31 - x32)^2 + (x48 - x49)^2) +
    x52 <= 0)
@NLconstraint(m, e149, -sqrt((x14 - x16)^2 + (x31 - x33)^2 + (x48 - x50)^2) +
    x52 <= 0)
@NLconstraint(m, e150, -sqrt((x14 - x17)^2 + (x31 - x34)^2 + (x48 - x51)^2) +
    x52 <= 0)
@NLconstraint(m, e151, -sqrt((x15 - x16)^2 + (x32 - x33)^2 + (x49 - x50)^2) +
    x52 <= 0)
@NLconstraint(m, e152, -sqrt((x15 - x17)^2 + (x32 - x34)^2 + (x49 - x51)^2) +
    x52 <= 0)
@NLconstraint(m, e153, -sqrt((x16 - x17)^2 + (x33 - x34)^2 + (x50 - x51)^2) +
    x52 <= 0)
