# NLP written by GAMS Convert at 03/17/24 14:47:59
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#        20        0       15        5        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        18       18        0        0        0        0        0        0
# FX      6
#
# Nonzero counts
#     Total    const       NL
#       100       10       90
#
# Reformulation has removed 1 variable and 1 equation

from pyomo.environ import *

model = m = ConcreteModel()

m.x1 = Var(within=Reals, bounds=(0,0), initialize=0)
m.x2 = Var(within=Reals, bounds=(0,0), initialize=0)
m.x3 = Var(within=Reals, bounds=(0,0), initialize=0)
m.x4 = Var(within=Reals, bounds=(0,5), initialize=0)
m.x5 = Var(within=Reals, bounds=(0,5), initialize=0)
m.x6 = Var(within=Reals, bounds=(0,5), initialize=0)
m.x7 = Var(within=Reals, bounds=(0,0), initialize=0)
m.x8 = Var(within=Reals, bounds=(0,0), initialize=0)
m.x9 = Var(within=Reals, bounds=(-5,5), initialize=0)
m.x10 = Var(within=Reals, bounds=(-5,5), initialize=0)
m.x11 = Var(within=Reals, bounds=(-5,5), initialize=0)
m.x12 = Var(within=Reals, bounds=(-5,5), initialize=0)
m.x13 = Var(within=Reals, bounds=(0,0), initialize=0)
m.x14 = Var(within=Reals, bounds=(-5,5), initialize=0)
m.x15 = Var(within=Reals, bounds=(-5,5), initialize=0)
m.x16 = Var(within=Reals, bounds=(-5,5), initialize=0)
m.x17 = Var(within=Reals, bounds=(-5,5), initialize=0)
m.x18 = Var(within=Reals, bounds=(-5,5), initialize=0)

m.obj = Objective(sense=minimize, expr= exp(-6 * sqrt((m.x1 - m.x2)**2 + (m.x7
    - m.x8)**2 + (m.x13 - m.x14)**2) + 6) * (exp(-6 * sqrt((m.x1 - m.x2)**2 +
    (m.x7 - m.x8)**2 + (m.x13 - m.x14)**2) + 6) - 2) + exp(-6 * sqrt((m.x1 -
    m.x3)**2 + (m.x7 - m.x9)**2 + (m.x13 - m.x15)**2) + 6) * (exp(-6 * sqrt((
    m.x1 - m.x3)**2 + (m.x7 - m.x9)**2 + (m.x13 - m.x15)**2) + 6) - 2) + exp(-6
    * sqrt((m.x1 - m.x4)**2 + (m.x7 - m.x10)**2 + (m.x13 - m.x16)**2) + 6) * (
    exp(-6 * sqrt((m.x1 - m.x4)**2 + (m.x7 - m.x10)**2 + (m.x13 - m.x16)**2) +
    6) - 2) + exp(-6 * sqrt((m.x1 - m.x5)**2 + (m.x7 - m.x11)**2 + (m.x13 -
    m.x17)**2) + 6) * (exp(-6 * sqrt((m.x1 - m.x5)**2 + (m.x7 - m.x11)**2 + (
    m.x13 - m.x17)**2) + 6) - 2) + exp(-6 * sqrt((m.x1 - m.x6)**2 + (m.x7 -
    m.x12)**2 + (m.x13 - m.x18)**2) + 6) * (exp(-6 * sqrt((m.x1 - m.x6)**2 + (
    m.x7 - m.x12)**2 + (m.x13 - m.x18)**2) + 6) - 2) + exp(-6 * sqrt((m.x2 -
    m.x3)**2 + (m.x8 - m.x9)**2 + (m.x14 - m.x15)**2) + 6) * (exp(-6 * sqrt((
    m.x2 - m.x3)**2 + (m.x8 - m.x9)**2 + (m.x14 - m.x15)**2) + 6) - 2) + exp(-6
    * sqrt((m.x2 - m.x4)**2 + (m.x8 - m.x10)**2 + (m.x14 - m.x16)**2) + 6) * (
    exp(-6 * sqrt((m.x2 - m.x4)**2 + (m.x8 - m.x10)**2 + (m.x14 - m.x16)**2) +
    6) - 2) + exp(-6 * sqrt((m.x2 - m.x5)**2 + (m.x8 - m.x11)**2 + (m.x14 -
    m.x17)**2) + 6) * (exp(-6 * sqrt((m.x2 - m.x5)**2 + (m.x8 - m.x11)**2 + (
    m.x14 - m.x17)**2) + 6) - 2) + exp(-6 * sqrt((m.x2 - m.x6)**2 + (m.x8 -
    m.x12)**2 + (m.x14 - m.x18)**2) + 6) * (exp(-6 * sqrt((m.x2 - m.x6)**2 + (
    m.x8 - m.x12)**2 + (m.x14 - m.x18)**2) + 6) - 2) + exp(-6 * sqrt((m.x3 -
    m.x4)**2 + (m.x9 - m.x10)**2 + (m.x15 - m.x16)**2) + 6) * (exp(-6 * sqrt((
    m.x3 - m.x4)**2 + (m.x9 - m.x10)**2 + (m.x15 - m.x16)**2) + 6) - 2) + exp(-
    6 * sqrt((m.x3 - m.x5)**2 + (m.x9 - m.x11)**2 + (m.x15 - m.x17)**2) + 6) *
    (exp(-6 * sqrt((m.x3 - m.x5)**2 + (m.x9 - m.x11)**2 + (m.x15 - m.x17)**2)
    + 6) - 2) + exp(-6 * sqrt((m.x3 - m.x6)**2 + (m.x9 - m.x12)**2 + (m.x15 -
    m.x18)**2) + 6) * (exp(-6 * sqrt((m.x3 - m.x6)**2 + (m.x9 - m.x12)**2 + (
    m.x15 - m.x18)**2) + 6) - 2) + exp(-6 * sqrt((m.x4 - m.x5)**2 + (m.x10 -
    m.x11)**2 + (m.x16 - m.x17)**2) + 6) * (exp(-6 * sqrt((m.x4 - m.x5)**2 + (
    m.x10 - m.x11)**2 + (m.x16 - m.x17)**2) + 6) - 2) + exp(-6 * sqrt((m.x4 -
    m.x6)**2 + (m.x10 - m.x12)**2 + (m.x16 - m.x18)**2) + 6) * (exp(-6 * sqrt((
    m.x4 - m.x6)**2 + (m.x10 - m.x12)**2 + (m.x16 - m.x18)**2) + 6) - 2) + exp(
    -6 * sqrt((m.x5 - m.x6)**2 + (m.x11 - m.x12)**2 + (m.x17 - m.x18)**2) + 6)
    * (exp(-6 * sqrt((m.x5 - m.x6)**2 + (m.x11 - m.x12)**2 + (m.x17 - m.x18)**
    2) + 6) - 2))

m.e1 = Constraint(expr= (m.x1 - m.x2)**2 + (m.x7 - m.x8)**2 + (m.x13 - m.x14)**
    2 >= 0.32159900740899994)
m.e2 = Constraint(expr= (m.x1 - m.x3)**2 + (m.x7 - m.x9)**2 + (m.x13 - m.x15)**
    2 >= 0.32159900740899994)
m.e3 = Constraint(expr= (m.x1 - m.x4)**2 + (m.x7 - m.x10)**2 + (m.x13 - m.x16)
    **2 >= 0.32159900740899994)
m.e4 = Constraint(expr= (m.x1 - m.x5)**2 + (m.x7 - m.x11)**2 + (m.x13 - m.x17)
    **2 >= 0.32159900740899994)
m.e5 = Constraint(expr= (m.x1 - m.x6)**2 + (m.x7 - m.x12)**2 + (m.x13 - m.x18)
    **2 >= 0.32159900740899994)
m.e6 = Constraint(expr= (m.x2 - m.x3)**2 + (m.x8 - m.x9)**2 + (m.x14 - m.x15)**
    2 >= 0.32159900740899994)
m.e7 = Constraint(expr= (m.x2 - m.x4)**2 + (m.x8 - m.x10)**2 + (m.x14 - m.x16)
    **2 >= 0.32159900740899994)
m.e8 = Constraint(expr= (m.x2 - m.x5)**2 + (m.x8 - m.x11)**2 + (m.x14 - m.x17)
    **2 >= 0.32159900740899994)
m.e9 = Constraint(expr= (m.x2 - m.x6)**2 + (m.x8 - m.x12)**2 + (m.x14 - m.x18)
    **2 >= 0.32159900740899994)
m.e10 = Constraint(expr= (m.x3 - m.x4)**2 + (m.x9 - m.x10)**2 + (m.x15 - m.x16)
    **2 >= 0.32159900740899994)
m.e11 = Constraint(expr= (m.x3 - m.x5)**2 + (m.x9 - m.x11)**2 + (m.x15 - m.x17)
    **2 >= 0.32159900740899994)
m.e12 = Constraint(expr= (m.x3 - m.x6)**2 + (m.x9 - m.x12)**2 + (m.x15 - m.x18)
    **2 >= 0.32159900740899994)
m.e13 = Constraint(expr= (m.x4 - m.x5)**2 + (m.x10 - m.x11)**2 + (m.x16 - m.x17)
    **2 >= 0.32159900740899994)
m.e14 = Constraint(expr= (m.x4 - m.x6)**2 + (m.x10 - m.x12)**2 + (m.x16 - m.x18)
    **2 >= 0.32159900740899994)
m.e15 = Constraint(expr= (m.x5 - m.x6)**2 + (m.x11 - m.x12)**2 + (m.x17 - m.x18)
    **2 >= 0.32159900740899994)
m.e16 = Constraint(expr= m.x1 - m.x2 <= 0)
m.e17 = Constraint(expr= m.x2 - m.x3 <= 0)
m.e18 = Constraint(expr= m.x3 - m.x4 <= 0)
m.e19 = Constraint(expr= m.x4 - m.x5 <= 0)
m.e20 = Constraint(expr= m.x5 - m.x6 <= 0)
