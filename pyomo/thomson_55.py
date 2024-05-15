# NLP written by GAMS Convert at 05/15/24 11:41:30
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#        55       55        0        0        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#       165      165        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       165        0      165
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
m.x127 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x128 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x129 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x130 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x131 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x132 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x133 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x134 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x135 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x136 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x137 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x138 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x139 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x140 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x141 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x142 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x143 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x144 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x145 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x146 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x147 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x148 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x149 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x150 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x151 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x152 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x153 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x154 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x155 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x156 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x157 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x158 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x159 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x160 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x161 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x162 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x163 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x164 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x165 = Var(within=Reals, bounds=(-1,1), initialize=0)

m.obj = Objective(sense=minimize, expr= 1 / sqrt((m.x1 - m.x2)**2 + (m.x56 -
    m.x57)**2 + (m.x111 - m.x112)**2) + 1 / sqrt((m.x1 - m.x3)**2 + (m.x56 -
    m.x58)**2 + (m.x111 - m.x113)**2) + 1 / sqrt((m.x1 - m.x4)**2 + (m.x56 -
    m.x59)**2 + (m.x111 - m.x114)**2) + 1 / sqrt((m.x1 - m.x5)**2 + (m.x56 -
    m.x60)**2 + (m.x111 - m.x115)**2) + 1 / sqrt((m.x1 - m.x6)**2 + (m.x56 -
    m.x61)**2 + (m.x111 - m.x116)**2) + 1 / sqrt((m.x1 - m.x7)**2 + (m.x56 -
    m.x62)**2 + (m.x111 - m.x117)**2) + 1 / sqrt((m.x1 - m.x8)**2 + (m.x56 -
    m.x63)**2 + (m.x111 - m.x118)**2) + 1 / sqrt((m.x1 - m.x9)**2 + (m.x56 -
    m.x64)**2 + (m.x111 - m.x119)**2) + 1 / sqrt((m.x1 - m.x10)**2 + (m.x56 -
    m.x65)**2 + (m.x111 - m.x120)**2) + 1 / sqrt((m.x1 - m.x11)**2 + (m.x56 -
    m.x66)**2 + (m.x111 - m.x121)**2) + 1 / sqrt((m.x1 - m.x12)**2 + (m.x56 -
    m.x67)**2 + (m.x111 - m.x122)**2) + 1 / sqrt((m.x1 - m.x13)**2 + (m.x56 -
    m.x68)**2 + (m.x111 - m.x123)**2) + 1 / sqrt((m.x1 - m.x14)**2 + (m.x56 -
    m.x69)**2 + (m.x111 - m.x124)**2) + 1 / sqrt((m.x1 - m.x15)**2 + (m.x56 -
    m.x70)**2 + (m.x111 - m.x125)**2) + 1 / sqrt((m.x1 - m.x16)**2 + (m.x56 -
    m.x71)**2 + (m.x111 - m.x126)**2) + 1 / sqrt((m.x1 - m.x17)**2 + (m.x56 -
    m.x72)**2 + (m.x111 - m.x127)**2) + 1 / sqrt((m.x1 - m.x18)**2 + (m.x56 -
    m.x73)**2 + (m.x111 - m.x128)**2) + 1 / sqrt((m.x1 - m.x19)**2 + (m.x56 -
    m.x74)**2 + (m.x111 - m.x129)**2) + 1 / sqrt((m.x1 - m.x20)**2 + (m.x56 -
    m.x75)**2 + (m.x111 - m.x130)**2) + 1 / sqrt((m.x1 - m.x21)**2 + (m.x56 -
    m.x76)**2 + (m.x111 - m.x131)**2) + 1 / sqrt((m.x1 - m.x22)**2 + (m.x56 -
    m.x77)**2 + (m.x111 - m.x132)**2) + 1 / sqrt((m.x1 - m.x23)**2 + (m.x56 -
    m.x78)**2 + (m.x111 - m.x133)**2) + 1 / sqrt((m.x1 - m.x24)**2 + (m.x56 -
    m.x79)**2 + (m.x111 - m.x134)**2) + 1 / sqrt((m.x1 - m.x25)**2 + (m.x56 -
    m.x80)**2 + (m.x111 - m.x135)**2) + 1 / sqrt((m.x1 - m.x26)**2 + (m.x56 -
    m.x81)**2 + (m.x111 - m.x136)**2) + 1 / sqrt((m.x1 - m.x27)**2 + (m.x56 -
    m.x82)**2 + (m.x111 - m.x137)**2) + 1 / sqrt((m.x1 - m.x28)**2 + (m.x56 -
    m.x83)**2 + (m.x111 - m.x138)**2) + 1 / sqrt((m.x1 - m.x29)**2 + (m.x56 -
    m.x84)**2 + (m.x111 - m.x139)**2) + 1 / sqrt((m.x1 - m.x30)**2 + (m.x56 -
    m.x85)**2 + (m.x111 - m.x140)**2) + 1 / sqrt((m.x1 - m.x31)**2 + (m.x56 -
    m.x86)**2 + (m.x111 - m.x141)**2) + 1 / sqrt((m.x1 - m.x32)**2 + (m.x56 -
    m.x87)**2 + (m.x111 - m.x142)**2) + 1 / sqrt((m.x1 - m.x33)**2 + (m.x56 -
    m.x88)**2 + (m.x111 - m.x143)**2) + 1 / sqrt((m.x1 - m.x34)**2 + (m.x56 -
    m.x89)**2 + (m.x111 - m.x144)**2) + 1 / sqrt((m.x1 - m.x35)**2 + (m.x56 -
    m.x90)**2 + (m.x111 - m.x145)**2) + 1 / sqrt((m.x1 - m.x36)**2 + (m.x56 -
    m.x91)**2 + (m.x111 - m.x146)**2) + 1 / sqrt((m.x1 - m.x37)**2 + (m.x56 -
    m.x92)**2 + (m.x111 - m.x147)**2) + 1 / sqrt((m.x1 - m.x38)**2 + (m.x56 -
    m.x93)**2 + (m.x111 - m.x148)**2) + 1 / sqrt((m.x1 - m.x39)**2 + (m.x56 -
    m.x94)**2 + (m.x111 - m.x149)**2) + 1 / sqrt((m.x1 - m.x40)**2 + (m.x56 -
    m.x95)**2 + (m.x111 - m.x150)**2) + 1 / sqrt((m.x1 - m.x41)**2 + (m.x56 -
    m.x96)**2 + (m.x111 - m.x151)**2) + 1 / sqrt((m.x1 - m.x42)**2 + (m.x56 -
    m.x97)**2 + (m.x111 - m.x152)**2) + 1 / sqrt((m.x1 - m.x43)**2 + (m.x56 -
    m.x98)**2 + (m.x111 - m.x153)**2) + 1 / sqrt((m.x1 - m.x44)**2 + (m.x56 -
    m.x99)**2 + (m.x111 - m.x154)**2) + 1 / sqrt((m.x1 - m.x45)**2 + (m.x56 -
    m.x100)**2 + (m.x111 - m.x155)**2) + 1 / sqrt((m.x1 - m.x46)**2 + (m.x56 -
    m.x101)**2 + (m.x111 - m.x156)**2) + 1 / sqrt((m.x1 - m.x47)**2 + (m.x56 -
    m.x102)**2 + (m.x111 - m.x157)**2) + 1 / sqrt((m.x1 - m.x48)**2 + (m.x56 -
    m.x103)**2 + (m.x111 - m.x158)**2) + 1 / sqrt((m.x1 - m.x49)**2 + (m.x56 -
    m.x104)**2 + (m.x111 - m.x159)**2) + 1 / sqrt((m.x1 - m.x50)**2 + (m.x56 -
    m.x105)**2 + (m.x111 - m.x160)**2) + 1 / sqrt((m.x1 - m.x51)**2 + (m.x56 -
    m.x106)**2 + (m.x111 - m.x161)**2) + 1 / sqrt((m.x1 - m.x52)**2 + (m.x56 -
    m.x107)**2 + (m.x111 - m.x162)**2) + 1 / sqrt((m.x1 - m.x53)**2 + (m.x56 -
    m.x108)**2 + (m.x111 - m.x163)**2) + 1 / sqrt((m.x1 - m.x54)**2 + (m.x56 -
    m.x109)**2 + (m.x111 - m.x164)**2) + 1 / sqrt((m.x1 - m.x55)**2 + (m.x56 -
    m.x110)**2 + (m.x111 - m.x165)**2) + 1 / sqrt((m.x2 - m.x3)**2 + (m.x57 -
    m.x58)**2 + (m.x112 - m.x113)**2) + 1 / sqrt((m.x2 - m.x4)**2 + (m.x57 -
    m.x59)**2 + (m.x112 - m.x114)**2) + 1 / sqrt((m.x2 - m.x5)**2 + (m.x57 -
    m.x60)**2 + (m.x112 - m.x115)**2) + 1 / sqrt((m.x2 - m.x6)**2 + (m.x57 -
    m.x61)**2 + (m.x112 - m.x116)**2) + 1 / sqrt((m.x2 - m.x7)**2 + (m.x57 -
    m.x62)**2 + (m.x112 - m.x117)**2) + 1 / sqrt((m.x2 - m.x8)**2 + (m.x57 -
    m.x63)**2 + (m.x112 - m.x118)**2) + 1 / sqrt((m.x2 - m.x9)**2 + (m.x57 -
    m.x64)**2 + (m.x112 - m.x119)**2) + 1 / sqrt((m.x2 - m.x10)**2 + (m.x57 -
    m.x65)**2 + (m.x112 - m.x120)**2) + 1 / sqrt((m.x2 - m.x11)**2 + (m.x57 -
    m.x66)**2 + (m.x112 - m.x121)**2) + 1 / sqrt((m.x2 - m.x12)**2 + (m.x57 -
    m.x67)**2 + (m.x112 - m.x122)**2) + 1 / sqrt((m.x2 - m.x13)**2 + (m.x57 -
    m.x68)**2 + (m.x112 - m.x123)**2) + 1 / sqrt((m.x2 - m.x14)**2 + (m.x57 -
    m.x69)**2 + (m.x112 - m.x124)**2) + 1 / sqrt((m.x2 - m.x15)**2 + (m.x57 -
    m.x70)**2 + (m.x112 - m.x125)**2) + 1 / sqrt((m.x2 - m.x16)**2 + (m.x57 -
    m.x71)**2 + (m.x112 - m.x126)**2) + 1 / sqrt((m.x2 - m.x17)**2 + (m.x57 -
    m.x72)**2 + (m.x112 - m.x127)**2) + 1 / sqrt((m.x2 - m.x18)**2 + (m.x57 -
    m.x73)**2 + (m.x112 - m.x128)**2) + 1 / sqrt((m.x2 - m.x19)**2 + (m.x57 -
    m.x74)**2 + (m.x112 - m.x129)**2) + 1 / sqrt((m.x2 - m.x20)**2 + (m.x57 -
    m.x75)**2 + (m.x112 - m.x130)**2) + 1 / sqrt((m.x2 - m.x21)**2 + (m.x57 -
    m.x76)**2 + (m.x112 - m.x131)**2) + 1 / sqrt((m.x2 - m.x22)**2 + (m.x57 -
    m.x77)**2 + (m.x112 - m.x132)**2) + 1 / sqrt((m.x2 - m.x23)**2 + (m.x57 -
    m.x78)**2 + (m.x112 - m.x133)**2) + 1 / sqrt((m.x2 - m.x24)**2 + (m.x57 -
    m.x79)**2 + (m.x112 - m.x134)**2) + 1 / sqrt((m.x2 - m.x25)**2 + (m.x57 -
    m.x80)**2 + (m.x112 - m.x135)**2) + 1 / sqrt((m.x2 - m.x26)**2 + (m.x57 -
    m.x81)**2 + (m.x112 - m.x136)**2) + 1 / sqrt((m.x2 - m.x27)**2 + (m.x57 -
    m.x82)**2 + (m.x112 - m.x137)**2) + 1 / sqrt((m.x2 - m.x28)**2 + (m.x57 -
    m.x83)**2 + (m.x112 - m.x138)**2) + 1 / sqrt((m.x2 - m.x29)**2 + (m.x57 -
    m.x84)**2 + (m.x112 - m.x139)**2) + 1 / sqrt((m.x2 - m.x30)**2 + (m.x57 -
    m.x85)**2 + (m.x112 - m.x140)**2) + 1 / sqrt((m.x2 - m.x31)**2 + (m.x57 -
    m.x86)**2 + (m.x112 - m.x141)**2) + 1 / sqrt((m.x2 - m.x32)**2 + (m.x57 -
    m.x87)**2 + (m.x112 - m.x142)**2) + 1 / sqrt((m.x2 - m.x33)**2 + (m.x57 -
    m.x88)**2 + (m.x112 - m.x143)**2) + 1 / sqrt((m.x2 - m.x34)**2 + (m.x57 -
    m.x89)**2 + (m.x112 - m.x144)**2) + 1 / sqrt((m.x2 - m.x35)**2 + (m.x57 -
    m.x90)**2 + (m.x112 - m.x145)**2) + 1 / sqrt((m.x2 - m.x36)**2 + (m.x57 -
    m.x91)**2 + (m.x112 - m.x146)**2) + 1 / sqrt((m.x2 - m.x37)**2 + (m.x57 -
    m.x92)**2 + (m.x112 - m.x147)**2) + 1 / sqrt((m.x2 - m.x38)**2 + (m.x57 -
    m.x93)**2 + (m.x112 - m.x148)**2) + 1 / sqrt((m.x2 - m.x39)**2 + (m.x57 -
    m.x94)**2 + (m.x112 - m.x149)**2) + 1 / sqrt((m.x2 - m.x40)**2 + (m.x57 -
    m.x95)**2 + (m.x112 - m.x150)**2) + 1 / sqrt((m.x2 - m.x41)**2 + (m.x57 -
    m.x96)**2 + (m.x112 - m.x151)**2) + 1 / sqrt((m.x2 - m.x42)**2 + (m.x57 -
    m.x97)**2 + (m.x112 - m.x152)**2) + 1 / sqrt((m.x2 - m.x43)**2 + (m.x57 -
    m.x98)**2 + (m.x112 - m.x153)**2) + 1 / sqrt((m.x2 - m.x44)**2 + (m.x57 -
    m.x99)**2 + (m.x112 - m.x154)**2) + 1 / sqrt((m.x2 - m.x45)**2 + (m.x57 -
    m.x100)**2 + (m.x112 - m.x155)**2) + 1 / sqrt((m.x2 - m.x46)**2 + (m.x57 -
    m.x101)**2 + (m.x112 - m.x156)**2) + 1 / sqrt((m.x2 - m.x47)**2 + (m.x57 -
    m.x102)**2 + (m.x112 - m.x157)**2) + 1 / sqrt((m.x2 - m.x48)**2 + (m.x57 -
    m.x103)**2 + (m.x112 - m.x158)**2) + 1 / sqrt((m.x2 - m.x49)**2 + (m.x57 -
    m.x104)**2 + (m.x112 - m.x159)**2) + 1 / sqrt((m.x2 - m.x50)**2 + (m.x57 -
    m.x105)**2 + (m.x112 - m.x160)**2) + 1 / sqrt((m.x2 - m.x51)**2 + (m.x57 -
    m.x106)**2 + (m.x112 - m.x161)**2) + 1 / sqrt((m.x2 - m.x52)**2 + (m.x57 -
    m.x107)**2 + (m.x112 - m.x162)**2) + 1 / sqrt((m.x2 - m.x53)**2 + (m.x57 -
    m.x108)**2 + (m.x112 - m.x163)**2) + 1 / sqrt((m.x2 - m.x54)**2 + (m.x57 -
    m.x109)**2 + (m.x112 - m.x164)**2) + 1 / sqrt((m.x2 - m.x55)**2 + (m.x57 -
    m.x110)**2 + (m.x112 - m.x165)**2) + 1 / sqrt((m.x3 - m.x4)**2 + (m.x58 -
    m.x59)**2 + (m.x113 - m.x114)**2) + 1 / sqrt((m.x3 - m.x5)**2 + (m.x58 -
    m.x60)**2 + (m.x113 - m.x115)**2) + 1 / sqrt((m.x3 - m.x6)**2 + (m.x58 -
    m.x61)**2 + (m.x113 - m.x116)**2) + 1 / sqrt((m.x3 - m.x7)**2 + (m.x58 -
    m.x62)**2 + (m.x113 - m.x117)**2) + 1 / sqrt((m.x3 - m.x8)**2 + (m.x58 -
    m.x63)**2 + (m.x113 - m.x118)**2) + 1 / sqrt((m.x3 - m.x9)**2 + (m.x58 -
    m.x64)**2 + (m.x113 - m.x119)**2) + 1 / sqrt((m.x3 - m.x10)**2 + (m.x58 -
    m.x65)**2 + (m.x113 - m.x120)**2) + 1 / sqrt((m.x3 - m.x11)**2 + (m.x58 -
    m.x66)**2 + (m.x113 - m.x121)**2) + 1 / sqrt((m.x3 - m.x12)**2 + (m.x58 -
    m.x67)**2 + (m.x113 - m.x122)**2) + 1 / sqrt((m.x3 - m.x13)**2 + (m.x58 -
    m.x68)**2 + (m.x113 - m.x123)**2) + 1 / sqrt((m.x3 - m.x14)**2 + (m.x58 -
    m.x69)**2 + (m.x113 - m.x124)**2) + 1 / sqrt((m.x3 - m.x15)**2 + (m.x58 -
    m.x70)**2 + (m.x113 - m.x125)**2) + 1 / sqrt((m.x3 - m.x16)**2 + (m.x58 -
    m.x71)**2 + (m.x113 - m.x126)**2) + 1 / sqrt((m.x3 - m.x17)**2 + (m.x58 -
    m.x72)**2 + (m.x113 - m.x127)**2) + 1 / sqrt((m.x3 - m.x18)**2 + (m.x58 -
    m.x73)**2 + (m.x113 - m.x128)**2) + 1 / sqrt((m.x3 - m.x19)**2 + (m.x58 -
    m.x74)**2 + (m.x113 - m.x129)**2) + 1 / sqrt((m.x3 - m.x20)**2 + (m.x58 -
    m.x75)**2 + (m.x113 - m.x130)**2) + 1 / sqrt((m.x3 - m.x21)**2 + (m.x58 -
    m.x76)**2 + (m.x113 - m.x131)**2) + 1 / sqrt((m.x3 - m.x22)**2 + (m.x58 -
    m.x77)**2 + (m.x113 - m.x132)**2) + 1 / sqrt((m.x3 - m.x23)**2 + (m.x58 -
    m.x78)**2 + (m.x113 - m.x133)**2) + 1 / sqrt((m.x3 - m.x24)**2 + (m.x58 -
    m.x79)**2 + (m.x113 - m.x134)**2) + 1 / sqrt((m.x3 - m.x25)**2 + (m.x58 -
    m.x80)**2 + (m.x113 - m.x135)**2) + 1 / sqrt((m.x3 - m.x26)**2 + (m.x58 -
    m.x81)**2 + (m.x113 - m.x136)**2) + 1 / sqrt((m.x3 - m.x27)**2 + (m.x58 -
    m.x82)**2 + (m.x113 - m.x137)**2) + 1 / sqrt((m.x3 - m.x28)**2 + (m.x58 -
    m.x83)**2 + (m.x113 - m.x138)**2) + 1 / sqrt((m.x3 - m.x29)**2 + (m.x58 -
    m.x84)**2 + (m.x113 - m.x139)**2) + 1 / sqrt((m.x3 - m.x30)**2 + (m.x58 -
    m.x85)**2 + (m.x113 - m.x140)**2) + 1 / sqrt((m.x3 - m.x31)**2 + (m.x58 -
    m.x86)**2 + (m.x113 - m.x141)**2) + 1 / sqrt((m.x3 - m.x32)**2 + (m.x58 -
    m.x87)**2 + (m.x113 - m.x142)**2) + 1 / sqrt((m.x3 - m.x33)**2 + (m.x58 -
    m.x88)**2 + (m.x113 - m.x143)**2) + 1 / sqrt((m.x3 - m.x34)**2 + (m.x58 -
    m.x89)**2 + (m.x113 - m.x144)**2) + 1 / sqrt((m.x3 - m.x35)**2 + (m.x58 -
    m.x90)**2 + (m.x113 - m.x145)**2) + 1 / sqrt((m.x3 - m.x36)**2 + (m.x58 -
    m.x91)**2 + (m.x113 - m.x146)**2) + 1 / sqrt((m.x3 - m.x37)**2 + (m.x58 -
    m.x92)**2 + (m.x113 - m.x147)**2) + 1 / sqrt((m.x3 - m.x38)**2 + (m.x58 -
    m.x93)**2 + (m.x113 - m.x148)**2) + 1 / sqrt((m.x3 - m.x39)**2 + (m.x58 -
    m.x94)**2 + (m.x113 - m.x149)**2) + 1 / sqrt((m.x3 - m.x40)**2 + (m.x58 -
    m.x95)**2 + (m.x113 - m.x150)**2) + 1 / sqrt((m.x3 - m.x41)**2 + (m.x58 -
    m.x96)**2 + (m.x113 - m.x151)**2) + 1 / sqrt((m.x3 - m.x42)**2 + (m.x58 -
    m.x97)**2 + (m.x113 - m.x152)**2) + 1 / sqrt((m.x3 - m.x43)**2 + (m.x58 -
    m.x98)**2 + (m.x113 - m.x153)**2) + 1 / sqrt((m.x3 - m.x44)**2 + (m.x58 -
    m.x99)**2 + (m.x113 - m.x154)**2) + 1 / sqrt((m.x3 - m.x45)**2 + (m.x58 -
    m.x100)**2 + (m.x113 - m.x155)**2) + 1 / sqrt((m.x3 - m.x46)**2 + (m.x58 -
    m.x101)**2 + (m.x113 - m.x156)**2) + 1 / sqrt((m.x3 - m.x47)**2 + (m.x58 -
    m.x102)**2 + (m.x113 - m.x157)**2) + 1 / sqrt((m.x3 - m.x48)**2 + (m.x58 -
    m.x103)**2 + (m.x113 - m.x158)**2) + 1 / sqrt((m.x3 - m.x49)**2 + (m.x58 -
    m.x104)**2 + (m.x113 - m.x159)**2) + 1 / sqrt((m.x3 - m.x50)**2 + (m.x58 -
    m.x105)**2 + (m.x113 - m.x160)**2) + 1 / sqrt((m.x3 - m.x51)**2 + (m.x58 -
    m.x106)**2 + (m.x113 - m.x161)**2) + 1 / sqrt((m.x3 - m.x52)**2 + (m.x58 -
    m.x107)**2 + (m.x113 - m.x162)**2) + 1 / sqrt((m.x3 - m.x53)**2 + (m.x58 -
    m.x108)**2 + (m.x113 - m.x163)**2) + 1 / sqrt((m.x3 - m.x54)**2 + (m.x58 -
    m.x109)**2 + (m.x113 - m.x164)**2) + 1 / sqrt((m.x3 - m.x55)**2 + (m.x58 -
    m.x110)**2 + (m.x113 - m.x165)**2) + 1 / sqrt((m.x4 - m.x5)**2 + (m.x59 -
    m.x60)**2 + (m.x114 - m.x115)**2) + 1 / sqrt((m.x4 - m.x6)**2 + (m.x59 -
    m.x61)**2 + (m.x114 - m.x116)**2) + 1 / sqrt((m.x4 - m.x7)**2 + (m.x59 -
    m.x62)**2 + (m.x114 - m.x117)**2) + 1 / sqrt((m.x4 - m.x8)**2 + (m.x59 -
    m.x63)**2 + (m.x114 - m.x118)**2) + 1 / sqrt((m.x4 - m.x9)**2 + (m.x59 -
    m.x64)**2 + (m.x114 - m.x119)**2) + 1 / sqrt((m.x4 - m.x10)**2 + (m.x59 -
    m.x65)**2 + (m.x114 - m.x120)**2) + 1 / sqrt((m.x4 - m.x11)**2 + (m.x59 -
    m.x66)**2 + (m.x114 - m.x121)**2) + 1 / sqrt((m.x4 - m.x12)**2 + (m.x59 -
    m.x67)**2 + (m.x114 - m.x122)**2) + 1 / sqrt((m.x4 - m.x13)**2 + (m.x59 -
    m.x68)**2 + (m.x114 - m.x123)**2) + 1 / sqrt((m.x4 - m.x14)**2 + (m.x59 -
    m.x69)**2 + (m.x114 - m.x124)**2) + 1 / sqrt((m.x4 - m.x15)**2 + (m.x59 -
    m.x70)**2 + (m.x114 - m.x125)**2) + 1 / sqrt((m.x4 - m.x16)**2 + (m.x59 -
    m.x71)**2 + (m.x114 - m.x126)**2) + 1 / sqrt((m.x4 - m.x17)**2 + (m.x59 -
    m.x72)**2 + (m.x114 - m.x127)**2) + 1 / sqrt((m.x4 - m.x18)**2 + (m.x59 -
    m.x73)**2 + (m.x114 - m.x128)**2) + 1 / sqrt((m.x4 - m.x19)**2 + (m.x59 -
    m.x74)**2 + (m.x114 - m.x129)**2) + 1 / sqrt((m.x4 - m.x20)**2 + (m.x59 -
    m.x75)**2 + (m.x114 - m.x130)**2) + 1 / sqrt((m.x4 - m.x21)**2 + (m.x59 -
    m.x76)**2 + (m.x114 - m.x131)**2) + 1 / sqrt((m.x4 - m.x22)**2 + (m.x59 -
    m.x77)**2 + (m.x114 - m.x132)**2) + 1 / sqrt((m.x4 - m.x23)**2 + (m.x59 -
    m.x78)**2 + (m.x114 - m.x133)**2) + 1 / sqrt((m.x4 - m.x24)**2 + (m.x59 -
    m.x79)**2 + (m.x114 - m.x134)**2) + 1 / sqrt((m.x4 - m.x25)**2 + (m.x59 -
    m.x80)**2 + (m.x114 - m.x135)**2) + 1 / sqrt((m.x4 - m.x26)**2 + (m.x59 -
    m.x81)**2 + (m.x114 - m.x136)**2) + 1 / sqrt((m.x4 - m.x27)**2 + (m.x59 -
    m.x82)**2 + (m.x114 - m.x137)**2) + 1 / sqrt((m.x4 - m.x28)**2 + (m.x59 -
    m.x83)**2 + (m.x114 - m.x138)**2) + 1 / sqrt((m.x4 - m.x29)**2 + (m.x59 -
    m.x84)**2 + (m.x114 - m.x139)**2) + 1 / sqrt((m.x4 - m.x30)**2 + (m.x59 -
    m.x85)**2 + (m.x114 - m.x140)**2) + 1 / sqrt((m.x4 - m.x31)**2 + (m.x59 -
    m.x86)**2 + (m.x114 - m.x141)**2) + 1 / sqrt((m.x4 - m.x32)**2 + (m.x59 -
    m.x87)**2 + (m.x114 - m.x142)**2) + 1 / sqrt((m.x4 - m.x33)**2 + (m.x59 -
    m.x88)**2 + (m.x114 - m.x143)**2) + 1 / sqrt((m.x4 - m.x34)**2 + (m.x59 -
    m.x89)**2 + (m.x114 - m.x144)**2) + 1 / sqrt((m.x4 - m.x35)**2 + (m.x59 -
    m.x90)**2 + (m.x114 - m.x145)**2) + 1 / sqrt((m.x4 - m.x36)**2 + (m.x59 -
    m.x91)**2 + (m.x114 - m.x146)**2) + 1 / sqrt((m.x4 - m.x37)**2 + (m.x59 -
    m.x92)**2 + (m.x114 - m.x147)**2) + 1 / sqrt((m.x4 - m.x38)**2 + (m.x59 -
    m.x93)**2 + (m.x114 - m.x148)**2) + 1 / sqrt((m.x4 - m.x39)**2 + (m.x59 -
    m.x94)**2 + (m.x114 - m.x149)**2) + 1 / sqrt((m.x4 - m.x40)**2 + (m.x59 -
    m.x95)**2 + (m.x114 - m.x150)**2) + 1 / sqrt((m.x4 - m.x41)**2 + (m.x59 -
    m.x96)**2 + (m.x114 - m.x151)**2) + 1 / sqrt((m.x4 - m.x42)**2 + (m.x59 -
    m.x97)**2 + (m.x114 - m.x152)**2) + 1 / sqrt((m.x4 - m.x43)**2 + (m.x59 -
    m.x98)**2 + (m.x114 - m.x153)**2) + 1 / sqrt((m.x4 - m.x44)**2 + (m.x59 -
    m.x99)**2 + (m.x114 - m.x154)**2) + 1 / sqrt((m.x4 - m.x45)**2 + (m.x59 -
    m.x100)**2 + (m.x114 - m.x155)**2) + 1 / sqrt((m.x4 - m.x46)**2 + (m.x59 -
    m.x101)**2 + (m.x114 - m.x156)**2) + 1 / sqrt((m.x4 - m.x47)**2 + (m.x59 -
    m.x102)**2 + (m.x114 - m.x157)**2) + 1 / sqrt((m.x4 - m.x48)**2 + (m.x59 -
    m.x103)**2 + (m.x114 - m.x158)**2) + 1 / sqrt((m.x4 - m.x49)**2 + (m.x59 -
    m.x104)**2 + (m.x114 - m.x159)**2) + 1 / sqrt((m.x4 - m.x50)**2 + (m.x59 -
    m.x105)**2 + (m.x114 - m.x160)**2) + 1 / sqrt((m.x4 - m.x51)**2 + (m.x59 -
    m.x106)**2 + (m.x114 - m.x161)**2) + 1 / sqrt((m.x4 - m.x52)**2 + (m.x59 -
    m.x107)**2 + (m.x114 - m.x162)**2) + 1 / sqrt((m.x4 - m.x53)**2 + (m.x59 -
    m.x108)**2 + (m.x114 - m.x163)**2) + 1 / sqrt((m.x4 - m.x54)**2 + (m.x59 -
    m.x109)**2 + (m.x114 - m.x164)**2) + 1 / sqrt((m.x4 - m.x55)**2 + (m.x59 -
    m.x110)**2 + (m.x114 - m.x165)**2) + 1 / sqrt((m.x5 - m.x6)**2 + (m.x60 -
    m.x61)**2 + (m.x115 - m.x116)**2) + 1 / sqrt((m.x5 - m.x7)**2 + (m.x60 -
    m.x62)**2 + (m.x115 - m.x117)**2) + 1 / sqrt((m.x5 - m.x8)**2 + (m.x60 -
    m.x63)**2 + (m.x115 - m.x118)**2) + 1 / sqrt((m.x5 - m.x9)**2 + (m.x60 -
    m.x64)**2 + (m.x115 - m.x119)**2) + 1 / sqrt((m.x5 - m.x10)**2 + (m.x60 -
    m.x65)**2 + (m.x115 - m.x120)**2) + 1 / sqrt((m.x5 - m.x11)**2 + (m.x60 -
    m.x66)**2 + (m.x115 - m.x121)**2) + 1 / sqrt((m.x5 - m.x12)**2 + (m.x60 -
    m.x67)**2 + (m.x115 - m.x122)**2) + 1 / sqrt((m.x5 - m.x13)**2 + (m.x60 -
    m.x68)**2 + (m.x115 - m.x123)**2) + 1 / sqrt((m.x5 - m.x14)**2 + (m.x60 -
    m.x69)**2 + (m.x115 - m.x124)**2) + 1 / sqrt((m.x5 - m.x15)**2 + (m.x60 -
    m.x70)**2 + (m.x115 - m.x125)**2) + 1 / sqrt((m.x5 - m.x16)**2 + (m.x60 -
    m.x71)**2 + (m.x115 - m.x126)**2) + 1 / sqrt((m.x5 - m.x17)**2 + (m.x60 -
    m.x72)**2 + (m.x115 - m.x127)**2) + 1 / sqrt((m.x5 - m.x18)**2 + (m.x60 -
    m.x73)**2 + (m.x115 - m.x128)**2) + 1 / sqrt((m.x5 - m.x19)**2 + (m.x60 -
    m.x74)**2 + (m.x115 - m.x129)**2) + 1 / sqrt((m.x5 - m.x20)**2 + (m.x60 -
    m.x75)**2 + (m.x115 - m.x130)**2) + 1 / sqrt((m.x5 - m.x21)**2 + (m.x60 -
    m.x76)**2 + (m.x115 - m.x131)**2) + 1 / sqrt((m.x5 - m.x22)**2 + (m.x60 -
    m.x77)**2 + (m.x115 - m.x132)**2) + 1 / sqrt((m.x5 - m.x23)**2 + (m.x60 -
    m.x78)**2 + (m.x115 - m.x133)**2) + 1 / sqrt((m.x5 - m.x24)**2 + (m.x60 -
    m.x79)**2 + (m.x115 - m.x134)**2) + 1 / sqrt((m.x5 - m.x25)**2 + (m.x60 -
    m.x80)**2 + (m.x115 - m.x135)**2) + 1 / sqrt((m.x5 - m.x26)**2 + (m.x60 -
    m.x81)**2 + (m.x115 - m.x136)**2) + 1 / sqrt((m.x5 - m.x27)**2 + (m.x60 -
    m.x82)**2 + (m.x115 - m.x137)**2) + 1 / sqrt((m.x5 - m.x28)**2 + (m.x60 -
    m.x83)**2 + (m.x115 - m.x138)**2) + 1 / sqrt((m.x5 - m.x29)**2 + (m.x60 -
    m.x84)**2 + (m.x115 - m.x139)**2) + 1 / sqrt((m.x5 - m.x30)**2 + (m.x60 -
    m.x85)**2 + (m.x115 - m.x140)**2) + 1 / sqrt((m.x5 - m.x31)**2 + (m.x60 -
    m.x86)**2 + (m.x115 - m.x141)**2) + 1 / sqrt((m.x5 - m.x32)**2 + (m.x60 -
    m.x87)**2 + (m.x115 - m.x142)**2) + 1 / sqrt((m.x5 - m.x33)**2 + (m.x60 -
    m.x88)**2 + (m.x115 - m.x143)**2) + 1 / sqrt((m.x5 - m.x34)**2 + (m.x60 -
    m.x89)**2 + (m.x115 - m.x144)**2) + 1 / sqrt((m.x5 - m.x35)**2 + (m.x60 -
    m.x90)**2 + (m.x115 - m.x145)**2) + 1 / sqrt((m.x5 - m.x36)**2 + (m.x60 -
    m.x91)**2 + (m.x115 - m.x146)**2) + 1 / sqrt((m.x5 - m.x37)**2 + (m.x60 -
    m.x92)**2 + (m.x115 - m.x147)**2) + 1 / sqrt((m.x5 - m.x38)**2 + (m.x60 -
    m.x93)**2 + (m.x115 - m.x148)**2) + 1 / sqrt((m.x5 - m.x39)**2 + (m.x60 -
    m.x94)**2 + (m.x115 - m.x149)**2) + 1 / sqrt((m.x5 - m.x40)**2 + (m.x60 -
    m.x95)**2 + (m.x115 - m.x150)**2) + 1 / sqrt((m.x5 - m.x41)**2 + (m.x60 -
    m.x96)**2 + (m.x115 - m.x151)**2) + 1 / sqrt((m.x5 - m.x42)**2 + (m.x60 -
    m.x97)**2 + (m.x115 - m.x152)**2) + 1 / sqrt((m.x5 - m.x43)**2 + (m.x60 -
    m.x98)**2 + (m.x115 - m.x153)**2) + 1 / sqrt((m.x5 - m.x44)**2 + (m.x60 -
    m.x99)**2 + (m.x115 - m.x154)**2) + 1 / sqrt((m.x5 - m.x45)**2 + (m.x60 -
    m.x100)**2 + (m.x115 - m.x155)**2) + 1 / sqrt((m.x5 - m.x46)**2 + (m.x60 -
    m.x101)**2 + (m.x115 - m.x156)**2) + 1 / sqrt((m.x5 - m.x47)**2 + (m.x60 -
    m.x102)**2 + (m.x115 - m.x157)**2) + 1 / sqrt((m.x5 - m.x48)**2 + (m.x60 -
    m.x103)**2 + (m.x115 - m.x158)**2) + 1 / sqrt((m.x5 - m.x49)**2 + (m.x60 -
    m.x104)**2 + (m.x115 - m.x159)**2) + 1 / sqrt((m.x5 - m.x50)**2 + (m.x60 -
    m.x105)**2 + (m.x115 - m.x160)**2) + 1 / sqrt((m.x5 - m.x51)**2 + (m.x60 -
    m.x106)**2 + (m.x115 - m.x161)**2) + 1 / sqrt((m.x5 - m.x52)**2 + (m.x60 -
    m.x107)**2 + (m.x115 - m.x162)**2) + 1 / sqrt((m.x5 - m.x53)**2 + (m.x60 -
    m.x108)**2 + (m.x115 - m.x163)**2) + 1 / sqrt((m.x5 - m.x54)**2 + (m.x60 -
    m.x109)**2 + (m.x115 - m.x164)**2) + 1 / sqrt((m.x5 - m.x55)**2 + (m.x60 -
    m.x110)**2 + (m.x115 - m.x165)**2) + 1 / sqrt((m.x6 - m.x7)**2 + (m.x61 -
    m.x62)**2 + (m.x116 - m.x117)**2) + 1 / sqrt((m.x6 - m.x8)**2 + (m.x61 -
    m.x63)**2 + (m.x116 - m.x118)**2) + 1 / sqrt((m.x6 - m.x9)**2 + (m.x61 -
    m.x64)**2 + (m.x116 - m.x119)**2) + 1 / sqrt((m.x6 - m.x10)**2 + (m.x61 -
    m.x65)**2 + (m.x116 - m.x120)**2) + 1 / sqrt((m.x6 - m.x11)**2 + (m.x61 -
    m.x66)**2 + (m.x116 - m.x121)**2) + 1 / sqrt((m.x6 - m.x12)**2 + (m.x61 -
    m.x67)**2 + (m.x116 - m.x122)**2) + 1 / sqrt((m.x6 - m.x13)**2 + (m.x61 -
    m.x68)**2 + (m.x116 - m.x123)**2) + 1 / sqrt((m.x6 - m.x14)**2 + (m.x61 -
    m.x69)**2 + (m.x116 - m.x124)**2) + 1 / sqrt((m.x6 - m.x15)**2 + (m.x61 -
    m.x70)**2 + (m.x116 - m.x125)**2) + 1 / sqrt((m.x6 - m.x16)**2 + (m.x61 -
    m.x71)**2 + (m.x116 - m.x126)**2) + 1 / sqrt((m.x6 - m.x17)**2 + (m.x61 -
    m.x72)**2 + (m.x116 - m.x127)**2) + 1 / sqrt((m.x6 - m.x18)**2 + (m.x61 -
    m.x73)**2 + (m.x116 - m.x128)**2) + 1 / sqrt((m.x6 - m.x19)**2 + (m.x61 -
    m.x74)**2 + (m.x116 - m.x129)**2) + 1 / sqrt((m.x6 - m.x20)**2 + (m.x61 -
    m.x75)**2 + (m.x116 - m.x130)**2) + 1 / sqrt((m.x6 - m.x21)**2 + (m.x61 -
    m.x76)**2 + (m.x116 - m.x131)**2) + 1 / sqrt((m.x6 - m.x22)**2 + (m.x61 -
    m.x77)**2 + (m.x116 - m.x132)**2) + 1 / sqrt((m.x6 - m.x23)**2 + (m.x61 -
    m.x78)**2 + (m.x116 - m.x133)**2) + 1 / sqrt((m.x6 - m.x24)**2 + (m.x61 -
    m.x79)**2 + (m.x116 - m.x134)**2) + 1 / sqrt((m.x6 - m.x25)**2 + (m.x61 -
    m.x80)**2 + (m.x116 - m.x135)**2) + 1 / sqrt((m.x6 - m.x26)**2 + (m.x61 -
    m.x81)**2 + (m.x116 - m.x136)**2) + 1 / sqrt((m.x6 - m.x27)**2 + (m.x61 -
    m.x82)**2 + (m.x116 - m.x137)**2) + 1 / sqrt((m.x6 - m.x28)**2 + (m.x61 -
    m.x83)**2 + (m.x116 - m.x138)**2) + 1 / sqrt((m.x6 - m.x29)**2 + (m.x61 -
    m.x84)**2 + (m.x116 - m.x139)**2) + 1 / sqrt((m.x6 - m.x30)**2 + (m.x61 -
    m.x85)**2 + (m.x116 - m.x140)**2) + 1 / sqrt((m.x6 - m.x31)**2 + (m.x61 -
    m.x86)**2 + (m.x116 - m.x141)**2) + 1 / sqrt((m.x6 - m.x32)**2 + (m.x61 -
    m.x87)**2 + (m.x116 - m.x142)**2) + 1 / sqrt((m.x6 - m.x33)**2 + (m.x61 -
    m.x88)**2 + (m.x116 - m.x143)**2) + 1 / sqrt((m.x6 - m.x34)**2 + (m.x61 -
    m.x89)**2 + (m.x116 - m.x144)**2) + 1 / sqrt((m.x6 - m.x35)**2 + (m.x61 -
    m.x90)**2 + (m.x116 - m.x145)**2) + 1 / sqrt((m.x6 - m.x36)**2 + (m.x61 -
    m.x91)**2 + (m.x116 - m.x146)**2) + 1 / sqrt((m.x6 - m.x37)**2 + (m.x61 -
    m.x92)**2 + (m.x116 - m.x147)**2) + 1 / sqrt((m.x6 - m.x38)**2 + (m.x61 -
    m.x93)**2 + (m.x116 - m.x148)**2) + 1 / sqrt((m.x6 - m.x39)**2 + (m.x61 -
    m.x94)**2 + (m.x116 - m.x149)**2) + 1 / sqrt((m.x6 - m.x40)**2 + (m.x61 -
    m.x95)**2 + (m.x116 - m.x150)**2) + 1 / sqrt((m.x6 - m.x41)**2 + (m.x61 -
    m.x96)**2 + (m.x116 - m.x151)**2) + 1 / sqrt((m.x6 - m.x42)**2 + (m.x61 -
    m.x97)**2 + (m.x116 - m.x152)**2) + 1 / sqrt((m.x6 - m.x43)**2 + (m.x61 -
    m.x98)**2 + (m.x116 - m.x153)**2) + 1 / sqrt((m.x6 - m.x44)**2 + (m.x61 -
    m.x99)**2 + (m.x116 - m.x154)**2) + 1 / sqrt((m.x6 - m.x45)**2 + (m.x61 -
    m.x100)**2 + (m.x116 - m.x155)**2) + 1 / sqrt((m.x6 - m.x46)**2 + (m.x61 -
    m.x101)**2 + (m.x116 - m.x156)**2) + 1 / sqrt((m.x6 - m.x47)**2 + (m.x61 -
    m.x102)**2 + (m.x116 - m.x157)**2) + 1 / sqrt((m.x6 - m.x48)**2 + (m.x61 -
    m.x103)**2 + (m.x116 - m.x158)**2) + 1 / sqrt((m.x6 - m.x49)**2 + (m.x61 -
    m.x104)**2 + (m.x116 - m.x159)**2) + 1 / sqrt((m.x6 - m.x50)**2 + (m.x61 -
    m.x105)**2 + (m.x116 - m.x160)**2) + 1 / sqrt((m.x6 - m.x51)**2 + (m.x61 -
    m.x106)**2 + (m.x116 - m.x161)**2) + 1 / sqrt((m.x6 - m.x52)**2 + (m.x61 -
    m.x107)**2 + (m.x116 - m.x162)**2) + 1 / sqrt((m.x6 - m.x53)**2 + (m.x61 -
    m.x108)**2 + (m.x116 - m.x163)**2) + 1 / sqrt((m.x6 - m.x54)**2 + (m.x61 -
    m.x109)**2 + (m.x116 - m.x164)**2) + 1 / sqrt((m.x6 - m.x55)**2 + (m.x61 -
    m.x110)**2 + (m.x116 - m.x165)**2) + 1 / sqrt((m.x7 - m.x8)**2 + (m.x62 -
    m.x63)**2 + (m.x117 - m.x118)**2) + 1 / sqrt((m.x7 - m.x9)**2 + (m.x62 -
    m.x64)**2 + (m.x117 - m.x119)**2) + 1 / sqrt((m.x7 - m.x10)**2 + (m.x62 -
    m.x65)**2 + (m.x117 - m.x120)**2) + 1 / sqrt((m.x7 - m.x11)**2 + (m.x62 -
    m.x66)**2 + (m.x117 - m.x121)**2) + 1 / sqrt((m.x7 - m.x12)**2 + (m.x62 -
    m.x67)**2 + (m.x117 - m.x122)**2) + 1 / sqrt((m.x7 - m.x13)**2 + (m.x62 -
    m.x68)**2 + (m.x117 - m.x123)**2) + 1 / sqrt((m.x7 - m.x14)**2 + (m.x62 -
    m.x69)**2 + (m.x117 - m.x124)**2) + 1 / sqrt((m.x7 - m.x15)**2 + (m.x62 -
    m.x70)**2 + (m.x117 - m.x125)**2) + 1 / sqrt((m.x7 - m.x16)**2 + (m.x62 -
    m.x71)**2 + (m.x117 - m.x126)**2) + 1 / sqrt((m.x7 - m.x17)**2 + (m.x62 -
    m.x72)**2 + (m.x117 - m.x127)**2) + 1 / sqrt((m.x7 - m.x18)**2 + (m.x62 -
    m.x73)**2 + (m.x117 - m.x128)**2) + 1 / sqrt((m.x7 - m.x19)**2 + (m.x62 -
    m.x74)**2 + (m.x117 - m.x129)**2) + 1 / sqrt((m.x7 - m.x20)**2 + (m.x62 -
    m.x75)**2 + (m.x117 - m.x130)**2) + 1 / sqrt((m.x7 - m.x21)**2 + (m.x62 -
    m.x76)**2 + (m.x117 - m.x131)**2) + 1 / sqrt((m.x7 - m.x22)**2 + (m.x62 -
    m.x77)**2 + (m.x117 - m.x132)**2) + 1 / sqrt((m.x7 - m.x23)**2 + (m.x62 -
    m.x78)**2 + (m.x117 - m.x133)**2) + 1 / sqrt((m.x7 - m.x24)**2 + (m.x62 -
    m.x79)**2 + (m.x117 - m.x134)**2) + 1 / sqrt((m.x7 - m.x25)**2 + (m.x62 -
    m.x80)**2 + (m.x117 - m.x135)**2) + 1 / sqrt((m.x7 - m.x26)**2 + (m.x62 -
    m.x81)**2 + (m.x117 - m.x136)**2) + 1 / sqrt((m.x7 - m.x27)**2 + (m.x62 -
    m.x82)**2 + (m.x117 - m.x137)**2) + 1 / sqrt((m.x7 - m.x28)**2 + (m.x62 -
    m.x83)**2 + (m.x117 - m.x138)**2) + 1 / sqrt((m.x7 - m.x29)**2 + (m.x62 -
    m.x84)**2 + (m.x117 - m.x139)**2) + 1 / sqrt((m.x7 - m.x30)**2 + (m.x62 -
    m.x85)**2 + (m.x117 - m.x140)**2) + 1 / sqrt((m.x7 - m.x31)**2 + (m.x62 -
    m.x86)**2 + (m.x117 - m.x141)**2) + 1 / sqrt((m.x7 - m.x32)**2 + (m.x62 -
    m.x87)**2 + (m.x117 - m.x142)**2) + 1 / sqrt((m.x7 - m.x33)**2 + (m.x62 -
    m.x88)**2 + (m.x117 - m.x143)**2) + 1 / sqrt((m.x7 - m.x34)**2 + (m.x62 -
    m.x89)**2 + (m.x117 - m.x144)**2) + 1 / sqrt((m.x7 - m.x35)**2 + (m.x62 -
    m.x90)**2 + (m.x117 - m.x145)**2) + 1 / sqrt((m.x7 - m.x36)**2 + (m.x62 -
    m.x91)**2 + (m.x117 - m.x146)**2) + 1 / sqrt((m.x7 - m.x37)**2 + (m.x62 -
    m.x92)**2 + (m.x117 - m.x147)**2) + 1 / sqrt((m.x7 - m.x38)**2 + (m.x62 -
    m.x93)**2 + (m.x117 - m.x148)**2) + 1 / sqrt((m.x7 - m.x39)**2 + (m.x62 -
    m.x94)**2 + (m.x117 - m.x149)**2) + 1 / sqrt((m.x7 - m.x40)**2 + (m.x62 -
    m.x95)**2 + (m.x117 - m.x150)**2) + 1 / sqrt((m.x7 - m.x41)**2 + (m.x62 -
    m.x96)**2 + (m.x117 - m.x151)**2) + 1 / sqrt((m.x7 - m.x42)**2 + (m.x62 -
    m.x97)**2 + (m.x117 - m.x152)**2) + 1 / sqrt((m.x7 - m.x43)**2 + (m.x62 -
    m.x98)**2 + (m.x117 - m.x153)**2) + 1 / sqrt((m.x7 - m.x44)**2 + (m.x62 -
    m.x99)**2 + (m.x117 - m.x154)**2) + 1 / sqrt((m.x7 - m.x45)**2 + (m.x62 -
    m.x100)**2 + (m.x117 - m.x155)**2) + 1 / sqrt((m.x7 - m.x46)**2 + (m.x62 -
    m.x101)**2 + (m.x117 - m.x156)**2) + 1 / sqrt((m.x7 - m.x47)**2 + (m.x62 -
    m.x102)**2 + (m.x117 - m.x157)**2) + 1 / sqrt((m.x7 - m.x48)**2 + (m.x62 -
    m.x103)**2 + (m.x117 - m.x158)**2) + 1 / sqrt((m.x7 - m.x49)**2 + (m.x62 -
    m.x104)**2 + (m.x117 - m.x159)**2) + 1 / sqrt((m.x7 - m.x50)**2 + (m.x62 -
    m.x105)**2 + (m.x117 - m.x160)**2) + 1 / sqrt((m.x7 - m.x51)**2 + (m.x62 -
    m.x106)**2 + (m.x117 - m.x161)**2) + 1 / sqrt((m.x7 - m.x52)**2 + (m.x62 -
    m.x107)**2 + (m.x117 - m.x162)**2) + 1 / sqrt((m.x7 - m.x53)**2 + (m.x62 -
    m.x108)**2 + (m.x117 - m.x163)**2) + 1 / sqrt((m.x7 - m.x54)**2 + (m.x62 -
    m.x109)**2 + (m.x117 - m.x164)**2) + 1 / sqrt((m.x7 - m.x55)**2 + (m.x62 -
    m.x110)**2 + (m.x117 - m.x165)**2) + 1 / sqrt((m.x8 - m.x9)**2 + (m.x63 -
    m.x64)**2 + (m.x118 - m.x119)**2) + 1 / sqrt((m.x8 - m.x10)**2 + (m.x63 -
    m.x65)**2 + (m.x118 - m.x120)**2) + 1 / sqrt((m.x8 - m.x11)**2 + (m.x63 -
    m.x66)**2 + (m.x118 - m.x121)**2) + 1 / sqrt((m.x8 - m.x12)**2 + (m.x63 -
    m.x67)**2 + (m.x118 - m.x122)**2) + 1 / sqrt((m.x8 - m.x13)**2 + (m.x63 -
    m.x68)**2 + (m.x118 - m.x123)**2) + 1 / sqrt((m.x8 - m.x14)**2 + (m.x63 -
    m.x69)**2 + (m.x118 - m.x124)**2) + 1 / sqrt((m.x8 - m.x15)**2 + (m.x63 -
    m.x70)**2 + (m.x118 - m.x125)**2) + 1 / sqrt((m.x8 - m.x16)**2 + (m.x63 -
    m.x71)**2 + (m.x118 - m.x126)**2) + 1 / sqrt((m.x8 - m.x17)**2 + (m.x63 -
    m.x72)**2 + (m.x118 - m.x127)**2) + 1 / sqrt((m.x8 - m.x18)**2 + (m.x63 -
    m.x73)**2 + (m.x118 - m.x128)**2) + 1 / sqrt((m.x8 - m.x19)**2 + (m.x63 -
    m.x74)**2 + (m.x118 - m.x129)**2) + 1 / sqrt((m.x8 - m.x20)**2 + (m.x63 -
    m.x75)**2 + (m.x118 - m.x130)**2) + 1 / sqrt((m.x8 - m.x21)**2 + (m.x63 -
    m.x76)**2 + (m.x118 - m.x131)**2) + 1 / sqrt((m.x8 - m.x22)**2 + (m.x63 -
    m.x77)**2 + (m.x118 - m.x132)**2) + 1 / sqrt((m.x8 - m.x23)**2 + (m.x63 -
    m.x78)**2 + (m.x118 - m.x133)**2) + 1 / sqrt((m.x8 - m.x24)**2 + (m.x63 -
    m.x79)**2 + (m.x118 - m.x134)**2) + 1 / sqrt((m.x8 - m.x25)**2 + (m.x63 -
    m.x80)**2 + (m.x118 - m.x135)**2) + 1 / sqrt((m.x8 - m.x26)**2 + (m.x63 -
    m.x81)**2 + (m.x118 - m.x136)**2) + 1 / sqrt((m.x8 - m.x27)**2 + (m.x63 -
    m.x82)**2 + (m.x118 - m.x137)**2) + 1 / sqrt((m.x8 - m.x28)**2 + (m.x63 -
    m.x83)**2 + (m.x118 - m.x138)**2) + 1 / sqrt((m.x8 - m.x29)**2 + (m.x63 -
    m.x84)**2 + (m.x118 - m.x139)**2) + 1 / sqrt((m.x8 - m.x30)**2 + (m.x63 -
    m.x85)**2 + (m.x118 - m.x140)**2) + 1 / sqrt((m.x8 - m.x31)**2 + (m.x63 -
    m.x86)**2 + (m.x118 - m.x141)**2) + 1 / sqrt((m.x8 - m.x32)**2 + (m.x63 -
    m.x87)**2 + (m.x118 - m.x142)**2) + 1 / sqrt((m.x8 - m.x33)**2 + (m.x63 -
    m.x88)**2 + (m.x118 - m.x143)**2) + 1 / sqrt((m.x8 - m.x34)**2 + (m.x63 -
    m.x89)**2 + (m.x118 - m.x144)**2) + 1 / sqrt((m.x8 - m.x35)**2 + (m.x63 -
    m.x90)**2 + (m.x118 - m.x145)**2) + 1 / sqrt((m.x8 - m.x36)**2 + (m.x63 -
    m.x91)**2 + (m.x118 - m.x146)**2) + 1 / sqrt((m.x8 - m.x37)**2 + (m.x63 -
    m.x92)**2 + (m.x118 - m.x147)**2) + 1 / sqrt((m.x8 - m.x38)**2 + (m.x63 -
    m.x93)**2 + (m.x118 - m.x148)**2) + 1 / sqrt((m.x8 - m.x39)**2 + (m.x63 -
    m.x94)**2 + (m.x118 - m.x149)**2) + 1 / sqrt((m.x8 - m.x40)**2 + (m.x63 -
    m.x95)**2 + (m.x118 - m.x150)**2) + 1 / sqrt((m.x8 - m.x41)**2 + (m.x63 -
    m.x96)**2 + (m.x118 - m.x151)**2) + 1 / sqrt((m.x8 - m.x42)**2 + (m.x63 -
    m.x97)**2 + (m.x118 - m.x152)**2) + 1 / sqrt((m.x8 - m.x43)**2 + (m.x63 -
    m.x98)**2 + (m.x118 - m.x153)**2) + 1 / sqrt((m.x8 - m.x44)**2 + (m.x63 -
    m.x99)**2 + (m.x118 - m.x154)**2) + 1 / sqrt((m.x8 - m.x45)**2 + (m.x63 -
    m.x100)**2 + (m.x118 - m.x155)**2) + 1 / sqrt((m.x8 - m.x46)**2 + (m.x63 -
    m.x101)**2 + (m.x118 - m.x156)**2) + 1 / sqrt((m.x8 - m.x47)**2 + (m.x63 -
    m.x102)**2 + (m.x118 - m.x157)**2) + 1 / sqrt((m.x8 - m.x48)**2 + (m.x63 -
    m.x103)**2 + (m.x118 - m.x158)**2) + 1 / sqrt((m.x8 - m.x49)**2 + (m.x63 -
    m.x104)**2 + (m.x118 - m.x159)**2) + 1 / sqrt((m.x8 - m.x50)**2 + (m.x63 -
    m.x105)**2 + (m.x118 - m.x160)**2) + 1 / sqrt((m.x8 - m.x51)**2 + (m.x63 -
    m.x106)**2 + (m.x118 - m.x161)**2) + 1 / sqrt((m.x8 - m.x52)**2 + (m.x63 -
    m.x107)**2 + (m.x118 - m.x162)**2) + 1 / sqrt((m.x8 - m.x53)**2 + (m.x63 -
    m.x108)**2 + (m.x118 - m.x163)**2) + 1 / sqrt((m.x8 - m.x54)**2 + (m.x63 -
    m.x109)**2 + (m.x118 - m.x164)**2) + 1 / sqrt((m.x8 - m.x55)**2 + (m.x63 -
    m.x110)**2 + (m.x118 - m.x165)**2) + 1 / sqrt((m.x9 - m.x10)**2 + (m.x64 -
    m.x65)**2 + (m.x119 - m.x120)**2) + 1 / sqrt((m.x9 - m.x11)**2 + (m.x64 -
    m.x66)**2 + (m.x119 - m.x121)**2) + 1 / sqrt((m.x9 - m.x12)**2 + (m.x64 -
    m.x67)**2 + (m.x119 - m.x122)**2) + 1 / sqrt((m.x9 - m.x13)**2 + (m.x64 -
    m.x68)**2 + (m.x119 - m.x123)**2) + 1 / sqrt((m.x9 - m.x14)**2 + (m.x64 -
    m.x69)**2 + (m.x119 - m.x124)**2) + 1 / sqrt((m.x9 - m.x15)**2 + (m.x64 -
    m.x70)**2 + (m.x119 - m.x125)**2) + 1 / sqrt((m.x9 - m.x16)**2 + (m.x64 -
    m.x71)**2 + (m.x119 - m.x126)**2) + 1 / sqrt((m.x9 - m.x17)**2 + (m.x64 -
    m.x72)**2 + (m.x119 - m.x127)**2) + 1 / sqrt((m.x9 - m.x18)**2 + (m.x64 -
    m.x73)**2 + (m.x119 - m.x128)**2) + 1 / sqrt((m.x9 - m.x19)**2 + (m.x64 -
    m.x74)**2 + (m.x119 - m.x129)**2) + 1 / sqrt((m.x9 - m.x20)**2 + (m.x64 -
    m.x75)**2 + (m.x119 - m.x130)**2) + 1 / sqrt((m.x9 - m.x21)**2 + (m.x64 -
    m.x76)**2 + (m.x119 - m.x131)**2) + 1 / sqrt((m.x9 - m.x22)**2 + (m.x64 -
    m.x77)**2 + (m.x119 - m.x132)**2) + 1 / sqrt((m.x9 - m.x23)**2 + (m.x64 -
    m.x78)**2 + (m.x119 - m.x133)**2) + 1 / sqrt((m.x9 - m.x24)**2 + (m.x64 -
    m.x79)**2 + (m.x119 - m.x134)**2) + 1 / sqrt((m.x9 - m.x25)**2 + (m.x64 -
    m.x80)**2 + (m.x119 - m.x135)**2) + 1 / sqrt((m.x9 - m.x26)**2 + (m.x64 -
    m.x81)**2 + (m.x119 - m.x136)**2) + 1 / sqrt((m.x9 - m.x27)**2 + (m.x64 -
    m.x82)**2 + (m.x119 - m.x137)**2) + 1 / sqrt((m.x9 - m.x28)**2 + (m.x64 -
    m.x83)**2 + (m.x119 - m.x138)**2) + 1 / sqrt((m.x9 - m.x29)**2 + (m.x64 -
    m.x84)**2 + (m.x119 - m.x139)**2) + 1 / sqrt((m.x9 - m.x30)**2 + (m.x64 -
    m.x85)**2 + (m.x119 - m.x140)**2) + 1 / sqrt((m.x9 - m.x31)**2 + (m.x64 -
    m.x86)**2 + (m.x119 - m.x141)**2) + 1 / sqrt((m.x9 - m.x32)**2 + (m.x64 -
    m.x87)**2 + (m.x119 - m.x142)**2) + 1 / sqrt((m.x9 - m.x33)**2 + (m.x64 -
    m.x88)**2 + (m.x119 - m.x143)**2) + 1 / sqrt((m.x9 - m.x34)**2 + (m.x64 -
    m.x89)**2 + (m.x119 - m.x144)**2) + 1 / sqrt((m.x9 - m.x35)**2 + (m.x64 -
    m.x90)**2 + (m.x119 - m.x145)**2) + 1 / sqrt((m.x9 - m.x36)**2 + (m.x64 -
    m.x91)**2 + (m.x119 - m.x146)**2) + 1 / sqrt((m.x9 - m.x37)**2 + (m.x64 -
    m.x92)**2 + (m.x119 - m.x147)**2) + 1 / sqrt((m.x9 - m.x38)**2 + (m.x64 -
    m.x93)**2 + (m.x119 - m.x148)**2) + 1 / sqrt((m.x9 - m.x39)**2 + (m.x64 -
    m.x94)**2 + (m.x119 - m.x149)**2) + 1 / sqrt((m.x9 - m.x40)**2 + (m.x64 -
    m.x95)**2 + (m.x119 - m.x150)**2) + 1 / sqrt((m.x9 - m.x41)**2 + (m.x64 -
    m.x96)**2 + (m.x119 - m.x151)**2) + 1 / sqrt((m.x9 - m.x42)**2 + (m.x64 -
    m.x97)**2 + (m.x119 - m.x152)**2) + 1 / sqrt((m.x9 - m.x43)**2 + (m.x64 -
    m.x98)**2 + (m.x119 - m.x153)**2) + 1 / sqrt((m.x9 - m.x44)**2 + (m.x64 -
    m.x99)**2 + (m.x119 - m.x154)**2) + 1 / sqrt((m.x9 - m.x45)**2 + (m.x64 -
    m.x100)**2 + (m.x119 - m.x155)**2) + 1 / sqrt((m.x9 - m.x46)**2 + (m.x64 -
    m.x101)**2 + (m.x119 - m.x156)**2) + 1 / sqrt((m.x9 - m.x47)**2 + (m.x64 -
    m.x102)**2 + (m.x119 - m.x157)**2) + 1 / sqrt((m.x9 - m.x48)**2 + (m.x64 -
    m.x103)**2 + (m.x119 - m.x158)**2) + 1 / sqrt((m.x9 - m.x49)**2 + (m.x64 -
    m.x104)**2 + (m.x119 - m.x159)**2) + 1 / sqrt((m.x9 - m.x50)**2 + (m.x64 -
    m.x105)**2 + (m.x119 - m.x160)**2) + 1 / sqrt((m.x9 - m.x51)**2 + (m.x64 -
    m.x106)**2 + (m.x119 - m.x161)**2) + 1 / sqrt((m.x9 - m.x52)**2 + (m.x64 -
    m.x107)**2 + (m.x119 - m.x162)**2) + 1 / sqrt((m.x9 - m.x53)**2 + (m.x64 -
    m.x108)**2 + (m.x119 - m.x163)**2) + 1 / sqrt((m.x9 - m.x54)**2 + (m.x64 -
    m.x109)**2 + (m.x119 - m.x164)**2) + 1 / sqrt((m.x9 - m.x55)**2 + (m.x64 -
    m.x110)**2 + (m.x119 - m.x165)**2) + 1 / sqrt((m.x10 - m.x11)**2 + (m.x65
    - m.x66)**2 + (m.x120 - m.x121)**2) + 1 / sqrt((m.x10 - m.x12)**2 + (m.x65
    - m.x67)**2 + (m.x120 - m.x122)**2) + 1 / sqrt((m.x10 - m.x13)**2 + (m.x65
    - m.x68)**2 + (m.x120 - m.x123)**2) + 1 / sqrt((m.x10 - m.x14)**2 + (m.x65
    - m.x69)**2 + (m.x120 - m.x124)**2) + 1 / sqrt((m.x10 - m.x15)**2 + (m.x65
    - m.x70)**2 + (m.x120 - m.x125)**2) + 1 / sqrt((m.x10 - m.x16)**2 + (m.x65
    - m.x71)**2 + (m.x120 - m.x126)**2) + 1 / sqrt((m.x10 - m.x17)**2 + (m.x65
    - m.x72)**2 + (m.x120 - m.x127)**2) + 1 / sqrt((m.x10 - m.x18)**2 + (m.x65
    - m.x73)**2 + (m.x120 - m.x128)**2) + 1 / sqrt((m.x10 - m.x19)**2 + (m.x65
    - m.x74)**2 + (m.x120 - m.x129)**2) + 1 / sqrt((m.x10 - m.x20)**2 + (m.x65
    - m.x75)**2 + (m.x120 - m.x130)**2) + 1 / sqrt((m.x10 - m.x21)**2 + (m.x65
    - m.x76)**2 + (m.x120 - m.x131)**2) + 1 / sqrt((m.x10 - m.x22)**2 + (m.x65
    - m.x77)**2 + (m.x120 - m.x132)**2) + 1 / sqrt((m.x10 - m.x23)**2 + (m.x65
    - m.x78)**2 + (m.x120 - m.x133)**2) + 1 / sqrt((m.x10 - m.x24)**2 + (m.x65
    - m.x79)**2 + (m.x120 - m.x134)**2) + 1 / sqrt((m.x10 - m.x25)**2 + (m.x65
    - m.x80)**2 + (m.x120 - m.x135)**2) + 1 / sqrt((m.x10 - m.x26)**2 + (m.x65
    - m.x81)**2 + (m.x120 - m.x136)**2) + 1 / sqrt((m.x10 - m.x27)**2 + (m.x65
    - m.x82)**2 + (m.x120 - m.x137)**2) + 1 / sqrt((m.x10 - m.x28)**2 + (m.x65
    - m.x83)**2 + (m.x120 - m.x138)**2) + 1 / sqrt((m.x10 - m.x29)**2 + (m.x65
    - m.x84)**2 + (m.x120 - m.x139)**2) + 1 / sqrt((m.x10 - m.x30)**2 + (m.x65
    - m.x85)**2 + (m.x120 - m.x140)**2) + 1 / sqrt((m.x10 - m.x31)**2 + (m.x65
    - m.x86)**2 + (m.x120 - m.x141)**2) + 1 / sqrt((m.x10 - m.x32)**2 + (m.x65
    - m.x87)**2 + (m.x120 - m.x142)**2) + 1 / sqrt((m.x10 - m.x33)**2 + (m.x65
    - m.x88)**2 + (m.x120 - m.x143)**2) + 1 / sqrt((m.x10 - m.x34)**2 + (m.x65
    - m.x89)**2 + (m.x120 - m.x144)**2) + 1 / sqrt((m.x10 - m.x35)**2 + (m.x65
    - m.x90)**2 + (m.x120 - m.x145)**2) + 1 / sqrt((m.x10 - m.x36)**2 + (m.x65
    - m.x91)**2 + (m.x120 - m.x146)**2) + 1 / sqrt((m.x10 - m.x37)**2 + (m.x65
    - m.x92)**2 + (m.x120 - m.x147)**2) + 1 / sqrt((m.x10 - m.x38)**2 + (m.x65
    - m.x93)**2 + (m.x120 - m.x148)**2) + 1 / sqrt((m.x10 - m.x39)**2 + (m.x65
    - m.x94)**2 + (m.x120 - m.x149)**2) + 1 / sqrt((m.x10 - m.x40)**2 + (m.x65
    - m.x95)**2 + (m.x120 - m.x150)**2) + 1 / sqrt((m.x10 - m.x41)**2 + (m.x65
    - m.x96)**2 + (m.x120 - m.x151)**2) + 1 / sqrt((m.x10 - m.x42)**2 + (m.x65
    - m.x97)**2 + (m.x120 - m.x152)**2) + 1 / sqrt((m.x10 - m.x43)**2 + (m.x65
    - m.x98)**2 + (m.x120 - m.x153)**2) + 1 / sqrt((m.x10 - m.x44)**2 + (m.x65
    - m.x99)**2 + (m.x120 - m.x154)**2) + 1 / sqrt((m.x10 - m.x45)**2 + (m.x65
    - m.x100)**2 + (m.x120 - m.x155)**2) + 1 / sqrt((m.x10 - m.x46)**2 + (
    m.x65 - m.x101)**2 + (m.x120 - m.x156)**2) + 1 / sqrt((m.x10 - m.x47)**2 +
    (m.x65 - m.x102)**2 + (m.x120 - m.x157)**2) + 1 / sqrt((m.x10 - m.x48)**2
    + (m.x65 - m.x103)**2 + (m.x120 - m.x158)**2) + 1 / sqrt((m.x10 - m.x49)**
    2 + (m.x65 - m.x104)**2 + (m.x120 - m.x159)**2) + 1 / sqrt((m.x10 - m.x50)
    **2 + (m.x65 - m.x105)**2 + (m.x120 - m.x160)**2) + 1 / sqrt((m.x10 - m.x51)
    **2 + (m.x65 - m.x106)**2 + (m.x120 - m.x161)**2) + 1 / sqrt((m.x10 - m.x52)
    **2 + (m.x65 - m.x107)**2 + (m.x120 - m.x162)**2) + 1 / sqrt((m.x10 - m.x53)
    **2 + (m.x65 - m.x108)**2 + (m.x120 - m.x163)**2) + 1 / sqrt((m.x10 - m.x54)
    **2 + (m.x65 - m.x109)**2 + (m.x120 - m.x164)**2) + 1 / sqrt((m.x10 - m.x55)
    **2 + (m.x65 - m.x110)**2 + (m.x120 - m.x165)**2) + 1 / sqrt((m.x11 - m.x12)
    **2 + (m.x66 - m.x67)**2 + (m.x121 - m.x122)**2) + 1 / sqrt((m.x11 - m.x13)
    **2 + (m.x66 - m.x68)**2 + (m.x121 - m.x123)**2) + 1 / sqrt((m.x11 - m.x14)
    **2 + (m.x66 - m.x69)**2 + (m.x121 - m.x124)**2) + 1 / sqrt((m.x11 - m.x15)
    **2 + (m.x66 - m.x70)**2 + (m.x121 - m.x125)**2) + 1 / sqrt((m.x11 - m.x16)
    **2 + (m.x66 - m.x71)**2 + (m.x121 - m.x126)**2) + 1 / sqrt((m.x11 - m.x17)
    **2 + (m.x66 - m.x72)**2 + (m.x121 - m.x127)**2) + 1 / sqrt((m.x11 - m.x18)
    **2 + (m.x66 - m.x73)**2 + (m.x121 - m.x128)**2) + 1 / sqrt((m.x11 - m.x19)
    **2 + (m.x66 - m.x74)**2 + (m.x121 - m.x129)**2) + 1 / sqrt((m.x11 - m.x20)
    **2 + (m.x66 - m.x75)**2 + (m.x121 - m.x130)**2) + 1 / sqrt((m.x11 - m.x21)
    **2 + (m.x66 - m.x76)**2 + (m.x121 - m.x131)**2) + 1 / sqrt((m.x11 - m.x22)
    **2 + (m.x66 - m.x77)**2 + (m.x121 - m.x132)**2) + 1 / sqrt((m.x11 - m.x23)
    **2 + (m.x66 - m.x78)**2 + (m.x121 - m.x133)**2) + 1 / sqrt((m.x11 - m.x24)
    **2 + (m.x66 - m.x79)**2 + (m.x121 - m.x134)**2) + 1 / sqrt((m.x11 - m.x25)
    **2 + (m.x66 - m.x80)**2 + (m.x121 - m.x135)**2) + 1 / sqrt((m.x11 - m.x26)
    **2 + (m.x66 - m.x81)**2 + (m.x121 - m.x136)**2) + 1 / sqrt((m.x11 - m.x27)
    **2 + (m.x66 - m.x82)**2 + (m.x121 - m.x137)**2) + 1 / sqrt((m.x11 - m.x28)
    **2 + (m.x66 - m.x83)**2 + (m.x121 - m.x138)**2) + 1 / sqrt((m.x11 - m.x29)
    **2 + (m.x66 - m.x84)**2 + (m.x121 - m.x139)**2) + 1 / sqrt((m.x11 - m.x30)
    **2 + (m.x66 - m.x85)**2 + (m.x121 - m.x140)**2) + 1 / sqrt((m.x11 - m.x31)
    **2 + (m.x66 - m.x86)**2 + (m.x121 - m.x141)**2) + 1 / sqrt((m.x11 - m.x32)
    **2 + (m.x66 - m.x87)**2 + (m.x121 - m.x142)**2) + 1 / sqrt((m.x11 - m.x33)
    **2 + (m.x66 - m.x88)**2 + (m.x121 - m.x143)**2) + 1 / sqrt((m.x11 - m.x34)
    **2 + (m.x66 - m.x89)**2 + (m.x121 - m.x144)**2) + 1 / sqrt((m.x11 - m.x35)
    **2 + (m.x66 - m.x90)**2 + (m.x121 - m.x145)**2) + 1 / sqrt((m.x11 - m.x36)
    **2 + (m.x66 - m.x91)**2 + (m.x121 - m.x146)**2) + 1 / sqrt((m.x11 - m.x37)
    **2 + (m.x66 - m.x92)**2 + (m.x121 - m.x147)**2) + 1 / sqrt((m.x11 - m.x38)
    **2 + (m.x66 - m.x93)**2 + (m.x121 - m.x148)**2) + 1 / sqrt((m.x11 - m.x39)
    **2 + (m.x66 - m.x94)**2 + (m.x121 - m.x149)**2) + 1 / sqrt((m.x11 - m.x40)
    **2 + (m.x66 - m.x95)**2 + (m.x121 - m.x150)**2) + 1 / sqrt((m.x11 - m.x41)
    **2 + (m.x66 - m.x96)**2 + (m.x121 - m.x151)**2) + 1 / sqrt((m.x11 - m.x42)
    **2 + (m.x66 - m.x97)**2 + (m.x121 - m.x152)**2) + 1 / sqrt((m.x11 - m.x43)
    **2 + (m.x66 - m.x98)**2 + (m.x121 - m.x153)**2) + 1 / sqrt((m.x11 - m.x44)
    **2 + (m.x66 - m.x99)**2 + (m.x121 - m.x154)**2) + 1 / sqrt((m.x11 - m.x45)
    **2 + (m.x66 - m.x100)**2 + (m.x121 - m.x155)**2) + 1 / sqrt((m.x11 - m.x46)
    **2 + (m.x66 - m.x101)**2 + (m.x121 - m.x156)**2) + 1 / sqrt((m.x11 - m.x47)
    **2 + (m.x66 - m.x102)**2 + (m.x121 - m.x157)**2) + 1 / sqrt((m.x11 - m.x48)
    **2 + (m.x66 - m.x103)**2 + (m.x121 - m.x158)**2) + 1 / sqrt((m.x11 - m.x49)
    **2 + (m.x66 - m.x104)**2 + (m.x121 - m.x159)**2) + 1 / sqrt((m.x11 - m.x50)
    **2 + (m.x66 - m.x105)**2 + (m.x121 - m.x160)**2) + 1 / sqrt((m.x11 - m.x51)
    **2 + (m.x66 - m.x106)**2 + (m.x121 - m.x161)**2) + 1 / sqrt((m.x11 - m.x52)
    **2 + (m.x66 - m.x107)**2 + (m.x121 - m.x162)**2) + 1 / sqrt((m.x11 - m.x53)
    **2 + (m.x66 - m.x108)**2 + (m.x121 - m.x163)**2) + 1 / sqrt((m.x11 - m.x54)
    **2 + (m.x66 - m.x109)**2 + (m.x121 - m.x164)**2) + 1 / sqrt((m.x11 - m.x55)
    **2 + (m.x66 - m.x110)**2 + (m.x121 - m.x165)**2) + 1 / sqrt((m.x12 - m.x13)
    **2 + (m.x67 - m.x68)**2 + (m.x122 - m.x123)**2) + 1 / sqrt((m.x12 - m.x14)
    **2 + (m.x67 - m.x69)**2 + (m.x122 - m.x124)**2) + 1 / sqrt((m.x12 - m.x15)
    **2 + (m.x67 - m.x70)**2 + (m.x122 - m.x125)**2) + 1 / sqrt((m.x12 - m.x16)
    **2 + (m.x67 - m.x71)**2 + (m.x122 - m.x126)**2) + 1 / sqrt((m.x12 - m.x17)
    **2 + (m.x67 - m.x72)**2 + (m.x122 - m.x127)**2) + 1 / sqrt((m.x12 - m.x18)
    **2 + (m.x67 - m.x73)**2 + (m.x122 - m.x128)**2) + 1 / sqrt((m.x12 - m.x19)
    **2 + (m.x67 - m.x74)**2 + (m.x122 - m.x129)**2) + 1 / sqrt((m.x12 - m.x20)
    **2 + (m.x67 - m.x75)**2 + (m.x122 - m.x130)**2) + 1 / sqrt((m.x12 - m.x21)
    **2 + (m.x67 - m.x76)**2 + (m.x122 - m.x131)**2) + 1 / sqrt((m.x12 - m.x22)
    **2 + (m.x67 - m.x77)**2 + (m.x122 - m.x132)**2) + 1 / sqrt((m.x12 - m.x23)
    **2 + (m.x67 - m.x78)**2 + (m.x122 - m.x133)**2) + 1 / sqrt((m.x12 - m.x24)
    **2 + (m.x67 - m.x79)**2 + (m.x122 - m.x134)**2) + 1 / sqrt((m.x12 - m.x25)
    **2 + (m.x67 - m.x80)**2 + (m.x122 - m.x135)**2) + 1 / sqrt((m.x12 - m.x26)
    **2 + (m.x67 - m.x81)**2 + (m.x122 - m.x136)**2) + 1 / sqrt((m.x12 - m.x27)
    **2 + (m.x67 - m.x82)**2 + (m.x122 - m.x137)**2) + 1 / sqrt((m.x12 - m.x28)
    **2 + (m.x67 - m.x83)**2 + (m.x122 - m.x138)**2) + 1 / sqrt((m.x12 - m.x29)
    **2 + (m.x67 - m.x84)**2 + (m.x122 - m.x139)**2) + 1 / sqrt((m.x12 - m.x30)
    **2 + (m.x67 - m.x85)**2 + (m.x122 - m.x140)**2) + 1 / sqrt((m.x12 - m.x31)
    **2 + (m.x67 - m.x86)**2 + (m.x122 - m.x141)**2) + 1 / sqrt((m.x12 - m.x32)
    **2 + (m.x67 - m.x87)**2 + (m.x122 - m.x142)**2) + 1 / sqrt((m.x12 - m.x33)
    **2 + (m.x67 - m.x88)**2 + (m.x122 - m.x143)**2) + 1 / sqrt((m.x12 - m.x34)
    **2 + (m.x67 - m.x89)**2 + (m.x122 - m.x144)**2) + 1 / sqrt((m.x12 - m.x35)
    **2 + (m.x67 - m.x90)**2 + (m.x122 - m.x145)**2) + 1 / sqrt((m.x12 - m.x36)
    **2 + (m.x67 - m.x91)**2 + (m.x122 - m.x146)**2) + 1 / sqrt((m.x12 - m.x37)
    **2 + (m.x67 - m.x92)**2 + (m.x122 - m.x147)**2) + 1 / sqrt((m.x12 - m.x38)
    **2 + (m.x67 - m.x93)**2 + (m.x122 - m.x148)**2) + 1 / sqrt((m.x12 - m.x39)
    **2 + (m.x67 - m.x94)**2 + (m.x122 - m.x149)**2) + 1 / sqrt((m.x12 - m.x40)
    **2 + (m.x67 - m.x95)**2 + (m.x122 - m.x150)**2) + 1 / sqrt((m.x12 - m.x41)
    **2 + (m.x67 - m.x96)**2 + (m.x122 - m.x151)**2) + 1 / sqrt((m.x12 - m.x42)
    **2 + (m.x67 - m.x97)**2 + (m.x122 - m.x152)**2) + 1 / sqrt((m.x12 - m.x43)
    **2 + (m.x67 - m.x98)**2 + (m.x122 - m.x153)**2) + 1 / sqrt((m.x12 - m.x44)
    **2 + (m.x67 - m.x99)**2 + (m.x122 - m.x154)**2) + 1 / sqrt((m.x12 - m.x45)
    **2 + (m.x67 - m.x100)**2 + (m.x122 - m.x155)**2) + 1 / sqrt((m.x12 - m.x46)
    **2 + (m.x67 - m.x101)**2 + (m.x122 - m.x156)**2) + 1 / sqrt((m.x12 - m.x47)
    **2 + (m.x67 - m.x102)**2 + (m.x122 - m.x157)**2) + 1 / sqrt((m.x12 - m.x48)
    **2 + (m.x67 - m.x103)**2 + (m.x122 - m.x158)**2) + 1 / sqrt((m.x12 - m.x49)
    **2 + (m.x67 - m.x104)**2 + (m.x122 - m.x159)**2) + 1 / sqrt((m.x12 - m.x50)
    **2 + (m.x67 - m.x105)**2 + (m.x122 - m.x160)**2) + 1 / sqrt((m.x12 - m.x51)
    **2 + (m.x67 - m.x106)**2 + (m.x122 - m.x161)**2) + 1 / sqrt((m.x12 - m.x52)
    **2 + (m.x67 - m.x107)**2 + (m.x122 - m.x162)**2) + 1 / sqrt((m.x12 - m.x53)
    **2 + (m.x67 - m.x108)**2 + (m.x122 - m.x163)**2) + 1 / sqrt((m.x12 - m.x54)
    **2 + (m.x67 - m.x109)**2 + (m.x122 - m.x164)**2) + 1 / sqrt((m.x12 - m.x55)
    **2 + (m.x67 - m.x110)**2 + (m.x122 - m.x165)**2) + 1 / sqrt((m.x13 - m.x14)
    **2 + (m.x68 - m.x69)**2 + (m.x123 - m.x124)**2) + 1 / sqrt((m.x13 - m.x15)
    **2 + (m.x68 - m.x70)**2 + (m.x123 - m.x125)**2) + 1 / sqrt((m.x13 - m.x16)
    **2 + (m.x68 - m.x71)**2 + (m.x123 - m.x126)**2) + 1 / sqrt((m.x13 - m.x17)
    **2 + (m.x68 - m.x72)**2 + (m.x123 - m.x127)**2) + 1 / sqrt((m.x13 - m.x18)
    **2 + (m.x68 - m.x73)**2 + (m.x123 - m.x128)**2) + 1 / sqrt((m.x13 - m.x19)
    **2 + (m.x68 - m.x74)**2 + (m.x123 - m.x129)**2) + 1 / sqrt((m.x13 - m.x20)
    **2 + (m.x68 - m.x75)**2 + (m.x123 - m.x130)**2) + 1 / sqrt((m.x13 - m.x21)
    **2 + (m.x68 - m.x76)**2 + (m.x123 - m.x131)**2) + 1 / sqrt((m.x13 - m.x22)
    **2 + (m.x68 - m.x77)**2 + (m.x123 - m.x132)**2) + 1 / sqrt((m.x13 - m.x23)
    **2 + (m.x68 - m.x78)**2 + (m.x123 - m.x133)**2) + 1 / sqrt((m.x13 - m.x24)
    **2 + (m.x68 - m.x79)**2 + (m.x123 - m.x134)**2) + 1 / sqrt((m.x13 - m.x25)
    **2 + (m.x68 - m.x80)**2 + (m.x123 - m.x135)**2) + 1 / sqrt((m.x13 - m.x26)
    **2 + (m.x68 - m.x81)**2 + (m.x123 - m.x136)**2) + 1 / sqrt((m.x13 - m.x27)
    **2 + (m.x68 - m.x82)**2 + (m.x123 - m.x137)**2) + 1 / sqrt((m.x13 - m.x28)
    **2 + (m.x68 - m.x83)**2 + (m.x123 - m.x138)**2) + 1 / sqrt((m.x13 - m.x29)
    **2 + (m.x68 - m.x84)**2 + (m.x123 - m.x139)**2) + 1 / sqrt((m.x13 - m.x30)
    **2 + (m.x68 - m.x85)**2 + (m.x123 - m.x140)**2) + 1 / sqrt((m.x13 - m.x31)
    **2 + (m.x68 - m.x86)**2 + (m.x123 - m.x141)**2) + 1 / sqrt((m.x13 - m.x32)
    **2 + (m.x68 - m.x87)**2 + (m.x123 - m.x142)**2) + 1 / sqrt((m.x13 - m.x33)
    **2 + (m.x68 - m.x88)**2 + (m.x123 - m.x143)**2) + 1 / sqrt((m.x13 - m.x34)
    **2 + (m.x68 - m.x89)**2 + (m.x123 - m.x144)**2) + 1 / sqrt((m.x13 - m.x35)
    **2 + (m.x68 - m.x90)**2 + (m.x123 - m.x145)**2) + 1 / sqrt((m.x13 - m.x36)
    **2 + (m.x68 - m.x91)**2 + (m.x123 - m.x146)**2) + 1 / sqrt((m.x13 - m.x37)
    **2 + (m.x68 - m.x92)**2 + (m.x123 - m.x147)**2) + 1 / sqrt((m.x13 - m.x38)
    **2 + (m.x68 - m.x93)**2 + (m.x123 - m.x148)**2) + 1 / sqrt((m.x13 - m.x39)
    **2 + (m.x68 - m.x94)**2 + (m.x123 - m.x149)**2) + 1 / sqrt((m.x13 - m.x40)
    **2 + (m.x68 - m.x95)**2 + (m.x123 - m.x150)**2) + 1 / sqrt((m.x13 - m.x41)
    **2 + (m.x68 - m.x96)**2 + (m.x123 - m.x151)**2) + 1 / sqrt((m.x13 - m.x42)
    **2 + (m.x68 - m.x97)**2 + (m.x123 - m.x152)**2) + 1 / sqrt((m.x13 - m.x43)
    **2 + (m.x68 - m.x98)**2 + (m.x123 - m.x153)**2) + 1 / sqrt((m.x13 - m.x44)
    **2 + (m.x68 - m.x99)**2 + (m.x123 - m.x154)**2) + 1 / sqrt((m.x13 - m.x45)
    **2 + (m.x68 - m.x100)**2 + (m.x123 - m.x155)**2) + 1 / sqrt((m.x13 - m.x46)
    **2 + (m.x68 - m.x101)**2 + (m.x123 - m.x156)**2) + 1 / sqrt((m.x13 - m.x47)
    **2 + (m.x68 - m.x102)**2 + (m.x123 - m.x157)**2) + 1 / sqrt((m.x13 - m.x48)
    **2 + (m.x68 - m.x103)**2 + (m.x123 - m.x158)**2) + 1 / sqrt((m.x13 - m.x49)
    **2 + (m.x68 - m.x104)**2 + (m.x123 - m.x159)**2) + 1 / sqrt((m.x13 - m.x50)
    **2 + (m.x68 - m.x105)**2 + (m.x123 - m.x160)**2) + 1 / sqrt((m.x13 - m.x51)
    **2 + (m.x68 - m.x106)**2 + (m.x123 - m.x161)**2) + 1 / sqrt((m.x13 - m.x52)
    **2 + (m.x68 - m.x107)**2 + (m.x123 - m.x162)**2) + 1 / sqrt((m.x13 - m.x53)
    **2 + (m.x68 - m.x108)**2 + (m.x123 - m.x163)**2) + 1 / sqrt((m.x13 - m.x54)
    **2 + (m.x68 - m.x109)**2 + (m.x123 - m.x164)**2) + 1 / sqrt((m.x13 - m.x55)
    **2 + (m.x68 - m.x110)**2 + (m.x123 - m.x165)**2) + 1 / sqrt((m.x14 - m.x15)
    **2 + (m.x69 - m.x70)**2 + (m.x124 - m.x125)**2) + 1 / sqrt((m.x14 - m.x16)
    **2 + (m.x69 - m.x71)**2 + (m.x124 - m.x126)**2) + 1 / sqrt((m.x14 - m.x17)
    **2 + (m.x69 - m.x72)**2 + (m.x124 - m.x127)**2) + 1 / sqrt((m.x14 - m.x18)
    **2 + (m.x69 - m.x73)**2 + (m.x124 - m.x128)**2) + 1 / sqrt((m.x14 - m.x19)
    **2 + (m.x69 - m.x74)**2 + (m.x124 - m.x129)**2) + 1 / sqrt((m.x14 - m.x20)
    **2 + (m.x69 - m.x75)**2 + (m.x124 - m.x130)**2) + 1 / sqrt((m.x14 - m.x21)
    **2 + (m.x69 - m.x76)**2 + (m.x124 - m.x131)**2) + 1 / sqrt((m.x14 - m.x22)
    **2 + (m.x69 - m.x77)**2 + (m.x124 - m.x132)**2) + 1 / sqrt((m.x14 - m.x23)
    **2 + (m.x69 - m.x78)**2 + (m.x124 - m.x133)**2) + 1 / sqrt((m.x14 - m.x24)
    **2 + (m.x69 - m.x79)**2 + (m.x124 - m.x134)**2) + 1 / sqrt((m.x14 - m.x25)
    **2 + (m.x69 - m.x80)**2 + (m.x124 - m.x135)**2) + 1 / sqrt((m.x14 - m.x26)
    **2 + (m.x69 - m.x81)**2 + (m.x124 - m.x136)**2) + 1 / sqrt((m.x14 - m.x27)
    **2 + (m.x69 - m.x82)**2 + (m.x124 - m.x137)**2) + 1 / sqrt((m.x14 - m.x28)
    **2 + (m.x69 - m.x83)**2 + (m.x124 - m.x138)**2) + 1 / sqrt((m.x14 - m.x29)
    **2 + (m.x69 - m.x84)**2 + (m.x124 - m.x139)**2) + 1 / sqrt((m.x14 - m.x30)
    **2 + (m.x69 - m.x85)**2 + (m.x124 - m.x140)**2) + 1 / sqrt((m.x14 - m.x31)
    **2 + (m.x69 - m.x86)**2 + (m.x124 - m.x141)**2) + 1 / sqrt((m.x14 - m.x32)
    **2 + (m.x69 - m.x87)**2 + (m.x124 - m.x142)**2) + 1 / sqrt((m.x14 - m.x33)
    **2 + (m.x69 - m.x88)**2 + (m.x124 - m.x143)**2) + 1 / sqrt((m.x14 - m.x34)
    **2 + (m.x69 - m.x89)**2 + (m.x124 - m.x144)**2) + 1 / sqrt((m.x14 - m.x35)
    **2 + (m.x69 - m.x90)**2 + (m.x124 - m.x145)**2) + 1 / sqrt((m.x14 - m.x36)
    **2 + (m.x69 - m.x91)**2 + (m.x124 - m.x146)**2) + 1 / sqrt((m.x14 - m.x37)
    **2 + (m.x69 - m.x92)**2 + (m.x124 - m.x147)**2) + 1 / sqrt((m.x14 - m.x38)
    **2 + (m.x69 - m.x93)**2 + (m.x124 - m.x148)**2) + 1 / sqrt((m.x14 - m.x39)
    **2 + (m.x69 - m.x94)**2 + (m.x124 - m.x149)**2) + 1 / sqrt((m.x14 - m.x40)
    **2 + (m.x69 - m.x95)**2 + (m.x124 - m.x150)**2) + 1 / sqrt((m.x14 - m.x41)
    **2 + (m.x69 - m.x96)**2 + (m.x124 - m.x151)**2) + 1 / sqrt((m.x14 - m.x42)
    **2 + (m.x69 - m.x97)**2 + (m.x124 - m.x152)**2) + 1 / sqrt((m.x14 - m.x43)
    **2 + (m.x69 - m.x98)**2 + (m.x124 - m.x153)**2) + 1 / sqrt((m.x14 - m.x44)
    **2 + (m.x69 - m.x99)**2 + (m.x124 - m.x154)**2) + 1 / sqrt((m.x14 - m.x45)
    **2 + (m.x69 - m.x100)**2 + (m.x124 - m.x155)**2) + 1 / sqrt((m.x14 - m.x46)
    **2 + (m.x69 - m.x101)**2 + (m.x124 - m.x156)**2) + 1 / sqrt((m.x14 - m.x47)
    **2 + (m.x69 - m.x102)**2 + (m.x124 - m.x157)**2) + 1 / sqrt((m.x14 - m.x48)
    **2 + (m.x69 - m.x103)**2 + (m.x124 - m.x158)**2) + 1 / sqrt((m.x14 - m.x49)
    **2 + (m.x69 - m.x104)**2 + (m.x124 - m.x159)**2) + 1 / sqrt((m.x14 - m.x50)
    **2 + (m.x69 - m.x105)**2 + (m.x124 - m.x160)**2) + 1 / sqrt((m.x14 - m.x51)
    **2 + (m.x69 - m.x106)**2 + (m.x124 - m.x161)**2) + 1 / sqrt((m.x14 - m.x52)
    **2 + (m.x69 - m.x107)**2 + (m.x124 - m.x162)**2) + 1 / sqrt((m.x14 - m.x53)
    **2 + (m.x69 - m.x108)**2 + (m.x124 - m.x163)**2) + 1 / sqrt((m.x14 - m.x54)
    **2 + (m.x69 - m.x109)**2 + (m.x124 - m.x164)**2) + 1 / sqrt((m.x14 - m.x55)
    **2 + (m.x69 - m.x110)**2 + (m.x124 - m.x165)**2) + 1 / sqrt((m.x15 - m.x16)
    **2 + (m.x70 - m.x71)**2 + (m.x125 - m.x126)**2) + 1 / sqrt((m.x15 - m.x17)
    **2 + (m.x70 - m.x72)**2 + (m.x125 - m.x127)**2) + 1 / sqrt((m.x15 - m.x18)
    **2 + (m.x70 - m.x73)**2 + (m.x125 - m.x128)**2) + 1 / sqrt((m.x15 - m.x19)
    **2 + (m.x70 - m.x74)**2 + (m.x125 - m.x129)**2) + 1 / sqrt((m.x15 - m.x20)
    **2 + (m.x70 - m.x75)**2 + (m.x125 - m.x130)**2) + 1 / sqrt((m.x15 - m.x21)
    **2 + (m.x70 - m.x76)**2 + (m.x125 - m.x131)**2) + 1 / sqrt((m.x15 - m.x22)
    **2 + (m.x70 - m.x77)**2 + (m.x125 - m.x132)**2) + 1 / sqrt((m.x15 - m.x23)
    **2 + (m.x70 - m.x78)**2 + (m.x125 - m.x133)**2) + 1 / sqrt((m.x15 - m.x24)
    **2 + (m.x70 - m.x79)**2 + (m.x125 - m.x134)**2) + 1 / sqrt((m.x15 - m.x25)
    **2 + (m.x70 - m.x80)**2 + (m.x125 - m.x135)**2) + 1 / sqrt((m.x15 - m.x26)
    **2 + (m.x70 - m.x81)**2 + (m.x125 - m.x136)**2) + 1 / sqrt((m.x15 - m.x27)
    **2 + (m.x70 - m.x82)**2 + (m.x125 - m.x137)**2) + 1 / sqrt((m.x15 - m.x28)
    **2 + (m.x70 - m.x83)**2 + (m.x125 - m.x138)**2) + 1 / sqrt((m.x15 - m.x29)
    **2 + (m.x70 - m.x84)**2 + (m.x125 - m.x139)**2) + 1 / sqrt((m.x15 - m.x30)
    **2 + (m.x70 - m.x85)**2 + (m.x125 - m.x140)**2) + 1 / sqrt((m.x15 - m.x31)
    **2 + (m.x70 - m.x86)**2 + (m.x125 - m.x141)**2) + 1 / sqrt((m.x15 - m.x32)
    **2 + (m.x70 - m.x87)**2 + (m.x125 - m.x142)**2) + 1 / sqrt((m.x15 - m.x33)
    **2 + (m.x70 - m.x88)**2 + (m.x125 - m.x143)**2) + 1 / sqrt((m.x15 - m.x34)
    **2 + (m.x70 - m.x89)**2 + (m.x125 - m.x144)**2) + 1 / sqrt((m.x15 - m.x35)
    **2 + (m.x70 - m.x90)**2 + (m.x125 - m.x145)**2) + 1 / sqrt((m.x15 - m.x36)
    **2 + (m.x70 - m.x91)**2 + (m.x125 - m.x146)**2) + 1 / sqrt((m.x15 - m.x37)
    **2 + (m.x70 - m.x92)**2 + (m.x125 - m.x147)**2) + 1 / sqrt((m.x15 - m.x38)
    **2 + (m.x70 - m.x93)**2 + (m.x125 - m.x148)**2) + 1 / sqrt((m.x15 - m.x39)
    **2 + (m.x70 - m.x94)**2 + (m.x125 - m.x149)**2) + 1 / sqrt((m.x15 - m.x40)
    **2 + (m.x70 - m.x95)**2 + (m.x125 - m.x150)**2) + 1 / sqrt((m.x15 - m.x41)
    **2 + (m.x70 - m.x96)**2 + (m.x125 - m.x151)**2) + 1 / sqrt((m.x15 - m.x42)
    **2 + (m.x70 - m.x97)**2 + (m.x125 - m.x152)**2) + 1 / sqrt((m.x15 - m.x43)
    **2 + (m.x70 - m.x98)**2 + (m.x125 - m.x153)**2) + 1 / sqrt((m.x15 - m.x44)
    **2 + (m.x70 - m.x99)**2 + (m.x125 - m.x154)**2) + 1 / sqrt((m.x15 - m.x45)
    **2 + (m.x70 - m.x100)**2 + (m.x125 - m.x155)**2) + 1 / sqrt((m.x15 - m.x46)
    **2 + (m.x70 - m.x101)**2 + (m.x125 - m.x156)**2) + 1 / sqrt((m.x15 - m.x47)
    **2 + (m.x70 - m.x102)**2 + (m.x125 - m.x157)**2) + 1 / sqrt((m.x15 - m.x48)
    **2 + (m.x70 - m.x103)**2 + (m.x125 - m.x158)**2) + 1 / sqrt((m.x15 - m.x49)
    **2 + (m.x70 - m.x104)**2 + (m.x125 - m.x159)**2) + 1 / sqrt((m.x15 - m.x50)
    **2 + (m.x70 - m.x105)**2 + (m.x125 - m.x160)**2) + 1 / sqrt((m.x15 - m.x51)
    **2 + (m.x70 - m.x106)**2 + (m.x125 - m.x161)**2) + 1 / sqrt((m.x15 - m.x52)
    **2 + (m.x70 - m.x107)**2 + (m.x125 - m.x162)**2) + 1 / sqrt((m.x15 - m.x53)
    **2 + (m.x70 - m.x108)**2 + (m.x125 - m.x163)**2) + 1 / sqrt((m.x15 - m.x54)
    **2 + (m.x70 - m.x109)**2 + (m.x125 - m.x164)**2) + 1 / sqrt((m.x15 - m.x55)
    **2 + (m.x70 - m.x110)**2 + (m.x125 - m.x165)**2) + 1 / sqrt((m.x16 - m.x17)
    **2 + (m.x71 - m.x72)**2 + (m.x126 - m.x127)**2) + 1 / sqrt((m.x16 - m.x18)
    **2 + (m.x71 - m.x73)**2 + (m.x126 - m.x128)**2) + 1 / sqrt((m.x16 - m.x19)
    **2 + (m.x71 - m.x74)**2 + (m.x126 - m.x129)**2) + 1 / sqrt((m.x16 - m.x20)
    **2 + (m.x71 - m.x75)**2 + (m.x126 - m.x130)**2) + 1 / sqrt((m.x16 - m.x21)
    **2 + (m.x71 - m.x76)**2 + (m.x126 - m.x131)**2) + 1 / sqrt((m.x16 - m.x22)
    **2 + (m.x71 - m.x77)**2 + (m.x126 - m.x132)**2) + 1 / sqrt((m.x16 - m.x23)
    **2 + (m.x71 - m.x78)**2 + (m.x126 - m.x133)**2) + 1 / sqrt((m.x16 - m.x24)
    **2 + (m.x71 - m.x79)**2 + (m.x126 - m.x134)**2) + 1 / sqrt((m.x16 - m.x25)
    **2 + (m.x71 - m.x80)**2 + (m.x126 - m.x135)**2) + 1 / sqrt((m.x16 - m.x26)
    **2 + (m.x71 - m.x81)**2 + (m.x126 - m.x136)**2) + 1 / sqrt((m.x16 - m.x27)
    **2 + (m.x71 - m.x82)**2 + (m.x126 - m.x137)**2) + 1 / sqrt((m.x16 - m.x28)
    **2 + (m.x71 - m.x83)**2 + (m.x126 - m.x138)**2) + 1 / sqrt((m.x16 - m.x29)
    **2 + (m.x71 - m.x84)**2 + (m.x126 - m.x139)**2) + 1 / sqrt((m.x16 - m.x30)
    **2 + (m.x71 - m.x85)**2 + (m.x126 - m.x140)**2) + 1 / sqrt((m.x16 - m.x31)
    **2 + (m.x71 - m.x86)**2 + (m.x126 - m.x141)**2) + 1 / sqrt((m.x16 - m.x32)
    **2 + (m.x71 - m.x87)**2 + (m.x126 - m.x142)**2) + 1 / sqrt((m.x16 - m.x33)
    **2 + (m.x71 - m.x88)**2 + (m.x126 - m.x143)**2) + 1 / sqrt((m.x16 - m.x34)
    **2 + (m.x71 - m.x89)**2 + (m.x126 - m.x144)**2) + 1 / sqrt((m.x16 - m.x35)
    **2 + (m.x71 - m.x90)**2 + (m.x126 - m.x145)**2) + 1 / sqrt((m.x16 - m.x36)
    **2 + (m.x71 - m.x91)**2 + (m.x126 - m.x146)**2) + 1 / sqrt((m.x16 - m.x37)
    **2 + (m.x71 - m.x92)**2 + (m.x126 - m.x147)**2) + 1 / sqrt((m.x16 - m.x38)
    **2 + (m.x71 - m.x93)**2 + (m.x126 - m.x148)**2) + 1 / sqrt((m.x16 - m.x39)
    **2 + (m.x71 - m.x94)**2 + (m.x126 - m.x149)**2) + 1 / sqrt((m.x16 - m.x40)
    **2 + (m.x71 - m.x95)**2 + (m.x126 - m.x150)**2) + 1 / sqrt((m.x16 - m.x41)
    **2 + (m.x71 - m.x96)**2 + (m.x126 - m.x151)**2) + 1 / sqrt((m.x16 - m.x42)
    **2 + (m.x71 - m.x97)**2 + (m.x126 - m.x152)**2) + 1 / sqrt((m.x16 - m.x43)
    **2 + (m.x71 - m.x98)**2 + (m.x126 - m.x153)**2) + 1 / sqrt((m.x16 - m.x44)
    **2 + (m.x71 - m.x99)**2 + (m.x126 - m.x154)**2) + 1 / sqrt((m.x16 - m.x45)
    **2 + (m.x71 - m.x100)**2 + (m.x126 - m.x155)**2) + 1 / sqrt((m.x16 - m.x46)
    **2 + (m.x71 - m.x101)**2 + (m.x126 - m.x156)**2) + 1 / sqrt((m.x16 - m.x47)
    **2 + (m.x71 - m.x102)**2 + (m.x126 - m.x157)**2) + 1 / sqrt((m.x16 - m.x48)
    **2 + (m.x71 - m.x103)**2 + (m.x126 - m.x158)**2) + 1 / sqrt((m.x16 - m.x49)
    **2 + (m.x71 - m.x104)**2 + (m.x126 - m.x159)**2) + 1 / sqrt((m.x16 - m.x50)
    **2 + (m.x71 - m.x105)**2 + (m.x126 - m.x160)**2) + 1 / sqrt((m.x16 - m.x51)
    **2 + (m.x71 - m.x106)**2 + (m.x126 - m.x161)**2) + 1 / sqrt((m.x16 - m.x52)
    **2 + (m.x71 - m.x107)**2 + (m.x126 - m.x162)**2) + 1 / sqrt((m.x16 - m.x53)
    **2 + (m.x71 - m.x108)**2 + (m.x126 - m.x163)**2) + 1 / sqrt((m.x16 - m.x54)
    **2 + (m.x71 - m.x109)**2 + (m.x126 - m.x164)**2) + 1 / sqrt((m.x16 - m.x55)
    **2 + (m.x71 - m.x110)**2 + (m.x126 - m.x165)**2) + 1 / sqrt((m.x17 - m.x18)
    **2 + (m.x72 - m.x73)**2 + (m.x127 - m.x128)**2) + 1 / sqrt((m.x17 - m.x19)
    **2 + (m.x72 - m.x74)**2 + (m.x127 - m.x129)**2) + 1 / sqrt((m.x17 - m.x20)
    **2 + (m.x72 - m.x75)**2 + (m.x127 - m.x130)**2) + 1 / sqrt((m.x17 - m.x21)
    **2 + (m.x72 - m.x76)**2 + (m.x127 - m.x131)**2) + 1 / sqrt((m.x17 - m.x22)
    **2 + (m.x72 - m.x77)**2 + (m.x127 - m.x132)**2) + 1 / sqrt((m.x17 - m.x23)
    **2 + (m.x72 - m.x78)**2 + (m.x127 - m.x133)**2) + 1 / sqrt((m.x17 - m.x24)
    **2 + (m.x72 - m.x79)**2 + (m.x127 - m.x134)**2) + 1 / sqrt((m.x17 - m.x25)
    **2 + (m.x72 - m.x80)**2 + (m.x127 - m.x135)**2) + 1 / sqrt((m.x17 - m.x26)
    **2 + (m.x72 - m.x81)**2 + (m.x127 - m.x136)**2) + 1 / sqrt((m.x17 - m.x27)
    **2 + (m.x72 - m.x82)**2 + (m.x127 - m.x137)**2) + 1 / sqrt((m.x17 - m.x28)
    **2 + (m.x72 - m.x83)**2 + (m.x127 - m.x138)**2) + 1 / sqrt((m.x17 - m.x29)
    **2 + (m.x72 - m.x84)**2 + (m.x127 - m.x139)**2) + 1 / sqrt((m.x17 - m.x30)
    **2 + (m.x72 - m.x85)**2 + (m.x127 - m.x140)**2) + 1 / sqrt((m.x17 - m.x31)
    **2 + (m.x72 - m.x86)**2 + (m.x127 - m.x141)**2) + 1 / sqrt((m.x17 - m.x32)
    **2 + (m.x72 - m.x87)**2 + (m.x127 - m.x142)**2) + 1 / sqrt((m.x17 - m.x33)
    **2 + (m.x72 - m.x88)**2 + (m.x127 - m.x143)**2) + 1 / sqrt((m.x17 - m.x34)
    **2 + (m.x72 - m.x89)**2 + (m.x127 - m.x144)**2) + 1 / sqrt((m.x17 - m.x35)
    **2 + (m.x72 - m.x90)**2 + (m.x127 - m.x145)**2) + 1 / sqrt((m.x17 - m.x36)
    **2 + (m.x72 - m.x91)**2 + (m.x127 - m.x146)**2) + 1 / sqrt((m.x17 - m.x37)
    **2 + (m.x72 - m.x92)**2 + (m.x127 - m.x147)**2) + 1 / sqrt((m.x17 - m.x38)
    **2 + (m.x72 - m.x93)**2 + (m.x127 - m.x148)**2) + 1 / sqrt((m.x17 - m.x39)
    **2 + (m.x72 - m.x94)**2 + (m.x127 - m.x149)**2) + 1 / sqrt((m.x17 - m.x40)
    **2 + (m.x72 - m.x95)**2 + (m.x127 - m.x150)**2) + 1 / sqrt((m.x17 - m.x41)
    **2 + (m.x72 - m.x96)**2 + (m.x127 - m.x151)**2) + 1 / sqrt((m.x17 - m.x42)
    **2 + (m.x72 - m.x97)**2 + (m.x127 - m.x152)**2) + 1 / sqrt((m.x17 - m.x43)
    **2 + (m.x72 - m.x98)**2 + (m.x127 - m.x153)**2) + 1 / sqrt((m.x17 - m.x44)
    **2 + (m.x72 - m.x99)**2 + (m.x127 - m.x154)**2) + 1 / sqrt((m.x17 - m.x45)
    **2 + (m.x72 - m.x100)**2 + (m.x127 - m.x155)**2) + 1 / sqrt((m.x17 - m.x46)
    **2 + (m.x72 - m.x101)**2 + (m.x127 - m.x156)**2) + 1 / sqrt((m.x17 - m.x47)
    **2 + (m.x72 - m.x102)**2 + (m.x127 - m.x157)**2) + 1 / sqrt((m.x17 - m.x48)
    **2 + (m.x72 - m.x103)**2 + (m.x127 - m.x158)**2) + 1 / sqrt((m.x17 - m.x49)
    **2 + (m.x72 - m.x104)**2 + (m.x127 - m.x159)**2) + 1 / sqrt((m.x17 - m.x50)
    **2 + (m.x72 - m.x105)**2 + (m.x127 - m.x160)**2) + 1 / sqrt((m.x17 - m.x51)
    **2 + (m.x72 - m.x106)**2 + (m.x127 - m.x161)**2) + 1 / sqrt((m.x17 - m.x52)
    **2 + (m.x72 - m.x107)**2 + (m.x127 - m.x162)**2) + 1 / sqrt((m.x17 - m.x53)
    **2 + (m.x72 - m.x108)**2 + (m.x127 - m.x163)**2) + 1 / sqrt((m.x17 - m.x54)
    **2 + (m.x72 - m.x109)**2 + (m.x127 - m.x164)**2) + 1 / sqrt((m.x17 - m.x55)
    **2 + (m.x72 - m.x110)**2 + (m.x127 - m.x165)**2) + 1 / sqrt((m.x18 - m.x19)
    **2 + (m.x73 - m.x74)**2 + (m.x128 - m.x129)**2) + 1 / sqrt((m.x18 - m.x20)
    **2 + (m.x73 - m.x75)**2 + (m.x128 - m.x130)**2) + 1 / sqrt((m.x18 - m.x21)
    **2 + (m.x73 - m.x76)**2 + (m.x128 - m.x131)**2) + 1 / sqrt((m.x18 - m.x22)
    **2 + (m.x73 - m.x77)**2 + (m.x128 - m.x132)**2) + 1 / sqrt((m.x18 - m.x23)
    **2 + (m.x73 - m.x78)**2 + (m.x128 - m.x133)**2) + 1 / sqrt((m.x18 - m.x24)
    **2 + (m.x73 - m.x79)**2 + (m.x128 - m.x134)**2) + 1 / sqrt((m.x18 - m.x25)
    **2 + (m.x73 - m.x80)**2 + (m.x128 - m.x135)**2) + 1 / sqrt((m.x18 - m.x26)
    **2 + (m.x73 - m.x81)**2 + (m.x128 - m.x136)**2) + 1 / sqrt((m.x18 - m.x27)
    **2 + (m.x73 - m.x82)**2 + (m.x128 - m.x137)**2) + 1 / sqrt((m.x18 - m.x28)
    **2 + (m.x73 - m.x83)**2 + (m.x128 - m.x138)**2) + 1 / sqrt((m.x18 - m.x29)
    **2 + (m.x73 - m.x84)**2 + (m.x128 - m.x139)**2) + 1 / sqrt((m.x18 - m.x30)
    **2 + (m.x73 - m.x85)**2 + (m.x128 - m.x140)**2) + 1 / sqrt((m.x18 - m.x31)
    **2 + (m.x73 - m.x86)**2 + (m.x128 - m.x141)**2) + 1 / sqrt((m.x18 - m.x32)
    **2 + (m.x73 - m.x87)**2 + (m.x128 - m.x142)**2) + 1 / sqrt((m.x18 - m.x33)
    **2 + (m.x73 - m.x88)**2 + (m.x128 - m.x143)**2) + 1 / sqrt((m.x18 - m.x34)
    **2 + (m.x73 - m.x89)**2 + (m.x128 - m.x144)**2) + 1 / sqrt((m.x18 - m.x35)
    **2 + (m.x73 - m.x90)**2 + (m.x128 - m.x145)**2) + 1 / sqrt((m.x18 - m.x36)
    **2 + (m.x73 - m.x91)**2 + (m.x128 - m.x146)**2) + 1 / sqrt((m.x18 - m.x37)
    **2 + (m.x73 - m.x92)**2 + (m.x128 - m.x147)**2) + 1 / sqrt((m.x18 - m.x38)
    **2 + (m.x73 - m.x93)**2 + (m.x128 - m.x148)**2) + 1 / sqrt((m.x18 - m.x39)
    **2 + (m.x73 - m.x94)**2 + (m.x128 - m.x149)**2) + 1 / sqrt((m.x18 - m.x40)
    **2 + (m.x73 - m.x95)**2 + (m.x128 - m.x150)**2) + 1 / sqrt((m.x18 - m.x41)
    **2 + (m.x73 - m.x96)**2 + (m.x128 - m.x151)**2) + 1 / sqrt((m.x18 - m.x42)
    **2 + (m.x73 - m.x97)**2 + (m.x128 - m.x152)**2) + 1 / sqrt((m.x18 - m.x43)
    **2 + (m.x73 - m.x98)**2 + (m.x128 - m.x153)**2) + 1 / sqrt((m.x18 - m.x44)
    **2 + (m.x73 - m.x99)**2 + (m.x128 - m.x154)**2) + 1 / sqrt((m.x18 - m.x45)
    **2 + (m.x73 - m.x100)**2 + (m.x128 - m.x155)**2) + 1 / sqrt((m.x18 - m.x46)
    **2 + (m.x73 - m.x101)**2 + (m.x128 - m.x156)**2) + 1 / sqrt((m.x18 - m.x47)
    **2 + (m.x73 - m.x102)**2 + (m.x128 - m.x157)**2) + 1 / sqrt((m.x18 - m.x48)
    **2 + (m.x73 - m.x103)**2 + (m.x128 - m.x158)**2) + 1 / sqrt((m.x18 - m.x49)
    **2 + (m.x73 - m.x104)**2 + (m.x128 - m.x159)**2) + 1 / sqrt((m.x18 - m.x50)
    **2 + (m.x73 - m.x105)**2 + (m.x128 - m.x160)**2) + 1 / sqrt((m.x18 - m.x51)
    **2 + (m.x73 - m.x106)**2 + (m.x128 - m.x161)**2) + 1 / sqrt((m.x18 - m.x52)
    **2 + (m.x73 - m.x107)**2 + (m.x128 - m.x162)**2) + 1 / sqrt((m.x18 - m.x53)
    **2 + (m.x73 - m.x108)**2 + (m.x128 - m.x163)**2) + 1 / sqrt((m.x18 - m.x54)
    **2 + (m.x73 - m.x109)**2 + (m.x128 - m.x164)**2) + 1 / sqrt((m.x18 - m.x55)
    **2 + (m.x73 - m.x110)**2 + (m.x128 - m.x165)**2) + 1 / sqrt((m.x19 - m.x20)
    **2 + (m.x74 - m.x75)**2 + (m.x129 - m.x130)**2) + 1 / sqrt((m.x19 - m.x21)
    **2 + (m.x74 - m.x76)**2 + (m.x129 - m.x131)**2) + 1 / sqrt((m.x19 - m.x22)
    **2 + (m.x74 - m.x77)**2 + (m.x129 - m.x132)**2) + 1 / sqrt((m.x19 - m.x23)
    **2 + (m.x74 - m.x78)**2 + (m.x129 - m.x133)**2) + 1 / sqrt((m.x19 - m.x24)
    **2 + (m.x74 - m.x79)**2 + (m.x129 - m.x134)**2) + 1 / sqrt((m.x19 - m.x25)
    **2 + (m.x74 - m.x80)**2 + (m.x129 - m.x135)**2) + 1 / sqrt((m.x19 - m.x26)
    **2 + (m.x74 - m.x81)**2 + (m.x129 - m.x136)**2) + 1 / sqrt((m.x19 - m.x27)
    **2 + (m.x74 - m.x82)**2 + (m.x129 - m.x137)**2) + 1 / sqrt((m.x19 - m.x28)
    **2 + (m.x74 - m.x83)**2 + (m.x129 - m.x138)**2) + 1 / sqrt((m.x19 - m.x29)
    **2 + (m.x74 - m.x84)**2 + (m.x129 - m.x139)**2) + 1 / sqrt((m.x19 - m.x30)
    **2 + (m.x74 - m.x85)**2 + (m.x129 - m.x140)**2) + 1 / sqrt((m.x19 - m.x31)
    **2 + (m.x74 - m.x86)**2 + (m.x129 - m.x141)**2) + 1 / sqrt((m.x19 - m.x32)
    **2 + (m.x74 - m.x87)**2 + (m.x129 - m.x142)**2) + 1 / sqrt((m.x19 - m.x33)
    **2 + (m.x74 - m.x88)**2 + (m.x129 - m.x143)**2) + 1 / sqrt((m.x19 - m.x34)
    **2 + (m.x74 - m.x89)**2 + (m.x129 - m.x144)**2) + 1 / sqrt((m.x19 - m.x35)
    **2 + (m.x74 - m.x90)**2 + (m.x129 - m.x145)**2) + 1 / sqrt((m.x19 - m.x36)
    **2 + (m.x74 - m.x91)**2 + (m.x129 - m.x146)**2) + 1 / sqrt((m.x19 - m.x37)
    **2 + (m.x74 - m.x92)**2 + (m.x129 - m.x147)**2) + 1 / sqrt((m.x19 - m.x38)
    **2 + (m.x74 - m.x93)**2 + (m.x129 - m.x148)**2) + 1 / sqrt((m.x19 - m.x39)
    **2 + (m.x74 - m.x94)**2 + (m.x129 - m.x149)**2) + 1 / sqrt((m.x19 - m.x40)
    **2 + (m.x74 - m.x95)**2 + (m.x129 - m.x150)**2) + 1 / sqrt((m.x19 - m.x41)
    **2 + (m.x74 - m.x96)**2 + (m.x129 - m.x151)**2) + 1 / sqrt((m.x19 - m.x42)
    **2 + (m.x74 - m.x97)**2 + (m.x129 - m.x152)**2) + 1 / sqrt((m.x19 - m.x43)
    **2 + (m.x74 - m.x98)**2 + (m.x129 - m.x153)**2) + 1 / sqrt((m.x19 - m.x44)
    **2 + (m.x74 - m.x99)**2 + (m.x129 - m.x154)**2) + 1 / sqrt((m.x19 - m.x45)
    **2 + (m.x74 - m.x100)**2 + (m.x129 - m.x155)**2) + 1 / sqrt((m.x19 - m.x46)
    **2 + (m.x74 - m.x101)**2 + (m.x129 - m.x156)**2) + 1 / sqrt((m.x19 - m.x47)
    **2 + (m.x74 - m.x102)**2 + (m.x129 - m.x157)**2) + 1 / sqrt((m.x19 - m.x48)
    **2 + (m.x74 - m.x103)**2 + (m.x129 - m.x158)**2) + 1 / sqrt((m.x19 - m.x49)
    **2 + (m.x74 - m.x104)**2 + (m.x129 - m.x159)**2) + 1 / sqrt((m.x19 - m.x50)
    **2 + (m.x74 - m.x105)**2 + (m.x129 - m.x160)**2) + 1 / sqrt((m.x19 - m.x51)
    **2 + (m.x74 - m.x106)**2 + (m.x129 - m.x161)**2) + 1 / sqrt((m.x19 - m.x52)
    **2 + (m.x74 - m.x107)**2 + (m.x129 - m.x162)**2) + 1 / sqrt((m.x19 - m.x53)
    **2 + (m.x74 - m.x108)**2 + (m.x129 - m.x163)**2) + 1 / sqrt((m.x19 - m.x54)
    **2 + (m.x74 - m.x109)**2 + (m.x129 - m.x164)**2) + 1 / sqrt((m.x19 - m.x55)
    **2 + (m.x74 - m.x110)**2 + (m.x129 - m.x165)**2) + 1 / sqrt((m.x20 - m.x21)
    **2 + (m.x75 - m.x76)**2 + (m.x130 - m.x131)**2) + 1 / sqrt((m.x20 - m.x22)
    **2 + (m.x75 - m.x77)**2 + (m.x130 - m.x132)**2) + 1 / sqrt((m.x20 - m.x23)
    **2 + (m.x75 - m.x78)**2 + (m.x130 - m.x133)**2) + 1 / sqrt((m.x20 - m.x24)
    **2 + (m.x75 - m.x79)**2 + (m.x130 - m.x134)**2) + 1 / sqrt((m.x20 - m.x25)
    **2 + (m.x75 - m.x80)**2 + (m.x130 - m.x135)**2) + 1 / sqrt((m.x20 - m.x26)
    **2 + (m.x75 - m.x81)**2 + (m.x130 - m.x136)**2) + 1 / sqrt((m.x20 - m.x27)
    **2 + (m.x75 - m.x82)**2 + (m.x130 - m.x137)**2) + 1 / sqrt((m.x20 - m.x28)
    **2 + (m.x75 - m.x83)**2 + (m.x130 - m.x138)**2) + 1 / sqrt((m.x20 - m.x29)
    **2 + (m.x75 - m.x84)**2 + (m.x130 - m.x139)**2) + 1 / sqrt((m.x20 - m.x30)
    **2 + (m.x75 - m.x85)**2 + (m.x130 - m.x140)**2) + 1 / sqrt((m.x20 - m.x31)
    **2 + (m.x75 - m.x86)**2 + (m.x130 - m.x141)**2) + 1 / sqrt((m.x20 - m.x32)
    **2 + (m.x75 - m.x87)**2 + (m.x130 - m.x142)**2) + 1 / sqrt((m.x20 - m.x33)
    **2 + (m.x75 - m.x88)**2 + (m.x130 - m.x143)**2) + 1 / sqrt((m.x20 - m.x34)
    **2 + (m.x75 - m.x89)**2 + (m.x130 - m.x144)**2) + 1 / sqrt((m.x20 - m.x35)
    **2 + (m.x75 - m.x90)**2 + (m.x130 - m.x145)**2) + 1 / sqrt((m.x20 - m.x36)
    **2 + (m.x75 - m.x91)**2 + (m.x130 - m.x146)**2) + 1 / sqrt((m.x20 - m.x37)
    **2 + (m.x75 - m.x92)**2 + (m.x130 - m.x147)**2) + 1 / sqrt((m.x20 - m.x38)
    **2 + (m.x75 - m.x93)**2 + (m.x130 - m.x148)**2) + 1 / sqrt((m.x20 - m.x39)
    **2 + (m.x75 - m.x94)**2 + (m.x130 - m.x149)**2) + 1 / sqrt((m.x20 - m.x40)
    **2 + (m.x75 - m.x95)**2 + (m.x130 - m.x150)**2) + 1 / sqrt((m.x20 - m.x41)
    **2 + (m.x75 - m.x96)**2 + (m.x130 - m.x151)**2) + 1 / sqrt((m.x20 - m.x42)
    **2 + (m.x75 - m.x97)**2 + (m.x130 - m.x152)**2) + 1 / sqrt((m.x20 - m.x43)
    **2 + (m.x75 - m.x98)**2 + (m.x130 - m.x153)**2) + 1 / sqrt((m.x20 - m.x44)
    **2 + (m.x75 - m.x99)**2 + (m.x130 - m.x154)**2) + 1 / sqrt((m.x20 - m.x45)
    **2 + (m.x75 - m.x100)**2 + (m.x130 - m.x155)**2) + 1 / sqrt((m.x20 - m.x46)
    **2 + (m.x75 - m.x101)**2 + (m.x130 - m.x156)**2) + 1 / sqrt((m.x20 - m.x47)
    **2 + (m.x75 - m.x102)**2 + (m.x130 - m.x157)**2) + 1 / sqrt((m.x20 - m.x48)
    **2 + (m.x75 - m.x103)**2 + (m.x130 - m.x158)**2) + 1 / sqrt((m.x20 - m.x49)
    **2 + (m.x75 - m.x104)**2 + (m.x130 - m.x159)**2) + 1 / sqrt((m.x20 - m.x50)
    **2 + (m.x75 - m.x105)**2 + (m.x130 - m.x160)**2) + 1 / sqrt((m.x20 - m.x51)
    **2 + (m.x75 - m.x106)**2 + (m.x130 - m.x161)**2) + 1 / sqrt((m.x20 - m.x52)
    **2 + (m.x75 - m.x107)**2 + (m.x130 - m.x162)**2) + 1 / sqrt((m.x20 - m.x53)
    **2 + (m.x75 - m.x108)**2 + (m.x130 - m.x163)**2) + 1 / sqrt((m.x20 - m.x54)
    **2 + (m.x75 - m.x109)**2 + (m.x130 - m.x164)**2) + 1 / sqrt((m.x20 - m.x55)
    **2 + (m.x75 - m.x110)**2 + (m.x130 - m.x165)**2) + 1 / sqrt((m.x21 - m.x22)
    **2 + (m.x76 - m.x77)**2 + (m.x131 - m.x132)**2) + 1 / sqrt((m.x21 - m.x23)
    **2 + (m.x76 - m.x78)**2 + (m.x131 - m.x133)**2) + 1 / sqrt((m.x21 - m.x24)
    **2 + (m.x76 - m.x79)**2 + (m.x131 - m.x134)**2) + 1 / sqrt((m.x21 - m.x25)
    **2 + (m.x76 - m.x80)**2 + (m.x131 - m.x135)**2) + 1 / sqrt((m.x21 - m.x26)
    **2 + (m.x76 - m.x81)**2 + (m.x131 - m.x136)**2) + 1 / sqrt((m.x21 - m.x27)
    **2 + (m.x76 - m.x82)**2 + (m.x131 - m.x137)**2) + 1 / sqrt((m.x21 - m.x28)
    **2 + (m.x76 - m.x83)**2 + (m.x131 - m.x138)**2) + 1 / sqrt((m.x21 - m.x29)
    **2 + (m.x76 - m.x84)**2 + (m.x131 - m.x139)**2) + 1 / sqrt((m.x21 - m.x30)
    **2 + (m.x76 - m.x85)**2 + (m.x131 - m.x140)**2) + 1 / sqrt((m.x21 - m.x31)
    **2 + (m.x76 - m.x86)**2 + (m.x131 - m.x141)**2) + 1 / sqrt((m.x21 - m.x32)
    **2 + (m.x76 - m.x87)**2 + (m.x131 - m.x142)**2) + 1 / sqrt((m.x21 - m.x33)
    **2 + (m.x76 - m.x88)**2 + (m.x131 - m.x143)**2) + 1 / sqrt((m.x21 - m.x34)
    **2 + (m.x76 - m.x89)**2 + (m.x131 - m.x144)**2) + 1 / sqrt((m.x21 - m.x35)
    **2 + (m.x76 - m.x90)**2 + (m.x131 - m.x145)**2) + 1 / sqrt((m.x21 - m.x36)
    **2 + (m.x76 - m.x91)**2 + (m.x131 - m.x146)**2) + 1 / sqrt((m.x21 - m.x37)
    **2 + (m.x76 - m.x92)**2 + (m.x131 - m.x147)**2) + 1 / sqrt((m.x21 - m.x38)
    **2 + (m.x76 - m.x93)**2 + (m.x131 - m.x148)**2) + 1 / sqrt((m.x21 - m.x39)
    **2 + (m.x76 - m.x94)**2 + (m.x131 - m.x149)**2) + 1 / sqrt((m.x21 - m.x40)
    **2 + (m.x76 - m.x95)**2 + (m.x131 - m.x150)**2) + 1 / sqrt((m.x21 - m.x41)
    **2 + (m.x76 - m.x96)**2 + (m.x131 - m.x151)**2) + 1 / sqrt((m.x21 - m.x42)
    **2 + (m.x76 - m.x97)**2 + (m.x131 - m.x152)**2) + 1 / sqrt((m.x21 - m.x43)
    **2 + (m.x76 - m.x98)**2 + (m.x131 - m.x153)**2) + 1 / sqrt((m.x21 - m.x44)
    **2 + (m.x76 - m.x99)**2 + (m.x131 - m.x154)**2) + 1 / sqrt((m.x21 - m.x45)
    **2 + (m.x76 - m.x100)**2 + (m.x131 - m.x155)**2) + 1 / sqrt((m.x21 - m.x46)
    **2 + (m.x76 - m.x101)**2 + (m.x131 - m.x156)**2) + 1 / sqrt((m.x21 - m.x47)
    **2 + (m.x76 - m.x102)**2 + (m.x131 - m.x157)**2) + 1 / sqrt((m.x21 - m.x48)
    **2 + (m.x76 - m.x103)**2 + (m.x131 - m.x158)**2) + 1 / sqrt((m.x21 - m.x49)
    **2 + (m.x76 - m.x104)**2 + (m.x131 - m.x159)**2) + 1 / sqrt((m.x21 - m.x50)
    **2 + (m.x76 - m.x105)**2 + (m.x131 - m.x160)**2) + 1 / sqrt((m.x21 - m.x51)
    **2 + (m.x76 - m.x106)**2 + (m.x131 - m.x161)**2) + 1 / sqrt((m.x21 - m.x52)
    **2 + (m.x76 - m.x107)**2 + (m.x131 - m.x162)**2) + 1 / sqrt((m.x21 - m.x53)
    **2 + (m.x76 - m.x108)**2 + (m.x131 - m.x163)**2) + 1 / sqrt((m.x21 - m.x54)
    **2 + (m.x76 - m.x109)**2 + (m.x131 - m.x164)**2) + 1 / sqrt((m.x21 - m.x55)
    **2 + (m.x76 - m.x110)**2 + (m.x131 - m.x165)**2) + 1 / sqrt((m.x22 - m.x23)
    **2 + (m.x77 - m.x78)**2 + (m.x132 - m.x133)**2) + 1 / sqrt((m.x22 - m.x24)
    **2 + (m.x77 - m.x79)**2 + (m.x132 - m.x134)**2) + 1 / sqrt((m.x22 - m.x25)
    **2 + (m.x77 - m.x80)**2 + (m.x132 - m.x135)**2) + 1 / sqrt((m.x22 - m.x26)
    **2 + (m.x77 - m.x81)**2 + (m.x132 - m.x136)**2) + 1 / sqrt((m.x22 - m.x27)
    **2 + (m.x77 - m.x82)**2 + (m.x132 - m.x137)**2) + 1 / sqrt((m.x22 - m.x28)
    **2 + (m.x77 - m.x83)**2 + (m.x132 - m.x138)**2) + 1 / sqrt((m.x22 - m.x29)
    **2 + (m.x77 - m.x84)**2 + (m.x132 - m.x139)**2) + 1 / sqrt((m.x22 - m.x30)
    **2 + (m.x77 - m.x85)**2 + (m.x132 - m.x140)**2) + 1 / sqrt((m.x22 - m.x31)
    **2 + (m.x77 - m.x86)**2 + (m.x132 - m.x141)**2) + 1 / sqrt((m.x22 - m.x32)
    **2 + (m.x77 - m.x87)**2 + (m.x132 - m.x142)**2) + 1 / sqrt((m.x22 - m.x33)
    **2 + (m.x77 - m.x88)**2 + (m.x132 - m.x143)**2) + 1 / sqrt((m.x22 - m.x34)
    **2 + (m.x77 - m.x89)**2 + (m.x132 - m.x144)**2) + 1 / sqrt((m.x22 - m.x35)
    **2 + (m.x77 - m.x90)**2 + (m.x132 - m.x145)**2) + 1 / sqrt((m.x22 - m.x36)
    **2 + (m.x77 - m.x91)**2 + (m.x132 - m.x146)**2) + 1 / sqrt((m.x22 - m.x37)
    **2 + (m.x77 - m.x92)**2 + (m.x132 - m.x147)**2) + 1 / sqrt((m.x22 - m.x38)
    **2 + (m.x77 - m.x93)**2 + (m.x132 - m.x148)**2) + 1 / sqrt((m.x22 - m.x39)
    **2 + (m.x77 - m.x94)**2 + (m.x132 - m.x149)**2) + 1 / sqrt((m.x22 - m.x40)
    **2 + (m.x77 - m.x95)**2 + (m.x132 - m.x150)**2) + 1 / sqrt((m.x22 - m.x41)
    **2 + (m.x77 - m.x96)**2 + (m.x132 - m.x151)**2) + 1 / sqrt((m.x22 - m.x42)
    **2 + (m.x77 - m.x97)**2 + (m.x132 - m.x152)**2) + 1 / sqrt((m.x22 - m.x43)
    **2 + (m.x77 - m.x98)**2 + (m.x132 - m.x153)**2) + 1 / sqrt((m.x22 - m.x44)
    **2 + (m.x77 - m.x99)**2 + (m.x132 - m.x154)**2) + 1 / sqrt((m.x22 - m.x45)
    **2 + (m.x77 - m.x100)**2 + (m.x132 - m.x155)**2) + 1 / sqrt((m.x22 - m.x46)
    **2 + (m.x77 - m.x101)**2 + (m.x132 - m.x156)**2) + 1 / sqrt((m.x22 - m.x47)
    **2 + (m.x77 - m.x102)**2 + (m.x132 - m.x157)**2) + 1 / sqrt((m.x22 - m.x48)
    **2 + (m.x77 - m.x103)**2 + (m.x132 - m.x158)**2) + 1 / sqrt((m.x22 - m.x49)
    **2 + (m.x77 - m.x104)**2 + (m.x132 - m.x159)**2) + 1 / sqrt((m.x22 - m.x50)
    **2 + (m.x77 - m.x105)**2 + (m.x132 - m.x160)**2) + 1 / sqrt((m.x22 - m.x51)
    **2 + (m.x77 - m.x106)**2 + (m.x132 - m.x161)**2) + 1 / sqrt((m.x22 - m.x52)
    **2 + (m.x77 - m.x107)**2 + (m.x132 - m.x162)**2) + 1 / sqrt((m.x22 - m.x53)
    **2 + (m.x77 - m.x108)**2 + (m.x132 - m.x163)**2) + 1 / sqrt((m.x22 - m.x54)
    **2 + (m.x77 - m.x109)**2 + (m.x132 - m.x164)**2) + 1 / sqrt((m.x22 - m.x55)
    **2 + (m.x77 - m.x110)**2 + (m.x132 - m.x165)**2) + 1 / sqrt((m.x23 - m.x24)
    **2 + (m.x78 - m.x79)**2 + (m.x133 - m.x134)**2) + 1 / sqrt((m.x23 - m.x25)
    **2 + (m.x78 - m.x80)**2 + (m.x133 - m.x135)**2) + 1 / sqrt((m.x23 - m.x26)
    **2 + (m.x78 - m.x81)**2 + (m.x133 - m.x136)**2) + 1 / sqrt((m.x23 - m.x27)
    **2 + (m.x78 - m.x82)**2 + (m.x133 - m.x137)**2) + 1 / sqrt((m.x23 - m.x28)
    **2 + (m.x78 - m.x83)**2 + (m.x133 - m.x138)**2) + 1 / sqrt((m.x23 - m.x29)
    **2 + (m.x78 - m.x84)**2 + (m.x133 - m.x139)**2) + 1 / sqrt((m.x23 - m.x30)
    **2 + (m.x78 - m.x85)**2 + (m.x133 - m.x140)**2) + 1 / sqrt((m.x23 - m.x31)
    **2 + (m.x78 - m.x86)**2 + (m.x133 - m.x141)**2) + 1 / sqrt((m.x23 - m.x32)
    **2 + (m.x78 - m.x87)**2 + (m.x133 - m.x142)**2) + 1 / sqrt((m.x23 - m.x33)
    **2 + (m.x78 - m.x88)**2 + (m.x133 - m.x143)**2) + 1 / sqrt((m.x23 - m.x34)
    **2 + (m.x78 - m.x89)**2 + (m.x133 - m.x144)**2) + 1 / sqrt((m.x23 - m.x35)
    **2 + (m.x78 - m.x90)**2 + (m.x133 - m.x145)**2) + 1 / sqrt((m.x23 - m.x36)
    **2 + (m.x78 - m.x91)**2 + (m.x133 - m.x146)**2) + 1 / sqrt((m.x23 - m.x37)
    **2 + (m.x78 - m.x92)**2 + (m.x133 - m.x147)**2) + 1 / sqrt((m.x23 - m.x38)
    **2 + (m.x78 - m.x93)**2 + (m.x133 - m.x148)**2) + 1 / sqrt((m.x23 - m.x39)
    **2 + (m.x78 - m.x94)**2 + (m.x133 - m.x149)**2) + 1 / sqrt((m.x23 - m.x40)
    **2 + (m.x78 - m.x95)**2 + (m.x133 - m.x150)**2) + 1 / sqrt((m.x23 - m.x41)
    **2 + (m.x78 - m.x96)**2 + (m.x133 - m.x151)**2) + 1 / sqrt((m.x23 - m.x42)
    **2 + (m.x78 - m.x97)**2 + (m.x133 - m.x152)**2) + 1 / sqrt((m.x23 - m.x43)
    **2 + (m.x78 - m.x98)**2 + (m.x133 - m.x153)**2) + 1 / sqrt((m.x23 - m.x44)
    **2 + (m.x78 - m.x99)**2 + (m.x133 - m.x154)**2) + 1 / sqrt((m.x23 - m.x45)
    **2 + (m.x78 - m.x100)**2 + (m.x133 - m.x155)**2) + 1 / sqrt((m.x23 - m.x46)
    **2 + (m.x78 - m.x101)**2 + (m.x133 - m.x156)**2) + 1 / sqrt((m.x23 - m.x47)
    **2 + (m.x78 - m.x102)**2 + (m.x133 - m.x157)**2) + 1 / sqrt((m.x23 - m.x48)
    **2 + (m.x78 - m.x103)**2 + (m.x133 - m.x158)**2) + 1 / sqrt((m.x23 - m.x49)
    **2 + (m.x78 - m.x104)**2 + (m.x133 - m.x159)**2) + 1 / sqrt((m.x23 - m.x50)
    **2 + (m.x78 - m.x105)**2 + (m.x133 - m.x160)**2) + 1 / sqrt((m.x23 - m.x51)
    **2 + (m.x78 - m.x106)**2 + (m.x133 - m.x161)**2) + 1 / sqrt((m.x23 - m.x52)
    **2 + (m.x78 - m.x107)**2 + (m.x133 - m.x162)**2) + 1 / sqrt((m.x23 - m.x53)
    **2 + (m.x78 - m.x108)**2 + (m.x133 - m.x163)**2) + 1 / sqrt((m.x23 - m.x54)
    **2 + (m.x78 - m.x109)**2 + (m.x133 - m.x164)**2) + 1 / sqrt((m.x23 - m.x55)
    **2 + (m.x78 - m.x110)**2 + (m.x133 - m.x165)**2) + 1 / sqrt((m.x24 - m.x25)
    **2 + (m.x79 - m.x80)**2 + (m.x134 - m.x135)**2) + 1 / sqrt((m.x24 - m.x26)
    **2 + (m.x79 - m.x81)**2 + (m.x134 - m.x136)**2) + 1 / sqrt((m.x24 - m.x27)
    **2 + (m.x79 - m.x82)**2 + (m.x134 - m.x137)**2) + 1 / sqrt((m.x24 - m.x28)
    **2 + (m.x79 - m.x83)**2 + (m.x134 - m.x138)**2) + 1 / sqrt((m.x24 - m.x29)
    **2 + (m.x79 - m.x84)**2 + (m.x134 - m.x139)**2) + 1 / sqrt((m.x24 - m.x30)
    **2 + (m.x79 - m.x85)**2 + (m.x134 - m.x140)**2) + 1 / sqrt((m.x24 - m.x31)
    **2 + (m.x79 - m.x86)**2 + (m.x134 - m.x141)**2) + 1 / sqrt((m.x24 - m.x32)
    **2 + (m.x79 - m.x87)**2 + (m.x134 - m.x142)**2) + 1 / sqrt((m.x24 - m.x33)
    **2 + (m.x79 - m.x88)**2 + (m.x134 - m.x143)**2) + 1 / sqrt((m.x24 - m.x34)
    **2 + (m.x79 - m.x89)**2 + (m.x134 - m.x144)**2) + 1 / sqrt((m.x24 - m.x35)
    **2 + (m.x79 - m.x90)**2 + (m.x134 - m.x145)**2) + 1 / sqrt((m.x24 - m.x36)
    **2 + (m.x79 - m.x91)**2 + (m.x134 - m.x146)**2) + 1 / sqrt((m.x24 - m.x37)
    **2 + (m.x79 - m.x92)**2 + (m.x134 - m.x147)**2) + 1 / sqrt((m.x24 - m.x38)
    **2 + (m.x79 - m.x93)**2 + (m.x134 - m.x148)**2) + 1 / sqrt((m.x24 - m.x39)
    **2 + (m.x79 - m.x94)**2 + (m.x134 - m.x149)**2) + 1 / sqrt((m.x24 - m.x40)
    **2 + (m.x79 - m.x95)**2 + (m.x134 - m.x150)**2) + 1 / sqrt((m.x24 - m.x41)
    **2 + (m.x79 - m.x96)**2 + (m.x134 - m.x151)**2) + 1 / sqrt((m.x24 - m.x42)
    **2 + (m.x79 - m.x97)**2 + (m.x134 - m.x152)**2) + 1 / sqrt((m.x24 - m.x43)
    **2 + (m.x79 - m.x98)**2 + (m.x134 - m.x153)**2) + 1 / sqrt((m.x24 - m.x44)
    **2 + (m.x79 - m.x99)**2 + (m.x134 - m.x154)**2) + 1 / sqrt((m.x24 - m.x45)
    **2 + (m.x79 - m.x100)**2 + (m.x134 - m.x155)**2) + 1 / sqrt((m.x24 - m.x46)
    **2 + (m.x79 - m.x101)**2 + (m.x134 - m.x156)**2) + 1 / sqrt((m.x24 - m.x47)
    **2 + (m.x79 - m.x102)**2 + (m.x134 - m.x157)**2) + 1 / sqrt((m.x24 - m.x48)
    **2 + (m.x79 - m.x103)**2 + (m.x134 - m.x158)**2) + 1 / sqrt((m.x24 - m.x49)
    **2 + (m.x79 - m.x104)**2 + (m.x134 - m.x159)**2) + 1 / sqrt((m.x24 - m.x50)
    **2 + (m.x79 - m.x105)**2 + (m.x134 - m.x160)**2) + 1 / sqrt((m.x24 - m.x51)
    **2 + (m.x79 - m.x106)**2 + (m.x134 - m.x161)**2) + 1 / sqrt((m.x24 - m.x52)
    **2 + (m.x79 - m.x107)**2 + (m.x134 - m.x162)**2) + 1 / sqrt((m.x24 - m.x53)
    **2 + (m.x79 - m.x108)**2 + (m.x134 - m.x163)**2) + 1 / sqrt((m.x24 - m.x54)
    **2 + (m.x79 - m.x109)**2 + (m.x134 - m.x164)**2) + 1 / sqrt((m.x24 - m.x55)
    **2 + (m.x79 - m.x110)**2 + (m.x134 - m.x165)**2) + 1 / sqrt((m.x25 - m.x26)
    **2 + (m.x80 - m.x81)**2 + (m.x135 - m.x136)**2) + 1 / sqrt((m.x25 - m.x27)
    **2 + (m.x80 - m.x82)**2 + (m.x135 - m.x137)**2) + 1 / sqrt((m.x25 - m.x28)
    **2 + (m.x80 - m.x83)**2 + (m.x135 - m.x138)**2) + 1 / sqrt((m.x25 - m.x29)
    **2 + (m.x80 - m.x84)**2 + (m.x135 - m.x139)**2) + 1 / sqrt((m.x25 - m.x30)
    **2 + (m.x80 - m.x85)**2 + (m.x135 - m.x140)**2) + 1 / sqrt((m.x25 - m.x31)
    **2 + (m.x80 - m.x86)**2 + (m.x135 - m.x141)**2) + 1 / sqrt((m.x25 - m.x32)
    **2 + (m.x80 - m.x87)**2 + (m.x135 - m.x142)**2) + 1 / sqrt((m.x25 - m.x33)
    **2 + (m.x80 - m.x88)**2 + (m.x135 - m.x143)**2) + 1 / sqrt((m.x25 - m.x34)
    **2 + (m.x80 - m.x89)**2 + (m.x135 - m.x144)**2) + 1 / sqrt((m.x25 - m.x35)
    **2 + (m.x80 - m.x90)**2 + (m.x135 - m.x145)**2) + 1 / sqrt((m.x25 - m.x36)
    **2 + (m.x80 - m.x91)**2 + (m.x135 - m.x146)**2) + 1 / sqrt((m.x25 - m.x37)
    **2 + (m.x80 - m.x92)**2 + (m.x135 - m.x147)**2) + 1 / sqrt((m.x25 - m.x38)
    **2 + (m.x80 - m.x93)**2 + (m.x135 - m.x148)**2) + 1 / sqrt((m.x25 - m.x39)
    **2 + (m.x80 - m.x94)**2 + (m.x135 - m.x149)**2) + 1 / sqrt((m.x25 - m.x40)
    **2 + (m.x80 - m.x95)**2 + (m.x135 - m.x150)**2) + 1 / sqrt((m.x25 - m.x41)
    **2 + (m.x80 - m.x96)**2 + (m.x135 - m.x151)**2) + 1 / sqrt((m.x25 - m.x42)
    **2 + (m.x80 - m.x97)**2 + (m.x135 - m.x152)**2) + 1 / sqrt((m.x25 - m.x43)
    **2 + (m.x80 - m.x98)**2 + (m.x135 - m.x153)**2) + 1 / sqrt((m.x25 - m.x44)
    **2 + (m.x80 - m.x99)**2 + (m.x135 - m.x154)**2) + 1 / sqrt((m.x25 - m.x45)
    **2 + (m.x80 - m.x100)**2 + (m.x135 - m.x155)**2) + 1 / sqrt((m.x25 - m.x46)
    **2 + (m.x80 - m.x101)**2 + (m.x135 - m.x156)**2) + 1 / sqrt((m.x25 - m.x47)
    **2 + (m.x80 - m.x102)**2 + (m.x135 - m.x157)**2) + 1 / sqrt((m.x25 - m.x48)
    **2 + (m.x80 - m.x103)**2 + (m.x135 - m.x158)**2) + 1 / sqrt((m.x25 - m.x49)
    **2 + (m.x80 - m.x104)**2 + (m.x135 - m.x159)**2) + 1 / sqrt((m.x25 - m.x50)
    **2 + (m.x80 - m.x105)**2 + (m.x135 - m.x160)**2) + 1 / sqrt((m.x25 - m.x51)
    **2 + (m.x80 - m.x106)**2 + (m.x135 - m.x161)**2) + 1 / sqrt((m.x25 - m.x52)
    **2 + (m.x80 - m.x107)**2 + (m.x135 - m.x162)**2) + 1 / sqrt((m.x25 - m.x53)
    **2 + (m.x80 - m.x108)**2 + (m.x135 - m.x163)**2) + 1 / sqrt((m.x25 - m.x54)
    **2 + (m.x80 - m.x109)**2 + (m.x135 - m.x164)**2) + 1 / sqrt((m.x25 - m.x55)
    **2 + (m.x80 - m.x110)**2 + (m.x135 - m.x165)**2) + 1 / sqrt((m.x26 - m.x27)
    **2 + (m.x81 - m.x82)**2 + (m.x136 - m.x137)**2) + 1 / sqrt((m.x26 - m.x28)
    **2 + (m.x81 - m.x83)**2 + (m.x136 - m.x138)**2) + 1 / sqrt((m.x26 - m.x29)
    **2 + (m.x81 - m.x84)**2 + (m.x136 - m.x139)**2) + 1 / sqrt((m.x26 - m.x30)
    **2 + (m.x81 - m.x85)**2 + (m.x136 - m.x140)**2) + 1 / sqrt((m.x26 - m.x31)
    **2 + (m.x81 - m.x86)**2 + (m.x136 - m.x141)**2) + 1 / sqrt((m.x26 - m.x32)
    **2 + (m.x81 - m.x87)**2 + (m.x136 - m.x142)**2) + 1 / sqrt((m.x26 - m.x33)
    **2 + (m.x81 - m.x88)**2 + (m.x136 - m.x143)**2) + 1 / sqrt((m.x26 - m.x34)
    **2 + (m.x81 - m.x89)**2 + (m.x136 - m.x144)**2) + 1 / sqrt((m.x26 - m.x35)
    **2 + (m.x81 - m.x90)**2 + (m.x136 - m.x145)**2) + 1 / sqrt((m.x26 - m.x36)
    **2 + (m.x81 - m.x91)**2 + (m.x136 - m.x146)**2) + 1 / sqrt((m.x26 - m.x37)
    **2 + (m.x81 - m.x92)**2 + (m.x136 - m.x147)**2) + 1 / sqrt((m.x26 - m.x38)
    **2 + (m.x81 - m.x93)**2 + (m.x136 - m.x148)**2) + 1 / sqrt((m.x26 - m.x39)
    **2 + (m.x81 - m.x94)**2 + (m.x136 - m.x149)**2) + 1 / sqrt((m.x26 - m.x40)
    **2 + (m.x81 - m.x95)**2 + (m.x136 - m.x150)**2) + 1 / sqrt((m.x26 - m.x41)
    **2 + (m.x81 - m.x96)**2 + (m.x136 - m.x151)**2) + 1 / sqrt((m.x26 - m.x42)
    **2 + (m.x81 - m.x97)**2 + (m.x136 - m.x152)**2) + 1 / sqrt((m.x26 - m.x43)
    **2 + (m.x81 - m.x98)**2 + (m.x136 - m.x153)**2) + 1 / sqrt((m.x26 - m.x44)
    **2 + (m.x81 - m.x99)**2 + (m.x136 - m.x154)**2) + 1 / sqrt((m.x26 - m.x45)
    **2 + (m.x81 - m.x100)**2 + (m.x136 - m.x155)**2) + 1 / sqrt((m.x26 - m.x46)
    **2 + (m.x81 - m.x101)**2 + (m.x136 - m.x156)**2) + 1 / sqrt((m.x26 - m.x47)
    **2 + (m.x81 - m.x102)**2 + (m.x136 - m.x157)**2) + 1 / sqrt((m.x26 - m.x48)
    **2 + (m.x81 - m.x103)**2 + (m.x136 - m.x158)**2) + 1 / sqrt((m.x26 - m.x49)
    **2 + (m.x81 - m.x104)**2 + (m.x136 - m.x159)**2) + 1 / sqrt((m.x26 - m.x50)
    **2 + (m.x81 - m.x105)**2 + (m.x136 - m.x160)**2) + 1 / sqrt((m.x26 - m.x51)
    **2 + (m.x81 - m.x106)**2 + (m.x136 - m.x161)**2) + 1 / sqrt((m.x26 - m.x52)
    **2 + (m.x81 - m.x107)**2 + (m.x136 - m.x162)**2) + 1 / sqrt((m.x26 - m.x53)
    **2 + (m.x81 - m.x108)**2 + (m.x136 - m.x163)**2) + 1 / sqrt((m.x26 - m.x54)
    **2 + (m.x81 - m.x109)**2 + (m.x136 - m.x164)**2) + 1 / sqrt((m.x26 - m.x55)
    **2 + (m.x81 - m.x110)**2 + (m.x136 - m.x165)**2) + 1 / sqrt((m.x27 - m.x28)
    **2 + (m.x82 - m.x83)**2 + (m.x137 - m.x138)**2) + 1 / sqrt((m.x27 - m.x29)
    **2 + (m.x82 - m.x84)**2 + (m.x137 - m.x139)**2) + 1 / sqrt((m.x27 - m.x30)
    **2 + (m.x82 - m.x85)**2 + (m.x137 - m.x140)**2) + 1 / sqrt((m.x27 - m.x31)
    **2 + (m.x82 - m.x86)**2 + (m.x137 - m.x141)**2) + 1 / sqrt((m.x27 - m.x32)
    **2 + (m.x82 - m.x87)**2 + (m.x137 - m.x142)**2) + 1 / sqrt((m.x27 - m.x33)
    **2 + (m.x82 - m.x88)**2 + (m.x137 - m.x143)**2) + 1 / sqrt((m.x27 - m.x34)
    **2 + (m.x82 - m.x89)**2 + (m.x137 - m.x144)**2) + 1 / sqrt((m.x27 - m.x35)
    **2 + (m.x82 - m.x90)**2 + (m.x137 - m.x145)**2) + 1 / sqrt((m.x27 - m.x36)
    **2 + (m.x82 - m.x91)**2 + (m.x137 - m.x146)**2) + 1 / sqrt((m.x27 - m.x37)
    **2 + (m.x82 - m.x92)**2 + (m.x137 - m.x147)**2) + 1 / sqrt((m.x27 - m.x38)
    **2 + (m.x82 - m.x93)**2 + (m.x137 - m.x148)**2) + 1 / sqrt((m.x27 - m.x39)
    **2 + (m.x82 - m.x94)**2 + (m.x137 - m.x149)**2) + 1 / sqrt((m.x27 - m.x40)
    **2 + (m.x82 - m.x95)**2 + (m.x137 - m.x150)**2) + 1 / sqrt((m.x27 - m.x41)
    **2 + (m.x82 - m.x96)**2 + (m.x137 - m.x151)**2) + 1 / sqrt((m.x27 - m.x42)
    **2 + (m.x82 - m.x97)**2 + (m.x137 - m.x152)**2) + 1 / sqrt((m.x27 - m.x43)
    **2 + (m.x82 - m.x98)**2 + (m.x137 - m.x153)**2) + 1 / sqrt((m.x27 - m.x44)
    **2 + (m.x82 - m.x99)**2 + (m.x137 - m.x154)**2) + 1 / sqrt((m.x27 - m.x45)
    **2 + (m.x82 - m.x100)**2 + (m.x137 - m.x155)**2) + 1 / sqrt((m.x27 - m.x46)
    **2 + (m.x82 - m.x101)**2 + (m.x137 - m.x156)**2) + 1 / sqrt((m.x27 - m.x47)
    **2 + (m.x82 - m.x102)**2 + (m.x137 - m.x157)**2) + 1 / sqrt((m.x27 - m.x48)
    **2 + (m.x82 - m.x103)**2 + (m.x137 - m.x158)**2) + 1 / sqrt((m.x27 - m.x49)
    **2 + (m.x82 - m.x104)**2 + (m.x137 - m.x159)**2) + 1 / sqrt((m.x27 - m.x50)
    **2 + (m.x82 - m.x105)**2 + (m.x137 - m.x160)**2) + 1 / sqrt((m.x27 - m.x51)
    **2 + (m.x82 - m.x106)**2 + (m.x137 - m.x161)**2) + 1 / sqrt((m.x27 - m.x52)
    **2 + (m.x82 - m.x107)**2 + (m.x137 - m.x162)**2) + 1 / sqrt((m.x27 - m.x53)
    **2 + (m.x82 - m.x108)**2 + (m.x137 - m.x163)**2) + 1 / sqrt((m.x27 - m.x54)
    **2 + (m.x82 - m.x109)**2 + (m.x137 - m.x164)**2) + 1 / sqrt((m.x27 - m.x55)
    **2 + (m.x82 - m.x110)**2 + (m.x137 - m.x165)**2) + 1 / sqrt((m.x28 - m.x29)
    **2 + (m.x83 - m.x84)**2 + (m.x138 - m.x139)**2) + 1 / sqrt((m.x28 - m.x30)
    **2 + (m.x83 - m.x85)**2 + (m.x138 - m.x140)**2) + 1 / sqrt((m.x28 - m.x31)
    **2 + (m.x83 - m.x86)**2 + (m.x138 - m.x141)**2) + 1 / sqrt((m.x28 - m.x32)
    **2 + (m.x83 - m.x87)**2 + (m.x138 - m.x142)**2) + 1 / sqrt((m.x28 - m.x33)
    **2 + (m.x83 - m.x88)**2 + (m.x138 - m.x143)**2) + 1 / sqrt((m.x28 - m.x34)
    **2 + (m.x83 - m.x89)**2 + (m.x138 - m.x144)**2) + 1 / sqrt((m.x28 - m.x35)
    **2 + (m.x83 - m.x90)**2 + (m.x138 - m.x145)**2) + 1 / sqrt((m.x28 - m.x36)
    **2 + (m.x83 - m.x91)**2 + (m.x138 - m.x146)**2) + 1 / sqrt((m.x28 - m.x37)
    **2 + (m.x83 - m.x92)**2 + (m.x138 - m.x147)**2) + 1 / sqrt((m.x28 - m.x38)
    **2 + (m.x83 - m.x93)**2 + (m.x138 - m.x148)**2) + 1 / sqrt((m.x28 - m.x39)
    **2 + (m.x83 - m.x94)**2 + (m.x138 - m.x149)**2) + 1 / sqrt((m.x28 - m.x40)
    **2 + (m.x83 - m.x95)**2 + (m.x138 - m.x150)**2) + 1 / sqrt((m.x28 - m.x41)
    **2 + (m.x83 - m.x96)**2 + (m.x138 - m.x151)**2) + 1 / sqrt((m.x28 - m.x42)
    **2 + (m.x83 - m.x97)**2 + (m.x138 - m.x152)**2) + 1 / sqrt((m.x28 - m.x43)
    **2 + (m.x83 - m.x98)**2 + (m.x138 - m.x153)**2) + 1 / sqrt((m.x28 - m.x44)
    **2 + (m.x83 - m.x99)**2 + (m.x138 - m.x154)**2) + 1 / sqrt((m.x28 - m.x45)
    **2 + (m.x83 - m.x100)**2 + (m.x138 - m.x155)**2) + 1 / sqrt((m.x28 - m.x46)
    **2 + (m.x83 - m.x101)**2 + (m.x138 - m.x156)**2) + 1 / sqrt((m.x28 - m.x47)
    **2 + (m.x83 - m.x102)**2 + (m.x138 - m.x157)**2) + 1 / sqrt((m.x28 - m.x48)
    **2 + (m.x83 - m.x103)**2 + (m.x138 - m.x158)**2) + 1 / sqrt((m.x28 - m.x49)
    **2 + (m.x83 - m.x104)**2 + (m.x138 - m.x159)**2) + 1 / sqrt((m.x28 - m.x50)
    **2 + (m.x83 - m.x105)**2 + (m.x138 - m.x160)**2) + 1 / sqrt((m.x28 - m.x51)
    **2 + (m.x83 - m.x106)**2 + (m.x138 - m.x161)**2) + 1 / sqrt((m.x28 - m.x52)
    **2 + (m.x83 - m.x107)**2 + (m.x138 - m.x162)**2) + 1 / sqrt((m.x28 - m.x53)
    **2 + (m.x83 - m.x108)**2 + (m.x138 - m.x163)**2) + 1 / sqrt((m.x28 - m.x54)
    **2 + (m.x83 - m.x109)**2 + (m.x138 - m.x164)**2) + 1 / sqrt((m.x28 - m.x55)
    **2 + (m.x83 - m.x110)**2 + (m.x138 - m.x165)**2) + 1 / sqrt((m.x29 - m.x30)
    **2 + (m.x84 - m.x85)**2 + (m.x139 - m.x140)**2) + 1 / sqrt((m.x29 - m.x31)
    **2 + (m.x84 - m.x86)**2 + (m.x139 - m.x141)**2) + 1 / sqrt((m.x29 - m.x32)
    **2 + (m.x84 - m.x87)**2 + (m.x139 - m.x142)**2) + 1 / sqrt((m.x29 - m.x33)
    **2 + (m.x84 - m.x88)**2 + (m.x139 - m.x143)**2) + 1 / sqrt((m.x29 - m.x34)
    **2 + (m.x84 - m.x89)**2 + (m.x139 - m.x144)**2) + 1 / sqrt((m.x29 - m.x35)
    **2 + (m.x84 - m.x90)**2 + (m.x139 - m.x145)**2) + 1 / sqrt((m.x29 - m.x36)
    **2 + (m.x84 - m.x91)**2 + (m.x139 - m.x146)**2) + 1 / sqrt((m.x29 - m.x37)
    **2 + (m.x84 - m.x92)**2 + (m.x139 - m.x147)**2) + 1 / sqrt((m.x29 - m.x38)
    **2 + (m.x84 - m.x93)**2 + (m.x139 - m.x148)**2) + 1 / sqrt((m.x29 - m.x39)
    **2 + (m.x84 - m.x94)**2 + (m.x139 - m.x149)**2) + 1 / sqrt((m.x29 - m.x40)
    **2 + (m.x84 - m.x95)**2 + (m.x139 - m.x150)**2) + 1 / sqrt((m.x29 - m.x41)
    **2 + (m.x84 - m.x96)**2 + (m.x139 - m.x151)**2) + 1 / sqrt((m.x29 - m.x42)
    **2 + (m.x84 - m.x97)**2 + (m.x139 - m.x152)**2) + 1 / sqrt((m.x29 - m.x43)
    **2 + (m.x84 - m.x98)**2 + (m.x139 - m.x153)**2) + 1 / sqrt((m.x29 - m.x44)
    **2 + (m.x84 - m.x99)**2 + (m.x139 - m.x154)**2) + 1 / sqrt((m.x29 - m.x45)
    **2 + (m.x84 - m.x100)**2 + (m.x139 - m.x155)**2) + 1 / sqrt((m.x29 - m.x46)
    **2 + (m.x84 - m.x101)**2 + (m.x139 - m.x156)**2) + 1 / sqrt((m.x29 - m.x47)
    **2 + (m.x84 - m.x102)**2 + (m.x139 - m.x157)**2) + 1 / sqrt((m.x29 - m.x48)
    **2 + (m.x84 - m.x103)**2 + (m.x139 - m.x158)**2) + 1 / sqrt((m.x29 - m.x49)
    **2 + (m.x84 - m.x104)**2 + (m.x139 - m.x159)**2) + 1 / sqrt((m.x29 - m.x50)
    **2 + (m.x84 - m.x105)**2 + (m.x139 - m.x160)**2) + 1 / sqrt((m.x29 - m.x51)
    **2 + (m.x84 - m.x106)**2 + (m.x139 - m.x161)**2) + 1 / sqrt((m.x29 - m.x52)
    **2 + (m.x84 - m.x107)**2 + (m.x139 - m.x162)**2) + 1 / sqrt((m.x29 - m.x53)
    **2 + (m.x84 - m.x108)**2 + (m.x139 - m.x163)**2) + 1 / sqrt((m.x29 - m.x54)
    **2 + (m.x84 - m.x109)**2 + (m.x139 - m.x164)**2) + 1 / sqrt((m.x29 - m.x55)
    **2 + (m.x84 - m.x110)**2 + (m.x139 - m.x165)**2) + 1 / sqrt((m.x30 - m.x31)
    **2 + (m.x85 - m.x86)**2 + (m.x140 - m.x141)**2) + 1 / sqrt((m.x30 - m.x32)
    **2 + (m.x85 - m.x87)**2 + (m.x140 - m.x142)**2) + 1 / sqrt((m.x30 - m.x33)
    **2 + (m.x85 - m.x88)**2 + (m.x140 - m.x143)**2) + 1 / sqrt((m.x30 - m.x34)
    **2 + (m.x85 - m.x89)**2 + (m.x140 - m.x144)**2) + 1 / sqrt((m.x30 - m.x35)
    **2 + (m.x85 - m.x90)**2 + (m.x140 - m.x145)**2) + 1 / sqrt((m.x30 - m.x36)
    **2 + (m.x85 - m.x91)**2 + (m.x140 - m.x146)**2) + 1 / sqrt((m.x30 - m.x37)
    **2 + (m.x85 - m.x92)**2 + (m.x140 - m.x147)**2) + 1 / sqrt((m.x30 - m.x38)
    **2 + (m.x85 - m.x93)**2 + (m.x140 - m.x148)**2) + 1 / sqrt((m.x30 - m.x39)
    **2 + (m.x85 - m.x94)**2 + (m.x140 - m.x149)**2) + 1 / sqrt((m.x30 - m.x40)
    **2 + (m.x85 - m.x95)**2 + (m.x140 - m.x150)**2) + 1 / sqrt((m.x30 - m.x41)
    **2 + (m.x85 - m.x96)**2 + (m.x140 - m.x151)**2) + 1 / sqrt((m.x30 - m.x42)
    **2 + (m.x85 - m.x97)**2 + (m.x140 - m.x152)**2) + 1 / sqrt((m.x30 - m.x43)
    **2 + (m.x85 - m.x98)**2 + (m.x140 - m.x153)**2) + 1 / sqrt((m.x30 - m.x44)
    **2 + (m.x85 - m.x99)**2 + (m.x140 - m.x154)**2) + 1 / sqrt((m.x30 - m.x45)
    **2 + (m.x85 - m.x100)**2 + (m.x140 - m.x155)**2) + 1 / sqrt((m.x30 - m.x46)
    **2 + (m.x85 - m.x101)**2 + (m.x140 - m.x156)**2) + 1 / sqrt((m.x30 - m.x47)
    **2 + (m.x85 - m.x102)**2 + (m.x140 - m.x157)**2) + 1 / sqrt((m.x30 - m.x48)
    **2 + (m.x85 - m.x103)**2 + (m.x140 - m.x158)**2) + 1 / sqrt((m.x30 - m.x49)
    **2 + (m.x85 - m.x104)**2 + (m.x140 - m.x159)**2) + 1 / sqrt((m.x30 - m.x50)
    **2 + (m.x85 - m.x105)**2 + (m.x140 - m.x160)**2) + 1 / sqrt((m.x30 - m.x51)
    **2 + (m.x85 - m.x106)**2 + (m.x140 - m.x161)**2) + 1 / sqrt((m.x30 - m.x52)
    **2 + (m.x85 - m.x107)**2 + (m.x140 - m.x162)**2) + 1 / sqrt((m.x30 - m.x53)
    **2 + (m.x85 - m.x108)**2 + (m.x140 - m.x163)**2) + 1 / sqrt((m.x30 - m.x54)
    **2 + (m.x85 - m.x109)**2 + (m.x140 - m.x164)**2) + 1 / sqrt((m.x30 - m.x55)
    **2 + (m.x85 - m.x110)**2 + (m.x140 - m.x165)**2) + 1 / sqrt((m.x31 - m.x32)
    **2 + (m.x86 - m.x87)**2 + (m.x141 - m.x142)**2) + 1 / sqrt((m.x31 - m.x33)
    **2 + (m.x86 - m.x88)**2 + (m.x141 - m.x143)**2) + 1 / sqrt((m.x31 - m.x34)
    **2 + (m.x86 - m.x89)**2 + (m.x141 - m.x144)**2) + 1 / sqrt((m.x31 - m.x35)
    **2 + (m.x86 - m.x90)**2 + (m.x141 - m.x145)**2) + 1 / sqrt((m.x31 - m.x36)
    **2 + (m.x86 - m.x91)**2 + (m.x141 - m.x146)**2) + 1 / sqrt((m.x31 - m.x37)
    **2 + (m.x86 - m.x92)**2 + (m.x141 - m.x147)**2) + 1 / sqrt((m.x31 - m.x38)
    **2 + (m.x86 - m.x93)**2 + (m.x141 - m.x148)**2) + 1 / sqrt((m.x31 - m.x39)
    **2 + (m.x86 - m.x94)**2 + (m.x141 - m.x149)**2) + 1 / sqrt((m.x31 - m.x40)
    **2 + (m.x86 - m.x95)**2 + (m.x141 - m.x150)**2) + 1 / sqrt((m.x31 - m.x41)
    **2 + (m.x86 - m.x96)**2 + (m.x141 - m.x151)**2) + 1 / sqrt((m.x31 - m.x42)
    **2 + (m.x86 - m.x97)**2 + (m.x141 - m.x152)**2) + 1 / sqrt((m.x31 - m.x43)
    **2 + (m.x86 - m.x98)**2 + (m.x141 - m.x153)**2) + 1 / sqrt((m.x31 - m.x44)
    **2 + (m.x86 - m.x99)**2 + (m.x141 - m.x154)**2) + 1 / sqrt((m.x31 - m.x45)
    **2 + (m.x86 - m.x100)**2 + (m.x141 - m.x155)**2) + 1 / sqrt((m.x31 - m.x46)
    **2 + (m.x86 - m.x101)**2 + (m.x141 - m.x156)**2) + 1 / sqrt((m.x31 - m.x47)
    **2 + (m.x86 - m.x102)**2 + (m.x141 - m.x157)**2) + 1 / sqrt((m.x31 - m.x48)
    **2 + (m.x86 - m.x103)**2 + (m.x141 - m.x158)**2) + 1 / sqrt((m.x31 - m.x49)
    **2 + (m.x86 - m.x104)**2 + (m.x141 - m.x159)**2) + 1 / sqrt((m.x31 - m.x50)
    **2 + (m.x86 - m.x105)**2 + (m.x141 - m.x160)**2) + 1 / sqrt((m.x31 - m.x51)
    **2 + (m.x86 - m.x106)**2 + (m.x141 - m.x161)**2) + 1 / sqrt((m.x31 - m.x52)
    **2 + (m.x86 - m.x107)**2 + (m.x141 - m.x162)**2) + 1 / sqrt((m.x31 - m.x53)
    **2 + (m.x86 - m.x108)**2 + (m.x141 - m.x163)**2) + 1 / sqrt((m.x31 - m.x54)
    **2 + (m.x86 - m.x109)**2 + (m.x141 - m.x164)**2) + 1 / sqrt((m.x31 - m.x55)
    **2 + (m.x86 - m.x110)**2 + (m.x141 - m.x165)**2) + 1 / sqrt((m.x32 - m.x33)
    **2 + (m.x87 - m.x88)**2 + (m.x142 - m.x143)**2) + 1 / sqrt((m.x32 - m.x34)
    **2 + (m.x87 - m.x89)**2 + (m.x142 - m.x144)**2) + 1 / sqrt((m.x32 - m.x35)
    **2 + (m.x87 - m.x90)**2 + (m.x142 - m.x145)**2) + 1 / sqrt((m.x32 - m.x36)
    **2 + (m.x87 - m.x91)**2 + (m.x142 - m.x146)**2) + 1 / sqrt((m.x32 - m.x37)
    **2 + (m.x87 - m.x92)**2 + (m.x142 - m.x147)**2) + 1 / sqrt((m.x32 - m.x38)
    **2 + (m.x87 - m.x93)**2 + (m.x142 - m.x148)**2) + 1 / sqrt((m.x32 - m.x39)
    **2 + (m.x87 - m.x94)**2 + (m.x142 - m.x149)**2) + 1 / sqrt((m.x32 - m.x40)
    **2 + (m.x87 - m.x95)**2 + (m.x142 - m.x150)**2) + 1 / sqrt((m.x32 - m.x41)
    **2 + (m.x87 - m.x96)**2 + (m.x142 - m.x151)**2) + 1 / sqrt((m.x32 - m.x42)
    **2 + (m.x87 - m.x97)**2 + (m.x142 - m.x152)**2) + 1 / sqrt((m.x32 - m.x43)
    **2 + (m.x87 - m.x98)**2 + (m.x142 - m.x153)**2) + 1 / sqrt((m.x32 - m.x44)
    **2 + (m.x87 - m.x99)**2 + (m.x142 - m.x154)**2) + 1 / sqrt((m.x32 - m.x45)
    **2 + (m.x87 - m.x100)**2 + (m.x142 - m.x155)**2) + 1 / sqrt((m.x32 - m.x46)
    **2 + (m.x87 - m.x101)**2 + (m.x142 - m.x156)**2) + 1 / sqrt((m.x32 - m.x47)
    **2 + (m.x87 - m.x102)**2 + (m.x142 - m.x157)**2) + 1 / sqrt((m.x32 - m.x48)
    **2 + (m.x87 - m.x103)**2 + (m.x142 - m.x158)**2) + 1 / sqrt((m.x32 - m.x49)
    **2 + (m.x87 - m.x104)**2 + (m.x142 - m.x159)**2) + 1 / sqrt((m.x32 - m.x50)
    **2 + (m.x87 - m.x105)**2 + (m.x142 - m.x160)**2) + 1 / sqrt((m.x32 - m.x51)
    **2 + (m.x87 - m.x106)**2 + (m.x142 - m.x161)**2) + 1 / sqrt((m.x32 - m.x52)
    **2 + (m.x87 - m.x107)**2 + (m.x142 - m.x162)**2) + 1 / sqrt((m.x32 - m.x53)
    **2 + (m.x87 - m.x108)**2 + (m.x142 - m.x163)**2) + 1 / sqrt((m.x32 - m.x54)
    **2 + (m.x87 - m.x109)**2 + (m.x142 - m.x164)**2) + 1 / sqrt((m.x32 - m.x55)
    **2 + (m.x87 - m.x110)**2 + (m.x142 - m.x165)**2) + 1 / sqrt((m.x33 - m.x34)
    **2 + (m.x88 - m.x89)**2 + (m.x143 - m.x144)**2) + 1 / sqrt((m.x33 - m.x35)
    **2 + (m.x88 - m.x90)**2 + (m.x143 - m.x145)**2) + 1 / sqrt((m.x33 - m.x36)
    **2 + (m.x88 - m.x91)**2 + (m.x143 - m.x146)**2) + 1 / sqrt((m.x33 - m.x37)
    **2 + (m.x88 - m.x92)**2 + (m.x143 - m.x147)**2) + 1 / sqrt((m.x33 - m.x38)
    **2 + (m.x88 - m.x93)**2 + (m.x143 - m.x148)**2) + 1 / sqrt((m.x33 - m.x39)
    **2 + (m.x88 - m.x94)**2 + (m.x143 - m.x149)**2) + 1 / sqrt((m.x33 - m.x40)
    **2 + (m.x88 - m.x95)**2 + (m.x143 - m.x150)**2) + 1 / sqrt((m.x33 - m.x41)
    **2 + (m.x88 - m.x96)**2 + (m.x143 - m.x151)**2) + 1 / sqrt((m.x33 - m.x42)
    **2 + (m.x88 - m.x97)**2 + (m.x143 - m.x152)**2) + 1 / sqrt((m.x33 - m.x43)
    **2 + (m.x88 - m.x98)**2 + (m.x143 - m.x153)**2) + 1 / sqrt((m.x33 - m.x44)
    **2 + (m.x88 - m.x99)**2 + (m.x143 - m.x154)**2) + 1 / sqrt((m.x33 - m.x45)
    **2 + (m.x88 - m.x100)**2 + (m.x143 - m.x155)**2) + 1 / sqrt((m.x33 - m.x46)
    **2 + (m.x88 - m.x101)**2 + (m.x143 - m.x156)**2) + 1 / sqrt((m.x33 - m.x47)
    **2 + (m.x88 - m.x102)**2 + (m.x143 - m.x157)**2) + 1 / sqrt((m.x33 - m.x48)
    **2 + (m.x88 - m.x103)**2 + (m.x143 - m.x158)**2) + 1 / sqrt((m.x33 - m.x49)
    **2 + (m.x88 - m.x104)**2 + (m.x143 - m.x159)**2) + 1 / sqrt((m.x33 - m.x50)
    **2 + (m.x88 - m.x105)**2 + (m.x143 - m.x160)**2) + 1 / sqrt((m.x33 - m.x51)
    **2 + (m.x88 - m.x106)**2 + (m.x143 - m.x161)**2) + 1 / sqrt((m.x33 - m.x52)
    **2 + (m.x88 - m.x107)**2 + (m.x143 - m.x162)**2) + 1 / sqrt((m.x33 - m.x53)
    **2 + (m.x88 - m.x108)**2 + (m.x143 - m.x163)**2) + 1 / sqrt((m.x33 - m.x54)
    **2 + (m.x88 - m.x109)**2 + (m.x143 - m.x164)**2) + 1 / sqrt((m.x33 - m.x55)
    **2 + (m.x88 - m.x110)**2 + (m.x143 - m.x165)**2) + 1 / sqrt((m.x34 - m.x35)
    **2 + (m.x89 - m.x90)**2 + (m.x144 - m.x145)**2) + 1 / sqrt((m.x34 - m.x36)
    **2 + (m.x89 - m.x91)**2 + (m.x144 - m.x146)**2) + 1 / sqrt((m.x34 - m.x37)
    **2 + (m.x89 - m.x92)**2 + (m.x144 - m.x147)**2) + 1 / sqrt((m.x34 - m.x38)
    **2 + (m.x89 - m.x93)**2 + (m.x144 - m.x148)**2) + 1 / sqrt((m.x34 - m.x39)
    **2 + (m.x89 - m.x94)**2 + (m.x144 - m.x149)**2) + 1 / sqrt((m.x34 - m.x40)
    **2 + (m.x89 - m.x95)**2 + (m.x144 - m.x150)**2) + 1 / sqrt((m.x34 - m.x41)
    **2 + (m.x89 - m.x96)**2 + (m.x144 - m.x151)**2) + 1 / sqrt((m.x34 - m.x42)
    **2 + (m.x89 - m.x97)**2 + (m.x144 - m.x152)**2) + 1 / sqrt((m.x34 - m.x43)
    **2 + (m.x89 - m.x98)**2 + (m.x144 - m.x153)**2) + 1 / sqrt((m.x34 - m.x44)
    **2 + (m.x89 - m.x99)**2 + (m.x144 - m.x154)**2) + 1 / sqrt((m.x34 - m.x45)
    **2 + (m.x89 - m.x100)**2 + (m.x144 - m.x155)**2) + 1 / sqrt((m.x34 - m.x46)
    **2 + (m.x89 - m.x101)**2 + (m.x144 - m.x156)**2) + 1 / sqrt((m.x34 - m.x47)
    **2 + (m.x89 - m.x102)**2 + (m.x144 - m.x157)**2) + 1 / sqrt((m.x34 - m.x48)
    **2 + (m.x89 - m.x103)**2 + (m.x144 - m.x158)**2) + 1 / sqrt((m.x34 - m.x49)
    **2 + (m.x89 - m.x104)**2 + (m.x144 - m.x159)**2) + 1 / sqrt((m.x34 - m.x50)
    **2 + (m.x89 - m.x105)**2 + (m.x144 - m.x160)**2) + 1 / sqrt((m.x34 - m.x51)
    **2 + (m.x89 - m.x106)**2 + (m.x144 - m.x161)**2) + 1 / sqrt((m.x34 - m.x52)
    **2 + (m.x89 - m.x107)**2 + (m.x144 - m.x162)**2) + 1 / sqrt((m.x34 - m.x53)
    **2 + (m.x89 - m.x108)**2 + (m.x144 - m.x163)**2) + 1 / sqrt((m.x34 - m.x54)
    **2 + (m.x89 - m.x109)**2 + (m.x144 - m.x164)**2) + 1 / sqrt((m.x34 - m.x55)
    **2 + (m.x89 - m.x110)**2 + (m.x144 - m.x165)**2) + 1 / sqrt((m.x35 - m.x36)
    **2 + (m.x90 - m.x91)**2 + (m.x145 - m.x146)**2) + 1 / sqrt((m.x35 - m.x37)
    **2 + (m.x90 - m.x92)**2 + (m.x145 - m.x147)**2) + 1 / sqrt((m.x35 - m.x38)
    **2 + (m.x90 - m.x93)**2 + (m.x145 - m.x148)**2) + 1 / sqrt((m.x35 - m.x39)
    **2 + (m.x90 - m.x94)**2 + (m.x145 - m.x149)**2) + 1 / sqrt((m.x35 - m.x40)
    **2 + (m.x90 - m.x95)**2 + (m.x145 - m.x150)**2) + 1 / sqrt((m.x35 - m.x41)
    **2 + (m.x90 - m.x96)**2 + (m.x145 - m.x151)**2) + 1 / sqrt((m.x35 - m.x42)
    **2 + (m.x90 - m.x97)**2 + (m.x145 - m.x152)**2) + 1 / sqrt((m.x35 - m.x43)
    **2 + (m.x90 - m.x98)**2 + (m.x145 - m.x153)**2) + 1 / sqrt((m.x35 - m.x44)
    **2 + (m.x90 - m.x99)**2 + (m.x145 - m.x154)**2) + 1 / sqrt((m.x35 - m.x45)
    **2 + (m.x90 - m.x100)**2 + (m.x145 - m.x155)**2) + 1 / sqrt((m.x35 - m.x46)
    **2 + (m.x90 - m.x101)**2 + (m.x145 - m.x156)**2) + 1 / sqrt((m.x35 - m.x47)
    **2 + (m.x90 - m.x102)**2 + (m.x145 - m.x157)**2) + 1 / sqrt((m.x35 - m.x48)
    **2 + (m.x90 - m.x103)**2 + (m.x145 - m.x158)**2) + 1 / sqrt((m.x35 - m.x49)
    **2 + (m.x90 - m.x104)**2 + (m.x145 - m.x159)**2) + 1 / sqrt((m.x35 - m.x50)
    **2 + (m.x90 - m.x105)**2 + (m.x145 - m.x160)**2) + 1 / sqrt((m.x35 - m.x51)
    **2 + (m.x90 - m.x106)**2 + (m.x145 - m.x161)**2) + 1 / sqrt((m.x35 - m.x52)
    **2 + (m.x90 - m.x107)**2 + (m.x145 - m.x162)**2) + 1 / sqrt((m.x35 - m.x53)
    **2 + (m.x90 - m.x108)**2 + (m.x145 - m.x163)**2) + 1 / sqrt((m.x35 - m.x54)
    **2 + (m.x90 - m.x109)**2 + (m.x145 - m.x164)**2) + 1 / sqrt((m.x35 - m.x55)
    **2 + (m.x90 - m.x110)**2 + (m.x145 - m.x165)**2) + 1 / sqrt((m.x36 - m.x37)
    **2 + (m.x91 - m.x92)**2 + (m.x146 - m.x147)**2) + 1 / sqrt((m.x36 - m.x38)
    **2 + (m.x91 - m.x93)**2 + (m.x146 - m.x148)**2) + 1 / sqrt((m.x36 - m.x39)
    **2 + (m.x91 - m.x94)**2 + (m.x146 - m.x149)**2) + 1 / sqrt((m.x36 - m.x40)
    **2 + (m.x91 - m.x95)**2 + (m.x146 - m.x150)**2) + 1 / sqrt((m.x36 - m.x41)
    **2 + (m.x91 - m.x96)**2 + (m.x146 - m.x151)**2) + 1 / sqrt((m.x36 - m.x42)
    **2 + (m.x91 - m.x97)**2 + (m.x146 - m.x152)**2) + 1 / sqrt((m.x36 - m.x43)
    **2 + (m.x91 - m.x98)**2 + (m.x146 - m.x153)**2) + 1 / sqrt((m.x36 - m.x44)
    **2 + (m.x91 - m.x99)**2 + (m.x146 - m.x154)**2) + 1 / sqrt((m.x36 - m.x45)
    **2 + (m.x91 - m.x100)**2 + (m.x146 - m.x155)**2) + 1 / sqrt((m.x36 - m.x46)
    **2 + (m.x91 - m.x101)**2 + (m.x146 - m.x156)**2) + 1 / sqrt((m.x36 - m.x47)
    **2 + (m.x91 - m.x102)**2 + (m.x146 - m.x157)**2) + 1 / sqrt((m.x36 - m.x48)
    **2 + (m.x91 - m.x103)**2 + (m.x146 - m.x158)**2) + 1 / sqrt((m.x36 - m.x49)
    **2 + (m.x91 - m.x104)**2 + (m.x146 - m.x159)**2) + 1 / sqrt((m.x36 - m.x50)
    **2 + (m.x91 - m.x105)**2 + (m.x146 - m.x160)**2) + 1 / sqrt((m.x36 - m.x51)
    **2 + (m.x91 - m.x106)**2 + (m.x146 - m.x161)**2) + 1 / sqrt((m.x36 - m.x52)
    **2 + (m.x91 - m.x107)**2 + (m.x146 - m.x162)**2) + 1 / sqrt((m.x36 - m.x53)
    **2 + (m.x91 - m.x108)**2 + (m.x146 - m.x163)**2) + 1 / sqrt((m.x36 - m.x54)
    **2 + (m.x91 - m.x109)**2 + (m.x146 - m.x164)**2) + 1 / sqrt((m.x36 - m.x55)
    **2 + (m.x91 - m.x110)**2 + (m.x146 - m.x165)**2) + 1 / sqrt((m.x37 - m.x38)
    **2 + (m.x92 - m.x93)**2 + (m.x147 - m.x148)**2) + 1 / sqrt((m.x37 - m.x39)
    **2 + (m.x92 - m.x94)**2 + (m.x147 - m.x149)**2) + 1 / sqrt((m.x37 - m.x40)
    **2 + (m.x92 - m.x95)**2 + (m.x147 - m.x150)**2) + 1 / sqrt((m.x37 - m.x41)
    **2 + (m.x92 - m.x96)**2 + (m.x147 - m.x151)**2) + 1 / sqrt((m.x37 - m.x42)
    **2 + (m.x92 - m.x97)**2 + (m.x147 - m.x152)**2) + 1 / sqrt((m.x37 - m.x43)
    **2 + (m.x92 - m.x98)**2 + (m.x147 - m.x153)**2) + 1 / sqrt((m.x37 - m.x44)
    **2 + (m.x92 - m.x99)**2 + (m.x147 - m.x154)**2) + 1 / sqrt((m.x37 - m.x45)
    **2 + (m.x92 - m.x100)**2 + (m.x147 - m.x155)**2) + 1 / sqrt((m.x37 - m.x46)
    **2 + (m.x92 - m.x101)**2 + (m.x147 - m.x156)**2) + 1 / sqrt((m.x37 - m.x47)
    **2 + (m.x92 - m.x102)**2 + (m.x147 - m.x157)**2) + 1 / sqrt((m.x37 - m.x48)
    **2 + (m.x92 - m.x103)**2 + (m.x147 - m.x158)**2) + 1 / sqrt((m.x37 - m.x49)
    **2 + (m.x92 - m.x104)**2 + (m.x147 - m.x159)**2) + 1 / sqrt((m.x37 - m.x50)
    **2 + (m.x92 - m.x105)**2 + (m.x147 - m.x160)**2) + 1 / sqrt((m.x37 - m.x51)
    **2 + (m.x92 - m.x106)**2 + (m.x147 - m.x161)**2) + 1 / sqrt((m.x37 - m.x52)
    **2 + (m.x92 - m.x107)**2 + (m.x147 - m.x162)**2) + 1 / sqrt((m.x37 - m.x53)
    **2 + (m.x92 - m.x108)**2 + (m.x147 - m.x163)**2) + 1 / sqrt((m.x37 - m.x54)
    **2 + (m.x92 - m.x109)**2 + (m.x147 - m.x164)**2) + 1 / sqrt((m.x37 - m.x55)
    **2 + (m.x92 - m.x110)**2 + (m.x147 - m.x165)**2) + 1 / sqrt((m.x38 - m.x39)
    **2 + (m.x93 - m.x94)**2 + (m.x148 - m.x149)**2) + 1 / sqrt((m.x38 - m.x40)
    **2 + (m.x93 - m.x95)**2 + (m.x148 - m.x150)**2) + 1 / sqrt((m.x38 - m.x41)
    **2 + (m.x93 - m.x96)**2 + (m.x148 - m.x151)**2) + 1 / sqrt((m.x38 - m.x42)
    **2 + (m.x93 - m.x97)**2 + (m.x148 - m.x152)**2) + 1 / sqrt((m.x38 - m.x43)
    **2 + (m.x93 - m.x98)**2 + (m.x148 - m.x153)**2) + 1 / sqrt((m.x38 - m.x44)
    **2 + (m.x93 - m.x99)**2 + (m.x148 - m.x154)**2) + 1 / sqrt((m.x38 - m.x45)
    **2 + (m.x93 - m.x100)**2 + (m.x148 - m.x155)**2) + 1 / sqrt((m.x38 - m.x46)
    **2 + (m.x93 - m.x101)**2 + (m.x148 - m.x156)**2) + 1 / sqrt((m.x38 - m.x47)
    **2 + (m.x93 - m.x102)**2 + (m.x148 - m.x157)**2) + 1 / sqrt((m.x38 - m.x48)
    **2 + (m.x93 - m.x103)**2 + (m.x148 - m.x158)**2) + 1 / sqrt((m.x38 - m.x49)
    **2 + (m.x93 - m.x104)**2 + (m.x148 - m.x159)**2) + 1 / sqrt((m.x38 - m.x50)
    **2 + (m.x93 - m.x105)**2 + (m.x148 - m.x160)**2) + 1 / sqrt((m.x38 - m.x51)
    **2 + (m.x93 - m.x106)**2 + (m.x148 - m.x161)**2) + 1 / sqrt((m.x38 - m.x52)
    **2 + (m.x93 - m.x107)**2 + (m.x148 - m.x162)**2) + 1 / sqrt((m.x38 - m.x53)
    **2 + (m.x93 - m.x108)**2 + (m.x148 - m.x163)**2) + 1 / sqrt((m.x38 - m.x54)
    **2 + (m.x93 - m.x109)**2 + (m.x148 - m.x164)**2) + 1 / sqrt((m.x38 - m.x55)
    **2 + (m.x93 - m.x110)**2 + (m.x148 - m.x165)**2) + 1 / sqrt((m.x39 - m.x40)
    **2 + (m.x94 - m.x95)**2 + (m.x149 - m.x150)**2) + 1 / sqrt((m.x39 - m.x41)
    **2 + (m.x94 - m.x96)**2 + (m.x149 - m.x151)**2) + 1 / sqrt((m.x39 - m.x42)
    **2 + (m.x94 - m.x97)**2 + (m.x149 - m.x152)**2) + 1 / sqrt((m.x39 - m.x43)
    **2 + (m.x94 - m.x98)**2 + (m.x149 - m.x153)**2) + 1 / sqrt((m.x39 - m.x44)
    **2 + (m.x94 - m.x99)**2 + (m.x149 - m.x154)**2) + 1 / sqrt((m.x39 - m.x45)
    **2 + (m.x94 - m.x100)**2 + (m.x149 - m.x155)**2) + 1 / sqrt((m.x39 - m.x46)
    **2 + (m.x94 - m.x101)**2 + (m.x149 - m.x156)**2) + 1 / sqrt((m.x39 - m.x47)
    **2 + (m.x94 - m.x102)**2 + (m.x149 - m.x157)**2) + 1 / sqrt((m.x39 - m.x48)
    **2 + (m.x94 - m.x103)**2 + (m.x149 - m.x158)**2) + 1 / sqrt((m.x39 - m.x49)
    **2 + (m.x94 - m.x104)**2 + (m.x149 - m.x159)**2) + 1 / sqrt((m.x39 - m.x50)
    **2 + (m.x94 - m.x105)**2 + (m.x149 - m.x160)**2) + 1 / sqrt((m.x39 - m.x51)
    **2 + (m.x94 - m.x106)**2 + (m.x149 - m.x161)**2) + 1 / sqrt((m.x39 - m.x52)
    **2 + (m.x94 - m.x107)**2 + (m.x149 - m.x162)**2) + 1 / sqrt((m.x39 - m.x53)
    **2 + (m.x94 - m.x108)**2 + (m.x149 - m.x163)**2) + 1 / sqrt((m.x39 - m.x54)
    **2 + (m.x94 - m.x109)**2 + (m.x149 - m.x164)**2) + 1 / sqrt((m.x39 - m.x55)
    **2 + (m.x94 - m.x110)**2 + (m.x149 - m.x165)**2) + 1 / sqrt((m.x40 - m.x41)
    **2 + (m.x95 - m.x96)**2 + (m.x150 - m.x151)**2) + 1 / sqrt((m.x40 - m.x42)
    **2 + (m.x95 - m.x97)**2 + (m.x150 - m.x152)**2) + 1 / sqrt((m.x40 - m.x43)
    **2 + (m.x95 - m.x98)**2 + (m.x150 - m.x153)**2) + 1 / sqrt((m.x40 - m.x44)
    **2 + (m.x95 - m.x99)**2 + (m.x150 - m.x154)**2) + 1 / sqrt((m.x40 - m.x45)
    **2 + (m.x95 - m.x100)**2 + (m.x150 - m.x155)**2) + 1 / sqrt((m.x40 - m.x46)
    **2 + (m.x95 - m.x101)**2 + (m.x150 - m.x156)**2) + 1 / sqrt((m.x40 - m.x47)
    **2 + (m.x95 - m.x102)**2 + (m.x150 - m.x157)**2) + 1 / sqrt((m.x40 - m.x48)
    **2 + (m.x95 - m.x103)**2 + (m.x150 - m.x158)**2) + 1 / sqrt((m.x40 - m.x49)
    **2 + (m.x95 - m.x104)**2 + (m.x150 - m.x159)**2) + 1 / sqrt((m.x40 - m.x50)
    **2 + (m.x95 - m.x105)**2 + (m.x150 - m.x160)**2) + 1 / sqrt((m.x40 - m.x51)
    **2 + (m.x95 - m.x106)**2 + (m.x150 - m.x161)**2) + 1 / sqrt((m.x40 - m.x52)
    **2 + (m.x95 - m.x107)**2 + (m.x150 - m.x162)**2) + 1 / sqrt((m.x40 - m.x53)
    **2 + (m.x95 - m.x108)**2 + (m.x150 - m.x163)**2) + 1 / sqrt((m.x40 - m.x54)
    **2 + (m.x95 - m.x109)**2 + (m.x150 - m.x164)**2) + 1 / sqrt((m.x40 - m.x55)
    **2 + (m.x95 - m.x110)**2 + (m.x150 - m.x165)**2) + 1 / sqrt((m.x41 - m.x42)
    **2 + (m.x96 - m.x97)**2 + (m.x151 - m.x152)**2) + 1 / sqrt((m.x41 - m.x43)
    **2 + (m.x96 - m.x98)**2 + (m.x151 - m.x153)**2) + 1 / sqrt((m.x41 - m.x44)
    **2 + (m.x96 - m.x99)**2 + (m.x151 - m.x154)**2) + 1 / sqrt((m.x41 - m.x45)
    **2 + (m.x96 - m.x100)**2 + (m.x151 - m.x155)**2) + 1 / sqrt((m.x41 - m.x46)
    **2 + (m.x96 - m.x101)**2 + (m.x151 - m.x156)**2) + 1 / sqrt((m.x41 - m.x47)
    **2 + (m.x96 - m.x102)**2 + (m.x151 - m.x157)**2) + 1 / sqrt((m.x41 - m.x48)
    **2 + (m.x96 - m.x103)**2 + (m.x151 - m.x158)**2) + 1 / sqrt((m.x41 - m.x49)
    **2 + (m.x96 - m.x104)**2 + (m.x151 - m.x159)**2) + 1 / sqrt((m.x41 - m.x50)
    **2 + (m.x96 - m.x105)**2 + (m.x151 - m.x160)**2) + 1 / sqrt((m.x41 - m.x51)
    **2 + (m.x96 - m.x106)**2 + (m.x151 - m.x161)**2) + 1 / sqrt((m.x41 - m.x52)
    **2 + (m.x96 - m.x107)**2 + (m.x151 - m.x162)**2) + 1 / sqrt((m.x41 - m.x53)
    **2 + (m.x96 - m.x108)**2 + (m.x151 - m.x163)**2) + 1 / sqrt((m.x41 - m.x54)
    **2 + (m.x96 - m.x109)**2 + (m.x151 - m.x164)**2) + 1 / sqrt((m.x41 - m.x55)
    **2 + (m.x96 - m.x110)**2 + (m.x151 - m.x165)**2) + 1 / sqrt((m.x42 - m.x43)
    **2 + (m.x97 - m.x98)**2 + (m.x152 - m.x153)**2) + 1 / sqrt((m.x42 - m.x44)
    **2 + (m.x97 - m.x99)**2 + (m.x152 - m.x154)**2) + 1 / sqrt((m.x42 - m.x45)
    **2 + (m.x97 - m.x100)**2 + (m.x152 - m.x155)**2) + 1 / sqrt((m.x42 - m.x46)
    **2 + (m.x97 - m.x101)**2 + (m.x152 - m.x156)**2) + 1 / sqrt((m.x42 - m.x47)
    **2 + (m.x97 - m.x102)**2 + (m.x152 - m.x157)**2) + 1 / sqrt((m.x42 - m.x48)
    **2 + (m.x97 - m.x103)**2 + (m.x152 - m.x158)**2) + 1 / sqrt((m.x42 - m.x49)
    **2 + (m.x97 - m.x104)**2 + (m.x152 - m.x159)**2) + 1 / sqrt((m.x42 - m.x50)
    **2 + (m.x97 - m.x105)**2 + (m.x152 - m.x160)**2) + 1 / sqrt((m.x42 - m.x51)
    **2 + (m.x97 - m.x106)**2 + (m.x152 - m.x161)**2) + 1 / sqrt((m.x42 - m.x52)
    **2 + (m.x97 - m.x107)**2 + (m.x152 - m.x162)**2) + 1 / sqrt((m.x42 - m.x53)
    **2 + (m.x97 - m.x108)**2 + (m.x152 - m.x163)**2) + 1 / sqrt((m.x42 - m.x54)
    **2 + (m.x97 - m.x109)**2 + (m.x152 - m.x164)**2) + 1 / sqrt((m.x42 - m.x55)
    **2 + (m.x97 - m.x110)**2 + (m.x152 - m.x165)**2) + 1 / sqrt((m.x43 - m.x44)
    **2 + (m.x98 - m.x99)**2 + (m.x153 - m.x154)**2) + 1 / sqrt((m.x43 - m.x45)
    **2 + (m.x98 - m.x100)**2 + (m.x153 - m.x155)**2) + 1 / sqrt((m.x43 - m.x46)
    **2 + (m.x98 - m.x101)**2 + (m.x153 - m.x156)**2) + 1 / sqrt((m.x43 - m.x47)
    **2 + (m.x98 - m.x102)**2 + (m.x153 - m.x157)**2) + 1 / sqrt((m.x43 - m.x48)
    **2 + (m.x98 - m.x103)**2 + (m.x153 - m.x158)**2) + 1 / sqrt((m.x43 - m.x49)
    **2 + (m.x98 - m.x104)**2 + (m.x153 - m.x159)**2) + 1 / sqrt((m.x43 - m.x50)
    **2 + (m.x98 - m.x105)**2 + (m.x153 - m.x160)**2) + 1 / sqrt((m.x43 - m.x51)
    **2 + (m.x98 - m.x106)**2 + (m.x153 - m.x161)**2) + 1 / sqrt((m.x43 - m.x52)
    **2 + (m.x98 - m.x107)**2 + (m.x153 - m.x162)**2) + 1 / sqrt((m.x43 - m.x53)
    **2 + (m.x98 - m.x108)**2 + (m.x153 - m.x163)**2) + 1 / sqrt((m.x43 - m.x54)
    **2 + (m.x98 - m.x109)**2 + (m.x153 - m.x164)**2) + 1 / sqrt((m.x43 - m.x55)
    **2 + (m.x98 - m.x110)**2 + (m.x153 - m.x165)**2) + 1 / sqrt((m.x44 - m.x45)
    **2 + (m.x99 - m.x100)**2 + (m.x154 - m.x155)**2) + 1 / sqrt((m.x44 - m.x46)
    **2 + (m.x99 - m.x101)**2 + (m.x154 - m.x156)**2) + 1 / sqrt((m.x44 - m.x47)
    **2 + (m.x99 - m.x102)**2 + (m.x154 - m.x157)**2) + 1 / sqrt((m.x44 - m.x48)
    **2 + (m.x99 - m.x103)**2 + (m.x154 - m.x158)**2) + 1 / sqrt((m.x44 - m.x49)
    **2 + (m.x99 - m.x104)**2 + (m.x154 - m.x159)**2) + 1 / sqrt((m.x44 - m.x50)
    **2 + (m.x99 - m.x105)**2 + (m.x154 - m.x160)**2) + 1 / sqrt((m.x44 - m.x51)
    **2 + (m.x99 - m.x106)**2 + (m.x154 - m.x161)**2) + 1 / sqrt((m.x44 - m.x52)
    **2 + (m.x99 - m.x107)**2 + (m.x154 - m.x162)**2) + 1 / sqrt((m.x44 - m.x53)
    **2 + (m.x99 - m.x108)**2 + (m.x154 - m.x163)**2) + 1 / sqrt((m.x44 - m.x54)
    **2 + (m.x99 - m.x109)**2 + (m.x154 - m.x164)**2) + 1 / sqrt((m.x44 - m.x55)
    **2 + (m.x99 - m.x110)**2 + (m.x154 - m.x165)**2) + 1 / sqrt((m.x45 - m.x46)
    **2 + (m.x100 - m.x101)**2 + (m.x155 - m.x156)**2) + 1 / sqrt((m.x45 -
    m.x47)**2 + (m.x100 - m.x102)**2 + (m.x155 - m.x157)**2) + 1 / sqrt((m.x45
    - m.x48)**2 + (m.x100 - m.x103)**2 + (m.x155 - m.x158)**2) + 1 / sqrt((
    m.x45 - m.x49)**2 + (m.x100 - m.x104)**2 + (m.x155 - m.x159)**2) + 1 /
    sqrt((m.x45 - m.x50)**2 + (m.x100 - m.x105)**2 + (m.x155 - m.x160)**2) + 1
    / sqrt((m.x45 - m.x51)**2 + (m.x100 - m.x106)**2 + (m.x155 - m.x161)**2)
    + 1 / sqrt((m.x45 - m.x52)**2 + (m.x100 - m.x107)**2 + (m.x155 - m.x162)**
    2) + 1 / sqrt((m.x45 - m.x53)**2 + (m.x100 - m.x108)**2 + (m.x155 - m.x163)
    **2) + 1 / sqrt((m.x45 - m.x54)**2 + (m.x100 - m.x109)**2 + (m.x155 -
    m.x164)**2) + 1 / sqrt((m.x45 - m.x55)**2 + (m.x100 - m.x110)**2 + (m.x155
    - m.x165)**2) + 1 / sqrt((m.x46 - m.x47)**2 + (m.x101 - m.x102)**2 + (
    m.x156 - m.x157)**2) + 1 / sqrt((m.x46 - m.x48)**2 + (m.x101 - m.x103)**2
    + (m.x156 - m.x158)**2) + 1 / sqrt((m.x46 - m.x49)**2 + (m.x101 - m.x104)
    **2 + (m.x156 - m.x159)**2) + 1 / sqrt((m.x46 - m.x50)**2 + (m.x101 -
    m.x105)**2 + (m.x156 - m.x160)**2) + 1 / sqrt((m.x46 - m.x51)**2 + (m.x101
    - m.x106)**2 + (m.x156 - m.x161)**2) + 1 / sqrt((m.x46 - m.x52)**2 + (
    m.x101 - m.x107)**2 + (m.x156 - m.x162)**2) + 1 / sqrt((m.x46 - m.x53)**2
    + (m.x101 - m.x108)**2 + (m.x156 - m.x163)**2) + 1 / sqrt((m.x46 - m.x54)
    **2 + (m.x101 - m.x109)**2 + (m.x156 - m.x164)**2) + 1 / sqrt((m.x46 -
    m.x55)**2 + (m.x101 - m.x110)**2 + (m.x156 - m.x165)**2) + 1 / sqrt((m.x47
    - m.x48)**2 + (m.x102 - m.x103)**2 + (m.x157 - m.x158)**2) + 1 / sqrt((
    m.x47 - m.x49)**2 + (m.x102 - m.x104)**2 + (m.x157 - m.x159)**2) + 1 /
    sqrt((m.x47 - m.x50)**2 + (m.x102 - m.x105)**2 + (m.x157 - m.x160)**2) + 1
    / sqrt((m.x47 - m.x51)**2 + (m.x102 - m.x106)**2 + (m.x157 - m.x161)**2)
    + 1 / sqrt((m.x47 - m.x52)**2 + (m.x102 - m.x107)**2 + (m.x157 - m.x162)**
    2) + 1 / sqrt((m.x47 - m.x53)**2 + (m.x102 - m.x108)**2 + (m.x157 - m.x163)
    **2) + 1 / sqrt((m.x47 - m.x54)**2 + (m.x102 - m.x109)**2 + (m.x157 -
    m.x164)**2) + 1 / sqrt((m.x47 - m.x55)**2 + (m.x102 - m.x110)**2 + (m.x157
    - m.x165)**2) + 1 / sqrt((m.x48 - m.x49)**2 + (m.x103 - m.x104)**2 + (
    m.x158 - m.x159)**2) + 1 / sqrt((m.x48 - m.x50)**2 + (m.x103 - m.x105)**2
    + (m.x158 - m.x160)**2) + 1 / sqrt((m.x48 - m.x51)**2 + (m.x103 - m.x106)
    **2 + (m.x158 - m.x161)**2) + 1 / sqrt((m.x48 - m.x52)**2 + (m.x103 -
    m.x107)**2 + (m.x158 - m.x162)**2) + 1 / sqrt((m.x48 - m.x53)**2 + (m.x103
    - m.x108)**2 + (m.x158 - m.x163)**2) + 1 / sqrt((m.x48 - m.x54)**2 + (
    m.x103 - m.x109)**2 + (m.x158 - m.x164)**2) + 1 / sqrt((m.x48 - m.x55)**2
    + (m.x103 - m.x110)**2 + (m.x158 - m.x165)**2) + 1 / sqrt((m.x49 - m.x50)
    **2 + (m.x104 - m.x105)**2 + (m.x159 - m.x160)**2) + 1 / sqrt((m.x49 -
    m.x51)**2 + (m.x104 - m.x106)**2 + (m.x159 - m.x161)**2) + 1 / sqrt((m.x49
    - m.x52)**2 + (m.x104 - m.x107)**2 + (m.x159 - m.x162)**2) + 1 / sqrt((
    m.x49 - m.x53)**2 + (m.x104 - m.x108)**2 + (m.x159 - m.x163)**2) + 1 /
    sqrt((m.x49 - m.x54)**2 + (m.x104 - m.x109)**2 + (m.x159 - m.x164)**2) + 1
    / sqrt((m.x49 - m.x55)**2 + (m.x104 - m.x110)**2 + (m.x159 - m.x165)**2)
    + 1 / sqrt((m.x50 - m.x51)**2 + (m.x105 - m.x106)**2 + (m.x160 - m.x161)**
    2) + 1 / sqrt((m.x50 - m.x52)**2 + (m.x105 - m.x107)**2 + (m.x160 - m.x162)
    **2) + 1 / sqrt((m.x50 - m.x53)**2 + (m.x105 - m.x108)**2 + (m.x160 -
    m.x163)**2) + 1 / sqrt((m.x50 - m.x54)**2 + (m.x105 - m.x109)**2 + (m.x160
    - m.x164)**2) + 1 / sqrt((m.x50 - m.x55)**2 + (m.x105 - m.x110)**2 + (
    m.x160 - m.x165)**2) + 1 / sqrt((m.x51 - m.x52)**2 + (m.x106 - m.x107)**2
    + (m.x161 - m.x162)**2) + 1 / sqrt((m.x51 - m.x53)**2 + (m.x106 - m.x108)
    **2 + (m.x161 - m.x163)**2) + 1 / sqrt((m.x51 - m.x54)**2 + (m.x106 -
    m.x109)**2 + (m.x161 - m.x164)**2) + 1 / sqrt((m.x51 - m.x55)**2 + (m.x106
    - m.x110)**2 + (m.x161 - m.x165)**2) + 1 / sqrt((m.x52 - m.x53)**2 + (
    m.x107 - m.x108)**2 + (m.x162 - m.x163)**2) + 1 / sqrt((m.x52 - m.x54)**2
    + (m.x107 - m.x109)**2 + (m.x162 - m.x164)**2) + 1 / sqrt((m.x52 - m.x55)
    **2 + (m.x107 - m.x110)**2 + (m.x162 - m.x165)**2) + 1 / sqrt((m.x53 -
    m.x54)**2 + (m.x108 - m.x109)**2 + (m.x163 - m.x164)**2) + 1 / sqrt((m.x53
    - m.x55)**2 + (m.x108 - m.x110)**2 + (m.x163 - m.x165)**2) + 1 / sqrt((
    m.x54 - m.x55)**2 + (m.x109 - m.x110)**2 + (m.x164 - m.x165)**2))

m.e1 = Constraint(expr= m.x1**2 + m.x56**2 + m.x111**2 == 1)
m.e2 = Constraint(expr= m.x2**2 + m.x57**2 + m.x112**2 == 1)
m.e3 = Constraint(expr= m.x3**2 + m.x58**2 + m.x113**2 == 1)
m.e4 = Constraint(expr= m.x4**2 + m.x59**2 + m.x114**2 == 1)
m.e5 = Constraint(expr= m.x5**2 + m.x60**2 + m.x115**2 == 1)
m.e6 = Constraint(expr= m.x6**2 + m.x61**2 + m.x116**2 == 1)
m.e7 = Constraint(expr= m.x7**2 + m.x62**2 + m.x117**2 == 1)
m.e8 = Constraint(expr= m.x8**2 + m.x63**2 + m.x118**2 == 1)
m.e9 = Constraint(expr= m.x9**2 + m.x64**2 + m.x119**2 == 1)
m.e10 = Constraint(expr= m.x10**2 + m.x65**2 + m.x120**2 == 1)
m.e11 = Constraint(expr= m.x11**2 + m.x66**2 + m.x121**2 == 1)
m.e12 = Constraint(expr= m.x12**2 + m.x67**2 + m.x122**2 == 1)
m.e13 = Constraint(expr= m.x13**2 + m.x68**2 + m.x123**2 == 1)
m.e14 = Constraint(expr= m.x14**2 + m.x69**2 + m.x124**2 == 1)
m.e15 = Constraint(expr= m.x15**2 + m.x70**2 + m.x125**2 == 1)
m.e16 = Constraint(expr= m.x16**2 + m.x71**2 + m.x126**2 == 1)
m.e17 = Constraint(expr= m.x17**2 + m.x72**2 + m.x127**2 == 1)
m.e18 = Constraint(expr= m.x18**2 + m.x73**2 + m.x128**2 == 1)
m.e19 = Constraint(expr= m.x19**2 + m.x74**2 + m.x129**2 == 1)
m.e20 = Constraint(expr= m.x20**2 + m.x75**2 + m.x130**2 == 1)
m.e21 = Constraint(expr= m.x21**2 + m.x76**2 + m.x131**2 == 1)
m.e22 = Constraint(expr= m.x22**2 + m.x77**2 + m.x132**2 == 1)
m.e23 = Constraint(expr= m.x23**2 + m.x78**2 + m.x133**2 == 1)
m.e24 = Constraint(expr= m.x24**2 + m.x79**2 + m.x134**2 == 1)
m.e25 = Constraint(expr= m.x25**2 + m.x80**2 + m.x135**2 == 1)
m.e26 = Constraint(expr= m.x26**2 + m.x81**2 + m.x136**2 == 1)
m.e27 = Constraint(expr= m.x27**2 + m.x82**2 + m.x137**2 == 1)
m.e28 = Constraint(expr= m.x28**2 + m.x83**2 + m.x138**2 == 1)
m.e29 = Constraint(expr= m.x29**2 + m.x84**2 + m.x139**2 == 1)
m.e30 = Constraint(expr= m.x30**2 + m.x85**2 + m.x140**2 == 1)
m.e31 = Constraint(expr= m.x31**2 + m.x86**2 + m.x141**2 == 1)
m.e32 = Constraint(expr= m.x32**2 + m.x87**2 + m.x142**2 == 1)
m.e33 = Constraint(expr= m.x33**2 + m.x88**2 + m.x143**2 == 1)
m.e34 = Constraint(expr= m.x34**2 + m.x89**2 + m.x144**2 == 1)
m.e35 = Constraint(expr= m.x35**2 + m.x90**2 + m.x145**2 == 1)
m.e36 = Constraint(expr= m.x36**2 + m.x91**2 + m.x146**2 == 1)
m.e37 = Constraint(expr= m.x37**2 + m.x92**2 + m.x147**2 == 1)
m.e38 = Constraint(expr= m.x38**2 + m.x93**2 + m.x148**2 == 1)
m.e39 = Constraint(expr= m.x39**2 + m.x94**2 + m.x149**2 == 1)
m.e40 = Constraint(expr= m.x40**2 + m.x95**2 + m.x150**2 == 1)
m.e41 = Constraint(expr= m.x41**2 + m.x96**2 + m.x151**2 == 1)
m.e42 = Constraint(expr= m.x42**2 + m.x97**2 + m.x152**2 == 1)
m.e43 = Constraint(expr= m.x43**2 + m.x98**2 + m.x153**2 == 1)
m.e44 = Constraint(expr= m.x44**2 + m.x99**2 + m.x154**2 == 1)
m.e45 = Constraint(expr= m.x45**2 + m.x100**2 + m.x155**2 == 1)
m.e46 = Constraint(expr= m.x46**2 + m.x101**2 + m.x156**2 == 1)
m.e47 = Constraint(expr= m.x47**2 + m.x102**2 + m.x157**2 == 1)
m.e48 = Constraint(expr= m.x48**2 + m.x103**2 + m.x158**2 == 1)
m.e49 = Constraint(expr= m.x49**2 + m.x104**2 + m.x159**2 == 1)
m.e50 = Constraint(expr= m.x50**2 + m.x105**2 + m.x160**2 == 1)
m.e51 = Constraint(expr= m.x51**2 + m.x106**2 + m.x161**2 == 1)
m.e52 = Constraint(expr= m.x52**2 + m.x107**2 + m.x162**2 == 1)
m.e53 = Constraint(expr= m.x53**2 + m.x108**2 + m.x163**2 == 1)
m.e54 = Constraint(expr= m.x54**2 + m.x109**2 + m.x164**2 == 1)
m.e55 = Constraint(expr= m.x55**2 + m.x110**2 + m.x165**2 == 1)
