# NLP written by GAMS Convert at 05/15/24 11:45:57
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#      3003        0        0     3003        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#         7        7        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#      9012     3000     6012
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
m.e501 = Constraint(expr= -(-0.30097 + m.x1)**2 - (-0.30367 + m.x4)**2 + m.x7
    <= 0)
m.e502 = Constraint(expr= -(-0.55243 + m.x1)**2 - (-0.54373 + m.x4)**2 + m.x7
    <= 0)
m.e503 = Constraint(expr= -(-0.14217 + m.x1)**2 - (-0.83687 + m.x4)**2 + m.x7
    <= 0)
m.e504 = Constraint(expr= -(-0.17523 + m.x1)**2 - (-0.71453 + m.x4)**2 + m.x7
    <= 0)
m.e505 = Constraint(expr= -(-0.13537 + m.x1)**2 - (-0.84207 + m.x4)**2 + m.x7
    <= 0)
m.e506 = Constraint(expr= -(-0.08603 + m.x1)**2 - (-0.25333 + m.x4)**2 + m.x7
    <= 0)
m.e507 = Constraint(expr= -(-0.20057 + m.x1)**2 - (-0.43927 + m.x4)**2 + m.x7
    <= 0)
m.e508 = Constraint(expr= -(-0.76483 + m.x1)**2 - (-0.44013 + m.x4)**2 + m.x7
    <= 0)
m.e509 = Constraint(expr= -(-0.45777 + m.x1)**2 - (-0.94847 + m.x4)**2 + m.x7
    <= 0)
m.e510 = Constraint(expr= -(-0.49163 + m.x1)**2 - (-0.35493 + m.x4)**2 + m.x7
    <= 0)
m.e511 = Constraint(expr= -(-0.22697 + m.x1)**2 - (-0.88967 + m.x4)**2 + m.x7
    <= 0)
m.e512 = Constraint(expr= -(-0.34643 + m.x1)**2 - (-0.87773 + m.x4)**2 + m.x7
    <= 0)
m.e513 = Constraint(expr= -(-0.02817 + m.x1)**2 - (-0.98287 + m.x4)**2 + m.x7
    <= 0)
m.e514 = Constraint(expr= -(-0.20923 + m.x1)**2 - (-0.68853 + m.x4)**2 + m.x7
    <= 0)
m.e515 = Constraint(expr= -(-0.58137 + m.x1)**2 - (-0.14807 + m.x4)**2 + m.x7
    <= 0)
m.e516 = Constraint(expr= -(-0.76003 + m.x1)**2 - (-0.26733 + m.x4)**2 + m.x7
    <= 0)
m.e517 = Constraint(expr= -(-0.80657 + m.x1)**2 - (-0.50527 + m.x4)**2 + m.x7
    <= 0)
m.e518 = Constraint(expr= -(-0.47883 + m.x1)**2 - (-0.89413 + m.x4)**2 + m.x7
    <= 0)
m.e519 = Constraint(expr= -(-0.82377 + m.x1)**2 - (-0.37447 + m.x4)**2 + m.x7
    <= 0)
m.e520 = Constraint(expr= -(-0.64563 + m.x1)**2 - (-0.64893 + m.x4)**2 + m.x7
    <= 0)
m.e521 = Constraint(expr= -(-0.95297 + m.x1)**2 - (-0.27567 + m.x4)**2 + m.x7
    <= 0)
m.e522 = Constraint(expr= -(-0.34043 + m.x1)**2 - (-0.41173 + m.x4)**2 + m.x7
    <= 0)
m.e523 = Constraint(expr= -(-0.71417 + m.x1)**2 - (-0.92887 + m.x4)**2 + m.x7
    <= 0)
m.e524 = Constraint(expr= -(-0.44323 + m.x1)**2 - (-0.86253 + m.x4)**2 + m.x7
    <= 0)
m.e525 = Constraint(expr= -(-0.82737 + m.x1)**2 - (-0.25407 + m.x4)**2 + m.x7
    <= 0)
m.e526 = Constraint(expr= -(-0.63403 + m.x1)**2 - (-0.48133 + m.x4)**2 + m.x7
    <= 0)
m.e527 = Constraint(expr= -(-0.21257 + m.x1)**2 - (-0.37127 + m.x4)**2 + m.x7
    <= 0)
m.e528 = Constraint(expr= -(-0.39283 + m.x1)**2 - (-0.54813 + m.x4)**2 + m.x7
    <= 0)
m.e529 = Constraint(expr= -(-0.98977 + m.x1)**2 - (-0.60047 + m.x4)**2 + m.x7
    <= 0)
m.e530 = Constraint(expr= -(-0.99963 + m.x1)**2 - (-0.14293 + m.x4)**2 + m.x7
    <= 0)
m.e531 = Constraint(expr= -(-0.47897 + m.x1)**2 - (-0.46167 + m.x4)**2 + m.x7
    <= 0)
m.e532 = Constraint(expr= -(-0.53443 + m.x1)**2 - (-0.14573 + m.x4)**2 + m.x7
    <= 0)
m.e533 = Constraint(expr= -(-0.20017 + m.x1)**2 - (-0.67487 + m.x4)**2 + m.x7
    <= 0)
m.e534 = Constraint(expr= -(-0.87723 + m.x1)**2 - (-0.23653 + m.x4)**2 + m.x7
    <= 0)
m.e535 = Constraint(expr= -(-0.87337 + m.x1)**2 - (-0.16007 + m.x4)**2 + m.x7
    <= 0)
m.e536 = Constraint(expr= -(-0.70803 + m.x1)**2 - (-0.89533 + m.x4)**2 + m.x7
    <= 0)
m.e537 = Constraint(expr= -(-0.41857 + m.x1)**2 - (-0.03727 + m.x4)**2 + m.x7
    <= 0)
m.e538 = Constraint(expr= -(-0.50683 + m.x1)**2 - (-0.40213 + m.x4)**2 + m.x7
    <= 0)
m.e539 = Constraint(expr= -(-0.95577 + m.x1)**2 - (-0.62647 + m.x4)**2 + m.x7
    <= 0)
m.e540 = Constraint(expr= -(-0.55363 + m.x1)**2 - (-0.83693 + m.x4)**2 + m.x7
    <= 0)
m.e541 = Constraint(expr= -(-0.80497 + m.x1)**2 - (-0.44767 + m.x4)**2 + m.x7
    <= 0)
m.e542 = Constraint(expr= -(-0.92843 + m.x1)**2 - (-0.07973 + m.x4)**2 + m.x7
    <= 0)
m.e543 = Constraint(expr= -(-0.48617 + m.x1)**2 - (-0.22087 + m.x4)**2 + m.x7
    <= 0)
m.e544 = Constraint(expr= -(-0.51123 + m.x1)**2 - (-0.81053 + m.x4)**2 + m.x7
    <= 0)
m.e545 = Constraint(expr= -(-0.71937 + m.x1)**2 - (-0.86607 + m.x4)**2 + m.x7
    <= 0)
m.e546 = Constraint(expr= -(-0.98203 + m.x1)**2 - (-0.50933 + m.x4)**2 + m.x7
    <= 0)
m.e547 = Constraint(expr= -(-0.42457 + m.x1)**2 - (-0.50327 + m.x4)**2 + m.x7
    <= 0)
m.e548 = Constraint(expr= -(-0.82083 + m.x1)**2 - (-0.45613 + m.x4)**2 + m.x7
    <= 0)
m.e549 = Constraint(expr= -(-0.72177 + m.x1)**2 - (-0.45247 + m.x4)**2 + m.x7
    <= 0)
m.e550 = Constraint(expr= -(-0.30763 + m.x1)**2 - (-0.73093 + m.x4)**2 + m.x7
    <= 0)
m.e551 = Constraint(expr= -(-0.93097 + m.x1)**2 - (-0.23367 + m.x4)**2 + m.x7
    <= 0)
m.e552 = Constraint(expr= -(-0.52243 + m.x1)**2 - (-0.21373 + m.x4)**2 + m.x7
    <= 0)
m.e553 = Constraint(expr= -(-0.57217 + m.x1)**2 - (-0.56687 + m.x4)**2 + m.x7
    <= 0)
m.e554 = Constraint(expr= -(-0.34523 + m.x1)**2 - (-0.58453 + m.x4)**2 + m.x7
    <= 0)
m.e555 = Constraint(expr= -(-0.36537 + m.x1)**2 - (-0.37207 + m.x4)**2 + m.x7
    <= 0)
m.e556 = Constraint(expr= -(-0.45603 + m.x1)**2 - (-0.32333 + m.x4)**2 + m.x7
    <= 0)
m.e557 = Constraint(expr= -(-0.23057 + m.x1)**2 - (-0.76927 + m.x4)**2 + m.x7
    <= 0)
m.e558 = Constraint(expr= -(-0.33483 + m.x1)**2 - (-0.71013 + m.x4)**2 + m.x7
    <= 0)
m.e559 = Constraint(expr= -(-0.28777 + m.x1)**2 - (-0.07847 + m.x4)**2 + m.x7
    <= 0)
m.e560 = Constraint(expr= -(-0.26163 + m.x1)**2 - (-0.82493 + m.x4)**2 + m.x7
    <= 0)
m.e561 = Constraint(expr= -(-0.85697 + m.x1)**2 - (-0.81967 + m.x4)**2 + m.x7
    <= 0)
m.e562 = Constraint(expr= -(-0.31643 + m.x1)**2 - (-0.54773 + m.x4)**2 + m.x7
    <= 0)
m.e563 = Constraint(expr= -(-0.45817 + m.x1)**2 - (-0.71287 + m.x4)**2 + m.x7
    <= 0)
m.e564 = Constraint(expr= -(-0.37923 + m.x1)**2 - (-0.55853 + m.x4)**2 + m.x7
    <= 0)
m.e565 = Constraint(expr= -(-0.81137 + m.x1)**2 - (-0.67807 + m.x4)**2 + m.x7
    <= 0)
m.e566 = Constraint(expr= -(-0.13003 + m.x1)**2 - (-0.33733 + m.x4)**2 + m.x7
    <= 0)
m.e567 = Constraint(expr= -(-0.83657 + m.x1)**2 - (-0.83527 + m.x4)**2 + m.x7
    <= 0)
m.e568 = Constraint(expr= -(-0.04883 + m.x1)**2 - (-0.16413 + m.x4)**2 + m.x7
    <= 0)
m.e569 = Constraint(expr= -(-0.65377 + m.x1)**2 - (-0.50447 + m.x4)**2 + m.x7
    <= 0)
m.e570 = Constraint(expr= -(-0.41563 + m.x1)**2 - (-0.11893 + m.x4)**2 + m.x7
    <= 0)
m.e571 = Constraint(expr= -(-0.58297 + m.x1)**2 - (-0.20567 + m.x4)**2 + m.x7
    <= 0)
m.e572 = Constraint(expr= -(-0.31043 + m.x1)**2 - (-0.08173 + m.x4)**2 + m.x7
    <= 0)
m.e573 = Constraint(expr= -(-0.14417 + m.x1)**2 - (-0.65887 + m.x4)**2 + m.x7
    <= 0)
m.e574 = Constraint(expr= -(-0.61323 + m.x1)**2 - (-0.73253 + m.x4)**2 + m.x7
    <= 0)
m.e575 = Constraint(expr= -(-0.05737 + m.x1)**2 - (-0.78407 + m.x4)**2 + m.x7
    <= 0)
m.e576 = Constraint(expr= -(-0.00403 + m.x1)**2 - (-0.55133 + m.x4)**2 + m.x7
    <= 0)
m.e577 = Constraint(expr= -(-0.24257 + m.x1)**2 - (-0.70127 + m.x4)**2 + m.x7
    <= 0)
m.e578 = Constraint(expr= -(-0.96283 + m.x1)**2 - (-0.81813 + m.x4)**2 + m.x7
    <= 0)
m.e579 = Constraint(expr= -(-0.81977 + m.x1)**2 - (-0.73047 + m.x4)**2 + m.x7
    <= 0)
m.e580 = Constraint(expr= -(-0.76963 + m.x1)**2 - (-0.61293 + m.x4)**2 + m.x7
    <= 0)
m.e581 = Constraint(expr= -(-0.10897 + m.x1)**2 - (-0.39167 + m.x4)**2 + m.x7
    <= 0)
m.e582 = Constraint(expr= -(-0.50443 + m.x1)**2 - (-0.81573 + m.x4)**2 + m.x7
    <= 0)
m.e583 = Constraint(expr= -(-0.63017 + m.x1)**2 - (-0.40487 + m.x4)**2 + m.x7
    <= 0)
m.e584 = Constraint(expr= -(-0.04723 + m.x1)**2 - (-0.10653 + m.x4)**2 + m.x7
    <= 0)
m.e585 = Constraint(expr= -(-0.10337 + m.x1)**2 - (-0.69007 + m.x4)**2 + m.x7
    <= 0)
m.e586 = Constraint(expr= -(-0.07803 + m.x1)**2 - (-0.96533 + m.x4)**2 + m.x7
    <= 0)
m.e587 = Constraint(expr= -(-0.44857 + m.x1)**2 - (-0.36727 + m.x4)**2 + m.x7
    <= 0)
m.e588 = Constraint(expr= -(-0.07683 + m.x1)**2 - (-0.67213 + m.x4)**2 + m.x7
    <= 0)
m.e589 = Constraint(expr= -(-0.78577 + m.x1)**2 - (-0.75647 + m.x4)**2 + m.x7
    <= 0)
m.e590 = Constraint(expr= -(-0.32363 + m.x1)**2 - (-0.30693 + m.x4)**2 + m.x7
    <= 0)
m.e591 = Constraint(expr= -(-0.43497 + m.x1)**2 - (-0.37767 + m.x4)**2 + m.x7
    <= 0)
m.e592 = Constraint(expr= -(-0.89843 + m.x1)**2 - (-0.74973 + m.x4)**2 + m.x7
    <= 0)
m.e593 = Constraint(expr= -(-0.91617 + m.x1)**2 - (-0.95087 + m.x4)**2 + m.x7
    <= 0)
m.e594 = Constraint(expr= -(-0.68123 + m.x1)**2 - (-0.68053 + m.x4)**2 + m.x7
    <= 0)
m.e595 = Constraint(expr= -(-0.94937 + m.x1)**2 - (-0.39607 + m.x4)**2 + m.x7
    <= 0)
m.e596 = Constraint(expr= -(-0.35203 + m.x1)**2 - (-0.57933 + m.x4)**2 + m.x7
    <= 0)
m.e597 = Constraint(expr= -(-0.45457 + m.x1)**2 - (-0.83327 + m.x4)**2 + m.x7
    <= 0)
m.e598 = Constraint(expr= -(-0.39083 + m.x1)**2 - (-0.72613 + m.x4)**2 + m.x7
    <= 0)
m.e599 = Constraint(expr= -(-0.55177 + m.x1)**2 - (-0.58247 + m.x4)**2 + m.x7
    <= 0)
m.e600 = Constraint(expr= -(-0.07763 + m.x1)**2 - (-0.20093 + m.x4)**2 + m.x7
    <= 0)
m.e601 = Constraint(expr= -(-0.56097 + m.x1)**2 - (-0.16367 + m.x4)**2 + m.x7
    <= 0)
m.e602 = Constraint(expr= -(-0.49243 + m.x1)**2 - (-0.88373 + m.x4)**2 + m.x7
    <= 0)
m.e603 = Constraint(expr= -(-0.00217 + m.x1)**2 - (-0.29687 + m.x4)**2 + m.x7
    <= 0)
m.e604 = Constraint(expr= -(-0.51523 + m.x1)**2 - (-0.45453 + m.x4)**2 + m.x7
    <= 0)
m.e605 = Constraint(expr= -(-0.59537 + m.x1)**2 - (-0.90207 + m.x4)**2 + m.x7
    <= 0)
m.e606 = Constraint(expr= -(-0.82603 + m.x1)**2 - (-0.39333 + m.x4)**2 + m.x7
    <= 0)
m.e607 = Constraint(expr= -(-0.26057 + m.x1)**2 - (-0.09927 + m.x4)**2 + m.x7
    <= 0)
m.e608 = Constraint(expr= -(-0.90483 + m.x1)**2 - (-0.98013 + m.x4)**2 + m.x7
    <= 0)
m.e609 = Constraint(expr= -(-0.11777 + m.x1)**2 - (-0.20847 + m.x4)**2 + m.x7
    <= 0)
m.e610 = Constraint(expr= -(-0.03163 + m.x1)**2 - (-0.29493 + m.x4)**2 + m.x7
    <= 0)
m.e611 = Constraint(expr= -(-0.48697 + m.x1)**2 - (-0.74967 + m.x4)**2 + m.x7
    <= 0)
m.e612 = Constraint(expr= -(-0.28643 + m.x1)**2 - (-0.21773 + m.x4)**2 + m.x7
    <= 0)
m.e613 = Constraint(expr= -(-0.88817 + m.x1)**2 - (-0.44287 + m.x4)**2 + m.x7
    <= 0)
m.e614 = Constraint(expr= -(-0.54923 + m.x1)**2 - (-0.42853 + m.x4)**2 + m.x7
    <= 0)
m.e615 = Constraint(expr= -(-0.04137 + m.x1)**2 - (-0.20807 + m.x4)**2 + m.x7
    <= 0)
m.e616 = Constraint(expr= -(-0.50003 + m.x1)**2 - (-0.40733 + m.x4)**2 + m.x7
    <= 0)
m.e617 = Constraint(expr= -(-0.86657 + m.x1)**2 - (-0.16527 + m.x4)**2 + m.x7
    <= 0)
m.e618 = Constraint(expr= -(-0.61883 + m.x1)**2 - (-0.43413 + m.x4)**2 + m.x7
    <= 0)
m.e619 = Constraint(expr= -(-0.48377 + m.x1)**2 - (-0.63447 + m.x4)**2 + m.x7
    <= 0)
m.e620 = Constraint(expr= -(-0.18563 + m.x1)**2 - (-0.58893 + m.x4)**2 + m.x7
    <= 0)
m.e621 = Constraint(expr= -(-0.21297 + m.x1)**2 - (-0.13567 + m.x4)**2 + m.x7
    <= 0)
m.e622 = Constraint(expr= -(-0.28043 + m.x1)**2 - (-0.75173 + m.x4)**2 + m.x7
    <= 0)
m.e623 = Constraint(expr= -(-0.57417 + m.x1)**2 - (-0.38887 + m.x4)**2 + m.x7
    <= 0)
m.e624 = Constraint(expr= -(-0.78323 + m.x1)**2 - (-0.60253 + m.x4)**2 + m.x7
    <= 0)
m.e625 = Constraint(expr= -(-0.28737 + m.x1)**2 - (-0.31407 + m.x4)**2 + m.x7
    <= 0)
m.e626 = Constraint(expr= -(-0.37403 + m.x1)**2 - (-0.62133 + m.x4)**2 + m.x7
    <= 0)
m.e627 = Constraint(expr= -(-0.27257 + m.x1)**2 - (-0.03127 + m.x4)**2 + m.x7
    <= 0)
m.e628 = Constraint(expr= -(-0.53283 + m.x1)**2 - (-0.08813 + m.x4)**2 + m.x7
    <= 0)
m.e629 = Constraint(expr= -(-0.64977 + m.x1)**2 - (-0.86047 + m.x4)**2 + m.x7
    <= 0)
m.e630 = Constraint(expr= -(-0.53963 + m.x1)**2 - (-0.08293 + m.x4)**2 + m.x7
    <= 0)
m.e631 = Constraint(expr= -(-0.73897 + m.x1)**2 - (-0.32167 + m.x4)**2 + m.x7
    <= 0)
m.e632 = Constraint(expr= -(-0.47443 + m.x1)**2 - (-0.48573 + m.x4)**2 + m.x7
    <= 0)
m.e633 = Constraint(expr= -(-0.06017 + m.x1)**2 - (-0.13487 + m.x4)**2 + m.x7
    <= 0)
m.e634 = Constraint(expr= -(-0.21723 + m.x1)**2 - (-0.97653 + m.x4)**2 + m.x7
    <= 0)
m.e635 = Constraint(expr= -(-0.33337 + m.x1)**2 - (-0.22007 + m.x4)**2 + m.x7
    <= 0)
m.e636 = Constraint(expr= -(-0.44803 + m.x1)**2 - (-0.03533 + m.x4)**2 + m.x7
    <= 0)
m.e637 = Constraint(expr= -(-0.47857 + m.x1)**2 - (-0.69727 + m.x4)**2 + m.x7
    <= 0)
m.e638 = Constraint(expr= -(-0.64683 + m.x1)**2 - (-0.94213 + m.x4)**2 + m.x7
    <= 0)
m.e639 = Constraint(expr= -(-0.61577 + m.x1)**2 - (-0.88647 + m.x4)**2 + m.x7
    <= 0)
m.e640 = Constraint(expr= -(-0.09363 + m.x1)**2 - (-0.77693 + m.x4)**2 + m.x7
    <= 0)
m.e641 = Constraint(expr= -(-0.06497 + m.x1)**2 - (-0.30767 + m.x4)**2 + m.x7
    <= 0)
m.e642 = Constraint(expr= -(-0.86843 + m.x1)**2 - (-0.41973 + m.x4)**2 + m.x7
    <= 0)
m.e643 = Constraint(expr= -(-0.34617 + m.x1)**2 - (-0.68087 + m.x4)**2 + m.x7
    <= 0)
m.e644 = Constraint(expr= -(-0.85123 + m.x1)**2 - (-0.55053 + m.x4)**2 + m.x7
    <= 0)
m.e645 = Constraint(expr= -(-0.17937 + m.x1)**2 - (-0.92607 + m.x4)**2 + m.x7
    <= 0)
m.e646 = Constraint(expr= -(-0.72203 + m.x1)**2 - (-0.64933 + m.x4)**2 + m.x7
    <= 0)
m.e647 = Constraint(expr= -(-0.48457 + m.x1)**2 - (-0.16327 + m.x4)**2 + m.x7
    <= 0)
m.e648 = Constraint(expr= -(-0.96083 + m.x1)**2 - (-0.99613 + m.x4)**2 + m.x7
    <= 0)
m.e649 = Constraint(expr= -(-0.38177 + m.x1)**2 - (-0.71247 + m.x4)**2 + m.x7
    <= 0)
m.e650 = Constraint(expr= -(-0.84763 + m.x1)**2 - (-0.67093 + m.x4)**2 + m.x7
    <= 0)
m.e651 = Constraint(expr= -(-0.19097 + m.x1)**2 - (-0.09367 + m.x4)**2 + m.x7
    <= 0)
m.e652 = Constraint(expr= -(-0.46243 + m.x1)**2 - (-0.55373 + m.x4)**2 + m.x7
    <= 0)
m.e653 = Constraint(expr= -(-0.43217 + m.x1)**2 - (-0.02687 + m.x4)**2 + m.x7
    <= 0)
m.e654 = Constraint(expr= -(-0.68523 + m.x1)**2 - (-0.32453 + m.x4)**2 + m.x7
    <= 0)
m.e655 = Constraint(expr= -(-0.82537 + m.x1)**2 - (-0.43207 + m.x4)**2 + m.x7
    <= 0)
m.e656 = Constraint(expr= -(-0.19603 + m.x1)**2 - (-0.46333 + m.x4)**2 + m.x7
    <= 0)
m.e657 = Constraint(expr= -(-0.29057 + m.x1)**2 - (-0.42927 + m.x4)**2 + m.x7
    <= 0)
m.e658 = Constraint(expr= -(-0.47483 + m.x1)**2 - (-0.25013 + m.x4)**2 + m.x7
    <= 0)
m.e659 = Constraint(expr= -(-0.94777 + m.x1)**2 - (-0.33847 + m.x4)**2 + m.x7
    <= 0)
m.e660 = Constraint(expr= -(-0.80163 + m.x1)**2 - (-0.76493 + m.x4)**2 + m.x7
    <= 0)
m.e661 = Constraint(expr= -(-0.11697 + m.x1)**2 - (-0.67967 + m.x4)**2 + m.x7
    <= 0)
m.e662 = Constraint(expr= -(-0.25643 + m.x1)**2 - (-0.88773 + m.x4)**2 + m.x7
    <= 0)
m.e663 = Constraint(expr= -(-0.31817 + m.x1)**2 - (-0.17287 + m.x4)**2 + m.x7
    <= 0)
m.e664 = Constraint(expr= -(-0.71923 + m.x1)**2 - (-0.29853 + m.x4)**2 + m.x7
    <= 0)
m.e665 = Constraint(expr= -(-0.27137 + m.x1)**2 - (-0.73807 + m.x4)**2 + m.x7
    <= 0)
m.e666 = Constraint(expr= -(-0.87003 + m.x1)**2 - (-0.47733 + m.x4)**2 + m.x7
    <= 0)
m.e667 = Constraint(expr= -(-0.89657 + m.x1)**2 - (-0.49527 + m.x4)**2 + m.x7
    <= 0)
m.e668 = Constraint(expr= -(-0.18883 + m.x1)**2 - (-0.70413 + m.x4)**2 + m.x7
    <= 0)
m.e669 = Constraint(expr= -(-0.31377 + m.x1)**2 - (-0.76447 + m.x4)**2 + m.x7
    <= 0)
m.e670 = Constraint(expr= -(-0.95563 + m.x1)**2 - (-0.05893 + m.x4)**2 + m.x7
    <= 0)
m.e671 = Constraint(expr= -(-0.84297 + m.x1)**2 - (-0.06567 + m.x4)**2 + m.x7
    <= 0)
m.e672 = Constraint(expr= -(-0.25043 + m.x1)**2 - (-0.42173 + m.x4)**2 + m.x7
    <= 0)
m.e673 = Constraint(expr= -(-0.00417 + m.x1)**2 - (-0.11887 + m.x4)**2 + m.x7
    <= 0)
m.e674 = Constraint(expr= -(-0.95323 + m.x1)**2 - (-0.47253 + m.x4)**2 + m.x7
    <= 0)
m.e675 = Constraint(expr= -(-0.51737 + m.x1)**2 - (-0.84407 + m.x4)**2 + m.x7
    <= 0)
m.e676 = Constraint(expr= -(-0.74403 + m.x1)**2 - (-0.69133 + m.x4)**2 + m.x7
    <= 0)
m.e677 = Constraint(expr= -(-0.30257 + m.x1)**2 - (-0.36127 + m.x4)**2 + m.x7
    <= 0)
m.e678 = Constraint(expr= -(-0.10283 + m.x1)**2 - (-0.35813 + m.x4)**2 + m.x7
    <= 0)
m.e679 = Constraint(expr= -(-0.47977 + m.x1)**2 - (-0.99047 + m.x4)**2 + m.x7
    <= 0)
m.e680 = Constraint(expr= -(-0.30963 + m.x1)**2 - (-0.55293 + m.x4)**2 + m.x7
    <= 0)
m.e681 = Constraint(expr= -(-0.36897 + m.x1)**2 - (-0.25167 + m.x4)**2 + m.x7
    <= 0)
m.e682 = Constraint(expr= -(-0.44443 + m.x1)**2 - (-0.15573 + m.x4)**2 + m.x7
    <= 0)
m.e683 = Constraint(expr= -(-0.49017 + m.x1)**2 - (-0.86487 + m.x4)**2 + m.x7
    <= 0)
m.e684 = Constraint(expr= -(-0.38723 + m.x1)**2 - (-0.84653 + m.x4)**2 + m.x7
    <= 0)
m.e685 = Constraint(expr= -(-0.56337 + m.x1)**2 - (-0.75007 + m.x4)**2 + m.x7
    <= 0)
m.e686 = Constraint(expr= -(-0.81803 + m.x1)**2 - (-0.10533 + m.x4)**2 + m.x7
    <= 0)
m.e687 = Constraint(expr= -(-0.50857 + m.x1)**2 - (-0.02727 + m.x4)**2 + m.x7
    <= 0)
m.e688 = Constraint(expr= -(-0.21683 + m.x1)**2 - (-0.21213 + m.x4)**2 + m.x7
    <= 0)
m.e689 = Constraint(expr= -(-0.44577 + m.x1)**2 - (-0.01647 + m.x4)**2 + m.x7
    <= 0)
m.e690 = Constraint(expr= -(-0.86363 + m.x1)**2 - (-0.24693 + m.x4)**2 + m.x7
    <= 0)
m.e691 = Constraint(expr= -(-0.69497 + m.x1)**2 - (-0.23767 + m.x4)**2 + m.x7
    <= 0)
m.e692 = Constraint(expr= -(-0.83843 + m.x1)**2 - (-0.08973 + m.x4)**2 + m.x7
    <= 0)
m.e693 = Constraint(expr= -(-0.77617 + m.x1)**2 - (-0.41087 + m.x4)**2 + m.x7
    <= 0)
m.e694 = Constraint(expr= -(-0.02123 + m.x1)**2 - (-0.42053 + m.x4)**2 + m.x7
    <= 0)
m.e695 = Constraint(expr= -(-0.40937 + m.x1)**2 - (-0.45607 + m.x4)**2 + m.x7
    <= 0)
m.e696 = Constraint(expr= -(-0.09203 + m.x1)**2 - (-0.71933 + m.x4)**2 + m.x7
    <= 0)
m.e697 = Constraint(expr= -(-0.51457 + m.x1)**2 - (-0.49327 + m.x4)**2 + m.x7
    <= 0)
m.e698 = Constraint(expr= -(-0.53083 + m.x1)**2 - (-0.26613 + m.x4)**2 + m.x7
    <= 0)
m.e699 = Constraint(expr= -(-0.21177 + m.x1)**2 - (-0.84247 + m.x4)**2 + m.x7
    <= 0)
m.e700 = Constraint(expr= -(-0.61763 + m.x1)**2 - (-0.14093 + m.x4)**2 + m.x7
    <= 0)
m.e701 = Constraint(expr= -(-0.82097 + m.x1)**2 - (-0.02367 + m.x4)**2 + m.x7
    <= 0)
m.e702 = Constraint(expr= -(-0.43243 + m.x1)**2 - (-0.22373 + m.x4)**2 + m.x7
    <= 0)
m.e703 = Constraint(expr= -(-0.86217 + m.x1)**2 - (-0.75687 + m.x4)**2 + m.x7
    <= 0)
m.e704 = Constraint(expr= -(-0.85523 + m.x1)**2 - (-0.19453 + m.x4)**2 + m.x7
    <= 0)
m.e705 = Constraint(expr= -(-0.05537 + m.x1)**2 - (-0.96207 + m.x4)**2 + m.x7
    <= 0)
m.e706 = Constraint(expr= -(-0.56603 + m.x1)**2 - (-0.53333 + m.x4)**2 + m.x7
    <= 0)
m.e707 = Constraint(expr= -(-0.32057 + m.x1)**2 - (-0.75927 + m.x4)**2 + m.x7
    <= 0)
m.e708 = Constraint(expr= -(-0.04483 + m.x1)**2 - (-0.52013 + m.x4)**2 + m.x7
    <= 0)
m.e709 = Constraint(expr= -(-0.77777 + m.x1)**2 - (-0.46847 + m.x4)**2 + m.x7
    <= 0)
m.e710 = Constraint(expr= -(-0.57163 + m.x1)**2 - (-0.23493 + m.x4)**2 + m.x7
    <= 0)
m.e711 = Constraint(expr= -(-0.74697 + m.x1)**2 - (-0.60967 + m.x4)**2 + m.x7
    <= 0)
m.e712 = Constraint(expr= -(-0.22643 + m.x1)**2 - (-0.55773 + m.x4)**2 + m.x7
    <= 0)
m.e713 = Constraint(expr= -(-0.74817 + m.x1)**2 - (-0.90287 + m.x4)**2 + m.x7
    <= 0)
m.e714 = Constraint(expr= -(-0.88923 + m.x1)**2 - (-0.16853 + m.x4)**2 + m.x7
    <= 0)
m.e715 = Constraint(expr= -(-0.50137 + m.x1)**2 - (-0.26807 + m.x4)**2 + m.x7
    <= 0)
m.e716 = Constraint(expr= -(-0.24003 + m.x1)**2 - (-0.54733 + m.x4)**2 + m.x7
    <= 0)
m.e717 = Constraint(expr= -(-0.92657 + m.x1)**2 - (-0.82527 + m.x4)**2 + m.x7
    <= 0)
m.e718 = Constraint(expr= -(-0.75883 + m.x1)**2 - (-0.97413 + m.x4)**2 + m.x7
    <= 0)
m.e719 = Constraint(expr= -(-0.14377 + m.x1)**2 - (-0.89447 + m.x4)**2 + m.x7
    <= 0)
m.e720 = Constraint(expr= -(-0.72563 + m.x1)**2 - (-0.52893 + m.x4)**2 + m.x7
    <= 0)
m.e721 = Constraint(expr= -(-0.47297 + m.x1)**2 - (-0.99567 + m.x4)**2 + m.x7
    <= 0)
m.e722 = Constraint(expr= -(-0.22043 + m.x1)**2 - (-0.09173 + m.x4)**2 + m.x7
    <= 0)
m.e723 = Constraint(expr= -(-0.43417 + m.x1)**2 - (-0.84887 + m.x4)**2 + m.x7
    <= 0)
m.e724 = Constraint(expr= -(-0.12323 + m.x1)**2 - (-0.34253 + m.x4)**2 + m.x7
    <= 0)
m.e725 = Constraint(expr= -(-0.74737 + m.x1)**2 - (-0.37407 + m.x4)**2 + m.x7
    <= 0)
m.e726 = Constraint(expr= -(-0.11403 + m.x1)**2 - (-0.76133 + m.x4)**2 + m.x7
    <= 0)
m.e727 = Constraint(expr= -(-0.33257 + m.x1)**2 - (-0.69127 + m.x4)**2 + m.x7
    <= 0)
m.e728 = Constraint(expr= -(-0.67283 + m.x1)**2 - (-0.62813 + m.x4)**2 + m.x7
    <= 0)
m.e729 = Constraint(expr= -(-0.30977 + m.x1)**2 - (-0.12047 + m.x4)**2 + m.x7
    <= 0)
m.e730 = Constraint(expr= -(-0.07963 + m.x1)**2 - (-0.02293 + m.x4)**2 + m.x7
    <= 0)
m.e731 = Constraint(expr= -(-0.99897 + m.x1)**2 - (-0.18167 + m.x4)**2 + m.x7
    <= 0)
m.e732 = Constraint(expr= -(-0.41443 + m.x1)**2 - (-0.82573 + m.x4)**2 + m.x7
    <= 0)
m.e733 = Constraint(expr= -(-0.92017 + m.x1)**2 - (-0.59487 + m.x4)**2 + m.x7
    <= 0)
m.e734 = Constraint(expr= -(-0.55723 + m.x1)**2 - (-0.71653 + m.x4)**2 + m.x7
    <= 0)
m.e735 = Constraint(expr= -(-0.79337 + m.x1)**2 - (-0.28007 + m.x4)**2 + m.x7
    <= 0)
m.e736 = Constraint(expr= -(-0.18803 + m.x1)**2 - (-0.17533 + m.x4)**2 + m.x7
    <= 0)
m.e737 = Constraint(expr= -(-0.53857 + m.x1)**2 - (-0.35727 + m.x4)**2 + m.x7
    <= 0)
m.e738 = Constraint(expr= -(-0.78683 + m.x1)**2 - (-0.48213 + m.x4)**2 + m.x7
    <= 0)
m.e739 = Constraint(expr= -(-0.27577 + m.x1)**2 - (-0.14647 + m.x4)**2 + m.x7
    <= 0)
m.e740 = Constraint(expr= -(-0.63363 + m.x1)**2 - (-0.71693 + m.x4)**2 + m.x7
    <= 0)
m.e741 = Constraint(expr= -(-0.32497 + m.x1)**2 - (-0.16767 + m.x4)**2 + m.x7
    <= 0)
m.e742 = Constraint(expr= -(-0.80843 + m.x1)**2 - (-0.75973 + m.x4)**2 + m.x7
    <= 0)
m.e743 = Constraint(expr= -(-0.20617 + m.x1)**2 - (-0.14087 + m.x4)**2 + m.x7
    <= 0)
m.e744 = Constraint(expr= -(-0.19123 + m.x1)**2 - (-0.29053 + m.x4)**2 + m.x7
    <= 0)
m.e745 = Constraint(expr= -(-0.63937 + m.x1)**2 - (-0.98607 + m.x4)**2 + m.x7
    <= 0)
m.e746 = Constraint(expr= -(-0.46203 + m.x1)**2 - (-0.78933 + m.x4)**2 + m.x7
    <= 0)
m.e747 = Constraint(expr= -(-0.54457 + m.x1)**2 - (-0.82327 + m.x4)**2 + m.x7
    <= 0)
m.e748 = Constraint(expr= -(-0.10083 + m.x1)**2 - (-0.53613 + m.x4)**2 + m.x7
    <= 0)
m.e749 = Constraint(expr= -(-0.04177 + m.x1)**2 - (-0.97247 + m.x4)**2 + m.x7
    <= 0)
m.e750 = Constraint(expr= -(-0.38763 + m.x1)**2 - (-0.61093 + m.x4)**2 + m.x7
    <= 0)
m.e751 = Constraint(expr= -(-0.45097 + m.x1)**2 - (-0.95367 + m.x4)**2 + m.x7
    <= 0)
m.e752 = Constraint(expr= -(-0.40243 + m.x1)**2 - (-0.89373 + m.x4)**2 + m.x7
    <= 0)
m.e753 = Constraint(expr= -(-0.29217 + m.x1)**2 - (-0.48687 + m.x4)**2 + m.x7
    <= 0)
m.e754 = Constraint(expr= -(-0.02523 + m.x1)**2 - (-0.06453 + m.x4)**2 + m.x7
    <= 0)
m.e755 = Constraint(expr= -(-0.28537 + m.x1)**2 - (-0.49207 + m.x4)**2 + m.x7
    <= 0)
m.e756 = Constraint(expr= -(-0.93603 + m.x1)**2 - (-0.60333 + m.x4)**2 + m.x7
    <= 0)
m.e757 = Constraint(expr= -(-0.35057 + m.x1)**2 - (-0.08927 + m.x4)**2 + m.x7
    <= 0)
m.e758 = Constraint(expr= -(-0.61483 + m.x1)**2 - (-0.79013 + m.x4)**2 + m.x7
    <= 0)
m.e759 = Constraint(expr= -(-0.60777 + m.x1)**2 - (-0.59847 + m.x4)**2 + m.x7
    <= 0)
m.e760 = Constraint(expr= -(-0.34163 + m.x1)**2 - (-0.70493 + m.x4)**2 + m.x7
    <= 0)
m.e761 = Constraint(expr= -(-0.37697 + m.x1)**2 - (-0.53967 + m.x4)**2 + m.x7
    <= 0)
m.e762 = Constraint(expr= -(-0.19643 + m.x1)**2 - (-0.22773 + m.x4)**2 + m.x7
    <= 0)
m.e763 = Constraint(expr= -(-0.17817 + m.x1)**2 - (-0.63287 + m.x4)**2 + m.x7
    <= 0)
m.e764 = Constraint(expr= -(-0.05923 + m.x1)**2 - (-0.03853 + m.x4)**2 + m.x7
    <= 0)
m.e765 = Constraint(expr= -(-0.73137 + m.x1)**2 - (-0.79807 + m.x4)**2 + m.x7
    <= 0)
m.e766 = Constraint(expr= -(-0.61003 + m.x1)**2 - (-0.61733 + m.x4)**2 + m.x7
    <= 0)
m.e767 = Constraint(expr= -(-0.95657 + m.x1)**2 - (-0.15527 + m.x4)**2 + m.x7
    <= 0)
m.e768 = Constraint(expr= -(-0.32883 + m.x1)**2 - (-0.24413 + m.x4)**2 + m.x7
    <= 0)
m.e769 = Constraint(expr= -(-0.97377 + m.x1)**2 - (-0.02447 + m.x4)**2 + m.x7
    <= 0)
m.e770 = Constraint(expr= -(-0.49563 + m.x1)**2 - (-0.99893 + m.x4)**2 + m.x7
    <= 0)
m.e771 = Constraint(expr= -(-0.10297 + m.x1)**2 - (-0.92567 + m.x4)**2 + m.x7
    <= 0)
m.e772 = Constraint(expr= -(-0.19043 + m.x1)**2 - (-0.76173 + m.x4)**2 + m.x7
    <= 0)
m.e773 = Constraint(expr= -(-0.86417 + m.x1)**2 - (-0.57887 + m.x4)**2 + m.x7
    <= 0)
m.e774 = Constraint(expr= -(-0.29323 + m.x1)**2 - (-0.21253 + m.x4)**2 + m.x7
    <= 0)
m.e775 = Constraint(expr= -(-0.97737 + m.x1)**2 - (-0.90407 + m.x4)**2 + m.x7
    <= 0)
m.e776 = Constraint(expr= -(-0.48403 + m.x1)**2 - (-0.83133 + m.x4)**2 + m.x7
    <= 0)
m.e777 = Constraint(expr= -(-0.36257 + m.x1)**2 - (-0.02127 + m.x4)**2 + m.x7
    <= 0)
m.e778 = Constraint(expr= -(-0.24283 + m.x1)**2 - (-0.89813 + m.x4)**2 + m.x7
    <= 0)
m.e779 = Constraint(expr= -(-0.13977 + m.x1)**2 - (-0.25047 + m.x4)**2 + m.x7
    <= 0)
m.e780 = Constraint(expr= -(-0.84963 + m.x1)**2 - (-0.49293 + m.x4)**2 + m.x7
    <= 0)
m.e781 = Constraint(expr= -(-0.62897 + m.x1)**2 - (-0.11167 + m.x4)**2 + m.x7
    <= 0)
m.e782 = Constraint(expr= -(-0.38443 + m.x1)**2 - (-0.49573 + m.x4)**2 + m.x7
    <= 0)
m.e783 = Constraint(expr= -(-0.35017 + m.x1)**2 - (-0.32487 + m.x4)**2 + m.x7
    <= 0)
m.e784 = Constraint(expr= -(-0.72723 + m.x1)**2 - (-0.58653 + m.x4)**2 + m.x7
    <= 0)
m.e785 = Constraint(expr= -(-0.02337 + m.x1)**2 - (-0.81007 + m.x4)**2 + m.x7
    <= 0)
m.e786 = Constraint(expr= -(-0.55803 + m.x1)**2 - (-0.24533 + m.x4)**2 + m.x7
    <= 0)
m.e787 = Constraint(expr= -(-0.56857 + m.x1)**2 - (-0.68727 + m.x4)**2 + m.x7
    <= 0)
m.e788 = Constraint(expr= -(-0.35683 + m.x1)**2 - (-0.75213 + m.x4)**2 + m.x7
    <= 0)
m.e789 = Constraint(expr= -(-0.10577 + m.x1)**2 - (-0.27647 + m.x4)**2 + m.x7
    <= 0)
m.e790 = Constraint(expr= -(-0.40363 + m.x1)**2 - (-0.18693 + m.x4)**2 + m.x7
    <= 0)
m.e791 = Constraint(expr= -(-0.95497 + m.x1)**2 - (-0.09767 + m.x4)**2 + m.x7
    <= 0)
m.e792 = Constraint(expr= -(-0.77843 + m.x1)**2 - (-0.42973 + m.x4)**2 + m.x7
    <= 0)
m.e793 = Constraint(expr= -(-0.63617 + m.x1)**2 - (-0.87087 + m.x4)**2 + m.x7
    <= 0)
m.e794 = Constraint(expr= -(-0.36123 + m.x1)**2 - (-0.16053 + m.x4)**2 + m.x7
    <= 0)
m.e795 = Constraint(expr= -(-0.86937 + m.x1)**2 - (-0.51607 + m.x4)**2 + m.x7
    <= 0)
m.e796 = Constraint(expr= -(-0.83203 + m.x1)**2 - (-0.85933 + m.x4)**2 + m.x7
    <= 0)
m.e797 = Constraint(expr= -(-0.57457 + m.x1)**2 - (-0.15327 + m.x4)**2 + m.x7
    <= 0)
m.e798 = Constraint(expr= -(-0.67083 + m.x1)**2 - (-0.80613 + m.x4)**2 + m.x7
    <= 0)
m.e799 = Constraint(expr= -(-0.87177 + m.x1)**2 - (-0.10247 + m.x4)**2 + m.x7
    <= 0)
m.e800 = Constraint(expr= -(-0.15763 + m.x1)**2 - (-0.08093 + m.x4)**2 + m.x7
    <= 0)
m.e801 = Constraint(expr= -(-0.08097 + m.x1)**2 - (-0.88367 + m.x4)**2 + m.x7
    <= 0)
m.e802 = Constraint(expr= -(-0.37243 + m.x1)**2 - (-0.56373 + m.x4)**2 + m.x7
    <= 0)
m.e803 = Constraint(expr= -(-0.72217 + m.x1)**2 - (-0.21687 + m.x4)**2 + m.x7
    <= 0)
m.e804 = Constraint(expr= -(-0.19523 + m.x1)**2 - (-0.93453 + m.x4)**2 + m.x7
    <= 0)
m.e805 = Constraint(expr= -(-0.51537 + m.x1)**2 - (-0.02207 + m.x4)**2 + m.x7
    <= 0)
m.e806 = Constraint(expr= -(-0.30603 + m.x1)**2 - (-0.67333 + m.x4)**2 + m.x7
    <= 0)
m.e807 = Constraint(expr= -(-0.38057 + m.x1)**2 - (-0.41927 + m.x4)**2 + m.x7
    <= 0)
m.e808 = Constraint(expr= -(-0.18483 + m.x1)**2 - (-0.06013 + m.x4)**2 + m.x7
    <= 0)
m.e809 = Constraint(expr= -(-0.43777 + m.x1)**2 - (-0.72847 + m.x4)**2 + m.x7
    <= 0)
m.e810 = Constraint(expr= -(-0.11163 + m.x1)**2 - (-0.17493 + m.x4)**2 + m.x7
    <= 0)
m.e811 = Constraint(expr= -(-0.00697 + m.x1)**2 - (-0.46967 + m.x4)**2 + m.x7
    <= 0)
m.e812 = Constraint(expr= -(-0.16643 + m.x1)**2 - (-0.89773 + m.x4)**2 + m.x7
    <= 0)
m.e813 = Constraint(expr= -(-0.60817 + m.x1)**2 - (-0.36287 + m.x4)**2 + m.x7
    <= 0)
m.e814 = Constraint(expr= -(-0.22923 + m.x1)**2 - (-0.90853 + m.x4)**2 + m.x7
    <= 0)
m.e815 = Constraint(expr= -(-0.96137 + m.x1)**2 - (-0.32807 + m.x4)**2 + m.x7
    <= 0)
m.e816 = Constraint(expr= -(-0.98003 + m.x1)**2 - (-0.68733 + m.x4)**2 + m.x7
    <= 0)
m.e817 = Constraint(expr= -(-0.98657 + m.x1)**2 - (-0.48527 + m.x4)**2 + m.x7
    <= 0)
m.e818 = Constraint(expr= -(-0.89883 + m.x1)**2 - (-0.51413 + m.x4)**2 + m.x7
    <= 0)
m.e819 = Constraint(expr= -(-0.80377 + m.x1)**2 - (-0.15447 + m.x4)**2 + m.x7
    <= 0)
m.e820 = Constraint(expr= -(-0.26563 + m.x1)**2 - (-0.46893 + m.x4)**2 + m.x7
    <= 0)
m.e821 = Constraint(expr= -(-0.73297 + m.x1)**2 - (-0.85567 + m.x4)**2 + m.x7
    <= 0)
m.e822 = Constraint(expr= -(-0.16043 + m.x1)**2 - (-0.43173 + m.x4)**2 + m.x7
    <= 0)
m.e823 = Constraint(expr= -(-0.29417 + m.x1)**2 - (-0.30887 + m.x4)**2 + m.x7
    <= 0)
m.e824 = Constraint(expr= -(-0.46323 + m.x1)**2 - (-0.08253 + m.x4)**2 + m.x7
    <= 0)
m.e825 = Constraint(expr= -(-0.20737 + m.x1)**2 - (-0.43407 + m.x4)**2 + m.x7
    <= 0)
m.e826 = Constraint(expr= -(-0.85403 + m.x1)**2 - (-0.90133 + m.x4)**2 + m.x7
    <= 0)
m.e827 = Constraint(expr= -(-0.39257 + m.x1)**2 - (-0.35127 + m.x4)**2 + m.x7
    <= 0)
m.e828 = Constraint(expr= -(-0.81283 + m.x1)**2 - (-0.16813 + m.x4)**2 + m.x7
    <= 0)
m.e829 = Constraint(expr= -(-0.96977 + m.x1)**2 - (-0.38047 + m.x4)**2 + m.x7
    <= 0)
m.e830 = Constraint(expr= -(-0.61963 + m.x1)**2 - (-0.96293 + m.x4)**2 + m.x7
    <= 0)
m.e831 = Constraint(expr= -(-0.25897 + m.x1)**2 - (-0.04167 + m.x4)**2 + m.x7
    <= 0)
m.e832 = Constraint(expr= -(-0.35443 + m.x1)**2 - (-0.16573 + m.x4)**2 + m.x7
    <= 0)
m.e833 = Constraint(expr= -(-0.78017 + m.x1)**2 - (-0.05487 + m.x4)**2 + m.x7
    <= 0)
m.e834 = Constraint(expr= -(-0.89723 + m.x1)**2 - (-0.45653 + m.x4)**2 + m.x7
    <= 0)
m.e835 = Constraint(expr= -(-0.25337 + m.x1)**2 - (-0.34007 + m.x4)**2 + m.x7
    <= 0)
m.e836 = Constraint(expr= -(-0.92803 + m.x1)**2 - (-0.31533 + m.x4)**2 + m.x7
    <= 0)
m.e837 = Constraint(expr= -(-0.59857 + m.x1)**2 - (-0.01727 + m.x4)**2 + m.x7
    <= 0)
m.e838 = Constraint(expr= -(-0.92683 + m.x1)**2 - (-0.02213 + m.x4)**2 + m.x7
    <= 0)
m.e839 = Constraint(expr= -(-0.93577 + m.x1)**2 - (-0.40647 + m.x4)**2 + m.x7
    <= 0)
m.e840 = Constraint(expr= -(-0.17363 + m.x1)**2 - (-0.65693 + m.x4)**2 + m.x7
    <= 0)
m.e841 = Constraint(expr= -(-0.58497 + m.x1)**2 - (-0.02767 + m.x4)**2 + m.x7
    <= 0)
m.e842 = Constraint(expr= -(-0.74843 + m.x1)**2 - (-0.09973 + m.x4)**2 + m.x7
    <= 0)
m.e843 = Constraint(expr= -(-0.06617 + m.x1)**2 - (-0.60087 + m.x4)**2 + m.x7
    <= 0)
m.e844 = Constraint(expr= -(-0.53123 + m.x1)**2 - (-0.03053 + m.x4)**2 + m.x7
    <= 0)
m.e845 = Constraint(expr= -(-0.09937 + m.x1)**2 - (-0.04607 + m.x4)**2 + m.x7
    <= 0)
m.e846 = Constraint(expr= -(-0.20203 + m.x1)**2 - (-0.92933 + m.x4)**2 + m.x7
    <= 0)
m.e847 = Constraint(expr= -(-0.60457 + m.x1)**2 - (-0.48327 + m.x4)**2 + m.x7
    <= 0)
m.e848 = Constraint(expr= -(-0.24083 + m.x1)**2 - (-0.07613 + m.x4)**2 + m.x7
    <= 0)
m.e849 = Constraint(expr= -(-0.70177 + m.x1)**2 - (-0.23247 + m.x4)**2 + m.x7
    <= 0)
m.e850 = Constraint(expr= -(-0.92763 + m.x1)**2 - (-0.55093 + m.x4)**2 + m.x7
    <= 0)
m.e851 = Constraint(expr= -(-0.71097 + m.x1)**2 - (-0.81367 + m.x4)**2 + m.x7
    <= 0)
m.e852 = Constraint(expr= -(-0.34243 + m.x1)**2 - (-0.23373 + m.x4)**2 + m.x7
    <= 0)
m.e853 = Constraint(expr= -(-0.15217 + m.x1)**2 - (-0.94687 + m.x4)**2 + m.x7
    <= 0)
m.e854 = Constraint(expr= -(-0.36523 + m.x1)**2 - (-0.80453 + m.x4)**2 + m.x7
    <= 0)
m.e855 = Constraint(expr= -(-0.74537 + m.x1)**2 - (-0.55207 + m.x4)**2 + m.x7
    <= 0)
m.e856 = Constraint(expr= -(-0.67603 + m.x1)**2 - (-0.74333 + m.x4)**2 + m.x7
    <= 0)
m.e857 = Constraint(expr= -(-0.41057 + m.x1)**2 - (-0.74927 + m.x4)**2 + m.x7
    <= 0)
m.e858 = Constraint(expr= -(-0.75483 + m.x1)**2 - (-0.33013 + m.x4)**2 + m.x7
    <= 0)
m.e859 = Constraint(expr= -(-0.26777 + m.x1)**2 - (-0.85847 + m.x4)**2 + m.x7
    <= 0)
m.e860 = Constraint(expr= -(-0.88163 + m.x1)**2 - (-0.64493 + m.x4)**2 + m.x7
    <= 0)
m.e861 = Constraint(expr= -(-0.63697 + m.x1)**2 - (-0.39967 + m.x4)**2 + m.x7
    <= 0)
m.e862 = Constraint(expr= -(-0.13643 + m.x1)**2 - (-0.56773 + m.x4)**2 + m.x7
    <= 0)
m.e863 = Constraint(expr= -(-0.03817 + m.x1)**2 - (-0.09287 + m.x4)**2 + m.x7
    <= 0)
m.e864 = Constraint(expr= -(-0.39923 + m.x1)**2 - (-0.77853 + m.x4)**2 + m.x7
    <= 0)
m.e865 = Constraint(expr= -(-0.19137 + m.x1)**2 - (-0.85807 + m.x4)**2 + m.x7
    <= 0)
m.e866 = Constraint(expr= -(-0.35003 + m.x1)**2 - (-0.75733 + m.x4)**2 + m.x7
    <= 0)
m.e867 = Constraint(expr= -(-0.01657 + m.x1)**2 - (-0.81527 + m.x4)**2 + m.x7
    <= 0)
m.e868 = Constraint(expr= -(-0.46883 + m.x1)**2 - (-0.78413 + m.x4)**2 + m.x7
    <= 0)
m.e869 = Constraint(expr= -(-0.63377 + m.x1)**2 - (-0.28447 + m.x4)**2 + m.x7
    <= 0)
m.e870 = Constraint(expr= -(-0.03563 + m.x1)**2 - (-0.93893 + m.x4)**2 + m.x7
    <= 0)
m.e871 = Constraint(expr= -(-0.36297 + m.x1)**2 - (-0.78567 + m.x4)**2 + m.x7
    <= 0)
m.e872 = Constraint(expr= -(-0.13043 + m.x1)**2 - (-0.10173 + m.x4)**2 + m.x7
    <= 0)
m.e873 = Constraint(expr= -(-0.72417 + m.x1)**2 - (-0.03887 + m.x4)**2 + m.x7
    <= 0)
m.e874 = Constraint(expr= -(-0.63323 + m.x1)**2 - (-0.95253 + m.x4)**2 + m.x7
    <= 0)
m.e875 = Constraint(expr= -(-0.43737 + m.x1)**2 - (-0.96407 + m.x4)**2 + m.x7
    <= 0)
m.e876 = Constraint(expr= -(-0.22403 + m.x1)**2 - (-0.97133 + m.x4)**2 + m.x7
    <= 0)
m.e877 = Constraint(expr= -(-0.42257 + m.x1)**2 - (-0.68127 + m.x4)**2 + m.x7
    <= 0)
m.e878 = Constraint(expr= -(-0.38283 + m.x1)**2 - (-0.43813 + m.x4)**2 + m.x7
    <= 0)
m.e879 = Constraint(expr= -(-0.79977 + m.x1)**2 - (-0.51047 + m.x4)**2 + m.x7
    <= 0)
m.e880 = Constraint(expr= -(-0.38963 + m.x1)**2 - (-0.43293 + m.x4)**2 + m.x7
    <= 0)
m.e881 = Constraint(expr= -(-0.88897 + m.x1)**2 - (-0.97167 + m.x4)**2 + m.x7
    <= 0)
m.e882 = Constraint(expr= -(-0.32443 + m.x1)**2 - (-0.83573 + m.x4)**2 + m.x7
    <= 0)
m.e883 = Constraint(expr= -(-0.21017 + m.x1)**2 - (-0.78487 + m.x4)**2 + m.x7
    <= 0)
m.e884 = Constraint(expr= -(-0.06723 + m.x1)**2 - (-0.32653 + m.x4)**2 + m.x7
    <= 0)
m.e885 = Constraint(expr= -(-0.48337 + m.x1)**2 - (-0.87007 + m.x4)**2 + m.x7
    <= 0)
m.e886 = Constraint(expr= -(-0.29803 + m.x1)**2 - (-0.38533 + m.x4)**2 + m.x7
    <= 0)
m.e887 = Constraint(expr= -(-0.62857 + m.x1)**2 - (-0.34727 + m.x4)**2 + m.x7
    <= 0)
m.e888 = Constraint(expr= -(-0.49683 + m.x1)**2 - (-0.29213 + m.x4)**2 + m.x7
    <= 0)
m.e889 = Constraint(expr= -(-0.76577 + m.x1)**2 - (-0.53647 + m.x4)**2 + m.x7
    <= 0)
m.e890 = Constraint(expr= -(-0.94363 + m.x1)**2 - (-0.12693 + m.x4)**2 + m.x7
    <= 0)
m.e891 = Constraint(expr= -(-0.21497 + m.x1)**2 - (-0.95767 + m.x4)**2 + m.x7
    <= 0)
m.e892 = Constraint(expr= -(-0.71843 + m.x1)**2 - (-0.76973 + m.x4)**2 + m.x7
    <= 0)
m.e893 = Constraint(expr= -(-0.49617 + m.x1)**2 - (-0.33087 + m.x4)**2 + m.x7
    <= 0)
m.e894 = Constraint(expr= -(-0.70123 + m.x1)**2 - (-0.90053 + m.x4)**2 + m.x7
    <= 0)
m.e895 = Constraint(expr= -(-0.32937 + m.x1)**2 - (-0.57607 + m.x4)**2 + m.x7
    <= 0)
m.e896 = Constraint(expr= -(-0.57203 + m.x1)**2 - (-0.99933 + m.x4)**2 + m.x7
    <= 0)
m.e897 = Constraint(expr= -(-0.63457 + m.x1)**2 - (-0.81327 + m.x4)**2 + m.x7
    <= 0)
m.e898 = Constraint(expr= -(-0.81083 + m.x1)**2 - (-0.34613 + m.x4)**2 + m.x7
    <= 0)
m.e899 = Constraint(expr= -(-0.53177 + m.x1)**2 - (-0.36247 + m.x4)**2 + m.x7
    <= 0)
m.e900 = Constraint(expr= -(-0.69763 + m.x1)**2 - (-0.02093 + m.x4)**2 + m.x7
    <= 0)
m.e901 = Constraint(expr= -(-0.34097 + m.x1)**2 - (-0.74367 + m.x4)**2 + m.x7
    <= 0)
m.e902 = Constraint(expr= -(-0.31243 + m.x1)**2 - (-0.90373 + m.x4)**2 + m.x7
    <= 0)
m.e903 = Constraint(expr= -(-0.58217 + m.x1)**2 - (-0.67687 + m.x4)**2 + m.x7
    <= 0)
m.e904 = Constraint(expr= -(-0.53523 + m.x1)**2 - (-0.67453 + m.x4)**2 + m.x7
    <= 0)
m.e905 = Constraint(expr= -(-0.97537 + m.x1)**2 - (-0.08207 + m.x4)**2 + m.x7
    <= 0)
m.e906 = Constraint(expr= -(-0.04603 + m.x1)**2 - (-0.81333 + m.x4)**2 + m.x7
    <= 0)
m.e907 = Constraint(expr= -(-0.44057 + m.x1)**2 - (-0.07927 + m.x4)**2 + m.x7
    <= 0)
m.e908 = Constraint(expr= -(-0.32483 + m.x1)**2 - (-0.60013 + m.x4)**2 + m.x7
    <= 0)
m.e909 = Constraint(expr= -(-0.09777 + m.x1)**2 - (-0.98847 + m.x4)**2 + m.x7
    <= 0)
m.e910 = Constraint(expr= -(-0.65163 + m.x1)**2 - (-0.11493 + m.x4)**2 + m.x7
    <= 0)
m.e911 = Constraint(expr= -(-0.26697 + m.x1)**2 - (-0.32967 + m.x4)**2 + m.x7
    <= 0)
m.e912 = Constraint(expr= -(-0.10643 + m.x1)**2 - (-0.23773 + m.x4)**2 + m.x7
    <= 0)
m.e913 = Constraint(expr= -(-0.46817 + m.x1)**2 - (-0.82287 + m.x4)**2 + m.x7
    <= 0)
m.e914 = Constraint(expr= -(-0.56923 + m.x1)**2 - (-0.64853 + m.x4)**2 + m.x7
    <= 0)
m.e915 = Constraint(expr= -(-0.42137 + m.x1)**2 - (-0.38807 + m.x4)**2 + m.x7
    <= 0)
m.e916 = Constraint(expr= -(-0.72003 + m.x1)**2 - (-0.82733 + m.x4)**2 + m.x7
    <= 0)
m.e917 = Constraint(expr= -(-0.04657 + m.x1)**2 - (-0.14527 + m.x4)**2 + m.x7
    <= 0)
m.e918 = Constraint(expr= -(-0.03883 + m.x1)**2 - (-0.05413 + m.x4)**2 + m.x7
    <= 0)
m.e919 = Constraint(expr= -(-0.46377 + m.x1)**2 - (-0.41447 + m.x4)**2 + m.x7
    <= 0)
m.e920 = Constraint(expr= -(-0.80563 + m.x1)**2 - (-0.40893 + m.x4)**2 + m.x7
    <= 0)
m.e921 = Constraint(expr= -(-0.99297 + m.x1)**2 - (-0.71567 + m.x4)**2 + m.x7
    <= 0)
m.e922 = Constraint(expr= -(-0.10043 + m.x1)**2 - (-0.77173 + m.x4)**2 + m.x7
    <= 0)
m.e923 = Constraint(expr= -(-0.15417 + m.x1)**2 - (-0.76887 + m.x4)**2 + m.x7
    <= 0)
m.e924 = Constraint(expr= -(-0.80323 + m.x1)**2 - (-0.82253 + m.x4)**2 + m.x7
    <= 0)
m.e925 = Constraint(expr= -(-0.66737 + m.x1)**2 - (-0.49407 + m.x4)**2 + m.x7
    <= 0)
m.e926 = Constraint(expr= -(-0.59403 + m.x1)**2 - (-0.04133 + m.x4)**2 + m.x7
    <= 0)
m.e927 = Constraint(expr= -(-0.45257 + m.x1)**2 - (-0.01127 + m.x4)**2 + m.x7
    <= 0)
m.e928 = Constraint(expr= -(-0.95283 + m.x1)**2 - (-0.70813 + m.x4)**2 + m.x7
    <= 0)
m.e929 = Constraint(expr= -(-0.62977 + m.x1)**2 - (-0.64047 + m.x4)**2 + m.x7
    <= 0)
m.e930 = Constraint(expr= -(-0.15963 + m.x1)**2 - (-0.90293 + m.x4)**2 + m.x7
    <= 0)
m.e931 = Constraint(expr= -(-0.51897 + m.x1)**2 - (-0.90167 + m.x4)**2 + m.x7
    <= 0)
m.e932 = Constraint(expr= -(-0.29443 + m.x1)**2 - (-0.50573 + m.x4)**2 + m.x7
    <= 0)
m.e933 = Constraint(expr= -(-0.64017 + m.x1)**2 - (-0.51487 + m.x4)**2 + m.x7
    <= 0)
m.e934 = Constraint(expr= -(-0.23723 + m.x1)**2 - (-0.19653 + m.x4)**2 + m.x7
    <= 0)
m.e935 = Constraint(expr= -(-0.71337 + m.x1)**2 - (-0.40007 + m.x4)**2 + m.x7
    <= 0)
m.e936 = Constraint(expr= -(-0.66803 + m.x1)**2 - (-0.45533 + m.x4)**2 + m.x7
    <= 0)
m.e937 = Constraint(expr= -(-0.65857 + m.x1)**2 - (-0.67727 + m.x4)**2 + m.x7
    <= 0)
m.e938 = Constraint(expr= -(-0.06683 + m.x1)**2 - (-0.56213 + m.x4)**2 + m.x7
    <= 0)
m.e939 = Constraint(expr= -(-0.59577 + m.x1)**2 - (-0.66647 + m.x4)**2 + m.x7
    <= 0)
m.e940 = Constraint(expr= -(-0.71363 + m.x1)**2 - (-0.59693 + m.x4)**2 + m.x7
    <= 0)
m.e941 = Constraint(expr= -(-0.84497 + m.x1)**2 - (-0.88767 + m.x4)**2 + m.x7
    <= 0)
m.e942 = Constraint(expr= -(-0.68843 + m.x1)**2 - (-0.43973 + m.x4)**2 + m.x7
    <= 0)
m.e943 = Constraint(expr= -(-0.92617 + m.x1)**2 - (-0.06087 + m.x4)**2 + m.x7
    <= 0)
m.e944 = Constraint(expr= -(-0.87123 + m.x1)**2 - (-0.77053 + m.x4)**2 + m.x7
    <= 0)
m.e945 = Constraint(expr= -(-0.55937 + m.x1)**2 - (-0.10607 + m.x4)**2 + m.x7
    <= 0)
m.e946 = Constraint(expr= -(-0.94203 + m.x1)**2 - (-0.06933 + m.x4)**2 + m.x7
    <= 0)
m.e947 = Constraint(expr= -(-0.66457 + m.x1)**2 - (-0.14327 + m.x4)**2 + m.x7
    <= 0)
m.e948 = Constraint(expr= -(-0.38083 + m.x1)**2 - (-0.61613 + m.x4)**2 + m.x7
    <= 0)
m.e949 = Constraint(expr= -(-0.36177 + m.x1)**2 - (-0.49247 + m.x4)**2 + m.x7
    <= 0)
m.e950 = Constraint(expr= -(-0.46763 + m.x1)**2 - (-0.49093 + m.x4)**2 + m.x7
    <= 0)
m.e951 = Constraint(expr= -(-0.97097 + m.x1)**2 - (-0.67367 + m.x4)**2 + m.x7
    <= 0)
m.e952 = Constraint(expr= -(-0.28243 + m.x1)**2 - (-0.57373 + m.x4)**2 + m.x7
    <= 0)
m.e953 = Constraint(expr= -(-0.01217 + m.x1)**2 - (-0.40687 + m.x4)**2 + m.x7
    <= 0)
m.e954 = Constraint(expr= -(-0.70523 + m.x1)**2 - (-0.54453 + m.x4)**2 + m.x7
    <= 0)
m.e955 = Constraint(expr= -(-0.20537 + m.x1)**2 - (-0.61207 + m.x4)**2 + m.x7
    <= 0)
m.e956 = Constraint(expr= -(-0.41603 + m.x1)**2 - (-0.88333 + m.x4)**2 + m.x7
    <= 0)
m.e957 = Constraint(expr= -(-0.47057 + m.x1)**2 - (-0.40927 + m.x4)**2 + m.x7
    <= 0)
m.e958 = Constraint(expr= -(-0.89483 + m.x1)**2 - (-0.87013 + m.x4)**2 + m.x7
    <= 0)
m.e959 = Constraint(expr= -(-0.92777 + m.x1)**2 - (-0.11847 + m.x4)**2 + m.x7
    <= 0)
m.e960 = Constraint(expr= -(-0.42163 + m.x1)**2 - (-0.58493 + m.x4)**2 + m.x7
    <= 0)
m.e961 = Constraint(expr= -(-0.89697 + m.x1)**2 - (-0.25967 + m.x4)**2 + m.x7
    <= 0)
m.e962 = Constraint(expr= -(-0.07643 + m.x1)**2 - (-0.90773 + m.x4)**2 + m.x7
    <= 0)
m.e963 = Constraint(expr= -(-0.89817 + m.x1)**2 - (-0.55287 + m.x4)**2 + m.x7
    <= 0)
m.e964 = Constraint(expr= -(-0.73923 + m.x1)**2 - (-0.51853 + m.x4)**2 + m.x7
    <= 0)
m.e965 = Constraint(expr= -(-0.65137 + m.x1)**2 - (-0.91807 + m.x4)**2 + m.x7
    <= 0)
m.e966 = Constraint(expr= -(-0.09003 + m.x1)**2 - (-0.89733 + m.x4)**2 + m.x7
    <= 0)
m.e967 = Constraint(expr= -(-0.07657 + m.x1)**2 - (-0.47527 + m.x4)**2 + m.x7
    <= 0)
m.e968 = Constraint(expr= -(-0.60883 + m.x1)**2 - (-0.32413 + m.x4)**2 + m.x7
    <= 0)
m.e969 = Constraint(expr= -(-0.29377 + m.x1)**2 - (-0.54447 + m.x4)**2 + m.x7
    <= 0)
m.e970 = Constraint(expr= -(-0.57563 + m.x1)**2 - (-0.87893 + m.x4)**2 + m.x7
    <= 0)
m.e971 = Constraint(expr= -(-0.62297 + m.x1)**2 - (-0.64567 + m.x4)**2 + m.x7
    <= 0)
m.e972 = Constraint(expr= -(-0.07043 + m.x1)**2 - (-0.44173 + m.x4)**2 + m.x7
    <= 0)
m.e973 = Constraint(expr= -(-0.58417 + m.x1)**2 - (-0.49887 + m.x4)**2 + m.x7
    <= 0)
m.e974 = Constraint(expr= -(-0.97323 + m.x1)**2 - (-0.69253 + m.x4)**2 + m.x7
    <= 0)
m.e975 = Constraint(expr= -(-0.89737 + m.x1)**2 - (-0.02407 + m.x4)**2 + m.x7
    <= 0)
m.e976 = Constraint(expr= -(-0.96403 + m.x1)**2 - (-0.11133 + m.x4)**2 + m.x7
    <= 0)
m.e977 = Constraint(expr= -(-0.48257 + m.x1)**2 - (-0.34127 + m.x4)**2 + m.x7
    <= 0)
m.e978 = Constraint(expr= -(-0.52283 + m.x1)**2 - (-0.97813 + m.x4)**2 + m.x7
    <= 0)
m.e979 = Constraint(expr= -(-0.45977 + m.x1)**2 - (-0.77047 + m.x4)**2 + m.x7
    <= 0)
m.e980 = Constraint(expr= -(-0.92963 + m.x1)**2 - (-0.37293 + m.x4)**2 + m.x7
    <= 0)
m.e981 = Constraint(expr= -(-0.14897 + m.x1)**2 - (-0.83167 + m.x4)**2 + m.x7
    <= 0)
m.e982 = Constraint(expr= -(-0.26443 + m.x1)**2 - (-0.17573 + m.x4)**2 + m.x7
    <= 0)
m.e983 = Constraint(expr= -(-0.07017 + m.x1)**2 - (-0.24487 + m.x4)**2 + m.x7
    <= 0)
m.e984 = Constraint(expr= -(-0.40723 + m.x1)**2 - (-0.06653 + m.x4)**2 + m.x7
    <= 0)
m.e985 = Constraint(expr= -(-0.94337 + m.x1)**2 - (-0.93007 + m.x4)**2 + m.x7
    <= 0)
m.e986 = Constraint(expr= -(-0.03803 + m.x1)**2 - (-0.52533 + m.x4)**2 + m.x7
    <= 0)
m.e987 = Constraint(expr= -(-0.68857 + m.x1)**2 - (-0.00727 + m.x4)**2 + m.x7
    <= 0)
m.e988 = Constraint(expr= -(-0.63683 + m.x1)**2 - (-0.83213 + m.x4)**2 + m.x7
    <= 0)
m.e989 = Constraint(expr= -(-0.42577 + m.x1)**2 - (-0.79647 + m.x4)**2 + m.x7
    <= 0)
m.e990 = Constraint(expr= -(-0.48363 + m.x1)**2 - (-0.06693 + m.x4)**2 + m.x7
    <= 0)
m.e991 = Constraint(expr= -(-0.47497 + m.x1)**2 - (-0.81767 + m.x4)**2 + m.x7
    <= 0)
m.e992 = Constraint(expr= -(-0.65843 + m.x1)**2 - (-0.10973 + m.x4)**2 + m.x7
    <= 0)
m.e993 = Constraint(expr= -(-0.35617 + m.x1)**2 - (-0.79087 + m.x4)**2 + m.x7
    <= 0)
m.e994 = Constraint(expr= -(-0.04123 + m.x1)**2 - (-0.64053 + m.x4)**2 + m.x7
    <= 0)
m.e995 = Constraint(expr= -(-0.78937 + m.x1)**2 - (-0.63607 + m.x4)**2 + m.x7
    <= 0)
m.e996 = Constraint(expr= -(-0.31203 + m.x1)**2 - (-0.13933 + m.x4)**2 + m.x7
    <= 0)
m.e997 = Constraint(expr= -(-0.69457 + m.x1)**2 - (-0.47327 + m.x4)**2 + m.x7
    <= 0)
m.e998 = Constraint(expr= -(-0.95083 + m.x1)**2 - (-0.88613 + m.x4)**2 + m.x7
    <= 0)
m.e999 = Constraint(expr= -(-0.19177 + m.x1)**2 - (-0.62247 + m.x4)**2 + m.x7
    <= 0)
m.e1000 = Constraint(expr= -(-0.23763 + m.x1)**2 - (-0.96093 + m.x4)**2 + m.x7
    <= 0)
m.e1001 = Constraint(expr= -(-0.00097 + m.x2)**2 - (-0.00367 + m.x5)**2 + m.x7
    <= 0)
m.e1002 = Constraint(expr= -(-0.85243 + m.x2)**2 - (-0.84373 + m.x5)**2 + m.x7
    <= 0)
m.e1003 = Constraint(expr= -(-0.84217 + m.x2)**2 - (-0.53687 + m.x5)**2 + m.x7
    <= 0)
m.e1004 = Constraint(expr= -(-0.47523 + m.x2)**2 - (-0.01453 + m.x5)**2 + m.x7
    <= 0)
m.e1005 = Constraint(expr= -(-0.83537 + m.x2)**2 - (-0.54207 + m.x5)**2 + m.x7
    <= 0)
m.e1006 = Constraint(expr= -(-0.38603 + m.x2)**2 - (-0.55333 + m.x5)**2 + m.x7
    <= 0)
m.e1007 = Constraint(expr= -(-0.90057 + m.x2)**2 - (-0.13927 + m.x5)**2 + m.x7
    <= 0)
m.e1008 = Constraint(expr= -(-0.06483 + m.x2)**2 - (-0.74013 + m.x5)**2 + m.x7
    <= 0)
m.e1009 = Constraint(expr= -(-0.15777 + m.x2)**2 - (-0.64847 + m.x5)**2 + m.x7
    <= 0)
m.e1010 = Constraint(expr= -(-0.79163 + m.x2)**2 - (-0.65493 + m.x5)**2 + m.x7
    <= 0)
m.e1011 = Constraint(expr= -(-0.92697 + m.x2)**2 - (-0.58967 + m.x5)**2 + m.x7
    <= 0)
m.e1012 = Constraint(expr= -(-0.64643 + m.x2)**2 - (-0.17773 + m.x5)**2 + m.x7
    <= 0)
m.e1013 = Constraint(expr= -(-0.72817 + m.x2)**2 - (-0.68287 + m.x5)**2 + m.x7
    <= 0)
m.e1014 = Constraint(expr= -(-0.50923 + m.x2)**2 - (-0.98853 + m.x5)**2 + m.x7
    <= 0)
m.e1015 = Constraint(expr= -(-0.28137 + m.x2)**2 - (-0.84807 + m.x5)**2 + m.x7
    <= 0)
m.e1016 = Constraint(expr= -(-0.06003 + m.x2)**2 - (-0.56733 + m.x5)**2 + m.x7
    <= 0)
m.e1017 = Constraint(expr= -(-0.50657 + m.x2)**2 - (-0.20527 + m.x5)**2 + m.x7
    <= 0)
m.e1018 = Constraint(expr= -(-0.77883 + m.x2)**2 - (-0.19413 + m.x5)**2 + m.x7
    <= 0)
m.e1019 = Constraint(expr= -(-0.52377 + m.x2)**2 - (-0.07447 + m.x5)**2 + m.x7
    <= 0)
m.e1020 = Constraint(expr= -(-0.94563 + m.x2)**2 - (-0.94893 + m.x5)**2 + m.x7
    <= 0)
m.e1021 = Constraint(expr= -(-0.65297 + m.x2)**2 - (-0.97567 + m.x5)**2 + m.x7
    <= 0)
m.e1022 = Constraint(expr= -(-0.64043 + m.x2)**2 - (-0.71173 + m.x5)**2 + m.x7
    <= 0)
m.e1023 = Constraint(expr= -(-0.41417 + m.x2)**2 - (-0.62887 + m.x5)**2 + m.x7
    <= 0)
m.e1024 = Constraint(expr= -(-0.74323 + m.x2)**2 - (-0.16253 + m.x5)**2 + m.x7
    <= 0)
m.e1025 = Constraint(expr= -(-0.52737 + m.x2)**2 - (-0.95407 + m.x5)**2 + m.x7
    <= 0)
m.e1026 = Constraint(expr= -(-0.93403 + m.x2)**2 - (-0.78133 + m.x5)**2 + m.x7
    <= 0)
m.e1027 = Constraint(expr= -(-0.91257 + m.x2)**2 - (-0.07127 + m.x5)**2 + m.x7
    <= 0)
m.e1028 = Constraint(expr= -(-0.69283 + m.x2)**2 - (-0.84813 + m.x5)**2 + m.x7
    <= 0)
m.e1029 = Constraint(expr= -(-0.68977 + m.x2)**2 - (-0.30047 + m.x5)**2 + m.x7
    <= 0)
m.e1030 = Constraint(expr= -(-0.29963 + m.x2)**2 - (-0.44293 + m.x5)**2 + m.x7
    <= 0)
m.e1031 = Constraint(expr= -(-0.17897 + m.x2)**2 - (-0.16167 + m.x5)**2 + m.x7
    <= 0)
m.e1032 = Constraint(expr= -(-0.83443 + m.x2)**2 - (-0.44573 + m.x5)**2 + m.x7
    <= 0)
m.e1033 = Constraint(expr= -(-0.90017 + m.x2)**2 - (-0.37487 + m.x5)**2 + m.x7
    <= 0)
m.e1034 = Constraint(expr= -(-0.17723 + m.x2)**2 - (-0.53653 + m.x5)**2 + m.x7
    <= 0)
m.e1035 = Constraint(expr= -(-0.57337 + m.x2)**2 - (-0.86007 + m.x5)**2 + m.x7
    <= 0)
m.e1036 = Constraint(expr= -(-0.00803 + m.x2)**2 - (-0.19533 + m.x5)**2 + m.x7
    <= 0)
m.e1037 = Constraint(expr= -(-0.11857 + m.x2)**2 - (-0.73727 + m.x5)**2 + m.x7
    <= 0)
m.e1038 = Constraint(expr= -(-0.80683 + m.x2)**2 - (-0.70213 + m.x5)**2 + m.x7
    <= 0)
m.e1039 = Constraint(expr= -(-0.65577 + m.x2)**2 - (-0.32647 + m.x5)**2 + m.x7
    <= 0)
m.e1040 = Constraint(expr= -(-0.85363 + m.x2)**2 - (-0.13693 + m.x5)**2 + m.x7
    <= 0)
m.e1041 = Constraint(expr= -(-0.50497 + m.x2)**2 - (-0.14767 + m.x5)**2 + m.x7
    <= 0)
m.e1042 = Constraint(expr= -(-0.22843 + m.x2)**2 - (-0.37973 + m.x5)**2 + m.x7
    <= 0)
m.e1043 = Constraint(expr= -(-0.18617 + m.x2)**2 - (-0.92087 + m.x5)**2 + m.x7
    <= 0)
m.e1044 = Constraint(expr= -(-0.81123 + m.x2)**2 - (-0.11053 + m.x5)**2 + m.x7
    <= 0)
m.e1045 = Constraint(expr= -(-0.41937 + m.x2)**2 - (-0.56607 + m.x5)**2 + m.x7
    <= 0)
m.e1046 = Constraint(expr= -(-0.28203 + m.x2)**2 - (-0.80933 + m.x5)**2 + m.x7
    <= 0)
m.e1047 = Constraint(expr= -(-0.12457 + m.x2)**2 - (-0.20327 + m.x5)**2 + m.x7
    <= 0)
m.e1048 = Constraint(expr= -(-0.12083 + m.x2)**2 - (-0.75613 + m.x5)**2 + m.x7
    <= 0)
m.e1049 = Constraint(expr= -(-0.42177 + m.x2)**2 - (-0.15247 + m.x5)**2 + m.x7
    <= 0)
m.e1050 = Constraint(expr= -(-0.60763 + m.x2)**2 - (-0.03093 + m.x5)**2 + m.x7
    <= 0)
m.e1051 = Constraint(expr= -(-0.63097 + m.x2)**2 - (-0.93367 + m.x5)**2 + m.x7
    <= 0)
m.e1052 = Constraint(expr= -(-0.82243 + m.x2)**2 - (-0.51373 + m.x5)**2 + m.x7
    <= 0)
m.e1053 = Constraint(expr= -(-0.27217 + m.x2)**2 - (-0.26687 + m.x5)**2 + m.x7
    <= 0)
m.e1054 = Constraint(expr= -(-0.64523 + m.x2)**2 - (-0.88453 + m.x5)**2 + m.x7
    <= 0)
m.e1055 = Constraint(expr= -(-0.06537 + m.x2)**2 - (-0.07207 + m.x5)**2 + m.x7
    <= 0)
m.e1056 = Constraint(expr= -(-0.75603 + m.x2)**2 - (-0.62333 + m.x5)**2 + m.x7
    <= 0)
m.e1057 = Constraint(expr= -(-0.93057 + m.x2)**2 - (-0.46927 + m.x5)**2 + m.x7
    <= 0)
m.e1058 = Constraint(expr= -(-0.63483 + m.x2)**2 - (-0.01013 + m.x5)**2 + m.x7
    <= 0)
m.e1059 = Constraint(expr= -(-0.98777 + m.x2)**2 - (-0.77847 + m.x5)**2 + m.x7
    <= 0)
m.e1060 = Constraint(expr= -(-0.56163 + m.x2)**2 - (-0.12493 + m.x5)**2 + m.x7
    <= 0)
m.e1061 = Constraint(expr= -(-0.55697 + m.x2)**2 - (-0.51967 + m.x5)**2 + m.x7
    <= 0)
m.e1062 = Constraint(expr= -(-0.61643 + m.x2)**2 - (-0.84773 + m.x5)**2 + m.x7
    <= 0)
m.e1063 = Constraint(expr= -(-0.15817 + m.x2)**2 - (-0.41287 + m.x5)**2 + m.x7
    <= 0)
m.e1064 = Constraint(expr= -(-0.67923 + m.x2)**2 - (-0.85853 + m.x5)**2 + m.x7
    <= 0)
m.e1065 = Constraint(expr= -(-0.51137 + m.x2)**2 - (-0.37807 + m.x5)**2 + m.x7
    <= 0)
m.e1066 = Constraint(expr= -(-0.43003 + m.x2)**2 - (-0.63733 + m.x5)**2 + m.x7
    <= 0)
m.e1067 = Constraint(expr= -(-0.53657 + m.x2)**2 - (-0.53527 + m.x5)**2 + m.x7
    <= 0)
m.e1068 = Constraint(expr= -(-0.34883 + m.x2)**2 - (-0.46413 + m.x5)**2 + m.x7
    <= 0)
m.e1069 = Constraint(expr= -(-0.35377 + m.x2)**2 - (-0.20447 + m.x5)**2 + m.x7
    <= 0)
m.e1070 = Constraint(expr= -(-0.71563 + m.x2)**2 - (-0.41893 + m.x5)**2 + m.x7
    <= 0)
m.e1071 = Constraint(expr= -(-0.28297 + m.x2)**2 - (-0.90567 + m.x5)**2 + m.x7
    <= 0)
m.e1072 = Constraint(expr= -(-0.61043 + m.x2)**2 - (-0.38173 + m.x5)**2 + m.x7
    <= 0)
m.e1073 = Constraint(expr= -(-0.84417 + m.x2)**2 - (-0.35887 + m.x5)**2 + m.x7
    <= 0)
m.e1074 = Constraint(expr= -(-0.91323 + m.x2)**2 - (-0.03253 + m.x5)**2 + m.x7
    <= 0)
m.e1075 = Constraint(expr= -(-0.75737 + m.x2)**2 - (-0.48407 + m.x5)**2 + m.x7
    <= 0)
m.e1076 = Constraint(expr= -(-0.30403 + m.x2)**2 - (-0.85133 + m.x5)**2 + m.x7
    <= 0)
m.e1077 = Constraint(expr= -(-0.94257 + m.x2)**2 - (-0.40127 + m.x5)**2 + m.x7
    <= 0)
m.e1078 = Constraint(expr= -(-0.26283 + m.x2)**2 - (-0.11813 + m.x5)**2 + m.x7
    <= 0)
m.e1079 = Constraint(expr= -(-0.51977 + m.x2)**2 - (-0.43047 + m.x5)**2 + m.x7
    <= 0)
m.e1080 = Constraint(expr= -(-0.06963 + m.x2)**2 - (-0.91293 + m.x5)**2 + m.x7
    <= 0)
m.e1081 = Constraint(expr= -(-0.80897 + m.x2)**2 - (-0.09167 + m.x5)**2 + m.x7
    <= 0)
m.e1082 = Constraint(expr= -(-0.80443 + m.x2)**2 - (-0.11573 + m.x5)**2 + m.x7
    <= 0)
m.e1083 = Constraint(expr= -(-0.33017 + m.x2)**2 - (-0.10487 + m.x5)**2 + m.x7
    <= 0)
m.e1084 = Constraint(expr= -(-0.34723 + m.x2)**2 - (-0.40653 + m.x5)**2 + m.x7
    <= 0)
m.e1085 = Constraint(expr= -(-0.80337 + m.x2)**2 - (-0.39007 + m.x5)**2 + m.x7
    <= 0)
m.e1086 = Constraint(expr= -(-0.37803 + m.x2)**2 - (-0.26533 + m.x5)**2 + m.x7
    <= 0)
m.e1087 = Constraint(expr= -(-0.14857 + m.x2)**2 - (-0.06727 + m.x5)**2 + m.x7
    <= 0)
m.e1088 = Constraint(expr= -(-0.37683 + m.x2)**2 - (-0.97213 + m.x5)**2 + m.x7
    <= 0)
m.e1089 = Constraint(expr= -(-0.48577 + m.x2)**2 - (-0.45647 + m.x5)**2 + m.x7
    <= 0)
m.e1090 = Constraint(expr= -(-0.62363 + m.x2)**2 - (-0.60693 + m.x5)**2 + m.x7
    <= 0)
m.e1091 = Constraint(expr= -(-0.13497 + m.x2)**2 - (-0.07767 + m.x5)**2 + m.x7
    <= 0)
m.e1092 = Constraint(expr= -(-0.19843 + m.x2)**2 - (-0.04973 + m.x5)**2 + m.x7
    <= 0)
m.e1093 = Constraint(expr= -(-0.61617 + m.x2)**2 - (-0.65087 + m.x5)**2 + m.x7
    <= 0)
m.e1094 = Constraint(expr= -(-0.98123 + m.x2)**2 - (-0.98053 + m.x5)**2 + m.x7
    <= 0)
m.e1095 = Constraint(expr= -(-0.64937 + m.x2)**2 - (-0.09607 + m.x5)**2 + m.x7
    <= 0)
m.e1096 = Constraint(expr= -(-0.65203 + m.x2)**2 - (-0.87933 + m.x5)**2 + m.x7
    <= 0)
m.e1097 = Constraint(expr= -(-0.15457 + m.x2)**2 - (-0.53327 + m.x5)**2 + m.x7
    <= 0)
m.e1098 = Constraint(expr= -(-0.69083 + m.x2)**2 - (-0.02613 + m.x5)**2 + m.x7
    <= 0)
m.e1099 = Constraint(expr= -(-0.25177 + m.x2)**2 - (-0.28247 + m.x5)**2 + m.x7
    <= 0)
m.e1100 = Constraint(expr= -(-0.37763 + m.x2)**2 - (-0.50093 + m.x5)**2 + m.x7
    <= 0)
m.e1101 = Constraint(expr= -(-0.26097 + m.x2)**2 - (-0.86367 + m.x5)**2 + m.x7
    <= 0)
m.e1102 = Constraint(expr= -(-0.79243 + m.x2)**2 - (-0.18373 + m.x5)**2 + m.x7
    <= 0)
m.e1103 = Constraint(expr= -(-0.70217 + m.x2)**2 - (-0.99687 + m.x5)**2 + m.x7
    <= 0)
m.e1104 = Constraint(expr= -(-0.81523 + m.x2)**2 - (-0.75453 + m.x5)**2 + m.x7
    <= 0)
m.e1105 = Constraint(expr= -(-0.29537 + m.x2)**2 - (-0.60207 + m.x5)**2 + m.x7
    <= 0)
m.e1106 = Constraint(expr= -(-0.12603 + m.x2)**2 - (-0.69333 + m.x5)**2 + m.x7
    <= 0)
m.e1107 = Constraint(expr= -(-0.96057 + m.x2)**2 - (-0.79927 + m.x5)**2 + m.x7
    <= 0)
m.e1108 = Constraint(expr= -(-0.20483 + m.x2)**2 - (-0.28013 + m.x5)**2 + m.x7
    <= 0)
m.e1109 = Constraint(expr= -(-0.81777 + m.x2)**2 - (-0.90847 + m.x5)**2 + m.x7
    <= 0)
m.e1110 = Constraint(expr= -(-0.33163 + m.x2)**2 - (-0.59493 + m.x5)**2 + m.x7
    <= 0)
m.e1111 = Constraint(expr= -(-0.18697 + m.x2)**2 - (-0.44967 + m.x5)**2 + m.x7
    <= 0)
m.e1112 = Constraint(expr= -(-0.58643 + m.x2)**2 - (-0.51773 + m.x5)**2 + m.x7
    <= 0)
m.e1113 = Constraint(expr= -(-0.58817 + m.x2)**2 - (-0.14287 + m.x5)**2 + m.x7
    <= 0)
m.e1114 = Constraint(expr= -(-0.84923 + m.x2)**2 - (-0.72853 + m.x5)**2 + m.x7
    <= 0)
m.e1115 = Constraint(expr= -(-0.74137 + m.x2)**2 - (-0.90807 + m.x5)**2 + m.x7
    <= 0)
m.e1116 = Constraint(expr= -(-0.80003 + m.x2)**2 - (-0.70733 + m.x5)**2 + m.x7
    <= 0)
m.e1117 = Constraint(expr= -(-0.56657 + m.x2)**2 - (-0.86527 + m.x5)**2 + m.x7
    <= 0)
m.e1118 = Constraint(expr= -(-0.91883 + m.x2)**2 - (-0.73413 + m.x5)**2 + m.x7
    <= 0)
m.e1119 = Constraint(expr= -(-0.18377 + m.x2)**2 - (-0.33447 + m.x5)**2 + m.x7
    <= 0)
m.e1120 = Constraint(expr= -(-0.48563 + m.x2)**2 - (-0.88893 + m.x5)**2 + m.x7
    <= 0)
m.e1121 = Constraint(expr= -(-0.91297 + m.x2)**2 - (-0.83567 + m.x5)**2 + m.x7
    <= 0)
m.e1122 = Constraint(expr= -(-0.58043 + m.x2)**2 - (-0.05173 + m.x5)**2 + m.x7
    <= 0)
m.e1123 = Constraint(expr= -(-0.27417 + m.x2)**2 - (-0.08887 + m.x5)**2 + m.x7
    <= 0)
m.e1124 = Constraint(expr= -(-0.08323 + m.x2)**2 - (-0.90253 + m.x5)**2 + m.x7
    <= 0)
m.e1125 = Constraint(expr= -(-0.98737 + m.x2)**2 - (-0.01407 + m.x5)**2 + m.x7
    <= 0)
m.e1126 = Constraint(expr= -(-0.67403 + m.x2)**2 - (-0.92133 + m.x5)**2 + m.x7
    <= 0)
m.e1127 = Constraint(expr= -(-0.97257 + m.x2)**2 - (-0.73127 + m.x5)**2 + m.x7
    <= 0)
m.e1128 = Constraint(expr= -(-0.83283 + m.x2)**2 - (-0.38813 + m.x5)**2 + m.x7
    <= 0)
m.e1129 = Constraint(expr= -(-0.34977 + m.x2)**2 - (-0.56047 + m.x5)**2 + m.x7
    <= 0)
m.e1130 = Constraint(expr= -(-0.83963 + m.x2)**2 - (-0.38293 + m.x5)**2 + m.x7
    <= 0)
m.e1131 = Constraint(expr= -(-0.43897 + m.x2)**2 - (-0.02167 + m.x5)**2 + m.x7
    <= 0)
m.e1132 = Constraint(expr= -(-0.77443 + m.x2)**2 - (-0.78573 + m.x5)**2 + m.x7
    <= 0)
m.e1133 = Constraint(expr= -(-0.76017 + m.x2)**2 - (-0.83487 + m.x5)**2 + m.x7
    <= 0)
m.e1134 = Constraint(expr= -(-0.51723 + m.x2)**2 - (-0.27653 + m.x5)**2 + m.x7
    <= 0)
m.e1135 = Constraint(expr= -(-0.03337 + m.x2)**2 - (-0.92007 + m.x5)**2 + m.x7
    <= 0)
m.e1136 = Constraint(expr= -(-0.74803 + m.x2)**2 - (-0.33533 + m.x5)**2 + m.x7
    <= 0)
m.e1137 = Constraint(expr= -(-0.17857 + m.x2)**2 - (-0.39727 + m.x5)**2 + m.x7
    <= 0)
m.e1138 = Constraint(expr= -(-0.94683 + m.x2)**2 - (-0.24213 + m.x5)**2 + m.x7
    <= 0)
m.e1139 = Constraint(expr= -(-0.31577 + m.x2)**2 - (-0.58647 + m.x5)**2 + m.x7
    <= 0)
m.e1140 = Constraint(expr= -(-0.39363 + m.x2)**2 - (-0.07693 + m.x5)**2 + m.x7
    <= 0)
m.e1141 = Constraint(expr= -(-0.76497 + m.x2)**2 - (-0.00767 + m.x5)**2 + m.x7
    <= 0)
m.e1142 = Constraint(expr= -(-0.16843 + m.x2)**2 - (-0.71973 + m.x5)**2 + m.x7
    <= 0)
m.e1143 = Constraint(expr= -(-0.04617 + m.x2)**2 - (-0.38087 + m.x5)**2 + m.x7
    <= 0)
m.e1144 = Constraint(expr= -(-0.15123 + m.x2)**2 - (-0.85053 + m.x5)**2 + m.x7
    <= 0)
m.e1145 = Constraint(expr= -(-0.87937 + m.x2)**2 - (-0.62607 + m.x5)**2 + m.x7
    <= 0)
m.e1146 = Constraint(expr= -(-0.02203 + m.x2)**2 - (-0.94933 + m.x5)**2 + m.x7
    <= 0)
m.e1147 = Constraint(expr= -(-0.18457 + m.x2)**2 - (-0.86327 + m.x5)**2 + m.x7
    <= 0)
m.e1148 = Constraint(expr= -(-0.26083 + m.x2)**2 - (-0.29613 + m.x5)**2 + m.x7
    <= 0)
m.e1149 = Constraint(expr= -(-0.08177 + m.x2)**2 - (-0.41247 + m.x5)**2 + m.x7
    <= 0)
m.e1150 = Constraint(expr= -(-0.14763 + m.x2)**2 - (-0.97093 + m.x5)**2 + m.x7
    <= 0)
m.e1151 = Constraint(expr= -(-0.89097 + m.x2)**2 - (-0.79367 + m.x5)**2 + m.x7
    <= 0)
m.e1152 = Constraint(expr= -(-0.76243 + m.x2)**2 - (-0.85373 + m.x5)**2 + m.x7
    <= 0)
m.e1153 = Constraint(expr= -(-0.13217 + m.x2)**2 - (-0.72687 + m.x5)**2 + m.x7
    <= 0)
m.e1154 = Constraint(expr= -(-0.98523 + m.x2)**2 - (-0.62453 + m.x5)**2 + m.x7
    <= 0)
m.e1155 = Constraint(expr= -(-0.52537 + m.x2)**2 - (-0.13207 + m.x5)**2 + m.x7
    <= 0)
m.e1156 = Constraint(expr= -(-0.49603 + m.x2)**2 - (-0.76333 + m.x5)**2 + m.x7
    <= 0)
m.e1157 = Constraint(expr= -(-0.99057 + m.x2)**2 - (-0.12927 + m.x5)**2 + m.x7
    <= 0)
m.e1158 = Constraint(expr= -(-0.77483 + m.x2)**2 - (-0.55013 + m.x5)**2 + m.x7
    <= 0)
m.e1159 = Constraint(expr= -(-0.64777 + m.x2)**2 - (-0.03847 + m.x5)**2 + m.x7
    <= 0)
m.e1160 = Constraint(expr= -(-0.10163 + m.x2)**2 - (-0.06493 + m.x5)**2 + m.x7
    <= 0)
m.e1161 = Constraint(expr= -(-0.81697 + m.x2)**2 - (-0.37967 + m.x5)**2 + m.x7
    <= 0)
m.e1162 = Constraint(expr= -(-0.55643 + m.x2)**2 - (-0.18773 + m.x5)**2 + m.x7
    <= 0)
m.e1163 = Constraint(expr= -(-0.01817 + m.x2)**2 - (-0.87287 + m.x5)**2 + m.x7
    <= 0)
m.e1164 = Constraint(expr= -(-0.01923 + m.x2)**2 - (-0.59853 + m.x5)**2 + m.x7
    <= 0)
m.e1165 = Constraint(expr= -(-0.97137 + m.x2)**2 - (-0.43807 + m.x5)**2 + m.x7
    <= 0)
m.e1166 = Constraint(expr= -(-0.17003 + m.x2)**2 - (-0.77733 + m.x5)**2 + m.x7
    <= 0)
m.e1167 = Constraint(expr= -(-0.59657 + m.x2)**2 - (-0.19527 + m.x5)**2 + m.x7
    <= 0)
m.e1168 = Constraint(expr= -(-0.48883 + m.x2)**2 - (-0.00413 + m.x5)**2 + m.x7
    <= 0)
m.e1169 = Constraint(expr= -(-0.01377 + m.x2)**2 - (-0.46447 + m.x5)**2 + m.x7
    <= 0)
m.e1170 = Constraint(expr= -(-0.25563 + m.x2)**2 - (-0.35893 + m.x5)**2 + m.x7
    <= 0)
m.e1171 = Constraint(expr= -(-0.54297 + m.x2)**2 - (-0.76567 + m.x5)**2 + m.x7
    <= 0)
m.e1172 = Constraint(expr= -(-0.55043 + m.x2)**2 - (-0.72173 + m.x5)**2 + m.x7
    <= 0)
m.e1173 = Constraint(expr= -(-0.70417 + m.x2)**2 - (-0.81887 + m.x5)**2 + m.x7
    <= 0)
m.e1174 = Constraint(expr= -(-0.25323 + m.x2)**2 - (-0.77253 + m.x5)**2 + m.x7
    <= 0)
m.e1175 = Constraint(expr= -(-0.21737 + m.x2)**2 - (-0.54407 + m.x5)**2 + m.x7
    <= 0)
m.e1176 = Constraint(expr= -(-0.04403 + m.x2)**2 - (-0.99133 + m.x5)**2 + m.x7
    <= 0)
m.e1177 = Constraint(expr= -(-0.00257 + m.x2)**2 - (-0.06127 + m.x5)**2 + m.x7
    <= 0)
m.e1178 = Constraint(expr= -(-0.40283 + m.x2)**2 - (-0.65813 + m.x5)**2 + m.x7
    <= 0)
m.e1179 = Constraint(expr= -(-0.17977 + m.x2)**2 - (-0.69047 + m.x5)**2 + m.x7
    <= 0)
m.e1180 = Constraint(expr= -(-0.60963 + m.x2)**2 - (-0.85293 + m.x5)**2 + m.x7
    <= 0)
m.e1181 = Constraint(expr= -(-0.06897 + m.x2)**2 - (-0.95167 + m.x5)**2 + m.x7
    <= 0)
m.e1182 = Constraint(expr= -(-0.74443 + m.x2)**2 - (-0.45573 + m.x5)**2 + m.x7
    <= 0)
m.e1183 = Constraint(expr= -(-0.19017 + m.x2)**2 - (-0.56487 + m.x5)**2 + m.x7
    <= 0)
m.e1184 = Constraint(expr= -(-0.68723 + m.x2)**2 - (-0.14653 + m.x5)**2 + m.x7
    <= 0)
m.e1185 = Constraint(expr= -(-0.26337 + m.x2)**2 - (-0.45007 + m.x5)**2 + m.x7
    <= 0)
m.e1186 = Constraint(expr= -(-0.11803 + m.x2)**2 - (-0.40533 + m.x5)**2 + m.x7
    <= 0)
m.e1187 = Constraint(expr= -(-0.20857 + m.x2)**2 - (-0.72727 + m.x5)**2 + m.x7
    <= 0)
m.e1188 = Constraint(expr= -(-0.51683 + m.x2)**2 - (-0.51213 + m.x5)**2 + m.x7
    <= 0)
m.e1189 = Constraint(expr= -(-0.14577 + m.x2)**2 - (-0.71647 + m.x5)**2 + m.x7
    <= 0)
m.e1190 = Constraint(expr= -(-0.16363 + m.x2)**2 - (-0.54693 + m.x5)**2 + m.x7
    <= 0)
m.e1191 = Constraint(expr= -(-0.39497 + m.x2)**2 - (-0.93767 + m.x5)**2 + m.x7
    <= 0)
m.e1192 = Constraint(expr= -(-0.13843 + m.x2)**2 - (-0.38973 + m.x5)**2 + m.x7
    <= 0)
m.e1193 = Constraint(expr= -(-0.47617 + m.x2)**2 - (-0.11087 + m.x5)**2 + m.x7
    <= 0)
m.e1194 = Constraint(expr= -(-0.32123 + m.x2)**2 - (-0.72053 + m.x5)**2 + m.x7
    <= 0)
m.e1195 = Constraint(expr= -(-0.10937 + m.x2)**2 - (-0.15607 + m.x5)**2 + m.x7
    <= 0)
m.e1196 = Constraint(expr= -(-0.39203 + m.x2)**2 - (-0.01933 + m.x5)**2 + m.x7
    <= 0)
m.e1197 = Constraint(expr= -(-0.21457 + m.x2)**2 - (-0.19327 + m.x5)**2 + m.x7
    <= 0)
m.e1198 = Constraint(expr= -(-0.83083 + m.x2)**2 - (-0.56613 + m.x5)**2 + m.x7
    <= 0)
m.e1199 = Constraint(expr= -(-0.91177 + m.x2)**2 - (-0.54247 + m.x5)**2 + m.x7
    <= 0)
m.e1200 = Constraint(expr= -(-0.91763 + m.x2)**2 - (-0.44093 + m.x5)**2 + m.x7
    <= 0)
m.e1201 = Constraint(expr= -(-0.52097 + m.x2)**2 - (-0.72367 + m.x5)**2 + m.x7
    <= 0)
m.e1202 = Constraint(expr= -(-0.73243 + m.x2)**2 - (-0.52373 + m.x5)**2 + m.x7
    <= 0)
m.e1203 = Constraint(expr= -(-0.56217 + m.x2)**2 - (-0.45687 + m.x5)**2 + m.x7
    <= 0)
m.e1204 = Constraint(expr= -(-0.15523 + m.x2)**2 - (-0.49453 + m.x5)**2 + m.x7
    <= 0)
m.e1205 = Constraint(expr= -(-0.75537 + m.x2)**2 - (-0.66207 + m.x5)**2 + m.x7
    <= 0)
m.e1206 = Constraint(expr= -(-0.86603 + m.x2)**2 - (-0.83333 + m.x5)**2 + m.x7
    <= 0)
m.e1207 = Constraint(expr= -(-0.02057 + m.x2)**2 - (-0.45927 + m.x5)**2 + m.x7
    <= 0)
m.e1208 = Constraint(expr= -(-0.34483 + m.x2)**2 - (-0.82013 + m.x5)**2 + m.x7
    <= 0)
m.e1209 = Constraint(expr= -(-0.47777 + m.x2)**2 - (-0.16847 + m.x5)**2 + m.x7
    <= 0)
m.e1210 = Constraint(expr= -(-0.87163 + m.x2)**2 - (-0.53493 + m.x5)**2 + m.x7
    <= 0)
m.e1211 = Constraint(expr= -(-0.44697 + m.x2)**2 - (-0.30967 + m.x5)**2 + m.x7
    <= 0)
m.e1212 = Constraint(expr= -(-0.52643 + m.x2)**2 - (-0.85773 + m.x5)**2 + m.x7
    <= 0)
m.e1213 = Constraint(expr= -(-0.44817 + m.x2)**2 - (-0.60287 + m.x5)**2 + m.x7
    <= 0)
m.e1214 = Constraint(expr= -(-0.18923 + m.x2)**2 - (-0.46853 + m.x5)**2 + m.x7
    <= 0)
m.e1215 = Constraint(expr= -(-0.20137 + m.x2)**2 - (-0.96807 + m.x5)**2 + m.x7
    <= 0)
m.e1216 = Constraint(expr= -(-0.54003 + m.x2)**2 - (-0.84733 + m.x5)**2 + m.x7
    <= 0)
m.e1217 = Constraint(expr= -(-0.62657 + m.x2)**2 - (-0.52527 + m.x5)**2 + m.x7
    <= 0)
m.e1218 = Constraint(expr= -(-0.05883 + m.x2)**2 - (-0.27413 + m.x5)**2 + m.x7
    <= 0)
m.e1219 = Constraint(expr= -(-0.84377 + m.x2)**2 - (-0.59447 + m.x5)**2 + m.x7
    <= 0)
m.e1220 = Constraint(expr= -(-0.02563 + m.x2)**2 - (-0.82893 + m.x5)**2 + m.x7
    <= 0)
m.e1221 = Constraint(expr= -(-0.17297 + m.x2)**2 - (-0.69567 + m.x5)**2 + m.x7
    <= 0)
m.e1222 = Constraint(expr= -(-0.52043 + m.x2)**2 - (-0.39173 + m.x5)**2 + m.x7
    <= 0)
m.e1223 = Constraint(expr= -(-0.13417 + m.x2)**2 - (-0.54887 + m.x5)**2 + m.x7
    <= 0)
m.e1224 = Constraint(expr= -(-0.42323 + m.x2)**2 - (-0.64253 + m.x5)**2 + m.x7
    <= 0)
m.e1225 = Constraint(expr= -(-0.44737 + m.x2)**2 - (-0.07407 + m.x5)**2 + m.x7
    <= 0)
m.e1226 = Constraint(expr= -(-0.41403 + m.x2)**2 - (-0.06133 + m.x5)**2 + m.x7
    <= 0)
m.e1227 = Constraint(expr= -(-0.03257 + m.x2)**2 - (-0.39127 + m.x5)**2 + m.x7
    <= 0)
m.e1228 = Constraint(expr= -(-0.97283 + m.x2)**2 - (-0.92813 + m.x5)**2 + m.x7
    <= 0)
m.e1229 = Constraint(expr= -(-0.00977 + m.x2)**2 - (-0.82047 + m.x5)**2 + m.x7
    <= 0)
m.e1230 = Constraint(expr= -(-0.37963 + m.x2)**2 - (-0.32293 + m.x5)**2 + m.x7
    <= 0)
m.e1231 = Constraint(expr= -(-0.69897 + m.x2)**2 - (-0.88167 + m.x5)**2 + m.x7
    <= 0)
m.e1232 = Constraint(expr= -(-0.71443 + m.x2)**2 - (-0.12573 + m.x5)**2 + m.x7
    <= 0)
m.e1233 = Constraint(expr= -(-0.62017 + m.x2)**2 - (-0.29487 + m.x5)**2 + m.x7
    <= 0)
m.e1234 = Constraint(expr= -(-0.85723 + m.x2)**2 - (-0.01653 + m.x5)**2 + m.x7
    <= 0)
m.e1235 = Constraint(expr= -(-0.49337 + m.x2)**2 - (-0.98007 + m.x5)**2 + m.x7
    <= 0)
m.e1236 = Constraint(expr= -(-0.48803 + m.x2)**2 - (-0.47533 + m.x5)**2 + m.x7
    <= 0)
m.e1237 = Constraint(expr= -(-0.23857 + m.x2)**2 - (-0.05727 + m.x5)**2 + m.x7
    <= 0)
m.e1238 = Constraint(expr= -(-0.08683 + m.x2)**2 - (-0.78213 + m.x5)**2 + m.x7
    <= 0)
m.e1239 = Constraint(expr= -(-0.97577 + m.x2)**2 - (-0.84647 + m.x5)**2 + m.x7
    <= 0)
m.e1240 = Constraint(expr= -(-0.93363 + m.x2)**2 - (-0.01693 + m.x5)**2 + m.x7
    <= 0)
m.e1241 = Constraint(expr= -(-0.02497 + m.x2)**2 - (-0.86767 + m.x5)**2 + m.x7
    <= 0)
m.e1242 = Constraint(expr= -(-0.10843 + m.x2)**2 - (-0.05973 + m.x5)**2 + m.x7
    <= 0)
m.e1243 = Constraint(expr= -(-0.90617 + m.x2)**2 - (-0.84087 + m.x5)**2 + m.x7
    <= 0)
m.e1244 = Constraint(expr= -(-0.49123 + m.x2)**2 - (-0.59053 + m.x5)**2 + m.x7
    <= 0)
m.e1245 = Constraint(expr= -(-0.33937 + m.x2)**2 - (-0.68607 + m.x5)**2 + m.x7
    <= 0)
m.e1246 = Constraint(expr= -(-0.76203 + m.x2)**2 - (-0.08933 + m.x5)**2 + m.x7
    <= 0)
m.e1247 = Constraint(expr= -(-0.24457 + m.x2)**2 - (-0.52327 + m.x5)**2 + m.x7
    <= 0)
m.e1248 = Constraint(expr= -(-0.40083 + m.x2)**2 - (-0.83613 + m.x5)**2 + m.x7
    <= 0)
m.e1249 = Constraint(expr= -(-0.74177 + m.x2)**2 - (-0.67247 + m.x5)**2 + m.x7
    <= 0)
m.e1250 = Constraint(expr= -(-0.68763 + m.x2)**2 - (-0.91093 + m.x5)**2 + m.x7
    <= 0)
m.e1251 = Constraint(expr= -(-0.15097 + m.x2)**2 - (-0.65367 + m.x5)**2 + m.x7
    <= 0)
m.e1252 = Constraint(expr= -(-0.70243 + m.x2)**2 - (-0.19373 + m.x5)**2 + m.x7
    <= 0)
m.e1253 = Constraint(expr= -(-0.99217 + m.x2)**2 - (-0.18687 + m.x5)**2 + m.x7
    <= 0)
m.e1254 = Constraint(expr= -(-0.32523 + m.x2)**2 - (-0.36453 + m.x5)**2 + m.x7
    <= 0)
m.e1255 = Constraint(expr= -(-0.98537 + m.x2)**2 - (-0.19207 + m.x5)**2 + m.x7
    <= 0)
m.e1256 = Constraint(expr= -(-0.23603 + m.x2)**2 - (-0.90333 + m.x5)**2 + m.x7
    <= 0)
m.e1257 = Constraint(expr= -(-0.05057 + m.x2)**2 - (-0.78927 + m.x5)**2 + m.x7
    <= 0)
m.e1258 = Constraint(expr= -(-0.91483 + m.x2)**2 - (-0.09013 + m.x5)**2 + m.x7
    <= 0)
m.e1259 = Constraint(expr= -(-0.30777 + m.x2)**2 - (-0.29847 + m.x5)**2 + m.x7
    <= 0)
m.e1260 = Constraint(expr= -(-0.64163 + m.x2)**2 - (-0.00493 + m.x5)**2 + m.x7
    <= 0)
m.e1261 = Constraint(expr= -(-0.07697 + m.x2)**2 - (-0.23967 + m.x5)**2 + m.x7
    <= 0)
m.e1262 = Constraint(expr= -(-0.49643 + m.x2)**2 - (-0.52773 + m.x5)**2 + m.x7
    <= 0)
m.e1263 = Constraint(expr= -(-0.87817 + m.x2)**2 - (-0.33287 + m.x5)**2 + m.x7
    <= 0)
m.e1264 = Constraint(expr= -(-0.35923 + m.x2)**2 - (-0.33853 + m.x5)**2 + m.x7
    <= 0)
m.e1265 = Constraint(expr= -(-0.43137 + m.x2)**2 - (-0.49807 + m.x5)**2 + m.x7
    <= 0)
m.e1266 = Constraint(expr= -(-0.91003 + m.x2)**2 - (-0.91733 + m.x5)**2 + m.x7
    <= 0)
m.e1267 = Constraint(expr= -(-0.65657 + m.x2)**2 - (-0.85527 + m.x5)**2 + m.x7
    <= 0)
m.e1268 = Constraint(expr= -(-0.62883 + m.x2)**2 - (-0.54413 + m.x5)**2 + m.x7
    <= 0)
m.e1269 = Constraint(expr= -(-0.67377 + m.x2)**2 - (-0.72447 + m.x5)**2 + m.x7
    <= 0)
m.e1270 = Constraint(expr= -(-0.79563 + m.x2)**2 - (-0.29893 + m.x5)**2 + m.x7
    <= 0)
m.e1271 = Constraint(expr= -(-0.80297 + m.x2)**2 - (-0.62567 + m.x5)**2 + m.x7
    <= 0)
m.e1272 = Constraint(expr= -(-0.49043 + m.x2)**2 - (-0.06173 + m.x5)**2 + m.x7
    <= 0)
m.e1273 = Constraint(expr= -(-0.56417 + m.x2)**2 - (-0.27887 + m.x5)**2 + m.x7
    <= 0)
m.e1274 = Constraint(expr= -(-0.59323 + m.x2)**2 - (-0.51253 + m.x5)**2 + m.x7
    <= 0)
m.e1275 = Constraint(expr= -(-0.67737 + m.x2)**2 - (-0.60407 + m.x5)**2 + m.x7
    <= 0)
m.e1276 = Constraint(expr= -(-0.78403 + m.x2)**2 - (-0.13133 + m.x5)**2 + m.x7
    <= 0)
m.e1277 = Constraint(expr= -(-0.06257 + m.x2)**2 - (-0.72127 + m.x5)**2 + m.x7
    <= 0)
m.e1278 = Constraint(expr= -(-0.54283 + m.x2)**2 - (-0.19813 + m.x5)**2 + m.x7
    <= 0)
m.e1279 = Constraint(expr= -(-0.83977 + m.x2)**2 - (-0.95047 + m.x5)**2 + m.x7
    <= 0)
m.e1280 = Constraint(expr= -(-0.14963 + m.x2)**2 - (-0.79293 + m.x5)**2 + m.x7
    <= 0)
m.e1281 = Constraint(expr= -(-0.32897 + m.x2)**2 - (-0.81167 + m.x5)**2 + m.x7
    <= 0)
m.e1282 = Constraint(expr= -(-0.68443 + m.x2)**2 - (-0.79573 + m.x5)**2 + m.x7
    <= 0)
m.e1283 = Constraint(expr= -(-0.05017 + m.x2)**2 - (-0.02487 + m.x5)**2 + m.x7
    <= 0)
m.e1284 = Constraint(expr= -(-0.02723 + m.x2)**2 - (-0.88653 + m.x5)**2 + m.x7
    <= 0)
m.e1285 = Constraint(expr= -(-0.72337 + m.x2)**2 - (-0.51007 + m.x5)**2 + m.x7
    <= 0)
m.e1286 = Constraint(expr= -(-0.85803 + m.x2)**2 - (-0.54533 + m.x5)**2 + m.x7
    <= 0)
m.e1287 = Constraint(expr= -(-0.26857 + m.x2)**2 - (-0.38727 + m.x5)**2 + m.x7
    <= 0)
m.e1288 = Constraint(expr= -(-0.65683 + m.x2)**2 - (-0.05213 + m.x5)**2 + m.x7
    <= 0)
m.e1289 = Constraint(expr= -(-0.80577 + m.x2)**2 - (-0.97647 + m.x5)**2 + m.x7
    <= 0)
m.e1290 = Constraint(expr= -(-0.70363 + m.x2)**2 - (-0.48693 + m.x5)**2 + m.x7
    <= 0)
m.e1291 = Constraint(expr= -(-0.65497 + m.x2)**2 - (-0.79767 + m.x5)**2 + m.x7
    <= 0)
m.e1292 = Constraint(expr= -(-0.07843 + m.x2)**2 - (-0.72973 + m.x5)**2 + m.x7
    <= 0)
m.e1293 = Constraint(expr= -(-0.33617 + m.x2)**2 - (-0.57087 + m.x5)**2 + m.x7
    <= 0)
m.e1294 = Constraint(expr= -(-0.66123 + m.x2)**2 - (-0.46053 + m.x5)**2 + m.x7
    <= 0)
m.e1295 = Constraint(expr= -(-0.56937 + m.x2)**2 - (-0.21607 + m.x5)**2 + m.x7
    <= 0)
m.e1296 = Constraint(expr= -(-0.13203 + m.x2)**2 - (-0.15933 + m.x5)**2 + m.x7
    <= 0)
m.e1297 = Constraint(expr= -(-0.27457 + m.x2)**2 - (-0.85327 + m.x5)**2 + m.x7
    <= 0)
m.e1298 = Constraint(expr= -(-0.97083 + m.x2)**2 - (-0.10613 + m.x5)**2 + m.x7
    <= 0)
m.e1299 = Constraint(expr= -(-0.57177 + m.x2)**2 - (-0.80247 + m.x5)**2 + m.x7
    <= 0)
m.e1300 = Constraint(expr= -(-0.45763 + m.x2)**2 - (-0.38093 + m.x5)**2 + m.x7
    <= 0)
m.e1301 = Constraint(expr= -(-0.78097 + m.x2)**2 - (-0.58367 + m.x5)**2 + m.x7
    <= 0)
m.e1302 = Constraint(expr= -(-0.67243 + m.x2)**2 - (-0.86373 + m.x5)**2 + m.x7
    <= 0)
m.e1303 = Constraint(expr= -(-0.42217 + m.x2)**2 - (-0.91687 + m.x5)**2 + m.x7
    <= 0)
m.e1304 = Constraint(expr= -(-0.49523 + m.x2)**2 - (-0.23453 + m.x5)**2 + m.x7
    <= 0)
m.e1305 = Constraint(expr= -(-0.21537 + m.x2)**2 - (-0.72207 + m.x5)**2 + m.x7
    <= 0)
m.e1306 = Constraint(expr= -(-0.60603 + m.x2)**2 - (-0.97333 + m.x5)**2 + m.x7
    <= 0)
m.e1307 = Constraint(expr= -(-0.08057 + m.x2)**2 - (-0.11927 + m.x5)**2 + m.x7
    <= 0)
m.e1308 = Constraint(expr= -(-0.48483 + m.x2)**2 - (-0.36013 + m.x5)**2 + m.x7
    <= 0)
m.e1309 = Constraint(expr= -(-0.13777 + m.x2)**2 - (-0.42847 + m.x5)**2 + m.x7
    <= 0)
m.e1310 = Constraint(expr= -(-0.41163 + m.x2)**2 - (-0.47493 + m.x5)**2 + m.x7
    <= 0)
m.e1311 = Constraint(expr= -(-0.70697 + m.x2)**2 - (-0.16967 + m.x5)**2 + m.x7
    <= 0)
m.e1312 = Constraint(expr= -(-0.46643 + m.x2)**2 - (-0.19773 + m.x5)**2 + m.x7
    <= 0)
m.e1313 = Constraint(expr= -(-0.30817 + m.x2)**2 - (-0.06287 + m.x5)**2 + m.x7
    <= 0)
m.e1314 = Constraint(expr= -(-0.52923 + m.x2)**2 - (-0.20853 + m.x5)**2 + m.x7
    <= 0)
m.e1315 = Constraint(expr= -(-0.66137 + m.x2)**2 - (-0.02807 + m.x5)**2 + m.x7
    <= 0)
m.e1316 = Constraint(expr= -(-0.28003 + m.x2)**2 - (-0.98733 + m.x5)**2 + m.x7
    <= 0)
m.e1317 = Constraint(expr= -(-0.68657 + m.x2)**2 - (-0.18527 + m.x5)**2 + m.x7
    <= 0)
m.e1318 = Constraint(expr= -(-0.19883 + m.x2)**2 - (-0.81413 + m.x5)**2 + m.x7
    <= 0)
m.e1319 = Constraint(expr= -(-0.50377 + m.x2)**2 - (-0.85447 + m.x5)**2 + m.x7
    <= 0)
m.e1320 = Constraint(expr= -(-0.56563 + m.x2)**2 - (-0.76893 + m.x5)**2 + m.x7
    <= 0)
m.e1321 = Constraint(expr= -(-0.43297 + m.x2)**2 - (-0.55567 + m.x5)**2 + m.x7
    <= 0)
m.e1322 = Constraint(expr= -(-0.46043 + m.x2)**2 - (-0.73173 + m.x5)**2 + m.x7
    <= 0)
m.e1323 = Constraint(expr= -(-0.99417 + m.x2)**2 - (-0.00887 + m.x5)**2 + m.x7
    <= 0)
m.e1324 = Constraint(expr= -(-0.76323 + m.x2)**2 - (-0.38253 + m.x5)**2 + m.x7
    <= 0)
m.e1325 = Constraint(expr= -(-0.90737 + m.x2)**2 - (-0.13407 + m.x5)**2 + m.x7
    <= 0)
m.e1326 = Constraint(expr= -(-0.15403 + m.x2)**2 - (-0.20133 + m.x5)**2 + m.x7
    <= 0)
m.e1327 = Constraint(expr= -(-0.09257 + m.x2)**2 - (-0.05127 + m.x5)**2 + m.x7
    <= 0)
m.e1328 = Constraint(expr= -(-0.11283 + m.x2)**2 - (-0.46813 + m.x5)**2 + m.x7
    <= 0)
m.e1329 = Constraint(expr= -(-0.66977 + m.x2)**2 - (-0.08047 + m.x5)**2 + m.x7
    <= 0)
m.e1330 = Constraint(expr= -(-0.91963 + m.x2)**2 - (-0.26293 + m.x5)**2 + m.x7
    <= 0)
m.e1331 = Constraint(expr= -(-0.95897 + m.x2)**2 - (-0.74167 + m.x5)**2 + m.x7
    <= 0)
m.e1332 = Constraint(expr= -(-0.65443 + m.x2)**2 - (-0.46573 + m.x5)**2 + m.x7
    <= 0)
m.e1333 = Constraint(expr= -(-0.48017 + m.x2)**2 - (-0.75487 + m.x5)**2 + m.x7
    <= 0)
m.e1334 = Constraint(expr= -(-0.19723 + m.x2)**2 - (-0.75653 + m.x5)**2 + m.x7
    <= 0)
m.e1335 = Constraint(expr= -(-0.95337 + m.x2)**2 - (-0.04007 + m.x5)**2 + m.x7
    <= 0)
m.e1336 = Constraint(expr= -(-0.22803 + m.x2)**2 - (-0.61533 + m.x5)**2 + m.x7
    <= 0)
m.e1337 = Constraint(expr= -(-0.29857 + m.x2)**2 - (-0.71727 + m.x5)**2 + m.x7
    <= 0)
m.e1338 = Constraint(expr= -(-0.22683 + m.x2)**2 - (-0.32213 + m.x5)**2 + m.x7
    <= 0)
m.e1339 = Constraint(expr= -(-0.63577 + m.x2)**2 - (-0.10647 + m.x5)**2 + m.x7
    <= 0)
m.e1340 = Constraint(expr= -(-0.47363 + m.x2)**2 - (-0.95693 + m.x5)**2 + m.x7
    <= 0)
m.e1341 = Constraint(expr= -(-0.28497 + m.x2)**2 - (-0.72767 + m.x5)**2 + m.x7
    <= 0)
m.e1342 = Constraint(expr= -(-0.04843 + m.x2)**2 - (-0.39973 + m.x5)**2 + m.x7
    <= 0)
m.e1343 = Constraint(expr= -(-0.76617 + m.x2)**2 - (-0.30087 + m.x5)**2 + m.x7
    <= 0)
m.e1344 = Constraint(expr= -(-0.83123 + m.x2)**2 - (-0.33053 + m.x5)**2 + m.x7
    <= 0)
m.e1345 = Constraint(expr= -(-0.79937 + m.x2)**2 - (-0.74607 + m.x5)**2 + m.x7
    <= 0)
m.e1346 = Constraint(expr= -(-0.50203 + m.x2)**2 - (-0.22933 + m.x5)**2 + m.x7
    <= 0)
m.e1347 = Constraint(expr= -(-0.30457 + m.x2)**2 - (-0.18327 + m.x5)**2 + m.x7
    <= 0)
m.e1348 = Constraint(expr= -(-0.54083 + m.x2)**2 - (-0.37613 + m.x5)**2 + m.x7
    <= 0)
m.e1349 = Constraint(expr= -(-0.40177 + m.x2)**2 - (-0.93247 + m.x5)**2 + m.x7
    <= 0)
m.e1350 = Constraint(expr= -(-0.22763 + m.x2)**2 - (-0.85093 + m.x5)**2 + m.x7
    <= 0)
m.e1351 = Constraint(expr= -(-0.41097 + m.x2)**2 - (-0.51367 + m.x5)**2 + m.x7
    <= 0)
m.e1352 = Constraint(expr= -(-0.64243 + m.x2)**2 - (-0.53373 + m.x5)**2 + m.x7
    <= 0)
m.e1353 = Constraint(expr= -(-0.85217 + m.x2)**2 - (-0.64687 + m.x5)**2 + m.x7
    <= 0)
m.e1354 = Constraint(expr= -(-0.66523 + m.x2)**2 - (-0.10453 + m.x5)**2 + m.x7
    <= 0)
m.e1355 = Constraint(expr= -(-0.44537 + m.x2)**2 - (-0.25207 + m.x5)**2 + m.x7
    <= 0)
m.e1356 = Constraint(expr= -(-0.97603 + m.x2)**2 - (-0.04333 + m.x5)**2 + m.x7
    <= 0)
m.e1357 = Constraint(expr= -(-0.11057 + m.x2)**2 - (-0.44927 + m.x5)**2 + m.x7
    <= 0)
m.e1358 = Constraint(expr= -(-0.05483 + m.x2)**2 - (-0.63013 + m.x5)**2 + m.x7
    <= 0)
m.e1359 = Constraint(expr= -(-0.96777 + m.x2)**2 - (-0.55847 + m.x5)**2 + m.x7
    <= 0)
m.e1360 = Constraint(expr= -(-0.18163 + m.x2)**2 - (-0.94493 + m.x5)**2 + m.x7
    <= 0)
m.e1361 = Constraint(expr= -(-0.33697 + m.x2)**2 - (-0.09967 + m.x5)**2 + m.x7
    <= 0)
m.e1362 = Constraint(expr= -(-0.43643 + m.x2)**2 - (-0.86773 + m.x5)**2 + m.x7
    <= 0)
m.e1363 = Constraint(expr= -(-0.73817 + m.x2)**2 - (-0.79287 + m.x5)**2 + m.x7
    <= 0)
m.e1364 = Constraint(expr= -(-0.69923 + m.x2)**2 - (-0.07853 + m.x5)**2 + m.x7
    <= 0)
m.e1365 = Constraint(expr= -(-0.89137 + m.x2)**2 - (-0.55807 + m.x5)**2 + m.x7
    <= 0)
m.e1366 = Constraint(expr= -(-0.65003 + m.x2)**2 - (-0.05733 + m.x5)**2 + m.x7
    <= 0)
m.e1367 = Constraint(expr= -(-0.71657 + m.x2)**2 - (-0.51527 + m.x5)**2 + m.x7
    <= 0)
m.e1368 = Constraint(expr= -(-0.76883 + m.x2)**2 - (-0.08413 + m.x5)**2 + m.x7
    <= 0)
m.e1369 = Constraint(expr= -(-0.33377 + m.x2)**2 - (-0.98447 + m.x5)**2 + m.x7
    <= 0)
m.e1370 = Constraint(expr= -(-0.33563 + m.x2)**2 - (-0.23893 + m.x5)**2 + m.x7
    <= 0)
m.e1371 = Constraint(expr= -(-0.06297 + m.x2)**2 - (-0.48567 + m.x5)**2 + m.x7
    <= 0)
m.e1372 = Constraint(expr= -(-0.43043 + m.x2)**2 - (-0.40173 + m.x5)**2 + m.x7
    <= 0)
m.e1373 = Constraint(expr= -(-0.42417 + m.x2)**2 - (-0.73887 + m.x5)**2 + m.x7
    <= 0)
m.e1374 = Constraint(expr= -(-0.93323 + m.x2)**2 - (-0.25253 + m.x5)**2 + m.x7
    <= 0)
m.e1375 = Constraint(expr= -(-0.13737 + m.x2)**2 - (-0.66407 + m.x5)**2 + m.x7
    <= 0)
m.e1376 = Constraint(expr= -(-0.52403 + m.x2)**2 - (-0.27133 + m.x5)**2 + m.x7
    <= 0)
m.e1377 = Constraint(expr= -(-0.12257 + m.x2)**2 - (-0.38127 + m.x5)**2 + m.x7
    <= 0)
m.e1378 = Constraint(expr= -(-0.68283 + m.x2)**2 - (-0.73813 + m.x5)**2 + m.x7
    <= 0)
m.e1379 = Constraint(expr= -(-0.49977 + m.x2)**2 - (-0.21047 + m.x5)**2 + m.x7
    <= 0)
m.e1380 = Constraint(expr= -(-0.68963 + m.x2)**2 - (-0.73293 + m.x5)**2 + m.x7
    <= 0)
m.e1381 = Constraint(expr= -(-0.58897 + m.x2)**2 - (-0.67167 + m.x5)**2 + m.x7
    <= 0)
m.e1382 = Constraint(expr= -(-0.62443 + m.x2)**2 - (-0.13573 + m.x5)**2 + m.x7
    <= 0)
m.e1383 = Constraint(expr= -(-0.91017 + m.x2)**2 - (-0.48487 + m.x5)**2 + m.x7
    <= 0)
m.e1384 = Constraint(expr= -(-0.36723 + m.x2)**2 - (-0.62653 + m.x5)**2 + m.x7
    <= 0)
m.e1385 = Constraint(expr= -(-0.18337 + m.x2)**2 - (-0.57007 + m.x5)**2 + m.x7
    <= 0)
m.e1386 = Constraint(expr= -(-0.59803 + m.x2)**2 - (-0.68533 + m.x5)**2 + m.x7
    <= 0)
m.e1387 = Constraint(expr= -(-0.32857 + m.x2)**2 - (-0.04727 + m.x5)**2 + m.x7
    <= 0)
m.e1388 = Constraint(expr= -(-0.79683 + m.x2)**2 - (-0.59213 + m.x5)**2 + m.x7
    <= 0)
m.e1389 = Constraint(expr= -(-0.46577 + m.x2)**2 - (-0.23647 + m.x5)**2 + m.x7
    <= 0)
m.e1390 = Constraint(expr= -(-0.24363 + m.x2)**2 - (-0.42693 + m.x5)**2 + m.x7
    <= 0)
m.e1391 = Constraint(expr= -(-0.91497 + m.x2)**2 - (-0.65767 + m.x5)**2 + m.x7
    <= 0)
m.e1392 = Constraint(expr= -(-0.01843 + m.x2)**2 - (-0.06973 + m.x5)**2 + m.x7
    <= 0)
m.e1393 = Constraint(expr= -(-0.19617 + m.x2)**2 - (-0.03087 + m.x5)**2 + m.x7
    <= 0)
m.e1394 = Constraint(expr= -(-0.00123 + m.x2)**2 - (-0.20053 + m.x5)**2 + m.x7
    <= 0)
m.e1395 = Constraint(expr= -(-0.02937 + m.x2)**2 - (-0.27607 + m.x5)**2 + m.x7
    <= 0)
m.e1396 = Constraint(expr= -(-0.87203 + m.x2)**2 - (-0.29933 + m.x5)**2 + m.x7
    <= 0)
m.e1397 = Constraint(expr= -(-0.33457 + m.x2)**2 - (-0.51327 + m.x5)**2 + m.x7
    <= 0)
m.e1398 = Constraint(expr= -(-0.11083 + m.x2)**2 - (-0.64613 + m.x5)**2 + m.x7
    <= 0)
m.e1399 = Constraint(expr= -(-0.23177 + m.x2)**2 - (-0.06247 + m.x5)**2 + m.x7
    <= 0)
m.e1400 = Constraint(expr= -(-0.99763 + m.x2)**2 - (-0.32093 + m.x5)**2 + m.x7
    <= 0)
m.e1401 = Constraint(expr= -(-0.04097 + m.x2)**2 - (-0.44367 + m.x5)**2 + m.x7
    <= 0)
m.e1402 = Constraint(expr= -(-0.61243 + m.x2)**2 - (-0.20373 + m.x5)**2 + m.x7
    <= 0)
m.e1403 = Constraint(expr= -(-0.28217 + m.x2)**2 - (-0.37687 + m.x5)**2 + m.x7
    <= 0)
m.e1404 = Constraint(expr= -(-0.83523 + m.x2)**2 - (-0.97453 + m.x5)**2 + m.x7
    <= 0)
m.e1405 = Constraint(expr= -(-0.67537 + m.x2)**2 - (-0.78207 + m.x5)**2 + m.x7
    <= 0)
m.e1406 = Constraint(expr= -(-0.34603 + m.x2)**2 - (-0.11333 + m.x5)**2 + m.x7
    <= 0)
m.e1407 = Constraint(expr= -(-0.14057 + m.x2)**2 - (-0.77927 + m.x5)**2 + m.x7
    <= 0)
m.e1408 = Constraint(expr= -(-0.62483 + m.x2)**2 - (-0.90013 + m.x5)**2 + m.x7
    <= 0)
m.e1409 = Constraint(expr= -(-0.79777 + m.x2)**2 - (-0.68847 + m.x5)**2 + m.x7
    <= 0)
m.e1410 = Constraint(expr= -(-0.95163 + m.x2)**2 - (-0.41493 + m.x5)**2 + m.x7
    <= 0)
m.e1411 = Constraint(expr= -(-0.96697 + m.x2)**2 - (-0.02967 + m.x5)**2 + m.x7
    <= 0)
m.e1412 = Constraint(expr= -(-0.40643 + m.x2)**2 - (-0.53773 + m.x5)**2 + m.x7
    <= 0)
m.e1413 = Constraint(expr= -(-0.16817 + m.x2)**2 - (-0.52287 + m.x5)**2 + m.x7
    <= 0)
m.e1414 = Constraint(expr= -(-0.86923 + m.x2)**2 - (-0.94853 + m.x5)**2 + m.x7
    <= 0)
m.e1415 = Constraint(expr= -(-0.12137 + m.x2)**2 - (-0.08807 + m.x5)**2 + m.x7
    <= 0)
m.e1416 = Constraint(expr= -(-0.02003 + m.x2)**2 - (-0.12733 + m.x5)**2 + m.x7
    <= 0)
m.e1417 = Constraint(expr= -(-0.74657 + m.x2)**2 - (-0.84527 + m.x5)**2 + m.x7
    <= 0)
m.e1418 = Constraint(expr= -(-0.33883 + m.x2)**2 - (-0.35413 + m.x5)**2 + m.x7
    <= 0)
m.e1419 = Constraint(expr= -(-0.16377 + m.x2)**2 - (-0.11447 + m.x5)**2 + m.x7
    <= 0)
m.e1420 = Constraint(expr= -(-0.10563 + m.x2)**2 - (-0.70893 + m.x5)**2 + m.x7
    <= 0)
m.e1421 = Constraint(expr= -(-0.69297 + m.x2)**2 - (-0.41567 + m.x5)**2 + m.x7
    <= 0)
m.e1422 = Constraint(expr= -(-0.40043 + m.x2)**2 - (-0.07173 + m.x5)**2 + m.x7
    <= 0)
m.e1423 = Constraint(expr= -(-0.85417 + m.x2)**2 - (-0.46887 + m.x5)**2 + m.x7
    <= 0)
m.e1424 = Constraint(expr= -(-0.10323 + m.x2)**2 - (-0.12253 + m.x5)**2 + m.x7
    <= 0)
m.e1425 = Constraint(expr= -(-0.36737 + m.x2)**2 - (-0.19407 + m.x5)**2 + m.x7
    <= 0)
m.e1426 = Constraint(expr= -(-0.89403 + m.x2)**2 - (-0.34133 + m.x5)**2 + m.x7
    <= 0)
m.e1427 = Constraint(expr= -(-0.15257 + m.x2)**2 - (-0.71127 + m.x5)**2 + m.x7
    <= 0)
m.e1428 = Constraint(expr= -(-0.25283 + m.x2)**2 - (-0.00813 + m.x5)**2 + m.x7
    <= 0)
m.e1429 = Constraint(expr= -(-0.32977 + m.x2)**2 - (-0.34047 + m.x5)**2 + m.x7
    <= 0)
m.e1430 = Constraint(expr= -(-0.45963 + m.x2)**2 - (-0.20293 + m.x5)**2 + m.x7
    <= 0)
m.e1431 = Constraint(expr= -(-0.21897 + m.x2)**2 - (-0.60167 + m.x5)**2 + m.x7
    <= 0)
m.e1432 = Constraint(expr= -(-0.59443 + m.x2)**2 - (-0.80573 + m.x5)**2 + m.x7
    <= 0)
m.e1433 = Constraint(expr= -(-0.34017 + m.x2)**2 - (-0.21487 + m.x5)**2 + m.x7
    <= 0)
m.e1434 = Constraint(expr= -(-0.53723 + m.x2)**2 - (-0.49653 + m.x5)**2 + m.x7
    <= 0)
m.e1435 = Constraint(expr= -(-0.41337 + m.x2)**2 - (-0.10007 + m.x5)**2 + m.x7
    <= 0)
m.e1436 = Constraint(expr= -(-0.96803 + m.x2)**2 - (-0.75533 + m.x5)**2 + m.x7
    <= 0)
m.e1437 = Constraint(expr= -(-0.35857 + m.x2)**2 - (-0.37727 + m.x5)**2 + m.x7
    <= 0)
m.e1438 = Constraint(expr= -(-0.36683 + m.x2)**2 - (-0.86213 + m.x5)**2 + m.x7
    <= 0)
m.e1439 = Constraint(expr= -(-0.29577 + m.x2)**2 - (-0.36647 + m.x5)**2 + m.x7
    <= 0)
m.e1440 = Constraint(expr= -(-0.01363 + m.x2)**2 - (-0.89693 + m.x5)**2 + m.x7
    <= 0)
m.e1441 = Constraint(expr= -(-0.54497 + m.x2)**2 - (-0.58767 + m.x5)**2 + m.x7
    <= 0)
m.e1442 = Constraint(expr= -(-0.98843 + m.x2)**2 - (-0.73973 + m.x5)**2 + m.x7
    <= 0)
m.e1443 = Constraint(expr= -(-0.62617 + m.x2)**2 - (-0.76087 + m.x5)**2 + m.x7
    <= 0)
m.e1444 = Constraint(expr= -(-0.17123 + m.x2)**2 - (-0.07053 + m.x5)**2 + m.x7
    <= 0)
m.e1445 = Constraint(expr= -(-0.25937 + m.x2)**2 - (-0.80607 + m.x5)**2 + m.x7
    <= 0)
m.e1446 = Constraint(expr= -(-0.24203 + m.x2)**2 - (-0.36933 + m.x5)**2 + m.x7
    <= 0)
m.e1447 = Constraint(expr= -(-0.36457 + m.x2)**2 - (-0.84327 + m.x5)**2 + m.x7
    <= 0)
m.e1448 = Constraint(expr= -(-0.68083 + m.x2)**2 - (-0.91613 + m.x5)**2 + m.x7
    <= 0)
m.e1449 = Constraint(expr= -(-0.06177 + m.x2)**2 - (-0.19247 + m.x5)**2 + m.x7
    <= 0)
m.e1450 = Constraint(expr= -(-0.76763 + m.x2)**2 - (-0.79093 + m.x5)**2 + m.x7
    <= 0)
m.e1451 = Constraint(expr= -(-0.67097 + m.x2)**2 - (-0.37367 + m.x5)**2 + m.x7
    <= 0)
m.e1452 = Constraint(expr= -(-0.58243 + m.x2)**2 - (-0.87373 + m.x5)**2 + m.x7
    <= 0)
m.e1453 = Constraint(expr= -(-0.71217 + m.x2)**2 - (-0.10687 + m.x5)**2 + m.x7
    <= 0)
m.e1454 = Constraint(expr= -(-0.00523 + m.x2)**2 - (-0.84453 + m.x5)**2 + m.x7
    <= 0)
m.e1455 = Constraint(expr= -(-0.90537 + m.x2)**2 - (-0.31207 + m.x5)**2 + m.x7
    <= 0)
m.e1456 = Constraint(expr= -(-0.71603 + m.x2)**2 - (-0.18333 + m.x5)**2 + m.x7
    <= 0)
m.e1457 = Constraint(expr= -(-0.17057 + m.x2)**2 - (-0.10927 + m.x5)**2 + m.x7
    <= 0)
m.e1458 = Constraint(expr= -(-0.19483 + m.x2)**2 - (-0.17013 + m.x5)**2 + m.x7
    <= 0)
m.e1459 = Constraint(expr= -(-0.62777 + m.x2)**2 - (-0.81847 + m.x5)**2 + m.x7
    <= 0)
m.e1460 = Constraint(expr= -(-0.72163 + m.x2)**2 - (-0.88493 + m.x5)**2 + m.x7
    <= 0)
m.e1461 = Constraint(expr= -(-0.59697 + m.x2)**2 - (-0.95967 + m.x5)**2 + m.x7
    <= 0)
m.e1462 = Constraint(expr= -(-0.37643 + m.x2)**2 - (-0.20773 + m.x5)**2 + m.x7
    <= 0)
m.e1463 = Constraint(expr= -(-0.59817 + m.x2)**2 - (-0.25287 + m.x5)**2 + m.x7
    <= 0)
m.e1464 = Constraint(expr= -(-0.03923 + m.x2)**2 - (-0.81853 + m.x5)**2 + m.x7
    <= 0)
m.e1465 = Constraint(expr= -(-0.35137 + m.x2)**2 - (-0.61807 + m.x5)**2 + m.x7
    <= 0)
m.e1466 = Constraint(expr= -(-0.39003 + m.x2)**2 - (-0.19733 + m.x5)**2 + m.x7
    <= 0)
m.e1467 = Constraint(expr= -(-0.77657 + m.x2)**2 - (-0.17527 + m.x5)**2 + m.x7
    <= 0)
m.e1468 = Constraint(expr= -(-0.90883 + m.x2)**2 - (-0.62413 + m.x5)**2 + m.x7
    <= 0)
m.e1469 = Constraint(expr= -(-0.99377 + m.x2)**2 - (-0.24447 + m.x5)**2 + m.x7
    <= 0)
m.e1470 = Constraint(expr= -(-0.87563 + m.x2)**2 - (-0.17893 + m.x5)**2 + m.x7
    <= 0)
m.e1471 = Constraint(expr= -(-0.32297 + m.x2)**2 - (-0.34567 + m.x5)**2 + m.x7
    <= 0)
m.e1472 = Constraint(expr= -(-0.37043 + m.x2)**2 - (-0.74173 + m.x5)**2 + m.x7
    <= 0)
m.e1473 = Constraint(expr= -(-0.28417 + m.x2)**2 - (-0.19887 + m.x5)**2 + m.x7
    <= 0)
m.e1474 = Constraint(expr= -(-0.27323 + m.x2)**2 - (-0.99253 + m.x5)**2 + m.x7
    <= 0)
m.e1475 = Constraint(expr= -(-0.59737 + m.x2)**2 - (-0.72407 + m.x5)**2 + m.x7
    <= 0)
m.e1476 = Constraint(expr= -(-0.26403 + m.x2)**2 - (-0.41133 + m.x5)**2 + m.x7
    <= 0)
m.e1477 = Constraint(expr= -(-0.18257 + m.x2)**2 - (-0.04127 + m.x5)**2 + m.x7
    <= 0)
m.e1478 = Constraint(expr= -(-0.82283 + m.x2)**2 - (-0.27813 + m.x5)**2 + m.x7
    <= 0)
m.e1479 = Constraint(expr= -(-0.15977 + m.x2)**2 - (-0.47047 + m.x5)**2 + m.x7
    <= 0)
m.e1480 = Constraint(expr= -(-0.22963 + m.x2)**2 - (-0.67293 + m.x5)**2 + m.x7
    <= 0)
m.e1481 = Constraint(expr= -(-0.84897 + m.x2)**2 - (-0.53167 + m.x5)**2 + m.x7
    <= 0)
m.e1482 = Constraint(expr= -(-0.56443 + m.x2)**2 - (-0.47573 + m.x5)**2 + m.x7
    <= 0)
m.e1483 = Constraint(expr= -(-0.77017 + m.x2)**2 - (-0.94487 + m.x5)**2 + m.x7
    <= 0)
m.e1484 = Constraint(expr= -(-0.70723 + m.x2)**2 - (-0.36653 + m.x5)**2 + m.x7
    <= 0)
m.e1485 = Constraint(expr= -(-0.64337 + m.x2)**2 - (-0.63007 + m.x5)**2 + m.x7
    <= 0)
m.e1486 = Constraint(expr= -(-0.33803 + m.x2)**2 - (-0.82533 + m.x5)**2 + m.x7
    <= 0)
m.e1487 = Constraint(expr= -(-0.38857 + m.x2)**2 - (-0.70727 + m.x5)**2 + m.x7
    <= 0)
m.e1488 = Constraint(expr= -(-0.93683 + m.x2)**2 - (-0.13213 + m.x5)**2 + m.x7
    <= 0)
m.e1489 = Constraint(expr= -(-0.12577 + m.x2)**2 - (-0.49647 + m.x5)**2 + m.x7
    <= 0)
m.e1490 = Constraint(expr= -(-0.78363 + m.x2)**2 - (-0.36693 + m.x5)**2 + m.x7
    <= 0)
m.e1491 = Constraint(expr= -(-0.17497 + m.x2)**2 - (-0.51767 + m.x5)**2 + m.x7
    <= 0)
m.e1492 = Constraint(expr= -(-0.95843 + m.x2)**2 - (-0.40973 + m.x5)**2 + m.x7
    <= 0)
m.e1493 = Constraint(expr= -(-0.05617 + m.x2)**2 - (-0.49087 + m.x5)**2 + m.x7
    <= 0)
m.e1494 = Constraint(expr= -(-0.34123 + m.x2)**2 - (-0.94053 + m.x5)**2 + m.x7
    <= 0)
m.e1495 = Constraint(expr= -(-0.48937 + m.x2)**2 - (-0.33607 + m.x5)**2 + m.x7
    <= 0)
m.e1496 = Constraint(expr= -(-0.61203 + m.x2)**2 - (-0.43933 + m.x5)**2 + m.x7
    <= 0)
m.e1497 = Constraint(expr= -(-0.39457 + m.x2)**2 - (-0.17327 + m.x5)**2 + m.x7
    <= 0)
m.e1498 = Constraint(expr= -(-0.25083 + m.x2)**2 - (-0.18613 + m.x5)**2 + m.x7
    <= 0)
m.e1499 = Constraint(expr= -(-0.89177 + m.x2)**2 - (-0.32247 + m.x5)**2 + m.x7
    <= 0)
m.e1500 = Constraint(expr= -(-0.53763 + m.x2)**2 - (-0.26093 + m.x5)**2 + m.x7
    <= 0)
m.e1501 = Constraint(expr= -(-0.30097 + m.x2)**2 - (-0.30367 + m.x5)**2 + m.x7
    <= 0)
m.e1502 = Constraint(expr= -(-0.55243 + m.x2)**2 - (-0.54373 + m.x5)**2 + m.x7
    <= 0)
m.e1503 = Constraint(expr= -(-0.14217 + m.x2)**2 - (-0.83687 + m.x5)**2 + m.x7
    <= 0)
m.e1504 = Constraint(expr= -(-0.17523 + m.x2)**2 - (-0.71453 + m.x5)**2 + m.x7
    <= 0)
m.e1505 = Constraint(expr= -(-0.13537 + m.x2)**2 - (-0.84207 + m.x5)**2 + m.x7
    <= 0)
m.e1506 = Constraint(expr= -(-0.08603 + m.x2)**2 - (-0.25333 + m.x5)**2 + m.x7
    <= 0)
m.e1507 = Constraint(expr= -(-0.20057 + m.x2)**2 - (-0.43927 + m.x5)**2 + m.x7
    <= 0)
m.e1508 = Constraint(expr= -(-0.76483 + m.x2)**2 - (-0.44013 + m.x5)**2 + m.x7
    <= 0)
m.e1509 = Constraint(expr= -(-0.45777 + m.x2)**2 - (-0.94847 + m.x5)**2 + m.x7
    <= 0)
m.e1510 = Constraint(expr= -(-0.49163 + m.x2)**2 - (-0.35493 + m.x5)**2 + m.x7
    <= 0)
m.e1511 = Constraint(expr= -(-0.22697 + m.x2)**2 - (-0.88967 + m.x5)**2 + m.x7
    <= 0)
m.e1512 = Constraint(expr= -(-0.34643 + m.x2)**2 - (-0.87773 + m.x5)**2 + m.x7
    <= 0)
m.e1513 = Constraint(expr= -(-0.02817 + m.x2)**2 - (-0.98287 + m.x5)**2 + m.x7
    <= 0)
m.e1514 = Constraint(expr= -(-0.20923 + m.x2)**2 - (-0.68853 + m.x5)**2 + m.x7
    <= 0)
m.e1515 = Constraint(expr= -(-0.58137 + m.x2)**2 - (-0.14807 + m.x5)**2 + m.x7
    <= 0)
m.e1516 = Constraint(expr= -(-0.76003 + m.x2)**2 - (-0.26733 + m.x5)**2 + m.x7
    <= 0)
m.e1517 = Constraint(expr= -(-0.80657 + m.x2)**2 - (-0.50527 + m.x5)**2 + m.x7
    <= 0)
m.e1518 = Constraint(expr= -(-0.47883 + m.x2)**2 - (-0.89413 + m.x5)**2 + m.x7
    <= 0)
m.e1519 = Constraint(expr= -(-0.82377 + m.x2)**2 - (-0.37447 + m.x5)**2 + m.x7
    <= 0)
m.e1520 = Constraint(expr= -(-0.64563 + m.x2)**2 - (-0.64893 + m.x5)**2 + m.x7
    <= 0)
m.e1521 = Constraint(expr= -(-0.95297 + m.x2)**2 - (-0.27567 + m.x5)**2 + m.x7
    <= 0)
m.e1522 = Constraint(expr= -(-0.34043 + m.x2)**2 - (-0.41173 + m.x5)**2 + m.x7
    <= 0)
m.e1523 = Constraint(expr= -(-0.71417 + m.x2)**2 - (-0.92887 + m.x5)**2 + m.x7
    <= 0)
m.e1524 = Constraint(expr= -(-0.44323 + m.x2)**2 - (-0.86253 + m.x5)**2 + m.x7
    <= 0)
m.e1525 = Constraint(expr= -(-0.82737 + m.x2)**2 - (-0.25407 + m.x5)**2 + m.x7
    <= 0)
m.e1526 = Constraint(expr= -(-0.63403 + m.x2)**2 - (-0.48133 + m.x5)**2 + m.x7
    <= 0)
m.e1527 = Constraint(expr= -(-0.21257 + m.x2)**2 - (-0.37127 + m.x5)**2 + m.x7
    <= 0)
m.e1528 = Constraint(expr= -(-0.39283 + m.x2)**2 - (-0.54813 + m.x5)**2 + m.x7
    <= 0)
m.e1529 = Constraint(expr= -(-0.98977 + m.x2)**2 - (-0.60047 + m.x5)**2 + m.x7
    <= 0)
m.e1530 = Constraint(expr= -(-0.99963 + m.x2)**2 - (-0.14293 + m.x5)**2 + m.x7
    <= 0)
m.e1531 = Constraint(expr= -(-0.47897 + m.x2)**2 - (-0.46167 + m.x5)**2 + m.x7
    <= 0)
m.e1532 = Constraint(expr= -(-0.53443 + m.x2)**2 - (-0.14573 + m.x5)**2 + m.x7
    <= 0)
m.e1533 = Constraint(expr= -(-0.20017 + m.x2)**2 - (-0.67487 + m.x5)**2 + m.x7
    <= 0)
m.e1534 = Constraint(expr= -(-0.87723 + m.x2)**2 - (-0.23653 + m.x5)**2 + m.x7
    <= 0)
m.e1535 = Constraint(expr= -(-0.87337 + m.x2)**2 - (-0.16007 + m.x5)**2 + m.x7
    <= 0)
m.e1536 = Constraint(expr= -(-0.70803 + m.x2)**2 - (-0.89533 + m.x5)**2 + m.x7
    <= 0)
m.e1537 = Constraint(expr= -(-0.41857 + m.x2)**2 - (-0.03727 + m.x5)**2 + m.x7
    <= 0)
m.e1538 = Constraint(expr= -(-0.50683 + m.x2)**2 - (-0.40213 + m.x5)**2 + m.x7
    <= 0)
m.e1539 = Constraint(expr= -(-0.95577 + m.x2)**2 - (-0.62647 + m.x5)**2 + m.x7
    <= 0)
m.e1540 = Constraint(expr= -(-0.55363 + m.x2)**2 - (-0.83693 + m.x5)**2 + m.x7
    <= 0)
m.e1541 = Constraint(expr= -(-0.80497 + m.x2)**2 - (-0.44767 + m.x5)**2 + m.x7
    <= 0)
m.e1542 = Constraint(expr= -(-0.92843 + m.x2)**2 - (-0.07973 + m.x5)**2 + m.x7
    <= 0)
m.e1543 = Constraint(expr= -(-0.48617 + m.x2)**2 - (-0.22087 + m.x5)**2 + m.x7
    <= 0)
m.e1544 = Constraint(expr= -(-0.51123 + m.x2)**2 - (-0.81053 + m.x5)**2 + m.x7
    <= 0)
m.e1545 = Constraint(expr= -(-0.71937 + m.x2)**2 - (-0.86607 + m.x5)**2 + m.x7
    <= 0)
m.e1546 = Constraint(expr= -(-0.98203 + m.x2)**2 - (-0.50933 + m.x5)**2 + m.x7
    <= 0)
m.e1547 = Constraint(expr= -(-0.42457 + m.x2)**2 - (-0.50327 + m.x5)**2 + m.x7
    <= 0)
m.e1548 = Constraint(expr= -(-0.82083 + m.x2)**2 - (-0.45613 + m.x5)**2 + m.x7
    <= 0)
m.e1549 = Constraint(expr= -(-0.72177 + m.x2)**2 - (-0.45247 + m.x5)**2 + m.x7
    <= 0)
m.e1550 = Constraint(expr= -(-0.30763 + m.x2)**2 - (-0.73093 + m.x5)**2 + m.x7
    <= 0)
m.e1551 = Constraint(expr= -(-0.93097 + m.x2)**2 - (-0.23367 + m.x5)**2 + m.x7
    <= 0)
m.e1552 = Constraint(expr= -(-0.52243 + m.x2)**2 - (-0.21373 + m.x5)**2 + m.x7
    <= 0)
m.e1553 = Constraint(expr= -(-0.57217 + m.x2)**2 - (-0.56687 + m.x5)**2 + m.x7
    <= 0)
m.e1554 = Constraint(expr= -(-0.34523 + m.x2)**2 - (-0.58453 + m.x5)**2 + m.x7
    <= 0)
m.e1555 = Constraint(expr= -(-0.36537 + m.x2)**2 - (-0.37207 + m.x5)**2 + m.x7
    <= 0)
m.e1556 = Constraint(expr= -(-0.45603 + m.x2)**2 - (-0.32333 + m.x5)**2 + m.x7
    <= 0)
m.e1557 = Constraint(expr= -(-0.23057 + m.x2)**2 - (-0.76927 + m.x5)**2 + m.x7
    <= 0)
m.e1558 = Constraint(expr= -(-0.33483 + m.x2)**2 - (-0.71013 + m.x5)**2 + m.x7
    <= 0)
m.e1559 = Constraint(expr= -(-0.28777 + m.x2)**2 - (-0.07847 + m.x5)**2 + m.x7
    <= 0)
m.e1560 = Constraint(expr= -(-0.26163 + m.x2)**2 - (-0.82493 + m.x5)**2 + m.x7
    <= 0)
m.e1561 = Constraint(expr= -(-0.85697 + m.x2)**2 - (-0.81967 + m.x5)**2 + m.x7
    <= 0)
m.e1562 = Constraint(expr= -(-0.31643 + m.x2)**2 - (-0.54773 + m.x5)**2 + m.x7
    <= 0)
m.e1563 = Constraint(expr= -(-0.45817 + m.x2)**2 - (-0.71287 + m.x5)**2 + m.x7
    <= 0)
m.e1564 = Constraint(expr= -(-0.37923 + m.x2)**2 - (-0.55853 + m.x5)**2 + m.x7
    <= 0)
m.e1565 = Constraint(expr= -(-0.81137 + m.x2)**2 - (-0.67807 + m.x5)**2 + m.x7
    <= 0)
m.e1566 = Constraint(expr= -(-0.13003 + m.x2)**2 - (-0.33733 + m.x5)**2 + m.x7
    <= 0)
m.e1567 = Constraint(expr= -(-0.83657 + m.x2)**2 - (-0.83527 + m.x5)**2 + m.x7
    <= 0)
m.e1568 = Constraint(expr= -(-0.04883 + m.x2)**2 - (-0.16413 + m.x5)**2 + m.x7
    <= 0)
m.e1569 = Constraint(expr= -(-0.65377 + m.x2)**2 - (-0.50447 + m.x5)**2 + m.x7
    <= 0)
m.e1570 = Constraint(expr= -(-0.41563 + m.x2)**2 - (-0.11893 + m.x5)**2 + m.x7
    <= 0)
m.e1571 = Constraint(expr= -(-0.58297 + m.x2)**2 - (-0.20567 + m.x5)**2 + m.x7
    <= 0)
m.e1572 = Constraint(expr= -(-0.31043 + m.x2)**2 - (-0.08173 + m.x5)**2 + m.x7
    <= 0)
m.e1573 = Constraint(expr= -(-0.14417 + m.x2)**2 - (-0.65887 + m.x5)**2 + m.x7
    <= 0)
m.e1574 = Constraint(expr= -(-0.61323 + m.x2)**2 - (-0.73253 + m.x5)**2 + m.x7
    <= 0)
m.e1575 = Constraint(expr= -(-0.05737 + m.x2)**2 - (-0.78407 + m.x5)**2 + m.x7
    <= 0)
m.e1576 = Constraint(expr= -(-0.00403 + m.x2)**2 - (-0.55133 + m.x5)**2 + m.x7
    <= 0)
m.e1577 = Constraint(expr= -(-0.24257 + m.x2)**2 - (-0.70127 + m.x5)**2 + m.x7
    <= 0)
m.e1578 = Constraint(expr= -(-0.96283 + m.x2)**2 - (-0.81813 + m.x5)**2 + m.x7
    <= 0)
m.e1579 = Constraint(expr= -(-0.81977 + m.x2)**2 - (-0.73047 + m.x5)**2 + m.x7
    <= 0)
m.e1580 = Constraint(expr= -(-0.76963 + m.x2)**2 - (-0.61293 + m.x5)**2 + m.x7
    <= 0)
m.e1581 = Constraint(expr= -(-0.10897 + m.x2)**2 - (-0.39167 + m.x5)**2 + m.x7
    <= 0)
m.e1582 = Constraint(expr= -(-0.50443 + m.x2)**2 - (-0.81573 + m.x5)**2 + m.x7
    <= 0)
m.e1583 = Constraint(expr= -(-0.63017 + m.x2)**2 - (-0.40487 + m.x5)**2 + m.x7
    <= 0)
m.e1584 = Constraint(expr= -(-0.04723 + m.x2)**2 - (-0.10653 + m.x5)**2 + m.x7
    <= 0)
m.e1585 = Constraint(expr= -(-0.10337 + m.x2)**2 - (-0.69007 + m.x5)**2 + m.x7
    <= 0)
m.e1586 = Constraint(expr= -(-0.07803 + m.x2)**2 - (-0.96533 + m.x5)**2 + m.x7
    <= 0)
m.e1587 = Constraint(expr= -(-0.44857 + m.x2)**2 - (-0.36727 + m.x5)**2 + m.x7
    <= 0)
m.e1588 = Constraint(expr= -(-0.07683 + m.x2)**2 - (-0.67213 + m.x5)**2 + m.x7
    <= 0)
m.e1589 = Constraint(expr= -(-0.78577 + m.x2)**2 - (-0.75647 + m.x5)**2 + m.x7
    <= 0)
m.e1590 = Constraint(expr= -(-0.32363 + m.x2)**2 - (-0.30693 + m.x5)**2 + m.x7
    <= 0)
m.e1591 = Constraint(expr= -(-0.43497 + m.x2)**2 - (-0.37767 + m.x5)**2 + m.x7
    <= 0)
m.e1592 = Constraint(expr= -(-0.89843 + m.x2)**2 - (-0.74973 + m.x5)**2 + m.x7
    <= 0)
m.e1593 = Constraint(expr= -(-0.91617 + m.x2)**2 - (-0.95087 + m.x5)**2 + m.x7
    <= 0)
m.e1594 = Constraint(expr= -(-0.68123 + m.x2)**2 - (-0.68053 + m.x5)**2 + m.x7
    <= 0)
m.e1595 = Constraint(expr= -(-0.94937 + m.x2)**2 - (-0.39607 + m.x5)**2 + m.x7
    <= 0)
m.e1596 = Constraint(expr= -(-0.35203 + m.x2)**2 - (-0.57933 + m.x5)**2 + m.x7
    <= 0)
m.e1597 = Constraint(expr= -(-0.45457 + m.x2)**2 - (-0.83327 + m.x5)**2 + m.x7
    <= 0)
m.e1598 = Constraint(expr= -(-0.39083 + m.x2)**2 - (-0.72613 + m.x5)**2 + m.x7
    <= 0)
m.e1599 = Constraint(expr= -(-0.55177 + m.x2)**2 - (-0.58247 + m.x5)**2 + m.x7
    <= 0)
m.e1600 = Constraint(expr= -(-0.07763 + m.x2)**2 - (-0.20093 + m.x5)**2 + m.x7
    <= 0)
m.e1601 = Constraint(expr= -(-0.56097 + m.x2)**2 - (-0.16367 + m.x5)**2 + m.x7
    <= 0)
m.e1602 = Constraint(expr= -(-0.49243 + m.x2)**2 - (-0.88373 + m.x5)**2 + m.x7
    <= 0)
m.e1603 = Constraint(expr= -(-0.00217 + m.x2)**2 - (-0.29687 + m.x5)**2 + m.x7
    <= 0)
m.e1604 = Constraint(expr= -(-0.51523 + m.x2)**2 - (-0.45453 + m.x5)**2 + m.x7
    <= 0)
m.e1605 = Constraint(expr= -(-0.59537 + m.x2)**2 - (-0.90207 + m.x5)**2 + m.x7
    <= 0)
m.e1606 = Constraint(expr= -(-0.82603 + m.x2)**2 - (-0.39333 + m.x5)**2 + m.x7
    <= 0)
m.e1607 = Constraint(expr= -(-0.26057 + m.x2)**2 - (-0.09927 + m.x5)**2 + m.x7
    <= 0)
m.e1608 = Constraint(expr= -(-0.90483 + m.x2)**2 - (-0.98013 + m.x5)**2 + m.x7
    <= 0)
m.e1609 = Constraint(expr= -(-0.11777 + m.x2)**2 - (-0.20847 + m.x5)**2 + m.x7
    <= 0)
m.e1610 = Constraint(expr= -(-0.03163 + m.x2)**2 - (-0.29493 + m.x5)**2 + m.x7
    <= 0)
m.e1611 = Constraint(expr= -(-0.48697 + m.x2)**2 - (-0.74967 + m.x5)**2 + m.x7
    <= 0)
m.e1612 = Constraint(expr= -(-0.28643 + m.x2)**2 - (-0.21773 + m.x5)**2 + m.x7
    <= 0)
m.e1613 = Constraint(expr= -(-0.88817 + m.x2)**2 - (-0.44287 + m.x5)**2 + m.x7
    <= 0)
m.e1614 = Constraint(expr= -(-0.54923 + m.x2)**2 - (-0.42853 + m.x5)**2 + m.x7
    <= 0)
m.e1615 = Constraint(expr= -(-0.04137 + m.x2)**2 - (-0.20807 + m.x5)**2 + m.x7
    <= 0)
m.e1616 = Constraint(expr= -(-0.50003 + m.x2)**2 - (-0.40733 + m.x5)**2 + m.x7
    <= 0)
m.e1617 = Constraint(expr= -(-0.86657 + m.x2)**2 - (-0.16527 + m.x5)**2 + m.x7
    <= 0)
m.e1618 = Constraint(expr= -(-0.61883 + m.x2)**2 - (-0.43413 + m.x5)**2 + m.x7
    <= 0)
m.e1619 = Constraint(expr= -(-0.48377 + m.x2)**2 - (-0.63447 + m.x5)**2 + m.x7
    <= 0)
m.e1620 = Constraint(expr= -(-0.18563 + m.x2)**2 - (-0.58893 + m.x5)**2 + m.x7
    <= 0)
m.e1621 = Constraint(expr= -(-0.21297 + m.x2)**2 - (-0.13567 + m.x5)**2 + m.x7
    <= 0)
m.e1622 = Constraint(expr= -(-0.28043 + m.x2)**2 - (-0.75173 + m.x5)**2 + m.x7
    <= 0)
m.e1623 = Constraint(expr= -(-0.57417 + m.x2)**2 - (-0.38887 + m.x5)**2 + m.x7
    <= 0)
m.e1624 = Constraint(expr= -(-0.78323 + m.x2)**2 - (-0.60253 + m.x5)**2 + m.x7
    <= 0)
m.e1625 = Constraint(expr= -(-0.28737 + m.x2)**2 - (-0.31407 + m.x5)**2 + m.x7
    <= 0)
m.e1626 = Constraint(expr= -(-0.37403 + m.x2)**2 - (-0.62133 + m.x5)**2 + m.x7
    <= 0)
m.e1627 = Constraint(expr= -(-0.27257 + m.x2)**2 - (-0.03127 + m.x5)**2 + m.x7
    <= 0)
m.e1628 = Constraint(expr= -(-0.53283 + m.x2)**2 - (-0.08813 + m.x5)**2 + m.x7
    <= 0)
m.e1629 = Constraint(expr= -(-0.64977 + m.x2)**2 - (-0.86047 + m.x5)**2 + m.x7
    <= 0)
m.e1630 = Constraint(expr= -(-0.53963 + m.x2)**2 - (-0.08293 + m.x5)**2 + m.x7
    <= 0)
m.e1631 = Constraint(expr= -(-0.73897 + m.x2)**2 - (-0.32167 + m.x5)**2 + m.x7
    <= 0)
m.e1632 = Constraint(expr= -(-0.47443 + m.x2)**2 - (-0.48573 + m.x5)**2 + m.x7
    <= 0)
m.e1633 = Constraint(expr= -(-0.06017 + m.x2)**2 - (-0.13487 + m.x5)**2 + m.x7
    <= 0)
m.e1634 = Constraint(expr= -(-0.21723 + m.x2)**2 - (-0.97653 + m.x5)**2 + m.x7
    <= 0)
m.e1635 = Constraint(expr= -(-0.33337 + m.x2)**2 - (-0.22007 + m.x5)**2 + m.x7
    <= 0)
m.e1636 = Constraint(expr= -(-0.44803 + m.x2)**2 - (-0.03533 + m.x5)**2 + m.x7
    <= 0)
m.e1637 = Constraint(expr= -(-0.47857 + m.x2)**2 - (-0.69727 + m.x5)**2 + m.x7
    <= 0)
m.e1638 = Constraint(expr= -(-0.64683 + m.x2)**2 - (-0.94213 + m.x5)**2 + m.x7
    <= 0)
m.e1639 = Constraint(expr= -(-0.61577 + m.x2)**2 - (-0.88647 + m.x5)**2 + m.x7
    <= 0)
m.e1640 = Constraint(expr= -(-0.09363 + m.x2)**2 - (-0.77693 + m.x5)**2 + m.x7
    <= 0)
m.e1641 = Constraint(expr= -(-0.06497 + m.x2)**2 - (-0.30767 + m.x5)**2 + m.x7
    <= 0)
m.e1642 = Constraint(expr= -(-0.86843 + m.x2)**2 - (-0.41973 + m.x5)**2 + m.x7
    <= 0)
m.e1643 = Constraint(expr= -(-0.34617 + m.x2)**2 - (-0.68087 + m.x5)**2 + m.x7
    <= 0)
m.e1644 = Constraint(expr= -(-0.85123 + m.x2)**2 - (-0.55053 + m.x5)**2 + m.x7
    <= 0)
m.e1645 = Constraint(expr= -(-0.17937 + m.x2)**2 - (-0.92607 + m.x5)**2 + m.x7
    <= 0)
m.e1646 = Constraint(expr= -(-0.72203 + m.x2)**2 - (-0.64933 + m.x5)**2 + m.x7
    <= 0)
m.e1647 = Constraint(expr= -(-0.48457 + m.x2)**2 - (-0.16327 + m.x5)**2 + m.x7
    <= 0)
m.e1648 = Constraint(expr= -(-0.96083 + m.x2)**2 - (-0.99613 + m.x5)**2 + m.x7
    <= 0)
m.e1649 = Constraint(expr= -(-0.38177 + m.x2)**2 - (-0.71247 + m.x5)**2 + m.x7
    <= 0)
m.e1650 = Constraint(expr= -(-0.84763 + m.x2)**2 - (-0.67093 + m.x5)**2 + m.x7
    <= 0)
m.e1651 = Constraint(expr= -(-0.19097 + m.x2)**2 - (-0.09367 + m.x5)**2 + m.x7
    <= 0)
m.e1652 = Constraint(expr= -(-0.46243 + m.x2)**2 - (-0.55373 + m.x5)**2 + m.x7
    <= 0)
m.e1653 = Constraint(expr= -(-0.43217 + m.x2)**2 - (-0.02687 + m.x5)**2 + m.x7
    <= 0)
m.e1654 = Constraint(expr= -(-0.68523 + m.x2)**2 - (-0.32453 + m.x5)**2 + m.x7
    <= 0)
m.e1655 = Constraint(expr= -(-0.82537 + m.x2)**2 - (-0.43207 + m.x5)**2 + m.x7
    <= 0)
m.e1656 = Constraint(expr= -(-0.19603 + m.x2)**2 - (-0.46333 + m.x5)**2 + m.x7
    <= 0)
m.e1657 = Constraint(expr= -(-0.29057 + m.x2)**2 - (-0.42927 + m.x5)**2 + m.x7
    <= 0)
m.e1658 = Constraint(expr= -(-0.47483 + m.x2)**2 - (-0.25013 + m.x5)**2 + m.x7
    <= 0)
m.e1659 = Constraint(expr= -(-0.94777 + m.x2)**2 - (-0.33847 + m.x5)**2 + m.x7
    <= 0)
m.e1660 = Constraint(expr= -(-0.80163 + m.x2)**2 - (-0.76493 + m.x5)**2 + m.x7
    <= 0)
m.e1661 = Constraint(expr= -(-0.11697 + m.x2)**2 - (-0.67967 + m.x5)**2 + m.x7
    <= 0)
m.e1662 = Constraint(expr= -(-0.25643 + m.x2)**2 - (-0.88773 + m.x5)**2 + m.x7
    <= 0)
m.e1663 = Constraint(expr= -(-0.31817 + m.x2)**2 - (-0.17287 + m.x5)**2 + m.x7
    <= 0)
m.e1664 = Constraint(expr= -(-0.71923 + m.x2)**2 - (-0.29853 + m.x5)**2 + m.x7
    <= 0)
m.e1665 = Constraint(expr= -(-0.27137 + m.x2)**2 - (-0.73807 + m.x5)**2 + m.x7
    <= 0)
m.e1666 = Constraint(expr= -(-0.87003 + m.x2)**2 - (-0.47733 + m.x5)**2 + m.x7
    <= 0)
m.e1667 = Constraint(expr= -(-0.89657 + m.x2)**2 - (-0.49527 + m.x5)**2 + m.x7
    <= 0)
m.e1668 = Constraint(expr= -(-0.18883 + m.x2)**2 - (-0.70413 + m.x5)**2 + m.x7
    <= 0)
m.e1669 = Constraint(expr= -(-0.31377 + m.x2)**2 - (-0.76447 + m.x5)**2 + m.x7
    <= 0)
m.e1670 = Constraint(expr= -(-0.95563 + m.x2)**2 - (-0.05893 + m.x5)**2 + m.x7
    <= 0)
m.e1671 = Constraint(expr= -(-0.84297 + m.x2)**2 - (-0.06567 + m.x5)**2 + m.x7
    <= 0)
m.e1672 = Constraint(expr= -(-0.25043 + m.x2)**2 - (-0.42173 + m.x5)**2 + m.x7
    <= 0)
m.e1673 = Constraint(expr= -(-0.00417 + m.x2)**2 - (-0.11887 + m.x5)**2 + m.x7
    <= 0)
m.e1674 = Constraint(expr= -(-0.95323 + m.x2)**2 - (-0.47253 + m.x5)**2 + m.x7
    <= 0)
m.e1675 = Constraint(expr= -(-0.51737 + m.x2)**2 - (-0.84407 + m.x5)**2 + m.x7
    <= 0)
m.e1676 = Constraint(expr= -(-0.74403 + m.x2)**2 - (-0.69133 + m.x5)**2 + m.x7
    <= 0)
m.e1677 = Constraint(expr= -(-0.30257 + m.x2)**2 - (-0.36127 + m.x5)**2 + m.x7
    <= 0)
m.e1678 = Constraint(expr= -(-0.10283 + m.x2)**2 - (-0.35813 + m.x5)**2 + m.x7
    <= 0)
m.e1679 = Constraint(expr= -(-0.47977 + m.x2)**2 - (-0.99047 + m.x5)**2 + m.x7
    <= 0)
m.e1680 = Constraint(expr= -(-0.30963 + m.x2)**2 - (-0.55293 + m.x5)**2 + m.x7
    <= 0)
m.e1681 = Constraint(expr= -(-0.36897 + m.x2)**2 - (-0.25167 + m.x5)**2 + m.x7
    <= 0)
m.e1682 = Constraint(expr= -(-0.44443 + m.x2)**2 - (-0.15573 + m.x5)**2 + m.x7
    <= 0)
m.e1683 = Constraint(expr= -(-0.49017 + m.x2)**2 - (-0.86487 + m.x5)**2 + m.x7
    <= 0)
m.e1684 = Constraint(expr= -(-0.38723 + m.x2)**2 - (-0.84653 + m.x5)**2 + m.x7
    <= 0)
m.e1685 = Constraint(expr= -(-0.56337 + m.x2)**2 - (-0.75007 + m.x5)**2 + m.x7
    <= 0)
m.e1686 = Constraint(expr= -(-0.81803 + m.x2)**2 - (-0.10533 + m.x5)**2 + m.x7
    <= 0)
m.e1687 = Constraint(expr= -(-0.50857 + m.x2)**2 - (-0.02727 + m.x5)**2 + m.x7
    <= 0)
m.e1688 = Constraint(expr= -(-0.21683 + m.x2)**2 - (-0.21213 + m.x5)**2 + m.x7
    <= 0)
m.e1689 = Constraint(expr= -(-0.44577 + m.x2)**2 - (-0.01647 + m.x5)**2 + m.x7
    <= 0)
m.e1690 = Constraint(expr= -(-0.86363 + m.x2)**2 - (-0.24693 + m.x5)**2 + m.x7
    <= 0)
m.e1691 = Constraint(expr= -(-0.69497 + m.x2)**2 - (-0.23767 + m.x5)**2 + m.x7
    <= 0)
m.e1692 = Constraint(expr= -(-0.83843 + m.x2)**2 - (-0.08973 + m.x5)**2 + m.x7
    <= 0)
m.e1693 = Constraint(expr= -(-0.77617 + m.x2)**2 - (-0.41087 + m.x5)**2 + m.x7
    <= 0)
m.e1694 = Constraint(expr= -(-0.02123 + m.x2)**2 - (-0.42053 + m.x5)**2 + m.x7
    <= 0)
m.e1695 = Constraint(expr= -(-0.40937 + m.x2)**2 - (-0.45607 + m.x5)**2 + m.x7
    <= 0)
m.e1696 = Constraint(expr= -(-0.09203 + m.x2)**2 - (-0.71933 + m.x5)**2 + m.x7
    <= 0)
m.e1697 = Constraint(expr= -(-0.51457 + m.x2)**2 - (-0.49327 + m.x5)**2 + m.x7
    <= 0)
m.e1698 = Constraint(expr= -(-0.53083 + m.x2)**2 - (-0.26613 + m.x5)**2 + m.x7
    <= 0)
m.e1699 = Constraint(expr= -(-0.21177 + m.x2)**2 - (-0.84247 + m.x5)**2 + m.x7
    <= 0)
m.e1700 = Constraint(expr= -(-0.61763 + m.x2)**2 - (-0.14093 + m.x5)**2 + m.x7
    <= 0)
m.e1701 = Constraint(expr= -(-0.82097 + m.x2)**2 - (-0.02367 + m.x5)**2 + m.x7
    <= 0)
m.e1702 = Constraint(expr= -(-0.43243 + m.x2)**2 - (-0.22373 + m.x5)**2 + m.x7
    <= 0)
m.e1703 = Constraint(expr= -(-0.86217 + m.x2)**2 - (-0.75687 + m.x5)**2 + m.x7
    <= 0)
m.e1704 = Constraint(expr= -(-0.85523 + m.x2)**2 - (-0.19453 + m.x5)**2 + m.x7
    <= 0)
m.e1705 = Constraint(expr= -(-0.05537 + m.x2)**2 - (-0.96207 + m.x5)**2 + m.x7
    <= 0)
m.e1706 = Constraint(expr= -(-0.56603 + m.x2)**2 - (-0.53333 + m.x5)**2 + m.x7
    <= 0)
m.e1707 = Constraint(expr= -(-0.32057 + m.x2)**2 - (-0.75927 + m.x5)**2 + m.x7
    <= 0)
m.e1708 = Constraint(expr= -(-0.04483 + m.x2)**2 - (-0.52013 + m.x5)**2 + m.x7
    <= 0)
m.e1709 = Constraint(expr= -(-0.77777 + m.x2)**2 - (-0.46847 + m.x5)**2 + m.x7
    <= 0)
m.e1710 = Constraint(expr= -(-0.57163 + m.x2)**2 - (-0.23493 + m.x5)**2 + m.x7
    <= 0)
m.e1711 = Constraint(expr= -(-0.74697 + m.x2)**2 - (-0.60967 + m.x5)**2 + m.x7
    <= 0)
m.e1712 = Constraint(expr= -(-0.22643 + m.x2)**2 - (-0.55773 + m.x5)**2 + m.x7
    <= 0)
m.e1713 = Constraint(expr= -(-0.74817 + m.x2)**2 - (-0.90287 + m.x5)**2 + m.x7
    <= 0)
m.e1714 = Constraint(expr= -(-0.88923 + m.x2)**2 - (-0.16853 + m.x5)**2 + m.x7
    <= 0)
m.e1715 = Constraint(expr= -(-0.50137 + m.x2)**2 - (-0.26807 + m.x5)**2 + m.x7
    <= 0)
m.e1716 = Constraint(expr= -(-0.24003 + m.x2)**2 - (-0.54733 + m.x5)**2 + m.x7
    <= 0)
m.e1717 = Constraint(expr= -(-0.92657 + m.x2)**2 - (-0.82527 + m.x5)**2 + m.x7
    <= 0)
m.e1718 = Constraint(expr= -(-0.75883 + m.x2)**2 - (-0.97413 + m.x5)**2 + m.x7
    <= 0)
m.e1719 = Constraint(expr= -(-0.14377 + m.x2)**2 - (-0.89447 + m.x5)**2 + m.x7
    <= 0)
m.e1720 = Constraint(expr= -(-0.72563 + m.x2)**2 - (-0.52893 + m.x5)**2 + m.x7
    <= 0)
m.e1721 = Constraint(expr= -(-0.47297 + m.x2)**2 - (-0.99567 + m.x5)**2 + m.x7
    <= 0)
m.e1722 = Constraint(expr= -(-0.22043 + m.x2)**2 - (-0.09173 + m.x5)**2 + m.x7
    <= 0)
m.e1723 = Constraint(expr= -(-0.43417 + m.x2)**2 - (-0.84887 + m.x5)**2 + m.x7
    <= 0)
m.e1724 = Constraint(expr= -(-0.12323 + m.x2)**2 - (-0.34253 + m.x5)**2 + m.x7
    <= 0)
m.e1725 = Constraint(expr= -(-0.74737 + m.x2)**2 - (-0.37407 + m.x5)**2 + m.x7
    <= 0)
m.e1726 = Constraint(expr= -(-0.11403 + m.x2)**2 - (-0.76133 + m.x5)**2 + m.x7
    <= 0)
m.e1727 = Constraint(expr= -(-0.33257 + m.x2)**2 - (-0.69127 + m.x5)**2 + m.x7
    <= 0)
m.e1728 = Constraint(expr= -(-0.67283 + m.x2)**2 - (-0.62813 + m.x5)**2 + m.x7
    <= 0)
m.e1729 = Constraint(expr= -(-0.30977 + m.x2)**2 - (-0.12047 + m.x5)**2 + m.x7
    <= 0)
m.e1730 = Constraint(expr= -(-0.07963 + m.x2)**2 - (-0.02293 + m.x5)**2 + m.x7
    <= 0)
m.e1731 = Constraint(expr= -(-0.99897 + m.x2)**2 - (-0.18167 + m.x5)**2 + m.x7
    <= 0)
m.e1732 = Constraint(expr= -(-0.41443 + m.x2)**2 - (-0.82573 + m.x5)**2 + m.x7
    <= 0)
m.e1733 = Constraint(expr= -(-0.92017 + m.x2)**2 - (-0.59487 + m.x5)**2 + m.x7
    <= 0)
m.e1734 = Constraint(expr= -(-0.55723 + m.x2)**2 - (-0.71653 + m.x5)**2 + m.x7
    <= 0)
m.e1735 = Constraint(expr= -(-0.79337 + m.x2)**2 - (-0.28007 + m.x5)**2 + m.x7
    <= 0)
m.e1736 = Constraint(expr= -(-0.18803 + m.x2)**2 - (-0.17533 + m.x5)**2 + m.x7
    <= 0)
m.e1737 = Constraint(expr= -(-0.53857 + m.x2)**2 - (-0.35727 + m.x5)**2 + m.x7
    <= 0)
m.e1738 = Constraint(expr= -(-0.78683 + m.x2)**2 - (-0.48213 + m.x5)**2 + m.x7
    <= 0)
m.e1739 = Constraint(expr= -(-0.27577 + m.x2)**2 - (-0.14647 + m.x5)**2 + m.x7
    <= 0)
m.e1740 = Constraint(expr= -(-0.63363 + m.x2)**2 - (-0.71693 + m.x5)**2 + m.x7
    <= 0)
m.e1741 = Constraint(expr= -(-0.32497 + m.x2)**2 - (-0.16767 + m.x5)**2 + m.x7
    <= 0)
m.e1742 = Constraint(expr= -(-0.80843 + m.x2)**2 - (-0.75973 + m.x5)**2 + m.x7
    <= 0)
m.e1743 = Constraint(expr= -(-0.20617 + m.x2)**2 - (-0.14087 + m.x5)**2 + m.x7
    <= 0)
m.e1744 = Constraint(expr= -(-0.19123 + m.x2)**2 - (-0.29053 + m.x5)**2 + m.x7
    <= 0)
m.e1745 = Constraint(expr= -(-0.63937 + m.x2)**2 - (-0.98607 + m.x5)**2 + m.x7
    <= 0)
m.e1746 = Constraint(expr= -(-0.46203 + m.x2)**2 - (-0.78933 + m.x5)**2 + m.x7
    <= 0)
m.e1747 = Constraint(expr= -(-0.54457 + m.x2)**2 - (-0.82327 + m.x5)**2 + m.x7
    <= 0)
m.e1748 = Constraint(expr= -(-0.10083 + m.x2)**2 - (-0.53613 + m.x5)**2 + m.x7
    <= 0)
m.e1749 = Constraint(expr= -(-0.04177 + m.x2)**2 - (-0.97247 + m.x5)**2 + m.x7
    <= 0)
m.e1750 = Constraint(expr= -(-0.38763 + m.x2)**2 - (-0.61093 + m.x5)**2 + m.x7
    <= 0)
m.e1751 = Constraint(expr= -(-0.45097 + m.x2)**2 - (-0.95367 + m.x5)**2 + m.x7
    <= 0)
m.e1752 = Constraint(expr= -(-0.40243 + m.x2)**2 - (-0.89373 + m.x5)**2 + m.x7
    <= 0)
m.e1753 = Constraint(expr= -(-0.29217 + m.x2)**2 - (-0.48687 + m.x5)**2 + m.x7
    <= 0)
m.e1754 = Constraint(expr= -(-0.02523 + m.x2)**2 - (-0.06453 + m.x5)**2 + m.x7
    <= 0)
m.e1755 = Constraint(expr= -(-0.28537 + m.x2)**2 - (-0.49207 + m.x5)**2 + m.x7
    <= 0)
m.e1756 = Constraint(expr= -(-0.93603 + m.x2)**2 - (-0.60333 + m.x5)**2 + m.x7
    <= 0)
m.e1757 = Constraint(expr= -(-0.35057 + m.x2)**2 - (-0.08927 + m.x5)**2 + m.x7
    <= 0)
m.e1758 = Constraint(expr= -(-0.61483 + m.x2)**2 - (-0.79013 + m.x5)**2 + m.x7
    <= 0)
m.e1759 = Constraint(expr= -(-0.60777 + m.x2)**2 - (-0.59847 + m.x5)**2 + m.x7
    <= 0)
m.e1760 = Constraint(expr= -(-0.34163 + m.x2)**2 - (-0.70493 + m.x5)**2 + m.x7
    <= 0)
m.e1761 = Constraint(expr= -(-0.37697 + m.x2)**2 - (-0.53967 + m.x5)**2 + m.x7
    <= 0)
m.e1762 = Constraint(expr= -(-0.19643 + m.x2)**2 - (-0.22773 + m.x5)**2 + m.x7
    <= 0)
m.e1763 = Constraint(expr= -(-0.17817 + m.x2)**2 - (-0.63287 + m.x5)**2 + m.x7
    <= 0)
m.e1764 = Constraint(expr= -(-0.05923 + m.x2)**2 - (-0.03853 + m.x5)**2 + m.x7
    <= 0)
m.e1765 = Constraint(expr= -(-0.73137 + m.x2)**2 - (-0.79807 + m.x5)**2 + m.x7
    <= 0)
m.e1766 = Constraint(expr= -(-0.61003 + m.x2)**2 - (-0.61733 + m.x5)**2 + m.x7
    <= 0)
m.e1767 = Constraint(expr= -(-0.95657 + m.x2)**2 - (-0.15527 + m.x5)**2 + m.x7
    <= 0)
m.e1768 = Constraint(expr= -(-0.32883 + m.x2)**2 - (-0.24413 + m.x5)**2 + m.x7
    <= 0)
m.e1769 = Constraint(expr= -(-0.97377 + m.x2)**2 - (-0.02447 + m.x5)**2 + m.x7
    <= 0)
m.e1770 = Constraint(expr= -(-0.49563 + m.x2)**2 - (-0.99893 + m.x5)**2 + m.x7
    <= 0)
m.e1771 = Constraint(expr= -(-0.10297 + m.x2)**2 - (-0.92567 + m.x5)**2 + m.x7
    <= 0)
m.e1772 = Constraint(expr= -(-0.19043 + m.x2)**2 - (-0.76173 + m.x5)**2 + m.x7
    <= 0)
m.e1773 = Constraint(expr= -(-0.86417 + m.x2)**2 - (-0.57887 + m.x5)**2 + m.x7
    <= 0)
m.e1774 = Constraint(expr= -(-0.29323 + m.x2)**2 - (-0.21253 + m.x5)**2 + m.x7
    <= 0)
m.e1775 = Constraint(expr= -(-0.97737 + m.x2)**2 - (-0.90407 + m.x5)**2 + m.x7
    <= 0)
m.e1776 = Constraint(expr= -(-0.48403 + m.x2)**2 - (-0.83133 + m.x5)**2 + m.x7
    <= 0)
m.e1777 = Constraint(expr= -(-0.36257 + m.x2)**2 - (-0.02127 + m.x5)**2 + m.x7
    <= 0)
m.e1778 = Constraint(expr= -(-0.24283 + m.x2)**2 - (-0.89813 + m.x5)**2 + m.x7
    <= 0)
m.e1779 = Constraint(expr= -(-0.13977 + m.x2)**2 - (-0.25047 + m.x5)**2 + m.x7
    <= 0)
m.e1780 = Constraint(expr= -(-0.84963 + m.x2)**2 - (-0.49293 + m.x5)**2 + m.x7
    <= 0)
m.e1781 = Constraint(expr= -(-0.62897 + m.x2)**2 - (-0.11167 + m.x5)**2 + m.x7
    <= 0)
m.e1782 = Constraint(expr= -(-0.38443 + m.x2)**2 - (-0.49573 + m.x5)**2 + m.x7
    <= 0)
m.e1783 = Constraint(expr= -(-0.35017 + m.x2)**2 - (-0.32487 + m.x5)**2 + m.x7
    <= 0)
m.e1784 = Constraint(expr= -(-0.72723 + m.x2)**2 - (-0.58653 + m.x5)**2 + m.x7
    <= 0)
m.e1785 = Constraint(expr= -(-0.02337 + m.x2)**2 - (-0.81007 + m.x5)**2 + m.x7
    <= 0)
m.e1786 = Constraint(expr= -(-0.55803 + m.x2)**2 - (-0.24533 + m.x5)**2 + m.x7
    <= 0)
m.e1787 = Constraint(expr= -(-0.56857 + m.x2)**2 - (-0.68727 + m.x5)**2 + m.x7
    <= 0)
m.e1788 = Constraint(expr= -(-0.35683 + m.x2)**2 - (-0.75213 + m.x5)**2 + m.x7
    <= 0)
m.e1789 = Constraint(expr= -(-0.10577 + m.x2)**2 - (-0.27647 + m.x5)**2 + m.x7
    <= 0)
m.e1790 = Constraint(expr= -(-0.40363 + m.x2)**2 - (-0.18693 + m.x5)**2 + m.x7
    <= 0)
m.e1791 = Constraint(expr= -(-0.95497 + m.x2)**2 - (-0.09767 + m.x5)**2 + m.x7
    <= 0)
m.e1792 = Constraint(expr= -(-0.77843 + m.x2)**2 - (-0.42973 + m.x5)**2 + m.x7
    <= 0)
m.e1793 = Constraint(expr= -(-0.63617 + m.x2)**2 - (-0.87087 + m.x5)**2 + m.x7
    <= 0)
m.e1794 = Constraint(expr= -(-0.36123 + m.x2)**2 - (-0.16053 + m.x5)**2 + m.x7
    <= 0)
m.e1795 = Constraint(expr= -(-0.86937 + m.x2)**2 - (-0.51607 + m.x5)**2 + m.x7
    <= 0)
m.e1796 = Constraint(expr= -(-0.83203 + m.x2)**2 - (-0.85933 + m.x5)**2 + m.x7
    <= 0)
m.e1797 = Constraint(expr= -(-0.57457 + m.x2)**2 - (-0.15327 + m.x5)**2 + m.x7
    <= 0)
m.e1798 = Constraint(expr= -(-0.67083 + m.x2)**2 - (-0.80613 + m.x5)**2 + m.x7
    <= 0)
m.e1799 = Constraint(expr= -(-0.87177 + m.x2)**2 - (-0.10247 + m.x5)**2 + m.x7
    <= 0)
m.e1800 = Constraint(expr= -(-0.15763 + m.x2)**2 - (-0.08093 + m.x5)**2 + m.x7
    <= 0)
m.e1801 = Constraint(expr= -(-0.08097 + m.x2)**2 - (-0.88367 + m.x5)**2 + m.x7
    <= 0)
m.e1802 = Constraint(expr= -(-0.37243 + m.x2)**2 - (-0.56373 + m.x5)**2 + m.x7
    <= 0)
m.e1803 = Constraint(expr= -(-0.72217 + m.x2)**2 - (-0.21687 + m.x5)**2 + m.x7
    <= 0)
m.e1804 = Constraint(expr= -(-0.19523 + m.x2)**2 - (-0.93453 + m.x5)**2 + m.x7
    <= 0)
m.e1805 = Constraint(expr= -(-0.51537 + m.x2)**2 - (-0.02207 + m.x5)**2 + m.x7
    <= 0)
m.e1806 = Constraint(expr= -(-0.30603 + m.x2)**2 - (-0.67333 + m.x5)**2 + m.x7
    <= 0)
m.e1807 = Constraint(expr= -(-0.38057 + m.x2)**2 - (-0.41927 + m.x5)**2 + m.x7
    <= 0)
m.e1808 = Constraint(expr= -(-0.18483 + m.x2)**2 - (-0.06013 + m.x5)**2 + m.x7
    <= 0)
m.e1809 = Constraint(expr= -(-0.43777 + m.x2)**2 - (-0.72847 + m.x5)**2 + m.x7
    <= 0)
m.e1810 = Constraint(expr= -(-0.11163 + m.x2)**2 - (-0.17493 + m.x5)**2 + m.x7
    <= 0)
m.e1811 = Constraint(expr= -(-0.00697 + m.x2)**2 - (-0.46967 + m.x5)**2 + m.x7
    <= 0)
m.e1812 = Constraint(expr= -(-0.16643 + m.x2)**2 - (-0.89773 + m.x5)**2 + m.x7
    <= 0)
m.e1813 = Constraint(expr= -(-0.60817 + m.x2)**2 - (-0.36287 + m.x5)**2 + m.x7
    <= 0)
m.e1814 = Constraint(expr= -(-0.22923 + m.x2)**2 - (-0.90853 + m.x5)**2 + m.x7
    <= 0)
m.e1815 = Constraint(expr= -(-0.96137 + m.x2)**2 - (-0.32807 + m.x5)**2 + m.x7
    <= 0)
m.e1816 = Constraint(expr= -(-0.98003 + m.x2)**2 - (-0.68733 + m.x5)**2 + m.x7
    <= 0)
m.e1817 = Constraint(expr= -(-0.98657 + m.x2)**2 - (-0.48527 + m.x5)**2 + m.x7
    <= 0)
m.e1818 = Constraint(expr= -(-0.89883 + m.x2)**2 - (-0.51413 + m.x5)**2 + m.x7
    <= 0)
m.e1819 = Constraint(expr= -(-0.80377 + m.x2)**2 - (-0.15447 + m.x5)**2 + m.x7
    <= 0)
m.e1820 = Constraint(expr= -(-0.26563 + m.x2)**2 - (-0.46893 + m.x5)**2 + m.x7
    <= 0)
m.e1821 = Constraint(expr= -(-0.73297 + m.x2)**2 - (-0.85567 + m.x5)**2 + m.x7
    <= 0)
m.e1822 = Constraint(expr= -(-0.16043 + m.x2)**2 - (-0.43173 + m.x5)**2 + m.x7
    <= 0)
m.e1823 = Constraint(expr= -(-0.29417 + m.x2)**2 - (-0.30887 + m.x5)**2 + m.x7
    <= 0)
m.e1824 = Constraint(expr= -(-0.46323 + m.x2)**2 - (-0.08253 + m.x5)**2 + m.x7
    <= 0)
m.e1825 = Constraint(expr= -(-0.20737 + m.x2)**2 - (-0.43407 + m.x5)**2 + m.x7
    <= 0)
m.e1826 = Constraint(expr= -(-0.85403 + m.x2)**2 - (-0.90133 + m.x5)**2 + m.x7
    <= 0)
m.e1827 = Constraint(expr= -(-0.39257 + m.x2)**2 - (-0.35127 + m.x5)**2 + m.x7
    <= 0)
m.e1828 = Constraint(expr= -(-0.81283 + m.x2)**2 - (-0.16813 + m.x5)**2 + m.x7
    <= 0)
m.e1829 = Constraint(expr= -(-0.96977 + m.x2)**2 - (-0.38047 + m.x5)**2 + m.x7
    <= 0)
m.e1830 = Constraint(expr= -(-0.61963 + m.x2)**2 - (-0.96293 + m.x5)**2 + m.x7
    <= 0)
m.e1831 = Constraint(expr= -(-0.25897 + m.x2)**2 - (-0.04167 + m.x5)**2 + m.x7
    <= 0)
m.e1832 = Constraint(expr= -(-0.35443 + m.x2)**2 - (-0.16573 + m.x5)**2 + m.x7
    <= 0)
m.e1833 = Constraint(expr= -(-0.78017 + m.x2)**2 - (-0.05487 + m.x5)**2 + m.x7
    <= 0)
m.e1834 = Constraint(expr= -(-0.89723 + m.x2)**2 - (-0.45653 + m.x5)**2 + m.x7
    <= 0)
m.e1835 = Constraint(expr= -(-0.25337 + m.x2)**2 - (-0.34007 + m.x5)**2 + m.x7
    <= 0)
m.e1836 = Constraint(expr= -(-0.92803 + m.x2)**2 - (-0.31533 + m.x5)**2 + m.x7
    <= 0)
m.e1837 = Constraint(expr= -(-0.59857 + m.x2)**2 - (-0.01727 + m.x5)**2 + m.x7
    <= 0)
m.e1838 = Constraint(expr= -(-0.92683 + m.x2)**2 - (-0.02213 + m.x5)**2 + m.x7
    <= 0)
m.e1839 = Constraint(expr= -(-0.93577 + m.x2)**2 - (-0.40647 + m.x5)**2 + m.x7
    <= 0)
m.e1840 = Constraint(expr= -(-0.17363 + m.x2)**2 - (-0.65693 + m.x5)**2 + m.x7
    <= 0)
m.e1841 = Constraint(expr= -(-0.58497 + m.x2)**2 - (-0.02767 + m.x5)**2 + m.x7
    <= 0)
m.e1842 = Constraint(expr= -(-0.74843 + m.x2)**2 - (-0.09973 + m.x5)**2 + m.x7
    <= 0)
m.e1843 = Constraint(expr= -(-0.06617 + m.x2)**2 - (-0.60087 + m.x5)**2 + m.x7
    <= 0)
m.e1844 = Constraint(expr= -(-0.53123 + m.x2)**2 - (-0.03053 + m.x5)**2 + m.x7
    <= 0)
m.e1845 = Constraint(expr= -(-0.09937 + m.x2)**2 - (-0.04607 + m.x5)**2 + m.x7
    <= 0)
m.e1846 = Constraint(expr= -(-0.20203 + m.x2)**2 - (-0.92933 + m.x5)**2 + m.x7
    <= 0)
m.e1847 = Constraint(expr= -(-0.60457 + m.x2)**2 - (-0.48327 + m.x5)**2 + m.x7
    <= 0)
m.e1848 = Constraint(expr= -(-0.24083 + m.x2)**2 - (-0.07613 + m.x5)**2 + m.x7
    <= 0)
m.e1849 = Constraint(expr= -(-0.70177 + m.x2)**2 - (-0.23247 + m.x5)**2 + m.x7
    <= 0)
m.e1850 = Constraint(expr= -(-0.92763 + m.x2)**2 - (-0.55093 + m.x5)**2 + m.x7
    <= 0)
m.e1851 = Constraint(expr= -(-0.71097 + m.x2)**2 - (-0.81367 + m.x5)**2 + m.x7
    <= 0)
m.e1852 = Constraint(expr= -(-0.34243 + m.x2)**2 - (-0.23373 + m.x5)**2 + m.x7
    <= 0)
m.e1853 = Constraint(expr= -(-0.15217 + m.x2)**2 - (-0.94687 + m.x5)**2 + m.x7
    <= 0)
m.e1854 = Constraint(expr= -(-0.36523 + m.x2)**2 - (-0.80453 + m.x5)**2 + m.x7
    <= 0)
m.e1855 = Constraint(expr= -(-0.74537 + m.x2)**2 - (-0.55207 + m.x5)**2 + m.x7
    <= 0)
m.e1856 = Constraint(expr= -(-0.67603 + m.x2)**2 - (-0.74333 + m.x5)**2 + m.x7
    <= 0)
m.e1857 = Constraint(expr= -(-0.41057 + m.x2)**2 - (-0.74927 + m.x5)**2 + m.x7
    <= 0)
m.e1858 = Constraint(expr= -(-0.75483 + m.x2)**2 - (-0.33013 + m.x5)**2 + m.x7
    <= 0)
m.e1859 = Constraint(expr= -(-0.26777 + m.x2)**2 - (-0.85847 + m.x5)**2 + m.x7
    <= 0)
m.e1860 = Constraint(expr= -(-0.88163 + m.x2)**2 - (-0.64493 + m.x5)**2 + m.x7
    <= 0)
m.e1861 = Constraint(expr= -(-0.63697 + m.x2)**2 - (-0.39967 + m.x5)**2 + m.x7
    <= 0)
m.e1862 = Constraint(expr= -(-0.13643 + m.x2)**2 - (-0.56773 + m.x5)**2 + m.x7
    <= 0)
m.e1863 = Constraint(expr= -(-0.03817 + m.x2)**2 - (-0.09287 + m.x5)**2 + m.x7
    <= 0)
m.e1864 = Constraint(expr= -(-0.39923 + m.x2)**2 - (-0.77853 + m.x5)**2 + m.x7
    <= 0)
m.e1865 = Constraint(expr= -(-0.19137 + m.x2)**2 - (-0.85807 + m.x5)**2 + m.x7
    <= 0)
m.e1866 = Constraint(expr= -(-0.35003 + m.x2)**2 - (-0.75733 + m.x5)**2 + m.x7
    <= 0)
m.e1867 = Constraint(expr= -(-0.01657 + m.x2)**2 - (-0.81527 + m.x5)**2 + m.x7
    <= 0)
m.e1868 = Constraint(expr= -(-0.46883 + m.x2)**2 - (-0.78413 + m.x5)**2 + m.x7
    <= 0)
m.e1869 = Constraint(expr= -(-0.63377 + m.x2)**2 - (-0.28447 + m.x5)**2 + m.x7
    <= 0)
m.e1870 = Constraint(expr= -(-0.03563 + m.x2)**2 - (-0.93893 + m.x5)**2 + m.x7
    <= 0)
m.e1871 = Constraint(expr= -(-0.36297 + m.x2)**2 - (-0.78567 + m.x5)**2 + m.x7
    <= 0)
m.e1872 = Constraint(expr= -(-0.13043 + m.x2)**2 - (-0.10173 + m.x5)**2 + m.x7
    <= 0)
m.e1873 = Constraint(expr= -(-0.72417 + m.x2)**2 - (-0.03887 + m.x5)**2 + m.x7
    <= 0)
m.e1874 = Constraint(expr= -(-0.63323 + m.x2)**2 - (-0.95253 + m.x5)**2 + m.x7
    <= 0)
m.e1875 = Constraint(expr= -(-0.43737 + m.x2)**2 - (-0.96407 + m.x5)**2 + m.x7
    <= 0)
m.e1876 = Constraint(expr= -(-0.22403 + m.x2)**2 - (-0.97133 + m.x5)**2 + m.x7
    <= 0)
m.e1877 = Constraint(expr= -(-0.42257 + m.x2)**2 - (-0.68127 + m.x5)**2 + m.x7
    <= 0)
m.e1878 = Constraint(expr= -(-0.38283 + m.x2)**2 - (-0.43813 + m.x5)**2 + m.x7
    <= 0)
m.e1879 = Constraint(expr= -(-0.79977 + m.x2)**2 - (-0.51047 + m.x5)**2 + m.x7
    <= 0)
m.e1880 = Constraint(expr= -(-0.38963 + m.x2)**2 - (-0.43293 + m.x5)**2 + m.x7
    <= 0)
m.e1881 = Constraint(expr= -(-0.88897 + m.x2)**2 - (-0.97167 + m.x5)**2 + m.x7
    <= 0)
m.e1882 = Constraint(expr= -(-0.32443 + m.x2)**2 - (-0.83573 + m.x5)**2 + m.x7
    <= 0)
m.e1883 = Constraint(expr= -(-0.21017 + m.x2)**2 - (-0.78487 + m.x5)**2 + m.x7
    <= 0)
m.e1884 = Constraint(expr= -(-0.06723 + m.x2)**2 - (-0.32653 + m.x5)**2 + m.x7
    <= 0)
m.e1885 = Constraint(expr= -(-0.48337 + m.x2)**2 - (-0.87007 + m.x5)**2 + m.x7
    <= 0)
m.e1886 = Constraint(expr= -(-0.29803 + m.x2)**2 - (-0.38533 + m.x5)**2 + m.x7
    <= 0)
m.e1887 = Constraint(expr= -(-0.62857 + m.x2)**2 - (-0.34727 + m.x5)**2 + m.x7
    <= 0)
m.e1888 = Constraint(expr= -(-0.49683 + m.x2)**2 - (-0.29213 + m.x5)**2 + m.x7
    <= 0)
m.e1889 = Constraint(expr= -(-0.76577 + m.x2)**2 - (-0.53647 + m.x5)**2 + m.x7
    <= 0)
m.e1890 = Constraint(expr= -(-0.94363 + m.x2)**2 - (-0.12693 + m.x5)**2 + m.x7
    <= 0)
m.e1891 = Constraint(expr= -(-0.21497 + m.x2)**2 - (-0.95767 + m.x5)**2 + m.x7
    <= 0)
m.e1892 = Constraint(expr= -(-0.71843 + m.x2)**2 - (-0.76973 + m.x5)**2 + m.x7
    <= 0)
m.e1893 = Constraint(expr= -(-0.49617 + m.x2)**2 - (-0.33087 + m.x5)**2 + m.x7
    <= 0)
m.e1894 = Constraint(expr= -(-0.70123 + m.x2)**2 - (-0.90053 + m.x5)**2 + m.x7
    <= 0)
m.e1895 = Constraint(expr= -(-0.32937 + m.x2)**2 - (-0.57607 + m.x5)**2 + m.x7
    <= 0)
m.e1896 = Constraint(expr= -(-0.57203 + m.x2)**2 - (-0.99933 + m.x5)**2 + m.x7
    <= 0)
m.e1897 = Constraint(expr= -(-0.63457 + m.x2)**2 - (-0.81327 + m.x5)**2 + m.x7
    <= 0)
m.e1898 = Constraint(expr= -(-0.81083 + m.x2)**2 - (-0.34613 + m.x5)**2 + m.x7
    <= 0)
m.e1899 = Constraint(expr= -(-0.53177 + m.x2)**2 - (-0.36247 + m.x5)**2 + m.x7
    <= 0)
m.e1900 = Constraint(expr= -(-0.69763 + m.x2)**2 - (-0.02093 + m.x5)**2 + m.x7
    <= 0)
m.e1901 = Constraint(expr= -(-0.34097 + m.x2)**2 - (-0.74367 + m.x5)**2 + m.x7
    <= 0)
m.e1902 = Constraint(expr= -(-0.31243 + m.x2)**2 - (-0.90373 + m.x5)**2 + m.x7
    <= 0)
m.e1903 = Constraint(expr= -(-0.58217 + m.x2)**2 - (-0.67687 + m.x5)**2 + m.x7
    <= 0)
m.e1904 = Constraint(expr= -(-0.53523 + m.x2)**2 - (-0.67453 + m.x5)**2 + m.x7
    <= 0)
m.e1905 = Constraint(expr= -(-0.97537 + m.x2)**2 - (-0.08207 + m.x5)**2 + m.x7
    <= 0)
m.e1906 = Constraint(expr= -(-0.04603 + m.x2)**2 - (-0.81333 + m.x5)**2 + m.x7
    <= 0)
m.e1907 = Constraint(expr= -(-0.44057 + m.x2)**2 - (-0.07927 + m.x5)**2 + m.x7
    <= 0)
m.e1908 = Constraint(expr= -(-0.32483 + m.x2)**2 - (-0.60013 + m.x5)**2 + m.x7
    <= 0)
m.e1909 = Constraint(expr= -(-0.09777 + m.x2)**2 - (-0.98847 + m.x5)**2 + m.x7
    <= 0)
m.e1910 = Constraint(expr= -(-0.65163 + m.x2)**2 - (-0.11493 + m.x5)**2 + m.x7
    <= 0)
m.e1911 = Constraint(expr= -(-0.26697 + m.x2)**2 - (-0.32967 + m.x5)**2 + m.x7
    <= 0)
m.e1912 = Constraint(expr= -(-0.10643 + m.x2)**2 - (-0.23773 + m.x5)**2 + m.x7
    <= 0)
m.e1913 = Constraint(expr= -(-0.46817 + m.x2)**2 - (-0.82287 + m.x5)**2 + m.x7
    <= 0)
m.e1914 = Constraint(expr= -(-0.56923 + m.x2)**2 - (-0.64853 + m.x5)**2 + m.x7
    <= 0)
m.e1915 = Constraint(expr= -(-0.42137 + m.x2)**2 - (-0.38807 + m.x5)**2 + m.x7
    <= 0)
m.e1916 = Constraint(expr= -(-0.72003 + m.x2)**2 - (-0.82733 + m.x5)**2 + m.x7
    <= 0)
m.e1917 = Constraint(expr= -(-0.04657 + m.x2)**2 - (-0.14527 + m.x5)**2 + m.x7
    <= 0)
m.e1918 = Constraint(expr= -(-0.03883 + m.x2)**2 - (-0.05413 + m.x5)**2 + m.x7
    <= 0)
m.e1919 = Constraint(expr= -(-0.46377 + m.x2)**2 - (-0.41447 + m.x5)**2 + m.x7
    <= 0)
m.e1920 = Constraint(expr= -(-0.80563 + m.x2)**2 - (-0.40893 + m.x5)**2 + m.x7
    <= 0)
m.e1921 = Constraint(expr= -(-0.99297 + m.x2)**2 - (-0.71567 + m.x5)**2 + m.x7
    <= 0)
m.e1922 = Constraint(expr= -(-0.10043 + m.x2)**2 - (-0.77173 + m.x5)**2 + m.x7
    <= 0)
m.e1923 = Constraint(expr= -(-0.15417 + m.x2)**2 - (-0.76887 + m.x5)**2 + m.x7
    <= 0)
m.e1924 = Constraint(expr= -(-0.80323 + m.x2)**2 - (-0.82253 + m.x5)**2 + m.x7
    <= 0)
m.e1925 = Constraint(expr= -(-0.66737 + m.x2)**2 - (-0.49407 + m.x5)**2 + m.x7
    <= 0)
m.e1926 = Constraint(expr= -(-0.59403 + m.x2)**2 - (-0.04133 + m.x5)**2 + m.x7
    <= 0)
m.e1927 = Constraint(expr= -(-0.45257 + m.x2)**2 - (-0.01127 + m.x5)**2 + m.x7
    <= 0)
m.e1928 = Constraint(expr= -(-0.95283 + m.x2)**2 - (-0.70813 + m.x5)**2 + m.x7
    <= 0)
m.e1929 = Constraint(expr= -(-0.62977 + m.x2)**2 - (-0.64047 + m.x5)**2 + m.x7
    <= 0)
m.e1930 = Constraint(expr= -(-0.15963 + m.x2)**2 - (-0.90293 + m.x5)**2 + m.x7
    <= 0)
m.e1931 = Constraint(expr= -(-0.51897 + m.x2)**2 - (-0.90167 + m.x5)**2 + m.x7
    <= 0)
m.e1932 = Constraint(expr= -(-0.29443 + m.x2)**2 - (-0.50573 + m.x5)**2 + m.x7
    <= 0)
m.e1933 = Constraint(expr= -(-0.64017 + m.x2)**2 - (-0.51487 + m.x5)**2 + m.x7
    <= 0)
m.e1934 = Constraint(expr= -(-0.23723 + m.x2)**2 - (-0.19653 + m.x5)**2 + m.x7
    <= 0)
m.e1935 = Constraint(expr= -(-0.71337 + m.x2)**2 - (-0.40007 + m.x5)**2 + m.x7
    <= 0)
m.e1936 = Constraint(expr= -(-0.66803 + m.x2)**2 - (-0.45533 + m.x5)**2 + m.x7
    <= 0)
m.e1937 = Constraint(expr= -(-0.65857 + m.x2)**2 - (-0.67727 + m.x5)**2 + m.x7
    <= 0)
m.e1938 = Constraint(expr= -(-0.06683 + m.x2)**2 - (-0.56213 + m.x5)**2 + m.x7
    <= 0)
m.e1939 = Constraint(expr= -(-0.59577 + m.x2)**2 - (-0.66647 + m.x5)**2 + m.x7
    <= 0)
m.e1940 = Constraint(expr= -(-0.71363 + m.x2)**2 - (-0.59693 + m.x5)**2 + m.x7
    <= 0)
m.e1941 = Constraint(expr= -(-0.84497 + m.x2)**2 - (-0.88767 + m.x5)**2 + m.x7
    <= 0)
m.e1942 = Constraint(expr= -(-0.68843 + m.x2)**2 - (-0.43973 + m.x5)**2 + m.x7
    <= 0)
m.e1943 = Constraint(expr= -(-0.92617 + m.x2)**2 - (-0.06087 + m.x5)**2 + m.x7
    <= 0)
m.e1944 = Constraint(expr= -(-0.87123 + m.x2)**2 - (-0.77053 + m.x5)**2 + m.x7
    <= 0)
m.e1945 = Constraint(expr= -(-0.55937 + m.x2)**2 - (-0.10607 + m.x5)**2 + m.x7
    <= 0)
m.e1946 = Constraint(expr= -(-0.94203 + m.x2)**2 - (-0.06933 + m.x5)**2 + m.x7
    <= 0)
m.e1947 = Constraint(expr= -(-0.66457 + m.x2)**2 - (-0.14327 + m.x5)**2 + m.x7
    <= 0)
m.e1948 = Constraint(expr= -(-0.38083 + m.x2)**2 - (-0.61613 + m.x5)**2 + m.x7
    <= 0)
m.e1949 = Constraint(expr= -(-0.36177 + m.x2)**2 - (-0.49247 + m.x5)**2 + m.x7
    <= 0)
m.e1950 = Constraint(expr= -(-0.46763 + m.x2)**2 - (-0.49093 + m.x5)**2 + m.x7
    <= 0)
m.e1951 = Constraint(expr= -(-0.97097 + m.x2)**2 - (-0.67367 + m.x5)**2 + m.x7
    <= 0)
m.e1952 = Constraint(expr= -(-0.28243 + m.x2)**2 - (-0.57373 + m.x5)**2 + m.x7
    <= 0)
m.e1953 = Constraint(expr= -(-0.01217 + m.x2)**2 - (-0.40687 + m.x5)**2 + m.x7
    <= 0)
m.e1954 = Constraint(expr= -(-0.70523 + m.x2)**2 - (-0.54453 + m.x5)**2 + m.x7
    <= 0)
m.e1955 = Constraint(expr= -(-0.20537 + m.x2)**2 - (-0.61207 + m.x5)**2 + m.x7
    <= 0)
m.e1956 = Constraint(expr= -(-0.41603 + m.x2)**2 - (-0.88333 + m.x5)**2 + m.x7
    <= 0)
m.e1957 = Constraint(expr= -(-0.47057 + m.x2)**2 - (-0.40927 + m.x5)**2 + m.x7
    <= 0)
m.e1958 = Constraint(expr= -(-0.89483 + m.x2)**2 - (-0.87013 + m.x5)**2 + m.x7
    <= 0)
m.e1959 = Constraint(expr= -(-0.92777 + m.x2)**2 - (-0.11847 + m.x5)**2 + m.x7
    <= 0)
m.e1960 = Constraint(expr= -(-0.42163 + m.x2)**2 - (-0.58493 + m.x5)**2 + m.x7
    <= 0)
m.e1961 = Constraint(expr= -(-0.89697 + m.x2)**2 - (-0.25967 + m.x5)**2 + m.x7
    <= 0)
m.e1962 = Constraint(expr= -(-0.07643 + m.x2)**2 - (-0.90773 + m.x5)**2 + m.x7
    <= 0)
m.e1963 = Constraint(expr= -(-0.89817 + m.x2)**2 - (-0.55287 + m.x5)**2 + m.x7
    <= 0)
m.e1964 = Constraint(expr= -(-0.73923 + m.x2)**2 - (-0.51853 + m.x5)**2 + m.x7
    <= 0)
m.e1965 = Constraint(expr= -(-0.65137 + m.x2)**2 - (-0.91807 + m.x5)**2 + m.x7
    <= 0)
m.e1966 = Constraint(expr= -(-0.09003 + m.x2)**2 - (-0.89733 + m.x5)**2 + m.x7
    <= 0)
m.e1967 = Constraint(expr= -(-0.07657 + m.x2)**2 - (-0.47527 + m.x5)**2 + m.x7
    <= 0)
m.e1968 = Constraint(expr= -(-0.60883 + m.x2)**2 - (-0.32413 + m.x5)**2 + m.x7
    <= 0)
m.e1969 = Constraint(expr= -(-0.29377 + m.x2)**2 - (-0.54447 + m.x5)**2 + m.x7
    <= 0)
m.e1970 = Constraint(expr= -(-0.57563 + m.x2)**2 - (-0.87893 + m.x5)**2 + m.x7
    <= 0)
m.e1971 = Constraint(expr= -(-0.62297 + m.x2)**2 - (-0.64567 + m.x5)**2 + m.x7
    <= 0)
m.e1972 = Constraint(expr= -(-0.07043 + m.x2)**2 - (-0.44173 + m.x5)**2 + m.x7
    <= 0)
m.e1973 = Constraint(expr= -(-0.58417 + m.x2)**2 - (-0.49887 + m.x5)**2 + m.x7
    <= 0)
m.e1974 = Constraint(expr= -(-0.97323 + m.x2)**2 - (-0.69253 + m.x5)**2 + m.x7
    <= 0)
m.e1975 = Constraint(expr= -(-0.89737 + m.x2)**2 - (-0.02407 + m.x5)**2 + m.x7
    <= 0)
m.e1976 = Constraint(expr= -(-0.96403 + m.x2)**2 - (-0.11133 + m.x5)**2 + m.x7
    <= 0)
m.e1977 = Constraint(expr= -(-0.48257 + m.x2)**2 - (-0.34127 + m.x5)**2 + m.x7
    <= 0)
m.e1978 = Constraint(expr= -(-0.52283 + m.x2)**2 - (-0.97813 + m.x5)**2 + m.x7
    <= 0)
m.e1979 = Constraint(expr= -(-0.45977 + m.x2)**2 - (-0.77047 + m.x5)**2 + m.x7
    <= 0)
m.e1980 = Constraint(expr= -(-0.92963 + m.x2)**2 - (-0.37293 + m.x5)**2 + m.x7
    <= 0)
m.e1981 = Constraint(expr= -(-0.14897 + m.x2)**2 - (-0.83167 + m.x5)**2 + m.x7
    <= 0)
m.e1982 = Constraint(expr= -(-0.26443 + m.x2)**2 - (-0.17573 + m.x5)**2 + m.x7
    <= 0)
m.e1983 = Constraint(expr= -(-0.07017 + m.x2)**2 - (-0.24487 + m.x5)**2 + m.x7
    <= 0)
m.e1984 = Constraint(expr= -(-0.40723 + m.x2)**2 - (-0.06653 + m.x5)**2 + m.x7
    <= 0)
m.e1985 = Constraint(expr= -(-0.94337 + m.x2)**2 - (-0.93007 + m.x5)**2 + m.x7
    <= 0)
m.e1986 = Constraint(expr= -(-0.03803 + m.x2)**2 - (-0.52533 + m.x5)**2 + m.x7
    <= 0)
m.e1987 = Constraint(expr= -(-0.68857 + m.x2)**2 - (-0.00727 + m.x5)**2 + m.x7
    <= 0)
m.e1988 = Constraint(expr= -(-0.63683 + m.x2)**2 - (-0.83213 + m.x5)**2 + m.x7
    <= 0)
m.e1989 = Constraint(expr= -(-0.42577 + m.x2)**2 - (-0.79647 + m.x5)**2 + m.x7
    <= 0)
m.e1990 = Constraint(expr= -(-0.48363 + m.x2)**2 - (-0.06693 + m.x5)**2 + m.x7
    <= 0)
m.e1991 = Constraint(expr= -(-0.47497 + m.x2)**2 - (-0.81767 + m.x5)**2 + m.x7
    <= 0)
m.e1992 = Constraint(expr= -(-0.65843 + m.x2)**2 - (-0.10973 + m.x5)**2 + m.x7
    <= 0)
m.e1993 = Constraint(expr= -(-0.35617 + m.x2)**2 - (-0.79087 + m.x5)**2 + m.x7
    <= 0)
m.e1994 = Constraint(expr= -(-0.04123 + m.x2)**2 - (-0.64053 + m.x5)**2 + m.x7
    <= 0)
m.e1995 = Constraint(expr= -(-0.78937 + m.x2)**2 - (-0.63607 + m.x5)**2 + m.x7
    <= 0)
m.e1996 = Constraint(expr= -(-0.31203 + m.x2)**2 - (-0.13933 + m.x5)**2 + m.x7
    <= 0)
m.e1997 = Constraint(expr= -(-0.69457 + m.x2)**2 - (-0.47327 + m.x5)**2 + m.x7
    <= 0)
m.e1998 = Constraint(expr= -(-0.95083 + m.x2)**2 - (-0.88613 + m.x5)**2 + m.x7
    <= 0)
m.e1999 = Constraint(expr= -(-0.19177 + m.x2)**2 - (-0.62247 + m.x5)**2 + m.x7
    <= 0)
m.e2000 = Constraint(expr= -(-0.23763 + m.x2)**2 - (-0.96093 + m.x5)**2 + m.x7
    <= 0)
m.e2001 = Constraint(expr= -(-0.00097 + m.x3)**2 - (-0.00367 + m.x6)**2 + m.x7
    <= 0)
m.e2002 = Constraint(expr= -(-0.85243 + m.x3)**2 - (-0.84373 + m.x6)**2 + m.x7
    <= 0)
m.e2003 = Constraint(expr= -(-0.84217 + m.x3)**2 - (-0.53687 + m.x6)**2 + m.x7
    <= 0)
m.e2004 = Constraint(expr= -(-0.47523 + m.x3)**2 - (-0.01453 + m.x6)**2 + m.x7
    <= 0)
m.e2005 = Constraint(expr= -(-0.83537 + m.x3)**2 - (-0.54207 + m.x6)**2 + m.x7
    <= 0)
m.e2006 = Constraint(expr= -(-0.38603 + m.x3)**2 - (-0.55333 + m.x6)**2 + m.x7
    <= 0)
m.e2007 = Constraint(expr= -(-0.90057 + m.x3)**2 - (-0.13927 + m.x6)**2 + m.x7
    <= 0)
m.e2008 = Constraint(expr= -(-0.06483 + m.x3)**2 - (-0.74013 + m.x6)**2 + m.x7
    <= 0)
m.e2009 = Constraint(expr= -(-0.15777 + m.x3)**2 - (-0.64847 + m.x6)**2 + m.x7
    <= 0)
m.e2010 = Constraint(expr= -(-0.79163 + m.x3)**2 - (-0.65493 + m.x6)**2 + m.x7
    <= 0)
m.e2011 = Constraint(expr= -(-0.92697 + m.x3)**2 - (-0.58967 + m.x6)**2 + m.x7
    <= 0)
m.e2012 = Constraint(expr= -(-0.64643 + m.x3)**2 - (-0.17773 + m.x6)**2 + m.x7
    <= 0)
m.e2013 = Constraint(expr= -(-0.72817 + m.x3)**2 - (-0.68287 + m.x6)**2 + m.x7
    <= 0)
m.e2014 = Constraint(expr= -(-0.50923 + m.x3)**2 - (-0.98853 + m.x6)**2 + m.x7
    <= 0)
m.e2015 = Constraint(expr= -(-0.28137 + m.x3)**2 - (-0.84807 + m.x6)**2 + m.x7
    <= 0)
m.e2016 = Constraint(expr= -(-0.06003 + m.x3)**2 - (-0.56733 + m.x6)**2 + m.x7
    <= 0)
m.e2017 = Constraint(expr= -(-0.50657 + m.x3)**2 - (-0.20527 + m.x6)**2 + m.x7
    <= 0)
m.e2018 = Constraint(expr= -(-0.77883 + m.x3)**2 - (-0.19413 + m.x6)**2 + m.x7
    <= 0)
m.e2019 = Constraint(expr= -(-0.52377 + m.x3)**2 - (-0.07447 + m.x6)**2 + m.x7
    <= 0)
m.e2020 = Constraint(expr= -(-0.94563 + m.x3)**2 - (-0.94893 + m.x6)**2 + m.x7
    <= 0)
m.e2021 = Constraint(expr= -(-0.65297 + m.x3)**2 - (-0.97567 + m.x6)**2 + m.x7
    <= 0)
m.e2022 = Constraint(expr= -(-0.64043 + m.x3)**2 - (-0.71173 + m.x6)**2 + m.x7
    <= 0)
m.e2023 = Constraint(expr= -(-0.41417 + m.x3)**2 - (-0.62887 + m.x6)**2 + m.x7
    <= 0)
m.e2024 = Constraint(expr= -(-0.74323 + m.x3)**2 - (-0.16253 + m.x6)**2 + m.x7
    <= 0)
m.e2025 = Constraint(expr= -(-0.52737 + m.x3)**2 - (-0.95407 + m.x6)**2 + m.x7
    <= 0)
m.e2026 = Constraint(expr= -(-0.93403 + m.x3)**2 - (-0.78133 + m.x6)**2 + m.x7
    <= 0)
m.e2027 = Constraint(expr= -(-0.91257 + m.x3)**2 - (-0.07127 + m.x6)**2 + m.x7
    <= 0)
m.e2028 = Constraint(expr= -(-0.69283 + m.x3)**2 - (-0.84813 + m.x6)**2 + m.x7
    <= 0)
m.e2029 = Constraint(expr= -(-0.68977 + m.x3)**2 - (-0.30047 + m.x6)**2 + m.x7
    <= 0)
m.e2030 = Constraint(expr= -(-0.29963 + m.x3)**2 - (-0.44293 + m.x6)**2 + m.x7
    <= 0)
m.e2031 = Constraint(expr= -(-0.17897 + m.x3)**2 - (-0.16167 + m.x6)**2 + m.x7
    <= 0)
m.e2032 = Constraint(expr= -(-0.83443 + m.x3)**2 - (-0.44573 + m.x6)**2 + m.x7
    <= 0)
m.e2033 = Constraint(expr= -(-0.90017 + m.x3)**2 - (-0.37487 + m.x6)**2 + m.x7
    <= 0)
m.e2034 = Constraint(expr= -(-0.17723 + m.x3)**2 - (-0.53653 + m.x6)**2 + m.x7
    <= 0)
m.e2035 = Constraint(expr= -(-0.57337 + m.x3)**2 - (-0.86007 + m.x6)**2 + m.x7
    <= 0)
m.e2036 = Constraint(expr= -(-0.00803 + m.x3)**2 - (-0.19533 + m.x6)**2 + m.x7
    <= 0)
m.e2037 = Constraint(expr= -(-0.11857 + m.x3)**2 - (-0.73727 + m.x6)**2 + m.x7
    <= 0)
m.e2038 = Constraint(expr= -(-0.80683 + m.x3)**2 - (-0.70213 + m.x6)**2 + m.x7
    <= 0)
m.e2039 = Constraint(expr= -(-0.65577 + m.x3)**2 - (-0.32647 + m.x6)**2 + m.x7
    <= 0)
m.e2040 = Constraint(expr= -(-0.85363 + m.x3)**2 - (-0.13693 + m.x6)**2 + m.x7
    <= 0)
m.e2041 = Constraint(expr= -(-0.50497 + m.x3)**2 - (-0.14767 + m.x6)**2 + m.x7
    <= 0)
m.e2042 = Constraint(expr= -(-0.22843 + m.x3)**2 - (-0.37973 + m.x6)**2 + m.x7
    <= 0)
m.e2043 = Constraint(expr= -(-0.18617 + m.x3)**2 - (-0.92087 + m.x6)**2 + m.x7
    <= 0)
m.e2044 = Constraint(expr= -(-0.81123 + m.x3)**2 - (-0.11053 + m.x6)**2 + m.x7
    <= 0)
m.e2045 = Constraint(expr= -(-0.41937 + m.x3)**2 - (-0.56607 + m.x6)**2 + m.x7
    <= 0)
m.e2046 = Constraint(expr= -(-0.28203 + m.x3)**2 - (-0.80933 + m.x6)**2 + m.x7
    <= 0)
m.e2047 = Constraint(expr= -(-0.12457 + m.x3)**2 - (-0.20327 + m.x6)**2 + m.x7
    <= 0)
m.e2048 = Constraint(expr= -(-0.12083 + m.x3)**2 - (-0.75613 + m.x6)**2 + m.x7
    <= 0)
m.e2049 = Constraint(expr= -(-0.42177 + m.x3)**2 - (-0.15247 + m.x6)**2 + m.x7
    <= 0)
m.e2050 = Constraint(expr= -(-0.60763 + m.x3)**2 - (-0.03093 + m.x6)**2 + m.x7
    <= 0)
m.e2051 = Constraint(expr= -(-0.63097 + m.x3)**2 - (-0.93367 + m.x6)**2 + m.x7
    <= 0)
m.e2052 = Constraint(expr= -(-0.82243 + m.x3)**2 - (-0.51373 + m.x6)**2 + m.x7
    <= 0)
m.e2053 = Constraint(expr= -(-0.27217 + m.x3)**2 - (-0.26687 + m.x6)**2 + m.x7
    <= 0)
m.e2054 = Constraint(expr= -(-0.64523 + m.x3)**2 - (-0.88453 + m.x6)**2 + m.x7
    <= 0)
m.e2055 = Constraint(expr= -(-0.06537 + m.x3)**2 - (-0.07207 + m.x6)**2 + m.x7
    <= 0)
m.e2056 = Constraint(expr= -(-0.75603 + m.x3)**2 - (-0.62333 + m.x6)**2 + m.x7
    <= 0)
m.e2057 = Constraint(expr= -(-0.93057 + m.x3)**2 - (-0.46927 + m.x6)**2 + m.x7
    <= 0)
m.e2058 = Constraint(expr= -(-0.63483 + m.x3)**2 - (-0.01013 + m.x6)**2 + m.x7
    <= 0)
m.e2059 = Constraint(expr= -(-0.98777 + m.x3)**2 - (-0.77847 + m.x6)**2 + m.x7
    <= 0)
m.e2060 = Constraint(expr= -(-0.56163 + m.x3)**2 - (-0.12493 + m.x6)**2 + m.x7
    <= 0)
m.e2061 = Constraint(expr= -(-0.55697 + m.x3)**2 - (-0.51967 + m.x6)**2 + m.x7
    <= 0)
m.e2062 = Constraint(expr= -(-0.61643 + m.x3)**2 - (-0.84773 + m.x6)**2 + m.x7
    <= 0)
m.e2063 = Constraint(expr= -(-0.15817 + m.x3)**2 - (-0.41287 + m.x6)**2 + m.x7
    <= 0)
m.e2064 = Constraint(expr= -(-0.67923 + m.x3)**2 - (-0.85853 + m.x6)**2 + m.x7
    <= 0)
m.e2065 = Constraint(expr= -(-0.51137 + m.x3)**2 - (-0.37807 + m.x6)**2 + m.x7
    <= 0)
m.e2066 = Constraint(expr= -(-0.43003 + m.x3)**2 - (-0.63733 + m.x6)**2 + m.x7
    <= 0)
m.e2067 = Constraint(expr= -(-0.53657 + m.x3)**2 - (-0.53527 + m.x6)**2 + m.x7
    <= 0)
m.e2068 = Constraint(expr= -(-0.34883 + m.x3)**2 - (-0.46413 + m.x6)**2 + m.x7
    <= 0)
m.e2069 = Constraint(expr= -(-0.35377 + m.x3)**2 - (-0.20447 + m.x6)**2 + m.x7
    <= 0)
m.e2070 = Constraint(expr= -(-0.71563 + m.x3)**2 - (-0.41893 + m.x6)**2 + m.x7
    <= 0)
m.e2071 = Constraint(expr= -(-0.28297 + m.x3)**2 - (-0.90567 + m.x6)**2 + m.x7
    <= 0)
m.e2072 = Constraint(expr= -(-0.61043 + m.x3)**2 - (-0.38173 + m.x6)**2 + m.x7
    <= 0)
m.e2073 = Constraint(expr= -(-0.84417 + m.x3)**2 - (-0.35887 + m.x6)**2 + m.x7
    <= 0)
m.e2074 = Constraint(expr= -(-0.91323 + m.x3)**2 - (-0.03253 + m.x6)**2 + m.x7
    <= 0)
m.e2075 = Constraint(expr= -(-0.75737 + m.x3)**2 - (-0.48407 + m.x6)**2 + m.x7
    <= 0)
m.e2076 = Constraint(expr= -(-0.30403 + m.x3)**2 - (-0.85133 + m.x6)**2 + m.x7
    <= 0)
m.e2077 = Constraint(expr= -(-0.94257 + m.x3)**2 - (-0.40127 + m.x6)**2 + m.x7
    <= 0)
m.e2078 = Constraint(expr= -(-0.26283 + m.x3)**2 - (-0.11813 + m.x6)**2 + m.x7
    <= 0)
m.e2079 = Constraint(expr= -(-0.51977 + m.x3)**2 - (-0.43047 + m.x6)**2 + m.x7
    <= 0)
m.e2080 = Constraint(expr= -(-0.06963 + m.x3)**2 - (-0.91293 + m.x6)**2 + m.x7
    <= 0)
m.e2081 = Constraint(expr= -(-0.80897 + m.x3)**2 - (-0.09167 + m.x6)**2 + m.x7
    <= 0)
m.e2082 = Constraint(expr= -(-0.80443 + m.x3)**2 - (-0.11573 + m.x6)**2 + m.x7
    <= 0)
m.e2083 = Constraint(expr= -(-0.33017 + m.x3)**2 - (-0.10487 + m.x6)**2 + m.x7
    <= 0)
m.e2084 = Constraint(expr= -(-0.34723 + m.x3)**2 - (-0.40653 + m.x6)**2 + m.x7
    <= 0)
m.e2085 = Constraint(expr= -(-0.80337 + m.x3)**2 - (-0.39007 + m.x6)**2 + m.x7
    <= 0)
m.e2086 = Constraint(expr= -(-0.37803 + m.x3)**2 - (-0.26533 + m.x6)**2 + m.x7
    <= 0)
m.e2087 = Constraint(expr= -(-0.14857 + m.x3)**2 - (-0.06727 + m.x6)**2 + m.x7
    <= 0)
m.e2088 = Constraint(expr= -(-0.37683 + m.x3)**2 - (-0.97213 + m.x6)**2 + m.x7
    <= 0)
m.e2089 = Constraint(expr= -(-0.48577 + m.x3)**2 - (-0.45647 + m.x6)**2 + m.x7
    <= 0)
m.e2090 = Constraint(expr= -(-0.62363 + m.x3)**2 - (-0.60693 + m.x6)**2 + m.x7
    <= 0)
m.e2091 = Constraint(expr= -(-0.13497 + m.x3)**2 - (-0.07767 + m.x6)**2 + m.x7
    <= 0)
m.e2092 = Constraint(expr= -(-0.19843 + m.x3)**2 - (-0.04973 + m.x6)**2 + m.x7
    <= 0)
m.e2093 = Constraint(expr= -(-0.61617 + m.x3)**2 - (-0.65087 + m.x6)**2 + m.x7
    <= 0)
m.e2094 = Constraint(expr= -(-0.98123 + m.x3)**2 - (-0.98053 + m.x6)**2 + m.x7
    <= 0)
m.e2095 = Constraint(expr= -(-0.64937 + m.x3)**2 - (-0.09607 + m.x6)**2 + m.x7
    <= 0)
m.e2096 = Constraint(expr= -(-0.65203 + m.x3)**2 - (-0.87933 + m.x6)**2 + m.x7
    <= 0)
m.e2097 = Constraint(expr= -(-0.15457 + m.x3)**2 - (-0.53327 + m.x6)**2 + m.x7
    <= 0)
m.e2098 = Constraint(expr= -(-0.69083 + m.x3)**2 - (-0.02613 + m.x6)**2 + m.x7
    <= 0)
m.e2099 = Constraint(expr= -(-0.25177 + m.x3)**2 - (-0.28247 + m.x6)**2 + m.x7
    <= 0)
m.e2100 = Constraint(expr= -(-0.37763 + m.x3)**2 - (-0.50093 + m.x6)**2 + m.x7
    <= 0)
m.e2101 = Constraint(expr= -(-0.26097 + m.x3)**2 - (-0.86367 + m.x6)**2 + m.x7
    <= 0)
m.e2102 = Constraint(expr= -(-0.79243 + m.x3)**2 - (-0.18373 + m.x6)**2 + m.x7
    <= 0)
m.e2103 = Constraint(expr= -(-0.70217 + m.x3)**2 - (-0.99687 + m.x6)**2 + m.x7
    <= 0)
m.e2104 = Constraint(expr= -(-0.81523 + m.x3)**2 - (-0.75453 + m.x6)**2 + m.x7
    <= 0)
m.e2105 = Constraint(expr= -(-0.29537 + m.x3)**2 - (-0.60207 + m.x6)**2 + m.x7
    <= 0)
m.e2106 = Constraint(expr= -(-0.12603 + m.x3)**2 - (-0.69333 + m.x6)**2 + m.x7
    <= 0)
m.e2107 = Constraint(expr= -(-0.96057 + m.x3)**2 - (-0.79927 + m.x6)**2 + m.x7
    <= 0)
m.e2108 = Constraint(expr= -(-0.20483 + m.x3)**2 - (-0.28013 + m.x6)**2 + m.x7
    <= 0)
m.e2109 = Constraint(expr= -(-0.81777 + m.x3)**2 - (-0.90847 + m.x6)**2 + m.x7
    <= 0)
m.e2110 = Constraint(expr= -(-0.33163 + m.x3)**2 - (-0.59493 + m.x6)**2 + m.x7
    <= 0)
m.e2111 = Constraint(expr= -(-0.18697 + m.x3)**2 - (-0.44967 + m.x6)**2 + m.x7
    <= 0)
m.e2112 = Constraint(expr= -(-0.58643 + m.x3)**2 - (-0.51773 + m.x6)**2 + m.x7
    <= 0)
m.e2113 = Constraint(expr= -(-0.58817 + m.x3)**2 - (-0.14287 + m.x6)**2 + m.x7
    <= 0)
m.e2114 = Constraint(expr= -(-0.84923 + m.x3)**2 - (-0.72853 + m.x6)**2 + m.x7
    <= 0)
m.e2115 = Constraint(expr= -(-0.74137 + m.x3)**2 - (-0.90807 + m.x6)**2 + m.x7
    <= 0)
m.e2116 = Constraint(expr= -(-0.80003 + m.x3)**2 - (-0.70733 + m.x6)**2 + m.x7
    <= 0)
m.e2117 = Constraint(expr= -(-0.56657 + m.x3)**2 - (-0.86527 + m.x6)**2 + m.x7
    <= 0)
m.e2118 = Constraint(expr= -(-0.91883 + m.x3)**2 - (-0.73413 + m.x6)**2 + m.x7
    <= 0)
m.e2119 = Constraint(expr= -(-0.18377 + m.x3)**2 - (-0.33447 + m.x6)**2 + m.x7
    <= 0)
m.e2120 = Constraint(expr= -(-0.48563 + m.x3)**2 - (-0.88893 + m.x6)**2 + m.x7
    <= 0)
m.e2121 = Constraint(expr= -(-0.91297 + m.x3)**2 - (-0.83567 + m.x6)**2 + m.x7
    <= 0)
m.e2122 = Constraint(expr= -(-0.58043 + m.x3)**2 - (-0.05173 + m.x6)**2 + m.x7
    <= 0)
m.e2123 = Constraint(expr= -(-0.27417 + m.x3)**2 - (-0.08887 + m.x6)**2 + m.x7
    <= 0)
m.e2124 = Constraint(expr= -(-0.08323 + m.x3)**2 - (-0.90253 + m.x6)**2 + m.x7
    <= 0)
m.e2125 = Constraint(expr= -(-0.98737 + m.x3)**2 - (-0.01407 + m.x6)**2 + m.x7
    <= 0)
m.e2126 = Constraint(expr= -(-0.67403 + m.x3)**2 - (-0.92133 + m.x6)**2 + m.x7
    <= 0)
m.e2127 = Constraint(expr= -(-0.97257 + m.x3)**2 - (-0.73127 + m.x6)**2 + m.x7
    <= 0)
m.e2128 = Constraint(expr= -(-0.83283 + m.x3)**2 - (-0.38813 + m.x6)**2 + m.x7
    <= 0)
m.e2129 = Constraint(expr= -(-0.34977 + m.x3)**2 - (-0.56047 + m.x6)**2 + m.x7
    <= 0)
m.e2130 = Constraint(expr= -(-0.83963 + m.x3)**2 - (-0.38293 + m.x6)**2 + m.x7
    <= 0)
m.e2131 = Constraint(expr= -(-0.43897 + m.x3)**2 - (-0.02167 + m.x6)**2 + m.x7
    <= 0)
m.e2132 = Constraint(expr= -(-0.77443 + m.x3)**2 - (-0.78573 + m.x6)**2 + m.x7
    <= 0)
m.e2133 = Constraint(expr= -(-0.76017 + m.x3)**2 - (-0.83487 + m.x6)**2 + m.x7
    <= 0)
m.e2134 = Constraint(expr= -(-0.51723 + m.x3)**2 - (-0.27653 + m.x6)**2 + m.x7
    <= 0)
m.e2135 = Constraint(expr= -(-0.03337 + m.x3)**2 - (-0.92007 + m.x6)**2 + m.x7
    <= 0)
m.e2136 = Constraint(expr= -(-0.74803 + m.x3)**2 - (-0.33533 + m.x6)**2 + m.x7
    <= 0)
m.e2137 = Constraint(expr= -(-0.17857 + m.x3)**2 - (-0.39727 + m.x6)**2 + m.x7
    <= 0)
m.e2138 = Constraint(expr= -(-0.94683 + m.x3)**2 - (-0.24213 + m.x6)**2 + m.x7
    <= 0)
m.e2139 = Constraint(expr= -(-0.31577 + m.x3)**2 - (-0.58647 + m.x6)**2 + m.x7
    <= 0)
m.e2140 = Constraint(expr= -(-0.39363 + m.x3)**2 - (-0.07693 + m.x6)**2 + m.x7
    <= 0)
m.e2141 = Constraint(expr= -(-0.76497 + m.x3)**2 - (-0.00767 + m.x6)**2 + m.x7
    <= 0)
m.e2142 = Constraint(expr= -(-0.16843 + m.x3)**2 - (-0.71973 + m.x6)**2 + m.x7
    <= 0)
m.e2143 = Constraint(expr= -(-0.04617 + m.x3)**2 - (-0.38087 + m.x6)**2 + m.x7
    <= 0)
m.e2144 = Constraint(expr= -(-0.15123 + m.x3)**2 - (-0.85053 + m.x6)**2 + m.x7
    <= 0)
m.e2145 = Constraint(expr= -(-0.87937 + m.x3)**2 - (-0.62607 + m.x6)**2 + m.x7
    <= 0)
m.e2146 = Constraint(expr= -(-0.02203 + m.x3)**2 - (-0.94933 + m.x6)**2 + m.x7
    <= 0)
m.e2147 = Constraint(expr= -(-0.18457 + m.x3)**2 - (-0.86327 + m.x6)**2 + m.x7
    <= 0)
m.e2148 = Constraint(expr= -(-0.26083 + m.x3)**2 - (-0.29613 + m.x6)**2 + m.x7
    <= 0)
m.e2149 = Constraint(expr= -(-0.08177 + m.x3)**2 - (-0.41247 + m.x6)**2 + m.x7
    <= 0)
m.e2150 = Constraint(expr= -(-0.14763 + m.x3)**2 - (-0.97093 + m.x6)**2 + m.x7
    <= 0)
m.e2151 = Constraint(expr= -(-0.89097 + m.x3)**2 - (-0.79367 + m.x6)**2 + m.x7
    <= 0)
m.e2152 = Constraint(expr= -(-0.76243 + m.x3)**2 - (-0.85373 + m.x6)**2 + m.x7
    <= 0)
m.e2153 = Constraint(expr= -(-0.13217 + m.x3)**2 - (-0.72687 + m.x6)**2 + m.x7
    <= 0)
m.e2154 = Constraint(expr= -(-0.98523 + m.x3)**2 - (-0.62453 + m.x6)**2 + m.x7
    <= 0)
m.e2155 = Constraint(expr= -(-0.52537 + m.x3)**2 - (-0.13207 + m.x6)**2 + m.x7
    <= 0)
m.e2156 = Constraint(expr= -(-0.49603 + m.x3)**2 - (-0.76333 + m.x6)**2 + m.x7
    <= 0)
m.e2157 = Constraint(expr= -(-0.99057 + m.x3)**2 - (-0.12927 + m.x6)**2 + m.x7
    <= 0)
m.e2158 = Constraint(expr= -(-0.77483 + m.x3)**2 - (-0.55013 + m.x6)**2 + m.x7
    <= 0)
m.e2159 = Constraint(expr= -(-0.64777 + m.x3)**2 - (-0.03847 + m.x6)**2 + m.x7
    <= 0)
m.e2160 = Constraint(expr= -(-0.10163 + m.x3)**2 - (-0.06493 + m.x6)**2 + m.x7
    <= 0)
m.e2161 = Constraint(expr= -(-0.81697 + m.x3)**2 - (-0.37967 + m.x6)**2 + m.x7
    <= 0)
m.e2162 = Constraint(expr= -(-0.55643 + m.x3)**2 - (-0.18773 + m.x6)**2 + m.x7
    <= 0)
m.e2163 = Constraint(expr= -(-0.01817 + m.x3)**2 - (-0.87287 + m.x6)**2 + m.x7
    <= 0)
m.e2164 = Constraint(expr= -(-0.01923 + m.x3)**2 - (-0.59853 + m.x6)**2 + m.x7
    <= 0)
m.e2165 = Constraint(expr= -(-0.97137 + m.x3)**2 - (-0.43807 + m.x6)**2 + m.x7
    <= 0)
m.e2166 = Constraint(expr= -(-0.17003 + m.x3)**2 - (-0.77733 + m.x6)**2 + m.x7
    <= 0)
m.e2167 = Constraint(expr= -(-0.59657 + m.x3)**2 - (-0.19527 + m.x6)**2 + m.x7
    <= 0)
m.e2168 = Constraint(expr= -(-0.48883 + m.x3)**2 - (-0.00413 + m.x6)**2 + m.x7
    <= 0)
m.e2169 = Constraint(expr= -(-0.01377 + m.x3)**2 - (-0.46447 + m.x6)**2 + m.x7
    <= 0)
m.e2170 = Constraint(expr= -(-0.25563 + m.x3)**2 - (-0.35893 + m.x6)**2 + m.x7
    <= 0)
m.e2171 = Constraint(expr= -(-0.54297 + m.x3)**2 - (-0.76567 + m.x6)**2 + m.x7
    <= 0)
m.e2172 = Constraint(expr= -(-0.55043 + m.x3)**2 - (-0.72173 + m.x6)**2 + m.x7
    <= 0)
m.e2173 = Constraint(expr= -(-0.70417 + m.x3)**2 - (-0.81887 + m.x6)**2 + m.x7
    <= 0)
m.e2174 = Constraint(expr= -(-0.25323 + m.x3)**2 - (-0.77253 + m.x6)**2 + m.x7
    <= 0)
m.e2175 = Constraint(expr= -(-0.21737 + m.x3)**2 - (-0.54407 + m.x6)**2 + m.x7
    <= 0)
m.e2176 = Constraint(expr= -(-0.04403 + m.x3)**2 - (-0.99133 + m.x6)**2 + m.x7
    <= 0)
m.e2177 = Constraint(expr= -(-0.00257 + m.x3)**2 - (-0.06127 + m.x6)**2 + m.x7
    <= 0)
m.e2178 = Constraint(expr= -(-0.40283 + m.x3)**2 - (-0.65813 + m.x6)**2 + m.x7
    <= 0)
m.e2179 = Constraint(expr= -(-0.17977 + m.x3)**2 - (-0.69047 + m.x6)**2 + m.x7
    <= 0)
m.e2180 = Constraint(expr= -(-0.60963 + m.x3)**2 - (-0.85293 + m.x6)**2 + m.x7
    <= 0)
m.e2181 = Constraint(expr= -(-0.06897 + m.x3)**2 - (-0.95167 + m.x6)**2 + m.x7
    <= 0)
m.e2182 = Constraint(expr= -(-0.74443 + m.x3)**2 - (-0.45573 + m.x6)**2 + m.x7
    <= 0)
m.e2183 = Constraint(expr= -(-0.19017 + m.x3)**2 - (-0.56487 + m.x6)**2 + m.x7
    <= 0)
m.e2184 = Constraint(expr= -(-0.68723 + m.x3)**2 - (-0.14653 + m.x6)**2 + m.x7
    <= 0)
m.e2185 = Constraint(expr= -(-0.26337 + m.x3)**2 - (-0.45007 + m.x6)**2 + m.x7
    <= 0)
m.e2186 = Constraint(expr= -(-0.11803 + m.x3)**2 - (-0.40533 + m.x6)**2 + m.x7
    <= 0)
m.e2187 = Constraint(expr= -(-0.20857 + m.x3)**2 - (-0.72727 + m.x6)**2 + m.x7
    <= 0)
m.e2188 = Constraint(expr= -(-0.51683 + m.x3)**2 - (-0.51213 + m.x6)**2 + m.x7
    <= 0)
m.e2189 = Constraint(expr= -(-0.14577 + m.x3)**2 - (-0.71647 + m.x6)**2 + m.x7
    <= 0)
m.e2190 = Constraint(expr= -(-0.16363 + m.x3)**2 - (-0.54693 + m.x6)**2 + m.x7
    <= 0)
m.e2191 = Constraint(expr= -(-0.39497 + m.x3)**2 - (-0.93767 + m.x6)**2 + m.x7
    <= 0)
m.e2192 = Constraint(expr= -(-0.13843 + m.x3)**2 - (-0.38973 + m.x6)**2 + m.x7
    <= 0)
m.e2193 = Constraint(expr= -(-0.47617 + m.x3)**2 - (-0.11087 + m.x6)**2 + m.x7
    <= 0)
m.e2194 = Constraint(expr= -(-0.32123 + m.x3)**2 - (-0.72053 + m.x6)**2 + m.x7
    <= 0)
m.e2195 = Constraint(expr= -(-0.10937 + m.x3)**2 - (-0.15607 + m.x6)**2 + m.x7
    <= 0)
m.e2196 = Constraint(expr= -(-0.39203 + m.x3)**2 - (-0.01933 + m.x6)**2 + m.x7
    <= 0)
m.e2197 = Constraint(expr= -(-0.21457 + m.x3)**2 - (-0.19327 + m.x6)**2 + m.x7
    <= 0)
m.e2198 = Constraint(expr= -(-0.83083 + m.x3)**2 - (-0.56613 + m.x6)**2 + m.x7
    <= 0)
m.e2199 = Constraint(expr= -(-0.91177 + m.x3)**2 - (-0.54247 + m.x6)**2 + m.x7
    <= 0)
m.e2200 = Constraint(expr= -(-0.91763 + m.x3)**2 - (-0.44093 + m.x6)**2 + m.x7
    <= 0)
m.e2201 = Constraint(expr= -(-0.52097 + m.x3)**2 - (-0.72367 + m.x6)**2 + m.x7
    <= 0)
m.e2202 = Constraint(expr= -(-0.73243 + m.x3)**2 - (-0.52373 + m.x6)**2 + m.x7
    <= 0)
m.e2203 = Constraint(expr= -(-0.56217 + m.x3)**2 - (-0.45687 + m.x6)**2 + m.x7
    <= 0)
m.e2204 = Constraint(expr= -(-0.15523 + m.x3)**2 - (-0.49453 + m.x6)**2 + m.x7
    <= 0)
m.e2205 = Constraint(expr= -(-0.75537 + m.x3)**2 - (-0.66207 + m.x6)**2 + m.x7
    <= 0)
m.e2206 = Constraint(expr= -(-0.86603 + m.x3)**2 - (-0.83333 + m.x6)**2 + m.x7
    <= 0)
m.e2207 = Constraint(expr= -(-0.02057 + m.x3)**2 - (-0.45927 + m.x6)**2 + m.x7
    <= 0)
m.e2208 = Constraint(expr= -(-0.34483 + m.x3)**2 - (-0.82013 + m.x6)**2 + m.x7
    <= 0)
m.e2209 = Constraint(expr= -(-0.47777 + m.x3)**2 - (-0.16847 + m.x6)**2 + m.x7
    <= 0)
m.e2210 = Constraint(expr= -(-0.87163 + m.x3)**2 - (-0.53493 + m.x6)**2 + m.x7
    <= 0)
m.e2211 = Constraint(expr= -(-0.44697 + m.x3)**2 - (-0.30967 + m.x6)**2 + m.x7
    <= 0)
m.e2212 = Constraint(expr= -(-0.52643 + m.x3)**2 - (-0.85773 + m.x6)**2 + m.x7
    <= 0)
m.e2213 = Constraint(expr= -(-0.44817 + m.x3)**2 - (-0.60287 + m.x6)**2 + m.x7
    <= 0)
m.e2214 = Constraint(expr= -(-0.18923 + m.x3)**2 - (-0.46853 + m.x6)**2 + m.x7
    <= 0)
m.e2215 = Constraint(expr= -(-0.20137 + m.x3)**2 - (-0.96807 + m.x6)**2 + m.x7
    <= 0)
m.e2216 = Constraint(expr= -(-0.54003 + m.x3)**2 - (-0.84733 + m.x6)**2 + m.x7
    <= 0)
m.e2217 = Constraint(expr= -(-0.62657 + m.x3)**2 - (-0.52527 + m.x6)**2 + m.x7
    <= 0)
m.e2218 = Constraint(expr= -(-0.05883 + m.x3)**2 - (-0.27413 + m.x6)**2 + m.x7
    <= 0)
m.e2219 = Constraint(expr= -(-0.84377 + m.x3)**2 - (-0.59447 + m.x6)**2 + m.x7
    <= 0)
m.e2220 = Constraint(expr= -(-0.02563 + m.x3)**2 - (-0.82893 + m.x6)**2 + m.x7
    <= 0)
m.e2221 = Constraint(expr= -(-0.17297 + m.x3)**2 - (-0.69567 + m.x6)**2 + m.x7
    <= 0)
m.e2222 = Constraint(expr= -(-0.52043 + m.x3)**2 - (-0.39173 + m.x6)**2 + m.x7
    <= 0)
m.e2223 = Constraint(expr= -(-0.13417 + m.x3)**2 - (-0.54887 + m.x6)**2 + m.x7
    <= 0)
m.e2224 = Constraint(expr= -(-0.42323 + m.x3)**2 - (-0.64253 + m.x6)**2 + m.x7
    <= 0)
m.e2225 = Constraint(expr= -(-0.44737 + m.x3)**2 - (-0.07407 + m.x6)**2 + m.x7
    <= 0)
m.e2226 = Constraint(expr= -(-0.41403 + m.x3)**2 - (-0.06133 + m.x6)**2 + m.x7
    <= 0)
m.e2227 = Constraint(expr= -(-0.03257 + m.x3)**2 - (-0.39127 + m.x6)**2 + m.x7
    <= 0)
m.e2228 = Constraint(expr= -(-0.97283 + m.x3)**2 - (-0.92813 + m.x6)**2 + m.x7
    <= 0)
m.e2229 = Constraint(expr= -(-0.00977 + m.x3)**2 - (-0.82047 + m.x6)**2 + m.x7
    <= 0)
m.e2230 = Constraint(expr= -(-0.37963 + m.x3)**2 - (-0.32293 + m.x6)**2 + m.x7
    <= 0)
m.e2231 = Constraint(expr= -(-0.69897 + m.x3)**2 - (-0.88167 + m.x6)**2 + m.x7
    <= 0)
m.e2232 = Constraint(expr= -(-0.71443 + m.x3)**2 - (-0.12573 + m.x6)**2 + m.x7
    <= 0)
m.e2233 = Constraint(expr= -(-0.62017 + m.x3)**2 - (-0.29487 + m.x6)**2 + m.x7
    <= 0)
m.e2234 = Constraint(expr= -(-0.85723 + m.x3)**2 - (-0.01653 + m.x6)**2 + m.x7
    <= 0)
m.e2235 = Constraint(expr= -(-0.49337 + m.x3)**2 - (-0.98007 + m.x6)**2 + m.x7
    <= 0)
m.e2236 = Constraint(expr= -(-0.48803 + m.x3)**2 - (-0.47533 + m.x6)**2 + m.x7
    <= 0)
m.e2237 = Constraint(expr= -(-0.23857 + m.x3)**2 - (-0.05727 + m.x6)**2 + m.x7
    <= 0)
m.e2238 = Constraint(expr= -(-0.08683 + m.x3)**2 - (-0.78213 + m.x6)**2 + m.x7
    <= 0)
m.e2239 = Constraint(expr= -(-0.97577 + m.x3)**2 - (-0.84647 + m.x6)**2 + m.x7
    <= 0)
m.e2240 = Constraint(expr= -(-0.93363 + m.x3)**2 - (-0.01693 + m.x6)**2 + m.x7
    <= 0)
m.e2241 = Constraint(expr= -(-0.02497 + m.x3)**2 - (-0.86767 + m.x6)**2 + m.x7
    <= 0)
m.e2242 = Constraint(expr= -(-0.10843 + m.x3)**2 - (-0.05973 + m.x6)**2 + m.x7
    <= 0)
m.e2243 = Constraint(expr= -(-0.90617 + m.x3)**2 - (-0.84087 + m.x6)**2 + m.x7
    <= 0)
m.e2244 = Constraint(expr= -(-0.49123 + m.x3)**2 - (-0.59053 + m.x6)**2 + m.x7
    <= 0)
m.e2245 = Constraint(expr= -(-0.33937 + m.x3)**2 - (-0.68607 + m.x6)**2 + m.x7
    <= 0)
m.e2246 = Constraint(expr= -(-0.76203 + m.x3)**2 - (-0.08933 + m.x6)**2 + m.x7
    <= 0)
m.e2247 = Constraint(expr= -(-0.24457 + m.x3)**2 - (-0.52327 + m.x6)**2 + m.x7
    <= 0)
m.e2248 = Constraint(expr= -(-0.40083 + m.x3)**2 - (-0.83613 + m.x6)**2 + m.x7
    <= 0)
m.e2249 = Constraint(expr= -(-0.74177 + m.x3)**2 - (-0.67247 + m.x6)**2 + m.x7
    <= 0)
m.e2250 = Constraint(expr= -(-0.68763 + m.x3)**2 - (-0.91093 + m.x6)**2 + m.x7
    <= 0)
m.e2251 = Constraint(expr= -(-0.15097 + m.x3)**2 - (-0.65367 + m.x6)**2 + m.x7
    <= 0)
m.e2252 = Constraint(expr= -(-0.70243 + m.x3)**2 - (-0.19373 + m.x6)**2 + m.x7
    <= 0)
m.e2253 = Constraint(expr= -(-0.99217 + m.x3)**2 - (-0.18687 + m.x6)**2 + m.x7
    <= 0)
m.e2254 = Constraint(expr= -(-0.32523 + m.x3)**2 - (-0.36453 + m.x6)**2 + m.x7
    <= 0)
m.e2255 = Constraint(expr= -(-0.98537 + m.x3)**2 - (-0.19207 + m.x6)**2 + m.x7
    <= 0)
m.e2256 = Constraint(expr= -(-0.23603 + m.x3)**2 - (-0.90333 + m.x6)**2 + m.x7
    <= 0)
m.e2257 = Constraint(expr= -(-0.05057 + m.x3)**2 - (-0.78927 + m.x6)**2 + m.x7
    <= 0)
m.e2258 = Constraint(expr= -(-0.91483 + m.x3)**2 - (-0.09013 + m.x6)**2 + m.x7
    <= 0)
m.e2259 = Constraint(expr= -(-0.30777 + m.x3)**2 - (-0.29847 + m.x6)**2 + m.x7
    <= 0)
m.e2260 = Constraint(expr= -(-0.64163 + m.x3)**2 - (-0.00493 + m.x6)**2 + m.x7
    <= 0)
m.e2261 = Constraint(expr= -(-0.07697 + m.x3)**2 - (-0.23967 + m.x6)**2 + m.x7
    <= 0)
m.e2262 = Constraint(expr= -(-0.49643 + m.x3)**2 - (-0.52773 + m.x6)**2 + m.x7
    <= 0)
m.e2263 = Constraint(expr= -(-0.87817 + m.x3)**2 - (-0.33287 + m.x6)**2 + m.x7
    <= 0)
m.e2264 = Constraint(expr= -(-0.35923 + m.x3)**2 - (-0.33853 + m.x6)**2 + m.x7
    <= 0)
m.e2265 = Constraint(expr= -(-0.43137 + m.x3)**2 - (-0.49807 + m.x6)**2 + m.x7
    <= 0)
m.e2266 = Constraint(expr= -(-0.91003 + m.x3)**2 - (-0.91733 + m.x6)**2 + m.x7
    <= 0)
m.e2267 = Constraint(expr= -(-0.65657 + m.x3)**2 - (-0.85527 + m.x6)**2 + m.x7
    <= 0)
m.e2268 = Constraint(expr= -(-0.62883 + m.x3)**2 - (-0.54413 + m.x6)**2 + m.x7
    <= 0)
m.e2269 = Constraint(expr= -(-0.67377 + m.x3)**2 - (-0.72447 + m.x6)**2 + m.x7
    <= 0)
m.e2270 = Constraint(expr= -(-0.79563 + m.x3)**2 - (-0.29893 + m.x6)**2 + m.x7
    <= 0)
m.e2271 = Constraint(expr= -(-0.80297 + m.x3)**2 - (-0.62567 + m.x6)**2 + m.x7
    <= 0)
m.e2272 = Constraint(expr= -(-0.49043 + m.x3)**2 - (-0.06173 + m.x6)**2 + m.x7
    <= 0)
m.e2273 = Constraint(expr= -(-0.56417 + m.x3)**2 - (-0.27887 + m.x6)**2 + m.x7
    <= 0)
m.e2274 = Constraint(expr= -(-0.59323 + m.x3)**2 - (-0.51253 + m.x6)**2 + m.x7
    <= 0)
m.e2275 = Constraint(expr= -(-0.67737 + m.x3)**2 - (-0.60407 + m.x6)**2 + m.x7
    <= 0)
m.e2276 = Constraint(expr= -(-0.78403 + m.x3)**2 - (-0.13133 + m.x6)**2 + m.x7
    <= 0)
m.e2277 = Constraint(expr= -(-0.06257 + m.x3)**2 - (-0.72127 + m.x6)**2 + m.x7
    <= 0)
m.e2278 = Constraint(expr= -(-0.54283 + m.x3)**2 - (-0.19813 + m.x6)**2 + m.x7
    <= 0)
m.e2279 = Constraint(expr= -(-0.83977 + m.x3)**2 - (-0.95047 + m.x6)**2 + m.x7
    <= 0)
m.e2280 = Constraint(expr= -(-0.14963 + m.x3)**2 - (-0.79293 + m.x6)**2 + m.x7
    <= 0)
m.e2281 = Constraint(expr= -(-0.32897 + m.x3)**2 - (-0.81167 + m.x6)**2 + m.x7
    <= 0)
m.e2282 = Constraint(expr= -(-0.68443 + m.x3)**2 - (-0.79573 + m.x6)**2 + m.x7
    <= 0)
m.e2283 = Constraint(expr= -(-0.05017 + m.x3)**2 - (-0.02487 + m.x6)**2 + m.x7
    <= 0)
m.e2284 = Constraint(expr= -(-0.02723 + m.x3)**2 - (-0.88653 + m.x6)**2 + m.x7
    <= 0)
m.e2285 = Constraint(expr= -(-0.72337 + m.x3)**2 - (-0.51007 + m.x6)**2 + m.x7
    <= 0)
m.e2286 = Constraint(expr= -(-0.85803 + m.x3)**2 - (-0.54533 + m.x6)**2 + m.x7
    <= 0)
m.e2287 = Constraint(expr= -(-0.26857 + m.x3)**2 - (-0.38727 + m.x6)**2 + m.x7
    <= 0)
m.e2288 = Constraint(expr= -(-0.65683 + m.x3)**2 - (-0.05213 + m.x6)**2 + m.x7
    <= 0)
m.e2289 = Constraint(expr= -(-0.80577 + m.x3)**2 - (-0.97647 + m.x6)**2 + m.x7
    <= 0)
m.e2290 = Constraint(expr= -(-0.70363 + m.x3)**2 - (-0.48693 + m.x6)**2 + m.x7
    <= 0)
m.e2291 = Constraint(expr= -(-0.65497 + m.x3)**2 - (-0.79767 + m.x6)**2 + m.x7
    <= 0)
m.e2292 = Constraint(expr= -(-0.07843 + m.x3)**2 - (-0.72973 + m.x6)**2 + m.x7
    <= 0)
m.e2293 = Constraint(expr= -(-0.33617 + m.x3)**2 - (-0.57087 + m.x6)**2 + m.x7
    <= 0)
m.e2294 = Constraint(expr= -(-0.66123 + m.x3)**2 - (-0.46053 + m.x6)**2 + m.x7
    <= 0)
m.e2295 = Constraint(expr= -(-0.56937 + m.x3)**2 - (-0.21607 + m.x6)**2 + m.x7
    <= 0)
m.e2296 = Constraint(expr= -(-0.13203 + m.x3)**2 - (-0.15933 + m.x6)**2 + m.x7
    <= 0)
m.e2297 = Constraint(expr= -(-0.27457 + m.x3)**2 - (-0.85327 + m.x6)**2 + m.x7
    <= 0)
m.e2298 = Constraint(expr= -(-0.97083 + m.x3)**2 - (-0.10613 + m.x6)**2 + m.x7
    <= 0)
m.e2299 = Constraint(expr= -(-0.57177 + m.x3)**2 - (-0.80247 + m.x6)**2 + m.x7
    <= 0)
m.e2300 = Constraint(expr= -(-0.45763 + m.x3)**2 - (-0.38093 + m.x6)**2 + m.x7
    <= 0)
m.e2301 = Constraint(expr= -(-0.78097 + m.x3)**2 - (-0.58367 + m.x6)**2 + m.x7
    <= 0)
m.e2302 = Constraint(expr= -(-0.67243 + m.x3)**2 - (-0.86373 + m.x6)**2 + m.x7
    <= 0)
m.e2303 = Constraint(expr= -(-0.42217 + m.x3)**2 - (-0.91687 + m.x6)**2 + m.x7
    <= 0)
m.e2304 = Constraint(expr= -(-0.49523 + m.x3)**2 - (-0.23453 + m.x6)**2 + m.x7
    <= 0)
m.e2305 = Constraint(expr= -(-0.21537 + m.x3)**2 - (-0.72207 + m.x6)**2 + m.x7
    <= 0)
m.e2306 = Constraint(expr= -(-0.60603 + m.x3)**2 - (-0.97333 + m.x6)**2 + m.x7
    <= 0)
m.e2307 = Constraint(expr= -(-0.08057 + m.x3)**2 - (-0.11927 + m.x6)**2 + m.x7
    <= 0)
m.e2308 = Constraint(expr= -(-0.48483 + m.x3)**2 - (-0.36013 + m.x6)**2 + m.x7
    <= 0)
m.e2309 = Constraint(expr= -(-0.13777 + m.x3)**2 - (-0.42847 + m.x6)**2 + m.x7
    <= 0)
m.e2310 = Constraint(expr= -(-0.41163 + m.x3)**2 - (-0.47493 + m.x6)**2 + m.x7
    <= 0)
m.e2311 = Constraint(expr= -(-0.70697 + m.x3)**2 - (-0.16967 + m.x6)**2 + m.x7
    <= 0)
m.e2312 = Constraint(expr= -(-0.46643 + m.x3)**2 - (-0.19773 + m.x6)**2 + m.x7
    <= 0)
m.e2313 = Constraint(expr= -(-0.30817 + m.x3)**2 - (-0.06287 + m.x6)**2 + m.x7
    <= 0)
m.e2314 = Constraint(expr= -(-0.52923 + m.x3)**2 - (-0.20853 + m.x6)**2 + m.x7
    <= 0)
m.e2315 = Constraint(expr= -(-0.66137 + m.x3)**2 - (-0.02807 + m.x6)**2 + m.x7
    <= 0)
m.e2316 = Constraint(expr= -(-0.28003 + m.x3)**2 - (-0.98733 + m.x6)**2 + m.x7
    <= 0)
m.e2317 = Constraint(expr= -(-0.68657 + m.x3)**2 - (-0.18527 + m.x6)**2 + m.x7
    <= 0)
m.e2318 = Constraint(expr= -(-0.19883 + m.x3)**2 - (-0.81413 + m.x6)**2 + m.x7
    <= 0)
m.e2319 = Constraint(expr= -(-0.50377 + m.x3)**2 - (-0.85447 + m.x6)**2 + m.x7
    <= 0)
m.e2320 = Constraint(expr= -(-0.56563 + m.x3)**2 - (-0.76893 + m.x6)**2 + m.x7
    <= 0)
m.e2321 = Constraint(expr= -(-0.43297 + m.x3)**2 - (-0.55567 + m.x6)**2 + m.x7
    <= 0)
m.e2322 = Constraint(expr= -(-0.46043 + m.x3)**2 - (-0.73173 + m.x6)**2 + m.x7
    <= 0)
m.e2323 = Constraint(expr= -(-0.99417 + m.x3)**2 - (-0.00887 + m.x6)**2 + m.x7
    <= 0)
m.e2324 = Constraint(expr= -(-0.76323 + m.x3)**2 - (-0.38253 + m.x6)**2 + m.x7
    <= 0)
m.e2325 = Constraint(expr= -(-0.90737 + m.x3)**2 - (-0.13407 + m.x6)**2 + m.x7
    <= 0)
m.e2326 = Constraint(expr= -(-0.15403 + m.x3)**2 - (-0.20133 + m.x6)**2 + m.x7
    <= 0)
m.e2327 = Constraint(expr= -(-0.09257 + m.x3)**2 - (-0.05127 + m.x6)**2 + m.x7
    <= 0)
m.e2328 = Constraint(expr= -(-0.11283 + m.x3)**2 - (-0.46813 + m.x6)**2 + m.x7
    <= 0)
m.e2329 = Constraint(expr= -(-0.66977 + m.x3)**2 - (-0.08047 + m.x6)**2 + m.x7
    <= 0)
m.e2330 = Constraint(expr= -(-0.91963 + m.x3)**2 - (-0.26293 + m.x6)**2 + m.x7
    <= 0)
m.e2331 = Constraint(expr= -(-0.95897 + m.x3)**2 - (-0.74167 + m.x6)**2 + m.x7
    <= 0)
m.e2332 = Constraint(expr= -(-0.65443 + m.x3)**2 - (-0.46573 + m.x6)**2 + m.x7
    <= 0)
m.e2333 = Constraint(expr= -(-0.48017 + m.x3)**2 - (-0.75487 + m.x6)**2 + m.x7
    <= 0)
m.e2334 = Constraint(expr= -(-0.19723 + m.x3)**2 - (-0.75653 + m.x6)**2 + m.x7
    <= 0)
m.e2335 = Constraint(expr= -(-0.95337 + m.x3)**2 - (-0.04007 + m.x6)**2 + m.x7
    <= 0)
m.e2336 = Constraint(expr= -(-0.22803 + m.x3)**2 - (-0.61533 + m.x6)**2 + m.x7
    <= 0)
m.e2337 = Constraint(expr= -(-0.29857 + m.x3)**2 - (-0.71727 + m.x6)**2 + m.x7
    <= 0)
m.e2338 = Constraint(expr= -(-0.22683 + m.x3)**2 - (-0.32213 + m.x6)**2 + m.x7
    <= 0)
m.e2339 = Constraint(expr= -(-0.63577 + m.x3)**2 - (-0.10647 + m.x6)**2 + m.x7
    <= 0)
m.e2340 = Constraint(expr= -(-0.47363 + m.x3)**2 - (-0.95693 + m.x6)**2 + m.x7
    <= 0)
m.e2341 = Constraint(expr= -(-0.28497 + m.x3)**2 - (-0.72767 + m.x6)**2 + m.x7
    <= 0)
m.e2342 = Constraint(expr= -(-0.04843 + m.x3)**2 - (-0.39973 + m.x6)**2 + m.x7
    <= 0)
m.e2343 = Constraint(expr= -(-0.76617 + m.x3)**2 - (-0.30087 + m.x6)**2 + m.x7
    <= 0)
m.e2344 = Constraint(expr= -(-0.83123 + m.x3)**2 - (-0.33053 + m.x6)**2 + m.x7
    <= 0)
m.e2345 = Constraint(expr= -(-0.79937 + m.x3)**2 - (-0.74607 + m.x6)**2 + m.x7
    <= 0)
m.e2346 = Constraint(expr= -(-0.50203 + m.x3)**2 - (-0.22933 + m.x6)**2 + m.x7
    <= 0)
m.e2347 = Constraint(expr= -(-0.30457 + m.x3)**2 - (-0.18327 + m.x6)**2 + m.x7
    <= 0)
m.e2348 = Constraint(expr= -(-0.54083 + m.x3)**2 - (-0.37613 + m.x6)**2 + m.x7
    <= 0)
m.e2349 = Constraint(expr= -(-0.40177 + m.x3)**2 - (-0.93247 + m.x6)**2 + m.x7
    <= 0)
m.e2350 = Constraint(expr= -(-0.22763 + m.x3)**2 - (-0.85093 + m.x6)**2 + m.x7
    <= 0)
m.e2351 = Constraint(expr= -(-0.41097 + m.x3)**2 - (-0.51367 + m.x6)**2 + m.x7
    <= 0)
m.e2352 = Constraint(expr= -(-0.64243 + m.x3)**2 - (-0.53373 + m.x6)**2 + m.x7
    <= 0)
m.e2353 = Constraint(expr= -(-0.85217 + m.x3)**2 - (-0.64687 + m.x6)**2 + m.x7
    <= 0)
m.e2354 = Constraint(expr= -(-0.66523 + m.x3)**2 - (-0.10453 + m.x6)**2 + m.x7
    <= 0)
m.e2355 = Constraint(expr= -(-0.44537 + m.x3)**2 - (-0.25207 + m.x6)**2 + m.x7
    <= 0)
m.e2356 = Constraint(expr= -(-0.97603 + m.x3)**2 - (-0.04333 + m.x6)**2 + m.x7
    <= 0)
m.e2357 = Constraint(expr= -(-0.11057 + m.x3)**2 - (-0.44927 + m.x6)**2 + m.x7
    <= 0)
m.e2358 = Constraint(expr= -(-0.05483 + m.x3)**2 - (-0.63013 + m.x6)**2 + m.x7
    <= 0)
m.e2359 = Constraint(expr= -(-0.96777 + m.x3)**2 - (-0.55847 + m.x6)**2 + m.x7
    <= 0)
m.e2360 = Constraint(expr= -(-0.18163 + m.x3)**2 - (-0.94493 + m.x6)**2 + m.x7
    <= 0)
m.e2361 = Constraint(expr= -(-0.33697 + m.x3)**2 - (-0.09967 + m.x6)**2 + m.x7
    <= 0)
m.e2362 = Constraint(expr= -(-0.43643 + m.x3)**2 - (-0.86773 + m.x6)**2 + m.x7
    <= 0)
m.e2363 = Constraint(expr= -(-0.73817 + m.x3)**2 - (-0.79287 + m.x6)**2 + m.x7
    <= 0)
m.e2364 = Constraint(expr= -(-0.69923 + m.x3)**2 - (-0.07853 + m.x6)**2 + m.x7
    <= 0)
m.e2365 = Constraint(expr= -(-0.89137 + m.x3)**2 - (-0.55807 + m.x6)**2 + m.x7
    <= 0)
m.e2366 = Constraint(expr= -(-0.65003 + m.x3)**2 - (-0.05733 + m.x6)**2 + m.x7
    <= 0)
m.e2367 = Constraint(expr= -(-0.71657 + m.x3)**2 - (-0.51527 + m.x6)**2 + m.x7
    <= 0)
m.e2368 = Constraint(expr= -(-0.76883 + m.x3)**2 - (-0.08413 + m.x6)**2 + m.x7
    <= 0)
m.e2369 = Constraint(expr= -(-0.33377 + m.x3)**2 - (-0.98447 + m.x6)**2 + m.x7
    <= 0)
m.e2370 = Constraint(expr= -(-0.33563 + m.x3)**2 - (-0.23893 + m.x6)**2 + m.x7
    <= 0)
m.e2371 = Constraint(expr= -(-0.06297 + m.x3)**2 - (-0.48567 + m.x6)**2 + m.x7
    <= 0)
m.e2372 = Constraint(expr= -(-0.43043 + m.x3)**2 - (-0.40173 + m.x6)**2 + m.x7
    <= 0)
m.e2373 = Constraint(expr= -(-0.42417 + m.x3)**2 - (-0.73887 + m.x6)**2 + m.x7
    <= 0)
m.e2374 = Constraint(expr= -(-0.93323 + m.x3)**2 - (-0.25253 + m.x6)**2 + m.x7
    <= 0)
m.e2375 = Constraint(expr= -(-0.13737 + m.x3)**2 - (-0.66407 + m.x6)**2 + m.x7
    <= 0)
m.e2376 = Constraint(expr= -(-0.52403 + m.x3)**2 - (-0.27133 + m.x6)**2 + m.x7
    <= 0)
m.e2377 = Constraint(expr= -(-0.12257 + m.x3)**2 - (-0.38127 + m.x6)**2 + m.x7
    <= 0)
m.e2378 = Constraint(expr= -(-0.68283 + m.x3)**2 - (-0.73813 + m.x6)**2 + m.x7
    <= 0)
m.e2379 = Constraint(expr= -(-0.49977 + m.x3)**2 - (-0.21047 + m.x6)**2 + m.x7
    <= 0)
m.e2380 = Constraint(expr= -(-0.68963 + m.x3)**2 - (-0.73293 + m.x6)**2 + m.x7
    <= 0)
m.e2381 = Constraint(expr= -(-0.58897 + m.x3)**2 - (-0.67167 + m.x6)**2 + m.x7
    <= 0)
m.e2382 = Constraint(expr= -(-0.62443 + m.x3)**2 - (-0.13573 + m.x6)**2 + m.x7
    <= 0)
m.e2383 = Constraint(expr= -(-0.91017 + m.x3)**2 - (-0.48487 + m.x6)**2 + m.x7
    <= 0)
m.e2384 = Constraint(expr= -(-0.36723 + m.x3)**2 - (-0.62653 + m.x6)**2 + m.x7
    <= 0)
m.e2385 = Constraint(expr= -(-0.18337 + m.x3)**2 - (-0.57007 + m.x6)**2 + m.x7
    <= 0)
m.e2386 = Constraint(expr= -(-0.59803 + m.x3)**2 - (-0.68533 + m.x6)**2 + m.x7
    <= 0)
m.e2387 = Constraint(expr= -(-0.32857 + m.x3)**2 - (-0.04727 + m.x6)**2 + m.x7
    <= 0)
m.e2388 = Constraint(expr= -(-0.79683 + m.x3)**2 - (-0.59213 + m.x6)**2 + m.x7
    <= 0)
m.e2389 = Constraint(expr= -(-0.46577 + m.x3)**2 - (-0.23647 + m.x6)**2 + m.x7
    <= 0)
m.e2390 = Constraint(expr= -(-0.24363 + m.x3)**2 - (-0.42693 + m.x6)**2 + m.x7
    <= 0)
m.e2391 = Constraint(expr= -(-0.91497 + m.x3)**2 - (-0.65767 + m.x6)**2 + m.x7
    <= 0)
m.e2392 = Constraint(expr= -(-0.01843 + m.x3)**2 - (-0.06973 + m.x6)**2 + m.x7
    <= 0)
m.e2393 = Constraint(expr= -(-0.19617 + m.x3)**2 - (-0.03087 + m.x6)**2 + m.x7
    <= 0)
m.e2394 = Constraint(expr= -(-0.00123 + m.x3)**2 - (-0.20053 + m.x6)**2 + m.x7
    <= 0)
m.e2395 = Constraint(expr= -(-0.02937 + m.x3)**2 - (-0.27607 + m.x6)**2 + m.x7
    <= 0)
m.e2396 = Constraint(expr= -(-0.87203 + m.x3)**2 - (-0.29933 + m.x6)**2 + m.x7
    <= 0)
m.e2397 = Constraint(expr= -(-0.33457 + m.x3)**2 - (-0.51327 + m.x6)**2 + m.x7
    <= 0)
m.e2398 = Constraint(expr= -(-0.11083 + m.x3)**2 - (-0.64613 + m.x6)**2 + m.x7
    <= 0)
m.e2399 = Constraint(expr= -(-0.23177 + m.x3)**2 - (-0.06247 + m.x6)**2 + m.x7
    <= 0)
m.e2400 = Constraint(expr= -(-0.99763 + m.x3)**2 - (-0.32093 + m.x6)**2 + m.x7
    <= 0)
m.e2401 = Constraint(expr= -(-0.04097 + m.x3)**2 - (-0.44367 + m.x6)**2 + m.x7
    <= 0)
m.e2402 = Constraint(expr= -(-0.61243 + m.x3)**2 - (-0.20373 + m.x6)**2 + m.x7
    <= 0)
m.e2403 = Constraint(expr= -(-0.28217 + m.x3)**2 - (-0.37687 + m.x6)**2 + m.x7
    <= 0)
m.e2404 = Constraint(expr= -(-0.83523 + m.x3)**2 - (-0.97453 + m.x6)**2 + m.x7
    <= 0)
m.e2405 = Constraint(expr= -(-0.67537 + m.x3)**2 - (-0.78207 + m.x6)**2 + m.x7
    <= 0)
m.e2406 = Constraint(expr= -(-0.34603 + m.x3)**2 - (-0.11333 + m.x6)**2 + m.x7
    <= 0)
m.e2407 = Constraint(expr= -(-0.14057 + m.x3)**2 - (-0.77927 + m.x6)**2 + m.x7
    <= 0)
m.e2408 = Constraint(expr= -(-0.62483 + m.x3)**2 - (-0.90013 + m.x6)**2 + m.x7
    <= 0)
m.e2409 = Constraint(expr= -(-0.79777 + m.x3)**2 - (-0.68847 + m.x6)**2 + m.x7
    <= 0)
m.e2410 = Constraint(expr= -(-0.95163 + m.x3)**2 - (-0.41493 + m.x6)**2 + m.x7
    <= 0)
m.e2411 = Constraint(expr= -(-0.96697 + m.x3)**2 - (-0.02967 + m.x6)**2 + m.x7
    <= 0)
m.e2412 = Constraint(expr= -(-0.40643 + m.x3)**2 - (-0.53773 + m.x6)**2 + m.x7
    <= 0)
m.e2413 = Constraint(expr= -(-0.16817 + m.x3)**2 - (-0.52287 + m.x6)**2 + m.x7
    <= 0)
m.e2414 = Constraint(expr= -(-0.86923 + m.x3)**2 - (-0.94853 + m.x6)**2 + m.x7
    <= 0)
m.e2415 = Constraint(expr= -(-0.12137 + m.x3)**2 - (-0.08807 + m.x6)**2 + m.x7
    <= 0)
m.e2416 = Constraint(expr= -(-0.02003 + m.x3)**2 - (-0.12733 + m.x6)**2 + m.x7
    <= 0)
m.e2417 = Constraint(expr= -(-0.74657 + m.x3)**2 - (-0.84527 + m.x6)**2 + m.x7
    <= 0)
m.e2418 = Constraint(expr= -(-0.33883 + m.x3)**2 - (-0.35413 + m.x6)**2 + m.x7
    <= 0)
m.e2419 = Constraint(expr= -(-0.16377 + m.x3)**2 - (-0.11447 + m.x6)**2 + m.x7
    <= 0)
m.e2420 = Constraint(expr= -(-0.10563 + m.x3)**2 - (-0.70893 + m.x6)**2 + m.x7
    <= 0)
m.e2421 = Constraint(expr= -(-0.69297 + m.x3)**2 - (-0.41567 + m.x6)**2 + m.x7
    <= 0)
m.e2422 = Constraint(expr= -(-0.40043 + m.x3)**2 - (-0.07173 + m.x6)**2 + m.x7
    <= 0)
m.e2423 = Constraint(expr= -(-0.85417 + m.x3)**2 - (-0.46887 + m.x6)**2 + m.x7
    <= 0)
m.e2424 = Constraint(expr= -(-0.10323 + m.x3)**2 - (-0.12253 + m.x6)**2 + m.x7
    <= 0)
m.e2425 = Constraint(expr= -(-0.36737 + m.x3)**2 - (-0.19407 + m.x6)**2 + m.x7
    <= 0)
m.e2426 = Constraint(expr= -(-0.89403 + m.x3)**2 - (-0.34133 + m.x6)**2 + m.x7
    <= 0)
m.e2427 = Constraint(expr= -(-0.15257 + m.x3)**2 - (-0.71127 + m.x6)**2 + m.x7
    <= 0)
m.e2428 = Constraint(expr= -(-0.25283 + m.x3)**2 - (-0.00813 + m.x6)**2 + m.x7
    <= 0)
m.e2429 = Constraint(expr= -(-0.32977 + m.x3)**2 - (-0.34047 + m.x6)**2 + m.x7
    <= 0)
m.e2430 = Constraint(expr= -(-0.45963 + m.x3)**2 - (-0.20293 + m.x6)**2 + m.x7
    <= 0)
m.e2431 = Constraint(expr= -(-0.21897 + m.x3)**2 - (-0.60167 + m.x6)**2 + m.x7
    <= 0)
m.e2432 = Constraint(expr= -(-0.59443 + m.x3)**2 - (-0.80573 + m.x6)**2 + m.x7
    <= 0)
m.e2433 = Constraint(expr= -(-0.34017 + m.x3)**2 - (-0.21487 + m.x6)**2 + m.x7
    <= 0)
m.e2434 = Constraint(expr= -(-0.53723 + m.x3)**2 - (-0.49653 + m.x6)**2 + m.x7
    <= 0)
m.e2435 = Constraint(expr= -(-0.41337 + m.x3)**2 - (-0.10007 + m.x6)**2 + m.x7
    <= 0)
m.e2436 = Constraint(expr= -(-0.96803 + m.x3)**2 - (-0.75533 + m.x6)**2 + m.x7
    <= 0)
m.e2437 = Constraint(expr= -(-0.35857 + m.x3)**2 - (-0.37727 + m.x6)**2 + m.x7
    <= 0)
m.e2438 = Constraint(expr= -(-0.36683 + m.x3)**2 - (-0.86213 + m.x6)**2 + m.x7
    <= 0)
m.e2439 = Constraint(expr= -(-0.29577 + m.x3)**2 - (-0.36647 + m.x6)**2 + m.x7
    <= 0)
m.e2440 = Constraint(expr= -(-0.01363 + m.x3)**2 - (-0.89693 + m.x6)**2 + m.x7
    <= 0)
m.e2441 = Constraint(expr= -(-0.54497 + m.x3)**2 - (-0.58767 + m.x6)**2 + m.x7
    <= 0)
m.e2442 = Constraint(expr= -(-0.98843 + m.x3)**2 - (-0.73973 + m.x6)**2 + m.x7
    <= 0)
m.e2443 = Constraint(expr= -(-0.62617 + m.x3)**2 - (-0.76087 + m.x6)**2 + m.x7
    <= 0)
m.e2444 = Constraint(expr= -(-0.17123 + m.x3)**2 - (-0.07053 + m.x6)**2 + m.x7
    <= 0)
m.e2445 = Constraint(expr= -(-0.25937 + m.x3)**2 - (-0.80607 + m.x6)**2 + m.x7
    <= 0)
m.e2446 = Constraint(expr= -(-0.24203 + m.x3)**2 - (-0.36933 + m.x6)**2 + m.x7
    <= 0)
m.e2447 = Constraint(expr= -(-0.36457 + m.x3)**2 - (-0.84327 + m.x6)**2 + m.x7
    <= 0)
m.e2448 = Constraint(expr= -(-0.68083 + m.x3)**2 - (-0.91613 + m.x6)**2 + m.x7
    <= 0)
m.e2449 = Constraint(expr= -(-0.06177 + m.x3)**2 - (-0.19247 + m.x6)**2 + m.x7
    <= 0)
m.e2450 = Constraint(expr= -(-0.76763 + m.x3)**2 - (-0.79093 + m.x6)**2 + m.x7
    <= 0)
m.e2451 = Constraint(expr= -(-0.67097 + m.x3)**2 - (-0.37367 + m.x6)**2 + m.x7
    <= 0)
m.e2452 = Constraint(expr= -(-0.58243 + m.x3)**2 - (-0.87373 + m.x6)**2 + m.x7
    <= 0)
m.e2453 = Constraint(expr= -(-0.71217 + m.x3)**2 - (-0.10687 + m.x6)**2 + m.x7
    <= 0)
m.e2454 = Constraint(expr= -(-0.00523 + m.x3)**2 - (-0.84453 + m.x6)**2 + m.x7
    <= 0)
m.e2455 = Constraint(expr= -(-0.90537 + m.x3)**2 - (-0.31207 + m.x6)**2 + m.x7
    <= 0)
m.e2456 = Constraint(expr= -(-0.71603 + m.x3)**2 - (-0.18333 + m.x6)**2 + m.x7
    <= 0)
m.e2457 = Constraint(expr= -(-0.17057 + m.x3)**2 - (-0.10927 + m.x6)**2 + m.x7
    <= 0)
m.e2458 = Constraint(expr= -(-0.19483 + m.x3)**2 - (-0.17013 + m.x6)**2 + m.x7
    <= 0)
m.e2459 = Constraint(expr= -(-0.62777 + m.x3)**2 - (-0.81847 + m.x6)**2 + m.x7
    <= 0)
m.e2460 = Constraint(expr= -(-0.72163 + m.x3)**2 - (-0.88493 + m.x6)**2 + m.x7
    <= 0)
m.e2461 = Constraint(expr= -(-0.59697 + m.x3)**2 - (-0.95967 + m.x6)**2 + m.x7
    <= 0)
m.e2462 = Constraint(expr= -(-0.37643 + m.x3)**2 - (-0.20773 + m.x6)**2 + m.x7
    <= 0)
m.e2463 = Constraint(expr= -(-0.59817 + m.x3)**2 - (-0.25287 + m.x6)**2 + m.x7
    <= 0)
m.e2464 = Constraint(expr= -(-0.03923 + m.x3)**2 - (-0.81853 + m.x6)**2 + m.x7
    <= 0)
m.e2465 = Constraint(expr= -(-0.35137 + m.x3)**2 - (-0.61807 + m.x6)**2 + m.x7
    <= 0)
m.e2466 = Constraint(expr= -(-0.39003 + m.x3)**2 - (-0.19733 + m.x6)**2 + m.x7
    <= 0)
m.e2467 = Constraint(expr= -(-0.77657 + m.x3)**2 - (-0.17527 + m.x6)**2 + m.x7
    <= 0)
m.e2468 = Constraint(expr= -(-0.90883 + m.x3)**2 - (-0.62413 + m.x6)**2 + m.x7
    <= 0)
m.e2469 = Constraint(expr= -(-0.99377 + m.x3)**2 - (-0.24447 + m.x6)**2 + m.x7
    <= 0)
m.e2470 = Constraint(expr= -(-0.87563 + m.x3)**2 - (-0.17893 + m.x6)**2 + m.x7
    <= 0)
m.e2471 = Constraint(expr= -(-0.32297 + m.x3)**2 - (-0.34567 + m.x6)**2 + m.x7
    <= 0)
m.e2472 = Constraint(expr= -(-0.37043 + m.x3)**2 - (-0.74173 + m.x6)**2 + m.x7
    <= 0)
m.e2473 = Constraint(expr= -(-0.28417 + m.x3)**2 - (-0.19887 + m.x6)**2 + m.x7
    <= 0)
m.e2474 = Constraint(expr= -(-0.27323 + m.x3)**2 - (-0.99253 + m.x6)**2 + m.x7
    <= 0)
m.e2475 = Constraint(expr= -(-0.59737 + m.x3)**2 - (-0.72407 + m.x6)**2 + m.x7
    <= 0)
m.e2476 = Constraint(expr= -(-0.26403 + m.x3)**2 - (-0.41133 + m.x6)**2 + m.x7
    <= 0)
m.e2477 = Constraint(expr= -(-0.18257 + m.x3)**2 - (-0.04127 + m.x6)**2 + m.x7
    <= 0)
m.e2478 = Constraint(expr= -(-0.82283 + m.x3)**2 - (-0.27813 + m.x6)**2 + m.x7
    <= 0)
m.e2479 = Constraint(expr= -(-0.15977 + m.x3)**2 - (-0.47047 + m.x6)**2 + m.x7
    <= 0)
m.e2480 = Constraint(expr= -(-0.22963 + m.x3)**2 - (-0.67293 + m.x6)**2 + m.x7
    <= 0)
m.e2481 = Constraint(expr= -(-0.84897 + m.x3)**2 - (-0.53167 + m.x6)**2 + m.x7
    <= 0)
m.e2482 = Constraint(expr= -(-0.56443 + m.x3)**2 - (-0.47573 + m.x6)**2 + m.x7
    <= 0)
m.e2483 = Constraint(expr= -(-0.77017 + m.x3)**2 - (-0.94487 + m.x6)**2 + m.x7
    <= 0)
m.e2484 = Constraint(expr= -(-0.70723 + m.x3)**2 - (-0.36653 + m.x6)**2 + m.x7
    <= 0)
m.e2485 = Constraint(expr= -(-0.64337 + m.x3)**2 - (-0.63007 + m.x6)**2 + m.x7
    <= 0)
m.e2486 = Constraint(expr= -(-0.33803 + m.x3)**2 - (-0.82533 + m.x6)**2 + m.x7
    <= 0)
m.e2487 = Constraint(expr= -(-0.38857 + m.x3)**2 - (-0.70727 + m.x6)**2 + m.x7
    <= 0)
m.e2488 = Constraint(expr= -(-0.93683 + m.x3)**2 - (-0.13213 + m.x6)**2 + m.x7
    <= 0)
m.e2489 = Constraint(expr= -(-0.12577 + m.x3)**2 - (-0.49647 + m.x6)**2 + m.x7
    <= 0)
m.e2490 = Constraint(expr= -(-0.78363 + m.x3)**2 - (-0.36693 + m.x6)**2 + m.x7
    <= 0)
m.e2491 = Constraint(expr= -(-0.17497 + m.x3)**2 - (-0.51767 + m.x6)**2 + m.x7
    <= 0)
m.e2492 = Constraint(expr= -(-0.95843 + m.x3)**2 - (-0.40973 + m.x6)**2 + m.x7
    <= 0)
m.e2493 = Constraint(expr= -(-0.05617 + m.x3)**2 - (-0.49087 + m.x6)**2 + m.x7
    <= 0)
m.e2494 = Constraint(expr= -(-0.34123 + m.x3)**2 - (-0.94053 + m.x6)**2 + m.x7
    <= 0)
m.e2495 = Constraint(expr= -(-0.48937 + m.x3)**2 - (-0.33607 + m.x6)**2 + m.x7
    <= 0)
m.e2496 = Constraint(expr= -(-0.61203 + m.x3)**2 - (-0.43933 + m.x6)**2 + m.x7
    <= 0)
m.e2497 = Constraint(expr= -(-0.39457 + m.x3)**2 - (-0.17327 + m.x6)**2 + m.x7
    <= 0)
m.e2498 = Constraint(expr= -(-0.25083 + m.x3)**2 - (-0.18613 + m.x6)**2 + m.x7
    <= 0)
m.e2499 = Constraint(expr= -(-0.89177 + m.x3)**2 - (-0.32247 + m.x6)**2 + m.x7
    <= 0)
m.e2500 = Constraint(expr= -(-0.53763 + m.x3)**2 - (-0.26093 + m.x6)**2 + m.x7
    <= 0)
m.e2501 = Constraint(expr= -(-0.30097 + m.x3)**2 - (-0.30367 + m.x6)**2 + m.x7
    <= 0)
m.e2502 = Constraint(expr= -(-0.55243 + m.x3)**2 - (-0.54373 + m.x6)**2 + m.x7
    <= 0)
m.e2503 = Constraint(expr= -(-0.14217 + m.x3)**2 - (-0.83687 + m.x6)**2 + m.x7
    <= 0)
m.e2504 = Constraint(expr= -(-0.17523 + m.x3)**2 - (-0.71453 + m.x6)**2 + m.x7
    <= 0)
m.e2505 = Constraint(expr= -(-0.13537 + m.x3)**2 - (-0.84207 + m.x6)**2 + m.x7
    <= 0)
m.e2506 = Constraint(expr= -(-0.08603 + m.x3)**2 - (-0.25333 + m.x6)**2 + m.x7
    <= 0)
m.e2507 = Constraint(expr= -(-0.20057 + m.x3)**2 - (-0.43927 + m.x6)**2 + m.x7
    <= 0)
m.e2508 = Constraint(expr= -(-0.76483 + m.x3)**2 - (-0.44013 + m.x6)**2 + m.x7
    <= 0)
m.e2509 = Constraint(expr= -(-0.45777 + m.x3)**2 - (-0.94847 + m.x6)**2 + m.x7
    <= 0)
m.e2510 = Constraint(expr= -(-0.49163 + m.x3)**2 - (-0.35493 + m.x6)**2 + m.x7
    <= 0)
m.e2511 = Constraint(expr= -(-0.22697 + m.x3)**2 - (-0.88967 + m.x6)**2 + m.x7
    <= 0)
m.e2512 = Constraint(expr= -(-0.34643 + m.x3)**2 - (-0.87773 + m.x6)**2 + m.x7
    <= 0)
m.e2513 = Constraint(expr= -(-0.02817 + m.x3)**2 - (-0.98287 + m.x6)**2 + m.x7
    <= 0)
m.e2514 = Constraint(expr= -(-0.20923 + m.x3)**2 - (-0.68853 + m.x6)**2 + m.x7
    <= 0)
m.e2515 = Constraint(expr= -(-0.58137 + m.x3)**2 - (-0.14807 + m.x6)**2 + m.x7
    <= 0)
m.e2516 = Constraint(expr= -(-0.76003 + m.x3)**2 - (-0.26733 + m.x6)**2 + m.x7
    <= 0)
m.e2517 = Constraint(expr= -(-0.80657 + m.x3)**2 - (-0.50527 + m.x6)**2 + m.x7
    <= 0)
m.e2518 = Constraint(expr= -(-0.47883 + m.x3)**2 - (-0.89413 + m.x6)**2 + m.x7
    <= 0)
m.e2519 = Constraint(expr= -(-0.82377 + m.x3)**2 - (-0.37447 + m.x6)**2 + m.x7
    <= 0)
m.e2520 = Constraint(expr= -(-0.64563 + m.x3)**2 - (-0.64893 + m.x6)**2 + m.x7
    <= 0)
m.e2521 = Constraint(expr= -(-0.95297 + m.x3)**2 - (-0.27567 + m.x6)**2 + m.x7
    <= 0)
m.e2522 = Constraint(expr= -(-0.34043 + m.x3)**2 - (-0.41173 + m.x6)**2 + m.x7
    <= 0)
m.e2523 = Constraint(expr= -(-0.71417 + m.x3)**2 - (-0.92887 + m.x6)**2 + m.x7
    <= 0)
m.e2524 = Constraint(expr= -(-0.44323 + m.x3)**2 - (-0.86253 + m.x6)**2 + m.x7
    <= 0)
m.e2525 = Constraint(expr= -(-0.82737 + m.x3)**2 - (-0.25407 + m.x6)**2 + m.x7
    <= 0)
m.e2526 = Constraint(expr= -(-0.63403 + m.x3)**2 - (-0.48133 + m.x6)**2 + m.x7
    <= 0)
m.e2527 = Constraint(expr= -(-0.21257 + m.x3)**2 - (-0.37127 + m.x6)**2 + m.x7
    <= 0)
m.e2528 = Constraint(expr= -(-0.39283 + m.x3)**2 - (-0.54813 + m.x6)**2 + m.x7
    <= 0)
m.e2529 = Constraint(expr= -(-0.98977 + m.x3)**2 - (-0.60047 + m.x6)**2 + m.x7
    <= 0)
m.e2530 = Constraint(expr= -(-0.99963 + m.x3)**2 - (-0.14293 + m.x6)**2 + m.x7
    <= 0)
m.e2531 = Constraint(expr= -(-0.47897 + m.x3)**2 - (-0.46167 + m.x6)**2 + m.x7
    <= 0)
m.e2532 = Constraint(expr= -(-0.53443 + m.x3)**2 - (-0.14573 + m.x6)**2 + m.x7
    <= 0)
m.e2533 = Constraint(expr= -(-0.20017 + m.x3)**2 - (-0.67487 + m.x6)**2 + m.x7
    <= 0)
m.e2534 = Constraint(expr= -(-0.87723 + m.x3)**2 - (-0.23653 + m.x6)**2 + m.x7
    <= 0)
m.e2535 = Constraint(expr= -(-0.87337 + m.x3)**2 - (-0.16007 + m.x6)**2 + m.x7
    <= 0)
m.e2536 = Constraint(expr= -(-0.70803 + m.x3)**2 - (-0.89533 + m.x6)**2 + m.x7
    <= 0)
m.e2537 = Constraint(expr= -(-0.41857 + m.x3)**2 - (-0.03727 + m.x6)**2 + m.x7
    <= 0)
m.e2538 = Constraint(expr= -(-0.50683 + m.x3)**2 - (-0.40213 + m.x6)**2 + m.x7
    <= 0)
m.e2539 = Constraint(expr= -(-0.95577 + m.x3)**2 - (-0.62647 + m.x6)**2 + m.x7
    <= 0)
m.e2540 = Constraint(expr= -(-0.55363 + m.x3)**2 - (-0.83693 + m.x6)**2 + m.x7
    <= 0)
m.e2541 = Constraint(expr= -(-0.80497 + m.x3)**2 - (-0.44767 + m.x6)**2 + m.x7
    <= 0)
m.e2542 = Constraint(expr= -(-0.92843 + m.x3)**2 - (-0.07973 + m.x6)**2 + m.x7
    <= 0)
m.e2543 = Constraint(expr= -(-0.48617 + m.x3)**2 - (-0.22087 + m.x6)**2 + m.x7
    <= 0)
m.e2544 = Constraint(expr= -(-0.51123 + m.x3)**2 - (-0.81053 + m.x6)**2 + m.x7
    <= 0)
m.e2545 = Constraint(expr= -(-0.71937 + m.x3)**2 - (-0.86607 + m.x6)**2 + m.x7
    <= 0)
m.e2546 = Constraint(expr= -(-0.98203 + m.x3)**2 - (-0.50933 + m.x6)**2 + m.x7
    <= 0)
m.e2547 = Constraint(expr= -(-0.42457 + m.x3)**2 - (-0.50327 + m.x6)**2 + m.x7
    <= 0)
m.e2548 = Constraint(expr= -(-0.82083 + m.x3)**2 - (-0.45613 + m.x6)**2 + m.x7
    <= 0)
m.e2549 = Constraint(expr= -(-0.72177 + m.x3)**2 - (-0.45247 + m.x6)**2 + m.x7
    <= 0)
m.e2550 = Constraint(expr= -(-0.30763 + m.x3)**2 - (-0.73093 + m.x6)**2 + m.x7
    <= 0)
m.e2551 = Constraint(expr= -(-0.93097 + m.x3)**2 - (-0.23367 + m.x6)**2 + m.x7
    <= 0)
m.e2552 = Constraint(expr= -(-0.52243 + m.x3)**2 - (-0.21373 + m.x6)**2 + m.x7
    <= 0)
m.e2553 = Constraint(expr= -(-0.57217 + m.x3)**2 - (-0.56687 + m.x6)**2 + m.x7
    <= 0)
m.e2554 = Constraint(expr= -(-0.34523 + m.x3)**2 - (-0.58453 + m.x6)**2 + m.x7
    <= 0)
m.e2555 = Constraint(expr= -(-0.36537 + m.x3)**2 - (-0.37207 + m.x6)**2 + m.x7
    <= 0)
m.e2556 = Constraint(expr= -(-0.45603 + m.x3)**2 - (-0.32333 + m.x6)**2 + m.x7
    <= 0)
m.e2557 = Constraint(expr= -(-0.23057 + m.x3)**2 - (-0.76927 + m.x6)**2 + m.x7
    <= 0)
m.e2558 = Constraint(expr= -(-0.33483 + m.x3)**2 - (-0.71013 + m.x6)**2 + m.x7
    <= 0)
m.e2559 = Constraint(expr= -(-0.28777 + m.x3)**2 - (-0.07847 + m.x6)**2 + m.x7
    <= 0)
m.e2560 = Constraint(expr= -(-0.26163 + m.x3)**2 - (-0.82493 + m.x6)**2 + m.x7
    <= 0)
m.e2561 = Constraint(expr= -(-0.85697 + m.x3)**2 - (-0.81967 + m.x6)**2 + m.x7
    <= 0)
m.e2562 = Constraint(expr= -(-0.31643 + m.x3)**2 - (-0.54773 + m.x6)**2 + m.x7
    <= 0)
m.e2563 = Constraint(expr= -(-0.45817 + m.x3)**2 - (-0.71287 + m.x6)**2 + m.x7
    <= 0)
m.e2564 = Constraint(expr= -(-0.37923 + m.x3)**2 - (-0.55853 + m.x6)**2 + m.x7
    <= 0)
m.e2565 = Constraint(expr= -(-0.81137 + m.x3)**2 - (-0.67807 + m.x6)**2 + m.x7
    <= 0)
m.e2566 = Constraint(expr= -(-0.13003 + m.x3)**2 - (-0.33733 + m.x6)**2 + m.x7
    <= 0)
m.e2567 = Constraint(expr= -(-0.83657 + m.x3)**2 - (-0.83527 + m.x6)**2 + m.x7
    <= 0)
m.e2568 = Constraint(expr= -(-0.04883 + m.x3)**2 - (-0.16413 + m.x6)**2 + m.x7
    <= 0)
m.e2569 = Constraint(expr= -(-0.65377 + m.x3)**2 - (-0.50447 + m.x6)**2 + m.x7
    <= 0)
m.e2570 = Constraint(expr= -(-0.41563 + m.x3)**2 - (-0.11893 + m.x6)**2 + m.x7
    <= 0)
m.e2571 = Constraint(expr= -(-0.58297 + m.x3)**2 - (-0.20567 + m.x6)**2 + m.x7
    <= 0)
m.e2572 = Constraint(expr= -(-0.31043 + m.x3)**2 - (-0.08173 + m.x6)**2 + m.x7
    <= 0)
m.e2573 = Constraint(expr= -(-0.14417 + m.x3)**2 - (-0.65887 + m.x6)**2 + m.x7
    <= 0)
m.e2574 = Constraint(expr= -(-0.61323 + m.x3)**2 - (-0.73253 + m.x6)**2 + m.x7
    <= 0)
m.e2575 = Constraint(expr= -(-0.05737 + m.x3)**2 - (-0.78407 + m.x6)**2 + m.x7
    <= 0)
m.e2576 = Constraint(expr= -(-0.00403 + m.x3)**2 - (-0.55133 + m.x6)**2 + m.x7
    <= 0)
m.e2577 = Constraint(expr= -(-0.24257 + m.x3)**2 - (-0.70127 + m.x6)**2 + m.x7
    <= 0)
m.e2578 = Constraint(expr= -(-0.96283 + m.x3)**2 - (-0.81813 + m.x6)**2 + m.x7
    <= 0)
m.e2579 = Constraint(expr= -(-0.81977 + m.x3)**2 - (-0.73047 + m.x6)**2 + m.x7
    <= 0)
m.e2580 = Constraint(expr= -(-0.76963 + m.x3)**2 - (-0.61293 + m.x6)**2 + m.x7
    <= 0)
m.e2581 = Constraint(expr= -(-0.10897 + m.x3)**2 - (-0.39167 + m.x6)**2 + m.x7
    <= 0)
m.e2582 = Constraint(expr= -(-0.50443 + m.x3)**2 - (-0.81573 + m.x6)**2 + m.x7
    <= 0)
m.e2583 = Constraint(expr= -(-0.63017 + m.x3)**2 - (-0.40487 + m.x6)**2 + m.x7
    <= 0)
m.e2584 = Constraint(expr= -(-0.04723 + m.x3)**2 - (-0.10653 + m.x6)**2 + m.x7
    <= 0)
m.e2585 = Constraint(expr= -(-0.10337 + m.x3)**2 - (-0.69007 + m.x6)**2 + m.x7
    <= 0)
m.e2586 = Constraint(expr= -(-0.07803 + m.x3)**2 - (-0.96533 + m.x6)**2 + m.x7
    <= 0)
m.e2587 = Constraint(expr= -(-0.44857 + m.x3)**2 - (-0.36727 + m.x6)**2 + m.x7
    <= 0)
m.e2588 = Constraint(expr= -(-0.07683 + m.x3)**2 - (-0.67213 + m.x6)**2 + m.x7
    <= 0)
m.e2589 = Constraint(expr= -(-0.78577 + m.x3)**2 - (-0.75647 + m.x6)**2 + m.x7
    <= 0)
m.e2590 = Constraint(expr= -(-0.32363 + m.x3)**2 - (-0.30693 + m.x6)**2 + m.x7
    <= 0)
m.e2591 = Constraint(expr= -(-0.43497 + m.x3)**2 - (-0.37767 + m.x6)**2 + m.x7
    <= 0)
m.e2592 = Constraint(expr= -(-0.89843 + m.x3)**2 - (-0.74973 + m.x6)**2 + m.x7
    <= 0)
m.e2593 = Constraint(expr= -(-0.91617 + m.x3)**2 - (-0.95087 + m.x6)**2 + m.x7
    <= 0)
m.e2594 = Constraint(expr= -(-0.68123 + m.x3)**2 - (-0.68053 + m.x6)**2 + m.x7
    <= 0)
m.e2595 = Constraint(expr= -(-0.94937 + m.x3)**2 - (-0.39607 + m.x6)**2 + m.x7
    <= 0)
m.e2596 = Constraint(expr= -(-0.35203 + m.x3)**2 - (-0.57933 + m.x6)**2 + m.x7
    <= 0)
m.e2597 = Constraint(expr= -(-0.45457 + m.x3)**2 - (-0.83327 + m.x6)**2 + m.x7
    <= 0)
m.e2598 = Constraint(expr= -(-0.39083 + m.x3)**2 - (-0.72613 + m.x6)**2 + m.x7
    <= 0)
m.e2599 = Constraint(expr= -(-0.55177 + m.x3)**2 - (-0.58247 + m.x6)**2 + m.x7
    <= 0)
m.e2600 = Constraint(expr= -(-0.07763 + m.x3)**2 - (-0.20093 + m.x6)**2 + m.x7
    <= 0)
m.e2601 = Constraint(expr= -(-0.56097 + m.x3)**2 - (-0.16367 + m.x6)**2 + m.x7
    <= 0)
m.e2602 = Constraint(expr= -(-0.49243 + m.x3)**2 - (-0.88373 + m.x6)**2 + m.x7
    <= 0)
m.e2603 = Constraint(expr= -(-0.00217 + m.x3)**2 - (-0.29687 + m.x6)**2 + m.x7
    <= 0)
m.e2604 = Constraint(expr= -(-0.51523 + m.x3)**2 - (-0.45453 + m.x6)**2 + m.x7
    <= 0)
m.e2605 = Constraint(expr= -(-0.59537 + m.x3)**2 - (-0.90207 + m.x6)**2 + m.x7
    <= 0)
m.e2606 = Constraint(expr= -(-0.82603 + m.x3)**2 - (-0.39333 + m.x6)**2 + m.x7
    <= 0)
m.e2607 = Constraint(expr= -(-0.26057 + m.x3)**2 - (-0.09927 + m.x6)**2 + m.x7
    <= 0)
m.e2608 = Constraint(expr= -(-0.90483 + m.x3)**2 - (-0.98013 + m.x6)**2 + m.x7
    <= 0)
m.e2609 = Constraint(expr= -(-0.11777 + m.x3)**2 - (-0.20847 + m.x6)**2 + m.x7
    <= 0)
m.e2610 = Constraint(expr= -(-0.03163 + m.x3)**2 - (-0.29493 + m.x6)**2 + m.x7
    <= 0)
m.e2611 = Constraint(expr= -(-0.48697 + m.x3)**2 - (-0.74967 + m.x6)**2 + m.x7
    <= 0)
m.e2612 = Constraint(expr= -(-0.28643 + m.x3)**2 - (-0.21773 + m.x6)**2 + m.x7
    <= 0)
m.e2613 = Constraint(expr= -(-0.88817 + m.x3)**2 - (-0.44287 + m.x6)**2 + m.x7
    <= 0)
m.e2614 = Constraint(expr= -(-0.54923 + m.x3)**2 - (-0.42853 + m.x6)**2 + m.x7
    <= 0)
m.e2615 = Constraint(expr= -(-0.04137 + m.x3)**2 - (-0.20807 + m.x6)**2 + m.x7
    <= 0)
m.e2616 = Constraint(expr= -(-0.50003 + m.x3)**2 - (-0.40733 + m.x6)**2 + m.x7
    <= 0)
m.e2617 = Constraint(expr= -(-0.86657 + m.x3)**2 - (-0.16527 + m.x6)**2 + m.x7
    <= 0)
m.e2618 = Constraint(expr= -(-0.61883 + m.x3)**2 - (-0.43413 + m.x6)**2 + m.x7
    <= 0)
m.e2619 = Constraint(expr= -(-0.48377 + m.x3)**2 - (-0.63447 + m.x6)**2 + m.x7
    <= 0)
m.e2620 = Constraint(expr= -(-0.18563 + m.x3)**2 - (-0.58893 + m.x6)**2 + m.x7
    <= 0)
m.e2621 = Constraint(expr= -(-0.21297 + m.x3)**2 - (-0.13567 + m.x6)**2 + m.x7
    <= 0)
m.e2622 = Constraint(expr= -(-0.28043 + m.x3)**2 - (-0.75173 + m.x6)**2 + m.x7
    <= 0)
m.e2623 = Constraint(expr= -(-0.57417 + m.x3)**2 - (-0.38887 + m.x6)**2 + m.x7
    <= 0)
m.e2624 = Constraint(expr= -(-0.78323 + m.x3)**2 - (-0.60253 + m.x6)**2 + m.x7
    <= 0)
m.e2625 = Constraint(expr= -(-0.28737 + m.x3)**2 - (-0.31407 + m.x6)**2 + m.x7
    <= 0)
m.e2626 = Constraint(expr= -(-0.37403 + m.x3)**2 - (-0.62133 + m.x6)**2 + m.x7
    <= 0)
m.e2627 = Constraint(expr= -(-0.27257 + m.x3)**2 - (-0.03127 + m.x6)**2 + m.x7
    <= 0)
m.e2628 = Constraint(expr= -(-0.53283 + m.x3)**2 - (-0.08813 + m.x6)**2 + m.x7
    <= 0)
m.e2629 = Constraint(expr= -(-0.64977 + m.x3)**2 - (-0.86047 + m.x6)**2 + m.x7
    <= 0)
m.e2630 = Constraint(expr= -(-0.53963 + m.x3)**2 - (-0.08293 + m.x6)**2 + m.x7
    <= 0)
m.e2631 = Constraint(expr= -(-0.73897 + m.x3)**2 - (-0.32167 + m.x6)**2 + m.x7
    <= 0)
m.e2632 = Constraint(expr= -(-0.47443 + m.x3)**2 - (-0.48573 + m.x6)**2 + m.x7
    <= 0)
m.e2633 = Constraint(expr= -(-0.06017 + m.x3)**2 - (-0.13487 + m.x6)**2 + m.x7
    <= 0)
m.e2634 = Constraint(expr= -(-0.21723 + m.x3)**2 - (-0.97653 + m.x6)**2 + m.x7
    <= 0)
m.e2635 = Constraint(expr= -(-0.33337 + m.x3)**2 - (-0.22007 + m.x6)**2 + m.x7
    <= 0)
m.e2636 = Constraint(expr= -(-0.44803 + m.x3)**2 - (-0.03533 + m.x6)**2 + m.x7
    <= 0)
m.e2637 = Constraint(expr= -(-0.47857 + m.x3)**2 - (-0.69727 + m.x6)**2 + m.x7
    <= 0)
m.e2638 = Constraint(expr= -(-0.64683 + m.x3)**2 - (-0.94213 + m.x6)**2 + m.x7
    <= 0)
m.e2639 = Constraint(expr= -(-0.61577 + m.x3)**2 - (-0.88647 + m.x6)**2 + m.x7
    <= 0)
m.e2640 = Constraint(expr= -(-0.09363 + m.x3)**2 - (-0.77693 + m.x6)**2 + m.x7
    <= 0)
m.e2641 = Constraint(expr= -(-0.06497 + m.x3)**2 - (-0.30767 + m.x6)**2 + m.x7
    <= 0)
m.e2642 = Constraint(expr= -(-0.86843 + m.x3)**2 - (-0.41973 + m.x6)**2 + m.x7
    <= 0)
m.e2643 = Constraint(expr= -(-0.34617 + m.x3)**2 - (-0.68087 + m.x6)**2 + m.x7
    <= 0)
m.e2644 = Constraint(expr= -(-0.85123 + m.x3)**2 - (-0.55053 + m.x6)**2 + m.x7
    <= 0)
m.e2645 = Constraint(expr= -(-0.17937 + m.x3)**2 - (-0.92607 + m.x6)**2 + m.x7
    <= 0)
m.e2646 = Constraint(expr= -(-0.72203 + m.x3)**2 - (-0.64933 + m.x6)**2 + m.x7
    <= 0)
m.e2647 = Constraint(expr= -(-0.48457 + m.x3)**2 - (-0.16327 + m.x6)**2 + m.x7
    <= 0)
m.e2648 = Constraint(expr= -(-0.96083 + m.x3)**2 - (-0.99613 + m.x6)**2 + m.x7
    <= 0)
m.e2649 = Constraint(expr= -(-0.38177 + m.x3)**2 - (-0.71247 + m.x6)**2 + m.x7
    <= 0)
m.e2650 = Constraint(expr= -(-0.84763 + m.x3)**2 - (-0.67093 + m.x6)**2 + m.x7
    <= 0)
m.e2651 = Constraint(expr= -(-0.19097 + m.x3)**2 - (-0.09367 + m.x6)**2 + m.x7
    <= 0)
m.e2652 = Constraint(expr= -(-0.46243 + m.x3)**2 - (-0.55373 + m.x6)**2 + m.x7
    <= 0)
m.e2653 = Constraint(expr= -(-0.43217 + m.x3)**2 - (-0.02687 + m.x6)**2 + m.x7
    <= 0)
m.e2654 = Constraint(expr= -(-0.68523 + m.x3)**2 - (-0.32453 + m.x6)**2 + m.x7
    <= 0)
m.e2655 = Constraint(expr= -(-0.82537 + m.x3)**2 - (-0.43207 + m.x6)**2 + m.x7
    <= 0)
m.e2656 = Constraint(expr= -(-0.19603 + m.x3)**2 - (-0.46333 + m.x6)**2 + m.x7
    <= 0)
m.e2657 = Constraint(expr= -(-0.29057 + m.x3)**2 - (-0.42927 + m.x6)**2 + m.x7
    <= 0)
m.e2658 = Constraint(expr= -(-0.47483 + m.x3)**2 - (-0.25013 + m.x6)**2 + m.x7
    <= 0)
m.e2659 = Constraint(expr= -(-0.94777 + m.x3)**2 - (-0.33847 + m.x6)**2 + m.x7
    <= 0)
m.e2660 = Constraint(expr= -(-0.80163 + m.x3)**2 - (-0.76493 + m.x6)**2 + m.x7
    <= 0)
m.e2661 = Constraint(expr= -(-0.11697 + m.x3)**2 - (-0.67967 + m.x6)**2 + m.x7
    <= 0)
m.e2662 = Constraint(expr= -(-0.25643 + m.x3)**2 - (-0.88773 + m.x6)**2 + m.x7
    <= 0)
m.e2663 = Constraint(expr= -(-0.31817 + m.x3)**2 - (-0.17287 + m.x6)**2 + m.x7
    <= 0)
m.e2664 = Constraint(expr= -(-0.71923 + m.x3)**2 - (-0.29853 + m.x6)**2 + m.x7
    <= 0)
m.e2665 = Constraint(expr= -(-0.27137 + m.x3)**2 - (-0.73807 + m.x6)**2 + m.x7
    <= 0)
m.e2666 = Constraint(expr= -(-0.87003 + m.x3)**2 - (-0.47733 + m.x6)**2 + m.x7
    <= 0)
m.e2667 = Constraint(expr= -(-0.89657 + m.x3)**2 - (-0.49527 + m.x6)**2 + m.x7
    <= 0)
m.e2668 = Constraint(expr= -(-0.18883 + m.x3)**2 - (-0.70413 + m.x6)**2 + m.x7
    <= 0)
m.e2669 = Constraint(expr= -(-0.31377 + m.x3)**2 - (-0.76447 + m.x6)**2 + m.x7
    <= 0)
m.e2670 = Constraint(expr= -(-0.95563 + m.x3)**2 - (-0.05893 + m.x6)**2 + m.x7
    <= 0)
m.e2671 = Constraint(expr= -(-0.84297 + m.x3)**2 - (-0.06567 + m.x6)**2 + m.x7
    <= 0)
m.e2672 = Constraint(expr= -(-0.25043 + m.x3)**2 - (-0.42173 + m.x6)**2 + m.x7
    <= 0)
m.e2673 = Constraint(expr= -(-0.00417 + m.x3)**2 - (-0.11887 + m.x6)**2 + m.x7
    <= 0)
m.e2674 = Constraint(expr= -(-0.95323 + m.x3)**2 - (-0.47253 + m.x6)**2 + m.x7
    <= 0)
m.e2675 = Constraint(expr= -(-0.51737 + m.x3)**2 - (-0.84407 + m.x6)**2 + m.x7
    <= 0)
m.e2676 = Constraint(expr= -(-0.74403 + m.x3)**2 - (-0.69133 + m.x6)**2 + m.x7
    <= 0)
m.e2677 = Constraint(expr= -(-0.30257 + m.x3)**2 - (-0.36127 + m.x6)**2 + m.x7
    <= 0)
m.e2678 = Constraint(expr= -(-0.10283 + m.x3)**2 - (-0.35813 + m.x6)**2 + m.x7
    <= 0)
m.e2679 = Constraint(expr= -(-0.47977 + m.x3)**2 - (-0.99047 + m.x6)**2 + m.x7
    <= 0)
m.e2680 = Constraint(expr= -(-0.30963 + m.x3)**2 - (-0.55293 + m.x6)**2 + m.x7
    <= 0)
m.e2681 = Constraint(expr= -(-0.36897 + m.x3)**2 - (-0.25167 + m.x6)**2 + m.x7
    <= 0)
m.e2682 = Constraint(expr= -(-0.44443 + m.x3)**2 - (-0.15573 + m.x6)**2 + m.x7
    <= 0)
m.e2683 = Constraint(expr= -(-0.49017 + m.x3)**2 - (-0.86487 + m.x6)**2 + m.x7
    <= 0)
m.e2684 = Constraint(expr= -(-0.38723 + m.x3)**2 - (-0.84653 + m.x6)**2 + m.x7
    <= 0)
m.e2685 = Constraint(expr= -(-0.56337 + m.x3)**2 - (-0.75007 + m.x6)**2 + m.x7
    <= 0)
m.e2686 = Constraint(expr= -(-0.81803 + m.x3)**2 - (-0.10533 + m.x6)**2 + m.x7
    <= 0)
m.e2687 = Constraint(expr= -(-0.50857 + m.x3)**2 - (-0.02727 + m.x6)**2 + m.x7
    <= 0)
m.e2688 = Constraint(expr= -(-0.21683 + m.x3)**2 - (-0.21213 + m.x6)**2 + m.x7
    <= 0)
m.e2689 = Constraint(expr= -(-0.44577 + m.x3)**2 - (-0.01647 + m.x6)**2 + m.x7
    <= 0)
m.e2690 = Constraint(expr= -(-0.86363 + m.x3)**2 - (-0.24693 + m.x6)**2 + m.x7
    <= 0)
m.e2691 = Constraint(expr= -(-0.69497 + m.x3)**2 - (-0.23767 + m.x6)**2 + m.x7
    <= 0)
m.e2692 = Constraint(expr= -(-0.83843 + m.x3)**2 - (-0.08973 + m.x6)**2 + m.x7
    <= 0)
m.e2693 = Constraint(expr= -(-0.77617 + m.x3)**2 - (-0.41087 + m.x6)**2 + m.x7
    <= 0)
m.e2694 = Constraint(expr= -(-0.02123 + m.x3)**2 - (-0.42053 + m.x6)**2 + m.x7
    <= 0)
m.e2695 = Constraint(expr= -(-0.40937 + m.x3)**2 - (-0.45607 + m.x6)**2 + m.x7
    <= 0)
m.e2696 = Constraint(expr= -(-0.09203 + m.x3)**2 - (-0.71933 + m.x6)**2 + m.x7
    <= 0)
m.e2697 = Constraint(expr= -(-0.51457 + m.x3)**2 - (-0.49327 + m.x6)**2 + m.x7
    <= 0)
m.e2698 = Constraint(expr= -(-0.53083 + m.x3)**2 - (-0.26613 + m.x6)**2 + m.x7
    <= 0)
m.e2699 = Constraint(expr= -(-0.21177 + m.x3)**2 - (-0.84247 + m.x6)**2 + m.x7
    <= 0)
m.e2700 = Constraint(expr= -(-0.61763 + m.x3)**2 - (-0.14093 + m.x6)**2 + m.x7
    <= 0)
m.e2701 = Constraint(expr= -(-0.82097 + m.x3)**2 - (-0.02367 + m.x6)**2 + m.x7
    <= 0)
m.e2702 = Constraint(expr= -(-0.43243 + m.x3)**2 - (-0.22373 + m.x6)**2 + m.x7
    <= 0)
m.e2703 = Constraint(expr= -(-0.86217 + m.x3)**2 - (-0.75687 + m.x6)**2 + m.x7
    <= 0)
m.e2704 = Constraint(expr= -(-0.85523 + m.x3)**2 - (-0.19453 + m.x6)**2 + m.x7
    <= 0)
m.e2705 = Constraint(expr= -(-0.05537 + m.x3)**2 - (-0.96207 + m.x6)**2 + m.x7
    <= 0)
m.e2706 = Constraint(expr= -(-0.56603 + m.x3)**2 - (-0.53333 + m.x6)**2 + m.x7
    <= 0)
m.e2707 = Constraint(expr= -(-0.32057 + m.x3)**2 - (-0.75927 + m.x6)**2 + m.x7
    <= 0)
m.e2708 = Constraint(expr= -(-0.04483 + m.x3)**2 - (-0.52013 + m.x6)**2 + m.x7
    <= 0)
m.e2709 = Constraint(expr= -(-0.77777 + m.x3)**2 - (-0.46847 + m.x6)**2 + m.x7
    <= 0)
m.e2710 = Constraint(expr= -(-0.57163 + m.x3)**2 - (-0.23493 + m.x6)**2 + m.x7
    <= 0)
m.e2711 = Constraint(expr= -(-0.74697 + m.x3)**2 - (-0.60967 + m.x6)**2 + m.x7
    <= 0)
m.e2712 = Constraint(expr= -(-0.22643 + m.x3)**2 - (-0.55773 + m.x6)**2 + m.x7
    <= 0)
m.e2713 = Constraint(expr= -(-0.74817 + m.x3)**2 - (-0.90287 + m.x6)**2 + m.x7
    <= 0)
m.e2714 = Constraint(expr= -(-0.88923 + m.x3)**2 - (-0.16853 + m.x6)**2 + m.x7
    <= 0)
m.e2715 = Constraint(expr= -(-0.50137 + m.x3)**2 - (-0.26807 + m.x6)**2 + m.x7
    <= 0)
m.e2716 = Constraint(expr= -(-0.24003 + m.x3)**2 - (-0.54733 + m.x6)**2 + m.x7
    <= 0)
m.e2717 = Constraint(expr= -(-0.92657 + m.x3)**2 - (-0.82527 + m.x6)**2 + m.x7
    <= 0)
m.e2718 = Constraint(expr= -(-0.75883 + m.x3)**2 - (-0.97413 + m.x6)**2 + m.x7
    <= 0)
m.e2719 = Constraint(expr= -(-0.14377 + m.x3)**2 - (-0.89447 + m.x6)**2 + m.x7
    <= 0)
m.e2720 = Constraint(expr= -(-0.72563 + m.x3)**2 - (-0.52893 + m.x6)**2 + m.x7
    <= 0)
m.e2721 = Constraint(expr= -(-0.47297 + m.x3)**2 - (-0.99567 + m.x6)**2 + m.x7
    <= 0)
m.e2722 = Constraint(expr= -(-0.22043 + m.x3)**2 - (-0.09173 + m.x6)**2 + m.x7
    <= 0)
m.e2723 = Constraint(expr= -(-0.43417 + m.x3)**2 - (-0.84887 + m.x6)**2 + m.x7
    <= 0)
m.e2724 = Constraint(expr= -(-0.12323 + m.x3)**2 - (-0.34253 + m.x6)**2 + m.x7
    <= 0)
m.e2725 = Constraint(expr= -(-0.74737 + m.x3)**2 - (-0.37407 + m.x6)**2 + m.x7
    <= 0)
m.e2726 = Constraint(expr= -(-0.11403 + m.x3)**2 - (-0.76133 + m.x6)**2 + m.x7
    <= 0)
m.e2727 = Constraint(expr= -(-0.33257 + m.x3)**2 - (-0.69127 + m.x6)**2 + m.x7
    <= 0)
m.e2728 = Constraint(expr= -(-0.67283 + m.x3)**2 - (-0.62813 + m.x6)**2 + m.x7
    <= 0)
m.e2729 = Constraint(expr= -(-0.30977 + m.x3)**2 - (-0.12047 + m.x6)**2 + m.x7
    <= 0)
m.e2730 = Constraint(expr= -(-0.07963 + m.x3)**2 - (-0.02293 + m.x6)**2 + m.x7
    <= 0)
m.e2731 = Constraint(expr= -(-0.99897 + m.x3)**2 - (-0.18167 + m.x6)**2 + m.x7
    <= 0)
m.e2732 = Constraint(expr= -(-0.41443 + m.x3)**2 - (-0.82573 + m.x6)**2 + m.x7
    <= 0)
m.e2733 = Constraint(expr= -(-0.92017 + m.x3)**2 - (-0.59487 + m.x6)**2 + m.x7
    <= 0)
m.e2734 = Constraint(expr= -(-0.55723 + m.x3)**2 - (-0.71653 + m.x6)**2 + m.x7
    <= 0)
m.e2735 = Constraint(expr= -(-0.79337 + m.x3)**2 - (-0.28007 + m.x6)**2 + m.x7
    <= 0)
m.e2736 = Constraint(expr= -(-0.18803 + m.x3)**2 - (-0.17533 + m.x6)**2 + m.x7
    <= 0)
m.e2737 = Constraint(expr= -(-0.53857 + m.x3)**2 - (-0.35727 + m.x6)**2 + m.x7
    <= 0)
m.e2738 = Constraint(expr= -(-0.78683 + m.x3)**2 - (-0.48213 + m.x6)**2 + m.x7
    <= 0)
m.e2739 = Constraint(expr= -(-0.27577 + m.x3)**2 - (-0.14647 + m.x6)**2 + m.x7
    <= 0)
m.e2740 = Constraint(expr= -(-0.63363 + m.x3)**2 - (-0.71693 + m.x6)**2 + m.x7
    <= 0)
m.e2741 = Constraint(expr= -(-0.32497 + m.x3)**2 - (-0.16767 + m.x6)**2 + m.x7
    <= 0)
m.e2742 = Constraint(expr= -(-0.80843 + m.x3)**2 - (-0.75973 + m.x6)**2 + m.x7
    <= 0)
m.e2743 = Constraint(expr= -(-0.20617 + m.x3)**2 - (-0.14087 + m.x6)**2 + m.x7
    <= 0)
m.e2744 = Constraint(expr= -(-0.19123 + m.x3)**2 - (-0.29053 + m.x6)**2 + m.x7
    <= 0)
m.e2745 = Constraint(expr= -(-0.63937 + m.x3)**2 - (-0.98607 + m.x6)**2 + m.x7
    <= 0)
m.e2746 = Constraint(expr= -(-0.46203 + m.x3)**2 - (-0.78933 + m.x6)**2 + m.x7
    <= 0)
m.e2747 = Constraint(expr= -(-0.54457 + m.x3)**2 - (-0.82327 + m.x6)**2 + m.x7
    <= 0)
m.e2748 = Constraint(expr= -(-0.10083 + m.x3)**2 - (-0.53613 + m.x6)**2 + m.x7
    <= 0)
m.e2749 = Constraint(expr= -(-0.04177 + m.x3)**2 - (-0.97247 + m.x6)**2 + m.x7
    <= 0)
m.e2750 = Constraint(expr= -(-0.38763 + m.x3)**2 - (-0.61093 + m.x6)**2 + m.x7
    <= 0)
m.e2751 = Constraint(expr= -(-0.45097 + m.x3)**2 - (-0.95367 + m.x6)**2 + m.x7
    <= 0)
m.e2752 = Constraint(expr= -(-0.40243 + m.x3)**2 - (-0.89373 + m.x6)**2 + m.x7
    <= 0)
m.e2753 = Constraint(expr= -(-0.29217 + m.x3)**2 - (-0.48687 + m.x6)**2 + m.x7
    <= 0)
m.e2754 = Constraint(expr= -(-0.02523 + m.x3)**2 - (-0.06453 + m.x6)**2 + m.x7
    <= 0)
m.e2755 = Constraint(expr= -(-0.28537 + m.x3)**2 - (-0.49207 + m.x6)**2 + m.x7
    <= 0)
m.e2756 = Constraint(expr= -(-0.93603 + m.x3)**2 - (-0.60333 + m.x6)**2 + m.x7
    <= 0)
m.e2757 = Constraint(expr= -(-0.35057 + m.x3)**2 - (-0.08927 + m.x6)**2 + m.x7
    <= 0)
m.e2758 = Constraint(expr= -(-0.61483 + m.x3)**2 - (-0.79013 + m.x6)**2 + m.x7
    <= 0)
m.e2759 = Constraint(expr= -(-0.60777 + m.x3)**2 - (-0.59847 + m.x6)**2 + m.x7
    <= 0)
m.e2760 = Constraint(expr= -(-0.34163 + m.x3)**2 - (-0.70493 + m.x6)**2 + m.x7
    <= 0)
m.e2761 = Constraint(expr= -(-0.37697 + m.x3)**2 - (-0.53967 + m.x6)**2 + m.x7
    <= 0)
m.e2762 = Constraint(expr= -(-0.19643 + m.x3)**2 - (-0.22773 + m.x6)**2 + m.x7
    <= 0)
m.e2763 = Constraint(expr= -(-0.17817 + m.x3)**2 - (-0.63287 + m.x6)**2 + m.x7
    <= 0)
m.e2764 = Constraint(expr= -(-0.05923 + m.x3)**2 - (-0.03853 + m.x6)**2 + m.x7
    <= 0)
m.e2765 = Constraint(expr= -(-0.73137 + m.x3)**2 - (-0.79807 + m.x6)**2 + m.x7
    <= 0)
m.e2766 = Constraint(expr= -(-0.61003 + m.x3)**2 - (-0.61733 + m.x6)**2 + m.x7
    <= 0)
m.e2767 = Constraint(expr= -(-0.95657 + m.x3)**2 - (-0.15527 + m.x6)**2 + m.x7
    <= 0)
m.e2768 = Constraint(expr= -(-0.32883 + m.x3)**2 - (-0.24413 + m.x6)**2 + m.x7
    <= 0)
m.e2769 = Constraint(expr= -(-0.97377 + m.x3)**2 - (-0.02447 + m.x6)**2 + m.x7
    <= 0)
m.e2770 = Constraint(expr= -(-0.49563 + m.x3)**2 - (-0.99893 + m.x6)**2 + m.x7
    <= 0)
m.e2771 = Constraint(expr= -(-0.10297 + m.x3)**2 - (-0.92567 + m.x6)**2 + m.x7
    <= 0)
m.e2772 = Constraint(expr= -(-0.19043 + m.x3)**2 - (-0.76173 + m.x6)**2 + m.x7
    <= 0)
m.e2773 = Constraint(expr= -(-0.86417 + m.x3)**2 - (-0.57887 + m.x6)**2 + m.x7
    <= 0)
m.e2774 = Constraint(expr= -(-0.29323 + m.x3)**2 - (-0.21253 + m.x6)**2 + m.x7
    <= 0)
m.e2775 = Constraint(expr= -(-0.97737 + m.x3)**2 - (-0.90407 + m.x6)**2 + m.x7
    <= 0)
m.e2776 = Constraint(expr= -(-0.48403 + m.x3)**2 - (-0.83133 + m.x6)**2 + m.x7
    <= 0)
m.e2777 = Constraint(expr= -(-0.36257 + m.x3)**2 - (-0.02127 + m.x6)**2 + m.x7
    <= 0)
m.e2778 = Constraint(expr= -(-0.24283 + m.x3)**2 - (-0.89813 + m.x6)**2 + m.x7
    <= 0)
m.e2779 = Constraint(expr= -(-0.13977 + m.x3)**2 - (-0.25047 + m.x6)**2 + m.x7
    <= 0)
m.e2780 = Constraint(expr= -(-0.84963 + m.x3)**2 - (-0.49293 + m.x6)**2 + m.x7
    <= 0)
m.e2781 = Constraint(expr= -(-0.62897 + m.x3)**2 - (-0.11167 + m.x6)**2 + m.x7
    <= 0)
m.e2782 = Constraint(expr= -(-0.38443 + m.x3)**2 - (-0.49573 + m.x6)**2 + m.x7
    <= 0)
m.e2783 = Constraint(expr= -(-0.35017 + m.x3)**2 - (-0.32487 + m.x6)**2 + m.x7
    <= 0)
m.e2784 = Constraint(expr= -(-0.72723 + m.x3)**2 - (-0.58653 + m.x6)**2 + m.x7
    <= 0)
m.e2785 = Constraint(expr= -(-0.02337 + m.x3)**2 - (-0.81007 + m.x6)**2 + m.x7
    <= 0)
m.e2786 = Constraint(expr= -(-0.55803 + m.x3)**2 - (-0.24533 + m.x6)**2 + m.x7
    <= 0)
m.e2787 = Constraint(expr= -(-0.56857 + m.x3)**2 - (-0.68727 + m.x6)**2 + m.x7
    <= 0)
m.e2788 = Constraint(expr= -(-0.35683 + m.x3)**2 - (-0.75213 + m.x6)**2 + m.x7
    <= 0)
m.e2789 = Constraint(expr= -(-0.10577 + m.x3)**2 - (-0.27647 + m.x6)**2 + m.x7
    <= 0)
m.e2790 = Constraint(expr= -(-0.40363 + m.x3)**2 - (-0.18693 + m.x6)**2 + m.x7
    <= 0)
m.e2791 = Constraint(expr= -(-0.95497 + m.x3)**2 - (-0.09767 + m.x6)**2 + m.x7
    <= 0)
m.e2792 = Constraint(expr= -(-0.77843 + m.x3)**2 - (-0.42973 + m.x6)**2 + m.x7
    <= 0)
m.e2793 = Constraint(expr= -(-0.63617 + m.x3)**2 - (-0.87087 + m.x6)**2 + m.x7
    <= 0)
m.e2794 = Constraint(expr= -(-0.36123 + m.x3)**2 - (-0.16053 + m.x6)**2 + m.x7
    <= 0)
m.e2795 = Constraint(expr= -(-0.86937 + m.x3)**2 - (-0.51607 + m.x6)**2 + m.x7
    <= 0)
m.e2796 = Constraint(expr= -(-0.83203 + m.x3)**2 - (-0.85933 + m.x6)**2 + m.x7
    <= 0)
m.e2797 = Constraint(expr= -(-0.57457 + m.x3)**2 - (-0.15327 + m.x6)**2 + m.x7
    <= 0)
m.e2798 = Constraint(expr= -(-0.67083 + m.x3)**2 - (-0.80613 + m.x6)**2 + m.x7
    <= 0)
m.e2799 = Constraint(expr= -(-0.87177 + m.x3)**2 - (-0.10247 + m.x6)**2 + m.x7
    <= 0)
m.e2800 = Constraint(expr= -(-0.15763 + m.x3)**2 - (-0.08093 + m.x6)**2 + m.x7
    <= 0)
m.e2801 = Constraint(expr= -(-0.08097 + m.x3)**2 - (-0.88367 + m.x6)**2 + m.x7
    <= 0)
m.e2802 = Constraint(expr= -(-0.37243 + m.x3)**2 - (-0.56373 + m.x6)**2 + m.x7
    <= 0)
m.e2803 = Constraint(expr= -(-0.72217 + m.x3)**2 - (-0.21687 + m.x6)**2 + m.x7
    <= 0)
m.e2804 = Constraint(expr= -(-0.19523 + m.x3)**2 - (-0.93453 + m.x6)**2 + m.x7
    <= 0)
m.e2805 = Constraint(expr= -(-0.51537 + m.x3)**2 - (-0.02207 + m.x6)**2 + m.x7
    <= 0)
m.e2806 = Constraint(expr= -(-0.30603 + m.x3)**2 - (-0.67333 + m.x6)**2 + m.x7
    <= 0)
m.e2807 = Constraint(expr= -(-0.38057 + m.x3)**2 - (-0.41927 + m.x6)**2 + m.x7
    <= 0)
m.e2808 = Constraint(expr= -(-0.18483 + m.x3)**2 - (-0.06013 + m.x6)**2 + m.x7
    <= 0)
m.e2809 = Constraint(expr= -(-0.43777 + m.x3)**2 - (-0.72847 + m.x6)**2 + m.x7
    <= 0)
m.e2810 = Constraint(expr= -(-0.11163 + m.x3)**2 - (-0.17493 + m.x6)**2 + m.x7
    <= 0)
m.e2811 = Constraint(expr= -(-0.00697 + m.x3)**2 - (-0.46967 + m.x6)**2 + m.x7
    <= 0)
m.e2812 = Constraint(expr= -(-0.16643 + m.x3)**2 - (-0.89773 + m.x6)**2 + m.x7
    <= 0)
m.e2813 = Constraint(expr= -(-0.60817 + m.x3)**2 - (-0.36287 + m.x6)**2 + m.x7
    <= 0)
m.e2814 = Constraint(expr= -(-0.22923 + m.x3)**2 - (-0.90853 + m.x6)**2 + m.x7
    <= 0)
m.e2815 = Constraint(expr= -(-0.96137 + m.x3)**2 - (-0.32807 + m.x6)**2 + m.x7
    <= 0)
m.e2816 = Constraint(expr= -(-0.98003 + m.x3)**2 - (-0.68733 + m.x6)**2 + m.x7
    <= 0)
m.e2817 = Constraint(expr= -(-0.98657 + m.x3)**2 - (-0.48527 + m.x6)**2 + m.x7
    <= 0)
m.e2818 = Constraint(expr= -(-0.89883 + m.x3)**2 - (-0.51413 + m.x6)**2 + m.x7
    <= 0)
m.e2819 = Constraint(expr= -(-0.80377 + m.x3)**2 - (-0.15447 + m.x6)**2 + m.x7
    <= 0)
m.e2820 = Constraint(expr= -(-0.26563 + m.x3)**2 - (-0.46893 + m.x6)**2 + m.x7
    <= 0)
m.e2821 = Constraint(expr= -(-0.73297 + m.x3)**2 - (-0.85567 + m.x6)**2 + m.x7
    <= 0)
m.e2822 = Constraint(expr= -(-0.16043 + m.x3)**2 - (-0.43173 + m.x6)**2 + m.x7
    <= 0)
m.e2823 = Constraint(expr= -(-0.29417 + m.x3)**2 - (-0.30887 + m.x6)**2 + m.x7
    <= 0)
m.e2824 = Constraint(expr= -(-0.46323 + m.x3)**2 - (-0.08253 + m.x6)**2 + m.x7
    <= 0)
m.e2825 = Constraint(expr= -(-0.20737 + m.x3)**2 - (-0.43407 + m.x6)**2 + m.x7
    <= 0)
m.e2826 = Constraint(expr= -(-0.85403 + m.x3)**2 - (-0.90133 + m.x6)**2 + m.x7
    <= 0)
m.e2827 = Constraint(expr= -(-0.39257 + m.x3)**2 - (-0.35127 + m.x6)**2 + m.x7
    <= 0)
m.e2828 = Constraint(expr= -(-0.81283 + m.x3)**2 - (-0.16813 + m.x6)**2 + m.x7
    <= 0)
m.e2829 = Constraint(expr= -(-0.96977 + m.x3)**2 - (-0.38047 + m.x6)**2 + m.x7
    <= 0)
m.e2830 = Constraint(expr= -(-0.61963 + m.x3)**2 - (-0.96293 + m.x6)**2 + m.x7
    <= 0)
m.e2831 = Constraint(expr= -(-0.25897 + m.x3)**2 - (-0.04167 + m.x6)**2 + m.x7
    <= 0)
m.e2832 = Constraint(expr= -(-0.35443 + m.x3)**2 - (-0.16573 + m.x6)**2 + m.x7
    <= 0)
m.e2833 = Constraint(expr= -(-0.78017 + m.x3)**2 - (-0.05487 + m.x6)**2 + m.x7
    <= 0)
m.e2834 = Constraint(expr= -(-0.89723 + m.x3)**2 - (-0.45653 + m.x6)**2 + m.x7
    <= 0)
m.e2835 = Constraint(expr= -(-0.25337 + m.x3)**2 - (-0.34007 + m.x6)**2 + m.x7
    <= 0)
m.e2836 = Constraint(expr= -(-0.92803 + m.x3)**2 - (-0.31533 + m.x6)**2 + m.x7
    <= 0)
m.e2837 = Constraint(expr= -(-0.59857 + m.x3)**2 - (-0.01727 + m.x6)**2 + m.x7
    <= 0)
m.e2838 = Constraint(expr= -(-0.92683 + m.x3)**2 - (-0.02213 + m.x6)**2 + m.x7
    <= 0)
m.e2839 = Constraint(expr= -(-0.93577 + m.x3)**2 - (-0.40647 + m.x6)**2 + m.x7
    <= 0)
m.e2840 = Constraint(expr= -(-0.17363 + m.x3)**2 - (-0.65693 + m.x6)**2 + m.x7
    <= 0)
m.e2841 = Constraint(expr= -(-0.58497 + m.x3)**2 - (-0.02767 + m.x6)**2 + m.x7
    <= 0)
m.e2842 = Constraint(expr= -(-0.74843 + m.x3)**2 - (-0.09973 + m.x6)**2 + m.x7
    <= 0)
m.e2843 = Constraint(expr= -(-0.06617 + m.x3)**2 - (-0.60087 + m.x6)**2 + m.x7
    <= 0)
m.e2844 = Constraint(expr= -(-0.53123 + m.x3)**2 - (-0.03053 + m.x6)**2 + m.x7
    <= 0)
m.e2845 = Constraint(expr= -(-0.09937 + m.x3)**2 - (-0.04607 + m.x6)**2 + m.x7
    <= 0)
m.e2846 = Constraint(expr= -(-0.20203 + m.x3)**2 - (-0.92933 + m.x6)**2 + m.x7
    <= 0)
m.e2847 = Constraint(expr= -(-0.60457 + m.x3)**2 - (-0.48327 + m.x6)**2 + m.x7
    <= 0)
m.e2848 = Constraint(expr= -(-0.24083 + m.x3)**2 - (-0.07613 + m.x6)**2 + m.x7
    <= 0)
m.e2849 = Constraint(expr= -(-0.70177 + m.x3)**2 - (-0.23247 + m.x6)**2 + m.x7
    <= 0)
m.e2850 = Constraint(expr= -(-0.92763 + m.x3)**2 - (-0.55093 + m.x6)**2 + m.x7
    <= 0)
m.e2851 = Constraint(expr= -(-0.71097 + m.x3)**2 - (-0.81367 + m.x6)**2 + m.x7
    <= 0)
m.e2852 = Constraint(expr= -(-0.34243 + m.x3)**2 - (-0.23373 + m.x6)**2 + m.x7
    <= 0)
m.e2853 = Constraint(expr= -(-0.15217 + m.x3)**2 - (-0.94687 + m.x6)**2 + m.x7
    <= 0)
m.e2854 = Constraint(expr= -(-0.36523 + m.x3)**2 - (-0.80453 + m.x6)**2 + m.x7
    <= 0)
m.e2855 = Constraint(expr= -(-0.74537 + m.x3)**2 - (-0.55207 + m.x6)**2 + m.x7
    <= 0)
m.e2856 = Constraint(expr= -(-0.67603 + m.x3)**2 - (-0.74333 + m.x6)**2 + m.x7
    <= 0)
m.e2857 = Constraint(expr= -(-0.41057 + m.x3)**2 - (-0.74927 + m.x6)**2 + m.x7
    <= 0)
m.e2858 = Constraint(expr= -(-0.75483 + m.x3)**2 - (-0.33013 + m.x6)**2 + m.x7
    <= 0)
m.e2859 = Constraint(expr= -(-0.26777 + m.x3)**2 - (-0.85847 + m.x6)**2 + m.x7
    <= 0)
m.e2860 = Constraint(expr= -(-0.88163 + m.x3)**2 - (-0.64493 + m.x6)**2 + m.x7
    <= 0)
m.e2861 = Constraint(expr= -(-0.63697 + m.x3)**2 - (-0.39967 + m.x6)**2 + m.x7
    <= 0)
m.e2862 = Constraint(expr= -(-0.13643 + m.x3)**2 - (-0.56773 + m.x6)**2 + m.x7
    <= 0)
m.e2863 = Constraint(expr= -(-0.03817 + m.x3)**2 - (-0.09287 + m.x6)**2 + m.x7
    <= 0)
m.e2864 = Constraint(expr= -(-0.39923 + m.x3)**2 - (-0.77853 + m.x6)**2 + m.x7
    <= 0)
m.e2865 = Constraint(expr= -(-0.19137 + m.x3)**2 - (-0.85807 + m.x6)**2 + m.x7
    <= 0)
m.e2866 = Constraint(expr= -(-0.35003 + m.x3)**2 - (-0.75733 + m.x6)**2 + m.x7
    <= 0)
m.e2867 = Constraint(expr= -(-0.01657 + m.x3)**2 - (-0.81527 + m.x6)**2 + m.x7
    <= 0)
m.e2868 = Constraint(expr= -(-0.46883 + m.x3)**2 - (-0.78413 + m.x6)**2 + m.x7
    <= 0)
m.e2869 = Constraint(expr= -(-0.63377 + m.x3)**2 - (-0.28447 + m.x6)**2 + m.x7
    <= 0)
m.e2870 = Constraint(expr= -(-0.03563 + m.x3)**2 - (-0.93893 + m.x6)**2 + m.x7
    <= 0)
m.e2871 = Constraint(expr= -(-0.36297 + m.x3)**2 - (-0.78567 + m.x6)**2 + m.x7
    <= 0)
m.e2872 = Constraint(expr= -(-0.13043 + m.x3)**2 - (-0.10173 + m.x6)**2 + m.x7
    <= 0)
m.e2873 = Constraint(expr= -(-0.72417 + m.x3)**2 - (-0.03887 + m.x6)**2 + m.x7
    <= 0)
m.e2874 = Constraint(expr= -(-0.63323 + m.x3)**2 - (-0.95253 + m.x6)**2 + m.x7
    <= 0)
m.e2875 = Constraint(expr= -(-0.43737 + m.x3)**2 - (-0.96407 + m.x6)**2 + m.x7
    <= 0)
m.e2876 = Constraint(expr= -(-0.22403 + m.x3)**2 - (-0.97133 + m.x6)**2 + m.x7
    <= 0)
m.e2877 = Constraint(expr= -(-0.42257 + m.x3)**2 - (-0.68127 + m.x6)**2 + m.x7
    <= 0)
m.e2878 = Constraint(expr= -(-0.38283 + m.x3)**2 - (-0.43813 + m.x6)**2 + m.x7
    <= 0)
m.e2879 = Constraint(expr= -(-0.79977 + m.x3)**2 - (-0.51047 + m.x6)**2 + m.x7
    <= 0)
m.e2880 = Constraint(expr= -(-0.38963 + m.x3)**2 - (-0.43293 + m.x6)**2 + m.x7
    <= 0)
m.e2881 = Constraint(expr= -(-0.88897 + m.x3)**2 - (-0.97167 + m.x6)**2 + m.x7
    <= 0)
m.e2882 = Constraint(expr= -(-0.32443 + m.x3)**2 - (-0.83573 + m.x6)**2 + m.x7
    <= 0)
m.e2883 = Constraint(expr= -(-0.21017 + m.x3)**2 - (-0.78487 + m.x6)**2 + m.x7
    <= 0)
m.e2884 = Constraint(expr= -(-0.06723 + m.x3)**2 - (-0.32653 + m.x6)**2 + m.x7
    <= 0)
m.e2885 = Constraint(expr= -(-0.48337 + m.x3)**2 - (-0.87007 + m.x6)**2 + m.x7
    <= 0)
m.e2886 = Constraint(expr= -(-0.29803 + m.x3)**2 - (-0.38533 + m.x6)**2 + m.x7
    <= 0)
m.e2887 = Constraint(expr= -(-0.62857 + m.x3)**2 - (-0.34727 + m.x6)**2 + m.x7
    <= 0)
m.e2888 = Constraint(expr= -(-0.49683 + m.x3)**2 - (-0.29213 + m.x6)**2 + m.x7
    <= 0)
m.e2889 = Constraint(expr= -(-0.76577 + m.x3)**2 - (-0.53647 + m.x6)**2 + m.x7
    <= 0)
m.e2890 = Constraint(expr= -(-0.94363 + m.x3)**2 - (-0.12693 + m.x6)**2 + m.x7
    <= 0)
m.e2891 = Constraint(expr= -(-0.21497 + m.x3)**2 - (-0.95767 + m.x6)**2 + m.x7
    <= 0)
m.e2892 = Constraint(expr= -(-0.71843 + m.x3)**2 - (-0.76973 + m.x6)**2 + m.x7
    <= 0)
m.e2893 = Constraint(expr= -(-0.49617 + m.x3)**2 - (-0.33087 + m.x6)**2 + m.x7
    <= 0)
m.e2894 = Constraint(expr= -(-0.70123 + m.x3)**2 - (-0.90053 + m.x6)**2 + m.x7
    <= 0)
m.e2895 = Constraint(expr= -(-0.32937 + m.x3)**2 - (-0.57607 + m.x6)**2 + m.x7
    <= 0)
m.e2896 = Constraint(expr= -(-0.57203 + m.x3)**2 - (-0.99933 + m.x6)**2 + m.x7
    <= 0)
m.e2897 = Constraint(expr= -(-0.63457 + m.x3)**2 - (-0.81327 + m.x6)**2 + m.x7
    <= 0)
m.e2898 = Constraint(expr= -(-0.81083 + m.x3)**2 - (-0.34613 + m.x6)**2 + m.x7
    <= 0)
m.e2899 = Constraint(expr= -(-0.53177 + m.x3)**2 - (-0.36247 + m.x6)**2 + m.x7
    <= 0)
m.e2900 = Constraint(expr= -(-0.69763 + m.x3)**2 - (-0.02093 + m.x6)**2 + m.x7
    <= 0)
m.e2901 = Constraint(expr= -(-0.34097 + m.x3)**2 - (-0.74367 + m.x6)**2 + m.x7
    <= 0)
m.e2902 = Constraint(expr= -(-0.31243 + m.x3)**2 - (-0.90373 + m.x6)**2 + m.x7
    <= 0)
m.e2903 = Constraint(expr= -(-0.58217 + m.x3)**2 - (-0.67687 + m.x6)**2 + m.x7
    <= 0)
m.e2904 = Constraint(expr= -(-0.53523 + m.x3)**2 - (-0.67453 + m.x6)**2 + m.x7
    <= 0)
m.e2905 = Constraint(expr= -(-0.97537 + m.x3)**2 - (-0.08207 + m.x6)**2 + m.x7
    <= 0)
m.e2906 = Constraint(expr= -(-0.04603 + m.x3)**2 - (-0.81333 + m.x6)**2 + m.x7
    <= 0)
m.e2907 = Constraint(expr= -(-0.44057 + m.x3)**2 - (-0.07927 + m.x6)**2 + m.x7
    <= 0)
m.e2908 = Constraint(expr= -(-0.32483 + m.x3)**2 - (-0.60013 + m.x6)**2 + m.x7
    <= 0)
m.e2909 = Constraint(expr= -(-0.09777 + m.x3)**2 - (-0.98847 + m.x6)**2 + m.x7
    <= 0)
m.e2910 = Constraint(expr= -(-0.65163 + m.x3)**2 - (-0.11493 + m.x6)**2 + m.x7
    <= 0)
m.e2911 = Constraint(expr= -(-0.26697 + m.x3)**2 - (-0.32967 + m.x6)**2 + m.x7
    <= 0)
m.e2912 = Constraint(expr= -(-0.10643 + m.x3)**2 - (-0.23773 + m.x6)**2 + m.x7
    <= 0)
m.e2913 = Constraint(expr= -(-0.46817 + m.x3)**2 - (-0.82287 + m.x6)**2 + m.x7
    <= 0)
m.e2914 = Constraint(expr= -(-0.56923 + m.x3)**2 - (-0.64853 + m.x6)**2 + m.x7
    <= 0)
m.e2915 = Constraint(expr= -(-0.42137 + m.x3)**2 - (-0.38807 + m.x6)**2 + m.x7
    <= 0)
m.e2916 = Constraint(expr= -(-0.72003 + m.x3)**2 - (-0.82733 + m.x6)**2 + m.x7
    <= 0)
m.e2917 = Constraint(expr= -(-0.04657 + m.x3)**2 - (-0.14527 + m.x6)**2 + m.x7
    <= 0)
m.e2918 = Constraint(expr= -(-0.03883 + m.x3)**2 - (-0.05413 + m.x6)**2 + m.x7
    <= 0)
m.e2919 = Constraint(expr= -(-0.46377 + m.x3)**2 - (-0.41447 + m.x6)**2 + m.x7
    <= 0)
m.e2920 = Constraint(expr= -(-0.80563 + m.x3)**2 - (-0.40893 + m.x6)**2 + m.x7
    <= 0)
m.e2921 = Constraint(expr= -(-0.99297 + m.x3)**2 - (-0.71567 + m.x6)**2 + m.x7
    <= 0)
m.e2922 = Constraint(expr= -(-0.10043 + m.x3)**2 - (-0.77173 + m.x6)**2 + m.x7
    <= 0)
m.e2923 = Constraint(expr= -(-0.15417 + m.x3)**2 - (-0.76887 + m.x6)**2 + m.x7
    <= 0)
m.e2924 = Constraint(expr= -(-0.80323 + m.x3)**2 - (-0.82253 + m.x6)**2 + m.x7
    <= 0)
m.e2925 = Constraint(expr= -(-0.66737 + m.x3)**2 - (-0.49407 + m.x6)**2 + m.x7
    <= 0)
m.e2926 = Constraint(expr= -(-0.59403 + m.x3)**2 - (-0.04133 + m.x6)**2 + m.x7
    <= 0)
m.e2927 = Constraint(expr= -(-0.45257 + m.x3)**2 - (-0.01127 + m.x6)**2 + m.x7
    <= 0)
m.e2928 = Constraint(expr= -(-0.95283 + m.x3)**2 - (-0.70813 + m.x6)**2 + m.x7
    <= 0)
m.e2929 = Constraint(expr= -(-0.62977 + m.x3)**2 - (-0.64047 + m.x6)**2 + m.x7
    <= 0)
m.e2930 = Constraint(expr= -(-0.15963 + m.x3)**2 - (-0.90293 + m.x6)**2 + m.x7
    <= 0)
m.e2931 = Constraint(expr= -(-0.51897 + m.x3)**2 - (-0.90167 + m.x6)**2 + m.x7
    <= 0)
m.e2932 = Constraint(expr= -(-0.29443 + m.x3)**2 - (-0.50573 + m.x6)**2 + m.x7
    <= 0)
m.e2933 = Constraint(expr= -(-0.64017 + m.x3)**2 - (-0.51487 + m.x6)**2 + m.x7
    <= 0)
m.e2934 = Constraint(expr= -(-0.23723 + m.x3)**2 - (-0.19653 + m.x6)**2 + m.x7
    <= 0)
m.e2935 = Constraint(expr= -(-0.71337 + m.x3)**2 - (-0.40007 + m.x6)**2 + m.x7
    <= 0)
m.e2936 = Constraint(expr= -(-0.66803 + m.x3)**2 - (-0.45533 + m.x6)**2 + m.x7
    <= 0)
m.e2937 = Constraint(expr= -(-0.65857 + m.x3)**2 - (-0.67727 + m.x6)**2 + m.x7
    <= 0)
m.e2938 = Constraint(expr= -(-0.06683 + m.x3)**2 - (-0.56213 + m.x6)**2 + m.x7
    <= 0)
m.e2939 = Constraint(expr= -(-0.59577 + m.x3)**2 - (-0.66647 + m.x6)**2 + m.x7
    <= 0)
m.e2940 = Constraint(expr= -(-0.71363 + m.x3)**2 - (-0.59693 + m.x6)**2 + m.x7
    <= 0)
m.e2941 = Constraint(expr= -(-0.84497 + m.x3)**2 - (-0.88767 + m.x6)**2 + m.x7
    <= 0)
m.e2942 = Constraint(expr= -(-0.68843 + m.x3)**2 - (-0.43973 + m.x6)**2 + m.x7
    <= 0)
m.e2943 = Constraint(expr= -(-0.92617 + m.x3)**2 - (-0.06087 + m.x6)**2 + m.x7
    <= 0)
m.e2944 = Constraint(expr= -(-0.87123 + m.x3)**2 - (-0.77053 + m.x6)**2 + m.x7
    <= 0)
m.e2945 = Constraint(expr= -(-0.55937 + m.x3)**2 - (-0.10607 + m.x6)**2 + m.x7
    <= 0)
m.e2946 = Constraint(expr= -(-0.94203 + m.x3)**2 - (-0.06933 + m.x6)**2 + m.x7
    <= 0)
m.e2947 = Constraint(expr= -(-0.66457 + m.x3)**2 - (-0.14327 + m.x6)**2 + m.x7
    <= 0)
m.e2948 = Constraint(expr= -(-0.38083 + m.x3)**2 - (-0.61613 + m.x6)**2 + m.x7
    <= 0)
m.e2949 = Constraint(expr= -(-0.36177 + m.x3)**2 - (-0.49247 + m.x6)**2 + m.x7
    <= 0)
m.e2950 = Constraint(expr= -(-0.46763 + m.x3)**2 - (-0.49093 + m.x6)**2 + m.x7
    <= 0)
m.e2951 = Constraint(expr= -(-0.97097 + m.x3)**2 - (-0.67367 + m.x6)**2 + m.x7
    <= 0)
m.e2952 = Constraint(expr= -(-0.28243 + m.x3)**2 - (-0.57373 + m.x6)**2 + m.x7
    <= 0)
m.e2953 = Constraint(expr= -(-0.01217 + m.x3)**2 - (-0.40687 + m.x6)**2 + m.x7
    <= 0)
m.e2954 = Constraint(expr= -(-0.70523 + m.x3)**2 - (-0.54453 + m.x6)**2 + m.x7
    <= 0)
m.e2955 = Constraint(expr= -(-0.20537 + m.x3)**2 - (-0.61207 + m.x6)**2 + m.x7
    <= 0)
m.e2956 = Constraint(expr= -(-0.41603 + m.x3)**2 - (-0.88333 + m.x6)**2 + m.x7
    <= 0)
m.e2957 = Constraint(expr= -(-0.47057 + m.x3)**2 - (-0.40927 + m.x6)**2 + m.x7
    <= 0)
m.e2958 = Constraint(expr= -(-0.89483 + m.x3)**2 - (-0.87013 + m.x6)**2 + m.x7
    <= 0)
m.e2959 = Constraint(expr= -(-0.92777 + m.x3)**2 - (-0.11847 + m.x6)**2 + m.x7
    <= 0)
m.e2960 = Constraint(expr= -(-0.42163 + m.x3)**2 - (-0.58493 + m.x6)**2 + m.x7
    <= 0)
m.e2961 = Constraint(expr= -(-0.89697 + m.x3)**2 - (-0.25967 + m.x6)**2 + m.x7
    <= 0)
m.e2962 = Constraint(expr= -(-0.07643 + m.x3)**2 - (-0.90773 + m.x6)**2 + m.x7
    <= 0)
m.e2963 = Constraint(expr= -(-0.89817 + m.x3)**2 - (-0.55287 + m.x6)**2 + m.x7
    <= 0)
m.e2964 = Constraint(expr= -(-0.73923 + m.x3)**2 - (-0.51853 + m.x6)**2 + m.x7
    <= 0)
m.e2965 = Constraint(expr= -(-0.65137 + m.x3)**2 - (-0.91807 + m.x6)**2 + m.x7
    <= 0)
m.e2966 = Constraint(expr= -(-0.09003 + m.x3)**2 - (-0.89733 + m.x6)**2 + m.x7
    <= 0)
m.e2967 = Constraint(expr= -(-0.07657 + m.x3)**2 - (-0.47527 + m.x6)**2 + m.x7
    <= 0)
m.e2968 = Constraint(expr= -(-0.60883 + m.x3)**2 - (-0.32413 + m.x6)**2 + m.x7
    <= 0)
m.e2969 = Constraint(expr= -(-0.29377 + m.x3)**2 - (-0.54447 + m.x6)**2 + m.x7
    <= 0)
m.e2970 = Constraint(expr= -(-0.57563 + m.x3)**2 - (-0.87893 + m.x6)**2 + m.x7
    <= 0)
m.e2971 = Constraint(expr= -(-0.62297 + m.x3)**2 - (-0.64567 + m.x6)**2 + m.x7
    <= 0)
m.e2972 = Constraint(expr= -(-0.07043 + m.x3)**2 - (-0.44173 + m.x6)**2 + m.x7
    <= 0)
m.e2973 = Constraint(expr= -(-0.58417 + m.x3)**2 - (-0.49887 + m.x6)**2 + m.x7
    <= 0)
m.e2974 = Constraint(expr= -(-0.97323 + m.x3)**2 - (-0.69253 + m.x6)**2 + m.x7
    <= 0)
m.e2975 = Constraint(expr= -(-0.89737 + m.x3)**2 - (-0.02407 + m.x6)**2 + m.x7
    <= 0)
m.e2976 = Constraint(expr= -(-0.96403 + m.x3)**2 - (-0.11133 + m.x6)**2 + m.x7
    <= 0)
m.e2977 = Constraint(expr= -(-0.48257 + m.x3)**2 - (-0.34127 + m.x6)**2 + m.x7
    <= 0)
m.e2978 = Constraint(expr= -(-0.52283 + m.x3)**2 - (-0.97813 + m.x6)**2 + m.x7
    <= 0)
m.e2979 = Constraint(expr= -(-0.45977 + m.x3)**2 - (-0.77047 + m.x6)**2 + m.x7
    <= 0)
m.e2980 = Constraint(expr= -(-0.92963 + m.x3)**2 - (-0.37293 + m.x6)**2 + m.x7
    <= 0)
m.e2981 = Constraint(expr= -(-0.14897 + m.x3)**2 - (-0.83167 + m.x6)**2 + m.x7
    <= 0)
m.e2982 = Constraint(expr= -(-0.26443 + m.x3)**2 - (-0.17573 + m.x6)**2 + m.x7
    <= 0)
m.e2983 = Constraint(expr= -(-0.07017 + m.x3)**2 - (-0.24487 + m.x6)**2 + m.x7
    <= 0)
m.e2984 = Constraint(expr= -(-0.40723 + m.x3)**2 - (-0.06653 + m.x6)**2 + m.x7
    <= 0)
m.e2985 = Constraint(expr= -(-0.94337 + m.x3)**2 - (-0.93007 + m.x6)**2 + m.x7
    <= 0)
m.e2986 = Constraint(expr= -(-0.03803 + m.x3)**2 - (-0.52533 + m.x6)**2 + m.x7
    <= 0)
m.e2987 = Constraint(expr= -(-0.68857 + m.x3)**2 - (-0.00727 + m.x6)**2 + m.x7
    <= 0)
m.e2988 = Constraint(expr= -(-0.63683 + m.x3)**2 - (-0.83213 + m.x6)**2 + m.x7
    <= 0)
m.e2989 = Constraint(expr= -(-0.42577 + m.x3)**2 - (-0.79647 + m.x6)**2 + m.x7
    <= 0)
m.e2990 = Constraint(expr= -(-0.48363 + m.x3)**2 - (-0.06693 + m.x6)**2 + m.x7
    <= 0)
m.e2991 = Constraint(expr= -(-0.47497 + m.x3)**2 - (-0.81767 + m.x6)**2 + m.x7
    <= 0)
m.e2992 = Constraint(expr= -(-0.65843 + m.x3)**2 - (-0.10973 + m.x6)**2 + m.x7
    <= 0)
m.e2993 = Constraint(expr= -(-0.35617 + m.x3)**2 - (-0.79087 + m.x6)**2 + m.x7
    <= 0)
m.e2994 = Constraint(expr= -(-0.04123 + m.x3)**2 - (-0.64053 + m.x6)**2 + m.x7
    <= 0)
m.e2995 = Constraint(expr= -(-0.78937 + m.x3)**2 - (-0.63607 + m.x6)**2 + m.x7
    <= 0)
m.e2996 = Constraint(expr= -(-0.31203 + m.x3)**2 - (-0.13933 + m.x6)**2 + m.x7
    <= 0)
m.e2997 = Constraint(expr= -(-0.69457 + m.x3)**2 - (-0.47327 + m.x6)**2 + m.x7
    <= 0)
m.e2998 = Constraint(expr= -(-0.95083 + m.x3)**2 - (-0.88613 + m.x6)**2 + m.x7
    <= 0)
m.e2999 = Constraint(expr= -(-0.19177 + m.x3)**2 - (-0.62247 + m.x6)**2 + m.x7
    <= 0)
m.e3000 = Constraint(expr= -(-0.23763 + m.x3)**2 - (-0.96093 + m.x6)**2 + m.x7
    <= 0)
m.e3001 = Constraint(expr= -(m.x1 - m.x2)**2 - (m.x4 - m.x5)**2
    <= -0.3333333333333333)
m.e3002 = Constraint(expr= -(m.x1 - m.x3)**2 - (m.x4 - m.x6)**2
    <= -0.3333333333333333)
m.e3003 = Constraint(expr= -(m.x2 - m.x3)**2 - (m.x5 - m.x6)**2
    <= -0.3333333333333333)
