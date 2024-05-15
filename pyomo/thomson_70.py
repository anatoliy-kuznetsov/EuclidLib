# NLP written by GAMS Convert at 05/15/24 11:40:42
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#        70       70        0        0        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#       210      210        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       210        0      210
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
m.x166 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x167 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x168 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x169 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x170 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x171 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x172 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x173 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x174 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x175 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x176 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x177 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x178 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x179 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x180 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x181 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x182 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x183 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x184 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x185 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x186 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x187 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x188 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x189 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x190 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x191 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x192 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x193 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x194 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x195 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x196 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x197 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x198 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x199 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x200 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x201 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x202 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x203 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x204 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x205 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x206 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x207 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x208 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x209 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x210 = Var(within=Reals, bounds=(-1,1), initialize=0)

m.obj = Objective(sense=minimize, expr= 1 / sqrt((m.x1 - m.x2)**2 + (m.x71 -
    m.x72)**2 + (m.x141 - m.x142)**2) + 1 / sqrt((m.x1 - m.x3)**2 + (m.x71 -
    m.x73)**2 + (m.x141 - m.x143)**2) + 1 / sqrt((m.x1 - m.x4)**2 + (m.x71 -
    m.x74)**2 + (m.x141 - m.x144)**2) + 1 / sqrt((m.x1 - m.x5)**2 + (m.x71 -
    m.x75)**2 + (m.x141 - m.x145)**2) + 1 / sqrt((m.x1 - m.x6)**2 + (m.x71 -
    m.x76)**2 + (m.x141 - m.x146)**2) + 1 / sqrt((m.x1 - m.x7)**2 + (m.x71 -
    m.x77)**2 + (m.x141 - m.x147)**2) + 1 / sqrt((m.x1 - m.x8)**2 + (m.x71 -
    m.x78)**2 + (m.x141 - m.x148)**2) + 1 / sqrt((m.x1 - m.x9)**2 + (m.x71 -
    m.x79)**2 + (m.x141 - m.x149)**2) + 1 / sqrt((m.x1 - m.x10)**2 + (m.x71 -
    m.x80)**2 + (m.x141 - m.x150)**2) + 1 / sqrt((m.x1 - m.x11)**2 + (m.x71 -
    m.x81)**2 + (m.x141 - m.x151)**2) + 1 / sqrt((m.x1 - m.x12)**2 + (m.x71 -
    m.x82)**2 + (m.x141 - m.x152)**2) + 1 / sqrt((m.x1 - m.x13)**2 + (m.x71 -
    m.x83)**2 + (m.x141 - m.x153)**2) + 1 / sqrt((m.x1 - m.x14)**2 + (m.x71 -
    m.x84)**2 + (m.x141 - m.x154)**2) + 1 / sqrt((m.x1 - m.x15)**2 + (m.x71 -
    m.x85)**2 + (m.x141 - m.x155)**2) + 1 / sqrt((m.x1 - m.x16)**2 + (m.x71 -
    m.x86)**2 + (m.x141 - m.x156)**2) + 1 / sqrt((m.x1 - m.x17)**2 + (m.x71 -
    m.x87)**2 + (m.x141 - m.x157)**2) + 1 / sqrt((m.x1 - m.x18)**2 + (m.x71 -
    m.x88)**2 + (m.x141 - m.x158)**2) + 1 / sqrt((m.x1 - m.x19)**2 + (m.x71 -
    m.x89)**2 + (m.x141 - m.x159)**2) + 1 / sqrt((m.x1 - m.x20)**2 + (m.x71 -
    m.x90)**2 + (m.x141 - m.x160)**2) + 1 / sqrt((m.x1 - m.x21)**2 + (m.x71 -
    m.x91)**2 + (m.x141 - m.x161)**2) + 1 / sqrt((m.x1 - m.x22)**2 + (m.x71 -
    m.x92)**2 + (m.x141 - m.x162)**2) + 1 / sqrt((m.x1 - m.x23)**2 + (m.x71 -
    m.x93)**2 + (m.x141 - m.x163)**2) + 1 / sqrt((m.x1 - m.x24)**2 + (m.x71 -
    m.x94)**2 + (m.x141 - m.x164)**2) + 1 / sqrt((m.x1 - m.x25)**2 + (m.x71 -
    m.x95)**2 + (m.x141 - m.x165)**2) + 1 / sqrt((m.x1 - m.x26)**2 + (m.x71 -
    m.x96)**2 + (m.x141 - m.x166)**2) + 1 / sqrt((m.x1 - m.x27)**2 + (m.x71 -
    m.x97)**2 + (m.x141 - m.x167)**2) + 1 / sqrt((m.x1 - m.x28)**2 + (m.x71 -
    m.x98)**2 + (m.x141 - m.x168)**2) + 1 / sqrt((m.x1 - m.x29)**2 + (m.x71 -
    m.x99)**2 + (m.x141 - m.x169)**2) + 1 / sqrt((m.x1 - m.x30)**2 + (m.x71 -
    m.x100)**2 + (m.x141 - m.x170)**2) + 1 / sqrt((m.x1 - m.x31)**2 + (m.x71 -
    m.x101)**2 + (m.x141 - m.x171)**2) + 1 / sqrt((m.x1 - m.x32)**2 + (m.x71 -
    m.x102)**2 + (m.x141 - m.x172)**2) + 1 / sqrt((m.x1 - m.x33)**2 + (m.x71 -
    m.x103)**2 + (m.x141 - m.x173)**2) + 1 / sqrt((m.x1 - m.x34)**2 + (m.x71 -
    m.x104)**2 + (m.x141 - m.x174)**2) + 1 / sqrt((m.x1 - m.x35)**2 + (m.x71 -
    m.x105)**2 + (m.x141 - m.x175)**2) + 1 / sqrt((m.x1 - m.x36)**2 + (m.x71 -
    m.x106)**2 + (m.x141 - m.x176)**2) + 1 / sqrt((m.x1 - m.x37)**2 + (m.x71 -
    m.x107)**2 + (m.x141 - m.x177)**2) + 1 / sqrt((m.x1 - m.x38)**2 + (m.x71 -
    m.x108)**2 + (m.x141 - m.x178)**2) + 1 / sqrt((m.x1 - m.x39)**2 + (m.x71 -
    m.x109)**2 + (m.x141 - m.x179)**2) + 1 / sqrt((m.x1 - m.x40)**2 + (m.x71 -
    m.x110)**2 + (m.x141 - m.x180)**2) + 1 / sqrt((m.x1 - m.x41)**2 + (m.x71 -
    m.x111)**2 + (m.x141 - m.x181)**2) + 1 / sqrt((m.x1 - m.x42)**2 + (m.x71 -
    m.x112)**2 + (m.x141 - m.x182)**2) + 1 / sqrt((m.x1 - m.x43)**2 + (m.x71 -
    m.x113)**2 + (m.x141 - m.x183)**2) + 1 / sqrt((m.x1 - m.x44)**2 + (m.x71 -
    m.x114)**2 + (m.x141 - m.x184)**2) + 1 / sqrt((m.x1 - m.x45)**2 + (m.x71 -
    m.x115)**2 + (m.x141 - m.x185)**2) + 1 / sqrt((m.x1 - m.x46)**2 + (m.x71 -
    m.x116)**2 + (m.x141 - m.x186)**2) + 1 / sqrt((m.x1 - m.x47)**2 + (m.x71 -
    m.x117)**2 + (m.x141 - m.x187)**2) + 1 / sqrt((m.x1 - m.x48)**2 + (m.x71 -
    m.x118)**2 + (m.x141 - m.x188)**2) + 1 / sqrt((m.x1 - m.x49)**2 + (m.x71 -
    m.x119)**2 + (m.x141 - m.x189)**2) + 1 / sqrt((m.x1 - m.x50)**2 + (m.x71 -
    m.x120)**2 + (m.x141 - m.x190)**2) + 1 / sqrt((m.x1 - m.x51)**2 + (m.x71 -
    m.x121)**2 + (m.x141 - m.x191)**2) + 1 / sqrt((m.x1 - m.x52)**2 + (m.x71 -
    m.x122)**2 + (m.x141 - m.x192)**2) + 1 / sqrt((m.x1 - m.x53)**2 + (m.x71 -
    m.x123)**2 + (m.x141 - m.x193)**2) + 1 / sqrt((m.x1 - m.x54)**2 + (m.x71 -
    m.x124)**2 + (m.x141 - m.x194)**2) + 1 / sqrt((m.x1 - m.x55)**2 + (m.x71 -
    m.x125)**2 + (m.x141 - m.x195)**2) + 1 / sqrt((m.x1 - m.x56)**2 + (m.x71 -
    m.x126)**2 + (m.x141 - m.x196)**2) + 1 / sqrt((m.x1 - m.x57)**2 + (m.x71 -
    m.x127)**2 + (m.x141 - m.x197)**2) + 1 / sqrt((m.x1 - m.x58)**2 + (m.x71 -
    m.x128)**2 + (m.x141 - m.x198)**2) + 1 / sqrt((m.x1 - m.x59)**2 + (m.x71 -
    m.x129)**2 + (m.x141 - m.x199)**2) + 1 / sqrt((m.x1 - m.x60)**2 + (m.x71 -
    m.x130)**2 + (m.x141 - m.x200)**2) + 1 / sqrt((m.x1 - m.x61)**2 + (m.x71 -
    m.x131)**2 + (m.x141 - m.x201)**2) + 1 / sqrt((m.x1 - m.x62)**2 + (m.x71 -
    m.x132)**2 + (m.x141 - m.x202)**2) + 1 / sqrt((m.x1 - m.x63)**2 + (m.x71 -
    m.x133)**2 + (m.x141 - m.x203)**2) + 1 / sqrt((m.x1 - m.x64)**2 + (m.x71 -
    m.x134)**2 + (m.x141 - m.x204)**2) + 1 / sqrt((m.x1 - m.x65)**2 + (m.x71 -
    m.x135)**2 + (m.x141 - m.x205)**2) + 1 / sqrt((m.x1 - m.x66)**2 + (m.x71 -
    m.x136)**2 + (m.x141 - m.x206)**2) + 1 / sqrt((m.x1 - m.x67)**2 + (m.x71 -
    m.x137)**2 + (m.x141 - m.x207)**2) + 1 / sqrt((m.x1 - m.x68)**2 + (m.x71 -
    m.x138)**2 + (m.x141 - m.x208)**2) + 1 / sqrt((m.x1 - m.x69)**2 + (m.x71 -
    m.x139)**2 + (m.x141 - m.x209)**2) + 1 / sqrt((m.x1 - m.x70)**2 + (m.x71 -
    m.x140)**2 + (m.x141 - m.x210)**2) + 1 / sqrt((m.x2 - m.x3)**2 + (m.x72 -
    m.x73)**2 + (m.x142 - m.x143)**2) + 1 / sqrt((m.x2 - m.x4)**2 + (m.x72 -
    m.x74)**2 + (m.x142 - m.x144)**2) + 1 / sqrt((m.x2 - m.x5)**2 + (m.x72 -
    m.x75)**2 + (m.x142 - m.x145)**2) + 1 / sqrt((m.x2 - m.x6)**2 + (m.x72 -
    m.x76)**2 + (m.x142 - m.x146)**2) + 1 / sqrt((m.x2 - m.x7)**2 + (m.x72 -
    m.x77)**2 + (m.x142 - m.x147)**2) + 1 / sqrt((m.x2 - m.x8)**2 + (m.x72 -
    m.x78)**2 + (m.x142 - m.x148)**2) + 1 / sqrt((m.x2 - m.x9)**2 + (m.x72 -
    m.x79)**2 + (m.x142 - m.x149)**2) + 1 / sqrt((m.x2 - m.x10)**2 + (m.x72 -
    m.x80)**2 + (m.x142 - m.x150)**2) + 1 / sqrt((m.x2 - m.x11)**2 + (m.x72 -
    m.x81)**2 + (m.x142 - m.x151)**2) + 1 / sqrt((m.x2 - m.x12)**2 + (m.x72 -
    m.x82)**2 + (m.x142 - m.x152)**2) + 1 / sqrt((m.x2 - m.x13)**2 + (m.x72 -
    m.x83)**2 + (m.x142 - m.x153)**2) + 1 / sqrt((m.x2 - m.x14)**2 + (m.x72 -
    m.x84)**2 + (m.x142 - m.x154)**2) + 1 / sqrt((m.x2 - m.x15)**2 + (m.x72 -
    m.x85)**2 + (m.x142 - m.x155)**2) + 1 / sqrt((m.x2 - m.x16)**2 + (m.x72 -
    m.x86)**2 + (m.x142 - m.x156)**2) + 1 / sqrt((m.x2 - m.x17)**2 + (m.x72 -
    m.x87)**2 + (m.x142 - m.x157)**2) + 1 / sqrt((m.x2 - m.x18)**2 + (m.x72 -
    m.x88)**2 + (m.x142 - m.x158)**2) + 1 / sqrt((m.x2 - m.x19)**2 + (m.x72 -
    m.x89)**2 + (m.x142 - m.x159)**2) + 1 / sqrt((m.x2 - m.x20)**2 + (m.x72 -
    m.x90)**2 + (m.x142 - m.x160)**2) + 1 / sqrt((m.x2 - m.x21)**2 + (m.x72 -
    m.x91)**2 + (m.x142 - m.x161)**2) + 1 / sqrt((m.x2 - m.x22)**2 + (m.x72 -
    m.x92)**2 + (m.x142 - m.x162)**2) + 1 / sqrt((m.x2 - m.x23)**2 + (m.x72 -
    m.x93)**2 + (m.x142 - m.x163)**2) + 1 / sqrt((m.x2 - m.x24)**2 + (m.x72 -
    m.x94)**2 + (m.x142 - m.x164)**2) + 1 / sqrt((m.x2 - m.x25)**2 + (m.x72 -
    m.x95)**2 + (m.x142 - m.x165)**2) + 1 / sqrt((m.x2 - m.x26)**2 + (m.x72 -
    m.x96)**2 + (m.x142 - m.x166)**2) + 1 / sqrt((m.x2 - m.x27)**2 + (m.x72 -
    m.x97)**2 + (m.x142 - m.x167)**2) + 1 / sqrt((m.x2 - m.x28)**2 + (m.x72 -
    m.x98)**2 + (m.x142 - m.x168)**2) + 1 / sqrt((m.x2 - m.x29)**2 + (m.x72 -
    m.x99)**2 + (m.x142 - m.x169)**2) + 1 / sqrt((m.x2 - m.x30)**2 + (m.x72 -
    m.x100)**2 + (m.x142 - m.x170)**2) + 1 / sqrt((m.x2 - m.x31)**2 + (m.x72 -
    m.x101)**2 + (m.x142 - m.x171)**2) + 1 / sqrt((m.x2 - m.x32)**2 + (m.x72 -
    m.x102)**2 + (m.x142 - m.x172)**2) + 1 / sqrt((m.x2 - m.x33)**2 + (m.x72 -
    m.x103)**2 + (m.x142 - m.x173)**2) + 1 / sqrt((m.x2 - m.x34)**2 + (m.x72 -
    m.x104)**2 + (m.x142 - m.x174)**2) + 1 / sqrt((m.x2 - m.x35)**2 + (m.x72 -
    m.x105)**2 + (m.x142 - m.x175)**2) + 1 / sqrt((m.x2 - m.x36)**2 + (m.x72 -
    m.x106)**2 + (m.x142 - m.x176)**2) + 1 / sqrt((m.x2 - m.x37)**2 + (m.x72 -
    m.x107)**2 + (m.x142 - m.x177)**2) + 1 / sqrt((m.x2 - m.x38)**2 + (m.x72 -
    m.x108)**2 + (m.x142 - m.x178)**2) + 1 / sqrt((m.x2 - m.x39)**2 + (m.x72 -
    m.x109)**2 + (m.x142 - m.x179)**2) + 1 / sqrt((m.x2 - m.x40)**2 + (m.x72 -
    m.x110)**2 + (m.x142 - m.x180)**2) + 1 / sqrt((m.x2 - m.x41)**2 + (m.x72 -
    m.x111)**2 + (m.x142 - m.x181)**2) + 1 / sqrt((m.x2 - m.x42)**2 + (m.x72 -
    m.x112)**2 + (m.x142 - m.x182)**2) + 1 / sqrt((m.x2 - m.x43)**2 + (m.x72 -
    m.x113)**2 + (m.x142 - m.x183)**2) + 1 / sqrt((m.x2 - m.x44)**2 + (m.x72 -
    m.x114)**2 + (m.x142 - m.x184)**2) + 1 / sqrt((m.x2 - m.x45)**2 + (m.x72 -
    m.x115)**2 + (m.x142 - m.x185)**2) + 1 / sqrt((m.x2 - m.x46)**2 + (m.x72 -
    m.x116)**2 + (m.x142 - m.x186)**2) + 1 / sqrt((m.x2 - m.x47)**2 + (m.x72 -
    m.x117)**2 + (m.x142 - m.x187)**2) + 1 / sqrt((m.x2 - m.x48)**2 + (m.x72 -
    m.x118)**2 + (m.x142 - m.x188)**2) + 1 / sqrt((m.x2 - m.x49)**2 + (m.x72 -
    m.x119)**2 + (m.x142 - m.x189)**2) + 1 / sqrt((m.x2 - m.x50)**2 + (m.x72 -
    m.x120)**2 + (m.x142 - m.x190)**2) + 1 / sqrt((m.x2 - m.x51)**2 + (m.x72 -
    m.x121)**2 + (m.x142 - m.x191)**2) + 1 / sqrt((m.x2 - m.x52)**2 + (m.x72 -
    m.x122)**2 + (m.x142 - m.x192)**2) + 1 / sqrt((m.x2 - m.x53)**2 + (m.x72 -
    m.x123)**2 + (m.x142 - m.x193)**2) + 1 / sqrt((m.x2 - m.x54)**2 + (m.x72 -
    m.x124)**2 + (m.x142 - m.x194)**2) + 1 / sqrt((m.x2 - m.x55)**2 + (m.x72 -
    m.x125)**2 + (m.x142 - m.x195)**2) + 1 / sqrt((m.x2 - m.x56)**2 + (m.x72 -
    m.x126)**2 + (m.x142 - m.x196)**2) + 1 / sqrt((m.x2 - m.x57)**2 + (m.x72 -
    m.x127)**2 + (m.x142 - m.x197)**2) + 1 / sqrt((m.x2 - m.x58)**2 + (m.x72 -
    m.x128)**2 + (m.x142 - m.x198)**2) + 1 / sqrt((m.x2 - m.x59)**2 + (m.x72 -
    m.x129)**2 + (m.x142 - m.x199)**2) + 1 / sqrt((m.x2 - m.x60)**2 + (m.x72 -
    m.x130)**2 + (m.x142 - m.x200)**2) + 1 / sqrt((m.x2 - m.x61)**2 + (m.x72 -
    m.x131)**2 + (m.x142 - m.x201)**2) + 1 / sqrt((m.x2 - m.x62)**2 + (m.x72 -
    m.x132)**2 + (m.x142 - m.x202)**2) + 1 / sqrt((m.x2 - m.x63)**2 + (m.x72 -
    m.x133)**2 + (m.x142 - m.x203)**2) + 1 / sqrt((m.x2 - m.x64)**2 + (m.x72 -
    m.x134)**2 + (m.x142 - m.x204)**2) + 1 / sqrt((m.x2 - m.x65)**2 + (m.x72 -
    m.x135)**2 + (m.x142 - m.x205)**2) + 1 / sqrt((m.x2 - m.x66)**2 + (m.x72 -
    m.x136)**2 + (m.x142 - m.x206)**2) + 1 / sqrt((m.x2 - m.x67)**2 + (m.x72 -
    m.x137)**2 + (m.x142 - m.x207)**2) + 1 / sqrt((m.x2 - m.x68)**2 + (m.x72 -
    m.x138)**2 + (m.x142 - m.x208)**2) + 1 / sqrt((m.x2 - m.x69)**2 + (m.x72 -
    m.x139)**2 + (m.x142 - m.x209)**2) + 1 / sqrt((m.x2 - m.x70)**2 + (m.x72 -
    m.x140)**2 + (m.x142 - m.x210)**2) + 1 / sqrt((m.x3 - m.x4)**2 + (m.x73 -
    m.x74)**2 + (m.x143 - m.x144)**2) + 1 / sqrt((m.x3 - m.x5)**2 + (m.x73 -
    m.x75)**2 + (m.x143 - m.x145)**2) + 1 / sqrt((m.x3 - m.x6)**2 + (m.x73 -
    m.x76)**2 + (m.x143 - m.x146)**2) + 1 / sqrt((m.x3 - m.x7)**2 + (m.x73 -
    m.x77)**2 + (m.x143 - m.x147)**2) + 1 / sqrt((m.x3 - m.x8)**2 + (m.x73 -
    m.x78)**2 + (m.x143 - m.x148)**2) + 1 / sqrt((m.x3 - m.x9)**2 + (m.x73 -
    m.x79)**2 + (m.x143 - m.x149)**2) + 1 / sqrt((m.x3 - m.x10)**2 + (m.x73 -
    m.x80)**2 + (m.x143 - m.x150)**2) + 1 / sqrt((m.x3 - m.x11)**2 + (m.x73 -
    m.x81)**2 + (m.x143 - m.x151)**2) + 1 / sqrt((m.x3 - m.x12)**2 + (m.x73 -
    m.x82)**2 + (m.x143 - m.x152)**2) + 1 / sqrt((m.x3 - m.x13)**2 + (m.x73 -
    m.x83)**2 + (m.x143 - m.x153)**2) + 1 / sqrt((m.x3 - m.x14)**2 + (m.x73 -
    m.x84)**2 + (m.x143 - m.x154)**2) + 1 / sqrt((m.x3 - m.x15)**2 + (m.x73 -
    m.x85)**2 + (m.x143 - m.x155)**2) + 1 / sqrt((m.x3 - m.x16)**2 + (m.x73 -
    m.x86)**2 + (m.x143 - m.x156)**2) + 1 / sqrt((m.x3 - m.x17)**2 + (m.x73 -
    m.x87)**2 + (m.x143 - m.x157)**2) + 1 / sqrt((m.x3 - m.x18)**2 + (m.x73 -
    m.x88)**2 + (m.x143 - m.x158)**2) + 1 / sqrt((m.x3 - m.x19)**2 + (m.x73 -
    m.x89)**2 + (m.x143 - m.x159)**2) + 1 / sqrt((m.x3 - m.x20)**2 + (m.x73 -
    m.x90)**2 + (m.x143 - m.x160)**2) + 1 / sqrt((m.x3 - m.x21)**2 + (m.x73 -
    m.x91)**2 + (m.x143 - m.x161)**2) + 1 / sqrt((m.x3 - m.x22)**2 + (m.x73 -
    m.x92)**2 + (m.x143 - m.x162)**2) + 1 / sqrt((m.x3 - m.x23)**2 + (m.x73 -
    m.x93)**2 + (m.x143 - m.x163)**2) + 1 / sqrt((m.x3 - m.x24)**2 + (m.x73 -
    m.x94)**2 + (m.x143 - m.x164)**2) + 1 / sqrt((m.x3 - m.x25)**2 + (m.x73 -
    m.x95)**2 + (m.x143 - m.x165)**2) + 1 / sqrt((m.x3 - m.x26)**2 + (m.x73 -
    m.x96)**2 + (m.x143 - m.x166)**2) + 1 / sqrt((m.x3 - m.x27)**2 + (m.x73 -
    m.x97)**2 + (m.x143 - m.x167)**2) + 1 / sqrt((m.x3 - m.x28)**2 + (m.x73 -
    m.x98)**2 + (m.x143 - m.x168)**2) + 1 / sqrt((m.x3 - m.x29)**2 + (m.x73 -
    m.x99)**2 + (m.x143 - m.x169)**2) + 1 / sqrt((m.x3 - m.x30)**2 + (m.x73 -
    m.x100)**2 + (m.x143 - m.x170)**2) + 1 / sqrt((m.x3 - m.x31)**2 + (m.x73 -
    m.x101)**2 + (m.x143 - m.x171)**2) + 1 / sqrt((m.x3 - m.x32)**2 + (m.x73 -
    m.x102)**2 + (m.x143 - m.x172)**2) + 1 / sqrt((m.x3 - m.x33)**2 + (m.x73 -
    m.x103)**2 + (m.x143 - m.x173)**2) + 1 / sqrt((m.x3 - m.x34)**2 + (m.x73 -
    m.x104)**2 + (m.x143 - m.x174)**2) + 1 / sqrt((m.x3 - m.x35)**2 + (m.x73 -
    m.x105)**2 + (m.x143 - m.x175)**2) + 1 / sqrt((m.x3 - m.x36)**2 + (m.x73 -
    m.x106)**2 + (m.x143 - m.x176)**2) + 1 / sqrt((m.x3 - m.x37)**2 + (m.x73 -
    m.x107)**2 + (m.x143 - m.x177)**2) + 1 / sqrt((m.x3 - m.x38)**2 + (m.x73 -
    m.x108)**2 + (m.x143 - m.x178)**2) + 1 / sqrt((m.x3 - m.x39)**2 + (m.x73 -
    m.x109)**2 + (m.x143 - m.x179)**2) + 1 / sqrt((m.x3 - m.x40)**2 + (m.x73 -
    m.x110)**2 + (m.x143 - m.x180)**2) + 1 / sqrt((m.x3 - m.x41)**2 + (m.x73 -
    m.x111)**2 + (m.x143 - m.x181)**2) + 1 / sqrt((m.x3 - m.x42)**2 + (m.x73 -
    m.x112)**2 + (m.x143 - m.x182)**2) + 1 / sqrt((m.x3 - m.x43)**2 + (m.x73 -
    m.x113)**2 + (m.x143 - m.x183)**2) + 1 / sqrt((m.x3 - m.x44)**2 + (m.x73 -
    m.x114)**2 + (m.x143 - m.x184)**2) + 1 / sqrt((m.x3 - m.x45)**2 + (m.x73 -
    m.x115)**2 + (m.x143 - m.x185)**2) + 1 / sqrt((m.x3 - m.x46)**2 + (m.x73 -
    m.x116)**2 + (m.x143 - m.x186)**2) + 1 / sqrt((m.x3 - m.x47)**2 + (m.x73 -
    m.x117)**2 + (m.x143 - m.x187)**2) + 1 / sqrt((m.x3 - m.x48)**2 + (m.x73 -
    m.x118)**2 + (m.x143 - m.x188)**2) + 1 / sqrt((m.x3 - m.x49)**2 + (m.x73 -
    m.x119)**2 + (m.x143 - m.x189)**2) + 1 / sqrt((m.x3 - m.x50)**2 + (m.x73 -
    m.x120)**2 + (m.x143 - m.x190)**2) + 1 / sqrt((m.x3 - m.x51)**2 + (m.x73 -
    m.x121)**2 + (m.x143 - m.x191)**2) + 1 / sqrt((m.x3 - m.x52)**2 + (m.x73 -
    m.x122)**2 + (m.x143 - m.x192)**2) + 1 / sqrt((m.x3 - m.x53)**2 + (m.x73 -
    m.x123)**2 + (m.x143 - m.x193)**2) + 1 / sqrt((m.x3 - m.x54)**2 + (m.x73 -
    m.x124)**2 + (m.x143 - m.x194)**2) + 1 / sqrt((m.x3 - m.x55)**2 + (m.x73 -
    m.x125)**2 + (m.x143 - m.x195)**2) + 1 / sqrt((m.x3 - m.x56)**2 + (m.x73 -
    m.x126)**2 + (m.x143 - m.x196)**2) + 1 / sqrt((m.x3 - m.x57)**2 + (m.x73 -
    m.x127)**2 + (m.x143 - m.x197)**2) + 1 / sqrt((m.x3 - m.x58)**2 + (m.x73 -
    m.x128)**2 + (m.x143 - m.x198)**2) + 1 / sqrt((m.x3 - m.x59)**2 + (m.x73 -
    m.x129)**2 + (m.x143 - m.x199)**2) + 1 / sqrt((m.x3 - m.x60)**2 + (m.x73 -
    m.x130)**2 + (m.x143 - m.x200)**2) + 1 / sqrt((m.x3 - m.x61)**2 + (m.x73 -
    m.x131)**2 + (m.x143 - m.x201)**2) + 1 / sqrt((m.x3 - m.x62)**2 + (m.x73 -
    m.x132)**2 + (m.x143 - m.x202)**2) + 1 / sqrt((m.x3 - m.x63)**2 + (m.x73 -
    m.x133)**2 + (m.x143 - m.x203)**2) + 1 / sqrt((m.x3 - m.x64)**2 + (m.x73 -
    m.x134)**2 + (m.x143 - m.x204)**2) + 1 / sqrt((m.x3 - m.x65)**2 + (m.x73 -
    m.x135)**2 + (m.x143 - m.x205)**2) + 1 / sqrt((m.x3 - m.x66)**2 + (m.x73 -
    m.x136)**2 + (m.x143 - m.x206)**2) + 1 / sqrt((m.x3 - m.x67)**2 + (m.x73 -
    m.x137)**2 + (m.x143 - m.x207)**2) + 1 / sqrt((m.x3 - m.x68)**2 + (m.x73 -
    m.x138)**2 + (m.x143 - m.x208)**2) + 1 / sqrt((m.x3 - m.x69)**2 + (m.x73 -
    m.x139)**2 + (m.x143 - m.x209)**2) + 1 / sqrt((m.x3 - m.x70)**2 + (m.x73 -
    m.x140)**2 + (m.x143 - m.x210)**2) + 1 / sqrt((m.x4 - m.x5)**2 + (m.x74 -
    m.x75)**2 + (m.x144 - m.x145)**2) + 1 / sqrt((m.x4 - m.x6)**2 + (m.x74 -
    m.x76)**2 + (m.x144 - m.x146)**2) + 1 / sqrt((m.x4 - m.x7)**2 + (m.x74 -
    m.x77)**2 + (m.x144 - m.x147)**2) + 1 / sqrt((m.x4 - m.x8)**2 + (m.x74 -
    m.x78)**2 + (m.x144 - m.x148)**2) + 1 / sqrt((m.x4 - m.x9)**2 + (m.x74 -
    m.x79)**2 + (m.x144 - m.x149)**2) + 1 / sqrt((m.x4 - m.x10)**2 + (m.x74 -
    m.x80)**2 + (m.x144 - m.x150)**2) + 1 / sqrt((m.x4 - m.x11)**2 + (m.x74 -
    m.x81)**2 + (m.x144 - m.x151)**2) + 1 / sqrt((m.x4 - m.x12)**2 + (m.x74 -
    m.x82)**2 + (m.x144 - m.x152)**2) + 1 / sqrt((m.x4 - m.x13)**2 + (m.x74 -
    m.x83)**2 + (m.x144 - m.x153)**2) + 1 / sqrt((m.x4 - m.x14)**2 + (m.x74 -
    m.x84)**2 + (m.x144 - m.x154)**2) + 1 / sqrt((m.x4 - m.x15)**2 + (m.x74 -
    m.x85)**2 + (m.x144 - m.x155)**2) + 1 / sqrt((m.x4 - m.x16)**2 + (m.x74 -
    m.x86)**2 + (m.x144 - m.x156)**2) + 1 / sqrt((m.x4 - m.x17)**2 + (m.x74 -
    m.x87)**2 + (m.x144 - m.x157)**2) + 1 / sqrt((m.x4 - m.x18)**2 + (m.x74 -
    m.x88)**2 + (m.x144 - m.x158)**2) + 1 / sqrt((m.x4 - m.x19)**2 + (m.x74 -
    m.x89)**2 + (m.x144 - m.x159)**2) + 1 / sqrt((m.x4 - m.x20)**2 + (m.x74 -
    m.x90)**2 + (m.x144 - m.x160)**2) + 1 / sqrt((m.x4 - m.x21)**2 + (m.x74 -
    m.x91)**2 + (m.x144 - m.x161)**2) + 1 / sqrt((m.x4 - m.x22)**2 + (m.x74 -
    m.x92)**2 + (m.x144 - m.x162)**2) + 1 / sqrt((m.x4 - m.x23)**2 + (m.x74 -
    m.x93)**2 + (m.x144 - m.x163)**2) + 1 / sqrt((m.x4 - m.x24)**2 + (m.x74 -
    m.x94)**2 + (m.x144 - m.x164)**2) + 1 / sqrt((m.x4 - m.x25)**2 + (m.x74 -
    m.x95)**2 + (m.x144 - m.x165)**2) + 1 / sqrt((m.x4 - m.x26)**2 + (m.x74 -
    m.x96)**2 + (m.x144 - m.x166)**2) + 1 / sqrt((m.x4 - m.x27)**2 + (m.x74 -
    m.x97)**2 + (m.x144 - m.x167)**2) + 1 / sqrt((m.x4 - m.x28)**2 + (m.x74 -
    m.x98)**2 + (m.x144 - m.x168)**2) + 1 / sqrt((m.x4 - m.x29)**2 + (m.x74 -
    m.x99)**2 + (m.x144 - m.x169)**2) + 1 / sqrt((m.x4 - m.x30)**2 + (m.x74 -
    m.x100)**2 + (m.x144 - m.x170)**2) + 1 / sqrt((m.x4 - m.x31)**2 + (m.x74 -
    m.x101)**2 + (m.x144 - m.x171)**2) + 1 / sqrt((m.x4 - m.x32)**2 + (m.x74 -
    m.x102)**2 + (m.x144 - m.x172)**2) + 1 / sqrt((m.x4 - m.x33)**2 + (m.x74 -
    m.x103)**2 + (m.x144 - m.x173)**2) + 1 / sqrt((m.x4 - m.x34)**2 + (m.x74 -
    m.x104)**2 + (m.x144 - m.x174)**2) + 1 / sqrt((m.x4 - m.x35)**2 + (m.x74 -
    m.x105)**2 + (m.x144 - m.x175)**2) + 1 / sqrt((m.x4 - m.x36)**2 + (m.x74 -
    m.x106)**2 + (m.x144 - m.x176)**2) + 1 / sqrt((m.x4 - m.x37)**2 + (m.x74 -
    m.x107)**2 + (m.x144 - m.x177)**2) + 1 / sqrt((m.x4 - m.x38)**2 + (m.x74 -
    m.x108)**2 + (m.x144 - m.x178)**2) + 1 / sqrt((m.x4 - m.x39)**2 + (m.x74 -
    m.x109)**2 + (m.x144 - m.x179)**2) + 1 / sqrt((m.x4 - m.x40)**2 + (m.x74 -
    m.x110)**2 + (m.x144 - m.x180)**2) + 1 / sqrt((m.x4 - m.x41)**2 + (m.x74 -
    m.x111)**2 + (m.x144 - m.x181)**2) + 1 / sqrt((m.x4 - m.x42)**2 + (m.x74 -
    m.x112)**2 + (m.x144 - m.x182)**2) + 1 / sqrt((m.x4 - m.x43)**2 + (m.x74 -
    m.x113)**2 + (m.x144 - m.x183)**2) + 1 / sqrt((m.x4 - m.x44)**2 + (m.x74 -
    m.x114)**2 + (m.x144 - m.x184)**2) + 1 / sqrt((m.x4 - m.x45)**2 + (m.x74 -
    m.x115)**2 + (m.x144 - m.x185)**2) + 1 / sqrt((m.x4 - m.x46)**2 + (m.x74 -
    m.x116)**2 + (m.x144 - m.x186)**2) + 1 / sqrt((m.x4 - m.x47)**2 + (m.x74 -
    m.x117)**2 + (m.x144 - m.x187)**2) + 1 / sqrt((m.x4 - m.x48)**2 + (m.x74 -
    m.x118)**2 + (m.x144 - m.x188)**2) + 1 / sqrt((m.x4 - m.x49)**2 + (m.x74 -
    m.x119)**2 + (m.x144 - m.x189)**2) + 1 / sqrt((m.x4 - m.x50)**2 + (m.x74 -
    m.x120)**2 + (m.x144 - m.x190)**2) + 1 / sqrt((m.x4 - m.x51)**2 + (m.x74 -
    m.x121)**2 + (m.x144 - m.x191)**2) + 1 / sqrt((m.x4 - m.x52)**2 + (m.x74 -
    m.x122)**2 + (m.x144 - m.x192)**2) + 1 / sqrt((m.x4 - m.x53)**2 + (m.x74 -
    m.x123)**2 + (m.x144 - m.x193)**2) + 1 / sqrt((m.x4 - m.x54)**2 + (m.x74 -
    m.x124)**2 + (m.x144 - m.x194)**2) + 1 / sqrt((m.x4 - m.x55)**2 + (m.x74 -
    m.x125)**2 + (m.x144 - m.x195)**2) + 1 / sqrt((m.x4 - m.x56)**2 + (m.x74 -
    m.x126)**2 + (m.x144 - m.x196)**2) + 1 / sqrt((m.x4 - m.x57)**2 + (m.x74 -
    m.x127)**2 + (m.x144 - m.x197)**2) + 1 / sqrt((m.x4 - m.x58)**2 + (m.x74 -
    m.x128)**2 + (m.x144 - m.x198)**2) + 1 / sqrt((m.x4 - m.x59)**2 + (m.x74 -
    m.x129)**2 + (m.x144 - m.x199)**2) + 1 / sqrt((m.x4 - m.x60)**2 + (m.x74 -
    m.x130)**2 + (m.x144 - m.x200)**2) + 1 / sqrt((m.x4 - m.x61)**2 + (m.x74 -
    m.x131)**2 + (m.x144 - m.x201)**2) + 1 / sqrt((m.x4 - m.x62)**2 + (m.x74 -
    m.x132)**2 + (m.x144 - m.x202)**2) + 1 / sqrt((m.x4 - m.x63)**2 + (m.x74 -
    m.x133)**2 + (m.x144 - m.x203)**2) + 1 / sqrt((m.x4 - m.x64)**2 + (m.x74 -
    m.x134)**2 + (m.x144 - m.x204)**2) + 1 / sqrt((m.x4 - m.x65)**2 + (m.x74 -
    m.x135)**2 + (m.x144 - m.x205)**2) + 1 / sqrt((m.x4 - m.x66)**2 + (m.x74 -
    m.x136)**2 + (m.x144 - m.x206)**2) + 1 / sqrt((m.x4 - m.x67)**2 + (m.x74 -
    m.x137)**2 + (m.x144 - m.x207)**2) + 1 / sqrt((m.x4 - m.x68)**2 + (m.x74 -
    m.x138)**2 + (m.x144 - m.x208)**2) + 1 / sqrt((m.x4 - m.x69)**2 + (m.x74 -
    m.x139)**2 + (m.x144 - m.x209)**2) + 1 / sqrt((m.x4 - m.x70)**2 + (m.x74 -
    m.x140)**2 + (m.x144 - m.x210)**2) + 1 / sqrt((m.x5 - m.x6)**2 + (m.x75 -
    m.x76)**2 + (m.x145 - m.x146)**2) + 1 / sqrt((m.x5 - m.x7)**2 + (m.x75 -
    m.x77)**2 + (m.x145 - m.x147)**2) + 1 / sqrt((m.x5 - m.x8)**2 + (m.x75 -
    m.x78)**2 + (m.x145 - m.x148)**2) + 1 / sqrt((m.x5 - m.x9)**2 + (m.x75 -
    m.x79)**2 + (m.x145 - m.x149)**2) + 1 / sqrt((m.x5 - m.x10)**2 + (m.x75 -
    m.x80)**2 + (m.x145 - m.x150)**2) + 1 / sqrt((m.x5 - m.x11)**2 + (m.x75 -
    m.x81)**2 + (m.x145 - m.x151)**2) + 1 / sqrt((m.x5 - m.x12)**2 + (m.x75 -
    m.x82)**2 + (m.x145 - m.x152)**2) + 1 / sqrt((m.x5 - m.x13)**2 + (m.x75 -
    m.x83)**2 + (m.x145 - m.x153)**2) + 1 / sqrt((m.x5 - m.x14)**2 + (m.x75 -
    m.x84)**2 + (m.x145 - m.x154)**2) + 1 / sqrt((m.x5 - m.x15)**2 + (m.x75 -
    m.x85)**2 + (m.x145 - m.x155)**2) + 1 / sqrt((m.x5 - m.x16)**2 + (m.x75 -
    m.x86)**2 + (m.x145 - m.x156)**2) + 1 / sqrt((m.x5 - m.x17)**2 + (m.x75 -
    m.x87)**2 + (m.x145 - m.x157)**2) + 1 / sqrt((m.x5 - m.x18)**2 + (m.x75 -
    m.x88)**2 + (m.x145 - m.x158)**2) + 1 / sqrt((m.x5 - m.x19)**2 + (m.x75 -
    m.x89)**2 + (m.x145 - m.x159)**2) + 1 / sqrt((m.x5 - m.x20)**2 + (m.x75 -
    m.x90)**2 + (m.x145 - m.x160)**2) + 1 / sqrt((m.x5 - m.x21)**2 + (m.x75 -
    m.x91)**2 + (m.x145 - m.x161)**2) + 1 / sqrt((m.x5 - m.x22)**2 + (m.x75 -
    m.x92)**2 + (m.x145 - m.x162)**2) + 1 / sqrt((m.x5 - m.x23)**2 + (m.x75 -
    m.x93)**2 + (m.x145 - m.x163)**2) + 1 / sqrt((m.x5 - m.x24)**2 + (m.x75 -
    m.x94)**2 + (m.x145 - m.x164)**2) + 1 / sqrt((m.x5 - m.x25)**2 + (m.x75 -
    m.x95)**2 + (m.x145 - m.x165)**2) + 1 / sqrt((m.x5 - m.x26)**2 + (m.x75 -
    m.x96)**2 + (m.x145 - m.x166)**2) + 1 / sqrt((m.x5 - m.x27)**2 + (m.x75 -
    m.x97)**2 + (m.x145 - m.x167)**2) + 1 / sqrt((m.x5 - m.x28)**2 + (m.x75 -
    m.x98)**2 + (m.x145 - m.x168)**2) + 1 / sqrt((m.x5 - m.x29)**2 + (m.x75 -
    m.x99)**2 + (m.x145 - m.x169)**2) + 1 / sqrt((m.x5 - m.x30)**2 + (m.x75 -
    m.x100)**2 + (m.x145 - m.x170)**2) + 1 / sqrt((m.x5 - m.x31)**2 + (m.x75 -
    m.x101)**2 + (m.x145 - m.x171)**2) + 1 / sqrt((m.x5 - m.x32)**2 + (m.x75 -
    m.x102)**2 + (m.x145 - m.x172)**2) + 1 / sqrt((m.x5 - m.x33)**2 + (m.x75 -
    m.x103)**2 + (m.x145 - m.x173)**2) + 1 / sqrt((m.x5 - m.x34)**2 + (m.x75 -
    m.x104)**2 + (m.x145 - m.x174)**2) + 1 / sqrt((m.x5 - m.x35)**2 + (m.x75 -
    m.x105)**2 + (m.x145 - m.x175)**2) + 1 / sqrt((m.x5 - m.x36)**2 + (m.x75 -
    m.x106)**2 + (m.x145 - m.x176)**2) + 1 / sqrt((m.x5 - m.x37)**2 + (m.x75 -
    m.x107)**2 + (m.x145 - m.x177)**2) + 1 / sqrt((m.x5 - m.x38)**2 + (m.x75 -
    m.x108)**2 + (m.x145 - m.x178)**2) + 1 / sqrt((m.x5 - m.x39)**2 + (m.x75 -
    m.x109)**2 + (m.x145 - m.x179)**2) + 1 / sqrt((m.x5 - m.x40)**2 + (m.x75 -
    m.x110)**2 + (m.x145 - m.x180)**2) + 1 / sqrt((m.x5 - m.x41)**2 + (m.x75 -
    m.x111)**2 + (m.x145 - m.x181)**2) + 1 / sqrt((m.x5 - m.x42)**2 + (m.x75 -
    m.x112)**2 + (m.x145 - m.x182)**2) + 1 / sqrt((m.x5 - m.x43)**2 + (m.x75 -
    m.x113)**2 + (m.x145 - m.x183)**2) + 1 / sqrt((m.x5 - m.x44)**2 + (m.x75 -
    m.x114)**2 + (m.x145 - m.x184)**2) + 1 / sqrt((m.x5 - m.x45)**2 + (m.x75 -
    m.x115)**2 + (m.x145 - m.x185)**2) + 1 / sqrt((m.x5 - m.x46)**2 + (m.x75 -
    m.x116)**2 + (m.x145 - m.x186)**2) + 1 / sqrt((m.x5 - m.x47)**2 + (m.x75 -
    m.x117)**2 + (m.x145 - m.x187)**2) + 1 / sqrt((m.x5 - m.x48)**2 + (m.x75 -
    m.x118)**2 + (m.x145 - m.x188)**2) + 1 / sqrt((m.x5 - m.x49)**2 + (m.x75 -
    m.x119)**2 + (m.x145 - m.x189)**2) + 1 / sqrt((m.x5 - m.x50)**2 + (m.x75 -
    m.x120)**2 + (m.x145 - m.x190)**2) + 1 / sqrt((m.x5 - m.x51)**2 + (m.x75 -
    m.x121)**2 + (m.x145 - m.x191)**2) + 1 / sqrt((m.x5 - m.x52)**2 + (m.x75 -
    m.x122)**2 + (m.x145 - m.x192)**2) + 1 / sqrt((m.x5 - m.x53)**2 + (m.x75 -
    m.x123)**2 + (m.x145 - m.x193)**2) + 1 / sqrt((m.x5 - m.x54)**2 + (m.x75 -
    m.x124)**2 + (m.x145 - m.x194)**2) + 1 / sqrt((m.x5 - m.x55)**2 + (m.x75 -
    m.x125)**2 + (m.x145 - m.x195)**2) + 1 / sqrt((m.x5 - m.x56)**2 + (m.x75 -
    m.x126)**2 + (m.x145 - m.x196)**2) + 1 / sqrt((m.x5 - m.x57)**2 + (m.x75 -
    m.x127)**2 + (m.x145 - m.x197)**2) + 1 / sqrt((m.x5 - m.x58)**2 + (m.x75 -
    m.x128)**2 + (m.x145 - m.x198)**2) + 1 / sqrt((m.x5 - m.x59)**2 + (m.x75 -
    m.x129)**2 + (m.x145 - m.x199)**2) + 1 / sqrt((m.x5 - m.x60)**2 + (m.x75 -
    m.x130)**2 + (m.x145 - m.x200)**2) + 1 / sqrt((m.x5 - m.x61)**2 + (m.x75 -
    m.x131)**2 + (m.x145 - m.x201)**2) + 1 / sqrt((m.x5 - m.x62)**2 + (m.x75 -
    m.x132)**2 + (m.x145 - m.x202)**2) + 1 / sqrt((m.x5 - m.x63)**2 + (m.x75 -
    m.x133)**2 + (m.x145 - m.x203)**2) + 1 / sqrt((m.x5 - m.x64)**2 + (m.x75 -
    m.x134)**2 + (m.x145 - m.x204)**2) + 1 / sqrt((m.x5 - m.x65)**2 + (m.x75 -
    m.x135)**2 + (m.x145 - m.x205)**2) + 1 / sqrt((m.x5 - m.x66)**2 + (m.x75 -
    m.x136)**2 + (m.x145 - m.x206)**2) + 1 / sqrt((m.x5 - m.x67)**2 + (m.x75 -
    m.x137)**2 + (m.x145 - m.x207)**2) + 1 / sqrt((m.x5 - m.x68)**2 + (m.x75 -
    m.x138)**2 + (m.x145 - m.x208)**2) + 1 / sqrt((m.x5 - m.x69)**2 + (m.x75 -
    m.x139)**2 + (m.x145 - m.x209)**2) + 1 / sqrt((m.x5 - m.x70)**2 + (m.x75 -
    m.x140)**2 + (m.x145 - m.x210)**2) + 1 / sqrt((m.x6 - m.x7)**2 + (m.x76 -
    m.x77)**2 + (m.x146 - m.x147)**2) + 1 / sqrt((m.x6 - m.x8)**2 + (m.x76 -
    m.x78)**2 + (m.x146 - m.x148)**2) + 1 / sqrt((m.x6 - m.x9)**2 + (m.x76 -
    m.x79)**2 + (m.x146 - m.x149)**2) + 1 / sqrt((m.x6 - m.x10)**2 + (m.x76 -
    m.x80)**2 + (m.x146 - m.x150)**2) + 1 / sqrt((m.x6 - m.x11)**2 + (m.x76 -
    m.x81)**2 + (m.x146 - m.x151)**2) + 1 / sqrt((m.x6 - m.x12)**2 + (m.x76 -
    m.x82)**2 + (m.x146 - m.x152)**2) + 1 / sqrt((m.x6 - m.x13)**2 + (m.x76 -
    m.x83)**2 + (m.x146 - m.x153)**2) + 1 / sqrt((m.x6 - m.x14)**2 + (m.x76 -
    m.x84)**2 + (m.x146 - m.x154)**2) + 1 / sqrt((m.x6 - m.x15)**2 + (m.x76 -
    m.x85)**2 + (m.x146 - m.x155)**2) + 1 / sqrt((m.x6 - m.x16)**2 + (m.x76 -
    m.x86)**2 + (m.x146 - m.x156)**2) + 1 / sqrt((m.x6 - m.x17)**2 + (m.x76 -
    m.x87)**2 + (m.x146 - m.x157)**2) + 1 / sqrt((m.x6 - m.x18)**2 + (m.x76 -
    m.x88)**2 + (m.x146 - m.x158)**2) + 1 / sqrt((m.x6 - m.x19)**2 + (m.x76 -
    m.x89)**2 + (m.x146 - m.x159)**2) + 1 / sqrt((m.x6 - m.x20)**2 + (m.x76 -
    m.x90)**2 + (m.x146 - m.x160)**2) + 1 / sqrt((m.x6 - m.x21)**2 + (m.x76 -
    m.x91)**2 + (m.x146 - m.x161)**2) + 1 / sqrt((m.x6 - m.x22)**2 + (m.x76 -
    m.x92)**2 + (m.x146 - m.x162)**2) + 1 / sqrt((m.x6 - m.x23)**2 + (m.x76 -
    m.x93)**2 + (m.x146 - m.x163)**2) + 1 / sqrt((m.x6 - m.x24)**2 + (m.x76 -
    m.x94)**2 + (m.x146 - m.x164)**2) + 1 / sqrt((m.x6 - m.x25)**2 + (m.x76 -
    m.x95)**2 + (m.x146 - m.x165)**2) + 1 / sqrt((m.x6 - m.x26)**2 + (m.x76 -
    m.x96)**2 + (m.x146 - m.x166)**2) + 1 / sqrt((m.x6 - m.x27)**2 + (m.x76 -
    m.x97)**2 + (m.x146 - m.x167)**2) + 1 / sqrt((m.x6 - m.x28)**2 + (m.x76 -
    m.x98)**2 + (m.x146 - m.x168)**2) + 1 / sqrt((m.x6 - m.x29)**2 + (m.x76 -
    m.x99)**2 + (m.x146 - m.x169)**2) + 1 / sqrt((m.x6 - m.x30)**2 + (m.x76 -
    m.x100)**2 + (m.x146 - m.x170)**2) + 1 / sqrt((m.x6 - m.x31)**2 + (m.x76 -
    m.x101)**2 + (m.x146 - m.x171)**2) + 1 / sqrt((m.x6 - m.x32)**2 + (m.x76 -
    m.x102)**2 + (m.x146 - m.x172)**2) + 1 / sqrt((m.x6 - m.x33)**2 + (m.x76 -
    m.x103)**2 + (m.x146 - m.x173)**2) + 1 / sqrt((m.x6 - m.x34)**2 + (m.x76 -
    m.x104)**2 + (m.x146 - m.x174)**2) + 1 / sqrt((m.x6 - m.x35)**2 + (m.x76 -
    m.x105)**2 + (m.x146 - m.x175)**2) + 1 / sqrt((m.x6 - m.x36)**2 + (m.x76 -
    m.x106)**2 + (m.x146 - m.x176)**2) + 1 / sqrt((m.x6 - m.x37)**2 + (m.x76 -
    m.x107)**2 + (m.x146 - m.x177)**2) + 1 / sqrt((m.x6 - m.x38)**2 + (m.x76 -
    m.x108)**2 + (m.x146 - m.x178)**2) + 1 / sqrt((m.x6 - m.x39)**2 + (m.x76 -
    m.x109)**2 + (m.x146 - m.x179)**2) + 1 / sqrt((m.x6 - m.x40)**2 + (m.x76 -
    m.x110)**2 + (m.x146 - m.x180)**2) + 1 / sqrt((m.x6 - m.x41)**2 + (m.x76 -
    m.x111)**2 + (m.x146 - m.x181)**2) + 1 / sqrt((m.x6 - m.x42)**2 + (m.x76 -
    m.x112)**2 + (m.x146 - m.x182)**2) + 1 / sqrt((m.x6 - m.x43)**2 + (m.x76 -
    m.x113)**2 + (m.x146 - m.x183)**2) + 1 / sqrt((m.x6 - m.x44)**2 + (m.x76 -
    m.x114)**2 + (m.x146 - m.x184)**2) + 1 / sqrt((m.x6 - m.x45)**2 + (m.x76 -
    m.x115)**2 + (m.x146 - m.x185)**2) + 1 / sqrt((m.x6 - m.x46)**2 + (m.x76 -
    m.x116)**2 + (m.x146 - m.x186)**2) + 1 / sqrt((m.x6 - m.x47)**2 + (m.x76 -
    m.x117)**2 + (m.x146 - m.x187)**2) + 1 / sqrt((m.x6 - m.x48)**2 + (m.x76 -
    m.x118)**2 + (m.x146 - m.x188)**2) + 1 / sqrt((m.x6 - m.x49)**2 + (m.x76 -
    m.x119)**2 + (m.x146 - m.x189)**2) + 1 / sqrt((m.x6 - m.x50)**2 + (m.x76 -
    m.x120)**2 + (m.x146 - m.x190)**2) + 1 / sqrt((m.x6 - m.x51)**2 + (m.x76 -
    m.x121)**2 + (m.x146 - m.x191)**2) + 1 / sqrt((m.x6 - m.x52)**2 + (m.x76 -
    m.x122)**2 + (m.x146 - m.x192)**2) + 1 / sqrt((m.x6 - m.x53)**2 + (m.x76 -
    m.x123)**2 + (m.x146 - m.x193)**2) + 1 / sqrt((m.x6 - m.x54)**2 + (m.x76 -
    m.x124)**2 + (m.x146 - m.x194)**2) + 1 / sqrt((m.x6 - m.x55)**2 + (m.x76 -
    m.x125)**2 + (m.x146 - m.x195)**2) + 1 / sqrt((m.x6 - m.x56)**2 + (m.x76 -
    m.x126)**2 + (m.x146 - m.x196)**2) + 1 / sqrt((m.x6 - m.x57)**2 + (m.x76 -
    m.x127)**2 + (m.x146 - m.x197)**2) + 1 / sqrt((m.x6 - m.x58)**2 + (m.x76 -
    m.x128)**2 + (m.x146 - m.x198)**2) + 1 / sqrt((m.x6 - m.x59)**2 + (m.x76 -
    m.x129)**2 + (m.x146 - m.x199)**2) + 1 / sqrt((m.x6 - m.x60)**2 + (m.x76 -
    m.x130)**2 + (m.x146 - m.x200)**2) + 1 / sqrt((m.x6 - m.x61)**2 + (m.x76 -
    m.x131)**2 + (m.x146 - m.x201)**2) + 1 / sqrt((m.x6 - m.x62)**2 + (m.x76 -
    m.x132)**2 + (m.x146 - m.x202)**2) + 1 / sqrt((m.x6 - m.x63)**2 + (m.x76 -
    m.x133)**2 + (m.x146 - m.x203)**2) + 1 / sqrt((m.x6 - m.x64)**2 + (m.x76 -
    m.x134)**2 + (m.x146 - m.x204)**2) + 1 / sqrt((m.x6 - m.x65)**2 + (m.x76 -
    m.x135)**2 + (m.x146 - m.x205)**2) + 1 / sqrt((m.x6 - m.x66)**2 + (m.x76 -
    m.x136)**2 + (m.x146 - m.x206)**2) + 1 / sqrt((m.x6 - m.x67)**2 + (m.x76 -
    m.x137)**2 + (m.x146 - m.x207)**2) + 1 / sqrt((m.x6 - m.x68)**2 + (m.x76 -
    m.x138)**2 + (m.x146 - m.x208)**2) + 1 / sqrt((m.x6 - m.x69)**2 + (m.x76 -
    m.x139)**2 + (m.x146 - m.x209)**2) + 1 / sqrt((m.x6 - m.x70)**2 + (m.x76 -
    m.x140)**2 + (m.x146 - m.x210)**2) + 1 / sqrt((m.x7 - m.x8)**2 + (m.x77 -
    m.x78)**2 + (m.x147 - m.x148)**2) + 1 / sqrt((m.x7 - m.x9)**2 + (m.x77 -
    m.x79)**2 + (m.x147 - m.x149)**2) + 1 / sqrt((m.x7 - m.x10)**2 + (m.x77 -
    m.x80)**2 + (m.x147 - m.x150)**2) + 1 / sqrt((m.x7 - m.x11)**2 + (m.x77 -
    m.x81)**2 + (m.x147 - m.x151)**2) + 1 / sqrt((m.x7 - m.x12)**2 + (m.x77 -
    m.x82)**2 + (m.x147 - m.x152)**2) + 1 / sqrt((m.x7 - m.x13)**2 + (m.x77 -
    m.x83)**2 + (m.x147 - m.x153)**2) + 1 / sqrt((m.x7 - m.x14)**2 + (m.x77 -
    m.x84)**2 + (m.x147 - m.x154)**2) + 1 / sqrt((m.x7 - m.x15)**2 + (m.x77 -
    m.x85)**2 + (m.x147 - m.x155)**2) + 1 / sqrt((m.x7 - m.x16)**2 + (m.x77 -
    m.x86)**2 + (m.x147 - m.x156)**2) + 1 / sqrt((m.x7 - m.x17)**2 + (m.x77 -
    m.x87)**2 + (m.x147 - m.x157)**2) + 1 / sqrt((m.x7 - m.x18)**2 + (m.x77 -
    m.x88)**2 + (m.x147 - m.x158)**2) + 1 / sqrt((m.x7 - m.x19)**2 + (m.x77 -
    m.x89)**2 + (m.x147 - m.x159)**2) + 1 / sqrt((m.x7 - m.x20)**2 + (m.x77 -
    m.x90)**2 + (m.x147 - m.x160)**2) + 1 / sqrt((m.x7 - m.x21)**2 + (m.x77 -
    m.x91)**2 + (m.x147 - m.x161)**2) + 1 / sqrt((m.x7 - m.x22)**2 + (m.x77 -
    m.x92)**2 + (m.x147 - m.x162)**2) + 1 / sqrt((m.x7 - m.x23)**2 + (m.x77 -
    m.x93)**2 + (m.x147 - m.x163)**2) + 1 / sqrt((m.x7 - m.x24)**2 + (m.x77 -
    m.x94)**2 + (m.x147 - m.x164)**2) + 1 / sqrt((m.x7 - m.x25)**2 + (m.x77 -
    m.x95)**2 + (m.x147 - m.x165)**2) + 1 / sqrt((m.x7 - m.x26)**2 + (m.x77 -
    m.x96)**2 + (m.x147 - m.x166)**2) + 1 / sqrt((m.x7 - m.x27)**2 + (m.x77 -
    m.x97)**2 + (m.x147 - m.x167)**2) + 1 / sqrt((m.x7 - m.x28)**2 + (m.x77 -
    m.x98)**2 + (m.x147 - m.x168)**2) + 1 / sqrt((m.x7 - m.x29)**2 + (m.x77 -
    m.x99)**2 + (m.x147 - m.x169)**2) + 1 / sqrt((m.x7 - m.x30)**2 + (m.x77 -
    m.x100)**2 + (m.x147 - m.x170)**2) + 1 / sqrt((m.x7 - m.x31)**2 + (m.x77 -
    m.x101)**2 + (m.x147 - m.x171)**2) + 1 / sqrt((m.x7 - m.x32)**2 + (m.x77 -
    m.x102)**2 + (m.x147 - m.x172)**2) + 1 / sqrt((m.x7 - m.x33)**2 + (m.x77 -
    m.x103)**2 + (m.x147 - m.x173)**2) + 1 / sqrt((m.x7 - m.x34)**2 + (m.x77 -
    m.x104)**2 + (m.x147 - m.x174)**2) + 1 / sqrt((m.x7 - m.x35)**2 + (m.x77 -
    m.x105)**2 + (m.x147 - m.x175)**2) + 1 / sqrt((m.x7 - m.x36)**2 + (m.x77 -
    m.x106)**2 + (m.x147 - m.x176)**2) + 1 / sqrt((m.x7 - m.x37)**2 + (m.x77 -
    m.x107)**2 + (m.x147 - m.x177)**2) + 1 / sqrt((m.x7 - m.x38)**2 + (m.x77 -
    m.x108)**2 + (m.x147 - m.x178)**2) + 1 / sqrt((m.x7 - m.x39)**2 + (m.x77 -
    m.x109)**2 + (m.x147 - m.x179)**2) + 1 / sqrt((m.x7 - m.x40)**2 + (m.x77 -
    m.x110)**2 + (m.x147 - m.x180)**2) + 1 / sqrt((m.x7 - m.x41)**2 + (m.x77 -
    m.x111)**2 + (m.x147 - m.x181)**2) + 1 / sqrt((m.x7 - m.x42)**2 + (m.x77 -
    m.x112)**2 + (m.x147 - m.x182)**2) + 1 / sqrt((m.x7 - m.x43)**2 + (m.x77 -
    m.x113)**2 + (m.x147 - m.x183)**2) + 1 / sqrt((m.x7 - m.x44)**2 + (m.x77 -
    m.x114)**2 + (m.x147 - m.x184)**2) + 1 / sqrt((m.x7 - m.x45)**2 + (m.x77 -
    m.x115)**2 + (m.x147 - m.x185)**2) + 1 / sqrt((m.x7 - m.x46)**2 + (m.x77 -
    m.x116)**2 + (m.x147 - m.x186)**2) + 1 / sqrt((m.x7 - m.x47)**2 + (m.x77 -
    m.x117)**2 + (m.x147 - m.x187)**2) + 1 / sqrt((m.x7 - m.x48)**2 + (m.x77 -
    m.x118)**2 + (m.x147 - m.x188)**2) + 1 / sqrt((m.x7 - m.x49)**2 + (m.x77 -
    m.x119)**2 + (m.x147 - m.x189)**2) + 1 / sqrt((m.x7 - m.x50)**2 + (m.x77 -
    m.x120)**2 + (m.x147 - m.x190)**2) + 1 / sqrt((m.x7 - m.x51)**2 + (m.x77 -
    m.x121)**2 + (m.x147 - m.x191)**2) + 1 / sqrt((m.x7 - m.x52)**2 + (m.x77 -
    m.x122)**2 + (m.x147 - m.x192)**2) + 1 / sqrt((m.x7 - m.x53)**2 + (m.x77 -
    m.x123)**2 + (m.x147 - m.x193)**2) + 1 / sqrt((m.x7 - m.x54)**2 + (m.x77 -
    m.x124)**2 + (m.x147 - m.x194)**2) + 1 / sqrt((m.x7 - m.x55)**2 + (m.x77 -
    m.x125)**2 + (m.x147 - m.x195)**2) + 1 / sqrt((m.x7 - m.x56)**2 + (m.x77 -
    m.x126)**2 + (m.x147 - m.x196)**2) + 1 / sqrt((m.x7 - m.x57)**2 + (m.x77 -
    m.x127)**2 + (m.x147 - m.x197)**2) + 1 / sqrt((m.x7 - m.x58)**2 + (m.x77 -
    m.x128)**2 + (m.x147 - m.x198)**2) + 1 / sqrt((m.x7 - m.x59)**2 + (m.x77 -
    m.x129)**2 + (m.x147 - m.x199)**2) + 1 / sqrt((m.x7 - m.x60)**2 + (m.x77 -
    m.x130)**2 + (m.x147 - m.x200)**2) + 1 / sqrt((m.x7 - m.x61)**2 + (m.x77 -
    m.x131)**2 + (m.x147 - m.x201)**2) + 1 / sqrt((m.x7 - m.x62)**2 + (m.x77 -
    m.x132)**2 + (m.x147 - m.x202)**2) + 1 / sqrt((m.x7 - m.x63)**2 + (m.x77 -
    m.x133)**2 + (m.x147 - m.x203)**2) + 1 / sqrt((m.x7 - m.x64)**2 + (m.x77 -
    m.x134)**2 + (m.x147 - m.x204)**2) + 1 / sqrt((m.x7 - m.x65)**2 + (m.x77 -
    m.x135)**2 + (m.x147 - m.x205)**2) + 1 / sqrt((m.x7 - m.x66)**2 + (m.x77 -
    m.x136)**2 + (m.x147 - m.x206)**2) + 1 / sqrt((m.x7 - m.x67)**2 + (m.x77 -
    m.x137)**2 + (m.x147 - m.x207)**2) + 1 / sqrt((m.x7 - m.x68)**2 + (m.x77 -
    m.x138)**2 + (m.x147 - m.x208)**2) + 1 / sqrt((m.x7 - m.x69)**2 + (m.x77 -
    m.x139)**2 + (m.x147 - m.x209)**2) + 1 / sqrt((m.x7 - m.x70)**2 + (m.x77 -
    m.x140)**2 + (m.x147 - m.x210)**2) + 1 / sqrt((m.x8 - m.x9)**2 + (m.x78 -
    m.x79)**2 + (m.x148 - m.x149)**2) + 1 / sqrt((m.x8 - m.x10)**2 + (m.x78 -
    m.x80)**2 + (m.x148 - m.x150)**2) + 1 / sqrt((m.x8 - m.x11)**2 + (m.x78 -
    m.x81)**2 + (m.x148 - m.x151)**2) + 1 / sqrt((m.x8 - m.x12)**2 + (m.x78 -
    m.x82)**2 + (m.x148 - m.x152)**2) + 1 / sqrt((m.x8 - m.x13)**2 + (m.x78 -
    m.x83)**2 + (m.x148 - m.x153)**2) + 1 / sqrt((m.x8 - m.x14)**2 + (m.x78 -
    m.x84)**2 + (m.x148 - m.x154)**2) + 1 / sqrt((m.x8 - m.x15)**2 + (m.x78 -
    m.x85)**2 + (m.x148 - m.x155)**2) + 1 / sqrt((m.x8 - m.x16)**2 + (m.x78 -
    m.x86)**2 + (m.x148 - m.x156)**2) + 1 / sqrt((m.x8 - m.x17)**2 + (m.x78 -
    m.x87)**2 + (m.x148 - m.x157)**2) + 1 / sqrt((m.x8 - m.x18)**2 + (m.x78 -
    m.x88)**2 + (m.x148 - m.x158)**2) + 1 / sqrt((m.x8 - m.x19)**2 + (m.x78 -
    m.x89)**2 + (m.x148 - m.x159)**2) + 1 / sqrt((m.x8 - m.x20)**2 + (m.x78 -
    m.x90)**2 + (m.x148 - m.x160)**2) + 1 / sqrt((m.x8 - m.x21)**2 + (m.x78 -
    m.x91)**2 + (m.x148 - m.x161)**2) + 1 / sqrt((m.x8 - m.x22)**2 + (m.x78 -
    m.x92)**2 + (m.x148 - m.x162)**2) + 1 / sqrt((m.x8 - m.x23)**2 + (m.x78 -
    m.x93)**2 + (m.x148 - m.x163)**2) + 1 / sqrt((m.x8 - m.x24)**2 + (m.x78 -
    m.x94)**2 + (m.x148 - m.x164)**2) + 1 / sqrt((m.x8 - m.x25)**2 + (m.x78 -
    m.x95)**2 + (m.x148 - m.x165)**2) + 1 / sqrt((m.x8 - m.x26)**2 + (m.x78 -
    m.x96)**2 + (m.x148 - m.x166)**2) + 1 / sqrt((m.x8 - m.x27)**2 + (m.x78 -
    m.x97)**2 + (m.x148 - m.x167)**2) + 1 / sqrt((m.x8 - m.x28)**2 + (m.x78 -
    m.x98)**2 + (m.x148 - m.x168)**2) + 1 / sqrt((m.x8 - m.x29)**2 + (m.x78 -
    m.x99)**2 + (m.x148 - m.x169)**2) + 1 / sqrt((m.x8 - m.x30)**2 + (m.x78 -
    m.x100)**2 + (m.x148 - m.x170)**2) + 1 / sqrt((m.x8 - m.x31)**2 + (m.x78 -
    m.x101)**2 + (m.x148 - m.x171)**2) + 1 / sqrt((m.x8 - m.x32)**2 + (m.x78 -
    m.x102)**2 + (m.x148 - m.x172)**2) + 1 / sqrt((m.x8 - m.x33)**2 + (m.x78 -
    m.x103)**2 + (m.x148 - m.x173)**2) + 1 / sqrt((m.x8 - m.x34)**2 + (m.x78 -
    m.x104)**2 + (m.x148 - m.x174)**2) + 1 / sqrt((m.x8 - m.x35)**2 + (m.x78 -
    m.x105)**2 + (m.x148 - m.x175)**2) + 1 / sqrt((m.x8 - m.x36)**2 + (m.x78 -
    m.x106)**2 + (m.x148 - m.x176)**2) + 1 / sqrt((m.x8 - m.x37)**2 + (m.x78 -
    m.x107)**2 + (m.x148 - m.x177)**2) + 1 / sqrt((m.x8 - m.x38)**2 + (m.x78 -
    m.x108)**2 + (m.x148 - m.x178)**2) + 1 / sqrt((m.x8 - m.x39)**2 + (m.x78 -
    m.x109)**2 + (m.x148 - m.x179)**2) + 1 / sqrt((m.x8 - m.x40)**2 + (m.x78 -
    m.x110)**2 + (m.x148 - m.x180)**2) + 1 / sqrt((m.x8 - m.x41)**2 + (m.x78 -
    m.x111)**2 + (m.x148 - m.x181)**2) + 1 / sqrt((m.x8 - m.x42)**2 + (m.x78 -
    m.x112)**2 + (m.x148 - m.x182)**2) + 1 / sqrt((m.x8 - m.x43)**2 + (m.x78 -
    m.x113)**2 + (m.x148 - m.x183)**2) + 1 / sqrt((m.x8 - m.x44)**2 + (m.x78 -
    m.x114)**2 + (m.x148 - m.x184)**2) + 1 / sqrt((m.x8 - m.x45)**2 + (m.x78 -
    m.x115)**2 + (m.x148 - m.x185)**2) + 1 / sqrt((m.x8 - m.x46)**2 + (m.x78 -
    m.x116)**2 + (m.x148 - m.x186)**2) + 1 / sqrt((m.x8 - m.x47)**2 + (m.x78 -
    m.x117)**2 + (m.x148 - m.x187)**2) + 1 / sqrt((m.x8 - m.x48)**2 + (m.x78 -
    m.x118)**2 + (m.x148 - m.x188)**2) + 1 / sqrt((m.x8 - m.x49)**2 + (m.x78 -
    m.x119)**2 + (m.x148 - m.x189)**2) + 1 / sqrt((m.x8 - m.x50)**2 + (m.x78 -
    m.x120)**2 + (m.x148 - m.x190)**2) + 1 / sqrt((m.x8 - m.x51)**2 + (m.x78 -
    m.x121)**2 + (m.x148 - m.x191)**2) + 1 / sqrt((m.x8 - m.x52)**2 + (m.x78 -
    m.x122)**2 + (m.x148 - m.x192)**2) + 1 / sqrt((m.x8 - m.x53)**2 + (m.x78 -
    m.x123)**2 + (m.x148 - m.x193)**2) + 1 / sqrt((m.x8 - m.x54)**2 + (m.x78 -
    m.x124)**2 + (m.x148 - m.x194)**2) + 1 / sqrt((m.x8 - m.x55)**2 + (m.x78 -
    m.x125)**2 + (m.x148 - m.x195)**2) + 1 / sqrt((m.x8 - m.x56)**2 + (m.x78 -
    m.x126)**2 + (m.x148 - m.x196)**2) + 1 / sqrt((m.x8 - m.x57)**2 + (m.x78 -
    m.x127)**2 + (m.x148 - m.x197)**2) + 1 / sqrt((m.x8 - m.x58)**2 + (m.x78 -
    m.x128)**2 + (m.x148 - m.x198)**2) + 1 / sqrt((m.x8 - m.x59)**2 + (m.x78 -
    m.x129)**2 + (m.x148 - m.x199)**2) + 1 / sqrt((m.x8 - m.x60)**2 + (m.x78 -
    m.x130)**2 + (m.x148 - m.x200)**2) + 1 / sqrt((m.x8 - m.x61)**2 + (m.x78 -
    m.x131)**2 + (m.x148 - m.x201)**2) + 1 / sqrt((m.x8 - m.x62)**2 + (m.x78 -
    m.x132)**2 + (m.x148 - m.x202)**2) + 1 / sqrt((m.x8 - m.x63)**2 + (m.x78 -
    m.x133)**2 + (m.x148 - m.x203)**2) + 1 / sqrt((m.x8 - m.x64)**2 + (m.x78 -
    m.x134)**2 + (m.x148 - m.x204)**2) + 1 / sqrt((m.x8 - m.x65)**2 + (m.x78 -
    m.x135)**2 + (m.x148 - m.x205)**2) + 1 / sqrt((m.x8 - m.x66)**2 + (m.x78 -
    m.x136)**2 + (m.x148 - m.x206)**2) + 1 / sqrt((m.x8 - m.x67)**2 + (m.x78 -
    m.x137)**2 + (m.x148 - m.x207)**2) + 1 / sqrt((m.x8 - m.x68)**2 + (m.x78 -
    m.x138)**2 + (m.x148 - m.x208)**2) + 1 / sqrt((m.x8 - m.x69)**2 + (m.x78 -
    m.x139)**2 + (m.x148 - m.x209)**2) + 1 / sqrt((m.x8 - m.x70)**2 + (m.x78 -
    m.x140)**2 + (m.x148 - m.x210)**2) + 1 / sqrt((m.x9 - m.x10)**2 + (m.x79 -
    m.x80)**2 + (m.x149 - m.x150)**2) + 1 / sqrt((m.x9 - m.x11)**2 + (m.x79 -
    m.x81)**2 + (m.x149 - m.x151)**2) + 1 / sqrt((m.x9 - m.x12)**2 + (m.x79 -
    m.x82)**2 + (m.x149 - m.x152)**2) + 1 / sqrt((m.x9 - m.x13)**2 + (m.x79 -
    m.x83)**2 + (m.x149 - m.x153)**2) + 1 / sqrt((m.x9 - m.x14)**2 + (m.x79 -
    m.x84)**2 + (m.x149 - m.x154)**2) + 1 / sqrt((m.x9 - m.x15)**2 + (m.x79 -
    m.x85)**2 + (m.x149 - m.x155)**2) + 1 / sqrt((m.x9 - m.x16)**2 + (m.x79 -
    m.x86)**2 + (m.x149 - m.x156)**2) + 1 / sqrt((m.x9 - m.x17)**2 + (m.x79 -
    m.x87)**2 + (m.x149 - m.x157)**2) + 1 / sqrt((m.x9 - m.x18)**2 + (m.x79 -
    m.x88)**2 + (m.x149 - m.x158)**2) + 1 / sqrt((m.x9 - m.x19)**2 + (m.x79 -
    m.x89)**2 + (m.x149 - m.x159)**2) + 1 / sqrt((m.x9 - m.x20)**2 + (m.x79 -
    m.x90)**2 + (m.x149 - m.x160)**2) + 1 / sqrt((m.x9 - m.x21)**2 + (m.x79 -
    m.x91)**2 + (m.x149 - m.x161)**2) + 1 / sqrt((m.x9 - m.x22)**2 + (m.x79 -
    m.x92)**2 + (m.x149 - m.x162)**2) + 1 / sqrt((m.x9 - m.x23)**2 + (m.x79 -
    m.x93)**2 + (m.x149 - m.x163)**2) + 1 / sqrt((m.x9 - m.x24)**2 + (m.x79 -
    m.x94)**2 + (m.x149 - m.x164)**2) + 1 / sqrt((m.x9 - m.x25)**2 + (m.x79 -
    m.x95)**2 + (m.x149 - m.x165)**2) + 1 / sqrt((m.x9 - m.x26)**2 + (m.x79 -
    m.x96)**2 + (m.x149 - m.x166)**2) + 1 / sqrt((m.x9 - m.x27)**2 + (m.x79 -
    m.x97)**2 + (m.x149 - m.x167)**2) + 1 / sqrt((m.x9 - m.x28)**2 + (m.x79 -
    m.x98)**2 + (m.x149 - m.x168)**2) + 1 / sqrt((m.x9 - m.x29)**2 + (m.x79 -
    m.x99)**2 + (m.x149 - m.x169)**2) + 1 / sqrt((m.x9 - m.x30)**2 + (m.x79 -
    m.x100)**2 + (m.x149 - m.x170)**2) + 1 / sqrt((m.x9 - m.x31)**2 + (m.x79 -
    m.x101)**2 + (m.x149 - m.x171)**2) + 1 / sqrt((m.x9 - m.x32)**2 + (m.x79 -
    m.x102)**2 + (m.x149 - m.x172)**2) + 1 / sqrt((m.x9 - m.x33)**2 + (m.x79 -
    m.x103)**2 + (m.x149 - m.x173)**2) + 1 / sqrt((m.x9 - m.x34)**2 + (m.x79 -
    m.x104)**2 + (m.x149 - m.x174)**2) + 1 / sqrt((m.x9 - m.x35)**2 + (m.x79 -
    m.x105)**2 + (m.x149 - m.x175)**2) + 1 / sqrt((m.x9 - m.x36)**2 + (m.x79 -
    m.x106)**2 + (m.x149 - m.x176)**2) + 1 / sqrt((m.x9 - m.x37)**2 + (m.x79 -
    m.x107)**2 + (m.x149 - m.x177)**2) + 1 / sqrt((m.x9 - m.x38)**2 + (m.x79 -
    m.x108)**2 + (m.x149 - m.x178)**2) + 1 / sqrt((m.x9 - m.x39)**2 + (m.x79 -
    m.x109)**2 + (m.x149 - m.x179)**2) + 1 / sqrt((m.x9 - m.x40)**2 + (m.x79 -
    m.x110)**2 + (m.x149 - m.x180)**2) + 1 / sqrt((m.x9 - m.x41)**2 + (m.x79 -
    m.x111)**2 + (m.x149 - m.x181)**2) + 1 / sqrt((m.x9 - m.x42)**2 + (m.x79 -
    m.x112)**2 + (m.x149 - m.x182)**2) + 1 / sqrt((m.x9 - m.x43)**2 + (m.x79 -
    m.x113)**2 + (m.x149 - m.x183)**2) + 1 / sqrt((m.x9 - m.x44)**2 + (m.x79 -
    m.x114)**2 + (m.x149 - m.x184)**2) + 1 / sqrt((m.x9 - m.x45)**2 + (m.x79 -
    m.x115)**2 + (m.x149 - m.x185)**2) + 1 / sqrt((m.x9 - m.x46)**2 + (m.x79 -
    m.x116)**2 + (m.x149 - m.x186)**2) + 1 / sqrt((m.x9 - m.x47)**2 + (m.x79 -
    m.x117)**2 + (m.x149 - m.x187)**2) + 1 / sqrt((m.x9 - m.x48)**2 + (m.x79 -
    m.x118)**2 + (m.x149 - m.x188)**2) + 1 / sqrt((m.x9 - m.x49)**2 + (m.x79 -
    m.x119)**2 + (m.x149 - m.x189)**2) + 1 / sqrt((m.x9 - m.x50)**2 + (m.x79 -
    m.x120)**2 + (m.x149 - m.x190)**2) + 1 / sqrt((m.x9 - m.x51)**2 + (m.x79 -
    m.x121)**2 + (m.x149 - m.x191)**2) + 1 / sqrt((m.x9 - m.x52)**2 + (m.x79 -
    m.x122)**2 + (m.x149 - m.x192)**2) + 1 / sqrt((m.x9 - m.x53)**2 + (m.x79 -
    m.x123)**2 + (m.x149 - m.x193)**2) + 1 / sqrt((m.x9 - m.x54)**2 + (m.x79 -
    m.x124)**2 + (m.x149 - m.x194)**2) + 1 / sqrt((m.x9 - m.x55)**2 + (m.x79 -
    m.x125)**2 + (m.x149 - m.x195)**2) + 1 / sqrt((m.x9 - m.x56)**2 + (m.x79 -
    m.x126)**2 + (m.x149 - m.x196)**2) + 1 / sqrt((m.x9 - m.x57)**2 + (m.x79 -
    m.x127)**2 + (m.x149 - m.x197)**2) + 1 / sqrt((m.x9 - m.x58)**2 + (m.x79 -
    m.x128)**2 + (m.x149 - m.x198)**2) + 1 / sqrt((m.x9 - m.x59)**2 + (m.x79 -
    m.x129)**2 + (m.x149 - m.x199)**2) + 1 / sqrt((m.x9 - m.x60)**2 + (m.x79 -
    m.x130)**2 + (m.x149 - m.x200)**2) + 1 / sqrt((m.x9 - m.x61)**2 + (m.x79 -
    m.x131)**2 + (m.x149 - m.x201)**2) + 1 / sqrt((m.x9 - m.x62)**2 + (m.x79 -
    m.x132)**2 + (m.x149 - m.x202)**2) + 1 / sqrt((m.x9 - m.x63)**2 + (m.x79 -
    m.x133)**2 + (m.x149 - m.x203)**2) + 1 / sqrt((m.x9 - m.x64)**2 + (m.x79 -
    m.x134)**2 + (m.x149 - m.x204)**2) + 1 / sqrt((m.x9 - m.x65)**2 + (m.x79 -
    m.x135)**2 + (m.x149 - m.x205)**2) + 1 / sqrt((m.x9 - m.x66)**2 + (m.x79 -
    m.x136)**2 + (m.x149 - m.x206)**2) + 1 / sqrt((m.x9 - m.x67)**2 + (m.x79 -
    m.x137)**2 + (m.x149 - m.x207)**2) + 1 / sqrt((m.x9 - m.x68)**2 + (m.x79 -
    m.x138)**2 + (m.x149 - m.x208)**2) + 1 / sqrt((m.x9 - m.x69)**2 + (m.x79 -
    m.x139)**2 + (m.x149 - m.x209)**2) + 1 / sqrt((m.x9 - m.x70)**2 + (m.x79 -
    m.x140)**2 + (m.x149 - m.x210)**2) + 1 / sqrt((m.x10 - m.x11)**2 + (m.x80
    - m.x81)**2 + (m.x150 - m.x151)**2) + 1 / sqrt((m.x10 - m.x12)**2 + (m.x80
    - m.x82)**2 + (m.x150 - m.x152)**2) + 1 / sqrt((m.x10 - m.x13)**2 + (m.x80
    - m.x83)**2 + (m.x150 - m.x153)**2) + 1 / sqrt((m.x10 - m.x14)**2 + (m.x80
    - m.x84)**2 + (m.x150 - m.x154)**2) + 1 / sqrt((m.x10 - m.x15)**2 + (m.x80
    - m.x85)**2 + (m.x150 - m.x155)**2) + 1 / sqrt((m.x10 - m.x16)**2 + (m.x80
    - m.x86)**2 + (m.x150 - m.x156)**2) + 1 / sqrt((m.x10 - m.x17)**2 + (m.x80
    - m.x87)**2 + (m.x150 - m.x157)**2) + 1 / sqrt((m.x10 - m.x18)**2 + (m.x80
    - m.x88)**2 + (m.x150 - m.x158)**2) + 1 / sqrt((m.x10 - m.x19)**2 + (m.x80
    - m.x89)**2 + (m.x150 - m.x159)**2) + 1 / sqrt((m.x10 - m.x20)**2 + (m.x80
    - m.x90)**2 + (m.x150 - m.x160)**2) + 1 / sqrt((m.x10 - m.x21)**2 + (m.x80
    - m.x91)**2 + (m.x150 - m.x161)**2) + 1 / sqrt((m.x10 - m.x22)**2 + (m.x80
    - m.x92)**2 + (m.x150 - m.x162)**2) + 1 / sqrt((m.x10 - m.x23)**2 + (m.x80
    - m.x93)**2 + (m.x150 - m.x163)**2) + 1 / sqrt((m.x10 - m.x24)**2 + (m.x80
    - m.x94)**2 + (m.x150 - m.x164)**2) + 1 / sqrt((m.x10 - m.x25)**2 + (m.x80
    - m.x95)**2 + (m.x150 - m.x165)**2) + 1 / sqrt((m.x10 - m.x26)**2 + (m.x80
    - m.x96)**2 + (m.x150 - m.x166)**2) + 1 / sqrt((m.x10 - m.x27)**2 + (m.x80
    - m.x97)**2 + (m.x150 - m.x167)**2) + 1 / sqrt((m.x10 - m.x28)**2 + (m.x80
    - m.x98)**2 + (m.x150 - m.x168)**2) + 1 / sqrt((m.x10 - m.x29)**2 + (m.x80
    - m.x99)**2 + (m.x150 - m.x169)**2) + 1 / sqrt((m.x10 - m.x30)**2 + (m.x80
    - m.x100)**2 + (m.x150 - m.x170)**2) + 1 / sqrt((m.x10 - m.x31)**2 + (
    m.x80 - m.x101)**2 + (m.x150 - m.x171)**2) + 1 / sqrt((m.x10 - m.x32)**2 +
    (m.x80 - m.x102)**2 + (m.x150 - m.x172)**2) + 1 / sqrt((m.x10 - m.x33)**2
    + (m.x80 - m.x103)**2 + (m.x150 - m.x173)**2) + 1 / sqrt((m.x10 - m.x34)**
    2 + (m.x80 - m.x104)**2 + (m.x150 - m.x174)**2) + 1 / sqrt((m.x10 - m.x35)
    **2 + (m.x80 - m.x105)**2 + (m.x150 - m.x175)**2) + 1 / sqrt((m.x10 - m.x36)
    **2 + (m.x80 - m.x106)**2 + (m.x150 - m.x176)**2) + 1 / sqrt((m.x10 - m.x37)
    **2 + (m.x80 - m.x107)**2 + (m.x150 - m.x177)**2) + 1 / sqrt((m.x10 - m.x38)
    **2 + (m.x80 - m.x108)**2 + (m.x150 - m.x178)**2) + 1 / sqrt((m.x10 - m.x39)
    **2 + (m.x80 - m.x109)**2 + (m.x150 - m.x179)**2) + 1 / sqrt((m.x10 - m.x40)
    **2 + (m.x80 - m.x110)**2 + (m.x150 - m.x180)**2) + 1 / sqrt((m.x10 - m.x41)
    **2 + (m.x80 - m.x111)**2 + (m.x150 - m.x181)**2) + 1 / sqrt((m.x10 - m.x42)
    **2 + (m.x80 - m.x112)**2 + (m.x150 - m.x182)**2) + 1 / sqrt((m.x10 - m.x43)
    **2 + (m.x80 - m.x113)**2 + (m.x150 - m.x183)**2) + 1 / sqrt((m.x10 - m.x44)
    **2 + (m.x80 - m.x114)**2 + (m.x150 - m.x184)**2) + 1 / sqrt((m.x10 - m.x45)
    **2 + (m.x80 - m.x115)**2 + (m.x150 - m.x185)**2) + 1 / sqrt((m.x10 - m.x46)
    **2 + (m.x80 - m.x116)**2 + (m.x150 - m.x186)**2) + 1 / sqrt((m.x10 - m.x47)
    **2 + (m.x80 - m.x117)**2 + (m.x150 - m.x187)**2) + 1 / sqrt((m.x10 - m.x48)
    **2 + (m.x80 - m.x118)**2 + (m.x150 - m.x188)**2) + 1 / sqrt((m.x10 - m.x49)
    **2 + (m.x80 - m.x119)**2 + (m.x150 - m.x189)**2) + 1 / sqrt((m.x10 - m.x50)
    **2 + (m.x80 - m.x120)**2 + (m.x150 - m.x190)**2) + 1 / sqrt((m.x10 - m.x51)
    **2 + (m.x80 - m.x121)**2 + (m.x150 - m.x191)**2) + 1 / sqrt((m.x10 - m.x52)
    **2 + (m.x80 - m.x122)**2 + (m.x150 - m.x192)**2) + 1 / sqrt((m.x10 - m.x53)
    **2 + (m.x80 - m.x123)**2 + (m.x150 - m.x193)**2) + 1 / sqrt((m.x10 - m.x54)
    **2 + (m.x80 - m.x124)**2 + (m.x150 - m.x194)**2) + 1 / sqrt((m.x10 - m.x55)
    **2 + (m.x80 - m.x125)**2 + (m.x150 - m.x195)**2) + 1 / sqrt((m.x10 - m.x56)
    **2 + (m.x80 - m.x126)**2 + (m.x150 - m.x196)**2) + 1 / sqrt((m.x10 - m.x57)
    **2 + (m.x80 - m.x127)**2 + (m.x150 - m.x197)**2) + 1 / sqrt((m.x10 - m.x58)
    **2 + (m.x80 - m.x128)**2 + (m.x150 - m.x198)**2) + 1 / sqrt((m.x10 - m.x59)
    **2 + (m.x80 - m.x129)**2 + (m.x150 - m.x199)**2) + 1 / sqrt((m.x10 - m.x60)
    **2 + (m.x80 - m.x130)**2 + (m.x150 - m.x200)**2) + 1 / sqrt((m.x10 - m.x61)
    **2 + (m.x80 - m.x131)**2 + (m.x150 - m.x201)**2) + 1 / sqrt((m.x10 - m.x62)
    **2 + (m.x80 - m.x132)**2 + (m.x150 - m.x202)**2) + 1 / sqrt((m.x10 - m.x63)
    **2 + (m.x80 - m.x133)**2 + (m.x150 - m.x203)**2) + 1 / sqrt((m.x10 - m.x64)
    **2 + (m.x80 - m.x134)**2 + (m.x150 - m.x204)**2) + 1 / sqrt((m.x10 - m.x65)
    **2 + (m.x80 - m.x135)**2 + (m.x150 - m.x205)**2) + 1 / sqrt((m.x10 - m.x66)
    **2 + (m.x80 - m.x136)**2 + (m.x150 - m.x206)**2) + 1 / sqrt((m.x10 - m.x67)
    **2 + (m.x80 - m.x137)**2 + (m.x150 - m.x207)**2) + 1 / sqrt((m.x10 - m.x68)
    **2 + (m.x80 - m.x138)**2 + (m.x150 - m.x208)**2) + 1 / sqrt((m.x10 - m.x69)
    **2 + (m.x80 - m.x139)**2 + (m.x150 - m.x209)**2) + 1 / sqrt((m.x10 - m.x70)
    **2 + (m.x80 - m.x140)**2 + (m.x150 - m.x210)**2) + 1 / sqrt((m.x11 - m.x12)
    **2 + (m.x81 - m.x82)**2 + (m.x151 - m.x152)**2) + 1 / sqrt((m.x11 - m.x13)
    **2 + (m.x81 - m.x83)**2 + (m.x151 - m.x153)**2) + 1 / sqrt((m.x11 - m.x14)
    **2 + (m.x81 - m.x84)**2 + (m.x151 - m.x154)**2) + 1 / sqrt((m.x11 - m.x15)
    **2 + (m.x81 - m.x85)**2 + (m.x151 - m.x155)**2) + 1 / sqrt((m.x11 - m.x16)
    **2 + (m.x81 - m.x86)**2 + (m.x151 - m.x156)**2) + 1 / sqrt((m.x11 - m.x17)
    **2 + (m.x81 - m.x87)**2 + (m.x151 - m.x157)**2) + 1 / sqrt((m.x11 - m.x18)
    **2 + (m.x81 - m.x88)**2 + (m.x151 - m.x158)**2) + 1 / sqrt((m.x11 - m.x19)
    **2 + (m.x81 - m.x89)**2 + (m.x151 - m.x159)**2) + 1 / sqrt((m.x11 - m.x20)
    **2 + (m.x81 - m.x90)**2 + (m.x151 - m.x160)**2) + 1 / sqrt((m.x11 - m.x21)
    **2 + (m.x81 - m.x91)**2 + (m.x151 - m.x161)**2) + 1 / sqrt((m.x11 - m.x22)
    **2 + (m.x81 - m.x92)**2 + (m.x151 - m.x162)**2) + 1 / sqrt((m.x11 - m.x23)
    **2 + (m.x81 - m.x93)**2 + (m.x151 - m.x163)**2) + 1 / sqrt((m.x11 - m.x24)
    **2 + (m.x81 - m.x94)**2 + (m.x151 - m.x164)**2) + 1 / sqrt((m.x11 - m.x25)
    **2 + (m.x81 - m.x95)**2 + (m.x151 - m.x165)**2) + 1 / sqrt((m.x11 - m.x26)
    **2 + (m.x81 - m.x96)**2 + (m.x151 - m.x166)**2) + 1 / sqrt((m.x11 - m.x27)
    **2 + (m.x81 - m.x97)**2 + (m.x151 - m.x167)**2) + 1 / sqrt((m.x11 - m.x28)
    **2 + (m.x81 - m.x98)**2 + (m.x151 - m.x168)**2) + 1 / sqrt((m.x11 - m.x29)
    **2 + (m.x81 - m.x99)**2 + (m.x151 - m.x169)**2) + 1 / sqrt((m.x11 - m.x30)
    **2 + (m.x81 - m.x100)**2 + (m.x151 - m.x170)**2) + 1 / sqrt((m.x11 - m.x31)
    **2 + (m.x81 - m.x101)**2 + (m.x151 - m.x171)**2) + 1 / sqrt((m.x11 - m.x32)
    **2 + (m.x81 - m.x102)**2 + (m.x151 - m.x172)**2) + 1 / sqrt((m.x11 - m.x33)
    **2 + (m.x81 - m.x103)**2 + (m.x151 - m.x173)**2) + 1 / sqrt((m.x11 - m.x34)
    **2 + (m.x81 - m.x104)**2 + (m.x151 - m.x174)**2) + 1 / sqrt((m.x11 - m.x35)
    **2 + (m.x81 - m.x105)**2 + (m.x151 - m.x175)**2) + 1 / sqrt((m.x11 - m.x36)
    **2 + (m.x81 - m.x106)**2 + (m.x151 - m.x176)**2) + 1 / sqrt((m.x11 - m.x37)
    **2 + (m.x81 - m.x107)**2 + (m.x151 - m.x177)**2) + 1 / sqrt((m.x11 - m.x38)
    **2 + (m.x81 - m.x108)**2 + (m.x151 - m.x178)**2) + 1 / sqrt((m.x11 - m.x39)
    **2 + (m.x81 - m.x109)**2 + (m.x151 - m.x179)**2) + 1 / sqrt((m.x11 - m.x40)
    **2 + (m.x81 - m.x110)**2 + (m.x151 - m.x180)**2) + 1 / sqrt((m.x11 - m.x41)
    **2 + (m.x81 - m.x111)**2 + (m.x151 - m.x181)**2) + 1 / sqrt((m.x11 - m.x42)
    **2 + (m.x81 - m.x112)**2 + (m.x151 - m.x182)**2) + 1 / sqrt((m.x11 - m.x43)
    **2 + (m.x81 - m.x113)**2 + (m.x151 - m.x183)**2) + 1 / sqrt((m.x11 - m.x44)
    **2 + (m.x81 - m.x114)**2 + (m.x151 - m.x184)**2) + 1 / sqrt((m.x11 - m.x45)
    **2 + (m.x81 - m.x115)**2 + (m.x151 - m.x185)**2) + 1 / sqrt((m.x11 - m.x46)
    **2 + (m.x81 - m.x116)**2 + (m.x151 - m.x186)**2) + 1 / sqrt((m.x11 - m.x47)
    **2 + (m.x81 - m.x117)**2 + (m.x151 - m.x187)**2) + 1 / sqrt((m.x11 - m.x48)
    **2 + (m.x81 - m.x118)**2 + (m.x151 - m.x188)**2) + 1 / sqrt((m.x11 - m.x49)
    **2 + (m.x81 - m.x119)**2 + (m.x151 - m.x189)**2) + 1 / sqrt((m.x11 - m.x50)
    **2 + (m.x81 - m.x120)**2 + (m.x151 - m.x190)**2) + 1 / sqrt((m.x11 - m.x51)
    **2 + (m.x81 - m.x121)**2 + (m.x151 - m.x191)**2) + 1 / sqrt((m.x11 - m.x52)
    **2 + (m.x81 - m.x122)**2 + (m.x151 - m.x192)**2) + 1 / sqrt((m.x11 - m.x53)
    **2 + (m.x81 - m.x123)**2 + (m.x151 - m.x193)**2) + 1 / sqrt((m.x11 - m.x54)
    **2 + (m.x81 - m.x124)**2 + (m.x151 - m.x194)**2) + 1 / sqrt((m.x11 - m.x55)
    **2 + (m.x81 - m.x125)**2 + (m.x151 - m.x195)**2) + 1 / sqrt((m.x11 - m.x56)
    **2 + (m.x81 - m.x126)**2 + (m.x151 - m.x196)**2) + 1 / sqrt((m.x11 - m.x57)
    **2 + (m.x81 - m.x127)**2 + (m.x151 - m.x197)**2) + 1 / sqrt((m.x11 - m.x58)
    **2 + (m.x81 - m.x128)**2 + (m.x151 - m.x198)**2) + 1 / sqrt((m.x11 - m.x59)
    **2 + (m.x81 - m.x129)**2 + (m.x151 - m.x199)**2) + 1 / sqrt((m.x11 - m.x60)
    **2 + (m.x81 - m.x130)**2 + (m.x151 - m.x200)**2) + 1 / sqrt((m.x11 - m.x61)
    **2 + (m.x81 - m.x131)**2 + (m.x151 - m.x201)**2) + 1 / sqrt((m.x11 - m.x62)
    **2 + (m.x81 - m.x132)**2 + (m.x151 - m.x202)**2) + 1 / sqrt((m.x11 - m.x63)
    **2 + (m.x81 - m.x133)**2 + (m.x151 - m.x203)**2) + 1 / sqrt((m.x11 - m.x64)
    **2 + (m.x81 - m.x134)**2 + (m.x151 - m.x204)**2) + 1 / sqrt((m.x11 - m.x65)
    **2 + (m.x81 - m.x135)**2 + (m.x151 - m.x205)**2) + 1 / sqrt((m.x11 - m.x66)
    **2 + (m.x81 - m.x136)**2 + (m.x151 - m.x206)**2) + 1 / sqrt((m.x11 - m.x67)
    **2 + (m.x81 - m.x137)**2 + (m.x151 - m.x207)**2) + 1 / sqrt((m.x11 - m.x68)
    **2 + (m.x81 - m.x138)**2 + (m.x151 - m.x208)**2) + 1 / sqrt((m.x11 - m.x69)
    **2 + (m.x81 - m.x139)**2 + (m.x151 - m.x209)**2) + 1 / sqrt((m.x11 - m.x70)
    **2 + (m.x81 - m.x140)**2 + (m.x151 - m.x210)**2) + 1 / sqrt((m.x12 - m.x13)
    **2 + (m.x82 - m.x83)**2 + (m.x152 - m.x153)**2) + 1 / sqrt((m.x12 - m.x14)
    **2 + (m.x82 - m.x84)**2 + (m.x152 - m.x154)**2) + 1 / sqrt((m.x12 - m.x15)
    **2 + (m.x82 - m.x85)**2 + (m.x152 - m.x155)**2) + 1 / sqrt((m.x12 - m.x16)
    **2 + (m.x82 - m.x86)**2 + (m.x152 - m.x156)**2) + 1 / sqrt((m.x12 - m.x17)
    **2 + (m.x82 - m.x87)**2 + (m.x152 - m.x157)**2) + 1 / sqrt((m.x12 - m.x18)
    **2 + (m.x82 - m.x88)**2 + (m.x152 - m.x158)**2) + 1 / sqrt((m.x12 - m.x19)
    **2 + (m.x82 - m.x89)**2 + (m.x152 - m.x159)**2) + 1 / sqrt((m.x12 - m.x20)
    **2 + (m.x82 - m.x90)**2 + (m.x152 - m.x160)**2) + 1 / sqrt((m.x12 - m.x21)
    **2 + (m.x82 - m.x91)**2 + (m.x152 - m.x161)**2) + 1 / sqrt((m.x12 - m.x22)
    **2 + (m.x82 - m.x92)**2 + (m.x152 - m.x162)**2) + 1 / sqrt((m.x12 - m.x23)
    **2 + (m.x82 - m.x93)**2 + (m.x152 - m.x163)**2) + 1 / sqrt((m.x12 - m.x24)
    **2 + (m.x82 - m.x94)**2 + (m.x152 - m.x164)**2) + 1 / sqrt((m.x12 - m.x25)
    **2 + (m.x82 - m.x95)**2 + (m.x152 - m.x165)**2) + 1 / sqrt((m.x12 - m.x26)
    **2 + (m.x82 - m.x96)**2 + (m.x152 - m.x166)**2) + 1 / sqrt((m.x12 - m.x27)
    **2 + (m.x82 - m.x97)**2 + (m.x152 - m.x167)**2) + 1 / sqrt((m.x12 - m.x28)
    **2 + (m.x82 - m.x98)**2 + (m.x152 - m.x168)**2) + 1 / sqrt((m.x12 - m.x29)
    **2 + (m.x82 - m.x99)**2 + (m.x152 - m.x169)**2) + 1 / sqrt((m.x12 - m.x30)
    **2 + (m.x82 - m.x100)**2 + (m.x152 - m.x170)**2) + 1 / sqrt((m.x12 - m.x31)
    **2 + (m.x82 - m.x101)**2 + (m.x152 - m.x171)**2) + 1 / sqrt((m.x12 - m.x32)
    **2 + (m.x82 - m.x102)**2 + (m.x152 - m.x172)**2) + 1 / sqrt((m.x12 - m.x33)
    **2 + (m.x82 - m.x103)**2 + (m.x152 - m.x173)**2) + 1 / sqrt((m.x12 - m.x34)
    **2 + (m.x82 - m.x104)**2 + (m.x152 - m.x174)**2) + 1 / sqrt((m.x12 - m.x35)
    **2 + (m.x82 - m.x105)**2 + (m.x152 - m.x175)**2) + 1 / sqrt((m.x12 - m.x36)
    **2 + (m.x82 - m.x106)**2 + (m.x152 - m.x176)**2) + 1 / sqrt((m.x12 - m.x37)
    **2 + (m.x82 - m.x107)**2 + (m.x152 - m.x177)**2) + 1 / sqrt((m.x12 - m.x38)
    **2 + (m.x82 - m.x108)**2 + (m.x152 - m.x178)**2) + 1 / sqrt((m.x12 - m.x39)
    **2 + (m.x82 - m.x109)**2 + (m.x152 - m.x179)**2) + 1 / sqrt((m.x12 - m.x40)
    **2 + (m.x82 - m.x110)**2 + (m.x152 - m.x180)**2) + 1 / sqrt((m.x12 - m.x41)
    **2 + (m.x82 - m.x111)**2 + (m.x152 - m.x181)**2) + 1 / sqrt((m.x12 - m.x42)
    **2 + (m.x82 - m.x112)**2 + (m.x152 - m.x182)**2) + 1 / sqrt((m.x12 - m.x43)
    **2 + (m.x82 - m.x113)**2 + (m.x152 - m.x183)**2) + 1 / sqrt((m.x12 - m.x44)
    **2 + (m.x82 - m.x114)**2 + (m.x152 - m.x184)**2) + 1 / sqrt((m.x12 - m.x45)
    **2 + (m.x82 - m.x115)**2 + (m.x152 - m.x185)**2) + 1 / sqrt((m.x12 - m.x46)
    **2 + (m.x82 - m.x116)**2 + (m.x152 - m.x186)**2) + 1 / sqrt((m.x12 - m.x47)
    **2 + (m.x82 - m.x117)**2 + (m.x152 - m.x187)**2) + 1 / sqrt((m.x12 - m.x48)
    **2 + (m.x82 - m.x118)**2 + (m.x152 - m.x188)**2) + 1 / sqrt((m.x12 - m.x49)
    **2 + (m.x82 - m.x119)**2 + (m.x152 - m.x189)**2) + 1 / sqrt((m.x12 - m.x50)
    **2 + (m.x82 - m.x120)**2 + (m.x152 - m.x190)**2) + 1 / sqrt((m.x12 - m.x51)
    **2 + (m.x82 - m.x121)**2 + (m.x152 - m.x191)**2) + 1 / sqrt((m.x12 - m.x52)
    **2 + (m.x82 - m.x122)**2 + (m.x152 - m.x192)**2) + 1 / sqrt((m.x12 - m.x53)
    **2 + (m.x82 - m.x123)**2 + (m.x152 - m.x193)**2) + 1 / sqrt((m.x12 - m.x54)
    **2 + (m.x82 - m.x124)**2 + (m.x152 - m.x194)**2) + 1 / sqrt((m.x12 - m.x55)
    **2 + (m.x82 - m.x125)**2 + (m.x152 - m.x195)**2) + 1 / sqrt((m.x12 - m.x56)
    **2 + (m.x82 - m.x126)**2 + (m.x152 - m.x196)**2) + 1 / sqrt((m.x12 - m.x57)
    **2 + (m.x82 - m.x127)**2 + (m.x152 - m.x197)**2) + 1 / sqrt((m.x12 - m.x58)
    **2 + (m.x82 - m.x128)**2 + (m.x152 - m.x198)**2) + 1 / sqrt((m.x12 - m.x59)
    **2 + (m.x82 - m.x129)**2 + (m.x152 - m.x199)**2) + 1 / sqrt((m.x12 - m.x60)
    **2 + (m.x82 - m.x130)**2 + (m.x152 - m.x200)**2) + 1 / sqrt((m.x12 - m.x61)
    **2 + (m.x82 - m.x131)**2 + (m.x152 - m.x201)**2) + 1 / sqrt((m.x12 - m.x62)
    **2 + (m.x82 - m.x132)**2 + (m.x152 - m.x202)**2) + 1 / sqrt((m.x12 - m.x63)
    **2 + (m.x82 - m.x133)**2 + (m.x152 - m.x203)**2) + 1 / sqrt((m.x12 - m.x64)
    **2 + (m.x82 - m.x134)**2 + (m.x152 - m.x204)**2) + 1 / sqrt((m.x12 - m.x65)
    **2 + (m.x82 - m.x135)**2 + (m.x152 - m.x205)**2) + 1 / sqrt((m.x12 - m.x66)
    **2 + (m.x82 - m.x136)**2 + (m.x152 - m.x206)**2) + 1 / sqrt((m.x12 - m.x67)
    **2 + (m.x82 - m.x137)**2 + (m.x152 - m.x207)**2) + 1 / sqrt((m.x12 - m.x68)
    **2 + (m.x82 - m.x138)**2 + (m.x152 - m.x208)**2) + 1 / sqrt((m.x12 - m.x69)
    **2 + (m.x82 - m.x139)**2 + (m.x152 - m.x209)**2) + 1 / sqrt((m.x12 - m.x70)
    **2 + (m.x82 - m.x140)**2 + (m.x152 - m.x210)**2) + 1 / sqrt((m.x13 - m.x14)
    **2 + (m.x83 - m.x84)**2 + (m.x153 - m.x154)**2) + 1 / sqrt((m.x13 - m.x15)
    **2 + (m.x83 - m.x85)**2 + (m.x153 - m.x155)**2) + 1 / sqrt((m.x13 - m.x16)
    **2 + (m.x83 - m.x86)**2 + (m.x153 - m.x156)**2) + 1 / sqrt((m.x13 - m.x17)
    **2 + (m.x83 - m.x87)**2 + (m.x153 - m.x157)**2) + 1 / sqrt((m.x13 - m.x18)
    **2 + (m.x83 - m.x88)**2 + (m.x153 - m.x158)**2) + 1 / sqrt((m.x13 - m.x19)
    **2 + (m.x83 - m.x89)**2 + (m.x153 - m.x159)**2) + 1 / sqrt((m.x13 - m.x20)
    **2 + (m.x83 - m.x90)**2 + (m.x153 - m.x160)**2) + 1 / sqrt((m.x13 - m.x21)
    **2 + (m.x83 - m.x91)**2 + (m.x153 - m.x161)**2) + 1 / sqrt((m.x13 - m.x22)
    **2 + (m.x83 - m.x92)**2 + (m.x153 - m.x162)**2) + 1 / sqrt((m.x13 - m.x23)
    **2 + (m.x83 - m.x93)**2 + (m.x153 - m.x163)**2) + 1 / sqrt((m.x13 - m.x24)
    **2 + (m.x83 - m.x94)**2 + (m.x153 - m.x164)**2) + 1 / sqrt((m.x13 - m.x25)
    **2 + (m.x83 - m.x95)**2 + (m.x153 - m.x165)**2) + 1 / sqrt((m.x13 - m.x26)
    **2 + (m.x83 - m.x96)**2 + (m.x153 - m.x166)**2) + 1 / sqrt((m.x13 - m.x27)
    **2 + (m.x83 - m.x97)**2 + (m.x153 - m.x167)**2) + 1 / sqrt((m.x13 - m.x28)
    **2 + (m.x83 - m.x98)**2 + (m.x153 - m.x168)**2) + 1 / sqrt((m.x13 - m.x29)
    **2 + (m.x83 - m.x99)**2 + (m.x153 - m.x169)**2) + 1 / sqrt((m.x13 - m.x30)
    **2 + (m.x83 - m.x100)**2 + (m.x153 - m.x170)**2) + 1 / sqrt((m.x13 - m.x31)
    **2 + (m.x83 - m.x101)**2 + (m.x153 - m.x171)**2) + 1 / sqrt((m.x13 - m.x32)
    **2 + (m.x83 - m.x102)**2 + (m.x153 - m.x172)**2) + 1 / sqrt((m.x13 - m.x33)
    **2 + (m.x83 - m.x103)**2 + (m.x153 - m.x173)**2) + 1 / sqrt((m.x13 - m.x34)
    **2 + (m.x83 - m.x104)**2 + (m.x153 - m.x174)**2) + 1 / sqrt((m.x13 - m.x35)
    **2 + (m.x83 - m.x105)**2 + (m.x153 - m.x175)**2) + 1 / sqrt((m.x13 - m.x36)
    **2 + (m.x83 - m.x106)**2 + (m.x153 - m.x176)**2) + 1 / sqrt((m.x13 - m.x37)
    **2 + (m.x83 - m.x107)**2 + (m.x153 - m.x177)**2) + 1 / sqrt((m.x13 - m.x38)
    **2 + (m.x83 - m.x108)**2 + (m.x153 - m.x178)**2) + 1 / sqrt((m.x13 - m.x39)
    **2 + (m.x83 - m.x109)**2 + (m.x153 - m.x179)**2) + 1 / sqrt((m.x13 - m.x40)
    **2 + (m.x83 - m.x110)**2 + (m.x153 - m.x180)**2) + 1 / sqrt((m.x13 - m.x41)
    **2 + (m.x83 - m.x111)**2 + (m.x153 - m.x181)**2) + 1 / sqrt((m.x13 - m.x42)
    **2 + (m.x83 - m.x112)**2 + (m.x153 - m.x182)**2) + 1 / sqrt((m.x13 - m.x43)
    **2 + (m.x83 - m.x113)**2 + (m.x153 - m.x183)**2) + 1 / sqrt((m.x13 - m.x44)
    **2 + (m.x83 - m.x114)**2 + (m.x153 - m.x184)**2) + 1 / sqrt((m.x13 - m.x45)
    **2 + (m.x83 - m.x115)**2 + (m.x153 - m.x185)**2) + 1 / sqrt((m.x13 - m.x46)
    **2 + (m.x83 - m.x116)**2 + (m.x153 - m.x186)**2) + 1 / sqrt((m.x13 - m.x47)
    **2 + (m.x83 - m.x117)**2 + (m.x153 - m.x187)**2) + 1 / sqrt((m.x13 - m.x48)
    **2 + (m.x83 - m.x118)**2 + (m.x153 - m.x188)**2) + 1 / sqrt((m.x13 - m.x49)
    **2 + (m.x83 - m.x119)**2 + (m.x153 - m.x189)**2) + 1 / sqrt((m.x13 - m.x50)
    **2 + (m.x83 - m.x120)**2 + (m.x153 - m.x190)**2) + 1 / sqrt((m.x13 - m.x51)
    **2 + (m.x83 - m.x121)**2 + (m.x153 - m.x191)**2) + 1 / sqrt((m.x13 - m.x52)
    **2 + (m.x83 - m.x122)**2 + (m.x153 - m.x192)**2) + 1 / sqrt((m.x13 - m.x53)
    **2 + (m.x83 - m.x123)**2 + (m.x153 - m.x193)**2) + 1 / sqrt((m.x13 - m.x54)
    **2 + (m.x83 - m.x124)**2 + (m.x153 - m.x194)**2) + 1 / sqrt((m.x13 - m.x55)
    **2 + (m.x83 - m.x125)**2 + (m.x153 - m.x195)**2) + 1 / sqrt((m.x13 - m.x56)
    **2 + (m.x83 - m.x126)**2 + (m.x153 - m.x196)**2) + 1 / sqrt((m.x13 - m.x57)
    **2 + (m.x83 - m.x127)**2 + (m.x153 - m.x197)**2) + 1 / sqrt((m.x13 - m.x58)
    **2 + (m.x83 - m.x128)**2 + (m.x153 - m.x198)**2) + 1 / sqrt((m.x13 - m.x59)
    **2 + (m.x83 - m.x129)**2 + (m.x153 - m.x199)**2) + 1 / sqrt((m.x13 - m.x60)
    **2 + (m.x83 - m.x130)**2 + (m.x153 - m.x200)**2) + 1 / sqrt((m.x13 - m.x61)
    **2 + (m.x83 - m.x131)**2 + (m.x153 - m.x201)**2) + 1 / sqrt((m.x13 - m.x62)
    **2 + (m.x83 - m.x132)**2 + (m.x153 - m.x202)**2) + 1 / sqrt((m.x13 - m.x63)
    **2 + (m.x83 - m.x133)**2 + (m.x153 - m.x203)**2) + 1 / sqrt((m.x13 - m.x64)
    **2 + (m.x83 - m.x134)**2 + (m.x153 - m.x204)**2) + 1 / sqrt((m.x13 - m.x65)
    **2 + (m.x83 - m.x135)**2 + (m.x153 - m.x205)**2) + 1 / sqrt((m.x13 - m.x66)
    **2 + (m.x83 - m.x136)**2 + (m.x153 - m.x206)**2) + 1 / sqrt((m.x13 - m.x67)
    **2 + (m.x83 - m.x137)**2 + (m.x153 - m.x207)**2) + 1 / sqrt((m.x13 - m.x68)
    **2 + (m.x83 - m.x138)**2 + (m.x153 - m.x208)**2) + 1 / sqrt((m.x13 - m.x69)
    **2 + (m.x83 - m.x139)**2 + (m.x153 - m.x209)**2) + 1 / sqrt((m.x13 - m.x70)
    **2 + (m.x83 - m.x140)**2 + (m.x153 - m.x210)**2) + 1 / sqrt((m.x14 - m.x15)
    **2 + (m.x84 - m.x85)**2 + (m.x154 - m.x155)**2) + 1 / sqrt((m.x14 - m.x16)
    **2 + (m.x84 - m.x86)**2 + (m.x154 - m.x156)**2) + 1 / sqrt((m.x14 - m.x17)
    **2 + (m.x84 - m.x87)**2 + (m.x154 - m.x157)**2) + 1 / sqrt((m.x14 - m.x18)
    **2 + (m.x84 - m.x88)**2 + (m.x154 - m.x158)**2) + 1 / sqrt((m.x14 - m.x19)
    **2 + (m.x84 - m.x89)**2 + (m.x154 - m.x159)**2) + 1 / sqrt((m.x14 - m.x20)
    **2 + (m.x84 - m.x90)**2 + (m.x154 - m.x160)**2) + 1 / sqrt((m.x14 - m.x21)
    **2 + (m.x84 - m.x91)**2 + (m.x154 - m.x161)**2) + 1 / sqrt((m.x14 - m.x22)
    **2 + (m.x84 - m.x92)**2 + (m.x154 - m.x162)**2) + 1 / sqrt((m.x14 - m.x23)
    **2 + (m.x84 - m.x93)**2 + (m.x154 - m.x163)**2) + 1 / sqrt((m.x14 - m.x24)
    **2 + (m.x84 - m.x94)**2 + (m.x154 - m.x164)**2) + 1 / sqrt((m.x14 - m.x25)
    **2 + (m.x84 - m.x95)**2 + (m.x154 - m.x165)**2) + 1 / sqrt((m.x14 - m.x26)
    **2 + (m.x84 - m.x96)**2 + (m.x154 - m.x166)**2) + 1 / sqrt((m.x14 - m.x27)
    **2 + (m.x84 - m.x97)**2 + (m.x154 - m.x167)**2) + 1 / sqrt((m.x14 - m.x28)
    **2 + (m.x84 - m.x98)**2 + (m.x154 - m.x168)**2) + 1 / sqrt((m.x14 - m.x29)
    **2 + (m.x84 - m.x99)**2 + (m.x154 - m.x169)**2) + 1 / sqrt((m.x14 - m.x30)
    **2 + (m.x84 - m.x100)**2 + (m.x154 - m.x170)**2) + 1 / sqrt((m.x14 - m.x31)
    **2 + (m.x84 - m.x101)**2 + (m.x154 - m.x171)**2) + 1 / sqrt((m.x14 - m.x32)
    **2 + (m.x84 - m.x102)**2 + (m.x154 - m.x172)**2) + 1 / sqrt((m.x14 - m.x33)
    **2 + (m.x84 - m.x103)**2 + (m.x154 - m.x173)**2) + 1 / sqrt((m.x14 - m.x34)
    **2 + (m.x84 - m.x104)**2 + (m.x154 - m.x174)**2) + 1 / sqrt((m.x14 - m.x35)
    **2 + (m.x84 - m.x105)**2 + (m.x154 - m.x175)**2) + 1 / sqrt((m.x14 - m.x36)
    **2 + (m.x84 - m.x106)**2 + (m.x154 - m.x176)**2) + 1 / sqrt((m.x14 - m.x37)
    **2 + (m.x84 - m.x107)**2 + (m.x154 - m.x177)**2) + 1 / sqrt((m.x14 - m.x38)
    **2 + (m.x84 - m.x108)**2 + (m.x154 - m.x178)**2) + 1 / sqrt((m.x14 - m.x39)
    **2 + (m.x84 - m.x109)**2 + (m.x154 - m.x179)**2) + 1 / sqrt((m.x14 - m.x40)
    **2 + (m.x84 - m.x110)**2 + (m.x154 - m.x180)**2) + 1 / sqrt((m.x14 - m.x41)
    **2 + (m.x84 - m.x111)**2 + (m.x154 - m.x181)**2) + 1 / sqrt((m.x14 - m.x42)
    **2 + (m.x84 - m.x112)**2 + (m.x154 - m.x182)**2) + 1 / sqrt((m.x14 - m.x43)
    **2 + (m.x84 - m.x113)**2 + (m.x154 - m.x183)**2) + 1 / sqrt((m.x14 - m.x44)
    **2 + (m.x84 - m.x114)**2 + (m.x154 - m.x184)**2) + 1 / sqrt((m.x14 - m.x45)
    **2 + (m.x84 - m.x115)**2 + (m.x154 - m.x185)**2) + 1 / sqrt((m.x14 - m.x46)
    **2 + (m.x84 - m.x116)**2 + (m.x154 - m.x186)**2) + 1 / sqrt((m.x14 - m.x47)
    **2 + (m.x84 - m.x117)**2 + (m.x154 - m.x187)**2) + 1 / sqrt((m.x14 - m.x48)
    **2 + (m.x84 - m.x118)**2 + (m.x154 - m.x188)**2) + 1 / sqrt((m.x14 - m.x49)
    **2 + (m.x84 - m.x119)**2 + (m.x154 - m.x189)**2) + 1 / sqrt((m.x14 - m.x50)
    **2 + (m.x84 - m.x120)**2 + (m.x154 - m.x190)**2) + 1 / sqrt((m.x14 - m.x51)
    **2 + (m.x84 - m.x121)**2 + (m.x154 - m.x191)**2) + 1 / sqrt((m.x14 - m.x52)
    **2 + (m.x84 - m.x122)**2 + (m.x154 - m.x192)**2) + 1 / sqrt((m.x14 - m.x53)
    **2 + (m.x84 - m.x123)**2 + (m.x154 - m.x193)**2) + 1 / sqrt((m.x14 - m.x54)
    **2 + (m.x84 - m.x124)**2 + (m.x154 - m.x194)**2) + 1 / sqrt((m.x14 - m.x55)
    **2 + (m.x84 - m.x125)**2 + (m.x154 - m.x195)**2) + 1 / sqrt((m.x14 - m.x56)
    **2 + (m.x84 - m.x126)**2 + (m.x154 - m.x196)**2) + 1 / sqrt((m.x14 - m.x57)
    **2 + (m.x84 - m.x127)**2 + (m.x154 - m.x197)**2) + 1 / sqrt((m.x14 - m.x58)
    **2 + (m.x84 - m.x128)**2 + (m.x154 - m.x198)**2) + 1 / sqrt((m.x14 - m.x59)
    **2 + (m.x84 - m.x129)**2 + (m.x154 - m.x199)**2) + 1 / sqrt((m.x14 - m.x60)
    **2 + (m.x84 - m.x130)**2 + (m.x154 - m.x200)**2) + 1 / sqrt((m.x14 - m.x61)
    **2 + (m.x84 - m.x131)**2 + (m.x154 - m.x201)**2) + 1 / sqrt((m.x14 - m.x62)
    **2 + (m.x84 - m.x132)**2 + (m.x154 - m.x202)**2) + 1 / sqrt((m.x14 - m.x63)
    **2 + (m.x84 - m.x133)**2 + (m.x154 - m.x203)**2) + 1 / sqrt((m.x14 - m.x64)
    **2 + (m.x84 - m.x134)**2 + (m.x154 - m.x204)**2) + 1 / sqrt((m.x14 - m.x65)
    **2 + (m.x84 - m.x135)**2 + (m.x154 - m.x205)**2) + 1 / sqrt((m.x14 - m.x66)
    **2 + (m.x84 - m.x136)**2 + (m.x154 - m.x206)**2) + 1 / sqrt((m.x14 - m.x67)
    **2 + (m.x84 - m.x137)**2 + (m.x154 - m.x207)**2) + 1 / sqrt((m.x14 - m.x68)
    **2 + (m.x84 - m.x138)**2 + (m.x154 - m.x208)**2) + 1 / sqrt((m.x14 - m.x69)
    **2 + (m.x84 - m.x139)**2 + (m.x154 - m.x209)**2) + 1 / sqrt((m.x14 - m.x70)
    **2 + (m.x84 - m.x140)**2 + (m.x154 - m.x210)**2) + 1 / sqrt((m.x15 - m.x16)
    **2 + (m.x85 - m.x86)**2 + (m.x155 - m.x156)**2) + 1 / sqrt((m.x15 - m.x17)
    **2 + (m.x85 - m.x87)**2 + (m.x155 - m.x157)**2) + 1 / sqrt((m.x15 - m.x18)
    **2 + (m.x85 - m.x88)**2 + (m.x155 - m.x158)**2) + 1 / sqrt((m.x15 - m.x19)
    **2 + (m.x85 - m.x89)**2 + (m.x155 - m.x159)**2) + 1 / sqrt((m.x15 - m.x20)
    **2 + (m.x85 - m.x90)**2 + (m.x155 - m.x160)**2) + 1 / sqrt((m.x15 - m.x21)
    **2 + (m.x85 - m.x91)**2 + (m.x155 - m.x161)**2) + 1 / sqrt((m.x15 - m.x22)
    **2 + (m.x85 - m.x92)**2 + (m.x155 - m.x162)**2) + 1 / sqrt((m.x15 - m.x23)
    **2 + (m.x85 - m.x93)**2 + (m.x155 - m.x163)**2) + 1 / sqrt((m.x15 - m.x24)
    **2 + (m.x85 - m.x94)**2 + (m.x155 - m.x164)**2) + 1 / sqrt((m.x15 - m.x25)
    **2 + (m.x85 - m.x95)**2 + (m.x155 - m.x165)**2) + 1 / sqrt((m.x15 - m.x26)
    **2 + (m.x85 - m.x96)**2 + (m.x155 - m.x166)**2) + 1 / sqrt((m.x15 - m.x27)
    **2 + (m.x85 - m.x97)**2 + (m.x155 - m.x167)**2) + 1 / sqrt((m.x15 - m.x28)
    **2 + (m.x85 - m.x98)**2 + (m.x155 - m.x168)**2) + 1 / sqrt((m.x15 - m.x29)
    **2 + (m.x85 - m.x99)**2 + (m.x155 - m.x169)**2) + 1 / sqrt((m.x15 - m.x30)
    **2 + (m.x85 - m.x100)**2 + (m.x155 - m.x170)**2) + 1 / sqrt((m.x15 - m.x31)
    **2 + (m.x85 - m.x101)**2 + (m.x155 - m.x171)**2) + 1 / sqrt((m.x15 - m.x32)
    **2 + (m.x85 - m.x102)**2 + (m.x155 - m.x172)**2) + 1 / sqrt((m.x15 - m.x33)
    **2 + (m.x85 - m.x103)**2 + (m.x155 - m.x173)**2) + 1 / sqrt((m.x15 - m.x34)
    **2 + (m.x85 - m.x104)**2 + (m.x155 - m.x174)**2) + 1 / sqrt((m.x15 - m.x35)
    **2 + (m.x85 - m.x105)**2 + (m.x155 - m.x175)**2) + 1 / sqrt((m.x15 - m.x36)
    **2 + (m.x85 - m.x106)**2 + (m.x155 - m.x176)**2) + 1 / sqrt((m.x15 - m.x37)
    **2 + (m.x85 - m.x107)**2 + (m.x155 - m.x177)**2) + 1 / sqrt((m.x15 - m.x38)
    **2 + (m.x85 - m.x108)**2 + (m.x155 - m.x178)**2) + 1 / sqrt((m.x15 - m.x39)
    **2 + (m.x85 - m.x109)**2 + (m.x155 - m.x179)**2) + 1 / sqrt((m.x15 - m.x40)
    **2 + (m.x85 - m.x110)**2 + (m.x155 - m.x180)**2) + 1 / sqrt((m.x15 - m.x41)
    **2 + (m.x85 - m.x111)**2 + (m.x155 - m.x181)**2) + 1 / sqrt((m.x15 - m.x42)
    **2 + (m.x85 - m.x112)**2 + (m.x155 - m.x182)**2) + 1 / sqrt((m.x15 - m.x43)
    **2 + (m.x85 - m.x113)**2 + (m.x155 - m.x183)**2) + 1 / sqrt((m.x15 - m.x44)
    **2 + (m.x85 - m.x114)**2 + (m.x155 - m.x184)**2) + 1 / sqrt((m.x15 - m.x45)
    **2 + (m.x85 - m.x115)**2 + (m.x155 - m.x185)**2) + 1 / sqrt((m.x15 - m.x46)
    **2 + (m.x85 - m.x116)**2 + (m.x155 - m.x186)**2) + 1 / sqrt((m.x15 - m.x47)
    **2 + (m.x85 - m.x117)**2 + (m.x155 - m.x187)**2) + 1 / sqrt((m.x15 - m.x48)
    **2 + (m.x85 - m.x118)**2 + (m.x155 - m.x188)**2) + 1 / sqrt((m.x15 - m.x49)
    **2 + (m.x85 - m.x119)**2 + (m.x155 - m.x189)**2) + 1 / sqrt((m.x15 - m.x50)
    **2 + (m.x85 - m.x120)**2 + (m.x155 - m.x190)**2) + 1 / sqrt((m.x15 - m.x51)
    **2 + (m.x85 - m.x121)**2 + (m.x155 - m.x191)**2) + 1 / sqrt((m.x15 - m.x52)
    **2 + (m.x85 - m.x122)**2 + (m.x155 - m.x192)**2) + 1 / sqrt((m.x15 - m.x53)
    **2 + (m.x85 - m.x123)**2 + (m.x155 - m.x193)**2) + 1 / sqrt((m.x15 - m.x54)
    **2 + (m.x85 - m.x124)**2 + (m.x155 - m.x194)**2) + 1 / sqrt((m.x15 - m.x55)
    **2 + (m.x85 - m.x125)**2 + (m.x155 - m.x195)**2) + 1 / sqrt((m.x15 - m.x56)
    **2 + (m.x85 - m.x126)**2 + (m.x155 - m.x196)**2) + 1 / sqrt((m.x15 - m.x57)
    **2 + (m.x85 - m.x127)**2 + (m.x155 - m.x197)**2) + 1 / sqrt((m.x15 - m.x58)
    **2 + (m.x85 - m.x128)**2 + (m.x155 - m.x198)**2) + 1 / sqrt((m.x15 - m.x59)
    **2 + (m.x85 - m.x129)**2 + (m.x155 - m.x199)**2) + 1 / sqrt((m.x15 - m.x60)
    **2 + (m.x85 - m.x130)**2 + (m.x155 - m.x200)**2) + 1 / sqrt((m.x15 - m.x61)
    **2 + (m.x85 - m.x131)**2 + (m.x155 - m.x201)**2) + 1 / sqrt((m.x15 - m.x62)
    **2 + (m.x85 - m.x132)**2 + (m.x155 - m.x202)**2) + 1 / sqrt((m.x15 - m.x63)
    **2 + (m.x85 - m.x133)**2 + (m.x155 - m.x203)**2) + 1 / sqrt((m.x15 - m.x64)
    **2 + (m.x85 - m.x134)**2 + (m.x155 - m.x204)**2) + 1 / sqrt((m.x15 - m.x65)
    **2 + (m.x85 - m.x135)**2 + (m.x155 - m.x205)**2) + 1 / sqrt((m.x15 - m.x66)
    **2 + (m.x85 - m.x136)**2 + (m.x155 - m.x206)**2) + 1 / sqrt((m.x15 - m.x67)
    **2 + (m.x85 - m.x137)**2 + (m.x155 - m.x207)**2) + 1 / sqrt((m.x15 - m.x68)
    **2 + (m.x85 - m.x138)**2 + (m.x155 - m.x208)**2) + 1 / sqrt((m.x15 - m.x69)
    **2 + (m.x85 - m.x139)**2 + (m.x155 - m.x209)**2) + 1 / sqrt((m.x15 - m.x70)
    **2 + (m.x85 - m.x140)**2 + (m.x155 - m.x210)**2) + 1 / sqrt((m.x16 - m.x17)
    **2 + (m.x86 - m.x87)**2 + (m.x156 - m.x157)**2) + 1 / sqrt((m.x16 - m.x18)
    **2 + (m.x86 - m.x88)**2 + (m.x156 - m.x158)**2) + 1 / sqrt((m.x16 - m.x19)
    **2 + (m.x86 - m.x89)**2 + (m.x156 - m.x159)**2) + 1 / sqrt((m.x16 - m.x20)
    **2 + (m.x86 - m.x90)**2 + (m.x156 - m.x160)**2) + 1 / sqrt((m.x16 - m.x21)
    **2 + (m.x86 - m.x91)**2 + (m.x156 - m.x161)**2) + 1 / sqrt((m.x16 - m.x22)
    **2 + (m.x86 - m.x92)**2 + (m.x156 - m.x162)**2) + 1 / sqrt((m.x16 - m.x23)
    **2 + (m.x86 - m.x93)**2 + (m.x156 - m.x163)**2) + 1 / sqrt((m.x16 - m.x24)
    **2 + (m.x86 - m.x94)**2 + (m.x156 - m.x164)**2) + 1 / sqrt((m.x16 - m.x25)
    **2 + (m.x86 - m.x95)**2 + (m.x156 - m.x165)**2) + 1 / sqrt((m.x16 - m.x26)
    **2 + (m.x86 - m.x96)**2 + (m.x156 - m.x166)**2) + 1 / sqrt((m.x16 - m.x27)
    **2 + (m.x86 - m.x97)**2 + (m.x156 - m.x167)**2) + 1 / sqrt((m.x16 - m.x28)
    **2 + (m.x86 - m.x98)**2 + (m.x156 - m.x168)**2) + 1 / sqrt((m.x16 - m.x29)
    **2 + (m.x86 - m.x99)**2 + (m.x156 - m.x169)**2) + 1 / sqrt((m.x16 - m.x30)
    **2 + (m.x86 - m.x100)**2 + (m.x156 - m.x170)**2) + 1 / sqrt((m.x16 - m.x31)
    **2 + (m.x86 - m.x101)**2 + (m.x156 - m.x171)**2) + 1 / sqrt((m.x16 - m.x32)
    **2 + (m.x86 - m.x102)**2 + (m.x156 - m.x172)**2) + 1 / sqrt((m.x16 - m.x33)
    **2 + (m.x86 - m.x103)**2 + (m.x156 - m.x173)**2) + 1 / sqrt((m.x16 - m.x34)
    **2 + (m.x86 - m.x104)**2 + (m.x156 - m.x174)**2) + 1 / sqrt((m.x16 - m.x35)
    **2 + (m.x86 - m.x105)**2 + (m.x156 - m.x175)**2) + 1 / sqrt((m.x16 - m.x36)
    **2 + (m.x86 - m.x106)**2 + (m.x156 - m.x176)**2) + 1 / sqrt((m.x16 - m.x37)
    **2 + (m.x86 - m.x107)**2 + (m.x156 - m.x177)**2) + 1 / sqrt((m.x16 - m.x38)
    **2 + (m.x86 - m.x108)**2 + (m.x156 - m.x178)**2) + 1 / sqrt((m.x16 - m.x39)
    **2 + (m.x86 - m.x109)**2 + (m.x156 - m.x179)**2) + 1 / sqrt((m.x16 - m.x40)
    **2 + (m.x86 - m.x110)**2 + (m.x156 - m.x180)**2) + 1 / sqrt((m.x16 - m.x41)
    **2 + (m.x86 - m.x111)**2 + (m.x156 - m.x181)**2) + 1 / sqrt((m.x16 - m.x42)
    **2 + (m.x86 - m.x112)**2 + (m.x156 - m.x182)**2) + 1 / sqrt((m.x16 - m.x43)
    **2 + (m.x86 - m.x113)**2 + (m.x156 - m.x183)**2) + 1 / sqrt((m.x16 - m.x44)
    **2 + (m.x86 - m.x114)**2 + (m.x156 - m.x184)**2) + 1 / sqrt((m.x16 - m.x45)
    **2 + (m.x86 - m.x115)**2 + (m.x156 - m.x185)**2) + 1 / sqrt((m.x16 - m.x46)
    **2 + (m.x86 - m.x116)**2 + (m.x156 - m.x186)**2) + 1 / sqrt((m.x16 - m.x47)
    **2 + (m.x86 - m.x117)**2 + (m.x156 - m.x187)**2) + 1 / sqrt((m.x16 - m.x48)
    **2 + (m.x86 - m.x118)**2 + (m.x156 - m.x188)**2) + 1 / sqrt((m.x16 - m.x49)
    **2 + (m.x86 - m.x119)**2 + (m.x156 - m.x189)**2) + 1 / sqrt((m.x16 - m.x50)
    **2 + (m.x86 - m.x120)**2 + (m.x156 - m.x190)**2) + 1 / sqrt((m.x16 - m.x51)
    **2 + (m.x86 - m.x121)**2 + (m.x156 - m.x191)**2) + 1 / sqrt((m.x16 - m.x52)
    **2 + (m.x86 - m.x122)**2 + (m.x156 - m.x192)**2) + 1 / sqrt((m.x16 - m.x53)
    **2 + (m.x86 - m.x123)**2 + (m.x156 - m.x193)**2) + 1 / sqrt((m.x16 - m.x54)
    **2 + (m.x86 - m.x124)**2 + (m.x156 - m.x194)**2) + 1 / sqrt((m.x16 - m.x55)
    **2 + (m.x86 - m.x125)**2 + (m.x156 - m.x195)**2) + 1 / sqrt((m.x16 - m.x56)
    **2 + (m.x86 - m.x126)**2 + (m.x156 - m.x196)**2) + 1 / sqrt((m.x16 - m.x57)
    **2 + (m.x86 - m.x127)**2 + (m.x156 - m.x197)**2) + 1 / sqrt((m.x16 - m.x58)
    **2 + (m.x86 - m.x128)**2 + (m.x156 - m.x198)**2) + 1 / sqrt((m.x16 - m.x59)
    **2 + (m.x86 - m.x129)**2 + (m.x156 - m.x199)**2) + 1 / sqrt((m.x16 - m.x60)
    **2 + (m.x86 - m.x130)**2 + (m.x156 - m.x200)**2) + 1 / sqrt((m.x16 - m.x61)
    **2 + (m.x86 - m.x131)**2 + (m.x156 - m.x201)**2) + 1 / sqrt((m.x16 - m.x62)
    **2 + (m.x86 - m.x132)**2 + (m.x156 - m.x202)**2) + 1 / sqrt((m.x16 - m.x63)
    **2 + (m.x86 - m.x133)**2 + (m.x156 - m.x203)**2) + 1 / sqrt((m.x16 - m.x64)
    **2 + (m.x86 - m.x134)**2 + (m.x156 - m.x204)**2) + 1 / sqrt((m.x16 - m.x65)
    **2 + (m.x86 - m.x135)**2 + (m.x156 - m.x205)**2) + 1 / sqrt((m.x16 - m.x66)
    **2 + (m.x86 - m.x136)**2 + (m.x156 - m.x206)**2) + 1 / sqrt((m.x16 - m.x67)
    **2 + (m.x86 - m.x137)**2 + (m.x156 - m.x207)**2) + 1 / sqrt((m.x16 - m.x68)
    **2 + (m.x86 - m.x138)**2 + (m.x156 - m.x208)**2) + 1 / sqrt((m.x16 - m.x69)
    **2 + (m.x86 - m.x139)**2 + (m.x156 - m.x209)**2) + 1 / sqrt((m.x16 - m.x70)
    **2 + (m.x86 - m.x140)**2 + (m.x156 - m.x210)**2) + 1 / sqrt((m.x17 - m.x18)
    **2 + (m.x87 - m.x88)**2 + (m.x157 - m.x158)**2) + 1 / sqrt((m.x17 - m.x19)
    **2 + (m.x87 - m.x89)**2 + (m.x157 - m.x159)**2) + 1 / sqrt((m.x17 - m.x20)
    **2 + (m.x87 - m.x90)**2 + (m.x157 - m.x160)**2) + 1 / sqrt((m.x17 - m.x21)
    **2 + (m.x87 - m.x91)**2 + (m.x157 - m.x161)**2) + 1 / sqrt((m.x17 - m.x22)
    **2 + (m.x87 - m.x92)**2 + (m.x157 - m.x162)**2) + 1 / sqrt((m.x17 - m.x23)
    **2 + (m.x87 - m.x93)**2 + (m.x157 - m.x163)**2) + 1 / sqrt((m.x17 - m.x24)
    **2 + (m.x87 - m.x94)**2 + (m.x157 - m.x164)**2) + 1 / sqrt((m.x17 - m.x25)
    **2 + (m.x87 - m.x95)**2 + (m.x157 - m.x165)**2) + 1 / sqrt((m.x17 - m.x26)
    **2 + (m.x87 - m.x96)**2 + (m.x157 - m.x166)**2) + 1 / sqrt((m.x17 - m.x27)
    **2 + (m.x87 - m.x97)**2 + (m.x157 - m.x167)**2) + 1 / sqrt((m.x17 - m.x28)
    **2 + (m.x87 - m.x98)**2 + (m.x157 - m.x168)**2) + 1 / sqrt((m.x17 - m.x29)
    **2 + (m.x87 - m.x99)**2 + (m.x157 - m.x169)**2) + 1 / sqrt((m.x17 - m.x30)
    **2 + (m.x87 - m.x100)**2 + (m.x157 - m.x170)**2) + 1 / sqrt((m.x17 - m.x31)
    **2 + (m.x87 - m.x101)**2 + (m.x157 - m.x171)**2) + 1 / sqrt((m.x17 - m.x32)
    **2 + (m.x87 - m.x102)**2 + (m.x157 - m.x172)**2) + 1 / sqrt((m.x17 - m.x33)
    **2 + (m.x87 - m.x103)**2 + (m.x157 - m.x173)**2) + 1 / sqrt((m.x17 - m.x34)
    **2 + (m.x87 - m.x104)**2 + (m.x157 - m.x174)**2) + 1 / sqrt((m.x17 - m.x35)
    **2 + (m.x87 - m.x105)**2 + (m.x157 - m.x175)**2) + 1 / sqrt((m.x17 - m.x36)
    **2 + (m.x87 - m.x106)**2 + (m.x157 - m.x176)**2) + 1 / sqrt((m.x17 - m.x37)
    **2 + (m.x87 - m.x107)**2 + (m.x157 - m.x177)**2) + 1 / sqrt((m.x17 - m.x38)
    **2 + (m.x87 - m.x108)**2 + (m.x157 - m.x178)**2) + 1 / sqrt((m.x17 - m.x39)
    **2 + (m.x87 - m.x109)**2 + (m.x157 - m.x179)**2) + 1 / sqrt((m.x17 - m.x40)
    **2 + (m.x87 - m.x110)**2 + (m.x157 - m.x180)**2) + 1 / sqrt((m.x17 - m.x41)
    **2 + (m.x87 - m.x111)**2 + (m.x157 - m.x181)**2) + 1 / sqrt((m.x17 - m.x42)
    **2 + (m.x87 - m.x112)**2 + (m.x157 - m.x182)**2) + 1 / sqrt((m.x17 - m.x43)
    **2 + (m.x87 - m.x113)**2 + (m.x157 - m.x183)**2) + 1 / sqrt((m.x17 - m.x44)
    **2 + (m.x87 - m.x114)**2 + (m.x157 - m.x184)**2) + 1 / sqrt((m.x17 - m.x45)
    **2 + (m.x87 - m.x115)**2 + (m.x157 - m.x185)**2) + 1 / sqrt((m.x17 - m.x46)
    **2 + (m.x87 - m.x116)**2 + (m.x157 - m.x186)**2) + 1 / sqrt((m.x17 - m.x47)
    **2 + (m.x87 - m.x117)**2 + (m.x157 - m.x187)**2) + 1 / sqrt((m.x17 - m.x48)
    **2 + (m.x87 - m.x118)**2 + (m.x157 - m.x188)**2) + 1 / sqrt((m.x17 - m.x49)
    **2 + (m.x87 - m.x119)**2 + (m.x157 - m.x189)**2) + 1 / sqrt((m.x17 - m.x50)
    **2 + (m.x87 - m.x120)**2 + (m.x157 - m.x190)**2) + 1 / sqrt((m.x17 - m.x51)
    **2 + (m.x87 - m.x121)**2 + (m.x157 - m.x191)**2) + 1 / sqrt((m.x17 - m.x52)
    **2 + (m.x87 - m.x122)**2 + (m.x157 - m.x192)**2) + 1 / sqrt((m.x17 - m.x53)
    **2 + (m.x87 - m.x123)**2 + (m.x157 - m.x193)**2) + 1 / sqrt((m.x17 - m.x54)
    **2 + (m.x87 - m.x124)**2 + (m.x157 - m.x194)**2) + 1 / sqrt((m.x17 - m.x55)
    **2 + (m.x87 - m.x125)**2 + (m.x157 - m.x195)**2) + 1 / sqrt((m.x17 - m.x56)
    **2 + (m.x87 - m.x126)**2 + (m.x157 - m.x196)**2) + 1 / sqrt((m.x17 - m.x57)
    **2 + (m.x87 - m.x127)**2 + (m.x157 - m.x197)**2) + 1 / sqrt((m.x17 - m.x58)
    **2 + (m.x87 - m.x128)**2 + (m.x157 - m.x198)**2) + 1 / sqrt((m.x17 - m.x59)
    **2 + (m.x87 - m.x129)**2 + (m.x157 - m.x199)**2) + 1 / sqrt((m.x17 - m.x60)
    **2 + (m.x87 - m.x130)**2 + (m.x157 - m.x200)**2) + 1 / sqrt((m.x17 - m.x61)
    **2 + (m.x87 - m.x131)**2 + (m.x157 - m.x201)**2) + 1 / sqrt((m.x17 - m.x62)
    **2 + (m.x87 - m.x132)**2 + (m.x157 - m.x202)**2) + 1 / sqrt((m.x17 - m.x63)
    **2 + (m.x87 - m.x133)**2 + (m.x157 - m.x203)**2) + 1 / sqrt((m.x17 - m.x64)
    **2 + (m.x87 - m.x134)**2 + (m.x157 - m.x204)**2) + 1 / sqrt((m.x17 - m.x65)
    **2 + (m.x87 - m.x135)**2 + (m.x157 - m.x205)**2) + 1 / sqrt((m.x17 - m.x66)
    **2 + (m.x87 - m.x136)**2 + (m.x157 - m.x206)**2) + 1 / sqrt((m.x17 - m.x67)
    **2 + (m.x87 - m.x137)**2 + (m.x157 - m.x207)**2) + 1 / sqrt((m.x17 - m.x68)
    **2 + (m.x87 - m.x138)**2 + (m.x157 - m.x208)**2) + 1 / sqrt((m.x17 - m.x69)
    **2 + (m.x87 - m.x139)**2 + (m.x157 - m.x209)**2) + 1 / sqrt((m.x17 - m.x70)
    **2 + (m.x87 - m.x140)**2 + (m.x157 - m.x210)**2) + 1 / sqrt((m.x18 - m.x19)
    **2 + (m.x88 - m.x89)**2 + (m.x158 - m.x159)**2) + 1 / sqrt((m.x18 - m.x20)
    **2 + (m.x88 - m.x90)**2 + (m.x158 - m.x160)**2) + 1 / sqrt((m.x18 - m.x21)
    **2 + (m.x88 - m.x91)**2 + (m.x158 - m.x161)**2) + 1 / sqrt((m.x18 - m.x22)
    **2 + (m.x88 - m.x92)**2 + (m.x158 - m.x162)**2) + 1 / sqrt((m.x18 - m.x23)
    **2 + (m.x88 - m.x93)**2 + (m.x158 - m.x163)**2) + 1 / sqrt((m.x18 - m.x24)
    **2 + (m.x88 - m.x94)**2 + (m.x158 - m.x164)**2) + 1 / sqrt((m.x18 - m.x25)
    **2 + (m.x88 - m.x95)**2 + (m.x158 - m.x165)**2) + 1 / sqrt((m.x18 - m.x26)
    **2 + (m.x88 - m.x96)**2 + (m.x158 - m.x166)**2) + 1 / sqrt((m.x18 - m.x27)
    **2 + (m.x88 - m.x97)**2 + (m.x158 - m.x167)**2) + 1 / sqrt((m.x18 - m.x28)
    **2 + (m.x88 - m.x98)**2 + (m.x158 - m.x168)**2) + 1 / sqrt((m.x18 - m.x29)
    **2 + (m.x88 - m.x99)**2 + (m.x158 - m.x169)**2) + 1 / sqrt((m.x18 - m.x30)
    **2 + (m.x88 - m.x100)**2 + (m.x158 - m.x170)**2) + 1 / sqrt((m.x18 - m.x31)
    **2 + (m.x88 - m.x101)**2 + (m.x158 - m.x171)**2) + 1 / sqrt((m.x18 - m.x32)
    **2 + (m.x88 - m.x102)**2 + (m.x158 - m.x172)**2) + 1 / sqrt((m.x18 - m.x33)
    **2 + (m.x88 - m.x103)**2 + (m.x158 - m.x173)**2) + 1 / sqrt((m.x18 - m.x34)
    **2 + (m.x88 - m.x104)**2 + (m.x158 - m.x174)**2) + 1 / sqrt((m.x18 - m.x35)
    **2 + (m.x88 - m.x105)**2 + (m.x158 - m.x175)**2) + 1 / sqrt((m.x18 - m.x36)
    **2 + (m.x88 - m.x106)**2 + (m.x158 - m.x176)**2) + 1 / sqrt((m.x18 - m.x37)
    **2 + (m.x88 - m.x107)**2 + (m.x158 - m.x177)**2) + 1 / sqrt((m.x18 - m.x38)
    **2 + (m.x88 - m.x108)**2 + (m.x158 - m.x178)**2) + 1 / sqrt((m.x18 - m.x39)
    **2 + (m.x88 - m.x109)**2 + (m.x158 - m.x179)**2) + 1 / sqrt((m.x18 - m.x40)
    **2 + (m.x88 - m.x110)**2 + (m.x158 - m.x180)**2) + 1 / sqrt((m.x18 - m.x41)
    **2 + (m.x88 - m.x111)**2 + (m.x158 - m.x181)**2) + 1 / sqrt((m.x18 - m.x42)
    **2 + (m.x88 - m.x112)**2 + (m.x158 - m.x182)**2) + 1 / sqrt((m.x18 - m.x43)
    **2 + (m.x88 - m.x113)**2 + (m.x158 - m.x183)**2) + 1 / sqrt((m.x18 - m.x44)
    **2 + (m.x88 - m.x114)**2 + (m.x158 - m.x184)**2) + 1 / sqrt((m.x18 - m.x45)
    **2 + (m.x88 - m.x115)**2 + (m.x158 - m.x185)**2) + 1 / sqrt((m.x18 - m.x46)
    **2 + (m.x88 - m.x116)**2 + (m.x158 - m.x186)**2) + 1 / sqrt((m.x18 - m.x47)
    **2 + (m.x88 - m.x117)**2 + (m.x158 - m.x187)**2) + 1 / sqrt((m.x18 - m.x48)
    **2 + (m.x88 - m.x118)**2 + (m.x158 - m.x188)**2) + 1 / sqrt((m.x18 - m.x49)
    **2 + (m.x88 - m.x119)**2 + (m.x158 - m.x189)**2) + 1 / sqrt((m.x18 - m.x50)
    **2 + (m.x88 - m.x120)**2 + (m.x158 - m.x190)**2) + 1 / sqrt((m.x18 - m.x51)
    **2 + (m.x88 - m.x121)**2 + (m.x158 - m.x191)**2) + 1 / sqrt((m.x18 - m.x52)
    **2 + (m.x88 - m.x122)**2 + (m.x158 - m.x192)**2) + 1 / sqrt((m.x18 - m.x53)
    **2 + (m.x88 - m.x123)**2 + (m.x158 - m.x193)**2) + 1 / sqrt((m.x18 - m.x54)
    **2 + (m.x88 - m.x124)**2 + (m.x158 - m.x194)**2) + 1 / sqrt((m.x18 - m.x55)
    **2 + (m.x88 - m.x125)**2 + (m.x158 - m.x195)**2) + 1 / sqrt((m.x18 - m.x56)
    **2 + (m.x88 - m.x126)**2 + (m.x158 - m.x196)**2) + 1 / sqrt((m.x18 - m.x57)
    **2 + (m.x88 - m.x127)**2 + (m.x158 - m.x197)**2) + 1 / sqrt((m.x18 - m.x58)
    **2 + (m.x88 - m.x128)**2 + (m.x158 - m.x198)**2) + 1 / sqrt((m.x18 - m.x59)
    **2 + (m.x88 - m.x129)**2 + (m.x158 - m.x199)**2) + 1 / sqrt((m.x18 - m.x60)
    **2 + (m.x88 - m.x130)**2 + (m.x158 - m.x200)**2) + 1 / sqrt((m.x18 - m.x61)
    **2 + (m.x88 - m.x131)**2 + (m.x158 - m.x201)**2) + 1 / sqrt((m.x18 - m.x62)
    **2 + (m.x88 - m.x132)**2 + (m.x158 - m.x202)**2) + 1 / sqrt((m.x18 - m.x63)
    **2 + (m.x88 - m.x133)**2 + (m.x158 - m.x203)**2) + 1 / sqrt((m.x18 - m.x64)
    **2 + (m.x88 - m.x134)**2 + (m.x158 - m.x204)**2) + 1 / sqrt((m.x18 - m.x65)
    **2 + (m.x88 - m.x135)**2 + (m.x158 - m.x205)**2) + 1 / sqrt((m.x18 - m.x66)
    **2 + (m.x88 - m.x136)**2 + (m.x158 - m.x206)**2) + 1 / sqrt((m.x18 - m.x67)
    **2 + (m.x88 - m.x137)**2 + (m.x158 - m.x207)**2) + 1 / sqrt((m.x18 - m.x68)
    **2 + (m.x88 - m.x138)**2 + (m.x158 - m.x208)**2) + 1 / sqrt((m.x18 - m.x69)
    **2 + (m.x88 - m.x139)**2 + (m.x158 - m.x209)**2) + 1 / sqrt((m.x18 - m.x70)
    **2 + (m.x88 - m.x140)**2 + (m.x158 - m.x210)**2) + 1 / sqrt((m.x19 - m.x20)
    **2 + (m.x89 - m.x90)**2 + (m.x159 - m.x160)**2) + 1 / sqrt((m.x19 - m.x21)
    **2 + (m.x89 - m.x91)**2 + (m.x159 - m.x161)**2) + 1 / sqrt((m.x19 - m.x22)
    **2 + (m.x89 - m.x92)**2 + (m.x159 - m.x162)**2) + 1 / sqrt((m.x19 - m.x23)
    **2 + (m.x89 - m.x93)**2 + (m.x159 - m.x163)**2) + 1 / sqrt((m.x19 - m.x24)
    **2 + (m.x89 - m.x94)**2 + (m.x159 - m.x164)**2) + 1 / sqrt((m.x19 - m.x25)
    **2 + (m.x89 - m.x95)**2 + (m.x159 - m.x165)**2) + 1 / sqrt((m.x19 - m.x26)
    **2 + (m.x89 - m.x96)**2 + (m.x159 - m.x166)**2) + 1 / sqrt((m.x19 - m.x27)
    **2 + (m.x89 - m.x97)**2 + (m.x159 - m.x167)**2) + 1 / sqrt((m.x19 - m.x28)
    **2 + (m.x89 - m.x98)**2 + (m.x159 - m.x168)**2) + 1 / sqrt((m.x19 - m.x29)
    **2 + (m.x89 - m.x99)**2 + (m.x159 - m.x169)**2) + 1 / sqrt((m.x19 - m.x30)
    **2 + (m.x89 - m.x100)**2 + (m.x159 - m.x170)**2) + 1 / sqrt((m.x19 - m.x31)
    **2 + (m.x89 - m.x101)**2 + (m.x159 - m.x171)**2) + 1 / sqrt((m.x19 - m.x32)
    **2 + (m.x89 - m.x102)**2 + (m.x159 - m.x172)**2) + 1 / sqrt((m.x19 - m.x33)
    **2 + (m.x89 - m.x103)**2 + (m.x159 - m.x173)**2) + 1 / sqrt((m.x19 - m.x34)
    **2 + (m.x89 - m.x104)**2 + (m.x159 - m.x174)**2) + 1 / sqrt((m.x19 - m.x35)
    **2 + (m.x89 - m.x105)**2 + (m.x159 - m.x175)**2) + 1 / sqrt((m.x19 - m.x36)
    **2 + (m.x89 - m.x106)**2 + (m.x159 - m.x176)**2) + 1 / sqrt((m.x19 - m.x37)
    **2 + (m.x89 - m.x107)**2 + (m.x159 - m.x177)**2) + 1 / sqrt((m.x19 - m.x38)
    **2 + (m.x89 - m.x108)**2 + (m.x159 - m.x178)**2) + 1 / sqrt((m.x19 - m.x39)
    **2 + (m.x89 - m.x109)**2 + (m.x159 - m.x179)**2) + 1 / sqrt((m.x19 - m.x40)
    **2 + (m.x89 - m.x110)**2 + (m.x159 - m.x180)**2) + 1 / sqrt((m.x19 - m.x41)
    **2 + (m.x89 - m.x111)**2 + (m.x159 - m.x181)**2) + 1 / sqrt((m.x19 - m.x42)
    **2 + (m.x89 - m.x112)**2 + (m.x159 - m.x182)**2) + 1 / sqrt((m.x19 - m.x43)
    **2 + (m.x89 - m.x113)**2 + (m.x159 - m.x183)**2) + 1 / sqrt((m.x19 - m.x44)
    **2 + (m.x89 - m.x114)**2 + (m.x159 - m.x184)**2) + 1 / sqrt((m.x19 - m.x45)
    **2 + (m.x89 - m.x115)**2 + (m.x159 - m.x185)**2) + 1 / sqrt((m.x19 - m.x46)
    **2 + (m.x89 - m.x116)**2 + (m.x159 - m.x186)**2) + 1 / sqrt((m.x19 - m.x47)
    **2 + (m.x89 - m.x117)**2 + (m.x159 - m.x187)**2) + 1 / sqrt((m.x19 - m.x48)
    **2 + (m.x89 - m.x118)**2 + (m.x159 - m.x188)**2) + 1 / sqrt((m.x19 - m.x49)
    **2 + (m.x89 - m.x119)**2 + (m.x159 - m.x189)**2) + 1 / sqrt((m.x19 - m.x50)
    **2 + (m.x89 - m.x120)**2 + (m.x159 - m.x190)**2) + 1 / sqrt((m.x19 - m.x51)
    **2 + (m.x89 - m.x121)**2 + (m.x159 - m.x191)**2) + 1 / sqrt((m.x19 - m.x52)
    **2 + (m.x89 - m.x122)**2 + (m.x159 - m.x192)**2) + 1 / sqrt((m.x19 - m.x53)
    **2 + (m.x89 - m.x123)**2 + (m.x159 - m.x193)**2) + 1 / sqrt((m.x19 - m.x54)
    **2 + (m.x89 - m.x124)**2 + (m.x159 - m.x194)**2) + 1 / sqrt((m.x19 - m.x55)
    **2 + (m.x89 - m.x125)**2 + (m.x159 - m.x195)**2) + 1 / sqrt((m.x19 - m.x56)
    **2 + (m.x89 - m.x126)**2 + (m.x159 - m.x196)**2) + 1 / sqrt((m.x19 - m.x57)
    **2 + (m.x89 - m.x127)**2 + (m.x159 - m.x197)**2) + 1 / sqrt((m.x19 - m.x58)
    **2 + (m.x89 - m.x128)**2 + (m.x159 - m.x198)**2) + 1 / sqrt((m.x19 - m.x59)
    **2 + (m.x89 - m.x129)**2 + (m.x159 - m.x199)**2) + 1 / sqrt((m.x19 - m.x60)
    **2 + (m.x89 - m.x130)**2 + (m.x159 - m.x200)**2) + 1 / sqrt((m.x19 - m.x61)
    **2 + (m.x89 - m.x131)**2 + (m.x159 - m.x201)**2) + 1 / sqrt((m.x19 - m.x62)
    **2 + (m.x89 - m.x132)**2 + (m.x159 - m.x202)**2) + 1 / sqrt((m.x19 - m.x63)
    **2 + (m.x89 - m.x133)**2 + (m.x159 - m.x203)**2) + 1 / sqrt((m.x19 - m.x64)
    **2 + (m.x89 - m.x134)**2 + (m.x159 - m.x204)**2) + 1 / sqrt((m.x19 - m.x65)
    **2 + (m.x89 - m.x135)**2 + (m.x159 - m.x205)**2) + 1 / sqrt((m.x19 - m.x66)
    **2 + (m.x89 - m.x136)**2 + (m.x159 - m.x206)**2) + 1 / sqrt((m.x19 - m.x67)
    **2 + (m.x89 - m.x137)**2 + (m.x159 - m.x207)**2) + 1 / sqrt((m.x19 - m.x68)
    **2 + (m.x89 - m.x138)**2 + (m.x159 - m.x208)**2) + 1 / sqrt((m.x19 - m.x69)
    **2 + (m.x89 - m.x139)**2 + (m.x159 - m.x209)**2) + 1 / sqrt((m.x19 - m.x70)
    **2 + (m.x89 - m.x140)**2 + (m.x159 - m.x210)**2) + 1 / sqrt((m.x20 - m.x21)
    **2 + (m.x90 - m.x91)**2 + (m.x160 - m.x161)**2) + 1 / sqrt((m.x20 - m.x22)
    **2 + (m.x90 - m.x92)**2 + (m.x160 - m.x162)**2) + 1 / sqrt((m.x20 - m.x23)
    **2 + (m.x90 - m.x93)**2 + (m.x160 - m.x163)**2) + 1 / sqrt((m.x20 - m.x24)
    **2 + (m.x90 - m.x94)**2 + (m.x160 - m.x164)**2) + 1 / sqrt((m.x20 - m.x25)
    **2 + (m.x90 - m.x95)**2 + (m.x160 - m.x165)**2) + 1 / sqrt((m.x20 - m.x26)
    **2 + (m.x90 - m.x96)**2 + (m.x160 - m.x166)**2) + 1 / sqrt((m.x20 - m.x27)
    **2 + (m.x90 - m.x97)**2 + (m.x160 - m.x167)**2) + 1 / sqrt((m.x20 - m.x28)
    **2 + (m.x90 - m.x98)**2 + (m.x160 - m.x168)**2) + 1 / sqrt((m.x20 - m.x29)
    **2 + (m.x90 - m.x99)**2 + (m.x160 - m.x169)**2) + 1 / sqrt((m.x20 - m.x30)
    **2 + (m.x90 - m.x100)**2 + (m.x160 - m.x170)**2) + 1 / sqrt((m.x20 - m.x31)
    **2 + (m.x90 - m.x101)**2 + (m.x160 - m.x171)**2) + 1 / sqrt((m.x20 - m.x32)
    **2 + (m.x90 - m.x102)**2 + (m.x160 - m.x172)**2) + 1 / sqrt((m.x20 - m.x33)
    **2 + (m.x90 - m.x103)**2 + (m.x160 - m.x173)**2) + 1 / sqrt((m.x20 - m.x34)
    **2 + (m.x90 - m.x104)**2 + (m.x160 - m.x174)**2) + 1 / sqrt((m.x20 - m.x35)
    **2 + (m.x90 - m.x105)**2 + (m.x160 - m.x175)**2) + 1 / sqrt((m.x20 - m.x36)
    **2 + (m.x90 - m.x106)**2 + (m.x160 - m.x176)**2) + 1 / sqrt((m.x20 - m.x37)
    **2 + (m.x90 - m.x107)**2 + (m.x160 - m.x177)**2) + 1 / sqrt((m.x20 - m.x38)
    **2 + (m.x90 - m.x108)**2 + (m.x160 - m.x178)**2) + 1 / sqrt((m.x20 - m.x39)
    **2 + (m.x90 - m.x109)**2 + (m.x160 - m.x179)**2) + 1 / sqrt((m.x20 - m.x40)
    **2 + (m.x90 - m.x110)**2 + (m.x160 - m.x180)**2) + 1 / sqrt((m.x20 - m.x41)
    **2 + (m.x90 - m.x111)**2 + (m.x160 - m.x181)**2) + 1 / sqrt((m.x20 - m.x42)
    **2 + (m.x90 - m.x112)**2 + (m.x160 - m.x182)**2) + 1 / sqrt((m.x20 - m.x43)
    **2 + (m.x90 - m.x113)**2 + (m.x160 - m.x183)**2) + 1 / sqrt((m.x20 - m.x44)
    **2 + (m.x90 - m.x114)**2 + (m.x160 - m.x184)**2) + 1 / sqrt((m.x20 - m.x45)
    **2 + (m.x90 - m.x115)**2 + (m.x160 - m.x185)**2) + 1 / sqrt((m.x20 - m.x46)
    **2 + (m.x90 - m.x116)**2 + (m.x160 - m.x186)**2) + 1 / sqrt((m.x20 - m.x47)
    **2 + (m.x90 - m.x117)**2 + (m.x160 - m.x187)**2) + 1 / sqrt((m.x20 - m.x48)
    **2 + (m.x90 - m.x118)**2 + (m.x160 - m.x188)**2) + 1 / sqrt((m.x20 - m.x49)
    **2 + (m.x90 - m.x119)**2 + (m.x160 - m.x189)**2) + 1 / sqrt((m.x20 - m.x50)
    **2 + (m.x90 - m.x120)**2 + (m.x160 - m.x190)**2) + 1 / sqrt((m.x20 - m.x51)
    **2 + (m.x90 - m.x121)**2 + (m.x160 - m.x191)**2) + 1 / sqrt((m.x20 - m.x52)
    **2 + (m.x90 - m.x122)**2 + (m.x160 - m.x192)**2) + 1 / sqrt((m.x20 - m.x53)
    **2 + (m.x90 - m.x123)**2 + (m.x160 - m.x193)**2) + 1 / sqrt((m.x20 - m.x54)
    **2 + (m.x90 - m.x124)**2 + (m.x160 - m.x194)**2) + 1 / sqrt((m.x20 - m.x55)
    **2 + (m.x90 - m.x125)**2 + (m.x160 - m.x195)**2) + 1 / sqrt((m.x20 - m.x56)
    **2 + (m.x90 - m.x126)**2 + (m.x160 - m.x196)**2) + 1 / sqrt((m.x20 - m.x57)
    **2 + (m.x90 - m.x127)**2 + (m.x160 - m.x197)**2) + 1 / sqrt((m.x20 - m.x58)
    **2 + (m.x90 - m.x128)**2 + (m.x160 - m.x198)**2) + 1 / sqrt((m.x20 - m.x59)
    **2 + (m.x90 - m.x129)**2 + (m.x160 - m.x199)**2) + 1 / sqrt((m.x20 - m.x60)
    **2 + (m.x90 - m.x130)**2 + (m.x160 - m.x200)**2) + 1 / sqrt((m.x20 - m.x61)
    **2 + (m.x90 - m.x131)**2 + (m.x160 - m.x201)**2) + 1 / sqrt((m.x20 - m.x62)
    **2 + (m.x90 - m.x132)**2 + (m.x160 - m.x202)**2) + 1 / sqrt((m.x20 - m.x63)
    **2 + (m.x90 - m.x133)**2 + (m.x160 - m.x203)**2) + 1 / sqrt((m.x20 - m.x64)
    **2 + (m.x90 - m.x134)**2 + (m.x160 - m.x204)**2) + 1 / sqrt((m.x20 - m.x65)
    **2 + (m.x90 - m.x135)**2 + (m.x160 - m.x205)**2) + 1 / sqrt((m.x20 - m.x66)
    **2 + (m.x90 - m.x136)**2 + (m.x160 - m.x206)**2) + 1 / sqrt((m.x20 - m.x67)
    **2 + (m.x90 - m.x137)**2 + (m.x160 - m.x207)**2) + 1 / sqrt((m.x20 - m.x68)
    **2 + (m.x90 - m.x138)**2 + (m.x160 - m.x208)**2) + 1 / sqrt((m.x20 - m.x69)
    **2 + (m.x90 - m.x139)**2 + (m.x160 - m.x209)**2) + 1 / sqrt((m.x20 - m.x70)
    **2 + (m.x90 - m.x140)**2 + (m.x160 - m.x210)**2) + 1 / sqrt((m.x21 - m.x22)
    **2 + (m.x91 - m.x92)**2 + (m.x161 - m.x162)**2) + 1 / sqrt((m.x21 - m.x23)
    **2 + (m.x91 - m.x93)**2 + (m.x161 - m.x163)**2) + 1 / sqrt((m.x21 - m.x24)
    **2 + (m.x91 - m.x94)**2 + (m.x161 - m.x164)**2) + 1 / sqrt((m.x21 - m.x25)
    **2 + (m.x91 - m.x95)**2 + (m.x161 - m.x165)**2) + 1 / sqrt((m.x21 - m.x26)
    **2 + (m.x91 - m.x96)**2 + (m.x161 - m.x166)**2) + 1 / sqrt((m.x21 - m.x27)
    **2 + (m.x91 - m.x97)**2 + (m.x161 - m.x167)**2) + 1 / sqrt((m.x21 - m.x28)
    **2 + (m.x91 - m.x98)**2 + (m.x161 - m.x168)**2) + 1 / sqrt((m.x21 - m.x29)
    **2 + (m.x91 - m.x99)**2 + (m.x161 - m.x169)**2) + 1 / sqrt((m.x21 - m.x30)
    **2 + (m.x91 - m.x100)**2 + (m.x161 - m.x170)**2) + 1 / sqrt((m.x21 - m.x31)
    **2 + (m.x91 - m.x101)**2 + (m.x161 - m.x171)**2) + 1 / sqrt((m.x21 - m.x32)
    **2 + (m.x91 - m.x102)**2 + (m.x161 - m.x172)**2) + 1 / sqrt((m.x21 - m.x33)
    **2 + (m.x91 - m.x103)**2 + (m.x161 - m.x173)**2) + 1 / sqrt((m.x21 - m.x34)
    **2 + (m.x91 - m.x104)**2 + (m.x161 - m.x174)**2) + 1 / sqrt((m.x21 - m.x35)
    **2 + (m.x91 - m.x105)**2 + (m.x161 - m.x175)**2) + 1 / sqrt((m.x21 - m.x36)
    **2 + (m.x91 - m.x106)**2 + (m.x161 - m.x176)**2) + 1 / sqrt((m.x21 - m.x37)
    **2 + (m.x91 - m.x107)**2 + (m.x161 - m.x177)**2) + 1 / sqrt((m.x21 - m.x38)
    **2 + (m.x91 - m.x108)**2 + (m.x161 - m.x178)**2) + 1 / sqrt((m.x21 - m.x39)
    **2 + (m.x91 - m.x109)**2 + (m.x161 - m.x179)**2) + 1 / sqrt((m.x21 - m.x40)
    **2 + (m.x91 - m.x110)**2 + (m.x161 - m.x180)**2) + 1 / sqrt((m.x21 - m.x41)
    **2 + (m.x91 - m.x111)**2 + (m.x161 - m.x181)**2) + 1 / sqrt((m.x21 - m.x42)
    **2 + (m.x91 - m.x112)**2 + (m.x161 - m.x182)**2) + 1 / sqrt((m.x21 - m.x43)
    **2 + (m.x91 - m.x113)**2 + (m.x161 - m.x183)**2) + 1 / sqrt((m.x21 - m.x44)
    **2 + (m.x91 - m.x114)**2 + (m.x161 - m.x184)**2) + 1 / sqrt((m.x21 - m.x45)
    **2 + (m.x91 - m.x115)**2 + (m.x161 - m.x185)**2) + 1 / sqrt((m.x21 - m.x46)
    **2 + (m.x91 - m.x116)**2 + (m.x161 - m.x186)**2) + 1 / sqrt((m.x21 - m.x47)
    **2 + (m.x91 - m.x117)**2 + (m.x161 - m.x187)**2) + 1 / sqrt((m.x21 - m.x48)
    **2 + (m.x91 - m.x118)**2 + (m.x161 - m.x188)**2) + 1 / sqrt((m.x21 - m.x49)
    **2 + (m.x91 - m.x119)**2 + (m.x161 - m.x189)**2) + 1 / sqrt((m.x21 - m.x50)
    **2 + (m.x91 - m.x120)**2 + (m.x161 - m.x190)**2) + 1 / sqrt((m.x21 - m.x51)
    **2 + (m.x91 - m.x121)**2 + (m.x161 - m.x191)**2) + 1 / sqrt((m.x21 - m.x52)
    **2 + (m.x91 - m.x122)**2 + (m.x161 - m.x192)**2) + 1 / sqrt((m.x21 - m.x53)
    **2 + (m.x91 - m.x123)**2 + (m.x161 - m.x193)**2) + 1 / sqrt((m.x21 - m.x54)
    **2 + (m.x91 - m.x124)**2 + (m.x161 - m.x194)**2) + 1 / sqrt((m.x21 - m.x55)
    **2 + (m.x91 - m.x125)**2 + (m.x161 - m.x195)**2) + 1 / sqrt((m.x21 - m.x56)
    **2 + (m.x91 - m.x126)**2 + (m.x161 - m.x196)**2) + 1 / sqrt((m.x21 - m.x57)
    **2 + (m.x91 - m.x127)**2 + (m.x161 - m.x197)**2) + 1 / sqrt((m.x21 - m.x58)
    **2 + (m.x91 - m.x128)**2 + (m.x161 - m.x198)**2) + 1 / sqrt((m.x21 - m.x59)
    **2 + (m.x91 - m.x129)**2 + (m.x161 - m.x199)**2) + 1 / sqrt((m.x21 - m.x60)
    **2 + (m.x91 - m.x130)**2 + (m.x161 - m.x200)**2) + 1 / sqrt((m.x21 - m.x61)
    **2 + (m.x91 - m.x131)**2 + (m.x161 - m.x201)**2) + 1 / sqrt((m.x21 - m.x62)
    **2 + (m.x91 - m.x132)**2 + (m.x161 - m.x202)**2) + 1 / sqrt((m.x21 - m.x63)
    **2 + (m.x91 - m.x133)**2 + (m.x161 - m.x203)**2) + 1 / sqrt((m.x21 - m.x64)
    **2 + (m.x91 - m.x134)**2 + (m.x161 - m.x204)**2) + 1 / sqrt((m.x21 - m.x65)
    **2 + (m.x91 - m.x135)**2 + (m.x161 - m.x205)**2) + 1 / sqrt((m.x21 - m.x66)
    **2 + (m.x91 - m.x136)**2 + (m.x161 - m.x206)**2) + 1 / sqrt((m.x21 - m.x67)
    **2 + (m.x91 - m.x137)**2 + (m.x161 - m.x207)**2) + 1 / sqrt((m.x21 - m.x68)
    **2 + (m.x91 - m.x138)**2 + (m.x161 - m.x208)**2) + 1 / sqrt((m.x21 - m.x69)
    **2 + (m.x91 - m.x139)**2 + (m.x161 - m.x209)**2) + 1 / sqrt((m.x21 - m.x70)
    **2 + (m.x91 - m.x140)**2 + (m.x161 - m.x210)**2) + 1 / sqrt((m.x22 - m.x23)
    **2 + (m.x92 - m.x93)**2 + (m.x162 - m.x163)**2) + 1 / sqrt((m.x22 - m.x24)
    **2 + (m.x92 - m.x94)**2 + (m.x162 - m.x164)**2) + 1 / sqrt((m.x22 - m.x25)
    **2 + (m.x92 - m.x95)**2 + (m.x162 - m.x165)**2) + 1 / sqrt((m.x22 - m.x26)
    **2 + (m.x92 - m.x96)**2 + (m.x162 - m.x166)**2) + 1 / sqrt((m.x22 - m.x27)
    **2 + (m.x92 - m.x97)**2 + (m.x162 - m.x167)**2) + 1 / sqrt((m.x22 - m.x28)
    **2 + (m.x92 - m.x98)**2 + (m.x162 - m.x168)**2) + 1 / sqrt((m.x22 - m.x29)
    **2 + (m.x92 - m.x99)**2 + (m.x162 - m.x169)**2) + 1 / sqrt((m.x22 - m.x30)
    **2 + (m.x92 - m.x100)**2 + (m.x162 - m.x170)**2) + 1 / sqrt((m.x22 - m.x31)
    **2 + (m.x92 - m.x101)**2 + (m.x162 - m.x171)**2) + 1 / sqrt((m.x22 - m.x32)
    **2 + (m.x92 - m.x102)**2 + (m.x162 - m.x172)**2) + 1 / sqrt((m.x22 - m.x33)
    **2 + (m.x92 - m.x103)**2 + (m.x162 - m.x173)**2) + 1 / sqrt((m.x22 - m.x34)
    **2 + (m.x92 - m.x104)**2 + (m.x162 - m.x174)**2) + 1 / sqrt((m.x22 - m.x35)
    **2 + (m.x92 - m.x105)**2 + (m.x162 - m.x175)**2) + 1 / sqrt((m.x22 - m.x36)
    **2 + (m.x92 - m.x106)**2 + (m.x162 - m.x176)**2) + 1 / sqrt((m.x22 - m.x37)
    **2 + (m.x92 - m.x107)**2 + (m.x162 - m.x177)**2) + 1 / sqrt((m.x22 - m.x38)
    **2 + (m.x92 - m.x108)**2 + (m.x162 - m.x178)**2) + 1 / sqrt((m.x22 - m.x39)
    **2 + (m.x92 - m.x109)**2 + (m.x162 - m.x179)**2) + 1 / sqrt((m.x22 - m.x40)
    **2 + (m.x92 - m.x110)**2 + (m.x162 - m.x180)**2) + 1 / sqrt((m.x22 - m.x41)
    **2 + (m.x92 - m.x111)**2 + (m.x162 - m.x181)**2) + 1 / sqrt((m.x22 - m.x42)
    **2 + (m.x92 - m.x112)**2 + (m.x162 - m.x182)**2) + 1 / sqrt((m.x22 - m.x43)
    **2 + (m.x92 - m.x113)**2 + (m.x162 - m.x183)**2) + 1 / sqrt((m.x22 - m.x44)
    **2 + (m.x92 - m.x114)**2 + (m.x162 - m.x184)**2) + 1 / sqrt((m.x22 - m.x45)
    **2 + (m.x92 - m.x115)**2 + (m.x162 - m.x185)**2) + 1 / sqrt((m.x22 - m.x46)
    **2 + (m.x92 - m.x116)**2 + (m.x162 - m.x186)**2) + 1 / sqrt((m.x22 - m.x47)
    **2 + (m.x92 - m.x117)**2 + (m.x162 - m.x187)**2) + 1 / sqrt((m.x22 - m.x48)
    **2 + (m.x92 - m.x118)**2 + (m.x162 - m.x188)**2) + 1 / sqrt((m.x22 - m.x49)
    **2 + (m.x92 - m.x119)**2 + (m.x162 - m.x189)**2) + 1 / sqrt((m.x22 - m.x50)
    **2 + (m.x92 - m.x120)**2 + (m.x162 - m.x190)**2) + 1 / sqrt((m.x22 - m.x51)
    **2 + (m.x92 - m.x121)**2 + (m.x162 - m.x191)**2) + 1 / sqrt((m.x22 - m.x52)
    **2 + (m.x92 - m.x122)**2 + (m.x162 - m.x192)**2) + 1 / sqrt((m.x22 - m.x53)
    **2 + (m.x92 - m.x123)**2 + (m.x162 - m.x193)**2) + 1 / sqrt((m.x22 - m.x54)
    **2 + (m.x92 - m.x124)**2 + (m.x162 - m.x194)**2) + 1 / sqrt((m.x22 - m.x55)
    **2 + (m.x92 - m.x125)**2 + (m.x162 - m.x195)**2) + 1 / sqrt((m.x22 - m.x56)
    **2 + (m.x92 - m.x126)**2 + (m.x162 - m.x196)**2) + 1 / sqrt((m.x22 - m.x57)
    **2 + (m.x92 - m.x127)**2 + (m.x162 - m.x197)**2) + 1 / sqrt((m.x22 - m.x58)
    **2 + (m.x92 - m.x128)**2 + (m.x162 - m.x198)**2) + 1 / sqrt((m.x22 - m.x59)
    **2 + (m.x92 - m.x129)**2 + (m.x162 - m.x199)**2) + 1 / sqrt((m.x22 - m.x60)
    **2 + (m.x92 - m.x130)**2 + (m.x162 - m.x200)**2) + 1 / sqrt((m.x22 - m.x61)
    **2 + (m.x92 - m.x131)**2 + (m.x162 - m.x201)**2) + 1 / sqrt((m.x22 - m.x62)
    **2 + (m.x92 - m.x132)**2 + (m.x162 - m.x202)**2) + 1 / sqrt((m.x22 - m.x63)
    **2 + (m.x92 - m.x133)**2 + (m.x162 - m.x203)**2) + 1 / sqrt((m.x22 - m.x64)
    **2 + (m.x92 - m.x134)**2 + (m.x162 - m.x204)**2) + 1 / sqrt((m.x22 - m.x65)
    **2 + (m.x92 - m.x135)**2 + (m.x162 - m.x205)**2) + 1 / sqrt((m.x22 - m.x66)
    **2 + (m.x92 - m.x136)**2 + (m.x162 - m.x206)**2) + 1 / sqrt((m.x22 - m.x67)
    **2 + (m.x92 - m.x137)**2 + (m.x162 - m.x207)**2) + 1 / sqrt((m.x22 - m.x68)
    **2 + (m.x92 - m.x138)**2 + (m.x162 - m.x208)**2) + 1 / sqrt((m.x22 - m.x69)
    **2 + (m.x92 - m.x139)**2 + (m.x162 - m.x209)**2) + 1 / sqrt((m.x22 - m.x70)
    **2 + (m.x92 - m.x140)**2 + (m.x162 - m.x210)**2) + 1 / sqrt((m.x23 - m.x24)
    **2 + (m.x93 - m.x94)**2 + (m.x163 - m.x164)**2) + 1 / sqrt((m.x23 - m.x25)
    **2 + (m.x93 - m.x95)**2 + (m.x163 - m.x165)**2) + 1 / sqrt((m.x23 - m.x26)
    **2 + (m.x93 - m.x96)**2 + (m.x163 - m.x166)**2) + 1 / sqrt((m.x23 - m.x27)
    **2 + (m.x93 - m.x97)**2 + (m.x163 - m.x167)**2) + 1 / sqrt((m.x23 - m.x28)
    **2 + (m.x93 - m.x98)**2 + (m.x163 - m.x168)**2) + 1 / sqrt((m.x23 - m.x29)
    **2 + (m.x93 - m.x99)**2 + (m.x163 - m.x169)**2) + 1 / sqrt((m.x23 - m.x30)
    **2 + (m.x93 - m.x100)**2 + (m.x163 - m.x170)**2) + 1 / sqrt((m.x23 - m.x31)
    **2 + (m.x93 - m.x101)**2 + (m.x163 - m.x171)**2) + 1 / sqrt((m.x23 - m.x32)
    **2 + (m.x93 - m.x102)**2 + (m.x163 - m.x172)**2) + 1 / sqrt((m.x23 - m.x33)
    **2 + (m.x93 - m.x103)**2 + (m.x163 - m.x173)**2) + 1 / sqrt((m.x23 - m.x34)
    **2 + (m.x93 - m.x104)**2 + (m.x163 - m.x174)**2) + 1 / sqrt((m.x23 - m.x35)
    **2 + (m.x93 - m.x105)**2 + (m.x163 - m.x175)**2) + 1 / sqrt((m.x23 - m.x36)
    **2 + (m.x93 - m.x106)**2 + (m.x163 - m.x176)**2) + 1 / sqrt((m.x23 - m.x37)
    **2 + (m.x93 - m.x107)**2 + (m.x163 - m.x177)**2) + 1 / sqrt((m.x23 - m.x38)
    **2 + (m.x93 - m.x108)**2 + (m.x163 - m.x178)**2) + 1 / sqrt((m.x23 - m.x39)
    **2 + (m.x93 - m.x109)**2 + (m.x163 - m.x179)**2) + 1 / sqrt((m.x23 - m.x40)
    **2 + (m.x93 - m.x110)**2 + (m.x163 - m.x180)**2) + 1 / sqrt((m.x23 - m.x41)
    **2 + (m.x93 - m.x111)**2 + (m.x163 - m.x181)**2) + 1 / sqrt((m.x23 - m.x42)
    **2 + (m.x93 - m.x112)**2 + (m.x163 - m.x182)**2) + 1 / sqrt((m.x23 - m.x43)
    **2 + (m.x93 - m.x113)**2 + (m.x163 - m.x183)**2) + 1 / sqrt((m.x23 - m.x44)
    **2 + (m.x93 - m.x114)**2 + (m.x163 - m.x184)**2) + 1 / sqrt((m.x23 - m.x45)
    **2 + (m.x93 - m.x115)**2 + (m.x163 - m.x185)**2) + 1 / sqrt((m.x23 - m.x46)
    **2 + (m.x93 - m.x116)**2 + (m.x163 - m.x186)**2) + 1 / sqrt((m.x23 - m.x47)
    **2 + (m.x93 - m.x117)**2 + (m.x163 - m.x187)**2) + 1 / sqrt((m.x23 - m.x48)
    **2 + (m.x93 - m.x118)**2 + (m.x163 - m.x188)**2) + 1 / sqrt((m.x23 - m.x49)
    **2 + (m.x93 - m.x119)**2 + (m.x163 - m.x189)**2) + 1 / sqrt((m.x23 - m.x50)
    **2 + (m.x93 - m.x120)**2 + (m.x163 - m.x190)**2) + 1 / sqrt((m.x23 - m.x51)
    **2 + (m.x93 - m.x121)**2 + (m.x163 - m.x191)**2) + 1 / sqrt((m.x23 - m.x52)
    **2 + (m.x93 - m.x122)**2 + (m.x163 - m.x192)**2) + 1 / sqrt((m.x23 - m.x53)
    **2 + (m.x93 - m.x123)**2 + (m.x163 - m.x193)**2) + 1 / sqrt((m.x23 - m.x54)
    **2 + (m.x93 - m.x124)**2 + (m.x163 - m.x194)**2) + 1 / sqrt((m.x23 - m.x55)
    **2 + (m.x93 - m.x125)**2 + (m.x163 - m.x195)**2) + 1 / sqrt((m.x23 - m.x56)
    **2 + (m.x93 - m.x126)**2 + (m.x163 - m.x196)**2) + 1 / sqrt((m.x23 - m.x57)
    **2 + (m.x93 - m.x127)**2 + (m.x163 - m.x197)**2) + 1 / sqrt((m.x23 - m.x58)
    **2 + (m.x93 - m.x128)**2 + (m.x163 - m.x198)**2) + 1 / sqrt((m.x23 - m.x59)
    **2 + (m.x93 - m.x129)**2 + (m.x163 - m.x199)**2) + 1 / sqrt((m.x23 - m.x60)
    **2 + (m.x93 - m.x130)**2 + (m.x163 - m.x200)**2) + 1 / sqrt((m.x23 - m.x61)
    **2 + (m.x93 - m.x131)**2 + (m.x163 - m.x201)**2) + 1 / sqrt((m.x23 - m.x62)
    **2 + (m.x93 - m.x132)**2 + (m.x163 - m.x202)**2) + 1 / sqrt((m.x23 - m.x63)
    **2 + (m.x93 - m.x133)**2 + (m.x163 - m.x203)**2) + 1 / sqrt((m.x23 - m.x64)
    **2 + (m.x93 - m.x134)**2 + (m.x163 - m.x204)**2) + 1 / sqrt((m.x23 - m.x65)
    **2 + (m.x93 - m.x135)**2 + (m.x163 - m.x205)**2) + 1 / sqrt((m.x23 - m.x66)
    **2 + (m.x93 - m.x136)**2 + (m.x163 - m.x206)**2) + 1 / sqrt((m.x23 - m.x67)
    **2 + (m.x93 - m.x137)**2 + (m.x163 - m.x207)**2) + 1 / sqrt((m.x23 - m.x68)
    **2 + (m.x93 - m.x138)**2 + (m.x163 - m.x208)**2) + 1 / sqrt((m.x23 - m.x69)
    **2 + (m.x93 - m.x139)**2 + (m.x163 - m.x209)**2) + 1 / sqrt((m.x23 - m.x70)
    **2 + (m.x93 - m.x140)**2 + (m.x163 - m.x210)**2) + 1 / sqrt((m.x24 - m.x25)
    **2 + (m.x94 - m.x95)**2 + (m.x164 - m.x165)**2) + 1 / sqrt((m.x24 - m.x26)
    **2 + (m.x94 - m.x96)**2 + (m.x164 - m.x166)**2) + 1 / sqrt((m.x24 - m.x27)
    **2 + (m.x94 - m.x97)**2 + (m.x164 - m.x167)**2) + 1 / sqrt((m.x24 - m.x28)
    **2 + (m.x94 - m.x98)**2 + (m.x164 - m.x168)**2) + 1 / sqrt((m.x24 - m.x29)
    **2 + (m.x94 - m.x99)**2 + (m.x164 - m.x169)**2) + 1 / sqrt((m.x24 - m.x30)
    **2 + (m.x94 - m.x100)**2 + (m.x164 - m.x170)**2) + 1 / sqrt((m.x24 - m.x31)
    **2 + (m.x94 - m.x101)**2 + (m.x164 - m.x171)**2) + 1 / sqrt((m.x24 - m.x32)
    **2 + (m.x94 - m.x102)**2 + (m.x164 - m.x172)**2) + 1 / sqrt((m.x24 - m.x33)
    **2 + (m.x94 - m.x103)**2 + (m.x164 - m.x173)**2) + 1 / sqrt((m.x24 - m.x34)
    **2 + (m.x94 - m.x104)**2 + (m.x164 - m.x174)**2) + 1 / sqrt((m.x24 - m.x35)
    **2 + (m.x94 - m.x105)**2 + (m.x164 - m.x175)**2) + 1 / sqrt((m.x24 - m.x36)
    **2 + (m.x94 - m.x106)**2 + (m.x164 - m.x176)**2) + 1 / sqrt((m.x24 - m.x37)
    **2 + (m.x94 - m.x107)**2 + (m.x164 - m.x177)**2) + 1 / sqrt((m.x24 - m.x38)
    **2 + (m.x94 - m.x108)**2 + (m.x164 - m.x178)**2) + 1 / sqrt((m.x24 - m.x39)
    **2 + (m.x94 - m.x109)**2 + (m.x164 - m.x179)**2) + 1 / sqrt((m.x24 - m.x40)
    **2 + (m.x94 - m.x110)**2 + (m.x164 - m.x180)**2) + 1 / sqrt((m.x24 - m.x41)
    **2 + (m.x94 - m.x111)**2 + (m.x164 - m.x181)**2) + 1 / sqrt((m.x24 - m.x42)
    **2 + (m.x94 - m.x112)**2 + (m.x164 - m.x182)**2) + 1 / sqrt((m.x24 - m.x43)
    **2 + (m.x94 - m.x113)**2 + (m.x164 - m.x183)**2) + 1 / sqrt((m.x24 - m.x44)
    **2 + (m.x94 - m.x114)**2 + (m.x164 - m.x184)**2) + 1 / sqrt((m.x24 - m.x45)
    **2 + (m.x94 - m.x115)**2 + (m.x164 - m.x185)**2) + 1 / sqrt((m.x24 - m.x46)
    **2 + (m.x94 - m.x116)**2 + (m.x164 - m.x186)**2) + 1 / sqrt((m.x24 - m.x47)
    **2 + (m.x94 - m.x117)**2 + (m.x164 - m.x187)**2) + 1 / sqrt((m.x24 - m.x48)
    **2 + (m.x94 - m.x118)**2 + (m.x164 - m.x188)**2) + 1 / sqrt((m.x24 - m.x49)
    **2 + (m.x94 - m.x119)**2 + (m.x164 - m.x189)**2) + 1 / sqrt((m.x24 - m.x50)
    **2 + (m.x94 - m.x120)**2 + (m.x164 - m.x190)**2) + 1 / sqrt((m.x24 - m.x51)
    **2 + (m.x94 - m.x121)**2 + (m.x164 - m.x191)**2) + 1 / sqrt((m.x24 - m.x52)
    **2 + (m.x94 - m.x122)**2 + (m.x164 - m.x192)**2) + 1 / sqrt((m.x24 - m.x53)
    **2 + (m.x94 - m.x123)**2 + (m.x164 - m.x193)**2) + 1 / sqrt((m.x24 - m.x54)
    **2 + (m.x94 - m.x124)**2 + (m.x164 - m.x194)**2) + 1 / sqrt((m.x24 - m.x55)
    **2 + (m.x94 - m.x125)**2 + (m.x164 - m.x195)**2) + 1 / sqrt((m.x24 - m.x56)
    **2 + (m.x94 - m.x126)**2 + (m.x164 - m.x196)**2) + 1 / sqrt((m.x24 - m.x57)
    **2 + (m.x94 - m.x127)**2 + (m.x164 - m.x197)**2) + 1 / sqrt((m.x24 - m.x58)
    **2 + (m.x94 - m.x128)**2 + (m.x164 - m.x198)**2) + 1 / sqrt((m.x24 - m.x59)
    **2 + (m.x94 - m.x129)**2 + (m.x164 - m.x199)**2) + 1 / sqrt((m.x24 - m.x60)
    **2 + (m.x94 - m.x130)**2 + (m.x164 - m.x200)**2) + 1 / sqrt((m.x24 - m.x61)
    **2 + (m.x94 - m.x131)**2 + (m.x164 - m.x201)**2) + 1 / sqrt((m.x24 - m.x62)
    **2 + (m.x94 - m.x132)**2 + (m.x164 - m.x202)**2) + 1 / sqrt((m.x24 - m.x63)
    **2 + (m.x94 - m.x133)**2 + (m.x164 - m.x203)**2) + 1 / sqrt((m.x24 - m.x64)
    **2 + (m.x94 - m.x134)**2 + (m.x164 - m.x204)**2) + 1 / sqrt((m.x24 - m.x65)
    **2 + (m.x94 - m.x135)**2 + (m.x164 - m.x205)**2) + 1 / sqrt((m.x24 - m.x66)
    **2 + (m.x94 - m.x136)**2 + (m.x164 - m.x206)**2) + 1 / sqrt((m.x24 - m.x67)
    **2 + (m.x94 - m.x137)**2 + (m.x164 - m.x207)**2) + 1 / sqrt((m.x24 - m.x68)
    **2 + (m.x94 - m.x138)**2 + (m.x164 - m.x208)**2) + 1 / sqrt((m.x24 - m.x69)
    **2 + (m.x94 - m.x139)**2 + (m.x164 - m.x209)**2) + 1 / sqrt((m.x24 - m.x70)
    **2 + (m.x94 - m.x140)**2 + (m.x164 - m.x210)**2) + 1 / sqrt((m.x25 - m.x26)
    **2 + (m.x95 - m.x96)**2 + (m.x165 - m.x166)**2) + 1 / sqrt((m.x25 - m.x27)
    **2 + (m.x95 - m.x97)**2 + (m.x165 - m.x167)**2) + 1 / sqrt((m.x25 - m.x28)
    **2 + (m.x95 - m.x98)**2 + (m.x165 - m.x168)**2) + 1 / sqrt((m.x25 - m.x29)
    **2 + (m.x95 - m.x99)**2 + (m.x165 - m.x169)**2) + 1 / sqrt((m.x25 - m.x30)
    **2 + (m.x95 - m.x100)**2 + (m.x165 - m.x170)**2) + 1 / sqrt((m.x25 - m.x31)
    **2 + (m.x95 - m.x101)**2 + (m.x165 - m.x171)**2) + 1 / sqrt((m.x25 - m.x32)
    **2 + (m.x95 - m.x102)**2 + (m.x165 - m.x172)**2) + 1 / sqrt((m.x25 - m.x33)
    **2 + (m.x95 - m.x103)**2 + (m.x165 - m.x173)**2) + 1 / sqrt((m.x25 - m.x34)
    **2 + (m.x95 - m.x104)**2 + (m.x165 - m.x174)**2) + 1 / sqrt((m.x25 - m.x35)
    **2 + (m.x95 - m.x105)**2 + (m.x165 - m.x175)**2) + 1 / sqrt((m.x25 - m.x36)
    **2 + (m.x95 - m.x106)**2 + (m.x165 - m.x176)**2) + 1 / sqrt((m.x25 - m.x37)
    **2 + (m.x95 - m.x107)**2 + (m.x165 - m.x177)**2) + 1 / sqrt((m.x25 - m.x38)
    **2 + (m.x95 - m.x108)**2 + (m.x165 - m.x178)**2) + 1 / sqrt((m.x25 - m.x39)
    **2 + (m.x95 - m.x109)**2 + (m.x165 - m.x179)**2) + 1 / sqrt((m.x25 - m.x40)
    **2 + (m.x95 - m.x110)**2 + (m.x165 - m.x180)**2) + 1 / sqrt((m.x25 - m.x41)
    **2 + (m.x95 - m.x111)**2 + (m.x165 - m.x181)**2) + 1 / sqrt((m.x25 - m.x42)
    **2 + (m.x95 - m.x112)**2 + (m.x165 - m.x182)**2) + 1 / sqrt((m.x25 - m.x43)
    **2 + (m.x95 - m.x113)**2 + (m.x165 - m.x183)**2) + 1 / sqrt((m.x25 - m.x44)
    **2 + (m.x95 - m.x114)**2 + (m.x165 - m.x184)**2) + 1 / sqrt((m.x25 - m.x45)
    **2 + (m.x95 - m.x115)**2 + (m.x165 - m.x185)**2) + 1 / sqrt((m.x25 - m.x46)
    **2 + (m.x95 - m.x116)**2 + (m.x165 - m.x186)**2) + 1 / sqrt((m.x25 - m.x47)
    **2 + (m.x95 - m.x117)**2 + (m.x165 - m.x187)**2) + 1 / sqrt((m.x25 - m.x48)
    **2 + (m.x95 - m.x118)**2 + (m.x165 - m.x188)**2) + 1 / sqrt((m.x25 - m.x49)
    **2 + (m.x95 - m.x119)**2 + (m.x165 - m.x189)**2) + 1 / sqrt((m.x25 - m.x50)
    **2 + (m.x95 - m.x120)**2 + (m.x165 - m.x190)**2) + 1 / sqrt((m.x25 - m.x51)
    **2 + (m.x95 - m.x121)**2 + (m.x165 - m.x191)**2) + 1 / sqrt((m.x25 - m.x52)
    **2 + (m.x95 - m.x122)**2 + (m.x165 - m.x192)**2) + 1 / sqrt((m.x25 - m.x53)
    **2 + (m.x95 - m.x123)**2 + (m.x165 - m.x193)**2) + 1 / sqrt((m.x25 - m.x54)
    **2 + (m.x95 - m.x124)**2 + (m.x165 - m.x194)**2) + 1 / sqrt((m.x25 - m.x55)
    **2 + (m.x95 - m.x125)**2 + (m.x165 - m.x195)**2) + 1 / sqrt((m.x25 - m.x56)
    **2 + (m.x95 - m.x126)**2 + (m.x165 - m.x196)**2) + 1 / sqrt((m.x25 - m.x57)
    **2 + (m.x95 - m.x127)**2 + (m.x165 - m.x197)**2) + 1 / sqrt((m.x25 - m.x58)
    **2 + (m.x95 - m.x128)**2 + (m.x165 - m.x198)**2) + 1 / sqrt((m.x25 - m.x59)
    **2 + (m.x95 - m.x129)**2 + (m.x165 - m.x199)**2) + 1 / sqrt((m.x25 - m.x60)
    **2 + (m.x95 - m.x130)**2 + (m.x165 - m.x200)**2) + 1 / sqrt((m.x25 - m.x61)
    **2 + (m.x95 - m.x131)**2 + (m.x165 - m.x201)**2) + 1 / sqrt((m.x25 - m.x62)
    **2 + (m.x95 - m.x132)**2 + (m.x165 - m.x202)**2) + 1 / sqrt((m.x25 - m.x63)
    **2 + (m.x95 - m.x133)**2 + (m.x165 - m.x203)**2) + 1 / sqrt((m.x25 - m.x64)
    **2 + (m.x95 - m.x134)**2 + (m.x165 - m.x204)**2) + 1 / sqrt((m.x25 - m.x65)
    **2 + (m.x95 - m.x135)**2 + (m.x165 - m.x205)**2) + 1 / sqrt((m.x25 - m.x66)
    **2 + (m.x95 - m.x136)**2 + (m.x165 - m.x206)**2) + 1 / sqrt((m.x25 - m.x67)
    **2 + (m.x95 - m.x137)**2 + (m.x165 - m.x207)**2) + 1 / sqrt((m.x25 - m.x68)
    **2 + (m.x95 - m.x138)**2 + (m.x165 - m.x208)**2) + 1 / sqrt((m.x25 - m.x69)
    **2 + (m.x95 - m.x139)**2 + (m.x165 - m.x209)**2) + 1 / sqrt((m.x25 - m.x70)
    **2 + (m.x95 - m.x140)**2 + (m.x165 - m.x210)**2) + 1 / sqrt((m.x26 - m.x27)
    **2 + (m.x96 - m.x97)**2 + (m.x166 - m.x167)**2) + 1 / sqrt((m.x26 - m.x28)
    **2 + (m.x96 - m.x98)**2 + (m.x166 - m.x168)**2) + 1 / sqrt((m.x26 - m.x29)
    **2 + (m.x96 - m.x99)**2 + (m.x166 - m.x169)**2) + 1 / sqrt((m.x26 - m.x30)
    **2 + (m.x96 - m.x100)**2 + (m.x166 - m.x170)**2) + 1 / sqrt((m.x26 - m.x31)
    **2 + (m.x96 - m.x101)**2 + (m.x166 - m.x171)**2) + 1 / sqrt((m.x26 - m.x32)
    **2 + (m.x96 - m.x102)**2 + (m.x166 - m.x172)**2) + 1 / sqrt((m.x26 - m.x33)
    **2 + (m.x96 - m.x103)**2 + (m.x166 - m.x173)**2) + 1 / sqrt((m.x26 - m.x34)
    **2 + (m.x96 - m.x104)**2 + (m.x166 - m.x174)**2) + 1 / sqrt((m.x26 - m.x35)
    **2 + (m.x96 - m.x105)**2 + (m.x166 - m.x175)**2) + 1 / sqrt((m.x26 - m.x36)
    **2 + (m.x96 - m.x106)**2 + (m.x166 - m.x176)**2) + 1 / sqrt((m.x26 - m.x37)
    **2 + (m.x96 - m.x107)**2 + (m.x166 - m.x177)**2) + 1 / sqrt((m.x26 - m.x38)
    **2 + (m.x96 - m.x108)**2 + (m.x166 - m.x178)**2) + 1 / sqrt((m.x26 - m.x39)
    **2 + (m.x96 - m.x109)**2 + (m.x166 - m.x179)**2) + 1 / sqrt((m.x26 - m.x40)
    **2 + (m.x96 - m.x110)**2 + (m.x166 - m.x180)**2) + 1 / sqrt((m.x26 - m.x41)
    **2 + (m.x96 - m.x111)**2 + (m.x166 - m.x181)**2) + 1 / sqrt((m.x26 - m.x42)
    **2 + (m.x96 - m.x112)**2 + (m.x166 - m.x182)**2) + 1 / sqrt((m.x26 - m.x43)
    **2 + (m.x96 - m.x113)**2 + (m.x166 - m.x183)**2) + 1 / sqrt((m.x26 - m.x44)
    **2 + (m.x96 - m.x114)**2 + (m.x166 - m.x184)**2) + 1 / sqrt((m.x26 - m.x45)
    **2 + (m.x96 - m.x115)**2 + (m.x166 - m.x185)**2) + 1 / sqrt((m.x26 - m.x46)
    **2 + (m.x96 - m.x116)**2 + (m.x166 - m.x186)**2) + 1 / sqrt((m.x26 - m.x47)
    **2 + (m.x96 - m.x117)**2 + (m.x166 - m.x187)**2) + 1 / sqrt((m.x26 - m.x48)
    **2 + (m.x96 - m.x118)**2 + (m.x166 - m.x188)**2) + 1 / sqrt((m.x26 - m.x49)
    **2 + (m.x96 - m.x119)**2 + (m.x166 - m.x189)**2) + 1 / sqrt((m.x26 - m.x50)
    **2 + (m.x96 - m.x120)**2 + (m.x166 - m.x190)**2) + 1 / sqrt((m.x26 - m.x51)
    **2 + (m.x96 - m.x121)**2 + (m.x166 - m.x191)**2) + 1 / sqrt((m.x26 - m.x52)
    **2 + (m.x96 - m.x122)**2 + (m.x166 - m.x192)**2) + 1 / sqrt((m.x26 - m.x53)
    **2 + (m.x96 - m.x123)**2 + (m.x166 - m.x193)**2) + 1 / sqrt((m.x26 - m.x54)
    **2 + (m.x96 - m.x124)**2 + (m.x166 - m.x194)**2) + 1 / sqrt((m.x26 - m.x55)
    **2 + (m.x96 - m.x125)**2 + (m.x166 - m.x195)**2) + 1 / sqrt((m.x26 - m.x56)
    **2 + (m.x96 - m.x126)**2 + (m.x166 - m.x196)**2) + 1 / sqrt((m.x26 - m.x57)
    **2 + (m.x96 - m.x127)**2 + (m.x166 - m.x197)**2) + 1 / sqrt((m.x26 - m.x58)
    **2 + (m.x96 - m.x128)**2 + (m.x166 - m.x198)**2) + 1 / sqrt((m.x26 - m.x59)
    **2 + (m.x96 - m.x129)**2 + (m.x166 - m.x199)**2) + 1 / sqrt((m.x26 - m.x60)
    **2 + (m.x96 - m.x130)**2 + (m.x166 - m.x200)**2) + 1 / sqrt((m.x26 - m.x61)
    **2 + (m.x96 - m.x131)**2 + (m.x166 - m.x201)**2) + 1 / sqrt((m.x26 - m.x62)
    **2 + (m.x96 - m.x132)**2 + (m.x166 - m.x202)**2) + 1 / sqrt((m.x26 - m.x63)
    **2 + (m.x96 - m.x133)**2 + (m.x166 - m.x203)**2) + 1 / sqrt((m.x26 - m.x64)
    **2 + (m.x96 - m.x134)**2 + (m.x166 - m.x204)**2) + 1 / sqrt((m.x26 - m.x65)
    **2 + (m.x96 - m.x135)**2 + (m.x166 - m.x205)**2) + 1 / sqrt((m.x26 - m.x66)
    **2 + (m.x96 - m.x136)**2 + (m.x166 - m.x206)**2) + 1 / sqrt((m.x26 - m.x67)
    **2 + (m.x96 - m.x137)**2 + (m.x166 - m.x207)**2) + 1 / sqrt((m.x26 - m.x68)
    **2 + (m.x96 - m.x138)**2 + (m.x166 - m.x208)**2) + 1 / sqrt((m.x26 - m.x69)
    **2 + (m.x96 - m.x139)**2 + (m.x166 - m.x209)**2) + 1 / sqrt((m.x26 - m.x70)
    **2 + (m.x96 - m.x140)**2 + (m.x166 - m.x210)**2) + 1 / sqrt((m.x27 - m.x28)
    **2 + (m.x97 - m.x98)**2 + (m.x167 - m.x168)**2) + 1 / sqrt((m.x27 - m.x29)
    **2 + (m.x97 - m.x99)**2 + (m.x167 - m.x169)**2) + 1 / sqrt((m.x27 - m.x30)
    **2 + (m.x97 - m.x100)**2 + (m.x167 - m.x170)**2) + 1 / sqrt((m.x27 - m.x31)
    **2 + (m.x97 - m.x101)**2 + (m.x167 - m.x171)**2) + 1 / sqrt((m.x27 - m.x32)
    **2 + (m.x97 - m.x102)**2 + (m.x167 - m.x172)**2) + 1 / sqrt((m.x27 - m.x33)
    **2 + (m.x97 - m.x103)**2 + (m.x167 - m.x173)**2) + 1 / sqrt((m.x27 - m.x34)
    **2 + (m.x97 - m.x104)**2 + (m.x167 - m.x174)**2) + 1 / sqrt((m.x27 - m.x35)
    **2 + (m.x97 - m.x105)**2 + (m.x167 - m.x175)**2) + 1 / sqrt((m.x27 - m.x36)
    **2 + (m.x97 - m.x106)**2 + (m.x167 - m.x176)**2) + 1 / sqrt((m.x27 - m.x37)
    **2 + (m.x97 - m.x107)**2 + (m.x167 - m.x177)**2) + 1 / sqrt((m.x27 - m.x38)
    **2 + (m.x97 - m.x108)**2 + (m.x167 - m.x178)**2) + 1 / sqrt((m.x27 - m.x39)
    **2 + (m.x97 - m.x109)**2 + (m.x167 - m.x179)**2) + 1 / sqrt((m.x27 - m.x40)
    **2 + (m.x97 - m.x110)**2 + (m.x167 - m.x180)**2) + 1 / sqrt((m.x27 - m.x41)
    **2 + (m.x97 - m.x111)**2 + (m.x167 - m.x181)**2) + 1 / sqrt((m.x27 - m.x42)
    **2 + (m.x97 - m.x112)**2 + (m.x167 - m.x182)**2) + 1 / sqrt((m.x27 - m.x43)
    **2 + (m.x97 - m.x113)**2 + (m.x167 - m.x183)**2) + 1 / sqrt((m.x27 - m.x44)
    **2 + (m.x97 - m.x114)**2 + (m.x167 - m.x184)**2) + 1 / sqrt((m.x27 - m.x45)
    **2 + (m.x97 - m.x115)**2 + (m.x167 - m.x185)**2) + 1 / sqrt((m.x27 - m.x46)
    **2 + (m.x97 - m.x116)**2 + (m.x167 - m.x186)**2) + 1 / sqrt((m.x27 - m.x47)
    **2 + (m.x97 - m.x117)**2 + (m.x167 - m.x187)**2) + 1 / sqrt((m.x27 - m.x48)
    **2 + (m.x97 - m.x118)**2 + (m.x167 - m.x188)**2) + 1 / sqrt((m.x27 - m.x49)
    **2 + (m.x97 - m.x119)**2 + (m.x167 - m.x189)**2) + 1 / sqrt((m.x27 - m.x50)
    **2 + (m.x97 - m.x120)**2 + (m.x167 - m.x190)**2) + 1 / sqrt((m.x27 - m.x51)
    **2 + (m.x97 - m.x121)**2 + (m.x167 - m.x191)**2) + 1 / sqrt((m.x27 - m.x52)
    **2 + (m.x97 - m.x122)**2 + (m.x167 - m.x192)**2) + 1 / sqrt((m.x27 - m.x53)
    **2 + (m.x97 - m.x123)**2 + (m.x167 - m.x193)**2) + 1 / sqrt((m.x27 - m.x54)
    **2 + (m.x97 - m.x124)**2 + (m.x167 - m.x194)**2) + 1 / sqrt((m.x27 - m.x55)
    **2 + (m.x97 - m.x125)**2 + (m.x167 - m.x195)**2) + 1 / sqrt((m.x27 - m.x56)
    **2 + (m.x97 - m.x126)**2 + (m.x167 - m.x196)**2) + 1 / sqrt((m.x27 - m.x57)
    **2 + (m.x97 - m.x127)**2 + (m.x167 - m.x197)**2) + 1 / sqrt((m.x27 - m.x58)
    **2 + (m.x97 - m.x128)**2 + (m.x167 - m.x198)**2) + 1 / sqrt((m.x27 - m.x59)
    **2 + (m.x97 - m.x129)**2 + (m.x167 - m.x199)**2) + 1 / sqrt((m.x27 - m.x60)
    **2 + (m.x97 - m.x130)**2 + (m.x167 - m.x200)**2) + 1 / sqrt((m.x27 - m.x61)
    **2 + (m.x97 - m.x131)**2 + (m.x167 - m.x201)**2) + 1 / sqrt((m.x27 - m.x62)
    **2 + (m.x97 - m.x132)**2 + (m.x167 - m.x202)**2) + 1 / sqrt((m.x27 - m.x63)
    **2 + (m.x97 - m.x133)**2 + (m.x167 - m.x203)**2) + 1 / sqrt((m.x27 - m.x64)
    **2 + (m.x97 - m.x134)**2 + (m.x167 - m.x204)**2) + 1 / sqrt((m.x27 - m.x65)
    **2 + (m.x97 - m.x135)**2 + (m.x167 - m.x205)**2) + 1 / sqrt((m.x27 - m.x66)
    **2 + (m.x97 - m.x136)**2 + (m.x167 - m.x206)**2) + 1 / sqrt((m.x27 - m.x67)
    **2 + (m.x97 - m.x137)**2 + (m.x167 - m.x207)**2) + 1 / sqrt((m.x27 - m.x68)
    **2 + (m.x97 - m.x138)**2 + (m.x167 - m.x208)**2) + 1 / sqrt((m.x27 - m.x69)
    **2 + (m.x97 - m.x139)**2 + (m.x167 - m.x209)**2) + 1 / sqrt((m.x27 - m.x70)
    **2 + (m.x97 - m.x140)**2 + (m.x167 - m.x210)**2) + 1 / sqrt((m.x28 - m.x29)
    **2 + (m.x98 - m.x99)**2 + (m.x168 - m.x169)**2) + 1 / sqrt((m.x28 - m.x30)
    **2 + (m.x98 - m.x100)**2 + (m.x168 - m.x170)**2) + 1 / sqrt((m.x28 - m.x31)
    **2 + (m.x98 - m.x101)**2 + (m.x168 - m.x171)**2) + 1 / sqrt((m.x28 - m.x32)
    **2 + (m.x98 - m.x102)**2 + (m.x168 - m.x172)**2) + 1 / sqrt((m.x28 - m.x33)
    **2 + (m.x98 - m.x103)**2 + (m.x168 - m.x173)**2) + 1 / sqrt((m.x28 - m.x34)
    **2 + (m.x98 - m.x104)**2 + (m.x168 - m.x174)**2) + 1 / sqrt((m.x28 - m.x35)
    **2 + (m.x98 - m.x105)**2 + (m.x168 - m.x175)**2) + 1 / sqrt((m.x28 - m.x36)
    **2 + (m.x98 - m.x106)**2 + (m.x168 - m.x176)**2) + 1 / sqrt((m.x28 - m.x37)
    **2 + (m.x98 - m.x107)**2 + (m.x168 - m.x177)**2) + 1 / sqrt((m.x28 - m.x38)
    **2 + (m.x98 - m.x108)**2 + (m.x168 - m.x178)**2) + 1 / sqrt((m.x28 - m.x39)
    **2 + (m.x98 - m.x109)**2 + (m.x168 - m.x179)**2) + 1 / sqrt((m.x28 - m.x40)
    **2 + (m.x98 - m.x110)**2 + (m.x168 - m.x180)**2) + 1 / sqrt((m.x28 - m.x41)
    **2 + (m.x98 - m.x111)**2 + (m.x168 - m.x181)**2) + 1 / sqrt((m.x28 - m.x42)
    **2 + (m.x98 - m.x112)**2 + (m.x168 - m.x182)**2) + 1 / sqrt((m.x28 - m.x43)
    **2 + (m.x98 - m.x113)**2 + (m.x168 - m.x183)**2) + 1 / sqrt((m.x28 - m.x44)
    **2 + (m.x98 - m.x114)**2 + (m.x168 - m.x184)**2) + 1 / sqrt((m.x28 - m.x45)
    **2 + (m.x98 - m.x115)**2 + (m.x168 - m.x185)**2) + 1 / sqrt((m.x28 - m.x46)
    **2 + (m.x98 - m.x116)**2 + (m.x168 - m.x186)**2) + 1 / sqrt((m.x28 - m.x47)
    **2 + (m.x98 - m.x117)**2 + (m.x168 - m.x187)**2) + 1 / sqrt((m.x28 - m.x48)
    **2 + (m.x98 - m.x118)**2 + (m.x168 - m.x188)**2) + 1 / sqrt((m.x28 - m.x49)
    **2 + (m.x98 - m.x119)**2 + (m.x168 - m.x189)**2) + 1 / sqrt((m.x28 - m.x50)
    **2 + (m.x98 - m.x120)**2 + (m.x168 - m.x190)**2) + 1 / sqrt((m.x28 - m.x51)
    **2 + (m.x98 - m.x121)**2 + (m.x168 - m.x191)**2) + 1 / sqrt((m.x28 - m.x52)
    **2 + (m.x98 - m.x122)**2 + (m.x168 - m.x192)**2) + 1 / sqrt((m.x28 - m.x53)
    **2 + (m.x98 - m.x123)**2 + (m.x168 - m.x193)**2) + 1 / sqrt((m.x28 - m.x54)
    **2 + (m.x98 - m.x124)**2 + (m.x168 - m.x194)**2) + 1 / sqrt((m.x28 - m.x55)
    **2 + (m.x98 - m.x125)**2 + (m.x168 - m.x195)**2) + 1 / sqrt((m.x28 - m.x56)
    **2 + (m.x98 - m.x126)**2 + (m.x168 - m.x196)**2) + 1 / sqrt((m.x28 - m.x57)
    **2 + (m.x98 - m.x127)**2 + (m.x168 - m.x197)**2) + 1 / sqrt((m.x28 - m.x58)
    **2 + (m.x98 - m.x128)**2 + (m.x168 - m.x198)**2) + 1 / sqrt((m.x28 - m.x59)
    **2 + (m.x98 - m.x129)**2 + (m.x168 - m.x199)**2) + 1 / sqrt((m.x28 - m.x60)
    **2 + (m.x98 - m.x130)**2 + (m.x168 - m.x200)**2) + 1 / sqrt((m.x28 - m.x61)
    **2 + (m.x98 - m.x131)**2 + (m.x168 - m.x201)**2) + 1 / sqrt((m.x28 - m.x62)
    **2 + (m.x98 - m.x132)**2 + (m.x168 - m.x202)**2) + 1 / sqrt((m.x28 - m.x63)
    **2 + (m.x98 - m.x133)**2 + (m.x168 - m.x203)**2) + 1 / sqrt((m.x28 - m.x64)
    **2 + (m.x98 - m.x134)**2 + (m.x168 - m.x204)**2) + 1 / sqrt((m.x28 - m.x65)
    **2 + (m.x98 - m.x135)**2 + (m.x168 - m.x205)**2) + 1 / sqrt((m.x28 - m.x66)
    **2 + (m.x98 - m.x136)**2 + (m.x168 - m.x206)**2) + 1 / sqrt((m.x28 - m.x67)
    **2 + (m.x98 - m.x137)**2 + (m.x168 - m.x207)**2) + 1 / sqrt((m.x28 - m.x68)
    **2 + (m.x98 - m.x138)**2 + (m.x168 - m.x208)**2) + 1 / sqrt((m.x28 - m.x69)
    **2 + (m.x98 - m.x139)**2 + (m.x168 - m.x209)**2) + 1 / sqrt((m.x28 - m.x70)
    **2 + (m.x98 - m.x140)**2 + (m.x168 - m.x210)**2) + 1 / sqrt((m.x29 - m.x30)
    **2 + (m.x99 - m.x100)**2 + (m.x169 - m.x170)**2) + 1 / sqrt((m.x29 - m.x31)
    **2 + (m.x99 - m.x101)**2 + (m.x169 - m.x171)**2) + 1 / sqrt((m.x29 - m.x32)
    **2 + (m.x99 - m.x102)**2 + (m.x169 - m.x172)**2) + 1 / sqrt((m.x29 - m.x33)
    **2 + (m.x99 - m.x103)**2 + (m.x169 - m.x173)**2) + 1 / sqrt((m.x29 - m.x34)
    **2 + (m.x99 - m.x104)**2 + (m.x169 - m.x174)**2) + 1 / sqrt((m.x29 - m.x35)
    **2 + (m.x99 - m.x105)**2 + (m.x169 - m.x175)**2) + 1 / sqrt((m.x29 - m.x36)
    **2 + (m.x99 - m.x106)**2 + (m.x169 - m.x176)**2) + 1 / sqrt((m.x29 - m.x37)
    **2 + (m.x99 - m.x107)**2 + (m.x169 - m.x177)**2) + 1 / sqrt((m.x29 - m.x38)
    **2 + (m.x99 - m.x108)**2 + (m.x169 - m.x178)**2) + 1 / sqrt((m.x29 - m.x39)
    **2 + (m.x99 - m.x109)**2 + (m.x169 - m.x179)**2) + 1 / sqrt((m.x29 - m.x40)
    **2 + (m.x99 - m.x110)**2 + (m.x169 - m.x180)**2) + 1 / sqrt((m.x29 - m.x41)
    **2 + (m.x99 - m.x111)**2 + (m.x169 - m.x181)**2) + 1 / sqrt((m.x29 - m.x42)
    **2 + (m.x99 - m.x112)**2 + (m.x169 - m.x182)**2) + 1 / sqrt((m.x29 - m.x43)
    **2 + (m.x99 - m.x113)**2 + (m.x169 - m.x183)**2) + 1 / sqrt((m.x29 - m.x44)
    **2 + (m.x99 - m.x114)**2 + (m.x169 - m.x184)**2) + 1 / sqrt((m.x29 - m.x45)
    **2 + (m.x99 - m.x115)**2 + (m.x169 - m.x185)**2) + 1 / sqrt((m.x29 - m.x46)
    **2 + (m.x99 - m.x116)**2 + (m.x169 - m.x186)**2) + 1 / sqrt((m.x29 - m.x47)
    **2 + (m.x99 - m.x117)**2 + (m.x169 - m.x187)**2) + 1 / sqrt((m.x29 - m.x48)
    **2 + (m.x99 - m.x118)**2 + (m.x169 - m.x188)**2) + 1 / sqrt((m.x29 - m.x49)
    **2 + (m.x99 - m.x119)**2 + (m.x169 - m.x189)**2) + 1 / sqrt((m.x29 - m.x50)
    **2 + (m.x99 - m.x120)**2 + (m.x169 - m.x190)**2) + 1 / sqrt((m.x29 - m.x51)
    **2 + (m.x99 - m.x121)**2 + (m.x169 - m.x191)**2) + 1 / sqrt((m.x29 - m.x52)
    **2 + (m.x99 - m.x122)**2 + (m.x169 - m.x192)**2) + 1 / sqrt((m.x29 - m.x53)
    **2 + (m.x99 - m.x123)**2 + (m.x169 - m.x193)**2) + 1 / sqrt((m.x29 - m.x54)
    **2 + (m.x99 - m.x124)**2 + (m.x169 - m.x194)**2) + 1 / sqrt((m.x29 - m.x55)
    **2 + (m.x99 - m.x125)**2 + (m.x169 - m.x195)**2) + 1 / sqrt((m.x29 - m.x56)
    **2 + (m.x99 - m.x126)**2 + (m.x169 - m.x196)**2) + 1 / sqrt((m.x29 - m.x57)
    **2 + (m.x99 - m.x127)**2 + (m.x169 - m.x197)**2) + 1 / sqrt((m.x29 - m.x58)
    **2 + (m.x99 - m.x128)**2 + (m.x169 - m.x198)**2) + 1 / sqrt((m.x29 - m.x59)
    **2 + (m.x99 - m.x129)**2 + (m.x169 - m.x199)**2) + 1 / sqrt((m.x29 - m.x60)
    **2 + (m.x99 - m.x130)**2 + (m.x169 - m.x200)**2) + 1 / sqrt((m.x29 - m.x61)
    **2 + (m.x99 - m.x131)**2 + (m.x169 - m.x201)**2) + 1 / sqrt((m.x29 - m.x62)
    **2 + (m.x99 - m.x132)**2 + (m.x169 - m.x202)**2) + 1 / sqrt((m.x29 - m.x63)
    **2 + (m.x99 - m.x133)**2 + (m.x169 - m.x203)**2) + 1 / sqrt((m.x29 - m.x64)
    **2 + (m.x99 - m.x134)**2 + (m.x169 - m.x204)**2) + 1 / sqrt((m.x29 - m.x65)
    **2 + (m.x99 - m.x135)**2 + (m.x169 - m.x205)**2) + 1 / sqrt((m.x29 - m.x66)
    **2 + (m.x99 - m.x136)**2 + (m.x169 - m.x206)**2) + 1 / sqrt((m.x29 - m.x67)
    **2 + (m.x99 - m.x137)**2 + (m.x169 - m.x207)**2) + 1 / sqrt((m.x29 - m.x68)
    **2 + (m.x99 - m.x138)**2 + (m.x169 - m.x208)**2) + 1 / sqrt((m.x29 - m.x69)
    **2 + (m.x99 - m.x139)**2 + (m.x169 - m.x209)**2) + 1 / sqrt((m.x29 - m.x70)
    **2 + (m.x99 - m.x140)**2 + (m.x169 - m.x210)**2) + 1 / sqrt((m.x30 - m.x31)
    **2 + (m.x100 - m.x101)**2 + (m.x170 - m.x171)**2) + 1 / sqrt((m.x30 -
    m.x32)**2 + (m.x100 - m.x102)**2 + (m.x170 - m.x172)**2) + 1 / sqrt((m.x30
    - m.x33)**2 + (m.x100 - m.x103)**2 + (m.x170 - m.x173)**2) + 1 / sqrt((
    m.x30 - m.x34)**2 + (m.x100 - m.x104)**2 + (m.x170 - m.x174)**2) + 1 /
    sqrt((m.x30 - m.x35)**2 + (m.x100 - m.x105)**2 + (m.x170 - m.x175)**2) + 1
    / sqrt((m.x30 - m.x36)**2 + (m.x100 - m.x106)**2 + (m.x170 - m.x176)**2)
    + 1 / sqrt((m.x30 - m.x37)**2 + (m.x100 - m.x107)**2 + (m.x170 - m.x177)**
    2) + 1 / sqrt((m.x30 - m.x38)**2 + (m.x100 - m.x108)**2 + (m.x170 - m.x178)
    **2) + 1 / sqrt((m.x30 - m.x39)**2 + (m.x100 - m.x109)**2 + (m.x170 -
    m.x179)**2) + 1 / sqrt((m.x30 - m.x40)**2 + (m.x100 - m.x110)**2 + (m.x170
    - m.x180)**2) + 1 / sqrt((m.x30 - m.x41)**2 + (m.x100 - m.x111)**2 + (
    m.x170 - m.x181)**2) + 1 / sqrt((m.x30 - m.x42)**2 + (m.x100 - m.x112)**2
    + (m.x170 - m.x182)**2) + 1 / sqrt((m.x30 - m.x43)**2 + (m.x100 - m.x113)
    **2 + (m.x170 - m.x183)**2) + 1 / sqrt((m.x30 - m.x44)**2 + (m.x100 -
    m.x114)**2 + (m.x170 - m.x184)**2) + 1 / sqrt((m.x30 - m.x45)**2 + (m.x100
    - m.x115)**2 + (m.x170 - m.x185)**2) + 1 / sqrt((m.x30 - m.x46)**2 + (
    m.x100 - m.x116)**2 + (m.x170 - m.x186)**2) + 1 / sqrt((m.x30 - m.x47)**2
    + (m.x100 - m.x117)**2 + (m.x170 - m.x187)**2) + 1 / sqrt((m.x30 - m.x48)
    **2 + (m.x100 - m.x118)**2 + (m.x170 - m.x188)**2) + 1 / sqrt((m.x30 -
    m.x49)**2 + (m.x100 - m.x119)**2 + (m.x170 - m.x189)**2) + 1 / sqrt((m.x30
    - m.x50)**2 + (m.x100 - m.x120)**2 + (m.x170 - m.x190)**2) + 1 / sqrt((
    m.x30 - m.x51)**2 + (m.x100 - m.x121)**2 + (m.x170 - m.x191)**2) + 1 /
    sqrt((m.x30 - m.x52)**2 + (m.x100 - m.x122)**2 + (m.x170 - m.x192)**2) + 1
    / sqrt((m.x30 - m.x53)**2 + (m.x100 - m.x123)**2 + (m.x170 - m.x193)**2)
    + 1 / sqrt((m.x30 - m.x54)**2 + (m.x100 - m.x124)**2 + (m.x170 - m.x194)**
    2) + 1 / sqrt((m.x30 - m.x55)**2 + (m.x100 - m.x125)**2 + (m.x170 - m.x195)
    **2) + 1 / sqrt((m.x30 - m.x56)**2 + (m.x100 - m.x126)**2 + (m.x170 -
    m.x196)**2) + 1 / sqrt((m.x30 - m.x57)**2 + (m.x100 - m.x127)**2 + (m.x170
    - m.x197)**2) + 1 / sqrt((m.x30 - m.x58)**2 + (m.x100 - m.x128)**2 + (
    m.x170 - m.x198)**2) + 1 / sqrt((m.x30 - m.x59)**2 + (m.x100 - m.x129)**2
    + (m.x170 - m.x199)**2) + 1 / sqrt((m.x30 - m.x60)**2 + (m.x100 - m.x130)
    **2 + (m.x170 - m.x200)**2) + 1 / sqrt((m.x30 - m.x61)**2 + (m.x100 -
    m.x131)**2 + (m.x170 - m.x201)**2) + 1 / sqrt((m.x30 - m.x62)**2 + (m.x100
    - m.x132)**2 + (m.x170 - m.x202)**2) + 1 / sqrt((m.x30 - m.x63)**2 + (
    m.x100 - m.x133)**2 + (m.x170 - m.x203)**2) + 1 / sqrt((m.x30 - m.x64)**2
    + (m.x100 - m.x134)**2 + (m.x170 - m.x204)**2) + 1 / sqrt((m.x30 - m.x65)
    **2 + (m.x100 - m.x135)**2 + (m.x170 - m.x205)**2) + 1 / sqrt((m.x30 -
    m.x66)**2 + (m.x100 - m.x136)**2 + (m.x170 - m.x206)**2) + 1 / sqrt((m.x30
    - m.x67)**2 + (m.x100 - m.x137)**2 + (m.x170 - m.x207)**2) + 1 / sqrt((
    m.x30 - m.x68)**2 + (m.x100 - m.x138)**2 + (m.x170 - m.x208)**2) + 1 /
    sqrt((m.x30 - m.x69)**2 + (m.x100 - m.x139)**2 + (m.x170 - m.x209)**2) + 1
    / sqrt((m.x30 - m.x70)**2 + (m.x100 - m.x140)**2 + (m.x170 - m.x210)**2)
    + 1 / sqrt((m.x31 - m.x32)**2 + (m.x101 - m.x102)**2 + (m.x171 - m.x172)**
    2) + 1 / sqrt((m.x31 - m.x33)**2 + (m.x101 - m.x103)**2 + (m.x171 - m.x173)
    **2) + 1 / sqrt((m.x31 - m.x34)**2 + (m.x101 - m.x104)**2 + (m.x171 -
    m.x174)**2) + 1 / sqrt((m.x31 - m.x35)**2 + (m.x101 - m.x105)**2 + (m.x171
    - m.x175)**2) + 1 / sqrt((m.x31 - m.x36)**2 + (m.x101 - m.x106)**2 + (
    m.x171 - m.x176)**2) + 1 / sqrt((m.x31 - m.x37)**2 + (m.x101 - m.x107)**2
    + (m.x171 - m.x177)**2) + 1 / sqrt((m.x31 - m.x38)**2 + (m.x101 - m.x108)
    **2 + (m.x171 - m.x178)**2) + 1 / sqrt((m.x31 - m.x39)**2 + (m.x101 -
    m.x109)**2 + (m.x171 - m.x179)**2) + 1 / sqrt((m.x31 - m.x40)**2 + (m.x101
    - m.x110)**2 + (m.x171 - m.x180)**2) + 1 / sqrt((m.x31 - m.x41)**2 + (
    m.x101 - m.x111)**2 + (m.x171 - m.x181)**2) + 1 / sqrt((m.x31 - m.x42)**2
    + (m.x101 - m.x112)**2 + (m.x171 - m.x182)**2) + 1 / sqrt((m.x31 - m.x43)
    **2 + (m.x101 - m.x113)**2 + (m.x171 - m.x183)**2) + 1 / sqrt((m.x31 -
    m.x44)**2 + (m.x101 - m.x114)**2 + (m.x171 - m.x184)**2) + 1 / sqrt((m.x31
    - m.x45)**2 + (m.x101 - m.x115)**2 + (m.x171 - m.x185)**2) + 1 / sqrt((
    m.x31 - m.x46)**2 + (m.x101 - m.x116)**2 + (m.x171 - m.x186)**2) + 1 /
    sqrt((m.x31 - m.x47)**2 + (m.x101 - m.x117)**2 + (m.x171 - m.x187)**2) + 1
    / sqrt((m.x31 - m.x48)**2 + (m.x101 - m.x118)**2 + (m.x171 - m.x188)**2)
    + 1 / sqrt((m.x31 - m.x49)**2 + (m.x101 - m.x119)**2 + (m.x171 - m.x189)**
    2) + 1 / sqrt((m.x31 - m.x50)**2 + (m.x101 - m.x120)**2 + (m.x171 - m.x190)
    **2) + 1 / sqrt((m.x31 - m.x51)**2 + (m.x101 - m.x121)**2 + (m.x171 -
    m.x191)**2) + 1 / sqrt((m.x31 - m.x52)**2 + (m.x101 - m.x122)**2 + (m.x171
    - m.x192)**2) + 1 / sqrt((m.x31 - m.x53)**2 + (m.x101 - m.x123)**2 + (
    m.x171 - m.x193)**2) + 1 / sqrt((m.x31 - m.x54)**2 + (m.x101 - m.x124)**2
    + (m.x171 - m.x194)**2) + 1 / sqrt((m.x31 - m.x55)**2 + (m.x101 - m.x125)
    **2 + (m.x171 - m.x195)**2) + 1 / sqrt((m.x31 - m.x56)**2 + (m.x101 -
    m.x126)**2 + (m.x171 - m.x196)**2) + 1 / sqrt((m.x31 - m.x57)**2 + (m.x101
    - m.x127)**2 + (m.x171 - m.x197)**2) + 1 / sqrt((m.x31 - m.x58)**2 + (
    m.x101 - m.x128)**2 + (m.x171 - m.x198)**2) + 1 / sqrt((m.x31 - m.x59)**2
    + (m.x101 - m.x129)**2 + (m.x171 - m.x199)**2) + 1 / sqrt((m.x31 - m.x60)
    **2 + (m.x101 - m.x130)**2 + (m.x171 - m.x200)**2) + 1 / sqrt((m.x31 -
    m.x61)**2 + (m.x101 - m.x131)**2 + (m.x171 - m.x201)**2) + 1 / sqrt((m.x31
    - m.x62)**2 + (m.x101 - m.x132)**2 + (m.x171 - m.x202)**2) + 1 / sqrt((
    m.x31 - m.x63)**2 + (m.x101 - m.x133)**2 + (m.x171 - m.x203)**2) + 1 /
    sqrt((m.x31 - m.x64)**2 + (m.x101 - m.x134)**2 + (m.x171 - m.x204)**2) + 1
    / sqrt((m.x31 - m.x65)**2 + (m.x101 - m.x135)**2 + (m.x171 - m.x205)**2)
    + 1 / sqrt((m.x31 - m.x66)**2 + (m.x101 - m.x136)**2 + (m.x171 - m.x206)**
    2) + 1 / sqrt((m.x31 - m.x67)**2 + (m.x101 - m.x137)**2 + (m.x171 - m.x207)
    **2) + 1 / sqrt((m.x31 - m.x68)**2 + (m.x101 - m.x138)**2 + (m.x171 -
    m.x208)**2) + 1 / sqrt((m.x31 - m.x69)**2 + (m.x101 - m.x139)**2 + (m.x171
    - m.x209)**2) + 1 / sqrt((m.x31 - m.x70)**2 + (m.x101 - m.x140)**2 + (
    m.x171 - m.x210)**2) + 1 / sqrt((m.x32 - m.x33)**2 + (m.x102 - m.x103)**2
    + (m.x172 - m.x173)**2) + 1 / sqrt((m.x32 - m.x34)**2 + (m.x102 - m.x104)
    **2 + (m.x172 - m.x174)**2) + 1 / sqrt((m.x32 - m.x35)**2 + (m.x102 -
    m.x105)**2 + (m.x172 - m.x175)**2) + 1 / sqrt((m.x32 - m.x36)**2 + (m.x102
    - m.x106)**2 + (m.x172 - m.x176)**2) + 1 / sqrt((m.x32 - m.x37)**2 + (
    m.x102 - m.x107)**2 + (m.x172 - m.x177)**2) + 1 / sqrt((m.x32 - m.x38)**2
    + (m.x102 - m.x108)**2 + (m.x172 - m.x178)**2) + 1 / sqrt((m.x32 - m.x39)
    **2 + (m.x102 - m.x109)**2 + (m.x172 - m.x179)**2) + 1 / sqrt((m.x32 -
    m.x40)**2 + (m.x102 - m.x110)**2 + (m.x172 - m.x180)**2) + 1 / sqrt((m.x32
    - m.x41)**2 + (m.x102 - m.x111)**2 + (m.x172 - m.x181)**2) + 1 / sqrt((
    m.x32 - m.x42)**2 + (m.x102 - m.x112)**2 + (m.x172 - m.x182)**2) + 1 /
    sqrt((m.x32 - m.x43)**2 + (m.x102 - m.x113)**2 + (m.x172 - m.x183)**2) + 1
    / sqrt((m.x32 - m.x44)**2 + (m.x102 - m.x114)**2 + (m.x172 - m.x184)**2)
    + 1 / sqrt((m.x32 - m.x45)**2 + (m.x102 - m.x115)**2 + (m.x172 - m.x185)**
    2) + 1 / sqrt((m.x32 - m.x46)**2 + (m.x102 - m.x116)**2 + (m.x172 - m.x186)
    **2) + 1 / sqrt((m.x32 - m.x47)**2 + (m.x102 - m.x117)**2 + (m.x172 -
    m.x187)**2) + 1 / sqrt((m.x32 - m.x48)**2 + (m.x102 - m.x118)**2 + (m.x172
    - m.x188)**2) + 1 / sqrt((m.x32 - m.x49)**2 + (m.x102 - m.x119)**2 + (
    m.x172 - m.x189)**2) + 1 / sqrt((m.x32 - m.x50)**2 + (m.x102 - m.x120)**2
    + (m.x172 - m.x190)**2) + 1 / sqrt((m.x32 - m.x51)**2 + (m.x102 - m.x121)
    **2 + (m.x172 - m.x191)**2) + 1 / sqrt((m.x32 - m.x52)**2 + (m.x102 -
    m.x122)**2 + (m.x172 - m.x192)**2) + 1 / sqrt((m.x32 - m.x53)**2 + (m.x102
    - m.x123)**2 + (m.x172 - m.x193)**2) + 1 / sqrt((m.x32 - m.x54)**2 + (
    m.x102 - m.x124)**2 + (m.x172 - m.x194)**2) + 1 / sqrt((m.x32 - m.x55)**2
    + (m.x102 - m.x125)**2 + (m.x172 - m.x195)**2) + 1 / sqrt((m.x32 - m.x56)
    **2 + (m.x102 - m.x126)**2 + (m.x172 - m.x196)**2) + 1 / sqrt((m.x32 -
    m.x57)**2 + (m.x102 - m.x127)**2 + (m.x172 - m.x197)**2) + 1 / sqrt((m.x32
    - m.x58)**2 + (m.x102 - m.x128)**2 + (m.x172 - m.x198)**2) + 1 / sqrt((
    m.x32 - m.x59)**2 + (m.x102 - m.x129)**2 + (m.x172 - m.x199)**2) + 1 /
    sqrt((m.x32 - m.x60)**2 + (m.x102 - m.x130)**2 + (m.x172 - m.x200)**2) + 1
    / sqrt((m.x32 - m.x61)**2 + (m.x102 - m.x131)**2 + (m.x172 - m.x201)**2)
    + 1 / sqrt((m.x32 - m.x62)**2 + (m.x102 - m.x132)**2 + (m.x172 - m.x202)**
    2) + 1 / sqrt((m.x32 - m.x63)**2 + (m.x102 - m.x133)**2 + (m.x172 - m.x203)
    **2) + 1 / sqrt((m.x32 - m.x64)**2 + (m.x102 - m.x134)**2 + (m.x172 -
    m.x204)**2) + 1 / sqrt((m.x32 - m.x65)**2 + (m.x102 - m.x135)**2 + (m.x172
    - m.x205)**2) + 1 / sqrt((m.x32 - m.x66)**2 + (m.x102 - m.x136)**2 + (
    m.x172 - m.x206)**2) + 1 / sqrt((m.x32 - m.x67)**2 + (m.x102 - m.x137)**2
    + (m.x172 - m.x207)**2) + 1 / sqrt((m.x32 - m.x68)**2 + (m.x102 - m.x138)
    **2 + (m.x172 - m.x208)**2) + 1 / sqrt((m.x32 - m.x69)**2 + (m.x102 -
    m.x139)**2 + (m.x172 - m.x209)**2) + 1 / sqrt((m.x32 - m.x70)**2 + (m.x102
    - m.x140)**2 + (m.x172 - m.x210)**2) + 1 / sqrt((m.x33 - m.x34)**2 + (
    m.x103 - m.x104)**2 + (m.x173 - m.x174)**2) + 1 / sqrt((m.x33 - m.x35)**2
    + (m.x103 - m.x105)**2 + (m.x173 - m.x175)**2) + 1 / sqrt((m.x33 - m.x36)
    **2 + (m.x103 - m.x106)**2 + (m.x173 - m.x176)**2) + 1 / sqrt((m.x33 -
    m.x37)**2 + (m.x103 - m.x107)**2 + (m.x173 - m.x177)**2) + 1 / sqrt((m.x33
    - m.x38)**2 + (m.x103 - m.x108)**2 + (m.x173 - m.x178)**2) + 1 / sqrt((
    m.x33 - m.x39)**2 + (m.x103 - m.x109)**2 + (m.x173 - m.x179)**2) + 1 /
    sqrt((m.x33 - m.x40)**2 + (m.x103 - m.x110)**2 + (m.x173 - m.x180)**2) + 1
    / sqrt((m.x33 - m.x41)**2 + (m.x103 - m.x111)**2 + (m.x173 - m.x181)**2)
    + 1 / sqrt((m.x33 - m.x42)**2 + (m.x103 - m.x112)**2 + (m.x173 - m.x182)**
    2) + 1 / sqrt((m.x33 - m.x43)**2 + (m.x103 - m.x113)**2 + (m.x173 - m.x183)
    **2) + 1 / sqrt((m.x33 - m.x44)**2 + (m.x103 - m.x114)**2 + (m.x173 -
    m.x184)**2) + 1 / sqrt((m.x33 - m.x45)**2 + (m.x103 - m.x115)**2 + (m.x173
    - m.x185)**2) + 1 / sqrt((m.x33 - m.x46)**2 + (m.x103 - m.x116)**2 + (
    m.x173 - m.x186)**2) + 1 / sqrt((m.x33 - m.x47)**2 + (m.x103 - m.x117)**2
    + (m.x173 - m.x187)**2) + 1 / sqrt((m.x33 - m.x48)**2 + (m.x103 - m.x118)
    **2 + (m.x173 - m.x188)**2) + 1 / sqrt((m.x33 - m.x49)**2 + (m.x103 -
    m.x119)**2 + (m.x173 - m.x189)**2) + 1 / sqrt((m.x33 - m.x50)**2 + (m.x103
    - m.x120)**2 + (m.x173 - m.x190)**2) + 1 / sqrt((m.x33 - m.x51)**2 + (
    m.x103 - m.x121)**2 + (m.x173 - m.x191)**2) + 1 / sqrt((m.x33 - m.x52)**2
    + (m.x103 - m.x122)**2 + (m.x173 - m.x192)**2) + 1 / sqrt((m.x33 - m.x53)
    **2 + (m.x103 - m.x123)**2 + (m.x173 - m.x193)**2) + 1 / sqrt((m.x33 -
    m.x54)**2 + (m.x103 - m.x124)**2 + (m.x173 - m.x194)**2) + 1 / sqrt((m.x33
    - m.x55)**2 + (m.x103 - m.x125)**2 + (m.x173 - m.x195)**2) + 1 / sqrt((
    m.x33 - m.x56)**2 + (m.x103 - m.x126)**2 + (m.x173 - m.x196)**2) + 1 /
    sqrt((m.x33 - m.x57)**2 + (m.x103 - m.x127)**2 + (m.x173 - m.x197)**2) + 1
    / sqrt((m.x33 - m.x58)**2 + (m.x103 - m.x128)**2 + (m.x173 - m.x198)**2)
    + 1 / sqrt((m.x33 - m.x59)**2 + (m.x103 - m.x129)**2 + (m.x173 - m.x199)**
    2) + 1 / sqrt((m.x33 - m.x60)**2 + (m.x103 - m.x130)**2 + (m.x173 - m.x200)
    **2) + 1 / sqrt((m.x33 - m.x61)**2 + (m.x103 - m.x131)**2 + (m.x173 -
    m.x201)**2) + 1 / sqrt((m.x33 - m.x62)**2 + (m.x103 - m.x132)**2 + (m.x173
    - m.x202)**2) + 1 / sqrt((m.x33 - m.x63)**2 + (m.x103 - m.x133)**2 + (
    m.x173 - m.x203)**2) + 1 / sqrt((m.x33 - m.x64)**2 + (m.x103 - m.x134)**2
    + (m.x173 - m.x204)**2) + 1 / sqrt((m.x33 - m.x65)**2 + (m.x103 - m.x135)
    **2 + (m.x173 - m.x205)**2) + 1 / sqrt((m.x33 - m.x66)**2 + (m.x103 -
    m.x136)**2 + (m.x173 - m.x206)**2) + 1 / sqrt((m.x33 - m.x67)**2 + (m.x103
    - m.x137)**2 + (m.x173 - m.x207)**2) + 1 / sqrt((m.x33 - m.x68)**2 + (
    m.x103 - m.x138)**2 + (m.x173 - m.x208)**2) + 1 / sqrt((m.x33 - m.x69)**2
    + (m.x103 - m.x139)**2 + (m.x173 - m.x209)**2) + 1 / sqrt((m.x33 - m.x70)
    **2 + (m.x103 - m.x140)**2 + (m.x173 - m.x210)**2) + 1 / sqrt((m.x34 -
    m.x35)**2 + (m.x104 - m.x105)**2 + (m.x174 - m.x175)**2) + 1 / sqrt((m.x34
    - m.x36)**2 + (m.x104 - m.x106)**2 + (m.x174 - m.x176)**2) + 1 / sqrt((
    m.x34 - m.x37)**2 + (m.x104 - m.x107)**2 + (m.x174 - m.x177)**2) + 1 /
    sqrt((m.x34 - m.x38)**2 + (m.x104 - m.x108)**2 + (m.x174 - m.x178)**2) + 1
    / sqrt((m.x34 - m.x39)**2 + (m.x104 - m.x109)**2 + (m.x174 - m.x179)**2)
    + 1 / sqrt((m.x34 - m.x40)**2 + (m.x104 - m.x110)**2 + (m.x174 - m.x180)**
    2) + 1 / sqrt((m.x34 - m.x41)**2 + (m.x104 - m.x111)**2 + (m.x174 - m.x181)
    **2) + 1 / sqrt((m.x34 - m.x42)**2 + (m.x104 - m.x112)**2 + (m.x174 -
    m.x182)**2) + 1 / sqrt((m.x34 - m.x43)**2 + (m.x104 - m.x113)**2 + (m.x174
    - m.x183)**2) + 1 / sqrt((m.x34 - m.x44)**2 + (m.x104 - m.x114)**2 + (
    m.x174 - m.x184)**2) + 1 / sqrt((m.x34 - m.x45)**2 + (m.x104 - m.x115)**2
    + (m.x174 - m.x185)**2) + 1 / sqrt((m.x34 - m.x46)**2 + (m.x104 - m.x116)
    **2 + (m.x174 - m.x186)**2) + 1 / sqrt((m.x34 - m.x47)**2 + (m.x104 -
    m.x117)**2 + (m.x174 - m.x187)**2) + 1 / sqrt((m.x34 - m.x48)**2 + (m.x104
    - m.x118)**2 + (m.x174 - m.x188)**2) + 1 / sqrt((m.x34 - m.x49)**2 + (
    m.x104 - m.x119)**2 + (m.x174 - m.x189)**2) + 1 / sqrt((m.x34 - m.x50)**2
    + (m.x104 - m.x120)**2 + (m.x174 - m.x190)**2) + 1 / sqrt((m.x34 - m.x51)
    **2 + (m.x104 - m.x121)**2 + (m.x174 - m.x191)**2) + 1 / sqrt((m.x34 -
    m.x52)**2 + (m.x104 - m.x122)**2 + (m.x174 - m.x192)**2) + 1 / sqrt((m.x34
    - m.x53)**2 + (m.x104 - m.x123)**2 + (m.x174 - m.x193)**2) + 1 / sqrt((
    m.x34 - m.x54)**2 + (m.x104 - m.x124)**2 + (m.x174 - m.x194)**2) + 1 /
    sqrt((m.x34 - m.x55)**2 + (m.x104 - m.x125)**2 + (m.x174 - m.x195)**2) + 1
    / sqrt((m.x34 - m.x56)**2 + (m.x104 - m.x126)**2 + (m.x174 - m.x196)**2)
    + 1 / sqrt((m.x34 - m.x57)**2 + (m.x104 - m.x127)**2 + (m.x174 - m.x197)**
    2) + 1 / sqrt((m.x34 - m.x58)**2 + (m.x104 - m.x128)**2 + (m.x174 - m.x198)
    **2) + 1 / sqrt((m.x34 - m.x59)**2 + (m.x104 - m.x129)**2 + (m.x174 -
    m.x199)**2) + 1 / sqrt((m.x34 - m.x60)**2 + (m.x104 - m.x130)**2 + (m.x174
    - m.x200)**2) + 1 / sqrt((m.x34 - m.x61)**2 + (m.x104 - m.x131)**2 + (
    m.x174 - m.x201)**2) + 1 / sqrt((m.x34 - m.x62)**2 + (m.x104 - m.x132)**2
    + (m.x174 - m.x202)**2) + 1 / sqrt((m.x34 - m.x63)**2 + (m.x104 - m.x133)
    **2 + (m.x174 - m.x203)**2) + 1 / sqrt((m.x34 - m.x64)**2 + (m.x104 -
    m.x134)**2 + (m.x174 - m.x204)**2) + 1 / sqrt((m.x34 - m.x65)**2 + (m.x104
    - m.x135)**2 + (m.x174 - m.x205)**2) + 1 / sqrt((m.x34 - m.x66)**2 + (
    m.x104 - m.x136)**2 + (m.x174 - m.x206)**2) + 1 / sqrt((m.x34 - m.x67)**2
    + (m.x104 - m.x137)**2 + (m.x174 - m.x207)**2) + 1 / sqrt((m.x34 - m.x68)
    **2 + (m.x104 - m.x138)**2 + (m.x174 - m.x208)**2) + 1 / sqrt((m.x34 -
    m.x69)**2 + (m.x104 - m.x139)**2 + (m.x174 - m.x209)**2) + 1 / sqrt((m.x34
    - m.x70)**2 + (m.x104 - m.x140)**2 + (m.x174 - m.x210)**2) + 1 / sqrt((
    m.x35 - m.x36)**2 + (m.x105 - m.x106)**2 + (m.x175 - m.x176)**2) + 1 /
    sqrt((m.x35 - m.x37)**2 + (m.x105 - m.x107)**2 + (m.x175 - m.x177)**2) + 1
    / sqrt((m.x35 - m.x38)**2 + (m.x105 - m.x108)**2 + (m.x175 - m.x178)**2)
    + 1 / sqrt((m.x35 - m.x39)**2 + (m.x105 - m.x109)**2 + (m.x175 - m.x179)**
    2) + 1 / sqrt((m.x35 - m.x40)**2 + (m.x105 - m.x110)**2 + (m.x175 - m.x180)
    **2) + 1 / sqrt((m.x35 - m.x41)**2 + (m.x105 - m.x111)**2 + (m.x175 -
    m.x181)**2) + 1 / sqrt((m.x35 - m.x42)**2 + (m.x105 - m.x112)**2 + (m.x175
    - m.x182)**2) + 1 / sqrt((m.x35 - m.x43)**2 + (m.x105 - m.x113)**2 + (
    m.x175 - m.x183)**2) + 1 / sqrt((m.x35 - m.x44)**2 + (m.x105 - m.x114)**2
    + (m.x175 - m.x184)**2) + 1 / sqrt((m.x35 - m.x45)**2 + (m.x105 - m.x115)
    **2 + (m.x175 - m.x185)**2) + 1 / sqrt((m.x35 - m.x46)**2 + (m.x105 -
    m.x116)**2 + (m.x175 - m.x186)**2) + 1 / sqrt((m.x35 - m.x47)**2 + (m.x105
    - m.x117)**2 + (m.x175 - m.x187)**2) + 1 / sqrt((m.x35 - m.x48)**2 + (
    m.x105 - m.x118)**2 + (m.x175 - m.x188)**2) + 1 / sqrt((m.x35 - m.x49)**2
    + (m.x105 - m.x119)**2 + (m.x175 - m.x189)**2) + 1 / sqrt((m.x35 - m.x50)
    **2 + (m.x105 - m.x120)**2 + (m.x175 - m.x190)**2) + 1 / sqrt((m.x35 -
    m.x51)**2 + (m.x105 - m.x121)**2 + (m.x175 - m.x191)**2) + 1 / sqrt((m.x35
    - m.x52)**2 + (m.x105 - m.x122)**2 + (m.x175 - m.x192)**2) + 1 / sqrt((
    m.x35 - m.x53)**2 + (m.x105 - m.x123)**2 + (m.x175 - m.x193)**2) + 1 /
    sqrt((m.x35 - m.x54)**2 + (m.x105 - m.x124)**2 + (m.x175 - m.x194)**2) + 1
    / sqrt((m.x35 - m.x55)**2 + (m.x105 - m.x125)**2 + (m.x175 - m.x195)**2)
    + 1 / sqrt((m.x35 - m.x56)**2 + (m.x105 - m.x126)**2 + (m.x175 - m.x196)**
    2) + 1 / sqrt((m.x35 - m.x57)**2 + (m.x105 - m.x127)**2 + (m.x175 - m.x197)
    **2) + 1 / sqrt((m.x35 - m.x58)**2 + (m.x105 - m.x128)**2 + (m.x175 -
    m.x198)**2) + 1 / sqrt((m.x35 - m.x59)**2 + (m.x105 - m.x129)**2 + (m.x175
    - m.x199)**2) + 1 / sqrt((m.x35 - m.x60)**2 + (m.x105 - m.x130)**2 + (
    m.x175 - m.x200)**2) + 1 / sqrt((m.x35 - m.x61)**2 + (m.x105 - m.x131)**2
    + (m.x175 - m.x201)**2) + 1 / sqrt((m.x35 - m.x62)**2 + (m.x105 - m.x132)
    **2 + (m.x175 - m.x202)**2) + 1 / sqrt((m.x35 - m.x63)**2 + (m.x105 -
    m.x133)**2 + (m.x175 - m.x203)**2) + 1 / sqrt((m.x35 - m.x64)**2 + (m.x105
    - m.x134)**2 + (m.x175 - m.x204)**2) + 1 / sqrt((m.x35 - m.x65)**2 + (
    m.x105 - m.x135)**2 + (m.x175 - m.x205)**2) + 1 / sqrt((m.x35 - m.x66)**2
    + (m.x105 - m.x136)**2 + (m.x175 - m.x206)**2) + 1 / sqrt((m.x35 - m.x67)
    **2 + (m.x105 - m.x137)**2 + (m.x175 - m.x207)**2) + 1 / sqrt((m.x35 -
    m.x68)**2 + (m.x105 - m.x138)**2 + (m.x175 - m.x208)**2) + 1 / sqrt((m.x35
    - m.x69)**2 + (m.x105 - m.x139)**2 + (m.x175 - m.x209)**2) + 1 / sqrt((
    m.x35 - m.x70)**2 + (m.x105 - m.x140)**2 + (m.x175 - m.x210)**2) + 1 /
    sqrt((m.x36 - m.x37)**2 + (m.x106 - m.x107)**2 + (m.x176 - m.x177)**2) + 1
    / sqrt((m.x36 - m.x38)**2 + (m.x106 - m.x108)**2 + (m.x176 - m.x178)**2)
    + 1 / sqrt((m.x36 - m.x39)**2 + (m.x106 - m.x109)**2 + (m.x176 - m.x179)**
    2) + 1 / sqrt((m.x36 - m.x40)**2 + (m.x106 - m.x110)**2 + (m.x176 - m.x180)
    **2) + 1 / sqrt((m.x36 - m.x41)**2 + (m.x106 - m.x111)**2 + (m.x176 -
    m.x181)**2) + 1 / sqrt((m.x36 - m.x42)**2 + (m.x106 - m.x112)**2 + (m.x176
    - m.x182)**2) + 1 / sqrt((m.x36 - m.x43)**2 + (m.x106 - m.x113)**2 + (
    m.x176 - m.x183)**2) + 1 / sqrt((m.x36 - m.x44)**2 + (m.x106 - m.x114)**2
    + (m.x176 - m.x184)**2) + 1 / sqrt((m.x36 - m.x45)**2 + (m.x106 - m.x115)
    **2 + (m.x176 - m.x185)**2) + 1 / sqrt((m.x36 - m.x46)**2 + (m.x106 -
    m.x116)**2 + (m.x176 - m.x186)**2) + 1 / sqrt((m.x36 - m.x47)**2 + (m.x106
    - m.x117)**2 + (m.x176 - m.x187)**2) + 1 / sqrt((m.x36 - m.x48)**2 + (
    m.x106 - m.x118)**2 + (m.x176 - m.x188)**2) + 1 / sqrt((m.x36 - m.x49)**2
    + (m.x106 - m.x119)**2 + (m.x176 - m.x189)**2) + 1 / sqrt((m.x36 - m.x50)
    **2 + (m.x106 - m.x120)**2 + (m.x176 - m.x190)**2) + 1 / sqrt((m.x36 -
    m.x51)**2 + (m.x106 - m.x121)**2 + (m.x176 - m.x191)**2) + 1 / sqrt((m.x36
    - m.x52)**2 + (m.x106 - m.x122)**2 + (m.x176 - m.x192)**2) + 1 / sqrt((
    m.x36 - m.x53)**2 + (m.x106 - m.x123)**2 + (m.x176 - m.x193)**2) + 1 /
    sqrt((m.x36 - m.x54)**2 + (m.x106 - m.x124)**2 + (m.x176 - m.x194)**2) + 1
    / sqrt((m.x36 - m.x55)**2 + (m.x106 - m.x125)**2 + (m.x176 - m.x195)**2)
    + 1 / sqrt((m.x36 - m.x56)**2 + (m.x106 - m.x126)**2 + (m.x176 - m.x196)**
    2) + 1 / sqrt((m.x36 - m.x57)**2 + (m.x106 - m.x127)**2 + (m.x176 - m.x197)
    **2) + 1 / sqrt((m.x36 - m.x58)**2 + (m.x106 - m.x128)**2 + (m.x176 -
    m.x198)**2) + 1 / sqrt((m.x36 - m.x59)**2 + (m.x106 - m.x129)**2 + (m.x176
    - m.x199)**2) + 1 / sqrt((m.x36 - m.x60)**2 + (m.x106 - m.x130)**2 + (
    m.x176 - m.x200)**2) + 1 / sqrt((m.x36 - m.x61)**2 + (m.x106 - m.x131)**2
    + (m.x176 - m.x201)**2) + 1 / sqrt((m.x36 - m.x62)**2 + (m.x106 - m.x132)
    **2 + (m.x176 - m.x202)**2) + 1 / sqrt((m.x36 - m.x63)**2 + (m.x106 -
    m.x133)**2 + (m.x176 - m.x203)**2) + 1 / sqrt((m.x36 - m.x64)**2 + (m.x106
    - m.x134)**2 + (m.x176 - m.x204)**2) + 1 / sqrt((m.x36 - m.x65)**2 + (
    m.x106 - m.x135)**2 + (m.x176 - m.x205)**2) + 1 / sqrt((m.x36 - m.x66)**2
    + (m.x106 - m.x136)**2 + (m.x176 - m.x206)**2) + 1 / sqrt((m.x36 - m.x67)
    **2 + (m.x106 - m.x137)**2 + (m.x176 - m.x207)**2) + 1 / sqrt((m.x36 -
    m.x68)**2 + (m.x106 - m.x138)**2 + (m.x176 - m.x208)**2) + 1 / sqrt((m.x36
    - m.x69)**2 + (m.x106 - m.x139)**2 + (m.x176 - m.x209)**2) + 1 / sqrt((
    m.x36 - m.x70)**2 + (m.x106 - m.x140)**2 + (m.x176 - m.x210)**2) + 1 /
    sqrt((m.x37 - m.x38)**2 + (m.x107 - m.x108)**2 + (m.x177 - m.x178)**2) + 1
    / sqrt((m.x37 - m.x39)**2 + (m.x107 - m.x109)**2 + (m.x177 - m.x179)**2)
    + 1 / sqrt((m.x37 - m.x40)**2 + (m.x107 - m.x110)**2 + (m.x177 - m.x180)**
    2) + 1 / sqrt((m.x37 - m.x41)**2 + (m.x107 - m.x111)**2 + (m.x177 - m.x181)
    **2) + 1 / sqrt((m.x37 - m.x42)**2 + (m.x107 - m.x112)**2 + (m.x177 -
    m.x182)**2) + 1 / sqrt((m.x37 - m.x43)**2 + (m.x107 - m.x113)**2 + (m.x177
    - m.x183)**2) + 1 / sqrt((m.x37 - m.x44)**2 + (m.x107 - m.x114)**2 + (
    m.x177 - m.x184)**2) + 1 / sqrt((m.x37 - m.x45)**2 + (m.x107 - m.x115)**2
    + (m.x177 - m.x185)**2) + 1 / sqrt((m.x37 - m.x46)**2 + (m.x107 - m.x116)
    **2 + (m.x177 - m.x186)**2) + 1 / sqrt((m.x37 - m.x47)**2 + (m.x107 -
    m.x117)**2 + (m.x177 - m.x187)**2) + 1 / sqrt((m.x37 - m.x48)**2 + (m.x107
    - m.x118)**2 + (m.x177 - m.x188)**2) + 1 / sqrt((m.x37 - m.x49)**2 + (
    m.x107 - m.x119)**2 + (m.x177 - m.x189)**2) + 1 / sqrt((m.x37 - m.x50)**2
    + (m.x107 - m.x120)**2 + (m.x177 - m.x190)**2) + 1 / sqrt((m.x37 - m.x51)
    **2 + (m.x107 - m.x121)**2 + (m.x177 - m.x191)**2) + 1 / sqrt((m.x37 -
    m.x52)**2 + (m.x107 - m.x122)**2 + (m.x177 - m.x192)**2) + 1 / sqrt((m.x37
    - m.x53)**2 + (m.x107 - m.x123)**2 + (m.x177 - m.x193)**2) + 1 / sqrt((
    m.x37 - m.x54)**2 + (m.x107 - m.x124)**2 + (m.x177 - m.x194)**2) + 1 /
    sqrt((m.x37 - m.x55)**2 + (m.x107 - m.x125)**2 + (m.x177 - m.x195)**2) + 1
    / sqrt((m.x37 - m.x56)**2 + (m.x107 - m.x126)**2 + (m.x177 - m.x196)**2)
    + 1 / sqrt((m.x37 - m.x57)**2 + (m.x107 - m.x127)**2 + (m.x177 - m.x197)**
    2) + 1 / sqrt((m.x37 - m.x58)**2 + (m.x107 - m.x128)**2 + (m.x177 - m.x198)
    **2) + 1 / sqrt((m.x37 - m.x59)**2 + (m.x107 - m.x129)**2 + (m.x177 -
    m.x199)**2) + 1 / sqrt((m.x37 - m.x60)**2 + (m.x107 - m.x130)**2 + (m.x177
    - m.x200)**2) + 1 / sqrt((m.x37 - m.x61)**2 + (m.x107 - m.x131)**2 + (
    m.x177 - m.x201)**2) + 1 / sqrt((m.x37 - m.x62)**2 + (m.x107 - m.x132)**2
    + (m.x177 - m.x202)**2) + 1 / sqrt((m.x37 - m.x63)**2 + (m.x107 - m.x133)
    **2 + (m.x177 - m.x203)**2) + 1 / sqrt((m.x37 - m.x64)**2 + (m.x107 -
    m.x134)**2 + (m.x177 - m.x204)**2) + 1 / sqrt((m.x37 - m.x65)**2 + (m.x107
    - m.x135)**2 + (m.x177 - m.x205)**2) + 1 / sqrt((m.x37 - m.x66)**2 + (
    m.x107 - m.x136)**2 + (m.x177 - m.x206)**2) + 1 / sqrt((m.x37 - m.x67)**2
    + (m.x107 - m.x137)**2 + (m.x177 - m.x207)**2) + 1 / sqrt((m.x37 - m.x68)
    **2 + (m.x107 - m.x138)**2 + (m.x177 - m.x208)**2) + 1 / sqrt((m.x37 -
    m.x69)**2 + (m.x107 - m.x139)**2 + (m.x177 - m.x209)**2) + 1 / sqrt((m.x37
    - m.x70)**2 + (m.x107 - m.x140)**2 + (m.x177 - m.x210)**2) + 1 / sqrt((
    m.x38 - m.x39)**2 + (m.x108 - m.x109)**2 + (m.x178 - m.x179)**2) + 1 /
    sqrt((m.x38 - m.x40)**2 + (m.x108 - m.x110)**2 + (m.x178 - m.x180)**2) + 1
    / sqrt((m.x38 - m.x41)**2 + (m.x108 - m.x111)**2 + (m.x178 - m.x181)**2)
    + 1 / sqrt((m.x38 - m.x42)**2 + (m.x108 - m.x112)**2 + (m.x178 - m.x182)**
    2) + 1 / sqrt((m.x38 - m.x43)**2 + (m.x108 - m.x113)**2 + (m.x178 - m.x183)
    **2) + 1 / sqrt((m.x38 - m.x44)**2 + (m.x108 - m.x114)**2 + (m.x178 -
    m.x184)**2) + 1 / sqrt((m.x38 - m.x45)**2 + (m.x108 - m.x115)**2 + (m.x178
    - m.x185)**2) + 1 / sqrt((m.x38 - m.x46)**2 + (m.x108 - m.x116)**2 + (
    m.x178 - m.x186)**2) + 1 / sqrt((m.x38 - m.x47)**2 + (m.x108 - m.x117)**2
    + (m.x178 - m.x187)**2) + 1 / sqrt((m.x38 - m.x48)**2 + (m.x108 - m.x118)
    **2 + (m.x178 - m.x188)**2) + 1 / sqrt((m.x38 - m.x49)**2 + (m.x108 -
    m.x119)**2 + (m.x178 - m.x189)**2) + 1 / sqrt((m.x38 - m.x50)**2 + (m.x108
    - m.x120)**2 + (m.x178 - m.x190)**2) + 1 / sqrt((m.x38 - m.x51)**2 + (
    m.x108 - m.x121)**2 + (m.x178 - m.x191)**2) + 1 / sqrt((m.x38 - m.x52)**2
    + (m.x108 - m.x122)**2 + (m.x178 - m.x192)**2) + 1 / sqrt((m.x38 - m.x53)
    **2 + (m.x108 - m.x123)**2 + (m.x178 - m.x193)**2) + 1 / sqrt((m.x38 -
    m.x54)**2 + (m.x108 - m.x124)**2 + (m.x178 - m.x194)**2) + 1 / sqrt((m.x38
    - m.x55)**2 + (m.x108 - m.x125)**2 + (m.x178 - m.x195)**2) + 1 / sqrt((
    m.x38 - m.x56)**2 + (m.x108 - m.x126)**2 + (m.x178 - m.x196)**2) + 1 /
    sqrt((m.x38 - m.x57)**2 + (m.x108 - m.x127)**2 + (m.x178 - m.x197)**2) + 1
    / sqrt((m.x38 - m.x58)**2 + (m.x108 - m.x128)**2 + (m.x178 - m.x198)**2)
    + 1 / sqrt((m.x38 - m.x59)**2 + (m.x108 - m.x129)**2 + (m.x178 - m.x199)**
    2) + 1 / sqrt((m.x38 - m.x60)**2 + (m.x108 - m.x130)**2 + (m.x178 - m.x200)
    **2) + 1 / sqrt((m.x38 - m.x61)**2 + (m.x108 - m.x131)**2 + (m.x178 -
    m.x201)**2) + 1 / sqrt((m.x38 - m.x62)**2 + (m.x108 - m.x132)**2 + (m.x178
    - m.x202)**2) + 1 / sqrt((m.x38 - m.x63)**2 + (m.x108 - m.x133)**2 + (
    m.x178 - m.x203)**2) + 1 / sqrt((m.x38 - m.x64)**2 + (m.x108 - m.x134)**2
    + (m.x178 - m.x204)**2) + 1 / sqrt((m.x38 - m.x65)**2 + (m.x108 - m.x135)
    **2 + (m.x178 - m.x205)**2) + 1 / sqrt((m.x38 - m.x66)**2 + (m.x108 -
    m.x136)**2 + (m.x178 - m.x206)**2) + 1 / sqrt((m.x38 - m.x67)**2 + (m.x108
    - m.x137)**2 + (m.x178 - m.x207)**2) + 1 / sqrt((m.x38 - m.x68)**2 + (
    m.x108 - m.x138)**2 + (m.x178 - m.x208)**2) + 1 / sqrt((m.x38 - m.x69)**2
    + (m.x108 - m.x139)**2 + (m.x178 - m.x209)**2) + 1 / sqrt((m.x38 - m.x70)
    **2 + (m.x108 - m.x140)**2 + (m.x178 - m.x210)**2) + 1 / sqrt((m.x39 -
    m.x40)**2 + (m.x109 - m.x110)**2 + (m.x179 - m.x180)**2) + 1 / sqrt((m.x39
    - m.x41)**2 + (m.x109 - m.x111)**2 + (m.x179 - m.x181)**2) + 1 / sqrt((
    m.x39 - m.x42)**2 + (m.x109 - m.x112)**2 + (m.x179 - m.x182)**2) + 1 /
    sqrt((m.x39 - m.x43)**2 + (m.x109 - m.x113)**2 + (m.x179 - m.x183)**2) + 1
    / sqrt((m.x39 - m.x44)**2 + (m.x109 - m.x114)**2 + (m.x179 - m.x184)**2)
    + 1 / sqrt((m.x39 - m.x45)**2 + (m.x109 - m.x115)**2 + (m.x179 - m.x185)**
    2) + 1 / sqrt((m.x39 - m.x46)**2 + (m.x109 - m.x116)**2 + (m.x179 - m.x186)
    **2) + 1 / sqrt((m.x39 - m.x47)**2 + (m.x109 - m.x117)**2 + (m.x179 -
    m.x187)**2) + 1 / sqrt((m.x39 - m.x48)**2 + (m.x109 - m.x118)**2 + (m.x179
    - m.x188)**2) + 1 / sqrt((m.x39 - m.x49)**2 + (m.x109 - m.x119)**2 + (
    m.x179 - m.x189)**2) + 1 / sqrt((m.x39 - m.x50)**2 + (m.x109 - m.x120)**2
    + (m.x179 - m.x190)**2) + 1 / sqrt((m.x39 - m.x51)**2 + (m.x109 - m.x121)
    **2 + (m.x179 - m.x191)**2) + 1 / sqrt((m.x39 - m.x52)**2 + (m.x109 -
    m.x122)**2 + (m.x179 - m.x192)**2) + 1 / sqrt((m.x39 - m.x53)**2 + (m.x109
    - m.x123)**2 + (m.x179 - m.x193)**2) + 1 / sqrt((m.x39 - m.x54)**2 + (
    m.x109 - m.x124)**2 + (m.x179 - m.x194)**2) + 1 / sqrt((m.x39 - m.x55)**2
    + (m.x109 - m.x125)**2 + (m.x179 - m.x195)**2) + 1 / sqrt((m.x39 - m.x56)
    **2 + (m.x109 - m.x126)**2 + (m.x179 - m.x196)**2) + 1 / sqrt((m.x39 -
    m.x57)**2 + (m.x109 - m.x127)**2 + (m.x179 - m.x197)**2) + 1 / sqrt((m.x39
    - m.x58)**2 + (m.x109 - m.x128)**2 + (m.x179 - m.x198)**2) + 1 / sqrt((
    m.x39 - m.x59)**2 + (m.x109 - m.x129)**2 + (m.x179 - m.x199)**2) + 1 /
    sqrt((m.x39 - m.x60)**2 + (m.x109 - m.x130)**2 + (m.x179 - m.x200)**2) + 1
    / sqrt((m.x39 - m.x61)**2 + (m.x109 - m.x131)**2 + (m.x179 - m.x201)**2)
    + 1 / sqrt((m.x39 - m.x62)**2 + (m.x109 - m.x132)**2 + (m.x179 - m.x202)**
    2) + 1 / sqrt((m.x39 - m.x63)**2 + (m.x109 - m.x133)**2 + (m.x179 - m.x203)
    **2) + 1 / sqrt((m.x39 - m.x64)**2 + (m.x109 - m.x134)**2 + (m.x179 -
    m.x204)**2) + 1 / sqrt((m.x39 - m.x65)**2 + (m.x109 - m.x135)**2 + (m.x179
    - m.x205)**2) + 1 / sqrt((m.x39 - m.x66)**2 + (m.x109 - m.x136)**2 + (
    m.x179 - m.x206)**2) + 1 / sqrt((m.x39 - m.x67)**2 + (m.x109 - m.x137)**2
    + (m.x179 - m.x207)**2) + 1 / sqrt((m.x39 - m.x68)**2 + (m.x109 - m.x138)
    **2 + (m.x179 - m.x208)**2) + 1 / sqrt((m.x39 - m.x69)**2 + (m.x109 -
    m.x139)**2 + (m.x179 - m.x209)**2) + 1 / sqrt((m.x39 - m.x70)**2 + (m.x109
    - m.x140)**2 + (m.x179 - m.x210)**2) + 1 / sqrt((m.x40 - m.x41)**2 + (
    m.x110 - m.x111)**2 + (m.x180 - m.x181)**2) + 1 / sqrt((m.x40 - m.x42)**2
    + (m.x110 - m.x112)**2 + (m.x180 - m.x182)**2) + 1 / sqrt((m.x40 - m.x43)
    **2 + (m.x110 - m.x113)**2 + (m.x180 - m.x183)**2) + 1 / sqrt((m.x40 -
    m.x44)**2 + (m.x110 - m.x114)**2 + (m.x180 - m.x184)**2) + 1 / sqrt((m.x40
    - m.x45)**2 + (m.x110 - m.x115)**2 + (m.x180 - m.x185)**2) + 1 / sqrt((
    m.x40 - m.x46)**2 + (m.x110 - m.x116)**2 + (m.x180 - m.x186)**2) + 1 /
    sqrt((m.x40 - m.x47)**2 + (m.x110 - m.x117)**2 + (m.x180 - m.x187)**2) + 1
    / sqrt((m.x40 - m.x48)**2 + (m.x110 - m.x118)**2 + (m.x180 - m.x188)**2)
    + 1 / sqrt((m.x40 - m.x49)**2 + (m.x110 - m.x119)**2 + (m.x180 - m.x189)**
    2) + 1 / sqrt((m.x40 - m.x50)**2 + (m.x110 - m.x120)**2 + (m.x180 - m.x190)
    **2) + 1 / sqrt((m.x40 - m.x51)**2 + (m.x110 - m.x121)**2 + (m.x180 -
    m.x191)**2) + 1 / sqrt((m.x40 - m.x52)**2 + (m.x110 - m.x122)**2 + (m.x180
    - m.x192)**2) + 1 / sqrt((m.x40 - m.x53)**2 + (m.x110 - m.x123)**2 + (
    m.x180 - m.x193)**2) + 1 / sqrt((m.x40 - m.x54)**2 + (m.x110 - m.x124)**2
    + (m.x180 - m.x194)**2) + 1 / sqrt((m.x40 - m.x55)**2 + (m.x110 - m.x125)
    **2 + (m.x180 - m.x195)**2) + 1 / sqrt((m.x40 - m.x56)**2 + (m.x110 -
    m.x126)**2 + (m.x180 - m.x196)**2) + 1 / sqrt((m.x40 - m.x57)**2 + (m.x110
    - m.x127)**2 + (m.x180 - m.x197)**2) + 1 / sqrt((m.x40 - m.x58)**2 + (
    m.x110 - m.x128)**2 + (m.x180 - m.x198)**2) + 1 / sqrt((m.x40 - m.x59)**2
    + (m.x110 - m.x129)**2 + (m.x180 - m.x199)**2) + 1 / sqrt((m.x40 - m.x60)
    **2 + (m.x110 - m.x130)**2 + (m.x180 - m.x200)**2) + 1 / sqrt((m.x40 -
    m.x61)**2 + (m.x110 - m.x131)**2 + (m.x180 - m.x201)**2) + 1 / sqrt((m.x40
    - m.x62)**2 + (m.x110 - m.x132)**2 + (m.x180 - m.x202)**2) + 1 / sqrt((
    m.x40 - m.x63)**2 + (m.x110 - m.x133)**2 + (m.x180 - m.x203)**2) + 1 /
    sqrt((m.x40 - m.x64)**2 + (m.x110 - m.x134)**2 + (m.x180 - m.x204)**2) + 1
    / sqrt((m.x40 - m.x65)**2 + (m.x110 - m.x135)**2 + (m.x180 - m.x205)**2)
    + 1 / sqrt((m.x40 - m.x66)**2 + (m.x110 - m.x136)**2 + (m.x180 - m.x206)**
    2) + 1 / sqrt((m.x40 - m.x67)**2 + (m.x110 - m.x137)**2 + (m.x180 - m.x207)
    **2) + 1 / sqrt((m.x40 - m.x68)**2 + (m.x110 - m.x138)**2 + (m.x180 -
    m.x208)**2) + 1 / sqrt((m.x40 - m.x69)**2 + (m.x110 - m.x139)**2 + (m.x180
    - m.x209)**2) + 1 / sqrt((m.x40 - m.x70)**2 + (m.x110 - m.x140)**2 + (
    m.x180 - m.x210)**2) + 1 / sqrt((m.x41 - m.x42)**2 + (m.x111 - m.x112)**2
    + (m.x181 - m.x182)**2) + 1 / sqrt((m.x41 - m.x43)**2 + (m.x111 - m.x113)
    **2 + (m.x181 - m.x183)**2) + 1 / sqrt((m.x41 - m.x44)**2 + (m.x111 -
    m.x114)**2 + (m.x181 - m.x184)**2) + 1 / sqrt((m.x41 - m.x45)**2 + (m.x111
    - m.x115)**2 + (m.x181 - m.x185)**2) + 1 / sqrt((m.x41 - m.x46)**2 + (
    m.x111 - m.x116)**2 + (m.x181 - m.x186)**2) + 1 / sqrt((m.x41 - m.x47)**2
    + (m.x111 - m.x117)**2 + (m.x181 - m.x187)**2) + 1 / sqrt((m.x41 - m.x48)
    **2 + (m.x111 - m.x118)**2 + (m.x181 - m.x188)**2) + 1 / sqrt((m.x41 -
    m.x49)**2 + (m.x111 - m.x119)**2 + (m.x181 - m.x189)**2) + 1 / sqrt((m.x41
    - m.x50)**2 + (m.x111 - m.x120)**2 + (m.x181 - m.x190)**2) + 1 / sqrt((
    m.x41 - m.x51)**2 + (m.x111 - m.x121)**2 + (m.x181 - m.x191)**2) + 1 /
    sqrt((m.x41 - m.x52)**2 + (m.x111 - m.x122)**2 + (m.x181 - m.x192)**2) + 1
    / sqrt((m.x41 - m.x53)**2 + (m.x111 - m.x123)**2 + (m.x181 - m.x193)**2)
    + 1 / sqrt((m.x41 - m.x54)**2 + (m.x111 - m.x124)**2 + (m.x181 - m.x194)**
    2) + 1 / sqrt((m.x41 - m.x55)**2 + (m.x111 - m.x125)**2 + (m.x181 - m.x195)
    **2) + 1 / sqrt((m.x41 - m.x56)**2 + (m.x111 - m.x126)**2 + (m.x181 -
    m.x196)**2) + 1 / sqrt((m.x41 - m.x57)**2 + (m.x111 - m.x127)**2 + (m.x181
    - m.x197)**2) + 1 / sqrt((m.x41 - m.x58)**2 + (m.x111 - m.x128)**2 + (
    m.x181 - m.x198)**2) + 1 / sqrt((m.x41 - m.x59)**2 + (m.x111 - m.x129)**2
    + (m.x181 - m.x199)**2) + 1 / sqrt((m.x41 - m.x60)**2 + (m.x111 - m.x130)
    **2 + (m.x181 - m.x200)**2) + 1 / sqrt((m.x41 - m.x61)**2 + (m.x111 -
    m.x131)**2 + (m.x181 - m.x201)**2) + 1 / sqrt((m.x41 - m.x62)**2 + (m.x111
    - m.x132)**2 + (m.x181 - m.x202)**2) + 1 / sqrt((m.x41 - m.x63)**2 + (
    m.x111 - m.x133)**2 + (m.x181 - m.x203)**2) + 1 / sqrt((m.x41 - m.x64)**2
    + (m.x111 - m.x134)**2 + (m.x181 - m.x204)**2) + 1 / sqrt((m.x41 - m.x65)
    **2 + (m.x111 - m.x135)**2 + (m.x181 - m.x205)**2) + 1 / sqrt((m.x41 -
    m.x66)**2 + (m.x111 - m.x136)**2 + (m.x181 - m.x206)**2) + 1 / sqrt((m.x41
    - m.x67)**2 + (m.x111 - m.x137)**2 + (m.x181 - m.x207)**2) + 1 / sqrt((
    m.x41 - m.x68)**2 + (m.x111 - m.x138)**2 + (m.x181 - m.x208)**2) + 1 /
    sqrt((m.x41 - m.x69)**2 + (m.x111 - m.x139)**2 + (m.x181 - m.x209)**2) + 1
    / sqrt((m.x41 - m.x70)**2 + (m.x111 - m.x140)**2 + (m.x181 - m.x210)**2)
    + 1 / sqrt((m.x42 - m.x43)**2 + (m.x112 - m.x113)**2 + (m.x182 - m.x183)**
    2) + 1 / sqrt((m.x42 - m.x44)**2 + (m.x112 - m.x114)**2 + (m.x182 - m.x184)
    **2) + 1 / sqrt((m.x42 - m.x45)**2 + (m.x112 - m.x115)**2 + (m.x182 -
    m.x185)**2) + 1 / sqrt((m.x42 - m.x46)**2 + (m.x112 - m.x116)**2 + (m.x182
    - m.x186)**2) + 1 / sqrt((m.x42 - m.x47)**2 + (m.x112 - m.x117)**2 + (
    m.x182 - m.x187)**2) + 1 / sqrt((m.x42 - m.x48)**2 + (m.x112 - m.x118)**2
    + (m.x182 - m.x188)**2) + 1 / sqrt((m.x42 - m.x49)**2 + (m.x112 - m.x119)
    **2 + (m.x182 - m.x189)**2) + 1 / sqrt((m.x42 - m.x50)**2 + (m.x112 -
    m.x120)**2 + (m.x182 - m.x190)**2) + 1 / sqrt((m.x42 - m.x51)**2 + (m.x112
    - m.x121)**2 + (m.x182 - m.x191)**2) + 1 / sqrt((m.x42 - m.x52)**2 + (
    m.x112 - m.x122)**2 + (m.x182 - m.x192)**2) + 1 / sqrt((m.x42 - m.x53)**2
    + (m.x112 - m.x123)**2 + (m.x182 - m.x193)**2) + 1 / sqrt((m.x42 - m.x54)
    **2 + (m.x112 - m.x124)**2 + (m.x182 - m.x194)**2) + 1 / sqrt((m.x42 -
    m.x55)**2 + (m.x112 - m.x125)**2 + (m.x182 - m.x195)**2) + 1 / sqrt((m.x42
    - m.x56)**2 + (m.x112 - m.x126)**2 + (m.x182 - m.x196)**2) + 1 / sqrt((
    m.x42 - m.x57)**2 + (m.x112 - m.x127)**2 + (m.x182 - m.x197)**2) + 1 /
    sqrt((m.x42 - m.x58)**2 + (m.x112 - m.x128)**2 + (m.x182 - m.x198)**2) + 1
    / sqrt((m.x42 - m.x59)**2 + (m.x112 - m.x129)**2 + (m.x182 - m.x199)**2)
    + 1 / sqrt((m.x42 - m.x60)**2 + (m.x112 - m.x130)**2 + (m.x182 - m.x200)**
    2) + 1 / sqrt((m.x42 - m.x61)**2 + (m.x112 - m.x131)**2 + (m.x182 - m.x201)
    **2) + 1 / sqrt((m.x42 - m.x62)**2 + (m.x112 - m.x132)**2 + (m.x182 -
    m.x202)**2) + 1 / sqrt((m.x42 - m.x63)**2 + (m.x112 - m.x133)**2 + (m.x182
    - m.x203)**2) + 1 / sqrt((m.x42 - m.x64)**2 + (m.x112 - m.x134)**2 + (
    m.x182 - m.x204)**2) + 1 / sqrt((m.x42 - m.x65)**2 + (m.x112 - m.x135)**2
    + (m.x182 - m.x205)**2) + 1 / sqrt((m.x42 - m.x66)**2 + (m.x112 - m.x136)
    **2 + (m.x182 - m.x206)**2) + 1 / sqrt((m.x42 - m.x67)**2 + (m.x112 -
    m.x137)**2 + (m.x182 - m.x207)**2) + 1 / sqrt((m.x42 - m.x68)**2 + (m.x112
    - m.x138)**2 + (m.x182 - m.x208)**2) + 1 / sqrt((m.x42 - m.x69)**2 + (
    m.x112 - m.x139)**2 + (m.x182 - m.x209)**2) + 1 / sqrt((m.x42 - m.x70)**2
    + (m.x112 - m.x140)**2 + (m.x182 - m.x210)**2) + 1 / sqrt((m.x43 - m.x44)
    **2 + (m.x113 - m.x114)**2 + (m.x183 - m.x184)**2) + 1 / sqrt((m.x43 -
    m.x45)**2 + (m.x113 - m.x115)**2 + (m.x183 - m.x185)**2) + 1 / sqrt((m.x43
    - m.x46)**2 + (m.x113 - m.x116)**2 + (m.x183 - m.x186)**2) + 1 / sqrt((
    m.x43 - m.x47)**2 + (m.x113 - m.x117)**2 + (m.x183 - m.x187)**2) + 1 /
    sqrt((m.x43 - m.x48)**2 + (m.x113 - m.x118)**2 + (m.x183 - m.x188)**2) + 1
    / sqrt((m.x43 - m.x49)**2 + (m.x113 - m.x119)**2 + (m.x183 - m.x189)**2)
    + 1 / sqrt((m.x43 - m.x50)**2 + (m.x113 - m.x120)**2 + (m.x183 - m.x190)**
    2) + 1 / sqrt((m.x43 - m.x51)**2 + (m.x113 - m.x121)**2 + (m.x183 - m.x191)
    **2) + 1 / sqrt((m.x43 - m.x52)**2 + (m.x113 - m.x122)**2 + (m.x183 -
    m.x192)**2) + 1 / sqrt((m.x43 - m.x53)**2 + (m.x113 - m.x123)**2 + (m.x183
    - m.x193)**2) + 1 / sqrt((m.x43 - m.x54)**2 + (m.x113 - m.x124)**2 + (
    m.x183 - m.x194)**2) + 1 / sqrt((m.x43 - m.x55)**2 + (m.x113 - m.x125)**2
    + (m.x183 - m.x195)**2) + 1 / sqrt((m.x43 - m.x56)**2 + (m.x113 - m.x126)
    **2 + (m.x183 - m.x196)**2) + 1 / sqrt((m.x43 - m.x57)**2 + (m.x113 -
    m.x127)**2 + (m.x183 - m.x197)**2) + 1 / sqrt((m.x43 - m.x58)**2 + (m.x113
    - m.x128)**2 + (m.x183 - m.x198)**2) + 1 / sqrt((m.x43 - m.x59)**2 + (
    m.x113 - m.x129)**2 + (m.x183 - m.x199)**2) + 1 / sqrt((m.x43 - m.x60)**2
    + (m.x113 - m.x130)**2 + (m.x183 - m.x200)**2) + 1 / sqrt((m.x43 - m.x61)
    **2 + (m.x113 - m.x131)**2 + (m.x183 - m.x201)**2) + 1 / sqrt((m.x43 -
    m.x62)**2 + (m.x113 - m.x132)**2 + (m.x183 - m.x202)**2) + 1 / sqrt((m.x43
    - m.x63)**2 + (m.x113 - m.x133)**2 + (m.x183 - m.x203)**2) + 1 / sqrt((
    m.x43 - m.x64)**2 + (m.x113 - m.x134)**2 + (m.x183 - m.x204)**2) + 1 /
    sqrt((m.x43 - m.x65)**2 + (m.x113 - m.x135)**2 + (m.x183 - m.x205)**2) + 1
    / sqrt((m.x43 - m.x66)**2 + (m.x113 - m.x136)**2 + (m.x183 - m.x206)**2)
    + 1 / sqrt((m.x43 - m.x67)**2 + (m.x113 - m.x137)**2 + (m.x183 - m.x207)**
    2) + 1 / sqrt((m.x43 - m.x68)**2 + (m.x113 - m.x138)**2 + (m.x183 - m.x208)
    **2) + 1 / sqrt((m.x43 - m.x69)**2 + (m.x113 - m.x139)**2 + (m.x183 -
    m.x209)**2) + 1 / sqrt((m.x43 - m.x70)**2 + (m.x113 - m.x140)**2 + (m.x183
    - m.x210)**2) + 1 / sqrt((m.x44 - m.x45)**2 + (m.x114 - m.x115)**2 + (
    m.x184 - m.x185)**2) + 1 / sqrt((m.x44 - m.x46)**2 + (m.x114 - m.x116)**2
    + (m.x184 - m.x186)**2) + 1 / sqrt((m.x44 - m.x47)**2 + (m.x114 - m.x117)
    **2 + (m.x184 - m.x187)**2) + 1 / sqrt((m.x44 - m.x48)**2 + (m.x114 -
    m.x118)**2 + (m.x184 - m.x188)**2) + 1 / sqrt((m.x44 - m.x49)**2 + (m.x114
    - m.x119)**2 + (m.x184 - m.x189)**2) + 1 / sqrt((m.x44 - m.x50)**2 + (
    m.x114 - m.x120)**2 + (m.x184 - m.x190)**2) + 1 / sqrt((m.x44 - m.x51)**2
    + (m.x114 - m.x121)**2 + (m.x184 - m.x191)**2) + 1 / sqrt((m.x44 - m.x52)
    **2 + (m.x114 - m.x122)**2 + (m.x184 - m.x192)**2) + 1 / sqrt((m.x44 -
    m.x53)**2 + (m.x114 - m.x123)**2 + (m.x184 - m.x193)**2) + 1 / sqrt((m.x44
    - m.x54)**2 + (m.x114 - m.x124)**2 + (m.x184 - m.x194)**2) + 1 / sqrt((
    m.x44 - m.x55)**2 + (m.x114 - m.x125)**2 + (m.x184 - m.x195)**2) + 1 /
    sqrt((m.x44 - m.x56)**2 + (m.x114 - m.x126)**2 + (m.x184 - m.x196)**2) + 1
    / sqrt((m.x44 - m.x57)**2 + (m.x114 - m.x127)**2 + (m.x184 - m.x197)**2)
    + 1 / sqrt((m.x44 - m.x58)**2 + (m.x114 - m.x128)**2 + (m.x184 - m.x198)**
    2) + 1 / sqrt((m.x44 - m.x59)**2 + (m.x114 - m.x129)**2 + (m.x184 - m.x199)
    **2) + 1 / sqrt((m.x44 - m.x60)**2 + (m.x114 - m.x130)**2 + (m.x184 -
    m.x200)**2) + 1 / sqrt((m.x44 - m.x61)**2 + (m.x114 - m.x131)**2 + (m.x184
    - m.x201)**2) + 1 / sqrt((m.x44 - m.x62)**2 + (m.x114 - m.x132)**2 + (
    m.x184 - m.x202)**2) + 1 / sqrt((m.x44 - m.x63)**2 + (m.x114 - m.x133)**2
    + (m.x184 - m.x203)**2) + 1 / sqrt((m.x44 - m.x64)**2 + (m.x114 - m.x134)
    **2 + (m.x184 - m.x204)**2) + 1 / sqrt((m.x44 - m.x65)**2 + (m.x114 -
    m.x135)**2 + (m.x184 - m.x205)**2) + 1 / sqrt((m.x44 - m.x66)**2 + (m.x114
    - m.x136)**2 + (m.x184 - m.x206)**2) + 1 / sqrt((m.x44 - m.x67)**2 + (
    m.x114 - m.x137)**2 + (m.x184 - m.x207)**2) + 1 / sqrt((m.x44 - m.x68)**2
    + (m.x114 - m.x138)**2 + (m.x184 - m.x208)**2) + 1 / sqrt((m.x44 - m.x69)
    **2 + (m.x114 - m.x139)**2 + (m.x184 - m.x209)**2) + 1 / sqrt((m.x44 -
    m.x70)**2 + (m.x114 - m.x140)**2 + (m.x184 - m.x210)**2) + 1 / sqrt((m.x45
    - m.x46)**2 + (m.x115 - m.x116)**2 + (m.x185 - m.x186)**2) + 1 / sqrt((
    m.x45 - m.x47)**2 + (m.x115 - m.x117)**2 + (m.x185 - m.x187)**2) + 1 /
    sqrt((m.x45 - m.x48)**2 + (m.x115 - m.x118)**2 + (m.x185 - m.x188)**2) + 1
    / sqrt((m.x45 - m.x49)**2 + (m.x115 - m.x119)**2 + (m.x185 - m.x189)**2)
    + 1 / sqrt((m.x45 - m.x50)**2 + (m.x115 - m.x120)**2 + (m.x185 - m.x190)**
    2) + 1 / sqrt((m.x45 - m.x51)**2 + (m.x115 - m.x121)**2 + (m.x185 - m.x191)
    **2) + 1 / sqrt((m.x45 - m.x52)**2 + (m.x115 - m.x122)**2 + (m.x185 -
    m.x192)**2) + 1 / sqrt((m.x45 - m.x53)**2 + (m.x115 - m.x123)**2 + (m.x185
    - m.x193)**2) + 1 / sqrt((m.x45 - m.x54)**2 + (m.x115 - m.x124)**2 + (
    m.x185 - m.x194)**2) + 1 / sqrt((m.x45 - m.x55)**2 + (m.x115 - m.x125)**2
    + (m.x185 - m.x195)**2) + 1 / sqrt((m.x45 - m.x56)**2 + (m.x115 - m.x126)
    **2 + (m.x185 - m.x196)**2) + 1 / sqrt((m.x45 - m.x57)**2 + (m.x115 -
    m.x127)**2 + (m.x185 - m.x197)**2) + 1 / sqrt((m.x45 - m.x58)**2 + (m.x115
    - m.x128)**2 + (m.x185 - m.x198)**2) + 1 / sqrt((m.x45 - m.x59)**2 + (
    m.x115 - m.x129)**2 + (m.x185 - m.x199)**2) + 1 / sqrt((m.x45 - m.x60)**2
    + (m.x115 - m.x130)**2 + (m.x185 - m.x200)**2) + 1 / sqrt((m.x45 - m.x61)
    **2 + (m.x115 - m.x131)**2 + (m.x185 - m.x201)**2) + 1 / sqrt((m.x45 -
    m.x62)**2 + (m.x115 - m.x132)**2 + (m.x185 - m.x202)**2) + 1 / sqrt((m.x45
    - m.x63)**2 + (m.x115 - m.x133)**2 + (m.x185 - m.x203)**2) + 1 / sqrt((
    m.x45 - m.x64)**2 + (m.x115 - m.x134)**2 + (m.x185 - m.x204)**2) + 1 /
    sqrt((m.x45 - m.x65)**2 + (m.x115 - m.x135)**2 + (m.x185 - m.x205)**2) + 1
    / sqrt((m.x45 - m.x66)**2 + (m.x115 - m.x136)**2 + (m.x185 - m.x206)**2)
    + 1 / sqrt((m.x45 - m.x67)**2 + (m.x115 - m.x137)**2 + (m.x185 - m.x207)**
    2) + 1 / sqrt((m.x45 - m.x68)**2 + (m.x115 - m.x138)**2 + (m.x185 - m.x208)
    **2) + 1 / sqrt((m.x45 - m.x69)**2 + (m.x115 - m.x139)**2 + (m.x185 -
    m.x209)**2) + 1 / sqrt((m.x45 - m.x70)**2 + (m.x115 - m.x140)**2 + (m.x185
    - m.x210)**2) + 1 / sqrt((m.x46 - m.x47)**2 + (m.x116 - m.x117)**2 + (
    m.x186 - m.x187)**2) + 1 / sqrt((m.x46 - m.x48)**2 + (m.x116 - m.x118)**2
    + (m.x186 - m.x188)**2) + 1 / sqrt((m.x46 - m.x49)**2 + (m.x116 - m.x119)
    **2 + (m.x186 - m.x189)**2) + 1 / sqrt((m.x46 - m.x50)**2 + (m.x116 -
    m.x120)**2 + (m.x186 - m.x190)**2) + 1 / sqrt((m.x46 - m.x51)**2 + (m.x116
    - m.x121)**2 + (m.x186 - m.x191)**2) + 1 / sqrt((m.x46 - m.x52)**2 + (
    m.x116 - m.x122)**2 + (m.x186 - m.x192)**2) + 1 / sqrt((m.x46 - m.x53)**2
    + (m.x116 - m.x123)**2 + (m.x186 - m.x193)**2) + 1 / sqrt((m.x46 - m.x54)
    **2 + (m.x116 - m.x124)**2 + (m.x186 - m.x194)**2) + 1 / sqrt((m.x46 -
    m.x55)**2 + (m.x116 - m.x125)**2 + (m.x186 - m.x195)**2) + 1 / sqrt((m.x46
    - m.x56)**2 + (m.x116 - m.x126)**2 + (m.x186 - m.x196)**2) + 1 / sqrt((
    m.x46 - m.x57)**2 + (m.x116 - m.x127)**2 + (m.x186 - m.x197)**2) + 1 /
    sqrt((m.x46 - m.x58)**2 + (m.x116 - m.x128)**2 + (m.x186 - m.x198)**2) + 1
    / sqrt((m.x46 - m.x59)**2 + (m.x116 - m.x129)**2 + (m.x186 - m.x199)**2)
    + 1 / sqrt((m.x46 - m.x60)**2 + (m.x116 - m.x130)**2 + (m.x186 - m.x200)**
    2) + 1 / sqrt((m.x46 - m.x61)**2 + (m.x116 - m.x131)**2 + (m.x186 - m.x201)
    **2) + 1 / sqrt((m.x46 - m.x62)**2 + (m.x116 - m.x132)**2 + (m.x186 -
    m.x202)**2) + 1 / sqrt((m.x46 - m.x63)**2 + (m.x116 - m.x133)**2 + (m.x186
    - m.x203)**2) + 1 / sqrt((m.x46 - m.x64)**2 + (m.x116 - m.x134)**2 + (
    m.x186 - m.x204)**2) + 1 / sqrt((m.x46 - m.x65)**2 + (m.x116 - m.x135)**2
    + (m.x186 - m.x205)**2) + 1 / sqrt((m.x46 - m.x66)**2 + (m.x116 - m.x136)
    **2 + (m.x186 - m.x206)**2) + 1 / sqrt((m.x46 - m.x67)**2 + (m.x116 -
    m.x137)**2 + (m.x186 - m.x207)**2) + 1 / sqrt((m.x46 - m.x68)**2 + (m.x116
    - m.x138)**2 + (m.x186 - m.x208)**2) + 1 / sqrt((m.x46 - m.x69)**2 + (
    m.x116 - m.x139)**2 + (m.x186 - m.x209)**2) + 1 / sqrt((m.x46 - m.x70)**2
    + (m.x116 - m.x140)**2 + (m.x186 - m.x210)**2) + 1 / sqrt((m.x47 - m.x48)
    **2 + (m.x117 - m.x118)**2 + (m.x187 - m.x188)**2) + 1 / sqrt((m.x47 -
    m.x49)**2 + (m.x117 - m.x119)**2 + (m.x187 - m.x189)**2) + 1 / sqrt((m.x47
    - m.x50)**2 + (m.x117 - m.x120)**2 + (m.x187 - m.x190)**2) + 1 / sqrt((
    m.x47 - m.x51)**2 + (m.x117 - m.x121)**2 + (m.x187 - m.x191)**2) + 1 /
    sqrt((m.x47 - m.x52)**2 + (m.x117 - m.x122)**2 + (m.x187 - m.x192)**2) + 1
    / sqrt((m.x47 - m.x53)**2 + (m.x117 - m.x123)**2 + (m.x187 - m.x193)**2)
    + 1 / sqrt((m.x47 - m.x54)**2 + (m.x117 - m.x124)**2 + (m.x187 - m.x194)**
    2) + 1 / sqrt((m.x47 - m.x55)**2 + (m.x117 - m.x125)**2 + (m.x187 - m.x195)
    **2) + 1 / sqrt((m.x47 - m.x56)**2 + (m.x117 - m.x126)**2 + (m.x187 -
    m.x196)**2) + 1 / sqrt((m.x47 - m.x57)**2 + (m.x117 - m.x127)**2 + (m.x187
    - m.x197)**2) + 1 / sqrt((m.x47 - m.x58)**2 + (m.x117 - m.x128)**2 + (
    m.x187 - m.x198)**2) + 1 / sqrt((m.x47 - m.x59)**2 + (m.x117 - m.x129)**2
    + (m.x187 - m.x199)**2) + 1 / sqrt((m.x47 - m.x60)**2 + (m.x117 - m.x130)
    **2 + (m.x187 - m.x200)**2) + 1 / sqrt((m.x47 - m.x61)**2 + (m.x117 -
    m.x131)**2 + (m.x187 - m.x201)**2) + 1 / sqrt((m.x47 - m.x62)**2 + (m.x117
    - m.x132)**2 + (m.x187 - m.x202)**2) + 1 / sqrt((m.x47 - m.x63)**2 + (
    m.x117 - m.x133)**2 + (m.x187 - m.x203)**2) + 1 / sqrt((m.x47 - m.x64)**2
    + (m.x117 - m.x134)**2 + (m.x187 - m.x204)**2) + 1 / sqrt((m.x47 - m.x65)
    **2 + (m.x117 - m.x135)**2 + (m.x187 - m.x205)**2) + 1 / sqrt((m.x47 -
    m.x66)**2 + (m.x117 - m.x136)**2 + (m.x187 - m.x206)**2) + 1 / sqrt((m.x47
    - m.x67)**2 + (m.x117 - m.x137)**2 + (m.x187 - m.x207)**2) + 1 / sqrt((
    m.x47 - m.x68)**2 + (m.x117 - m.x138)**2 + (m.x187 - m.x208)**2) + 1 /
    sqrt((m.x47 - m.x69)**2 + (m.x117 - m.x139)**2 + (m.x187 - m.x209)**2) + 1
    / sqrt((m.x47 - m.x70)**2 + (m.x117 - m.x140)**2 + (m.x187 - m.x210)**2)
    + 1 / sqrt((m.x48 - m.x49)**2 + (m.x118 - m.x119)**2 + (m.x188 - m.x189)**
    2) + 1 / sqrt((m.x48 - m.x50)**2 + (m.x118 - m.x120)**2 + (m.x188 - m.x190)
    **2) + 1 / sqrt((m.x48 - m.x51)**2 + (m.x118 - m.x121)**2 + (m.x188 -
    m.x191)**2) + 1 / sqrt((m.x48 - m.x52)**2 + (m.x118 - m.x122)**2 + (m.x188
    - m.x192)**2) + 1 / sqrt((m.x48 - m.x53)**2 + (m.x118 - m.x123)**2 + (
    m.x188 - m.x193)**2) + 1 / sqrt((m.x48 - m.x54)**2 + (m.x118 - m.x124)**2
    + (m.x188 - m.x194)**2) + 1 / sqrt((m.x48 - m.x55)**2 + (m.x118 - m.x125)
    **2 + (m.x188 - m.x195)**2) + 1 / sqrt((m.x48 - m.x56)**2 + (m.x118 -
    m.x126)**2 + (m.x188 - m.x196)**2) + 1 / sqrt((m.x48 - m.x57)**2 + (m.x118
    - m.x127)**2 + (m.x188 - m.x197)**2) + 1 / sqrt((m.x48 - m.x58)**2 + (
    m.x118 - m.x128)**2 + (m.x188 - m.x198)**2) + 1 / sqrt((m.x48 - m.x59)**2
    + (m.x118 - m.x129)**2 + (m.x188 - m.x199)**2) + 1 / sqrt((m.x48 - m.x60)
    **2 + (m.x118 - m.x130)**2 + (m.x188 - m.x200)**2) + 1 / sqrt((m.x48 -
    m.x61)**2 + (m.x118 - m.x131)**2 + (m.x188 - m.x201)**2) + 1 / sqrt((m.x48
    - m.x62)**2 + (m.x118 - m.x132)**2 + (m.x188 - m.x202)**2) + 1 / sqrt((
    m.x48 - m.x63)**2 + (m.x118 - m.x133)**2 + (m.x188 - m.x203)**2) + 1 /
    sqrt((m.x48 - m.x64)**2 + (m.x118 - m.x134)**2 + (m.x188 - m.x204)**2) + 1
    / sqrt((m.x48 - m.x65)**2 + (m.x118 - m.x135)**2 + (m.x188 - m.x205)**2)
    + 1 / sqrt((m.x48 - m.x66)**2 + (m.x118 - m.x136)**2 + (m.x188 - m.x206)**
    2) + 1 / sqrt((m.x48 - m.x67)**2 + (m.x118 - m.x137)**2 + (m.x188 - m.x207)
    **2) + 1 / sqrt((m.x48 - m.x68)**2 + (m.x118 - m.x138)**2 + (m.x188 -
    m.x208)**2) + 1 / sqrt((m.x48 - m.x69)**2 + (m.x118 - m.x139)**2 + (m.x188
    - m.x209)**2) + 1 / sqrt((m.x48 - m.x70)**2 + (m.x118 - m.x140)**2 + (
    m.x188 - m.x210)**2) + 1 / sqrt((m.x49 - m.x50)**2 + (m.x119 - m.x120)**2
    + (m.x189 - m.x190)**2) + 1 / sqrt((m.x49 - m.x51)**2 + (m.x119 - m.x121)
    **2 + (m.x189 - m.x191)**2) + 1 / sqrt((m.x49 - m.x52)**2 + (m.x119 -
    m.x122)**2 + (m.x189 - m.x192)**2) + 1 / sqrt((m.x49 - m.x53)**2 + (m.x119
    - m.x123)**2 + (m.x189 - m.x193)**2) + 1 / sqrt((m.x49 - m.x54)**2 + (
    m.x119 - m.x124)**2 + (m.x189 - m.x194)**2) + 1 / sqrt((m.x49 - m.x55)**2
    + (m.x119 - m.x125)**2 + (m.x189 - m.x195)**2) + 1 / sqrt((m.x49 - m.x56)
    **2 + (m.x119 - m.x126)**2 + (m.x189 - m.x196)**2) + 1 / sqrt((m.x49 -
    m.x57)**2 + (m.x119 - m.x127)**2 + (m.x189 - m.x197)**2) + 1 / sqrt((m.x49
    - m.x58)**2 + (m.x119 - m.x128)**2 + (m.x189 - m.x198)**2) + 1 / sqrt((
    m.x49 - m.x59)**2 + (m.x119 - m.x129)**2 + (m.x189 - m.x199)**2) + 1 /
    sqrt((m.x49 - m.x60)**2 + (m.x119 - m.x130)**2 + (m.x189 - m.x200)**2) + 1
    / sqrt((m.x49 - m.x61)**2 + (m.x119 - m.x131)**2 + (m.x189 - m.x201)**2)
    + 1 / sqrt((m.x49 - m.x62)**2 + (m.x119 - m.x132)**2 + (m.x189 - m.x202)**
    2) + 1 / sqrt((m.x49 - m.x63)**2 + (m.x119 - m.x133)**2 + (m.x189 - m.x203)
    **2) + 1 / sqrt((m.x49 - m.x64)**2 + (m.x119 - m.x134)**2 + (m.x189 -
    m.x204)**2) + 1 / sqrt((m.x49 - m.x65)**2 + (m.x119 - m.x135)**2 + (m.x189
    - m.x205)**2) + 1 / sqrt((m.x49 - m.x66)**2 + (m.x119 - m.x136)**2 + (
    m.x189 - m.x206)**2) + 1 / sqrt((m.x49 - m.x67)**2 + (m.x119 - m.x137)**2
    + (m.x189 - m.x207)**2) + 1 / sqrt((m.x49 - m.x68)**2 + (m.x119 - m.x138)
    **2 + (m.x189 - m.x208)**2) + 1 / sqrt((m.x49 - m.x69)**2 + (m.x119 -
    m.x139)**2 + (m.x189 - m.x209)**2) + 1 / sqrt((m.x49 - m.x70)**2 + (m.x119
    - m.x140)**2 + (m.x189 - m.x210)**2) + 1 / sqrt((m.x50 - m.x51)**2 + (
    m.x120 - m.x121)**2 + (m.x190 - m.x191)**2) + 1 / sqrt((m.x50 - m.x52)**2
    + (m.x120 - m.x122)**2 + (m.x190 - m.x192)**2) + 1 / sqrt((m.x50 - m.x53)
    **2 + (m.x120 - m.x123)**2 + (m.x190 - m.x193)**2) + 1 / sqrt((m.x50 -
    m.x54)**2 + (m.x120 - m.x124)**2 + (m.x190 - m.x194)**2) + 1 / sqrt((m.x50
    - m.x55)**2 + (m.x120 - m.x125)**2 + (m.x190 - m.x195)**2) + 1 / sqrt((
    m.x50 - m.x56)**2 + (m.x120 - m.x126)**2 + (m.x190 - m.x196)**2) + 1 /
    sqrt((m.x50 - m.x57)**2 + (m.x120 - m.x127)**2 + (m.x190 - m.x197)**2) + 1
    / sqrt((m.x50 - m.x58)**2 + (m.x120 - m.x128)**2 + (m.x190 - m.x198)**2)
    + 1 / sqrt((m.x50 - m.x59)**2 + (m.x120 - m.x129)**2 + (m.x190 - m.x199)**
    2) + 1 / sqrt((m.x50 - m.x60)**2 + (m.x120 - m.x130)**2 + (m.x190 - m.x200)
    **2) + 1 / sqrt((m.x50 - m.x61)**2 + (m.x120 - m.x131)**2 + (m.x190 -
    m.x201)**2) + 1 / sqrt((m.x50 - m.x62)**2 + (m.x120 - m.x132)**2 + (m.x190
    - m.x202)**2) + 1 / sqrt((m.x50 - m.x63)**2 + (m.x120 - m.x133)**2 + (
    m.x190 - m.x203)**2) + 1 / sqrt((m.x50 - m.x64)**2 + (m.x120 - m.x134)**2
    + (m.x190 - m.x204)**2) + 1 / sqrt((m.x50 - m.x65)**2 + (m.x120 - m.x135)
    **2 + (m.x190 - m.x205)**2) + 1 / sqrt((m.x50 - m.x66)**2 + (m.x120 -
    m.x136)**2 + (m.x190 - m.x206)**2) + 1 / sqrt((m.x50 - m.x67)**2 + (m.x120
    - m.x137)**2 + (m.x190 - m.x207)**2) + 1 / sqrt((m.x50 - m.x68)**2 + (
    m.x120 - m.x138)**2 + (m.x190 - m.x208)**2) + 1 / sqrt((m.x50 - m.x69)**2
    + (m.x120 - m.x139)**2 + (m.x190 - m.x209)**2) + 1 / sqrt((m.x50 - m.x70)
    **2 + (m.x120 - m.x140)**2 + (m.x190 - m.x210)**2) + 1 / sqrt((m.x51 -
    m.x52)**2 + (m.x121 - m.x122)**2 + (m.x191 - m.x192)**2) + 1 / sqrt((m.x51
    - m.x53)**2 + (m.x121 - m.x123)**2 + (m.x191 - m.x193)**2) + 1 / sqrt((
    m.x51 - m.x54)**2 + (m.x121 - m.x124)**2 + (m.x191 - m.x194)**2) + 1 /
    sqrt((m.x51 - m.x55)**2 + (m.x121 - m.x125)**2 + (m.x191 - m.x195)**2) + 1
    / sqrt((m.x51 - m.x56)**2 + (m.x121 - m.x126)**2 + (m.x191 - m.x196)**2)
    + 1 / sqrt((m.x51 - m.x57)**2 + (m.x121 - m.x127)**2 + (m.x191 - m.x197)**
    2) + 1 / sqrt((m.x51 - m.x58)**2 + (m.x121 - m.x128)**2 + (m.x191 - m.x198)
    **2) + 1 / sqrt((m.x51 - m.x59)**2 + (m.x121 - m.x129)**2 + (m.x191 -
    m.x199)**2) + 1 / sqrt((m.x51 - m.x60)**2 + (m.x121 - m.x130)**2 + (m.x191
    - m.x200)**2) + 1 / sqrt((m.x51 - m.x61)**2 + (m.x121 - m.x131)**2 + (
    m.x191 - m.x201)**2) + 1 / sqrt((m.x51 - m.x62)**2 + (m.x121 - m.x132)**2
    + (m.x191 - m.x202)**2) + 1 / sqrt((m.x51 - m.x63)**2 + (m.x121 - m.x133)
    **2 + (m.x191 - m.x203)**2) + 1 / sqrt((m.x51 - m.x64)**2 + (m.x121 -
    m.x134)**2 + (m.x191 - m.x204)**2) + 1 / sqrt((m.x51 - m.x65)**2 + (m.x121
    - m.x135)**2 + (m.x191 - m.x205)**2) + 1 / sqrt((m.x51 - m.x66)**2 + (
    m.x121 - m.x136)**2 + (m.x191 - m.x206)**2) + 1 / sqrt((m.x51 - m.x67)**2
    + (m.x121 - m.x137)**2 + (m.x191 - m.x207)**2) + 1 / sqrt((m.x51 - m.x68)
    **2 + (m.x121 - m.x138)**2 + (m.x191 - m.x208)**2) + 1 / sqrt((m.x51 -
    m.x69)**2 + (m.x121 - m.x139)**2 + (m.x191 - m.x209)**2) + 1 / sqrt((m.x51
    - m.x70)**2 + (m.x121 - m.x140)**2 + (m.x191 - m.x210)**2) + 1 / sqrt((
    m.x52 - m.x53)**2 + (m.x122 - m.x123)**2 + (m.x192 - m.x193)**2) + 1 /
    sqrt((m.x52 - m.x54)**2 + (m.x122 - m.x124)**2 + (m.x192 - m.x194)**2) + 1
    / sqrt((m.x52 - m.x55)**2 + (m.x122 - m.x125)**2 + (m.x192 - m.x195)**2)
    + 1 / sqrt((m.x52 - m.x56)**2 + (m.x122 - m.x126)**2 + (m.x192 - m.x196)**
    2) + 1 / sqrt((m.x52 - m.x57)**2 + (m.x122 - m.x127)**2 + (m.x192 - m.x197)
    **2) + 1 / sqrt((m.x52 - m.x58)**2 + (m.x122 - m.x128)**2 + (m.x192 -
    m.x198)**2) + 1 / sqrt((m.x52 - m.x59)**2 + (m.x122 - m.x129)**2 + (m.x192
    - m.x199)**2) + 1 / sqrt((m.x52 - m.x60)**2 + (m.x122 - m.x130)**2 + (
    m.x192 - m.x200)**2) + 1 / sqrt((m.x52 - m.x61)**2 + (m.x122 - m.x131)**2
    + (m.x192 - m.x201)**2) + 1 / sqrt((m.x52 - m.x62)**2 + (m.x122 - m.x132)
    **2 + (m.x192 - m.x202)**2) + 1 / sqrt((m.x52 - m.x63)**2 + (m.x122 -
    m.x133)**2 + (m.x192 - m.x203)**2) + 1 / sqrt((m.x52 - m.x64)**2 + (m.x122
    - m.x134)**2 + (m.x192 - m.x204)**2) + 1 / sqrt((m.x52 - m.x65)**2 + (
    m.x122 - m.x135)**2 + (m.x192 - m.x205)**2) + 1 / sqrt((m.x52 - m.x66)**2
    + (m.x122 - m.x136)**2 + (m.x192 - m.x206)**2) + 1 / sqrt((m.x52 - m.x67)
    **2 + (m.x122 - m.x137)**2 + (m.x192 - m.x207)**2) + 1 / sqrt((m.x52 -
    m.x68)**2 + (m.x122 - m.x138)**2 + (m.x192 - m.x208)**2) + 1 / sqrt((m.x52
    - m.x69)**2 + (m.x122 - m.x139)**2 + (m.x192 - m.x209)**2) + 1 / sqrt((
    m.x52 - m.x70)**2 + (m.x122 - m.x140)**2 + (m.x192 - m.x210)**2) + 1 /
    sqrt((m.x53 - m.x54)**2 + (m.x123 - m.x124)**2 + (m.x193 - m.x194)**2) + 1
    / sqrt((m.x53 - m.x55)**2 + (m.x123 - m.x125)**2 + (m.x193 - m.x195)**2)
    + 1 / sqrt((m.x53 - m.x56)**2 + (m.x123 - m.x126)**2 + (m.x193 - m.x196)**
    2) + 1 / sqrt((m.x53 - m.x57)**2 + (m.x123 - m.x127)**2 + (m.x193 - m.x197)
    **2) + 1 / sqrt((m.x53 - m.x58)**2 + (m.x123 - m.x128)**2 + (m.x193 -
    m.x198)**2) + 1 / sqrt((m.x53 - m.x59)**2 + (m.x123 - m.x129)**2 + (m.x193
    - m.x199)**2) + 1 / sqrt((m.x53 - m.x60)**2 + (m.x123 - m.x130)**2 + (
    m.x193 - m.x200)**2) + 1 / sqrt((m.x53 - m.x61)**2 + (m.x123 - m.x131)**2
    + (m.x193 - m.x201)**2) + 1 / sqrt((m.x53 - m.x62)**2 + (m.x123 - m.x132)
    **2 + (m.x193 - m.x202)**2) + 1 / sqrt((m.x53 - m.x63)**2 + (m.x123 -
    m.x133)**2 + (m.x193 - m.x203)**2) + 1 / sqrt((m.x53 - m.x64)**2 + (m.x123
    - m.x134)**2 + (m.x193 - m.x204)**2) + 1 / sqrt((m.x53 - m.x65)**2 + (
    m.x123 - m.x135)**2 + (m.x193 - m.x205)**2) + 1 / sqrt((m.x53 - m.x66)**2
    + (m.x123 - m.x136)**2 + (m.x193 - m.x206)**2) + 1 / sqrt((m.x53 - m.x67)
    **2 + (m.x123 - m.x137)**2 + (m.x193 - m.x207)**2) + 1 / sqrt((m.x53 -
    m.x68)**2 + (m.x123 - m.x138)**2 + (m.x193 - m.x208)**2) + 1 / sqrt((m.x53
    - m.x69)**2 + (m.x123 - m.x139)**2 + (m.x193 - m.x209)**2) + 1 / sqrt((
    m.x53 - m.x70)**2 + (m.x123 - m.x140)**2 + (m.x193 - m.x210)**2) + 1 /
    sqrt((m.x54 - m.x55)**2 + (m.x124 - m.x125)**2 + (m.x194 - m.x195)**2) + 1
    / sqrt((m.x54 - m.x56)**2 + (m.x124 - m.x126)**2 + (m.x194 - m.x196)**2)
    + 1 / sqrt((m.x54 - m.x57)**2 + (m.x124 - m.x127)**2 + (m.x194 - m.x197)**
    2) + 1 / sqrt((m.x54 - m.x58)**2 + (m.x124 - m.x128)**2 + (m.x194 - m.x198)
    **2) + 1 / sqrt((m.x54 - m.x59)**2 + (m.x124 - m.x129)**2 + (m.x194 -
    m.x199)**2) + 1 / sqrt((m.x54 - m.x60)**2 + (m.x124 - m.x130)**2 + (m.x194
    - m.x200)**2) + 1 / sqrt((m.x54 - m.x61)**2 + (m.x124 - m.x131)**2 + (
    m.x194 - m.x201)**2) + 1 / sqrt((m.x54 - m.x62)**2 + (m.x124 - m.x132)**2
    + (m.x194 - m.x202)**2) + 1 / sqrt((m.x54 - m.x63)**2 + (m.x124 - m.x133)
    **2 + (m.x194 - m.x203)**2) + 1 / sqrt((m.x54 - m.x64)**2 + (m.x124 -
    m.x134)**2 + (m.x194 - m.x204)**2) + 1 / sqrt((m.x54 - m.x65)**2 + (m.x124
    - m.x135)**2 + (m.x194 - m.x205)**2) + 1 / sqrt((m.x54 - m.x66)**2 + (
    m.x124 - m.x136)**2 + (m.x194 - m.x206)**2) + 1 / sqrt((m.x54 - m.x67)**2
    + (m.x124 - m.x137)**2 + (m.x194 - m.x207)**2) + 1 / sqrt((m.x54 - m.x68)
    **2 + (m.x124 - m.x138)**2 + (m.x194 - m.x208)**2) + 1 / sqrt((m.x54 -
    m.x69)**2 + (m.x124 - m.x139)**2 + (m.x194 - m.x209)**2) + 1 / sqrt((m.x54
    - m.x70)**2 + (m.x124 - m.x140)**2 + (m.x194 - m.x210)**2) + 1 / sqrt((
    m.x55 - m.x56)**2 + (m.x125 - m.x126)**2 + (m.x195 - m.x196)**2) + 1 /
    sqrt((m.x55 - m.x57)**2 + (m.x125 - m.x127)**2 + (m.x195 - m.x197)**2) + 1
    / sqrt((m.x55 - m.x58)**2 + (m.x125 - m.x128)**2 + (m.x195 - m.x198)**2)
    + 1 / sqrt((m.x55 - m.x59)**2 + (m.x125 - m.x129)**2 + (m.x195 - m.x199)**
    2) + 1 / sqrt((m.x55 - m.x60)**2 + (m.x125 - m.x130)**2 + (m.x195 - m.x200)
    **2) + 1 / sqrt((m.x55 - m.x61)**2 + (m.x125 - m.x131)**2 + (m.x195 -
    m.x201)**2) + 1 / sqrt((m.x55 - m.x62)**2 + (m.x125 - m.x132)**2 + (m.x195
    - m.x202)**2) + 1 / sqrt((m.x55 - m.x63)**2 + (m.x125 - m.x133)**2 + (
    m.x195 - m.x203)**2) + 1 / sqrt((m.x55 - m.x64)**2 + (m.x125 - m.x134)**2
    + (m.x195 - m.x204)**2) + 1 / sqrt((m.x55 - m.x65)**2 + (m.x125 - m.x135)
    **2 + (m.x195 - m.x205)**2) + 1 / sqrt((m.x55 - m.x66)**2 + (m.x125 -
    m.x136)**2 + (m.x195 - m.x206)**2) + 1 / sqrt((m.x55 - m.x67)**2 + (m.x125
    - m.x137)**2 + (m.x195 - m.x207)**2) + 1 / sqrt((m.x55 - m.x68)**2 + (
    m.x125 - m.x138)**2 + (m.x195 - m.x208)**2) + 1 / sqrt((m.x55 - m.x69)**2
    + (m.x125 - m.x139)**2 + (m.x195 - m.x209)**2) + 1 / sqrt((m.x55 - m.x70)
    **2 + (m.x125 - m.x140)**2 + (m.x195 - m.x210)**2) + 1 / sqrt((m.x56 -
    m.x57)**2 + (m.x126 - m.x127)**2 + (m.x196 - m.x197)**2) + 1 / sqrt((m.x56
    - m.x58)**2 + (m.x126 - m.x128)**2 + (m.x196 - m.x198)**2) + 1 / sqrt((
    m.x56 - m.x59)**2 + (m.x126 - m.x129)**2 + (m.x196 - m.x199)**2) + 1 /
    sqrt((m.x56 - m.x60)**2 + (m.x126 - m.x130)**2 + (m.x196 - m.x200)**2) + 1
    / sqrt((m.x56 - m.x61)**2 + (m.x126 - m.x131)**2 + (m.x196 - m.x201)**2)
    + 1 / sqrt((m.x56 - m.x62)**2 + (m.x126 - m.x132)**2 + (m.x196 - m.x202)**
    2) + 1 / sqrt((m.x56 - m.x63)**2 + (m.x126 - m.x133)**2 + (m.x196 - m.x203)
    **2) + 1 / sqrt((m.x56 - m.x64)**2 + (m.x126 - m.x134)**2 + (m.x196 -
    m.x204)**2) + 1 / sqrt((m.x56 - m.x65)**2 + (m.x126 - m.x135)**2 + (m.x196
    - m.x205)**2) + 1 / sqrt((m.x56 - m.x66)**2 + (m.x126 - m.x136)**2 + (
    m.x196 - m.x206)**2) + 1 / sqrt((m.x56 - m.x67)**2 + (m.x126 - m.x137)**2
    + (m.x196 - m.x207)**2) + 1 / sqrt((m.x56 - m.x68)**2 + (m.x126 - m.x138)
    **2 + (m.x196 - m.x208)**2) + 1 / sqrt((m.x56 - m.x69)**2 + (m.x126 -
    m.x139)**2 + (m.x196 - m.x209)**2) + 1 / sqrt((m.x56 - m.x70)**2 + (m.x126
    - m.x140)**2 + (m.x196 - m.x210)**2) + 1 / sqrt((m.x57 - m.x58)**2 + (
    m.x127 - m.x128)**2 + (m.x197 - m.x198)**2) + 1 / sqrt((m.x57 - m.x59)**2
    + (m.x127 - m.x129)**2 + (m.x197 - m.x199)**2) + 1 / sqrt((m.x57 - m.x60)
    **2 + (m.x127 - m.x130)**2 + (m.x197 - m.x200)**2) + 1 / sqrt((m.x57 -
    m.x61)**2 + (m.x127 - m.x131)**2 + (m.x197 - m.x201)**2) + 1 / sqrt((m.x57
    - m.x62)**2 + (m.x127 - m.x132)**2 + (m.x197 - m.x202)**2) + 1 / sqrt((
    m.x57 - m.x63)**2 + (m.x127 - m.x133)**2 + (m.x197 - m.x203)**2) + 1 /
    sqrt((m.x57 - m.x64)**2 + (m.x127 - m.x134)**2 + (m.x197 - m.x204)**2) + 1
    / sqrt((m.x57 - m.x65)**2 + (m.x127 - m.x135)**2 + (m.x197 - m.x205)**2)
    + 1 / sqrt((m.x57 - m.x66)**2 + (m.x127 - m.x136)**2 + (m.x197 - m.x206)**
    2) + 1 / sqrt((m.x57 - m.x67)**2 + (m.x127 - m.x137)**2 + (m.x197 - m.x207)
    **2) + 1 / sqrt((m.x57 - m.x68)**2 + (m.x127 - m.x138)**2 + (m.x197 -
    m.x208)**2) + 1 / sqrt((m.x57 - m.x69)**2 + (m.x127 - m.x139)**2 + (m.x197
    - m.x209)**2) + 1 / sqrt((m.x57 - m.x70)**2 + (m.x127 - m.x140)**2 + (
    m.x197 - m.x210)**2) + 1 / sqrt((m.x58 - m.x59)**2 + (m.x128 - m.x129)**2
    + (m.x198 - m.x199)**2) + 1 / sqrt((m.x58 - m.x60)**2 + (m.x128 - m.x130)
    **2 + (m.x198 - m.x200)**2) + 1 / sqrt((m.x58 - m.x61)**2 + (m.x128 -
    m.x131)**2 + (m.x198 - m.x201)**2) + 1 / sqrt((m.x58 - m.x62)**2 + (m.x128
    - m.x132)**2 + (m.x198 - m.x202)**2) + 1 / sqrt((m.x58 - m.x63)**2 + (
    m.x128 - m.x133)**2 + (m.x198 - m.x203)**2) + 1 / sqrt((m.x58 - m.x64)**2
    + (m.x128 - m.x134)**2 + (m.x198 - m.x204)**2) + 1 / sqrt((m.x58 - m.x65)
    **2 + (m.x128 - m.x135)**2 + (m.x198 - m.x205)**2) + 1 / sqrt((m.x58 -
    m.x66)**2 + (m.x128 - m.x136)**2 + (m.x198 - m.x206)**2) + 1 / sqrt((m.x58
    - m.x67)**2 + (m.x128 - m.x137)**2 + (m.x198 - m.x207)**2) + 1 / sqrt((
    m.x58 - m.x68)**2 + (m.x128 - m.x138)**2 + (m.x198 - m.x208)**2) + 1 /
    sqrt((m.x58 - m.x69)**2 + (m.x128 - m.x139)**2 + (m.x198 - m.x209)**2) + 1
    / sqrt((m.x58 - m.x70)**2 + (m.x128 - m.x140)**2 + (m.x198 - m.x210)**2)
    + 1 / sqrt((m.x59 - m.x60)**2 + (m.x129 - m.x130)**2 + (m.x199 - m.x200)**
    2) + 1 / sqrt((m.x59 - m.x61)**2 + (m.x129 - m.x131)**2 + (m.x199 - m.x201)
    **2) + 1 / sqrt((m.x59 - m.x62)**2 + (m.x129 - m.x132)**2 + (m.x199 -
    m.x202)**2) + 1 / sqrt((m.x59 - m.x63)**2 + (m.x129 - m.x133)**2 + (m.x199
    - m.x203)**2) + 1 / sqrt((m.x59 - m.x64)**2 + (m.x129 - m.x134)**2 + (
    m.x199 - m.x204)**2) + 1 / sqrt((m.x59 - m.x65)**2 + (m.x129 - m.x135)**2
    + (m.x199 - m.x205)**2) + 1 / sqrt((m.x59 - m.x66)**2 + (m.x129 - m.x136)
    **2 + (m.x199 - m.x206)**2) + 1 / sqrt((m.x59 - m.x67)**2 + (m.x129 -
    m.x137)**2 + (m.x199 - m.x207)**2) + 1 / sqrt((m.x59 - m.x68)**2 + (m.x129
    - m.x138)**2 + (m.x199 - m.x208)**2) + 1 / sqrt((m.x59 - m.x69)**2 + (
    m.x129 - m.x139)**2 + (m.x199 - m.x209)**2) + 1 / sqrt((m.x59 - m.x70)**2
    + (m.x129 - m.x140)**2 + (m.x199 - m.x210)**2) + 1 / sqrt((m.x60 - m.x61)
    **2 + (m.x130 - m.x131)**2 + (m.x200 - m.x201)**2) + 1 / sqrt((m.x60 -
    m.x62)**2 + (m.x130 - m.x132)**2 + (m.x200 - m.x202)**2) + 1 / sqrt((m.x60
    - m.x63)**2 + (m.x130 - m.x133)**2 + (m.x200 - m.x203)**2) + 1 / sqrt((
    m.x60 - m.x64)**2 + (m.x130 - m.x134)**2 + (m.x200 - m.x204)**2) + 1 /
    sqrt((m.x60 - m.x65)**2 + (m.x130 - m.x135)**2 + (m.x200 - m.x205)**2) + 1
    / sqrt((m.x60 - m.x66)**2 + (m.x130 - m.x136)**2 + (m.x200 - m.x206)**2)
    + 1 / sqrt((m.x60 - m.x67)**2 + (m.x130 - m.x137)**2 + (m.x200 - m.x207)**
    2) + 1 / sqrt((m.x60 - m.x68)**2 + (m.x130 - m.x138)**2 + (m.x200 - m.x208)
    **2) + 1 / sqrt((m.x60 - m.x69)**2 + (m.x130 - m.x139)**2 + (m.x200 -
    m.x209)**2) + 1 / sqrt((m.x60 - m.x70)**2 + (m.x130 - m.x140)**2 + (m.x200
    - m.x210)**2) + 1 / sqrt((m.x61 - m.x62)**2 + (m.x131 - m.x132)**2 + (
    m.x201 - m.x202)**2) + 1 / sqrt((m.x61 - m.x63)**2 + (m.x131 - m.x133)**2
    + (m.x201 - m.x203)**2) + 1 / sqrt((m.x61 - m.x64)**2 + (m.x131 - m.x134)
    **2 + (m.x201 - m.x204)**2) + 1 / sqrt((m.x61 - m.x65)**2 + (m.x131 -
    m.x135)**2 + (m.x201 - m.x205)**2) + 1 / sqrt((m.x61 - m.x66)**2 + (m.x131
    - m.x136)**2 + (m.x201 - m.x206)**2) + 1 / sqrt((m.x61 - m.x67)**2 + (
    m.x131 - m.x137)**2 + (m.x201 - m.x207)**2) + 1 / sqrt((m.x61 - m.x68)**2
    + (m.x131 - m.x138)**2 + (m.x201 - m.x208)**2) + 1 / sqrt((m.x61 - m.x69)
    **2 + (m.x131 - m.x139)**2 + (m.x201 - m.x209)**2) + 1 / sqrt((m.x61 -
    m.x70)**2 + (m.x131 - m.x140)**2 + (m.x201 - m.x210)**2) + 1 / sqrt((m.x62
    - m.x63)**2 + (m.x132 - m.x133)**2 + (m.x202 - m.x203)**2) + 1 / sqrt((
    m.x62 - m.x64)**2 + (m.x132 - m.x134)**2 + (m.x202 - m.x204)**2) + 1 /
    sqrt((m.x62 - m.x65)**2 + (m.x132 - m.x135)**2 + (m.x202 - m.x205)**2) + 1
    / sqrt((m.x62 - m.x66)**2 + (m.x132 - m.x136)**2 + (m.x202 - m.x206)**2)
    + 1 / sqrt((m.x62 - m.x67)**2 + (m.x132 - m.x137)**2 + (m.x202 - m.x207)**
    2) + 1 / sqrt((m.x62 - m.x68)**2 + (m.x132 - m.x138)**2 + (m.x202 - m.x208)
    **2) + 1 / sqrt((m.x62 - m.x69)**2 + (m.x132 - m.x139)**2 + (m.x202 -
    m.x209)**2) + 1 / sqrt((m.x62 - m.x70)**2 + (m.x132 - m.x140)**2 + (m.x202
    - m.x210)**2) + 1 / sqrt((m.x63 - m.x64)**2 + (m.x133 - m.x134)**2 + (
    m.x203 - m.x204)**2) + 1 / sqrt((m.x63 - m.x65)**2 + (m.x133 - m.x135)**2
    + (m.x203 - m.x205)**2) + 1 / sqrt((m.x63 - m.x66)**2 + (m.x133 - m.x136)
    **2 + (m.x203 - m.x206)**2) + 1 / sqrt((m.x63 - m.x67)**2 + (m.x133 -
    m.x137)**2 + (m.x203 - m.x207)**2) + 1 / sqrt((m.x63 - m.x68)**2 + (m.x133
    - m.x138)**2 + (m.x203 - m.x208)**2) + 1 / sqrt((m.x63 - m.x69)**2 + (
    m.x133 - m.x139)**2 + (m.x203 - m.x209)**2) + 1 / sqrt((m.x63 - m.x70)**2
    + (m.x133 - m.x140)**2 + (m.x203 - m.x210)**2) + 1 / sqrt((m.x64 - m.x65)
    **2 + (m.x134 - m.x135)**2 + (m.x204 - m.x205)**2) + 1 / sqrt((m.x64 -
    m.x66)**2 + (m.x134 - m.x136)**2 + (m.x204 - m.x206)**2) + 1 / sqrt((m.x64
    - m.x67)**2 + (m.x134 - m.x137)**2 + (m.x204 - m.x207)**2) + 1 / sqrt((
    m.x64 - m.x68)**2 + (m.x134 - m.x138)**2 + (m.x204 - m.x208)**2) + 1 /
    sqrt((m.x64 - m.x69)**2 + (m.x134 - m.x139)**2 + (m.x204 - m.x209)**2) + 1
    / sqrt((m.x64 - m.x70)**2 + (m.x134 - m.x140)**2 + (m.x204 - m.x210)**2)
    + 1 / sqrt((m.x65 - m.x66)**2 + (m.x135 - m.x136)**2 + (m.x205 - m.x206)**
    2) + 1 / sqrt((m.x65 - m.x67)**2 + (m.x135 - m.x137)**2 + (m.x205 - m.x207)
    **2) + 1 / sqrt((m.x65 - m.x68)**2 + (m.x135 - m.x138)**2 + (m.x205 -
    m.x208)**2) + 1 / sqrt((m.x65 - m.x69)**2 + (m.x135 - m.x139)**2 + (m.x205
    - m.x209)**2) + 1 / sqrt((m.x65 - m.x70)**2 + (m.x135 - m.x140)**2 + (
    m.x205 - m.x210)**2) + 1 / sqrt((m.x66 - m.x67)**2 + (m.x136 - m.x137)**2
    + (m.x206 - m.x207)**2) + 1 / sqrt((m.x66 - m.x68)**2 + (m.x136 - m.x138)
    **2 + (m.x206 - m.x208)**2) + 1 / sqrt((m.x66 - m.x69)**2 + (m.x136 -
    m.x139)**2 + (m.x206 - m.x209)**2) + 1 / sqrt((m.x66 - m.x70)**2 + (m.x136
    - m.x140)**2 + (m.x206 - m.x210)**2) + 1 / sqrt((m.x67 - m.x68)**2 + (
    m.x137 - m.x138)**2 + (m.x207 - m.x208)**2) + 1 / sqrt((m.x67 - m.x69)**2
    + (m.x137 - m.x139)**2 + (m.x207 - m.x209)**2) + 1 / sqrt((m.x67 - m.x70)
    **2 + (m.x137 - m.x140)**2 + (m.x207 - m.x210)**2) + 1 / sqrt((m.x68 -
    m.x69)**2 + (m.x138 - m.x139)**2 + (m.x208 - m.x209)**2) + 1 / sqrt((m.x68
    - m.x70)**2 + (m.x138 - m.x140)**2 + (m.x208 - m.x210)**2) + 1 / sqrt((
    m.x69 - m.x70)**2 + (m.x139 - m.x140)**2 + (m.x209 - m.x210)**2))

m.e1 = Constraint(expr= m.x1**2 + m.x71**2 + m.x141**2 == 1)
m.e2 = Constraint(expr= m.x2**2 + m.x72**2 + m.x142**2 == 1)
m.e3 = Constraint(expr= m.x3**2 + m.x73**2 + m.x143**2 == 1)
m.e4 = Constraint(expr= m.x4**2 + m.x74**2 + m.x144**2 == 1)
m.e5 = Constraint(expr= m.x5**2 + m.x75**2 + m.x145**2 == 1)
m.e6 = Constraint(expr= m.x6**2 + m.x76**2 + m.x146**2 == 1)
m.e7 = Constraint(expr= m.x7**2 + m.x77**2 + m.x147**2 == 1)
m.e8 = Constraint(expr= m.x8**2 + m.x78**2 + m.x148**2 == 1)
m.e9 = Constraint(expr= m.x9**2 + m.x79**2 + m.x149**2 == 1)
m.e10 = Constraint(expr= m.x10**2 + m.x80**2 + m.x150**2 == 1)
m.e11 = Constraint(expr= m.x11**2 + m.x81**2 + m.x151**2 == 1)
m.e12 = Constraint(expr= m.x12**2 + m.x82**2 + m.x152**2 == 1)
m.e13 = Constraint(expr= m.x13**2 + m.x83**2 + m.x153**2 == 1)
m.e14 = Constraint(expr= m.x14**2 + m.x84**2 + m.x154**2 == 1)
m.e15 = Constraint(expr= m.x15**2 + m.x85**2 + m.x155**2 == 1)
m.e16 = Constraint(expr= m.x16**2 + m.x86**2 + m.x156**2 == 1)
m.e17 = Constraint(expr= m.x17**2 + m.x87**2 + m.x157**2 == 1)
m.e18 = Constraint(expr= m.x18**2 + m.x88**2 + m.x158**2 == 1)
m.e19 = Constraint(expr= m.x19**2 + m.x89**2 + m.x159**2 == 1)
m.e20 = Constraint(expr= m.x20**2 + m.x90**2 + m.x160**2 == 1)
m.e21 = Constraint(expr= m.x21**2 + m.x91**2 + m.x161**2 == 1)
m.e22 = Constraint(expr= m.x22**2 + m.x92**2 + m.x162**2 == 1)
m.e23 = Constraint(expr= m.x23**2 + m.x93**2 + m.x163**2 == 1)
m.e24 = Constraint(expr= m.x24**2 + m.x94**2 + m.x164**2 == 1)
m.e25 = Constraint(expr= m.x25**2 + m.x95**2 + m.x165**2 == 1)
m.e26 = Constraint(expr= m.x26**2 + m.x96**2 + m.x166**2 == 1)
m.e27 = Constraint(expr= m.x27**2 + m.x97**2 + m.x167**2 == 1)
m.e28 = Constraint(expr= m.x28**2 + m.x98**2 + m.x168**2 == 1)
m.e29 = Constraint(expr= m.x29**2 + m.x99**2 + m.x169**2 == 1)
m.e30 = Constraint(expr= m.x30**2 + m.x100**2 + m.x170**2 == 1)
m.e31 = Constraint(expr= m.x31**2 + m.x101**2 + m.x171**2 == 1)
m.e32 = Constraint(expr= m.x32**2 + m.x102**2 + m.x172**2 == 1)
m.e33 = Constraint(expr= m.x33**2 + m.x103**2 + m.x173**2 == 1)
m.e34 = Constraint(expr= m.x34**2 + m.x104**2 + m.x174**2 == 1)
m.e35 = Constraint(expr= m.x35**2 + m.x105**2 + m.x175**2 == 1)
m.e36 = Constraint(expr= m.x36**2 + m.x106**2 + m.x176**2 == 1)
m.e37 = Constraint(expr= m.x37**2 + m.x107**2 + m.x177**2 == 1)
m.e38 = Constraint(expr= m.x38**2 + m.x108**2 + m.x178**2 == 1)
m.e39 = Constraint(expr= m.x39**2 + m.x109**2 + m.x179**2 == 1)
m.e40 = Constraint(expr= m.x40**2 + m.x110**2 + m.x180**2 == 1)
m.e41 = Constraint(expr= m.x41**2 + m.x111**2 + m.x181**2 == 1)
m.e42 = Constraint(expr= m.x42**2 + m.x112**2 + m.x182**2 == 1)
m.e43 = Constraint(expr= m.x43**2 + m.x113**2 + m.x183**2 == 1)
m.e44 = Constraint(expr= m.x44**2 + m.x114**2 + m.x184**2 == 1)
m.e45 = Constraint(expr= m.x45**2 + m.x115**2 + m.x185**2 == 1)
m.e46 = Constraint(expr= m.x46**2 + m.x116**2 + m.x186**2 == 1)
m.e47 = Constraint(expr= m.x47**2 + m.x117**2 + m.x187**2 == 1)
m.e48 = Constraint(expr= m.x48**2 + m.x118**2 + m.x188**2 == 1)
m.e49 = Constraint(expr= m.x49**2 + m.x119**2 + m.x189**2 == 1)
m.e50 = Constraint(expr= m.x50**2 + m.x120**2 + m.x190**2 == 1)
m.e51 = Constraint(expr= m.x51**2 + m.x121**2 + m.x191**2 == 1)
m.e52 = Constraint(expr= m.x52**2 + m.x122**2 + m.x192**2 == 1)
m.e53 = Constraint(expr= m.x53**2 + m.x123**2 + m.x193**2 == 1)
m.e54 = Constraint(expr= m.x54**2 + m.x124**2 + m.x194**2 == 1)
m.e55 = Constraint(expr= m.x55**2 + m.x125**2 + m.x195**2 == 1)
m.e56 = Constraint(expr= m.x56**2 + m.x126**2 + m.x196**2 == 1)
m.e57 = Constraint(expr= m.x57**2 + m.x127**2 + m.x197**2 == 1)
m.e58 = Constraint(expr= m.x58**2 + m.x128**2 + m.x198**2 == 1)
m.e59 = Constraint(expr= m.x59**2 + m.x129**2 + m.x199**2 == 1)
m.e60 = Constraint(expr= m.x60**2 + m.x130**2 + m.x200**2 == 1)
m.e61 = Constraint(expr= m.x61**2 + m.x131**2 + m.x201**2 == 1)
m.e62 = Constraint(expr= m.x62**2 + m.x132**2 + m.x202**2 == 1)
m.e63 = Constraint(expr= m.x63**2 + m.x133**2 + m.x203**2 == 1)
m.e64 = Constraint(expr= m.x64**2 + m.x134**2 + m.x204**2 == 1)
m.e65 = Constraint(expr= m.x65**2 + m.x135**2 + m.x205**2 == 1)
m.e66 = Constraint(expr= m.x66**2 + m.x136**2 + m.x206**2 == 1)
m.e67 = Constraint(expr= m.x67**2 + m.x137**2 + m.x207**2 == 1)
m.e68 = Constraint(expr= m.x68**2 + m.x138**2 + m.x208**2 == 1)
m.e69 = Constraint(expr= m.x69**2 + m.x139**2 + m.x209**2 == 1)
m.e70 = Constraint(expr= m.x70**2 + m.x140**2 + m.x210**2 == 1)
