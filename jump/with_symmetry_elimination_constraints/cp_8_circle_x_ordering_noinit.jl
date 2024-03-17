# NLP written by GAMS Convert at 03/17/24 14:47:55
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#        43        0       28       15        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        17       17        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       178       14      164
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
@variable(m, -1 <= x11 <= 1, start=0)
@variable(m, -1 <= x12 <= 1, start=0)
@variable(m, -1 <= x13 <= 1, start=0)
@variable(m, -1 <= x14 <= 1, start=0)
@variable(m, -1 <= x15 <= 1, start=0)
@variable(m, -1 <= x16 <= 1, start=0)
@variable(m, x17, start=0)

@objective(m, Max, x17)

@NLconstraint(m, e1, (x1 - x2)^2 + (x9 - x10)^2 - (2 * x17)^2 >= 0)
@NLconstraint(m, e2, (x1 - x3)^2 + (x9 - x11)^2 - (2 * x17)^2 >= 0)
@NLconstraint(m, e3, (x1 - x4)^2 + (x9 - x12)^2 - (2 * x17)^2 >= 0)
@NLconstraint(m, e4, (x1 - x5)^2 + (x9 - x13)^2 - (2 * x17)^2 >= 0)
@NLconstraint(m, e5, (x1 - x6)^2 + (x9 - x14)^2 - (2 * x17)^2 >= 0)
@NLconstraint(m, e6, (x1 - x7)^2 + (x9 - x15)^2 - (2 * x17)^2 >= 0)
@NLconstraint(m, e7, (x1 - x8)^2 + (x9 - x16)^2 - (2 * x17)^2 >= 0)
@NLconstraint(m, e8, (x2 - x3)^2 + (x10 - x11)^2 - (2 * x17)^2 >= 0)
@NLconstraint(m, e9, (x2 - x4)^2 + (x10 - x12)^2 - (2 * x17)^2 >= 0)
@NLconstraint(m, e10, (x2 - x5)^2 + (x10 - x13)^2 - (2 * x17)^2 >= 0)
@NLconstraint(m, e11, (x2 - x6)^2 + (x10 - x14)^2 - (2 * x17)^2 >= 0)
@NLconstraint(m, e12, (x2 - x7)^2 + (x10 - x15)^2 - (2 * x17)^2 >= 0)
@NLconstraint(m, e13, (x2 - x8)^2 + (x10 - x16)^2 - (2 * x17)^2 >= 0)
@NLconstraint(m, e14, (x3 - x4)^2 + (x11 - x12)^2 - (2 * x17)^2 >= 0)
@NLconstraint(m, e15, (x3 - x5)^2 + (x11 - x13)^2 - (2 * x17)^2 >= 0)
@NLconstraint(m, e16, (x3 - x6)^2 + (x11 - x14)^2 - (2 * x17)^2 >= 0)
@NLconstraint(m, e17, (x3 - x7)^2 + (x11 - x15)^2 - (2 * x17)^2 >= 0)
@NLconstraint(m, e18, (x3 - x8)^2 + (x11 - x16)^2 - (2 * x17)^2 >= 0)
@NLconstraint(m, e19, (x4 - x5)^2 + (x12 - x13)^2 - (2 * x17)^2 >= 0)
@NLconstraint(m, e20, (x4 - x6)^2 + (x12 - x14)^2 - (2 * x17)^2 >= 0)
@NLconstraint(m, e21, (x4 - x7)^2 + (x12 - x15)^2 - (2 * x17)^2 >= 0)
@NLconstraint(m, e22, (x4 - x8)^2 + (x12 - x16)^2 - (2 * x17)^2 >= 0)
@NLconstraint(m, e23, (x5 - x6)^2 + (x13 - x14)^2 - (2 * x17)^2 >= 0)
@NLconstraint(m, e24, (x5 - x7)^2 + (x13 - x15)^2 - (2 * x17)^2 >= 0)
@NLconstraint(m, e25, (x5 - x8)^2 + (x13 - x16)^2 - (2 * x17)^2 >= 0)
@NLconstraint(m, e26, (x6 - x7)^2 + (x14 - x15)^2 - (2 * x17)^2 >= 0)
@NLconstraint(m, e27, (x6 - x8)^2 + (x14 - x16)^2 - (2 * x17)^2 >= 0)
@NLconstraint(m, e28, (x7 - x8)^2 + (x15 - x16)^2 - (2 * x17)^2 >= 0)
@constraint(m, e29, x1 - x2 <= 0)
@constraint(m, e30, x2 - x3 <= 0)
@constraint(m, e31, x3 - x4 <= 0)
@constraint(m, e32, x4 - x5 <= 0)
@constraint(m, e33, x5 - x6 <= 0)
@constraint(m, e34, x6 - x7 <= 0)
@constraint(m, e35, x7 - x8 <= 0)
@NLconstraint(m, e36, x1^2 + x9^2 - (1 - x17)^2 <= 0)
@NLconstraint(m, e37, x2^2 + x10^2 - (1 - x17)^2 <= 0)
@NLconstraint(m, e38, x3^2 + x11^2 - (1 - x17)^2 <= 0)
@NLconstraint(m, e39, x4^2 + x12^2 - (1 - x17)^2 <= 0)
@NLconstraint(m, e40, x5^2 + x13^2 - (1 - x17)^2 <= 0)
@NLconstraint(m, e41, x6^2 + x14^2 - (1 - x17)^2 <= 0)
@NLconstraint(m, e42, x7^2 + x15^2 - (1 - x17)^2 <= 0)
@NLconstraint(m, e43, x8^2 + x16^2 - (1 - x17)^2 <= 0)
