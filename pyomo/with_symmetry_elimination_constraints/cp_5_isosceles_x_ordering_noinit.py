# NLP written by GAMS Convert at 03/17/24 14:47:59
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#        29        0       25        4        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        11       11        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#        93       43       50
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
m.x7 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x8 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x9 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x10 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x11 = Var(within=Reals, bounds=(None,None), initialize=0)

m.obj = Objective(sense=maximize, expr= m.x11)

m.e1 = Constraint(expr= (m.x1 - m.x2)**2 + (m.x6 - m.x7)**2 - (2 * m.x11)**2
    >= 0)
m.e2 = Constraint(expr= (m.x1 - m.x3)**2 + (m.x6 - m.x8)**2 - (2 * m.x11)**2
    >= 0)
m.e3 = Constraint(expr= (m.x1 - m.x4)**2 + (m.x6 - m.x9)**2 - (2 * m.x11)**2
    >= 0)
m.e4 = Constraint(expr= (m.x1 - m.x5)**2 + (m.x6 - m.x10)**2 - (2 * m.x11)**2
    >= 0)
m.e5 = Constraint(expr= (m.x2 - m.x3)**2 + (m.x7 - m.x8)**2 - (2 * m.x11)**2
    >= 0)
m.e6 = Constraint(expr= (m.x2 - m.x4)**2 + (m.x7 - m.x9)**2 - (2 * m.x11)**2
    >= 0)
m.e7 = Constraint(expr= (m.x2 - m.x5)**2 + (m.x7 - m.x10)**2 - (2 * m.x11)**2
    >= 0)
m.e8 = Constraint(expr= (m.x3 - m.x4)**2 + (m.x8 - m.x9)**2 - (2 * m.x11)**2
    >= 0)
m.e9 = Constraint(expr= (m.x3 - m.x5)**2 + (m.x8 - m.x10)**2 - (2 * m.x11)**2
    >= 0)
m.e10 = Constraint(expr= (m.x4 - m.x5)**2 + (m.x9 - m.x10)**2 - (2 * m.x11)**2
    >= 0)
m.e11 = Constraint(expr= m.x1 - m.x2 <= 0)
m.e12 = Constraint(expr= m.x2 - m.x3 <= 0)
m.e13 = Constraint(expr= m.x3 - m.x4 <= 0)
m.e14 = Constraint(expr= m.x4 - m.x5 <= 0)
m.e15 = Constraint(expr= m.x1 - m.x11 >= 0)
m.e16 = Constraint(expr= m.x2 - m.x11 >= 0)
m.e17 = Constraint(expr= m.x3 - m.x11 >= 0)
m.e18 = Constraint(expr= m.x4 - m.x11 >= 0)
m.e19 = Constraint(expr= m.x5 - m.x11 >= 0)
m.e20 = Constraint(expr= m.x6 - m.x11 >= 0)
m.e21 = Constraint(expr= m.x7 - m.x11 >= 0)
m.e22 = Constraint(expr= m.x8 - m.x11 >= 0)
m.e23 = Constraint(expr= m.x9 - m.x11 >= 0)
m.e24 = Constraint(expr= m.x10 - m.x11 >= 0)
m.e25 = Constraint(expr= -0.7071067811865475 * m.x1 - 0.7071067811865475 * m.x6
    - m.x11 >= -0.7071067811865475)
m.e26 = Constraint(expr= -0.7071067811865475 * m.x2 - 0.7071067811865475 * m.x7
    - m.x11 >= -0.7071067811865475)
m.e27 = Constraint(expr= -0.7071067811865475 * m.x3 - 0.7071067811865475 * m.x8
    - m.x11 >= -0.7071067811865475)
m.e28 = Constraint(expr= -0.7071067811865475 * m.x4 - 0.7071067811865475 * m.x9
    - m.x11 >= -0.7071067811865475)
m.e29 = Constraint(expr= -0.7071067811865475 * m.x5 - 0.7071067811865475 *
    m.x10 - m.x11 >= -0.7071067811865475)