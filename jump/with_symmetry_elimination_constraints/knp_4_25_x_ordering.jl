# NLP written by GAMS Convert at 03/17/24 14:47:55
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       349       25      300       24        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#       101      101        0        0        0        0        0        0
# FX      4
#
# Nonzero counts
#     Total    const       NL
#      2848      348     2500
#
# Reformulation has removed 1 variable and 1 equation

using JuMP
using MathOptInterface
const MOI = MathOptInterface

model = m = Model()

@variable(m, -2 <= x1 <= -2, start=-2)
@variable(m, 0 <= x2 <= 0, start=0)
@variable(m, 0 <= x3 <= 0, start=0)
@variable(m, 0 <= x4 <= 0, start=0)
@variable(m, -2 <= x5 <= 2, start=0)
@variable(m, -2 <= x6 <= 2, start=0)
@variable(m, -2 <= x7 <= 2, start=0)
@variable(m, -2 <= x8 <= 2, start=0)
@variable(m, -2 <= x9 <= 2, start=0)
@variable(m, -2 <= x10 <= 2, start=0)
@variable(m, -2 <= x11 <= 2, start=0)
@variable(m, -2 <= x12 <= 2, start=0)
@variable(m, -2 <= x13 <= 2, start=0)
@variable(m, -2 <= x14 <= 2, start=0)
@variable(m, -2 <= x15 <= 2, start=0)
@variable(m, -2 <= x16 <= 2, start=0)
@variable(m, -2 <= x17 <= 2, start=0)
@variable(m, -2 <= x18 <= 2, start=0)
@variable(m, -2 <= x19 <= 2, start=0)
@variable(m, -2 <= x20 <= 2, start=0)
@variable(m, -2 <= x21 <= 2, start=0)
@variable(m, -2 <= x22 <= 2, start=0)
@variable(m, -2 <= x23 <= 2, start=0)
@variable(m, -2 <= x24 <= 2, start=0)
@variable(m, -2 <= x25 <= 2, start=0)
@variable(m, -2 <= x26 <= 2, start=0)
@variable(m, -2 <= x27 <= 2, start=0)
@variable(m, -2 <= x28 <= 2, start=0)
@variable(m, -2 <= x29 <= 2, start=0)
@variable(m, -2 <= x30 <= 2, start=0)
@variable(m, -2 <= x31 <= 2, start=0)
@variable(m, -2 <= x32 <= 2, start=0)
@variable(m, -2 <= x33 <= 2, start=0)
@variable(m, -2 <= x34 <= 2, start=0)
@variable(m, -2 <= x35 <= 2, start=0)
@variable(m, -2 <= x36 <= 2, start=0)
@variable(m, -2 <= x37 <= 2, start=0)
@variable(m, -2 <= x38 <= 2, start=0)
@variable(m, -2 <= x39 <= 2, start=0)
@variable(m, -2 <= x40 <= 2, start=0)
@variable(m, -2 <= x41 <= 2, start=0)
@variable(m, -2 <= x42 <= 2, start=0)
@variable(m, -2 <= x43 <= 2, start=0)
@variable(m, -2 <= x44 <= 2, start=0)
@variable(m, -2 <= x45 <= 2, start=0)
@variable(m, -2 <= x46 <= 2, start=0)
@variable(m, -2 <= x47 <= 2, start=0)
@variable(m, -2 <= x48 <= 2, start=0)
@variable(m, -2 <= x49 <= 2, start=0)
@variable(m, -2 <= x50 <= 2, start=0)
@variable(m, -2 <= x51 <= 2, start=0)
@variable(m, -2 <= x52 <= 2, start=0)
@variable(m, -2 <= x53 <= 2, start=0)
@variable(m, -2 <= x54 <= 2, start=0)
@variable(m, -2 <= x55 <= 2, start=0)
@variable(m, -2 <= x56 <= 2, start=0)
@variable(m, -2 <= x57 <= 2, start=0)
@variable(m, -2 <= x58 <= 2, start=0)
@variable(m, -2 <= x59 <= 2, start=0)
@variable(m, -2 <= x60 <= 2, start=0)
@variable(m, -2 <= x61 <= 2, start=0)
@variable(m, -2 <= x62 <= 2, start=0)
@variable(m, -2 <= x63 <= 2, start=0)
@variable(m, -2 <= x64 <= 2, start=0)
@variable(m, -2 <= x65 <= 2, start=0)
@variable(m, -2 <= x66 <= 2, start=0)
@variable(m, -2 <= x67 <= 2, start=0)
@variable(m, -2 <= x68 <= 2, start=0)
@variable(m, -2 <= x69 <= 2, start=0)
@variable(m, -2 <= x70 <= 2, start=0)
@variable(m, -2 <= x71 <= 2, start=0)
@variable(m, -2 <= x72 <= 2, start=0)
@variable(m, -2 <= x73 <= 2, start=0)
@variable(m, -2 <= x74 <= 2, start=0)
@variable(m, -2 <= x75 <= 2, start=0)
@variable(m, -2 <= x76 <= 2, start=0)
@variable(m, -2 <= x77 <= 2, start=0)
@variable(m, -2 <= x78 <= 2, start=0)
@variable(m, -2 <= x79 <= 2, start=0)
@variable(m, -2 <= x80 <= 2, start=0)
@variable(m, -2 <= x81 <= 2, start=0)
@variable(m, -2 <= x82 <= 2, start=0)
@variable(m, -2 <= x83 <= 2, start=0)
@variable(m, -2 <= x84 <= 2, start=0)
@variable(m, -2 <= x85 <= 2, start=0)
@variable(m, -2 <= x86 <= 2, start=0)
@variable(m, -2 <= x87 <= 2, start=0)
@variable(m, -2 <= x88 <= 2, start=0)
@variable(m, -2 <= x89 <= 2, start=0)
@variable(m, -2 <= x90 <= 2, start=0)
@variable(m, -2 <= x91 <= 2, start=0)
@variable(m, -2 <= x92 <= 2, start=0)
@variable(m, -2 <= x93 <= 2, start=0)
@variable(m, -2 <= x94 <= 2, start=0)
@variable(m, -2 <= x95 <= 2, start=0)
@variable(m, -2 <= x96 <= 2, start=0)
@variable(m, -2 <= x97 <= 2, start=0)
@variable(m, -2 <= x98 <= 2, start=0)
@variable(m, -2 <= x99 <= 2, start=0)
@variable(m, -2 <= x100 <= 2, start=0)
@variable(m, x101 <= 4, start=0)

@objective(m, Max, x101)

@NLconstraint(m, e1, (x1 - x5)^2 + (x2 - x6)^2 + (x3 - x7)^2 + (x4 - x8)^2 -
    x101 >= 0)
@NLconstraint(m, e2, (x1 - x9)^2 + (x2 - x10)^2 + (x3 - x11)^2 + (x4 - x12)^2
    - x101 >= 0)
@NLconstraint(m, e3, (x1 - x13)^2 + (x2 - x14)^2 + (x3 - x15)^2 + (x4 - x16)^2
    - x101 >= 0)
@NLconstraint(m, e4, (x1 - x17)^2 + (x2 - x18)^2 + (x3 - x19)^2 + (x4 - x20)^2
    - x101 >= 0)
@NLconstraint(m, e5, (x1 - x21)^2 + (x2 - x22)^2 + (x3 - x23)^2 + (x4 - x24)^2
    - x101 >= 0)
@NLconstraint(m, e6, (x1 - x25)^2 + (x2 - x26)^2 + (x3 - x27)^2 + (x4 - x28)^2
    - x101 >= 0)
@NLconstraint(m, e7, (x1 - x29)^2 + (x2 - x30)^2 + (x3 - x31)^2 + (x4 - x32)^2
    - x101 >= 0)
@NLconstraint(m, e8, (x1 - x33)^2 + (x2 - x34)^2 + (x3 - x35)^2 + (x4 - x36)^2
    - x101 >= 0)
@NLconstraint(m, e9, (x1 - x37)^2 + (x2 - x38)^2 + (x3 - x39)^2 + (x4 - x40)^2
    - x101 >= 0)
@NLconstraint(m, e10, (x1 - x41)^2 + (x2 - x42)^2 + (x3 - x43)^2 + (x4 - x44)^2
    - x101 >= 0)
@NLconstraint(m, e11, (x1 - x45)^2 + (x2 - x46)^2 + (x3 - x47)^2 + (x4 - x48)^2
    - x101 >= 0)
@NLconstraint(m, e12, (x1 - x49)^2 + (x2 - x50)^2 + (x3 - x51)^2 + (x4 - x52)^2
    - x101 >= 0)
@NLconstraint(m, e13, (x1 - x53)^2 + (x2 - x54)^2 + (x3 - x55)^2 + (x4 - x56)^2
    - x101 >= 0)
@NLconstraint(m, e14, (x1 - x57)^2 + (x2 - x58)^2 + (x3 - x59)^2 + (x4 - x60)^2
    - x101 >= 0)
@NLconstraint(m, e15, (x1 - x61)^2 + (x2 - x62)^2 + (x3 - x63)^2 + (x4 - x64)^2
    - x101 >= 0)
@NLconstraint(m, e16, (x1 - x65)^2 + (x2 - x66)^2 + (x3 - x67)^2 + (x4 - x68)^2
    - x101 >= 0)
@NLconstraint(m, e17, (x1 - x69)^2 + (x2 - x70)^2 + (x3 - x71)^2 + (x4 - x72)^2
    - x101 >= 0)
@NLconstraint(m, e18, (x1 - x73)^2 + (x2 - x74)^2 + (x3 - x75)^2 + (x4 - x76)^2
    - x101 >= 0)
@NLconstraint(m, e19, (x1 - x77)^2 + (x2 - x78)^2 + (x3 - x79)^2 + (x4 - x80)^2
    - x101 >= 0)
@NLconstraint(m, e20, (x1 - x81)^2 + (x2 - x82)^2 + (x3 - x83)^2 + (x4 - x84)^2
    - x101 >= 0)
@NLconstraint(m, e21, (x1 - x85)^2 + (x2 - x86)^2 + (x3 - x87)^2 + (x4 - x88)^2
    - x101 >= 0)
@NLconstraint(m, e22, (x1 - x89)^2 + (x2 - x90)^2 + (x3 - x91)^2 + (x4 - x92)^2
    - x101 >= 0)
@NLconstraint(m, e23, (x1 - x93)^2 + (x2 - x94)^2 + (x3 - x95)^2 + (x4 - x96)^2
    - x101 >= 0)
@NLconstraint(m, e24, (x1 - x97)^2 + (x2 - x98)^2 + (x3 - x99)^2 + (x4 - x100)^
    2 - x101 >= 0)
@NLconstraint(m, e25, (x5 - x9)^2 + (x6 - x10)^2 + (x7 - x11)^2 + (x8 - x12)^2
    - x101 >= 0)
@NLconstraint(m, e26, (x5 - x13)^2 + (x6 - x14)^2 + (x7 - x15)^2 + (x8 - x16)^2
    - x101 >= 0)
@NLconstraint(m, e27, (x5 - x17)^2 + (x6 - x18)^2 + (x7 - x19)^2 + (x8 - x20)^2
    - x101 >= 0)
@NLconstraint(m, e28, (x5 - x21)^2 + (x6 - x22)^2 + (x7 - x23)^2 + (x8 - x24)^2
    - x101 >= 0)
@NLconstraint(m, e29, (x5 - x25)^2 + (x6 - x26)^2 + (x7 - x27)^2 + (x8 - x28)^2
    - x101 >= 0)
@NLconstraint(m, e30, (x5 - x29)^2 + (x6 - x30)^2 + (x7 - x31)^2 + (x8 - x32)^2
    - x101 >= 0)
@NLconstraint(m, e31, (x5 - x33)^2 + (x6 - x34)^2 + (x7 - x35)^2 + (x8 - x36)^2
    - x101 >= 0)
@NLconstraint(m, e32, (x5 - x37)^2 + (x6 - x38)^2 + (x7 - x39)^2 + (x8 - x40)^2
    - x101 >= 0)
@NLconstraint(m, e33, (x5 - x41)^2 + (x6 - x42)^2 + (x7 - x43)^2 + (x8 - x44)^2
    - x101 >= 0)
@NLconstraint(m, e34, (x5 - x45)^2 + (x6 - x46)^2 + (x7 - x47)^2 + (x8 - x48)^2
    - x101 >= 0)
@NLconstraint(m, e35, (x5 - x49)^2 + (x6 - x50)^2 + (x7 - x51)^2 + (x8 - x52)^2
    - x101 >= 0)
@NLconstraint(m, e36, (x5 - x53)^2 + (x6 - x54)^2 + (x7 - x55)^2 + (x8 - x56)^2
    - x101 >= 0)
@NLconstraint(m, e37, (x5 - x57)^2 + (x6 - x58)^2 + (x7 - x59)^2 + (x8 - x60)^2
    - x101 >= 0)
@NLconstraint(m, e38, (x5 - x61)^2 + (x6 - x62)^2 + (x7 - x63)^2 + (x8 - x64)^2
    - x101 >= 0)
@NLconstraint(m, e39, (x5 - x65)^2 + (x6 - x66)^2 + (x7 - x67)^2 + (x8 - x68)^2
    - x101 >= 0)
@NLconstraint(m, e40, (x5 - x69)^2 + (x6 - x70)^2 + (x7 - x71)^2 + (x8 - x72)^2
    - x101 >= 0)
@NLconstraint(m, e41, (x5 - x73)^2 + (x6 - x74)^2 + (x7 - x75)^2 + (x8 - x76)^2
    - x101 >= 0)
@NLconstraint(m, e42, (x5 - x77)^2 + (x6 - x78)^2 + (x7 - x79)^2 + (x8 - x80)^2
    - x101 >= 0)
@NLconstraint(m, e43, (x5 - x81)^2 + (x6 - x82)^2 + (x7 - x83)^2 + (x8 - x84)^2
    - x101 >= 0)
@NLconstraint(m, e44, (x5 - x85)^2 + (x6 - x86)^2 + (x7 - x87)^2 + (x8 - x88)^2
    - x101 >= 0)
@NLconstraint(m, e45, (x5 - x89)^2 + (x6 - x90)^2 + (x7 - x91)^2 + (x8 - x92)^2
    - x101 >= 0)
@NLconstraint(m, e46, (x5 - x93)^2 + (x6 - x94)^2 + (x7 - x95)^2 + (x8 - x96)^2
    - x101 >= 0)
@NLconstraint(m, e47, (x5 - x97)^2 + (x6 - x98)^2 + (x7 - x99)^2 + (x8 - x100)^
    2 - x101 >= 0)
@NLconstraint(m, e48, (x9 - x13)^2 + (x10 - x14)^2 + (x11 - x15)^2 + (x12 - x16)
    ^2 - x101 >= 0)
@NLconstraint(m, e49, (x9 - x17)^2 + (x10 - x18)^2 + (x11 - x19)^2 + (x12 - x20)
    ^2 - x101 >= 0)
@NLconstraint(m, e50, (x9 - x21)^2 + (x10 - x22)^2 + (x11 - x23)^2 + (x12 - x24)
    ^2 - x101 >= 0)
@NLconstraint(m, e51, (x9 - x25)^2 + (x10 - x26)^2 + (x11 - x27)^2 + (x12 - x28)
    ^2 - x101 >= 0)
@NLconstraint(m, e52, (x9 - x29)^2 + (x10 - x30)^2 + (x11 - x31)^2 + (x12 - x32)
    ^2 - x101 >= 0)
@NLconstraint(m, e53, (x9 - x33)^2 + (x10 - x34)^2 + (x11 - x35)^2 + (x12 - x36)
    ^2 - x101 >= 0)
@NLconstraint(m, e54, (x9 - x37)^2 + (x10 - x38)^2 + (x11 - x39)^2 + (x12 - x40)
    ^2 - x101 >= 0)
@NLconstraint(m, e55, (x9 - x41)^2 + (x10 - x42)^2 + (x11 - x43)^2 + (x12 - x44)
    ^2 - x101 >= 0)
@NLconstraint(m, e56, (x9 - x45)^2 + (x10 - x46)^2 + (x11 - x47)^2 + (x12 - x48)
    ^2 - x101 >= 0)
@NLconstraint(m, e57, (x9 - x49)^2 + (x10 - x50)^2 + (x11 - x51)^2 + (x12 - x52)
    ^2 - x101 >= 0)
@NLconstraint(m, e58, (x9 - x53)^2 + (x10 - x54)^2 + (x11 - x55)^2 + (x12 - x56)
    ^2 - x101 >= 0)
@NLconstraint(m, e59, (x9 - x57)^2 + (x10 - x58)^2 + (x11 - x59)^2 + (x12 - x60)
    ^2 - x101 >= 0)
@NLconstraint(m, e60, (x9 - x61)^2 + (x10 - x62)^2 + (x11 - x63)^2 + (x12 - x64)
    ^2 - x101 >= 0)
@NLconstraint(m, e61, (x9 - x65)^2 + (x10 - x66)^2 + (x11 - x67)^2 + (x12 - x68)
    ^2 - x101 >= 0)
@NLconstraint(m, e62, (x9 - x69)^2 + (x10 - x70)^2 + (x11 - x71)^2 + (x12 - x72)
    ^2 - x101 >= 0)
@NLconstraint(m, e63, (x9 - x73)^2 + (x10 - x74)^2 + (x11 - x75)^2 + (x12 - x76)
    ^2 - x101 >= 0)
@NLconstraint(m, e64, (x9 - x77)^2 + (x10 - x78)^2 + (x11 - x79)^2 + (x12 - x80)
    ^2 - x101 >= 0)
@NLconstraint(m, e65, (x9 - x81)^2 + (x10 - x82)^2 + (x11 - x83)^2 + (x12 - x84)
    ^2 - x101 >= 0)
@NLconstraint(m, e66, (x9 - x85)^2 + (x10 - x86)^2 + (x11 - x87)^2 + (x12 - x88)
    ^2 - x101 >= 0)
@NLconstraint(m, e67, (x9 - x89)^2 + (x10 - x90)^2 + (x11 - x91)^2 + (x12 - x92)
    ^2 - x101 >= 0)
@NLconstraint(m, e68, (x9 - x93)^2 + (x10 - x94)^2 + (x11 - x95)^2 + (x12 - x96)
    ^2 - x101 >= 0)
@NLconstraint(m, e69, (x9 - x97)^2 + (x10 - x98)^2 + (x11 - x99)^2 + (x12 -
    x100)^2 - x101 >= 0)
@NLconstraint(m, e70, (x13 - x17)^2 + (x14 - x18)^2 + (x15 - x19)^2 + (x16 -
    x20)^2 - x101 >= 0)
@NLconstraint(m, e71, (x13 - x21)^2 + (x14 - x22)^2 + (x15 - x23)^2 + (x16 -
    x24)^2 - x101 >= 0)
@NLconstraint(m, e72, (x13 - x25)^2 + (x14 - x26)^2 + (x15 - x27)^2 + (x16 -
    x28)^2 - x101 >= 0)
@NLconstraint(m, e73, (x13 - x29)^2 + (x14 - x30)^2 + (x15 - x31)^2 + (x16 -
    x32)^2 - x101 >= 0)
@NLconstraint(m, e74, (x13 - x33)^2 + (x14 - x34)^2 + (x15 - x35)^2 + (x16 -
    x36)^2 - x101 >= 0)
@NLconstraint(m, e75, (x13 - x37)^2 + (x14 - x38)^2 + (x15 - x39)^2 + (x16 -
    x40)^2 - x101 >= 0)
@NLconstraint(m, e76, (x13 - x41)^2 + (x14 - x42)^2 + (x15 - x43)^2 + (x16 -
    x44)^2 - x101 >= 0)
@NLconstraint(m, e77, (x13 - x45)^2 + (x14 - x46)^2 + (x15 - x47)^2 + (x16 -
    x48)^2 - x101 >= 0)
@NLconstraint(m, e78, (x13 - x49)^2 + (x14 - x50)^2 + (x15 - x51)^2 + (x16 -
    x52)^2 - x101 >= 0)
@NLconstraint(m, e79, (x13 - x53)^2 + (x14 - x54)^2 + (x15 - x55)^2 + (x16 -
    x56)^2 - x101 >= 0)
@NLconstraint(m, e80, (x13 - x57)^2 + (x14 - x58)^2 + (x15 - x59)^2 + (x16 -
    x60)^2 - x101 >= 0)
@NLconstraint(m, e81, (x13 - x61)^2 + (x14 - x62)^2 + (x15 - x63)^2 + (x16 -
    x64)^2 - x101 >= 0)
@NLconstraint(m, e82, (x13 - x65)^2 + (x14 - x66)^2 + (x15 - x67)^2 + (x16 -
    x68)^2 - x101 >= 0)
@NLconstraint(m, e83, (x13 - x69)^2 + (x14 - x70)^2 + (x15 - x71)^2 + (x16 -
    x72)^2 - x101 >= 0)
@NLconstraint(m, e84, (x13 - x73)^2 + (x14 - x74)^2 + (x15 - x75)^2 + (x16 -
    x76)^2 - x101 >= 0)
@NLconstraint(m, e85, (x13 - x77)^2 + (x14 - x78)^2 + (x15 - x79)^2 + (x16 -
    x80)^2 - x101 >= 0)
@NLconstraint(m, e86, (x13 - x81)^2 + (x14 - x82)^2 + (x15 - x83)^2 + (x16 -
    x84)^2 - x101 >= 0)
@NLconstraint(m, e87, (x13 - x85)^2 + (x14 - x86)^2 + (x15 - x87)^2 + (x16 -
    x88)^2 - x101 >= 0)
@NLconstraint(m, e88, (x13 - x89)^2 + (x14 - x90)^2 + (x15 - x91)^2 + (x16 -
    x92)^2 - x101 >= 0)
@NLconstraint(m, e89, (x13 - x93)^2 + (x14 - x94)^2 + (x15 - x95)^2 + (x16 -
    x96)^2 - x101 >= 0)
@NLconstraint(m, e90, (x13 - x97)^2 + (x14 - x98)^2 + (x15 - x99)^2 + (x16 -
    x100)^2 - x101 >= 0)
@NLconstraint(m, e91, (x17 - x21)^2 + (x18 - x22)^2 + (x19 - x23)^2 + (x20 -
    x24)^2 - x101 >= 0)
@NLconstraint(m, e92, (x17 - x25)^2 + (x18 - x26)^2 + (x19 - x27)^2 + (x20 -
    x28)^2 - x101 >= 0)
@NLconstraint(m, e93, (x17 - x29)^2 + (x18 - x30)^2 + (x19 - x31)^2 + (x20 -
    x32)^2 - x101 >= 0)
@NLconstraint(m, e94, (x17 - x33)^2 + (x18 - x34)^2 + (x19 - x35)^2 + (x20 -
    x36)^2 - x101 >= 0)
@NLconstraint(m, e95, (x17 - x37)^2 + (x18 - x38)^2 + (x19 - x39)^2 + (x20 -
    x40)^2 - x101 >= 0)
@NLconstraint(m, e96, (x17 - x41)^2 + (x18 - x42)^2 + (x19 - x43)^2 + (x20 -
    x44)^2 - x101 >= 0)
@NLconstraint(m, e97, (x17 - x45)^2 + (x18 - x46)^2 + (x19 - x47)^2 + (x20 -
    x48)^2 - x101 >= 0)
@NLconstraint(m, e98, (x17 - x49)^2 + (x18 - x50)^2 + (x19 - x51)^2 + (x20 -
    x52)^2 - x101 >= 0)
@NLconstraint(m, e99, (x17 - x53)^2 + (x18 - x54)^2 + (x19 - x55)^2 + (x20 -
    x56)^2 - x101 >= 0)
@NLconstraint(m, e100, (x17 - x57)^2 + (x18 - x58)^2 + (x19 - x59)^2 + (x20 -
    x60)^2 - x101 >= 0)
@NLconstraint(m, e101, (x17 - x61)^2 + (x18 - x62)^2 + (x19 - x63)^2 + (x20 -
    x64)^2 - x101 >= 0)
@NLconstraint(m, e102, (x17 - x65)^2 + (x18 - x66)^2 + (x19 - x67)^2 + (x20 -
    x68)^2 - x101 >= 0)
@NLconstraint(m, e103, (x17 - x69)^2 + (x18 - x70)^2 + (x19 - x71)^2 + (x20 -
    x72)^2 - x101 >= 0)
@NLconstraint(m, e104, (x17 - x73)^2 + (x18 - x74)^2 + (x19 - x75)^2 + (x20 -
    x76)^2 - x101 >= 0)
@NLconstraint(m, e105, (x17 - x77)^2 + (x18 - x78)^2 + (x19 - x79)^2 + (x20 -
    x80)^2 - x101 >= 0)
@NLconstraint(m, e106, (x17 - x81)^2 + (x18 - x82)^2 + (x19 - x83)^2 + (x20 -
    x84)^2 - x101 >= 0)
@NLconstraint(m, e107, (x17 - x85)^2 + (x18 - x86)^2 + (x19 - x87)^2 + (x20 -
    x88)^2 - x101 >= 0)
@NLconstraint(m, e108, (x17 - x89)^2 + (x18 - x90)^2 + (x19 - x91)^2 + (x20 -
    x92)^2 - x101 >= 0)
@NLconstraint(m, e109, (x17 - x93)^2 + (x18 - x94)^2 + (x19 - x95)^2 + (x20 -
    x96)^2 - x101 >= 0)
@NLconstraint(m, e110, (x17 - x97)^2 + (x18 - x98)^2 + (x19 - x99)^2 + (x20 -
    x100)^2 - x101 >= 0)
@NLconstraint(m, e111, (x21 - x25)^2 + (x22 - x26)^2 + (x23 - x27)^2 + (x24 -
    x28)^2 - x101 >= 0)
@NLconstraint(m, e112, (x21 - x29)^2 + (x22 - x30)^2 + (x23 - x31)^2 + (x24 -
    x32)^2 - x101 >= 0)
@NLconstraint(m, e113, (x21 - x33)^2 + (x22 - x34)^2 + (x23 - x35)^2 + (x24 -
    x36)^2 - x101 >= 0)
@NLconstraint(m, e114, (x21 - x37)^2 + (x22 - x38)^2 + (x23 - x39)^2 + (x24 -
    x40)^2 - x101 >= 0)
@NLconstraint(m, e115, (x21 - x41)^2 + (x22 - x42)^2 + (x23 - x43)^2 + (x24 -
    x44)^2 - x101 >= 0)
@NLconstraint(m, e116, (x21 - x45)^2 + (x22 - x46)^2 + (x23 - x47)^2 + (x24 -
    x48)^2 - x101 >= 0)
@NLconstraint(m, e117, (x21 - x49)^2 + (x22 - x50)^2 + (x23 - x51)^2 + (x24 -
    x52)^2 - x101 >= 0)
@NLconstraint(m, e118, (x21 - x53)^2 + (x22 - x54)^2 + (x23 - x55)^2 + (x24 -
    x56)^2 - x101 >= 0)
@NLconstraint(m, e119, (x21 - x57)^2 + (x22 - x58)^2 + (x23 - x59)^2 + (x24 -
    x60)^2 - x101 >= 0)
@NLconstraint(m, e120, (x21 - x61)^2 + (x22 - x62)^2 + (x23 - x63)^2 + (x24 -
    x64)^2 - x101 >= 0)
@NLconstraint(m, e121, (x21 - x65)^2 + (x22 - x66)^2 + (x23 - x67)^2 + (x24 -
    x68)^2 - x101 >= 0)
@NLconstraint(m, e122, (x21 - x69)^2 + (x22 - x70)^2 + (x23 - x71)^2 + (x24 -
    x72)^2 - x101 >= 0)
@NLconstraint(m, e123, (x21 - x73)^2 + (x22 - x74)^2 + (x23 - x75)^2 + (x24 -
    x76)^2 - x101 >= 0)
@NLconstraint(m, e124, (x21 - x77)^2 + (x22 - x78)^2 + (x23 - x79)^2 + (x24 -
    x80)^2 - x101 >= 0)
@NLconstraint(m, e125, (x21 - x81)^2 + (x22 - x82)^2 + (x23 - x83)^2 + (x24 -
    x84)^2 - x101 >= 0)
@NLconstraint(m, e126, (x21 - x85)^2 + (x22 - x86)^2 + (x23 - x87)^2 + (x24 -
    x88)^2 - x101 >= 0)
@NLconstraint(m, e127, (x21 - x89)^2 + (x22 - x90)^2 + (x23 - x91)^2 + (x24 -
    x92)^2 - x101 >= 0)
@NLconstraint(m, e128, (x21 - x93)^2 + (x22 - x94)^2 + (x23 - x95)^2 + (x24 -
    x96)^2 - x101 >= 0)
@NLconstraint(m, e129, (x21 - x97)^2 + (x22 - x98)^2 + (x23 - x99)^2 + (x24 -
    x100)^2 - x101 >= 0)
@NLconstraint(m, e130, (x25 - x29)^2 + (x26 - x30)^2 + (x27 - x31)^2 + (x28 -
    x32)^2 - x101 >= 0)
@NLconstraint(m, e131, (x25 - x33)^2 + (x26 - x34)^2 + (x27 - x35)^2 + (x28 -
    x36)^2 - x101 >= 0)
@NLconstraint(m, e132, (x25 - x37)^2 + (x26 - x38)^2 + (x27 - x39)^2 + (x28 -
    x40)^2 - x101 >= 0)
@NLconstraint(m, e133, (x25 - x41)^2 + (x26 - x42)^2 + (x27 - x43)^2 + (x28 -
    x44)^2 - x101 >= 0)
@NLconstraint(m, e134, (x25 - x45)^2 + (x26 - x46)^2 + (x27 - x47)^2 + (x28 -
    x48)^2 - x101 >= 0)
@NLconstraint(m, e135, (x25 - x49)^2 + (x26 - x50)^2 + (x27 - x51)^2 + (x28 -
    x52)^2 - x101 >= 0)
@NLconstraint(m, e136, (x25 - x53)^2 + (x26 - x54)^2 + (x27 - x55)^2 + (x28 -
    x56)^2 - x101 >= 0)
@NLconstraint(m, e137, (x25 - x57)^2 + (x26 - x58)^2 + (x27 - x59)^2 + (x28 -
    x60)^2 - x101 >= 0)
@NLconstraint(m, e138, (x25 - x61)^2 + (x26 - x62)^2 + (x27 - x63)^2 + (x28 -
    x64)^2 - x101 >= 0)
@NLconstraint(m, e139, (x25 - x65)^2 + (x26 - x66)^2 + (x27 - x67)^2 + (x28 -
    x68)^2 - x101 >= 0)
@NLconstraint(m, e140, (x25 - x69)^2 + (x26 - x70)^2 + (x27 - x71)^2 + (x28 -
    x72)^2 - x101 >= 0)
@NLconstraint(m, e141, (x25 - x73)^2 + (x26 - x74)^2 + (x27 - x75)^2 + (x28 -
    x76)^2 - x101 >= 0)
@NLconstraint(m, e142, (x25 - x77)^2 + (x26 - x78)^2 + (x27 - x79)^2 + (x28 -
    x80)^2 - x101 >= 0)
@NLconstraint(m, e143, (x25 - x81)^2 + (x26 - x82)^2 + (x27 - x83)^2 + (x28 -
    x84)^2 - x101 >= 0)
@NLconstraint(m, e144, (x25 - x85)^2 + (x26 - x86)^2 + (x27 - x87)^2 + (x28 -
    x88)^2 - x101 >= 0)
@NLconstraint(m, e145, (x25 - x89)^2 + (x26 - x90)^2 + (x27 - x91)^2 + (x28 -
    x92)^2 - x101 >= 0)
@NLconstraint(m, e146, (x25 - x93)^2 + (x26 - x94)^2 + (x27 - x95)^2 + (x28 -
    x96)^2 - x101 >= 0)
@NLconstraint(m, e147, (x25 - x97)^2 + (x26 - x98)^2 + (x27 - x99)^2 + (x28 -
    x100)^2 - x101 >= 0)
@NLconstraint(m, e148, (x29 - x33)^2 + (x30 - x34)^2 + (x31 - x35)^2 + (x32 -
    x36)^2 - x101 >= 0)
@NLconstraint(m, e149, (x29 - x37)^2 + (x30 - x38)^2 + (x31 - x39)^2 + (x32 -
    x40)^2 - x101 >= 0)
@NLconstraint(m, e150, (x29 - x41)^2 + (x30 - x42)^2 + (x31 - x43)^2 + (x32 -
    x44)^2 - x101 >= 0)
@NLconstraint(m, e151, (x29 - x45)^2 + (x30 - x46)^2 + (x31 - x47)^2 + (x32 -
    x48)^2 - x101 >= 0)
@NLconstraint(m, e152, (x29 - x49)^2 + (x30 - x50)^2 + (x31 - x51)^2 + (x32 -
    x52)^2 - x101 >= 0)
@NLconstraint(m, e153, (x29 - x53)^2 + (x30 - x54)^2 + (x31 - x55)^2 + (x32 -
    x56)^2 - x101 >= 0)
@NLconstraint(m, e154, (x29 - x57)^2 + (x30 - x58)^2 + (x31 - x59)^2 + (x32 -
    x60)^2 - x101 >= 0)
@NLconstraint(m, e155, (x29 - x61)^2 + (x30 - x62)^2 + (x31 - x63)^2 + (x32 -
    x64)^2 - x101 >= 0)
@NLconstraint(m, e156, (x29 - x65)^2 + (x30 - x66)^2 + (x31 - x67)^2 + (x32 -
    x68)^2 - x101 >= 0)
@NLconstraint(m, e157, (x29 - x69)^2 + (x30 - x70)^2 + (x31 - x71)^2 + (x32 -
    x72)^2 - x101 >= 0)
@NLconstraint(m, e158, (x29 - x73)^2 + (x30 - x74)^2 + (x31 - x75)^2 + (x32 -
    x76)^2 - x101 >= 0)
@NLconstraint(m, e159, (x29 - x77)^2 + (x30 - x78)^2 + (x31 - x79)^2 + (x32 -
    x80)^2 - x101 >= 0)
@NLconstraint(m, e160, (x29 - x81)^2 + (x30 - x82)^2 + (x31 - x83)^2 + (x32 -
    x84)^2 - x101 >= 0)
@NLconstraint(m, e161, (x29 - x85)^2 + (x30 - x86)^2 + (x31 - x87)^2 + (x32 -
    x88)^2 - x101 >= 0)
@NLconstraint(m, e162, (x29 - x89)^2 + (x30 - x90)^2 + (x31 - x91)^2 + (x32 -
    x92)^2 - x101 >= 0)
@NLconstraint(m, e163, (x29 - x93)^2 + (x30 - x94)^2 + (x31 - x95)^2 + (x32 -
    x96)^2 - x101 >= 0)
@NLconstraint(m, e164, (x29 - x97)^2 + (x30 - x98)^2 + (x31 - x99)^2 + (x32 -
    x100)^2 - x101 >= 0)
@NLconstraint(m, e165, (x33 - x37)^2 + (x34 - x38)^2 + (x35 - x39)^2 + (x36 -
    x40)^2 - x101 >= 0)
@NLconstraint(m, e166, (x33 - x41)^2 + (x34 - x42)^2 + (x35 - x43)^2 + (x36 -
    x44)^2 - x101 >= 0)
@NLconstraint(m, e167, (x33 - x45)^2 + (x34 - x46)^2 + (x35 - x47)^2 + (x36 -
    x48)^2 - x101 >= 0)
@NLconstraint(m, e168, (x33 - x49)^2 + (x34 - x50)^2 + (x35 - x51)^2 + (x36 -
    x52)^2 - x101 >= 0)
@NLconstraint(m, e169, (x33 - x53)^2 + (x34 - x54)^2 + (x35 - x55)^2 + (x36 -
    x56)^2 - x101 >= 0)
@NLconstraint(m, e170, (x33 - x57)^2 + (x34 - x58)^2 + (x35 - x59)^2 + (x36 -
    x60)^2 - x101 >= 0)
@NLconstraint(m, e171, (x33 - x61)^2 + (x34 - x62)^2 + (x35 - x63)^2 + (x36 -
    x64)^2 - x101 >= 0)
@NLconstraint(m, e172, (x33 - x65)^2 + (x34 - x66)^2 + (x35 - x67)^2 + (x36 -
    x68)^2 - x101 >= 0)
@NLconstraint(m, e173, (x33 - x69)^2 + (x34 - x70)^2 + (x35 - x71)^2 + (x36 -
    x72)^2 - x101 >= 0)
@NLconstraint(m, e174, (x33 - x73)^2 + (x34 - x74)^2 + (x35 - x75)^2 + (x36 -
    x76)^2 - x101 >= 0)
@NLconstraint(m, e175, (x33 - x77)^2 + (x34 - x78)^2 + (x35 - x79)^2 + (x36 -
    x80)^2 - x101 >= 0)
@NLconstraint(m, e176, (x33 - x81)^2 + (x34 - x82)^2 + (x35 - x83)^2 + (x36 -
    x84)^2 - x101 >= 0)
@NLconstraint(m, e177, (x33 - x85)^2 + (x34 - x86)^2 + (x35 - x87)^2 + (x36 -
    x88)^2 - x101 >= 0)
@NLconstraint(m, e178, (x33 - x89)^2 + (x34 - x90)^2 + (x35 - x91)^2 + (x36 -
    x92)^2 - x101 >= 0)
@NLconstraint(m, e179, (x33 - x93)^2 + (x34 - x94)^2 + (x35 - x95)^2 + (x36 -
    x96)^2 - x101 >= 0)
@NLconstraint(m, e180, (x33 - x97)^2 + (x34 - x98)^2 + (x35 - x99)^2 + (x36 -
    x100)^2 - x101 >= 0)
@NLconstraint(m, e181, (x37 - x41)^2 + (x38 - x42)^2 + (x39 - x43)^2 + (x40 -
    x44)^2 - x101 >= 0)
@NLconstraint(m, e182, (x37 - x45)^2 + (x38 - x46)^2 + (x39 - x47)^2 + (x40 -
    x48)^2 - x101 >= 0)
@NLconstraint(m, e183, (x37 - x49)^2 + (x38 - x50)^2 + (x39 - x51)^2 + (x40 -
    x52)^2 - x101 >= 0)
@NLconstraint(m, e184, (x37 - x53)^2 + (x38 - x54)^2 + (x39 - x55)^2 + (x40 -
    x56)^2 - x101 >= 0)
@NLconstraint(m, e185, (x37 - x57)^2 + (x38 - x58)^2 + (x39 - x59)^2 + (x40 -
    x60)^2 - x101 >= 0)
@NLconstraint(m, e186, (x37 - x61)^2 + (x38 - x62)^2 + (x39 - x63)^2 + (x40 -
    x64)^2 - x101 >= 0)
@NLconstraint(m, e187, (x37 - x65)^2 + (x38 - x66)^2 + (x39 - x67)^2 + (x40 -
    x68)^2 - x101 >= 0)
@NLconstraint(m, e188, (x37 - x69)^2 + (x38 - x70)^2 + (x39 - x71)^2 + (x40 -
    x72)^2 - x101 >= 0)
@NLconstraint(m, e189, (x37 - x73)^2 + (x38 - x74)^2 + (x39 - x75)^2 + (x40 -
    x76)^2 - x101 >= 0)
@NLconstraint(m, e190, (x37 - x77)^2 + (x38 - x78)^2 + (x39 - x79)^2 + (x40 -
    x80)^2 - x101 >= 0)
@NLconstraint(m, e191, (x37 - x81)^2 + (x38 - x82)^2 + (x39 - x83)^2 + (x40 -
    x84)^2 - x101 >= 0)
@NLconstraint(m, e192, (x37 - x85)^2 + (x38 - x86)^2 + (x39 - x87)^2 + (x40 -
    x88)^2 - x101 >= 0)
@NLconstraint(m, e193, (x37 - x89)^2 + (x38 - x90)^2 + (x39 - x91)^2 + (x40 -
    x92)^2 - x101 >= 0)
@NLconstraint(m, e194, (x37 - x93)^2 + (x38 - x94)^2 + (x39 - x95)^2 + (x40 -
    x96)^2 - x101 >= 0)
@NLconstraint(m, e195, (x37 - x97)^2 + (x38 - x98)^2 + (x39 - x99)^2 + (x40 -
    x100)^2 - x101 >= 0)
@NLconstraint(m, e196, (x41 - x45)^2 + (x42 - x46)^2 + (x43 - x47)^2 + (x44 -
    x48)^2 - x101 >= 0)
@NLconstraint(m, e197, (x41 - x49)^2 + (x42 - x50)^2 + (x43 - x51)^2 + (x44 -
    x52)^2 - x101 >= 0)
@NLconstraint(m, e198, (x41 - x53)^2 + (x42 - x54)^2 + (x43 - x55)^2 + (x44 -
    x56)^2 - x101 >= 0)
@NLconstraint(m, e199, (x41 - x57)^2 + (x42 - x58)^2 + (x43 - x59)^2 + (x44 -
    x60)^2 - x101 >= 0)
@NLconstraint(m, e200, (x41 - x61)^2 + (x42 - x62)^2 + (x43 - x63)^2 + (x44 -
    x64)^2 - x101 >= 0)
@NLconstraint(m, e201, (x41 - x65)^2 + (x42 - x66)^2 + (x43 - x67)^2 + (x44 -
    x68)^2 - x101 >= 0)
@NLconstraint(m, e202, (x41 - x69)^2 + (x42 - x70)^2 + (x43 - x71)^2 + (x44 -
    x72)^2 - x101 >= 0)
@NLconstraint(m, e203, (x41 - x73)^2 + (x42 - x74)^2 + (x43 - x75)^2 + (x44 -
    x76)^2 - x101 >= 0)
@NLconstraint(m, e204, (x41 - x77)^2 + (x42 - x78)^2 + (x43 - x79)^2 + (x44 -
    x80)^2 - x101 >= 0)
@NLconstraint(m, e205, (x41 - x81)^2 + (x42 - x82)^2 + (x43 - x83)^2 + (x44 -
    x84)^2 - x101 >= 0)
@NLconstraint(m, e206, (x41 - x85)^2 + (x42 - x86)^2 + (x43 - x87)^2 + (x44 -
    x88)^2 - x101 >= 0)
@NLconstraint(m, e207, (x41 - x89)^2 + (x42 - x90)^2 + (x43 - x91)^2 + (x44 -
    x92)^2 - x101 >= 0)
@NLconstraint(m, e208, (x41 - x93)^2 + (x42 - x94)^2 + (x43 - x95)^2 + (x44 -
    x96)^2 - x101 >= 0)
@NLconstraint(m, e209, (x41 - x97)^2 + (x42 - x98)^2 + (x43 - x99)^2 + (x44 -
    x100)^2 - x101 >= 0)
@NLconstraint(m, e210, (x45 - x49)^2 + (x46 - x50)^2 + (x47 - x51)^2 + (x48 -
    x52)^2 - x101 >= 0)
@NLconstraint(m, e211, (x45 - x53)^2 + (x46 - x54)^2 + (x47 - x55)^2 + (x48 -
    x56)^2 - x101 >= 0)
@NLconstraint(m, e212, (x45 - x57)^2 + (x46 - x58)^2 + (x47 - x59)^2 + (x48 -
    x60)^2 - x101 >= 0)
@NLconstraint(m, e213, (x45 - x61)^2 + (x46 - x62)^2 + (x47 - x63)^2 + (x48 -
    x64)^2 - x101 >= 0)
@NLconstraint(m, e214, (x45 - x65)^2 + (x46 - x66)^2 + (x47 - x67)^2 + (x48 -
    x68)^2 - x101 >= 0)
@NLconstraint(m, e215, (x45 - x69)^2 + (x46 - x70)^2 + (x47 - x71)^2 + (x48 -
    x72)^2 - x101 >= 0)
@NLconstraint(m, e216, (x45 - x73)^2 + (x46 - x74)^2 + (x47 - x75)^2 + (x48 -
    x76)^2 - x101 >= 0)
@NLconstraint(m, e217, (x45 - x77)^2 + (x46 - x78)^2 + (x47 - x79)^2 + (x48 -
    x80)^2 - x101 >= 0)
@NLconstraint(m, e218, (x45 - x81)^2 + (x46 - x82)^2 + (x47 - x83)^2 + (x48 -
    x84)^2 - x101 >= 0)
@NLconstraint(m, e219, (x45 - x85)^2 + (x46 - x86)^2 + (x47 - x87)^2 + (x48 -
    x88)^2 - x101 >= 0)
@NLconstraint(m, e220, (x45 - x89)^2 + (x46 - x90)^2 + (x47 - x91)^2 + (x48 -
    x92)^2 - x101 >= 0)
@NLconstraint(m, e221, (x45 - x93)^2 + (x46 - x94)^2 + (x47 - x95)^2 + (x48 -
    x96)^2 - x101 >= 0)
@NLconstraint(m, e222, (x45 - x97)^2 + (x46 - x98)^2 + (x47 - x99)^2 + (x48 -
    x100)^2 - x101 >= 0)
@NLconstraint(m, e223, (x49 - x53)^2 + (x50 - x54)^2 + (x51 - x55)^2 + (x52 -
    x56)^2 - x101 >= 0)
@NLconstraint(m, e224, (x49 - x57)^2 + (x50 - x58)^2 + (x51 - x59)^2 + (x52 -
    x60)^2 - x101 >= 0)
@NLconstraint(m, e225, (x49 - x61)^2 + (x50 - x62)^2 + (x51 - x63)^2 + (x52 -
    x64)^2 - x101 >= 0)
@NLconstraint(m, e226, (x49 - x65)^2 + (x50 - x66)^2 + (x51 - x67)^2 + (x52 -
    x68)^2 - x101 >= 0)
@NLconstraint(m, e227, (x49 - x69)^2 + (x50 - x70)^2 + (x51 - x71)^2 + (x52 -
    x72)^2 - x101 >= 0)
@NLconstraint(m, e228, (x49 - x73)^2 + (x50 - x74)^2 + (x51 - x75)^2 + (x52 -
    x76)^2 - x101 >= 0)
@NLconstraint(m, e229, (x49 - x77)^2 + (x50 - x78)^2 + (x51 - x79)^2 + (x52 -
    x80)^2 - x101 >= 0)
@NLconstraint(m, e230, (x49 - x81)^2 + (x50 - x82)^2 + (x51 - x83)^2 + (x52 -
    x84)^2 - x101 >= 0)
@NLconstraint(m, e231, (x49 - x85)^2 + (x50 - x86)^2 + (x51 - x87)^2 + (x52 -
    x88)^2 - x101 >= 0)
@NLconstraint(m, e232, (x49 - x89)^2 + (x50 - x90)^2 + (x51 - x91)^2 + (x52 -
    x92)^2 - x101 >= 0)
@NLconstraint(m, e233, (x49 - x93)^2 + (x50 - x94)^2 + (x51 - x95)^2 + (x52 -
    x96)^2 - x101 >= 0)
@NLconstraint(m, e234, (x49 - x97)^2 + (x50 - x98)^2 + (x51 - x99)^2 + (x52 -
    x100)^2 - x101 >= 0)
@NLconstraint(m, e235, (x53 - x57)^2 + (x54 - x58)^2 + (x55 - x59)^2 + (x56 -
    x60)^2 - x101 >= 0)
@NLconstraint(m, e236, (x53 - x61)^2 + (x54 - x62)^2 + (x55 - x63)^2 + (x56 -
    x64)^2 - x101 >= 0)
@NLconstraint(m, e237, (x53 - x65)^2 + (x54 - x66)^2 + (x55 - x67)^2 + (x56 -
    x68)^2 - x101 >= 0)
@NLconstraint(m, e238, (x53 - x69)^2 + (x54 - x70)^2 + (x55 - x71)^2 + (x56 -
    x72)^2 - x101 >= 0)
@NLconstraint(m, e239, (x53 - x73)^2 + (x54 - x74)^2 + (x55 - x75)^2 + (x56 -
    x76)^2 - x101 >= 0)
@NLconstraint(m, e240, (x53 - x77)^2 + (x54 - x78)^2 + (x55 - x79)^2 + (x56 -
    x80)^2 - x101 >= 0)
@NLconstraint(m, e241, (x53 - x81)^2 + (x54 - x82)^2 + (x55 - x83)^2 + (x56 -
    x84)^2 - x101 >= 0)
@NLconstraint(m, e242, (x53 - x85)^2 + (x54 - x86)^2 + (x55 - x87)^2 + (x56 -
    x88)^2 - x101 >= 0)
@NLconstraint(m, e243, (x53 - x89)^2 + (x54 - x90)^2 + (x55 - x91)^2 + (x56 -
    x92)^2 - x101 >= 0)
@NLconstraint(m, e244, (x53 - x93)^2 + (x54 - x94)^2 + (x55 - x95)^2 + (x56 -
    x96)^2 - x101 >= 0)
@NLconstraint(m, e245, (x53 - x97)^2 + (x54 - x98)^2 + (x55 - x99)^2 + (x56 -
    x100)^2 - x101 >= 0)
@NLconstraint(m, e246, (x57 - x61)^2 + (x58 - x62)^2 + (x59 - x63)^2 + (x60 -
    x64)^2 - x101 >= 0)
@NLconstraint(m, e247, (x57 - x65)^2 + (x58 - x66)^2 + (x59 - x67)^2 + (x60 -
    x68)^2 - x101 >= 0)
@NLconstraint(m, e248, (x57 - x69)^2 + (x58 - x70)^2 + (x59 - x71)^2 + (x60 -
    x72)^2 - x101 >= 0)
@NLconstraint(m, e249, (x57 - x73)^2 + (x58 - x74)^2 + (x59 - x75)^2 + (x60 -
    x76)^2 - x101 >= 0)
@NLconstraint(m, e250, (x57 - x77)^2 + (x58 - x78)^2 + (x59 - x79)^2 + (x60 -
    x80)^2 - x101 >= 0)
@NLconstraint(m, e251, (x57 - x81)^2 + (x58 - x82)^2 + (x59 - x83)^2 + (x60 -
    x84)^2 - x101 >= 0)
@NLconstraint(m, e252, (x57 - x85)^2 + (x58 - x86)^2 + (x59 - x87)^2 + (x60 -
    x88)^2 - x101 >= 0)
@NLconstraint(m, e253, (x57 - x89)^2 + (x58 - x90)^2 + (x59 - x91)^2 + (x60 -
    x92)^2 - x101 >= 0)
@NLconstraint(m, e254, (x57 - x93)^2 + (x58 - x94)^2 + (x59 - x95)^2 + (x60 -
    x96)^2 - x101 >= 0)
@NLconstraint(m, e255, (x57 - x97)^2 + (x58 - x98)^2 + (x59 - x99)^2 + (x60 -
    x100)^2 - x101 >= 0)
@NLconstraint(m, e256, (x61 - x65)^2 + (x62 - x66)^2 + (x63 - x67)^2 + (x64 -
    x68)^2 - x101 >= 0)
@NLconstraint(m, e257, (x61 - x69)^2 + (x62 - x70)^2 + (x63 - x71)^2 + (x64 -
    x72)^2 - x101 >= 0)
@NLconstraint(m, e258, (x61 - x73)^2 + (x62 - x74)^2 + (x63 - x75)^2 + (x64 -
    x76)^2 - x101 >= 0)
@NLconstraint(m, e259, (x61 - x77)^2 + (x62 - x78)^2 + (x63 - x79)^2 + (x64 -
    x80)^2 - x101 >= 0)
@NLconstraint(m, e260, (x61 - x81)^2 + (x62 - x82)^2 + (x63 - x83)^2 + (x64 -
    x84)^2 - x101 >= 0)
@NLconstraint(m, e261, (x61 - x85)^2 + (x62 - x86)^2 + (x63 - x87)^2 + (x64 -
    x88)^2 - x101 >= 0)
@NLconstraint(m, e262, (x61 - x89)^2 + (x62 - x90)^2 + (x63 - x91)^2 + (x64 -
    x92)^2 - x101 >= 0)
@NLconstraint(m, e263, (x61 - x93)^2 + (x62 - x94)^2 + (x63 - x95)^2 + (x64 -
    x96)^2 - x101 >= 0)
@NLconstraint(m, e264, (x61 - x97)^2 + (x62 - x98)^2 + (x63 - x99)^2 + (x64 -
    x100)^2 - x101 >= 0)
@NLconstraint(m, e265, (x65 - x69)^2 + (x66 - x70)^2 + (x67 - x71)^2 + (x68 -
    x72)^2 - x101 >= 0)
@NLconstraint(m, e266, (x65 - x73)^2 + (x66 - x74)^2 + (x67 - x75)^2 + (x68 -
    x76)^2 - x101 >= 0)
@NLconstraint(m, e267, (x65 - x77)^2 + (x66 - x78)^2 + (x67 - x79)^2 + (x68 -
    x80)^2 - x101 >= 0)
@NLconstraint(m, e268, (x65 - x81)^2 + (x66 - x82)^2 + (x67 - x83)^2 + (x68 -
    x84)^2 - x101 >= 0)
@NLconstraint(m, e269, (x65 - x85)^2 + (x66 - x86)^2 + (x67 - x87)^2 + (x68 -
    x88)^2 - x101 >= 0)
@NLconstraint(m, e270, (x65 - x89)^2 + (x66 - x90)^2 + (x67 - x91)^2 + (x68 -
    x92)^2 - x101 >= 0)
@NLconstraint(m, e271, (x65 - x93)^2 + (x66 - x94)^2 + (x67 - x95)^2 + (x68 -
    x96)^2 - x101 >= 0)
@NLconstraint(m, e272, (x65 - x97)^2 + (x66 - x98)^2 + (x67 - x99)^2 + (x68 -
    x100)^2 - x101 >= 0)
@NLconstraint(m, e273, (x69 - x73)^2 + (x70 - x74)^2 + (x71 - x75)^2 + (x72 -
    x76)^2 - x101 >= 0)
@NLconstraint(m, e274, (x69 - x77)^2 + (x70 - x78)^2 + (x71 - x79)^2 + (x72 -
    x80)^2 - x101 >= 0)
@NLconstraint(m, e275, (x69 - x81)^2 + (x70 - x82)^2 + (x71 - x83)^2 + (x72 -
    x84)^2 - x101 >= 0)
@NLconstraint(m, e276, (x69 - x85)^2 + (x70 - x86)^2 + (x71 - x87)^2 + (x72 -
    x88)^2 - x101 >= 0)
@NLconstraint(m, e277, (x69 - x89)^2 + (x70 - x90)^2 + (x71 - x91)^2 + (x72 -
    x92)^2 - x101 >= 0)
@NLconstraint(m, e278, (x69 - x93)^2 + (x70 - x94)^2 + (x71 - x95)^2 + (x72 -
    x96)^2 - x101 >= 0)
@NLconstraint(m, e279, (x69 - x97)^2 + (x70 - x98)^2 + (x71 - x99)^2 + (x72 -
    x100)^2 - x101 >= 0)
@NLconstraint(m, e280, (x73 - x77)^2 + (x74 - x78)^2 + (x75 - x79)^2 + (x76 -
    x80)^2 - x101 >= 0)
@NLconstraint(m, e281, (x73 - x81)^2 + (x74 - x82)^2 + (x75 - x83)^2 + (x76 -
    x84)^2 - x101 >= 0)
@NLconstraint(m, e282, (x73 - x85)^2 + (x74 - x86)^2 + (x75 - x87)^2 + (x76 -
    x88)^2 - x101 >= 0)
@NLconstraint(m, e283, (x73 - x89)^2 + (x74 - x90)^2 + (x75 - x91)^2 + (x76 -
    x92)^2 - x101 >= 0)
@NLconstraint(m, e284, (x73 - x93)^2 + (x74 - x94)^2 + (x75 - x95)^2 + (x76 -
    x96)^2 - x101 >= 0)
@NLconstraint(m, e285, (x73 - x97)^2 + (x74 - x98)^2 + (x75 - x99)^2 + (x76 -
    x100)^2 - x101 >= 0)
@NLconstraint(m, e286, (x77 - x81)^2 + (x78 - x82)^2 + (x79 - x83)^2 + (x80 -
    x84)^2 - x101 >= 0)
@NLconstraint(m, e287, (x77 - x85)^2 + (x78 - x86)^2 + (x79 - x87)^2 + (x80 -
    x88)^2 - x101 >= 0)
@NLconstraint(m, e288, (x77 - x89)^2 + (x78 - x90)^2 + (x79 - x91)^2 + (x80 -
    x92)^2 - x101 >= 0)
@NLconstraint(m, e289, (x77 - x93)^2 + (x78 - x94)^2 + (x79 - x95)^2 + (x80 -
    x96)^2 - x101 >= 0)
@NLconstraint(m, e290, (x77 - x97)^2 + (x78 - x98)^2 + (x79 - x99)^2 + (x80 -
    x100)^2 - x101 >= 0)
@NLconstraint(m, e291, (x81 - x85)^2 + (x82 - x86)^2 + (x83 - x87)^2 + (x84 -
    x88)^2 - x101 >= 0)
@NLconstraint(m, e292, (x81 - x89)^2 + (x82 - x90)^2 + (x83 - x91)^2 + (x84 -
    x92)^2 - x101 >= 0)
@NLconstraint(m, e293, (x81 - x93)^2 + (x82 - x94)^2 + (x83 - x95)^2 + (x84 -
    x96)^2 - x101 >= 0)
@NLconstraint(m, e294, (x81 - x97)^2 + (x82 - x98)^2 + (x83 - x99)^2 + (x84 -
    x100)^2 - x101 >= 0)
@NLconstraint(m, e295, (x85 - x89)^2 + (x86 - x90)^2 + (x87 - x91)^2 + (x88 -
    x92)^2 - x101 >= 0)
@NLconstraint(m, e296, (x85 - x93)^2 + (x86 - x94)^2 + (x87 - x95)^2 + (x88 -
    x96)^2 - x101 >= 0)
@NLconstraint(m, e297, (x85 - x97)^2 + (x86 - x98)^2 + (x87 - x99)^2 + (x88 -
    x100)^2 - x101 >= 0)
@NLconstraint(m, e298, (x89 - x93)^2 + (x90 - x94)^2 + (x91 - x95)^2 + (x92 -
    x96)^2 - x101 >= 0)
@NLconstraint(m, e299, (x89 - x97)^2 + (x90 - x98)^2 + (x91 - x99)^2 + (x92 -
    x100)^2 - x101 >= 0)
@NLconstraint(m, e300, (x93 - x97)^2 + (x94 - x98)^2 + (x95 - x99)^2 + (x96 -
    x100)^2 - x101 >= 0)
@constraint(m, e301, x1 - x5 <= 0)
@constraint(m, e302, x5 - x9 <= 0)
@constraint(m, e303, x9 - x13 <= 0)
@constraint(m, e304, x13 - x17 <= 0)
@constraint(m, e305, x17 - x21 <= 0)
@constraint(m, e306, x21 - x25 <= 0)
@constraint(m, e307, x25 - x29 <= 0)
@constraint(m, e308, x29 - x33 <= 0)
@constraint(m, e309, x33 - x37 <= 0)
@constraint(m, e310, x37 - x41 <= 0)
@constraint(m, e311, x41 - x45 <= 0)
@constraint(m, e312, x45 - x49 <= 0)
@constraint(m, e313, x49 - x53 <= 0)
@constraint(m, e314, x53 - x57 <= 0)
@constraint(m, e315, x57 - x61 <= 0)
@constraint(m, e316, x61 - x65 <= 0)
@constraint(m, e317, x65 - x69 <= 0)
@constraint(m, e318, x69 - x73 <= 0)
@constraint(m, e319, x73 - x77 <= 0)
@constraint(m, e320, x77 - x81 <= 0)
@constraint(m, e321, x81 - x85 <= 0)
@constraint(m, e322, x85 - x89 <= 0)
@constraint(m, e323, x89 - x93 <= 0)
@constraint(m, e324, x93 - x97 <= 0)
@NLconstraint(m, e325, x1^2 + x2^2 + x3^2 + x4^2 == 4)
@NLconstraint(m, e326, x5^2 + x6^2 + x7^2 + x8^2 == 4)
@NLconstraint(m, e327, x9^2 + x10^2 + x11^2 + x12^2 == 4)
@NLconstraint(m, e328, x13^2 + x14^2 + x15^2 + x16^2 == 4)
@NLconstraint(m, e329, x17^2 + x18^2 + x19^2 + x20^2 == 4)
@NLconstraint(m, e330, x21^2 + x22^2 + x23^2 + x24^2 == 4)
@NLconstraint(m, e331, x25^2 + x26^2 + x27^2 + x28^2 == 4)
@NLconstraint(m, e332, x29^2 + x30^2 + x31^2 + x32^2 == 4)
@NLconstraint(m, e333, x33^2 + x34^2 + x35^2 + x36^2 == 4)
@NLconstraint(m, e334, x37^2 + x38^2 + x39^2 + x40^2 == 4)
@NLconstraint(m, e335, x41^2 + x42^2 + x43^2 + x44^2 == 4)
@NLconstraint(m, e336, x45^2 + x46^2 + x47^2 + x48^2 == 4)
@NLconstraint(m, e337, x49^2 + x50^2 + x51^2 + x52^2 == 4)
@NLconstraint(m, e338, x53^2 + x54^2 + x55^2 + x56^2 == 4)
@NLconstraint(m, e339, x57^2 + x58^2 + x59^2 + x60^2 == 4)
@NLconstraint(m, e340, x61^2 + x62^2 + x63^2 + x64^2 == 4)
@NLconstraint(m, e341, x65^2 + x66^2 + x67^2 + x68^2 == 4)
@NLconstraint(m, e342, x69^2 + x70^2 + x71^2 + x72^2 == 4)
@NLconstraint(m, e343, x73^2 + x74^2 + x75^2 + x76^2 == 4)
@NLconstraint(m, e344, x77^2 + x78^2 + x79^2 + x80^2 == 4)
@NLconstraint(m, e345, x81^2 + x82^2 + x83^2 + x84^2 == 4)
@NLconstraint(m, e346, x85^2 + x86^2 + x87^2 + x88^2 == 4)
@NLconstraint(m, e347, x89^2 + x90^2 + x91^2 + x92^2 == 4)
@NLconstraint(m, e348, x93^2 + x94^2 + x95^2 + x96^2 == 4)
@NLconstraint(m, e349, x97^2 + x98^2 + x99^2 + x100^2 == 4)
