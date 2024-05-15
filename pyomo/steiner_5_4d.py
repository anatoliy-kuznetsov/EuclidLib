# MINLP written by GAMS Convert at 05/15/24 11:59:10
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#        28       10       18        0        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        48       30       18        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       159       75       84
#
# Reformulation has removed 1 variable and 1 equation

from pyomo.environ import *

model = m = ConcreteModel()

m.x1 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x2 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x3 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x4 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x5 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x6 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x7 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x8 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x9 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x10 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x11 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x12 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x13 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x14 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x15 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x16 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x17 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x18 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x19 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x20 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x21 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x22 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x23 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x24 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x25 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x26 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x27 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x28 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x29 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x30 = Var(within=Reals, bounds=(0,1), initialize=0)
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
m.b46 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b47 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b48 = Var(within=Binary, bounds=(0,1), initialize=0)

m.obj = Objective(sense=minimize, expr= m.x1 + m.x2 + m.x3 + m.x4 + m.x5 + m.x6
    + m.x7 + m.x8 + m.x9 + m.x10 + m.x11 + m.x12 + m.x13 + m.x14 + m.x15 +
    m.x16 + m.x17 + m.x18)

m.e1 = Constraint(expr= -sqrt((m.x19 - m.x23)**2 + (m.x20 - m.x24)**2 + (m.x21
    - m.x25)**2 + (m.x22 - m.x26)**2) + m.x1 - 2 * m.b31 >= -2)
m.e2 = Constraint(expr= -sqrt((m.x19 - m.x27)**2 + (m.x20 - m.x28)**2 + (m.x21
    - m.x29)**2 + (m.x22 - m.x30)**2) + m.x2 - 2 * m.b32 >= -2)
m.e3 = Constraint(expr= -sqrt((m.x23 - m.x27)**2 + (m.x24 - m.x28)**2 + (m.x25
    - m.x29)**2 + (m.x26 - m.x30)**2) + m.x3 - 2 * m.b33 >= -2)
m.e4 = Constraint(expr= -sqrt((-0.9056396761745207 + m.x19)**2 + (
    -0.6862541570267026 + m.x20)**2 + (-0.7665092563626442 + m.x21)**2 + (
    -0.9046162378132736 + m.x22)**2) + m.x4 - 2 * m.b34 >= -2)
m.e5 = Constraint(expr= -sqrt((-0.2598274474889769 + m.x19)**2 + (
    -0.6357258696059892 + m.x20)**2 + (-0.9049456946664788 + m.x21)**2 + (
    -0.8721303740697106 + m.x22)**2) + m.x5 - 2 * m.b35 >= -2)
m.e6 = Constraint(expr= -sqrt((-0.5729406692492218 + m.x19)**2 + (
    -0.1693780871255699 + m.x20)**2 + (-0.4115230620409567 + m.x21)**2 + (
    -0.9938380127773296 + m.x22)**2) + m.x6 - 2 * m.b36 >= -2)
m.e7 = Constraint(expr= -sqrt((-0.10324779991117994 + m.x19)**2 + (
    -0.31913914884928973 + m.x20)**2 + (-0.9500391079535002 + m.x21)**2 + (
    -0.4494007558523254 + m.x22)**2) + m.x7 - 2 * m.b37 >= -2)
m.e8 = Constraint(expr= -sqrt((-0.20865257233244294 + m.x19)**2 + (
    -0.316903983245593 + m.x20)**2 + (-0.9086358448961127 + m.x21)**2 + (
    -0.33556881046847387 + m.x22)**2) + m.x8 - 2 * m.b38 >= -2)
m.e9 = Constraint(expr= -sqrt((-0.9056396761745207 + m.x23)**2 + (
    -0.6862541570267026 + m.x24)**2 + (-0.7665092563626442 + m.x25)**2 + (
    -0.9046162378132736 + m.x26)**2) + m.x9 - 2 * m.b39 >= -2)
m.e10 = Constraint(expr= -sqrt((-0.2598274474889769 + m.x23)**2 + (
    -0.6357258696059892 + m.x24)**2 + (-0.9049456946664788 + m.x25)**2 + (
    -0.8721303740697106 + m.x26)**2) + m.x10 - 2 * m.b40 >= -2)
m.e11 = Constraint(expr= -sqrt((-0.5729406692492218 + m.x23)**2 + (
    -0.1693780871255699 + m.x24)**2 + (-0.4115230620409567 + m.x25)**2 + (
    -0.9938380127773296 + m.x26)**2) + m.x11 - 2 * m.b41 >= -2)
m.e12 = Constraint(expr= -sqrt((-0.10324779991117994 + m.x23)**2 + (
    -0.31913914884928973 + m.x24)**2 + (-0.9500391079535002 + m.x25)**2 + (
    -0.4494007558523254 + m.x26)**2) + m.x12 - 2 * m.b42 >= -2)
m.e13 = Constraint(expr= -sqrt((-0.20865257233244294 + m.x23)**2 + (
    -0.316903983245593 + m.x24)**2 + (-0.9086358448961127 + m.x25)**2 + (
    -0.33556881046847387 + m.x26)**2) + m.x13 - 2 * m.b43 >= -2)
m.e14 = Constraint(expr= -sqrt((-0.9056396761745207 + m.x27)**2 + (
    -0.6862541570267026 + m.x28)**2 + (-0.7665092563626442 + m.x29)**2 + (
    -0.9046162378132736 + m.x30)**2) + m.x14 - 2 * m.b44 >= -2)
m.e15 = Constraint(expr= -sqrt((-0.2598274474889769 + m.x27)**2 + (
    -0.6357258696059892 + m.x28)**2 + (-0.9049456946664788 + m.x29)**2 + (
    -0.8721303740697106 + m.x30)**2) + m.x15 - 2 * m.b45 >= -2)
m.e16 = Constraint(expr= -sqrt((-0.5729406692492218 + m.x27)**2 + (
    -0.1693780871255699 + m.x28)**2 + (-0.4115230620409567 + m.x29)**2 + (
    -0.9938380127773296 + m.x30)**2) + m.x16 - 2 * m.b46 >= -2)
m.e17 = Constraint(expr= -sqrt((-0.10324779991117994 + m.x27)**2 + (
    -0.31913914884928973 + m.x28)**2 + (-0.9500391079535002 + m.x29)**2 + (
    -0.4494007558523254 + m.x30)**2) + m.x17 - 2 * m.b47 >= -2)
m.e18 = Constraint(expr= -sqrt((-0.20865257233244294 + m.x27)**2 + (
    -0.316903983245593 + m.x28)**2 + (-0.9086358448961127 + m.x29)**2 + (
    -0.33556881046847387 + m.x30)**2) + m.x18 - 2 * m.b48 >= -2)
m.e19 = Constraint(expr= m.b34 + m.b39 + m.b44 == 1)
m.e20 = Constraint(expr= m.b35 + m.b40 + m.b45 == 1)
m.e21 = Constraint(expr= m.b36 + m.b41 + m.b46 == 1)
m.e22 = Constraint(expr= m.b37 + m.b42 + m.b47 == 1)
m.e23 = Constraint(expr= m.b38 + m.b43 + m.b48 == 1)
m.e24 = Constraint(expr= m.b31 + m.b32 + m.b34 + m.b35 + m.b36 + m.b37 + m.b38
    == 3)
m.e25 = Constraint(expr= m.b31 + m.b33 + m.b39 + m.b40 + m.b41 + m.b42 + m.b43
    == 3)
m.e26 = Constraint(expr= m.b32 + m.b33 + m.b44 + m.b45 + m.b46 + m.b47 + m.b48
    == 3)
m.e27 = Constraint(expr= m.b31 == 1)
m.e28 = Constraint(expr= m.b32 + m.b33 == 1)
