# NLP written by GAMS Convert at 05/15/24 11:47:59
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#        26       26        0        0        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        78       78        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#        78        0       78
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

m.obj = Objective(sense=minimize, expr= 1 / sqrt((m.x1 - m.x2)**2 + (m.x27 -
    m.x28)**2 + (m.x53 - m.x54)**2) + 1 / sqrt((m.x1 - m.x3)**2 + (m.x27 -
    m.x29)**2 + (m.x53 - m.x55)**2) + 1 / sqrt((m.x1 - m.x4)**2 + (m.x27 -
    m.x30)**2 + (m.x53 - m.x56)**2) + 1 / sqrt((m.x1 - m.x5)**2 + (m.x27 -
    m.x31)**2 + (m.x53 - m.x57)**2) + 1 / sqrt((m.x1 - m.x6)**2 + (m.x27 -
    m.x32)**2 + (m.x53 - m.x58)**2) + 1 / sqrt((m.x1 - m.x7)**2 + (m.x27 -
    m.x33)**2 + (m.x53 - m.x59)**2) + 1 / sqrt((m.x1 - m.x8)**2 + (m.x27 -
    m.x34)**2 + (m.x53 - m.x60)**2) + 1 / sqrt((m.x1 - m.x9)**2 + (m.x27 -
    m.x35)**2 + (m.x53 - m.x61)**2) + 1 / sqrt((m.x1 - m.x10)**2 + (m.x27 -
    m.x36)**2 + (m.x53 - m.x62)**2) + 1 / sqrt((m.x1 - m.x11)**2 + (m.x27 -
    m.x37)**2 + (m.x53 - m.x63)**2) + 1 / sqrt((m.x1 - m.x12)**2 + (m.x27 -
    m.x38)**2 + (m.x53 - m.x64)**2) + 1 / sqrt((m.x1 - m.x13)**2 + (m.x27 -
    m.x39)**2 + (m.x53 - m.x65)**2) + 1 / sqrt((m.x1 - m.x14)**2 + (m.x27 -
    m.x40)**2 + (m.x53 - m.x66)**2) + 1 / sqrt((m.x1 - m.x15)**2 + (m.x27 -
    m.x41)**2 + (m.x53 - m.x67)**2) + 1 / sqrt((m.x1 - m.x16)**2 + (m.x27 -
    m.x42)**2 + (m.x53 - m.x68)**2) + 1 / sqrt((m.x1 - m.x17)**2 + (m.x27 -
    m.x43)**2 + (m.x53 - m.x69)**2) + 1 / sqrt((m.x1 - m.x18)**2 + (m.x27 -
    m.x44)**2 + (m.x53 - m.x70)**2) + 1 / sqrt((m.x1 - m.x19)**2 + (m.x27 -
    m.x45)**2 + (m.x53 - m.x71)**2) + 1 / sqrt((m.x1 - m.x20)**2 + (m.x27 -
    m.x46)**2 + (m.x53 - m.x72)**2) + 1 / sqrt((m.x1 - m.x21)**2 + (m.x27 -
    m.x47)**2 + (m.x53 - m.x73)**2) + 1 / sqrt((m.x1 - m.x22)**2 + (m.x27 -
    m.x48)**2 + (m.x53 - m.x74)**2) + 1 / sqrt((m.x1 - m.x23)**2 + (m.x27 -
    m.x49)**2 + (m.x53 - m.x75)**2) + 1 / sqrt((m.x1 - m.x24)**2 + (m.x27 -
    m.x50)**2 + (m.x53 - m.x76)**2) + 1 / sqrt((m.x1 - m.x25)**2 + (m.x27 -
    m.x51)**2 + (m.x53 - m.x77)**2) + 1 / sqrt((m.x1 - m.x26)**2 + (m.x27 -
    m.x52)**2 + (m.x53 - m.x78)**2) + 1 / sqrt((m.x2 - m.x3)**2 + (m.x28 -
    m.x29)**2 + (m.x54 - m.x55)**2) + 1 / sqrt((m.x2 - m.x4)**2 + (m.x28 -
    m.x30)**2 + (m.x54 - m.x56)**2) + 1 / sqrt((m.x2 - m.x5)**2 + (m.x28 -
    m.x31)**2 + (m.x54 - m.x57)**2) + 1 / sqrt((m.x2 - m.x6)**2 + (m.x28 -
    m.x32)**2 + (m.x54 - m.x58)**2) + 1 / sqrt((m.x2 - m.x7)**2 + (m.x28 -
    m.x33)**2 + (m.x54 - m.x59)**2) + 1 / sqrt((m.x2 - m.x8)**2 + (m.x28 -
    m.x34)**2 + (m.x54 - m.x60)**2) + 1 / sqrt((m.x2 - m.x9)**2 + (m.x28 -
    m.x35)**2 + (m.x54 - m.x61)**2) + 1 / sqrt((m.x2 - m.x10)**2 + (m.x28 -
    m.x36)**2 + (m.x54 - m.x62)**2) + 1 / sqrt((m.x2 - m.x11)**2 + (m.x28 -
    m.x37)**2 + (m.x54 - m.x63)**2) + 1 / sqrt((m.x2 - m.x12)**2 + (m.x28 -
    m.x38)**2 + (m.x54 - m.x64)**2) + 1 / sqrt((m.x2 - m.x13)**2 + (m.x28 -
    m.x39)**2 + (m.x54 - m.x65)**2) + 1 / sqrt((m.x2 - m.x14)**2 + (m.x28 -
    m.x40)**2 + (m.x54 - m.x66)**2) + 1 / sqrt((m.x2 - m.x15)**2 + (m.x28 -
    m.x41)**2 + (m.x54 - m.x67)**2) + 1 / sqrt((m.x2 - m.x16)**2 + (m.x28 -
    m.x42)**2 + (m.x54 - m.x68)**2) + 1 / sqrt((m.x2 - m.x17)**2 + (m.x28 -
    m.x43)**2 + (m.x54 - m.x69)**2) + 1 / sqrt((m.x2 - m.x18)**2 + (m.x28 -
    m.x44)**2 + (m.x54 - m.x70)**2) + 1 / sqrt((m.x2 - m.x19)**2 + (m.x28 -
    m.x45)**2 + (m.x54 - m.x71)**2) + 1 / sqrt((m.x2 - m.x20)**2 + (m.x28 -
    m.x46)**2 + (m.x54 - m.x72)**2) + 1 / sqrt((m.x2 - m.x21)**2 + (m.x28 -
    m.x47)**2 + (m.x54 - m.x73)**2) + 1 / sqrt((m.x2 - m.x22)**2 + (m.x28 -
    m.x48)**2 + (m.x54 - m.x74)**2) + 1 / sqrt((m.x2 - m.x23)**2 + (m.x28 -
    m.x49)**2 + (m.x54 - m.x75)**2) + 1 / sqrt((m.x2 - m.x24)**2 + (m.x28 -
    m.x50)**2 + (m.x54 - m.x76)**2) + 1 / sqrt((m.x2 - m.x25)**2 + (m.x28 -
    m.x51)**2 + (m.x54 - m.x77)**2) + 1 / sqrt((m.x2 - m.x26)**2 + (m.x28 -
    m.x52)**2 + (m.x54 - m.x78)**2) + 1 / sqrt((m.x3 - m.x4)**2 + (m.x29 -
    m.x30)**2 + (m.x55 - m.x56)**2) + 1 / sqrt((m.x3 - m.x5)**2 + (m.x29 -
    m.x31)**2 + (m.x55 - m.x57)**2) + 1 / sqrt((m.x3 - m.x6)**2 + (m.x29 -
    m.x32)**2 + (m.x55 - m.x58)**2) + 1 / sqrt((m.x3 - m.x7)**2 + (m.x29 -
    m.x33)**2 + (m.x55 - m.x59)**2) + 1 / sqrt((m.x3 - m.x8)**2 + (m.x29 -
    m.x34)**2 + (m.x55 - m.x60)**2) + 1 / sqrt((m.x3 - m.x9)**2 + (m.x29 -
    m.x35)**2 + (m.x55 - m.x61)**2) + 1 / sqrt((m.x3 - m.x10)**2 + (m.x29 -
    m.x36)**2 + (m.x55 - m.x62)**2) + 1 / sqrt((m.x3 - m.x11)**2 + (m.x29 -
    m.x37)**2 + (m.x55 - m.x63)**2) + 1 / sqrt((m.x3 - m.x12)**2 + (m.x29 -
    m.x38)**2 + (m.x55 - m.x64)**2) + 1 / sqrt((m.x3 - m.x13)**2 + (m.x29 -
    m.x39)**2 + (m.x55 - m.x65)**2) + 1 / sqrt((m.x3 - m.x14)**2 + (m.x29 -
    m.x40)**2 + (m.x55 - m.x66)**2) + 1 / sqrt((m.x3 - m.x15)**2 + (m.x29 -
    m.x41)**2 + (m.x55 - m.x67)**2) + 1 / sqrt((m.x3 - m.x16)**2 + (m.x29 -
    m.x42)**2 + (m.x55 - m.x68)**2) + 1 / sqrt((m.x3 - m.x17)**2 + (m.x29 -
    m.x43)**2 + (m.x55 - m.x69)**2) + 1 / sqrt((m.x3 - m.x18)**2 + (m.x29 -
    m.x44)**2 + (m.x55 - m.x70)**2) + 1 / sqrt((m.x3 - m.x19)**2 + (m.x29 -
    m.x45)**2 + (m.x55 - m.x71)**2) + 1 / sqrt((m.x3 - m.x20)**2 + (m.x29 -
    m.x46)**2 + (m.x55 - m.x72)**2) + 1 / sqrt((m.x3 - m.x21)**2 + (m.x29 -
    m.x47)**2 + (m.x55 - m.x73)**2) + 1 / sqrt((m.x3 - m.x22)**2 + (m.x29 -
    m.x48)**2 + (m.x55 - m.x74)**2) + 1 / sqrt((m.x3 - m.x23)**2 + (m.x29 -
    m.x49)**2 + (m.x55 - m.x75)**2) + 1 / sqrt((m.x3 - m.x24)**2 + (m.x29 -
    m.x50)**2 + (m.x55 - m.x76)**2) + 1 / sqrt((m.x3 - m.x25)**2 + (m.x29 -
    m.x51)**2 + (m.x55 - m.x77)**2) + 1 / sqrt((m.x3 - m.x26)**2 + (m.x29 -
    m.x52)**2 + (m.x55 - m.x78)**2) + 1 / sqrt((m.x4 - m.x5)**2 + (m.x30 -
    m.x31)**2 + (m.x56 - m.x57)**2) + 1 / sqrt((m.x4 - m.x6)**2 + (m.x30 -
    m.x32)**2 + (m.x56 - m.x58)**2) + 1 / sqrt((m.x4 - m.x7)**2 + (m.x30 -
    m.x33)**2 + (m.x56 - m.x59)**2) + 1 / sqrt((m.x4 - m.x8)**2 + (m.x30 -
    m.x34)**2 + (m.x56 - m.x60)**2) + 1 / sqrt((m.x4 - m.x9)**2 + (m.x30 -
    m.x35)**2 + (m.x56 - m.x61)**2) + 1 / sqrt((m.x4 - m.x10)**2 + (m.x30 -
    m.x36)**2 + (m.x56 - m.x62)**2) + 1 / sqrt((m.x4 - m.x11)**2 + (m.x30 -
    m.x37)**2 + (m.x56 - m.x63)**2) + 1 / sqrt((m.x4 - m.x12)**2 + (m.x30 -
    m.x38)**2 + (m.x56 - m.x64)**2) + 1 / sqrt((m.x4 - m.x13)**2 + (m.x30 -
    m.x39)**2 + (m.x56 - m.x65)**2) + 1 / sqrt((m.x4 - m.x14)**2 + (m.x30 -
    m.x40)**2 + (m.x56 - m.x66)**2) + 1 / sqrt((m.x4 - m.x15)**2 + (m.x30 -
    m.x41)**2 + (m.x56 - m.x67)**2) + 1 / sqrt((m.x4 - m.x16)**2 + (m.x30 -
    m.x42)**2 + (m.x56 - m.x68)**2) + 1 / sqrt((m.x4 - m.x17)**2 + (m.x30 -
    m.x43)**2 + (m.x56 - m.x69)**2) + 1 / sqrt((m.x4 - m.x18)**2 + (m.x30 -
    m.x44)**2 + (m.x56 - m.x70)**2) + 1 / sqrt((m.x4 - m.x19)**2 + (m.x30 -
    m.x45)**2 + (m.x56 - m.x71)**2) + 1 / sqrt((m.x4 - m.x20)**2 + (m.x30 -
    m.x46)**2 + (m.x56 - m.x72)**2) + 1 / sqrt((m.x4 - m.x21)**2 + (m.x30 -
    m.x47)**2 + (m.x56 - m.x73)**2) + 1 / sqrt((m.x4 - m.x22)**2 + (m.x30 -
    m.x48)**2 + (m.x56 - m.x74)**2) + 1 / sqrt((m.x4 - m.x23)**2 + (m.x30 -
    m.x49)**2 + (m.x56 - m.x75)**2) + 1 / sqrt((m.x4 - m.x24)**2 + (m.x30 -
    m.x50)**2 + (m.x56 - m.x76)**2) + 1 / sqrt((m.x4 - m.x25)**2 + (m.x30 -
    m.x51)**2 + (m.x56 - m.x77)**2) + 1 / sqrt((m.x4 - m.x26)**2 + (m.x30 -
    m.x52)**2 + (m.x56 - m.x78)**2) + 1 / sqrt((m.x5 - m.x6)**2 + (m.x31 -
    m.x32)**2 + (m.x57 - m.x58)**2) + 1 / sqrt((m.x5 - m.x7)**2 + (m.x31 -
    m.x33)**2 + (m.x57 - m.x59)**2) + 1 / sqrt((m.x5 - m.x8)**2 + (m.x31 -
    m.x34)**2 + (m.x57 - m.x60)**2) + 1 / sqrt((m.x5 - m.x9)**2 + (m.x31 -
    m.x35)**2 + (m.x57 - m.x61)**2) + 1 / sqrt((m.x5 - m.x10)**2 + (m.x31 -
    m.x36)**2 + (m.x57 - m.x62)**2) + 1 / sqrt((m.x5 - m.x11)**2 + (m.x31 -
    m.x37)**2 + (m.x57 - m.x63)**2) + 1 / sqrt((m.x5 - m.x12)**2 + (m.x31 -
    m.x38)**2 + (m.x57 - m.x64)**2) + 1 / sqrt((m.x5 - m.x13)**2 + (m.x31 -
    m.x39)**2 + (m.x57 - m.x65)**2) + 1 / sqrt((m.x5 - m.x14)**2 + (m.x31 -
    m.x40)**2 + (m.x57 - m.x66)**2) + 1 / sqrt((m.x5 - m.x15)**2 + (m.x31 -
    m.x41)**2 + (m.x57 - m.x67)**2) + 1 / sqrt((m.x5 - m.x16)**2 + (m.x31 -
    m.x42)**2 + (m.x57 - m.x68)**2) + 1 / sqrt((m.x5 - m.x17)**2 + (m.x31 -
    m.x43)**2 + (m.x57 - m.x69)**2) + 1 / sqrt((m.x5 - m.x18)**2 + (m.x31 -
    m.x44)**2 + (m.x57 - m.x70)**2) + 1 / sqrt((m.x5 - m.x19)**2 + (m.x31 -
    m.x45)**2 + (m.x57 - m.x71)**2) + 1 / sqrt((m.x5 - m.x20)**2 + (m.x31 -
    m.x46)**2 + (m.x57 - m.x72)**2) + 1 / sqrt((m.x5 - m.x21)**2 + (m.x31 -
    m.x47)**2 + (m.x57 - m.x73)**2) + 1 / sqrt((m.x5 - m.x22)**2 + (m.x31 -
    m.x48)**2 + (m.x57 - m.x74)**2) + 1 / sqrt((m.x5 - m.x23)**2 + (m.x31 -
    m.x49)**2 + (m.x57 - m.x75)**2) + 1 / sqrt((m.x5 - m.x24)**2 + (m.x31 -
    m.x50)**2 + (m.x57 - m.x76)**2) + 1 / sqrt((m.x5 - m.x25)**2 + (m.x31 -
    m.x51)**2 + (m.x57 - m.x77)**2) + 1 / sqrt((m.x5 - m.x26)**2 + (m.x31 -
    m.x52)**2 + (m.x57 - m.x78)**2) + 1 / sqrt((m.x6 - m.x7)**2 + (m.x32 -
    m.x33)**2 + (m.x58 - m.x59)**2) + 1 / sqrt((m.x6 - m.x8)**2 + (m.x32 -
    m.x34)**2 + (m.x58 - m.x60)**2) + 1 / sqrt((m.x6 - m.x9)**2 + (m.x32 -
    m.x35)**2 + (m.x58 - m.x61)**2) + 1 / sqrt((m.x6 - m.x10)**2 + (m.x32 -
    m.x36)**2 + (m.x58 - m.x62)**2) + 1 / sqrt((m.x6 - m.x11)**2 + (m.x32 -
    m.x37)**2 + (m.x58 - m.x63)**2) + 1 / sqrt((m.x6 - m.x12)**2 + (m.x32 -
    m.x38)**2 + (m.x58 - m.x64)**2) + 1 / sqrt((m.x6 - m.x13)**2 + (m.x32 -
    m.x39)**2 + (m.x58 - m.x65)**2) + 1 / sqrt((m.x6 - m.x14)**2 + (m.x32 -
    m.x40)**2 + (m.x58 - m.x66)**2) + 1 / sqrt((m.x6 - m.x15)**2 + (m.x32 -
    m.x41)**2 + (m.x58 - m.x67)**2) + 1 / sqrt((m.x6 - m.x16)**2 + (m.x32 -
    m.x42)**2 + (m.x58 - m.x68)**2) + 1 / sqrt((m.x6 - m.x17)**2 + (m.x32 -
    m.x43)**2 + (m.x58 - m.x69)**2) + 1 / sqrt((m.x6 - m.x18)**2 + (m.x32 -
    m.x44)**2 + (m.x58 - m.x70)**2) + 1 / sqrt((m.x6 - m.x19)**2 + (m.x32 -
    m.x45)**2 + (m.x58 - m.x71)**2) + 1 / sqrt((m.x6 - m.x20)**2 + (m.x32 -
    m.x46)**2 + (m.x58 - m.x72)**2) + 1 / sqrt((m.x6 - m.x21)**2 + (m.x32 -
    m.x47)**2 + (m.x58 - m.x73)**2) + 1 / sqrt((m.x6 - m.x22)**2 + (m.x32 -
    m.x48)**2 + (m.x58 - m.x74)**2) + 1 / sqrt((m.x6 - m.x23)**2 + (m.x32 -
    m.x49)**2 + (m.x58 - m.x75)**2) + 1 / sqrt((m.x6 - m.x24)**2 + (m.x32 -
    m.x50)**2 + (m.x58 - m.x76)**2) + 1 / sqrt((m.x6 - m.x25)**2 + (m.x32 -
    m.x51)**2 + (m.x58 - m.x77)**2) + 1 / sqrt((m.x6 - m.x26)**2 + (m.x32 -
    m.x52)**2 + (m.x58 - m.x78)**2) + 1 / sqrt((m.x7 - m.x8)**2 + (m.x33 -
    m.x34)**2 + (m.x59 - m.x60)**2) + 1 / sqrt((m.x7 - m.x9)**2 + (m.x33 -
    m.x35)**2 + (m.x59 - m.x61)**2) + 1 / sqrt((m.x7 - m.x10)**2 + (m.x33 -
    m.x36)**2 + (m.x59 - m.x62)**2) + 1 / sqrt((m.x7 - m.x11)**2 + (m.x33 -
    m.x37)**2 + (m.x59 - m.x63)**2) + 1 / sqrt((m.x7 - m.x12)**2 + (m.x33 -
    m.x38)**2 + (m.x59 - m.x64)**2) + 1 / sqrt((m.x7 - m.x13)**2 + (m.x33 -
    m.x39)**2 + (m.x59 - m.x65)**2) + 1 / sqrt((m.x7 - m.x14)**2 + (m.x33 -
    m.x40)**2 + (m.x59 - m.x66)**2) + 1 / sqrt((m.x7 - m.x15)**2 + (m.x33 -
    m.x41)**2 + (m.x59 - m.x67)**2) + 1 / sqrt((m.x7 - m.x16)**2 + (m.x33 -
    m.x42)**2 + (m.x59 - m.x68)**2) + 1 / sqrt((m.x7 - m.x17)**2 + (m.x33 -
    m.x43)**2 + (m.x59 - m.x69)**2) + 1 / sqrt((m.x7 - m.x18)**2 + (m.x33 -
    m.x44)**2 + (m.x59 - m.x70)**2) + 1 / sqrt((m.x7 - m.x19)**2 + (m.x33 -
    m.x45)**2 + (m.x59 - m.x71)**2) + 1 / sqrt((m.x7 - m.x20)**2 + (m.x33 -
    m.x46)**2 + (m.x59 - m.x72)**2) + 1 / sqrt((m.x7 - m.x21)**2 + (m.x33 -
    m.x47)**2 + (m.x59 - m.x73)**2) + 1 / sqrt((m.x7 - m.x22)**2 + (m.x33 -
    m.x48)**2 + (m.x59 - m.x74)**2) + 1 / sqrt((m.x7 - m.x23)**2 + (m.x33 -
    m.x49)**2 + (m.x59 - m.x75)**2) + 1 / sqrt((m.x7 - m.x24)**2 + (m.x33 -
    m.x50)**2 + (m.x59 - m.x76)**2) + 1 / sqrt((m.x7 - m.x25)**2 + (m.x33 -
    m.x51)**2 + (m.x59 - m.x77)**2) + 1 / sqrt((m.x7 - m.x26)**2 + (m.x33 -
    m.x52)**2 + (m.x59 - m.x78)**2) + 1 / sqrt((m.x8 - m.x9)**2 + (m.x34 -
    m.x35)**2 + (m.x60 - m.x61)**2) + 1 / sqrt((m.x8 - m.x10)**2 + (m.x34 -
    m.x36)**2 + (m.x60 - m.x62)**2) + 1 / sqrt((m.x8 - m.x11)**2 + (m.x34 -
    m.x37)**2 + (m.x60 - m.x63)**2) + 1 / sqrt((m.x8 - m.x12)**2 + (m.x34 -
    m.x38)**2 + (m.x60 - m.x64)**2) + 1 / sqrt((m.x8 - m.x13)**2 + (m.x34 -
    m.x39)**2 + (m.x60 - m.x65)**2) + 1 / sqrt((m.x8 - m.x14)**2 + (m.x34 -
    m.x40)**2 + (m.x60 - m.x66)**2) + 1 / sqrt((m.x8 - m.x15)**2 + (m.x34 -
    m.x41)**2 + (m.x60 - m.x67)**2) + 1 / sqrt((m.x8 - m.x16)**2 + (m.x34 -
    m.x42)**2 + (m.x60 - m.x68)**2) + 1 / sqrt((m.x8 - m.x17)**2 + (m.x34 -
    m.x43)**2 + (m.x60 - m.x69)**2) + 1 / sqrt((m.x8 - m.x18)**2 + (m.x34 -
    m.x44)**2 + (m.x60 - m.x70)**2) + 1 / sqrt((m.x8 - m.x19)**2 + (m.x34 -
    m.x45)**2 + (m.x60 - m.x71)**2) + 1 / sqrt((m.x8 - m.x20)**2 + (m.x34 -
    m.x46)**2 + (m.x60 - m.x72)**2) + 1 / sqrt((m.x8 - m.x21)**2 + (m.x34 -
    m.x47)**2 + (m.x60 - m.x73)**2) + 1 / sqrt((m.x8 - m.x22)**2 + (m.x34 -
    m.x48)**2 + (m.x60 - m.x74)**2) + 1 / sqrt((m.x8 - m.x23)**2 + (m.x34 -
    m.x49)**2 + (m.x60 - m.x75)**2) + 1 / sqrt((m.x8 - m.x24)**2 + (m.x34 -
    m.x50)**2 + (m.x60 - m.x76)**2) + 1 / sqrt((m.x8 - m.x25)**2 + (m.x34 -
    m.x51)**2 + (m.x60 - m.x77)**2) + 1 / sqrt((m.x8 - m.x26)**2 + (m.x34 -
    m.x52)**2 + (m.x60 - m.x78)**2) + 1 / sqrt((m.x9 - m.x10)**2 + (m.x35 -
    m.x36)**2 + (m.x61 - m.x62)**2) + 1 / sqrt((m.x9 - m.x11)**2 + (m.x35 -
    m.x37)**2 + (m.x61 - m.x63)**2) + 1 / sqrt((m.x9 - m.x12)**2 + (m.x35 -
    m.x38)**2 + (m.x61 - m.x64)**2) + 1 / sqrt((m.x9 - m.x13)**2 + (m.x35 -
    m.x39)**2 + (m.x61 - m.x65)**2) + 1 / sqrt((m.x9 - m.x14)**2 + (m.x35 -
    m.x40)**2 + (m.x61 - m.x66)**2) + 1 / sqrt((m.x9 - m.x15)**2 + (m.x35 -
    m.x41)**2 + (m.x61 - m.x67)**2) + 1 / sqrt((m.x9 - m.x16)**2 + (m.x35 -
    m.x42)**2 + (m.x61 - m.x68)**2) + 1 / sqrt((m.x9 - m.x17)**2 + (m.x35 -
    m.x43)**2 + (m.x61 - m.x69)**2) + 1 / sqrt((m.x9 - m.x18)**2 + (m.x35 -
    m.x44)**2 + (m.x61 - m.x70)**2) + 1 / sqrt((m.x9 - m.x19)**2 + (m.x35 -
    m.x45)**2 + (m.x61 - m.x71)**2) + 1 / sqrt((m.x9 - m.x20)**2 + (m.x35 -
    m.x46)**2 + (m.x61 - m.x72)**2) + 1 / sqrt((m.x9 - m.x21)**2 + (m.x35 -
    m.x47)**2 + (m.x61 - m.x73)**2) + 1 / sqrt((m.x9 - m.x22)**2 + (m.x35 -
    m.x48)**2 + (m.x61 - m.x74)**2) + 1 / sqrt((m.x9 - m.x23)**2 + (m.x35 -
    m.x49)**2 + (m.x61 - m.x75)**2) + 1 / sqrt((m.x9 - m.x24)**2 + (m.x35 -
    m.x50)**2 + (m.x61 - m.x76)**2) + 1 / sqrt((m.x9 - m.x25)**2 + (m.x35 -
    m.x51)**2 + (m.x61 - m.x77)**2) + 1 / sqrt((m.x9 - m.x26)**2 + (m.x35 -
    m.x52)**2 + (m.x61 - m.x78)**2) + 1 / sqrt((m.x10 - m.x11)**2 + (m.x36 -
    m.x37)**2 + (m.x62 - m.x63)**2) + 1 / sqrt((m.x10 - m.x12)**2 + (m.x36 -
    m.x38)**2 + (m.x62 - m.x64)**2) + 1 / sqrt((m.x10 - m.x13)**2 + (m.x36 -
    m.x39)**2 + (m.x62 - m.x65)**2) + 1 / sqrt((m.x10 - m.x14)**2 + (m.x36 -
    m.x40)**2 + (m.x62 - m.x66)**2) + 1 / sqrt((m.x10 - m.x15)**2 + (m.x36 -
    m.x41)**2 + (m.x62 - m.x67)**2) + 1 / sqrt((m.x10 - m.x16)**2 + (m.x36 -
    m.x42)**2 + (m.x62 - m.x68)**2) + 1 / sqrt((m.x10 - m.x17)**2 + (m.x36 -
    m.x43)**2 + (m.x62 - m.x69)**2) + 1 / sqrt((m.x10 - m.x18)**2 + (m.x36 -
    m.x44)**2 + (m.x62 - m.x70)**2) + 1 / sqrt((m.x10 - m.x19)**2 + (m.x36 -
    m.x45)**2 + (m.x62 - m.x71)**2) + 1 / sqrt((m.x10 - m.x20)**2 + (m.x36 -
    m.x46)**2 + (m.x62 - m.x72)**2) + 1 / sqrt((m.x10 - m.x21)**2 + (m.x36 -
    m.x47)**2 + (m.x62 - m.x73)**2) + 1 / sqrt((m.x10 - m.x22)**2 + (m.x36 -
    m.x48)**2 + (m.x62 - m.x74)**2) + 1 / sqrt((m.x10 - m.x23)**2 + (m.x36 -
    m.x49)**2 + (m.x62 - m.x75)**2) + 1 / sqrt((m.x10 - m.x24)**2 + (m.x36 -
    m.x50)**2 + (m.x62 - m.x76)**2) + 1 / sqrt((m.x10 - m.x25)**2 + (m.x36 -
    m.x51)**2 + (m.x62 - m.x77)**2) + 1 / sqrt((m.x10 - m.x26)**2 + (m.x36 -
    m.x52)**2 + (m.x62 - m.x78)**2) + 1 / sqrt((m.x11 - m.x12)**2 + (m.x37 -
    m.x38)**2 + (m.x63 - m.x64)**2) + 1 / sqrt((m.x11 - m.x13)**2 + (m.x37 -
    m.x39)**2 + (m.x63 - m.x65)**2) + 1 / sqrt((m.x11 - m.x14)**2 + (m.x37 -
    m.x40)**2 + (m.x63 - m.x66)**2) + 1 / sqrt((m.x11 - m.x15)**2 + (m.x37 -
    m.x41)**2 + (m.x63 - m.x67)**2) + 1 / sqrt((m.x11 - m.x16)**2 + (m.x37 -
    m.x42)**2 + (m.x63 - m.x68)**2) + 1 / sqrt((m.x11 - m.x17)**2 + (m.x37 -
    m.x43)**2 + (m.x63 - m.x69)**2) + 1 / sqrt((m.x11 - m.x18)**2 + (m.x37 -
    m.x44)**2 + (m.x63 - m.x70)**2) + 1 / sqrt((m.x11 - m.x19)**2 + (m.x37 -
    m.x45)**2 + (m.x63 - m.x71)**2) + 1 / sqrt((m.x11 - m.x20)**2 + (m.x37 -
    m.x46)**2 + (m.x63 - m.x72)**2) + 1 / sqrt((m.x11 - m.x21)**2 + (m.x37 -
    m.x47)**2 + (m.x63 - m.x73)**2) + 1 / sqrt((m.x11 - m.x22)**2 + (m.x37 -
    m.x48)**2 + (m.x63 - m.x74)**2) + 1 / sqrt((m.x11 - m.x23)**2 + (m.x37 -
    m.x49)**2 + (m.x63 - m.x75)**2) + 1 / sqrt((m.x11 - m.x24)**2 + (m.x37 -
    m.x50)**2 + (m.x63 - m.x76)**2) + 1 / sqrt((m.x11 - m.x25)**2 + (m.x37 -
    m.x51)**2 + (m.x63 - m.x77)**2) + 1 / sqrt((m.x11 - m.x26)**2 + (m.x37 -
    m.x52)**2 + (m.x63 - m.x78)**2) + 1 / sqrt((m.x12 - m.x13)**2 + (m.x38 -
    m.x39)**2 + (m.x64 - m.x65)**2) + 1 / sqrt((m.x12 - m.x14)**2 + (m.x38 -
    m.x40)**2 + (m.x64 - m.x66)**2) + 1 / sqrt((m.x12 - m.x15)**2 + (m.x38 -
    m.x41)**2 + (m.x64 - m.x67)**2) + 1 / sqrt((m.x12 - m.x16)**2 + (m.x38 -
    m.x42)**2 + (m.x64 - m.x68)**2) + 1 / sqrt((m.x12 - m.x17)**2 + (m.x38 -
    m.x43)**2 + (m.x64 - m.x69)**2) + 1 / sqrt((m.x12 - m.x18)**2 + (m.x38 -
    m.x44)**2 + (m.x64 - m.x70)**2) + 1 / sqrt((m.x12 - m.x19)**2 + (m.x38 -
    m.x45)**2 + (m.x64 - m.x71)**2) + 1 / sqrt((m.x12 - m.x20)**2 + (m.x38 -
    m.x46)**2 + (m.x64 - m.x72)**2) + 1 / sqrt((m.x12 - m.x21)**2 + (m.x38 -
    m.x47)**2 + (m.x64 - m.x73)**2) + 1 / sqrt((m.x12 - m.x22)**2 + (m.x38 -
    m.x48)**2 + (m.x64 - m.x74)**2) + 1 / sqrt((m.x12 - m.x23)**2 + (m.x38 -
    m.x49)**2 + (m.x64 - m.x75)**2) + 1 / sqrt((m.x12 - m.x24)**2 + (m.x38 -
    m.x50)**2 + (m.x64 - m.x76)**2) + 1 / sqrt((m.x12 - m.x25)**2 + (m.x38 -
    m.x51)**2 + (m.x64 - m.x77)**2) + 1 / sqrt((m.x12 - m.x26)**2 + (m.x38 -
    m.x52)**2 + (m.x64 - m.x78)**2) + 1 / sqrt((m.x13 - m.x14)**2 + (m.x39 -
    m.x40)**2 + (m.x65 - m.x66)**2) + 1 / sqrt((m.x13 - m.x15)**2 + (m.x39 -
    m.x41)**2 + (m.x65 - m.x67)**2) + 1 / sqrt((m.x13 - m.x16)**2 + (m.x39 -
    m.x42)**2 + (m.x65 - m.x68)**2) + 1 / sqrt((m.x13 - m.x17)**2 + (m.x39 -
    m.x43)**2 + (m.x65 - m.x69)**2) + 1 / sqrt((m.x13 - m.x18)**2 + (m.x39 -
    m.x44)**2 + (m.x65 - m.x70)**2) + 1 / sqrt((m.x13 - m.x19)**2 + (m.x39 -
    m.x45)**2 + (m.x65 - m.x71)**2) + 1 / sqrt((m.x13 - m.x20)**2 + (m.x39 -
    m.x46)**2 + (m.x65 - m.x72)**2) + 1 / sqrt((m.x13 - m.x21)**2 + (m.x39 -
    m.x47)**2 + (m.x65 - m.x73)**2) + 1 / sqrt((m.x13 - m.x22)**2 + (m.x39 -
    m.x48)**2 + (m.x65 - m.x74)**2) + 1 / sqrt((m.x13 - m.x23)**2 + (m.x39 -
    m.x49)**2 + (m.x65 - m.x75)**2) + 1 / sqrt((m.x13 - m.x24)**2 + (m.x39 -
    m.x50)**2 + (m.x65 - m.x76)**2) + 1 / sqrt((m.x13 - m.x25)**2 + (m.x39 -
    m.x51)**2 + (m.x65 - m.x77)**2) + 1 / sqrt((m.x13 - m.x26)**2 + (m.x39 -
    m.x52)**2 + (m.x65 - m.x78)**2) + 1 / sqrt((m.x14 - m.x15)**2 + (m.x40 -
    m.x41)**2 + (m.x66 - m.x67)**2) + 1 / sqrt((m.x14 - m.x16)**2 + (m.x40 -
    m.x42)**2 + (m.x66 - m.x68)**2) + 1 / sqrt((m.x14 - m.x17)**2 + (m.x40 -
    m.x43)**2 + (m.x66 - m.x69)**2) + 1 / sqrt((m.x14 - m.x18)**2 + (m.x40 -
    m.x44)**2 + (m.x66 - m.x70)**2) + 1 / sqrt((m.x14 - m.x19)**2 + (m.x40 -
    m.x45)**2 + (m.x66 - m.x71)**2) + 1 / sqrt((m.x14 - m.x20)**2 + (m.x40 -
    m.x46)**2 + (m.x66 - m.x72)**2) + 1 / sqrt((m.x14 - m.x21)**2 + (m.x40 -
    m.x47)**2 + (m.x66 - m.x73)**2) + 1 / sqrt((m.x14 - m.x22)**2 + (m.x40 -
    m.x48)**2 + (m.x66 - m.x74)**2) + 1 / sqrt((m.x14 - m.x23)**2 + (m.x40 -
    m.x49)**2 + (m.x66 - m.x75)**2) + 1 / sqrt((m.x14 - m.x24)**2 + (m.x40 -
    m.x50)**2 + (m.x66 - m.x76)**2) + 1 / sqrt((m.x14 - m.x25)**2 + (m.x40 -
    m.x51)**2 + (m.x66 - m.x77)**2) + 1 / sqrt((m.x14 - m.x26)**2 + (m.x40 -
    m.x52)**2 + (m.x66 - m.x78)**2) + 1 / sqrt((m.x15 - m.x16)**2 + (m.x41 -
    m.x42)**2 + (m.x67 - m.x68)**2) + 1 / sqrt((m.x15 - m.x17)**2 + (m.x41 -
    m.x43)**2 + (m.x67 - m.x69)**2) + 1 / sqrt((m.x15 - m.x18)**2 + (m.x41 -
    m.x44)**2 + (m.x67 - m.x70)**2) + 1 / sqrt((m.x15 - m.x19)**2 + (m.x41 -
    m.x45)**2 + (m.x67 - m.x71)**2) + 1 / sqrt((m.x15 - m.x20)**2 + (m.x41 -
    m.x46)**2 + (m.x67 - m.x72)**2) + 1 / sqrt((m.x15 - m.x21)**2 + (m.x41 -
    m.x47)**2 + (m.x67 - m.x73)**2) + 1 / sqrt((m.x15 - m.x22)**2 + (m.x41 -
    m.x48)**2 + (m.x67 - m.x74)**2) + 1 / sqrt((m.x15 - m.x23)**2 + (m.x41 -
    m.x49)**2 + (m.x67 - m.x75)**2) + 1 / sqrt((m.x15 - m.x24)**2 + (m.x41 -
    m.x50)**2 + (m.x67 - m.x76)**2) + 1 / sqrt((m.x15 - m.x25)**2 + (m.x41 -
    m.x51)**2 + (m.x67 - m.x77)**2) + 1 / sqrt((m.x15 - m.x26)**2 + (m.x41 -
    m.x52)**2 + (m.x67 - m.x78)**2) + 1 / sqrt((m.x16 - m.x17)**2 + (m.x42 -
    m.x43)**2 + (m.x68 - m.x69)**2) + 1 / sqrt((m.x16 - m.x18)**2 + (m.x42 -
    m.x44)**2 + (m.x68 - m.x70)**2) + 1 / sqrt((m.x16 - m.x19)**2 + (m.x42 -
    m.x45)**2 + (m.x68 - m.x71)**2) + 1 / sqrt((m.x16 - m.x20)**2 + (m.x42 -
    m.x46)**2 + (m.x68 - m.x72)**2) + 1 / sqrt((m.x16 - m.x21)**2 + (m.x42 -
    m.x47)**2 + (m.x68 - m.x73)**2) + 1 / sqrt((m.x16 - m.x22)**2 + (m.x42 -
    m.x48)**2 + (m.x68 - m.x74)**2) + 1 / sqrt((m.x16 - m.x23)**2 + (m.x42 -
    m.x49)**2 + (m.x68 - m.x75)**2) + 1 / sqrt((m.x16 - m.x24)**2 + (m.x42 -
    m.x50)**2 + (m.x68 - m.x76)**2) + 1 / sqrt((m.x16 - m.x25)**2 + (m.x42 -
    m.x51)**2 + (m.x68 - m.x77)**2) + 1 / sqrt((m.x16 - m.x26)**2 + (m.x42 -
    m.x52)**2 + (m.x68 - m.x78)**2) + 1 / sqrt((m.x17 - m.x18)**2 + (m.x43 -
    m.x44)**2 + (m.x69 - m.x70)**2) + 1 / sqrt((m.x17 - m.x19)**2 + (m.x43 -
    m.x45)**2 + (m.x69 - m.x71)**2) + 1 / sqrt((m.x17 - m.x20)**2 + (m.x43 -
    m.x46)**2 + (m.x69 - m.x72)**2) + 1 / sqrt((m.x17 - m.x21)**2 + (m.x43 -
    m.x47)**2 + (m.x69 - m.x73)**2) + 1 / sqrt((m.x17 - m.x22)**2 + (m.x43 -
    m.x48)**2 + (m.x69 - m.x74)**2) + 1 / sqrt((m.x17 - m.x23)**2 + (m.x43 -
    m.x49)**2 + (m.x69 - m.x75)**2) + 1 / sqrt((m.x17 - m.x24)**2 + (m.x43 -
    m.x50)**2 + (m.x69 - m.x76)**2) + 1 / sqrt((m.x17 - m.x25)**2 + (m.x43 -
    m.x51)**2 + (m.x69 - m.x77)**2) + 1 / sqrt((m.x17 - m.x26)**2 + (m.x43 -
    m.x52)**2 + (m.x69 - m.x78)**2) + 1 / sqrt((m.x18 - m.x19)**2 + (m.x44 -
    m.x45)**2 + (m.x70 - m.x71)**2) + 1 / sqrt((m.x18 - m.x20)**2 + (m.x44 -
    m.x46)**2 + (m.x70 - m.x72)**2) + 1 / sqrt((m.x18 - m.x21)**2 + (m.x44 -
    m.x47)**2 + (m.x70 - m.x73)**2) + 1 / sqrt((m.x18 - m.x22)**2 + (m.x44 -
    m.x48)**2 + (m.x70 - m.x74)**2) + 1 / sqrt((m.x18 - m.x23)**2 + (m.x44 -
    m.x49)**2 + (m.x70 - m.x75)**2) + 1 / sqrt((m.x18 - m.x24)**2 + (m.x44 -
    m.x50)**2 + (m.x70 - m.x76)**2) + 1 / sqrt((m.x18 - m.x25)**2 + (m.x44 -
    m.x51)**2 + (m.x70 - m.x77)**2) + 1 / sqrt((m.x18 - m.x26)**2 + (m.x44 -
    m.x52)**2 + (m.x70 - m.x78)**2) + 1 / sqrt((m.x19 - m.x20)**2 + (m.x45 -
    m.x46)**2 + (m.x71 - m.x72)**2) + 1 / sqrt((m.x19 - m.x21)**2 + (m.x45 -
    m.x47)**2 + (m.x71 - m.x73)**2) + 1 / sqrt((m.x19 - m.x22)**2 + (m.x45 -
    m.x48)**2 + (m.x71 - m.x74)**2) + 1 / sqrt((m.x19 - m.x23)**2 + (m.x45 -
    m.x49)**2 + (m.x71 - m.x75)**2) + 1 / sqrt((m.x19 - m.x24)**2 + (m.x45 -
    m.x50)**2 + (m.x71 - m.x76)**2) + 1 / sqrt((m.x19 - m.x25)**2 + (m.x45 -
    m.x51)**2 + (m.x71 - m.x77)**2) + 1 / sqrt((m.x19 - m.x26)**2 + (m.x45 -
    m.x52)**2 + (m.x71 - m.x78)**2) + 1 / sqrt((m.x20 - m.x21)**2 + (m.x46 -
    m.x47)**2 + (m.x72 - m.x73)**2) + 1 / sqrt((m.x20 - m.x22)**2 + (m.x46 -
    m.x48)**2 + (m.x72 - m.x74)**2) + 1 / sqrt((m.x20 - m.x23)**2 + (m.x46 -
    m.x49)**2 + (m.x72 - m.x75)**2) + 1 / sqrt((m.x20 - m.x24)**2 + (m.x46 -
    m.x50)**2 + (m.x72 - m.x76)**2) + 1 / sqrt((m.x20 - m.x25)**2 + (m.x46 -
    m.x51)**2 + (m.x72 - m.x77)**2) + 1 / sqrt((m.x20 - m.x26)**2 + (m.x46 -
    m.x52)**2 + (m.x72 - m.x78)**2) + 1 / sqrt((m.x21 - m.x22)**2 + (m.x47 -
    m.x48)**2 + (m.x73 - m.x74)**2) + 1 / sqrt((m.x21 - m.x23)**2 + (m.x47 -
    m.x49)**2 + (m.x73 - m.x75)**2) + 1 / sqrt((m.x21 - m.x24)**2 + (m.x47 -
    m.x50)**2 + (m.x73 - m.x76)**2) + 1 / sqrt((m.x21 - m.x25)**2 + (m.x47 -
    m.x51)**2 + (m.x73 - m.x77)**2) + 1 / sqrt((m.x21 - m.x26)**2 + (m.x47 -
    m.x52)**2 + (m.x73 - m.x78)**2) + 1 / sqrt((m.x22 - m.x23)**2 + (m.x48 -
    m.x49)**2 + (m.x74 - m.x75)**2) + 1 / sqrt((m.x22 - m.x24)**2 + (m.x48 -
    m.x50)**2 + (m.x74 - m.x76)**2) + 1 / sqrt((m.x22 - m.x25)**2 + (m.x48 -
    m.x51)**2 + (m.x74 - m.x77)**2) + 1 / sqrt((m.x22 - m.x26)**2 + (m.x48 -
    m.x52)**2 + (m.x74 - m.x78)**2) + 1 / sqrt((m.x23 - m.x24)**2 + (m.x49 -
    m.x50)**2 + (m.x75 - m.x76)**2) + 1 / sqrt((m.x23 - m.x25)**2 + (m.x49 -
    m.x51)**2 + (m.x75 - m.x77)**2) + 1 / sqrt((m.x23 - m.x26)**2 + (m.x49 -
    m.x52)**2 + (m.x75 - m.x78)**2) + 1 / sqrt((m.x24 - m.x25)**2 + (m.x50 -
    m.x51)**2 + (m.x76 - m.x77)**2) + 1 / sqrt((m.x24 - m.x26)**2 + (m.x50 -
    m.x52)**2 + (m.x76 - m.x78)**2) + 1 / sqrt((m.x25 - m.x26)**2 + (m.x51 -
    m.x52)**2 + (m.x77 - m.x78)**2))

m.e1 = Constraint(expr= m.x1**2 + m.x27**2 + m.x53**2 == 1)
m.e2 = Constraint(expr= m.x2**2 + m.x28**2 + m.x54**2 == 1)
m.e3 = Constraint(expr= m.x3**2 + m.x29**2 + m.x55**2 == 1)
m.e4 = Constraint(expr= m.x4**2 + m.x30**2 + m.x56**2 == 1)
m.e5 = Constraint(expr= m.x5**2 + m.x31**2 + m.x57**2 == 1)
m.e6 = Constraint(expr= m.x6**2 + m.x32**2 + m.x58**2 == 1)
m.e7 = Constraint(expr= m.x7**2 + m.x33**2 + m.x59**2 == 1)
m.e8 = Constraint(expr= m.x8**2 + m.x34**2 + m.x60**2 == 1)
m.e9 = Constraint(expr= m.x9**2 + m.x35**2 + m.x61**2 == 1)
m.e10 = Constraint(expr= m.x10**2 + m.x36**2 + m.x62**2 == 1)
m.e11 = Constraint(expr= m.x11**2 + m.x37**2 + m.x63**2 == 1)
m.e12 = Constraint(expr= m.x12**2 + m.x38**2 + m.x64**2 == 1)
m.e13 = Constraint(expr= m.x13**2 + m.x39**2 + m.x65**2 == 1)
m.e14 = Constraint(expr= m.x14**2 + m.x40**2 + m.x66**2 == 1)
m.e15 = Constraint(expr= m.x15**2 + m.x41**2 + m.x67**2 == 1)
m.e16 = Constraint(expr= m.x16**2 + m.x42**2 + m.x68**2 == 1)
m.e17 = Constraint(expr= m.x17**2 + m.x43**2 + m.x69**2 == 1)
m.e18 = Constraint(expr= m.x18**2 + m.x44**2 + m.x70**2 == 1)
m.e19 = Constraint(expr= m.x19**2 + m.x45**2 + m.x71**2 == 1)
m.e20 = Constraint(expr= m.x20**2 + m.x46**2 + m.x72**2 == 1)
m.e21 = Constraint(expr= m.x21**2 + m.x47**2 + m.x73**2 == 1)
m.e22 = Constraint(expr= m.x22**2 + m.x48**2 + m.x74**2 == 1)
m.e23 = Constraint(expr= m.x23**2 + m.x49**2 + m.x75**2 == 1)
m.e24 = Constraint(expr= m.x24**2 + m.x50**2 + m.x76**2 == 1)
m.e25 = Constraint(expr= m.x25**2 + m.x51**2 + m.x77**2 == 1)
m.e26 = Constraint(expr= m.x26**2 + m.x52**2 + m.x78**2 == 1)
