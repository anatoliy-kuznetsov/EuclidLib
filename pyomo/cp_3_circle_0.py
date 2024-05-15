# NLP written by GAMS Convert at 05/15/24 11:45:23
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#         9        3        3        3        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        10       10        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#        33        6       27
#
# Reformulation has removed 1 variable and 1 equation

from pyomo.environ import *

model = m = ConcreteModel()

m.x1 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x2 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x3 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x4 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x5 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x6 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x7 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x8 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x9 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x10 = Var(within=Reals, bounds=(None,None), initialize=0)

m.obj = Objective(sense=maximize, expr= m.x10)

m.e1 = Constraint(expr= (m.x1 - m.x2)**2 + (m.x4 - m.x5)**2 - (m.x7 + m.x8)**2
    >= 0)
m.e2 = Constraint(expr= (m.x1 - m.x3)**2 + (m.x4 - m.x6)**2 - (m.x7 + m.x9)**2
    >= 0)
m.e3 = Constraint(expr= (m.x2 - m.x3)**2 + (m.x5 - m.x6)**2 - (m.x8 + m.x9)**2
    >= 0)
m.e4 = Constraint(expr= m.x7 - m.x10 == 0)
m.e5 = Constraint(expr= m.x8 - m.x10 == 0)
m.e6 = Constraint(expr= m.x9 - m.x10 == 0)
m.e7 = Constraint(expr= m.x1**2 + m.x4**2 - (1 - m.x7)**2 <= 0)
m.e8 = Constraint(expr= m.x2**2 + m.x5**2 - (1 - m.x8)**2 <= 0)
m.e9 = Constraint(expr= m.x3**2 + m.x6**2 - (1 - m.x9)**2 <= 0)
