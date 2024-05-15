# NLP written by GAMS Convert at 05/15/24 11:38:00
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       378       27        0      351        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        82       82        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#      2538      351     2187
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
m.x59 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x60 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x61 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x62 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x63 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x64 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x65 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x66 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x67 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x68 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x69 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x70 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x71 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x72 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x73 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x74 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x75 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x76 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x77 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x78 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x79 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x80 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x81 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x82 = Var(within=Reals, bounds=(None,None), initialize=0)

m.obj = Objective(sense=maximize, expr= m.x82)

m.e1 = Constraint(expr= m.x1**2 + m.x28**2 + m.x55**2 == 1)
m.e2 = Constraint(expr= m.x2**2 + m.x29**2 + m.x56**2 == 1)
m.e3 = Constraint(expr= m.x3**2 + m.x30**2 + m.x57**2 == 1)
m.e4 = Constraint(expr= m.x4**2 + m.x31**2 + m.x58**2 == 1)
m.e5 = Constraint(expr= m.x5**2 + m.x32**2 + m.x59**2 == 1)
m.e6 = Constraint(expr= m.x6**2 + m.x33**2 + m.x60**2 == 1)
m.e7 = Constraint(expr= m.x7**2 + m.x34**2 + m.x61**2 == 1)
m.e8 = Constraint(expr= m.x8**2 + m.x35**2 + m.x62**2 == 1)
m.e9 = Constraint(expr= m.x9**2 + m.x36**2 + m.x63**2 == 1)
m.e10 = Constraint(expr= m.x10**2 + m.x37**2 + m.x64**2 == 1)
m.e11 = Constraint(expr= m.x11**2 + m.x38**2 + m.x65**2 == 1)
m.e12 = Constraint(expr= m.x12**2 + m.x39**2 + m.x66**2 == 1)
m.e13 = Constraint(expr= m.x13**2 + m.x40**2 + m.x67**2 == 1)
m.e14 = Constraint(expr= m.x14**2 + m.x41**2 + m.x68**2 == 1)
m.e15 = Constraint(expr= m.x15**2 + m.x42**2 + m.x69**2 == 1)
m.e16 = Constraint(expr= m.x16**2 + m.x43**2 + m.x70**2 == 1)
m.e17 = Constraint(expr= m.x17**2 + m.x44**2 + m.x71**2 == 1)
m.e18 = Constraint(expr= m.x18**2 + m.x45**2 + m.x72**2 == 1)
m.e19 = Constraint(expr= m.x19**2 + m.x46**2 + m.x73**2 == 1)
m.e20 = Constraint(expr= m.x20**2 + m.x47**2 + m.x74**2 == 1)
m.e21 = Constraint(expr= m.x21**2 + m.x48**2 + m.x75**2 == 1)
m.e22 = Constraint(expr= m.x22**2 + m.x49**2 + m.x76**2 == 1)
m.e23 = Constraint(expr= m.x23**2 + m.x50**2 + m.x77**2 == 1)
m.e24 = Constraint(expr= m.x24**2 + m.x51**2 + m.x78**2 == 1)
m.e25 = Constraint(expr= m.x25**2 + m.x52**2 + m.x79**2 == 1)
m.e26 = Constraint(expr= m.x26**2 + m.x53**2 + m.x80**2 == 1)
m.e27 = Constraint(expr= m.x27**2 + m.x54**2 + m.x81**2 == 1)
m.e28 = Constraint(expr= -sqrt((m.x1 - m.x2)**2 + (m.x28 - m.x29)**2 + (m.x55
    - m.x56)**2) + m.x82 <= 0)
m.e29 = Constraint(expr= -sqrt((m.x1 - m.x3)**2 + (m.x28 - m.x30)**2 + (m.x55
    - m.x57)**2) + m.x82 <= 0)
m.e30 = Constraint(expr= -sqrt((m.x1 - m.x4)**2 + (m.x28 - m.x31)**2 + (m.x55
    - m.x58)**2) + m.x82 <= 0)
m.e31 = Constraint(expr= -sqrt((m.x1 - m.x5)**2 + (m.x28 - m.x32)**2 + (m.x55
    - m.x59)**2) + m.x82 <= 0)
m.e32 = Constraint(expr= -sqrt((m.x1 - m.x6)**2 + (m.x28 - m.x33)**2 + (m.x55
    - m.x60)**2) + m.x82 <= 0)
m.e33 = Constraint(expr= -sqrt((m.x1 - m.x7)**2 + (m.x28 - m.x34)**2 + (m.x55
    - m.x61)**2) + m.x82 <= 0)
m.e34 = Constraint(expr= -sqrt((m.x1 - m.x8)**2 + (m.x28 - m.x35)**2 + (m.x55
    - m.x62)**2) + m.x82 <= 0)
m.e35 = Constraint(expr= -sqrt((m.x1 - m.x9)**2 + (m.x28 - m.x36)**2 + (m.x55
    - m.x63)**2) + m.x82 <= 0)
m.e36 = Constraint(expr= -sqrt((m.x1 - m.x10)**2 + (m.x28 - m.x37)**2 + (m.x55
    - m.x64)**2) + m.x82 <= 0)
m.e37 = Constraint(expr= -sqrt((m.x1 - m.x11)**2 + (m.x28 - m.x38)**2 + (m.x55
    - m.x65)**2) + m.x82 <= 0)
m.e38 = Constraint(expr= -sqrt((m.x1 - m.x12)**2 + (m.x28 - m.x39)**2 + (m.x55
    - m.x66)**2) + m.x82 <= 0)
m.e39 = Constraint(expr= -sqrt((m.x1 - m.x13)**2 + (m.x28 - m.x40)**2 + (m.x55
    - m.x67)**2) + m.x82 <= 0)
m.e40 = Constraint(expr= -sqrt((m.x1 - m.x14)**2 + (m.x28 - m.x41)**2 + (m.x55
    - m.x68)**2) + m.x82 <= 0)
m.e41 = Constraint(expr= -sqrt((m.x1 - m.x15)**2 + (m.x28 - m.x42)**2 + (m.x55
    - m.x69)**2) + m.x82 <= 0)
m.e42 = Constraint(expr= -sqrt((m.x1 - m.x16)**2 + (m.x28 - m.x43)**2 + (m.x55
    - m.x70)**2) + m.x82 <= 0)
m.e43 = Constraint(expr= -sqrt((m.x1 - m.x17)**2 + (m.x28 - m.x44)**2 + (m.x55
    - m.x71)**2) + m.x82 <= 0)
m.e44 = Constraint(expr= -sqrt((m.x1 - m.x18)**2 + (m.x28 - m.x45)**2 + (m.x55
    - m.x72)**2) + m.x82 <= 0)
m.e45 = Constraint(expr= -sqrt((m.x1 - m.x19)**2 + (m.x28 - m.x46)**2 + (m.x55
    - m.x73)**2) + m.x82 <= 0)
m.e46 = Constraint(expr= -sqrt((m.x1 - m.x20)**2 + (m.x28 - m.x47)**2 + (m.x55
    - m.x74)**2) + m.x82 <= 0)
m.e47 = Constraint(expr= -sqrt((m.x1 - m.x21)**2 + (m.x28 - m.x48)**2 + (m.x55
    - m.x75)**2) + m.x82 <= 0)
m.e48 = Constraint(expr= -sqrt((m.x1 - m.x22)**2 + (m.x28 - m.x49)**2 + (m.x55
    - m.x76)**2) + m.x82 <= 0)
m.e49 = Constraint(expr= -sqrt((m.x1 - m.x23)**2 + (m.x28 - m.x50)**2 + (m.x55
    - m.x77)**2) + m.x82 <= 0)
m.e50 = Constraint(expr= -sqrt((m.x1 - m.x24)**2 + (m.x28 - m.x51)**2 + (m.x55
    - m.x78)**2) + m.x82 <= 0)
m.e51 = Constraint(expr= -sqrt((m.x1 - m.x25)**2 + (m.x28 - m.x52)**2 + (m.x55
    - m.x79)**2) + m.x82 <= 0)
m.e52 = Constraint(expr= -sqrt((m.x1 - m.x26)**2 + (m.x28 - m.x53)**2 + (m.x55
    - m.x80)**2) + m.x82 <= 0)
m.e53 = Constraint(expr= -sqrt((m.x1 - m.x27)**2 + (m.x28 - m.x54)**2 + (m.x55
    - m.x81)**2) + m.x82 <= 0)
m.e54 = Constraint(expr= -sqrt((m.x2 - m.x3)**2 + (m.x29 - m.x30)**2 + (m.x56
    - m.x57)**2) + m.x82 <= 0)
m.e55 = Constraint(expr= -sqrt((m.x2 - m.x4)**2 + (m.x29 - m.x31)**2 + (m.x56
    - m.x58)**2) + m.x82 <= 0)
m.e56 = Constraint(expr= -sqrt((m.x2 - m.x5)**2 + (m.x29 - m.x32)**2 + (m.x56
    - m.x59)**2) + m.x82 <= 0)
m.e57 = Constraint(expr= -sqrt((m.x2 - m.x6)**2 + (m.x29 - m.x33)**2 + (m.x56
    - m.x60)**2) + m.x82 <= 0)
m.e58 = Constraint(expr= -sqrt((m.x2 - m.x7)**2 + (m.x29 - m.x34)**2 + (m.x56
    - m.x61)**2) + m.x82 <= 0)
m.e59 = Constraint(expr= -sqrt((m.x2 - m.x8)**2 + (m.x29 - m.x35)**2 + (m.x56
    - m.x62)**2) + m.x82 <= 0)
m.e60 = Constraint(expr= -sqrt((m.x2 - m.x9)**2 + (m.x29 - m.x36)**2 + (m.x56
    - m.x63)**2) + m.x82 <= 0)
m.e61 = Constraint(expr= -sqrt((m.x2 - m.x10)**2 + (m.x29 - m.x37)**2 + (m.x56
    - m.x64)**2) + m.x82 <= 0)
m.e62 = Constraint(expr= -sqrt((m.x2 - m.x11)**2 + (m.x29 - m.x38)**2 + (m.x56
    - m.x65)**2) + m.x82 <= 0)
m.e63 = Constraint(expr= -sqrt((m.x2 - m.x12)**2 + (m.x29 - m.x39)**2 + (m.x56
    - m.x66)**2) + m.x82 <= 0)
m.e64 = Constraint(expr= -sqrt((m.x2 - m.x13)**2 + (m.x29 - m.x40)**2 + (m.x56
    - m.x67)**2) + m.x82 <= 0)
m.e65 = Constraint(expr= -sqrt((m.x2 - m.x14)**2 + (m.x29 - m.x41)**2 + (m.x56
    - m.x68)**2) + m.x82 <= 0)
m.e66 = Constraint(expr= -sqrt((m.x2 - m.x15)**2 + (m.x29 - m.x42)**2 + (m.x56
    - m.x69)**2) + m.x82 <= 0)
m.e67 = Constraint(expr= -sqrt((m.x2 - m.x16)**2 + (m.x29 - m.x43)**2 + (m.x56
    - m.x70)**2) + m.x82 <= 0)
m.e68 = Constraint(expr= -sqrt((m.x2 - m.x17)**2 + (m.x29 - m.x44)**2 + (m.x56
    - m.x71)**2) + m.x82 <= 0)
m.e69 = Constraint(expr= -sqrt((m.x2 - m.x18)**2 + (m.x29 - m.x45)**2 + (m.x56
    - m.x72)**2) + m.x82 <= 0)
m.e70 = Constraint(expr= -sqrt((m.x2 - m.x19)**2 + (m.x29 - m.x46)**2 + (m.x56
    - m.x73)**2) + m.x82 <= 0)
m.e71 = Constraint(expr= -sqrt((m.x2 - m.x20)**2 + (m.x29 - m.x47)**2 + (m.x56
    - m.x74)**2) + m.x82 <= 0)
m.e72 = Constraint(expr= -sqrt((m.x2 - m.x21)**2 + (m.x29 - m.x48)**2 + (m.x56
    - m.x75)**2) + m.x82 <= 0)
m.e73 = Constraint(expr= -sqrt((m.x2 - m.x22)**2 + (m.x29 - m.x49)**2 + (m.x56
    - m.x76)**2) + m.x82 <= 0)
m.e74 = Constraint(expr= -sqrt((m.x2 - m.x23)**2 + (m.x29 - m.x50)**2 + (m.x56
    - m.x77)**2) + m.x82 <= 0)
m.e75 = Constraint(expr= -sqrt((m.x2 - m.x24)**2 + (m.x29 - m.x51)**2 + (m.x56
    - m.x78)**2) + m.x82 <= 0)
m.e76 = Constraint(expr= -sqrt((m.x2 - m.x25)**2 + (m.x29 - m.x52)**2 + (m.x56
    - m.x79)**2) + m.x82 <= 0)
m.e77 = Constraint(expr= -sqrt((m.x2 - m.x26)**2 + (m.x29 - m.x53)**2 + (m.x56
    - m.x80)**2) + m.x82 <= 0)
m.e78 = Constraint(expr= -sqrt((m.x2 - m.x27)**2 + (m.x29 - m.x54)**2 + (m.x56
    - m.x81)**2) + m.x82 <= 0)
m.e79 = Constraint(expr= -sqrt((m.x3 - m.x4)**2 + (m.x30 - m.x31)**2 + (m.x57
    - m.x58)**2) + m.x82 <= 0)
m.e80 = Constraint(expr= -sqrt((m.x3 - m.x5)**2 + (m.x30 - m.x32)**2 + (m.x57
    - m.x59)**2) + m.x82 <= 0)
m.e81 = Constraint(expr= -sqrt((m.x3 - m.x6)**2 + (m.x30 - m.x33)**2 + (m.x57
    - m.x60)**2) + m.x82 <= 0)
m.e82 = Constraint(expr= -sqrt((m.x3 - m.x7)**2 + (m.x30 - m.x34)**2 + (m.x57
    - m.x61)**2) + m.x82 <= 0)
m.e83 = Constraint(expr= -sqrt((m.x3 - m.x8)**2 + (m.x30 - m.x35)**2 + (m.x57
    - m.x62)**2) + m.x82 <= 0)
m.e84 = Constraint(expr= -sqrt((m.x3 - m.x9)**2 + (m.x30 - m.x36)**2 + (m.x57
    - m.x63)**2) + m.x82 <= 0)
m.e85 = Constraint(expr= -sqrt((m.x3 - m.x10)**2 + (m.x30 - m.x37)**2 + (m.x57
    - m.x64)**2) + m.x82 <= 0)
m.e86 = Constraint(expr= -sqrt((m.x3 - m.x11)**2 + (m.x30 - m.x38)**2 + (m.x57
    - m.x65)**2) + m.x82 <= 0)
m.e87 = Constraint(expr= -sqrt((m.x3 - m.x12)**2 + (m.x30 - m.x39)**2 + (m.x57
    - m.x66)**2) + m.x82 <= 0)
m.e88 = Constraint(expr= -sqrt((m.x3 - m.x13)**2 + (m.x30 - m.x40)**2 + (m.x57
    - m.x67)**2) + m.x82 <= 0)
m.e89 = Constraint(expr= -sqrt((m.x3 - m.x14)**2 + (m.x30 - m.x41)**2 + (m.x57
    - m.x68)**2) + m.x82 <= 0)
m.e90 = Constraint(expr= -sqrt((m.x3 - m.x15)**2 + (m.x30 - m.x42)**2 + (m.x57
    - m.x69)**2) + m.x82 <= 0)
m.e91 = Constraint(expr= -sqrt((m.x3 - m.x16)**2 + (m.x30 - m.x43)**2 + (m.x57
    - m.x70)**2) + m.x82 <= 0)
m.e92 = Constraint(expr= -sqrt((m.x3 - m.x17)**2 + (m.x30 - m.x44)**2 + (m.x57
    - m.x71)**2) + m.x82 <= 0)
m.e93 = Constraint(expr= -sqrt((m.x3 - m.x18)**2 + (m.x30 - m.x45)**2 + (m.x57
    - m.x72)**2) + m.x82 <= 0)
m.e94 = Constraint(expr= -sqrt((m.x3 - m.x19)**2 + (m.x30 - m.x46)**2 + (m.x57
    - m.x73)**2) + m.x82 <= 0)
m.e95 = Constraint(expr= -sqrt((m.x3 - m.x20)**2 + (m.x30 - m.x47)**2 + (m.x57
    - m.x74)**2) + m.x82 <= 0)
m.e96 = Constraint(expr= -sqrt((m.x3 - m.x21)**2 + (m.x30 - m.x48)**2 + (m.x57
    - m.x75)**2) + m.x82 <= 0)
m.e97 = Constraint(expr= -sqrt((m.x3 - m.x22)**2 + (m.x30 - m.x49)**2 + (m.x57
    - m.x76)**2) + m.x82 <= 0)
m.e98 = Constraint(expr= -sqrt((m.x3 - m.x23)**2 + (m.x30 - m.x50)**2 + (m.x57
    - m.x77)**2) + m.x82 <= 0)
m.e99 = Constraint(expr= -sqrt((m.x3 - m.x24)**2 + (m.x30 - m.x51)**2 + (m.x57
    - m.x78)**2) + m.x82 <= 0)
m.e100 = Constraint(expr= -sqrt((m.x3 - m.x25)**2 + (m.x30 - m.x52)**2 + (m.x57
    - m.x79)**2) + m.x82 <= 0)
m.e101 = Constraint(expr= -sqrt((m.x3 - m.x26)**2 + (m.x30 - m.x53)**2 + (m.x57
    - m.x80)**2) + m.x82 <= 0)
m.e102 = Constraint(expr= -sqrt((m.x3 - m.x27)**2 + (m.x30 - m.x54)**2 + (m.x57
    - m.x81)**2) + m.x82 <= 0)
m.e103 = Constraint(expr= -sqrt((m.x4 - m.x5)**2 + (m.x31 - m.x32)**2 + (m.x58
    - m.x59)**2) + m.x82 <= 0)
m.e104 = Constraint(expr= -sqrt((m.x4 - m.x6)**2 + (m.x31 - m.x33)**2 + (m.x58
    - m.x60)**2) + m.x82 <= 0)
m.e105 = Constraint(expr= -sqrt((m.x4 - m.x7)**2 + (m.x31 - m.x34)**2 + (m.x58
    - m.x61)**2) + m.x82 <= 0)
m.e106 = Constraint(expr= -sqrt((m.x4 - m.x8)**2 + (m.x31 - m.x35)**2 + (m.x58
    - m.x62)**2) + m.x82 <= 0)
m.e107 = Constraint(expr= -sqrt((m.x4 - m.x9)**2 + (m.x31 - m.x36)**2 + (m.x58
    - m.x63)**2) + m.x82 <= 0)
m.e108 = Constraint(expr= -sqrt((m.x4 - m.x10)**2 + (m.x31 - m.x37)**2 + (m.x58
    - m.x64)**2) + m.x82 <= 0)
m.e109 = Constraint(expr= -sqrt((m.x4 - m.x11)**2 + (m.x31 - m.x38)**2 + (m.x58
    - m.x65)**2) + m.x82 <= 0)
m.e110 = Constraint(expr= -sqrt((m.x4 - m.x12)**2 + (m.x31 - m.x39)**2 + (m.x58
    - m.x66)**2) + m.x82 <= 0)
m.e111 = Constraint(expr= -sqrt((m.x4 - m.x13)**2 + (m.x31 - m.x40)**2 + (m.x58
    - m.x67)**2) + m.x82 <= 0)
m.e112 = Constraint(expr= -sqrt((m.x4 - m.x14)**2 + (m.x31 - m.x41)**2 + (m.x58
    - m.x68)**2) + m.x82 <= 0)
m.e113 = Constraint(expr= -sqrt((m.x4 - m.x15)**2 + (m.x31 - m.x42)**2 + (m.x58
    - m.x69)**2) + m.x82 <= 0)
m.e114 = Constraint(expr= -sqrt((m.x4 - m.x16)**2 + (m.x31 - m.x43)**2 + (m.x58
    - m.x70)**2) + m.x82 <= 0)
m.e115 = Constraint(expr= -sqrt((m.x4 - m.x17)**2 + (m.x31 - m.x44)**2 + (m.x58
    - m.x71)**2) + m.x82 <= 0)
m.e116 = Constraint(expr= -sqrt((m.x4 - m.x18)**2 + (m.x31 - m.x45)**2 + (m.x58
    - m.x72)**2) + m.x82 <= 0)
m.e117 = Constraint(expr= -sqrt((m.x4 - m.x19)**2 + (m.x31 - m.x46)**2 + (m.x58
    - m.x73)**2) + m.x82 <= 0)
m.e118 = Constraint(expr= -sqrt((m.x4 - m.x20)**2 + (m.x31 - m.x47)**2 + (m.x58
    - m.x74)**2) + m.x82 <= 0)
m.e119 = Constraint(expr= -sqrt((m.x4 - m.x21)**2 + (m.x31 - m.x48)**2 + (m.x58
    - m.x75)**2) + m.x82 <= 0)
m.e120 = Constraint(expr= -sqrt((m.x4 - m.x22)**2 + (m.x31 - m.x49)**2 + (m.x58
    - m.x76)**2) + m.x82 <= 0)
m.e121 = Constraint(expr= -sqrt((m.x4 - m.x23)**2 + (m.x31 - m.x50)**2 + (m.x58
    - m.x77)**2) + m.x82 <= 0)
m.e122 = Constraint(expr= -sqrt((m.x4 - m.x24)**2 + (m.x31 - m.x51)**2 + (m.x58
    - m.x78)**2) + m.x82 <= 0)
m.e123 = Constraint(expr= -sqrt((m.x4 - m.x25)**2 + (m.x31 - m.x52)**2 + (m.x58
    - m.x79)**2) + m.x82 <= 0)
m.e124 = Constraint(expr= -sqrt((m.x4 - m.x26)**2 + (m.x31 - m.x53)**2 + (m.x58
    - m.x80)**2) + m.x82 <= 0)
m.e125 = Constraint(expr= -sqrt((m.x4 - m.x27)**2 + (m.x31 - m.x54)**2 + (m.x58
    - m.x81)**2) + m.x82 <= 0)
m.e126 = Constraint(expr= -sqrt((m.x5 - m.x6)**2 + (m.x32 - m.x33)**2 + (m.x59
    - m.x60)**2) + m.x82 <= 0)
m.e127 = Constraint(expr= -sqrt((m.x5 - m.x7)**2 + (m.x32 - m.x34)**2 + (m.x59
    - m.x61)**2) + m.x82 <= 0)
m.e128 = Constraint(expr= -sqrt((m.x5 - m.x8)**2 + (m.x32 - m.x35)**2 + (m.x59
    - m.x62)**2) + m.x82 <= 0)
m.e129 = Constraint(expr= -sqrt((m.x5 - m.x9)**2 + (m.x32 - m.x36)**2 + (m.x59
    - m.x63)**2) + m.x82 <= 0)
m.e130 = Constraint(expr= -sqrt((m.x5 - m.x10)**2 + (m.x32 - m.x37)**2 + (m.x59
    - m.x64)**2) + m.x82 <= 0)
m.e131 = Constraint(expr= -sqrt((m.x5 - m.x11)**2 + (m.x32 - m.x38)**2 + (m.x59
    - m.x65)**2) + m.x82 <= 0)
m.e132 = Constraint(expr= -sqrt((m.x5 - m.x12)**2 + (m.x32 - m.x39)**2 + (m.x59
    - m.x66)**2) + m.x82 <= 0)
m.e133 = Constraint(expr= -sqrt((m.x5 - m.x13)**2 + (m.x32 - m.x40)**2 + (m.x59
    - m.x67)**2) + m.x82 <= 0)
m.e134 = Constraint(expr= -sqrt((m.x5 - m.x14)**2 + (m.x32 - m.x41)**2 + (m.x59
    - m.x68)**2) + m.x82 <= 0)
m.e135 = Constraint(expr= -sqrt((m.x5 - m.x15)**2 + (m.x32 - m.x42)**2 + (m.x59
    - m.x69)**2) + m.x82 <= 0)
m.e136 = Constraint(expr= -sqrt((m.x5 - m.x16)**2 + (m.x32 - m.x43)**2 + (m.x59
    - m.x70)**2) + m.x82 <= 0)
m.e137 = Constraint(expr= -sqrt((m.x5 - m.x17)**2 + (m.x32 - m.x44)**2 + (m.x59
    - m.x71)**2) + m.x82 <= 0)
m.e138 = Constraint(expr= -sqrt((m.x5 - m.x18)**2 + (m.x32 - m.x45)**2 + (m.x59
    - m.x72)**2) + m.x82 <= 0)
m.e139 = Constraint(expr= -sqrt((m.x5 - m.x19)**2 + (m.x32 - m.x46)**2 + (m.x59
    - m.x73)**2) + m.x82 <= 0)
m.e140 = Constraint(expr= -sqrt((m.x5 - m.x20)**2 + (m.x32 - m.x47)**2 + (m.x59
    - m.x74)**2) + m.x82 <= 0)
m.e141 = Constraint(expr= -sqrt((m.x5 - m.x21)**2 + (m.x32 - m.x48)**2 + (m.x59
    - m.x75)**2) + m.x82 <= 0)
m.e142 = Constraint(expr= -sqrt((m.x5 - m.x22)**2 + (m.x32 - m.x49)**2 + (m.x59
    - m.x76)**2) + m.x82 <= 0)
m.e143 = Constraint(expr= -sqrt((m.x5 - m.x23)**2 + (m.x32 - m.x50)**2 + (m.x59
    - m.x77)**2) + m.x82 <= 0)
m.e144 = Constraint(expr= -sqrt((m.x5 - m.x24)**2 + (m.x32 - m.x51)**2 + (m.x59
    - m.x78)**2) + m.x82 <= 0)
m.e145 = Constraint(expr= -sqrt((m.x5 - m.x25)**2 + (m.x32 - m.x52)**2 + (m.x59
    - m.x79)**2) + m.x82 <= 0)
m.e146 = Constraint(expr= -sqrt((m.x5 - m.x26)**2 + (m.x32 - m.x53)**2 + (m.x59
    - m.x80)**2) + m.x82 <= 0)
m.e147 = Constraint(expr= -sqrt((m.x5 - m.x27)**2 + (m.x32 - m.x54)**2 + (m.x59
    - m.x81)**2) + m.x82 <= 0)
m.e148 = Constraint(expr= -sqrt((m.x6 - m.x7)**2 + (m.x33 - m.x34)**2 + (m.x60
    - m.x61)**2) + m.x82 <= 0)
m.e149 = Constraint(expr= -sqrt((m.x6 - m.x8)**2 + (m.x33 - m.x35)**2 + (m.x60
    - m.x62)**2) + m.x82 <= 0)
m.e150 = Constraint(expr= -sqrt((m.x6 - m.x9)**2 + (m.x33 - m.x36)**2 + (m.x60
    - m.x63)**2) + m.x82 <= 0)
m.e151 = Constraint(expr= -sqrt((m.x6 - m.x10)**2 + (m.x33 - m.x37)**2 + (m.x60
    - m.x64)**2) + m.x82 <= 0)
m.e152 = Constraint(expr= -sqrt((m.x6 - m.x11)**2 + (m.x33 - m.x38)**2 + (m.x60
    - m.x65)**2) + m.x82 <= 0)
m.e153 = Constraint(expr= -sqrt((m.x6 - m.x12)**2 + (m.x33 - m.x39)**2 + (m.x60
    - m.x66)**2) + m.x82 <= 0)
m.e154 = Constraint(expr= -sqrt((m.x6 - m.x13)**2 + (m.x33 - m.x40)**2 + (m.x60
    - m.x67)**2) + m.x82 <= 0)
m.e155 = Constraint(expr= -sqrt((m.x6 - m.x14)**2 + (m.x33 - m.x41)**2 + (m.x60
    - m.x68)**2) + m.x82 <= 0)
m.e156 = Constraint(expr= -sqrt((m.x6 - m.x15)**2 + (m.x33 - m.x42)**2 + (m.x60
    - m.x69)**2) + m.x82 <= 0)
m.e157 = Constraint(expr= -sqrt((m.x6 - m.x16)**2 + (m.x33 - m.x43)**2 + (m.x60
    - m.x70)**2) + m.x82 <= 0)
m.e158 = Constraint(expr= -sqrt((m.x6 - m.x17)**2 + (m.x33 - m.x44)**2 + (m.x60
    - m.x71)**2) + m.x82 <= 0)
m.e159 = Constraint(expr= -sqrt((m.x6 - m.x18)**2 + (m.x33 - m.x45)**2 + (m.x60
    - m.x72)**2) + m.x82 <= 0)
m.e160 = Constraint(expr= -sqrt((m.x6 - m.x19)**2 + (m.x33 - m.x46)**2 + (m.x60
    - m.x73)**2) + m.x82 <= 0)
m.e161 = Constraint(expr= -sqrt((m.x6 - m.x20)**2 + (m.x33 - m.x47)**2 + (m.x60
    - m.x74)**2) + m.x82 <= 0)
m.e162 = Constraint(expr= -sqrt((m.x6 - m.x21)**2 + (m.x33 - m.x48)**2 + (m.x60
    - m.x75)**2) + m.x82 <= 0)
m.e163 = Constraint(expr= -sqrt((m.x6 - m.x22)**2 + (m.x33 - m.x49)**2 + (m.x60
    - m.x76)**2) + m.x82 <= 0)
m.e164 = Constraint(expr= -sqrt((m.x6 - m.x23)**2 + (m.x33 - m.x50)**2 + (m.x60
    - m.x77)**2) + m.x82 <= 0)
m.e165 = Constraint(expr= -sqrt((m.x6 - m.x24)**2 + (m.x33 - m.x51)**2 + (m.x60
    - m.x78)**2) + m.x82 <= 0)
m.e166 = Constraint(expr= -sqrt((m.x6 - m.x25)**2 + (m.x33 - m.x52)**2 + (m.x60
    - m.x79)**2) + m.x82 <= 0)
m.e167 = Constraint(expr= -sqrt((m.x6 - m.x26)**2 + (m.x33 - m.x53)**2 + (m.x60
    - m.x80)**2) + m.x82 <= 0)
m.e168 = Constraint(expr= -sqrt((m.x6 - m.x27)**2 + (m.x33 - m.x54)**2 + (m.x60
    - m.x81)**2) + m.x82 <= 0)
m.e169 = Constraint(expr= -sqrt((m.x7 - m.x8)**2 + (m.x34 - m.x35)**2 + (m.x61
    - m.x62)**2) + m.x82 <= 0)
m.e170 = Constraint(expr= -sqrt((m.x7 - m.x9)**2 + (m.x34 - m.x36)**2 + (m.x61
    - m.x63)**2) + m.x82 <= 0)
m.e171 = Constraint(expr= -sqrt((m.x7 - m.x10)**2 + (m.x34 - m.x37)**2 + (m.x61
    - m.x64)**2) + m.x82 <= 0)
m.e172 = Constraint(expr= -sqrt((m.x7 - m.x11)**2 + (m.x34 - m.x38)**2 + (m.x61
    - m.x65)**2) + m.x82 <= 0)
m.e173 = Constraint(expr= -sqrt((m.x7 - m.x12)**2 + (m.x34 - m.x39)**2 + (m.x61
    - m.x66)**2) + m.x82 <= 0)
m.e174 = Constraint(expr= -sqrt((m.x7 - m.x13)**2 + (m.x34 - m.x40)**2 + (m.x61
    - m.x67)**2) + m.x82 <= 0)
m.e175 = Constraint(expr= -sqrt((m.x7 - m.x14)**2 + (m.x34 - m.x41)**2 + (m.x61
    - m.x68)**2) + m.x82 <= 0)
m.e176 = Constraint(expr= -sqrt((m.x7 - m.x15)**2 + (m.x34 - m.x42)**2 + (m.x61
    - m.x69)**2) + m.x82 <= 0)
m.e177 = Constraint(expr= -sqrt((m.x7 - m.x16)**2 + (m.x34 - m.x43)**2 + (m.x61
    - m.x70)**2) + m.x82 <= 0)
m.e178 = Constraint(expr= -sqrt((m.x7 - m.x17)**2 + (m.x34 - m.x44)**2 + (m.x61
    - m.x71)**2) + m.x82 <= 0)
m.e179 = Constraint(expr= -sqrt((m.x7 - m.x18)**2 + (m.x34 - m.x45)**2 + (m.x61
    - m.x72)**2) + m.x82 <= 0)
m.e180 = Constraint(expr= -sqrt((m.x7 - m.x19)**2 + (m.x34 - m.x46)**2 + (m.x61
    - m.x73)**2) + m.x82 <= 0)
m.e181 = Constraint(expr= -sqrt((m.x7 - m.x20)**2 + (m.x34 - m.x47)**2 + (m.x61
    - m.x74)**2) + m.x82 <= 0)
m.e182 = Constraint(expr= -sqrt((m.x7 - m.x21)**2 + (m.x34 - m.x48)**2 + (m.x61
    - m.x75)**2) + m.x82 <= 0)
m.e183 = Constraint(expr= -sqrt((m.x7 - m.x22)**2 + (m.x34 - m.x49)**2 + (m.x61
    - m.x76)**2) + m.x82 <= 0)
m.e184 = Constraint(expr= -sqrt((m.x7 - m.x23)**2 + (m.x34 - m.x50)**2 + (m.x61
    - m.x77)**2) + m.x82 <= 0)
m.e185 = Constraint(expr= -sqrt((m.x7 - m.x24)**2 + (m.x34 - m.x51)**2 + (m.x61
    - m.x78)**2) + m.x82 <= 0)
m.e186 = Constraint(expr= -sqrt((m.x7 - m.x25)**2 + (m.x34 - m.x52)**2 + (m.x61
    - m.x79)**2) + m.x82 <= 0)
m.e187 = Constraint(expr= -sqrt((m.x7 - m.x26)**2 + (m.x34 - m.x53)**2 + (m.x61
    - m.x80)**2) + m.x82 <= 0)
m.e188 = Constraint(expr= -sqrt((m.x7 - m.x27)**2 + (m.x34 - m.x54)**2 + (m.x61
    - m.x81)**2) + m.x82 <= 0)
m.e189 = Constraint(expr= -sqrt((m.x8 - m.x9)**2 + (m.x35 - m.x36)**2 + (m.x62
    - m.x63)**2) + m.x82 <= 0)
m.e190 = Constraint(expr= -sqrt((m.x8 - m.x10)**2 + (m.x35 - m.x37)**2 + (m.x62
    - m.x64)**2) + m.x82 <= 0)
m.e191 = Constraint(expr= -sqrt((m.x8 - m.x11)**2 + (m.x35 - m.x38)**2 + (m.x62
    - m.x65)**2) + m.x82 <= 0)
m.e192 = Constraint(expr= -sqrt((m.x8 - m.x12)**2 + (m.x35 - m.x39)**2 + (m.x62
    - m.x66)**2) + m.x82 <= 0)
m.e193 = Constraint(expr= -sqrt((m.x8 - m.x13)**2 + (m.x35 - m.x40)**2 + (m.x62
    - m.x67)**2) + m.x82 <= 0)
m.e194 = Constraint(expr= -sqrt((m.x8 - m.x14)**2 + (m.x35 - m.x41)**2 + (m.x62
    - m.x68)**2) + m.x82 <= 0)
m.e195 = Constraint(expr= -sqrt((m.x8 - m.x15)**2 + (m.x35 - m.x42)**2 + (m.x62
    - m.x69)**2) + m.x82 <= 0)
m.e196 = Constraint(expr= -sqrt((m.x8 - m.x16)**2 + (m.x35 - m.x43)**2 + (m.x62
    - m.x70)**2) + m.x82 <= 0)
m.e197 = Constraint(expr= -sqrt((m.x8 - m.x17)**2 + (m.x35 - m.x44)**2 + (m.x62
    - m.x71)**2) + m.x82 <= 0)
m.e198 = Constraint(expr= -sqrt((m.x8 - m.x18)**2 + (m.x35 - m.x45)**2 + (m.x62
    - m.x72)**2) + m.x82 <= 0)
m.e199 = Constraint(expr= -sqrt((m.x8 - m.x19)**2 + (m.x35 - m.x46)**2 + (m.x62
    - m.x73)**2) + m.x82 <= 0)
m.e200 = Constraint(expr= -sqrt((m.x8 - m.x20)**2 + (m.x35 - m.x47)**2 + (m.x62
    - m.x74)**2) + m.x82 <= 0)
m.e201 = Constraint(expr= -sqrt((m.x8 - m.x21)**2 + (m.x35 - m.x48)**2 + (m.x62
    - m.x75)**2) + m.x82 <= 0)
m.e202 = Constraint(expr= -sqrt((m.x8 - m.x22)**2 + (m.x35 - m.x49)**2 + (m.x62
    - m.x76)**2) + m.x82 <= 0)
m.e203 = Constraint(expr= -sqrt((m.x8 - m.x23)**2 + (m.x35 - m.x50)**2 + (m.x62
    - m.x77)**2) + m.x82 <= 0)
m.e204 = Constraint(expr= -sqrt((m.x8 - m.x24)**2 + (m.x35 - m.x51)**2 + (m.x62
    - m.x78)**2) + m.x82 <= 0)
m.e205 = Constraint(expr= -sqrt((m.x8 - m.x25)**2 + (m.x35 - m.x52)**2 + (m.x62
    - m.x79)**2) + m.x82 <= 0)
m.e206 = Constraint(expr= -sqrt((m.x8 - m.x26)**2 + (m.x35 - m.x53)**2 + (m.x62
    - m.x80)**2) + m.x82 <= 0)
m.e207 = Constraint(expr= -sqrt((m.x8 - m.x27)**2 + (m.x35 - m.x54)**2 + (m.x62
    - m.x81)**2) + m.x82 <= 0)
m.e208 = Constraint(expr= -sqrt((m.x9 - m.x10)**2 + (m.x36 - m.x37)**2 + (m.x63
    - m.x64)**2) + m.x82 <= 0)
m.e209 = Constraint(expr= -sqrt((m.x9 - m.x11)**2 + (m.x36 - m.x38)**2 + (m.x63
    - m.x65)**2) + m.x82 <= 0)
m.e210 = Constraint(expr= -sqrt((m.x9 - m.x12)**2 + (m.x36 - m.x39)**2 + (m.x63
    - m.x66)**2) + m.x82 <= 0)
m.e211 = Constraint(expr= -sqrt((m.x9 - m.x13)**2 + (m.x36 - m.x40)**2 + (m.x63
    - m.x67)**2) + m.x82 <= 0)
m.e212 = Constraint(expr= -sqrt((m.x9 - m.x14)**2 + (m.x36 - m.x41)**2 + (m.x63
    - m.x68)**2) + m.x82 <= 0)
m.e213 = Constraint(expr= -sqrt((m.x9 - m.x15)**2 + (m.x36 - m.x42)**2 + (m.x63
    - m.x69)**2) + m.x82 <= 0)
m.e214 = Constraint(expr= -sqrt((m.x9 - m.x16)**2 + (m.x36 - m.x43)**2 + (m.x63
    - m.x70)**2) + m.x82 <= 0)
m.e215 = Constraint(expr= -sqrt((m.x9 - m.x17)**2 + (m.x36 - m.x44)**2 + (m.x63
    - m.x71)**2) + m.x82 <= 0)
m.e216 = Constraint(expr= -sqrt((m.x9 - m.x18)**2 + (m.x36 - m.x45)**2 + (m.x63
    - m.x72)**2) + m.x82 <= 0)
m.e217 = Constraint(expr= -sqrt((m.x9 - m.x19)**2 + (m.x36 - m.x46)**2 + (m.x63
    - m.x73)**2) + m.x82 <= 0)
m.e218 = Constraint(expr= -sqrt((m.x9 - m.x20)**2 + (m.x36 - m.x47)**2 + (m.x63
    - m.x74)**2) + m.x82 <= 0)
m.e219 = Constraint(expr= -sqrt((m.x9 - m.x21)**2 + (m.x36 - m.x48)**2 + (m.x63
    - m.x75)**2) + m.x82 <= 0)
m.e220 = Constraint(expr= -sqrt((m.x9 - m.x22)**2 + (m.x36 - m.x49)**2 + (m.x63
    - m.x76)**2) + m.x82 <= 0)
m.e221 = Constraint(expr= -sqrt((m.x9 - m.x23)**2 + (m.x36 - m.x50)**2 + (m.x63
    - m.x77)**2) + m.x82 <= 0)
m.e222 = Constraint(expr= -sqrt((m.x9 - m.x24)**2 + (m.x36 - m.x51)**2 + (m.x63
    - m.x78)**2) + m.x82 <= 0)
m.e223 = Constraint(expr= -sqrt((m.x9 - m.x25)**2 + (m.x36 - m.x52)**2 + (m.x63
    - m.x79)**2) + m.x82 <= 0)
m.e224 = Constraint(expr= -sqrt((m.x9 - m.x26)**2 + (m.x36 - m.x53)**2 + (m.x63
    - m.x80)**2) + m.x82 <= 0)
m.e225 = Constraint(expr= -sqrt((m.x9 - m.x27)**2 + (m.x36 - m.x54)**2 + (m.x63
    - m.x81)**2) + m.x82 <= 0)
m.e226 = Constraint(expr= -sqrt((m.x10 - m.x11)**2 + (m.x37 - m.x38)**2 + (
    m.x64 - m.x65)**2) + m.x82 <= 0)
m.e227 = Constraint(expr= -sqrt((m.x10 - m.x12)**2 + (m.x37 - m.x39)**2 + (
    m.x64 - m.x66)**2) + m.x82 <= 0)
m.e228 = Constraint(expr= -sqrt((m.x10 - m.x13)**2 + (m.x37 - m.x40)**2 + (
    m.x64 - m.x67)**2) + m.x82 <= 0)
m.e229 = Constraint(expr= -sqrt((m.x10 - m.x14)**2 + (m.x37 - m.x41)**2 + (
    m.x64 - m.x68)**2) + m.x82 <= 0)
m.e230 = Constraint(expr= -sqrt((m.x10 - m.x15)**2 + (m.x37 - m.x42)**2 + (
    m.x64 - m.x69)**2) + m.x82 <= 0)
m.e231 = Constraint(expr= -sqrt((m.x10 - m.x16)**2 + (m.x37 - m.x43)**2 + (
    m.x64 - m.x70)**2) + m.x82 <= 0)
m.e232 = Constraint(expr= -sqrt((m.x10 - m.x17)**2 + (m.x37 - m.x44)**2 + (
    m.x64 - m.x71)**2) + m.x82 <= 0)
m.e233 = Constraint(expr= -sqrt((m.x10 - m.x18)**2 + (m.x37 - m.x45)**2 + (
    m.x64 - m.x72)**2) + m.x82 <= 0)
m.e234 = Constraint(expr= -sqrt((m.x10 - m.x19)**2 + (m.x37 - m.x46)**2 + (
    m.x64 - m.x73)**2) + m.x82 <= 0)
m.e235 = Constraint(expr= -sqrt((m.x10 - m.x20)**2 + (m.x37 - m.x47)**2 + (
    m.x64 - m.x74)**2) + m.x82 <= 0)
m.e236 = Constraint(expr= -sqrt((m.x10 - m.x21)**2 + (m.x37 - m.x48)**2 + (
    m.x64 - m.x75)**2) + m.x82 <= 0)
m.e237 = Constraint(expr= -sqrt((m.x10 - m.x22)**2 + (m.x37 - m.x49)**2 + (
    m.x64 - m.x76)**2) + m.x82 <= 0)
m.e238 = Constraint(expr= -sqrt((m.x10 - m.x23)**2 + (m.x37 - m.x50)**2 + (
    m.x64 - m.x77)**2) + m.x82 <= 0)
m.e239 = Constraint(expr= -sqrt((m.x10 - m.x24)**2 + (m.x37 - m.x51)**2 + (
    m.x64 - m.x78)**2) + m.x82 <= 0)
m.e240 = Constraint(expr= -sqrt((m.x10 - m.x25)**2 + (m.x37 - m.x52)**2 + (
    m.x64 - m.x79)**2) + m.x82 <= 0)
m.e241 = Constraint(expr= -sqrt((m.x10 - m.x26)**2 + (m.x37 - m.x53)**2 + (
    m.x64 - m.x80)**2) + m.x82 <= 0)
m.e242 = Constraint(expr= -sqrt((m.x10 - m.x27)**2 + (m.x37 - m.x54)**2 + (
    m.x64 - m.x81)**2) + m.x82 <= 0)
m.e243 = Constraint(expr= -sqrt((m.x11 - m.x12)**2 + (m.x38 - m.x39)**2 + (
    m.x65 - m.x66)**2) + m.x82 <= 0)
m.e244 = Constraint(expr= -sqrt((m.x11 - m.x13)**2 + (m.x38 - m.x40)**2 + (
    m.x65 - m.x67)**2) + m.x82 <= 0)
m.e245 = Constraint(expr= -sqrt((m.x11 - m.x14)**2 + (m.x38 - m.x41)**2 + (
    m.x65 - m.x68)**2) + m.x82 <= 0)
m.e246 = Constraint(expr= -sqrt((m.x11 - m.x15)**2 + (m.x38 - m.x42)**2 + (
    m.x65 - m.x69)**2) + m.x82 <= 0)
m.e247 = Constraint(expr= -sqrt((m.x11 - m.x16)**2 + (m.x38 - m.x43)**2 + (
    m.x65 - m.x70)**2) + m.x82 <= 0)
m.e248 = Constraint(expr= -sqrt((m.x11 - m.x17)**2 + (m.x38 - m.x44)**2 + (
    m.x65 - m.x71)**2) + m.x82 <= 0)
m.e249 = Constraint(expr= -sqrt((m.x11 - m.x18)**2 + (m.x38 - m.x45)**2 + (
    m.x65 - m.x72)**2) + m.x82 <= 0)
m.e250 = Constraint(expr= -sqrt((m.x11 - m.x19)**2 + (m.x38 - m.x46)**2 + (
    m.x65 - m.x73)**2) + m.x82 <= 0)
m.e251 = Constraint(expr= -sqrt((m.x11 - m.x20)**2 + (m.x38 - m.x47)**2 + (
    m.x65 - m.x74)**2) + m.x82 <= 0)
m.e252 = Constraint(expr= -sqrt((m.x11 - m.x21)**2 + (m.x38 - m.x48)**2 + (
    m.x65 - m.x75)**2) + m.x82 <= 0)
m.e253 = Constraint(expr= -sqrt((m.x11 - m.x22)**2 + (m.x38 - m.x49)**2 + (
    m.x65 - m.x76)**2) + m.x82 <= 0)
m.e254 = Constraint(expr= -sqrt((m.x11 - m.x23)**2 + (m.x38 - m.x50)**2 + (
    m.x65 - m.x77)**2) + m.x82 <= 0)
m.e255 = Constraint(expr= -sqrt((m.x11 - m.x24)**2 + (m.x38 - m.x51)**2 + (
    m.x65 - m.x78)**2) + m.x82 <= 0)
m.e256 = Constraint(expr= -sqrt((m.x11 - m.x25)**2 + (m.x38 - m.x52)**2 + (
    m.x65 - m.x79)**2) + m.x82 <= 0)
m.e257 = Constraint(expr= -sqrt((m.x11 - m.x26)**2 + (m.x38 - m.x53)**2 + (
    m.x65 - m.x80)**2) + m.x82 <= 0)
m.e258 = Constraint(expr= -sqrt((m.x11 - m.x27)**2 + (m.x38 - m.x54)**2 + (
    m.x65 - m.x81)**2) + m.x82 <= 0)
m.e259 = Constraint(expr= -sqrt((m.x12 - m.x13)**2 + (m.x39 - m.x40)**2 + (
    m.x66 - m.x67)**2) + m.x82 <= 0)
m.e260 = Constraint(expr= -sqrt((m.x12 - m.x14)**2 + (m.x39 - m.x41)**2 + (
    m.x66 - m.x68)**2) + m.x82 <= 0)
m.e261 = Constraint(expr= -sqrt((m.x12 - m.x15)**2 + (m.x39 - m.x42)**2 + (
    m.x66 - m.x69)**2) + m.x82 <= 0)
m.e262 = Constraint(expr= -sqrt((m.x12 - m.x16)**2 + (m.x39 - m.x43)**2 + (
    m.x66 - m.x70)**2) + m.x82 <= 0)
m.e263 = Constraint(expr= -sqrt((m.x12 - m.x17)**2 + (m.x39 - m.x44)**2 + (
    m.x66 - m.x71)**2) + m.x82 <= 0)
m.e264 = Constraint(expr= -sqrt((m.x12 - m.x18)**2 + (m.x39 - m.x45)**2 + (
    m.x66 - m.x72)**2) + m.x82 <= 0)
m.e265 = Constraint(expr= -sqrt((m.x12 - m.x19)**2 + (m.x39 - m.x46)**2 + (
    m.x66 - m.x73)**2) + m.x82 <= 0)
m.e266 = Constraint(expr= -sqrt((m.x12 - m.x20)**2 + (m.x39 - m.x47)**2 + (
    m.x66 - m.x74)**2) + m.x82 <= 0)
m.e267 = Constraint(expr= -sqrt((m.x12 - m.x21)**2 + (m.x39 - m.x48)**2 + (
    m.x66 - m.x75)**2) + m.x82 <= 0)
m.e268 = Constraint(expr= -sqrt((m.x12 - m.x22)**2 + (m.x39 - m.x49)**2 + (
    m.x66 - m.x76)**2) + m.x82 <= 0)
m.e269 = Constraint(expr= -sqrt((m.x12 - m.x23)**2 + (m.x39 - m.x50)**2 + (
    m.x66 - m.x77)**2) + m.x82 <= 0)
m.e270 = Constraint(expr= -sqrt((m.x12 - m.x24)**2 + (m.x39 - m.x51)**2 + (
    m.x66 - m.x78)**2) + m.x82 <= 0)
m.e271 = Constraint(expr= -sqrt((m.x12 - m.x25)**2 + (m.x39 - m.x52)**2 + (
    m.x66 - m.x79)**2) + m.x82 <= 0)
m.e272 = Constraint(expr= -sqrt((m.x12 - m.x26)**2 + (m.x39 - m.x53)**2 + (
    m.x66 - m.x80)**2) + m.x82 <= 0)
m.e273 = Constraint(expr= -sqrt((m.x12 - m.x27)**2 + (m.x39 - m.x54)**2 + (
    m.x66 - m.x81)**2) + m.x82 <= 0)
m.e274 = Constraint(expr= -sqrt((m.x13 - m.x14)**2 + (m.x40 - m.x41)**2 + (
    m.x67 - m.x68)**2) + m.x82 <= 0)
m.e275 = Constraint(expr= -sqrt((m.x13 - m.x15)**2 + (m.x40 - m.x42)**2 + (
    m.x67 - m.x69)**2) + m.x82 <= 0)
m.e276 = Constraint(expr= -sqrt((m.x13 - m.x16)**2 + (m.x40 - m.x43)**2 + (
    m.x67 - m.x70)**2) + m.x82 <= 0)
m.e277 = Constraint(expr= -sqrt((m.x13 - m.x17)**2 + (m.x40 - m.x44)**2 + (
    m.x67 - m.x71)**2) + m.x82 <= 0)
m.e278 = Constraint(expr= -sqrt((m.x13 - m.x18)**2 + (m.x40 - m.x45)**2 + (
    m.x67 - m.x72)**2) + m.x82 <= 0)
m.e279 = Constraint(expr= -sqrt((m.x13 - m.x19)**2 + (m.x40 - m.x46)**2 + (
    m.x67 - m.x73)**2) + m.x82 <= 0)
m.e280 = Constraint(expr= -sqrt((m.x13 - m.x20)**2 + (m.x40 - m.x47)**2 + (
    m.x67 - m.x74)**2) + m.x82 <= 0)
m.e281 = Constraint(expr= -sqrt((m.x13 - m.x21)**2 + (m.x40 - m.x48)**2 + (
    m.x67 - m.x75)**2) + m.x82 <= 0)
m.e282 = Constraint(expr= -sqrt((m.x13 - m.x22)**2 + (m.x40 - m.x49)**2 + (
    m.x67 - m.x76)**2) + m.x82 <= 0)
m.e283 = Constraint(expr= -sqrt((m.x13 - m.x23)**2 + (m.x40 - m.x50)**2 + (
    m.x67 - m.x77)**2) + m.x82 <= 0)
m.e284 = Constraint(expr= -sqrt((m.x13 - m.x24)**2 + (m.x40 - m.x51)**2 + (
    m.x67 - m.x78)**2) + m.x82 <= 0)
m.e285 = Constraint(expr= -sqrt((m.x13 - m.x25)**2 + (m.x40 - m.x52)**2 + (
    m.x67 - m.x79)**2) + m.x82 <= 0)
m.e286 = Constraint(expr= -sqrt((m.x13 - m.x26)**2 + (m.x40 - m.x53)**2 + (
    m.x67 - m.x80)**2) + m.x82 <= 0)
m.e287 = Constraint(expr= -sqrt((m.x13 - m.x27)**2 + (m.x40 - m.x54)**2 + (
    m.x67 - m.x81)**2) + m.x82 <= 0)
m.e288 = Constraint(expr= -sqrt((m.x14 - m.x15)**2 + (m.x41 - m.x42)**2 + (
    m.x68 - m.x69)**2) + m.x82 <= 0)
m.e289 = Constraint(expr= -sqrt((m.x14 - m.x16)**2 + (m.x41 - m.x43)**2 + (
    m.x68 - m.x70)**2) + m.x82 <= 0)
m.e290 = Constraint(expr= -sqrt((m.x14 - m.x17)**2 + (m.x41 - m.x44)**2 + (
    m.x68 - m.x71)**2) + m.x82 <= 0)
m.e291 = Constraint(expr= -sqrt((m.x14 - m.x18)**2 + (m.x41 - m.x45)**2 + (
    m.x68 - m.x72)**2) + m.x82 <= 0)
m.e292 = Constraint(expr= -sqrt((m.x14 - m.x19)**2 + (m.x41 - m.x46)**2 + (
    m.x68 - m.x73)**2) + m.x82 <= 0)
m.e293 = Constraint(expr= -sqrt((m.x14 - m.x20)**2 + (m.x41 - m.x47)**2 + (
    m.x68 - m.x74)**2) + m.x82 <= 0)
m.e294 = Constraint(expr= -sqrt((m.x14 - m.x21)**2 + (m.x41 - m.x48)**2 + (
    m.x68 - m.x75)**2) + m.x82 <= 0)
m.e295 = Constraint(expr= -sqrt((m.x14 - m.x22)**2 + (m.x41 - m.x49)**2 + (
    m.x68 - m.x76)**2) + m.x82 <= 0)
m.e296 = Constraint(expr= -sqrt((m.x14 - m.x23)**2 + (m.x41 - m.x50)**2 + (
    m.x68 - m.x77)**2) + m.x82 <= 0)
m.e297 = Constraint(expr= -sqrt((m.x14 - m.x24)**2 + (m.x41 - m.x51)**2 + (
    m.x68 - m.x78)**2) + m.x82 <= 0)
m.e298 = Constraint(expr= -sqrt((m.x14 - m.x25)**2 + (m.x41 - m.x52)**2 + (
    m.x68 - m.x79)**2) + m.x82 <= 0)
m.e299 = Constraint(expr= -sqrt((m.x14 - m.x26)**2 + (m.x41 - m.x53)**2 + (
    m.x68 - m.x80)**2) + m.x82 <= 0)
m.e300 = Constraint(expr= -sqrt((m.x14 - m.x27)**2 + (m.x41 - m.x54)**2 + (
    m.x68 - m.x81)**2) + m.x82 <= 0)
m.e301 = Constraint(expr= -sqrt((m.x15 - m.x16)**2 + (m.x42 - m.x43)**2 + (
    m.x69 - m.x70)**2) + m.x82 <= 0)
m.e302 = Constraint(expr= -sqrt((m.x15 - m.x17)**2 + (m.x42 - m.x44)**2 + (
    m.x69 - m.x71)**2) + m.x82 <= 0)
m.e303 = Constraint(expr= -sqrt((m.x15 - m.x18)**2 + (m.x42 - m.x45)**2 + (
    m.x69 - m.x72)**2) + m.x82 <= 0)
m.e304 = Constraint(expr= -sqrt((m.x15 - m.x19)**2 + (m.x42 - m.x46)**2 + (
    m.x69 - m.x73)**2) + m.x82 <= 0)
m.e305 = Constraint(expr= -sqrt((m.x15 - m.x20)**2 + (m.x42 - m.x47)**2 + (
    m.x69 - m.x74)**2) + m.x82 <= 0)
m.e306 = Constraint(expr= -sqrt((m.x15 - m.x21)**2 + (m.x42 - m.x48)**2 + (
    m.x69 - m.x75)**2) + m.x82 <= 0)
m.e307 = Constraint(expr= -sqrt((m.x15 - m.x22)**2 + (m.x42 - m.x49)**2 + (
    m.x69 - m.x76)**2) + m.x82 <= 0)
m.e308 = Constraint(expr= -sqrt((m.x15 - m.x23)**2 + (m.x42 - m.x50)**2 + (
    m.x69 - m.x77)**2) + m.x82 <= 0)
m.e309 = Constraint(expr= -sqrt((m.x15 - m.x24)**2 + (m.x42 - m.x51)**2 + (
    m.x69 - m.x78)**2) + m.x82 <= 0)
m.e310 = Constraint(expr= -sqrt((m.x15 - m.x25)**2 + (m.x42 - m.x52)**2 + (
    m.x69 - m.x79)**2) + m.x82 <= 0)
m.e311 = Constraint(expr= -sqrt((m.x15 - m.x26)**2 + (m.x42 - m.x53)**2 + (
    m.x69 - m.x80)**2) + m.x82 <= 0)
m.e312 = Constraint(expr= -sqrt((m.x15 - m.x27)**2 + (m.x42 - m.x54)**2 + (
    m.x69 - m.x81)**2) + m.x82 <= 0)
m.e313 = Constraint(expr= -sqrt((m.x16 - m.x17)**2 + (m.x43 - m.x44)**2 + (
    m.x70 - m.x71)**2) + m.x82 <= 0)
m.e314 = Constraint(expr= -sqrt((m.x16 - m.x18)**2 + (m.x43 - m.x45)**2 + (
    m.x70 - m.x72)**2) + m.x82 <= 0)
m.e315 = Constraint(expr= -sqrt((m.x16 - m.x19)**2 + (m.x43 - m.x46)**2 + (
    m.x70 - m.x73)**2) + m.x82 <= 0)
m.e316 = Constraint(expr= -sqrt((m.x16 - m.x20)**2 + (m.x43 - m.x47)**2 + (
    m.x70 - m.x74)**2) + m.x82 <= 0)
m.e317 = Constraint(expr= -sqrt((m.x16 - m.x21)**2 + (m.x43 - m.x48)**2 + (
    m.x70 - m.x75)**2) + m.x82 <= 0)
m.e318 = Constraint(expr= -sqrt((m.x16 - m.x22)**2 + (m.x43 - m.x49)**2 + (
    m.x70 - m.x76)**2) + m.x82 <= 0)
m.e319 = Constraint(expr= -sqrt((m.x16 - m.x23)**2 + (m.x43 - m.x50)**2 + (
    m.x70 - m.x77)**2) + m.x82 <= 0)
m.e320 = Constraint(expr= -sqrt((m.x16 - m.x24)**2 + (m.x43 - m.x51)**2 + (
    m.x70 - m.x78)**2) + m.x82 <= 0)
m.e321 = Constraint(expr= -sqrt((m.x16 - m.x25)**2 + (m.x43 - m.x52)**2 + (
    m.x70 - m.x79)**2) + m.x82 <= 0)
m.e322 = Constraint(expr= -sqrt((m.x16 - m.x26)**2 + (m.x43 - m.x53)**2 + (
    m.x70 - m.x80)**2) + m.x82 <= 0)
m.e323 = Constraint(expr= -sqrt((m.x16 - m.x27)**2 + (m.x43 - m.x54)**2 + (
    m.x70 - m.x81)**2) + m.x82 <= 0)
m.e324 = Constraint(expr= -sqrt((m.x17 - m.x18)**2 + (m.x44 - m.x45)**2 + (
    m.x71 - m.x72)**2) + m.x82 <= 0)
m.e325 = Constraint(expr= -sqrt((m.x17 - m.x19)**2 + (m.x44 - m.x46)**2 + (
    m.x71 - m.x73)**2) + m.x82 <= 0)
m.e326 = Constraint(expr= -sqrt((m.x17 - m.x20)**2 + (m.x44 - m.x47)**2 + (
    m.x71 - m.x74)**2) + m.x82 <= 0)
m.e327 = Constraint(expr= -sqrt((m.x17 - m.x21)**2 + (m.x44 - m.x48)**2 + (
    m.x71 - m.x75)**2) + m.x82 <= 0)
m.e328 = Constraint(expr= -sqrt((m.x17 - m.x22)**2 + (m.x44 - m.x49)**2 + (
    m.x71 - m.x76)**2) + m.x82 <= 0)
m.e329 = Constraint(expr= -sqrt((m.x17 - m.x23)**2 + (m.x44 - m.x50)**2 + (
    m.x71 - m.x77)**2) + m.x82 <= 0)
m.e330 = Constraint(expr= -sqrt((m.x17 - m.x24)**2 + (m.x44 - m.x51)**2 + (
    m.x71 - m.x78)**2) + m.x82 <= 0)
m.e331 = Constraint(expr= -sqrt((m.x17 - m.x25)**2 + (m.x44 - m.x52)**2 + (
    m.x71 - m.x79)**2) + m.x82 <= 0)
m.e332 = Constraint(expr= -sqrt((m.x17 - m.x26)**2 + (m.x44 - m.x53)**2 + (
    m.x71 - m.x80)**2) + m.x82 <= 0)
m.e333 = Constraint(expr= -sqrt((m.x17 - m.x27)**2 + (m.x44 - m.x54)**2 + (
    m.x71 - m.x81)**2) + m.x82 <= 0)
m.e334 = Constraint(expr= -sqrt((m.x18 - m.x19)**2 + (m.x45 - m.x46)**2 + (
    m.x72 - m.x73)**2) + m.x82 <= 0)
m.e335 = Constraint(expr= -sqrt((m.x18 - m.x20)**2 + (m.x45 - m.x47)**2 + (
    m.x72 - m.x74)**2) + m.x82 <= 0)
m.e336 = Constraint(expr= -sqrt((m.x18 - m.x21)**2 + (m.x45 - m.x48)**2 + (
    m.x72 - m.x75)**2) + m.x82 <= 0)
m.e337 = Constraint(expr= -sqrt((m.x18 - m.x22)**2 + (m.x45 - m.x49)**2 + (
    m.x72 - m.x76)**2) + m.x82 <= 0)
m.e338 = Constraint(expr= -sqrt((m.x18 - m.x23)**2 + (m.x45 - m.x50)**2 + (
    m.x72 - m.x77)**2) + m.x82 <= 0)
m.e339 = Constraint(expr= -sqrt((m.x18 - m.x24)**2 + (m.x45 - m.x51)**2 + (
    m.x72 - m.x78)**2) + m.x82 <= 0)
m.e340 = Constraint(expr= -sqrt((m.x18 - m.x25)**2 + (m.x45 - m.x52)**2 + (
    m.x72 - m.x79)**2) + m.x82 <= 0)
m.e341 = Constraint(expr= -sqrt((m.x18 - m.x26)**2 + (m.x45 - m.x53)**2 + (
    m.x72 - m.x80)**2) + m.x82 <= 0)
m.e342 = Constraint(expr= -sqrt((m.x18 - m.x27)**2 + (m.x45 - m.x54)**2 + (
    m.x72 - m.x81)**2) + m.x82 <= 0)
m.e343 = Constraint(expr= -sqrt((m.x19 - m.x20)**2 + (m.x46 - m.x47)**2 + (
    m.x73 - m.x74)**2) + m.x82 <= 0)
m.e344 = Constraint(expr= -sqrt((m.x19 - m.x21)**2 + (m.x46 - m.x48)**2 + (
    m.x73 - m.x75)**2) + m.x82 <= 0)
m.e345 = Constraint(expr= -sqrt((m.x19 - m.x22)**2 + (m.x46 - m.x49)**2 + (
    m.x73 - m.x76)**2) + m.x82 <= 0)
m.e346 = Constraint(expr= -sqrt((m.x19 - m.x23)**2 + (m.x46 - m.x50)**2 + (
    m.x73 - m.x77)**2) + m.x82 <= 0)
m.e347 = Constraint(expr= -sqrt((m.x19 - m.x24)**2 + (m.x46 - m.x51)**2 + (
    m.x73 - m.x78)**2) + m.x82 <= 0)
m.e348 = Constraint(expr= -sqrt((m.x19 - m.x25)**2 + (m.x46 - m.x52)**2 + (
    m.x73 - m.x79)**2) + m.x82 <= 0)
m.e349 = Constraint(expr= -sqrt((m.x19 - m.x26)**2 + (m.x46 - m.x53)**2 + (
    m.x73 - m.x80)**2) + m.x82 <= 0)
m.e350 = Constraint(expr= -sqrt((m.x19 - m.x27)**2 + (m.x46 - m.x54)**2 + (
    m.x73 - m.x81)**2) + m.x82 <= 0)
m.e351 = Constraint(expr= -sqrt((m.x20 - m.x21)**2 + (m.x47 - m.x48)**2 + (
    m.x74 - m.x75)**2) + m.x82 <= 0)
m.e352 = Constraint(expr= -sqrt((m.x20 - m.x22)**2 + (m.x47 - m.x49)**2 + (
    m.x74 - m.x76)**2) + m.x82 <= 0)
m.e353 = Constraint(expr= -sqrt((m.x20 - m.x23)**2 + (m.x47 - m.x50)**2 + (
    m.x74 - m.x77)**2) + m.x82 <= 0)
m.e354 = Constraint(expr= -sqrt((m.x20 - m.x24)**2 + (m.x47 - m.x51)**2 + (
    m.x74 - m.x78)**2) + m.x82 <= 0)
m.e355 = Constraint(expr= -sqrt((m.x20 - m.x25)**2 + (m.x47 - m.x52)**2 + (
    m.x74 - m.x79)**2) + m.x82 <= 0)
m.e356 = Constraint(expr= -sqrt((m.x20 - m.x26)**2 + (m.x47 - m.x53)**2 + (
    m.x74 - m.x80)**2) + m.x82 <= 0)
m.e357 = Constraint(expr= -sqrt((m.x20 - m.x27)**2 + (m.x47 - m.x54)**2 + (
    m.x74 - m.x81)**2) + m.x82 <= 0)
m.e358 = Constraint(expr= -sqrt((m.x21 - m.x22)**2 + (m.x48 - m.x49)**2 + (
    m.x75 - m.x76)**2) + m.x82 <= 0)
m.e359 = Constraint(expr= -sqrt((m.x21 - m.x23)**2 + (m.x48 - m.x50)**2 + (
    m.x75 - m.x77)**2) + m.x82 <= 0)
m.e360 = Constraint(expr= -sqrt((m.x21 - m.x24)**2 + (m.x48 - m.x51)**2 + (
    m.x75 - m.x78)**2) + m.x82 <= 0)
m.e361 = Constraint(expr= -sqrt((m.x21 - m.x25)**2 + (m.x48 - m.x52)**2 + (
    m.x75 - m.x79)**2) + m.x82 <= 0)
m.e362 = Constraint(expr= -sqrt((m.x21 - m.x26)**2 + (m.x48 - m.x53)**2 + (
    m.x75 - m.x80)**2) + m.x82 <= 0)
m.e363 = Constraint(expr= -sqrt((m.x21 - m.x27)**2 + (m.x48 - m.x54)**2 + (
    m.x75 - m.x81)**2) + m.x82 <= 0)
m.e364 = Constraint(expr= -sqrt((m.x22 - m.x23)**2 + (m.x49 - m.x50)**2 + (
    m.x76 - m.x77)**2) + m.x82 <= 0)
m.e365 = Constraint(expr= -sqrt((m.x22 - m.x24)**2 + (m.x49 - m.x51)**2 + (
    m.x76 - m.x78)**2) + m.x82 <= 0)
m.e366 = Constraint(expr= -sqrt((m.x22 - m.x25)**2 + (m.x49 - m.x52)**2 + (
    m.x76 - m.x79)**2) + m.x82 <= 0)
m.e367 = Constraint(expr= -sqrt((m.x22 - m.x26)**2 + (m.x49 - m.x53)**2 + (
    m.x76 - m.x80)**2) + m.x82 <= 0)
m.e368 = Constraint(expr= -sqrt((m.x22 - m.x27)**2 + (m.x49 - m.x54)**2 + (
    m.x76 - m.x81)**2) + m.x82 <= 0)
m.e369 = Constraint(expr= -sqrt((m.x23 - m.x24)**2 + (m.x50 - m.x51)**2 + (
    m.x77 - m.x78)**2) + m.x82 <= 0)
m.e370 = Constraint(expr= -sqrt((m.x23 - m.x25)**2 + (m.x50 - m.x52)**2 + (
    m.x77 - m.x79)**2) + m.x82 <= 0)
m.e371 = Constraint(expr= -sqrt((m.x23 - m.x26)**2 + (m.x50 - m.x53)**2 + (
    m.x77 - m.x80)**2) + m.x82 <= 0)
m.e372 = Constraint(expr= -sqrt((m.x23 - m.x27)**2 + (m.x50 - m.x54)**2 + (
    m.x77 - m.x81)**2) + m.x82 <= 0)
m.e373 = Constraint(expr= -sqrt((m.x24 - m.x25)**2 + (m.x51 - m.x52)**2 + (
    m.x78 - m.x79)**2) + m.x82 <= 0)
m.e374 = Constraint(expr= -sqrt((m.x24 - m.x26)**2 + (m.x51 - m.x53)**2 + (
    m.x78 - m.x80)**2) + m.x82 <= 0)
m.e375 = Constraint(expr= -sqrt((m.x24 - m.x27)**2 + (m.x51 - m.x54)**2 + (
    m.x78 - m.x81)**2) + m.x82 <= 0)
m.e376 = Constraint(expr= -sqrt((m.x25 - m.x26)**2 + (m.x52 - m.x53)**2 + (
    m.x79 - m.x80)**2) + m.x82 <= 0)
m.e377 = Constraint(expr= -sqrt((m.x25 - m.x27)**2 + (m.x52 - m.x54)**2 + (
    m.x79 - m.x81)**2) + m.x82 <= 0)
m.e378 = Constraint(expr= -sqrt((m.x26 - m.x27)**2 + (m.x53 - m.x54)**2 + (
    m.x80 - m.x81)**2) + m.x82 <= 0)
