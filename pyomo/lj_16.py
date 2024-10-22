# NLP written by GAMS Convert at 05/15/24 11:42:07
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       120        0      120        0        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        48       48        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       720        0      720
#
# Reformulation has removed 1 variable and 1 equation

from pyomo.environ import *

model = m = ConcreteModel()

m.x1 = Var(within=Reals, bounds=(0,15), initialize=0)
m.x2 = Var(within=Reals, bounds=(0,15), initialize=0)
m.x3 = Var(within=Reals, bounds=(0,15), initialize=0)
m.x4 = Var(within=Reals, bounds=(0,15), initialize=0)
m.x5 = Var(within=Reals, bounds=(0,15), initialize=0)
m.x6 = Var(within=Reals, bounds=(0,15), initialize=0)
m.x7 = Var(within=Reals, bounds=(0,15), initialize=0)
m.x8 = Var(within=Reals, bounds=(0,15), initialize=0)
m.x9 = Var(within=Reals, bounds=(0,15), initialize=0)
m.x10 = Var(within=Reals, bounds=(0,15), initialize=0)
m.x11 = Var(within=Reals, bounds=(0,15), initialize=0)
m.x12 = Var(within=Reals, bounds=(0,15), initialize=0)
m.x13 = Var(within=Reals, bounds=(0,15), initialize=0)
m.x14 = Var(within=Reals, bounds=(0,15), initialize=0)
m.x15 = Var(within=Reals, bounds=(0,15), initialize=0)
m.x16 = Var(within=Reals, bounds=(0,15), initialize=0)
m.x17 = Var(within=Reals, bounds=(-15,15), initialize=0)
m.x18 = Var(within=Reals, bounds=(-15,15), initialize=0)
m.x19 = Var(within=Reals, bounds=(-15,15), initialize=0)
m.x20 = Var(within=Reals, bounds=(-15,15), initialize=0)
m.x21 = Var(within=Reals, bounds=(-15,15), initialize=0)
m.x22 = Var(within=Reals, bounds=(-15,15), initialize=0)
m.x23 = Var(within=Reals, bounds=(-15,15), initialize=0)
m.x24 = Var(within=Reals, bounds=(-15,15), initialize=0)
m.x25 = Var(within=Reals, bounds=(-15,15), initialize=0)
m.x26 = Var(within=Reals, bounds=(-15,15), initialize=0)
m.x27 = Var(within=Reals, bounds=(-15,15), initialize=0)
m.x28 = Var(within=Reals, bounds=(-15,15), initialize=0)
m.x29 = Var(within=Reals, bounds=(-15,15), initialize=0)
m.x30 = Var(within=Reals, bounds=(-15,15), initialize=0)
m.x31 = Var(within=Reals, bounds=(-15,15), initialize=0)
m.x32 = Var(within=Reals, bounds=(-15,15), initialize=0)
m.x33 = Var(within=Reals, bounds=(-15,15), initialize=0)
m.x34 = Var(within=Reals, bounds=(-15,15), initialize=0)
m.x35 = Var(within=Reals, bounds=(-15,15), initialize=0)
m.x36 = Var(within=Reals, bounds=(-15,15), initialize=0)
m.x37 = Var(within=Reals, bounds=(-15,15), initialize=0)
m.x38 = Var(within=Reals, bounds=(-15,15), initialize=0)
m.x39 = Var(within=Reals, bounds=(-15,15), initialize=0)
m.x40 = Var(within=Reals, bounds=(-15,15), initialize=0)
m.x41 = Var(within=Reals, bounds=(-15,15), initialize=0)
m.x42 = Var(within=Reals, bounds=(-15,15), initialize=0)
m.x43 = Var(within=Reals, bounds=(-15,15), initialize=0)
m.x44 = Var(within=Reals, bounds=(-15,15), initialize=0)
m.x45 = Var(within=Reals, bounds=(-15,15), initialize=0)
m.x46 = Var(within=Reals, bounds=(-15,15), initialize=0)
m.x47 = Var(within=Reals, bounds=(-15,15), initialize=0)
m.x48 = Var(within=Reals, bounds=(-15,15), initialize=0)

m.obj = Objective(sense=minimize, expr= ((m.x1 - m.x2)**2 + (m.x17 - m.x18)**2
    + (m.x33 - m.x34)**2)**(-3) * (((m.x1 - m.x2)**2 + (m.x17 - m.x18)**2 + (
    m.x33 - m.x34)**2)**(-3) - 2) + ((m.x1 - m.x3)**2 + (m.x17 - m.x19)**2 + (
    m.x33 - m.x35)**2)**(-3) * (((m.x1 - m.x3)**2 + (m.x17 - m.x19)**2 + (m.x33
    - m.x35)**2)**(-3) - 2) + ((m.x1 - m.x4)**2 + (m.x17 - m.x20)**2 + (m.x33
    - m.x36)**2)**(-3) * (((m.x1 - m.x4)**2 + (m.x17 - m.x20)**2 + (m.x33 -
    m.x36)**2)**(-3) - 2) + ((m.x1 - m.x5)**2 + (m.x17 - m.x21)**2 + (m.x33 -
    m.x37)**2)**(-3) * (((m.x1 - m.x5)**2 + (m.x17 - m.x21)**2 + (m.x33 - m.x37)
    **2)**(-3) - 2) + ((m.x1 - m.x6)**2 + (m.x17 - m.x22)**2 + (m.x33 - m.x38)
    **2)**(-3) * (((m.x1 - m.x6)**2 + (m.x17 - m.x22)**2 + (m.x33 - m.x38)**2)
    **(-3) - 2) + ((m.x1 - m.x7)**2 + (m.x17 - m.x23)**2 + (m.x33 - m.x39)**2)
    **(-3) * (((m.x1 - m.x7)**2 + (m.x17 - m.x23)**2 + (m.x33 - m.x39)**2)**(-3)
    - 2) + ((m.x1 - m.x8)**2 + (m.x17 - m.x24)**2 + (m.x33 - m.x40)**2)**(-3)
    * (((m.x1 - m.x8)**2 + (m.x17 - m.x24)**2 + (m.x33 - m.x40)**2)**(-3) - 2)
    + ((m.x1 - m.x9)**2 + (m.x17 - m.x25)**2 + (m.x33 - m.x41)**2)**(-3) * (((
    m.x1 - m.x9)**2 + (m.x17 - m.x25)**2 + (m.x33 - m.x41)**2)**(-3) - 2) + ((
    m.x1 - m.x10)**2 + (m.x17 - m.x26)**2 + (m.x33 - m.x42)**2)**(-3) * (((m.x1
    - m.x10)**2 + (m.x17 - m.x26)**2 + (m.x33 - m.x42)**2)**(-3) - 2) + ((m.x1
    - m.x11)**2 + (m.x17 - m.x27)**2 + (m.x33 - m.x43)**2)**(-3) * (((m.x1 -
    m.x11)**2 + (m.x17 - m.x27)**2 + (m.x33 - m.x43)**2)**(-3) - 2) + ((m.x1 -
    m.x12)**2 + (m.x17 - m.x28)**2 + (m.x33 - m.x44)**2)**(-3) * (((m.x1 -
    m.x12)**2 + (m.x17 - m.x28)**2 + (m.x33 - m.x44)**2)**(-3) - 2) + ((m.x1 -
    m.x13)**2 + (m.x17 - m.x29)**2 + (m.x33 - m.x45)**2)**(-3) * (((m.x1 -
    m.x13)**2 + (m.x17 - m.x29)**2 + (m.x33 - m.x45)**2)**(-3) - 2) + ((m.x1 -
    m.x14)**2 + (m.x17 - m.x30)**2 + (m.x33 - m.x46)**2)**(-3) * (((m.x1 -
    m.x14)**2 + (m.x17 - m.x30)**2 + (m.x33 - m.x46)**2)**(-3) - 2) + ((m.x1 -
    m.x15)**2 + (m.x17 - m.x31)**2 + (m.x33 - m.x47)**2)**(-3) * (((m.x1 -
    m.x15)**2 + (m.x17 - m.x31)**2 + (m.x33 - m.x47)**2)**(-3) - 2) + ((m.x1 -
    m.x16)**2 + (m.x17 - m.x32)**2 + (m.x33 - m.x48)**2)**(-3) * (((m.x1 -
    m.x16)**2 + (m.x17 - m.x32)**2 + (m.x33 - m.x48)**2)**(-3) - 2) + ((m.x2 -
    m.x3)**2 + (m.x18 - m.x19)**2 + (m.x34 - m.x35)**2)**(-3) * (((m.x2 - m.x3)
    **2 + (m.x18 - m.x19)**2 + (m.x34 - m.x35)**2)**(-3) - 2) + ((m.x2 - m.x4)
    **2 + (m.x18 - m.x20)**2 + (m.x34 - m.x36)**2)**(-3) * (((m.x2 - m.x4)**2
    + (m.x18 - m.x20)**2 + (m.x34 - m.x36)**2)**(-3) - 2) + ((m.x2 - m.x5)**2
    + (m.x18 - m.x21)**2 + (m.x34 - m.x37)**2)**(-3) * (((m.x2 - m.x5)**2 + (
    m.x18 - m.x21)**2 + (m.x34 - m.x37)**2)**(-3) - 2) + ((m.x2 - m.x6)**2 + (
    m.x18 - m.x22)**2 + (m.x34 - m.x38)**2)**(-3) * (((m.x2 - m.x6)**2 + (m.x18
    - m.x22)**2 + (m.x34 - m.x38)**2)**(-3) - 2) + ((m.x2 - m.x7)**2 + (m.x18
    - m.x23)**2 + (m.x34 - m.x39)**2)**(-3) * (((m.x2 - m.x7)**2 + (m.x18 -
    m.x23)**2 + (m.x34 - m.x39)**2)**(-3) - 2) + ((m.x2 - m.x8)**2 + (m.x18 -
    m.x24)**2 + (m.x34 - m.x40)**2)**(-3) * (((m.x2 - m.x8)**2 + (m.x18 - m.x24)
    **2 + (m.x34 - m.x40)**2)**(-3) - 2) + ((m.x2 - m.x9)**2 + (m.x18 - m.x25)
    **2 + (m.x34 - m.x41)**2)**(-3) * (((m.x2 - m.x9)**2 + (m.x18 - m.x25)**2
    + (m.x34 - m.x41)**2)**(-3) - 2) + ((m.x2 - m.x10)**2 + (m.x18 - m.x26)**2
    + (m.x34 - m.x42)**2)**(-3) * (((m.x2 - m.x10)**2 + (m.x18 - m.x26)**2 + (
    m.x34 - m.x42)**2)**(-3) - 2) + ((m.x2 - m.x11)**2 + (m.x18 - m.x27)**2 + (
    m.x34 - m.x43)**2)**(-3) * (((m.x2 - m.x11)**2 + (m.x18 - m.x27)**2 + (
    m.x34 - m.x43)**2)**(-3) - 2) + ((m.x2 - m.x12)**2 + (m.x18 - m.x28)**2 + (
    m.x34 - m.x44)**2)**(-3) * (((m.x2 - m.x12)**2 + (m.x18 - m.x28)**2 + (
    m.x34 - m.x44)**2)**(-3) - 2) + ((m.x2 - m.x13)**2 + (m.x18 - m.x29)**2 + (
    m.x34 - m.x45)**2)**(-3) * (((m.x2 - m.x13)**2 + (m.x18 - m.x29)**2 + (
    m.x34 - m.x45)**2)**(-3) - 2) + ((m.x2 - m.x14)**2 + (m.x18 - m.x30)**2 + (
    m.x34 - m.x46)**2)**(-3) * (((m.x2 - m.x14)**2 + (m.x18 - m.x30)**2 + (
    m.x34 - m.x46)**2)**(-3) - 2) + ((m.x2 - m.x15)**2 + (m.x18 - m.x31)**2 + (
    m.x34 - m.x47)**2)**(-3) * (((m.x2 - m.x15)**2 + (m.x18 - m.x31)**2 + (
    m.x34 - m.x47)**2)**(-3) - 2) + ((m.x2 - m.x16)**2 + (m.x18 - m.x32)**2 + (
    m.x34 - m.x48)**2)**(-3) * (((m.x2 - m.x16)**2 + (m.x18 - m.x32)**2 + (
    m.x34 - m.x48)**2)**(-3) - 2) + ((m.x3 - m.x4)**2 + (m.x19 - m.x20)**2 + (
    m.x35 - m.x36)**2)**(-3) * (((m.x3 - m.x4)**2 + (m.x19 - m.x20)**2 + (m.x35
    - m.x36)**2)**(-3) - 2) + ((m.x3 - m.x5)**2 + (m.x19 - m.x21)**2 + (m.x35
    - m.x37)**2)**(-3) * (((m.x3 - m.x5)**2 + (m.x19 - m.x21)**2 + (m.x35 -
    m.x37)**2)**(-3) - 2) + ((m.x3 - m.x6)**2 + (m.x19 - m.x22)**2 + (m.x35 -
    m.x38)**2)**(-3) * (((m.x3 - m.x6)**2 + (m.x19 - m.x22)**2 + (m.x35 - m.x38)
    **2)**(-3) - 2) + ((m.x3 - m.x7)**2 + (m.x19 - m.x23)**2 + (m.x35 - m.x39)
    **2)**(-3) * (((m.x3 - m.x7)**2 + (m.x19 - m.x23)**2 + (m.x35 - m.x39)**2)
    **(-3) - 2) + ((m.x3 - m.x8)**2 + (m.x19 - m.x24)**2 + (m.x35 - m.x40)**2)
    **(-3) * (((m.x3 - m.x8)**2 + (m.x19 - m.x24)**2 + (m.x35 - m.x40)**2)**(-3)
    - 2) + ((m.x3 - m.x9)**2 + (m.x19 - m.x25)**2 + (m.x35 - m.x41)**2)**(-3)
    * (((m.x3 - m.x9)**2 + (m.x19 - m.x25)**2 + (m.x35 - m.x41)**2)**(-3) - 2)
    + ((m.x3 - m.x10)**2 + (m.x19 - m.x26)**2 + (m.x35 - m.x42)**2)**(-3) * ((
    (m.x3 - m.x10)**2 + (m.x19 - m.x26)**2 + (m.x35 - m.x42)**2)**(-3) - 2) + (
    (m.x3 - m.x11)**2 + (m.x19 - m.x27)**2 + (m.x35 - m.x43)**2)**(-3) * (((
    m.x3 - m.x11)**2 + (m.x19 - m.x27)**2 + (m.x35 - m.x43)**2)**(-3) - 2) + ((
    m.x3 - m.x12)**2 + (m.x19 - m.x28)**2 + (m.x35 - m.x44)**2)**(-3) * (((m.x3
    - m.x12)**2 + (m.x19 - m.x28)**2 + (m.x35 - m.x44)**2)**(-3) - 2) + ((m.x3
    - m.x13)**2 + (m.x19 - m.x29)**2 + (m.x35 - m.x45)**2)**(-3) * (((m.x3 -
    m.x13)**2 + (m.x19 - m.x29)**2 + (m.x35 - m.x45)**2)**(-3) - 2) + ((m.x3 -
    m.x14)**2 + (m.x19 - m.x30)**2 + (m.x35 - m.x46)**2)**(-3) * (((m.x3 -
    m.x14)**2 + (m.x19 - m.x30)**2 + (m.x35 - m.x46)**2)**(-3) - 2) + ((m.x3 -
    m.x15)**2 + (m.x19 - m.x31)**2 + (m.x35 - m.x47)**2)**(-3) * (((m.x3 -
    m.x15)**2 + (m.x19 - m.x31)**2 + (m.x35 - m.x47)**2)**(-3) - 2) + ((m.x3 -
    m.x16)**2 + (m.x19 - m.x32)**2 + (m.x35 - m.x48)**2)**(-3) * (((m.x3 -
    m.x16)**2 + (m.x19 - m.x32)**2 + (m.x35 - m.x48)**2)**(-3) - 2) + ((m.x4 -
    m.x5)**2 + (m.x20 - m.x21)**2 + (m.x36 - m.x37)**2)**(-3) * (((m.x4 - m.x5)
    **2 + (m.x20 - m.x21)**2 + (m.x36 - m.x37)**2)**(-3) - 2) + ((m.x4 - m.x6)
    **2 + (m.x20 - m.x22)**2 + (m.x36 - m.x38)**2)**(-3) * (((m.x4 - m.x6)**2
    + (m.x20 - m.x22)**2 + (m.x36 - m.x38)**2)**(-3) - 2) + ((m.x4 - m.x7)**2
    + (m.x20 - m.x23)**2 + (m.x36 - m.x39)**2)**(-3) * (((m.x4 - m.x7)**2 + (
    m.x20 - m.x23)**2 + (m.x36 - m.x39)**2)**(-3) - 2) + ((m.x4 - m.x8)**2 + (
    m.x20 - m.x24)**2 + (m.x36 - m.x40)**2)**(-3) * (((m.x4 - m.x8)**2 + (m.x20
    - m.x24)**2 + (m.x36 - m.x40)**2)**(-3) - 2) + ((m.x4 - m.x9)**2 + (m.x20
    - m.x25)**2 + (m.x36 - m.x41)**2)**(-3) * (((m.x4 - m.x9)**2 + (m.x20 -
    m.x25)**2 + (m.x36 - m.x41)**2)**(-3) - 2) + ((m.x4 - m.x10)**2 + (m.x20 -
    m.x26)**2 + (m.x36 - m.x42)**2)**(-3) * (((m.x4 - m.x10)**2 + (m.x20 -
    m.x26)**2 + (m.x36 - m.x42)**2)**(-3) - 2) + ((m.x4 - m.x11)**2 + (m.x20 -
    m.x27)**2 + (m.x36 - m.x43)**2)**(-3) * (((m.x4 - m.x11)**2 + (m.x20 -
    m.x27)**2 + (m.x36 - m.x43)**2)**(-3) - 2) + ((m.x4 - m.x12)**2 + (m.x20 -
    m.x28)**2 + (m.x36 - m.x44)**2)**(-3) * (((m.x4 - m.x12)**2 + (m.x20 -
    m.x28)**2 + (m.x36 - m.x44)**2)**(-3) - 2) + ((m.x4 - m.x13)**2 + (m.x20 -
    m.x29)**2 + (m.x36 - m.x45)**2)**(-3) * (((m.x4 - m.x13)**2 + (m.x20 -
    m.x29)**2 + (m.x36 - m.x45)**2)**(-3) - 2) + ((m.x4 - m.x14)**2 + (m.x20 -
    m.x30)**2 + (m.x36 - m.x46)**2)**(-3) * (((m.x4 - m.x14)**2 + (m.x20 -
    m.x30)**2 + (m.x36 - m.x46)**2)**(-3) - 2) + ((m.x4 - m.x15)**2 + (m.x20 -
    m.x31)**2 + (m.x36 - m.x47)**2)**(-3) * (((m.x4 - m.x15)**2 + (m.x20 -
    m.x31)**2 + (m.x36 - m.x47)**2)**(-3) - 2) + ((m.x4 - m.x16)**2 + (m.x20 -
    m.x32)**2 + (m.x36 - m.x48)**2)**(-3) * (((m.x4 - m.x16)**2 + (m.x20 -
    m.x32)**2 + (m.x36 - m.x48)**2)**(-3) - 2) + ((m.x5 - m.x6)**2 + (m.x21 -
    m.x22)**2 + (m.x37 - m.x38)**2)**(-3) * (((m.x5 - m.x6)**2 + (m.x21 - m.x22)
    **2 + (m.x37 - m.x38)**2)**(-3) - 2) + ((m.x5 - m.x7)**2 + (m.x21 - m.x23)
    **2 + (m.x37 - m.x39)**2)**(-3) * (((m.x5 - m.x7)**2 + (m.x21 - m.x23)**2
    + (m.x37 - m.x39)**2)**(-3) - 2) + ((m.x5 - m.x8)**2 + (m.x21 - m.x24)**2
    + (m.x37 - m.x40)**2)**(-3) * (((m.x5 - m.x8)**2 + (m.x21 - m.x24)**2 + (
    m.x37 - m.x40)**2)**(-3) - 2) + ((m.x5 - m.x9)**2 + (m.x21 - m.x25)**2 + (
    m.x37 - m.x41)**2)**(-3) * (((m.x5 - m.x9)**2 + (m.x21 - m.x25)**2 + (m.x37
    - m.x41)**2)**(-3) - 2) + ((m.x5 - m.x10)**2 + (m.x21 - m.x26)**2 + (m.x37
    - m.x42)**2)**(-3) * (((m.x5 - m.x10)**2 + (m.x21 - m.x26)**2 + (m.x37 -
    m.x42)**2)**(-3) - 2) + ((m.x5 - m.x11)**2 + (m.x21 - m.x27)**2 + (m.x37 -
    m.x43)**2)**(-3) * (((m.x5 - m.x11)**2 + (m.x21 - m.x27)**2 + (m.x37 -
    m.x43)**2)**(-3) - 2) + ((m.x5 - m.x12)**2 + (m.x21 - m.x28)**2 + (m.x37 -
    m.x44)**2)**(-3) * (((m.x5 - m.x12)**2 + (m.x21 - m.x28)**2 + (m.x37 -
    m.x44)**2)**(-3) - 2) + ((m.x5 - m.x13)**2 + (m.x21 - m.x29)**2 + (m.x37 -
    m.x45)**2)**(-3) * (((m.x5 - m.x13)**2 + (m.x21 - m.x29)**2 + (m.x37 -
    m.x45)**2)**(-3) - 2) + ((m.x5 - m.x14)**2 + (m.x21 - m.x30)**2 + (m.x37 -
    m.x46)**2)**(-3) * (((m.x5 - m.x14)**2 + (m.x21 - m.x30)**2 + (m.x37 -
    m.x46)**2)**(-3) - 2) + ((m.x5 - m.x15)**2 + (m.x21 - m.x31)**2 + (m.x37 -
    m.x47)**2)**(-3) * (((m.x5 - m.x15)**2 + (m.x21 - m.x31)**2 + (m.x37 -
    m.x47)**2)**(-3) - 2) + ((m.x5 - m.x16)**2 + (m.x21 - m.x32)**2 + (m.x37 -
    m.x48)**2)**(-3) * (((m.x5 - m.x16)**2 + (m.x21 - m.x32)**2 + (m.x37 -
    m.x48)**2)**(-3) - 2) + ((m.x6 - m.x7)**2 + (m.x22 - m.x23)**2 + (m.x38 -
    m.x39)**2)**(-3) * (((m.x6 - m.x7)**2 + (m.x22 - m.x23)**2 + (m.x38 - m.x39)
    **2)**(-3) - 2) + ((m.x6 - m.x8)**2 + (m.x22 - m.x24)**2 + (m.x38 - m.x40)
    **2)**(-3) * (((m.x6 - m.x8)**2 + (m.x22 - m.x24)**2 + (m.x38 - m.x40)**2)
    **(-3) - 2) + ((m.x6 - m.x9)**2 + (m.x22 - m.x25)**2 + (m.x38 - m.x41)**2)
    **(-3) * (((m.x6 - m.x9)**2 + (m.x22 - m.x25)**2 + (m.x38 - m.x41)**2)**(-3)
    - 2) + ((m.x6 - m.x10)**2 + (m.x22 - m.x26)**2 + (m.x38 - m.x42)**2)**(-3)
    * (((m.x6 - m.x10)**2 + (m.x22 - m.x26)**2 + (m.x38 - m.x42)**2)**(-3) - 2)
    + ((m.x6 - m.x11)**2 + (m.x22 - m.x27)**2 + (m.x38 - m.x43)**2)**(-3) * ((
    (m.x6 - m.x11)**2 + (m.x22 - m.x27)**2 + (m.x38 - m.x43)**2)**(-3) - 2) + (
    (m.x6 - m.x12)**2 + (m.x22 - m.x28)**2 + (m.x38 - m.x44)**2)**(-3) * (((
    m.x6 - m.x12)**2 + (m.x22 - m.x28)**2 + (m.x38 - m.x44)**2)**(-3) - 2) + ((
    m.x6 - m.x13)**2 + (m.x22 - m.x29)**2 + (m.x38 - m.x45)**2)**(-3) * (((m.x6
    - m.x13)**2 + (m.x22 - m.x29)**2 + (m.x38 - m.x45)**2)**(-3) - 2) + ((m.x6
    - m.x14)**2 + (m.x22 - m.x30)**2 + (m.x38 - m.x46)**2)**(-3) * (((m.x6 -
    m.x14)**2 + (m.x22 - m.x30)**2 + (m.x38 - m.x46)**2)**(-3) - 2) + ((m.x6 -
    m.x15)**2 + (m.x22 - m.x31)**2 + (m.x38 - m.x47)**2)**(-3) * (((m.x6 -
    m.x15)**2 + (m.x22 - m.x31)**2 + (m.x38 - m.x47)**2)**(-3) - 2) + ((m.x6 -
    m.x16)**2 + (m.x22 - m.x32)**2 + (m.x38 - m.x48)**2)**(-3) * (((m.x6 -
    m.x16)**2 + (m.x22 - m.x32)**2 + (m.x38 - m.x48)**2)**(-3) - 2) + ((m.x7 -
    m.x8)**2 + (m.x23 - m.x24)**2 + (m.x39 - m.x40)**2)**(-3) * (((m.x7 - m.x8)
    **2 + (m.x23 - m.x24)**2 + (m.x39 - m.x40)**2)**(-3) - 2) + ((m.x7 - m.x9)
    **2 + (m.x23 - m.x25)**2 + (m.x39 - m.x41)**2)**(-3) * (((m.x7 - m.x9)**2
    + (m.x23 - m.x25)**2 + (m.x39 - m.x41)**2)**(-3) - 2) + ((m.x7 - m.x10)**2
    + (m.x23 - m.x26)**2 + (m.x39 - m.x42)**2)**(-3) * (((m.x7 - m.x10)**2 + (
    m.x23 - m.x26)**2 + (m.x39 - m.x42)**2)**(-3) - 2) + ((m.x7 - m.x11)**2 + (
    m.x23 - m.x27)**2 + (m.x39 - m.x43)**2)**(-3) * (((m.x7 - m.x11)**2 + (
    m.x23 - m.x27)**2 + (m.x39 - m.x43)**2)**(-3) - 2) + ((m.x7 - m.x12)**2 + (
    m.x23 - m.x28)**2 + (m.x39 - m.x44)**2)**(-3) * (((m.x7 - m.x12)**2 + (
    m.x23 - m.x28)**2 + (m.x39 - m.x44)**2)**(-3) - 2) + ((m.x7 - m.x13)**2 + (
    m.x23 - m.x29)**2 + (m.x39 - m.x45)**2)**(-3) * (((m.x7 - m.x13)**2 + (
    m.x23 - m.x29)**2 + (m.x39 - m.x45)**2)**(-3) - 2) + ((m.x7 - m.x14)**2 + (
    m.x23 - m.x30)**2 + (m.x39 - m.x46)**2)**(-3) * (((m.x7 - m.x14)**2 + (
    m.x23 - m.x30)**2 + (m.x39 - m.x46)**2)**(-3) - 2) + ((m.x7 - m.x15)**2 + (
    m.x23 - m.x31)**2 + (m.x39 - m.x47)**2)**(-3) * (((m.x7 - m.x15)**2 + (
    m.x23 - m.x31)**2 + (m.x39 - m.x47)**2)**(-3) - 2) + ((m.x7 - m.x16)**2 + (
    m.x23 - m.x32)**2 + (m.x39 - m.x48)**2)**(-3) * (((m.x7 - m.x16)**2 + (
    m.x23 - m.x32)**2 + (m.x39 - m.x48)**2)**(-3) - 2) + ((m.x8 - m.x9)**2 + (
    m.x24 - m.x25)**2 + (m.x40 - m.x41)**2)**(-3) * (((m.x8 - m.x9)**2 + (m.x24
    - m.x25)**2 + (m.x40 - m.x41)**2)**(-3) - 2) + ((m.x8 - m.x10)**2 + (m.x24
    - m.x26)**2 + (m.x40 - m.x42)**2)**(-3) * (((m.x8 - m.x10)**2 + (m.x24 -
    m.x26)**2 + (m.x40 - m.x42)**2)**(-3) - 2) + ((m.x8 - m.x11)**2 + (m.x24 -
    m.x27)**2 + (m.x40 - m.x43)**2)**(-3) * (((m.x8 - m.x11)**2 + (m.x24 -
    m.x27)**2 + (m.x40 - m.x43)**2)**(-3) - 2) + ((m.x8 - m.x12)**2 + (m.x24 -
    m.x28)**2 + (m.x40 - m.x44)**2)**(-3) * (((m.x8 - m.x12)**2 + (m.x24 -
    m.x28)**2 + (m.x40 - m.x44)**2)**(-3) - 2) + ((m.x8 - m.x13)**2 + (m.x24 -
    m.x29)**2 + (m.x40 - m.x45)**2)**(-3) * (((m.x8 - m.x13)**2 + (m.x24 -
    m.x29)**2 + (m.x40 - m.x45)**2)**(-3) - 2) + ((m.x8 - m.x14)**2 + (m.x24 -
    m.x30)**2 + (m.x40 - m.x46)**2)**(-3) * (((m.x8 - m.x14)**2 + (m.x24 -
    m.x30)**2 + (m.x40 - m.x46)**2)**(-3) - 2) + ((m.x8 - m.x15)**2 + (m.x24 -
    m.x31)**2 + (m.x40 - m.x47)**2)**(-3) * (((m.x8 - m.x15)**2 + (m.x24 -
    m.x31)**2 + (m.x40 - m.x47)**2)**(-3) - 2) + ((m.x8 - m.x16)**2 + (m.x24 -
    m.x32)**2 + (m.x40 - m.x48)**2)**(-3) * (((m.x8 - m.x16)**2 + (m.x24 -
    m.x32)**2 + (m.x40 - m.x48)**2)**(-3) - 2) + ((m.x9 - m.x10)**2 + (m.x25 -
    m.x26)**2 + (m.x41 - m.x42)**2)**(-3) * (((m.x9 - m.x10)**2 + (m.x25 -
    m.x26)**2 + (m.x41 - m.x42)**2)**(-3) - 2) + ((m.x9 - m.x11)**2 + (m.x25 -
    m.x27)**2 + (m.x41 - m.x43)**2)**(-3) * (((m.x9 - m.x11)**2 + (m.x25 -
    m.x27)**2 + (m.x41 - m.x43)**2)**(-3) - 2) + ((m.x9 - m.x12)**2 + (m.x25 -
    m.x28)**2 + (m.x41 - m.x44)**2)**(-3) * (((m.x9 - m.x12)**2 + (m.x25 -
    m.x28)**2 + (m.x41 - m.x44)**2)**(-3) - 2) + ((m.x9 - m.x13)**2 + (m.x25 -
    m.x29)**2 + (m.x41 - m.x45)**2)**(-3) * (((m.x9 - m.x13)**2 + (m.x25 -
    m.x29)**2 + (m.x41 - m.x45)**2)**(-3) - 2) + ((m.x9 - m.x14)**2 + (m.x25 -
    m.x30)**2 + (m.x41 - m.x46)**2)**(-3) * (((m.x9 - m.x14)**2 + (m.x25 -
    m.x30)**2 + (m.x41 - m.x46)**2)**(-3) - 2) + ((m.x9 - m.x15)**2 + (m.x25 -
    m.x31)**2 + (m.x41 - m.x47)**2)**(-3) * (((m.x9 - m.x15)**2 + (m.x25 -
    m.x31)**2 + (m.x41 - m.x47)**2)**(-3) - 2) + ((m.x9 - m.x16)**2 + (m.x25 -
    m.x32)**2 + (m.x41 - m.x48)**2)**(-3) * (((m.x9 - m.x16)**2 + (m.x25 -
    m.x32)**2 + (m.x41 - m.x48)**2)**(-3) - 2) + ((m.x10 - m.x11)**2 + (m.x26
    - m.x27)**2 + (m.x42 - m.x43)**2)**(-3) * (((m.x10 - m.x11)**2 + (m.x26 -
    m.x27)**2 + (m.x42 - m.x43)**2)**(-3) - 2) + ((m.x10 - m.x12)**2 + (m.x26
    - m.x28)**2 + (m.x42 - m.x44)**2)**(-3) * (((m.x10 - m.x12)**2 + (m.x26 -
    m.x28)**2 + (m.x42 - m.x44)**2)**(-3) - 2) + ((m.x10 - m.x13)**2 + (m.x26
    - m.x29)**2 + (m.x42 - m.x45)**2)**(-3) * (((m.x10 - m.x13)**2 + (m.x26 -
    m.x29)**2 + (m.x42 - m.x45)**2)**(-3) - 2) + ((m.x10 - m.x14)**2 + (m.x26
    - m.x30)**2 + (m.x42 - m.x46)**2)**(-3) * (((m.x10 - m.x14)**2 + (m.x26 -
    m.x30)**2 + (m.x42 - m.x46)**2)**(-3) - 2) + ((m.x10 - m.x15)**2 + (m.x26
    - m.x31)**2 + (m.x42 - m.x47)**2)**(-3) * (((m.x10 - m.x15)**2 + (m.x26 -
    m.x31)**2 + (m.x42 - m.x47)**2)**(-3) - 2) + ((m.x10 - m.x16)**2 + (m.x26
    - m.x32)**2 + (m.x42 - m.x48)**2)**(-3) * (((m.x10 - m.x16)**2 + (m.x26 -
    m.x32)**2 + (m.x42 - m.x48)**2)**(-3) - 2) + ((m.x11 - m.x12)**2 + (m.x27
    - m.x28)**2 + (m.x43 - m.x44)**2)**(-3) * (((m.x11 - m.x12)**2 + (m.x27 -
    m.x28)**2 + (m.x43 - m.x44)**2)**(-3) - 2) + ((m.x11 - m.x13)**2 + (m.x27
    - m.x29)**2 + (m.x43 - m.x45)**2)**(-3) * (((m.x11 - m.x13)**2 + (m.x27 -
    m.x29)**2 + (m.x43 - m.x45)**2)**(-3) - 2) + ((m.x11 - m.x14)**2 + (m.x27
    - m.x30)**2 + (m.x43 - m.x46)**2)**(-3) * (((m.x11 - m.x14)**2 + (m.x27 -
    m.x30)**2 + (m.x43 - m.x46)**2)**(-3) - 2) + ((m.x11 - m.x15)**2 + (m.x27
    - m.x31)**2 + (m.x43 - m.x47)**2)**(-3) * (((m.x11 - m.x15)**2 + (m.x27 -
    m.x31)**2 + (m.x43 - m.x47)**2)**(-3) - 2) + ((m.x11 - m.x16)**2 + (m.x27
    - m.x32)**2 + (m.x43 - m.x48)**2)**(-3) * (((m.x11 - m.x16)**2 + (m.x27 -
    m.x32)**2 + (m.x43 - m.x48)**2)**(-3) - 2) + ((m.x12 - m.x13)**2 + (m.x28
    - m.x29)**2 + (m.x44 - m.x45)**2)**(-3) * (((m.x12 - m.x13)**2 + (m.x28 -
    m.x29)**2 + (m.x44 - m.x45)**2)**(-3) - 2) + ((m.x12 - m.x14)**2 + (m.x28
    - m.x30)**2 + (m.x44 - m.x46)**2)**(-3) * (((m.x12 - m.x14)**2 + (m.x28 -
    m.x30)**2 + (m.x44 - m.x46)**2)**(-3) - 2) + ((m.x12 - m.x15)**2 + (m.x28
    - m.x31)**2 + (m.x44 - m.x47)**2)**(-3) * (((m.x12 - m.x15)**2 + (m.x28 -
    m.x31)**2 + (m.x44 - m.x47)**2)**(-3) - 2) + ((m.x12 - m.x16)**2 + (m.x28
    - m.x32)**2 + (m.x44 - m.x48)**2)**(-3) * (((m.x12 - m.x16)**2 + (m.x28 -
    m.x32)**2 + (m.x44 - m.x48)**2)**(-3) - 2) + ((m.x13 - m.x14)**2 + (m.x29
    - m.x30)**2 + (m.x45 - m.x46)**2)**(-3) * (((m.x13 - m.x14)**2 + (m.x29 -
    m.x30)**2 + (m.x45 - m.x46)**2)**(-3) - 2) + ((m.x13 - m.x15)**2 + (m.x29
    - m.x31)**2 + (m.x45 - m.x47)**2)**(-3) * (((m.x13 - m.x15)**2 + (m.x29 -
    m.x31)**2 + (m.x45 - m.x47)**2)**(-3) - 2) + ((m.x13 - m.x16)**2 + (m.x29
    - m.x32)**2 + (m.x45 - m.x48)**2)**(-3) * (((m.x13 - m.x16)**2 + (m.x29 -
    m.x32)**2 + (m.x45 - m.x48)**2)**(-3) - 2) + ((m.x14 - m.x15)**2 + (m.x30
    - m.x31)**2 + (m.x46 - m.x47)**2)**(-3) * (((m.x14 - m.x15)**2 + (m.x30 -
    m.x31)**2 + (m.x46 - m.x47)**2)**(-3) - 2) + ((m.x14 - m.x16)**2 + (m.x30
    - m.x32)**2 + (m.x46 - m.x48)**2)**(-3) * (((m.x14 - m.x16)**2 + (m.x30 -
    m.x32)**2 + (m.x46 - m.x48)**2)**(-3) - 2) + ((m.x15 - m.x16)**2 + (m.x31
    - m.x32)**2 + (m.x47 - m.x48)**2)**(-3) * (((m.x15 - m.x16)**2 + (m.x31 -
    m.x32)**2 + (m.x47 - m.x48)**2)**(-3) - 2))

m.e1 = Constraint(expr= (m.x1 - m.x2)**2 + (m.x17 - m.x18)**2 + (m.x33 - m.x34)
    **2 >= 0.46785600000000005)
m.e2 = Constraint(expr= (m.x1 - m.x3)**2 + (m.x17 - m.x19)**2 + (m.x33 - m.x35)
    **2 >= 0.46785600000000005)
m.e3 = Constraint(expr= (m.x1 - m.x4)**2 + (m.x17 - m.x20)**2 + (m.x33 - m.x36)
    **2 >= 0.46785600000000005)
m.e4 = Constraint(expr= (m.x1 - m.x5)**2 + (m.x17 - m.x21)**2 + (m.x33 - m.x37)
    **2 >= 0.46785600000000005)
m.e5 = Constraint(expr= (m.x1 - m.x6)**2 + (m.x17 - m.x22)**2 + (m.x33 - m.x38)
    **2 >= 0.46785600000000005)
m.e6 = Constraint(expr= (m.x1 - m.x7)**2 + (m.x17 - m.x23)**2 + (m.x33 - m.x39)
    **2 >= 0.46785600000000005)
m.e7 = Constraint(expr= (m.x1 - m.x8)**2 + (m.x17 - m.x24)**2 + (m.x33 - m.x40)
    **2 >= 0.46785600000000005)
m.e8 = Constraint(expr= (m.x1 - m.x9)**2 + (m.x17 - m.x25)**2 + (m.x33 - m.x41)
    **2 >= 0.46785600000000005)
m.e9 = Constraint(expr= (m.x1 - m.x10)**2 + (m.x17 - m.x26)**2 + (m.x33 - m.x42)
    **2 >= 0.46785600000000005)
m.e10 = Constraint(expr= (m.x1 - m.x11)**2 + (m.x17 - m.x27)**2 + (m.x33 -
    m.x43)**2 >= 0.46785600000000005)
m.e11 = Constraint(expr= (m.x1 - m.x12)**2 + (m.x17 - m.x28)**2 + (m.x33 -
    m.x44)**2 >= 0.46785600000000005)
m.e12 = Constraint(expr= (m.x1 - m.x13)**2 + (m.x17 - m.x29)**2 + (m.x33 -
    m.x45)**2 >= 0.46785600000000005)
m.e13 = Constraint(expr= (m.x1 - m.x14)**2 + (m.x17 - m.x30)**2 + (m.x33 -
    m.x46)**2 >= 0.46785600000000005)
m.e14 = Constraint(expr= (m.x1 - m.x15)**2 + (m.x17 - m.x31)**2 + (m.x33 -
    m.x47)**2 >= 0.46785600000000005)
m.e15 = Constraint(expr= (m.x1 - m.x16)**2 + (m.x17 - m.x32)**2 + (m.x33 -
    m.x48)**2 >= 0.46785600000000005)
m.e16 = Constraint(expr= (m.x2 - m.x3)**2 + (m.x18 - m.x19)**2 + (m.x34 - m.x35)
    **2 >= 0.46785600000000005)
m.e17 = Constraint(expr= (m.x2 - m.x4)**2 + (m.x18 - m.x20)**2 + (m.x34 - m.x36)
    **2 >= 0.46785600000000005)
m.e18 = Constraint(expr= (m.x2 - m.x5)**2 + (m.x18 - m.x21)**2 + (m.x34 - m.x37)
    **2 >= 0.46785600000000005)
m.e19 = Constraint(expr= (m.x2 - m.x6)**2 + (m.x18 - m.x22)**2 + (m.x34 - m.x38)
    **2 >= 0.46785600000000005)
m.e20 = Constraint(expr= (m.x2 - m.x7)**2 + (m.x18 - m.x23)**2 + (m.x34 - m.x39)
    **2 >= 0.46785600000000005)
m.e21 = Constraint(expr= (m.x2 - m.x8)**2 + (m.x18 - m.x24)**2 + (m.x34 - m.x40)
    **2 >= 0.46785600000000005)
m.e22 = Constraint(expr= (m.x2 - m.x9)**2 + (m.x18 - m.x25)**2 + (m.x34 - m.x41)
    **2 >= 0.46785600000000005)
m.e23 = Constraint(expr= (m.x2 - m.x10)**2 + (m.x18 - m.x26)**2 + (m.x34 -
    m.x42)**2 >= 0.46785600000000005)
m.e24 = Constraint(expr= (m.x2 - m.x11)**2 + (m.x18 - m.x27)**2 + (m.x34 -
    m.x43)**2 >= 0.46785600000000005)
m.e25 = Constraint(expr= (m.x2 - m.x12)**2 + (m.x18 - m.x28)**2 + (m.x34 -
    m.x44)**2 >= 0.46785600000000005)
m.e26 = Constraint(expr= (m.x2 - m.x13)**2 + (m.x18 - m.x29)**2 + (m.x34 -
    m.x45)**2 >= 0.46785600000000005)
m.e27 = Constraint(expr= (m.x2 - m.x14)**2 + (m.x18 - m.x30)**2 + (m.x34 -
    m.x46)**2 >= 0.46785600000000005)
m.e28 = Constraint(expr= (m.x2 - m.x15)**2 + (m.x18 - m.x31)**2 + (m.x34 -
    m.x47)**2 >= 0.46785600000000005)
m.e29 = Constraint(expr= (m.x2 - m.x16)**2 + (m.x18 - m.x32)**2 + (m.x34 -
    m.x48)**2 >= 0.46785600000000005)
m.e30 = Constraint(expr= (m.x3 - m.x4)**2 + (m.x19 - m.x20)**2 + (m.x35 - m.x36)
    **2 >= 0.46785600000000005)
m.e31 = Constraint(expr= (m.x3 - m.x5)**2 + (m.x19 - m.x21)**2 + (m.x35 - m.x37)
    **2 >= 0.46785600000000005)
m.e32 = Constraint(expr= (m.x3 - m.x6)**2 + (m.x19 - m.x22)**2 + (m.x35 - m.x38)
    **2 >= 0.46785600000000005)
m.e33 = Constraint(expr= (m.x3 - m.x7)**2 + (m.x19 - m.x23)**2 + (m.x35 - m.x39)
    **2 >= 0.46785600000000005)
m.e34 = Constraint(expr= (m.x3 - m.x8)**2 + (m.x19 - m.x24)**2 + (m.x35 - m.x40)
    **2 >= 0.46785600000000005)
m.e35 = Constraint(expr= (m.x3 - m.x9)**2 + (m.x19 - m.x25)**2 + (m.x35 - m.x41)
    **2 >= 0.46785600000000005)
m.e36 = Constraint(expr= (m.x3 - m.x10)**2 + (m.x19 - m.x26)**2 + (m.x35 -
    m.x42)**2 >= 0.46785600000000005)
m.e37 = Constraint(expr= (m.x3 - m.x11)**2 + (m.x19 - m.x27)**2 + (m.x35 -
    m.x43)**2 >= 0.46785600000000005)
m.e38 = Constraint(expr= (m.x3 - m.x12)**2 + (m.x19 - m.x28)**2 + (m.x35 -
    m.x44)**2 >= 0.46785600000000005)
m.e39 = Constraint(expr= (m.x3 - m.x13)**2 + (m.x19 - m.x29)**2 + (m.x35 -
    m.x45)**2 >= 0.46785600000000005)
m.e40 = Constraint(expr= (m.x3 - m.x14)**2 + (m.x19 - m.x30)**2 + (m.x35 -
    m.x46)**2 >= 0.46785600000000005)
m.e41 = Constraint(expr= (m.x3 - m.x15)**2 + (m.x19 - m.x31)**2 + (m.x35 -
    m.x47)**2 >= 0.46785600000000005)
m.e42 = Constraint(expr= (m.x3 - m.x16)**2 + (m.x19 - m.x32)**2 + (m.x35 -
    m.x48)**2 >= 0.46785600000000005)
m.e43 = Constraint(expr= (m.x4 - m.x5)**2 + (m.x20 - m.x21)**2 + (m.x36 - m.x37)
    **2 >= 0.46785600000000005)
m.e44 = Constraint(expr= (m.x4 - m.x6)**2 + (m.x20 - m.x22)**2 + (m.x36 - m.x38)
    **2 >= 0.46785600000000005)
m.e45 = Constraint(expr= (m.x4 - m.x7)**2 + (m.x20 - m.x23)**2 + (m.x36 - m.x39)
    **2 >= 0.46785600000000005)
m.e46 = Constraint(expr= (m.x4 - m.x8)**2 + (m.x20 - m.x24)**2 + (m.x36 - m.x40)
    **2 >= 0.46785600000000005)
m.e47 = Constraint(expr= (m.x4 - m.x9)**2 + (m.x20 - m.x25)**2 + (m.x36 - m.x41)
    **2 >= 0.46785600000000005)
m.e48 = Constraint(expr= (m.x4 - m.x10)**2 + (m.x20 - m.x26)**2 + (m.x36 -
    m.x42)**2 >= 0.46785600000000005)
m.e49 = Constraint(expr= (m.x4 - m.x11)**2 + (m.x20 - m.x27)**2 + (m.x36 -
    m.x43)**2 >= 0.46785600000000005)
m.e50 = Constraint(expr= (m.x4 - m.x12)**2 + (m.x20 - m.x28)**2 + (m.x36 -
    m.x44)**2 >= 0.46785600000000005)
m.e51 = Constraint(expr= (m.x4 - m.x13)**2 + (m.x20 - m.x29)**2 + (m.x36 -
    m.x45)**2 >= 0.46785600000000005)
m.e52 = Constraint(expr= (m.x4 - m.x14)**2 + (m.x20 - m.x30)**2 + (m.x36 -
    m.x46)**2 >= 0.46785600000000005)
m.e53 = Constraint(expr= (m.x4 - m.x15)**2 + (m.x20 - m.x31)**2 + (m.x36 -
    m.x47)**2 >= 0.46785600000000005)
m.e54 = Constraint(expr= (m.x4 - m.x16)**2 + (m.x20 - m.x32)**2 + (m.x36 -
    m.x48)**2 >= 0.46785600000000005)
m.e55 = Constraint(expr= (m.x5 - m.x6)**2 + (m.x21 - m.x22)**2 + (m.x37 - m.x38)
    **2 >= 0.46785600000000005)
m.e56 = Constraint(expr= (m.x5 - m.x7)**2 + (m.x21 - m.x23)**2 + (m.x37 - m.x39)
    **2 >= 0.46785600000000005)
m.e57 = Constraint(expr= (m.x5 - m.x8)**2 + (m.x21 - m.x24)**2 + (m.x37 - m.x40)
    **2 >= 0.46785600000000005)
m.e58 = Constraint(expr= (m.x5 - m.x9)**2 + (m.x21 - m.x25)**2 + (m.x37 - m.x41)
    **2 >= 0.46785600000000005)
m.e59 = Constraint(expr= (m.x5 - m.x10)**2 + (m.x21 - m.x26)**2 + (m.x37 -
    m.x42)**2 >= 0.46785600000000005)
m.e60 = Constraint(expr= (m.x5 - m.x11)**2 + (m.x21 - m.x27)**2 + (m.x37 -
    m.x43)**2 >= 0.46785600000000005)
m.e61 = Constraint(expr= (m.x5 - m.x12)**2 + (m.x21 - m.x28)**2 + (m.x37 -
    m.x44)**2 >= 0.46785600000000005)
m.e62 = Constraint(expr= (m.x5 - m.x13)**2 + (m.x21 - m.x29)**2 + (m.x37 -
    m.x45)**2 >= 0.46785600000000005)
m.e63 = Constraint(expr= (m.x5 - m.x14)**2 + (m.x21 - m.x30)**2 + (m.x37 -
    m.x46)**2 >= 0.46785600000000005)
m.e64 = Constraint(expr= (m.x5 - m.x15)**2 + (m.x21 - m.x31)**2 + (m.x37 -
    m.x47)**2 >= 0.46785600000000005)
m.e65 = Constraint(expr= (m.x5 - m.x16)**2 + (m.x21 - m.x32)**2 + (m.x37 -
    m.x48)**2 >= 0.46785600000000005)
m.e66 = Constraint(expr= (m.x6 - m.x7)**2 + (m.x22 - m.x23)**2 + (m.x38 - m.x39)
    **2 >= 0.46785600000000005)
m.e67 = Constraint(expr= (m.x6 - m.x8)**2 + (m.x22 - m.x24)**2 + (m.x38 - m.x40)
    **2 >= 0.46785600000000005)
m.e68 = Constraint(expr= (m.x6 - m.x9)**2 + (m.x22 - m.x25)**2 + (m.x38 - m.x41)
    **2 >= 0.46785600000000005)
m.e69 = Constraint(expr= (m.x6 - m.x10)**2 + (m.x22 - m.x26)**2 + (m.x38 -
    m.x42)**2 >= 0.46785600000000005)
m.e70 = Constraint(expr= (m.x6 - m.x11)**2 + (m.x22 - m.x27)**2 + (m.x38 -
    m.x43)**2 >= 0.46785600000000005)
m.e71 = Constraint(expr= (m.x6 - m.x12)**2 + (m.x22 - m.x28)**2 + (m.x38 -
    m.x44)**2 >= 0.46785600000000005)
m.e72 = Constraint(expr= (m.x6 - m.x13)**2 + (m.x22 - m.x29)**2 + (m.x38 -
    m.x45)**2 >= 0.46785600000000005)
m.e73 = Constraint(expr= (m.x6 - m.x14)**2 + (m.x22 - m.x30)**2 + (m.x38 -
    m.x46)**2 >= 0.46785600000000005)
m.e74 = Constraint(expr= (m.x6 - m.x15)**2 + (m.x22 - m.x31)**2 + (m.x38 -
    m.x47)**2 >= 0.46785600000000005)
m.e75 = Constraint(expr= (m.x6 - m.x16)**2 + (m.x22 - m.x32)**2 + (m.x38 -
    m.x48)**2 >= 0.46785600000000005)
m.e76 = Constraint(expr= (m.x7 - m.x8)**2 + (m.x23 - m.x24)**2 + (m.x39 - m.x40)
    **2 >= 0.46785600000000005)
m.e77 = Constraint(expr= (m.x7 - m.x9)**2 + (m.x23 - m.x25)**2 + (m.x39 - m.x41)
    **2 >= 0.46785600000000005)
m.e78 = Constraint(expr= (m.x7 - m.x10)**2 + (m.x23 - m.x26)**2 + (m.x39 -
    m.x42)**2 >= 0.46785600000000005)
m.e79 = Constraint(expr= (m.x7 - m.x11)**2 + (m.x23 - m.x27)**2 + (m.x39 -
    m.x43)**2 >= 0.46785600000000005)
m.e80 = Constraint(expr= (m.x7 - m.x12)**2 + (m.x23 - m.x28)**2 + (m.x39 -
    m.x44)**2 >= 0.46785600000000005)
m.e81 = Constraint(expr= (m.x7 - m.x13)**2 + (m.x23 - m.x29)**2 + (m.x39 -
    m.x45)**2 >= 0.46785600000000005)
m.e82 = Constraint(expr= (m.x7 - m.x14)**2 + (m.x23 - m.x30)**2 + (m.x39 -
    m.x46)**2 >= 0.46785600000000005)
m.e83 = Constraint(expr= (m.x7 - m.x15)**2 + (m.x23 - m.x31)**2 + (m.x39 -
    m.x47)**2 >= 0.46785600000000005)
m.e84 = Constraint(expr= (m.x7 - m.x16)**2 + (m.x23 - m.x32)**2 + (m.x39 -
    m.x48)**2 >= 0.46785600000000005)
m.e85 = Constraint(expr= (m.x8 - m.x9)**2 + (m.x24 - m.x25)**2 + (m.x40 - m.x41)
    **2 >= 0.46785600000000005)
m.e86 = Constraint(expr= (m.x8 - m.x10)**2 + (m.x24 - m.x26)**2 + (m.x40 -
    m.x42)**2 >= 0.46785600000000005)
m.e87 = Constraint(expr= (m.x8 - m.x11)**2 + (m.x24 - m.x27)**2 + (m.x40 -
    m.x43)**2 >= 0.46785600000000005)
m.e88 = Constraint(expr= (m.x8 - m.x12)**2 + (m.x24 - m.x28)**2 + (m.x40 -
    m.x44)**2 >= 0.46785600000000005)
m.e89 = Constraint(expr= (m.x8 - m.x13)**2 + (m.x24 - m.x29)**2 + (m.x40 -
    m.x45)**2 >= 0.46785600000000005)
m.e90 = Constraint(expr= (m.x8 - m.x14)**2 + (m.x24 - m.x30)**2 + (m.x40 -
    m.x46)**2 >= 0.46785600000000005)
m.e91 = Constraint(expr= (m.x8 - m.x15)**2 + (m.x24 - m.x31)**2 + (m.x40 -
    m.x47)**2 >= 0.46785600000000005)
m.e92 = Constraint(expr= (m.x8 - m.x16)**2 + (m.x24 - m.x32)**2 + (m.x40 -
    m.x48)**2 >= 0.46785600000000005)
m.e93 = Constraint(expr= (m.x9 - m.x10)**2 + (m.x25 - m.x26)**2 + (m.x41 -
    m.x42)**2 >= 0.46785600000000005)
m.e94 = Constraint(expr= (m.x9 - m.x11)**2 + (m.x25 - m.x27)**2 + (m.x41 -
    m.x43)**2 >= 0.46785600000000005)
m.e95 = Constraint(expr= (m.x9 - m.x12)**2 + (m.x25 - m.x28)**2 + (m.x41 -
    m.x44)**2 >= 0.46785600000000005)
m.e96 = Constraint(expr= (m.x9 - m.x13)**2 + (m.x25 - m.x29)**2 + (m.x41 -
    m.x45)**2 >= 0.46785600000000005)
m.e97 = Constraint(expr= (m.x9 - m.x14)**2 + (m.x25 - m.x30)**2 + (m.x41 -
    m.x46)**2 >= 0.46785600000000005)
m.e98 = Constraint(expr= (m.x9 - m.x15)**2 + (m.x25 - m.x31)**2 + (m.x41 -
    m.x47)**2 >= 0.46785600000000005)
m.e99 = Constraint(expr= (m.x9 - m.x16)**2 + (m.x25 - m.x32)**2 + (m.x41 -
    m.x48)**2 >= 0.46785600000000005)
m.e100 = Constraint(expr= (m.x10 - m.x11)**2 + (m.x26 - m.x27)**2 + (m.x42 -
    m.x43)**2 >= 0.46785600000000005)
m.e101 = Constraint(expr= (m.x10 - m.x12)**2 + (m.x26 - m.x28)**2 + (m.x42 -
    m.x44)**2 >= 0.46785600000000005)
m.e102 = Constraint(expr= (m.x10 - m.x13)**2 + (m.x26 - m.x29)**2 + (m.x42 -
    m.x45)**2 >= 0.46785600000000005)
m.e103 = Constraint(expr= (m.x10 - m.x14)**2 + (m.x26 - m.x30)**2 + (m.x42 -
    m.x46)**2 >= 0.46785600000000005)
m.e104 = Constraint(expr= (m.x10 - m.x15)**2 + (m.x26 - m.x31)**2 + (m.x42 -
    m.x47)**2 >= 0.46785600000000005)
m.e105 = Constraint(expr= (m.x10 - m.x16)**2 + (m.x26 - m.x32)**2 + (m.x42 -
    m.x48)**2 >= 0.46785600000000005)
m.e106 = Constraint(expr= (m.x11 - m.x12)**2 + (m.x27 - m.x28)**2 + (m.x43 -
    m.x44)**2 >= 0.46785600000000005)
m.e107 = Constraint(expr= (m.x11 - m.x13)**2 + (m.x27 - m.x29)**2 + (m.x43 -
    m.x45)**2 >= 0.46785600000000005)
m.e108 = Constraint(expr= (m.x11 - m.x14)**2 + (m.x27 - m.x30)**2 + (m.x43 -
    m.x46)**2 >= 0.46785600000000005)
m.e109 = Constraint(expr= (m.x11 - m.x15)**2 + (m.x27 - m.x31)**2 + (m.x43 -
    m.x47)**2 >= 0.46785600000000005)
m.e110 = Constraint(expr= (m.x11 - m.x16)**2 + (m.x27 - m.x32)**2 + (m.x43 -
    m.x48)**2 >= 0.46785600000000005)
m.e111 = Constraint(expr= (m.x12 - m.x13)**2 + (m.x28 - m.x29)**2 + (m.x44 -
    m.x45)**2 >= 0.46785600000000005)
m.e112 = Constraint(expr= (m.x12 - m.x14)**2 + (m.x28 - m.x30)**2 + (m.x44 -
    m.x46)**2 >= 0.46785600000000005)
m.e113 = Constraint(expr= (m.x12 - m.x15)**2 + (m.x28 - m.x31)**2 + (m.x44 -
    m.x47)**2 >= 0.46785600000000005)
m.e114 = Constraint(expr= (m.x12 - m.x16)**2 + (m.x28 - m.x32)**2 + (m.x44 -
    m.x48)**2 >= 0.46785600000000005)
m.e115 = Constraint(expr= (m.x13 - m.x14)**2 + (m.x29 - m.x30)**2 + (m.x45 -
    m.x46)**2 >= 0.46785600000000005)
m.e116 = Constraint(expr= (m.x13 - m.x15)**2 + (m.x29 - m.x31)**2 + (m.x45 -
    m.x47)**2 >= 0.46785600000000005)
m.e117 = Constraint(expr= (m.x13 - m.x16)**2 + (m.x29 - m.x32)**2 + (m.x45 -
    m.x48)**2 >= 0.46785600000000005)
m.e118 = Constraint(expr= (m.x14 - m.x15)**2 + (m.x30 - m.x31)**2 + (m.x46 -
    m.x47)**2 >= 0.46785600000000005)
m.e119 = Constraint(expr= (m.x14 - m.x16)**2 + (m.x30 - m.x32)**2 + (m.x46 -
    m.x48)**2 >= 0.46785600000000005)
m.e120 = Constraint(expr= (m.x15 - m.x16)**2 + (m.x31 - m.x32)**2 + (m.x47 -
    m.x48)**2 >= 0.46785600000000005)
