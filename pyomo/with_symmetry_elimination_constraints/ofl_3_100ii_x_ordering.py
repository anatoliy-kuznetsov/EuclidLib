# NLP written by GAMS Convert at 03/17/24 14:47:58
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       305        0        0      305        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#         7        7        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       916      304      612
#
# Reformulation has removed 1 variable and 1 equation

from pyomo.environ import *

model = m = ConcreteModel()

m.x1 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x2 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x3 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x4 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x5 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x6 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x7 = Var(within=Reals, bounds=(None,None), initialize=0)

m.obj = Objective(sense=maximize, expr= m.x7)

m.e1 = Constraint(expr= -(-0.00097 + m.x1)**2 - (-0.00367 + m.x4)**2 + m.x7
    <= 0)
m.e2 = Constraint(expr= -(-0.85243 + m.x1)**2 - (-0.84373 + m.x4)**2 + m.x7
    <= 0)
m.e3 = Constraint(expr= -(-0.84217 + m.x1)**2 - (-0.53687 + m.x4)**2 + m.x7
    <= 0)
m.e4 = Constraint(expr= -(-0.47523 + m.x1)**2 - (-0.01453 + m.x4)**2 + m.x7
    <= 0)
m.e5 = Constraint(expr= -(-0.83537 + m.x1)**2 - (-0.54207 + m.x4)**2 + m.x7
    <= 0)
m.e6 = Constraint(expr= -(-0.38603 + m.x1)**2 - (-0.55333 + m.x4)**2 + m.x7
    <= 0)
m.e7 = Constraint(expr= -(-0.90057 + m.x1)**2 - (-0.13927 + m.x4)**2 + m.x7
    <= 0)
m.e8 = Constraint(expr= -(-0.06483 + m.x1)**2 - (-0.74013 + m.x4)**2 + m.x7
    <= 0)
m.e9 = Constraint(expr= -(-0.15777 + m.x1)**2 - (-0.64847 + m.x4)**2 + m.x7
    <= 0)
m.e10 = Constraint(expr= -(-0.79163 + m.x1)**2 - (-0.65493 + m.x4)**2 + m.x7
    <= 0)
m.e11 = Constraint(expr= -(-0.92697 + m.x1)**2 - (-0.58967 + m.x4)**2 + m.x7
    <= 0)
m.e12 = Constraint(expr= -(-0.64643 + m.x1)**2 - (-0.17773 + m.x4)**2 + m.x7
    <= 0)
m.e13 = Constraint(expr= -(-0.72817 + m.x1)**2 - (-0.68287 + m.x4)**2 + m.x7
    <= 0)
m.e14 = Constraint(expr= -(-0.50923 + m.x1)**2 - (-0.98853 + m.x4)**2 + m.x7
    <= 0)
m.e15 = Constraint(expr= -(-0.28137 + m.x1)**2 - (-0.84807 + m.x4)**2 + m.x7
    <= 0)
m.e16 = Constraint(expr= -(-0.06003 + m.x1)**2 - (-0.56733 + m.x4)**2 + m.x7
    <= 0)
m.e17 = Constraint(expr= -(-0.50657 + m.x1)**2 - (-0.20527 + m.x4)**2 + m.x7
    <= 0)
m.e18 = Constraint(expr= -(-0.77883 + m.x1)**2 - (-0.19413 + m.x4)**2 + m.x7
    <= 0)
m.e19 = Constraint(expr= -(-0.52377 + m.x1)**2 - (-0.07447 + m.x4)**2 + m.x7
    <= 0)
m.e20 = Constraint(expr= -(-0.94563 + m.x1)**2 - (-0.94893 + m.x4)**2 + m.x7
    <= 0)
m.e21 = Constraint(expr= -(-0.65297 + m.x1)**2 - (-0.97567 + m.x4)**2 + m.x7
    <= 0)
m.e22 = Constraint(expr= -(-0.64043 + m.x1)**2 - (-0.71173 + m.x4)**2 + m.x7
    <= 0)
m.e23 = Constraint(expr= -(-0.41417 + m.x1)**2 - (-0.62887 + m.x4)**2 + m.x7
    <= 0)
m.e24 = Constraint(expr= -(-0.74323 + m.x1)**2 - (-0.16253 + m.x4)**2 + m.x7
    <= 0)
m.e25 = Constraint(expr= -(-0.52737 + m.x1)**2 - (-0.95407 + m.x4)**2 + m.x7
    <= 0)
m.e26 = Constraint(expr= -(-0.93403 + m.x1)**2 - (-0.78133 + m.x4)**2 + m.x7
    <= 0)
m.e27 = Constraint(expr= -(-0.91257 + m.x1)**2 - (-0.07127 + m.x4)**2 + m.x7
    <= 0)
m.e28 = Constraint(expr= -(-0.69283 + m.x1)**2 - (-0.84813 + m.x4)**2 + m.x7
    <= 0)
m.e29 = Constraint(expr= -(-0.68977 + m.x1)**2 - (-0.30047 + m.x4)**2 + m.x7
    <= 0)
m.e30 = Constraint(expr= -(-0.29963 + m.x1)**2 - (-0.44293 + m.x4)**2 + m.x7
    <= 0)
m.e31 = Constraint(expr= -(-0.17897 + m.x1)**2 - (-0.16167 + m.x4)**2 + m.x7
    <= 0)
m.e32 = Constraint(expr= -(-0.83443 + m.x1)**2 - (-0.44573 + m.x4)**2 + m.x7
    <= 0)
m.e33 = Constraint(expr= -(-0.90017 + m.x1)**2 - (-0.37487 + m.x4)**2 + m.x7
    <= 0)
m.e34 = Constraint(expr= -(-0.17723 + m.x1)**2 - (-0.53653 + m.x4)**2 + m.x7
    <= 0)
m.e35 = Constraint(expr= -(-0.57337 + m.x1)**2 - (-0.86007 + m.x4)**2 + m.x7
    <= 0)
m.e36 = Constraint(expr= -(-0.00803 + m.x1)**2 - (-0.19533 + m.x4)**2 + m.x7
    <= 0)
m.e37 = Constraint(expr= -(-0.11857 + m.x1)**2 - (-0.73727 + m.x4)**2 + m.x7
    <= 0)
m.e38 = Constraint(expr= -(-0.80683 + m.x1)**2 - (-0.70213 + m.x4)**2 + m.x7
    <= 0)
m.e39 = Constraint(expr= -(-0.65577 + m.x1)**2 - (-0.32647 + m.x4)**2 + m.x7
    <= 0)
m.e40 = Constraint(expr= -(-0.85363 + m.x1)**2 - (-0.13693 + m.x4)**2 + m.x7
    <= 0)
m.e41 = Constraint(expr= -(-0.50497 + m.x1)**2 - (-0.14767 + m.x4)**2 + m.x7
    <= 0)
m.e42 = Constraint(expr= -(-0.22843 + m.x1)**2 - (-0.37973 + m.x4)**2 + m.x7
    <= 0)
m.e43 = Constraint(expr= -(-0.18617 + m.x1)**2 - (-0.92087 + m.x4)**2 + m.x7
    <= 0)
m.e44 = Constraint(expr= -(-0.81123 + m.x1)**2 - (-0.11053 + m.x4)**2 + m.x7
    <= 0)
m.e45 = Constraint(expr= -(-0.41937 + m.x1)**2 - (-0.56607 + m.x4)**2 + m.x7
    <= 0)
m.e46 = Constraint(expr= -(-0.28203 + m.x1)**2 - (-0.80933 + m.x4)**2 + m.x7
    <= 0)
m.e47 = Constraint(expr= -(-0.12457 + m.x1)**2 - (-0.20327 + m.x4)**2 + m.x7
    <= 0)
m.e48 = Constraint(expr= -(-0.12083 + m.x1)**2 - (-0.75613 + m.x4)**2 + m.x7
    <= 0)
m.e49 = Constraint(expr= -(-0.42177 + m.x1)**2 - (-0.15247 + m.x4)**2 + m.x7
    <= 0)
m.e50 = Constraint(expr= -(-0.60763 + m.x1)**2 - (-0.03093 + m.x4)**2 + m.x7
    <= 0)
m.e51 = Constraint(expr= -(-0.63097 + m.x1)**2 - (-0.93367 + m.x4)**2 + m.x7
    <= 0)
m.e52 = Constraint(expr= -(-0.82243 + m.x1)**2 - (-0.51373 + m.x4)**2 + m.x7
    <= 0)
m.e53 = Constraint(expr= -(-0.27217 + m.x1)**2 - (-0.26687 + m.x4)**2 + m.x7
    <= 0)
m.e54 = Constraint(expr= -(-0.64523 + m.x1)**2 - (-0.88453 + m.x4)**2 + m.x7
    <= 0)
m.e55 = Constraint(expr= -(-0.06537 + m.x1)**2 - (-0.07207 + m.x4)**2 + m.x7
    <= 0)
m.e56 = Constraint(expr= -(-0.75603 + m.x1)**2 - (-0.62333 + m.x4)**2 + m.x7
    <= 0)
m.e57 = Constraint(expr= -(-0.93057 + m.x1)**2 - (-0.46927 + m.x4)**2 + m.x7
    <= 0)
m.e58 = Constraint(expr= -(-0.63483 + m.x1)**2 - (-0.01013 + m.x4)**2 + m.x7
    <= 0)
m.e59 = Constraint(expr= -(-0.98777 + m.x1)**2 - (-0.77847 + m.x4)**2 + m.x7
    <= 0)
m.e60 = Constraint(expr= -(-0.56163 + m.x1)**2 - (-0.12493 + m.x4)**2 + m.x7
    <= 0)
m.e61 = Constraint(expr= -(-0.55697 + m.x1)**2 - (-0.51967 + m.x4)**2 + m.x7
    <= 0)
m.e62 = Constraint(expr= -(-0.61643 + m.x1)**2 - (-0.84773 + m.x4)**2 + m.x7
    <= 0)
m.e63 = Constraint(expr= -(-0.15817 + m.x1)**2 - (-0.41287 + m.x4)**2 + m.x7
    <= 0)
m.e64 = Constraint(expr= -(-0.67923 + m.x1)**2 - (-0.85853 + m.x4)**2 + m.x7
    <= 0)
m.e65 = Constraint(expr= -(-0.51137 + m.x1)**2 - (-0.37807 + m.x4)**2 + m.x7
    <= 0)
m.e66 = Constraint(expr= -(-0.43003 + m.x1)**2 - (-0.63733 + m.x4)**2 + m.x7
    <= 0)
m.e67 = Constraint(expr= -(-0.53657 + m.x1)**2 - (-0.53527 + m.x4)**2 + m.x7
    <= 0)
m.e68 = Constraint(expr= -(-0.34883 + m.x1)**2 - (-0.46413 + m.x4)**2 + m.x7
    <= 0)
m.e69 = Constraint(expr= -(-0.35377 + m.x1)**2 - (-0.20447 + m.x4)**2 + m.x7
    <= 0)
m.e70 = Constraint(expr= -(-0.71563 + m.x1)**2 - (-0.41893 + m.x4)**2 + m.x7
    <= 0)
m.e71 = Constraint(expr= -(-0.28297 + m.x1)**2 - (-0.90567 + m.x4)**2 + m.x7
    <= 0)
m.e72 = Constraint(expr= -(-0.61043 + m.x1)**2 - (-0.38173 + m.x4)**2 + m.x7
    <= 0)
m.e73 = Constraint(expr= -(-0.84417 + m.x1)**2 - (-0.35887 + m.x4)**2 + m.x7
    <= 0)
m.e74 = Constraint(expr= -(-0.91323 + m.x1)**2 - (-0.03253 + m.x4)**2 + m.x7
    <= 0)
m.e75 = Constraint(expr= -(-0.75737 + m.x1)**2 - (-0.48407 + m.x4)**2 + m.x7
    <= 0)
m.e76 = Constraint(expr= -(-0.30403 + m.x1)**2 - (-0.85133 + m.x4)**2 + m.x7
    <= 0)
m.e77 = Constraint(expr= -(-0.94257 + m.x1)**2 - (-0.40127 + m.x4)**2 + m.x7
    <= 0)
m.e78 = Constraint(expr= -(-0.26283 + m.x1)**2 - (-0.11813 + m.x4)**2 + m.x7
    <= 0)
m.e79 = Constraint(expr= -(-0.51977 + m.x1)**2 - (-0.43047 + m.x4)**2 + m.x7
    <= 0)
m.e80 = Constraint(expr= -(-0.06963 + m.x1)**2 - (-0.91293 + m.x4)**2 + m.x7
    <= 0)
m.e81 = Constraint(expr= -(-0.80897 + m.x1)**2 - (-0.09167 + m.x4)**2 + m.x7
    <= 0)
m.e82 = Constraint(expr= -(-0.80443 + m.x1)**2 - (-0.11573 + m.x4)**2 + m.x7
    <= 0)
m.e83 = Constraint(expr= -(-0.33017 + m.x1)**2 - (-0.10487 + m.x4)**2 + m.x7
    <= 0)
m.e84 = Constraint(expr= -(-0.34723 + m.x1)**2 - (-0.40653 + m.x4)**2 + m.x7
    <= 0)
m.e85 = Constraint(expr= -(-0.80337 + m.x1)**2 - (-0.39007 + m.x4)**2 + m.x7
    <= 0)
m.e86 = Constraint(expr= -(-0.37803 + m.x1)**2 - (-0.26533 + m.x4)**2 + m.x7
    <= 0)
m.e87 = Constraint(expr= -(-0.14857 + m.x1)**2 - (-0.06727 + m.x4)**2 + m.x7
    <= 0)
m.e88 = Constraint(expr= -(-0.37683 + m.x1)**2 - (-0.97213 + m.x4)**2 + m.x7
    <= 0)
m.e89 = Constraint(expr= -(-0.48577 + m.x1)**2 - (-0.45647 + m.x4)**2 + m.x7
    <= 0)
m.e90 = Constraint(expr= -(-0.62363 + m.x1)**2 - (-0.60693 + m.x4)**2 + m.x7
    <= 0)
m.e91 = Constraint(expr= -(-0.13497 + m.x1)**2 - (-0.07767 + m.x4)**2 + m.x7
    <= 0)
m.e92 = Constraint(expr= -(-0.19843 + m.x1)**2 - (-0.04973 + m.x4)**2 + m.x7
    <= 0)
m.e93 = Constraint(expr= -(-0.61617 + m.x1)**2 - (-0.65087 + m.x4)**2 + m.x7
    <= 0)
m.e94 = Constraint(expr= -(-0.98123 + m.x1)**2 - (-0.98053 + m.x4)**2 + m.x7
    <= 0)
m.e95 = Constraint(expr= -(-0.64937 + m.x1)**2 - (-0.09607 + m.x4)**2 + m.x7
    <= 0)
m.e96 = Constraint(expr= -(-0.65203 + m.x1)**2 - (-0.87933 + m.x4)**2 + m.x7
    <= 0)
m.e97 = Constraint(expr= -(-0.15457 + m.x1)**2 - (-0.53327 + m.x4)**2 + m.x7
    <= 0)
m.e98 = Constraint(expr= -(-0.69083 + m.x1)**2 - (-0.02613 + m.x4)**2 + m.x7
    <= 0)
m.e99 = Constraint(expr= -(-0.25177 + m.x1)**2 - (-0.28247 + m.x4)**2 + m.x7
    <= 0)
m.e100 = Constraint(expr= -(-0.37763 + m.x1)**2 - (-0.50093 + m.x4)**2 + m.x7
    <= 0)
m.e101 = Constraint(expr= -(-0.00097 + m.x2)**2 - (-0.00367 + m.x5)**2 + m.x7
    <= 0)
m.e102 = Constraint(expr= -(-0.85243 + m.x2)**2 - (-0.84373 + m.x5)**2 + m.x7
    <= 0)
m.e103 = Constraint(expr= -(-0.84217 + m.x2)**2 - (-0.53687 + m.x5)**2 + m.x7
    <= 0)
m.e104 = Constraint(expr= -(-0.47523 + m.x2)**2 - (-0.01453 + m.x5)**2 + m.x7
    <= 0)
m.e105 = Constraint(expr= -(-0.83537 + m.x2)**2 - (-0.54207 + m.x5)**2 + m.x7
    <= 0)
m.e106 = Constraint(expr= -(-0.38603 + m.x2)**2 - (-0.55333 + m.x5)**2 + m.x7
    <= 0)
m.e107 = Constraint(expr= -(-0.90057 + m.x2)**2 - (-0.13927 + m.x5)**2 + m.x7
    <= 0)
m.e108 = Constraint(expr= -(-0.06483 + m.x2)**2 - (-0.74013 + m.x5)**2 + m.x7
    <= 0)
m.e109 = Constraint(expr= -(-0.15777 + m.x2)**2 - (-0.64847 + m.x5)**2 + m.x7
    <= 0)
m.e110 = Constraint(expr= -(-0.79163 + m.x2)**2 - (-0.65493 + m.x5)**2 + m.x7
    <= 0)
m.e111 = Constraint(expr= -(-0.92697 + m.x2)**2 - (-0.58967 + m.x5)**2 + m.x7
    <= 0)
m.e112 = Constraint(expr= -(-0.64643 + m.x2)**2 - (-0.17773 + m.x5)**2 + m.x7
    <= 0)
m.e113 = Constraint(expr= -(-0.72817 + m.x2)**2 - (-0.68287 + m.x5)**2 + m.x7
    <= 0)
m.e114 = Constraint(expr= -(-0.50923 + m.x2)**2 - (-0.98853 + m.x5)**2 + m.x7
    <= 0)
m.e115 = Constraint(expr= -(-0.28137 + m.x2)**2 - (-0.84807 + m.x5)**2 + m.x7
    <= 0)
m.e116 = Constraint(expr= -(-0.06003 + m.x2)**2 - (-0.56733 + m.x5)**2 + m.x7
    <= 0)
m.e117 = Constraint(expr= -(-0.50657 + m.x2)**2 - (-0.20527 + m.x5)**2 + m.x7
    <= 0)
m.e118 = Constraint(expr= -(-0.77883 + m.x2)**2 - (-0.19413 + m.x5)**2 + m.x7
    <= 0)
m.e119 = Constraint(expr= -(-0.52377 + m.x2)**2 - (-0.07447 + m.x5)**2 + m.x7
    <= 0)
m.e120 = Constraint(expr= -(-0.94563 + m.x2)**2 - (-0.94893 + m.x5)**2 + m.x7
    <= 0)
m.e121 = Constraint(expr= -(-0.65297 + m.x2)**2 - (-0.97567 + m.x5)**2 + m.x7
    <= 0)
m.e122 = Constraint(expr= -(-0.64043 + m.x2)**2 - (-0.71173 + m.x5)**2 + m.x7
    <= 0)
m.e123 = Constraint(expr= -(-0.41417 + m.x2)**2 - (-0.62887 + m.x5)**2 + m.x7
    <= 0)
m.e124 = Constraint(expr= -(-0.74323 + m.x2)**2 - (-0.16253 + m.x5)**2 + m.x7
    <= 0)
m.e125 = Constraint(expr= -(-0.52737 + m.x2)**2 - (-0.95407 + m.x5)**2 + m.x7
    <= 0)
m.e126 = Constraint(expr= -(-0.93403 + m.x2)**2 - (-0.78133 + m.x5)**2 + m.x7
    <= 0)
m.e127 = Constraint(expr= -(-0.91257 + m.x2)**2 - (-0.07127 + m.x5)**2 + m.x7
    <= 0)
m.e128 = Constraint(expr= -(-0.69283 + m.x2)**2 - (-0.84813 + m.x5)**2 + m.x7
    <= 0)
m.e129 = Constraint(expr= -(-0.68977 + m.x2)**2 - (-0.30047 + m.x5)**2 + m.x7
    <= 0)
m.e130 = Constraint(expr= -(-0.29963 + m.x2)**2 - (-0.44293 + m.x5)**2 + m.x7
    <= 0)
m.e131 = Constraint(expr= -(-0.17897 + m.x2)**2 - (-0.16167 + m.x5)**2 + m.x7
    <= 0)
m.e132 = Constraint(expr= -(-0.83443 + m.x2)**2 - (-0.44573 + m.x5)**2 + m.x7
    <= 0)
m.e133 = Constraint(expr= -(-0.90017 + m.x2)**2 - (-0.37487 + m.x5)**2 + m.x7
    <= 0)
m.e134 = Constraint(expr= -(-0.17723 + m.x2)**2 - (-0.53653 + m.x5)**2 + m.x7
    <= 0)
m.e135 = Constraint(expr= -(-0.57337 + m.x2)**2 - (-0.86007 + m.x5)**2 + m.x7
    <= 0)
m.e136 = Constraint(expr= -(-0.00803 + m.x2)**2 - (-0.19533 + m.x5)**2 + m.x7
    <= 0)
m.e137 = Constraint(expr= -(-0.11857 + m.x2)**2 - (-0.73727 + m.x5)**2 + m.x7
    <= 0)
m.e138 = Constraint(expr= -(-0.80683 + m.x2)**2 - (-0.70213 + m.x5)**2 + m.x7
    <= 0)
m.e139 = Constraint(expr= -(-0.65577 + m.x2)**2 - (-0.32647 + m.x5)**2 + m.x7
    <= 0)
m.e140 = Constraint(expr= -(-0.85363 + m.x2)**2 - (-0.13693 + m.x5)**2 + m.x7
    <= 0)
m.e141 = Constraint(expr= -(-0.50497 + m.x2)**2 - (-0.14767 + m.x5)**2 + m.x7
    <= 0)
m.e142 = Constraint(expr= -(-0.22843 + m.x2)**2 - (-0.37973 + m.x5)**2 + m.x7
    <= 0)
m.e143 = Constraint(expr= -(-0.18617 + m.x2)**2 - (-0.92087 + m.x5)**2 + m.x7
    <= 0)
m.e144 = Constraint(expr= -(-0.81123 + m.x2)**2 - (-0.11053 + m.x5)**2 + m.x7
    <= 0)
m.e145 = Constraint(expr= -(-0.41937 + m.x2)**2 - (-0.56607 + m.x5)**2 + m.x7
    <= 0)
m.e146 = Constraint(expr= -(-0.28203 + m.x2)**2 - (-0.80933 + m.x5)**2 + m.x7
    <= 0)
m.e147 = Constraint(expr= -(-0.12457 + m.x2)**2 - (-0.20327 + m.x5)**2 + m.x7
    <= 0)
m.e148 = Constraint(expr= -(-0.12083 + m.x2)**2 - (-0.75613 + m.x5)**2 + m.x7
    <= 0)
m.e149 = Constraint(expr= -(-0.42177 + m.x2)**2 - (-0.15247 + m.x5)**2 + m.x7
    <= 0)
m.e150 = Constraint(expr= -(-0.60763 + m.x2)**2 - (-0.03093 + m.x5)**2 + m.x7
    <= 0)
m.e151 = Constraint(expr= -(-0.63097 + m.x2)**2 - (-0.93367 + m.x5)**2 + m.x7
    <= 0)
m.e152 = Constraint(expr= -(-0.82243 + m.x2)**2 - (-0.51373 + m.x5)**2 + m.x7
    <= 0)
m.e153 = Constraint(expr= -(-0.27217 + m.x2)**2 - (-0.26687 + m.x5)**2 + m.x7
    <= 0)
m.e154 = Constraint(expr= -(-0.64523 + m.x2)**2 - (-0.88453 + m.x5)**2 + m.x7
    <= 0)
m.e155 = Constraint(expr= -(-0.06537 + m.x2)**2 - (-0.07207 + m.x5)**2 + m.x7
    <= 0)
m.e156 = Constraint(expr= -(-0.75603 + m.x2)**2 - (-0.62333 + m.x5)**2 + m.x7
    <= 0)
m.e157 = Constraint(expr= -(-0.93057 + m.x2)**2 - (-0.46927 + m.x5)**2 + m.x7
    <= 0)
m.e158 = Constraint(expr= -(-0.63483 + m.x2)**2 - (-0.01013 + m.x5)**2 + m.x7
    <= 0)
m.e159 = Constraint(expr= -(-0.98777 + m.x2)**2 - (-0.77847 + m.x5)**2 + m.x7
    <= 0)
m.e160 = Constraint(expr= -(-0.56163 + m.x2)**2 - (-0.12493 + m.x5)**2 + m.x7
    <= 0)
m.e161 = Constraint(expr= -(-0.55697 + m.x2)**2 - (-0.51967 + m.x5)**2 + m.x7
    <= 0)
m.e162 = Constraint(expr= -(-0.61643 + m.x2)**2 - (-0.84773 + m.x5)**2 + m.x7
    <= 0)
m.e163 = Constraint(expr= -(-0.15817 + m.x2)**2 - (-0.41287 + m.x5)**2 + m.x7
    <= 0)
m.e164 = Constraint(expr= -(-0.67923 + m.x2)**2 - (-0.85853 + m.x5)**2 + m.x7
    <= 0)
m.e165 = Constraint(expr= -(-0.51137 + m.x2)**2 - (-0.37807 + m.x5)**2 + m.x7
    <= 0)
m.e166 = Constraint(expr= -(-0.43003 + m.x2)**2 - (-0.63733 + m.x5)**2 + m.x7
    <= 0)
m.e167 = Constraint(expr= -(-0.53657 + m.x2)**2 - (-0.53527 + m.x5)**2 + m.x7
    <= 0)
m.e168 = Constraint(expr= -(-0.34883 + m.x2)**2 - (-0.46413 + m.x5)**2 + m.x7
    <= 0)
m.e169 = Constraint(expr= -(-0.35377 + m.x2)**2 - (-0.20447 + m.x5)**2 + m.x7
    <= 0)
m.e170 = Constraint(expr= -(-0.71563 + m.x2)**2 - (-0.41893 + m.x5)**2 + m.x7
    <= 0)
m.e171 = Constraint(expr= -(-0.28297 + m.x2)**2 - (-0.90567 + m.x5)**2 + m.x7
    <= 0)
m.e172 = Constraint(expr= -(-0.61043 + m.x2)**2 - (-0.38173 + m.x5)**2 + m.x7
    <= 0)
m.e173 = Constraint(expr= -(-0.84417 + m.x2)**2 - (-0.35887 + m.x5)**2 + m.x7
    <= 0)
m.e174 = Constraint(expr= -(-0.91323 + m.x2)**2 - (-0.03253 + m.x5)**2 + m.x7
    <= 0)
m.e175 = Constraint(expr= -(-0.75737 + m.x2)**2 - (-0.48407 + m.x5)**2 + m.x7
    <= 0)
m.e176 = Constraint(expr= -(-0.30403 + m.x2)**2 - (-0.85133 + m.x5)**2 + m.x7
    <= 0)
m.e177 = Constraint(expr= -(-0.94257 + m.x2)**2 - (-0.40127 + m.x5)**2 + m.x7
    <= 0)
m.e178 = Constraint(expr= -(-0.26283 + m.x2)**2 - (-0.11813 + m.x5)**2 + m.x7
    <= 0)
m.e179 = Constraint(expr= -(-0.51977 + m.x2)**2 - (-0.43047 + m.x5)**2 + m.x7
    <= 0)
m.e180 = Constraint(expr= -(-0.06963 + m.x2)**2 - (-0.91293 + m.x5)**2 + m.x7
    <= 0)
m.e181 = Constraint(expr= -(-0.80897 + m.x2)**2 - (-0.09167 + m.x5)**2 + m.x7
    <= 0)
m.e182 = Constraint(expr= -(-0.80443 + m.x2)**2 - (-0.11573 + m.x5)**2 + m.x7
    <= 0)
m.e183 = Constraint(expr= -(-0.33017 + m.x2)**2 - (-0.10487 + m.x5)**2 + m.x7
    <= 0)
m.e184 = Constraint(expr= -(-0.34723 + m.x2)**2 - (-0.40653 + m.x5)**2 + m.x7
    <= 0)
m.e185 = Constraint(expr= -(-0.80337 + m.x2)**2 - (-0.39007 + m.x5)**2 + m.x7
    <= 0)
m.e186 = Constraint(expr= -(-0.37803 + m.x2)**2 - (-0.26533 + m.x5)**2 + m.x7
    <= 0)
m.e187 = Constraint(expr= -(-0.14857 + m.x2)**2 - (-0.06727 + m.x5)**2 + m.x7
    <= 0)
m.e188 = Constraint(expr= -(-0.37683 + m.x2)**2 - (-0.97213 + m.x5)**2 + m.x7
    <= 0)
m.e189 = Constraint(expr= -(-0.48577 + m.x2)**2 - (-0.45647 + m.x5)**2 + m.x7
    <= 0)
m.e190 = Constraint(expr= -(-0.62363 + m.x2)**2 - (-0.60693 + m.x5)**2 + m.x7
    <= 0)
m.e191 = Constraint(expr= -(-0.13497 + m.x2)**2 - (-0.07767 + m.x5)**2 + m.x7
    <= 0)
m.e192 = Constraint(expr= -(-0.19843 + m.x2)**2 - (-0.04973 + m.x5)**2 + m.x7
    <= 0)
m.e193 = Constraint(expr= -(-0.61617 + m.x2)**2 - (-0.65087 + m.x5)**2 + m.x7
    <= 0)
m.e194 = Constraint(expr= -(-0.98123 + m.x2)**2 - (-0.98053 + m.x5)**2 + m.x7
    <= 0)
m.e195 = Constraint(expr= -(-0.64937 + m.x2)**2 - (-0.09607 + m.x5)**2 + m.x7
    <= 0)
m.e196 = Constraint(expr= -(-0.65203 + m.x2)**2 - (-0.87933 + m.x5)**2 + m.x7
    <= 0)
m.e197 = Constraint(expr= -(-0.15457 + m.x2)**2 - (-0.53327 + m.x5)**2 + m.x7
    <= 0)
m.e198 = Constraint(expr= -(-0.69083 + m.x2)**2 - (-0.02613 + m.x5)**2 + m.x7
    <= 0)
m.e199 = Constraint(expr= -(-0.25177 + m.x2)**2 - (-0.28247 + m.x5)**2 + m.x7
    <= 0)
m.e200 = Constraint(expr= -(-0.37763 + m.x2)**2 - (-0.50093 + m.x5)**2 + m.x7
    <= 0)
m.e201 = Constraint(expr= -(-0.00097 + m.x3)**2 - (-0.00367 + m.x6)**2 + m.x7
    <= 0)
m.e202 = Constraint(expr= -(-0.85243 + m.x3)**2 - (-0.84373 + m.x6)**2 + m.x7
    <= 0)
m.e203 = Constraint(expr= -(-0.84217 + m.x3)**2 - (-0.53687 + m.x6)**2 + m.x7
    <= 0)
m.e204 = Constraint(expr= -(-0.47523 + m.x3)**2 - (-0.01453 + m.x6)**2 + m.x7
    <= 0)
m.e205 = Constraint(expr= -(-0.83537 + m.x3)**2 - (-0.54207 + m.x6)**2 + m.x7
    <= 0)
m.e206 = Constraint(expr= -(-0.38603 + m.x3)**2 - (-0.55333 + m.x6)**2 + m.x7
    <= 0)
m.e207 = Constraint(expr= -(-0.90057 + m.x3)**2 - (-0.13927 + m.x6)**2 + m.x7
    <= 0)
m.e208 = Constraint(expr= -(-0.06483 + m.x3)**2 - (-0.74013 + m.x6)**2 + m.x7
    <= 0)
m.e209 = Constraint(expr= -(-0.15777 + m.x3)**2 - (-0.64847 + m.x6)**2 + m.x7
    <= 0)
m.e210 = Constraint(expr= -(-0.79163 + m.x3)**2 - (-0.65493 + m.x6)**2 + m.x7
    <= 0)
m.e211 = Constraint(expr= -(-0.92697 + m.x3)**2 - (-0.58967 + m.x6)**2 + m.x7
    <= 0)
m.e212 = Constraint(expr= -(-0.64643 + m.x3)**2 - (-0.17773 + m.x6)**2 + m.x7
    <= 0)
m.e213 = Constraint(expr= -(-0.72817 + m.x3)**2 - (-0.68287 + m.x6)**2 + m.x7
    <= 0)
m.e214 = Constraint(expr= -(-0.50923 + m.x3)**2 - (-0.98853 + m.x6)**2 + m.x7
    <= 0)
m.e215 = Constraint(expr= -(-0.28137 + m.x3)**2 - (-0.84807 + m.x6)**2 + m.x7
    <= 0)
m.e216 = Constraint(expr= -(-0.06003 + m.x3)**2 - (-0.56733 + m.x6)**2 + m.x7
    <= 0)
m.e217 = Constraint(expr= -(-0.50657 + m.x3)**2 - (-0.20527 + m.x6)**2 + m.x7
    <= 0)
m.e218 = Constraint(expr= -(-0.77883 + m.x3)**2 - (-0.19413 + m.x6)**2 + m.x7
    <= 0)
m.e219 = Constraint(expr= -(-0.52377 + m.x3)**2 - (-0.07447 + m.x6)**2 + m.x7
    <= 0)
m.e220 = Constraint(expr= -(-0.94563 + m.x3)**2 - (-0.94893 + m.x6)**2 + m.x7
    <= 0)
m.e221 = Constraint(expr= -(-0.65297 + m.x3)**2 - (-0.97567 + m.x6)**2 + m.x7
    <= 0)
m.e222 = Constraint(expr= -(-0.64043 + m.x3)**2 - (-0.71173 + m.x6)**2 + m.x7
    <= 0)
m.e223 = Constraint(expr= -(-0.41417 + m.x3)**2 - (-0.62887 + m.x6)**2 + m.x7
    <= 0)
m.e224 = Constraint(expr= -(-0.74323 + m.x3)**2 - (-0.16253 + m.x6)**2 + m.x7
    <= 0)
m.e225 = Constraint(expr= -(-0.52737 + m.x3)**2 - (-0.95407 + m.x6)**2 + m.x7
    <= 0)
m.e226 = Constraint(expr= -(-0.93403 + m.x3)**2 - (-0.78133 + m.x6)**2 + m.x7
    <= 0)
m.e227 = Constraint(expr= -(-0.91257 + m.x3)**2 - (-0.07127 + m.x6)**2 + m.x7
    <= 0)
m.e228 = Constraint(expr= -(-0.69283 + m.x3)**2 - (-0.84813 + m.x6)**2 + m.x7
    <= 0)
m.e229 = Constraint(expr= -(-0.68977 + m.x3)**2 - (-0.30047 + m.x6)**2 + m.x7
    <= 0)
m.e230 = Constraint(expr= -(-0.29963 + m.x3)**2 - (-0.44293 + m.x6)**2 + m.x7
    <= 0)
m.e231 = Constraint(expr= -(-0.17897 + m.x3)**2 - (-0.16167 + m.x6)**2 + m.x7
    <= 0)
m.e232 = Constraint(expr= -(-0.83443 + m.x3)**2 - (-0.44573 + m.x6)**2 + m.x7
    <= 0)
m.e233 = Constraint(expr= -(-0.90017 + m.x3)**2 - (-0.37487 + m.x6)**2 + m.x7
    <= 0)
m.e234 = Constraint(expr= -(-0.17723 + m.x3)**2 - (-0.53653 + m.x6)**2 + m.x7
    <= 0)
m.e235 = Constraint(expr= -(-0.57337 + m.x3)**2 - (-0.86007 + m.x6)**2 + m.x7
    <= 0)
m.e236 = Constraint(expr= -(-0.00803 + m.x3)**2 - (-0.19533 + m.x6)**2 + m.x7
    <= 0)
m.e237 = Constraint(expr= -(-0.11857 + m.x3)**2 - (-0.73727 + m.x6)**2 + m.x7
    <= 0)
m.e238 = Constraint(expr= -(-0.80683 + m.x3)**2 - (-0.70213 + m.x6)**2 + m.x7
    <= 0)
m.e239 = Constraint(expr= -(-0.65577 + m.x3)**2 - (-0.32647 + m.x6)**2 + m.x7
    <= 0)
m.e240 = Constraint(expr= -(-0.85363 + m.x3)**2 - (-0.13693 + m.x6)**2 + m.x7
    <= 0)
m.e241 = Constraint(expr= -(-0.50497 + m.x3)**2 - (-0.14767 + m.x6)**2 + m.x7
    <= 0)
m.e242 = Constraint(expr= -(-0.22843 + m.x3)**2 - (-0.37973 + m.x6)**2 + m.x7
    <= 0)
m.e243 = Constraint(expr= -(-0.18617 + m.x3)**2 - (-0.92087 + m.x6)**2 + m.x7
    <= 0)
m.e244 = Constraint(expr= -(-0.81123 + m.x3)**2 - (-0.11053 + m.x6)**2 + m.x7
    <= 0)
m.e245 = Constraint(expr= -(-0.41937 + m.x3)**2 - (-0.56607 + m.x6)**2 + m.x7
    <= 0)
m.e246 = Constraint(expr= -(-0.28203 + m.x3)**2 - (-0.80933 + m.x6)**2 + m.x7
    <= 0)
m.e247 = Constraint(expr= -(-0.12457 + m.x3)**2 - (-0.20327 + m.x6)**2 + m.x7
    <= 0)
m.e248 = Constraint(expr= -(-0.12083 + m.x3)**2 - (-0.75613 + m.x6)**2 + m.x7
    <= 0)
m.e249 = Constraint(expr= -(-0.42177 + m.x3)**2 - (-0.15247 + m.x6)**2 + m.x7
    <= 0)
m.e250 = Constraint(expr= -(-0.60763 + m.x3)**2 - (-0.03093 + m.x6)**2 + m.x7
    <= 0)
m.e251 = Constraint(expr= -(-0.63097 + m.x3)**2 - (-0.93367 + m.x6)**2 + m.x7
    <= 0)
m.e252 = Constraint(expr= -(-0.82243 + m.x3)**2 - (-0.51373 + m.x6)**2 + m.x7
    <= 0)
m.e253 = Constraint(expr= -(-0.27217 + m.x3)**2 - (-0.26687 + m.x6)**2 + m.x7
    <= 0)
m.e254 = Constraint(expr= -(-0.64523 + m.x3)**2 - (-0.88453 + m.x6)**2 + m.x7
    <= 0)
m.e255 = Constraint(expr= -(-0.06537 + m.x3)**2 - (-0.07207 + m.x6)**2 + m.x7
    <= 0)
m.e256 = Constraint(expr= -(-0.75603 + m.x3)**2 - (-0.62333 + m.x6)**2 + m.x7
    <= 0)
m.e257 = Constraint(expr= -(-0.93057 + m.x3)**2 - (-0.46927 + m.x6)**2 + m.x7
    <= 0)
m.e258 = Constraint(expr= -(-0.63483 + m.x3)**2 - (-0.01013 + m.x6)**2 + m.x7
    <= 0)
m.e259 = Constraint(expr= -(-0.98777 + m.x3)**2 - (-0.77847 + m.x6)**2 + m.x7
    <= 0)
m.e260 = Constraint(expr= -(-0.56163 + m.x3)**2 - (-0.12493 + m.x6)**2 + m.x7
    <= 0)
m.e261 = Constraint(expr= -(-0.55697 + m.x3)**2 - (-0.51967 + m.x6)**2 + m.x7
    <= 0)
m.e262 = Constraint(expr= -(-0.61643 + m.x3)**2 - (-0.84773 + m.x6)**2 + m.x7
    <= 0)
m.e263 = Constraint(expr= -(-0.15817 + m.x3)**2 - (-0.41287 + m.x6)**2 + m.x7
    <= 0)
m.e264 = Constraint(expr= -(-0.67923 + m.x3)**2 - (-0.85853 + m.x6)**2 + m.x7
    <= 0)
m.e265 = Constraint(expr= -(-0.51137 + m.x3)**2 - (-0.37807 + m.x6)**2 + m.x7
    <= 0)
m.e266 = Constraint(expr= -(-0.43003 + m.x3)**2 - (-0.63733 + m.x6)**2 + m.x7
    <= 0)
m.e267 = Constraint(expr= -(-0.53657 + m.x3)**2 - (-0.53527 + m.x6)**2 + m.x7
    <= 0)
m.e268 = Constraint(expr= -(-0.34883 + m.x3)**2 - (-0.46413 + m.x6)**2 + m.x7
    <= 0)
m.e269 = Constraint(expr= -(-0.35377 + m.x3)**2 - (-0.20447 + m.x6)**2 + m.x7
    <= 0)
m.e270 = Constraint(expr= -(-0.71563 + m.x3)**2 - (-0.41893 + m.x6)**2 + m.x7
    <= 0)
m.e271 = Constraint(expr= -(-0.28297 + m.x3)**2 - (-0.90567 + m.x6)**2 + m.x7
    <= 0)
m.e272 = Constraint(expr= -(-0.61043 + m.x3)**2 - (-0.38173 + m.x6)**2 + m.x7
    <= 0)
m.e273 = Constraint(expr= -(-0.84417 + m.x3)**2 - (-0.35887 + m.x6)**2 + m.x7
    <= 0)
m.e274 = Constraint(expr= -(-0.91323 + m.x3)**2 - (-0.03253 + m.x6)**2 + m.x7
    <= 0)
m.e275 = Constraint(expr= -(-0.75737 + m.x3)**2 - (-0.48407 + m.x6)**2 + m.x7
    <= 0)
m.e276 = Constraint(expr= -(-0.30403 + m.x3)**2 - (-0.85133 + m.x6)**2 + m.x7
    <= 0)
m.e277 = Constraint(expr= -(-0.94257 + m.x3)**2 - (-0.40127 + m.x6)**2 + m.x7
    <= 0)
m.e278 = Constraint(expr= -(-0.26283 + m.x3)**2 - (-0.11813 + m.x6)**2 + m.x7
    <= 0)
m.e279 = Constraint(expr= -(-0.51977 + m.x3)**2 - (-0.43047 + m.x6)**2 + m.x7
    <= 0)
m.e280 = Constraint(expr= -(-0.06963 + m.x3)**2 - (-0.91293 + m.x6)**2 + m.x7
    <= 0)
m.e281 = Constraint(expr= -(-0.80897 + m.x3)**2 - (-0.09167 + m.x6)**2 + m.x7
    <= 0)
m.e282 = Constraint(expr= -(-0.80443 + m.x3)**2 - (-0.11573 + m.x6)**2 + m.x7
    <= 0)
m.e283 = Constraint(expr= -(-0.33017 + m.x3)**2 - (-0.10487 + m.x6)**2 + m.x7
    <= 0)
m.e284 = Constraint(expr= -(-0.34723 + m.x3)**2 - (-0.40653 + m.x6)**2 + m.x7
    <= 0)
m.e285 = Constraint(expr= -(-0.80337 + m.x3)**2 - (-0.39007 + m.x6)**2 + m.x7
    <= 0)
m.e286 = Constraint(expr= -(-0.37803 + m.x3)**2 - (-0.26533 + m.x6)**2 + m.x7
    <= 0)
m.e287 = Constraint(expr= -(-0.14857 + m.x3)**2 - (-0.06727 + m.x6)**2 + m.x7
    <= 0)
m.e288 = Constraint(expr= -(-0.37683 + m.x3)**2 - (-0.97213 + m.x6)**2 + m.x7
    <= 0)
m.e289 = Constraint(expr= -(-0.48577 + m.x3)**2 - (-0.45647 + m.x6)**2 + m.x7
    <= 0)
m.e290 = Constraint(expr= -(-0.62363 + m.x3)**2 - (-0.60693 + m.x6)**2 + m.x7
    <= 0)
m.e291 = Constraint(expr= -(-0.13497 + m.x3)**2 - (-0.07767 + m.x6)**2 + m.x7
    <= 0)
m.e292 = Constraint(expr= -(-0.19843 + m.x3)**2 - (-0.04973 + m.x6)**2 + m.x7
    <= 0)
m.e293 = Constraint(expr= -(-0.61617 + m.x3)**2 - (-0.65087 + m.x6)**2 + m.x7
    <= 0)
m.e294 = Constraint(expr= -(-0.98123 + m.x3)**2 - (-0.98053 + m.x6)**2 + m.x7
    <= 0)
m.e295 = Constraint(expr= -(-0.64937 + m.x3)**2 - (-0.09607 + m.x6)**2 + m.x7
    <= 0)
m.e296 = Constraint(expr= -(-0.65203 + m.x3)**2 - (-0.87933 + m.x6)**2 + m.x7
    <= 0)
m.e297 = Constraint(expr= -(-0.15457 + m.x3)**2 - (-0.53327 + m.x6)**2 + m.x7
    <= 0)
m.e298 = Constraint(expr= -(-0.69083 + m.x3)**2 - (-0.02613 + m.x6)**2 + m.x7
    <= 0)
m.e299 = Constraint(expr= -(-0.25177 + m.x3)**2 - (-0.28247 + m.x6)**2 + m.x7
    <= 0)
m.e300 = Constraint(expr= -(-0.37763 + m.x3)**2 - (-0.50093 + m.x6)**2 + m.x7
    <= 0)
m.e301 = Constraint(expr= -(m.x1 - m.x2)**2 - (m.x4 - m.x5)**2
    <= -0.3333333333333333)
m.e302 = Constraint(expr= -(m.x1 - m.x3)**2 - (m.x4 - m.x6)**2
    <= -0.3333333333333333)
m.e303 = Constraint(expr= -(m.x2 - m.x3)**2 - (m.x5 - m.x6)**2
    <= -0.3333333333333333)
m.e304 = Constraint(expr= m.x1 - m.x2 <= 0)
m.e305 = Constraint(expr= m.x2 - m.x3 <= 0)
