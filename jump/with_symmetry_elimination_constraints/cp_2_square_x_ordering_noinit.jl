# NLP written by GAMS Convert at 03/17/24 14:47:57
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#        10        0        5        5        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#         5        5        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#        23       18        5
#
# Reformulation has removed 1 variable and 1 equation

using JuMP
using MathOptInterface
const MOI = MathOptInterface

model = m = Model()

@variable(m, -0.5 <= x1 <= 0.5, start=0)
@variable(m, -0.5 <= x2 <= 0.5, start=0)
@variable(m, -0.5 <= x3 <= 0.5, start=0)
@variable(m, -0.5 <= x4 <= 0.5, start=0)
@variable(m, x5, start=0)

@objective(m, Max, x5)

@NLconstraint(m, e1, (x1 - x2)^2 + (x3 - x4)^2 - (2 * x5)^2 >= 0)
@constraint(m, e2, x1 - x2 <= 0)
@constraint(m, e3, x1 + x5 <= 0.5)
@constraint(m, e4, x2 + x5 <= 0.5)
@constraint(m, e5, x1 - x5 >= -0.5)
@constraint(m, e6, x2 - x5 >= -0.5)
@constraint(m, e7, x3 + x5 <= 0.5)
@constraint(m, e8, x4 + x5 <= 0.5)
@constraint(m, e9, x3 - x5 >= -0.5)
@constraint(m, e10, x4 - x5 >= -0.5)