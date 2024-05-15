# NLP written by GAMS Convert at 05/15/24 11:29:20
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#        27        6       15        6        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        19       19        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       120       12      108
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
@constraint(m, e17, x14 - 0.7071067811865476 * x19 == 0)
@constraint(m, e18, x15 - 0.5773502691896257 * x19 == 0)
@constraint(m, e19, x16 - 0.5 * x19 == 0)
@constraint(m, e20, x17 - 0.447213595499958 * x19 == 0)
@constraint(m, e21, x18 - 0.408248290463863 * x19 == 0)
@NLconstraint(m, e22, x1^2 + x7^2 - (1 - x13)^2 <= 0)
@NLconstraint(m, e23, x2^2 + x8^2 - (1 - x14)^2 <= 0)
@NLconstraint(m, e24, x3^2 + x9^2 - (1 - x15)^2 <= 0)
@NLconstraint(m, e25, x4^2 + x10^2 - (1 - x16)^2 <= 0)
@NLconstraint(m, e26, x5^2 + x11^2 - (1 - x17)^2 <= 0)
@NLconstraint(m, e27, x6^2 + x12^2 - (1 - x18)^2 <= 0)
