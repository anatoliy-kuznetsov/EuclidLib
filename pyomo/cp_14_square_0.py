# NLP written by GAMS Convert at 05/15/24 11:50:01
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       161       14      119       28        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        43       43        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       686      140      546
#
# Reformulation has removed 1 variable and 1 equation

from pyomo.environ import *

model = m = ConcreteModel()

m.x1 = Var(within=Reals, bounds=(-0.5,0.5), initialize=0)
m.x2 = Var(within=Reals, bounds=(-0.5,0.5), initialize=0)
m.x3 = Var(within=Reals, bounds=(-0.5,0.5), initialize=0)
m.x4 = Var(within=Reals, bounds=(-0.5,0.5), initialize=0)
m.x5 = Var(within=Reals, bounds=(-0.5,0.5), initialize=0)
m.x6 = Var(within=Reals, bounds=(-0.5,0.5), initialize=0)
m.x7 = Var(within=Reals, bounds=(-0.5,0.5), initialize=0)
m.x8 = Var(within=Reals, bounds=(-0.5,0.5), initialize=0)
m.x9 = Var(within=Reals, bounds=(-0.5,0.5), initialize=0)
m.x10 = Var(within=Reals, bounds=(-0.5,0.5), initialize=0)
m.x11 = Var(within=Reals, bounds=(-0.5,0.5), initialize=0)
m.x12 = Var(within=Reals, bounds=(-0.5,0.5), initialize=0)
m.x13 = Var(within=Reals, bounds=(-0.5,0.5), initialize=0)
m.x14 = Var(within=Reals, bounds=(-0.5,0.5), initialize=0)
m.x15 = Var(within=Reals, bounds=(-0.5,0.5), initialize=0)
m.x16 = Var(within=Reals, bounds=(-0.5,0.5), initialize=0)
m.x17 = Var(within=Reals, bounds=(-0.5,0.5), initialize=0)
m.x18 = Var(within=Reals, bounds=(-0.5,0.5), initialize=0)
m.x19 = Var(within=Reals, bounds=(-0.5,0.5), initialize=0)
m.x20 = Var(within=Reals, bounds=(-0.5,0.5), initialize=0)
m.x21 = Var(within=Reals, bounds=(-0.5,0.5), initialize=0)
m.x22 = Var(within=Reals, bounds=(-0.5,0.5), initialize=0)
m.x23 = Var(within=Reals, bounds=(-0.5,0.5), initialize=0)
m.x24 = Var(within=Reals, bounds=(-0.5,0.5), initialize=0)
m.x25 = Var(within=Reals, bounds=(-0.5,0.5), initialize=0)
m.x26 = Var(within=Reals, bounds=(-0.5,0.5), initialize=0)
m.x27 = Var(within=Reals, bounds=(-0.5,0.5), initialize=0)
m.x28 = Var(within=Reals, bounds=(-0.5,0.5), initialize=0)
m.x29 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x30 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x31 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x32 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x33 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x34 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x35 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x36 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x37 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x38 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x39 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x40 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x41 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x42 = Var(within=Reals, bounds=(None,None), initialize=0)
m.x43 = Var(within=Reals, bounds=(None,None), initialize=0)

m.obj = Objective(sense=maximize, expr= m.x43)

m.e1 = Constraint(expr= (m.x1 - m.x2)**2 + (m.x15 - m.x16)**2 - (m.x29 + m.x30)
    **2 >= 0)
m.e2 = Constraint(expr= (m.x1 - m.x3)**2 + (m.x15 - m.x17)**2 - (m.x29 + m.x31)
    **2 >= 0)
m.e3 = Constraint(expr= (m.x1 - m.x4)**2 + (m.x15 - m.x18)**2 - (m.x29 + m.x32)
    **2 >= 0)
m.e4 = Constraint(expr= (m.x1 - m.x5)**2 + (m.x15 - m.x19)**2 - (m.x29 + m.x33)
    **2 >= 0)
m.e5 = Constraint(expr= (m.x1 - m.x6)**2 + (m.x15 - m.x20)**2 - (m.x29 + m.x34)
    **2 >= 0)
m.e6 = Constraint(expr= (m.x1 - m.x7)**2 + (m.x15 - m.x21)**2 - (m.x29 + m.x35)
    **2 >= 0)
m.e7 = Constraint(expr= (m.x1 - m.x8)**2 + (m.x15 - m.x22)**2 - (m.x29 + m.x36)
    **2 >= 0)
m.e8 = Constraint(expr= (m.x1 - m.x9)**2 + (m.x15 - m.x23)**2 - (m.x29 + m.x37)
    **2 >= 0)
m.e9 = Constraint(expr= (m.x1 - m.x10)**2 + (m.x15 - m.x24)**2 - (m.x29 + m.x38)
    **2 >= 0)
m.e10 = Constraint(expr= (m.x1 - m.x11)**2 + (m.x15 - m.x25)**2 - (m.x29 +
    m.x39)**2 >= 0)
m.e11 = Constraint(expr= (m.x1 - m.x12)**2 + (m.x15 - m.x26)**2 - (m.x29 +
    m.x40)**2 >= 0)
m.e12 = Constraint(expr= (m.x1 - m.x13)**2 + (m.x15 - m.x27)**2 - (m.x29 +
    m.x41)**2 >= 0)
m.e13 = Constraint(expr= (m.x1 - m.x14)**2 + (m.x15 - m.x28)**2 - (m.x29 +
    m.x42)**2 >= 0)
m.e14 = Constraint(expr= (m.x2 - m.x3)**2 + (m.x16 - m.x17)**2 - (m.x30 + m.x31)
    **2 >= 0)
m.e15 = Constraint(expr= (m.x2 - m.x4)**2 + (m.x16 - m.x18)**2 - (m.x30 + m.x32)
    **2 >= 0)
m.e16 = Constraint(expr= (m.x2 - m.x5)**2 + (m.x16 - m.x19)**2 - (m.x30 + m.x33)
    **2 >= 0)
m.e17 = Constraint(expr= (m.x2 - m.x6)**2 + (m.x16 - m.x20)**2 - (m.x30 + m.x34)
    **2 >= 0)
m.e18 = Constraint(expr= (m.x2 - m.x7)**2 + (m.x16 - m.x21)**2 - (m.x30 + m.x35)
    **2 >= 0)
m.e19 = Constraint(expr= (m.x2 - m.x8)**2 + (m.x16 - m.x22)**2 - (m.x30 + m.x36)
    **2 >= 0)
m.e20 = Constraint(expr= (m.x2 - m.x9)**2 + (m.x16 - m.x23)**2 - (m.x30 + m.x37)
    **2 >= 0)
m.e21 = Constraint(expr= (m.x2 - m.x10)**2 + (m.x16 - m.x24)**2 - (m.x30 +
    m.x38)**2 >= 0)
m.e22 = Constraint(expr= (m.x2 - m.x11)**2 + (m.x16 - m.x25)**2 - (m.x30 +
    m.x39)**2 >= 0)
m.e23 = Constraint(expr= (m.x2 - m.x12)**2 + (m.x16 - m.x26)**2 - (m.x30 +
    m.x40)**2 >= 0)
m.e24 = Constraint(expr= (m.x2 - m.x13)**2 + (m.x16 - m.x27)**2 - (m.x30 +
    m.x41)**2 >= 0)
m.e25 = Constraint(expr= (m.x2 - m.x14)**2 + (m.x16 - m.x28)**2 - (m.x30 +
    m.x42)**2 >= 0)
m.e26 = Constraint(expr= (m.x3 - m.x4)**2 + (m.x17 - m.x18)**2 - (m.x31 + m.x32)
    **2 >= 0)
m.e27 = Constraint(expr= (m.x3 - m.x5)**2 + (m.x17 - m.x19)**2 - (m.x31 + m.x33)
    **2 >= 0)
m.e28 = Constraint(expr= (m.x3 - m.x6)**2 + (m.x17 - m.x20)**2 - (m.x31 + m.x34)
    **2 >= 0)
m.e29 = Constraint(expr= (m.x3 - m.x7)**2 + (m.x17 - m.x21)**2 - (m.x31 + m.x35)
    **2 >= 0)
m.e30 = Constraint(expr= (m.x3 - m.x8)**2 + (m.x17 - m.x22)**2 - (m.x31 + m.x36)
    **2 >= 0)
m.e31 = Constraint(expr= (m.x3 - m.x9)**2 + (m.x17 - m.x23)**2 - (m.x31 + m.x37)
    **2 >= 0)
m.e32 = Constraint(expr= (m.x3 - m.x10)**2 + (m.x17 - m.x24)**2 - (m.x31 +
    m.x38)**2 >= 0)
m.e33 = Constraint(expr= (m.x3 - m.x11)**2 + (m.x17 - m.x25)**2 - (m.x31 +
    m.x39)**2 >= 0)
m.e34 = Constraint(expr= (m.x3 - m.x12)**2 + (m.x17 - m.x26)**2 - (m.x31 +
    m.x40)**2 >= 0)
m.e35 = Constraint(expr= (m.x3 - m.x13)**2 + (m.x17 - m.x27)**2 - (m.x31 +
    m.x41)**2 >= 0)
m.e36 = Constraint(expr= (m.x3 - m.x14)**2 + (m.x17 - m.x28)**2 - (m.x31 +
    m.x42)**2 >= 0)
m.e37 = Constraint(expr= (m.x4 - m.x5)**2 + (m.x18 - m.x19)**2 - (m.x32 + m.x33)
    **2 >= 0)
m.e38 = Constraint(expr= (m.x4 - m.x6)**2 + (m.x18 - m.x20)**2 - (m.x32 + m.x34)
    **2 >= 0)
m.e39 = Constraint(expr= (m.x4 - m.x7)**2 + (m.x18 - m.x21)**2 - (m.x32 + m.x35)
    **2 >= 0)
m.e40 = Constraint(expr= (m.x4 - m.x8)**2 + (m.x18 - m.x22)**2 - (m.x32 + m.x36)
    **2 >= 0)
m.e41 = Constraint(expr= (m.x4 - m.x9)**2 + (m.x18 - m.x23)**2 - (m.x32 + m.x37)
    **2 >= 0)
m.e42 = Constraint(expr= (m.x4 - m.x10)**2 + (m.x18 - m.x24)**2 - (m.x32 +
    m.x38)**2 >= 0)
m.e43 = Constraint(expr= (m.x4 - m.x11)**2 + (m.x18 - m.x25)**2 - (m.x32 +
    m.x39)**2 >= 0)
m.e44 = Constraint(expr= (m.x4 - m.x12)**2 + (m.x18 - m.x26)**2 - (m.x32 +
    m.x40)**2 >= 0)
m.e45 = Constraint(expr= (m.x4 - m.x13)**2 + (m.x18 - m.x27)**2 - (m.x32 +
    m.x41)**2 >= 0)
m.e46 = Constraint(expr= (m.x4 - m.x14)**2 + (m.x18 - m.x28)**2 - (m.x32 +
    m.x42)**2 >= 0)
m.e47 = Constraint(expr= (m.x5 - m.x6)**2 + (m.x19 - m.x20)**2 - (m.x33 + m.x34)
    **2 >= 0)
m.e48 = Constraint(expr= (m.x5 - m.x7)**2 + (m.x19 - m.x21)**2 - (m.x33 + m.x35)
    **2 >= 0)
m.e49 = Constraint(expr= (m.x5 - m.x8)**2 + (m.x19 - m.x22)**2 - (m.x33 + m.x36)
    **2 >= 0)
m.e50 = Constraint(expr= (m.x5 - m.x9)**2 + (m.x19 - m.x23)**2 - (m.x33 + m.x37)
    **2 >= 0)
m.e51 = Constraint(expr= (m.x5 - m.x10)**2 + (m.x19 - m.x24)**2 - (m.x33 +
    m.x38)**2 >= 0)
m.e52 = Constraint(expr= (m.x5 - m.x11)**2 + (m.x19 - m.x25)**2 - (m.x33 +
    m.x39)**2 >= 0)
m.e53 = Constraint(expr= (m.x5 - m.x12)**2 + (m.x19 - m.x26)**2 - (m.x33 +
    m.x40)**2 >= 0)
m.e54 = Constraint(expr= (m.x5 - m.x13)**2 + (m.x19 - m.x27)**2 - (m.x33 +
    m.x41)**2 >= 0)
m.e55 = Constraint(expr= (m.x5 - m.x14)**2 + (m.x19 - m.x28)**2 - (m.x33 +
    m.x42)**2 >= 0)
m.e56 = Constraint(expr= (m.x6 - m.x7)**2 + (m.x20 - m.x21)**2 - (m.x34 + m.x35)
    **2 >= 0)
m.e57 = Constraint(expr= (m.x6 - m.x8)**2 + (m.x20 - m.x22)**2 - (m.x34 + m.x36)
    **2 >= 0)
m.e58 = Constraint(expr= (m.x6 - m.x9)**2 + (m.x20 - m.x23)**2 - (m.x34 + m.x37)
    **2 >= 0)
m.e59 = Constraint(expr= (m.x6 - m.x10)**2 + (m.x20 - m.x24)**2 - (m.x34 +
    m.x38)**2 >= 0)
m.e60 = Constraint(expr= (m.x6 - m.x11)**2 + (m.x20 - m.x25)**2 - (m.x34 +
    m.x39)**2 >= 0)
m.e61 = Constraint(expr= (m.x6 - m.x12)**2 + (m.x20 - m.x26)**2 - (m.x34 +
    m.x40)**2 >= 0)
m.e62 = Constraint(expr= (m.x6 - m.x13)**2 + (m.x20 - m.x27)**2 - (m.x34 +
    m.x41)**2 >= 0)
m.e63 = Constraint(expr= (m.x6 - m.x14)**2 + (m.x20 - m.x28)**2 - (m.x34 +
    m.x42)**2 >= 0)
m.e64 = Constraint(expr= (m.x7 - m.x8)**2 + (m.x21 - m.x22)**2 - (m.x35 + m.x36)
    **2 >= 0)
m.e65 = Constraint(expr= (m.x7 - m.x9)**2 + (m.x21 - m.x23)**2 - (m.x35 + m.x37)
    **2 >= 0)
m.e66 = Constraint(expr= (m.x7 - m.x10)**2 + (m.x21 - m.x24)**2 - (m.x35 +
    m.x38)**2 >= 0)
m.e67 = Constraint(expr= (m.x7 - m.x11)**2 + (m.x21 - m.x25)**2 - (m.x35 +
    m.x39)**2 >= 0)
m.e68 = Constraint(expr= (m.x7 - m.x12)**2 + (m.x21 - m.x26)**2 - (m.x35 +
    m.x40)**2 >= 0)
m.e69 = Constraint(expr= (m.x7 - m.x13)**2 + (m.x21 - m.x27)**2 - (m.x35 +
    m.x41)**2 >= 0)
m.e70 = Constraint(expr= (m.x7 - m.x14)**2 + (m.x21 - m.x28)**2 - (m.x35 +
    m.x42)**2 >= 0)
m.e71 = Constraint(expr= (m.x8 - m.x9)**2 + (m.x22 - m.x23)**2 - (m.x36 + m.x37)
    **2 >= 0)
m.e72 = Constraint(expr= (m.x8 - m.x10)**2 + (m.x22 - m.x24)**2 - (m.x36 +
    m.x38)**2 >= 0)
m.e73 = Constraint(expr= (m.x8 - m.x11)**2 + (m.x22 - m.x25)**2 - (m.x36 +
    m.x39)**2 >= 0)
m.e74 = Constraint(expr= (m.x8 - m.x12)**2 + (m.x22 - m.x26)**2 - (m.x36 +
    m.x40)**2 >= 0)
m.e75 = Constraint(expr= (m.x8 - m.x13)**2 + (m.x22 - m.x27)**2 - (m.x36 +
    m.x41)**2 >= 0)
m.e76 = Constraint(expr= (m.x8 - m.x14)**2 + (m.x22 - m.x28)**2 - (m.x36 +
    m.x42)**2 >= 0)
m.e77 = Constraint(expr= (m.x9 - m.x10)**2 + (m.x23 - m.x24)**2 - (m.x37 +
    m.x38)**2 >= 0)
m.e78 = Constraint(expr= (m.x9 - m.x11)**2 + (m.x23 - m.x25)**2 - (m.x37 +
    m.x39)**2 >= 0)
m.e79 = Constraint(expr= (m.x9 - m.x12)**2 + (m.x23 - m.x26)**2 - (m.x37 +
    m.x40)**2 >= 0)
m.e80 = Constraint(expr= (m.x9 - m.x13)**2 + (m.x23 - m.x27)**2 - (m.x37 +
    m.x41)**2 >= 0)
m.e81 = Constraint(expr= (m.x9 - m.x14)**2 + (m.x23 - m.x28)**2 - (m.x37 +
    m.x42)**2 >= 0)
m.e82 = Constraint(expr= (m.x10 - m.x11)**2 + (m.x24 - m.x25)**2 - (m.x38 +
    m.x39)**2 >= 0)
m.e83 = Constraint(expr= (m.x10 - m.x12)**2 + (m.x24 - m.x26)**2 - (m.x38 +
    m.x40)**2 >= 0)
m.e84 = Constraint(expr= (m.x10 - m.x13)**2 + (m.x24 - m.x27)**2 - (m.x38 +
    m.x41)**2 >= 0)
m.e85 = Constraint(expr= (m.x10 - m.x14)**2 + (m.x24 - m.x28)**2 - (m.x38 +
    m.x42)**2 >= 0)
m.e86 = Constraint(expr= (m.x11 - m.x12)**2 + (m.x25 - m.x26)**2 - (m.x39 +
    m.x40)**2 >= 0)
m.e87 = Constraint(expr= (m.x11 - m.x13)**2 + (m.x25 - m.x27)**2 - (m.x39 +
    m.x41)**2 >= 0)
m.e88 = Constraint(expr= (m.x11 - m.x14)**2 + (m.x25 - m.x28)**2 - (m.x39 +
    m.x42)**2 >= 0)
m.e89 = Constraint(expr= (m.x12 - m.x13)**2 + (m.x26 - m.x27)**2 - (m.x40 +
    m.x41)**2 >= 0)
m.e90 = Constraint(expr= (m.x12 - m.x14)**2 + (m.x26 - m.x28)**2 - (m.x40 +
    m.x42)**2 >= 0)
m.e91 = Constraint(expr= (m.x13 - m.x14)**2 + (m.x27 - m.x28)**2 - (m.x41 +
    m.x42)**2 >= 0)
m.e92 = Constraint(expr= m.x29 - m.x43 == 0)
m.e93 = Constraint(expr= m.x30 - m.x43 == 0)
m.e94 = Constraint(expr= m.x31 - m.x43 == 0)
m.e95 = Constraint(expr= m.x32 - m.x43 == 0)
m.e96 = Constraint(expr= m.x33 - m.x43 == 0)
m.e97 = Constraint(expr= m.x34 - m.x43 == 0)
m.e98 = Constraint(expr= m.x35 - m.x43 == 0)
m.e99 = Constraint(expr= m.x36 - m.x43 == 0)
m.e100 = Constraint(expr= m.x37 - m.x43 == 0)
m.e101 = Constraint(expr= m.x38 - m.x43 == 0)
m.e102 = Constraint(expr= m.x39 - m.x43 == 0)
m.e103 = Constraint(expr= m.x40 - m.x43 == 0)
m.e104 = Constraint(expr= m.x41 - m.x43 == 0)
m.e105 = Constraint(expr= m.x42 - m.x43 == 0)
m.e106 = Constraint(expr= m.x1 + m.x29 <= 0.5)
m.e107 = Constraint(expr= m.x2 + m.x30 <= 0.5)
m.e108 = Constraint(expr= m.x3 + m.x31 <= 0.5)
m.e109 = Constraint(expr= m.x4 + m.x32 <= 0.5)
m.e110 = Constraint(expr= m.x5 + m.x33 <= 0.5)
m.e111 = Constraint(expr= m.x6 + m.x34 <= 0.5)
m.e112 = Constraint(expr= m.x7 + m.x35 <= 0.5)
m.e113 = Constraint(expr= m.x8 + m.x36 <= 0.5)
m.e114 = Constraint(expr= m.x9 + m.x37 <= 0.5)
m.e115 = Constraint(expr= m.x10 + m.x38 <= 0.5)
m.e116 = Constraint(expr= m.x11 + m.x39 <= 0.5)
m.e117 = Constraint(expr= m.x12 + m.x40 <= 0.5)
m.e118 = Constraint(expr= m.x13 + m.x41 <= 0.5)
m.e119 = Constraint(expr= m.x14 + m.x42 <= 0.5)
m.e120 = Constraint(expr= m.x1 - m.x29 >= -0.5)
m.e121 = Constraint(expr= m.x2 - m.x30 >= -0.5)
m.e122 = Constraint(expr= m.x3 - m.x31 >= -0.5)
m.e123 = Constraint(expr= m.x4 - m.x32 >= -0.5)
m.e124 = Constraint(expr= m.x5 - m.x33 >= -0.5)
m.e125 = Constraint(expr= m.x6 - m.x34 >= -0.5)
m.e126 = Constraint(expr= m.x7 - m.x35 >= -0.5)
m.e127 = Constraint(expr= m.x8 - m.x36 >= -0.5)
m.e128 = Constraint(expr= m.x9 - m.x37 >= -0.5)
m.e129 = Constraint(expr= m.x10 - m.x38 >= -0.5)
m.e130 = Constraint(expr= m.x11 - m.x39 >= -0.5)
m.e131 = Constraint(expr= m.x12 - m.x40 >= -0.5)
m.e132 = Constraint(expr= m.x13 - m.x41 >= -0.5)
m.e133 = Constraint(expr= m.x14 - m.x42 >= -0.5)
m.e134 = Constraint(expr= m.x15 + m.x29 <= 0.5)
m.e135 = Constraint(expr= m.x16 + m.x30 <= 0.5)
m.e136 = Constraint(expr= m.x17 + m.x31 <= 0.5)
m.e137 = Constraint(expr= m.x18 + m.x32 <= 0.5)
m.e138 = Constraint(expr= m.x19 + m.x33 <= 0.5)
m.e139 = Constraint(expr= m.x20 + m.x34 <= 0.5)
m.e140 = Constraint(expr= m.x21 + m.x35 <= 0.5)
m.e141 = Constraint(expr= m.x22 + m.x36 <= 0.5)
m.e142 = Constraint(expr= m.x23 + m.x37 <= 0.5)
m.e143 = Constraint(expr= m.x24 + m.x38 <= 0.5)
m.e144 = Constraint(expr= m.x25 + m.x39 <= 0.5)
m.e145 = Constraint(expr= m.x26 + m.x40 <= 0.5)
m.e146 = Constraint(expr= m.x27 + m.x41 <= 0.5)
m.e147 = Constraint(expr= m.x28 + m.x42 <= 0.5)
m.e148 = Constraint(expr= m.x15 - m.x29 >= -0.5)
m.e149 = Constraint(expr= m.x16 - m.x30 >= -0.5)
m.e150 = Constraint(expr= m.x17 - m.x31 >= -0.5)
m.e151 = Constraint(expr= m.x18 - m.x32 >= -0.5)
m.e152 = Constraint(expr= m.x19 - m.x33 >= -0.5)
m.e153 = Constraint(expr= m.x20 - m.x34 >= -0.5)
m.e154 = Constraint(expr= m.x21 - m.x35 >= -0.5)
m.e155 = Constraint(expr= m.x22 - m.x36 >= -0.5)
m.e156 = Constraint(expr= m.x23 - m.x37 >= -0.5)
m.e157 = Constraint(expr= m.x24 - m.x38 >= -0.5)
m.e158 = Constraint(expr= m.x25 - m.x39 >= -0.5)
m.e159 = Constraint(expr= m.x26 - m.x40 >= -0.5)
m.e160 = Constraint(expr= m.x27 - m.x41 >= -0.5)
m.e161 = Constraint(expr= m.x28 - m.x42 >= -0.5)