# NLP written by GAMS Convert at 05/15/24 11:42:39
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#        42       42        0        0        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#       126      126        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       126        0      126
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
m.x82 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x83 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x84 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x85 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x86 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x87 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x88 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x89 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x90 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x91 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x92 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x93 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x94 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x95 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x96 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x97 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x98 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x99 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x100 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x101 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x102 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x103 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x104 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x105 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x106 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x107 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x108 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x109 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x110 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x111 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x112 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x113 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x114 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x115 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x116 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x117 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x118 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x119 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x120 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x121 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x122 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x123 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x124 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x125 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x126 = Var(within=Reals, bounds=(-1,1), initialize=0)

m.obj = Objective(sense=minimize, expr= 1 / sqrt((m.x1 - m.x2)**2 + (m.x43 -
    m.x44)**2 + (m.x85 - m.x86)**2) + 1 / sqrt((m.x1 - m.x3)**2 + (m.x43 -
    m.x45)**2 + (m.x85 - m.x87)**2) + 1 / sqrt((m.x1 - m.x4)**2 + (m.x43 -
    m.x46)**2 + (m.x85 - m.x88)**2) + 1 / sqrt((m.x1 - m.x5)**2 + (m.x43 -
    m.x47)**2 + (m.x85 - m.x89)**2) + 1 / sqrt((m.x1 - m.x6)**2 + (m.x43 -
    m.x48)**2 + (m.x85 - m.x90)**2) + 1 / sqrt((m.x1 - m.x7)**2 + (m.x43 -
    m.x49)**2 + (m.x85 - m.x91)**2) + 1 / sqrt((m.x1 - m.x8)**2 + (m.x43 -
    m.x50)**2 + (m.x85 - m.x92)**2) + 1 / sqrt((m.x1 - m.x9)**2 + (m.x43 -
    m.x51)**2 + (m.x85 - m.x93)**2) + 1 / sqrt((m.x1 - m.x10)**2 + (m.x43 -
    m.x52)**2 + (m.x85 - m.x94)**2) + 1 / sqrt((m.x1 - m.x11)**2 + (m.x43 -
    m.x53)**2 + (m.x85 - m.x95)**2) + 1 / sqrt((m.x1 - m.x12)**2 + (m.x43 -
    m.x54)**2 + (m.x85 - m.x96)**2) + 1 / sqrt((m.x1 - m.x13)**2 + (m.x43 -
    m.x55)**2 + (m.x85 - m.x97)**2) + 1 / sqrt((m.x1 - m.x14)**2 + (m.x43 -
    m.x56)**2 + (m.x85 - m.x98)**2) + 1 / sqrt((m.x1 - m.x15)**2 + (m.x43 -
    m.x57)**2 + (m.x85 - m.x99)**2) + 1 / sqrt((m.x1 - m.x16)**2 + (m.x43 -
    m.x58)**2 + (m.x85 - m.x100)**2) + 1 / sqrt((m.x1 - m.x17)**2 + (m.x43 -
    m.x59)**2 + (m.x85 - m.x101)**2) + 1 / sqrt((m.x1 - m.x18)**2 + (m.x43 -
    m.x60)**2 + (m.x85 - m.x102)**2) + 1 / sqrt((m.x1 - m.x19)**2 + (m.x43 -
    m.x61)**2 + (m.x85 - m.x103)**2) + 1 / sqrt((m.x1 - m.x20)**2 + (m.x43 -
    m.x62)**2 + (m.x85 - m.x104)**2) + 1 / sqrt((m.x1 - m.x21)**2 + (m.x43 -
    m.x63)**2 + (m.x85 - m.x105)**2) + 1 / sqrt((m.x1 - m.x22)**2 + (m.x43 -
    m.x64)**2 + (m.x85 - m.x106)**2) + 1 / sqrt((m.x1 - m.x23)**2 + (m.x43 -
    m.x65)**2 + (m.x85 - m.x107)**2) + 1 / sqrt((m.x1 - m.x24)**2 + (m.x43 -
    m.x66)**2 + (m.x85 - m.x108)**2) + 1 / sqrt((m.x1 - m.x25)**2 + (m.x43 -
    m.x67)**2 + (m.x85 - m.x109)**2) + 1 / sqrt((m.x1 - m.x26)**2 + (m.x43 -
    m.x68)**2 + (m.x85 - m.x110)**2) + 1 / sqrt((m.x1 - m.x27)**2 + (m.x43 -
    m.x69)**2 + (m.x85 - m.x111)**2) + 1 / sqrt((m.x1 - m.x28)**2 + (m.x43 -
    m.x70)**2 + (m.x85 - m.x112)**2) + 1 / sqrt((m.x1 - m.x29)**2 + (m.x43 -
    m.x71)**2 + (m.x85 - m.x113)**2) + 1 / sqrt((m.x1 - m.x30)**2 + (m.x43 -
    m.x72)**2 + (m.x85 - m.x114)**2) + 1 / sqrt((m.x1 - m.x31)**2 + (m.x43 -
    m.x73)**2 + (m.x85 - m.x115)**2) + 1 / sqrt((m.x1 - m.x32)**2 + (m.x43 -
    m.x74)**2 + (m.x85 - m.x116)**2) + 1 / sqrt((m.x1 - m.x33)**2 + (m.x43 -
    m.x75)**2 + (m.x85 - m.x117)**2) + 1 / sqrt((m.x1 - m.x34)**2 + (m.x43 -
    m.x76)**2 + (m.x85 - m.x118)**2) + 1 / sqrt((m.x1 - m.x35)**2 + (m.x43 -
    m.x77)**2 + (m.x85 - m.x119)**2) + 1 / sqrt((m.x1 - m.x36)**2 + (m.x43 -
    m.x78)**2 + (m.x85 - m.x120)**2) + 1 / sqrt((m.x1 - m.x37)**2 + (m.x43 -
    m.x79)**2 + (m.x85 - m.x121)**2) + 1 / sqrt((m.x1 - m.x38)**2 + (m.x43 -
    m.x80)**2 + (m.x85 - m.x122)**2) + 1 / sqrt((m.x1 - m.x39)**2 + (m.x43 -
    m.x81)**2 + (m.x85 - m.x123)**2) + 1 / sqrt((m.x1 - m.x40)**2 + (m.x43 -
    m.x82)**2 + (m.x85 - m.x124)**2) + 1 / sqrt((m.x1 - m.x41)**2 + (m.x43 -
    m.x83)**2 + (m.x85 - m.x125)**2) + 1 / sqrt((m.x1 - m.x42)**2 + (m.x43 -
    m.x84)**2 + (m.x85 - m.x126)**2) + 1 / sqrt((m.x2 - m.x3)**2 + (m.x44 -
    m.x45)**2 + (m.x86 - m.x87)**2) + 1 / sqrt((m.x2 - m.x4)**2 + (m.x44 -
    m.x46)**2 + (m.x86 - m.x88)**2) + 1 / sqrt((m.x2 - m.x5)**2 + (m.x44 -
    m.x47)**2 + (m.x86 - m.x89)**2) + 1 / sqrt((m.x2 - m.x6)**2 + (m.x44 -
    m.x48)**2 + (m.x86 - m.x90)**2) + 1 / sqrt((m.x2 - m.x7)**2 + (m.x44 -
    m.x49)**2 + (m.x86 - m.x91)**2) + 1 / sqrt((m.x2 - m.x8)**2 + (m.x44 -
    m.x50)**2 + (m.x86 - m.x92)**2) + 1 / sqrt((m.x2 - m.x9)**2 + (m.x44 -
    m.x51)**2 + (m.x86 - m.x93)**2) + 1 / sqrt((m.x2 - m.x10)**2 + (m.x44 -
    m.x52)**2 + (m.x86 - m.x94)**2) + 1 / sqrt((m.x2 - m.x11)**2 + (m.x44 -
    m.x53)**2 + (m.x86 - m.x95)**2) + 1 / sqrt((m.x2 - m.x12)**2 + (m.x44 -
    m.x54)**2 + (m.x86 - m.x96)**2) + 1 / sqrt((m.x2 - m.x13)**2 + (m.x44 -
    m.x55)**2 + (m.x86 - m.x97)**2) + 1 / sqrt((m.x2 - m.x14)**2 + (m.x44 -
    m.x56)**2 + (m.x86 - m.x98)**2) + 1 / sqrt((m.x2 - m.x15)**2 + (m.x44 -
    m.x57)**2 + (m.x86 - m.x99)**2) + 1 / sqrt((m.x2 - m.x16)**2 + (m.x44 -
    m.x58)**2 + (m.x86 - m.x100)**2) + 1 / sqrt((m.x2 - m.x17)**2 + (m.x44 -
    m.x59)**2 + (m.x86 - m.x101)**2) + 1 / sqrt((m.x2 - m.x18)**2 + (m.x44 -
    m.x60)**2 + (m.x86 - m.x102)**2) + 1 / sqrt((m.x2 - m.x19)**2 + (m.x44 -
    m.x61)**2 + (m.x86 - m.x103)**2) + 1 / sqrt((m.x2 - m.x20)**2 + (m.x44 -
    m.x62)**2 + (m.x86 - m.x104)**2) + 1 / sqrt((m.x2 - m.x21)**2 + (m.x44 -
    m.x63)**2 + (m.x86 - m.x105)**2) + 1 / sqrt((m.x2 - m.x22)**2 + (m.x44 -
    m.x64)**2 + (m.x86 - m.x106)**2) + 1 / sqrt((m.x2 - m.x23)**2 + (m.x44 -
    m.x65)**2 + (m.x86 - m.x107)**2) + 1 / sqrt((m.x2 - m.x24)**2 + (m.x44 -
    m.x66)**2 + (m.x86 - m.x108)**2) + 1 / sqrt((m.x2 - m.x25)**2 + (m.x44 -
    m.x67)**2 + (m.x86 - m.x109)**2) + 1 / sqrt((m.x2 - m.x26)**2 + (m.x44 -
    m.x68)**2 + (m.x86 - m.x110)**2) + 1 / sqrt((m.x2 - m.x27)**2 + (m.x44 -
    m.x69)**2 + (m.x86 - m.x111)**2) + 1 / sqrt((m.x2 - m.x28)**2 + (m.x44 -
    m.x70)**2 + (m.x86 - m.x112)**2) + 1 / sqrt((m.x2 - m.x29)**2 + (m.x44 -
    m.x71)**2 + (m.x86 - m.x113)**2) + 1 / sqrt((m.x2 - m.x30)**2 + (m.x44 -
    m.x72)**2 + (m.x86 - m.x114)**2) + 1 / sqrt((m.x2 - m.x31)**2 + (m.x44 -
    m.x73)**2 + (m.x86 - m.x115)**2) + 1 / sqrt((m.x2 - m.x32)**2 + (m.x44 -
    m.x74)**2 + (m.x86 - m.x116)**2) + 1 / sqrt((m.x2 - m.x33)**2 + (m.x44 -
    m.x75)**2 + (m.x86 - m.x117)**2) + 1 / sqrt((m.x2 - m.x34)**2 + (m.x44 -
    m.x76)**2 + (m.x86 - m.x118)**2) + 1 / sqrt((m.x2 - m.x35)**2 + (m.x44 -
    m.x77)**2 + (m.x86 - m.x119)**2) + 1 / sqrt((m.x2 - m.x36)**2 + (m.x44 -
    m.x78)**2 + (m.x86 - m.x120)**2) + 1 / sqrt((m.x2 - m.x37)**2 + (m.x44 -
    m.x79)**2 + (m.x86 - m.x121)**2) + 1 / sqrt((m.x2 - m.x38)**2 + (m.x44 -
    m.x80)**2 + (m.x86 - m.x122)**2) + 1 / sqrt((m.x2 - m.x39)**2 + (m.x44 -
    m.x81)**2 + (m.x86 - m.x123)**2) + 1 / sqrt((m.x2 - m.x40)**2 + (m.x44 -
    m.x82)**2 + (m.x86 - m.x124)**2) + 1 / sqrt((m.x2 - m.x41)**2 + (m.x44 -
    m.x83)**2 + (m.x86 - m.x125)**2) + 1 / sqrt((m.x2 - m.x42)**2 + (m.x44 -
    m.x84)**2 + (m.x86 - m.x126)**2) + 1 / sqrt((m.x3 - m.x4)**2 + (m.x45 -
    m.x46)**2 + (m.x87 - m.x88)**2) + 1 / sqrt((m.x3 - m.x5)**2 + (m.x45 -
    m.x47)**2 + (m.x87 - m.x89)**2) + 1 / sqrt((m.x3 - m.x6)**2 + (m.x45 -
    m.x48)**2 + (m.x87 - m.x90)**2) + 1 / sqrt((m.x3 - m.x7)**2 + (m.x45 -
    m.x49)**2 + (m.x87 - m.x91)**2) + 1 / sqrt((m.x3 - m.x8)**2 + (m.x45 -
    m.x50)**2 + (m.x87 - m.x92)**2) + 1 / sqrt((m.x3 - m.x9)**2 + (m.x45 -
    m.x51)**2 + (m.x87 - m.x93)**2) + 1 / sqrt((m.x3 - m.x10)**2 + (m.x45 -
    m.x52)**2 + (m.x87 - m.x94)**2) + 1 / sqrt((m.x3 - m.x11)**2 + (m.x45 -
    m.x53)**2 + (m.x87 - m.x95)**2) + 1 / sqrt((m.x3 - m.x12)**2 + (m.x45 -
    m.x54)**2 + (m.x87 - m.x96)**2) + 1 / sqrt((m.x3 - m.x13)**2 + (m.x45 -
    m.x55)**2 + (m.x87 - m.x97)**2) + 1 / sqrt((m.x3 - m.x14)**2 + (m.x45 -
    m.x56)**2 + (m.x87 - m.x98)**2) + 1 / sqrt((m.x3 - m.x15)**2 + (m.x45 -
    m.x57)**2 + (m.x87 - m.x99)**2) + 1 / sqrt((m.x3 - m.x16)**2 + (m.x45 -
    m.x58)**2 + (m.x87 - m.x100)**2) + 1 / sqrt((m.x3 - m.x17)**2 + (m.x45 -
    m.x59)**2 + (m.x87 - m.x101)**2) + 1 / sqrt((m.x3 - m.x18)**2 + (m.x45 -
    m.x60)**2 + (m.x87 - m.x102)**2) + 1 / sqrt((m.x3 - m.x19)**2 + (m.x45 -
    m.x61)**2 + (m.x87 - m.x103)**2) + 1 / sqrt((m.x3 - m.x20)**2 + (m.x45 -
    m.x62)**2 + (m.x87 - m.x104)**2) + 1 / sqrt((m.x3 - m.x21)**2 + (m.x45 -
    m.x63)**2 + (m.x87 - m.x105)**2) + 1 / sqrt((m.x3 - m.x22)**2 + (m.x45 -
    m.x64)**2 + (m.x87 - m.x106)**2) + 1 / sqrt((m.x3 - m.x23)**2 + (m.x45 -
    m.x65)**2 + (m.x87 - m.x107)**2) + 1 / sqrt((m.x3 - m.x24)**2 + (m.x45 -
    m.x66)**2 + (m.x87 - m.x108)**2) + 1 / sqrt((m.x3 - m.x25)**2 + (m.x45 -
    m.x67)**2 + (m.x87 - m.x109)**2) + 1 / sqrt((m.x3 - m.x26)**2 + (m.x45 -
    m.x68)**2 + (m.x87 - m.x110)**2) + 1 / sqrt((m.x3 - m.x27)**2 + (m.x45 -
    m.x69)**2 + (m.x87 - m.x111)**2) + 1 / sqrt((m.x3 - m.x28)**2 + (m.x45 -
    m.x70)**2 + (m.x87 - m.x112)**2) + 1 / sqrt((m.x3 - m.x29)**2 + (m.x45 -
    m.x71)**2 + (m.x87 - m.x113)**2) + 1 / sqrt((m.x3 - m.x30)**2 + (m.x45 -
    m.x72)**2 + (m.x87 - m.x114)**2) + 1 / sqrt((m.x3 - m.x31)**2 + (m.x45 -
    m.x73)**2 + (m.x87 - m.x115)**2) + 1 / sqrt((m.x3 - m.x32)**2 + (m.x45 -
    m.x74)**2 + (m.x87 - m.x116)**2) + 1 / sqrt((m.x3 - m.x33)**2 + (m.x45 -
    m.x75)**2 + (m.x87 - m.x117)**2) + 1 / sqrt((m.x3 - m.x34)**2 + (m.x45 -
    m.x76)**2 + (m.x87 - m.x118)**2) + 1 / sqrt((m.x3 - m.x35)**2 + (m.x45 -
    m.x77)**2 + (m.x87 - m.x119)**2) + 1 / sqrt((m.x3 - m.x36)**2 + (m.x45 -
    m.x78)**2 + (m.x87 - m.x120)**2) + 1 / sqrt((m.x3 - m.x37)**2 + (m.x45 -
    m.x79)**2 + (m.x87 - m.x121)**2) + 1 / sqrt((m.x3 - m.x38)**2 + (m.x45 -
    m.x80)**2 + (m.x87 - m.x122)**2) + 1 / sqrt((m.x3 - m.x39)**2 + (m.x45 -
    m.x81)**2 + (m.x87 - m.x123)**2) + 1 / sqrt((m.x3 - m.x40)**2 + (m.x45 -
    m.x82)**2 + (m.x87 - m.x124)**2) + 1 / sqrt((m.x3 - m.x41)**2 + (m.x45 -
    m.x83)**2 + (m.x87 - m.x125)**2) + 1 / sqrt((m.x3 - m.x42)**2 + (m.x45 -
    m.x84)**2 + (m.x87 - m.x126)**2) + 1 / sqrt((m.x4 - m.x5)**2 + (m.x46 -
    m.x47)**2 + (m.x88 - m.x89)**2) + 1 / sqrt((m.x4 - m.x6)**2 + (m.x46 -
    m.x48)**2 + (m.x88 - m.x90)**2) + 1 / sqrt((m.x4 - m.x7)**2 + (m.x46 -
    m.x49)**2 + (m.x88 - m.x91)**2) + 1 / sqrt((m.x4 - m.x8)**2 + (m.x46 -
    m.x50)**2 + (m.x88 - m.x92)**2) + 1 / sqrt((m.x4 - m.x9)**2 + (m.x46 -
    m.x51)**2 + (m.x88 - m.x93)**2) + 1 / sqrt((m.x4 - m.x10)**2 + (m.x46 -
    m.x52)**2 + (m.x88 - m.x94)**2) + 1 / sqrt((m.x4 - m.x11)**2 + (m.x46 -
    m.x53)**2 + (m.x88 - m.x95)**2) + 1 / sqrt((m.x4 - m.x12)**2 + (m.x46 -
    m.x54)**2 + (m.x88 - m.x96)**2) + 1 / sqrt((m.x4 - m.x13)**2 + (m.x46 -
    m.x55)**2 + (m.x88 - m.x97)**2) + 1 / sqrt((m.x4 - m.x14)**2 + (m.x46 -
    m.x56)**2 + (m.x88 - m.x98)**2) + 1 / sqrt((m.x4 - m.x15)**2 + (m.x46 -
    m.x57)**2 + (m.x88 - m.x99)**2) + 1 / sqrt((m.x4 - m.x16)**2 + (m.x46 -
    m.x58)**2 + (m.x88 - m.x100)**2) + 1 / sqrt((m.x4 - m.x17)**2 + (m.x46 -
    m.x59)**2 + (m.x88 - m.x101)**2) + 1 / sqrt((m.x4 - m.x18)**2 + (m.x46 -
    m.x60)**2 + (m.x88 - m.x102)**2) + 1 / sqrt((m.x4 - m.x19)**2 + (m.x46 -
    m.x61)**2 + (m.x88 - m.x103)**2) + 1 / sqrt((m.x4 - m.x20)**2 + (m.x46 -
    m.x62)**2 + (m.x88 - m.x104)**2) + 1 / sqrt((m.x4 - m.x21)**2 + (m.x46 -
    m.x63)**2 + (m.x88 - m.x105)**2) + 1 / sqrt((m.x4 - m.x22)**2 + (m.x46 -
    m.x64)**2 + (m.x88 - m.x106)**2) + 1 / sqrt((m.x4 - m.x23)**2 + (m.x46 -
    m.x65)**2 + (m.x88 - m.x107)**2) + 1 / sqrt((m.x4 - m.x24)**2 + (m.x46 -
    m.x66)**2 + (m.x88 - m.x108)**2) + 1 / sqrt((m.x4 - m.x25)**2 + (m.x46 -
    m.x67)**2 + (m.x88 - m.x109)**2) + 1 / sqrt((m.x4 - m.x26)**2 + (m.x46 -
    m.x68)**2 + (m.x88 - m.x110)**2) + 1 / sqrt((m.x4 - m.x27)**2 + (m.x46 -
    m.x69)**2 + (m.x88 - m.x111)**2) + 1 / sqrt((m.x4 - m.x28)**2 + (m.x46 -
    m.x70)**2 + (m.x88 - m.x112)**2) + 1 / sqrt((m.x4 - m.x29)**2 + (m.x46 -
    m.x71)**2 + (m.x88 - m.x113)**2) + 1 / sqrt((m.x4 - m.x30)**2 + (m.x46 -
    m.x72)**2 + (m.x88 - m.x114)**2) + 1 / sqrt((m.x4 - m.x31)**2 + (m.x46 -
    m.x73)**2 + (m.x88 - m.x115)**2) + 1 / sqrt((m.x4 - m.x32)**2 + (m.x46 -
    m.x74)**2 + (m.x88 - m.x116)**2) + 1 / sqrt((m.x4 - m.x33)**2 + (m.x46 -
    m.x75)**2 + (m.x88 - m.x117)**2) + 1 / sqrt((m.x4 - m.x34)**2 + (m.x46 -
    m.x76)**2 + (m.x88 - m.x118)**2) + 1 / sqrt((m.x4 - m.x35)**2 + (m.x46 -
    m.x77)**2 + (m.x88 - m.x119)**2) + 1 / sqrt((m.x4 - m.x36)**2 + (m.x46 -
    m.x78)**2 + (m.x88 - m.x120)**2) + 1 / sqrt((m.x4 - m.x37)**2 + (m.x46 -
    m.x79)**2 + (m.x88 - m.x121)**2) + 1 / sqrt((m.x4 - m.x38)**2 + (m.x46 -
    m.x80)**2 + (m.x88 - m.x122)**2) + 1 / sqrt((m.x4 - m.x39)**2 + (m.x46 -
    m.x81)**2 + (m.x88 - m.x123)**2) + 1 / sqrt((m.x4 - m.x40)**2 + (m.x46 -
    m.x82)**2 + (m.x88 - m.x124)**2) + 1 / sqrt((m.x4 - m.x41)**2 + (m.x46 -
    m.x83)**2 + (m.x88 - m.x125)**2) + 1 / sqrt((m.x4 - m.x42)**2 + (m.x46 -
    m.x84)**2 + (m.x88 - m.x126)**2) + 1 / sqrt((m.x5 - m.x6)**2 + (m.x47 -
    m.x48)**2 + (m.x89 - m.x90)**2) + 1 / sqrt((m.x5 - m.x7)**2 + (m.x47 -
    m.x49)**2 + (m.x89 - m.x91)**2) + 1 / sqrt((m.x5 - m.x8)**2 + (m.x47 -
    m.x50)**2 + (m.x89 - m.x92)**2) + 1 / sqrt((m.x5 - m.x9)**2 + (m.x47 -
    m.x51)**2 + (m.x89 - m.x93)**2) + 1 / sqrt((m.x5 - m.x10)**2 + (m.x47 -
    m.x52)**2 + (m.x89 - m.x94)**2) + 1 / sqrt((m.x5 - m.x11)**2 + (m.x47 -
    m.x53)**2 + (m.x89 - m.x95)**2) + 1 / sqrt((m.x5 - m.x12)**2 + (m.x47 -
    m.x54)**2 + (m.x89 - m.x96)**2) + 1 / sqrt((m.x5 - m.x13)**2 + (m.x47 -
    m.x55)**2 + (m.x89 - m.x97)**2) + 1 / sqrt((m.x5 - m.x14)**2 + (m.x47 -
    m.x56)**2 + (m.x89 - m.x98)**2) + 1 / sqrt((m.x5 - m.x15)**2 + (m.x47 -
    m.x57)**2 + (m.x89 - m.x99)**2) + 1 / sqrt((m.x5 - m.x16)**2 + (m.x47 -
    m.x58)**2 + (m.x89 - m.x100)**2) + 1 / sqrt((m.x5 - m.x17)**2 + (m.x47 -
    m.x59)**2 + (m.x89 - m.x101)**2) + 1 / sqrt((m.x5 - m.x18)**2 + (m.x47 -
    m.x60)**2 + (m.x89 - m.x102)**2) + 1 / sqrt((m.x5 - m.x19)**2 + (m.x47 -
    m.x61)**2 + (m.x89 - m.x103)**2) + 1 / sqrt((m.x5 - m.x20)**2 + (m.x47 -
    m.x62)**2 + (m.x89 - m.x104)**2) + 1 / sqrt((m.x5 - m.x21)**2 + (m.x47 -
    m.x63)**2 + (m.x89 - m.x105)**2) + 1 / sqrt((m.x5 - m.x22)**2 + (m.x47 -
    m.x64)**2 + (m.x89 - m.x106)**2) + 1 / sqrt((m.x5 - m.x23)**2 + (m.x47 -
    m.x65)**2 + (m.x89 - m.x107)**2) + 1 / sqrt((m.x5 - m.x24)**2 + (m.x47 -
    m.x66)**2 + (m.x89 - m.x108)**2) + 1 / sqrt((m.x5 - m.x25)**2 + (m.x47 -
    m.x67)**2 + (m.x89 - m.x109)**2) + 1 / sqrt((m.x5 - m.x26)**2 + (m.x47 -
    m.x68)**2 + (m.x89 - m.x110)**2) + 1 / sqrt((m.x5 - m.x27)**2 + (m.x47 -
    m.x69)**2 + (m.x89 - m.x111)**2) + 1 / sqrt((m.x5 - m.x28)**2 + (m.x47 -
    m.x70)**2 + (m.x89 - m.x112)**2) + 1 / sqrt((m.x5 - m.x29)**2 + (m.x47 -
    m.x71)**2 + (m.x89 - m.x113)**2) + 1 / sqrt((m.x5 - m.x30)**2 + (m.x47 -
    m.x72)**2 + (m.x89 - m.x114)**2) + 1 / sqrt((m.x5 - m.x31)**2 + (m.x47 -
    m.x73)**2 + (m.x89 - m.x115)**2) + 1 / sqrt((m.x5 - m.x32)**2 + (m.x47 -
    m.x74)**2 + (m.x89 - m.x116)**2) + 1 / sqrt((m.x5 - m.x33)**2 + (m.x47 -
    m.x75)**2 + (m.x89 - m.x117)**2) + 1 / sqrt((m.x5 - m.x34)**2 + (m.x47 -
    m.x76)**2 + (m.x89 - m.x118)**2) + 1 / sqrt((m.x5 - m.x35)**2 + (m.x47 -
    m.x77)**2 + (m.x89 - m.x119)**2) + 1 / sqrt((m.x5 - m.x36)**2 + (m.x47 -
    m.x78)**2 + (m.x89 - m.x120)**2) + 1 / sqrt((m.x5 - m.x37)**2 + (m.x47 -
    m.x79)**2 + (m.x89 - m.x121)**2) + 1 / sqrt((m.x5 - m.x38)**2 + (m.x47 -
    m.x80)**2 + (m.x89 - m.x122)**2) + 1 / sqrt((m.x5 - m.x39)**2 + (m.x47 -
    m.x81)**2 + (m.x89 - m.x123)**2) + 1 / sqrt((m.x5 - m.x40)**2 + (m.x47 -
    m.x82)**2 + (m.x89 - m.x124)**2) + 1 / sqrt((m.x5 - m.x41)**2 + (m.x47 -
    m.x83)**2 + (m.x89 - m.x125)**2) + 1 / sqrt((m.x5 - m.x42)**2 + (m.x47 -
    m.x84)**2 + (m.x89 - m.x126)**2) + 1 / sqrt((m.x6 - m.x7)**2 + (m.x48 -
    m.x49)**2 + (m.x90 - m.x91)**2) + 1 / sqrt((m.x6 - m.x8)**2 + (m.x48 -
    m.x50)**2 + (m.x90 - m.x92)**2) + 1 / sqrt((m.x6 - m.x9)**2 + (m.x48 -
    m.x51)**2 + (m.x90 - m.x93)**2) + 1 / sqrt((m.x6 - m.x10)**2 + (m.x48 -
    m.x52)**2 + (m.x90 - m.x94)**2) + 1 / sqrt((m.x6 - m.x11)**2 + (m.x48 -
    m.x53)**2 + (m.x90 - m.x95)**2) + 1 / sqrt((m.x6 - m.x12)**2 + (m.x48 -
    m.x54)**2 + (m.x90 - m.x96)**2) + 1 / sqrt((m.x6 - m.x13)**2 + (m.x48 -
    m.x55)**2 + (m.x90 - m.x97)**2) + 1 / sqrt((m.x6 - m.x14)**2 + (m.x48 -
    m.x56)**2 + (m.x90 - m.x98)**2) + 1 / sqrt((m.x6 - m.x15)**2 + (m.x48 -
    m.x57)**2 + (m.x90 - m.x99)**2) + 1 / sqrt((m.x6 - m.x16)**2 + (m.x48 -
    m.x58)**2 + (m.x90 - m.x100)**2) + 1 / sqrt((m.x6 - m.x17)**2 + (m.x48 -
    m.x59)**2 + (m.x90 - m.x101)**2) + 1 / sqrt((m.x6 - m.x18)**2 + (m.x48 -
    m.x60)**2 + (m.x90 - m.x102)**2) + 1 / sqrt((m.x6 - m.x19)**2 + (m.x48 -
    m.x61)**2 + (m.x90 - m.x103)**2) + 1 / sqrt((m.x6 - m.x20)**2 + (m.x48 -
    m.x62)**2 + (m.x90 - m.x104)**2) + 1 / sqrt((m.x6 - m.x21)**2 + (m.x48 -
    m.x63)**2 + (m.x90 - m.x105)**2) + 1 / sqrt((m.x6 - m.x22)**2 + (m.x48 -
    m.x64)**2 + (m.x90 - m.x106)**2) + 1 / sqrt((m.x6 - m.x23)**2 + (m.x48 -
    m.x65)**2 + (m.x90 - m.x107)**2) + 1 / sqrt((m.x6 - m.x24)**2 + (m.x48 -
    m.x66)**2 + (m.x90 - m.x108)**2) + 1 / sqrt((m.x6 - m.x25)**2 + (m.x48 -
    m.x67)**2 + (m.x90 - m.x109)**2) + 1 / sqrt((m.x6 - m.x26)**2 + (m.x48 -
    m.x68)**2 + (m.x90 - m.x110)**2) + 1 / sqrt((m.x6 - m.x27)**2 + (m.x48 -
    m.x69)**2 + (m.x90 - m.x111)**2) + 1 / sqrt((m.x6 - m.x28)**2 + (m.x48 -
    m.x70)**2 + (m.x90 - m.x112)**2) + 1 / sqrt((m.x6 - m.x29)**2 + (m.x48 -
    m.x71)**2 + (m.x90 - m.x113)**2) + 1 / sqrt((m.x6 - m.x30)**2 + (m.x48 -
    m.x72)**2 + (m.x90 - m.x114)**2) + 1 / sqrt((m.x6 - m.x31)**2 + (m.x48 -
    m.x73)**2 + (m.x90 - m.x115)**2) + 1 / sqrt((m.x6 - m.x32)**2 + (m.x48 -
    m.x74)**2 + (m.x90 - m.x116)**2) + 1 / sqrt((m.x6 - m.x33)**2 + (m.x48 -
    m.x75)**2 + (m.x90 - m.x117)**2) + 1 / sqrt((m.x6 - m.x34)**2 + (m.x48 -
    m.x76)**2 + (m.x90 - m.x118)**2) + 1 / sqrt((m.x6 - m.x35)**2 + (m.x48 -
    m.x77)**2 + (m.x90 - m.x119)**2) + 1 / sqrt((m.x6 - m.x36)**2 + (m.x48 -
    m.x78)**2 + (m.x90 - m.x120)**2) + 1 / sqrt((m.x6 - m.x37)**2 + (m.x48 -
    m.x79)**2 + (m.x90 - m.x121)**2) + 1 / sqrt((m.x6 - m.x38)**2 + (m.x48 -
    m.x80)**2 + (m.x90 - m.x122)**2) + 1 / sqrt((m.x6 - m.x39)**2 + (m.x48 -
    m.x81)**2 + (m.x90 - m.x123)**2) + 1 / sqrt((m.x6 - m.x40)**2 + (m.x48 -
    m.x82)**2 + (m.x90 - m.x124)**2) + 1 / sqrt((m.x6 - m.x41)**2 + (m.x48 -
    m.x83)**2 + (m.x90 - m.x125)**2) + 1 / sqrt((m.x6 - m.x42)**2 + (m.x48 -
    m.x84)**2 + (m.x90 - m.x126)**2) + 1 / sqrt((m.x7 - m.x8)**2 + (m.x49 -
    m.x50)**2 + (m.x91 - m.x92)**2) + 1 / sqrt((m.x7 - m.x9)**2 + (m.x49 -
    m.x51)**2 + (m.x91 - m.x93)**2) + 1 / sqrt((m.x7 - m.x10)**2 + (m.x49 -
    m.x52)**2 + (m.x91 - m.x94)**2) + 1 / sqrt((m.x7 - m.x11)**2 + (m.x49 -
    m.x53)**2 + (m.x91 - m.x95)**2) + 1 / sqrt((m.x7 - m.x12)**2 + (m.x49 -
    m.x54)**2 + (m.x91 - m.x96)**2) + 1 / sqrt((m.x7 - m.x13)**2 + (m.x49 -
    m.x55)**2 + (m.x91 - m.x97)**2) + 1 / sqrt((m.x7 - m.x14)**2 + (m.x49 -
    m.x56)**2 + (m.x91 - m.x98)**2) + 1 / sqrt((m.x7 - m.x15)**2 + (m.x49 -
    m.x57)**2 + (m.x91 - m.x99)**2) + 1 / sqrt((m.x7 - m.x16)**2 + (m.x49 -
    m.x58)**2 + (m.x91 - m.x100)**2) + 1 / sqrt((m.x7 - m.x17)**2 + (m.x49 -
    m.x59)**2 + (m.x91 - m.x101)**2) + 1 / sqrt((m.x7 - m.x18)**2 + (m.x49 -
    m.x60)**2 + (m.x91 - m.x102)**2) + 1 / sqrt((m.x7 - m.x19)**2 + (m.x49 -
    m.x61)**2 + (m.x91 - m.x103)**2) + 1 / sqrt((m.x7 - m.x20)**2 + (m.x49 -
    m.x62)**2 + (m.x91 - m.x104)**2) + 1 / sqrt((m.x7 - m.x21)**2 + (m.x49 -
    m.x63)**2 + (m.x91 - m.x105)**2) + 1 / sqrt((m.x7 - m.x22)**2 + (m.x49 -
    m.x64)**2 + (m.x91 - m.x106)**2) + 1 / sqrt((m.x7 - m.x23)**2 + (m.x49 -
    m.x65)**2 + (m.x91 - m.x107)**2) + 1 / sqrt((m.x7 - m.x24)**2 + (m.x49 -
    m.x66)**2 + (m.x91 - m.x108)**2) + 1 / sqrt((m.x7 - m.x25)**2 + (m.x49 -
    m.x67)**2 + (m.x91 - m.x109)**2) + 1 / sqrt((m.x7 - m.x26)**2 + (m.x49 -
    m.x68)**2 + (m.x91 - m.x110)**2) + 1 / sqrt((m.x7 - m.x27)**2 + (m.x49 -
    m.x69)**2 + (m.x91 - m.x111)**2) + 1 / sqrt((m.x7 - m.x28)**2 + (m.x49 -
    m.x70)**2 + (m.x91 - m.x112)**2) + 1 / sqrt((m.x7 - m.x29)**2 + (m.x49 -
    m.x71)**2 + (m.x91 - m.x113)**2) + 1 / sqrt((m.x7 - m.x30)**2 + (m.x49 -
    m.x72)**2 + (m.x91 - m.x114)**2) + 1 / sqrt((m.x7 - m.x31)**2 + (m.x49 -
    m.x73)**2 + (m.x91 - m.x115)**2) + 1 / sqrt((m.x7 - m.x32)**2 + (m.x49 -
    m.x74)**2 + (m.x91 - m.x116)**2) + 1 / sqrt((m.x7 - m.x33)**2 + (m.x49 -
    m.x75)**2 + (m.x91 - m.x117)**2) + 1 / sqrt((m.x7 - m.x34)**2 + (m.x49 -
    m.x76)**2 + (m.x91 - m.x118)**2) + 1 / sqrt((m.x7 - m.x35)**2 + (m.x49 -
    m.x77)**2 + (m.x91 - m.x119)**2) + 1 / sqrt((m.x7 - m.x36)**2 + (m.x49 -
    m.x78)**2 + (m.x91 - m.x120)**2) + 1 / sqrt((m.x7 - m.x37)**2 + (m.x49 -
    m.x79)**2 + (m.x91 - m.x121)**2) + 1 / sqrt((m.x7 - m.x38)**2 + (m.x49 -
    m.x80)**2 + (m.x91 - m.x122)**2) + 1 / sqrt((m.x7 - m.x39)**2 + (m.x49 -
    m.x81)**2 + (m.x91 - m.x123)**2) + 1 / sqrt((m.x7 - m.x40)**2 + (m.x49 -
    m.x82)**2 + (m.x91 - m.x124)**2) + 1 / sqrt((m.x7 - m.x41)**2 + (m.x49 -
    m.x83)**2 + (m.x91 - m.x125)**2) + 1 / sqrt((m.x7 - m.x42)**2 + (m.x49 -
    m.x84)**2 + (m.x91 - m.x126)**2) + 1 / sqrt((m.x8 - m.x9)**2 + (m.x50 -
    m.x51)**2 + (m.x92 - m.x93)**2) + 1 / sqrt((m.x8 - m.x10)**2 + (m.x50 -
    m.x52)**2 + (m.x92 - m.x94)**2) + 1 / sqrt((m.x8 - m.x11)**2 + (m.x50 -
    m.x53)**2 + (m.x92 - m.x95)**2) + 1 / sqrt((m.x8 - m.x12)**2 + (m.x50 -
    m.x54)**2 + (m.x92 - m.x96)**2) + 1 / sqrt((m.x8 - m.x13)**2 + (m.x50 -
    m.x55)**2 + (m.x92 - m.x97)**2) + 1 / sqrt((m.x8 - m.x14)**2 + (m.x50 -
    m.x56)**2 + (m.x92 - m.x98)**2) + 1 / sqrt((m.x8 - m.x15)**2 + (m.x50 -
    m.x57)**2 + (m.x92 - m.x99)**2) + 1 / sqrt((m.x8 - m.x16)**2 + (m.x50 -
    m.x58)**2 + (m.x92 - m.x100)**2) + 1 / sqrt((m.x8 - m.x17)**2 + (m.x50 -
    m.x59)**2 + (m.x92 - m.x101)**2) + 1 / sqrt((m.x8 - m.x18)**2 + (m.x50 -
    m.x60)**2 + (m.x92 - m.x102)**2) + 1 / sqrt((m.x8 - m.x19)**2 + (m.x50 -
    m.x61)**2 + (m.x92 - m.x103)**2) + 1 / sqrt((m.x8 - m.x20)**2 + (m.x50 -
    m.x62)**2 + (m.x92 - m.x104)**2) + 1 / sqrt((m.x8 - m.x21)**2 + (m.x50 -
    m.x63)**2 + (m.x92 - m.x105)**2) + 1 / sqrt((m.x8 - m.x22)**2 + (m.x50 -
    m.x64)**2 + (m.x92 - m.x106)**2) + 1 / sqrt((m.x8 - m.x23)**2 + (m.x50 -
    m.x65)**2 + (m.x92 - m.x107)**2) + 1 / sqrt((m.x8 - m.x24)**2 + (m.x50 -
    m.x66)**2 + (m.x92 - m.x108)**2) + 1 / sqrt((m.x8 - m.x25)**2 + (m.x50 -
    m.x67)**2 + (m.x92 - m.x109)**2) + 1 / sqrt((m.x8 - m.x26)**2 + (m.x50 -
    m.x68)**2 + (m.x92 - m.x110)**2) + 1 / sqrt((m.x8 - m.x27)**2 + (m.x50 -
    m.x69)**2 + (m.x92 - m.x111)**2) + 1 / sqrt((m.x8 - m.x28)**2 + (m.x50 -
    m.x70)**2 + (m.x92 - m.x112)**2) + 1 / sqrt((m.x8 - m.x29)**2 + (m.x50 -
    m.x71)**2 + (m.x92 - m.x113)**2) + 1 / sqrt((m.x8 - m.x30)**2 + (m.x50 -
    m.x72)**2 + (m.x92 - m.x114)**2) + 1 / sqrt((m.x8 - m.x31)**2 + (m.x50 -
    m.x73)**2 + (m.x92 - m.x115)**2) + 1 / sqrt((m.x8 - m.x32)**2 + (m.x50 -
    m.x74)**2 + (m.x92 - m.x116)**2) + 1 / sqrt((m.x8 - m.x33)**2 + (m.x50 -
    m.x75)**2 + (m.x92 - m.x117)**2) + 1 / sqrt((m.x8 - m.x34)**2 + (m.x50 -
    m.x76)**2 + (m.x92 - m.x118)**2) + 1 / sqrt((m.x8 - m.x35)**2 + (m.x50 -
    m.x77)**2 + (m.x92 - m.x119)**2) + 1 / sqrt((m.x8 - m.x36)**2 + (m.x50 -
    m.x78)**2 + (m.x92 - m.x120)**2) + 1 / sqrt((m.x8 - m.x37)**2 + (m.x50 -
    m.x79)**2 + (m.x92 - m.x121)**2) + 1 / sqrt((m.x8 - m.x38)**2 + (m.x50 -
    m.x80)**2 + (m.x92 - m.x122)**2) + 1 / sqrt((m.x8 - m.x39)**2 + (m.x50 -
    m.x81)**2 + (m.x92 - m.x123)**2) + 1 / sqrt((m.x8 - m.x40)**2 + (m.x50 -
    m.x82)**2 + (m.x92 - m.x124)**2) + 1 / sqrt((m.x8 - m.x41)**2 + (m.x50 -
    m.x83)**2 + (m.x92 - m.x125)**2) + 1 / sqrt((m.x8 - m.x42)**2 + (m.x50 -
    m.x84)**2 + (m.x92 - m.x126)**2) + 1 / sqrt((m.x9 - m.x10)**2 + (m.x51 -
    m.x52)**2 + (m.x93 - m.x94)**2) + 1 / sqrt((m.x9 - m.x11)**2 + (m.x51 -
    m.x53)**2 + (m.x93 - m.x95)**2) + 1 / sqrt((m.x9 - m.x12)**2 + (m.x51 -
    m.x54)**2 + (m.x93 - m.x96)**2) + 1 / sqrt((m.x9 - m.x13)**2 + (m.x51 -
    m.x55)**2 + (m.x93 - m.x97)**2) + 1 / sqrt((m.x9 - m.x14)**2 + (m.x51 -
    m.x56)**2 + (m.x93 - m.x98)**2) + 1 / sqrt((m.x9 - m.x15)**2 + (m.x51 -
    m.x57)**2 + (m.x93 - m.x99)**2) + 1 / sqrt((m.x9 - m.x16)**2 + (m.x51 -
    m.x58)**2 + (m.x93 - m.x100)**2) + 1 / sqrt((m.x9 - m.x17)**2 + (m.x51 -
    m.x59)**2 + (m.x93 - m.x101)**2) + 1 / sqrt((m.x9 - m.x18)**2 + (m.x51 -
    m.x60)**2 + (m.x93 - m.x102)**2) + 1 / sqrt((m.x9 - m.x19)**2 + (m.x51 -
    m.x61)**2 + (m.x93 - m.x103)**2) + 1 / sqrt((m.x9 - m.x20)**2 + (m.x51 -
    m.x62)**2 + (m.x93 - m.x104)**2) + 1 / sqrt((m.x9 - m.x21)**2 + (m.x51 -
    m.x63)**2 + (m.x93 - m.x105)**2) + 1 / sqrt((m.x9 - m.x22)**2 + (m.x51 -
    m.x64)**2 + (m.x93 - m.x106)**2) + 1 / sqrt((m.x9 - m.x23)**2 + (m.x51 -
    m.x65)**2 + (m.x93 - m.x107)**2) + 1 / sqrt((m.x9 - m.x24)**2 + (m.x51 -
    m.x66)**2 + (m.x93 - m.x108)**2) + 1 / sqrt((m.x9 - m.x25)**2 + (m.x51 -
    m.x67)**2 + (m.x93 - m.x109)**2) + 1 / sqrt((m.x9 - m.x26)**2 + (m.x51 -
    m.x68)**2 + (m.x93 - m.x110)**2) + 1 / sqrt((m.x9 - m.x27)**2 + (m.x51 -
    m.x69)**2 + (m.x93 - m.x111)**2) + 1 / sqrt((m.x9 - m.x28)**2 + (m.x51 -
    m.x70)**2 + (m.x93 - m.x112)**2) + 1 / sqrt((m.x9 - m.x29)**2 + (m.x51 -
    m.x71)**2 + (m.x93 - m.x113)**2) + 1 / sqrt((m.x9 - m.x30)**2 + (m.x51 -
    m.x72)**2 + (m.x93 - m.x114)**2) + 1 / sqrt((m.x9 - m.x31)**2 + (m.x51 -
    m.x73)**2 + (m.x93 - m.x115)**2) + 1 / sqrt((m.x9 - m.x32)**2 + (m.x51 -
    m.x74)**2 + (m.x93 - m.x116)**2) + 1 / sqrt((m.x9 - m.x33)**2 + (m.x51 -
    m.x75)**2 + (m.x93 - m.x117)**2) + 1 / sqrt((m.x9 - m.x34)**2 + (m.x51 -
    m.x76)**2 + (m.x93 - m.x118)**2) + 1 / sqrt((m.x9 - m.x35)**2 + (m.x51 -
    m.x77)**2 + (m.x93 - m.x119)**2) + 1 / sqrt((m.x9 - m.x36)**2 + (m.x51 -
    m.x78)**2 + (m.x93 - m.x120)**2) + 1 / sqrt((m.x9 - m.x37)**2 + (m.x51 -
    m.x79)**2 + (m.x93 - m.x121)**2) + 1 / sqrt((m.x9 - m.x38)**2 + (m.x51 -
    m.x80)**2 + (m.x93 - m.x122)**2) + 1 / sqrt((m.x9 - m.x39)**2 + (m.x51 -
    m.x81)**2 + (m.x93 - m.x123)**2) + 1 / sqrt((m.x9 - m.x40)**2 + (m.x51 -
    m.x82)**2 + (m.x93 - m.x124)**2) + 1 / sqrt((m.x9 - m.x41)**2 + (m.x51 -
    m.x83)**2 + (m.x93 - m.x125)**2) + 1 / sqrt((m.x9 - m.x42)**2 + (m.x51 -
    m.x84)**2 + (m.x93 - m.x126)**2) + 1 / sqrt((m.x10 - m.x11)**2 + (m.x52 -
    m.x53)**2 + (m.x94 - m.x95)**2) + 1 / sqrt((m.x10 - m.x12)**2 + (m.x52 -
    m.x54)**2 + (m.x94 - m.x96)**2) + 1 / sqrt((m.x10 - m.x13)**2 + (m.x52 -
    m.x55)**2 + (m.x94 - m.x97)**2) + 1 / sqrt((m.x10 - m.x14)**2 + (m.x52 -
    m.x56)**2 + (m.x94 - m.x98)**2) + 1 / sqrt((m.x10 - m.x15)**2 + (m.x52 -
    m.x57)**2 + (m.x94 - m.x99)**2) + 1 / sqrt((m.x10 - m.x16)**2 + (m.x52 -
    m.x58)**2 + (m.x94 - m.x100)**2) + 1 / sqrt((m.x10 - m.x17)**2 + (m.x52 -
    m.x59)**2 + (m.x94 - m.x101)**2) + 1 / sqrt((m.x10 - m.x18)**2 + (m.x52 -
    m.x60)**2 + (m.x94 - m.x102)**2) + 1 / sqrt((m.x10 - m.x19)**2 + (m.x52 -
    m.x61)**2 + (m.x94 - m.x103)**2) + 1 / sqrt((m.x10 - m.x20)**2 + (m.x52 -
    m.x62)**2 + (m.x94 - m.x104)**2) + 1 / sqrt((m.x10 - m.x21)**2 + (m.x52 -
    m.x63)**2 + (m.x94 - m.x105)**2) + 1 / sqrt((m.x10 - m.x22)**2 + (m.x52 -
    m.x64)**2 + (m.x94 - m.x106)**2) + 1 / sqrt((m.x10 - m.x23)**2 + (m.x52 -
    m.x65)**2 + (m.x94 - m.x107)**2) + 1 / sqrt((m.x10 - m.x24)**2 + (m.x52 -
    m.x66)**2 + (m.x94 - m.x108)**2) + 1 / sqrt((m.x10 - m.x25)**2 + (m.x52 -
    m.x67)**2 + (m.x94 - m.x109)**2) + 1 / sqrt((m.x10 - m.x26)**2 + (m.x52 -
    m.x68)**2 + (m.x94 - m.x110)**2) + 1 / sqrt((m.x10 - m.x27)**2 + (m.x52 -
    m.x69)**2 + (m.x94 - m.x111)**2) + 1 / sqrt((m.x10 - m.x28)**2 + (m.x52 -
    m.x70)**2 + (m.x94 - m.x112)**2) + 1 / sqrt((m.x10 - m.x29)**2 + (m.x52 -
    m.x71)**2 + (m.x94 - m.x113)**2) + 1 / sqrt((m.x10 - m.x30)**2 + (m.x52 -
    m.x72)**2 + (m.x94 - m.x114)**2) + 1 / sqrt((m.x10 - m.x31)**2 + (m.x52 -
    m.x73)**2 + (m.x94 - m.x115)**2) + 1 / sqrt((m.x10 - m.x32)**2 + (m.x52 -
    m.x74)**2 + (m.x94 - m.x116)**2) + 1 / sqrt((m.x10 - m.x33)**2 + (m.x52 -
    m.x75)**2 + (m.x94 - m.x117)**2) + 1 / sqrt((m.x10 - m.x34)**2 + (m.x52 -
    m.x76)**2 + (m.x94 - m.x118)**2) + 1 / sqrt((m.x10 - m.x35)**2 + (m.x52 -
    m.x77)**2 + (m.x94 - m.x119)**2) + 1 / sqrt((m.x10 - m.x36)**2 + (m.x52 -
    m.x78)**2 + (m.x94 - m.x120)**2) + 1 / sqrt((m.x10 - m.x37)**2 + (m.x52 -
    m.x79)**2 + (m.x94 - m.x121)**2) + 1 / sqrt((m.x10 - m.x38)**2 + (m.x52 -
    m.x80)**2 + (m.x94 - m.x122)**2) + 1 / sqrt((m.x10 - m.x39)**2 + (m.x52 -
    m.x81)**2 + (m.x94 - m.x123)**2) + 1 / sqrt((m.x10 - m.x40)**2 + (m.x52 -
    m.x82)**2 + (m.x94 - m.x124)**2) + 1 / sqrt((m.x10 - m.x41)**2 + (m.x52 -
    m.x83)**2 + (m.x94 - m.x125)**2) + 1 / sqrt((m.x10 - m.x42)**2 + (m.x52 -
    m.x84)**2 + (m.x94 - m.x126)**2) + 1 / sqrt((m.x11 - m.x12)**2 + (m.x53 -
    m.x54)**2 + (m.x95 - m.x96)**2) + 1 / sqrt((m.x11 - m.x13)**2 + (m.x53 -
    m.x55)**2 + (m.x95 - m.x97)**2) + 1 / sqrt((m.x11 - m.x14)**2 + (m.x53 -
    m.x56)**2 + (m.x95 - m.x98)**2) + 1 / sqrt((m.x11 - m.x15)**2 + (m.x53 -
    m.x57)**2 + (m.x95 - m.x99)**2) + 1 / sqrt((m.x11 - m.x16)**2 + (m.x53 -
    m.x58)**2 + (m.x95 - m.x100)**2) + 1 / sqrt((m.x11 - m.x17)**2 + (m.x53 -
    m.x59)**2 + (m.x95 - m.x101)**2) + 1 / sqrt((m.x11 - m.x18)**2 + (m.x53 -
    m.x60)**2 + (m.x95 - m.x102)**2) + 1 / sqrt((m.x11 - m.x19)**2 + (m.x53 -
    m.x61)**2 + (m.x95 - m.x103)**2) + 1 / sqrt((m.x11 - m.x20)**2 + (m.x53 -
    m.x62)**2 + (m.x95 - m.x104)**2) + 1 / sqrt((m.x11 - m.x21)**2 + (m.x53 -
    m.x63)**2 + (m.x95 - m.x105)**2) + 1 / sqrt((m.x11 - m.x22)**2 + (m.x53 -
    m.x64)**2 + (m.x95 - m.x106)**2) + 1 / sqrt((m.x11 - m.x23)**2 + (m.x53 -
    m.x65)**2 + (m.x95 - m.x107)**2) + 1 / sqrt((m.x11 - m.x24)**2 + (m.x53 -
    m.x66)**2 + (m.x95 - m.x108)**2) + 1 / sqrt((m.x11 - m.x25)**2 + (m.x53 -
    m.x67)**2 + (m.x95 - m.x109)**2) + 1 / sqrt((m.x11 - m.x26)**2 + (m.x53 -
    m.x68)**2 + (m.x95 - m.x110)**2) + 1 / sqrt((m.x11 - m.x27)**2 + (m.x53 -
    m.x69)**2 + (m.x95 - m.x111)**2) + 1 / sqrt((m.x11 - m.x28)**2 + (m.x53 -
    m.x70)**2 + (m.x95 - m.x112)**2) + 1 / sqrt((m.x11 - m.x29)**2 + (m.x53 -
    m.x71)**2 + (m.x95 - m.x113)**2) + 1 / sqrt((m.x11 - m.x30)**2 + (m.x53 -
    m.x72)**2 + (m.x95 - m.x114)**2) + 1 / sqrt((m.x11 - m.x31)**2 + (m.x53 -
    m.x73)**2 + (m.x95 - m.x115)**2) + 1 / sqrt((m.x11 - m.x32)**2 + (m.x53 -
    m.x74)**2 + (m.x95 - m.x116)**2) + 1 / sqrt((m.x11 - m.x33)**2 + (m.x53 -
    m.x75)**2 + (m.x95 - m.x117)**2) + 1 / sqrt((m.x11 - m.x34)**2 + (m.x53 -
    m.x76)**2 + (m.x95 - m.x118)**2) + 1 / sqrt((m.x11 - m.x35)**2 + (m.x53 -
    m.x77)**2 + (m.x95 - m.x119)**2) + 1 / sqrt((m.x11 - m.x36)**2 + (m.x53 -
    m.x78)**2 + (m.x95 - m.x120)**2) + 1 / sqrt((m.x11 - m.x37)**2 + (m.x53 -
    m.x79)**2 + (m.x95 - m.x121)**2) + 1 / sqrt((m.x11 - m.x38)**2 + (m.x53 -
    m.x80)**2 + (m.x95 - m.x122)**2) + 1 / sqrt((m.x11 - m.x39)**2 + (m.x53 -
    m.x81)**2 + (m.x95 - m.x123)**2) + 1 / sqrt((m.x11 - m.x40)**2 + (m.x53 -
    m.x82)**2 + (m.x95 - m.x124)**2) + 1 / sqrt((m.x11 - m.x41)**2 + (m.x53 -
    m.x83)**2 + (m.x95 - m.x125)**2) + 1 / sqrt((m.x11 - m.x42)**2 + (m.x53 -
    m.x84)**2 + (m.x95 - m.x126)**2) + 1 / sqrt((m.x12 - m.x13)**2 + (m.x54 -
    m.x55)**2 + (m.x96 - m.x97)**2) + 1 / sqrt((m.x12 - m.x14)**2 + (m.x54 -
    m.x56)**2 + (m.x96 - m.x98)**2) + 1 / sqrt((m.x12 - m.x15)**2 + (m.x54 -
    m.x57)**2 + (m.x96 - m.x99)**2) + 1 / sqrt((m.x12 - m.x16)**2 + (m.x54 -
    m.x58)**2 + (m.x96 - m.x100)**2) + 1 / sqrt((m.x12 - m.x17)**2 + (m.x54 -
    m.x59)**2 + (m.x96 - m.x101)**2) + 1 / sqrt((m.x12 - m.x18)**2 + (m.x54 -
    m.x60)**2 + (m.x96 - m.x102)**2) + 1 / sqrt((m.x12 - m.x19)**2 + (m.x54 -
    m.x61)**2 + (m.x96 - m.x103)**2) + 1 / sqrt((m.x12 - m.x20)**2 + (m.x54 -
    m.x62)**2 + (m.x96 - m.x104)**2) + 1 / sqrt((m.x12 - m.x21)**2 + (m.x54 -
    m.x63)**2 + (m.x96 - m.x105)**2) + 1 / sqrt((m.x12 - m.x22)**2 + (m.x54 -
    m.x64)**2 + (m.x96 - m.x106)**2) + 1 / sqrt((m.x12 - m.x23)**2 + (m.x54 -
    m.x65)**2 + (m.x96 - m.x107)**2) + 1 / sqrt((m.x12 - m.x24)**2 + (m.x54 -
    m.x66)**2 + (m.x96 - m.x108)**2) + 1 / sqrt((m.x12 - m.x25)**2 + (m.x54 -
    m.x67)**2 + (m.x96 - m.x109)**2) + 1 / sqrt((m.x12 - m.x26)**2 + (m.x54 -
    m.x68)**2 + (m.x96 - m.x110)**2) + 1 / sqrt((m.x12 - m.x27)**2 + (m.x54 -
    m.x69)**2 + (m.x96 - m.x111)**2) + 1 / sqrt((m.x12 - m.x28)**2 + (m.x54 -
    m.x70)**2 + (m.x96 - m.x112)**2) + 1 / sqrt((m.x12 - m.x29)**2 + (m.x54 -
    m.x71)**2 + (m.x96 - m.x113)**2) + 1 / sqrt((m.x12 - m.x30)**2 + (m.x54 -
    m.x72)**2 + (m.x96 - m.x114)**2) + 1 / sqrt((m.x12 - m.x31)**2 + (m.x54 -
    m.x73)**2 + (m.x96 - m.x115)**2) + 1 / sqrt((m.x12 - m.x32)**2 + (m.x54 -
    m.x74)**2 + (m.x96 - m.x116)**2) + 1 / sqrt((m.x12 - m.x33)**2 + (m.x54 -
    m.x75)**2 + (m.x96 - m.x117)**2) + 1 / sqrt((m.x12 - m.x34)**2 + (m.x54 -
    m.x76)**2 + (m.x96 - m.x118)**2) + 1 / sqrt((m.x12 - m.x35)**2 + (m.x54 -
    m.x77)**2 + (m.x96 - m.x119)**2) + 1 / sqrt((m.x12 - m.x36)**2 + (m.x54 -
    m.x78)**2 + (m.x96 - m.x120)**2) + 1 / sqrt((m.x12 - m.x37)**2 + (m.x54 -
    m.x79)**2 + (m.x96 - m.x121)**2) + 1 / sqrt((m.x12 - m.x38)**2 + (m.x54 -
    m.x80)**2 + (m.x96 - m.x122)**2) + 1 / sqrt((m.x12 - m.x39)**2 + (m.x54 -
    m.x81)**2 + (m.x96 - m.x123)**2) + 1 / sqrt((m.x12 - m.x40)**2 + (m.x54 -
    m.x82)**2 + (m.x96 - m.x124)**2) + 1 / sqrt((m.x12 - m.x41)**2 + (m.x54 -
    m.x83)**2 + (m.x96 - m.x125)**2) + 1 / sqrt((m.x12 - m.x42)**2 + (m.x54 -
    m.x84)**2 + (m.x96 - m.x126)**2) + 1 / sqrt((m.x13 - m.x14)**2 + (m.x55 -
    m.x56)**2 + (m.x97 - m.x98)**2) + 1 / sqrt((m.x13 - m.x15)**2 + (m.x55 -
    m.x57)**2 + (m.x97 - m.x99)**2) + 1 / sqrt((m.x13 - m.x16)**2 + (m.x55 -
    m.x58)**2 + (m.x97 - m.x100)**2) + 1 / sqrt((m.x13 - m.x17)**2 + (m.x55 -
    m.x59)**2 + (m.x97 - m.x101)**2) + 1 / sqrt((m.x13 - m.x18)**2 + (m.x55 -
    m.x60)**2 + (m.x97 - m.x102)**2) + 1 / sqrt((m.x13 - m.x19)**2 + (m.x55 -
    m.x61)**2 + (m.x97 - m.x103)**2) + 1 / sqrt((m.x13 - m.x20)**2 + (m.x55 -
    m.x62)**2 + (m.x97 - m.x104)**2) + 1 / sqrt((m.x13 - m.x21)**2 + (m.x55 -
    m.x63)**2 + (m.x97 - m.x105)**2) + 1 / sqrt((m.x13 - m.x22)**2 + (m.x55 -
    m.x64)**2 + (m.x97 - m.x106)**2) + 1 / sqrt((m.x13 - m.x23)**2 + (m.x55 -
    m.x65)**2 + (m.x97 - m.x107)**2) + 1 / sqrt((m.x13 - m.x24)**2 + (m.x55 -
    m.x66)**2 + (m.x97 - m.x108)**2) + 1 / sqrt((m.x13 - m.x25)**2 + (m.x55 -
    m.x67)**2 + (m.x97 - m.x109)**2) + 1 / sqrt((m.x13 - m.x26)**2 + (m.x55 -
    m.x68)**2 + (m.x97 - m.x110)**2) + 1 / sqrt((m.x13 - m.x27)**2 + (m.x55 -
    m.x69)**2 + (m.x97 - m.x111)**2) + 1 / sqrt((m.x13 - m.x28)**2 + (m.x55 -
    m.x70)**2 + (m.x97 - m.x112)**2) + 1 / sqrt((m.x13 - m.x29)**2 + (m.x55 -
    m.x71)**2 + (m.x97 - m.x113)**2) + 1 / sqrt((m.x13 - m.x30)**2 + (m.x55 -
    m.x72)**2 + (m.x97 - m.x114)**2) + 1 / sqrt((m.x13 - m.x31)**2 + (m.x55 -
    m.x73)**2 + (m.x97 - m.x115)**2) + 1 / sqrt((m.x13 - m.x32)**2 + (m.x55 -
    m.x74)**2 + (m.x97 - m.x116)**2) + 1 / sqrt((m.x13 - m.x33)**2 + (m.x55 -
    m.x75)**2 + (m.x97 - m.x117)**2) + 1 / sqrt((m.x13 - m.x34)**2 + (m.x55 -
    m.x76)**2 + (m.x97 - m.x118)**2) + 1 / sqrt((m.x13 - m.x35)**2 + (m.x55 -
    m.x77)**2 + (m.x97 - m.x119)**2) + 1 / sqrt((m.x13 - m.x36)**2 + (m.x55 -
    m.x78)**2 + (m.x97 - m.x120)**2) + 1 / sqrt((m.x13 - m.x37)**2 + (m.x55 -
    m.x79)**2 + (m.x97 - m.x121)**2) + 1 / sqrt((m.x13 - m.x38)**2 + (m.x55 -
    m.x80)**2 + (m.x97 - m.x122)**2) + 1 / sqrt((m.x13 - m.x39)**2 + (m.x55 -
    m.x81)**2 + (m.x97 - m.x123)**2) + 1 / sqrt((m.x13 - m.x40)**2 + (m.x55 -
    m.x82)**2 + (m.x97 - m.x124)**2) + 1 / sqrt((m.x13 - m.x41)**2 + (m.x55 -
    m.x83)**2 + (m.x97 - m.x125)**2) + 1 / sqrt((m.x13 - m.x42)**2 + (m.x55 -
    m.x84)**2 + (m.x97 - m.x126)**2) + 1 / sqrt((m.x14 - m.x15)**2 + (m.x56 -
    m.x57)**2 + (m.x98 - m.x99)**2) + 1 / sqrt((m.x14 - m.x16)**2 + (m.x56 -
    m.x58)**2 + (m.x98 - m.x100)**2) + 1 / sqrt((m.x14 - m.x17)**2 + (m.x56 -
    m.x59)**2 + (m.x98 - m.x101)**2) + 1 / sqrt((m.x14 - m.x18)**2 + (m.x56 -
    m.x60)**2 + (m.x98 - m.x102)**2) + 1 / sqrt((m.x14 - m.x19)**2 + (m.x56 -
    m.x61)**2 + (m.x98 - m.x103)**2) + 1 / sqrt((m.x14 - m.x20)**2 + (m.x56 -
    m.x62)**2 + (m.x98 - m.x104)**2) + 1 / sqrt((m.x14 - m.x21)**2 + (m.x56 -
    m.x63)**2 + (m.x98 - m.x105)**2) + 1 / sqrt((m.x14 - m.x22)**2 + (m.x56 -
    m.x64)**2 + (m.x98 - m.x106)**2) + 1 / sqrt((m.x14 - m.x23)**2 + (m.x56 -
    m.x65)**2 + (m.x98 - m.x107)**2) + 1 / sqrt((m.x14 - m.x24)**2 + (m.x56 -
    m.x66)**2 + (m.x98 - m.x108)**2) + 1 / sqrt((m.x14 - m.x25)**2 + (m.x56 -
    m.x67)**2 + (m.x98 - m.x109)**2) + 1 / sqrt((m.x14 - m.x26)**2 + (m.x56 -
    m.x68)**2 + (m.x98 - m.x110)**2) + 1 / sqrt((m.x14 - m.x27)**2 + (m.x56 -
    m.x69)**2 + (m.x98 - m.x111)**2) + 1 / sqrt((m.x14 - m.x28)**2 + (m.x56 -
    m.x70)**2 + (m.x98 - m.x112)**2) + 1 / sqrt((m.x14 - m.x29)**2 + (m.x56 -
    m.x71)**2 + (m.x98 - m.x113)**2) + 1 / sqrt((m.x14 - m.x30)**2 + (m.x56 -
    m.x72)**2 + (m.x98 - m.x114)**2) + 1 / sqrt((m.x14 - m.x31)**2 + (m.x56 -
    m.x73)**2 + (m.x98 - m.x115)**2) + 1 / sqrt((m.x14 - m.x32)**2 + (m.x56 -
    m.x74)**2 + (m.x98 - m.x116)**2) + 1 / sqrt((m.x14 - m.x33)**2 + (m.x56 -
    m.x75)**2 + (m.x98 - m.x117)**2) + 1 / sqrt((m.x14 - m.x34)**2 + (m.x56 -
    m.x76)**2 + (m.x98 - m.x118)**2) + 1 / sqrt((m.x14 - m.x35)**2 + (m.x56 -
    m.x77)**2 + (m.x98 - m.x119)**2) + 1 / sqrt((m.x14 - m.x36)**2 + (m.x56 -
    m.x78)**2 + (m.x98 - m.x120)**2) + 1 / sqrt((m.x14 - m.x37)**2 + (m.x56 -
    m.x79)**2 + (m.x98 - m.x121)**2) + 1 / sqrt((m.x14 - m.x38)**2 + (m.x56 -
    m.x80)**2 + (m.x98 - m.x122)**2) + 1 / sqrt((m.x14 - m.x39)**2 + (m.x56 -
    m.x81)**2 + (m.x98 - m.x123)**2) + 1 / sqrt((m.x14 - m.x40)**2 + (m.x56 -
    m.x82)**2 + (m.x98 - m.x124)**2) + 1 / sqrt((m.x14 - m.x41)**2 + (m.x56 -
    m.x83)**2 + (m.x98 - m.x125)**2) + 1 / sqrt((m.x14 - m.x42)**2 + (m.x56 -
    m.x84)**2 + (m.x98 - m.x126)**2) + 1 / sqrt((m.x15 - m.x16)**2 + (m.x57 -
    m.x58)**2 + (m.x99 - m.x100)**2) + 1 / sqrt((m.x15 - m.x17)**2 + (m.x57 -
    m.x59)**2 + (m.x99 - m.x101)**2) + 1 / sqrt((m.x15 - m.x18)**2 + (m.x57 -
    m.x60)**2 + (m.x99 - m.x102)**2) + 1 / sqrt((m.x15 - m.x19)**2 + (m.x57 -
    m.x61)**2 + (m.x99 - m.x103)**2) + 1 / sqrt((m.x15 - m.x20)**2 + (m.x57 -
    m.x62)**2 + (m.x99 - m.x104)**2) + 1 / sqrt((m.x15 - m.x21)**2 + (m.x57 -
    m.x63)**2 + (m.x99 - m.x105)**2) + 1 / sqrt((m.x15 - m.x22)**2 + (m.x57 -
    m.x64)**2 + (m.x99 - m.x106)**2) + 1 / sqrt((m.x15 - m.x23)**2 + (m.x57 -
    m.x65)**2 + (m.x99 - m.x107)**2) + 1 / sqrt((m.x15 - m.x24)**2 + (m.x57 -
    m.x66)**2 + (m.x99 - m.x108)**2) + 1 / sqrt((m.x15 - m.x25)**2 + (m.x57 -
    m.x67)**2 + (m.x99 - m.x109)**2) + 1 / sqrt((m.x15 - m.x26)**2 + (m.x57 -
    m.x68)**2 + (m.x99 - m.x110)**2) + 1 / sqrt((m.x15 - m.x27)**2 + (m.x57 -
    m.x69)**2 + (m.x99 - m.x111)**2) + 1 / sqrt((m.x15 - m.x28)**2 + (m.x57 -
    m.x70)**2 + (m.x99 - m.x112)**2) + 1 / sqrt((m.x15 - m.x29)**2 + (m.x57 -
    m.x71)**2 + (m.x99 - m.x113)**2) + 1 / sqrt((m.x15 - m.x30)**2 + (m.x57 -
    m.x72)**2 + (m.x99 - m.x114)**2) + 1 / sqrt((m.x15 - m.x31)**2 + (m.x57 -
    m.x73)**2 + (m.x99 - m.x115)**2) + 1 / sqrt((m.x15 - m.x32)**2 + (m.x57 -
    m.x74)**2 + (m.x99 - m.x116)**2) + 1 / sqrt((m.x15 - m.x33)**2 + (m.x57 -
    m.x75)**2 + (m.x99 - m.x117)**2) + 1 / sqrt((m.x15 - m.x34)**2 + (m.x57 -
    m.x76)**2 + (m.x99 - m.x118)**2) + 1 / sqrt((m.x15 - m.x35)**2 + (m.x57 -
    m.x77)**2 + (m.x99 - m.x119)**2) + 1 / sqrt((m.x15 - m.x36)**2 + (m.x57 -
    m.x78)**2 + (m.x99 - m.x120)**2) + 1 / sqrt((m.x15 - m.x37)**2 + (m.x57 -
    m.x79)**2 + (m.x99 - m.x121)**2) + 1 / sqrt((m.x15 - m.x38)**2 + (m.x57 -
    m.x80)**2 + (m.x99 - m.x122)**2) + 1 / sqrt((m.x15 - m.x39)**2 + (m.x57 -
    m.x81)**2 + (m.x99 - m.x123)**2) + 1 / sqrt((m.x15 - m.x40)**2 + (m.x57 -
    m.x82)**2 + (m.x99 - m.x124)**2) + 1 / sqrt((m.x15 - m.x41)**2 + (m.x57 -
    m.x83)**2 + (m.x99 - m.x125)**2) + 1 / sqrt((m.x15 - m.x42)**2 + (m.x57 -
    m.x84)**2 + (m.x99 - m.x126)**2) + 1 / sqrt((m.x16 - m.x17)**2 + (m.x58 -
    m.x59)**2 + (m.x100 - m.x101)**2) + 1 / sqrt((m.x16 - m.x18)**2 + (m.x58 -
    m.x60)**2 + (m.x100 - m.x102)**2) + 1 / sqrt((m.x16 - m.x19)**2 + (m.x58 -
    m.x61)**2 + (m.x100 - m.x103)**2) + 1 / sqrt((m.x16 - m.x20)**2 + (m.x58 -
    m.x62)**2 + (m.x100 - m.x104)**2) + 1 / sqrt((m.x16 - m.x21)**2 + (m.x58 -
    m.x63)**2 + (m.x100 - m.x105)**2) + 1 / sqrt((m.x16 - m.x22)**2 + (m.x58 -
    m.x64)**2 + (m.x100 - m.x106)**2) + 1 / sqrt((m.x16 - m.x23)**2 + (m.x58 -
    m.x65)**2 + (m.x100 - m.x107)**2) + 1 / sqrt((m.x16 - m.x24)**2 + (m.x58 -
    m.x66)**2 + (m.x100 - m.x108)**2) + 1 / sqrt((m.x16 - m.x25)**2 + (m.x58 -
    m.x67)**2 + (m.x100 - m.x109)**2) + 1 / sqrt((m.x16 - m.x26)**2 + (m.x58 -
    m.x68)**2 + (m.x100 - m.x110)**2) + 1 / sqrt((m.x16 - m.x27)**2 + (m.x58 -
    m.x69)**2 + (m.x100 - m.x111)**2) + 1 / sqrt((m.x16 - m.x28)**2 + (m.x58 -
    m.x70)**2 + (m.x100 - m.x112)**2) + 1 / sqrt((m.x16 - m.x29)**2 + (m.x58 -
    m.x71)**2 + (m.x100 - m.x113)**2) + 1 / sqrt((m.x16 - m.x30)**2 + (m.x58 -
    m.x72)**2 + (m.x100 - m.x114)**2) + 1 / sqrt((m.x16 - m.x31)**2 + (m.x58 -
    m.x73)**2 + (m.x100 - m.x115)**2) + 1 / sqrt((m.x16 - m.x32)**2 + (m.x58 -
    m.x74)**2 + (m.x100 - m.x116)**2) + 1 / sqrt((m.x16 - m.x33)**2 + (m.x58 -
    m.x75)**2 + (m.x100 - m.x117)**2) + 1 / sqrt((m.x16 - m.x34)**2 + (m.x58 -
    m.x76)**2 + (m.x100 - m.x118)**2) + 1 / sqrt((m.x16 - m.x35)**2 + (m.x58 -
    m.x77)**2 + (m.x100 - m.x119)**2) + 1 / sqrt((m.x16 - m.x36)**2 + (m.x58 -
    m.x78)**2 + (m.x100 - m.x120)**2) + 1 / sqrt((m.x16 - m.x37)**2 + (m.x58 -
    m.x79)**2 + (m.x100 - m.x121)**2) + 1 / sqrt((m.x16 - m.x38)**2 + (m.x58 -
    m.x80)**2 + (m.x100 - m.x122)**2) + 1 / sqrt((m.x16 - m.x39)**2 + (m.x58 -
    m.x81)**2 + (m.x100 - m.x123)**2) + 1 / sqrt((m.x16 - m.x40)**2 + (m.x58 -
    m.x82)**2 + (m.x100 - m.x124)**2) + 1 / sqrt((m.x16 - m.x41)**2 + (m.x58 -
    m.x83)**2 + (m.x100 - m.x125)**2) + 1 / sqrt((m.x16 - m.x42)**2 + (m.x58 -
    m.x84)**2 + (m.x100 - m.x126)**2) + 1 / sqrt((m.x17 - m.x18)**2 + (m.x59 -
    m.x60)**2 + (m.x101 - m.x102)**2) + 1 / sqrt((m.x17 - m.x19)**2 + (m.x59 -
    m.x61)**2 + (m.x101 - m.x103)**2) + 1 / sqrt((m.x17 - m.x20)**2 + (m.x59 -
    m.x62)**2 + (m.x101 - m.x104)**2) + 1 / sqrt((m.x17 - m.x21)**2 + (m.x59 -
    m.x63)**2 + (m.x101 - m.x105)**2) + 1 / sqrt((m.x17 - m.x22)**2 + (m.x59 -
    m.x64)**2 + (m.x101 - m.x106)**2) + 1 / sqrt((m.x17 - m.x23)**2 + (m.x59 -
    m.x65)**2 + (m.x101 - m.x107)**2) + 1 / sqrt((m.x17 - m.x24)**2 + (m.x59 -
    m.x66)**2 + (m.x101 - m.x108)**2) + 1 / sqrt((m.x17 - m.x25)**2 + (m.x59 -
    m.x67)**2 + (m.x101 - m.x109)**2) + 1 / sqrt((m.x17 - m.x26)**2 + (m.x59 -
    m.x68)**2 + (m.x101 - m.x110)**2) + 1 / sqrt((m.x17 - m.x27)**2 + (m.x59 -
    m.x69)**2 + (m.x101 - m.x111)**2) + 1 / sqrt((m.x17 - m.x28)**2 + (m.x59 -
    m.x70)**2 + (m.x101 - m.x112)**2) + 1 / sqrt((m.x17 - m.x29)**2 + (m.x59 -
    m.x71)**2 + (m.x101 - m.x113)**2) + 1 / sqrt((m.x17 - m.x30)**2 + (m.x59 -
    m.x72)**2 + (m.x101 - m.x114)**2) + 1 / sqrt((m.x17 - m.x31)**2 + (m.x59 -
    m.x73)**2 + (m.x101 - m.x115)**2) + 1 / sqrt((m.x17 - m.x32)**2 + (m.x59 -
    m.x74)**2 + (m.x101 - m.x116)**2) + 1 / sqrt((m.x17 - m.x33)**2 + (m.x59 -
    m.x75)**2 + (m.x101 - m.x117)**2) + 1 / sqrt((m.x17 - m.x34)**2 + (m.x59 -
    m.x76)**2 + (m.x101 - m.x118)**2) + 1 / sqrt((m.x17 - m.x35)**2 + (m.x59 -
    m.x77)**2 + (m.x101 - m.x119)**2) + 1 / sqrt((m.x17 - m.x36)**2 + (m.x59 -
    m.x78)**2 + (m.x101 - m.x120)**2) + 1 / sqrt((m.x17 - m.x37)**2 + (m.x59 -
    m.x79)**2 + (m.x101 - m.x121)**2) + 1 / sqrt((m.x17 - m.x38)**2 + (m.x59 -
    m.x80)**2 + (m.x101 - m.x122)**2) + 1 / sqrt((m.x17 - m.x39)**2 + (m.x59 -
    m.x81)**2 + (m.x101 - m.x123)**2) + 1 / sqrt((m.x17 - m.x40)**2 + (m.x59 -
    m.x82)**2 + (m.x101 - m.x124)**2) + 1 / sqrt((m.x17 - m.x41)**2 + (m.x59 -
    m.x83)**2 + (m.x101 - m.x125)**2) + 1 / sqrt((m.x17 - m.x42)**2 + (m.x59 -
    m.x84)**2 + (m.x101 - m.x126)**2) + 1 / sqrt((m.x18 - m.x19)**2 + (m.x60 -
    m.x61)**2 + (m.x102 - m.x103)**2) + 1 / sqrt((m.x18 - m.x20)**2 + (m.x60 -
    m.x62)**2 + (m.x102 - m.x104)**2) + 1 / sqrt((m.x18 - m.x21)**2 + (m.x60 -
    m.x63)**2 + (m.x102 - m.x105)**2) + 1 / sqrt((m.x18 - m.x22)**2 + (m.x60 -
    m.x64)**2 + (m.x102 - m.x106)**2) + 1 / sqrt((m.x18 - m.x23)**2 + (m.x60 -
    m.x65)**2 + (m.x102 - m.x107)**2) + 1 / sqrt((m.x18 - m.x24)**2 + (m.x60 -
    m.x66)**2 + (m.x102 - m.x108)**2) + 1 / sqrt((m.x18 - m.x25)**2 + (m.x60 -
    m.x67)**2 + (m.x102 - m.x109)**2) + 1 / sqrt((m.x18 - m.x26)**2 + (m.x60 -
    m.x68)**2 + (m.x102 - m.x110)**2) + 1 / sqrt((m.x18 - m.x27)**2 + (m.x60 -
    m.x69)**2 + (m.x102 - m.x111)**2) + 1 / sqrt((m.x18 - m.x28)**2 + (m.x60 -
    m.x70)**2 + (m.x102 - m.x112)**2) + 1 / sqrt((m.x18 - m.x29)**2 + (m.x60 -
    m.x71)**2 + (m.x102 - m.x113)**2) + 1 / sqrt((m.x18 - m.x30)**2 + (m.x60 -
    m.x72)**2 + (m.x102 - m.x114)**2) + 1 / sqrt((m.x18 - m.x31)**2 + (m.x60 -
    m.x73)**2 + (m.x102 - m.x115)**2) + 1 / sqrt((m.x18 - m.x32)**2 + (m.x60 -
    m.x74)**2 + (m.x102 - m.x116)**2) + 1 / sqrt((m.x18 - m.x33)**2 + (m.x60 -
    m.x75)**2 + (m.x102 - m.x117)**2) + 1 / sqrt((m.x18 - m.x34)**2 + (m.x60 -
    m.x76)**2 + (m.x102 - m.x118)**2) + 1 / sqrt((m.x18 - m.x35)**2 + (m.x60 -
    m.x77)**2 + (m.x102 - m.x119)**2) + 1 / sqrt((m.x18 - m.x36)**2 + (m.x60 -
    m.x78)**2 + (m.x102 - m.x120)**2) + 1 / sqrt((m.x18 - m.x37)**2 + (m.x60 -
    m.x79)**2 + (m.x102 - m.x121)**2) + 1 / sqrt((m.x18 - m.x38)**2 + (m.x60 -
    m.x80)**2 + (m.x102 - m.x122)**2) + 1 / sqrt((m.x18 - m.x39)**2 + (m.x60 -
    m.x81)**2 + (m.x102 - m.x123)**2) + 1 / sqrt((m.x18 - m.x40)**2 + (m.x60 -
    m.x82)**2 + (m.x102 - m.x124)**2) + 1 / sqrt((m.x18 - m.x41)**2 + (m.x60 -
    m.x83)**2 + (m.x102 - m.x125)**2) + 1 / sqrt((m.x18 - m.x42)**2 + (m.x60 -
    m.x84)**2 + (m.x102 - m.x126)**2) + 1 / sqrt((m.x19 - m.x20)**2 + (m.x61 -
    m.x62)**2 + (m.x103 - m.x104)**2) + 1 / sqrt((m.x19 - m.x21)**2 + (m.x61 -
    m.x63)**2 + (m.x103 - m.x105)**2) + 1 / sqrt((m.x19 - m.x22)**2 + (m.x61 -
    m.x64)**2 + (m.x103 - m.x106)**2) + 1 / sqrt((m.x19 - m.x23)**2 + (m.x61 -
    m.x65)**2 + (m.x103 - m.x107)**2) + 1 / sqrt((m.x19 - m.x24)**2 + (m.x61 -
    m.x66)**2 + (m.x103 - m.x108)**2) + 1 / sqrt((m.x19 - m.x25)**2 + (m.x61 -
    m.x67)**2 + (m.x103 - m.x109)**2) + 1 / sqrt((m.x19 - m.x26)**2 + (m.x61 -
    m.x68)**2 + (m.x103 - m.x110)**2) + 1 / sqrt((m.x19 - m.x27)**2 + (m.x61 -
    m.x69)**2 + (m.x103 - m.x111)**2) + 1 / sqrt((m.x19 - m.x28)**2 + (m.x61 -
    m.x70)**2 + (m.x103 - m.x112)**2) + 1 / sqrt((m.x19 - m.x29)**2 + (m.x61 -
    m.x71)**2 + (m.x103 - m.x113)**2) + 1 / sqrt((m.x19 - m.x30)**2 + (m.x61 -
    m.x72)**2 + (m.x103 - m.x114)**2) + 1 / sqrt((m.x19 - m.x31)**2 + (m.x61 -
    m.x73)**2 + (m.x103 - m.x115)**2) + 1 / sqrt((m.x19 - m.x32)**2 + (m.x61 -
    m.x74)**2 + (m.x103 - m.x116)**2) + 1 / sqrt((m.x19 - m.x33)**2 + (m.x61 -
    m.x75)**2 + (m.x103 - m.x117)**2) + 1 / sqrt((m.x19 - m.x34)**2 + (m.x61 -
    m.x76)**2 + (m.x103 - m.x118)**2) + 1 / sqrt((m.x19 - m.x35)**2 + (m.x61 -
    m.x77)**2 + (m.x103 - m.x119)**2) + 1 / sqrt((m.x19 - m.x36)**2 + (m.x61 -
    m.x78)**2 + (m.x103 - m.x120)**2) + 1 / sqrt((m.x19 - m.x37)**2 + (m.x61 -
    m.x79)**2 + (m.x103 - m.x121)**2) + 1 / sqrt((m.x19 - m.x38)**2 + (m.x61 -
    m.x80)**2 + (m.x103 - m.x122)**2) + 1 / sqrt((m.x19 - m.x39)**2 + (m.x61 -
    m.x81)**2 + (m.x103 - m.x123)**2) + 1 / sqrt((m.x19 - m.x40)**2 + (m.x61 -
    m.x82)**2 + (m.x103 - m.x124)**2) + 1 / sqrt((m.x19 - m.x41)**2 + (m.x61 -
    m.x83)**2 + (m.x103 - m.x125)**2) + 1 / sqrt((m.x19 - m.x42)**2 + (m.x61 -
    m.x84)**2 + (m.x103 - m.x126)**2) + 1 / sqrt((m.x20 - m.x21)**2 + (m.x62 -
    m.x63)**2 + (m.x104 - m.x105)**2) + 1 / sqrt((m.x20 - m.x22)**2 + (m.x62 -
    m.x64)**2 + (m.x104 - m.x106)**2) + 1 / sqrt((m.x20 - m.x23)**2 + (m.x62 -
    m.x65)**2 + (m.x104 - m.x107)**2) + 1 / sqrt((m.x20 - m.x24)**2 + (m.x62 -
    m.x66)**2 + (m.x104 - m.x108)**2) + 1 / sqrt((m.x20 - m.x25)**2 + (m.x62 -
    m.x67)**2 + (m.x104 - m.x109)**2) + 1 / sqrt((m.x20 - m.x26)**2 + (m.x62 -
    m.x68)**2 + (m.x104 - m.x110)**2) + 1 / sqrt((m.x20 - m.x27)**2 + (m.x62 -
    m.x69)**2 + (m.x104 - m.x111)**2) + 1 / sqrt((m.x20 - m.x28)**2 + (m.x62 -
    m.x70)**2 + (m.x104 - m.x112)**2) + 1 / sqrt((m.x20 - m.x29)**2 + (m.x62 -
    m.x71)**2 + (m.x104 - m.x113)**2) + 1 / sqrt((m.x20 - m.x30)**2 + (m.x62 -
    m.x72)**2 + (m.x104 - m.x114)**2) + 1 / sqrt((m.x20 - m.x31)**2 + (m.x62 -
    m.x73)**2 + (m.x104 - m.x115)**2) + 1 / sqrt((m.x20 - m.x32)**2 + (m.x62 -
    m.x74)**2 + (m.x104 - m.x116)**2) + 1 / sqrt((m.x20 - m.x33)**2 + (m.x62 -
    m.x75)**2 + (m.x104 - m.x117)**2) + 1 / sqrt((m.x20 - m.x34)**2 + (m.x62 -
    m.x76)**2 + (m.x104 - m.x118)**2) + 1 / sqrt((m.x20 - m.x35)**2 + (m.x62 -
    m.x77)**2 + (m.x104 - m.x119)**2) + 1 / sqrt((m.x20 - m.x36)**2 + (m.x62 -
    m.x78)**2 + (m.x104 - m.x120)**2) + 1 / sqrt((m.x20 - m.x37)**2 + (m.x62 -
    m.x79)**2 + (m.x104 - m.x121)**2) + 1 / sqrt((m.x20 - m.x38)**2 + (m.x62 -
    m.x80)**2 + (m.x104 - m.x122)**2) + 1 / sqrt((m.x20 - m.x39)**2 + (m.x62 -
    m.x81)**2 + (m.x104 - m.x123)**2) + 1 / sqrt((m.x20 - m.x40)**2 + (m.x62 -
    m.x82)**2 + (m.x104 - m.x124)**2) + 1 / sqrt((m.x20 - m.x41)**2 + (m.x62 -
    m.x83)**2 + (m.x104 - m.x125)**2) + 1 / sqrt((m.x20 - m.x42)**2 + (m.x62 -
    m.x84)**2 + (m.x104 - m.x126)**2) + 1 / sqrt((m.x21 - m.x22)**2 + (m.x63 -
    m.x64)**2 + (m.x105 - m.x106)**2) + 1 / sqrt((m.x21 - m.x23)**2 + (m.x63 -
    m.x65)**2 + (m.x105 - m.x107)**2) + 1 / sqrt((m.x21 - m.x24)**2 + (m.x63 -
    m.x66)**2 + (m.x105 - m.x108)**2) + 1 / sqrt((m.x21 - m.x25)**2 + (m.x63 -
    m.x67)**2 + (m.x105 - m.x109)**2) + 1 / sqrt((m.x21 - m.x26)**2 + (m.x63 -
    m.x68)**2 + (m.x105 - m.x110)**2) + 1 / sqrt((m.x21 - m.x27)**2 + (m.x63 -
    m.x69)**2 + (m.x105 - m.x111)**2) + 1 / sqrt((m.x21 - m.x28)**2 + (m.x63 -
    m.x70)**2 + (m.x105 - m.x112)**2) + 1 / sqrt((m.x21 - m.x29)**2 + (m.x63 -
    m.x71)**2 + (m.x105 - m.x113)**2) + 1 / sqrt((m.x21 - m.x30)**2 + (m.x63 -
    m.x72)**2 + (m.x105 - m.x114)**2) + 1 / sqrt((m.x21 - m.x31)**2 + (m.x63 -
    m.x73)**2 + (m.x105 - m.x115)**2) + 1 / sqrt((m.x21 - m.x32)**2 + (m.x63 -
    m.x74)**2 + (m.x105 - m.x116)**2) + 1 / sqrt((m.x21 - m.x33)**2 + (m.x63 -
    m.x75)**2 + (m.x105 - m.x117)**2) + 1 / sqrt((m.x21 - m.x34)**2 + (m.x63 -
    m.x76)**2 + (m.x105 - m.x118)**2) + 1 / sqrt((m.x21 - m.x35)**2 + (m.x63 -
    m.x77)**2 + (m.x105 - m.x119)**2) + 1 / sqrt((m.x21 - m.x36)**2 + (m.x63 -
    m.x78)**2 + (m.x105 - m.x120)**2) + 1 / sqrt((m.x21 - m.x37)**2 + (m.x63 -
    m.x79)**2 + (m.x105 - m.x121)**2) + 1 / sqrt((m.x21 - m.x38)**2 + (m.x63 -
    m.x80)**2 + (m.x105 - m.x122)**2) + 1 / sqrt((m.x21 - m.x39)**2 + (m.x63 -
    m.x81)**2 + (m.x105 - m.x123)**2) + 1 / sqrt((m.x21 - m.x40)**2 + (m.x63 -
    m.x82)**2 + (m.x105 - m.x124)**2) + 1 / sqrt((m.x21 - m.x41)**2 + (m.x63 -
    m.x83)**2 + (m.x105 - m.x125)**2) + 1 / sqrt((m.x21 - m.x42)**2 + (m.x63 -
    m.x84)**2 + (m.x105 - m.x126)**2) + 1 / sqrt((m.x22 - m.x23)**2 + (m.x64 -
    m.x65)**2 + (m.x106 - m.x107)**2) + 1 / sqrt((m.x22 - m.x24)**2 + (m.x64 -
    m.x66)**2 + (m.x106 - m.x108)**2) + 1 / sqrt((m.x22 - m.x25)**2 + (m.x64 -
    m.x67)**2 + (m.x106 - m.x109)**2) + 1 / sqrt((m.x22 - m.x26)**2 + (m.x64 -
    m.x68)**2 + (m.x106 - m.x110)**2) + 1 / sqrt((m.x22 - m.x27)**2 + (m.x64 -
    m.x69)**2 + (m.x106 - m.x111)**2) + 1 / sqrt((m.x22 - m.x28)**2 + (m.x64 -
    m.x70)**2 + (m.x106 - m.x112)**2) + 1 / sqrt((m.x22 - m.x29)**2 + (m.x64 -
    m.x71)**2 + (m.x106 - m.x113)**2) + 1 / sqrt((m.x22 - m.x30)**2 + (m.x64 -
    m.x72)**2 + (m.x106 - m.x114)**2) + 1 / sqrt((m.x22 - m.x31)**2 + (m.x64 -
    m.x73)**2 + (m.x106 - m.x115)**2) + 1 / sqrt((m.x22 - m.x32)**2 + (m.x64 -
    m.x74)**2 + (m.x106 - m.x116)**2) + 1 / sqrt((m.x22 - m.x33)**2 + (m.x64 -
    m.x75)**2 + (m.x106 - m.x117)**2) + 1 / sqrt((m.x22 - m.x34)**2 + (m.x64 -
    m.x76)**2 + (m.x106 - m.x118)**2) + 1 / sqrt((m.x22 - m.x35)**2 + (m.x64 -
    m.x77)**2 + (m.x106 - m.x119)**2) + 1 / sqrt((m.x22 - m.x36)**2 + (m.x64 -
    m.x78)**2 + (m.x106 - m.x120)**2) + 1 / sqrt((m.x22 - m.x37)**2 + (m.x64 -
    m.x79)**2 + (m.x106 - m.x121)**2) + 1 / sqrt((m.x22 - m.x38)**2 + (m.x64 -
    m.x80)**2 + (m.x106 - m.x122)**2) + 1 / sqrt((m.x22 - m.x39)**2 + (m.x64 -
    m.x81)**2 + (m.x106 - m.x123)**2) + 1 / sqrt((m.x22 - m.x40)**2 + (m.x64 -
    m.x82)**2 + (m.x106 - m.x124)**2) + 1 / sqrt((m.x22 - m.x41)**2 + (m.x64 -
    m.x83)**2 + (m.x106 - m.x125)**2) + 1 / sqrt((m.x22 - m.x42)**2 + (m.x64 -
    m.x84)**2 + (m.x106 - m.x126)**2) + 1 / sqrt((m.x23 - m.x24)**2 + (m.x65 -
    m.x66)**2 + (m.x107 - m.x108)**2) + 1 / sqrt((m.x23 - m.x25)**2 + (m.x65 -
    m.x67)**2 + (m.x107 - m.x109)**2) + 1 / sqrt((m.x23 - m.x26)**2 + (m.x65 -
    m.x68)**2 + (m.x107 - m.x110)**2) + 1 / sqrt((m.x23 - m.x27)**2 + (m.x65 -
    m.x69)**2 + (m.x107 - m.x111)**2) + 1 / sqrt((m.x23 - m.x28)**2 + (m.x65 -
    m.x70)**2 + (m.x107 - m.x112)**2) + 1 / sqrt((m.x23 - m.x29)**2 + (m.x65 -
    m.x71)**2 + (m.x107 - m.x113)**2) + 1 / sqrt((m.x23 - m.x30)**2 + (m.x65 -
    m.x72)**2 + (m.x107 - m.x114)**2) + 1 / sqrt((m.x23 - m.x31)**2 + (m.x65 -
    m.x73)**2 + (m.x107 - m.x115)**2) + 1 / sqrt((m.x23 - m.x32)**2 + (m.x65 -
    m.x74)**2 + (m.x107 - m.x116)**2) + 1 / sqrt((m.x23 - m.x33)**2 + (m.x65 -
    m.x75)**2 + (m.x107 - m.x117)**2) + 1 / sqrt((m.x23 - m.x34)**2 + (m.x65 -
    m.x76)**2 + (m.x107 - m.x118)**2) + 1 / sqrt((m.x23 - m.x35)**2 + (m.x65 -
    m.x77)**2 + (m.x107 - m.x119)**2) + 1 / sqrt((m.x23 - m.x36)**2 + (m.x65 -
    m.x78)**2 + (m.x107 - m.x120)**2) + 1 / sqrt((m.x23 - m.x37)**2 + (m.x65 -
    m.x79)**2 + (m.x107 - m.x121)**2) + 1 / sqrt((m.x23 - m.x38)**2 + (m.x65 -
    m.x80)**2 + (m.x107 - m.x122)**2) + 1 / sqrt((m.x23 - m.x39)**2 + (m.x65 -
    m.x81)**2 + (m.x107 - m.x123)**2) + 1 / sqrt((m.x23 - m.x40)**2 + (m.x65 -
    m.x82)**2 + (m.x107 - m.x124)**2) + 1 / sqrt((m.x23 - m.x41)**2 + (m.x65 -
    m.x83)**2 + (m.x107 - m.x125)**2) + 1 / sqrt((m.x23 - m.x42)**2 + (m.x65 -
    m.x84)**2 + (m.x107 - m.x126)**2) + 1 / sqrt((m.x24 - m.x25)**2 + (m.x66 -
    m.x67)**2 + (m.x108 - m.x109)**2) + 1 / sqrt((m.x24 - m.x26)**2 + (m.x66 -
    m.x68)**2 + (m.x108 - m.x110)**2) + 1 / sqrt((m.x24 - m.x27)**2 + (m.x66 -
    m.x69)**2 + (m.x108 - m.x111)**2) + 1 / sqrt((m.x24 - m.x28)**2 + (m.x66 -
    m.x70)**2 + (m.x108 - m.x112)**2) + 1 / sqrt((m.x24 - m.x29)**2 + (m.x66 -
    m.x71)**2 + (m.x108 - m.x113)**2) + 1 / sqrt((m.x24 - m.x30)**2 + (m.x66 -
    m.x72)**2 + (m.x108 - m.x114)**2) + 1 / sqrt((m.x24 - m.x31)**2 + (m.x66 -
    m.x73)**2 + (m.x108 - m.x115)**2) + 1 / sqrt((m.x24 - m.x32)**2 + (m.x66 -
    m.x74)**2 + (m.x108 - m.x116)**2) + 1 / sqrt((m.x24 - m.x33)**2 + (m.x66 -
    m.x75)**2 + (m.x108 - m.x117)**2) + 1 / sqrt((m.x24 - m.x34)**2 + (m.x66 -
    m.x76)**2 + (m.x108 - m.x118)**2) + 1 / sqrt((m.x24 - m.x35)**2 + (m.x66 -
    m.x77)**2 + (m.x108 - m.x119)**2) + 1 / sqrt((m.x24 - m.x36)**2 + (m.x66 -
    m.x78)**2 + (m.x108 - m.x120)**2) + 1 / sqrt((m.x24 - m.x37)**2 + (m.x66 -
    m.x79)**2 + (m.x108 - m.x121)**2) + 1 / sqrt((m.x24 - m.x38)**2 + (m.x66 -
    m.x80)**2 + (m.x108 - m.x122)**2) + 1 / sqrt((m.x24 - m.x39)**2 + (m.x66 -
    m.x81)**2 + (m.x108 - m.x123)**2) + 1 / sqrt((m.x24 - m.x40)**2 + (m.x66 -
    m.x82)**2 + (m.x108 - m.x124)**2) + 1 / sqrt((m.x24 - m.x41)**2 + (m.x66 -
    m.x83)**2 + (m.x108 - m.x125)**2) + 1 / sqrt((m.x24 - m.x42)**2 + (m.x66 -
    m.x84)**2 + (m.x108 - m.x126)**2) + 1 / sqrt((m.x25 - m.x26)**2 + (m.x67 -
    m.x68)**2 + (m.x109 - m.x110)**2) + 1 / sqrt((m.x25 - m.x27)**2 + (m.x67 -
    m.x69)**2 + (m.x109 - m.x111)**2) + 1 / sqrt((m.x25 - m.x28)**2 + (m.x67 -
    m.x70)**2 + (m.x109 - m.x112)**2) + 1 / sqrt((m.x25 - m.x29)**2 + (m.x67 -
    m.x71)**2 + (m.x109 - m.x113)**2) + 1 / sqrt((m.x25 - m.x30)**2 + (m.x67 -
    m.x72)**2 + (m.x109 - m.x114)**2) + 1 / sqrt((m.x25 - m.x31)**2 + (m.x67 -
    m.x73)**2 + (m.x109 - m.x115)**2) + 1 / sqrt((m.x25 - m.x32)**2 + (m.x67 -
    m.x74)**2 + (m.x109 - m.x116)**2) + 1 / sqrt((m.x25 - m.x33)**2 + (m.x67 -
    m.x75)**2 + (m.x109 - m.x117)**2) + 1 / sqrt((m.x25 - m.x34)**2 + (m.x67 -
    m.x76)**2 + (m.x109 - m.x118)**2) + 1 / sqrt((m.x25 - m.x35)**2 + (m.x67 -
    m.x77)**2 + (m.x109 - m.x119)**2) + 1 / sqrt((m.x25 - m.x36)**2 + (m.x67 -
    m.x78)**2 + (m.x109 - m.x120)**2) + 1 / sqrt((m.x25 - m.x37)**2 + (m.x67 -
    m.x79)**2 + (m.x109 - m.x121)**2) + 1 / sqrt((m.x25 - m.x38)**2 + (m.x67 -
    m.x80)**2 + (m.x109 - m.x122)**2) + 1 / sqrt((m.x25 - m.x39)**2 + (m.x67 -
    m.x81)**2 + (m.x109 - m.x123)**2) + 1 / sqrt((m.x25 - m.x40)**2 + (m.x67 -
    m.x82)**2 + (m.x109 - m.x124)**2) + 1 / sqrt((m.x25 - m.x41)**2 + (m.x67 -
    m.x83)**2 + (m.x109 - m.x125)**2) + 1 / sqrt((m.x25 - m.x42)**2 + (m.x67 -
    m.x84)**2 + (m.x109 - m.x126)**2) + 1 / sqrt((m.x26 - m.x27)**2 + (m.x68 -
    m.x69)**2 + (m.x110 - m.x111)**2) + 1 / sqrt((m.x26 - m.x28)**2 + (m.x68 -
    m.x70)**2 + (m.x110 - m.x112)**2) + 1 / sqrt((m.x26 - m.x29)**2 + (m.x68 -
    m.x71)**2 + (m.x110 - m.x113)**2) + 1 / sqrt((m.x26 - m.x30)**2 + (m.x68 -
    m.x72)**2 + (m.x110 - m.x114)**2) + 1 / sqrt((m.x26 - m.x31)**2 + (m.x68 -
    m.x73)**2 + (m.x110 - m.x115)**2) + 1 / sqrt((m.x26 - m.x32)**2 + (m.x68 -
    m.x74)**2 + (m.x110 - m.x116)**2) + 1 / sqrt((m.x26 - m.x33)**2 + (m.x68 -
    m.x75)**2 + (m.x110 - m.x117)**2) + 1 / sqrt((m.x26 - m.x34)**2 + (m.x68 -
    m.x76)**2 + (m.x110 - m.x118)**2) + 1 / sqrt((m.x26 - m.x35)**2 + (m.x68 -
    m.x77)**2 + (m.x110 - m.x119)**2) + 1 / sqrt((m.x26 - m.x36)**2 + (m.x68 -
    m.x78)**2 + (m.x110 - m.x120)**2) + 1 / sqrt((m.x26 - m.x37)**2 + (m.x68 -
    m.x79)**2 + (m.x110 - m.x121)**2) + 1 / sqrt((m.x26 - m.x38)**2 + (m.x68 -
    m.x80)**2 + (m.x110 - m.x122)**2) + 1 / sqrt((m.x26 - m.x39)**2 + (m.x68 -
    m.x81)**2 + (m.x110 - m.x123)**2) + 1 / sqrt((m.x26 - m.x40)**2 + (m.x68 -
    m.x82)**2 + (m.x110 - m.x124)**2) + 1 / sqrt((m.x26 - m.x41)**2 + (m.x68 -
    m.x83)**2 + (m.x110 - m.x125)**2) + 1 / sqrt((m.x26 - m.x42)**2 + (m.x68 -
    m.x84)**2 + (m.x110 - m.x126)**2) + 1 / sqrt((m.x27 - m.x28)**2 + (m.x69 -
    m.x70)**2 + (m.x111 - m.x112)**2) + 1 / sqrt((m.x27 - m.x29)**2 + (m.x69 -
    m.x71)**2 + (m.x111 - m.x113)**2) + 1 / sqrt((m.x27 - m.x30)**2 + (m.x69 -
    m.x72)**2 + (m.x111 - m.x114)**2) + 1 / sqrt((m.x27 - m.x31)**2 + (m.x69 -
    m.x73)**2 + (m.x111 - m.x115)**2) + 1 / sqrt((m.x27 - m.x32)**2 + (m.x69 -
    m.x74)**2 + (m.x111 - m.x116)**2) + 1 / sqrt((m.x27 - m.x33)**2 + (m.x69 -
    m.x75)**2 + (m.x111 - m.x117)**2) + 1 / sqrt((m.x27 - m.x34)**2 + (m.x69 -
    m.x76)**2 + (m.x111 - m.x118)**2) + 1 / sqrt((m.x27 - m.x35)**2 + (m.x69 -
    m.x77)**2 + (m.x111 - m.x119)**2) + 1 / sqrt((m.x27 - m.x36)**2 + (m.x69 -
    m.x78)**2 + (m.x111 - m.x120)**2) + 1 / sqrt((m.x27 - m.x37)**2 + (m.x69 -
    m.x79)**2 + (m.x111 - m.x121)**2) + 1 / sqrt((m.x27 - m.x38)**2 + (m.x69 -
    m.x80)**2 + (m.x111 - m.x122)**2) + 1 / sqrt((m.x27 - m.x39)**2 + (m.x69 -
    m.x81)**2 + (m.x111 - m.x123)**2) + 1 / sqrt((m.x27 - m.x40)**2 + (m.x69 -
    m.x82)**2 + (m.x111 - m.x124)**2) + 1 / sqrt((m.x27 - m.x41)**2 + (m.x69 -
    m.x83)**2 + (m.x111 - m.x125)**2) + 1 / sqrt((m.x27 - m.x42)**2 + (m.x69 -
    m.x84)**2 + (m.x111 - m.x126)**2) + 1 / sqrt((m.x28 - m.x29)**2 + (m.x70 -
    m.x71)**2 + (m.x112 - m.x113)**2) + 1 / sqrt((m.x28 - m.x30)**2 + (m.x70 -
    m.x72)**2 + (m.x112 - m.x114)**2) + 1 / sqrt((m.x28 - m.x31)**2 + (m.x70 -
    m.x73)**2 + (m.x112 - m.x115)**2) + 1 / sqrt((m.x28 - m.x32)**2 + (m.x70 -
    m.x74)**2 + (m.x112 - m.x116)**2) + 1 / sqrt((m.x28 - m.x33)**2 + (m.x70 -
    m.x75)**2 + (m.x112 - m.x117)**2) + 1 / sqrt((m.x28 - m.x34)**2 + (m.x70 -
    m.x76)**2 + (m.x112 - m.x118)**2) + 1 / sqrt((m.x28 - m.x35)**2 + (m.x70 -
    m.x77)**2 + (m.x112 - m.x119)**2) + 1 / sqrt((m.x28 - m.x36)**2 + (m.x70 -
    m.x78)**2 + (m.x112 - m.x120)**2) + 1 / sqrt((m.x28 - m.x37)**2 + (m.x70 -
    m.x79)**2 + (m.x112 - m.x121)**2) + 1 / sqrt((m.x28 - m.x38)**2 + (m.x70 -
    m.x80)**2 + (m.x112 - m.x122)**2) + 1 / sqrt((m.x28 - m.x39)**2 + (m.x70 -
    m.x81)**2 + (m.x112 - m.x123)**2) + 1 / sqrt((m.x28 - m.x40)**2 + (m.x70 -
    m.x82)**2 + (m.x112 - m.x124)**2) + 1 / sqrt((m.x28 - m.x41)**2 + (m.x70 -
    m.x83)**2 + (m.x112 - m.x125)**2) + 1 / sqrt((m.x28 - m.x42)**2 + (m.x70 -
    m.x84)**2 + (m.x112 - m.x126)**2) + 1 / sqrt((m.x29 - m.x30)**2 + (m.x71 -
    m.x72)**2 + (m.x113 - m.x114)**2) + 1 / sqrt((m.x29 - m.x31)**2 + (m.x71 -
    m.x73)**2 + (m.x113 - m.x115)**2) + 1 / sqrt((m.x29 - m.x32)**2 + (m.x71 -
    m.x74)**2 + (m.x113 - m.x116)**2) + 1 / sqrt((m.x29 - m.x33)**2 + (m.x71 -
    m.x75)**2 + (m.x113 - m.x117)**2) + 1 / sqrt((m.x29 - m.x34)**2 + (m.x71 -
    m.x76)**2 + (m.x113 - m.x118)**2) + 1 / sqrt((m.x29 - m.x35)**2 + (m.x71 -
    m.x77)**2 + (m.x113 - m.x119)**2) + 1 / sqrt((m.x29 - m.x36)**2 + (m.x71 -
    m.x78)**2 + (m.x113 - m.x120)**2) + 1 / sqrt((m.x29 - m.x37)**2 + (m.x71 -
    m.x79)**2 + (m.x113 - m.x121)**2) + 1 / sqrt((m.x29 - m.x38)**2 + (m.x71 -
    m.x80)**2 + (m.x113 - m.x122)**2) + 1 / sqrt((m.x29 - m.x39)**2 + (m.x71 -
    m.x81)**2 + (m.x113 - m.x123)**2) + 1 / sqrt((m.x29 - m.x40)**2 + (m.x71 -
    m.x82)**2 + (m.x113 - m.x124)**2) + 1 / sqrt((m.x29 - m.x41)**2 + (m.x71 -
    m.x83)**2 + (m.x113 - m.x125)**2) + 1 / sqrt((m.x29 - m.x42)**2 + (m.x71 -
    m.x84)**2 + (m.x113 - m.x126)**2) + 1 / sqrt((m.x30 - m.x31)**2 + (m.x72 -
    m.x73)**2 + (m.x114 - m.x115)**2) + 1 / sqrt((m.x30 - m.x32)**2 + (m.x72 -
    m.x74)**2 + (m.x114 - m.x116)**2) + 1 / sqrt((m.x30 - m.x33)**2 + (m.x72 -
    m.x75)**2 + (m.x114 - m.x117)**2) + 1 / sqrt((m.x30 - m.x34)**2 + (m.x72 -
    m.x76)**2 + (m.x114 - m.x118)**2) + 1 / sqrt((m.x30 - m.x35)**2 + (m.x72 -
    m.x77)**2 + (m.x114 - m.x119)**2) + 1 / sqrt((m.x30 - m.x36)**2 + (m.x72 -
    m.x78)**2 + (m.x114 - m.x120)**2) + 1 / sqrt((m.x30 - m.x37)**2 + (m.x72 -
    m.x79)**2 + (m.x114 - m.x121)**2) + 1 / sqrt((m.x30 - m.x38)**2 + (m.x72 -
    m.x80)**2 + (m.x114 - m.x122)**2) + 1 / sqrt((m.x30 - m.x39)**2 + (m.x72 -
    m.x81)**2 + (m.x114 - m.x123)**2) + 1 / sqrt((m.x30 - m.x40)**2 + (m.x72 -
    m.x82)**2 + (m.x114 - m.x124)**2) + 1 / sqrt((m.x30 - m.x41)**2 + (m.x72 -
    m.x83)**2 + (m.x114 - m.x125)**2) + 1 / sqrt((m.x30 - m.x42)**2 + (m.x72 -
    m.x84)**2 + (m.x114 - m.x126)**2) + 1 / sqrt((m.x31 - m.x32)**2 + (m.x73 -
    m.x74)**2 + (m.x115 - m.x116)**2) + 1 / sqrt((m.x31 - m.x33)**2 + (m.x73 -
    m.x75)**2 + (m.x115 - m.x117)**2) + 1 / sqrt((m.x31 - m.x34)**2 + (m.x73 -
    m.x76)**2 + (m.x115 - m.x118)**2) + 1 / sqrt((m.x31 - m.x35)**2 + (m.x73 -
    m.x77)**2 + (m.x115 - m.x119)**2) + 1 / sqrt((m.x31 - m.x36)**2 + (m.x73 -
    m.x78)**2 + (m.x115 - m.x120)**2) + 1 / sqrt((m.x31 - m.x37)**2 + (m.x73 -
    m.x79)**2 + (m.x115 - m.x121)**2) + 1 / sqrt((m.x31 - m.x38)**2 + (m.x73 -
    m.x80)**2 + (m.x115 - m.x122)**2) + 1 / sqrt((m.x31 - m.x39)**2 + (m.x73 -
    m.x81)**2 + (m.x115 - m.x123)**2) + 1 / sqrt((m.x31 - m.x40)**2 + (m.x73 -
    m.x82)**2 + (m.x115 - m.x124)**2) + 1 / sqrt((m.x31 - m.x41)**2 + (m.x73 -
    m.x83)**2 + (m.x115 - m.x125)**2) + 1 / sqrt((m.x31 - m.x42)**2 + (m.x73 -
    m.x84)**2 + (m.x115 - m.x126)**2) + 1 / sqrt((m.x32 - m.x33)**2 + (m.x74 -
    m.x75)**2 + (m.x116 - m.x117)**2) + 1 / sqrt((m.x32 - m.x34)**2 + (m.x74 -
    m.x76)**2 + (m.x116 - m.x118)**2) + 1 / sqrt((m.x32 - m.x35)**2 + (m.x74 -
    m.x77)**2 + (m.x116 - m.x119)**2) + 1 / sqrt((m.x32 - m.x36)**2 + (m.x74 -
    m.x78)**2 + (m.x116 - m.x120)**2) + 1 / sqrt((m.x32 - m.x37)**2 + (m.x74 -
    m.x79)**2 + (m.x116 - m.x121)**2) + 1 / sqrt((m.x32 - m.x38)**2 + (m.x74 -
    m.x80)**2 + (m.x116 - m.x122)**2) + 1 / sqrt((m.x32 - m.x39)**2 + (m.x74 -
    m.x81)**2 + (m.x116 - m.x123)**2) + 1 / sqrt((m.x32 - m.x40)**2 + (m.x74 -
    m.x82)**2 + (m.x116 - m.x124)**2) + 1 / sqrt((m.x32 - m.x41)**2 + (m.x74 -
    m.x83)**2 + (m.x116 - m.x125)**2) + 1 / sqrt((m.x32 - m.x42)**2 + (m.x74 -
    m.x84)**2 + (m.x116 - m.x126)**2) + 1 / sqrt((m.x33 - m.x34)**2 + (m.x75 -
    m.x76)**2 + (m.x117 - m.x118)**2) + 1 / sqrt((m.x33 - m.x35)**2 + (m.x75 -
    m.x77)**2 + (m.x117 - m.x119)**2) + 1 / sqrt((m.x33 - m.x36)**2 + (m.x75 -
    m.x78)**2 + (m.x117 - m.x120)**2) + 1 / sqrt((m.x33 - m.x37)**2 + (m.x75 -
    m.x79)**2 + (m.x117 - m.x121)**2) + 1 / sqrt((m.x33 - m.x38)**2 + (m.x75 -
    m.x80)**2 + (m.x117 - m.x122)**2) + 1 / sqrt((m.x33 - m.x39)**2 + (m.x75 -
    m.x81)**2 + (m.x117 - m.x123)**2) + 1 / sqrt((m.x33 - m.x40)**2 + (m.x75 -
    m.x82)**2 + (m.x117 - m.x124)**2) + 1 / sqrt((m.x33 - m.x41)**2 + (m.x75 -
    m.x83)**2 + (m.x117 - m.x125)**2) + 1 / sqrt((m.x33 - m.x42)**2 + (m.x75 -
    m.x84)**2 + (m.x117 - m.x126)**2) + 1 / sqrt((m.x34 - m.x35)**2 + (m.x76 -
    m.x77)**2 + (m.x118 - m.x119)**2) + 1 / sqrt((m.x34 - m.x36)**2 + (m.x76 -
    m.x78)**2 + (m.x118 - m.x120)**2) + 1 / sqrt((m.x34 - m.x37)**2 + (m.x76 -
    m.x79)**2 + (m.x118 - m.x121)**2) + 1 / sqrt((m.x34 - m.x38)**2 + (m.x76 -
    m.x80)**2 + (m.x118 - m.x122)**2) + 1 / sqrt((m.x34 - m.x39)**2 + (m.x76 -
    m.x81)**2 + (m.x118 - m.x123)**2) + 1 / sqrt((m.x34 - m.x40)**2 + (m.x76 -
    m.x82)**2 + (m.x118 - m.x124)**2) + 1 / sqrt((m.x34 - m.x41)**2 + (m.x76 -
    m.x83)**2 + (m.x118 - m.x125)**2) + 1 / sqrt((m.x34 - m.x42)**2 + (m.x76 -
    m.x84)**2 + (m.x118 - m.x126)**2) + 1 / sqrt((m.x35 - m.x36)**2 + (m.x77 -
    m.x78)**2 + (m.x119 - m.x120)**2) + 1 / sqrt((m.x35 - m.x37)**2 + (m.x77 -
    m.x79)**2 + (m.x119 - m.x121)**2) + 1 / sqrt((m.x35 - m.x38)**2 + (m.x77 -
    m.x80)**2 + (m.x119 - m.x122)**2) + 1 / sqrt((m.x35 - m.x39)**2 + (m.x77 -
    m.x81)**2 + (m.x119 - m.x123)**2) + 1 / sqrt((m.x35 - m.x40)**2 + (m.x77 -
    m.x82)**2 + (m.x119 - m.x124)**2) + 1 / sqrt((m.x35 - m.x41)**2 + (m.x77 -
    m.x83)**2 + (m.x119 - m.x125)**2) + 1 / sqrt((m.x35 - m.x42)**2 + (m.x77 -
    m.x84)**2 + (m.x119 - m.x126)**2) + 1 / sqrt((m.x36 - m.x37)**2 + (m.x78 -
    m.x79)**2 + (m.x120 - m.x121)**2) + 1 / sqrt((m.x36 - m.x38)**2 + (m.x78 -
    m.x80)**2 + (m.x120 - m.x122)**2) + 1 / sqrt((m.x36 - m.x39)**2 + (m.x78 -
    m.x81)**2 + (m.x120 - m.x123)**2) + 1 / sqrt((m.x36 - m.x40)**2 + (m.x78 -
    m.x82)**2 + (m.x120 - m.x124)**2) + 1 / sqrt((m.x36 - m.x41)**2 + (m.x78 -
    m.x83)**2 + (m.x120 - m.x125)**2) + 1 / sqrt((m.x36 - m.x42)**2 + (m.x78 -
    m.x84)**2 + (m.x120 - m.x126)**2) + 1 / sqrt((m.x37 - m.x38)**2 + (m.x79 -
    m.x80)**2 + (m.x121 - m.x122)**2) + 1 / sqrt((m.x37 - m.x39)**2 + (m.x79 -
    m.x81)**2 + (m.x121 - m.x123)**2) + 1 / sqrt((m.x37 - m.x40)**2 + (m.x79 -
    m.x82)**2 + (m.x121 - m.x124)**2) + 1 / sqrt((m.x37 - m.x41)**2 + (m.x79 -
    m.x83)**2 + (m.x121 - m.x125)**2) + 1 / sqrt((m.x37 - m.x42)**2 + (m.x79 -
    m.x84)**2 + (m.x121 - m.x126)**2) + 1 / sqrt((m.x38 - m.x39)**2 + (m.x80 -
    m.x81)**2 + (m.x122 - m.x123)**2) + 1 / sqrt((m.x38 - m.x40)**2 + (m.x80 -
    m.x82)**2 + (m.x122 - m.x124)**2) + 1 / sqrt((m.x38 - m.x41)**2 + (m.x80 -
    m.x83)**2 + (m.x122 - m.x125)**2) + 1 / sqrt((m.x38 - m.x42)**2 + (m.x80 -
    m.x84)**2 + (m.x122 - m.x126)**2) + 1 / sqrt((m.x39 - m.x40)**2 + (m.x81 -
    m.x82)**2 + (m.x123 - m.x124)**2) + 1 / sqrt((m.x39 - m.x41)**2 + (m.x81 -
    m.x83)**2 + (m.x123 - m.x125)**2) + 1 / sqrt((m.x39 - m.x42)**2 + (m.x81 -
    m.x84)**2 + (m.x123 - m.x126)**2) + 1 / sqrt((m.x40 - m.x41)**2 + (m.x82 -
    m.x83)**2 + (m.x124 - m.x125)**2) + 1 / sqrt((m.x40 - m.x42)**2 + (m.x82 -
    m.x84)**2 + (m.x124 - m.x126)**2) + 1 / sqrt((m.x41 - m.x42)**2 + (m.x83 -
    m.x84)**2 + (m.x125 - m.x126)**2))

m.e1 = Constraint(expr= m.x1**2 + m.x43**2 + m.x85**2 == 1)
m.e2 = Constraint(expr= m.x2**2 + m.x44**2 + m.x86**2 == 1)
m.e3 = Constraint(expr= m.x3**2 + m.x45**2 + m.x87**2 == 1)
m.e4 = Constraint(expr= m.x4**2 + m.x46**2 + m.x88**2 == 1)
m.e5 = Constraint(expr= m.x5**2 + m.x47**2 + m.x89**2 == 1)
m.e6 = Constraint(expr= m.x6**2 + m.x48**2 + m.x90**2 == 1)
m.e7 = Constraint(expr= m.x7**2 + m.x49**2 + m.x91**2 == 1)
m.e8 = Constraint(expr= m.x8**2 + m.x50**2 + m.x92**2 == 1)
m.e9 = Constraint(expr= m.x9**2 + m.x51**2 + m.x93**2 == 1)
m.e10 = Constraint(expr= m.x10**2 + m.x52**2 + m.x94**2 == 1)
m.e11 = Constraint(expr= m.x11**2 + m.x53**2 + m.x95**2 == 1)
m.e12 = Constraint(expr= m.x12**2 + m.x54**2 + m.x96**2 == 1)
m.e13 = Constraint(expr= m.x13**2 + m.x55**2 + m.x97**2 == 1)
m.e14 = Constraint(expr= m.x14**2 + m.x56**2 + m.x98**2 == 1)
m.e15 = Constraint(expr= m.x15**2 + m.x57**2 + m.x99**2 == 1)
m.e16 = Constraint(expr= m.x16**2 + m.x58**2 + m.x100**2 == 1)
m.e17 = Constraint(expr= m.x17**2 + m.x59**2 + m.x101**2 == 1)
m.e18 = Constraint(expr= m.x18**2 + m.x60**2 + m.x102**2 == 1)
m.e19 = Constraint(expr= m.x19**2 + m.x61**2 + m.x103**2 == 1)
m.e20 = Constraint(expr= m.x20**2 + m.x62**2 + m.x104**2 == 1)
m.e21 = Constraint(expr= m.x21**2 + m.x63**2 + m.x105**2 == 1)
m.e22 = Constraint(expr= m.x22**2 + m.x64**2 + m.x106**2 == 1)
m.e23 = Constraint(expr= m.x23**2 + m.x65**2 + m.x107**2 == 1)
m.e24 = Constraint(expr= m.x24**2 + m.x66**2 + m.x108**2 == 1)
m.e25 = Constraint(expr= m.x25**2 + m.x67**2 + m.x109**2 == 1)
m.e26 = Constraint(expr= m.x26**2 + m.x68**2 + m.x110**2 == 1)
m.e27 = Constraint(expr= m.x27**2 + m.x69**2 + m.x111**2 == 1)
m.e28 = Constraint(expr= m.x28**2 + m.x70**2 + m.x112**2 == 1)
m.e29 = Constraint(expr= m.x29**2 + m.x71**2 + m.x113**2 == 1)
m.e30 = Constraint(expr= m.x30**2 + m.x72**2 + m.x114**2 == 1)
m.e31 = Constraint(expr= m.x31**2 + m.x73**2 + m.x115**2 == 1)
m.e32 = Constraint(expr= m.x32**2 + m.x74**2 + m.x116**2 == 1)
m.e33 = Constraint(expr= m.x33**2 + m.x75**2 + m.x117**2 == 1)
m.e34 = Constraint(expr= m.x34**2 + m.x76**2 + m.x118**2 == 1)
m.e35 = Constraint(expr= m.x35**2 + m.x77**2 + m.x119**2 == 1)
m.e36 = Constraint(expr= m.x36**2 + m.x78**2 + m.x120**2 == 1)
m.e37 = Constraint(expr= m.x37**2 + m.x79**2 + m.x121**2 == 1)
m.e38 = Constraint(expr= m.x38**2 + m.x80**2 + m.x122**2 == 1)
m.e39 = Constraint(expr= m.x39**2 + m.x81**2 + m.x123**2 == 1)
m.e40 = Constraint(expr= m.x40**2 + m.x82**2 + m.x124**2 == 1)
m.e41 = Constraint(expr= m.x41**2 + m.x83**2 + m.x125**2 == 1)
m.e42 = Constraint(expr= m.x42**2 + m.x84**2 + m.x126**2 == 1)
