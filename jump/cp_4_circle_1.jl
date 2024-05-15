# NLP written by GAMS Convert at 05/15/24 11:32:36
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#        14        4        6        4        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        13       13        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#        56        8       48
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
@variable(m, x9, start=0)
@variable(m, x10, start=0)
@variable(m, x11, start=0)
@variable(m, x12, start=0)
@variable(m, x13, start=0)

@objective(m, Max, x13)

@NLconstraint(m, e1, (x1 - x2)^2 + (x5 - x6)^2 - (x9 + x10)^2 >= 0)
@NLconstraint(m, e2, (x1 - x3)^2 + (x5 - x7)^2 - (x9 + x11)^2 >= 0)
@NLconstraint(m, e3, (x1 - x4)^2 + (x5 - x8)^2 - (x9 + x12)^2 >= 0)
@NLconstraint(m, e4, (x2 - x3)^2 + (x6 - x7)^2 - (x10 + x11)^2 >= 0)
@NLconstraint(m, e5, (x2 - x4)^2 + (x6 - x8)^2 - (x10 + x12)^2 >= 0)
@NLconstraint(m, e6, (x3 - x4)^2 + (x7 - x8)^2 - (x11 + x12)^2 >= 0)
@constraint(m, e7, x9 - x13 == 0)
@constraint(m, e8, x10 - 2 * x13 == 0)
@constraint(m, e9, x11 - 3.0000000000000004 * x13 == 0)
@constraint(m, e10, x12 - 4 * x13 == 0)
@NLconstraint(m, e11, x1^2 + x5^2 - (1 - x9)^2 <= 0)
@NLconstraint(m, e12, x2^2 + x6^2 - (1 - x10)^2 <= 0)
@NLconstraint(m, e13, x3^2 + x7^2 - (1 - x11)^2 <= 0)
@NLconstraint(m, e14, x4^2 + x8^2 - (1 - x12)^2 <= 0)
