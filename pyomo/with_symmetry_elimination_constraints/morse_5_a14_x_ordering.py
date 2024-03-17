# NLP written by GAMS Convert at 03/17/24 14:48:04
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#        14        0       10        4        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        15       15        0        0        0        0        0        0
# FX      6
#
# Nonzero counts
#     Total    const       NL
#        68        8       60
#
# Reformulation has removed 1 variable and 1 equation

from pyomo.environ import *

model = m = ConcreteModel()

m.x1 = Var(within=Reals, bounds=(0,0), initialize=0)
m.x2 = Var(within=Reals, bounds=(0,0), initialize=0)
m.x3 = Var(within=Reals, bounds=(0,0), initialize=0)
m.x4 = Var(within=Reals, bounds=(0,4), initialize=0)
m.x5 = Var(within=Reals, bounds=(0,4), initialize=0)
m.x6 = Var(within=Reals, bounds=(0,0), initialize=0)
m.x7 = Var(within=Reals, bounds=(0,0), initialize=0)
m.x8 = Var(within=Reals, bounds=(-4,4), initialize=0)
m.x9 = Var(within=Reals, bounds=(-4,4), initialize=0)
m.x10 = Var(within=Reals, bounds=(-4,4), initialize=0)
m.x11 = Var(within=Reals, bounds=(0,0), initialize=0)
m.x12 = Var(within=Reals, bounds=(-4,4), initialize=0)
m.x13 = Var(within=Reals, bounds=(-4,4), initialize=0)
m.x14 = Var(within=Reals, bounds=(-4,4), initialize=0)
m.x15 = Var(within=Reals, bounds=(-4,4), initialize=0)

m.obj = Objective(sense=minimize, expr= exp(-14 * sqrt((m.x1 - m.x2)**2 + (m.x6
    - m.x7)**2 + (m.x11 - m.x12)**2) + 14) * (exp(-14 * sqrt((m.x1 - m.x2)**2
    + (m.x6 - m.x7)**2 + (m.x11 - m.x12)**2) + 14) - 2) + exp(-14 * sqrt((m.x1
    - m.x3)**2 + (m.x6 - m.x8)**2 + (m.x11 - m.x13)**2) + 14) * (exp(-14 *
    sqrt((m.x1 - m.x3)**2 + (m.x6 - m.x8)**2 + (m.x11 - m.x13)**2) + 14) - 2)
    + exp(-14 * sqrt((m.x1 - m.x4)**2 + (m.x6 - m.x9)**2 + (m.x11 - m.x14)**2)
    + 14) * (exp(-14 * sqrt((m.x1 - m.x4)**2 + (m.x6 - m.x9)**2 + (m.x11 -
    m.x14)**2) + 14) - 2) + exp(-14 * sqrt((m.x1 - m.x5)**2 + (m.x6 - m.x10)**2
    + (m.x11 - m.x15)**2) + 14) * (exp(-14 * sqrt((m.x1 - m.x5)**2 + (m.x6 -
    m.x10)**2 + (m.x11 - m.x15)**2) + 14) - 2) + exp(-14 * sqrt((m.x2 - m.x3)**
    2 + (m.x7 - m.x8)**2 + (m.x12 - m.x13)**2) + 14) * (exp(-14 * sqrt((m.x2 -
    m.x3)**2 + (m.x7 - m.x8)**2 + (m.x12 - m.x13)**2) + 14) - 2) + exp(-14 *
    sqrt((m.x2 - m.x4)**2 + (m.x7 - m.x9)**2 + (m.x12 - m.x14)**2) + 14) * (exp
    (-14 * sqrt((m.x2 - m.x4)**2 + (m.x7 - m.x9)**2 + (m.x12 - m.x14)**2) + 14)
    - 2) + exp(-14 * sqrt((m.x2 - m.x5)**2 + (m.x7 - m.x10)**2 + (m.x12 -
    m.x15)**2) + 14) * (exp(-14 * sqrt((m.x2 - m.x5)**2 + (m.x7 - m.x10)**2 + (
    m.x12 - m.x15)**2) + 14) - 2) + exp(-14 * sqrt((m.x3 - m.x4)**2 + (m.x8 -
    m.x9)**2 + (m.x13 - m.x14)**2) + 14) * (exp(-14 * sqrt((m.x3 - m.x4)**2 + (
    m.x8 - m.x9)**2 + (m.x13 - m.x14)**2) + 14) - 2) + exp(-14 * sqrt((m.x3 -
    m.x5)**2 + (m.x8 - m.x10)**2 + (m.x13 - m.x15)**2) + 14) * (exp(-14 * sqrt(
    (m.x3 - m.x5)**2 + (m.x8 - m.x10)**2 + (m.x13 - m.x15)**2) + 14) - 2) + exp
    (-14 * sqrt((m.x4 - m.x5)**2 + (m.x9 - m.x10)**2 + (m.x14 - m.x15)**2) + 14)
    * (exp(-14 * sqrt((m.x4 - m.x5)**2 + (m.x9 - m.x10)**2 + (m.x14 - m.x15)**
    2) + 14) - 2))

m.e1 = Constraint(expr= (m.x1 - m.x2)**2 + (m.x6 - m.x7)**2 + (m.x11 - m.x12)**
    2 >= 0.7298336158090001)
m.e2 = Constraint(expr= (m.x1 - m.x3)**2 + (m.x6 - m.x8)**2 + (m.x11 - m.x13)**
    2 >= 0.7298336158090001)
m.e3 = Constraint(expr= (m.x1 - m.x4)**2 + (m.x6 - m.x9)**2 + (m.x11 - m.x14)**
    2 >= 0.7298336158090001)
m.e4 = Constraint(expr= (m.x1 - m.x5)**2 + (m.x6 - m.x10)**2 + (m.x11 - m.x15)
    **2 >= 0.7298336158090001)
m.e5 = Constraint(expr= (m.x2 - m.x3)**2 + (m.x7 - m.x8)**2 + (m.x12 - m.x13)**
    2 >= 0.7298336158090001)
m.e6 = Constraint(expr= (m.x2 - m.x4)**2 + (m.x7 - m.x9)**2 + (m.x12 - m.x14)**
    2 >= 0.7298336158090001)
m.e7 = Constraint(expr= (m.x2 - m.x5)**2 + (m.x7 - m.x10)**2 + (m.x12 - m.x15)
    **2 >= 0.7298336158090001)
m.e8 = Constraint(expr= (m.x3 - m.x4)**2 + (m.x8 - m.x9)**2 + (m.x13 - m.x14)**
    2 >= 0.7298336158090001)
m.e9 = Constraint(expr= (m.x3 - m.x5)**2 + (m.x8 - m.x10)**2 + (m.x13 - m.x15)
    **2 >= 0.7298336158090001)
m.e10 = Constraint(expr= (m.x4 - m.x5)**2 + (m.x9 - m.x10)**2 + (m.x14 - m.x15)
    **2 >= 0.7298336158090001)
m.e11 = Constraint(expr= m.x1 - m.x2 <= 0)
m.e12 = Constraint(expr= m.x2 - m.x3 <= 0)
m.e13 = Constraint(expr= m.x3 - m.x4 <= 0)
m.e14 = Constraint(expr= m.x4 - m.x5 <= 0)
