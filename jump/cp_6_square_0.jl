# NLP written by GAMS Convert at 05/15/24 11:30:31
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#        45        6       27       12        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        19       19        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       150       60       90
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
@variable(m, x13, start=0)
@variable(m, x14, start=0)
@variable(m, x15, start=0)
@variable(m, x16, start=0)
@variable(m, x17, start=0)
@variable(m, x18, start=0)
@variable(m, x19, start=0)

@objective(m, Max, x19)

@NLconstraint(m, e1, (x1 - x2)^2 + (x7 - x8)^2 - (x13 + x14)^2 >= 0)
@NLconstraint(m, e2, (x1 - x3)^2 + (x7 - x9)^2 - (x13 + x15)^2 >= 0)
@NLconstraint(m, e3, (x1 - x4)^2 + (x7 - x10)^2 - (x13 + x16)^2 >= 0)
@NLconstraint(m, e4, (x1 - x5)^2 + (x7 - x11)^2 - (x13 + x17)^2 >= 0)
@NLconstraint(m, e5, (x1 - x6)^2 + (x7 - x12)^2 - (x13 + x18)^2 >= 0)
@NLconstraint(m, e6, (x2 - x3)^2 + (x8 - x9)^2 - (x14 + x15)^2 >= 0)
@NLconstraint(m, e7, (x2 - x4)^2 + (x8 - x10)^2 - (x14 + x16)^2 >= 0)
@NLconstraint(m, e8, (x2 - x5)^2 + (x8 - x11)^2 - (x14 + x17)^2 >= 0)
@NLconstraint(m, e9, (x2 - x6)^2 + (x8 - x12)^2 - (x14 + x18)^2 >= 0)
@NLconstraint(m, e10, (x3 - x4)^2 + (x9 - x10)^2 - (x15 + x16)^2 >= 0)
@NLconstraint(m, e11, (x3 - x5)^2 + (x9 - x11)^2 - (x15 + x17)^2 >= 0)
@NLconstraint(m, e12, (x3 - x6)^2 + (x9 - x12)^2 - (x15 + x18)^2 >= 0)
@NLconstraint(m, e13, (x4 - x5)^2 + (x10 - x11)^2 - (x16 + x17)^2 >= 0)
@NLconstraint(m, e14, (x4 - x6)^2 + (x10 - x12)^2 - (x16 + x18)^2 >= 0)
@NLconstraint(m, e15, (x5 - x6)^2 + (x11 - x12)^2 - (x17 + x18)^2 >= 0)
@constraint(m, e16, x13 - x19 == 0)
@constraint(m, e17, x14 - x19 == 0)
@constraint(m, e18, x15 - x19 == 0)
@constraint(m, e19, x16 - x19 == 0)
@constraint(m, e20, x17 - x19 == 0)
@constraint(m, e21, x18 - x19 == 0)
@constraint(m, e22, x1 + x13 <= 0.5)
@constraint(m, e23, x2 + x14 <= 0.5)
@constraint(m, e24, x3 + x15 <= 0.5)
@constraint(m, e25, x4 + x16 <= 0.5)
@constraint(m, e26, x5 + x17 <= 0.5)
@constraint(m, e27, x6 + x18 <= 0.5)
@constraint(m, e28, x1 - x13 >= -0.5)
@constraint(m, e29, x2 - x14 >= -0.5)
@constraint(m, e30, x3 - x15 >= -0.5)
@constraint(m, e31, x4 - x16 >= -0.5)
@constraint(m, e32, x5 - x17 >= -0.5)
@constraint(m, e33, x6 - x18 >= -0.5)
@constraint(m, e34, x7 + x13 <= 0.5)
@constraint(m, e35, x8 + x14 <= 0.5)
@constraint(m, e36, x9 + x15 <= 0.5)
@constraint(m, e37, x10 + x16 <= 0.5)
@constraint(m, e38, x11 + x17 <= 0.5)
@constraint(m, e39, x12 + x18 <= 0.5)
@constraint(m, e40, x7 - x13 >= -0.5)
@constraint(m, e41, x8 - x14 >= -0.5)
@constraint(m, e42, x9 - x15 >= -0.5)
@constraint(m, e43, x10 - x16 >= -0.5)
@constraint(m, e44, x11 - x17 >= -0.5)
@constraint(m, e45, x12 - x18 >= -0.5)
