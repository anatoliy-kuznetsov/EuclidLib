# NLP written by GAMS Convert at 05/15/24 11:28:38
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#        18        3        9        6        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        10       10        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#        48       30       18
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
@variable(m, -0.5 <= x5 <= 0.5, start=0)
@variable(m, -0.5 <= x6 <= 0.5, start=0)
@variable(m, x7, start=0)
@variable(m, x8, start=0)
@variable(m, x9, start=0)
@variable(m, x10, start=0)

@objective(m, Max, x10)

@NLconstraint(m, e1, (x1 - x2)^2 + (x4 - x5)^2 - (x7 + x8)^2 >= 0)
@NLconstraint(m, e2, (x1 - x3)^2 + (x4 - x6)^2 - (x7 + x9)^2 >= 0)
@NLconstraint(m, e3, (x2 - x3)^2 + (x5 - x6)^2 - (x8 + x9)^2 >= 0)
@constraint(m, e4, x7 - x10 == 0)
@constraint(m, e5, x8 - x10 == 0)
@constraint(m, e6, x9 - x10 == 0)
@constraint(m, e7, x1 + x7 <= 0.5)
@constraint(m, e8, x2 + x8 <= 0.5)
@constraint(m, e9, x3 + x9 <= 0.5)
@constraint(m, e10, x1 - x7 >= -0.5)
@constraint(m, e11, x2 - x8 >= -0.5)
@constraint(m, e12, x3 - x9 >= -0.5)
@constraint(m, e13, x4 + x7 <= 0.5)
@constraint(m, e14, x5 + x8 <= 0.5)
@constraint(m, e15, x6 + x9 <= 0.5)
@constraint(m, e16, x4 - x7 >= -0.5)
@constraint(m, e17, x5 - x8 >= -0.5)
@constraint(m, e18, x6 - x9 >= -0.5)
