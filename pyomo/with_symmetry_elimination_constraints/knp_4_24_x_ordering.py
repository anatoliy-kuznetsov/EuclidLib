# NLP written by GAMS Convert at 03/17/24 14:47:58
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       323       24      276       23        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        97       97        0        0        0        0        0        0
# FX      4
#
# Nonzero counts
#     Total    const       NL
#      2626      322     2304
#
# Reformulation has removed 1 variable and 1 equation

from pyomo.environ import *

model = m = ConcreteModel()

m.x1 = Var(within=Reals, bounds=(-2,-2), initialize=-2)
m.x2 = Var(within=Reals, bounds=(0,0), initialize=0)
m.x3 = Var(within=Reals, bounds=(0,0), initialize=0)
m.x4 = Var(within=Reals, bounds=(0,0), initialize=0)
m.x5 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x6 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x7 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x8 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x9 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x10 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x11 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x12 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x13 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x14 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x15 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x16 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x17 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x18 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x19 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x20 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x21 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x22 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x23 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x24 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x25 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x26 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x27 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x28 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x29 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x30 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x31 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x32 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x33 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x34 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x35 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x36 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x37 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x38 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x39 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x40 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x41 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x42 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x43 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x44 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x45 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x46 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x47 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x48 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x49 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x50 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x51 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x52 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x53 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x54 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x55 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x56 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x57 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x58 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x59 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x60 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x61 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x62 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x63 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x64 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x65 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x66 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x67 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x68 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x69 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x70 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x71 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x72 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x73 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x74 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x75 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x76 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x77 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x78 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x79 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x80 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x81 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x82 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x83 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x84 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x85 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x86 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x87 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x88 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x89 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x90 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x91 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x92 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x93 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x94 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x95 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x96 = Var(within=Reals, bounds=(-2,2), initialize=0)
m.x97 = Var(within=Reals, bounds=(None,4), initialize=0)

m.obj = Objective(sense=maximize, expr= m.x97)

m.e1 = Constraint(expr= (m.x1 - m.x5)**2 + (m.x2 - m.x6)**2 + (m.x3 - m.x7)**2
    + (m.x4 - m.x8)**2 - m.x97 >= 0)
m.e2 = Constraint(expr= (m.x1 - m.x9)**2 + (m.x2 - m.x10)**2 + (m.x3 - m.x11)**
    2 + (m.x4 - m.x12)**2 - m.x97 >= 0)
m.e3 = Constraint(expr= (m.x1 - m.x13)**2 + (m.x2 - m.x14)**2 + (m.x3 - m.x15)
    **2 + (m.x4 - m.x16)**2 - m.x97 >= 0)
m.e4 = Constraint(expr= (m.x1 - m.x17)**2 + (m.x2 - m.x18)**2 + (m.x3 - m.x19)
    **2 + (m.x4 - m.x20)**2 - m.x97 >= 0)
m.e5 = Constraint(expr= (m.x1 - m.x21)**2 + (m.x2 - m.x22)**2 + (m.x3 - m.x23)
    **2 + (m.x4 - m.x24)**2 - m.x97 >= 0)
m.e6 = Constraint(expr= (m.x1 - m.x25)**2 + (m.x2 - m.x26)**2 + (m.x3 - m.x27)
    **2 + (m.x4 - m.x28)**2 - m.x97 >= 0)
m.e7 = Constraint(expr= (m.x1 - m.x29)**2 + (m.x2 - m.x30)**2 + (m.x3 - m.x31)
    **2 + (m.x4 - m.x32)**2 - m.x97 >= 0)
m.e8 = Constraint(expr= (m.x1 - m.x33)**2 + (m.x2 - m.x34)**2 + (m.x3 - m.x35)
    **2 + (m.x4 - m.x36)**2 - m.x97 >= 0)
m.e9 = Constraint(expr= (m.x1 - m.x37)**2 + (m.x2 - m.x38)**2 + (m.x3 - m.x39)
    **2 + (m.x4 - m.x40)**2 - m.x97 >= 0)
m.e10 = Constraint(expr= (m.x1 - m.x41)**2 + (m.x2 - m.x42)**2 + (m.x3 - m.x43)
    **2 + (m.x4 - m.x44)**2 - m.x97 >= 0)
m.e11 = Constraint(expr= (m.x1 - m.x45)**2 + (m.x2 - m.x46)**2 + (m.x3 - m.x47)
    **2 + (m.x4 - m.x48)**2 - m.x97 >= 0)
m.e12 = Constraint(expr= (m.x1 - m.x49)**2 + (m.x2 - m.x50)**2 + (m.x3 - m.x51)
    **2 + (m.x4 - m.x52)**2 - m.x97 >= 0)
m.e13 = Constraint(expr= (m.x1 - m.x53)**2 + (m.x2 - m.x54)**2 + (m.x3 - m.x55)
    **2 + (m.x4 - m.x56)**2 - m.x97 >= 0)
m.e14 = Constraint(expr= (m.x1 - m.x57)**2 + (m.x2 - m.x58)**2 + (m.x3 - m.x59)
    **2 + (m.x4 - m.x60)**2 - m.x97 >= 0)
m.e15 = Constraint(expr= (m.x1 - m.x61)**2 + (m.x2 - m.x62)**2 + (m.x3 - m.x63)
    **2 + (m.x4 - m.x64)**2 - m.x97 >= 0)
m.e16 = Constraint(expr= (m.x1 - m.x65)**2 + (m.x2 - m.x66)**2 + (m.x3 - m.x67)
    **2 + (m.x4 - m.x68)**2 - m.x97 >= 0)
m.e17 = Constraint(expr= (m.x1 - m.x69)**2 + (m.x2 - m.x70)**2 + (m.x3 - m.x71)
    **2 + (m.x4 - m.x72)**2 - m.x97 >= 0)
m.e18 = Constraint(expr= (m.x1 - m.x73)**2 + (m.x2 - m.x74)**2 + (m.x3 - m.x75)
    **2 + (m.x4 - m.x76)**2 - m.x97 >= 0)
m.e19 = Constraint(expr= (m.x1 - m.x77)**2 + (m.x2 - m.x78)**2 + (m.x3 - m.x79)
    **2 + (m.x4 - m.x80)**2 - m.x97 >= 0)
m.e20 = Constraint(expr= (m.x1 - m.x81)**2 + (m.x2 - m.x82)**2 + (m.x3 - m.x83)
    **2 + (m.x4 - m.x84)**2 - m.x97 >= 0)
m.e21 = Constraint(expr= (m.x1 - m.x85)**2 + (m.x2 - m.x86)**2 + (m.x3 - m.x87)
    **2 + (m.x4 - m.x88)**2 - m.x97 >= 0)
m.e22 = Constraint(expr= (m.x1 - m.x89)**2 + (m.x2 - m.x90)**2 + (m.x3 - m.x91)
    **2 + (m.x4 - m.x92)**2 - m.x97 >= 0)
m.e23 = Constraint(expr= (m.x1 - m.x93)**2 + (m.x2 - m.x94)**2 + (m.x3 - m.x95)
    **2 + (m.x4 - m.x96)**2 - m.x97 >= 0)
m.e24 = Constraint(expr= (m.x5 - m.x9)**2 + (m.x6 - m.x10)**2 + (m.x7 - m.x11)
    **2 + (m.x8 - m.x12)**2 - m.x97 >= 0)
m.e25 = Constraint(expr= (m.x5 - m.x13)**2 + (m.x6 - m.x14)**2 + (m.x7 - m.x15)
    **2 + (m.x8 - m.x16)**2 - m.x97 >= 0)
m.e26 = Constraint(expr= (m.x5 - m.x17)**2 + (m.x6 - m.x18)**2 + (m.x7 - m.x19)
    **2 + (m.x8 - m.x20)**2 - m.x97 >= 0)
m.e27 = Constraint(expr= (m.x5 - m.x21)**2 + (m.x6 - m.x22)**2 + (m.x7 - m.x23)
    **2 + (m.x8 - m.x24)**2 - m.x97 >= 0)
m.e28 = Constraint(expr= (m.x5 - m.x25)**2 + (m.x6 - m.x26)**2 + (m.x7 - m.x27)
    **2 + (m.x8 - m.x28)**2 - m.x97 >= 0)
m.e29 = Constraint(expr= (m.x5 - m.x29)**2 + (m.x6 - m.x30)**2 + (m.x7 - m.x31)
    **2 + (m.x8 - m.x32)**2 - m.x97 >= 0)
m.e30 = Constraint(expr= (m.x5 - m.x33)**2 + (m.x6 - m.x34)**2 + (m.x7 - m.x35)
    **2 + (m.x8 - m.x36)**2 - m.x97 >= 0)
m.e31 = Constraint(expr= (m.x5 - m.x37)**2 + (m.x6 - m.x38)**2 + (m.x7 - m.x39)
    **2 + (m.x8 - m.x40)**2 - m.x97 >= 0)
m.e32 = Constraint(expr= (m.x5 - m.x41)**2 + (m.x6 - m.x42)**2 + (m.x7 - m.x43)
    **2 + (m.x8 - m.x44)**2 - m.x97 >= 0)
m.e33 = Constraint(expr= (m.x5 - m.x45)**2 + (m.x6 - m.x46)**2 + (m.x7 - m.x47)
    **2 + (m.x8 - m.x48)**2 - m.x97 >= 0)
m.e34 = Constraint(expr= (m.x5 - m.x49)**2 + (m.x6 - m.x50)**2 + (m.x7 - m.x51)
    **2 + (m.x8 - m.x52)**2 - m.x97 >= 0)
m.e35 = Constraint(expr= (m.x5 - m.x53)**2 + (m.x6 - m.x54)**2 + (m.x7 - m.x55)
    **2 + (m.x8 - m.x56)**2 - m.x97 >= 0)
m.e36 = Constraint(expr= (m.x5 - m.x57)**2 + (m.x6 - m.x58)**2 + (m.x7 - m.x59)
    **2 + (m.x8 - m.x60)**2 - m.x97 >= 0)
m.e37 = Constraint(expr= (m.x5 - m.x61)**2 + (m.x6 - m.x62)**2 + (m.x7 - m.x63)
    **2 + (m.x8 - m.x64)**2 - m.x97 >= 0)
m.e38 = Constraint(expr= (m.x5 - m.x65)**2 + (m.x6 - m.x66)**2 + (m.x7 - m.x67)
    **2 + (m.x8 - m.x68)**2 - m.x97 >= 0)
m.e39 = Constraint(expr= (m.x5 - m.x69)**2 + (m.x6 - m.x70)**2 + (m.x7 - m.x71)
    **2 + (m.x8 - m.x72)**2 - m.x97 >= 0)
m.e40 = Constraint(expr= (m.x5 - m.x73)**2 + (m.x6 - m.x74)**2 + (m.x7 - m.x75)
    **2 + (m.x8 - m.x76)**2 - m.x97 >= 0)
m.e41 = Constraint(expr= (m.x5 - m.x77)**2 + (m.x6 - m.x78)**2 + (m.x7 - m.x79)
    **2 + (m.x8 - m.x80)**2 - m.x97 >= 0)
m.e42 = Constraint(expr= (m.x5 - m.x81)**2 + (m.x6 - m.x82)**2 + (m.x7 - m.x83)
    **2 + (m.x8 - m.x84)**2 - m.x97 >= 0)
m.e43 = Constraint(expr= (m.x5 - m.x85)**2 + (m.x6 - m.x86)**2 + (m.x7 - m.x87)
    **2 + (m.x8 - m.x88)**2 - m.x97 >= 0)
m.e44 = Constraint(expr= (m.x5 - m.x89)**2 + (m.x6 - m.x90)**2 + (m.x7 - m.x91)
    **2 + (m.x8 - m.x92)**2 - m.x97 >= 0)
m.e45 = Constraint(expr= (m.x5 - m.x93)**2 + (m.x6 - m.x94)**2 + (m.x7 - m.x95)
    **2 + (m.x8 - m.x96)**2 - m.x97 >= 0)
m.e46 = Constraint(expr= (m.x9 - m.x13)**2 + (m.x10 - m.x14)**2 + (m.x11 -
    m.x15)**2 + (m.x12 - m.x16)**2 - m.x97 >= 0)
m.e47 = Constraint(expr= (m.x9 - m.x17)**2 + (m.x10 - m.x18)**2 + (m.x11 -
    m.x19)**2 + (m.x12 - m.x20)**2 - m.x97 >= 0)
m.e48 = Constraint(expr= (m.x9 - m.x21)**2 + (m.x10 - m.x22)**2 + (m.x11 -
    m.x23)**2 + (m.x12 - m.x24)**2 - m.x97 >= 0)
m.e49 = Constraint(expr= (m.x9 - m.x25)**2 + (m.x10 - m.x26)**2 + (m.x11 -
    m.x27)**2 + (m.x12 - m.x28)**2 - m.x97 >= 0)
m.e50 = Constraint(expr= (m.x9 - m.x29)**2 + (m.x10 - m.x30)**2 + (m.x11 -
    m.x31)**2 + (m.x12 - m.x32)**2 - m.x97 >= 0)
m.e51 = Constraint(expr= (m.x9 - m.x33)**2 + (m.x10 - m.x34)**2 + (m.x11 -
    m.x35)**2 + (m.x12 - m.x36)**2 - m.x97 >= 0)
m.e52 = Constraint(expr= (m.x9 - m.x37)**2 + (m.x10 - m.x38)**2 + (m.x11 -
    m.x39)**2 + (m.x12 - m.x40)**2 - m.x97 >= 0)
m.e53 = Constraint(expr= (m.x9 - m.x41)**2 + (m.x10 - m.x42)**2 + (m.x11 -
    m.x43)**2 + (m.x12 - m.x44)**2 - m.x97 >= 0)
m.e54 = Constraint(expr= (m.x9 - m.x45)**2 + (m.x10 - m.x46)**2 + (m.x11 -
    m.x47)**2 + (m.x12 - m.x48)**2 - m.x97 >= 0)
m.e55 = Constraint(expr= (m.x9 - m.x49)**2 + (m.x10 - m.x50)**2 + (m.x11 -
    m.x51)**2 + (m.x12 - m.x52)**2 - m.x97 >= 0)
m.e56 = Constraint(expr= (m.x9 - m.x53)**2 + (m.x10 - m.x54)**2 + (m.x11 -
    m.x55)**2 + (m.x12 - m.x56)**2 - m.x97 >= 0)
m.e57 = Constraint(expr= (m.x9 - m.x57)**2 + (m.x10 - m.x58)**2 + (m.x11 -
    m.x59)**2 + (m.x12 - m.x60)**2 - m.x97 >= 0)
m.e58 = Constraint(expr= (m.x9 - m.x61)**2 + (m.x10 - m.x62)**2 + (m.x11 -
    m.x63)**2 + (m.x12 - m.x64)**2 - m.x97 >= 0)
m.e59 = Constraint(expr= (m.x9 - m.x65)**2 + (m.x10 - m.x66)**2 + (m.x11 -
    m.x67)**2 + (m.x12 - m.x68)**2 - m.x97 >= 0)
m.e60 = Constraint(expr= (m.x9 - m.x69)**2 + (m.x10 - m.x70)**2 + (m.x11 -
    m.x71)**2 + (m.x12 - m.x72)**2 - m.x97 >= 0)
m.e61 = Constraint(expr= (m.x9 - m.x73)**2 + (m.x10 - m.x74)**2 + (m.x11 -
    m.x75)**2 + (m.x12 - m.x76)**2 - m.x97 >= 0)
m.e62 = Constraint(expr= (m.x9 - m.x77)**2 + (m.x10 - m.x78)**2 + (m.x11 -
    m.x79)**2 + (m.x12 - m.x80)**2 - m.x97 >= 0)
m.e63 = Constraint(expr= (m.x9 - m.x81)**2 + (m.x10 - m.x82)**2 + (m.x11 -
    m.x83)**2 + (m.x12 - m.x84)**2 - m.x97 >= 0)
m.e64 = Constraint(expr= (m.x9 - m.x85)**2 + (m.x10 - m.x86)**2 + (m.x11 -
    m.x87)**2 + (m.x12 - m.x88)**2 - m.x97 >= 0)
m.e65 = Constraint(expr= (m.x9 - m.x89)**2 + (m.x10 - m.x90)**2 + (m.x11 -
    m.x91)**2 + (m.x12 - m.x92)**2 - m.x97 >= 0)
m.e66 = Constraint(expr= (m.x9 - m.x93)**2 + (m.x10 - m.x94)**2 + (m.x11 -
    m.x95)**2 + (m.x12 - m.x96)**2 - m.x97 >= 0)
m.e67 = Constraint(expr= (m.x13 - m.x17)**2 + (m.x14 - m.x18)**2 + (m.x15 -
    m.x19)**2 + (m.x16 - m.x20)**2 - m.x97 >= 0)
m.e68 = Constraint(expr= (m.x13 - m.x21)**2 + (m.x14 - m.x22)**2 + (m.x15 -
    m.x23)**2 + (m.x16 - m.x24)**2 - m.x97 >= 0)
m.e69 = Constraint(expr= (m.x13 - m.x25)**2 + (m.x14 - m.x26)**2 + (m.x15 -
    m.x27)**2 + (m.x16 - m.x28)**2 - m.x97 >= 0)
m.e70 = Constraint(expr= (m.x13 - m.x29)**2 + (m.x14 - m.x30)**2 + (m.x15 -
    m.x31)**2 + (m.x16 - m.x32)**2 - m.x97 >= 0)
m.e71 = Constraint(expr= (m.x13 - m.x33)**2 + (m.x14 - m.x34)**2 + (m.x15 -
    m.x35)**2 + (m.x16 - m.x36)**2 - m.x97 >= 0)
m.e72 = Constraint(expr= (m.x13 - m.x37)**2 + (m.x14 - m.x38)**2 + (m.x15 -
    m.x39)**2 + (m.x16 - m.x40)**2 - m.x97 >= 0)
m.e73 = Constraint(expr= (m.x13 - m.x41)**2 + (m.x14 - m.x42)**2 + (m.x15 -
    m.x43)**2 + (m.x16 - m.x44)**2 - m.x97 >= 0)
m.e74 = Constraint(expr= (m.x13 - m.x45)**2 + (m.x14 - m.x46)**2 + (m.x15 -
    m.x47)**2 + (m.x16 - m.x48)**2 - m.x97 >= 0)
m.e75 = Constraint(expr= (m.x13 - m.x49)**2 + (m.x14 - m.x50)**2 + (m.x15 -
    m.x51)**2 + (m.x16 - m.x52)**2 - m.x97 >= 0)
m.e76 = Constraint(expr= (m.x13 - m.x53)**2 + (m.x14 - m.x54)**2 + (m.x15 -
    m.x55)**2 + (m.x16 - m.x56)**2 - m.x97 >= 0)
m.e77 = Constraint(expr= (m.x13 - m.x57)**2 + (m.x14 - m.x58)**2 + (m.x15 -
    m.x59)**2 + (m.x16 - m.x60)**2 - m.x97 >= 0)
m.e78 = Constraint(expr= (m.x13 - m.x61)**2 + (m.x14 - m.x62)**2 + (m.x15 -
    m.x63)**2 + (m.x16 - m.x64)**2 - m.x97 >= 0)
m.e79 = Constraint(expr= (m.x13 - m.x65)**2 + (m.x14 - m.x66)**2 + (m.x15 -
    m.x67)**2 + (m.x16 - m.x68)**2 - m.x97 >= 0)
m.e80 = Constraint(expr= (m.x13 - m.x69)**2 + (m.x14 - m.x70)**2 + (m.x15 -
    m.x71)**2 + (m.x16 - m.x72)**2 - m.x97 >= 0)
m.e81 = Constraint(expr= (m.x13 - m.x73)**2 + (m.x14 - m.x74)**2 + (m.x15 -
    m.x75)**2 + (m.x16 - m.x76)**2 - m.x97 >= 0)
m.e82 = Constraint(expr= (m.x13 - m.x77)**2 + (m.x14 - m.x78)**2 + (m.x15 -
    m.x79)**2 + (m.x16 - m.x80)**2 - m.x97 >= 0)
m.e83 = Constraint(expr= (m.x13 - m.x81)**2 + (m.x14 - m.x82)**2 + (m.x15 -
    m.x83)**2 + (m.x16 - m.x84)**2 - m.x97 >= 0)
m.e84 = Constraint(expr= (m.x13 - m.x85)**2 + (m.x14 - m.x86)**2 + (m.x15 -
    m.x87)**2 + (m.x16 - m.x88)**2 - m.x97 >= 0)
m.e85 = Constraint(expr= (m.x13 - m.x89)**2 + (m.x14 - m.x90)**2 + (m.x15 -
    m.x91)**2 + (m.x16 - m.x92)**2 - m.x97 >= 0)
m.e86 = Constraint(expr= (m.x13 - m.x93)**2 + (m.x14 - m.x94)**2 + (m.x15 -
    m.x95)**2 + (m.x16 - m.x96)**2 - m.x97 >= 0)
m.e87 = Constraint(expr= (m.x17 - m.x21)**2 + (m.x18 - m.x22)**2 + (m.x19 -
    m.x23)**2 + (m.x20 - m.x24)**2 - m.x97 >= 0)
m.e88 = Constraint(expr= (m.x17 - m.x25)**2 + (m.x18 - m.x26)**2 + (m.x19 -
    m.x27)**2 + (m.x20 - m.x28)**2 - m.x97 >= 0)
m.e89 = Constraint(expr= (m.x17 - m.x29)**2 + (m.x18 - m.x30)**2 + (m.x19 -
    m.x31)**2 + (m.x20 - m.x32)**2 - m.x97 >= 0)
m.e90 = Constraint(expr= (m.x17 - m.x33)**2 + (m.x18 - m.x34)**2 + (m.x19 -
    m.x35)**2 + (m.x20 - m.x36)**2 - m.x97 >= 0)
m.e91 = Constraint(expr= (m.x17 - m.x37)**2 + (m.x18 - m.x38)**2 + (m.x19 -
    m.x39)**2 + (m.x20 - m.x40)**2 - m.x97 >= 0)
m.e92 = Constraint(expr= (m.x17 - m.x41)**2 + (m.x18 - m.x42)**2 + (m.x19 -
    m.x43)**2 + (m.x20 - m.x44)**2 - m.x97 >= 0)
m.e93 = Constraint(expr= (m.x17 - m.x45)**2 + (m.x18 - m.x46)**2 + (m.x19 -
    m.x47)**2 + (m.x20 - m.x48)**2 - m.x97 >= 0)
m.e94 = Constraint(expr= (m.x17 - m.x49)**2 + (m.x18 - m.x50)**2 + (m.x19 -
    m.x51)**2 + (m.x20 - m.x52)**2 - m.x97 >= 0)
m.e95 = Constraint(expr= (m.x17 - m.x53)**2 + (m.x18 - m.x54)**2 + (m.x19 -
    m.x55)**2 + (m.x20 - m.x56)**2 - m.x97 >= 0)
m.e96 = Constraint(expr= (m.x17 - m.x57)**2 + (m.x18 - m.x58)**2 + (m.x19 -
    m.x59)**2 + (m.x20 - m.x60)**2 - m.x97 >= 0)
m.e97 = Constraint(expr= (m.x17 - m.x61)**2 + (m.x18 - m.x62)**2 + (m.x19 -
    m.x63)**2 + (m.x20 - m.x64)**2 - m.x97 >= 0)
m.e98 = Constraint(expr= (m.x17 - m.x65)**2 + (m.x18 - m.x66)**2 + (m.x19 -
    m.x67)**2 + (m.x20 - m.x68)**2 - m.x97 >= 0)
m.e99 = Constraint(expr= (m.x17 - m.x69)**2 + (m.x18 - m.x70)**2 + (m.x19 -
    m.x71)**2 + (m.x20 - m.x72)**2 - m.x97 >= 0)
m.e100 = Constraint(expr= (m.x17 - m.x73)**2 + (m.x18 - m.x74)**2 + (m.x19 -
    m.x75)**2 + (m.x20 - m.x76)**2 - m.x97 >= 0)
m.e101 = Constraint(expr= (m.x17 - m.x77)**2 + (m.x18 - m.x78)**2 + (m.x19 -
    m.x79)**2 + (m.x20 - m.x80)**2 - m.x97 >= 0)
m.e102 = Constraint(expr= (m.x17 - m.x81)**2 + (m.x18 - m.x82)**2 + (m.x19 -
    m.x83)**2 + (m.x20 - m.x84)**2 - m.x97 >= 0)
m.e103 = Constraint(expr= (m.x17 - m.x85)**2 + (m.x18 - m.x86)**2 + (m.x19 -
    m.x87)**2 + (m.x20 - m.x88)**2 - m.x97 >= 0)
m.e104 = Constraint(expr= (m.x17 - m.x89)**2 + (m.x18 - m.x90)**2 + (m.x19 -
    m.x91)**2 + (m.x20 - m.x92)**2 - m.x97 >= 0)
m.e105 = Constraint(expr= (m.x17 - m.x93)**2 + (m.x18 - m.x94)**2 + (m.x19 -
    m.x95)**2 + (m.x20 - m.x96)**2 - m.x97 >= 0)
m.e106 = Constraint(expr= (m.x21 - m.x25)**2 + (m.x22 - m.x26)**2 + (m.x23 -
    m.x27)**2 + (m.x24 - m.x28)**2 - m.x97 >= 0)
m.e107 = Constraint(expr= (m.x21 - m.x29)**2 + (m.x22 - m.x30)**2 + (m.x23 -
    m.x31)**2 + (m.x24 - m.x32)**2 - m.x97 >= 0)
m.e108 = Constraint(expr= (m.x21 - m.x33)**2 + (m.x22 - m.x34)**2 + (m.x23 -
    m.x35)**2 + (m.x24 - m.x36)**2 - m.x97 >= 0)
m.e109 = Constraint(expr= (m.x21 - m.x37)**2 + (m.x22 - m.x38)**2 + (m.x23 -
    m.x39)**2 + (m.x24 - m.x40)**2 - m.x97 >= 0)
m.e110 = Constraint(expr= (m.x21 - m.x41)**2 + (m.x22 - m.x42)**2 + (m.x23 -
    m.x43)**2 + (m.x24 - m.x44)**2 - m.x97 >= 0)
m.e111 = Constraint(expr= (m.x21 - m.x45)**2 + (m.x22 - m.x46)**2 + (m.x23 -
    m.x47)**2 + (m.x24 - m.x48)**2 - m.x97 >= 0)
m.e112 = Constraint(expr= (m.x21 - m.x49)**2 + (m.x22 - m.x50)**2 + (m.x23 -
    m.x51)**2 + (m.x24 - m.x52)**2 - m.x97 >= 0)
m.e113 = Constraint(expr= (m.x21 - m.x53)**2 + (m.x22 - m.x54)**2 + (m.x23 -
    m.x55)**2 + (m.x24 - m.x56)**2 - m.x97 >= 0)
m.e114 = Constraint(expr= (m.x21 - m.x57)**2 + (m.x22 - m.x58)**2 + (m.x23 -
    m.x59)**2 + (m.x24 - m.x60)**2 - m.x97 >= 0)
m.e115 = Constraint(expr= (m.x21 - m.x61)**2 + (m.x22 - m.x62)**2 + (m.x23 -
    m.x63)**2 + (m.x24 - m.x64)**2 - m.x97 >= 0)
m.e116 = Constraint(expr= (m.x21 - m.x65)**2 + (m.x22 - m.x66)**2 + (m.x23 -
    m.x67)**2 + (m.x24 - m.x68)**2 - m.x97 >= 0)
m.e117 = Constraint(expr= (m.x21 - m.x69)**2 + (m.x22 - m.x70)**2 + (m.x23 -
    m.x71)**2 + (m.x24 - m.x72)**2 - m.x97 >= 0)
m.e118 = Constraint(expr= (m.x21 - m.x73)**2 + (m.x22 - m.x74)**2 + (m.x23 -
    m.x75)**2 + (m.x24 - m.x76)**2 - m.x97 >= 0)
m.e119 = Constraint(expr= (m.x21 - m.x77)**2 + (m.x22 - m.x78)**2 + (m.x23 -
    m.x79)**2 + (m.x24 - m.x80)**2 - m.x97 >= 0)
m.e120 = Constraint(expr= (m.x21 - m.x81)**2 + (m.x22 - m.x82)**2 + (m.x23 -
    m.x83)**2 + (m.x24 - m.x84)**2 - m.x97 >= 0)
m.e121 = Constraint(expr= (m.x21 - m.x85)**2 + (m.x22 - m.x86)**2 + (m.x23 -
    m.x87)**2 + (m.x24 - m.x88)**2 - m.x97 >= 0)
m.e122 = Constraint(expr= (m.x21 - m.x89)**2 + (m.x22 - m.x90)**2 + (m.x23 -
    m.x91)**2 + (m.x24 - m.x92)**2 - m.x97 >= 0)
m.e123 = Constraint(expr= (m.x21 - m.x93)**2 + (m.x22 - m.x94)**2 + (m.x23 -
    m.x95)**2 + (m.x24 - m.x96)**2 - m.x97 >= 0)
m.e124 = Constraint(expr= (m.x25 - m.x29)**2 + (m.x26 - m.x30)**2 + (m.x27 -
    m.x31)**2 + (m.x28 - m.x32)**2 - m.x97 >= 0)
m.e125 = Constraint(expr= (m.x25 - m.x33)**2 + (m.x26 - m.x34)**2 + (m.x27 -
    m.x35)**2 + (m.x28 - m.x36)**2 - m.x97 >= 0)
m.e126 = Constraint(expr= (m.x25 - m.x37)**2 + (m.x26 - m.x38)**2 + (m.x27 -
    m.x39)**2 + (m.x28 - m.x40)**2 - m.x97 >= 0)
m.e127 = Constraint(expr= (m.x25 - m.x41)**2 + (m.x26 - m.x42)**2 + (m.x27 -
    m.x43)**2 + (m.x28 - m.x44)**2 - m.x97 >= 0)
m.e128 = Constraint(expr= (m.x25 - m.x45)**2 + (m.x26 - m.x46)**2 + (m.x27 -
    m.x47)**2 + (m.x28 - m.x48)**2 - m.x97 >= 0)
m.e129 = Constraint(expr= (m.x25 - m.x49)**2 + (m.x26 - m.x50)**2 + (m.x27 -
    m.x51)**2 + (m.x28 - m.x52)**2 - m.x97 >= 0)
m.e130 = Constraint(expr= (m.x25 - m.x53)**2 + (m.x26 - m.x54)**2 + (m.x27 -
    m.x55)**2 + (m.x28 - m.x56)**2 - m.x97 >= 0)
m.e131 = Constraint(expr= (m.x25 - m.x57)**2 + (m.x26 - m.x58)**2 + (m.x27 -
    m.x59)**2 + (m.x28 - m.x60)**2 - m.x97 >= 0)
m.e132 = Constraint(expr= (m.x25 - m.x61)**2 + (m.x26 - m.x62)**2 + (m.x27 -
    m.x63)**2 + (m.x28 - m.x64)**2 - m.x97 >= 0)
m.e133 = Constraint(expr= (m.x25 - m.x65)**2 + (m.x26 - m.x66)**2 + (m.x27 -
    m.x67)**2 + (m.x28 - m.x68)**2 - m.x97 >= 0)
m.e134 = Constraint(expr= (m.x25 - m.x69)**2 + (m.x26 - m.x70)**2 + (m.x27 -
    m.x71)**2 + (m.x28 - m.x72)**2 - m.x97 >= 0)
m.e135 = Constraint(expr= (m.x25 - m.x73)**2 + (m.x26 - m.x74)**2 + (m.x27 -
    m.x75)**2 + (m.x28 - m.x76)**2 - m.x97 >= 0)
m.e136 = Constraint(expr= (m.x25 - m.x77)**2 + (m.x26 - m.x78)**2 + (m.x27 -
    m.x79)**2 + (m.x28 - m.x80)**2 - m.x97 >= 0)
m.e137 = Constraint(expr= (m.x25 - m.x81)**2 + (m.x26 - m.x82)**2 + (m.x27 -
    m.x83)**2 + (m.x28 - m.x84)**2 - m.x97 >= 0)
m.e138 = Constraint(expr= (m.x25 - m.x85)**2 + (m.x26 - m.x86)**2 + (m.x27 -
    m.x87)**2 + (m.x28 - m.x88)**2 - m.x97 >= 0)
m.e139 = Constraint(expr= (m.x25 - m.x89)**2 + (m.x26 - m.x90)**2 + (m.x27 -
    m.x91)**2 + (m.x28 - m.x92)**2 - m.x97 >= 0)
m.e140 = Constraint(expr= (m.x25 - m.x93)**2 + (m.x26 - m.x94)**2 + (m.x27 -
    m.x95)**2 + (m.x28 - m.x96)**2 - m.x97 >= 0)
m.e141 = Constraint(expr= (m.x29 - m.x33)**2 + (m.x30 - m.x34)**2 + (m.x31 -
    m.x35)**2 + (m.x32 - m.x36)**2 - m.x97 >= 0)
m.e142 = Constraint(expr= (m.x29 - m.x37)**2 + (m.x30 - m.x38)**2 + (m.x31 -
    m.x39)**2 + (m.x32 - m.x40)**2 - m.x97 >= 0)
m.e143 = Constraint(expr= (m.x29 - m.x41)**2 + (m.x30 - m.x42)**2 + (m.x31 -
    m.x43)**2 + (m.x32 - m.x44)**2 - m.x97 >= 0)
m.e144 = Constraint(expr= (m.x29 - m.x45)**2 + (m.x30 - m.x46)**2 + (m.x31 -
    m.x47)**2 + (m.x32 - m.x48)**2 - m.x97 >= 0)
m.e145 = Constraint(expr= (m.x29 - m.x49)**2 + (m.x30 - m.x50)**2 + (m.x31 -
    m.x51)**2 + (m.x32 - m.x52)**2 - m.x97 >= 0)
m.e146 = Constraint(expr= (m.x29 - m.x53)**2 + (m.x30 - m.x54)**2 + (m.x31 -
    m.x55)**2 + (m.x32 - m.x56)**2 - m.x97 >= 0)
m.e147 = Constraint(expr= (m.x29 - m.x57)**2 + (m.x30 - m.x58)**2 + (m.x31 -
    m.x59)**2 + (m.x32 - m.x60)**2 - m.x97 >= 0)
m.e148 = Constraint(expr= (m.x29 - m.x61)**2 + (m.x30 - m.x62)**2 + (m.x31 -
    m.x63)**2 + (m.x32 - m.x64)**2 - m.x97 >= 0)
m.e149 = Constraint(expr= (m.x29 - m.x65)**2 + (m.x30 - m.x66)**2 + (m.x31 -
    m.x67)**2 + (m.x32 - m.x68)**2 - m.x97 >= 0)
m.e150 = Constraint(expr= (m.x29 - m.x69)**2 + (m.x30 - m.x70)**2 + (m.x31 -
    m.x71)**2 + (m.x32 - m.x72)**2 - m.x97 >= 0)
m.e151 = Constraint(expr= (m.x29 - m.x73)**2 + (m.x30 - m.x74)**2 + (m.x31 -
    m.x75)**2 + (m.x32 - m.x76)**2 - m.x97 >= 0)
m.e152 = Constraint(expr= (m.x29 - m.x77)**2 + (m.x30 - m.x78)**2 + (m.x31 -
    m.x79)**2 + (m.x32 - m.x80)**2 - m.x97 >= 0)
m.e153 = Constraint(expr= (m.x29 - m.x81)**2 + (m.x30 - m.x82)**2 + (m.x31 -
    m.x83)**2 + (m.x32 - m.x84)**2 - m.x97 >= 0)
m.e154 = Constraint(expr= (m.x29 - m.x85)**2 + (m.x30 - m.x86)**2 + (m.x31 -
    m.x87)**2 + (m.x32 - m.x88)**2 - m.x97 >= 0)
m.e155 = Constraint(expr= (m.x29 - m.x89)**2 + (m.x30 - m.x90)**2 + (m.x31 -
    m.x91)**2 + (m.x32 - m.x92)**2 - m.x97 >= 0)
m.e156 = Constraint(expr= (m.x29 - m.x93)**2 + (m.x30 - m.x94)**2 + (m.x31 -
    m.x95)**2 + (m.x32 - m.x96)**2 - m.x97 >= 0)
m.e157 = Constraint(expr= (m.x33 - m.x37)**2 + (m.x34 - m.x38)**2 + (m.x35 -
    m.x39)**2 + (m.x36 - m.x40)**2 - m.x97 >= 0)
m.e158 = Constraint(expr= (m.x33 - m.x41)**2 + (m.x34 - m.x42)**2 + (m.x35 -
    m.x43)**2 + (m.x36 - m.x44)**2 - m.x97 >= 0)
m.e159 = Constraint(expr= (m.x33 - m.x45)**2 + (m.x34 - m.x46)**2 + (m.x35 -
    m.x47)**2 + (m.x36 - m.x48)**2 - m.x97 >= 0)
m.e160 = Constraint(expr= (m.x33 - m.x49)**2 + (m.x34 - m.x50)**2 + (m.x35 -
    m.x51)**2 + (m.x36 - m.x52)**2 - m.x97 >= 0)
m.e161 = Constraint(expr= (m.x33 - m.x53)**2 + (m.x34 - m.x54)**2 + (m.x35 -
    m.x55)**2 + (m.x36 - m.x56)**2 - m.x97 >= 0)
m.e162 = Constraint(expr= (m.x33 - m.x57)**2 + (m.x34 - m.x58)**2 + (m.x35 -
    m.x59)**2 + (m.x36 - m.x60)**2 - m.x97 >= 0)
m.e163 = Constraint(expr= (m.x33 - m.x61)**2 + (m.x34 - m.x62)**2 + (m.x35 -
    m.x63)**2 + (m.x36 - m.x64)**2 - m.x97 >= 0)
m.e164 = Constraint(expr= (m.x33 - m.x65)**2 + (m.x34 - m.x66)**2 + (m.x35 -
    m.x67)**2 + (m.x36 - m.x68)**2 - m.x97 >= 0)
m.e165 = Constraint(expr= (m.x33 - m.x69)**2 + (m.x34 - m.x70)**2 + (m.x35 -
    m.x71)**2 + (m.x36 - m.x72)**2 - m.x97 >= 0)
m.e166 = Constraint(expr= (m.x33 - m.x73)**2 + (m.x34 - m.x74)**2 + (m.x35 -
    m.x75)**2 + (m.x36 - m.x76)**2 - m.x97 >= 0)
m.e167 = Constraint(expr= (m.x33 - m.x77)**2 + (m.x34 - m.x78)**2 + (m.x35 -
    m.x79)**2 + (m.x36 - m.x80)**2 - m.x97 >= 0)
m.e168 = Constraint(expr= (m.x33 - m.x81)**2 + (m.x34 - m.x82)**2 + (m.x35 -
    m.x83)**2 + (m.x36 - m.x84)**2 - m.x97 >= 0)
m.e169 = Constraint(expr= (m.x33 - m.x85)**2 + (m.x34 - m.x86)**2 + (m.x35 -
    m.x87)**2 + (m.x36 - m.x88)**2 - m.x97 >= 0)
m.e170 = Constraint(expr= (m.x33 - m.x89)**2 + (m.x34 - m.x90)**2 + (m.x35 -
    m.x91)**2 + (m.x36 - m.x92)**2 - m.x97 >= 0)
m.e171 = Constraint(expr= (m.x33 - m.x93)**2 + (m.x34 - m.x94)**2 + (m.x35 -
    m.x95)**2 + (m.x36 - m.x96)**2 - m.x97 >= 0)
m.e172 = Constraint(expr= (m.x37 - m.x41)**2 + (m.x38 - m.x42)**2 + (m.x39 -
    m.x43)**2 + (m.x40 - m.x44)**2 - m.x97 >= 0)
m.e173 = Constraint(expr= (m.x37 - m.x45)**2 + (m.x38 - m.x46)**2 + (m.x39 -
    m.x47)**2 + (m.x40 - m.x48)**2 - m.x97 >= 0)
m.e174 = Constraint(expr= (m.x37 - m.x49)**2 + (m.x38 - m.x50)**2 + (m.x39 -
    m.x51)**2 + (m.x40 - m.x52)**2 - m.x97 >= 0)
m.e175 = Constraint(expr= (m.x37 - m.x53)**2 + (m.x38 - m.x54)**2 + (m.x39 -
    m.x55)**2 + (m.x40 - m.x56)**2 - m.x97 >= 0)
m.e176 = Constraint(expr= (m.x37 - m.x57)**2 + (m.x38 - m.x58)**2 + (m.x39 -
    m.x59)**2 + (m.x40 - m.x60)**2 - m.x97 >= 0)
m.e177 = Constraint(expr= (m.x37 - m.x61)**2 + (m.x38 - m.x62)**2 + (m.x39 -
    m.x63)**2 + (m.x40 - m.x64)**2 - m.x97 >= 0)
m.e178 = Constraint(expr= (m.x37 - m.x65)**2 + (m.x38 - m.x66)**2 + (m.x39 -
    m.x67)**2 + (m.x40 - m.x68)**2 - m.x97 >= 0)
m.e179 = Constraint(expr= (m.x37 - m.x69)**2 + (m.x38 - m.x70)**2 + (m.x39 -
    m.x71)**2 + (m.x40 - m.x72)**2 - m.x97 >= 0)
m.e180 = Constraint(expr= (m.x37 - m.x73)**2 + (m.x38 - m.x74)**2 + (m.x39 -
    m.x75)**2 + (m.x40 - m.x76)**2 - m.x97 >= 0)
m.e181 = Constraint(expr= (m.x37 - m.x77)**2 + (m.x38 - m.x78)**2 + (m.x39 -
    m.x79)**2 + (m.x40 - m.x80)**2 - m.x97 >= 0)
m.e182 = Constraint(expr= (m.x37 - m.x81)**2 + (m.x38 - m.x82)**2 + (m.x39 -
    m.x83)**2 + (m.x40 - m.x84)**2 - m.x97 >= 0)
m.e183 = Constraint(expr= (m.x37 - m.x85)**2 + (m.x38 - m.x86)**2 + (m.x39 -
    m.x87)**2 + (m.x40 - m.x88)**2 - m.x97 >= 0)
m.e184 = Constraint(expr= (m.x37 - m.x89)**2 + (m.x38 - m.x90)**2 + (m.x39 -
    m.x91)**2 + (m.x40 - m.x92)**2 - m.x97 >= 0)
m.e185 = Constraint(expr= (m.x37 - m.x93)**2 + (m.x38 - m.x94)**2 + (m.x39 -
    m.x95)**2 + (m.x40 - m.x96)**2 - m.x97 >= 0)
m.e186 = Constraint(expr= (m.x41 - m.x45)**2 + (m.x42 - m.x46)**2 + (m.x43 -
    m.x47)**2 + (m.x44 - m.x48)**2 - m.x97 >= 0)
m.e187 = Constraint(expr= (m.x41 - m.x49)**2 + (m.x42 - m.x50)**2 + (m.x43 -
    m.x51)**2 + (m.x44 - m.x52)**2 - m.x97 >= 0)
m.e188 = Constraint(expr= (m.x41 - m.x53)**2 + (m.x42 - m.x54)**2 + (m.x43 -
    m.x55)**2 + (m.x44 - m.x56)**2 - m.x97 >= 0)
m.e189 = Constraint(expr= (m.x41 - m.x57)**2 + (m.x42 - m.x58)**2 + (m.x43 -
    m.x59)**2 + (m.x44 - m.x60)**2 - m.x97 >= 0)
m.e190 = Constraint(expr= (m.x41 - m.x61)**2 + (m.x42 - m.x62)**2 + (m.x43 -
    m.x63)**2 + (m.x44 - m.x64)**2 - m.x97 >= 0)
m.e191 = Constraint(expr= (m.x41 - m.x65)**2 + (m.x42 - m.x66)**2 + (m.x43 -
    m.x67)**2 + (m.x44 - m.x68)**2 - m.x97 >= 0)
m.e192 = Constraint(expr= (m.x41 - m.x69)**2 + (m.x42 - m.x70)**2 + (m.x43 -
    m.x71)**2 + (m.x44 - m.x72)**2 - m.x97 >= 0)
m.e193 = Constraint(expr= (m.x41 - m.x73)**2 + (m.x42 - m.x74)**2 + (m.x43 -
    m.x75)**2 + (m.x44 - m.x76)**2 - m.x97 >= 0)
m.e194 = Constraint(expr= (m.x41 - m.x77)**2 + (m.x42 - m.x78)**2 + (m.x43 -
    m.x79)**2 + (m.x44 - m.x80)**2 - m.x97 >= 0)
m.e195 = Constraint(expr= (m.x41 - m.x81)**2 + (m.x42 - m.x82)**2 + (m.x43 -
    m.x83)**2 + (m.x44 - m.x84)**2 - m.x97 >= 0)
m.e196 = Constraint(expr= (m.x41 - m.x85)**2 + (m.x42 - m.x86)**2 + (m.x43 -
    m.x87)**2 + (m.x44 - m.x88)**2 - m.x97 >= 0)
m.e197 = Constraint(expr= (m.x41 - m.x89)**2 + (m.x42 - m.x90)**2 + (m.x43 -
    m.x91)**2 + (m.x44 - m.x92)**2 - m.x97 >= 0)
m.e198 = Constraint(expr= (m.x41 - m.x93)**2 + (m.x42 - m.x94)**2 + (m.x43 -
    m.x95)**2 + (m.x44 - m.x96)**2 - m.x97 >= 0)
m.e199 = Constraint(expr= (m.x45 - m.x49)**2 + (m.x46 - m.x50)**2 + (m.x47 -
    m.x51)**2 + (m.x48 - m.x52)**2 - m.x97 >= 0)
m.e200 = Constraint(expr= (m.x45 - m.x53)**2 + (m.x46 - m.x54)**2 + (m.x47 -
    m.x55)**2 + (m.x48 - m.x56)**2 - m.x97 >= 0)
m.e201 = Constraint(expr= (m.x45 - m.x57)**2 + (m.x46 - m.x58)**2 + (m.x47 -
    m.x59)**2 + (m.x48 - m.x60)**2 - m.x97 >= 0)
m.e202 = Constraint(expr= (m.x45 - m.x61)**2 + (m.x46 - m.x62)**2 + (m.x47 -
    m.x63)**2 + (m.x48 - m.x64)**2 - m.x97 >= 0)
m.e203 = Constraint(expr= (m.x45 - m.x65)**2 + (m.x46 - m.x66)**2 + (m.x47 -
    m.x67)**2 + (m.x48 - m.x68)**2 - m.x97 >= 0)
m.e204 = Constraint(expr= (m.x45 - m.x69)**2 + (m.x46 - m.x70)**2 + (m.x47 -
    m.x71)**2 + (m.x48 - m.x72)**2 - m.x97 >= 0)
m.e205 = Constraint(expr= (m.x45 - m.x73)**2 + (m.x46 - m.x74)**2 + (m.x47 -
    m.x75)**2 + (m.x48 - m.x76)**2 - m.x97 >= 0)
m.e206 = Constraint(expr= (m.x45 - m.x77)**2 + (m.x46 - m.x78)**2 + (m.x47 -
    m.x79)**2 + (m.x48 - m.x80)**2 - m.x97 >= 0)
m.e207 = Constraint(expr= (m.x45 - m.x81)**2 + (m.x46 - m.x82)**2 + (m.x47 -
    m.x83)**2 + (m.x48 - m.x84)**2 - m.x97 >= 0)
m.e208 = Constraint(expr= (m.x45 - m.x85)**2 + (m.x46 - m.x86)**2 + (m.x47 -
    m.x87)**2 + (m.x48 - m.x88)**2 - m.x97 >= 0)
m.e209 = Constraint(expr= (m.x45 - m.x89)**2 + (m.x46 - m.x90)**2 + (m.x47 -
    m.x91)**2 + (m.x48 - m.x92)**2 - m.x97 >= 0)
m.e210 = Constraint(expr= (m.x45 - m.x93)**2 + (m.x46 - m.x94)**2 + (m.x47 -
    m.x95)**2 + (m.x48 - m.x96)**2 - m.x97 >= 0)
m.e211 = Constraint(expr= (m.x49 - m.x53)**2 + (m.x50 - m.x54)**2 + (m.x51 -
    m.x55)**2 + (m.x52 - m.x56)**2 - m.x97 >= 0)
m.e212 = Constraint(expr= (m.x49 - m.x57)**2 + (m.x50 - m.x58)**2 + (m.x51 -
    m.x59)**2 + (m.x52 - m.x60)**2 - m.x97 >= 0)
m.e213 = Constraint(expr= (m.x49 - m.x61)**2 + (m.x50 - m.x62)**2 + (m.x51 -
    m.x63)**2 + (m.x52 - m.x64)**2 - m.x97 >= 0)
m.e214 = Constraint(expr= (m.x49 - m.x65)**2 + (m.x50 - m.x66)**2 + (m.x51 -
    m.x67)**2 + (m.x52 - m.x68)**2 - m.x97 >= 0)
m.e215 = Constraint(expr= (m.x49 - m.x69)**2 + (m.x50 - m.x70)**2 + (m.x51 -
    m.x71)**2 + (m.x52 - m.x72)**2 - m.x97 >= 0)
m.e216 = Constraint(expr= (m.x49 - m.x73)**2 + (m.x50 - m.x74)**2 + (m.x51 -
    m.x75)**2 + (m.x52 - m.x76)**2 - m.x97 >= 0)
m.e217 = Constraint(expr= (m.x49 - m.x77)**2 + (m.x50 - m.x78)**2 + (m.x51 -
    m.x79)**2 + (m.x52 - m.x80)**2 - m.x97 >= 0)
m.e218 = Constraint(expr= (m.x49 - m.x81)**2 + (m.x50 - m.x82)**2 + (m.x51 -
    m.x83)**2 + (m.x52 - m.x84)**2 - m.x97 >= 0)
m.e219 = Constraint(expr= (m.x49 - m.x85)**2 + (m.x50 - m.x86)**2 + (m.x51 -
    m.x87)**2 + (m.x52 - m.x88)**2 - m.x97 >= 0)
m.e220 = Constraint(expr= (m.x49 - m.x89)**2 + (m.x50 - m.x90)**2 + (m.x51 -
    m.x91)**2 + (m.x52 - m.x92)**2 - m.x97 >= 0)
m.e221 = Constraint(expr= (m.x49 - m.x93)**2 + (m.x50 - m.x94)**2 + (m.x51 -
    m.x95)**2 + (m.x52 - m.x96)**2 - m.x97 >= 0)
m.e222 = Constraint(expr= (m.x53 - m.x57)**2 + (m.x54 - m.x58)**2 + (m.x55 -
    m.x59)**2 + (m.x56 - m.x60)**2 - m.x97 >= 0)
m.e223 = Constraint(expr= (m.x53 - m.x61)**2 + (m.x54 - m.x62)**2 + (m.x55 -
    m.x63)**2 + (m.x56 - m.x64)**2 - m.x97 >= 0)
m.e224 = Constraint(expr= (m.x53 - m.x65)**2 + (m.x54 - m.x66)**2 + (m.x55 -
    m.x67)**2 + (m.x56 - m.x68)**2 - m.x97 >= 0)
m.e225 = Constraint(expr= (m.x53 - m.x69)**2 + (m.x54 - m.x70)**2 + (m.x55 -
    m.x71)**2 + (m.x56 - m.x72)**2 - m.x97 >= 0)
m.e226 = Constraint(expr= (m.x53 - m.x73)**2 + (m.x54 - m.x74)**2 + (m.x55 -
    m.x75)**2 + (m.x56 - m.x76)**2 - m.x97 >= 0)
m.e227 = Constraint(expr= (m.x53 - m.x77)**2 + (m.x54 - m.x78)**2 + (m.x55 -
    m.x79)**2 + (m.x56 - m.x80)**2 - m.x97 >= 0)
m.e228 = Constraint(expr= (m.x53 - m.x81)**2 + (m.x54 - m.x82)**2 + (m.x55 -
    m.x83)**2 + (m.x56 - m.x84)**2 - m.x97 >= 0)
m.e229 = Constraint(expr= (m.x53 - m.x85)**2 + (m.x54 - m.x86)**2 + (m.x55 -
    m.x87)**2 + (m.x56 - m.x88)**2 - m.x97 >= 0)
m.e230 = Constraint(expr= (m.x53 - m.x89)**2 + (m.x54 - m.x90)**2 + (m.x55 -
    m.x91)**2 + (m.x56 - m.x92)**2 - m.x97 >= 0)
m.e231 = Constraint(expr= (m.x53 - m.x93)**2 + (m.x54 - m.x94)**2 + (m.x55 -
    m.x95)**2 + (m.x56 - m.x96)**2 - m.x97 >= 0)
m.e232 = Constraint(expr= (m.x57 - m.x61)**2 + (m.x58 - m.x62)**2 + (m.x59 -
    m.x63)**2 + (m.x60 - m.x64)**2 - m.x97 >= 0)
m.e233 = Constraint(expr= (m.x57 - m.x65)**2 + (m.x58 - m.x66)**2 + (m.x59 -
    m.x67)**2 + (m.x60 - m.x68)**2 - m.x97 >= 0)
m.e234 = Constraint(expr= (m.x57 - m.x69)**2 + (m.x58 - m.x70)**2 + (m.x59 -
    m.x71)**2 + (m.x60 - m.x72)**2 - m.x97 >= 0)
m.e235 = Constraint(expr= (m.x57 - m.x73)**2 + (m.x58 - m.x74)**2 + (m.x59 -
    m.x75)**2 + (m.x60 - m.x76)**2 - m.x97 >= 0)
m.e236 = Constraint(expr= (m.x57 - m.x77)**2 + (m.x58 - m.x78)**2 + (m.x59 -
    m.x79)**2 + (m.x60 - m.x80)**2 - m.x97 >= 0)
m.e237 = Constraint(expr= (m.x57 - m.x81)**2 + (m.x58 - m.x82)**2 + (m.x59 -
    m.x83)**2 + (m.x60 - m.x84)**2 - m.x97 >= 0)
m.e238 = Constraint(expr= (m.x57 - m.x85)**2 + (m.x58 - m.x86)**2 + (m.x59 -
    m.x87)**2 + (m.x60 - m.x88)**2 - m.x97 >= 0)
m.e239 = Constraint(expr= (m.x57 - m.x89)**2 + (m.x58 - m.x90)**2 + (m.x59 -
    m.x91)**2 + (m.x60 - m.x92)**2 - m.x97 >= 0)
m.e240 = Constraint(expr= (m.x57 - m.x93)**2 + (m.x58 - m.x94)**2 + (m.x59 -
    m.x95)**2 + (m.x60 - m.x96)**2 - m.x97 >= 0)
m.e241 = Constraint(expr= (m.x61 - m.x65)**2 + (m.x62 - m.x66)**2 + (m.x63 -
    m.x67)**2 + (m.x64 - m.x68)**2 - m.x97 >= 0)
m.e242 = Constraint(expr= (m.x61 - m.x69)**2 + (m.x62 - m.x70)**2 + (m.x63 -
    m.x71)**2 + (m.x64 - m.x72)**2 - m.x97 >= 0)
m.e243 = Constraint(expr= (m.x61 - m.x73)**2 + (m.x62 - m.x74)**2 + (m.x63 -
    m.x75)**2 + (m.x64 - m.x76)**2 - m.x97 >= 0)
m.e244 = Constraint(expr= (m.x61 - m.x77)**2 + (m.x62 - m.x78)**2 + (m.x63 -
    m.x79)**2 + (m.x64 - m.x80)**2 - m.x97 >= 0)
m.e245 = Constraint(expr= (m.x61 - m.x81)**2 + (m.x62 - m.x82)**2 + (m.x63 -
    m.x83)**2 + (m.x64 - m.x84)**2 - m.x97 >= 0)
m.e246 = Constraint(expr= (m.x61 - m.x85)**2 + (m.x62 - m.x86)**2 + (m.x63 -
    m.x87)**2 + (m.x64 - m.x88)**2 - m.x97 >= 0)
m.e247 = Constraint(expr= (m.x61 - m.x89)**2 + (m.x62 - m.x90)**2 + (m.x63 -
    m.x91)**2 + (m.x64 - m.x92)**2 - m.x97 >= 0)
m.e248 = Constraint(expr= (m.x61 - m.x93)**2 + (m.x62 - m.x94)**2 + (m.x63 -
    m.x95)**2 + (m.x64 - m.x96)**2 - m.x97 >= 0)
m.e249 = Constraint(expr= (m.x65 - m.x69)**2 + (m.x66 - m.x70)**2 + (m.x67 -
    m.x71)**2 + (m.x68 - m.x72)**2 - m.x97 >= 0)
m.e250 = Constraint(expr= (m.x65 - m.x73)**2 + (m.x66 - m.x74)**2 + (m.x67 -
    m.x75)**2 + (m.x68 - m.x76)**2 - m.x97 >= 0)
m.e251 = Constraint(expr= (m.x65 - m.x77)**2 + (m.x66 - m.x78)**2 + (m.x67 -
    m.x79)**2 + (m.x68 - m.x80)**2 - m.x97 >= 0)
m.e252 = Constraint(expr= (m.x65 - m.x81)**2 + (m.x66 - m.x82)**2 + (m.x67 -
    m.x83)**2 + (m.x68 - m.x84)**2 - m.x97 >= 0)
m.e253 = Constraint(expr= (m.x65 - m.x85)**2 + (m.x66 - m.x86)**2 + (m.x67 -
    m.x87)**2 + (m.x68 - m.x88)**2 - m.x97 >= 0)
m.e254 = Constraint(expr= (m.x65 - m.x89)**2 + (m.x66 - m.x90)**2 + (m.x67 -
    m.x91)**2 + (m.x68 - m.x92)**2 - m.x97 >= 0)
m.e255 = Constraint(expr= (m.x65 - m.x93)**2 + (m.x66 - m.x94)**2 + (m.x67 -
    m.x95)**2 + (m.x68 - m.x96)**2 - m.x97 >= 0)
m.e256 = Constraint(expr= (m.x69 - m.x73)**2 + (m.x70 - m.x74)**2 + (m.x71 -
    m.x75)**2 + (m.x72 - m.x76)**2 - m.x97 >= 0)
m.e257 = Constraint(expr= (m.x69 - m.x77)**2 + (m.x70 - m.x78)**2 + (m.x71 -
    m.x79)**2 + (m.x72 - m.x80)**2 - m.x97 >= 0)
m.e258 = Constraint(expr= (m.x69 - m.x81)**2 + (m.x70 - m.x82)**2 + (m.x71 -
    m.x83)**2 + (m.x72 - m.x84)**2 - m.x97 >= 0)
m.e259 = Constraint(expr= (m.x69 - m.x85)**2 + (m.x70 - m.x86)**2 + (m.x71 -
    m.x87)**2 + (m.x72 - m.x88)**2 - m.x97 >= 0)
m.e260 = Constraint(expr= (m.x69 - m.x89)**2 + (m.x70 - m.x90)**2 + (m.x71 -
    m.x91)**2 + (m.x72 - m.x92)**2 - m.x97 >= 0)
m.e261 = Constraint(expr= (m.x69 - m.x93)**2 + (m.x70 - m.x94)**2 + (m.x71 -
    m.x95)**2 + (m.x72 - m.x96)**2 - m.x97 >= 0)
m.e262 = Constraint(expr= (m.x73 - m.x77)**2 + (m.x74 - m.x78)**2 + (m.x75 -
    m.x79)**2 + (m.x76 - m.x80)**2 - m.x97 >= 0)
m.e263 = Constraint(expr= (m.x73 - m.x81)**2 + (m.x74 - m.x82)**2 + (m.x75 -
    m.x83)**2 + (m.x76 - m.x84)**2 - m.x97 >= 0)
m.e264 = Constraint(expr= (m.x73 - m.x85)**2 + (m.x74 - m.x86)**2 + (m.x75 -
    m.x87)**2 + (m.x76 - m.x88)**2 - m.x97 >= 0)
m.e265 = Constraint(expr= (m.x73 - m.x89)**2 + (m.x74 - m.x90)**2 + (m.x75 -
    m.x91)**2 + (m.x76 - m.x92)**2 - m.x97 >= 0)
m.e266 = Constraint(expr= (m.x73 - m.x93)**2 + (m.x74 - m.x94)**2 + (m.x75 -
    m.x95)**2 + (m.x76 - m.x96)**2 - m.x97 >= 0)
m.e267 = Constraint(expr= (m.x77 - m.x81)**2 + (m.x78 - m.x82)**2 + (m.x79 -
    m.x83)**2 + (m.x80 - m.x84)**2 - m.x97 >= 0)
m.e268 = Constraint(expr= (m.x77 - m.x85)**2 + (m.x78 - m.x86)**2 + (m.x79 -
    m.x87)**2 + (m.x80 - m.x88)**2 - m.x97 >= 0)
m.e269 = Constraint(expr= (m.x77 - m.x89)**2 + (m.x78 - m.x90)**2 + (m.x79 -
    m.x91)**2 + (m.x80 - m.x92)**2 - m.x97 >= 0)
m.e270 = Constraint(expr= (m.x77 - m.x93)**2 + (m.x78 - m.x94)**2 + (m.x79 -
    m.x95)**2 + (m.x80 - m.x96)**2 - m.x97 >= 0)
m.e271 = Constraint(expr= (m.x81 - m.x85)**2 + (m.x82 - m.x86)**2 + (m.x83 -
    m.x87)**2 + (m.x84 - m.x88)**2 - m.x97 >= 0)
m.e272 = Constraint(expr= (m.x81 - m.x89)**2 + (m.x82 - m.x90)**2 + (m.x83 -
    m.x91)**2 + (m.x84 - m.x92)**2 - m.x97 >= 0)
m.e273 = Constraint(expr= (m.x81 - m.x93)**2 + (m.x82 - m.x94)**2 + (m.x83 -
    m.x95)**2 + (m.x84 - m.x96)**2 - m.x97 >= 0)
m.e274 = Constraint(expr= (m.x85 - m.x89)**2 + (m.x86 - m.x90)**2 + (m.x87 -
    m.x91)**2 + (m.x88 - m.x92)**2 - m.x97 >= 0)
m.e275 = Constraint(expr= (m.x85 - m.x93)**2 + (m.x86 - m.x94)**2 + (m.x87 -
    m.x95)**2 + (m.x88 - m.x96)**2 - m.x97 >= 0)
m.e276 = Constraint(expr= (m.x89 - m.x93)**2 + (m.x90 - m.x94)**2 + (m.x91 -
    m.x95)**2 + (m.x92 - m.x96)**2 - m.x97 >= 0)
m.e277 = Constraint(expr= m.x1 - m.x5 <= 0)
m.e278 = Constraint(expr= m.x5 - m.x9 <= 0)
m.e279 = Constraint(expr= m.x9 - m.x13 <= 0)
m.e280 = Constraint(expr= m.x13 - m.x17 <= 0)
m.e281 = Constraint(expr= m.x17 - m.x21 <= 0)
m.e282 = Constraint(expr= m.x21 - m.x25 <= 0)
m.e283 = Constraint(expr= m.x25 - m.x29 <= 0)
m.e284 = Constraint(expr= m.x29 - m.x33 <= 0)
m.e285 = Constraint(expr= m.x33 - m.x37 <= 0)
m.e286 = Constraint(expr= m.x37 - m.x41 <= 0)
m.e287 = Constraint(expr= m.x41 - m.x45 <= 0)
m.e288 = Constraint(expr= m.x45 - m.x49 <= 0)
m.e289 = Constraint(expr= m.x49 - m.x53 <= 0)
m.e290 = Constraint(expr= m.x53 - m.x57 <= 0)
m.e291 = Constraint(expr= m.x57 - m.x61 <= 0)
m.e292 = Constraint(expr= m.x61 - m.x65 <= 0)
m.e293 = Constraint(expr= m.x65 - m.x69 <= 0)
m.e294 = Constraint(expr= m.x69 - m.x73 <= 0)
m.e295 = Constraint(expr= m.x73 - m.x77 <= 0)
m.e296 = Constraint(expr= m.x77 - m.x81 <= 0)
m.e297 = Constraint(expr= m.x81 - m.x85 <= 0)
m.e298 = Constraint(expr= m.x85 - m.x89 <= 0)
m.e299 = Constraint(expr= m.x89 - m.x93 <= 0)
m.e300 = Constraint(expr= m.x1**2 + m.x2**2 + m.x3**2 + m.x4**2 == 4)
m.e301 = Constraint(expr= m.x5**2 + m.x6**2 + m.x7**2 + m.x8**2 == 4)
m.e302 = Constraint(expr= m.x9**2 + m.x10**2 + m.x11**2 + m.x12**2 == 4)
m.e303 = Constraint(expr= m.x13**2 + m.x14**2 + m.x15**2 + m.x16**2 == 4)
m.e304 = Constraint(expr= m.x17**2 + m.x18**2 + m.x19**2 + m.x20**2 == 4)
m.e305 = Constraint(expr= m.x21**2 + m.x22**2 + m.x23**2 + m.x24**2 == 4)
m.e306 = Constraint(expr= m.x25**2 + m.x26**2 + m.x27**2 + m.x28**2 == 4)
m.e307 = Constraint(expr= m.x29**2 + m.x30**2 + m.x31**2 + m.x32**2 == 4)
m.e308 = Constraint(expr= m.x33**2 + m.x34**2 + m.x35**2 + m.x36**2 == 4)
m.e309 = Constraint(expr= m.x37**2 + m.x38**2 + m.x39**2 + m.x40**2 == 4)
m.e310 = Constraint(expr= m.x41**2 + m.x42**2 + m.x43**2 + m.x44**2 == 4)
m.e311 = Constraint(expr= m.x45**2 + m.x46**2 + m.x47**2 + m.x48**2 == 4)
m.e312 = Constraint(expr= m.x49**2 + m.x50**2 + m.x51**2 + m.x52**2 == 4)
m.e313 = Constraint(expr= m.x53**2 + m.x54**2 + m.x55**2 + m.x56**2 == 4)
m.e314 = Constraint(expr= m.x57**2 + m.x58**2 + m.x59**2 + m.x60**2 == 4)
m.e315 = Constraint(expr= m.x61**2 + m.x62**2 + m.x63**2 + m.x64**2 == 4)
m.e316 = Constraint(expr= m.x65**2 + m.x66**2 + m.x67**2 + m.x68**2 == 4)
m.e317 = Constraint(expr= m.x69**2 + m.x70**2 + m.x71**2 + m.x72**2 == 4)
m.e318 = Constraint(expr= m.x73**2 + m.x74**2 + m.x75**2 + m.x76**2 == 4)
m.e319 = Constraint(expr= m.x77**2 + m.x78**2 + m.x79**2 + m.x80**2 == 4)
m.e320 = Constraint(expr= m.x81**2 + m.x82**2 + m.x83**2 + m.x84**2 == 4)
m.e321 = Constraint(expr= m.x85**2 + m.x86**2 + m.x87**2 + m.x88**2 == 4)
m.e322 = Constraint(expr= m.x89**2 + m.x90**2 + m.x91**2 + m.x92**2 == 4)
m.e323 = Constraint(expr= m.x93**2 + m.x94**2 + m.x95**2 + m.x96**2 == 4)
