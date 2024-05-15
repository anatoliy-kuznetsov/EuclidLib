# NLP written by GAMS Convert at 05/15/24 11:32:44
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#        20       20        0        0        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        60       60        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#        60        0       60
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

@NLobjective(m, Min, 1 / sqrt((x1 - x2)^2 + (x21 - x22)^2 + (x41 - x42)^2) + 1
    / sqrt((x1 - x3)^2 + (x21 - x23)^2 + (x41 - x43)^2) + 1 / sqrt((x1 - x4)^2
    + (x21 - x24)^2 + (x41 - x44)^2) + 1 / sqrt((x1 - x5)^2 + (x21 - x25)^2 +
    (x41 - x45)^2) + 1 / sqrt((x1 - x6)^2 + (x21 - x26)^2 + (x41 - x46)^2) + 1
    / sqrt((x1 - x7)^2 + (x21 - x27)^2 + (x41 - x47)^2) + 1 / sqrt((x1 - x8)^2
    + (x21 - x28)^2 + (x41 - x48)^2) + 1 / sqrt((x1 - x9)^2 + (x21 - x29)^2 +
    (x41 - x49)^2) + 1 / sqrt((x1 - x10)^2 + (x21 - x30)^2 + (x41 - x50)^2) + 1
    / sqrt((x1 - x11)^2 + (x21 - x31)^2 + (x41 - x51)^2) + 1 / sqrt((x1 - x12)
    ^2 + (x21 - x32)^2 + (x41 - x52)^2) + 1 / sqrt((x1 - x13)^2 + (x21 - x33)^2
    + (x41 - x53)^2) + 1 / sqrt((x1 - x14)^2 + (x21 - x34)^2 + (x41 - x54)^2)
    + 1 / sqrt((x1 - x15)^2 + (x21 - x35)^2 + (x41 - x55)^2) + 1 / sqrt((x1 -
    x16)^2 + (x21 - x36)^2 + (x41 - x56)^2) + 1 / sqrt((x1 - x17)^2 + (x21 -
    x37)^2 + (x41 - x57)^2) + 1 / sqrt((x1 - x18)^2 + (x21 - x38)^2 + (x41 -
    x58)^2) + 1 / sqrt((x1 - x19)^2 + (x21 - x39)^2 + (x41 - x59)^2) + 1 /
    sqrt((x1 - x20)^2 + (x21 - x40)^2 + (x41 - x60)^2) + 1 / sqrt((x2 - x3)^2
    + (x22 - x23)^2 + (x42 - x43)^2) + 1 / sqrt((x2 - x4)^2 + (x22 - x24)^2 +
    (x42 - x44)^2) + 1 / sqrt((x2 - x5)^2 + (x22 - x25)^2 + (x42 - x45)^2) + 1
    / sqrt((x2 - x6)^2 + (x22 - x26)^2 + (x42 - x46)^2) + 1 / sqrt((x2 - x7)^2
    + (x22 - x27)^2 + (x42 - x47)^2) + 1 / sqrt((x2 - x8)^2 + (x22 - x28)^2 +
    (x42 - x48)^2) + 1 / sqrt((x2 - x9)^2 + (x22 - x29)^2 + (x42 - x49)^2) + 1
    / sqrt((x2 - x10)^2 + (x22 - x30)^2 + (x42 - x50)^2) + 1 / sqrt((x2 - x11)
    ^2 + (x22 - x31)^2 + (x42 - x51)^2) + 1 / sqrt((x2 - x12)^2 + (x22 - x32)^2
    + (x42 - x52)^2) + 1 / sqrt((x2 - x13)^2 + (x22 - x33)^2 + (x42 - x53)^2)
    + 1 / sqrt((x2 - x14)^2 + (x22 - x34)^2 + (x42 - x54)^2) + 1 / sqrt((x2 -
    x15)^2 + (x22 - x35)^2 + (x42 - x55)^2) + 1 / sqrt((x2 - x16)^2 + (x22 -
    x36)^2 + (x42 - x56)^2) + 1 / sqrt((x2 - x17)^2 + (x22 - x37)^2 + (x42 -
    x57)^2) + 1 / sqrt((x2 - x18)^2 + (x22 - x38)^2 + (x42 - x58)^2) + 1 /
    sqrt((x2 - x19)^2 + (x22 - x39)^2 + (x42 - x59)^2) + 1 / sqrt((x2 - x20)^2
    + (x22 - x40)^2 + (x42 - x60)^2) + 1 / sqrt((x3 - x4)^2 + (x23 - x24)^2 +
    (x43 - x44)^2) + 1 / sqrt((x3 - x5)^2 + (x23 - x25)^2 + (x43 - x45)^2) + 1
    / sqrt((x3 - x6)^2 + (x23 - x26)^2 + (x43 - x46)^2) + 1 / sqrt((x3 - x7)^2
    + (x23 - x27)^2 + (x43 - x47)^2) + 1 / sqrt((x3 - x8)^2 + (x23 - x28)^2 +
    (x43 - x48)^2) + 1 / sqrt((x3 - x9)^2 + (x23 - x29)^2 + (x43 - x49)^2) + 1
    / sqrt((x3 - x10)^2 + (x23 - x30)^2 + (x43 - x50)^2) + 1 / sqrt((x3 - x11)
    ^2 + (x23 - x31)^2 + (x43 - x51)^2) + 1 / sqrt((x3 - x12)^2 + (x23 - x32)^2
    + (x43 - x52)^2) + 1 / sqrt((x3 - x13)^2 + (x23 - x33)^2 + (x43 - x53)^2)
    + 1 / sqrt((x3 - x14)^2 + (x23 - x34)^2 + (x43 - x54)^2) + 1 / sqrt((x3 -
    x15)^2 + (x23 - x35)^2 + (x43 - x55)^2) + 1 / sqrt((x3 - x16)^2 + (x23 -
    x36)^2 + (x43 - x56)^2) + 1 / sqrt((x3 - x17)^2 + (x23 - x37)^2 + (x43 -
    x57)^2) + 1 / sqrt((x3 - x18)^2 + (x23 - x38)^2 + (x43 - x58)^2) + 1 /
    sqrt((x3 - x19)^2 + (x23 - x39)^2 + (x43 - x59)^2) + 1 / sqrt((x3 - x20)^2
    + (x23 - x40)^2 + (x43 - x60)^2) + 1 / sqrt((x4 - x5)^2 + (x24 - x25)^2 +
    (x44 - x45)^2) + 1 / sqrt((x4 - x6)^2 + (x24 - x26)^2 + (x44 - x46)^2) + 1
    / sqrt((x4 - x7)^2 + (x24 - x27)^2 + (x44 - x47)^2) + 1 / sqrt((x4 - x8)^2
    + (x24 - x28)^2 + (x44 - x48)^2) + 1 / sqrt((x4 - x9)^2 + (x24 - x29)^2 +
    (x44 - x49)^2) + 1 / sqrt((x4 - x10)^2 + (x24 - x30)^2 + (x44 - x50)^2) + 1
    / sqrt((x4 - x11)^2 + (x24 - x31)^2 + (x44 - x51)^2) + 1 / sqrt((x4 - x12)
    ^2 + (x24 - x32)^2 + (x44 - x52)^2) + 1 / sqrt((x4 - x13)^2 + (x24 - x33)^2
    + (x44 - x53)^2) + 1 / sqrt((x4 - x14)^2 + (x24 - x34)^2 + (x44 - x54)^2)
    + 1 / sqrt((x4 - x15)^2 + (x24 - x35)^2 + (x44 - x55)^2) + 1 / sqrt((x4 -
    x16)^2 + (x24 - x36)^2 + (x44 - x56)^2) + 1 / sqrt((x4 - x17)^2 + (x24 -
    x37)^2 + (x44 - x57)^2) + 1 / sqrt((x4 - x18)^2 + (x24 - x38)^2 + (x44 -
    x58)^2) + 1 / sqrt((x4 - x19)^2 + (x24 - x39)^2 + (x44 - x59)^2) + 1 /
    sqrt((x4 - x20)^2 + (x24 - x40)^2 + (x44 - x60)^2) + 1 / sqrt((x5 - x6)^2
    + (x25 - x26)^2 + (x45 - x46)^2) + 1 / sqrt((x5 - x7)^2 + (x25 - x27)^2 +
    (x45 - x47)^2) + 1 / sqrt((x5 - x8)^2 + (x25 - x28)^2 + (x45 - x48)^2) + 1
    / sqrt((x5 - x9)^2 + (x25 - x29)^2 + (x45 - x49)^2) + 1 / sqrt((x5 - x10)^
    2 + (x25 - x30)^2 + (x45 - x50)^2) + 1 / sqrt((x5 - x11)^2 + (x25 - x31)^2
    + (x45 - x51)^2) + 1 / sqrt((x5 - x12)^2 + (x25 - x32)^2 + (x45 - x52)^2)
    + 1 / sqrt((x5 - x13)^2 + (x25 - x33)^2 + (x45 - x53)^2) + 1 / sqrt((x5 -
    x14)^2 + (x25 - x34)^2 + (x45 - x54)^2) + 1 / sqrt((x5 - x15)^2 + (x25 -
    x35)^2 + (x45 - x55)^2) + 1 / sqrt((x5 - x16)^2 + (x25 - x36)^2 + (x45 -
    x56)^2) + 1 / sqrt((x5 - x17)^2 + (x25 - x37)^2 + (x45 - x57)^2) + 1 /
    sqrt((x5 - x18)^2 + (x25 - x38)^2 + (x45 - x58)^2) + 1 / sqrt((x5 - x19)^2
    + (x25 - x39)^2 + (x45 - x59)^2) + 1 / sqrt((x5 - x20)^2 + (x25 - x40)^2
    + (x45 - x60)^2) + 1 / sqrt((x6 - x7)^2 + (x26 - x27)^2 + (x46 - x47)^2)
    + 1 / sqrt((x6 - x8)^2 + (x26 - x28)^2 + (x46 - x48)^2) + 1 / sqrt((x6 -
    x9)^2 + (x26 - x29)^2 + (x46 - x49)^2) + 1 / sqrt((x6 - x10)^2 + (x26 - x30)
    ^2 + (x46 - x50)^2) + 1 / sqrt((x6 - x11)^2 + (x26 - x31)^2 + (x46 - x51)^2)
    + 1 / sqrt((x6 - x12)^2 + (x26 - x32)^2 + (x46 - x52)^2) + 1 / sqrt((x6 -
    x13)^2 + (x26 - x33)^2 + (x46 - x53)^2) + 1 / sqrt((x6 - x14)^2 + (x26 -
    x34)^2 + (x46 - x54)^2) + 1 / sqrt((x6 - x15)^2 + (x26 - x35)^2 + (x46 -
    x55)^2) + 1 / sqrt((x6 - x16)^2 + (x26 - x36)^2 + (x46 - x56)^2) + 1 /
    sqrt((x6 - x17)^2 + (x26 - x37)^2 + (x46 - x57)^2) + 1 / sqrt((x6 - x18)^2
    + (x26 - x38)^2 + (x46 - x58)^2) + 1 / sqrt((x6 - x19)^2 + (x26 - x39)^2
    + (x46 - x59)^2) + 1 / sqrt((x6 - x20)^2 + (x26 - x40)^2 + (x46 - x60)^2)
    + 1 / sqrt((x7 - x8)^2 + (x27 - x28)^2 + (x47 - x48)^2) + 1 / sqrt((x7 -
    x9)^2 + (x27 - x29)^2 + (x47 - x49)^2) + 1 / sqrt((x7 - x10)^2 + (x27 - x30)
    ^2 + (x47 - x50)^2) + 1 / sqrt((x7 - x11)^2 + (x27 - x31)^2 + (x47 - x51)^2)
    + 1 / sqrt((x7 - x12)^2 + (x27 - x32)^2 + (x47 - x52)^2) + 1 / sqrt((x7 -
    x13)^2 + (x27 - x33)^2 + (x47 - x53)^2) + 1 / sqrt((x7 - x14)^2 + (x27 -
    x34)^2 + (x47 - x54)^2) + 1 / sqrt((x7 - x15)^2 + (x27 - x35)^2 + (x47 -
    x55)^2) + 1 / sqrt((x7 - x16)^2 + (x27 - x36)^2 + (x47 - x56)^2) + 1 /
    sqrt((x7 - x17)^2 + (x27 - x37)^2 + (x47 - x57)^2) + 1 / sqrt((x7 - x18)^2
    + (x27 - x38)^2 + (x47 - x58)^2) + 1 / sqrt((x7 - x19)^2 + (x27 - x39)^2
    + (x47 - x59)^2) + 1 / sqrt((x7 - x20)^2 + (x27 - x40)^2 + (x47 - x60)^2)
    + 1 / sqrt((x8 - x9)^2 + (x28 - x29)^2 + (x48 - x49)^2) + 1 / sqrt((x8 -
    x10)^2 + (x28 - x30)^2 + (x48 - x50)^2) + 1 / sqrt((x8 - x11)^2 + (x28 -
    x31)^2 + (x48 - x51)^2) + 1 / sqrt((x8 - x12)^2 + (x28 - x32)^2 + (x48 -
    x52)^2) + 1 / sqrt((x8 - x13)^2 + (x28 - x33)^2 + (x48 - x53)^2) + 1 /
    sqrt((x8 - x14)^2 + (x28 - x34)^2 + (x48 - x54)^2) + 1 / sqrt((x8 - x15)^2
    + (x28 - x35)^2 + (x48 - x55)^2) + 1 / sqrt((x8 - x16)^2 + (x28 - x36)^2
    + (x48 - x56)^2) + 1 / sqrt((x8 - x17)^2 + (x28 - x37)^2 + (x48 - x57)^2)
    + 1 / sqrt((x8 - x18)^2 + (x28 - x38)^2 + (x48 - x58)^2) + 1 / sqrt((x8 -
    x19)^2 + (x28 - x39)^2 + (x48 - x59)^2) + 1 / sqrt((x8 - x20)^2 + (x28 -
    x40)^2 + (x48 - x60)^2) + 1 / sqrt((x9 - x10)^2 + (x29 - x30)^2 + (x49 -
    x50)^2) + 1 / sqrt((x9 - x11)^2 + (x29 - x31)^2 + (x49 - x51)^2) + 1 /
    sqrt((x9 - x12)^2 + (x29 - x32)^2 + (x49 - x52)^2) + 1 / sqrt((x9 - x13)^2
    + (x29 - x33)^2 + (x49 - x53)^2) + 1 / sqrt((x9 - x14)^2 + (x29 - x34)^2
    + (x49 - x54)^2) + 1 / sqrt((x9 - x15)^2 + (x29 - x35)^2 + (x49 - x55)^2)
    + 1 / sqrt((x9 - x16)^2 + (x29 - x36)^2 + (x49 - x56)^2) + 1 / sqrt((x9 -
    x17)^2 + (x29 - x37)^2 + (x49 - x57)^2) + 1 / sqrt((x9 - x18)^2 + (x29 -
    x38)^2 + (x49 - x58)^2) + 1 / sqrt((x9 - x19)^2 + (x29 - x39)^2 + (x49 -
    x59)^2) + 1 / sqrt((x9 - x20)^2 + (x29 - x40)^2 + (x49 - x60)^2) + 1 /
    sqrt((x10 - x11)^2 + (x30 - x31)^2 + (x50 - x51)^2) + 1 / sqrt((x10 - x12)^
    2 + (x30 - x32)^2 + (x50 - x52)^2) + 1 / sqrt((x10 - x13)^2 + (x30 - x33)^2
    + (x50 - x53)^2) + 1 / sqrt((x10 - x14)^2 + (x30 - x34)^2 + (x50 - x54)^2)
    + 1 / sqrt((x10 - x15)^2 + (x30 - x35)^2 + (x50 - x55)^2) + 1 / sqrt((x10
    - x16)^2 + (x30 - x36)^2 + (x50 - x56)^2) + 1 / sqrt((x10 - x17)^2 + (x30
    - x37)^2 + (x50 - x57)^2) + 1 / sqrt((x10 - x18)^2 + (x30 - x38)^2 + (x50
    - x58)^2) + 1 / sqrt((x10 - x19)^2 + (x30 - x39)^2 + (x50 - x59)^2) + 1 /
    sqrt((x10 - x20)^2 + (x30 - x40)^2 + (x50 - x60)^2) + 1 / sqrt((x11 - x12)^
    2 + (x31 - x32)^2 + (x51 - x52)^2) + 1 / sqrt((x11 - x13)^2 + (x31 - x33)^2
    + (x51 - x53)^2) + 1 / sqrt((x11 - x14)^2 + (x31 - x34)^2 + (x51 - x54)^2)
    + 1 / sqrt((x11 - x15)^2 + (x31 - x35)^2 + (x51 - x55)^2) + 1 / sqrt((x11
    - x16)^2 + (x31 - x36)^2 + (x51 - x56)^2) + 1 / sqrt((x11 - x17)^2 + (x31
    - x37)^2 + (x51 - x57)^2) + 1 / sqrt((x11 - x18)^2 + (x31 - x38)^2 + (x51
    - x58)^2) + 1 / sqrt((x11 - x19)^2 + (x31 - x39)^2 + (x51 - x59)^2) + 1 /
    sqrt((x11 - x20)^2 + (x31 - x40)^2 + (x51 - x60)^2) + 1 / sqrt((x12 - x13)^
    2 + (x32 - x33)^2 + (x52 - x53)^2) + 1 / sqrt((x12 - x14)^2 + (x32 - x34)^2
    + (x52 - x54)^2) + 1 / sqrt((x12 - x15)^2 + (x32 - x35)^2 + (x52 - x55)^2)
    + 1 / sqrt((x12 - x16)^2 + (x32 - x36)^2 + (x52 - x56)^2) + 1 / sqrt((x12
    - x17)^2 + (x32 - x37)^2 + (x52 - x57)^2) + 1 / sqrt((x12 - x18)^2 + (x32
    - x38)^2 + (x52 - x58)^2) + 1 / sqrt((x12 - x19)^2 + (x32 - x39)^2 + (x52
    - x59)^2) + 1 / sqrt((x12 - x20)^2 + (x32 - x40)^2 + (x52 - x60)^2) + 1 /
    sqrt((x13 - x14)^2 + (x33 - x34)^2 + (x53 - x54)^2) + 1 / sqrt((x13 - x15)^
    2 + (x33 - x35)^2 + (x53 - x55)^2) + 1 / sqrt((x13 - x16)^2 + (x33 - x36)^2
    + (x53 - x56)^2) + 1 / sqrt((x13 - x17)^2 + (x33 - x37)^2 + (x53 - x57)^2)
    + 1 / sqrt((x13 - x18)^2 + (x33 - x38)^2 + (x53 - x58)^2) + 1 / sqrt((x13
    - x19)^2 + (x33 - x39)^2 + (x53 - x59)^2) + 1 / sqrt((x13 - x20)^2 + (x33
    - x40)^2 + (x53 - x60)^2) + 1 / sqrt((x14 - x15)^2 + (x34 - x35)^2 + (x54
    - x55)^2) + 1 / sqrt((x14 - x16)^2 + (x34 - x36)^2 + (x54 - x56)^2) + 1 /
    sqrt((x14 - x17)^2 + (x34 - x37)^2 + (x54 - x57)^2) + 1 / sqrt((x14 - x18)^
    2 + (x34 - x38)^2 + (x54 - x58)^2) + 1 / sqrt((x14 - x19)^2 + (x34 - x39)^2
    + (x54 - x59)^2) + 1 / sqrt((x14 - x20)^2 + (x34 - x40)^2 + (x54 - x60)^2)
    + 1 / sqrt((x15 - x16)^2 + (x35 - x36)^2 + (x55 - x56)^2) + 1 / sqrt((x15
    - x17)^2 + (x35 - x37)^2 + (x55 - x57)^2) + 1 / sqrt((x15 - x18)^2 + (x35
    - x38)^2 + (x55 - x58)^2) + 1 / sqrt((x15 - x19)^2 + (x35 - x39)^2 + (x55
    - x59)^2) + 1 / sqrt((x15 - x20)^2 + (x35 - x40)^2 + (x55 - x60)^2) + 1 /
    sqrt((x16 - x17)^2 + (x36 - x37)^2 + (x56 - x57)^2) + 1 / sqrt((x16 - x18)^
    2 + (x36 - x38)^2 + (x56 - x58)^2) + 1 / sqrt((x16 - x19)^2 + (x36 - x39)^2
    + (x56 - x59)^2) + 1 / sqrt((x16 - x20)^2 + (x36 - x40)^2 + (x56 - x60)^2)
    + 1 / sqrt((x17 - x18)^2 + (x37 - x38)^2 + (x57 - x58)^2) + 1 / sqrt((x17
    - x19)^2 + (x37 - x39)^2 + (x57 - x59)^2) + 1 / sqrt((x17 - x20)^2 + (x37
    - x40)^2 + (x57 - x60)^2) + 1 / sqrt((x18 - x19)^2 + (x38 - x39)^2 + (x58
    - x59)^2) + 1 / sqrt((x18 - x20)^2 + (x38 - x40)^2 + (x58 - x60)^2) + 1 /
    sqrt((x19 - x20)^2 + (x39 - x40)^2 + (x59 - x60)^2))

@NLconstraint(m, e1, x1^2 + x21^2 + x41^2 == 1)
@NLconstraint(m, e2, x2^2 + x22^2 + x42^2 == 1)
@NLconstraint(m, e3, x3^2 + x23^2 + x43^2 == 1)
@NLconstraint(m, e4, x4^2 + x24^2 + x44^2 == 1)
@NLconstraint(m, e5, x5^2 + x25^2 + x45^2 == 1)
@NLconstraint(m, e6, x6^2 + x26^2 + x46^2 == 1)
@NLconstraint(m, e7, x7^2 + x27^2 + x47^2 == 1)
@NLconstraint(m, e8, x8^2 + x28^2 + x48^2 == 1)
@NLconstraint(m, e9, x9^2 + x29^2 + x49^2 == 1)
@NLconstraint(m, e10, x10^2 + x30^2 + x50^2 == 1)
@NLconstraint(m, e11, x11^2 + x31^2 + x51^2 == 1)
@NLconstraint(m, e12, x12^2 + x32^2 + x52^2 == 1)
@NLconstraint(m, e13, x13^2 + x33^2 + x53^2 == 1)
@NLconstraint(m, e14, x14^2 + x34^2 + x54^2 == 1)
@NLconstraint(m, e15, x15^2 + x35^2 + x55^2 == 1)
@NLconstraint(m, e16, x16^2 + x36^2 + x56^2 == 1)
@NLconstraint(m, e17, x17^2 + x37^2 + x57^2 == 1)
@NLconstraint(m, e18, x18^2 + x38^2 + x58^2 == 1)
@NLconstraint(m, e19, x19^2 + x39^2 + x59^2 == 1)
@NLconstraint(m, e20, x20^2 + x40^2 + x60^2 == 1)
