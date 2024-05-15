# MINLP written by GAMS Convert at 05/15/24 12:01:30
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#        28       10       18        0        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        42       24       18        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       117       75       42
#
# Reformulation has removed 1 variable and 1 equation

from pyomo.environ import *

model = m = ConcreteModel()

m.x1 = Var(within=Reals, bounds=(0,1.4142135623730951), initialize=0)
m.x2 = Var(within=Reals, bounds=(0,1.4142135623730951), initialize=0)
m.x3 = Var(within=Reals, bounds=(0,1.4142135623730951), initialize=0)
m.x4 = Var(within=Reals, bounds=(0,1.4142135623730951), initialize=0)
m.x5 = Var(within=Reals, bounds=(0,1.4142135623730951), initialize=0)
m.x6 = Var(within=Reals, bounds=(0,1.4142135623730951), initialize=0)
m.x7 = Var(within=Reals, bounds=(0,1.4142135623730951), initialize=0)
m.x8 = Var(within=Reals, bounds=(0,1.4142135623730951), initialize=0)
m.x9 = Var(within=Reals, bounds=(0,1.4142135623730951), initialize=0)
m.x10 = Var(within=Reals, bounds=(0,1.4142135623730951), initialize=0)
m.x11 = Var(within=Reals, bounds=(0,1.4142135623730951), initialize=0)
m.x12 = Var(within=Reals, bounds=(0,1.4142135623730951), initialize=0)
m.x13 = Var(within=Reals, bounds=(0,1.4142135623730951), initialize=0)
m.x14 = Var(within=Reals, bounds=(0,1.4142135623730951), initialize=0)
m.x15 = Var(within=Reals, bounds=(0,1.4142135623730951), initialize=0)
m.x16 = Var(within=Reals, bounds=(0,1.4142135623730951), initialize=0)
m.x17 = Var(within=Reals, bounds=(0,1.4142135623730951), initialize=0)
m.x18 = Var(within=Reals, bounds=(0,1.4142135623730951), initialize=0)
m.x19 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x20 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x21 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x22 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x23 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x24 = Var(within=Reals, bounds=(0,1), initialize=0)
m.b25 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b26 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b27 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b28 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b29 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b30 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b31 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b32 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b33 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b34 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b35 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b36 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b37 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b38 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b39 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b40 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b41 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b42 = Var(within=Binary, bounds=(0,1), initialize=0)

m.obj = Objective(sense=minimize, expr= m.x1 + m.x2 + m.x3 + m.x4 + m.x5 + m.x6
    + m.x7 + m.x8 + m.x9 + m.x10 + m.x11 + m.x12 + m.x13 + m.x14 + m.x15 +
    m.x16 + m.x17 + m.x18)

m.e1 = Constraint(expr= -sqrt((m.x19 - m.x21)**2 + (m.x20 - m.x22)**2) + m.x1
    - 1.4142135623730951 * m.b25 >= -1.4142135623730951)
m.e2 = Constraint(expr= -sqrt((m.x19 - m.x23)**2 + (m.x20 - m.x24)**2) + m.x2
    - 1.4142135623730951 * m.b26 >= -1.4142135623730951)
m.e3 = Constraint(expr= -sqrt((m.x21 - m.x23)**2 + (m.x22 - m.x24)**2) + m.x3
    - 1.4142135623730951 * m.b27 >= -1.4142135623730951)
m.e4 = Constraint(expr= -sqrt((-0.5714025946899135 + m.x19)**2 + (
    -0.4288890546751146 + m.x20)**2) + m.x4 - 1.4142135623730951 * m.b28
    >= -1.4142135623730951)
m.e5 = Constraint(expr= -sqrt((-0.5780913011344704 + m.x19)**2 + (
    -0.20609823213950174 + m.x20)**2) + m.x5 - 1.4142135623730951 * m.b29
    >= -1.4142135623730951)
m.e6 = Constraint(expr= -sqrt((-0.81332125135732 + m.x19)**2 + (
    -0.8235888725334455 + m.x20)**2) + m.x6 - 1.4142135623730951 * m.b30
    >= -1.4142135623730951)
m.e7 = Constraint(expr= -sqrt((-0.6534725339011758 + m.x19)**2 + (
    -0.16022955651881965 + m.x20)**2) + m.x7 - 1.4142135623730951 * m.b31
    >= -1.4142135623730951)
m.e8 = Constraint(expr= -sqrt((-0.5206693596399246 + m.x19)**2 + (
    -0.32777281162209315 + m.x20)**2) + m.x8 - 1.4142135623730951 * m.b32
    >= -1.4142135623730951)
m.e9 = Constraint(expr= -sqrt((-0.5714025946899135 + m.x21)**2 + (
    -0.4288890546751146 + m.x22)**2) + m.x9 - 1.4142135623730951 * m.b33
    >= -1.4142135623730951)
m.e10 = Constraint(expr= -sqrt((-0.5780913011344704 + m.x21)**2 + (
    -0.20609823213950174 + m.x22)**2) + m.x10 - 1.4142135623730951 * m.b34
    >= -1.4142135623730951)
m.e11 = Constraint(expr= -sqrt((-0.81332125135732 + m.x21)**2 + (
    -0.8235888725334455 + m.x22)**2) + m.x11 - 1.4142135623730951 * m.b35
    >= -1.4142135623730951)
m.e12 = Constraint(expr= -sqrt((-0.6534725339011758 + m.x21)**2 + (
    -0.16022955651881965 + m.x22)**2) + m.x12 - 1.4142135623730951 * m.b36
    >= -1.4142135623730951)
m.e13 = Constraint(expr= -sqrt((-0.5206693596399246 + m.x21)**2 + (
    -0.32777281162209315 + m.x22)**2) + m.x13 - 1.4142135623730951 * m.b37
    >= -1.4142135623730951)
m.e14 = Constraint(expr= -sqrt((-0.5714025946899135 + m.x23)**2 + (
    -0.4288890546751146 + m.x24)**2) + m.x14 - 1.4142135623730951 * m.b38
    >= -1.4142135623730951)
m.e15 = Constraint(expr= -sqrt((-0.5780913011344704 + m.x23)**2 + (
    -0.20609823213950174 + m.x24)**2) + m.x15 - 1.4142135623730951 * m.b39
    >= -1.4142135623730951)
m.e16 = Constraint(expr= -sqrt((-0.81332125135732 + m.x23)**2 + (
    -0.8235888725334455 + m.x24)**2) + m.x16 - 1.4142135623730951 * m.b40
    >= -1.4142135623730951)
m.e17 = Constraint(expr= -sqrt((-0.6534725339011758 + m.x23)**2 + (
    -0.16022955651881965 + m.x24)**2) + m.x17 - 1.4142135623730951 * m.b41
    >= -1.4142135623730951)
m.e18 = Constraint(expr= -sqrt((-0.5206693596399246 + m.x23)**2 + (
    -0.32777281162209315 + m.x24)**2) + m.x18 - 1.4142135623730951 * m.b42
    >= -1.4142135623730951)
m.e19 = Constraint(expr= m.b28 + m.b33 + m.b38 == 1)
m.e20 = Constraint(expr= m.b29 + m.b34 + m.b39 == 1)
m.e21 = Constraint(expr= m.b30 + m.b35 + m.b40 == 1)
m.e22 = Constraint(expr= m.b31 + m.b36 + m.b41 == 1)
m.e23 = Constraint(expr= m.b32 + m.b37 + m.b42 == 1)
m.e24 = Constraint(expr= m.b25 + m.b26 + m.b28 + m.b29 + m.b30 + m.b31 + m.b32
    == 3)
m.e25 = Constraint(expr= m.b25 + m.b27 + m.b33 + m.b34 + m.b35 + m.b36 + m.b37
    == 3)
m.e26 = Constraint(expr= m.b26 + m.b27 + m.b38 + m.b39 + m.b40 + m.b41 + m.b42
    == 3)
m.e27 = Constraint(expr= m.b25 == 1)
m.e28 = Constraint(expr= m.b26 + m.b27 == 1)
