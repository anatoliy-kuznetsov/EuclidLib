# NLP written by GAMS Convert at 05/15/24 11:34:03
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#        15       15        0        0        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        45       45        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#        45        0       45
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

@NLobjective(m, Min, 1 / sqrt((x1 - x2)^2 + (x16 - x17)^2 + (x31 - x32)^2) + 1
    / sqrt((x1 - x3)^2 + (x16 - x18)^2 + (x31 - x33)^2) + 1 / sqrt((x1 - x4)^2
    + (x16 - x19)^2 + (x31 - x34)^2) + 1 / sqrt((x1 - x5)^2 + (x16 - x20)^2 +
    (x31 - x35)^2) + 1 / sqrt((x1 - x6)^2 + (x16 - x21)^2 + (x31 - x36)^2) + 1
    / sqrt((x1 - x7)^2 + (x16 - x22)^2 + (x31 - x37)^2) + 1 / sqrt((x1 - x8)^2
    + (x16 - x23)^2 + (x31 - x38)^2) + 1 / sqrt((x1 - x9)^2 + (x16 - x24)^2 +
    (x31 - x39)^2) + 1 / sqrt((x1 - x10)^2 + (x16 - x25)^2 + (x31 - x40)^2) + 1
    / sqrt((x1 - x11)^2 + (x16 - x26)^2 + (x31 - x41)^2) + 1 / sqrt((x1 - x12)
    ^2 + (x16 - x27)^2 + (x31 - x42)^2) + 1 / sqrt((x1 - x13)^2 + (x16 - x28)^2
    + (x31 - x43)^2) + 1 / sqrt((x1 - x14)^2 + (x16 - x29)^2 + (x31 - x44)^2)
    + 1 / sqrt((x1 - x15)^2 + (x16 - x30)^2 + (x31 - x45)^2) + 1 / sqrt((x2 -
    x3)^2 + (x17 - x18)^2 + (x32 - x33)^2) + 1 / sqrt((x2 - x4)^2 + (x17 - x19)
    ^2 + (x32 - x34)^2) + 1 / sqrt((x2 - x5)^2 + (x17 - x20)^2 + (x32 - x35)^2)
    + 1 / sqrt((x2 - x6)^2 + (x17 - x21)^2 + (x32 - x36)^2) + 1 / sqrt((x2 -
    x7)^2 + (x17 - x22)^2 + (x32 - x37)^2) + 1 / sqrt((x2 - x8)^2 + (x17 - x23)
    ^2 + (x32 - x38)^2) + 1 / sqrt((x2 - x9)^2 + (x17 - x24)^2 + (x32 - x39)^2)
    + 1 / sqrt((x2 - x10)^2 + (x17 - x25)^2 + (x32 - x40)^2) + 1 / sqrt((x2 -
    x11)^2 + (x17 - x26)^2 + (x32 - x41)^2) + 1 / sqrt((x2 - x12)^2 + (x17 -
    x27)^2 + (x32 - x42)^2) + 1 / sqrt((x2 - x13)^2 + (x17 - x28)^2 + (x32 -
    x43)^2) + 1 / sqrt((x2 - x14)^2 + (x17 - x29)^2 + (x32 - x44)^2) + 1 /
    sqrt((x2 - x15)^2 + (x17 - x30)^2 + (x32 - x45)^2) + 1 / sqrt((x3 - x4)^2
    + (x18 - x19)^2 + (x33 - x34)^2) + 1 / sqrt((x3 - x5)^2 + (x18 - x20)^2 +
    (x33 - x35)^2) + 1 / sqrt((x3 - x6)^2 + (x18 - x21)^2 + (x33 - x36)^2) + 1
    / sqrt((x3 - x7)^2 + (x18 - x22)^2 + (x33 - x37)^2) + 1 / sqrt((x3 - x8)^2
    + (x18 - x23)^2 + (x33 - x38)^2) + 1 / sqrt((x3 - x9)^2 + (x18 - x24)^2 +
    (x33 - x39)^2) + 1 / sqrt((x3 - x10)^2 + (x18 - x25)^2 + (x33 - x40)^2) + 1
    / sqrt((x3 - x11)^2 + (x18 - x26)^2 + (x33 - x41)^2) + 1 / sqrt((x3 - x12)
    ^2 + (x18 - x27)^2 + (x33 - x42)^2) + 1 / sqrt((x3 - x13)^2 + (x18 - x28)^2
    + (x33 - x43)^2) + 1 / sqrt((x3 - x14)^2 + (x18 - x29)^2 + (x33 - x44)^2)
    + 1 / sqrt((x3 - x15)^2 + (x18 - x30)^2 + (x33 - x45)^2) + 1 / sqrt((x4 -
    x5)^2 + (x19 - x20)^2 + (x34 - x35)^2) + 1 / sqrt((x4 - x6)^2 + (x19 - x21)
    ^2 + (x34 - x36)^2) + 1 / sqrt((x4 - x7)^2 + (x19 - x22)^2 + (x34 - x37)^2)
    + 1 / sqrt((x4 - x8)^2 + (x19 - x23)^2 + (x34 - x38)^2) + 1 / sqrt((x4 -
    x9)^2 + (x19 - x24)^2 + (x34 - x39)^2) + 1 / sqrt((x4 - x10)^2 + (x19 - x25)
    ^2 + (x34 - x40)^2) + 1 / sqrt((x4 - x11)^2 + (x19 - x26)^2 + (x34 - x41)^2)
    + 1 / sqrt((x4 - x12)^2 + (x19 - x27)^2 + (x34 - x42)^2) + 1 / sqrt((x4 -
    x13)^2 + (x19 - x28)^2 + (x34 - x43)^2) + 1 / sqrt((x4 - x14)^2 + (x19 -
    x29)^2 + (x34 - x44)^2) + 1 / sqrt((x4 - x15)^2 + (x19 - x30)^2 + (x34 -
    x45)^2) + 1 / sqrt((x5 - x6)^2 + (x20 - x21)^2 + (x35 - x36)^2) + 1 / sqrt(
    (x5 - x7)^2 + (x20 - x22)^2 + (x35 - x37)^2) + 1 / sqrt((x5 - x8)^2 + (x20
    - x23)^2 + (x35 - x38)^2) + 1 / sqrt((x5 - x9)^2 + (x20 - x24)^2 + (x35 -
    x39)^2) + 1 / sqrt((x5 - x10)^2 + (x20 - x25)^2 + (x35 - x40)^2) + 1 /
    sqrt((x5 - x11)^2 + (x20 - x26)^2 + (x35 - x41)^2) + 1 / sqrt((x5 - x12)^2
    + (x20 - x27)^2 + (x35 - x42)^2) + 1 / sqrt((x5 - x13)^2 + (x20 - x28)^2
    + (x35 - x43)^2) + 1 / sqrt((x5 - x14)^2 + (x20 - x29)^2 + (x35 - x44)^2)
    + 1 / sqrt((x5 - x15)^2 + (x20 - x30)^2 + (x35 - x45)^2) + 1 / sqrt((x6 -
    x7)^2 + (x21 - x22)^2 + (x36 - x37)^2) + 1 / sqrt((x6 - x8)^2 + (x21 - x23)
    ^2 + (x36 - x38)^2) + 1 / sqrt((x6 - x9)^2 + (x21 - x24)^2 + (x36 - x39)^2)
    + 1 / sqrt((x6 - x10)^2 + (x21 - x25)^2 + (x36 - x40)^2) + 1 / sqrt((x6 -
    x11)^2 + (x21 - x26)^2 + (x36 - x41)^2) + 1 / sqrt((x6 - x12)^2 + (x21 -
    x27)^2 + (x36 - x42)^2) + 1 / sqrt((x6 - x13)^2 + (x21 - x28)^2 + (x36 -
    x43)^2) + 1 / sqrt((x6 - x14)^2 + (x21 - x29)^2 + (x36 - x44)^2) + 1 /
    sqrt((x6 - x15)^2 + (x21 - x30)^2 + (x36 - x45)^2) + 1 / sqrt((x7 - x8)^2
    + (x22 - x23)^2 + (x37 - x38)^2) + 1 / sqrt((x7 - x9)^2 + (x22 - x24)^2 +
    (x37 - x39)^2) + 1 / sqrt((x7 - x10)^2 + (x22 - x25)^2 + (x37 - x40)^2) + 1
    / sqrt((x7 - x11)^2 + (x22 - x26)^2 + (x37 - x41)^2) + 1 / sqrt((x7 - x12)
    ^2 + (x22 - x27)^2 + (x37 - x42)^2) + 1 / sqrt((x7 - x13)^2 + (x22 - x28)^2
    + (x37 - x43)^2) + 1 / sqrt((x7 - x14)^2 + (x22 - x29)^2 + (x37 - x44)^2)
    + 1 / sqrt((x7 - x15)^2 + (x22 - x30)^2 + (x37 - x45)^2) + 1 / sqrt((x8 -
    x9)^2 + (x23 - x24)^2 + (x38 - x39)^2) + 1 / sqrt((x8 - x10)^2 + (x23 - x25)
    ^2 + (x38 - x40)^2) + 1 / sqrt((x8 - x11)^2 + (x23 - x26)^2 + (x38 - x41)^2)
    + 1 / sqrt((x8 - x12)^2 + (x23 - x27)^2 + (x38 - x42)^2) + 1 / sqrt((x8 -
    x13)^2 + (x23 - x28)^2 + (x38 - x43)^2) + 1 / sqrt((x8 - x14)^2 + (x23 -
    x29)^2 + (x38 - x44)^2) + 1 / sqrt((x8 - x15)^2 + (x23 - x30)^2 + (x38 -
    x45)^2) + 1 / sqrt((x9 - x10)^2 + (x24 - x25)^2 + (x39 - x40)^2) + 1 /
    sqrt((x9 - x11)^2 + (x24 - x26)^2 + (x39 - x41)^2) + 1 / sqrt((x9 - x12)^2
    + (x24 - x27)^2 + (x39 - x42)^2) + 1 / sqrt((x9 - x13)^2 + (x24 - x28)^2
    + (x39 - x43)^2) + 1 / sqrt((x9 - x14)^2 + (x24 - x29)^2 + (x39 - x44)^2)
    + 1 / sqrt((x9 - x15)^2 + (x24 - x30)^2 + (x39 - x45)^2) + 1 / sqrt((x10
    - x11)^2 + (x25 - x26)^2 + (x40 - x41)^2) + 1 / sqrt((x10 - x12)^2 + (x25
    - x27)^2 + (x40 - x42)^2) + 1 / sqrt((x10 - x13)^2 + (x25 - x28)^2 + (x40
    - x43)^2) + 1 / sqrt((x10 - x14)^2 + (x25 - x29)^2 + (x40 - x44)^2) + 1 /
    sqrt((x10 - x15)^2 + (x25 - x30)^2 + (x40 - x45)^2) + 1 / sqrt((x11 - x12)^
    2 + (x26 - x27)^2 + (x41 - x42)^2) + 1 / sqrt((x11 - x13)^2 + (x26 - x28)^2
    + (x41 - x43)^2) + 1 / sqrt((x11 - x14)^2 + (x26 - x29)^2 + (x41 - x44)^2)
    + 1 / sqrt((x11 - x15)^2 + (x26 - x30)^2 + (x41 - x45)^2) + 1 / sqrt((x12
    - x13)^2 + (x27 - x28)^2 + (x42 - x43)^2) + 1 / sqrt((x12 - x14)^2 + (x27
    - x29)^2 + (x42 - x44)^2) + 1 / sqrt((x12 - x15)^2 + (x27 - x30)^2 + (x42
    - x45)^2) + 1 / sqrt((x13 - x14)^2 + (x28 - x29)^2 + (x43 - x44)^2) + 1 /
    sqrt((x13 - x15)^2 + (x28 - x30)^2 + (x43 - x45)^2) + 1 / sqrt((x14 - x15)^
    2 + (x29 - x30)^2 + (x44 - x45)^2))

@NLconstraint(m, e1, x1^2 + x16^2 + x31^2 == 1)
@NLconstraint(m, e2, x2^2 + x17^2 + x32^2 == 1)
@NLconstraint(m, e3, x3^2 + x18^2 + x33^2 == 1)
@NLconstraint(m, e4, x4^2 + x19^2 + x34^2 == 1)
@NLconstraint(m, e5, x5^2 + x20^2 + x35^2 == 1)
@NLconstraint(m, e6, x6^2 + x21^2 + x36^2 == 1)
@NLconstraint(m, e7, x7^2 + x22^2 + x37^2 == 1)
@NLconstraint(m, e8, x8^2 + x23^2 + x38^2 == 1)
@NLconstraint(m, e9, x9^2 + x24^2 + x39^2 == 1)
@NLconstraint(m, e10, x10^2 + x25^2 + x40^2 == 1)
@NLconstraint(m, e11, x11^2 + x26^2 + x41^2 == 1)
@NLconstraint(m, e12, x12^2 + x27^2 + x42^2 == 1)
@NLconstraint(m, e13, x13^2 + x28^2 + x43^2 == 1)
@NLconstraint(m, e14, x14^2 + x29^2 + x44^2 == 1)
@NLconstraint(m, e15, x15^2 + x30^2 + x45^2 == 1)