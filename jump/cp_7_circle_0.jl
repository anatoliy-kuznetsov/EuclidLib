# NLP written by GAMS Convert at 05/15/24 11:34:55
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#        35        7       21        7        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        22       22        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       161       14      147
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
@variable(m, x15, start=0)
@variable(m, x16, start=0)
@variable(m, x17, start=0)
@variable(m, x18, start=0)
@variable(m, x19, start=0)
@variable(m, x20, start=0)
@variable(m, x21, start=0)
@variable(m, x22, start=0)

@objective(m, Max, x22)

@NLconstraint(m, e1, (x1 - x2)^2 + (x8 - x9)^2 - (x15 + x16)^2 >= 0)
@NLconstraint(m, e2, (x1 - x3)^2 + (x8 - x10)^2 - (x15 + x17)^2 >= 0)
@NLconstraint(m, e3, (x1 - x4)^2 + (x8 - x11)^2 - (x15 + x18)^2 >= 0)
@NLconstraint(m, e4, (x1 - x5)^2 + (x8 - x12)^2 - (x15 + x19)^2 >= 0)
@NLconstraint(m, e5, (x1 - x6)^2 + (x8 - x13)^2 - (x15 + x20)^2 >= 0)
@NLconstraint(m, e6, (x1 - x7)^2 + (x8 - x14)^2 - (x15 + x21)^2 >= 0)
@NLconstraint(m, e7, (x2 - x3)^2 + (x9 - x10)^2 - (x16 + x17)^2 >= 0)
@NLconstraint(m, e8, (x2 - x4)^2 + (x9 - x11)^2 - (x16 + x18)^2 >= 0)
@NLconstraint(m, e9, (x2 - x5)^2 + (x9 - x12)^2 - (x16 + x19)^2 >= 0)
@NLconstraint(m, e10, (x2 - x6)^2 + (x9 - x13)^2 - (x16 + x20)^2 >= 0)
@NLconstraint(m, e11, (x2 - x7)^2 + (x9 - x14)^2 - (x16 + x21)^2 >= 0)
@NLconstraint(m, e12, (x3 - x4)^2 + (x10 - x11)^2 - (x17 + x18)^2 >= 0)
@NLconstraint(m, e13, (x3 - x5)^2 + (x10 - x12)^2 - (x17 + x19)^2 >= 0)
@NLconstraint(m, e14, (x3 - x6)^2 + (x10 - x13)^2 - (x17 + x20)^2 >= 0)
@NLconstraint(m, e15, (x3 - x7)^2 + (x10 - x14)^2 - (x17 + x21)^2 >= 0)
@NLconstraint(m, e16, (x4 - x5)^2 + (x11 - x12)^2 - (x18 + x19)^2 >= 0)
@NLconstraint(m, e17, (x4 - x6)^2 + (x11 - x13)^2 - (x18 + x20)^2 >= 0)
@NLconstraint(m, e18, (x4 - x7)^2 + (x11 - x14)^2 - (x18 + x21)^2 >= 0)
@NLconstraint(m, e19, (x5 - x6)^2 + (x12 - x13)^2 - (x19 + x20)^2 >= 0)
@NLconstraint(m, e20, (x5 - x7)^2 + (x12 - x14)^2 - (x19 + x21)^2 >= 0)
@NLconstraint(m, e21, (x6 - x7)^2 + (x13 - x14)^2 - (x20 + x21)^2 >= 0)
@constraint(m, e22, x15 - x22 == 0)
@constraint(m, e23, x16 - x22 == 0)
@constraint(m, e24, x17 - x22 == 0)
@constraint(m, e25, x18 - x22 == 0)
@constraint(m, e26, x19 - x22 == 0)
@constraint(m, e27, x20 - x22 == 0)
@constraint(m, e28, x21 - x22 == 0)
@NLconstraint(m, e29, x1^2 + x8^2 - (1 - x15)^2 <= 0)
@NLconstraint(m, e30, x2^2 + x9^2 - (1 - x16)^2 <= 0)
@NLconstraint(m, e31, x3^2 + x10^2 - (1 - x17)^2 <= 0)
@NLconstraint(m, e32, x4^2 + x11^2 - (1 - x18)^2 <= 0)
@NLconstraint(m, e33, x5^2 + x12^2 - (1 - x19)^2 <= 0)
@NLconstraint(m, e34, x6^2 + x13^2 - (1 - x20)^2 <= 0)
@NLconstraint(m, e35, x7^2 + x14^2 - (1 - x21)^2 <= 0)
