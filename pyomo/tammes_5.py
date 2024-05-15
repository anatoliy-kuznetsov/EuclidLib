# NLP written by GAMS Convert at 05/15/24 11:45:06
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#        15        5        0       10        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        16       16        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#        85       10       75
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
m.x7 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x8 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x9 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x10 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x11 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x12 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x13 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x14 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x15 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x16 = Var(within=Reals, bounds=(None,None), initialize=0)

m.obj = Objective(sense=maximize, expr= m.x16)

m.e1 = Constraint(expr= m.x1**2 + m.x6**2 + m.x11**2 == 1)
m.e2 = Constraint(expr= m.x2**2 + m.x7**2 + m.x12**2 == 1)
m.e3 = Constraint(expr= m.x3**2 + m.x8**2 + m.x13**2 == 1)
m.e4 = Constraint(expr= m.x4**2 + m.x9**2 + m.x14**2 == 1)
m.e5 = Constraint(expr= m.x5**2 + m.x10**2 + m.x15**2 == 1)
m.e6 = Constraint(expr= -sqrt((m.x1 - m.x2)**2 + (m.x6 - m.x7)**2 + (m.x11 -
    m.x12)**2) + m.x16 <= 0)
m.e7 = Constraint(expr= -sqrt((m.x1 - m.x3)**2 + (m.x6 - m.x8)**2 + (m.x11 -
    m.x13)**2) + m.x16 <= 0)
m.e8 = Constraint(expr= -sqrt((m.x1 - m.x4)**2 + (m.x6 - m.x9)**2 + (m.x11 -
    m.x14)**2) + m.x16 <= 0)
m.e9 = Constraint(expr= -sqrt((m.x1 - m.x5)**2 + (m.x6 - m.x10)**2 + (m.x11 -
    m.x15)**2) + m.x16 <= 0)
m.e10 = Constraint(expr= -sqrt((m.x2 - m.x3)**2 + (m.x7 - m.x8)**2 + (m.x12 -
    m.x13)**2) + m.x16 <= 0)
m.e11 = Constraint(expr= -sqrt((m.x2 - m.x4)**2 + (m.x7 - m.x9)**2 + (m.x12 -
    m.x14)**2) + m.x16 <= 0)
m.e12 = Constraint(expr= -sqrt((m.x2 - m.x5)**2 + (m.x7 - m.x10)**2 + (m.x12 -
    m.x15)**2) + m.x16 <= 0)
m.e13 = Constraint(expr= -sqrt((m.x3 - m.x4)**2 + (m.x8 - m.x9)**2 + (m.x13 -
    m.x14)**2) + m.x16 <= 0)
m.e14 = Constraint(expr= -sqrt((m.x3 - m.x5)**2 + (m.x8 - m.x10)**2 + (m.x13 -
    m.x15)**2) + m.x16 <= 0)
m.e15 = Constraint(expr= -sqrt((m.x4 - m.x5)**2 + (m.x9 - m.x10)**2 + (m.x14 -
    m.x15)**2) + m.x16 <= 0)
