# NLP written by GAMS Convert at 03/17/24 14:47:55
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#        19        0       10        9        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        11       11        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#        73        8       65
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
@variable(m, x11, start=0)

@objective(m, Max, x11)

@NLconstraint(m, e1, (x1 - x2)^2 + (x6 - x7)^2 - (2 * x11)^2 >= 0)
@NLconstraint(m, e2, (x1 - x3)^2 + (x6 - x8)^2 - (2 * x11)^2 >= 0)
@NLconstraint(m, e3, (x1 - x4)^2 + (x6 - x9)^2 - (2 * x11)^2 >= 0)
@NLconstraint(m, e4, (x1 - x5)^2 + (x6 - x10)^2 - (2 * x11)^2 >= 0)
@NLconstraint(m, e5, (x2 - x3)^2 + (x7 - x8)^2 - (2 * x11)^2 >= 0)
@NLconstraint(m, e6, (x2 - x4)^2 + (x7 - x9)^2 - (2 * x11)^2 >= 0)
@NLconstraint(m, e7, (x2 - x5)^2 + (x7 - x10)^2 - (2 * x11)^2 >= 0)
@NLconstraint(m, e8, (x3 - x4)^2 + (x8 - x9)^2 - (2 * x11)^2 >= 0)
@NLconstraint(m, e9, (x3 - x5)^2 + (x8 - x10)^2 - (2 * x11)^2 >= 0)
@NLconstraint(m, e10, (x4 - x5)^2 + (x9 - x10)^2 - (2 * x11)^2 >= 0)
@constraint(m, e11, x1 - x2 <= 0)
@constraint(m, e12, x2 - x3 <= 0)
@constraint(m, e13, x3 - x4 <= 0)
@constraint(m, e14, x4 - x5 <= 0)
@NLconstraint(m, e15, x1^2 + x6^2 - (1 - x11)^2 <= 0)
@NLconstraint(m, e16, x2^2 + x7^2 - (1 - x11)^2 <= 0)
@NLconstraint(m, e17, x3^2 + x8^2 - (1 - x11)^2 <= 0)
@NLconstraint(m, e18, x4^2 + x9^2 - (1 - x11)^2 <= 0)
@NLconstraint(m, e19, x5^2 + x10^2 - (1 - x11)^2 <= 0)