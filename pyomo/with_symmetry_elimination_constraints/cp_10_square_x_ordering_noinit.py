# NLP written by GAMS Convert at 03/17/24 14:48:00
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#        94        0       65       29        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        21       21        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       323       98      225
#
# Reformulation has removed 1 variable and 1 equation

from pyomo.environ import *

model = m = ConcreteModel()

m.x1 = Var(within=Reals, bounds=(-0.5,0.5), initialize=0)
m.x2 = Var(within=Reals, bounds=(-0.5,0.5), initialize=0)
m.x3 = Var(within=Reals, bounds=(-0.5,0.5), initialize=0)
m.x4 = Var(within=Reals, bounds=(-0.5,0.5), initialize=0)
m.x5 = Var(within=Reals, bounds=(-0.5,0.5), initialize=0)
m.x6 = Var(within=Reals, bounds=(-0.5,0.5), initialize=0)
m.x7 = Var(within=Reals, bounds=(-0.5,0.5), initialize=0)
m.x8 = Var(within=Reals, bounds=(-0.5,0.5), initialize=0)
m.x9 = Var(within=Reals, bounds=(-0.5,0.5), initialize=0)
m.x10 = Var(within=Reals, bounds=(-0.5,0.5), initialize=0)
m.x11 = Var(within=Reals, bounds=(-0.5,0.5), initialize=0)
m.x12 = Var(within=Reals, bounds=(-0.5,0.5), initialize=0)
m.x13 = Var(within=Reals, bounds=(-0.5,0.5), initialize=0)
m.x14 = Var(within=Reals, bounds=(-0.5,0.5), initialize=0)
m.x15 = Var(within=Reals, bounds=(-0.5,0.5), initialize=0)
m.x16 = Var(within=Reals, bounds=(-0.5,0.5), initialize=0)
m.x17 = Var(within=Reals, bounds=(-0.5,0.5), initialize=0)
m.x18 = Var(within=Reals, bounds=(-0.5,0.5), initialize=0)
m.x19 = Var(within=Reals, bounds=(-0.5,0.5), initialize=0)
m.x20 = Var(within=Reals, bounds=(-0.5,0.5), initialize=0)
m.x21 = Var(within=Reals, bounds=(None,None), initialize=0)

m.obj = Objective(sense=maximize, expr= m.x21)

m.e1 = Constraint(expr= (m.x1 - m.x2)**2 + (m.x11 - m.x12)**2 - (2 * m.x21)**2
    >= 0)
m.e2 = Constraint(expr= (m.x1 - m.x3)**2 + (m.x11 - m.x13)**2 - (2 * m.x21)**2
    >= 0)
m.e3 = Constraint(expr= (m.x1 - m.x4)**2 + (m.x11 - m.x14)**2 - (2 * m.x21)**2
    >= 0)
m.e4 = Constraint(expr= (m.x1 - m.x5)**2 + (m.x11 - m.x15)**2 - (2 * m.x21)**2
    >= 0)
m.e5 = Constraint(expr= (m.x1 - m.x6)**2 + (m.x11 - m.x16)**2 - (2 * m.x21)**2
    >= 0)
m.e6 = Constraint(expr= (m.x1 - m.x7)**2 + (m.x11 - m.x17)**2 - (2 * m.x21)**2
    >= 0)
m.e7 = Constraint(expr= (m.x1 - m.x8)**2 + (m.x11 - m.x18)**2 - (2 * m.x21)**2
    >= 0)
m.e8 = Constraint(expr= (m.x1 - m.x9)**2 + (m.x11 - m.x19)**2 - (2 * m.x21)**2
    >= 0)
m.e9 = Constraint(expr= (m.x1 - m.x10)**2 + (m.x11 - m.x20)**2 - (2 * m.x21)**2
    >= 0)
m.e10 = Constraint(expr= (m.x2 - m.x3)**2 + (m.x12 - m.x13)**2 - (2 * m.x21)**2
    >= 0)
m.e11 = Constraint(expr= (m.x2 - m.x4)**2 + (m.x12 - m.x14)**2 - (2 * m.x21)**2
    >= 0)
m.e12 = Constraint(expr= (m.x2 - m.x5)**2 + (m.x12 - m.x15)**2 - (2 * m.x21)**2
    >= 0)
m.e13 = Constraint(expr= (m.x2 - m.x6)**2 + (m.x12 - m.x16)**2 - (2 * m.x21)**2
    >= 0)
m.e14 = Constraint(expr= (m.x2 - m.x7)**2 + (m.x12 - m.x17)**2 - (2 * m.x21)**2
    >= 0)
m.e15 = Constraint(expr= (m.x2 - m.x8)**2 + (m.x12 - m.x18)**2 - (2 * m.x21)**2
    >= 0)
m.e16 = Constraint(expr= (m.x2 - m.x9)**2 + (m.x12 - m.x19)**2 - (2 * m.x21)**2
    >= 0)
m.e17 = Constraint(expr= (m.x2 - m.x10)**2 + (m.x12 - m.x20)**2 - (2 * m.x21)**
    2 >= 0)
m.e18 = Constraint(expr= (m.x3 - m.x4)**2 + (m.x13 - m.x14)**2 - (2 * m.x21)**2
    >= 0)
m.e19 = Constraint(expr= (m.x3 - m.x5)**2 + (m.x13 - m.x15)**2 - (2 * m.x21)**2
    >= 0)
m.e20 = Constraint(expr= (m.x3 - m.x6)**2 + (m.x13 - m.x16)**2 - (2 * m.x21)**2
    >= 0)
m.e21 = Constraint(expr= (m.x3 - m.x7)**2 + (m.x13 - m.x17)**2 - (2 * m.x21)**2
    >= 0)
m.e22 = Constraint(expr= (m.x3 - m.x8)**2 + (m.x13 - m.x18)**2 - (2 * m.x21)**2
    >= 0)
m.e23 = Constraint(expr= (m.x3 - m.x9)**2 + (m.x13 - m.x19)**2 - (2 * m.x21)**2
    >= 0)
m.e24 = Constraint(expr= (m.x3 - m.x10)**2 + (m.x13 - m.x20)**2 - (2 * m.x21)**
    2 >= 0)
m.e25 = Constraint(expr= (m.x4 - m.x5)**2 + (m.x14 - m.x15)**2 - (2 * m.x21)**2
    >= 0)
m.e26 = Constraint(expr= (m.x4 - m.x6)**2 + (m.x14 - m.x16)**2 - (2 * m.x21)**2
    >= 0)
m.e27 = Constraint(expr= (m.x4 - m.x7)**2 + (m.x14 - m.x17)**2 - (2 * m.x21)**2
    >= 0)
m.e28 = Constraint(expr= (m.x4 - m.x8)**2 + (m.x14 - m.x18)**2 - (2 * m.x21)**2
    >= 0)
m.e29 = Constraint(expr= (m.x4 - m.x9)**2 + (m.x14 - m.x19)**2 - (2 * m.x21)**2
    >= 0)
m.e30 = Constraint(expr= (m.x4 - m.x10)**2 + (m.x14 - m.x20)**2 - (2 * m.x21)**
    2 >= 0)
m.e31 = Constraint(expr= (m.x5 - m.x6)**2 + (m.x15 - m.x16)**2 - (2 * m.x21)**2
    >= 0)
m.e32 = Constraint(expr= (m.x5 - m.x7)**2 + (m.x15 - m.x17)**2 - (2 * m.x21)**2
    >= 0)
m.e33 = Constraint(expr= (m.x5 - m.x8)**2 + (m.x15 - m.x18)**2 - (2 * m.x21)**2
    >= 0)
m.e34 = Constraint(expr= (m.x5 - m.x9)**2 + (m.x15 - m.x19)**2 - (2 * m.x21)**2
    >= 0)
m.e35 = Constraint(expr= (m.x5 - m.x10)**2 + (m.x15 - m.x20)**2 - (2 * m.x21)**
    2 >= 0)
m.e36 = Constraint(expr= (m.x6 - m.x7)**2 + (m.x16 - m.x17)**2 - (2 * m.x21)**2
    >= 0)
m.e37 = Constraint(expr= (m.x6 - m.x8)**2 + (m.x16 - m.x18)**2 - (2 * m.x21)**2
    >= 0)
m.e38 = Constraint(expr= (m.x6 - m.x9)**2 + (m.x16 - m.x19)**2 - (2 * m.x21)**2
    >= 0)
m.e39 = Constraint(expr= (m.x6 - m.x10)**2 + (m.x16 - m.x20)**2 - (2 * m.x21)**
    2 >= 0)
m.e40 = Constraint(expr= (m.x7 - m.x8)**2 + (m.x17 - m.x18)**2 - (2 * m.x21)**2
    >= 0)
m.e41 = Constraint(expr= (m.x7 - m.x9)**2 + (m.x17 - m.x19)**2 - (2 * m.x21)**2
    >= 0)
m.e42 = Constraint(expr= (m.x7 - m.x10)**2 + (m.x17 - m.x20)**2 - (2 * m.x21)**
    2 >= 0)
m.e43 = Constraint(expr= (m.x8 - m.x9)**2 + (m.x18 - m.x19)**2 - (2 * m.x21)**2
    >= 0)
m.e44 = Constraint(expr= (m.x8 - m.x10)**2 + (m.x18 - m.x20)**2 - (2 * m.x21)**
    2 >= 0)
m.e45 = Constraint(expr= (m.x9 - m.x10)**2 + (m.x19 - m.x20)**2 - (2 * m.x21)**
    2 >= 0)
m.e46 = Constraint(expr= m.x1 - m.x2 <= 0)
m.e47 = Constraint(expr= m.x2 - m.x3 <= 0)
m.e48 = Constraint(expr= m.x3 - m.x4 <= 0)
m.e49 = Constraint(expr= m.x4 - m.x5 <= 0)
m.e50 = Constraint(expr= m.x5 - m.x6 <= 0)
m.e51 = Constraint(expr= m.x6 - m.x7 <= 0)
m.e52 = Constraint(expr= m.x7 - m.x8 <= 0)
m.e53 = Constraint(expr= m.x8 - m.x9 <= 0)
m.e54 = Constraint(expr= m.x9 - m.x10 <= 0)
m.e55 = Constraint(expr= m.x1 + m.x21 <= 0.5)
m.e56 = Constraint(expr= m.x2 + m.x21 <= 0.5)
m.e57 = Constraint(expr= m.x3 + m.x21 <= 0.5)
m.e58 = Constraint(expr= m.x4 + m.x21 <= 0.5)
m.e59 = Constraint(expr= m.x5 + m.x21 <= 0.5)
m.e60 = Constraint(expr= m.x6 + m.x21 <= 0.5)
m.e61 = Constraint(expr= m.x7 + m.x21 <= 0.5)
m.e62 = Constraint(expr= m.x8 + m.x21 <= 0.5)
m.e63 = Constraint(expr= m.x9 + m.x21 <= 0.5)
m.e64 = Constraint(expr= m.x10 + m.x21 <= 0.5)
m.e65 = Constraint(expr= m.x1 - m.x21 >= -0.5)
m.e66 = Constraint(expr= m.x2 - m.x21 >= -0.5)
m.e67 = Constraint(expr= m.x3 - m.x21 >= -0.5)
m.e68 = Constraint(expr= m.x4 - m.x21 >= -0.5)
m.e69 = Constraint(expr= m.x5 - m.x21 >= -0.5)
m.e70 = Constraint(expr= m.x6 - m.x21 >= -0.5)
m.e71 = Constraint(expr= m.x7 - m.x21 >= -0.5)
m.e72 = Constraint(expr= m.x8 - m.x21 >= -0.5)
m.e73 = Constraint(expr= m.x9 - m.x21 >= -0.5)
m.e74 = Constraint(expr= m.x10 - m.x21 >= -0.5)
m.e75 = Constraint(expr= m.x11 + m.x21 <= 0.5)
m.e76 = Constraint(expr= m.x12 + m.x21 <= 0.5)
m.e77 = Constraint(expr= m.x13 + m.x21 <= 0.5)
m.e78 = Constraint(expr= m.x14 + m.x21 <= 0.5)
m.e79 = Constraint(expr= m.x15 + m.x21 <= 0.5)
m.e80 = Constraint(expr= m.x16 + m.x21 <= 0.5)
m.e81 = Constraint(expr= m.x17 + m.x21 <= 0.5)
m.e82 = Constraint(expr= m.x18 + m.x21 <= 0.5)
m.e83 = Constraint(expr= m.x19 + m.x21 <= 0.5)
m.e84 = Constraint(expr= m.x20 + m.x21 <= 0.5)
m.e85 = Constraint(expr= m.x11 - m.x21 >= -0.5)
m.e86 = Constraint(expr= m.x12 - m.x21 >= -0.5)
m.e87 = Constraint(expr= m.x13 - m.x21 >= -0.5)
m.e88 = Constraint(expr= m.x14 - m.x21 >= -0.5)
m.e89 = Constraint(expr= m.x15 - m.x21 >= -0.5)
m.e90 = Constraint(expr= m.x16 - m.x21 >= -0.5)
m.e91 = Constraint(expr= m.x17 - m.x21 >= -0.5)
m.e92 = Constraint(expr= m.x18 - m.x21 >= -0.5)
m.e93 = Constraint(expr= m.x19 - m.x21 >= -0.5)
m.e94 = Constraint(expr= m.x20 - m.x21 >= -0.5)
