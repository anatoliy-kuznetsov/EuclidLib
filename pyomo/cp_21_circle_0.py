# NLP written by GAMS Convert at 05/15/24 11:39:19
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       252       21      210       21        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        64       64        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#      1365       42     1323
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
m.x43 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x44 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x45 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x46 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x47 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x48 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x49 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x50 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x51 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x52 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x53 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x54 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x55 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x56 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x57 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x58 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x59 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x60 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x61 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x62 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x63 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x64 = Var(within=Reals, bounds=(None,None), initialize=0)

m.obj = Objective(sense=maximize, expr= m.x64)

m.e1 = Constraint(expr= (m.x1 - m.x2)**2 + (m.x22 - m.x23)**2 - (m.x43 + m.x44)
    **2 >= 0)
m.e2 = Constraint(expr= (m.x1 - m.x3)**2 + (m.x22 - m.x24)**2 - (m.x43 + m.x45)
    **2 >= 0)
m.e3 = Constraint(expr= (m.x1 - m.x4)**2 + (m.x22 - m.x25)**2 - (m.x43 + m.x46)
    **2 >= 0)
m.e4 = Constraint(expr= (m.x1 - m.x5)**2 + (m.x22 - m.x26)**2 - (m.x43 + m.x47)
    **2 >= 0)
m.e5 = Constraint(expr= (m.x1 - m.x6)**2 + (m.x22 - m.x27)**2 - (m.x43 + m.x48)
    **2 >= 0)
m.e6 = Constraint(expr= (m.x1 - m.x7)**2 + (m.x22 - m.x28)**2 - (m.x43 + m.x49)
    **2 >= 0)
m.e7 = Constraint(expr= (m.x1 - m.x8)**2 + (m.x22 - m.x29)**2 - (m.x43 + m.x50)
    **2 >= 0)
m.e8 = Constraint(expr= (m.x1 - m.x9)**2 + (m.x22 - m.x30)**2 - (m.x43 + m.x51)
    **2 >= 0)
m.e9 = Constraint(expr= (m.x1 - m.x10)**2 + (m.x22 - m.x31)**2 - (m.x43 + m.x52)
    **2 >= 0)
m.e10 = Constraint(expr= (m.x1 - m.x11)**2 + (m.x22 - m.x32)**2 - (m.x43 +
    m.x53)**2 >= 0)
m.e11 = Constraint(expr= (m.x1 - m.x12)**2 + (m.x22 - m.x33)**2 - (m.x43 +
    m.x54)**2 >= 0)
m.e12 = Constraint(expr= (m.x1 - m.x13)**2 + (m.x22 - m.x34)**2 - (m.x43 +
    m.x55)**2 >= 0)
m.e13 = Constraint(expr= (m.x1 - m.x14)**2 + (m.x22 - m.x35)**2 - (m.x43 +
    m.x56)**2 >= 0)
m.e14 = Constraint(expr= (m.x1 - m.x15)**2 + (m.x22 - m.x36)**2 - (m.x43 +
    m.x57)**2 >= 0)
m.e15 = Constraint(expr= (m.x1 - m.x16)**2 + (m.x22 - m.x37)**2 - (m.x43 +
    m.x58)**2 >= 0)
m.e16 = Constraint(expr= (m.x1 - m.x17)**2 + (m.x22 - m.x38)**2 - (m.x43 +
    m.x59)**2 >= 0)
m.e17 = Constraint(expr= (m.x1 - m.x18)**2 + (m.x22 - m.x39)**2 - (m.x43 +
    m.x60)**2 >= 0)
m.e18 = Constraint(expr= (m.x1 - m.x19)**2 + (m.x22 - m.x40)**2 - (m.x43 +
    m.x61)**2 >= 0)
m.e19 = Constraint(expr= (m.x1 - m.x20)**2 + (m.x22 - m.x41)**2 - (m.x43 +
    m.x62)**2 >= 0)
m.e20 = Constraint(expr= (m.x1 - m.x21)**2 + (m.x22 - m.x42)**2 - (m.x43 +
    m.x63)**2 >= 0)
m.e21 = Constraint(expr= (m.x2 - m.x3)**2 + (m.x23 - m.x24)**2 - (m.x44 + m.x45)
    **2 >= 0)
m.e22 = Constraint(expr= (m.x2 - m.x4)**2 + (m.x23 - m.x25)**2 - (m.x44 + m.x46)
    **2 >= 0)
m.e23 = Constraint(expr= (m.x2 - m.x5)**2 + (m.x23 - m.x26)**2 - (m.x44 + m.x47)
    **2 >= 0)
m.e24 = Constraint(expr= (m.x2 - m.x6)**2 + (m.x23 - m.x27)**2 - (m.x44 + m.x48)
    **2 >= 0)
m.e25 = Constraint(expr= (m.x2 - m.x7)**2 + (m.x23 - m.x28)**2 - (m.x44 + m.x49)
    **2 >= 0)
m.e26 = Constraint(expr= (m.x2 - m.x8)**2 + (m.x23 - m.x29)**2 - (m.x44 + m.x50)
    **2 >= 0)
m.e27 = Constraint(expr= (m.x2 - m.x9)**2 + (m.x23 - m.x30)**2 - (m.x44 + m.x51)
    **2 >= 0)
m.e28 = Constraint(expr= (m.x2 - m.x10)**2 + (m.x23 - m.x31)**2 - (m.x44 +
    m.x52)**2 >= 0)
m.e29 = Constraint(expr= (m.x2 - m.x11)**2 + (m.x23 - m.x32)**2 - (m.x44 +
    m.x53)**2 >= 0)
m.e30 = Constraint(expr= (m.x2 - m.x12)**2 + (m.x23 - m.x33)**2 - (m.x44 +
    m.x54)**2 >= 0)
m.e31 = Constraint(expr= (m.x2 - m.x13)**2 + (m.x23 - m.x34)**2 - (m.x44 +
    m.x55)**2 >= 0)
m.e32 = Constraint(expr= (m.x2 - m.x14)**2 + (m.x23 - m.x35)**2 - (m.x44 +
    m.x56)**2 >= 0)
m.e33 = Constraint(expr= (m.x2 - m.x15)**2 + (m.x23 - m.x36)**2 - (m.x44 +
    m.x57)**2 >= 0)
m.e34 = Constraint(expr= (m.x2 - m.x16)**2 + (m.x23 - m.x37)**2 - (m.x44 +
    m.x58)**2 >= 0)
m.e35 = Constraint(expr= (m.x2 - m.x17)**2 + (m.x23 - m.x38)**2 - (m.x44 +
    m.x59)**2 >= 0)
m.e36 = Constraint(expr= (m.x2 - m.x18)**2 + (m.x23 - m.x39)**2 - (m.x44 +
    m.x60)**2 >= 0)
m.e37 = Constraint(expr= (m.x2 - m.x19)**2 + (m.x23 - m.x40)**2 - (m.x44 +
    m.x61)**2 >= 0)
m.e38 = Constraint(expr= (m.x2 - m.x20)**2 + (m.x23 - m.x41)**2 - (m.x44 +
    m.x62)**2 >= 0)
m.e39 = Constraint(expr= (m.x2 - m.x21)**2 + (m.x23 - m.x42)**2 - (m.x44 +
    m.x63)**2 >= 0)
m.e40 = Constraint(expr= (m.x3 - m.x4)**2 + (m.x24 - m.x25)**2 - (m.x45 + m.x46)
    **2 >= 0)
m.e41 = Constraint(expr= (m.x3 - m.x5)**2 + (m.x24 - m.x26)**2 - (m.x45 + m.x47)
    **2 >= 0)
m.e42 = Constraint(expr= (m.x3 - m.x6)**2 + (m.x24 - m.x27)**2 - (m.x45 + m.x48)
    **2 >= 0)
m.e43 = Constraint(expr= (m.x3 - m.x7)**2 + (m.x24 - m.x28)**2 - (m.x45 + m.x49)
    **2 >= 0)
m.e44 = Constraint(expr= (m.x3 - m.x8)**2 + (m.x24 - m.x29)**2 - (m.x45 + m.x50)
    **2 >= 0)
m.e45 = Constraint(expr= (m.x3 - m.x9)**2 + (m.x24 - m.x30)**2 - (m.x45 + m.x51)
    **2 >= 0)
m.e46 = Constraint(expr= (m.x3 - m.x10)**2 + (m.x24 - m.x31)**2 - (m.x45 +
    m.x52)**2 >= 0)
m.e47 = Constraint(expr= (m.x3 - m.x11)**2 + (m.x24 - m.x32)**2 - (m.x45 +
    m.x53)**2 >= 0)
m.e48 = Constraint(expr= (m.x3 - m.x12)**2 + (m.x24 - m.x33)**2 - (m.x45 +
    m.x54)**2 >= 0)
m.e49 = Constraint(expr= (m.x3 - m.x13)**2 + (m.x24 - m.x34)**2 - (m.x45 +
    m.x55)**2 >= 0)
m.e50 = Constraint(expr= (m.x3 - m.x14)**2 + (m.x24 - m.x35)**2 - (m.x45 +
    m.x56)**2 >= 0)
m.e51 = Constraint(expr= (m.x3 - m.x15)**2 + (m.x24 - m.x36)**2 - (m.x45 +
    m.x57)**2 >= 0)
m.e52 = Constraint(expr= (m.x3 - m.x16)**2 + (m.x24 - m.x37)**2 - (m.x45 +
    m.x58)**2 >= 0)
m.e53 = Constraint(expr= (m.x3 - m.x17)**2 + (m.x24 - m.x38)**2 - (m.x45 +
    m.x59)**2 >= 0)
m.e54 = Constraint(expr= (m.x3 - m.x18)**2 + (m.x24 - m.x39)**2 - (m.x45 +
    m.x60)**2 >= 0)
m.e55 = Constraint(expr= (m.x3 - m.x19)**2 + (m.x24 - m.x40)**2 - (m.x45 +
    m.x61)**2 >= 0)
m.e56 = Constraint(expr= (m.x3 - m.x20)**2 + (m.x24 - m.x41)**2 - (m.x45 +
    m.x62)**2 >= 0)
m.e57 = Constraint(expr= (m.x3 - m.x21)**2 + (m.x24 - m.x42)**2 - (m.x45 +
    m.x63)**2 >= 0)
m.e58 = Constraint(expr= (m.x4 - m.x5)**2 + (m.x25 - m.x26)**2 - (m.x46 + m.x47)
    **2 >= 0)
m.e59 = Constraint(expr= (m.x4 - m.x6)**2 + (m.x25 - m.x27)**2 - (m.x46 + m.x48)
    **2 >= 0)
m.e60 = Constraint(expr= (m.x4 - m.x7)**2 + (m.x25 - m.x28)**2 - (m.x46 + m.x49)
    **2 >= 0)
m.e61 = Constraint(expr= (m.x4 - m.x8)**2 + (m.x25 - m.x29)**2 - (m.x46 + m.x50)
    **2 >= 0)
m.e62 = Constraint(expr= (m.x4 - m.x9)**2 + (m.x25 - m.x30)**2 - (m.x46 + m.x51)
    **2 >= 0)
m.e63 = Constraint(expr= (m.x4 - m.x10)**2 + (m.x25 - m.x31)**2 - (m.x46 +
    m.x52)**2 >= 0)
m.e64 = Constraint(expr= (m.x4 - m.x11)**2 + (m.x25 - m.x32)**2 - (m.x46 +
    m.x53)**2 >= 0)
m.e65 = Constraint(expr= (m.x4 - m.x12)**2 + (m.x25 - m.x33)**2 - (m.x46 +
    m.x54)**2 >= 0)
m.e66 = Constraint(expr= (m.x4 - m.x13)**2 + (m.x25 - m.x34)**2 - (m.x46 +
    m.x55)**2 >= 0)
m.e67 = Constraint(expr= (m.x4 - m.x14)**2 + (m.x25 - m.x35)**2 - (m.x46 +
    m.x56)**2 >= 0)
m.e68 = Constraint(expr= (m.x4 - m.x15)**2 + (m.x25 - m.x36)**2 - (m.x46 +
    m.x57)**2 >= 0)
m.e69 = Constraint(expr= (m.x4 - m.x16)**2 + (m.x25 - m.x37)**2 - (m.x46 +
    m.x58)**2 >= 0)
m.e70 = Constraint(expr= (m.x4 - m.x17)**2 + (m.x25 - m.x38)**2 - (m.x46 +
    m.x59)**2 >= 0)
m.e71 = Constraint(expr= (m.x4 - m.x18)**2 + (m.x25 - m.x39)**2 - (m.x46 +
    m.x60)**2 >= 0)
m.e72 = Constraint(expr= (m.x4 - m.x19)**2 + (m.x25 - m.x40)**2 - (m.x46 +
    m.x61)**2 >= 0)
m.e73 = Constraint(expr= (m.x4 - m.x20)**2 + (m.x25 - m.x41)**2 - (m.x46 +
    m.x62)**2 >= 0)
m.e74 = Constraint(expr= (m.x4 - m.x21)**2 + (m.x25 - m.x42)**2 - (m.x46 +
    m.x63)**2 >= 0)
m.e75 = Constraint(expr= (m.x5 - m.x6)**2 + (m.x26 - m.x27)**2 - (m.x47 + m.x48)
    **2 >= 0)
m.e76 = Constraint(expr= (m.x5 - m.x7)**2 + (m.x26 - m.x28)**2 - (m.x47 + m.x49)
    **2 >= 0)
m.e77 = Constraint(expr= (m.x5 - m.x8)**2 + (m.x26 - m.x29)**2 - (m.x47 + m.x50)
    **2 >= 0)
m.e78 = Constraint(expr= (m.x5 - m.x9)**2 + (m.x26 - m.x30)**2 - (m.x47 + m.x51)
    **2 >= 0)
m.e79 = Constraint(expr= (m.x5 - m.x10)**2 + (m.x26 - m.x31)**2 - (m.x47 +
    m.x52)**2 >= 0)
m.e80 = Constraint(expr= (m.x5 - m.x11)**2 + (m.x26 - m.x32)**2 - (m.x47 +
    m.x53)**2 >= 0)
m.e81 = Constraint(expr= (m.x5 - m.x12)**2 + (m.x26 - m.x33)**2 - (m.x47 +
    m.x54)**2 >= 0)
m.e82 = Constraint(expr= (m.x5 - m.x13)**2 + (m.x26 - m.x34)**2 - (m.x47 +
    m.x55)**2 >= 0)
m.e83 = Constraint(expr= (m.x5 - m.x14)**2 + (m.x26 - m.x35)**2 - (m.x47 +
    m.x56)**2 >= 0)
m.e84 = Constraint(expr= (m.x5 - m.x15)**2 + (m.x26 - m.x36)**2 - (m.x47 +
    m.x57)**2 >= 0)
m.e85 = Constraint(expr= (m.x5 - m.x16)**2 + (m.x26 - m.x37)**2 - (m.x47 +
    m.x58)**2 >= 0)
m.e86 = Constraint(expr= (m.x5 - m.x17)**2 + (m.x26 - m.x38)**2 - (m.x47 +
    m.x59)**2 >= 0)
m.e87 = Constraint(expr= (m.x5 - m.x18)**2 + (m.x26 - m.x39)**2 - (m.x47 +
    m.x60)**2 >= 0)
m.e88 = Constraint(expr= (m.x5 - m.x19)**2 + (m.x26 - m.x40)**2 - (m.x47 +
    m.x61)**2 >= 0)
m.e89 = Constraint(expr= (m.x5 - m.x20)**2 + (m.x26 - m.x41)**2 - (m.x47 +
    m.x62)**2 >= 0)
m.e90 = Constraint(expr= (m.x5 - m.x21)**2 + (m.x26 - m.x42)**2 - (m.x47 +
    m.x63)**2 >= 0)
m.e91 = Constraint(expr= (m.x6 - m.x7)**2 + (m.x27 - m.x28)**2 - (m.x48 + m.x49)
    **2 >= 0)
m.e92 = Constraint(expr= (m.x6 - m.x8)**2 + (m.x27 - m.x29)**2 - (m.x48 + m.x50)
    **2 >= 0)
m.e93 = Constraint(expr= (m.x6 - m.x9)**2 + (m.x27 - m.x30)**2 - (m.x48 + m.x51)
    **2 >= 0)
m.e94 = Constraint(expr= (m.x6 - m.x10)**2 + (m.x27 - m.x31)**2 - (m.x48 +
    m.x52)**2 >= 0)
m.e95 = Constraint(expr= (m.x6 - m.x11)**2 + (m.x27 - m.x32)**2 - (m.x48 +
    m.x53)**2 >= 0)
m.e96 = Constraint(expr= (m.x6 - m.x12)**2 + (m.x27 - m.x33)**2 - (m.x48 +
    m.x54)**2 >= 0)
m.e97 = Constraint(expr= (m.x6 - m.x13)**2 + (m.x27 - m.x34)**2 - (m.x48 +
    m.x55)**2 >= 0)
m.e98 = Constraint(expr= (m.x6 - m.x14)**2 + (m.x27 - m.x35)**2 - (m.x48 +
    m.x56)**2 >= 0)
m.e99 = Constraint(expr= (m.x6 - m.x15)**2 + (m.x27 - m.x36)**2 - (m.x48 +
    m.x57)**2 >= 0)
m.e100 = Constraint(expr= (m.x6 - m.x16)**2 + (m.x27 - m.x37)**2 - (m.x48 +
    m.x58)**2 >= 0)
m.e101 = Constraint(expr= (m.x6 - m.x17)**2 + (m.x27 - m.x38)**2 - (m.x48 +
    m.x59)**2 >= 0)
m.e102 = Constraint(expr= (m.x6 - m.x18)**2 + (m.x27 - m.x39)**2 - (m.x48 +
    m.x60)**2 >= 0)
m.e103 = Constraint(expr= (m.x6 - m.x19)**2 + (m.x27 - m.x40)**2 - (m.x48 +
    m.x61)**2 >= 0)
m.e104 = Constraint(expr= (m.x6 - m.x20)**2 + (m.x27 - m.x41)**2 - (m.x48 +
    m.x62)**2 >= 0)
m.e105 = Constraint(expr= (m.x6 - m.x21)**2 + (m.x27 - m.x42)**2 - (m.x48 +
    m.x63)**2 >= 0)
m.e106 = Constraint(expr= (m.x7 - m.x8)**2 + (m.x28 - m.x29)**2 - (m.x49 +
    m.x50)**2 >= 0)
m.e107 = Constraint(expr= (m.x7 - m.x9)**2 + (m.x28 - m.x30)**2 - (m.x49 +
    m.x51)**2 >= 0)
m.e108 = Constraint(expr= (m.x7 - m.x10)**2 + (m.x28 - m.x31)**2 - (m.x49 +
    m.x52)**2 >= 0)
m.e109 = Constraint(expr= (m.x7 - m.x11)**2 + (m.x28 - m.x32)**2 - (m.x49 +
    m.x53)**2 >= 0)
m.e110 = Constraint(expr= (m.x7 - m.x12)**2 + (m.x28 - m.x33)**2 - (m.x49 +
    m.x54)**2 >= 0)
m.e111 = Constraint(expr= (m.x7 - m.x13)**2 + (m.x28 - m.x34)**2 - (m.x49 +
    m.x55)**2 >= 0)
m.e112 = Constraint(expr= (m.x7 - m.x14)**2 + (m.x28 - m.x35)**2 - (m.x49 +
    m.x56)**2 >= 0)
m.e113 = Constraint(expr= (m.x7 - m.x15)**2 + (m.x28 - m.x36)**2 - (m.x49 +
    m.x57)**2 >= 0)
m.e114 = Constraint(expr= (m.x7 - m.x16)**2 + (m.x28 - m.x37)**2 - (m.x49 +
    m.x58)**2 >= 0)
m.e115 = Constraint(expr= (m.x7 - m.x17)**2 + (m.x28 - m.x38)**2 - (m.x49 +
    m.x59)**2 >= 0)
m.e116 = Constraint(expr= (m.x7 - m.x18)**2 + (m.x28 - m.x39)**2 - (m.x49 +
    m.x60)**2 >= 0)
m.e117 = Constraint(expr= (m.x7 - m.x19)**2 + (m.x28 - m.x40)**2 - (m.x49 +
    m.x61)**2 >= 0)
m.e118 = Constraint(expr= (m.x7 - m.x20)**2 + (m.x28 - m.x41)**2 - (m.x49 +
    m.x62)**2 >= 0)
m.e119 = Constraint(expr= (m.x7 - m.x21)**2 + (m.x28 - m.x42)**2 - (m.x49 +
    m.x63)**2 >= 0)
m.e120 = Constraint(expr= (m.x8 - m.x9)**2 + (m.x29 - m.x30)**2 - (m.x50 +
    m.x51)**2 >= 0)
m.e121 = Constraint(expr= (m.x8 - m.x10)**2 + (m.x29 - m.x31)**2 - (m.x50 +
    m.x52)**2 >= 0)
m.e122 = Constraint(expr= (m.x8 - m.x11)**2 + (m.x29 - m.x32)**2 - (m.x50 +
    m.x53)**2 >= 0)
m.e123 = Constraint(expr= (m.x8 - m.x12)**2 + (m.x29 - m.x33)**2 - (m.x50 +
    m.x54)**2 >= 0)
m.e124 = Constraint(expr= (m.x8 - m.x13)**2 + (m.x29 - m.x34)**2 - (m.x50 +
    m.x55)**2 >= 0)
m.e125 = Constraint(expr= (m.x8 - m.x14)**2 + (m.x29 - m.x35)**2 - (m.x50 +
    m.x56)**2 >= 0)
m.e126 = Constraint(expr= (m.x8 - m.x15)**2 + (m.x29 - m.x36)**2 - (m.x50 +
    m.x57)**2 >= 0)
m.e127 = Constraint(expr= (m.x8 - m.x16)**2 + (m.x29 - m.x37)**2 - (m.x50 +
    m.x58)**2 >= 0)
m.e128 = Constraint(expr= (m.x8 - m.x17)**2 + (m.x29 - m.x38)**2 - (m.x50 +
    m.x59)**2 >= 0)
m.e129 = Constraint(expr= (m.x8 - m.x18)**2 + (m.x29 - m.x39)**2 - (m.x50 +
    m.x60)**2 >= 0)
m.e130 = Constraint(expr= (m.x8 - m.x19)**2 + (m.x29 - m.x40)**2 - (m.x50 +
    m.x61)**2 >= 0)
m.e131 = Constraint(expr= (m.x8 - m.x20)**2 + (m.x29 - m.x41)**2 - (m.x50 +
    m.x62)**2 >= 0)
m.e132 = Constraint(expr= (m.x8 - m.x21)**2 + (m.x29 - m.x42)**2 - (m.x50 +
    m.x63)**2 >= 0)
m.e133 = Constraint(expr= (m.x9 - m.x10)**2 + (m.x30 - m.x31)**2 - (m.x51 +
    m.x52)**2 >= 0)
m.e134 = Constraint(expr= (m.x9 - m.x11)**2 + (m.x30 - m.x32)**2 - (m.x51 +
    m.x53)**2 >= 0)
m.e135 = Constraint(expr= (m.x9 - m.x12)**2 + (m.x30 - m.x33)**2 - (m.x51 +
    m.x54)**2 >= 0)
m.e136 = Constraint(expr= (m.x9 - m.x13)**2 + (m.x30 - m.x34)**2 - (m.x51 +
    m.x55)**2 >= 0)
m.e137 = Constraint(expr= (m.x9 - m.x14)**2 + (m.x30 - m.x35)**2 - (m.x51 +
    m.x56)**2 >= 0)
m.e138 = Constraint(expr= (m.x9 - m.x15)**2 + (m.x30 - m.x36)**2 - (m.x51 +
    m.x57)**2 >= 0)
m.e139 = Constraint(expr= (m.x9 - m.x16)**2 + (m.x30 - m.x37)**2 - (m.x51 +
    m.x58)**2 >= 0)
m.e140 = Constraint(expr= (m.x9 - m.x17)**2 + (m.x30 - m.x38)**2 - (m.x51 +
    m.x59)**2 >= 0)
m.e141 = Constraint(expr= (m.x9 - m.x18)**2 + (m.x30 - m.x39)**2 - (m.x51 +
    m.x60)**2 >= 0)
m.e142 = Constraint(expr= (m.x9 - m.x19)**2 + (m.x30 - m.x40)**2 - (m.x51 +
    m.x61)**2 >= 0)
m.e143 = Constraint(expr= (m.x9 - m.x20)**2 + (m.x30 - m.x41)**2 - (m.x51 +
    m.x62)**2 >= 0)
m.e144 = Constraint(expr= (m.x9 - m.x21)**2 + (m.x30 - m.x42)**2 - (m.x51 +
    m.x63)**2 >= 0)
m.e145 = Constraint(expr= (m.x10 - m.x11)**2 + (m.x31 - m.x32)**2 - (m.x52 +
    m.x53)**2 >= 0)
m.e146 = Constraint(expr= (m.x10 - m.x12)**2 + (m.x31 - m.x33)**2 - (m.x52 +
    m.x54)**2 >= 0)
m.e147 = Constraint(expr= (m.x10 - m.x13)**2 + (m.x31 - m.x34)**2 - (m.x52 +
    m.x55)**2 >= 0)
m.e148 = Constraint(expr= (m.x10 - m.x14)**2 + (m.x31 - m.x35)**2 - (m.x52 +
    m.x56)**2 >= 0)
m.e149 = Constraint(expr= (m.x10 - m.x15)**2 + (m.x31 - m.x36)**2 - (m.x52 +
    m.x57)**2 >= 0)
m.e150 = Constraint(expr= (m.x10 - m.x16)**2 + (m.x31 - m.x37)**2 - (m.x52 +
    m.x58)**2 >= 0)
m.e151 = Constraint(expr= (m.x10 - m.x17)**2 + (m.x31 - m.x38)**2 - (m.x52 +
    m.x59)**2 >= 0)
m.e152 = Constraint(expr= (m.x10 - m.x18)**2 + (m.x31 - m.x39)**2 - (m.x52 +
    m.x60)**2 >= 0)
m.e153 = Constraint(expr= (m.x10 - m.x19)**2 + (m.x31 - m.x40)**2 - (m.x52 +
    m.x61)**2 >= 0)
m.e154 = Constraint(expr= (m.x10 - m.x20)**2 + (m.x31 - m.x41)**2 - (m.x52 +
    m.x62)**2 >= 0)
m.e155 = Constraint(expr= (m.x10 - m.x21)**2 + (m.x31 - m.x42)**2 - (m.x52 +
    m.x63)**2 >= 0)
m.e156 = Constraint(expr= (m.x11 - m.x12)**2 + (m.x32 - m.x33)**2 - (m.x53 +
    m.x54)**2 >= 0)
m.e157 = Constraint(expr= (m.x11 - m.x13)**2 + (m.x32 - m.x34)**2 - (m.x53 +
    m.x55)**2 >= 0)
m.e158 = Constraint(expr= (m.x11 - m.x14)**2 + (m.x32 - m.x35)**2 - (m.x53 +
    m.x56)**2 >= 0)
m.e159 = Constraint(expr= (m.x11 - m.x15)**2 + (m.x32 - m.x36)**2 - (m.x53 +
    m.x57)**2 >= 0)
m.e160 = Constraint(expr= (m.x11 - m.x16)**2 + (m.x32 - m.x37)**2 - (m.x53 +
    m.x58)**2 >= 0)
m.e161 = Constraint(expr= (m.x11 - m.x17)**2 + (m.x32 - m.x38)**2 - (m.x53 +
    m.x59)**2 >= 0)
m.e162 = Constraint(expr= (m.x11 - m.x18)**2 + (m.x32 - m.x39)**2 - (m.x53 +
    m.x60)**2 >= 0)
m.e163 = Constraint(expr= (m.x11 - m.x19)**2 + (m.x32 - m.x40)**2 - (m.x53 +
    m.x61)**2 >= 0)
m.e164 = Constraint(expr= (m.x11 - m.x20)**2 + (m.x32 - m.x41)**2 - (m.x53 +
    m.x62)**2 >= 0)
m.e165 = Constraint(expr= (m.x11 - m.x21)**2 + (m.x32 - m.x42)**2 - (m.x53 +
    m.x63)**2 >= 0)
m.e166 = Constraint(expr= (m.x12 - m.x13)**2 + (m.x33 - m.x34)**2 - (m.x54 +
    m.x55)**2 >= 0)
m.e167 = Constraint(expr= (m.x12 - m.x14)**2 + (m.x33 - m.x35)**2 - (m.x54 +
    m.x56)**2 >= 0)
m.e168 = Constraint(expr= (m.x12 - m.x15)**2 + (m.x33 - m.x36)**2 - (m.x54 +
    m.x57)**2 >= 0)
m.e169 = Constraint(expr= (m.x12 - m.x16)**2 + (m.x33 - m.x37)**2 - (m.x54 +
    m.x58)**2 >= 0)
m.e170 = Constraint(expr= (m.x12 - m.x17)**2 + (m.x33 - m.x38)**2 - (m.x54 +
    m.x59)**2 >= 0)
m.e171 = Constraint(expr= (m.x12 - m.x18)**2 + (m.x33 - m.x39)**2 - (m.x54 +
    m.x60)**2 >= 0)
m.e172 = Constraint(expr= (m.x12 - m.x19)**2 + (m.x33 - m.x40)**2 - (m.x54 +
    m.x61)**2 >= 0)
m.e173 = Constraint(expr= (m.x12 - m.x20)**2 + (m.x33 - m.x41)**2 - (m.x54 +
    m.x62)**2 >= 0)
m.e174 = Constraint(expr= (m.x12 - m.x21)**2 + (m.x33 - m.x42)**2 - (m.x54 +
    m.x63)**2 >= 0)
m.e175 = Constraint(expr= (m.x13 - m.x14)**2 + (m.x34 - m.x35)**2 - (m.x55 +
    m.x56)**2 >= 0)
m.e176 = Constraint(expr= (m.x13 - m.x15)**2 + (m.x34 - m.x36)**2 - (m.x55 +
    m.x57)**2 >= 0)
m.e177 = Constraint(expr= (m.x13 - m.x16)**2 + (m.x34 - m.x37)**2 - (m.x55 +
    m.x58)**2 >= 0)
m.e178 = Constraint(expr= (m.x13 - m.x17)**2 + (m.x34 - m.x38)**2 - (m.x55 +
    m.x59)**2 >= 0)
m.e179 = Constraint(expr= (m.x13 - m.x18)**2 + (m.x34 - m.x39)**2 - (m.x55 +
    m.x60)**2 >= 0)
m.e180 = Constraint(expr= (m.x13 - m.x19)**2 + (m.x34 - m.x40)**2 - (m.x55 +
    m.x61)**2 >= 0)
m.e181 = Constraint(expr= (m.x13 - m.x20)**2 + (m.x34 - m.x41)**2 - (m.x55 +
    m.x62)**2 >= 0)
m.e182 = Constraint(expr= (m.x13 - m.x21)**2 + (m.x34 - m.x42)**2 - (m.x55 +
    m.x63)**2 >= 0)
m.e183 = Constraint(expr= (m.x14 - m.x15)**2 + (m.x35 - m.x36)**2 - (m.x56 +
    m.x57)**2 >= 0)
m.e184 = Constraint(expr= (m.x14 - m.x16)**2 + (m.x35 - m.x37)**2 - (m.x56 +
    m.x58)**2 >= 0)
m.e185 = Constraint(expr= (m.x14 - m.x17)**2 + (m.x35 - m.x38)**2 - (m.x56 +
    m.x59)**2 >= 0)
m.e186 = Constraint(expr= (m.x14 - m.x18)**2 + (m.x35 - m.x39)**2 - (m.x56 +
    m.x60)**2 >= 0)
m.e187 = Constraint(expr= (m.x14 - m.x19)**2 + (m.x35 - m.x40)**2 - (m.x56 +
    m.x61)**2 >= 0)
m.e188 = Constraint(expr= (m.x14 - m.x20)**2 + (m.x35 - m.x41)**2 - (m.x56 +
    m.x62)**2 >= 0)
m.e189 = Constraint(expr= (m.x14 - m.x21)**2 + (m.x35 - m.x42)**2 - (m.x56 +
    m.x63)**2 >= 0)
m.e190 = Constraint(expr= (m.x15 - m.x16)**2 + (m.x36 - m.x37)**2 - (m.x57 +
    m.x58)**2 >= 0)
m.e191 = Constraint(expr= (m.x15 - m.x17)**2 + (m.x36 - m.x38)**2 - (m.x57 +
    m.x59)**2 >= 0)
m.e192 = Constraint(expr= (m.x15 - m.x18)**2 + (m.x36 - m.x39)**2 - (m.x57 +
    m.x60)**2 >= 0)
m.e193 = Constraint(expr= (m.x15 - m.x19)**2 + (m.x36 - m.x40)**2 - (m.x57 +
    m.x61)**2 >= 0)
m.e194 = Constraint(expr= (m.x15 - m.x20)**2 + (m.x36 - m.x41)**2 - (m.x57 +
    m.x62)**2 >= 0)
m.e195 = Constraint(expr= (m.x15 - m.x21)**2 + (m.x36 - m.x42)**2 - (m.x57 +
    m.x63)**2 >= 0)
m.e196 = Constraint(expr= (m.x16 - m.x17)**2 + (m.x37 - m.x38)**2 - (m.x58 +
    m.x59)**2 >= 0)
m.e197 = Constraint(expr= (m.x16 - m.x18)**2 + (m.x37 - m.x39)**2 - (m.x58 +
    m.x60)**2 >= 0)
m.e198 = Constraint(expr= (m.x16 - m.x19)**2 + (m.x37 - m.x40)**2 - (m.x58 +
    m.x61)**2 >= 0)
m.e199 = Constraint(expr= (m.x16 - m.x20)**2 + (m.x37 - m.x41)**2 - (m.x58 +
    m.x62)**2 >= 0)
m.e200 = Constraint(expr= (m.x16 - m.x21)**2 + (m.x37 - m.x42)**2 - (m.x58 +
    m.x63)**2 >= 0)
m.e201 = Constraint(expr= (m.x17 - m.x18)**2 + (m.x38 - m.x39)**2 - (m.x59 +
    m.x60)**2 >= 0)
m.e202 = Constraint(expr= (m.x17 - m.x19)**2 + (m.x38 - m.x40)**2 - (m.x59 +
    m.x61)**2 >= 0)
m.e203 = Constraint(expr= (m.x17 - m.x20)**2 + (m.x38 - m.x41)**2 - (m.x59 +
    m.x62)**2 >= 0)
m.e204 = Constraint(expr= (m.x17 - m.x21)**2 + (m.x38 - m.x42)**2 - (m.x59 +
    m.x63)**2 >= 0)
m.e205 = Constraint(expr= (m.x18 - m.x19)**2 + (m.x39 - m.x40)**2 - (m.x60 +
    m.x61)**2 >= 0)
m.e206 = Constraint(expr= (m.x18 - m.x20)**2 + (m.x39 - m.x41)**2 - (m.x60 +
    m.x62)**2 >= 0)
m.e207 = Constraint(expr= (m.x18 - m.x21)**2 + (m.x39 - m.x42)**2 - (m.x60 +
    m.x63)**2 >= 0)
m.e208 = Constraint(expr= (m.x19 - m.x20)**2 + (m.x40 - m.x41)**2 - (m.x61 +
    m.x62)**2 >= 0)
m.e209 = Constraint(expr= (m.x19 - m.x21)**2 + (m.x40 - m.x42)**2 - (m.x61 +
    m.x63)**2 >= 0)
m.e210 = Constraint(expr= (m.x20 - m.x21)**2 + (m.x41 - m.x42)**2 - (m.x62 +
    m.x63)**2 >= 0)
m.e211 = Constraint(expr= m.x43 - m.x64 == 0)
m.e212 = Constraint(expr= m.x44 - m.x64 == 0)
m.e213 = Constraint(expr= m.x45 - m.x64 == 0)
m.e214 = Constraint(expr= m.x46 - m.x64 == 0)
m.e215 = Constraint(expr= m.x47 - m.x64 == 0)
m.e216 = Constraint(expr= m.x48 - m.x64 == 0)
m.e217 = Constraint(expr= m.x49 - m.x64 == 0)
m.e218 = Constraint(expr= m.x50 - m.x64 == 0)
m.e219 = Constraint(expr= m.x51 - m.x64 == 0)
m.e220 = Constraint(expr= m.x52 - m.x64 == 0)
m.e221 = Constraint(expr= m.x53 - m.x64 == 0)
m.e222 = Constraint(expr= m.x54 - m.x64 == 0)
m.e223 = Constraint(expr= m.x55 - m.x64 == 0)
m.e224 = Constraint(expr= m.x56 - m.x64 == 0)
m.e225 = Constraint(expr= m.x57 - m.x64 == 0)
m.e226 = Constraint(expr= m.x58 - m.x64 == 0)
m.e227 = Constraint(expr= m.x59 - m.x64 == 0)
m.e228 = Constraint(expr= m.x60 - m.x64 == 0)
m.e229 = Constraint(expr= m.x61 - m.x64 == 0)
m.e230 = Constraint(expr= m.x62 - m.x64 == 0)
m.e231 = Constraint(expr= m.x63 - m.x64 == 0)
m.e232 = Constraint(expr= m.x1**2 + m.x22**2 - (1 - m.x43)**2 <= 0)
m.e233 = Constraint(expr= m.x2**2 + m.x23**2 - (1 - m.x44)**2 <= 0)
m.e234 = Constraint(expr= m.x3**2 + m.x24**2 - (1 - m.x45)**2 <= 0)
m.e235 = Constraint(expr= m.x4**2 + m.x25**2 - (1 - m.x46)**2 <= 0)
m.e236 = Constraint(expr= m.x5**2 + m.x26**2 - (1 - m.x47)**2 <= 0)
m.e237 = Constraint(expr= m.x6**2 + m.x27**2 - (1 - m.x48)**2 <= 0)
m.e238 = Constraint(expr= m.x7**2 + m.x28**2 - (1 - m.x49)**2 <= 0)
m.e239 = Constraint(expr= m.x8**2 + m.x29**2 - (1 - m.x50)**2 <= 0)
m.e240 = Constraint(expr= m.x9**2 + m.x30**2 - (1 - m.x51)**2 <= 0)
m.e241 = Constraint(expr= m.x10**2 + m.x31**2 - (1 - m.x52)**2 <= 0)
m.e242 = Constraint(expr= m.x11**2 + m.x32**2 - (1 - m.x53)**2 <= 0)
m.e243 = Constraint(expr= m.x12**2 + m.x33**2 - (1 - m.x54)**2 <= 0)
m.e244 = Constraint(expr= m.x13**2 + m.x34**2 - (1 - m.x55)**2 <= 0)
m.e245 = Constraint(expr= m.x14**2 + m.x35**2 - (1 - m.x56)**2 <= 0)
m.e246 = Constraint(expr= m.x15**2 + m.x36**2 - (1 - m.x57)**2 <= 0)
m.e247 = Constraint(expr= m.x16**2 + m.x37**2 - (1 - m.x58)**2 <= 0)
m.e248 = Constraint(expr= m.x17**2 + m.x38**2 - (1 - m.x59)**2 <= 0)
m.e249 = Constraint(expr= m.x18**2 + m.x39**2 - (1 - m.x60)**2 <= 0)
m.e250 = Constraint(expr= m.x19**2 + m.x40**2 - (1 - m.x61)**2 <= 0)
m.e251 = Constraint(expr= m.x20**2 + m.x41**2 - (1 - m.x62)**2 <= 0)
m.e252 = Constraint(expr= m.x21**2 + m.x42**2 - (1 - m.x63)**2 <= 0)