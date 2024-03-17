# NLP written by GAMS Convert at 03/17/24 14:47:58
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#        55        0       35       20        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        15       15        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       173       68      105
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
@variable(m, -0.5 <= x9 <= 0.5, start=0)
@variable(m, -0.5 <= x10 <= 0.5, start=0)
@variable(m, -0.5 <= x11 <= 0.5, start=0)
@variable(m, -0.5 <= x12 <= 0.5, start=0)
@variable(m, -0.5 <= x13 <= 0.5, start=0)
@variable(m, -0.5 <= x14 <= 0.5, start=0)
@variable(m, x15, start=0)

@objective(m, Max, x15)

@NLconstraint(m, e1, (x1 - x2)^2 + (x8 - x9)^2 - (2 * x15)^2 >= 0)
@NLconstraint(m, e2, (x1 - x3)^2 + (x8 - x10)^2 - (2 * x15)^2 >= 0)
@NLconstraint(m, e3, (x1 - x4)^2 + (x8 - x11)^2 - (2 * x15)^2 >= 0)
@NLconstraint(m, e4, (x1 - x5)^2 + (x8 - x12)^2 - (2 * x15)^2 >= 0)
@NLconstraint(m, e5, (x1 - x6)^2 + (x8 - x13)^2 - (2 * x15)^2 >= 0)
@NLconstraint(m, e6, (x1 - x7)^2 + (x8 - x14)^2 - (2 * x15)^2 >= 0)
@NLconstraint(m, e7, (x2 - x3)^2 + (x9 - x10)^2 - (2 * x15)^2 >= 0)
@NLconstraint(m, e8, (x2 - x4)^2 + (x9 - x11)^2 - (2 * x15)^2 >= 0)
@NLconstraint(m, e9, (x2 - x5)^2 + (x9 - x12)^2 - (2 * x15)^2 >= 0)
@NLconstraint(m, e10, (x2 - x6)^2 + (x9 - x13)^2 - (2 * x15)^2 >= 0)
@NLconstraint(m, e11, (x2 - x7)^2 + (x9 - x14)^2 - (2 * x15)^2 >= 0)
@NLconstraint(m, e12, (x3 - x4)^2 + (x10 - x11)^2 - (2 * x15)^2 >= 0)
@NLconstraint(m, e13, (x3 - x5)^2 + (x10 - x12)^2 - (2 * x15)^2 >= 0)
@NLconstraint(m, e14, (x3 - x6)^2 + (x10 - x13)^2 - (2 * x15)^2 >= 0)
@NLconstraint(m, e15, (x3 - x7)^2 + (x10 - x14)^2 - (2 * x15)^2 >= 0)
@NLconstraint(m, e16, (x4 - x5)^2 + (x11 - x12)^2 - (2 * x15)^2 >= 0)
@NLconstraint(m, e17, (x4 - x6)^2 + (x11 - x13)^2 - (2 * x15)^2 >= 0)
@NLconstraint(m, e18, (x4 - x7)^2 + (x11 - x14)^2 - (2 * x15)^2 >= 0)
@NLconstraint(m, e19, (x5 - x6)^2 + (x12 - x13)^2 - (2 * x15)^2 >= 0)
@NLconstraint(m, e20, (x5 - x7)^2 + (x12 - x14)^2 - (2 * x15)^2 >= 0)
@NLconstraint(m, e21, (x6 - x7)^2 + (x13 - x14)^2 - (2 * x15)^2 >= 0)
@constraint(m, e22, x1 - x2 <= 0)
@constraint(m, e23, x2 - x3 <= 0)
@constraint(m, e24, x3 - x4 <= 0)
@constraint(m, e25, x4 - x5 <= 0)
@constraint(m, e26, x5 - x6 <= 0)
@constraint(m, e27, x6 - x7 <= 0)
@constraint(m, e28, x1 + x15 <= 0.5)
@constraint(m, e29, x2 + x15 <= 0.5)
@constraint(m, e30, x3 + x15 <= 0.5)
@constraint(m, e31, x4 + x15 <= 0.5)
@constraint(m, e32, x5 + x15 <= 0.5)
@constraint(m, e33, x6 + x15 <= 0.5)
@constraint(m, e34, x7 + x15 <= 0.5)
@constraint(m, e35, x1 - x15 >= -0.5)
@constraint(m, e36, x2 - x15 >= -0.5)
@constraint(m, e37, x3 - x15 >= -0.5)
@constraint(m, e38, x4 - x15 >= -0.5)
@constraint(m, e39, x5 - x15 >= -0.5)
@constraint(m, e40, x6 - x15 >= -0.5)
@constraint(m, e41, x7 - x15 >= -0.5)
@constraint(m, e42, x8 + x15 <= 0.5)
@constraint(m, e43, x9 + x15 <= 0.5)
@constraint(m, e44, x10 + x15 <= 0.5)
@constraint(m, e45, x11 + x15 <= 0.5)
@constraint(m, e46, x12 + x15 <= 0.5)
@constraint(m, e47, x13 + x15 <= 0.5)
@constraint(m, e48, x14 + x15 <= 0.5)
@constraint(m, e49, x8 - x15 >= -0.5)
@constraint(m, e50, x9 - x15 >= -0.5)
@constraint(m, e51, x10 - x15 >= -0.5)
@constraint(m, e52, x11 - x15 >= -0.5)
@constraint(m, e53, x12 - x15 >= -0.5)
@constraint(m, e54, x13 - x15 >= -0.5)
@constraint(m, e55, x14 - x15 >= -0.5)
