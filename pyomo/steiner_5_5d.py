# MINLP written by GAMS Convert at 05/15/24 12:01:00
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#        28       10       18        0        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        51       33       18        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       180       75      105
#
# Reformulation has removed 1 variable and 1 equation

from pyomo.environ import *

model = m = ConcreteModel()

m.x1 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x2 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x3 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x4 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x5 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x6 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x7 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x8 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x9 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x10 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x11 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x12 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x13 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x14 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x15 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x16 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x17 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x18 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
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
m.x31 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x32 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x33 = Var(within=Reals, bounds=(0,1), initialize=0)
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
m.b49 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b50 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b51 = Var(within=Binary, bounds=(0,1), initialize=0)

m.obj = Objective(sense=minimize, expr= m.x1 + m.x2 + m.x3 + m.x4 + m.x5 + m.x6
    + m.x7 + m.x8 + m.x9 + m.x10 + m.x11 + m.x12 + m.x13 + m.x14 + m.x15 +
    m.x16 + m.x17 + m.x18)

m.e1 = Constraint(expr= -sqrt((m.x19 - m.x24)**2 + (m.x20 - m.x25)**2 + (m.x21
    - m.x26)**2 + (m.x22 - m.x27)**2 + (m.x23 - m.x28)**2) + m.x1 -
    2.23606797749979 * m.b34 >= -2.23606797749979)
m.e2 = Constraint(expr= -sqrt((m.x19 - m.x29)**2 + (m.x20 - m.x30)**2 + (m.x21
    - m.x31)**2 + (m.x22 - m.x32)**2 + (m.x23 - m.x33)**2) + m.x2 -
    2.23606797749979 * m.b35 >= -2.23606797749979)
m.e3 = Constraint(expr= -sqrt((m.x24 - m.x29)**2 + (m.x25 - m.x30)**2 + (m.x26
    - m.x31)**2 + (m.x27 - m.x32)**2 + (m.x28 - m.x33)**2) + m.x3 -
    2.23606797749979 * m.b36 >= -2.23606797749979)
m.e4 = Constraint(expr= -sqrt((-0.376962302390386 + m.x19)**2 + (
    -0.9267885077263207 + m.x20)**2 + (-0.8434467391322422 + m.x21)**2 + (
    -0.21404576995204339 + m.x22)**2 + (-0.8717081122454375 + m.x23)**2) + m.x4
    - 2.23606797749979 * m.b37 >= -2.23606797749979)
m.e5 = Constraint(expr= -sqrt((-0.6364617457506916 + m.x19)**2 + (
    -0.04239212615820076 + m.x20)**2 + (-0.9529720601244589 + m.x21)**2 + (
    -0.25568366821646715 + m.x22)**2 + (-0.305900980269444 + m.x23)**2) + m.x5
    - 2.23606797749979 * m.b38 >= -2.23606797749979)
m.e6 = Constraint(expr= -sqrt((-0.4240801565062292 + m.x19)**2 + (
    -0.5885140140252595 + m.x20)**2 + (-0.1243916494838736 + m.x21)**2 + (
    -0.686677304871223 + m.x22)**2 + (-0.8322405233765763 + m.x23)**2) + m.x6
    - 2.23606797749979 * m.b39 >= -2.23606797749979)
m.e7 = Constraint(expr= -sqrt((-0.5123190504571955 + m.x19)**2 + (
    -0.7944608177634946 + m.x20)**2 + (-0.6249799602888791 + m.x21)**2 + (
    -0.8248125234140684 + m.x22)**2 + (-0.18093878439654187 + m.x23)**2) + m.x7
    - 2.23606797749979 * m.b40 >= -2.23606797749979)
m.e8 = Constraint(expr= -sqrt((-0.358677331460587 + m.x19)**2 + (
    -0.46939438227304753 + m.x20)**2 + (-0.1039841315397021 + m.x21)**2 + (
    -0.9731064575430529 + m.x22)**2 + (-0.6360295241926393 + m.x23)**2) + m.x8
    - 2.23606797749979 * m.b41 >= -2.23606797749979)
m.e9 = Constraint(expr= -sqrt((-0.376962302390386 + m.x24)**2 + (
    -0.9267885077263207 + m.x25)**2 + (-0.8434467391322422 + m.x26)**2 + (
    -0.21404576995204339 + m.x27)**2 + (-0.8717081122454375 + m.x28)**2) + m.x9
    - 2.23606797749979 * m.b42 >= -2.23606797749979)
m.e10 = Constraint(expr= -sqrt((-0.6364617457506916 + m.x24)**2 + (
    -0.04239212615820076 + m.x25)**2 + (-0.9529720601244589 + m.x26)**2 + (
    -0.25568366821646715 + m.x27)**2 + (-0.305900980269444 + m.x28)**2) + m.x10
    - 2.23606797749979 * m.b43 >= -2.23606797749979)
m.e11 = Constraint(expr= -sqrt((-0.4240801565062292 + m.x24)**2 + (
    -0.5885140140252595 + m.x25)**2 + (-0.1243916494838736 + m.x26)**2 + (
    -0.686677304871223 + m.x27)**2 + (-0.8322405233765763 + m.x28)**2) + m.x11
    - 2.23606797749979 * m.b44 >= -2.23606797749979)
m.e12 = Constraint(expr= -sqrt((-0.5123190504571955 + m.x24)**2 + (
    -0.7944608177634946 + m.x25)**2 + (-0.6249799602888791 + m.x26)**2 + (
    -0.8248125234140684 + m.x27)**2 + (-0.18093878439654187 + m.x28)**2) +
    m.x12 - 2.23606797749979 * m.b45 >= -2.23606797749979)
m.e13 = Constraint(expr= -sqrt((-0.358677331460587 + m.x24)**2 + (
    -0.46939438227304753 + m.x25)**2 + (-0.1039841315397021 + m.x26)**2 + (
    -0.9731064575430529 + m.x27)**2 + (-0.6360295241926393 + m.x28)**2) + m.x13
    - 2.23606797749979 * m.b46 >= -2.23606797749979)
m.e14 = Constraint(expr= -sqrt((-0.376962302390386 + m.x29)**2 + (
    -0.9267885077263207 + m.x30)**2 + (-0.8434467391322422 + m.x31)**2 + (
    -0.21404576995204339 + m.x32)**2 + (-0.8717081122454375 + m.x33)**2) +
    m.x14 - 2.23606797749979 * m.b47 >= -2.23606797749979)
m.e15 = Constraint(expr= -sqrt((-0.6364617457506916 + m.x29)**2 + (
    -0.04239212615820076 + m.x30)**2 + (-0.9529720601244589 + m.x31)**2 + (
    -0.25568366821646715 + m.x32)**2 + (-0.305900980269444 + m.x33)**2) + m.x15
    - 2.23606797749979 * m.b48 >= -2.23606797749979)
m.e16 = Constraint(expr= -sqrt((-0.4240801565062292 + m.x29)**2 + (
    -0.5885140140252595 + m.x30)**2 + (-0.1243916494838736 + m.x31)**2 + (
    -0.686677304871223 + m.x32)**2 + (-0.8322405233765763 + m.x33)**2) + m.x16
    - 2.23606797749979 * m.b49 >= -2.23606797749979)
m.e17 = Constraint(expr= -sqrt((-0.5123190504571955 + m.x29)**2 + (
    -0.7944608177634946 + m.x30)**2 + (-0.6249799602888791 + m.x31)**2 + (
    -0.8248125234140684 + m.x32)**2 + (-0.18093878439654187 + m.x33)**2) +
    m.x17 - 2.23606797749979 * m.b50 >= -2.23606797749979)
m.e18 = Constraint(expr= -sqrt((-0.358677331460587 + m.x29)**2 + (
    -0.46939438227304753 + m.x30)**2 + (-0.1039841315397021 + m.x31)**2 + (
    -0.9731064575430529 + m.x32)**2 + (-0.6360295241926393 + m.x33)**2) + m.x18
    - 2.23606797749979 * m.b51 >= -2.23606797749979)
m.e19 = Constraint(expr= m.b37 + m.b42 + m.b47 == 1)
m.e20 = Constraint(expr= m.b38 + m.b43 + m.b48 == 1)
m.e21 = Constraint(expr= m.b39 + m.b44 + m.b49 == 1)
m.e22 = Constraint(expr= m.b40 + m.b45 + m.b50 == 1)
m.e23 = Constraint(expr= m.b41 + m.b46 + m.b51 == 1)
m.e24 = Constraint(expr= m.b34 + m.b35 + m.b37 + m.b38 + m.b39 + m.b40 + m.b41
    == 3)
m.e25 = Constraint(expr= m.b34 + m.b36 + m.b42 + m.b43 + m.b44 + m.b45 + m.b46
    == 3)
m.e26 = Constraint(expr= m.b35 + m.b36 + m.b47 + m.b48 + m.b49 + m.b50 + m.b51
    == 3)
m.e27 = Constraint(expr= m.b34 == 1)
m.e28 = Constraint(expr= m.b35 + m.b36 == 1)
