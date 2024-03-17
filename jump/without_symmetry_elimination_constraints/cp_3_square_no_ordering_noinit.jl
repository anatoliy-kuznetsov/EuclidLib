# NLP written by GAMS Convert at 03/17/24 14:48:06
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#        15        0        9        6        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#         7        7        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#        39       24       15
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

@objective(m, Max, x7)

@NLconstraint(m, e1, (x1 - x2)^2 + (x4 - x5)^2 - (2 * x7)^2 >= 0)
@NLconstraint(m, e2, (x1 - x3)^2 + (x4 - x6)^2 - (2 * x7)^2 >= 0)
@NLconstraint(m, e3, (x2 - x3)^2 + (x5 - x6)^2 - (2 * x7)^2 >= 0)
@constraint(m, e4, x1 + x7 <= 0.5)
@constraint(m, e5, x2 + x7 <= 0.5)
@constraint(m, e6, x3 + x7 <= 0.5)
@constraint(m, e7, x1 - x7 >= -0.5)
@constraint(m, e8, x2 - x7 >= -0.5)
@constraint(m, e9, x3 - x7 >= -0.5)
@constraint(m, e10, x4 + x7 <= 0.5)
@constraint(m, e11, x5 + x7 <= 0.5)
@constraint(m, e12, x6 + x7 <= 0.5)
@constraint(m, e13, x4 - x7 >= -0.5)
@constraint(m, e14, x5 - x7 >= -0.5)
@constraint(m, e15, x6 - x7 >= -0.5)
