# NLP written by GAMS Convert at 03/17/24 14:48:16
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#        12        0       12        0        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#         7        7        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#        36       21       15
#
# Reformulation has removed 1 variable and 1 equation

from pyomo.environ import *

model = m = ConcreteModel()

m.x1 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x2 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x3 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x4 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x5 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x6 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x7 = Var(within=Reals, bounds=(None,None), initialize=0)

m.obj = Objective(sense=maximize, expr= m.x7)

m.e1 = Constraint(expr= (m.x1 - m.x2)**2 + (m.x4 - m.x5)**2 - (2 * m.x7)**2
    >= 0)
m.e2 = Constraint(expr= (m.x1 - m.x3)**2 + (m.x4 - m.x6)**2 - (2 * m.x7)**2
    >= 0)
m.e3 = Constraint(expr= (m.x2 - m.x3)**2 + (m.x5 - m.x6)**2 - (2 * m.x7)**2
    >= 0)
m.e4 = Constraint(expr= m.x1 - m.x7 >= 0)
m.e5 = Constraint(expr= m.x2 - m.x7 >= 0)
m.e6 = Constraint(expr= m.x3 - m.x7 >= 0)
m.e7 = Constraint(expr= m.x4 - m.x7 >= 0)
m.e8 = Constraint(expr= m.x5 - m.x7 >= 0)
m.e9 = Constraint(expr= m.x6 - m.x7 >= 0)
m.e10 = Constraint(expr= -0.7071067811865475 * m.x1 - 0.7071067811865475 * m.x4
    - m.x7 >= -0.7071067811865475)
m.e11 = Constraint(expr= -0.7071067811865475 * m.x2 - 0.7071067811865475 * m.x5
    - m.x7 >= -0.7071067811865475)
m.e12 = Constraint(expr= -0.7071067811865475 * m.x3 - 0.7071067811865475 * m.x6
    - m.x7 >= -0.7071067811865475)