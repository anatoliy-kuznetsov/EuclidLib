# NLP written by GAMS Convert at 05/15/24 11:46:26
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#      1503        0        0     1503        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#         7        7        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#      4512     1500     3012
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
m.e101 = Constraint(expr= -(-0.26097 + m.x1)**2 - (-0.86367 + m.x4)**2 + m.x7
    <= 0)
m.e102 = Constraint(expr= -(-0.79243 + m.x1)**2 - (-0.18373 + m.x4)**2 + m.x7
    <= 0)
m.e103 = Constraint(expr= -(-0.70217 + m.x1)**2 - (-0.99687 + m.x4)**2 + m.x7
    <= 0)
m.e104 = Constraint(expr= -(-0.81523 + m.x1)**2 - (-0.75453 + m.x4)**2 + m.x7
    <= 0)
m.e105 = Constraint(expr= -(-0.29537 + m.x1)**2 - (-0.60207 + m.x4)**2 + m.x7
    <= 0)
m.e106 = Constraint(expr= -(-0.12603 + m.x1)**2 - (-0.69333 + m.x4)**2 + m.x7
    <= 0)
m.e107 = Constraint(expr= -(-0.96057 + m.x1)**2 - (-0.79927 + m.x4)**2 + m.x7
    <= 0)
m.e108 = Constraint(expr= -(-0.20483 + m.x1)**2 - (-0.28013 + m.x4)**2 + m.x7
    <= 0)
m.e109 = Constraint(expr= -(-0.81777 + m.x1)**2 - (-0.90847 + m.x4)**2 + m.x7
    <= 0)
m.e110 = Constraint(expr= -(-0.33163 + m.x1)**2 - (-0.59493 + m.x4)**2 + m.x7
    <= 0)
m.e111 = Constraint(expr= -(-0.18697 + m.x1)**2 - (-0.44967 + m.x4)**2 + m.x7
    <= 0)
m.e112 = Constraint(expr= -(-0.58643 + m.x1)**2 - (-0.51773 + m.x4)**2 + m.x7
    <= 0)
m.e113 = Constraint(expr= -(-0.58817 + m.x1)**2 - (-0.14287 + m.x4)**2 + m.x7
    <= 0)
m.e114 = Constraint(expr= -(-0.84923 + m.x1)**2 - (-0.72853 + m.x4)**2 + m.x7
    <= 0)
m.e115 = Constraint(expr= -(-0.74137 + m.x1)**2 - (-0.90807 + m.x4)**2 + m.x7
    <= 0)
m.e116 = Constraint(expr= -(-0.80003 + m.x1)**2 - (-0.70733 + m.x4)**2 + m.x7
    <= 0)
m.e117 = Constraint(expr= -(-0.56657 + m.x1)**2 - (-0.86527 + m.x4)**2 + m.x7
    <= 0)
m.e118 = Constraint(expr= -(-0.91883 + m.x1)**2 - (-0.73413 + m.x4)**2 + m.x7
    <= 0)
m.e119 = Constraint(expr= -(-0.18377 + m.x1)**2 - (-0.33447 + m.x4)**2 + m.x7
    <= 0)
m.e120 = Constraint(expr= -(-0.48563 + m.x1)**2 - (-0.88893 + m.x4)**2 + m.x7
    <= 0)
m.e121 = Constraint(expr= -(-0.91297 + m.x1)**2 - (-0.83567 + m.x4)**2 + m.x7
    <= 0)
m.e122 = Constraint(expr= -(-0.58043 + m.x1)**2 - (-0.05173 + m.x4)**2 + m.x7
    <= 0)
m.e123 = Constraint(expr= -(-0.27417 + m.x1)**2 - (-0.08887 + m.x4)**2 + m.x7
    <= 0)
m.e124 = Constraint(expr= -(-0.08323 + m.x1)**2 - (-0.90253 + m.x4)**2 + m.x7
    <= 0)
m.e125 = Constraint(expr= -(-0.98737 + m.x1)**2 - (-0.01407 + m.x4)**2 + m.x7
    <= 0)
m.e126 = Constraint(expr= -(-0.67403 + m.x1)**2 - (-0.92133 + m.x4)**2 + m.x7
    <= 0)
m.e127 = Constraint(expr= -(-0.97257 + m.x1)**2 - (-0.73127 + m.x4)**2 + m.x7
    <= 0)
m.e128 = Constraint(expr= -(-0.83283 + m.x1)**2 - (-0.38813 + m.x4)**2 + m.x7
    <= 0)
m.e129 = Constraint(expr= -(-0.34977 + m.x1)**2 - (-0.56047 + m.x4)**2 + m.x7
    <= 0)
m.e130 = Constraint(expr= -(-0.83963 + m.x1)**2 - (-0.38293 + m.x4)**2 + m.x7
    <= 0)
m.e131 = Constraint(expr= -(-0.43897 + m.x1)**2 - (-0.02167 + m.x4)**2 + m.x7
    <= 0)
m.e132 = Constraint(expr= -(-0.77443 + m.x1)**2 - (-0.78573 + m.x4)**2 + m.x7
    <= 0)
m.e133 = Constraint(expr= -(-0.76017 + m.x1)**2 - (-0.83487 + m.x4)**2 + m.x7
    <= 0)
m.e134 = Constraint(expr= -(-0.51723 + m.x1)**2 - (-0.27653 + m.x4)**2 + m.x7
    <= 0)
m.e135 = Constraint(expr= -(-0.03337 + m.x1)**2 - (-0.92007 + m.x4)**2 + m.x7
    <= 0)
m.e136 = Constraint(expr= -(-0.74803 + m.x1)**2 - (-0.33533 + m.x4)**2 + m.x7
    <= 0)
m.e137 = Constraint(expr= -(-0.17857 + m.x1)**2 - (-0.39727 + m.x4)**2 + m.x7
    <= 0)
m.e138 = Constraint(expr= -(-0.94683 + m.x1)**2 - (-0.24213 + m.x4)**2 + m.x7
    <= 0)
m.e139 = Constraint(expr= -(-0.31577 + m.x1)**2 - (-0.58647 + m.x4)**2 + m.x7
    <= 0)
m.e140 = Constraint(expr= -(-0.39363 + m.x1)**2 - (-0.07693 + m.x4)**2 + m.x7
    <= 0)
m.e141 = Constraint(expr= -(-0.76497 + m.x1)**2 - (-0.00767 + m.x4)**2 + m.x7
    <= 0)
m.e142 = Constraint(expr= -(-0.16843 + m.x1)**2 - (-0.71973 + m.x4)**2 + m.x7
    <= 0)
m.e143 = Constraint(expr= -(-0.04617 + m.x1)**2 - (-0.38087 + m.x4)**2 + m.x7
    <= 0)
m.e144 = Constraint(expr= -(-0.15123 + m.x1)**2 - (-0.85053 + m.x4)**2 + m.x7
    <= 0)
m.e145 = Constraint(expr= -(-0.87937 + m.x1)**2 - (-0.62607 + m.x4)**2 + m.x7
    <= 0)
m.e146 = Constraint(expr= -(-0.02203 + m.x1)**2 - (-0.94933 + m.x4)**2 + m.x7
    <= 0)
m.e147 = Constraint(expr= -(-0.18457 + m.x1)**2 - (-0.86327 + m.x4)**2 + m.x7
    <= 0)
m.e148 = Constraint(expr= -(-0.26083 + m.x1)**2 - (-0.29613 + m.x4)**2 + m.x7
    <= 0)
m.e149 = Constraint(expr= -(-0.08177 + m.x1)**2 - (-0.41247 + m.x4)**2 + m.x7
    <= 0)
m.e150 = Constraint(expr= -(-0.14763 + m.x1)**2 - (-0.97093 + m.x4)**2 + m.x7
    <= 0)
m.e151 = Constraint(expr= -(-0.89097 + m.x1)**2 - (-0.79367 + m.x4)**2 + m.x7
    <= 0)
m.e152 = Constraint(expr= -(-0.76243 + m.x1)**2 - (-0.85373 + m.x4)**2 + m.x7
    <= 0)
m.e153 = Constraint(expr= -(-0.13217 + m.x1)**2 - (-0.72687 + m.x4)**2 + m.x7
    <= 0)
m.e154 = Constraint(expr= -(-0.98523 + m.x1)**2 - (-0.62453 + m.x4)**2 + m.x7
    <= 0)
m.e155 = Constraint(expr= -(-0.52537 + m.x1)**2 - (-0.13207 + m.x4)**2 + m.x7
    <= 0)
m.e156 = Constraint(expr= -(-0.49603 + m.x1)**2 - (-0.76333 + m.x4)**2 + m.x7
    <= 0)
m.e157 = Constraint(expr= -(-0.99057 + m.x1)**2 - (-0.12927 + m.x4)**2 + m.x7
    <= 0)
m.e158 = Constraint(expr= -(-0.77483 + m.x1)**2 - (-0.55013 + m.x4)**2 + m.x7
    <= 0)
m.e159 = Constraint(expr= -(-0.64777 + m.x1)**2 - (-0.03847 + m.x4)**2 + m.x7
    <= 0)
m.e160 = Constraint(expr= -(-0.10163 + m.x1)**2 - (-0.06493 + m.x4)**2 + m.x7
    <= 0)
m.e161 = Constraint(expr= -(-0.81697 + m.x1)**2 - (-0.37967 + m.x4)**2 + m.x7
    <= 0)
m.e162 = Constraint(expr= -(-0.55643 + m.x1)**2 - (-0.18773 + m.x4)**2 + m.x7
    <= 0)
m.e163 = Constraint(expr= -(-0.01817 + m.x1)**2 - (-0.87287 + m.x4)**2 + m.x7
    <= 0)
m.e164 = Constraint(expr= -(-0.01923 + m.x1)**2 - (-0.59853 + m.x4)**2 + m.x7
    <= 0)
m.e165 = Constraint(expr= -(-0.97137 + m.x1)**2 - (-0.43807 + m.x4)**2 + m.x7
    <= 0)
m.e166 = Constraint(expr= -(-0.17003 + m.x1)**2 - (-0.77733 + m.x4)**2 + m.x7
    <= 0)
m.e167 = Constraint(expr= -(-0.59657 + m.x1)**2 - (-0.19527 + m.x4)**2 + m.x7
    <= 0)
m.e168 = Constraint(expr= -(-0.48883 + m.x1)**2 - (-0.00413 + m.x4)**2 + m.x7
    <= 0)
m.e169 = Constraint(expr= -(-0.01377 + m.x1)**2 - (-0.46447 + m.x4)**2 + m.x7
    <= 0)
m.e170 = Constraint(expr= -(-0.25563 + m.x1)**2 - (-0.35893 + m.x4)**2 + m.x7
    <= 0)
m.e171 = Constraint(expr= -(-0.54297 + m.x1)**2 - (-0.76567 + m.x4)**2 + m.x7
    <= 0)
m.e172 = Constraint(expr= -(-0.55043 + m.x1)**2 - (-0.72173 + m.x4)**2 + m.x7
    <= 0)
m.e173 = Constraint(expr= -(-0.70417 + m.x1)**2 - (-0.81887 + m.x4)**2 + m.x7
    <= 0)
m.e174 = Constraint(expr= -(-0.25323 + m.x1)**2 - (-0.77253 + m.x4)**2 + m.x7
    <= 0)
m.e175 = Constraint(expr= -(-0.21737 + m.x1)**2 - (-0.54407 + m.x4)**2 + m.x7
    <= 0)
m.e176 = Constraint(expr= -(-0.04403 + m.x1)**2 - (-0.99133 + m.x4)**2 + m.x7
    <= 0)
m.e177 = Constraint(expr= -(-0.00257 + m.x1)**2 - (-0.06127 + m.x4)**2 + m.x7
    <= 0)
m.e178 = Constraint(expr= -(-0.40283 + m.x1)**2 - (-0.65813 + m.x4)**2 + m.x7
    <= 0)
m.e179 = Constraint(expr= -(-0.17977 + m.x1)**2 - (-0.69047 + m.x4)**2 + m.x7
    <= 0)
m.e180 = Constraint(expr= -(-0.60963 + m.x1)**2 - (-0.85293 + m.x4)**2 + m.x7
    <= 0)
m.e181 = Constraint(expr= -(-0.06897 + m.x1)**2 - (-0.95167 + m.x4)**2 + m.x7
    <= 0)
m.e182 = Constraint(expr= -(-0.74443 + m.x1)**2 - (-0.45573 + m.x4)**2 + m.x7
    <= 0)
m.e183 = Constraint(expr= -(-0.19017 + m.x1)**2 - (-0.56487 + m.x4)**2 + m.x7
    <= 0)
m.e184 = Constraint(expr= -(-0.68723 + m.x1)**2 - (-0.14653 + m.x4)**2 + m.x7
    <= 0)
m.e185 = Constraint(expr= -(-0.26337 + m.x1)**2 - (-0.45007 + m.x4)**2 + m.x7
    <= 0)
m.e186 = Constraint(expr= -(-0.11803 + m.x1)**2 - (-0.40533 + m.x4)**2 + m.x7
    <= 0)
m.e187 = Constraint(expr= -(-0.20857 + m.x1)**2 - (-0.72727 + m.x4)**2 + m.x7
    <= 0)
m.e188 = Constraint(expr= -(-0.51683 + m.x1)**2 - (-0.51213 + m.x4)**2 + m.x7
    <= 0)
m.e189 = Constraint(expr= -(-0.14577 + m.x1)**2 - (-0.71647 + m.x4)**2 + m.x7
    <= 0)
m.e190 = Constraint(expr= -(-0.16363 + m.x1)**2 - (-0.54693 + m.x4)**2 + m.x7
    <= 0)
m.e191 = Constraint(expr= -(-0.39497 + m.x1)**2 - (-0.93767 + m.x4)**2 + m.x7
    <= 0)
m.e192 = Constraint(expr= -(-0.13843 + m.x1)**2 - (-0.38973 + m.x4)**2 + m.x7
    <= 0)
m.e193 = Constraint(expr= -(-0.47617 + m.x1)**2 - (-0.11087 + m.x4)**2 + m.x7
    <= 0)
m.e194 = Constraint(expr= -(-0.32123 + m.x1)**2 - (-0.72053 + m.x4)**2 + m.x7
    <= 0)
m.e195 = Constraint(expr= -(-0.10937 + m.x1)**2 - (-0.15607 + m.x4)**2 + m.x7
    <= 0)
m.e196 = Constraint(expr= -(-0.39203 + m.x1)**2 - (-0.01933 + m.x4)**2 + m.x7
    <= 0)
m.e197 = Constraint(expr= -(-0.21457 + m.x1)**2 - (-0.19327 + m.x4)**2 + m.x7
    <= 0)
m.e198 = Constraint(expr= -(-0.83083 + m.x1)**2 - (-0.56613 + m.x4)**2 + m.x7
    <= 0)
m.e199 = Constraint(expr= -(-0.91177 + m.x1)**2 - (-0.54247 + m.x4)**2 + m.x7
    <= 0)
m.e200 = Constraint(expr= -(-0.91763 + m.x1)**2 - (-0.44093 + m.x4)**2 + m.x7
    <= 0)
m.e201 = Constraint(expr= -(-0.52097 + m.x1)**2 - (-0.72367 + m.x4)**2 + m.x7
    <= 0)
m.e202 = Constraint(expr= -(-0.73243 + m.x1)**2 - (-0.52373 + m.x4)**2 + m.x7
    <= 0)
m.e203 = Constraint(expr= -(-0.56217 + m.x1)**2 - (-0.45687 + m.x4)**2 + m.x7
    <= 0)
m.e204 = Constraint(expr= -(-0.15523 + m.x1)**2 - (-0.49453 + m.x4)**2 + m.x7
    <= 0)
m.e205 = Constraint(expr= -(-0.75537 + m.x1)**2 - (-0.66207 + m.x4)**2 + m.x7
    <= 0)
m.e206 = Constraint(expr= -(-0.86603 + m.x1)**2 - (-0.83333 + m.x4)**2 + m.x7
    <= 0)
m.e207 = Constraint(expr= -(-0.02057 + m.x1)**2 - (-0.45927 + m.x4)**2 + m.x7
    <= 0)
m.e208 = Constraint(expr= -(-0.34483 + m.x1)**2 - (-0.82013 + m.x4)**2 + m.x7
    <= 0)
m.e209 = Constraint(expr= -(-0.47777 + m.x1)**2 - (-0.16847 + m.x4)**2 + m.x7
    <= 0)
m.e210 = Constraint(expr= -(-0.87163 + m.x1)**2 - (-0.53493 + m.x4)**2 + m.x7
    <= 0)
m.e211 = Constraint(expr= -(-0.44697 + m.x1)**2 - (-0.30967 + m.x4)**2 + m.x7
    <= 0)
m.e212 = Constraint(expr= -(-0.52643 + m.x1)**2 - (-0.85773 + m.x4)**2 + m.x7
    <= 0)
m.e213 = Constraint(expr= -(-0.44817 + m.x1)**2 - (-0.60287 + m.x4)**2 + m.x7
    <= 0)
m.e214 = Constraint(expr= -(-0.18923 + m.x1)**2 - (-0.46853 + m.x4)**2 + m.x7
    <= 0)
m.e215 = Constraint(expr= -(-0.20137 + m.x1)**2 - (-0.96807 + m.x4)**2 + m.x7
    <= 0)
m.e216 = Constraint(expr= -(-0.54003 + m.x1)**2 - (-0.84733 + m.x4)**2 + m.x7
    <= 0)
m.e217 = Constraint(expr= -(-0.62657 + m.x1)**2 - (-0.52527 + m.x4)**2 + m.x7
    <= 0)
m.e218 = Constraint(expr= -(-0.05883 + m.x1)**2 - (-0.27413 + m.x4)**2 + m.x7
    <= 0)
m.e219 = Constraint(expr= -(-0.84377 + m.x1)**2 - (-0.59447 + m.x4)**2 + m.x7
    <= 0)
m.e220 = Constraint(expr= -(-0.02563 + m.x1)**2 - (-0.82893 + m.x4)**2 + m.x7
    <= 0)
m.e221 = Constraint(expr= -(-0.17297 + m.x1)**2 - (-0.69567 + m.x4)**2 + m.x7
    <= 0)
m.e222 = Constraint(expr= -(-0.52043 + m.x1)**2 - (-0.39173 + m.x4)**2 + m.x7
    <= 0)
m.e223 = Constraint(expr= -(-0.13417 + m.x1)**2 - (-0.54887 + m.x4)**2 + m.x7
    <= 0)
m.e224 = Constraint(expr= -(-0.42323 + m.x1)**2 - (-0.64253 + m.x4)**2 + m.x7
    <= 0)
m.e225 = Constraint(expr= -(-0.44737 + m.x1)**2 - (-0.07407 + m.x4)**2 + m.x7
    <= 0)
m.e226 = Constraint(expr= -(-0.41403 + m.x1)**2 - (-0.06133 + m.x4)**2 + m.x7
    <= 0)
m.e227 = Constraint(expr= -(-0.03257 + m.x1)**2 - (-0.39127 + m.x4)**2 + m.x7
    <= 0)
m.e228 = Constraint(expr= -(-0.97283 + m.x1)**2 - (-0.92813 + m.x4)**2 + m.x7
    <= 0)
m.e229 = Constraint(expr= -(-0.00977 + m.x1)**2 - (-0.82047 + m.x4)**2 + m.x7
    <= 0)
m.e230 = Constraint(expr= -(-0.37963 + m.x1)**2 - (-0.32293 + m.x4)**2 + m.x7
    <= 0)
m.e231 = Constraint(expr= -(-0.69897 + m.x1)**2 - (-0.88167 + m.x4)**2 + m.x7
    <= 0)
m.e232 = Constraint(expr= -(-0.71443 + m.x1)**2 - (-0.12573 + m.x4)**2 + m.x7
    <= 0)
m.e233 = Constraint(expr= -(-0.62017 + m.x1)**2 - (-0.29487 + m.x4)**2 + m.x7
    <= 0)
m.e234 = Constraint(expr= -(-0.85723 + m.x1)**2 - (-0.01653 + m.x4)**2 + m.x7
    <= 0)
m.e235 = Constraint(expr= -(-0.49337 + m.x1)**2 - (-0.98007 + m.x4)**2 + m.x7
    <= 0)
m.e236 = Constraint(expr= -(-0.48803 + m.x1)**2 - (-0.47533 + m.x4)**2 + m.x7
    <= 0)
m.e237 = Constraint(expr= -(-0.23857 + m.x1)**2 - (-0.05727 + m.x4)**2 + m.x7
    <= 0)
m.e238 = Constraint(expr= -(-0.08683 + m.x1)**2 - (-0.78213 + m.x4)**2 + m.x7
    <= 0)
m.e239 = Constraint(expr= -(-0.97577 + m.x1)**2 - (-0.84647 + m.x4)**2 + m.x7
    <= 0)
m.e240 = Constraint(expr= -(-0.93363 + m.x1)**2 - (-0.01693 + m.x4)**2 + m.x7
    <= 0)
m.e241 = Constraint(expr= -(-0.02497 + m.x1)**2 - (-0.86767 + m.x4)**2 + m.x7
    <= 0)
m.e242 = Constraint(expr= -(-0.10843 + m.x1)**2 - (-0.05973 + m.x4)**2 + m.x7
    <= 0)
m.e243 = Constraint(expr= -(-0.90617 + m.x1)**2 - (-0.84087 + m.x4)**2 + m.x7
    <= 0)
m.e244 = Constraint(expr= -(-0.49123 + m.x1)**2 - (-0.59053 + m.x4)**2 + m.x7
    <= 0)
m.e245 = Constraint(expr= -(-0.33937 + m.x1)**2 - (-0.68607 + m.x4)**2 + m.x7
    <= 0)
m.e246 = Constraint(expr= -(-0.76203 + m.x1)**2 - (-0.08933 + m.x4)**2 + m.x7
    <= 0)
m.e247 = Constraint(expr= -(-0.24457 + m.x1)**2 - (-0.52327 + m.x4)**2 + m.x7
    <= 0)
m.e248 = Constraint(expr= -(-0.40083 + m.x1)**2 - (-0.83613 + m.x4)**2 + m.x7
    <= 0)
m.e249 = Constraint(expr= -(-0.74177 + m.x1)**2 - (-0.67247 + m.x4)**2 + m.x7
    <= 0)
m.e250 = Constraint(expr= -(-0.68763 + m.x1)**2 - (-0.91093 + m.x4)**2 + m.x7
    <= 0)
m.e251 = Constraint(expr= -(-0.15097 + m.x1)**2 - (-0.65367 + m.x4)**2 + m.x7
    <= 0)
m.e252 = Constraint(expr= -(-0.70243 + m.x1)**2 - (-0.19373 + m.x4)**2 + m.x7
    <= 0)
m.e253 = Constraint(expr= -(-0.99217 + m.x1)**2 - (-0.18687 + m.x4)**2 + m.x7
    <= 0)
m.e254 = Constraint(expr= -(-0.32523 + m.x1)**2 - (-0.36453 + m.x4)**2 + m.x7
    <= 0)
m.e255 = Constraint(expr= -(-0.98537 + m.x1)**2 - (-0.19207 + m.x4)**2 + m.x7
    <= 0)
m.e256 = Constraint(expr= -(-0.23603 + m.x1)**2 - (-0.90333 + m.x4)**2 + m.x7
    <= 0)
m.e257 = Constraint(expr= -(-0.05057 + m.x1)**2 - (-0.78927 + m.x4)**2 + m.x7
    <= 0)
m.e258 = Constraint(expr= -(-0.91483 + m.x1)**2 - (-0.09013 + m.x4)**2 + m.x7
    <= 0)
m.e259 = Constraint(expr= -(-0.30777 + m.x1)**2 - (-0.29847 + m.x4)**2 + m.x7
    <= 0)
m.e260 = Constraint(expr= -(-0.64163 + m.x1)**2 - (-0.00493 + m.x4)**2 + m.x7
    <= 0)
m.e261 = Constraint(expr= -(-0.07697 + m.x1)**2 - (-0.23967 + m.x4)**2 + m.x7
    <= 0)
m.e262 = Constraint(expr= -(-0.49643 + m.x1)**2 - (-0.52773 + m.x4)**2 + m.x7
    <= 0)
m.e263 = Constraint(expr= -(-0.87817 + m.x1)**2 - (-0.33287 + m.x4)**2 + m.x7
    <= 0)
m.e264 = Constraint(expr= -(-0.35923 + m.x1)**2 - (-0.33853 + m.x4)**2 + m.x7
    <= 0)
m.e265 = Constraint(expr= -(-0.43137 + m.x1)**2 - (-0.49807 + m.x4)**2 + m.x7
    <= 0)
m.e266 = Constraint(expr= -(-0.91003 + m.x1)**2 - (-0.91733 + m.x4)**2 + m.x7
    <= 0)
m.e267 = Constraint(expr= -(-0.65657 + m.x1)**2 - (-0.85527 + m.x4)**2 + m.x7
    <= 0)
m.e268 = Constraint(expr= -(-0.62883 + m.x1)**2 - (-0.54413 + m.x4)**2 + m.x7
    <= 0)
m.e269 = Constraint(expr= -(-0.67377 + m.x1)**2 - (-0.72447 + m.x4)**2 + m.x7
    <= 0)
m.e270 = Constraint(expr= -(-0.79563 + m.x1)**2 - (-0.29893 + m.x4)**2 + m.x7
    <= 0)
m.e271 = Constraint(expr= -(-0.80297 + m.x1)**2 - (-0.62567 + m.x4)**2 + m.x7
    <= 0)
m.e272 = Constraint(expr= -(-0.49043 + m.x1)**2 - (-0.06173 + m.x4)**2 + m.x7
    <= 0)
m.e273 = Constraint(expr= -(-0.56417 + m.x1)**2 - (-0.27887 + m.x4)**2 + m.x7
    <= 0)
m.e274 = Constraint(expr= -(-0.59323 + m.x1)**2 - (-0.51253 + m.x4)**2 + m.x7
    <= 0)
m.e275 = Constraint(expr= -(-0.67737 + m.x1)**2 - (-0.60407 + m.x4)**2 + m.x7
    <= 0)
m.e276 = Constraint(expr= -(-0.78403 + m.x1)**2 - (-0.13133 + m.x4)**2 + m.x7
    <= 0)
m.e277 = Constraint(expr= -(-0.06257 + m.x1)**2 - (-0.72127 + m.x4)**2 + m.x7
    <= 0)
m.e278 = Constraint(expr= -(-0.54283 + m.x1)**2 - (-0.19813 + m.x4)**2 + m.x7
    <= 0)
m.e279 = Constraint(expr= -(-0.83977 + m.x1)**2 - (-0.95047 + m.x4)**2 + m.x7
    <= 0)
m.e280 = Constraint(expr= -(-0.14963 + m.x1)**2 - (-0.79293 + m.x4)**2 + m.x7
    <= 0)
m.e281 = Constraint(expr= -(-0.32897 + m.x1)**2 - (-0.81167 + m.x4)**2 + m.x7
    <= 0)
m.e282 = Constraint(expr= -(-0.68443 + m.x1)**2 - (-0.79573 + m.x4)**2 + m.x7
    <= 0)
m.e283 = Constraint(expr= -(-0.05017 + m.x1)**2 - (-0.02487 + m.x4)**2 + m.x7
    <= 0)
m.e284 = Constraint(expr= -(-0.02723 + m.x1)**2 - (-0.88653 + m.x4)**2 + m.x7
    <= 0)
m.e285 = Constraint(expr= -(-0.72337 + m.x1)**2 - (-0.51007 + m.x4)**2 + m.x7
    <= 0)
m.e286 = Constraint(expr= -(-0.85803 + m.x1)**2 - (-0.54533 + m.x4)**2 + m.x7
    <= 0)
m.e287 = Constraint(expr= -(-0.26857 + m.x1)**2 - (-0.38727 + m.x4)**2 + m.x7
    <= 0)
m.e288 = Constraint(expr= -(-0.65683 + m.x1)**2 - (-0.05213 + m.x4)**2 + m.x7
    <= 0)
m.e289 = Constraint(expr= -(-0.80577 + m.x1)**2 - (-0.97647 + m.x4)**2 + m.x7
    <= 0)
m.e290 = Constraint(expr= -(-0.70363 + m.x1)**2 - (-0.48693 + m.x4)**2 + m.x7
    <= 0)
m.e291 = Constraint(expr= -(-0.65497 + m.x1)**2 - (-0.79767 + m.x4)**2 + m.x7
    <= 0)
m.e292 = Constraint(expr= -(-0.07843 + m.x1)**2 - (-0.72973 + m.x4)**2 + m.x7
    <= 0)
m.e293 = Constraint(expr= -(-0.33617 + m.x1)**2 - (-0.57087 + m.x4)**2 + m.x7
    <= 0)
m.e294 = Constraint(expr= -(-0.66123 + m.x1)**2 - (-0.46053 + m.x4)**2 + m.x7
    <= 0)
m.e295 = Constraint(expr= -(-0.56937 + m.x1)**2 - (-0.21607 + m.x4)**2 + m.x7
    <= 0)
m.e296 = Constraint(expr= -(-0.13203 + m.x1)**2 - (-0.15933 + m.x4)**2 + m.x7
    <= 0)
m.e297 = Constraint(expr= -(-0.27457 + m.x1)**2 - (-0.85327 + m.x4)**2 + m.x7
    <= 0)
m.e298 = Constraint(expr= -(-0.97083 + m.x1)**2 - (-0.10613 + m.x4)**2 + m.x7
    <= 0)
m.e299 = Constraint(expr= -(-0.57177 + m.x1)**2 - (-0.80247 + m.x4)**2 + m.x7
    <= 0)
m.e300 = Constraint(expr= -(-0.45763 + m.x1)**2 - (-0.38093 + m.x4)**2 + m.x7
    <= 0)
m.e301 = Constraint(expr= -(-0.78097 + m.x1)**2 - (-0.58367 + m.x4)**2 + m.x7
    <= 0)
m.e302 = Constraint(expr= -(-0.67243 + m.x1)**2 - (-0.86373 + m.x4)**2 + m.x7
    <= 0)
m.e303 = Constraint(expr= -(-0.42217 + m.x1)**2 - (-0.91687 + m.x4)**2 + m.x7
    <= 0)
m.e304 = Constraint(expr= -(-0.49523 + m.x1)**2 - (-0.23453 + m.x4)**2 + m.x7
    <= 0)
m.e305 = Constraint(expr= -(-0.21537 + m.x1)**2 - (-0.72207 + m.x4)**2 + m.x7
    <= 0)
m.e306 = Constraint(expr= -(-0.60603 + m.x1)**2 - (-0.97333 + m.x4)**2 + m.x7
    <= 0)
m.e307 = Constraint(expr= -(-0.08057 + m.x1)**2 - (-0.11927 + m.x4)**2 + m.x7
    <= 0)
m.e308 = Constraint(expr= -(-0.48483 + m.x1)**2 - (-0.36013 + m.x4)**2 + m.x7
    <= 0)
m.e309 = Constraint(expr= -(-0.13777 + m.x1)**2 - (-0.42847 + m.x4)**2 + m.x7
    <= 0)
m.e310 = Constraint(expr= -(-0.41163 + m.x1)**2 - (-0.47493 + m.x4)**2 + m.x7
    <= 0)
m.e311 = Constraint(expr= -(-0.70697 + m.x1)**2 - (-0.16967 + m.x4)**2 + m.x7
    <= 0)
m.e312 = Constraint(expr= -(-0.46643 + m.x1)**2 - (-0.19773 + m.x4)**2 + m.x7
    <= 0)
m.e313 = Constraint(expr= -(-0.30817 + m.x1)**2 - (-0.06287 + m.x4)**2 + m.x7
    <= 0)
m.e314 = Constraint(expr= -(-0.52923 + m.x1)**2 - (-0.20853 + m.x4)**2 + m.x7
    <= 0)
m.e315 = Constraint(expr= -(-0.66137 + m.x1)**2 - (-0.02807 + m.x4)**2 + m.x7
    <= 0)
m.e316 = Constraint(expr= -(-0.28003 + m.x1)**2 - (-0.98733 + m.x4)**2 + m.x7
    <= 0)
m.e317 = Constraint(expr= -(-0.68657 + m.x1)**2 - (-0.18527 + m.x4)**2 + m.x7
    <= 0)
m.e318 = Constraint(expr= -(-0.19883 + m.x1)**2 - (-0.81413 + m.x4)**2 + m.x7
    <= 0)
m.e319 = Constraint(expr= -(-0.50377 + m.x1)**2 - (-0.85447 + m.x4)**2 + m.x7
    <= 0)
m.e320 = Constraint(expr= -(-0.56563 + m.x1)**2 - (-0.76893 + m.x4)**2 + m.x7
    <= 0)
m.e321 = Constraint(expr= -(-0.43297 + m.x1)**2 - (-0.55567 + m.x4)**2 + m.x7
    <= 0)
m.e322 = Constraint(expr= -(-0.46043 + m.x1)**2 - (-0.73173 + m.x4)**2 + m.x7
    <= 0)
m.e323 = Constraint(expr= -(-0.99417 + m.x1)**2 - (-0.00887 + m.x4)**2 + m.x7
    <= 0)
m.e324 = Constraint(expr= -(-0.76323 + m.x1)**2 - (-0.38253 + m.x4)**2 + m.x7
    <= 0)
m.e325 = Constraint(expr= -(-0.90737 + m.x1)**2 - (-0.13407 + m.x4)**2 + m.x7
    <= 0)
m.e326 = Constraint(expr= -(-0.15403 + m.x1)**2 - (-0.20133 + m.x4)**2 + m.x7
    <= 0)
m.e327 = Constraint(expr= -(-0.09257 + m.x1)**2 - (-0.05127 + m.x4)**2 + m.x7
    <= 0)
m.e328 = Constraint(expr= -(-0.11283 + m.x1)**2 - (-0.46813 + m.x4)**2 + m.x7
    <= 0)
m.e329 = Constraint(expr= -(-0.66977 + m.x1)**2 - (-0.08047 + m.x4)**2 + m.x7
    <= 0)
m.e330 = Constraint(expr= -(-0.91963 + m.x1)**2 - (-0.26293 + m.x4)**2 + m.x7
    <= 0)
m.e331 = Constraint(expr= -(-0.95897 + m.x1)**2 - (-0.74167 + m.x4)**2 + m.x7
    <= 0)
m.e332 = Constraint(expr= -(-0.65443 + m.x1)**2 - (-0.46573 + m.x4)**2 + m.x7
    <= 0)
m.e333 = Constraint(expr= -(-0.48017 + m.x1)**2 - (-0.75487 + m.x4)**2 + m.x7
    <= 0)
m.e334 = Constraint(expr= -(-0.19723 + m.x1)**2 - (-0.75653 + m.x4)**2 + m.x7
    <= 0)
m.e335 = Constraint(expr= -(-0.95337 + m.x1)**2 - (-0.04007 + m.x4)**2 + m.x7
    <= 0)
m.e336 = Constraint(expr= -(-0.22803 + m.x1)**2 - (-0.61533 + m.x4)**2 + m.x7
    <= 0)
m.e337 = Constraint(expr= -(-0.29857 + m.x1)**2 - (-0.71727 + m.x4)**2 + m.x7
    <= 0)
m.e338 = Constraint(expr= -(-0.22683 + m.x1)**2 - (-0.32213 + m.x4)**2 + m.x7
    <= 0)
m.e339 = Constraint(expr= -(-0.63577 + m.x1)**2 - (-0.10647 + m.x4)**2 + m.x7
    <= 0)
m.e340 = Constraint(expr= -(-0.47363 + m.x1)**2 - (-0.95693 + m.x4)**2 + m.x7
    <= 0)
m.e341 = Constraint(expr= -(-0.28497 + m.x1)**2 - (-0.72767 + m.x4)**2 + m.x7
    <= 0)
m.e342 = Constraint(expr= -(-0.04843 + m.x1)**2 - (-0.39973 + m.x4)**2 + m.x7
    <= 0)
m.e343 = Constraint(expr= -(-0.76617 + m.x1)**2 - (-0.30087 + m.x4)**2 + m.x7
    <= 0)
m.e344 = Constraint(expr= -(-0.83123 + m.x1)**2 - (-0.33053 + m.x4)**2 + m.x7
    <= 0)
m.e345 = Constraint(expr= -(-0.79937 + m.x1)**2 - (-0.74607 + m.x4)**2 + m.x7
    <= 0)
m.e346 = Constraint(expr= -(-0.50203 + m.x1)**2 - (-0.22933 + m.x4)**2 + m.x7
    <= 0)
m.e347 = Constraint(expr= -(-0.30457 + m.x1)**2 - (-0.18327 + m.x4)**2 + m.x7
    <= 0)
m.e348 = Constraint(expr= -(-0.54083 + m.x1)**2 - (-0.37613 + m.x4)**2 + m.x7
    <= 0)
m.e349 = Constraint(expr= -(-0.40177 + m.x1)**2 - (-0.93247 + m.x4)**2 + m.x7
    <= 0)
m.e350 = Constraint(expr= -(-0.22763 + m.x1)**2 - (-0.85093 + m.x4)**2 + m.x7
    <= 0)
m.e351 = Constraint(expr= -(-0.41097 + m.x1)**2 - (-0.51367 + m.x4)**2 + m.x7
    <= 0)
m.e352 = Constraint(expr= -(-0.64243 + m.x1)**2 - (-0.53373 + m.x4)**2 + m.x7
    <= 0)
m.e353 = Constraint(expr= -(-0.85217 + m.x1)**2 - (-0.64687 + m.x4)**2 + m.x7
    <= 0)
m.e354 = Constraint(expr= -(-0.66523 + m.x1)**2 - (-0.10453 + m.x4)**2 + m.x7
    <= 0)
m.e355 = Constraint(expr= -(-0.44537 + m.x1)**2 - (-0.25207 + m.x4)**2 + m.x7
    <= 0)
m.e356 = Constraint(expr= -(-0.97603 + m.x1)**2 - (-0.04333 + m.x4)**2 + m.x7
    <= 0)
m.e357 = Constraint(expr= -(-0.11057 + m.x1)**2 - (-0.44927 + m.x4)**2 + m.x7
    <= 0)
m.e358 = Constraint(expr= -(-0.05483 + m.x1)**2 - (-0.63013 + m.x4)**2 + m.x7
    <= 0)
m.e359 = Constraint(expr= -(-0.96777 + m.x1)**2 - (-0.55847 + m.x4)**2 + m.x7
    <= 0)
m.e360 = Constraint(expr= -(-0.18163 + m.x1)**2 - (-0.94493 + m.x4)**2 + m.x7
    <= 0)
m.e361 = Constraint(expr= -(-0.33697 + m.x1)**2 - (-0.09967 + m.x4)**2 + m.x7
    <= 0)
m.e362 = Constraint(expr= -(-0.43643 + m.x1)**2 - (-0.86773 + m.x4)**2 + m.x7
    <= 0)
m.e363 = Constraint(expr= -(-0.73817 + m.x1)**2 - (-0.79287 + m.x4)**2 + m.x7
    <= 0)
m.e364 = Constraint(expr= -(-0.69923 + m.x1)**2 - (-0.07853 + m.x4)**2 + m.x7
    <= 0)
m.e365 = Constraint(expr= -(-0.89137 + m.x1)**2 - (-0.55807 + m.x4)**2 + m.x7
    <= 0)
m.e366 = Constraint(expr= -(-0.65003 + m.x1)**2 - (-0.05733 + m.x4)**2 + m.x7
    <= 0)
m.e367 = Constraint(expr= -(-0.71657 + m.x1)**2 - (-0.51527 + m.x4)**2 + m.x7
    <= 0)
m.e368 = Constraint(expr= -(-0.76883 + m.x1)**2 - (-0.08413 + m.x4)**2 + m.x7
    <= 0)
m.e369 = Constraint(expr= -(-0.33377 + m.x1)**2 - (-0.98447 + m.x4)**2 + m.x7
    <= 0)
m.e370 = Constraint(expr= -(-0.33563 + m.x1)**2 - (-0.23893 + m.x4)**2 + m.x7
    <= 0)
m.e371 = Constraint(expr= -(-0.06297 + m.x1)**2 - (-0.48567 + m.x4)**2 + m.x7
    <= 0)
m.e372 = Constraint(expr= -(-0.43043 + m.x1)**2 - (-0.40173 + m.x4)**2 + m.x7
    <= 0)
m.e373 = Constraint(expr= -(-0.42417 + m.x1)**2 - (-0.73887 + m.x4)**2 + m.x7
    <= 0)
m.e374 = Constraint(expr= -(-0.93323 + m.x1)**2 - (-0.25253 + m.x4)**2 + m.x7
    <= 0)
m.e375 = Constraint(expr= -(-0.13737 + m.x1)**2 - (-0.66407 + m.x4)**2 + m.x7
    <= 0)
m.e376 = Constraint(expr= -(-0.52403 + m.x1)**2 - (-0.27133 + m.x4)**2 + m.x7
    <= 0)
m.e377 = Constraint(expr= -(-0.12257 + m.x1)**2 - (-0.38127 + m.x4)**2 + m.x7
    <= 0)
m.e378 = Constraint(expr= -(-0.68283 + m.x1)**2 - (-0.73813 + m.x4)**2 + m.x7
    <= 0)
m.e379 = Constraint(expr= -(-0.49977 + m.x1)**2 - (-0.21047 + m.x4)**2 + m.x7
    <= 0)
m.e380 = Constraint(expr= -(-0.68963 + m.x1)**2 - (-0.73293 + m.x4)**2 + m.x7
    <= 0)
m.e381 = Constraint(expr= -(-0.58897 + m.x1)**2 - (-0.67167 + m.x4)**2 + m.x7
    <= 0)
m.e382 = Constraint(expr= -(-0.62443 + m.x1)**2 - (-0.13573 + m.x4)**2 + m.x7
    <= 0)
m.e383 = Constraint(expr= -(-0.91017 + m.x1)**2 - (-0.48487 + m.x4)**2 + m.x7
    <= 0)
m.e384 = Constraint(expr= -(-0.36723 + m.x1)**2 - (-0.62653 + m.x4)**2 + m.x7
    <= 0)
m.e385 = Constraint(expr= -(-0.18337 + m.x1)**2 - (-0.57007 + m.x4)**2 + m.x7
    <= 0)
m.e386 = Constraint(expr= -(-0.59803 + m.x1)**2 - (-0.68533 + m.x4)**2 + m.x7
    <= 0)
m.e387 = Constraint(expr= -(-0.32857 + m.x1)**2 - (-0.04727 + m.x4)**2 + m.x7
    <= 0)
m.e388 = Constraint(expr= -(-0.79683 + m.x1)**2 - (-0.59213 + m.x4)**2 + m.x7
    <= 0)
m.e389 = Constraint(expr= -(-0.46577 + m.x1)**2 - (-0.23647 + m.x4)**2 + m.x7
    <= 0)
m.e390 = Constraint(expr= -(-0.24363 + m.x1)**2 - (-0.42693 + m.x4)**2 + m.x7
    <= 0)
m.e391 = Constraint(expr= -(-0.91497 + m.x1)**2 - (-0.65767 + m.x4)**2 + m.x7
    <= 0)
m.e392 = Constraint(expr= -(-0.01843 + m.x1)**2 - (-0.06973 + m.x4)**2 + m.x7
    <= 0)
m.e393 = Constraint(expr= -(-0.19617 + m.x1)**2 - (-0.03087 + m.x4)**2 + m.x7
    <= 0)
m.e394 = Constraint(expr= -(-0.00123 + m.x1)**2 - (-0.20053 + m.x4)**2 + m.x7
    <= 0)
m.e395 = Constraint(expr= -(-0.02937 + m.x1)**2 - (-0.27607 + m.x4)**2 + m.x7
    <= 0)
m.e396 = Constraint(expr= -(-0.87203 + m.x1)**2 - (-0.29933 + m.x4)**2 + m.x7
    <= 0)
m.e397 = Constraint(expr= -(-0.33457 + m.x1)**2 - (-0.51327 + m.x4)**2 + m.x7
    <= 0)
m.e398 = Constraint(expr= -(-0.11083 + m.x1)**2 - (-0.64613 + m.x4)**2 + m.x7
    <= 0)
m.e399 = Constraint(expr= -(-0.23177 + m.x1)**2 - (-0.06247 + m.x4)**2 + m.x7
    <= 0)
m.e400 = Constraint(expr= -(-0.99763 + m.x1)**2 - (-0.32093 + m.x4)**2 + m.x7
    <= 0)
m.e401 = Constraint(expr= -(-0.04097 + m.x1)**2 - (-0.44367 + m.x4)**2 + m.x7
    <= 0)
m.e402 = Constraint(expr= -(-0.61243 + m.x1)**2 - (-0.20373 + m.x4)**2 + m.x7
    <= 0)
m.e403 = Constraint(expr= -(-0.28217 + m.x1)**2 - (-0.37687 + m.x4)**2 + m.x7
    <= 0)
m.e404 = Constraint(expr= -(-0.83523 + m.x1)**2 - (-0.97453 + m.x4)**2 + m.x7
    <= 0)
m.e405 = Constraint(expr= -(-0.67537 + m.x1)**2 - (-0.78207 + m.x4)**2 + m.x7
    <= 0)
m.e406 = Constraint(expr= -(-0.34603 + m.x1)**2 - (-0.11333 + m.x4)**2 + m.x7
    <= 0)
m.e407 = Constraint(expr= -(-0.14057 + m.x1)**2 - (-0.77927 + m.x4)**2 + m.x7
    <= 0)
m.e408 = Constraint(expr= -(-0.62483 + m.x1)**2 - (-0.90013 + m.x4)**2 + m.x7
    <= 0)
m.e409 = Constraint(expr= -(-0.79777 + m.x1)**2 - (-0.68847 + m.x4)**2 + m.x7
    <= 0)
m.e410 = Constraint(expr= -(-0.95163 + m.x1)**2 - (-0.41493 + m.x4)**2 + m.x7
    <= 0)
m.e411 = Constraint(expr= -(-0.96697 + m.x1)**2 - (-0.02967 + m.x4)**2 + m.x7
    <= 0)
m.e412 = Constraint(expr= -(-0.40643 + m.x1)**2 - (-0.53773 + m.x4)**2 + m.x7
    <= 0)
m.e413 = Constraint(expr= -(-0.16817 + m.x1)**2 - (-0.52287 + m.x4)**2 + m.x7
    <= 0)
m.e414 = Constraint(expr= -(-0.86923 + m.x1)**2 - (-0.94853 + m.x4)**2 + m.x7
    <= 0)
m.e415 = Constraint(expr= -(-0.12137 + m.x1)**2 - (-0.08807 + m.x4)**2 + m.x7
    <= 0)
m.e416 = Constraint(expr= -(-0.02003 + m.x1)**2 - (-0.12733 + m.x4)**2 + m.x7
    <= 0)
m.e417 = Constraint(expr= -(-0.74657 + m.x1)**2 - (-0.84527 + m.x4)**2 + m.x7
    <= 0)
m.e418 = Constraint(expr= -(-0.33883 + m.x1)**2 - (-0.35413 + m.x4)**2 + m.x7
    <= 0)
m.e419 = Constraint(expr= -(-0.16377 + m.x1)**2 - (-0.11447 + m.x4)**2 + m.x7
    <= 0)
m.e420 = Constraint(expr= -(-0.10563 + m.x1)**2 - (-0.70893 + m.x4)**2 + m.x7
    <= 0)
m.e421 = Constraint(expr= -(-0.69297 + m.x1)**2 - (-0.41567 + m.x4)**2 + m.x7
    <= 0)
m.e422 = Constraint(expr= -(-0.40043 + m.x1)**2 - (-0.07173 + m.x4)**2 + m.x7
    <= 0)
m.e423 = Constraint(expr= -(-0.85417 + m.x1)**2 - (-0.46887 + m.x4)**2 + m.x7
    <= 0)
m.e424 = Constraint(expr= -(-0.10323 + m.x1)**2 - (-0.12253 + m.x4)**2 + m.x7
    <= 0)
m.e425 = Constraint(expr= -(-0.36737 + m.x1)**2 - (-0.19407 + m.x4)**2 + m.x7
    <= 0)
m.e426 = Constraint(expr= -(-0.89403 + m.x1)**2 - (-0.34133 + m.x4)**2 + m.x7
    <= 0)
m.e427 = Constraint(expr= -(-0.15257 + m.x1)**2 - (-0.71127 + m.x4)**2 + m.x7
    <= 0)
m.e428 = Constraint(expr= -(-0.25283 + m.x1)**2 - (-0.00813 + m.x4)**2 + m.x7
    <= 0)
m.e429 = Constraint(expr= -(-0.32977 + m.x1)**2 - (-0.34047 + m.x4)**2 + m.x7
    <= 0)
m.e430 = Constraint(expr= -(-0.45963 + m.x1)**2 - (-0.20293 + m.x4)**2 + m.x7
    <= 0)
m.e431 = Constraint(expr= -(-0.21897 + m.x1)**2 - (-0.60167 + m.x4)**2 + m.x7
    <= 0)
m.e432 = Constraint(expr= -(-0.59443 + m.x1)**2 - (-0.80573 + m.x4)**2 + m.x7
    <= 0)
m.e433 = Constraint(expr= -(-0.34017 + m.x1)**2 - (-0.21487 + m.x4)**2 + m.x7
    <= 0)
m.e434 = Constraint(expr= -(-0.53723 + m.x1)**2 - (-0.49653 + m.x4)**2 + m.x7
    <= 0)
m.e435 = Constraint(expr= -(-0.41337 + m.x1)**2 - (-0.10007 + m.x4)**2 + m.x7
    <= 0)
m.e436 = Constraint(expr= -(-0.96803 + m.x1)**2 - (-0.75533 + m.x4)**2 + m.x7
    <= 0)
m.e437 = Constraint(expr= -(-0.35857 + m.x1)**2 - (-0.37727 + m.x4)**2 + m.x7
    <= 0)
m.e438 = Constraint(expr= -(-0.36683 + m.x1)**2 - (-0.86213 + m.x4)**2 + m.x7
    <= 0)
m.e439 = Constraint(expr= -(-0.29577 + m.x1)**2 - (-0.36647 + m.x4)**2 + m.x7
    <= 0)
m.e440 = Constraint(expr= -(-0.01363 + m.x1)**2 - (-0.89693 + m.x4)**2 + m.x7
    <= 0)
m.e441 = Constraint(expr= -(-0.54497 + m.x1)**2 - (-0.58767 + m.x4)**2 + m.x7
    <= 0)
m.e442 = Constraint(expr= -(-0.98843 + m.x1)**2 - (-0.73973 + m.x4)**2 + m.x7
    <= 0)
m.e443 = Constraint(expr= -(-0.62617 + m.x1)**2 - (-0.76087 + m.x4)**2 + m.x7
    <= 0)
m.e444 = Constraint(expr= -(-0.17123 + m.x1)**2 - (-0.07053 + m.x4)**2 + m.x7
    <= 0)
m.e445 = Constraint(expr= -(-0.25937 + m.x1)**2 - (-0.80607 + m.x4)**2 + m.x7
    <= 0)
m.e446 = Constraint(expr= -(-0.24203 + m.x1)**2 - (-0.36933 + m.x4)**2 + m.x7
    <= 0)
m.e447 = Constraint(expr= -(-0.36457 + m.x1)**2 - (-0.84327 + m.x4)**2 + m.x7
    <= 0)
m.e448 = Constraint(expr= -(-0.68083 + m.x1)**2 - (-0.91613 + m.x4)**2 + m.x7
    <= 0)
m.e449 = Constraint(expr= -(-0.06177 + m.x1)**2 - (-0.19247 + m.x4)**2 + m.x7
    <= 0)
m.e450 = Constraint(expr= -(-0.76763 + m.x1)**2 - (-0.79093 + m.x4)**2 + m.x7
    <= 0)
m.e451 = Constraint(expr= -(-0.67097 + m.x1)**2 - (-0.37367 + m.x4)**2 + m.x7
    <= 0)
m.e452 = Constraint(expr= -(-0.58243 + m.x1)**2 - (-0.87373 + m.x4)**2 + m.x7
    <= 0)
m.e453 = Constraint(expr= -(-0.71217 + m.x1)**2 - (-0.10687 + m.x4)**2 + m.x7
    <= 0)
m.e454 = Constraint(expr= -(-0.00523 + m.x1)**2 - (-0.84453 + m.x4)**2 + m.x7
    <= 0)
m.e455 = Constraint(expr= -(-0.90537 + m.x1)**2 - (-0.31207 + m.x4)**2 + m.x7
    <= 0)
m.e456 = Constraint(expr= -(-0.71603 + m.x1)**2 - (-0.18333 + m.x4)**2 + m.x7
    <= 0)
m.e457 = Constraint(expr= -(-0.17057 + m.x1)**2 - (-0.10927 + m.x4)**2 + m.x7
    <= 0)
m.e458 = Constraint(expr= -(-0.19483 + m.x1)**2 - (-0.17013 + m.x4)**2 + m.x7
    <= 0)
m.e459 = Constraint(expr= -(-0.62777 + m.x1)**2 - (-0.81847 + m.x4)**2 + m.x7
    <= 0)
m.e460 = Constraint(expr= -(-0.72163 + m.x1)**2 - (-0.88493 + m.x4)**2 + m.x7
    <= 0)
m.e461 = Constraint(expr= -(-0.59697 + m.x1)**2 - (-0.95967 + m.x4)**2 + m.x7
    <= 0)
m.e462 = Constraint(expr= -(-0.37643 + m.x1)**2 - (-0.20773 + m.x4)**2 + m.x7
    <= 0)
m.e463 = Constraint(expr= -(-0.59817 + m.x1)**2 - (-0.25287 + m.x4)**2 + m.x7
    <= 0)
m.e464 = Constraint(expr= -(-0.03923 + m.x1)**2 - (-0.81853 + m.x4)**2 + m.x7
    <= 0)
m.e465 = Constraint(expr= -(-0.35137 + m.x1)**2 - (-0.61807 + m.x4)**2 + m.x7
    <= 0)
m.e466 = Constraint(expr= -(-0.39003 + m.x1)**2 - (-0.19733 + m.x4)**2 + m.x7
    <= 0)
m.e467 = Constraint(expr= -(-0.77657 + m.x1)**2 - (-0.17527 + m.x4)**2 + m.x7
    <= 0)
m.e468 = Constraint(expr= -(-0.90883 + m.x1)**2 - (-0.62413 + m.x4)**2 + m.x7
    <= 0)
m.e469 = Constraint(expr= -(-0.99377 + m.x1)**2 - (-0.24447 + m.x4)**2 + m.x7
    <= 0)
m.e470 = Constraint(expr= -(-0.87563 + m.x1)**2 - (-0.17893 + m.x4)**2 + m.x7
    <= 0)
m.e471 = Constraint(expr= -(-0.32297 + m.x1)**2 - (-0.34567 + m.x4)**2 + m.x7
    <= 0)
m.e472 = Constraint(expr= -(-0.37043 + m.x1)**2 - (-0.74173 + m.x4)**2 + m.x7
    <= 0)
m.e473 = Constraint(expr= -(-0.28417 + m.x1)**2 - (-0.19887 + m.x4)**2 + m.x7
    <= 0)
m.e474 = Constraint(expr= -(-0.27323 + m.x1)**2 - (-0.99253 + m.x4)**2 + m.x7
    <= 0)
m.e475 = Constraint(expr= -(-0.59737 + m.x1)**2 - (-0.72407 + m.x4)**2 + m.x7
    <= 0)
m.e476 = Constraint(expr= -(-0.26403 + m.x1)**2 - (-0.41133 + m.x4)**2 + m.x7
    <= 0)
m.e477 = Constraint(expr= -(-0.18257 + m.x1)**2 - (-0.04127 + m.x4)**2 + m.x7
    <= 0)
m.e478 = Constraint(expr= -(-0.82283 + m.x1)**2 - (-0.27813 + m.x4)**2 + m.x7
    <= 0)
m.e479 = Constraint(expr= -(-0.15977 + m.x1)**2 - (-0.47047 + m.x4)**2 + m.x7
    <= 0)
m.e480 = Constraint(expr= -(-0.22963 + m.x1)**2 - (-0.67293 + m.x4)**2 + m.x7
    <= 0)
m.e481 = Constraint(expr= -(-0.84897 + m.x1)**2 - (-0.53167 + m.x4)**2 + m.x7
    <= 0)
m.e482 = Constraint(expr= -(-0.56443 + m.x1)**2 - (-0.47573 + m.x4)**2 + m.x7
    <= 0)
m.e483 = Constraint(expr= -(-0.77017 + m.x1)**2 - (-0.94487 + m.x4)**2 + m.x7
    <= 0)
m.e484 = Constraint(expr= -(-0.70723 + m.x1)**2 - (-0.36653 + m.x4)**2 + m.x7
    <= 0)
m.e485 = Constraint(expr= -(-0.64337 + m.x1)**2 - (-0.63007 + m.x4)**2 + m.x7
    <= 0)
m.e486 = Constraint(expr= -(-0.33803 + m.x1)**2 - (-0.82533 + m.x4)**2 + m.x7
    <= 0)
m.e487 = Constraint(expr= -(-0.38857 + m.x1)**2 - (-0.70727 + m.x4)**2 + m.x7
    <= 0)
m.e488 = Constraint(expr= -(-0.93683 + m.x1)**2 - (-0.13213 + m.x4)**2 + m.x7
    <= 0)
m.e489 = Constraint(expr= -(-0.12577 + m.x1)**2 - (-0.49647 + m.x4)**2 + m.x7
    <= 0)
m.e490 = Constraint(expr= -(-0.78363 + m.x1)**2 - (-0.36693 + m.x4)**2 + m.x7
    <= 0)
m.e491 = Constraint(expr= -(-0.17497 + m.x1)**2 - (-0.51767 + m.x4)**2 + m.x7
    <= 0)
m.e492 = Constraint(expr= -(-0.95843 + m.x1)**2 - (-0.40973 + m.x4)**2 + m.x7
    <= 0)
m.e493 = Constraint(expr= -(-0.05617 + m.x1)**2 - (-0.49087 + m.x4)**2 + m.x7
    <= 0)
m.e494 = Constraint(expr= -(-0.34123 + m.x1)**2 - (-0.94053 + m.x4)**2 + m.x7
    <= 0)
m.e495 = Constraint(expr= -(-0.48937 + m.x1)**2 - (-0.33607 + m.x4)**2 + m.x7
    <= 0)
m.e496 = Constraint(expr= -(-0.61203 + m.x1)**2 - (-0.43933 + m.x4)**2 + m.x7
    <= 0)
m.e497 = Constraint(expr= -(-0.39457 + m.x1)**2 - (-0.17327 + m.x4)**2 + m.x7
    <= 0)
m.e498 = Constraint(expr= -(-0.25083 + m.x1)**2 - (-0.18613 + m.x4)**2 + m.x7
    <= 0)
m.e499 = Constraint(expr= -(-0.89177 + m.x1)**2 - (-0.32247 + m.x4)**2 + m.x7
    <= 0)
m.e500 = Constraint(expr= -(-0.53763 + m.x1)**2 - (-0.26093 + m.x4)**2 + m.x7
    <= 0)
m.e501 = Constraint(expr= -(-0.00097 + m.x2)**2 - (-0.00367 + m.x5)**2 + m.x7
    <= 0)
m.e502 = Constraint(expr= -(-0.85243 + m.x2)**2 - (-0.84373 + m.x5)**2 + m.x7
    <= 0)
m.e503 = Constraint(expr= -(-0.84217 + m.x2)**2 - (-0.53687 + m.x5)**2 + m.x7
    <= 0)
m.e504 = Constraint(expr= -(-0.47523 + m.x2)**2 - (-0.01453 + m.x5)**2 + m.x7
    <= 0)
m.e505 = Constraint(expr= -(-0.83537 + m.x2)**2 - (-0.54207 + m.x5)**2 + m.x7
    <= 0)
m.e506 = Constraint(expr= -(-0.38603 + m.x2)**2 - (-0.55333 + m.x5)**2 + m.x7
    <= 0)
m.e507 = Constraint(expr= -(-0.90057 + m.x2)**2 - (-0.13927 + m.x5)**2 + m.x7
    <= 0)
m.e508 = Constraint(expr= -(-0.06483 + m.x2)**2 - (-0.74013 + m.x5)**2 + m.x7
    <= 0)
m.e509 = Constraint(expr= -(-0.15777 + m.x2)**2 - (-0.64847 + m.x5)**2 + m.x7
    <= 0)
m.e510 = Constraint(expr= -(-0.79163 + m.x2)**2 - (-0.65493 + m.x5)**2 + m.x7
    <= 0)
m.e511 = Constraint(expr= -(-0.92697 + m.x2)**2 - (-0.58967 + m.x5)**2 + m.x7
    <= 0)
m.e512 = Constraint(expr= -(-0.64643 + m.x2)**2 - (-0.17773 + m.x5)**2 + m.x7
    <= 0)
m.e513 = Constraint(expr= -(-0.72817 + m.x2)**2 - (-0.68287 + m.x5)**2 + m.x7
    <= 0)
m.e514 = Constraint(expr= -(-0.50923 + m.x2)**2 - (-0.98853 + m.x5)**2 + m.x7
    <= 0)
m.e515 = Constraint(expr= -(-0.28137 + m.x2)**2 - (-0.84807 + m.x5)**2 + m.x7
    <= 0)
m.e516 = Constraint(expr= -(-0.06003 + m.x2)**2 - (-0.56733 + m.x5)**2 + m.x7
    <= 0)
m.e517 = Constraint(expr= -(-0.50657 + m.x2)**2 - (-0.20527 + m.x5)**2 + m.x7
    <= 0)
m.e518 = Constraint(expr= -(-0.77883 + m.x2)**2 - (-0.19413 + m.x5)**2 + m.x7
    <= 0)
m.e519 = Constraint(expr= -(-0.52377 + m.x2)**2 - (-0.07447 + m.x5)**2 + m.x7
    <= 0)
m.e520 = Constraint(expr= -(-0.94563 + m.x2)**2 - (-0.94893 + m.x5)**2 + m.x7
    <= 0)
m.e521 = Constraint(expr= -(-0.65297 + m.x2)**2 - (-0.97567 + m.x5)**2 + m.x7
    <= 0)
m.e522 = Constraint(expr= -(-0.64043 + m.x2)**2 - (-0.71173 + m.x5)**2 + m.x7
    <= 0)
m.e523 = Constraint(expr= -(-0.41417 + m.x2)**2 - (-0.62887 + m.x5)**2 + m.x7
    <= 0)
m.e524 = Constraint(expr= -(-0.74323 + m.x2)**2 - (-0.16253 + m.x5)**2 + m.x7
    <= 0)
m.e525 = Constraint(expr= -(-0.52737 + m.x2)**2 - (-0.95407 + m.x5)**2 + m.x7
    <= 0)
m.e526 = Constraint(expr= -(-0.93403 + m.x2)**2 - (-0.78133 + m.x5)**2 + m.x7
    <= 0)
m.e527 = Constraint(expr= -(-0.91257 + m.x2)**2 - (-0.07127 + m.x5)**2 + m.x7
    <= 0)
m.e528 = Constraint(expr= -(-0.69283 + m.x2)**2 - (-0.84813 + m.x5)**2 + m.x7
    <= 0)
m.e529 = Constraint(expr= -(-0.68977 + m.x2)**2 - (-0.30047 + m.x5)**2 + m.x7
    <= 0)
m.e530 = Constraint(expr= -(-0.29963 + m.x2)**2 - (-0.44293 + m.x5)**2 + m.x7
    <= 0)
m.e531 = Constraint(expr= -(-0.17897 + m.x2)**2 - (-0.16167 + m.x5)**2 + m.x7
    <= 0)
m.e532 = Constraint(expr= -(-0.83443 + m.x2)**2 - (-0.44573 + m.x5)**2 + m.x7
    <= 0)
m.e533 = Constraint(expr= -(-0.90017 + m.x2)**2 - (-0.37487 + m.x5)**2 + m.x7
    <= 0)
m.e534 = Constraint(expr= -(-0.17723 + m.x2)**2 - (-0.53653 + m.x5)**2 + m.x7
    <= 0)
m.e535 = Constraint(expr= -(-0.57337 + m.x2)**2 - (-0.86007 + m.x5)**2 + m.x7
    <= 0)
m.e536 = Constraint(expr= -(-0.00803 + m.x2)**2 - (-0.19533 + m.x5)**2 + m.x7
    <= 0)
m.e537 = Constraint(expr= -(-0.11857 + m.x2)**2 - (-0.73727 + m.x5)**2 + m.x7
    <= 0)
m.e538 = Constraint(expr= -(-0.80683 + m.x2)**2 - (-0.70213 + m.x5)**2 + m.x7
    <= 0)
m.e539 = Constraint(expr= -(-0.65577 + m.x2)**2 - (-0.32647 + m.x5)**2 + m.x7
    <= 0)
m.e540 = Constraint(expr= -(-0.85363 + m.x2)**2 - (-0.13693 + m.x5)**2 + m.x7
    <= 0)
m.e541 = Constraint(expr= -(-0.50497 + m.x2)**2 - (-0.14767 + m.x5)**2 + m.x7
    <= 0)
m.e542 = Constraint(expr= -(-0.22843 + m.x2)**2 - (-0.37973 + m.x5)**2 + m.x7
    <= 0)
m.e543 = Constraint(expr= -(-0.18617 + m.x2)**2 - (-0.92087 + m.x5)**2 + m.x7
    <= 0)
m.e544 = Constraint(expr= -(-0.81123 + m.x2)**2 - (-0.11053 + m.x5)**2 + m.x7
    <= 0)
m.e545 = Constraint(expr= -(-0.41937 + m.x2)**2 - (-0.56607 + m.x5)**2 + m.x7
    <= 0)
m.e546 = Constraint(expr= -(-0.28203 + m.x2)**2 - (-0.80933 + m.x5)**2 + m.x7
    <= 0)
m.e547 = Constraint(expr= -(-0.12457 + m.x2)**2 - (-0.20327 + m.x5)**2 + m.x7
    <= 0)
m.e548 = Constraint(expr= -(-0.12083 + m.x2)**2 - (-0.75613 + m.x5)**2 + m.x7
    <= 0)
m.e549 = Constraint(expr= -(-0.42177 + m.x2)**2 - (-0.15247 + m.x5)**2 + m.x7
    <= 0)
m.e550 = Constraint(expr= -(-0.60763 + m.x2)**2 - (-0.03093 + m.x5)**2 + m.x7
    <= 0)
m.e551 = Constraint(expr= -(-0.63097 + m.x2)**2 - (-0.93367 + m.x5)**2 + m.x7
    <= 0)
m.e552 = Constraint(expr= -(-0.82243 + m.x2)**2 - (-0.51373 + m.x5)**2 + m.x7
    <= 0)
m.e553 = Constraint(expr= -(-0.27217 + m.x2)**2 - (-0.26687 + m.x5)**2 + m.x7
    <= 0)
m.e554 = Constraint(expr= -(-0.64523 + m.x2)**2 - (-0.88453 + m.x5)**2 + m.x7
    <= 0)
m.e555 = Constraint(expr= -(-0.06537 + m.x2)**2 - (-0.07207 + m.x5)**2 + m.x7
    <= 0)
m.e556 = Constraint(expr= -(-0.75603 + m.x2)**2 - (-0.62333 + m.x5)**2 + m.x7
    <= 0)
m.e557 = Constraint(expr= -(-0.93057 + m.x2)**2 - (-0.46927 + m.x5)**2 + m.x7
    <= 0)
m.e558 = Constraint(expr= -(-0.63483 + m.x2)**2 - (-0.01013 + m.x5)**2 + m.x7
    <= 0)
m.e559 = Constraint(expr= -(-0.98777 + m.x2)**2 - (-0.77847 + m.x5)**2 + m.x7
    <= 0)
m.e560 = Constraint(expr= -(-0.56163 + m.x2)**2 - (-0.12493 + m.x5)**2 + m.x7
    <= 0)
m.e561 = Constraint(expr= -(-0.55697 + m.x2)**2 - (-0.51967 + m.x5)**2 + m.x7
    <= 0)
m.e562 = Constraint(expr= -(-0.61643 + m.x2)**2 - (-0.84773 + m.x5)**2 + m.x7
    <= 0)
m.e563 = Constraint(expr= -(-0.15817 + m.x2)**2 - (-0.41287 + m.x5)**2 + m.x7
    <= 0)
m.e564 = Constraint(expr= -(-0.67923 + m.x2)**2 - (-0.85853 + m.x5)**2 + m.x7
    <= 0)
m.e565 = Constraint(expr= -(-0.51137 + m.x2)**2 - (-0.37807 + m.x5)**2 + m.x7
    <= 0)
m.e566 = Constraint(expr= -(-0.43003 + m.x2)**2 - (-0.63733 + m.x5)**2 + m.x7
    <= 0)
m.e567 = Constraint(expr= -(-0.53657 + m.x2)**2 - (-0.53527 + m.x5)**2 + m.x7
    <= 0)
m.e568 = Constraint(expr= -(-0.34883 + m.x2)**2 - (-0.46413 + m.x5)**2 + m.x7
    <= 0)
m.e569 = Constraint(expr= -(-0.35377 + m.x2)**2 - (-0.20447 + m.x5)**2 + m.x7
    <= 0)
m.e570 = Constraint(expr= -(-0.71563 + m.x2)**2 - (-0.41893 + m.x5)**2 + m.x7
    <= 0)
m.e571 = Constraint(expr= -(-0.28297 + m.x2)**2 - (-0.90567 + m.x5)**2 + m.x7
    <= 0)
m.e572 = Constraint(expr= -(-0.61043 + m.x2)**2 - (-0.38173 + m.x5)**2 + m.x7
    <= 0)
m.e573 = Constraint(expr= -(-0.84417 + m.x2)**2 - (-0.35887 + m.x5)**2 + m.x7
    <= 0)
m.e574 = Constraint(expr= -(-0.91323 + m.x2)**2 - (-0.03253 + m.x5)**2 + m.x7
    <= 0)
m.e575 = Constraint(expr= -(-0.75737 + m.x2)**2 - (-0.48407 + m.x5)**2 + m.x7
    <= 0)
m.e576 = Constraint(expr= -(-0.30403 + m.x2)**2 - (-0.85133 + m.x5)**2 + m.x7
    <= 0)
m.e577 = Constraint(expr= -(-0.94257 + m.x2)**2 - (-0.40127 + m.x5)**2 + m.x7
    <= 0)
m.e578 = Constraint(expr= -(-0.26283 + m.x2)**2 - (-0.11813 + m.x5)**2 + m.x7
    <= 0)
m.e579 = Constraint(expr= -(-0.51977 + m.x2)**2 - (-0.43047 + m.x5)**2 + m.x7
    <= 0)
m.e580 = Constraint(expr= -(-0.06963 + m.x2)**2 - (-0.91293 + m.x5)**2 + m.x7
    <= 0)
m.e581 = Constraint(expr= -(-0.80897 + m.x2)**2 - (-0.09167 + m.x5)**2 + m.x7
    <= 0)
m.e582 = Constraint(expr= -(-0.80443 + m.x2)**2 - (-0.11573 + m.x5)**2 + m.x7
    <= 0)
m.e583 = Constraint(expr= -(-0.33017 + m.x2)**2 - (-0.10487 + m.x5)**2 + m.x7
    <= 0)
m.e584 = Constraint(expr= -(-0.34723 + m.x2)**2 - (-0.40653 + m.x5)**2 + m.x7
    <= 0)
m.e585 = Constraint(expr= -(-0.80337 + m.x2)**2 - (-0.39007 + m.x5)**2 + m.x7
    <= 0)
m.e586 = Constraint(expr= -(-0.37803 + m.x2)**2 - (-0.26533 + m.x5)**2 + m.x7
    <= 0)
m.e587 = Constraint(expr= -(-0.14857 + m.x2)**2 - (-0.06727 + m.x5)**2 + m.x7
    <= 0)
m.e588 = Constraint(expr= -(-0.37683 + m.x2)**2 - (-0.97213 + m.x5)**2 + m.x7
    <= 0)
m.e589 = Constraint(expr= -(-0.48577 + m.x2)**2 - (-0.45647 + m.x5)**2 + m.x7
    <= 0)
m.e590 = Constraint(expr= -(-0.62363 + m.x2)**2 - (-0.60693 + m.x5)**2 + m.x7
    <= 0)
m.e591 = Constraint(expr= -(-0.13497 + m.x2)**2 - (-0.07767 + m.x5)**2 + m.x7
    <= 0)
m.e592 = Constraint(expr= -(-0.19843 + m.x2)**2 - (-0.04973 + m.x5)**2 + m.x7
    <= 0)
m.e593 = Constraint(expr= -(-0.61617 + m.x2)**2 - (-0.65087 + m.x5)**2 + m.x7
    <= 0)
m.e594 = Constraint(expr= -(-0.98123 + m.x2)**2 - (-0.98053 + m.x5)**2 + m.x7
    <= 0)
m.e595 = Constraint(expr= -(-0.64937 + m.x2)**2 - (-0.09607 + m.x5)**2 + m.x7
    <= 0)
m.e596 = Constraint(expr= -(-0.65203 + m.x2)**2 - (-0.87933 + m.x5)**2 + m.x7
    <= 0)
m.e597 = Constraint(expr= -(-0.15457 + m.x2)**2 - (-0.53327 + m.x5)**2 + m.x7
    <= 0)
m.e598 = Constraint(expr= -(-0.69083 + m.x2)**2 - (-0.02613 + m.x5)**2 + m.x7
    <= 0)
m.e599 = Constraint(expr= -(-0.25177 + m.x2)**2 - (-0.28247 + m.x5)**2 + m.x7
    <= 0)
m.e600 = Constraint(expr= -(-0.37763 + m.x2)**2 - (-0.50093 + m.x5)**2 + m.x7
    <= 0)
m.e601 = Constraint(expr= -(-0.26097 + m.x2)**2 - (-0.86367 + m.x5)**2 + m.x7
    <= 0)
m.e602 = Constraint(expr= -(-0.79243 + m.x2)**2 - (-0.18373 + m.x5)**2 + m.x7
    <= 0)
m.e603 = Constraint(expr= -(-0.70217 + m.x2)**2 - (-0.99687 + m.x5)**2 + m.x7
    <= 0)
m.e604 = Constraint(expr= -(-0.81523 + m.x2)**2 - (-0.75453 + m.x5)**2 + m.x7
    <= 0)
m.e605 = Constraint(expr= -(-0.29537 + m.x2)**2 - (-0.60207 + m.x5)**2 + m.x7
    <= 0)
m.e606 = Constraint(expr= -(-0.12603 + m.x2)**2 - (-0.69333 + m.x5)**2 + m.x7
    <= 0)
m.e607 = Constraint(expr= -(-0.96057 + m.x2)**2 - (-0.79927 + m.x5)**2 + m.x7
    <= 0)
m.e608 = Constraint(expr= -(-0.20483 + m.x2)**2 - (-0.28013 + m.x5)**2 + m.x7
    <= 0)
m.e609 = Constraint(expr= -(-0.81777 + m.x2)**2 - (-0.90847 + m.x5)**2 + m.x7
    <= 0)
m.e610 = Constraint(expr= -(-0.33163 + m.x2)**2 - (-0.59493 + m.x5)**2 + m.x7
    <= 0)
m.e611 = Constraint(expr= -(-0.18697 + m.x2)**2 - (-0.44967 + m.x5)**2 + m.x7
    <= 0)
m.e612 = Constraint(expr= -(-0.58643 + m.x2)**2 - (-0.51773 + m.x5)**2 + m.x7
    <= 0)
m.e613 = Constraint(expr= -(-0.58817 + m.x2)**2 - (-0.14287 + m.x5)**2 + m.x7
    <= 0)
m.e614 = Constraint(expr= -(-0.84923 + m.x2)**2 - (-0.72853 + m.x5)**2 + m.x7
    <= 0)
m.e615 = Constraint(expr= -(-0.74137 + m.x2)**2 - (-0.90807 + m.x5)**2 + m.x7
    <= 0)
m.e616 = Constraint(expr= -(-0.80003 + m.x2)**2 - (-0.70733 + m.x5)**2 + m.x7
    <= 0)
m.e617 = Constraint(expr= -(-0.56657 + m.x2)**2 - (-0.86527 + m.x5)**2 + m.x7
    <= 0)
m.e618 = Constraint(expr= -(-0.91883 + m.x2)**2 - (-0.73413 + m.x5)**2 + m.x7
    <= 0)
m.e619 = Constraint(expr= -(-0.18377 + m.x2)**2 - (-0.33447 + m.x5)**2 + m.x7
    <= 0)
m.e620 = Constraint(expr= -(-0.48563 + m.x2)**2 - (-0.88893 + m.x5)**2 + m.x7
    <= 0)
m.e621 = Constraint(expr= -(-0.91297 + m.x2)**2 - (-0.83567 + m.x5)**2 + m.x7
    <= 0)
m.e622 = Constraint(expr= -(-0.58043 + m.x2)**2 - (-0.05173 + m.x5)**2 + m.x7
    <= 0)
m.e623 = Constraint(expr= -(-0.27417 + m.x2)**2 - (-0.08887 + m.x5)**2 + m.x7
    <= 0)
m.e624 = Constraint(expr= -(-0.08323 + m.x2)**2 - (-0.90253 + m.x5)**2 + m.x7
    <= 0)
m.e625 = Constraint(expr= -(-0.98737 + m.x2)**2 - (-0.01407 + m.x5)**2 + m.x7
    <= 0)
m.e626 = Constraint(expr= -(-0.67403 + m.x2)**2 - (-0.92133 + m.x5)**2 + m.x7
    <= 0)
m.e627 = Constraint(expr= -(-0.97257 + m.x2)**2 - (-0.73127 + m.x5)**2 + m.x7
    <= 0)
m.e628 = Constraint(expr= -(-0.83283 + m.x2)**2 - (-0.38813 + m.x5)**2 + m.x7
    <= 0)
m.e629 = Constraint(expr= -(-0.34977 + m.x2)**2 - (-0.56047 + m.x5)**2 + m.x7
    <= 0)
m.e630 = Constraint(expr= -(-0.83963 + m.x2)**2 - (-0.38293 + m.x5)**2 + m.x7
    <= 0)
m.e631 = Constraint(expr= -(-0.43897 + m.x2)**2 - (-0.02167 + m.x5)**2 + m.x7
    <= 0)
m.e632 = Constraint(expr= -(-0.77443 + m.x2)**2 - (-0.78573 + m.x5)**2 + m.x7
    <= 0)
m.e633 = Constraint(expr= -(-0.76017 + m.x2)**2 - (-0.83487 + m.x5)**2 + m.x7
    <= 0)
m.e634 = Constraint(expr= -(-0.51723 + m.x2)**2 - (-0.27653 + m.x5)**2 + m.x7
    <= 0)
m.e635 = Constraint(expr= -(-0.03337 + m.x2)**2 - (-0.92007 + m.x5)**2 + m.x7
    <= 0)
m.e636 = Constraint(expr= -(-0.74803 + m.x2)**2 - (-0.33533 + m.x5)**2 + m.x7
    <= 0)
m.e637 = Constraint(expr= -(-0.17857 + m.x2)**2 - (-0.39727 + m.x5)**2 + m.x7
    <= 0)
m.e638 = Constraint(expr= -(-0.94683 + m.x2)**2 - (-0.24213 + m.x5)**2 + m.x7
    <= 0)
m.e639 = Constraint(expr= -(-0.31577 + m.x2)**2 - (-0.58647 + m.x5)**2 + m.x7
    <= 0)
m.e640 = Constraint(expr= -(-0.39363 + m.x2)**2 - (-0.07693 + m.x5)**2 + m.x7
    <= 0)
m.e641 = Constraint(expr= -(-0.76497 + m.x2)**2 - (-0.00767 + m.x5)**2 + m.x7
    <= 0)
m.e642 = Constraint(expr= -(-0.16843 + m.x2)**2 - (-0.71973 + m.x5)**2 + m.x7
    <= 0)
m.e643 = Constraint(expr= -(-0.04617 + m.x2)**2 - (-0.38087 + m.x5)**2 + m.x7
    <= 0)
m.e644 = Constraint(expr= -(-0.15123 + m.x2)**2 - (-0.85053 + m.x5)**2 + m.x7
    <= 0)
m.e645 = Constraint(expr= -(-0.87937 + m.x2)**2 - (-0.62607 + m.x5)**2 + m.x7
    <= 0)
m.e646 = Constraint(expr= -(-0.02203 + m.x2)**2 - (-0.94933 + m.x5)**2 + m.x7
    <= 0)
m.e647 = Constraint(expr= -(-0.18457 + m.x2)**2 - (-0.86327 + m.x5)**2 + m.x7
    <= 0)
m.e648 = Constraint(expr= -(-0.26083 + m.x2)**2 - (-0.29613 + m.x5)**2 + m.x7
    <= 0)
m.e649 = Constraint(expr= -(-0.08177 + m.x2)**2 - (-0.41247 + m.x5)**2 + m.x7
    <= 0)
m.e650 = Constraint(expr= -(-0.14763 + m.x2)**2 - (-0.97093 + m.x5)**2 + m.x7
    <= 0)
m.e651 = Constraint(expr= -(-0.89097 + m.x2)**2 - (-0.79367 + m.x5)**2 + m.x7
    <= 0)
m.e652 = Constraint(expr= -(-0.76243 + m.x2)**2 - (-0.85373 + m.x5)**2 + m.x7
    <= 0)
m.e653 = Constraint(expr= -(-0.13217 + m.x2)**2 - (-0.72687 + m.x5)**2 + m.x7
    <= 0)
m.e654 = Constraint(expr= -(-0.98523 + m.x2)**2 - (-0.62453 + m.x5)**2 + m.x7
    <= 0)
m.e655 = Constraint(expr= -(-0.52537 + m.x2)**2 - (-0.13207 + m.x5)**2 + m.x7
    <= 0)
m.e656 = Constraint(expr= -(-0.49603 + m.x2)**2 - (-0.76333 + m.x5)**2 + m.x7
    <= 0)
m.e657 = Constraint(expr= -(-0.99057 + m.x2)**2 - (-0.12927 + m.x5)**2 + m.x7
    <= 0)
m.e658 = Constraint(expr= -(-0.77483 + m.x2)**2 - (-0.55013 + m.x5)**2 + m.x7
    <= 0)
m.e659 = Constraint(expr= -(-0.64777 + m.x2)**2 - (-0.03847 + m.x5)**2 + m.x7
    <= 0)
m.e660 = Constraint(expr= -(-0.10163 + m.x2)**2 - (-0.06493 + m.x5)**2 + m.x7
    <= 0)
m.e661 = Constraint(expr= -(-0.81697 + m.x2)**2 - (-0.37967 + m.x5)**2 + m.x7
    <= 0)
m.e662 = Constraint(expr= -(-0.55643 + m.x2)**2 - (-0.18773 + m.x5)**2 + m.x7
    <= 0)
m.e663 = Constraint(expr= -(-0.01817 + m.x2)**2 - (-0.87287 + m.x5)**2 + m.x7
    <= 0)
m.e664 = Constraint(expr= -(-0.01923 + m.x2)**2 - (-0.59853 + m.x5)**2 + m.x7
    <= 0)
m.e665 = Constraint(expr= -(-0.97137 + m.x2)**2 - (-0.43807 + m.x5)**2 + m.x7
    <= 0)
m.e666 = Constraint(expr= -(-0.17003 + m.x2)**2 - (-0.77733 + m.x5)**2 + m.x7
    <= 0)
m.e667 = Constraint(expr= -(-0.59657 + m.x2)**2 - (-0.19527 + m.x5)**2 + m.x7
    <= 0)
m.e668 = Constraint(expr= -(-0.48883 + m.x2)**2 - (-0.00413 + m.x5)**2 + m.x7
    <= 0)
m.e669 = Constraint(expr= -(-0.01377 + m.x2)**2 - (-0.46447 + m.x5)**2 + m.x7
    <= 0)
m.e670 = Constraint(expr= -(-0.25563 + m.x2)**2 - (-0.35893 + m.x5)**2 + m.x7
    <= 0)
m.e671 = Constraint(expr= -(-0.54297 + m.x2)**2 - (-0.76567 + m.x5)**2 + m.x7
    <= 0)
m.e672 = Constraint(expr= -(-0.55043 + m.x2)**2 - (-0.72173 + m.x5)**2 + m.x7
    <= 0)
m.e673 = Constraint(expr= -(-0.70417 + m.x2)**2 - (-0.81887 + m.x5)**2 + m.x7
    <= 0)
m.e674 = Constraint(expr= -(-0.25323 + m.x2)**2 - (-0.77253 + m.x5)**2 + m.x7
    <= 0)
m.e675 = Constraint(expr= -(-0.21737 + m.x2)**2 - (-0.54407 + m.x5)**2 + m.x7
    <= 0)
m.e676 = Constraint(expr= -(-0.04403 + m.x2)**2 - (-0.99133 + m.x5)**2 + m.x7
    <= 0)
m.e677 = Constraint(expr= -(-0.00257 + m.x2)**2 - (-0.06127 + m.x5)**2 + m.x7
    <= 0)
m.e678 = Constraint(expr= -(-0.40283 + m.x2)**2 - (-0.65813 + m.x5)**2 + m.x7
    <= 0)
m.e679 = Constraint(expr= -(-0.17977 + m.x2)**2 - (-0.69047 + m.x5)**2 + m.x7
    <= 0)
m.e680 = Constraint(expr= -(-0.60963 + m.x2)**2 - (-0.85293 + m.x5)**2 + m.x7
    <= 0)
m.e681 = Constraint(expr= -(-0.06897 + m.x2)**2 - (-0.95167 + m.x5)**2 + m.x7
    <= 0)
m.e682 = Constraint(expr= -(-0.74443 + m.x2)**2 - (-0.45573 + m.x5)**2 + m.x7
    <= 0)
m.e683 = Constraint(expr= -(-0.19017 + m.x2)**2 - (-0.56487 + m.x5)**2 + m.x7
    <= 0)
m.e684 = Constraint(expr= -(-0.68723 + m.x2)**2 - (-0.14653 + m.x5)**2 + m.x7
    <= 0)
m.e685 = Constraint(expr= -(-0.26337 + m.x2)**2 - (-0.45007 + m.x5)**2 + m.x7
    <= 0)
m.e686 = Constraint(expr= -(-0.11803 + m.x2)**2 - (-0.40533 + m.x5)**2 + m.x7
    <= 0)
m.e687 = Constraint(expr= -(-0.20857 + m.x2)**2 - (-0.72727 + m.x5)**2 + m.x7
    <= 0)
m.e688 = Constraint(expr= -(-0.51683 + m.x2)**2 - (-0.51213 + m.x5)**2 + m.x7
    <= 0)
m.e689 = Constraint(expr= -(-0.14577 + m.x2)**2 - (-0.71647 + m.x5)**2 + m.x7
    <= 0)
m.e690 = Constraint(expr= -(-0.16363 + m.x2)**2 - (-0.54693 + m.x5)**2 + m.x7
    <= 0)
m.e691 = Constraint(expr= -(-0.39497 + m.x2)**2 - (-0.93767 + m.x5)**2 + m.x7
    <= 0)
m.e692 = Constraint(expr= -(-0.13843 + m.x2)**2 - (-0.38973 + m.x5)**2 + m.x7
    <= 0)
m.e693 = Constraint(expr= -(-0.47617 + m.x2)**2 - (-0.11087 + m.x5)**2 + m.x7
    <= 0)
m.e694 = Constraint(expr= -(-0.32123 + m.x2)**2 - (-0.72053 + m.x5)**2 + m.x7
    <= 0)
m.e695 = Constraint(expr= -(-0.10937 + m.x2)**2 - (-0.15607 + m.x5)**2 + m.x7
    <= 0)
m.e696 = Constraint(expr= -(-0.39203 + m.x2)**2 - (-0.01933 + m.x5)**2 + m.x7
    <= 0)
m.e697 = Constraint(expr= -(-0.21457 + m.x2)**2 - (-0.19327 + m.x5)**2 + m.x7
    <= 0)
m.e698 = Constraint(expr= -(-0.83083 + m.x2)**2 - (-0.56613 + m.x5)**2 + m.x7
    <= 0)
m.e699 = Constraint(expr= -(-0.91177 + m.x2)**2 - (-0.54247 + m.x5)**2 + m.x7
    <= 0)
m.e700 = Constraint(expr= -(-0.91763 + m.x2)**2 - (-0.44093 + m.x5)**2 + m.x7
    <= 0)
m.e701 = Constraint(expr= -(-0.52097 + m.x2)**2 - (-0.72367 + m.x5)**2 + m.x7
    <= 0)
m.e702 = Constraint(expr= -(-0.73243 + m.x2)**2 - (-0.52373 + m.x5)**2 + m.x7
    <= 0)
m.e703 = Constraint(expr= -(-0.56217 + m.x2)**2 - (-0.45687 + m.x5)**2 + m.x7
    <= 0)
m.e704 = Constraint(expr= -(-0.15523 + m.x2)**2 - (-0.49453 + m.x5)**2 + m.x7
    <= 0)
m.e705 = Constraint(expr= -(-0.75537 + m.x2)**2 - (-0.66207 + m.x5)**2 + m.x7
    <= 0)
m.e706 = Constraint(expr= -(-0.86603 + m.x2)**2 - (-0.83333 + m.x5)**2 + m.x7
    <= 0)
m.e707 = Constraint(expr= -(-0.02057 + m.x2)**2 - (-0.45927 + m.x5)**2 + m.x7
    <= 0)
m.e708 = Constraint(expr= -(-0.34483 + m.x2)**2 - (-0.82013 + m.x5)**2 + m.x7
    <= 0)
m.e709 = Constraint(expr= -(-0.47777 + m.x2)**2 - (-0.16847 + m.x5)**2 + m.x7
    <= 0)
m.e710 = Constraint(expr= -(-0.87163 + m.x2)**2 - (-0.53493 + m.x5)**2 + m.x7
    <= 0)
m.e711 = Constraint(expr= -(-0.44697 + m.x2)**2 - (-0.30967 + m.x5)**2 + m.x7
    <= 0)
m.e712 = Constraint(expr= -(-0.52643 + m.x2)**2 - (-0.85773 + m.x5)**2 + m.x7
    <= 0)
m.e713 = Constraint(expr= -(-0.44817 + m.x2)**2 - (-0.60287 + m.x5)**2 + m.x7
    <= 0)
m.e714 = Constraint(expr= -(-0.18923 + m.x2)**2 - (-0.46853 + m.x5)**2 + m.x7
    <= 0)
m.e715 = Constraint(expr= -(-0.20137 + m.x2)**2 - (-0.96807 + m.x5)**2 + m.x7
    <= 0)
m.e716 = Constraint(expr= -(-0.54003 + m.x2)**2 - (-0.84733 + m.x5)**2 + m.x7
    <= 0)
m.e717 = Constraint(expr= -(-0.62657 + m.x2)**2 - (-0.52527 + m.x5)**2 + m.x7
    <= 0)
m.e718 = Constraint(expr= -(-0.05883 + m.x2)**2 - (-0.27413 + m.x5)**2 + m.x7
    <= 0)
m.e719 = Constraint(expr= -(-0.84377 + m.x2)**2 - (-0.59447 + m.x5)**2 + m.x7
    <= 0)
m.e720 = Constraint(expr= -(-0.02563 + m.x2)**2 - (-0.82893 + m.x5)**2 + m.x7
    <= 0)
m.e721 = Constraint(expr= -(-0.17297 + m.x2)**2 - (-0.69567 + m.x5)**2 + m.x7
    <= 0)
m.e722 = Constraint(expr= -(-0.52043 + m.x2)**2 - (-0.39173 + m.x5)**2 + m.x7
    <= 0)
m.e723 = Constraint(expr= -(-0.13417 + m.x2)**2 - (-0.54887 + m.x5)**2 + m.x7
    <= 0)
m.e724 = Constraint(expr= -(-0.42323 + m.x2)**2 - (-0.64253 + m.x5)**2 + m.x7
    <= 0)
m.e725 = Constraint(expr= -(-0.44737 + m.x2)**2 - (-0.07407 + m.x5)**2 + m.x7
    <= 0)
m.e726 = Constraint(expr= -(-0.41403 + m.x2)**2 - (-0.06133 + m.x5)**2 + m.x7
    <= 0)
m.e727 = Constraint(expr= -(-0.03257 + m.x2)**2 - (-0.39127 + m.x5)**2 + m.x7
    <= 0)
m.e728 = Constraint(expr= -(-0.97283 + m.x2)**2 - (-0.92813 + m.x5)**2 + m.x7
    <= 0)
m.e729 = Constraint(expr= -(-0.00977 + m.x2)**2 - (-0.82047 + m.x5)**2 + m.x7
    <= 0)
m.e730 = Constraint(expr= -(-0.37963 + m.x2)**2 - (-0.32293 + m.x5)**2 + m.x7
    <= 0)
m.e731 = Constraint(expr= -(-0.69897 + m.x2)**2 - (-0.88167 + m.x5)**2 + m.x7
    <= 0)
m.e732 = Constraint(expr= -(-0.71443 + m.x2)**2 - (-0.12573 + m.x5)**2 + m.x7
    <= 0)
m.e733 = Constraint(expr= -(-0.62017 + m.x2)**2 - (-0.29487 + m.x5)**2 + m.x7
    <= 0)
m.e734 = Constraint(expr= -(-0.85723 + m.x2)**2 - (-0.01653 + m.x5)**2 + m.x7
    <= 0)
m.e735 = Constraint(expr= -(-0.49337 + m.x2)**2 - (-0.98007 + m.x5)**2 + m.x7
    <= 0)
m.e736 = Constraint(expr= -(-0.48803 + m.x2)**2 - (-0.47533 + m.x5)**2 + m.x7
    <= 0)
m.e737 = Constraint(expr= -(-0.23857 + m.x2)**2 - (-0.05727 + m.x5)**2 + m.x7
    <= 0)
m.e738 = Constraint(expr= -(-0.08683 + m.x2)**2 - (-0.78213 + m.x5)**2 + m.x7
    <= 0)
m.e739 = Constraint(expr= -(-0.97577 + m.x2)**2 - (-0.84647 + m.x5)**2 + m.x7
    <= 0)
m.e740 = Constraint(expr= -(-0.93363 + m.x2)**2 - (-0.01693 + m.x5)**2 + m.x7
    <= 0)
m.e741 = Constraint(expr= -(-0.02497 + m.x2)**2 - (-0.86767 + m.x5)**2 + m.x7
    <= 0)
m.e742 = Constraint(expr= -(-0.10843 + m.x2)**2 - (-0.05973 + m.x5)**2 + m.x7
    <= 0)
m.e743 = Constraint(expr= -(-0.90617 + m.x2)**2 - (-0.84087 + m.x5)**2 + m.x7
    <= 0)
m.e744 = Constraint(expr= -(-0.49123 + m.x2)**2 - (-0.59053 + m.x5)**2 + m.x7
    <= 0)
m.e745 = Constraint(expr= -(-0.33937 + m.x2)**2 - (-0.68607 + m.x5)**2 + m.x7
    <= 0)
m.e746 = Constraint(expr= -(-0.76203 + m.x2)**2 - (-0.08933 + m.x5)**2 + m.x7
    <= 0)
m.e747 = Constraint(expr= -(-0.24457 + m.x2)**2 - (-0.52327 + m.x5)**2 + m.x7
    <= 0)
m.e748 = Constraint(expr= -(-0.40083 + m.x2)**2 - (-0.83613 + m.x5)**2 + m.x7
    <= 0)
m.e749 = Constraint(expr= -(-0.74177 + m.x2)**2 - (-0.67247 + m.x5)**2 + m.x7
    <= 0)
m.e750 = Constraint(expr= -(-0.68763 + m.x2)**2 - (-0.91093 + m.x5)**2 + m.x7
    <= 0)
m.e751 = Constraint(expr= -(-0.15097 + m.x2)**2 - (-0.65367 + m.x5)**2 + m.x7
    <= 0)
m.e752 = Constraint(expr= -(-0.70243 + m.x2)**2 - (-0.19373 + m.x5)**2 + m.x7
    <= 0)
m.e753 = Constraint(expr= -(-0.99217 + m.x2)**2 - (-0.18687 + m.x5)**2 + m.x7
    <= 0)
m.e754 = Constraint(expr= -(-0.32523 + m.x2)**2 - (-0.36453 + m.x5)**2 + m.x7
    <= 0)
m.e755 = Constraint(expr= -(-0.98537 + m.x2)**2 - (-0.19207 + m.x5)**2 + m.x7
    <= 0)
m.e756 = Constraint(expr= -(-0.23603 + m.x2)**2 - (-0.90333 + m.x5)**2 + m.x7
    <= 0)
m.e757 = Constraint(expr= -(-0.05057 + m.x2)**2 - (-0.78927 + m.x5)**2 + m.x7
    <= 0)
m.e758 = Constraint(expr= -(-0.91483 + m.x2)**2 - (-0.09013 + m.x5)**2 + m.x7
    <= 0)
m.e759 = Constraint(expr= -(-0.30777 + m.x2)**2 - (-0.29847 + m.x5)**2 + m.x7
    <= 0)
m.e760 = Constraint(expr= -(-0.64163 + m.x2)**2 - (-0.00493 + m.x5)**2 + m.x7
    <= 0)
m.e761 = Constraint(expr= -(-0.07697 + m.x2)**2 - (-0.23967 + m.x5)**2 + m.x7
    <= 0)
m.e762 = Constraint(expr= -(-0.49643 + m.x2)**2 - (-0.52773 + m.x5)**2 + m.x7
    <= 0)
m.e763 = Constraint(expr= -(-0.87817 + m.x2)**2 - (-0.33287 + m.x5)**2 + m.x7
    <= 0)
m.e764 = Constraint(expr= -(-0.35923 + m.x2)**2 - (-0.33853 + m.x5)**2 + m.x7
    <= 0)
m.e765 = Constraint(expr= -(-0.43137 + m.x2)**2 - (-0.49807 + m.x5)**2 + m.x7
    <= 0)
m.e766 = Constraint(expr= -(-0.91003 + m.x2)**2 - (-0.91733 + m.x5)**2 + m.x7
    <= 0)
m.e767 = Constraint(expr= -(-0.65657 + m.x2)**2 - (-0.85527 + m.x5)**2 + m.x7
    <= 0)
m.e768 = Constraint(expr= -(-0.62883 + m.x2)**2 - (-0.54413 + m.x5)**2 + m.x7
    <= 0)
m.e769 = Constraint(expr= -(-0.67377 + m.x2)**2 - (-0.72447 + m.x5)**2 + m.x7
    <= 0)
m.e770 = Constraint(expr= -(-0.79563 + m.x2)**2 - (-0.29893 + m.x5)**2 + m.x7
    <= 0)
m.e771 = Constraint(expr= -(-0.80297 + m.x2)**2 - (-0.62567 + m.x5)**2 + m.x7
    <= 0)
m.e772 = Constraint(expr= -(-0.49043 + m.x2)**2 - (-0.06173 + m.x5)**2 + m.x7
    <= 0)
m.e773 = Constraint(expr= -(-0.56417 + m.x2)**2 - (-0.27887 + m.x5)**2 + m.x7
    <= 0)
m.e774 = Constraint(expr= -(-0.59323 + m.x2)**2 - (-0.51253 + m.x5)**2 + m.x7
    <= 0)
m.e775 = Constraint(expr= -(-0.67737 + m.x2)**2 - (-0.60407 + m.x5)**2 + m.x7
    <= 0)
m.e776 = Constraint(expr= -(-0.78403 + m.x2)**2 - (-0.13133 + m.x5)**2 + m.x7
    <= 0)
m.e777 = Constraint(expr= -(-0.06257 + m.x2)**2 - (-0.72127 + m.x5)**2 + m.x7
    <= 0)
m.e778 = Constraint(expr= -(-0.54283 + m.x2)**2 - (-0.19813 + m.x5)**2 + m.x7
    <= 0)
m.e779 = Constraint(expr= -(-0.83977 + m.x2)**2 - (-0.95047 + m.x5)**2 + m.x7
    <= 0)
m.e780 = Constraint(expr= -(-0.14963 + m.x2)**2 - (-0.79293 + m.x5)**2 + m.x7
    <= 0)
m.e781 = Constraint(expr= -(-0.32897 + m.x2)**2 - (-0.81167 + m.x5)**2 + m.x7
    <= 0)
m.e782 = Constraint(expr= -(-0.68443 + m.x2)**2 - (-0.79573 + m.x5)**2 + m.x7
    <= 0)
m.e783 = Constraint(expr= -(-0.05017 + m.x2)**2 - (-0.02487 + m.x5)**2 + m.x7
    <= 0)
m.e784 = Constraint(expr= -(-0.02723 + m.x2)**2 - (-0.88653 + m.x5)**2 + m.x7
    <= 0)
m.e785 = Constraint(expr= -(-0.72337 + m.x2)**2 - (-0.51007 + m.x5)**2 + m.x7
    <= 0)
m.e786 = Constraint(expr= -(-0.85803 + m.x2)**2 - (-0.54533 + m.x5)**2 + m.x7
    <= 0)
m.e787 = Constraint(expr= -(-0.26857 + m.x2)**2 - (-0.38727 + m.x5)**2 + m.x7
    <= 0)
m.e788 = Constraint(expr= -(-0.65683 + m.x2)**2 - (-0.05213 + m.x5)**2 + m.x7
    <= 0)
m.e789 = Constraint(expr= -(-0.80577 + m.x2)**2 - (-0.97647 + m.x5)**2 + m.x7
    <= 0)
m.e790 = Constraint(expr= -(-0.70363 + m.x2)**2 - (-0.48693 + m.x5)**2 + m.x7
    <= 0)
m.e791 = Constraint(expr= -(-0.65497 + m.x2)**2 - (-0.79767 + m.x5)**2 + m.x7
    <= 0)
m.e792 = Constraint(expr= -(-0.07843 + m.x2)**2 - (-0.72973 + m.x5)**2 + m.x7
    <= 0)
m.e793 = Constraint(expr= -(-0.33617 + m.x2)**2 - (-0.57087 + m.x5)**2 + m.x7
    <= 0)
m.e794 = Constraint(expr= -(-0.66123 + m.x2)**2 - (-0.46053 + m.x5)**2 + m.x7
    <= 0)
m.e795 = Constraint(expr= -(-0.56937 + m.x2)**2 - (-0.21607 + m.x5)**2 + m.x7
    <= 0)
m.e796 = Constraint(expr= -(-0.13203 + m.x2)**2 - (-0.15933 + m.x5)**2 + m.x7
    <= 0)
m.e797 = Constraint(expr= -(-0.27457 + m.x2)**2 - (-0.85327 + m.x5)**2 + m.x7
    <= 0)
m.e798 = Constraint(expr= -(-0.97083 + m.x2)**2 - (-0.10613 + m.x5)**2 + m.x7
    <= 0)
m.e799 = Constraint(expr= -(-0.57177 + m.x2)**2 - (-0.80247 + m.x5)**2 + m.x7
    <= 0)
m.e800 = Constraint(expr= -(-0.45763 + m.x2)**2 - (-0.38093 + m.x5)**2 + m.x7
    <= 0)
m.e801 = Constraint(expr= -(-0.78097 + m.x2)**2 - (-0.58367 + m.x5)**2 + m.x7
    <= 0)
m.e802 = Constraint(expr= -(-0.67243 + m.x2)**2 - (-0.86373 + m.x5)**2 + m.x7
    <= 0)
m.e803 = Constraint(expr= -(-0.42217 + m.x2)**2 - (-0.91687 + m.x5)**2 + m.x7
    <= 0)
m.e804 = Constraint(expr= -(-0.49523 + m.x2)**2 - (-0.23453 + m.x5)**2 + m.x7
    <= 0)
m.e805 = Constraint(expr= -(-0.21537 + m.x2)**2 - (-0.72207 + m.x5)**2 + m.x7
    <= 0)
m.e806 = Constraint(expr= -(-0.60603 + m.x2)**2 - (-0.97333 + m.x5)**2 + m.x7
    <= 0)
m.e807 = Constraint(expr= -(-0.08057 + m.x2)**2 - (-0.11927 + m.x5)**2 + m.x7
    <= 0)
m.e808 = Constraint(expr= -(-0.48483 + m.x2)**2 - (-0.36013 + m.x5)**2 + m.x7
    <= 0)
m.e809 = Constraint(expr= -(-0.13777 + m.x2)**2 - (-0.42847 + m.x5)**2 + m.x7
    <= 0)
m.e810 = Constraint(expr= -(-0.41163 + m.x2)**2 - (-0.47493 + m.x5)**2 + m.x7
    <= 0)
m.e811 = Constraint(expr= -(-0.70697 + m.x2)**2 - (-0.16967 + m.x5)**2 + m.x7
    <= 0)
m.e812 = Constraint(expr= -(-0.46643 + m.x2)**2 - (-0.19773 + m.x5)**2 + m.x7
    <= 0)
m.e813 = Constraint(expr= -(-0.30817 + m.x2)**2 - (-0.06287 + m.x5)**2 + m.x7
    <= 0)
m.e814 = Constraint(expr= -(-0.52923 + m.x2)**2 - (-0.20853 + m.x5)**2 + m.x7
    <= 0)
m.e815 = Constraint(expr= -(-0.66137 + m.x2)**2 - (-0.02807 + m.x5)**2 + m.x7
    <= 0)
m.e816 = Constraint(expr= -(-0.28003 + m.x2)**2 - (-0.98733 + m.x5)**2 + m.x7
    <= 0)
m.e817 = Constraint(expr= -(-0.68657 + m.x2)**2 - (-0.18527 + m.x5)**2 + m.x7
    <= 0)
m.e818 = Constraint(expr= -(-0.19883 + m.x2)**2 - (-0.81413 + m.x5)**2 + m.x7
    <= 0)
m.e819 = Constraint(expr= -(-0.50377 + m.x2)**2 - (-0.85447 + m.x5)**2 + m.x7
    <= 0)
m.e820 = Constraint(expr= -(-0.56563 + m.x2)**2 - (-0.76893 + m.x5)**2 + m.x7
    <= 0)
m.e821 = Constraint(expr= -(-0.43297 + m.x2)**2 - (-0.55567 + m.x5)**2 + m.x7
    <= 0)
m.e822 = Constraint(expr= -(-0.46043 + m.x2)**2 - (-0.73173 + m.x5)**2 + m.x7
    <= 0)
m.e823 = Constraint(expr= -(-0.99417 + m.x2)**2 - (-0.00887 + m.x5)**2 + m.x7
    <= 0)
m.e824 = Constraint(expr= -(-0.76323 + m.x2)**2 - (-0.38253 + m.x5)**2 + m.x7
    <= 0)
m.e825 = Constraint(expr= -(-0.90737 + m.x2)**2 - (-0.13407 + m.x5)**2 + m.x7
    <= 0)
m.e826 = Constraint(expr= -(-0.15403 + m.x2)**2 - (-0.20133 + m.x5)**2 + m.x7
    <= 0)
m.e827 = Constraint(expr= -(-0.09257 + m.x2)**2 - (-0.05127 + m.x5)**2 + m.x7
    <= 0)
m.e828 = Constraint(expr= -(-0.11283 + m.x2)**2 - (-0.46813 + m.x5)**2 + m.x7
    <= 0)
m.e829 = Constraint(expr= -(-0.66977 + m.x2)**2 - (-0.08047 + m.x5)**2 + m.x7
    <= 0)
m.e830 = Constraint(expr= -(-0.91963 + m.x2)**2 - (-0.26293 + m.x5)**2 + m.x7
    <= 0)
m.e831 = Constraint(expr= -(-0.95897 + m.x2)**2 - (-0.74167 + m.x5)**2 + m.x7
    <= 0)
m.e832 = Constraint(expr= -(-0.65443 + m.x2)**2 - (-0.46573 + m.x5)**2 + m.x7
    <= 0)
m.e833 = Constraint(expr= -(-0.48017 + m.x2)**2 - (-0.75487 + m.x5)**2 + m.x7
    <= 0)
m.e834 = Constraint(expr= -(-0.19723 + m.x2)**2 - (-0.75653 + m.x5)**2 + m.x7
    <= 0)
m.e835 = Constraint(expr= -(-0.95337 + m.x2)**2 - (-0.04007 + m.x5)**2 + m.x7
    <= 0)
m.e836 = Constraint(expr= -(-0.22803 + m.x2)**2 - (-0.61533 + m.x5)**2 + m.x7
    <= 0)
m.e837 = Constraint(expr= -(-0.29857 + m.x2)**2 - (-0.71727 + m.x5)**2 + m.x7
    <= 0)
m.e838 = Constraint(expr= -(-0.22683 + m.x2)**2 - (-0.32213 + m.x5)**2 + m.x7
    <= 0)
m.e839 = Constraint(expr= -(-0.63577 + m.x2)**2 - (-0.10647 + m.x5)**2 + m.x7
    <= 0)
m.e840 = Constraint(expr= -(-0.47363 + m.x2)**2 - (-0.95693 + m.x5)**2 + m.x7
    <= 0)
m.e841 = Constraint(expr= -(-0.28497 + m.x2)**2 - (-0.72767 + m.x5)**2 + m.x7
    <= 0)
m.e842 = Constraint(expr= -(-0.04843 + m.x2)**2 - (-0.39973 + m.x5)**2 + m.x7
    <= 0)
m.e843 = Constraint(expr= -(-0.76617 + m.x2)**2 - (-0.30087 + m.x5)**2 + m.x7
    <= 0)
m.e844 = Constraint(expr= -(-0.83123 + m.x2)**2 - (-0.33053 + m.x5)**2 + m.x7
    <= 0)
m.e845 = Constraint(expr= -(-0.79937 + m.x2)**2 - (-0.74607 + m.x5)**2 + m.x7
    <= 0)
m.e846 = Constraint(expr= -(-0.50203 + m.x2)**2 - (-0.22933 + m.x5)**2 + m.x7
    <= 0)
m.e847 = Constraint(expr= -(-0.30457 + m.x2)**2 - (-0.18327 + m.x5)**2 + m.x7
    <= 0)
m.e848 = Constraint(expr= -(-0.54083 + m.x2)**2 - (-0.37613 + m.x5)**2 + m.x7
    <= 0)
m.e849 = Constraint(expr= -(-0.40177 + m.x2)**2 - (-0.93247 + m.x5)**2 + m.x7
    <= 0)
m.e850 = Constraint(expr= -(-0.22763 + m.x2)**2 - (-0.85093 + m.x5)**2 + m.x7
    <= 0)
m.e851 = Constraint(expr= -(-0.41097 + m.x2)**2 - (-0.51367 + m.x5)**2 + m.x7
    <= 0)
m.e852 = Constraint(expr= -(-0.64243 + m.x2)**2 - (-0.53373 + m.x5)**2 + m.x7
    <= 0)
m.e853 = Constraint(expr= -(-0.85217 + m.x2)**2 - (-0.64687 + m.x5)**2 + m.x7
    <= 0)
m.e854 = Constraint(expr= -(-0.66523 + m.x2)**2 - (-0.10453 + m.x5)**2 + m.x7
    <= 0)
m.e855 = Constraint(expr= -(-0.44537 + m.x2)**2 - (-0.25207 + m.x5)**2 + m.x7
    <= 0)
m.e856 = Constraint(expr= -(-0.97603 + m.x2)**2 - (-0.04333 + m.x5)**2 + m.x7
    <= 0)
m.e857 = Constraint(expr= -(-0.11057 + m.x2)**2 - (-0.44927 + m.x5)**2 + m.x7
    <= 0)
m.e858 = Constraint(expr= -(-0.05483 + m.x2)**2 - (-0.63013 + m.x5)**2 + m.x7
    <= 0)
m.e859 = Constraint(expr= -(-0.96777 + m.x2)**2 - (-0.55847 + m.x5)**2 + m.x7
    <= 0)
m.e860 = Constraint(expr= -(-0.18163 + m.x2)**2 - (-0.94493 + m.x5)**2 + m.x7
    <= 0)
m.e861 = Constraint(expr= -(-0.33697 + m.x2)**2 - (-0.09967 + m.x5)**2 + m.x7
    <= 0)
m.e862 = Constraint(expr= -(-0.43643 + m.x2)**2 - (-0.86773 + m.x5)**2 + m.x7
    <= 0)
m.e863 = Constraint(expr= -(-0.73817 + m.x2)**2 - (-0.79287 + m.x5)**2 + m.x7
    <= 0)
m.e864 = Constraint(expr= -(-0.69923 + m.x2)**2 - (-0.07853 + m.x5)**2 + m.x7
    <= 0)
m.e865 = Constraint(expr= -(-0.89137 + m.x2)**2 - (-0.55807 + m.x5)**2 + m.x7
    <= 0)
m.e866 = Constraint(expr= -(-0.65003 + m.x2)**2 - (-0.05733 + m.x5)**2 + m.x7
    <= 0)
m.e867 = Constraint(expr= -(-0.71657 + m.x2)**2 - (-0.51527 + m.x5)**2 + m.x7
    <= 0)
m.e868 = Constraint(expr= -(-0.76883 + m.x2)**2 - (-0.08413 + m.x5)**2 + m.x7
    <= 0)
m.e869 = Constraint(expr= -(-0.33377 + m.x2)**2 - (-0.98447 + m.x5)**2 + m.x7
    <= 0)
m.e870 = Constraint(expr= -(-0.33563 + m.x2)**2 - (-0.23893 + m.x5)**2 + m.x7
    <= 0)
m.e871 = Constraint(expr= -(-0.06297 + m.x2)**2 - (-0.48567 + m.x5)**2 + m.x7
    <= 0)
m.e872 = Constraint(expr= -(-0.43043 + m.x2)**2 - (-0.40173 + m.x5)**2 + m.x7
    <= 0)
m.e873 = Constraint(expr= -(-0.42417 + m.x2)**2 - (-0.73887 + m.x5)**2 + m.x7
    <= 0)
m.e874 = Constraint(expr= -(-0.93323 + m.x2)**2 - (-0.25253 + m.x5)**2 + m.x7
    <= 0)
m.e875 = Constraint(expr= -(-0.13737 + m.x2)**2 - (-0.66407 + m.x5)**2 + m.x7
    <= 0)
m.e876 = Constraint(expr= -(-0.52403 + m.x2)**2 - (-0.27133 + m.x5)**2 + m.x7
    <= 0)
m.e877 = Constraint(expr= -(-0.12257 + m.x2)**2 - (-0.38127 + m.x5)**2 + m.x7
    <= 0)
m.e878 = Constraint(expr= -(-0.68283 + m.x2)**2 - (-0.73813 + m.x5)**2 + m.x7
    <= 0)
m.e879 = Constraint(expr= -(-0.49977 + m.x2)**2 - (-0.21047 + m.x5)**2 + m.x7
    <= 0)
m.e880 = Constraint(expr= -(-0.68963 + m.x2)**2 - (-0.73293 + m.x5)**2 + m.x7
    <= 0)
m.e881 = Constraint(expr= -(-0.58897 + m.x2)**2 - (-0.67167 + m.x5)**2 + m.x7
    <= 0)
m.e882 = Constraint(expr= -(-0.62443 + m.x2)**2 - (-0.13573 + m.x5)**2 + m.x7
    <= 0)
m.e883 = Constraint(expr= -(-0.91017 + m.x2)**2 - (-0.48487 + m.x5)**2 + m.x7
    <= 0)
m.e884 = Constraint(expr= -(-0.36723 + m.x2)**2 - (-0.62653 + m.x5)**2 + m.x7
    <= 0)
m.e885 = Constraint(expr= -(-0.18337 + m.x2)**2 - (-0.57007 + m.x5)**2 + m.x7
    <= 0)
m.e886 = Constraint(expr= -(-0.59803 + m.x2)**2 - (-0.68533 + m.x5)**2 + m.x7
    <= 0)
m.e887 = Constraint(expr= -(-0.32857 + m.x2)**2 - (-0.04727 + m.x5)**2 + m.x7
    <= 0)
m.e888 = Constraint(expr= -(-0.79683 + m.x2)**2 - (-0.59213 + m.x5)**2 + m.x7
    <= 0)
m.e889 = Constraint(expr= -(-0.46577 + m.x2)**2 - (-0.23647 + m.x5)**2 + m.x7
    <= 0)
m.e890 = Constraint(expr= -(-0.24363 + m.x2)**2 - (-0.42693 + m.x5)**2 + m.x7
    <= 0)
m.e891 = Constraint(expr= -(-0.91497 + m.x2)**2 - (-0.65767 + m.x5)**2 + m.x7
    <= 0)
m.e892 = Constraint(expr= -(-0.01843 + m.x2)**2 - (-0.06973 + m.x5)**2 + m.x7
    <= 0)
m.e893 = Constraint(expr= -(-0.19617 + m.x2)**2 - (-0.03087 + m.x5)**2 + m.x7
    <= 0)
m.e894 = Constraint(expr= -(-0.00123 + m.x2)**2 - (-0.20053 + m.x5)**2 + m.x7
    <= 0)
m.e895 = Constraint(expr= -(-0.02937 + m.x2)**2 - (-0.27607 + m.x5)**2 + m.x7
    <= 0)
m.e896 = Constraint(expr= -(-0.87203 + m.x2)**2 - (-0.29933 + m.x5)**2 + m.x7
    <= 0)
m.e897 = Constraint(expr= -(-0.33457 + m.x2)**2 - (-0.51327 + m.x5)**2 + m.x7
    <= 0)
m.e898 = Constraint(expr= -(-0.11083 + m.x2)**2 - (-0.64613 + m.x5)**2 + m.x7
    <= 0)
m.e899 = Constraint(expr= -(-0.23177 + m.x2)**2 - (-0.06247 + m.x5)**2 + m.x7
    <= 0)
m.e900 = Constraint(expr= -(-0.99763 + m.x2)**2 - (-0.32093 + m.x5)**2 + m.x7
    <= 0)
m.e901 = Constraint(expr= -(-0.04097 + m.x2)**2 - (-0.44367 + m.x5)**2 + m.x7
    <= 0)
m.e902 = Constraint(expr= -(-0.61243 + m.x2)**2 - (-0.20373 + m.x5)**2 + m.x7
    <= 0)
m.e903 = Constraint(expr= -(-0.28217 + m.x2)**2 - (-0.37687 + m.x5)**2 + m.x7
    <= 0)
m.e904 = Constraint(expr= -(-0.83523 + m.x2)**2 - (-0.97453 + m.x5)**2 + m.x7
    <= 0)
m.e905 = Constraint(expr= -(-0.67537 + m.x2)**2 - (-0.78207 + m.x5)**2 + m.x7
    <= 0)
m.e906 = Constraint(expr= -(-0.34603 + m.x2)**2 - (-0.11333 + m.x5)**2 + m.x7
    <= 0)
m.e907 = Constraint(expr= -(-0.14057 + m.x2)**2 - (-0.77927 + m.x5)**2 + m.x7
    <= 0)
m.e908 = Constraint(expr= -(-0.62483 + m.x2)**2 - (-0.90013 + m.x5)**2 + m.x7
    <= 0)
m.e909 = Constraint(expr= -(-0.79777 + m.x2)**2 - (-0.68847 + m.x5)**2 + m.x7
    <= 0)
m.e910 = Constraint(expr= -(-0.95163 + m.x2)**2 - (-0.41493 + m.x5)**2 + m.x7
    <= 0)
m.e911 = Constraint(expr= -(-0.96697 + m.x2)**2 - (-0.02967 + m.x5)**2 + m.x7
    <= 0)
m.e912 = Constraint(expr= -(-0.40643 + m.x2)**2 - (-0.53773 + m.x5)**2 + m.x7
    <= 0)
m.e913 = Constraint(expr= -(-0.16817 + m.x2)**2 - (-0.52287 + m.x5)**2 + m.x7
    <= 0)
m.e914 = Constraint(expr= -(-0.86923 + m.x2)**2 - (-0.94853 + m.x5)**2 + m.x7
    <= 0)
m.e915 = Constraint(expr= -(-0.12137 + m.x2)**2 - (-0.08807 + m.x5)**2 + m.x7
    <= 0)
m.e916 = Constraint(expr= -(-0.02003 + m.x2)**2 - (-0.12733 + m.x5)**2 + m.x7
    <= 0)
m.e917 = Constraint(expr= -(-0.74657 + m.x2)**2 - (-0.84527 + m.x5)**2 + m.x7
    <= 0)
m.e918 = Constraint(expr= -(-0.33883 + m.x2)**2 - (-0.35413 + m.x5)**2 + m.x7
    <= 0)
m.e919 = Constraint(expr= -(-0.16377 + m.x2)**2 - (-0.11447 + m.x5)**2 + m.x7
    <= 0)
m.e920 = Constraint(expr= -(-0.10563 + m.x2)**2 - (-0.70893 + m.x5)**2 + m.x7
    <= 0)
m.e921 = Constraint(expr= -(-0.69297 + m.x2)**2 - (-0.41567 + m.x5)**2 + m.x7
    <= 0)
m.e922 = Constraint(expr= -(-0.40043 + m.x2)**2 - (-0.07173 + m.x5)**2 + m.x7
    <= 0)
m.e923 = Constraint(expr= -(-0.85417 + m.x2)**2 - (-0.46887 + m.x5)**2 + m.x7
    <= 0)
m.e924 = Constraint(expr= -(-0.10323 + m.x2)**2 - (-0.12253 + m.x5)**2 + m.x7
    <= 0)
m.e925 = Constraint(expr= -(-0.36737 + m.x2)**2 - (-0.19407 + m.x5)**2 + m.x7
    <= 0)
m.e926 = Constraint(expr= -(-0.89403 + m.x2)**2 - (-0.34133 + m.x5)**2 + m.x7
    <= 0)
m.e927 = Constraint(expr= -(-0.15257 + m.x2)**2 - (-0.71127 + m.x5)**2 + m.x7
    <= 0)
m.e928 = Constraint(expr= -(-0.25283 + m.x2)**2 - (-0.00813 + m.x5)**2 + m.x7
    <= 0)
m.e929 = Constraint(expr= -(-0.32977 + m.x2)**2 - (-0.34047 + m.x5)**2 + m.x7
    <= 0)
m.e930 = Constraint(expr= -(-0.45963 + m.x2)**2 - (-0.20293 + m.x5)**2 + m.x7
    <= 0)
m.e931 = Constraint(expr= -(-0.21897 + m.x2)**2 - (-0.60167 + m.x5)**2 + m.x7
    <= 0)
m.e932 = Constraint(expr= -(-0.59443 + m.x2)**2 - (-0.80573 + m.x5)**2 + m.x7
    <= 0)
m.e933 = Constraint(expr= -(-0.34017 + m.x2)**2 - (-0.21487 + m.x5)**2 + m.x7
    <= 0)
m.e934 = Constraint(expr= -(-0.53723 + m.x2)**2 - (-0.49653 + m.x5)**2 + m.x7
    <= 0)
m.e935 = Constraint(expr= -(-0.41337 + m.x2)**2 - (-0.10007 + m.x5)**2 + m.x7
    <= 0)
m.e936 = Constraint(expr= -(-0.96803 + m.x2)**2 - (-0.75533 + m.x5)**2 + m.x7
    <= 0)
m.e937 = Constraint(expr= -(-0.35857 + m.x2)**2 - (-0.37727 + m.x5)**2 + m.x7
    <= 0)
m.e938 = Constraint(expr= -(-0.36683 + m.x2)**2 - (-0.86213 + m.x5)**2 + m.x7
    <= 0)
m.e939 = Constraint(expr= -(-0.29577 + m.x2)**2 - (-0.36647 + m.x5)**2 + m.x7
    <= 0)
m.e940 = Constraint(expr= -(-0.01363 + m.x2)**2 - (-0.89693 + m.x5)**2 + m.x7
    <= 0)
m.e941 = Constraint(expr= -(-0.54497 + m.x2)**2 - (-0.58767 + m.x5)**2 + m.x7
    <= 0)
m.e942 = Constraint(expr= -(-0.98843 + m.x2)**2 - (-0.73973 + m.x5)**2 + m.x7
    <= 0)
m.e943 = Constraint(expr= -(-0.62617 + m.x2)**2 - (-0.76087 + m.x5)**2 + m.x7
    <= 0)
m.e944 = Constraint(expr= -(-0.17123 + m.x2)**2 - (-0.07053 + m.x5)**2 + m.x7
    <= 0)
m.e945 = Constraint(expr= -(-0.25937 + m.x2)**2 - (-0.80607 + m.x5)**2 + m.x7
    <= 0)
m.e946 = Constraint(expr= -(-0.24203 + m.x2)**2 - (-0.36933 + m.x5)**2 + m.x7
    <= 0)
m.e947 = Constraint(expr= -(-0.36457 + m.x2)**2 - (-0.84327 + m.x5)**2 + m.x7
    <= 0)
m.e948 = Constraint(expr= -(-0.68083 + m.x2)**2 - (-0.91613 + m.x5)**2 + m.x7
    <= 0)
m.e949 = Constraint(expr= -(-0.06177 + m.x2)**2 - (-0.19247 + m.x5)**2 + m.x7
    <= 0)
m.e950 = Constraint(expr= -(-0.76763 + m.x2)**2 - (-0.79093 + m.x5)**2 + m.x7
    <= 0)
m.e951 = Constraint(expr= -(-0.67097 + m.x2)**2 - (-0.37367 + m.x5)**2 + m.x7
    <= 0)
m.e952 = Constraint(expr= -(-0.58243 + m.x2)**2 - (-0.87373 + m.x5)**2 + m.x7
    <= 0)
m.e953 = Constraint(expr= -(-0.71217 + m.x2)**2 - (-0.10687 + m.x5)**2 + m.x7
    <= 0)
m.e954 = Constraint(expr= -(-0.00523 + m.x2)**2 - (-0.84453 + m.x5)**2 + m.x7
    <= 0)
m.e955 = Constraint(expr= -(-0.90537 + m.x2)**2 - (-0.31207 + m.x5)**2 + m.x7
    <= 0)
m.e956 = Constraint(expr= -(-0.71603 + m.x2)**2 - (-0.18333 + m.x5)**2 + m.x7
    <= 0)
m.e957 = Constraint(expr= -(-0.17057 + m.x2)**2 - (-0.10927 + m.x5)**2 + m.x7
    <= 0)
m.e958 = Constraint(expr= -(-0.19483 + m.x2)**2 - (-0.17013 + m.x5)**2 + m.x7
    <= 0)
m.e959 = Constraint(expr= -(-0.62777 + m.x2)**2 - (-0.81847 + m.x5)**2 + m.x7
    <= 0)
m.e960 = Constraint(expr= -(-0.72163 + m.x2)**2 - (-0.88493 + m.x5)**2 + m.x7
    <= 0)
m.e961 = Constraint(expr= -(-0.59697 + m.x2)**2 - (-0.95967 + m.x5)**2 + m.x7
    <= 0)
m.e962 = Constraint(expr= -(-0.37643 + m.x2)**2 - (-0.20773 + m.x5)**2 + m.x7
    <= 0)
m.e963 = Constraint(expr= -(-0.59817 + m.x2)**2 - (-0.25287 + m.x5)**2 + m.x7
    <= 0)
m.e964 = Constraint(expr= -(-0.03923 + m.x2)**2 - (-0.81853 + m.x5)**2 + m.x7
    <= 0)
m.e965 = Constraint(expr= -(-0.35137 + m.x2)**2 - (-0.61807 + m.x5)**2 + m.x7
    <= 0)
m.e966 = Constraint(expr= -(-0.39003 + m.x2)**2 - (-0.19733 + m.x5)**2 + m.x7
    <= 0)
m.e967 = Constraint(expr= -(-0.77657 + m.x2)**2 - (-0.17527 + m.x5)**2 + m.x7
    <= 0)
m.e968 = Constraint(expr= -(-0.90883 + m.x2)**2 - (-0.62413 + m.x5)**2 + m.x7
    <= 0)
m.e969 = Constraint(expr= -(-0.99377 + m.x2)**2 - (-0.24447 + m.x5)**2 + m.x7
    <= 0)
m.e970 = Constraint(expr= -(-0.87563 + m.x2)**2 - (-0.17893 + m.x5)**2 + m.x7
    <= 0)
m.e971 = Constraint(expr= -(-0.32297 + m.x2)**2 - (-0.34567 + m.x5)**2 + m.x7
    <= 0)
m.e972 = Constraint(expr= -(-0.37043 + m.x2)**2 - (-0.74173 + m.x5)**2 + m.x7
    <= 0)
m.e973 = Constraint(expr= -(-0.28417 + m.x2)**2 - (-0.19887 + m.x5)**2 + m.x7
    <= 0)
m.e974 = Constraint(expr= -(-0.27323 + m.x2)**2 - (-0.99253 + m.x5)**2 + m.x7
    <= 0)
m.e975 = Constraint(expr= -(-0.59737 + m.x2)**2 - (-0.72407 + m.x5)**2 + m.x7
    <= 0)
m.e976 = Constraint(expr= -(-0.26403 + m.x2)**2 - (-0.41133 + m.x5)**2 + m.x7
    <= 0)
m.e977 = Constraint(expr= -(-0.18257 + m.x2)**2 - (-0.04127 + m.x5)**2 + m.x7
    <= 0)
m.e978 = Constraint(expr= -(-0.82283 + m.x2)**2 - (-0.27813 + m.x5)**2 + m.x7
    <= 0)
m.e979 = Constraint(expr= -(-0.15977 + m.x2)**2 - (-0.47047 + m.x5)**2 + m.x7
    <= 0)
m.e980 = Constraint(expr= -(-0.22963 + m.x2)**2 - (-0.67293 + m.x5)**2 + m.x7
    <= 0)
m.e981 = Constraint(expr= -(-0.84897 + m.x2)**2 - (-0.53167 + m.x5)**2 + m.x7
    <= 0)
m.e982 = Constraint(expr= -(-0.56443 + m.x2)**2 - (-0.47573 + m.x5)**2 + m.x7
    <= 0)
m.e983 = Constraint(expr= -(-0.77017 + m.x2)**2 - (-0.94487 + m.x5)**2 + m.x7
    <= 0)
m.e984 = Constraint(expr= -(-0.70723 + m.x2)**2 - (-0.36653 + m.x5)**2 + m.x7
    <= 0)
m.e985 = Constraint(expr= -(-0.64337 + m.x2)**2 - (-0.63007 + m.x5)**2 + m.x7
    <= 0)
m.e986 = Constraint(expr= -(-0.33803 + m.x2)**2 - (-0.82533 + m.x5)**2 + m.x7
    <= 0)
m.e987 = Constraint(expr= -(-0.38857 + m.x2)**2 - (-0.70727 + m.x5)**2 + m.x7
    <= 0)
m.e988 = Constraint(expr= -(-0.93683 + m.x2)**2 - (-0.13213 + m.x5)**2 + m.x7
    <= 0)
m.e989 = Constraint(expr= -(-0.12577 + m.x2)**2 - (-0.49647 + m.x5)**2 + m.x7
    <= 0)
m.e990 = Constraint(expr= -(-0.78363 + m.x2)**2 - (-0.36693 + m.x5)**2 + m.x7
    <= 0)
m.e991 = Constraint(expr= -(-0.17497 + m.x2)**2 - (-0.51767 + m.x5)**2 + m.x7
    <= 0)
m.e992 = Constraint(expr= -(-0.95843 + m.x2)**2 - (-0.40973 + m.x5)**2 + m.x7
    <= 0)
m.e993 = Constraint(expr= -(-0.05617 + m.x2)**2 - (-0.49087 + m.x5)**2 + m.x7
    <= 0)
m.e994 = Constraint(expr= -(-0.34123 + m.x2)**2 - (-0.94053 + m.x5)**2 + m.x7
    <= 0)
m.e995 = Constraint(expr= -(-0.48937 + m.x2)**2 - (-0.33607 + m.x5)**2 + m.x7
    <= 0)
m.e996 = Constraint(expr= -(-0.61203 + m.x2)**2 - (-0.43933 + m.x5)**2 + m.x7
    <= 0)
m.e997 = Constraint(expr= -(-0.39457 + m.x2)**2 - (-0.17327 + m.x5)**2 + m.x7
    <= 0)
m.e998 = Constraint(expr= -(-0.25083 + m.x2)**2 - (-0.18613 + m.x5)**2 + m.x7
    <= 0)
m.e999 = Constraint(expr= -(-0.89177 + m.x2)**2 - (-0.32247 + m.x5)**2 + m.x7
    <= 0)
m.e1000 = Constraint(expr= -(-0.53763 + m.x2)**2 - (-0.26093 + m.x5)**2 + m.x7
    <= 0)
m.e1001 = Constraint(expr= -(-0.00097 + m.x3)**2 - (-0.00367 + m.x6)**2 + m.x7
    <= 0)
m.e1002 = Constraint(expr= -(-0.85243 + m.x3)**2 - (-0.84373 + m.x6)**2 + m.x7
    <= 0)
m.e1003 = Constraint(expr= -(-0.84217 + m.x3)**2 - (-0.53687 + m.x6)**2 + m.x7
    <= 0)
m.e1004 = Constraint(expr= -(-0.47523 + m.x3)**2 - (-0.01453 + m.x6)**2 + m.x7
    <= 0)
m.e1005 = Constraint(expr= -(-0.83537 + m.x3)**2 - (-0.54207 + m.x6)**2 + m.x7
    <= 0)
m.e1006 = Constraint(expr= -(-0.38603 + m.x3)**2 - (-0.55333 + m.x6)**2 + m.x7
    <= 0)
m.e1007 = Constraint(expr= -(-0.90057 + m.x3)**2 - (-0.13927 + m.x6)**2 + m.x7
    <= 0)
m.e1008 = Constraint(expr= -(-0.06483 + m.x3)**2 - (-0.74013 + m.x6)**2 + m.x7
    <= 0)
m.e1009 = Constraint(expr= -(-0.15777 + m.x3)**2 - (-0.64847 + m.x6)**2 + m.x7
    <= 0)
m.e1010 = Constraint(expr= -(-0.79163 + m.x3)**2 - (-0.65493 + m.x6)**2 + m.x7
    <= 0)
m.e1011 = Constraint(expr= -(-0.92697 + m.x3)**2 - (-0.58967 + m.x6)**2 + m.x7
    <= 0)
m.e1012 = Constraint(expr= -(-0.64643 + m.x3)**2 - (-0.17773 + m.x6)**2 + m.x7
    <= 0)
m.e1013 = Constraint(expr= -(-0.72817 + m.x3)**2 - (-0.68287 + m.x6)**2 + m.x7
    <= 0)
m.e1014 = Constraint(expr= -(-0.50923 + m.x3)**2 - (-0.98853 + m.x6)**2 + m.x7
    <= 0)
m.e1015 = Constraint(expr= -(-0.28137 + m.x3)**2 - (-0.84807 + m.x6)**2 + m.x7
    <= 0)
m.e1016 = Constraint(expr= -(-0.06003 + m.x3)**2 - (-0.56733 + m.x6)**2 + m.x7
    <= 0)
m.e1017 = Constraint(expr= -(-0.50657 + m.x3)**2 - (-0.20527 + m.x6)**2 + m.x7
    <= 0)
m.e1018 = Constraint(expr= -(-0.77883 + m.x3)**2 - (-0.19413 + m.x6)**2 + m.x7
    <= 0)
m.e1019 = Constraint(expr= -(-0.52377 + m.x3)**2 - (-0.07447 + m.x6)**2 + m.x7
    <= 0)
m.e1020 = Constraint(expr= -(-0.94563 + m.x3)**2 - (-0.94893 + m.x6)**2 + m.x7
    <= 0)
m.e1021 = Constraint(expr= -(-0.65297 + m.x3)**2 - (-0.97567 + m.x6)**2 + m.x7
    <= 0)
m.e1022 = Constraint(expr= -(-0.64043 + m.x3)**2 - (-0.71173 + m.x6)**2 + m.x7
    <= 0)
m.e1023 = Constraint(expr= -(-0.41417 + m.x3)**2 - (-0.62887 + m.x6)**2 + m.x7
    <= 0)
m.e1024 = Constraint(expr= -(-0.74323 + m.x3)**2 - (-0.16253 + m.x6)**2 + m.x7
    <= 0)
m.e1025 = Constraint(expr= -(-0.52737 + m.x3)**2 - (-0.95407 + m.x6)**2 + m.x7
    <= 0)
m.e1026 = Constraint(expr= -(-0.93403 + m.x3)**2 - (-0.78133 + m.x6)**2 + m.x7
    <= 0)
m.e1027 = Constraint(expr= -(-0.91257 + m.x3)**2 - (-0.07127 + m.x6)**2 + m.x7
    <= 0)
m.e1028 = Constraint(expr= -(-0.69283 + m.x3)**2 - (-0.84813 + m.x6)**2 + m.x7
    <= 0)
m.e1029 = Constraint(expr= -(-0.68977 + m.x3)**2 - (-0.30047 + m.x6)**2 + m.x7
    <= 0)
m.e1030 = Constraint(expr= -(-0.29963 + m.x3)**2 - (-0.44293 + m.x6)**2 + m.x7
    <= 0)
m.e1031 = Constraint(expr= -(-0.17897 + m.x3)**2 - (-0.16167 + m.x6)**2 + m.x7
    <= 0)
m.e1032 = Constraint(expr= -(-0.83443 + m.x3)**2 - (-0.44573 + m.x6)**2 + m.x7
    <= 0)
m.e1033 = Constraint(expr= -(-0.90017 + m.x3)**2 - (-0.37487 + m.x6)**2 + m.x7
    <= 0)
m.e1034 = Constraint(expr= -(-0.17723 + m.x3)**2 - (-0.53653 + m.x6)**2 + m.x7
    <= 0)
m.e1035 = Constraint(expr= -(-0.57337 + m.x3)**2 - (-0.86007 + m.x6)**2 + m.x7
    <= 0)
m.e1036 = Constraint(expr= -(-0.00803 + m.x3)**2 - (-0.19533 + m.x6)**2 + m.x7
    <= 0)
m.e1037 = Constraint(expr= -(-0.11857 + m.x3)**2 - (-0.73727 + m.x6)**2 + m.x7
    <= 0)
m.e1038 = Constraint(expr= -(-0.80683 + m.x3)**2 - (-0.70213 + m.x6)**2 + m.x7
    <= 0)
m.e1039 = Constraint(expr= -(-0.65577 + m.x3)**2 - (-0.32647 + m.x6)**2 + m.x7
    <= 0)
m.e1040 = Constraint(expr= -(-0.85363 + m.x3)**2 - (-0.13693 + m.x6)**2 + m.x7
    <= 0)
m.e1041 = Constraint(expr= -(-0.50497 + m.x3)**2 - (-0.14767 + m.x6)**2 + m.x7
    <= 0)
m.e1042 = Constraint(expr= -(-0.22843 + m.x3)**2 - (-0.37973 + m.x6)**2 + m.x7
    <= 0)
m.e1043 = Constraint(expr= -(-0.18617 + m.x3)**2 - (-0.92087 + m.x6)**2 + m.x7
    <= 0)
m.e1044 = Constraint(expr= -(-0.81123 + m.x3)**2 - (-0.11053 + m.x6)**2 + m.x7
    <= 0)
m.e1045 = Constraint(expr= -(-0.41937 + m.x3)**2 - (-0.56607 + m.x6)**2 + m.x7
    <= 0)
m.e1046 = Constraint(expr= -(-0.28203 + m.x3)**2 - (-0.80933 + m.x6)**2 + m.x7
    <= 0)
m.e1047 = Constraint(expr= -(-0.12457 + m.x3)**2 - (-0.20327 + m.x6)**2 + m.x7
    <= 0)
m.e1048 = Constraint(expr= -(-0.12083 + m.x3)**2 - (-0.75613 + m.x6)**2 + m.x7
    <= 0)
m.e1049 = Constraint(expr= -(-0.42177 + m.x3)**2 - (-0.15247 + m.x6)**2 + m.x7
    <= 0)
m.e1050 = Constraint(expr= -(-0.60763 + m.x3)**2 - (-0.03093 + m.x6)**2 + m.x7
    <= 0)
m.e1051 = Constraint(expr= -(-0.63097 + m.x3)**2 - (-0.93367 + m.x6)**2 + m.x7
    <= 0)
m.e1052 = Constraint(expr= -(-0.82243 + m.x3)**2 - (-0.51373 + m.x6)**2 + m.x7
    <= 0)
m.e1053 = Constraint(expr= -(-0.27217 + m.x3)**2 - (-0.26687 + m.x6)**2 + m.x7
    <= 0)
m.e1054 = Constraint(expr= -(-0.64523 + m.x3)**2 - (-0.88453 + m.x6)**2 + m.x7
    <= 0)
m.e1055 = Constraint(expr= -(-0.06537 + m.x3)**2 - (-0.07207 + m.x6)**2 + m.x7
    <= 0)
m.e1056 = Constraint(expr= -(-0.75603 + m.x3)**2 - (-0.62333 + m.x6)**2 + m.x7
    <= 0)
m.e1057 = Constraint(expr= -(-0.93057 + m.x3)**2 - (-0.46927 + m.x6)**2 + m.x7
    <= 0)
m.e1058 = Constraint(expr= -(-0.63483 + m.x3)**2 - (-0.01013 + m.x6)**2 + m.x7
    <= 0)
m.e1059 = Constraint(expr= -(-0.98777 + m.x3)**2 - (-0.77847 + m.x6)**2 + m.x7
    <= 0)
m.e1060 = Constraint(expr= -(-0.56163 + m.x3)**2 - (-0.12493 + m.x6)**2 + m.x7
    <= 0)
m.e1061 = Constraint(expr= -(-0.55697 + m.x3)**2 - (-0.51967 + m.x6)**2 + m.x7
    <= 0)
m.e1062 = Constraint(expr= -(-0.61643 + m.x3)**2 - (-0.84773 + m.x6)**2 + m.x7
    <= 0)
m.e1063 = Constraint(expr= -(-0.15817 + m.x3)**2 - (-0.41287 + m.x6)**2 + m.x7
    <= 0)
m.e1064 = Constraint(expr= -(-0.67923 + m.x3)**2 - (-0.85853 + m.x6)**2 + m.x7
    <= 0)
m.e1065 = Constraint(expr= -(-0.51137 + m.x3)**2 - (-0.37807 + m.x6)**2 + m.x7
    <= 0)
m.e1066 = Constraint(expr= -(-0.43003 + m.x3)**2 - (-0.63733 + m.x6)**2 + m.x7
    <= 0)
m.e1067 = Constraint(expr= -(-0.53657 + m.x3)**2 - (-0.53527 + m.x6)**2 + m.x7
    <= 0)
m.e1068 = Constraint(expr= -(-0.34883 + m.x3)**2 - (-0.46413 + m.x6)**2 + m.x7
    <= 0)
m.e1069 = Constraint(expr= -(-0.35377 + m.x3)**2 - (-0.20447 + m.x6)**2 + m.x7
    <= 0)
m.e1070 = Constraint(expr= -(-0.71563 + m.x3)**2 - (-0.41893 + m.x6)**2 + m.x7
    <= 0)
m.e1071 = Constraint(expr= -(-0.28297 + m.x3)**2 - (-0.90567 + m.x6)**2 + m.x7
    <= 0)
m.e1072 = Constraint(expr= -(-0.61043 + m.x3)**2 - (-0.38173 + m.x6)**2 + m.x7
    <= 0)
m.e1073 = Constraint(expr= -(-0.84417 + m.x3)**2 - (-0.35887 + m.x6)**2 + m.x7
    <= 0)
m.e1074 = Constraint(expr= -(-0.91323 + m.x3)**2 - (-0.03253 + m.x6)**2 + m.x7
    <= 0)
m.e1075 = Constraint(expr= -(-0.75737 + m.x3)**2 - (-0.48407 + m.x6)**2 + m.x7
    <= 0)
m.e1076 = Constraint(expr= -(-0.30403 + m.x3)**2 - (-0.85133 + m.x6)**2 + m.x7
    <= 0)
m.e1077 = Constraint(expr= -(-0.94257 + m.x3)**2 - (-0.40127 + m.x6)**2 + m.x7
    <= 0)
m.e1078 = Constraint(expr= -(-0.26283 + m.x3)**2 - (-0.11813 + m.x6)**2 + m.x7
    <= 0)
m.e1079 = Constraint(expr= -(-0.51977 + m.x3)**2 - (-0.43047 + m.x6)**2 + m.x7
    <= 0)
m.e1080 = Constraint(expr= -(-0.06963 + m.x3)**2 - (-0.91293 + m.x6)**2 + m.x7
    <= 0)
m.e1081 = Constraint(expr= -(-0.80897 + m.x3)**2 - (-0.09167 + m.x6)**2 + m.x7
    <= 0)
m.e1082 = Constraint(expr= -(-0.80443 + m.x3)**2 - (-0.11573 + m.x6)**2 + m.x7
    <= 0)
m.e1083 = Constraint(expr= -(-0.33017 + m.x3)**2 - (-0.10487 + m.x6)**2 + m.x7
    <= 0)
m.e1084 = Constraint(expr= -(-0.34723 + m.x3)**2 - (-0.40653 + m.x6)**2 + m.x7
    <= 0)
m.e1085 = Constraint(expr= -(-0.80337 + m.x3)**2 - (-0.39007 + m.x6)**2 + m.x7
    <= 0)
m.e1086 = Constraint(expr= -(-0.37803 + m.x3)**2 - (-0.26533 + m.x6)**2 + m.x7
    <= 0)
m.e1087 = Constraint(expr= -(-0.14857 + m.x3)**2 - (-0.06727 + m.x6)**2 + m.x7
    <= 0)
m.e1088 = Constraint(expr= -(-0.37683 + m.x3)**2 - (-0.97213 + m.x6)**2 + m.x7
    <= 0)
m.e1089 = Constraint(expr= -(-0.48577 + m.x3)**2 - (-0.45647 + m.x6)**2 + m.x7
    <= 0)
m.e1090 = Constraint(expr= -(-0.62363 + m.x3)**2 - (-0.60693 + m.x6)**2 + m.x7
    <= 0)
m.e1091 = Constraint(expr= -(-0.13497 + m.x3)**2 - (-0.07767 + m.x6)**2 + m.x7
    <= 0)
m.e1092 = Constraint(expr= -(-0.19843 + m.x3)**2 - (-0.04973 + m.x6)**2 + m.x7
    <= 0)
m.e1093 = Constraint(expr= -(-0.61617 + m.x3)**2 - (-0.65087 + m.x6)**2 + m.x7
    <= 0)
m.e1094 = Constraint(expr= -(-0.98123 + m.x3)**2 - (-0.98053 + m.x6)**2 + m.x7
    <= 0)
m.e1095 = Constraint(expr= -(-0.64937 + m.x3)**2 - (-0.09607 + m.x6)**2 + m.x7
    <= 0)
m.e1096 = Constraint(expr= -(-0.65203 + m.x3)**2 - (-0.87933 + m.x6)**2 + m.x7
    <= 0)
m.e1097 = Constraint(expr= -(-0.15457 + m.x3)**2 - (-0.53327 + m.x6)**2 + m.x7
    <= 0)
m.e1098 = Constraint(expr= -(-0.69083 + m.x3)**2 - (-0.02613 + m.x6)**2 + m.x7
    <= 0)
m.e1099 = Constraint(expr= -(-0.25177 + m.x3)**2 - (-0.28247 + m.x6)**2 + m.x7
    <= 0)
m.e1100 = Constraint(expr= -(-0.37763 + m.x3)**2 - (-0.50093 + m.x6)**2 + m.x7
    <= 0)
m.e1101 = Constraint(expr= -(-0.26097 + m.x3)**2 - (-0.86367 + m.x6)**2 + m.x7
    <= 0)
m.e1102 = Constraint(expr= -(-0.79243 + m.x3)**2 - (-0.18373 + m.x6)**2 + m.x7
    <= 0)
m.e1103 = Constraint(expr= -(-0.70217 + m.x3)**2 - (-0.99687 + m.x6)**2 + m.x7
    <= 0)
m.e1104 = Constraint(expr= -(-0.81523 + m.x3)**2 - (-0.75453 + m.x6)**2 + m.x7
    <= 0)
m.e1105 = Constraint(expr= -(-0.29537 + m.x3)**2 - (-0.60207 + m.x6)**2 + m.x7
    <= 0)
m.e1106 = Constraint(expr= -(-0.12603 + m.x3)**2 - (-0.69333 + m.x6)**2 + m.x7
    <= 0)
m.e1107 = Constraint(expr= -(-0.96057 + m.x3)**2 - (-0.79927 + m.x6)**2 + m.x7
    <= 0)
m.e1108 = Constraint(expr= -(-0.20483 + m.x3)**2 - (-0.28013 + m.x6)**2 + m.x7
    <= 0)
m.e1109 = Constraint(expr= -(-0.81777 + m.x3)**2 - (-0.90847 + m.x6)**2 + m.x7
    <= 0)
m.e1110 = Constraint(expr= -(-0.33163 + m.x3)**2 - (-0.59493 + m.x6)**2 + m.x7
    <= 0)
m.e1111 = Constraint(expr= -(-0.18697 + m.x3)**2 - (-0.44967 + m.x6)**2 + m.x7
    <= 0)
m.e1112 = Constraint(expr= -(-0.58643 + m.x3)**2 - (-0.51773 + m.x6)**2 + m.x7
    <= 0)
m.e1113 = Constraint(expr= -(-0.58817 + m.x3)**2 - (-0.14287 + m.x6)**2 + m.x7
    <= 0)
m.e1114 = Constraint(expr= -(-0.84923 + m.x3)**2 - (-0.72853 + m.x6)**2 + m.x7
    <= 0)
m.e1115 = Constraint(expr= -(-0.74137 + m.x3)**2 - (-0.90807 + m.x6)**2 + m.x7
    <= 0)
m.e1116 = Constraint(expr= -(-0.80003 + m.x3)**2 - (-0.70733 + m.x6)**2 + m.x7
    <= 0)
m.e1117 = Constraint(expr= -(-0.56657 + m.x3)**2 - (-0.86527 + m.x6)**2 + m.x7
    <= 0)
m.e1118 = Constraint(expr= -(-0.91883 + m.x3)**2 - (-0.73413 + m.x6)**2 + m.x7
    <= 0)
m.e1119 = Constraint(expr= -(-0.18377 + m.x3)**2 - (-0.33447 + m.x6)**2 + m.x7
    <= 0)
m.e1120 = Constraint(expr= -(-0.48563 + m.x3)**2 - (-0.88893 + m.x6)**2 + m.x7
    <= 0)
m.e1121 = Constraint(expr= -(-0.91297 + m.x3)**2 - (-0.83567 + m.x6)**2 + m.x7
    <= 0)
m.e1122 = Constraint(expr= -(-0.58043 + m.x3)**2 - (-0.05173 + m.x6)**2 + m.x7
    <= 0)
m.e1123 = Constraint(expr= -(-0.27417 + m.x3)**2 - (-0.08887 + m.x6)**2 + m.x7
    <= 0)
m.e1124 = Constraint(expr= -(-0.08323 + m.x3)**2 - (-0.90253 + m.x6)**2 + m.x7
    <= 0)
m.e1125 = Constraint(expr= -(-0.98737 + m.x3)**2 - (-0.01407 + m.x6)**2 + m.x7
    <= 0)
m.e1126 = Constraint(expr= -(-0.67403 + m.x3)**2 - (-0.92133 + m.x6)**2 + m.x7
    <= 0)
m.e1127 = Constraint(expr= -(-0.97257 + m.x3)**2 - (-0.73127 + m.x6)**2 + m.x7
    <= 0)
m.e1128 = Constraint(expr= -(-0.83283 + m.x3)**2 - (-0.38813 + m.x6)**2 + m.x7
    <= 0)
m.e1129 = Constraint(expr= -(-0.34977 + m.x3)**2 - (-0.56047 + m.x6)**2 + m.x7
    <= 0)
m.e1130 = Constraint(expr= -(-0.83963 + m.x3)**2 - (-0.38293 + m.x6)**2 + m.x7
    <= 0)
m.e1131 = Constraint(expr= -(-0.43897 + m.x3)**2 - (-0.02167 + m.x6)**2 + m.x7
    <= 0)
m.e1132 = Constraint(expr= -(-0.77443 + m.x3)**2 - (-0.78573 + m.x6)**2 + m.x7
    <= 0)
m.e1133 = Constraint(expr= -(-0.76017 + m.x3)**2 - (-0.83487 + m.x6)**2 + m.x7
    <= 0)
m.e1134 = Constraint(expr= -(-0.51723 + m.x3)**2 - (-0.27653 + m.x6)**2 + m.x7
    <= 0)
m.e1135 = Constraint(expr= -(-0.03337 + m.x3)**2 - (-0.92007 + m.x6)**2 + m.x7
    <= 0)
m.e1136 = Constraint(expr= -(-0.74803 + m.x3)**2 - (-0.33533 + m.x6)**2 + m.x7
    <= 0)
m.e1137 = Constraint(expr= -(-0.17857 + m.x3)**2 - (-0.39727 + m.x6)**2 + m.x7
    <= 0)
m.e1138 = Constraint(expr= -(-0.94683 + m.x3)**2 - (-0.24213 + m.x6)**2 + m.x7
    <= 0)
m.e1139 = Constraint(expr= -(-0.31577 + m.x3)**2 - (-0.58647 + m.x6)**2 + m.x7
    <= 0)
m.e1140 = Constraint(expr= -(-0.39363 + m.x3)**2 - (-0.07693 + m.x6)**2 + m.x7
    <= 0)
m.e1141 = Constraint(expr= -(-0.76497 + m.x3)**2 - (-0.00767 + m.x6)**2 + m.x7
    <= 0)
m.e1142 = Constraint(expr= -(-0.16843 + m.x3)**2 - (-0.71973 + m.x6)**2 + m.x7
    <= 0)
m.e1143 = Constraint(expr= -(-0.04617 + m.x3)**2 - (-0.38087 + m.x6)**2 + m.x7
    <= 0)
m.e1144 = Constraint(expr= -(-0.15123 + m.x3)**2 - (-0.85053 + m.x6)**2 + m.x7
    <= 0)
m.e1145 = Constraint(expr= -(-0.87937 + m.x3)**2 - (-0.62607 + m.x6)**2 + m.x7
    <= 0)
m.e1146 = Constraint(expr= -(-0.02203 + m.x3)**2 - (-0.94933 + m.x6)**2 + m.x7
    <= 0)
m.e1147 = Constraint(expr= -(-0.18457 + m.x3)**2 - (-0.86327 + m.x6)**2 + m.x7
    <= 0)
m.e1148 = Constraint(expr= -(-0.26083 + m.x3)**2 - (-0.29613 + m.x6)**2 + m.x7
    <= 0)
m.e1149 = Constraint(expr= -(-0.08177 + m.x3)**2 - (-0.41247 + m.x6)**2 + m.x7
    <= 0)
m.e1150 = Constraint(expr= -(-0.14763 + m.x3)**2 - (-0.97093 + m.x6)**2 + m.x7
    <= 0)
m.e1151 = Constraint(expr= -(-0.89097 + m.x3)**2 - (-0.79367 + m.x6)**2 + m.x7
    <= 0)
m.e1152 = Constraint(expr= -(-0.76243 + m.x3)**2 - (-0.85373 + m.x6)**2 + m.x7
    <= 0)
m.e1153 = Constraint(expr= -(-0.13217 + m.x3)**2 - (-0.72687 + m.x6)**2 + m.x7
    <= 0)
m.e1154 = Constraint(expr= -(-0.98523 + m.x3)**2 - (-0.62453 + m.x6)**2 + m.x7
    <= 0)
m.e1155 = Constraint(expr= -(-0.52537 + m.x3)**2 - (-0.13207 + m.x6)**2 + m.x7
    <= 0)
m.e1156 = Constraint(expr= -(-0.49603 + m.x3)**2 - (-0.76333 + m.x6)**2 + m.x7
    <= 0)
m.e1157 = Constraint(expr= -(-0.99057 + m.x3)**2 - (-0.12927 + m.x6)**2 + m.x7
    <= 0)
m.e1158 = Constraint(expr= -(-0.77483 + m.x3)**2 - (-0.55013 + m.x6)**2 + m.x7
    <= 0)
m.e1159 = Constraint(expr= -(-0.64777 + m.x3)**2 - (-0.03847 + m.x6)**2 + m.x7
    <= 0)
m.e1160 = Constraint(expr= -(-0.10163 + m.x3)**2 - (-0.06493 + m.x6)**2 + m.x7
    <= 0)
m.e1161 = Constraint(expr= -(-0.81697 + m.x3)**2 - (-0.37967 + m.x6)**2 + m.x7
    <= 0)
m.e1162 = Constraint(expr= -(-0.55643 + m.x3)**2 - (-0.18773 + m.x6)**2 + m.x7
    <= 0)
m.e1163 = Constraint(expr= -(-0.01817 + m.x3)**2 - (-0.87287 + m.x6)**2 + m.x7
    <= 0)
m.e1164 = Constraint(expr= -(-0.01923 + m.x3)**2 - (-0.59853 + m.x6)**2 + m.x7
    <= 0)
m.e1165 = Constraint(expr= -(-0.97137 + m.x3)**2 - (-0.43807 + m.x6)**2 + m.x7
    <= 0)
m.e1166 = Constraint(expr= -(-0.17003 + m.x3)**2 - (-0.77733 + m.x6)**2 + m.x7
    <= 0)
m.e1167 = Constraint(expr= -(-0.59657 + m.x3)**2 - (-0.19527 + m.x6)**2 + m.x7
    <= 0)
m.e1168 = Constraint(expr= -(-0.48883 + m.x3)**2 - (-0.00413 + m.x6)**2 + m.x7
    <= 0)
m.e1169 = Constraint(expr= -(-0.01377 + m.x3)**2 - (-0.46447 + m.x6)**2 + m.x7
    <= 0)
m.e1170 = Constraint(expr= -(-0.25563 + m.x3)**2 - (-0.35893 + m.x6)**2 + m.x7
    <= 0)
m.e1171 = Constraint(expr= -(-0.54297 + m.x3)**2 - (-0.76567 + m.x6)**2 + m.x7
    <= 0)
m.e1172 = Constraint(expr= -(-0.55043 + m.x3)**2 - (-0.72173 + m.x6)**2 + m.x7
    <= 0)
m.e1173 = Constraint(expr= -(-0.70417 + m.x3)**2 - (-0.81887 + m.x6)**2 + m.x7
    <= 0)
m.e1174 = Constraint(expr= -(-0.25323 + m.x3)**2 - (-0.77253 + m.x6)**2 + m.x7
    <= 0)
m.e1175 = Constraint(expr= -(-0.21737 + m.x3)**2 - (-0.54407 + m.x6)**2 + m.x7
    <= 0)
m.e1176 = Constraint(expr= -(-0.04403 + m.x3)**2 - (-0.99133 + m.x6)**2 + m.x7
    <= 0)
m.e1177 = Constraint(expr= -(-0.00257 + m.x3)**2 - (-0.06127 + m.x6)**2 + m.x7
    <= 0)
m.e1178 = Constraint(expr= -(-0.40283 + m.x3)**2 - (-0.65813 + m.x6)**2 + m.x7
    <= 0)
m.e1179 = Constraint(expr= -(-0.17977 + m.x3)**2 - (-0.69047 + m.x6)**2 + m.x7
    <= 0)
m.e1180 = Constraint(expr= -(-0.60963 + m.x3)**2 - (-0.85293 + m.x6)**2 + m.x7
    <= 0)
m.e1181 = Constraint(expr= -(-0.06897 + m.x3)**2 - (-0.95167 + m.x6)**2 + m.x7
    <= 0)
m.e1182 = Constraint(expr= -(-0.74443 + m.x3)**2 - (-0.45573 + m.x6)**2 + m.x7
    <= 0)
m.e1183 = Constraint(expr= -(-0.19017 + m.x3)**2 - (-0.56487 + m.x6)**2 + m.x7
    <= 0)
m.e1184 = Constraint(expr= -(-0.68723 + m.x3)**2 - (-0.14653 + m.x6)**2 + m.x7
    <= 0)
m.e1185 = Constraint(expr= -(-0.26337 + m.x3)**2 - (-0.45007 + m.x6)**2 + m.x7
    <= 0)
m.e1186 = Constraint(expr= -(-0.11803 + m.x3)**2 - (-0.40533 + m.x6)**2 + m.x7
    <= 0)
m.e1187 = Constraint(expr= -(-0.20857 + m.x3)**2 - (-0.72727 + m.x6)**2 + m.x7
    <= 0)
m.e1188 = Constraint(expr= -(-0.51683 + m.x3)**2 - (-0.51213 + m.x6)**2 + m.x7
    <= 0)
m.e1189 = Constraint(expr= -(-0.14577 + m.x3)**2 - (-0.71647 + m.x6)**2 + m.x7
    <= 0)
m.e1190 = Constraint(expr= -(-0.16363 + m.x3)**2 - (-0.54693 + m.x6)**2 + m.x7
    <= 0)
m.e1191 = Constraint(expr= -(-0.39497 + m.x3)**2 - (-0.93767 + m.x6)**2 + m.x7
    <= 0)
m.e1192 = Constraint(expr= -(-0.13843 + m.x3)**2 - (-0.38973 + m.x6)**2 + m.x7
    <= 0)
m.e1193 = Constraint(expr= -(-0.47617 + m.x3)**2 - (-0.11087 + m.x6)**2 + m.x7
    <= 0)
m.e1194 = Constraint(expr= -(-0.32123 + m.x3)**2 - (-0.72053 + m.x6)**2 + m.x7
    <= 0)
m.e1195 = Constraint(expr= -(-0.10937 + m.x3)**2 - (-0.15607 + m.x6)**2 + m.x7
    <= 0)
m.e1196 = Constraint(expr= -(-0.39203 + m.x3)**2 - (-0.01933 + m.x6)**2 + m.x7
    <= 0)
m.e1197 = Constraint(expr= -(-0.21457 + m.x3)**2 - (-0.19327 + m.x6)**2 + m.x7
    <= 0)
m.e1198 = Constraint(expr= -(-0.83083 + m.x3)**2 - (-0.56613 + m.x6)**2 + m.x7
    <= 0)
m.e1199 = Constraint(expr= -(-0.91177 + m.x3)**2 - (-0.54247 + m.x6)**2 + m.x7
    <= 0)
m.e1200 = Constraint(expr= -(-0.91763 + m.x3)**2 - (-0.44093 + m.x6)**2 + m.x7
    <= 0)
m.e1201 = Constraint(expr= -(-0.52097 + m.x3)**2 - (-0.72367 + m.x6)**2 + m.x7
    <= 0)
m.e1202 = Constraint(expr= -(-0.73243 + m.x3)**2 - (-0.52373 + m.x6)**2 + m.x7
    <= 0)
m.e1203 = Constraint(expr= -(-0.56217 + m.x3)**2 - (-0.45687 + m.x6)**2 + m.x7
    <= 0)
m.e1204 = Constraint(expr= -(-0.15523 + m.x3)**2 - (-0.49453 + m.x6)**2 + m.x7
    <= 0)
m.e1205 = Constraint(expr= -(-0.75537 + m.x3)**2 - (-0.66207 + m.x6)**2 + m.x7
    <= 0)
m.e1206 = Constraint(expr= -(-0.86603 + m.x3)**2 - (-0.83333 + m.x6)**2 + m.x7
    <= 0)
m.e1207 = Constraint(expr= -(-0.02057 + m.x3)**2 - (-0.45927 + m.x6)**2 + m.x7
    <= 0)
m.e1208 = Constraint(expr= -(-0.34483 + m.x3)**2 - (-0.82013 + m.x6)**2 + m.x7
    <= 0)
m.e1209 = Constraint(expr= -(-0.47777 + m.x3)**2 - (-0.16847 + m.x6)**2 + m.x7
    <= 0)
m.e1210 = Constraint(expr= -(-0.87163 + m.x3)**2 - (-0.53493 + m.x6)**2 + m.x7
    <= 0)
m.e1211 = Constraint(expr= -(-0.44697 + m.x3)**2 - (-0.30967 + m.x6)**2 + m.x7
    <= 0)
m.e1212 = Constraint(expr= -(-0.52643 + m.x3)**2 - (-0.85773 + m.x6)**2 + m.x7
    <= 0)
m.e1213 = Constraint(expr= -(-0.44817 + m.x3)**2 - (-0.60287 + m.x6)**2 + m.x7
    <= 0)
m.e1214 = Constraint(expr= -(-0.18923 + m.x3)**2 - (-0.46853 + m.x6)**2 + m.x7
    <= 0)
m.e1215 = Constraint(expr= -(-0.20137 + m.x3)**2 - (-0.96807 + m.x6)**2 + m.x7
    <= 0)
m.e1216 = Constraint(expr= -(-0.54003 + m.x3)**2 - (-0.84733 + m.x6)**2 + m.x7
    <= 0)
m.e1217 = Constraint(expr= -(-0.62657 + m.x3)**2 - (-0.52527 + m.x6)**2 + m.x7
    <= 0)
m.e1218 = Constraint(expr= -(-0.05883 + m.x3)**2 - (-0.27413 + m.x6)**2 + m.x7
    <= 0)
m.e1219 = Constraint(expr= -(-0.84377 + m.x3)**2 - (-0.59447 + m.x6)**2 + m.x7
    <= 0)
m.e1220 = Constraint(expr= -(-0.02563 + m.x3)**2 - (-0.82893 + m.x6)**2 + m.x7
    <= 0)
m.e1221 = Constraint(expr= -(-0.17297 + m.x3)**2 - (-0.69567 + m.x6)**2 + m.x7
    <= 0)
m.e1222 = Constraint(expr= -(-0.52043 + m.x3)**2 - (-0.39173 + m.x6)**2 + m.x7
    <= 0)
m.e1223 = Constraint(expr= -(-0.13417 + m.x3)**2 - (-0.54887 + m.x6)**2 + m.x7
    <= 0)
m.e1224 = Constraint(expr= -(-0.42323 + m.x3)**2 - (-0.64253 + m.x6)**2 + m.x7
    <= 0)
m.e1225 = Constraint(expr= -(-0.44737 + m.x3)**2 - (-0.07407 + m.x6)**2 + m.x7
    <= 0)
m.e1226 = Constraint(expr= -(-0.41403 + m.x3)**2 - (-0.06133 + m.x6)**2 + m.x7
    <= 0)
m.e1227 = Constraint(expr= -(-0.03257 + m.x3)**2 - (-0.39127 + m.x6)**2 + m.x7
    <= 0)
m.e1228 = Constraint(expr= -(-0.97283 + m.x3)**2 - (-0.92813 + m.x6)**2 + m.x7
    <= 0)
m.e1229 = Constraint(expr= -(-0.00977 + m.x3)**2 - (-0.82047 + m.x6)**2 + m.x7
    <= 0)
m.e1230 = Constraint(expr= -(-0.37963 + m.x3)**2 - (-0.32293 + m.x6)**2 + m.x7
    <= 0)
m.e1231 = Constraint(expr= -(-0.69897 + m.x3)**2 - (-0.88167 + m.x6)**2 + m.x7
    <= 0)
m.e1232 = Constraint(expr= -(-0.71443 + m.x3)**2 - (-0.12573 + m.x6)**2 + m.x7
    <= 0)
m.e1233 = Constraint(expr= -(-0.62017 + m.x3)**2 - (-0.29487 + m.x6)**2 + m.x7
    <= 0)
m.e1234 = Constraint(expr= -(-0.85723 + m.x3)**2 - (-0.01653 + m.x6)**2 + m.x7
    <= 0)
m.e1235 = Constraint(expr= -(-0.49337 + m.x3)**2 - (-0.98007 + m.x6)**2 + m.x7
    <= 0)
m.e1236 = Constraint(expr= -(-0.48803 + m.x3)**2 - (-0.47533 + m.x6)**2 + m.x7
    <= 0)
m.e1237 = Constraint(expr= -(-0.23857 + m.x3)**2 - (-0.05727 + m.x6)**2 + m.x7
    <= 0)
m.e1238 = Constraint(expr= -(-0.08683 + m.x3)**2 - (-0.78213 + m.x6)**2 + m.x7
    <= 0)
m.e1239 = Constraint(expr= -(-0.97577 + m.x3)**2 - (-0.84647 + m.x6)**2 + m.x7
    <= 0)
m.e1240 = Constraint(expr= -(-0.93363 + m.x3)**2 - (-0.01693 + m.x6)**2 + m.x7
    <= 0)
m.e1241 = Constraint(expr= -(-0.02497 + m.x3)**2 - (-0.86767 + m.x6)**2 + m.x7
    <= 0)
m.e1242 = Constraint(expr= -(-0.10843 + m.x3)**2 - (-0.05973 + m.x6)**2 + m.x7
    <= 0)
m.e1243 = Constraint(expr= -(-0.90617 + m.x3)**2 - (-0.84087 + m.x6)**2 + m.x7
    <= 0)
m.e1244 = Constraint(expr= -(-0.49123 + m.x3)**2 - (-0.59053 + m.x6)**2 + m.x7
    <= 0)
m.e1245 = Constraint(expr= -(-0.33937 + m.x3)**2 - (-0.68607 + m.x6)**2 + m.x7
    <= 0)
m.e1246 = Constraint(expr= -(-0.76203 + m.x3)**2 - (-0.08933 + m.x6)**2 + m.x7
    <= 0)
m.e1247 = Constraint(expr= -(-0.24457 + m.x3)**2 - (-0.52327 + m.x6)**2 + m.x7
    <= 0)
m.e1248 = Constraint(expr= -(-0.40083 + m.x3)**2 - (-0.83613 + m.x6)**2 + m.x7
    <= 0)
m.e1249 = Constraint(expr= -(-0.74177 + m.x3)**2 - (-0.67247 + m.x6)**2 + m.x7
    <= 0)
m.e1250 = Constraint(expr= -(-0.68763 + m.x3)**2 - (-0.91093 + m.x6)**2 + m.x7
    <= 0)
m.e1251 = Constraint(expr= -(-0.15097 + m.x3)**2 - (-0.65367 + m.x6)**2 + m.x7
    <= 0)
m.e1252 = Constraint(expr= -(-0.70243 + m.x3)**2 - (-0.19373 + m.x6)**2 + m.x7
    <= 0)
m.e1253 = Constraint(expr= -(-0.99217 + m.x3)**2 - (-0.18687 + m.x6)**2 + m.x7
    <= 0)
m.e1254 = Constraint(expr= -(-0.32523 + m.x3)**2 - (-0.36453 + m.x6)**2 + m.x7
    <= 0)
m.e1255 = Constraint(expr= -(-0.98537 + m.x3)**2 - (-0.19207 + m.x6)**2 + m.x7
    <= 0)
m.e1256 = Constraint(expr= -(-0.23603 + m.x3)**2 - (-0.90333 + m.x6)**2 + m.x7
    <= 0)
m.e1257 = Constraint(expr= -(-0.05057 + m.x3)**2 - (-0.78927 + m.x6)**2 + m.x7
    <= 0)
m.e1258 = Constraint(expr= -(-0.91483 + m.x3)**2 - (-0.09013 + m.x6)**2 + m.x7
    <= 0)
m.e1259 = Constraint(expr= -(-0.30777 + m.x3)**2 - (-0.29847 + m.x6)**2 + m.x7
    <= 0)
m.e1260 = Constraint(expr= -(-0.64163 + m.x3)**2 - (-0.00493 + m.x6)**2 + m.x7
    <= 0)
m.e1261 = Constraint(expr= -(-0.07697 + m.x3)**2 - (-0.23967 + m.x6)**2 + m.x7
    <= 0)
m.e1262 = Constraint(expr= -(-0.49643 + m.x3)**2 - (-0.52773 + m.x6)**2 + m.x7
    <= 0)
m.e1263 = Constraint(expr= -(-0.87817 + m.x3)**2 - (-0.33287 + m.x6)**2 + m.x7
    <= 0)
m.e1264 = Constraint(expr= -(-0.35923 + m.x3)**2 - (-0.33853 + m.x6)**2 + m.x7
    <= 0)
m.e1265 = Constraint(expr= -(-0.43137 + m.x3)**2 - (-0.49807 + m.x6)**2 + m.x7
    <= 0)
m.e1266 = Constraint(expr= -(-0.91003 + m.x3)**2 - (-0.91733 + m.x6)**2 + m.x7
    <= 0)
m.e1267 = Constraint(expr= -(-0.65657 + m.x3)**2 - (-0.85527 + m.x6)**2 + m.x7
    <= 0)
m.e1268 = Constraint(expr= -(-0.62883 + m.x3)**2 - (-0.54413 + m.x6)**2 + m.x7
    <= 0)
m.e1269 = Constraint(expr= -(-0.67377 + m.x3)**2 - (-0.72447 + m.x6)**2 + m.x7
    <= 0)
m.e1270 = Constraint(expr= -(-0.79563 + m.x3)**2 - (-0.29893 + m.x6)**2 + m.x7
    <= 0)
m.e1271 = Constraint(expr= -(-0.80297 + m.x3)**2 - (-0.62567 + m.x6)**2 + m.x7
    <= 0)
m.e1272 = Constraint(expr= -(-0.49043 + m.x3)**2 - (-0.06173 + m.x6)**2 + m.x7
    <= 0)
m.e1273 = Constraint(expr= -(-0.56417 + m.x3)**2 - (-0.27887 + m.x6)**2 + m.x7
    <= 0)
m.e1274 = Constraint(expr= -(-0.59323 + m.x3)**2 - (-0.51253 + m.x6)**2 + m.x7
    <= 0)
m.e1275 = Constraint(expr= -(-0.67737 + m.x3)**2 - (-0.60407 + m.x6)**2 + m.x7
    <= 0)
m.e1276 = Constraint(expr= -(-0.78403 + m.x3)**2 - (-0.13133 + m.x6)**2 + m.x7
    <= 0)
m.e1277 = Constraint(expr= -(-0.06257 + m.x3)**2 - (-0.72127 + m.x6)**2 + m.x7
    <= 0)
m.e1278 = Constraint(expr= -(-0.54283 + m.x3)**2 - (-0.19813 + m.x6)**2 + m.x7
    <= 0)
m.e1279 = Constraint(expr= -(-0.83977 + m.x3)**2 - (-0.95047 + m.x6)**2 + m.x7
    <= 0)
m.e1280 = Constraint(expr= -(-0.14963 + m.x3)**2 - (-0.79293 + m.x6)**2 + m.x7
    <= 0)
m.e1281 = Constraint(expr= -(-0.32897 + m.x3)**2 - (-0.81167 + m.x6)**2 + m.x7
    <= 0)
m.e1282 = Constraint(expr= -(-0.68443 + m.x3)**2 - (-0.79573 + m.x6)**2 + m.x7
    <= 0)
m.e1283 = Constraint(expr= -(-0.05017 + m.x3)**2 - (-0.02487 + m.x6)**2 + m.x7
    <= 0)
m.e1284 = Constraint(expr= -(-0.02723 + m.x3)**2 - (-0.88653 + m.x6)**2 + m.x7
    <= 0)
m.e1285 = Constraint(expr= -(-0.72337 + m.x3)**2 - (-0.51007 + m.x6)**2 + m.x7
    <= 0)
m.e1286 = Constraint(expr= -(-0.85803 + m.x3)**2 - (-0.54533 + m.x6)**2 + m.x7
    <= 0)
m.e1287 = Constraint(expr= -(-0.26857 + m.x3)**2 - (-0.38727 + m.x6)**2 + m.x7
    <= 0)
m.e1288 = Constraint(expr= -(-0.65683 + m.x3)**2 - (-0.05213 + m.x6)**2 + m.x7
    <= 0)
m.e1289 = Constraint(expr= -(-0.80577 + m.x3)**2 - (-0.97647 + m.x6)**2 + m.x7
    <= 0)
m.e1290 = Constraint(expr= -(-0.70363 + m.x3)**2 - (-0.48693 + m.x6)**2 + m.x7
    <= 0)
m.e1291 = Constraint(expr= -(-0.65497 + m.x3)**2 - (-0.79767 + m.x6)**2 + m.x7
    <= 0)
m.e1292 = Constraint(expr= -(-0.07843 + m.x3)**2 - (-0.72973 + m.x6)**2 + m.x7
    <= 0)
m.e1293 = Constraint(expr= -(-0.33617 + m.x3)**2 - (-0.57087 + m.x6)**2 + m.x7
    <= 0)
m.e1294 = Constraint(expr= -(-0.66123 + m.x3)**2 - (-0.46053 + m.x6)**2 + m.x7
    <= 0)
m.e1295 = Constraint(expr= -(-0.56937 + m.x3)**2 - (-0.21607 + m.x6)**2 + m.x7
    <= 0)
m.e1296 = Constraint(expr= -(-0.13203 + m.x3)**2 - (-0.15933 + m.x6)**2 + m.x7
    <= 0)
m.e1297 = Constraint(expr= -(-0.27457 + m.x3)**2 - (-0.85327 + m.x6)**2 + m.x7
    <= 0)
m.e1298 = Constraint(expr= -(-0.97083 + m.x3)**2 - (-0.10613 + m.x6)**2 + m.x7
    <= 0)
m.e1299 = Constraint(expr= -(-0.57177 + m.x3)**2 - (-0.80247 + m.x6)**2 + m.x7
    <= 0)
m.e1300 = Constraint(expr= -(-0.45763 + m.x3)**2 - (-0.38093 + m.x6)**2 + m.x7
    <= 0)
m.e1301 = Constraint(expr= -(-0.78097 + m.x3)**2 - (-0.58367 + m.x6)**2 + m.x7
    <= 0)
m.e1302 = Constraint(expr= -(-0.67243 + m.x3)**2 - (-0.86373 + m.x6)**2 + m.x7
    <= 0)
m.e1303 = Constraint(expr= -(-0.42217 + m.x3)**2 - (-0.91687 + m.x6)**2 + m.x7
    <= 0)
m.e1304 = Constraint(expr= -(-0.49523 + m.x3)**2 - (-0.23453 + m.x6)**2 + m.x7
    <= 0)
m.e1305 = Constraint(expr= -(-0.21537 + m.x3)**2 - (-0.72207 + m.x6)**2 + m.x7
    <= 0)
m.e1306 = Constraint(expr= -(-0.60603 + m.x3)**2 - (-0.97333 + m.x6)**2 + m.x7
    <= 0)
m.e1307 = Constraint(expr= -(-0.08057 + m.x3)**2 - (-0.11927 + m.x6)**2 + m.x7
    <= 0)
m.e1308 = Constraint(expr= -(-0.48483 + m.x3)**2 - (-0.36013 + m.x6)**2 + m.x7
    <= 0)
m.e1309 = Constraint(expr= -(-0.13777 + m.x3)**2 - (-0.42847 + m.x6)**2 + m.x7
    <= 0)
m.e1310 = Constraint(expr= -(-0.41163 + m.x3)**2 - (-0.47493 + m.x6)**2 + m.x7
    <= 0)
m.e1311 = Constraint(expr= -(-0.70697 + m.x3)**2 - (-0.16967 + m.x6)**2 + m.x7
    <= 0)
m.e1312 = Constraint(expr= -(-0.46643 + m.x3)**2 - (-0.19773 + m.x6)**2 + m.x7
    <= 0)
m.e1313 = Constraint(expr= -(-0.30817 + m.x3)**2 - (-0.06287 + m.x6)**2 + m.x7
    <= 0)
m.e1314 = Constraint(expr= -(-0.52923 + m.x3)**2 - (-0.20853 + m.x6)**2 + m.x7
    <= 0)
m.e1315 = Constraint(expr= -(-0.66137 + m.x3)**2 - (-0.02807 + m.x6)**2 + m.x7
    <= 0)
m.e1316 = Constraint(expr= -(-0.28003 + m.x3)**2 - (-0.98733 + m.x6)**2 + m.x7
    <= 0)
m.e1317 = Constraint(expr= -(-0.68657 + m.x3)**2 - (-0.18527 + m.x6)**2 + m.x7
    <= 0)
m.e1318 = Constraint(expr= -(-0.19883 + m.x3)**2 - (-0.81413 + m.x6)**2 + m.x7
    <= 0)
m.e1319 = Constraint(expr= -(-0.50377 + m.x3)**2 - (-0.85447 + m.x6)**2 + m.x7
    <= 0)
m.e1320 = Constraint(expr= -(-0.56563 + m.x3)**2 - (-0.76893 + m.x6)**2 + m.x7
    <= 0)
m.e1321 = Constraint(expr= -(-0.43297 + m.x3)**2 - (-0.55567 + m.x6)**2 + m.x7
    <= 0)
m.e1322 = Constraint(expr= -(-0.46043 + m.x3)**2 - (-0.73173 + m.x6)**2 + m.x7
    <= 0)
m.e1323 = Constraint(expr= -(-0.99417 + m.x3)**2 - (-0.00887 + m.x6)**2 + m.x7
    <= 0)
m.e1324 = Constraint(expr= -(-0.76323 + m.x3)**2 - (-0.38253 + m.x6)**2 + m.x7
    <= 0)
m.e1325 = Constraint(expr= -(-0.90737 + m.x3)**2 - (-0.13407 + m.x6)**2 + m.x7
    <= 0)
m.e1326 = Constraint(expr= -(-0.15403 + m.x3)**2 - (-0.20133 + m.x6)**2 + m.x7
    <= 0)
m.e1327 = Constraint(expr= -(-0.09257 + m.x3)**2 - (-0.05127 + m.x6)**2 + m.x7
    <= 0)
m.e1328 = Constraint(expr= -(-0.11283 + m.x3)**2 - (-0.46813 + m.x6)**2 + m.x7
    <= 0)
m.e1329 = Constraint(expr= -(-0.66977 + m.x3)**2 - (-0.08047 + m.x6)**2 + m.x7
    <= 0)
m.e1330 = Constraint(expr= -(-0.91963 + m.x3)**2 - (-0.26293 + m.x6)**2 + m.x7
    <= 0)
m.e1331 = Constraint(expr= -(-0.95897 + m.x3)**2 - (-0.74167 + m.x6)**2 + m.x7
    <= 0)
m.e1332 = Constraint(expr= -(-0.65443 + m.x3)**2 - (-0.46573 + m.x6)**2 + m.x7
    <= 0)
m.e1333 = Constraint(expr= -(-0.48017 + m.x3)**2 - (-0.75487 + m.x6)**2 + m.x7
    <= 0)
m.e1334 = Constraint(expr= -(-0.19723 + m.x3)**2 - (-0.75653 + m.x6)**2 + m.x7
    <= 0)
m.e1335 = Constraint(expr= -(-0.95337 + m.x3)**2 - (-0.04007 + m.x6)**2 + m.x7
    <= 0)
m.e1336 = Constraint(expr= -(-0.22803 + m.x3)**2 - (-0.61533 + m.x6)**2 + m.x7
    <= 0)
m.e1337 = Constraint(expr= -(-0.29857 + m.x3)**2 - (-0.71727 + m.x6)**2 + m.x7
    <= 0)
m.e1338 = Constraint(expr= -(-0.22683 + m.x3)**2 - (-0.32213 + m.x6)**2 + m.x7
    <= 0)
m.e1339 = Constraint(expr= -(-0.63577 + m.x3)**2 - (-0.10647 + m.x6)**2 + m.x7
    <= 0)
m.e1340 = Constraint(expr= -(-0.47363 + m.x3)**2 - (-0.95693 + m.x6)**2 + m.x7
    <= 0)
m.e1341 = Constraint(expr= -(-0.28497 + m.x3)**2 - (-0.72767 + m.x6)**2 + m.x7
    <= 0)
m.e1342 = Constraint(expr= -(-0.04843 + m.x3)**2 - (-0.39973 + m.x6)**2 + m.x7
    <= 0)
m.e1343 = Constraint(expr= -(-0.76617 + m.x3)**2 - (-0.30087 + m.x6)**2 + m.x7
    <= 0)
m.e1344 = Constraint(expr= -(-0.83123 + m.x3)**2 - (-0.33053 + m.x6)**2 + m.x7
    <= 0)
m.e1345 = Constraint(expr= -(-0.79937 + m.x3)**2 - (-0.74607 + m.x6)**2 + m.x7
    <= 0)
m.e1346 = Constraint(expr= -(-0.50203 + m.x3)**2 - (-0.22933 + m.x6)**2 + m.x7
    <= 0)
m.e1347 = Constraint(expr= -(-0.30457 + m.x3)**2 - (-0.18327 + m.x6)**2 + m.x7
    <= 0)
m.e1348 = Constraint(expr= -(-0.54083 + m.x3)**2 - (-0.37613 + m.x6)**2 + m.x7
    <= 0)
m.e1349 = Constraint(expr= -(-0.40177 + m.x3)**2 - (-0.93247 + m.x6)**2 + m.x7
    <= 0)
m.e1350 = Constraint(expr= -(-0.22763 + m.x3)**2 - (-0.85093 + m.x6)**2 + m.x7
    <= 0)
m.e1351 = Constraint(expr= -(-0.41097 + m.x3)**2 - (-0.51367 + m.x6)**2 + m.x7
    <= 0)
m.e1352 = Constraint(expr= -(-0.64243 + m.x3)**2 - (-0.53373 + m.x6)**2 + m.x7
    <= 0)
m.e1353 = Constraint(expr= -(-0.85217 + m.x3)**2 - (-0.64687 + m.x6)**2 + m.x7
    <= 0)
m.e1354 = Constraint(expr= -(-0.66523 + m.x3)**2 - (-0.10453 + m.x6)**2 + m.x7
    <= 0)
m.e1355 = Constraint(expr= -(-0.44537 + m.x3)**2 - (-0.25207 + m.x6)**2 + m.x7
    <= 0)
m.e1356 = Constraint(expr= -(-0.97603 + m.x3)**2 - (-0.04333 + m.x6)**2 + m.x7
    <= 0)
m.e1357 = Constraint(expr= -(-0.11057 + m.x3)**2 - (-0.44927 + m.x6)**2 + m.x7
    <= 0)
m.e1358 = Constraint(expr= -(-0.05483 + m.x3)**2 - (-0.63013 + m.x6)**2 + m.x7
    <= 0)
m.e1359 = Constraint(expr= -(-0.96777 + m.x3)**2 - (-0.55847 + m.x6)**2 + m.x7
    <= 0)
m.e1360 = Constraint(expr= -(-0.18163 + m.x3)**2 - (-0.94493 + m.x6)**2 + m.x7
    <= 0)
m.e1361 = Constraint(expr= -(-0.33697 + m.x3)**2 - (-0.09967 + m.x6)**2 + m.x7
    <= 0)
m.e1362 = Constraint(expr= -(-0.43643 + m.x3)**2 - (-0.86773 + m.x6)**2 + m.x7
    <= 0)
m.e1363 = Constraint(expr= -(-0.73817 + m.x3)**2 - (-0.79287 + m.x6)**2 + m.x7
    <= 0)
m.e1364 = Constraint(expr= -(-0.69923 + m.x3)**2 - (-0.07853 + m.x6)**2 + m.x7
    <= 0)
m.e1365 = Constraint(expr= -(-0.89137 + m.x3)**2 - (-0.55807 + m.x6)**2 + m.x7
    <= 0)
m.e1366 = Constraint(expr= -(-0.65003 + m.x3)**2 - (-0.05733 + m.x6)**2 + m.x7
    <= 0)
m.e1367 = Constraint(expr= -(-0.71657 + m.x3)**2 - (-0.51527 + m.x6)**2 + m.x7
    <= 0)
m.e1368 = Constraint(expr= -(-0.76883 + m.x3)**2 - (-0.08413 + m.x6)**2 + m.x7
    <= 0)
m.e1369 = Constraint(expr= -(-0.33377 + m.x3)**2 - (-0.98447 + m.x6)**2 + m.x7
    <= 0)
m.e1370 = Constraint(expr= -(-0.33563 + m.x3)**2 - (-0.23893 + m.x6)**2 + m.x7
    <= 0)
m.e1371 = Constraint(expr= -(-0.06297 + m.x3)**2 - (-0.48567 + m.x6)**2 + m.x7
    <= 0)
m.e1372 = Constraint(expr= -(-0.43043 + m.x3)**2 - (-0.40173 + m.x6)**2 + m.x7
    <= 0)
m.e1373 = Constraint(expr= -(-0.42417 + m.x3)**2 - (-0.73887 + m.x6)**2 + m.x7
    <= 0)
m.e1374 = Constraint(expr= -(-0.93323 + m.x3)**2 - (-0.25253 + m.x6)**2 + m.x7
    <= 0)
m.e1375 = Constraint(expr= -(-0.13737 + m.x3)**2 - (-0.66407 + m.x6)**2 + m.x7
    <= 0)
m.e1376 = Constraint(expr= -(-0.52403 + m.x3)**2 - (-0.27133 + m.x6)**2 + m.x7
    <= 0)
m.e1377 = Constraint(expr= -(-0.12257 + m.x3)**2 - (-0.38127 + m.x6)**2 + m.x7
    <= 0)
m.e1378 = Constraint(expr= -(-0.68283 + m.x3)**2 - (-0.73813 + m.x6)**2 + m.x7
    <= 0)
m.e1379 = Constraint(expr= -(-0.49977 + m.x3)**2 - (-0.21047 + m.x6)**2 + m.x7
    <= 0)
m.e1380 = Constraint(expr= -(-0.68963 + m.x3)**2 - (-0.73293 + m.x6)**2 + m.x7
    <= 0)
m.e1381 = Constraint(expr= -(-0.58897 + m.x3)**2 - (-0.67167 + m.x6)**2 + m.x7
    <= 0)
m.e1382 = Constraint(expr= -(-0.62443 + m.x3)**2 - (-0.13573 + m.x6)**2 + m.x7
    <= 0)
m.e1383 = Constraint(expr= -(-0.91017 + m.x3)**2 - (-0.48487 + m.x6)**2 + m.x7
    <= 0)
m.e1384 = Constraint(expr= -(-0.36723 + m.x3)**2 - (-0.62653 + m.x6)**2 + m.x7
    <= 0)
m.e1385 = Constraint(expr= -(-0.18337 + m.x3)**2 - (-0.57007 + m.x6)**2 + m.x7
    <= 0)
m.e1386 = Constraint(expr= -(-0.59803 + m.x3)**2 - (-0.68533 + m.x6)**2 + m.x7
    <= 0)
m.e1387 = Constraint(expr= -(-0.32857 + m.x3)**2 - (-0.04727 + m.x6)**2 + m.x7
    <= 0)
m.e1388 = Constraint(expr= -(-0.79683 + m.x3)**2 - (-0.59213 + m.x6)**2 + m.x7
    <= 0)
m.e1389 = Constraint(expr= -(-0.46577 + m.x3)**2 - (-0.23647 + m.x6)**2 + m.x7
    <= 0)
m.e1390 = Constraint(expr= -(-0.24363 + m.x3)**2 - (-0.42693 + m.x6)**2 + m.x7
    <= 0)
m.e1391 = Constraint(expr= -(-0.91497 + m.x3)**2 - (-0.65767 + m.x6)**2 + m.x7
    <= 0)
m.e1392 = Constraint(expr= -(-0.01843 + m.x3)**2 - (-0.06973 + m.x6)**2 + m.x7
    <= 0)
m.e1393 = Constraint(expr= -(-0.19617 + m.x3)**2 - (-0.03087 + m.x6)**2 + m.x7
    <= 0)
m.e1394 = Constraint(expr= -(-0.00123 + m.x3)**2 - (-0.20053 + m.x6)**2 + m.x7
    <= 0)
m.e1395 = Constraint(expr= -(-0.02937 + m.x3)**2 - (-0.27607 + m.x6)**2 + m.x7
    <= 0)
m.e1396 = Constraint(expr= -(-0.87203 + m.x3)**2 - (-0.29933 + m.x6)**2 + m.x7
    <= 0)
m.e1397 = Constraint(expr= -(-0.33457 + m.x3)**2 - (-0.51327 + m.x6)**2 + m.x7
    <= 0)
m.e1398 = Constraint(expr= -(-0.11083 + m.x3)**2 - (-0.64613 + m.x6)**2 + m.x7
    <= 0)
m.e1399 = Constraint(expr= -(-0.23177 + m.x3)**2 - (-0.06247 + m.x6)**2 + m.x7
    <= 0)
m.e1400 = Constraint(expr= -(-0.99763 + m.x3)**2 - (-0.32093 + m.x6)**2 + m.x7
    <= 0)
m.e1401 = Constraint(expr= -(-0.04097 + m.x3)**2 - (-0.44367 + m.x6)**2 + m.x7
    <= 0)
m.e1402 = Constraint(expr= -(-0.61243 + m.x3)**2 - (-0.20373 + m.x6)**2 + m.x7
    <= 0)
m.e1403 = Constraint(expr= -(-0.28217 + m.x3)**2 - (-0.37687 + m.x6)**2 + m.x7
    <= 0)
m.e1404 = Constraint(expr= -(-0.83523 + m.x3)**2 - (-0.97453 + m.x6)**2 + m.x7
    <= 0)
m.e1405 = Constraint(expr= -(-0.67537 + m.x3)**2 - (-0.78207 + m.x6)**2 + m.x7
    <= 0)
m.e1406 = Constraint(expr= -(-0.34603 + m.x3)**2 - (-0.11333 + m.x6)**2 + m.x7
    <= 0)
m.e1407 = Constraint(expr= -(-0.14057 + m.x3)**2 - (-0.77927 + m.x6)**2 + m.x7
    <= 0)
m.e1408 = Constraint(expr= -(-0.62483 + m.x3)**2 - (-0.90013 + m.x6)**2 + m.x7
    <= 0)
m.e1409 = Constraint(expr= -(-0.79777 + m.x3)**2 - (-0.68847 + m.x6)**2 + m.x7
    <= 0)
m.e1410 = Constraint(expr= -(-0.95163 + m.x3)**2 - (-0.41493 + m.x6)**2 + m.x7
    <= 0)
m.e1411 = Constraint(expr= -(-0.96697 + m.x3)**2 - (-0.02967 + m.x6)**2 + m.x7
    <= 0)
m.e1412 = Constraint(expr= -(-0.40643 + m.x3)**2 - (-0.53773 + m.x6)**2 + m.x7
    <= 0)
m.e1413 = Constraint(expr= -(-0.16817 + m.x3)**2 - (-0.52287 + m.x6)**2 + m.x7
    <= 0)
m.e1414 = Constraint(expr= -(-0.86923 + m.x3)**2 - (-0.94853 + m.x6)**2 + m.x7
    <= 0)
m.e1415 = Constraint(expr= -(-0.12137 + m.x3)**2 - (-0.08807 + m.x6)**2 + m.x7
    <= 0)
m.e1416 = Constraint(expr= -(-0.02003 + m.x3)**2 - (-0.12733 + m.x6)**2 + m.x7
    <= 0)
m.e1417 = Constraint(expr= -(-0.74657 + m.x3)**2 - (-0.84527 + m.x6)**2 + m.x7
    <= 0)
m.e1418 = Constraint(expr= -(-0.33883 + m.x3)**2 - (-0.35413 + m.x6)**2 + m.x7
    <= 0)
m.e1419 = Constraint(expr= -(-0.16377 + m.x3)**2 - (-0.11447 + m.x6)**2 + m.x7
    <= 0)
m.e1420 = Constraint(expr= -(-0.10563 + m.x3)**2 - (-0.70893 + m.x6)**2 + m.x7
    <= 0)
m.e1421 = Constraint(expr= -(-0.69297 + m.x3)**2 - (-0.41567 + m.x6)**2 + m.x7
    <= 0)
m.e1422 = Constraint(expr= -(-0.40043 + m.x3)**2 - (-0.07173 + m.x6)**2 + m.x7
    <= 0)
m.e1423 = Constraint(expr= -(-0.85417 + m.x3)**2 - (-0.46887 + m.x6)**2 + m.x7
    <= 0)
m.e1424 = Constraint(expr= -(-0.10323 + m.x3)**2 - (-0.12253 + m.x6)**2 + m.x7
    <= 0)
m.e1425 = Constraint(expr= -(-0.36737 + m.x3)**2 - (-0.19407 + m.x6)**2 + m.x7
    <= 0)
m.e1426 = Constraint(expr= -(-0.89403 + m.x3)**2 - (-0.34133 + m.x6)**2 + m.x7
    <= 0)
m.e1427 = Constraint(expr= -(-0.15257 + m.x3)**2 - (-0.71127 + m.x6)**2 + m.x7
    <= 0)
m.e1428 = Constraint(expr= -(-0.25283 + m.x3)**2 - (-0.00813 + m.x6)**2 + m.x7
    <= 0)
m.e1429 = Constraint(expr= -(-0.32977 + m.x3)**2 - (-0.34047 + m.x6)**2 + m.x7
    <= 0)
m.e1430 = Constraint(expr= -(-0.45963 + m.x3)**2 - (-0.20293 + m.x6)**2 + m.x7
    <= 0)
m.e1431 = Constraint(expr= -(-0.21897 + m.x3)**2 - (-0.60167 + m.x6)**2 + m.x7
    <= 0)
m.e1432 = Constraint(expr= -(-0.59443 + m.x3)**2 - (-0.80573 + m.x6)**2 + m.x7
    <= 0)
m.e1433 = Constraint(expr= -(-0.34017 + m.x3)**2 - (-0.21487 + m.x6)**2 + m.x7
    <= 0)
m.e1434 = Constraint(expr= -(-0.53723 + m.x3)**2 - (-0.49653 + m.x6)**2 + m.x7
    <= 0)
m.e1435 = Constraint(expr= -(-0.41337 + m.x3)**2 - (-0.10007 + m.x6)**2 + m.x7
    <= 0)
m.e1436 = Constraint(expr= -(-0.96803 + m.x3)**2 - (-0.75533 + m.x6)**2 + m.x7
    <= 0)
m.e1437 = Constraint(expr= -(-0.35857 + m.x3)**2 - (-0.37727 + m.x6)**2 + m.x7
    <= 0)
m.e1438 = Constraint(expr= -(-0.36683 + m.x3)**2 - (-0.86213 + m.x6)**2 + m.x7
    <= 0)
m.e1439 = Constraint(expr= -(-0.29577 + m.x3)**2 - (-0.36647 + m.x6)**2 + m.x7
    <= 0)
m.e1440 = Constraint(expr= -(-0.01363 + m.x3)**2 - (-0.89693 + m.x6)**2 + m.x7
    <= 0)
m.e1441 = Constraint(expr= -(-0.54497 + m.x3)**2 - (-0.58767 + m.x6)**2 + m.x7
    <= 0)
m.e1442 = Constraint(expr= -(-0.98843 + m.x3)**2 - (-0.73973 + m.x6)**2 + m.x7
    <= 0)
m.e1443 = Constraint(expr= -(-0.62617 + m.x3)**2 - (-0.76087 + m.x6)**2 + m.x7
    <= 0)
m.e1444 = Constraint(expr= -(-0.17123 + m.x3)**2 - (-0.07053 + m.x6)**2 + m.x7
    <= 0)
m.e1445 = Constraint(expr= -(-0.25937 + m.x3)**2 - (-0.80607 + m.x6)**2 + m.x7
    <= 0)
m.e1446 = Constraint(expr= -(-0.24203 + m.x3)**2 - (-0.36933 + m.x6)**2 + m.x7
    <= 0)
m.e1447 = Constraint(expr= -(-0.36457 + m.x3)**2 - (-0.84327 + m.x6)**2 + m.x7
    <= 0)
m.e1448 = Constraint(expr= -(-0.68083 + m.x3)**2 - (-0.91613 + m.x6)**2 + m.x7
    <= 0)
m.e1449 = Constraint(expr= -(-0.06177 + m.x3)**2 - (-0.19247 + m.x6)**2 + m.x7
    <= 0)
m.e1450 = Constraint(expr= -(-0.76763 + m.x3)**2 - (-0.79093 + m.x6)**2 + m.x7
    <= 0)
m.e1451 = Constraint(expr= -(-0.67097 + m.x3)**2 - (-0.37367 + m.x6)**2 + m.x7
    <= 0)
m.e1452 = Constraint(expr= -(-0.58243 + m.x3)**2 - (-0.87373 + m.x6)**2 + m.x7
    <= 0)
m.e1453 = Constraint(expr= -(-0.71217 + m.x3)**2 - (-0.10687 + m.x6)**2 + m.x7
    <= 0)
m.e1454 = Constraint(expr= -(-0.00523 + m.x3)**2 - (-0.84453 + m.x6)**2 + m.x7
    <= 0)
m.e1455 = Constraint(expr= -(-0.90537 + m.x3)**2 - (-0.31207 + m.x6)**2 + m.x7
    <= 0)
m.e1456 = Constraint(expr= -(-0.71603 + m.x3)**2 - (-0.18333 + m.x6)**2 + m.x7
    <= 0)
m.e1457 = Constraint(expr= -(-0.17057 + m.x3)**2 - (-0.10927 + m.x6)**2 + m.x7
    <= 0)
m.e1458 = Constraint(expr= -(-0.19483 + m.x3)**2 - (-0.17013 + m.x6)**2 + m.x7
    <= 0)
m.e1459 = Constraint(expr= -(-0.62777 + m.x3)**2 - (-0.81847 + m.x6)**2 + m.x7
    <= 0)
m.e1460 = Constraint(expr= -(-0.72163 + m.x3)**2 - (-0.88493 + m.x6)**2 + m.x7
    <= 0)
m.e1461 = Constraint(expr= -(-0.59697 + m.x3)**2 - (-0.95967 + m.x6)**2 + m.x7
    <= 0)
m.e1462 = Constraint(expr= -(-0.37643 + m.x3)**2 - (-0.20773 + m.x6)**2 + m.x7
    <= 0)
m.e1463 = Constraint(expr= -(-0.59817 + m.x3)**2 - (-0.25287 + m.x6)**2 + m.x7
    <= 0)
m.e1464 = Constraint(expr= -(-0.03923 + m.x3)**2 - (-0.81853 + m.x6)**2 + m.x7
    <= 0)
m.e1465 = Constraint(expr= -(-0.35137 + m.x3)**2 - (-0.61807 + m.x6)**2 + m.x7
    <= 0)
m.e1466 = Constraint(expr= -(-0.39003 + m.x3)**2 - (-0.19733 + m.x6)**2 + m.x7
    <= 0)
m.e1467 = Constraint(expr= -(-0.77657 + m.x3)**2 - (-0.17527 + m.x6)**2 + m.x7
    <= 0)
m.e1468 = Constraint(expr= -(-0.90883 + m.x3)**2 - (-0.62413 + m.x6)**2 + m.x7
    <= 0)
m.e1469 = Constraint(expr= -(-0.99377 + m.x3)**2 - (-0.24447 + m.x6)**2 + m.x7
    <= 0)
m.e1470 = Constraint(expr= -(-0.87563 + m.x3)**2 - (-0.17893 + m.x6)**2 + m.x7
    <= 0)
m.e1471 = Constraint(expr= -(-0.32297 + m.x3)**2 - (-0.34567 + m.x6)**2 + m.x7
    <= 0)
m.e1472 = Constraint(expr= -(-0.37043 + m.x3)**2 - (-0.74173 + m.x6)**2 + m.x7
    <= 0)
m.e1473 = Constraint(expr= -(-0.28417 + m.x3)**2 - (-0.19887 + m.x6)**2 + m.x7
    <= 0)
m.e1474 = Constraint(expr= -(-0.27323 + m.x3)**2 - (-0.99253 + m.x6)**2 + m.x7
    <= 0)
m.e1475 = Constraint(expr= -(-0.59737 + m.x3)**2 - (-0.72407 + m.x6)**2 + m.x7
    <= 0)
m.e1476 = Constraint(expr= -(-0.26403 + m.x3)**2 - (-0.41133 + m.x6)**2 + m.x7
    <= 0)
m.e1477 = Constraint(expr= -(-0.18257 + m.x3)**2 - (-0.04127 + m.x6)**2 + m.x7
    <= 0)
m.e1478 = Constraint(expr= -(-0.82283 + m.x3)**2 - (-0.27813 + m.x6)**2 + m.x7
    <= 0)
m.e1479 = Constraint(expr= -(-0.15977 + m.x3)**2 - (-0.47047 + m.x6)**2 + m.x7
    <= 0)
m.e1480 = Constraint(expr= -(-0.22963 + m.x3)**2 - (-0.67293 + m.x6)**2 + m.x7
    <= 0)
m.e1481 = Constraint(expr= -(-0.84897 + m.x3)**2 - (-0.53167 + m.x6)**2 + m.x7
    <= 0)
m.e1482 = Constraint(expr= -(-0.56443 + m.x3)**2 - (-0.47573 + m.x6)**2 + m.x7
    <= 0)
m.e1483 = Constraint(expr= -(-0.77017 + m.x3)**2 - (-0.94487 + m.x6)**2 + m.x7
    <= 0)
m.e1484 = Constraint(expr= -(-0.70723 + m.x3)**2 - (-0.36653 + m.x6)**2 + m.x7
    <= 0)
m.e1485 = Constraint(expr= -(-0.64337 + m.x3)**2 - (-0.63007 + m.x6)**2 + m.x7
    <= 0)
m.e1486 = Constraint(expr= -(-0.33803 + m.x3)**2 - (-0.82533 + m.x6)**2 + m.x7
    <= 0)
m.e1487 = Constraint(expr= -(-0.38857 + m.x3)**2 - (-0.70727 + m.x6)**2 + m.x7
    <= 0)
m.e1488 = Constraint(expr= -(-0.93683 + m.x3)**2 - (-0.13213 + m.x6)**2 + m.x7
    <= 0)
m.e1489 = Constraint(expr= -(-0.12577 + m.x3)**2 - (-0.49647 + m.x6)**2 + m.x7
    <= 0)
m.e1490 = Constraint(expr= -(-0.78363 + m.x3)**2 - (-0.36693 + m.x6)**2 + m.x7
    <= 0)
m.e1491 = Constraint(expr= -(-0.17497 + m.x3)**2 - (-0.51767 + m.x6)**2 + m.x7
    <= 0)
m.e1492 = Constraint(expr= -(-0.95843 + m.x3)**2 - (-0.40973 + m.x6)**2 + m.x7
    <= 0)
m.e1493 = Constraint(expr= -(-0.05617 + m.x3)**2 - (-0.49087 + m.x6)**2 + m.x7
    <= 0)
m.e1494 = Constraint(expr= -(-0.34123 + m.x3)**2 - (-0.94053 + m.x6)**2 + m.x7
    <= 0)
m.e1495 = Constraint(expr= -(-0.48937 + m.x3)**2 - (-0.33607 + m.x6)**2 + m.x7
    <= 0)
m.e1496 = Constraint(expr= -(-0.61203 + m.x3)**2 - (-0.43933 + m.x6)**2 + m.x7
    <= 0)
m.e1497 = Constraint(expr= -(-0.39457 + m.x3)**2 - (-0.17327 + m.x6)**2 + m.x7
    <= 0)
m.e1498 = Constraint(expr= -(-0.25083 + m.x3)**2 - (-0.18613 + m.x6)**2 + m.x7
    <= 0)
m.e1499 = Constraint(expr= -(-0.89177 + m.x3)**2 - (-0.32247 + m.x6)**2 + m.x7
    <= 0)
m.e1500 = Constraint(expr= -(-0.53763 + m.x3)**2 - (-0.26093 + m.x6)**2 + m.x7
    <= 0)
m.e1501 = Constraint(expr= -(m.x1 - m.x2)**2 - (m.x4 - m.x5)**2
    <= -0.3333333333333333)
m.e1502 = Constraint(expr= -(m.x1 - m.x3)**2 - (m.x4 - m.x6)**2
    <= -0.3333333333333333)
m.e1503 = Constraint(expr= -(m.x2 - m.x3)**2 - (m.x5 - m.x6)**2
    <= -0.3333333333333333)
