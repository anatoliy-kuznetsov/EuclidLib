# NLP written by GAMS Convert at 05/15/24 11:48:16
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#        36        0       36        0        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        27       27        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       216        0      216
#
# Reformulation has removed 1 variable and 1 equation

from pyomo.environ import *

model = m = ConcreteModel()

m.x1 = Var(within=Reals, bounds=(0,8), initialize=0)
m.x2 = Var(within=Reals, bounds=(0,8), initialize=0)
m.x3 = Var(within=Reals, bounds=(0,8), initialize=0)
m.x4 = Var(within=Reals, bounds=(0,8), initialize=0)
m.x5 = Var(within=Reals, bounds=(0,8), initialize=0)
m.x6 = Var(within=Reals, bounds=(0,8), initialize=0)
m.x7 = Var(within=Reals, bounds=(0,8), initialize=0)
m.x8 = Var(within=Reals, bounds=(0,8), initialize=0)
m.x9 = Var(within=Reals, bounds=(0,8), initialize=0)
m.x10 = Var(within=Reals, bounds=(-8,8), initialize=0)
m.x11 = Var(within=Reals, bounds=(-8,8), initialize=0)
m.x12 = Var(within=Reals, bounds=(-8,8), initialize=0)
m.x13 = Var(within=Reals, bounds=(-8,8), initialize=0)
m.x14 = Var(within=Reals, bounds=(-8,8), initialize=0)
m.x15 = Var(within=Reals, bounds=(-8,8), initialize=0)
m.x16 = Var(within=Reals, bounds=(-8,8), initialize=0)
m.x17 = Var(within=Reals, bounds=(-8,8), initialize=0)
m.x18 = Var(within=Reals, bounds=(-8,8), initialize=0)
m.x19 = Var(within=Reals, bounds=(-8,8), initialize=0)
m.x20 = Var(within=Reals, bounds=(-8,8), initialize=0)
m.x21 = Var(within=Reals, bounds=(-8,8), initialize=0)
m.x22 = Var(within=Reals, bounds=(-8,8), initialize=0)
m.x23 = Var(within=Reals, bounds=(-8,8), initialize=0)
m.x24 = Var(within=Reals, bounds=(-8,8), initialize=0)
m.x25 = Var(within=Reals, bounds=(-8,8), initialize=0)
m.x26 = Var(within=Reals, bounds=(-8,8), initialize=0)
m.x27 = Var(within=Reals, bounds=(-8,8), initialize=0)

m.obj = Objective(sense=minimize, expr= exp(-6 * sqrt((m.x1 - m.x2)**2 + (m.x10
    - m.x11)**2 + (m.x19 - m.x20)**2) + 6) * (exp(-6 * sqrt((m.x1 - m.x2)**2
    + (m.x10 - m.x11)**2 + (m.x19 - m.x20)**2) + 6) - 2) + exp(-6 * sqrt((m.x1
    - m.x3)**2 + (m.x10 - m.x12)**2 + (m.x19 - m.x21)**2) + 6) * (exp(-6 *
    sqrt((m.x1 - m.x3)**2 + (m.x10 - m.x12)**2 + (m.x19 - m.x21)**2) + 6) - 2)
    + exp(-6 * sqrt((m.x1 - m.x4)**2 + (m.x10 - m.x13)**2 + (m.x19 - m.x22)**2)
    + 6) * (exp(-6 * sqrt((m.x1 - m.x4)**2 + (m.x10 - m.x13)**2 + (m.x19 -
    m.x22)**2) + 6) - 2) + exp(-6 * sqrt((m.x1 - m.x5)**2 + (m.x10 - m.x14)**2
    + (m.x19 - m.x23)**2) + 6) * (exp(-6 * sqrt((m.x1 - m.x5)**2 + (m.x10 -
    m.x14)**2 + (m.x19 - m.x23)**2) + 6) - 2) + exp(-6 * sqrt((m.x1 - m.x6)**2
    + (m.x10 - m.x15)**2 + (m.x19 - m.x24)**2) + 6) * (exp(-6 * sqrt((m.x1 -
    m.x6)**2 + (m.x10 - m.x15)**2 + (m.x19 - m.x24)**2) + 6) - 2) + exp(-6 *
    sqrt((m.x1 - m.x7)**2 + (m.x10 - m.x16)**2 + (m.x19 - m.x25)**2) + 6) * (
    exp(-6 * sqrt((m.x1 - m.x7)**2 + (m.x10 - m.x16)**2 + (m.x19 - m.x25)**2)
    + 6) - 2) + exp(-6 * sqrt((m.x1 - m.x8)**2 + (m.x10 - m.x17)**2 + (m.x19
    - m.x26)**2) + 6) * (exp(-6 * sqrt((m.x1 - m.x8)**2 + (m.x10 - m.x17)**2
    + (m.x19 - m.x26)**2) + 6) - 2) + exp(-6 * sqrt((m.x1 - m.x9)**2 + (m.x10
    - m.x18)**2 + (m.x19 - m.x27)**2) + 6) * (exp(-6 * sqrt((m.x1 - m.x9)**2
    + (m.x10 - m.x18)**2 + (m.x19 - m.x27)**2) + 6) - 2) + exp(-6 * sqrt((m.x2
    - m.x3)**2 + (m.x11 - m.x12)**2 + (m.x20 - m.x21)**2) + 6) * (exp(-6 *
    sqrt((m.x2 - m.x3)**2 + (m.x11 - m.x12)**2 + (m.x20 - m.x21)**2) + 6) - 2)
    + exp(-6 * sqrt((m.x2 - m.x4)**2 + (m.x11 - m.x13)**2 + (m.x20 - m.x22)**2)
    + 6) * (exp(-6 * sqrt((m.x2 - m.x4)**2 + (m.x11 - m.x13)**2 + (m.x20 -
    m.x22)**2) + 6) - 2) + exp(-6 * sqrt((m.x2 - m.x5)**2 + (m.x11 - m.x14)**2
    + (m.x20 - m.x23)**2) + 6) * (exp(-6 * sqrt((m.x2 - m.x5)**2 + (m.x11 -
    m.x14)**2 + (m.x20 - m.x23)**2) + 6) - 2) + exp(-6 * sqrt((m.x2 - m.x6)**2
    + (m.x11 - m.x15)**2 + (m.x20 - m.x24)**2) + 6) * (exp(-6 * sqrt((m.x2 -
    m.x6)**2 + (m.x11 - m.x15)**2 + (m.x20 - m.x24)**2) + 6) - 2) + exp(-6 *
    sqrt((m.x2 - m.x7)**2 + (m.x11 - m.x16)**2 + (m.x20 - m.x25)**2) + 6) * (
    exp(-6 * sqrt((m.x2 - m.x7)**2 + (m.x11 - m.x16)**2 + (m.x20 - m.x25)**2)
    + 6) - 2) + exp(-6 * sqrt((m.x2 - m.x8)**2 + (m.x11 - m.x17)**2 + (m.x20
    - m.x26)**2) + 6) * (exp(-6 * sqrt((m.x2 - m.x8)**2 + (m.x11 - m.x17)**2
    + (m.x20 - m.x26)**2) + 6) - 2) + exp(-6 * sqrt((m.x2 - m.x9)**2 + (m.x11
    - m.x18)**2 + (m.x20 - m.x27)**2) + 6) * (exp(-6 * sqrt((m.x2 - m.x9)**2
    + (m.x11 - m.x18)**2 + (m.x20 - m.x27)**2) + 6) - 2) + exp(-6 * sqrt((m.x3
    - m.x4)**2 + (m.x12 - m.x13)**2 + (m.x21 - m.x22)**2) + 6) * (exp(-6 *
    sqrt((m.x3 - m.x4)**2 + (m.x12 - m.x13)**2 + (m.x21 - m.x22)**2) + 6) - 2)
    + exp(-6 * sqrt((m.x3 - m.x5)**2 + (m.x12 - m.x14)**2 + (m.x21 - m.x23)**2)
    + 6) * (exp(-6 * sqrt((m.x3 - m.x5)**2 + (m.x12 - m.x14)**2 + (m.x21 -
    m.x23)**2) + 6) - 2) + exp(-6 * sqrt((m.x3 - m.x6)**2 + (m.x12 - m.x15)**2
    + (m.x21 - m.x24)**2) + 6) * (exp(-6 * sqrt((m.x3 - m.x6)**2 + (m.x12 -
    m.x15)**2 + (m.x21 - m.x24)**2) + 6) - 2) + exp(-6 * sqrt((m.x3 - m.x7)**2
    + (m.x12 - m.x16)**2 + (m.x21 - m.x25)**2) + 6) * (exp(-6 * sqrt((m.x3 -
    m.x7)**2 + (m.x12 - m.x16)**2 + (m.x21 - m.x25)**2) + 6) - 2) + exp(-6 *
    sqrt((m.x3 - m.x8)**2 + (m.x12 - m.x17)**2 + (m.x21 - m.x26)**2) + 6) * (
    exp(-6 * sqrt((m.x3 - m.x8)**2 + (m.x12 - m.x17)**2 + (m.x21 - m.x26)**2)
    + 6) - 2) + exp(-6 * sqrt((m.x3 - m.x9)**2 + (m.x12 - m.x18)**2 + (m.x21
    - m.x27)**2) + 6) * (exp(-6 * sqrt((m.x3 - m.x9)**2 + (m.x12 - m.x18)**2
    + (m.x21 - m.x27)**2) + 6) - 2) + exp(-6 * sqrt((m.x4 - m.x5)**2 + (m.x13
    - m.x14)**2 + (m.x22 - m.x23)**2) + 6) * (exp(-6 * sqrt((m.x4 - m.x5)**2
    + (m.x13 - m.x14)**2 + (m.x22 - m.x23)**2) + 6) - 2) + exp(-6 * sqrt((m.x4
    - m.x6)**2 + (m.x13 - m.x15)**2 + (m.x22 - m.x24)**2) + 6) * (exp(-6 *
    sqrt((m.x4 - m.x6)**2 + (m.x13 - m.x15)**2 + (m.x22 - m.x24)**2) + 6) - 2)
    + exp(-6 * sqrt((m.x4 - m.x7)**2 + (m.x13 - m.x16)**2 + (m.x22 - m.x25)**2)
    + 6) * (exp(-6 * sqrt((m.x4 - m.x7)**2 + (m.x13 - m.x16)**2 + (m.x22 -
    m.x25)**2) + 6) - 2) + exp(-6 * sqrt((m.x4 - m.x8)**2 + (m.x13 - m.x17)**2
    + (m.x22 - m.x26)**2) + 6) * (exp(-6 * sqrt((m.x4 - m.x8)**2 + (m.x13 -
    m.x17)**2 + (m.x22 - m.x26)**2) + 6) - 2) + exp(-6 * sqrt((m.x4 - m.x9)**2
    + (m.x13 - m.x18)**2 + (m.x22 - m.x27)**2) + 6) * (exp(-6 * sqrt((m.x4 -
    m.x9)**2 + (m.x13 - m.x18)**2 + (m.x22 - m.x27)**2) + 6) - 2) + exp(-6 *
    sqrt((m.x5 - m.x6)**2 + (m.x14 - m.x15)**2 + (m.x23 - m.x24)**2) + 6) * (
    exp(-6 * sqrt((m.x5 - m.x6)**2 + (m.x14 - m.x15)**2 + (m.x23 - m.x24)**2)
    + 6) - 2) + exp(-6 * sqrt((m.x5 - m.x7)**2 + (m.x14 - m.x16)**2 + (m.x23
    - m.x25)**2) + 6) * (exp(-6 * sqrt((m.x5 - m.x7)**2 + (m.x14 - m.x16)**2
    + (m.x23 - m.x25)**2) + 6) - 2) + exp(-6 * sqrt((m.x5 - m.x8)**2 + (m.x14
    - m.x17)**2 + (m.x23 - m.x26)**2) + 6) * (exp(-6 * sqrt((m.x5 - m.x8)**2
    + (m.x14 - m.x17)**2 + (m.x23 - m.x26)**2) + 6) - 2) + exp(-6 * sqrt((m.x5
    - m.x9)**2 + (m.x14 - m.x18)**2 + (m.x23 - m.x27)**2) + 6) * (exp(-6 *
    sqrt((m.x5 - m.x9)**2 + (m.x14 - m.x18)**2 + (m.x23 - m.x27)**2) + 6) - 2)
    + exp(-6 * sqrt((m.x6 - m.x7)**2 + (m.x15 - m.x16)**2 + (m.x24 - m.x25)**2)
    + 6) * (exp(-6 * sqrt((m.x6 - m.x7)**2 + (m.x15 - m.x16)**2 + (m.x24 -
    m.x25)**2) + 6) - 2) + exp(-6 * sqrt((m.x6 - m.x8)**2 + (m.x15 - m.x17)**2
    + (m.x24 - m.x26)**2) + 6) * (exp(-6 * sqrt((m.x6 - m.x8)**2 + (m.x15 -
    m.x17)**2 + (m.x24 - m.x26)**2) + 6) - 2) + exp(-6 * sqrt((m.x6 - m.x9)**2
    + (m.x15 - m.x18)**2 + (m.x24 - m.x27)**2) + 6) * (exp(-6 * sqrt((m.x6 -
    m.x9)**2 + (m.x15 - m.x18)**2 + (m.x24 - m.x27)**2) + 6) - 2) + exp(-6 *
    sqrt((m.x7 - m.x8)**2 + (m.x16 - m.x17)**2 + (m.x25 - m.x26)**2) + 6) * (
    exp(-6 * sqrt((m.x7 - m.x8)**2 + (m.x16 - m.x17)**2 + (m.x25 - m.x26)**2)
    + 6) - 2) + exp(-6 * sqrt((m.x7 - m.x9)**2 + (m.x16 - m.x18)**2 + (m.x25
    - m.x27)**2) + 6) * (exp(-6 * sqrt((m.x7 - m.x9)**2 + (m.x16 - m.x18)**2
    + (m.x25 - m.x27)**2) + 6) - 2) + exp(-6 * sqrt((m.x8 - m.x9)**2 + (m.x17
    - m.x18)**2 + (m.x26 - m.x27)**2) + 6) * (exp(-6 * sqrt((m.x8 - m.x9)**2
    + (m.x17 - m.x18)**2 + (m.x26 - m.x27)**2) + 6) - 2))

m.e1 = Constraint(expr= (m.x1 - m.x2)**2 + (m.x10 - m.x11)**2 + (m.x19 - m.x20)
    **2 >= 0.32159900740899994)
m.e2 = Constraint(expr= (m.x1 - m.x3)**2 + (m.x10 - m.x12)**2 + (m.x19 - m.x21)
    **2 >= 0.32159900740899994)
m.e3 = Constraint(expr= (m.x1 - m.x4)**2 + (m.x10 - m.x13)**2 + (m.x19 - m.x22)
    **2 >= 0.32159900740899994)
m.e4 = Constraint(expr= (m.x1 - m.x5)**2 + (m.x10 - m.x14)**2 + (m.x19 - m.x23)
    **2 >= 0.32159900740899994)
m.e5 = Constraint(expr= (m.x1 - m.x6)**2 + (m.x10 - m.x15)**2 + (m.x19 - m.x24)
    **2 >= 0.32159900740899994)
m.e6 = Constraint(expr= (m.x1 - m.x7)**2 + (m.x10 - m.x16)**2 + (m.x19 - m.x25)
    **2 >= 0.32159900740899994)
m.e7 = Constraint(expr= (m.x1 - m.x8)**2 + (m.x10 - m.x17)**2 + (m.x19 - m.x26)
    **2 >= 0.32159900740899994)
m.e8 = Constraint(expr= (m.x1 - m.x9)**2 + (m.x10 - m.x18)**2 + (m.x19 - m.x27)
    **2 >= 0.32159900740899994)
m.e9 = Constraint(expr= (m.x2 - m.x3)**2 + (m.x11 - m.x12)**2 + (m.x20 - m.x21)
    **2 >= 0.32159900740899994)
m.e10 = Constraint(expr= (m.x2 - m.x4)**2 + (m.x11 - m.x13)**2 + (m.x20 - m.x22)
    **2 >= 0.32159900740899994)
m.e11 = Constraint(expr= (m.x2 - m.x5)**2 + (m.x11 - m.x14)**2 + (m.x20 - m.x23)
    **2 >= 0.32159900740899994)
m.e12 = Constraint(expr= (m.x2 - m.x6)**2 + (m.x11 - m.x15)**2 + (m.x20 - m.x24)
    **2 >= 0.32159900740899994)
m.e13 = Constraint(expr= (m.x2 - m.x7)**2 + (m.x11 - m.x16)**2 + (m.x20 - m.x25)
    **2 >= 0.32159900740899994)
m.e14 = Constraint(expr= (m.x2 - m.x8)**2 + (m.x11 - m.x17)**2 + (m.x20 - m.x26)
    **2 >= 0.32159900740899994)
m.e15 = Constraint(expr= (m.x2 - m.x9)**2 + (m.x11 - m.x18)**2 + (m.x20 - m.x27)
    **2 >= 0.32159900740899994)
m.e16 = Constraint(expr= (m.x3 - m.x4)**2 + (m.x12 - m.x13)**2 + (m.x21 - m.x22)
    **2 >= 0.32159900740899994)
m.e17 = Constraint(expr= (m.x3 - m.x5)**2 + (m.x12 - m.x14)**2 + (m.x21 - m.x23)
    **2 >= 0.32159900740899994)
m.e18 = Constraint(expr= (m.x3 - m.x6)**2 + (m.x12 - m.x15)**2 + (m.x21 - m.x24)
    **2 >= 0.32159900740899994)
m.e19 = Constraint(expr= (m.x3 - m.x7)**2 + (m.x12 - m.x16)**2 + (m.x21 - m.x25)
    **2 >= 0.32159900740899994)
m.e20 = Constraint(expr= (m.x3 - m.x8)**2 + (m.x12 - m.x17)**2 + (m.x21 - m.x26)
    **2 >= 0.32159900740899994)
m.e21 = Constraint(expr= (m.x3 - m.x9)**2 + (m.x12 - m.x18)**2 + (m.x21 - m.x27)
    **2 >= 0.32159900740899994)
m.e22 = Constraint(expr= (m.x4 - m.x5)**2 + (m.x13 - m.x14)**2 + (m.x22 - m.x23)
    **2 >= 0.32159900740899994)
m.e23 = Constraint(expr= (m.x4 - m.x6)**2 + (m.x13 - m.x15)**2 + (m.x22 - m.x24)
    **2 >= 0.32159900740899994)
m.e24 = Constraint(expr= (m.x4 - m.x7)**2 + (m.x13 - m.x16)**2 + (m.x22 - m.x25)
    **2 >= 0.32159900740899994)
m.e25 = Constraint(expr= (m.x4 - m.x8)**2 + (m.x13 - m.x17)**2 + (m.x22 - m.x26)
    **2 >= 0.32159900740899994)
m.e26 = Constraint(expr= (m.x4 - m.x9)**2 + (m.x13 - m.x18)**2 + (m.x22 - m.x27)
    **2 >= 0.32159900740899994)
m.e27 = Constraint(expr= (m.x5 - m.x6)**2 + (m.x14 - m.x15)**2 + (m.x23 - m.x24)
    **2 >= 0.32159900740899994)
m.e28 = Constraint(expr= (m.x5 - m.x7)**2 + (m.x14 - m.x16)**2 + (m.x23 - m.x25)
    **2 >= 0.32159900740899994)
m.e29 = Constraint(expr= (m.x5 - m.x8)**2 + (m.x14 - m.x17)**2 + (m.x23 - m.x26)
    **2 >= 0.32159900740899994)
m.e30 = Constraint(expr= (m.x5 - m.x9)**2 + (m.x14 - m.x18)**2 + (m.x23 - m.x27)
    **2 >= 0.32159900740899994)
m.e31 = Constraint(expr= (m.x6 - m.x7)**2 + (m.x15 - m.x16)**2 + (m.x24 - m.x25)
    **2 >= 0.32159900740899994)
m.e32 = Constraint(expr= (m.x6 - m.x8)**2 + (m.x15 - m.x17)**2 + (m.x24 - m.x26)
    **2 >= 0.32159900740899994)
m.e33 = Constraint(expr= (m.x6 - m.x9)**2 + (m.x15 - m.x18)**2 + (m.x24 - m.x27)
    **2 >= 0.32159900740899994)
m.e34 = Constraint(expr= (m.x7 - m.x8)**2 + (m.x16 - m.x17)**2 + (m.x25 - m.x26)
    **2 >= 0.32159900740899994)
m.e35 = Constraint(expr= (m.x7 - m.x9)**2 + (m.x16 - m.x18)**2 + (m.x25 - m.x27)
    **2 >= 0.32159900740899994)
m.e36 = Constraint(expr= (m.x8 - m.x9)**2 + (m.x17 - m.x18)**2 + (m.x26 - m.x27)
    **2 >= 0.32159900740899994)
