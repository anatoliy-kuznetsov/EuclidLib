# NLP written by GAMS Convert at 05/15/24 11:30:39
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       136        0      136        0        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        51       51        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       816        0      816
#
# Reformulation has removed 1 variable and 1 equation

using JuMP
using MathOptInterface
const MOI = MathOptInterface

model = m = Model()

@variable(m, 0 <= x1 <= 16, start=0)
@variable(m, 0 <= x2 <= 16, start=0)
@variable(m, 0 <= x3 <= 16, start=0)
@variable(m, 0 <= x4 <= 16, start=0)
@variable(m, 0 <= x5 <= 16, start=0)
@variable(m, 0 <= x6 <= 16, start=0)
@variable(m, 0 <= x7 <= 16, start=0)
@variable(m, 0 <= x8 <= 16, start=0)
@variable(m, 0 <= x9 <= 16, start=0)
@variable(m, 0 <= x10 <= 16, start=0)
@variable(m, 0 <= x11 <= 16, start=0)
@variable(m, 0 <= x12 <= 16, start=0)
@variable(m, 0 <= x13 <= 16, start=0)
@variable(m, 0 <= x14 <= 16, start=0)
@variable(m, 0 <= x15 <= 16, start=0)
@variable(m, 0 <= x16 <= 16, start=0)
@variable(m, 0 <= x17 <= 16, start=0)
@variable(m, -16 <= x18 <= 16, start=0)
@variable(m, -16 <= x19 <= 16, start=0)
@variable(m, -16 <= x20 <= 16, start=0)
@variable(m, -16 <= x21 <= 16, start=0)
@variable(m, -16 <= x22 <= 16, start=0)
@variable(m, -16 <= x23 <= 16, start=0)
@variable(m, -16 <= x24 <= 16, start=0)
@variable(m, -16 <= x25 <= 16, start=0)
@variable(m, -16 <= x26 <= 16, start=0)
@variable(m, -16 <= x27 <= 16, start=0)
@variable(m, -16 <= x28 <= 16, start=0)
@variable(m, -16 <= x29 <= 16, start=0)
@variable(m, -16 <= x30 <= 16, start=0)
@variable(m, -16 <= x31 <= 16, start=0)
@variable(m, -16 <= x32 <= 16, start=0)
@variable(m, -16 <= x33 <= 16, start=0)
@variable(m, -16 <= x34 <= 16, start=0)
@variable(m, -16 <= x35 <= 16, start=0)
@variable(m, -16 <= x36 <= 16, start=0)
@variable(m, -16 <= x37 <= 16, start=0)
@variable(m, -16 <= x38 <= 16, start=0)
@variable(m, -16 <= x39 <= 16, start=0)
@variable(m, -16 <= x40 <= 16, start=0)
@variable(m, -16 <= x41 <= 16, start=0)
@variable(m, -16 <= x42 <= 16, start=0)
@variable(m, -16 <= x43 <= 16, start=0)
@variable(m, -16 <= x44 <= 16, start=0)
@variable(m, -16 <= x45 <= 16, start=0)
@variable(m, -16 <= x46 <= 16, start=0)
@variable(m, -16 <= x47 <= 16, start=0)
@variable(m, -16 <= x48 <= 16, start=0)
@variable(m, -16 <= x49 <= 16, start=0)
@variable(m, -16 <= x50 <= 16, start=0)
@variable(m, -16 <= x51 <= 16, start=0)

@NLobjective(m, Min, exp(-6 * sqrt((x1 - x2)^2 + (x18 - x19)^2 + (x35 - x36)^2)
    + 6) * (exp(-6 * sqrt((x1 - x2)^2 + (x18 - x19)^2 + (x35 - x36)^2) + 6) -
    2) + exp(-6 * sqrt((x1 - x3)^2 + (x18 - x20)^2 + (x35 - x37)^2) + 6) * (
    exp(-6 * sqrt((x1 - x3)^2 + (x18 - x20)^2 + (x35 - x37)^2) + 6) - 2) + exp(
    -6 * sqrt((x1 - x4)^2 + (x18 - x21)^2 + (x35 - x38)^2) + 6) * (exp(-6 *
    sqrt((x1 - x4)^2 + (x18 - x21)^2 + (x35 - x38)^2) + 6) - 2) + exp(-6 *
    sqrt((x1 - x5)^2 + (x18 - x22)^2 + (x35 - x39)^2) + 6) * (exp(-6 * sqrt((x1
    - x5)^2 + (x18 - x22)^2 + (x35 - x39)^2) + 6) - 2) + exp(-6 * sqrt((x1 -
    x6)^2 + (x18 - x23)^2 + (x35 - x40)^2) + 6) * (exp(-6 * sqrt((x1 - x6)^2 +
    (x18 - x23)^2 + (x35 - x40)^2) + 6) - 2) + exp(-6 * sqrt((x1 - x7)^2 + (x18
    - x24)^2 + (x35 - x41)^2) + 6) * (exp(-6 * sqrt((x1 - x7)^2 + (x18 - x24)^
    2 + (x35 - x41)^2) + 6) - 2) + exp(-6 * sqrt((x1 - x8)^2 + (x18 - x25)^2 +
    (x35 - x42)^2) + 6) * (exp(-6 * sqrt((x1 - x8)^2 + (x18 - x25)^2 + (x35 -
    x42)^2) + 6) - 2) + exp(-6 * sqrt((x1 - x9)^2 + (x18 - x26)^2 + (x35 - x43)
    ^2) + 6) * (exp(-6 * sqrt((x1 - x9)^2 + (x18 - x26)^2 + (x35 - x43)^2) + 6)
    - 2) + exp(-6 * sqrt((x1 - x10)^2 + (x18 - x27)^2 + (x35 - x44)^2) + 6) *
    (exp(-6 * sqrt((x1 - x10)^2 + (x18 - x27)^2 + (x35 - x44)^2) + 6) - 2) +
    exp(-6 * sqrt((x1 - x11)^2 + (x18 - x28)^2 + (x35 - x45)^2) + 6) * (exp(-6
    * sqrt((x1 - x11)^2 + (x18 - x28)^2 + (x35 - x45)^2) + 6) - 2) + exp(-6 *
    sqrt((x1 - x12)^2 + (x18 - x29)^2 + (x35 - x46)^2) + 6) * (exp(-6 * sqrt((
    x1 - x12)^2 + (x18 - x29)^2 + (x35 - x46)^2) + 6) - 2) + exp(-6 * sqrt((x1
    - x13)^2 + (x18 - x30)^2 + (x35 - x47)^2) + 6) * (exp(-6 * sqrt((x1 - x13)
    ^2 + (x18 - x30)^2 + (x35 - x47)^2) + 6) - 2) + exp(-6 * sqrt((x1 - x14)^2
    + (x18 - x31)^2 + (x35 - x48)^2) + 6) * (exp(-6 * sqrt((x1 - x14)^2 + (x18
    - x31)^2 + (x35 - x48)^2) + 6) - 2) + exp(-6 * sqrt((x1 - x15)^2 + (x18 -
    x32)^2 + (x35 - x49)^2) + 6) * (exp(-6 * sqrt((x1 - x15)^2 + (x18 - x32)^2
    + (x35 - x49)^2) + 6) - 2) + exp(-6 * sqrt((x1 - x16)^2 + (x18 - x33)^2 +
    (x35 - x50)^2) + 6) * (exp(-6 * sqrt((x1 - x16)^2 + (x18 - x33)^2 + (x35 -
    x50)^2) + 6) - 2) + exp(-6 * sqrt((x1 - x17)^2 + (x18 - x34)^2 + (x35 - x51)
    ^2) + 6) * (exp(-6 * sqrt((x1 - x17)^2 + (x18 - x34)^2 + (x35 - x51)^2) + 6)
    - 2) + exp(-6 * sqrt((x2 - x3)^2 + (x19 - x20)^2 + (x36 - x37)^2) + 6) * (
    exp(-6 * sqrt((x2 - x3)^2 + (x19 - x20)^2 + (x36 - x37)^2) + 6) - 2) + exp(
    -6 * sqrt((x2 - x4)^2 + (x19 - x21)^2 + (x36 - x38)^2) + 6) * (exp(-6 *
    sqrt((x2 - x4)^2 + (x19 - x21)^2 + (x36 - x38)^2) + 6) - 2) + exp(-6 *
    sqrt((x2 - x5)^2 + (x19 - x22)^2 + (x36 - x39)^2) + 6) * (exp(-6 * sqrt((x2
    - x5)^2 + (x19 - x22)^2 + (x36 - x39)^2) + 6) - 2) + exp(-6 * sqrt((x2 -
    x6)^2 + (x19 - x23)^2 + (x36 - x40)^2) + 6) * (exp(-6 * sqrt((x2 - x6)^2 +
    (x19 - x23)^2 + (x36 - x40)^2) + 6) - 2) + exp(-6 * sqrt((x2 - x7)^2 + (x19
    - x24)^2 + (x36 - x41)^2) + 6) * (exp(-6 * sqrt((x2 - x7)^2 + (x19 - x24)^
    2 + (x36 - x41)^2) + 6) - 2) + exp(-6 * sqrt((x2 - x8)^2 + (x19 - x25)^2 +
    (x36 - x42)^2) + 6) * (exp(-6 * sqrt((x2 - x8)^2 + (x19 - x25)^2 + (x36 -
    x42)^2) + 6) - 2) + exp(-6 * sqrt((x2 - x9)^2 + (x19 - x26)^2 + (x36 - x43)
    ^2) + 6) * (exp(-6 * sqrt((x2 - x9)^2 + (x19 - x26)^2 + (x36 - x43)^2) + 6)
    - 2) + exp(-6 * sqrt((x2 - x10)^2 + (x19 - x27)^2 + (x36 - x44)^2) + 6) *
    (exp(-6 * sqrt((x2 - x10)^2 + (x19 - x27)^2 + (x36 - x44)^2) + 6) - 2) +
    exp(-6 * sqrt((x2 - x11)^2 + (x19 - x28)^2 + (x36 - x45)^2) + 6) * (exp(-6
    * sqrt((x2 - x11)^2 + (x19 - x28)^2 + (x36 - x45)^2) + 6) - 2) + exp(-6 *
    sqrt((x2 - x12)^2 + (x19 - x29)^2 + (x36 - x46)^2) + 6) * (exp(-6 * sqrt((
    x2 - x12)^2 + (x19 - x29)^2 + (x36 - x46)^2) + 6) - 2) + exp(-6 * sqrt((x2
    - x13)^2 + (x19 - x30)^2 + (x36 - x47)^2) + 6) * (exp(-6 * sqrt((x2 - x13)
    ^2 + (x19 - x30)^2 + (x36 - x47)^2) + 6) - 2) + exp(-6 * sqrt((x2 - x14)^2
    + (x19 - x31)^2 + (x36 - x48)^2) + 6) * (exp(-6 * sqrt((x2 - x14)^2 + (x19
    - x31)^2 + (x36 - x48)^2) + 6) - 2) + exp(-6 * sqrt((x2 - x15)^2 + (x19 -
    x32)^2 + (x36 - x49)^2) + 6) * (exp(-6 * sqrt((x2 - x15)^2 + (x19 - x32)^2
    + (x36 - x49)^2) + 6) - 2) + exp(-6 * sqrt((x2 - x16)^2 + (x19 - x33)^2 +
    (x36 - x50)^2) + 6) * (exp(-6 * sqrt((x2 - x16)^2 + (x19 - x33)^2 + (x36 -
    x50)^2) + 6) - 2) + exp(-6 * sqrt((x2 - x17)^2 + (x19 - x34)^2 + (x36 - x51)
    ^2) + 6) * (exp(-6 * sqrt((x2 - x17)^2 + (x19 - x34)^2 + (x36 - x51)^2) + 6)
    - 2) + exp(-6 * sqrt((x3 - x4)^2 + (x20 - x21)^2 + (x37 - x38)^2) + 6) * (
    exp(-6 * sqrt((x3 - x4)^2 + (x20 - x21)^2 + (x37 - x38)^2) + 6) - 2) + exp(
    -6 * sqrt((x3 - x5)^2 + (x20 - x22)^2 + (x37 - x39)^2) + 6) * (exp(-6 *
    sqrt((x3 - x5)^2 + (x20 - x22)^2 + (x37 - x39)^2) + 6) - 2) + exp(-6 *
    sqrt((x3 - x6)^2 + (x20 - x23)^2 + (x37 - x40)^2) + 6) * (exp(-6 * sqrt((x3
    - x6)^2 + (x20 - x23)^2 + (x37 - x40)^2) + 6) - 2) + exp(-6 * sqrt((x3 -
    x7)^2 + (x20 - x24)^2 + (x37 - x41)^2) + 6) * (exp(-6 * sqrt((x3 - x7)^2 +
    (x20 - x24)^2 + (x37 - x41)^2) + 6) - 2) + exp(-6 * sqrt((x3 - x8)^2 + (x20
    - x25)^2 + (x37 - x42)^2) + 6) * (exp(-6 * sqrt((x3 - x8)^2 + (x20 - x25)^
    2 + (x37 - x42)^2) + 6) - 2) + exp(-6 * sqrt((x3 - x9)^2 + (x20 - x26)^2 +
    (x37 - x43)^2) + 6) * (exp(-6 * sqrt((x3 - x9)^2 + (x20 - x26)^2 + (x37 -
    x43)^2) + 6) - 2) + exp(-6 * sqrt((x3 - x10)^2 + (x20 - x27)^2 + (x37 - x44)
    ^2) + 6) * (exp(-6 * sqrt((x3 - x10)^2 + (x20 - x27)^2 + (x37 - x44)^2) + 6)
    - 2) + exp(-6 * sqrt((x3 - x11)^2 + (x20 - x28)^2 + (x37 - x45)^2) + 6) *
    (exp(-6 * sqrt((x3 - x11)^2 + (x20 - x28)^2 + (x37 - x45)^2) + 6) - 2) +
    exp(-6 * sqrt((x3 - x12)^2 + (x20 - x29)^2 + (x37 - x46)^2) + 6) * (exp(-6
    * sqrt((x3 - x12)^2 + (x20 - x29)^2 + (x37 - x46)^2) + 6) - 2) + exp(-6 *
    sqrt((x3 - x13)^2 + (x20 - x30)^2 + (x37 - x47)^2) + 6) * (exp(-6 * sqrt((
    x3 - x13)^2 + (x20 - x30)^2 + (x37 - x47)^2) + 6) - 2) + exp(-6 * sqrt((x3
    - x14)^2 + (x20 - x31)^2 + (x37 - x48)^2) + 6) * (exp(-6 * sqrt((x3 - x14)
    ^2 + (x20 - x31)^2 + (x37 - x48)^2) + 6) - 2) + exp(-6 * sqrt((x3 - x15)^2
    + (x20 - x32)^2 + (x37 - x49)^2) + 6) * (exp(-6 * sqrt((x3 - x15)^2 + (x20
    - x32)^2 + (x37 - x49)^2) + 6) - 2) + exp(-6 * sqrt((x3 - x16)^2 + (x20 -
    x33)^2 + (x37 - x50)^2) + 6) * (exp(-6 * sqrt((x3 - x16)^2 + (x20 - x33)^2
    + (x37 - x50)^2) + 6) - 2) + exp(-6 * sqrt((x3 - x17)^2 + (x20 - x34)^2 +
    (x37 - x51)^2) + 6) * (exp(-6 * sqrt((x3 - x17)^2 + (x20 - x34)^2 + (x37 -
    x51)^2) + 6) - 2) + exp(-6 * sqrt((x4 - x5)^2 + (x21 - x22)^2 + (x38 - x39)
    ^2) + 6) * (exp(-6 * sqrt((x4 - x5)^2 + (x21 - x22)^2 + (x38 - x39)^2) + 6)
    - 2) + exp(-6 * sqrt((x4 - x6)^2 + (x21 - x23)^2 + (x38 - x40)^2) + 6) * (
    exp(-6 * sqrt((x4 - x6)^2 + (x21 - x23)^2 + (x38 - x40)^2) + 6) - 2) + exp(
    -6 * sqrt((x4 - x7)^2 + (x21 - x24)^2 + (x38 - x41)^2) + 6) * (exp(-6 *
    sqrt((x4 - x7)^2 + (x21 - x24)^2 + (x38 - x41)^2) + 6) - 2) + exp(-6 *
    sqrt((x4 - x8)^2 + (x21 - x25)^2 + (x38 - x42)^2) + 6) * (exp(-6 * sqrt((x4
    - x8)^2 + (x21 - x25)^2 + (x38 - x42)^2) + 6) - 2) + exp(-6 * sqrt((x4 -
    x9)^2 + (x21 - x26)^2 + (x38 - x43)^2) + 6) * (exp(-6 * sqrt((x4 - x9)^2 +
    (x21 - x26)^2 + (x38 - x43)^2) + 6) - 2) + exp(-6 * sqrt((x4 - x10)^2 + (
    x21 - x27)^2 + (x38 - x44)^2) + 6) * (exp(-6 * sqrt((x4 - x10)^2 + (x21 -
    x27)^2 + (x38 - x44)^2) + 6) - 2) + exp(-6 * sqrt((x4 - x11)^2 + (x21 - x28)
    ^2 + (x38 - x45)^2) + 6) * (exp(-6 * sqrt((x4 - x11)^2 + (x21 - x28)^2 + (
    x38 - x45)^2) + 6) - 2) + exp(-6 * sqrt((x4 - x12)^2 + (x21 - x29)^2 + (x38
    - x46)^2) + 6) * (exp(-6 * sqrt((x4 - x12)^2 + (x21 - x29)^2 + (x38 - x46)
    ^2) + 6) - 2) + exp(-6 * sqrt((x4 - x13)^2 + (x21 - x30)^2 + (x38 - x47)^2)
    + 6) * (exp(-6 * sqrt((x4 - x13)^2 + (x21 - x30)^2 + (x38 - x47)^2) + 6)
    - 2) + exp(-6 * sqrt((x4 - x14)^2 + (x21 - x31)^2 + (x38 - x48)^2) + 6) *
    (exp(-6 * sqrt((x4 - x14)^2 + (x21 - x31)^2 + (x38 - x48)^2) + 6) - 2) +
    exp(-6 * sqrt((x4 - x15)^2 + (x21 - x32)^2 + (x38 - x49)^2) + 6) * (exp(-6
    * sqrt((x4 - x15)^2 + (x21 - x32)^2 + (x38 - x49)^2) + 6) - 2) + exp(-6 *
    sqrt((x4 - x16)^2 + (x21 - x33)^2 + (x38 - x50)^2) + 6) * (exp(-6 * sqrt((
    x4 - x16)^2 + (x21 - x33)^2 + (x38 - x50)^2) + 6) - 2) + exp(-6 * sqrt((x4
    - x17)^2 + (x21 - x34)^2 + (x38 - x51)^2) + 6) * (exp(-6 * sqrt((x4 - x17)
    ^2 + (x21 - x34)^2 + (x38 - x51)^2) + 6) - 2) + exp(-6 * sqrt((x5 - x6)^2
    + (x22 - x23)^2 + (x39 - x40)^2) + 6) * (exp(-6 * sqrt((x5 - x6)^2 + (x22
    - x23)^2 + (x39 - x40)^2) + 6) - 2) + exp(-6 * sqrt((x5 - x7)^2 + (x22 -
    x24)^2 + (x39 - x41)^2) + 6) * (exp(-6 * sqrt((x5 - x7)^2 + (x22 - x24)^2
    + (x39 - x41)^2) + 6) - 2) + exp(-6 * sqrt((x5 - x8)^2 + (x22 - x25)^2 + (
    x39 - x42)^2) + 6) * (exp(-6 * sqrt((x5 - x8)^2 + (x22 - x25)^2 + (x39 -
    x42)^2) + 6) - 2) + exp(-6 * sqrt((x5 - x9)^2 + (x22 - x26)^2 + (x39 - x43)
    ^2) + 6) * (exp(-6 * sqrt((x5 - x9)^2 + (x22 - x26)^2 + (x39 - x43)^2) + 6)
    - 2) + exp(-6 * sqrt((x5 - x10)^2 + (x22 - x27)^2 + (x39 - x44)^2) + 6) *
    (exp(-6 * sqrt((x5 - x10)^2 + (x22 - x27)^2 + (x39 - x44)^2) + 6) - 2) +
    exp(-6 * sqrt((x5 - x11)^2 + (x22 - x28)^2 + (x39 - x45)^2) + 6) * (exp(-6
    * sqrt((x5 - x11)^2 + (x22 - x28)^2 + (x39 - x45)^2) + 6) - 2) + exp(-6 *
    sqrt((x5 - x12)^2 + (x22 - x29)^2 + (x39 - x46)^2) + 6) * (exp(-6 * sqrt((
    x5 - x12)^2 + (x22 - x29)^2 + (x39 - x46)^2) + 6) - 2) + exp(-6 * sqrt((x5
    - x13)^2 + (x22 - x30)^2 + (x39 - x47)^2) + 6) * (exp(-6 * sqrt((x5 - x13)
    ^2 + (x22 - x30)^2 + (x39 - x47)^2) + 6) - 2) + exp(-6 * sqrt((x5 - x14)^2
    + (x22 - x31)^2 + (x39 - x48)^2) + 6) * (exp(-6 * sqrt((x5 - x14)^2 + (x22
    - x31)^2 + (x39 - x48)^2) + 6) - 2) + exp(-6 * sqrt((x5 - x15)^2 + (x22 -
    x32)^2 + (x39 - x49)^2) + 6) * (exp(-6 * sqrt((x5 - x15)^2 + (x22 - x32)^2
    + (x39 - x49)^2) + 6) - 2) + exp(-6 * sqrt((x5 - x16)^2 + (x22 - x33)^2 +
    (x39 - x50)^2) + 6) * (exp(-6 * sqrt((x5 - x16)^2 + (x22 - x33)^2 + (x39 -
    x50)^2) + 6) - 2) + exp(-6 * sqrt((x5 - x17)^2 + (x22 - x34)^2 + (x39 - x51)
    ^2) + 6) * (exp(-6 * sqrt((x5 - x17)^2 + (x22 - x34)^2 + (x39 - x51)^2) + 6)
    - 2) + exp(-6 * sqrt((x6 - x7)^2 + (x23 - x24)^2 + (x40 - x41)^2) + 6) * (
    exp(-6 * sqrt((x6 - x7)^2 + (x23 - x24)^2 + (x40 - x41)^2) + 6) - 2) + exp(
    -6 * sqrt((x6 - x8)^2 + (x23 - x25)^2 + (x40 - x42)^2) + 6) * (exp(-6 *
    sqrt((x6 - x8)^2 + (x23 - x25)^2 + (x40 - x42)^2) + 6) - 2) + exp(-6 *
    sqrt((x6 - x9)^2 + (x23 - x26)^2 + (x40 - x43)^2) + 6) * (exp(-6 * sqrt((x6
    - x9)^2 + (x23 - x26)^2 + (x40 - x43)^2) + 6) - 2) + exp(-6 * sqrt((x6 -
    x10)^2 + (x23 - x27)^2 + (x40 - x44)^2) + 6) * (exp(-6 * sqrt((x6 - x10)^2
    + (x23 - x27)^2 + (x40 - x44)^2) + 6) - 2) + exp(-6 * sqrt((x6 - x11)^2 +
    (x23 - x28)^2 + (x40 - x45)^2) + 6) * (exp(-6 * sqrt((x6 - x11)^2 + (x23 -
    x28)^2 + (x40 - x45)^2) + 6) - 2) + exp(-6 * sqrt((x6 - x12)^2 + (x23 - x29)
    ^2 + (x40 - x46)^2) + 6) * (exp(-6 * sqrt((x6 - x12)^2 + (x23 - x29)^2 + (
    x40 - x46)^2) + 6) - 2) + exp(-6 * sqrt((x6 - x13)^2 + (x23 - x30)^2 + (x40
    - x47)^2) + 6) * (exp(-6 * sqrt((x6 - x13)^2 + (x23 - x30)^2 + (x40 - x47)
    ^2) + 6) - 2) + exp(-6 * sqrt((x6 - x14)^2 + (x23 - x31)^2 + (x40 - x48)^2)
    + 6) * (exp(-6 * sqrt((x6 - x14)^2 + (x23 - x31)^2 + (x40 - x48)^2) + 6)
    - 2) + exp(-6 * sqrt((x6 - x15)^2 + (x23 - x32)^2 + (x40 - x49)^2) + 6) *
    (exp(-6 * sqrt((x6 - x15)^2 + (x23 - x32)^2 + (x40 - x49)^2) + 6) - 2) +
    exp(-6 * sqrt((x6 - x16)^2 + (x23 - x33)^2 + (x40 - x50)^2) + 6) * (exp(-6
    * sqrt((x6 - x16)^2 + (x23 - x33)^2 + (x40 - x50)^2) + 6) - 2) + exp(-6 *
    sqrt((x6 - x17)^2 + (x23 - x34)^2 + (x40 - x51)^2) + 6) * (exp(-6 * sqrt((
    x6 - x17)^2 + (x23 - x34)^2 + (x40 - x51)^2) + 6) - 2) + exp(-6 * sqrt((x7
    - x8)^2 + (x24 - x25)^2 + (x41 - x42)^2) + 6) * (exp(-6 * sqrt((x7 - x8)^2
    + (x24 - x25)^2 + (x41 - x42)^2) + 6) - 2) + exp(-6 * sqrt((x7 - x9)^2 + (
    x24 - x26)^2 + (x41 - x43)^2) + 6) * (exp(-6 * sqrt((x7 - x9)^2 + (x24 -
    x26)^2 + (x41 - x43)^2) + 6) - 2) + exp(-6 * sqrt((x7 - x10)^2 + (x24 - x27)
    ^2 + (x41 - x44)^2) + 6) * (exp(-6 * sqrt((x7 - x10)^2 + (x24 - x27)^2 + (
    x41 - x44)^2) + 6) - 2) + exp(-6 * sqrt((x7 - x11)^2 + (x24 - x28)^2 + (x41
    - x45)^2) + 6) * (exp(-6 * sqrt((x7 - x11)^2 + (x24 - x28)^2 + (x41 - x45)
    ^2) + 6) - 2) + exp(-6 * sqrt((x7 - x12)^2 + (x24 - x29)^2 + (x41 - x46)^2)
    + 6) * (exp(-6 * sqrt((x7 - x12)^2 + (x24 - x29)^2 + (x41 - x46)^2) + 6)
    - 2) + exp(-6 * sqrt((x7 - x13)^2 + (x24 - x30)^2 + (x41 - x47)^2) + 6) *
    (exp(-6 * sqrt((x7 - x13)^2 + (x24 - x30)^2 + (x41 - x47)^2) + 6) - 2) +
    exp(-6 * sqrt((x7 - x14)^2 + (x24 - x31)^2 + (x41 - x48)^2) + 6) * (exp(-6
    * sqrt((x7 - x14)^2 + (x24 - x31)^2 + (x41 - x48)^2) + 6) - 2) + exp(-6 *
    sqrt((x7 - x15)^2 + (x24 - x32)^2 + (x41 - x49)^2) + 6) * (exp(-6 * sqrt((
    x7 - x15)^2 + (x24 - x32)^2 + (x41 - x49)^2) + 6) - 2) + exp(-6 * sqrt((x7
    - x16)^2 + (x24 - x33)^2 + (x41 - x50)^2) + 6) * (exp(-6 * sqrt((x7 - x16)
    ^2 + (x24 - x33)^2 + (x41 - x50)^2) + 6) - 2) + exp(-6 * sqrt((x7 - x17)^2
    + (x24 - x34)^2 + (x41 - x51)^2) + 6) * (exp(-6 * sqrt((x7 - x17)^2 + (x24
    - x34)^2 + (x41 - x51)^2) + 6) - 2) + exp(-6 * sqrt((x8 - x9)^2 + (x25 -
    x26)^2 + (x42 - x43)^2) + 6) * (exp(-6 * sqrt((x8 - x9)^2 + (x25 - x26)^2
    + (x42 - x43)^2) + 6) - 2) + exp(-6 * sqrt((x8 - x10)^2 + (x25 - x27)^2 +
    (x42 - x44)^2) + 6) * (exp(-6 * sqrt((x8 - x10)^2 + (x25 - x27)^2 + (x42 -
    x44)^2) + 6) - 2) + exp(-6 * sqrt((x8 - x11)^2 + (x25 - x28)^2 + (x42 - x45)
    ^2) + 6) * (exp(-6 * sqrt((x8 - x11)^2 + (x25 - x28)^2 + (x42 - x45)^2) + 6)
    - 2) + exp(-6 * sqrt((x8 - x12)^2 + (x25 - x29)^2 + (x42 - x46)^2) + 6) *
    (exp(-6 * sqrt((x8 - x12)^2 + (x25 - x29)^2 + (x42 - x46)^2) + 6) - 2) +
    exp(-6 * sqrt((x8 - x13)^2 + (x25 - x30)^2 + (x42 - x47)^2) + 6) * (exp(-6
    * sqrt((x8 - x13)^2 + (x25 - x30)^2 + (x42 - x47)^2) + 6) - 2) + exp(-6 *
    sqrt((x8 - x14)^2 + (x25 - x31)^2 + (x42 - x48)^2) + 6) * (exp(-6 * sqrt((
    x8 - x14)^2 + (x25 - x31)^2 + (x42 - x48)^2) + 6) - 2) + exp(-6 * sqrt((x8
    - x15)^2 + (x25 - x32)^2 + (x42 - x49)^2) + 6) * (exp(-6 * sqrt((x8 - x15)
    ^2 + (x25 - x32)^2 + (x42 - x49)^2) + 6) - 2) + exp(-6 * sqrt((x8 - x16)^2
    + (x25 - x33)^2 + (x42 - x50)^2) + 6) * (exp(-6 * sqrt((x8 - x16)^2 + (x25
    - x33)^2 + (x42 - x50)^2) + 6) - 2) + exp(-6 * sqrt((x8 - x17)^2 + (x25 -
    x34)^2 + (x42 - x51)^2) + 6) * (exp(-6 * sqrt((x8 - x17)^2 + (x25 - x34)^2
    + (x42 - x51)^2) + 6) - 2) + exp(-6 * sqrt((x9 - x10)^2 + (x26 - x27)^2 +
    (x43 - x44)^2) + 6) * (exp(-6 * sqrt((x9 - x10)^2 + (x26 - x27)^2 + (x43 -
    x44)^2) + 6) - 2) + exp(-6 * sqrt((x9 - x11)^2 + (x26 - x28)^2 + (x43 - x45)
    ^2) + 6) * (exp(-6 * sqrt((x9 - x11)^2 + (x26 - x28)^2 + (x43 - x45)^2) + 6)
    - 2) + exp(-6 * sqrt((x9 - x12)^2 + (x26 - x29)^2 + (x43 - x46)^2) + 6) *
    (exp(-6 * sqrt((x9 - x12)^2 + (x26 - x29)^2 + (x43 - x46)^2) + 6) - 2) +
    exp(-6 * sqrt((x9 - x13)^2 + (x26 - x30)^2 + (x43 - x47)^2) + 6) * (exp(-6
    * sqrt((x9 - x13)^2 + (x26 - x30)^2 + (x43 - x47)^2) + 6) - 2) + exp(-6 *
    sqrt((x9 - x14)^2 + (x26 - x31)^2 + (x43 - x48)^2) + 6) * (exp(-6 * sqrt((
    x9 - x14)^2 + (x26 - x31)^2 + (x43 - x48)^2) + 6) - 2) + exp(-6 * sqrt((x9
    - x15)^2 + (x26 - x32)^2 + (x43 - x49)^2) + 6) * (exp(-6 * sqrt((x9 - x15)
    ^2 + (x26 - x32)^2 + (x43 - x49)^2) + 6) - 2) + exp(-6 * sqrt((x9 - x16)^2
    + (x26 - x33)^2 + (x43 - x50)^2) + 6) * (exp(-6 * sqrt((x9 - x16)^2 + (x26
    - x33)^2 + (x43 - x50)^2) + 6) - 2) + exp(-6 * sqrt((x9 - x17)^2 + (x26 -
    x34)^2 + (x43 - x51)^2) + 6) * (exp(-6 * sqrt((x9 - x17)^2 + (x26 - x34)^2
    + (x43 - x51)^2) + 6) - 2) + exp(-6 * sqrt((x10 - x11)^2 + (x27 - x28)^2
    + (x44 - x45)^2) + 6) * (exp(-6 * sqrt((x10 - x11)^2 + (x27 - x28)^2 + (
    x44 - x45)^2) + 6) - 2) + exp(-6 * sqrt((x10 - x12)^2 + (x27 - x29)^2 + (
    x44 - x46)^2) + 6) * (exp(-6 * sqrt((x10 - x12)^2 + (x27 - x29)^2 + (x44 -
    x46)^2) + 6) - 2) + exp(-6 * sqrt((x10 - x13)^2 + (x27 - x30)^2 + (x44 -
    x47)^2) + 6) * (exp(-6 * sqrt((x10 - x13)^2 + (x27 - x30)^2 + (x44 - x47)^2)
    + 6) - 2) + exp(-6 * sqrt((x10 - x14)^2 + (x27 - x31)^2 + (x44 - x48)^2)
    + 6) * (exp(-6 * sqrt((x10 - x14)^2 + (x27 - x31)^2 + (x44 - x48)^2) + 6)
    - 2) + exp(-6 * sqrt((x10 - x15)^2 + (x27 - x32)^2 + (x44 - x49)^2) + 6)
    * (exp(-6 * sqrt((x10 - x15)^2 + (x27 - x32)^2 + (x44 - x49)^2) + 6) - 2)
    + exp(-6 * sqrt((x10 - x16)^2 + (x27 - x33)^2 + (x44 - x50)^2) + 6) * (
    exp(-6 * sqrt((x10 - x16)^2 + (x27 - x33)^2 + (x44 - x50)^2) + 6) - 2) +
    exp(-6 * sqrt((x10 - x17)^2 + (x27 - x34)^2 + (x44 - x51)^2) + 6) * (exp(-6
    * sqrt((x10 - x17)^2 + (x27 - x34)^2 + (x44 - x51)^2) + 6) - 2) + exp(-6
    * sqrt((x11 - x12)^2 + (x28 - x29)^2 + (x45 - x46)^2) + 6) * (exp(-6 *
    sqrt((x11 - x12)^2 + (x28 - x29)^2 + (x45 - x46)^2) + 6) - 2) + exp(-6 *
    sqrt((x11 - x13)^2 + (x28 - x30)^2 + (x45 - x47)^2) + 6) * (exp(-6 * sqrt((
    x11 - x13)^2 + (x28 - x30)^2 + (x45 - x47)^2) + 6) - 2) + exp(-6 * sqrt((
    x11 - x14)^2 + (x28 - x31)^2 + (x45 - x48)^2) + 6) * (exp(-6 * sqrt((x11 -
    x14)^2 + (x28 - x31)^2 + (x45 - x48)^2) + 6) - 2) + exp(-6 * sqrt((x11 -
    x15)^2 + (x28 - x32)^2 + (x45 - x49)^2) + 6) * (exp(-6 * sqrt((x11 - x15)^2
    + (x28 - x32)^2 + (x45 - x49)^2) + 6) - 2) + exp(-6 * sqrt((x11 - x16)^2
    + (x28 - x33)^2 + (x45 - x50)^2) + 6) * (exp(-6 * sqrt((x11 - x16)^2 + (
    x28 - x33)^2 + (x45 - x50)^2) + 6) - 2) + exp(-6 * sqrt((x11 - x17)^2 + (
    x28 - x34)^2 + (x45 - x51)^2) + 6) * (exp(-6 * sqrt((x11 - x17)^2 + (x28 -
    x34)^2 + (x45 - x51)^2) + 6) - 2) + exp(-6 * sqrt((x12 - x13)^2 + (x29 -
    x30)^2 + (x46 - x47)^2) + 6) * (exp(-6 * sqrt((x12 - x13)^2 + (x29 - x30)^2
    + (x46 - x47)^2) + 6) - 2) + exp(-6 * sqrt((x12 - x14)^2 + (x29 - x31)^2
    + (x46 - x48)^2) + 6) * (exp(-6 * sqrt((x12 - x14)^2 + (x29 - x31)^2 + (
    x46 - x48)^2) + 6) - 2) + exp(-6 * sqrt((x12 - x15)^2 + (x29 - x32)^2 + (
    x46 - x49)^2) + 6) * (exp(-6 * sqrt((x12 - x15)^2 + (x29 - x32)^2 + (x46 -
    x49)^2) + 6) - 2) + exp(-6 * sqrt((x12 - x16)^2 + (x29 - x33)^2 + (x46 -
    x50)^2) + 6) * (exp(-6 * sqrt((x12 - x16)^2 + (x29 - x33)^2 + (x46 - x50)^2)
    + 6) - 2) + exp(-6 * sqrt((x12 - x17)^2 + (x29 - x34)^2 + (x46 - x51)^2)
    + 6) * (exp(-6 * sqrt((x12 - x17)^2 + (x29 - x34)^2 + (x46 - x51)^2) + 6)
    - 2) + exp(-6 * sqrt((x13 - x14)^2 + (x30 - x31)^2 + (x47 - x48)^2) + 6)
    * (exp(-6 * sqrt((x13 - x14)^2 + (x30 - x31)^2 + (x47 - x48)^2) + 6) - 2)
    + exp(-6 * sqrt((x13 - x15)^2 + (x30 - x32)^2 + (x47 - x49)^2) + 6) * (
    exp(-6 * sqrt((x13 - x15)^2 + (x30 - x32)^2 + (x47 - x49)^2) + 6) - 2) +
    exp(-6 * sqrt((x13 - x16)^2 + (x30 - x33)^2 + (x47 - x50)^2) + 6) * (exp(-6
    * sqrt((x13 - x16)^2 + (x30 - x33)^2 + (x47 - x50)^2) + 6) - 2) + exp(-6
    * sqrt((x13 - x17)^2 + (x30 - x34)^2 + (x47 - x51)^2) + 6) * (exp(-6 *
    sqrt((x13 - x17)^2 + (x30 - x34)^2 + (x47 - x51)^2) + 6) - 2) + exp(-6 *
    sqrt((x14 - x15)^2 + (x31 - x32)^2 + (x48 - x49)^2) + 6) * (exp(-6 * sqrt((
    x14 - x15)^2 + (x31 - x32)^2 + (x48 - x49)^2) + 6) - 2) + exp(-6 * sqrt((
    x14 - x16)^2 + (x31 - x33)^2 + (x48 - x50)^2) + 6) * (exp(-6 * sqrt((x14 -
    x16)^2 + (x31 - x33)^2 + (x48 - x50)^2) + 6) - 2) + exp(-6 * sqrt((x14 -
    x17)^2 + (x31 - x34)^2 + (x48 - x51)^2) + 6) * (exp(-6 * sqrt((x14 - x17)^2
    + (x31 - x34)^2 + (x48 - x51)^2) + 6) - 2) + exp(-6 * sqrt((x15 - x16)^2
    + (x32 - x33)^2 + (x49 - x50)^2) + 6) * (exp(-6 * sqrt((x15 - x16)^2 + (
    x32 - x33)^2 + (x49 - x50)^2) + 6) - 2) + exp(-6 * sqrt((x15 - x17)^2 + (
    x32 - x34)^2 + (x49 - x51)^2) + 6) * (exp(-6 * sqrt((x15 - x17)^2 + (x32 -
    x34)^2 + (x49 - x51)^2) + 6) - 2) + exp(-6 * sqrt((x16 - x17)^2 + (x33 -
    x34)^2 + (x50 - x51)^2) + 6) * (exp(-6 * sqrt((x16 - x17)^2 + (x33 - x34)^2
    + (x50 - x51)^2) + 6) - 2))

@NLconstraint(m, e1, (x1 - x2)^2 + (x18 - x19)^2 + (x35 - x36)^2
    >= 0.32159900740899994)
@NLconstraint(m, e2, (x1 - x3)^2 + (x18 - x20)^2 + (x35 - x37)^2
    >= 0.32159900740899994)
@NLconstraint(m, e3, (x1 - x4)^2 + (x18 - x21)^2 + (x35 - x38)^2
    >= 0.32159900740899994)
@NLconstraint(m, e4, (x1 - x5)^2 + (x18 - x22)^2 + (x35 - x39)^2
    >= 0.32159900740899994)
@NLconstraint(m, e5, (x1 - x6)^2 + (x18 - x23)^2 + (x35 - x40)^2
    >= 0.32159900740899994)
@NLconstraint(m, e6, (x1 - x7)^2 + (x18 - x24)^2 + (x35 - x41)^2
    >= 0.32159900740899994)
@NLconstraint(m, e7, (x1 - x8)^2 + (x18 - x25)^2 + (x35 - x42)^2
    >= 0.32159900740899994)
@NLconstraint(m, e8, (x1 - x9)^2 + (x18 - x26)^2 + (x35 - x43)^2
    >= 0.32159900740899994)
@NLconstraint(m, e9, (x1 - x10)^2 + (x18 - x27)^2 + (x35 - x44)^2
    >= 0.32159900740899994)
@NLconstraint(m, e10, (x1 - x11)^2 + (x18 - x28)^2 + (x35 - x45)^2
    >= 0.32159900740899994)
@NLconstraint(m, e11, (x1 - x12)^2 + (x18 - x29)^2 + (x35 - x46)^2
    >= 0.32159900740899994)
@NLconstraint(m, e12, (x1 - x13)^2 + (x18 - x30)^2 + (x35 - x47)^2
    >= 0.32159900740899994)
@NLconstraint(m, e13, (x1 - x14)^2 + (x18 - x31)^2 + (x35 - x48)^2
    >= 0.32159900740899994)
@NLconstraint(m, e14, (x1 - x15)^2 + (x18 - x32)^2 + (x35 - x49)^2
    >= 0.32159900740899994)
@NLconstraint(m, e15, (x1 - x16)^2 + (x18 - x33)^2 + (x35 - x50)^2
    >= 0.32159900740899994)
@NLconstraint(m, e16, (x1 - x17)^2 + (x18 - x34)^2 + (x35 - x51)^2
    >= 0.32159900740899994)
@NLconstraint(m, e17, (x2 - x3)^2 + (x19 - x20)^2 + (x36 - x37)^2
    >= 0.32159900740899994)
@NLconstraint(m, e18, (x2 - x4)^2 + (x19 - x21)^2 + (x36 - x38)^2
    >= 0.32159900740899994)
@NLconstraint(m, e19, (x2 - x5)^2 + (x19 - x22)^2 + (x36 - x39)^2
    >= 0.32159900740899994)
@NLconstraint(m, e20, (x2 - x6)^2 + (x19 - x23)^2 + (x36 - x40)^2
    >= 0.32159900740899994)
@NLconstraint(m, e21, (x2 - x7)^2 + (x19 - x24)^2 + (x36 - x41)^2
    >= 0.32159900740899994)
@NLconstraint(m, e22, (x2 - x8)^2 + (x19 - x25)^2 + (x36 - x42)^2
    >= 0.32159900740899994)
@NLconstraint(m, e23, (x2 - x9)^2 + (x19 - x26)^2 + (x36 - x43)^2
    >= 0.32159900740899994)
@NLconstraint(m, e24, (x2 - x10)^2 + (x19 - x27)^2 + (x36 - x44)^2
    >= 0.32159900740899994)
@NLconstraint(m, e25, (x2 - x11)^2 + (x19 - x28)^2 + (x36 - x45)^2
    >= 0.32159900740899994)
@NLconstraint(m, e26, (x2 - x12)^2 + (x19 - x29)^2 + (x36 - x46)^2
    >= 0.32159900740899994)
@NLconstraint(m, e27, (x2 - x13)^2 + (x19 - x30)^2 + (x36 - x47)^2
    >= 0.32159900740899994)
@NLconstraint(m, e28, (x2 - x14)^2 + (x19 - x31)^2 + (x36 - x48)^2
    >= 0.32159900740899994)
@NLconstraint(m, e29, (x2 - x15)^2 + (x19 - x32)^2 + (x36 - x49)^2
    >= 0.32159900740899994)
@NLconstraint(m, e30, (x2 - x16)^2 + (x19 - x33)^2 + (x36 - x50)^2
    >= 0.32159900740899994)
@NLconstraint(m, e31, (x2 - x17)^2 + (x19 - x34)^2 + (x36 - x51)^2
    >= 0.32159900740899994)
@NLconstraint(m, e32, (x3 - x4)^2 + (x20 - x21)^2 + (x37 - x38)^2
    >= 0.32159900740899994)
@NLconstraint(m, e33, (x3 - x5)^2 + (x20 - x22)^2 + (x37 - x39)^2
    >= 0.32159900740899994)
@NLconstraint(m, e34, (x3 - x6)^2 + (x20 - x23)^2 + (x37 - x40)^2
    >= 0.32159900740899994)
@NLconstraint(m, e35, (x3 - x7)^2 + (x20 - x24)^2 + (x37 - x41)^2
    >= 0.32159900740899994)
@NLconstraint(m, e36, (x3 - x8)^2 + (x20 - x25)^2 + (x37 - x42)^2
    >= 0.32159900740899994)
@NLconstraint(m, e37, (x3 - x9)^2 + (x20 - x26)^2 + (x37 - x43)^2
    >= 0.32159900740899994)
@NLconstraint(m, e38, (x3 - x10)^2 + (x20 - x27)^2 + (x37 - x44)^2
    >= 0.32159900740899994)
@NLconstraint(m, e39, (x3 - x11)^2 + (x20 - x28)^2 + (x37 - x45)^2
    >= 0.32159900740899994)
@NLconstraint(m, e40, (x3 - x12)^2 + (x20 - x29)^2 + (x37 - x46)^2
    >= 0.32159900740899994)
@NLconstraint(m, e41, (x3 - x13)^2 + (x20 - x30)^2 + (x37 - x47)^2
    >= 0.32159900740899994)
@NLconstraint(m, e42, (x3 - x14)^2 + (x20 - x31)^2 + (x37 - x48)^2
    >= 0.32159900740899994)
@NLconstraint(m, e43, (x3 - x15)^2 + (x20 - x32)^2 + (x37 - x49)^2
    >= 0.32159900740899994)
@NLconstraint(m, e44, (x3 - x16)^2 + (x20 - x33)^2 + (x37 - x50)^2
    >= 0.32159900740899994)
@NLconstraint(m, e45, (x3 - x17)^2 + (x20 - x34)^2 + (x37 - x51)^2
    >= 0.32159900740899994)
@NLconstraint(m, e46, (x4 - x5)^2 + (x21 - x22)^2 + (x38 - x39)^2
    >= 0.32159900740899994)
@NLconstraint(m, e47, (x4 - x6)^2 + (x21 - x23)^2 + (x38 - x40)^2
    >= 0.32159900740899994)
@NLconstraint(m, e48, (x4 - x7)^2 + (x21 - x24)^2 + (x38 - x41)^2
    >= 0.32159900740899994)
@NLconstraint(m, e49, (x4 - x8)^2 + (x21 - x25)^2 + (x38 - x42)^2
    >= 0.32159900740899994)
@NLconstraint(m, e50, (x4 - x9)^2 + (x21 - x26)^2 + (x38 - x43)^2
    >= 0.32159900740899994)
@NLconstraint(m, e51, (x4 - x10)^2 + (x21 - x27)^2 + (x38 - x44)^2
    >= 0.32159900740899994)
@NLconstraint(m, e52, (x4 - x11)^2 + (x21 - x28)^2 + (x38 - x45)^2
    >= 0.32159900740899994)
@NLconstraint(m, e53, (x4 - x12)^2 + (x21 - x29)^2 + (x38 - x46)^2
    >= 0.32159900740899994)
@NLconstraint(m, e54, (x4 - x13)^2 + (x21 - x30)^2 + (x38 - x47)^2
    >= 0.32159900740899994)
@NLconstraint(m, e55, (x4 - x14)^2 + (x21 - x31)^2 + (x38 - x48)^2
    >= 0.32159900740899994)
@NLconstraint(m, e56, (x4 - x15)^2 + (x21 - x32)^2 + (x38 - x49)^2
    >= 0.32159900740899994)
@NLconstraint(m, e57, (x4 - x16)^2 + (x21 - x33)^2 + (x38 - x50)^2
    >= 0.32159900740899994)
@NLconstraint(m, e58, (x4 - x17)^2 + (x21 - x34)^2 + (x38 - x51)^2
    >= 0.32159900740899994)
@NLconstraint(m, e59, (x5 - x6)^2 + (x22 - x23)^2 + (x39 - x40)^2
    >= 0.32159900740899994)
@NLconstraint(m, e60, (x5 - x7)^2 + (x22 - x24)^2 + (x39 - x41)^2
    >= 0.32159900740899994)
@NLconstraint(m, e61, (x5 - x8)^2 + (x22 - x25)^2 + (x39 - x42)^2
    >= 0.32159900740899994)
@NLconstraint(m, e62, (x5 - x9)^2 + (x22 - x26)^2 + (x39 - x43)^2
    >= 0.32159900740899994)
@NLconstraint(m, e63, (x5 - x10)^2 + (x22 - x27)^2 + (x39 - x44)^2
    >= 0.32159900740899994)
@NLconstraint(m, e64, (x5 - x11)^2 + (x22 - x28)^2 + (x39 - x45)^2
    >= 0.32159900740899994)
@NLconstraint(m, e65, (x5 - x12)^2 + (x22 - x29)^2 + (x39 - x46)^2
    >= 0.32159900740899994)
@NLconstraint(m, e66, (x5 - x13)^2 + (x22 - x30)^2 + (x39 - x47)^2
    >= 0.32159900740899994)
@NLconstraint(m, e67, (x5 - x14)^2 + (x22 - x31)^2 + (x39 - x48)^2
    >= 0.32159900740899994)
@NLconstraint(m, e68, (x5 - x15)^2 + (x22 - x32)^2 + (x39 - x49)^2
    >= 0.32159900740899994)
@NLconstraint(m, e69, (x5 - x16)^2 + (x22 - x33)^2 + (x39 - x50)^2
    >= 0.32159900740899994)
@NLconstraint(m, e70, (x5 - x17)^2 + (x22 - x34)^2 + (x39 - x51)^2
    >= 0.32159900740899994)
@NLconstraint(m, e71, (x6 - x7)^2 + (x23 - x24)^2 + (x40 - x41)^2
    >= 0.32159900740899994)
@NLconstraint(m, e72, (x6 - x8)^2 + (x23 - x25)^2 + (x40 - x42)^2
    >= 0.32159900740899994)
@NLconstraint(m, e73, (x6 - x9)^2 + (x23 - x26)^2 + (x40 - x43)^2
    >= 0.32159900740899994)
@NLconstraint(m, e74, (x6 - x10)^2 + (x23 - x27)^2 + (x40 - x44)^2
    >= 0.32159900740899994)
@NLconstraint(m, e75, (x6 - x11)^2 + (x23 - x28)^2 + (x40 - x45)^2
    >= 0.32159900740899994)
@NLconstraint(m, e76, (x6 - x12)^2 + (x23 - x29)^2 + (x40 - x46)^2
    >= 0.32159900740899994)
@NLconstraint(m, e77, (x6 - x13)^2 + (x23 - x30)^2 + (x40 - x47)^2
    >= 0.32159900740899994)
@NLconstraint(m, e78, (x6 - x14)^2 + (x23 - x31)^2 + (x40 - x48)^2
    >= 0.32159900740899994)
@NLconstraint(m, e79, (x6 - x15)^2 + (x23 - x32)^2 + (x40 - x49)^2
    >= 0.32159900740899994)
@NLconstraint(m, e80, (x6 - x16)^2 + (x23 - x33)^2 + (x40 - x50)^2
    >= 0.32159900740899994)
@NLconstraint(m, e81, (x6 - x17)^2 + (x23 - x34)^2 + (x40 - x51)^2
    >= 0.32159900740899994)
@NLconstraint(m, e82, (x7 - x8)^2 + (x24 - x25)^2 + (x41 - x42)^2
    >= 0.32159900740899994)
@NLconstraint(m, e83, (x7 - x9)^2 + (x24 - x26)^2 + (x41 - x43)^2
    >= 0.32159900740899994)
@NLconstraint(m, e84, (x7 - x10)^2 + (x24 - x27)^2 + (x41 - x44)^2
    >= 0.32159900740899994)
@NLconstraint(m, e85, (x7 - x11)^2 + (x24 - x28)^2 + (x41 - x45)^2
    >= 0.32159900740899994)
@NLconstraint(m, e86, (x7 - x12)^2 + (x24 - x29)^2 + (x41 - x46)^2
    >= 0.32159900740899994)
@NLconstraint(m, e87, (x7 - x13)^2 + (x24 - x30)^2 + (x41 - x47)^2
    >= 0.32159900740899994)
@NLconstraint(m, e88, (x7 - x14)^2 + (x24 - x31)^2 + (x41 - x48)^2
    >= 0.32159900740899994)
@NLconstraint(m, e89, (x7 - x15)^2 + (x24 - x32)^2 + (x41 - x49)^2
    >= 0.32159900740899994)
@NLconstraint(m, e90, (x7 - x16)^2 + (x24 - x33)^2 + (x41 - x50)^2
    >= 0.32159900740899994)
@NLconstraint(m, e91, (x7 - x17)^2 + (x24 - x34)^2 + (x41 - x51)^2
    >= 0.32159900740899994)
@NLconstraint(m, e92, (x8 - x9)^2 + (x25 - x26)^2 + (x42 - x43)^2
    >= 0.32159900740899994)
@NLconstraint(m, e93, (x8 - x10)^2 + (x25 - x27)^2 + (x42 - x44)^2
    >= 0.32159900740899994)
@NLconstraint(m, e94, (x8 - x11)^2 + (x25 - x28)^2 + (x42 - x45)^2
    >= 0.32159900740899994)
@NLconstraint(m, e95, (x8 - x12)^2 + (x25 - x29)^2 + (x42 - x46)^2
    >= 0.32159900740899994)
@NLconstraint(m, e96, (x8 - x13)^2 + (x25 - x30)^2 + (x42 - x47)^2
    >= 0.32159900740899994)
@NLconstraint(m, e97, (x8 - x14)^2 + (x25 - x31)^2 + (x42 - x48)^2
    >= 0.32159900740899994)
@NLconstraint(m, e98, (x8 - x15)^2 + (x25 - x32)^2 + (x42 - x49)^2
    >= 0.32159900740899994)
@NLconstraint(m, e99, (x8 - x16)^2 + (x25 - x33)^2 + (x42 - x50)^2
    >= 0.32159900740899994)
@NLconstraint(m, e100, (x8 - x17)^2 + (x25 - x34)^2 + (x42 - x51)^2
    >= 0.32159900740899994)
@NLconstraint(m, e101, (x9 - x10)^2 + (x26 - x27)^2 + (x43 - x44)^2
    >= 0.32159900740899994)
@NLconstraint(m, e102, (x9 - x11)^2 + (x26 - x28)^2 + (x43 - x45)^2
    >= 0.32159900740899994)
@NLconstraint(m, e103, (x9 - x12)^2 + (x26 - x29)^2 + (x43 - x46)^2
    >= 0.32159900740899994)
@NLconstraint(m, e104, (x9 - x13)^2 + (x26 - x30)^2 + (x43 - x47)^2
    >= 0.32159900740899994)
@NLconstraint(m, e105, (x9 - x14)^2 + (x26 - x31)^2 + (x43 - x48)^2
    >= 0.32159900740899994)
@NLconstraint(m, e106, (x9 - x15)^2 + (x26 - x32)^2 + (x43 - x49)^2
    >= 0.32159900740899994)
@NLconstraint(m, e107, (x9 - x16)^2 + (x26 - x33)^2 + (x43 - x50)^2
    >= 0.32159900740899994)
@NLconstraint(m, e108, (x9 - x17)^2 + (x26 - x34)^2 + (x43 - x51)^2
    >= 0.32159900740899994)
@NLconstraint(m, e109, (x10 - x11)^2 + (x27 - x28)^2 + (x44 - x45)^2
    >= 0.32159900740899994)
@NLconstraint(m, e110, (x10 - x12)^2 + (x27 - x29)^2 + (x44 - x46)^2
    >= 0.32159900740899994)
@NLconstraint(m, e111, (x10 - x13)^2 + (x27 - x30)^2 + (x44 - x47)^2
    >= 0.32159900740899994)
@NLconstraint(m, e112, (x10 - x14)^2 + (x27 - x31)^2 + (x44 - x48)^2
    >= 0.32159900740899994)
@NLconstraint(m, e113, (x10 - x15)^2 + (x27 - x32)^2 + (x44 - x49)^2
    >= 0.32159900740899994)
@NLconstraint(m, e114, (x10 - x16)^2 + (x27 - x33)^2 + (x44 - x50)^2
    >= 0.32159900740899994)
@NLconstraint(m, e115, (x10 - x17)^2 + (x27 - x34)^2 + (x44 - x51)^2
    >= 0.32159900740899994)
@NLconstraint(m, e116, (x11 - x12)^2 + (x28 - x29)^2 + (x45 - x46)^2
    >= 0.32159900740899994)
@NLconstraint(m, e117, (x11 - x13)^2 + (x28 - x30)^2 + (x45 - x47)^2
    >= 0.32159900740899994)
@NLconstraint(m, e118, (x11 - x14)^2 + (x28 - x31)^2 + (x45 - x48)^2
    >= 0.32159900740899994)
@NLconstraint(m, e119, (x11 - x15)^2 + (x28 - x32)^2 + (x45 - x49)^2
    >= 0.32159900740899994)
@NLconstraint(m, e120, (x11 - x16)^2 + (x28 - x33)^2 + (x45 - x50)^2
    >= 0.32159900740899994)
@NLconstraint(m, e121, (x11 - x17)^2 + (x28 - x34)^2 + (x45 - x51)^2
    >= 0.32159900740899994)
@NLconstraint(m, e122, (x12 - x13)^2 + (x29 - x30)^2 + (x46 - x47)^2
    >= 0.32159900740899994)
@NLconstraint(m, e123, (x12 - x14)^2 + (x29 - x31)^2 + (x46 - x48)^2
    >= 0.32159900740899994)
@NLconstraint(m, e124, (x12 - x15)^2 + (x29 - x32)^2 + (x46 - x49)^2
    >= 0.32159900740899994)
@NLconstraint(m, e125, (x12 - x16)^2 + (x29 - x33)^2 + (x46 - x50)^2
    >= 0.32159900740899994)
@NLconstraint(m, e126, (x12 - x17)^2 + (x29 - x34)^2 + (x46 - x51)^2
    >= 0.32159900740899994)
@NLconstraint(m, e127, (x13 - x14)^2 + (x30 - x31)^2 + (x47 - x48)^2
    >= 0.32159900740899994)
@NLconstraint(m, e128, (x13 - x15)^2 + (x30 - x32)^2 + (x47 - x49)^2
    >= 0.32159900740899994)
@NLconstraint(m, e129, (x13 - x16)^2 + (x30 - x33)^2 + (x47 - x50)^2
    >= 0.32159900740899994)
@NLconstraint(m, e130, (x13 - x17)^2 + (x30 - x34)^2 + (x47 - x51)^2
    >= 0.32159900740899994)
@NLconstraint(m, e131, (x14 - x15)^2 + (x31 - x32)^2 + (x48 - x49)^2
    >= 0.32159900740899994)
@NLconstraint(m, e132, (x14 - x16)^2 + (x31 - x33)^2 + (x48 - x50)^2
    >= 0.32159900740899994)
@NLconstraint(m, e133, (x14 - x17)^2 + (x31 - x34)^2 + (x48 - x51)^2
    >= 0.32159900740899994)
@NLconstraint(m, e134, (x15 - x16)^2 + (x32 - x33)^2 + (x49 - x50)^2
    >= 0.32159900740899994)
@NLconstraint(m, e135, (x15 - x17)^2 + (x32 - x34)^2 + (x49 - x51)^2
    >= 0.32159900740899994)
@NLconstraint(m, e136, (x16 - x17)^2 + (x33 - x34)^2 + (x50 - x51)^2
    >= 0.32159900740899994)
