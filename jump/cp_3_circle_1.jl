# NLP written by GAMS Convert at 05/15/24 11:27:08
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#         9        3        3        3        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        10       10        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#        33        6       27
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
@variable(m, x8, start=0)
@variable(m, x9, start=0)
@variable(m, x10, start=0)

@objective(m, Max, x10)

@NLconstraint(m, e1, (x1 - x2)^2 + (x4 - x5)^2 - (x7 + x8)^2 >= 0)
@NLconstraint(m, e2, (x1 - x3)^2 + (x4 - x6)^2 - (x7 + x9)^2 >= 0)
@NLconstraint(m, e3, (x2 - x3)^2 + (x5 - x6)^2 - (x8 + x9)^2 >= 0)
@constraint(m, e4, x7 - x10 == 0)
@constraint(m, e5, x8 - 2 * x10 == 0)
@constraint(m, e6, x9 - 3.0000000000000004 * x10 == 0)
@NLconstraint(m, e7, x1^2 + x4^2 - (1 - x7)^2 <= 0)
@NLconstraint(m, e8, x2^2 + x5^2 - (1 - x8)^2 <= 0)
@NLconstraint(m, e9, x3^2 + x6^2 - (1 - x9)^2 <= 0)
