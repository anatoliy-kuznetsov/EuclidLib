# NLP written by GAMS Convert at 03/17/24 14:48:15
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#         3        0        1        2        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#         5        5        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#        11        0       11
#
# Reformulation has removed 1 variable and 1 equation

from pyomo.environ import *

model = m = ConcreteModel()

m.x1 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x2 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x3 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x4 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x5 = Var(within=Reals, bounds=(None,None), initialize=0)

m.obj = Objective(sense=maximize, expr= m.x5)

m.e1 = Constraint(expr= (m.x1 - m.x2)**2 + (m.x3 - m.x4)**2 - (2 * m.x5)**2
    >= 0)
m.e2 = Constraint(expr= m.x1**2 + m.x3**2 - (1 - m.x5)**2 <= 0)
m.e3 = Constraint(expr= m.x2**2 + m.x4**2 - (1 - m.x5)**2 <= 0)