# NLP written by GAMS Convert at 05/15/24 11:34:46
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#        28        7       21        0        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        15       15        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       119       21       98
#
# Reformulation has removed 1 variable and 1 equation

using JuMP
using MathOptInterface
const MOI = MathOptInterface

model = m = Model()

@variable(m, -2 <= x1 <= 2, start=0)
@variable(m, -2 <= x2 <= 2, start=0)
@variable(m, -2 <= x3 <= 2, start=0)
@variable(m, -2 <= x4 <= 2, start=0)
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
@variable(m, x15 <= 4, start=0)

@objective(m, Max, x15)

@NLconstraint(m, e1, (x1 - x3)^2 + (x2 - x4)^2 - x15 >= 0)
@NLconstraint(m, e2, (x1 - x5)^2 + (x2 - x6)^2 - x15 >= 0)
@NLconstraint(m, e3, (x1 - x7)^2 + (x2 - x8)^2 - x15 >= 0)
@NLconstraint(m, e4, (x1 - x9)^2 + (x2 - x10)^2 - x15 >= 0)
@NLconstraint(m, e5, (x1 - x11)^2 + (x2 - x12)^2 - x15 >= 0)
@NLconstraint(m, e6, (x1 - x13)^2 + (x2 - x14)^2 - x15 >= 0)
@NLconstraint(m, e7, (x3 - x5)^2 + (x4 - x6)^2 - x15 >= 0)
@NLconstraint(m, e8, (x3 - x7)^2 + (x4 - x8)^2 - x15 >= 0)
@NLconstraint(m, e9, (x3 - x9)^2 + (x4 - x10)^2 - x15 >= 0)
@NLconstraint(m, e10, (x3 - x11)^2 + (x4 - x12)^2 - x15 >= 0)
@NLconstraint(m, e11, (x3 - x13)^2 + (x4 - x14)^2 - x15 >= 0)
@NLconstraint(m, e12, (x5 - x7)^2 + (x6 - x8)^2 - x15 >= 0)
@NLconstraint(m, e13, (x5 - x9)^2 + (x6 - x10)^2 - x15 >= 0)
@NLconstraint(m, e14, (x5 - x11)^2 + (x6 - x12)^2 - x15 >= 0)
@NLconstraint(m, e15, (x5 - x13)^2 + (x6 - x14)^2 - x15 >= 0)
@NLconstraint(m, e16, (x7 - x9)^2 + (x8 - x10)^2 - x15 >= 0)
@NLconstraint(m, e17, (x7 - x11)^2 + (x8 - x12)^2 - x15 >= 0)
@NLconstraint(m, e18, (x7 - x13)^2 + (x8 - x14)^2 - x15 >= 0)
@NLconstraint(m, e19, (x9 - x11)^2 + (x10 - x12)^2 - x15 >= 0)
@NLconstraint(m, e20, (x9 - x13)^2 + (x10 - x14)^2 - x15 >= 0)
@NLconstraint(m, e21, (x11 - x13)^2 + (x12 - x14)^2 - x15 >= 0)
@NLconstraint(m, e22, x1^2 + x2^2 == 4)
@NLconstraint(m, e23, x3^2 + x4^2 == 4)
@NLconstraint(m, e24, x5^2 + x6^2 == 4)
@NLconstraint(m, e25, x7^2 + x8^2 == 4)
@NLconstraint(m, e26, x9^2 + x10^2 == 4)
@NLconstraint(m, e27, x11^2 + x12^2 == 4)
@NLconstraint(m, e28, x13^2 + x14^2 == 4)
