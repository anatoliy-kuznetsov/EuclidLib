# NLP written by GAMS Convert at 03/17/24 14:47:55
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#        26        6       15        5        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        13       13        0        0        0        0        0        0
# FX      2
#
# Nonzero counts
#     Total    const       NL
#        97       25       72
#
# Reformulation has removed 1 variable and 1 equation

using JuMP
using MathOptInterface
const MOI = MathOptInterface

model = m = Model()

@variable(m, -2 <= x1 <= -2, start=-2)
@variable(m, 0 <= x2 <= 0, start=0)
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
@variable(m, x13 <= 4, start=0)

@objective(m, Max, x13)

@NLconstraint(m, e1, (x1 - x3)^2 + (x2 - x4)^2 - x13 >= 0)
@NLconstraint(m, e2, (x1 - x5)^2 + (x2 - x6)^2 - x13 >= 0)
@NLconstraint(m, e3, (x1 - x7)^2 + (x2 - x8)^2 - x13 >= 0)
@NLconstraint(m, e4, (x1 - x9)^2 + (x2 - x10)^2 - x13 >= 0)
@NLconstraint(m, e5, (x1 - x11)^2 + (x2 - x12)^2 - x13 >= 0)
@NLconstraint(m, e6, (x3 - x5)^2 + (x4 - x6)^2 - x13 >= 0)
@NLconstraint(m, e7, (x3 - x7)^2 + (x4 - x8)^2 - x13 >= 0)
@NLconstraint(m, e8, (x3 - x9)^2 + (x4 - x10)^2 - x13 >= 0)
@NLconstraint(m, e9, (x3 - x11)^2 + (x4 - x12)^2 - x13 >= 0)
@NLconstraint(m, e10, (x5 - x7)^2 + (x6 - x8)^2 - x13 >= 0)
@NLconstraint(m, e11, (x5 - x9)^2 + (x6 - x10)^2 - x13 >= 0)
@NLconstraint(m, e12, (x5 - x11)^2 + (x6 - x12)^2 - x13 >= 0)
@NLconstraint(m, e13, (x7 - x9)^2 + (x8 - x10)^2 - x13 >= 0)
@NLconstraint(m, e14, (x7 - x11)^2 + (x8 - x12)^2 - x13 >= 0)
@NLconstraint(m, e15, (x9 - x11)^2 + (x10 - x12)^2 - x13 >= 0)
@constraint(m, e16, x1 - x3 <= 0)
@constraint(m, e17, x3 - x5 <= 0)
@constraint(m, e18, x5 - x7 <= 0)
@constraint(m, e19, x7 - x9 <= 0)
@constraint(m, e20, x9 - x11 <= 0)
@NLconstraint(m, e21, x1^2 + x2^2 == 4)
@NLconstraint(m, e22, x3^2 + x4^2 == 4)
@NLconstraint(m, e23, x5^2 + x6^2 == 4)
@NLconstraint(m, e24, x7^2 + x8^2 == 4)
@NLconstraint(m, e25, x9^2 + x10^2 == 4)
@NLconstraint(m, e26, x11^2 + x12^2 == 4)
