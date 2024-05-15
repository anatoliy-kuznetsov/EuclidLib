# NLP written by GAMS Convert at 05/15/24 11:26:24
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#        26        4       14        8        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        13       13        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#        76       40       36
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
@variable(m, -0.5 <= x7 <= 0.5, start=0)
@variable(m, -0.5 <= x8 <= 0.5, start=0)
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
@constraint(m, e8, x10 - x13 == 0)
@constraint(m, e9, x11 - x13 == 0)
@constraint(m, e10, x12 - x13 == 0)
@constraint(m, e11, x1 + x9 <= 0.5)
@constraint(m, e12, x2 + x10 <= 0.5)
@constraint(m, e13, x3 + x11 <= 0.5)
@constraint(m, e14, x4 + x12 <= 0.5)
@constraint(m, e15, x1 - x9 >= -0.5)
@constraint(m, e16, x2 - x10 >= -0.5)
@constraint(m, e17, x3 - x11 >= -0.5)
@constraint(m, e18, x4 - x12 >= -0.5)
@constraint(m, e19, x5 + x9 <= 0.5)
@constraint(m, e20, x6 + x10 <= 0.5)
@constraint(m, e21, x7 + x11 <= 0.5)
@constraint(m, e22, x8 + x12 <= 0.5)
@constraint(m, e23, x5 - x9 >= -0.5)
@constraint(m, e24, x6 - x10 >= -0.5)
@constraint(m, e25, x7 - x11 >= -0.5)
@constraint(m, e26, x8 - x12 >= -0.5)
