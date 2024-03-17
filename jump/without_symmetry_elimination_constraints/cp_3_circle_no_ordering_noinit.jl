# NLP written by GAMS Convert at 03/17/24 14:48:07
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#         6        0        3        3        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#         7        7        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#        24        0       24
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
@variable(m, x7, start=0)

@objective(m, Max, x7)

@NLconstraint(m, e1, (x1 - x2)^2 + (x4 - x5)^2 - (2 * x7)^2 >= 0)
@NLconstraint(m, e2, (x1 - x3)^2 + (x4 - x6)^2 - (2 * x7)^2 >= 0)
@NLconstraint(m, e3, (x2 - x3)^2 + (x5 - x6)^2 - (2 * x7)^2 >= 0)
@NLconstraint(m, e4, x1^2 + x4^2 - (1 - x7)^2 <= 0)
@NLconstraint(m, e5, x2^2 + x5^2 - (1 - x7)^2 <= 0)
@NLconstraint(m, e6, x3^2 + x6^2 - (1 - x7)^2 <= 0)
