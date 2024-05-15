# MINLP written by GAMS Convert at 05/15/24 12:00:08
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#        28       10       18        0        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        45       27       18        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       138       75       63
#
# Reformulation has removed 1 variable and 1 equation

from pyomo.environ import *

model = m = ConcreteModel()

m.x1 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x2 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x3 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x4 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x5 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x6 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x7 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x8 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x9 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x10 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x11 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x12 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x13 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x14 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x15 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x16 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x17 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x18 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x19 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x20 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x21 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x22 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x23 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x24 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x25 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x26 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x27 = Var(within=Reals, bounds=(0,1), initialize=0)
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
m.b43 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b44 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b45 = Var(within=Binary, bounds=(0,1), initialize=0)

m.obj = Objective(sense=minimize, expr= m.x1 + m.x2 + m.x3 + m.x4 + m.x5 + m.x6
    + m.x7 + m.x8 + m.x9 + m.x10 + m.x11 + m.x12 + m.x13 + m.x14 + m.x15 +
    m.x16 + m.x17 + m.x18)

m.e1 = Constraint(expr= -sqrt((m.x19 - m.x22)**2 + (m.x20 - m.x23)**2 + (m.x21
    - m.x24)**2) + m.x1 - 1.7320508075688772 * m.b28 >= -1.7320508075688772)
m.e2 = Constraint(expr= -sqrt((m.x19 - m.x25)**2 + (m.x20 - m.x26)**2 + (m.x21
    - m.x27)**2) + m.x2 - 1.7320508075688772 * m.b29 >= -1.7320508075688772)
m.e3 = Constraint(expr= -sqrt((m.x22 - m.x25)**2 + (m.x23 - m.x26)**2 + (m.x24
    - m.x27)**2) + m.x3 - 1.7320508075688772 * m.b30 >= -1.7320508075688772)
m.e4 = Constraint(expr= -sqrt((-0.965242141552123 + m.x19)**2 + (
    -0.011654693792141124 + m.x20)**2 + (-0.7359916197968754 + m.x21)**2) +
    m.x4 - 1.7320508075688772 * m.b31 >= -1.7320508075688772)
m.e5 = Constraint(expr= -sqrt((-0.15801272476474815 + m.x19)**2 + (
    -0.9863394516628233 + m.x20)**2 + (-0.016880654207976242 + m.x21)**2) +
    m.x5 - 1.7320508075688772 * m.b32 >= -1.7320508075688772)
m.e6 = Constraint(expr= -sqrt((-0.8794912681346712 + m.x19)**2 + (
    -0.6813506644014146 + m.x20)**2 + (-0.8573423824815248 + m.x21)**2) + m.x6
    - 1.7320508075688772 * m.b33 >= -1.7320508075688772)
m.e7 = Constraint(expr= -sqrt((-0.9998162341661194 + m.x19)**2 + (
    -0.23971518216378862 + m.x20)**2 + (-0.33807775725669986 + m.x21)**2) +
    m.x7 - 1.7320508075688772 * m.b34 >= -1.7320508075688772)
m.e8 = Constraint(expr= -sqrt((-0.7081943329851277 + m.x19)**2 + (
    -0.28058168584313725 + m.x20)**2 + (-0.2633142571474607 + m.x21)**2) + m.x8
    - 1.7320508075688772 * m.b35 >= -1.7320508075688772)
m.e9 = Constraint(expr= -sqrt((-0.965242141552123 + m.x22)**2 + (
    -0.011654693792141124 + m.x23)**2 + (-0.7359916197968754 + m.x24)**2) +
    m.x9 - 1.7320508075688772 * m.b36 >= -1.7320508075688772)
m.e10 = Constraint(expr= -sqrt((-0.15801272476474815 + m.x22)**2 + (
    -0.9863394516628233 + m.x23)**2 + (-0.016880654207976242 + m.x24)**2) +
    m.x10 - 1.7320508075688772 * m.b37 >= -1.7320508075688772)
m.e11 = Constraint(expr= -sqrt((-0.8794912681346712 + m.x22)**2 + (
    -0.6813506644014146 + m.x23)**2 + (-0.8573423824815248 + m.x24)**2) + m.x11
    - 1.7320508075688772 * m.b38 >= -1.7320508075688772)
m.e12 = Constraint(expr= -sqrt((-0.9998162341661194 + m.x22)**2 + (
    -0.23971518216378862 + m.x23)**2 + (-0.33807775725669986 + m.x24)**2) +
    m.x12 - 1.7320508075688772 * m.b39 >= -1.7320508075688772)
m.e13 = Constraint(expr= -sqrt((-0.7081943329851277 + m.x22)**2 + (
    -0.28058168584313725 + m.x23)**2 + (-0.2633142571474607 + m.x24)**2) +
    m.x13 - 1.7320508075688772 * m.b40 >= -1.7320508075688772)
m.e14 = Constraint(expr= -sqrt((-0.965242141552123 + m.x25)**2 + (
    -0.011654693792141124 + m.x26)**2 + (-0.7359916197968754 + m.x27)**2) +
    m.x14 - 1.7320508075688772 * m.b41 >= -1.7320508075688772)
m.e15 = Constraint(expr= -sqrt((-0.15801272476474815 + m.x25)**2 + (
    -0.9863394516628233 + m.x26)**2 + (-0.016880654207976242 + m.x27)**2) +
    m.x15 - 1.7320508075688772 * m.b42 >= -1.7320508075688772)
m.e16 = Constraint(expr= -sqrt((-0.8794912681346712 + m.x25)**2 + (
    -0.6813506644014146 + m.x26)**2 + (-0.8573423824815248 + m.x27)**2) + m.x16
    - 1.7320508075688772 * m.b43 >= -1.7320508075688772)
m.e17 = Constraint(expr= -sqrt((-0.9998162341661194 + m.x25)**2 + (
    -0.23971518216378862 + m.x26)**2 + (-0.33807775725669986 + m.x27)**2) +
    m.x17 - 1.7320508075688772 * m.b44 >= -1.7320508075688772)
m.e18 = Constraint(expr= -sqrt((-0.7081943329851277 + m.x25)**2 + (
    -0.28058168584313725 + m.x26)**2 + (-0.2633142571474607 + m.x27)**2) +
    m.x18 - 1.7320508075688772 * m.b45 >= -1.7320508075688772)
m.e19 = Constraint(expr= m.b31 + m.b36 + m.b41 == 1)
m.e20 = Constraint(expr= m.b32 + m.b37 + m.b42 == 1)
m.e21 = Constraint(expr= m.b33 + m.b38 + m.b43 == 1)
m.e22 = Constraint(expr= m.b34 + m.b39 + m.b44 == 1)
m.e23 = Constraint(expr= m.b35 + m.b40 + m.b45 == 1)
m.e24 = Constraint(expr= m.b28 + m.b29 + m.b31 + m.b32 + m.b33 + m.b34 + m.b35
    == 3)
m.e25 = Constraint(expr= m.b28 + m.b30 + m.b36 + m.b37 + m.b38 + m.b39 + m.b40
    == 3)
m.e26 = Constraint(expr= m.b29 + m.b30 + m.b41 + m.b42 + m.b43 + m.b44 + m.b45
    == 3)
m.e27 = Constraint(expr= m.b28 == 1)
m.e28 = Constraint(expr= m.b29 + m.b30 == 1)
