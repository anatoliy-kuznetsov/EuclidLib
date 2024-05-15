# NLP written by GAMS Convert at 05/15/24 11:48:55
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       464       29      406       29        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        88       88        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#      2581       58     2523
#
# Reformulation has removed 1 variable and 1 equation

from pyomo.environ import *

model = m = ConcreteModel()

m.x1 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x2 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x3 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x4 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x5 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x6 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x7 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x8 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x9 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x10 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x11 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x12 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x13 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x14 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x15 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x16 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x17 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x18 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x19 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x20 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x21 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x22 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x23 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x24 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x25 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x26 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x27 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x28 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x29 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x30 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x31 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x32 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x33 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x34 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x35 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x36 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x37 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x38 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x39 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x40 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x41 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x42 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x43 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x44 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x45 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x46 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x47 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x48 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x49 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x50 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x51 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x52 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x53 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x54 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x55 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x56 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x57 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x58 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x59 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x60 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x61 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x62 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x63 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x64 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x65 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x66 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x67 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x68 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x69 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x70 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x71 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x72 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x73 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x74 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x75 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x76 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x77 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x78 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x79 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x80 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x81 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x82 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x83 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x84 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x85 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x86 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x87 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x88 = Var(within=Reals, bounds=(None,None), initialize=0)

m.obj = Objective(sense=maximize, expr= m.x88)

m.e1 = Constraint(expr= (m.x1 - m.x2)**2 + (m.x30 - m.x31)**2 - (m.x59 + m.x60)
    **2 >= 0)
m.e2 = Constraint(expr= (m.x1 - m.x3)**2 + (m.x30 - m.x32)**2 - (m.x59 + m.x61)
    **2 >= 0)
m.e3 = Constraint(expr= (m.x1 - m.x4)**2 + (m.x30 - m.x33)**2 - (m.x59 + m.x62)
    **2 >= 0)
m.e4 = Constraint(expr= (m.x1 - m.x5)**2 + (m.x30 - m.x34)**2 - (m.x59 + m.x63)
    **2 >= 0)
m.e5 = Constraint(expr= (m.x1 - m.x6)**2 + (m.x30 - m.x35)**2 - (m.x59 + m.x64)
    **2 >= 0)
m.e6 = Constraint(expr= (m.x1 - m.x7)**2 + (m.x30 - m.x36)**2 - (m.x59 + m.x65)
    **2 >= 0)
m.e7 = Constraint(expr= (m.x1 - m.x8)**2 + (m.x30 - m.x37)**2 - (m.x59 + m.x66)
    **2 >= 0)
m.e8 = Constraint(expr= (m.x1 - m.x9)**2 + (m.x30 - m.x38)**2 - (m.x59 + m.x67)
    **2 >= 0)
m.e9 = Constraint(expr= (m.x1 - m.x10)**2 + (m.x30 - m.x39)**2 - (m.x59 + m.x68)
    **2 >= 0)
m.e10 = Constraint(expr= (m.x1 - m.x11)**2 + (m.x30 - m.x40)**2 - (m.x59 +
    m.x69)**2 >= 0)
m.e11 = Constraint(expr= (m.x1 - m.x12)**2 + (m.x30 - m.x41)**2 - (m.x59 +
    m.x70)**2 >= 0)
m.e12 = Constraint(expr= (m.x1 - m.x13)**2 + (m.x30 - m.x42)**2 - (m.x59 +
    m.x71)**2 >= 0)
m.e13 = Constraint(expr= (m.x1 - m.x14)**2 + (m.x30 - m.x43)**2 - (m.x59 +
    m.x72)**2 >= 0)
m.e14 = Constraint(expr= (m.x1 - m.x15)**2 + (m.x30 - m.x44)**2 - (m.x59 +
    m.x73)**2 >= 0)
m.e15 = Constraint(expr= (m.x1 - m.x16)**2 + (m.x30 - m.x45)**2 - (m.x59 +
    m.x74)**2 >= 0)
m.e16 = Constraint(expr= (m.x1 - m.x17)**2 + (m.x30 - m.x46)**2 - (m.x59 +
    m.x75)**2 >= 0)
m.e17 = Constraint(expr= (m.x1 - m.x18)**2 + (m.x30 - m.x47)**2 - (m.x59 +
    m.x76)**2 >= 0)
m.e18 = Constraint(expr= (m.x1 - m.x19)**2 + (m.x30 - m.x48)**2 - (m.x59 +
    m.x77)**2 >= 0)
m.e19 = Constraint(expr= (m.x1 - m.x20)**2 + (m.x30 - m.x49)**2 - (m.x59 +
    m.x78)**2 >= 0)
m.e20 = Constraint(expr= (m.x1 - m.x21)**2 + (m.x30 - m.x50)**2 - (m.x59 +
    m.x79)**2 >= 0)
m.e21 = Constraint(expr= (m.x1 - m.x22)**2 + (m.x30 - m.x51)**2 - (m.x59 +
    m.x80)**2 >= 0)
m.e22 = Constraint(expr= (m.x1 - m.x23)**2 + (m.x30 - m.x52)**2 - (m.x59 +
    m.x81)**2 >= 0)
m.e23 = Constraint(expr= (m.x1 - m.x24)**2 + (m.x30 - m.x53)**2 - (m.x59 +
    m.x82)**2 >= 0)
m.e24 = Constraint(expr= (m.x1 - m.x25)**2 + (m.x30 - m.x54)**2 - (m.x59 +
    m.x83)**2 >= 0)
m.e25 = Constraint(expr= (m.x1 - m.x26)**2 + (m.x30 - m.x55)**2 - (m.x59 +
    m.x84)**2 >= 0)
m.e26 = Constraint(expr= (m.x1 - m.x27)**2 + (m.x30 - m.x56)**2 - (m.x59 +
    m.x85)**2 >= 0)
m.e27 = Constraint(expr= (m.x1 - m.x28)**2 + (m.x30 - m.x57)**2 - (m.x59 +
    m.x86)**2 >= 0)
m.e28 = Constraint(expr= (m.x1 - m.x29)**2 + (m.x30 - m.x58)**2 - (m.x59 +
    m.x87)**2 >= 0)
m.e29 = Constraint(expr= (m.x2 - m.x3)**2 + (m.x31 - m.x32)**2 - (m.x60 + m.x61)
    **2 >= 0)
m.e30 = Constraint(expr= (m.x2 - m.x4)**2 + (m.x31 - m.x33)**2 - (m.x60 + m.x62)
    **2 >= 0)
m.e31 = Constraint(expr= (m.x2 - m.x5)**2 + (m.x31 - m.x34)**2 - (m.x60 + m.x63)
    **2 >= 0)
m.e32 = Constraint(expr= (m.x2 - m.x6)**2 + (m.x31 - m.x35)**2 - (m.x60 + m.x64)
    **2 >= 0)
m.e33 = Constraint(expr= (m.x2 - m.x7)**2 + (m.x31 - m.x36)**2 - (m.x60 + m.x65)
    **2 >= 0)
m.e34 = Constraint(expr= (m.x2 - m.x8)**2 + (m.x31 - m.x37)**2 - (m.x60 + m.x66)
    **2 >= 0)
m.e35 = Constraint(expr= (m.x2 - m.x9)**2 + (m.x31 - m.x38)**2 - (m.x60 + m.x67)
    **2 >= 0)
m.e36 = Constraint(expr= (m.x2 - m.x10)**2 + (m.x31 - m.x39)**2 - (m.x60 +
    m.x68)**2 >= 0)
m.e37 = Constraint(expr= (m.x2 - m.x11)**2 + (m.x31 - m.x40)**2 - (m.x60 +
    m.x69)**2 >= 0)
m.e38 = Constraint(expr= (m.x2 - m.x12)**2 + (m.x31 - m.x41)**2 - (m.x60 +
    m.x70)**2 >= 0)
m.e39 = Constraint(expr= (m.x2 - m.x13)**2 + (m.x31 - m.x42)**2 - (m.x60 +
    m.x71)**2 >= 0)
m.e40 = Constraint(expr= (m.x2 - m.x14)**2 + (m.x31 - m.x43)**2 - (m.x60 +
    m.x72)**2 >= 0)
m.e41 = Constraint(expr= (m.x2 - m.x15)**2 + (m.x31 - m.x44)**2 - (m.x60 +
    m.x73)**2 >= 0)
m.e42 = Constraint(expr= (m.x2 - m.x16)**2 + (m.x31 - m.x45)**2 - (m.x60 +
    m.x74)**2 >= 0)
m.e43 = Constraint(expr= (m.x2 - m.x17)**2 + (m.x31 - m.x46)**2 - (m.x60 +
    m.x75)**2 >= 0)
m.e44 = Constraint(expr= (m.x2 - m.x18)**2 + (m.x31 - m.x47)**2 - (m.x60 +
    m.x76)**2 >= 0)
m.e45 = Constraint(expr= (m.x2 - m.x19)**2 + (m.x31 - m.x48)**2 - (m.x60 +
    m.x77)**2 >= 0)
m.e46 = Constraint(expr= (m.x2 - m.x20)**2 + (m.x31 - m.x49)**2 - (m.x60 +
    m.x78)**2 >= 0)
m.e47 = Constraint(expr= (m.x2 - m.x21)**2 + (m.x31 - m.x50)**2 - (m.x60 +
    m.x79)**2 >= 0)
m.e48 = Constraint(expr= (m.x2 - m.x22)**2 + (m.x31 - m.x51)**2 - (m.x60 +
    m.x80)**2 >= 0)
m.e49 = Constraint(expr= (m.x2 - m.x23)**2 + (m.x31 - m.x52)**2 - (m.x60 +
    m.x81)**2 >= 0)
m.e50 = Constraint(expr= (m.x2 - m.x24)**2 + (m.x31 - m.x53)**2 - (m.x60 +
    m.x82)**2 >= 0)
m.e51 = Constraint(expr= (m.x2 - m.x25)**2 + (m.x31 - m.x54)**2 - (m.x60 +
    m.x83)**2 >= 0)
m.e52 = Constraint(expr= (m.x2 - m.x26)**2 + (m.x31 - m.x55)**2 - (m.x60 +
    m.x84)**2 >= 0)
m.e53 = Constraint(expr= (m.x2 - m.x27)**2 + (m.x31 - m.x56)**2 - (m.x60 +
    m.x85)**2 >= 0)
m.e54 = Constraint(expr= (m.x2 - m.x28)**2 + (m.x31 - m.x57)**2 - (m.x60 +
    m.x86)**2 >= 0)
m.e55 = Constraint(expr= (m.x2 - m.x29)**2 + (m.x31 - m.x58)**2 - (m.x60 +
    m.x87)**2 >= 0)
m.e56 = Constraint(expr= (m.x3 - m.x4)**2 + (m.x32 - m.x33)**2 - (m.x61 + m.x62)
    **2 >= 0)
m.e57 = Constraint(expr= (m.x3 - m.x5)**2 + (m.x32 - m.x34)**2 - (m.x61 + m.x63)
    **2 >= 0)
m.e58 = Constraint(expr= (m.x3 - m.x6)**2 + (m.x32 - m.x35)**2 - (m.x61 + m.x64)
    **2 >= 0)
m.e59 = Constraint(expr= (m.x3 - m.x7)**2 + (m.x32 - m.x36)**2 - (m.x61 + m.x65)
    **2 >= 0)
m.e60 = Constraint(expr= (m.x3 - m.x8)**2 + (m.x32 - m.x37)**2 - (m.x61 + m.x66)
    **2 >= 0)
m.e61 = Constraint(expr= (m.x3 - m.x9)**2 + (m.x32 - m.x38)**2 - (m.x61 + m.x67)
    **2 >= 0)
m.e62 = Constraint(expr= (m.x3 - m.x10)**2 + (m.x32 - m.x39)**2 - (m.x61 +
    m.x68)**2 >= 0)
m.e63 = Constraint(expr= (m.x3 - m.x11)**2 + (m.x32 - m.x40)**2 - (m.x61 +
    m.x69)**2 >= 0)
m.e64 = Constraint(expr= (m.x3 - m.x12)**2 + (m.x32 - m.x41)**2 - (m.x61 +
    m.x70)**2 >= 0)
m.e65 = Constraint(expr= (m.x3 - m.x13)**2 + (m.x32 - m.x42)**2 - (m.x61 +
    m.x71)**2 >= 0)
m.e66 = Constraint(expr= (m.x3 - m.x14)**2 + (m.x32 - m.x43)**2 - (m.x61 +
    m.x72)**2 >= 0)
m.e67 = Constraint(expr= (m.x3 - m.x15)**2 + (m.x32 - m.x44)**2 - (m.x61 +
    m.x73)**2 >= 0)
m.e68 = Constraint(expr= (m.x3 - m.x16)**2 + (m.x32 - m.x45)**2 - (m.x61 +
    m.x74)**2 >= 0)
m.e69 = Constraint(expr= (m.x3 - m.x17)**2 + (m.x32 - m.x46)**2 - (m.x61 +
    m.x75)**2 >= 0)
m.e70 = Constraint(expr= (m.x3 - m.x18)**2 + (m.x32 - m.x47)**2 - (m.x61 +
    m.x76)**2 >= 0)
m.e71 = Constraint(expr= (m.x3 - m.x19)**2 + (m.x32 - m.x48)**2 - (m.x61 +
    m.x77)**2 >= 0)
m.e72 = Constraint(expr= (m.x3 - m.x20)**2 + (m.x32 - m.x49)**2 - (m.x61 +
    m.x78)**2 >= 0)
m.e73 = Constraint(expr= (m.x3 - m.x21)**2 + (m.x32 - m.x50)**2 - (m.x61 +
    m.x79)**2 >= 0)
m.e74 = Constraint(expr= (m.x3 - m.x22)**2 + (m.x32 - m.x51)**2 - (m.x61 +
    m.x80)**2 >= 0)
m.e75 = Constraint(expr= (m.x3 - m.x23)**2 + (m.x32 - m.x52)**2 - (m.x61 +
    m.x81)**2 >= 0)
m.e76 = Constraint(expr= (m.x3 - m.x24)**2 + (m.x32 - m.x53)**2 - (m.x61 +
    m.x82)**2 >= 0)
m.e77 = Constraint(expr= (m.x3 - m.x25)**2 + (m.x32 - m.x54)**2 - (m.x61 +
    m.x83)**2 >= 0)
m.e78 = Constraint(expr= (m.x3 - m.x26)**2 + (m.x32 - m.x55)**2 - (m.x61 +
    m.x84)**2 >= 0)
m.e79 = Constraint(expr= (m.x3 - m.x27)**2 + (m.x32 - m.x56)**2 - (m.x61 +
    m.x85)**2 >= 0)
m.e80 = Constraint(expr= (m.x3 - m.x28)**2 + (m.x32 - m.x57)**2 - (m.x61 +
    m.x86)**2 >= 0)
m.e81 = Constraint(expr= (m.x3 - m.x29)**2 + (m.x32 - m.x58)**2 - (m.x61 +
    m.x87)**2 >= 0)
m.e82 = Constraint(expr= (m.x4 - m.x5)**2 + (m.x33 - m.x34)**2 - (m.x62 + m.x63)
    **2 >= 0)
m.e83 = Constraint(expr= (m.x4 - m.x6)**2 + (m.x33 - m.x35)**2 - (m.x62 + m.x64)
    **2 >= 0)
m.e84 = Constraint(expr= (m.x4 - m.x7)**2 + (m.x33 - m.x36)**2 - (m.x62 + m.x65)
    **2 >= 0)
m.e85 = Constraint(expr= (m.x4 - m.x8)**2 + (m.x33 - m.x37)**2 - (m.x62 + m.x66)
    **2 >= 0)
m.e86 = Constraint(expr= (m.x4 - m.x9)**2 + (m.x33 - m.x38)**2 - (m.x62 + m.x67)
    **2 >= 0)
m.e87 = Constraint(expr= (m.x4 - m.x10)**2 + (m.x33 - m.x39)**2 - (m.x62 +
    m.x68)**2 >= 0)
m.e88 = Constraint(expr= (m.x4 - m.x11)**2 + (m.x33 - m.x40)**2 - (m.x62 +
    m.x69)**2 >= 0)
m.e89 = Constraint(expr= (m.x4 - m.x12)**2 + (m.x33 - m.x41)**2 - (m.x62 +
    m.x70)**2 >= 0)
m.e90 = Constraint(expr= (m.x4 - m.x13)**2 + (m.x33 - m.x42)**2 - (m.x62 +
    m.x71)**2 >= 0)
m.e91 = Constraint(expr= (m.x4 - m.x14)**2 + (m.x33 - m.x43)**2 - (m.x62 +
    m.x72)**2 >= 0)
m.e92 = Constraint(expr= (m.x4 - m.x15)**2 + (m.x33 - m.x44)**2 - (m.x62 +
    m.x73)**2 >= 0)
m.e93 = Constraint(expr= (m.x4 - m.x16)**2 + (m.x33 - m.x45)**2 - (m.x62 +
    m.x74)**2 >= 0)
m.e94 = Constraint(expr= (m.x4 - m.x17)**2 + (m.x33 - m.x46)**2 - (m.x62 +
    m.x75)**2 >= 0)
m.e95 = Constraint(expr= (m.x4 - m.x18)**2 + (m.x33 - m.x47)**2 - (m.x62 +
    m.x76)**2 >= 0)
m.e96 = Constraint(expr= (m.x4 - m.x19)**2 + (m.x33 - m.x48)**2 - (m.x62 +
    m.x77)**2 >= 0)
m.e97 = Constraint(expr= (m.x4 - m.x20)**2 + (m.x33 - m.x49)**2 - (m.x62 +
    m.x78)**2 >= 0)
m.e98 = Constraint(expr= (m.x4 - m.x21)**2 + (m.x33 - m.x50)**2 - (m.x62 +
    m.x79)**2 >= 0)
m.e99 = Constraint(expr= (m.x4 - m.x22)**2 + (m.x33 - m.x51)**2 - (m.x62 +
    m.x80)**2 >= 0)
m.e100 = Constraint(expr= (m.x4 - m.x23)**2 + (m.x33 - m.x52)**2 - (m.x62 +
    m.x81)**2 >= 0)
m.e101 = Constraint(expr= (m.x4 - m.x24)**2 + (m.x33 - m.x53)**2 - (m.x62 +
    m.x82)**2 >= 0)
m.e102 = Constraint(expr= (m.x4 - m.x25)**2 + (m.x33 - m.x54)**2 - (m.x62 +
    m.x83)**2 >= 0)
m.e103 = Constraint(expr= (m.x4 - m.x26)**2 + (m.x33 - m.x55)**2 - (m.x62 +
    m.x84)**2 >= 0)
m.e104 = Constraint(expr= (m.x4 - m.x27)**2 + (m.x33 - m.x56)**2 - (m.x62 +
    m.x85)**2 >= 0)
m.e105 = Constraint(expr= (m.x4 - m.x28)**2 + (m.x33 - m.x57)**2 - (m.x62 +
    m.x86)**2 >= 0)
m.e106 = Constraint(expr= (m.x4 - m.x29)**2 + (m.x33 - m.x58)**2 - (m.x62 +
    m.x87)**2 >= 0)
m.e107 = Constraint(expr= (m.x5 - m.x6)**2 + (m.x34 - m.x35)**2 - (m.x63 +
    m.x64)**2 >= 0)
m.e108 = Constraint(expr= (m.x5 - m.x7)**2 + (m.x34 - m.x36)**2 - (m.x63 +
    m.x65)**2 >= 0)
m.e109 = Constraint(expr= (m.x5 - m.x8)**2 + (m.x34 - m.x37)**2 - (m.x63 +
    m.x66)**2 >= 0)
m.e110 = Constraint(expr= (m.x5 - m.x9)**2 + (m.x34 - m.x38)**2 - (m.x63 +
    m.x67)**2 >= 0)
m.e111 = Constraint(expr= (m.x5 - m.x10)**2 + (m.x34 - m.x39)**2 - (m.x63 +
    m.x68)**2 >= 0)
m.e112 = Constraint(expr= (m.x5 - m.x11)**2 + (m.x34 - m.x40)**2 - (m.x63 +
    m.x69)**2 >= 0)
m.e113 = Constraint(expr= (m.x5 - m.x12)**2 + (m.x34 - m.x41)**2 - (m.x63 +
    m.x70)**2 >= 0)
m.e114 = Constraint(expr= (m.x5 - m.x13)**2 + (m.x34 - m.x42)**2 - (m.x63 +
    m.x71)**2 >= 0)
m.e115 = Constraint(expr= (m.x5 - m.x14)**2 + (m.x34 - m.x43)**2 - (m.x63 +
    m.x72)**2 >= 0)
m.e116 = Constraint(expr= (m.x5 - m.x15)**2 + (m.x34 - m.x44)**2 - (m.x63 +
    m.x73)**2 >= 0)
m.e117 = Constraint(expr= (m.x5 - m.x16)**2 + (m.x34 - m.x45)**2 - (m.x63 +
    m.x74)**2 >= 0)
m.e118 = Constraint(expr= (m.x5 - m.x17)**2 + (m.x34 - m.x46)**2 - (m.x63 +
    m.x75)**2 >= 0)
m.e119 = Constraint(expr= (m.x5 - m.x18)**2 + (m.x34 - m.x47)**2 - (m.x63 +
    m.x76)**2 >= 0)
m.e120 = Constraint(expr= (m.x5 - m.x19)**2 + (m.x34 - m.x48)**2 - (m.x63 +
    m.x77)**2 >= 0)
m.e121 = Constraint(expr= (m.x5 - m.x20)**2 + (m.x34 - m.x49)**2 - (m.x63 +
    m.x78)**2 >= 0)
m.e122 = Constraint(expr= (m.x5 - m.x21)**2 + (m.x34 - m.x50)**2 - (m.x63 +
    m.x79)**2 >= 0)
m.e123 = Constraint(expr= (m.x5 - m.x22)**2 + (m.x34 - m.x51)**2 - (m.x63 +
    m.x80)**2 >= 0)
m.e124 = Constraint(expr= (m.x5 - m.x23)**2 + (m.x34 - m.x52)**2 - (m.x63 +
    m.x81)**2 >= 0)
m.e125 = Constraint(expr= (m.x5 - m.x24)**2 + (m.x34 - m.x53)**2 - (m.x63 +
    m.x82)**2 >= 0)
m.e126 = Constraint(expr= (m.x5 - m.x25)**2 + (m.x34 - m.x54)**2 - (m.x63 +
    m.x83)**2 >= 0)
m.e127 = Constraint(expr= (m.x5 - m.x26)**2 + (m.x34 - m.x55)**2 - (m.x63 +
    m.x84)**2 >= 0)
m.e128 = Constraint(expr= (m.x5 - m.x27)**2 + (m.x34 - m.x56)**2 - (m.x63 +
    m.x85)**2 >= 0)
m.e129 = Constraint(expr= (m.x5 - m.x28)**2 + (m.x34 - m.x57)**2 - (m.x63 +
    m.x86)**2 >= 0)
m.e130 = Constraint(expr= (m.x5 - m.x29)**2 + (m.x34 - m.x58)**2 - (m.x63 +
    m.x87)**2 >= 0)
m.e131 = Constraint(expr= (m.x6 - m.x7)**2 + (m.x35 - m.x36)**2 - (m.x64 +
    m.x65)**2 >= 0)
m.e132 = Constraint(expr= (m.x6 - m.x8)**2 + (m.x35 - m.x37)**2 - (m.x64 +
    m.x66)**2 >= 0)
m.e133 = Constraint(expr= (m.x6 - m.x9)**2 + (m.x35 - m.x38)**2 - (m.x64 +
    m.x67)**2 >= 0)
m.e134 = Constraint(expr= (m.x6 - m.x10)**2 + (m.x35 - m.x39)**2 - (m.x64 +
    m.x68)**2 >= 0)
m.e135 = Constraint(expr= (m.x6 - m.x11)**2 + (m.x35 - m.x40)**2 - (m.x64 +
    m.x69)**2 >= 0)
m.e136 = Constraint(expr= (m.x6 - m.x12)**2 + (m.x35 - m.x41)**2 - (m.x64 +
    m.x70)**2 >= 0)
m.e137 = Constraint(expr= (m.x6 - m.x13)**2 + (m.x35 - m.x42)**2 - (m.x64 +
    m.x71)**2 >= 0)
m.e138 = Constraint(expr= (m.x6 - m.x14)**2 + (m.x35 - m.x43)**2 - (m.x64 +
    m.x72)**2 >= 0)
m.e139 = Constraint(expr= (m.x6 - m.x15)**2 + (m.x35 - m.x44)**2 - (m.x64 +
    m.x73)**2 >= 0)
m.e140 = Constraint(expr= (m.x6 - m.x16)**2 + (m.x35 - m.x45)**2 - (m.x64 +
    m.x74)**2 >= 0)
m.e141 = Constraint(expr= (m.x6 - m.x17)**2 + (m.x35 - m.x46)**2 - (m.x64 +
    m.x75)**2 >= 0)
m.e142 = Constraint(expr= (m.x6 - m.x18)**2 + (m.x35 - m.x47)**2 - (m.x64 +
    m.x76)**2 >= 0)
m.e143 = Constraint(expr= (m.x6 - m.x19)**2 + (m.x35 - m.x48)**2 - (m.x64 +
    m.x77)**2 >= 0)
m.e144 = Constraint(expr= (m.x6 - m.x20)**2 + (m.x35 - m.x49)**2 - (m.x64 +
    m.x78)**2 >= 0)
m.e145 = Constraint(expr= (m.x6 - m.x21)**2 + (m.x35 - m.x50)**2 - (m.x64 +
    m.x79)**2 >= 0)
m.e146 = Constraint(expr= (m.x6 - m.x22)**2 + (m.x35 - m.x51)**2 - (m.x64 +
    m.x80)**2 >= 0)
m.e147 = Constraint(expr= (m.x6 - m.x23)**2 + (m.x35 - m.x52)**2 - (m.x64 +
    m.x81)**2 >= 0)
m.e148 = Constraint(expr= (m.x6 - m.x24)**2 + (m.x35 - m.x53)**2 - (m.x64 +
    m.x82)**2 >= 0)
m.e149 = Constraint(expr= (m.x6 - m.x25)**2 + (m.x35 - m.x54)**2 - (m.x64 +
    m.x83)**2 >= 0)
m.e150 = Constraint(expr= (m.x6 - m.x26)**2 + (m.x35 - m.x55)**2 - (m.x64 +
    m.x84)**2 >= 0)
m.e151 = Constraint(expr= (m.x6 - m.x27)**2 + (m.x35 - m.x56)**2 - (m.x64 +
    m.x85)**2 >= 0)
m.e152 = Constraint(expr= (m.x6 - m.x28)**2 + (m.x35 - m.x57)**2 - (m.x64 +
    m.x86)**2 >= 0)
m.e153 = Constraint(expr= (m.x6 - m.x29)**2 + (m.x35 - m.x58)**2 - (m.x64 +
    m.x87)**2 >= 0)
m.e154 = Constraint(expr= (m.x7 - m.x8)**2 + (m.x36 - m.x37)**2 - (m.x65 +
    m.x66)**2 >= 0)
m.e155 = Constraint(expr= (m.x7 - m.x9)**2 + (m.x36 - m.x38)**2 - (m.x65 +
    m.x67)**2 >= 0)
m.e156 = Constraint(expr= (m.x7 - m.x10)**2 + (m.x36 - m.x39)**2 - (m.x65 +
    m.x68)**2 >= 0)
m.e157 = Constraint(expr= (m.x7 - m.x11)**2 + (m.x36 - m.x40)**2 - (m.x65 +
    m.x69)**2 >= 0)
m.e158 = Constraint(expr= (m.x7 - m.x12)**2 + (m.x36 - m.x41)**2 - (m.x65 +
    m.x70)**2 >= 0)
m.e159 = Constraint(expr= (m.x7 - m.x13)**2 + (m.x36 - m.x42)**2 - (m.x65 +
    m.x71)**2 >= 0)
m.e160 = Constraint(expr= (m.x7 - m.x14)**2 + (m.x36 - m.x43)**2 - (m.x65 +
    m.x72)**2 >= 0)
m.e161 = Constraint(expr= (m.x7 - m.x15)**2 + (m.x36 - m.x44)**2 - (m.x65 +
    m.x73)**2 >= 0)
m.e162 = Constraint(expr= (m.x7 - m.x16)**2 + (m.x36 - m.x45)**2 - (m.x65 +
    m.x74)**2 >= 0)
m.e163 = Constraint(expr= (m.x7 - m.x17)**2 + (m.x36 - m.x46)**2 - (m.x65 +
    m.x75)**2 >= 0)
m.e164 = Constraint(expr= (m.x7 - m.x18)**2 + (m.x36 - m.x47)**2 - (m.x65 +
    m.x76)**2 >= 0)
m.e165 = Constraint(expr= (m.x7 - m.x19)**2 + (m.x36 - m.x48)**2 - (m.x65 +
    m.x77)**2 >= 0)
m.e166 = Constraint(expr= (m.x7 - m.x20)**2 + (m.x36 - m.x49)**2 - (m.x65 +
    m.x78)**2 >= 0)
m.e167 = Constraint(expr= (m.x7 - m.x21)**2 + (m.x36 - m.x50)**2 - (m.x65 +
    m.x79)**2 >= 0)
m.e168 = Constraint(expr= (m.x7 - m.x22)**2 + (m.x36 - m.x51)**2 - (m.x65 +
    m.x80)**2 >= 0)
m.e169 = Constraint(expr= (m.x7 - m.x23)**2 + (m.x36 - m.x52)**2 - (m.x65 +
    m.x81)**2 >= 0)
m.e170 = Constraint(expr= (m.x7 - m.x24)**2 + (m.x36 - m.x53)**2 - (m.x65 +
    m.x82)**2 >= 0)
m.e171 = Constraint(expr= (m.x7 - m.x25)**2 + (m.x36 - m.x54)**2 - (m.x65 +
    m.x83)**2 >= 0)
m.e172 = Constraint(expr= (m.x7 - m.x26)**2 + (m.x36 - m.x55)**2 - (m.x65 +
    m.x84)**2 >= 0)
m.e173 = Constraint(expr= (m.x7 - m.x27)**2 + (m.x36 - m.x56)**2 - (m.x65 +
    m.x85)**2 >= 0)
m.e174 = Constraint(expr= (m.x7 - m.x28)**2 + (m.x36 - m.x57)**2 - (m.x65 +
    m.x86)**2 >= 0)
m.e175 = Constraint(expr= (m.x7 - m.x29)**2 + (m.x36 - m.x58)**2 - (m.x65 +
    m.x87)**2 >= 0)
m.e176 = Constraint(expr= (m.x8 - m.x9)**2 + (m.x37 - m.x38)**2 - (m.x66 +
    m.x67)**2 >= 0)
m.e177 = Constraint(expr= (m.x8 - m.x10)**2 + (m.x37 - m.x39)**2 - (m.x66 +
    m.x68)**2 >= 0)
m.e178 = Constraint(expr= (m.x8 - m.x11)**2 + (m.x37 - m.x40)**2 - (m.x66 +
    m.x69)**2 >= 0)
m.e179 = Constraint(expr= (m.x8 - m.x12)**2 + (m.x37 - m.x41)**2 - (m.x66 +
    m.x70)**2 >= 0)
m.e180 = Constraint(expr= (m.x8 - m.x13)**2 + (m.x37 - m.x42)**2 - (m.x66 +
    m.x71)**2 >= 0)
m.e181 = Constraint(expr= (m.x8 - m.x14)**2 + (m.x37 - m.x43)**2 - (m.x66 +
    m.x72)**2 >= 0)
m.e182 = Constraint(expr= (m.x8 - m.x15)**2 + (m.x37 - m.x44)**2 - (m.x66 +
    m.x73)**2 >= 0)
m.e183 = Constraint(expr= (m.x8 - m.x16)**2 + (m.x37 - m.x45)**2 - (m.x66 +
    m.x74)**2 >= 0)
m.e184 = Constraint(expr= (m.x8 - m.x17)**2 + (m.x37 - m.x46)**2 - (m.x66 +
    m.x75)**2 >= 0)
m.e185 = Constraint(expr= (m.x8 - m.x18)**2 + (m.x37 - m.x47)**2 - (m.x66 +
    m.x76)**2 >= 0)
m.e186 = Constraint(expr= (m.x8 - m.x19)**2 + (m.x37 - m.x48)**2 - (m.x66 +
    m.x77)**2 >= 0)
m.e187 = Constraint(expr= (m.x8 - m.x20)**2 + (m.x37 - m.x49)**2 - (m.x66 +
    m.x78)**2 >= 0)
m.e188 = Constraint(expr= (m.x8 - m.x21)**2 + (m.x37 - m.x50)**2 - (m.x66 +
    m.x79)**2 >= 0)
m.e189 = Constraint(expr= (m.x8 - m.x22)**2 + (m.x37 - m.x51)**2 - (m.x66 +
    m.x80)**2 >= 0)
m.e190 = Constraint(expr= (m.x8 - m.x23)**2 + (m.x37 - m.x52)**2 - (m.x66 +
    m.x81)**2 >= 0)
m.e191 = Constraint(expr= (m.x8 - m.x24)**2 + (m.x37 - m.x53)**2 - (m.x66 +
    m.x82)**2 >= 0)
m.e192 = Constraint(expr= (m.x8 - m.x25)**2 + (m.x37 - m.x54)**2 - (m.x66 +
    m.x83)**2 >= 0)
m.e193 = Constraint(expr= (m.x8 - m.x26)**2 + (m.x37 - m.x55)**2 - (m.x66 +
    m.x84)**2 >= 0)
m.e194 = Constraint(expr= (m.x8 - m.x27)**2 + (m.x37 - m.x56)**2 - (m.x66 +
    m.x85)**2 >= 0)
m.e195 = Constraint(expr= (m.x8 - m.x28)**2 + (m.x37 - m.x57)**2 - (m.x66 +
    m.x86)**2 >= 0)
m.e196 = Constraint(expr= (m.x8 - m.x29)**2 + (m.x37 - m.x58)**2 - (m.x66 +
    m.x87)**2 >= 0)
m.e197 = Constraint(expr= (m.x9 - m.x10)**2 + (m.x38 - m.x39)**2 - (m.x67 +
    m.x68)**2 >= 0)
m.e198 = Constraint(expr= (m.x9 - m.x11)**2 + (m.x38 - m.x40)**2 - (m.x67 +
    m.x69)**2 >= 0)
m.e199 = Constraint(expr= (m.x9 - m.x12)**2 + (m.x38 - m.x41)**2 - (m.x67 +
    m.x70)**2 >= 0)
m.e200 = Constraint(expr= (m.x9 - m.x13)**2 + (m.x38 - m.x42)**2 - (m.x67 +
    m.x71)**2 >= 0)
m.e201 = Constraint(expr= (m.x9 - m.x14)**2 + (m.x38 - m.x43)**2 - (m.x67 +
    m.x72)**2 >= 0)
m.e202 = Constraint(expr= (m.x9 - m.x15)**2 + (m.x38 - m.x44)**2 - (m.x67 +
    m.x73)**2 >= 0)
m.e203 = Constraint(expr= (m.x9 - m.x16)**2 + (m.x38 - m.x45)**2 - (m.x67 +
    m.x74)**2 >= 0)
m.e204 = Constraint(expr= (m.x9 - m.x17)**2 + (m.x38 - m.x46)**2 - (m.x67 +
    m.x75)**2 >= 0)
m.e205 = Constraint(expr= (m.x9 - m.x18)**2 + (m.x38 - m.x47)**2 - (m.x67 +
    m.x76)**2 >= 0)
m.e206 = Constraint(expr= (m.x9 - m.x19)**2 + (m.x38 - m.x48)**2 - (m.x67 +
    m.x77)**2 >= 0)
m.e207 = Constraint(expr= (m.x9 - m.x20)**2 + (m.x38 - m.x49)**2 - (m.x67 +
    m.x78)**2 >= 0)
m.e208 = Constraint(expr= (m.x9 - m.x21)**2 + (m.x38 - m.x50)**2 - (m.x67 +
    m.x79)**2 >= 0)
m.e209 = Constraint(expr= (m.x9 - m.x22)**2 + (m.x38 - m.x51)**2 - (m.x67 +
    m.x80)**2 >= 0)
m.e210 = Constraint(expr= (m.x9 - m.x23)**2 + (m.x38 - m.x52)**2 - (m.x67 +
    m.x81)**2 >= 0)
m.e211 = Constraint(expr= (m.x9 - m.x24)**2 + (m.x38 - m.x53)**2 - (m.x67 +
    m.x82)**2 >= 0)
m.e212 = Constraint(expr= (m.x9 - m.x25)**2 + (m.x38 - m.x54)**2 - (m.x67 +
    m.x83)**2 >= 0)
m.e213 = Constraint(expr= (m.x9 - m.x26)**2 + (m.x38 - m.x55)**2 - (m.x67 +
    m.x84)**2 >= 0)
m.e214 = Constraint(expr= (m.x9 - m.x27)**2 + (m.x38 - m.x56)**2 - (m.x67 +
    m.x85)**2 >= 0)
m.e215 = Constraint(expr= (m.x9 - m.x28)**2 + (m.x38 - m.x57)**2 - (m.x67 +
    m.x86)**2 >= 0)
m.e216 = Constraint(expr= (m.x9 - m.x29)**2 + (m.x38 - m.x58)**2 - (m.x67 +
    m.x87)**2 >= 0)
m.e217 = Constraint(expr= (m.x10 - m.x11)**2 + (m.x39 - m.x40)**2 - (m.x68 +
    m.x69)**2 >= 0)
m.e218 = Constraint(expr= (m.x10 - m.x12)**2 + (m.x39 - m.x41)**2 - (m.x68 +
    m.x70)**2 >= 0)
m.e219 = Constraint(expr= (m.x10 - m.x13)**2 + (m.x39 - m.x42)**2 - (m.x68 +
    m.x71)**2 >= 0)
m.e220 = Constraint(expr= (m.x10 - m.x14)**2 + (m.x39 - m.x43)**2 - (m.x68 +
    m.x72)**2 >= 0)
m.e221 = Constraint(expr= (m.x10 - m.x15)**2 + (m.x39 - m.x44)**2 - (m.x68 +
    m.x73)**2 >= 0)
m.e222 = Constraint(expr= (m.x10 - m.x16)**2 + (m.x39 - m.x45)**2 - (m.x68 +
    m.x74)**2 >= 0)
m.e223 = Constraint(expr= (m.x10 - m.x17)**2 + (m.x39 - m.x46)**2 - (m.x68 +
    m.x75)**2 >= 0)
m.e224 = Constraint(expr= (m.x10 - m.x18)**2 + (m.x39 - m.x47)**2 - (m.x68 +
    m.x76)**2 >= 0)
m.e225 = Constraint(expr= (m.x10 - m.x19)**2 + (m.x39 - m.x48)**2 - (m.x68 +
    m.x77)**2 >= 0)
m.e226 = Constraint(expr= (m.x10 - m.x20)**2 + (m.x39 - m.x49)**2 - (m.x68 +
    m.x78)**2 >= 0)
m.e227 = Constraint(expr= (m.x10 - m.x21)**2 + (m.x39 - m.x50)**2 - (m.x68 +
    m.x79)**2 >= 0)
m.e228 = Constraint(expr= (m.x10 - m.x22)**2 + (m.x39 - m.x51)**2 - (m.x68 +
    m.x80)**2 >= 0)
m.e229 = Constraint(expr= (m.x10 - m.x23)**2 + (m.x39 - m.x52)**2 - (m.x68 +
    m.x81)**2 >= 0)
m.e230 = Constraint(expr= (m.x10 - m.x24)**2 + (m.x39 - m.x53)**2 - (m.x68 +
    m.x82)**2 >= 0)
m.e231 = Constraint(expr= (m.x10 - m.x25)**2 + (m.x39 - m.x54)**2 - (m.x68 +
    m.x83)**2 >= 0)
m.e232 = Constraint(expr= (m.x10 - m.x26)**2 + (m.x39 - m.x55)**2 - (m.x68 +
    m.x84)**2 >= 0)
m.e233 = Constraint(expr= (m.x10 - m.x27)**2 + (m.x39 - m.x56)**2 - (m.x68 +
    m.x85)**2 >= 0)
m.e234 = Constraint(expr= (m.x10 - m.x28)**2 + (m.x39 - m.x57)**2 - (m.x68 +
    m.x86)**2 >= 0)
m.e235 = Constraint(expr= (m.x10 - m.x29)**2 + (m.x39 - m.x58)**2 - (m.x68 +
    m.x87)**2 >= 0)
m.e236 = Constraint(expr= (m.x11 - m.x12)**2 + (m.x40 - m.x41)**2 - (m.x69 +
    m.x70)**2 >= 0)
m.e237 = Constraint(expr= (m.x11 - m.x13)**2 + (m.x40 - m.x42)**2 - (m.x69 +
    m.x71)**2 >= 0)
m.e238 = Constraint(expr= (m.x11 - m.x14)**2 + (m.x40 - m.x43)**2 - (m.x69 +
    m.x72)**2 >= 0)
m.e239 = Constraint(expr= (m.x11 - m.x15)**2 + (m.x40 - m.x44)**2 - (m.x69 +
    m.x73)**2 >= 0)
m.e240 = Constraint(expr= (m.x11 - m.x16)**2 + (m.x40 - m.x45)**2 - (m.x69 +
    m.x74)**2 >= 0)
m.e241 = Constraint(expr= (m.x11 - m.x17)**2 + (m.x40 - m.x46)**2 - (m.x69 +
    m.x75)**2 >= 0)
m.e242 = Constraint(expr= (m.x11 - m.x18)**2 + (m.x40 - m.x47)**2 - (m.x69 +
    m.x76)**2 >= 0)
m.e243 = Constraint(expr= (m.x11 - m.x19)**2 + (m.x40 - m.x48)**2 - (m.x69 +
    m.x77)**2 >= 0)
m.e244 = Constraint(expr= (m.x11 - m.x20)**2 + (m.x40 - m.x49)**2 - (m.x69 +
    m.x78)**2 >= 0)
m.e245 = Constraint(expr= (m.x11 - m.x21)**2 + (m.x40 - m.x50)**2 - (m.x69 +
    m.x79)**2 >= 0)
m.e246 = Constraint(expr= (m.x11 - m.x22)**2 + (m.x40 - m.x51)**2 - (m.x69 +
    m.x80)**2 >= 0)
m.e247 = Constraint(expr= (m.x11 - m.x23)**2 + (m.x40 - m.x52)**2 - (m.x69 +
    m.x81)**2 >= 0)
m.e248 = Constraint(expr= (m.x11 - m.x24)**2 + (m.x40 - m.x53)**2 - (m.x69 +
    m.x82)**2 >= 0)
m.e249 = Constraint(expr= (m.x11 - m.x25)**2 + (m.x40 - m.x54)**2 - (m.x69 +
    m.x83)**2 >= 0)
m.e250 = Constraint(expr= (m.x11 - m.x26)**2 + (m.x40 - m.x55)**2 - (m.x69 +
    m.x84)**2 >= 0)
m.e251 = Constraint(expr= (m.x11 - m.x27)**2 + (m.x40 - m.x56)**2 - (m.x69 +
    m.x85)**2 >= 0)
m.e252 = Constraint(expr= (m.x11 - m.x28)**2 + (m.x40 - m.x57)**2 - (m.x69 +
    m.x86)**2 >= 0)
m.e253 = Constraint(expr= (m.x11 - m.x29)**2 + (m.x40 - m.x58)**2 - (m.x69 +
    m.x87)**2 >= 0)
m.e254 = Constraint(expr= (m.x12 - m.x13)**2 + (m.x41 - m.x42)**2 - (m.x70 +
    m.x71)**2 >= 0)
m.e255 = Constraint(expr= (m.x12 - m.x14)**2 + (m.x41 - m.x43)**2 - (m.x70 +
    m.x72)**2 >= 0)
m.e256 = Constraint(expr= (m.x12 - m.x15)**2 + (m.x41 - m.x44)**2 - (m.x70 +
    m.x73)**2 >= 0)
m.e257 = Constraint(expr= (m.x12 - m.x16)**2 + (m.x41 - m.x45)**2 - (m.x70 +
    m.x74)**2 >= 0)
m.e258 = Constraint(expr= (m.x12 - m.x17)**2 + (m.x41 - m.x46)**2 - (m.x70 +
    m.x75)**2 >= 0)
m.e259 = Constraint(expr= (m.x12 - m.x18)**2 + (m.x41 - m.x47)**2 - (m.x70 +
    m.x76)**2 >= 0)
m.e260 = Constraint(expr= (m.x12 - m.x19)**2 + (m.x41 - m.x48)**2 - (m.x70 +
    m.x77)**2 >= 0)
m.e261 = Constraint(expr= (m.x12 - m.x20)**2 + (m.x41 - m.x49)**2 - (m.x70 +
    m.x78)**2 >= 0)
m.e262 = Constraint(expr= (m.x12 - m.x21)**2 + (m.x41 - m.x50)**2 - (m.x70 +
    m.x79)**2 >= 0)
m.e263 = Constraint(expr= (m.x12 - m.x22)**2 + (m.x41 - m.x51)**2 - (m.x70 +
    m.x80)**2 >= 0)
m.e264 = Constraint(expr= (m.x12 - m.x23)**2 + (m.x41 - m.x52)**2 - (m.x70 +
    m.x81)**2 >= 0)
m.e265 = Constraint(expr= (m.x12 - m.x24)**2 + (m.x41 - m.x53)**2 - (m.x70 +
    m.x82)**2 >= 0)
m.e266 = Constraint(expr= (m.x12 - m.x25)**2 + (m.x41 - m.x54)**2 - (m.x70 +
    m.x83)**2 >= 0)
m.e267 = Constraint(expr= (m.x12 - m.x26)**2 + (m.x41 - m.x55)**2 - (m.x70 +
    m.x84)**2 >= 0)
m.e268 = Constraint(expr= (m.x12 - m.x27)**2 + (m.x41 - m.x56)**2 - (m.x70 +
    m.x85)**2 >= 0)
m.e269 = Constraint(expr= (m.x12 - m.x28)**2 + (m.x41 - m.x57)**2 - (m.x70 +
    m.x86)**2 >= 0)
m.e270 = Constraint(expr= (m.x12 - m.x29)**2 + (m.x41 - m.x58)**2 - (m.x70 +
    m.x87)**2 >= 0)
m.e271 = Constraint(expr= (m.x13 - m.x14)**2 + (m.x42 - m.x43)**2 - (m.x71 +
    m.x72)**2 >= 0)
m.e272 = Constraint(expr= (m.x13 - m.x15)**2 + (m.x42 - m.x44)**2 - (m.x71 +
    m.x73)**2 >= 0)
m.e273 = Constraint(expr= (m.x13 - m.x16)**2 + (m.x42 - m.x45)**2 - (m.x71 +
    m.x74)**2 >= 0)
m.e274 = Constraint(expr= (m.x13 - m.x17)**2 + (m.x42 - m.x46)**2 - (m.x71 +
    m.x75)**2 >= 0)
m.e275 = Constraint(expr= (m.x13 - m.x18)**2 + (m.x42 - m.x47)**2 - (m.x71 +
    m.x76)**2 >= 0)
m.e276 = Constraint(expr= (m.x13 - m.x19)**2 + (m.x42 - m.x48)**2 - (m.x71 +
    m.x77)**2 >= 0)
m.e277 = Constraint(expr= (m.x13 - m.x20)**2 + (m.x42 - m.x49)**2 - (m.x71 +
    m.x78)**2 >= 0)
m.e278 = Constraint(expr= (m.x13 - m.x21)**2 + (m.x42 - m.x50)**2 - (m.x71 +
    m.x79)**2 >= 0)
m.e279 = Constraint(expr= (m.x13 - m.x22)**2 + (m.x42 - m.x51)**2 - (m.x71 +
    m.x80)**2 >= 0)
m.e280 = Constraint(expr= (m.x13 - m.x23)**2 + (m.x42 - m.x52)**2 - (m.x71 +
    m.x81)**2 >= 0)
m.e281 = Constraint(expr= (m.x13 - m.x24)**2 + (m.x42 - m.x53)**2 - (m.x71 +
    m.x82)**2 >= 0)
m.e282 = Constraint(expr= (m.x13 - m.x25)**2 + (m.x42 - m.x54)**2 - (m.x71 +
    m.x83)**2 >= 0)
m.e283 = Constraint(expr= (m.x13 - m.x26)**2 + (m.x42 - m.x55)**2 - (m.x71 +
    m.x84)**2 >= 0)
m.e284 = Constraint(expr= (m.x13 - m.x27)**2 + (m.x42 - m.x56)**2 - (m.x71 +
    m.x85)**2 >= 0)
m.e285 = Constraint(expr= (m.x13 - m.x28)**2 + (m.x42 - m.x57)**2 - (m.x71 +
    m.x86)**2 >= 0)
m.e286 = Constraint(expr= (m.x13 - m.x29)**2 + (m.x42 - m.x58)**2 - (m.x71 +
    m.x87)**2 >= 0)
m.e287 = Constraint(expr= (m.x14 - m.x15)**2 + (m.x43 - m.x44)**2 - (m.x72 +
    m.x73)**2 >= 0)
m.e288 = Constraint(expr= (m.x14 - m.x16)**2 + (m.x43 - m.x45)**2 - (m.x72 +
    m.x74)**2 >= 0)
m.e289 = Constraint(expr= (m.x14 - m.x17)**2 + (m.x43 - m.x46)**2 - (m.x72 +
    m.x75)**2 >= 0)
m.e290 = Constraint(expr= (m.x14 - m.x18)**2 + (m.x43 - m.x47)**2 - (m.x72 +
    m.x76)**2 >= 0)
m.e291 = Constraint(expr= (m.x14 - m.x19)**2 + (m.x43 - m.x48)**2 - (m.x72 +
    m.x77)**2 >= 0)
m.e292 = Constraint(expr= (m.x14 - m.x20)**2 + (m.x43 - m.x49)**2 - (m.x72 +
    m.x78)**2 >= 0)
m.e293 = Constraint(expr= (m.x14 - m.x21)**2 + (m.x43 - m.x50)**2 - (m.x72 +
    m.x79)**2 >= 0)
m.e294 = Constraint(expr= (m.x14 - m.x22)**2 + (m.x43 - m.x51)**2 - (m.x72 +
    m.x80)**2 >= 0)
m.e295 = Constraint(expr= (m.x14 - m.x23)**2 + (m.x43 - m.x52)**2 - (m.x72 +
    m.x81)**2 >= 0)
m.e296 = Constraint(expr= (m.x14 - m.x24)**2 + (m.x43 - m.x53)**2 - (m.x72 +
    m.x82)**2 >= 0)
m.e297 = Constraint(expr= (m.x14 - m.x25)**2 + (m.x43 - m.x54)**2 - (m.x72 +
    m.x83)**2 >= 0)
m.e298 = Constraint(expr= (m.x14 - m.x26)**2 + (m.x43 - m.x55)**2 - (m.x72 +
    m.x84)**2 >= 0)
m.e299 = Constraint(expr= (m.x14 - m.x27)**2 + (m.x43 - m.x56)**2 - (m.x72 +
    m.x85)**2 >= 0)
m.e300 = Constraint(expr= (m.x14 - m.x28)**2 + (m.x43 - m.x57)**2 - (m.x72 +
    m.x86)**2 >= 0)
m.e301 = Constraint(expr= (m.x14 - m.x29)**2 + (m.x43 - m.x58)**2 - (m.x72 +
    m.x87)**2 >= 0)
m.e302 = Constraint(expr= (m.x15 - m.x16)**2 + (m.x44 - m.x45)**2 - (m.x73 +
    m.x74)**2 >= 0)
m.e303 = Constraint(expr= (m.x15 - m.x17)**2 + (m.x44 - m.x46)**2 - (m.x73 +
    m.x75)**2 >= 0)
m.e304 = Constraint(expr= (m.x15 - m.x18)**2 + (m.x44 - m.x47)**2 - (m.x73 +
    m.x76)**2 >= 0)
m.e305 = Constraint(expr= (m.x15 - m.x19)**2 + (m.x44 - m.x48)**2 - (m.x73 +
    m.x77)**2 >= 0)
m.e306 = Constraint(expr= (m.x15 - m.x20)**2 + (m.x44 - m.x49)**2 - (m.x73 +
    m.x78)**2 >= 0)
m.e307 = Constraint(expr= (m.x15 - m.x21)**2 + (m.x44 - m.x50)**2 - (m.x73 +
    m.x79)**2 >= 0)
m.e308 = Constraint(expr= (m.x15 - m.x22)**2 + (m.x44 - m.x51)**2 - (m.x73 +
    m.x80)**2 >= 0)
m.e309 = Constraint(expr= (m.x15 - m.x23)**2 + (m.x44 - m.x52)**2 - (m.x73 +
    m.x81)**2 >= 0)
m.e310 = Constraint(expr= (m.x15 - m.x24)**2 + (m.x44 - m.x53)**2 - (m.x73 +
    m.x82)**2 >= 0)
m.e311 = Constraint(expr= (m.x15 - m.x25)**2 + (m.x44 - m.x54)**2 - (m.x73 +
    m.x83)**2 >= 0)
m.e312 = Constraint(expr= (m.x15 - m.x26)**2 + (m.x44 - m.x55)**2 - (m.x73 +
    m.x84)**2 >= 0)
m.e313 = Constraint(expr= (m.x15 - m.x27)**2 + (m.x44 - m.x56)**2 - (m.x73 +
    m.x85)**2 >= 0)
m.e314 = Constraint(expr= (m.x15 - m.x28)**2 + (m.x44 - m.x57)**2 - (m.x73 +
    m.x86)**2 >= 0)
m.e315 = Constraint(expr= (m.x15 - m.x29)**2 + (m.x44 - m.x58)**2 - (m.x73 +
    m.x87)**2 >= 0)
m.e316 = Constraint(expr= (m.x16 - m.x17)**2 + (m.x45 - m.x46)**2 - (m.x74 +
    m.x75)**2 >= 0)
m.e317 = Constraint(expr= (m.x16 - m.x18)**2 + (m.x45 - m.x47)**2 - (m.x74 +
    m.x76)**2 >= 0)
m.e318 = Constraint(expr= (m.x16 - m.x19)**2 + (m.x45 - m.x48)**2 - (m.x74 +
    m.x77)**2 >= 0)
m.e319 = Constraint(expr= (m.x16 - m.x20)**2 + (m.x45 - m.x49)**2 - (m.x74 +
    m.x78)**2 >= 0)
m.e320 = Constraint(expr= (m.x16 - m.x21)**2 + (m.x45 - m.x50)**2 - (m.x74 +
    m.x79)**2 >= 0)
m.e321 = Constraint(expr= (m.x16 - m.x22)**2 + (m.x45 - m.x51)**2 - (m.x74 +
    m.x80)**2 >= 0)
m.e322 = Constraint(expr= (m.x16 - m.x23)**2 + (m.x45 - m.x52)**2 - (m.x74 +
    m.x81)**2 >= 0)
m.e323 = Constraint(expr= (m.x16 - m.x24)**2 + (m.x45 - m.x53)**2 - (m.x74 +
    m.x82)**2 >= 0)
m.e324 = Constraint(expr= (m.x16 - m.x25)**2 + (m.x45 - m.x54)**2 - (m.x74 +
    m.x83)**2 >= 0)
m.e325 = Constraint(expr= (m.x16 - m.x26)**2 + (m.x45 - m.x55)**2 - (m.x74 +
    m.x84)**2 >= 0)
m.e326 = Constraint(expr= (m.x16 - m.x27)**2 + (m.x45 - m.x56)**2 - (m.x74 +
    m.x85)**2 >= 0)
m.e327 = Constraint(expr= (m.x16 - m.x28)**2 + (m.x45 - m.x57)**2 - (m.x74 +
    m.x86)**2 >= 0)
m.e328 = Constraint(expr= (m.x16 - m.x29)**2 + (m.x45 - m.x58)**2 - (m.x74 +
    m.x87)**2 >= 0)
m.e329 = Constraint(expr= (m.x17 - m.x18)**2 + (m.x46 - m.x47)**2 - (m.x75 +
    m.x76)**2 >= 0)
m.e330 = Constraint(expr= (m.x17 - m.x19)**2 + (m.x46 - m.x48)**2 - (m.x75 +
    m.x77)**2 >= 0)
m.e331 = Constraint(expr= (m.x17 - m.x20)**2 + (m.x46 - m.x49)**2 - (m.x75 +
    m.x78)**2 >= 0)
m.e332 = Constraint(expr= (m.x17 - m.x21)**2 + (m.x46 - m.x50)**2 - (m.x75 +
    m.x79)**2 >= 0)
m.e333 = Constraint(expr= (m.x17 - m.x22)**2 + (m.x46 - m.x51)**2 - (m.x75 +
    m.x80)**2 >= 0)
m.e334 = Constraint(expr= (m.x17 - m.x23)**2 + (m.x46 - m.x52)**2 - (m.x75 +
    m.x81)**2 >= 0)
m.e335 = Constraint(expr= (m.x17 - m.x24)**2 + (m.x46 - m.x53)**2 - (m.x75 +
    m.x82)**2 >= 0)
m.e336 = Constraint(expr= (m.x17 - m.x25)**2 + (m.x46 - m.x54)**2 - (m.x75 +
    m.x83)**2 >= 0)
m.e337 = Constraint(expr= (m.x17 - m.x26)**2 + (m.x46 - m.x55)**2 - (m.x75 +
    m.x84)**2 >= 0)
m.e338 = Constraint(expr= (m.x17 - m.x27)**2 + (m.x46 - m.x56)**2 - (m.x75 +
    m.x85)**2 >= 0)
m.e339 = Constraint(expr= (m.x17 - m.x28)**2 + (m.x46 - m.x57)**2 - (m.x75 +
    m.x86)**2 >= 0)
m.e340 = Constraint(expr= (m.x17 - m.x29)**2 + (m.x46 - m.x58)**2 - (m.x75 +
    m.x87)**2 >= 0)
m.e341 = Constraint(expr= (m.x18 - m.x19)**2 + (m.x47 - m.x48)**2 - (m.x76 +
    m.x77)**2 >= 0)
m.e342 = Constraint(expr= (m.x18 - m.x20)**2 + (m.x47 - m.x49)**2 - (m.x76 +
    m.x78)**2 >= 0)
m.e343 = Constraint(expr= (m.x18 - m.x21)**2 + (m.x47 - m.x50)**2 - (m.x76 +
    m.x79)**2 >= 0)
m.e344 = Constraint(expr= (m.x18 - m.x22)**2 + (m.x47 - m.x51)**2 - (m.x76 +
    m.x80)**2 >= 0)
m.e345 = Constraint(expr= (m.x18 - m.x23)**2 + (m.x47 - m.x52)**2 - (m.x76 +
    m.x81)**2 >= 0)
m.e346 = Constraint(expr= (m.x18 - m.x24)**2 + (m.x47 - m.x53)**2 - (m.x76 +
    m.x82)**2 >= 0)
m.e347 = Constraint(expr= (m.x18 - m.x25)**2 + (m.x47 - m.x54)**2 - (m.x76 +
    m.x83)**2 >= 0)
m.e348 = Constraint(expr= (m.x18 - m.x26)**2 + (m.x47 - m.x55)**2 - (m.x76 +
    m.x84)**2 >= 0)
m.e349 = Constraint(expr= (m.x18 - m.x27)**2 + (m.x47 - m.x56)**2 - (m.x76 +
    m.x85)**2 >= 0)
m.e350 = Constraint(expr= (m.x18 - m.x28)**2 + (m.x47 - m.x57)**2 - (m.x76 +
    m.x86)**2 >= 0)
m.e351 = Constraint(expr= (m.x18 - m.x29)**2 + (m.x47 - m.x58)**2 - (m.x76 +
    m.x87)**2 >= 0)
m.e352 = Constraint(expr= (m.x19 - m.x20)**2 + (m.x48 - m.x49)**2 - (m.x77 +
    m.x78)**2 >= 0)
m.e353 = Constraint(expr= (m.x19 - m.x21)**2 + (m.x48 - m.x50)**2 - (m.x77 +
    m.x79)**2 >= 0)
m.e354 = Constraint(expr= (m.x19 - m.x22)**2 + (m.x48 - m.x51)**2 - (m.x77 +
    m.x80)**2 >= 0)
m.e355 = Constraint(expr= (m.x19 - m.x23)**2 + (m.x48 - m.x52)**2 - (m.x77 +
    m.x81)**2 >= 0)
m.e356 = Constraint(expr= (m.x19 - m.x24)**2 + (m.x48 - m.x53)**2 - (m.x77 +
    m.x82)**2 >= 0)
m.e357 = Constraint(expr= (m.x19 - m.x25)**2 + (m.x48 - m.x54)**2 - (m.x77 +
    m.x83)**2 >= 0)
m.e358 = Constraint(expr= (m.x19 - m.x26)**2 + (m.x48 - m.x55)**2 - (m.x77 +
    m.x84)**2 >= 0)
m.e359 = Constraint(expr= (m.x19 - m.x27)**2 + (m.x48 - m.x56)**2 - (m.x77 +
    m.x85)**2 >= 0)
m.e360 = Constraint(expr= (m.x19 - m.x28)**2 + (m.x48 - m.x57)**2 - (m.x77 +
    m.x86)**2 >= 0)
m.e361 = Constraint(expr= (m.x19 - m.x29)**2 + (m.x48 - m.x58)**2 - (m.x77 +
    m.x87)**2 >= 0)
m.e362 = Constraint(expr= (m.x20 - m.x21)**2 + (m.x49 - m.x50)**2 - (m.x78 +
    m.x79)**2 >= 0)
m.e363 = Constraint(expr= (m.x20 - m.x22)**2 + (m.x49 - m.x51)**2 - (m.x78 +
    m.x80)**2 >= 0)
m.e364 = Constraint(expr= (m.x20 - m.x23)**2 + (m.x49 - m.x52)**2 - (m.x78 +
    m.x81)**2 >= 0)
m.e365 = Constraint(expr= (m.x20 - m.x24)**2 + (m.x49 - m.x53)**2 - (m.x78 +
    m.x82)**2 >= 0)
m.e366 = Constraint(expr= (m.x20 - m.x25)**2 + (m.x49 - m.x54)**2 - (m.x78 +
    m.x83)**2 >= 0)
m.e367 = Constraint(expr= (m.x20 - m.x26)**2 + (m.x49 - m.x55)**2 - (m.x78 +
    m.x84)**2 >= 0)
m.e368 = Constraint(expr= (m.x20 - m.x27)**2 + (m.x49 - m.x56)**2 - (m.x78 +
    m.x85)**2 >= 0)
m.e369 = Constraint(expr= (m.x20 - m.x28)**2 + (m.x49 - m.x57)**2 - (m.x78 +
    m.x86)**2 >= 0)
m.e370 = Constraint(expr= (m.x20 - m.x29)**2 + (m.x49 - m.x58)**2 - (m.x78 +
    m.x87)**2 >= 0)
m.e371 = Constraint(expr= (m.x21 - m.x22)**2 + (m.x50 - m.x51)**2 - (m.x79 +
    m.x80)**2 >= 0)
m.e372 = Constraint(expr= (m.x21 - m.x23)**2 + (m.x50 - m.x52)**2 - (m.x79 +
    m.x81)**2 >= 0)
m.e373 = Constraint(expr= (m.x21 - m.x24)**2 + (m.x50 - m.x53)**2 - (m.x79 +
    m.x82)**2 >= 0)
m.e374 = Constraint(expr= (m.x21 - m.x25)**2 + (m.x50 - m.x54)**2 - (m.x79 +
    m.x83)**2 >= 0)
m.e375 = Constraint(expr= (m.x21 - m.x26)**2 + (m.x50 - m.x55)**2 - (m.x79 +
    m.x84)**2 >= 0)
m.e376 = Constraint(expr= (m.x21 - m.x27)**2 + (m.x50 - m.x56)**2 - (m.x79 +
    m.x85)**2 >= 0)
m.e377 = Constraint(expr= (m.x21 - m.x28)**2 + (m.x50 - m.x57)**2 - (m.x79 +
    m.x86)**2 >= 0)
m.e378 = Constraint(expr= (m.x21 - m.x29)**2 + (m.x50 - m.x58)**2 - (m.x79 +
    m.x87)**2 >= 0)
m.e379 = Constraint(expr= (m.x22 - m.x23)**2 + (m.x51 - m.x52)**2 - (m.x80 +
    m.x81)**2 >= 0)
m.e380 = Constraint(expr= (m.x22 - m.x24)**2 + (m.x51 - m.x53)**2 - (m.x80 +
    m.x82)**2 >= 0)
m.e381 = Constraint(expr= (m.x22 - m.x25)**2 + (m.x51 - m.x54)**2 - (m.x80 +
    m.x83)**2 >= 0)
m.e382 = Constraint(expr= (m.x22 - m.x26)**2 + (m.x51 - m.x55)**2 - (m.x80 +
    m.x84)**2 >= 0)
m.e383 = Constraint(expr= (m.x22 - m.x27)**2 + (m.x51 - m.x56)**2 - (m.x80 +
    m.x85)**2 >= 0)
m.e384 = Constraint(expr= (m.x22 - m.x28)**2 + (m.x51 - m.x57)**2 - (m.x80 +
    m.x86)**2 >= 0)
m.e385 = Constraint(expr= (m.x22 - m.x29)**2 + (m.x51 - m.x58)**2 - (m.x80 +
    m.x87)**2 >= 0)
m.e386 = Constraint(expr= (m.x23 - m.x24)**2 + (m.x52 - m.x53)**2 - (m.x81 +
    m.x82)**2 >= 0)
m.e387 = Constraint(expr= (m.x23 - m.x25)**2 + (m.x52 - m.x54)**2 - (m.x81 +
    m.x83)**2 >= 0)
m.e388 = Constraint(expr= (m.x23 - m.x26)**2 + (m.x52 - m.x55)**2 - (m.x81 +
    m.x84)**2 >= 0)
m.e389 = Constraint(expr= (m.x23 - m.x27)**2 + (m.x52 - m.x56)**2 - (m.x81 +
    m.x85)**2 >= 0)
m.e390 = Constraint(expr= (m.x23 - m.x28)**2 + (m.x52 - m.x57)**2 - (m.x81 +
    m.x86)**2 >= 0)
m.e391 = Constraint(expr= (m.x23 - m.x29)**2 + (m.x52 - m.x58)**2 - (m.x81 +
    m.x87)**2 >= 0)
m.e392 = Constraint(expr= (m.x24 - m.x25)**2 + (m.x53 - m.x54)**2 - (m.x82 +
    m.x83)**2 >= 0)
m.e393 = Constraint(expr= (m.x24 - m.x26)**2 + (m.x53 - m.x55)**2 - (m.x82 +
    m.x84)**2 >= 0)
m.e394 = Constraint(expr= (m.x24 - m.x27)**2 + (m.x53 - m.x56)**2 - (m.x82 +
    m.x85)**2 >= 0)
m.e395 = Constraint(expr= (m.x24 - m.x28)**2 + (m.x53 - m.x57)**2 - (m.x82 +
    m.x86)**2 >= 0)
m.e396 = Constraint(expr= (m.x24 - m.x29)**2 + (m.x53 - m.x58)**2 - (m.x82 +
    m.x87)**2 >= 0)
m.e397 = Constraint(expr= (m.x25 - m.x26)**2 + (m.x54 - m.x55)**2 - (m.x83 +
    m.x84)**2 >= 0)
m.e398 = Constraint(expr= (m.x25 - m.x27)**2 + (m.x54 - m.x56)**2 - (m.x83 +
    m.x85)**2 >= 0)
m.e399 = Constraint(expr= (m.x25 - m.x28)**2 + (m.x54 - m.x57)**2 - (m.x83 +
    m.x86)**2 >= 0)
m.e400 = Constraint(expr= (m.x25 - m.x29)**2 + (m.x54 - m.x58)**2 - (m.x83 +
    m.x87)**2 >= 0)
m.e401 = Constraint(expr= (m.x26 - m.x27)**2 + (m.x55 - m.x56)**2 - (m.x84 +
    m.x85)**2 >= 0)
m.e402 = Constraint(expr= (m.x26 - m.x28)**2 + (m.x55 - m.x57)**2 - (m.x84 +
    m.x86)**2 >= 0)
m.e403 = Constraint(expr= (m.x26 - m.x29)**2 + (m.x55 - m.x58)**2 - (m.x84 +
    m.x87)**2 >= 0)
m.e404 = Constraint(expr= (m.x27 - m.x28)**2 + (m.x56 - m.x57)**2 - (m.x85 +
    m.x86)**2 >= 0)
m.e405 = Constraint(expr= (m.x27 - m.x29)**2 + (m.x56 - m.x58)**2 - (m.x85 +
    m.x87)**2 >= 0)
m.e406 = Constraint(expr= (m.x28 - m.x29)**2 + (m.x57 - m.x58)**2 - (m.x86 +
    m.x87)**2 >= 0)
m.e407 = Constraint(expr= m.x59 - m.x88 == 0)
m.e408 = Constraint(expr= m.x60 - 2 * m.x88 == 0)
m.e409 = Constraint(expr= m.x61 - 3.0000000000000004 * m.x88 == 0)
m.e410 = Constraint(expr= m.x62 - 4 * m.x88 == 0)
m.e411 = Constraint(expr= m.x63 - 4.999999999999999 * m.x88 == 0)
m.e412 = Constraint(expr= m.x64 - 6 * m.x88 == 0)
m.e413 = Constraint(expr= m.x65 - 6.999999999999999 * m.x88 == 0)
m.e414 = Constraint(expr= m.x66 - 7.999999999999998 * m.x88 == 0)
m.e415 = Constraint(expr= m.x67 - 9.000000000000002 * m.x88 == 0)
m.e416 = Constraint(expr= m.x68 - 10.000000000000002 * m.x88 == 0)
m.e417 = Constraint(expr= m.x69 - 11.000000000000002 * m.x88 == 0)
m.e418 = Constraint(expr= m.x70 - 12 * m.x88 == 0)
m.e419 = Constraint(expr= m.x71 - 13 * m.x88 == 0)
m.e420 = Constraint(expr= m.x72 - 13.999999999999996 * m.x88 == 0)
m.e421 = Constraint(expr= m.x73 - 15 * m.x88 == 0)
m.e422 = Constraint(expr= m.x74 - 15.999999999999998 * m.x88 == 0)
m.e423 = Constraint(expr= m.x75 - 17 * m.x88 == 0)
m.e424 = Constraint(expr= m.x76 - 17.999999999999996 * m.x88 == 0)
m.e425 = Constraint(expr= m.x77 - 18.999999999999996 * m.x88 == 0)
m.e426 = Constraint(expr= m.x78 - 19.999999999999996 * m.x88 == 0)
m.e427 = Constraint(expr= m.x79 - 21 * m.x88 == 0)
m.e428 = Constraint(expr= m.x80 - 22.000000000000004 * m.x88 == 0)
m.e429 = Constraint(expr= m.x81 - 23 * m.x88 == 0)
m.e430 = Constraint(expr= m.x82 - 24.000000000000004 * m.x88 == 0)
m.e431 = Constraint(expr= m.x83 - 24.999999999999996 * m.x88 == 0)
m.e432 = Constraint(expr= m.x84 - 26.000000000000004 * m.x88 == 0)
m.e433 = Constraint(expr= m.x85 - 27 * m.x88 == 0)
m.e434 = Constraint(expr= m.x86 - 27.999999999999996 * m.x88 == 0)
m.e435 = Constraint(expr= m.x87 - 29.000000000000004 * m.x88 == 0)
m.e436 = Constraint(expr= m.x1**2 + m.x30**2 - (1 - m.x59)**2 <= 0)
m.e437 = Constraint(expr= m.x2**2 + m.x31**2 - (1 - m.x60)**2 <= 0)
m.e438 = Constraint(expr= m.x3**2 + m.x32**2 - (1 - m.x61)**2 <= 0)
m.e439 = Constraint(expr= m.x4**2 + m.x33**2 - (1 - m.x62)**2 <= 0)
m.e440 = Constraint(expr= m.x5**2 + m.x34**2 - (1 - m.x63)**2 <= 0)
m.e441 = Constraint(expr= m.x6**2 + m.x35**2 - (1 - m.x64)**2 <= 0)
m.e442 = Constraint(expr= m.x7**2 + m.x36**2 - (1 - m.x65)**2 <= 0)
m.e443 = Constraint(expr= m.x8**2 + m.x37**2 - (1 - m.x66)**2 <= 0)
m.e444 = Constraint(expr= m.x9**2 + m.x38**2 - (1 - m.x67)**2 <= 0)
m.e445 = Constraint(expr= m.x10**2 + m.x39**2 - (1 - m.x68)**2 <= 0)
m.e446 = Constraint(expr= m.x11**2 + m.x40**2 - (1 - m.x69)**2 <= 0)
m.e447 = Constraint(expr= m.x12**2 + m.x41**2 - (1 - m.x70)**2 <= 0)
m.e448 = Constraint(expr= m.x13**2 + m.x42**2 - (1 - m.x71)**2 <= 0)
m.e449 = Constraint(expr= m.x14**2 + m.x43**2 - (1 - m.x72)**2 <= 0)
m.e450 = Constraint(expr= m.x15**2 + m.x44**2 - (1 - m.x73)**2 <= 0)
m.e451 = Constraint(expr= m.x16**2 + m.x45**2 - (1 - m.x74)**2 <= 0)
m.e452 = Constraint(expr= m.x17**2 + m.x46**2 - (1 - m.x75)**2 <= 0)
m.e453 = Constraint(expr= m.x18**2 + m.x47**2 - (1 - m.x76)**2 <= 0)
m.e454 = Constraint(expr= m.x19**2 + m.x48**2 - (1 - m.x77)**2 <= 0)
m.e455 = Constraint(expr= m.x20**2 + m.x49**2 - (1 - m.x78)**2 <= 0)
m.e456 = Constraint(expr= m.x21**2 + m.x50**2 - (1 - m.x79)**2 <= 0)
m.e457 = Constraint(expr= m.x22**2 + m.x51**2 - (1 - m.x80)**2 <= 0)
m.e458 = Constraint(expr= m.x23**2 + m.x52**2 - (1 - m.x81)**2 <= 0)
m.e459 = Constraint(expr= m.x24**2 + m.x53**2 - (1 - m.x82)**2 <= 0)
m.e460 = Constraint(expr= m.x25**2 + m.x54**2 - (1 - m.x83)**2 <= 0)
m.e461 = Constraint(expr= m.x26**2 + m.x55**2 - (1 - m.x84)**2 <= 0)
m.e462 = Constraint(expr= m.x27**2 + m.x56**2 - (1 - m.x85)**2 <= 0)
m.e463 = Constraint(expr= m.x28**2 + m.x57**2 - (1 - m.x86)**2 <= 0)
m.e464 = Constraint(expr= m.x29**2 + m.x58**2 - (1 - m.x87)**2 <= 0)
