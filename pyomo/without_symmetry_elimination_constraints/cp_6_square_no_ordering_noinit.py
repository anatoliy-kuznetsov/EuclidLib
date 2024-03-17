# NLP written by GAMS Convert at 03/17/24 14:48:12
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#        39        0       27       12        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        13       13        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       123       48       75
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
m.x13 = Var(within=Reals, bounds=(None,None), initialize=0)

m.obj = Objective(sense=maximize, expr= m.x13)

m.e1 = Constraint(expr= (m.x1 - m.x2)**2 + (m.x7 - m.x8)**2 - (2 * m.x13)**2
    >= 0)
m.e2 = Constraint(expr= (m.x1 - m.x3)**2 + (m.x7 - m.x9)**2 - (2 * m.x13)**2
    >= 0)
m.e3 = Constraint(expr= (m.x1 - m.x4)**2 + (m.x7 - m.x10)**2 - (2 * m.x13)**2
    >= 0)
m.e4 = Constraint(expr= (m.x1 - m.x5)**2 + (m.x7 - m.x11)**2 - (2 * m.x13)**2
    >= 0)
m.e5 = Constraint(expr= (m.x1 - m.x6)**2 + (m.x7 - m.x12)**2 - (2 * m.x13)**2
    >= 0)
m.e6 = Constraint(expr= (m.x2 - m.x3)**2 + (m.x8 - m.x9)**2 - (2 * m.x13)**2
    >= 0)
m.e7 = Constraint(expr= (m.x2 - m.x4)**2 + (m.x8 - m.x10)**2 - (2 * m.x13)**2
    >= 0)
m.e8 = Constraint(expr= (m.x2 - m.x5)**2 + (m.x8 - m.x11)**2 - (2 * m.x13)**2
    >= 0)
m.e9 = Constraint(expr= (m.x2 - m.x6)**2 + (m.x8 - m.x12)**2 - (2 * m.x13)**2
    >= 0)
m.e10 = Constraint(expr= (m.x3 - m.x4)**2 + (m.x9 - m.x10)**2 - (2 * m.x13)**2
    >= 0)
m.e11 = Constraint(expr= (m.x3 - m.x5)**2 + (m.x9 - m.x11)**2 - (2 * m.x13)**2
    >= 0)
m.e12 = Constraint(expr= (m.x3 - m.x6)**2 + (m.x9 - m.x12)**2 - (2 * m.x13)**2
    >= 0)
m.e13 = Constraint(expr= (m.x4 - m.x5)**2 + (m.x10 - m.x11)**2 - (2 * m.x13)**2
    >= 0)
m.e14 = Constraint(expr= (m.x4 - m.x6)**2 + (m.x10 - m.x12)**2 - (2 * m.x13)**2
    >= 0)
m.e15 = Constraint(expr= (m.x5 - m.x6)**2 + (m.x11 - m.x12)**2 - (2 * m.x13)**2
    >= 0)
m.e16 = Constraint(expr= m.x1 + m.x13 <= 0.5)
m.e17 = Constraint(expr= m.x2 + m.x13 <= 0.5)
m.e18 = Constraint(expr= m.x3 + m.x13 <= 0.5)
m.e19 = Constraint(expr= m.x4 + m.x13 <= 0.5)
m.e20 = Constraint(expr= m.x5 + m.x13 <= 0.5)
m.e21 = Constraint(expr= m.x6 + m.x13 <= 0.5)
m.e22 = Constraint(expr= m.x1 - m.x13 >= -0.5)
m.e23 = Constraint(expr= m.x2 - m.x13 >= -0.5)
m.e24 = Constraint(expr= m.x3 - m.x13 >= -0.5)
m.e25 = Constraint(expr= m.x4 - m.x13 >= -0.5)
m.e26 = Constraint(expr= m.x5 - m.x13 >= -0.5)
m.e27 = Constraint(expr= m.x6 - m.x13 >= -0.5)
m.e28 = Constraint(expr= m.x7 + m.x13 <= 0.5)
m.e29 = Constraint(expr= m.x8 + m.x13 <= 0.5)
m.e30 = Constraint(expr= m.x9 + m.x13 <= 0.5)
m.e31 = Constraint(expr= m.x10 + m.x13 <= 0.5)
m.e32 = Constraint(expr= m.x11 + m.x13 <= 0.5)
m.e33 = Constraint(expr= m.x12 + m.x13 <= 0.5)
m.e34 = Constraint(expr= m.x7 - m.x13 >= -0.5)
m.e35 = Constraint(expr= m.x8 - m.x13 >= -0.5)
m.e36 = Constraint(expr= m.x9 - m.x13 >= -0.5)
m.e37 = Constraint(expr= m.x10 - m.x13 >= -0.5)
m.e38 = Constraint(expr= m.x11 - m.x13 >= -0.5)
m.e39 = Constraint(expr= m.x12 - m.x13 >= -0.5)
