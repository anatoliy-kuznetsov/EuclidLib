# NLP written by GAMS Convert at 05/15/24 11:39:15
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#      3081        0     3081        0        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#       237      237        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#     18486        0    18486
#
# Reformulation has removed 1 variable and 1 equation

from pyomo.environ import *

model = m = ConcreteModel()

m.x1 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x2 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x3 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x4 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x5 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x6 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x7 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x8 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x9 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x10 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x11 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x12 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x13 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x14 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x15 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x16 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x17 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x18 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x19 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x20 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x21 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x22 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x23 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x24 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x25 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x26 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x27 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x28 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x29 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x30 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x31 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x32 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x33 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x34 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x35 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x36 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x37 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x38 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x39 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x40 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x41 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x42 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x43 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x44 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x45 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x46 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x47 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x48 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x49 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x50 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x51 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x52 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x53 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x54 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x55 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x56 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x57 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x58 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x59 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x60 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x61 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x62 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x63 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x64 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x65 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x66 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x67 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x68 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x69 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x70 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x71 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x72 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x73 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x74 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x75 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x76 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x77 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x78 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x79 = Var(within=Reals, bounds=(0,78), initialize=0)
m.x80 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x81 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x82 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x83 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x84 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x85 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x86 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x87 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x88 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x89 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x90 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x91 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x92 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x93 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x94 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x95 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x96 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x97 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x98 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x99 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x100 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x101 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x102 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x103 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x104 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x105 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x106 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x107 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x108 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x109 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x110 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x111 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x112 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x113 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x114 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x115 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x116 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x117 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x118 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x119 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x120 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x121 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x122 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x123 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x124 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x125 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x126 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x127 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x128 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x129 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x130 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x131 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x132 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x133 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x134 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x135 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x136 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x137 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x138 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x139 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x140 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x141 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x142 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x143 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x144 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x145 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x146 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x147 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x148 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x149 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x150 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x151 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x152 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x153 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x154 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x155 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x156 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x157 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x158 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x159 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x160 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x161 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x162 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x163 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x164 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x165 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x166 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x167 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x168 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x169 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x170 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x171 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x172 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x173 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x174 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x175 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x176 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x177 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x178 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x179 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x180 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x181 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x182 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x183 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x184 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x185 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x186 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x187 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x188 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x189 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x190 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x191 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x192 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x193 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x194 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x195 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x196 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x197 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x198 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x199 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x200 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x201 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x202 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x203 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x204 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x205 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x206 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x207 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x208 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x209 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x210 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x211 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x212 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x213 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x214 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x215 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x216 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x217 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x218 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x219 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x220 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x221 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x222 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x223 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x224 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x225 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x226 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x227 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x228 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x229 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x230 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x231 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x232 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x233 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x234 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x235 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x236 = Var(within=Reals, bounds=(-78,78), initialize=0)
m.x237 = Var(within=Reals, bounds=(-78,78), initialize=0)

m.obj = Objective(sense=minimize, expr= ((m.x1 - m.x2)**2 + (m.x80 - m.x81)**2
    + (m.x159 - m.x160)**2)**(-3) * (((m.x1 - m.x2)**2 + (m.x80 - m.x81)**2 +
    (m.x159 - m.x160)**2)**(-3) - 2) + ((m.x1 - m.x3)**2 + (m.x80 - m.x82)**2
    + (m.x159 - m.x161)**2)**(-3) * (((m.x1 - m.x3)**2 + (m.x80 - m.x82)**2 +
    (m.x159 - m.x161)**2)**(-3) - 2) + ((m.x1 - m.x4)**2 + (m.x80 - m.x83)**2
    + (m.x159 - m.x162)**2)**(-3) * (((m.x1 - m.x4)**2 + (m.x80 - m.x83)**2 +
    (m.x159 - m.x162)**2)**(-3) - 2) + ((m.x1 - m.x5)**2 + (m.x80 - m.x84)**2
    + (m.x159 - m.x163)**2)**(-3) * (((m.x1 - m.x5)**2 + (m.x80 - m.x84)**2 +
    (m.x159 - m.x163)**2)**(-3) - 2) + ((m.x1 - m.x6)**2 + (m.x80 - m.x85)**2
    + (m.x159 - m.x164)**2)**(-3) * (((m.x1 - m.x6)**2 + (m.x80 - m.x85)**2 +
    (m.x159 - m.x164)**2)**(-3) - 2) + ((m.x1 - m.x7)**2 + (m.x80 - m.x86)**2
    + (m.x159 - m.x165)**2)**(-3) * (((m.x1 - m.x7)**2 + (m.x80 - m.x86)**2 +
    (m.x159 - m.x165)**2)**(-3) - 2) + ((m.x1 - m.x8)**2 + (m.x80 - m.x87)**2
    + (m.x159 - m.x166)**2)**(-3) * (((m.x1 - m.x8)**2 + (m.x80 - m.x87)**2 +
    (m.x159 - m.x166)**2)**(-3) - 2) + ((m.x1 - m.x9)**2 + (m.x80 - m.x88)**2
    + (m.x159 - m.x167)**2)**(-3) * (((m.x1 - m.x9)**2 + (m.x80 - m.x88)**2 +
    (m.x159 - m.x167)**2)**(-3) - 2) + ((m.x1 - m.x10)**2 + (m.x80 - m.x89)**2
    + (m.x159 - m.x168)**2)**(-3) * (((m.x1 - m.x10)**2 + (m.x80 - m.x89)**2
    + (m.x159 - m.x168)**2)**(-3) - 2) + ((m.x1 - m.x11)**2 + (m.x80 - m.x90)
    **2 + (m.x159 - m.x169)**2)**(-3) * (((m.x1 - m.x11)**2 + (m.x80 - m.x90)**
    2 + (m.x159 - m.x169)**2)**(-3) - 2) + ((m.x1 - m.x12)**2 + (m.x80 - m.x91)
    **2 + (m.x159 - m.x170)**2)**(-3) * (((m.x1 - m.x12)**2 + (m.x80 - m.x91)**
    2 + (m.x159 - m.x170)**2)**(-3) - 2) + ((m.x1 - m.x13)**2 + (m.x80 - m.x92)
    **2 + (m.x159 - m.x171)**2)**(-3) * (((m.x1 - m.x13)**2 + (m.x80 - m.x92)**
    2 + (m.x159 - m.x171)**2)**(-3) - 2) + ((m.x1 - m.x14)**2 + (m.x80 - m.x93)
    **2 + (m.x159 - m.x172)**2)**(-3) * (((m.x1 - m.x14)**2 + (m.x80 - m.x93)**
    2 + (m.x159 - m.x172)**2)**(-3) - 2) + ((m.x1 - m.x15)**2 + (m.x80 - m.x94)
    **2 + (m.x159 - m.x173)**2)**(-3) * (((m.x1 - m.x15)**2 + (m.x80 - m.x94)**
    2 + (m.x159 - m.x173)**2)**(-3) - 2) + ((m.x1 - m.x16)**2 + (m.x80 - m.x95)
    **2 + (m.x159 - m.x174)**2)**(-3) * (((m.x1 - m.x16)**2 + (m.x80 - m.x95)**
    2 + (m.x159 - m.x174)**2)**(-3) - 2) + ((m.x1 - m.x17)**2 + (m.x80 - m.x96)
    **2 + (m.x159 - m.x175)**2)**(-3) * (((m.x1 - m.x17)**2 + (m.x80 - m.x96)**
    2 + (m.x159 - m.x175)**2)**(-3) - 2) + ((m.x1 - m.x18)**2 + (m.x80 - m.x97)
    **2 + (m.x159 - m.x176)**2)**(-3) * (((m.x1 - m.x18)**2 + (m.x80 - m.x97)**
    2 + (m.x159 - m.x176)**2)**(-3) - 2) + ((m.x1 - m.x19)**2 + (m.x80 - m.x98)
    **2 + (m.x159 - m.x177)**2)**(-3) * (((m.x1 - m.x19)**2 + (m.x80 - m.x98)**
    2 + (m.x159 - m.x177)**2)**(-3) - 2) + ((m.x1 - m.x20)**2 + (m.x80 - m.x99)
    **2 + (m.x159 - m.x178)**2)**(-3) * (((m.x1 - m.x20)**2 + (m.x80 - m.x99)**
    2 + (m.x159 - m.x178)**2)**(-3) - 2) + ((m.x1 - m.x21)**2 + (m.x80 - m.x100)
    **2 + (m.x159 - m.x179)**2)**(-3) * (((m.x1 - m.x21)**2 + (m.x80 - m.x100)
    **2 + (m.x159 - m.x179)**2)**(-3) - 2) + ((m.x1 - m.x22)**2 + (m.x80 -
    m.x101)**2 + (m.x159 - m.x180)**2)**(-3) * (((m.x1 - m.x22)**2 + (m.x80 -
    m.x101)**2 + (m.x159 - m.x180)**2)**(-3) - 2) + ((m.x1 - m.x23)**2 + (m.x80
    - m.x102)**2 + (m.x159 - m.x181)**2)**(-3) * (((m.x1 - m.x23)**2 + (m.x80
    - m.x102)**2 + (m.x159 - m.x181)**2)**(-3) - 2) + ((m.x1 - m.x24)**2 + (
    m.x80 - m.x103)**2 + (m.x159 - m.x182)**2)**(-3) * (((m.x1 - m.x24)**2 + (
    m.x80 - m.x103)**2 + (m.x159 - m.x182)**2)**(-3) - 2) + ((m.x1 - m.x25)**2
    + (m.x80 - m.x104)**2 + (m.x159 - m.x183)**2)**(-3) * (((m.x1 - m.x25)**2
    + (m.x80 - m.x104)**2 + (m.x159 - m.x183)**2)**(-3) - 2) + ((m.x1 - m.x26)
    **2 + (m.x80 - m.x105)**2 + (m.x159 - m.x184)**2)**(-3) * (((m.x1 - m.x26)
    **2 + (m.x80 - m.x105)**2 + (m.x159 - m.x184)**2)**(-3) - 2) + ((m.x1 -
    m.x27)**2 + (m.x80 - m.x106)**2 + (m.x159 - m.x185)**2)**(-3) * (((m.x1 -
    m.x27)**2 + (m.x80 - m.x106)**2 + (m.x159 - m.x185)**2)**(-3) - 2) + ((m.x1
    - m.x28)**2 + (m.x80 - m.x107)**2 + (m.x159 - m.x186)**2)**(-3) * (((m.x1
    - m.x28)**2 + (m.x80 - m.x107)**2 + (m.x159 - m.x186)**2)**(-3) - 2) + ((
    m.x1 - m.x29)**2 + (m.x80 - m.x108)**2 + (m.x159 - m.x187)**2)**(-3) * (((
    m.x1 - m.x29)**2 + (m.x80 - m.x108)**2 + (m.x159 - m.x187)**2)**(-3) - 2)
    + ((m.x1 - m.x30)**2 + (m.x80 - m.x109)**2 + (m.x159 - m.x188)**2)**(-3)
    * (((m.x1 - m.x30)**2 + (m.x80 - m.x109)**2 + (m.x159 - m.x188)**2)**(-3)
    - 2) + ((m.x1 - m.x31)**2 + (m.x80 - m.x110)**2 + (m.x159 - m.x189)**2)**(
    -3) * (((m.x1 - m.x31)**2 + (m.x80 - m.x110)**2 + (m.x159 - m.x189)**2)**(
    -3) - 2) + ((m.x1 - m.x32)**2 + (m.x80 - m.x111)**2 + (m.x159 - m.x190)**2)
    **(-3) * (((m.x1 - m.x32)**2 + (m.x80 - m.x111)**2 + (m.x159 - m.x190)**2)
    **(-3) - 2) + ((m.x1 - m.x33)**2 + (m.x80 - m.x112)**2 + (m.x159 - m.x191)
    **2)**(-3) * (((m.x1 - m.x33)**2 + (m.x80 - m.x112)**2 + (m.x159 - m.x191)
    **2)**(-3) - 2) + ((m.x1 - m.x34)**2 + (m.x80 - m.x113)**2 + (m.x159 -
    m.x192)**2)**(-3) * (((m.x1 - m.x34)**2 + (m.x80 - m.x113)**2 + (m.x159 -
    m.x192)**2)**(-3) - 2) + ((m.x1 - m.x35)**2 + (m.x80 - m.x114)**2 + (m.x159
    - m.x193)**2)**(-3) * (((m.x1 - m.x35)**2 + (m.x80 - m.x114)**2 + (m.x159
    - m.x193)**2)**(-3) - 2) + ((m.x1 - m.x36)**2 + (m.x80 - m.x115)**2 + (
    m.x159 - m.x194)**2)**(-3) * (((m.x1 - m.x36)**2 + (m.x80 - m.x115)**2 + (
    m.x159 - m.x194)**2)**(-3) - 2) + ((m.x1 - m.x37)**2 + (m.x80 - m.x116)**2
    + (m.x159 - m.x195)**2)**(-3) * (((m.x1 - m.x37)**2 + (m.x80 - m.x116)**2
    + (m.x159 - m.x195)**2)**(-3) - 2) + ((m.x1 - m.x38)**2 + (m.x80 - m.x117)
    **2 + (m.x159 - m.x196)**2)**(-3) * (((m.x1 - m.x38)**2 + (m.x80 - m.x117)
    **2 + (m.x159 - m.x196)**2)**(-3) - 2) + ((m.x1 - m.x39)**2 + (m.x80 -
    m.x118)**2 + (m.x159 - m.x197)**2)**(-3) * (((m.x1 - m.x39)**2 + (m.x80 -
    m.x118)**2 + (m.x159 - m.x197)**2)**(-3) - 2) + ((m.x1 - m.x40)**2 + (m.x80
    - m.x119)**2 + (m.x159 - m.x198)**2)**(-3) * (((m.x1 - m.x40)**2 + (m.x80
    - m.x119)**2 + (m.x159 - m.x198)**2)**(-3) - 2) + ((m.x1 - m.x41)**2 + (
    m.x80 - m.x120)**2 + (m.x159 - m.x199)**2)**(-3) * (((m.x1 - m.x41)**2 + (
    m.x80 - m.x120)**2 + (m.x159 - m.x199)**2)**(-3) - 2) + ((m.x1 - m.x42)**2
    + (m.x80 - m.x121)**2 + (m.x159 - m.x200)**2)**(-3) * (((m.x1 - m.x42)**2
    + (m.x80 - m.x121)**2 + (m.x159 - m.x200)**2)**(-3) - 2) + ((m.x1 - m.x43)
    **2 + (m.x80 - m.x122)**2 + (m.x159 - m.x201)**2)**(-3) * (((m.x1 - m.x43)
    **2 + (m.x80 - m.x122)**2 + (m.x159 - m.x201)**2)**(-3) - 2) + ((m.x1 -
    m.x44)**2 + (m.x80 - m.x123)**2 + (m.x159 - m.x202)**2)**(-3) * (((m.x1 -
    m.x44)**2 + (m.x80 - m.x123)**2 + (m.x159 - m.x202)**2)**(-3) - 2) + ((m.x1
    - m.x45)**2 + (m.x80 - m.x124)**2 + (m.x159 - m.x203)**2)**(-3) * (((m.x1
    - m.x45)**2 + (m.x80 - m.x124)**2 + (m.x159 - m.x203)**2)**(-3) - 2) + ((
    m.x1 - m.x46)**2 + (m.x80 - m.x125)**2 + (m.x159 - m.x204)**2)**(-3) * (((
    m.x1 - m.x46)**2 + (m.x80 - m.x125)**2 + (m.x159 - m.x204)**2)**(-3) - 2)
    + ((m.x1 - m.x47)**2 + (m.x80 - m.x126)**2 + (m.x159 - m.x205)**2)**(-3)
    * (((m.x1 - m.x47)**2 + (m.x80 - m.x126)**2 + (m.x159 - m.x205)**2)**(-3)
    - 2) + ((m.x1 - m.x48)**2 + (m.x80 - m.x127)**2 + (m.x159 - m.x206)**2)**(
    -3) * (((m.x1 - m.x48)**2 + (m.x80 - m.x127)**2 + (m.x159 - m.x206)**2)**(
    -3) - 2) + ((m.x1 - m.x49)**2 + (m.x80 - m.x128)**2 + (m.x159 - m.x207)**2)
    **(-3) * (((m.x1 - m.x49)**2 + (m.x80 - m.x128)**2 + (m.x159 - m.x207)**2)
    **(-3) - 2) + ((m.x1 - m.x50)**2 + (m.x80 - m.x129)**2 + (m.x159 - m.x208)
    **2)**(-3) * (((m.x1 - m.x50)**2 + (m.x80 - m.x129)**2 + (m.x159 - m.x208)
    **2)**(-3) - 2) + ((m.x1 - m.x51)**2 + (m.x80 - m.x130)**2 + (m.x159 -
    m.x209)**2)**(-3) * (((m.x1 - m.x51)**2 + (m.x80 - m.x130)**2 + (m.x159 -
    m.x209)**2)**(-3) - 2) + ((m.x1 - m.x52)**2 + (m.x80 - m.x131)**2 + (m.x159
    - m.x210)**2)**(-3) * (((m.x1 - m.x52)**2 + (m.x80 - m.x131)**2 + (m.x159
    - m.x210)**2)**(-3) - 2) + ((m.x1 - m.x53)**2 + (m.x80 - m.x132)**2 + (
    m.x159 - m.x211)**2)**(-3) * (((m.x1 - m.x53)**2 + (m.x80 - m.x132)**2 + (
    m.x159 - m.x211)**2)**(-3) - 2) + ((m.x1 - m.x54)**2 + (m.x80 - m.x133)**2
    + (m.x159 - m.x212)**2)**(-3) * (((m.x1 - m.x54)**2 + (m.x80 - m.x133)**2
    + (m.x159 - m.x212)**2)**(-3) - 2) + ((m.x1 - m.x55)**2 + (m.x80 - m.x134)
    **2 + (m.x159 - m.x213)**2)**(-3) * (((m.x1 - m.x55)**2 + (m.x80 - m.x134)
    **2 + (m.x159 - m.x213)**2)**(-3) - 2) + ((m.x1 - m.x56)**2 + (m.x80 -
    m.x135)**2 + (m.x159 - m.x214)**2)**(-3) * (((m.x1 - m.x56)**2 + (m.x80 -
    m.x135)**2 + (m.x159 - m.x214)**2)**(-3) - 2) + ((m.x1 - m.x57)**2 + (m.x80
    - m.x136)**2 + (m.x159 - m.x215)**2)**(-3) * (((m.x1 - m.x57)**2 + (m.x80
    - m.x136)**2 + (m.x159 - m.x215)**2)**(-3) - 2) + ((m.x1 - m.x58)**2 + (
    m.x80 - m.x137)**2 + (m.x159 - m.x216)**2)**(-3) * (((m.x1 - m.x58)**2 + (
    m.x80 - m.x137)**2 + (m.x159 - m.x216)**2)**(-3) - 2) + ((m.x1 - m.x59)**2
    + (m.x80 - m.x138)**2 + (m.x159 - m.x217)**2)**(-3) * (((m.x1 - m.x59)**2
    + (m.x80 - m.x138)**2 + (m.x159 - m.x217)**2)**(-3) - 2) + ((m.x1 - m.x60)
    **2 + (m.x80 - m.x139)**2 + (m.x159 - m.x218)**2)**(-3) * (((m.x1 - m.x60)
    **2 + (m.x80 - m.x139)**2 + (m.x159 - m.x218)**2)**(-3) - 2) + ((m.x1 -
    m.x61)**2 + (m.x80 - m.x140)**2 + (m.x159 - m.x219)**2)**(-3) * (((m.x1 -
    m.x61)**2 + (m.x80 - m.x140)**2 + (m.x159 - m.x219)**2)**(-3) - 2) + ((m.x1
    - m.x62)**2 + (m.x80 - m.x141)**2 + (m.x159 - m.x220)**2)**(-3) * (((m.x1
    - m.x62)**2 + (m.x80 - m.x141)**2 + (m.x159 - m.x220)**2)**(-3) - 2) + ((
    m.x1 - m.x63)**2 + (m.x80 - m.x142)**2 + (m.x159 - m.x221)**2)**(-3) * (((
    m.x1 - m.x63)**2 + (m.x80 - m.x142)**2 + (m.x159 - m.x221)**2)**(-3) - 2)
    + ((m.x1 - m.x64)**2 + (m.x80 - m.x143)**2 + (m.x159 - m.x222)**2)**(-3)
    * (((m.x1 - m.x64)**2 + (m.x80 - m.x143)**2 + (m.x159 - m.x222)**2)**(-3)
    - 2) + ((m.x1 - m.x65)**2 + (m.x80 - m.x144)**2 + (m.x159 - m.x223)**2)**(
    -3) * (((m.x1 - m.x65)**2 + (m.x80 - m.x144)**2 + (m.x159 - m.x223)**2)**(
    -3) - 2) + ((m.x1 - m.x66)**2 + (m.x80 - m.x145)**2 + (m.x159 - m.x224)**2)
    **(-3) * (((m.x1 - m.x66)**2 + (m.x80 - m.x145)**2 + (m.x159 - m.x224)**2)
    **(-3) - 2) + ((m.x1 - m.x67)**2 + (m.x80 - m.x146)**2 + (m.x159 - m.x225)
    **2)**(-3) * (((m.x1 - m.x67)**2 + (m.x80 - m.x146)**2 + (m.x159 - m.x225)
    **2)**(-3) - 2) + ((m.x1 - m.x68)**2 + (m.x80 - m.x147)**2 + (m.x159 -
    m.x226)**2)**(-3) * (((m.x1 - m.x68)**2 + (m.x80 - m.x147)**2 + (m.x159 -
    m.x226)**2)**(-3) - 2) + ((m.x1 - m.x69)**2 + (m.x80 - m.x148)**2 + (m.x159
    - m.x227)**2)**(-3) * (((m.x1 - m.x69)**2 + (m.x80 - m.x148)**2 + (m.x159
    - m.x227)**2)**(-3) - 2) + ((m.x1 - m.x70)**2 + (m.x80 - m.x149)**2 + (
    m.x159 - m.x228)**2)**(-3) * (((m.x1 - m.x70)**2 + (m.x80 - m.x149)**2 + (
    m.x159 - m.x228)**2)**(-3) - 2) + ((m.x1 - m.x71)**2 + (m.x80 - m.x150)**2
    + (m.x159 - m.x229)**2)**(-3) * (((m.x1 - m.x71)**2 + (m.x80 - m.x150)**2
    + (m.x159 - m.x229)**2)**(-3) - 2) + ((m.x1 - m.x72)**2 + (m.x80 - m.x151)
    **2 + (m.x159 - m.x230)**2)**(-3) * (((m.x1 - m.x72)**2 + (m.x80 - m.x151)
    **2 + (m.x159 - m.x230)**2)**(-3) - 2) + ((m.x1 - m.x73)**2 + (m.x80 -
    m.x152)**2 + (m.x159 - m.x231)**2)**(-3) * (((m.x1 - m.x73)**2 + (m.x80 -
    m.x152)**2 + (m.x159 - m.x231)**2)**(-3) - 2) + ((m.x1 - m.x74)**2 + (m.x80
    - m.x153)**2 + (m.x159 - m.x232)**2)**(-3) * (((m.x1 - m.x74)**2 + (m.x80
    - m.x153)**2 + (m.x159 - m.x232)**2)**(-3) - 2) + ((m.x1 - m.x75)**2 + (
    m.x80 - m.x154)**2 + (m.x159 - m.x233)**2)**(-3) * (((m.x1 - m.x75)**2 + (
    m.x80 - m.x154)**2 + (m.x159 - m.x233)**2)**(-3) - 2) + ((m.x1 - m.x76)**2
    + (m.x80 - m.x155)**2 + (m.x159 - m.x234)**2)**(-3) * (((m.x1 - m.x76)**2
    + (m.x80 - m.x155)**2 + (m.x159 - m.x234)**2)**(-3) - 2) + ((m.x1 - m.x77)
    **2 + (m.x80 - m.x156)**2 + (m.x159 - m.x235)**2)**(-3) * (((m.x1 - m.x77)
    **2 + (m.x80 - m.x156)**2 + (m.x159 - m.x235)**2)**(-3) - 2) + ((m.x1 -
    m.x78)**2 + (m.x80 - m.x157)**2 + (m.x159 - m.x236)**2)**(-3) * (((m.x1 -
    m.x78)**2 + (m.x80 - m.x157)**2 + (m.x159 - m.x236)**2)**(-3) - 2) + ((m.x1
    - m.x79)**2 + (m.x80 - m.x158)**2 + (m.x159 - m.x237)**2)**(-3) * (((m.x1
    - m.x79)**2 + (m.x80 - m.x158)**2 + (m.x159 - m.x237)**2)**(-3) - 2) + ((
    m.x2 - m.x3)**2 + (m.x81 - m.x82)**2 + (m.x160 - m.x161)**2)**(-3) * (((
    m.x2 - m.x3)**2 + (m.x81 - m.x82)**2 + (m.x160 - m.x161)**2)**(-3) - 2) + (
    (m.x2 - m.x4)**2 + (m.x81 - m.x83)**2 + (m.x160 - m.x162)**2)**(-3) * (((
    m.x2 - m.x4)**2 + (m.x81 - m.x83)**2 + (m.x160 - m.x162)**2)**(-3) - 2) + (
    (m.x2 - m.x5)**2 + (m.x81 - m.x84)**2 + (m.x160 - m.x163)**2)**(-3) * (((
    m.x2 - m.x5)**2 + (m.x81 - m.x84)**2 + (m.x160 - m.x163)**2)**(-3) - 2) + (
    (m.x2 - m.x6)**2 + (m.x81 - m.x85)**2 + (m.x160 - m.x164)**2)**(-3) * (((
    m.x2 - m.x6)**2 + (m.x81 - m.x85)**2 + (m.x160 - m.x164)**2)**(-3) - 2) + (
    (m.x2 - m.x7)**2 + (m.x81 - m.x86)**2 + (m.x160 - m.x165)**2)**(-3) * (((
    m.x2 - m.x7)**2 + (m.x81 - m.x86)**2 + (m.x160 - m.x165)**2)**(-3) - 2) + (
    (m.x2 - m.x8)**2 + (m.x81 - m.x87)**2 + (m.x160 - m.x166)**2)**(-3) * (((
    m.x2 - m.x8)**2 + (m.x81 - m.x87)**2 + (m.x160 - m.x166)**2)**(-3) - 2) + (
    (m.x2 - m.x9)**2 + (m.x81 - m.x88)**2 + (m.x160 - m.x167)**2)**(-3) * (((
    m.x2 - m.x9)**2 + (m.x81 - m.x88)**2 + (m.x160 - m.x167)**2)**(-3) - 2) + (
    (m.x2 - m.x10)**2 + (m.x81 - m.x89)**2 + (m.x160 - m.x168)**2)**(-3) * (((
    m.x2 - m.x10)**2 + (m.x81 - m.x89)**2 + (m.x160 - m.x168)**2)**(-3) - 2) +
    ((m.x2 - m.x11)**2 + (m.x81 - m.x90)**2 + (m.x160 - m.x169)**2)**(-3) * (((
    m.x2 - m.x11)**2 + (m.x81 - m.x90)**2 + (m.x160 - m.x169)**2)**(-3) - 2) +
    ((m.x2 - m.x12)**2 + (m.x81 - m.x91)**2 + (m.x160 - m.x170)**2)**(-3) * (((
    m.x2 - m.x12)**2 + (m.x81 - m.x91)**2 + (m.x160 - m.x170)**2)**(-3) - 2) +
    ((m.x2 - m.x13)**2 + (m.x81 - m.x92)**2 + (m.x160 - m.x171)**2)**(-3) * (((
    m.x2 - m.x13)**2 + (m.x81 - m.x92)**2 + (m.x160 - m.x171)**2)**(-3) - 2) +
    ((m.x2 - m.x14)**2 + (m.x81 - m.x93)**2 + (m.x160 - m.x172)**2)**(-3) * (((
    m.x2 - m.x14)**2 + (m.x81 - m.x93)**2 + (m.x160 - m.x172)**2)**(-3) - 2) +
    ((m.x2 - m.x15)**2 + (m.x81 - m.x94)**2 + (m.x160 - m.x173)**2)**(-3) * (((
    m.x2 - m.x15)**2 + (m.x81 - m.x94)**2 + (m.x160 - m.x173)**2)**(-3) - 2) +
    ((m.x2 - m.x16)**2 + (m.x81 - m.x95)**2 + (m.x160 - m.x174)**2)**(-3) * (((
    m.x2 - m.x16)**2 + (m.x81 - m.x95)**2 + (m.x160 - m.x174)**2)**(-3) - 2) +
    ((m.x2 - m.x17)**2 + (m.x81 - m.x96)**2 + (m.x160 - m.x175)**2)**(-3) * (((
    m.x2 - m.x17)**2 + (m.x81 - m.x96)**2 + (m.x160 - m.x175)**2)**(-3) - 2) +
    ((m.x2 - m.x18)**2 + (m.x81 - m.x97)**2 + (m.x160 - m.x176)**2)**(-3) * (((
    m.x2 - m.x18)**2 + (m.x81 - m.x97)**2 + (m.x160 - m.x176)**2)**(-3) - 2) +
    ((m.x2 - m.x19)**2 + (m.x81 - m.x98)**2 + (m.x160 - m.x177)**2)**(-3) * (((
    m.x2 - m.x19)**2 + (m.x81 - m.x98)**2 + (m.x160 - m.x177)**2)**(-3) - 2) +
    ((m.x2 - m.x20)**2 + (m.x81 - m.x99)**2 + (m.x160 - m.x178)**2)**(-3) * (((
    m.x2 - m.x20)**2 + (m.x81 - m.x99)**2 + (m.x160 - m.x178)**2)**(-3) - 2) +
    ((m.x2 - m.x21)**2 + (m.x81 - m.x100)**2 + (m.x160 - m.x179)**2)**(-3) * ((
    (m.x2 - m.x21)**2 + (m.x81 - m.x100)**2 + (m.x160 - m.x179)**2)**(-3) - 2)
    + ((m.x2 - m.x22)**2 + (m.x81 - m.x101)**2 + (m.x160 - m.x180)**2)**(-3)
    * (((m.x2 - m.x22)**2 + (m.x81 - m.x101)**2 + (m.x160 - m.x180)**2)**(-3)
    - 2) + ((m.x2 - m.x23)**2 + (m.x81 - m.x102)**2 + (m.x160 - m.x181)**2)**(
    -3) * (((m.x2 - m.x23)**2 + (m.x81 - m.x102)**2 + (m.x160 - m.x181)**2)**(
    -3) - 2) + ((m.x2 - m.x24)**2 + (m.x81 - m.x103)**2 + (m.x160 - m.x182)**2)
    **(-3) * (((m.x2 - m.x24)**2 + (m.x81 - m.x103)**2 + (m.x160 - m.x182)**2)
    **(-3) - 2) + ((m.x2 - m.x25)**2 + (m.x81 - m.x104)**2 + (m.x160 - m.x183)
    **2)**(-3) * (((m.x2 - m.x25)**2 + (m.x81 - m.x104)**2 + (m.x160 - m.x183)
    **2)**(-3) - 2) + ((m.x2 - m.x26)**2 + (m.x81 - m.x105)**2 + (m.x160 -
    m.x184)**2)**(-3) * (((m.x2 - m.x26)**2 + (m.x81 - m.x105)**2 + (m.x160 -
    m.x184)**2)**(-3) - 2) + ((m.x2 - m.x27)**2 + (m.x81 - m.x106)**2 + (m.x160
    - m.x185)**2)**(-3) * (((m.x2 - m.x27)**2 + (m.x81 - m.x106)**2 + (m.x160
    - m.x185)**2)**(-3) - 2) + ((m.x2 - m.x28)**2 + (m.x81 - m.x107)**2 + (
    m.x160 - m.x186)**2)**(-3) * (((m.x2 - m.x28)**2 + (m.x81 - m.x107)**2 + (
    m.x160 - m.x186)**2)**(-3) - 2) + ((m.x2 - m.x29)**2 + (m.x81 - m.x108)**2
    + (m.x160 - m.x187)**2)**(-3) * (((m.x2 - m.x29)**2 + (m.x81 - m.x108)**2
    + (m.x160 - m.x187)**2)**(-3) - 2) + ((m.x2 - m.x30)**2 + (m.x81 - m.x109)
    **2 + (m.x160 - m.x188)**2)**(-3) * (((m.x2 - m.x30)**2 + (m.x81 - m.x109)
    **2 + (m.x160 - m.x188)**2)**(-3) - 2) + ((m.x2 - m.x31)**2 + (m.x81 -
    m.x110)**2 + (m.x160 - m.x189)**2)**(-3) * (((m.x2 - m.x31)**2 + (m.x81 -
    m.x110)**2 + (m.x160 - m.x189)**2)**(-3) - 2) + ((m.x2 - m.x32)**2 + (m.x81
    - m.x111)**2 + (m.x160 - m.x190)**2)**(-3) * (((m.x2 - m.x32)**2 + (m.x81
    - m.x111)**2 + (m.x160 - m.x190)**2)**(-3) - 2) + ((m.x2 - m.x33)**2 + (
    m.x81 - m.x112)**2 + (m.x160 - m.x191)**2)**(-3) * (((m.x2 - m.x33)**2 + (
    m.x81 - m.x112)**2 + (m.x160 - m.x191)**2)**(-3) - 2) + ((m.x2 - m.x34)**2
    + (m.x81 - m.x113)**2 + (m.x160 - m.x192)**2)**(-3) * (((m.x2 - m.x34)**2
    + (m.x81 - m.x113)**2 + (m.x160 - m.x192)**2)**(-3) - 2) + ((m.x2 - m.x35)
    **2 + (m.x81 - m.x114)**2 + (m.x160 - m.x193)**2)**(-3) * (((m.x2 - m.x35)
    **2 + (m.x81 - m.x114)**2 + (m.x160 - m.x193)**2)**(-3) - 2) + ((m.x2 -
    m.x36)**2 + (m.x81 - m.x115)**2 + (m.x160 - m.x194)**2)**(-3) * (((m.x2 -
    m.x36)**2 + (m.x81 - m.x115)**2 + (m.x160 - m.x194)**2)**(-3) - 2) + ((m.x2
    - m.x37)**2 + (m.x81 - m.x116)**2 + (m.x160 - m.x195)**2)**(-3) * (((m.x2
    - m.x37)**2 + (m.x81 - m.x116)**2 + (m.x160 - m.x195)**2)**(-3) - 2) + ((
    m.x2 - m.x38)**2 + (m.x81 - m.x117)**2 + (m.x160 - m.x196)**2)**(-3) * (((
    m.x2 - m.x38)**2 + (m.x81 - m.x117)**2 + (m.x160 - m.x196)**2)**(-3) - 2)
    + ((m.x2 - m.x39)**2 + (m.x81 - m.x118)**2 + (m.x160 - m.x197)**2)**(-3)
    * (((m.x2 - m.x39)**2 + (m.x81 - m.x118)**2 + (m.x160 - m.x197)**2)**(-3)
    - 2) + ((m.x2 - m.x40)**2 + (m.x81 - m.x119)**2 + (m.x160 - m.x198)**2)**(
    -3) * (((m.x2 - m.x40)**2 + (m.x81 - m.x119)**2 + (m.x160 - m.x198)**2)**(
    -3) - 2) + ((m.x2 - m.x41)**2 + (m.x81 - m.x120)**2 + (m.x160 - m.x199)**2)
    **(-3) * (((m.x2 - m.x41)**2 + (m.x81 - m.x120)**2 + (m.x160 - m.x199)**2)
    **(-3) - 2) + ((m.x2 - m.x42)**2 + (m.x81 - m.x121)**2 + (m.x160 - m.x200)
    **2)**(-3) * (((m.x2 - m.x42)**2 + (m.x81 - m.x121)**2 + (m.x160 - m.x200)
    **2)**(-3) - 2) + ((m.x2 - m.x43)**2 + (m.x81 - m.x122)**2 + (m.x160 -
    m.x201)**2)**(-3) * (((m.x2 - m.x43)**2 + (m.x81 - m.x122)**2 + (m.x160 -
    m.x201)**2)**(-3) - 2) + ((m.x2 - m.x44)**2 + (m.x81 - m.x123)**2 + (m.x160
    - m.x202)**2)**(-3) * (((m.x2 - m.x44)**2 + (m.x81 - m.x123)**2 + (m.x160
    - m.x202)**2)**(-3) - 2) + ((m.x2 - m.x45)**2 + (m.x81 - m.x124)**2 + (
    m.x160 - m.x203)**2)**(-3) * (((m.x2 - m.x45)**2 + (m.x81 - m.x124)**2 + (
    m.x160 - m.x203)**2)**(-3) - 2) + ((m.x2 - m.x46)**2 + (m.x81 - m.x125)**2
    + (m.x160 - m.x204)**2)**(-3) * (((m.x2 - m.x46)**2 + (m.x81 - m.x125)**2
    + (m.x160 - m.x204)**2)**(-3) - 2) + ((m.x2 - m.x47)**2 + (m.x81 - m.x126)
    **2 + (m.x160 - m.x205)**2)**(-3) * (((m.x2 - m.x47)**2 + (m.x81 - m.x126)
    **2 + (m.x160 - m.x205)**2)**(-3) - 2) + ((m.x2 - m.x48)**2 + (m.x81 -
    m.x127)**2 + (m.x160 - m.x206)**2)**(-3) * (((m.x2 - m.x48)**2 + (m.x81 -
    m.x127)**2 + (m.x160 - m.x206)**2)**(-3) - 2) + ((m.x2 - m.x49)**2 + (m.x81
    - m.x128)**2 + (m.x160 - m.x207)**2)**(-3) * (((m.x2 - m.x49)**2 + (m.x81
    - m.x128)**2 + (m.x160 - m.x207)**2)**(-3) - 2) + ((m.x2 - m.x50)**2 + (
    m.x81 - m.x129)**2 + (m.x160 - m.x208)**2)**(-3) * (((m.x2 - m.x50)**2 + (
    m.x81 - m.x129)**2 + (m.x160 - m.x208)**2)**(-3) - 2) + ((m.x2 - m.x51)**2
    + (m.x81 - m.x130)**2 + (m.x160 - m.x209)**2)**(-3) * (((m.x2 - m.x51)**2
    + (m.x81 - m.x130)**2 + (m.x160 - m.x209)**2)**(-3) - 2) + ((m.x2 - m.x52)
    **2 + (m.x81 - m.x131)**2 + (m.x160 - m.x210)**2)**(-3) * (((m.x2 - m.x52)
    **2 + (m.x81 - m.x131)**2 + (m.x160 - m.x210)**2)**(-3) - 2) + ((m.x2 -
    m.x53)**2 + (m.x81 - m.x132)**2 + (m.x160 - m.x211)**2)**(-3) * (((m.x2 -
    m.x53)**2 + (m.x81 - m.x132)**2 + (m.x160 - m.x211)**2)**(-3) - 2) + ((m.x2
    - m.x54)**2 + (m.x81 - m.x133)**2 + (m.x160 - m.x212)**2)**(-3) * (((m.x2
    - m.x54)**2 + (m.x81 - m.x133)**2 + (m.x160 - m.x212)**2)**(-3) - 2) + ((
    m.x2 - m.x55)**2 + (m.x81 - m.x134)**2 + (m.x160 - m.x213)**2)**(-3) * (((
    m.x2 - m.x55)**2 + (m.x81 - m.x134)**2 + (m.x160 - m.x213)**2)**(-3) - 2)
    + ((m.x2 - m.x56)**2 + (m.x81 - m.x135)**2 + (m.x160 - m.x214)**2)**(-3)
    * (((m.x2 - m.x56)**2 + (m.x81 - m.x135)**2 + (m.x160 - m.x214)**2)**(-3)
    - 2) + ((m.x2 - m.x57)**2 + (m.x81 - m.x136)**2 + (m.x160 - m.x215)**2)**(
    -3) * (((m.x2 - m.x57)**2 + (m.x81 - m.x136)**2 + (m.x160 - m.x215)**2)**(
    -3) - 2) + ((m.x2 - m.x58)**2 + (m.x81 - m.x137)**2 + (m.x160 - m.x216)**2)
    **(-3) * (((m.x2 - m.x58)**2 + (m.x81 - m.x137)**2 + (m.x160 - m.x216)**2)
    **(-3) - 2) + ((m.x2 - m.x59)**2 + (m.x81 - m.x138)**2 + (m.x160 - m.x217)
    **2)**(-3) * (((m.x2 - m.x59)**2 + (m.x81 - m.x138)**2 + (m.x160 - m.x217)
    **2)**(-3) - 2) + ((m.x2 - m.x60)**2 + (m.x81 - m.x139)**2 + (m.x160 -
    m.x218)**2)**(-3) * (((m.x2 - m.x60)**2 + (m.x81 - m.x139)**2 + (m.x160 -
    m.x218)**2)**(-3) - 2) + ((m.x2 - m.x61)**2 + (m.x81 - m.x140)**2 + (m.x160
    - m.x219)**2)**(-3) * (((m.x2 - m.x61)**2 + (m.x81 - m.x140)**2 + (m.x160
    - m.x219)**2)**(-3) - 2) + ((m.x2 - m.x62)**2 + (m.x81 - m.x141)**2 + (
    m.x160 - m.x220)**2)**(-3) * (((m.x2 - m.x62)**2 + (m.x81 - m.x141)**2 + (
    m.x160 - m.x220)**2)**(-3) - 2) + ((m.x2 - m.x63)**2 + (m.x81 - m.x142)**2
    + (m.x160 - m.x221)**2)**(-3) * (((m.x2 - m.x63)**2 + (m.x81 - m.x142)**2
    + (m.x160 - m.x221)**2)**(-3) - 2) + ((m.x2 - m.x64)**2 + (m.x81 - m.x143)
    **2 + (m.x160 - m.x222)**2)**(-3) * (((m.x2 - m.x64)**2 + (m.x81 - m.x143)
    **2 + (m.x160 - m.x222)**2)**(-3) - 2) + ((m.x2 - m.x65)**2 + (m.x81 -
    m.x144)**2 + (m.x160 - m.x223)**2)**(-3) * (((m.x2 - m.x65)**2 + (m.x81 -
    m.x144)**2 + (m.x160 - m.x223)**2)**(-3) - 2) + ((m.x2 - m.x66)**2 + (m.x81
    - m.x145)**2 + (m.x160 - m.x224)**2)**(-3) * (((m.x2 - m.x66)**2 + (m.x81
    - m.x145)**2 + (m.x160 - m.x224)**2)**(-3) - 2) + ((m.x2 - m.x67)**2 + (
    m.x81 - m.x146)**2 + (m.x160 - m.x225)**2)**(-3) * (((m.x2 - m.x67)**2 + (
    m.x81 - m.x146)**2 + (m.x160 - m.x225)**2)**(-3) - 2) + ((m.x2 - m.x68)**2
    + (m.x81 - m.x147)**2 + (m.x160 - m.x226)**2)**(-3) * (((m.x2 - m.x68)**2
    + (m.x81 - m.x147)**2 + (m.x160 - m.x226)**2)**(-3) - 2) + ((m.x2 - m.x69)
    **2 + (m.x81 - m.x148)**2 + (m.x160 - m.x227)**2)**(-3) * (((m.x2 - m.x69)
    **2 + (m.x81 - m.x148)**2 + (m.x160 - m.x227)**2)**(-3) - 2) + ((m.x2 -
    m.x70)**2 + (m.x81 - m.x149)**2 + (m.x160 - m.x228)**2)**(-3) * (((m.x2 -
    m.x70)**2 + (m.x81 - m.x149)**2 + (m.x160 - m.x228)**2)**(-3) - 2) + ((m.x2
    - m.x71)**2 + (m.x81 - m.x150)**2 + (m.x160 - m.x229)**2)**(-3) * (((m.x2
    - m.x71)**2 + (m.x81 - m.x150)**2 + (m.x160 - m.x229)**2)**(-3) - 2) + ((
    m.x2 - m.x72)**2 + (m.x81 - m.x151)**2 + (m.x160 - m.x230)**2)**(-3) * (((
    m.x2 - m.x72)**2 + (m.x81 - m.x151)**2 + (m.x160 - m.x230)**2)**(-3) - 2)
    + ((m.x2 - m.x73)**2 + (m.x81 - m.x152)**2 + (m.x160 - m.x231)**2)**(-3)
    * (((m.x2 - m.x73)**2 + (m.x81 - m.x152)**2 + (m.x160 - m.x231)**2)**(-3)
    - 2) + ((m.x2 - m.x74)**2 + (m.x81 - m.x153)**2 + (m.x160 - m.x232)**2)**(
    -3) * (((m.x2 - m.x74)**2 + (m.x81 - m.x153)**2 + (m.x160 - m.x232)**2)**(
    -3) - 2) + ((m.x2 - m.x75)**2 + (m.x81 - m.x154)**2 + (m.x160 - m.x233)**2)
    **(-3) * (((m.x2 - m.x75)**2 + (m.x81 - m.x154)**2 + (m.x160 - m.x233)**2)
    **(-3) - 2) + ((m.x2 - m.x76)**2 + (m.x81 - m.x155)**2 + (m.x160 - m.x234)
    **2)**(-3) * (((m.x2 - m.x76)**2 + (m.x81 - m.x155)**2 + (m.x160 - m.x234)
    **2)**(-3) - 2) + ((m.x2 - m.x77)**2 + (m.x81 - m.x156)**2 + (m.x160 -
    m.x235)**2)**(-3) * (((m.x2 - m.x77)**2 + (m.x81 - m.x156)**2 + (m.x160 -
    m.x235)**2)**(-3) - 2) + ((m.x2 - m.x78)**2 + (m.x81 - m.x157)**2 + (m.x160
    - m.x236)**2)**(-3) * (((m.x2 - m.x78)**2 + (m.x81 - m.x157)**2 + (m.x160
    - m.x236)**2)**(-3) - 2) + ((m.x2 - m.x79)**2 + (m.x81 - m.x158)**2 + (
    m.x160 - m.x237)**2)**(-3) * (((m.x2 - m.x79)**2 + (m.x81 - m.x158)**2 + (
    m.x160 - m.x237)**2)**(-3) - 2) + ((m.x3 - m.x4)**2 + (m.x82 - m.x83)**2 +
    (m.x161 - m.x162)**2)**(-3) * (((m.x3 - m.x4)**2 + (m.x82 - m.x83)**2 + (
    m.x161 - m.x162)**2)**(-3) - 2) + ((m.x3 - m.x5)**2 + (m.x82 - m.x84)**2 +
    (m.x161 - m.x163)**2)**(-3) * (((m.x3 - m.x5)**2 + (m.x82 - m.x84)**2 + (
    m.x161 - m.x163)**2)**(-3) - 2) + ((m.x3 - m.x6)**2 + (m.x82 - m.x85)**2 +
    (m.x161 - m.x164)**2)**(-3) * (((m.x3 - m.x6)**2 + (m.x82 - m.x85)**2 + (
    m.x161 - m.x164)**2)**(-3) - 2) + ((m.x3 - m.x7)**2 + (m.x82 - m.x86)**2 +
    (m.x161 - m.x165)**2)**(-3) * (((m.x3 - m.x7)**2 + (m.x82 - m.x86)**2 + (
    m.x161 - m.x165)**2)**(-3) - 2) + ((m.x3 - m.x8)**2 + (m.x82 - m.x87)**2 +
    (m.x161 - m.x166)**2)**(-3) * (((m.x3 - m.x8)**2 + (m.x82 - m.x87)**2 + (
    m.x161 - m.x166)**2)**(-3) - 2) + ((m.x3 - m.x9)**2 + (m.x82 - m.x88)**2 +
    (m.x161 - m.x167)**2)**(-3) * (((m.x3 - m.x9)**2 + (m.x82 - m.x88)**2 + (
    m.x161 - m.x167)**2)**(-3) - 2) + ((m.x3 - m.x10)**2 + (m.x82 - m.x89)**2
    + (m.x161 - m.x168)**2)**(-3) * (((m.x3 - m.x10)**2 + (m.x82 - m.x89)**2
    + (m.x161 - m.x168)**2)**(-3) - 2) + ((m.x3 - m.x11)**2 + (m.x82 - m.x90)
    **2 + (m.x161 - m.x169)**2)**(-3) * (((m.x3 - m.x11)**2 + (m.x82 - m.x90)**
    2 + (m.x161 - m.x169)**2)**(-3) - 2) + ((m.x3 - m.x12)**2 + (m.x82 - m.x91)
    **2 + (m.x161 - m.x170)**2)**(-3) * (((m.x3 - m.x12)**2 + (m.x82 - m.x91)**
    2 + (m.x161 - m.x170)**2)**(-3) - 2) + ((m.x3 - m.x13)**2 + (m.x82 - m.x92)
    **2 + (m.x161 - m.x171)**2)**(-3) * (((m.x3 - m.x13)**2 + (m.x82 - m.x92)**
    2 + (m.x161 - m.x171)**2)**(-3) - 2) + ((m.x3 - m.x14)**2 + (m.x82 - m.x93)
    **2 + (m.x161 - m.x172)**2)**(-3) * (((m.x3 - m.x14)**2 + (m.x82 - m.x93)**
    2 + (m.x161 - m.x172)**2)**(-3) - 2) + ((m.x3 - m.x15)**2 + (m.x82 - m.x94)
    **2 + (m.x161 - m.x173)**2)**(-3) * (((m.x3 - m.x15)**2 + (m.x82 - m.x94)**
    2 + (m.x161 - m.x173)**2)**(-3) - 2) + ((m.x3 - m.x16)**2 + (m.x82 - m.x95)
    **2 + (m.x161 - m.x174)**2)**(-3) * (((m.x3 - m.x16)**2 + (m.x82 - m.x95)**
    2 + (m.x161 - m.x174)**2)**(-3) - 2) + ((m.x3 - m.x17)**2 + (m.x82 - m.x96)
    **2 + (m.x161 - m.x175)**2)**(-3) * (((m.x3 - m.x17)**2 + (m.x82 - m.x96)**
    2 + (m.x161 - m.x175)**2)**(-3) - 2) + ((m.x3 - m.x18)**2 + (m.x82 - m.x97)
    **2 + (m.x161 - m.x176)**2)**(-3) * (((m.x3 - m.x18)**2 + (m.x82 - m.x97)**
    2 + (m.x161 - m.x176)**2)**(-3) - 2) + ((m.x3 - m.x19)**2 + (m.x82 - m.x98)
    **2 + (m.x161 - m.x177)**2)**(-3) * (((m.x3 - m.x19)**2 + (m.x82 - m.x98)**
    2 + (m.x161 - m.x177)**2)**(-3) - 2) + ((m.x3 - m.x20)**2 + (m.x82 - m.x99)
    **2 + (m.x161 - m.x178)**2)**(-3) * (((m.x3 - m.x20)**2 + (m.x82 - m.x99)**
    2 + (m.x161 - m.x178)**2)**(-3) - 2) + ((m.x3 - m.x21)**2 + (m.x82 - m.x100)
    **2 + (m.x161 - m.x179)**2)**(-3) * (((m.x3 - m.x21)**2 + (m.x82 - m.x100)
    **2 + (m.x161 - m.x179)**2)**(-3) - 2) + ((m.x3 - m.x22)**2 + (m.x82 -
    m.x101)**2 + (m.x161 - m.x180)**2)**(-3) * (((m.x3 - m.x22)**2 + (m.x82 -
    m.x101)**2 + (m.x161 - m.x180)**2)**(-3) - 2) + ((m.x3 - m.x23)**2 + (m.x82
    - m.x102)**2 + (m.x161 - m.x181)**2)**(-3) * (((m.x3 - m.x23)**2 + (m.x82
    - m.x102)**2 + (m.x161 - m.x181)**2)**(-3) - 2) + ((m.x3 - m.x24)**2 + (
    m.x82 - m.x103)**2 + (m.x161 - m.x182)**2)**(-3) * (((m.x3 - m.x24)**2 + (
    m.x82 - m.x103)**2 + (m.x161 - m.x182)**2)**(-3) - 2) + ((m.x3 - m.x25)**2
    + (m.x82 - m.x104)**2 + (m.x161 - m.x183)**2)**(-3) * (((m.x3 - m.x25)**2
    + (m.x82 - m.x104)**2 + (m.x161 - m.x183)**2)**(-3) - 2) + ((m.x3 - m.x26)
    **2 + (m.x82 - m.x105)**2 + (m.x161 - m.x184)**2)**(-3) * (((m.x3 - m.x26)
    **2 + (m.x82 - m.x105)**2 + (m.x161 - m.x184)**2)**(-3) - 2) + ((m.x3 -
    m.x27)**2 + (m.x82 - m.x106)**2 + (m.x161 - m.x185)**2)**(-3) * (((m.x3 -
    m.x27)**2 + (m.x82 - m.x106)**2 + (m.x161 - m.x185)**2)**(-3) - 2) + ((m.x3
    - m.x28)**2 + (m.x82 - m.x107)**2 + (m.x161 - m.x186)**2)**(-3) * (((m.x3
    - m.x28)**2 + (m.x82 - m.x107)**2 + (m.x161 - m.x186)**2)**(-3) - 2) + ((
    m.x3 - m.x29)**2 + (m.x82 - m.x108)**2 + (m.x161 - m.x187)**2)**(-3) * (((
    m.x3 - m.x29)**2 + (m.x82 - m.x108)**2 + (m.x161 - m.x187)**2)**(-3) - 2)
    + ((m.x3 - m.x30)**2 + (m.x82 - m.x109)**2 + (m.x161 - m.x188)**2)**(-3)
    * (((m.x3 - m.x30)**2 + (m.x82 - m.x109)**2 + (m.x161 - m.x188)**2)**(-3)
    - 2) + ((m.x3 - m.x31)**2 + (m.x82 - m.x110)**2 + (m.x161 - m.x189)**2)**(
    -3) * (((m.x3 - m.x31)**2 + (m.x82 - m.x110)**2 + (m.x161 - m.x189)**2)**(
    -3) - 2) + ((m.x3 - m.x32)**2 + (m.x82 - m.x111)**2 + (m.x161 - m.x190)**2)
    **(-3) * (((m.x3 - m.x32)**2 + (m.x82 - m.x111)**2 + (m.x161 - m.x190)**2)
    **(-3) - 2) + ((m.x3 - m.x33)**2 + (m.x82 - m.x112)**2 + (m.x161 - m.x191)
    **2)**(-3) * (((m.x3 - m.x33)**2 + (m.x82 - m.x112)**2 + (m.x161 - m.x191)
    **2)**(-3) - 2) + ((m.x3 - m.x34)**2 + (m.x82 - m.x113)**2 + (m.x161 -
    m.x192)**2)**(-3) * (((m.x3 - m.x34)**2 + (m.x82 - m.x113)**2 + (m.x161 -
    m.x192)**2)**(-3) - 2) + ((m.x3 - m.x35)**2 + (m.x82 - m.x114)**2 + (m.x161
    - m.x193)**2)**(-3) * (((m.x3 - m.x35)**2 + (m.x82 - m.x114)**2 + (m.x161
    - m.x193)**2)**(-3) - 2) + ((m.x3 - m.x36)**2 + (m.x82 - m.x115)**2 + (
    m.x161 - m.x194)**2)**(-3) * (((m.x3 - m.x36)**2 + (m.x82 - m.x115)**2 + (
    m.x161 - m.x194)**2)**(-3) - 2) + ((m.x3 - m.x37)**2 + (m.x82 - m.x116)**2
    + (m.x161 - m.x195)**2)**(-3) * (((m.x3 - m.x37)**2 + (m.x82 - m.x116)**2
    + (m.x161 - m.x195)**2)**(-3) - 2) + ((m.x3 - m.x38)**2 + (m.x82 - m.x117)
    **2 + (m.x161 - m.x196)**2)**(-3) * (((m.x3 - m.x38)**2 + (m.x82 - m.x117)
    **2 + (m.x161 - m.x196)**2)**(-3) - 2) + ((m.x3 - m.x39)**2 + (m.x82 -
    m.x118)**2 + (m.x161 - m.x197)**2)**(-3) * (((m.x3 - m.x39)**2 + (m.x82 -
    m.x118)**2 + (m.x161 - m.x197)**2)**(-3) - 2) + ((m.x3 - m.x40)**2 + (m.x82
    - m.x119)**2 + (m.x161 - m.x198)**2)**(-3) * (((m.x3 - m.x40)**2 + (m.x82
    - m.x119)**2 + (m.x161 - m.x198)**2)**(-3) - 2) + ((m.x3 - m.x41)**2 + (
    m.x82 - m.x120)**2 + (m.x161 - m.x199)**2)**(-3) * (((m.x3 - m.x41)**2 + (
    m.x82 - m.x120)**2 + (m.x161 - m.x199)**2)**(-3) - 2) + ((m.x3 - m.x42)**2
    + (m.x82 - m.x121)**2 + (m.x161 - m.x200)**2)**(-3) * (((m.x3 - m.x42)**2
    + (m.x82 - m.x121)**2 + (m.x161 - m.x200)**2)**(-3) - 2) + ((m.x3 - m.x43)
    **2 + (m.x82 - m.x122)**2 + (m.x161 - m.x201)**2)**(-3) * (((m.x3 - m.x43)
    **2 + (m.x82 - m.x122)**2 + (m.x161 - m.x201)**2)**(-3) - 2) + ((m.x3 -
    m.x44)**2 + (m.x82 - m.x123)**2 + (m.x161 - m.x202)**2)**(-3) * (((m.x3 -
    m.x44)**2 + (m.x82 - m.x123)**2 + (m.x161 - m.x202)**2)**(-3) - 2) + ((m.x3
    - m.x45)**2 + (m.x82 - m.x124)**2 + (m.x161 - m.x203)**2)**(-3) * (((m.x3
    - m.x45)**2 + (m.x82 - m.x124)**2 + (m.x161 - m.x203)**2)**(-3) - 2) + ((
    m.x3 - m.x46)**2 + (m.x82 - m.x125)**2 + (m.x161 - m.x204)**2)**(-3) * (((
    m.x3 - m.x46)**2 + (m.x82 - m.x125)**2 + (m.x161 - m.x204)**2)**(-3) - 2)
    + ((m.x3 - m.x47)**2 + (m.x82 - m.x126)**2 + (m.x161 - m.x205)**2)**(-3)
    * (((m.x3 - m.x47)**2 + (m.x82 - m.x126)**2 + (m.x161 - m.x205)**2)**(-3)
    - 2) + ((m.x3 - m.x48)**2 + (m.x82 - m.x127)**2 + (m.x161 - m.x206)**2)**(
    -3) * (((m.x3 - m.x48)**2 + (m.x82 - m.x127)**2 + (m.x161 - m.x206)**2)**(
    -3) - 2) + ((m.x3 - m.x49)**2 + (m.x82 - m.x128)**2 + (m.x161 - m.x207)**2)
    **(-3) * (((m.x3 - m.x49)**2 + (m.x82 - m.x128)**2 + (m.x161 - m.x207)**2)
    **(-3) - 2) + ((m.x3 - m.x50)**2 + (m.x82 - m.x129)**2 + (m.x161 - m.x208)
    **2)**(-3) * (((m.x3 - m.x50)**2 + (m.x82 - m.x129)**2 + (m.x161 - m.x208)
    **2)**(-3) - 2) + ((m.x3 - m.x51)**2 + (m.x82 - m.x130)**2 + (m.x161 -
    m.x209)**2)**(-3) * (((m.x3 - m.x51)**2 + (m.x82 - m.x130)**2 + (m.x161 -
    m.x209)**2)**(-3) - 2) + ((m.x3 - m.x52)**2 + (m.x82 - m.x131)**2 + (m.x161
    - m.x210)**2)**(-3) * (((m.x3 - m.x52)**2 + (m.x82 - m.x131)**2 + (m.x161
    - m.x210)**2)**(-3) - 2) + ((m.x3 - m.x53)**2 + (m.x82 - m.x132)**2 + (
    m.x161 - m.x211)**2)**(-3) * (((m.x3 - m.x53)**2 + (m.x82 - m.x132)**2 + (
    m.x161 - m.x211)**2)**(-3) - 2) + ((m.x3 - m.x54)**2 + (m.x82 - m.x133)**2
    + (m.x161 - m.x212)**2)**(-3) * (((m.x3 - m.x54)**2 + (m.x82 - m.x133)**2
    + (m.x161 - m.x212)**2)**(-3) - 2) + ((m.x3 - m.x55)**2 + (m.x82 - m.x134)
    **2 + (m.x161 - m.x213)**2)**(-3) * (((m.x3 - m.x55)**2 + (m.x82 - m.x134)
    **2 + (m.x161 - m.x213)**2)**(-3) - 2) + ((m.x3 - m.x56)**2 + (m.x82 -
    m.x135)**2 + (m.x161 - m.x214)**2)**(-3) * (((m.x3 - m.x56)**2 + (m.x82 -
    m.x135)**2 + (m.x161 - m.x214)**2)**(-3) - 2) + ((m.x3 - m.x57)**2 + (m.x82
    - m.x136)**2 + (m.x161 - m.x215)**2)**(-3) * (((m.x3 - m.x57)**2 + (m.x82
    - m.x136)**2 + (m.x161 - m.x215)**2)**(-3) - 2) + ((m.x3 - m.x58)**2 + (
    m.x82 - m.x137)**2 + (m.x161 - m.x216)**2)**(-3) * (((m.x3 - m.x58)**2 + (
    m.x82 - m.x137)**2 + (m.x161 - m.x216)**2)**(-3) - 2) + ((m.x3 - m.x59)**2
    + (m.x82 - m.x138)**2 + (m.x161 - m.x217)**2)**(-3) * (((m.x3 - m.x59)**2
    + (m.x82 - m.x138)**2 + (m.x161 - m.x217)**2)**(-3) - 2) + ((m.x3 - m.x60)
    **2 + (m.x82 - m.x139)**2 + (m.x161 - m.x218)**2)**(-3) * (((m.x3 - m.x60)
    **2 + (m.x82 - m.x139)**2 + (m.x161 - m.x218)**2)**(-3) - 2) + ((m.x3 -
    m.x61)**2 + (m.x82 - m.x140)**2 + (m.x161 - m.x219)**2)**(-3) * (((m.x3 -
    m.x61)**2 + (m.x82 - m.x140)**2 + (m.x161 - m.x219)**2)**(-3) - 2) + ((m.x3
    - m.x62)**2 + (m.x82 - m.x141)**2 + (m.x161 - m.x220)**2)**(-3) * (((m.x3
    - m.x62)**2 + (m.x82 - m.x141)**2 + (m.x161 - m.x220)**2)**(-3) - 2) + ((
    m.x3 - m.x63)**2 + (m.x82 - m.x142)**2 + (m.x161 - m.x221)**2)**(-3) * (((
    m.x3 - m.x63)**2 + (m.x82 - m.x142)**2 + (m.x161 - m.x221)**2)**(-3) - 2)
    + ((m.x3 - m.x64)**2 + (m.x82 - m.x143)**2 + (m.x161 - m.x222)**2)**(-3)
    * (((m.x3 - m.x64)**2 + (m.x82 - m.x143)**2 + (m.x161 - m.x222)**2)**(-3)
    - 2) + ((m.x3 - m.x65)**2 + (m.x82 - m.x144)**2 + (m.x161 - m.x223)**2)**(
    -3) * (((m.x3 - m.x65)**2 + (m.x82 - m.x144)**2 + (m.x161 - m.x223)**2)**(
    -3) - 2) + ((m.x3 - m.x66)**2 + (m.x82 - m.x145)**2 + (m.x161 - m.x224)**2)
    **(-3) * (((m.x3 - m.x66)**2 + (m.x82 - m.x145)**2 + (m.x161 - m.x224)**2)
    **(-3) - 2) + ((m.x3 - m.x67)**2 + (m.x82 - m.x146)**2 + (m.x161 - m.x225)
    **2)**(-3) * (((m.x3 - m.x67)**2 + (m.x82 - m.x146)**2 + (m.x161 - m.x225)
    **2)**(-3) - 2) + ((m.x3 - m.x68)**2 + (m.x82 - m.x147)**2 + (m.x161 -
    m.x226)**2)**(-3) * (((m.x3 - m.x68)**2 + (m.x82 - m.x147)**2 + (m.x161 -
    m.x226)**2)**(-3) - 2) + ((m.x3 - m.x69)**2 + (m.x82 - m.x148)**2 + (m.x161
    - m.x227)**2)**(-3) * (((m.x3 - m.x69)**2 + (m.x82 - m.x148)**2 + (m.x161
    - m.x227)**2)**(-3) - 2) + ((m.x3 - m.x70)**2 + (m.x82 - m.x149)**2 + (
    m.x161 - m.x228)**2)**(-3) * (((m.x3 - m.x70)**2 + (m.x82 - m.x149)**2 + (
    m.x161 - m.x228)**2)**(-3) - 2) + ((m.x3 - m.x71)**2 + (m.x82 - m.x150)**2
    + (m.x161 - m.x229)**2)**(-3) * (((m.x3 - m.x71)**2 + (m.x82 - m.x150)**2
    + (m.x161 - m.x229)**2)**(-3) - 2) + ((m.x3 - m.x72)**2 + (m.x82 - m.x151)
    **2 + (m.x161 - m.x230)**2)**(-3) * (((m.x3 - m.x72)**2 + (m.x82 - m.x151)
    **2 + (m.x161 - m.x230)**2)**(-3) - 2) + ((m.x3 - m.x73)**2 + (m.x82 -
    m.x152)**2 + (m.x161 - m.x231)**2)**(-3) * (((m.x3 - m.x73)**2 + (m.x82 -
    m.x152)**2 + (m.x161 - m.x231)**2)**(-3) - 2) + ((m.x3 - m.x74)**2 + (m.x82
    - m.x153)**2 + (m.x161 - m.x232)**2)**(-3) * (((m.x3 - m.x74)**2 + (m.x82
    - m.x153)**2 + (m.x161 - m.x232)**2)**(-3) - 2) + ((m.x3 - m.x75)**2 + (
    m.x82 - m.x154)**2 + (m.x161 - m.x233)**2)**(-3) * (((m.x3 - m.x75)**2 + (
    m.x82 - m.x154)**2 + (m.x161 - m.x233)**2)**(-3) - 2) + ((m.x3 - m.x76)**2
    + (m.x82 - m.x155)**2 + (m.x161 - m.x234)**2)**(-3) * (((m.x3 - m.x76)**2
    + (m.x82 - m.x155)**2 + (m.x161 - m.x234)**2)**(-3) - 2) + ((m.x3 - m.x77)
    **2 + (m.x82 - m.x156)**2 + (m.x161 - m.x235)**2)**(-3) * (((m.x3 - m.x77)
    **2 + (m.x82 - m.x156)**2 + (m.x161 - m.x235)**2)**(-3) - 2) + ((m.x3 -
    m.x78)**2 + (m.x82 - m.x157)**2 + (m.x161 - m.x236)**2)**(-3) * (((m.x3 -
    m.x78)**2 + (m.x82 - m.x157)**2 + (m.x161 - m.x236)**2)**(-3) - 2) + ((m.x3
    - m.x79)**2 + (m.x82 - m.x158)**2 + (m.x161 - m.x237)**2)**(-3) * (((m.x3
    - m.x79)**2 + (m.x82 - m.x158)**2 + (m.x161 - m.x237)**2)**(-3) - 2) + ((
    m.x4 - m.x5)**2 + (m.x83 - m.x84)**2 + (m.x162 - m.x163)**2)**(-3) * (((
    m.x4 - m.x5)**2 + (m.x83 - m.x84)**2 + (m.x162 - m.x163)**2)**(-3) - 2) + (
    (m.x4 - m.x6)**2 + (m.x83 - m.x85)**2 + (m.x162 - m.x164)**2)**(-3) * (((
    m.x4 - m.x6)**2 + (m.x83 - m.x85)**2 + (m.x162 - m.x164)**2)**(-3) - 2) + (
    (m.x4 - m.x7)**2 + (m.x83 - m.x86)**2 + (m.x162 - m.x165)**2)**(-3) * (((
    m.x4 - m.x7)**2 + (m.x83 - m.x86)**2 + (m.x162 - m.x165)**2)**(-3) - 2) + (
    (m.x4 - m.x8)**2 + (m.x83 - m.x87)**2 + (m.x162 - m.x166)**2)**(-3) * (((
    m.x4 - m.x8)**2 + (m.x83 - m.x87)**2 + (m.x162 - m.x166)**2)**(-3) - 2) + (
    (m.x4 - m.x9)**2 + (m.x83 - m.x88)**2 + (m.x162 - m.x167)**2)**(-3) * (((
    m.x4 - m.x9)**2 + (m.x83 - m.x88)**2 + (m.x162 - m.x167)**2)**(-3) - 2) + (
    (m.x4 - m.x10)**2 + (m.x83 - m.x89)**2 + (m.x162 - m.x168)**2)**(-3) * (((
    m.x4 - m.x10)**2 + (m.x83 - m.x89)**2 + (m.x162 - m.x168)**2)**(-3) - 2) +
    ((m.x4 - m.x11)**2 + (m.x83 - m.x90)**2 + (m.x162 - m.x169)**2)**(-3) * (((
    m.x4 - m.x11)**2 + (m.x83 - m.x90)**2 + (m.x162 - m.x169)**2)**(-3) - 2) +
    ((m.x4 - m.x12)**2 + (m.x83 - m.x91)**2 + (m.x162 - m.x170)**2)**(-3) * (((
    m.x4 - m.x12)**2 + (m.x83 - m.x91)**2 + (m.x162 - m.x170)**2)**(-3) - 2) +
    ((m.x4 - m.x13)**2 + (m.x83 - m.x92)**2 + (m.x162 - m.x171)**2)**(-3) * (((
    m.x4 - m.x13)**2 + (m.x83 - m.x92)**2 + (m.x162 - m.x171)**2)**(-3) - 2) +
    ((m.x4 - m.x14)**2 + (m.x83 - m.x93)**2 + (m.x162 - m.x172)**2)**(-3) * (((
    m.x4 - m.x14)**2 + (m.x83 - m.x93)**2 + (m.x162 - m.x172)**2)**(-3) - 2) +
    ((m.x4 - m.x15)**2 + (m.x83 - m.x94)**2 + (m.x162 - m.x173)**2)**(-3) * (((
    m.x4 - m.x15)**2 + (m.x83 - m.x94)**2 + (m.x162 - m.x173)**2)**(-3) - 2) +
    ((m.x4 - m.x16)**2 + (m.x83 - m.x95)**2 + (m.x162 - m.x174)**2)**(-3) * (((
    m.x4 - m.x16)**2 + (m.x83 - m.x95)**2 + (m.x162 - m.x174)**2)**(-3) - 2) +
    ((m.x4 - m.x17)**2 + (m.x83 - m.x96)**2 + (m.x162 - m.x175)**2)**(-3) * (((
    m.x4 - m.x17)**2 + (m.x83 - m.x96)**2 + (m.x162 - m.x175)**2)**(-3) - 2) +
    ((m.x4 - m.x18)**2 + (m.x83 - m.x97)**2 + (m.x162 - m.x176)**2)**(-3) * (((
    m.x4 - m.x18)**2 + (m.x83 - m.x97)**2 + (m.x162 - m.x176)**2)**(-3) - 2) +
    ((m.x4 - m.x19)**2 + (m.x83 - m.x98)**2 + (m.x162 - m.x177)**2)**(-3) * (((
    m.x4 - m.x19)**2 + (m.x83 - m.x98)**2 + (m.x162 - m.x177)**2)**(-3) - 2) +
    ((m.x4 - m.x20)**2 + (m.x83 - m.x99)**2 + (m.x162 - m.x178)**2)**(-3) * (((
    m.x4 - m.x20)**2 + (m.x83 - m.x99)**2 + (m.x162 - m.x178)**2)**(-3) - 2) +
    ((m.x4 - m.x21)**2 + (m.x83 - m.x100)**2 + (m.x162 - m.x179)**2)**(-3) * ((
    (m.x4 - m.x21)**2 + (m.x83 - m.x100)**2 + (m.x162 - m.x179)**2)**(-3) - 2)
    + ((m.x4 - m.x22)**2 + (m.x83 - m.x101)**2 + (m.x162 - m.x180)**2)**(-3)
    * (((m.x4 - m.x22)**2 + (m.x83 - m.x101)**2 + (m.x162 - m.x180)**2)**(-3)
    - 2) + ((m.x4 - m.x23)**2 + (m.x83 - m.x102)**2 + (m.x162 - m.x181)**2)**(
    -3) * (((m.x4 - m.x23)**2 + (m.x83 - m.x102)**2 + (m.x162 - m.x181)**2)**(
    -3) - 2) + ((m.x4 - m.x24)**2 + (m.x83 - m.x103)**2 + (m.x162 - m.x182)**2)
    **(-3) * (((m.x4 - m.x24)**2 + (m.x83 - m.x103)**2 + (m.x162 - m.x182)**2)
    **(-3) - 2) + ((m.x4 - m.x25)**2 + (m.x83 - m.x104)**2 + (m.x162 - m.x183)
    **2)**(-3) * (((m.x4 - m.x25)**2 + (m.x83 - m.x104)**2 + (m.x162 - m.x183)
    **2)**(-3) - 2) + ((m.x4 - m.x26)**2 + (m.x83 - m.x105)**2 + (m.x162 -
    m.x184)**2)**(-3) * (((m.x4 - m.x26)**2 + (m.x83 - m.x105)**2 + (m.x162 -
    m.x184)**2)**(-3) - 2) + ((m.x4 - m.x27)**2 + (m.x83 - m.x106)**2 + (m.x162
    - m.x185)**2)**(-3) * (((m.x4 - m.x27)**2 + (m.x83 - m.x106)**2 + (m.x162
    - m.x185)**2)**(-3) - 2) + ((m.x4 - m.x28)**2 + (m.x83 - m.x107)**2 + (
    m.x162 - m.x186)**2)**(-3) * (((m.x4 - m.x28)**2 + (m.x83 - m.x107)**2 + (
    m.x162 - m.x186)**2)**(-3) - 2) + ((m.x4 - m.x29)**2 + (m.x83 - m.x108)**2
    + (m.x162 - m.x187)**2)**(-3) * (((m.x4 - m.x29)**2 + (m.x83 - m.x108)**2
    + (m.x162 - m.x187)**2)**(-3) - 2) + ((m.x4 - m.x30)**2 + (m.x83 - m.x109)
    **2 + (m.x162 - m.x188)**2)**(-3) * (((m.x4 - m.x30)**2 + (m.x83 - m.x109)
    **2 + (m.x162 - m.x188)**2)**(-3) - 2) + ((m.x4 - m.x31)**2 + (m.x83 -
    m.x110)**2 + (m.x162 - m.x189)**2)**(-3) * (((m.x4 - m.x31)**2 + (m.x83 -
    m.x110)**2 + (m.x162 - m.x189)**2)**(-3) - 2) + ((m.x4 - m.x32)**2 + (m.x83
    - m.x111)**2 + (m.x162 - m.x190)**2)**(-3) * (((m.x4 - m.x32)**2 + (m.x83
    - m.x111)**2 + (m.x162 - m.x190)**2)**(-3) - 2) + ((m.x4 - m.x33)**2 + (
    m.x83 - m.x112)**2 + (m.x162 - m.x191)**2)**(-3) * (((m.x4 - m.x33)**2 + (
    m.x83 - m.x112)**2 + (m.x162 - m.x191)**2)**(-3) - 2) + ((m.x4 - m.x34)**2
    + (m.x83 - m.x113)**2 + (m.x162 - m.x192)**2)**(-3) * (((m.x4 - m.x34)**2
    + (m.x83 - m.x113)**2 + (m.x162 - m.x192)**2)**(-3) - 2) + ((m.x4 - m.x35)
    **2 + (m.x83 - m.x114)**2 + (m.x162 - m.x193)**2)**(-3) * (((m.x4 - m.x35)
    **2 + (m.x83 - m.x114)**2 + (m.x162 - m.x193)**2)**(-3) - 2) + ((m.x4 -
    m.x36)**2 + (m.x83 - m.x115)**2 + (m.x162 - m.x194)**2)**(-3) * (((m.x4 -
    m.x36)**2 + (m.x83 - m.x115)**2 + (m.x162 - m.x194)**2)**(-3) - 2) + ((m.x4
    - m.x37)**2 + (m.x83 - m.x116)**2 + (m.x162 - m.x195)**2)**(-3) * (((m.x4
    - m.x37)**2 + (m.x83 - m.x116)**2 + (m.x162 - m.x195)**2)**(-3) - 2) + ((
    m.x4 - m.x38)**2 + (m.x83 - m.x117)**2 + (m.x162 - m.x196)**2)**(-3) * (((
    m.x4 - m.x38)**2 + (m.x83 - m.x117)**2 + (m.x162 - m.x196)**2)**(-3) - 2)
    + ((m.x4 - m.x39)**2 + (m.x83 - m.x118)**2 + (m.x162 - m.x197)**2)**(-3)
    * (((m.x4 - m.x39)**2 + (m.x83 - m.x118)**2 + (m.x162 - m.x197)**2)**(-3)
    - 2) + ((m.x4 - m.x40)**2 + (m.x83 - m.x119)**2 + (m.x162 - m.x198)**2)**(
    -3) * (((m.x4 - m.x40)**2 + (m.x83 - m.x119)**2 + (m.x162 - m.x198)**2)**(
    -3) - 2) + ((m.x4 - m.x41)**2 + (m.x83 - m.x120)**2 + (m.x162 - m.x199)**2)
    **(-3) * (((m.x4 - m.x41)**2 + (m.x83 - m.x120)**2 + (m.x162 - m.x199)**2)
    **(-3) - 2) + ((m.x4 - m.x42)**2 + (m.x83 - m.x121)**2 + (m.x162 - m.x200)
    **2)**(-3) * (((m.x4 - m.x42)**2 + (m.x83 - m.x121)**2 + (m.x162 - m.x200)
    **2)**(-3) - 2) + ((m.x4 - m.x43)**2 + (m.x83 - m.x122)**2 + (m.x162 -
    m.x201)**2)**(-3) * (((m.x4 - m.x43)**2 + (m.x83 - m.x122)**2 + (m.x162 -
    m.x201)**2)**(-3) - 2) + ((m.x4 - m.x44)**2 + (m.x83 - m.x123)**2 + (m.x162
    - m.x202)**2)**(-3) * (((m.x4 - m.x44)**2 + (m.x83 - m.x123)**2 + (m.x162
    - m.x202)**2)**(-3) - 2) + ((m.x4 - m.x45)**2 + (m.x83 - m.x124)**2 + (
    m.x162 - m.x203)**2)**(-3) * (((m.x4 - m.x45)**2 + (m.x83 - m.x124)**2 + (
    m.x162 - m.x203)**2)**(-3) - 2) + ((m.x4 - m.x46)**2 + (m.x83 - m.x125)**2
    + (m.x162 - m.x204)**2)**(-3) * (((m.x4 - m.x46)**2 + (m.x83 - m.x125)**2
    + (m.x162 - m.x204)**2)**(-3) - 2) + ((m.x4 - m.x47)**2 + (m.x83 - m.x126)
    **2 + (m.x162 - m.x205)**2)**(-3) * (((m.x4 - m.x47)**2 + (m.x83 - m.x126)
    **2 + (m.x162 - m.x205)**2)**(-3) - 2) + ((m.x4 - m.x48)**2 + (m.x83 -
    m.x127)**2 + (m.x162 - m.x206)**2)**(-3) * (((m.x4 - m.x48)**2 + (m.x83 -
    m.x127)**2 + (m.x162 - m.x206)**2)**(-3) - 2) + ((m.x4 - m.x49)**2 + (m.x83
    - m.x128)**2 + (m.x162 - m.x207)**2)**(-3) * (((m.x4 - m.x49)**2 + (m.x83
    - m.x128)**2 + (m.x162 - m.x207)**2)**(-3) - 2) + ((m.x4 - m.x50)**2 + (
    m.x83 - m.x129)**2 + (m.x162 - m.x208)**2)**(-3) * (((m.x4 - m.x50)**2 + (
    m.x83 - m.x129)**2 + (m.x162 - m.x208)**2)**(-3) - 2) + ((m.x4 - m.x51)**2
    + (m.x83 - m.x130)**2 + (m.x162 - m.x209)**2)**(-3) * (((m.x4 - m.x51)**2
    + (m.x83 - m.x130)**2 + (m.x162 - m.x209)**2)**(-3) - 2) + ((m.x4 - m.x52)
    **2 + (m.x83 - m.x131)**2 + (m.x162 - m.x210)**2)**(-3) * (((m.x4 - m.x52)
    **2 + (m.x83 - m.x131)**2 + (m.x162 - m.x210)**2)**(-3) - 2) + ((m.x4 -
    m.x53)**2 + (m.x83 - m.x132)**2 + (m.x162 - m.x211)**2)**(-3) * (((m.x4 -
    m.x53)**2 + (m.x83 - m.x132)**2 + (m.x162 - m.x211)**2)**(-3) - 2) + ((m.x4
    - m.x54)**2 + (m.x83 - m.x133)**2 + (m.x162 - m.x212)**2)**(-3) * (((m.x4
    - m.x54)**2 + (m.x83 - m.x133)**2 + (m.x162 - m.x212)**2)**(-3) - 2) + ((
    m.x4 - m.x55)**2 + (m.x83 - m.x134)**2 + (m.x162 - m.x213)**2)**(-3) * (((
    m.x4 - m.x55)**2 + (m.x83 - m.x134)**2 + (m.x162 - m.x213)**2)**(-3) - 2)
    + ((m.x4 - m.x56)**2 + (m.x83 - m.x135)**2 + (m.x162 - m.x214)**2)**(-3)
    * (((m.x4 - m.x56)**2 + (m.x83 - m.x135)**2 + (m.x162 - m.x214)**2)**(-3)
    - 2) + ((m.x4 - m.x57)**2 + (m.x83 - m.x136)**2 + (m.x162 - m.x215)**2)**(
    -3) * (((m.x4 - m.x57)**2 + (m.x83 - m.x136)**2 + (m.x162 - m.x215)**2)**(
    -3) - 2) + ((m.x4 - m.x58)**2 + (m.x83 - m.x137)**2 + (m.x162 - m.x216)**2)
    **(-3) * (((m.x4 - m.x58)**2 + (m.x83 - m.x137)**2 + (m.x162 - m.x216)**2)
    **(-3) - 2) + ((m.x4 - m.x59)**2 + (m.x83 - m.x138)**2 + (m.x162 - m.x217)
    **2)**(-3) * (((m.x4 - m.x59)**2 + (m.x83 - m.x138)**2 + (m.x162 - m.x217)
    **2)**(-3) - 2) + ((m.x4 - m.x60)**2 + (m.x83 - m.x139)**2 + (m.x162 -
    m.x218)**2)**(-3) * (((m.x4 - m.x60)**2 + (m.x83 - m.x139)**2 + (m.x162 -
    m.x218)**2)**(-3) - 2) + ((m.x4 - m.x61)**2 + (m.x83 - m.x140)**2 + (m.x162
    - m.x219)**2)**(-3) * (((m.x4 - m.x61)**2 + (m.x83 - m.x140)**2 + (m.x162
    - m.x219)**2)**(-3) - 2) + ((m.x4 - m.x62)**2 + (m.x83 - m.x141)**2 + (
    m.x162 - m.x220)**2)**(-3) * (((m.x4 - m.x62)**2 + (m.x83 - m.x141)**2 + (
    m.x162 - m.x220)**2)**(-3) - 2) + ((m.x4 - m.x63)**2 + (m.x83 - m.x142)**2
    + (m.x162 - m.x221)**2)**(-3) * (((m.x4 - m.x63)**2 + (m.x83 - m.x142)**2
    + (m.x162 - m.x221)**2)**(-3) - 2) + ((m.x4 - m.x64)**2 + (m.x83 - m.x143)
    **2 + (m.x162 - m.x222)**2)**(-3) * (((m.x4 - m.x64)**2 + (m.x83 - m.x143)
    **2 + (m.x162 - m.x222)**2)**(-3) - 2) + ((m.x4 - m.x65)**2 + (m.x83 -
    m.x144)**2 + (m.x162 - m.x223)**2)**(-3) * (((m.x4 - m.x65)**2 + (m.x83 -
    m.x144)**2 + (m.x162 - m.x223)**2)**(-3) - 2) + ((m.x4 - m.x66)**2 + (m.x83
    - m.x145)**2 + (m.x162 - m.x224)**2)**(-3) * (((m.x4 - m.x66)**2 + (m.x83
    - m.x145)**2 + (m.x162 - m.x224)**2)**(-3) - 2) + ((m.x4 - m.x67)**2 + (
    m.x83 - m.x146)**2 + (m.x162 - m.x225)**2)**(-3) * (((m.x4 - m.x67)**2 + (
    m.x83 - m.x146)**2 + (m.x162 - m.x225)**2)**(-3) - 2) + ((m.x4 - m.x68)**2
    + (m.x83 - m.x147)**2 + (m.x162 - m.x226)**2)**(-3) * (((m.x4 - m.x68)**2
    + (m.x83 - m.x147)**2 + (m.x162 - m.x226)**2)**(-3) - 2) + ((m.x4 - m.x69)
    **2 + (m.x83 - m.x148)**2 + (m.x162 - m.x227)**2)**(-3) * (((m.x4 - m.x69)
    **2 + (m.x83 - m.x148)**2 + (m.x162 - m.x227)**2)**(-3) - 2) + ((m.x4 -
    m.x70)**2 + (m.x83 - m.x149)**2 + (m.x162 - m.x228)**2)**(-3) * (((m.x4 -
    m.x70)**2 + (m.x83 - m.x149)**2 + (m.x162 - m.x228)**2)**(-3) - 2) + ((m.x4
    - m.x71)**2 + (m.x83 - m.x150)**2 + (m.x162 - m.x229)**2)**(-3) * (((m.x4
    - m.x71)**2 + (m.x83 - m.x150)**2 + (m.x162 - m.x229)**2)**(-3) - 2) + ((
    m.x4 - m.x72)**2 + (m.x83 - m.x151)**2 + (m.x162 - m.x230)**2)**(-3) * (((
    m.x4 - m.x72)**2 + (m.x83 - m.x151)**2 + (m.x162 - m.x230)**2)**(-3) - 2)
    + ((m.x4 - m.x73)**2 + (m.x83 - m.x152)**2 + (m.x162 - m.x231)**2)**(-3)
    * (((m.x4 - m.x73)**2 + (m.x83 - m.x152)**2 + (m.x162 - m.x231)**2)**(-3)
    - 2) + ((m.x4 - m.x74)**2 + (m.x83 - m.x153)**2 + (m.x162 - m.x232)**2)**(
    -3) * (((m.x4 - m.x74)**2 + (m.x83 - m.x153)**2 + (m.x162 - m.x232)**2)**(
    -3) - 2) + ((m.x4 - m.x75)**2 + (m.x83 - m.x154)**2 + (m.x162 - m.x233)**2)
    **(-3) * (((m.x4 - m.x75)**2 + (m.x83 - m.x154)**2 + (m.x162 - m.x233)**2)
    **(-3) - 2) + ((m.x4 - m.x76)**2 + (m.x83 - m.x155)**2 + (m.x162 - m.x234)
    **2)**(-3) * (((m.x4 - m.x76)**2 + (m.x83 - m.x155)**2 + (m.x162 - m.x234)
    **2)**(-3) - 2) + ((m.x4 - m.x77)**2 + (m.x83 - m.x156)**2 + (m.x162 -
    m.x235)**2)**(-3) * (((m.x4 - m.x77)**2 + (m.x83 - m.x156)**2 + (m.x162 -
    m.x235)**2)**(-3) - 2) + ((m.x4 - m.x78)**2 + (m.x83 - m.x157)**2 + (m.x162
    - m.x236)**2)**(-3) * (((m.x4 - m.x78)**2 + (m.x83 - m.x157)**2 + (m.x162
    - m.x236)**2)**(-3) - 2) + ((m.x4 - m.x79)**2 + (m.x83 - m.x158)**2 + (
    m.x162 - m.x237)**2)**(-3) * (((m.x4 - m.x79)**2 + (m.x83 - m.x158)**2 + (
    m.x162 - m.x237)**2)**(-3) - 2) + ((m.x5 - m.x6)**2 + (m.x84 - m.x85)**2 +
    (m.x163 - m.x164)**2)**(-3) * (((m.x5 - m.x6)**2 + (m.x84 - m.x85)**2 + (
    m.x163 - m.x164)**2)**(-3) - 2) + ((m.x5 - m.x7)**2 + (m.x84 - m.x86)**2 +
    (m.x163 - m.x165)**2)**(-3) * (((m.x5 - m.x7)**2 + (m.x84 - m.x86)**2 + (
    m.x163 - m.x165)**2)**(-3) - 2) + ((m.x5 - m.x8)**2 + (m.x84 - m.x87)**2 +
    (m.x163 - m.x166)**2)**(-3) * (((m.x5 - m.x8)**2 + (m.x84 - m.x87)**2 + (
    m.x163 - m.x166)**2)**(-3) - 2) + ((m.x5 - m.x9)**2 + (m.x84 - m.x88)**2 +
    (m.x163 - m.x167)**2)**(-3) * (((m.x5 - m.x9)**2 + (m.x84 - m.x88)**2 + (
    m.x163 - m.x167)**2)**(-3) - 2) + ((m.x5 - m.x10)**2 + (m.x84 - m.x89)**2
    + (m.x163 - m.x168)**2)**(-3) * (((m.x5 - m.x10)**2 + (m.x84 - m.x89)**2
    + (m.x163 - m.x168)**2)**(-3) - 2) + ((m.x5 - m.x11)**2 + (m.x84 - m.x90)
    **2 + (m.x163 - m.x169)**2)**(-3) * (((m.x5 - m.x11)**2 + (m.x84 - m.x90)**
    2 + (m.x163 - m.x169)**2)**(-3) - 2) + ((m.x5 - m.x12)**2 + (m.x84 - m.x91)
    **2 + (m.x163 - m.x170)**2)**(-3) * (((m.x5 - m.x12)**2 + (m.x84 - m.x91)**
    2 + (m.x163 - m.x170)**2)**(-3) - 2) + ((m.x5 - m.x13)**2 + (m.x84 - m.x92)
    **2 + (m.x163 - m.x171)**2)**(-3) * (((m.x5 - m.x13)**2 + (m.x84 - m.x92)**
    2 + (m.x163 - m.x171)**2)**(-3) - 2) + ((m.x5 - m.x14)**2 + (m.x84 - m.x93)
    **2 + (m.x163 - m.x172)**2)**(-3) * (((m.x5 - m.x14)**2 + (m.x84 - m.x93)**
    2 + (m.x163 - m.x172)**2)**(-3) - 2) + ((m.x5 - m.x15)**2 + (m.x84 - m.x94)
    **2 + (m.x163 - m.x173)**2)**(-3) * (((m.x5 - m.x15)**2 + (m.x84 - m.x94)**
    2 + (m.x163 - m.x173)**2)**(-3) - 2) + ((m.x5 - m.x16)**2 + (m.x84 - m.x95)
    **2 + (m.x163 - m.x174)**2)**(-3) * (((m.x5 - m.x16)**2 + (m.x84 - m.x95)**
    2 + (m.x163 - m.x174)**2)**(-3) - 2) + ((m.x5 - m.x17)**2 + (m.x84 - m.x96)
    **2 + (m.x163 - m.x175)**2)**(-3) * (((m.x5 - m.x17)**2 + (m.x84 - m.x96)**
    2 + (m.x163 - m.x175)**2)**(-3) - 2) + ((m.x5 - m.x18)**2 + (m.x84 - m.x97)
    **2 + (m.x163 - m.x176)**2)**(-3) * (((m.x5 - m.x18)**2 + (m.x84 - m.x97)**
    2 + (m.x163 - m.x176)**2)**(-3) - 2) + ((m.x5 - m.x19)**2 + (m.x84 - m.x98)
    **2 + (m.x163 - m.x177)**2)**(-3) * (((m.x5 - m.x19)**2 + (m.x84 - m.x98)**
    2 + (m.x163 - m.x177)**2)**(-3) - 2) + ((m.x5 - m.x20)**2 + (m.x84 - m.x99)
    **2 + (m.x163 - m.x178)**2)**(-3) * (((m.x5 - m.x20)**2 + (m.x84 - m.x99)**
    2 + (m.x163 - m.x178)**2)**(-3) - 2) + ((m.x5 - m.x21)**2 + (m.x84 - m.x100)
    **2 + (m.x163 - m.x179)**2)**(-3) * (((m.x5 - m.x21)**2 + (m.x84 - m.x100)
    **2 + (m.x163 - m.x179)**2)**(-3) - 2) + ((m.x5 - m.x22)**2 + (m.x84 -
    m.x101)**2 + (m.x163 - m.x180)**2)**(-3) * (((m.x5 - m.x22)**2 + (m.x84 -
    m.x101)**2 + (m.x163 - m.x180)**2)**(-3) - 2) + ((m.x5 - m.x23)**2 + (m.x84
    - m.x102)**2 + (m.x163 - m.x181)**2)**(-3) * (((m.x5 - m.x23)**2 + (m.x84
    - m.x102)**2 + (m.x163 - m.x181)**2)**(-3) - 2) + ((m.x5 - m.x24)**2 + (
    m.x84 - m.x103)**2 + (m.x163 - m.x182)**2)**(-3) * (((m.x5 - m.x24)**2 + (
    m.x84 - m.x103)**2 + (m.x163 - m.x182)**2)**(-3) - 2) + ((m.x5 - m.x25)**2
    + (m.x84 - m.x104)**2 + (m.x163 - m.x183)**2)**(-3) * (((m.x5 - m.x25)**2
    + (m.x84 - m.x104)**2 + (m.x163 - m.x183)**2)**(-3) - 2) + ((m.x5 - m.x26)
    **2 + (m.x84 - m.x105)**2 + (m.x163 - m.x184)**2)**(-3) * (((m.x5 - m.x26)
    **2 + (m.x84 - m.x105)**2 + (m.x163 - m.x184)**2)**(-3) - 2) + ((m.x5 -
    m.x27)**2 + (m.x84 - m.x106)**2 + (m.x163 - m.x185)**2)**(-3) * (((m.x5 -
    m.x27)**2 + (m.x84 - m.x106)**2 + (m.x163 - m.x185)**2)**(-3) - 2) + ((m.x5
    - m.x28)**2 + (m.x84 - m.x107)**2 + (m.x163 - m.x186)**2)**(-3) * (((m.x5
    - m.x28)**2 + (m.x84 - m.x107)**2 + (m.x163 - m.x186)**2)**(-3) - 2) + ((
    m.x5 - m.x29)**2 + (m.x84 - m.x108)**2 + (m.x163 - m.x187)**2)**(-3) * (((
    m.x5 - m.x29)**2 + (m.x84 - m.x108)**2 + (m.x163 - m.x187)**2)**(-3) - 2)
    + ((m.x5 - m.x30)**2 + (m.x84 - m.x109)**2 + (m.x163 - m.x188)**2)**(-3)
    * (((m.x5 - m.x30)**2 + (m.x84 - m.x109)**2 + (m.x163 - m.x188)**2)**(-3)
    - 2) + ((m.x5 - m.x31)**2 + (m.x84 - m.x110)**2 + (m.x163 - m.x189)**2)**(
    -3) * (((m.x5 - m.x31)**2 + (m.x84 - m.x110)**2 + (m.x163 - m.x189)**2)**(
    -3) - 2) + ((m.x5 - m.x32)**2 + (m.x84 - m.x111)**2 + (m.x163 - m.x190)**2)
    **(-3) * (((m.x5 - m.x32)**2 + (m.x84 - m.x111)**2 + (m.x163 - m.x190)**2)
    **(-3) - 2) + ((m.x5 - m.x33)**2 + (m.x84 - m.x112)**2 + (m.x163 - m.x191)
    **2)**(-3) * (((m.x5 - m.x33)**2 + (m.x84 - m.x112)**2 + (m.x163 - m.x191)
    **2)**(-3) - 2) + ((m.x5 - m.x34)**2 + (m.x84 - m.x113)**2 + (m.x163 -
    m.x192)**2)**(-3) * (((m.x5 - m.x34)**2 + (m.x84 - m.x113)**2 + (m.x163 -
    m.x192)**2)**(-3) - 2) + ((m.x5 - m.x35)**2 + (m.x84 - m.x114)**2 + (m.x163
    - m.x193)**2)**(-3) * (((m.x5 - m.x35)**2 + (m.x84 - m.x114)**2 + (m.x163
    - m.x193)**2)**(-3) - 2) + ((m.x5 - m.x36)**2 + (m.x84 - m.x115)**2 + (
    m.x163 - m.x194)**2)**(-3) * (((m.x5 - m.x36)**2 + (m.x84 - m.x115)**2 + (
    m.x163 - m.x194)**2)**(-3) - 2) + ((m.x5 - m.x37)**2 + (m.x84 - m.x116)**2
    + (m.x163 - m.x195)**2)**(-3) * (((m.x5 - m.x37)**2 + (m.x84 - m.x116)**2
    + (m.x163 - m.x195)**2)**(-3) - 2) + ((m.x5 - m.x38)**2 + (m.x84 - m.x117)
    **2 + (m.x163 - m.x196)**2)**(-3) * (((m.x5 - m.x38)**2 + (m.x84 - m.x117)
    **2 + (m.x163 - m.x196)**2)**(-3) - 2) + ((m.x5 - m.x39)**2 + (m.x84 -
    m.x118)**2 + (m.x163 - m.x197)**2)**(-3) * (((m.x5 - m.x39)**2 + (m.x84 -
    m.x118)**2 + (m.x163 - m.x197)**2)**(-3) - 2) + ((m.x5 - m.x40)**2 + (m.x84
    - m.x119)**2 + (m.x163 - m.x198)**2)**(-3) * (((m.x5 - m.x40)**2 + (m.x84
    - m.x119)**2 + (m.x163 - m.x198)**2)**(-3) - 2) + ((m.x5 - m.x41)**2 + (
    m.x84 - m.x120)**2 + (m.x163 - m.x199)**2)**(-3) * (((m.x5 - m.x41)**2 + (
    m.x84 - m.x120)**2 + (m.x163 - m.x199)**2)**(-3) - 2) + ((m.x5 - m.x42)**2
    + (m.x84 - m.x121)**2 + (m.x163 - m.x200)**2)**(-3) * (((m.x5 - m.x42)**2
    + (m.x84 - m.x121)**2 + (m.x163 - m.x200)**2)**(-3) - 2) + ((m.x5 - m.x43)
    **2 + (m.x84 - m.x122)**2 + (m.x163 - m.x201)**2)**(-3) * (((m.x5 - m.x43)
    **2 + (m.x84 - m.x122)**2 + (m.x163 - m.x201)**2)**(-3) - 2) + ((m.x5 -
    m.x44)**2 + (m.x84 - m.x123)**2 + (m.x163 - m.x202)**2)**(-3) * (((m.x5 -
    m.x44)**2 + (m.x84 - m.x123)**2 + (m.x163 - m.x202)**2)**(-3) - 2) + ((m.x5
    - m.x45)**2 + (m.x84 - m.x124)**2 + (m.x163 - m.x203)**2)**(-3) * (((m.x5
    - m.x45)**2 + (m.x84 - m.x124)**2 + (m.x163 - m.x203)**2)**(-3) - 2) + ((
    m.x5 - m.x46)**2 + (m.x84 - m.x125)**2 + (m.x163 - m.x204)**2)**(-3) * (((
    m.x5 - m.x46)**2 + (m.x84 - m.x125)**2 + (m.x163 - m.x204)**2)**(-3) - 2)
    + ((m.x5 - m.x47)**2 + (m.x84 - m.x126)**2 + (m.x163 - m.x205)**2)**(-3)
    * (((m.x5 - m.x47)**2 + (m.x84 - m.x126)**2 + (m.x163 - m.x205)**2)**(-3)
    - 2) + ((m.x5 - m.x48)**2 + (m.x84 - m.x127)**2 + (m.x163 - m.x206)**2)**(
    -3) * (((m.x5 - m.x48)**2 + (m.x84 - m.x127)**2 + (m.x163 - m.x206)**2)**(
    -3) - 2) + ((m.x5 - m.x49)**2 + (m.x84 - m.x128)**2 + (m.x163 - m.x207)**2)
    **(-3) * (((m.x5 - m.x49)**2 + (m.x84 - m.x128)**2 + (m.x163 - m.x207)**2)
    **(-3) - 2) + ((m.x5 - m.x50)**2 + (m.x84 - m.x129)**2 + (m.x163 - m.x208)
    **2)**(-3) * (((m.x5 - m.x50)**2 + (m.x84 - m.x129)**2 + (m.x163 - m.x208)
    **2)**(-3) - 2) + ((m.x5 - m.x51)**2 + (m.x84 - m.x130)**2 + (m.x163 -
    m.x209)**2)**(-3) * (((m.x5 - m.x51)**2 + (m.x84 - m.x130)**2 + (m.x163 -
    m.x209)**2)**(-3) - 2) + ((m.x5 - m.x52)**2 + (m.x84 - m.x131)**2 + (m.x163
    - m.x210)**2)**(-3) * (((m.x5 - m.x52)**2 + (m.x84 - m.x131)**2 + (m.x163
    - m.x210)**2)**(-3) - 2) + ((m.x5 - m.x53)**2 + (m.x84 - m.x132)**2 + (
    m.x163 - m.x211)**2)**(-3) * (((m.x5 - m.x53)**2 + (m.x84 - m.x132)**2 + (
    m.x163 - m.x211)**2)**(-3) - 2) + ((m.x5 - m.x54)**2 + (m.x84 - m.x133)**2
    + (m.x163 - m.x212)**2)**(-3) * (((m.x5 - m.x54)**2 + (m.x84 - m.x133)**2
    + (m.x163 - m.x212)**2)**(-3) - 2) + ((m.x5 - m.x55)**2 + (m.x84 - m.x134)
    **2 + (m.x163 - m.x213)**2)**(-3) * (((m.x5 - m.x55)**2 + (m.x84 - m.x134)
    **2 + (m.x163 - m.x213)**2)**(-3) - 2) + ((m.x5 - m.x56)**2 + (m.x84 -
    m.x135)**2 + (m.x163 - m.x214)**2)**(-3) * (((m.x5 - m.x56)**2 + (m.x84 -
    m.x135)**2 + (m.x163 - m.x214)**2)**(-3) - 2) + ((m.x5 - m.x57)**2 + (m.x84
    - m.x136)**2 + (m.x163 - m.x215)**2)**(-3) * (((m.x5 - m.x57)**2 + (m.x84
    - m.x136)**2 + (m.x163 - m.x215)**2)**(-3) - 2) + ((m.x5 - m.x58)**2 + (
    m.x84 - m.x137)**2 + (m.x163 - m.x216)**2)**(-3) * (((m.x5 - m.x58)**2 + (
    m.x84 - m.x137)**2 + (m.x163 - m.x216)**2)**(-3) - 2) + ((m.x5 - m.x59)**2
    + (m.x84 - m.x138)**2 + (m.x163 - m.x217)**2)**(-3) * (((m.x5 - m.x59)**2
    + (m.x84 - m.x138)**2 + (m.x163 - m.x217)**2)**(-3) - 2) + ((m.x5 - m.x60)
    **2 + (m.x84 - m.x139)**2 + (m.x163 - m.x218)**2)**(-3) * (((m.x5 - m.x60)
    **2 + (m.x84 - m.x139)**2 + (m.x163 - m.x218)**2)**(-3) - 2) + ((m.x5 -
    m.x61)**2 + (m.x84 - m.x140)**2 + (m.x163 - m.x219)**2)**(-3) * (((m.x5 -
    m.x61)**2 + (m.x84 - m.x140)**2 + (m.x163 - m.x219)**2)**(-3) - 2) + ((m.x5
    - m.x62)**2 + (m.x84 - m.x141)**2 + (m.x163 - m.x220)**2)**(-3) * (((m.x5
    - m.x62)**2 + (m.x84 - m.x141)**2 + (m.x163 - m.x220)**2)**(-3) - 2) + ((
    m.x5 - m.x63)**2 + (m.x84 - m.x142)**2 + (m.x163 - m.x221)**2)**(-3) * (((
    m.x5 - m.x63)**2 + (m.x84 - m.x142)**2 + (m.x163 - m.x221)**2)**(-3) - 2)
    + ((m.x5 - m.x64)**2 + (m.x84 - m.x143)**2 + (m.x163 - m.x222)**2)**(-3)
    * (((m.x5 - m.x64)**2 + (m.x84 - m.x143)**2 + (m.x163 - m.x222)**2)**(-3)
    - 2) + ((m.x5 - m.x65)**2 + (m.x84 - m.x144)**2 + (m.x163 - m.x223)**2)**(
    -3) * (((m.x5 - m.x65)**2 + (m.x84 - m.x144)**2 + (m.x163 - m.x223)**2)**(
    -3) - 2) + ((m.x5 - m.x66)**2 + (m.x84 - m.x145)**2 + (m.x163 - m.x224)**2)
    **(-3) * (((m.x5 - m.x66)**2 + (m.x84 - m.x145)**2 + (m.x163 - m.x224)**2)
    **(-3) - 2) + ((m.x5 - m.x67)**2 + (m.x84 - m.x146)**2 + (m.x163 - m.x225)
    **2)**(-3) * (((m.x5 - m.x67)**2 + (m.x84 - m.x146)**2 + (m.x163 - m.x225)
    **2)**(-3) - 2) + ((m.x5 - m.x68)**2 + (m.x84 - m.x147)**2 + (m.x163 -
    m.x226)**2)**(-3) * (((m.x5 - m.x68)**2 + (m.x84 - m.x147)**2 + (m.x163 -
    m.x226)**2)**(-3) - 2) + ((m.x5 - m.x69)**2 + (m.x84 - m.x148)**2 + (m.x163
    - m.x227)**2)**(-3) * (((m.x5 - m.x69)**2 + (m.x84 - m.x148)**2 + (m.x163
    - m.x227)**2)**(-3) - 2) + ((m.x5 - m.x70)**2 + (m.x84 - m.x149)**2 + (
    m.x163 - m.x228)**2)**(-3) * (((m.x5 - m.x70)**2 + (m.x84 - m.x149)**2 + (
    m.x163 - m.x228)**2)**(-3) - 2) + ((m.x5 - m.x71)**2 + (m.x84 - m.x150)**2
    + (m.x163 - m.x229)**2)**(-3) * (((m.x5 - m.x71)**2 + (m.x84 - m.x150)**2
    + (m.x163 - m.x229)**2)**(-3) - 2) + ((m.x5 - m.x72)**2 + (m.x84 - m.x151)
    **2 + (m.x163 - m.x230)**2)**(-3) * (((m.x5 - m.x72)**2 + (m.x84 - m.x151)
    **2 + (m.x163 - m.x230)**2)**(-3) - 2) + ((m.x5 - m.x73)**2 + (m.x84 -
    m.x152)**2 + (m.x163 - m.x231)**2)**(-3) * (((m.x5 - m.x73)**2 + (m.x84 -
    m.x152)**2 + (m.x163 - m.x231)**2)**(-3) - 2) + ((m.x5 - m.x74)**2 + (m.x84
    - m.x153)**2 + (m.x163 - m.x232)**2)**(-3) * (((m.x5 - m.x74)**2 + (m.x84
    - m.x153)**2 + (m.x163 - m.x232)**2)**(-3) - 2) + ((m.x5 - m.x75)**2 + (
    m.x84 - m.x154)**2 + (m.x163 - m.x233)**2)**(-3) * (((m.x5 - m.x75)**2 + (
    m.x84 - m.x154)**2 + (m.x163 - m.x233)**2)**(-3) - 2) + ((m.x5 - m.x76)**2
    + (m.x84 - m.x155)**2 + (m.x163 - m.x234)**2)**(-3) * (((m.x5 - m.x76)**2
    + (m.x84 - m.x155)**2 + (m.x163 - m.x234)**2)**(-3) - 2) + ((m.x5 - m.x77)
    **2 + (m.x84 - m.x156)**2 + (m.x163 - m.x235)**2)**(-3) * (((m.x5 - m.x77)
    **2 + (m.x84 - m.x156)**2 + (m.x163 - m.x235)**2)**(-3) - 2) + ((m.x5 -
    m.x78)**2 + (m.x84 - m.x157)**2 + (m.x163 - m.x236)**2)**(-3) * (((m.x5 -
    m.x78)**2 + (m.x84 - m.x157)**2 + (m.x163 - m.x236)**2)**(-3) - 2) + ((m.x5
    - m.x79)**2 + (m.x84 - m.x158)**2 + (m.x163 - m.x237)**2)**(-3) * (((m.x5
    - m.x79)**2 + (m.x84 - m.x158)**2 + (m.x163 - m.x237)**2)**(-3) - 2) + ((
    m.x6 - m.x7)**2 + (m.x85 - m.x86)**2 + (m.x164 - m.x165)**2)**(-3) * (((
    m.x6 - m.x7)**2 + (m.x85 - m.x86)**2 + (m.x164 - m.x165)**2)**(-3) - 2) + (
    (m.x6 - m.x8)**2 + (m.x85 - m.x87)**2 + (m.x164 - m.x166)**2)**(-3) * (((
    m.x6 - m.x8)**2 + (m.x85 - m.x87)**2 + (m.x164 - m.x166)**2)**(-3) - 2) + (
    (m.x6 - m.x9)**2 + (m.x85 - m.x88)**2 + (m.x164 - m.x167)**2)**(-3) * (((
    m.x6 - m.x9)**2 + (m.x85 - m.x88)**2 + (m.x164 - m.x167)**2)**(-3) - 2) + (
    (m.x6 - m.x10)**2 + (m.x85 - m.x89)**2 + (m.x164 - m.x168)**2)**(-3) * (((
    m.x6 - m.x10)**2 + (m.x85 - m.x89)**2 + (m.x164 - m.x168)**2)**(-3) - 2) +
    ((m.x6 - m.x11)**2 + (m.x85 - m.x90)**2 + (m.x164 - m.x169)**2)**(-3) * (((
    m.x6 - m.x11)**2 + (m.x85 - m.x90)**2 + (m.x164 - m.x169)**2)**(-3) - 2) +
    ((m.x6 - m.x12)**2 + (m.x85 - m.x91)**2 + (m.x164 - m.x170)**2)**(-3) * (((
    m.x6 - m.x12)**2 + (m.x85 - m.x91)**2 + (m.x164 - m.x170)**2)**(-3) - 2) +
    ((m.x6 - m.x13)**2 + (m.x85 - m.x92)**2 + (m.x164 - m.x171)**2)**(-3) * (((
    m.x6 - m.x13)**2 + (m.x85 - m.x92)**2 + (m.x164 - m.x171)**2)**(-3) - 2) +
    ((m.x6 - m.x14)**2 + (m.x85 - m.x93)**2 + (m.x164 - m.x172)**2)**(-3) * (((
    m.x6 - m.x14)**2 + (m.x85 - m.x93)**2 + (m.x164 - m.x172)**2)**(-3) - 2) +
    ((m.x6 - m.x15)**2 + (m.x85 - m.x94)**2 + (m.x164 - m.x173)**2)**(-3) * (((
    m.x6 - m.x15)**2 + (m.x85 - m.x94)**2 + (m.x164 - m.x173)**2)**(-3) - 2) +
    ((m.x6 - m.x16)**2 + (m.x85 - m.x95)**2 + (m.x164 - m.x174)**2)**(-3) * (((
    m.x6 - m.x16)**2 + (m.x85 - m.x95)**2 + (m.x164 - m.x174)**2)**(-3) - 2) +
    ((m.x6 - m.x17)**2 + (m.x85 - m.x96)**2 + (m.x164 - m.x175)**2)**(-3) * (((
    m.x6 - m.x17)**2 + (m.x85 - m.x96)**2 + (m.x164 - m.x175)**2)**(-3) - 2) +
    ((m.x6 - m.x18)**2 + (m.x85 - m.x97)**2 + (m.x164 - m.x176)**2)**(-3) * (((
    m.x6 - m.x18)**2 + (m.x85 - m.x97)**2 + (m.x164 - m.x176)**2)**(-3) - 2) +
    ((m.x6 - m.x19)**2 + (m.x85 - m.x98)**2 + (m.x164 - m.x177)**2)**(-3) * (((
    m.x6 - m.x19)**2 + (m.x85 - m.x98)**2 + (m.x164 - m.x177)**2)**(-3) - 2) +
    ((m.x6 - m.x20)**2 + (m.x85 - m.x99)**2 + (m.x164 - m.x178)**2)**(-3) * (((
    m.x6 - m.x20)**2 + (m.x85 - m.x99)**2 + (m.x164 - m.x178)**2)**(-3) - 2) +
    ((m.x6 - m.x21)**2 + (m.x85 - m.x100)**2 + (m.x164 - m.x179)**2)**(-3) * ((
    (m.x6 - m.x21)**2 + (m.x85 - m.x100)**2 + (m.x164 - m.x179)**2)**(-3) - 2)
    + ((m.x6 - m.x22)**2 + (m.x85 - m.x101)**2 + (m.x164 - m.x180)**2)**(-3)
    * (((m.x6 - m.x22)**2 + (m.x85 - m.x101)**2 + (m.x164 - m.x180)**2)**(-3)
    - 2) + ((m.x6 - m.x23)**2 + (m.x85 - m.x102)**2 + (m.x164 - m.x181)**2)**(
    -3) * (((m.x6 - m.x23)**2 + (m.x85 - m.x102)**2 + (m.x164 - m.x181)**2)**(
    -3) - 2) + ((m.x6 - m.x24)**2 + (m.x85 - m.x103)**2 + (m.x164 - m.x182)**2)
    **(-3) * (((m.x6 - m.x24)**2 + (m.x85 - m.x103)**2 + (m.x164 - m.x182)**2)
    **(-3) - 2) + ((m.x6 - m.x25)**2 + (m.x85 - m.x104)**2 + (m.x164 - m.x183)
    **2)**(-3) * (((m.x6 - m.x25)**2 + (m.x85 - m.x104)**2 + (m.x164 - m.x183)
    **2)**(-3) - 2) + ((m.x6 - m.x26)**2 + (m.x85 - m.x105)**2 + (m.x164 -
    m.x184)**2)**(-3) * (((m.x6 - m.x26)**2 + (m.x85 - m.x105)**2 + (m.x164 -
    m.x184)**2)**(-3) - 2) + ((m.x6 - m.x27)**2 + (m.x85 - m.x106)**2 + (m.x164
    - m.x185)**2)**(-3) * (((m.x6 - m.x27)**2 + (m.x85 - m.x106)**2 + (m.x164
    - m.x185)**2)**(-3) - 2) + ((m.x6 - m.x28)**2 + (m.x85 - m.x107)**2 + (
    m.x164 - m.x186)**2)**(-3) * (((m.x6 - m.x28)**2 + (m.x85 - m.x107)**2 + (
    m.x164 - m.x186)**2)**(-3) - 2) + ((m.x6 - m.x29)**2 + (m.x85 - m.x108)**2
    + (m.x164 - m.x187)**2)**(-3) * (((m.x6 - m.x29)**2 + (m.x85 - m.x108)**2
    + (m.x164 - m.x187)**2)**(-3) - 2) + ((m.x6 - m.x30)**2 + (m.x85 - m.x109)
    **2 + (m.x164 - m.x188)**2)**(-3) * (((m.x6 - m.x30)**2 + (m.x85 - m.x109)
    **2 + (m.x164 - m.x188)**2)**(-3) - 2) + ((m.x6 - m.x31)**2 + (m.x85 -
    m.x110)**2 + (m.x164 - m.x189)**2)**(-3) * (((m.x6 - m.x31)**2 + (m.x85 -
    m.x110)**2 + (m.x164 - m.x189)**2)**(-3) - 2) + ((m.x6 - m.x32)**2 + (m.x85
    - m.x111)**2 + (m.x164 - m.x190)**2)**(-3) * (((m.x6 - m.x32)**2 + (m.x85
    - m.x111)**2 + (m.x164 - m.x190)**2)**(-3) - 2) + ((m.x6 - m.x33)**2 + (
    m.x85 - m.x112)**2 + (m.x164 - m.x191)**2)**(-3) * (((m.x6 - m.x33)**2 + (
    m.x85 - m.x112)**2 + (m.x164 - m.x191)**2)**(-3) - 2) + ((m.x6 - m.x34)**2
    + (m.x85 - m.x113)**2 + (m.x164 - m.x192)**2)**(-3) * (((m.x6 - m.x34)**2
    + (m.x85 - m.x113)**2 + (m.x164 - m.x192)**2)**(-3) - 2) + ((m.x6 - m.x35)
    **2 + (m.x85 - m.x114)**2 + (m.x164 - m.x193)**2)**(-3) * (((m.x6 - m.x35)
    **2 + (m.x85 - m.x114)**2 + (m.x164 - m.x193)**2)**(-3) - 2) + ((m.x6 -
    m.x36)**2 + (m.x85 - m.x115)**2 + (m.x164 - m.x194)**2)**(-3) * (((m.x6 -
    m.x36)**2 + (m.x85 - m.x115)**2 + (m.x164 - m.x194)**2)**(-3) - 2) + ((m.x6
    - m.x37)**2 + (m.x85 - m.x116)**2 + (m.x164 - m.x195)**2)**(-3) * (((m.x6
    - m.x37)**2 + (m.x85 - m.x116)**2 + (m.x164 - m.x195)**2)**(-3) - 2) + ((
    m.x6 - m.x38)**2 + (m.x85 - m.x117)**2 + (m.x164 - m.x196)**2)**(-3) * (((
    m.x6 - m.x38)**2 + (m.x85 - m.x117)**2 + (m.x164 - m.x196)**2)**(-3) - 2)
    + ((m.x6 - m.x39)**2 + (m.x85 - m.x118)**2 + (m.x164 - m.x197)**2)**(-3)
    * (((m.x6 - m.x39)**2 + (m.x85 - m.x118)**2 + (m.x164 - m.x197)**2)**(-3)
    - 2) + ((m.x6 - m.x40)**2 + (m.x85 - m.x119)**2 + (m.x164 - m.x198)**2)**(
    -3) * (((m.x6 - m.x40)**2 + (m.x85 - m.x119)**2 + (m.x164 - m.x198)**2)**(
    -3) - 2) + ((m.x6 - m.x41)**2 + (m.x85 - m.x120)**2 + (m.x164 - m.x199)**2)
    **(-3) * (((m.x6 - m.x41)**2 + (m.x85 - m.x120)**2 + (m.x164 - m.x199)**2)
    **(-3) - 2) + ((m.x6 - m.x42)**2 + (m.x85 - m.x121)**2 + (m.x164 - m.x200)
    **2)**(-3) * (((m.x6 - m.x42)**2 + (m.x85 - m.x121)**2 + (m.x164 - m.x200)
    **2)**(-3) - 2) + ((m.x6 - m.x43)**2 + (m.x85 - m.x122)**2 + (m.x164 -
    m.x201)**2)**(-3) * (((m.x6 - m.x43)**2 + (m.x85 - m.x122)**2 + (m.x164 -
    m.x201)**2)**(-3) - 2) + ((m.x6 - m.x44)**2 + (m.x85 - m.x123)**2 + (m.x164
    - m.x202)**2)**(-3) * (((m.x6 - m.x44)**2 + (m.x85 - m.x123)**2 + (m.x164
    - m.x202)**2)**(-3) - 2) + ((m.x6 - m.x45)**2 + (m.x85 - m.x124)**2 + (
    m.x164 - m.x203)**2)**(-3) * (((m.x6 - m.x45)**2 + (m.x85 - m.x124)**2 + (
    m.x164 - m.x203)**2)**(-3) - 2) + ((m.x6 - m.x46)**2 + (m.x85 - m.x125)**2
    + (m.x164 - m.x204)**2)**(-3) * (((m.x6 - m.x46)**2 + (m.x85 - m.x125)**2
    + (m.x164 - m.x204)**2)**(-3) - 2) + ((m.x6 - m.x47)**2 + (m.x85 - m.x126)
    **2 + (m.x164 - m.x205)**2)**(-3) * (((m.x6 - m.x47)**2 + (m.x85 - m.x126)
    **2 + (m.x164 - m.x205)**2)**(-3) - 2) + ((m.x6 - m.x48)**2 + (m.x85 -
    m.x127)**2 + (m.x164 - m.x206)**2)**(-3) * (((m.x6 - m.x48)**2 + (m.x85 -
    m.x127)**2 + (m.x164 - m.x206)**2)**(-3) - 2) + ((m.x6 - m.x49)**2 + (m.x85
    - m.x128)**2 + (m.x164 - m.x207)**2)**(-3) * (((m.x6 - m.x49)**2 + (m.x85
    - m.x128)**2 + (m.x164 - m.x207)**2)**(-3) - 2) + ((m.x6 - m.x50)**2 + (
    m.x85 - m.x129)**2 + (m.x164 - m.x208)**2)**(-3) * (((m.x6 - m.x50)**2 + (
    m.x85 - m.x129)**2 + (m.x164 - m.x208)**2)**(-3) - 2) + ((m.x6 - m.x51)**2
    + (m.x85 - m.x130)**2 + (m.x164 - m.x209)**2)**(-3) * (((m.x6 - m.x51)**2
    + (m.x85 - m.x130)**2 + (m.x164 - m.x209)**2)**(-3) - 2) + ((m.x6 - m.x52)
    **2 + (m.x85 - m.x131)**2 + (m.x164 - m.x210)**2)**(-3) * (((m.x6 - m.x52)
    **2 + (m.x85 - m.x131)**2 + (m.x164 - m.x210)**2)**(-3) - 2) + ((m.x6 -
    m.x53)**2 + (m.x85 - m.x132)**2 + (m.x164 - m.x211)**2)**(-3) * (((m.x6 -
    m.x53)**2 + (m.x85 - m.x132)**2 + (m.x164 - m.x211)**2)**(-3) - 2) + ((m.x6
    - m.x54)**2 + (m.x85 - m.x133)**2 + (m.x164 - m.x212)**2)**(-3) * (((m.x6
    - m.x54)**2 + (m.x85 - m.x133)**2 + (m.x164 - m.x212)**2)**(-3) - 2) + ((
    m.x6 - m.x55)**2 + (m.x85 - m.x134)**2 + (m.x164 - m.x213)**2)**(-3) * (((
    m.x6 - m.x55)**2 + (m.x85 - m.x134)**2 + (m.x164 - m.x213)**2)**(-3) - 2)
    + ((m.x6 - m.x56)**2 + (m.x85 - m.x135)**2 + (m.x164 - m.x214)**2)**(-3)
    * (((m.x6 - m.x56)**2 + (m.x85 - m.x135)**2 + (m.x164 - m.x214)**2)**(-3)
    - 2) + ((m.x6 - m.x57)**2 + (m.x85 - m.x136)**2 + (m.x164 - m.x215)**2)**(
    -3) * (((m.x6 - m.x57)**2 + (m.x85 - m.x136)**2 + (m.x164 - m.x215)**2)**(
    -3) - 2) + ((m.x6 - m.x58)**2 + (m.x85 - m.x137)**2 + (m.x164 - m.x216)**2)
    **(-3) * (((m.x6 - m.x58)**2 + (m.x85 - m.x137)**2 + (m.x164 - m.x216)**2)
    **(-3) - 2) + ((m.x6 - m.x59)**2 + (m.x85 - m.x138)**2 + (m.x164 - m.x217)
    **2)**(-3) * (((m.x6 - m.x59)**2 + (m.x85 - m.x138)**2 + (m.x164 - m.x217)
    **2)**(-3) - 2) + ((m.x6 - m.x60)**2 + (m.x85 - m.x139)**2 + (m.x164 -
    m.x218)**2)**(-3) * (((m.x6 - m.x60)**2 + (m.x85 - m.x139)**2 + (m.x164 -
    m.x218)**2)**(-3) - 2) + ((m.x6 - m.x61)**2 + (m.x85 - m.x140)**2 + (m.x164
    - m.x219)**2)**(-3) * (((m.x6 - m.x61)**2 + (m.x85 - m.x140)**2 + (m.x164
    - m.x219)**2)**(-3) - 2) + ((m.x6 - m.x62)**2 + (m.x85 - m.x141)**2 + (
    m.x164 - m.x220)**2)**(-3) * (((m.x6 - m.x62)**2 + (m.x85 - m.x141)**2 + (
    m.x164 - m.x220)**2)**(-3) - 2) + ((m.x6 - m.x63)**2 + (m.x85 - m.x142)**2
    + (m.x164 - m.x221)**2)**(-3) * (((m.x6 - m.x63)**2 + (m.x85 - m.x142)**2
    + (m.x164 - m.x221)**2)**(-3) - 2) + ((m.x6 - m.x64)**2 + (m.x85 - m.x143)
    **2 + (m.x164 - m.x222)**2)**(-3) * (((m.x6 - m.x64)**2 + (m.x85 - m.x143)
    **2 + (m.x164 - m.x222)**2)**(-3) - 2) + ((m.x6 - m.x65)**2 + (m.x85 -
    m.x144)**2 + (m.x164 - m.x223)**2)**(-3) * (((m.x6 - m.x65)**2 + (m.x85 -
    m.x144)**2 + (m.x164 - m.x223)**2)**(-3) - 2) + ((m.x6 - m.x66)**2 + (m.x85
    - m.x145)**2 + (m.x164 - m.x224)**2)**(-3) * (((m.x6 - m.x66)**2 + (m.x85
    - m.x145)**2 + (m.x164 - m.x224)**2)**(-3) - 2) + ((m.x6 - m.x67)**2 + (
    m.x85 - m.x146)**2 + (m.x164 - m.x225)**2)**(-3) * (((m.x6 - m.x67)**2 + (
    m.x85 - m.x146)**2 + (m.x164 - m.x225)**2)**(-3) - 2) + ((m.x6 - m.x68)**2
    + (m.x85 - m.x147)**2 + (m.x164 - m.x226)**2)**(-3) * (((m.x6 - m.x68)**2
    + (m.x85 - m.x147)**2 + (m.x164 - m.x226)**2)**(-3) - 2) + ((m.x6 - m.x69)
    **2 + (m.x85 - m.x148)**2 + (m.x164 - m.x227)**2)**(-3) * (((m.x6 - m.x69)
    **2 + (m.x85 - m.x148)**2 + (m.x164 - m.x227)**2)**(-3) - 2) + ((m.x6 -
    m.x70)**2 + (m.x85 - m.x149)**2 + (m.x164 - m.x228)**2)**(-3) * (((m.x6 -
    m.x70)**2 + (m.x85 - m.x149)**2 + (m.x164 - m.x228)**2)**(-3) - 2) + ((m.x6
    - m.x71)**2 + (m.x85 - m.x150)**2 + (m.x164 - m.x229)**2)**(-3) * (((m.x6
    - m.x71)**2 + (m.x85 - m.x150)**2 + (m.x164 - m.x229)**2)**(-3) - 2) + ((
    m.x6 - m.x72)**2 + (m.x85 - m.x151)**2 + (m.x164 - m.x230)**2)**(-3) * (((
    m.x6 - m.x72)**2 + (m.x85 - m.x151)**2 + (m.x164 - m.x230)**2)**(-3) - 2)
    + ((m.x6 - m.x73)**2 + (m.x85 - m.x152)**2 + (m.x164 - m.x231)**2)**(-3)
    * (((m.x6 - m.x73)**2 + (m.x85 - m.x152)**2 + (m.x164 - m.x231)**2)**(-3)
    - 2) + ((m.x6 - m.x74)**2 + (m.x85 - m.x153)**2 + (m.x164 - m.x232)**2)**(
    -3) * (((m.x6 - m.x74)**2 + (m.x85 - m.x153)**2 + (m.x164 - m.x232)**2)**(
    -3) - 2) + ((m.x6 - m.x75)**2 + (m.x85 - m.x154)**2 + (m.x164 - m.x233)**2)
    **(-3) * (((m.x6 - m.x75)**2 + (m.x85 - m.x154)**2 + (m.x164 - m.x233)**2)
    **(-3) - 2) + ((m.x6 - m.x76)**2 + (m.x85 - m.x155)**2 + (m.x164 - m.x234)
    **2)**(-3) * (((m.x6 - m.x76)**2 + (m.x85 - m.x155)**2 + (m.x164 - m.x234)
    **2)**(-3) - 2) + ((m.x6 - m.x77)**2 + (m.x85 - m.x156)**2 + (m.x164 -
    m.x235)**2)**(-3) * (((m.x6 - m.x77)**2 + (m.x85 - m.x156)**2 + (m.x164 -
    m.x235)**2)**(-3) - 2) + ((m.x6 - m.x78)**2 + (m.x85 - m.x157)**2 + (m.x164
    - m.x236)**2)**(-3) * (((m.x6 - m.x78)**2 + (m.x85 - m.x157)**2 + (m.x164
    - m.x236)**2)**(-3) - 2) + ((m.x6 - m.x79)**2 + (m.x85 - m.x158)**2 + (
    m.x164 - m.x237)**2)**(-3) * (((m.x6 - m.x79)**2 + (m.x85 - m.x158)**2 + (
    m.x164 - m.x237)**2)**(-3) - 2) + ((m.x7 - m.x8)**2 + (m.x86 - m.x87)**2 +
    (m.x165 - m.x166)**2)**(-3) * (((m.x7 - m.x8)**2 + (m.x86 - m.x87)**2 + (
    m.x165 - m.x166)**2)**(-3) - 2) + ((m.x7 - m.x9)**2 + (m.x86 - m.x88)**2 +
    (m.x165 - m.x167)**2)**(-3) * (((m.x7 - m.x9)**2 + (m.x86 - m.x88)**2 + (
    m.x165 - m.x167)**2)**(-3) - 2) + ((m.x7 - m.x10)**2 + (m.x86 - m.x89)**2
    + (m.x165 - m.x168)**2)**(-3) * (((m.x7 - m.x10)**2 + (m.x86 - m.x89)**2
    + (m.x165 - m.x168)**2)**(-3) - 2) + ((m.x7 - m.x11)**2 + (m.x86 - m.x90)
    **2 + (m.x165 - m.x169)**2)**(-3) * (((m.x7 - m.x11)**2 + (m.x86 - m.x90)**
    2 + (m.x165 - m.x169)**2)**(-3) - 2) + ((m.x7 - m.x12)**2 + (m.x86 - m.x91)
    **2 + (m.x165 - m.x170)**2)**(-3) * (((m.x7 - m.x12)**2 + (m.x86 - m.x91)**
    2 + (m.x165 - m.x170)**2)**(-3) - 2) + ((m.x7 - m.x13)**2 + (m.x86 - m.x92)
    **2 + (m.x165 - m.x171)**2)**(-3) * (((m.x7 - m.x13)**2 + (m.x86 - m.x92)**
    2 + (m.x165 - m.x171)**2)**(-3) - 2) + ((m.x7 - m.x14)**2 + (m.x86 - m.x93)
    **2 + (m.x165 - m.x172)**2)**(-3) * (((m.x7 - m.x14)**2 + (m.x86 - m.x93)**
    2 + (m.x165 - m.x172)**2)**(-3) - 2) + ((m.x7 - m.x15)**2 + (m.x86 - m.x94)
    **2 + (m.x165 - m.x173)**2)**(-3) * (((m.x7 - m.x15)**2 + (m.x86 - m.x94)**
    2 + (m.x165 - m.x173)**2)**(-3) - 2) + ((m.x7 - m.x16)**2 + (m.x86 - m.x95)
    **2 + (m.x165 - m.x174)**2)**(-3) * (((m.x7 - m.x16)**2 + (m.x86 - m.x95)**
    2 + (m.x165 - m.x174)**2)**(-3) - 2) + ((m.x7 - m.x17)**2 + (m.x86 - m.x96)
    **2 + (m.x165 - m.x175)**2)**(-3) * (((m.x7 - m.x17)**2 + (m.x86 - m.x96)**
    2 + (m.x165 - m.x175)**2)**(-3) - 2) + ((m.x7 - m.x18)**2 + (m.x86 - m.x97)
    **2 + (m.x165 - m.x176)**2)**(-3) * (((m.x7 - m.x18)**2 + (m.x86 - m.x97)**
    2 + (m.x165 - m.x176)**2)**(-3) - 2) + ((m.x7 - m.x19)**2 + (m.x86 - m.x98)
    **2 + (m.x165 - m.x177)**2)**(-3) * (((m.x7 - m.x19)**2 + (m.x86 - m.x98)**
    2 + (m.x165 - m.x177)**2)**(-3) - 2) + ((m.x7 - m.x20)**2 + (m.x86 - m.x99)
    **2 + (m.x165 - m.x178)**2)**(-3) * (((m.x7 - m.x20)**2 + (m.x86 - m.x99)**
    2 + (m.x165 - m.x178)**2)**(-3) - 2) + ((m.x7 - m.x21)**2 + (m.x86 - m.x100)
    **2 + (m.x165 - m.x179)**2)**(-3) * (((m.x7 - m.x21)**2 + (m.x86 - m.x100)
    **2 + (m.x165 - m.x179)**2)**(-3) - 2) + ((m.x7 - m.x22)**2 + (m.x86 -
    m.x101)**2 + (m.x165 - m.x180)**2)**(-3) * (((m.x7 - m.x22)**2 + (m.x86 -
    m.x101)**2 + (m.x165 - m.x180)**2)**(-3) - 2) + ((m.x7 - m.x23)**2 + (m.x86
    - m.x102)**2 + (m.x165 - m.x181)**2)**(-3) * (((m.x7 - m.x23)**2 + (m.x86
    - m.x102)**2 + (m.x165 - m.x181)**2)**(-3) - 2) + ((m.x7 - m.x24)**2 + (
    m.x86 - m.x103)**2 + (m.x165 - m.x182)**2)**(-3) * (((m.x7 - m.x24)**2 + (
    m.x86 - m.x103)**2 + (m.x165 - m.x182)**2)**(-3) - 2) + ((m.x7 - m.x25)**2
    + (m.x86 - m.x104)**2 + (m.x165 - m.x183)**2)**(-3) * (((m.x7 - m.x25)**2
    + (m.x86 - m.x104)**2 + (m.x165 - m.x183)**2)**(-3) - 2) + ((m.x7 - m.x26)
    **2 + (m.x86 - m.x105)**2 + (m.x165 - m.x184)**2)**(-3) * (((m.x7 - m.x26)
    **2 + (m.x86 - m.x105)**2 + (m.x165 - m.x184)**2)**(-3) - 2) + ((m.x7 -
    m.x27)**2 + (m.x86 - m.x106)**2 + (m.x165 - m.x185)**2)**(-3) * (((m.x7 -
    m.x27)**2 + (m.x86 - m.x106)**2 + (m.x165 - m.x185)**2)**(-3) - 2) + ((m.x7
    - m.x28)**2 + (m.x86 - m.x107)**2 + (m.x165 - m.x186)**2)**(-3) * (((m.x7
    - m.x28)**2 + (m.x86 - m.x107)**2 + (m.x165 - m.x186)**2)**(-3) - 2) + ((
    m.x7 - m.x29)**2 + (m.x86 - m.x108)**2 + (m.x165 - m.x187)**2)**(-3) * (((
    m.x7 - m.x29)**2 + (m.x86 - m.x108)**2 + (m.x165 - m.x187)**2)**(-3) - 2)
    + ((m.x7 - m.x30)**2 + (m.x86 - m.x109)**2 + (m.x165 - m.x188)**2)**(-3)
    * (((m.x7 - m.x30)**2 + (m.x86 - m.x109)**2 + (m.x165 - m.x188)**2)**(-3)
    - 2) + ((m.x7 - m.x31)**2 + (m.x86 - m.x110)**2 + (m.x165 - m.x189)**2)**(
    -3) * (((m.x7 - m.x31)**2 + (m.x86 - m.x110)**2 + (m.x165 - m.x189)**2)**(
    -3) - 2) + ((m.x7 - m.x32)**2 + (m.x86 - m.x111)**2 + (m.x165 - m.x190)**2)
    **(-3) * (((m.x7 - m.x32)**2 + (m.x86 - m.x111)**2 + (m.x165 - m.x190)**2)
    **(-3) - 2) + ((m.x7 - m.x33)**2 + (m.x86 - m.x112)**2 + (m.x165 - m.x191)
    **2)**(-3) * (((m.x7 - m.x33)**2 + (m.x86 - m.x112)**2 + (m.x165 - m.x191)
    **2)**(-3) - 2) + ((m.x7 - m.x34)**2 + (m.x86 - m.x113)**2 + (m.x165 -
    m.x192)**2)**(-3) * (((m.x7 - m.x34)**2 + (m.x86 - m.x113)**2 + (m.x165 -
    m.x192)**2)**(-3) - 2) + ((m.x7 - m.x35)**2 + (m.x86 - m.x114)**2 + (m.x165
    - m.x193)**2)**(-3) * (((m.x7 - m.x35)**2 + (m.x86 - m.x114)**2 + (m.x165
    - m.x193)**2)**(-3) - 2) + ((m.x7 - m.x36)**2 + (m.x86 - m.x115)**2 + (
    m.x165 - m.x194)**2)**(-3) * (((m.x7 - m.x36)**2 + (m.x86 - m.x115)**2 + (
    m.x165 - m.x194)**2)**(-3) - 2) + ((m.x7 - m.x37)**2 + (m.x86 - m.x116)**2
    + (m.x165 - m.x195)**2)**(-3) * (((m.x7 - m.x37)**2 + (m.x86 - m.x116)**2
    + (m.x165 - m.x195)**2)**(-3) - 2) + ((m.x7 - m.x38)**2 + (m.x86 - m.x117)
    **2 + (m.x165 - m.x196)**2)**(-3) * (((m.x7 - m.x38)**2 + (m.x86 - m.x117)
    **2 + (m.x165 - m.x196)**2)**(-3) - 2) + ((m.x7 - m.x39)**2 + (m.x86 -
    m.x118)**2 + (m.x165 - m.x197)**2)**(-3) * (((m.x7 - m.x39)**2 + (m.x86 -
    m.x118)**2 + (m.x165 - m.x197)**2)**(-3) - 2) + ((m.x7 - m.x40)**2 + (m.x86
    - m.x119)**2 + (m.x165 - m.x198)**2)**(-3) * (((m.x7 - m.x40)**2 + (m.x86
    - m.x119)**2 + (m.x165 - m.x198)**2)**(-3) - 2) + ((m.x7 - m.x41)**2 + (
    m.x86 - m.x120)**2 + (m.x165 - m.x199)**2)**(-3) * (((m.x7 - m.x41)**2 + (
    m.x86 - m.x120)**2 + (m.x165 - m.x199)**2)**(-3) - 2) + ((m.x7 - m.x42)**2
    + (m.x86 - m.x121)**2 + (m.x165 - m.x200)**2)**(-3) * (((m.x7 - m.x42)**2
    + (m.x86 - m.x121)**2 + (m.x165 - m.x200)**2)**(-3) - 2) + ((m.x7 - m.x43)
    **2 + (m.x86 - m.x122)**2 + (m.x165 - m.x201)**2)**(-3) * (((m.x7 - m.x43)
    **2 + (m.x86 - m.x122)**2 + (m.x165 - m.x201)**2)**(-3) - 2) + ((m.x7 -
    m.x44)**2 + (m.x86 - m.x123)**2 + (m.x165 - m.x202)**2)**(-3) * (((m.x7 -
    m.x44)**2 + (m.x86 - m.x123)**2 + (m.x165 - m.x202)**2)**(-3) - 2) + ((m.x7
    - m.x45)**2 + (m.x86 - m.x124)**2 + (m.x165 - m.x203)**2)**(-3) * (((m.x7
    - m.x45)**2 + (m.x86 - m.x124)**2 + (m.x165 - m.x203)**2)**(-3) - 2) + ((
    m.x7 - m.x46)**2 + (m.x86 - m.x125)**2 + (m.x165 - m.x204)**2)**(-3) * (((
    m.x7 - m.x46)**2 + (m.x86 - m.x125)**2 + (m.x165 - m.x204)**2)**(-3) - 2)
    + ((m.x7 - m.x47)**2 + (m.x86 - m.x126)**2 + (m.x165 - m.x205)**2)**(-3)
    * (((m.x7 - m.x47)**2 + (m.x86 - m.x126)**2 + (m.x165 - m.x205)**2)**(-3)
    - 2) + ((m.x7 - m.x48)**2 + (m.x86 - m.x127)**2 + (m.x165 - m.x206)**2)**(
    -3) * (((m.x7 - m.x48)**2 + (m.x86 - m.x127)**2 + (m.x165 - m.x206)**2)**(
    -3) - 2) + ((m.x7 - m.x49)**2 + (m.x86 - m.x128)**2 + (m.x165 - m.x207)**2)
    **(-3) * (((m.x7 - m.x49)**2 + (m.x86 - m.x128)**2 + (m.x165 - m.x207)**2)
    **(-3) - 2) + ((m.x7 - m.x50)**2 + (m.x86 - m.x129)**2 + (m.x165 - m.x208)
    **2)**(-3) * (((m.x7 - m.x50)**2 + (m.x86 - m.x129)**2 + (m.x165 - m.x208)
    **2)**(-3) - 2) + ((m.x7 - m.x51)**2 + (m.x86 - m.x130)**2 + (m.x165 -
    m.x209)**2)**(-3) * (((m.x7 - m.x51)**2 + (m.x86 - m.x130)**2 + (m.x165 -
    m.x209)**2)**(-3) - 2) + ((m.x7 - m.x52)**2 + (m.x86 - m.x131)**2 + (m.x165
    - m.x210)**2)**(-3) * (((m.x7 - m.x52)**2 + (m.x86 - m.x131)**2 + (m.x165
    - m.x210)**2)**(-3) - 2) + ((m.x7 - m.x53)**2 + (m.x86 - m.x132)**2 + (
    m.x165 - m.x211)**2)**(-3) * (((m.x7 - m.x53)**2 + (m.x86 - m.x132)**2 + (
    m.x165 - m.x211)**2)**(-3) - 2) + ((m.x7 - m.x54)**2 + (m.x86 - m.x133)**2
    + (m.x165 - m.x212)**2)**(-3) * (((m.x7 - m.x54)**2 + (m.x86 - m.x133)**2
    + (m.x165 - m.x212)**2)**(-3) - 2) + ((m.x7 - m.x55)**2 + (m.x86 - m.x134)
    **2 + (m.x165 - m.x213)**2)**(-3) * (((m.x7 - m.x55)**2 + (m.x86 - m.x134)
    **2 + (m.x165 - m.x213)**2)**(-3) - 2) + ((m.x7 - m.x56)**2 + (m.x86 -
    m.x135)**2 + (m.x165 - m.x214)**2)**(-3) * (((m.x7 - m.x56)**2 + (m.x86 -
    m.x135)**2 + (m.x165 - m.x214)**2)**(-3) - 2) + ((m.x7 - m.x57)**2 + (m.x86
    - m.x136)**2 + (m.x165 - m.x215)**2)**(-3) * (((m.x7 - m.x57)**2 + (m.x86
    - m.x136)**2 + (m.x165 - m.x215)**2)**(-3) - 2) + ((m.x7 - m.x58)**2 + (
    m.x86 - m.x137)**2 + (m.x165 - m.x216)**2)**(-3) * (((m.x7 - m.x58)**2 + (
    m.x86 - m.x137)**2 + (m.x165 - m.x216)**2)**(-3) - 2) + ((m.x7 - m.x59)**2
    + (m.x86 - m.x138)**2 + (m.x165 - m.x217)**2)**(-3) * (((m.x7 - m.x59)**2
    + (m.x86 - m.x138)**2 + (m.x165 - m.x217)**2)**(-3) - 2) + ((m.x7 - m.x60)
    **2 + (m.x86 - m.x139)**2 + (m.x165 - m.x218)**2)**(-3) * (((m.x7 - m.x60)
    **2 + (m.x86 - m.x139)**2 + (m.x165 - m.x218)**2)**(-3) - 2) + ((m.x7 -
    m.x61)**2 + (m.x86 - m.x140)**2 + (m.x165 - m.x219)**2)**(-3) * (((m.x7 -
    m.x61)**2 + (m.x86 - m.x140)**2 + (m.x165 - m.x219)**2)**(-3) - 2) + ((m.x7
    - m.x62)**2 + (m.x86 - m.x141)**2 + (m.x165 - m.x220)**2)**(-3) * (((m.x7
    - m.x62)**2 + (m.x86 - m.x141)**2 + (m.x165 - m.x220)**2)**(-3) - 2) + ((
    m.x7 - m.x63)**2 + (m.x86 - m.x142)**2 + (m.x165 - m.x221)**2)**(-3) * (((
    m.x7 - m.x63)**2 + (m.x86 - m.x142)**2 + (m.x165 - m.x221)**2)**(-3) - 2)
    + ((m.x7 - m.x64)**2 + (m.x86 - m.x143)**2 + (m.x165 - m.x222)**2)**(-3)
    * (((m.x7 - m.x64)**2 + (m.x86 - m.x143)**2 + (m.x165 - m.x222)**2)**(-3)
    - 2) + ((m.x7 - m.x65)**2 + (m.x86 - m.x144)**2 + (m.x165 - m.x223)**2)**(
    -3) * (((m.x7 - m.x65)**2 + (m.x86 - m.x144)**2 + (m.x165 - m.x223)**2)**(
    -3) - 2) + ((m.x7 - m.x66)**2 + (m.x86 - m.x145)**2 + (m.x165 - m.x224)**2)
    **(-3) * (((m.x7 - m.x66)**2 + (m.x86 - m.x145)**2 + (m.x165 - m.x224)**2)
    **(-3) - 2) + ((m.x7 - m.x67)**2 + (m.x86 - m.x146)**2 + (m.x165 - m.x225)
    **2)**(-3) * (((m.x7 - m.x67)**2 + (m.x86 - m.x146)**2 + (m.x165 - m.x225)
    **2)**(-3) - 2) + ((m.x7 - m.x68)**2 + (m.x86 - m.x147)**2 + (m.x165 -
    m.x226)**2)**(-3) * (((m.x7 - m.x68)**2 + (m.x86 - m.x147)**2 + (m.x165 -
    m.x226)**2)**(-3) - 2) + ((m.x7 - m.x69)**2 + (m.x86 - m.x148)**2 + (m.x165
    - m.x227)**2)**(-3) * (((m.x7 - m.x69)**2 + (m.x86 - m.x148)**2 + (m.x165
    - m.x227)**2)**(-3) - 2) + ((m.x7 - m.x70)**2 + (m.x86 - m.x149)**2 + (
    m.x165 - m.x228)**2)**(-3) * (((m.x7 - m.x70)**2 + (m.x86 - m.x149)**2 + (
    m.x165 - m.x228)**2)**(-3) - 2) + ((m.x7 - m.x71)**2 + (m.x86 - m.x150)**2
    + (m.x165 - m.x229)**2)**(-3) * (((m.x7 - m.x71)**2 + (m.x86 - m.x150)**2
    + (m.x165 - m.x229)**2)**(-3) - 2) + ((m.x7 - m.x72)**2 + (m.x86 - m.x151)
    **2 + (m.x165 - m.x230)**2)**(-3) * (((m.x7 - m.x72)**2 + (m.x86 - m.x151)
    **2 + (m.x165 - m.x230)**2)**(-3) - 2) + ((m.x7 - m.x73)**2 + (m.x86 -
    m.x152)**2 + (m.x165 - m.x231)**2)**(-3) * (((m.x7 - m.x73)**2 + (m.x86 -
    m.x152)**2 + (m.x165 - m.x231)**2)**(-3) - 2) + ((m.x7 - m.x74)**2 + (m.x86
    - m.x153)**2 + (m.x165 - m.x232)**2)**(-3) * (((m.x7 - m.x74)**2 + (m.x86
    - m.x153)**2 + (m.x165 - m.x232)**2)**(-3) - 2) + ((m.x7 - m.x75)**2 + (
    m.x86 - m.x154)**2 + (m.x165 - m.x233)**2)**(-3) * (((m.x7 - m.x75)**2 + (
    m.x86 - m.x154)**2 + (m.x165 - m.x233)**2)**(-3) - 2) + ((m.x7 - m.x76)**2
    + (m.x86 - m.x155)**2 + (m.x165 - m.x234)**2)**(-3) * (((m.x7 - m.x76)**2
    + (m.x86 - m.x155)**2 + (m.x165 - m.x234)**2)**(-3) - 2) + ((m.x7 - m.x77)
    **2 + (m.x86 - m.x156)**2 + (m.x165 - m.x235)**2)**(-3) * (((m.x7 - m.x77)
    **2 + (m.x86 - m.x156)**2 + (m.x165 - m.x235)**2)**(-3) - 2) + ((m.x7 -
    m.x78)**2 + (m.x86 - m.x157)**2 + (m.x165 - m.x236)**2)**(-3) * (((m.x7 -
    m.x78)**2 + (m.x86 - m.x157)**2 + (m.x165 - m.x236)**2)**(-3) - 2) + ((m.x7
    - m.x79)**2 + (m.x86 - m.x158)**2 + (m.x165 - m.x237)**2)**(-3) * (((m.x7
    - m.x79)**2 + (m.x86 - m.x158)**2 + (m.x165 - m.x237)**2)**(-3) - 2) + ((
    m.x8 - m.x9)**2 + (m.x87 - m.x88)**2 + (m.x166 - m.x167)**2)**(-3) * (((
    m.x8 - m.x9)**2 + (m.x87 - m.x88)**2 + (m.x166 - m.x167)**2)**(-3) - 2) + (
    (m.x8 - m.x10)**2 + (m.x87 - m.x89)**2 + (m.x166 - m.x168)**2)**(-3) * (((
    m.x8 - m.x10)**2 + (m.x87 - m.x89)**2 + (m.x166 - m.x168)**2)**(-3) - 2) +
    ((m.x8 - m.x11)**2 + (m.x87 - m.x90)**2 + (m.x166 - m.x169)**2)**(-3) * (((
    m.x8 - m.x11)**2 + (m.x87 - m.x90)**2 + (m.x166 - m.x169)**2)**(-3) - 2) +
    ((m.x8 - m.x12)**2 + (m.x87 - m.x91)**2 + (m.x166 - m.x170)**2)**(-3) * (((
    m.x8 - m.x12)**2 + (m.x87 - m.x91)**2 + (m.x166 - m.x170)**2)**(-3) - 2) +
    ((m.x8 - m.x13)**2 + (m.x87 - m.x92)**2 + (m.x166 - m.x171)**2)**(-3) * (((
    m.x8 - m.x13)**2 + (m.x87 - m.x92)**2 + (m.x166 - m.x171)**2)**(-3) - 2) +
    ((m.x8 - m.x14)**2 + (m.x87 - m.x93)**2 + (m.x166 - m.x172)**2)**(-3) * (((
    m.x8 - m.x14)**2 + (m.x87 - m.x93)**2 + (m.x166 - m.x172)**2)**(-3) - 2) +
    ((m.x8 - m.x15)**2 + (m.x87 - m.x94)**2 + (m.x166 - m.x173)**2)**(-3) * (((
    m.x8 - m.x15)**2 + (m.x87 - m.x94)**2 + (m.x166 - m.x173)**2)**(-3) - 2) +
    ((m.x8 - m.x16)**2 + (m.x87 - m.x95)**2 + (m.x166 - m.x174)**2)**(-3) * (((
    m.x8 - m.x16)**2 + (m.x87 - m.x95)**2 + (m.x166 - m.x174)**2)**(-3) - 2) +
    ((m.x8 - m.x17)**2 + (m.x87 - m.x96)**2 + (m.x166 - m.x175)**2)**(-3) * (((
    m.x8 - m.x17)**2 + (m.x87 - m.x96)**2 + (m.x166 - m.x175)**2)**(-3) - 2) +
    ((m.x8 - m.x18)**2 + (m.x87 - m.x97)**2 + (m.x166 - m.x176)**2)**(-3) * (((
    m.x8 - m.x18)**2 + (m.x87 - m.x97)**2 + (m.x166 - m.x176)**2)**(-3) - 2) +
    ((m.x8 - m.x19)**2 + (m.x87 - m.x98)**2 + (m.x166 - m.x177)**2)**(-3) * (((
    m.x8 - m.x19)**2 + (m.x87 - m.x98)**2 + (m.x166 - m.x177)**2)**(-3) - 2) +
    ((m.x8 - m.x20)**2 + (m.x87 - m.x99)**2 + (m.x166 - m.x178)**2)**(-3) * (((
    m.x8 - m.x20)**2 + (m.x87 - m.x99)**2 + (m.x166 - m.x178)**2)**(-3) - 2) +
    ((m.x8 - m.x21)**2 + (m.x87 - m.x100)**2 + (m.x166 - m.x179)**2)**(-3) * ((
    (m.x8 - m.x21)**2 + (m.x87 - m.x100)**2 + (m.x166 - m.x179)**2)**(-3) - 2)
    + ((m.x8 - m.x22)**2 + (m.x87 - m.x101)**2 + (m.x166 - m.x180)**2)**(-3)
    * (((m.x8 - m.x22)**2 + (m.x87 - m.x101)**2 + (m.x166 - m.x180)**2)**(-3)
    - 2) + ((m.x8 - m.x23)**2 + (m.x87 - m.x102)**2 + (m.x166 - m.x181)**2)**(
    -3) * (((m.x8 - m.x23)**2 + (m.x87 - m.x102)**2 + (m.x166 - m.x181)**2)**(
    -3) - 2) + ((m.x8 - m.x24)**2 + (m.x87 - m.x103)**2 + (m.x166 - m.x182)**2)
    **(-3) * (((m.x8 - m.x24)**2 + (m.x87 - m.x103)**2 + (m.x166 - m.x182)**2)
    **(-3) - 2) + ((m.x8 - m.x25)**2 + (m.x87 - m.x104)**2 + (m.x166 - m.x183)
    **2)**(-3) * (((m.x8 - m.x25)**2 + (m.x87 - m.x104)**2 + (m.x166 - m.x183)
    **2)**(-3) - 2) + ((m.x8 - m.x26)**2 + (m.x87 - m.x105)**2 + (m.x166 -
    m.x184)**2)**(-3) * (((m.x8 - m.x26)**2 + (m.x87 - m.x105)**2 + (m.x166 -
    m.x184)**2)**(-3) - 2) + ((m.x8 - m.x27)**2 + (m.x87 - m.x106)**2 + (m.x166
    - m.x185)**2)**(-3) * (((m.x8 - m.x27)**2 + (m.x87 - m.x106)**2 + (m.x166
    - m.x185)**2)**(-3) - 2) + ((m.x8 - m.x28)**2 + (m.x87 - m.x107)**2 + (
    m.x166 - m.x186)**2)**(-3) * (((m.x8 - m.x28)**2 + (m.x87 - m.x107)**2 + (
    m.x166 - m.x186)**2)**(-3) - 2) + ((m.x8 - m.x29)**2 + (m.x87 - m.x108)**2
    + (m.x166 - m.x187)**2)**(-3) * (((m.x8 - m.x29)**2 + (m.x87 - m.x108)**2
    + (m.x166 - m.x187)**2)**(-3) - 2) + ((m.x8 - m.x30)**2 + (m.x87 - m.x109)
    **2 + (m.x166 - m.x188)**2)**(-3) * (((m.x8 - m.x30)**2 + (m.x87 - m.x109)
    **2 + (m.x166 - m.x188)**2)**(-3) - 2) + ((m.x8 - m.x31)**2 + (m.x87 -
    m.x110)**2 + (m.x166 - m.x189)**2)**(-3) * (((m.x8 - m.x31)**2 + (m.x87 -
    m.x110)**2 + (m.x166 - m.x189)**2)**(-3) - 2) + ((m.x8 - m.x32)**2 + (m.x87
    - m.x111)**2 + (m.x166 - m.x190)**2)**(-3) * (((m.x8 - m.x32)**2 + (m.x87
    - m.x111)**2 + (m.x166 - m.x190)**2)**(-3) - 2) + ((m.x8 - m.x33)**2 + (
    m.x87 - m.x112)**2 + (m.x166 - m.x191)**2)**(-3) * (((m.x8 - m.x33)**2 + (
    m.x87 - m.x112)**2 + (m.x166 - m.x191)**2)**(-3) - 2) + ((m.x8 - m.x34)**2
    + (m.x87 - m.x113)**2 + (m.x166 - m.x192)**2)**(-3) * (((m.x8 - m.x34)**2
    + (m.x87 - m.x113)**2 + (m.x166 - m.x192)**2)**(-3) - 2) + ((m.x8 - m.x35)
    **2 + (m.x87 - m.x114)**2 + (m.x166 - m.x193)**2)**(-3) * (((m.x8 - m.x35)
    **2 + (m.x87 - m.x114)**2 + (m.x166 - m.x193)**2)**(-3) - 2) + ((m.x8 -
    m.x36)**2 + (m.x87 - m.x115)**2 + (m.x166 - m.x194)**2)**(-3) * (((m.x8 -
    m.x36)**2 + (m.x87 - m.x115)**2 + (m.x166 - m.x194)**2)**(-3) - 2) + ((m.x8
    - m.x37)**2 + (m.x87 - m.x116)**2 + (m.x166 - m.x195)**2)**(-3) * (((m.x8
    - m.x37)**2 + (m.x87 - m.x116)**2 + (m.x166 - m.x195)**2)**(-3) - 2) + ((
    m.x8 - m.x38)**2 + (m.x87 - m.x117)**2 + (m.x166 - m.x196)**2)**(-3) * (((
    m.x8 - m.x38)**2 + (m.x87 - m.x117)**2 + (m.x166 - m.x196)**2)**(-3) - 2)
    + ((m.x8 - m.x39)**2 + (m.x87 - m.x118)**2 + (m.x166 - m.x197)**2)**(-3)
    * (((m.x8 - m.x39)**2 + (m.x87 - m.x118)**2 + (m.x166 - m.x197)**2)**(-3)
    - 2) + ((m.x8 - m.x40)**2 + (m.x87 - m.x119)**2 + (m.x166 - m.x198)**2)**(
    -3) * (((m.x8 - m.x40)**2 + (m.x87 - m.x119)**2 + (m.x166 - m.x198)**2)**(
    -3) - 2) + ((m.x8 - m.x41)**2 + (m.x87 - m.x120)**2 + (m.x166 - m.x199)**2)
    **(-3) * (((m.x8 - m.x41)**2 + (m.x87 - m.x120)**2 + (m.x166 - m.x199)**2)
    **(-3) - 2) + ((m.x8 - m.x42)**2 + (m.x87 - m.x121)**2 + (m.x166 - m.x200)
    **2)**(-3) * (((m.x8 - m.x42)**2 + (m.x87 - m.x121)**2 + (m.x166 - m.x200)
    **2)**(-3) - 2) + ((m.x8 - m.x43)**2 + (m.x87 - m.x122)**2 + (m.x166 -
    m.x201)**2)**(-3) * (((m.x8 - m.x43)**2 + (m.x87 - m.x122)**2 + (m.x166 -
    m.x201)**2)**(-3) - 2) + ((m.x8 - m.x44)**2 + (m.x87 - m.x123)**2 + (m.x166
    - m.x202)**2)**(-3) * (((m.x8 - m.x44)**2 + (m.x87 - m.x123)**2 + (m.x166
    - m.x202)**2)**(-3) - 2) + ((m.x8 - m.x45)**2 + (m.x87 - m.x124)**2 + (
    m.x166 - m.x203)**2)**(-3) * (((m.x8 - m.x45)**2 + (m.x87 - m.x124)**2 + (
    m.x166 - m.x203)**2)**(-3) - 2) + ((m.x8 - m.x46)**2 + (m.x87 - m.x125)**2
    + (m.x166 - m.x204)**2)**(-3) * (((m.x8 - m.x46)**2 + (m.x87 - m.x125)**2
    + (m.x166 - m.x204)**2)**(-3) - 2) + ((m.x8 - m.x47)**2 + (m.x87 - m.x126)
    **2 + (m.x166 - m.x205)**2)**(-3) * (((m.x8 - m.x47)**2 + (m.x87 - m.x126)
    **2 + (m.x166 - m.x205)**2)**(-3) - 2) + ((m.x8 - m.x48)**2 + (m.x87 -
    m.x127)**2 + (m.x166 - m.x206)**2)**(-3) * (((m.x8 - m.x48)**2 + (m.x87 -
    m.x127)**2 + (m.x166 - m.x206)**2)**(-3) - 2) + ((m.x8 - m.x49)**2 + (m.x87
    - m.x128)**2 + (m.x166 - m.x207)**2)**(-3) * (((m.x8 - m.x49)**2 + (m.x87
    - m.x128)**2 + (m.x166 - m.x207)**2)**(-3) - 2) + ((m.x8 - m.x50)**2 + (
    m.x87 - m.x129)**2 + (m.x166 - m.x208)**2)**(-3) * (((m.x8 - m.x50)**2 + (
    m.x87 - m.x129)**2 + (m.x166 - m.x208)**2)**(-3) - 2) + ((m.x8 - m.x51)**2
    + (m.x87 - m.x130)**2 + (m.x166 - m.x209)**2)**(-3) * (((m.x8 - m.x51)**2
    + (m.x87 - m.x130)**2 + (m.x166 - m.x209)**2)**(-3) - 2) + ((m.x8 - m.x52)
    **2 + (m.x87 - m.x131)**2 + (m.x166 - m.x210)**2)**(-3) * (((m.x8 - m.x52)
    **2 + (m.x87 - m.x131)**2 + (m.x166 - m.x210)**2)**(-3) - 2) + ((m.x8 -
    m.x53)**2 + (m.x87 - m.x132)**2 + (m.x166 - m.x211)**2)**(-3) * (((m.x8 -
    m.x53)**2 + (m.x87 - m.x132)**2 + (m.x166 - m.x211)**2)**(-3) - 2) + ((m.x8
    - m.x54)**2 + (m.x87 - m.x133)**2 + (m.x166 - m.x212)**2)**(-3) * (((m.x8
    - m.x54)**2 + (m.x87 - m.x133)**2 + (m.x166 - m.x212)**2)**(-3) - 2) + ((
    m.x8 - m.x55)**2 + (m.x87 - m.x134)**2 + (m.x166 - m.x213)**2)**(-3) * (((
    m.x8 - m.x55)**2 + (m.x87 - m.x134)**2 + (m.x166 - m.x213)**2)**(-3) - 2)
    + ((m.x8 - m.x56)**2 + (m.x87 - m.x135)**2 + (m.x166 - m.x214)**2)**(-3)
    * (((m.x8 - m.x56)**2 + (m.x87 - m.x135)**2 + (m.x166 - m.x214)**2)**(-3)
    - 2) + ((m.x8 - m.x57)**2 + (m.x87 - m.x136)**2 + (m.x166 - m.x215)**2)**(
    -3) * (((m.x8 - m.x57)**2 + (m.x87 - m.x136)**2 + (m.x166 - m.x215)**2)**(
    -3) - 2) + ((m.x8 - m.x58)**2 + (m.x87 - m.x137)**2 + (m.x166 - m.x216)**2)
    **(-3) * (((m.x8 - m.x58)**2 + (m.x87 - m.x137)**2 + (m.x166 - m.x216)**2)
    **(-3) - 2) + ((m.x8 - m.x59)**2 + (m.x87 - m.x138)**2 + (m.x166 - m.x217)
    **2)**(-3) * (((m.x8 - m.x59)**2 + (m.x87 - m.x138)**2 + (m.x166 - m.x217)
    **2)**(-3) - 2) + ((m.x8 - m.x60)**2 + (m.x87 - m.x139)**2 + (m.x166 -
    m.x218)**2)**(-3) * (((m.x8 - m.x60)**2 + (m.x87 - m.x139)**2 + (m.x166 -
    m.x218)**2)**(-3) - 2) + ((m.x8 - m.x61)**2 + (m.x87 - m.x140)**2 + (m.x166
    - m.x219)**2)**(-3) * (((m.x8 - m.x61)**2 + (m.x87 - m.x140)**2 + (m.x166
    - m.x219)**2)**(-3) - 2) + ((m.x8 - m.x62)**2 + (m.x87 - m.x141)**2 + (
    m.x166 - m.x220)**2)**(-3) * (((m.x8 - m.x62)**2 + (m.x87 - m.x141)**2 + (
    m.x166 - m.x220)**2)**(-3) - 2) + ((m.x8 - m.x63)**2 + (m.x87 - m.x142)**2
    + (m.x166 - m.x221)**2)**(-3) * (((m.x8 - m.x63)**2 + (m.x87 - m.x142)**2
    + (m.x166 - m.x221)**2)**(-3) - 2) + ((m.x8 - m.x64)**2 + (m.x87 - m.x143)
    **2 + (m.x166 - m.x222)**2)**(-3) * (((m.x8 - m.x64)**2 + (m.x87 - m.x143)
    **2 + (m.x166 - m.x222)**2)**(-3) - 2) + ((m.x8 - m.x65)**2 + (m.x87 -
    m.x144)**2 + (m.x166 - m.x223)**2)**(-3) * (((m.x8 - m.x65)**2 + (m.x87 -
    m.x144)**2 + (m.x166 - m.x223)**2)**(-3) - 2) + ((m.x8 - m.x66)**2 + (m.x87
    - m.x145)**2 + (m.x166 - m.x224)**2)**(-3) * (((m.x8 - m.x66)**2 + (m.x87
    - m.x145)**2 + (m.x166 - m.x224)**2)**(-3) - 2) + ((m.x8 - m.x67)**2 + (
    m.x87 - m.x146)**2 + (m.x166 - m.x225)**2)**(-3) * (((m.x8 - m.x67)**2 + (
    m.x87 - m.x146)**2 + (m.x166 - m.x225)**2)**(-3) - 2) + ((m.x8 - m.x68)**2
    + (m.x87 - m.x147)**2 + (m.x166 - m.x226)**2)**(-3) * (((m.x8 - m.x68)**2
    + (m.x87 - m.x147)**2 + (m.x166 - m.x226)**2)**(-3) - 2) + ((m.x8 - m.x69)
    **2 + (m.x87 - m.x148)**2 + (m.x166 - m.x227)**2)**(-3) * (((m.x8 - m.x69)
    **2 + (m.x87 - m.x148)**2 + (m.x166 - m.x227)**2)**(-3) - 2) + ((m.x8 -
    m.x70)**2 + (m.x87 - m.x149)**2 + (m.x166 - m.x228)**2)**(-3) * (((m.x8 -
    m.x70)**2 + (m.x87 - m.x149)**2 + (m.x166 - m.x228)**2)**(-3) - 2) + ((m.x8
    - m.x71)**2 + (m.x87 - m.x150)**2 + (m.x166 - m.x229)**2)**(-3) * (((m.x8
    - m.x71)**2 + (m.x87 - m.x150)**2 + (m.x166 - m.x229)**2)**(-3) - 2) + ((
    m.x8 - m.x72)**2 + (m.x87 - m.x151)**2 + (m.x166 - m.x230)**2)**(-3) * (((
    m.x8 - m.x72)**2 + (m.x87 - m.x151)**2 + (m.x166 - m.x230)**2)**(-3) - 2)
    + ((m.x8 - m.x73)**2 + (m.x87 - m.x152)**2 + (m.x166 - m.x231)**2)**(-3)
    * (((m.x8 - m.x73)**2 + (m.x87 - m.x152)**2 + (m.x166 - m.x231)**2)**(-3)
    - 2) + ((m.x8 - m.x74)**2 + (m.x87 - m.x153)**2 + (m.x166 - m.x232)**2)**(
    -3) * (((m.x8 - m.x74)**2 + (m.x87 - m.x153)**2 + (m.x166 - m.x232)**2)**(
    -3) - 2) + ((m.x8 - m.x75)**2 + (m.x87 - m.x154)**2 + (m.x166 - m.x233)**2)
    **(-3) * (((m.x8 - m.x75)**2 + (m.x87 - m.x154)**2 + (m.x166 - m.x233)**2)
    **(-3) - 2) + ((m.x8 - m.x76)**2 + (m.x87 - m.x155)**2 + (m.x166 - m.x234)
    **2)**(-3) * (((m.x8 - m.x76)**2 + (m.x87 - m.x155)**2 + (m.x166 - m.x234)
    **2)**(-3) - 2) + ((m.x8 - m.x77)**2 + (m.x87 - m.x156)**2 + (m.x166 -
    m.x235)**2)**(-3) * (((m.x8 - m.x77)**2 + (m.x87 - m.x156)**2 + (m.x166 -
    m.x235)**2)**(-3) - 2) + ((m.x8 - m.x78)**2 + (m.x87 - m.x157)**2 + (m.x166
    - m.x236)**2)**(-3) * (((m.x8 - m.x78)**2 + (m.x87 - m.x157)**2 + (m.x166
    - m.x236)**2)**(-3) - 2) + ((m.x8 - m.x79)**2 + (m.x87 - m.x158)**2 + (
    m.x166 - m.x237)**2)**(-3) * (((m.x8 - m.x79)**2 + (m.x87 - m.x158)**2 + (
    m.x166 - m.x237)**2)**(-3) - 2) + ((m.x9 - m.x10)**2 + (m.x88 - m.x89)**2
    + (m.x167 - m.x168)**2)**(-3) * (((m.x9 - m.x10)**2 + (m.x88 - m.x89)**2
    + (m.x167 - m.x168)**2)**(-3) - 2) + ((m.x9 - m.x11)**2 + (m.x88 - m.x90)
    **2 + (m.x167 - m.x169)**2)**(-3) * (((m.x9 - m.x11)**2 + (m.x88 - m.x90)**
    2 + (m.x167 - m.x169)**2)**(-3) - 2) + ((m.x9 - m.x12)**2 + (m.x88 - m.x91)
    **2 + (m.x167 - m.x170)**2)**(-3) * (((m.x9 - m.x12)**2 + (m.x88 - m.x91)**
    2 + (m.x167 - m.x170)**2)**(-3) - 2) + ((m.x9 - m.x13)**2 + (m.x88 - m.x92)
    **2 + (m.x167 - m.x171)**2)**(-3) * (((m.x9 - m.x13)**2 + (m.x88 - m.x92)**
    2 + (m.x167 - m.x171)**2)**(-3) - 2) + ((m.x9 - m.x14)**2 + (m.x88 - m.x93)
    **2 + (m.x167 - m.x172)**2)**(-3) * (((m.x9 - m.x14)**2 + (m.x88 - m.x93)**
    2 + (m.x167 - m.x172)**2)**(-3) - 2) + ((m.x9 - m.x15)**2 + (m.x88 - m.x94)
    **2 + (m.x167 - m.x173)**2)**(-3) * (((m.x9 - m.x15)**2 + (m.x88 - m.x94)**
    2 + (m.x167 - m.x173)**2)**(-3) - 2) + ((m.x9 - m.x16)**2 + (m.x88 - m.x95)
    **2 + (m.x167 - m.x174)**2)**(-3) * (((m.x9 - m.x16)**2 + (m.x88 - m.x95)**
    2 + (m.x167 - m.x174)**2)**(-3) - 2) + ((m.x9 - m.x17)**2 + (m.x88 - m.x96)
    **2 + (m.x167 - m.x175)**2)**(-3) * (((m.x9 - m.x17)**2 + (m.x88 - m.x96)**
    2 + (m.x167 - m.x175)**2)**(-3) - 2) + ((m.x9 - m.x18)**2 + (m.x88 - m.x97)
    **2 + (m.x167 - m.x176)**2)**(-3) * (((m.x9 - m.x18)**2 + (m.x88 - m.x97)**
    2 + (m.x167 - m.x176)**2)**(-3) - 2) + ((m.x9 - m.x19)**2 + (m.x88 - m.x98)
    **2 + (m.x167 - m.x177)**2)**(-3) * (((m.x9 - m.x19)**2 + (m.x88 - m.x98)**
    2 + (m.x167 - m.x177)**2)**(-3) - 2) + ((m.x9 - m.x20)**2 + (m.x88 - m.x99)
    **2 + (m.x167 - m.x178)**2)**(-3) * (((m.x9 - m.x20)**2 + (m.x88 - m.x99)**
    2 + (m.x167 - m.x178)**2)**(-3) - 2) + ((m.x9 - m.x21)**2 + (m.x88 - m.x100)
    **2 + (m.x167 - m.x179)**2)**(-3) * (((m.x9 - m.x21)**2 + (m.x88 - m.x100)
    **2 + (m.x167 - m.x179)**2)**(-3) - 2) + ((m.x9 - m.x22)**2 + (m.x88 -
    m.x101)**2 + (m.x167 - m.x180)**2)**(-3) * (((m.x9 - m.x22)**2 + (m.x88 -
    m.x101)**2 + (m.x167 - m.x180)**2)**(-3) - 2) + ((m.x9 - m.x23)**2 + (m.x88
    - m.x102)**2 + (m.x167 - m.x181)**2)**(-3) * (((m.x9 - m.x23)**2 + (m.x88
    - m.x102)**2 + (m.x167 - m.x181)**2)**(-3) - 2) + ((m.x9 - m.x24)**2 + (
    m.x88 - m.x103)**2 + (m.x167 - m.x182)**2)**(-3) * (((m.x9 - m.x24)**2 + (
    m.x88 - m.x103)**2 + (m.x167 - m.x182)**2)**(-3) - 2) + ((m.x9 - m.x25)**2
    + (m.x88 - m.x104)**2 + (m.x167 - m.x183)**2)**(-3) * (((m.x9 - m.x25)**2
    + (m.x88 - m.x104)**2 + (m.x167 - m.x183)**2)**(-3) - 2) + ((m.x9 - m.x26)
    **2 + (m.x88 - m.x105)**2 + (m.x167 - m.x184)**2)**(-3) * (((m.x9 - m.x26)
    **2 + (m.x88 - m.x105)**2 + (m.x167 - m.x184)**2)**(-3) - 2) + ((m.x9 -
    m.x27)**2 + (m.x88 - m.x106)**2 + (m.x167 - m.x185)**2)**(-3) * (((m.x9 -
    m.x27)**2 + (m.x88 - m.x106)**2 + (m.x167 - m.x185)**2)**(-3) - 2) + ((m.x9
    - m.x28)**2 + (m.x88 - m.x107)**2 + (m.x167 - m.x186)**2)**(-3) * (((m.x9
    - m.x28)**2 + (m.x88 - m.x107)**2 + (m.x167 - m.x186)**2)**(-3) - 2) + ((
    m.x9 - m.x29)**2 + (m.x88 - m.x108)**2 + (m.x167 - m.x187)**2)**(-3) * (((
    m.x9 - m.x29)**2 + (m.x88 - m.x108)**2 + (m.x167 - m.x187)**2)**(-3) - 2)
    + ((m.x9 - m.x30)**2 + (m.x88 - m.x109)**2 + (m.x167 - m.x188)**2)**(-3)
    * (((m.x9 - m.x30)**2 + (m.x88 - m.x109)**2 + (m.x167 - m.x188)**2)**(-3)
    - 2) + ((m.x9 - m.x31)**2 + (m.x88 - m.x110)**2 + (m.x167 - m.x189)**2)**(
    -3) * (((m.x9 - m.x31)**2 + (m.x88 - m.x110)**2 + (m.x167 - m.x189)**2)**(
    -3) - 2) + ((m.x9 - m.x32)**2 + (m.x88 - m.x111)**2 + (m.x167 - m.x190)**2)
    **(-3) * (((m.x9 - m.x32)**2 + (m.x88 - m.x111)**2 + (m.x167 - m.x190)**2)
    **(-3) - 2) + ((m.x9 - m.x33)**2 + (m.x88 - m.x112)**2 + (m.x167 - m.x191)
    **2)**(-3) * (((m.x9 - m.x33)**2 + (m.x88 - m.x112)**2 + (m.x167 - m.x191)
    **2)**(-3) - 2) + ((m.x9 - m.x34)**2 + (m.x88 - m.x113)**2 + (m.x167 -
    m.x192)**2)**(-3) * (((m.x9 - m.x34)**2 + (m.x88 - m.x113)**2 + (m.x167 -
    m.x192)**2)**(-3) - 2) + ((m.x9 - m.x35)**2 + (m.x88 - m.x114)**2 + (m.x167
    - m.x193)**2)**(-3) * (((m.x9 - m.x35)**2 + (m.x88 - m.x114)**2 + (m.x167
    - m.x193)**2)**(-3) - 2) + ((m.x9 - m.x36)**2 + (m.x88 - m.x115)**2 + (
    m.x167 - m.x194)**2)**(-3) * (((m.x9 - m.x36)**2 + (m.x88 - m.x115)**2 + (
    m.x167 - m.x194)**2)**(-3) - 2) + ((m.x9 - m.x37)**2 + (m.x88 - m.x116)**2
    + (m.x167 - m.x195)**2)**(-3) * (((m.x9 - m.x37)**2 + (m.x88 - m.x116)**2
    + (m.x167 - m.x195)**2)**(-3) - 2) + ((m.x9 - m.x38)**2 + (m.x88 - m.x117)
    **2 + (m.x167 - m.x196)**2)**(-3) * (((m.x9 - m.x38)**2 + (m.x88 - m.x117)
    **2 + (m.x167 - m.x196)**2)**(-3) - 2) + ((m.x9 - m.x39)**2 + (m.x88 -
    m.x118)**2 + (m.x167 - m.x197)**2)**(-3) * (((m.x9 - m.x39)**2 + (m.x88 -
    m.x118)**2 + (m.x167 - m.x197)**2)**(-3) - 2) + ((m.x9 - m.x40)**2 + (m.x88
    - m.x119)**2 + (m.x167 - m.x198)**2)**(-3) * (((m.x9 - m.x40)**2 + (m.x88
    - m.x119)**2 + (m.x167 - m.x198)**2)**(-3) - 2) + ((m.x9 - m.x41)**2 + (
    m.x88 - m.x120)**2 + (m.x167 - m.x199)**2)**(-3) * (((m.x9 - m.x41)**2 + (
    m.x88 - m.x120)**2 + (m.x167 - m.x199)**2)**(-3) - 2) + ((m.x9 - m.x42)**2
    + (m.x88 - m.x121)**2 + (m.x167 - m.x200)**2)**(-3) * (((m.x9 - m.x42)**2
    + (m.x88 - m.x121)**2 + (m.x167 - m.x200)**2)**(-3) - 2) + ((m.x9 - m.x43)
    **2 + (m.x88 - m.x122)**2 + (m.x167 - m.x201)**2)**(-3) * (((m.x9 - m.x43)
    **2 + (m.x88 - m.x122)**2 + (m.x167 - m.x201)**2)**(-3) - 2) + ((m.x9 -
    m.x44)**2 + (m.x88 - m.x123)**2 + (m.x167 - m.x202)**2)**(-3) * (((m.x9 -
    m.x44)**2 + (m.x88 - m.x123)**2 + (m.x167 - m.x202)**2)**(-3) - 2) + ((m.x9
    - m.x45)**2 + (m.x88 - m.x124)**2 + (m.x167 - m.x203)**2)**(-3) * (((m.x9
    - m.x45)**2 + (m.x88 - m.x124)**2 + (m.x167 - m.x203)**2)**(-3) - 2) + ((
    m.x9 - m.x46)**2 + (m.x88 - m.x125)**2 + (m.x167 - m.x204)**2)**(-3) * (((
    m.x9 - m.x46)**2 + (m.x88 - m.x125)**2 + (m.x167 - m.x204)**2)**(-3) - 2)
    + ((m.x9 - m.x47)**2 + (m.x88 - m.x126)**2 + (m.x167 - m.x205)**2)**(-3)
    * (((m.x9 - m.x47)**2 + (m.x88 - m.x126)**2 + (m.x167 - m.x205)**2)**(-3)
    - 2) + ((m.x9 - m.x48)**2 + (m.x88 - m.x127)**2 + (m.x167 - m.x206)**2)**(
    -3) * (((m.x9 - m.x48)**2 + (m.x88 - m.x127)**2 + (m.x167 - m.x206)**2)**(
    -3) - 2) + ((m.x9 - m.x49)**2 + (m.x88 - m.x128)**2 + (m.x167 - m.x207)**2)
    **(-3) * (((m.x9 - m.x49)**2 + (m.x88 - m.x128)**2 + (m.x167 - m.x207)**2)
    **(-3) - 2) + ((m.x9 - m.x50)**2 + (m.x88 - m.x129)**2 + (m.x167 - m.x208)
    **2)**(-3) * (((m.x9 - m.x50)**2 + (m.x88 - m.x129)**2 + (m.x167 - m.x208)
    **2)**(-3) - 2) + ((m.x9 - m.x51)**2 + (m.x88 - m.x130)**2 + (m.x167 -
    m.x209)**2)**(-3) * (((m.x9 - m.x51)**2 + (m.x88 - m.x130)**2 + (m.x167 -
    m.x209)**2)**(-3) - 2) + ((m.x9 - m.x52)**2 + (m.x88 - m.x131)**2 + (m.x167
    - m.x210)**2)**(-3) * (((m.x9 - m.x52)**2 + (m.x88 - m.x131)**2 + (m.x167
    - m.x210)**2)**(-3) - 2) + ((m.x9 - m.x53)**2 + (m.x88 - m.x132)**2 + (
    m.x167 - m.x211)**2)**(-3) * (((m.x9 - m.x53)**2 + (m.x88 - m.x132)**2 + (
    m.x167 - m.x211)**2)**(-3) - 2) + ((m.x9 - m.x54)**2 + (m.x88 - m.x133)**2
    + (m.x167 - m.x212)**2)**(-3) * (((m.x9 - m.x54)**2 + (m.x88 - m.x133)**2
    + (m.x167 - m.x212)**2)**(-3) - 2) + ((m.x9 - m.x55)**2 + (m.x88 - m.x134)
    **2 + (m.x167 - m.x213)**2)**(-3) * (((m.x9 - m.x55)**2 + (m.x88 - m.x134)
    **2 + (m.x167 - m.x213)**2)**(-3) - 2) + ((m.x9 - m.x56)**2 + (m.x88 -
    m.x135)**2 + (m.x167 - m.x214)**2)**(-3) * (((m.x9 - m.x56)**2 + (m.x88 -
    m.x135)**2 + (m.x167 - m.x214)**2)**(-3) - 2) + ((m.x9 - m.x57)**2 + (m.x88
    - m.x136)**2 + (m.x167 - m.x215)**2)**(-3) * (((m.x9 - m.x57)**2 + (m.x88
    - m.x136)**2 + (m.x167 - m.x215)**2)**(-3) - 2) + ((m.x9 - m.x58)**2 + (
    m.x88 - m.x137)**2 + (m.x167 - m.x216)**2)**(-3) * (((m.x9 - m.x58)**2 + (
    m.x88 - m.x137)**2 + (m.x167 - m.x216)**2)**(-3) - 2) + ((m.x9 - m.x59)**2
    + (m.x88 - m.x138)**2 + (m.x167 - m.x217)**2)**(-3) * (((m.x9 - m.x59)**2
    + (m.x88 - m.x138)**2 + (m.x167 - m.x217)**2)**(-3) - 2) + ((m.x9 - m.x60)
    **2 + (m.x88 - m.x139)**2 + (m.x167 - m.x218)**2)**(-3) * (((m.x9 - m.x60)
    **2 + (m.x88 - m.x139)**2 + (m.x167 - m.x218)**2)**(-3) - 2) + ((m.x9 -
    m.x61)**2 + (m.x88 - m.x140)**2 + (m.x167 - m.x219)**2)**(-3) * (((m.x9 -
    m.x61)**2 + (m.x88 - m.x140)**2 + (m.x167 - m.x219)**2)**(-3) - 2) + ((m.x9
    - m.x62)**2 + (m.x88 - m.x141)**2 + (m.x167 - m.x220)**2)**(-3) * (((m.x9
    - m.x62)**2 + (m.x88 - m.x141)**2 + (m.x167 - m.x220)**2)**(-3) - 2) + ((
    m.x9 - m.x63)**2 + (m.x88 - m.x142)**2 + (m.x167 - m.x221)**2)**(-3) * (((
    m.x9 - m.x63)**2 + (m.x88 - m.x142)**2 + (m.x167 - m.x221)**2)**(-3) - 2)
    + ((m.x9 - m.x64)**2 + (m.x88 - m.x143)**2 + (m.x167 - m.x222)**2)**(-3)
    * (((m.x9 - m.x64)**2 + (m.x88 - m.x143)**2 + (m.x167 - m.x222)**2)**(-3)
    - 2) + ((m.x9 - m.x65)**2 + (m.x88 - m.x144)**2 + (m.x167 - m.x223)**2)**(
    -3) * (((m.x9 - m.x65)**2 + (m.x88 - m.x144)**2 + (m.x167 - m.x223)**2)**(
    -3) - 2) + ((m.x9 - m.x66)**2 + (m.x88 - m.x145)**2 + (m.x167 - m.x224)**2)
    **(-3) * (((m.x9 - m.x66)**2 + (m.x88 - m.x145)**2 + (m.x167 - m.x224)**2)
    **(-3) - 2) + ((m.x9 - m.x67)**2 + (m.x88 - m.x146)**2 + (m.x167 - m.x225)
    **2)**(-3) * (((m.x9 - m.x67)**2 + (m.x88 - m.x146)**2 + (m.x167 - m.x225)
    **2)**(-3) - 2) + ((m.x9 - m.x68)**2 + (m.x88 - m.x147)**2 + (m.x167 -
    m.x226)**2)**(-3) * (((m.x9 - m.x68)**2 + (m.x88 - m.x147)**2 + (m.x167 -
    m.x226)**2)**(-3) - 2) + ((m.x9 - m.x69)**2 + (m.x88 - m.x148)**2 + (m.x167
    - m.x227)**2)**(-3) * (((m.x9 - m.x69)**2 + (m.x88 - m.x148)**2 + (m.x167
    - m.x227)**2)**(-3) - 2) + ((m.x9 - m.x70)**2 + (m.x88 - m.x149)**2 + (
    m.x167 - m.x228)**2)**(-3) * (((m.x9 - m.x70)**2 + (m.x88 - m.x149)**2 + (
    m.x167 - m.x228)**2)**(-3) - 2) + ((m.x9 - m.x71)**2 + (m.x88 - m.x150)**2
    + (m.x167 - m.x229)**2)**(-3) * (((m.x9 - m.x71)**2 + (m.x88 - m.x150)**2
    + (m.x167 - m.x229)**2)**(-3) - 2) + ((m.x9 - m.x72)**2 + (m.x88 - m.x151)
    **2 + (m.x167 - m.x230)**2)**(-3) * (((m.x9 - m.x72)**2 + (m.x88 - m.x151)
    **2 + (m.x167 - m.x230)**2)**(-3) - 2) + ((m.x9 - m.x73)**2 + (m.x88 -
    m.x152)**2 + (m.x167 - m.x231)**2)**(-3) * (((m.x9 - m.x73)**2 + (m.x88 -
    m.x152)**2 + (m.x167 - m.x231)**2)**(-3) - 2) + ((m.x9 - m.x74)**2 + (m.x88
    - m.x153)**2 + (m.x167 - m.x232)**2)**(-3) * (((m.x9 - m.x74)**2 + (m.x88
    - m.x153)**2 + (m.x167 - m.x232)**2)**(-3) - 2) + ((m.x9 - m.x75)**2 + (
    m.x88 - m.x154)**2 + (m.x167 - m.x233)**2)**(-3) * (((m.x9 - m.x75)**2 + (
    m.x88 - m.x154)**2 + (m.x167 - m.x233)**2)**(-3) - 2) + ((m.x9 - m.x76)**2
    + (m.x88 - m.x155)**2 + (m.x167 - m.x234)**2)**(-3) * (((m.x9 - m.x76)**2
    + (m.x88 - m.x155)**2 + (m.x167 - m.x234)**2)**(-3) - 2) + ((m.x9 - m.x77)
    **2 + (m.x88 - m.x156)**2 + (m.x167 - m.x235)**2)**(-3) * (((m.x9 - m.x77)
    **2 + (m.x88 - m.x156)**2 + (m.x167 - m.x235)**2)**(-3) - 2) + ((m.x9 -
    m.x78)**2 + (m.x88 - m.x157)**2 + (m.x167 - m.x236)**2)**(-3) * (((m.x9 -
    m.x78)**2 + (m.x88 - m.x157)**2 + (m.x167 - m.x236)**2)**(-3) - 2) + ((m.x9
    - m.x79)**2 + (m.x88 - m.x158)**2 + (m.x167 - m.x237)**2)**(-3) * (((m.x9
    - m.x79)**2 + (m.x88 - m.x158)**2 + (m.x167 - m.x237)**2)**(-3) - 2) + ((
    m.x10 - m.x11)**2 + (m.x89 - m.x90)**2 + (m.x168 - m.x169)**2)**(-3) * (((
    m.x10 - m.x11)**2 + (m.x89 - m.x90)**2 + (m.x168 - m.x169)**2)**(-3) - 2)
    + ((m.x10 - m.x12)**2 + (m.x89 - m.x91)**2 + (m.x168 - m.x170)**2)**(-3)
    * (((m.x10 - m.x12)**2 + (m.x89 - m.x91)**2 + (m.x168 - m.x170)**2)**(-3)
    - 2) + ((m.x10 - m.x13)**2 + (m.x89 - m.x92)**2 + (m.x168 - m.x171)**2)**(
    -3) * (((m.x10 - m.x13)**2 + (m.x89 - m.x92)**2 + (m.x168 - m.x171)**2)**(
    -3) - 2) + ((m.x10 - m.x14)**2 + (m.x89 - m.x93)**2 + (m.x168 - m.x172)**2)
    **(-3) * (((m.x10 - m.x14)**2 + (m.x89 - m.x93)**2 + (m.x168 - m.x172)**2)
    **(-3) - 2) + ((m.x10 - m.x15)**2 + (m.x89 - m.x94)**2 + (m.x168 - m.x173)
    **2)**(-3) * (((m.x10 - m.x15)**2 + (m.x89 - m.x94)**2 + (m.x168 - m.x173)
    **2)**(-3) - 2) + ((m.x10 - m.x16)**2 + (m.x89 - m.x95)**2 + (m.x168 -
    m.x174)**2)**(-3) * (((m.x10 - m.x16)**2 + (m.x89 - m.x95)**2 + (m.x168 -
    m.x174)**2)**(-3) - 2) + ((m.x10 - m.x17)**2 + (m.x89 - m.x96)**2 + (m.x168
    - m.x175)**2)**(-3) * (((m.x10 - m.x17)**2 + (m.x89 - m.x96)**2 + (m.x168
    - m.x175)**2)**(-3) - 2) + ((m.x10 - m.x18)**2 + (m.x89 - m.x97)**2 + (
    m.x168 - m.x176)**2)**(-3) * (((m.x10 - m.x18)**2 + (m.x89 - m.x97)**2 + (
    m.x168 - m.x176)**2)**(-3) - 2) + ((m.x10 - m.x19)**2 + (m.x89 - m.x98)**2
    + (m.x168 - m.x177)**2)**(-3) * (((m.x10 - m.x19)**2 + (m.x89 - m.x98)**2
    + (m.x168 - m.x177)**2)**(-3) - 2) + ((m.x10 - m.x20)**2 + (m.x89 - m.x99)
    **2 + (m.x168 - m.x178)**2)**(-3) * (((m.x10 - m.x20)**2 + (m.x89 - m.x99)
    **2 + (m.x168 - m.x178)**2)**(-3) - 2) + ((m.x10 - m.x21)**2 + (m.x89 -
    m.x100)**2 + (m.x168 - m.x179)**2)**(-3) * (((m.x10 - m.x21)**2 + (m.x89 -
    m.x100)**2 + (m.x168 - m.x179)**2)**(-3) - 2) + ((m.x10 - m.x22)**2 + (
    m.x89 - m.x101)**2 + (m.x168 - m.x180)**2)**(-3) * (((m.x10 - m.x22)**2 + (
    m.x89 - m.x101)**2 + (m.x168 - m.x180)**2)**(-3) - 2) + ((m.x10 - m.x23)**2
    + (m.x89 - m.x102)**2 + (m.x168 - m.x181)**2)**(-3) * (((m.x10 - m.x23)**2
    + (m.x89 - m.x102)**2 + (m.x168 - m.x181)**2)**(-3) - 2) + ((m.x10 - m.x24)
    **2 + (m.x89 - m.x103)**2 + (m.x168 - m.x182)**2)**(-3) * (((m.x10 - m.x24)
    **2 + (m.x89 - m.x103)**2 + (m.x168 - m.x182)**2)**(-3) - 2) + ((m.x10 -
    m.x25)**2 + (m.x89 - m.x104)**2 + (m.x168 - m.x183)**2)**(-3) * (((m.x10 -
    m.x25)**2 + (m.x89 - m.x104)**2 + (m.x168 - m.x183)**2)**(-3) - 2) + ((
    m.x10 - m.x26)**2 + (m.x89 - m.x105)**2 + (m.x168 - m.x184)**2)**(-3) * (((
    m.x10 - m.x26)**2 + (m.x89 - m.x105)**2 + (m.x168 - m.x184)**2)**(-3) - 2)
    + ((m.x10 - m.x27)**2 + (m.x89 - m.x106)**2 + (m.x168 - m.x185)**2)**(-3)
    * (((m.x10 - m.x27)**2 + (m.x89 - m.x106)**2 + (m.x168 - m.x185)**2)**(-3)
    - 2) + ((m.x10 - m.x28)**2 + (m.x89 - m.x107)**2 + (m.x168 - m.x186)**2)**
    (-3) * (((m.x10 - m.x28)**2 + (m.x89 - m.x107)**2 + (m.x168 - m.x186)**2)**
    (-3) - 2) + ((m.x10 - m.x29)**2 + (m.x89 - m.x108)**2 + (m.x168 - m.x187)**
    2)**(-3) * (((m.x10 - m.x29)**2 + (m.x89 - m.x108)**2 + (m.x168 - m.x187)**
    2)**(-3) - 2) + ((m.x10 - m.x30)**2 + (m.x89 - m.x109)**2 + (m.x168 -
    m.x188)**2)**(-3) * (((m.x10 - m.x30)**2 + (m.x89 - m.x109)**2 + (m.x168 -
    m.x188)**2)**(-3) - 2) + ((m.x10 - m.x31)**2 + (m.x89 - m.x110)**2 + (
    m.x168 - m.x189)**2)**(-3) * (((m.x10 - m.x31)**2 + (m.x89 - m.x110)**2 + (
    m.x168 - m.x189)**2)**(-3) - 2) + ((m.x10 - m.x32)**2 + (m.x89 - m.x111)**2
    + (m.x168 - m.x190)**2)**(-3) * (((m.x10 - m.x32)**2 + (m.x89 - m.x111)**2
    + (m.x168 - m.x190)**2)**(-3) - 2) + ((m.x10 - m.x33)**2 + (m.x89 - m.x112)
    **2 + (m.x168 - m.x191)**2)**(-3) * (((m.x10 - m.x33)**2 + (m.x89 - m.x112)
    **2 + (m.x168 - m.x191)**2)**(-3) - 2) + ((m.x10 - m.x34)**2 + (m.x89 -
    m.x113)**2 + (m.x168 - m.x192)**2)**(-3) * (((m.x10 - m.x34)**2 + (m.x89 -
    m.x113)**2 + (m.x168 - m.x192)**2)**(-3) - 2) + ((m.x10 - m.x35)**2 + (
    m.x89 - m.x114)**2 + (m.x168 - m.x193)**2)**(-3) * (((m.x10 - m.x35)**2 + (
    m.x89 - m.x114)**2 + (m.x168 - m.x193)**2)**(-3) - 2) + ((m.x10 - m.x36)**2
    + (m.x89 - m.x115)**2 + (m.x168 - m.x194)**2)**(-3) * (((m.x10 - m.x36)**2
    + (m.x89 - m.x115)**2 + (m.x168 - m.x194)**2)**(-3) - 2) + ((m.x10 - m.x37)
    **2 + (m.x89 - m.x116)**2 + (m.x168 - m.x195)**2)**(-3) * (((m.x10 - m.x37)
    **2 + (m.x89 - m.x116)**2 + (m.x168 - m.x195)**2)**(-3) - 2) + ((m.x10 -
    m.x38)**2 + (m.x89 - m.x117)**2 + (m.x168 - m.x196)**2)**(-3) * (((m.x10 -
    m.x38)**2 + (m.x89 - m.x117)**2 + (m.x168 - m.x196)**2)**(-3) - 2) + ((
    m.x10 - m.x39)**2 + (m.x89 - m.x118)**2 + (m.x168 - m.x197)**2)**(-3) * (((
    m.x10 - m.x39)**2 + (m.x89 - m.x118)**2 + (m.x168 - m.x197)**2)**(-3) - 2)
    + ((m.x10 - m.x40)**2 + (m.x89 - m.x119)**2 + (m.x168 - m.x198)**2)**(-3)
    * (((m.x10 - m.x40)**2 + (m.x89 - m.x119)**2 + (m.x168 - m.x198)**2)**(-3)
    - 2) + ((m.x10 - m.x41)**2 + (m.x89 - m.x120)**2 + (m.x168 - m.x199)**2)**
    (-3) * (((m.x10 - m.x41)**2 + (m.x89 - m.x120)**2 + (m.x168 - m.x199)**2)**
    (-3) - 2) + ((m.x10 - m.x42)**2 + (m.x89 - m.x121)**2 + (m.x168 - m.x200)**
    2)**(-3) * (((m.x10 - m.x42)**2 + (m.x89 - m.x121)**2 + (m.x168 - m.x200)**
    2)**(-3) - 2) + ((m.x10 - m.x43)**2 + (m.x89 - m.x122)**2 + (m.x168 -
    m.x201)**2)**(-3) * (((m.x10 - m.x43)**2 + (m.x89 - m.x122)**2 + (m.x168 -
    m.x201)**2)**(-3) - 2) + ((m.x10 - m.x44)**2 + (m.x89 - m.x123)**2 + (
    m.x168 - m.x202)**2)**(-3) * (((m.x10 - m.x44)**2 + (m.x89 - m.x123)**2 + (
    m.x168 - m.x202)**2)**(-3) - 2) + ((m.x10 - m.x45)**2 + (m.x89 - m.x124)**2
    + (m.x168 - m.x203)**2)**(-3) * (((m.x10 - m.x45)**2 + (m.x89 - m.x124)**2
    + (m.x168 - m.x203)**2)**(-3) - 2) + ((m.x10 - m.x46)**2 + (m.x89 - m.x125)
    **2 + (m.x168 - m.x204)**2)**(-3) * (((m.x10 - m.x46)**2 + (m.x89 - m.x125)
    **2 + (m.x168 - m.x204)**2)**(-3) - 2) + ((m.x10 - m.x47)**2 + (m.x89 -
    m.x126)**2 + (m.x168 - m.x205)**2)**(-3) * (((m.x10 - m.x47)**2 + (m.x89 -
    m.x126)**2 + (m.x168 - m.x205)**2)**(-3) - 2) + ((m.x10 - m.x48)**2 + (
    m.x89 - m.x127)**2 + (m.x168 - m.x206)**2)**(-3) * (((m.x10 - m.x48)**2 + (
    m.x89 - m.x127)**2 + (m.x168 - m.x206)**2)**(-3) - 2) + ((m.x10 - m.x49)**2
    + (m.x89 - m.x128)**2 + (m.x168 - m.x207)**2)**(-3) * (((m.x10 - m.x49)**2
    + (m.x89 - m.x128)**2 + (m.x168 - m.x207)**2)**(-3) - 2) + ((m.x10 - m.x50)
    **2 + (m.x89 - m.x129)**2 + (m.x168 - m.x208)**2)**(-3) * (((m.x10 - m.x50)
    **2 + (m.x89 - m.x129)**2 + (m.x168 - m.x208)**2)**(-3) - 2) + ((m.x10 -
    m.x51)**2 + (m.x89 - m.x130)**2 + (m.x168 - m.x209)**2)**(-3) * (((m.x10 -
    m.x51)**2 + (m.x89 - m.x130)**2 + (m.x168 - m.x209)**2)**(-3) - 2) + ((
    m.x10 - m.x52)**2 + (m.x89 - m.x131)**2 + (m.x168 - m.x210)**2)**(-3) * (((
    m.x10 - m.x52)**2 + (m.x89 - m.x131)**2 + (m.x168 - m.x210)**2)**(-3) - 2)
    + ((m.x10 - m.x53)**2 + (m.x89 - m.x132)**2 + (m.x168 - m.x211)**2)**(-3)
    * (((m.x10 - m.x53)**2 + (m.x89 - m.x132)**2 + (m.x168 - m.x211)**2)**(-3)
    - 2) + ((m.x10 - m.x54)**2 + (m.x89 - m.x133)**2 + (m.x168 - m.x212)**2)**
    (-3) * (((m.x10 - m.x54)**2 + (m.x89 - m.x133)**2 + (m.x168 - m.x212)**2)**
    (-3) - 2) + ((m.x10 - m.x55)**2 + (m.x89 - m.x134)**2 + (m.x168 - m.x213)**
    2)**(-3) * (((m.x10 - m.x55)**2 + (m.x89 - m.x134)**2 + (m.x168 - m.x213)**
    2)**(-3) - 2) + ((m.x10 - m.x56)**2 + (m.x89 - m.x135)**2 + (m.x168 -
    m.x214)**2)**(-3) * (((m.x10 - m.x56)**2 + (m.x89 - m.x135)**2 + (m.x168 -
    m.x214)**2)**(-3) - 2) + ((m.x10 - m.x57)**2 + (m.x89 - m.x136)**2 + (
    m.x168 - m.x215)**2)**(-3) * (((m.x10 - m.x57)**2 + (m.x89 - m.x136)**2 + (
    m.x168 - m.x215)**2)**(-3) - 2) + ((m.x10 - m.x58)**2 + (m.x89 - m.x137)**2
    + (m.x168 - m.x216)**2)**(-3) * (((m.x10 - m.x58)**2 + (m.x89 - m.x137)**2
    + (m.x168 - m.x216)**2)**(-3) - 2) + ((m.x10 - m.x59)**2 + (m.x89 - m.x138)
    **2 + (m.x168 - m.x217)**2)**(-3) * (((m.x10 - m.x59)**2 + (m.x89 - m.x138)
    **2 + (m.x168 - m.x217)**2)**(-3) - 2) + ((m.x10 - m.x60)**2 + (m.x89 -
    m.x139)**2 + (m.x168 - m.x218)**2)**(-3) * (((m.x10 - m.x60)**2 + (m.x89 -
    m.x139)**2 + (m.x168 - m.x218)**2)**(-3) - 2) + ((m.x10 - m.x61)**2 + (
    m.x89 - m.x140)**2 + (m.x168 - m.x219)**2)**(-3) * (((m.x10 - m.x61)**2 + (
    m.x89 - m.x140)**2 + (m.x168 - m.x219)**2)**(-3) - 2) + ((m.x10 - m.x62)**2
    + (m.x89 - m.x141)**2 + (m.x168 - m.x220)**2)**(-3) * (((m.x10 - m.x62)**2
    + (m.x89 - m.x141)**2 + (m.x168 - m.x220)**2)**(-3) - 2) + ((m.x10 - m.x63)
    **2 + (m.x89 - m.x142)**2 + (m.x168 - m.x221)**2)**(-3) * (((m.x10 - m.x63)
    **2 + (m.x89 - m.x142)**2 + (m.x168 - m.x221)**2)**(-3) - 2) + ((m.x10 -
    m.x64)**2 + (m.x89 - m.x143)**2 + (m.x168 - m.x222)**2)**(-3) * (((m.x10 -
    m.x64)**2 + (m.x89 - m.x143)**2 + (m.x168 - m.x222)**2)**(-3) - 2) + ((
    m.x10 - m.x65)**2 + (m.x89 - m.x144)**2 + (m.x168 - m.x223)**2)**(-3) * (((
    m.x10 - m.x65)**2 + (m.x89 - m.x144)**2 + (m.x168 - m.x223)**2)**(-3) - 2)
    + ((m.x10 - m.x66)**2 + (m.x89 - m.x145)**2 + (m.x168 - m.x224)**2)**(-3)
    * (((m.x10 - m.x66)**2 + (m.x89 - m.x145)**2 + (m.x168 - m.x224)**2)**(-3)
    - 2) + ((m.x10 - m.x67)**2 + (m.x89 - m.x146)**2 + (m.x168 - m.x225)**2)**
    (-3) * (((m.x10 - m.x67)**2 + (m.x89 - m.x146)**2 + (m.x168 - m.x225)**2)**
    (-3) - 2) + ((m.x10 - m.x68)**2 + (m.x89 - m.x147)**2 + (m.x168 - m.x226)**
    2)**(-3) * (((m.x10 - m.x68)**2 + (m.x89 - m.x147)**2 + (m.x168 - m.x226)**
    2)**(-3) - 2) + ((m.x10 - m.x69)**2 + (m.x89 - m.x148)**2 + (m.x168 -
    m.x227)**2)**(-3) * (((m.x10 - m.x69)**2 + (m.x89 - m.x148)**2 + (m.x168 -
    m.x227)**2)**(-3) - 2) + ((m.x10 - m.x70)**2 + (m.x89 - m.x149)**2 + (
    m.x168 - m.x228)**2)**(-3) * (((m.x10 - m.x70)**2 + (m.x89 - m.x149)**2 + (
    m.x168 - m.x228)**2)**(-3) - 2) + ((m.x10 - m.x71)**2 + (m.x89 - m.x150)**2
    + (m.x168 - m.x229)**2)**(-3) * (((m.x10 - m.x71)**2 + (m.x89 - m.x150)**2
    + (m.x168 - m.x229)**2)**(-3) - 2) + ((m.x10 - m.x72)**2 + (m.x89 - m.x151)
    **2 + (m.x168 - m.x230)**2)**(-3) * (((m.x10 - m.x72)**2 + (m.x89 - m.x151)
    **2 + (m.x168 - m.x230)**2)**(-3) - 2) + ((m.x10 - m.x73)**2 + (m.x89 -
    m.x152)**2 + (m.x168 - m.x231)**2)**(-3) * (((m.x10 - m.x73)**2 + (m.x89 -
    m.x152)**2 + (m.x168 - m.x231)**2)**(-3) - 2) + ((m.x10 - m.x74)**2 + (
    m.x89 - m.x153)**2 + (m.x168 - m.x232)**2)**(-3) * (((m.x10 - m.x74)**2 + (
    m.x89 - m.x153)**2 + (m.x168 - m.x232)**2)**(-3) - 2) + ((m.x10 - m.x75)**2
    + (m.x89 - m.x154)**2 + (m.x168 - m.x233)**2)**(-3) * (((m.x10 - m.x75)**2
    + (m.x89 - m.x154)**2 + (m.x168 - m.x233)**2)**(-3) - 2) + ((m.x10 - m.x76)
    **2 + (m.x89 - m.x155)**2 + (m.x168 - m.x234)**2)**(-3) * (((m.x10 - m.x76)
    **2 + (m.x89 - m.x155)**2 + (m.x168 - m.x234)**2)**(-3) - 2) + ((m.x10 -
    m.x77)**2 + (m.x89 - m.x156)**2 + (m.x168 - m.x235)**2)**(-3) * (((m.x10 -
    m.x77)**2 + (m.x89 - m.x156)**2 + (m.x168 - m.x235)**2)**(-3) - 2) + ((
    m.x10 - m.x78)**2 + (m.x89 - m.x157)**2 + (m.x168 - m.x236)**2)**(-3) * (((
    m.x10 - m.x78)**2 + (m.x89 - m.x157)**2 + (m.x168 - m.x236)**2)**(-3) - 2)
    + ((m.x10 - m.x79)**2 + (m.x89 - m.x158)**2 + (m.x168 - m.x237)**2)**(-3)
    * (((m.x10 - m.x79)**2 + (m.x89 - m.x158)**2 + (m.x168 - m.x237)**2)**(-3)
    - 2) + ((m.x11 - m.x12)**2 + (m.x90 - m.x91)**2 + (m.x169 - m.x170)**2)**(
    -3) * (((m.x11 - m.x12)**2 + (m.x90 - m.x91)**2 + (m.x169 - m.x170)**2)**(
    -3) - 2) + ((m.x11 - m.x13)**2 + (m.x90 - m.x92)**2 + (m.x169 - m.x171)**2)
    **(-3) * (((m.x11 - m.x13)**2 + (m.x90 - m.x92)**2 + (m.x169 - m.x171)**2)
    **(-3) - 2) + ((m.x11 - m.x14)**2 + (m.x90 - m.x93)**2 + (m.x169 - m.x172)
    **2)**(-3) * (((m.x11 - m.x14)**2 + (m.x90 - m.x93)**2 + (m.x169 - m.x172)
    **2)**(-3) - 2) + ((m.x11 - m.x15)**2 + (m.x90 - m.x94)**2 + (m.x169 -
    m.x173)**2)**(-3) * (((m.x11 - m.x15)**2 + (m.x90 - m.x94)**2 + (m.x169 -
    m.x173)**2)**(-3) - 2) + ((m.x11 - m.x16)**2 + (m.x90 - m.x95)**2 + (m.x169
    - m.x174)**2)**(-3) * (((m.x11 - m.x16)**2 + (m.x90 - m.x95)**2 + (m.x169
    - m.x174)**2)**(-3) - 2) + ((m.x11 - m.x17)**2 + (m.x90 - m.x96)**2 + (
    m.x169 - m.x175)**2)**(-3) * (((m.x11 - m.x17)**2 + (m.x90 - m.x96)**2 + (
    m.x169 - m.x175)**2)**(-3) - 2) + ((m.x11 - m.x18)**2 + (m.x90 - m.x97)**2
    + (m.x169 - m.x176)**2)**(-3) * (((m.x11 - m.x18)**2 + (m.x90 - m.x97)**2
    + (m.x169 - m.x176)**2)**(-3) - 2) + ((m.x11 - m.x19)**2 + (m.x90 - m.x98)
    **2 + (m.x169 - m.x177)**2)**(-3) * (((m.x11 - m.x19)**2 + (m.x90 - m.x98)
    **2 + (m.x169 - m.x177)**2)**(-3) - 2) + ((m.x11 - m.x20)**2 + (m.x90 -
    m.x99)**2 + (m.x169 - m.x178)**2)**(-3) * (((m.x11 - m.x20)**2 + (m.x90 -
    m.x99)**2 + (m.x169 - m.x178)**2)**(-3) - 2) + ((m.x11 - m.x21)**2 + (m.x90
    - m.x100)**2 + (m.x169 - m.x179)**2)**(-3) * (((m.x11 - m.x21)**2 + (m.x90
    - m.x100)**2 + (m.x169 - m.x179)**2)**(-3) - 2) + ((m.x11 - m.x22)**2 + (
    m.x90 - m.x101)**2 + (m.x169 - m.x180)**2)**(-3) * (((m.x11 - m.x22)**2 + (
    m.x90 - m.x101)**2 + (m.x169 - m.x180)**2)**(-3) - 2) + ((m.x11 - m.x23)**2
    + (m.x90 - m.x102)**2 + (m.x169 - m.x181)**2)**(-3) * (((m.x11 - m.x23)**2
    + (m.x90 - m.x102)**2 + (m.x169 - m.x181)**2)**(-3) - 2) + ((m.x11 - m.x24)
    **2 + (m.x90 - m.x103)**2 + (m.x169 - m.x182)**2)**(-3) * (((m.x11 - m.x24)
    **2 + (m.x90 - m.x103)**2 + (m.x169 - m.x182)**2)**(-3) - 2) + ((m.x11 -
    m.x25)**2 + (m.x90 - m.x104)**2 + (m.x169 - m.x183)**2)**(-3) * (((m.x11 -
    m.x25)**2 + (m.x90 - m.x104)**2 + (m.x169 - m.x183)**2)**(-3) - 2) + ((
    m.x11 - m.x26)**2 + (m.x90 - m.x105)**2 + (m.x169 - m.x184)**2)**(-3) * (((
    m.x11 - m.x26)**2 + (m.x90 - m.x105)**2 + (m.x169 - m.x184)**2)**(-3) - 2)
    + ((m.x11 - m.x27)**2 + (m.x90 - m.x106)**2 + (m.x169 - m.x185)**2)**(-3)
    * (((m.x11 - m.x27)**2 + (m.x90 - m.x106)**2 + (m.x169 - m.x185)**2)**(-3)
    - 2) + ((m.x11 - m.x28)**2 + (m.x90 - m.x107)**2 + (m.x169 - m.x186)**2)**
    (-3) * (((m.x11 - m.x28)**2 + (m.x90 - m.x107)**2 + (m.x169 - m.x186)**2)**
    (-3) - 2) + ((m.x11 - m.x29)**2 + (m.x90 - m.x108)**2 + (m.x169 - m.x187)**
    2)**(-3) * (((m.x11 - m.x29)**2 + (m.x90 - m.x108)**2 + (m.x169 - m.x187)**
    2)**(-3) - 2) + ((m.x11 - m.x30)**2 + (m.x90 - m.x109)**2 + (m.x169 -
    m.x188)**2)**(-3) * (((m.x11 - m.x30)**2 + (m.x90 - m.x109)**2 + (m.x169 -
    m.x188)**2)**(-3) - 2) + ((m.x11 - m.x31)**2 + (m.x90 - m.x110)**2 + (
    m.x169 - m.x189)**2)**(-3) * (((m.x11 - m.x31)**2 + (m.x90 - m.x110)**2 + (
    m.x169 - m.x189)**2)**(-3) - 2) + ((m.x11 - m.x32)**2 + (m.x90 - m.x111)**2
    + (m.x169 - m.x190)**2)**(-3) * (((m.x11 - m.x32)**2 + (m.x90 - m.x111)**2
    + (m.x169 - m.x190)**2)**(-3) - 2) + ((m.x11 - m.x33)**2 + (m.x90 - m.x112)
    **2 + (m.x169 - m.x191)**2)**(-3) * (((m.x11 - m.x33)**2 + (m.x90 - m.x112)
    **2 + (m.x169 - m.x191)**2)**(-3) - 2) + ((m.x11 - m.x34)**2 + (m.x90 -
    m.x113)**2 + (m.x169 - m.x192)**2)**(-3) * (((m.x11 - m.x34)**2 + (m.x90 -
    m.x113)**2 + (m.x169 - m.x192)**2)**(-3) - 2) + ((m.x11 - m.x35)**2 + (
    m.x90 - m.x114)**2 + (m.x169 - m.x193)**2)**(-3) * (((m.x11 - m.x35)**2 + (
    m.x90 - m.x114)**2 + (m.x169 - m.x193)**2)**(-3) - 2) + ((m.x11 - m.x36)**2
    + (m.x90 - m.x115)**2 + (m.x169 - m.x194)**2)**(-3) * (((m.x11 - m.x36)**2
    + (m.x90 - m.x115)**2 + (m.x169 - m.x194)**2)**(-3) - 2) + ((m.x11 - m.x37)
    **2 + (m.x90 - m.x116)**2 + (m.x169 - m.x195)**2)**(-3) * (((m.x11 - m.x37)
    **2 + (m.x90 - m.x116)**2 + (m.x169 - m.x195)**2)**(-3) - 2) + ((m.x11 -
    m.x38)**2 + (m.x90 - m.x117)**2 + (m.x169 - m.x196)**2)**(-3) * (((m.x11 -
    m.x38)**2 + (m.x90 - m.x117)**2 + (m.x169 - m.x196)**2)**(-3) - 2) + ((
    m.x11 - m.x39)**2 + (m.x90 - m.x118)**2 + (m.x169 - m.x197)**2)**(-3) * (((
    m.x11 - m.x39)**2 + (m.x90 - m.x118)**2 + (m.x169 - m.x197)**2)**(-3) - 2)
    + ((m.x11 - m.x40)**2 + (m.x90 - m.x119)**2 + (m.x169 - m.x198)**2)**(-3)
    * (((m.x11 - m.x40)**2 + (m.x90 - m.x119)**2 + (m.x169 - m.x198)**2)**(-3)
    - 2) + ((m.x11 - m.x41)**2 + (m.x90 - m.x120)**2 + (m.x169 - m.x199)**2)**
    (-3) * (((m.x11 - m.x41)**2 + (m.x90 - m.x120)**2 + (m.x169 - m.x199)**2)**
    (-3) - 2) + ((m.x11 - m.x42)**2 + (m.x90 - m.x121)**2 + (m.x169 - m.x200)**
    2)**(-3) * (((m.x11 - m.x42)**2 + (m.x90 - m.x121)**2 + (m.x169 - m.x200)**
    2)**(-3) - 2) + ((m.x11 - m.x43)**2 + (m.x90 - m.x122)**2 + (m.x169 -
    m.x201)**2)**(-3) * (((m.x11 - m.x43)**2 + (m.x90 - m.x122)**2 + (m.x169 -
    m.x201)**2)**(-3) - 2) + ((m.x11 - m.x44)**2 + (m.x90 - m.x123)**2 + (
    m.x169 - m.x202)**2)**(-3) * (((m.x11 - m.x44)**2 + (m.x90 - m.x123)**2 + (
    m.x169 - m.x202)**2)**(-3) - 2) + ((m.x11 - m.x45)**2 + (m.x90 - m.x124)**2
    + (m.x169 - m.x203)**2)**(-3) * (((m.x11 - m.x45)**2 + (m.x90 - m.x124)**2
    + (m.x169 - m.x203)**2)**(-3) - 2) + ((m.x11 - m.x46)**2 + (m.x90 - m.x125)
    **2 + (m.x169 - m.x204)**2)**(-3) * (((m.x11 - m.x46)**2 + (m.x90 - m.x125)
    **2 + (m.x169 - m.x204)**2)**(-3) - 2) + ((m.x11 - m.x47)**2 + (m.x90 -
    m.x126)**2 + (m.x169 - m.x205)**2)**(-3) * (((m.x11 - m.x47)**2 + (m.x90 -
    m.x126)**2 + (m.x169 - m.x205)**2)**(-3) - 2) + ((m.x11 - m.x48)**2 + (
    m.x90 - m.x127)**2 + (m.x169 - m.x206)**2)**(-3) * (((m.x11 - m.x48)**2 + (
    m.x90 - m.x127)**2 + (m.x169 - m.x206)**2)**(-3) - 2) + ((m.x11 - m.x49)**2
    + (m.x90 - m.x128)**2 + (m.x169 - m.x207)**2)**(-3) * (((m.x11 - m.x49)**2
    + (m.x90 - m.x128)**2 + (m.x169 - m.x207)**2)**(-3) - 2) + ((m.x11 - m.x50)
    **2 + (m.x90 - m.x129)**2 + (m.x169 - m.x208)**2)**(-3) * (((m.x11 - m.x50)
    **2 + (m.x90 - m.x129)**2 + (m.x169 - m.x208)**2)**(-3) - 2) + ((m.x11 -
    m.x51)**2 + (m.x90 - m.x130)**2 + (m.x169 - m.x209)**2)**(-3) * (((m.x11 -
    m.x51)**2 + (m.x90 - m.x130)**2 + (m.x169 - m.x209)**2)**(-3) - 2) + ((
    m.x11 - m.x52)**2 + (m.x90 - m.x131)**2 + (m.x169 - m.x210)**2)**(-3) * (((
    m.x11 - m.x52)**2 + (m.x90 - m.x131)**2 + (m.x169 - m.x210)**2)**(-3) - 2)
    + ((m.x11 - m.x53)**2 + (m.x90 - m.x132)**2 + (m.x169 - m.x211)**2)**(-3)
    * (((m.x11 - m.x53)**2 + (m.x90 - m.x132)**2 + (m.x169 - m.x211)**2)**(-3)
    - 2) + ((m.x11 - m.x54)**2 + (m.x90 - m.x133)**2 + (m.x169 - m.x212)**2)**
    (-3) * (((m.x11 - m.x54)**2 + (m.x90 - m.x133)**2 + (m.x169 - m.x212)**2)**
    (-3) - 2) + ((m.x11 - m.x55)**2 + (m.x90 - m.x134)**2 + (m.x169 - m.x213)**
    2)**(-3) * (((m.x11 - m.x55)**2 + (m.x90 - m.x134)**2 + (m.x169 - m.x213)**
    2)**(-3) - 2) + ((m.x11 - m.x56)**2 + (m.x90 - m.x135)**2 + (m.x169 -
    m.x214)**2)**(-3) * (((m.x11 - m.x56)**2 + (m.x90 - m.x135)**2 + (m.x169 -
    m.x214)**2)**(-3) - 2) + ((m.x11 - m.x57)**2 + (m.x90 - m.x136)**2 + (
    m.x169 - m.x215)**2)**(-3) * (((m.x11 - m.x57)**2 + (m.x90 - m.x136)**2 + (
    m.x169 - m.x215)**2)**(-3) - 2) + ((m.x11 - m.x58)**2 + (m.x90 - m.x137)**2
    + (m.x169 - m.x216)**2)**(-3) * (((m.x11 - m.x58)**2 + (m.x90 - m.x137)**2
    + (m.x169 - m.x216)**2)**(-3) - 2) + ((m.x11 - m.x59)**2 + (m.x90 - m.x138)
    **2 + (m.x169 - m.x217)**2)**(-3) * (((m.x11 - m.x59)**2 + (m.x90 - m.x138)
    **2 + (m.x169 - m.x217)**2)**(-3) - 2) + ((m.x11 - m.x60)**2 + (m.x90 -
    m.x139)**2 + (m.x169 - m.x218)**2)**(-3) * (((m.x11 - m.x60)**2 + (m.x90 -
    m.x139)**2 + (m.x169 - m.x218)**2)**(-3) - 2) + ((m.x11 - m.x61)**2 + (
    m.x90 - m.x140)**2 + (m.x169 - m.x219)**2)**(-3) * (((m.x11 - m.x61)**2 + (
    m.x90 - m.x140)**2 + (m.x169 - m.x219)**2)**(-3) - 2) + ((m.x11 - m.x62)**2
    + (m.x90 - m.x141)**2 + (m.x169 - m.x220)**2)**(-3) * (((m.x11 - m.x62)**2
    + (m.x90 - m.x141)**2 + (m.x169 - m.x220)**2)**(-3) - 2) + ((m.x11 - m.x63)
    **2 + (m.x90 - m.x142)**2 + (m.x169 - m.x221)**2)**(-3) * (((m.x11 - m.x63)
    **2 + (m.x90 - m.x142)**2 + (m.x169 - m.x221)**2)**(-3) - 2) + ((m.x11 -
    m.x64)**2 + (m.x90 - m.x143)**2 + (m.x169 - m.x222)**2)**(-3) * (((m.x11 -
    m.x64)**2 + (m.x90 - m.x143)**2 + (m.x169 - m.x222)**2)**(-3) - 2) + ((
    m.x11 - m.x65)**2 + (m.x90 - m.x144)**2 + (m.x169 - m.x223)**2)**(-3) * (((
    m.x11 - m.x65)**2 + (m.x90 - m.x144)**2 + (m.x169 - m.x223)**2)**(-3) - 2)
    + ((m.x11 - m.x66)**2 + (m.x90 - m.x145)**2 + (m.x169 - m.x224)**2)**(-3)
    * (((m.x11 - m.x66)**2 + (m.x90 - m.x145)**2 + (m.x169 - m.x224)**2)**(-3)
    - 2) + ((m.x11 - m.x67)**2 + (m.x90 - m.x146)**2 + (m.x169 - m.x225)**2)**
    (-3) * (((m.x11 - m.x67)**2 + (m.x90 - m.x146)**2 + (m.x169 - m.x225)**2)**
    (-3) - 2) + ((m.x11 - m.x68)**2 + (m.x90 - m.x147)**2 + (m.x169 - m.x226)**
    2)**(-3) * (((m.x11 - m.x68)**2 + (m.x90 - m.x147)**2 + (m.x169 - m.x226)**
    2)**(-3) - 2) + ((m.x11 - m.x69)**2 + (m.x90 - m.x148)**2 + (m.x169 -
    m.x227)**2)**(-3) * (((m.x11 - m.x69)**2 + (m.x90 - m.x148)**2 + (m.x169 -
    m.x227)**2)**(-3) - 2) + ((m.x11 - m.x70)**2 + (m.x90 - m.x149)**2 + (
    m.x169 - m.x228)**2)**(-3) * (((m.x11 - m.x70)**2 + (m.x90 - m.x149)**2 + (
    m.x169 - m.x228)**2)**(-3) - 2) + ((m.x11 - m.x71)**2 + (m.x90 - m.x150)**2
    + (m.x169 - m.x229)**2)**(-3) * (((m.x11 - m.x71)**2 + (m.x90 - m.x150)**2
    + (m.x169 - m.x229)**2)**(-3) - 2) + ((m.x11 - m.x72)**2 + (m.x90 - m.x151)
    **2 + (m.x169 - m.x230)**2)**(-3) * (((m.x11 - m.x72)**2 + (m.x90 - m.x151)
    **2 + (m.x169 - m.x230)**2)**(-3) - 2) + ((m.x11 - m.x73)**2 + (m.x90 -
    m.x152)**2 + (m.x169 - m.x231)**2)**(-3) * (((m.x11 - m.x73)**2 + (m.x90 -
    m.x152)**2 + (m.x169 - m.x231)**2)**(-3) - 2) + ((m.x11 - m.x74)**2 + (
    m.x90 - m.x153)**2 + (m.x169 - m.x232)**2)**(-3) * (((m.x11 - m.x74)**2 + (
    m.x90 - m.x153)**2 + (m.x169 - m.x232)**2)**(-3) - 2) + ((m.x11 - m.x75)**2
    + (m.x90 - m.x154)**2 + (m.x169 - m.x233)**2)**(-3) * (((m.x11 - m.x75)**2
    + (m.x90 - m.x154)**2 + (m.x169 - m.x233)**2)**(-3) - 2) + ((m.x11 - m.x76)
    **2 + (m.x90 - m.x155)**2 + (m.x169 - m.x234)**2)**(-3) * (((m.x11 - m.x76)
    **2 + (m.x90 - m.x155)**2 + (m.x169 - m.x234)**2)**(-3) - 2) + ((m.x11 -
    m.x77)**2 + (m.x90 - m.x156)**2 + (m.x169 - m.x235)**2)**(-3) * (((m.x11 -
    m.x77)**2 + (m.x90 - m.x156)**2 + (m.x169 - m.x235)**2)**(-3) - 2) + ((
    m.x11 - m.x78)**2 + (m.x90 - m.x157)**2 + (m.x169 - m.x236)**2)**(-3) * (((
    m.x11 - m.x78)**2 + (m.x90 - m.x157)**2 + (m.x169 - m.x236)**2)**(-3) - 2)
    + ((m.x11 - m.x79)**2 + (m.x90 - m.x158)**2 + (m.x169 - m.x237)**2)**(-3)
    * (((m.x11 - m.x79)**2 + (m.x90 - m.x158)**2 + (m.x169 - m.x237)**2)**(-3)
    - 2) + ((m.x12 - m.x13)**2 + (m.x91 - m.x92)**2 + (m.x170 - m.x171)**2)**(
    -3) * (((m.x12 - m.x13)**2 + (m.x91 - m.x92)**2 + (m.x170 - m.x171)**2)**(
    -3) - 2) + ((m.x12 - m.x14)**2 + (m.x91 - m.x93)**2 + (m.x170 - m.x172)**2)
    **(-3) * (((m.x12 - m.x14)**2 + (m.x91 - m.x93)**2 + (m.x170 - m.x172)**2)
    **(-3) - 2) + ((m.x12 - m.x15)**2 + (m.x91 - m.x94)**2 + (m.x170 - m.x173)
    **2)**(-3) * (((m.x12 - m.x15)**2 + (m.x91 - m.x94)**2 + (m.x170 - m.x173)
    **2)**(-3) - 2) + ((m.x12 - m.x16)**2 + (m.x91 - m.x95)**2 + (m.x170 -
    m.x174)**2)**(-3) * (((m.x12 - m.x16)**2 + (m.x91 - m.x95)**2 + (m.x170 -
    m.x174)**2)**(-3) - 2) + ((m.x12 - m.x17)**2 + (m.x91 - m.x96)**2 + (m.x170
    - m.x175)**2)**(-3) * (((m.x12 - m.x17)**2 + (m.x91 - m.x96)**2 + (m.x170
    - m.x175)**2)**(-3) - 2) + ((m.x12 - m.x18)**2 + (m.x91 - m.x97)**2 + (
    m.x170 - m.x176)**2)**(-3) * (((m.x12 - m.x18)**2 + (m.x91 - m.x97)**2 + (
    m.x170 - m.x176)**2)**(-3) - 2) + ((m.x12 - m.x19)**2 + (m.x91 - m.x98)**2
    + (m.x170 - m.x177)**2)**(-3) * (((m.x12 - m.x19)**2 + (m.x91 - m.x98)**2
    + (m.x170 - m.x177)**2)**(-3) - 2) + ((m.x12 - m.x20)**2 + (m.x91 - m.x99)
    **2 + (m.x170 - m.x178)**2)**(-3) * (((m.x12 - m.x20)**2 + (m.x91 - m.x99)
    **2 + (m.x170 - m.x178)**2)**(-3) - 2) + ((m.x12 - m.x21)**2 + (m.x91 -
    m.x100)**2 + (m.x170 - m.x179)**2)**(-3) * (((m.x12 - m.x21)**2 + (m.x91 -
    m.x100)**2 + (m.x170 - m.x179)**2)**(-3) - 2) + ((m.x12 - m.x22)**2 + (
    m.x91 - m.x101)**2 + (m.x170 - m.x180)**2)**(-3) * (((m.x12 - m.x22)**2 + (
    m.x91 - m.x101)**2 + (m.x170 - m.x180)**2)**(-3) - 2) + ((m.x12 - m.x23)**2
    + (m.x91 - m.x102)**2 + (m.x170 - m.x181)**2)**(-3) * (((m.x12 - m.x23)**2
    + (m.x91 - m.x102)**2 + (m.x170 - m.x181)**2)**(-3) - 2) + ((m.x12 - m.x24)
    **2 + (m.x91 - m.x103)**2 + (m.x170 - m.x182)**2)**(-3) * (((m.x12 - m.x24)
    **2 + (m.x91 - m.x103)**2 + (m.x170 - m.x182)**2)**(-3) - 2) + ((m.x12 -
    m.x25)**2 + (m.x91 - m.x104)**2 + (m.x170 - m.x183)**2)**(-3) * (((m.x12 -
    m.x25)**2 + (m.x91 - m.x104)**2 + (m.x170 - m.x183)**2)**(-3) - 2) + ((
    m.x12 - m.x26)**2 + (m.x91 - m.x105)**2 + (m.x170 - m.x184)**2)**(-3) * (((
    m.x12 - m.x26)**2 + (m.x91 - m.x105)**2 + (m.x170 - m.x184)**2)**(-3) - 2)
    + ((m.x12 - m.x27)**2 + (m.x91 - m.x106)**2 + (m.x170 - m.x185)**2)**(-3)
    * (((m.x12 - m.x27)**2 + (m.x91 - m.x106)**2 + (m.x170 - m.x185)**2)**(-3)
    - 2) + ((m.x12 - m.x28)**2 + (m.x91 - m.x107)**2 + (m.x170 - m.x186)**2)**
    (-3) * (((m.x12 - m.x28)**2 + (m.x91 - m.x107)**2 + (m.x170 - m.x186)**2)**
    (-3) - 2) + ((m.x12 - m.x29)**2 + (m.x91 - m.x108)**2 + (m.x170 - m.x187)**
    2)**(-3) * (((m.x12 - m.x29)**2 + (m.x91 - m.x108)**2 + (m.x170 - m.x187)**
    2)**(-3) - 2) + ((m.x12 - m.x30)**2 + (m.x91 - m.x109)**2 + (m.x170 -
    m.x188)**2)**(-3) * (((m.x12 - m.x30)**2 + (m.x91 - m.x109)**2 + (m.x170 -
    m.x188)**2)**(-3) - 2) + ((m.x12 - m.x31)**2 + (m.x91 - m.x110)**2 + (
    m.x170 - m.x189)**2)**(-3) * (((m.x12 - m.x31)**2 + (m.x91 - m.x110)**2 + (
    m.x170 - m.x189)**2)**(-3) - 2) + ((m.x12 - m.x32)**2 + (m.x91 - m.x111)**2
    + (m.x170 - m.x190)**2)**(-3) * (((m.x12 - m.x32)**2 + (m.x91 - m.x111)**2
    + (m.x170 - m.x190)**2)**(-3) - 2) + ((m.x12 - m.x33)**2 + (m.x91 - m.x112)
    **2 + (m.x170 - m.x191)**2)**(-3) * (((m.x12 - m.x33)**2 + (m.x91 - m.x112)
    **2 + (m.x170 - m.x191)**2)**(-3) - 2) + ((m.x12 - m.x34)**2 + (m.x91 -
    m.x113)**2 + (m.x170 - m.x192)**2)**(-3) * (((m.x12 - m.x34)**2 + (m.x91 -
    m.x113)**2 + (m.x170 - m.x192)**2)**(-3) - 2) + ((m.x12 - m.x35)**2 + (
    m.x91 - m.x114)**2 + (m.x170 - m.x193)**2)**(-3) * (((m.x12 - m.x35)**2 + (
    m.x91 - m.x114)**2 + (m.x170 - m.x193)**2)**(-3) - 2) + ((m.x12 - m.x36)**2
    + (m.x91 - m.x115)**2 + (m.x170 - m.x194)**2)**(-3) * (((m.x12 - m.x36)**2
    + (m.x91 - m.x115)**2 + (m.x170 - m.x194)**2)**(-3) - 2) + ((m.x12 - m.x37)
    **2 + (m.x91 - m.x116)**2 + (m.x170 - m.x195)**2)**(-3) * (((m.x12 - m.x37)
    **2 + (m.x91 - m.x116)**2 + (m.x170 - m.x195)**2)**(-3) - 2) + ((m.x12 -
    m.x38)**2 + (m.x91 - m.x117)**2 + (m.x170 - m.x196)**2)**(-3) * (((m.x12 -
    m.x38)**2 + (m.x91 - m.x117)**2 + (m.x170 - m.x196)**2)**(-3) - 2) + ((
    m.x12 - m.x39)**2 + (m.x91 - m.x118)**2 + (m.x170 - m.x197)**2)**(-3) * (((
    m.x12 - m.x39)**2 + (m.x91 - m.x118)**2 + (m.x170 - m.x197)**2)**(-3) - 2)
    + ((m.x12 - m.x40)**2 + (m.x91 - m.x119)**2 + (m.x170 - m.x198)**2)**(-3)
    * (((m.x12 - m.x40)**2 + (m.x91 - m.x119)**2 + (m.x170 - m.x198)**2)**(-3)
    - 2) + ((m.x12 - m.x41)**2 + (m.x91 - m.x120)**2 + (m.x170 - m.x199)**2)**
    (-3) * (((m.x12 - m.x41)**2 + (m.x91 - m.x120)**2 + (m.x170 - m.x199)**2)**
    (-3) - 2) + ((m.x12 - m.x42)**2 + (m.x91 - m.x121)**2 + (m.x170 - m.x200)**
    2)**(-3) * (((m.x12 - m.x42)**2 + (m.x91 - m.x121)**2 + (m.x170 - m.x200)**
    2)**(-3) - 2) + ((m.x12 - m.x43)**2 + (m.x91 - m.x122)**2 + (m.x170 -
    m.x201)**2)**(-3) * (((m.x12 - m.x43)**2 + (m.x91 - m.x122)**2 + (m.x170 -
    m.x201)**2)**(-3) - 2) + ((m.x12 - m.x44)**2 + (m.x91 - m.x123)**2 + (
    m.x170 - m.x202)**2)**(-3) * (((m.x12 - m.x44)**2 + (m.x91 - m.x123)**2 + (
    m.x170 - m.x202)**2)**(-3) - 2) + ((m.x12 - m.x45)**2 + (m.x91 - m.x124)**2
    + (m.x170 - m.x203)**2)**(-3) * (((m.x12 - m.x45)**2 + (m.x91 - m.x124)**2
    + (m.x170 - m.x203)**2)**(-3) - 2) + ((m.x12 - m.x46)**2 + (m.x91 - m.x125)
    **2 + (m.x170 - m.x204)**2)**(-3) * (((m.x12 - m.x46)**2 + (m.x91 - m.x125)
    **2 + (m.x170 - m.x204)**2)**(-3) - 2) + ((m.x12 - m.x47)**2 + (m.x91 -
    m.x126)**2 + (m.x170 - m.x205)**2)**(-3) * (((m.x12 - m.x47)**2 + (m.x91 -
    m.x126)**2 + (m.x170 - m.x205)**2)**(-3) - 2) + ((m.x12 - m.x48)**2 + (
    m.x91 - m.x127)**2 + (m.x170 - m.x206)**2)**(-3) * (((m.x12 - m.x48)**2 + (
    m.x91 - m.x127)**2 + (m.x170 - m.x206)**2)**(-3) - 2) + ((m.x12 - m.x49)**2
    + (m.x91 - m.x128)**2 + (m.x170 - m.x207)**2)**(-3) * (((m.x12 - m.x49)**2
    + (m.x91 - m.x128)**2 + (m.x170 - m.x207)**2)**(-3) - 2) + ((m.x12 - m.x50)
    **2 + (m.x91 - m.x129)**2 + (m.x170 - m.x208)**2)**(-3) * (((m.x12 - m.x50)
    **2 + (m.x91 - m.x129)**2 + (m.x170 - m.x208)**2)**(-3) - 2) + ((m.x12 -
    m.x51)**2 + (m.x91 - m.x130)**2 + (m.x170 - m.x209)**2)**(-3) * (((m.x12 -
    m.x51)**2 + (m.x91 - m.x130)**2 + (m.x170 - m.x209)**2)**(-3) - 2) + ((
    m.x12 - m.x52)**2 + (m.x91 - m.x131)**2 + (m.x170 - m.x210)**2)**(-3) * (((
    m.x12 - m.x52)**2 + (m.x91 - m.x131)**2 + (m.x170 - m.x210)**2)**(-3) - 2)
    + ((m.x12 - m.x53)**2 + (m.x91 - m.x132)**2 + (m.x170 - m.x211)**2)**(-3)
    * (((m.x12 - m.x53)**2 + (m.x91 - m.x132)**2 + (m.x170 - m.x211)**2)**(-3)
    - 2) + ((m.x12 - m.x54)**2 + (m.x91 - m.x133)**2 + (m.x170 - m.x212)**2)**
    (-3) * (((m.x12 - m.x54)**2 + (m.x91 - m.x133)**2 + (m.x170 - m.x212)**2)**
    (-3) - 2) + ((m.x12 - m.x55)**2 + (m.x91 - m.x134)**2 + (m.x170 - m.x213)**
    2)**(-3) * (((m.x12 - m.x55)**2 + (m.x91 - m.x134)**2 + (m.x170 - m.x213)**
    2)**(-3) - 2) + ((m.x12 - m.x56)**2 + (m.x91 - m.x135)**2 + (m.x170 -
    m.x214)**2)**(-3) * (((m.x12 - m.x56)**2 + (m.x91 - m.x135)**2 + (m.x170 -
    m.x214)**2)**(-3) - 2) + ((m.x12 - m.x57)**2 + (m.x91 - m.x136)**2 + (
    m.x170 - m.x215)**2)**(-3) * (((m.x12 - m.x57)**2 + (m.x91 - m.x136)**2 + (
    m.x170 - m.x215)**2)**(-3) - 2) + ((m.x12 - m.x58)**2 + (m.x91 - m.x137)**2
    + (m.x170 - m.x216)**2)**(-3) * (((m.x12 - m.x58)**2 + (m.x91 - m.x137)**2
    + (m.x170 - m.x216)**2)**(-3) - 2) + ((m.x12 - m.x59)**2 + (m.x91 - m.x138)
    **2 + (m.x170 - m.x217)**2)**(-3) * (((m.x12 - m.x59)**2 + (m.x91 - m.x138)
    **2 + (m.x170 - m.x217)**2)**(-3) - 2) + ((m.x12 - m.x60)**2 + (m.x91 -
    m.x139)**2 + (m.x170 - m.x218)**2)**(-3) * (((m.x12 - m.x60)**2 + (m.x91 -
    m.x139)**2 + (m.x170 - m.x218)**2)**(-3) - 2) + ((m.x12 - m.x61)**2 + (
    m.x91 - m.x140)**2 + (m.x170 - m.x219)**2)**(-3) * (((m.x12 - m.x61)**2 + (
    m.x91 - m.x140)**2 + (m.x170 - m.x219)**2)**(-3) - 2) + ((m.x12 - m.x62)**2
    + (m.x91 - m.x141)**2 + (m.x170 - m.x220)**2)**(-3) * (((m.x12 - m.x62)**2
    + (m.x91 - m.x141)**2 + (m.x170 - m.x220)**2)**(-3) - 2) + ((m.x12 - m.x63)
    **2 + (m.x91 - m.x142)**2 + (m.x170 - m.x221)**2)**(-3) * (((m.x12 - m.x63)
    **2 + (m.x91 - m.x142)**2 + (m.x170 - m.x221)**2)**(-3) - 2) + ((m.x12 -
    m.x64)**2 + (m.x91 - m.x143)**2 + (m.x170 - m.x222)**2)**(-3) * (((m.x12 -
    m.x64)**2 + (m.x91 - m.x143)**2 + (m.x170 - m.x222)**2)**(-3) - 2) + ((
    m.x12 - m.x65)**2 + (m.x91 - m.x144)**2 + (m.x170 - m.x223)**2)**(-3) * (((
    m.x12 - m.x65)**2 + (m.x91 - m.x144)**2 + (m.x170 - m.x223)**2)**(-3) - 2)
    + ((m.x12 - m.x66)**2 + (m.x91 - m.x145)**2 + (m.x170 - m.x224)**2)**(-3)
    * (((m.x12 - m.x66)**2 + (m.x91 - m.x145)**2 + (m.x170 - m.x224)**2)**(-3)
    - 2) + ((m.x12 - m.x67)**2 + (m.x91 - m.x146)**2 + (m.x170 - m.x225)**2)**
    (-3) * (((m.x12 - m.x67)**2 + (m.x91 - m.x146)**2 + (m.x170 - m.x225)**2)**
    (-3) - 2) + ((m.x12 - m.x68)**2 + (m.x91 - m.x147)**2 + (m.x170 - m.x226)**
    2)**(-3) * (((m.x12 - m.x68)**2 + (m.x91 - m.x147)**2 + (m.x170 - m.x226)**
    2)**(-3) - 2) + ((m.x12 - m.x69)**2 + (m.x91 - m.x148)**2 + (m.x170 -
    m.x227)**2)**(-3) * (((m.x12 - m.x69)**2 + (m.x91 - m.x148)**2 + (m.x170 -
    m.x227)**2)**(-3) - 2) + ((m.x12 - m.x70)**2 + (m.x91 - m.x149)**2 + (
    m.x170 - m.x228)**2)**(-3) * (((m.x12 - m.x70)**2 + (m.x91 - m.x149)**2 + (
    m.x170 - m.x228)**2)**(-3) - 2) + ((m.x12 - m.x71)**2 + (m.x91 - m.x150)**2
    + (m.x170 - m.x229)**2)**(-3) * (((m.x12 - m.x71)**2 + (m.x91 - m.x150)**2
    + (m.x170 - m.x229)**2)**(-3) - 2) + ((m.x12 - m.x72)**2 + (m.x91 - m.x151)
    **2 + (m.x170 - m.x230)**2)**(-3) * (((m.x12 - m.x72)**2 + (m.x91 - m.x151)
    **2 + (m.x170 - m.x230)**2)**(-3) - 2) + ((m.x12 - m.x73)**2 + (m.x91 -
    m.x152)**2 + (m.x170 - m.x231)**2)**(-3) * (((m.x12 - m.x73)**2 + (m.x91 -
    m.x152)**2 + (m.x170 - m.x231)**2)**(-3) - 2) + ((m.x12 - m.x74)**2 + (
    m.x91 - m.x153)**2 + (m.x170 - m.x232)**2)**(-3) * (((m.x12 - m.x74)**2 + (
    m.x91 - m.x153)**2 + (m.x170 - m.x232)**2)**(-3) - 2) + ((m.x12 - m.x75)**2
    + (m.x91 - m.x154)**2 + (m.x170 - m.x233)**2)**(-3) * (((m.x12 - m.x75)**2
    + (m.x91 - m.x154)**2 + (m.x170 - m.x233)**2)**(-3) - 2) + ((m.x12 - m.x76)
    **2 + (m.x91 - m.x155)**2 + (m.x170 - m.x234)**2)**(-3) * (((m.x12 - m.x76)
    **2 + (m.x91 - m.x155)**2 + (m.x170 - m.x234)**2)**(-3) - 2) + ((m.x12 -
    m.x77)**2 + (m.x91 - m.x156)**2 + (m.x170 - m.x235)**2)**(-3) * (((m.x12 -
    m.x77)**2 + (m.x91 - m.x156)**2 + (m.x170 - m.x235)**2)**(-3) - 2) + ((
    m.x12 - m.x78)**2 + (m.x91 - m.x157)**2 + (m.x170 - m.x236)**2)**(-3) * (((
    m.x12 - m.x78)**2 + (m.x91 - m.x157)**2 + (m.x170 - m.x236)**2)**(-3) - 2)
    + ((m.x12 - m.x79)**2 + (m.x91 - m.x158)**2 + (m.x170 - m.x237)**2)**(-3)
    * (((m.x12 - m.x79)**2 + (m.x91 - m.x158)**2 + (m.x170 - m.x237)**2)**(-3)
    - 2) + ((m.x13 - m.x14)**2 + (m.x92 - m.x93)**2 + (m.x171 - m.x172)**2)**(
    -3) * (((m.x13 - m.x14)**2 + (m.x92 - m.x93)**2 + (m.x171 - m.x172)**2)**(
    -3) - 2) + ((m.x13 - m.x15)**2 + (m.x92 - m.x94)**2 + (m.x171 - m.x173)**2)
    **(-3) * (((m.x13 - m.x15)**2 + (m.x92 - m.x94)**2 + (m.x171 - m.x173)**2)
    **(-3) - 2) + ((m.x13 - m.x16)**2 + (m.x92 - m.x95)**2 + (m.x171 - m.x174)
    **2)**(-3) * (((m.x13 - m.x16)**2 + (m.x92 - m.x95)**2 + (m.x171 - m.x174)
    **2)**(-3) - 2) + ((m.x13 - m.x17)**2 + (m.x92 - m.x96)**2 + (m.x171 -
    m.x175)**2)**(-3) * (((m.x13 - m.x17)**2 + (m.x92 - m.x96)**2 + (m.x171 -
    m.x175)**2)**(-3) - 2) + ((m.x13 - m.x18)**2 + (m.x92 - m.x97)**2 + (m.x171
    - m.x176)**2)**(-3) * (((m.x13 - m.x18)**2 + (m.x92 - m.x97)**2 + (m.x171
    - m.x176)**2)**(-3) - 2) + ((m.x13 - m.x19)**2 + (m.x92 - m.x98)**2 + (
    m.x171 - m.x177)**2)**(-3) * (((m.x13 - m.x19)**2 + (m.x92 - m.x98)**2 + (
    m.x171 - m.x177)**2)**(-3) - 2) + ((m.x13 - m.x20)**2 + (m.x92 - m.x99)**2
    + (m.x171 - m.x178)**2)**(-3) * (((m.x13 - m.x20)**2 + (m.x92 - m.x99)**2
    + (m.x171 - m.x178)**2)**(-3) - 2) + ((m.x13 - m.x21)**2 + (m.x92 - m.x100)
    **2 + (m.x171 - m.x179)**2)**(-3) * (((m.x13 - m.x21)**2 + (m.x92 - m.x100)
    **2 + (m.x171 - m.x179)**2)**(-3) - 2) + ((m.x13 - m.x22)**2 + (m.x92 -
    m.x101)**2 + (m.x171 - m.x180)**2)**(-3) * (((m.x13 - m.x22)**2 + (m.x92 -
    m.x101)**2 + (m.x171 - m.x180)**2)**(-3) - 2) + ((m.x13 - m.x23)**2 + (
    m.x92 - m.x102)**2 + (m.x171 - m.x181)**2)**(-3) * (((m.x13 - m.x23)**2 + (
    m.x92 - m.x102)**2 + (m.x171 - m.x181)**2)**(-3) - 2) + ((m.x13 - m.x24)**2
    + (m.x92 - m.x103)**2 + (m.x171 - m.x182)**2)**(-3) * (((m.x13 - m.x24)**2
    + (m.x92 - m.x103)**2 + (m.x171 - m.x182)**2)**(-3) - 2) + ((m.x13 - m.x25)
    **2 + (m.x92 - m.x104)**2 + (m.x171 - m.x183)**2)**(-3) * (((m.x13 - m.x25)
    **2 + (m.x92 - m.x104)**2 + (m.x171 - m.x183)**2)**(-3) - 2) + ((m.x13 -
    m.x26)**2 + (m.x92 - m.x105)**2 + (m.x171 - m.x184)**2)**(-3) * (((m.x13 -
    m.x26)**2 + (m.x92 - m.x105)**2 + (m.x171 - m.x184)**2)**(-3) - 2) + ((
    m.x13 - m.x27)**2 + (m.x92 - m.x106)**2 + (m.x171 - m.x185)**2)**(-3) * (((
    m.x13 - m.x27)**2 + (m.x92 - m.x106)**2 + (m.x171 - m.x185)**2)**(-3) - 2)
    + ((m.x13 - m.x28)**2 + (m.x92 - m.x107)**2 + (m.x171 - m.x186)**2)**(-3)
    * (((m.x13 - m.x28)**2 + (m.x92 - m.x107)**2 + (m.x171 - m.x186)**2)**(-3)
    - 2) + ((m.x13 - m.x29)**2 + (m.x92 - m.x108)**2 + (m.x171 - m.x187)**2)**
    (-3) * (((m.x13 - m.x29)**2 + (m.x92 - m.x108)**2 + (m.x171 - m.x187)**2)**
    (-3) - 2) + ((m.x13 - m.x30)**2 + (m.x92 - m.x109)**2 + (m.x171 - m.x188)**
    2)**(-3) * (((m.x13 - m.x30)**2 + (m.x92 - m.x109)**2 + (m.x171 - m.x188)**
    2)**(-3) - 2) + ((m.x13 - m.x31)**2 + (m.x92 - m.x110)**2 + (m.x171 -
    m.x189)**2)**(-3) * (((m.x13 - m.x31)**2 + (m.x92 - m.x110)**2 + (m.x171 -
    m.x189)**2)**(-3) - 2) + ((m.x13 - m.x32)**2 + (m.x92 - m.x111)**2 + (
    m.x171 - m.x190)**2)**(-3) * (((m.x13 - m.x32)**2 + (m.x92 - m.x111)**2 + (
    m.x171 - m.x190)**2)**(-3) - 2) + ((m.x13 - m.x33)**2 + (m.x92 - m.x112)**2
    + (m.x171 - m.x191)**2)**(-3) * (((m.x13 - m.x33)**2 + (m.x92 - m.x112)**2
    + (m.x171 - m.x191)**2)**(-3) - 2) + ((m.x13 - m.x34)**2 + (m.x92 - m.x113)
    **2 + (m.x171 - m.x192)**2)**(-3) * (((m.x13 - m.x34)**2 + (m.x92 - m.x113)
    **2 + (m.x171 - m.x192)**2)**(-3) - 2) + ((m.x13 - m.x35)**2 + (m.x92 -
    m.x114)**2 + (m.x171 - m.x193)**2)**(-3) * (((m.x13 - m.x35)**2 + (m.x92 -
    m.x114)**2 + (m.x171 - m.x193)**2)**(-3) - 2) + ((m.x13 - m.x36)**2 + (
    m.x92 - m.x115)**2 + (m.x171 - m.x194)**2)**(-3) * (((m.x13 - m.x36)**2 + (
    m.x92 - m.x115)**2 + (m.x171 - m.x194)**2)**(-3) - 2) + ((m.x13 - m.x37)**2
    + (m.x92 - m.x116)**2 + (m.x171 - m.x195)**2)**(-3) * (((m.x13 - m.x37)**2
    + (m.x92 - m.x116)**2 + (m.x171 - m.x195)**2)**(-3) - 2) + ((m.x13 - m.x38)
    **2 + (m.x92 - m.x117)**2 + (m.x171 - m.x196)**2)**(-3) * (((m.x13 - m.x38)
    **2 + (m.x92 - m.x117)**2 + (m.x171 - m.x196)**2)**(-3) - 2) + ((m.x13 -
    m.x39)**2 + (m.x92 - m.x118)**2 + (m.x171 - m.x197)**2)**(-3) * (((m.x13 -
    m.x39)**2 + (m.x92 - m.x118)**2 + (m.x171 - m.x197)**2)**(-3) - 2) + ((
    m.x13 - m.x40)**2 + (m.x92 - m.x119)**2 + (m.x171 - m.x198)**2)**(-3) * (((
    m.x13 - m.x40)**2 + (m.x92 - m.x119)**2 + (m.x171 - m.x198)**2)**(-3) - 2)
    + ((m.x13 - m.x41)**2 + (m.x92 - m.x120)**2 + (m.x171 - m.x199)**2)**(-3)
    * (((m.x13 - m.x41)**2 + (m.x92 - m.x120)**2 + (m.x171 - m.x199)**2)**(-3)
    - 2) + ((m.x13 - m.x42)**2 + (m.x92 - m.x121)**2 + (m.x171 - m.x200)**2)**
    (-3) * (((m.x13 - m.x42)**2 + (m.x92 - m.x121)**2 + (m.x171 - m.x200)**2)**
    (-3) - 2) + ((m.x13 - m.x43)**2 + (m.x92 - m.x122)**2 + (m.x171 - m.x201)**
    2)**(-3) * (((m.x13 - m.x43)**2 + (m.x92 - m.x122)**2 + (m.x171 - m.x201)**
    2)**(-3) - 2) + ((m.x13 - m.x44)**2 + (m.x92 - m.x123)**2 + (m.x171 -
    m.x202)**2)**(-3) * (((m.x13 - m.x44)**2 + (m.x92 - m.x123)**2 + (m.x171 -
    m.x202)**2)**(-3) - 2) + ((m.x13 - m.x45)**2 + (m.x92 - m.x124)**2 + (
    m.x171 - m.x203)**2)**(-3) * (((m.x13 - m.x45)**2 + (m.x92 - m.x124)**2 + (
    m.x171 - m.x203)**2)**(-3) - 2) + ((m.x13 - m.x46)**2 + (m.x92 - m.x125)**2
    + (m.x171 - m.x204)**2)**(-3) * (((m.x13 - m.x46)**2 + (m.x92 - m.x125)**2
    + (m.x171 - m.x204)**2)**(-3) - 2) + ((m.x13 - m.x47)**2 + (m.x92 - m.x126)
    **2 + (m.x171 - m.x205)**2)**(-3) * (((m.x13 - m.x47)**2 + (m.x92 - m.x126)
    **2 + (m.x171 - m.x205)**2)**(-3) - 2) + ((m.x13 - m.x48)**2 + (m.x92 -
    m.x127)**2 + (m.x171 - m.x206)**2)**(-3) * (((m.x13 - m.x48)**2 + (m.x92 -
    m.x127)**2 + (m.x171 - m.x206)**2)**(-3) - 2) + ((m.x13 - m.x49)**2 + (
    m.x92 - m.x128)**2 + (m.x171 - m.x207)**2)**(-3) * (((m.x13 - m.x49)**2 + (
    m.x92 - m.x128)**2 + (m.x171 - m.x207)**2)**(-3) - 2) + ((m.x13 - m.x50)**2
    + (m.x92 - m.x129)**2 + (m.x171 - m.x208)**2)**(-3) * (((m.x13 - m.x50)**2
    + (m.x92 - m.x129)**2 + (m.x171 - m.x208)**2)**(-3) - 2) + ((m.x13 - m.x51)
    **2 + (m.x92 - m.x130)**2 + (m.x171 - m.x209)**2)**(-3) * (((m.x13 - m.x51)
    **2 + (m.x92 - m.x130)**2 + (m.x171 - m.x209)**2)**(-3) - 2) + ((m.x13 -
    m.x52)**2 + (m.x92 - m.x131)**2 + (m.x171 - m.x210)**2)**(-3) * (((m.x13 -
    m.x52)**2 + (m.x92 - m.x131)**2 + (m.x171 - m.x210)**2)**(-3) - 2) + ((
    m.x13 - m.x53)**2 + (m.x92 - m.x132)**2 + (m.x171 - m.x211)**2)**(-3) * (((
    m.x13 - m.x53)**2 + (m.x92 - m.x132)**2 + (m.x171 - m.x211)**2)**(-3) - 2)
    + ((m.x13 - m.x54)**2 + (m.x92 - m.x133)**2 + (m.x171 - m.x212)**2)**(-3)
    * (((m.x13 - m.x54)**2 + (m.x92 - m.x133)**2 + (m.x171 - m.x212)**2)**(-3)
    - 2) + ((m.x13 - m.x55)**2 + (m.x92 - m.x134)**2 + (m.x171 - m.x213)**2)**
    (-3) * (((m.x13 - m.x55)**2 + (m.x92 - m.x134)**2 + (m.x171 - m.x213)**2)**
    (-3) - 2) + ((m.x13 - m.x56)**2 + (m.x92 - m.x135)**2 + (m.x171 - m.x214)**
    2)**(-3) * (((m.x13 - m.x56)**2 + (m.x92 - m.x135)**2 + (m.x171 - m.x214)**
    2)**(-3) - 2) + ((m.x13 - m.x57)**2 + (m.x92 - m.x136)**2 + (m.x171 -
    m.x215)**2)**(-3) * (((m.x13 - m.x57)**2 + (m.x92 - m.x136)**2 + (m.x171 -
    m.x215)**2)**(-3) - 2) + ((m.x13 - m.x58)**2 + (m.x92 - m.x137)**2 + (
    m.x171 - m.x216)**2)**(-3) * (((m.x13 - m.x58)**2 + (m.x92 - m.x137)**2 + (
    m.x171 - m.x216)**2)**(-3) - 2) + ((m.x13 - m.x59)**2 + (m.x92 - m.x138)**2
    + (m.x171 - m.x217)**2)**(-3) * (((m.x13 - m.x59)**2 + (m.x92 - m.x138)**2
    + (m.x171 - m.x217)**2)**(-3) - 2) + ((m.x13 - m.x60)**2 + (m.x92 - m.x139)
    **2 + (m.x171 - m.x218)**2)**(-3) * (((m.x13 - m.x60)**2 + (m.x92 - m.x139)
    **2 + (m.x171 - m.x218)**2)**(-3) - 2) + ((m.x13 - m.x61)**2 + (m.x92 -
    m.x140)**2 + (m.x171 - m.x219)**2)**(-3) * (((m.x13 - m.x61)**2 + (m.x92 -
    m.x140)**2 + (m.x171 - m.x219)**2)**(-3) - 2) + ((m.x13 - m.x62)**2 + (
    m.x92 - m.x141)**2 + (m.x171 - m.x220)**2)**(-3) * (((m.x13 - m.x62)**2 + (
    m.x92 - m.x141)**2 + (m.x171 - m.x220)**2)**(-3) - 2) + ((m.x13 - m.x63)**2
    + (m.x92 - m.x142)**2 + (m.x171 - m.x221)**2)**(-3) * (((m.x13 - m.x63)**2
    + (m.x92 - m.x142)**2 + (m.x171 - m.x221)**2)**(-3) - 2) + ((m.x13 - m.x64)
    **2 + (m.x92 - m.x143)**2 + (m.x171 - m.x222)**2)**(-3) * (((m.x13 - m.x64)
    **2 + (m.x92 - m.x143)**2 + (m.x171 - m.x222)**2)**(-3) - 2) + ((m.x13 -
    m.x65)**2 + (m.x92 - m.x144)**2 + (m.x171 - m.x223)**2)**(-3) * (((m.x13 -
    m.x65)**2 + (m.x92 - m.x144)**2 + (m.x171 - m.x223)**2)**(-3) - 2) + ((
    m.x13 - m.x66)**2 + (m.x92 - m.x145)**2 + (m.x171 - m.x224)**2)**(-3) * (((
    m.x13 - m.x66)**2 + (m.x92 - m.x145)**2 + (m.x171 - m.x224)**2)**(-3) - 2)
    + ((m.x13 - m.x67)**2 + (m.x92 - m.x146)**2 + (m.x171 - m.x225)**2)**(-3)
    * (((m.x13 - m.x67)**2 + (m.x92 - m.x146)**2 + (m.x171 - m.x225)**2)**(-3)
    - 2) + ((m.x13 - m.x68)**2 + (m.x92 - m.x147)**2 + (m.x171 - m.x226)**2)**
    (-3) * (((m.x13 - m.x68)**2 + (m.x92 - m.x147)**2 + (m.x171 - m.x226)**2)**
    (-3) - 2) + ((m.x13 - m.x69)**2 + (m.x92 - m.x148)**2 + (m.x171 - m.x227)**
    2)**(-3) * (((m.x13 - m.x69)**2 + (m.x92 - m.x148)**2 + (m.x171 - m.x227)**
    2)**(-3) - 2) + ((m.x13 - m.x70)**2 + (m.x92 - m.x149)**2 + (m.x171 -
    m.x228)**2)**(-3) * (((m.x13 - m.x70)**2 + (m.x92 - m.x149)**2 + (m.x171 -
    m.x228)**2)**(-3) - 2) + ((m.x13 - m.x71)**2 + (m.x92 - m.x150)**2 + (
    m.x171 - m.x229)**2)**(-3) * (((m.x13 - m.x71)**2 + (m.x92 - m.x150)**2 + (
    m.x171 - m.x229)**2)**(-3) - 2) + ((m.x13 - m.x72)**2 + (m.x92 - m.x151)**2
    + (m.x171 - m.x230)**2)**(-3) * (((m.x13 - m.x72)**2 + (m.x92 - m.x151)**2
    + (m.x171 - m.x230)**2)**(-3) - 2) + ((m.x13 - m.x73)**2 + (m.x92 - m.x152)
    **2 + (m.x171 - m.x231)**2)**(-3) * (((m.x13 - m.x73)**2 + (m.x92 - m.x152)
    **2 + (m.x171 - m.x231)**2)**(-3) - 2) + ((m.x13 - m.x74)**2 + (m.x92 -
    m.x153)**2 + (m.x171 - m.x232)**2)**(-3) * (((m.x13 - m.x74)**2 + (m.x92 -
    m.x153)**2 + (m.x171 - m.x232)**2)**(-3) - 2) + ((m.x13 - m.x75)**2 + (
    m.x92 - m.x154)**2 + (m.x171 - m.x233)**2)**(-3) * (((m.x13 - m.x75)**2 + (
    m.x92 - m.x154)**2 + (m.x171 - m.x233)**2)**(-3) - 2) + ((m.x13 - m.x76)**2
    + (m.x92 - m.x155)**2 + (m.x171 - m.x234)**2)**(-3) * (((m.x13 - m.x76)**2
    + (m.x92 - m.x155)**2 + (m.x171 - m.x234)**2)**(-3) - 2) + ((m.x13 - m.x77)
    **2 + (m.x92 - m.x156)**2 + (m.x171 - m.x235)**2)**(-3) * (((m.x13 - m.x77)
    **2 + (m.x92 - m.x156)**2 + (m.x171 - m.x235)**2)**(-3) - 2) + ((m.x13 -
    m.x78)**2 + (m.x92 - m.x157)**2 + (m.x171 - m.x236)**2)**(-3) * (((m.x13 -
    m.x78)**2 + (m.x92 - m.x157)**2 + (m.x171 - m.x236)**2)**(-3) - 2) + ((
    m.x13 - m.x79)**2 + (m.x92 - m.x158)**2 + (m.x171 - m.x237)**2)**(-3) * (((
    m.x13 - m.x79)**2 + (m.x92 - m.x158)**2 + (m.x171 - m.x237)**2)**(-3) - 2)
    + ((m.x14 - m.x15)**2 + (m.x93 - m.x94)**2 + (m.x172 - m.x173)**2)**(-3)
    * (((m.x14 - m.x15)**2 + (m.x93 - m.x94)**2 + (m.x172 - m.x173)**2)**(-3)
    - 2) + ((m.x14 - m.x16)**2 + (m.x93 - m.x95)**2 + (m.x172 - m.x174)**2)**(
    -3) * (((m.x14 - m.x16)**2 + (m.x93 - m.x95)**2 + (m.x172 - m.x174)**2)**(
    -3) - 2) + ((m.x14 - m.x17)**2 + (m.x93 - m.x96)**2 + (m.x172 - m.x175)**2)
    **(-3) * (((m.x14 - m.x17)**2 + (m.x93 - m.x96)**2 + (m.x172 - m.x175)**2)
    **(-3) - 2) + ((m.x14 - m.x18)**2 + (m.x93 - m.x97)**2 + (m.x172 - m.x176)
    **2)**(-3) * (((m.x14 - m.x18)**2 + (m.x93 - m.x97)**2 + (m.x172 - m.x176)
    **2)**(-3) - 2) + ((m.x14 - m.x19)**2 + (m.x93 - m.x98)**2 + (m.x172 -
    m.x177)**2)**(-3) * (((m.x14 - m.x19)**2 + (m.x93 - m.x98)**2 + (m.x172 -
    m.x177)**2)**(-3) - 2) + ((m.x14 - m.x20)**2 + (m.x93 - m.x99)**2 + (m.x172
    - m.x178)**2)**(-3) * (((m.x14 - m.x20)**2 + (m.x93 - m.x99)**2 + (m.x172
    - m.x178)**2)**(-3) - 2) + ((m.x14 - m.x21)**2 + (m.x93 - m.x100)**2 + (
    m.x172 - m.x179)**2)**(-3) * (((m.x14 - m.x21)**2 + (m.x93 - m.x100)**2 + (
    m.x172 - m.x179)**2)**(-3) - 2) + ((m.x14 - m.x22)**2 + (m.x93 - m.x101)**2
    + (m.x172 - m.x180)**2)**(-3) * (((m.x14 - m.x22)**2 + (m.x93 - m.x101)**2
    + (m.x172 - m.x180)**2)**(-3) - 2) + ((m.x14 - m.x23)**2 + (m.x93 - m.x102)
    **2 + (m.x172 - m.x181)**2)**(-3) * (((m.x14 - m.x23)**2 + (m.x93 - m.x102)
    **2 + (m.x172 - m.x181)**2)**(-3) - 2) + ((m.x14 - m.x24)**2 + (m.x93 -
    m.x103)**2 + (m.x172 - m.x182)**2)**(-3) * (((m.x14 - m.x24)**2 + (m.x93 -
    m.x103)**2 + (m.x172 - m.x182)**2)**(-3) - 2) + ((m.x14 - m.x25)**2 + (
    m.x93 - m.x104)**2 + (m.x172 - m.x183)**2)**(-3) * (((m.x14 - m.x25)**2 + (
    m.x93 - m.x104)**2 + (m.x172 - m.x183)**2)**(-3) - 2) + ((m.x14 - m.x26)**2
    + (m.x93 - m.x105)**2 + (m.x172 - m.x184)**2)**(-3) * (((m.x14 - m.x26)**2
    + (m.x93 - m.x105)**2 + (m.x172 - m.x184)**2)**(-3) - 2) + ((m.x14 - m.x27)
    **2 + (m.x93 - m.x106)**2 + (m.x172 - m.x185)**2)**(-3) * (((m.x14 - m.x27)
    **2 + (m.x93 - m.x106)**2 + (m.x172 - m.x185)**2)**(-3) - 2) + ((m.x14 -
    m.x28)**2 + (m.x93 - m.x107)**2 + (m.x172 - m.x186)**2)**(-3) * (((m.x14 -
    m.x28)**2 + (m.x93 - m.x107)**2 + (m.x172 - m.x186)**2)**(-3) - 2) + ((
    m.x14 - m.x29)**2 + (m.x93 - m.x108)**2 + (m.x172 - m.x187)**2)**(-3) * (((
    m.x14 - m.x29)**2 + (m.x93 - m.x108)**2 + (m.x172 - m.x187)**2)**(-3) - 2)
    + ((m.x14 - m.x30)**2 + (m.x93 - m.x109)**2 + (m.x172 - m.x188)**2)**(-3)
    * (((m.x14 - m.x30)**2 + (m.x93 - m.x109)**2 + (m.x172 - m.x188)**2)**(-3)
    - 2) + ((m.x14 - m.x31)**2 + (m.x93 - m.x110)**2 + (m.x172 - m.x189)**2)**
    (-3) * (((m.x14 - m.x31)**2 + (m.x93 - m.x110)**2 + (m.x172 - m.x189)**2)**
    (-3) - 2) + ((m.x14 - m.x32)**2 + (m.x93 - m.x111)**2 + (m.x172 - m.x190)**
    2)**(-3) * (((m.x14 - m.x32)**2 + (m.x93 - m.x111)**2 + (m.x172 - m.x190)**
    2)**(-3) - 2) + ((m.x14 - m.x33)**2 + (m.x93 - m.x112)**2 + (m.x172 -
    m.x191)**2)**(-3) * (((m.x14 - m.x33)**2 + (m.x93 - m.x112)**2 + (m.x172 -
    m.x191)**2)**(-3) - 2) + ((m.x14 - m.x34)**2 + (m.x93 - m.x113)**2 + (
    m.x172 - m.x192)**2)**(-3) * (((m.x14 - m.x34)**2 + (m.x93 - m.x113)**2 + (
    m.x172 - m.x192)**2)**(-3) - 2) + ((m.x14 - m.x35)**2 + (m.x93 - m.x114)**2
    + (m.x172 - m.x193)**2)**(-3) * (((m.x14 - m.x35)**2 + (m.x93 - m.x114)**2
    + (m.x172 - m.x193)**2)**(-3) - 2) + ((m.x14 - m.x36)**2 + (m.x93 - m.x115)
    **2 + (m.x172 - m.x194)**2)**(-3) * (((m.x14 - m.x36)**2 + (m.x93 - m.x115)
    **2 + (m.x172 - m.x194)**2)**(-3) - 2) + ((m.x14 - m.x37)**2 + (m.x93 -
    m.x116)**2 + (m.x172 - m.x195)**2)**(-3) * (((m.x14 - m.x37)**2 + (m.x93 -
    m.x116)**2 + (m.x172 - m.x195)**2)**(-3) - 2) + ((m.x14 - m.x38)**2 + (
    m.x93 - m.x117)**2 + (m.x172 - m.x196)**2)**(-3) * (((m.x14 - m.x38)**2 + (
    m.x93 - m.x117)**2 + (m.x172 - m.x196)**2)**(-3) - 2) + ((m.x14 - m.x39)**2
    + (m.x93 - m.x118)**2 + (m.x172 - m.x197)**2)**(-3) * (((m.x14 - m.x39)**2
    + (m.x93 - m.x118)**2 + (m.x172 - m.x197)**2)**(-3) - 2) + ((m.x14 - m.x40)
    **2 + (m.x93 - m.x119)**2 + (m.x172 - m.x198)**2)**(-3) * (((m.x14 - m.x40)
    **2 + (m.x93 - m.x119)**2 + (m.x172 - m.x198)**2)**(-3) - 2) + ((m.x14 -
    m.x41)**2 + (m.x93 - m.x120)**2 + (m.x172 - m.x199)**2)**(-3) * (((m.x14 -
    m.x41)**2 + (m.x93 - m.x120)**2 + (m.x172 - m.x199)**2)**(-3) - 2) + ((
    m.x14 - m.x42)**2 + (m.x93 - m.x121)**2 + (m.x172 - m.x200)**2)**(-3) * (((
    m.x14 - m.x42)**2 + (m.x93 - m.x121)**2 + (m.x172 - m.x200)**2)**(-3) - 2)
    + ((m.x14 - m.x43)**2 + (m.x93 - m.x122)**2 + (m.x172 - m.x201)**2)**(-3)
    * (((m.x14 - m.x43)**2 + (m.x93 - m.x122)**2 + (m.x172 - m.x201)**2)**(-3)
    - 2) + ((m.x14 - m.x44)**2 + (m.x93 - m.x123)**2 + (m.x172 - m.x202)**2)**
    (-3) * (((m.x14 - m.x44)**2 + (m.x93 - m.x123)**2 + (m.x172 - m.x202)**2)**
    (-3) - 2) + ((m.x14 - m.x45)**2 + (m.x93 - m.x124)**2 + (m.x172 - m.x203)**
    2)**(-3) * (((m.x14 - m.x45)**2 + (m.x93 - m.x124)**2 + (m.x172 - m.x203)**
    2)**(-3) - 2) + ((m.x14 - m.x46)**2 + (m.x93 - m.x125)**2 + (m.x172 -
    m.x204)**2)**(-3) * (((m.x14 - m.x46)**2 + (m.x93 - m.x125)**2 + (m.x172 -
    m.x204)**2)**(-3) - 2) + ((m.x14 - m.x47)**2 + (m.x93 - m.x126)**2 + (
    m.x172 - m.x205)**2)**(-3) * (((m.x14 - m.x47)**2 + (m.x93 - m.x126)**2 + (
    m.x172 - m.x205)**2)**(-3) - 2) + ((m.x14 - m.x48)**2 + (m.x93 - m.x127)**2
    + (m.x172 - m.x206)**2)**(-3) * (((m.x14 - m.x48)**2 + (m.x93 - m.x127)**2
    + (m.x172 - m.x206)**2)**(-3) - 2) + ((m.x14 - m.x49)**2 + (m.x93 - m.x128)
    **2 + (m.x172 - m.x207)**2)**(-3) * (((m.x14 - m.x49)**2 + (m.x93 - m.x128)
    **2 + (m.x172 - m.x207)**2)**(-3) - 2) + ((m.x14 - m.x50)**2 + (m.x93 -
    m.x129)**2 + (m.x172 - m.x208)**2)**(-3) * (((m.x14 - m.x50)**2 + (m.x93 -
    m.x129)**2 + (m.x172 - m.x208)**2)**(-3) - 2) + ((m.x14 - m.x51)**2 + (
    m.x93 - m.x130)**2 + (m.x172 - m.x209)**2)**(-3) * (((m.x14 - m.x51)**2 + (
    m.x93 - m.x130)**2 + (m.x172 - m.x209)**2)**(-3) - 2) + ((m.x14 - m.x52)**2
    + (m.x93 - m.x131)**2 + (m.x172 - m.x210)**2)**(-3) * (((m.x14 - m.x52)**2
    + (m.x93 - m.x131)**2 + (m.x172 - m.x210)**2)**(-3) - 2) + ((m.x14 - m.x53)
    **2 + (m.x93 - m.x132)**2 + (m.x172 - m.x211)**2)**(-3) * (((m.x14 - m.x53)
    **2 + (m.x93 - m.x132)**2 + (m.x172 - m.x211)**2)**(-3) - 2) + ((m.x14 -
    m.x54)**2 + (m.x93 - m.x133)**2 + (m.x172 - m.x212)**2)**(-3) * (((m.x14 -
    m.x54)**2 + (m.x93 - m.x133)**2 + (m.x172 - m.x212)**2)**(-3) - 2) + ((
    m.x14 - m.x55)**2 + (m.x93 - m.x134)**2 + (m.x172 - m.x213)**2)**(-3) * (((
    m.x14 - m.x55)**2 + (m.x93 - m.x134)**2 + (m.x172 - m.x213)**2)**(-3) - 2)
    + ((m.x14 - m.x56)**2 + (m.x93 - m.x135)**2 + (m.x172 - m.x214)**2)**(-3)
    * (((m.x14 - m.x56)**2 + (m.x93 - m.x135)**2 + (m.x172 - m.x214)**2)**(-3)
    - 2) + ((m.x14 - m.x57)**2 + (m.x93 - m.x136)**2 + (m.x172 - m.x215)**2)**
    (-3) * (((m.x14 - m.x57)**2 + (m.x93 - m.x136)**2 + (m.x172 - m.x215)**2)**
    (-3) - 2) + ((m.x14 - m.x58)**2 + (m.x93 - m.x137)**2 + (m.x172 - m.x216)**
    2)**(-3) * (((m.x14 - m.x58)**2 + (m.x93 - m.x137)**2 + (m.x172 - m.x216)**
    2)**(-3) - 2) + ((m.x14 - m.x59)**2 + (m.x93 - m.x138)**2 + (m.x172 -
    m.x217)**2)**(-3) * (((m.x14 - m.x59)**2 + (m.x93 - m.x138)**2 + (m.x172 -
    m.x217)**2)**(-3) - 2) + ((m.x14 - m.x60)**2 + (m.x93 - m.x139)**2 + (
    m.x172 - m.x218)**2)**(-3) * (((m.x14 - m.x60)**2 + (m.x93 - m.x139)**2 + (
    m.x172 - m.x218)**2)**(-3) - 2) + ((m.x14 - m.x61)**2 + (m.x93 - m.x140)**2
    + (m.x172 - m.x219)**2)**(-3) * (((m.x14 - m.x61)**2 + (m.x93 - m.x140)**2
    + (m.x172 - m.x219)**2)**(-3) - 2) + ((m.x14 - m.x62)**2 + (m.x93 - m.x141)
    **2 + (m.x172 - m.x220)**2)**(-3) * (((m.x14 - m.x62)**2 + (m.x93 - m.x141)
    **2 + (m.x172 - m.x220)**2)**(-3) - 2) + ((m.x14 - m.x63)**2 + (m.x93 -
    m.x142)**2 + (m.x172 - m.x221)**2)**(-3) * (((m.x14 - m.x63)**2 + (m.x93 -
    m.x142)**2 + (m.x172 - m.x221)**2)**(-3) - 2) + ((m.x14 - m.x64)**2 + (
    m.x93 - m.x143)**2 + (m.x172 - m.x222)**2)**(-3) * (((m.x14 - m.x64)**2 + (
    m.x93 - m.x143)**2 + (m.x172 - m.x222)**2)**(-3) - 2) + ((m.x14 - m.x65)**2
    + (m.x93 - m.x144)**2 + (m.x172 - m.x223)**2)**(-3) * (((m.x14 - m.x65)**2
    + (m.x93 - m.x144)**2 + (m.x172 - m.x223)**2)**(-3) - 2) + ((m.x14 - m.x66)
    **2 + (m.x93 - m.x145)**2 + (m.x172 - m.x224)**2)**(-3) * (((m.x14 - m.x66)
    **2 + (m.x93 - m.x145)**2 + (m.x172 - m.x224)**2)**(-3) - 2) + ((m.x14 -
    m.x67)**2 + (m.x93 - m.x146)**2 + (m.x172 - m.x225)**2)**(-3) * (((m.x14 -
    m.x67)**2 + (m.x93 - m.x146)**2 + (m.x172 - m.x225)**2)**(-3) - 2) + ((
    m.x14 - m.x68)**2 + (m.x93 - m.x147)**2 + (m.x172 - m.x226)**2)**(-3) * (((
    m.x14 - m.x68)**2 + (m.x93 - m.x147)**2 + (m.x172 - m.x226)**2)**(-3) - 2)
    + ((m.x14 - m.x69)**2 + (m.x93 - m.x148)**2 + (m.x172 - m.x227)**2)**(-3)
    * (((m.x14 - m.x69)**2 + (m.x93 - m.x148)**2 + (m.x172 - m.x227)**2)**(-3)
    - 2) + ((m.x14 - m.x70)**2 + (m.x93 - m.x149)**2 + (m.x172 - m.x228)**2)**
    (-3) * (((m.x14 - m.x70)**2 + (m.x93 - m.x149)**2 + (m.x172 - m.x228)**2)**
    (-3) - 2) + ((m.x14 - m.x71)**2 + (m.x93 - m.x150)**2 + (m.x172 - m.x229)**
    2)**(-3) * (((m.x14 - m.x71)**2 + (m.x93 - m.x150)**2 + (m.x172 - m.x229)**
    2)**(-3) - 2) + ((m.x14 - m.x72)**2 + (m.x93 - m.x151)**2 + (m.x172 -
    m.x230)**2)**(-3) * (((m.x14 - m.x72)**2 + (m.x93 - m.x151)**2 + (m.x172 -
    m.x230)**2)**(-3) - 2) + ((m.x14 - m.x73)**2 + (m.x93 - m.x152)**2 + (
    m.x172 - m.x231)**2)**(-3) * (((m.x14 - m.x73)**2 + (m.x93 - m.x152)**2 + (
    m.x172 - m.x231)**2)**(-3) - 2) + ((m.x14 - m.x74)**2 + (m.x93 - m.x153)**2
    + (m.x172 - m.x232)**2)**(-3) * (((m.x14 - m.x74)**2 + (m.x93 - m.x153)**2
    + (m.x172 - m.x232)**2)**(-3) - 2) + ((m.x14 - m.x75)**2 + (m.x93 - m.x154)
    **2 + (m.x172 - m.x233)**2)**(-3) * (((m.x14 - m.x75)**2 + (m.x93 - m.x154)
    **2 + (m.x172 - m.x233)**2)**(-3) - 2) + ((m.x14 - m.x76)**2 + (m.x93 -
    m.x155)**2 + (m.x172 - m.x234)**2)**(-3) * (((m.x14 - m.x76)**2 + (m.x93 -
    m.x155)**2 + (m.x172 - m.x234)**2)**(-3) - 2) + ((m.x14 - m.x77)**2 + (
    m.x93 - m.x156)**2 + (m.x172 - m.x235)**2)**(-3) * (((m.x14 - m.x77)**2 + (
    m.x93 - m.x156)**2 + (m.x172 - m.x235)**2)**(-3) - 2) + ((m.x14 - m.x78)**2
    + (m.x93 - m.x157)**2 + (m.x172 - m.x236)**2)**(-3) * (((m.x14 - m.x78)**2
    + (m.x93 - m.x157)**2 + (m.x172 - m.x236)**2)**(-3) - 2) + ((m.x14 - m.x79)
    **2 + (m.x93 - m.x158)**2 + (m.x172 - m.x237)**2)**(-3) * (((m.x14 - m.x79)
    **2 + (m.x93 - m.x158)**2 + (m.x172 - m.x237)**2)**(-3) - 2) + ((m.x15 -
    m.x16)**2 + (m.x94 - m.x95)**2 + (m.x173 - m.x174)**2)**(-3) * (((m.x15 -
    m.x16)**2 + (m.x94 - m.x95)**2 + (m.x173 - m.x174)**2)**(-3) - 2) + ((m.x15
    - m.x17)**2 + (m.x94 - m.x96)**2 + (m.x173 - m.x175)**2)**(-3) * (((m.x15
    - m.x17)**2 + (m.x94 - m.x96)**2 + (m.x173 - m.x175)**2)**(-3) - 2) + ((
    m.x15 - m.x18)**2 + (m.x94 - m.x97)**2 + (m.x173 - m.x176)**2)**(-3) * (((
    m.x15 - m.x18)**2 + (m.x94 - m.x97)**2 + (m.x173 - m.x176)**2)**(-3) - 2)
    + ((m.x15 - m.x19)**2 + (m.x94 - m.x98)**2 + (m.x173 - m.x177)**2)**(-3)
    * (((m.x15 - m.x19)**2 + (m.x94 - m.x98)**2 + (m.x173 - m.x177)**2)**(-3)
    - 2) + ((m.x15 - m.x20)**2 + (m.x94 - m.x99)**2 + (m.x173 - m.x178)**2)**(
    -3) * (((m.x15 - m.x20)**2 + (m.x94 - m.x99)**2 + (m.x173 - m.x178)**2)**(
    -3) - 2) + ((m.x15 - m.x21)**2 + (m.x94 - m.x100)**2 + (m.x173 - m.x179)**2)
    **(-3) * (((m.x15 - m.x21)**2 + (m.x94 - m.x100)**2 + (m.x173 - m.x179)**2)
    **(-3) - 2) + ((m.x15 - m.x22)**2 + (m.x94 - m.x101)**2 + (m.x173 - m.x180)
    **2)**(-3) * (((m.x15 - m.x22)**2 + (m.x94 - m.x101)**2 + (m.x173 - m.x180)
    **2)**(-3) - 2) + ((m.x15 - m.x23)**2 + (m.x94 - m.x102)**2 + (m.x173 -
    m.x181)**2)**(-3) * (((m.x15 - m.x23)**2 + (m.x94 - m.x102)**2 + (m.x173 -
    m.x181)**2)**(-3) - 2) + ((m.x15 - m.x24)**2 + (m.x94 - m.x103)**2 + (
    m.x173 - m.x182)**2)**(-3) * (((m.x15 - m.x24)**2 + (m.x94 - m.x103)**2 + (
    m.x173 - m.x182)**2)**(-3) - 2) + ((m.x15 - m.x25)**2 + (m.x94 - m.x104)**2
    + (m.x173 - m.x183)**2)**(-3) * (((m.x15 - m.x25)**2 + (m.x94 - m.x104)**2
    + (m.x173 - m.x183)**2)**(-3) - 2) + ((m.x15 - m.x26)**2 + (m.x94 - m.x105)
    **2 + (m.x173 - m.x184)**2)**(-3) * (((m.x15 - m.x26)**2 + (m.x94 - m.x105)
    **2 + (m.x173 - m.x184)**2)**(-3) - 2) + ((m.x15 - m.x27)**2 + (m.x94 -
    m.x106)**2 + (m.x173 - m.x185)**2)**(-3) * (((m.x15 - m.x27)**2 + (m.x94 -
    m.x106)**2 + (m.x173 - m.x185)**2)**(-3) - 2) + ((m.x15 - m.x28)**2 + (
    m.x94 - m.x107)**2 + (m.x173 - m.x186)**2)**(-3) * (((m.x15 - m.x28)**2 + (
    m.x94 - m.x107)**2 + (m.x173 - m.x186)**2)**(-3) - 2) + ((m.x15 - m.x29)**2
    + (m.x94 - m.x108)**2 + (m.x173 - m.x187)**2)**(-3) * (((m.x15 - m.x29)**2
    + (m.x94 - m.x108)**2 + (m.x173 - m.x187)**2)**(-3) - 2) + ((m.x15 - m.x30)
    **2 + (m.x94 - m.x109)**2 + (m.x173 - m.x188)**2)**(-3) * (((m.x15 - m.x30)
    **2 + (m.x94 - m.x109)**2 + (m.x173 - m.x188)**2)**(-3) - 2) + ((m.x15 -
    m.x31)**2 + (m.x94 - m.x110)**2 + (m.x173 - m.x189)**2)**(-3) * (((m.x15 -
    m.x31)**2 + (m.x94 - m.x110)**2 + (m.x173 - m.x189)**2)**(-3) - 2) + ((
    m.x15 - m.x32)**2 + (m.x94 - m.x111)**2 + (m.x173 - m.x190)**2)**(-3) * (((
    m.x15 - m.x32)**2 + (m.x94 - m.x111)**2 + (m.x173 - m.x190)**2)**(-3) - 2)
    + ((m.x15 - m.x33)**2 + (m.x94 - m.x112)**2 + (m.x173 - m.x191)**2)**(-3)
    * (((m.x15 - m.x33)**2 + (m.x94 - m.x112)**2 + (m.x173 - m.x191)**2)**(-3)
    - 2) + ((m.x15 - m.x34)**2 + (m.x94 - m.x113)**2 + (m.x173 - m.x192)**2)**
    (-3) * (((m.x15 - m.x34)**2 + (m.x94 - m.x113)**2 + (m.x173 - m.x192)**2)**
    (-3) - 2) + ((m.x15 - m.x35)**2 + (m.x94 - m.x114)**2 + (m.x173 - m.x193)**
    2)**(-3) * (((m.x15 - m.x35)**2 + (m.x94 - m.x114)**2 + (m.x173 - m.x193)**
    2)**(-3) - 2) + ((m.x15 - m.x36)**2 + (m.x94 - m.x115)**2 + (m.x173 -
    m.x194)**2)**(-3) * (((m.x15 - m.x36)**2 + (m.x94 - m.x115)**2 + (m.x173 -
    m.x194)**2)**(-3) - 2) + ((m.x15 - m.x37)**2 + (m.x94 - m.x116)**2 + (
    m.x173 - m.x195)**2)**(-3) * (((m.x15 - m.x37)**2 + (m.x94 - m.x116)**2 + (
    m.x173 - m.x195)**2)**(-3) - 2) + ((m.x15 - m.x38)**2 + (m.x94 - m.x117)**2
    + (m.x173 - m.x196)**2)**(-3) * (((m.x15 - m.x38)**2 + (m.x94 - m.x117)**2
    + (m.x173 - m.x196)**2)**(-3) - 2) + ((m.x15 - m.x39)**2 + (m.x94 - m.x118)
    **2 + (m.x173 - m.x197)**2)**(-3) * (((m.x15 - m.x39)**2 + (m.x94 - m.x118)
    **2 + (m.x173 - m.x197)**2)**(-3) - 2) + ((m.x15 - m.x40)**2 + (m.x94 -
    m.x119)**2 + (m.x173 - m.x198)**2)**(-3) * (((m.x15 - m.x40)**2 + (m.x94 -
    m.x119)**2 + (m.x173 - m.x198)**2)**(-3) - 2) + ((m.x15 - m.x41)**2 + (
    m.x94 - m.x120)**2 + (m.x173 - m.x199)**2)**(-3) * (((m.x15 - m.x41)**2 + (
    m.x94 - m.x120)**2 + (m.x173 - m.x199)**2)**(-3) - 2) + ((m.x15 - m.x42)**2
    + (m.x94 - m.x121)**2 + (m.x173 - m.x200)**2)**(-3) * (((m.x15 - m.x42)**2
    + (m.x94 - m.x121)**2 + (m.x173 - m.x200)**2)**(-3) - 2) + ((m.x15 - m.x43)
    **2 + (m.x94 - m.x122)**2 + (m.x173 - m.x201)**2)**(-3) * (((m.x15 - m.x43)
    **2 + (m.x94 - m.x122)**2 + (m.x173 - m.x201)**2)**(-3) - 2) + ((m.x15 -
    m.x44)**2 + (m.x94 - m.x123)**2 + (m.x173 - m.x202)**2)**(-3) * (((m.x15 -
    m.x44)**2 + (m.x94 - m.x123)**2 + (m.x173 - m.x202)**2)**(-3) - 2) + ((
    m.x15 - m.x45)**2 + (m.x94 - m.x124)**2 + (m.x173 - m.x203)**2)**(-3) * (((
    m.x15 - m.x45)**2 + (m.x94 - m.x124)**2 + (m.x173 - m.x203)**2)**(-3) - 2)
    + ((m.x15 - m.x46)**2 + (m.x94 - m.x125)**2 + (m.x173 - m.x204)**2)**(-3)
    * (((m.x15 - m.x46)**2 + (m.x94 - m.x125)**2 + (m.x173 - m.x204)**2)**(-3)
    - 2) + ((m.x15 - m.x47)**2 + (m.x94 - m.x126)**2 + (m.x173 - m.x205)**2)**
    (-3) * (((m.x15 - m.x47)**2 + (m.x94 - m.x126)**2 + (m.x173 - m.x205)**2)**
    (-3) - 2) + ((m.x15 - m.x48)**2 + (m.x94 - m.x127)**2 + (m.x173 - m.x206)**
    2)**(-3) * (((m.x15 - m.x48)**2 + (m.x94 - m.x127)**2 + (m.x173 - m.x206)**
    2)**(-3) - 2) + ((m.x15 - m.x49)**2 + (m.x94 - m.x128)**2 + (m.x173 -
    m.x207)**2)**(-3) * (((m.x15 - m.x49)**2 + (m.x94 - m.x128)**2 + (m.x173 -
    m.x207)**2)**(-3) - 2) + ((m.x15 - m.x50)**2 + (m.x94 - m.x129)**2 + (
    m.x173 - m.x208)**2)**(-3) * (((m.x15 - m.x50)**2 + (m.x94 - m.x129)**2 + (
    m.x173 - m.x208)**2)**(-3) - 2) + ((m.x15 - m.x51)**2 + (m.x94 - m.x130)**2
    + (m.x173 - m.x209)**2)**(-3) * (((m.x15 - m.x51)**2 + (m.x94 - m.x130)**2
    + (m.x173 - m.x209)**2)**(-3) - 2) + ((m.x15 - m.x52)**2 + (m.x94 - m.x131)
    **2 + (m.x173 - m.x210)**2)**(-3) * (((m.x15 - m.x52)**2 + (m.x94 - m.x131)
    **2 + (m.x173 - m.x210)**2)**(-3) - 2) + ((m.x15 - m.x53)**2 + (m.x94 -
    m.x132)**2 + (m.x173 - m.x211)**2)**(-3) * (((m.x15 - m.x53)**2 + (m.x94 -
    m.x132)**2 + (m.x173 - m.x211)**2)**(-3) - 2) + ((m.x15 - m.x54)**2 + (
    m.x94 - m.x133)**2 + (m.x173 - m.x212)**2)**(-3) * (((m.x15 - m.x54)**2 + (
    m.x94 - m.x133)**2 + (m.x173 - m.x212)**2)**(-3) - 2) + ((m.x15 - m.x55)**2
    + (m.x94 - m.x134)**2 + (m.x173 - m.x213)**2)**(-3) * (((m.x15 - m.x55)**2
    + (m.x94 - m.x134)**2 + (m.x173 - m.x213)**2)**(-3) - 2) + ((m.x15 - m.x56)
    **2 + (m.x94 - m.x135)**2 + (m.x173 - m.x214)**2)**(-3) * (((m.x15 - m.x56)
    **2 + (m.x94 - m.x135)**2 + (m.x173 - m.x214)**2)**(-3) - 2) + ((m.x15 -
    m.x57)**2 + (m.x94 - m.x136)**2 + (m.x173 - m.x215)**2)**(-3) * (((m.x15 -
    m.x57)**2 + (m.x94 - m.x136)**2 + (m.x173 - m.x215)**2)**(-3) - 2) + ((
    m.x15 - m.x58)**2 + (m.x94 - m.x137)**2 + (m.x173 - m.x216)**2)**(-3) * (((
    m.x15 - m.x58)**2 + (m.x94 - m.x137)**2 + (m.x173 - m.x216)**2)**(-3) - 2)
    + ((m.x15 - m.x59)**2 + (m.x94 - m.x138)**2 + (m.x173 - m.x217)**2)**(-3)
    * (((m.x15 - m.x59)**2 + (m.x94 - m.x138)**2 + (m.x173 - m.x217)**2)**(-3)
    - 2) + ((m.x15 - m.x60)**2 + (m.x94 - m.x139)**2 + (m.x173 - m.x218)**2)**
    (-3) * (((m.x15 - m.x60)**2 + (m.x94 - m.x139)**2 + (m.x173 - m.x218)**2)**
    (-3) - 2) + ((m.x15 - m.x61)**2 + (m.x94 - m.x140)**2 + (m.x173 - m.x219)**
    2)**(-3) * (((m.x15 - m.x61)**2 + (m.x94 - m.x140)**2 + (m.x173 - m.x219)**
    2)**(-3) - 2) + ((m.x15 - m.x62)**2 + (m.x94 - m.x141)**2 + (m.x173 -
    m.x220)**2)**(-3) * (((m.x15 - m.x62)**2 + (m.x94 - m.x141)**2 + (m.x173 -
    m.x220)**2)**(-3) - 2) + ((m.x15 - m.x63)**2 + (m.x94 - m.x142)**2 + (
    m.x173 - m.x221)**2)**(-3) * (((m.x15 - m.x63)**2 + (m.x94 - m.x142)**2 + (
    m.x173 - m.x221)**2)**(-3) - 2) + ((m.x15 - m.x64)**2 + (m.x94 - m.x143)**2
    + (m.x173 - m.x222)**2)**(-3) * (((m.x15 - m.x64)**2 + (m.x94 - m.x143)**2
    + (m.x173 - m.x222)**2)**(-3) - 2) + ((m.x15 - m.x65)**2 + (m.x94 - m.x144)
    **2 + (m.x173 - m.x223)**2)**(-3) * (((m.x15 - m.x65)**2 + (m.x94 - m.x144)
    **2 + (m.x173 - m.x223)**2)**(-3) - 2) + ((m.x15 - m.x66)**2 + (m.x94 -
    m.x145)**2 + (m.x173 - m.x224)**2)**(-3) * (((m.x15 - m.x66)**2 + (m.x94 -
    m.x145)**2 + (m.x173 - m.x224)**2)**(-3) - 2) + ((m.x15 - m.x67)**2 + (
    m.x94 - m.x146)**2 + (m.x173 - m.x225)**2)**(-3) * (((m.x15 - m.x67)**2 + (
    m.x94 - m.x146)**2 + (m.x173 - m.x225)**2)**(-3) - 2) + ((m.x15 - m.x68)**2
    + (m.x94 - m.x147)**2 + (m.x173 - m.x226)**2)**(-3) * (((m.x15 - m.x68)**2
    + (m.x94 - m.x147)**2 + (m.x173 - m.x226)**2)**(-3) - 2) + ((m.x15 - m.x69)
    **2 + (m.x94 - m.x148)**2 + (m.x173 - m.x227)**2)**(-3) * (((m.x15 - m.x69)
    **2 + (m.x94 - m.x148)**2 + (m.x173 - m.x227)**2)**(-3) - 2) + ((m.x15 -
    m.x70)**2 + (m.x94 - m.x149)**2 + (m.x173 - m.x228)**2)**(-3) * (((m.x15 -
    m.x70)**2 + (m.x94 - m.x149)**2 + (m.x173 - m.x228)**2)**(-3) - 2) + ((
    m.x15 - m.x71)**2 + (m.x94 - m.x150)**2 + (m.x173 - m.x229)**2)**(-3) * (((
    m.x15 - m.x71)**2 + (m.x94 - m.x150)**2 + (m.x173 - m.x229)**2)**(-3) - 2)
    + ((m.x15 - m.x72)**2 + (m.x94 - m.x151)**2 + (m.x173 - m.x230)**2)**(-3)
    * (((m.x15 - m.x72)**2 + (m.x94 - m.x151)**2 + (m.x173 - m.x230)**2)**(-3)
    - 2) + ((m.x15 - m.x73)**2 + (m.x94 - m.x152)**2 + (m.x173 - m.x231)**2)**
    (-3) * (((m.x15 - m.x73)**2 + (m.x94 - m.x152)**2 + (m.x173 - m.x231)**2)**
    (-3) - 2) + ((m.x15 - m.x74)**2 + (m.x94 - m.x153)**2 + (m.x173 - m.x232)**
    2)**(-3) * (((m.x15 - m.x74)**2 + (m.x94 - m.x153)**2 + (m.x173 - m.x232)**
    2)**(-3) - 2) + ((m.x15 - m.x75)**2 + (m.x94 - m.x154)**2 + (m.x173 -
    m.x233)**2)**(-3) * (((m.x15 - m.x75)**2 + (m.x94 - m.x154)**2 + (m.x173 -
    m.x233)**2)**(-3) - 2) + ((m.x15 - m.x76)**2 + (m.x94 - m.x155)**2 + (
    m.x173 - m.x234)**2)**(-3) * (((m.x15 - m.x76)**2 + (m.x94 - m.x155)**2 + (
    m.x173 - m.x234)**2)**(-3) - 2) + ((m.x15 - m.x77)**2 + (m.x94 - m.x156)**2
    + (m.x173 - m.x235)**2)**(-3) * (((m.x15 - m.x77)**2 + (m.x94 - m.x156)**2
    + (m.x173 - m.x235)**2)**(-3) - 2) + ((m.x15 - m.x78)**2 + (m.x94 - m.x157)
    **2 + (m.x173 - m.x236)**2)**(-3) * (((m.x15 - m.x78)**2 + (m.x94 - m.x157)
    **2 + (m.x173 - m.x236)**2)**(-3) - 2) + ((m.x15 - m.x79)**2 + (m.x94 -
    m.x158)**2 + (m.x173 - m.x237)**2)**(-3) * (((m.x15 - m.x79)**2 + (m.x94 -
    m.x158)**2 + (m.x173 - m.x237)**2)**(-3) - 2) + ((m.x16 - m.x17)**2 + (
    m.x95 - m.x96)**2 + (m.x174 - m.x175)**2)**(-3) * (((m.x16 - m.x17)**2 + (
    m.x95 - m.x96)**2 + (m.x174 - m.x175)**2)**(-3) - 2) + ((m.x16 - m.x18)**2
    + (m.x95 - m.x97)**2 + (m.x174 - m.x176)**2)**(-3) * (((m.x16 - m.x18)**2
    + (m.x95 - m.x97)**2 + (m.x174 - m.x176)**2)**(-3) - 2) + ((m.x16 - m.x19)
    **2 + (m.x95 - m.x98)**2 + (m.x174 - m.x177)**2)**(-3) * (((m.x16 - m.x19)
    **2 + (m.x95 - m.x98)**2 + (m.x174 - m.x177)**2)**(-3) - 2) + ((m.x16 -
    m.x20)**2 + (m.x95 - m.x99)**2 + (m.x174 - m.x178)**2)**(-3) * (((m.x16 -
    m.x20)**2 + (m.x95 - m.x99)**2 + (m.x174 - m.x178)**2)**(-3) - 2) + ((m.x16
    - m.x21)**2 + (m.x95 - m.x100)**2 + (m.x174 - m.x179)**2)**(-3) * (((m.x16
    - m.x21)**2 + (m.x95 - m.x100)**2 + (m.x174 - m.x179)**2)**(-3) - 2) + ((
    m.x16 - m.x22)**2 + (m.x95 - m.x101)**2 + (m.x174 - m.x180)**2)**(-3) * (((
    m.x16 - m.x22)**2 + (m.x95 - m.x101)**2 + (m.x174 - m.x180)**2)**(-3) - 2)
    + ((m.x16 - m.x23)**2 + (m.x95 - m.x102)**2 + (m.x174 - m.x181)**2)**(-3)
    * (((m.x16 - m.x23)**2 + (m.x95 - m.x102)**2 + (m.x174 - m.x181)**2)**(-3)
    - 2) + ((m.x16 - m.x24)**2 + (m.x95 - m.x103)**2 + (m.x174 - m.x182)**2)**
    (-3) * (((m.x16 - m.x24)**2 + (m.x95 - m.x103)**2 + (m.x174 - m.x182)**2)**
    (-3) - 2) + ((m.x16 - m.x25)**2 + (m.x95 - m.x104)**2 + (m.x174 - m.x183)**
    2)**(-3) * (((m.x16 - m.x25)**2 + (m.x95 - m.x104)**2 + (m.x174 - m.x183)**
    2)**(-3) - 2) + ((m.x16 - m.x26)**2 + (m.x95 - m.x105)**2 + (m.x174 -
    m.x184)**2)**(-3) * (((m.x16 - m.x26)**2 + (m.x95 - m.x105)**2 + (m.x174 -
    m.x184)**2)**(-3) - 2) + ((m.x16 - m.x27)**2 + (m.x95 - m.x106)**2 + (
    m.x174 - m.x185)**2)**(-3) * (((m.x16 - m.x27)**2 + (m.x95 - m.x106)**2 + (
    m.x174 - m.x185)**2)**(-3) - 2) + ((m.x16 - m.x28)**2 + (m.x95 - m.x107)**2
    + (m.x174 - m.x186)**2)**(-3) * (((m.x16 - m.x28)**2 + (m.x95 - m.x107)**2
    + (m.x174 - m.x186)**2)**(-3) - 2) + ((m.x16 - m.x29)**2 + (m.x95 - m.x108)
    **2 + (m.x174 - m.x187)**2)**(-3) * (((m.x16 - m.x29)**2 + (m.x95 - m.x108)
    **2 + (m.x174 - m.x187)**2)**(-3) - 2) + ((m.x16 - m.x30)**2 + (m.x95 -
    m.x109)**2 + (m.x174 - m.x188)**2)**(-3) * (((m.x16 - m.x30)**2 + (m.x95 -
    m.x109)**2 + (m.x174 - m.x188)**2)**(-3) - 2) + ((m.x16 - m.x31)**2 + (
    m.x95 - m.x110)**2 + (m.x174 - m.x189)**2)**(-3) * (((m.x16 - m.x31)**2 + (
    m.x95 - m.x110)**2 + (m.x174 - m.x189)**2)**(-3) - 2) + ((m.x16 - m.x32)**2
    + (m.x95 - m.x111)**2 + (m.x174 - m.x190)**2)**(-3) * (((m.x16 - m.x32)**2
    + (m.x95 - m.x111)**2 + (m.x174 - m.x190)**2)**(-3) - 2) + ((m.x16 - m.x33)
    **2 + (m.x95 - m.x112)**2 + (m.x174 - m.x191)**2)**(-3) * (((m.x16 - m.x33)
    **2 + (m.x95 - m.x112)**2 + (m.x174 - m.x191)**2)**(-3) - 2) + ((m.x16 -
    m.x34)**2 + (m.x95 - m.x113)**2 + (m.x174 - m.x192)**2)**(-3) * (((m.x16 -
    m.x34)**2 + (m.x95 - m.x113)**2 + (m.x174 - m.x192)**2)**(-3) - 2) + ((
    m.x16 - m.x35)**2 + (m.x95 - m.x114)**2 + (m.x174 - m.x193)**2)**(-3) * (((
    m.x16 - m.x35)**2 + (m.x95 - m.x114)**2 + (m.x174 - m.x193)**2)**(-3) - 2)
    + ((m.x16 - m.x36)**2 + (m.x95 - m.x115)**2 + (m.x174 - m.x194)**2)**(-3)
    * (((m.x16 - m.x36)**2 + (m.x95 - m.x115)**2 + (m.x174 - m.x194)**2)**(-3)
    - 2) + ((m.x16 - m.x37)**2 + (m.x95 - m.x116)**2 + (m.x174 - m.x195)**2)**
    (-3) * (((m.x16 - m.x37)**2 + (m.x95 - m.x116)**2 + (m.x174 - m.x195)**2)**
    (-3) - 2) + ((m.x16 - m.x38)**2 + (m.x95 - m.x117)**2 + (m.x174 - m.x196)**
    2)**(-3) * (((m.x16 - m.x38)**2 + (m.x95 - m.x117)**2 + (m.x174 - m.x196)**
    2)**(-3) - 2) + ((m.x16 - m.x39)**2 + (m.x95 - m.x118)**2 + (m.x174 -
    m.x197)**2)**(-3) * (((m.x16 - m.x39)**2 + (m.x95 - m.x118)**2 + (m.x174 -
    m.x197)**2)**(-3) - 2) + ((m.x16 - m.x40)**2 + (m.x95 - m.x119)**2 + (
    m.x174 - m.x198)**2)**(-3) * (((m.x16 - m.x40)**2 + (m.x95 - m.x119)**2 + (
    m.x174 - m.x198)**2)**(-3) - 2) + ((m.x16 - m.x41)**2 + (m.x95 - m.x120)**2
    + (m.x174 - m.x199)**2)**(-3) * (((m.x16 - m.x41)**2 + (m.x95 - m.x120)**2
    + (m.x174 - m.x199)**2)**(-3) - 2) + ((m.x16 - m.x42)**2 + (m.x95 - m.x121)
    **2 + (m.x174 - m.x200)**2)**(-3) * (((m.x16 - m.x42)**2 + (m.x95 - m.x121)
    **2 + (m.x174 - m.x200)**2)**(-3) - 2) + ((m.x16 - m.x43)**2 + (m.x95 -
    m.x122)**2 + (m.x174 - m.x201)**2)**(-3) * (((m.x16 - m.x43)**2 + (m.x95 -
    m.x122)**2 + (m.x174 - m.x201)**2)**(-3) - 2) + ((m.x16 - m.x44)**2 + (
    m.x95 - m.x123)**2 + (m.x174 - m.x202)**2)**(-3) * (((m.x16 - m.x44)**2 + (
    m.x95 - m.x123)**2 + (m.x174 - m.x202)**2)**(-3) - 2) + ((m.x16 - m.x45)**2
    + (m.x95 - m.x124)**2 + (m.x174 - m.x203)**2)**(-3) * (((m.x16 - m.x45)**2
    + (m.x95 - m.x124)**2 + (m.x174 - m.x203)**2)**(-3) - 2) + ((m.x16 - m.x46)
    **2 + (m.x95 - m.x125)**2 + (m.x174 - m.x204)**2)**(-3) * (((m.x16 - m.x46)
    **2 + (m.x95 - m.x125)**2 + (m.x174 - m.x204)**2)**(-3) - 2) + ((m.x16 -
    m.x47)**2 + (m.x95 - m.x126)**2 + (m.x174 - m.x205)**2)**(-3) * (((m.x16 -
    m.x47)**2 + (m.x95 - m.x126)**2 + (m.x174 - m.x205)**2)**(-3) - 2) + ((
    m.x16 - m.x48)**2 + (m.x95 - m.x127)**2 + (m.x174 - m.x206)**2)**(-3) * (((
    m.x16 - m.x48)**2 + (m.x95 - m.x127)**2 + (m.x174 - m.x206)**2)**(-3) - 2)
    + ((m.x16 - m.x49)**2 + (m.x95 - m.x128)**2 + (m.x174 - m.x207)**2)**(-3)
    * (((m.x16 - m.x49)**2 + (m.x95 - m.x128)**2 + (m.x174 - m.x207)**2)**(-3)
    - 2) + ((m.x16 - m.x50)**2 + (m.x95 - m.x129)**2 + (m.x174 - m.x208)**2)**
    (-3) * (((m.x16 - m.x50)**2 + (m.x95 - m.x129)**2 + (m.x174 - m.x208)**2)**
    (-3) - 2) + ((m.x16 - m.x51)**2 + (m.x95 - m.x130)**2 + (m.x174 - m.x209)**
    2)**(-3) * (((m.x16 - m.x51)**2 + (m.x95 - m.x130)**2 + (m.x174 - m.x209)**
    2)**(-3) - 2) + ((m.x16 - m.x52)**2 + (m.x95 - m.x131)**2 + (m.x174 -
    m.x210)**2)**(-3) * (((m.x16 - m.x52)**2 + (m.x95 - m.x131)**2 + (m.x174 -
    m.x210)**2)**(-3) - 2) + ((m.x16 - m.x53)**2 + (m.x95 - m.x132)**2 + (
    m.x174 - m.x211)**2)**(-3) * (((m.x16 - m.x53)**2 + (m.x95 - m.x132)**2 + (
    m.x174 - m.x211)**2)**(-3) - 2) + ((m.x16 - m.x54)**2 + (m.x95 - m.x133)**2
    + (m.x174 - m.x212)**2)**(-3) * (((m.x16 - m.x54)**2 + (m.x95 - m.x133)**2
    + (m.x174 - m.x212)**2)**(-3) - 2) + ((m.x16 - m.x55)**2 + (m.x95 - m.x134)
    **2 + (m.x174 - m.x213)**2)**(-3) * (((m.x16 - m.x55)**2 + (m.x95 - m.x134)
    **2 + (m.x174 - m.x213)**2)**(-3) - 2) + ((m.x16 - m.x56)**2 + (m.x95 -
    m.x135)**2 + (m.x174 - m.x214)**2)**(-3) * (((m.x16 - m.x56)**2 + (m.x95 -
    m.x135)**2 + (m.x174 - m.x214)**2)**(-3) - 2) + ((m.x16 - m.x57)**2 + (
    m.x95 - m.x136)**2 + (m.x174 - m.x215)**2)**(-3) * (((m.x16 - m.x57)**2 + (
    m.x95 - m.x136)**2 + (m.x174 - m.x215)**2)**(-3) - 2) + ((m.x16 - m.x58)**2
    + (m.x95 - m.x137)**2 + (m.x174 - m.x216)**2)**(-3) * (((m.x16 - m.x58)**2
    + (m.x95 - m.x137)**2 + (m.x174 - m.x216)**2)**(-3) - 2) + ((m.x16 - m.x59)
    **2 + (m.x95 - m.x138)**2 + (m.x174 - m.x217)**2)**(-3) * (((m.x16 - m.x59)
    **2 + (m.x95 - m.x138)**2 + (m.x174 - m.x217)**2)**(-3) - 2) + ((m.x16 -
    m.x60)**2 + (m.x95 - m.x139)**2 + (m.x174 - m.x218)**2)**(-3) * (((m.x16 -
    m.x60)**2 + (m.x95 - m.x139)**2 + (m.x174 - m.x218)**2)**(-3) - 2) + ((
    m.x16 - m.x61)**2 + (m.x95 - m.x140)**2 + (m.x174 - m.x219)**2)**(-3) * (((
    m.x16 - m.x61)**2 + (m.x95 - m.x140)**2 + (m.x174 - m.x219)**2)**(-3) - 2)
    + ((m.x16 - m.x62)**2 + (m.x95 - m.x141)**2 + (m.x174 - m.x220)**2)**(-3)
    * (((m.x16 - m.x62)**2 + (m.x95 - m.x141)**2 + (m.x174 - m.x220)**2)**(-3)
    - 2) + ((m.x16 - m.x63)**2 + (m.x95 - m.x142)**2 + (m.x174 - m.x221)**2)**
    (-3) * (((m.x16 - m.x63)**2 + (m.x95 - m.x142)**2 + (m.x174 - m.x221)**2)**
    (-3) - 2) + ((m.x16 - m.x64)**2 + (m.x95 - m.x143)**2 + (m.x174 - m.x222)**
    2)**(-3) * (((m.x16 - m.x64)**2 + (m.x95 - m.x143)**2 + (m.x174 - m.x222)**
    2)**(-3) - 2) + ((m.x16 - m.x65)**2 + (m.x95 - m.x144)**2 + (m.x174 -
    m.x223)**2)**(-3) * (((m.x16 - m.x65)**2 + (m.x95 - m.x144)**2 + (m.x174 -
    m.x223)**2)**(-3) - 2) + ((m.x16 - m.x66)**2 + (m.x95 - m.x145)**2 + (
    m.x174 - m.x224)**2)**(-3) * (((m.x16 - m.x66)**2 + (m.x95 - m.x145)**2 + (
    m.x174 - m.x224)**2)**(-3) - 2) + ((m.x16 - m.x67)**2 + (m.x95 - m.x146)**2
    + (m.x174 - m.x225)**2)**(-3) * (((m.x16 - m.x67)**2 + (m.x95 - m.x146)**2
    + (m.x174 - m.x225)**2)**(-3) - 2) + ((m.x16 - m.x68)**2 + (m.x95 - m.x147)
    **2 + (m.x174 - m.x226)**2)**(-3) * (((m.x16 - m.x68)**2 + (m.x95 - m.x147)
    **2 + (m.x174 - m.x226)**2)**(-3) - 2) + ((m.x16 - m.x69)**2 + (m.x95 -
    m.x148)**2 + (m.x174 - m.x227)**2)**(-3) * (((m.x16 - m.x69)**2 + (m.x95 -
    m.x148)**2 + (m.x174 - m.x227)**2)**(-3) - 2) + ((m.x16 - m.x70)**2 + (
    m.x95 - m.x149)**2 + (m.x174 - m.x228)**2)**(-3) * (((m.x16 - m.x70)**2 + (
    m.x95 - m.x149)**2 + (m.x174 - m.x228)**2)**(-3) - 2) + ((m.x16 - m.x71)**2
    + (m.x95 - m.x150)**2 + (m.x174 - m.x229)**2)**(-3) * (((m.x16 - m.x71)**2
    + (m.x95 - m.x150)**2 + (m.x174 - m.x229)**2)**(-3) - 2) + ((m.x16 - m.x72)
    **2 + (m.x95 - m.x151)**2 + (m.x174 - m.x230)**2)**(-3) * (((m.x16 - m.x72)
    **2 + (m.x95 - m.x151)**2 + (m.x174 - m.x230)**2)**(-3) - 2) + ((m.x16 -
    m.x73)**2 + (m.x95 - m.x152)**2 + (m.x174 - m.x231)**2)**(-3) * (((m.x16 -
    m.x73)**2 + (m.x95 - m.x152)**2 + (m.x174 - m.x231)**2)**(-3) - 2) + ((
    m.x16 - m.x74)**2 + (m.x95 - m.x153)**2 + (m.x174 - m.x232)**2)**(-3) * (((
    m.x16 - m.x74)**2 + (m.x95 - m.x153)**2 + (m.x174 - m.x232)**2)**(-3) - 2)
    + ((m.x16 - m.x75)**2 + (m.x95 - m.x154)**2 + (m.x174 - m.x233)**2)**(-3)
    * (((m.x16 - m.x75)**2 + (m.x95 - m.x154)**2 + (m.x174 - m.x233)**2)**(-3)
    - 2) + ((m.x16 - m.x76)**2 + (m.x95 - m.x155)**2 + (m.x174 - m.x234)**2)**
    (-3) * (((m.x16 - m.x76)**2 + (m.x95 - m.x155)**2 + (m.x174 - m.x234)**2)**
    (-3) - 2) + ((m.x16 - m.x77)**2 + (m.x95 - m.x156)**2 + (m.x174 - m.x235)**
    2)**(-3) * (((m.x16 - m.x77)**2 + (m.x95 - m.x156)**2 + (m.x174 - m.x235)**
    2)**(-3) - 2) + ((m.x16 - m.x78)**2 + (m.x95 - m.x157)**2 + (m.x174 -
    m.x236)**2)**(-3) * (((m.x16 - m.x78)**2 + (m.x95 - m.x157)**2 + (m.x174 -
    m.x236)**2)**(-3) - 2) + ((m.x16 - m.x79)**2 + (m.x95 - m.x158)**2 + (
    m.x174 - m.x237)**2)**(-3) * (((m.x16 - m.x79)**2 + (m.x95 - m.x158)**2 + (
    m.x174 - m.x237)**2)**(-3) - 2) + ((m.x17 - m.x18)**2 + (m.x96 - m.x97)**2
    + (m.x175 - m.x176)**2)**(-3) * (((m.x17 - m.x18)**2 + (m.x96 - m.x97)**2
    + (m.x175 - m.x176)**2)**(-3) - 2) + ((m.x17 - m.x19)**2 + (m.x96 - m.x98)
    **2 + (m.x175 - m.x177)**2)**(-3) * (((m.x17 - m.x19)**2 + (m.x96 - m.x98)
    **2 + (m.x175 - m.x177)**2)**(-3) - 2) + ((m.x17 - m.x20)**2 + (m.x96 -
    m.x99)**2 + (m.x175 - m.x178)**2)**(-3) * (((m.x17 - m.x20)**2 + (m.x96 -
    m.x99)**2 + (m.x175 - m.x178)**2)**(-3) - 2) + ((m.x17 - m.x21)**2 + (m.x96
    - m.x100)**2 + (m.x175 - m.x179)**2)**(-3) * (((m.x17 - m.x21)**2 + (m.x96
    - m.x100)**2 + (m.x175 - m.x179)**2)**(-3) - 2) + ((m.x17 - m.x22)**2 + (
    m.x96 - m.x101)**2 + (m.x175 - m.x180)**2)**(-3) * (((m.x17 - m.x22)**2 + (
    m.x96 - m.x101)**2 + (m.x175 - m.x180)**2)**(-3) - 2) + ((m.x17 - m.x23)**2
    + (m.x96 - m.x102)**2 + (m.x175 - m.x181)**2)**(-3) * (((m.x17 - m.x23)**2
    + (m.x96 - m.x102)**2 + (m.x175 - m.x181)**2)**(-3) - 2) + ((m.x17 - m.x24)
    **2 + (m.x96 - m.x103)**2 + (m.x175 - m.x182)**2)**(-3) * (((m.x17 - m.x24)
    **2 + (m.x96 - m.x103)**2 + (m.x175 - m.x182)**2)**(-3) - 2) + ((m.x17 -
    m.x25)**2 + (m.x96 - m.x104)**2 + (m.x175 - m.x183)**2)**(-3) * (((m.x17 -
    m.x25)**2 + (m.x96 - m.x104)**2 + (m.x175 - m.x183)**2)**(-3) - 2) + ((
    m.x17 - m.x26)**2 + (m.x96 - m.x105)**2 + (m.x175 - m.x184)**2)**(-3) * (((
    m.x17 - m.x26)**2 + (m.x96 - m.x105)**2 + (m.x175 - m.x184)**2)**(-3) - 2)
    + ((m.x17 - m.x27)**2 + (m.x96 - m.x106)**2 + (m.x175 - m.x185)**2)**(-3)
    * (((m.x17 - m.x27)**2 + (m.x96 - m.x106)**2 + (m.x175 - m.x185)**2)**(-3)
    - 2) + ((m.x17 - m.x28)**2 + (m.x96 - m.x107)**2 + (m.x175 - m.x186)**2)**
    (-3) * (((m.x17 - m.x28)**2 + (m.x96 - m.x107)**2 + (m.x175 - m.x186)**2)**
    (-3) - 2) + ((m.x17 - m.x29)**2 + (m.x96 - m.x108)**2 + (m.x175 - m.x187)**
    2)**(-3) * (((m.x17 - m.x29)**2 + (m.x96 - m.x108)**2 + (m.x175 - m.x187)**
    2)**(-3) - 2) + ((m.x17 - m.x30)**2 + (m.x96 - m.x109)**2 + (m.x175 -
    m.x188)**2)**(-3) * (((m.x17 - m.x30)**2 + (m.x96 - m.x109)**2 + (m.x175 -
    m.x188)**2)**(-3) - 2) + ((m.x17 - m.x31)**2 + (m.x96 - m.x110)**2 + (
    m.x175 - m.x189)**2)**(-3) * (((m.x17 - m.x31)**2 + (m.x96 - m.x110)**2 + (
    m.x175 - m.x189)**2)**(-3) - 2) + ((m.x17 - m.x32)**2 + (m.x96 - m.x111)**2
    + (m.x175 - m.x190)**2)**(-3) * (((m.x17 - m.x32)**2 + (m.x96 - m.x111)**2
    + (m.x175 - m.x190)**2)**(-3) - 2) + ((m.x17 - m.x33)**2 + (m.x96 - m.x112)
    **2 + (m.x175 - m.x191)**2)**(-3) * (((m.x17 - m.x33)**2 + (m.x96 - m.x112)
    **2 + (m.x175 - m.x191)**2)**(-3) - 2) + ((m.x17 - m.x34)**2 + (m.x96 -
    m.x113)**2 + (m.x175 - m.x192)**2)**(-3) * (((m.x17 - m.x34)**2 + (m.x96 -
    m.x113)**2 + (m.x175 - m.x192)**2)**(-3) - 2) + ((m.x17 - m.x35)**2 + (
    m.x96 - m.x114)**2 + (m.x175 - m.x193)**2)**(-3) * (((m.x17 - m.x35)**2 + (
    m.x96 - m.x114)**2 + (m.x175 - m.x193)**2)**(-3) - 2) + ((m.x17 - m.x36)**2
    + (m.x96 - m.x115)**2 + (m.x175 - m.x194)**2)**(-3) * (((m.x17 - m.x36)**2
    + (m.x96 - m.x115)**2 + (m.x175 - m.x194)**2)**(-3) - 2) + ((m.x17 - m.x37)
    **2 + (m.x96 - m.x116)**2 + (m.x175 - m.x195)**2)**(-3) * (((m.x17 - m.x37)
    **2 + (m.x96 - m.x116)**2 + (m.x175 - m.x195)**2)**(-3) - 2) + ((m.x17 -
    m.x38)**2 + (m.x96 - m.x117)**2 + (m.x175 - m.x196)**2)**(-3) * (((m.x17 -
    m.x38)**2 + (m.x96 - m.x117)**2 + (m.x175 - m.x196)**2)**(-3) - 2) + ((
    m.x17 - m.x39)**2 + (m.x96 - m.x118)**2 + (m.x175 - m.x197)**2)**(-3) * (((
    m.x17 - m.x39)**2 + (m.x96 - m.x118)**2 + (m.x175 - m.x197)**2)**(-3) - 2)
    + ((m.x17 - m.x40)**2 + (m.x96 - m.x119)**2 + (m.x175 - m.x198)**2)**(-3)
    * (((m.x17 - m.x40)**2 + (m.x96 - m.x119)**2 + (m.x175 - m.x198)**2)**(-3)
    - 2) + ((m.x17 - m.x41)**2 + (m.x96 - m.x120)**2 + (m.x175 - m.x199)**2)**
    (-3) * (((m.x17 - m.x41)**2 + (m.x96 - m.x120)**2 + (m.x175 - m.x199)**2)**
    (-3) - 2) + ((m.x17 - m.x42)**2 + (m.x96 - m.x121)**2 + (m.x175 - m.x200)**
    2)**(-3) * (((m.x17 - m.x42)**2 + (m.x96 - m.x121)**2 + (m.x175 - m.x200)**
    2)**(-3) - 2) + ((m.x17 - m.x43)**2 + (m.x96 - m.x122)**2 + (m.x175 -
    m.x201)**2)**(-3) * (((m.x17 - m.x43)**2 + (m.x96 - m.x122)**2 + (m.x175 -
    m.x201)**2)**(-3) - 2) + ((m.x17 - m.x44)**2 + (m.x96 - m.x123)**2 + (
    m.x175 - m.x202)**2)**(-3) * (((m.x17 - m.x44)**2 + (m.x96 - m.x123)**2 + (
    m.x175 - m.x202)**2)**(-3) - 2) + ((m.x17 - m.x45)**2 + (m.x96 - m.x124)**2
    + (m.x175 - m.x203)**2)**(-3) * (((m.x17 - m.x45)**2 + (m.x96 - m.x124)**2
    + (m.x175 - m.x203)**2)**(-3) - 2) + ((m.x17 - m.x46)**2 + (m.x96 - m.x125)
    **2 + (m.x175 - m.x204)**2)**(-3) * (((m.x17 - m.x46)**2 + (m.x96 - m.x125)
    **2 + (m.x175 - m.x204)**2)**(-3) - 2) + ((m.x17 - m.x47)**2 + (m.x96 -
    m.x126)**2 + (m.x175 - m.x205)**2)**(-3) * (((m.x17 - m.x47)**2 + (m.x96 -
    m.x126)**2 + (m.x175 - m.x205)**2)**(-3) - 2) + ((m.x17 - m.x48)**2 + (
    m.x96 - m.x127)**2 + (m.x175 - m.x206)**2)**(-3) * (((m.x17 - m.x48)**2 + (
    m.x96 - m.x127)**2 + (m.x175 - m.x206)**2)**(-3) - 2) + ((m.x17 - m.x49)**2
    + (m.x96 - m.x128)**2 + (m.x175 - m.x207)**2)**(-3) * (((m.x17 - m.x49)**2
    + (m.x96 - m.x128)**2 + (m.x175 - m.x207)**2)**(-3) - 2) + ((m.x17 - m.x50)
    **2 + (m.x96 - m.x129)**2 + (m.x175 - m.x208)**2)**(-3) * (((m.x17 - m.x50)
    **2 + (m.x96 - m.x129)**2 + (m.x175 - m.x208)**2)**(-3) - 2) + ((m.x17 -
    m.x51)**2 + (m.x96 - m.x130)**2 + (m.x175 - m.x209)**2)**(-3) * (((m.x17 -
    m.x51)**2 + (m.x96 - m.x130)**2 + (m.x175 - m.x209)**2)**(-3) - 2) + ((
    m.x17 - m.x52)**2 + (m.x96 - m.x131)**2 + (m.x175 - m.x210)**2)**(-3) * (((
    m.x17 - m.x52)**2 + (m.x96 - m.x131)**2 + (m.x175 - m.x210)**2)**(-3) - 2)
    + ((m.x17 - m.x53)**2 + (m.x96 - m.x132)**2 + (m.x175 - m.x211)**2)**(-3)
    * (((m.x17 - m.x53)**2 + (m.x96 - m.x132)**2 + (m.x175 - m.x211)**2)**(-3)
    - 2) + ((m.x17 - m.x54)**2 + (m.x96 - m.x133)**2 + (m.x175 - m.x212)**2)**
    (-3) * (((m.x17 - m.x54)**2 + (m.x96 - m.x133)**2 + (m.x175 - m.x212)**2)**
    (-3) - 2) + ((m.x17 - m.x55)**2 + (m.x96 - m.x134)**2 + (m.x175 - m.x213)**
    2)**(-3) * (((m.x17 - m.x55)**2 + (m.x96 - m.x134)**2 + (m.x175 - m.x213)**
    2)**(-3) - 2) + ((m.x17 - m.x56)**2 + (m.x96 - m.x135)**2 + (m.x175 -
    m.x214)**2)**(-3) * (((m.x17 - m.x56)**2 + (m.x96 - m.x135)**2 + (m.x175 -
    m.x214)**2)**(-3) - 2) + ((m.x17 - m.x57)**2 + (m.x96 - m.x136)**2 + (
    m.x175 - m.x215)**2)**(-3) * (((m.x17 - m.x57)**2 + (m.x96 - m.x136)**2 + (
    m.x175 - m.x215)**2)**(-3) - 2) + ((m.x17 - m.x58)**2 + (m.x96 - m.x137)**2
    + (m.x175 - m.x216)**2)**(-3) * (((m.x17 - m.x58)**2 + (m.x96 - m.x137)**2
    + (m.x175 - m.x216)**2)**(-3) - 2) + ((m.x17 - m.x59)**2 + (m.x96 - m.x138)
    **2 + (m.x175 - m.x217)**2)**(-3) * (((m.x17 - m.x59)**2 + (m.x96 - m.x138)
    **2 + (m.x175 - m.x217)**2)**(-3) - 2) + ((m.x17 - m.x60)**2 + (m.x96 -
    m.x139)**2 + (m.x175 - m.x218)**2)**(-3) * (((m.x17 - m.x60)**2 + (m.x96 -
    m.x139)**2 + (m.x175 - m.x218)**2)**(-3) - 2) + ((m.x17 - m.x61)**2 + (
    m.x96 - m.x140)**2 + (m.x175 - m.x219)**2)**(-3) * (((m.x17 - m.x61)**2 + (
    m.x96 - m.x140)**2 + (m.x175 - m.x219)**2)**(-3) - 2) + ((m.x17 - m.x62)**2
    + (m.x96 - m.x141)**2 + (m.x175 - m.x220)**2)**(-3) * (((m.x17 - m.x62)**2
    + (m.x96 - m.x141)**2 + (m.x175 - m.x220)**2)**(-3) - 2) + ((m.x17 - m.x63)
    **2 + (m.x96 - m.x142)**2 + (m.x175 - m.x221)**2)**(-3) * (((m.x17 - m.x63)
    **2 + (m.x96 - m.x142)**2 + (m.x175 - m.x221)**2)**(-3) - 2) + ((m.x17 -
    m.x64)**2 + (m.x96 - m.x143)**2 + (m.x175 - m.x222)**2)**(-3) * (((m.x17 -
    m.x64)**2 + (m.x96 - m.x143)**2 + (m.x175 - m.x222)**2)**(-3) - 2) + ((
    m.x17 - m.x65)**2 + (m.x96 - m.x144)**2 + (m.x175 - m.x223)**2)**(-3) * (((
    m.x17 - m.x65)**2 + (m.x96 - m.x144)**2 + (m.x175 - m.x223)**2)**(-3) - 2)
    + ((m.x17 - m.x66)**2 + (m.x96 - m.x145)**2 + (m.x175 - m.x224)**2)**(-3)
    * (((m.x17 - m.x66)**2 + (m.x96 - m.x145)**2 + (m.x175 - m.x224)**2)**(-3)
    - 2) + ((m.x17 - m.x67)**2 + (m.x96 - m.x146)**2 + (m.x175 - m.x225)**2)**
    (-3) * (((m.x17 - m.x67)**2 + (m.x96 - m.x146)**2 + (m.x175 - m.x225)**2)**
    (-3) - 2) + ((m.x17 - m.x68)**2 + (m.x96 - m.x147)**2 + (m.x175 - m.x226)**
    2)**(-3) * (((m.x17 - m.x68)**2 + (m.x96 - m.x147)**2 + (m.x175 - m.x226)**
    2)**(-3) - 2) + ((m.x17 - m.x69)**2 + (m.x96 - m.x148)**2 + (m.x175 -
    m.x227)**2)**(-3) * (((m.x17 - m.x69)**2 + (m.x96 - m.x148)**2 + (m.x175 -
    m.x227)**2)**(-3) - 2) + ((m.x17 - m.x70)**2 + (m.x96 - m.x149)**2 + (
    m.x175 - m.x228)**2)**(-3) * (((m.x17 - m.x70)**2 + (m.x96 - m.x149)**2 + (
    m.x175 - m.x228)**2)**(-3) - 2) + ((m.x17 - m.x71)**2 + (m.x96 - m.x150)**2
    + (m.x175 - m.x229)**2)**(-3) * (((m.x17 - m.x71)**2 + (m.x96 - m.x150)**2
    + (m.x175 - m.x229)**2)**(-3) - 2) + ((m.x17 - m.x72)**2 + (m.x96 - m.x151)
    **2 + (m.x175 - m.x230)**2)**(-3) * (((m.x17 - m.x72)**2 + (m.x96 - m.x151)
    **2 + (m.x175 - m.x230)**2)**(-3) - 2) + ((m.x17 - m.x73)**2 + (m.x96 -
    m.x152)**2 + (m.x175 - m.x231)**2)**(-3) * (((m.x17 - m.x73)**2 + (m.x96 -
    m.x152)**2 + (m.x175 - m.x231)**2)**(-3) - 2) + ((m.x17 - m.x74)**2 + (
    m.x96 - m.x153)**2 + (m.x175 - m.x232)**2)**(-3) * (((m.x17 - m.x74)**2 + (
    m.x96 - m.x153)**2 + (m.x175 - m.x232)**2)**(-3) - 2) + ((m.x17 - m.x75)**2
    + (m.x96 - m.x154)**2 + (m.x175 - m.x233)**2)**(-3) * (((m.x17 - m.x75)**2
    + (m.x96 - m.x154)**2 + (m.x175 - m.x233)**2)**(-3) - 2) + ((m.x17 - m.x76)
    **2 + (m.x96 - m.x155)**2 + (m.x175 - m.x234)**2)**(-3) * (((m.x17 - m.x76)
    **2 + (m.x96 - m.x155)**2 + (m.x175 - m.x234)**2)**(-3) - 2) + ((m.x17 -
    m.x77)**2 + (m.x96 - m.x156)**2 + (m.x175 - m.x235)**2)**(-3) * (((m.x17 -
    m.x77)**2 + (m.x96 - m.x156)**2 + (m.x175 - m.x235)**2)**(-3) - 2) + ((
    m.x17 - m.x78)**2 + (m.x96 - m.x157)**2 + (m.x175 - m.x236)**2)**(-3) * (((
    m.x17 - m.x78)**2 + (m.x96 - m.x157)**2 + (m.x175 - m.x236)**2)**(-3) - 2)
    + ((m.x17 - m.x79)**2 + (m.x96 - m.x158)**2 + (m.x175 - m.x237)**2)**(-3)
    * (((m.x17 - m.x79)**2 + (m.x96 - m.x158)**2 + (m.x175 - m.x237)**2)**(-3)
    - 2) + ((m.x18 - m.x19)**2 + (m.x97 - m.x98)**2 + (m.x176 - m.x177)**2)**(
    -3) * (((m.x18 - m.x19)**2 + (m.x97 - m.x98)**2 + (m.x176 - m.x177)**2)**(
    -3) - 2) + ((m.x18 - m.x20)**2 + (m.x97 - m.x99)**2 + (m.x176 - m.x178)**2)
    **(-3) * (((m.x18 - m.x20)**2 + (m.x97 - m.x99)**2 + (m.x176 - m.x178)**2)
    **(-3) - 2) + ((m.x18 - m.x21)**2 + (m.x97 - m.x100)**2 + (m.x176 - m.x179)
    **2)**(-3) * (((m.x18 - m.x21)**2 + (m.x97 - m.x100)**2 + (m.x176 - m.x179)
    **2)**(-3) - 2) + ((m.x18 - m.x22)**2 + (m.x97 - m.x101)**2 + (m.x176 -
    m.x180)**2)**(-3) * (((m.x18 - m.x22)**2 + (m.x97 - m.x101)**2 + (m.x176 -
    m.x180)**2)**(-3) - 2) + ((m.x18 - m.x23)**2 + (m.x97 - m.x102)**2 + (
    m.x176 - m.x181)**2)**(-3) * (((m.x18 - m.x23)**2 + (m.x97 - m.x102)**2 + (
    m.x176 - m.x181)**2)**(-3) - 2) + ((m.x18 - m.x24)**2 + (m.x97 - m.x103)**2
    + (m.x176 - m.x182)**2)**(-3) * (((m.x18 - m.x24)**2 + (m.x97 - m.x103)**2
    + (m.x176 - m.x182)**2)**(-3) - 2) + ((m.x18 - m.x25)**2 + (m.x97 - m.x104)
    **2 + (m.x176 - m.x183)**2)**(-3) * (((m.x18 - m.x25)**2 + (m.x97 - m.x104)
    **2 + (m.x176 - m.x183)**2)**(-3) - 2) + ((m.x18 - m.x26)**2 + (m.x97 -
    m.x105)**2 + (m.x176 - m.x184)**2)**(-3) * (((m.x18 - m.x26)**2 + (m.x97 -
    m.x105)**2 + (m.x176 - m.x184)**2)**(-3) - 2) + ((m.x18 - m.x27)**2 + (
    m.x97 - m.x106)**2 + (m.x176 - m.x185)**2)**(-3) * (((m.x18 - m.x27)**2 + (
    m.x97 - m.x106)**2 + (m.x176 - m.x185)**2)**(-3) - 2) + ((m.x18 - m.x28)**2
    + (m.x97 - m.x107)**2 + (m.x176 - m.x186)**2)**(-3) * (((m.x18 - m.x28)**2
    + (m.x97 - m.x107)**2 + (m.x176 - m.x186)**2)**(-3) - 2) + ((m.x18 - m.x29)
    **2 + (m.x97 - m.x108)**2 + (m.x176 - m.x187)**2)**(-3) * (((m.x18 - m.x29)
    **2 + (m.x97 - m.x108)**2 + (m.x176 - m.x187)**2)**(-3) - 2) + ((m.x18 -
    m.x30)**2 + (m.x97 - m.x109)**2 + (m.x176 - m.x188)**2)**(-3) * (((m.x18 -
    m.x30)**2 + (m.x97 - m.x109)**2 + (m.x176 - m.x188)**2)**(-3) - 2) + ((
    m.x18 - m.x31)**2 + (m.x97 - m.x110)**2 + (m.x176 - m.x189)**2)**(-3) * (((
    m.x18 - m.x31)**2 + (m.x97 - m.x110)**2 + (m.x176 - m.x189)**2)**(-3) - 2)
    + ((m.x18 - m.x32)**2 + (m.x97 - m.x111)**2 + (m.x176 - m.x190)**2)**(-3)
    * (((m.x18 - m.x32)**2 + (m.x97 - m.x111)**2 + (m.x176 - m.x190)**2)**(-3)
    - 2) + ((m.x18 - m.x33)**2 + (m.x97 - m.x112)**2 + (m.x176 - m.x191)**2)**
    (-3) * (((m.x18 - m.x33)**2 + (m.x97 - m.x112)**2 + (m.x176 - m.x191)**2)**
    (-3) - 2) + ((m.x18 - m.x34)**2 + (m.x97 - m.x113)**2 + (m.x176 - m.x192)**
    2)**(-3) * (((m.x18 - m.x34)**2 + (m.x97 - m.x113)**2 + (m.x176 - m.x192)**
    2)**(-3) - 2) + ((m.x18 - m.x35)**2 + (m.x97 - m.x114)**2 + (m.x176 -
    m.x193)**2)**(-3) * (((m.x18 - m.x35)**2 + (m.x97 - m.x114)**2 + (m.x176 -
    m.x193)**2)**(-3) - 2) + ((m.x18 - m.x36)**2 + (m.x97 - m.x115)**2 + (
    m.x176 - m.x194)**2)**(-3) * (((m.x18 - m.x36)**2 + (m.x97 - m.x115)**2 + (
    m.x176 - m.x194)**2)**(-3) - 2) + ((m.x18 - m.x37)**2 + (m.x97 - m.x116)**2
    + (m.x176 - m.x195)**2)**(-3) * (((m.x18 - m.x37)**2 + (m.x97 - m.x116)**2
    + (m.x176 - m.x195)**2)**(-3) - 2) + ((m.x18 - m.x38)**2 + (m.x97 - m.x117)
    **2 + (m.x176 - m.x196)**2)**(-3) * (((m.x18 - m.x38)**2 + (m.x97 - m.x117)
    **2 + (m.x176 - m.x196)**2)**(-3) - 2) + ((m.x18 - m.x39)**2 + (m.x97 -
    m.x118)**2 + (m.x176 - m.x197)**2)**(-3) * (((m.x18 - m.x39)**2 + (m.x97 -
    m.x118)**2 + (m.x176 - m.x197)**2)**(-3) - 2) + ((m.x18 - m.x40)**2 + (
    m.x97 - m.x119)**2 + (m.x176 - m.x198)**2)**(-3) * (((m.x18 - m.x40)**2 + (
    m.x97 - m.x119)**2 + (m.x176 - m.x198)**2)**(-3) - 2) + ((m.x18 - m.x41)**2
    + (m.x97 - m.x120)**2 + (m.x176 - m.x199)**2)**(-3) * (((m.x18 - m.x41)**2
    + (m.x97 - m.x120)**2 + (m.x176 - m.x199)**2)**(-3) - 2) + ((m.x18 - m.x42)
    **2 + (m.x97 - m.x121)**2 + (m.x176 - m.x200)**2)**(-3) * (((m.x18 - m.x42)
    **2 + (m.x97 - m.x121)**2 + (m.x176 - m.x200)**2)**(-3) - 2) + ((m.x18 -
    m.x43)**2 + (m.x97 - m.x122)**2 + (m.x176 - m.x201)**2)**(-3) * (((m.x18 -
    m.x43)**2 + (m.x97 - m.x122)**2 + (m.x176 - m.x201)**2)**(-3) - 2) + ((
    m.x18 - m.x44)**2 + (m.x97 - m.x123)**2 + (m.x176 - m.x202)**2)**(-3) * (((
    m.x18 - m.x44)**2 + (m.x97 - m.x123)**2 + (m.x176 - m.x202)**2)**(-3) - 2)
    + ((m.x18 - m.x45)**2 + (m.x97 - m.x124)**2 + (m.x176 - m.x203)**2)**(-3)
    * (((m.x18 - m.x45)**2 + (m.x97 - m.x124)**2 + (m.x176 - m.x203)**2)**(-3)
    - 2) + ((m.x18 - m.x46)**2 + (m.x97 - m.x125)**2 + (m.x176 - m.x204)**2)**
    (-3) * (((m.x18 - m.x46)**2 + (m.x97 - m.x125)**2 + (m.x176 - m.x204)**2)**
    (-3) - 2) + ((m.x18 - m.x47)**2 + (m.x97 - m.x126)**2 + (m.x176 - m.x205)**
    2)**(-3) * (((m.x18 - m.x47)**2 + (m.x97 - m.x126)**2 + (m.x176 - m.x205)**
    2)**(-3) - 2) + ((m.x18 - m.x48)**2 + (m.x97 - m.x127)**2 + (m.x176 -
    m.x206)**2)**(-3) * (((m.x18 - m.x48)**2 + (m.x97 - m.x127)**2 + (m.x176 -
    m.x206)**2)**(-3) - 2) + ((m.x18 - m.x49)**2 + (m.x97 - m.x128)**2 + (
    m.x176 - m.x207)**2)**(-3) * (((m.x18 - m.x49)**2 + (m.x97 - m.x128)**2 + (
    m.x176 - m.x207)**2)**(-3) - 2) + ((m.x18 - m.x50)**2 + (m.x97 - m.x129)**2
    + (m.x176 - m.x208)**2)**(-3) * (((m.x18 - m.x50)**2 + (m.x97 - m.x129)**2
    + (m.x176 - m.x208)**2)**(-3) - 2) + ((m.x18 - m.x51)**2 + (m.x97 - m.x130)
    **2 + (m.x176 - m.x209)**2)**(-3) * (((m.x18 - m.x51)**2 + (m.x97 - m.x130)
    **2 + (m.x176 - m.x209)**2)**(-3) - 2) + ((m.x18 - m.x52)**2 + (m.x97 -
    m.x131)**2 + (m.x176 - m.x210)**2)**(-3) * (((m.x18 - m.x52)**2 + (m.x97 -
    m.x131)**2 + (m.x176 - m.x210)**2)**(-3) - 2) + ((m.x18 - m.x53)**2 + (
    m.x97 - m.x132)**2 + (m.x176 - m.x211)**2)**(-3) * (((m.x18 - m.x53)**2 + (
    m.x97 - m.x132)**2 + (m.x176 - m.x211)**2)**(-3) - 2) + ((m.x18 - m.x54)**2
    + (m.x97 - m.x133)**2 + (m.x176 - m.x212)**2)**(-3) * (((m.x18 - m.x54)**2
    + (m.x97 - m.x133)**2 + (m.x176 - m.x212)**2)**(-3) - 2) + ((m.x18 - m.x55)
    **2 + (m.x97 - m.x134)**2 + (m.x176 - m.x213)**2)**(-3) * (((m.x18 - m.x55)
    **2 + (m.x97 - m.x134)**2 + (m.x176 - m.x213)**2)**(-3) - 2) + ((m.x18 -
    m.x56)**2 + (m.x97 - m.x135)**2 + (m.x176 - m.x214)**2)**(-3) * (((m.x18 -
    m.x56)**2 + (m.x97 - m.x135)**2 + (m.x176 - m.x214)**2)**(-3) - 2) + ((
    m.x18 - m.x57)**2 + (m.x97 - m.x136)**2 + (m.x176 - m.x215)**2)**(-3) * (((
    m.x18 - m.x57)**2 + (m.x97 - m.x136)**2 + (m.x176 - m.x215)**2)**(-3) - 2)
    + ((m.x18 - m.x58)**2 + (m.x97 - m.x137)**2 + (m.x176 - m.x216)**2)**(-3)
    * (((m.x18 - m.x58)**2 + (m.x97 - m.x137)**2 + (m.x176 - m.x216)**2)**(-3)
    - 2) + ((m.x18 - m.x59)**2 + (m.x97 - m.x138)**2 + (m.x176 - m.x217)**2)**
    (-3) * (((m.x18 - m.x59)**2 + (m.x97 - m.x138)**2 + (m.x176 - m.x217)**2)**
    (-3) - 2) + ((m.x18 - m.x60)**2 + (m.x97 - m.x139)**2 + (m.x176 - m.x218)**
    2)**(-3) * (((m.x18 - m.x60)**2 + (m.x97 - m.x139)**2 + (m.x176 - m.x218)**
    2)**(-3) - 2) + ((m.x18 - m.x61)**2 + (m.x97 - m.x140)**2 + (m.x176 -
    m.x219)**2)**(-3) * (((m.x18 - m.x61)**2 + (m.x97 - m.x140)**2 + (m.x176 -
    m.x219)**2)**(-3) - 2) + ((m.x18 - m.x62)**2 + (m.x97 - m.x141)**2 + (
    m.x176 - m.x220)**2)**(-3) * (((m.x18 - m.x62)**2 + (m.x97 - m.x141)**2 + (
    m.x176 - m.x220)**2)**(-3) - 2) + ((m.x18 - m.x63)**2 + (m.x97 - m.x142)**2
    + (m.x176 - m.x221)**2)**(-3) * (((m.x18 - m.x63)**2 + (m.x97 - m.x142)**2
    + (m.x176 - m.x221)**2)**(-3) - 2) + ((m.x18 - m.x64)**2 + (m.x97 - m.x143)
    **2 + (m.x176 - m.x222)**2)**(-3) * (((m.x18 - m.x64)**2 + (m.x97 - m.x143)
    **2 + (m.x176 - m.x222)**2)**(-3) - 2) + ((m.x18 - m.x65)**2 + (m.x97 -
    m.x144)**2 + (m.x176 - m.x223)**2)**(-3) * (((m.x18 - m.x65)**2 + (m.x97 -
    m.x144)**2 + (m.x176 - m.x223)**2)**(-3) - 2) + ((m.x18 - m.x66)**2 + (
    m.x97 - m.x145)**2 + (m.x176 - m.x224)**2)**(-3) * (((m.x18 - m.x66)**2 + (
    m.x97 - m.x145)**2 + (m.x176 - m.x224)**2)**(-3) - 2) + ((m.x18 - m.x67)**2
    + (m.x97 - m.x146)**2 + (m.x176 - m.x225)**2)**(-3) * (((m.x18 - m.x67)**2
    + (m.x97 - m.x146)**2 + (m.x176 - m.x225)**2)**(-3) - 2) + ((m.x18 - m.x68)
    **2 + (m.x97 - m.x147)**2 + (m.x176 - m.x226)**2)**(-3) * (((m.x18 - m.x68)
    **2 + (m.x97 - m.x147)**2 + (m.x176 - m.x226)**2)**(-3) - 2) + ((m.x18 -
    m.x69)**2 + (m.x97 - m.x148)**2 + (m.x176 - m.x227)**2)**(-3) * (((m.x18 -
    m.x69)**2 + (m.x97 - m.x148)**2 + (m.x176 - m.x227)**2)**(-3) - 2) + ((
    m.x18 - m.x70)**2 + (m.x97 - m.x149)**2 + (m.x176 - m.x228)**2)**(-3) * (((
    m.x18 - m.x70)**2 + (m.x97 - m.x149)**2 + (m.x176 - m.x228)**2)**(-3) - 2)
    + ((m.x18 - m.x71)**2 + (m.x97 - m.x150)**2 + (m.x176 - m.x229)**2)**(-3)
    * (((m.x18 - m.x71)**2 + (m.x97 - m.x150)**2 + (m.x176 - m.x229)**2)**(-3)
    - 2) + ((m.x18 - m.x72)**2 + (m.x97 - m.x151)**2 + (m.x176 - m.x230)**2)**
    (-3) * (((m.x18 - m.x72)**2 + (m.x97 - m.x151)**2 + (m.x176 - m.x230)**2)**
    (-3) - 2) + ((m.x18 - m.x73)**2 + (m.x97 - m.x152)**2 + (m.x176 - m.x231)**
    2)**(-3) * (((m.x18 - m.x73)**2 + (m.x97 - m.x152)**2 + (m.x176 - m.x231)**
    2)**(-3) - 2) + ((m.x18 - m.x74)**2 + (m.x97 - m.x153)**2 + (m.x176 -
    m.x232)**2)**(-3) * (((m.x18 - m.x74)**2 + (m.x97 - m.x153)**2 + (m.x176 -
    m.x232)**2)**(-3) - 2) + ((m.x18 - m.x75)**2 + (m.x97 - m.x154)**2 + (
    m.x176 - m.x233)**2)**(-3) * (((m.x18 - m.x75)**2 + (m.x97 - m.x154)**2 + (
    m.x176 - m.x233)**2)**(-3) - 2) + ((m.x18 - m.x76)**2 + (m.x97 - m.x155)**2
    + (m.x176 - m.x234)**2)**(-3) * (((m.x18 - m.x76)**2 + (m.x97 - m.x155)**2
    + (m.x176 - m.x234)**2)**(-3) - 2) + ((m.x18 - m.x77)**2 + (m.x97 - m.x156)
    **2 + (m.x176 - m.x235)**2)**(-3) * (((m.x18 - m.x77)**2 + (m.x97 - m.x156)
    **2 + (m.x176 - m.x235)**2)**(-3) - 2) + ((m.x18 - m.x78)**2 + (m.x97 -
    m.x157)**2 + (m.x176 - m.x236)**2)**(-3) * (((m.x18 - m.x78)**2 + (m.x97 -
    m.x157)**2 + (m.x176 - m.x236)**2)**(-3) - 2) + ((m.x18 - m.x79)**2 + (
    m.x97 - m.x158)**2 + (m.x176 - m.x237)**2)**(-3) * (((m.x18 - m.x79)**2 + (
    m.x97 - m.x158)**2 + (m.x176 - m.x237)**2)**(-3) - 2) + ((m.x19 - m.x20)**2
    + (m.x98 - m.x99)**2 + (m.x177 - m.x178)**2)**(-3) * (((m.x19 - m.x20)**2
    + (m.x98 - m.x99)**2 + (m.x177 - m.x178)**2)**(-3) - 2) + ((m.x19 - m.x21)
    **2 + (m.x98 - m.x100)**2 + (m.x177 - m.x179)**2)**(-3) * (((m.x19 - m.x21)
    **2 + (m.x98 - m.x100)**2 + (m.x177 - m.x179)**2)**(-3) - 2) + ((m.x19 -
    m.x22)**2 + (m.x98 - m.x101)**2 + (m.x177 - m.x180)**2)**(-3) * (((m.x19 -
    m.x22)**2 + (m.x98 - m.x101)**2 + (m.x177 - m.x180)**2)**(-3) - 2) + ((
    m.x19 - m.x23)**2 + (m.x98 - m.x102)**2 + (m.x177 - m.x181)**2)**(-3) * (((
    m.x19 - m.x23)**2 + (m.x98 - m.x102)**2 + (m.x177 - m.x181)**2)**(-3) - 2)
    + ((m.x19 - m.x24)**2 + (m.x98 - m.x103)**2 + (m.x177 - m.x182)**2)**(-3)
    * (((m.x19 - m.x24)**2 + (m.x98 - m.x103)**2 + (m.x177 - m.x182)**2)**(-3)
    - 2) + ((m.x19 - m.x25)**2 + (m.x98 - m.x104)**2 + (m.x177 - m.x183)**2)**
    (-3) * (((m.x19 - m.x25)**2 + (m.x98 - m.x104)**2 + (m.x177 - m.x183)**2)**
    (-3) - 2) + ((m.x19 - m.x26)**2 + (m.x98 - m.x105)**2 + (m.x177 - m.x184)**
    2)**(-3) * (((m.x19 - m.x26)**2 + (m.x98 - m.x105)**2 + (m.x177 - m.x184)**
    2)**(-3) - 2) + ((m.x19 - m.x27)**2 + (m.x98 - m.x106)**2 + (m.x177 -
    m.x185)**2)**(-3) * (((m.x19 - m.x27)**2 + (m.x98 - m.x106)**2 + (m.x177 -
    m.x185)**2)**(-3) - 2) + ((m.x19 - m.x28)**2 + (m.x98 - m.x107)**2 + (
    m.x177 - m.x186)**2)**(-3) * (((m.x19 - m.x28)**2 + (m.x98 - m.x107)**2 + (
    m.x177 - m.x186)**2)**(-3) - 2) + ((m.x19 - m.x29)**2 + (m.x98 - m.x108)**2
    + (m.x177 - m.x187)**2)**(-3) * (((m.x19 - m.x29)**2 + (m.x98 - m.x108)**2
    + (m.x177 - m.x187)**2)**(-3) - 2) + ((m.x19 - m.x30)**2 + (m.x98 - m.x109)
    **2 + (m.x177 - m.x188)**2)**(-3) * (((m.x19 - m.x30)**2 + (m.x98 - m.x109)
    **2 + (m.x177 - m.x188)**2)**(-3) - 2) + ((m.x19 - m.x31)**2 + (m.x98 -
    m.x110)**2 + (m.x177 - m.x189)**2)**(-3) * (((m.x19 - m.x31)**2 + (m.x98 -
    m.x110)**2 + (m.x177 - m.x189)**2)**(-3) - 2) + ((m.x19 - m.x32)**2 + (
    m.x98 - m.x111)**2 + (m.x177 - m.x190)**2)**(-3) * (((m.x19 - m.x32)**2 + (
    m.x98 - m.x111)**2 + (m.x177 - m.x190)**2)**(-3) - 2) + ((m.x19 - m.x33)**2
    + (m.x98 - m.x112)**2 + (m.x177 - m.x191)**2)**(-3) * (((m.x19 - m.x33)**2
    + (m.x98 - m.x112)**2 + (m.x177 - m.x191)**2)**(-3) - 2) + ((m.x19 - m.x34)
    **2 + (m.x98 - m.x113)**2 + (m.x177 - m.x192)**2)**(-3) * (((m.x19 - m.x34)
    **2 + (m.x98 - m.x113)**2 + (m.x177 - m.x192)**2)**(-3) - 2) + ((m.x19 -
    m.x35)**2 + (m.x98 - m.x114)**2 + (m.x177 - m.x193)**2)**(-3) * (((m.x19 -
    m.x35)**2 + (m.x98 - m.x114)**2 + (m.x177 - m.x193)**2)**(-3) - 2) + ((
    m.x19 - m.x36)**2 + (m.x98 - m.x115)**2 + (m.x177 - m.x194)**2)**(-3) * (((
    m.x19 - m.x36)**2 + (m.x98 - m.x115)**2 + (m.x177 - m.x194)**2)**(-3) - 2)
    + ((m.x19 - m.x37)**2 + (m.x98 - m.x116)**2 + (m.x177 - m.x195)**2)**(-3)
    * (((m.x19 - m.x37)**2 + (m.x98 - m.x116)**2 + (m.x177 - m.x195)**2)**(-3)
    - 2) + ((m.x19 - m.x38)**2 + (m.x98 - m.x117)**2 + (m.x177 - m.x196)**2)**
    (-3) * (((m.x19 - m.x38)**2 + (m.x98 - m.x117)**2 + (m.x177 - m.x196)**2)**
    (-3) - 2) + ((m.x19 - m.x39)**2 + (m.x98 - m.x118)**2 + (m.x177 - m.x197)**
    2)**(-3) * (((m.x19 - m.x39)**2 + (m.x98 - m.x118)**2 + (m.x177 - m.x197)**
    2)**(-3) - 2) + ((m.x19 - m.x40)**2 + (m.x98 - m.x119)**2 + (m.x177 -
    m.x198)**2)**(-3) * (((m.x19 - m.x40)**2 + (m.x98 - m.x119)**2 + (m.x177 -
    m.x198)**2)**(-3) - 2) + ((m.x19 - m.x41)**2 + (m.x98 - m.x120)**2 + (
    m.x177 - m.x199)**2)**(-3) * (((m.x19 - m.x41)**2 + (m.x98 - m.x120)**2 + (
    m.x177 - m.x199)**2)**(-3) - 2) + ((m.x19 - m.x42)**2 + (m.x98 - m.x121)**2
    + (m.x177 - m.x200)**2)**(-3) * (((m.x19 - m.x42)**2 + (m.x98 - m.x121)**2
    + (m.x177 - m.x200)**2)**(-3) - 2) + ((m.x19 - m.x43)**2 + (m.x98 - m.x122)
    **2 + (m.x177 - m.x201)**2)**(-3) * (((m.x19 - m.x43)**2 + (m.x98 - m.x122)
    **2 + (m.x177 - m.x201)**2)**(-3) - 2) + ((m.x19 - m.x44)**2 + (m.x98 -
    m.x123)**2 + (m.x177 - m.x202)**2)**(-3) * (((m.x19 - m.x44)**2 + (m.x98 -
    m.x123)**2 + (m.x177 - m.x202)**2)**(-3) - 2) + ((m.x19 - m.x45)**2 + (
    m.x98 - m.x124)**2 + (m.x177 - m.x203)**2)**(-3) * (((m.x19 - m.x45)**2 + (
    m.x98 - m.x124)**2 + (m.x177 - m.x203)**2)**(-3) - 2) + ((m.x19 - m.x46)**2
    + (m.x98 - m.x125)**2 + (m.x177 - m.x204)**2)**(-3) * (((m.x19 - m.x46)**2
    + (m.x98 - m.x125)**2 + (m.x177 - m.x204)**2)**(-3) - 2) + ((m.x19 - m.x47)
    **2 + (m.x98 - m.x126)**2 + (m.x177 - m.x205)**2)**(-3) * (((m.x19 - m.x47)
    **2 + (m.x98 - m.x126)**2 + (m.x177 - m.x205)**2)**(-3) - 2) + ((m.x19 -
    m.x48)**2 + (m.x98 - m.x127)**2 + (m.x177 - m.x206)**2)**(-3) * (((m.x19 -
    m.x48)**2 + (m.x98 - m.x127)**2 + (m.x177 - m.x206)**2)**(-3) - 2) + ((
    m.x19 - m.x49)**2 + (m.x98 - m.x128)**2 + (m.x177 - m.x207)**2)**(-3) * (((
    m.x19 - m.x49)**2 + (m.x98 - m.x128)**2 + (m.x177 - m.x207)**2)**(-3) - 2)
    + ((m.x19 - m.x50)**2 + (m.x98 - m.x129)**2 + (m.x177 - m.x208)**2)**(-3)
    * (((m.x19 - m.x50)**2 + (m.x98 - m.x129)**2 + (m.x177 - m.x208)**2)**(-3)
    - 2) + ((m.x19 - m.x51)**2 + (m.x98 - m.x130)**2 + (m.x177 - m.x209)**2)**
    (-3) * (((m.x19 - m.x51)**2 + (m.x98 - m.x130)**2 + (m.x177 - m.x209)**2)**
    (-3) - 2) + ((m.x19 - m.x52)**2 + (m.x98 - m.x131)**2 + (m.x177 - m.x210)**
    2)**(-3) * (((m.x19 - m.x52)**2 + (m.x98 - m.x131)**2 + (m.x177 - m.x210)**
    2)**(-3) - 2) + ((m.x19 - m.x53)**2 + (m.x98 - m.x132)**2 + (m.x177 -
    m.x211)**2)**(-3) * (((m.x19 - m.x53)**2 + (m.x98 - m.x132)**2 + (m.x177 -
    m.x211)**2)**(-3) - 2) + ((m.x19 - m.x54)**2 + (m.x98 - m.x133)**2 + (
    m.x177 - m.x212)**2)**(-3) * (((m.x19 - m.x54)**2 + (m.x98 - m.x133)**2 + (
    m.x177 - m.x212)**2)**(-3) - 2) + ((m.x19 - m.x55)**2 + (m.x98 - m.x134)**2
    + (m.x177 - m.x213)**2)**(-3) * (((m.x19 - m.x55)**2 + (m.x98 - m.x134)**2
    + (m.x177 - m.x213)**2)**(-3) - 2) + ((m.x19 - m.x56)**2 + (m.x98 - m.x135)
    **2 + (m.x177 - m.x214)**2)**(-3) * (((m.x19 - m.x56)**2 + (m.x98 - m.x135)
    **2 + (m.x177 - m.x214)**2)**(-3) - 2) + ((m.x19 - m.x57)**2 + (m.x98 -
    m.x136)**2 + (m.x177 - m.x215)**2)**(-3) * (((m.x19 - m.x57)**2 + (m.x98 -
    m.x136)**2 + (m.x177 - m.x215)**2)**(-3) - 2) + ((m.x19 - m.x58)**2 + (
    m.x98 - m.x137)**2 + (m.x177 - m.x216)**2)**(-3) * (((m.x19 - m.x58)**2 + (
    m.x98 - m.x137)**2 + (m.x177 - m.x216)**2)**(-3) - 2) + ((m.x19 - m.x59)**2
    + (m.x98 - m.x138)**2 + (m.x177 - m.x217)**2)**(-3) * (((m.x19 - m.x59)**2
    + (m.x98 - m.x138)**2 + (m.x177 - m.x217)**2)**(-3) - 2) + ((m.x19 - m.x60)
    **2 + (m.x98 - m.x139)**2 + (m.x177 - m.x218)**2)**(-3) * (((m.x19 - m.x60)
    **2 + (m.x98 - m.x139)**2 + (m.x177 - m.x218)**2)**(-3) - 2) + ((m.x19 -
    m.x61)**2 + (m.x98 - m.x140)**2 + (m.x177 - m.x219)**2)**(-3) * (((m.x19 -
    m.x61)**2 + (m.x98 - m.x140)**2 + (m.x177 - m.x219)**2)**(-3) - 2) + ((
    m.x19 - m.x62)**2 + (m.x98 - m.x141)**2 + (m.x177 - m.x220)**2)**(-3) * (((
    m.x19 - m.x62)**2 + (m.x98 - m.x141)**2 + (m.x177 - m.x220)**2)**(-3) - 2)
    + ((m.x19 - m.x63)**2 + (m.x98 - m.x142)**2 + (m.x177 - m.x221)**2)**(-3)
    * (((m.x19 - m.x63)**2 + (m.x98 - m.x142)**2 + (m.x177 - m.x221)**2)**(-3)
    - 2) + ((m.x19 - m.x64)**2 + (m.x98 - m.x143)**2 + (m.x177 - m.x222)**2)**
    (-3) * (((m.x19 - m.x64)**2 + (m.x98 - m.x143)**2 + (m.x177 - m.x222)**2)**
    (-3) - 2) + ((m.x19 - m.x65)**2 + (m.x98 - m.x144)**2 + (m.x177 - m.x223)**
    2)**(-3) * (((m.x19 - m.x65)**2 + (m.x98 - m.x144)**2 + (m.x177 - m.x223)**
    2)**(-3) - 2) + ((m.x19 - m.x66)**2 + (m.x98 - m.x145)**2 + (m.x177 -
    m.x224)**2)**(-3) * (((m.x19 - m.x66)**2 + (m.x98 - m.x145)**2 + (m.x177 -
    m.x224)**2)**(-3) - 2) + ((m.x19 - m.x67)**2 + (m.x98 - m.x146)**2 + (
    m.x177 - m.x225)**2)**(-3) * (((m.x19 - m.x67)**2 + (m.x98 - m.x146)**2 + (
    m.x177 - m.x225)**2)**(-3) - 2) + ((m.x19 - m.x68)**2 + (m.x98 - m.x147)**2
    + (m.x177 - m.x226)**2)**(-3) * (((m.x19 - m.x68)**2 + (m.x98 - m.x147)**2
    + (m.x177 - m.x226)**2)**(-3) - 2) + ((m.x19 - m.x69)**2 + (m.x98 - m.x148)
    **2 + (m.x177 - m.x227)**2)**(-3) * (((m.x19 - m.x69)**2 + (m.x98 - m.x148)
    **2 + (m.x177 - m.x227)**2)**(-3) - 2) + ((m.x19 - m.x70)**2 + (m.x98 -
    m.x149)**2 + (m.x177 - m.x228)**2)**(-3) * (((m.x19 - m.x70)**2 + (m.x98 -
    m.x149)**2 + (m.x177 - m.x228)**2)**(-3) - 2) + ((m.x19 - m.x71)**2 + (
    m.x98 - m.x150)**2 + (m.x177 - m.x229)**2)**(-3) * (((m.x19 - m.x71)**2 + (
    m.x98 - m.x150)**2 + (m.x177 - m.x229)**2)**(-3) - 2) + ((m.x19 - m.x72)**2
    + (m.x98 - m.x151)**2 + (m.x177 - m.x230)**2)**(-3) * (((m.x19 - m.x72)**2
    + (m.x98 - m.x151)**2 + (m.x177 - m.x230)**2)**(-3) - 2) + ((m.x19 - m.x73)
    **2 + (m.x98 - m.x152)**2 + (m.x177 - m.x231)**2)**(-3) * (((m.x19 - m.x73)
    **2 + (m.x98 - m.x152)**2 + (m.x177 - m.x231)**2)**(-3) - 2) + ((m.x19 -
    m.x74)**2 + (m.x98 - m.x153)**2 + (m.x177 - m.x232)**2)**(-3) * (((m.x19 -
    m.x74)**2 + (m.x98 - m.x153)**2 + (m.x177 - m.x232)**2)**(-3) - 2) + ((
    m.x19 - m.x75)**2 + (m.x98 - m.x154)**2 + (m.x177 - m.x233)**2)**(-3) * (((
    m.x19 - m.x75)**2 + (m.x98 - m.x154)**2 + (m.x177 - m.x233)**2)**(-3) - 2)
    + ((m.x19 - m.x76)**2 + (m.x98 - m.x155)**2 + (m.x177 - m.x234)**2)**(-3)
    * (((m.x19 - m.x76)**2 + (m.x98 - m.x155)**2 + (m.x177 - m.x234)**2)**(-3)
    - 2) + ((m.x19 - m.x77)**2 + (m.x98 - m.x156)**2 + (m.x177 - m.x235)**2)**
    (-3) * (((m.x19 - m.x77)**2 + (m.x98 - m.x156)**2 + (m.x177 - m.x235)**2)**
    (-3) - 2) + ((m.x19 - m.x78)**2 + (m.x98 - m.x157)**2 + (m.x177 - m.x236)**
    2)**(-3) * (((m.x19 - m.x78)**2 + (m.x98 - m.x157)**2 + (m.x177 - m.x236)**
    2)**(-3) - 2) + ((m.x19 - m.x79)**2 + (m.x98 - m.x158)**2 + (m.x177 -
    m.x237)**2)**(-3) * (((m.x19 - m.x79)**2 + (m.x98 - m.x158)**2 + (m.x177 -
    m.x237)**2)**(-3) - 2) + ((m.x20 - m.x21)**2 + (m.x99 - m.x100)**2 + (
    m.x178 - m.x179)**2)**(-3) * (((m.x20 - m.x21)**2 + (m.x99 - m.x100)**2 + (
    m.x178 - m.x179)**2)**(-3) - 2) + ((m.x20 - m.x22)**2 + (m.x99 - m.x101)**2
    + (m.x178 - m.x180)**2)**(-3) * (((m.x20 - m.x22)**2 + (m.x99 - m.x101)**2
    + (m.x178 - m.x180)**2)**(-3) - 2) + ((m.x20 - m.x23)**2 + (m.x99 - m.x102)
    **2 + (m.x178 - m.x181)**2)**(-3) * (((m.x20 - m.x23)**2 + (m.x99 - m.x102)
    **2 + (m.x178 - m.x181)**2)**(-3) - 2) + ((m.x20 - m.x24)**2 + (m.x99 -
    m.x103)**2 + (m.x178 - m.x182)**2)**(-3) * (((m.x20 - m.x24)**2 + (m.x99 -
    m.x103)**2 + (m.x178 - m.x182)**2)**(-3) - 2) + ((m.x20 - m.x25)**2 + (
    m.x99 - m.x104)**2 + (m.x178 - m.x183)**2)**(-3) * (((m.x20 - m.x25)**2 + (
    m.x99 - m.x104)**2 + (m.x178 - m.x183)**2)**(-3) - 2) + ((m.x20 - m.x26)**2
    + (m.x99 - m.x105)**2 + (m.x178 - m.x184)**2)**(-3) * (((m.x20 - m.x26)**2
    + (m.x99 - m.x105)**2 + (m.x178 - m.x184)**2)**(-3) - 2) + ((m.x20 - m.x27)
    **2 + (m.x99 - m.x106)**2 + (m.x178 - m.x185)**2)**(-3) * (((m.x20 - m.x27)
    **2 + (m.x99 - m.x106)**2 + (m.x178 - m.x185)**2)**(-3) - 2) + ((m.x20 -
    m.x28)**2 + (m.x99 - m.x107)**2 + (m.x178 - m.x186)**2)**(-3) * (((m.x20 -
    m.x28)**2 + (m.x99 - m.x107)**2 + (m.x178 - m.x186)**2)**(-3) - 2) + ((
    m.x20 - m.x29)**2 + (m.x99 - m.x108)**2 + (m.x178 - m.x187)**2)**(-3) * (((
    m.x20 - m.x29)**2 + (m.x99 - m.x108)**2 + (m.x178 - m.x187)**2)**(-3) - 2)
    + ((m.x20 - m.x30)**2 + (m.x99 - m.x109)**2 + (m.x178 - m.x188)**2)**(-3)
    * (((m.x20 - m.x30)**2 + (m.x99 - m.x109)**2 + (m.x178 - m.x188)**2)**(-3)
    - 2) + ((m.x20 - m.x31)**2 + (m.x99 - m.x110)**2 + (m.x178 - m.x189)**2)**
    (-3) * (((m.x20 - m.x31)**2 + (m.x99 - m.x110)**2 + (m.x178 - m.x189)**2)**
    (-3) - 2) + ((m.x20 - m.x32)**2 + (m.x99 - m.x111)**2 + (m.x178 - m.x190)**
    2)**(-3) * (((m.x20 - m.x32)**2 + (m.x99 - m.x111)**2 + (m.x178 - m.x190)**
    2)**(-3) - 2) + ((m.x20 - m.x33)**2 + (m.x99 - m.x112)**2 + (m.x178 -
    m.x191)**2)**(-3) * (((m.x20 - m.x33)**2 + (m.x99 - m.x112)**2 + (m.x178 -
    m.x191)**2)**(-3) - 2) + ((m.x20 - m.x34)**2 + (m.x99 - m.x113)**2 + (
    m.x178 - m.x192)**2)**(-3) * (((m.x20 - m.x34)**2 + (m.x99 - m.x113)**2 + (
    m.x178 - m.x192)**2)**(-3) - 2) + ((m.x20 - m.x35)**2 + (m.x99 - m.x114)**2
    + (m.x178 - m.x193)**2)**(-3) * (((m.x20 - m.x35)**2 + (m.x99 - m.x114)**2
    + (m.x178 - m.x193)**2)**(-3) - 2) + ((m.x20 - m.x36)**2 + (m.x99 - m.x115)
    **2 + (m.x178 - m.x194)**2)**(-3) * (((m.x20 - m.x36)**2 + (m.x99 - m.x115)
    **2 + (m.x178 - m.x194)**2)**(-3) - 2) + ((m.x20 - m.x37)**2 + (m.x99 -
    m.x116)**2 + (m.x178 - m.x195)**2)**(-3) * (((m.x20 - m.x37)**2 + (m.x99 -
    m.x116)**2 + (m.x178 - m.x195)**2)**(-3) - 2) + ((m.x20 - m.x38)**2 + (
    m.x99 - m.x117)**2 + (m.x178 - m.x196)**2)**(-3) * (((m.x20 - m.x38)**2 + (
    m.x99 - m.x117)**2 + (m.x178 - m.x196)**2)**(-3) - 2) + ((m.x20 - m.x39)**2
    + (m.x99 - m.x118)**2 + (m.x178 - m.x197)**2)**(-3) * (((m.x20 - m.x39)**2
    + (m.x99 - m.x118)**2 + (m.x178 - m.x197)**2)**(-3) - 2) + ((m.x20 - m.x40)
    **2 + (m.x99 - m.x119)**2 + (m.x178 - m.x198)**2)**(-3) * (((m.x20 - m.x40)
    **2 + (m.x99 - m.x119)**2 + (m.x178 - m.x198)**2)**(-3) - 2) + ((m.x20 -
    m.x41)**2 + (m.x99 - m.x120)**2 + (m.x178 - m.x199)**2)**(-3) * (((m.x20 -
    m.x41)**2 + (m.x99 - m.x120)**2 + (m.x178 - m.x199)**2)**(-3) - 2) + ((
    m.x20 - m.x42)**2 + (m.x99 - m.x121)**2 + (m.x178 - m.x200)**2)**(-3) * (((
    m.x20 - m.x42)**2 + (m.x99 - m.x121)**2 + (m.x178 - m.x200)**2)**(-3) - 2)
    + ((m.x20 - m.x43)**2 + (m.x99 - m.x122)**2 + (m.x178 - m.x201)**2)**(-3)
    * (((m.x20 - m.x43)**2 + (m.x99 - m.x122)**2 + (m.x178 - m.x201)**2)**(-3)
    - 2) + ((m.x20 - m.x44)**2 + (m.x99 - m.x123)**2 + (m.x178 - m.x202)**2)**
    (-3) * (((m.x20 - m.x44)**2 + (m.x99 - m.x123)**2 + (m.x178 - m.x202)**2)**
    (-3) - 2) + ((m.x20 - m.x45)**2 + (m.x99 - m.x124)**2 + (m.x178 - m.x203)**
    2)**(-3) * (((m.x20 - m.x45)**2 + (m.x99 - m.x124)**2 + (m.x178 - m.x203)**
    2)**(-3) - 2) + ((m.x20 - m.x46)**2 + (m.x99 - m.x125)**2 + (m.x178 -
    m.x204)**2)**(-3) * (((m.x20 - m.x46)**2 + (m.x99 - m.x125)**2 + (m.x178 -
    m.x204)**2)**(-3) - 2) + ((m.x20 - m.x47)**2 + (m.x99 - m.x126)**2 + (
    m.x178 - m.x205)**2)**(-3) * (((m.x20 - m.x47)**2 + (m.x99 - m.x126)**2 + (
    m.x178 - m.x205)**2)**(-3) - 2) + ((m.x20 - m.x48)**2 + (m.x99 - m.x127)**2
    + (m.x178 - m.x206)**2)**(-3) * (((m.x20 - m.x48)**2 + (m.x99 - m.x127)**2
    + (m.x178 - m.x206)**2)**(-3) - 2) + ((m.x20 - m.x49)**2 + (m.x99 - m.x128)
    **2 + (m.x178 - m.x207)**2)**(-3) * (((m.x20 - m.x49)**2 + (m.x99 - m.x128)
    **2 + (m.x178 - m.x207)**2)**(-3) - 2) + ((m.x20 - m.x50)**2 + (m.x99 -
    m.x129)**2 + (m.x178 - m.x208)**2)**(-3) * (((m.x20 - m.x50)**2 + (m.x99 -
    m.x129)**2 + (m.x178 - m.x208)**2)**(-3) - 2) + ((m.x20 - m.x51)**2 + (
    m.x99 - m.x130)**2 + (m.x178 - m.x209)**2)**(-3) * (((m.x20 - m.x51)**2 + (
    m.x99 - m.x130)**2 + (m.x178 - m.x209)**2)**(-3) - 2) + ((m.x20 - m.x52)**2
    + (m.x99 - m.x131)**2 + (m.x178 - m.x210)**2)**(-3) * (((m.x20 - m.x52)**2
    + (m.x99 - m.x131)**2 + (m.x178 - m.x210)**2)**(-3) - 2) + ((m.x20 - m.x53)
    **2 + (m.x99 - m.x132)**2 + (m.x178 - m.x211)**2)**(-3) * (((m.x20 - m.x53)
    **2 + (m.x99 - m.x132)**2 + (m.x178 - m.x211)**2)**(-3) - 2) + ((m.x20 -
    m.x54)**2 + (m.x99 - m.x133)**2 + (m.x178 - m.x212)**2)**(-3) * (((m.x20 -
    m.x54)**2 + (m.x99 - m.x133)**2 + (m.x178 - m.x212)**2)**(-3) - 2) + ((
    m.x20 - m.x55)**2 + (m.x99 - m.x134)**2 + (m.x178 - m.x213)**2)**(-3) * (((
    m.x20 - m.x55)**2 + (m.x99 - m.x134)**2 + (m.x178 - m.x213)**2)**(-3) - 2)
    + ((m.x20 - m.x56)**2 + (m.x99 - m.x135)**2 + (m.x178 - m.x214)**2)**(-3)
    * (((m.x20 - m.x56)**2 + (m.x99 - m.x135)**2 + (m.x178 - m.x214)**2)**(-3)
    - 2) + ((m.x20 - m.x57)**2 + (m.x99 - m.x136)**2 + (m.x178 - m.x215)**2)**
    (-3) * (((m.x20 - m.x57)**2 + (m.x99 - m.x136)**2 + (m.x178 - m.x215)**2)**
    (-3) - 2) + ((m.x20 - m.x58)**2 + (m.x99 - m.x137)**2 + (m.x178 - m.x216)**
    2)**(-3) * (((m.x20 - m.x58)**2 + (m.x99 - m.x137)**2 + (m.x178 - m.x216)**
    2)**(-3) - 2) + ((m.x20 - m.x59)**2 + (m.x99 - m.x138)**2 + (m.x178 -
    m.x217)**2)**(-3) * (((m.x20 - m.x59)**2 + (m.x99 - m.x138)**2 + (m.x178 -
    m.x217)**2)**(-3) - 2) + ((m.x20 - m.x60)**2 + (m.x99 - m.x139)**2 + (
    m.x178 - m.x218)**2)**(-3) * (((m.x20 - m.x60)**2 + (m.x99 - m.x139)**2 + (
    m.x178 - m.x218)**2)**(-3) - 2) + ((m.x20 - m.x61)**2 + (m.x99 - m.x140)**2
    + (m.x178 - m.x219)**2)**(-3) * (((m.x20 - m.x61)**2 + (m.x99 - m.x140)**2
    + (m.x178 - m.x219)**2)**(-3) - 2) + ((m.x20 - m.x62)**2 + (m.x99 - m.x141)
    **2 + (m.x178 - m.x220)**2)**(-3) * (((m.x20 - m.x62)**2 + (m.x99 - m.x141)
    **2 + (m.x178 - m.x220)**2)**(-3) - 2) + ((m.x20 - m.x63)**2 + (m.x99 -
    m.x142)**2 + (m.x178 - m.x221)**2)**(-3) * (((m.x20 - m.x63)**2 + (m.x99 -
    m.x142)**2 + (m.x178 - m.x221)**2)**(-3) - 2) + ((m.x20 - m.x64)**2 + (
    m.x99 - m.x143)**2 + (m.x178 - m.x222)**2)**(-3) * (((m.x20 - m.x64)**2 + (
    m.x99 - m.x143)**2 + (m.x178 - m.x222)**2)**(-3) - 2) + ((m.x20 - m.x65)**2
    + (m.x99 - m.x144)**2 + (m.x178 - m.x223)**2)**(-3) * (((m.x20 - m.x65)**2
    + (m.x99 - m.x144)**2 + (m.x178 - m.x223)**2)**(-3) - 2) + ((m.x20 - m.x66)
    **2 + (m.x99 - m.x145)**2 + (m.x178 - m.x224)**2)**(-3) * (((m.x20 - m.x66)
    **2 + (m.x99 - m.x145)**2 + (m.x178 - m.x224)**2)**(-3) - 2) + ((m.x20 -
    m.x67)**2 + (m.x99 - m.x146)**2 + (m.x178 - m.x225)**2)**(-3) * (((m.x20 -
    m.x67)**2 + (m.x99 - m.x146)**2 + (m.x178 - m.x225)**2)**(-3) - 2) + ((
    m.x20 - m.x68)**2 + (m.x99 - m.x147)**2 + (m.x178 - m.x226)**2)**(-3) * (((
    m.x20 - m.x68)**2 + (m.x99 - m.x147)**2 + (m.x178 - m.x226)**2)**(-3) - 2)
    + ((m.x20 - m.x69)**2 + (m.x99 - m.x148)**2 + (m.x178 - m.x227)**2)**(-3)
    * (((m.x20 - m.x69)**2 + (m.x99 - m.x148)**2 + (m.x178 - m.x227)**2)**(-3)
    - 2) + ((m.x20 - m.x70)**2 + (m.x99 - m.x149)**2 + (m.x178 - m.x228)**2)**
    (-3) * (((m.x20 - m.x70)**2 + (m.x99 - m.x149)**2 + (m.x178 - m.x228)**2)**
    (-3) - 2) + ((m.x20 - m.x71)**2 + (m.x99 - m.x150)**2 + (m.x178 - m.x229)**
    2)**(-3) * (((m.x20 - m.x71)**2 + (m.x99 - m.x150)**2 + (m.x178 - m.x229)**
    2)**(-3) - 2) + ((m.x20 - m.x72)**2 + (m.x99 - m.x151)**2 + (m.x178 -
    m.x230)**2)**(-3) * (((m.x20 - m.x72)**2 + (m.x99 - m.x151)**2 + (m.x178 -
    m.x230)**2)**(-3) - 2) + ((m.x20 - m.x73)**2 + (m.x99 - m.x152)**2 + (
    m.x178 - m.x231)**2)**(-3) * (((m.x20 - m.x73)**2 + (m.x99 - m.x152)**2 + (
    m.x178 - m.x231)**2)**(-3) - 2) + ((m.x20 - m.x74)**2 + (m.x99 - m.x153)**2
    + (m.x178 - m.x232)**2)**(-3) * (((m.x20 - m.x74)**2 + (m.x99 - m.x153)**2
    + (m.x178 - m.x232)**2)**(-3) - 2) + ((m.x20 - m.x75)**2 + (m.x99 - m.x154)
    **2 + (m.x178 - m.x233)**2)**(-3) * (((m.x20 - m.x75)**2 + (m.x99 - m.x154)
    **2 + (m.x178 - m.x233)**2)**(-3) - 2) + ((m.x20 - m.x76)**2 + (m.x99 -
    m.x155)**2 + (m.x178 - m.x234)**2)**(-3) * (((m.x20 - m.x76)**2 + (m.x99 -
    m.x155)**2 + (m.x178 - m.x234)**2)**(-3) - 2) + ((m.x20 - m.x77)**2 + (
    m.x99 - m.x156)**2 + (m.x178 - m.x235)**2)**(-3) * (((m.x20 - m.x77)**2 + (
    m.x99 - m.x156)**2 + (m.x178 - m.x235)**2)**(-3) - 2) + ((m.x20 - m.x78)**2
    + (m.x99 - m.x157)**2 + (m.x178 - m.x236)**2)**(-3) * (((m.x20 - m.x78)**2
    + (m.x99 - m.x157)**2 + (m.x178 - m.x236)**2)**(-3) - 2) + ((m.x20 - m.x79)
    **2 + (m.x99 - m.x158)**2 + (m.x178 - m.x237)**2)**(-3) * (((m.x20 - m.x79)
    **2 + (m.x99 - m.x158)**2 + (m.x178 - m.x237)**2)**(-3) - 2) + ((m.x21 -
    m.x22)**2 + (m.x100 - m.x101)**2 + (m.x179 - m.x180)**2)**(-3) * (((m.x21
    - m.x22)**2 + (m.x100 - m.x101)**2 + (m.x179 - m.x180)**2)**(-3) - 2) + ((
    m.x21 - m.x23)**2 + (m.x100 - m.x102)**2 + (m.x179 - m.x181)**2)**(-3) * ((
    (m.x21 - m.x23)**2 + (m.x100 - m.x102)**2 + (m.x179 - m.x181)**2)**(-3) - 2)
    + ((m.x21 - m.x24)**2 + (m.x100 - m.x103)**2 + (m.x179 - m.x182)**2)**(-3)
    * (((m.x21 - m.x24)**2 + (m.x100 - m.x103)**2 + (m.x179 - m.x182)**2)**(-3)
    - 2) + ((m.x21 - m.x25)**2 + (m.x100 - m.x104)**2 + (m.x179 - m.x183)**2)
    **(-3) * (((m.x21 - m.x25)**2 + (m.x100 - m.x104)**2 + (m.x179 - m.x183)**2)
    **(-3) - 2) + ((m.x21 - m.x26)**2 + (m.x100 - m.x105)**2 + (m.x179 - m.x184)
    **2)**(-3) * (((m.x21 - m.x26)**2 + (m.x100 - m.x105)**2 + (m.x179 - m.x184)
    **2)**(-3) - 2) + ((m.x21 - m.x27)**2 + (m.x100 - m.x106)**2 + (m.x179 -
    m.x185)**2)**(-3) * (((m.x21 - m.x27)**2 + (m.x100 - m.x106)**2 + (m.x179
    - m.x185)**2)**(-3) - 2) + ((m.x21 - m.x28)**2 + (m.x100 - m.x107)**2 + (
    m.x179 - m.x186)**2)**(-3) * (((m.x21 - m.x28)**2 + (m.x100 - m.x107)**2 +
    (m.x179 - m.x186)**2)**(-3) - 2) + ((m.x21 - m.x29)**2 + (m.x100 - m.x108)
    **2 + (m.x179 - m.x187)**2)**(-3) * (((m.x21 - m.x29)**2 + (m.x100 - m.x108)
    **2 + (m.x179 - m.x187)**2)**(-3) - 2) + ((m.x21 - m.x30)**2 + (m.x100 -
    m.x109)**2 + (m.x179 - m.x188)**2)**(-3) * (((m.x21 - m.x30)**2 + (m.x100
    - m.x109)**2 + (m.x179 - m.x188)**2)**(-3) - 2) + ((m.x21 - m.x31)**2 + (
    m.x100 - m.x110)**2 + (m.x179 - m.x189)**2)**(-3) * (((m.x21 - m.x31)**2 +
    (m.x100 - m.x110)**2 + (m.x179 - m.x189)**2)**(-3) - 2) + ((m.x21 - m.x32)
    **2 + (m.x100 - m.x111)**2 + (m.x179 - m.x190)**2)**(-3) * (((m.x21 - m.x32)
    **2 + (m.x100 - m.x111)**2 + (m.x179 - m.x190)**2)**(-3) - 2) + ((m.x21 -
    m.x33)**2 + (m.x100 - m.x112)**2 + (m.x179 - m.x191)**2)**(-3) * (((m.x21
    - m.x33)**2 + (m.x100 - m.x112)**2 + (m.x179 - m.x191)**2)**(-3) - 2) + ((
    m.x21 - m.x34)**2 + (m.x100 - m.x113)**2 + (m.x179 - m.x192)**2)**(-3) * ((
    (m.x21 - m.x34)**2 + (m.x100 - m.x113)**2 + (m.x179 - m.x192)**2)**(-3) - 2)
    + ((m.x21 - m.x35)**2 + (m.x100 - m.x114)**2 + (m.x179 - m.x193)**2)**(-3)
    * (((m.x21 - m.x35)**2 + (m.x100 - m.x114)**2 + (m.x179 - m.x193)**2)**(-3)
    - 2) + ((m.x21 - m.x36)**2 + (m.x100 - m.x115)**2 + (m.x179 - m.x194)**2)
    **(-3) * (((m.x21 - m.x36)**2 + (m.x100 - m.x115)**2 + (m.x179 - m.x194)**2)
    **(-3) - 2) + ((m.x21 - m.x37)**2 + (m.x100 - m.x116)**2 + (m.x179 - m.x195)
    **2)**(-3) * (((m.x21 - m.x37)**2 + (m.x100 - m.x116)**2 + (m.x179 - m.x195)
    **2)**(-3) - 2) + ((m.x21 - m.x38)**2 + (m.x100 - m.x117)**2 + (m.x179 -
    m.x196)**2)**(-3) * (((m.x21 - m.x38)**2 + (m.x100 - m.x117)**2 + (m.x179
    - m.x196)**2)**(-3) - 2) + ((m.x21 - m.x39)**2 + (m.x100 - m.x118)**2 + (
    m.x179 - m.x197)**2)**(-3) * (((m.x21 - m.x39)**2 + (m.x100 - m.x118)**2 +
    (m.x179 - m.x197)**2)**(-3) - 2) + ((m.x21 - m.x40)**2 + (m.x100 - m.x119)
    **2 + (m.x179 - m.x198)**2)**(-3) * (((m.x21 - m.x40)**2 + (m.x100 - m.x119)
    **2 + (m.x179 - m.x198)**2)**(-3) - 2) + ((m.x21 - m.x41)**2 + (m.x100 -
    m.x120)**2 + (m.x179 - m.x199)**2)**(-3) * (((m.x21 - m.x41)**2 + (m.x100
    - m.x120)**2 + (m.x179 - m.x199)**2)**(-3) - 2) + ((m.x21 - m.x42)**2 + (
    m.x100 - m.x121)**2 + (m.x179 - m.x200)**2)**(-3) * (((m.x21 - m.x42)**2 +
    (m.x100 - m.x121)**2 + (m.x179 - m.x200)**2)**(-3) - 2) + ((m.x21 - m.x43)
    **2 + (m.x100 - m.x122)**2 + (m.x179 - m.x201)**2)**(-3) * (((m.x21 - m.x43)
    **2 + (m.x100 - m.x122)**2 + (m.x179 - m.x201)**2)**(-3) - 2) + ((m.x21 -
    m.x44)**2 + (m.x100 - m.x123)**2 + (m.x179 - m.x202)**2)**(-3) * (((m.x21
    - m.x44)**2 + (m.x100 - m.x123)**2 + (m.x179 - m.x202)**2)**(-3) - 2) + ((
    m.x21 - m.x45)**2 + (m.x100 - m.x124)**2 + (m.x179 - m.x203)**2)**(-3) * ((
    (m.x21 - m.x45)**2 + (m.x100 - m.x124)**2 + (m.x179 - m.x203)**2)**(-3) - 2)
    + ((m.x21 - m.x46)**2 + (m.x100 - m.x125)**2 + (m.x179 - m.x204)**2)**(-3)
    * (((m.x21 - m.x46)**2 + (m.x100 - m.x125)**2 + (m.x179 - m.x204)**2)**(-3)
    - 2) + ((m.x21 - m.x47)**2 + (m.x100 - m.x126)**2 + (m.x179 - m.x205)**2)
    **(-3) * (((m.x21 - m.x47)**2 + (m.x100 - m.x126)**2 + (m.x179 - m.x205)**2)
    **(-3) - 2) + ((m.x21 - m.x48)**2 + (m.x100 - m.x127)**2 + (m.x179 - m.x206)
    **2)**(-3) * (((m.x21 - m.x48)**2 + (m.x100 - m.x127)**2 + (m.x179 - m.x206)
    **2)**(-3) - 2) + ((m.x21 - m.x49)**2 + (m.x100 - m.x128)**2 + (m.x179 -
    m.x207)**2)**(-3) * (((m.x21 - m.x49)**2 + (m.x100 - m.x128)**2 + (m.x179
    - m.x207)**2)**(-3) - 2) + ((m.x21 - m.x50)**2 + (m.x100 - m.x129)**2 + (
    m.x179 - m.x208)**2)**(-3) * (((m.x21 - m.x50)**2 + (m.x100 - m.x129)**2 +
    (m.x179 - m.x208)**2)**(-3) - 2) + ((m.x21 - m.x51)**2 + (m.x100 - m.x130)
    **2 + (m.x179 - m.x209)**2)**(-3) * (((m.x21 - m.x51)**2 + (m.x100 - m.x130)
    **2 + (m.x179 - m.x209)**2)**(-3) - 2) + ((m.x21 - m.x52)**2 + (m.x100 -
    m.x131)**2 + (m.x179 - m.x210)**2)**(-3) * (((m.x21 - m.x52)**2 + (m.x100
    - m.x131)**2 + (m.x179 - m.x210)**2)**(-3) - 2) + ((m.x21 - m.x53)**2 + (
    m.x100 - m.x132)**2 + (m.x179 - m.x211)**2)**(-3) * (((m.x21 - m.x53)**2 +
    (m.x100 - m.x132)**2 + (m.x179 - m.x211)**2)**(-3) - 2) + ((m.x21 - m.x54)
    **2 + (m.x100 - m.x133)**2 + (m.x179 - m.x212)**2)**(-3) * (((m.x21 - m.x54)
    **2 + (m.x100 - m.x133)**2 + (m.x179 - m.x212)**2)**(-3) - 2) + ((m.x21 -
    m.x55)**2 + (m.x100 - m.x134)**2 + (m.x179 - m.x213)**2)**(-3) * (((m.x21
    - m.x55)**2 + (m.x100 - m.x134)**2 + (m.x179 - m.x213)**2)**(-3) - 2) + ((
    m.x21 - m.x56)**2 + (m.x100 - m.x135)**2 + (m.x179 - m.x214)**2)**(-3) * ((
    (m.x21 - m.x56)**2 + (m.x100 - m.x135)**2 + (m.x179 - m.x214)**2)**(-3) - 2)
    + ((m.x21 - m.x57)**2 + (m.x100 - m.x136)**2 + (m.x179 - m.x215)**2)**(-3)
    * (((m.x21 - m.x57)**2 + (m.x100 - m.x136)**2 + (m.x179 - m.x215)**2)**(-3)
    - 2) + ((m.x21 - m.x58)**2 + (m.x100 - m.x137)**2 + (m.x179 - m.x216)**2)
    **(-3) * (((m.x21 - m.x58)**2 + (m.x100 - m.x137)**2 + (m.x179 - m.x216)**2)
    **(-3) - 2) + ((m.x21 - m.x59)**2 + (m.x100 - m.x138)**2 + (m.x179 - m.x217)
    **2)**(-3) * (((m.x21 - m.x59)**2 + (m.x100 - m.x138)**2 + (m.x179 - m.x217)
    **2)**(-3) - 2) + ((m.x21 - m.x60)**2 + (m.x100 - m.x139)**2 + (m.x179 -
    m.x218)**2)**(-3) * (((m.x21 - m.x60)**2 + (m.x100 - m.x139)**2 + (m.x179
    - m.x218)**2)**(-3) - 2) + ((m.x21 - m.x61)**2 + (m.x100 - m.x140)**2 + (
    m.x179 - m.x219)**2)**(-3) * (((m.x21 - m.x61)**2 + (m.x100 - m.x140)**2 +
    (m.x179 - m.x219)**2)**(-3) - 2) + ((m.x21 - m.x62)**2 + (m.x100 - m.x141)
    **2 + (m.x179 - m.x220)**2)**(-3) * (((m.x21 - m.x62)**2 + (m.x100 - m.x141)
    **2 + (m.x179 - m.x220)**2)**(-3) - 2) + ((m.x21 - m.x63)**2 + (m.x100 -
    m.x142)**2 + (m.x179 - m.x221)**2)**(-3) * (((m.x21 - m.x63)**2 + (m.x100
    - m.x142)**2 + (m.x179 - m.x221)**2)**(-3) - 2) + ((m.x21 - m.x64)**2 + (
    m.x100 - m.x143)**2 + (m.x179 - m.x222)**2)**(-3) * (((m.x21 - m.x64)**2 +
    (m.x100 - m.x143)**2 + (m.x179 - m.x222)**2)**(-3) - 2) + ((m.x21 - m.x65)
    **2 + (m.x100 - m.x144)**2 + (m.x179 - m.x223)**2)**(-3) * (((m.x21 - m.x65)
    **2 + (m.x100 - m.x144)**2 + (m.x179 - m.x223)**2)**(-3) - 2) + ((m.x21 -
    m.x66)**2 + (m.x100 - m.x145)**2 + (m.x179 - m.x224)**2)**(-3) * (((m.x21
    - m.x66)**2 + (m.x100 - m.x145)**2 + (m.x179 - m.x224)**2)**(-3) - 2) + ((
    m.x21 - m.x67)**2 + (m.x100 - m.x146)**2 + (m.x179 - m.x225)**2)**(-3) * ((
    (m.x21 - m.x67)**2 + (m.x100 - m.x146)**2 + (m.x179 - m.x225)**2)**(-3) - 2)
    + ((m.x21 - m.x68)**2 + (m.x100 - m.x147)**2 + (m.x179 - m.x226)**2)**(-3)
    * (((m.x21 - m.x68)**2 + (m.x100 - m.x147)**2 + (m.x179 - m.x226)**2)**(-3)
    - 2) + ((m.x21 - m.x69)**2 + (m.x100 - m.x148)**2 + (m.x179 - m.x227)**2)
    **(-3) * (((m.x21 - m.x69)**2 + (m.x100 - m.x148)**2 + (m.x179 - m.x227)**2)
    **(-3) - 2) + ((m.x21 - m.x70)**2 + (m.x100 - m.x149)**2 + (m.x179 - m.x228)
    **2)**(-3) * (((m.x21 - m.x70)**2 + (m.x100 - m.x149)**2 + (m.x179 - m.x228)
    **2)**(-3) - 2) + ((m.x21 - m.x71)**2 + (m.x100 - m.x150)**2 + (m.x179 -
    m.x229)**2)**(-3) * (((m.x21 - m.x71)**2 + (m.x100 - m.x150)**2 + (m.x179
    - m.x229)**2)**(-3) - 2) + ((m.x21 - m.x72)**2 + (m.x100 - m.x151)**2 + (
    m.x179 - m.x230)**2)**(-3) * (((m.x21 - m.x72)**2 + (m.x100 - m.x151)**2 +
    (m.x179 - m.x230)**2)**(-3) - 2) + ((m.x21 - m.x73)**2 + (m.x100 - m.x152)
    **2 + (m.x179 - m.x231)**2)**(-3) * (((m.x21 - m.x73)**2 + (m.x100 - m.x152)
    **2 + (m.x179 - m.x231)**2)**(-3) - 2) + ((m.x21 - m.x74)**2 + (m.x100 -
    m.x153)**2 + (m.x179 - m.x232)**2)**(-3) * (((m.x21 - m.x74)**2 + (m.x100
    - m.x153)**2 + (m.x179 - m.x232)**2)**(-3) - 2) + ((m.x21 - m.x75)**2 + (
    m.x100 - m.x154)**2 + (m.x179 - m.x233)**2)**(-3) * (((m.x21 - m.x75)**2 +
    (m.x100 - m.x154)**2 + (m.x179 - m.x233)**2)**(-3) - 2) + ((m.x21 - m.x76)
    **2 + (m.x100 - m.x155)**2 + (m.x179 - m.x234)**2)**(-3) * (((m.x21 - m.x76)
    **2 + (m.x100 - m.x155)**2 + (m.x179 - m.x234)**2)**(-3) - 2) + ((m.x21 -
    m.x77)**2 + (m.x100 - m.x156)**2 + (m.x179 - m.x235)**2)**(-3) * (((m.x21
    - m.x77)**2 + (m.x100 - m.x156)**2 + (m.x179 - m.x235)**2)**(-3) - 2) + ((
    m.x21 - m.x78)**2 + (m.x100 - m.x157)**2 + (m.x179 - m.x236)**2)**(-3) * ((
    (m.x21 - m.x78)**2 + (m.x100 - m.x157)**2 + (m.x179 - m.x236)**2)**(-3) - 2)
    + ((m.x21 - m.x79)**2 + (m.x100 - m.x158)**2 + (m.x179 - m.x237)**2)**(-3)
    * (((m.x21 - m.x79)**2 + (m.x100 - m.x158)**2 + (m.x179 - m.x237)**2)**(-3)
    - 2) + ((m.x22 - m.x23)**2 + (m.x101 - m.x102)**2 + (m.x180 - m.x181)**2)
    **(-3) * (((m.x22 - m.x23)**2 + (m.x101 - m.x102)**2 + (m.x180 - m.x181)**2)
    **(-3) - 2) + ((m.x22 - m.x24)**2 + (m.x101 - m.x103)**2 + (m.x180 - m.x182)
    **2)**(-3) * (((m.x22 - m.x24)**2 + (m.x101 - m.x103)**2 + (m.x180 - m.x182)
    **2)**(-3) - 2) + ((m.x22 - m.x25)**2 + (m.x101 - m.x104)**2 + (m.x180 -
    m.x183)**2)**(-3) * (((m.x22 - m.x25)**2 + (m.x101 - m.x104)**2 + (m.x180
    - m.x183)**2)**(-3) - 2) + ((m.x22 - m.x26)**2 + (m.x101 - m.x105)**2 + (
    m.x180 - m.x184)**2)**(-3) * (((m.x22 - m.x26)**2 + (m.x101 - m.x105)**2 +
    (m.x180 - m.x184)**2)**(-3) - 2) + ((m.x22 - m.x27)**2 + (m.x101 - m.x106)
    **2 + (m.x180 - m.x185)**2)**(-3) * (((m.x22 - m.x27)**2 + (m.x101 - m.x106)
    **2 + (m.x180 - m.x185)**2)**(-3) - 2) + ((m.x22 - m.x28)**2 + (m.x101 -
    m.x107)**2 + (m.x180 - m.x186)**2)**(-3) * (((m.x22 - m.x28)**2 + (m.x101
    - m.x107)**2 + (m.x180 - m.x186)**2)**(-3) - 2) + ((m.x22 - m.x29)**2 + (
    m.x101 - m.x108)**2 + (m.x180 - m.x187)**2)**(-3) * (((m.x22 - m.x29)**2 +
    (m.x101 - m.x108)**2 + (m.x180 - m.x187)**2)**(-3) - 2) + ((m.x22 - m.x30)
    **2 + (m.x101 - m.x109)**2 + (m.x180 - m.x188)**2)**(-3) * (((m.x22 - m.x30)
    **2 + (m.x101 - m.x109)**2 + (m.x180 - m.x188)**2)**(-3) - 2) + ((m.x22 -
    m.x31)**2 + (m.x101 - m.x110)**2 + (m.x180 - m.x189)**2)**(-3) * (((m.x22
    - m.x31)**2 + (m.x101 - m.x110)**2 + (m.x180 - m.x189)**2)**(-3) - 2) + ((
    m.x22 - m.x32)**2 + (m.x101 - m.x111)**2 + (m.x180 - m.x190)**2)**(-3) * ((
    (m.x22 - m.x32)**2 + (m.x101 - m.x111)**2 + (m.x180 - m.x190)**2)**(-3) - 2)
    + ((m.x22 - m.x33)**2 + (m.x101 - m.x112)**2 + (m.x180 - m.x191)**2)**(-3)
    * (((m.x22 - m.x33)**2 + (m.x101 - m.x112)**2 + (m.x180 - m.x191)**2)**(-3)
    - 2) + ((m.x22 - m.x34)**2 + (m.x101 - m.x113)**2 + (m.x180 - m.x192)**2)
    **(-3) * (((m.x22 - m.x34)**2 + (m.x101 - m.x113)**2 + (m.x180 - m.x192)**2)
    **(-3) - 2) + ((m.x22 - m.x35)**2 + (m.x101 - m.x114)**2 + (m.x180 - m.x193)
    **2)**(-3) * (((m.x22 - m.x35)**2 + (m.x101 - m.x114)**2 + (m.x180 - m.x193)
    **2)**(-3) - 2) + ((m.x22 - m.x36)**2 + (m.x101 - m.x115)**2 + (m.x180 -
    m.x194)**2)**(-3) * (((m.x22 - m.x36)**2 + (m.x101 - m.x115)**2 + (m.x180
    - m.x194)**2)**(-3) - 2) + ((m.x22 - m.x37)**2 + (m.x101 - m.x116)**2 + (
    m.x180 - m.x195)**2)**(-3) * (((m.x22 - m.x37)**2 + (m.x101 - m.x116)**2 +
    (m.x180 - m.x195)**2)**(-3) - 2) + ((m.x22 - m.x38)**2 + (m.x101 - m.x117)
    **2 + (m.x180 - m.x196)**2)**(-3) * (((m.x22 - m.x38)**2 + (m.x101 - m.x117)
    **2 + (m.x180 - m.x196)**2)**(-3) - 2) + ((m.x22 - m.x39)**2 + (m.x101 -
    m.x118)**2 + (m.x180 - m.x197)**2)**(-3) * (((m.x22 - m.x39)**2 + (m.x101
    - m.x118)**2 + (m.x180 - m.x197)**2)**(-3) - 2) + ((m.x22 - m.x40)**2 + (
    m.x101 - m.x119)**2 + (m.x180 - m.x198)**2)**(-3) * (((m.x22 - m.x40)**2 +
    (m.x101 - m.x119)**2 + (m.x180 - m.x198)**2)**(-3) - 2) + ((m.x22 - m.x41)
    **2 + (m.x101 - m.x120)**2 + (m.x180 - m.x199)**2)**(-3) * (((m.x22 - m.x41)
    **2 + (m.x101 - m.x120)**2 + (m.x180 - m.x199)**2)**(-3) - 2) + ((m.x22 -
    m.x42)**2 + (m.x101 - m.x121)**2 + (m.x180 - m.x200)**2)**(-3) * (((m.x22
    - m.x42)**2 + (m.x101 - m.x121)**2 + (m.x180 - m.x200)**2)**(-3) - 2) + ((
    m.x22 - m.x43)**2 + (m.x101 - m.x122)**2 + (m.x180 - m.x201)**2)**(-3) * ((
    (m.x22 - m.x43)**2 + (m.x101 - m.x122)**2 + (m.x180 - m.x201)**2)**(-3) - 2)
    + ((m.x22 - m.x44)**2 + (m.x101 - m.x123)**2 + (m.x180 - m.x202)**2)**(-3)
    * (((m.x22 - m.x44)**2 + (m.x101 - m.x123)**2 + (m.x180 - m.x202)**2)**(-3)
    - 2) + ((m.x22 - m.x45)**2 + (m.x101 - m.x124)**2 + (m.x180 - m.x203)**2)
    **(-3) * (((m.x22 - m.x45)**2 + (m.x101 - m.x124)**2 + (m.x180 - m.x203)**2)
    **(-3) - 2) + ((m.x22 - m.x46)**2 + (m.x101 - m.x125)**2 + (m.x180 - m.x204)
    **2)**(-3) * (((m.x22 - m.x46)**2 + (m.x101 - m.x125)**2 + (m.x180 - m.x204)
    **2)**(-3) - 2) + ((m.x22 - m.x47)**2 + (m.x101 - m.x126)**2 + (m.x180 -
    m.x205)**2)**(-3) * (((m.x22 - m.x47)**2 + (m.x101 - m.x126)**2 + (m.x180
    - m.x205)**2)**(-3) - 2) + ((m.x22 - m.x48)**2 + (m.x101 - m.x127)**2 + (
    m.x180 - m.x206)**2)**(-3) * (((m.x22 - m.x48)**2 + (m.x101 - m.x127)**2 +
    (m.x180 - m.x206)**2)**(-3) - 2) + ((m.x22 - m.x49)**2 + (m.x101 - m.x128)
    **2 + (m.x180 - m.x207)**2)**(-3) * (((m.x22 - m.x49)**2 + (m.x101 - m.x128)
    **2 + (m.x180 - m.x207)**2)**(-3) - 2) + ((m.x22 - m.x50)**2 + (m.x101 -
    m.x129)**2 + (m.x180 - m.x208)**2)**(-3) * (((m.x22 - m.x50)**2 + (m.x101
    - m.x129)**2 + (m.x180 - m.x208)**2)**(-3) - 2) + ((m.x22 - m.x51)**2 + (
    m.x101 - m.x130)**2 + (m.x180 - m.x209)**2)**(-3) * (((m.x22 - m.x51)**2 +
    (m.x101 - m.x130)**2 + (m.x180 - m.x209)**2)**(-3) - 2) + ((m.x22 - m.x52)
    **2 + (m.x101 - m.x131)**2 + (m.x180 - m.x210)**2)**(-3) * (((m.x22 - m.x52)
    **2 + (m.x101 - m.x131)**2 + (m.x180 - m.x210)**2)**(-3) - 2) + ((m.x22 -
    m.x53)**2 + (m.x101 - m.x132)**2 + (m.x180 - m.x211)**2)**(-3) * (((m.x22
    - m.x53)**2 + (m.x101 - m.x132)**2 + (m.x180 - m.x211)**2)**(-3) - 2) + ((
    m.x22 - m.x54)**2 + (m.x101 - m.x133)**2 + (m.x180 - m.x212)**2)**(-3) * ((
    (m.x22 - m.x54)**2 + (m.x101 - m.x133)**2 + (m.x180 - m.x212)**2)**(-3) - 2)
    + ((m.x22 - m.x55)**2 + (m.x101 - m.x134)**2 + (m.x180 - m.x213)**2)**(-3)
    * (((m.x22 - m.x55)**2 + (m.x101 - m.x134)**2 + (m.x180 - m.x213)**2)**(-3)
    - 2) + ((m.x22 - m.x56)**2 + (m.x101 - m.x135)**2 + (m.x180 - m.x214)**2)
    **(-3) * (((m.x22 - m.x56)**2 + (m.x101 - m.x135)**2 + (m.x180 - m.x214)**2)
    **(-3) - 2) + ((m.x22 - m.x57)**2 + (m.x101 - m.x136)**2 + (m.x180 - m.x215)
    **2)**(-3) * (((m.x22 - m.x57)**2 + (m.x101 - m.x136)**2 + (m.x180 - m.x215)
    **2)**(-3) - 2) + ((m.x22 - m.x58)**2 + (m.x101 - m.x137)**2 + (m.x180 -
    m.x216)**2)**(-3) * (((m.x22 - m.x58)**2 + (m.x101 - m.x137)**2 + (m.x180
    - m.x216)**2)**(-3) - 2) + ((m.x22 - m.x59)**2 + (m.x101 - m.x138)**2 + (
    m.x180 - m.x217)**2)**(-3) * (((m.x22 - m.x59)**2 + (m.x101 - m.x138)**2 +
    (m.x180 - m.x217)**2)**(-3) - 2) + ((m.x22 - m.x60)**2 + (m.x101 - m.x139)
    **2 + (m.x180 - m.x218)**2)**(-3) * (((m.x22 - m.x60)**2 + (m.x101 - m.x139)
    **2 + (m.x180 - m.x218)**2)**(-3) - 2) + ((m.x22 - m.x61)**2 + (m.x101 -
    m.x140)**2 + (m.x180 - m.x219)**2)**(-3) * (((m.x22 - m.x61)**2 + (m.x101
    - m.x140)**2 + (m.x180 - m.x219)**2)**(-3) - 2) + ((m.x22 - m.x62)**2 + (
    m.x101 - m.x141)**2 + (m.x180 - m.x220)**2)**(-3) * (((m.x22 - m.x62)**2 +
    (m.x101 - m.x141)**2 + (m.x180 - m.x220)**2)**(-3) - 2) + ((m.x22 - m.x63)
    **2 + (m.x101 - m.x142)**2 + (m.x180 - m.x221)**2)**(-3) * (((m.x22 - m.x63)
    **2 + (m.x101 - m.x142)**2 + (m.x180 - m.x221)**2)**(-3) - 2) + ((m.x22 -
    m.x64)**2 + (m.x101 - m.x143)**2 + (m.x180 - m.x222)**2)**(-3) * (((m.x22
    - m.x64)**2 + (m.x101 - m.x143)**2 + (m.x180 - m.x222)**2)**(-3) - 2) + ((
    m.x22 - m.x65)**2 + (m.x101 - m.x144)**2 + (m.x180 - m.x223)**2)**(-3) * ((
    (m.x22 - m.x65)**2 + (m.x101 - m.x144)**2 + (m.x180 - m.x223)**2)**(-3) - 2)
    + ((m.x22 - m.x66)**2 + (m.x101 - m.x145)**2 + (m.x180 - m.x224)**2)**(-3)
    * (((m.x22 - m.x66)**2 + (m.x101 - m.x145)**2 + (m.x180 - m.x224)**2)**(-3)
    - 2) + ((m.x22 - m.x67)**2 + (m.x101 - m.x146)**2 + (m.x180 - m.x225)**2)
    **(-3) * (((m.x22 - m.x67)**2 + (m.x101 - m.x146)**2 + (m.x180 - m.x225)**2)
    **(-3) - 2) + ((m.x22 - m.x68)**2 + (m.x101 - m.x147)**2 + (m.x180 - m.x226)
    **2)**(-3) * (((m.x22 - m.x68)**2 + (m.x101 - m.x147)**2 + (m.x180 - m.x226)
    **2)**(-3) - 2) + ((m.x22 - m.x69)**2 + (m.x101 - m.x148)**2 + (m.x180 -
    m.x227)**2)**(-3) * (((m.x22 - m.x69)**2 + (m.x101 - m.x148)**2 + (m.x180
    - m.x227)**2)**(-3) - 2) + ((m.x22 - m.x70)**2 + (m.x101 - m.x149)**2 + (
    m.x180 - m.x228)**2)**(-3) * (((m.x22 - m.x70)**2 + (m.x101 - m.x149)**2 +
    (m.x180 - m.x228)**2)**(-3) - 2) + ((m.x22 - m.x71)**2 + (m.x101 - m.x150)
    **2 + (m.x180 - m.x229)**2)**(-3) * (((m.x22 - m.x71)**2 + (m.x101 - m.x150)
    **2 + (m.x180 - m.x229)**2)**(-3) - 2) + ((m.x22 - m.x72)**2 + (m.x101 -
    m.x151)**2 + (m.x180 - m.x230)**2)**(-3) * (((m.x22 - m.x72)**2 + (m.x101
    - m.x151)**2 + (m.x180 - m.x230)**2)**(-3) - 2) + ((m.x22 - m.x73)**2 + (
    m.x101 - m.x152)**2 + (m.x180 - m.x231)**2)**(-3) * (((m.x22 - m.x73)**2 +
    (m.x101 - m.x152)**2 + (m.x180 - m.x231)**2)**(-3) - 2) + ((m.x22 - m.x74)
    **2 + (m.x101 - m.x153)**2 + (m.x180 - m.x232)**2)**(-3) * (((m.x22 - m.x74)
    **2 + (m.x101 - m.x153)**2 + (m.x180 - m.x232)**2)**(-3) - 2) + ((m.x22 -
    m.x75)**2 + (m.x101 - m.x154)**2 + (m.x180 - m.x233)**2)**(-3) * (((m.x22
    - m.x75)**2 + (m.x101 - m.x154)**2 + (m.x180 - m.x233)**2)**(-3) - 2) + ((
    m.x22 - m.x76)**2 + (m.x101 - m.x155)**2 + (m.x180 - m.x234)**2)**(-3) * ((
    (m.x22 - m.x76)**2 + (m.x101 - m.x155)**2 + (m.x180 - m.x234)**2)**(-3) - 2)
    + ((m.x22 - m.x77)**2 + (m.x101 - m.x156)**2 + (m.x180 - m.x235)**2)**(-3)
    * (((m.x22 - m.x77)**2 + (m.x101 - m.x156)**2 + (m.x180 - m.x235)**2)**(-3)
    - 2) + ((m.x22 - m.x78)**2 + (m.x101 - m.x157)**2 + (m.x180 - m.x236)**2)
    **(-3) * (((m.x22 - m.x78)**2 + (m.x101 - m.x157)**2 + (m.x180 - m.x236)**2)
    **(-3) - 2) + ((m.x22 - m.x79)**2 + (m.x101 - m.x158)**2 + (m.x180 - m.x237)
    **2)**(-3) * (((m.x22 - m.x79)**2 + (m.x101 - m.x158)**2 + (m.x180 - m.x237)
    **2)**(-3) - 2) + ((m.x23 - m.x24)**2 + (m.x102 - m.x103)**2 + (m.x181 -
    m.x182)**2)**(-3) * (((m.x23 - m.x24)**2 + (m.x102 - m.x103)**2 + (m.x181
    - m.x182)**2)**(-3) - 2) + ((m.x23 - m.x25)**2 + (m.x102 - m.x104)**2 + (
    m.x181 - m.x183)**2)**(-3) * (((m.x23 - m.x25)**2 + (m.x102 - m.x104)**2 +
    (m.x181 - m.x183)**2)**(-3) - 2) + ((m.x23 - m.x26)**2 + (m.x102 - m.x105)
    **2 + (m.x181 - m.x184)**2)**(-3) * (((m.x23 - m.x26)**2 + (m.x102 - m.x105)
    **2 + (m.x181 - m.x184)**2)**(-3) - 2) + ((m.x23 - m.x27)**2 + (m.x102 -
    m.x106)**2 + (m.x181 - m.x185)**2)**(-3) * (((m.x23 - m.x27)**2 + (m.x102
    - m.x106)**2 + (m.x181 - m.x185)**2)**(-3) - 2) + ((m.x23 - m.x28)**2 + (
    m.x102 - m.x107)**2 + (m.x181 - m.x186)**2)**(-3) * (((m.x23 - m.x28)**2 +
    (m.x102 - m.x107)**2 + (m.x181 - m.x186)**2)**(-3) - 2) + ((m.x23 - m.x29)
    **2 + (m.x102 - m.x108)**2 + (m.x181 - m.x187)**2)**(-3) * (((m.x23 - m.x29)
    **2 + (m.x102 - m.x108)**2 + (m.x181 - m.x187)**2)**(-3) - 2) + ((m.x23 -
    m.x30)**2 + (m.x102 - m.x109)**2 + (m.x181 - m.x188)**2)**(-3) * (((m.x23
    - m.x30)**2 + (m.x102 - m.x109)**2 + (m.x181 - m.x188)**2)**(-3) - 2) + ((
    m.x23 - m.x31)**2 + (m.x102 - m.x110)**2 + (m.x181 - m.x189)**2)**(-3) * ((
    (m.x23 - m.x31)**2 + (m.x102 - m.x110)**2 + (m.x181 - m.x189)**2)**(-3) - 2)
    + ((m.x23 - m.x32)**2 + (m.x102 - m.x111)**2 + (m.x181 - m.x190)**2)**(-3)
    * (((m.x23 - m.x32)**2 + (m.x102 - m.x111)**2 + (m.x181 - m.x190)**2)**(-3)
    - 2) + ((m.x23 - m.x33)**2 + (m.x102 - m.x112)**2 + (m.x181 - m.x191)**2)
    **(-3) * (((m.x23 - m.x33)**2 + (m.x102 - m.x112)**2 + (m.x181 - m.x191)**2)
    **(-3) - 2) + ((m.x23 - m.x34)**2 + (m.x102 - m.x113)**2 + (m.x181 - m.x192)
    **2)**(-3) * (((m.x23 - m.x34)**2 + (m.x102 - m.x113)**2 + (m.x181 - m.x192)
    **2)**(-3) - 2) + ((m.x23 - m.x35)**2 + (m.x102 - m.x114)**2 + (m.x181 -
    m.x193)**2)**(-3) * (((m.x23 - m.x35)**2 + (m.x102 - m.x114)**2 + (m.x181
    - m.x193)**2)**(-3) - 2) + ((m.x23 - m.x36)**2 + (m.x102 - m.x115)**2 + (
    m.x181 - m.x194)**2)**(-3) * (((m.x23 - m.x36)**2 + (m.x102 - m.x115)**2 +
    (m.x181 - m.x194)**2)**(-3) - 2) + ((m.x23 - m.x37)**2 + (m.x102 - m.x116)
    **2 + (m.x181 - m.x195)**2)**(-3) * (((m.x23 - m.x37)**2 + (m.x102 - m.x116)
    **2 + (m.x181 - m.x195)**2)**(-3) - 2) + ((m.x23 - m.x38)**2 + (m.x102 -
    m.x117)**2 + (m.x181 - m.x196)**2)**(-3) * (((m.x23 - m.x38)**2 + (m.x102
    - m.x117)**2 + (m.x181 - m.x196)**2)**(-3) - 2) + ((m.x23 - m.x39)**2 + (
    m.x102 - m.x118)**2 + (m.x181 - m.x197)**2)**(-3) * (((m.x23 - m.x39)**2 +
    (m.x102 - m.x118)**2 + (m.x181 - m.x197)**2)**(-3) - 2) + ((m.x23 - m.x40)
    **2 + (m.x102 - m.x119)**2 + (m.x181 - m.x198)**2)**(-3) * (((m.x23 - m.x40)
    **2 + (m.x102 - m.x119)**2 + (m.x181 - m.x198)**2)**(-3) - 2) + ((m.x23 -
    m.x41)**2 + (m.x102 - m.x120)**2 + (m.x181 - m.x199)**2)**(-3) * (((m.x23
    - m.x41)**2 + (m.x102 - m.x120)**2 + (m.x181 - m.x199)**2)**(-3) - 2) + ((
    m.x23 - m.x42)**2 + (m.x102 - m.x121)**2 + (m.x181 - m.x200)**2)**(-3) * ((
    (m.x23 - m.x42)**2 + (m.x102 - m.x121)**2 + (m.x181 - m.x200)**2)**(-3) - 2)
    + ((m.x23 - m.x43)**2 + (m.x102 - m.x122)**2 + (m.x181 - m.x201)**2)**(-3)
    * (((m.x23 - m.x43)**2 + (m.x102 - m.x122)**2 + (m.x181 - m.x201)**2)**(-3)
    - 2) + ((m.x23 - m.x44)**2 + (m.x102 - m.x123)**2 + (m.x181 - m.x202)**2)
    **(-3) * (((m.x23 - m.x44)**2 + (m.x102 - m.x123)**2 + (m.x181 - m.x202)**2)
    **(-3) - 2) + ((m.x23 - m.x45)**2 + (m.x102 - m.x124)**2 + (m.x181 - m.x203)
    **2)**(-3) * (((m.x23 - m.x45)**2 + (m.x102 - m.x124)**2 + (m.x181 - m.x203)
    **2)**(-3) - 2) + ((m.x23 - m.x46)**2 + (m.x102 - m.x125)**2 + (m.x181 -
    m.x204)**2)**(-3) * (((m.x23 - m.x46)**2 + (m.x102 - m.x125)**2 + (m.x181
    - m.x204)**2)**(-3) - 2) + ((m.x23 - m.x47)**2 + (m.x102 - m.x126)**2 + (
    m.x181 - m.x205)**2)**(-3) * (((m.x23 - m.x47)**2 + (m.x102 - m.x126)**2 +
    (m.x181 - m.x205)**2)**(-3) - 2) + ((m.x23 - m.x48)**2 + (m.x102 - m.x127)
    **2 + (m.x181 - m.x206)**2)**(-3) * (((m.x23 - m.x48)**2 + (m.x102 - m.x127)
    **2 + (m.x181 - m.x206)**2)**(-3) - 2) + ((m.x23 - m.x49)**2 + (m.x102 -
    m.x128)**2 + (m.x181 - m.x207)**2)**(-3) * (((m.x23 - m.x49)**2 + (m.x102
    - m.x128)**2 + (m.x181 - m.x207)**2)**(-3) - 2) + ((m.x23 - m.x50)**2 + (
    m.x102 - m.x129)**2 + (m.x181 - m.x208)**2)**(-3) * (((m.x23 - m.x50)**2 +
    (m.x102 - m.x129)**2 + (m.x181 - m.x208)**2)**(-3) - 2) + ((m.x23 - m.x51)
    **2 + (m.x102 - m.x130)**2 + (m.x181 - m.x209)**2)**(-3) * (((m.x23 - m.x51)
    **2 + (m.x102 - m.x130)**2 + (m.x181 - m.x209)**2)**(-3) - 2) + ((m.x23 -
    m.x52)**2 + (m.x102 - m.x131)**2 + (m.x181 - m.x210)**2)**(-3) * (((m.x23
    - m.x52)**2 + (m.x102 - m.x131)**2 + (m.x181 - m.x210)**2)**(-3) - 2) + ((
    m.x23 - m.x53)**2 + (m.x102 - m.x132)**2 + (m.x181 - m.x211)**2)**(-3) * ((
    (m.x23 - m.x53)**2 + (m.x102 - m.x132)**2 + (m.x181 - m.x211)**2)**(-3) - 2)
    + ((m.x23 - m.x54)**2 + (m.x102 - m.x133)**2 + (m.x181 - m.x212)**2)**(-3)
    * (((m.x23 - m.x54)**2 + (m.x102 - m.x133)**2 + (m.x181 - m.x212)**2)**(-3)
    - 2) + ((m.x23 - m.x55)**2 + (m.x102 - m.x134)**2 + (m.x181 - m.x213)**2)
    **(-3) * (((m.x23 - m.x55)**2 + (m.x102 - m.x134)**2 + (m.x181 - m.x213)**2)
    **(-3) - 2) + ((m.x23 - m.x56)**2 + (m.x102 - m.x135)**2 + (m.x181 - m.x214)
    **2)**(-3) * (((m.x23 - m.x56)**2 + (m.x102 - m.x135)**2 + (m.x181 - m.x214)
    **2)**(-3) - 2) + ((m.x23 - m.x57)**2 + (m.x102 - m.x136)**2 + (m.x181 -
    m.x215)**2)**(-3) * (((m.x23 - m.x57)**2 + (m.x102 - m.x136)**2 + (m.x181
    - m.x215)**2)**(-3) - 2) + ((m.x23 - m.x58)**2 + (m.x102 - m.x137)**2 + (
    m.x181 - m.x216)**2)**(-3) * (((m.x23 - m.x58)**2 + (m.x102 - m.x137)**2 +
    (m.x181 - m.x216)**2)**(-3) - 2) + ((m.x23 - m.x59)**2 + (m.x102 - m.x138)
    **2 + (m.x181 - m.x217)**2)**(-3) * (((m.x23 - m.x59)**2 + (m.x102 - m.x138)
    **2 + (m.x181 - m.x217)**2)**(-3) - 2) + ((m.x23 - m.x60)**2 + (m.x102 -
    m.x139)**2 + (m.x181 - m.x218)**2)**(-3) * (((m.x23 - m.x60)**2 + (m.x102
    - m.x139)**2 + (m.x181 - m.x218)**2)**(-3) - 2) + ((m.x23 - m.x61)**2 + (
    m.x102 - m.x140)**2 + (m.x181 - m.x219)**2)**(-3) * (((m.x23 - m.x61)**2 +
    (m.x102 - m.x140)**2 + (m.x181 - m.x219)**2)**(-3) - 2) + ((m.x23 - m.x62)
    **2 + (m.x102 - m.x141)**2 + (m.x181 - m.x220)**2)**(-3) * (((m.x23 - m.x62)
    **2 + (m.x102 - m.x141)**2 + (m.x181 - m.x220)**2)**(-3) - 2) + ((m.x23 -
    m.x63)**2 + (m.x102 - m.x142)**2 + (m.x181 - m.x221)**2)**(-3) * (((m.x23
    - m.x63)**2 + (m.x102 - m.x142)**2 + (m.x181 - m.x221)**2)**(-3) - 2) + ((
    m.x23 - m.x64)**2 + (m.x102 - m.x143)**2 + (m.x181 - m.x222)**2)**(-3) * ((
    (m.x23 - m.x64)**2 + (m.x102 - m.x143)**2 + (m.x181 - m.x222)**2)**(-3) - 2)
    + ((m.x23 - m.x65)**2 + (m.x102 - m.x144)**2 + (m.x181 - m.x223)**2)**(-3)
    * (((m.x23 - m.x65)**2 + (m.x102 - m.x144)**2 + (m.x181 - m.x223)**2)**(-3)
    - 2) + ((m.x23 - m.x66)**2 + (m.x102 - m.x145)**2 + (m.x181 - m.x224)**2)
    **(-3) * (((m.x23 - m.x66)**2 + (m.x102 - m.x145)**2 + (m.x181 - m.x224)**2)
    **(-3) - 2) + ((m.x23 - m.x67)**2 + (m.x102 - m.x146)**2 + (m.x181 - m.x225)
    **2)**(-3) * (((m.x23 - m.x67)**2 + (m.x102 - m.x146)**2 + (m.x181 - m.x225)
    **2)**(-3) - 2) + ((m.x23 - m.x68)**2 + (m.x102 - m.x147)**2 + (m.x181 -
    m.x226)**2)**(-3) * (((m.x23 - m.x68)**2 + (m.x102 - m.x147)**2 + (m.x181
    - m.x226)**2)**(-3) - 2) + ((m.x23 - m.x69)**2 + (m.x102 - m.x148)**2 + (
    m.x181 - m.x227)**2)**(-3) * (((m.x23 - m.x69)**2 + (m.x102 - m.x148)**2 +
    (m.x181 - m.x227)**2)**(-3) - 2) + ((m.x23 - m.x70)**2 + (m.x102 - m.x149)
    **2 + (m.x181 - m.x228)**2)**(-3) * (((m.x23 - m.x70)**2 + (m.x102 - m.x149)
    **2 + (m.x181 - m.x228)**2)**(-3) - 2) + ((m.x23 - m.x71)**2 + (m.x102 -
    m.x150)**2 + (m.x181 - m.x229)**2)**(-3) * (((m.x23 - m.x71)**2 + (m.x102
    - m.x150)**2 + (m.x181 - m.x229)**2)**(-3) - 2) + ((m.x23 - m.x72)**2 + (
    m.x102 - m.x151)**2 + (m.x181 - m.x230)**2)**(-3) * (((m.x23 - m.x72)**2 +
    (m.x102 - m.x151)**2 + (m.x181 - m.x230)**2)**(-3) - 2) + ((m.x23 - m.x73)
    **2 + (m.x102 - m.x152)**2 + (m.x181 - m.x231)**2)**(-3) * (((m.x23 - m.x73)
    **2 + (m.x102 - m.x152)**2 + (m.x181 - m.x231)**2)**(-3) - 2) + ((m.x23 -
    m.x74)**2 + (m.x102 - m.x153)**2 + (m.x181 - m.x232)**2)**(-3) * (((m.x23
    - m.x74)**2 + (m.x102 - m.x153)**2 + (m.x181 - m.x232)**2)**(-3) - 2) + ((
    m.x23 - m.x75)**2 + (m.x102 - m.x154)**2 + (m.x181 - m.x233)**2)**(-3) * ((
    (m.x23 - m.x75)**2 + (m.x102 - m.x154)**2 + (m.x181 - m.x233)**2)**(-3) - 2)
    + ((m.x23 - m.x76)**2 + (m.x102 - m.x155)**2 + (m.x181 - m.x234)**2)**(-3)
    * (((m.x23 - m.x76)**2 + (m.x102 - m.x155)**2 + (m.x181 - m.x234)**2)**(-3)
    - 2) + ((m.x23 - m.x77)**2 + (m.x102 - m.x156)**2 + (m.x181 - m.x235)**2)
    **(-3) * (((m.x23 - m.x77)**2 + (m.x102 - m.x156)**2 + (m.x181 - m.x235)**2)
    **(-3) - 2) + ((m.x23 - m.x78)**2 + (m.x102 - m.x157)**2 + (m.x181 - m.x236)
    **2)**(-3) * (((m.x23 - m.x78)**2 + (m.x102 - m.x157)**2 + (m.x181 - m.x236)
    **2)**(-3) - 2) + ((m.x23 - m.x79)**2 + (m.x102 - m.x158)**2 + (m.x181 -
    m.x237)**2)**(-3) * (((m.x23 - m.x79)**2 + (m.x102 - m.x158)**2 + (m.x181
    - m.x237)**2)**(-3) - 2) + ((m.x24 - m.x25)**2 + (m.x103 - m.x104)**2 + (
    m.x182 - m.x183)**2)**(-3) * (((m.x24 - m.x25)**2 + (m.x103 - m.x104)**2 +
    (m.x182 - m.x183)**2)**(-3) - 2) + ((m.x24 - m.x26)**2 + (m.x103 - m.x105)
    **2 + (m.x182 - m.x184)**2)**(-3) * (((m.x24 - m.x26)**2 + (m.x103 - m.x105)
    **2 + (m.x182 - m.x184)**2)**(-3) - 2) + ((m.x24 - m.x27)**2 + (m.x103 -
    m.x106)**2 + (m.x182 - m.x185)**2)**(-3) * (((m.x24 - m.x27)**2 + (m.x103
    - m.x106)**2 + (m.x182 - m.x185)**2)**(-3) - 2) + ((m.x24 - m.x28)**2 + (
    m.x103 - m.x107)**2 + (m.x182 - m.x186)**2)**(-3) * (((m.x24 - m.x28)**2 +
    (m.x103 - m.x107)**2 + (m.x182 - m.x186)**2)**(-3) - 2) + ((m.x24 - m.x29)
    **2 + (m.x103 - m.x108)**2 + (m.x182 - m.x187)**2)**(-3) * (((m.x24 - m.x29)
    **2 + (m.x103 - m.x108)**2 + (m.x182 - m.x187)**2)**(-3) - 2) + ((m.x24 -
    m.x30)**2 + (m.x103 - m.x109)**2 + (m.x182 - m.x188)**2)**(-3) * (((m.x24
    - m.x30)**2 + (m.x103 - m.x109)**2 + (m.x182 - m.x188)**2)**(-3) - 2) + ((
    m.x24 - m.x31)**2 + (m.x103 - m.x110)**2 + (m.x182 - m.x189)**2)**(-3) * ((
    (m.x24 - m.x31)**2 + (m.x103 - m.x110)**2 + (m.x182 - m.x189)**2)**(-3) - 2)
    + ((m.x24 - m.x32)**2 + (m.x103 - m.x111)**2 + (m.x182 - m.x190)**2)**(-3)
    * (((m.x24 - m.x32)**2 + (m.x103 - m.x111)**2 + (m.x182 - m.x190)**2)**(-3)
    - 2) + ((m.x24 - m.x33)**2 + (m.x103 - m.x112)**2 + (m.x182 - m.x191)**2)
    **(-3) * (((m.x24 - m.x33)**2 + (m.x103 - m.x112)**2 + (m.x182 - m.x191)**2)
    **(-3) - 2) + ((m.x24 - m.x34)**2 + (m.x103 - m.x113)**2 + (m.x182 - m.x192)
    **2)**(-3) * (((m.x24 - m.x34)**2 + (m.x103 - m.x113)**2 + (m.x182 - m.x192)
    **2)**(-3) - 2) + ((m.x24 - m.x35)**2 + (m.x103 - m.x114)**2 + (m.x182 -
    m.x193)**2)**(-3) * (((m.x24 - m.x35)**2 + (m.x103 - m.x114)**2 + (m.x182
    - m.x193)**2)**(-3) - 2) + ((m.x24 - m.x36)**2 + (m.x103 - m.x115)**2 + (
    m.x182 - m.x194)**2)**(-3) * (((m.x24 - m.x36)**2 + (m.x103 - m.x115)**2 +
    (m.x182 - m.x194)**2)**(-3) - 2) + ((m.x24 - m.x37)**2 + (m.x103 - m.x116)
    **2 + (m.x182 - m.x195)**2)**(-3) * (((m.x24 - m.x37)**2 + (m.x103 - m.x116)
    **2 + (m.x182 - m.x195)**2)**(-3) - 2) + ((m.x24 - m.x38)**2 + (m.x103 -
    m.x117)**2 + (m.x182 - m.x196)**2)**(-3) * (((m.x24 - m.x38)**2 + (m.x103
    - m.x117)**2 + (m.x182 - m.x196)**2)**(-3) - 2) + ((m.x24 - m.x39)**2 + (
    m.x103 - m.x118)**2 + (m.x182 - m.x197)**2)**(-3) * (((m.x24 - m.x39)**2 +
    (m.x103 - m.x118)**2 + (m.x182 - m.x197)**2)**(-3) - 2) + ((m.x24 - m.x40)
    **2 + (m.x103 - m.x119)**2 + (m.x182 - m.x198)**2)**(-3) * (((m.x24 - m.x40)
    **2 + (m.x103 - m.x119)**2 + (m.x182 - m.x198)**2)**(-3) - 2) + ((m.x24 -
    m.x41)**2 + (m.x103 - m.x120)**2 + (m.x182 - m.x199)**2)**(-3) * (((m.x24
    - m.x41)**2 + (m.x103 - m.x120)**2 + (m.x182 - m.x199)**2)**(-3) - 2) + ((
    m.x24 - m.x42)**2 + (m.x103 - m.x121)**2 + (m.x182 - m.x200)**2)**(-3) * ((
    (m.x24 - m.x42)**2 + (m.x103 - m.x121)**2 + (m.x182 - m.x200)**2)**(-3) - 2)
    + ((m.x24 - m.x43)**2 + (m.x103 - m.x122)**2 + (m.x182 - m.x201)**2)**(-3)
    * (((m.x24 - m.x43)**2 + (m.x103 - m.x122)**2 + (m.x182 - m.x201)**2)**(-3)
    - 2) + ((m.x24 - m.x44)**2 + (m.x103 - m.x123)**2 + (m.x182 - m.x202)**2)
    **(-3) * (((m.x24 - m.x44)**2 + (m.x103 - m.x123)**2 + (m.x182 - m.x202)**2)
    **(-3) - 2) + ((m.x24 - m.x45)**2 + (m.x103 - m.x124)**2 + (m.x182 - m.x203)
    **2)**(-3) * (((m.x24 - m.x45)**2 + (m.x103 - m.x124)**2 + (m.x182 - m.x203)
    **2)**(-3) - 2) + ((m.x24 - m.x46)**2 + (m.x103 - m.x125)**2 + (m.x182 -
    m.x204)**2)**(-3) * (((m.x24 - m.x46)**2 + (m.x103 - m.x125)**2 + (m.x182
    - m.x204)**2)**(-3) - 2) + ((m.x24 - m.x47)**2 + (m.x103 - m.x126)**2 + (
    m.x182 - m.x205)**2)**(-3) * (((m.x24 - m.x47)**2 + (m.x103 - m.x126)**2 +
    (m.x182 - m.x205)**2)**(-3) - 2) + ((m.x24 - m.x48)**2 + (m.x103 - m.x127)
    **2 + (m.x182 - m.x206)**2)**(-3) * (((m.x24 - m.x48)**2 + (m.x103 - m.x127)
    **2 + (m.x182 - m.x206)**2)**(-3) - 2) + ((m.x24 - m.x49)**2 + (m.x103 -
    m.x128)**2 + (m.x182 - m.x207)**2)**(-3) * (((m.x24 - m.x49)**2 + (m.x103
    - m.x128)**2 + (m.x182 - m.x207)**2)**(-3) - 2) + ((m.x24 - m.x50)**2 + (
    m.x103 - m.x129)**2 + (m.x182 - m.x208)**2)**(-3) * (((m.x24 - m.x50)**2 +
    (m.x103 - m.x129)**2 + (m.x182 - m.x208)**2)**(-3) - 2) + ((m.x24 - m.x51)
    **2 + (m.x103 - m.x130)**2 + (m.x182 - m.x209)**2)**(-3) * (((m.x24 - m.x51)
    **2 + (m.x103 - m.x130)**2 + (m.x182 - m.x209)**2)**(-3) - 2) + ((m.x24 -
    m.x52)**2 + (m.x103 - m.x131)**2 + (m.x182 - m.x210)**2)**(-3) * (((m.x24
    - m.x52)**2 + (m.x103 - m.x131)**2 + (m.x182 - m.x210)**2)**(-3) - 2) + ((
    m.x24 - m.x53)**2 + (m.x103 - m.x132)**2 + (m.x182 - m.x211)**2)**(-3) * ((
    (m.x24 - m.x53)**2 + (m.x103 - m.x132)**2 + (m.x182 - m.x211)**2)**(-3) - 2)
    + ((m.x24 - m.x54)**2 + (m.x103 - m.x133)**2 + (m.x182 - m.x212)**2)**(-3)
    * (((m.x24 - m.x54)**2 + (m.x103 - m.x133)**2 + (m.x182 - m.x212)**2)**(-3)
    - 2) + ((m.x24 - m.x55)**2 + (m.x103 - m.x134)**2 + (m.x182 - m.x213)**2)
    **(-3) * (((m.x24 - m.x55)**2 + (m.x103 - m.x134)**2 + (m.x182 - m.x213)**2)
    **(-3) - 2) + ((m.x24 - m.x56)**2 + (m.x103 - m.x135)**2 + (m.x182 - m.x214)
    **2)**(-3) * (((m.x24 - m.x56)**2 + (m.x103 - m.x135)**2 + (m.x182 - m.x214)
    **2)**(-3) - 2) + ((m.x24 - m.x57)**2 + (m.x103 - m.x136)**2 + (m.x182 -
    m.x215)**2)**(-3) * (((m.x24 - m.x57)**2 + (m.x103 - m.x136)**2 + (m.x182
    - m.x215)**2)**(-3) - 2) + ((m.x24 - m.x58)**2 + (m.x103 - m.x137)**2 + (
    m.x182 - m.x216)**2)**(-3) * (((m.x24 - m.x58)**2 + (m.x103 - m.x137)**2 +
    (m.x182 - m.x216)**2)**(-3) - 2) + ((m.x24 - m.x59)**2 + (m.x103 - m.x138)
    **2 + (m.x182 - m.x217)**2)**(-3) * (((m.x24 - m.x59)**2 + (m.x103 - m.x138)
    **2 + (m.x182 - m.x217)**2)**(-3) - 2) + ((m.x24 - m.x60)**2 + (m.x103 -
    m.x139)**2 + (m.x182 - m.x218)**2)**(-3) * (((m.x24 - m.x60)**2 + (m.x103
    - m.x139)**2 + (m.x182 - m.x218)**2)**(-3) - 2) + ((m.x24 - m.x61)**2 + (
    m.x103 - m.x140)**2 + (m.x182 - m.x219)**2)**(-3) * (((m.x24 - m.x61)**2 +
    (m.x103 - m.x140)**2 + (m.x182 - m.x219)**2)**(-3) - 2) + ((m.x24 - m.x62)
    **2 + (m.x103 - m.x141)**2 + (m.x182 - m.x220)**2)**(-3) * (((m.x24 - m.x62)
    **2 + (m.x103 - m.x141)**2 + (m.x182 - m.x220)**2)**(-3) - 2) + ((m.x24 -
    m.x63)**2 + (m.x103 - m.x142)**2 + (m.x182 - m.x221)**2)**(-3) * (((m.x24
    - m.x63)**2 + (m.x103 - m.x142)**2 + (m.x182 - m.x221)**2)**(-3) - 2) + ((
    m.x24 - m.x64)**2 + (m.x103 - m.x143)**2 + (m.x182 - m.x222)**2)**(-3) * ((
    (m.x24 - m.x64)**2 + (m.x103 - m.x143)**2 + (m.x182 - m.x222)**2)**(-3) - 2)
    + ((m.x24 - m.x65)**2 + (m.x103 - m.x144)**2 + (m.x182 - m.x223)**2)**(-3)
    * (((m.x24 - m.x65)**2 + (m.x103 - m.x144)**2 + (m.x182 - m.x223)**2)**(-3)
    - 2) + ((m.x24 - m.x66)**2 + (m.x103 - m.x145)**2 + (m.x182 - m.x224)**2)
    **(-3) * (((m.x24 - m.x66)**2 + (m.x103 - m.x145)**2 + (m.x182 - m.x224)**2)
    **(-3) - 2) + ((m.x24 - m.x67)**2 + (m.x103 - m.x146)**2 + (m.x182 - m.x225)
    **2)**(-3) * (((m.x24 - m.x67)**2 + (m.x103 - m.x146)**2 + (m.x182 - m.x225)
    **2)**(-3) - 2) + ((m.x24 - m.x68)**2 + (m.x103 - m.x147)**2 + (m.x182 -
    m.x226)**2)**(-3) * (((m.x24 - m.x68)**2 + (m.x103 - m.x147)**2 + (m.x182
    - m.x226)**2)**(-3) - 2) + ((m.x24 - m.x69)**2 + (m.x103 - m.x148)**2 + (
    m.x182 - m.x227)**2)**(-3) * (((m.x24 - m.x69)**2 + (m.x103 - m.x148)**2 +
    (m.x182 - m.x227)**2)**(-3) - 2) + ((m.x24 - m.x70)**2 + (m.x103 - m.x149)
    **2 + (m.x182 - m.x228)**2)**(-3) * (((m.x24 - m.x70)**2 + (m.x103 - m.x149)
    **2 + (m.x182 - m.x228)**2)**(-3) - 2) + ((m.x24 - m.x71)**2 + (m.x103 -
    m.x150)**2 + (m.x182 - m.x229)**2)**(-3) * (((m.x24 - m.x71)**2 + (m.x103
    - m.x150)**2 + (m.x182 - m.x229)**2)**(-3) - 2) + ((m.x24 - m.x72)**2 + (
    m.x103 - m.x151)**2 + (m.x182 - m.x230)**2)**(-3) * (((m.x24 - m.x72)**2 +
    (m.x103 - m.x151)**2 + (m.x182 - m.x230)**2)**(-3) - 2) + ((m.x24 - m.x73)
    **2 + (m.x103 - m.x152)**2 + (m.x182 - m.x231)**2)**(-3) * (((m.x24 - m.x73)
    **2 + (m.x103 - m.x152)**2 + (m.x182 - m.x231)**2)**(-3) - 2) + ((m.x24 -
    m.x74)**2 + (m.x103 - m.x153)**2 + (m.x182 - m.x232)**2)**(-3) * (((m.x24
    - m.x74)**2 + (m.x103 - m.x153)**2 + (m.x182 - m.x232)**2)**(-3) - 2) + ((
    m.x24 - m.x75)**2 + (m.x103 - m.x154)**2 + (m.x182 - m.x233)**2)**(-3) * ((
    (m.x24 - m.x75)**2 + (m.x103 - m.x154)**2 + (m.x182 - m.x233)**2)**(-3) - 2)
    + ((m.x24 - m.x76)**2 + (m.x103 - m.x155)**2 + (m.x182 - m.x234)**2)**(-3)
    * (((m.x24 - m.x76)**2 + (m.x103 - m.x155)**2 + (m.x182 - m.x234)**2)**(-3)
    - 2) + ((m.x24 - m.x77)**2 + (m.x103 - m.x156)**2 + (m.x182 - m.x235)**2)
    **(-3) * (((m.x24 - m.x77)**2 + (m.x103 - m.x156)**2 + (m.x182 - m.x235)**2)
    **(-3) - 2) + ((m.x24 - m.x78)**2 + (m.x103 - m.x157)**2 + (m.x182 - m.x236)
    **2)**(-3) * (((m.x24 - m.x78)**2 + (m.x103 - m.x157)**2 + (m.x182 - m.x236)
    **2)**(-3) - 2) + ((m.x24 - m.x79)**2 + (m.x103 - m.x158)**2 + (m.x182 -
    m.x237)**2)**(-3) * (((m.x24 - m.x79)**2 + (m.x103 - m.x158)**2 + (m.x182
    - m.x237)**2)**(-3) - 2) + ((m.x25 - m.x26)**2 + (m.x104 - m.x105)**2 + (
    m.x183 - m.x184)**2)**(-3) * (((m.x25 - m.x26)**2 + (m.x104 - m.x105)**2 +
    (m.x183 - m.x184)**2)**(-3) - 2) + ((m.x25 - m.x27)**2 + (m.x104 - m.x106)
    **2 + (m.x183 - m.x185)**2)**(-3) * (((m.x25 - m.x27)**2 + (m.x104 - m.x106)
    **2 + (m.x183 - m.x185)**2)**(-3) - 2) + ((m.x25 - m.x28)**2 + (m.x104 -
    m.x107)**2 + (m.x183 - m.x186)**2)**(-3) * (((m.x25 - m.x28)**2 + (m.x104
    - m.x107)**2 + (m.x183 - m.x186)**2)**(-3) - 2) + ((m.x25 - m.x29)**2 + (
    m.x104 - m.x108)**2 + (m.x183 - m.x187)**2)**(-3) * (((m.x25 - m.x29)**2 +
    (m.x104 - m.x108)**2 + (m.x183 - m.x187)**2)**(-3) - 2) + ((m.x25 - m.x30)
    **2 + (m.x104 - m.x109)**2 + (m.x183 - m.x188)**2)**(-3) * (((m.x25 - m.x30)
    **2 + (m.x104 - m.x109)**2 + (m.x183 - m.x188)**2)**(-3) - 2) + ((m.x25 -
    m.x31)**2 + (m.x104 - m.x110)**2 + (m.x183 - m.x189)**2)**(-3) * (((m.x25
    - m.x31)**2 + (m.x104 - m.x110)**2 + (m.x183 - m.x189)**2)**(-3) - 2) + ((
    m.x25 - m.x32)**2 + (m.x104 - m.x111)**2 + (m.x183 - m.x190)**2)**(-3) * ((
    (m.x25 - m.x32)**2 + (m.x104 - m.x111)**2 + (m.x183 - m.x190)**2)**(-3) - 2)
    + ((m.x25 - m.x33)**2 + (m.x104 - m.x112)**2 + (m.x183 - m.x191)**2)**(-3)
    * (((m.x25 - m.x33)**2 + (m.x104 - m.x112)**2 + (m.x183 - m.x191)**2)**(-3)
    - 2) + ((m.x25 - m.x34)**2 + (m.x104 - m.x113)**2 + (m.x183 - m.x192)**2)
    **(-3) * (((m.x25 - m.x34)**2 + (m.x104 - m.x113)**2 + (m.x183 - m.x192)**2)
    **(-3) - 2) + ((m.x25 - m.x35)**2 + (m.x104 - m.x114)**2 + (m.x183 - m.x193)
    **2)**(-3) * (((m.x25 - m.x35)**2 + (m.x104 - m.x114)**2 + (m.x183 - m.x193)
    **2)**(-3) - 2) + ((m.x25 - m.x36)**2 + (m.x104 - m.x115)**2 + (m.x183 -
    m.x194)**2)**(-3) * (((m.x25 - m.x36)**2 + (m.x104 - m.x115)**2 + (m.x183
    - m.x194)**2)**(-3) - 2) + ((m.x25 - m.x37)**2 + (m.x104 - m.x116)**2 + (
    m.x183 - m.x195)**2)**(-3) * (((m.x25 - m.x37)**2 + (m.x104 - m.x116)**2 +
    (m.x183 - m.x195)**2)**(-3) - 2) + ((m.x25 - m.x38)**2 + (m.x104 - m.x117)
    **2 + (m.x183 - m.x196)**2)**(-3) * (((m.x25 - m.x38)**2 + (m.x104 - m.x117)
    **2 + (m.x183 - m.x196)**2)**(-3) - 2) + ((m.x25 - m.x39)**2 + (m.x104 -
    m.x118)**2 + (m.x183 - m.x197)**2)**(-3) * (((m.x25 - m.x39)**2 + (m.x104
    - m.x118)**2 + (m.x183 - m.x197)**2)**(-3) - 2) + ((m.x25 - m.x40)**2 + (
    m.x104 - m.x119)**2 + (m.x183 - m.x198)**2)**(-3) * (((m.x25 - m.x40)**2 +
    (m.x104 - m.x119)**2 + (m.x183 - m.x198)**2)**(-3) - 2) + ((m.x25 - m.x41)
    **2 + (m.x104 - m.x120)**2 + (m.x183 - m.x199)**2)**(-3) * (((m.x25 - m.x41)
    **2 + (m.x104 - m.x120)**2 + (m.x183 - m.x199)**2)**(-3) - 2) + ((m.x25 -
    m.x42)**2 + (m.x104 - m.x121)**2 + (m.x183 - m.x200)**2)**(-3) * (((m.x25
    - m.x42)**2 + (m.x104 - m.x121)**2 + (m.x183 - m.x200)**2)**(-3) - 2) + ((
    m.x25 - m.x43)**2 + (m.x104 - m.x122)**2 + (m.x183 - m.x201)**2)**(-3) * ((
    (m.x25 - m.x43)**2 + (m.x104 - m.x122)**2 + (m.x183 - m.x201)**2)**(-3) - 2)
    + ((m.x25 - m.x44)**2 + (m.x104 - m.x123)**2 + (m.x183 - m.x202)**2)**(-3)
    * (((m.x25 - m.x44)**2 + (m.x104 - m.x123)**2 + (m.x183 - m.x202)**2)**(-3)
    - 2) + ((m.x25 - m.x45)**2 + (m.x104 - m.x124)**2 + (m.x183 - m.x203)**2)
    **(-3) * (((m.x25 - m.x45)**2 + (m.x104 - m.x124)**2 + (m.x183 - m.x203)**2)
    **(-3) - 2) + ((m.x25 - m.x46)**2 + (m.x104 - m.x125)**2 + (m.x183 - m.x204)
    **2)**(-3) * (((m.x25 - m.x46)**2 + (m.x104 - m.x125)**2 + (m.x183 - m.x204)
    **2)**(-3) - 2) + ((m.x25 - m.x47)**2 + (m.x104 - m.x126)**2 + (m.x183 -
    m.x205)**2)**(-3) * (((m.x25 - m.x47)**2 + (m.x104 - m.x126)**2 + (m.x183
    - m.x205)**2)**(-3) - 2) + ((m.x25 - m.x48)**2 + (m.x104 - m.x127)**2 + (
    m.x183 - m.x206)**2)**(-3) * (((m.x25 - m.x48)**2 + (m.x104 - m.x127)**2 +
    (m.x183 - m.x206)**2)**(-3) - 2) + ((m.x25 - m.x49)**2 + (m.x104 - m.x128)
    **2 + (m.x183 - m.x207)**2)**(-3) * (((m.x25 - m.x49)**2 + (m.x104 - m.x128)
    **2 + (m.x183 - m.x207)**2)**(-3) - 2) + ((m.x25 - m.x50)**2 + (m.x104 -
    m.x129)**2 + (m.x183 - m.x208)**2)**(-3) * (((m.x25 - m.x50)**2 + (m.x104
    - m.x129)**2 + (m.x183 - m.x208)**2)**(-3) - 2) + ((m.x25 - m.x51)**2 + (
    m.x104 - m.x130)**2 + (m.x183 - m.x209)**2)**(-3) * (((m.x25 - m.x51)**2 +
    (m.x104 - m.x130)**2 + (m.x183 - m.x209)**2)**(-3) - 2) + ((m.x25 - m.x52)
    **2 + (m.x104 - m.x131)**2 + (m.x183 - m.x210)**2)**(-3) * (((m.x25 - m.x52)
    **2 + (m.x104 - m.x131)**2 + (m.x183 - m.x210)**2)**(-3) - 2) + ((m.x25 -
    m.x53)**2 + (m.x104 - m.x132)**2 + (m.x183 - m.x211)**2)**(-3) * (((m.x25
    - m.x53)**2 + (m.x104 - m.x132)**2 + (m.x183 - m.x211)**2)**(-3) - 2) + ((
    m.x25 - m.x54)**2 + (m.x104 - m.x133)**2 + (m.x183 - m.x212)**2)**(-3) * ((
    (m.x25 - m.x54)**2 + (m.x104 - m.x133)**2 + (m.x183 - m.x212)**2)**(-3) - 2)
    + ((m.x25 - m.x55)**2 + (m.x104 - m.x134)**2 + (m.x183 - m.x213)**2)**(-3)
    * (((m.x25 - m.x55)**2 + (m.x104 - m.x134)**2 + (m.x183 - m.x213)**2)**(-3)
    - 2) + ((m.x25 - m.x56)**2 + (m.x104 - m.x135)**2 + (m.x183 - m.x214)**2)
    **(-3) * (((m.x25 - m.x56)**2 + (m.x104 - m.x135)**2 + (m.x183 - m.x214)**2)
    **(-3) - 2) + ((m.x25 - m.x57)**2 + (m.x104 - m.x136)**2 + (m.x183 - m.x215)
    **2)**(-3) * (((m.x25 - m.x57)**2 + (m.x104 - m.x136)**2 + (m.x183 - m.x215)
    **2)**(-3) - 2) + ((m.x25 - m.x58)**2 + (m.x104 - m.x137)**2 + (m.x183 -
    m.x216)**2)**(-3) * (((m.x25 - m.x58)**2 + (m.x104 - m.x137)**2 + (m.x183
    - m.x216)**2)**(-3) - 2) + ((m.x25 - m.x59)**2 + (m.x104 - m.x138)**2 + (
    m.x183 - m.x217)**2)**(-3) * (((m.x25 - m.x59)**2 + (m.x104 - m.x138)**2 +
    (m.x183 - m.x217)**2)**(-3) - 2) + ((m.x25 - m.x60)**2 + (m.x104 - m.x139)
    **2 + (m.x183 - m.x218)**2)**(-3) * (((m.x25 - m.x60)**2 + (m.x104 - m.x139)
    **2 + (m.x183 - m.x218)**2)**(-3) - 2) + ((m.x25 - m.x61)**2 + (m.x104 -
    m.x140)**2 + (m.x183 - m.x219)**2)**(-3) * (((m.x25 - m.x61)**2 + (m.x104
    - m.x140)**2 + (m.x183 - m.x219)**2)**(-3) - 2) + ((m.x25 - m.x62)**2 + (
    m.x104 - m.x141)**2 + (m.x183 - m.x220)**2)**(-3) * (((m.x25 - m.x62)**2 +
    (m.x104 - m.x141)**2 + (m.x183 - m.x220)**2)**(-3) - 2) + ((m.x25 - m.x63)
    **2 + (m.x104 - m.x142)**2 + (m.x183 - m.x221)**2)**(-3) * (((m.x25 - m.x63)
    **2 + (m.x104 - m.x142)**2 + (m.x183 - m.x221)**2)**(-3) - 2) + ((m.x25 -
    m.x64)**2 + (m.x104 - m.x143)**2 + (m.x183 - m.x222)**2)**(-3) * (((m.x25
    - m.x64)**2 + (m.x104 - m.x143)**2 + (m.x183 - m.x222)**2)**(-3) - 2) + ((
    m.x25 - m.x65)**2 + (m.x104 - m.x144)**2 + (m.x183 - m.x223)**2)**(-3) * ((
    (m.x25 - m.x65)**2 + (m.x104 - m.x144)**2 + (m.x183 - m.x223)**2)**(-3) - 2)
    + ((m.x25 - m.x66)**2 + (m.x104 - m.x145)**2 + (m.x183 - m.x224)**2)**(-3)
    * (((m.x25 - m.x66)**2 + (m.x104 - m.x145)**2 + (m.x183 - m.x224)**2)**(-3)
    - 2) + ((m.x25 - m.x67)**2 + (m.x104 - m.x146)**2 + (m.x183 - m.x225)**2)
    **(-3) * (((m.x25 - m.x67)**2 + (m.x104 - m.x146)**2 + (m.x183 - m.x225)**2)
    **(-3) - 2) + ((m.x25 - m.x68)**2 + (m.x104 - m.x147)**2 + (m.x183 - m.x226)
    **2)**(-3) * (((m.x25 - m.x68)**2 + (m.x104 - m.x147)**2 + (m.x183 - m.x226)
    **2)**(-3) - 2) + ((m.x25 - m.x69)**2 + (m.x104 - m.x148)**2 + (m.x183 -
    m.x227)**2)**(-3) * (((m.x25 - m.x69)**2 + (m.x104 - m.x148)**2 + (m.x183
    - m.x227)**2)**(-3) - 2) + ((m.x25 - m.x70)**2 + (m.x104 - m.x149)**2 + (
    m.x183 - m.x228)**2)**(-3) * (((m.x25 - m.x70)**2 + (m.x104 - m.x149)**2 +
    (m.x183 - m.x228)**2)**(-3) - 2) + ((m.x25 - m.x71)**2 + (m.x104 - m.x150)
    **2 + (m.x183 - m.x229)**2)**(-3) * (((m.x25 - m.x71)**2 + (m.x104 - m.x150)
    **2 + (m.x183 - m.x229)**2)**(-3) - 2) + ((m.x25 - m.x72)**2 + (m.x104 -
    m.x151)**2 + (m.x183 - m.x230)**2)**(-3) * (((m.x25 - m.x72)**2 + (m.x104
    - m.x151)**2 + (m.x183 - m.x230)**2)**(-3) - 2) + ((m.x25 - m.x73)**2 + (
    m.x104 - m.x152)**2 + (m.x183 - m.x231)**2)**(-3) * (((m.x25 - m.x73)**2 +
    (m.x104 - m.x152)**2 + (m.x183 - m.x231)**2)**(-3) - 2) + ((m.x25 - m.x74)
    **2 + (m.x104 - m.x153)**2 + (m.x183 - m.x232)**2)**(-3) * (((m.x25 - m.x74)
    **2 + (m.x104 - m.x153)**2 + (m.x183 - m.x232)**2)**(-3) - 2) + ((m.x25 -
    m.x75)**2 + (m.x104 - m.x154)**2 + (m.x183 - m.x233)**2)**(-3) * (((m.x25
    - m.x75)**2 + (m.x104 - m.x154)**2 + (m.x183 - m.x233)**2)**(-3) - 2) + ((
    m.x25 - m.x76)**2 + (m.x104 - m.x155)**2 + (m.x183 - m.x234)**2)**(-3) * ((
    (m.x25 - m.x76)**2 + (m.x104 - m.x155)**2 + (m.x183 - m.x234)**2)**(-3) - 2)
    + ((m.x25 - m.x77)**2 + (m.x104 - m.x156)**2 + (m.x183 - m.x235)**2)**(-3)
    * (((m.x25 - m.x77)**2 + (m.x104 - m.x156)**2 + (m.x183 - m.x235)**2)**(-3)
    - 2) + ((m.x25 - m.x78)**2 + (m.x104 - m.x157)**2 + (m.x183 - m.x236)**2)
    **(-3) * (((m.x25 - m.x78)**2 + (m.x104 - m.x157)**2 + (m.x183 - m.x236)**2)
    **(-3) - 2) + ((m.x25 - m.x79)**2 + (m.x104 - m.x158)**2 + (m.x183 - m.x237)
    **2)**(-3) * (((m.x25 - m.x79)**2 + (m.x104 - m.x158)**2 + (m.x183 - m.x237)
    **2)**(-3) - 2) + ((m.x26 - m.x27)**2 + (m.x105 - m.x106)**2 + (m.x184 -
    m.x185)**2)**(-3) * (((m.x26 - m.x27)**2 + (m.x105 - m.x106)**2 + (m.x184
    - m.x185)**2)**(-3) - 2) + ((m.x26 - m.x28)**2 + (m.x105 - m.x107)**2 + (
    m.x184 - m.x186)**2)**(-3) * (((m.x26 - m.x28)**2 + (m.x105 - m.x107)**2 +
    (m.x184 - m.x186)**2)**(-3) - 2) + ((m.x26 - m.x29)**2 + (m.x105 - m.x108)
    **2 + (m.x184 - m.x187)**2)**(-3) * (((m.x26 - m.x29)**2 + (m.x105 - m.x108)
    **2 + (m.x184 - m.x187)**2)**(-3) - 2) + ((m.x26 - m.x30)**2 + (m.x105 -
    m.x109)**2 + (m.x184 - m.x188)**2)**(-3) * (((m.x26 - m.x30)**2 + (m.x105
    - m.x109)**2 + (m.x184 - m.x188)**2)**(-3) - 2) + ((m.x26 - m.x31)**2 + (
    m.x105 - m.x110)**2 + (m.x184 - m.x189)**2)**(-3) * (((m.x26 - m.x31)**2 +
    (m.x105 - m.x110)**2 + (m.x184 - m.x189)**2)**(-3) - 2) + ((m.x26 - m.x32)
    **2 + (m.x105 - m.x111)**2 + (m.x184 - m.x190)**2)**(-3) * (((m.x26 - m.x32)
    **2 + (m.x105 - m.x111)**2 + (m.x184 - m.x190)**2)**(-3) - 2) + ((m.x26 -
    m.x33)**2 + (m.x105 - m.x112)**2 + (m.x184 - m.x191)**2)**(-3) * (((m.x26
    - m.x33)**2 + (m.x105 - m.x112)**2 + (m.x184 - m.x191)**2)**(-3) - 2) + ((
    m.x26 - m.x34)**2 + (m.x105 - m.x113)**2 + (m.x184 - m.x192)**2)**(-3) * ((
    (m.x26 - m.x34)**2 + (m.x105 - m.x113)**2 + (m.x184 - m.x192)**2)**(-3) - 2)
    + ((m.x26 - m.x35)**2 + (m.x105 - m.x114)**2 + (m.x184 - m.x193)**2)**(-3)
    * (((m.x26 - m.x35)**2 + (m.x105 - m.x114)**2 + (m.x184 - m.x193)**2)**(-3)
    - 2) + ((m.x26 - m.x36)**2 + (m.x105 - m.x115)**2 + (m.x184 - m.x194)**2)
    **(-3) * (((m.x26 - m.x36)**2 + (m.x105 - m.x115)**2 + (m.x184 - m.x194)**2)
    **(-3) - 2) + ((m.x26 - m.x37)**2 + (m.x105 - m.x116)**2 + (m.x184 - m.x195)
    **2)**(-3) * (((m.x26 - m.x37)**2 + (m.x105 - m.x116)**2 + (m.x184 - m.x195)
    **2)**(-3) - 2) + ((m.x26 - m.x38)**2 + (m.x105 - m.x117)**2 + (m.x184 -
    m.x196)**2)**(-3) * (((m.x26 - m.x38)**2 + (m.x105 - m.x117)**2 + (m.x184
    - m.x196)**2)**(-3) - 2) + ((m.x26 - m.x39)**2 + (m.x105 - m.x118)**2 + (
    m.x184 - m.x197)**2)**(-3) * (((m.x26 - m.x39)**2 + (m.x105 - m.x118)**2 +
    (m.x184 - m.x197)**2)**(-3) - 2) + ((m.x26 - m.x40)**2 + (m.x105 - m.x119)
    **2 + (m.x184 - m.x198)**2)**(-3) * (((m.x26 - m.x40)**2 + (m.x105 - m.x119)
    **2 + (m.x184 - m.x198)**2)**(-3) - 2) + ((m.x26 - m.x41)**2 + (m.x105 -
    m.x120)**2 + (m.x184 - m.x199)**2)**(-3) * (((m.x26 - m.x41)**2 + (m.x105
    - m.x120)**2 + (m.x184 - m.x199)**2)**(-3) - 2) + ((m.x26 - m.x42)**2 + (
    m.x105 - m.x121)**2 + (m.x184 - m.x200)**2)**(-3) * (((m.x26 - m.x42)**2 +
    (m.x105 - m.x121)**2 + (m.x184 - m.x200)**2)**(-3) - 2) + ((m.x26 - m.x43)
    **2 + (m.x105 - m.x122)**2 + (m.x184 - m.x201)**2)**(-3) * (((m.x26 - m.x43)
    **2 + (m.x105 - m.x122)**2 + (m.x184 - m.x201)**2)**(-3) - 2) + ((m.x26 -
    m.x44)**2 + (m.x105 - m.x123)**2 + (m.x184 - m.x202)**2)**(-3) * (((m.x26
    - m.x44)**2 + (m.x105 - m.x123)**2 + (m.x184 - m.x202)**2)**(-3) - 2) + ((
    m.x26 - m.x45)**2 + (m.x105 - m.x124)**2 + (m.x184 - m.x203)**2)**(-3) * ((
    (m.x26 - m.x45)**2 + (m.x105 - m.x124)**2 + (m.x184 - m.x203)**2)**(-3) - 2)
    + ((m.x26 - m.x46)**2 + (m.x105 - m.x125)**2 + (m.x184 - m.x204)**2)**(-3)
    * (((m.x26 - m.x46)**2 + (m.x105 - m.x125)**2 + (m.x184 - m.x204)**2)**(-3)
    - 2) + ((m.x26 - m.x47)**2 + (m.x105 - m.x126)**2 + (m.x184 - m.x205)**2)
    **(-3) * (((m.x26 - m.x47)**2 + (m.x105 - m.x126)**2 + (m.x184 - m.x205)**2)
    **(-3) - 2) + ((m.x26 - m.x48)**2 + (m.x105 - m.x127)**2 + (m.x184 - m.x206)
    **2)**(-3) * (((m.x26 - m.x48)**2 + (m.x105 - m.x127)**2 + (m.x184 - m.x206)
    **2)**(-3) - 2) + ((m.x26 - m.x49)**2 + (m.x105 - m.x128)**2 + (m.x184 -
    m.x207)**2)**(-3) * (((m.x26 - m.x49)**2 + (m.x105 - m.x128)**2 + (m.x184
    - m.x207)**2)**(-3) - 2) + ((m.x26 - m.x50)**2 + (m.x105 - m.x129)**2 + (
    m.x184 - m.x208)**2)**(-3) * (((m.x26 - m.x50)**2 + (m.x105 - m.x129)**2 +
    (m.x184 - m.x208)**2)**(-3) - 2) + ((m.x26 - m.x51)**2 + (m.x105 - m.x130)
    **2 + (m.x184 - m.x209)**2)**(-3) * (((m.x26 - m.x51)**2 + (m.x105 - m.x130)
    **2 + (m.x184 - m.x209)**2)**(-3) - 2) + ((m.x26 - m.x52)**2 + (m.x105 -
    m.x131)**2 + (m.x184 - m.x210)**2)**(-3) * (((m.x26 - m.x52)**2 + (m.x105
    - m.x131)**2 + (m.x184 - m.x210)**2)**(-3) - 2) + ((m.x26 - m.x53)**2 + (
    m.x105 - m.x132)**2 + (m.x184 - m.x211)**2)**(-3) * (((m.x26 - m.x53)**2 +
    (m.x105 - m.x132)**2 + (m.x184 - m.x211)**2)**(-3) - 2) + ((m.x26 - m.x54)
    **2 + (m.x105 - m.x133)**2 + (m.x184 - m.x212)**2)**(-3) * (((m.x26 - m.x54)
    **2 + (m.x105 - m.x133)**2 + (m.x184 - m.x212)**2)**(-3) - 2) + ((m.x26 -
    m.x55)**2 + (m.x105 - m.x134)**2 + (m.x184 - m.x213)**2)**(-3) * (((m.x26
    - m.x55)**2 + (m.x105 - m.x134)**2 + (m.x184 - m.x213)**2)**(-3) - 2) + ((
    m.x26 - m.x56)**2 + (m.x105 - m.x135)**2 + (m.x184 - m.x214)**2)**(-3) * ((
    (m.x26 - m.x56)**2 + (m.x105 - m.x135)**2 + (m.x184 - m.x214)**2)**(-3) - 2)
    + ((m.x26 - m.x57)**2 + (m.x105 - m.x136)**2 + (m.x184 - m.x215)**2)**(-3)
    * (((m.x26 - m.x57)**2 + (m.x105 - m.x136)**2 + (m.x184 - m.x215)**2)**(-3)
    - 2) + ((m.x26 - m.x58)**2 + (m.x105 - m.x137)**2 + (m.x184 - m.x216)**2)
    **(-3) * (((m.x26 - m.x58)**2 + (m.x105 - m.x137)**2 + (m.x184 - m.x216)**2)
    **(-3) - 2) + ((m.x26 - m.x59)**2 + (m.x105 - m.x138)**2 + (m.x184 - m.x217)
    **2)**(-3) * (((m.x26 - m.x59)**2 + (m.x105 - m.x138)**2 + (m.x184 - m.x217)
    **2)**(-3) - 2) + ((m.x26 - m.x60)**2 + (m.x105 - m.x139)**2 + (m.x184 -
    m.x218)**2)**(-3) * (((m.x26 - m.x60)**2 + (m.x105 - m.x139)**2 + (m.x184
    - m.x218)**2)**(-3) - 2) + ((m.x26 - m.x61)**2 + (m.x105 - m.x140)**2 + (
    m.x184 - m.x219)**2)**(-3) * (((m.x26 - m.x61)**2 + (m.x105 - m.x140)**2 +
    (m.x184 - m.x219)**2)**(-3) - 2) + ((m.x26 - m.x62)**2 + (m.x105 - m.x141)
    **2 + (m.x184 - m.x220)**2)**(-3) * (((m.x26 - m.x62)**2 + (m.x105 - m.x141)
    **2 + (m.x184 - m.x220)**2)**(-3) - 2) + ((m.x26 - m.x63)**2 + (m.x105 -
    m.x142)**2 + (m.x184 - m.x221)**2)**(-3) * (((m.x26 - m.x63)**2 + (m.x105
    - m.x142)**2 + (m.x184 - m.x221)**2)**(-3) - 2) + ((m.x26 - m.x64)**2 + (
    m.x105 - m.x143)**2 + (m.x184 - m.x222)**2)**(-3) * (((m.x26 - m.x64)**2 +
    (m.x105 - m.x143)**2 + (m.x184 - m.x222)**2)**(-3) - 2) + ((m.x26 - m.x65)
    **2 + (m.x105 - m.x144)**2 + (m.x184 - m.x223)**2)**(-3) * (((m.x26 - m.x65)
    **2 + (m.x105 - m.x144)**2 + (m.x184 - m.x223)**2)**(-3) - 2) + ((m.x26 -
    m.x66)**2 + (m.x105 - m.x145)**2 + (m.x184 - m.x224)**2)**(-3) * (((m.x26
    - m.x66)**2 + (m.x105 - m.x145)**2 + (m.x184 - m.x224)**2)**(-3) - 2) + ((
    m.x26 - m.x67)**2 + (m.x105 - m.x146)**2 + (m.x184 - m.x225)**2)**(-3) * ((
    (m.x26 - m.x67)**2 + (m.x105 - m.x146)**2 + (m.x184 - m.x225)**2)**(-3) - 2)
    + ((m.x26 - m.x68)**2 + (m.x105 - m.x147)**2 + (m.x184 - m.x226)**2)**(-3)
    * (((m.x26 - m.x68)**2 + (m.x105 - m.x147)**2 + (m.x184 - m.x226)**2)**(-3)
    - 2) + ((m.x26 - m.x69)**2 + (m.x105 - m.x148)**2 + (m.x184 - m.x227)**2)
    **(-3) * (((m.x26 - m.x69)**2 + (m.x105 - m.x148)**2 + (m.x184 - m.x227)**2)
    **(-3) - 2) + ((m.x26 - m.x70)**2 + (m.x105 - m.x149)**2 + (m.x184 - m.x228)
    **2)**(-3) * (((m.x26 - m.x70)**2 + (m.x105 - m.x149)**2 + (m.x184 - m.x228)
    **2)**(-3) - 2) + ((m.x26 - m.x71)**2 + (m.x105 - m.x150)**2 + (m.x184 -
    m.x229)**2)**(-3) * (((m.x26 - m.x71)**2 + (m.x105 - m.x150)**2 + (m.x184
    - m.x229)**2)**(-3) - 2) + ((m.x26 - m.x72)**2 + (m.x105 - m.x151)**2 + (
    m.x184 - m.x230)**2)**(-3) * (((m.x26 - m.x72)**2 + (m.x105 - m.x151)**2 +
    (m.x184 - m.x230)**2)**(-3) - 2) + ((m.x26 - m.x73)**2 + (m.x105 - m.x152)
    **2 + (m.x184 - m.x231)**2)**(-3) * (((m.x26 - m.x73)**2 + (m.x105 - m.x152)
    **2 + (m.x184 - m.x231)**2)**(-3) - 2) + ((m.x26 - m.x74)**2 + (m.x105 -
    m.x153)**2 + (m.x184 - m.x232)**2)**(-3) * (((m.x26 - m.x74)**2 + (m.x105
    - m.x153)**2 + (m.x184 - m.x232)**2)**(-3) - 2) + ((m.x26 - m.x75)**2 + (
    m.x105 - m.x154)**2 + (m.x184 - m.x233)**2)**(-3) * (((m.x26 - m.x75)**2 +
    (m.x105 - m.x154)**2 + (m.x184 - m.x233)**2)**(-3) - 2) + ((m.x26 - m.x76)
    **2 + (m.x105 - m.x155)**2 + (m.x184 - m.x234)**2)**(-3) * (((m.x26 - m.x76)
    **2 + (m.x105 - m.x155)**2 + (m.x184 - m.x234)**2)**(-3) - 2) + ((m.x26 -
    m.x77)**2 + (m.x105 - m.x156)**2 + (m.x184 - m.x235)**2)**(-3) * (((m.x26
    - m.x77)**2 + (m.x105 - m.x156)**2 + (m.x184 - m.x235)**2)**(-3) - 2) + ((
    m.x26 - m.x78)**2 + (m.x105 - m.x157)**2 + (m.x184 - m.x236)**2)**(-3) * ((
    (m.x26 - m.x78)**2 + (m.x105 - m.x157)**2 + (m.x184 - m.x236)**2)**(-3) - 2)
    + ((m.x26 - m.x79)**2 + (m.x105 - m.x158)**2 + (m.x184 - m.x237)**2)**(-3)
    * (((m.x26 - m.x79)**2 + (m.x105 - m.x158)**2 + (m.x184 - m.x237)**2)**(-3)
    - 2) + ((m.x27 - m.x28)**2 + (m.x106 - m.x107)**2 + (m.x185 - m.x186)**2)
    **(-3) * (((m.x27 - m.x28)**2 + (m.x106 - m.x107)**2 + (m.x185 - m.x186)**2)
    **(-3) - 2) + ((m.x27 - m.x29)**2 + (m.x106 - m.x108)**2 + (m.x185 - m.x187)
    **2)**(-3) * (((m.x27 - m.x29)**2 + (m.x106 - m.x108)**2 + (m.x185 - m.x187)
    **2)**(-3) - 2) + ((m.x27 - m.x30)**2 + (m.x106 - m.x109)**2 + (m.x185 -
    m.x188)**2)**(-3) * (((m.x27 - m.x30)**2 + (m.x106 - m.x109)**2 + (m.x185
    - m.x188)**2)**(-3) - 2) + ((m.x27 - m.x31)**2 + (m.x106 - m.x110)**2 + (
    m.x185 - m.x189)**2)**(-3) * (((m.x27 - m.x31)**2 + (m.x106 - m.x110)**2 +
    (m.x185 - m.x189)**2)**(-3) - 2) + ((m.x27 - m.x32)**2 + (m.x106 - m.x111)
    **2 + (m.x185 - m.x190)**2)**(-3) * (((m.x27 - m.x32)**2 + (m.x106 - m.x111)
    **2 + (m.x185 - m.x190)**2)**(-3) - 2) + ((m.x27 - m.x33)**2 + (m.x106 -
    m.x112)**2 + (m.x185 - m.x191)**2)**(-3) * (((m.x27 - m.x33)**2 + (m.x106
    - m.x112)**2 + (m.x185 - m.x191)**2)**(-3) - 2) + ((m.x27 - m.x34)**2 + (
    m.x106 - m.x113)**2 + (m.x185 - m.x192)**2)**(-3) * (((m.x27 - m.x34)**2 +
    (m.x106 - m.x113)**2 + (m.x185 - m.x192)**2)**(-3) - 2) + ((m.x27 - m.x35)
    **2 + (m.x106 - m.x114)**2 + (m.x185 - m.x193)**2)**(-3) * (((m.x27 - m.x35)
    **2 + (m.x106 - m.x114)**2 + (m.x185 - m.x193)**2)**(-3) - 2) + ((m.x27 -
    m.x36)**2 + (m.x106 - m.x115)**2 + (m.x185 - m.x194)**2)**(-3) * (((m.x27
    - m.x36)**2 + (m.x106 - m.x115)**2 + (m.x185 - m.x194)**2)**(-3) - 2) + ((
    m.x27 - m.x37)**2 + (m.x106 - m.x116)**2 + (m.x185 - m.x195)**2)**(-3) * ((
    (m.x27 - m.x37)**2 + (m.x106 - m.x116)**2 + (m.x185 - m.x195)**2)**(-3) - 2)
    + ((m.x27 - m.x38)**2 + (m.x106 - m.x117)**2 + (m.x185 - m.x196)**2)**(-3)
    * (((m.x27 - m.x38)**2 + (m.x106 - m.x117)**2 + (m.x185 - m.x196)**2)**(-3)
    - 2) + ((m.x27 - m.x39)**2 + (m.x106 - m.x118)**2 + (m.x185 - m.x197)**2)
    **(-3) * (((m.x27 - m.x39)**2 + (m.x106 - m.x118)**2 + (m.x185 - m.x197)**2)
    **(-3) - 2) + ((m.x27 - m.x40)**2 + (m.x106 - m.x119)**2 + (m.x185 - m.x198)
    **2)**(-3) * (((m.x27 - m.x40)**2 + (m.x106 - m.x119)**2 + (m.x185 - m.x198)
    **2)**(-3) - 2) + ((m.x27 - m.x41)**2 + (m.x106 - m.x120)**2 + (m.x185 -
    m.x199)**2)**(-3) * (((m.x27 - m.x41)**2 + (m.x106 - m.x120)**2 + (m.x185
    - m.x199)**2)**(-3) - 2) + ((m.x27 - m.x42)**2 + (m.x106 - m.x121)**2 + (
    m.x185 - m.x200)**2)**(-3) * (((m.x27 - m.x42)**2 + (m.x106 - m.x121)**2 +
    (m.x185 - m.x200)**2)**(-3) - 2) + ((m.x27 - m.x43)**2 + (m.x106 - m.x122)
    **2 + (m.x185 - m.x201)**2)**(-3) * (((m.x27 - m.x43)**2 + (m.x106 - m.x122)
    **2 + (m.x185 - m.x201)**2)**(-3) - 2) + ((m.x27 - m.x44)**2 + (m.x106 -
    m.x123)**2 + (m.x185 - m.x202)**2)**(-3) * (((m.x27 - m.x44)**2 + (m.x106
    - m.x123)**2 + (m.x185 - m.x202)**2)**(-3) - 2) + ((m.x27 - m.x45)**2 + (
    m.x106 - m.x124)**2 + (m.x185 - m.x203)**2)**(-3) * (((m.x27 - m.x45)**2 +
    (m.x106 - m.x124)**2 + (m.x185 - m.x203)**2)**(-3) - 2) + ((m.x27 - m.x46)
    **2 + (m.x106 - m.x125)**2 + (m.x185 - m.x204)**2)**(-3) * (((m.x27 - m.x46)
    **2 + (m.x106 - m.x125)**2 + (m.x185 - m.x204)**2)**(-3) - 2) + ((m.x27 -
    m.x47)**2 + (m.x106 - m.x126)**2 + (m.x185 - m.x205)**2)**(-3) * (((m.x27
    - m.x47)**2 + (m.x106 - m.x126)**2 + (m.x185 - m.x205)**2)**(-3) - 2) + ((
    m.x27 - m.x48)**2 + (m.x106 - m.x127)**2 + (m.x185 - m.x206)**2)**(-3) * ((
    (m.x27 - m.x48)**2 + (m.x106 - m.x127)**2 + (m.x185 - m.x206)**2)**(-3) - 2)
    + ((m.x27 - m.x49)**2 + (m.x106 - m.x128)**2 + (m.x185 - m.x207)**2)**(-3)
    * (((m.x27 - m.x49)**2 + (m.x106 - m.x128)**2 + (m.x185 - m.x207)**2)**(-3)
    - 2) + ((m.x27 - m.x50)**2 + (m.x106 - m.x129)**2 + (m.x185 - m.x208)**2)
    **(-3) * (((m.x27 - m.x50)**2 + (m.x106 - m.x129)**2 + (m.x185 - m.x208)**2)
    **(-3) - 2) + ((m.x27 - m.x51)**2 + (m.x106 - m.x130)**2 + (m.x185 - m.x209)
    **2)**(-3) * (((m.x27 - m.x51)**2 + (m.x106 - m.x130)**2 + (m.x185 - m.x209)
    **2)**(-3) - 2) + ((m.x27 - m.x52)**2 + (m.x106 - m.x131)**2 + (m.x185 -
    m.x210)**2)**(-3) * (((m.x27 - m.x52)**2 + (m.x106 - m.x131)**2 + (m.x185
    - m.x210)**2)**(-3) - 2) + ((m.x27 - m.x53)**2 + (m.x106 - m.x132)**2 + (
    m.x185 - m.x211)**2)**(-3) * (((m.x27 - m.x53)**2 + (m.x106 - m.x132)**2 +
    (m.x185 - m.x211)**2)**(-3) - 2) + ((m.x27 - m.x54)**2 + (m.x106 - m.x133)
    **2 + (m.x185 - m.x212)**2)**(-3) * (((m.x27 - m.x54)**2 + (m.x106 - m.x133)
    **2 + (m.x185 - m.x212)**2)**(-3) - 2) + ((m.x27 - m.x55)**2 + (m.x106 -
    m.x134)**2 + (m.x185 - m.x213)**2)**(-3) * (((m.x27 - m.x55)**2 + (m.x106
    - m.x134)**2 + (m.x185 - m.x213)**2)**(-3) - 2) + ((m.x27 - m.x56)**2 + (
    m.x106 - m.x135)**2 + (m.x185 - m.x214)**2)**(-3) * (((m.x27 - m.x56)**2 +
    (m.x106 - m.x135)**2 + (m.x185 - m.x214)**2)**(-3) - 2) + ((m.x27 - m.x57)
    **2 + (m.x106 - m.x136)**2 + (m.x185 - m.x215)**2)**(-3) * (((m.x27 - m.x57)
    **2 + (m.x106 - m.x136)**2 + (m.x185 - m.x215)**2)**(-3) - 2) + ((m.x27 -
    m.x58)**2 + (m.x106 - m.x137)**2 + (m.x185 - m.x216)**2)**(-3) * (((m.x27
    - m.x58)**2 + (m.x106 - m.x137)**2 + (m.x185 - m.x216)**2)**(-3) - 2) + ((
    m.x27 - m.x59)**2 + (m.x106 - m.x138)**2 + (m.x185 - m.x217)**2)**(-3) * ((
    (m.x27 - m.x59)**2 + (m.x106 - m.x138)**2 + (m.x185 - m.x217)**2)**(-3) - 2)
    + ((m.x27 - m.x60)**2 + (m.x106 - m.x139)**2 + (m.x185 - m.x218)**2)**(-3)
    * (((m.x27 - m.x60)**2 + (m.x106 - m.x139)**2 + (m.x185 - m.x218)**2)**(-3)
    - 2) + ((m.x27 - m.x61)**2 + (m.x106 - m.x140)**2 + (m.x185 - m.x219)**2)
    **(-3) * (((m.x27 - m.x61)**2 + (m.x106 - m.x140)**2 + (m.x185 - m.x219)**2)
    **(-3) - 2) + ((m.x27 - m.x62)**2 + (m.x106 - m.x141)**2 + (m.x185 - m.x220)
    **2)**(-3) * (((m.x27 - m.x62)**2 + (m.x106 - m.x141)**2 + (m.x185 - m.x220)
    **2)**(-3) - 2) + ((m.x27 - m.x63)**2 + (m.x106 - m.x142)**2 + (m.x185 -
    m.x221)**2)**(-3) * (((m.x27 - m.x63)**2 + (m.x106 - m.x142)**2 + (m.x185
    - m.x221)**2)**(-3) - 2) + ((m.x27 - m.x64)**2 + (m.x106 - m.x143)**2 + (
    m.x185 - m.x222)**2)**(-3) * (((m.x27 - m.x64)**2 + (m.x106 - m.x143)**2 +
    (m.x185 - m.x222)**2)**(-3) - 2) + ((m.x27 - m.x65)**2 + (m.x106 - m.x144)
    **2 + (m.x185 - m.x223)**2)**(-3) * (((m.x27 - m.x65)**2 + (m.x106 - m.x144)
    **2 + (m.x185 - m.x223)**2)**(-3) - 2) + ((m.x27 - m.x66)**2 + (m.x106 -
    m.x145)**2 + (m.x185 - m.x224)**2)**(-3) * (((m.x27 - m.x66)**2 + (m.x106
    - m.x145)**2 + (m.x185 - m.x224)**2)**(-3) - 2) + ((m.x27 - m.x67)**2 + (
    m.x106 - m.x146)**2 + (m.x185 - m.x225)**2)**(-3) * (((m.x27 - m.x67)**2 +
    (m.x106 - m.x146)**2 + (m.x185 - m.x225)**2)**(-3) - 2) + ((m.x27 - m.x68)
    **2 + (m.x106 - m.x147)**2 + (m.x185 - m.x226)**2)**(-3) * (((m.x27 - m.x68)
    **2 + (m.x106 - m.x147)**2 + (m.x185 - m.x226)**2)**(-3) - 2) + ((m.x27 -
    m.x69)**2 + (m.x106 - m.x148)**2 + (m.x185 - m.x227)**2)**(-3) * (((m.x27
    - m.x69)**2 + (m.x106 - m.x148)**2 + (m.x185 - m.x227)**2)**(-3) - 2) + ((
    m.x27 - m.x70)**2 + (m.x106 - m.x149)**2 + (m.x185 - m.x228)**2)**(-3) * ((
    (m.x27 - m.x70)**2 + (m.x106 - m.x149)**2 + (m.x185 - m.x228)**2)**(-3) - 2)
    + ((m.x27 - m.x71)**2 + (m.x106 - m.x150)**2 + (m.x185 - m.x229)**2)**(-3)
    * (((m.x27 - m.x71)**2 + (m.x106 - m.x150)**2 + (m.x185 - m.x229)**2)**(-3)
    - 2) + ((m.x27 - m.x72)**2 + (m.x106 - m.x151)**2 + (m.x185 - m.x230)**2)
    **(-3) * (((m.x27 - m.x72)**2 + (m.x106 - m.x151)**2 + (m.x185 - m.x230)**2)
    **(-3) - 2) + ((m.x27 - m.x73)**2 + (m.x106 - m.x152)**2 + (m.x185 - m.x231)
    **2)**(-3) * (((m.x27 - m.x73)**2 + (m.x106 - m.x152)**2 + (m.x185 - m.x231)
    **2)**(-3) - 2) + ((m.x27 - m.x74)**2 + (m.x106 - m.x153)**2 + (m.x185 -
    m.x232)**2)**(-3) * (((m.x27 - m.x74)**2 + (m.x106 - m.x153)**2 + (m.x185
    - m.x232)**2)**(-3) - 2) + ((m.x27 - m.x75)**2 + (m.x106 - m.x154)**2 + (
    m.x185 - m.x233)**2)**(-3) * (((m.x27 - m.x75)**2 + (m.x106 - m.x154)**2 +
    (m.x185 - m.x233)**2)**(-3) - 2) + ((m.x27 - m.x76)**2 + (m.x106 - m.x155)
    **2 + (m.x185 - m.x234)**2)**(-3) * (((m.x27 - m.x76)**2 + (m.x106 - m.x155)
    **2 + (m.x185 - m.x234)**2)**(-3) - 2) + ((m.x27 - m.x77)**2 + (m.x106 -
    m.x156)**2 + (m.x185 - m.x235)**2)**(-3) * (((m.x27 - m.x77)**2 + (m.x106
    - m.x156)**2 + (m.x185 - m.x235)**2)**(-3) - 2) + ((m.x27 - m.x78)**2 + (
    m.x106 - m.x157)**2 + (m.x185 - m.x236)**2)**(-3) * (((m.x27 - m.x78)**2 +
    (m.x106 - m.x157)**2 + (m.x185 - m.x236)**2)**(-3) - 2) + ((m.x27 - m.x79)
    **2 + (m.x106 - m.x158)**2 + (m.x185 - m.x237)**2)**(-3) * (((m.x27 - m.x79)
    **2 + (m.x106 - m.x158)**2 + (m.x185 - m.x237)**2)**(-3) - 2) + ((m.x28 -
    m.x29)**2 + (m.x107 - m.x108)**2 + (m.x186 - m.x187)**2)**(-3) * (((m.x28
    - m.x29)**2 + (m.x107 - m.x108)**2 + (m.x186 - m.x187)**2)**(-3) - 2) + ((
    m.x28 - m.x30)**2 + (m.x107 - m.x109)**2 + (m.x186 - m.x188)**2)**(-3) * ((
    (m.x28 - m.x30)**2 + (m.x107 - m.x109)**2 + (m.x186 - m.x188)**2)**(-3) - 2)
    + ((m.x28 - m.x31)**2 + (m.x107 - m.x110)**2 + (m.x186 - m.x189)**2)**(-3)
    * (((m.x28 - m.x31)**2 + (m.x107 - m.x110)**2 + (m.x186 - m.x189)**2)**(-3)
    - 2) + ((m.x28 - m.x32)**2 + (m.x107 - m.x111)**2 + (m.x186 - m.x190)**2)
    **(-3) * (((m.x28 - m.x32)**2 + (m.x107 - m.x111)**2 + (m.x186 - m.x190)**2)
    **(-3) - 2) + ((m.x28 - m.x33)**2 + (m.x107 - m.x112)**2 + (m.x186 - m.x191)
    **2)**(-3) * (((m.x28 - m.x33)**2 + (m.x107 - m.x112)**2 + (m.x186 - m.x191)
    **2)**(-3) - 2) + ((m.x28 - m.x34)**2 + (m.x107 - m.x113)**2 + (m.x186 -
    m.x192)**2)**(-3) * (((m.x28 - m.x34)**2 + (m.x107 - m.x113)**2 + (m.x186
    - m.x192)**2)**(-3) - 2) + ((m.x28 - m.x35)**2 + (m.x107 - m.x114)**2 + (
    m.x186 - m.x193)**2)**(-3) * (((m.x28 - m.x35)**2 + (m.x107 - m.x114)**2 +
    (m.x186 - m.x193)**2)**(-3) - 2) + ((m.x28 - m.x36)**2 + (m.x107 - m.x115)
    **2 + (m.x186 - m.x194)**2)**(-3) * (((m.x28 - m.x36)**2 + (m.x107 - m.x115)
    **2 + (m.x186 - m.x194)**2)**(-3) - 2) + ((m.x28 - m.x37)**2 + (m.x107 -
    m.x116)**2 + (m.x186 - m.x195)**2)**(-3) * (((m.x28 - m.x37)**2 + (m.x107
    - m.x116)**2 + (m.x186 - m.x195)**2)**(-3) - 2) + ((m.x28 - m.x38)**2 + (
    m.x107 - m.x117)**2 + (m.x186 - m.x196)**2)**(-3) * (((m.x28 - m.x38)**2 +
    (m.x107 - m.x117)**2 + (m.x186 - m.x196)**2)**(-3) - 2) + ((m.x28 - m.x39)
    **2 + (m.x107 - m.x118)**2 + (m.x186 - m.x197)**2)**(-3) * (((m.x28 - m.x39)
    **2 + (m.x107 - m.x118)**2 + (m.x186 - m.x197)**2)**(-3) - 2) + ((m.x28 -
    m.x40)**2 + (m.x107 - m.x119)**2 + (m.x186 - m.x198)**2)**(-3) * (((m.x28
    - m.x40)**2 + (m.x107 - m.x119)**2 + (m.x186 - m.x198)**2)**(-3) - 2) + ((
    m.x28 - m.x41)**2 + (m.x107 - m.x120)**2 + (m.x186 - m.x199)**2)**(-3) * ((
    (m.x28 - m.x41)**2 + (m.x107 - m.x120)**2 + (m.x186 - m.x199)**2)**(-3) - 2)
    + ((m.x28 - m.x42)**2 + (m.x107 - m.x121)**2 + (m.x186 - m.x200)**2)**(-3)
    * (((m.x28 - m.x42)**2 + (m.x107 - m.x121)**2 + (m.x186 - m.x200)**2)**(-3)
    - 2) + ((m.x28 - m.x43)**2 + (m.x107 - m.x122)**2 + (m.x186 - m.x201)**2)
    **(-3) * (((m.x28 - m.x43)**2 + (m.x107 - m.x122)**2 + (m.x186 - m.x201)**2)
    **(-3) - 2) + ((m.x28 - m.x44)**2 + (m.x107 - m.x123)**2 + (m.x186 - m.x202)
    **2)**(-3) * (((m.x28 - m.x44)**2 + (m.x107 - m.x123)**2 + (m.x186 - m.x202)
    **2)**(-3) - 2) + ((m.x28 - m.x45)**2 + (m.x107 - m.x124)**2 + (m.x186 -
    m.x203)**2)**(-3) * (((m.x28 - m.x45)**2 + (m.x107 - m.x124)**2 + (m.x186
    - m.x203)**2)**(-3) - 2) + ((m.x28 - m.x46)**2 + (m.x107 - m.x125)**2 + (
    m.x186 - m.x204)**2)**(-3) * (((m.x28 - m.x46)**2 + (m.x107 - m.x125)**2 +
    (m.x186 - m.x204)**2)**(-3) - 2) + ((m.x28 - m.x47)**2 + (m.x107 - m.x126)
    **2 + (m.x186 - m.x205)**2)**(-3) * (((m.x28 - m.x47)**2 + (m.x107 - m.x126)
    **2 + (m.x186 - m.x205)**2)**(-3) - 2) + ((m.x28 - m.x48)**2 + (m.x107 -
    m.x127)**2 + (m.x186 - m.x206)**2)**(-3) * (((m.x28 - m.x48)**2 + (m.x107
    - m.x127)**2 + (m.x186 - m.x206)**2)**(-3) - 2) + ((m.x28 - m.x49)**2 + (
    m.x107 - m.x128)**2 + (m.x186 - m.x207)**2)**(-3) * (((m.x28 - m.x49)**2 +
    (m.x107 - m.x128)**2 + (m.x186 - m.x207)**2)**(-3) - 2) + ((m.x28 - m.x50)
    **2 + (m.x107 - m.x129)**2 + (m.x186 - m.x208)**2)**(-3) * (((m.x28 - m.x50)
    **2 + (m.x107 - m.x129)**2 + (m.x186 - m.x208)**2)**(-3) - 2) + ((m.x28 -
    m.x51)**2 + (m.x107 - m.x130)**2 + (m.x186 - m.x209)**2)**(-3) * (((m.x28
    - m.x51)**2 + (m.x107 - m.x130)**2 + (m.x186 - m.x209)**2)**(-3) - 2) + ((
    m.x28 - m.x52)**2 + (m.x107 - m.x131)**2 + (m.x186 - m.x210)**2)**(-3) * ((
    (m.x28 - m.x52)**2 + (m.x107 - m.x131)**2 + (m.x186 - m.x210)**2)**(-3) - 2)
    + ((m.x28 - m.x53)**2 + (m.x107 - m.x132)**2 + (m.x186 - m.x211)**2)**(-3)
    * (((m.x28 - m.x53)**2 + (m.x107 - m.x132)**2 + (m.x186 - m.x211)**2)**(-3)
    - 2) + ((m.x28 - m.x54)**2 + (m.x107 - m.x133)**2 + (m.x186 - m.x212)**2)
    **(-3) * (((m.x28 - m.x54)**2 + (m.x107 - m.x133)**2 + (m.x186 - m.x212)**2)
    **(-3) - 2) + ((m.x28 - m.x55)**2 + (m.x107 - m.x134)**2 + (m.x186 - m.x213)
    **2)**(-3) * (((m.x28 - m.x55)**2 + (m.x107 - m.x134)**2 + (m.x186 - m.x213)
    **2)**(-3) - 2) + ((m.x28 - m.x56)**2 + (m.x107 - m.x135)**2 + (m.x186 -
    m.x214)**2)**(-3) * (((m.x28 - m.x56)**2 + (m.x107 - m.x135)**2 + (m.x186
    - m.x214)**2)**(-3) - 2) + ((m.x28 - m.x57)**2 + (m.x107 - m.x136)**2 + (
    m.x186 - m.x215)**2)**(-3) * (((m.x28 - m.x57)**2 + (m.x107 - m.x136)**2 +
    (m.x186 - m.x215)**2)**(-3) - 2) + ((m.x28 - m.x58)**2 + (m.x107 - m.x137)
    **2 + (m.x186 - m.x216)**2)**(-3) * (((m.x28 - m.x58)**2 + (m.x107 - m.x137)
    **2 + (m.x186 - m.x216)**2)**(-3) - 2) + ((m.x28 - m.x59)**2 + (m.x107 -
    m.x138)**2 + (m.x186 - m.x217)**2)**(-3) * (((m.x28 - m.x59)**2 + (m.x107
    - m.x138)**2 + (m.x186 - m.x217)**2)**(-3) - 2) + ((m.x28 - m.x60)**2 + (
    m.x107 - m.x139)**2 + (m.x186 - m.x218)**2)**(-3) * (((m.x28 - m.x60)**2 +
    (m.x107 - m.x139)**2 + (m.x186 - m.x218)**2)**(-3) - 2) + ((m.x28 - m.x61)
    **2 + (m.x107 - m.x140)**2 + (m.x186 - m.x219)**2)**(-3) * (((m.x28 - m.x61)
    **2 + (m.x107 - m.x140)**2 + (m.x186 - m.x219)**2)**(-3) - 2) + ((m.x28 -
    m.x62)**2 + (m.x107 - m.x141)**2 + (m.x186 - m.x220)**2)**(-3) * (((m.x28
    - m.x62)**2 + (m.x107 - m.x141)**2 + (m.x186 - m.x220)**2)**(-3) - 2) + ((
    m.x28 - m.x63)**2 + (m.x107 - m.x142)**2 + (m.x186 - m.x221)**2)**(-3) * ((
    (m.x28 - m.x63)**2 + (m.x107 - m.x142)**2 + (m.x186 - m.x221)**2)**(-3) - 2)
    + ((m.x28 - m.x64)**2 + (m.x107 - m.x143)**2 + (m.x186 - m.x222)**2)**(-3)
    * (((m.x28 - m.x64)**2 + (m.x107 - m.x143)**2 + (m.x186 - m.x222)**2)**(-3)
    - 2) + ((m.x28 - m.x65)**2 + (m.x107 - m.x144)**2 + (m.x186 - m.x223)**2)
    **(-3) * (((m.x28 - m.x65)**2 + (m.x107 - m.x144)**2 + (m.x186 - m.x223)**2)
    **(-3) - 2) + ((m.x28 - m.x66)**2 + (m.x107 - m.x145)**2 + (m.x186 - m.x224)
    **2)**(-3) * (((m.x28 - m.x66)**2 + (m.x107 - m.x145)**2 + (m.x186 - m.x224)
    **2)**(-3) - 2) + ((m.x28 - m.x67)**2 + (m.x107 - m.x146)**2 + (m.x186 -
    m.x225)**2)**(-3) * (((m.x28 - m.x67)**2 + (m.x107 - m.x146)**2 + (m.x186
    - m.x225)**2)**(-3) - 2) + ((m.x28 - m.x68)**2 + (m.x107 - m.x147)**2 + (
    m.x186 - m.x226)**2)**(-3) * (((m.x28 - m.x68)**2 + (m.x107 - m.x147)**2 +
    (m.x186 - m.x226)**2)**(-3) - 2) + ((m.x28 - m.x69)**2 + (m.x107 - m.x148)
    **2 + (m.x186 - m.x227)**2)**(-3) * (((m.x28 - m.x69)**2 + (m.x107 - m.x148)
    **2 + (m.x186 - m.x227)**2)**(-3) - 2) + ((m.x28 - m.x70)**2 + (m.x107 -
    m.x149)**2 + (m.x186 - m.x228)**2)**(-3) * (((m.x28 - m.x70)**2 + (m.x107
    - m.x149)**2 + (m.x186 - m.x228)**2)**(-3) - 2) + ((m.x28 - m.x71)**2 + (
    m.x107 - m.x150)**2 + (m.x186 - m.x229)**2)**(-3) * (((m.x28 - m.x71)**2 +
    (m.x107 - m.x150)**2 + (m.x186 - m.x229)**2)**(-3) - 2) + ((m.x28 - m.x72)
    **2 + (m.x107 - m.x151)**2 + (m.x186 - m.x230)**2)**(-3) * (((m.x28 - m.x72)
    **2 + (m.x107 - m.x151)**2 + (m.x186 - m.x230)**2)**(-3) - 2) + ((m.x28 -
    m.x73)**2 + (m.x107 - m.x152)**2 + (m.x186 - m.x231)**2)**(-3) * (((m.x28
    - m.x73)**2 + (m.x107 - m.x152)**2 + (m.x186 - m.x231)**2)**(-3) - 2) + ((
    m.x28 - m.x74)**2 + (m.x107 - m.x153)**2 + (m.x186 - m.x232)**2)**(-3) * ((
    (m.x28 - m.x74)**2 + (m.x107 - m.x153)**2 + (m.x186 - m.x232)**2)**(-3) - 2)
    + ((m.x28 - m.x75)**2 + (m.x107 - m.x154)**2 + (m.x186 - m.x233)**2)**(-3)
    * (((m.x28 - m.x75)**2 + (m.x107 - m.x154)**2 + (m.x186 - m.x233)**2)**(-3)
    - 2) + ((m.x28 - m.x76)**2 + (m.x107 - m.x155)**2 + (m.x186 - m.x234)**2)
    **(-3) * (((m.x28 - m.x76)**2 + (m.x107 - m.x155)**2 + (m.x186 - m.x234)**2)
    **(-3) - 2) + ((m.x28 - m.x77)**2 + (m.x107 - m.x156)**2 + (m.x186 - m.x235)
    **2)**(-3) * (((m.x28 - m.x77)**2 + (m.x107 - m.x156)**2 + (m.x186 - m.x235)
    **2)**(-3) - 2) + ((m.x28 - m.x78)**2 + (m.x107 - m.x157)**2 + (m.x186 -
    m.x236)**2)**(-3) * (((m.x28 - m.x78)**2 + (m.x107 - m.x157)**2 + (m.x186
    - m.x236)**2)**(-3) - 2) + ((m.x28 - m.x79)**2 + (m.x107 - m.x158)**2 + (
    m.x186 - m.x237)**2)**(-3) * (((m.x28 - m.x79)**2 + (m.x107 - m.x158)**2 +
    (m.x186 - m.x237)**2)**(-3) - 2) + ((m.x29 - m.x30)**2 + (m.x108 - m.x109)
    **2 + (m.x187 - m.x188)**2)**(-3) * (((m.x29 - m.x30)**2 + (m.x108 - m.x109)
    **2 + (m.x187 - m.x188)**2)**(-3) - 2) + ((m.x29 - m.x31)**2 + (m.x108 -
    m.x110)**2 + (m.x187 - m.x189)**2)**(-3) * (((m.x29 - m.x31)**2 + (m.x108
    - m.x110)**2 + (m.x187 - m.x189)**2)**(-3) - 2) + ((m.x29 - m.x32)**2 + (
    m.x108 - m.x111)**2 + (m.x187 - m.x190)**2)**(-3) * (((m.x29 - m.x32)**2 +
    (m.x108 - m.x111)**2 + (m.x187 - m.x190)**2)**(-3) - 2) + ((m.x29 - m.x33)
    **2 + (m.x108 - m.x112)**2 + (m.x187 - m.x191)**2)**(-3) * (((m.x29 - m.x33)
    **2 + (m.x108 - m.x112)**2 + (m.x187 - m.x191)**2)**(-3) - 2) + ((m.x29 -
    m.x34)**2 + (m.x108 - m.x113)**2 + (m.x187 - m.x192)**2)**(-3) * (((m.x29
    - m.x34)**2 + (m.x108 - m.x113)**2 + (m.x187 - m.x192)**2)**(-3) - 2) + ((
    m.x29 - m.x35)**2 + (m.x108 - m.x114)**2 + (m.x187 - m.x193)**2)**(-3) * ((
    (m.x29 - m.x35)**2 + (m.x108 - m.x114)**2 + (m.x187 - m.x193)**2)**(-3) - 2)
    + ((m.x29 - m.x36)**2 + (m.x108 - m.x115)**2 + (m.x187 - m.x194)**2)**(-3)
    * (((m.x29 - m.x36)**2 + (m.x108 - m.x115)**2 + (m.x187 - m.x194)**2)**(-3)
    - 2) + ((m.x29 - m.x37)**2 + (m.x108 - m.x116)**2 + (m.x187 - m.x195)**2)
    **(-3) * (((m.x29 - m.x37)**2 + (m.x108 - m.x116)**2 + (m.x187 - m.x195)**2)
    **(-3) - 2) + ((m.x29 - m.x38)**2 + (m.x108 - m.x117)**2 + (m.x187 - m.x196)
    **2)**(-3) * (((m.x29 - m.x38)**2 + (m.x108 - m.x117)**2 + (m.x187 - m.x196)
    **2)**(-3) - 2) + ((m.x29 - m.x39)**2 + (m.x108 - m.x118)**2 + (m.x187 -
    m.x197)**2)**(-3) * (((m.x29 - m.x39)**2 + (m.x108 - m.x118)**2 + (m.x187
    - m.x197)**2)**(-3) - 2) + ((m.x29 - m.x40)**2 + (m.x108 - m.x119)**2 + (
    m.x187 - m.x198)**2)**(-3) * (((m.x29 - m.x40)**2 + (m.x108 - m.x119)**2 +
    (m.x187 - m.x198)**2)**(-3) - 2) + ((m.x29 - m.x41)**2 + (m.x108 - m.x120)
    **2 + (m.x187 - m.x199)**2)**(-3) * (((m.x29 - m.x41)**2 + (m.x108 - m.x120)
    **2 + (m.x187 - m.x199)**2)**(-3) - 2) + ((m.x29 - m.x42)**2 + (m.x108 -
    m.x121)**2 + (m.x187 - m.x200)**2)**(-3) * (((m.x29 - m.x42)**2 + (m.x108
    - m.x121)**2 + (m.x187 - m.x200)**2)**(-3) - 2) + ((m.x29 - m.x43)**2 + (
    m.x108 - m.x122)**2 + (m.x187 - m.x201)**2)**(-3) * (((m.x29 - m.x43)**2 +
    (m.x108 - m.x122)**2 + (m.x187 - m.x201)**2)**(-3) - 2) + ((m.x29 - m.x44)
    **2 + (m.x108 - m.x123)**2 + (m.x187 - m.x202)**2)**(-3) * (((m.x29 - m.x44)
    **2 + (m.x108 - m.x123)**2 + (m.x187 - m.x202)**2)**(-3) - 2) + ((m.x29 -
    m.x45)**2 + (m.x108 - m.x124)**2 + (m.x187 - m.x203)**2)**(-3) * (((m.x29
    - m.x45)**2 + (m.x108 - m.x124)**2 + (m.x187 - m.x203)**2)**(-3) - 2) + ((
    m.x29 - m.x46)**2 + (m.x108 - m.x125)**2 + (m.x187 - m.x204)**2)**(-3) * ((
    (m.x29 - m.x46)**2 + (m.x108 - m.x125)**2 + (m.x187 - m.x204)**2)**(-3) - 2)
    + ((m.x29 - m.x47)**2 + (m.x108 - m.x126)**2 + (m.x187 - m.x205)**2)**(-3)
    * (((m.x29 - m.x47)**2 + (m.x108 - m.x126)**2 + (m.x187 - m.x205)**2)**(-3)
    - 2) + ((m.x29 - m.x48)**2 + (m.x108 - m.x127)**2 + (m.x187 - m.x206)**2)
    **(-3) * (((m.x29 - m.x48)**2 + (m.x108 - m.x127)**2 + (m.x187 - m.x206)**2)
    **(-3) - 2) + ((m.x29 - m.x49)**2 + (m.x108 - m.x128)**2 + (m.x187 - m.x207)
    **2)**(-3) * (((m.x29 - m.x49)**2 + (m.x108 - m.x128)**2 + (m.x187 - m.x207)
    **2)**(-3) - 2) + ((m.x29 - m.x50)**2 + (m.x108 - m.x129)**2 + (m.x187 -
    m.x208)**2)**(-3) * (((m.x29 - m.x50)**2 + (m.x108 - m.x129)**2 + (m.x187
    - m.x208)**2)**(-3) - 2) + ((m.x29 - m.x51)**2 + (m.x108 - m.x130)**2 + (
    m.x187 - m.x209)**2)**(-3) * (((m.x29 - m.x51)**2 + (m.x108 - m.x130)**2 +
    (m.x187 - m.x209)**2)**(-3) - 2) + ((m.x29 - m.x52)**2 + (m.x108 - m.x131)
    **2 + (m.x187 - m.x210)**2)**(-3) * (((m.x29 - m.x52)**2 + (m.x108 - m.x131)
    **2 + (m.x187 - m.x210)**2)**(-3) - 2) + ((m.x29 - m.x53)**2 + (m.x108 -
    m.x132)**2 + (m.x187 - m.x211)**2)**(-3) * (((m.x29 - m.x53)**2 + (m.x108
    - m.x132)**2 + (m.x187 - m.x211)**2)**(-3) - 2) + ((m.x29 - m.x54)**2 + (
    m.x108 - m.x133)**2 + (m.x187 - m.x212)**2)**(-3) * (((m.x29 - m.x54)**2 +
    (m.x108 - m.x133)**2 + (m.x187 - m.x212)**2)**(-3) - 2) + ((m.x29 - m.x55)
    **2 + (m.x108 - m.x134)**2 + (m.x187 - m.x213)**2)**(-3) * (((m.x29 - m.x55)
    **2 + (m.x108 - m.x134)**2 + (m.x187 - m.x213)**2)**(-3) - 2) + ((m.x29 -
    m.x56)**2 + (m.x108 - m.x135)**2 + (m.x187 - m.x214)**2)**(-3) * (((m.x29
    - m.x56)**2 + (m.x108 - m.x135)**2 + (m.x187 - m.x214)**2)**(-3) - 2) + ((
    m.x29 - m.x57)**2 + (m.x108 - m.x136)**2 + (m.x187 - m.x215)**2)**(-3) * ((
    (m.x29 - m.x57)**2 + (m.x108 - m.x136)**2 + (m.x187 - m.x215)**2)**(-3) - 2)
    + ((m.x29 - m.x58)**2 + (m.x108 - m.x137)**2 + (m.x187 - m.x216)**2)**(-3)
    * (((m.x29 - m.x58)**2 + (m.x108 - m.x137)**2 + (m.x187 - m.x216)**2)**(-3)
    - 2) + ((m.x29 - m.x59)**2 + (m.x108 - m.x138)**2 + (m.x187 - m.x217)**2)
    **(-3) * (((m.x29 - m.x59)**2 + (m.x108 - m.x138)**2 + (m.x187 - m.x217)**2)
    **(-3) - 2) + ((m.x29 - m.x60)**2 + (m.x108 - m.x139)**2 + (m.x187 - m.x218)
    **2)**(-3) * (((m.x29 - m.x60)**2 + (m.x108 - m.x139)**2 + (m.x187 - m.x218)
    **2)**(-3) - 2) + ((m.x29 - m.x61)**2 + (m.x108 - m.x140)**2 + (m.x187 -
    m.x219)**2)**(-3) * (((m.x29 - m.x61)**2 + (m.x108 - m.x140)**2 + (m.x187
    - m.x219)**2)**(-3) - 2) + ((m.x29 - m.x62)**2 + (m.x108 - m.x141)**2 + (
    m.x187 - m.x220)**2)**(-3) * (((m.x29 - m.x62)**2 + (m.x108 - m.x141)**2 +
    (m.x187 - m.x220)**2)**(-3) - 2) + ((m.x29 - m.x63)**2 + (m.x108 - m.x142)
    **2 + (m.x187 - m.x221)**2)**(-3) * (((m.x29 - m.x63)**2 + (m.x108 - m.x142)
    **2 + (m.x187 - m.x221)**2)**(-3) - 2) + ((m.x29 - m.x64)**2 + (m.x108 -
    m.x143)**2 + (m.x187 - m.x222)**2)**(-3) * (((m.x29 - m.x64)**2 + (m.x108
    - m.x143)**2 + (m.x187 - m.x222)**2)**(-3) - 2) + ((m.x29 - m.x65)**2 + (
    m.x108 - m.x144)**2 + (m.x187 - m.x223)**2)**(-3) * (((m.x29 - m.x65)**2 +
    (m.x108 - m.x144)**2 + (m.x187 - m.x223)**2)**(-3) - 2) + ((m.x29 - m.x66)
    **2 + (m.x108 - m.x145)**2 + (m.x187 - m.x224)**2)**(-3) * (((m.x29 - m.x66)
    **2 + (m.x108 - m.x145)**2 + (m.x187 - m.x224)**2)**(-3) - 2) + ((m.x29 -
    m.x67)**2 + (m.x108 - m.x146)**2 + (m.x187 - m.x225)**2)**(-3) * (((m.x29
    - m.x67)**2 + (m.x108 - m.x146)**2 + (m.x187 - m.x225)**2)**(-3) - 2) + ((
    m.x29 - m.x68)**2 + (m.x108 - m.x147)**2 + (m.x187 - m.x226)**2)**(-3) * ((
    (m.x29 - m.x68)**2 + (m.x108 - m.x147)**2 + (m.x187 - m.x226)**2)**(-3) - 2)
    + ((m.x29 - m.x69)**2 + (m.x108 - m.x148)**2 + (m.x187 - m.x227)**2)**(-3)
    * (((m.x29 - m.x69)**2 + (m.x108 - m.x148)**2 + (m.x187 - m.x227)**2)**(-3)
    - 2) + ((m.x29 - m.x70)**2 + (m.x108 - m.x149)**2 + (m.x187 - m.x228)**2)
    **(-3) * (((m.x29 - m.x70)**2 + (m.x108 - m.x149)**2 + (m.x187 - m.x228)**2)
    **(-3) - 2) + ((m.x29 - m.x71)**2 + (m.x108 - m.x150)**2 + (m.x187 - m.x229)
    **2)**(-3) * (((m.x29 - m.x71)**2 + (m.x108 - m.x150)**2 + (m.x187 - m.x229)
    **2)**(-3) - 2) + ((m.x29 - m.x72)**2 + (m.x108 - m.x151)**2 + (m.x187 -
    m.x230)**2)**(-3) * (((m.x29 - m.x72)**2 + (m.x108 - m.x151)**2 + (m.x187
    - m.x230)**2)**(-3) - 2) + ((m.x29 - m.x73)**2 + (m.x108 - m.x152)**2 + (
    m.x187 - m.x231)**2)**(-3) * (((m.x29 - m.x73)**2 + (m.x108 - m.x152)**2 +
    (m.x187 - m.x231)**2)**(-3) - 2) + ((m.x29 - m.x74)**2 + (m.x108 - m.x153)
    **2 + (m.x187 - m.x232)**2)**(-3) * (((m.x29 - m.x74)**2 + (m.x108 - m.x153)
    **2 + (m.x187 - m.x232)**2)**(-3) - 2) + ((m.x29 - m.x75)**2 + (m.x108 -
    m.x154)**2 + (m.x187 - m.x233)**2)**(-3) * (((m.x29 - m.x75)**2 + (m.x108
    - m.x154)**2 + (m.x187 - m.x233)**2)**(-3) - 2) + ((m.x29 - m.x76)**2 + (
    m.x108 - m.x155)**2 + (m.x187 - m.x234)**2)**(-3) * (((m.x29 - m.x76)**2 +
    (m.x108 - m.x155)**2 + (m.x187 - m.x234)**2)**(-3) - 2) + ((m.x29 - m.x77)
    **2 + (m.x108 - m.x156)**2 + (m.x187 - m.x235)**2)**(-3) * (((m.x29 - m.x77)
    **2 + (m.x108 - m.x156)**2 + (m.x187 - m.x235)**2)**(-3) - 2) + ((m.x29 -
    m.x78)**2 + (m.x108 - m.x157)**2 + (m.x187 - m.x236)**2)**(-3) * (((m.x29
    - m.x78)**2 + (m.x108 - m.x157)**2 + (m.x187 - m.x236)**2)**(-3) - 2) + ((
    m.x29 - m.x79)**2 + (m.x108 - m.x158)**2 + (m.x187 - m.x237)**2)**(-3) * ((
    (m.x29 - m.x79)**2 + (m.x108 - m.x158)**2 + (m.x187 - m.x237)**2)**(-3) - 2)
    + ((m.x30 - m.x31)**2 + (m.x109 - m.x110)**2 + (m.x188 - m.x189)**2)**(-3)
    * (((m.x30 - m.x31)**2 + (m.x109 - m.x110)**2 + (m.x188 - m.x189)**2)**(-3)
    - 2) + ((m.x30 - m.x32)**2 + (m.x109 - m.x111)**2 + (m.x188 - m.x190)**2)
    **(-3) * (((m.x30 - m.x32)**2 + (m.x109 - m.x111)**2 + (m.x188 - m.x190)**2)
    **(-3) - 2) + ((m.x30 - m.x33)**2 + (m.x109 - m.x112)**2 + (m.x188 - m.x191)
    **2)**(-3) * (((m.x30 - m.x33)**2 + (m.x109 - m.x112)**2 + (m.x188 - m.x191)
    **2)**(-3) - 2) + ((m.x30 - m.x34)**2 + (m.x109 - m.x113)**2 + (m.x188 -
    m.x192)**2)**(-3) * (((m.x30 - m.x34)**2 + (m.x109 - m.x113)**2 + (m.x188
    - m.x192)**2)**(-3) - 2) + ((m.x30 - m.x35)**2 + (m.x109 - m.x114)**2 + (
    m.x188 - m.x193)**2)**(-3) * (((m.x30 - m.x35)**2 + (m.x109 - m.x114)**2 +
    (m.x188 - m.x193)**2)**(-3) - 2) + ((m.x30 - m.x36)**2 + (m.x109 - m.x115)
    **2 + (m.x188 - m.x194)**2)**(-3) * (((m.x30 - m.x36)**2 + (m.x109 - m.x115)
    **2 + (m.x188 - m.x194)**2)**(-3) - 2) + ((m.x30 - m.x37)**2 + (m.x109 -
    m.x116)**2 + (m.x188 - m.x195)**2)**(-3) * (((m.x30 - m.x37)**2 + (m.x109
    - m.x116)**2 + (m.x188 - m.x195)**2)**(-3) - 2) + ((m.x30 - m.x38)**2 + (
    m.x109 - m.x117)**2 + (m.x188 - m.x196)**2)**(-3) * (((m.x30 - m.x38)**2 +
    (m.x109 - m.x117)**2 + (m.x188 - m.x196)**2)**(-3) - 2) + ((m.x30 - m.x39)
    **2 + (m.x109 - m.x118)**2 + (m.x188 - m.x197)**2)**(-3) * (((m.x30 - m.x39)
    **2 + (m.x109 - m.x118)**2 + (m.x188 - m.x197)**2)**(-3) - 2) + ((m.x30 -
    m.x40)**2 + (m.x109 - m.x119)**2 + (m.x188 - m.x198)**2)**(-3) * (((m.x30
    - m.x40)**2 + (m.x109 - m.x119)**2 + (m.x188 - m.x198)**2)**(-3) - 2) + ((
    m.x30 - m.x41)**2 + (m.x109 - m.x120)**2 + (m.x188 - m.x199)**2)**(-3) * ((
    (m.x30 - m.x41)**2 + (m.x109 - m.x120)**2 + (m.x188 - m.x199)**2)**(-3) - 2)
    + ((m.x30 - m.x42)**2 + (m.x109 - m.x121)**2 + (m.x188 - m.x200)**2)**(-3)
    * (((m.x30 - m.x42)**2 + (m.x109 - m.x121)**2 + (m.x188 - m.x200)**2)**(-3)
    - 2) + ((m.x30 - m.x43)**2 + (m.x109 - m.x122)**2 + (m.x188 - m.x201)**2)
    **(-3) * (((m.x30 - m.x43)**2 + (m.x109 - m.x122)**2 + (m.x188 - m.x201)**2)
    **(-3) - 2) + ((m.x30 - m.x44)**2 + (m.x109 - m.x123)**2 + (m.x188 - m.x202)
    **2)**(-3) * (((m.x30 - m.x44)**2 + (m.x109 - m.x123)**2 + (m.x188 - m.x202)
    **2)**(-3) - 2) + ((m.x30 - m.x45)**2 + (m.x109 - m.x124)**2 + (m.x188 -
    m.x203)**2)**(-3) * (((m.x30 - m.x45)**2 + (m.x109 - m.x124)**2 + (m.x188
    - m.x203)**2)**(-3) - 2) + ((m.x30 - m.x46)**2 + (m.x109 - m.x125)**2 + (
    m.x188 - m.x204)**2)**(-3) * (((m.x30 - m.x46)**2 + (m.x109 - m.x125)**2 +
    (m.x188 - m.x204)**2)**(-3) - 2) + ((m.x30 - m.x47)**2 + (m.x109 - m.x126)
    **2 + (m.x188 - m.x205)**2)**(-3) * (((m.x30 - m.x47)**2 + (m.x109 - m.x126)
    **2 + (m.x188 - m.x205)**2)**(-3) - 2) + ((m.x30 - m.x48)**2 + (m.x109 -
    m.x127)**2 + (m.x188 - m.x206)**2)**(-3) * (((m.x30 - m.x48)**2 + (m.x109
    - m.x127)**2 + (m.x188 - m.x206)**2)**(-3) - 2) + ((m.x30 - m.x49)**2 + (
    m.x109 - m.x128)**2 + (m.x188 - m.x207)**2)**(-3) * (((m.x30 - m.x49)**2 +
    (m.x109 - m.x128)**2 + (m.x188 - m.x207)**2)**(-3) - 2) + ((m.x30 - m.x50)
    **2 + (m.x109 - m.x129)**2 + (m.x188 - m.x208)**2)**(-3) * (((m.x30 - m.x50)
    **2 + (m.x109 - m.x129)**2 + (m.x188 - m.x208)**2)**(-3) - 2) + ((m.x30 -
    m.x51)**2 + (m.x109 - m.x130)**2 + (m.x188 - m.x209)**2)**(-3) * (((m.x30
    - m.x51)**2 + (m.x109 - m.x130)**2 + (m.x188 - m.x209)**2)**(-3) - 2) + ((
    m.x30 - m.x52)**2 + (m.x109 - m.x131)**2 + (m.x188 - m.x210)**2)**(-3) * ((
    (m.x30 - m.x52)**2 + (m.x109 - m.x131)**2 + (m.x188 - m.x210)**2)**(-3) - 2)
    + ((m.x30 - m.x53)**2 + (m.x109 - m.x132)**2 + (m.x188 - m.x211)**2)**(-3)
    * (((m.x30 - m.x53)**2 + (m.x109 - m.x132)**2 + (m.x188 - m.x211)**2)**(-3)
    - 2) + ((m.x30 - m.x54)**2 + (m.x109 - m.x133)**2 + (m.x188 - m.x212)**2)
    **(-3) * (((m.x30 - m.x54)**2 + (m.x109 - m.x133)**2 + (m.x188 - m.x212)**2)
    **(-3) - 2) + ((m.x30 - m.x55)**2 + (m.x109 - m.x134)**2 + (m.x188 - m.x213)
    **2)**(-3) * (((m.x30 - m.x55)**2 + (m.x109 - m.x134)**2 + (m.x188 - m.x213)
    **2)**(-3) - 2) + ((m.x30 - m.x56)**2 + (m.x109 - m.x135)**2 + (m.x188 -
    m.x214)**2)**(-3) * (((m.x30 - m.x56)**2 + (m.x109 - m.x135)**2 + (m.x188
    - m.x214)**2)**(-3) - 2) + ((m.x30 - m.x57)**2 + (m.x109 - m.x136)**2 + (
    m.x188 - m.x215)**2)**(-3) * (((m.x30 - m.x57)**2 + (m.x109 - m.x136)**2 +
    (m.x188 - m.x215)**2)**(-3) - 2) + ((m.x30 - m.x58)**2 + (m.x109 - m.x137)
    **2 + (m.x188 - m.x216)**2)**(-3) * (((m.x30 - m.x58)**2 + (m.x109 - m.x137)
    **2 + (m.x188 - m.x216)**2)**(-3) - 2) + ((m.x30 - m.x59)**2 + (m.x109 -
    m.x138)**2 + (m.x188 - m.x217)**2)**(-3) * (((m.x30 - m.x59)**2 + (m.x109
    - m.x138)**2 + (m.x188 - m.x217)**2)**(-3) - 2) + ((m.x30 - m.x60)**2 + (
    m.x109 - m.x139)**2 + (m.x188 - m.x218)**2)**(-3) * (((m.x30 - m.x60)**2 +
    (m.x109 - m.x139)**2 + (m.x188 - m.x218)**2)**(-3) - 2) + ((m.x30 - m.x61)
    **2 + (m.x109 - m.x140)**2 + (m.x188 - m.x219)**2)**(-3) * (((m.x30 - m.x61)
    **2 + (m.x109 - m.x140)**2 + (m.x188 - m.x219)**2)**(-3) - 2) + ((m.x30 -
    m.x62)**2 + (m.x109 - m.x141)**2 + (m.x188 - m.x220)**2)**(-3) * (((m.x30
    - m.x62)**2 + (m.x109 - m.x141)**2 + (m.x188 - m.x220)**2)**(-3) - 2) + ((
    m.x30 - m.x63)**2 + (m.x109 - m.x142)**2 + (m.x188 - m.x221)**2)**(-3) * ((
    (m.x30 - m.x63)**2 + (m.x109 - m.x142)**2 + (m.x188 - m.x221)**2)**(-3) - 2)
    + ((m.x30 - m.x64)**2 + (m.x109 - m.x143)**2 + (m.x188 - m.x222)**2)**(-3)
    * (((m.x30 - m.x64)**2 + (m.x109 - m.x143)**2 + (m.x188 - m.x222)**2)**(-3)
    - 2) + ((m.x30 - m.x65)**2 + (m.x109 - m.x144)**2 + (m.x188 - m.x223)**2)
    **(-3) * (((m.x30 - m.x65)**2 + (m.x109 - m.x144)**2 + (m.x188 - m.x223)**2)
    **(-3) - 2) + ((m.x30 - m.x66)**2 + (m.x109 - m.x145)**2 + (m.x188 - m.x224)
    **2)**(-3) * (((m.x30 - m.x66)**2 + (m.x109 - m.x145)**2 + (m.x188 - m.x224)
    **2)**(-3) - 2) + ((m.x30 - m.x67)**2 + (m.x109 - m.x146)**2 + (m.x188 -
    m.x225)**2)**(-3) * (((m.x30 - m.x67)**2 + (m.x109 - m.x146)**2 + (m.x188
    - m.x225)**2)**(-3) - 2) + ((m.x30 - m.x68)**2 + (m.x109 - m.x147)**2 + (
    m.x188 - m.x226)**2)**(-3) * (((m.x30 - m.x68)**2 + (m.x109 - m.x147)**2 +
    (m.x188 - m.x226)**2)**(-3) - 2) + ((m.x30 - m.x69)**2 + (m.x109 - m.x148)
    **2 + (m.x188 - m.x227)**2)**(-3) * (((m.x30 - m.x69)**2 + (m.x109 - m.x148)
    **2 + (m.x188 - m.x227)**2)**(-3) - 2) + ((m.x30 - m.x70)**2 + (m.x109 -
    m.x149)**2 + (m.x188 - m.x228)**2)**(-3) * (((m.x30 - m.x70)**2 + (m.x109
    - m.x149)**2 + (m.x188 - m.x228)**2)**(-3) - 2) + ((m.x30 - m.x71)**2 + (
    m.x109 - m.x150)**2 + (m.x188 - m.x229)**2)**(-3) * (((m.x30 - m.x71)**2 +
    (m.x109 - m.x150)**2 + (m.x188 - m.x229)**2)**(-3) - 2) + ((m.x30 - m.x72)
    **2 + (m.x109 - m.x151)**2 + (m.x188 - m.x230)**2)**(-3) * (((m.x30 - m.x72)
    **2 + (m.x109 - m.x151)**2 + (m.x188 - m.x230)**2)**(-3) - 2) + ((m.x30 -
    m.x73)**2 + (m.x109 - m.x152)**2 + (m.x188 - m.x231)**2)**(-3) * (((m.x30
    - m.x73)**2 + (m.x109 - m.x152)**2 + (m.x188 - m.x231)**2)**(-3) - 2) + ((
    m.x30 - m.x74)**2 + (m.x109 - m.x153)**2 + (m.x188 - m.x232)**2)**(-3) * ((
    (m.x30 - m.x74)**2 + (m.x109 - m.x153)**2 + (m.x188 - m.x232)**2)**(-3) - 2)
    + ((m.x30 - m.x75)**2 + (m.x109 - m.x154)**2 + (m.x188 - m.x233)**2)**(-3)
    * (((m.x30 - m.x75)**2 + (m.x109 - m.x154)**2 + (m.x188 - m.x233)**2)**(-3)
    - 2) + ((m.x30 - m.x76)**2 + (m.x109 - m.x155)**2 + (m.x188 - m.x234)**2)
    **(-3) * (((m.x30 - m.x76)**2 + (m.x109 - m.x155)**2 + (m.x188 - m.x234)**2)
    **(-3) - 2) + ((m.x30 - m.x77)**2 + (m.x109 - m.x156)**2 + (m.x188 - m.x235)
    **2)**(-3) * (((m.x30 - m.x77)**2 + (m.x109 - m.x156)**2 + (m.x188 - m.x235)
    **2)**(-3) - 2) + ((m.x30 - m.x78)**2 + (m.x109 - m.x157)**2 + (m.x188 -
    m.x236)**2)**(-3) * (((m.x30 - m.x78)**2 + (m.x109 - m.x157)**2 + (m.x188
    - m.x236)**2)**(-3) - 2) + ((m.x30 - m.x79)**2 + (m.x109 - m.x158)**2 + (
    m.x188 - m.x237)**2)**(-3) * (((m.x30 - m.x79)**2 + (m.x109 - m.x158)**2 +
    (m.x188 - m.x237)**2)**(-3) - 2) + ((m.x31 - m.x32)**2 + (m.x110 - m.x111)
    **2 + (m.x189 - m.x190)**2)**(-3) * (((m.x31 - m.x32)**2 + (m.x110 - m.x111)
    **2 + (m.x189 - m.x190)**2)**(-3) - 2) + ((m.x31 - m.x33)**2 + (m.x110 -
    m.x112)**2 + (m.x189 - m.x191)**2)**(-3) * (((m.x31 - m.x33)**2 + (m.x110
    - m.x112)**2 + (m.x189 - m.x191)**2)**(-3) - 2) + ((m.x31 - m.x34)**2 + (
    m.x110 - m.x113)**2 + (m.x189 - m.x192)**2)**(-3) * (((m.x31 - m.x34)**2 +
    (m.x110 - m.x113)**2 + (m.x189 - m.x192)**2)**(-3) - 2) + ((m.x31 - m.x35)
    **2 + (m.x110 - m.x114)**2 + (m.x189 - m.x193)**2)**(-3) * (((m.x31 - m.x35)
    **2 + (m.x110 - m.x114)**2 + (m.x189 - m.x193)**2)**(-3) - 2) + ((m.x31 -
    m.x36)**2 + (m.x110 - m.x115)**2 + (m.x189 - m.x194)**2)**(-3) * (((m.x31
    - m.x36)**2 + (m.x110 - m.x115)**2 + (m.x189 - m.x194)**2)**(-3) - 2) + ((
    m.x31 - m.x37)**2 + (m.x110 - m.x116)**2 + (m.x189 - m.x195)**2)**(-3) * ((
    (m.x31 - m.x37)**2 + (m.x110 - m.x116)**2 + (m.x189 - m.x195)**2)**(-3) - 2)
    + ((m.x31 - m.x38)**2 + (m.x110 - m.x117)**2 + (m.x189 - m.x196)**2)**(-3)
    * (((m.x31 - m.x38)**2 + (m.x110 - m.x117)**2 + (m.x189 - m.x196)**2)**(-3)
    - 2) + ((m.x31 - m.x39)**2 + (m.x110 - m.x118)**2 + (m.x189 - m.x197)**2)
    **(-3) * (((m.x31 - m.x39)**2 + (m.x110 - m.x118)**2 + (m.x189 - m.x197)**2)
    **(-3) - 2) + ((m.x31 - m.x40)**2 + (m.x110 - m.x119)**2 + (m.x189 - m.x198)
    **2)**(-3) * (((m.x31 - m.x40)**2 + (m.x110 - m.x119)**2 + (m.x189 - m.x198)
    **2)**(-3) - 2) + ((m.x31 - m.x41)**2 + (m.x110 - m.x120)**2 + (m.x189 -
    m.x199)**2)**(-3) * (((m.x31 - m.x41)**2 + (m.x110 - m.x120)**2 + (m.x189
    - m.x199)**2)**(-3) - 2) + ((m.x31 - m.x42)**2 + (m.x110 - m.x121)**2 + (
    m.x189 - m.x200)**2)**(-3) * (((m.x31 - m.x42)**2 + (m.x110 - m.x121)**2 +
    (m.x189 - m.x200)**2)**(-3) - 2) + ((m.x31 - m.x43)**2 + (m.x110 - m.x122)
    **2 + (m.x189 - m.x201)**2)**(-3) * (((m.x31 - m.x43)**2 + (m.x110 - m.x122)
    **2 + (m.x189 - m.x201)**2)**(-3) - 2) + ((m.x31 - m.x44)**2 + (m.x110 -
    m.x123)**2 + (m.x189 - m.x202)**2)**(-3) * (((m.x31 - m.x44)**2 + (m.x110
    - m.x123)**2 + (m.x189 - m.x202)**2)**(-3) - 2) + ((m.x31 - m.x45)**2 + (
    m.x110 - m.x124)**2 + (m.x189 - m.x203)**2)**(-3) * (((m.x31 - m.x45)**2 +
    (m.x110 - m.x124)**2 + (m.x189 - m.x203)**2)**(-3) - 2) + ((m.x31 - m.x46)
    **2 + (m.x110 - m.x125)**2 + (m.x189 - m.x204)**2)**(-3) * (((m.x31 - m.x46)
    **2 + (m.x110 - m.x125)**2 + (m.x189 - m.x204)**2)**(-3) - 2) + ((m.x31 -
    m.x47)**2 + (m.x110 - m.x126)**2 + (m.x189 - m.x205)**2)**(-3) * (((m.x31
    - m.x47)**2 + (m.x110 - m.x126)**2 + (m.x189 - m.x205)**2)**(-3) - 2) + ((
    m.x31 - m.x48)**2 + (m.x110 - m.x127)**2 + (m.x189 - m.x206)**2)**(-3) * ((
    (m.x31 - m.x48)**2 + (m.x110 - m.x127)**2 + (m.x189 - m.x206)**2)**(-3) - 2)
    + ((m.x31 - m.x49)**2 + (m.x110 - m.x128)**2 + (m.x189 - m.x207)**2)**(-3)
    * (((m.x31 - m.x49)**2 + (m.x110 - m.x128)**2 + (m.x189 - m.x207)**2)**(-3)
    - 2) + ((m.x31 - m.x50)**2 + (m.x110 - m.x129)**2 + (m.x189 - m.x208)**2)
    **(-3) * (((m.x31 - m.x50)**2 + (m.x110 - m.x129)**2 + (m.x189 - m.x208)**2)
    **(-3) - 2) + ((m.x31 - m.x51)**2 + (m.x110 - m.x130)**2 + (m.x189 - m.x209)
    **2)**(-3) * (((m.x31 - m.x51)**2 + (m.x110 - m.x130)**2 + (m.x189 - m.x209)
    **2)**(-3) - 2) + ((m.x31 - m.x52)**2 + (m.x110 - m.x131)**2 + (m.x189 -
    m.x210)**2)**(-3) * (((m.x31 - m.x52)**2 + (m.x110 - m.x131)**2 + (m.x189
    - m.x210)**2)**(-3) - 2) + ((m.x31 - m.x53)**2 + (m.x110 - m.x132)**2 + (
    m.x189 - m.x211)**2)**(-3) * (((m.x31 - m.x53)**2 + (m.x110 - m.x132)**2 +
    (m.x189 - m.x211)**2)**(-3) - 2) + ((m.x31 - m.x54)**2 + (m.x110 - m.x133)
    **2 + (m.x189 - m.x212)**2)**(-3) * (((m.x31 - m.x54)**2 + (m.x110 - m.x133)
    **2 + (m.x189 - m.x212)**2)**(-3) - 2) + ((m.x31 - m.x55)**2 + (m.x110 -
    m.x134)**2 + (m.x189 - m.x213)**2)**(-3) * (((m.x31 - m.x55)**2 + (m.x110
    - m.x134)**2 + (m.x189 - m.x213)**2)**(-3) - 2) + ((m.x31 - m.x56)**2 + (
    m.x110 - m.x135)**2 + (m.x189 - m.x214)**2)**(-3) * (((m.x31 - m.x56)**2 +
    (m.x110 - m.x135)**2 + (m.x189 - m.x214)**2)**(-3) - 2) + ((m.x31 - m.x57)
    **2 + (m.x110 - m.x136)**2 + (m.x189 - m.x215)**2)**(-3) * (((m.x31 - m.x57)
    **2 + (m.x110 - m.x136)**2 + (m.x189 - m.x215)**2)**(-3) - 2) + ((m.x31 -
    m.x58)**2 + (m.x110 - m.x137)**2 + (m.x189 - m.x216)**2)**(-3) * (((m.x31
    - m.x58)**2 + (m.x110 - m.x137)**2 + (m.x189 - m.x216)**2)**(-3) - 2) + ((
    m.x31 - m.x59)**2 + (m.x110 - m.x138)**2 + (m.x189 - m.x217)**2)**(-3) * ((
    (m.x31 - m.x59)**2 + (m.x110 - m.x138)**2 + (m.x189 - m.x217)**2)**(-3) - 2)
    + ((m.x31 - m.x60)**2 + (m.x110 - m.x139)**2 + (m.x189 - m.x218)**2)**(-3)
    * (((m.x31 - m.x60)**2 + (m.x110 - m.x139)**2 + (m.x189 - m.x218)**2)**(-3)
    - 2) + ((m.x31 - m.x61)**2 + (m.x110 - m.x140)**2 + (m.x189 - m.x219)**2)
    **(-3) * (((m.x31 - m.x61)**2 + (m.x110 - m.x140)**2 + (m.x189 - m.x219)**2)
    **(-3) - 2) + ((m.x31 - m.x62)**2 + (m.x110 - m.x141)**2 + (m.x189 - m.x220)
    **2)**(-3) * (((m.x31 - m.x62)**2 + (m.x110 - m.x141)**2 + (m.x189 - m.x220)
    **2)**(-3) - 2) + ((m.x31 - m.x63)**2 + (m.x110 - m.x142)**2 + (m.x189 -
    m.x221)**2)**(-3) * (((m.x31 - m.x63)**2 + (m.x110 - m.x142)**2 + (m.x189
    - m.x221)**2)**(-3) - 2) + ((m.x31 - m.x64)**2 + (m.x110 - m.x143)**2 + (
    m.x189 - m.x222)**2)**(-3) * (((m.x31 - m.x64)**2 + (m.x110 - m.x143)**2 +
    (m.x189 - m.x222)**2)**(-3) - 2) + ((m.x31 - m.x65)**2 + (m.x110 - m.x144)
    **2 + (m.x189 - m.x223)**2)**(-3) * (((m.x31 - m.x65)**2 + (m.x110 - m.x144)
    **2 + (m.x189 - m.x223)**2)**(-3) - 2) + ((m.x31 - m.x66)**2 + (m.x110 -
    m.x145)**2 + (m.x189 - m.x224)**2)**(-3) * (((m.x31 - m.x66)**2 + (m.x110
    - m.x145)**2 + (m.x189 - m.x224)**2)**(-3) - 2) + ((m.x31 - m.x67)**2 + (
    m.x110 - m.x146)**2 + (m.x189 - m.x225)**2)**(-3) * (((m.x31 - m.x67)**2 +
    (m.x110 - m.x146)**2 + (m.x189 - m.x225)**2)**(-3) - 2) + ((m.x31 - m.x68)
    **2 + (m.x110 - m.x147)**2 + (m.x189 - m.x226)**2)**(-3) * (((m.x31 - m.x68)
    **2 + (m.x110 - m.x147)**2 + (m.x189 - m.x226)**2)**(-3) - 2) + ((m.x31 -
    m.x69)**2 + (m.x110 - m.x148)**2 + (m.x189 - m.x227)**2)**(-3) * (((m.x31
    - m.x69)**2 + (m.x110 - m.x148)**2 + (m.x189 - m.x227)**2)**(-3) - 2) + ((
    m.x31 - m.x70)**2 + (m.x110 - m.x149)**2 + (m.x189 - m.x228)**2)**(-3) * ((
    (m.x31 - m.x70)**2 + (m.x110 - m.x149)**2 + (m.x189 - m.x228)**2)**(-3) - 2)
    + ((m.x31 - m.x71)**2 + (m.x110 - m.x150)**2 + (m.x189 - m.x229)**2)**(-3)
    * (((m.x31 - m.x71)**2 + (m.x110 - m.x150)**2 + (m.x189 - m.x229)**2)**(-3)
    - 2) + ((m.x31 - m.x72)**2 + (m.x110 - m.x151)**2 + (m.x189 - m.x230)**2)
    **(-3) * (((m.x31 - m.x72)**2 + (m.x110 - m.x151)**2 + (m.x189 - m.x230)**2)
    **(-3) - 2) + ((m.x31 - m.x73)**2 + (m.x110 - m.x152)**2 + (m.x189 - m.x231)
    **2)**(-3) * (((m.x31 - m.x73)**2 + (m.x110 - m.x152)**2 + (m.x189 - m.x231)
    **2)**(-3) - 2) + ((m.x31 - m.x74)**2 + (m.x110 - m.x153)**2 + (m.x189 -
    m.x232)**2)**(-3) * (((m.x31 - m.x74)**2 + (m.x110 - m.x153)**2 + (m.x189
    - m.x232)**2)**(-3) - 2) + ((m.x31 - m.x75)**2 + (m.x110 - m.x154)**2 + (
    m.x189 - m.x233)**2)**(-3) * (((m.x31 - m.x75)**2 + (m.x110 - m.x154)**2 +
    (m.x189 - m.x233)**2)**(-3) - 2) + ((m.x31 - m.x76)**2 + (m.x110 - m.x155)
    **2 + (m.x189 - m.x234)**2)**(-3) * (((m.x31 - m.x76)**2 + (m.x110 - m.x155)
    **2 + (m.x189 - m.x234)**2)**(-3) - 2) + ((m.x31 - m.x77)**2 + (m.x110 -
    m.x156)**2 + (m.x189 - m.x235)**2)**(-3) * (((m.x31 - m.x77)**2 + (m.x110
    - m.x156)**2 + (m.x189 - m.x235)**2)**(-3) - 2) + ((m.x31 - m.x78)**2 + (
    m.x110 - m.x157)**2 + (m.x189 - m.x236)**2)**(-3) * (((m.x31 - m.x78)**2 +
    (m.x110 - m.x157)**2 + (m.x189 - m.x236)**2)**(-3) - 2) + ((m.x31 - m.x79)
    **2 + (m.x110 - m.x158)**2 + (m.x189 - m.x237)**2)**(-3) * (((m.x31 - m.x79)
    **2 + (m.x110 - m.x158)**2 + (m.x189 - m.x237)**2)**(-3) - 2) + ((m.x32 -
    m.x33)**2 + (m.x111 - m.x112)**2 + (m.x190 - m.x191)**2)**(-3) * (((m.x32
    - m.x33)**2 + (m.x111 - m.x112)**2 + (m.x190 - m.x191)**2)**(-3) - 2) + ((
    m.x32 - m.x34)**2 + (m.x111 - m.x113)**2 + (m.x190 - m.x192)**2)**(-3) * ((
    (m.x32 - m.x34)**2 + (m.x111 - m.x113)**2 + (m.x190 - m.x192)**2)**(-3) - 2)
    + ((m.x32 - m.x35)**2 + (m.x111 - m.x114)**2 + (m.x190 - m.x193)**2)**(-3)
    * (((m.x32 - m.x35)**2 + (m.x111 - m.x114)**2 + (m.x190 - m.x193)**2)**(-3)
    - 2) + ((m.x32 - m.x36)**2 + (m.x111 - m.x115)**2 + (m.x190 - m.x194)**2)
    **(-3) * (((m.x32 - m.x36)**2 + (m.x111 - m.x115)**2 + (m.x190 - m.x194)**2)
    **(-3) - 2) + ((m.x32 - m.x37)**2 + (m.x111 - m.x116)**2 + (m.x190 - m.x195)
    **2)**(-3) * (((m.x32 - m.x37)**2 + (m.x111 - m.x116)**2 + (m.x190 - m.x195)
    **2)**(-3) - 2) + ((m.x32 - m.x38)**2 + (m.x111 - m.x117)**2 + (m.x190 -
    m.x196)**2)**(-3) * (((m.x32 - m.x38)**2 + (m.x111 - m.x117)**2 + (m.x190
    - m.x196)**2)**(-3) - 2) + ((m.x32 - m.x39)**2 + (m.x111 - m.x118)**2 + (
    m.x190 - m.x197)**2)**(-3) * (((m.x32 - m.x39)**2 + (m.x111 - m.x118)**2 +
    (m.x190 - m.x197)**2)**(-3) - 2) + ((m.x32 - m.x40)**2 + (m.x111 - m.x119)
    **2 + (m.x190 - m.x198)**2)**(-3) * (((m.x32 - m.x40)**2 + (m.x111 - m.x119)
    **2 + (m.x190 - m.x198)**2)**(-3) - 2) + ((m.x32 - m.x41)**2 + (m.x111 -
    m.x120)**2 + (m.x190 - m.x199)**2)**(-3) * (((m.x32 - m.x41)**2 + (m.x111
    - m.x120)**2 + (m.x190 - m.x199)**2)**(-3) - 2) + ((m.x32 - m.x42)**2 + (
    m.x111 - m.x121)**2 + (m.x190 - m.x200)**2)**(-3) * (((m.x32 - m.x42)**2 +
    (m.x111 - m.x121)**2 + (m.x190 - m.x200)**2)**(-3) - 2) + ((m.x32 - m.x43)
    **2 + (m.x111 - m.x122)**2 + (m.x190 - m.x201)**2)**(-3) * (((m.x32 - m.x43)
    **2 + (m.x111 - m.x122)**2 + (m.x190 - m.x201)**2)**(-3) - 2) + ((m.x32 -
    m.x44)**2 + (m.x111 - m.x123)**2 + (m.x190 - m.x202)**2)**(-3) * (((m.x32
    - m.x44)**2 + (m.x111 - m.x123)**2 + (m.x190 - m.x202)**2)**(-3) - 2) + ((
    m.x32 - m.x45)**2 + (m.x111 - m.x124)**2 + (m.x190 - m.x203)**2)**(-3) * ((
    (m.x32 - m.x45)**2 + (m.x111 - m.x124)**2 + (m.x190 - m.x203)**2)**(-3) - 2)
    + ((m.x32 - m.x46)**2 + (m.x111 - m.x125)**2 + (m.x190 - m.x204)**2)**(-3)
    * (((m.x32 - m.x46)**2 + (m.x111 - m.x125)**2 + (m.x190 - m.x204)**2)**(-3)
    - 2) + ((m.x32 - m.x47)**2 + (m.x111 - m.x126)**2 + (m.x190 - m.x205)**2)
    **(-3) * (((m.x32 - m.x47)**2 + (m.x111 - m.x126)**2 + (m.x190 - m.x205)**2)
    **(-3) - 2) + ((m.x32 - m.x48)**2 + (m.x111 - m.x127)**2 + (m.x190 - m.x206)
    **2)**(-3) * (((m.x32 - m.x48)**2 + (m.x111 - m.x127)**2 + (m.x190 - m.x206)
    **2)**(-3) - 2) + ((m.x32 - m.x49)**2 + (m.x111 - m.x128)**2 + (m.x190 -
    m.x207)**2)**(-3) * (((m.x32 - m.x49)**2 + (m.x111 - m.x128)**2 + (m.x190
    - m.x207)**2)**(-3) - 2) + ((m.x32 - m.x50)**2 + (m.x111 - m.x129)**2 + (
    m.x190 - m.x208)**2)**(-3) * (((m.x32 - m.x50)**2 + (m.x111 - m.x129)**2 +
    (m.x190 - m.x208)**2)**(-3) - 2) + ((m.x32 - m.x51)**2 + (m.x111 - m.x130)
    **2 + (m.x190 - m.x209)**2)**(-3) * (((m.x32 - m.x51)**2 + (m.x111 - m.x130)
    **2 + (m.x190 - m.x209)**2)**(-3) - 2) + ((m.x32 - m.x52)**2 + (m.x111 -
    m.x131)**2 + (m.x190 - m.x210)**2)**(-3) * (((m.x32 - m.x52)**2 + (m.x111
    - m.x131)**2 + (m.x190 - m.x210)**2)**(-3) - 2) + ((m.x32 - m.x53)**2 + (
    m.x111 - m.x132)**2 + (m.x190 - m.x211)**2)**(-3) * (((m.x32 - m.x53)**2 +
    (m.x111 - m.x132)**2 + (m.x190 - m.x211)**2)**(-3) - 2) + ((m.x32 - m.x54)
    **2 + (m.x111 - m.x133)**2 + (m.x190 - m.x212)**2)**(-3) * (((m.x32 - m.x54)
    **2 + (m.x111 - m.x133)**2 + (m.x190 - m.x212)**2)**(-3) - 2) + ((m.x32 -
    m.x55)**2 + (m.x111 - m.x134)**2 + (m.x190 - m.x213)**2)**(-3) * (((m.x32
    - m.x55)**2 + (m.x111 - m.x134)**2 + (m.x190 - m.x213)**2)**(-3) - 2) + ((
    m.x32 - m.x56)**2 + (m.x111 - m.x135)**2 + (m.x190 - m.x214)**2)**(-3) * ((
    (m.x32 - m.x56)**2 + (m.x111 - m.x135)**2 + (m.x190 - m.x214)**2)**(-3) - 2)
    + ((m.x32 - m.x57)**2 + (m.x111 - m.x136)**2 + (m.x190 - m.x215)**2)**(-3)
    * (((m.x32 - m.x57)**2 + (m.x111 - m.x136)**2 + (m.x190 - m.x215)**2)**(-3)
    - 2) + ((m.x32 - m.x58)**2 + (m.x111 - m.x137)**2 + (m.x190 - m.x216)**2)
    **(-3) * (((m.x32 - m.x58)**2 + (m.x111 - m.x137)**2 + (m.x190 - m.x216)**2)
    **(-3) - 2) + ((m.x32 - m.x59)**2 + (m.x111 - m.x138)**2 + (m.x190 - m.x217)
    **2)**(-3) * (((m.x32 - m.x59)**2 + (m.x111 - m.x138)**2 + (m.x190 - m.x217)
    **2)**(-3) - 2) + ((m.x32 - m.x60)**2 + (m.x111 - m.x139)**2 + (m.x190 -
    m.x218)**2)**(-3) * (((m.x32 - m.x60)**2 + (m.x111 - m.x139)**2 + (m.x190
    - m.x218)**2)**(-3) - 2) + ((m.x32 - m.x61)**2 + (m.x111 - m.x140)**2 + (
    m.x190 - m.x219)**2)**(-3) * (((m.x32 - m.x61)**2 + (m.x111 - m.x140)**2 +
    (m.x190 - m.x219)**2)**(-3) - 2) + ((m.x32 - m.x62)**2 + (m.x111 - m.x141)
    **2 + (m.x190 - m.x220)**2)**(-3) * (((m.x32 - m.x62)**2 + (m.x111 - m.x141)
    **2 + (m.x190 - m.x220)**2)**(-3) - 2) + ((m.x32 - m.x63)**2 + (m.x111 -
    m.x142)**2 + (m.x190 - m.x221)**2)**(-3) * (((m.x32 - m.x63)**2 + (m.x111
    - m.x142)**2 + (m.x190 - m.x221)**2)**(-3) - 2) + ((m.x32 - m.x64)**2 + (
    m.x111 - m.x143)**2 + (m.x190 - m.x222)**2)**(-3) * (((m.x32 - m.x64)**2 +
    (m.x111 - m.x143)**2 + (m.x190 - m.x222)**2)**(-3) - 2) + ((m.x32 - m.x65)
    **2 + (m.x111 - m.x144)**2 + (m.x190 - m.x223)**2)**(-3) * (((m.x32 - m.x65)
    **2 + (m.x111 - m.x144)**2 + (m.x190 - m.x223)**2)**(-3) - 2) + ((m.x32 -
    m.x66)**2 + (m.x111 - m.x145)**2 + (m.x190 - m.x224)**2)**(-3) * (((m.x32
    - m.x66)**2 + (m.x111 - m.x145)**2 + (m.x190 - m.x224)**2)**(-3) - 2) + ((
    m.x32 - m.x67)**2 + (m.x111 - m.x146)**2 + (m.x190 - m.x225)**2)**(-3) * ((
    (m.x32 - m.x67)**2 + (m.x111 - m.x146)**2 + (m.x190 - m.x225)**2)**(-3) - 2)
    + ((m.x32 - m.x68)**2 + (m.x111 - m.x147)**2 + (m.x190 - m.x226)**2)**(-3)
    * (((m.x32 - m.x68)**2 + (m.x111 - m.x147)**2 + (m.x190 - m.x226)**2)**(-3)
    - 2) + ((m.x32 - m.x69)**2 + (m.x111 - m.x148)**2 + (m.x190 - m.x227)**2)
    **(-3) * (((m.x32 - m.x69)**2 + (m.x111 - m.x148)**2 + (m.x190 - m.x227)**2)
    **(-3) - 2) + ((m.x32 - m.x70)**2 + (m.x111 - m.x149)**2 + (m.x190 - m.x228)
    **2)**(-3) * (((m.x32 - m.x70)**2 + (m.x111 - m.x149)**2 + (m.x190 - m.x228)
    **2)**(-3) - 2) + ((m.x32 - m.x71)**2 + (m.x111 - m.x150)**2 + (m.x190 -
    m.x229)**2)**(-3) * (((m.x32 - m.x71)**2 + (m.x111 - m.x150)**2 + (m.x190
    - m.x229)**2)**(-3) - 2) + ((m.x32 - m.x72)**2 + (m.x111 - m.x151)**2 + (
    m.x190 - m.x230)**2)**(-3) * (((m.x32 - m.x72)**2 + (m.x111 - m.x151)**2 +
    (m.x190 - m.x230)**2)**(-3) - 2) + ((m.x32 - m.x73)**2 + (m.x111 - m.x152)
    **2 + (m.x190 - m.x231)**2)**(-3) * (((m.x32 - m.x73)**2 + (m.x111 - m.x152)
    **2 + (m.x190 - m.x231)**2)**(-3) - 2) + ((m.x32 - m.x74)**2 + (m.x111 -
    m.x153)**2 + (m.x190 - m.x232)**2)**(-3) * (((m.x32 - m.x74)**2 + (m.x111
    - m.x153)**2 + (m.x190 - m.x232)**2)**(-3) - 2) + ((m.x32 - m.x75)**2 + (
    m.x111 - m.x154)**2 + (m.x190 - m.x233)**2)**(-3) * (((m.x32 - m.x75)**2 +
    (m.x111 - m.x154)**2 + (m.x190 - m.x233)**2)**(-3) - 2) + ((m.x32 - m.x76)
    **2 + (m.x111 - m.x155)**2 + (m.x190 - m.x234)**2)**(-3) * (((m.x32 - m.x76)
    **2 + (m.x111 - m.x155)**2 + (m.x190 - m.x234)**2)**(-3) - 2) + ((m.x32 -
    m.x77)**2 + (m.x111 - m.x156)**2 + (m.x190 - m.x235)**2)**(-3) * (((m.x32
    - m.x77)**2 + (m.x111 - m.x156)**2 + (m.x190 - m.x235)**2)**(-3) - 2) + ((
    m.x32 - m.x78)**2 + (m.x111 - m.x157)**2 + (m.x190 - m.x236)**2)**(-3) * ((
    (m.x32 - m.x78)**2 + (m.x111 - m.x157)**2 + (m.x190 - m.x236)**2)**(-3) - 2)
    + ((m.x32 - m.x79)**2 + (m.x111 - m.x158)**2 + (m.x190 - m.x237)**2)**(-3)
    * (((m.x32 - m.x79)**2 + (m.x111 - m.x158)**2 + (m.x190 - m.x237)**2)**(-3)
    - 2) + ((m.x33 - m.x34)**2 + (m.x112 - m.x113)**2 + (m.x191 - m.x192)**2)
    **(-3) * (((m.x33 - m.x34)**2 + (m.x112 - m.x113)**2 + (m.x191 - m.x192)**2)
    **(-3) - 2) + ((m.x33 - m.x35)**2 + (m.x112 - m.x114)**2 + (m.x191 - m.x193)
    **2)**(-3) * (((m.x33 - m.x35)**2 + (m.x112 - m.x114)**2 + (m.x191 - m.x193)
    **2)**(-3) - 2) + ((m.x33 - m.x36)**2 + (m.x112 - m.x115)**2 + (m.x191 -
    m.x194)**2)**(-3) * (((m.x33 - m.x36)**2 + (m.x112 - m.x115)**2 + (m.x191
    - m.x194)**2)**(-3) - 2) + ((m.x33 - m.x37)**2 + (m.x112 - m.x116)**2 + (
    m.x191 - m.x195)**2)**(-3) * (((m.x33 - m.x37)**2 + (m.x112 - m.x116)**2 +
    (m.x191 - m.x195)**2)**(-3) - 2) + ((m.x33 - m.x38)**2 + (m.x112 - m.x117)
    **2 + (m.x191 - m.x196)**2)**(-3) * (((m.x33 - m.x38)**2 + (m.x112 - m.x117)
    **2 + (m.x191 - m.x196)**2)**(-3) - 2) + ((m.x33 - m.x39)**2 + (m.x112 -
    m.x118)**2 + (m.x191 - m.x197)**2)**(-3) * (((m.x33 - m.x39)**2 + (m.x112
    - m.x118)**2 + (m.x191 - m.x197)**2)**(-3) - 2) + ((m.x33 - m.x40)**2 + (
    m.x112 - m.x119)**2 + (m.x191 - m.x198)**2)**(-3) * (((m.x33 - m.x40)**2 +
    (m.x112 - m.x119)**2 + (m.x191 - m.x198)**2)**(-3) - 2) + ((m.x33 - m.x41)
    **2 + (m.x112 - m.x120)**2 + (m.x191 - m.x199)**2)**(-3) * (((m.x33 - m.x41)
    **2 + (m.x112 - m.x120)**2 + (m.x191 - m.x199)**2)**(-3) - 2) + ((m.x33 -
    m.x42)**2 + (m.x112 - m.x121)**2 + (m.x191 - m.x200)**2)**(-3) * (((m.x33
    - m.x42)**2 + (m.x112 - m.x121)**2 + (m.x191 - m.x200)**2)**(-3) - 2) + ((
    m.x33 - m.x43)**2 + (m.x112 - m.x122)**2 + (m.x191 - m.x201)**2)**(-3) * ((
    (m.x33 - m.x43)**2 + (m.x112 - m.x122)**2 + (m.x191 - m.x201)**2)**(-3) - 2)
    + ((m.x33 - m.x44)**2 + (m.x112 - m.x123)**2 + (m.x191 - m.x202)**2)**(-3)
    * (((m.x33 - m.x44)**2 + (m.x112 - m.x123)**2 + (m.x191 - m.x202)**2)**(-3)
    - 2) + ((m.x33 - m.x45)**2 + (m.x112 - m.x124)**2 + (m.x191 - m.x203)**2)
    **(-3) * (((m.x33 - m.x45)**2 + (m.x112 - m.x124)**2 + (m.x191 - m.x203)**2)
    **(-3) - 2) + ((m.x33 - m.x46)**2 + (m.x112 - m.x125)**2 + (m.x191 - m.x204)
    **2)**(-3) * (((m.x33 - m.x46)**2 + (m.x112 - m.x125)**2 + (m.x191 - m.x204)
    **2)**(-3) - 2) + ((m.x33 - m.x47)**2 + (m.x112 - m.x126)**2 + (m.x191 -
    m.x205)**2)**(-3) * (((m.x33 - m.x47)**2 + (m.x112 - m.x126)**2 + (m.x191
    - m.x205)**2)**(-3) - 2) + ((m.x33 - m.x48)**2 + (m.x112 - m.x127)**2 + (
    m.x191 - m.x206)**2)**(-3) * (((m.x33 - m.x48)**2 + (m.x112 - m.x127)**2 +
    (m.x191 - m.x206)**2)**(-3) - 2) + ((m.x33 - m.x49)**2 + (m.x112 - m.x128)
    **2 + (m.x191 - m.x207)**2)**(-3) * (((m.x33 - m.x49)**2 + (m.x112 - m.x128)
    **2 + (m.x191 - m.x207)**2)**(-3) - 2) + ((m.x33 - m.x50)**2 + (m.x112 -
    m.x129)**2 + (m.x191 - m.x208)**2)**(-3) * (((m.x33 - m.x50)**2 + (m.x112
    - m.x129)**2 + (m.x191 - m.x208)**2)**(-3) - 2) + ((m.x33 - m.x51)**2 + (
    m.x112 - m.x130)**2 + (m.x191 - m.x209)**2)**(-3) * (((m.x33 - m.x51)**2 +
    (m.x112 - m.x130)**2 + (m.x191 - m.x209)**2)**(-3) - 2) + ((m.x33 - m.x52)
    **2 + (m.x112 - m.x131)**2 + (m.x191 - m.x210)**2)**(-3) * (((m.x33 - m.x52)
    **2 + (m.x112 - m.x131)**2 + (m.x191 - m.x210)**2)**(-3) - 2) + ((m.x33 -
    m.x53)**2 + (m.x112 - m.x132)**2 + (m.x191 - m.x211)**2)**(-3) * (((m.x33
    - m.x53)**2 + (m.x112 - m.x132)**2 + (m.x191 - m.x211)**2)**(-3) - 2) + ((
    m.x33 - m.x54)**2 + (m.x112 - m.x133)**2 + (m.x191 - m.x212)**2)**(-3) * ((
    (m.x33 - m.x54)**2 + (m.x112 - m.x133)**2 + (m.x191 - m.x212)**2)**(-3) - 2)
    + ((m.x33 - m.x55)**2 + (m.x112 - m.x134)**2 + (m.x191 - m.x213)**2)**(-3)
    * (((m.x33 - m.x55)**2 + (m.x112 - m.x134)**2 + (m.x191 - m.x213)**2)**(-3)
    - 2) + ((m.x33 - m.x56)**2 + (m.x112 - m.x135)**2 + (m.x191 - m.x214)**2)
    **(-3) * (((m.x33 - m.x56)**2 + (m.x112 - m.x135)**2 + (m.x191 - m.x214)**2)
    **(-3) - 2) + ((m.x33 - m.x57)**2 + (m.x112 - m.x136)**2 + (m.x191 - m.x215)
    **2)**(-3) * (((m.x33 - m.x57)**2 + (m.x112 - m.x136)**2 + (m.x191 - m.x215)
    **2)**(-3) - 2) + ((m.x33 - m.x58)**2 + (m.x112 - m.x137)**2 + (m.x191 -
    m.x216)**2)**(-3) * (((m.x33 - m.x58)**2 + (m.x112 - m.x137)**2 + (m.x191
    - m.x216)**2)**(-3) - 2) + ((m.x33 - m.x59)**2 + (m.x112 - m.x138)**2 + (
    m.x191 - m.x217)**2)**(-3) * (((m.x33 - m.x59)**2 + (m.x112 - m.x138)**2 +
    (m.x191 - m.x217)**2)**(-3) - 2) + ((m.x33 - m.x60)**2 + (m.x112 - m.x139)
    **2 + (m.x191 - m.x218)**2)**(-3) * (((m.x33 - m.x60)**2 + (m.x112 - m.x139)
    **2 + (m.x191 - m.x218)**2)**(-3) - 2) + ((m.x33 - m.x61)**2 + (m.x112 -
    m.x140)**2 + (m.x191 - m.x219)**2)**(-3) * (((m.x33 - m.x61)**2 + (m.x112
    - m.x140)**2 + (m.x191 - m.x219)**2)**(-3) - 2) + ((m.x33 - m.x62)**2 + (
    m.x112 - m.x141)**2 + (m.x191 - m.x220)**2)**(-3) * (((m.x33 - m.x62)**2 +
    (m.x112 - m.x141)**2 + (m.x191 - m.x220)**2)**(-3) - 2) + ((m.x33 - m.x63)
    **2 + (m.x112 - m.x142)**2 + (m.x191 - m.x221)**2)**(-3) * (((m.x33 - m.x63)
    **2 + (m.x112 - m.x142)**2 + (m.x191 - m.x221)**2)**(-3) - 2) + ((m.x33 -
    m.x64)**2 + (m.x112 - m.x143)**2 + (m.x191 - m.x222)**2)**(-3) * (((m.x33
    - m.x64)**2 + (m.x112 - m.x143)**2 + (m.x191 - m.x222)**2)**(-3) - 2) + ((
    m.x33 - m.x65)**2 + (m.x112 - m.x144)**2 + (m.x191 - m.x223)**2)**(-3) * ((
    (m.x33 - m.x65)**2 + (m.x112 - m.x144)**2 + (m.x191 - m.x223)**2)**(-3) - 2)
    + ((m.x33 - m.x66)**2 + (m.x112 - m.x145)**2 + (m.x191 - m.x224)**2)**(-3)
    * (((m.x33 - m.x66)**2 + (m.x112 - m.x145)**2 + (m.x191 - m.x224)**2)**(-3)
    - 2) + ((m.x33 - m.x67)**2 + (m.x112 - m.x146)**2 + (m.x191 - m.x225)**2)
    **(-3) * (((m.x33 - m.x67)**2 + (m.x112 - m.x146)**2 + (m.x191 - m.x225)**2)
    **(-3) - 2) + ((m.x33 - m.x68)**2 + (m.x112 - m.x147)**2 + (m.x191 - m.x226)
    **2)**(-3) * (((m.x33 - m.x68)**2 + (m.x112 - m.x147)**2 + (m.x191 - m.x226)
    **2)**(-3) - 2) + ((m.x33 - m.x69)**2 + (m.x112 - m.x148)**2 + (m.x191 -
    m.x227)**2)**(-3) * (((m.x33 - m.x69)**2 + (m.x112 - m.x148)**2 + (m.x191
    - m.x227)**2)**(-3) - 2) + ((m.x33 - m.x70)**2 + (m.x112 - m.x149)**2 + (
    m.x191 - m.x228)**2)**(-3) * (((m.x33 - m.x70)**2 + (m.x112 - m.x149)**2 +
    (m.x191 - m.x228)**2)**(-3) - 2) + ((m.x33 - m.x71)**2 + (m.x112 - m.x150)
    **2 + (m.x191 - m.x229)**2)**(-3) * (((m.x33 - m.x71)**2 + (m.x112 - m.x150)
    **2 + (m.x191 - m.x229)**2)**(-3) - 2) + ((m.x33 - m.x72)**2 + (m.x112 -
    m.x151)**2 + (m.x191 - m.x230)**2)**(-3) * (((m.x33 - m.x72)**2 + (m.x112
    - m.x151)**2 + (m.x191 - m.x230)**2)**(-3) - 2) + ((m.x33 - m.x73)**2 + (
    m.x112 - m.x152)**2 + (m.x191 - m.x231)**2)**(-3) * (((m.x33 - m.x73)**2 +
    (m.x112 - m.x152)**2 + (m.x191 - m.x231)**2)**(-3) - 2) + ((m.x33 - m.x74)
    **2 + (m.x112 - m.x153)**2 + (m.x191 - m.x232)**2)**(-3) * (((m.x33 - m.x74)
    **2 + (m.x112 - m.x153)**2 + (m.x191 - m.x232)**2)**(-3) - 2) + ((m.x33 -
    m.x75)**2 + (m.x112 - m.x154)**2 + (m.x191 - m.x233)**2)**(-3) * (((m.x33
    - m.x75)**2 + (m.x112 - m.x154)**2 + (m.x191 - m.x233)**2)**(-3) - 2) + ((
    m.x33 - m.x76)**2 + (m.x112 - m.x155)**2 + (m.x191 - m.x234)**2)**(-3) * ((
    (m.x33 - m.x76)**2 + (m.x112 - m.x155)**2 + (m.x191 - m.x234)**2)**(-3) - 2)
    + ((m.x33 - m.x77)**2 + (m.x112 - m.x156)**2 + (m.x191 - m.x235)**2)**(-3)
    * (((m.x33 - m.x77)**2 + (m.x112 - m.x156)**2 + (m.x191 - m.x235)**2)**(-3)
    - 2) + ((m.x33 - m.x78)**2 + (m.x112 - m.x157)**2 + (m.x191 - m.x236)**2)
    **(-3) * (((m.x33 - m.x78)**2 + (m.x112 - m.x157)**2 + (m.x191 - m.x236)**2)
    **(-3) - 2) + ((m.x33 - m.x79)**2 + (m.x112 - m.x158)**2 + (m.x191 - m.x237)
    **2)**(-3) * (((m.x33 - m.x79)**2 + (m.x112 - m.x158)**2 + (m.x191 - m.x237)
    **2)**(-3) - 2) + ((m.x34 - m.x35)**2 + (m.x113 - m.x114)**2 + (m.x192 -
    m.x193)**2)**(-3) * (((m.x34 - m.x35)**2 + (m.x113 - m.x114)**2 + (m.x192
    - m.x193)**2)**(-3) - 2) + ((m.x34 - m.x36)**2 + (m.x113 - m.x115)**2 + (
    m.x192 - m.x194)**2)**(-3) * (((m.x34 - m.x36)**2 + (m.x113 - m.x115)**2 +
    (m.x192 - m.x194)**2)**(-3) - 2) + ((m.x34 - m.x37)**2 + (m.x113 - m.x116)
    **2 + (m.x192 - m.x195)**2)**(-3) * (((m.x34 - m.x37)**2 + (m.x113 - m.x116)
    **2 + (m.x192 - m.x195)**2)**(-3) - 2) + ((m.x34 - m.x38)**2 + (m.x113 -
    m.x117)**2 + (m.x192 - m.x196)**2)**(-3) * (((m.x34 - m.x38)**2 + (m.x113
    - m.x117)**2 + (m.x192 - m.x196)**2)**(-3) - 2) + ((m.x34 - m.x39)**2 + (
    m.x113 - m.x118)**2 + (m.x192 - m.x197)**2)**(-3) * (((m.x34 - m.x39)**2 +
    (m.x113 - m.x118)**2 + (m.x192 - m.x197)**2)**(-3) - 2) + ((m.x34 - m.x40)
    **2 + (m.x113 - m.x119)**2 + (m.x192 - m.x198)**2)**(-3) * (((m.x34 - m.x40)
    **2 + (m.x113 - m.x119)**2 + (m.x192 - m.x198)**2)**(-3) - 2) + ((m.x34 -
    m.x41)**2 + (m.x113 - m.x120)**2 + (m.x192 - m.x199)**2)**(-3) * (((m.x34
    - m.x41)**2 + (m.x113 - m.x120)**2 + (m.x192 - m.x199)**2)**(-3) - 2) + ((
    m.x34 - m.x42)**2 + (m.x113 - m.x121)**2 + (m.x192 - m.x200)**2)**(-3) * ((
    (m.x34 - m.x42)**2 + (m.x113 - m.x121)**2 + (m.x192 - m.x200)**2)**(-3) - 2)
    + ((m.x34 - m.x43)**2 + (m.x113 - m.x122)**2 + (m.x192 - m.x201)**2)**(-3)
    * (((m.x34 - m.x43)**2 + (m.x113 - m.x122)**2 + (m.x192 - m.x201)**2)**(-3)
    - 2) + ((m.x34 - m.x44)**2 + (m.x113 - m.x123)**2 + (m.x192 - m.x202)**2)
    **(-3) * (((m.x34 - m.x44)**2 + (m.x113 - m.x123)**2 + (m.x192 - m.x202)**2)
    **(-3) - 2) + ((m.x34 - m.x45)**2 + (m.x113 - m.x124)**2 + (m.x192 - m.x203)
    **2)**(-3) * (((m.x34 - m.x45)**2 + (m.x113 - m.x124)**2 + (m.x192 - m.x203)
    **2)**(-3) - 2) + ((m.x34 - m.x46)**2 + (m.x113 - m.x125)**2 + (m.x192 -
    m.x204)**2)**(-3) * (((m.x34 - m.x46)**2 + (m.x113 - m.x125)**2 + (m.x192
    - m.x204)**2)**(-3) - 2) + ((m.x34 - m.x47)**2 + (m.x113 - m.x126)**2 + (
    m.x192 - m.x205)**2)**(-3) * (((m.x34 - m.x47)**2 + (m.x113 - m.x126)**2 +
    (m.x192 - m.x205)**2)**(-3) - 2) + ((m.x34 - m.x48)**2 + (m.x113 - m.x127)
    **2 + (m.x192 - m.x206)**2)**(-3) * (((m.x34 - m.x48)**2 + (m.x113 - m.x127)
    **2 + (m.x192 - m.x206)**2)**(-3) - 2) + ((m.x34 - m.x49)**2 + (m.x113 -
    m.x128)**2 + (m.x192 - m.x207)**2)**(-3) * (((m.x34 - m.x49)**2 + (m.x113
    - m.x128)**2 + (m.x192 - m.x207)**2)**(-3) - 2) + ((m.x34 - m.x50)**2 + (
    m.x113 - m.x129)**2 + (m.x192 - m.x208)**2)**(-3) * (((m.x34 - m.x50)**2 +
    (m.x113 - m.x129)**2 + (m.x192 - m.x208)**2)**(-3) - 2) + ((m.x34 - m.x51)
    **2 + (m.x113 - m.x130)**2 + (m.x192 - m.x209)**2)**(-3) * (((m.x34 - m.x51)
    **2 + (m.x113 - m.x130)**2 + (m.x192 - m.x209)**2)**(-3) - 2) + ((m.x34 -
    m.x52)**2 + (m.x113 - m.x131)**2 + (m.x192 - m.x210)**2)**(-3) * (((m.x34
    - m.x52)**2 + (m.x113 - m.x131)**2 + (m.x192 - m.x210)**2)**(-3) - 2) + ((
    m.x34 - m.x53)**2 + (m.x113 - m.x132)**2 + (m.x192 - m.x211)**2)**(-3) * ((
    (m.x34 - m.x53)**2 + (m.x113 - m.x132)**2 + (m.x192 - m.x211)**2)**(-3) - 2)
    + ((m.x34 - m.x54)**2 + (m.x113 - m.x133)**2 + (m.x192 - m.x212)**2)**(-3)
    * (((m.x34 - m.x54)**2 + (m.x113 - m.x133)**2 + (m.x192 - m.x212)**2)**(-3)
    - 2) + ((m.x34 - m.x55)**2 + (m.x113 - m.x134)**2 + (m.x192 - m.x213)**2)
    **(-3) * (((m.x34 - m.x55)**2 + (m.x113 - m.x134)**2 + (m.x192 - m.x213)**2)
    **(-3) - 2) + ((m.x34 - m.x56)**2 + (m.x113 - m.x135)**2 + (m.x192 - m.x214)
    **2)**(-3) * (((m.x34 - m.x56)**2 + (m.x113 - m.x135)**2 + (m.x192 - m.x214)
    **2)**(-3) - 2) + ((m.x34 - m.x57)**2 + (m.x113 - m.x136)**2 + (m.x192 -
    m.x215)**2)**(-3) * (((m.x34 - m.x57)**2 + (m.x113 - m.x136)**2 + (m.x192
    - m.x215)**2)**(-3) - 2) + ((m.x34 - m.x58)**2 + (m.x113 - m.x137)**2 + (
    m.x192 - m.x216)**2)**(-3) * (((m.x34 - m.x58)**2 + (m.x113 - m.x137)**2 +
    (m.x192 - m.x216)**2)**(-3) - 2) + ((m.x34 - m.x59)**2 + (m.x113 - m.x138)
    **2 + (m.x192 - m.x217)**2)**(-3) * (((m.x34 - m.x59)**2 + (m.x113 - m.x138)
    **2 + (m.x192 - m.x217)**2)**(-3) - 2) + ((m.x34 - m.x60)**2 + (m.x113 -
    m.x139)**2 + (m.x192 - m.x218)**2)**(-3) * (((m.x34 - m.x60)**2 + (m.x113
    - m.x139)**2 + (m.x192 - m.x218)**2)**(-3) - 2) + ((m.x34 - m.x61)**2 + (
    m.x113 - m.x140)**2 + (m.x192 - m.x219)**2)**(-3) * (((m.x34 - m.x61)**2 +
    (m.x113 - m.x140)**2 + (m.x192 - m.x219)**2)**(-3) - 2) + ((m.x34 - m.x62)
    **2 + (m.x113 - m.x141)**2 + (m.x192 - m.x220)**2)**(-3) * (((m.x34 - m.x62)
    **2 + (m.x113 - m.x141)**2 + (m.x192 - m.x220)**2)**(-3) - 2) + ((m.x34 -
    m.x63)**2 + (m.x113 - m.x142)**2 + (m.x192 - m.x221)**2)**(-3) * (((m.x34
    - m.x63)**2 + (m.x113 - m.x142)**2 + (m.x192 - m.x221)**2)**(-3) - 2) + ((
    m.x34 - m.x64)**2 + (m.x113 - m.x143)**2 + (m.x192 - m.x222)**2)**(-3) * ((
    (m.x34 - m.x64)**2 + (m.x113 - m.x143)**2 + (m.x192 - m.x222)**2)**(-3) - 2)
    + ((m.x34 - m.x65)**2 + (m.x113 - m.x144)**2 + (m.x192 - m.x223)**2)**(-3)
    * (((m.x34 - m.x65)**2 + (m.x113 - m.x144)**2 + (m.x192 - m.x223)**2)**(-3)
    - 2) + ((m.x34 - m.x66)**2 + (m.x113 - m.x145)**2 + (m.x192 - m.x224)**2)
    **(-3) * (((m.x34 - m.x66)**2 + (m.x113 - m.x145)**2 + (m.x192 - m.x224)**2)
    **(-3) - 2) + ((m.x34 - m.x67)**2 + (m.x113 - m.x146)**2 + (m.x192 - m.x225)
    **2)**(-3) * (((m.x34 - m.x67)**2 + (m.x113 - m.x146)**2 + (m.x192 - m.x225)
    **2)**(-3) - 2) + ((m.x34 - m.x68)**2 + (m.x113 - m.x147)**2 + (m.x192 -
    m.x226)**2)**(-3) * (((m.x34 - m.x68)**2 + (m.x113 - m.x147)**2 + (m.x192
    - m.x226)**2)**(-3) - 2) + ((m.x34 - m.x69)**2 + (m.x113 - m.x148)**2 + (
    m.x192 - m.x227)**2)**(-3) * (((m.x34 - m.x69)**2 + (m.x113 - m.x148)**2 +
    (m.x192 - m.x227)**2)**(-3) - 2) + ((m.x34 - m.x70)**2 + (m.x113 - m.x149)
    **2 + (m.x192 - m.x228)**2)**(-3) * (((m.x34 - m.x70)**2 + (m.x113 - m.x149)
    **2 + (m.x192 - m.x228)**2)**(-3) - 2) + ((m.x34 - m.x71)**2 + (m.x113 -
    m.x150)**2 + (m.x192 - m.x229)**2)**(-3) * (((m.x34 - m.x71)**2 + (m.x113
    - m.x150)**2 + (m.x192 - m.x229)**2)**(-3) - 2) + ((m.x34 - m.x72)**2 + (
    m.x113 - m.x151)**2 + (m.x192 - m.x230)**2)**(-3) * (((m.x34 - m.x72)**2 +
    (m.x113 - m.x151)**2 + (m.x192 - m.x230)**2)**(-3) - 2) + ((m.x34 - m.x73)
    **2 + (m.x113 - m.x152)**2 + (m.x192 - m.x231)**2)**(-3) * (((m.x34 - m.x73)
    **2 + (m.x113 - m.x152)**2 + (m.x192 - m.x231)**2)**(-3) - 2) + ((m.x34 -
    m.x74)**2 + (m.x113 - m.x153)**2 + (m.x192 - m.x232)**2)**(-3) * (((m.x34
    - m.x74)**2 + (m.x113 - m.x153)**2 + (m.x192 - m.x232)**2)**(-3) - 2) + ((
    m.x34 - m.x75)**2 + (m.x113 - m.x154)**2 + (m.x192 - m.x233)**2)**(-3) * ((
    (m.x34 - m.x75)**2 + (m.x113 - m.x154)**2 + (m.x192 - m.x233)**2)**(-3) - 2)
    + ((m.x34 - m.x76)**2 + (m.x113 - m.x155)**2 + (m.x192 - m.x234)**2)**(-3)
    * (((m.x34 - m.x76)**2 + (m.x113 - m.x155)**2 + (m.x192 - m.x234)**2)**(-3)
    - 2) + ((m.x34 - m.x77)**2 + (m.x113 - m.x156)**2 + (m.x192 - m.x235)**2)
    **(-3) * (((m.x34 - m.x77)**2 + (m.x113 - m.x156)**2 + (m.x192 - m.x235)**2)
    **(-3) - 2) + ((m.x34 - m.x78)**2 + (m.x113 - m.x157)**2 + (m.x192 - m.x236)
    **2)**(-3) * (((m.x34 - m.x78)**2 + (m.x113 - m.x157)**2 + (m.x192 - m.x236)
    **2)**(-3) - 2) + ((m.x34 - m.x79)**2 + (m.x113 - m.x158)**2 + (m.x192 -
    m.x237)**2)**(-3) * (((m.x34 - m.x79)**2 + (m.x113 - m.x158)**2 + (m.x192
    - m.x237)**2)**(-3) - 2) + ((m.x35 - m.x36)**2 + (m.x114 - m.x115)**2 + (
    m.x193 - m.x194)**2)**(-3) * (((m.x35 - m.x36)**2 + (m.x114 - m.x115)**2 +
    (m.x193 - m.x194)**2)**(-3) - 2) + ((m.x35 - m.x37)**2 + (m.x114 - m.x116)
    **2 + (m.x193 - m.x195)**2)**(-3) * (((m.x35 - m.x37)**2 + (m.x114 - m.x116)
    **2 + (m.x193 - m.x195)**2)**(-3) - 2) + ((m.x35 - m.x38)**2 + (m.x114 -
    m.x117)**2 + (m.x193 - m.x196)**2)**(-3) * (((m.x35 - m.x38)**2 + (m.x114
    - m.x117)**2 + (m.x193 - m.x196)**2)**(-3) - 2) + ((m.x35 - m.x39)**2 + (
    m.x114 - m.x118)**2 + (m.x193 - m.x197)**2)**(-3) * (((m.x35 - m.x39)**2 +
    (m.x114 - m.x118)**2 + (m.x193 - m.x197)**2)**(-3) - 2) + ((m.x35 - m.x40)
    **2 + (m.x114 - m.x119)**2 + (m.x193 - m.x198)**2)**(-3) * (((m.x35 - m.x40)
    **2 + (m.x114 - m.x119)**2 + (m.x193 - m.x198)**2)**(-3) - 2) + ((m.x35 -
    m.x41)**2 + (m.x114 - m.x120)**2 + (m.x193 - m.x199)**2)**(-3) * (((m.x35
    - m.x41)**2 + (m.x114 - m.x120)**2 + (m.x193 - m.x199)**2)**(-3) - 2) + ((
    m.x35 - m.x42)**2 + (m.x114 - m.x121)**2 + (m.x193 - m.x200)**2)**(-3) * ((
    (m.x35 - m.x42)**2 + (m.x114 - m.x121)**2 + (m.x193 - m.x200)**2)**(-3) - 2)
    + ((m.x35 - m.x43)**2 + (m.x114 - m.x122)**2 + (m.x193 - m.x201)**2)**(-3)
    * (((m.x35 - m.x43)**2 + (m.x114 - m.x122)**2 + (m.x193 - m.x201)**2)**(-3)
    - 2) + ((m.x35 - m.x44)**2 + (m.x114 - m.x123)**2 + (m.x193 - m.x202)**2)
    **(-3) * (((m.x35 - m.x44)**2 + (m.x114 - m.x123)**2 + (m.x193 - m.x202)**2)
    **(-3) - 2) + ((m.x35 - m.x45)**2 + (m.x114 - m.x124)**2 + (m.x193 - m.x203)
    **2)**(-3) * (((m.x35 - m.x45)**2 + (m.x114 - m.x124)**2 + (m.x193 - m.x203)
    **2)**(-3) - 2) + ((m.x35 - m.x46)**2 + (m.x114 - m.x125)**2 + (m.x193 -
    m.x204)**2)**(-3) * (((m.x35 - m.x46)**2 + (m.x114 - m.x125)**2 + (m.x193
    - m.x204)**2)**(-3) - 2) + ((m.x35 - m.x47)**2 + (m.x114 - m.x126)**2 + (
    m.x193 - m.x205)**2)**(-3) * (((m.x35 - m.x47)**2 + (m.x114 - m.x126)**2 +
    (m.x193 - m.x205)**2)**(-3) - 2) + ((m.x35 - m.x48)**2 + (m.x114 - m.x127)
    **2 + (m.x193 - m.x206)**2)**(-3) * (((m.x35 - m.x48)**2 + (m.x114 - m.x127)
    **2 + (m.x193 - m.x206)**2)**(-3) - 2) + ((m.x35 - m.x49)**2 + (m.x114 -
    m.x128)**2 + (m.x193 - m.x207)**2)**(-3) * (((m.x35 - m.x49)**2 + (m.x114
    - m.x128)**2 + (m.x193 - m.x207)**2)**(-3) - 2) + ((m.x35 - m.x50)**2 + (
    m.x114 - m.x129)**2 + (m.x193 - m.x208)**2)**(-3) * (((m.x35 - m.x50)**2 +
    (m.x114 - m.x129)**2 + (m.x193 - m.x208)**2)**(-3) - 2) + ((m.x35 - m.x51)
    **2 + (m.x114 - m.x130)**2 + (m.x193 - m.x209)**2)**(-3) * (((m.x35 - m.x51)
    **2 + (m.x114 - m.x130)**2 + (m.x193 - m.x209)**2)**(-3) - 2) + ((m.x35 -
    m.x52)**2 + (m.x114 - m.x131)**2 + (m.x193 - m.x210)**2)**(-3) * (((m.x35
    - m.x52)**2 + (m.x114 - m.x131)**2 + (m.x193 - m.x210)**2)**(-3) - 2) + ((
    m.x35 - m.x53)**2 + (m.x114 - m.x132)**2 + (m.x193 - m.x211)**2)**(-3) * ((
    (m.x35 - m.x53)**2 + (m.x114 - m.x132)**2 + (m.x193 - m.x211)**2)**(-3) - 2)
    + ((m.x35 - m.x54)**2 + (m.x114 - m.x133)**2 + (m.x193 - m.x212)**2)**(-3)
    * (((m.x35 - m.x54)**2 + (m.x114 - m.x133)**2 + (m.x193 - m.x212)**2)**(-3)
    - 2) + ((m.x35 - m.x55)**2 + (m.x114 - m.x134)**2 + (m.x193 - m.x213)**2)
    **(-3) * (((m.x35 - m.x55)**2 + (m.x114 - m.x134)**2 + (m.x193 - m.x213)**2)
    **(-3) - 2) + ((m.x35 - m.x56)**2 + (m.x114 - m.x135)**2 + (m.x193 - m.x214)
    **2)**(-3) * (((m.x35 - m.x56)**2 + (m.x114 - m.x135)**2 + (m.x193 - m.x214)
    **2)**(-3) - 2) + ((m.x35 - m.x57)**2 + (m.x114 - m.x136)**2 + (m.x193 -
    m.x215)**2)**(-3) * (((m.x35 - m.x57)**2 + (m.x114 - m.x136)**2 + (m.x193
    - m.x215)**2)**(-3) - 2) + ((m.x35 - m.x58)**2 + (m.x114 - m.x137)**2 + (
    m.x193 - m.x216)**2)**(-3) * (((m.x35 - m.x58)**2 + (m.x114 - m.x137)**2 +
    (m.x193 - m.x216)**2)**(-3) - 2) + ((m.x35 - m.x59)**2 + (m.x114 - m.x138)
    **2 + (m.x193 - m.x217)**2)**(-3) * (((m.x35 - m.x59)**2 + (m.x114 - m.x138)
    **2 + (m.x193 - m.x217)**2)**(-3) - 2) + ((m.x35 - m.x60)**2 + (m.x114 -
    m.x139)**2 + (m.x193 - m.x218)**2)**(-3) * (((m.x35 - m.x60)**2 + (m.x114
    - m.x139)**2 + (m.x193 - m.x218)**2)**(-3) - 2) + ((m.x35 - m.x61)**2 + (
    m.x114 - m.x140)**2 + (m.x193 - m.x219)**2)**(-3) * (((m.x35 - m.x61)**2 +
    (m.x114 - m.x140)**2 + (m.x193 - m.x219)**2)**(-3) - 2) + ((m.x35 - m.x62)
    **2 + (m.x114 - m.x141)**2 + (m.x193 - m.x220)**2)**(-3) * (((m.x35 - m.x62)
    **2 + (m.x114 - m.x141)**2 + (m.x193 - m.x220)**2)**(-3) - 2) + ((m.x35 -
    m.x63)**2 + (m.x114 - m.x142)**2 + (m.x193 - m.x221)**2)**(-3) * (((m.x35
    - m.x63)**2 + (m.x114 - m.x142)**2 + (m.x193 - m.x221)**2)**(-3) - 2) + ((
    m.x35 - m.x64)**2 + (m.x114 - m.x143)**2 + (m.x193 - m.x222)**2)**(-3) * ((
    (m.x35 - m.x64)**2 + (m.x114 - m.x143)**2 + (m.x193 - m.x222)**2)**(-3) - 2)
    + ((m.x35 - m.x65)**2 + (m.x114 - m.x144)**2 + (m.x193 - m.x223)**2)**(-3)
    * (((m.x35 - m.x65)**2 + (m.x114 - m.x144)**2 + (m.x193 - m.x223)**2)**(-3)
    - 2) + ((m.x35 - m.x66)**2 + (m.x114 - m.x145)**2 + (m.x193 - m.x224)**2)
    **(-3) * (((m.x35 - m.x66)**2 + (m.x114 - m.x145)**2 + (m.x193 - m.x224)**2)
    **(-3) - 2) + ((m.x35 - m.x67)**2 + (m.x114 - m.x146)**2 + (m.x193 - m.x225)
    **2)**(-3) * (((m.x35 - m.x67)**2 + (m.x114 - m.x146)**2 + (m.x193 - m.x225)
    **2)**(-3) - 2) + ((m.x35 - m.x68)**2 + (m.x114 - m.x147)**2 + (m.x193 -
    m.x226)**2)**(-3) * (((m.x35 - m.x68)**2 + (m.x114 - m.x147)**2 + (m.x193
    - m.x226)**2)**(-3) - 2) + ((m.x35 - m.x69)**2 + (m.x114 - m.x148)**2 + (
    m.x193 - m.x227)**2)**(-3) * (((m.x35 - m.x69)**2 + (m.x114 - m.x148)**2 +
    (m.x193 - m.x227)**2)**(-3) - 2) + ((m.x35 - m.x70)**2 + (m.x114 - m.x149)
    **2 + (m.x193 - m.x228)**2)**(-3) * (((m.x35 - m.x70)**2 + (m.x114 - m.x149)
    **2 + (m.x193 - m.x228)**2)**(-3) - 2) + ((m.x35 - m.x71)**2 + (m.x114 -
    m.x150)**2 + (m.x193 - m.x229)**2)**(-3) * (((m.x35 - m.x71)**2 + (m.x114
    - m.x150)**2 + (m.x193 - m.x229)**2)**(-3) - 2) + ((m.x35 - m.x72)**2 + (
    m.x114 - m.x151)**2 + (m.x193 - m.x230)**2)**(-3) * (((m.x35 - m.x72)**2 +
    (m.x114 - m.x151)**2 + (m.x193 - m.x230)**2)**(-3) - 2) + ((m.x35 - m.x73)
    **2 + (m.x114 - m.x152)**2 + (m.x193 - m.x231)**2)**(-3) * (((m.x35 - m.x73)
    **2 + (m.x114 - m.x152)**2 + (m.x193 - m.x231)**2)**(-3) - 2) + ((m.x35 -
    m.x74)**2 + (m.x114 - m.x153)**2 + (m.x193 - m.x232)**2)**(-3) * (((m.x35
    - m.x74)**2 + (m.x114 - m.x153)**2 + (m.x193 - m.x232)**2)**(-3) - 2) + ((
    m.x35 - m.x75)**2 + (m.x114 - m.x154)**2 + (m.x193 - m.x233)**2)**(-3) * ((
    (m.x35 - m.x75)**2 + (m.x114 - m.x154)**2 + (m.x193 - m.x233)**2)**(-3) - 2)
    + ((m.x35 - m.x76)**2 + (m.x114 - m.x155)**2 + (m.x193 - m.x234)**2)**(-3)
    * (((m.x35 - m.x76)**2 + (m.x114 - m.x155)**2 + (m.x193 - m.x234)**2)**(-3)
    - 2) + ((m.x35 - m.x77)**2 + (m.x114 - m.x156)**2 + (m.x193 - m.x235)**2)
    **(-3) * (((m.x35 - m.x77)**2 + (m.x114 - m.x156)**2 + (m.x193 - m.x235)**2)
    **(-3) - 2) + ((m.x35 - m.x78)**2 + (m.x114 - m.x157)**2 + (m.x193 - m.x236)
    **2)**(-3) * (((m.x35 - m.x78)**2 + (m.x114 - m.x157)**2 + (m.x193 - m.x236)
    **2)**(-3) - 2) + ((m.x35 - m.x79)**2 + (m.x114 - m.x158)**2 + (m.x193 -
    m.x237)**2)**(-3) * (((m.x35 - m.x79)**2 + (m.x114 - m.x158)**2 + (m.x193
    - m.x237)**2)**(-3) - 2) + ((m.x36 - m.x37)**2 + (m.x115 - m.x116)**2 + (
    m.x194 - m.x195)**2)**(-3) * (((m.x36 - m.x37)**2 + (m.x115 - m.x116)**2 +
    (m.x194 - m.x195)**2)**(-3) - 2) + ((m.x36 - m.x38)**2 + (m.x115 - m.x117)
    **2 + (m.x194 - m.x196)**2)**(-3) * (((m.x36 - m.x38)**2 + (m.x115 - m.x117)
    **2 + (m.x194 - m.x196)**2)**(-3) - 2) + ((m.x36 - m.x39)**2 + (m.x115 -
    m.x118)**2 + (m.x194 - m.x197)**2)**(-3) * (((m.x36 - m.x39)**2 + (m.x115
    - m.x118)**2 + (m.x194 - m.x197)**2)**(-3) - 2) + ((m.x36 - m.x40)**2 + (
    m.x115 - m.x119)**2 + (m.x194 - m.x198)**2)**(-3) * (((m.x36 - m.x40)**2 +
    (m.x115 - m.x119)**2 + (m.x194 - m.x198)**2)**(-3) - 2) + ((m.x36 - m.x41)
    **2 + (m.x115 - m.x120)**2 + (m.x194 - m.x199)**2)**(-3) * (((m.x36 - m.x41)
    **2 + (m.x115 - m.x120)**2 + (m.x194 - m.x199)**2)**(-3) - 2) + ((m.x36 -
    m.x42)**2 + (m.x115 - m.x121)**2 + (m.x194 - m.x200)**2)**(-3) * (((m.x36
    - m.x42)**2 + (m.x115 - m.x121)**2 + (m.x194 - m.x200)**2)**(-3) - 2) + ((
    m.x36 - m.x43)**2 + (m.x115 - m.x122)**2 + (m.x194 - m.x201)**2)**(-3) * ((
    (m.x36 - m.x43)**2 + (m.x115 - m.x122)**2 + (m.x194 - m.x201)**2)**(-3) - 2)
    + ((m.x36 - m.x44)**2 + (m.x115 - m.x123)**2 + (m.x194 - m.x202)**2)**(-3)
    * (((m.x36 - m.x44)**2 + (m.x115 - m.x123)**2 + (m.x194 - m.x202)**2)**(-3)
    - 2) + ((m.x36 - m.x45)**2 + (m.x115 - m.x124)**2 + (m.x194 - m.x203)**2)
    **(-3) * (((m.x36 - m.x45)**2 + (m.x115 - m.x124)**2 + (m.x194 - m.x203)**2)
    **(-3) - 2) + ((m.x36 - m.x46)**2 + (m.x115 - m.x125)**2 + (m.x194 - m.x204)
    **2)**(-3) * (((m.x36 - m.x46)**2 + (m.x115 - m.x125)**2 + (m.x194 - m.x204)
    **2)**(-3) - 2) + ((m.x36 - m.x47)**2 + (m.x115 - m.x126)**2 + (m.x194 -
    m.x205)**2)**(-3) * (((m.x36 - m.x47)**2 + (m.x115 - m.x126)**2 + (m.x194
    - m.x205)**2)**(-3) - 2) + ((m.x36 - m.x48)**2 + (m.x115 - m.x127)**2 + (
    m.x194 - m.x206)**2)**(-3) * (((m.x36 - m.x48)**2 + (m.x115 - m.x127)**2 +
    (m.x194 - m.x206)**2)**(-3) - 2) + ((m.x36 - m.x49)**2 + (m.x115 - m.x128)
    **2 + (m.x194 - m.x207)**2)**(-3) * (((m.x36 - m.x49)**2 + (m.x115 - m.x128)
    **2 + (m.x194 - m.x207)**2)**(-3) - 2) + ((m.x36 - m.x50)**2 + (m.x115 -
    m.x129)**2 + (m.x194 - m.x208)**2)**(-3) * (((m.x36 - m.x50)**2 + (m.x115
    - m.x129)**2 + (m.x194 - m.x208)**2)**(-3) - 2) + ((m.x36 - m.x51)**2 + (
    m.x115 - m.x130)**2 + (m.x194 - m.x209)**2)**(-3) * (((m.x36 - m.x51)**2 +
    (m.x115 - m.x130)**2 + (m.x194 - m.x209)**2)**(-3) - 2) + ((m.x36 - m.x52)
    **2 + (m.x115 - m.x131)**2 + (m.x194 - m.x210)**2)**(-3) * (((m.x36 - m.x52)
    **2 + (m.x115 - m.x131)**2 + (m.x194 - m.x210)**2)**(-3) - 2) + ((m.x36 -
    m.x53)**2 + (m.x115 - m.x132)**2 + (m.x194 - m.x211)**2)**(-3) * (((m.x36
    - m.x53)**2 + (m.x115 - m.x132)**2 + (m.x194 - m.x211)**2)**(-3) - 2) + ((
    m.x36 - m.x54)**2 + (m.x115 - m.x133)**2 + (m.x194 - m.x212)**2)**(-3) * ((
    (m.x36 - m.x54)**2 + (m.x115 - m.x133)**2 + (m.x194 - m.x212)**2)**(-3) - 2)
    + ((m.x36 - m.x55)**2 + (m.x115 - m.x134)**2 + (m.x194 - m.x213)**2)**(-3)
    * (((m.x36 - m.x55)**2 + (m.x115 - m.x134)**2 + (m.x194 - m.x213)**2)**(-3)
    - 2) + ((m.x36 - m.x56)**2 + (m.x115 - m.x135)**2 + (m.x194 - m.x214)**2)
    **(-3) * (((m.x36 - m.x56)**2 + (m.x115 - m.x135)**2 + (m.x194 - m.x214)**2)
    **(-3) - 2) + ((m.x36 - m.x57)**2 + (m.x115 - m.x136)**2 + (m.x194 - m.x215)
    **2)**(-3) * (((m.x36 - m.x57)**2 + (m.x115 - m.x136)**2 + (m.x194 - m.x215)
    **2)**(-3) - 2) + ((m.x36 - m.x58)**2 + (m.x115 - m.x137)**2 + (m.x194 -
    m.x216)**2)**(-3) * (((m.x36 - m.x58)**2 + (m.x115 - m.x137)**2 + (m.x194
    - m.x216)**2)**(-3) - 2) + ((m.x36 - m.x59)**2 + (m.x115 - m.x138)**2 + (
    m.x194 - m.x217)**2)**(-3) * (((m.x36 - m.x59)**2 + (m.x115 - m.x138)**2 +
    (m.x194 - m.x217)**2)**(-3) - 2) + ((m.x36 - m.x60)**2 + (m.x115 - m.x139)
    **2 + (m.x194 - m.x218)**2)**(-3) * (((m.x36 - m.x60)**2 + (m.x115 - m.x139)
    **2 + (m.x194 - m.x218)**2)**(-3) - 2) + ((m.x36 - m.x61)**2 + (m.x115 -
    m.x140)**2 + (m.x194 - m.x219)**2)**(-3) * (((m.x36 - m.x61)**2 + (m.x115
    - m.x140)**2 + (m.x194 - m.x219)**2)**(-3) - 2) + ((m.x36 - m.x62)**2 + (
    m.x115 - m.x141)**2 + (m.x194 - m.x220)**2)**(-3) * (((m.x36 - m.x62)**2 +
    (m.x115 - m.x141)**2 + (m.x194 - m.x220)**2)**(-3) - 2) + ((m.x36 - m.x63)
    **2 + (m.x115 - m.x142)**2 + (m.x194 - m.x221)**2)**(-3) * (((m.x36 - m.x63)
    **2 + (m.x115 - m.x142)**2 + (m.x194 - m.x221)**2)**(-3) - 2) + ((m.x36 -
    m.x64)**2 + (m.x115 - m.x143)**2 + (m.x194 - m.x222)**2)**(-3) * (((m.x36
    - m.x64)**2 + (m.x115 - m.x143)**2 + (m.x194 - m.x222)**2)**(-3) - 2) + ((
    m.x36 - m.x65)**2 + (m.x115 - m.x144)**2 + (m.x194 - m.x223)**2)**(-3) * ((
    (m.x36 - m.x65)**2 + (m.x115 - m.x144)**2 + (m.x194 - m.x223)**2)**(-3) - 2)
    + ((m.x36 - m.x66)**2 + (m.x115 - m.x145)**2 + (m.x194 - m.x224)**2)**(-3)
    * (((m.x36 - m.x66)**2 + (m.x115 - m.x145)**2 + (m.x194 - m.x224)**2)**(-3)
    - 2) + ((m.x36 - m.x67)**2 + (m.x115 - m.x146)**2 + (m.x194 - m.x225)**2)
    **(-3) * (((m.x36 - m.x67)**2 + (m.x115 - m.x146)**2 + (m.x194 - m.x225)**2)
    **(-3) - 2) + ((m.x36 - m.x68)**2 + (m.x115 - m.x147)**2 + (m.x194 - m.x226)
    **2)**(-3) * (((m.x36 - m.x68)**2 + (m.x115 - m.x147)**2 + (m.x194 - m.x226)
    **2)**(-3) - 2) + ((m.x36 - m.x69)**2 + (m.x115 - m.x148)**2 + (m.x194 -
    m.x227)**2)**(-3) * (((m.x36 - m.x69)**2 + (m.x115 - m.x148)**2 + (m.x194
    - m.x227)**2)**(-3) - 2) + ((m.x36 - m.x70)**2 + (m.x115 - m.x149)**2 + (
    m.x194 - m.x228)**2)**(-3) * (((m.x36 - m.x70)**2 + (m.x115 - m.x149)**2 +
    (m.x194 - m.x228)**2)**(-3) - 2) + ((m.x36 - m.x71)**2 + (m.x115 - m.x150)
    **2 + (m.x194 - m.x229)**2)**(-3) * (((m.x36 - m.x71)**2 + (m.x115 - m.x150)
    **2 + (m.x194 - m.x229)**2)**(-3) - 2) + ((m.x36 - m.x72)**2 + (m.x115 -
    m.x151)**2 + (m.x194 - m.x230)**2)**(-3) * (((m.x36 - m.x72)**2 + (m.x115
    - m.x151)**2 + (m.x194 - m.x230)**2)**(-3) - 2) + ((m.x36 - m.x73)**2 + (
    m.x115 - m.x152)**2 + (m.x194 - m.x231)**2)**(-3) * (((m.x36 - m.x73)**2 +
    (m.x115 - m.x152)**2 + (m.x194 - m.x231)**2)**(-3) - 2) + ((m.x36 - m.x74)
    **2 + (m.x115 - m.x153)**2 + (m.x194 - m.x232)**2)**(-3) * (((m.x36 - m.x74)
    **2 + (m.x115 - m.x153)**2 + (m.x194 - m.x232)**2)**(-3) - 2) + ((m.x36 -
    m.x75)**2 + (m.x115 - m.x154)**2 + (m.x194 - m.x233)**2)**(-3) * (((m.x36
    - m.x75)**2 + (m.x115 - m.x154)**2 + (m.x194 - m.x233)**2)**(-3) - 2) + ((
    m.x36 - m.x76)**2 + (m.x115 - m.x155)**2 + (m.x194 - m.x234)**2)**(-3) * ((
    (m.x36 - m.x76)**2 + (m.x115 - m.x155)**2 + (m.x194 - m.x234)**2)**(-3) - 2)
    + ((m.x36 - m.x77)**2 + (m.x115 - m.x156)**2 + (m.x194 - m.x235)**2)**(-3)
    * (((m.x36 - m.x77)**2 + (m.x115 - m.x156)**2 + (m.x194 - m.x235)**2)**(-3)
    - 2) + ((m.x36 - m.x78)**2 + (m.x115 - m.x157)**2 + (m.x194 - m.x236)**2)
    **(-3) * (((m.x36 - m.x78)**2 + (m.x115 - m.x157)**2 + (m.x194 - m.x236)**2)
    **(-3) - 2) + ((m.x36 - m.x79)**2 + (m.x115 - m.x158)**2 + (m.x194 - m.x237)
    **2)**(-3) * (((m.x36 - m.x79)**2 + (m.x115 - m.x158)**2 + (m.x194 - m.x237)
    **2)**(-3) - 2) + ((m.x37 - m.x38)**2 + (m.x116 - m.x117)**2 + (m.x195 -
    m.x196)**2)**(-3) * (((m.x37 - m.x38)**2 + (m.x116 - m.x117)**2 + (m.x195
    - m.x196)**2)**(-3) - 2) + ((m.x37 - m.x39)**2 + (m.x116 - m.x118)**2 + (
    m.x195 - m.x197)**2)**(-3) * (((m.x37 - m.x39)**2 + (m.x116 - m.x118)**2 +
    (m.x195 - m.x197)**2)**(-3) - 2) + ((m.x37 - m.x40)**2 + (m.x116 - m.x119)
    **2 + (m.x195 - m.x198)**2)**(-3) * (((m.x37 - m.x40)**2 + (m.x116 - m.x119)
    **2 + (m.x195 - m.x198)**2)**(-3) - 2) + ((m.x37 - m.x41)**2 + (m.x116 -
    m.x120)**2 + (m.x195 - m.x199)**2)**(-3) * (((m.x37 - m.x41)**2 + (m.x116
    - m.x120)**2 + (m.x195 - m.x199)**2)**(-3) - 2) + ((m.x37 - m.x42)**2 + (
    m.x116 - m.x121)**2 + (m.x195 - m.x200)**2)**(-3) * (((m.x37 - m.x42)**2 +
    (m.x116 - m.x121)**2 + (m.x195 - m.x200)**2)**(-3) - 2) + ((m.x37 - m.x43)
    **2 + (m.x116 - m.x122)**2 + (m.x195 - m.x201)**2)**(-3) * (((m.x37 - m.x43)
    **2 + (m.x116 - m.x122)**2 + (m.x195 - m.x201)**2)**(-3) - 2) + ((m.x37 -
    m.x44)**2 + (m.x116 - m.x123)**2 + (m.x195 - m.x202)**2)**(-3) * (((m.x37
    - m.x44)**2 + (m.x116 - m.x123)**2 + (m.x195 - m.x202)**2)**(-3) - 2) + ((
    m.x37 - m.x45)**2 + (m.x116 - m.x124)**2 + (m.x195 - m.x203)**2)**(-3) * ((
    (m.x37 - m.x45)**2 + (m.x116 - m.x124)**2 + (m.x195 - m.x203)**2)**(-3) - 2)
    + ((m.x37 - m.x46)**2 + (m.x116 - m.x125)**2 + (m.x195 - m.x204)**2)**(-3)
    * (((m.x37 - m.x46)**2 + (m.x116 - m.x125)**2 + (m.x195 - m.x204)**2)**(-3)
    - 2) + ((m.x37 - m.x47)**2 + (m.x116 - m.x126)**2 + (m.x195 - m.x205)**2)
    **(-3) * (((m.x37 - m.x47)**2 + (m.x116 - m.x126)**2 + (m.x195 - m.x205)**2)
    **(-3) - 2) + ((m.x37 - m.x48)**2 + (m.x116 - m.x127)**2 + (m.x195 - m.x206)
    **2)**(-3) * (((m.x37 - m.x48)**2 + (m.x116 - m.x127)**2 + (m.x195 - m.x206)
    **2)**(-3) - 2) + ((m.x37 - m.x49)**2 + (m.x116 - m.x128)**2 + (m.x195 -
    m.x207)**2)**(-3) * (((m.x37 - m.x49)**2 + (m.x116 - m.x128)**2 + (m.x195
    - m.x207)**2)**(-3) - 2) + ((m.x37 - m.x50)**2 + (m.x116 - m.x129)**2 + (
    m.x195 - m.x208)**2)**(-3) * (((m.x37 - m.x50)**2 + (m.x116 - m.x129)**2 +
    (m.x195 - m.x208)**2)**(-3) - 2) + ((m.x37 - m.x51)**2 + (m.x116 - m.x130)
    **2 + (m.x195 - m.x209)**2)**(-3) * (((m.x37 - m.x51)**2 + (m.x116 - m.x130)
    **2 + (m.x195 - m.x209)**2)**(-3) - 2) + ((m.x37 - m.x52)**2 + (m.x116 -
    m.x131)**2 + (m.x195 - m.x210)**2)**(-3) * (((m.x37 - m.x52)**2 + (m.x116
    - m.x131)**2 + (m.x195 - m.x210)**2)**(-3) - 2) + ((m.x37 - m.x53)**2 + (
    m.x116 - m.x132)**2 + (m.x195 - m.x211)**2)**(-3) * (((m.x37 - m.x53)**2 +
    (m.x116 - m.x132)**2 + (m.x195 - m.x211)**2)**(-3) - 2) + ((m.x37 - m.x54)
    **2 + (m.x116 - m.x133)**2 + (m.x195 - m.x212)**2)**(-3) * (((m.x37 - m.x54)
    **2 + (m.x116 - m.x133)**2 + (m.x195 - m.x212)**2)**(-3) - 2) + ((m.x37 -
    m.x55)**2 + (m.x116 - m.x134)**2 + (m.x195 - m.x213)**2)**(-3) * (((m.x37
    - m.x55)**2 + (m.x116 - m.x134)**2 + (m.x195 - m.x213)**2)**(-3) - 2) + ((
    m.x37 - m.x56)**2 + (m.x116 - m.x135)**2 + (m.x195 - m.x214)**2)**(-3) * ((
    (m.x37 - m.x56)**2 + (m.x116 - m.x135)**2 + (m.x195 - m.x214)**2)**(-3) - 2)
    + ((m.x37 - m.x57)**2 + (m.x116 - m.x136)**2 + (m.x195 - m.x215)**2)**(-3)
    * (((m.x37 - m.x57)**2 + (m.x116 - m.x136)**2 + (m.x195 - m.x215)**2)**(-3)
    - 2) + ((m.x37 - m.x58)**2 + (m.x116 - m.x137)**2 + (m.x195 - m.x216)**2)
    **(-3) * (((m.x37 - m.x58)**2 + (m.x116 - m.x137)**2 + (m.x195 - m.x216)**2)
    **(-3) - 2) + ((m.x37 - m.x59)**2 + (m.x116 - m.x138)**2 + (m.x195 - m.x217)
    **2)**(-3) * (((m.x37 - m.x59)**2 + (m.x116 - m.x138)**2 + (m.x195 - m.x217)
    **2)**(-3) - 2) + ((m.x37 - m.x60)**2 + (m.x116 - m.x139)**2 + (m.x195 -
    m.x218)**2)**(-3) * (((m.x37 - m.x60)**2 + (m.x116 - m.x139)**2 + (m.x195
    - m.x218)**2)**(-3) - 2) + ((m.x37 - m.x61)**2 + (m.x116 - m.x140)**2 + (
    m.x195 - m.x219)**2)**(-3) * (((m.x37 - m.x61)**2 + (m.x116 - m.x140)**2 +
    (m.x195 - m.x219)**2)**(-3) - 2) + ((m.x37 - m.x62)**2 + (m.x116 - m.x141)
    **2 + (m.x195 - m.x220)**2)**(-3) * (((m.x37 - m.x62)**2 + (m.x116 - m.x141)
    **2 + (m.x195 - m.x220)**2)**(-3) - 2) + ((m.x37 - m.x63)**2 + (m.x116 -
    m.x142)**2 + (m.x195 - m.x221)**2)**(-3) * (((m.x37 - m.x63)**2 + (m.x116
    - m.x142)**2 + (m.x195 - m.x221)**2)**(-3) - 2) + ((m.x37 - m.x64)**2 + (
    m.x116 - m.x143)**2 + (m.x195 - m.x222)**2)**(-3) * (((m.x37 - m.x64)**2 +
    (m.x116 - m.x143)**2 + (m.x195 - m.x222)**2)**(-3) - 2) + ((m.x37 - m.x65)
    **2 + (m.x116 - m.x144)**2 + (m.x195 - m.x223)**2)**(-3) * (((m.x37 - m.x65)
    **2 + (m.x116 - m.x144)**2 + (m.x195 - m.x223)**2)**(-3) - 2) + ((m.x37 -
    m.x66)**2 + (m.x116 - m.x145)**2 + (m.x195 - m.x224)**2)**(-3) * (((m.x37
    - m.x66)**2 + (m.x116 - m.x145)**2 + (m.x195 - m.x224)**2)**(-3) - 2) + ((
    m.x37 - m.x67)**2 + (m.x116 - m.x146)**2 + (m.x195 - m.x225)**2)**(-3) * ((
    (m.x37 - m.x67)**2 + (m.x116 - m.x146)**2 + (m.x195 - m.x225)**2)**(-3) - 2)
    + ((m.x37 - m.x68)**2 + (m.x116 - m.x147)**2 + (m.x195 - m.x226)**2)**(-3)
    * (((m.x37 - m.x68)**2 + (m.x116 - m.x147)**2 + (m.x195 - m.x226)**2)**(-3)
    - 2) + ((m.x37 - m.x69)**2 + (m.x116 - m.x148)**2 + (m.x195 - m.x227)**2)
    **(-3) * (((m.x37 - m.x69)**2 + (m.x116 - m.x148)**2 + (m.x195 - m.x227)**2)
    **(-3) - 2) + ((m.x37 - m.x70)**2 + (m.x116 - m.x149)**2 + (m.x195 - m.x228)
    **2)**(-3) * (((m.x37 - m.x70)**2 + (m.x116 - m.x149)**2 + (m.x195 - m.x228)
    **2)**(-3) - 2) + ((m.x37 - m.x71)**2 + (m.x116 - m.x150)**2 + (m.x195 -
    m.x229)**2)**(-3) * (((m.x37 - m.x71)**2 + (m.x116 - m.x150)**2 + (m.x195
    - m.x229)**2)**(-3) - 2) + ((m.x37 - m.x72)**2 + (m.x116 - m.x151)**2 + (
    m.x195 - m.x230)**2)**(-3) * (((m.x37 - m.x72)**2 + (m.x116 - m.x151)**2 +
    (m.x195 - m.x230)**2)**(-3) - 2) + ((m.x37 - m.x73)**2 + (m.x116 - m.x152)
    **2 + (m.x195 - m.x231)**2)**(-3) * (((m.x37 - m.x73)**2 + (m.x116 - m.x152)
    **2 + (m.x195 - m.x231)**2)**(-3) - 2) + ((m.x37 - m.x74)**2 + (m.x116 -
    m.x153)**2 + (m.x195 - m.x232)**2)**(-3) * (((m.x37 - m.x74)**2 + (m.x116
    - m.x153)**2 + (m.x195 - m.x232)**2)**(-3) - 2) + ((m.x37 - m.x75)**2 + (
    m.x116 - m.x154)**2 + (m.x195 - m.x233)**2)**(-3) * (((m.x37 - m.x75)**2 +
    (m.x116 - m.x154)**2 + (m.x195 - m.x233)**2)**(-3) - 2) + ((m.x37 - m.x76)
    **2 + (m.x116 - m.x155)**2 + (m.x195 - m.x234)**2)**(-3) * (((m.x37 - m.x76)
    **2 + (m.x116 - m.x155)**2 + (m.x195 - m.x234)**2)**(-3) - 2) + ((m.x37 -
    m.x77)**2 + (m.x116 - m.x156)**2 + (m.x195 - m.x235)**2)**(-3) * (((m.x37
    - m.x77)**2 + (m.x116 - m.x156)**2 + (m.x195 - m.x235)**2)**(-3) - 2) + ((
    m.x37 - m.x78)**2 + (m.x116 - m.x157)**2 + (m.x195 - m.x236)**2)**(-3) * ((
    (m.x37 - m.x78)**2 + (m.x116 - m.x157)**2 + (m.x195 - m.x236)**2)**(-3) - 2)
    + ((m.x37 - m.x79)**2 + (m.x116 - m.x158)**2 + (m.x195 - m.x237)**2)**(-3)
    * (((m.x37 - m.x79)**2 + (m.x116 - m.x158)**2 + (m.x195 - m.x237)**2)**(-3)
    - 2) + ((m.x38 - m.x39)**2 + (m.x117 - m.x118)**2 + (m.x196 - m.x197)**2)
    **(-3) * (((m.x38 - m.x39)**2 + (m.x117 - m.x118)**2 + (m.x196 - m.x197)**2)
    **(-3) - 2) + ((m.x38 - m.x40)**2 + (m.x117 - m.x119)**2 + (m.x196 - m.x198)
    **2)**(-3) * (((m.x38 - m.x40)**2 + (m.x117 - m.x119)**2 + (m.x196 - m.x198)
    **2)**(-3) - 2) + ((m.x38 - m.x41)**2 + (m.x117 - m.x120)**2 + (m.x196 -
    m.x199)**2)**(-3) * (((m.x38 - m.x41)**2 + (m.x117 - m.x120)**2 + (m.x196
    - m.x199)**2)**(-3) - 2) + ((m.x38 - m.x42)**2 + (m.x117 - m.x121)**2 + (
    m.x196 - m.x200)**2)**(-3) * (((m.x38 - m.x42)**2 + (m.x117 - m.x121)**2 +
    (m.x196 - m.x200)**2)**(-3) - 2) + ((m.x38 - m.x43)**2 + (m.x117 - m.x122)
    **2 + (m.x196 - m.x201)**2)**(-3) * (((m.x38 - m.x43)**2 + (m.x117 - m.x122)
    **2 + (m.x196 - m.x201)**2)**(-3) - 2) + ((m.x38 - m.x44)**2 + (m.x117 -
    m.x123)**2 + (m.x196 - m.x202)**2)**(-3) * (((m.x38 - m.x44)**2 + (m.x117
    - m.x123)**2 + (m.x196 - m.x202)**2)**(-3) - 2) + ((m.x38 - m.x45)**2 + (
    m.x117 - m.x124)**2 + (m.x196 - m.x203)**2)**(-3) * (((m.x38 - m.x45)**2 +
    (m.x117 - m.x124)**2 + (m.x196 - m.x203)**2)**(-3) - 2) + ((m.x38 - m.x46)
    **2 + (m.x117 - m.x125)**2 + (m.x196 - m.x204)**2)**(-3) * (((m.x38 - m.x46)
    **2 + (m.x117 - m.x125)**2 + (m.x196 - m.x204)**2)**(-3) - 2) + ((m.x38 -
    m.x47)**2 + (m.x117 - m.x126)**2 + (m.x196 - m.x205)**2)**(-3) * (((m.x38
    - m.x47)**2 + (m.x117 - m.x126)**2 + (m.x196 - m.x205)**2)**(-3) - 2) + ((
    m.x38 - m.x48)**2 + (m.x117 - m.x127)**2 + (m.x196 - m.x206)**2)**(-3) * ((
    (m.x38 - m.x48)**2 + (m.x117 - m.x127)**2 + (m.x196 - m.x206)**2)**(-3) - 2)
    + ((m.x38 - m.x49)**2 + (m.x117 - m.x128)**2 + (m.x196 - m.x207)**2)**(-3)
    * (((m.x38 - m.x49)**2 + (m.x117 - m.x128)**2 + (m.x196 - m.x207)**2)**(-3)
    - 2) + ((m.x38 - m.x50)**2 + (m.x117 - m.x129)**2 + (m.x196 - m.x208)**2)
    **(-3) * (((m.x38 - m.x50)**2 + (m.x117 - m.x129)**2 + (m.x196 - m.x208)**2)
    **(-3) - 2) + ((m.x38 - m.x51)**2 + (m.x117 - m.x130)**2 + (m.x196 - m.x209)
    **2)**(-3) * (((m.x38 - m.x51)**2 + (m.x117 - m.x130)**2 + (m.x196 - m.x209)
    **2)**(-3) - 2) + ((m.x38 - m.x52)**2 + (m.x117 - m.x131)**2 + (m.x196 -
    m.x210)**2)**(-3) * (((m.x38 - m.x52)**2 + (m.x117 - m.x131)**2 + (m.x196
    - m.x210)**2)**(-3) - 2) + ((m.x38 - m.x53)**2 + (m.x117 - m.x132)**2 + (
    m.x196 - m.x211)**2)**(-3) * (((m.x38 - m.x53)**2 + (m.x117 - m.x132)**2 +
    (m.x196 - m.x211)**2)**(-3) - 2) + ((m.x38 - m.x54)**2 + (m.x117 - m.x133)
    **2 + (m.x196 - m.x212)**2)**(-3) * (((m.x38 - m.x54)**2 + (m.x117 - m.x133)
    **2 + (m.x196 - m.x212)**2)**(-3) - 2) + ((m.x38 - m.x55)**2 + (m.x117 -
    m.x134)**2 + (m.x196 - m.x213)**2)**(-3) * (((m.x38 - m.x55)**2 + (m.x117
    - m.x134)**2 + (m.x196 - m.x213)**2)**(-3) - 2) + ((m.x38 - m.x56)**2 + (
    m.x117 - m.x135)**2 + (m.x196 - m.x214)**2)**(-3) * (((m.x38 - m.x56)**2 +
    (m.x117 - m.x135)**2 + (m.x196 - m.x214)**2)**(-3) - 2) + ((m.x38 - m.x57)
    **2 + (m.x117 - m.x136)**2 + (m.x196 - m.x215)**2)**(-3) * (((m.x38 - m.x57)
    **2 + (m.x117 - m.x136)**2 + (m.x196 - m.x215)**2)**(-3) - 2) + ((m.x38 -
    m.x58)**2 + (m.x117 - m.x137)**2 + (m.x196 - m.x216)**2)**(-3) * (((m.x38
    - m.x58)**2 + (m.x117 - m.x137)**2 + (m.x196 - m.x216)**2)**(-3) - 2) + ((
    m.x38 - m.x59)**2 + (m.x117 - m.x138)**2 + (m.x196 - m.x217)**2)**(-3) * ((
    (m.x38 - m.x59)**2 + (m.x117 - m.x138)**2 + (m.x196 - m.x217)**2)**(-3) - 2)
    + ((m.x38 - m.x60)**2 + (m.x117 - m.x139)**2 + (m.x196 - m.x218)**2)**(-3)
    * (((m.x38 - m.x60)**2 + (m.x117 - m.x139)**2 + (m.x196 - m.x218)**2)**(-3)
    - 2) + ((m.x38 - m.x61)**2 + (m.x117 - m.x140)**2 + (m.x196 - m.x219)**2)
    **(-3) * (((m.x38 - m.x61)**2 + (m.x117 - m.x140)**2 + (m.x196 - m.x219)**2)
    **(-3) - 2) + ((m.x38 - m.x62)**2 + (m.x117 - m.x141)**2 + (m.x196 - m.x220)
    **2)**(-3) * (((m.x38 - m.x62)**2 + (m.x117 - m.x141)**2 + (m.x196 - m.x220)
    **2)**(-3) - 2) + ((m.x38 - m.x63)**2 + (m.x117 - m.x142)**2 + (m.x196 -
    m.x221)**2)**(-3) * (((m.x38 - m.x63)**2 + (m.x117 - m.x142)**2 + (m.x196
    - m.x221)**2)**(-3) - 2) + ((m.x38 - m.x64)**2 + (m.x117 - m.x143)**2 + (
    m.x196 - m.x222)**2)**(-3) * (((m.x38 - m.x64)**2 + (m.x117 - m.x143)**2 +
    (m.x196 - m.x222)**2)**(-3) - 2) + ((m.x38 - m.x65)**2 + (m.x117 - m.x144)
    **2 + (m.x196 - m.x223)**2)**(-3) * (((m.x38 - m.x65)**2 + (m.x117 - m.x144)
    **2 + (m.x196 - m.x223)**2)**(-3) - 2) + ((m.x38 - m.x66)**2 + (m.x117 -
    m.x145)**2 + (m.x196 - m.x224)**2)**(-3) * (((m.x38 - m.x66)**2 + (m.x117
    - m.x145)**2 + (m.x196 - m.x224)**2)**(-3) - 2) + ((m.x38 - m.x67)**2 + (
    m.x117 - m.x146)**2 + (m.x196 - m.x225)**2)**(-3) * (((m.x38 - m.x67)**2 +
    (m.x117 - m.x146)**2 + (m.x196 - m.x225)**2)**(-3) - 2) + ((m.x38 - m.x68)
    **2 + (m.x117 - m.x147)**2 + (m.x196 - m.x226)**2)**(-3) * (((m.x38 - m.x68)
    **2 + (m.x117 - m.x147)**2 + (m.x196 - m.x226)**2)**(-3) - 2) + ((m.x38 -
    m.x69)**2 + (m.x117 - m.x148)**2 + (m.x196 - m.x227)**2)**(-3) * (((m.x38
    - m.x69)**2 + (m.x117 - m.x148)**2 + (m.x196 - m.x227)**2)**(-3) - 2) + ((
    m.x38 - m.x70)**2 + (m.x117 - m.x149)**2 + (m.x196 - m.x228)**2)**(-3) * ((
    (m.x38 - m.x70)**2 + (m.x117 - m.x149)**2 + (m.x196 - m.x228)**2)**(-3) - 2)
    + ((m.x38 - m.x71)**2 + (m.x117 - m.x150)**2 + (m.x196 - m.x229)**2)**(-3)
    * (((m.x38 - m.x71)**2 + (m.x117 - m.x150)**2 + (m.x196 - m.x229)**2)**(-3)
    - 2) + ((m.x38 - m.x72)**2 + (m.x117 - m.x151)**2 + (m.x196 - m.x230)**2)
    **(-3) * (((m.x38 - m.x72)**2 + (m.x117 - m.x151)**2 + (m.x196 - m.x230)**2)
    **(-3) - 2) + ((m.x38 - m.x73)**2 + (m.x117 - m.x152)**2 + (m.x196 - m.x231)
    **2)**(-3) * (((m.x38 - m.x73)**2 + (m.x117 - m.x152)**2 + (m.x196 - m.x231)
    **2)**(-3) - 2) + ((m.x38 - m.x74)**2 + (m.x117 - m.x153)**2 + (m.x196 -
    m.x232)**2)**(-3) * (((m.x38 - m.x74)**2 + (m.x117 - m.x153)**2 + (m.x196
    - m.x232)**2)**(-3) - 2) + ((m.x38 - m.x75)**2 + (m.x117 - m.x154)**2 + (
    m.x196 - m.x233)**2)**(-3) * (((m.x38 - m.x75)**2 + (m.x117 - m.x154)**2 +
    (m.x196 - m.x233)**2)**(-3) - 2) + ((m.x38 - m.x76)**2 + (m.x117 - m.x155)
    **2 + (m.x196 - m.x234)**2)**(-3) * (((m.x38 - m.x76)**2 + (m.x117 - m.x155)
    **2 + (m.x196 - m.x234)**2)**(-3) - 2) + ((m.x38 - m.x77)**2 + (m.x117 -
    m.x156)**2 + (m.x196 - m.x235)**2)**(-3) * (((m.x38 - m.x77)**2 + (m.x117
    - m.x156)**2 + (m.x196 - m.x235)**2)**(-3) - 2) + ((m.x38 - m.x78)**2 + (
    m.x117 - m.x157)**2 + (m.x196 - m.x236)**2)**(-3) * (((m.x38 - m.x78)**2 +
    (m.x117 - m.x157)**2 + (m.x196 - m.x236)**2)**(-3) - 2) + ((m.x38 - m.x79)
    **2 + (m.x117 - m.x158)**2 + (m.x196 - m.x237)**2)**(-3) * (((m.x38 - m.x79)
    **2 + (m.x117 - m.x158)**2 + (m.x196 - m.x237)**2)**(-3) - 2) + ((m.x39 -
    m.x40)**2 + (m.x118 - m.x119)**2 + (m.x197 - m.x198)**2)**(-3) * (((m.x39
    - m.x40)**2 + (m.x118 - m.x119)**2 + (m.x197 - m.x198)**2)**(-3) - 2) + ((
    m.x39 - m.x41)**2 + (m.x118 - m.x120)**2 + (m.x197 - m.x199)**2)**(-3) * ((
    (m.x39 - m.x41)**2 + (m.x118 - m.x120)**2 + (m.x197 - m.x199)**2)**(-3) - 2)
    + ((m.x39 - m.x42)**2 + (m.x118 - m.x121)**2 + (m.x197 - m.x200)**2)**(-3)
    * (((m.x39 - m.x42)**2 + (m.x118 - m.x121)**2 + (m.x197 - m.x200)**2)**(-3)
    - 2) + ((m.x39 - m.x43)**2 + (m.x118 - m.x122)**2 + (m.x197 - m.x201)**2)
    **(-3) * (((m.x39 - m.x43)**2 + (m.x118 - m.x122)**2 + (m.x197 - m.x201)**2)
    **(-3) - 2) + ((m.x39 - m.x44)**2 + (m.x118 - m.x123)**2 + (m.x197 - m.x202)
    **2)**(-3) * (((m.x39 - m.x44)**2 + (m.x118 - m.x123)**2 + (m.x197 - m.x202)
    **2)**(-3) - 2) + ((m.x39 - m.x45)**2 + (m.x118 - m.x124)**2 + (m.x197 -
    m.x203)**2)**(-3) * (((m.x39 - m.x45)**2 + (m.x118 - m.x124)**2 + (m.x197
    - m.x203)**2)**(-3) - 2) + ((m.x39 - m.x46)**2 + (m.x118 - m.x125)**2 + (
    m.x197 - m.x204)**2)**(-3) * (((m.x39 - m.x46)**2 + (m.x118 - m.x125)**2 +
    (m.x197 - m.x204)**2)**(-3) - 2) + ((m.x39 - m.x47)**2 + (m.x118 - m.x126)
    **2 + (m.x197 - m.x205)**2)**(-3) * (((m.x39 - m.x47)**2 + (m.x118 - m.x126)
    **2 + (m.x197 - m.x205)**2)**(-3) - 2) + ((m.x39 - m.x48)**2 + (m.x118 -
    m.x127)**2 + (m.x197 - m.x206)**2)**(-3) * (((m.x39 - m.x48)**2 + (m.x118
    - m.x127)**2 + (m.x197 - m.x206)**2)**(-3) - 2) + ((m.x39 - m.x49)**2 + (
    m.x118 - m.x128)**2 + (m.x197 - m.x207)**2)**(-3) * (((m.x39 - m.x49)**2 +
    (m.x118 - m.x128)**2 + (m.x197 - m.x207)**2)**(-3) - 2) + ((m.x39 - m.x50)
    **2 + (m.x118 - m.x129)**2 + (m.x197 - m.x208)**2)**(-3) * (((m.x39 - m.x50)
    **2 + (m.x118 - m.x129)**2 + (m.x197 - m.x208)**2)**(-3) - 2) + ((m.x39 -
    m.x51)**2 + (m.x118 - m.x130)**2 + (m.x197 - m.x209)**2)**(-3) * (((m.x39
    - m.x51)**2 + (m.x118 - m.x130)**2 + (m.x197 - m.x209)**2)**(-3) - 2) + ((
    m.x39 - m.x52)**2 + (m.x118 - m.x131)**2 + (m.x197 - m.x210)**2)**(-3) * ((
    (m.x39 - m.x52)**2 + (m.x118 - m.x131)**2 + (m.x197 - m.x210)**2)**(-3) - 2)
    + ((m.x39 - m.x53)**2 + (m.x118 - m.x132)**2 + (m.x197 - m.x211)**2)**(-3)
    * (((m.x39 - m.x53)**2 + (m.x118 - m.x132)**2 + (m.x197 - m.x211)**2)**(-3)
    - 2) + ((m.x39 - m.x54)**2 + (m.x118 - m.x133)**2 + (m.x197 - m.x212)**2)
    **(-3) * (((m.x39 - m.x54)**2 + (m.x118 - m.x133)**2 + (m.x197 - m.x212)**2)
    **(-3) - 2) + ((m.x39 - m.x55)**2 + (m.x118 - m.x134)**2 + (m.x197 - m.x213)
    **2)**(-3) * (((m.x39 - m.x55)**2 + (m.x118 - m.x134)**2 + (m.x197 - m.x213)
    **2)**(-3) - 2) + ((m.x39 - m.x56)**2 + (m.x118 - m.x135)**2 + (m.x197 -
    m.x214)**2)**(-3) * (((m.x39 - m.x56)**2 + (m.x118 - m.x135)**2 + (m.x197
    - m.x214)**2)**(-3) - 2) + ((m.x39 - m.x57)**2 + (m.x118 - m.x136)**2 + (
    m.x197 - m.x215)**2)**(-3) * (((m.x39 - m.x57)**2 + (m.x118 - m.x136)**2 +
    (m.x197 - m.x215)**2)**(-3) - 2) + ((m.x39 - m.x58)**2 + (m.x118 - m.x137)
    **2 + (m.x197 - m.x216)**2)**(-3) * (((m.x39 - m.x58)**2 + (m.x118 - m.x137)
    **2 + (m.x197 - m.x216)**2)**(-3) - 2) + ((m.x39 - m.x59)**2 + (m.x118 -
    m.x138)**2 + (m.x197 - m.x217)**2)**(-3) * (((m.x39 - m.x59)**2 + (m.x118
    - m.x138)**2 + (m.x197 - m.x217)**2)**(-3) - 2) + ((m.x39 - m.x60)**2 + (
    m.x118 - m.x139)**2 + (m.x197 - m.x218)**2)**(-3) * (((m.x39 - m.x60)**2 +
    (m.x118 - m.x139)**2 + (m.x197 - m.x218)**2)**(-3) - 2) + ((m.x39 - m.x61)
    **2 + (m.x118 - m.x140)**2 + (m.x197 - m.x219)**2)**(-3) * (((m.x39 - m.x61)
    **2 + (m.x118 - m.x140)**2 + (m.x197 - m.x219)**2)**(-3) - 2) + ((m.x39 -
    m.x62)**2 + (m.x118 - m.x141)**2 + (m.x197 - m.x220)**2)**(-3) * (((m.x39
    - m.x62)**2 + (m.x118 - m.x141)**2 + (m.x197 - m.x220)**2)**(-3) - 2) + ((
    m.x39 - m.x63)**2 + (m.x118 - m.x142)**2 + (m.x197 - m.x221)**2)**(-3) * ((
    (m.x39 - m.x63)**2 + (m.x118 - m.x142)**2 + (m.x197 - m.x221)**2)**(-3) - 2)
    + ((m.x39 - m.x64)**2 + (m.x118 - m.x143)**2 + (m.x197 - m.x222)**2)**(-3)
    * (((m.x39 - m.x64)**2 + (m.x118 - m.x143)**2 + (m.x197 - m.x222)**2)**(-3)
    - 2) + ((m.x39 - m.x65)**2 + (m.x118 - m.x144)**2 + (m.x197 - m.x223)**2)
    **(-3) * (((m.x39 - m.x65)**2 + (m.x118 - m.x144)**2 + (m.x197 - m.x223)**2)
    **(-3) - 2) + ((m.x39 - m.x66)**2 + (m.x118 - m.x145)**2 + (m.x197 - m.x224)
    **2)**(-3) * (((m.x39 - m.x66)**2 + (m.x118 - m.x145)**2 + (m.x197 - m.x224)
    **2)**(-3) - 2) + ((m.x39 - m.x67)**2 + (m.x118 - m.x146)**2 + (m.x197 -
    m.x225)**2)**(-3) * (((m.x39 - m.x67)**2 + (m.x118 - m.x146)**2 + (m.x197
    - m.x225)**2)**(-3) - 2) + ((m.x39 - m.x68)**2 + (m.x118 - m.x147)**2 + (
    m.x197 - m.x226)**2)**(-3) * (((m.x39 - m.x68)**2 + (m.x118 - m.x147)**2 +
    (m.x197 - m.x226)**2)**(-3) - 2) + ((m.x39 - m.x69)**2 + (m.x118 - m.x148)
    **2 + (m.x197 - m.x227)**2)**(-3) * (((m.x39 - m.x69)**2 + (m.x118 - m.x148)
    **2 + (m.x197 - m.x227)**2)**(-3) - 2) + ((m.x39 - m.x70)**2 + (m.x118 -
    m.x149)**2 + (m.x197 - m.x228)**2)**(-3) * (((m.x39 - m.x70)**2 + (m.x118
    - m.x149)**2 + (m.x197 - m.x228)**2)**(-3) - 2) + ((m.x39 - m.x71)**2 + (
    m.x118 - m.x150)**2 + (m.x197 - m.x229)**2)**(-3) * (((m.x39 - m.x71)**2 +
    (m.x118 - m.x150)**2 + (m.x197 - m.x229)**2)**(-3) - 2) + ((m.x39 - m.x72)
    **2 + (m.x118 - m.x151)**2 + (m.x197 - m.x230)**2)**(-3) * (((m.x39 - m.x72)
    **2 + (m.x118 - m.x151)**2 + (m.x197 - m.x230)**2)**(-3) - 2) + ((m.x39 -
    m.x73)**2 + (m.x118 - m.x152)**2 + (m.x197 - m.x231)**2)**(-3) * (((m.x39
    - m.x73)**2 + (m.x118 - m.x152)**2 + (m.x197 - m.x231)**2)**(-3) - 2) + ((
    m.x39 - m.x74)**2 + (m.x118 - m.x153)**2 + (m.x197 - m.x232)**2)**(-3) * ((
    (m.x39 - m.x74)**2 + (m.x118 - m.x153)**2 + (m.x197 - m.x232)**2)**(-3) - 2)
    + ((m.x39 - m.x75)**2 + (m.x118 - m.x154)**2 + (m.x197 - m.x233)**2)**(-3)
    * (((m.x39 - m.x75)**2 + (m.x118 - m.x154)**2 + (m.x197 - m.x233)**2)**(-3)
    - 2) + ((m.x39 - m.x76)**2 + (m.x118 - m.x155)**2 + (m.x197 - m.x234)**2)
    **(-3) * (((m.x39 - m.x76)**2 + (m.x118 - m.x155)**2 + (m.x197 - m.x234)**2)
    **(-3) - 2) + ((m.x39 - m.x77)**2 + (m.x118 - m.x156)**2 + (m.x197 - m.x235)
    **2)**(-3) * (((m.x39 - m.x77)**2 + (m.x118 - m.x156)**2 + (m.x197 - m.x235)
    **2)**(-3) - 2) + ((m.x39 - m.x78)**2 + (m.x118 - m.x157)**2 + (m.x197 -
    m.x236)**2)**(-3) * (((m.x39 - m.x78)**2 + (m.x118 - m.x157)**2 + (m.x197
    - m.x236)**2)**(-3) - 2) + ((m.x39 - m.x79)**2 + (m.x118 - m.x158)**2 + (
    m.x197 - m.x237)**2)**(-3) * (((m.x39 - m.x79)**2 + (m.x118 - m.x158)**2 +
    (m.x197 - m.x237)**2)**(-3) - 2) + ((m.x40 - m.x41)**2 + (m.x119 - m.x120)
    **2 + (m.x198 - m.x199)**2)**(-3) * (((m.x40 - m.x41)**2 + (m.x119 - m.x120)
    **2 + (m.x198 - m.x199)**2)**(-3) - 2) + ((m.x40 - m.x42)**2 + (m.x119 -
    m.x121)**2 + (m.x198 - m.x200)**2)**(-3) * (((m.x40 - m.x42)**2 + (m.x119
    - m.x121)**2 + (m.x198 - m.x200)**2)**(-3) - 2) + ((m.x40 - m.x43)**2 + (
    m.x119 - m.x122)**2 + (m.x198 - m.x201)**2)**(-3) * (((m.x40 - m.x43)**2 +
    (m.x119 - m.x122)**2 + (m.x198 - m.x201)**2)**(-3) - 2) + ((m.x40 - m.x44)
    **2 + (m.x119 - m.x123)**2 + (m.x198 - m.x202)**2)**(-3) * (((m.x40 - m.x44)
    **2 + (m.x119 - m.x123)**2 + (m.x198 - m.x202)**2)**(-3) - 2) + ((m.x40 -
    m.x45)**2 + (m.x119 - m.x124)**2 + (m.x198 - m.x203)**2)**(-3) * (((m.x40
    - m.x45)**2 + (m.x119 - m.x124)**2 + (m.x198 - m.x203)**2)**(-3) - 2) + ((
    m.x40 - m.x46)**2 + (m.x119 - m.x125)**2 + (m.x198 - m.x204)**2)**(-3) * ((
    (m.x40 - m.x46)**2 + (m.x119 - m.x125)**2 + (m.x198 - m.x204)**2)**(-3) - 2)
    + ((m.x40 - m.x47)**2 + (m.x119 - m.x126)**2 + (m.x198 - m.x205)**2)**(-3)
    * (((m.x40 - m.x47)**2 + (m.x119 - m.x126)**2 + (m.x198 - m.x205)**2)**(-3)
    - 2) + ((m.x40 - m.x48)**2 + (m.x119 - m.x127)**2 + (m.x198 - m.x206)**2)
    **(-3) * (((m.x40 - m.x48)**2 + (m.x119 - m.x127)**2 + (m.x198 - m.x206)**2)
    **(-3) - 2) + ((m.x40 - m.x49)**2 + (m.x119 - m.x128)**2 + (m.x198 - m.x207)
    **2)**(-3) * (((m.x40 - m.x49)**2 + (m.x119 - m.x128)**2 + (m.x198 - m.x207)
    **2)**(-3) - 2) + ((m.x40 - m.x50)**2 + (m.x119 - m.x129)**2 + (m.x198 -
    m.x208)**2)**(-3) * (((m.x40 - m.x50)**2 + (m.x119 - m.x129)**2 + (m.x198
    - m.x208)**2)**(-3) - 2) + ((m.x40 - m.x51)**2 + (m.x119 - m.x130)**2 + (
    m.x198 - m.x209)**2)**(-3) * (((m.x40 - m.x51)**2 + (m.x119 - m.x130)**2 +
    (m.x198 - m.x209)**2)**(-3) - 2) + ((m.x40 - m.x52)**2 + (m.x119 - m.x131)
    **2 + (m.x198 - m.x210)**2)**(-3) * (((m.x40 - m.x52)**2 + (m.x119 - m.x131)
    **2 + (m.x198 - m.x210)**2)**(-3) - 2) + ((m.x40 - m.x53)**2 + (m.x119 -
    m.x132)**2 + (m.x198 - m.x211)**2)**(-3) * (((m.x40 - m.x53)**2 + (m.x119
    - m.x132)**2 + (m.x198 - m.x211)**2)**(-3) - 2) + ((m.x40 - m.x54)**2 + (
    m.x119 - m.x133)**2 + (m.x198 - m.x212)**2)**(-3) * (((m.x40 - m.x54)**2 +
    (m.x119 - m.x133)**2 + (m.x198 - m.x212)**2)**(-3) - 2) + ((m.x40 - m.x55)
    **2 + (m.x119 - m.x134)**2 + (m.x198 - m.x213)**2)**(-3) * (((m.x40 - m.x55)
    **2 + (m.x119 - m.x134)**2 + (m.x198 - m.x213)**2)**(-3) - 2) + ((m.x40 -
    m.x56)**2 + (m.x119 - m.x135)**2 + (m.x198 - m.x214)**2)**(-3) * (((m.x40
    - m.x56)**2 + (m.x119 - m.x135)**2 + (m.x198 - m.x214)**2)**(-3) - 2) + ((
    m.x40 - m.x57)**2 + (m.x119 - m.x136)**2 + (m.x198 - m.x215)**2)**(-3) * ((
    (m.x40 - m.x57)**2 + (m.x119 - m.x136)**2 + (m.x198 - m.x215)**2)**(-3) - 2)
    + ((m.x40 - m.x58)**2 + (m.x119 - m.x137)**2 + (m.x198 - m.x216)**2)**(-3)
    * (((m.x40 - m.x58)**2 + (m.x119 - m.x137)**2 + (m.x198 - m.x216)**2)**(-3)
    - 2) + ((m.x40 - m.x59)**2 + (m.x119 - m.x138)**2 + (m.x198 - m.x217)**2)
    **(-3) * (((m.x40 - m.x59)**2 + (m.x119 - m.x138)**2 + (m.x198 - m.x217)**2)
    **(-3) - 2) + ((m.x40 - m.x60)**2 + (m.x119 - m.x139)**2 + (m.x198 - m.x218)
    **2)**(-3) * (((m.x40 - m.x60)**2 + (m.x119 - m.x139)**2 + (m.x198 - m.x218)
    **2)**(-3) - 2) + ((m.x40 - m.x61)**2 + (m.x119 - m.x140)**2 + (m.x198 -
    m.x219)**2)**(-3) * (((m.x40 - m.x61)**2 + (m.x119 - m.x140)**2 + (m.x198
    - m.x219)**2)**(-3) - 2) + ((m.x40 - m.x62)**2 + (m.x119 - m.x141)**2 + (
    m.x198 - m.x220)**2)**(-3) * (((m.x40 - m.x62)**2 + (m.x119 - m.x141)**2 +
    (m.x198 - m.x220)**2)**(-3) - 2) + ((m.x40 - m.x63)**2 + (m.x119 - m.x142)
    **2 + (m.x198 - m.x221)**2)**(-3) * (((m.x40 - m.x63)**2 + (m.x119 - m.x142)
    **2 + (m.x198 - m.x221)**2)**(-3) - 2) + ((m.x40 - m.x64)**2 + (m.x119 -
    m.x143)**2 + (m.x198 - m.x222)**2)**(-3) * (((m.x40 - m.x64)**2 + (m.x119
    - m.x143)**2 + (m.x198 - m.x222)**2)**(-3) - 2) + ((m.x40 - m.x65)**2 + (
    m.x119 - m.x144)**2 + (m.x198 - m.x223)**2)**(-3) * (((m.x40 - m.x65)**2 +
    (m.x119 - m.x144)**2 + (m.x198 - m.x223)**2)**(-3) - 2) + ((m.x40 - m.x66)
    **2 + (m.x119 - m.x145)**2 + (m.x198 - m.x224)**2)**(-3) * (((m.x40 - m.x66)
    **2 + (m.x119 - m.x145)**2 + (m.x198 - m.x224)**2)**(-3) - 2) + ((m.x40 -
    m.x67)**2 + (m.x119 - m.x146)**2 + (m.x198 - m.x225)**2)**(-3) * (((m.x40
    - m.x67)**2 + (m.x119 - m.x146)**2 + (m.x198 - m.x225)**2)**(-3) - 2) + ((
    m.x40 - m.x68)**2 + (m.x119 - m.x147)**2 + (m.x198 - m.x226)**2)**(-3) * ((
    (m.x40 - m.x68)**2 + (m.x119 - m.x147)**2 + (m.x198 - m.x226)**2)**(-3) - 2)
    + ((m.x40 - m.x69)**2 + (m.x119 - m.x148)**2 + (m.x198 - m.x227)**2)**(-3)
    * (((m.x40 - m.x69)**2 + (m.x119 - m.x148)**2 + (m.x198 - m.x227)**2)**(-3)
    - 2) + ((m.x40 - m.x70)**2 + (m.x119 - m.x149)**2 + (m.x198 - m.x228)**2)
    **(-3) * (((m.x40 - m.x70)**2 + (m.x119 - m.x149)**2 + (m.x198 - m.x228)**2)
    **(-3) - 2) + ((m.x40 - m.x71)**2 + (m.x119 - m.x150)**2 + (m.x198 - m.x229)
    **2)**(-3) * (((m.x40 - m.x71)**2 + (m.x119 - m.x150)**2 + (m.x198 - m.x229)
    **2)**(-3) - 2) + ((m.x40 - m.x72)**2 + (m.x119 - m.x151)**2 + (m.x198 -
    m.x230)**2)**(-3) * (((m.x40 - m.x72)**2 + (m.x119 - m.x151)**2 + (m.x198
    - m.x230)**2)**(-3) - 2) + ((m.x40 - m.x73)**2 + (m.x119 - m.x152)**2 + (
    m.x198 - m.x231)**2)**(-3) * (((m.x40 - m.x73)**2 + (m.x119 - m.x152)**2 +
    (m.x198 - m.x231)**2)**(-3) - 2) + ((m.x40 - m.x74)**2 + (m.x119 - m.x153)
    **2 + (m.x198 - m.x232)**2)**(-3) * (((m.x40 - m.x74)**2 + (m.x119 - m.x153)
    **2 + (m.x198 - m.x232)**2)**(-3) - 2) + ((m.x40 - m.x75)**2 + (m.x119 -
    m.x154)**2 + (m.x198 - m.x233)**2)**(-3) * (((m.x40 - m.x75)**2 + (m.x119
    - m.x154)**2 + (m.x198 - m.x233)**2)**(-3) - 2) + ((m.x40 - m.x76)**2 + (
    m.x119 - m.x155)**2 + (m.x198 - m.x234)**2)**(-3) * (((m.x40 - m.x76)**2 +
    (m.x119 - m.x155)**2 + (m.x198 - m.x234)**2)**(-3) - 2) + ((m.x40 - m.x77)
    **2 + (m.x119 - m.x156)**2 + (m.x198 - m.x235)**2)**(-3) * (((m.x40 - m.x77)
    **2 + (m.x119 - m.x156)**2 + (m.x198 - m.x235)**2)**(-3) - 2) + ((m.x40 -
    m.x78)**2 + (m.x119 - m.x157)**2 + (m.x198 - m.x236)**2)**(-3) * (((m.x40
    - m.x78)**2 + (m.x119 - m.x157)**2 + (m.x198 - m.x236)**2)**(-3) - 2) + ((
    m.x40 - m.x79)**2 + (m.x119 - m.x158)**2 + (m.x198 - m.x237)**2)**(-3) * ((
    (m.x40 - m.x79)**2 + (m.x119 - m.x158)**2 + (m.x198 - m.x237)**2)**(-3) - 2)
    + ((m.x41 - m.x42)**2 + (m.x120 - m.x121)**2 + (m.x199 - m.x200)**2)**(-3)
    * (((m.x41 - m.x42)**2 + (m.x120 - m.x121)**2 + (m.x199 - m.x200)**2)**(-3)
    - 2) + ((m.x41 - m.x43)**2 + (m.x120 - m.x122)**2 + (m.x199 - m.x201)**2)
    **(-3) * (((m.x41 - m.x43)**2 + (m.x120 - m.x122)**2 + (m.x199 - m.x201)**2)
    **(-3) - 2) + ((m.x41 - m.x44)**2 + (m.x120 - m.x123)**2 + (m.x199 - m.x202)
    **2)**(-3) * (((m.x41 - m.x44)**2 + (m.x120 - m.x123)**2 + (m.x199 - m.x202)
    **2)**(-3) - 2) + ((m.x41 - m.x45)**2 + (m.x120 - m.x124)**2 + (m.x199 -
    m.x203)**2)**(-3) * (((m.x41 - m.x45)**2 + (m.x120 - m.x124)**2 + (m.x199
    - m.x203)**2)**(-3) - 2) + ((m.x41 - m.x46)**2 + (m.x120 - m.x125)**2 + (
    m.x199 - m.x204)**2)**(-3) * (((m.x41 - m.x46)**2 + (m.x120 - m.x125)**2 +
    (m.x199 - m.x204)**2)**(-3) - 2) + ((m.x41 - m.x47)**2 + (m.x120 - m.x126)
    **2 + (m.x199 - m.x205)**2)**(-3) * (((m.x41 - m.x47)**2 + (m.x120 - m.x126)
    **2 + (m.x199 - m.x205)**2)**(-3) - 2) + ((m.x41 - m.x48)**2 + (m.x120 -
    m.x127)**2 + (m.x199 - m.x206)**2)**(-3) * (((m.x41 - m.x48)**2 + (m.x120
    - m.x127)**2 + (m.x199 - m.x206)**2)**(-3) - 2) + ((m.x41 - m.x49)**2 + (
    m.x120 - m.x128)**2 + (m.x199 - m.x207)**2)**(-3) * (((m.x41 - m.x49)**2 +
    (m.x120 - m.x128)**2 + (m.x199 - m.x207)**2)**(-3) - 2) + ((m.x41 - m.x50)
    **2 + (m.x120 - m.x129)**2 + (m.x199 - m.x208)**2)**(-3) * (((m.x41 - m.x50)
    **2 + (m.x120 - m.x129)**2 + (m.x199 - m.x208)**2)**(-3) - 2) + ((m.x41 -
    m.x51)**2 + (m.x120 - m.x130)**2 + (m.x199 - m.x209)**2)**(-3) * (((m.x41
    - m.x51)**2 + (m.x120 - m.x130)**2 + (m.x199 - m.x209)**2)**(-3) - 2) + ((
    m.x41 - m.x52)**2 + (m.x120 - m.x131)**2 + (m.x199 - m.x210)**2)**(-3) * ((
    (m.x41 - m.x52)**2 + (m.x120 - m.x131)**2 + (m.x199 - m.x210)**2)**(-3) - 2)
    + ((m.x41 - m.x53)**2 + (m.x120 - m.x132)**2 + (m.x199 - m.x211)**2)**(-3)
    * (((m.x41 - m.x53)**2 + (m.x120 - m.x132)**2 + (m.x199 - m.x211)**2)**(-3)
    - 2) + ((m.x41 - m.x54)**2 + (m.x120 - m.x133)**2 + (m.x199 - m.x212)**2)
    **(-3) * (((m.x41 - m.x54)**2 + (m.x120 - m.x133)**2 + (m.x199 - m.x212)**2)
    **(-3) - 2) + ((m.x41 - m.x55)**2 + (m.x120 - m.x134)**2 + (m.x199 - m.x213)
    **2)**(-3) * (((m.x41 - m.x55)**2 + (m.x120 - m.x134)**2 + (m.x199 - m.x213)
    **2)**(-3) - 2) + ((m.x41 - m.x56)**2 + (m.x120 - m.x135)**2 + (m.x199 -
    m.x214)**2)**(-3) * (((m.x41 - m.x56)**2 + (m.x120 - m.x135)**2 + (m.x199
    - m.x214)**2)**(-3) - 2) + ((m.x41 - m.x57)**2 + (m.x120 - m.x136)**2 + (
    m.x199 - m.x215)**2)**(-3) * (((m.x41 - m.x57)**2 + (m.x120 - m.x136)**2 +
    (m.x199 - m.x215)**2)**(-3) - 2) + ((m.x41 - m.x58)**2 + (m.x120 - m.x137)
    **2 + (m.x199 - m.x216)**2)**(-3) * (((m.x41 - m.x58)**2 + (m.x120 - m.x137)
    **2 + (m.x199 - m.x216)**2)**(-3) - 2) + ((m.x41 - m.x59)**2 + (m.x120 -
    m.x138)**2 + (m.x199 - m.x217)**2)**(-3) * (((m.x41 - m.x59)**2 + (m.x120
    - m.x138)**2 + (m.x199 - m.x217)**2)**(-3) - 2) + ((m.x41 - m.x60)**2 + (
    m.x120 - m.x139)**2 + (m.x199 - m.x218)**2)**(-3) * (((m.x41 - m.x60)**2 +
    (m.x120 - m.x139)**2 + (m.x199 - m.x218)**2)**(-3) - 2) + ((m.x41 - m.x61)
    **2 + (m.x120 - m.x140)**2 + (m.x199 - m.x219)**2)**(-3) * (((m.x41 - m.x61)
    **2 + (m.x120 - m.x140)**2 + (m.x199 - m.x219)**2)**(-3) - 2) + ((m.x41 -
    m.x62)**2 + (m.x120 - m.x141)**2 + (m.x199 - m.x220)**2)**(-3) * (((m.x41
    - m.x62)**2 + (m.x120 - m.x141)**2 + (m.x199 - m.x220)**2)**(-3) - 2) + ((
    m.x41 - m.x63)**2 + (m.x120 - m.x142)**2 + (m.x199 - m.x221)**2)**(-3) * ((
    (m.x41 - m.x63)**2 + (m.x120 - m.x142)**2 + (m.x199 - m.x221)**2)**(-3) - 2)
    + ((m.x41 - m.x64)**2 + (m.x120 - m.x143)**2 + (m.x199 - m.x222)**2)**(-3)
    * (((m.x41 - m.x64)**2 + (m.x120 - m.x143)**2 + (m.x199 - m.x222)**2)**(-3)
    - 2) + ((m.x41 - m.x65)**2 + (m.x120 - m.x144)**2 + (m.x199 - m.x223)**2)
    **(-3) * (((m.x41 - m.x65)**2 + (m.x120 - m.x144)**2 + (m.x199 - m.x223)**2)
    **(-3) - 2) + ((m.x41 - m.x66)**2 + (m.x120 - m.x145)**2 + (m.x199 - m.x224)
    **2)**(-3) * (((m.x41 - m.x66)**2 + (m.x120 - m.x145)**2 + (m.x199 - m.x224)
    **2)**(-3) - 2) + ((m.x41 - m.x67)**2 + (m.x120 - m.x146)**2 + (m.x199 -
    m.x225)**2)**(-3) * (((m.x41 - m.x67)**2 + (m.x120 - m.x146)**2 + (m.x199
    - m.x225)**2)**(-3) - 2) + ((m.x41 - m.x68)**2 + (m.x120 - m.x147)**2 + (
    m.x199 - m.x226)**2)**(-3) * (((m.x41 - m.x68)**2 + (m.x120 - m.x147)**2 +
    (m.x199 - m.x226)**2)**(-3) - 2) + ((m.x41 - m.x69)**2 + (m.x120 - m.x148)
    **2 + (m.x199 - m.x227)**2)**(-3) * (((m.x41 - m.x69)**2 + (m.x120 - m.x148)
    **2 + (m.x199 - m.x227)**2)**(-3) - 2) + ((m.x41 - m.x70)**2 + (m.x120 -
    m.x149)**2 + (m.x199 - m.x228)**2)**(-3) * (((m.x41 - m.x70)**2 + (m.x120
    - m.x149)**2 + (m.x199 - m.x228)**2)**(-3) - 2) + ((m.x41 - m.x71)**2 + (
    m.x120 - m.x150)**2 + (m.x199 - m.x229)**2)**(-3) * (((m.x41 - m.x71)**2 +
    (m.x120 - m.x150)**2 + (m.x199 - m.x229)**2)**(-3) - 2) + ((m.x41 - m.x72)
    **2 + (m.x120 - m.x151)**2 + (m.x199 - m.x230)**2)**(-3) * (((m.x41 - m.x72)
    **2 + (m.x120 - m.x151)**2 + (m.x199 - m.x230)**2)**(-3) - 2) + ((m.x41 -
    m.x73)**2 + (m.x120 - m.x152)**2 + (m.x199 - m.x231)**2)**(-3) * (((m.x41
    - m.x73)**2 + (m.x120 - m.x152)**2 + (m.x199 - m.x231)**2)**(-3) - 2) + ((
    m.x41 - m.x74)**2 + (m.x120 - m.x153)**2 + (m.x199 - m.x232)**2)**(-3) * ((
    (m.x41 - m.x74)**2 + (m.x120 - m.x153)**2 + (m.x199 - m.x232)**2)**(-3) - 2)
    + ((m.x41 - m.x75)**2 + (m.x120 - m.x154)**2 + (m.x199 - m.x233)**2)**(-3)
    * (((m.x41 - m.x75)**2 + (m.x120 - m.x154)**2 + (m.x199 - m.x233)**2)**(-3)
    - 2) + ((m.x41 - m.x76)**2 + (m.x120 - m.x155)**2 + (m.x199 - m.x234)**2)
    **(-3) * (((m.x41 - m.x76)**2 + (m.x120 - m.x155)**2 + (m.x199 - m.x234)**2)
    **(-3) - 2) + ((m.x41 - m.x77)**2 + (m.x120 - m.x156)**2 + (m.x199 - m.x235)
    **2)**(-3) * (((m.x41 - m.x77)**2 + (m.x120 - m.x156)**2 + (m.x199 - m.x235)
    **2)**(-3) - 2) + ((m.x41 - m.x78)**2 + (m.x120 - m.x157)**2 + (m.x199 -
    m.x236)**2)**(-3) * (((m.x41 - m.x78)**2 + (m.x120 - m.x157)**2 + (m.x199
    - m.x236)**2)**(-3) - 2) + ((m.x41 - m.x79)**2 + (m.x120 - m.x158)**2 + (
    m.x199 - m.x237)**2)**(-3) * (((m.x41 - m.x79)**2 + (m.x120 - m.x158)**2 +
    (m.x199 - m.x237)**2)**(-3) - 2) + ((m.x42 - m.x43)**2 + (m.x121 - m.x122)
    **2 + (m.x200 - m.x201)**2)**(-3) * (((m.x42 - m.x43)**2 + (m.x121 - m.x122)
    **2 + (m.x200 - m.x201)**2)**(-3) - 2) + ((m.x42 - m.x44)**2 + (m.x121 -
    m.x123)**2 + (m.x200 - m.x202)**2)**(-3) * (((m.x42 - m.x44)**2 + (m.x121
    - m.x123)**2 + (m.x200 - m.x202)**2)**(-3) - 2) + ((m.x42 - m.x45)**2 + (
    m.x121 - m.x124)**2 + (m.x200 - m.x203)**2)**(-3) * (((m.x42 - m.x45)**2 +
    (m.x121 - m.x124)**2 + (m.x200 - m.x203)**2)**(-3) - 2) + ((m.x42 - m.x46)
    **2 + (m.x121 - m.x125)**2 + (m.x200 - m.x204)**2)**(-3) * (((m.x42 - m.x46)
    **2 + (m.x121 - m.x125)**2 + (m.x200 - m.x204)**2)**(-3) - 2) + ((m.x42 -
    m.x47)**2 + (m.x121 - m.x126)**2 + (m.x200 - m.x205)**2)**(-3) * (((m.x42
    - m.x47)**2 + (m.x121 - m.x126)**2 + (m.x200 - m.x205)**2)**(-3) - 2) + ((
    m.x42 - m.x48)**2 + (m.x121 - m.x127)**2 + (m.x200 - m.x206)**2)**(-3) * ((
    (m.x42 - m.x48)**2 + (m.x121 - m.x127)**2 + (m.x200 - m.x206)**2)**(-3) - 2)
    + ((m.x42 - m.x49)**2 + (m.x121 - m.x128)**2 + (m.x200 - m.x207)**2)**(-3)
    * (((m.x42 - m.x49)**2 + (m.x121 - m.x128)**2 + (m.x200 - m.x207)**2)**(-3)
    - 2) + ((m.x42 - m.x50)**2 + (m.x121 - m.x129)**2 + (m.x200 - m.x208)**2)
    **(-3) * (((m.x42 - m.x50)**2 + (m.x121 - m.x129)**2 + (m.x200 - m.x208)**2)
    **(-3) - 2) + ((m.x42 - m.x51)**2 + (m.x121 - m.x130)**2 + (m.x200 - m.x209)
    **2)**(-3) * (((m.x42 - m.x51)**2 + (m.x121 - m.x130)**2 + (m.x200 - m.x209)
    **2)**(-3) - 2) + ((m.x42 - m.x52)**2 + (m.x121 - m.x131)**2 + (m.x200 -
    m.x210)**2)**(-3) * (((m.x42 - m.x52)**2 + (m.x121 - m.x131)**2 + (m.x200
    - m.x210)**2)**(-3) - 2) + ((m.x42 - m.x53)**2 + (m.x121 - m.x132)**2 + (
    m.x200 - m.x211)**2)**(-3) * (((m.x42 - m.x53)**2 + (m.x121 - m.x132)**2 +
    (m.x200 - m.x211)**2)**(-3) - 2) + ((m.x42 - m.x54)**2 + (m.x121 - m.x133)
    **2 + (m.x200 - m.x212)**2)**(-3) * (((m.x42 - m.x54)**2 + (m.x121 - m.x133)
    **2 + (m.x200 - m.x212)**2)**(-3) - 2) + ((m.x42 - m.x55)**2 + (m.x121 -
    m.x134)**2 + (m.x200 - m.x213)**2)**(-3) * (((m.x42 - m.x55)**2 + (m.x121
    - m.x134)**2 + (m.x200 - m.x213)**2)**(-3) - 2) + ((m.x42 - m.x56)**2 + (
    m.x121 - m.x135)**2 + (m.x200 - m.x214)**2)**(-3) * (((m.x42 - m.x56)**2 +
    (m.x121 - m.x135)**2 + (m.x200 - m.x214)**2)**(-3) - 2) + ((m.x42 - m.x57)
    **2 + (m.x121 - m.x136)**2 + (m.x200 - m.x215)**2)**(-3) * (((m.x42 - m.x57)
    **2 + (m.x121 - m.x136)**2 + (m.x200 - m.x215)**2)**(-3) - 2) + ((m.x42 -
    m.x58)**2 + (m.x121 - m.x137)**2 + (m.x200 - m.x216)**2)**(-3) * (((m.x42
    - m.x58)**2 + (m.x121 - m.x137)**2 + (m.x200 - m.x216)**2)**(-3) - 2) + ((
    m.x42 - m.x59)**2 + (m.x121 - m.x138)**2 + (m.x200 - m.x217)**2)**(-3) * ((
    (m.x42 - m.x59)**2 + (m.x121 - m.x138)**2 + (m.x200 - m.x217)**2)**(-3) - 2)
    + ((m.x42 - m.x60)**2 + (m.x121 - m.x139)**2 + (m.x200 - m.x218)**2)**(-3)
    * (((m.x42 - m.x60)**2 + (m.x121 - m.x139)**2 + (m.x200 - m.x218)**2)**(-3)
    - 2) + ((m.x42 - m.x61)**2 + (m.x121 - m.x140)**2 + (m.x200 - m.x219)**2)
    **(-3) * (((m.x42 - m.x61)**2 + (m.x121 - m.x140)**2 + (m.x200 - m.x219)**2)
    **(-3) - 2) + ((m.x42 - m.x62)**2 + (m.x121 - m.x141)**2 + (m.x200 - m.x220)
    **2)**(-3) * (((m.x42 - m.x62)**2 + (m.x121 - m.x141)**2 + (m.x200 - m.x220)
    **2)**(-3) - 2) + ((m.x42 - m.x63)**2 + (m.x121 - m.x142)**2 + (m.x200 -
    m.x221)**2)**(-3) * (((m.x42 - m.x63)**2 + (m.x121 - m.x142)**2 + (m.x200
    - m.x221)**2)**(-3) - 2) + ((m.x42 - m.x64)**2 + (m.x121 - m.x143)**2 + (
    m.x200 - m.x222)**2)**(-3) * (((m.x42 - m.x64)**2 + (m.x121 - m.x143)**2 +
    (m.x200 - m.x222)**2)**(-3) - 2) + ((m.x42 - m.x65)**2 + (m.x121 - m.x144)
    **2 + (m.x200 - m.x223)**2)**(-3) * (((m.x42 - m.x65)**2 + (m.x121 - m.x144)
    **2 + (m.x200 - m.x223)**2)**(-3) - 2) + ((m.x42 - m.x66)**2 + (m.x121 -
    m.x145)**2 + (m.x200 - m.x224)**2)**(-3) * (((m.x42 - m.x66)**2 + (m.x121
    - m.x145)**2 + (m.x200 - m.x224)**2)**(-3) - 2) + ((m.x42 - m.x67)**2 + (
    m.x121 - m.x146)**2 + (m.x200 - m.x225)**2)**(-3) * (((m.x42 - m.x67)**2 +
    (m.x121 - m.x146)**2 + (m.x200 - m.x225)**2)**(-3) - 2) + ((m.x42 - m.x68)
    **2 + (m.x121 - m.x147)**2 + (m.x200 - m.x226)**2)**(-3) * (((m.x42 - m.x68)
    **2 + (m.x121 - m.x147)**2 + (m.x200 - m.x226)**2)**(-3) - 2) + ((m.x42 -
    m.x69)**2 + (m.x121 - m.x148)**2 + (m.x200 - m.x227)**2)**(-3) * (((m.x42
    - m.x69)**2 + (m.x121 - m.x148)**2 + (m.x200 - m.x227)**2)**(-3) - 2) + ((
    m.x42 - m.x70)**2 + (m.x121 - m.x149)**2 + (m.x200 - m.x228)**2)**(-3) * ((
    (m.x42 - m.x70)**2 + (m.x121 - m.x149)**2 + (m.x200 - m.x228)**2)**(-3) - 2)
    + ((m.x42 - m.x71)**2 + (m.x121 - m.x150)**2 + (m.x200 - m.x229)**2)**(-3)
    * (((m.x42 - m.x71)**2 + (m.x121 - m.x150)**2 + (m.x200 - m.x229)**2)**(-3)
    - 2) + ((m.x42 - m.x72)**2 + (m.x121 - m.x151)**2 + (m.x200 - m.x230)**2)
    **(-3) * (((m.x42 - m.x72)**2 + (m.x121 - m.x151)**2 + (m.x200 - m.x230)**2)
    **(-3) - 2) + ((m.x42 - m.x73)**2 + (m.x121 - m.x152)**2 + (m.x200 - m.x231)
    **2)**(-3) * (((m.x42 - m.x73)**2 + (m.x121 - m.x152)**2 + (m.x200 - m.x231)
    **2)**(-3) - 2) + ((m.x42 - m.x74)**2 + (m.x121 - m.x153)**2 + (m.x200 -
    m.x232)**2)**(-3) * (((m.x42 - m.x74)**2 + (m.x121 - m.x153)**2 + (m.x200
    - m.x232)**2)**(-3) - 2) + ((m.x42 - m.x75)**2 + (m.x121 - m.x154)**2 + (
    m.x200 - m.x233)**2)**(-3) * (((m.x42 - m.x75)**2 + (m.x121 - m.x154)**2 +
    (m.x200 - m.x233)**2)**(-3) - 2) + ((m.x42 - m.x76)**2 + (m.x121 - m.x155)
    **2 + (m.x200 - m.x234)**2)**(-3) * (((m.x42 - m.x76)**2 + (m.x121 - m.x155)
    **2 + (m.x200 - m.x234)**2)**(-3) - 2) + ((m.x42 - m.x77)**2 + (m.x121 -
    m.x156)**2 + (m.x200 - m.x235)**2)**(-3) * (((m.x42 - m.x77)**2 + (m.x121
    - m.x156)**2 + (m.x200 - m.x235)**2)**(-3) - 2) + ((m.x42 - m.x78)**2 + (
    m.x121 - m.x157)**2 + (m.x200 - m.x236)**2)**(-3) * (((m.x42 - m.x78)**2 +
    (m.x121 - m.x157)**2 + (m.x200 - m.x236)**2)**(-3) - 2) + ((m.x42 - m.x79)
    **2 + (m.x121 - m.x158)**2 + (m.x200 - m.x237)**2)**(-3) * (((m.x42 - m.x79)
    **2 + (m.x121 - m.x158)**2 + (m.x200 - m.x237)**2)**(-3) - 2) + ((m.x43 -
    m.x44)**2 + (m.x122 - m.x123)**2 + (m.x201 - m.x202)**2)**(-3) * (((m.x43
    - m.x44)**2 + (m.x122 - m.x123)**2 + (m.x201 - m.x202)**2)**(-3) - 2) + ((
    m.x43 - m.x45)**2 + (m.x122 - m.x124)**2 + (m.x201 - m.x203)**2)**(-3) * ((
    (m.x43 - m.x45)**2 + (m.x122 - m.x124)**2 + (m.x201 - m.x203)**2)**(-3) - 2)
    + ((m.x43 - m.x46)**2 + (m.x122 - m.x125)**2 + (m.x201 - m.x204)**2)**(-3)
    * (((m.x43 - m.x46)**2 + (m.x122 - m.x125)**2 + (m.x201 - m.x204)**2)**(-3)
    - 2) + ((m.x43 - m.x47)**2 + (m.x122 - m.x126)**2 + (m.x201 - m.x205)**2)
    **(-3) * (((m.x43 - m.x47)**2 + (m.x122 - m.x126)**2 + (m.x201 - m.x205)**2)
    **(-3) - 2) + ((m.x43 - m.x48)**2 + (m.x122 - m.x127)**2 + (m.x201 - m.x206)
    **2)**(-3) * (((m.x43 - m.x48)**2 + (m.x122 - m.x127)**2 + (m.x201 - m.x206)
    **2)**(-3) - 2) + ((m.x43 - m.x49)**2 + (m.x122 - m.x128)**2 + (m.x201 -
    m.x207)**2)**(-3) * (((m.x43 - m.x49)**2 + (m.x122 - m.x128)**2 + (m.x201
    - m.x207)**2)**(-3) - 2) + ((m.x43 - m.x50)**2 + (m.x122 - m.x129)**2 + (
    m.x201 - m.x208)**2)**(-3) * (((m.x43 - m.x50)**2 + (m.x122 - m.x129)**2 +
    (m.x201 - m.x208)**2)**(-3) - 2) + ((m.x43 - m.x51)**2 + (m.x122 - m.x130)
    **2 + (m.x201 - m.x209)**2)**(-3) * (((m.x43 - m.x51)**2 + (m.x122 - m.x130)
    **2 + (m.x201 - m.x209)**2)**(-3) - 2) + ((m.x43 - m.x52)**2 + (m.x122 -
    m.x131)**2 + (m.x201 - m.x210)**2)**(-3) * (((m.x43 - m.x52)**2 + (m.x122
    - m.x131)**2 + (m.x201 - m.x210)**2)**(-3) - 2) + ((m.x43 - m.x53)**2 + (
    m.x122 - m.x132)**2 + (m.x201 - m.x211)**2)**(-3) * (((m.x43 - m.x53)**2 +
    (m.x122 - m.x132)**2 + (m.x201 - m.x211)**2)**(-3) - 2) + ((m.x43 - m.x54)
    **2 + (m.x122 - m.x133)**2 + (m.x201 - m.x212)**2)**(-3) * (((m.x43 - m.x54)
    **2 + (m.x122 - m.x133)**2 + (m.x201 - m.x212)**2)**(-3) - 2) + ((m.x43 -
    m.x55)**2 + (m.x122 - m.x134)**2 + (m.x201 - m.x213)**2)**(-3) * (((m.x43
    - m.x55)**2 + (m.x122 - m.x134)**2 + (m.x201 - m.x213)**2)**(-3) - 2) + ((
    m.x43 - m.x56)**2 + (m.x122 - m.x135)**2 + (m.x201 - m.x214)**2)**(-3) * ((
    (m.x43 - m.x56)**2 + (m.x122 - m.x135)**2 + (m.x201 - m.x214)**2)**(-3) - 2)
    + ((m.x43 - m.x57)**2 + (m.x122 - m.x136)**2 + (m.x201 - m.x215)**2)**(-3)
    * (((m.x43 - m.x57)**2 + (m.x122 - m.x136)**2 + (m.x201 - m.x215)**2)**(-3)
    - 2) + ((m.x43 - m.x58)**2 + (m.x122 - m.x137)**2 + (m.x201 - m.x216)**2)
    **(-3) * (((m.x43 - m.x58)**2 + (m.x122 - m.x137)**2 + (m.x201 - m.x216)**2)
    **(-3) - 2) + ((m.x43 - m.x59)**2 + (m.x122 - m.x138)**2 + (m.x201 - m.x217)
    **2)**(-3) * (((m.x43 - m.x59)**2 + (m.x122 - m.x138)**2 + (m.x201 - m.x217)
    **2)**(-3) - 2) + ((m.x43 - m.x60)**2 + (m.x122 - m.x139)**2 + (m.x201 -
    m.x218)**2)**(-3) * (((m.x43 - m.x60)**2 + (m.x122 - m.x139)**2 + (m.x201
    - m.x218)**2)**(-3) - 2) + ((m.x43 - m.x61)**2 + (m.x122 - m.x140)**2 + (
    m.x201 - m.x219)**2)**(-3) * (((m.x43 - m.x61)**2 + (m.x122 - m.x140)**2 +
    (m.x201 - m.x219)**2)**(-3) - 2) + ((m.x43 - m.x62)**2 + (m.x122 - m.x141)
    **2 + (m.x201 - m.x220)**2)**(-3) * (((m.x43 - m.x62)**2 + (m.x122 - m.x141)
    **2 + (m.x201 - m.x220)**2)**(-3) - 2) + ((m.x43 - m.x63)**2 + (m.x122 -
    m.x142)**2 + (m.x201 - m.x221)**2)**(-3) * (((m.x43 - m.x63)**2 + (m.x122
    - m.x142)**2 + (m.x201 - m.x221)**2)**(-3) - 2) + ((m.x43 - m.x64)**2 + (
    m.x122 - m.x143)**2 + (m.x201 - m.x222)**2)**(-3) * (((m.x43 - m.x64)**2 +
    (m.x122 - m.x143)**2 + (m.x201 - m.x222)**2)**(-3) - 2) + ((m.x43 - m.x65)
    **2 + (m.x122 - m.x144)**2 + (m.x201 - m.x223)**2)**(-3) * (((m.x43 - m.x65)
    **2 + (m.x122 - m.x144)**2 + (m.x201 - m.x223)**2)**(-3) - 2) + ((m.x43 -
    m.x66)**2 + (m.x122 - m.x145)**2 + (m.x201 - m.x224)**2)**(-3) * (((m.x43
    - m.x66)**2 + (m.x122 - m.x145)**2 + (m.x201 - m.x224)**2)**(-3) - 2) + ((
    m.x43 - m.x67)**2 + (m.x122 - m.x146)**2 + (m.x201 - m.x225)**2)**(-3) * ((
    (m.x43 - m.x67)**2 + (m.x122 - m.x146)**2 + (m.x201 - m.x225)**2)**(-3) - 2)
    + ((m.x43 - m.x68)**2 + (m.x122 - m.x147)**2 + (m.x201 - m.x226)**2)**(-3)
    * (((m.x43 - m.x68)**2 + (m.x122 - m.x147)**2 + (m.x201 - m.x226)**2)**(-3)
    - 2) + ((m.x43 - m.x69)**2 + (m.x122 - m.x148)**2 + (m.x201 - m.x227)**2)
    **(-3) * (((m.x43 - m.x69)**2 + (m.x122 - m.x148)**2 + (m.x201 - m.x227)**2)
    **(-3) - 2) + ((m.x43 - m.x70)**2 + (m.x122 - m.x149)**2 + (m.x201 - m.x228)
    **2)**(-3) * (((m.x43 - m.x70)**2 + (m.x122 - m.x149)**2 + (m.x201 - m.x228)
    **2)**(-3) - 2) + ((m.x43 - m.x71)**2 + (m.x122 - m.x150)**2 + (m.x201 -
    m.x229)**2)**(-3) * (((m.x43 - m.x71)**2 + (m.x122 - m.x150)**2 + (m.x201
    - m.x229)**2)**(-3) - 2) + ((m.x43 - m.x72)**2 + (m.x122 - m.x151)**2 + (
    m.x201 - m.x230)**2)**(-3) * (((m.x43 - m.x72)**2 + (m.x122 - m.x151)**2 +
    (m.x201 - m.x230)**2)**(-3) - 2) + ((m.x43 - m.x73)**2 + (m.x122 - m.x152)
    **2 + (m.x201 - m.x231)**2)**(-3) * (((m.x43 - m.x73)**2 + (m.x122 - m.x152)
    **2 + (m.x201 - m.x231)**2)**(-3) - 2) + ((m.x43 - m.x74)**2 + (m.x122 -
    m.x153)**2 + (m.x201 - m.x232)**2)**(-3) * (((m.x43 - m.x74)**2 + (m.x122
    - m.x153)**2 + (m.x201 - m.x232)**2)**(-3) - 2) + ((m.x43 - m.x75)**2 + (
    m.x122 - m.x154)**2 + (m.x201 - m.x233)**2)**(-3) * (((m.x43 - m.x75)**2 +
    (m.x122 - m.x154)**2 + (m.x201 - m.x233)**2)**(-3) - 2) + ((m.x43 - m.x76)
    **2 + (m.x122 - m.x155)**2 + (m.x201 - m.x234)**2)**(-3) * (((m.x43 - m.x76)
    **2 + (m.x122 - m.x155)**2 + (m.x201 - m.x234)**2)**(-3) - 2) + ((m.x43 -
    m.x77)**2 + (m.x122 - m.x156)**2 + (m.x201 - m.x235)**2)**(-3) * (((m.x43
    - m.x77)**2 + (m.x122 - m.x156)**2 + (m.x201 - m.x235)**2)**(-3) - 2) + ((
    m.x43 - m.x78)**2 + (m.x122 - m.x157)**2 + (m.x201 - m.x236)**2)**(-3) * ((
    (m.x43 - m.x78)**2 + (m.x122 - m.x157)**2 + (m.x201 - m.x236)**2)**(-3) - 2)
    + ((m.x43 - m.x79)**2 + (m.x122 - m.x158)**2 + (m.x201 - m.x237)**2)**(-3)
    * (((m.x43 - m.x79)**2 + (m.x122 - m.x158)**2 + (m.x201 - m.x237)**2)**(-3)
    - 2) + ((m.x44 - m.x45)**2 + (m.x123 - m.x124)**2 + (m.x202 - m.x203)**2)
    **(-3) * (((m.x44 - m.x45)**2 + (m.x123 - m.x124)**2 + (m.x202 - m.x203)**2)
    **(-3) - 2) + ((m.x44 - m.x46)**2 + (m.x123 - m.x125)**2 + (m.x202 - m.x204)
    **2)**(-3) * (((m.x44 - m.x46)**2 + (m.x123 - m.x125)**2 + (m.x202 - m.x204)
    **2)**(-3) - 2) + ((m.x44 - m.x47)**2 + (m.x123 - m.x126)**2 + (m.x202 -
    m.x205)**2)**(-3) * (((m.x44 - m.x47)**2 + (m.x123 - m.x126)**2 + (m.x202
    - m.x205)**2)**(-3) - 2) + ((m.x44 - m.x48)**2 + (m.x123 - m.x127)**2 + (
    m.x202 - m.x206)**2)**(-3) * (((m.x44 - m.x48)**2 + (m.x123 - m.x127)**2 +
    (m.x202 - m.x206)**2)**(-3) - 2) + ((m.x44 - m.x49)**2 + (m.x123 - m.x128)
    **2 + (m.x202 - m.x207)**2)**(-3) * (((m.x44 - m.x49)**2 + (m.x123 - m.x128)
    **2 + (m.x202 - m.x207)**2)**(-3) - 2) + ((m.x44 - m.x50)**2 + (m.x123 -
    m.x129)**2 + (m.x202 - m.x208)**2)**(-3) * (((m.x44 - m.x50)**2 + (m.x123
    - m.x129)**2 + (m.x202 - m.x208)**2)**(-3) - 2) + ((m.x44 - m.x51)**2 + (
    m.x123 - m.x130)**2 + (m.x202 - m.x209)**2)**(-3) * (((m.x44 - m.x51)**2 +
    (m.x123 - m.x130)**2 + (m.x202 - m.x209)**2)**(-3) - 2) + ((m.x44 - m.x52)
    **2 + (m.x123 - m.x131)**2 + (m.x202 - m.x210)**2)**(-3) * (((m.x44 - m.x52)
    **2 + (m.x123 - m.x131)**2 + (m.x202 - m.x210)**2)**(-3) - 2) + ((m.x44 -
    m.x53)**2 + (m.x123 - m.x132)**2 + (m.x202 - m.x211)**2)**(-3) * (((m.x44
    - m.x53)**2 + (m.x123 - m.x132)**2 + (m.x202 - m.x211)**2)**(-3) - 2) + ((
    m.x44 - m.x54)**2 + (m.x123 - m.x133)**2 + (m.x202 - m.x212)**2)**(-3) * ((
    (m.x44 - m.x54)**2 + (m.x123 - m.x133)**2 + (m.x202 - m.x212)**2)**(-3) - 2)
    + ((m.x44 - m.x55)**2 + (m.x123 - m.x134)**2 + (m.x202 - m.x213)**2)**(-3)
    * (((m.x44 - m.x55)**2 + (m.x123 - m.x134)**2 + (m.x202 - m.x213)**2)**(-3)
    - 2) + ((m.x44 - m.x56)**2 + (m.x123 - m.x135)**2 + (m.x202 - m.x214)**2)
    **(-3) * (((m.x44 - m.x56)**2 + (m.x123 - m.x135)**2 + (m.x202 - m.x214)**2)
    **(-3) - 2) + ((m.x44 - m.x57)**2 + (m.x123 - m.x136)**2 + (m.x202 - m.x215)
    **2)**(-3) * (((m.x44 - m.x57)**2 + (m.x123 - m.x136)**2 + (m.x202 - m.x215)
    **2)**(-3) - 2) + ((m.x44 - m.x58)**2 + (m.x123 - m.x137)**2 + (m.x202 -
    m.x216)**2)**(-3) * (((m.x44 - m.x58)**2 + (m.x123 - m.x137)**2 + (m.x202
    - m.x216)**2)**(-3) - 2) + ((m.x44 - m.x59)**2 + (m.x123 - m.x138)**2 + (
    m.x202 - m.x217)**2)**(-3) * (((m.x44 - m.x59)**2 + (m.x123 - m.x138)**2 +
    (m.x202 - m.x217)**2)**(-3) - 2) + ((m.x44 - m.x60)**2 + (m.x123 - m.x139)
    **2 + (m.x202 - m.x218)**2)**(-3) * (((m.x44 - m.x60)**2 + (m.x123 - m.x139)
    **2 + (m.x202 - m.x218)**2)**(-3) - 2) + ((m.x44 - m.x61)**2 + (m.x123 -
    m.x140)**2 + (m.x202 - m.x219)**2)**(-3) * (((m.x44 - m.x61)**2 + (m.x123
    - m.x140)**2 + (m.x202 - m.x219)**2)**(-3) - 2) + ((m.x44 - m.x62)**2 + (
    m.x123 - m.x141)**2 + (m.x202 - m.x220)**2)**(-3) * (((m.x44 - m.x62)**2 +
    (m.x123 - m.x141)**2 + (m.x202 - m.x220)**2)**(-3) - 2) + ((m.x44 - m.x63)
    **2 + (m.x123 - m.x142)**2 + (m.x202 - m.x221)**2)**(-3) * (((m.x44 - m.x63)
    **2 + (m.x123 - m.x142)**2 + (m.x202 - m.x221)**2)**(-3) - 2) + ((m.x44 -
    m.x64)**2 + (m.x123 - m.x143)**2 + (m.x202 - m.x222)**2)**(-3) * (((m.x44
    - m.x64)**2 + (m.x123 - m.x143)**2 + (m.x202 - m.x222)**2)**(-3) - 2) + ((
    m.x44 - m.x65)**2 + (m.x123 - m.x144)**2 + (m.x202 - m.x223)**2)**(-3) * ((
    (m.x44 - m.x65)**2 + (m.x123 - m.x144)**2 + (m.x202 - m.x223)**2)**(-3) - 2)
    + ((m.x44 - m.x66)**2 + (m.x123 - m.x145)**2 + (m.x202 - m.x224)**2)**(-3)
    * (((m.x44 - m.x66)**2 + (m.x123 - m.x145)**2 + (m.x202 - m.x224)**2)**(-3)
    - 2) + ((m.x44 - m.x67)**2 + (m.x123 - m.x146)**2 + (m.x202 - m.x225)**2)
    **(-3) * (((m.x44 - m.x67)**2 + (m.x123 - m.x146)**2 + (m.x202 - m.x225)**2)
    **(-3) - 2) + ((m.x44 - m.x68)**2 + (m.x123 - m.x147)**2 + (m.x202 - m.x226)
    **2)**(-3) * (((m.x44 - m.x68)**2 + (m.x123 - m.x147)**2 + (m.x202 - m.x226)
    **2)**(-3) - 2) + ((m.x44 - m.x69)**2 + (m.x123 - m.x148)**2 + (m.x202 -
    m.x227)**2)**(-3) * (((m.x44 - m.x69)**2 + (m.x123 - m.x148)**2 + (m.x202
    - m.x227)**2)**(-3) - 2) + ((m.x44 - m.x70)**2 + (m.x123 - m.x149)**2 + (
    m.x202 - m.x228)**2)**(-3) * (((m.x44 - m.x70)**2 + (m.x123 - m.x149)**2 +
    (m.x202 - m.x228)**2)**(-3) - 2) + ((m.x44 - m.x71)**2 + (m.x123 - m.x150)
    **2 + (m.x202 - m.x229)**2)**(-3) * (((m.x44 - m.x71)**2 + (m.x123 - m.x150)
    **2 + (m.x202 - m.x229)**2)**(-3) - 2) + ((m.x44 - m.x72)**2 + (m.x123 -
    m.x151)**2 + (m.x202 - m.x230)**2)**(-3) * (((m.x44 - m.x72)**2 + (m.x123
    - m.x151)**2 + (m.x202 - m.x230)**2)**(-3) - 2) + ((m.x44 - m.x73)**2 + (
    m.x123 - m.x152)**2 + (m.x202 - m.x231)**2)**(-3) * (((m.x44 - m.x73)**2 +
    (m.x123 - m.x152)**2 + (m.x202 - m.x231)**2)**(-3) - 2) + ((m.x44 - m.x74)
    **2 + (m.x123 - m.x153)**2 + (m.x202 - m.x232)**2)**(-3) * (((m.x44 - m.x74)
    **2 + (m.x123 - m.x153)**2 + (m.x202 - m.x232)**2)**(-3) - 2) + ((m.x44 -
    m.x75)**2 + (m.x123 - m.x154)**2 + (m.x202 - m.x233)**2)**(-3) * (((m.x44
    - m.x75)**2 + (m.x123 - m.x154)**2 + (m.x202 - m.x233)**2)**(-3) - 2) + ((
    m.x44 - m.x76)**2 + (m.x123 - m.x155)**2 + (m.x202 - m.x234)**2)**(-3) * ((
    (m.x44 - m.x76)**2 + (m.x123 - m.x155)**2 + (m.x202 - m.x234)**2)**(-3) - 2)
    + ((m.x44 - m.x77)**2 + (m.x123 - m.x156)**2 + (m.x202 - m.x235)**2)**(-3)
    * (((m.x44 - m.x77)**2 + (m.x123 - m.x156)**2 + (m.x202 - m.x235)**2)**(-3)
    - 2) + ((m.x44 - m.x78)**2 + (m.x123 - m.x157)**2 + (m.x202 - m.x236)**2)
    **(-3) * (((m.x44 - m.x78)**2 + (m.x123 - m.x157)**2 + (m.x202 - m.x236)**2)
    **(-3) - 2) + ((m.x44 - m.x79)**2 + (m.x123 - m.x158)**2 + (m.x202 - m.x237)
    **2)**(-3) * (((m.x44 - m.x79)**2 + (m.x123 - m.x158)**2 + (m.x202 - m.x237)
    **2)**(-3) - 2) + ((m.x45 - m.x46)**2 + (m.x124 - m.x125)**2 + (m.x203 -
    m.x204)**2)**(-3) * (((m.x45 - m.x46)**2 + (m.x124 - m.x125)**2 + (m.x203
    - m.x204)**2)**(-3) - 2) + ((m.x45 - m.x47)**2 + (m.x124 - m.x126)**2 + (
    m.x203 - m.x205)**2)**(-3) * (((m.x45 - m.x47)**2 + (m.x124 - m.x126)**2 +
    (m.x203 - m.x205)**2)**(-3) - 2) + ((m.x45 - m.x48)**2 + (m.x124 - m.x127)
    **2 + (m.x203 - m.x206)**2)**(-3) * (((m.x45 - m.x48)**2 + (m.x124 - m.x127)
    **2 + (m.x203 - m.x206)**2)**(-3) - 2) + ((m.x45 - m.x49)**2 + (m.x124 -
    m.x128)**2 + (m.x203 - m.x207)**2)**(-3) * (((m.x45 - m.x49)**2 + (m.x124
    - m.x128)**2 + (m.x203 - m.x207)**2)**(-3) - 2) + ((m.x45 - m.x50)**2 + (
    m.x124 - m.x129)**2 + (m.x203 - m.x208)**2)**(-3) * (((m.x45 - m.x50)**2 +
    (m.x124 - m.x129)**2 + (m.x203 - m.x208)**2)**(-3) - 2) + ((m.x45 - m.x51)
    **2 + (m.x124 - m.x130)**2 + (m.x203 - m.x209)**2)**(-3) * (((m.x45 - m.x51)
    **2 + (m.x124 - m.x130)**2 + (m.x203 - m.x209)**2)**(-3) - 2) + ((m.x45 -
    m.x52)**2 + (m.x124 - m.x131)**2 + (m.x203 - m.x210)**2)**(-3) * (((m.x45
    - m.x52)**2 + (m.x124 - m.x131)**2 + (m.x203 - m.x210)**2)**(-3) - 2) + ((
    m.x45 - m.x53)**2 + (m.x124 - m.x132)**2 + (m.x203 - m.x211)**2)**(-3) * ((
    (m.x45 - m.x53)**2 + (m.x124 - m.x132)**2 + (m.x203 - m.x211)**2)**(-3) - 2)
    + ((m.x45 - m.x54)**2 + (m.x124 - m.x133)**2 + (m.x203 - m.x212)**2)**(-3)
    * (((m.x45 - m.x54)**2 + (m.x124 - m.x133)**2 + (m.x203 - m.x212)**2)**(-3)
    - 2) + ((m.x45 - m.x55)**2 + (m.x124 - m.x134)**2 + (m.x203 - m.x213)**2)
    **(-3) * (((m.x45 - m.x55)**2 + (m.x124 - m.x134)**2 + (m.x203 - m.x213)**2)
    **(-3) - 2) + ((m.x45 - m.x56)**2 + (m.x124 - m.x135)**2 + (m.x203 - m.x214)
    **2)**(-3) * (((m.x45 - m.x56)**2 + (m.x124 - m.x135)**2 + (m.x203 - m.x214)
    **2)**(-3) - 2) + ((m.x45 - m.x57)**2 + (m.x124 - m.x136)**2 + (m.x203 -
    m.x215)**2)**(-3) * (((m.x45 - m.x57)**2 + (m.x124 - m.x136)**2 + (m.x203
    - m.x215)**2)**(-3) - 2) + ((m.x45 - m.x58)**2 + (m.x124 - m.x137)**2 + (
    m.x203 - m.x216)**2)**(-3) * (((m.x45 - m.x58)**2 + (m.x124 - m.x137)**2 +
    (m.x203 - m.x216)**2)**(-3) - 2) + ((m.x45 - m.x59)**2 + (m.x124 - m.x138)
    **2 + (m.x203 - m.x217)**2)**(-3) * (((m.x45 - m.x59)**2 + (m.x124 - m.x138)
    **2 + (m.x203 - m.x217)**2)**(-3) - 2) + ((m.x45 - m.x60)**2 + (m.x124 -
    m.x139)**2 + (m.x203 - m.x218)**2)**(-3) * (((m.x45 - m.x60)**2 + (m.x124
    - m.x139)**2 + (m.x203 - m.x218)**2)**(-3) - 2) + ((m.x45 - m.x61)**2 + (
    m.x124 - m.x140)**2 + (m.x203 - m.x219)**2)**(-3) * (((m.x45 - m.x61)**2 +
    (m.x124 - m.x140)**2 + (m.x203 - m.x219)**2)**(-3) - 2) + ((m.x45 - m.x62)
    **2 + (m.x124 - m.x141)**2 + (m.x203 - m.x220)**2)**(-3) * (((m.x45 - m.x62)
    **2 + (m.x124 - m.x141)**2 + (m.x203 - m.x220)**2)**(-3) - 2) + ((m.x45 -
    m.x63)**2 + (m.x124 - m.x142)**2 + (m.x203 - m.x221)**2)**(-3) * (((m.x45
    - m.x63)**2 + (m.x124 - m.x142)**2 + (m.x203 - m.x221)**2)**(-3) - 2) + ((
    m.x45 - m.x64)**2 + (m.x124 - m.x143)**2 + (m.x203 - m.x222)**2)**(-3) * ((
    (m.x45 - m.x64)**2 + (m.x124 - m.x143)**2 + (m.x203 - m.x222)**2)**(-3) - 2)
    + ((m.x45 - m.x65)**2 + (m.x124 - m.x144)**2 + (m.x203 - m.x223)**2)**(-3)
    * (((m.x45 - m.x65)**2 + (m.x124 - m.x144)**2 + (m.x203 - m.x223)**2)**(-3)
    - 2) + ((m.x45 - m.x66)**2 + (m.x124 - m.x145)**2 + (m.x203 - m.x224)**2)
    **(-3) * (((m.x45 - m.x66)**2 + (m.x124 - m.x145)**2 + (m.x203 - m.x224)**2)
    **(-3) - 2) + ((m.x45 - m.x67)**2 + (m.x124 - m.x146)**2 + (m.x203 - m.x225)
    **2)**(-3) * (((m.x45 - m.x67)**2 + (m.x124 - m.x146)**2 + (m.x203 - m.x225)
    **2)**(-3) - 2) + ((m.x45 - m.x68)**2 + (m.x124 - m.x147)**2 + (m.x203 -
    m.x226)**2)**(-3) * (((m.x45 - m.x68)**2 + (m.x124 - m.x147)**2 + (m.x203
    - m.x226)**2)**(-3) - 2) + ((m.x45 - m.x69)**2 + (m.x124 - m.x148)**2 + (
    m.x203 - m.x227)**2)**(-3) * (((m.x45 - m.x69)**2 + (m.x124 - m.x148)**2 +
    (m.x203 - m.x227)**2)**(-3) - 2) + ((m.x45 - m.x70)**2 + (m.x124 - m.x149)
    **2 + (m.x203 - m.x228)**2)**(-3) * (((m.x45 - m.x70)**2 + (m.x124 - m.x149)
    **2 + (m.x203 - m.x228)**2)**(-3) - 2) + ((m.x45 - m.x71)**2 + (m.x124 -
    m.x150)**2 + (m.x203 - m.x229)**2)**(-3) * (((m.x45 - m.x71)**2 + (m.x124
    - m.x150)**2 + (m.x203 - m.x229)**2)**(-3) - 2) + ((m.x45 - m.x72)**2 + (
    m.x124 - m.x151)**2 + (m.x203 - m.x230)**2)**(-3) * (((m.x45 - m.x72)**2 +
    (m.x124 - m.x151)**2 + (m.x203 - m.x230)**2)**(-3) - 2) + ((m.x45 - m.x73)
    **2 + (m.x124 - m.x152)**2 + (m.x203 - m.x231)**2)**(-3) * (((m.x45 - m.x73)
    **2 + (m.x124 - m.x152)**2 + (m.x203 - m.x231)**2)**(-3) - 2) + ((m.x45 -
    m.x74)**2 + (m.x124 - m.x153)**2 + (m.x203 - m.x232)**2)**(-3) * (((m.x45
    - m.x74)**2 + (m.x124 - m.x153)**2 + (m.x203 - m.x232)**2)**(-3) - 2) + ((
    m.x45 - m.x75)**2 + (m.x124 - m.x154)**2 + (m.x203 - m.x233)**2)**(-3) * ((
    (m.x45 - m.x75)**2 + (m.x124 - m.x154)**2 + (m.x203 - m.x233)**2)**(-3) - 2)
    + ((m.x45 - m.x76)**2 + (m.x124 - m.x155)**2 + (m.x203 - m.x234)**2)**(-3)
    * (((m.x45 - m.x76)**2 + (m.x124 - m.x155)**2 + (m.x203 - m.x234)**2)**(-3)
    - 2) + ((m.x45 - m.x77)**2 + (m.x124 - m.x156)**2 + (m.x203 - m.x235)**2)
    **(-3) * (((m.x45 - m.x77)**2 + (m.x124 - m.x156)**2 + (m.x203 - m.x235)**2)
    **(-3) - 2) + ((m.x45 - m.x78)**2 + (m.x124 - m.x157)**2 + (m.x203 - m.x236)
    **2)**(-3) * (((m.x45 - m.x78)**2 + (m.x124 - m.x157)**2 + (m.x203 - m.x236)
    **2)**(-3) - 2) + ((m.x45 - m.x79)**2 + (m.x124 - m.x158)**2 + (m.x203 -
    m.x237)**2)**(-3) * (((m.x45 - m.x79)**2 + (m.x124 - m.x158)**2 + (m.x203
    - m.x237)**2)**(-3) - 2) + ((m.x46 - m.x47)**2 + (m.x125 - m.x126)**2 + (
    m.x204 - m.x205)**2)**(-3) * (((m.x46 - m.x47)**2 + (m.x125 - m.x126)**2 +
    (m.x204 - m.x205)**2)**(-3) - 2) + ((m.x46 - m.x48)**2 + (m.x125 - m.x127)
    **2 + (m.x204 - m.x206)**2)**(-3) * (((m.x46 - m.x48)**2 + (m.x125 - m.x127)
    **2 + (m.x204 - m.x206)**2)**(-3) - 2) + ((m.x46 - m.x49)**2 + (m.x125 -
    m.x128)**2 + (m.x204 - m.x207)**2)**(-3) * (((m.x46 - m.x49)**2 + (m.x125
    - m.x128)**2 + (m.x204 - m.x207)**2)**(-3) - 2) + ((m.x46 - m.x50)**2 + (
    m.x125 - m.x129)**2 + (m.x204 - m.x208)**2)**(-3) * (((m.x46 - m.x50)**2 +
    (m.x125 - m.x129)**2 + (m.x204 - m.x208)**2)**(-3) - 2) + ((m.x46 - m.x51)
    **2 + (m.x125 - m.x130)**2 + (m.x204 - m.x209)**2)**(-3) * (((m.x46 - m.x51)
    **2 + (m.x125 - m.x130)**2 + (m.x204 - m.x209)**2)**(-3) - 2) + ((m.x46 -
    m.x52)**2 + (m.x125 - m.x131)**2 + (m.x204 - m.x210)**2)**(-3) * (((m.x46
    - m.x52)**2 + (m.x125 - m.x131)**2 + (m.x204 - m.x210)**2)**(-3) - 2) + ((
    m.x46 - m.x53)**2 + (m.x125 - m.x132)**2 + (m.x204 - m.x211)**2)**(-3) * ((
    (m.x46 - m.x53)**2 + (m.x125 - m.x132)**2 + (m.x204 - m.x211)**2)**(-3) - 2)
    + ((m.x46 - m.x54)**2 + (m.x125 - m.x133)**2 + (m.x204 - m.x212)**2)**(-3)
    * (((m.x46 - m.x54)**2 + (m.x125 - m.x133)**2 + (m.x204 - m.x212)**2)**(-3)
    - 2) + ((m.x46 - m.x55)**2 + (m.x125 - m.x134)**2 + (m.x204 - m.x213)**2)
    **(-3) * (((m.x46 - m.x55)**2 + (m.x125 - m.x134)**2 + (m.x204 - m.x213)**2)
    **(-3) - 2) + ((m.x46 - m.x56)**2 + (m.x125 - m.x135)**2 + (m.x204 - m.x214)
    **2)**(-3) * (((m.x46 - m.x56)**2 + (m.x125 - m.x135)**2 + (m.x204 - m.x214)
    **2)**(-3) - 2) + ((m.x46 - m.x57)**2 + (m.x125 - m.x136)**2 + (m.x204 -
    m.x215)**2)**(-3) * (((m.x46 - m.x57)**2 + (m.x125 - m.x136)**2 + (m.x204
    - m.x215)**2)**(-3) - 2) + ((m.x46 - m.x58)**2 + (m.x125 - m.x137)**2 + (
    m.x204 - m.x216)**2)**(-3) * (((m.x46 - m.x58)**2 + (m.x125 - m.x137)**2 +
    (m.x204 - m.x216)**2)**(-3) - 2) + ((m.x46 - m.x59)**2 + (m.x125 - m.x138)
    **2 + (m.x204 - m.x217)**2)**(-3) * (((m.x46 - m.x59)**2 + (m.x125 - m.x138)
    **2 + (m.x204 - m.x217)**2)**(-3) - 2) + ((m.x46 - m.x60)**2 + (m.x125 -
    m.x139)**2 + (m.x204 - m.x218)**2)**(-3) * (((m.x46 - m.x60)**2 + (m.x125
    - m.x139)**2 + (m.x204 - m.x218)**2)**(-3) - 2) + ((m.x46 - m.x61)**2 + (
    m.x125 - m.x140)**2 + (m.x204 - m.x219)**2)**(-3) * (((m.x46 - m.x61)**2 +
    (m.x125 - m.x140)**2 + (m.x204 - m.x219)**2)**(-3) - 2) + ((m.x46 - m.x62)
    **2 + (m.x125 - m.x141)**2 + (m.x204 - m.x220)**2)**(-3) * (((m.x46 - m.x62)
    **2 + (m.x125 - m.x141)**2 + (m.x204 - m.x220)**2)**(-3) - 2) + ((m.x46 -
    m.x63)**2 + (m.x125 - m.x142)**2 + (m.x204 - m.x221)**2)**(-3) * (((m.x46
    - m.x63)**2 + (m.x125 - m.x142)**2 + (m.x204 - m.x221)**2)**(-3) - 2) + ((
    m.x46 - m.x64)**2 + (m.x125 - m.x143)**2 + (m.x204 - m.x222)**2)**(-3) * ((
    (m.x46 - m.x64)**2 + (m.x125 - m.x143)**2 + (m.x204 - m.x222)**2)**(-3) - 2)
    + ((m.x46 - m.x65)**2 + (m.x125 - m.x144)**2 + (m.x204 - m.x223)**2)**(-3)
    * (((m.x46 - m.x65)**2 + (m.x125 - m.x144)**2 + (m.x204 - m.x223)**2)**(-3)
    - 2) + ((m.x46 - m.x66)**2 + (m.x125 - m.x145)**2 + (m.x204 - m.x224)**2)
    **(-3) * (((m.x46 - m.x66)**2 + (m.x125 - m.x145)**2 + (m.x204 - m.x224)**2)
    **(-3) - 2) + ((m.x46 - m.x67)**2 + (m.x125 - m.x146)**2 + (m.x204 - m.x225)
    **2)**(-3) * (((m.x46 - m.x67)**2 + (m.x125 - m.x146)**2 + (m.x204 - m.x225)
    **2)**(-3) - 2) + ((m.x46 - m.x68)**2 + (m.x125 - m.x147)**2 + (m.x204 -
    m.x226)**2)**(-3) * (((m.x46 - m.x68)**2 + (m.x125 - m.x147)**2 + (m.x204
    - m.x226)**2)**(-3) - 2) + ((m.x46 - m.x69)**2 + (m.x125 - m.x148)**2 + (
    m.x204 - m.x227)**2)**(-3) * (((m.x46 - m.x69)**2 + (m.x125 - m.x148)**2 +
    (m.x204 - m.x227)**2)**(-3) - 2) + ((m.x46 - m.x70)**2 + (m.x125 - m.x149)
    **2 + (m.x204 - m.x228)**2)**(-3) * (((m.x46 - m.x70)**2 + (m.x125 - m.x149)
    **2 + (m.x204 - m.x228)**2)**(-3) - 2) + ((m.x46 - m.x71)**2 + (m.x125 -
    m.x150)**2 + (m.x204 - m.x229)**2)**(-3) * (((m.x46 - m.x71)**2 + (m.x125
    - m.x150)**2 + (m.x204 - m.x229)**2)**(-3) - 2) + ((m.x46 - m.x72)**2 + (
    m.x125 - m.x151)**2 + (m.x204 - m.x230)**2)**(-3) * (((m.x46 - m.x72)**2 +
    (m.x125 - m.x151)**2 + (m.x204 - m.x230)**2)**(-3) - 2) + ((m.x46 - m.x73)
    **2 + (m.x125 - m.x152)**2 + (m.x204 - m.x231)**2)**(-3) * (((m.x46 - m.x73)
    **2 + (m.x125 - m.x152)**2 + (m.x204 - m.x231)**2)**(-3) - 2) + ((m.x46 -
    m.x74)**2 + (m.x125 - m.x153)**2 + (m.x204 - m.x232)**2)**(-3) * (((m.x46
    - m.x74)**2 + (m.x125 - m.x153)**2 + (m.x204 - m.x232)**2)**(-3) - 2) + ((
    m.x46 - m.x75)**2 + (m.x125 - m.x154)**2 + (m.x204 - m.x233)**2)**(-3) * ((
    (m.x46 - m.x75)**2 + (m.x125 - m.x154)**2 + (m.x204 - m.x233)**2)**(-3) - 2)
    + ((m.x46 - m.x76)**2 + (m.x125 - m.x155)**2 + (m.x204 - m.x234)**2)**(-3)
    * (((m.x46 - m.x76)**2 + (m.x125 - m.x155)**2 + (m.x204 - m.x234)**2)**(-3)
    - 2) + ((m.x46 - m.x77)**2 + (m.x125 - m.x156)**2 + (m.x204 - m.x235)**2)
    **(-3) * (((m.x46 - m.x77)**2 + (m.x125 - m.x156)**2 + (m.x204 - m.x235)**2)
    **(-3) - 2) + ((m.x46 - m.x78)**2 + (m.x125 - m.x157)**2 + (m.x204 - m.x236)
    **2)**(-3) * (((m.x46 - m.x78)**2 + (m.x125 - m.x157)**2 + (m.x204 - m.x236)
    **2)**(-3) - 2) + ((m.x46 - m.x79)**2 + (m.x125 - m.x158)**2 + (m.x204 -
    m.x237)**2)**(-3) * (((m.x46 - m.x79)**2 + (m.x125 - m.x158)**2 + (m.x204
    - m.x237)**2)**(-3) - 2) + ((m.x47 - m.x48)**2 + (m.x126 - m.x127)**2 + (
    m.x205 - m.x206)**2)**(-3) * (((m.x47 - m.x48)**2 + (m.x126 - m.x127)**2 +
    (m.x205 - m.x206)**2)**(-3) - 2) + ((m.x47 - m.x49)**2 + (m.x126 - m.x128)
    **2 + (m.x205 - m.x207)**2)**(-3) * (((m.x47 - m.x49)**2 + (m.x126 - m.x128)
    **2 + (m.x205 - m.x207)**2)**(-3) - 2) + ((m.x47 - m.x50)**2 + (m.x126 -
    m.x129)**2 + (m.x205 - m.x208)**2)**(-3) * (((m.x47 - m.x50)**2 + (m.x126
    - m.x129)**2 + (m.x205 - m.x208)**2)**(-3) - 2) + ((m.x47 - m.x51)**2 + (
    m.x126 - m.x130)**2 + (m.x205 - m.x209)**2)**(-3) * (((m.x47 - m.x51)**2 +
    (m.x126 - m.x130)**2 + (m.x205 - m.x209)**2)**(-3) - 2) + ((m.x47 - m.x52)
    **2 + (m.x126 - m.x131)**2 + (m.x205 - m.x210)**2)**(-3) * (((m.x47 - m.x52)
    **2 + (m.x126 - m.x131)**2 + (m.x205 - m.x210)**2)**(-3) - 2) + ((m.x47 -
    m.x53)**2 + (m.x126 - m.x132)**2 + (m.x205 - m.x211)**2)**(-3) * (((m.x47
    - m.x53)**2 + (m.x126 - m.x132)**2 + (m.x205 - m.x211)**2)**(-3) - 2) + ((
    m.x47 - m.x54)**2 + (m.x126 - m.x133)**2 + (m.x205 - m.x212)**2)**(-3) * ((
    (m.x47 - m.x54)**2 + (m.x126 - m.x133)**2 + (m.x205 - m.x212)**2)**(-3) - 2)
    + ((m.x47 - m.x55)**2 + (m.x126 - m.x134)**2 + (m.x205 - m.x213)**2)**(-3)
    * (((m.x47 - m.x55)**2 + (m.x126 - m.x134)**2 + (m.x205 - m.x213)**2)**(-3)
    - 2) + ((m.x47 - m.x56)**2 + (m.x126 - m.x135)**2 + (m.x205 - m.x214)**2)
    **(-3) * (((m.x47 - m.x56)**2 + (m.x126 - m.x135)**2 + (m.x205 - m.x214)**2)
    **(-3) - 2) + ((m.x47 - m.x57)**2 + (m.x126 - m.x136)**2 + (m.x205 - m.x215)
    **2)**(-3) * (((m.x47 - m.x57)**2 + (m.x126 - m.x136)**2 + (m.x205 - m.x215)
    **2)**(-3) - 2) + ((m.x47 - m.x58)**2 + (m.x126 - m.x137)**2 + (m.x205 -
    m.x216)**2)**(-3) * (((m.x47 - m.x58)**2 + (m.x126 - m.x137)**2 + (m.x205
    - m.x216)**2)**(-3) - 2) + ((m.x47 - m.x59)**2 + (m.x126 - m.x138)**2 + (
    m.x205 - m.x217)**2)**(-3) * (((m.x47 - m.x59)**2 + (m.x126 - m.x138)**2 +
    (m.x205 - m.x217)**2)**(-3) - 2) + ((m.x47 - m.x60)**2 + (m.x126 - m.x139)
    **2 + (m.x205 - m.x218)**2)**(-3) * (((m.x47 - m.x60)**2 + (m.x126 - m.x139)
    **2 + (m.x205 - m.x218)**2)**(-3) - 2) + ((m.x47 - m.x61)**2 + (m.x126 -
    m.x140)**2 + (m.x205 - m.x219)**2)**(-3) * (((m.x47 - m.x61)**2 + (m.x126
    - m.x140)**2 + (m.x205 - m.x219)**2)**(-3) - 2) + ((m.x47 - m.x62)**2 + (
    m.x126 - m.x141)**2 + (m.x205 - m.x220)**2)**(-3) * (((m.x47 - m.x62)**2 +
    (m.x126 - m.x141)**2 + (m.x205 - m.x220)**2)**(-3) - 2) + ((m.x47 - m.x63)
    **2 + (m.x126 - m.x142)**2 + (m.x205 - m.x221)**2)**(-3) * (((m.x47 - m.x63)
    **2 + (m.x126 - m.x142)**2 + (m.x205 - m.x221)**2)**(-3) - 2) + ((m.x47 -
    m.x64)**2 + (m.x126 - m.x143)**2 + (m.x205 - m.x222)**2)**(-3) * (((m.x47
    - m.x64)**2 + (m.x126 - m.x143)**2 + (m.x205 - m.x222)**2)**(-3) - 2) + ((
    m.x47 - m.x65)**2 + (m.x126 - m.x144)**2 + (m.x205 - m.x223)**2)**(-3) * ((
    (m.x47 - m.x65)**2 + (m.x126 - m.x144)**2 + (m.x205 - m.x223)**2)**(-3) - 2)
    + ((m.x47 - m.x66)**2 + (m.x126 - m.x145)**2 + (m.x205 - m.x224)**2)**(-3)
    * (((m.x47 - m.x66)**2 + (m.x126 - m.x145)**2 + (m.x205 - m.x224)**2)**(-3)
    - 2) + ((m.x47 - m.x67)**2 + (m.x126 - m.x146)**2 + (m.x205 - m.x225)**2)
    **(-3) * (((m.x47 - m.x67)**2 + (m.x126 - m.x146)**2 + (m.x205 - m.x225)**2)
    **(-3) - 2) + ((m.x47 - m.x68)**2 + (m.x126 - m.x147)**2 + (m.x205 - m.x226)
    **2)**(-3) * (((m.x47 - m.x68)**2 + (m.x126 - m.x147)**2 + (m.x205 - m.x226)
    **2)**(-3) - 2) + ((m.x47 - m.x69)**2 + (m.x126 - m.x148)**2 + (m.x205 -
    m.x227)**2)**(-3) * (((m.x47 - m.x69)**2 + (m.x126 - m.x148)**2 + (m.x205
    - m.x227)**2)**(-3) - 2) + ((m.x47 - m.x70)**2 + (m.x126 - m.x149)**2 + (
    m.x205 - m.x228)**2)**(-3) * (((m.x47 - m.x70)**2 + (m.x126 - m.x149)**2 +
    (m.x205 - m.x228)**2)**(-3) - 2) + ((m.x47 - m.x71)**2 + (m.x126 - m.x150)
    **2 + (m.x205 - m.x229)**2)**(-3) * (((m.x47 - m.x71)**2 + (m.x126 - m.x150)
    **2 + (m.x205 - m.x229)**2)**(-3) - 2) + ((m.x47 - m.x72)**2 + (m.x126 -
    m.x151)**2 + (m.x205 - m.x230)**2)**(-3) * (((m.x47 - m.x72)**2 + (m.x126
    - m.x151)**2 + (m.x205 - m.x230)**2)**(-3) - 2) + ((m.x47 - m.x73)**2 + (
    m.x126 - m.x152)**2 + (m.x205 - m.x231)**2)**(-3) * (((m.x47 - m.x73)**2 +
    (m.x126 - m.x152)**2 + (m.x205 - m.x231)**2)**(-3) - 2) + ((m.x47 - m.x74)
    **2 + (m.x126 - m.x153)**2 + (m.x205 - m.x232)**2)**(-3) * (((m.x47 - m.x74)
    **2 + (m.x126 - m.x153)**2 + (m.x205 - m.x232)**2)**(-3) - 2) + ((m.x47 -
    m.x75)**2 + (m.x126 - m.x154)**2 + (m.x205 - m.x233)**2)**(-3) * (((m.x47
    - m.x75)**2 + (m.x126 - m.x154)**2 + (m.x205 - m.x233)**2)**(-3) - 2) + ((
    m.x47 - m.x76)**2 + (m.x126 - m.x155)**2 + (m.x205 - m.x234)**2)**(-3) * ((
    (m.x47 - m.x76)**2 + (m.x126 - m.x155)**2 + (m.x205 - m.x234)**2)**(-3) - 2)
    + ((m.x47 - m.x77)**2 + (m.x126 - m.x156)**2 + (m.x205 - m.x235)**2)**(-3)
    * (((m.x47 - m.x77)**2 + (m.x126 - m.x156)**2 + (m.x205 - m.x235)**2)**(-3)
    - 2) + ((m.x47 - m.x78)**2 + (m.x126 - m.x157)**2 + (m.x205 - m.x236)**2)
    **(-3) * (((m.x47 - m.x78)**2 + (m.x126 - m.x157)**2 + (m.x205 - m.x236)**2)
    **(-3) - 2) + ((m.x47 - m.x79)**2 + (m.x126 - m.x158)**2 + (m.x205 - m.x237)
    **2)**(-3) * (((m.x47 - m.x79)**2 + (m.x126 - m.x158)**2 + (m.x205 - m.x237)
    **2)**(-3) - 2) + ((m.x48 - m.x49)**2 + (m.x127 - m.x128)**2 + (m.x206 -
    m.x207)**2)**(-3) * (((m.x48 - m.x49)**2 + (m.x127 - m.x128)**2 + (m.x206
    - m.x207)**2)**(-3) - 2) + ((m.x48 - m.x50)**2 + (m.x127 - m.x129)**2 + (
    m.x206 - m.x208)**2)**(-3) * (((m.x48 - m.x50)**2 + (m.x127 - m.x129)**2 +
    (m.x206 - m.x208)**2)**(-3) - 2) + ((m.x48 - m.x51)**2 + (m.x127 - m.x130)
    **2 + (m.x206 - m.x209)**2)**(-3) * (((m.x48 - m.x51)**2 + (m.x127 - m.x130)
    **2 + (m.x206 - m.x209)**2)**(-3) - 2) + ((m.x48 - m.x52)**2 + (m.x127 -
    m.x131)**2 + (m.x206 - m.x210)**2)**(-3) * (((m.x48 - m.x52)**2 + (m.x127
    - m.x131)**2 + (m.x206 - m.x210)**2)**(-3) - 2) + ((m.x48 - m.x53)**2 + (
    m.x127 - m.x132)**2 + (m.x206 - m.x211)**2)**(-3) * (((m.x48 - m.x53)**2 +
    (m.x127 - m.x132)**2 + (m.x206 - m.x211)**2)**(-3) - 2) + ((m.x48 - m.x54)
    **2 + (m.x127 - m.x133)**2 + (m.x206 - m.x212)**2)**(-3) * (((m.x48 - m.x54)
    **2 + (m.x127 - m.x133)**2 + (m.x206 - m.x212)**2)**(-3) - 2) + ((m.x48 -
    m.x55)**2 + (m.x127 - m.x134)**2 + (m.x206 - m.x213)**2)**(-3) * (((m.x48
    - m.x55)**2 + (m.x127 - m.x134)**2 + (m.x206 - m.x213)**2)**(-3) - 2) + ((
    m.x48 - m.x56)**2 + (m.x127 - m.x135)**2 + (m.x206 - m.x214)**2)**(-3) * ((
    (m.x48 - m.x56)**2 + (m.x127 - m.x135)**2 + (m.x206 - m.x214)**2)**(-3) - 2)
    + ((m.x48 - m.x57)**2 + (m.x127 - m.x136)**2 + (m.x206 - m.x215)**2)**(-3)
    * (((m.x48 - m.x57)**2 + (m.x127 - m.x136)**2 + (m.x206 - m.x215)**2)**(-3)
    - 2) + ((m.x48 - m.x58)**2 + (m.x127 - m.x137)**2 + (m.x206 - m.x216)**2)
    **(-3) * (((m.x48 - m.x58)**2 + (m.x127 - m.x137)**2 + (m.x206 - m.x216)**2)
    **(-3) - 2) + ((m.x48 - m.x59)**2 + (m.x127 - m.x138)**2 + (m.x206 - m.x217)
    **2)**(-3) * (((m.x48 - m.x59)**2 + (m.x127 - m.x138)**2 + (m.x206 - m.x217)
    **2)**(-3) - 2) + ((m.x48 - m.x60)**2 + (m.x127 - m.x139)**2 + (m.x206 -
    m.x218)**2)**(-3) * (((m.x48 - m.x60)**2 + (m.x127 - m.x139)**2 + (m.x206
    - m.x218)**2)**(-3) - 2) + ((m.x48 - m.x61)**2 + (m.x127 - m.x140)**2 + (
    m.x206 - m.x219)**2)**(-3) * (((m.x48 - m.x61)**2 + (m.x127 - m.x140)**2 +
    (m.x206 - m.x219)**2)**(-3) - 2) + ((m.x48 - m.x62)**2 + (m.x127 - m.x141)
    **2 + (m.x206 - m.x220)**2)**(-3) * (((m.x48 - m.x62)**2 + (m.x127 - m.x141)
    **2 + (m.x206 - m.x220)**2)**(-3) - 2) + ((m.x48 - m.x63)**2 + (m.x127 -
    m.x142)**2 + (m.x206 - m.x221)**2)**(-3) * (((m.x48 - m.x63)**2 + (m.x127
    - m.x142)**2 + (m.x206 - m.x221)**2)**(-3) - 2) + ((m.x48 - m.x64)**2 + (
    m.x127 - m.x143)**2 + (m.x206 - m.x222)**2)**(-3) * (((m.x48 - m.x64)**2 +
    (m.x127 - m.x143)**2 + (m.x206 - m.x222)**2)**(-3) - 2) + ((m.x48 - m.x65)
    **2 + (m.x127 - m.x144)**2 + (m.x206 - m.x223)**2)**(-3) * (((m.x48 - m.x65)
    **2 + (m.x127 - m.x144)**2 + (m.x206 - m.x223)**2)**(-3) - 2) + ((m.x48 -
    m.x66)**2 + (m.x127 - m.x145)**2 + (m.x206 - m.x224)**2)**(-3) * (((m.x48
    - m.x66)**2 + (m.x127 - m.x145)**2 + (m.x206 - m.x224)**2)**(-3) - 2) + ((
    m.x48 - m.x67)**2 + (m.x127 - m.x146)**2 + (m.x206 - m.x225)**2)**(-3) * ((
    (m.x48 - m.x67)**2 + (m.x127 - m.x146)**2 + (m.x206 - m.x225)**2)**(-3) - 2)
    + ((m.x48 - m.x68)**2 + (m.x127 - m.x147)**2 + (m.x206 - m.x226)**2)**(-3)
    * (((m.x48 - m.x68)**2 + (m.x127 - m.x147)**2 + (m.x206 - m.x226)**2)**(-3)
    - 2) + ((m.x48 - m.x69)**2 + (m.x127 - m.x148)**2 + (m.x206 - m.x227)**2)
    **(-3) * (((m.x48 - m.x69)**2 + (m.x127 - m.x148)**2 + (m.x206 - m.x227)**2)
    **(-3) - 2) + ((m.x48 - m.x70)**2 + (m.x127 - m.x149)**2 + (m.x206 - m.x228)
    **2)**(-3) * (((m.x48 - m.x70)**2 + (m.x127 - m.x149)**2 + (m.x206 - m.x228)
    **2)**(-3) - 2) + ((m.x48 - m.x71)**2 + (m.x127 - m.x150)**2 + (m.x206 -
    m.x229)**2)**(-3) * (((m.x48 - m.x71)**2 + (m.x127 - m.x150)**2 + (m.x206
    - m.x229)**2)**(-3) - 2) + ((m.x48 - m.x72)**2 + (m.x127 - m.x151)**2 + (
    m.x206 - m.x230)**2)**(-3) * (((m.x48 - m.x72)**2 + (m.x127 - m.x151)**2 +
    (m.x206 - m.x230)**2)**(-3) - 2) + ((m.x48 - m.x73)**2 + (m.x127 - m.x152)
    **2 + (m.x206 - m.x231)**2)**(-3) * (((m.x48 - m.x73)**2 + (m.x127 - m.x152)
    **2 + (m.x206 - m.x231)**2)**(-3) - 2) + ((m.x48 - m.x74)**2 + (m.x127 -
    m.x153)**2 + (m.x206 - m.x232)**2)**(-3) * (((m.x48 - m.x74)**2 + (m.x127
    - m.x153)**2 + (m.x206 - m.x232)**2)**(-3) - 2) + ((m.x48 - m.x75)**2 + (
    m.x127 - m.x154)**2 + (m.x206 - m.x233)**2)**(-3) * (((m.x48 - m.x75)**2 +
    (m.x127 - m.x154)**2 + (m.x206 - m.x233)**2)**(-3) - 2) + ((m.x48 - m.x76)
    **2 + (m.x127 - m.x155)**2 + (m.x206 - m.x234)**2)**(-3) * (((m.x48 - m.x76)
    **2 + (m.x127 - m.x155)**2 + (m.x206 - m.x234)**2)**(-3) - 2) + ((m.x48 -
    m.x77)**2 + (m.x127 - m.x156)**2 + (m.x206 - m.x235)**2)**(-3) * (((m.x48
    - m.x77)**2 + (m.x127 - m.x156)**2 + (m.x206 - m.x235)**2)**(-3) - 2) + ((
    m.x48 - m.x78)**2 + (m.x127 - m.x157)**2 + (m.x206 - m.x236)**2)**(-3) * ((
    (m.x48 - m.x78)**2 + (m.x127 - m.x157)**2 + (m.x206 - m.x236)**2)**(-3) - 2)
    + ((m.x48 - m.x79)**2 + (m.x127 - m.x158)**2 + (m.x206 - m.x237)**2)**(-3)
    * (((m.x48 - m.x79)**2 + (m.x127 - m.x158)**2 + (m.x206 - m.x237)**2)**(-3)
    - 2) + ((m.x49 - m.x50)**2 + (m.x128 - m.x129)**2 + (m.x207 - m.x208)**2)
    **(-3) * (((m.x49 - m.x50)**2 + (m.x128 - m.x129)**2 + (m.x207 - m.x208)**2)
    **(-3) - 2) + ((m.x49 - m.x51)**2 + (m.x128 - m.x130)**2 + (m.x207 - m.x209)
    **2)**(-3) * (((m.x49 - m.x51)**2 + (m.x128 - m.x130)**2 + (m.x207 - m.x209)
    **2)**(-3) - 2) + ((m.x49 - m.x52)**2 + (m.x128 - m.x131)**2 + (m.x207 -
    m.x210)**2)**(-3) * (((m.x49 - m.x52)**2 + (m.x128 - m.x131)**2 + (m.x207
    - m.x210)**2)**(-3) - 2) + ((m.x49 - m.x53)**2 + (m.x128 - m.x132)**2 + (
    m.x207 - m.x211)**2)**(-3) * (((m.x49 - m.x53)**2 + (m.x128 - m.x132)**2 +
    (m.x207 - m.x211)**2)**(-3) - 2) + ((m.x49 - m.x54)**2 + (m.x128 - m.x133)
    **2 + (m.x207 - m.x212)**2)**(-3) * (((m.x49 - m.x54)**2 + (m.x128 - m.x133)
    **2 + (m.x207 - m.x212)**2)**(-3) - 2) + ((m.x49 - m.x55)**2 + (m.x128 -
    m.x134)**2 + (m.x207 - m.x213)**2)**(-3) * (((m.x49 - m.x55)**2 + (m.x128
    - m.x134)**2 + (m.x207 - m.x213)**2)**(-3) - 2) + ((m.x49 - m.x56)**2 + (
    m.x128 - m.x135)**2 + (m.x207 - m.x214)**2)**(-3) * (((m.x49 - m.x56)**2 +
    (m.x128 - m.x135)**2 + (m.x207 - m.x214)**2)**(-3) - 2) + ((m.x49 - m.x57)
    **2 + (m.x128 - m.x136)**2 + (m.x207 - m.x215)**2)**(-3) * (((m.x49 - m.x57)
    **2 + (m.x128 - m.x136)**2 + (m.x207 - m.x215)**2)**(-3) - 2) + ((m.x49 -
    m.x58)**2 + (m.x128 - m.x137)**2 + (m.x207 - m.x216)**2)**(-3) * (((m.x49
    - m.x58)**2 + (m.x128 - m.x137)**2 + (m.x207 - m.x216)**2)**(-3) - 2) + ((
    m.x49 - m.x59)**2 + (m.x128 - m.x138)**2 + (m.x207 - m.x217)**2)**(-3) * ((
    (m.x49 - m.x59)**2 + (m.x128 - m.x138)**2 + (m.x207 - m.x217)**2)**(-3) - 2)
    + ((m.x49 - m.x60)**2 + (m.x128 - m.x139)**2 + (m.x207 - m.x218)**2)**(-3)
    * (((m.x49 - m.x60)**2 + (m.x128 - m.x139)**2 + (m.x207 - m.x218)**2)**(-3)
    - 2) + ((m.x49 - m.x61)**2 + (m.x128 - m.x140)**2 + (m.x207 - m.x219)**2)
    **(-3) * (((m.x49 - m.x61)**2 + (m.x128 - m.x140)**2 + (m.x207 - m.x219)**2)
    **(-3) - 2) + ((m.x49 - m.x62)**2 + (m.x128 - m.x141)**2 + (m.x207 - m.x220)
    **2)**(-3) * (((m.x49 - m.x62)**2 + (m.x128 - m.x141)**2 + (m.x207 - m.x220)
    **2)**(-3) - 2) + ((m.x49 - m.x63)**2 + (m.x128 - m.x142)**2 + (m.x207 -
    m.x221)**2)**(-3) * (((m.x49 - m.x63)**2 + (m.x128 - m.x142)**2 + (m.x207
    - m.x221)**2)**(-3) - 2) + ((m.x49 - m.x64)**2 + (m.x128 - m.x143)**2 + (
    m.x207 - m.x222)**2)**(-3) * (((m.x49 - m.x64)**2 + (m.x128 - m.x143)**2 +
    (m.x207 - m.x222)**2)**(-3) - 2) + ((m.x49 - m.x65)**2 + (m.x128 - m.x144)
    **2 + (m.x207 - m.x223)**2)**(-3) * (((m.x49 - m.x65)**2 + (m.x128 - m.x144)
    **2 + (m.x207 - m.x223)**2)**(-3) - 2) + ((m.x49 - m.x66)**2 + (m.x128 -
    m.x145)**2 + (m.x207 - m.x224)**2)**(-3) * (((m.x49 - m.x66)**2 + (m.x128
    - m.x145)**2 + (m.x207 - m.x224)**2)**(-3) - 2) + ((m.x49 - m.x67)**2 + (
    m.x128 - m.x146)**2 + (m.x207 - m.x225)**2)**(-3) * (((m.x49 - m.x67)**2 +
    (m.x128 - m.x146)**2 + (m.x207 - m.x225)**2)**(-3) - 2) + ((m.x49 - m.x68)
    **2 + (m.x128 - m.x147)**2 + (m.x207 - m.x226)**2)**(-3) * (((m.x49 - m.x68)
    **2 + (m.x128 - m.x147)**2 + (m.x207 - m.x226)**2)**(-3) - 2) + ((m.x49 -
    m.x69)**2 + (m.x128 - m.x148)**2 + (m.x207 - m.x227)**2)**(-3) * (((m.x49
    - m.x69)**2 + (m.x128 - m.x148)**2 + (m.x207 - m.x227)**2)**(-3) - 2) + ((
    m.x49 - m.x70)**2 + (m.x128 - m.x149)**2 + (m.x207 - m.x228)**2)**(-3) * ((
    (m.x49 - m.x70)**2 + (m.x128 - m.x149)**2 + (m.x207 - m.x228)**2)**(-3) - 2)
    + ((m.x49 - m.x71)**2 + (m.x128 - m.x150)**2 + (m.x207 - m.x229)**2)**(-3)
    * (((m.x49 - m.x71)**2 + (m.x128 - m.x150)**2 + (m.x207 - m.x229)**2)**(-3)
    - 2) + ((m.x49 - m.x72)**2 + (m.x128 - m.x151)**2 + (m.x207 - m.x230)**2)
    **(-3) * (((m.x49 - m.x72)**2 + (m.x128 - m.x151)**2 + (m.x207 - m.x230)**2)
    **(-3) - 2) + ((m.x49 - m.x73)**2 + (m.x128 - m.x152)**2 + (m.x207 - m.x231)
    **2)**(-3) * (((m.x49 - m.x73)**2 + (m.x128 - m.x152)**2 + (m.x207 - m.x231)
    **2)**(-3) - 2) + ((m.x49 - m.x74)**2 + (m.x128 - m.x153)**2 + (m.x207 -
    m.x232)**2)**(-3) * (((m.x49 - m.x74)**2 + (m.x128 - m.x153)**2 + (m.x207
    - m.x232)**2)**(-3) - 2) + ((m.x49 - m.x75)**2 + (m.x128 - m.x154)**2 + (
    m.x207 - m.x233)**2)**(-3) * (((m.x49 - m.x75)**2 + (m.x128 - m.x154)**2 +
    (m.x207 - m.x233)**2)**(-3) - 2) + ((m.x49 - m.x76)**2 + (m.x128 - m.x155)
    **2 + (m.x207 - m.x234)**2)**(-3) * (((m.x49 - m.x76)**2 + (m.x128 - m.x155)
    **2 + (m.x207 - m.x234)**2)**(-3) - 2) + ((m.x49 - m.x77)**2 + (m.x128 -
    m.x156)**2 + (m.x207 - m.x235)**2)**(-3) * (((m.x49 - m.x77)**2 + (m.x128
    - m.x156)**2 + (m.x207 - m.x235)**2)**(-3) - 2) + ((m.x49 - m.x78)**2 + (
    m.x128 - m.x157)**2 + (m.x207 - m.x236)**2)**(-3) * (((m.x49 - m.x78)**2 +
    (m.x128 - m.x157)**2 + (m.x207 - m.x236)**2)**(-3) - 2) + ((m.x49 - m.x79)
    **2 + (m.x128 - m.x158)**2 + (m.x207 - m.x237)**2)**(-3) * (((m.x49 - m.x79)
    **2 + (m.x128 - m.x158)**2 + (m.x207 - m.x237)**2)**(-3) - 2) + ((m.x50 -
    m.x51)**2 + (m.x129 - m.x130)**2 + (m.x208 - m.x209)**2)**(-3) * (((m.x50
    - m.x51)**2 + (m.x129 - m.x130)**2 + (m.x208 - m.x209)**2)**(-3) - 2) + ((
    m.x50 - m.x52)**2 + (m.x129 - m.x131)**2 + (m.x208 - m.x210)**2)**(-3) * ((
    (m.x50 - m.x52)**2 + (m.x129 - m.x131)**2 + (m.x208 - m.x210)**2)**(-3) - 2)
    + ((m.x50 - m.x53)**2 + (m.x129 - m.x132)**2 + (m.x208 - m.x211)**2)**(-3)
    * (((m.x50 - m.x53)**2 + (m.x129 - m.x132)**2 + (m.x208 - m.x211)**2)**(-3)
    - 2) + ((m.x50 - m.x54)**2 + (m.x129 - m.x133)**2 + (m.x208 - m.x212)**2)
    **(-3) * (((m.x50 - m.x54)**2 + (m.x129 - m.x133)**2 + (m.x208 - m.x212)**2)
    **(-3) - 2) + ((m.x50 - m.x55)**2 + (m.x129 - m.x134)**2 + (m.x208 - m.x213)
    **2)**(-3) * (((m.x50 - m.x55)**2 + (m.x129 - m.x134)**2 + (m.x208 - m.x213)
    **2)**(-3) - 2) + ((m.x50 - m.x56)**2 + (m.x129 - m.x135)**2 + (m.x208 -
    m.x214)**2)**(-3) * (((m.x50 - m.x56)**2 + (m.x129 - m.x135)**2 + (m.x208
    - m.x214)**2)**(-3) - 2) + ((m.x50 - m.x57)**2 + (m.x129 - m.x136)**2 + (
    m.x208 - m.x215)**2)**(-3) * (((m.x50 - m.x57)**2 + (m.x129 - m.x136)**2 +
    (m.x208 - m.x215)**2)**(-3) - 2) + ((m.x50 - m.x58)**2 + (m.x129 - m.x137)
    **2 + (m.x208 - m.x216)**2)**(-3) * (((m.x50 - m.x58)**2 + (m.x129 - m.x137)
    **2 + (m.x208 - m.x216)**2)**(-3) - 2) + ((m.x50 - m.x59)**2 + (m.x129 -
    m.x138)**2 + (m.x208 - m.x217)**2)**(-3) * (((m.x50 - m.x59)**2 + (m.x129
    - m.x138)**2 + (m.x208 - m.x217)**2)**(-3) - 2) + ((m.x50 - m.x60)**2 + (
    m.x129 - m.x139)**2 + (m.x208 - m.x218)**2)**(-3) * (((m.x50 - m.x60)**2 +
    (m.x129 - m.x139)**2 + (m.x208 - m.x218)**2)**(-3) - 2) + ((m.x50 - m.x61)
    **2 + (m.x129 - m.x140)**2 + (m.x208 - m.x219)**2)**(-3) * (((m.x50 - m.x61)
    **2 + (m.x129 - m.x140)**2 + (m.x208 - m.x219)**2)**(-3) - 2) + ((m.x50 -
    m.x62)**2 + (m.x129 - m.x141)**2 + (m.x208 - m.x220)**2)**(-3) * (((m.x50
    - m.x62)**2 + (m.x129 - m.x141)**2 + (m.x208 - m.x220)**2)**(-3) - 2) + ((
    m.x50 - m.x63)**2 + (m.x129 - m.x142)**2 + (m.x208 - m.x221)**2)**(-3) * ((
    (m.x50 - m.x63)**2 + (m.x129 - m.x142)**2 + (m.x208 - m.x221)**2)**(-3) - 2)
    + ((m.x50 - m.x64)**2 + (m.x129 - m.x143)**2 + (m.x208 - m.x222)**2)**(-3)
    * (((m.x50 - m.x64)**2 + (m.x129 - m.x143)**2 + (m.x208 - m.x222)**2)**(-3)
    - 2) + ((m.x50 - m.x65)**2 + (m.x129 - m.x144)**2 + (m.x208 - m.x223)**2)
    **(-3) * (((m.x50 - m.x65)**2 + (m.x129 - m.x144)**2 + (m.x208 - m.x223)**2)
    **(-3) - 2) + ((m.x50 - m.x66)**2 + (m.x129 - m.x145)**2 + (m.x208 - m.x224)
    **2)**(-3) * (((m.x50 - m.x66)**2 + (m.x129 - m.x145)**2 + (m.x208 - m.x224)
    **2)**(-3) - 2) + ((m.x50 - m.x67)**2 + (m.x129 - m.x146)**2 + (m.x208 -
    m.x225)**2)**(-3) * (((m.x50 - m.x67)**2 + (m.x129 - m.x146)**2 + (m.x208
    - m.x225)**2)**(-3) - 2) + ((m.x50 - m.x68)**2 + (m.x129 - m.x147)**2 + (
    m.x208 - m.x226)**2)**(-3) * (((m.x50 - m.x68)**2 + (m.x129 - m.x147)**2 +
    (m.x208 - m.x226)**2)**(-3) - 2) + ((m.x50 - m.x69)**2 + (m.x129 - m.x148)
    **2 + (m.x208 - m.x227)**2)**(-3) * (((m.x50 - m.x69)**2 + (m.x129 - m.x148)
    **2 + (m.x208 - m.x227)**2)**(-3) - 2) + ((m.x50 - m.x70)**2 + (m.x129 -
    m.x149)**2 + (m.x208 - m.x228)**2)**(-3) * (((m.x50 - m.x70)**2 + (m.x129
    - m.x149)**2 + (m.x208 - m.x228)**2)**(-3) - 2) + ((m.x50 - m.x71)**2 + (
    m.x129 - m.x150)**2 + (m.x208 - m.x229)**2)**(-3) * (((m.x50 - m.x71)**2 +
    (m.x129 - m.x150)**2 + (m.x208 - m.x229)**2)**(-3) - 2) + ((m.x50 - m.x72)
    **2 + (m.x129 - m.x151)**2 + (m.x208 - m.x230)**2)**(-3) * (((m.x50 - m.x72)
    **2 + (m.x129 - m.x151)**2 + (m.x208 - m.x230)**2)**(-3) - 2) + ((m.x50 -
    m.x73)**2 + (m.x129 - m.x152)**2 + (m.x208 - m.x231)**2)**(-3) * (((m.x50
    - m.x73)**2 + (m.x129 - m.x152)**2 + (m.x208 - m.x231)**2)**(-3) - 2) + ((
    m.x50 - m.x74)**2 + (m.x129 - m.x153)**2 + (m.x208 - m.x232)**2)**(-3) * ((
    (m.x50 - m.x74)**2 + (m.x129 - m.x153)**2 + (m.x208 - m.x232)**2)**(-3) - 2)
    + ((m.x50 - m.x75)**2 + (m.x129 - m.x154)**2 + (m.x208 - m.x233)**2)**(-3)
    * (((m.x50 - m.x75)**2 + (m.x129 - m.x154)**2 + (m.x208 - m.x233)**2)**(-3)
    - 2) + ((m.x50 - m.x76)**2 + (m.x129 - m.x155)**2 + (m.x208 - m.x234)**2)
    **(-3) * (((m.x50 - m.x76)**2 + (m.x129 - m.x155)**2 + (m.x208 - m.x234)**2)
    **(-3) - 2) + ((m.x50 - m.x77)**2 + (m.x129 - m.x156)**2 + (m.x208 - m.x235)
    **2)**(-3) * (((m.x50 - m.x77)**2 + (m.x129 - m.x156)**2 + (m.x208 - m.x235)
    **2)**(-3) - 2) + ((m.x50 - m.x78)**2 + (m.x129 - m.x157)**2 + (m.x208 -
    m.x236)**2)**(-3) * (((m.x50 - m.x78)**2 + (m.x129 - m.x157)**2 + (m.x208
    - m.x236)**2)**(-3) - 2) + ((m.x50 - m.x79)**2 + (m.x129 - m.x158)**2 + (
    m.x208 - m.x237)**2)**(-3) * (((m.x50 - m.x79)**2 + (m.x129 - m.x158)**2 +
    (m.x208 - m.x237)**2)**(-3) - 2) + ((m.x51 - m.x52)**2 + (m.x130 - m.x131)
    **2 + (m.x209 - m.x210)**2)**(-3) * (((m.x51 - m.x52)**2 + (m.x130 - m.x131)
    **2 + (m.x209 - m.x210)**2)**(-3) - 2) + ((m.x51 - m.x53)**2 + (m.x130 -
    m.x132)**2 + (m.x209 - m.x211)**2)**(-3) * (((m.x51 - m.x53)**2 + (m.x130
    - m.x132)**2 + (m.x209 - m.x211)**2)**(-3) - 2) + ((m.x51 - m.x54)**2 + (
    m.x130 - m.x133)**2 + (m.x209 - m.x212)**2)**(-3) * (((m.x51 - m.x54)**2 +
    (m.x130 - m.x133)**2 + (m.x209 - m.x212)**2)**(-3) - 2) + ((m.x51 - m.x55)
    **2 + (m.x130 - m.x134)**2 + (m.x209 - m.x213)**2)**(-3) * (((m.x51 - m.x55)
    **2 + (m.x130 - m.x134)**2 + (m.x209 - m.x213)**2)**(-3) - 2) + ((m.x51 -
    m.x56)**2 + (m.x130 - m.x135)**2 + (m.x209 - m.x214)**2)**(-3) * (((m.x51
    - m.x56)**2 + (m.x130 - m.x135)**2 + (m.x209 - m.x214)**2)**(-3) - 2) + ((
    m.x51 - m.x57)**2 + (m.x130 - m.x136)**2 + (m.x209 - m.x215)**2)**(-3) * ((
    (m.x51 - m.x57)**2 + (m.x130 - m.x136)**2 + (m.x209 - m.x215)**2)**(-3) - 2)
    + ((m.x51 - m.x58)**2 + (m.x130 - m.x137)**2 + (m.x209 - m.x216)**2)**(-3)
    * (((m.x51 - m.x58)**2 + (m.x130 - m.x137)**2 + (m.x209 - m.x216)**2)**(-3)
    - 2) + ((m.x51 - m.x59)**2 + (m.x130 - m.x138)**2 + (m.x209 - m.x217)**2)
    **(-3) * (((m.x51 - m.x59)**2 + (m.x130 - m.x138)**2 + (m.x209 - m.x217)**2)
    **(-3) - 2) + ((m.x51 - m.x60)**2 + (m.x130 - m.x139)**2 + (m.x209 - m.x218)
    **2)**(-3) * (((m.x51 - m.x60)**2 + (m.x130 - m.x139)**2 + (m.x209 - m.x218)
    **2)**(-3) - 2) + ((m.x51 - m.x61)**2 + (m.x130 - m.x140)**2 + (m.x209 -
    m.x219)**2)**(-3) * (((m.x51 - m.x61)**2 + (m.x130 - m.x140)**2 + (m.x209
    - m.x219)**2)**(-3) - 2) + ((m.x51 - m.x62)**2 + (m.x130 - m.x141)**2 + (
    m.x209 - m.x220)**2)**(-3) * (((m.x51 - m.x62)**2 + (m.x130 - m.x141)**2 +
    (m.x209 - m.x220)**2)**(-3) - 2) + ((m.x51 - m.x63)**2 + (m.x130 - m.x142)
    **2 + (m.x209 - m.x221)**2)**(-3) * (((m.x51 - m.x63)**2 + (m.x130 - m.x142)
    **2 + (m.x209 - m.x221)**2)**(-3) - 2) + ((m.x51 - m.x64)**2 + (m.x130 -
    m.x143)**2 + (m.x209 - m.x222)**2)**(-3) * (((m.x51 - m.x64)**2 + (m.x130
    - m.x143)**2 + (m.x209 - m.x222)**2)**(-3) - 2) + ((m.x51 - m.x65)**2 + (
    m.x130 - m.x144)**2 + (m.x209 - m.x223)**2)**(-3) * (((m.x51 - m.x65)**2 +
    (m.x130 - m.x144)**2 + (m.x209 - m.x223)**2)**(-3) - 2) + ((m.x51 - m.x66)
    **2 + (m.x130 - m.x145)**2 + (m.x209 - m.x224)**2)**(-3) * (((m.x51 - m.x66)
    **2 + (m.x130 - m.x145)**2 + (m.x209 - m.x224)**2)**(-3) - 2) + ((m.x51 -
    m.x67)**2 + (m.x130 - m.x146)**2 + (m.x209 - m.x225)**2)**(-3) * (((m.x51
    - m.x67)**2 + (m.x130 - m.x146)**2 + (m.x209 - m.x225)**2)**(-3) - 2) + ((
    m.x51 - m.x68)**2 + (m.x130 - m.x147)**2 + (m.x209 - m.x226)**2)**(-3) * ((
    (m.x51 - m.x68)**2 + (m.x130 - m.x147)**2 + (m.x209 - m.x226)**2)**(-3) - 2)
    + ((m.x51 - m.x69)**2 + (m.x130 - m.x148)**2 + (m.x209 - m.x227)**2)**(-3)
    * (((m.x51 - m.x69)**2 + (m.x130 - m.x148)**2 + (m.x209 - m.x227)**2)**(-3)
    - 2) + ((m.x51 - m.x70)**2 + (m.x130 - m.x149)**2 + (m.x209 - m.x228)**2)
    **(-3) * (((m.x51 - m.x70)**2 + (m.x130 - m.x149)**2 + (m.x209 - m.x228)**2)
    **(-3) - 2) + ((m.x51 - m.x71)**2 + (m.x130 - m.x150)**2 + (m.x209 - m.x229)
    **2)**(-3) * (((m.x51 - m.x71)**2 + (m.x130 - m.x150)**2 + (m.x209 - m.x229)
    **2)**(-3) - 2) + ((m.x51 - m.x72)**2 + (m.x130 - m.x151)**2 + (m.x209 -
    m.x230)**2)**(-3) * (((m.x51 - m.x72)**2 + (m.x130 - m.x151)**2 + (m.x209
    - m.x230)**2)**(-3) - 2) + ((m.x51 - m.x73)**2 + (m.x130 - m.x152)**2 + (
    m.x209 - m.x231)**2)**(-3) * (((m.x51 - m.x73)**2 + (m.x130 - m.x152)**2 +
    (m.x209 - m.x231)**2)**(-3) - 2) + ((m.x51 - m.x74)**2 + (m.x130 - m.x153)
    **2 + (m.x209 - m.x232)**2)**(-3) * (((m.x51 - m.x74)**2 + (m.x130 - m.x153)
    **2 + (m.x209 - m.x232)**2)**(-3) - 2) + ((m.x51 - m.x75)**2 + (m.x130 -
    m.x154)**2 + (m.x209 - m.x233)**2)**(-3) * (((m.x51 - m.x75)**2 + (m.x130
    - m.x154)**2 + (m.x209 - m.x233)**2)**(-3) - 2) + ((m.x51 - m.x76)**2 + (
    m.x130 - m.x155)**2 + (m.x209 - m.x234)**2)**(-3) * (((m.x51 - m.x76)**2 +
    (m.x130 - m.x155)**2 + (m.x209 - m.x234)**2)**(-3) - 2) + ((m.x51 - m.x77)
    **2 + (m.x130 - m.x156)**2 + (m.x209 - m.x235)**2)**(-3) * (((m.x51 - m.x77)
    **2 + (m.x130 - m.x156)**2 + (m.x209 - m.x235)**2)**(-3) - 2) + ((m.x51 -
    m.x78)**2 + (m.x130 - m.x157)**2 + (m.x209 - m.x236)**2)**(-3) * (((m.x51
    - m.x78)**2 + (m.x130 - m.x157)**2 + (m.x209 - m.x236)**2)**(-3) - 2) + ((
    m.x51 - m.x79)**2 + (m.x130 - m.x158)**2 + (m.x209 - m.x237)**2)**(-3) * ((
    (m.x51 - m.x79)**2 + (m.x130 - m.x158)**2 + (m.x209 - m.x237)**2)**(-3) - 2)
    + ((m.x52 - m.x53)**2 + (m.x131 - m.x132)**2 + (m.x210 - m.x211)**2)**(-3)
    * (((m.x52 - m.x53)**2 + (m.x131 - m.x132)**2 + (m.x210 - m.x211)**2)**(-3)
    - 2) + ((m.x52 - m.x54)**2 + (m.x131 - m.x133)**2 + (m.x210 - m.x212)**2)
    **(-3) * (((m.x52 - m.x54)**2 + (m.x131 - m.x133)**2 + (m.x210 - m.x212)**2)
    **(-3) - 2) + ((m.x52 - m.x55)**2 + (m.x131 - m.x134)**2 + (m.x210 - m.x213)
    **2)**(-3) * (((m.x52 - m.x55)**2 + (m.x131 - m.x134)**2 + (m.x210 - m.x213)
    **2)**(-3) - 2) + ((m.x52 - m.x56)**2 + (m.x131 - m.x135)**2 + (m.x210 -
    m.x214)**2)**(-3) * (((m.x52 - m.x56)**2 + (m.x131 - m.x135)**2 + (m.x210
    - m.x214)**2)**(-3) - 2) + ((m.x52 - m.x57)**2 + (m.x131 - m.x136)**2 + (
    m.x210 - m.x215)**2)**(-3) * (((m.x52 - m.x57)**2 + (m.x131 - m.x136)**2 +
    (m.x210 - m.x215)**2)**(-3) - 2) + ((m.x52 - m.x58)**2 + (m.x131 - m.x137)
    **2 + (m.x210 - m.x216)**2)**(-3) * (((m.x52 - m.x58)**2 + (m.x131 - m.x137)
    **2 + (m.x210 - m.x216)**2)**(-3) - 2) + ((m.x52 - m.x59)**2 + (m.x131 -
    m.x138)**2 + (m.x210 - m.x217)**2)**(-3) * (((m.x52 - m.x59)**2 + (m.x131
    - m.x138)**2 + (m.x210 - m.x217)**2)**(-3) - 2) + ((m.x52 - m.x60)**2 + (
    m.x131 - m.x139)**2 + (m.x210 - m.x218)**2)**(-3) * (((m.x52 - m.x60)**2 +
    (m.x131 - m.x139)**2 + (m.x210 - m.x218)**2)**(-3) - 2) + ((m.x52 - m.x61)
    **2 + (m.x131 - m.x140)**2 + (m.x210 - m.x219)**2)**(-3) * (((m.x52 - m.x61)
    **2 + (m.x131 - m.x140)**2 + (m.x210 - m.x219)**2)**(-3) - 2) + ((m.x52 -
    m.x62)**2 + (m.x131 - m.x141)**2 + (m.x210 - m.x220)**2)**(-3) * (((m.x52
    - m.x62)**2 + (m.x131 - m.x141)**2 + (m.x210 - m.x220)**2)**(-3) - 2) + ((
    m.x52 - m.x63)**2 + (m.x131 - m.x142)**2 + (m.x210 - m.x221)**2)**(-3) * ((
    (m.x52 - m.x63)**2 + (m.x131 - m.x142)**2 + (m.x210 - m.x221)**2)**(-3) - 2)
    + ((m.x52 - m.x64)**2 + (m.x131 - m.x143)**2 + (m.x210 - m.x222)**2)**(-3)
    * (((m.x52 - m.x64)**2 + (m.x131 - m.x143)**2 + (m.x210 - m.x222)**2)**(-3)
    - 2) + ((m.x52 - m.x65)**2 + (m.x131 - m.x144)**2 + (m.x210 - m.x223)**2)
    **(-3) * (((m.x52 - m.x65)**2 + (m.x131 - m.x144)**2 + (m.x210 - m.x223)**2)
    **(-3) - 2) + ((m.x52 - m.x66)**2 + (m.x131 - m.x145)**2 + (m.x210 - m.x224)
    **2)**(-3) * (((m.x52 - m.x66)**2 + (m.x131 - m.x145)**2 + (m.x210 - m.x224)
    **2)**(-3) - 2) + ((m.x52 - m.x67)**2 + (m.x131 - m.x146)**2 + (m.x210 -
    m.x225)**2)**(-3) * (((m.x52 - m.x67)**2 + (m.x131 - m.x146)**2 + (m.x210
    - m.x225)**2)**(-3) - 2) + ((m.x52 - m.x68)**2 + (m.x131 - m.x147)**2 + (
    m.x210 - m.x226)**2)**(-3) * (((m.x52 - m.x68)**2 + (m.x131 - m.x147)**2 +
    (m.x210 - m.x226)**2)**(-3) - 2) + ((m.x52 - m.x69)**2 + (m.x131 - m.x148)
    **2 + (m.x210 - m.x227)**2)**(-3) * (((m.x52 - m.x69)**2 + (m.x131 - m.x148)
    **2 + (m.x210 - m.x227)**2)**(-3) - 2) + ((m.x52 - m.x70)**2 + (m.x131 -
    m.x149)**2 + (m.x210 - m.x228)**2)**(-3) * (((m.x52 - m.x70)**2 + (m.x131
    - m.x149)**2 + (m.x210 - m.x228)**2)**(-3) - 2) + ((m.x52 - m.x71)**2 + (
    m.x131 - m.x150)**2 + (m.x210 - m.x229)**2)**(-3) * (((m.x52 - m.x71)**2 +
    (m.x131 - m.x150)**2 + (m.x210 - m.x229)**2)**(-3) - 2) + ((m.x52 - m.x72)
    **2 + (m.x131 - m.x151)**2 + (m.x210 - m.x230)**2)**(-3) * (((m.x52 - m.x72)
    **2 + (m.x131 - m.x151)**2 + (m.x210 - m.x230)**2)**(-3) - 2) + ((m.x52 -
    m.x73)**2 + (m.x131 - m.x152)**2 + (m.x210 - m.x231)**2)**(-3) * (((m.x52
    - m.x73)**2 + (m.x131 - m.x152)**2 + (m.x210 - m.x231)**2)**(-3) - 2) + ((
    m.x52 - m.x74)**2 + (m.x131 - m.x153)**2 + (m.x210 - m.x232)**2)**(-3) * ((
    (m.x52 - m.x74)**2 + (m.x131 - m.x153)**2 + (m.x210 - m.x232)**2)**(-3) - 2)
    + ((m.x52 - m.x75)**2 + (m.x131 - m.x154)**2 + (m.x210 - m.x233)**2)**(-3)
    * (((m.x52 - m.x75)**2 + (m.x131 - m.x154)**2 + (m.x210 - m.x233)**2)**(-3)
    - 2) + ((m.x52 - m.x76)**2 + (m.x131 - m.x155)**2 + (m.x210 - m.x234)**2)
    **(-3) * (((m.x52 - m.x76)**2 + (m.x131 - m.x155)**2 + (m.x210 - m.x234)**2)
    **(-3) - 2) + ((m.x52 - m.x77)**2 + (m.x131 - m.x156)**2 + (m.x210 - m.x235)
    **2)**(-3) * (((m.x52 - m.x77)**2 + (m.x131 - m.x156)**2 + (m.x210 - m.x235)
    **2)**(-3) - 2) + ((m.x52 - m.x78)**2 + (m.x131 - m.x157)**2 + (m.x210 -
    m.x236)**2)**(-3) * (((m.x52 - m.x78)**2 + (m.x131 - m.x157)**2 + (m.x210
    - m.x236)**2)**(-3) - 2) + ((m.x52 - m.x79)**2 + (m.x131 - m.x158)**2 + (
    m.x210 - m.x237)**2)**(-3) * (((m.x52 - m.x79)**2 + (m.x131 - m.x158)**2 +
    (m.x210 - m.x237)**2)**(-3) - 2) + ((m.x53 - m.x54)**2 + (m.x132 - m.x133)
    **2 + (m.x211 - m.x212)**2)**(-3) * (((m.x53 - m.x54)**2 + (m.x132 - m.x133)
    **2 + (m.x211 - m.x212)**2)**(-3) - 2) + ((m.x53 - m.x55)**2 + (m.x132 -
    m.x134)**2 + (m.x211 - m.x213)**2)**(-3) * (((m.x53 - m.x55)**2 + (m.x132
    - m.x134)**2 + (m.x211 - m.x213)**2)**(-3) - 2) + ((m.x53 - m.x56)**2 + (
    m.x132 - m.x135)**2 + (m.x211 - m.x214)**2)**(-3) * (((m.x53 - m.x56)**2 +
    (m.x132 - m.x135)**2 + (m.x211 - m.x214)**2)**(-3) - 2) + ((m.x53 - m.x57)
    **2 + (m.x132 - m.x136)**2 + (m.x211 - m.x215)**2)**(-3) * (((m.x53 - m.x57)
    **2 + (m.x132 - m.x136)**2 + (m.x211 - m.x215)**2)**(-3) - 2) + ((m.x53 -
    m.x58)**2 + (m.x132 - m.x137)**2 + (m.x211 - m.x216)**2)**(-3) * (((m.x53
    - m.x58)**2 + (m.x132 - m.x137)**2 + (m.x211 - m.x216)**2)**(-3) - 2) + ((
    m.x53 - m.x59)**2 + (m.x132 - m.x138)**2 + (m.x211 - m.x217)**2)**(-3) * ((
    (m.x53 - m.x59)**2 + (m.x132 - m.x138)**2 + (m.x211 - m.x217)**2)**(-3) - 2)
    + ((m.x53 - m.x60)**2 + (m.x132 - m.x139)**2 + (m.x211 - m.x218)**2)**(-3)
    * (((m.x53 - m.x60)**2 + (m.x132 - m.x139)**2 + (m.x211 - m.x218)**2)**(-3)
    - 2) + ((m.x53 - m.x61)**2 + (m.x132 - m.x140)**2 + (m.x211 - m.x219)**2)
    **(-3) * (((m.x53 - m.x61)**2 + (m.x132 - m.x140)**2 + (m.x211 - m.x219)**2)
    **(-3) - 2) + ((m.x53 - m.x62)**2 + (m.x132 - m.x141)**2 + (m.x211 - m.x220)
    **2)**(-3) * (((m.x53 - m.x62)**2 + (m.x132 - m.x141)**2 + (m.x211 - m.x220)
    **2)**(-3) - 2) + ((m.x53 - m.x63)**2 + (m.x132 - m.x142)**2 + (m.x211 -
    m.x221)**2)**(-3) * (((m.x53 - m.x63)**2 + (m.x132 - m.x142)**2 + (m.x211
    - m.x221)**2)**(-3) - 2) + ((m.x53 - m.x64)**2 + (m.x132 - m.x143)**2 + (
    m.x211 - m.x222)**2)**(-3) * (((m.x53 - m.x64)**2 + (m.x132 - m.x143)**2 +
    (m.x211 - m.x222)**2)**(-3) - 2) + ((m.x53 - m.x65)**2 + (m.x132 - m.x144)
    **2 + (m.x211 - m.x223)**2)**(-3) * (((m.x53 - m.x65)**2 + (m.x132 - m.x144)
    **2 + (m.x211 - m.x223)**2)**(-3) - 2) + ((m.x53 - m.x66)**2 + (m.x132 -
    m.x145)**2 + (m.x211 - m.x224)**2)**(-3) * (((m.x53 - m.x66)**2 + (m.x132
    - m.x145)**2 + (m.x211 - m.x224)**2)**(-3) - 2) + ((m.x53 - m.x67)**2 + (
    m.x132 - m.x146)**2 + (m.x211 - m.x225)**2)**(-3) * (((m.x53 - m.x67)**2 +
    (m.x132 - m.x146)**2 + (m.x211 - m.x225)**2)**(-3) - 2) + ((m.x53 - m.x68)
    **2 + (m.x132 - m.x147)**2 + (m.x211 - m.x226)**2)**(-3) * (((m.x53 - m.x68)
    **2 + (m.x132 - m.x147)**2 + (m.x211 - m.x226)**2)**(-3) - 2) + ((m.x53 -
    m.x69)**2 + (m.x132 - m.x148)**2 + (m.x211 - m.x227)**2)**(-3) * (((m.x53
    - m.x69)**2 + (m.x132 - m.x148)**2 + (m.x211 - m.x227)**2)**(-3) - 2) + ((
    m.x53 - m.x70)**2 + (m.x132 - m.x149)**2 + (m.x211 - m.x228)**2)**(-3) * ((
    (m.x53 - m.x70)**2 + (m.x132 - m.x149)**2 + (m.x211 - m.x228)**2)**(-3) - 2)
    + ((m.x53 - m.x71)**2 + (m.x132 - m.x150)**2 + (m.x211 - m.x229)**2)**(-3)
    * (((m.x53 - m.x71)**2 + (m.x132 - m.x150)**2 + (m.x211 - m.x229)**2)**(-3)
    - 2) + ((m.x53 - m.x72)**2 + (m.x132 - m.x151)**2 + (m.x211 - m.x230)**2)
    **(-3) * (((m.x53 - m.x72)**2 + (m.x132 - m.x151)**2 + (m.x211 - m.x230)**2)
    **(-3) - 2) + ((m.x53 - m.x73)**2 + (m.x132 - m.x152)**2 + (m.x211 - m.x231)
    **2)**(-3) * (((m.x53 - m.x73)**2 + (m.x132 - m.x152)**2 + (m.x211 - m.x231)
    **2)**(-3) - 2) + ((m.x53 - m.x74)**2 + (m.x132 - m.x153)**2 + (m.x211 -
    m.x232)**2)**(-3) * (((m.x53 - m.x74)**2 + (m.x132 - m.x153)**2 + (m.x211
    - m.x232)**2)**(-3) - 2) + ((m.x53 - m.x75)**2 + (m.x132 - m.x154)**2 + (
    m.x211 - m.x233)**2)**(-3) * (((m.x53 - m.x75)**2 + (m.x132 - m.x154)**2 +
    (m.x211 - m.x233)**2)**(-3) - 2) + ((m.x53 - m.x76)**2 + (m.x132 - m.x155)
    **2 + (m.x211 - m.x234)**2)**(-3) * (((m.x53 - m.x76)**2 + (m.x132 - m.x155)
    **2 + (m.x211 - m.x234)**2)**(-3) - 2) + ((m.x53 - m.x77)**2 + (m.x132 -
    m.x156)**2 + (m.x211 - m.x235)**2)**(-3) * (((m.x53 - m.x77)**2 + (m.x132
    - m.x156)**2 + (m.x211 - m.x235)**2)**(-3) - 2) + ((m.x53 - m.x78)**2 + (
    m.x132 - m.x157)**2 + (m.x211 - m.x236)**2)**(-3) * (((m.x53 - m.x78)**2 +
    (m.x132 - m.x157)**2 + (m.x211 - m.x236)**2)**(-3) - 2) + ((m.x53 - m.x79)
    **2 + (m.x132 - m.x158)**2 + (m.x211 - m.x237)**2)**(-3) * (((m.x53 - m.x79)
    **2 + (m.x132 - m.x158)**2 + (m.x211 - m.x237)**2)**(-3) - 2) + ((m.x54 -
    m.x55)**2 + (m.x133 - m.x134)**2 + (m.x212 - m.x213)**2)**(-3) * (((m.x54
    - m.x55)**2 + (m.x133 - m.x134)**2 + (m.x212 - m.x213)**2)**(-3) - 2) + ((
    m.x54 - m.x56)**2 + (m.x133 - m.x135)**2 + (m.x212 - m.x214)**2)**(-3) * ((
    (m.x54 - m.x56)**2 + (m.x133 - m.x135)**2 + (m.x212 - m.x214)**2)**(-3) - 2)
    + ((m.x54 - m.x57)**2 + (m.x133 - m.x136)**2 + (m.x212 - m.x215)**2)**(-3)
    * (((m.x54 - m.x57)**2 + (m.x133 - m.x136)**2 + (m.x212 - m.x215)**2)**(-3)
    - 2) + ((m.x54 - m.x58)**2 + (m.x133 - m.x137)**2 + (m.x212 - m.x216)**2)
    **(-3) * (((m.x54 - m.x58)**2 + (m.x133 - m.x137)**2 + (m.x212 - m.x216)**2)
    **(-3) - 2) + ((m.x54 - m.x59)**2 + (m.x133 - m.x138)**2 + (m.x212 - m.x217)
    **2)**(-3) * (((m.x54 - m.x59)**2 + (m.x133 - m.x138)**2 + (m.x212 - m.x217)
    **2)**(-3) - 2) + ((m.x54 - m.x60)**2 + (m.x133 - m.x139)**2 + (m.x212 -
    m.x218)**2)**(-3) * (((m.x54 - m.x60)**2 + (m.x133 - m.x139)**2 + (m.x212
    - m.x218)**2)**(-3) - 2) + ((m.x54 - m.x61)**2 + (m.x133 - m.x140)**2 + (
    m.x212 - m.x219)**2)**(-3) * (((m.x54 - m.x61)**2 + (m.x133 - m.x140)**2 +
    (m.x212 - m.x219)**2)**(-3) - 2) + ((m.x54 - m.x62)**2 + (m.x133 - m.x141)
    **2 + (m.x212 - m.x220)**2)**(-3) * (((m.x54 - m.x62)**2 + (m.x133 - m.x141)
    **2 + (m.x212 - m.x220)**2)**(-3) - 2) + ((m.x54 - m.x63)**2 + (m.x133 -
    m.x142)**2 + (m.x212 - m.x221)**2)**(-3) * (((m.x54 - m.x63)**2 + (m.x133
    - m.x142)**2 + (m.x212 - m.x221)**2)**(-3) - 2) + ((m.x54 - m.x64)**2 + (
    m.x133 - m.x143)**2 + (m.x212 - m.x222)**2)**(-3) * (((m.x54 - m.x64)**2 +
    (m.x133 - m.x143)**2 + (m.x212 - m.x222)**2)**(-3) - 2) + ((m.x54 - m.x65)
    **2 + (m.x133 - m.x144)**2 + (m.x212 - m.x223)**2)**(-3) * (((m.x54 - m.x65)
    **2 + (m.x133 - m.x144)**2 + (m.x212 - m.x223)**2)**(-3) - 2) + ((m.x54 -
    m.x66)**2 + (m.x133 - m.x145)**2 + (m.x212 - m.x224)**2)**(-3) * (((m.x54
    - m.x66)**2 + (m.x133 - m.x145)**2 + (m.x212 - m.x224)**2)**(-3) - 2) + ((
    m.x54 - m.x67)**2 + (m.x133 - m.x146)**2 + (m.x212 - m.x225)**2)**(-3) * ((
    (m.x54 - m.x67)**2 + (m.x133 - m.x146)**2 + (m.x212 - m.x225)**2)**(-3) - 2)
    + ((m.x54 - m.x68)**2 + (m.x133 - m.x147)**2 + (m.x212 - m.x226)**2)**(-3)
    * (((m.x54 - m.x68)**2 + (m.x133 - m.x147)**2 + (m.x212 - m.x226)**2)**(-3)
    - 2) + ((m.x54 - m.x69)**2 + (m.x133 - m.x148)**2 + (m.x212 - m.x227)**2)
    **(-3) * (((m.x54 - m.x69)**2 + (m.x133 - m.x148)**2 + (m.x212 - m.x227)**2)
    **(-3) - 2) + ((m.x54 - m.x70)**2 + (m.x133 - m.x149)**2 + (m.x212 - m.x228)
    **2)**(-3) * (((m.x54 - m.x70)**2 + (m.x133 - m.x149)**2 + (m.x212 - m.x228)
    **2)**(-3) - 2) + ((m.x54 - m.x71)**2 + (m.x133 - m.x150)**2 + (m.x212 -
    m.x229)**2)**(-3) * (((m.x54 - m.x71)**2 + (m.x133 - m.x150)**2 + (m.x212
    - m.x229)**2)**(-3) - 2) + ((m.x54 - m.x72)**2 + (m.x133 - m.x151)**2 + (
    m.x212 - m.x230)**2)**(-3) * (((m.x54 - m.x72)**2 + (m.x133 - m.x151)**2 +
    (m.x212 - m.x230)**2)**(-3) - 2) + ((m.x54 - m.x73)**2 + (m.x133 - m.x152)
    **2 + (m.x212 - m.x231)**2)**(-3) * (((m.x54 - m.x73)**2 + (m.x133 - m.x152)
    **2 + (m.x212 - m.x231)**2)**(-3) - 2) + ((m.x54 - m.x74)**2 + (m.x133 -
    m.x153)**2 + (m.x212 - m.x232)**2)**(-3) * (((m.x54 - m.x74)**2 + (m.x133
    - m.x153)**2 + (m.x212 - m.x232)**2)**(-3) - 2) + ((m.x54 - m.x75)**2 + (
    m.x133 - m.x154)**2 + (m.x212 - m.x233)**2)**(-3) * (((m.x54 - m.x75)**2 +
    (m.x133 - m.x154)**2 + (m.x212 - m.x233)**2)**(-3) - 2) + ((m.x54 - m.x76)
    **2 + (m.x133 - m.x155)**2 + (m.x212 - m.x234)**2)**(-3) * (((m.x54 - m.x76)
    **2 + (m.x133 - m.x155)**2 + (m.x212 - m.x234)**2)**(-3) - 2) + ((m.x54 -
    m.x77)**2 + (m.x133 - m.x156)**2 + (m.x212 - m.x235)**2)**(-3) * (((m.x54
    - m.x77)**2 + (m.x133 - m.x156)**2 + (m.x212 - m.x235)**2)**(-3) - 2) + ((
    m.x54 - m.x78)**2 + (m.x133 - m.x157)**2 + (m.x212 - m.x236)**2)**(-3) * ((
    (m.x54 - m.x78)**2 + (m.x133 - m.x157)**2 + (m.x212 - m.x236)**2)**(-3) - 2)
    + ((m.x54 - m.x79)**2 + (m.x133 - m.x158)**2 + (m.x212 - m.x237)**2)**(-3)
    * (((m.x54 - m.x79)**2 + (m.x133 - m.x158)**2 + (m.x212 - m.x237)**2)**(-3)
    - 2) + ((m.x55 - m.x56)**2 + (m.x134 - m.x135)**2 + (m.x213 - m.x214)**2)
    **(-3) * (((m.x55 - m.x56)**2 + (m.x134 - m.x135)**2 + (m.x213 - m.x214)**2)
    **(-3) - 2) + ((m.x55 - m.x57)**2 + (m.x134 - m.x136)**2 + (m.x213 - m.x215)
    **2)**(-3) * (((m.x55 - m.x57)**2 + (m.x134 - m.x136)**2 + (m.x213 - m.x215)
    **2)**(-3) - 2) + ((m.x55 - m.x58)**2 + (m.x134 - m.x137)**2 + (m.x213 -
    m.x216)**2)**(-3) * (((m.x55 - m.x58)**2 + (m.x134 - m.x137)**2 + (m.x213
    - m.x216)**2)**(-3) - 2) + ((m.x55 - m.x59)**2 + (m.x134 - m.x138)**2 + (
    m.x213 - m.x217)**2)**(-3) * (((m.x55 - m.x59)**2 + (m.x134 - m.x138)**2 +
    (m.x213 - m.x217)**2)**(-3) - 2) + ((m.x55 - m.x60)**2 + (m.x134 - m.x139)
    **2 + (m.x213 - m.x218)**2)**(-3) * (((m.x55 - m.x60)**2 + (m.x134 - m.x139)
    **2 + (m.x213 - m.x218)**2)**(-3) - 2) + ((m.x55 - m.x61)**2 + (m.x134 -
    m.x140)**2 + (m.x213 - m.x219)**2)**(-3) * (((m.x55 - m.x61)**2 + (m.x134
    - m.x140)**2 + (m.x213 - m.x219)**2)**(-3) - 2) + ((m.x55 - m.x62)**2 + (
    m.x134 - m.x141)**2 + (m.x213 - m.x220)**2)**(-3) * (((m.x55 - m.x62)**2 +
    (m.x134 - m.x141)**2 + (m.x213 - m.x220)**2)**(-3) - 2) + ((m.x55 - m.x63)
    **2 + (m.x134 - m.x142)**2 + (m.x213 - m.x221)**2)**(-3) * (((m.x55 - m.x63)
    **2 + (m.x134 - m.x142)**2 + (m.x213 - m.x221)**2)**(-3) - 2) + ((m.x55 -
    m.x64)**2 + (m.x134 - m.x143)**2 + (m.x213 - m.x222)**2)**(-3) * (((m.x55
    - m.x64)**2 + (m.x134 - m.x143)**2 + (m.x213 - m.x222)**2)**(-3) - 2) + ((
    m.x55 - m.x65)**2 + (m.x134 - m.x144)**2 + (m.x213 - m.x223)**2)**(-3) * ((
    (m.x55 - m.x65)**2 + (m.x134 - m.x144)**2 + (m.x213 - m.x223)**2)**(-3) - 2)
    + ((m.x55 - m.x66)**2 + (m.x134 - m.x145)**2 + (m.x213 - m.x224)**2)**(-3)
    * (((m.x55 - m.x66)**2 + (m.x134 - m.x145)**2 + (m.x213 - m.x224)**2)**(-3)
    - 2) + ((m.x55 - m.x67)**2 + (m.x134 - m.x146)**2 + (m.x213 - m.x225)**2)
    **(-3) * (((m.x55 - m.x67)**2 + (m.x134 - m.x146)**2 + (m.x213 - m.x225)**2)
    **(-3) - 2) + ((m.x55 - m.x68)**2 + (m.x134 - m.x147)**2 + (m.x213 - m.x226)
    **2)**(-3) * (((m.x55 - m.x68)**2 + (m.x134 - m.x147)**2 + (m.x213 - m.x226)
    **2)**(-3) - 2) + ((m.x55 - m.x69)**2 + (m.x134 - m.x148)**2 + (m.x213 -
    m.x227)**2)**(-3) * (((m.x55 - m.x69)**2 + (m.x134 - m.x148)**2 + (m.x213
    - m.x227)**2)**(-3) - 2) + ((m.x55 - m.x70)**2 + (m.x134 - m.x149)**2 + (
    m.x213 - m.x228)**2)**(-3) * (((m.x55 - m.x70)**2 + (m.x134 - m.x149)**2 +
    (m.x213 - m.x228)**2)**(-3) - 2) + ((m.x55 - m.x71)**2 + (m.x134 - m.x150)
    **2 + (m.x213 - m.x229)**2)**(-3) * (((m.x55 - m.x71)**2 + (m.x134 - m.x150)
    **2 + (m.x213 - m.x229)**2)**(-3) - 2) + ((m.x55 - m.x72)**2 + (m.x134 -
    m.x151)**2 + (m.x213 - m.x230)**2)**(-3) * (((m.x55 - m.x72)**2 + (m.x134
    - m.x151)**2 + (m.x213 - m.x230)**2)**(-3) - 2) + ((m.x55 - m.x73)**2 + (
    m.x134 - m.x152)**2 + (m.x213 - m.x231)**2)**(-3) * (((m.x55 - m.x73)**2 +
    (m.x134 - m.x152)**2 + (m.x213 - m.x231)**2)**(-3) - 2) + ((m.x55 - m.x74)
    **2 + (m.x134 - m.x153)**2 + (m.x213 - m.x232)**2)**(-3) * (((m.x55 - m.x74)
    **2 + (m.x134 - m.x153)**2 + (m.x213 - m.x232)**2)**(-3) - 2) + ((m.x55 -
    m.x75)**2 + (m.x134 - m.x154)**2 + (m.x213 - m.x233)**2)**(-3) * (((m.x55
    - m.x75)**2 + (m.x134 - m.x154)**2 + (m.x213 - m.x233)**2)**(-3) - 2) + ((
    m.x55 - m.x76)**2 + (m.x134 - m.x155)**2 + (m.x213 - m.x234)**2)**(-3) * ((
    (m.x55 - m.x76)**2 + (m.x134 - m.x155)**2 + (m.x213 - m.x234)**2)**(-3) - 2)
    + ((m.x55 - m.x77)**2 + (m.x134 - m.x156)**2 + (m.x213 - m.x235)**2)**(-3)
    * (((m.x55 - m.x77)**2 + (m.x134 - m.x156)**2 + (m.x213 - m.x235)**2)**(-3)
    - 2) + ((m.x55 - m.x78)**2 + (m.x134 - m.x157)**2 + (m.x213 - m.x236)**2)
    **(-3) * (((m.x55 - m.x78)**2 + (m.x134 - m.x157)**2 + (m.x213 - m.x236)**2)
    **(-3) - 2) + ((m.x55 - m.x79)**2 + (m.x134 - m.x158)**2 + (m.x213 - m.x237)
    **2)**(-3) * (((m.x55 - m.x79)**2 + (m.x134 - m.x158)**2 + (m.x213 - m.x237)
    **2)**(-3) - 2) + ((m.x56 - m.x57)**2 + (m.x135 - m.x136)**2 + (m.x214 -
    m.x215)**2)**(-3) * (((m.x56 - m.x57)**2 + (m.x135 - m.x136)**2 + (m.x214
    - m.x215)**2)**(-3) - 2) + ((m.x56 - m.x58)**2 + (m.x135 - m.x137)**2 + (
    m.x214 - m.x216)**2)**(-3) * (((m.x56 - m.x58)**2 + (m.x135 - m.x137)**2 +
    (m.x214 - m.x216)**2)**(-3) - 2) + ((m.x56 - m.x59)**2 + (m.x135 - m.x138)
    **2 + (m.x214 - m.x217)**2)**(-3) * (((m.x56 - m.x59)**2 + (m.x135 - m.x138)
    **2 + (m.x214 - m.x217)**2)**(-3) - 2) + ((m.x56 - m.x60)**2 + (m.x135 -
    m.x139)**2 + (m.x214 - m.x218)**2)**(-3) * (((m.x56 - m.x60)**2 + (m.x135
    - m.x139)**2 + (m.x214 - m.x218)**2)**(-3) - 2) + ((m.x56 - m.x61)**2 + (
    m.x135 - m.x140)**2 + (m.x214 - m.x219)**2)**(-3) * (((m.x56 - m.x61)**2 +
    (m.x135 - m.x140)**2 + (m.x214 - m.x219)**2)**(-3) - 2) + ((m.x56 - m.x62)
    **2 + (m.x135 - m.x141)**2 + (m.x214 - m.x220)**2)**(-3) * (((m.x56 - m.x62)
    **2 + (m.x135 - m.x141)**2 + (m.x214 - m.x220)**2)**(-3) - 2) + ((m.x56 -
    m.x63)**2 + (m.x135 - m.x142)**2 + (m.x214 - m.x221)**2)**(-3) * (((m.x56
    - m.x63)**2 + (m.x135 - m.x142)**2 + (m.x214 - m.x221)**2)**(-3) - 2) + ((
    m.x56 - m.x64)**2 + (m.x135 - m.x143)**2 + (m.x214 - m.x222)**2)**(-3) * ((
    (m.x56 - m.x64)**2 + (m.x135 - m.x143)**2 + (m.x214 - m.x222)**2)**(-3) - 2)
    + ((m.x56 - m.x65)**2 + (m.x135 - m.x144)**2 + (m.x214 - m.x223)**2)**(-3)
    * (((m.x56 - m.x65)**2 + (m.x135 - m.x144)**2 + (m.x214 - m.x223)**2)**(-3)
    - 2) + ((m.x56 - m.x66)**2 + (m.x135 - m.x145)**2 + (m.x214 - m.x224)**2)
    **(-3) * (((m.x56 - m.x66)**2 + (m.x135 - m.x145)**2 + (m.x214 - m.x224)**2)
    **(-3) - 2) + ((m.x56 - m.x67)**2 + (m.x135 - m.x146)**2 + (m.x214 - m.x225)
    **2)**(-3) * (((m.x56 - m.x67)**2 + (m.x135 - m.x146)**2 + (m.x214 - m.x225)
    **2)**(-3) - 2) + ((m.x56 - m.x68)**2 + (m.x135 - m.x147)**2 + (m.x214 -
    m.x226)**2)**(-3) * (((m.x56 - m.x68)**2 + (m.x135 - m.x147)**2 + (m.x214
    - m.x226)**2)**(-3) - 2) + ((m.x56 - m.x69)**2 + (m.x135 - m.x148)**2 + (
    m.x214 - m.x227)**2)**(-3) * (((m.x56 - m.x69)**2 + (m.x135 - m.x148)**2 +
    (m.x214 - m.x227)**2)**(-3) - 2) + ((m.x56 - m.x70)**2 + (m.x135 - m.x149)
    **2 + (m.x214 - m.x228)**2)**(-3) * (((m.x56 - m.x70)**2 + (m.x135 - m.x149)
    **2 + (m.x214 - m.x228)**2)**(-3) - 2) + ((m.x56 - m.x71)**2 + (m.x135 -
    m.x150)**2 + (m.x214 - m.x229)**2)**(-3) * (((m.x56 - m.x71)**2 + (m.x135
    - m.x150)**2 + (m.x214 - m.x229)**2)**(-3) - 2) + ((m.x56 - m.x72)**2 + (
    m.x135 - m.x151)**2 + (m.x214 - m.x230)**2)**(-3) * (((m.x56 - m.x72)**2 +
    (m.x135 - m.x151)**2 + (m.x214 - m.x230)**2)**(-3) - 2) + ((m.x56 - m.x73)
    **2 + (m.x135 - m.x152)**2 + (m.x214 - m.x231)**2)**(-3) * (((m.x56 - m.x73)
    **2 + (m.x135 - m.x152)**2 + (m.x214 - m.x231)**2)**(-3) - 2) + ((m.x56 -
    m.x74)**2 + (m.x135 - m.x153)**2 + (m.x214 - m.x232)**2)**(-3) * (((m.x56
    - m.x74)**2 + (m.x135 - m.x153)**2 + (m.x214 - m.x232)**2)**(-3) - 2) + ((
    m.x56 - m.x75)**2 + (m.x135 - m.x154)**2 + (m.x214 - m.x233)**2)**(-3) * ((
    (m.x56 - m.x75)**2 + (m.x135 - m.x154)**2 + (m.x214 - m.x233)**2)**(-3) - 2)
    + ((m.x56 - m.x76)**2 + (m.x135 - m.x155)**2 + (m.x214 - m.x234)**2)**(-3)
    * (((m.x56 - m.x76)**2 + (m.x135 - m.x155)**2 + (m.x214 - m.x234)**2)**(-3)
    - 2) + ((m.x56 - m.x77)**2 + (m.x135 - m.x156)**2 + (m.x214 - m.x235)**2)
    **(-3) * (((m.x56 - m.x77)**2 + (m.x135 - m.x156)**2 + (m.x214 - m.x235)**2)
    **(-3) - 2) + ((m.x56 - m.x78)**2 + (m.x135 - m.x157)**2 + (m.x214 - m.x236)
    **2)**(-3) * (((m.x56 - m.x78)**2 + (m.x135 - m.x157)**2 + (m.x214 - m.x236)
    **2)**(-3) - 2) + ((m.x56 - m.x79)**2 + (m.x135 - m.x158)**2 + (m.x214 -
    m.x237)**2)**(-3) * (((m.x56 - m.x79)**2 + (m.x135 - m.x158)**2 + (m.x214
    - m.x237)**2)**(-3) - 2) + ((m.x57 - m.x58)**2 + (m.x136 - m.x137)**2 + (
    m.x215 - m.x216)**2)**(-3) * (((m.x57 - m.x58)**2 + (m.x136 - m.x137)**2 +
    (m.x215 - m.x216)**2)**(-3) - 2) + ((m.x57 - m.x59)**2 + (m.x136 - m.x138)
    **2 + (m.x215 - m.x217)**2)**(-3) * (((m.x57 - m.x59)**2 + (m.x136 - m.x138)
    **2 + (m.x215 - m.x217)**2)**(-3) - 2) + ((m.x57 - m.x60)**2 + (m.x136 -
    m.x139)**2 + (m.x215 - m.x218)**2)**(-3) * (((m.x57 - m.x60)**2 + (m.x136
    - m.x139)**2 + (m.x215 - m.x218)**2)**(-3) - 2) + ((m.x57 - m.x61)**2 + (
    m.x136 - m.x140)**2 + (m.x215 - m.x219)**2)**(-3) * (((m.x57 - m.x61)**2 +
    (m.x136 - m.x140)**2 + (m.x215 - m.x219)**2)**(-3) - 2) + ((m.x57 - m.x62)
    **2 + (m.x136 - m.x141)**2 + (m.x215 - m.x220)**2)**(-3) * (((m.x57 - m.x62)
    **2 + (m.x136 - m.x141)**2 + (m.x215 - m.x220)**2)**(-3) - 2) + ((m.x57 -
    m.x63)**2 + (m.x136 - m.x142)**2 + (m.x215 - m.x221)**2)**(-3) * (((m.x57
    - m.x63)**2 + (m.x136 - m.x142)**2 + (m.x215 - m.x221)**2)**(-3) - 2) + ((
    m.x57 - m.x64)**2 + (m.x136 - m.x143)**2 + (m.x215 - m.x222)**2)**(-3) * ((
    (m.x57 - m.x64)**2 + (m.x136 - m.x143)**2 + (m.x215 - m.x222)**2)**(-3) - 2)
    + ((m.x57 - m.x65)**2 + (m.x136 - m.x144)**2 + (m.x215 - m.x223)**2)**(-3)
    * (((m.x57 - m.x65)**2 + (m.x136 - m.x144)**2 + (m.x215 - m.x223)**2)**(-3)
    - 2) + ((m.x57 - m.x66)**2 + (m.x136 - m.x145)**2 + (m.x215 - m.x224)**2)
    **(-3) * (((m.x57 - m.x66)**2 + (m.x136 - m.x145)**2 + (m.x215 - m.x224)**2)
    **(-3) - 2) + ((m.x57 - m.x67)**2 + (m.x136 - m.x146)**2 + (m.x215 - m.x225)
    **2)**(-3) * (((m.x57 - m.x67)**2 + (m.x136 - m.x146)**2 + (m.x215 - m.x225)
    **2)**(-3) - 2) + ((m.x57 - m.x68)**2 + (m.x136 - m.x147)**2 + (m.x215 -
    m.x226)**2)**(-3) * (((m.x57 - m.x68)**2 + (m.x136 - m.x147)**2 + (m.x215
    - m.x226)**2)**(-3) - 2) + ((m.x57 - m.x69)**2 + (m.x136 - m.x148)**2 + (
    m.x215 - m.x227)**2)**(-3) * (((m.x57 - m.x69)**2 + (m.x136 - m.x148)**2 +
    (m.x215 - m.x227)**2)**(-3) - 2) + ((m.x57 - m.x70)**2 + (m.x136 - m.x149)
    **2 + (m.x215 - m.x228)**2)**(-3) * (((m.x57 - m.x70)**2 + (m.x136 - m.x149)
    **2 + (m.x215 - m.x228)**2)**(-3) - 2) + ((m.x57 - m.x71)**2 + (m.x136 -
    m.x150)**2 + (m.x215 - m.x229)**2)**(-3) * (((m.x57 - m.x71)**2 + (m.x136
    - m.x150)**2 + (m.x215 - m.x229)**2)**(-3) - 2) + ((m.x57 - m.x72)**2 + (
    m.x136 - m.x151)**2 + (m.x215 - m.x230)**2)**(-3) * (((m.x57 - m.x72)**2 +
    (m.x136 - m.x151)**2 + (m.x215 - m.x230)**2)**(-3) - 2) + ((m.x57 - m.x73)
    **2 + (m.x136 - m.x152)**2 + (m.x215 - m.x231)**2)**(-3) * (((m.x57 - m.x73)
    **2 + (m.x136 - m.x152)**2 + (m.x215 - m.x231)**2)**(-3) - 2) + ((m.x57 -
    m.x74)**2 + (m.x136 - m.x153)**2 + (m.x215 - m.x232)**2)**(-3) * (((m.x57
    - m.x74)**2 + (m.x136 - m.x153)**2 + (m.x215 - m.x232)**2)**(-3) - 2) + ((
    m.x57 - m.x75)**2 + (m.x136 - m.x154)**2 + (m.x215 - m.x233)**2)**(-3) * ((
    (m.x57 - m.x75)**2 + (m.x136 - m.x154)**2 + (m.x215 - m.x233)**2)**(-3) - 2)
    + ((m.x57 - m.x76)**2 + (m.x136 - m.x155)**2 + (m.x215 - m.x234)**2)**(-3)
    * (((m.x57 - m.x76)**2 + (m.x136 - m.x155)**2 + (m.x215 - m.x234)**2)**(-3)
    - 2) + ((m.x57 - m.x77)**2 + (m.x136 - m.x156)**2 + (m.x215 - m.x235)**2)
    **(-3) * (((m.x57 - m.x77)**2 + (m.x136 - m.x156)**2 + (m.x215 - m.x235)**2)
    **(-3) - 2) + ((m.x57 - m.x78)**2 + (m.x136 - m.x157)**2 + (m.x215 - m.x236)
    **2)**(-3) * (((m.x57 - m.x78)**2 + (m.x136 - m.x157)**2 + (m.x215 - m.x236)
    **2)**(-3) - 2) + ((m.x57 - m.x79)**2 + (m.x136 - m.x158)**2 + (m.x215 -
    m.x237)**2)**(-3) * (((m.x57 - m.x79)**2 + (m.x136 - m.x158)**2 + (m.x215
    - m.x237)**2)**(-3) - 2) + ((m.x58 - m.x59)**2 + (m.x137 - m.x138)**2 + (
    m.x216 - m.x217)**2)**(-3) * (((m.x58 - m.x59)**2 + (m.x137 - m.x138)**2 +
    (m.x216 - m.x217)**2)**(-3) - 2) + ((m.x58 - m.x60)**2 + (m.x137 - m.x139)
    **2 + (m.x216 - m.x218)**2)**(-3) * (((m.x58 - m.x60)**2 + (m.x137 - m.x139)
    **2 + (m.x216 - m.x218)**2)**(-3) - 2) + ((m.x58 - m.x61)**2 + (m.x137 -
    m.x140)**2 + (m.x216 - m.x219)**2)**(-3) * (((m.x58 - m.x61)**2 + (m.x137
    - m.x140)**2 + (m.x216 - m.x219)**2)**(-3) - 2) + ((m.x58 - m.x62)**2 + (
    m.x137 - m.x141)**2 + (m.x216 - m.x220)**2)**(-3) * (((m.x58 - m.x62)**2 +
    (m.x137 - m.x141)**2 + (m.x216 - m.x220)**2)**(-3) - 2) + ((m.x58 - m.x63)
    **2 + (m.x137 - m.x142)**2 + (m.x216 - m.x221)**2)**(-3) * (((m.x58 - m.x63)
    **2 + (m.x137 - m.x142)**2 + (m.x216 - m.x221)**2)**(-3) - 2) + ((m.x58 -
    m.x64)**2 + (m.x137 - m.x143)**2 + (m.x216 - m.x222)**2)**(-3) * (((m.x58
    - m.x64)**2 + (m.x137 - m.x143)**2 + (m.x216 - m.x222)**2)**(-3) - 2) + ((
    m.x58 - m.x65)**2 + (m.x137 - m.x144)**2 + (m.x216 - m.x223)**2)**(-3) * ((
    (m.x58 - m.x65)**2 + (m.x137 - m.x144)**2 + (m.x216 - m.x223)**2)**(-3) - 2)
    + ((m.x58 - m.x66)**2 + (m.x137 - m.x145)**2 + (m.x216 - m.x224)**2)**(-3)
    * (((m.x58 - m.x66)**2 + (m.x137 - m.x145)**2 + (m.x216 - m.x224)**2)**(-3)
    - 2) + ((m.x58 - m.x67)**2 + (m.x137 - m.x146)**2 + (m.x216 - m.x225)**2)
    **(-3) * (((m.x58 - m.x67)**2 + (m.x137 - m.x146)**2 + (m.x216 - m.x225)**2)
    **(-3) - 2) + ((m.x58 - m.x68)**2 + (m.x137 - m.x147)**2 + (m.x216 - m.x226)
    **2)**(-3) * (((m.x58 - m.x68)**2 + (m.x137 - m.x147)**2 + (m.x216 - m.x226)
    **2)**(-3) - 2) + ((m.x58 - m.x69)**2 + (m.x137 - m.x148)**2 + (m.x216 -
    m.x227)**2)**(-3) * (((m.x58 - m.x69)**2 + (m.x137 - m.x148)**2 + (m.x216
    - m.x227)**2)**(-3) - 2) + ((m.x58 - m.x70)**2 + (m.x137 - m.x149)**2 + (
    m.x216 - m.x228)**2)**(-3) * (((m.x58 - m.x70)**2 + (m.x137 - m.x149)**2 +
    (m.x216 - m.x228)**2)**(-3) - 2) + ((m.x58 - m.x71)**2 + (m.x137 - m.x150)
    **2 + (m.x216 - m.x229)**2)**(-3) * (((m.x58 - m.x71)**2 + (m.x137 - m.x150)
    **2 + (m.x216 - m.x229)**2)**(-3) - 2) + ((m.x58 - m.x72)**2 + (m.x137 -
    m.x151)**2 + (m.x216 - m.x230)**2)**(-3) * (((m.x58 - m.x72)**2 + (m.x137
    - m.x151)**2 + (m.x216 - m.x230)**2)**(-3) - 2) + ((m.x58 - m.x73)**2 + (
    m.x137 - m.x152)**2 + (m.x216 - m.x231)**2)**(-3) * (((m.x58 - m.x73)**2 +
    (m.x137 - m.x152)**2 + (m.x216 - m.x231)**2)**(-3) - 2) + ((m.x58 - m.x74)
    **2 + (m.x137 - m.x153)**2 + (m.x216 - m.x232)**2)**(-3) * (((m.x58 - m.x74)
    **2 + (m.x137 - m.x153)**2 + (m.x216 - m.x232)**2)**(-3) - 2) + ((m.x58 -
    m.x75)**2 + (m.x137 - m.x154)**2 + (m.x216 - m.x233)**2)**(-3) * (((m.x58
    - m.x75)**2 + (m.x137 - m.x154)**2 + (m.x216 - m.x233)**2)**(-3) - 2) + ((
    m.x58 - m.x76)**2 + (m.x137 - m.x155)**2 + (m.x216 - m.x234)**2)**(-3) * ((
    (m.x58 - m.x76)**2 + (m.x137 - m.x155)**2 + (m.x216 - m.x234)**2)**(-3) - 2)
    + ((m.x58 - m.x77)**2 + (m.x137 - m.x156)**2 + (m.x216 - m.x235)**2)**(-3)
    * (((m.x58 - m.x77)**2 + (m.x137 - m.x156)**2 + (m.x216 - m.x235)**2)**(-3)
    - 2) + ((m.x58 - m.x78)**2 + (m.x137 - m.x157)**2 + (m.x216 - m.x236)**2)
    **(-3) * (((m.x58 - m.x78)**2 + (m.x137 - m.x157)**2 + (m.x216 - m.x236)**2)
    **(-3) - 2) + ((m.x58 - m.x79)**2 + (m.x137 - m.x158)**2 + (m.x216 - m.x237)
    **2)**(-3) * (((m.x58 - m.x79)**2 + (m.x137 - m.x158)**2 + (m.x216 - m.x237)
    **2)**(-3) - 2) + ((m.x59 - m.x60)**2 + (m.x138 - m.x139)**2 + (m.x217 -
    m.x218)**2)**(-3) * (((m.x59 - m.x60)**2 + (m.x138 - m.x139)**2 + (m.x217
    - m.x218)**2)**(-3) - 2) + ((m.x59 - m.x61)**2 + (m.x138 - m.x140)**2 + (
    m.x217 - m.x219)**2)**(-3) * (((m.x59 - m.x61)**2 + (m.x138 - m.x140)**2 +
    (m.x217 - m.x219)**2)**(-3) - 2) + ((m.x59 - m.x62)**2 + (m.x138 - m.x141)
    **2 + (m.x217 - m.x220)**2)**(-3) * (((m.x59 - m.x62)**2 + (m.x138 - m.x141)
    **2 + (m.x217 - m.x220)**2)**(-3) - 2) + ((m.x59 - m.x63)**2 + (m.x138 -
    m.x142)**2 + (m.x217 - m.x221)**2)**(-3) * (((m.x59 - m.x63)**2 + (m.x138
    - m.x142)**2 + (m.x217 - m.x221)**2)**(-3) - 2) + ((m.x59 - m.x64)**2 + (
    m.x138 - m.x143)**2 + (m.x217 - m.x222)**2)**(-3) * (((m.x59 - m.x64)**2 +
    (m.x138 - m.x143)**2 + (m.x217 - m.x222)**2)**(-3) - 2) + ((m.x59 - m.x65)
    **2 + (m.x138 - m.x144)**2 + (m.x217 - m.x223)**2)**(-3) * (((m.x59 - m.x65)
    **2 + (m.x138 - m.x144)**2 + (m.x217 - m.x223)**2)**(-3) - 2) + ((m.x59 -
    m.x66)**2 + (m.x138 - m.x145)**2 + (m.x217 - m.x224)**2)**(-3) * (((m.x59
    - m.x66)**2 + (m.x138 - m.x145)**2 + (m.x217 - m.x224)**2)**(-3) - 2) + ((
    m.x59 - m.x67)**2 + (m.x138 - m.x146)**2 + (m.x217 - m.x225)**2)**(-3) * ((
    (m.x59 - m.x67)**2 + (m.x138 - m.x146)**2 + (m.x217 - m.x225)**2)**(-3) - 2)
    + ((m.x59 - m.x68)**2 + (m.x138 - m.x147)**2 + (m.x217 - m.x226)**2)**(-3)
    * (((m.x59 - m.x68)**2 + (m.x138 - m.x147)**2 + (m.x217 - m.x226)**2)**(-3)
    - 2) + ((m.x59 - m.x69)**2 + (m.x138 - m.x148)**2 + (m.x217 - m.x227)**2)
    **(-3) * (((m.x59 - m.x69)**2 + (m.x138 - m.x148)**2 + (m.x217 - m.x227)**2)
    **(-3) - 2) + ((m.x59 - m.x70)**2 + (m.x138 - m.x149)**2 + (m.x217 - m.x228)
    **2)**(-3) * (((m.x59 - m.x70)**2 + (m.x138 - m.x149)**2 + (m.x217 - m.x228)
    **2)**(-3) - 2) + ((m.x59 - m.x71)**2 + (m.x138 - m.x150)**2 + (m.x217 -
    m.x229)**2)**(-3) * (((m.x59 - m.x71)**2 + (m.x138 - m.x150)**2 + (m.x217
    - m.x229)**2)**(-3) - 2) + ((m.x59 - m.x72)**2 + (m.x138 - m.x151)**2 + (
    m.x217 - m.x230)**2)**(-3) * (((m.x59 - m.x72)**2 + (m.x138 - m.x151)**2 +
    (m.x217 - m.x230)**2)**(-3) - 2) + ((m.x59 - m.x73)**2 + (m.x138 - m.x152)
    **2 + (m.x217 - m.x231)**2)**(-3) * (((m.x59 - m.x73)**2 + (m.x138 - m.x152)
    **2 + (m.x217 - m.x231)**2)**(-3) - 2) + ((m.x59 - m.x74)**2 + (m.x138 -
    m.x153)**2 + (m.x217 - m.x232)**2)**(-3) * (((m.x59 - m.x74)**2 + (m.x138
    - m.x153)**2 + (m.x217 - m.x232)**2)**(-3) - 2) + ((m.x59 - m.x75)**2 + (
    m.x138 - m.x154)**2 + (m.x217 - m.x233)**2)**(-3) * (((m.x59 - m.x75)**2 +
    (m.x138 - m.x154)**2 + (m.x217 - m.x233)**2)**(-3) - 2) + ((m.x59 - m.x76)
    **2 + (m.x138 - m.x155)**2 + (m.x217 - m.x234)**2)**(-3) * (((m.x59 - m.x76)
    **2 + (m.x138 - m.x155)**2 + (m.x217 - m.x234)**2)**(-3) - 2) + ((m.x59 -
    m.x77)**2 + (m.x138 - m.x156)**2 + (m.x217 - m.x235)**2)**(-3) * (((m.x59
    - m.x77)**2 + (m.x138 - m.x156)**2 + (m.x217 - m.x235)**2)**(-3) - 2) + ((
    m.x59 - m.x78)**2 + (m.x138 - m.x157)**2 + (m.x217 - m.x236)**2)**(-3) * ((
    (m.x59 - m.x78)**2 + (m.x138 - m.x157)**2 + (m.x217 - m.x236)**2)**(-3) - 2)
    + ((m.x59 - m.x79)**2 + (m.x138 - m.x158)**2 + (m.x217 - m.x237)**2)**(-3)
    * (((m.x59 - m.x79)**2 + (m.x138 - m.x158)**2 + (m.x217 - m.x237)**2)**(-3)
    - 2) + ((m.x60 - m.x61)**2 + (m.x139 - m.x140)**2 + (m.x218 - m.x219)**2)
    **(-3) * (((m.x60 - m.x61)**2 + (m.x139 - m.x140)**2 + (m.x218 - m.x219)**2)
    **(-3) - 2) + ((m.x60 - m.x62)**2 + (m.x139 - m.x141)**2 + (m.x218 - m.x220)
    **2)**(-3) * (((m.x60 - m.x62)**2 + (m.x139 - m.x141)**2 + (m.x218 - m.x220)
    **2)**(-3) - 2) + ((m.x60 - m.x63)**2 + (m.x139 - m.x142)**2 + (m.x218 -
    m.x221)**2)**(-3) * (((m.x60 - m.x63)**2 + (m.x139 - m.x142)**2 + (m.x218
    - m.x221)**2)**(-3) - 2) + ((m.x60 - m.x64)**2 + (m.x139 - m.x143)**2 + (
    m.x218 - m.x222)**2)**(-3) * (((m.x60 - m.x64)**2 + (m.x139 - m.x143)**2 +
    (m.x218 - m.x222)**2)**(-3) - 2) + ((m.x60 - m.x65)**2 + (m.x139 - m.x144)
    **2 + (m.x218 - m.x223)**2)**(-3) * (((m.x60 - m.x65)**2 + (m.x139 - m.x144)
    **2 + (m.x218 - m.x223)**2)**(-3) - 2) + ((m.x60 - m.x66)**2 + (m.x139 -
    m.x145)**2 + (m.x218 - m.x224)**2)**(-3) * (((m.x60 - m.x66)**2 + (m.x139
    - m.x145)**2 + (m.x218 - m.x224)**2)**(-3) - 2) + ((m.x60 - m.x67)**2 + (
    m.x139 - m.x146)**2 + (m.x218 - m.x225)**2)**(-3) * (((m.x60 - m.x67)**2 +
    (m.x139 - m.x146)**2 + (m.x218 - m.x225)**2)**(-3) - 2) + ((m.x60 - m.x68)
    **2 + (m.x139 - m.x147)**2 + (m.x218 - m.x226)**2)**(-3) * (((m.x60 - m.x68)
    **2 + (m.x139 - m.x147)**2 + (m.x218 - m.x226)**2)**(-3) - 2) + ((m.x60 -
    m.x69)**2 + (m.x139 - m.x148)**2 + (m.x218 - m.x227)**2)**(-3) * (((m.x60
    - m.x69)**2 + (m.x139 - m.x148)**2 + (m.x218 - m.x227)**2)**(-3) - 2) + ((
    m.x60 - m.x70)**2 + (m.x139 - m.x149)**2 + (m.x218 - m.x228)**2)**(-3) * ((
    (m.x60 - m.x70)**2 + (m.x139 - m.x149)**2 + (m.x218 - m.x228)**2)**(-3) - 2)
    + ((m.x60 - m.x71)**2 + (m.x139 - m.x150)**2 + (m.x218 - m.x229)**2)**(-3)
    * (((m.x60 - m.x71)**2 + (m.x139 - m.x150)**2 + (m.x218 - m.x229)**2)**(-3)
    - 2) + ((m.x60 - m.x72)**2 + (m.x139 - m.x151)**2 + (m.x218 - m.x230)**2)
    **(-3) * (((m.x60 - m.x72)**2 + (m.x139 - m.x151)**2 + (m.x218 - m.x230)**2)
    **(-3) - 2) + ((m.x60 - m.x73)**2 + (m.x139 - m.x152)**2 + (m.x218 - m.x231)
    **2)**(-3) * (((m.x60 - m.x73)**2 + (m.x139 - m.x152)**2 + (m.x218 - m.x231)
    **2)**(-3) - 2) + ((m.x60 - m.x74)**2 + (m.x139 - m.x153)**2 + (m.x218 -
    m.x232)**2)**(-3) * (((m.x60 - m.x74)**2 + (m.x139 - m.x153)**2 + (m.x218
    - m.x232)**2)**(-3) - 2) + ((m.x60 - m.x75)**2 + (m.x139 - m.x154)**2 + (
    m.x218 - m.x233)**2)**(-3) * (((m.x60 - m.x75)**2 + (m.x139 - m.x154)**2 +
    (m.x218 - m.x233)**2)**(-3) - 2) + ((m.x60 - m.x76)**2 + (m.x139 - m.x155)
    **2 + (m.x218 - m.x234)**2)**(-3) * (((m.x60 - m.x76)**2 + (m.x139 - m.x155)
    **2 + (m.x218 - m.x234)**2)**(-3) - 2) + ((m.x60 - m.x77)**2 + (m.x139 -
    m.x156)**2 + (m.x218 - m.x235)**2)**(-3) * (((m.x60 - m.x77)**2 + (m.x139
    - m.x156)**2 + (m.x218 - m.x235)**2)**(-3) - 2) + ((m.x60 - m.x78)**2 + (
    m.x139 - m.x157)**2 + (m.x218 - m.x236)**2)**(-3) * (((m.x60 - m.x78)**2 +
    (m.x139 - m.x157)**2 + (m.x218 - m.x236)**2)**(-3) - 2) + ((m.x60 - m.x79)
    **2 + (m.x139 - m.x158)**2 + (m.x218 - m.x237)**2)**(-3) * (((m.x60 - m.x79)
    **2 + (m.x139 - m.x158)**2 + (m.x218 - m.x237)**2)**(-3) - 2) + ((m.x61 -
    m.x62)**2 + (m.x140 - m.x141)**2 + (m.x219 - m.x220)**2)**(-3) * (((m.x61
    - m.x62)**2 + (m.x140 - m.x141)**2 + (m.x219 - m.x220)**2)**(-3) - 2) + ((
    m.x61 - m.x63)**2 + (m.x140 - m.x142)**2 + (m.x219 - m.x221)**2)**(-3) * ((
    (m.x61 - m.x63)**2 + (m.x140 - m.x142)**2 + (m.x219 - m.x221)**2)**(-3) - 2)
    + ((m.x61 - m.x64)**2 + (m.x140 - m.x143)**2 + (m.x219 - m.x222)**2)**(-3)
    * (((m.x61 - m.x64)**2 + (m.x140 - m.x143)**2 + (m.x219 - m.x222)**2)**(-3)
    - 2) + ((m.x61 - m.x65)**2 + (m.x140 - m.x144)**2 + (m.x219 - m.x223)**2)
    **(-3) * (((m.x61 - m.x65)**2 + (m.x140 - m.x144)**2 + (m.x219 - m.x223)**2)
    **(-3) - 2) + ((m.x61 - m.x66)**2 + (m.x140 - m.x145)**2 + (m.x219 - m.x224)
    **2)**(-3) * (((m.x61 - m.x66)**2 + (m.x140 - m.x145)**2 + (m.x219 - m.x224)
    **2)**(-3) - 2) + ((m.x61 - m.x67)**2 + (m.x140 - m.x146)**2 + (m.x219 -
    m.x225)**2)**(-3) * (((m.x61 - m.x67)**2 + (m.x140 - m.x146)**2 + (m.x219
    - m.x225)**2)**(-3) - 2) + ((m.x61 - m.x68)**2 + (m.x140 - m.x147)**2 + (
    m.x219 - m.x226)**2)**(-3) * (((m.x61 - m.x68)**2 + (m.x140 - m.x147)**2 +
    (m.x219 - m.x226)**2)**(-3) - 2) + ((m.x61 - m.x69)**2 + (m.x140 - m.x148)
    **2 + (m.x219 - m.x227)**2)**(-3) * (((m.x61 - m.x69)**2 + (m.x140 - m.x148)
    **2 + (m.x219 - m.x227)**2)**(-3) - 2) + ((m.x61 - m.x70)**2 + (m.x140 -
    m.x149)**2 + (m.x219 - m.x228)**2)**(-3) * (((m.x61 - m.x70)**2 + (m.x140
    - m.x149)**2 + (m.x219 - m.x228)**2)**(-3) - 2) + ((m.x61 - m.x71)**2 + (
    m.x140 - m.x150)**2 + (m.x219 - m.x229)**2)**(-3) * (((m.x61 - m.x71)**2 +
    (m.x140 - m.x150)**2 + (m.x219 - m.x229)**2)**(-3) - 2) + ((m.x61 - m.x72)
    **2 + (m.x140 - m.x151)**2 + (m.x219 - m.x230)**2)**(-3) * (((m.x61 - m.x72)
    **2 + (m.x140 - m.x151)**2 + (m.x219 - m.x230)**2)**(-3) - 2) + ((m.x61 -
    m.x73)**2 + (m.x140 - m.x152)**2 + (m.x219 - m.x231)**2)**(-3) * (((m.x61
    - m.x73)**2 + (m.x140 - m.x152)**2 + (m.x219 - m.x231)**2)**(-3) - 2) + ((
    m.x61 - m.x74)**2 + (m.x140 - m.x153)**2 + (m.x219 - m.x232)**2)**(-3) * ((
    (m.x61 - m.x74)**2 + (m.x140 - m.x153)**2 + (m.x219 - m.x232)**2)**(-3) - 2)
    + ((m.x61 - m.x75)**2 + (m.x140 - m.x154)**2 + (m.x219 - m.x233)**2)**(-3)
    * (((m.x61 - m.x75)**2 + (m.x140 - m.x154)**2 + (m.x219 - m.x233)**2)**(-3)
    - 2) + ((m.x61 - m.x76)**2 + (m.x140 - m.x155)**2 + (m.x219 - m.x234)**2)
    **(-3) * (((m.x61 - m.x76)**2 + (m.x140 - m.x155)**2 + (m.x219 - m.x234)**2)
    **(-3) - 2) + ((m.x61 - m.x77)**2 + (m.x140 - m.x156)**2 + (m.x219 - m.x235)
    **2)**(-3) * (((m.x61 - m.x77)**2 + (m.x140 - m.x156)**2 + (m.x219 - m.x235)
    **2)**(-3) - 2) + ((m.x61 - m.x78)**2 + (m.x140 - m.x157)**2 + (m.x219 -
    m.x236)**2)**(-3) * (((m.x61 - m.x78)**2 + (m.x140 - m.x157)**2 + (m.x219
    - m.x236)**2)**(-3) - 2) + ((m.x61 - m.x79)**2 + (m.x140 - m.x158)**2 + (
    m.x219 - m.x237)**2)**(-3) * (((m.x61 - m.x79)**2 + (m.x140 - m.x158)**2 +
    (m.x219 - m.x237)**2)**(-3) - 2) + ((m.x62 - m.x63)**2 + (m.x141 - m.x142)
    **2 + (m.x220 - m.x221)**2)**(-3) * (((m.x62 - m.x63)**2 + (m.x141 - m.x142)
    **2 + (m.x220 - m.x221)**2)**(-3) - 2) + ((m.x62 - m.x64)**2 + (m.x141 -
    m.x143)**2 + (m.x220 - m.x222)**2)**(-3) * (((m.x62 - m.x64)**2 + (m.x141
    - m.x143)**2 + (m.x220 - m.x222)**2)**(-3) - 2) + ((m.x62 - m.x65)**2 + (
    m.x141 - m.x144)**2 + (m.x220 - m.x223)**2)**(-3) * (((m.x62 - m.x65)**2 +
    (m.x141 - m.x144)**2 + (m.x220 - m.x223)**2)**(-3) - 2) + ((m.x62 - m.x66)
    **2 + (m.x141 - m.x145)**2 + (m.x220 - m.x224)**2)**(-3) * (((m.x62 - m.x66)
    **2 + (m.x141 - m.x145)**2 + (m.x220 - m.x224)**2)**(-3) - 2) + ((m.x62 -
    m.x67)**2 + (m.x141 - m.x146)**2 + (m.x220 - m.x225)**2)**(-3) * (((m.x62
    - m.x67)**2 + (m.x141 - m.x146)**2 + (m.x220 - m.x225)**2)**(-3) - 2) + ((
    m.x62 - m.x68)**2 + (m.x141 - m.x147)**2 + (m.x220 - m.x226)**2)**(-3) * ((
    (m.x62 - m.x68)**2 + (m.x141 - m.x147)**2 + (m.x220 - m.x226)**2)**(-3) - 2)
    + ((m.x62 - m.x69)**2 + (m.x141 - m.x148)**2 + (m.x220 - m.x227)**2)**(-3)
    * (((m.x62 - m.x69)**2 + (m.x141 - m.x148)**2 + (m.x220 - m.x227)**2)**(-3)
    - 2) + ((m.x62 - m.x70)**2 + (m.x141 - m.x149)**2 + (m.x220 - m.x228)**2)
    **(-3) * (((m.x62 - m.x70)**2 + (m.x141 - m.x149)**2 + (m.x220 - m.x228)**2)
    **(-3) - 2) + ((m.x62 - m.x71)**2 + (m.x141 - m.x150)**2 + (m.x220 - m.x229)
    **2)**(-3) * (((m.x62 - m.x71)**2 + (m.x141 - m.x150)**2 + (m.x220 - m.x229)
    **2)**(-3) - 2) + ((m.x62 - m.x72)**2 + (m.x141 - m.x151)**2 + (m.x220 -
    m.x230)**2)**(-3) * (((m.x62 - m.x72)**2 + (m.x141 - m.x151)**2 + (m.x220
    - m.x230)**2)**(-3) - 2) + ((m.x62 - m.x73)**2 + (m.x141 - m.x152)**2 + (
    m.x220 - m.x231)**2)**(-3) * (((m.x62 - m.x73)**2 + (m.x141 - m.x152)**2 +
    (m.x220 - m.x231)**2)**(-3) - 2) + ((m.x62 - m.x74)**2 + (m.x141 - m.x153)
    **2 + (m.x220 - m.x232)**2)**(-3) * (((m.x62 - m.x74)**2 + (m.x141 - m.x153)
    **2 + (m.x220 - m.x232)**2)**(-3) - 2) + ((m.x62 - m.x75)**2 + (m.x141 -
    m.x154)**2 + (m.x220 - m.x233)**2)**(-3) * (((m.x62 - m.x75)**2 + (m.x141
    - m.x154)**2 + (m.x220 - m.x233)**2)**(-3) - 2) + ((m.x62 - m.x76)**2 + (
    m.x141 - m.x155)**2 + (m.x220 - m.x234)**2)**(-3) * (((m.x62 - m.x76)**2 +
    (m.x141 - m.x155)**2 + (m.x220 - m.x234)**2)**(-3) - 2) + ((m.x62 - m.x77)
    **2 + (m.x141 - m.x156)**2 + (m.x220 - m.x235)**2)**(-3) * (((m.x62 - m.x77)
    **2 + (m.x141 - m.x156)**2 + (m.x220 - m.x235)**2)**(-3) - 2) + ((m.x62 -
    m.x78)**2 + (m.x141 - m.x157)**2 + (m.x220 - m.x236)**2)**(-3) * (((m.x62
    - m.x78)**2 + (m.x141 - m.x157)**2 + (m.x220 - m.x236)**2)**(-3) - 2) + ((
    m.x62 - m.x79)**2 + (m.x141 - m.x158)**2 + (m.x220 - m.x237)**2)**(-3) * ((
    (m.x62 - m.x79)**2 + (m.x141 - m.x158)**2 + (m.x220 - m.x237)**2)**(-3) - 2)
    + ((m.x63 - m.x64)**2 + (m.x142 - m.x143)**2 + (m.x221 - m.x222)**2)**(-3)
    * (((m.x63 - m.x64)**2 + (m.x142 - m.x143)**2 + (m.x221 - m.x222)**2)**(-3)
    - 2) + ((m.x63 - m.x65)**2 + (m.x142 - m.x144)**2 + (m.x221 - m.x223)**2)
    **(-3) * (((m.x63 - m.x65)**2 + (m.x142 - m.x144)**2 + (m.x221 - m.x223)**2)
    **(-3) - 2) + ((m.x63 - m.x66)**2 + (m.x142 - m.x145)**2 + (m.x221 - m.x224)
    **2)**(-3) * (((m.x63 - m.x66)**2 + (m.x142 - m.x145)**2 + (m.x221 - m.x224)
    **2)**(-3) - 2) + ((m.x63 - m.x67)**2 + (m.x142 - m.x146)**2 + (m.x221 -
    m.x225)**2)**(-3) * (((m.x63 - m.x67)**2 + (m.x142 - m.x146)**2 + (m.x221
    - m.x225)**2)**(-3) - 2) + ((m.x63 - m.x68)**2 + (m.x142 - m.x147)**2 + (
    m.x221 - m.x226)**2)**(-3) * (((m.x63 - m.x68)**2 + (m.x142 - m.x147)**2 +
    (m.x221 - m.x226)**2)**(-3) - 2) + ((m.x63 - m.x69)**2 + (m.x142 - m.x148)
    **2 + (m.x221 - m.x227)**2)**(-3) * (((m.x63 - m.x69)**2 + (m.x142 - m.x148)
    **2 + (m.x221 - m.x227)**2)**(-3) - 2) + ((m.x63 - m.x70)**2 + (m.x142 -
    m.x149)**2 + (m.x221 - m.x228)**2)**(-3) * (((m.x63 - m.x70)**2 + (m.x142
    - m.x149)**2 + (m.x221 - m.x228)**2)**(-3) - 2) + ((m.x63 - m.x71)**2 + (
    m.x142 - m.x150)**2 + (m.x221 - m.x229)**2)**(-3) * (((m.x63 - m.x71)**2 +
    (m.x142 - m.x150)**2 + (m.x221 - m.x229)**2)**(-3) - 2) + ((m.x63 - m.x72)
    **2 + (m.x142 - m.x151)**2 + (m.x221 - m.x230)**2)**(-3) * (((m.x63 - m.x72)
    **2 + (m.x142 - m.x151)**2 + (m.x221 - m.x230)**2)**(-3) - 2) + ((m.x63 -
    m.x73)**2 + (m.x142 - m.x152)**2 + (m.x221 - m.x231)**2)**(-3) * (((m.x63
    - m.x73)**2 + (m.x142 - m.x152)**2 + (m.x221 - m.x231)**2)**(-3) - 2) + ((
    m.x63 - m.x74)**2 + (m.x142 - m.x153)**2 + (m.x221 - m.x232)**2)**(-3) * ((
    (m.x63 - m.x74)**2 + (m.x142 - m.x153)**2 + (m.x221 - m.x232)**2)**(-3) - 2)
    + ((m.x63 - m.x75)**2 + (m.x142 - m.x154)**2 + (m.x221 - m.x233)**2)**(-3)
    * (((m.x63 - m.x75)**2 + (m.x142 - m.x154)**2 + (m.x221 - m.x233)**2)**(-3)
    - 2) + ((m.x63 - m.x76)**2 + (m.x142 - m.x155)**2 + (m.x221 - m.x234)**2)
    **(-3) * (((m.x63 - m.x76)**2 + (m.x142 - m.x155)**2 + (m.x221 - m.x234)**2)
    **(-3) - 2) + ((m.x63 - m.x77)**2 + (m.x142 - m.x156)**2 + (m.x221 - m.x235)
    **2)**(-3) * (((m.x63 - m.x77)**2 + (m.x142 - m.x156)**2 + (m.x221 - m.x235)
    **2)**(-3) - 2) + ((m.x63 - m.x78)**2 + (m.x142 - m.x157)**2 + (m.x221 -
    m.x236)**2)**(-3) * (((m.x63 - m.x78)**2 + (m.x142 - m.x157)**2 + (m.x221
    - m.x236)**2)**(-3) - 2) + ((m.x63 - m.x79)**2 + (m.x142 - m.x158)**2 + (
    m.x221 - m.x237)**2)**(-3) * (((m.x63 - m.x79)**2 + (m.x142 - m.x158)**2 +
    (m.x221 - m.x237)**2)**(-3) - 2) + ((m.x64 - m.x65)**2 + (m.x143 - m.x144)
    **2 + (m.x222 - m.x223)**2)**(-3) * (((m.x64 - m.x65)**2 + (m.x143 - m.x144)
    **2 + (m.x222 - m.x223)**2)**(-3) - 2) + ((m.x64 - m.x66)**2 + (m.x143 -
    m.x145)**2 + (m.x222 - m.x224)**2)**(-3) * (((m.x64 - m.x66)**2 + (m.x143
    - m.x145)**2 + (m.x222 - m.x224)**2)**(-3) - 2) + ((m.x64 - m.x67)**2 + (
    m.x143 - m.x146)**2 + (m.x222 - m.x225)**2)**(-3) * (((m.x64 - m.x67)**2 +
    (m.x143 - m.x146)**2 + (m.x222 - m.x225)**2)**(-3) - 2) + ((m.x64 - m.x68)
    **2 + (m.x143 - m.x147)**2 + (m.x222 - m.x226)**2)**(-3) * (((m.x64 - m.x68)
    **2 + (m.x143 - m.x147)**2 + (m.x222 - m.x226)**2)**(-3) - 2) + ((m.x64 -
    m.x69)**2 + (m.x143 - m.x148)**2 + (m.x222 - m.x227)**2)**(-3) * (((m.x64
    - m.x69)**2 + (m.x143 - m.x148)**2 + (m.x222 - m.x227)**2)**(-3) - 2) + ((
    m.x64 - m.x70)**2 + (m.x143 - m.x149)**2 + (m.x222 - m.x228)**2)**(-3) * ((
    (m.x64 - m.x70)**2 + (m.x143 - m.x149)**2 + (m.x222 - m.x228)**2)**(-3) - 2)
    + ((m.x64 - m.x71)**2 + (m.x143 - m.x150)**2 + (m.x222 - m.x229)**2)**(-3)
    * (((m.x64 - m.x71)**2 + (m.x143 - m.x150)**2 + (m.x222 - m.x229)**2)**(-3)
    - 2) + ((m.x64 - m.x72)**2 + (m.x143 - m.x151)**2 + (m.x222 - m.x230)**2)
    **(-3) * (((m.x64 - m.x72)**2 + (m.x143 - m.x151)**2 + (m.x222 - m.x230)**2)
    **(-3) - 2) + ((m.x64 - m.x73)**2 + (m.x143 - m.x152)**2 + (m.x222 - m.x231)
    **2)**(-3) * (((m.x64 - m.x73)**2 + (m.x143 - m.x152)**2 + (m.x222 - m.x231)
    **2)**(-3) - 2) + ((m.x64 - m.x74)**2 + (m.x143 - m.x153)**2 + (m.x222 -
    m.x232)**2)**(-3) * (((m.x64 - m.x74)**2 + (m.x143 - m.x153)**2 + (m.x222
    - m.x232)**2)**(-3) - 2) + ((m.x64 - m.x75)**2 + (m.x143 - m.x154)**2 + (
    m.x222 - m.x233)**2)**(-3) * (((m.x64 - m.x75)**2 + (m.x143 - m.x154)**2 +
    (m.x222 - m.x233)**2)**(-3) - 2) + ((m.x64 - m.x76)**2 + (m.x143 - m.x155)
    **2 + (m.x222 - m.x234)**2)**(-3) * (((m.x64 - m.x76)**2 + (m.x143 - m.x155)
    **2 + (m.x222 - m.x234)**2)**(-3) - 2) + ((m.x64 - m.x77)**2 + (m.x143 -
    m.x156)**2 + (m.x222 - m.x235)**2)**(-3) * (((m.x64 - m.x77)**2 + (m.x143
    - m.x156)**2 + (m.x222 - m.x235)**2)**(-3) - 2) + ((m.x64 - m.x78)**2 + (
    m.x143 - m.x157)**2 + (m.x222 - m.x236)**2)**(-3) * (((m.x64 - m.x78)**2 +
    (m.x143 - m.x157)**2 + (m.x222 - m.x236)**2)**(-3) - 2) + ((m.x64 - m.x79)
    **2 + (m.x143 - m.x158)**2 + (m.x222 - m.x237)**2)**(-3) * (((m.x64 - m.x79)
    **2 + (m.x143 - m.x158)**2 + (m.x222 - m.x237)**2)**(-3) - 2) + ((m.x65 -
    m.x66)**2 + (m.x144 - m.x145)**2 + (m.x223 - m.x224)**2)**(-3) * (((m.x65
    - m.x66)**2 + (m.x144 - m.x145)**2 + (m.x223 - m.x224)**2)**(-3) - 2) + ((
    m.x65 - m.x67)**2 + (m.x144 - m.x146)**2 + (m.x223 - m.x225)**2)**(-3) * ((
    (m.x65 - m.x67)**2 + (m.x144 - m.x146)**2 + (m.x223 - m.x225)**2)**(-3) - 2)
    + ((m.x65 - m.x68)**2 + (m.x144 - m.x147)**2 + (m.x223 - m.x226)**2)**(-3)
    * (((m.x65 - m.x68)**2 + (m.x144 - m.x147)**2 + (m.x223 - m.x226)**2)**(-3)
    - 2) + ((m.x65 - m.x69)**2 + (m.x144 - m.x148)**2 + (m.x223 - m.x227)**2)
    **(-3) * (((m.x65 - m.x69)**2 + (m.x144 - m.x148)**2 + (m.x223 - m.x227)**2)
    **(-3) - 2) + ((m.x65 - m.x70)**2 + (m.x144 - m.x149)**2 + (m.x223 - m.x228)
    **2)**(-3) * (((m.x65 - m.x70)**2 + (m.x144 - m.x149)**2 + (m.x223 - m.x228)
    **2)**(-3) - 2) + ((m.x65 - m.x71)**2 + (m.x144 - m.x150)**2 + (m.x223 -
    m.x229)**2)**(-3) * (((m.x65 - m.x71)**2 + (m.x144 - m.x150)**2 + (m.x223
    - m.x229)**2)**(-3) - 2) + ((m.x65 - m.x72)**2 + (m.x144 - m.x151)**2 + (
    m.x223 - m.x230)**2)**(-3) * (((m.x65 - m.x72)**2 + (m.x144 - m.x151)**2 +
    (m.x223 - m.x230)**2)**(-3) - 2) + ((m.x65 - m.x73)**2 + (m.x144 - m.x152)
    **2 + (m.x223 - m.x231)**2)**(-3) * (((m.x65 - m.x73)**2 + (m.x144 - m.x152)
    **2 + (m.x223 - m.x231)**2)**(-3) - 2) + ((m.x65 - m.x74)**2 + (m.x144 -
    m.x153)**2 + (m.x223 - m.x232)**2)**(-3) * (((m.x65 - m.x74)**2 + (m.x144
    - m.x153)**2 + (m.x223 - m.x232)**2)**(-3) - 2) + ((m.x65 - m.x75)**2 + (
    m.x144 - m.x154)**2 + (m.x223 - m.x233)**2)**(-3) * (((m.x65 - m.x75)**2 +
    (m.x144 - m.x154)**2 + (m.x223 - m.x233)**2)**(-3) - 2) + ((m.x65 - m.x76)
    **2 + (m.x144 - m.x155)**2 + (m.x223 - m.x234)**2)**(-3) * (((m.x65 - m.x76)
    **2 + (m.x144 - m.x155)**2 + (m.x223 - m.x234)**2)**(-3) - 2) + ((m.x65 -
    m.x77)**2 + (m.x144 - m.x156)**2 + (m.x223 - m.x235)**2)**(-3) * (((m.x65
    - m.x77)**2 + (m.x144 - m.x156)**2 + (m.x223 - m.x235)**2)**(-3) - 2) + ((
    m.x65 - m.x78)**2 + (m.x144 - m.x157)**2 + (m.x223 - m.x236)**2)**(-3) * ((
    (m.x65 - m.x78)**2 + (m.x144 - m.x157)**2 + (m.x223 - m.x236)**2)**(-3) - 2)
    + ((m.x65 - m.x79)**2 + (m.x144 - m.x158)**2 + (m.x223 - m.x237)**2)**(-3)
    * (((m.x65 - m.x79)**2 + (m.x144 - m.x158)**2 + (m.x223 - m.x237)**2)**(-3)
    - 2) + ((m.x66 - m.x67)**2 + (m.x145 - m.x146)**2 + (m.x224 - m.x225)**2)
    **(-3) * (((m.x66 - m.x67)**2 + (m.x145 - m.x146)**2 + (m.x224 - m.x225)**2)
    **(-3) - 2) + ((m.x66 - m.x68)**2 + (m.x145 - m.x147)**2 + (m.x224 - m.x226)
    **2)**(-3) * (((m.x66 - m.x68)**2 + (m.x145 - m.x147)**2 + (m.x224 - m.x226)
    **2)**(-3) - 2) + ((m.x66 - m.x69)**2 + (m.x145 - m.x148)**2 + (m.x224 -
    m.x227)**2)**(-3) * (((m.x66 - m.x69)**2 + (m.x145 - m.x148)**2 + (m.x224
    - m.x227)**2)**(-3) - 2) + ((m.x66 - m.x70)**2 + (m.x145 - m.x149)**2 + (
    m.x224 - m.x228)**2)**(-3) * (((m.x66 - m.x70)**2 + (m.x145 - m.x149)**2 +
    (m.x224 - m.x228)**2)**(-3) - 2) + ((m.x66 - m.x71)**2 + (m.x145 - m.x150)
    **2 + (m.x224 - m.x229)**2)**(-3) * (((m.x66 - m.x71)**2 + (m.x145 - m.x150)
    **2 + (m.x224 - m.x229)**2)**(-3) - 2) + ((m.x66 - m.x72)**2 + (m.x145 -
    m.x151)**2 + (m.x224 - m.x230)**2)**(-3) * (((m.x66 - m.x72)**2 + (m.x145
    - m.x151)**2 + (m.x224 - m.x230)**2)**(-3) - 2) + ((m.x66 - m.x73)**2 + (
    m.x145 - m.x152)**2 + (m.x224 - m.x231)**2)**(-3) * (((m.x66 - m.x73)**2 +
    (m.x145 - m.x152)**2 + (m.x224 - m.x231)**2)**(-3) - 2) + ((m.x66 - m.x74)
    **2 + (m.x145 - m.x153)**2 + (m.x224 - m.x232)**2)**(-3) * (((m.x66 - m.x74)
    **2 + (m.x145 - m.x153)**2 + (m.x224 - m.x232)**2)**(-3) - 2) + ((m.x66 -
    m.x75)**2 + (m.x145 - m.x154)**2 + (m.x224 - m.x233)**2)**(-3) * (((m.x66
    - m.x75)**2 + (m.x145 - m.x154)**2 + (m.x224 - m.x233)**2)**(-3) - 2) + ((
    m.x66 - m.x76)**2 + (m.x145 - m.x155)**2 + (m.x224 - m.x234)**2)**(-3) * ((
    (m.x66 - m.x76)**2 + (m.x145 - m.x155)**2 + (m.x224 - m.x234)**2)**(-3) - 2)
    + ((m.x66 - m.x77)**2 + (m.x145 - m.x156)**2 + (m.x224 - m.x235)**2)**(-3)
    * (((m.x66 - m.x77)**2 + (m.x145 - m.x156)**2 + (m.x224 - m.x235)**2)**(-3)
    - 2) + ((m.x66 - m.x78)**2 + (m.x145 - m.x157)**2 + (m.x224 - m.x236)**2)
    **(-3) * (((m.x66 - m.x78)**2 + (m.x145 - m.x157)**2 + (m.x224 - m.x236)**2)
    **(-3) - 2) + ((m.x66 - m.x79)**2 + (m.x145 - m.x158)**2 + (m.x224 - m.x237)
    **2)**(-3) * (((m.x66 - m.x79)**2 + (m.x145 - m.x158)**2 + (m.x224 - m.x237)
    **2)**(-3) - 2) + ((m.x67 - m.x68)**2 + (m.x146 - m.x147)**2 + (m.x225 -
    m.x226)**2)**(-3) * (((m.x67 - m.x68)**2 + (m.x146 - m.x147)**2 + (m.x225
    - m.x226)**2)**(-3) - 2) + ((m.x67 - m.x69)**2 + (m.x146 - m.x148)**2 + (
    m.x225 - m.x227)**2)**(-3) * (((m.x67 - m.x69)**2 + (m.x146 - m.x148)**2 +
    (m.x225 - m.x227)**2)**(-3) - 2) + ((m.x67 - m.x70)**2 + (m.x146 - m.x149)
    **2 + (m.x225 - m.x228)**2)**(-3) * (((m.x67 - m.x70)**2 + (m.x146 - m.x149)
    **2 + (m.x225 - m.x228)**2)**(-3) - 2) + ((m.x67 - m.x71)**2 + (m.x146 -
    m.x150)**2 + (m.x225 - m.x229)**2)**(-3) * (((m.x67 - m.x71)**2 + (m.x146
    - m.x150)**2 + (m.x225 - m.x229)**2)**(-3) - 2) + ((m.x67 - m.x72)**2 + (
    m.x146 - m.x151)**2 + (m.x225 - m.x230)**2)**(-3) * (((m.x67 - m.x72)**2 +
    (m.x146 - m.x151)**2 + (m.x225 - m.x230)**2)**(-3) - 2) + ((m.x67 - m.x73)
    **2 + (m.x146 - m.x152)**2 + (m.x225 - m.x231)**2)**(-3) * (((m.x67 - m.x73)
    **2 + (m.x146 - m.x152)**2 + (m.x225 - m.x231)**2)**(-3) - 2) + ((m.x67 -
    m.x74)**2 + (m.x146 - m.x153)**2 + (m.x225 - m.x232)**2)**(-3) * (((m.x67
    - m.x74)**2 + (m.x146 - m.x153)**2 + (m.x225 - m.x232)**2)**(-3) - 2) + ((
    m.x67 - m.x75)**2 + (m.x146 - m.x154)**2 + (m.x225 - m.x233)**2)**(-3) * ((
    (m.x67 - m.x75)**2 + (m.x146 - m.x154)**2 + (m.x225 - m.x233)**2)**(-3) - 2)
    + ((m.x67 - m.x76)**2 + (m.x146 - m.x155)**2 + (m.x225 - m.x234)**2)**(-3)
    * (((m.x67 - m.x76)**2 + (m.x146 - m.x155)**2 + (m.x225 - m.x234)**2)**(-3)
    - 2) + ((m.x67 - m.x77)**2 + (m.x146 - m.x156)**2 + (m.x225 - m.x235)**2)
    **(-3) * (((m.x67 - m.x77)**2 + (m.x146 - m.x156)**2 + (m.x225 - m.x235)**2)
    **(-3) - 2) + ((m.x67 - m.x78)**2 + (m.x146 - m.x157)**2 + (m.x225 - m.x236)
    **2)**(-3) * (((m.x67 - m.x78)**2 + (m.x146 - m.x157)**2 + (m.x225 - m.x236)
    **2)**(-3) - 2) + ((m.x67 - m.x79)**2 + (m.x146 - m.x158)**2 + (m.x225 -
    m.x237)**2)**(-3) * (((m.x67 - m.x79)**2 + (m.x146 - m.x158)**2 + (m.x225
    - m.x237)**2)**(-3) - 2) + ((m.x68 - m.x69)**2 + (m.x147 - m.x148)**2 + (
    m.x226 - m.x227)**2)**(-3) * (((m.x68 - m.x69)**2 + (m.x147 - m.x148)**2 +
    (m.x226 - m.x227)**2)**(-3) - 2) + ((m.x68 - m.x70)**2 + (m.x147 - m.x149)
    **2 + (m.x226 - m.x228)**2)**(-3) * (((m.x68 - m.x70)**2 + (m.x147 - m.x149)
    **2 + (m.x226 - m.x228)**2)**(-3) - 2) + ((m.x68 - m.x71)**2 + (m.x147 -
    m.x150)**2 + (m.x226 - m.x229)**2)**(-3) * (((m.x68 - m.x71)**2 + (m.x147
    - m.x150)**2 + (m.x226 - m.x229)**2)**(-3) - 2) + ((m.x68 - m.x72)**2 + (
    m.x147 - m.x151)**2 + (m.x226 - m.x230)**2)**(-3) * (((m.x68 - m.x72)**2 +
    (m.x147 - m.x151)**2 + (m.x226 - m.x230)**2)**(-3) - 2) + ((m.x68 - m.x73)
    **2 + (m.x147 - m.x152)**2 + (m.x226 - m.x231)**2)**(-3) * (((m.x68 - m.x73)
    **2 + (m.x147 - m.x152)**2 + (m.x226 - m.x231)**2)**(-3) - 2) + ((m.x68 -
    m.x74)**2 + (m.x147 - m.x153)**2 + (m.x226 - m.x232)**2)**(-3) * (((m.x68
    - m.x74)**2 + (m.x147 - m.x153)**2 + (m.x226 - m.x232)**2)**(-3) - 2) + ((
    m.x68 - m.x75)**2 + (m.x147 - m.x154)**2 + (m.x226 - m.x233)**2)**(-3) * ((
    (m.x68 - m.x75)**2 + (m.x147 - m.x154)**2 + (m.x226 - m.x233)**2)**(-3) - 2)
    + ((m.x68 - m.x76)**2 + (m.x147 - m.x155)**2 + (m.x226 - m.x234)**2)**(-3)
    * (((m.x68 - m.x76)**2 + (m.x147 - m.x155)**2 + (m.x226 - m.x234)**2)**(-3)
    - 2) + ((m.x68 - m.x77)**2 + (m.x147 - m.x156)**2 + (m.x226 - m.x235)**2)
    **(-3) * (((m.x68 - m.x77)**2 + (m.x147 - m.x156)**2 + (m.x226 - m.x235)**2)
    **(-3) - 2) + ((m.x68 - m.x78)**2 + (m.x147 - m.x157)**2 + (m.x226 - m.x236)
    **2)**(-3) * (((m.x68 - m.x78)**2 + (m.x147 - m.x157)**2 + (m.x226 - m.x236)
    **2)**(-3) - 2) + ((m.x68 - m.x79)**2 + (m.x147 - m.x158)**2 + (m.x226 -
    m.x237)**2)**(-3) * (((m.x68 - m.x79)**2 + (m.x147 - m.x158)**2 + (m.x226
    - m.x237)**2)**(-3) - 2) + ((m.x69 - m.x70)**2 + (m.x148 - m.x149)**2 + (
    m.x227 - m.x228)**2)**(-3) * (((m.x69 - m.x70)**2 + (m.x148 - m.x149)**2 +
    (m.x227 - m.x228)**2)**(-3) - 2) + ((m.x69 - m.x71)**2 + (m.x148 - m.x150)
    **2 + (m.x227 - m.x229)**2)**(-3) * (((m.x69 - m.x71)**2 + (m.x148 - m.x150)
    **2 + (m.x227 - m.x229)**2)**(-3) - 2) + ((m.x69 - m.x72)**2 + (m.x148 -
    m.x151)**2 + (m.x227 - m.x230)**2)**(-3) * (((m.x69 - m.x72)**2 + (m.x148
    - m.x151)**2 + (m.x227 - m.x230)**2)**(-3) - 2) + ((m.x69 - m.x73)**2 + (
    m.x148 - m.x152)**2 + (m.x227 - m.x231)**2)**(-3) * (((m.x69 - m.x73)**2 +
    (m.x148 - m.x152)**2 + (m.x227 - m.x231)**2)**(-3) - 2) + ((m.x69 - m.x74)
    **2 + (m.x148 - m.x153)**2 + (m.x227 - m.x232)**2)**(-3) * (((m.x69 - m.x74)
    **2 + (m.x148 - m.x153)**2 + (m.x227 - m.x232)**2)**(-3) - 2) + ((m.x69 -
    m.x75)**2 + (m.x148 - m.x154)**2 + (m.x227 - m.x233)**2)**(-3) * (((m.x69
    - m.x75)**2 + (m.x148 - m.x154)**2 + (m.x227 - m.x233)**2)**(-3) - 2) + ((
    m.x69 - m.x76)**2 + (m.x148 - m.x155)**2 + (m.x227 - m.x234)**2)**(-3) * ((
    (m.x69 - m.x76)**2 + (m.x148 - m.x155)**2 + (m.x227 - m.x234)**2)**(-3) - 2)
    + ((m.x69 - m.x77)**2 + (m.x148 - m.x156)**2 + (m.x227 - m.x235)**2)**(-3)
    * (((m.x69 - m.x77)**2 + (m.x148 - m.x156)**2 + (m.x227 - m.x235)**2)**(-3)
    - 2) + ((m.x69 - m.x78)**2 + (m.x148 - m.x157)**2 + (m.x227 - m.x236)**2)
    **(-3) * (((m.x69 - m.x78)**2 + (m.x148 - m.x157)**2 + (m.x227 - m.x236)**2)
    **(-3) - 2) + ((m.x69 - m.x79)**2 + (m.x148 - m.x158)**2 + (m.x227 - m.x237)
    **2)**(-3) * (((m.x69 - m.x79)**2 + (m.x148 - m.x158)**2 + (m.x227 - m.x237)
    **2)**(-3) - 2) + ((m.x70 - m.x71)**2 + (m.x149 - m.x150)**2 + (m.x228 -
    m.x229)**2)**(-3) * (((m.x70 - m.x71)**2 + (m.x149 - m.x150)**2 + (m.x228
    - m.x229)**2)**(-3) - 2) + ((m.x70 - m.x72)**2 + (m.x149 - m.x151)**2 + (
    m.x228 - m.x230)**2)**(-3) * (((m.x70 - m.x72)**2 + (m.x149 - m.x151)**2 +
    (m.x228 - m.x230)**2)**(-3) - 2) + ((m.x70 - m.x73)**2 + (m.x149 - m.x152)
    **2 + (m.x228 - m.x231)**2)**(-3) * (((m.x70 - m.x73)**2 + (m.x149 - m.x152)
    **2 + (m.x228 - m.x231)**2)**(-3) - 2) + ((m.x70 - m.x74)**2 + (m.x149 -
    m.x153)**2 + (m.x228 - m.x232)**2)**(-3) * (((m.x70 - m.x74)**2 + (m.x149
    - m.x153)**2 + (m.x228 - m.x232)**2)**(-3) - 2) + ((m.x70 - m.x75)**2 + (
    m.x149 - m.x154)**2 + (m.x228 - m.x233)**2)**(-3) * (((m.x70 - m.x75)**2 +
    (m.x149 - m.x154)**2 + (m.x228 - m.x233)**2)**(-3) - 2) + ((m.x70 - m.x76)
    **2 + (m.x149 - m.x155)**2 + (m.x228 - m.x234)**2)**(-3) * (((m.x70 - m.x76)
    **2 + (m.x149 - m.x155)**2 + (m.x228 - m.x234)**2)**(-3) - 2) + ((m.x70 -
    m.x77)**2 + (m.x149 - m.x156)**2 + (m.x228 - m.x235)**2)**(-3) * (((m.x70
    - m.x77)**2 + (m.x149 - m.x156)**2 + (m.x228 - m.x235)**2)**(-3) - 2) + ((
    m.x70 - m.x78)**2 + (m.x149 - m.x157)**2 + (m.x228 - m.x236)**2)**(-3) * ((
    (m.x70 - m.x78)**2 + (m.x149 - m.x157)**2 + (m.x228 - m.x236)**2)**(-3) - 2)
    + ((m.x70 - m.x79)**2 + (m.x149 - m.x158)**2 + (m.x228 - m.x237)**2)**(-3)
    * (((m.x70 - m.x79)**2 + (m.x149 - m.x158)**2 + (m.x228 - m.x237)**2)**(-3)
    - 2) + ((m.x71 - m.x72)**2 + (m.x150 - m.x151)**2 + (m.x229 - m.x230)**2)
    **(-3) * (((m.x71 - m.x72)**2 + (m.x150 - m.x151)**2 + (m.x229 - m.x230)**2)
    **(-3) - 2) + ((m.x71 - m.x73)**2 + (m.x150 - m.x152)**2 + (m.x229 - m.x231)
    **2)**(-3) * (((m.x71 - m.x73)**2 + (m.x150 - m.x152)**2 + (m.x229 - m.x231)
    **2)**(-3) - 2) + ((m.x71 - m.x74)**2 + (m.x150 - m.x153)**2 + (m.x229 -
    m.x232)**2)**(-3) * (((m.x71 - m.x74)**2 + (m.x150 - m.x153)**2 + (m.x229
    - m.x232)**2)**(-3) - 2) + ((m.x71 - m.x75)**2 + (m.x150 - m.x154)**2 + (
    m.x229 - m.x233)**2)**(-3) * (((m.x71 - m.x75)**2 + (m.x150 - m.x154)**2 +
    (m.x229 - m.x233)**2)**(-3) - 2) + ((m.x71 - m.x76)**2 + (m.x150 - m.x155)
    **2 + (m.x229 - m.x234)**2)**(-3) * (((m.x71 - m.x76)**2 + (m.x150 - m.x155)
    **2 + (m.x229 - m.x234)**2)**(-3) - 2) + ((m.x71 - m.x77)**2 + (m.x150 -
    m.x156)**2 + (m.x229 - m.x235)**2)**(-3) * (((m.x71 - m.x77)**2 + (m.x150
    - m.x156)**2 + (m.x229 - m.x235)**2)**(-3) - 2) + ((m.x71 - m.x78)**2 + (
    m.x150 - m.x157)**2 + (m.x229 - m.x236)**2)**(-3) * (((m.x71 - m.x78)**2 +
    (m.x150 - m.x157)**2 + (m.x229 - m.x236)**2)**(-3) - 2) + ((m.x71 - m.x79)
    **2 + (m.x150 - m.x158)**2 + (m.x229 - m.x237)**2)**(-3) * (((m.x71 - m.x79)
    **2 + (m.x150 - m.x158)**2 + (m.x229 - m.x237)**2)**(-3) - 2) + ((m.x72 -
    m.x73)**2 + (m.x151 - m.x152)**2 + (m.x230 - m.x231)**2)**(-3) * (((m.x72
    - m.x73)**2 + (m.x151 - m.x152)**2 + (m.x230 - m.x231)**2)**(-3) - 2) + ((
    m.x72 - m.x74)**2 + (m.x151 - m.x153)**2 + (m.x230 - m.x232)**2)**(-3) * ((
    (m.x72 - m.x74)**2 + (m.x151 - m.x153)**2 + (m.x230 - m.x232)**2)**(-3) - 2)
    + ((m.x72 - m.x75)**2 + (m.x151 - m.x154)**2 + (m.x230 - m.x233)**2)**(-3)
    * (((m.x72 - m.x75)**2 + (m.x151 - m.x154)**2 + (m.x230 - m.x233)**2)**(-3)
    - 2) + ((m.x72 - m.x76)**2 + (m.x151 - m.x155)**2 + (m.x230 - m.x234)**2)
    **(-3) * (((m.x72 - m.x76)**2 + (m.x151 - m.x155)**2 + (m.x230 - m.x234)**2)
    **(-3) - 2) + ((m.x72 - m.x77)**2 + (m.x151 - m.x156)**2 + (m.x230 - m.x235)
    **2)**(-3) * (((m.x72 - m.x77)**2 + (m.x151 - m.x156)**2 + (m.x230 - m.x235)
    **2)**(-3) - 2) + ((m.x72 - m.x78)**2 + (m.x151 - m.x157)**2 + (m.x230 -
    m.x236)**2)**(-3) * (((m.x72 - m.x78)**2 + (m.x151 - m.x157)**2 + (m.x230
    - m.x236)**2)**(-3) - 2) + ((m.x72 - m.x79)**2 + (m.x151 - m.x158)**2 + (
    m.x230 - m.x237)**2)**(-3) * (((m.x72 - m.x79)**2 + (m.x151 - m.x158)**2 +
    (m.x230 - m.x237)**2)**(-3) - 2) + ((m.x73 - m.x74)**2 + (m.x152 - m.x153)
    **2 + (m.x231 - m.x232)**2)**(-3) * (((m.x73 - m.x74)**2 + (m.x152 - m.x153)
    **2 + (m.x231 - m.x232)**2)**(-3) - 2) + ((m.x73 - m.x75)**2 + (m.x152 -
    m.x154)**2 + (m.x231 - m.x233)**2)**(-3) * (((m.x73 - m.x75)**2 + (m.x152
    - m.x154)**2 + (m.x231 - m.x233)**2)**(-3) - 2) + ((m.x73 - m.x76)**2 + (
    m.x152 - m.x155)**2 + (m.x231 - m.x234)**2)**(-3) * (((m.x73 - m.x76)**2 +
    (m.x152 - m.x155)**2 + (m.x231 - m.x234)**2)**(-3) - 2) + ((m.x73 - m.x77)
    **2 + (m.x152 - m.x156)**2 + (m.x231 - m.x235)**2)**(-3) * (((m.x73 - m.x77)
    **2 + (m.x152 - m.x156)**2 + (m.x231 - m.x235)**2)**(-3) - 2) + ((m.x73 -
    m.x78)**2 + (m.x152 - m.x157)**2 + (m.x231 - m.x236)**2)**(-3) * (((m.x73
    - m.x78)**2 + (m.x152 - m.x157)**2 + (m.x231 - m.x236)**2)**(-3) - 2) + ((
    m.x73 - m.x79)**2 + (m.x152 - m.x158)**2 + (m.x231 - m.x237)**2)**(-3) * ((
    (m.x73 - m.x79)**2 + (m.x152 - m.x158)**2 + (m.x231 - m.x237)**2)**(-3) - 2)
    + ((m.x74 - m.x75)**2 + (m.x153 - m.x154)**2 + (m.x232 - m.x233)**2)**(-3)
    * (((m.x74 - m.x75)**2 + (m.x153 - m.x154)**2 + (m.x232 - m.x233)**2)**(-3)
    - 2) + ((m.x74 - m.x76)**2 + (m.x153 - m.x155)**2 + (m.x232 - m.x234)**2)
    **(-3) * (((m.x74 - m.x76)**2 + (m.x153 - m.x155)**2 + (m.x232 - m.x234)**2)
    **(-3) - 2) + ((m.x74 - m.x77)**2 + (m.x153 - m.x156)**2 + (m.x232 - m.x235)
    **2)**(-3) * (((m.x74 - m.x77)**2 + (m.x153 - m.x156)**2 + (m.x232 - m.x235)
    **2)**(-3) - 2) + ((m.x74 - m.x78)**2 + (m.x153 - m.x157)**2 + (m.x232 -
    m.x236)**2)**(-3) * (((m.x74 - m.x78)**2 + (m.x153 - m.x157)**2 + (m.x232
    - m.x236)**2)**(-3) - 2) + ((m.x74 - m.x79)**2 + (m.x153 - m.x158)**2 + (
    m.x232 - m.x237)**2)**(-3) * (((m.x74 - m.x79)**2 + (m.x153 - m.x158)**2 +
    (m.x232 - m.x237)**2)**(-3) - 2) + ((m.x75 - m.x76)**2 + (m.x154 - m.x155)
    **2 + (m.x233 - m.x234)**2)**(-3) * (((m.x75 - m.x76)**2 + (m.x154 - m.x155)
    **2 + (m.x233 - m.x234)**2)**(-3) - 2) + ((m.x75 - m.x77)**2 + (m.x154 -
    m.x156)**2 + (m.x233 - m.x235)**2)**(-3) * (((m.x75 - m.x77)**2 + (m.x154
    - m.x156)**2 + (m.x233 - m.x235)**2)**(-3) - 2) + ((m.x75 - m.x78)**2 + (
    m.x154 - m.x157)**2 + (m.x233 - m.x236)**2)**(-3) * (((m.x75 - m.x78)**2 +
    (m.x154 - m.x157)**2 + (m.x233 - m.x236)**2)**(-3) - 2) + ((m.x75 - m.x79)
    **2 + (m.x154 - m.x158)**2 + (m.x233 - m.x237)**2)**(-3) * (((m.x75 - m.x79)
    **2 + (m.x154 - m.x158)**2 + (m.x233 - m.x237)**2)**(-3) - 2) + ((m.x76 -
    m.x77)**2 + (m.x155 - m.x156)**2 + (m.x234 - m.x235)**2)**(-3) * (((m.x76
    - m.x77)**2 + (m.x155 - m.x156)**2 + (m.x234 - m.x235)**2)**(-3) - 2) + ((
    m.x76 - m.x78)**2 + (m.x155 - m.x157)**2 + (m.x234 - m.x236)**2)**(-3) * ((
    (m.x76 - m.x78)**2 + (m.x155 - m.x157)**2 + (m.x234 - m.x236)**2)**(-3) - 2)
    + ((m.x76 - m.x79)**2 + (m.x155 - m.x158)**2 + (m.x234 - m.x237)**2)**(-3)
    * (((m.x76 - m.x79)**2 + (m.x155 - m.x158)**2 + (m.x234 - m.x237)**2)**(-3)
    - 2) + ((m.x77 - m.x78)**2 + (m.x156 - m.x157)**2 + (m.x235 - m.x236)**2)
    **(-3) * (((m.x77 - m.x78)**2 + (m.x156 - m.x157)**2 + (m.x235 - m.x236)**2)
    **(-3) - 2) + ((m.x77 - m.x79)**2 + (m.x156 - m.x158)**2 + (m.x235 - m.x237)
    **2)**(-3) * (((m.x77 - m.x79)**2 + (m.x156 - m.x158)**2 + (m.x235 - m.x237)
    **2)**(-3) - 2) + ((m.x78 - m.x79)**2 + (m.x157 - m.x158)**2 + (m.x236 -
    m.x237)**2)**(-3) * (((m.x78 - m.x79)**2 + (m.x157 - m.x158)**2 + (m.x236
    - m.x237)**2)**(-3) - 2))

m.e1 = Constraint(expr= (m.x1 - m.x2)**2 + (m.x80 - m.x81)**2 + (m.x159 -
    m.x160)**2 >= 0.46785600000000005)
m.e2 = Constraint(expr= (m.x1 - m.x3)**2 + (m.x80 - m.x82)**2 + (m.x159 -
    m.x161)**2 >= 0.46785600000000005)
m.e3 = Constraint(expr= (m.x1 - m.x4)**2 + (m.x80 - m.x83)**2 + (m.x159 -
    m.x162)**2 >= 0.46785600000000005)
m.e4 = Constraint(expr= (m.x1 - m.x5)**2 + (m.x80 - m.x84)**2 + (m.x159 -
    m.x163)**2 >= 0.46785600000000005)
m.e5 = Constraint(expr= (m.x1 - m.x6)**2 + (m.x80 - m.x85)**2 + (m.x159 -
    m.x164)**2 >= 0.46785600000000005)
m.e6 = Constraint(expr= (m.x1 - m.x7)**2 + (m.x80 - m.x86)**2 + (m.x159 -
    m.x165)**2 >= 0.46785600000000005)
m.e7 = Constraint(expr= (m.x1 - m.x8)**2 + (m.x80 - m.x87)**2 + (m.x159 -
    m.x166)**2 >= 0.46785600000000005)
m.e8 = Constraint(expr= (m.x1 - m.x9)**2 + (m.x80 - m.x88)**2 + (m.x159 -
    m.x167)**2 >= 0.46785600000000005)
m.e9 = Constraint(expr= (m.x1 - m.x10)**2 + (m.x80 - m.x89)**2 + (m.x159 -
    m.x168)**2 >= 0.46785600000000005)
m.e10 = Constraint(expr= (m.x1 - m.x11)**2 + (m.x80 - m.x90)**2 + (m.x159 -
    m.x169)**2 >= 0.46785600000000005)
m.e11 = Constraint(expr= (m.x1 - m.x12)**2 + (m.x80 - m.x91)**2 + (m.x159 -
    m.x170)**2 >= 0.46785600000000005)
m.e12 = Constraint(expr= (m.x1 - m.x13)**2 + (m.x80 - m.x92)**2 + (m.x159 -
    m.x171)**2 >= 0.46785600000000005)
m.e13 = Constraint(expr= (m.x1 - m.x14)**2 + (m.x80 - m.x93)**2 + (m.x159 -
    m.x172)**2 >= 0.46785600000000005)
m.e14 = Constraint(expr= (m.x1 - m.x15)**2 + (m.x80 - m.x94)**2 + (m.x159 -
    m.x173)**2 >= 0.46785600000000005)
m.e15 = Constraint(expr= (m.x1 - m.x16)**2 + (m.x80 - m.x95)**2 + (m.x159 -
    m.x174)**2 >= 0.46785600000000005)
m.e16 = Constraint(expr= (m.x1 - m.x17)**2 + (m.x80 - m.x96)**2 + (m.x159 -
    m.x175)**2 >= 0.46785600000000005)
m.e17 = Constraint(expr= (m.x1 - m.x18)**2 + (m.x80 - m.x97)**2 + (m.x159 -
    m.x176)**2 >= 0.46785600000000005)
m.e18 = Constraint(expr= (m.x1 - m.x19)**2 + (m.x80 - m.x98)**2 + (m.x159 -
    m.x177)**2 >= 0.46785600000000005)
m.e19 = Constraint(expr= (m.x1 - m.x20)**2 + (m.x80 - m.x99)**2 + (m.x159 -
    m.x178)**2 >= 0.46785600000000005)
m.e20 = Constraint(expr= (m.x1 - m.x21)**2 + (m.x80 - m.x100)**2 + (m.x159 -
    m.x179)**2 >= 0.46785600000000005)
m.e21 = Constraint(expr= (m.x1 - m.x22)**2 + (m.x80 - m.x101)**2 + (m.x159 -
    m.x180)**2 >= 0.46785600000000005)
m.e22 = Constraint(expr= (m.x1 - m.x23)**2 + (m.x80 - m.x102)**2 + (m.x159 -
    m.x181)**2 >= 0.46785600000000005)
m.e23 = Constraint(expr= (m.x1 - m.x24)**2 + (m.x80 - m.x103)**2 + (m.x159 -
    m.x182)**2 >= 0.46785600000000005)
m.e24 = Constraint(expr= (m.x1 - m.x25)**2 + (m.x80 - m.x104)**2 + (m.x159 -
    m.x183)**2 >= 0.46785600000000005)
m.e25 = Constraint(expr= (m.x1 - m.x26)**2 + (m.x80 - m.x105)**2 + (m.x159 -
    m.x184)**2 >= 0.46785600000000005)
m.e26 = Constraint(expr= (m.x1 - m.x27)**2 + (m.x80 - m.x106)**2 + (m.x159 -
    m.x185)**2 >= 0.46785600000000005)
m.e27 = Constraint(expr= (m.x1 - m.x28)**2 + (m.x80 - m.x107)**2 + (m.x159 -
    m.x186)**2 >= 0.46785600000000005)
m.e28 = Constraint(expr= (m.x1 - m.x29)**2 + (m.x80 - m.x108)**2 + (m.x159 -
    m.x187)**2 >= 0.46785600000000005)
m.e29 = Constraint(expr= (m.x1 - m.x30)**2 + (m.x80 - m.x109)**2 + (m.x159 -
    m.x188)**2 >= 0.46785600000000005)
m.e30 = Constraint(expr= (m.x1 - m.x31)**2 + (m.x80 - m.x110)**2 + (m.x159 -
    m.x189)**2 >= 0.46785600000000005)
m.e31 = Constraint(expr= (m.x1 - m.x32)**2 + (m.x80 - m.x111)**2 + (m.x159 -
    m.x190)**2 >= 0.46785600000000005)
m.e32 = Constraint(expr= (m.x1 - m.x33)**2 + (m.x80 - m.x112)**2 + (m.x159 -
    m.x191)**2 >= 0.46785600000000005)
m.e33 = Constraint(expr= (m.x1 - m.x34)**2 + (m.x80 - m.x113)**2 + (m.x159 -
    m.x192)**2 >= 0.46785600000000005)
m.e34 = Constraint(expr= (m.x1 - m.x35)**2 + (m.x80 - m.x114)**2 + (m.x159 -
    m.x193)**2 >= 0.46785600000000005)
m.e35 = Constraint(expr= (m.x1 - m.x36)**2 + (m.x80 - m.x115)**2 + (m.x159 -
    m.x194)**2 >= 0.46785600000000005)
m.e36 = Constraint(expr= (m.x1 - m.x37)**2 + (m.x80 - m.x116)**2 + (m.x159 -
    m.x195)**2 >= 0.46785600000000005)
m.e37 = Constraint(expr= (m.x1 - m.x38)**2 + (m.x80 - m.x117)**2 + (m.x159 -
    m.x196)**2 >= 0.46785600000000005)
m.e38 = Constraint(expr= (m.x1 - m.x39)**2 + (m.x80 - m.x118)**2 + (m.x159 -
    m.x197)**2 >= 0.46785600000000005)
m.e39 = Constraint(expr= (m.x1 - m.x40)**2 + (m.x80 - m.x119)**2 + (m.x159 -
    m.x198)**2 >= 0.46785600000000005)
m.e40 = Constraint(expr= (m.x1 - m.x41)**2 + (m.x80 - m.x120)**2 + (m.x159 -
    m.x199)**2 >= 0.46785600000000005)
m.e41 = Constraint(expr= (m.x1 - m.x42)**2 + (m.x80 - m.x121)**2 + (m.x159 -
    m.x200)**2 >= 0.46785600000000005)
m.e42 = Constraint(expr= (m.x1 - m.x43)**2 + (m.x80 - m.x122)**2 + (m.x159 -
    m.x201)**2 >= 0.46785600000000005)
m.e43 = Constraint(expr= (m.x1 - m.x44)**2 + (m.x80 - m.x123)**2 + (m.x159 -
    m.x202)**2 >= 0.46785600000000005)
m.e44 = Constraint(expr= (m.x1 - m.x45)**2 + (m.x80 - m.x124)**2 + (m.x159 -
    m.x203)**2 >= 0.46785600000000005)
m.e45 = Constraint(expr= (m.x1 - m.x46)**2 + (m.x80 - m.x125)**2 + (m.x159 -
    m.x204)**2 >= 0.46785600000000005)
m.e46 = Constraint(expr= (m.x1 - m.x47)**2 + (m.x80 - m.x126)**2 + (m.x159 -
    m.x205)**2 >= 0.46785600000000005)
m.e47 = Constraint(expr= (m.x1 - m.x48)**2 + (m.x80 - m.x127)**2 + (m.x159 -
    m.x206)**2 >= 0.46785600000000005)
m.e48 = Constraint(expr= (m.x1 - m.x49)**2 + (m.x80 - m.x128)**2 + (m.x159 -
    m.x207)**2 >= 0.46785600000000005)
m.e49 = Constraint(expr= (m.x1 - m.x50)**2 + (m.x80 - m.x129)**2 + (m.x159 -
    m.x208)**2 >= 0.46785600000000005)
m.e50 = Constraint(expr= (m.x1 - m.x51)**2 + (m.x80 - m.x130)**2 + (m.x159 -
    m.x209)**2 >= 0.46785600000000005)
m.e51 = Constraint(expr= (m.x1 - m.x52)**2 + (m.x80 - m.x131)**2 + (m.x159 -
    m.x210)**2 >= 0.46785600000000005)
m.e52 = Constraint(expr= (m.x1 - m.x53)**2 + (m.x80 - m.x132)**2 + (m.x159 -
    m.x211)**2 >= 0.46785600000000005)
m.e53 = Constraint(expr= (m.x1 - m.x54)**2 + (m.x80 - m.x133)**2 + (m.x159 -
    m.x212)**2 >= 0.46785600000000005)
m.e54 = Constraint(expr= (m.x1 - m.x55)**2 + (m.x80 - m.x134)**2 + (m.x159 -
    m.x213)**2 >= 0.46785600000000005)
m.e55 = Constraint(expr= (m.x1 - m.x56)**2 + (m.x80 - m.x135)**2 + (m.x159 -
    m.x214)**2 >= 0.46785600000000005)
m.e56 = Constraint(expr= (m.x1 - m.x57)**2 + (m.x80 - m.x136)**2 + (m.x159 -
    m.x215)**2 >= 0.46785600000000005)
m.e57 = Constraint(expr= (m.x1 - m.x58)**2 + (m.x80 - m.x137)**2 + (m.x159 -
    m.x216)**2 >= 0.46785600000000005)
m.e58 = Constraint(expr= (m.x1 - m.x59)**2 + (m.x80 - m.x138)**2 + (m.x159 -
    m.x217)**2 >= 0.46785600000000005)
m.e59 = Constraint(expr= (m.x1 - m.x60)**2 + (m.x80 - m.x139)**2 + (m.x159 -
    m.x218)**2 >= 0.46785600000000005)
m.e60 = Constraint(expr= (m.x1 - m.x61)**2 + (m.x80 - m.x140)**2 + (m.x159 -
    m.x219)**2 >= 0.46785600000000005)
m.e61 = Constraint(expr= (m.x1 - m.x62)**2 + (m.x80 - m.x141)**2 + (m.x159 -
    m.x220)**2 >= 0.46785600000000005)
m.e62 = Constraint(expr= (m.x1 - m.x63)**2 + (m.x80 - m.x142)**2 + (m.x159 -
    m.x221)**2 >= 0.46785600000000005)
m.e63 = Constraint(expr= (m.x1 - m.x64)**2 + (m.x80 - m.x143)**2 + (m.x159 -
    m.x222)**2 >= 0.46785600000000005)
m.e64 = Constraint(expr= (m.x1 - m.x65)**2 + (m.x80 - m.x144)**2 + (m.x159 -
    m.x223)**2 >= 0.46785600000000005)
m.e65 = Constraint(expr= (m.x1 - m.x66)**2 + (m.x80 - m.x145)**2 + (m.x159 -
    m.x224)**2 >= 0.46785600000000005)
m.e66 = Constraint(expr= (m.x1 - m.x67)**2 + (m.x80 - m.x146)**2 + (m.x159 -
    m.x225)**2 >= 0.46785600000000005)
m.e67 = Constraint(expr= (m.x1 - m.x68)**2 + (m.x80 - m.x147)**2 + (m.x159 -
    m.x226)**2 >= 0.46785600000000005)
m.e68 = Constraint(expr= (m.x1 - m.x69)**2 + (m.x80 - m.x148)**2 + (m.x159 -
    m.x227)**2 >= 0.46785600000000005)
m.e69 = Constraint(expr= (m.x1 - m.x70)**2 + (m.x80 - m.x149)**2 + (m.x159 -
    m.x228)**2 >= 0.46785600000000005)
m.e70 = Constraint(expr= (m.x1 - m.x71)**2 + (m.x80 - m.x150)**2 + (m.x159 -
    m.x229)**2 >= 0.46785600000000005)
m.e71 = Constraint(expr= (m.x1 - m.x72)**2 + (m.x80 - m.x151)**2 + (m.x159 -
    m.x230)**2 >= 0.46785600000000005)
m.e72 = Constraint(expr= (m.x1 - m.x73)**2 + (m.x80 - m.x152)**2 + (m.x159 -
    m.x231)**2 >= 0.46785600000000005)
m.e73 = Constraint(expr= (m.x1 - m.x74)**2 + (m.x80 - m.x153)**2 + (m.x159 -
    m.x232)**2 >= 0.46785600000000005)
m.e74 = Constraint(expr= (m.x1 - m.x75)**2 + (m.x80 - m.x154)**2 + (m.x159 -
    m.x233)**2 >= 0.46785600000000005)
m.e75 = Constraint(expr= (m.x1 - m.x76)**2 + (m.x80 - m.x155)**2 + (m.x159 -
    m.x234)**2 >= 0.46785600000000005)
m.e76 = Constraint(expr= (m.x1 - m.x77)**2 + (m.x80 - m.x156)**2 + (m.x159 -
    m.x235)**2 >= 0.46785600000000005)
m.e77 = Constraint(expr= (m.x1 - m.x78)**2 + (m.x80 - m.x157)**2 + (m.x159 -
    m.x236)**2 >= 0.46785600000000005)
m.e78 = Constraint(expr= (m.x1 - m.x79)**2 + (m.x80 - m.x158)**2 + (m.x159 -
    m.x237)**2 >= 0.46785600000000005)
m.e79 = Constraint(expr= (m.x2 - m.x3)**2 + (m.x81 - m.x82)**2 + (m.x160 -
    m.x161)**2 >= 0.46785600000000005)
m.e80 = Constraint(expr= (m.x2 - m.x4)**2 + (m.x81 - m.x83)**2 + (m.x160 -
    m.x162)**2 >= 0.46785600000000005)
m.e81 = Constraint(expr= (m.x2 - m.x5)**2 + (m.x81 - m.x84)**2 + (m.x160 -
    m.x163)**2 >= 0.46785600000000005)
m.e82 = Constraint(expr= (m.x2 - m.x6)**2 + (m.x81 - m.x85)**2 + (m.x160 -
    m.x164)**2 >= 0.46785600000000005)
m.e83 = Constraint(expr= (m.x2 - m.x7)**2 + (m.x81 - m.x86)**2 + (m.x160 -
    m.x165)**2 >= 0.46785600000000005)
m.e84 = Constraint(expr= (m.x2 - m.x8)**2 + (m.x81 - m.x87)**2 + (m.x160 -
    m.x166)**2 >= 0.46785600000000005)
m.e85 = Constraint(expr= (m.x2 - m.x9)**2 + (m.x81 - m.x88)**2 + (m.x160 -
    m.x167)**2 >= 0.46785600000000005)
m.e86 = Constraint(expr= (m.x2 - m.x10)**2 + (m.x81 - m.x89)**2 + (m.x160 -
    m.x168)**2 >= 0.46785600000000005)
m.e87 = Constraint(expr= (m.x2 - m.x11)**2 + (m.x81 - m.x90)**2 + (m.x160 -
    m.x169)**2 >= 0.46785600000000005)
m.e88 = Constraint(expr= (m.x2 - m.x12)**2 + (m.x81 - m.x91)**2 + (m.x160 -
    m.x170)**2 >= 0.46785600000000005)
m.e89 = Constraint(expr= (m.x2 - m.x13)**2 + (m.x81 - m.x92)**2 + (m.x160 -
    m.x171)**2 >= 0.46785600000000005)
m.e90 = Constraint(expr= (m.x2 - m.x14)**2 + (m.x81 - m.x93)**2 + (m.x160 -
    m.x172)**2 >= 0.46785600000000005)
m.e91 = Constraint(expr= (m.x2 - m.x15)**2 + (m.x81 - m.x94)**2 + (m.x160 -
    m.x173)**2 >= 0.46785600000000005)
m.e92 = Constraint(expr= (m.x2 - m.x16)**2 + (m.x81 - m.x95)**2 + (m.x160 -
    m.x174)**2 >= 0.46785600000000005)
m.e93 = Constraint(expr= (m.x2 - m.x17)**2 + (m.x81 - m.x96)**2 + (m.x160 -
    m.x175)**2 >= 0.46785600000000005)
m.e94 = Constraint(expr= (m.x2 - m.x18)**2 + (m.x81 - m.x97)**2 + (m.x160 -
    m.x176)**2 >= 0.46785600000000005)
m.e95 = Constraint(expr= (m.x2 - m.x19)**2 + (m.x81 - m.x98)**2 + (m.x160 -
    m.x177)**2 >= 0.46785600000000005)
m.e96 = Constraint(expr= (m.x2 - m.x20)**2 + (m.x81 - m.x99)**2 + (m.x160 -
    m.x178)**2 >= 0.46785600000000005)
m.e97 = Constraint(expr= (m.x2 - m.x21)**2 + (m.x81 - m.x100)**2 + (m.x160 -
    m.x179)**2 >= 0.46785600000000005)
m.e98 = Constraint(expr= (m.x2 - m.x22)**2 + (m.x81 - m.x101)**2 + (m.x160 -
    m.x180)**2 >= 0.46785600000000005)
m.e99 = Constraint(expr= (m.x2 - m.x23)**2 + (m.x81 - m.x102)**2 + (m.x160 -
    m.x181)**2 >= 0.46785600000000005)
m.e100 = Constraint(expr= (m.x2 - m.x24)**2 + (m.x81 - m.x103)**2 + (m.x160 -
    m.x182)**2 >= 0.46785600000000005)
m.e101 = Constraint(expr= (m.x2 - m.x25)**2 + (m.x81 - m.x104)**2 + (m.x160 -
    m.x183)**2 >= 0.46785600000000005)
m.e102 = Constraint(expr= (m.x2 - m.x26)**2 + (m.x81 - m.x105)**2 + (m.x160 -
    m.x184)**2 >= 0.46785600000000005)
m.e103 = Constraint(expr= (m.x2 - m.x27)**2 + (m.x81 - m.x106)**2 + (m.x160 -
    m.x185)**2 >= 0.46785600000000005)
m.e104 = Constraint(expr= (m.x2 - m.x28)**2 + (m.x81 - m.x107)**2 + (m.x160 -
    m.x186)**2 >= 0.46785600000000005)
m.e105 = Constraint(expr= (m.x2 - m.x29)**2 + (m.x81 - m.x108)**2 + (m.x160 -
    m.x187)**2 >= 0.46785600000000005)
m.e106 = Constraint(expr= (m.x2 - m.x30)**2 + (m.x81 - m.x109)**2 + (m.x160 -
    m.x188)**2 >= 0.46785600000000005)
m.e107 = Constraint(expr= (m.x2 - m.x31)**2 + (m.x81 - m.x110)**2 + (m.x160 -
    m.x189)**2 >= 0.46785600000000005)
m.e108 = Constraint(expr= (m.x2 - m.x32)**2 + (m.x81 - m.x111)**2 + (m.x160 -
    m.x190)**2 >= 0.46785600000000005)
m.e109 = Constraint(expr= (m.x2 - m.x33)**2 + (m.x81 - m.x112)**2 + (m.x160 -
    m.x191)**2 >= 0.46785600000000005)
m.e110 = Constraint(expr= (m.x2 - m.x34)**2 + (m.x81 - m.x113)**2 + (m.x160 -
    m.x192)**2 >= 0.46785600000000005)
m.e111 = Constraint(expr= (m.x2 - m.x35)**2 + (m.x81 - m.x114)**2 + (m.x160 -
    m.x193)**2 >= 0.46785600000000005)
m.e112 = Constraint(expr= (m.x2 - m.x36)**2 + (m.x81 - m.x115)**2 + (m.x160 -
    m.x194)**2 >= 0.46785600000000005)
m.e113 = Constraint(expr= (m.x2 - m.x37)**2 + (m.x81 - m.x116)**2 + (m.x160 -
    m.x195)**2 >= 0.46785600000000005)
m.e114 = Constraint(expr= (m.x2 - m.x38)**2 + (m.x81 - m.x117)**2 + (m.x160 -
    m.x196)**2 >= 0.46785600000000005)
m.e115 = Constraint(expr= (m.x2 - m.x39)**2 + (m.x81 - m.x118)**2 + (m.x160 -
    m.x197)**2 >= 0.46785600000000005)
m.e116 = Constraint(expr= (m.x2 - m.x40)**2 + (m.x81 - m.x119)**2 + (m.x160 -
    m.x198)**2 >= 0.46785600000000005)
m.e117 = Constraint(expr= (m.x2 - m.x41)**2 + (m.x81 - m.x120)**2 + (m.x160 -
    m.x199)**2 >= 0.46785600000000005)
m.e118 = Constraint(expr= (m.x2 - m.x42)**2 + (m.x81 - m.x121)**2 + (m.x160 -
    m.x200)**2 >= 0.46785600000000005)
m.e119 = Constraint(expr= (m.x2 - m.x43)**2 + (m.x81 - m.x122)**2 + (m.x160 -
    m.x201)**2 >= 0.46785600000000005)
m.e120 = Constraint(expr= (m.x2 - m.x44)**2 + (m.x81 - m.x123)**2 + (m.x160 -
    m.x202)**2 >= 0.46785600000000005)
m.e121 = Constraint(expr= (m.x2 - m.x45)**2 + (m.x81 - m.x124)**2 + (m.x160 -
    m.x203)**2 >= 0.46785600000000005)
m.e122 = Constraint(expr= (m.x2 - m.x46)**2 + (m.x81 - m.x125)**2 + (m.x160 -
    m.x204)**2 >= 0.46785600000000005)
m.e123 = Constraint(expr= (m.x2 - m.x47)**2 + (m.x81 - m.x126)**2 + (m.x160 -
    m.x205)**2 >= 0.46785600000000005)
m.e124 = Constraint(expr= (m.x2 - m.x48)**2 + (m.x81 - m.x127)**2 + (m.x160 -
    m.x206)**2 >= 0.46785600000000005)
m.e125 = Constraint(expr= (m.x2 - m.x49)**2 + (m.x81 - m.x128)**2 + (m.x160 -
    m.x207)**2 >= 0.46785600000000005)
m.e126 = Constraint(expr= (m.x2 - m.x50)**2 + (m.x81 - m.x129)**2 + (m.x160 -
    m.x208)**2 >= 0.46785600000000005)
m.e127 = Constraint(expr= (m.x2 - m.x51)**2 + (m.x81 - m.x130)**2 + (m.x160 -
    m.x209)**2 >= 0.46785600000000005)
m.e128 = Constraint(expr= (m.x2 - m.x52)**2 + (m.x81 - m.x131)**2 + (m.x160 -
    m.x210)**2 >= 0.46785600000000005)
m.e129 = Constraint(expr= (m.x2 - m.x53)**2 + (m.x81 - m.x132)**2 + (m.x160 -
    m.x211)**2 >= 0.46785600000000005)
m.e130 = Constraint(expr= (m.x2 - m.x54)**2 + (m.x81 - m.x133)**2 + (m.x160 -
    m.x212)**2 >= 0.46785600000000005)
m.e131 = Constraint(expr= (m.x2 - m.x55)**2 + (m.x81 - m.x134)**2 + (m.x160 -
    m.x213)**2 >= 0.46785600000000005)
m.e132 = Constraint(expr= (m.x2 - m.x56)**2 + (m.x81 - m.x135)**2 + (m.x160 -
    m.x214)**2 >= 0.46785600000000005)
m.e133 = Constraint(expr= (m.x2 - m.x57)**2 + (m.x81 - m.x136)**2 + (m.x160 -
    m.x215)**2 >= 0.46785600000000005)
m.e134 = Constraint(expr= (m.x2 - m.x58)**2 + (m.x81 - m.x137)**2 + (m.x160 -
    m.x216)**2 >= 0.46785600000000005)
m.e135 = Constraint(expr= (m.x2 - m.x59)**2 + (m.x81 - m.x138)**2 + (m.x160 -
    m.x217)**2 >= 0.46785600000000005)
m.e136 = Constraint(expr= (m.x2 - m.x60)**2 + (m.x81 - m.x139)**2 + (m.x160 -
    m.x218)**2 >= 0.46785600000000005)
m.e137 = Constraint(expr= (m.x2 - m.x61)**2 + (m.x81 - m.x140)**2 + (m.x160 -
    m.x219)**2 >= 0.46785600000000005)
m.e138 = Constraint(expr= (m.x2 - m.x62)**2 + (m.x81 - m.x141)**2 + (m.x160 -
    m.x220)**2 >= 0.46785600000000005)
m.e139 = Constraint(expr= (m.x2 - m.x63)**2 + (m.x81 - m.x142)**2 + (m.x160 -
    m.x221)**2 >= 0.46785600000000005)
m.e140 = Constraint(expr= (m.x2 - m.x64)**2 + (m.x81 - m.x143)**2 + (m.x160 -
    m.x222)**2 >= 0.46785600000000005)
m.e141 = Constraint(expr= (m.x2 - m.x65)**2 + (m.x81 - m.x144)**2 + (m.x160 -
    m.x223)**2 >= 0.46785600000000005)
m.e142 = Constraint(expr= (m.x2 - m.x66)**2 + (m.x81 - m.x145)**2 + (m.x160 -
    m.x224)**2 >= 0.46785600000000005)
m.e143 = Constraint(expr= (m.x2 - m.x67)**2 + (m.x81 - m.x146)**2 + (m.x160 -
    m.x225)**2 >= 0.46785600000000005)
m.e144 = Constraint(expr= (m.x2 - m.x68)**2 + (m.x81 - m.x147)**2 + (m.x160 -
    m.x226)**2 >= 0.46785600000000005)
m.e145 = Constraint(expr= (m.x2 - m.x69)**2 + (m.x81 - m.x148)**2 + (m.x160 -
    m.x227)**2 >= 0.46785600000000005)
m.e146 = Constraint(expr= (m.x2 - m.x70)**2 + (m.x81 - m.x149)**2 + (m.x160 -
    m.x228)**2 >= 0.46785600000000005)
m.e147 = Constraint(expr= (m.x2 - m.x71)**2 + (m.x81 - m.x150)**2 + (m.x160 -
    m.x229)**2 >= 0.46785600000000005)
m.e148 = Constraint(expr= (m.x2 - m.x72)**2 + (m.x81 - m.x151)**2 + (m.x160 -
    m.x230)**2 >= 0.46785600000000005)
m.e149 = Constraint(expr= (m.x2 - m.x73)**2 + (m.x81 - m.x152)**2 + (m.x160 -
    m.x231)**2 >= 0.46785600000000005)
m.e150 = Constraint(expr= (m.x2 - m.x74)**2 + (m.x81 - m.x153)**2 + (m.x160 -
    m.x232)**2 >= 0.46785600000000005)
m.e151 = Constraint(expr= (m.x2 - m.x75)**2 + (m.x81 - m.x154)**2 + (m.x160 -
    m.x233)**2 >= 0.46785600000000005)
m.e152 = Constraint(expr= (m.x2 - m.x76)**2 + (m.x81 - m.x155)**2 + (m.x160 -
    m.x234)**2 >= 0.46785600000000005)
m.e153 = Constraint(expr= (m.x2 - m.x77)**2 + (m.x81 - m.x156)**2 + (m.x160 -
    m.x235)**2 >= 0.46785600000000005)
m.e154 = Constraint(expr= (m.x2 - m.x78)**2 + (m.x81 - m.x157)**2 + (m.x160 -
    m.x236)**2 >= 0.46785600000000005)
m.e155 = Constraint(expr= (m.x2 - m.x79)**2 + (m.x81 - m.x158)**2 + (m.x160 -
    m.x237)**2 >= 0.46785600000000005)
m.e156 = Constraint(expr= (m.x3 - m.x4)**2 + (m.x82 - m.x83)**2 + (m.x161 -
    m.x162)**2 >= 0.46785600000000005)
m.e157 = Constraint(expr= (m.x3 - m.x5)**2 + (m.x82 - m.x84)**2 + (m.x161 -
    m.x163)**2 >= 0.46785600000000005)
m.e158 = Constraint(expr= (m.x3 - m.x6)**2 + (m.x82 - m.x85)**2 + (m.x161 -
    m.x164)**2 >= 0.46785600000000005)
m.e159 = Constraint(expr= (m.x3 - m.x7)**2 + (m.x82 - m.x86)**2 + (m.x161 -
    m.x165)**2 >= 0.46785600000000005)
m.e160 = Constraint(expr= (m.x3 - m.x8)**2 + (m.x82 - m.x87)**2 + (m.x161 -
    m.x166)**2 >= 0.46785600000000005)
m.e161 = Constraint(expr= (m.x3 - m.x9)**2 + (m.x82 - m.x88)**2 + (m.x161 -
    m.x167)**2 >= 0.46785600000000005)
m.e162 = Constraint(expr= (m.x3 - m.x10)**2 + (m.x82 - m.x89)**2 + (m.x161 -
    m.x168)**2 >= 0.46785600000000005)
m.e163 = Constraint(expr= (m.x3 - m.x11)**2 + (m.x82 - m.x90)**2 + (m.x161 -
    m.x169)**2 >= 0.46785600000000005)
m.e164 = Constraint(expr= (m.x3 - m.x12)**2 + (m.x82 - m.x91)**2 + (m.x161 -
    m.x170)**2 >= 0.46785600000000005)
m.e165 = Constraint(expr= (m.x3 - m.x13)**2 + (m.x82 - m.x92)**2 + (m.x161 -
    m.x171)**2 >= 0.46785600000000005)
m.e166 = Constraint(expr= (m.x3 - m.x14)**2 + (m.x82 - m.x93)**2 + (m.x161 -
    m.x172)**2 >= 0.46785600000000005)
m.e167 = Constraint(expr= (m.x3 - m.x15)**2 + (m.x82 - m.x94)**2 + (m.x161 -
    m.x173)**2 >= 0.46785600000000005)
m.e168 = Constraint(expr= (m.x3 - m.x16)**2 + (m.x82 - m.x95)**2 + (m.x161 -
    m.x174)**2 >= 0.46785600000000005)
m.e169 = Constraint(expr= (m.x3 - m.x17)**2 + (m.x82 - m.x96)**2 + (m.x161 -
    m.x175)**2 >= 0.46785600000000005)
m.e170 = Constraint(expr= (m.x3 - m.x18)**2 + (m.x82 - m.x97)**2 + (m.x161 -
    m.x176)**2 >= 0.46785600000000005)
m.e171 = Constraint(expr= (m.x3 - m.x19)**2 + (m.x82 - m.x98)**2 + (m.x161 -
    m.x177)**2 >= 0.46785600000000005)
m.e172 = Constraint(expr= (m.x3 - m.x20)**2 + (m.x82 - m.x99)**2 + (m.x161 -
    m.x178)**2 >= 0.46785600000000005)
m.e173 = Constraint(expr= (m.x3 - m.x21)**2 + (m.x82 - m.x100)**2 + (m.x161 -
    m.x179)**2 >= 0.46785600000000005)
m.e174 = Constraint(expr= (m.x3 - m.x22)**2 + (m.x82 - m.x101)**2 + (m.x161 -
    m.x180)**2 >= 0.46785600000000005)
m.e175 = Constraint(expr= (m.x3 - m.x23)**2 + (m.x82 - m.x102)**2 + (m.x161 -
    m.x181)**2 >= 0.46785600000000005)
m.e176 = Constraint(expr= (m.x3 - m.x24)**2 + (m.x82 - m.x103)**2 + (m.x161 -
    m.x182)**2 >= 0.46785600000000005)
m.e177 = Constraint(expr= (m.x3 - m.x25)**2 + (m.x82 - m.x104)**2 + (m.x161 -
    m.x183)**2 >= 0.46785600000000005)
m.e178 = Constraint(expr= (m.x3 - m.x26)**2 + (m.x82 - m.x105)**2 + (m.x161 -
    m.x184)**2 >= 0.46785600000000005)
m.e179 = Constraint(expr= (m.x3 - m.x27)**2 + (m.x82 - m.x106)**2 + (m.x161 -
    m.x185)**2 >= 0.46785600000000005)
m.e180 = Constraint(expr= (m.x3 - m.x28)**2 + (m.x82 - m.x107)**2 + (m.x161 -
    m.x186)**2 >= 0.46785600000000005)
m.e181 = Constraint(expr= (m.x3 - m.x29)**2 + (m.x82 - m.x108)**2 + (m.x161 -
    m.x187)**2 >= 0.46785600000000005)
m.e182 = Constraint(expr= (m.x3 - m.x30)**2 + (m.x82 - m.x109)**2 + (m.x161 -
    m.x188)**2 >= 0.46785600000000005)
m.e183 = Constraint(expr= (m.x3 - m.x31)**2 + (m.x82 - m.x110)**2 + (m.x161 -
    m.x189)**2 >= 0.46785600000000005)
m.e184 = Constraint(expr= (m.x3 - m.x32)**2 + (m.x82 - m.x111)**2 + (m.x161 -
    m.x190)**2 >= 0.46785600000000005)
m.e185 = Constraint(expr= (m.x3 - m.x33)**2 + (m.x82 - m.x112)**2 + (m.x161 -
    m.x191)**2 >= 0.46785600000000005)
m.e186 = Constraint(expr= (m.x3 - m.x34)**2 + (m.x82 - m.x113)**2 + (m.x161 -
    m.x192)**2 >= 0.46785600000000005)
m.e187 = Constraint(expr= (m.x3 - m.x35)**2 + (m.x82 - m.x114)**2 + (m.x161 -
    m.x193)**2 >= 0.46785600000000005)
m.e188 = Constraint(expr= (m.x3 - m.x36)**2 + (m.x82 - m.x115)**2 + (m.x161 -
    m.x194)**2 >= 0.46785600000000005)
m.e189 = Constraint(expr= (m.x3 - m.x37)**2 + (m.x82 - m.x116)**2 + (m.x161 -
    m.x195)**2 >= 0.46785600000000005)
m.e190 = Constraint(expr= (m.x3 - m.x38)**2 + (m.x82 - m.x117)**2 + (m.x161 -
    m.x196)**2 >= 0.46785600000000005)
m.e191 = Constraint(expr= (m.x3 - m.x39)**2 + (m.x82 - m.x118)**2 + (m.x161 -
    m.x197)**2 >= 0.46785600000000005)
m.e192 = Constraint(expr= (m.x3 - m.x40)**2 + (m.x82 - m.x119)**2 + (m.x161 -
    m.x198)**2 >= 0.46785600000000005)
m.e193 = Constraint(expr= (m.x3 - m.x41)**2 + (m.x82 - m.x120)**2 + (m.x161 -
    m.x199)**2 >= 0.46785600000000005)
m.e194 = Constraint(expr= (m.x3 - m.x42)**2 + (m.x82 - m.x121)**2 + (m.x161 -
    m.x200)**2 >= 0.46785600000000005)
m.e195 = Constraint(expr= (m.x3 - m.x43)**2 + (m.x82 - m.x122)**2 + (m.x161 -
    m.x201)**2 >= 0.46785600000000005)
m.e196 = Constraint(expr= (m.x3 - m.x44)**2 + (m.x82 - m.x123)**2 + (m.x161 -
    m.x202)**2 >= 0.46785600000000005)
m.e197 = Constraint(expr= (m.x3 - m.x45)**2 + (m.x82 - m.x124)**2 + (m.x161 -
    m.x203)**2 >= 0.46785600000000005)
m.e198 = Constraint(expr= (m.x3 - m.x46)**2 + (m.x82 - m.x125)**2 + (m.x161 -
    m.x204)**2 >= 0.46785600000000005)
m.e199 = Constraint(expr= (m.x3 - m.x47)**2 + (m.x82 - m.x126)**2 + (m.x161 -
    m.x205)**2 >= 0.46785600000000005)
m.e200 = Constraint(expr= (m.x3 - m.x48)**2 + (m.x82 - m.x127)**2 + (m.x161 -
    m.x206)**2 >= 0.46785600000000005)
m.e201 = Constraint(expr= (m.x3 - m.x49)**2 + (m.x82 - m.x128)**2 + (m.x161 -
    m.x207)**2 >= 0.46785600000000005)
m.e202 = Constraint(expr= (m.x3 - m.x50)**2 + (m.x82 - m.x129)**2 + (m.x161 -
    m.x208)**2 >= 0.46785600000000005)
m.e203 = Constraint(expr= (m.x3 - m.x51)**2 + (m.x82 - m.x130)**2 + (m.x161 -
    m.x209)**2 >= 0.46785600000000005)
m.e204 = Constraint(expr= (m.x3 - m.x52)**2 + (m.x82 - m.x131)**2 + (m.x161 -
    m.x210)**2 >= 0.46785600000000005)
m.e205 = Constraint(expr= (m.x3 - m.x53)**2 + (m.x82 - m.x132)**2 + (m.x161 -
    m.x211)**2 >= 0.46785600000000005)
m.e206 = Constraint(expr= (m.x3 - m.x54)**2 + (m.x82 - m.x133)**2 + (m.x161 -
    m.x212)**2 >= 0.46785600000000005)
m.e207 = Constraint(expr= (m.x3 - m.x55)**2 + (m.x82 - m.x134)**2 + (m.x161 -
    m.x213)**2 >= 0.46785600000000005)
m.e208 = Constraint(expr= (m.x3 - m.x56)**2 + (m.x82 - m.x135)**2 + (m.x161 -
    m.x214)**2 >= 0.46785600000000005)
m.e209 = Constraint(expr= (m.x3 - m.x57)**2 + (m.x82 - m.x136)**2 + (m.x161 -
    m.x215)**2 >= 0.46785600000000005)
m.e210 = Constraint(expr= (m.x3 - m.x58)**2 + (m.x82 - m.x137)**2 + (m.x161 -
    m.x216)**2 >= 0.46785600000000005)
m.e211 = Constraint(expr= (m.x3 - m.x59)**2 + (m.x82 - m.x138)**2 + (m.x161 -
    m.x217)**2 >= 0.46785600000000005)
m.e212 = Constraint(expr= (m.x3 - m.x60)**2 + (m.x82 - m.x139)**2 + (m.x161 -
    m.x218)**2 >= 0.46785600000000005)
m.e213 = Constraint(expr= (m.x3 - m.x61)**2 + (m.x82 - m.x140)**2 + (m.x161 -
    m.x219)**2 >= 0.46785600000000005)
m.e214 = Constraint(expr= (m.x3 - m.x62)**2 + (m.x82 - m.x141)**2 + (m.x161 -
    m.x220)**2 >= 0.46785600000000005)
m.e215 = Constraint(expr= (m.x3 - m.x63)**2 + (m.x82 - m.x142)**2 + (m.x161 -
    m.x221)**2 >= 0.46785600000000005)
m.e216 = Constraint(expr= (m.x3 - m.x64)**2 + (m.x82 - m.x143)**2 + (m.x161 -
    m.x222)**2 >= 0.46785600000000005)
m.e217 = Constraint(expr= (m.x3 - m.x65)**2 + (m.x82 - m.x144)**2 + (m.x161 -
    m.x223)**2 >= 0.46785600000000005)
m.e218 = Constraint(expr= (m.x3 - m.x66)**2 + (m.x82 - m.x145)**2 + (m.x161 -
    m.x224)**2 >= 0.46785600000000005)
m.e219 = Constraint(expr= (m.x3 - m.x67)**2 + (m.x82 - m.x146)**2 + (m.x161 -
    m.x225)**2 >= 0.46785600000000005)
m.e220 = Constraint(expr= (m.x3 - m.x68)**2 + (m.x82 - m.x147)**2 + (m.x161 -
    m.x226)**2 >= 0.46785600000000005)
m.e221 = Constraint(expr= (m.x3 - m.x69)**2 + (m.x82 - m.x148)**2 + (m.x161 -
    m.x227)**2 >= 0.46785600000000005)
m.e222 = Constraint(expr= (m.x3 - m.x70)**2 + (m.x82 - m.x149)**2 + (m.x161 -
    m.x228)**2 >= 0.46785600000000005)
m.e223 = Constraint(expr= (m.x3 - m.x71)**2 + (m.x82 - m.x150)**2 + (m.x161 -
    m.x229)**2 >= 0.46785600000000005)
m.e224 = Constraint(expr= (m.x3 - m.x72)**2 + (m.x82 - m.x151)**2 + (m.x161 -
    m.x230)**2 >= 0.46785600000000005)
m.e225 = Constraint(expr= (m.x3 - m.x73)**2 + (m.x82 - m.x152)**2 + (m.x161 -
    m.x231)**2 >= 0.46785600000000005)
m.e226 = Constraint(expr= (m.x3 - m.x74)**2 + (m.x82 - m.x153)**2 + (m.x161 -
    m.x232)**2 >= 0.46785600000000005)
m.e227 = Constraint(expr= (m.x3 - m.x75)**2 + (m.x82 - m.x154)**2 + (m.x161 -
    m.x233)**2 >= 0.46785600000000005)
m.e228 = Constraint(expr= (m.x3 - m.x76)**2 + (m.x82 - m.x155)**2 + (m.x161 -
    m.x234)**2 >= 0.46785600000000005)
m.e229 = Constraint(expr= (m.x3 - m.x77)**2 + (m.x82 - m.x156)**2 + (m.x161 -
    m.x235)**2 >= 0.46785600000000005)
m.e230 = Constraint(expr= (m.x3 - m.x78)**2 + (m.x82 - m.x157)**2 + (m.x161 -
    m.x236)**2 >= 0.46785600000000005)
m.e231 = Constraint(expr= (m.x3 - m.x79)**2 + (m.x82 - m.x158)**2 + (m.x161 -
    m.x237)**2 >= 0.46785600000000005)
m.e232 = Constraint(expr= (m.x4 - m.x5)**2 + (m.x83 - m.x84)**2 + (m.x162 -
    m.x163)**2 >= 0.46785600000000005)
m.e233 = Constraint(expr= (m.x4 - m.x6)**2 + (m.x83 - m.x85)**2 + (m.x162 -
    m.x164)**2 >= 0.46785600000000005)
m.e234 = Constraint(expr= (m.x4 - m.x7)**2 + (m.x83 - m.x86)**2 + (m.x162 -
    m.x165)**2 >= 0.46785600000000005)
m.e235 = Constraint(expr= (m.x4 - m.x8)**2 + (m.x83 - m.x87)**2 + (m.x162 -
    m.x166)**2 >= 0.46785600000000005)
m.e236 = Constraint(expr= (m.x4 - m.x9)**2 + (m.x83 - m.x88)**2 + (m.x162 -
    m.x167)**2 >= 0.46785600000000005)
m.e237 = Constraint(expr= (m.x4 - m.x10)**2 + (m.x83 - m.x89)**2 + (m.x162 -
    m.x168)**2 >= 0.46785600000000005)
m.e238 = Constraint(expr= (m.x4 - m.x11)**2 + (m.x83 - m.x90)**2 + (m.x162 -
    m.x169)**2 >= 0.46785600000000005)
m.e239 = Constraint(expr= (m.x4 - m.x12)**2 + (m.x83 - m.x91)**2 + (m.x162 -
    m.x170)**2 >= 0.46785600000000005)
m.e240 = Constraint(expr= (m.x4 - m.x13)**2 + (m.x83 - m.x92)**2 + (m.x162 -
    m.x171)**2 >= 0.46785600000000005)
m.e241 = Constraint(expr= (m.x4 - m.x14)**2 + (m.x83 - m.x93)**2 + (m.x162 -
    m.x172)**2 >= 0.46785600000000005)
m.e242 = Constraint(expr= (m.x4 - m.x15)**2 + (m.x83 - m.x94)**2 + (m.x162 -
    m.x173)**2 >= 0.46785600000000005)
m.e243 = Constraint(expr= (m.x4 - m.x16)**2 + (m.x83 - m.x95)**2 + (m.x162 -
    m.x174)**2 >= 0.46785600000000005)
m.e244 = Constraint(expr= (m.x4 - m.x17)**2 + (m.x83 - m.x96)**2 + (m.x162 -
    m.x175)**2 >= 0.46785600000000005)
m.e245 = Constraint(expr= (m.x4 - m.x18)**2 + (m.x83 - m.x97)**2 + (m.x162 -
    m.x176)**2 >= 0.46785600000000005)
m.e246 = Constraint(expr= (m.x4 - m.x19)**2 + (m.x83 - m.x98)**2 + (m.x162 -
    m.x177)**2 >= 0.46785600000000005)
m.e247 = Constraint(expr= (m.x4 - m.x20)**2 + (m.x83 - m.x99)**2 + (m.x162 -
    m.x178)**2 >= 0.46785600000000005)
m.e248 = Constraint(expr= (m.x4 - m.x21)**2 + (m.x83 - m.x100)**2 + (m.x162 -
    m.x179)**2 >= 0.46785600000000005)
m.e249 = Constraint(expr= (m.x4 - m.x22)**2 + (m.x83 - m.x101)**2 + (m.x162 -
    m.x180)**2 >= 0.46785600000000005)
m.e250 = Constraint(expr= (m.x4 - m.x23)**2 + (m.x83 - m.x102)**2 + (m.x162 -
    m.x181)**2 >= 0.46785600000000005)
m.e251 = Constraint(expr= (m.x4 - m.x24)**2 + (m.x83 - m.x103)**2 + (m.x162 -
    m.x182)**2 >= 0.46785600000000005)
m.e252 = Constraint(expr= (m.x4 - m.x25)**2 + (m.x83 - m.x104)**2 + (m.x162 -
    m.x183)**2 >= 0.46785600000000005)
m.e253 = Constraint(expr= (m.x4 - m.x26)**2 + (m.x83 - m.x105)**2 + (m.x162 -
    m.x184)**2 >= 0.46785600000000005)
m.e254 = Constraint(expr= (m.x4 - m.x27)**2 + (m.x83 - m.x106)**2 + (m.x162 -
    m.x185)**2 >= 0.46785600000000005)
m.e255 = Constraint(expr= (m.x4 - m.x28)**2 + (m.x83 - m.x107)**2 + (m.x162 -
    m.x186)**2 >= 0.46785600000000005)
m.e256 = Constraint(expr= (m.x4 - m.x29)**2 + (m.x83 - m.x108)**2 + (m.x162 -
    m.x187)**2 >= 0.46785600000000005)
m.e257 = Constraint(expr= (m.x4 - m.x30)**2 + (m.x83 - m.x109)**2 + (m.x162 -
    m.x188)**2 >= 0.46785600000000005)
m.e258 = Constraint(expr= (m.x4 - m.x31)**2 + (m.x83 - m.x110)**2 + (m.x162 -
    m.x189)**2 >= 0.46785600000000005)
m.e259 = Constraint(expr= (m.x4 - m.x32)**2 + (m.x83 - m.x111)**2 + (m.x162 -
    m.x190)**2 >= 0.46785600000000005)
m.e260 = Constraint(expr= (m.x4 - m.x33)**2 + (m.x83 - m.x112)**2 + (m.x162 -
    m.x191)**2 >= 0.46785600000000005)
m.e261 = Constraint(expr= (m.x4 - m.x34)**2 + (m.x83 - m.x113)**2 + (m.x162 -
    m.x192)**2 >= 0.46785600000000005)
m.e262 = Constraint(expr= (m.x4 - m.x35)**2 + (m.x83 - m.x114)**2 + (m.x162 -
    m.x193)**2 >= 0.46785600000000005)
m.e263 = Constraint(expr= (m.x4 - m.x36)**2 + (m.x83 - m.x115)**2 + (m.x162 -
    m.x194)**2 >= 0.46785600000000005)
m.e264 = Constraint(expr= (m.x4 - m.x37)**2 + (m.x83 - m.x116)**2 + (m.x162 -
    m.x195)**2 >= 0.46785600000000005)
m.e265 = Constraint(expr= (m.x4 - m.x38)**2 + (m.x83 - m.x117)**2 + (m.x162 -
    m.x196)**2 >= 0.46785600000000005)
m.e266 = Constraint(expr= (m.x4 - m.x39)**2 + (m.x83 - m.x118)**2 + (m.x162 -
    m.x197)**2 >= 0.46785600000000005)
m.e267 = Constraint(expr= (m.x4 - m.x40)**2 + (m.x83 - m.x119)**2 + (m.x162 -
    m.x198)**2 >= 0.46785600000000005)
m.e268 = Constraint(expr= (m.x4 - m.x41)**2 + (m.x83 - m.x120)**2 + (m.x162 -
    m.x199)**2 >= 0.46785600000000005)
m.e269 = Constraint(expr= (m.x4 - m.x42)**2 + (m.x83 - m.x121)**2 + (m.x162 -
    m.x200)**2 >= 0.46785600000000005)
m.e270 = Constraint(expr= (m.x4 - m.x43)**2 + (m.x83 - m.x122)**2 + (m.x162 -
    m.x201)**2 >= 0.46785600000000005)
m.e271 = Constraint(expr= (m.x4 - m.x44)**2 + (m.x83 - m.x123)**2 + (m.x162 -
    m.x202)**2 >= 0.46785600000000005)
m.e272 = Constraint(expr= (m.x4 - m.x45)**2 + (m.x83 - m.x124)**2 + (m.x162 -
    m.x203)**2 >= 0.46785600000000005)
m.e273 = Constraint(expr= (m.x4 - m.x46)**2 + (m.x83 - m.x125)**2 + (m.x162 -
    m.x204)**2 >= 0.46785600000000005)
m.e274 = Constraint(expr= (m.x4 - m.x47)**2 + (m.x83 - m.x126)**2 + (m.x162 -
    m.x205)**2 >= 0.46785600000000005)
m.e275 = Constraint(expr= (m.x4 - m.x48)**2 + (m.x83 - m.x127)**2 + (m.x162 -
    m.x206)**2 >= 0.46785600000000005)
m.e276 = Constraint(expr= (m.x4 - m.x49)**2 + (m.x83 - m.x128)**2 + (m.x162 -
    m.x207)**2 >= 0.46785600000000005)
m.e277 = Constraint(expr= (m.x4 - m.x50)**2 + (m.x83 - m.x129)**2 + (m.x162 -
    m.x208)**2 >= 0.46785600000000005)
m.e278 = Constraint(expr= (m.x4 - m.x51)**2 + (m.x83 - m.x130)**2 + (m.x162 -
    m.x209)**2 >= 0.46785600000000005)
m.e279 = Constraint(expr= (m.x4 - m.x52)**2 + (m.x83 - m.x131)**2 + (m.x162 -
    m.x210)**2 >= 0.46785600000000005)
m.e280 = Constraint(expr= (m.x4 - m.x53)**2 + (m.x83 - m.x132)**2 + (m.x162 -
    m.x211)**2 >= 0.46785600000000005)
m.e281 = Constraint(expr= (m.x4 - m.x54)**2 + (m.x83 - m.x133)**2 + (m.x162 -
    m.x212)**2 >= 0.46785600000000005)
m.e282 = Constraint(expr= (m.x4 - m.x55)**2 + (m.x83 - m.x134)**2 + (m.x162 -
    m.x213)**2 >= 0.46785600000000005)
m.e283 = Constraint(expr= (m.x4 - m.x56)**2 + (m.x83 - m.x135)**2 + (m.x162 -
    m.x214)**2 >= 0.46785600000000005)
m.e284 = Constraint(expr= (m.x4 - m.x57)**2 + (m.x83 - m.x136)**2 + (m.x162 -
    m.x215)**2 >= 0.46785600000000005)
m.e285 = Constraint(expr= (m.x4 - m.x58)**2 + (m.x83 - m.x137)**2 + (m.x162 -
    m.x216)**2 >= 0.46785600000000005)
m.e286 = Constraint(expr= (m.x4 - m.x59)**2 + (m.x83 - m.x138)**2 + (m.x162 -
    m.x217)**2 >= 0.46785600000000005)
m.e287 = Constraint(expr= (m.x4 - m.x60)**2 + (m.x83 - m.x139)**2 + (m.x162 -
    m.x218)**2 >= 0.46785600000000005)
m.e288 = Constraint(expr= (m.x4 - m.x61)**2 + (m.x83 - m.x140)**2 + (m.x162 -
    m.x219)**2 >= 0.46785600000000005)
m.e289 = Constraint(expr= (m.x4 - m.x62)**2 + (m.x83 - m.x141)**2 + (m.x162 -
    m.x220)**2 >= 0.46785600000000005)
m.e290 = Constraint(expr= (m.x4 - m.x63)**2 + (m.x83 - m.x142)**2 + (m.x162 -
    m.x221)**2 >= 0.46785600000000005)
m.e291 = Constraint(expr= (m.x4 - m.x64)**2 + (m.x83 - m.x143)**2 + (m.x162 -
    m.x222)**2 >= 0.46785600000000005)
m.e292 = Constraint(expr= (m.x4 - m.x65)**2 + (m.x83 - m.x144)**2 + (m.x162 -
    m.x223)**2 >= 0.46785600000000005)
m.e293 = Constraint(expr= (m.x4 - m.x66)**2 + (m.x83 - m.x145)**2 + (m.x162 -
    m.x224)**2 >= 0.46785600000000005)
m.e294 = Constraint(expr= (m.x4 - m.x67)**2 + (m.x83 - m.x146)**2 + (m.x162 -
    m.x225)**2 >= 0.46785600000000005)
m.e295 = Constraint(expr= (m.x4 - m.x68)**2 + (m.x83 - m.x147)**2 + (m.x162 -
    m.x226)**2 >= 0.46785600000000005)
m.e296 = Constraint(expr= (m.x4 - m.x69)**2 + (m.x83 - m.x148)**2 + (m.x162 -
    m.x227)**2 >= 0.46785600000000005)
m.e297 = Constraint(expr= (m.x4 - m.x70)**2 + (m.x83 - m.x149)**2 + (m.x162 -
    m.x228)**2 >= 0.46785600000000005)
m.e298 = Constraint(expr= (m.x4 - m.x71)**2 + (m.x83 - m.x150)**2 + (m.x162 -
    m.x229)**2 >= 0.46785600000000005)
m.e299 = Constraint(expr= (m.x4 - m.x72)**2 + (m.x83 - m.x151)**2 + (m.x162 -
    m.x230)**2 >= 0.46785600000000005)
m.e300 = Constraint(expr= (m.x4 - m.x73)**2 + (m.x83 - m.x152)**2 + (m.x162 -
    m.x231)**2 >= 0.46785600000000005)
m.e301 = Constraint(expr= (m.x4 - m.x74)**2 + (m.x83 - m.x153)**2 + (m.x162 -
    m.x232)**2 >= 0.46785600000000005)
m.e302 = Constraint(expr= (m.x4 - m.x75)**2 + (m.x83 - m.x154)**2 + (m.x162 -
    m.x233)**2 >= 0.46785600000000005)
m.e303 = Constraint(expr= (m.x4 - m.x76)**2 + (m.x83 - m.x155)**2 + (m.x162 -
    m.x234)**2 >= 0.46785600000000005)
m.e304 = Constraint(expr= (m.x4 - m.x77)**2 + (m.x83 - m.x156)**2 + (m.x162 -
    m.x235)**2 >= 0.46785600000000005)
m.e305 = Constraint(expr= (m.x4 - m.x78)**2 + (m.x83 - m.x157)**2 + (m.x162 -
    m.x236)**2 >= 0.46785600000000005)
m.e306 = Constraint(expr= (m.x4 - m.x79)**2 + (m.x83 - m.x158)**2 + (m.x162 -
    m.x237)**2 >= 0.46785600000000005)
m.e307 = Constraint(expr= (m.x5 - m.x6)**2 + (m.x84 - m.x85)**2 + (m.x163 -
    m.x164)**2 >= 0.46785600000000005)
m.e308 = Constraint(expr= (m.x5 - m.x7)**2 + (m.x84 - m.x86)**2 + (m.x163 -
    m.x165)**2 >= 0.46785600000000005)
m.e309 = Constraint(expr= (m.x5 - m.x8)**2 + (m.x84 - m.x87)**2 + (m.x163 -
    m.x166)**2 >= 0.46785600000000005)
m.e310 = Constraint(expr= (m.x5 - m.x9)**2 + (m.x84 - m.x88)**2 + (m.x163 -
    m.x167)**2 >= 0.46785600000000005)
m.e311 = Constraint(expr= (m.x5 - m.x10)**2 + (m.x84 - m.x89)**2 + (m.x163 -
    m.x168)**2 >= 0.46785600000000005)
m.e312 = Constraint(expr= (m.x5 - m.x11)**2 + (m.x84 - m.x90)**2 + (m.x163 -
    m.x169)**2 >= 0.46785600000000005)
m.e313 = Constraint(expr= (m.x5 - m.x12)**2 + (m.x84 - m.x91)**2 + (m.x163 -
    m.x170)**2 >= 0.46785600000000005)
m.e314 = Constraint(expr= (m.x5 - m.x13)**2 + (m.x84 - m.x92)**2 + (m.x163 -
    m.x171)**2 >= 0.46785600000000005)
m.e315 = Constraint(expr= (m.x5 - m.x14)**2 + (m.x84 - m.x93)**2 + (m.x163 -
    m.x172)**2 >= 0.46785600000000005)
m.e316 = Constraint(expr= (m.x5 - m.x15)**2 + (m.x84 - m.x94)**2 + (m.x163 -
    m.x173)**2 >= 0.46785600000000005)
m.e317 = Constraint(expr= (m.x5 - m.x16)**2 + (m.x84 - m.x95)**2 + (m.x163 -
    m.x174)**2 >= 0.46785600000000005)
m.e318 = Constraint(expr= (m.x5 - m.x17)**2 + (m.x84 - m.x96)**2 + (m.x163 -
    m.x175)**2 >= 0.46785600000000005)
m.e319 = Constraint(expr= (m.x5 - m.x18)**2 + (m.x84 - m.x97)**2 + (m.x163 -
    m.x176)**2 >= 0.46785600000000005)
m.e320 = Constraint(expr= (m.x5 - m.x19)**2 + (m.x84 - m.x98)**2 + (m.x163 -
    m.x177)**2 >= 0.46785600000000005)
m.e321 = Constraint(expr= (m.x5 - m.x20)**2 + (m.x84 - m.x99)**2 + (m.x163 -
    m.x178)**2 >= 0.46785600000000005)
m.e322 = Constraint(expr= (m.x5 - m.x21)**2 + (m.x84 - m.x100)**2 + (m.x163 -
    m.x179)**2 >= 0.46785600000000005)
m.e323 = Constraint(expr= (m.x5 - m.x22)**2 + (m.x84 - m.x101)**2 + (m.x163 -
    m.x180)**2 >= 0.46785600000000005)
m.e324 = Constraint(expr= (m.x5 - m.x23)**2 + (m.x84 - m.x102)**2 + (m.x163 -
    m.x181)**2 >= 0.46785600000000005)
m.e325 = Constraint(expr= (m.x5 - m.x24)**2 + (m.x84 - m.x103)**2 + (m.x163 -
    m.x182)**2 >= 0.46785600000000005)
m.e326 = Constraint(expr= (m.x5 - m.x25)**2 + (m.x84 - m.x104)**2 + (m.x163 -
    m.x183)**2 >= 0.46785600000000005)
m.e327 = Constraint(expr= (m.x5 - m.x26)**2 + (m.x84 - m.x105)**2 + (m.x163 -
    m.x184)**2 >= 0.46785600000000005)
m.e328 = Constraint(expr= (m.x5 - m.x27)**2 + (m.x84 - m.x106)**2 + (m.x163 -
    m.x185)**2 >= 0.46785600000000005)
m.e329 = Constraint(expr= (m.x5 - m.x28)**2 + (m.x84 - m.x107)**2 + (m.x163 -
    m.x186)**2 >= 0.46785600000000005)
m.e330 = Constraint(expr= (m.x5 - m.x29)**2 + (m.x84 - m.x108)**2 + (m.x163 -
    m.x187)**2 >= 0.46785600000000005)
m.e331 = Constraint(expr= (m.x5 - m.x30)**2 + (m.x84 - m.x109)**2 + (m.x163 -
    m.x188)**2 >= 0.46785600000000005)
m.e332 = Constraint(expr= (m.x5 - m.x31)**2 + (m.x84 - m.x110)**2 + (m.x163 -
    m.x189)**2 >= 0.46785600000000005)
m.e333 = Constraint(expr= (m.x5 - m.x32)**2 + (m.x84 - m.x111)**2 + (m.x163 -
    m.x190)**2 >= 0.46785600000000005)
m.e334 = Constraint(expr= (m.x5 - m.x33)**2 + (m.x84 - m.x112)**2 + (m.x163 -
    m.x191)**2 >= 0.46785600000000005)
m.e335 = Constraint(expr= (m.x5 - m.x34)**2 + (m.x84 - m.x113)**2 + (m.x163 -
    m.x192)**2 >= 0.46785600000000005)
m.e336 = Constraint(expr= (m.x5 - m.x35)**2 + (m.x84 - m.x114)**2 + (m.x163 -
    m.x193)**2 >= 0.46785600000000005)
m.e337 = Constraint(expr= (m.x5 - m.x36)**2 + (m.x84 - m.x115)**2 + (m.x163 -
    m.x194)**2 >= 0.46785600000000005)
m.e338 = Constraint(expr= (m.x5 - m.x37)**2 + (m.x84 - m.x116)**2 + (m.x163 -
    m.x195)**2 >= 0.46785600000000005)
m.e339 = Constraint(expr= (m.x5 - m.x38)**2 + (m.x84 - m.x117)**2 + (m.x163 -
    m.x196)**2 >= 0.46785600000000005)
m.e340 = Constraint(expr= (m.x5 - m.x39)**2 + (m.x84 - m.x118)**2 + (m.x163 -
    m.x197)**2 >= 0.46785600000000005)
m.e341 = Constraint(expr= (m.x5 - m.x40)**2 + (m.x84 - m.x119)**2 + (m.x163 -
    m.x198)**2 >= 0.46785600000000005)
m.e342 = Constraint(expr= (m.x5 - m.x41)**2 + (m.x84 - m.x120)**2 + (m.x163 -
    m.x199)**2 >= 0.46785600000000005)
m.e343 = Constraint(expr= (m.x5 - m.x42)**2 + (m.x84 - m.x121)**2 + (m.x163 -
    m.x200)**2 >= 0.46785600000000005)
m.e344 = Constraint(expr= (m.x5 - m.x43)**2 + (m.x84 - m.x122)**2 + (m.x163 -
    m.x201)**2 >= 0.46785600000000005)
m.e345 = Constraint(expr= (m.x5 - m.x44)**2 + (m.x84 - m.x123)**2 + (m.x163 -
    m.x202)**2 >= 0.46785600000000005)
m.e346 = Constraint(expr= (m.x5 - m.x45)**2 + (m.x84 - m.x124)**2 + (m.x163 -
    m.x203)**2 >= 0.46785600000000005)
m.e347 = Constraint(expr= (m.x5 - m.x46)**2 + (m.x84 - m.x125)**2 + (m.x163 -
    m.x204)**2 >= 0.46785600000000005)
m.e348 = Constraint(expr= (m.x5 - m.x47)**2 + (m.x84 - m.x126)**2 + (m.x163 -
    m.x205)**2 >= 0.46785600000000005)
m.e349 = Constraint(expr= (m.x5 - m.x48)**2 + (m.x84 - m.x127)**2 + (m.x163 -
    m.x206)**2 >= 0.46785600000000005)
m.e350 = Constraint(expr= (m.x5 - m.x49)**2 + (m.x84 - m.x128)**2 + (m.x163 -
    m.x207)**2 >= 0.46785600000000005)
m.e351 = Constraint(expr= (m.x5 - m.x50)**2 + (m.x84 - m.x129)**2 + (m.x163 -
    m.x208)**2 >= 0.46785600000000005)
m.e352 = Constraint(expr= (m.x5 - m.x51)**2 + (m.x84 - m.x130)**2 + (m.x163 -
    m.x209)**2 >= 0.46785600000000005)
m.e353 = Constraint(expr= (m.x5 - m.x52)**2 + (m.x84 - m.x131)**2 + (m.x163 -
    m.x210)**2 >= 0.46785600000000005)
m.e354 = Constraint(expr= (m.x5 - m.x53)**2 + (m.x84 - m.x132)**2 + (m.x163 -
    m.x211)**2 >= 0.46785600000000005)
m.e355 = Constraint(expr= (m.x5 - m.x54)**2 + (m.x84 - m.x133)**2 + (m.x163 -
    m.x212)**2 >= 0.46785600000000005)
m.e356 = Constraint(expr= (m.x5 - m.x55)**2 + (m.x84 - m.x134)**2 + (m.x163 -
    m.x213)**2 >= 0.46785600000000005)
m.e357 = Constraint(expr= (m.x5 - m.x56)**2 + (m.x84 - m.x135)**2 + (m.x163 -
    m.x214)**2 >= 0.46785600000000005)
m.e358 = Constraint(expr= (m.x5 - m.x57)**2 + (m.x84 - m.x136)**2 + (m.x163 -
    m.x215)**2 >= 0.46785600000000005)
m.e359 = Constraint(expr= (m.x5 - m.x58)**2 + (m.x84 - m.x137)**2 + (m.x163 -
    m.x216)**2 >= 0.46785600000000005)
m.e360 = Constraint(expr= (m.x5 - m.x59)**2 + (m.x84 - m.x138)**2 + (m.x163 -
    m.x217)**2 >= 0.46785600000000005)
m.e361 = Constraint(expr= (m.x5 - m.x60)**2 + (m.x84 - m.x139)**2 + (m.x163 -
    m.x218)**2 >= 0.46785600000000005)
m.e362 = Constraint(expr= (m.x5 - m.x61)**2 + (m.x84 - m.x140)**2 + (m.x163 -
    m.x219)**2 >= 0.46785600000000005)
m.e363 = Constraint(expr= (m.x5 - m.x62)**2 + (m.x84 - m.x141)**2 + (m.x163 -
    m.x220)**2 >= 0.46785600000000005)
m.e364 = Constraint(expr= (m.x5 - m.x63)**2 + (m.x84 - m.x142)**2 + (m.x163 -
    m.x221)**2 >= 0.46785600000000005)
m.e365 = Constraint(expr= (m.x5 - m.x64)**2 + (m.x84 - m.x143)**2 + (m.x163 -
    m.x222)**2 >= 0.46785600000000005)
m.e366 = Constraint(expr= (m.x5 - m.x65)**2 + (m.x84 - m.x144)**2 + (m.x163 -
    m.x223)**2 >= 0.46785600000000005)
m.e367 = Constraint(expr= (m.x5 - m.x66)**2 + (m.x84 - m.x145)**2 + (m.x163 -
    m.x224)**2 >= 0.46785600000000005)
m.e368 = Constraint(expr= (m.x5 - m.x67)**2 + (m.x84 - m.x146)**2 + (m.x163 -
    m.x225)**2 >= 0.46785600000000005)
m.e369 = Constraint(expr= (m.x5 - m.x68)**2 + (m.x84 - m.x147)**2 + (m.x163 -
    m.x226)**2 >= 0.46785600000000005)
m.e370 = Constraint(expr= (m.x5 - m.x69)**2 + (m.x84 - m.x148)**2 + (m.x163 -
    m.x227)**2 >= 0.46785600000000005)
m.e371 = Constraint(expr= (m.x5 - m.x70)**2 + (m.x84 - m.x149)**2 + (m.x163 -
    m.x228)**2 >= 0.46785600000000005)
m.e372 = Constraint(expr= (m.x5 - m.x71)**2 + (m.x84 - m.x150)**2 + (m.x163 -
    m.x229)**2 >= 0.46785600000000005)
m.e373 = Constraint(expr= (m.x5 - m.x72)**2 + (m.x84 - m.x151)**2 + (m.x163 -
    m.x230)**2 >= 0.46785600000000005)
m.e374 = Constraint(expr= (m.x5 - m.x73)**2 + (m.x84 - m.x152)**2 + (m.x163 -
    m.x231)**2 >= 0.46785600000000005)
m.e375 = Constraint(expr= (m.x5 - m.x74)**2 + (m.x84 - m.x153)**2 + (m.x163 -
    m.x232)**2 >= 0.46785600000000005)
m.e376 = Constraint(expr= (m.x5 - m.x75)**2 + (m.x84 - m.x154)**2 + (m.x163 -
    m.x233)**2 >= 0.46785600000000005)
m.e377 = Constraint(expr= (m.x5 - m.x76)**2 + (m.x84 - m.x155)**2 + (m.x163 -
    m.x234)**2 >= 0.46785600000000005)
m.e378 = Constraint(expr= (m.x5 - m.x77)**2 + (m.x84 - m.x156)**2 + (m.x163 -
    m.x235)**2 >= 0.46785600000000005)
m.e379 = Constraint(expr= (m.x5 - m.x78)**2 + (m.x84 - m.x157)**2 + (m.x163 -
    m.x236)**2 >= 0.46785600000000005)
m.e380 = Constraint(expr= (m.x5 - m.x79)**2 + (m.x84 - m.x158)**2 + (m.x163 -
    m.x237)**2 >= 0.46785600000000005)
m.e381 = Constraint(expr= (m.x6 - m.x7)**2 + (m.x85 - m.x86)**2 + (m.x164 -
    m.x165)**2 >= 0.46785600000000005)
m.e382 = Constraint(expr= (m.x6 - m.x8)**2 + (m.x85 - m.x87)**2 + (m.x164 -
    m.x166)**2 >= 0.46785600000000005)
m.e383 = Constraint(expr= (m.x6 - m.x9)**2 + (m.x85 - m.x88)**2 + (m.x164 -
    m.x167)**2 >= 0.46785600000000005)
m.e384 = Constraint(expr= (m.x6 - m.x10)**2 + (m.x85 - m.x89)**2 + (m.x164 -
    m.x168)**2 >= 0.46785600000000005)
m.e385 = Constraint(expr= (m.x6 - m.x11)**2 + (m.x85 - m.x90)**2 + (m.x164 -
    m.x169)**2 >= 0.46785600000000005)
m.e386 = Constraint(expr= (m.x6 - m.x12)**2 + (m.x85 - m.x91)**2 + (m.x164 -
    m.x170)**2 >= 0.46785600000000005)
m.e387 = Constraint(expr= (m.x6 - m.x13)**2 + (m.x85 - m.x92)**2 + (m.x164 -
    m.x171)**2 >= 0.46785600000000005)
m.e388 = Constraint(expr= (m.x6 - m.x14)**2 + (m.x85 - m.x93)**2 + (m.x164 -
    m.x172)**2 >= 0.46785600000000005)
m.e389 = Constraint(expr= (m.x6 - m.x15)**2 + (m.x85 - m.x94)**2 + (m.x164 -
    m.x173)**2 >= 0.46785600000000005)
m.e390 = Constraint(expr= (m.x6 - m.x16)**2 + (m.x85 - m.x95)**2 + (m.x164 -
    m.x174)**2 >= 0.46785600000000005)
m.e391 = Constraint(expr= (m.x6 - m.x17)**2 + (m.x85 - m.x96)**2 + (m.x164 -
    m.x175)**2 >= 0.46785600000000005)
m.e392 = Constraint(expr= (m.x6 - m.x18)**2 + (m.x85 - m.x97)**2 + (m.x164 -
    m.x176)**2 >= 0.46785600000000005)
m.e393 = Constraint(expr= (m.x6 - m.x19)**2 + (m.x85 - m.x98)**2 + (m.x164 -
    m.x177)**2 >= 0.46785600000000005)
m.e394 = Constraint(expr= (m.x6 - m.x20)**2 + (m.x85 - m.x99)**2 + (m.x164 -
    m.x178)**2 >= 0.46785600000000005)
m.e395 = Constraint(expr= (m.x6 - m.x21)**2 + (m.x85 - m.x100)**2 + (m.x164 -
    m.x179)**2 >= 0.46785600000000005)
m.e396 = Constraint(expr= (m.x6 - m.x22)**2 + (m.x85 - m.x101)**2 + (m.x164 -
    m.x180)**2 >= 0.46785600000000005)
m.e397 = Constraint(expr= (m.x6 - m.x23)**2 + (m.x85 - m.x102)**2 + (m.x164 -
    m.x181)**2 >= 0.46785600000000005)
m.e398 = Constraint(expr= (m.x6 - m.x24)**2 + (m.x85 - m.x103)**2 + (m.x164 -
    m.x182)**2 >= 0.46785600000000005)
m.e399 = Constraint(expr= (m.x6 - m.x25)**2 + (m.x85 - m.x104)**2 + (m.x164 -
    m.x183)**2 >= 0.46785600000000005)
m.e400 = Constraint(expr= (m.x6 - m.x26)**2 + (m.x85 - m.x105)**2 + (m.x164 -
    m.x184)**2 >= 0.46785600000000005)
m.e401 = Constraint(expr= (m.x6 - m.x27)**2 + (m.x85 - m.x106)**2 + (m.x164 -
    m.x185)**2 >= 0.46785600000000005)
m.e402 = Constraint(expr= (m.x6 - m.x28)**2 + (m.x85 - m.x107)**2 + (m.x164 -
    m.x186)**2 >= 0.46785600000000005)
m.e403 = Constraint(expr= (m.x6 - m.x29)**2 + (m.x85 - m.x108)**2 + (m.x164 -
    m.x187)**2 >= 0.46785600000000005)
m.e404 = Constraint(expr= (m.x6 - m.x30)**2 + (m.x85 - m.x109)**2 + (m.x164 -
    m.x188)**2 >= 0.46785600000000005)
m.e405 = Constraint(expr= (m.x6 - m.x31)**2 + (m.x85 - m.x110)**2 + (m.x164 -
    m.x189)**2 >= 0.46785600000000005)
m.e406 = Constraint(expr= (m.x6 - m.x32)**2 + (m.x85 - m.x111)**2 + (m.x164 -
    m.x190)**2 >= 0.46785600000000005)
m.e407 = Constraint(expr= (m.x6 - m.x33)**2 + (m.x85 - m.x112)**2 + (m.x164 -
    m.x191)**2 >= 0.46785600000000005)
m.e408 = Constraint(expr= (m.x6 - m.x34)**2 + (m.x85 - m.x113)**2 + (m.x164 -
    m.x192)**2 >= 0.46785600000000005)
m.e409 = Constraint(expr= (m.x6 - m.x35)**2 + (m.x85 - m.x114)**2 + (m.x164 -
    m.x193)**2 >= 0.46785600000000005)
m.e410 = Constraint(expr= (m.x6 - m.x36)**2 + (m.x85 - m.x115)**2 + (m.x164 -
    m.x194)**2 >= 0.46785600000000005)
m.e411 = Constraint(expr= (m.x6 - m.x37)**2 + (m.x85 - m.x116)**2 + (m.x164 -
    m.x195)**2 >= 0.46785600000000005)
m.e412 = Constraint(expr= (m.x6 - m.x38)**2 + (m.x85 - m.x117)**2 + (m.x164 -
    m.x196)**2 >= 0.46785600000000005)
m.e413 = Constraint(expr= (m.x6 - m.x39)**2 + (m.x85 - m.x118)**2 + (m.x164 -
    m.x197)**2 >= 0.46785600000000005)
m.e414 = Constraint(expr= (m.x6 - m.x40)**2 + (m.x85 - m.x119)**2 + (m.x164 -
    m.x198)**2 >= 0.46785600000000005)
m.e415 = Constraint(expr= (m.x6 - m.x41)**2 + (m.x85 - m.x120)**2 + (m.x164 -
    m.x199)**2 >= 0.46785600000000005)
m.e416 = Constraint(expr= (m.x6 - m.x42)**2 + (m.x85 - m.x121)**2 + (m.x164 -
    m.x200)**2 >= 0.46785600000000005)
m.e417 = Constraint(expr= (m.x6 - m.x43)**2 + (m.x85 - m.x122)**2 + (m.x164 -
    m.x201)**2 >= 0.46785600000000005)
m.e418 = Constraint(expr= (m.x6 - m.x44)**2 + (m.x85 - m.x123)**2 + (m.x164 -
    m.x202)**2 >= 0.46785600000000005)
m.e419 = Constraint(expr= (m.x6 - m.x45)**2 + (m.x85 - m.x124)**2 + (m.x164 -
    m.x203)**2 >= 0.46785600000000005)
m.e420 = Constraint(expr= (m.x6 - m.x46)**2 + (m.x85 - m.x125)**2 + (m.x164 -
    m.x204)**2 >= 0.46785600000000005)
m.e421 = Constraint(expr= (m.x6 - m.x47)**2 + (m.x85 - m.x126)**2 + (m.x164 -
    m.x205)**2 >= 0.46785600000000005)
m.e422 = Constraint(expr= (m.x6 - m.x48)**2 + (m.x85 - m.x127)**2 + (m.x164 -
    m.x206)**2 >= 0.46785600000000005)
m.e423 = Constraint(expr= (m.x6 - m.x49)**2 + (m.x85 - m.x128)**2 + (m.x164 -
    m.x207)**2 >= 0.46785600000000005)
m.e424 = Constraint(expr= (m.x6 - m.x50)**2 + (m.x85 - m.x129)**2 + (m.x164 -
    m.x208)**2 >= 0.46785600000000005)
m.e425 = Constraint(expr= (m.x6 - m.x51)**2 + (m.x85 - m.x130)**2 + (m.x164 -
    m.x209)**2 >= 0.46785600000000005)
m.e426 = Constraint(expr= (m.x6 - m.x52)**2 + (m.x85 - m.x131)**2 + (m.x164 -
    m.x210)**2 >= 0.46785600000000005)
m.e427 = Constraint(expr= (m.x6 - m.x53)**2 + (m.x85 - m.x132)**2 + (m.x164 -
    m.x211)**2 >= 0.46785600000000005)
m.e428 = Constraint(expr= (m.x6 - m.x54)**2 + (m.x85 - m.x133)**2 + (m.x164 -
    m.x212)**2 >= 0.46785600000000005)
m.e429 = Constraint(expr= (m.x6 - m.x55)**2 + (m.x85 - m.x134)**2 + (m.x164 -
    m.x213)**2 >= 0.46785600000000005)
m.e430 = Constraint(expr= (m.x6 - m.x56)**2 + (m.x85 - m.x135)**2 + (m.x164 -
    m.x214)**2 >= 0.46785600000000005)
m.e431 = Constraint(expr= (m.x6 - m.x57)**2 + (m.x85 - m.x136)**2 + (m.x164 -
    m.x215)**2 >= 0.46785600000000005)
m.e432 = Constraint(expr= (m.x6 - m.x58)**2 + (m.x85 - m.x137)**2 + (m.x164 -
    m.x216)**2 >= 0.46785600000000005)
m.e433 = Constraint(expr= (m.x6 - m.x59)**2 + (m.x85 - m.x138)**2 + (m.x164 -
    m.x217)**2 >= 0.46785600000000005)
m.e434 = Constraint(expr= (m.x6 - m.x60)**2 + (m.x85 - m.x139)**2 + (m.x164 -
    m.x218)**2 >= 0.46785600000000005)
m.e435 = Constraint(expr= (m.x6 - m.x61)**2 + (m.x85 - m.x140)**2 + (m.x164 -
    m.x219)**2 >= 0.46785600000000005)
m.e436 = Constraint(expr= (m.x6 - m.x62)**2 + (m.x85 - m.x141)**2 + (m.x164 -
    m.x220)**2 >= 0.46785600000000005)
m.e437 = Constraint(expr= (m.x6 - m.x63)**2 + (m.x85 - m.x142)**2 + (m.x164 -
    m.x221)**2 >= 0.46785600000000005)
m.e438 = Constraint(expr= (m.x6 - m.x64)**2 + (m.x85 - m.x143)**2 + (m.x164 -
    m.x222)**2 >= 0.46785600000000005)
m.e439 = Constraint(expr= (m.x6 - m.x65)**2 + (m.x85 - m.x144)**2 + (m.x164 -
    m.x223)**2 >= 0.46785600000000005)
m.e440 = Constraint(expr= (m.x6 - m.x66)**2 + (m.x85 - m.x145)**2 + (m.x164 -
    m.x224)**2 >= 0.46785600000000005)
m.e441 = Constraint(expr= (m.x6 - m.x67)**2 + (m.x85 - m.x146)**2 + (m.x164 -
    m.x225)**2 >= 0.46785600000000005)
m.e442 = Constraint(expr= (m.x6 - m.x68)**2 + (m.x85 - m.x147)**2 + (m.x164 -
    m.x226)**2 >= 0.46785600000000005)
m.e443 = Constraint(expr= (m.x6 - m.x69)**2 + (m.x85 - m.x148)**2 + (m.x164 -
    m.x227)**2 >= 0.46785600000000005)
m.e444 = Constraint(expr= (m.x6 - m.x70)**2 + (m.x85 - m.x149)**2 + (m.x164 -
    m.x228)**2 >= 0.46785600000000005)
m.e445 = Constraint(expr= (m.x6 - m.x71)**2 + (m.x85 - m.x150)**2 + (m.x164 -
    m.x229)**2 >= 0.46785600000000005)
m.e446 = Constraint(expr= (m.x6 - m.x72)**2 + (m.x85 - m.x151)**2 + (m.x164 -
    m.x230)**2 >= 0.46785600000000005)
m.e447 = Constraint(expr= (m.x6 - m.x73)**2 + (m.x85 - m.x152)**2 + (m.x164 -
    m.x231)**2 >= 0.46785600000000005)
m.e448 = Constraint(expr= (m.x6 - m.x74)**2 + (m.x85 - m.x153)**2 + (m.x164 -
    m.x232)**2 >= 0.46785600000000005)
m.e449 = Constraint(expr= (m.x6 - m.x75)**2 + (m.x85 - m.x154)**2 + (m.x164 -
    m.x233)**2 >= 0.46785600000000005)
m.e450 = Constraint(expr= (m.x6 - m.x76)**2 + (m.x85 - m.x155)**2 + (m.x164 -
    m.x234)**2 >= 0.46785600000000005)
m.e451 = Constraint(expr= (m.x6 - m.x77)**2 + (m.x85 - m.x156)**2 + (m.x164 -
    m.x235)**2 >= 0.46785600000000005)
m.e452 = Constraint(expr= (m.x6 - m.x78)**2 + (m.x85 - m.x157)**2 + (m.x164 -
    m.x236)**2 >= 0.46785600000000005)
m.e453 = Constraint(expr= (m.x6 - m.x79)**2 + (m.x85 - m.x158)**2 + (m.x164 -
    m.x237)**2 >= 0.46785600000000005)
m.e454 = Constraint(expr= (m.x7 - m.x8)**2 + (m.x86 - m.x87)**2 + (m.x165 -
    m.x166)**2 >= 0.46785600000000005)
m.e455 = Constraint(expr= (m.x7 - m.x9)**2 + (m.x86 - m.x88)**2 + (m.x165 -
    m.x167)**2 >= 0.46785600000000005)
m.e456 = Constraint(expr= (m.x7 - m.x10)**2 + (m.x86 - m.x89)**2 + (m.x165 -
    m.x168)**2 >= 0.46785600000000005)
m.e457 = Constraint(expr= (m.x7 - m.x11)**2 + (m.x86 - m.x90)**2 + (m.x165 -
    m.x169)**2 >= 0.46785600000000005)
m.e458 = Constraint(expr= (m.x7 - m.x12)**2 + (m.x86 - m.x91)**2 + (m.x165 -
    m.x170)**2 >= 0.46785600000000005)
m.e459 = Constraint(expr= (m.x7 - m.x13)**2 + (m.x86 - m.x92)**2 + (m.x165 -
    m.x171)**2 >= 0.46785600000000005)
m.e460 = Constraint(expr= (m.x7 - m.x14)**2 + (m.x86 - m.x93)**2 + (m.x165 -
    m.x172)**2 >= 0.46785600000000005)
m.e461 = Constraint(expr= (m.x7 - m.x15)**2 + (m.x86 - m.x94)**2 + (m.x165 -
    m.x173)**2 >= 0.46785600000000005)
m.e462 = Constraint(expr= (m.x7 - m.x16)**2 + (m.x86 - m.x95)**2 + (m.x165 -
    m.x174)**2 >= 0.46785600000000005)
m.e463 = Constraint(expr= (m.x7 - m.x17)**2 + (m.x86 - m.x96)**2 + (m.x165 -
    m.x175)**2 >= 0.46785600000000005)
m.e464 = Constraint(expr= (m.x7 - m.x18)**2 + (m.x86 - m.x97)**2 + (m.x165 -
    m.x176)**2 >= 0.46785600000000005)
m.e465 = Constraint(expr= (m.x7 - m.x19)**2 + (m.x86 - m.x98)**2 + (m.x165 -
    m.x177)**2 >= 0.46785600000000005)
m.e466 = Constraint(expr= (m.x7 - m.x20)**2 + (m.x86 - m.x99)**2 + (m.x165 -
    m.x178)**2 >= 0.46785600000000005)
m.e467 = Constraint(expr= (m.x7 - m.x21)**2 + (m.x86 - m.x100)**2 + (m.x165 -
    m.x179)**2 >= 0.46785600000000005)
m.e468 = Constraint(expr= (m.x7 - m.x22)**2 + (m.x86 - m.x101)**2 + (m.x165 -
    m.x180)**2 >= 0.46785600000000005)
m.e469 = Constraint(expr= (m.x7 - m.x23)**2 + (m.x86 - m.x102)**2 + (m.x165 -
    m.x181)**2 >= 0.46785600000000005)
m.e470 = Constraint(expr= (m.x7 - m.x24)**2 + (m.x86 - m.x103)**2 + (m.x165 -
    m.x182)**2 >= 0.46785600000000005)
m.e471 = Constraint(expr= (m.x7 - m.x25)**2 + (m.x86 - m.x104)**2 + (m.x165 -
    m.x183)**2 >= 0.46785600000000005)
m.e472 = Constraint(expr= (m.x7 - m.x26)**2 + (m.x86 - m.x105)**2 + (m.x165 -
    m.x184)**2 >= 0.46785600000000005)
m.e473 = Constraint(expr= (m.x7 - m.x27)**2 + (m.x86 - m.x106)**2 + (m.x165 -
    m.x185)**2 >= 0.46785600000000005)
m.e474 = Constraint(expr= (m.x7 - m.x28)**2 + (m.x86 - m.x107)**2 + (m.x165 -
    m.x186)**2 >= 0.46785600000000005)
m.e475 = Constraint(expr= (m.x7 - m.x29)**2 + (m.x86 - m.x108)**2 + (m.x165 -
    m.x187)**2 >= 0.46785600000000005)
m.e476 = Constraint(expr= (m.x7 - m.x30)**2 + (m.x86 - m.x109)**2 + (m.x165 -
    m.x188)**2 >= 0.46785600000000005)
m.e477 = Constraint(expr= (m.x7 - m.x31)**2 + (m.x86 - m.x110)**2 + (m.x165 -
    m.x189)**2 >= 0.46785600000000005)
m.e478 = Constraint(expr= (m.x7 - m.x32)**2 + (m.x86 - m.x111)**2 + (m.x165 -
    m.x190)**2 >= 0.46785600000000005)
m.e479 = Constraint(expr= (m.x7 - m.x33)**2 + (m.x86 - m.x112)**2 + (m.x165 -
    m.x191)**2 >= 0.46785600000000005)
m.e480 = Constraint(expr= (m.x7 - m.x34)**2 + (m.x86 - m.x113)**2 + (m.x165 -
    m.x192)**2 >= 0.46785600000000005)
m.e481 = Constraint(expr= (m.x7 - m.x35)**2 + (m.x86 - m.x114)**2 + (m.x165 -
    m.x193)**2 >= 0.46785600000000005)
m.e482 = Constraint(expr= (m.x7 - m.x36)**2 + (m.x86 - m.x115)**2 + (m.x165 -
    m.x194)**2 >= 0.46785600000000005)
m.e483 = Constraint(expr= (m.x7 - m.x37)**2 + (m.x86 - m.x116)**2 + (m.x165 -
    m.x195)**2 >= 0.46785600000000005)
m.e484 = Constraint(expr= (m.x7 - m.x38)**2 + (m.x86 - m.x117)**2 + (m.x165 -
    m.x196)**2 >= 0.46785600000000005)
m.e485 = Constraint(expr= (m.x7 - m.x39)**2 + (m.x86 - m.x118)**2 + (m.x165 -
    m.x197)**2 >= 0.46785600000000005)
m.e486 = Constraint(expr= (m.x7 - m.x40)**2 + (m.x86 - m.x119)**2 + (m.x165 -
    m.x198)**2 >= 0.46785600000000005)
m.e487 = Constraint(expr= (m.x7 - m.x41)**2 + (m.x86 - m.x120)**2 + (m.x165 -
    m.x199)**2 >= 0.46785600000000005)
m.e488 = Constraint(expr= (m.x7 - m.x42)**2 + (m.x86 - m.x121)**2 + (m.x165 -
    m.x200)**2 >= 0.46785600000000005)
m.e489 = Constraint(expr= (m.x7 - m.x43)**2 + (m.x86 - m.x122)**2 + (m.x165 -
    m.x201)**2 >= 0.46785600000000005)
m.e490 = Constraint(expr= (m.x7 - m.x44)**2 + (m.x86 - m.x123)**2 + (m.x165 -
    m.x202)**2 >= 0.46785600000000005)
m.e491 = Constraint(expr= (m.x7 - m.x45)**2 + (m.x86 - m.x124)**2 + (m.x165 -
    m.x203)**2 >= 0.46785600000000005)
m.e492 = Constraint(expr= (m.x7 - m.x46)**2 + (m.x86 - m.x125)**2 + (m.x165 -
    m.x204)**2 >= 0.46785600000000005)
m.e493 = Constraint(expr= (m.x7 - m.x47)**2 + (m.x86 - m.x126)**2 + (m.x165 -
    m.x205)**2 >= 0.46785600000000005)
m.e494 = Constraint(expr= (m.x7 - m.x48)**2 + (m.x86 - m.x127)**2 + (m.x165 -
    m.x206)**2 >= 0.46785600000000005)
m.e495 = Constraint(expr= (m.x7 - m.x49)**2 + (m.x86 - m.x128)**2 + (m.x165 -
    m.x207)**2 >= 0.46785600000000005)
m.e496 = Constraint(expr= (m.x7 - m.x50)**2 + (m.x86 - m.x129)**2 + (m.x165 -
    m.x208)**2 >= 0.46785600000000005)
m.e497 = Constraint(expr= (m.x7 - m.x51)**2 + (m.x86 - m.x130)**2 + (m.x165 -
    m.x209)**2 >= 0.46785600000000005)
m.e498 = Constraint(expr= (m.x7 - m.x52)**2 + (m.x86 - m.x131)**2 + (m.x165 -
    m.x210)**2 >= 0.46785600000000005)
m.e499 = Constraint(expr= (m.x7 - m.x53)**2 + (m.x86 - m.x132)**2 + (m.x165 -
    m.x211)**2 >= 0.46785600000000005)
m.e500 = Constraint(expr= (m.x7 - m.x54)**2 + (m.x86 - m.x133)**2 + (m.x165 -
    m.x212)**2 >= 0.46785600000000005)
m.e501 = Constraint(expr= (m.x7 - m.x55)**2 + (m.x86 - m.x134)**2 + (m.x165 -
    m.x213)**2 >= 0.46785600000000005)
m.e502 = Constraint(expr= (m.x7 - m.x56)**2 + (m.x86 - m.x135)**2 + (m.x165 -
    m.x214)**2 >= 0.46785600000000005)
m.e503 = Constraint(expr= (m.x7 - m.x57)**2 + (m.x86 - m.x136)**2 + (m.x165 -
    m.x215)**2 >= 0.46785600000000005)
m.e504 = Constraint(expr= (m.x7 - m.x58)**2 + (m.x86 - m.x137)**2 + (m.x165 -
    m.x216)**2 >= 0.46785600000000005)
m.e505 = Constraint(expr= (m.x7 - m.x59)**2 + (m.x86 - m.x138)**2 + (m.x165 -
    m.x217)**2 >= 0.46785600000000005)
m.e506 = Constraint(expr= (m.x7 - m.x60)**2 + (m.x86 - m.x139)**2 + (m.x165 -
    m.x218)**2 >= 0.46785600000000005)
m.e507 = Constraint(expr= (m.x7 - m.x61)**2 + (m.x86 - m.x140)**2 + (m.x165 -
    m.x219)**2 >= 0.46785600000000005)
m.e508 = Constraint(expr= (m.x7 - m.x62)**2 + (m.x86 - m.x141)**2 + (m.x165 -
    m.x220)**2 >= 0.46785600000000005)
m.e509 = Constraint(expr= (m.x7 - m.x63)**2 + (m.x86 - m.x142)**2 + (m.x165 -
    m.x221)**2 >= 0.46785600000000005)
m.e510 = Constraint(expr= (m.x7 - m.x64)**2 + (m.x86 - m.x143)**2 + (m.x165 -
    m.x222)**2 >= 0.46785600000000005)
m.e511 = Constraint(expr= (m.x7 - m.x65)**2 + (m.x86 - m.x144)**2 + (m.x165 -
    m.x223)**2 >= 0.46785600000000005)
m.e512 = Constraint(expr= (m.x7 - m.x66)**2 + (m.x86 - m.x145)**2 + (m.x165 -
    m.x224)**2 >= 0.46785600000000005)
m.e513 = Constraint(expr= (m.x7 - m.x67)**2 + (m.x86 - m.x146)**2 + (m.x165 -
    m.x225)**2 >= 0.46785600000000005)
m.e514 = Constraint(expr= (m.x7 - m.x68)**2 + (m.x86 - m.x147)**2 + (m.x165 -
    m.x226)**2 >= 0.46785600000000005)
m.e515 = Constraint(expr= (m.x7 - m.x69)**2 + (m.x86 - m.x148)**2 + (m.x165 -
    m.x227)**2 >= 0.46785600000000005)
m.e516 = Constraint(expr= (m.x7 - m.x70)**2 + (m.x86 - m.x149)**2 + (m.x165 -
    m.x228)**2 >= 0.46785600000000005)
m.e517 = Constraint(expr= (m.x7 - m.x71)**2 + (m.x86 - m.x150)**2 + (m.x165 -
    m.x229)**2 >= 0.46785600000000005)
m.e518 = Constraint(expr= (m.x7 - m.x72)**2 + (m.x86 - m.x151)**2 + (m.x165 -
    m.x230)**2 >= 0.46785600000000005)
m.e519 = Constraint(expr= (m.x7 - m.x73)**2 + (m.x86 - m.x152)**2 + (m.x165 -
    m.x231)**2 >= 0.46785600000000005)
m.e520 = Constraint(expr= (m.x7 - m.x74)**2 + (m.x86 - m.x153)**2 + (m.x165 -
    m.x232)**2 >= 0.46785600000000005)
m.e521 = Constraint(expr= (m.x7 - m.x75)**2 + (m.x86 - m.x154)**2 + (m.x165 -
    m.x233)**2 >= 0.46785600000000005)
m.e522 = Constraint(expr= (m.x7 - m.x76)**2 + (m.x86 - m.x155)**2 + (m.x165 -
    m.x234)**2 >= 0.46785600000000005)
m.e523 = Constraint(expr= (m.x7 - m.x77)**2 + (m.x86 - m.x156)**2 + (m.x165 -
    m.x235)**2 >= 0.46785600000000005)
m.e524 = Constraint(expr= (m.x7 - m.x78)**2 + (m.x86 - m.x157)**2 + (m.x165 -
    m.x236)**2 >= 0.46785600000000005)
m.e525 = Constraint(expr= (m.x7 - m.x79)**2 + (m.x86 - m.x158)**2 + (m.x165 -
    m.x237)**2 >= 0.46785600000000005)
m.e526 = Constraint(expr= (m.x8 - m.x9)**2 + (m.x87 - m.x88)**2 + (m.x166 -
    m.x167)**2 >= 0.46785600000000005)
m.e527 = Constraint(expr= (m.x8 - m.x10)**2 + (m.x87 - m.x89)**2 + (m.x166 -
    m.x168)**2 >= 0.46785600000000005)
m.e528 = Constraint(expr= (m.x8 - m.x11)**2 + (m.x87 - m.x90)**2 + (m.x166 -
    m.x169)**2 >= 0.46785600000000005)
m.e529 = Constraint(expr= (m.x8 - m.x12)**2 + (m.x87 - m.x91)**2 + (m.x166 -
    m.x170)**2 >= 0.46785600000000005)
m.e530 = Constraint(expr= (m.x8 - m.x13)**2 + (m.x87 - m.x92)**2 + (m.x166 -
    m.x171)**2 >= 0.46785600000000005)
m.e531 = Constraint(expr= (m.x8 - m.x14)**2 + (m.x87 - m.x93)**2 + (m.x166 -
    m.x172)**2 >= 0.46785600000000005)
m.e532 = Constraint(expr= (m.x8 - m.x15)**2 + (m.x87 - m.x94)**2 + (m.x166 -
    m.x173)**2 >= 0.46785600000000005)
m.e533 = Constraint(expr= (m.x8 - m.x16)**2 + (m.x87 - m.x95)**2 + (m.x166 -
    m.x174)**2 >= 0.46785600000000005)
m.e534 = Constraint(expr= (m.x8 - m.x17)**2 + (m.x87 - m.x96)**2 + (m.x166 -
    m.x175)**2 >= 0.46785600000000005)
m.e535 = Constraint(expr= (m.x8 - m.x18)**2 + (m.x87 - m.x97)**2 + (m.x166 -
    m.x176)**2 >= 0.46785600000000005)
m.e536 = Constraint(expr= (m.x8 - m.x19)**2 + (m.x87 - m.x98)**2 + (m.x166 -
    m.x177)**2 >= 0.46785600000000005)
m.e537 = Constraint(expr= (m.x8 - m.x20)**2 + (m.x87 - m.x99)**2 + (m.x166 -
    m.x178)**2 >= 0.46785600000000005)
m.e538 = Constraint(expr= (m.x8 - m.x21)**2 + (m.x87 - m.x100)**2 + (m.x166 -
    m.x179)**2 >= 0.46785600000000005)
m.e539 = Constraint(expr= (m.x8 - m.x22)**2 + (m.x87 - m.x101)**2 + (m.x166 -
    m.x180)**2 >= 0.46785600000000005)
m.e540 = Constraint(expr= (m.x8 - m.x23)**2 + (m.x87 - m.x102)**2 + (m.x166 -
    m.x181)**2 >= 0.46785600000000005)
m.e541 = Constraint(expr= (m.x8 - m.x24)**2 + (m.x87 - m.x103)**2 + (m.x166 -
    m.x182)**2 >= 0.46785600000000005)
m.e542 = Constraint(expr= (m.x8 - m.x25)**2 + (m.x87 - m.x104)**2 + (m.x166 -
    m.x183)**2 >= 0.46785600000000005)
m.e543 = Constraint(expr= (m.x8 - m.x26)**2 + (m.x87 - m.x105)**2 + (m.x166 -
    m.x184)**2 >= 0.46785600000000005)
m.e544 = Constraint(expr= (m.x8 - m.x27)**2 + (m.x87 - m.x106)**2 + (m.x166 -
    m.x185)**2 >= 0.46785600000000005)
m.e545 = Constraint(expr= (m.x8 - m.x28)**2 + (m.x87 - m.x107)**2 + (m.x166 -
    m.x186)**2 >= 0.46785600000000005)
m.e546 = Constraint(expr= (m.x8 - m.x29)**2 + (m.x87 - m.x108)**2 + (m.x166 -
    m.x187)**2 >= 0.46785600000000005)
m.e547 = Constraint(expr= (m.x8 - m.x30)**2 + (m.x87 - m.x109)**2 + (m.x166 -
    m.x188)**2 >= 0.46785600000000005)
m.e548 = Constraint(expr= (m.x8 - m.x31)**2 + (m.x87 - m.x110)**2 + (m.x166 -
    m.x189)**2 >= 0.46785600000000005)
m.e549 = Constraint(expr= (m.x8 - m.x32)**2 + (m.x87 - m.x111)**2 + (m.x166 -
    m.x190)**2 >= 0.46785600000000005)
m.e550 = Constraint(expr= (m.x8 - m.x33)**2 + (m.x87 - m.x112)**2 + (m.x166 -
    m.x191)**2 >= 0.46785600000000005)
m.e551 = Constraint(expr= (m.x8 - m.x34)**2 + (m.x87 - m.x113)**2 + (m.x166 -
    m.x192)**2 >= 0.46785600000000005)
m.e552 = Constraint(expr= (m.x8 - m.x35)**2 + (m.x87 - m.x114)**2 + (m.x166 -
    m.x193)**2 >= 0.46785600000000005)
m.e553 = Constraint(expr= (m.x8 - m.x36)**2 + (m.x87 - m.x115)**2 + (m.x166 -
    m.x194)**2 >= 0.46785600000000005)
m.e554 = Constraint(expr= (m.x8 - m.x37)**2 + (m.x87 - m.x116)**2 + (m.x166 -
    m.x195)**2 >= 0.46785600000000005)
m.e555 = Constraint(expr= (m.x8 - m.x38)**2 + (m.x87 - m.x117)**2 + (m.x166 -
    m.x196)**2 >= 0.46785600000000005)
m.e556 = Constraint(expr= (m.x8 - m.x39)**2 + (m.x87 - m.x118)**2 + (m.x166 -
    m.x197)**2 >= 0.46785600000000005)
m.e557 = Constraint(expr= (m.x8 - m.x40)**2 + (m.x87 - m.x119)**2 + (m.x166 -
    m.x198)**2 >= 0.46785600000000005)
m.e558 = Constraint(expr= (m.x8 - m.x41)**2 + (m.x87 - m.x120)**2 + (m.x166 -
    m.x199)**2 >= 0.46785600000000005)
m.e559 = Constraint(expr= (m.x8 - m.x42)**2 + (m.x87 - m.x121)**2 + (m.x166 -
    m.x200)**2 >= 0.46785600000000005)
m.e560 = Constraint(expr= (m.x8 - m.x43)**2 + (m.x87 - m.x122)**2 + (m.x166 -
    m.x201)**2 >= 0.46785600000000005)
m.e561 = Constraint(expr= (m.x8 - m.x44)**2 + (m.x87 - m.x123)**2 + (m.x166 -
    m.x202)**2 >= 0.46785600000000005)
m.e562 = Constraint(expr= (m.x8 - m.x45)**2 + (m.x87 - m.x124)**2 + (m.x166 -
    m.x203)**2 >= 0.46785600000000005)
m.e563 = Constraint(expr= (m.x8 - m.x46)**2 + (m.x87 - m.x125)**2 + (m.x166 -
    m.x204)**2 >= 0.46785600000000005)
m.e564 = Constraint(expr= (m.x8 - m.x47)**2 + (m.x87 - m.x126)**2 + (m.x166 -
    m.x205)**2 >= 0.46785600000000005)
m.e565 = Constraint(expr= (m.x8 - m.x48)**2 + (m.x87 - m.x127)**2 + (m.x166 -
    m.x206)**2 >= 0.46785600000000005)
m.e566 = Constraint(expr= (m.x8 - m.x49)**2 + (m.x87 - m.x128)**2 + (m.x166 -
    m.x207)**2 >= 0.46785600000000005)
m.e567 = Constraint(expr= (m.x8 - m.x50)**2 + (m.x87 - m.x129)**2 + (m.x166 -
    m.x208)**2 >= 0.46785600000000005)
m.e568 = Constraint(expr= (m.x8 - m.x51)**2 + (m.x87 - m.x130)**2 + (m.x166 -
    m.x209)**2 >= 0.46785600000000005)
m.e569 = Constraint(expr= (m.x8 - m.x52)**2 + (m.x87 - m.x131)**2 + (m.x166 -
    m.x210)**2 >= 0.46785600000000005)
m.e570 = Constraint(expr= (m.x8 - m.x53)**2 + (m.x87 - m.x132)**2 + (m.x166 -
    m.x211)**2 >= 0.46785600000000005)
m.e571 = Constraint(expr= (m.x8 - m.x54)**2 + (m.x87 - m.x133)**2 + (m.x166 -
    m.x212)**2 >= 0.46785600000000005)
m.e572 = Constraint(expr= (m.x8 - m.x55)**2 + (m.x87 - m.x134)**2 + (m.x166 -
    m.x213)**2 >= 0.46785600000000005)
m.e573 = Constraint(expr= (m.x8 - m.x56)**2 + (m.x87 - m.x135)**2 + (m.x166 -
    m.x214)**2 >= 0.46785600000000005)
m.e574 = Constraint(expr= (m.x8 - m.x57)**2 + (m.x87 - m.x136)**2 + (m.x166 -
    m.x215)**2 >= 0.46785600000000005)
m.e575 = Constraint(expr= (m.x8 - m.x58)**2 + (m.x87 - m.x137)**2 + (m.x166 -
    m.x216)**2 >= 0.46785600000000005)
m.e576 = Constraint(expr= (m.x8 - m.x59)**2 + (m.x87 - m.x138)**2 + (m.x166 -
    m.x217)**2 >= 0.46785600000000005)
m.e577 = Constraint(expr= (m.x8 - m.x60)**2 + (m.x87 - m.x139)**2 + (m.x166 -
    m.x218)**2 >= 0.46785600000000005)
m.e578 = Constraint(expr= (m.x8 - m.x61)**2 + (m.x87 - m.x140)**2 + (m.x166 -
    m.x219)**2 >= 0.46785600000000005)
m.e579 = Constraint(expr= (m.x8 - m.x62)**2 + (m.x87 - m.x141)**2 + (m.x166 -
    m.x220)**2 >= 0.46785600000000005)
m.e580 = Constraint(expr= (m.x8 - m.x63)**2 + (m.x87 - m.x142)**2 + (m.x166 -
    m.x221)**2 >= 0.46785600000000005)
m.e581 = Constraint(expr= (m.x8 - m.x64)**2 + (m.x87 - m.x143)**2 + (m.x166 -
    m.x222)**2 >= 0.46785600000000005)
m.e582 = Constraint(expr= (m.x8 - m.x65)**2 + (m.x87 - m.x144)**2 + (m.x166 -
    m.x223)**2 >= 0.46785600000000005)
m.e583 = Constraint(expr= (m.x8 - m.x66)**2 + (m.x87 - m.x145)**2 + (m.x166 -
    m.x224)**2 >= 0.46785600000000005)
m.e584 = Constraint(expr= (m.x8 - m.x67)**2 + (m.x87 - m.x146)**2 + (m.x166 -
    m.x225)**2 >= 0.46785600000000005)
m.e585 = Constraint(expr= (m.x8 - m.x68)**2 + (m.x87 - m.x147)**2 + (m.x166 -
    m.x226)**2 >= 0.46785600000000005)
m.e586 = Constraint(expr= (m.x8 - m.x69)**2 + (m.x87 - m.x148)**2 + (m.x166 -
    m.x227)**2 >= 0.46785600000000005)
m.e587 = Constraint(expr= (m.x8 - m.x70)**2 + (m.x87 - m.x149)**2 + (m.x166 -
    m.x228)**2 >= 0.46785600000000005)
m.e588 = Constraint(expr= (m.x8 - m.x71)**2 + (m.x87 - m.x150)**2 + (m.x166 -
    m.x229)**2 >= 0.46785600000000005)
m.e589 = Constraint(expr= (m.x8 - m.x72)**2 + (m.x87 - m.x151)**2 + (m.x166 -
    m.x230)**2 >= 0.46785600000000005)
m.e590 = Constraint(expr= (m.x8 - m.x73)**2 + (m.x87 - m.x152)**2 + (m.x166 -
    m.x231)**2 >= 0.46785600000000005)
m.e591 = Constraint(expr= (m.x8 - m.x74)**2 + (m.x87 - m.x153)**2 + (m.x166 -
    m.x232)**2 >= 0.46785600000000005)
m.e592 = Constraint(expr= (m.x8 - m.x75)**2 + (m.x87 - m.x154)**2 + (m.x166 -
    m.x233)**2 >= 0.46785600000000005)
m.e593 = Constraint(expr= (m.x8 - m.x76)**2 + (m.x87 - m.x155)**2 + (m.x166 -
    m.x234)**2 >= 0.46785600000000005)
m.e594 = Constraint(expr= (m.x8 - m.x77)**2 + (m.x87 - m.x156)**2 + (m.x166 -
    m.x235)**2 >= 0.46785600000000005)
m.e595 = Constraint(expr= (m.x8 - m.x78)**2 + (m.x87 - m.x157)**2 + (m.x166 -
    m.x236)**2 >= 0.46785600000000005)
m.e596 = Constraint(expr= (m.x8 - m.x79)**2 + (m.x87 - m.x158)**2 + (m.x166 -
    m.x237)**2 >= 0.46785600000000005)
m.e597 = Constraint(expr= (m.x9 - m.x10)**2 + (m.x88 - m.x89)**2 + (m.x167 -
    m.x168)**2 >= 0.46785600000000005)
m.e598 = Constraint(expr= (m.x9 - m.x11)**2 + (m.x88 - m.x90)**2 + (m.x167 -
    m.x169)**2 >= 0.46785600000000005)
m.e599 = Constraint(expr= (m.x9 - m.x12)**2 + (m.x88 - m.x91)**2 + (m.x167 -
    m.x170)**2 >= 0.46785600000000005)
m.e600 = Constraint(expr= (m.x9 - m.x13)**2 + (m.x88 - m.x92)**2 + (m.x167 -
    m.x171)**2 >= 0.46785600000000005)
m.e601 = Constraint(expr= (m.x9 - m.x14)**2 + (m.x88 - m.x93)**2 + (m.x167 -
    m.x172)**2 >= 0.46785600000000005)
m.e602 = Constraint(expr= (m.x9 - m.x15)**2 + (m.x88 - m.x94)**2 + (m.x167 -
    m.x173)**2 >= 0.46785600000000005)
m.e603 = Constraint(expr= (m.x9 - m.x16)**2 + (m.x88 - m.x95)**2 + (m.x167 -
    m.x174)**2 >= 0.46785600000000005)
m.e604 = Constraint(expr= (m.x9 - m.x17)**2 + (m.x88 - m.x96)**2 + (m.x167 -
    m.x175)**2 >= 0.46785600000000005)
m.e605 = Constraint(expr= (m.x9 - m.x18)**2 + (m.x88 - m.x97)**2 + (m.x167 -
    m.x176)**2 >= 0.46785600000000005)
m.e606 = Constraint(expr= (m.x9 - m.x19)**2 + (m.x88 - m.x98)**2 + (m.x167 -
    m.x177)**2 >= 0.46785600000000005)
m.e607 = Constraint(expr= (m.x9 - m.x20)**2 + (m.x88 - m.x99)**2 + (m.x167 -
    m.x178)**2 >= 0.46785600000000005)
m.e608 = Constraint(expr= (m.x9 - m.x21)**2 + (m.x88 - m.x100)**2 + (m.x167 -
    m.x179)**2 >= 0.46785600000000005)
m.e609 = Constraint(expr= (m.x9 - m.x22)**2 + (m.x88 - m.x101)**2 + (m.x167 -
    m.x180)**2 >= 0.46785600000000005)
m.e610 = Constraint(expr= (m.x9 - m.x23)**2 + (m.x88 - m.x102)**2 + (m.x167 -
    m.x181)**2 >= 0.46785600000000005)
m.e611 = Constraint(expr= (m.x9 - m.x24)**2 + (m.x88 - m.x103)**2 + (m.x167 -
    m.x182)**2 >= 0.46785600000000005)
m.e612 = Constraint(expr= (m.x9 - m.x25)**2 + (m.x88 - m.x104)**2 + (m.x167 -
    m.x183)**2 >= 0.46785600000000005)
m.e613 = Constraint(expr= (m.x9 - m.x26)**2 + (m.x88 - m.x105)**2 + (m.x167 -
    m.x184)**2 >= 0.46785600000000005)
m.e614 = Constraint(expr= (m.x9 - m.x27)**2 + (m.x88 - m.x106)**2 + (m.x167 -
    m.x185)**2 >= 0.46785600000000005)
m.e615 = Constraint(expr= (m.x9 - m.x28)**2 + (m.x88 - m.x107)**2 + (m.x167 -
    m.x186)**2 >= 0.46785600000000005)
m.e616 = Constraint(expr= (m.x9 - m.x29)**2 + (m.x88 - m.x108)**2 + (m.x167 -
    m.x187)**2 >= 0.46785600000000005)
m.e617 = Constraint(expr= (m.x9 - m.x30)**2 + (m.x88 - m.x109)**2 + (m.x167 -
    m.x188)**2 >= 0.46785600000000005)
m.e618 = Constraint(expr= (m.x9 - m.x31)**2 + (m.x88 - m.x110)**2 + (m.x167 -
    m.x189)**2 >= 0.46785600000000005)
m.e619 = Constraint(expr= (m.x9 - m.x32)**2 + (m.x88 - m.x111)**2 + (m.x167 -
    m.x190)**2 >= 0.46785600000000005)
m.e620 = Constraint(expr= (m.x9 - m.x33)**2 + (m.x88 - m.x112)**2 + (m.x167 -
    m.x191)**2 >= 0.46785600000000005)
m.e621 = Constraint(expr= (m.x9 - m.x34)**2 + (m.x88 - m.x113)**2 + (m.x167 -
    m.x192)**2 >= 0.46785600000000005)
m.e622 = Constraint(expr= (m.x9 - m.x35)**2 + (m.x88 - m.x114)**2 + (m.x167 -
    m.x193)**2 >= 0.46785600000000005)
m.e623 = Constraint(expr= (m.x9 - m.x36)**2 + (m.x88 - m.x115)**2 + (m.x167 -
    m.x194)**2 >= 0.46785600000000005)
m.e624 = Constraint(expr= (m.x9 - m.x37)**2 + (m.x88 - m.x116)**2 + (m.x167 -
    m.x195)**2 >= 0.46785600000000005)
m.e625 = Constraint(expr= (m.x9 - m.x38)**2 + (m.x88 - m.x117)**2 + (m.x167 -
    m.x196)**2 >= 0.46785600000000005)
m.e626 = Constraint(expr= (m.x9 - m.x39)**2 + (m.x88 - m.x118)**2 + (m.x167 -
    m.x197)**2 >= 0.46785600000000005)
m.e627 = Constraint(expr= (m.x9 - m.x40)**2 + (m.x88 - m.x119)**2 + (m.x167 -
    m.x198)**2 >= 0.46785600000000005)
m.e628 = Constraint(expr= (m.x9 - m.x41)**2 + (m.x88 - m.x120)**2 + (m.x167 -
    m.x199)**2 >= 0.46785600000000005)
m.e629 = Constraint(expr= (m.x9 - m.x42)**2 + (m.x88 - m.x121)**2 + (m.x167 -
    m.x200)**2 >= 0.46785600000000005)
m.e630 = Constraint(expr= (m.x9 - m.x43)**2 + (m.x88 - m.x122)**2 + (m.x167 -
    m.x201)**2 >= 0.46785600000000005)
m.e631 = Constraint(expr= (m.x9 - m.x44)**2 + (m.x88 - m.x123)**2 + (m.x167 -
    m.x202)**2 >= 0.46785600000000005)
m.e632 = Constraint(expr= (m.x9 - m.x45)**2 + (m.x88 - m.x124)**2 + (m.x167 -
    m.x203)**2 >= 0.46785600000000005)
m.e633 = Constraint(expr= (m.x9 - m.x46)**2 + (m.x88 - m.x125)**2 + (m.x167 -
    m.x204)**2 >= 0.46785600000000005)
m.e634 = Constraint(expr= (m.x9 - m.x47)**2 + (m.x88 - m.x126)**2 + (m.x167 -
    m.x205)**2 >= 0.46785600000000005)
m.e635 = Constraint(expr= (m.x9 - m.x48)**2 + (m.x88 - m.x127)**2 + (m.x167 -
    m.x206)**2 >= 0.46785600000000005)
m.e636 = Constraint(expr= (m.x9 - m.x49)**2 + (m.x88 - m.x128)**2 + (m.x167 -
    m.x207)**2 >= 0.46785600000000005)
m.e637 = Constraint(expr= (m.x9 - m.x50)**2 + (m.x88 - m.x129)**2 + (m.x167 -
    m.x208)**2 >= 0.46785600000000005)
m.e638 = Constraint(expr= (m.x9 - m.x51)**2 + (m.x88 - m.x130)**2 + (m.x167 -
    m.x209)**2 >= 0.46785600000000005)
m.e639 = Constraint(expr= (m.x9 - m.x52)**2 + (m.x88 - m.x131)**2 + (m.x167 -
    m.x210)**2 >= 0.46785600000000005)
m.e640 = Constraint(expr= (m.x9 - m.x53)**2 + (m.x88 - m.x132)**2 + (m.x167 -
    m.x211)**2 >= 0.46785600000000005)
m.e641 = Constraint(expr= (m.x9 - m.x54)**2 + (m.x88 - m.x133)**2 + (m.x167 -
    m.x212)**2 >= 0.46785600000000005)
m.e642 = Constraint(expr= (m.x9 - m.x55)**2 + (m.x88 - m.x134)**2 + (m.x167 -
    m.x213)**2 >= 0.46785600000000005)
m.e643 = Constraint(expr= (m.x9 - m.x56)**2 + (m.x88 - m.x135)**2 + (m.x167 -
    m.x214)**2 >= 0.46785600000000005)
m.e644 = Constraint(expr= (m.x9 - m.x57)**2 + (m.x88 - m.x136)**2 + (m.x167 -
    m.x215)**2 >= 0.46785600000000005)
m.e645 = Constraint(expr= (m.x9 - m.x58)**2 + (m.x88 - m.x137)**2 + (m.x167 -
    m.x216)**2 >= 0.46785600000000005)
m.e646 = Constraint(expr= (m.x9 - m.x59)**2 + (m.x88 - m.x138)**2 + (m.x167 -
    m.x217)**2 >= 0.46785600000000005)
m.e647 = Constraint(expr= (m.x9 - m.x60)**2 + (m.x88 - m.x139)**2 + (m.x167 -
    m.x218)**2 >= 0.46785600000000005)
m.e648 = Constraint(expr= (m.x9 - m.x61)**2 + (m.x88 - m.x140)**2 + (m.x167 -
    m.x219)**2 >= 0.46785600000000005)
m.e649 = Constraint(expr= (m.x9 - m.x62)**2 + (m.x88 - m.x141)**2 + (m.x167 -
    m.x220)**2 >= 0.46785600000000005)
m.e650 = Constraint(expr= (m.x9 - m.x63)**2 + (m.x88 - m.x142)**2 + (m.x167 -
    m.x221)**2 >= 0.46785600000000005)
m.e651 = Constraint(expr= (m.x9 - m.x64)**2 + (m.x88 - m.x143)**2 + (m.x167 -
    m.x222)**2 >= 0.46785600000000005)
m.e652 = Constraint(expr= (m.x9 - m.x65)**2 + (m.x88 - m.x144)**2 + (m.x167 -
    m.x223)**2 >= 0.46785600000000005)
m.e653 = Constraint(expr= (m.x9 - m.x66)**2 + (m.x88 - m.x145)**2 + (m.x167 -
    m.x224)**2 >= 0.46785600000000005)
m.e654 = Constraint(expr= (m.x9 - m.x67)**2 + (m.x88 - m.x146)**2 + (m.x167 -
    m.x225)**2 >= 0.46785600000000005)
m.e655 = Constraint(expr= (m.x9 - m.x68)**2 + (m.x88 - m.x147)**2 + (m.x167 -
    m.x226)**2 >= 0.46785600000000005)
m.e656 = Constraint(expr= (m.x9 - m.x69)**2 + (m.x88 - m.x148)**2 + (m.x167 -
    m.x227)**2 >= 0.46785600000000005)
m.e657 = Constraint(expr= (m.x9 - m.x70)**2 + (m.x88 - m.x149)**2 + (m.x167 -
    m.x228)**2 >= 0.46785600000000005)
m.e658 = Constraint(expr= (m.x9 - m.x71)**2 + (m.x88 - m.x150)**2 + (m.x167 -
    m.x229)**2 >= 0.46785600000000005)
m.e659 = Constraint(expr= (m.x9 - m.x72)**2 + (m.x88 - m.x151)**2 + (m.x167 -
    m.x230)**2 >= 0.46785600000000005)
m.e660 = Constraint(expr= (m.x9 - m.x73)**2 + (m.x88 - m.x152)**2 + (m.x167 -
    m.x231)**2 >= 0.46785600000000005)
m.e661 = Constraint(expr= (m.x9 - m.x74)**2 + (m.x88 - m.x153)**2 + (m.x167 -
    m.x232)**2 >= 0.46785600000000005)
m.e662 = Constraint(expr= (m.x9 - m.x75)**2 + (m.x88 - m.x154)**2 + (m.x167 -
    m.x233)**2 >= 0.46785600000000005)
m.e663 = Constraint(expr= (m.x9 - m.x76)**2 + (m.x88 - m.x155)**2 + (m.x167 -
    m.x234)**2 >= 0.46785600000000005)
m.e664 = Constraint(expr= (m.x9 - m.x77)**2 + (m.x88 - m.x156)**2 + (m.x167 -
    m.x235)**2 >= 0.46785600000000005)
m.e665 = Constraint(expr= (m.x9 - m.x78)**2 + (m.x88 - m.x157)**2 + (m.x167 -
    m.x236)**2 >= 0.46785600000000005)
m.e666 = Constraint(expr= (m.x9 - m.x79)**2 + (m.x88 - m.x158)**2 + (m.x167 -
    m.x237)**2 >= 0.46785600000000005)
m.e667 = Constraint(expr= (m.x10 - m.x11)**2 + (m.x89 - m.x90)**2 + (m.x168 -
    m.x169)**2 >= 0.46785600000000005)
m.e668 = Constraint(expr= (m.x10 - m.x12)**2 + (m.x89 - m.x91)**2 + (m.x168 -
    m.x170)**2 >= 0.46785600000000005)
m.e669 = Constraint(expr= (m.x10 - m.x13)**2 + (m.x89 - m.x92)**2 + (m.x168 -
    m.x171)**2 >= 0.46785600000000005)
m.e670 = Constraint(expr= (m.x10 - m.x14)**2 + (m.x89 - m.x93)**2 + (m.x168 -
    m.x172)**2 >= 0.46785600000000005)
m.e671 = Constraint(expr= (m.x10 - m.x15)**2 + (m.x89 - m.x94)**2 + (m.x168 -
    m.x173)**2 >= 0.46785600000000005)
m.e672 = Constraint(expr= (m.x10 - m.x16)**2 + (m.x89 - m.x95)**2 + (m.x168 -
    m.x174)**2 >= 0.46785600000000005)
m.e673 = Constraint(expr= (m.x10 - m.x17)**2 + (m.x89 - m.x96)**2 + (m.x168 -
    m.x175)**2 >= 0.46785600000000005)
m.e674 = Constraint(expr= (m.x10 - m.x18)**2 + (m.x89 - m.x97)**2 + (m.x168 -
    m.x176)**2 >= 0.46785600000000005)
m.e675 = Constraint(expr= (m.x10 - m.x19)**2 + (m.x89 - m.x98)**2 + (m.x168 -
    m.x177)**2 >= 0.46785600000000005)
m.e676 = Constraint(expr= (m.x10 - m.x20)**2 + (m.x89 - m.x99)**2 + (m.x168 -
    m.x178)**2 >= 0.46785600000000005)
m.e677 = Constraint(expr= (m.x10 - m.x21)**2 + (m.x89 - m.x100)**2 + (m.x168 -
    m.x179)**2 >= 0.46785600000000005)
m.e678 = Constraint(expr= (m.x10 - m.x22)**2 + (m.x89 - m.x101)**2 + (m.x168 -
    m.x180)**2 >= 0.46785600000000005)
m.e679 = Constraint(expr= (m.x10 - m.x23)**2 + (m.x89 - m.x102)**2 + (m.x168 -
    m.x181)**2 >= 0.46785600000000005)
m.e680 = Constraint(expr= (m.x10 - m.x24)**2 + (m.x89 - m.x103)**2 + (m.x168 -
    m.x182)**2 >= 0.46785600000000005)
m.e681 = Constraint(expr= (m.x10 - m.x25)**2 + (m.x89 - m.x104)**2 + (m.x168 -
    m.x183)**2 >= 0.46785600000000005)
m.e682 = Constraint(expr= (m.x10 - m.x26)**2 + (m.x89 - m.x105)**2 + (m.x168 -
    m.x184)**2 >= 0.46785600000000005)
m.e683 = Constraint(expr= (m.x10 - m.x27)**2 + (m.x89 - m.x106)**2 + (m.x168 -
    m.x185)**2 >= 0.46785600000000005)
m.e684 = Constraint(expr= (m.x10 - m.x28)**2 + (m.x89 - m.x107)**2 + (m.x168 -
    m.x186)**2 >= 0.46785600000000005)
m.e685 = Constraint(expr= (m.x10 - m.x29)**2 + (m.x89 - m.x108)**2 + (m.x168 -
    m.x187)**2 >= 0.46785600000000005)
m.e686 = Constraint(expr= (m.x10 - m.x30)**2 + (m.x89 - m.x109)**2 + (m.x168 -
    m.x188)**2 >= 0.46785600000000005)
m.e687 = Constraint(expr= (m.x10 - m.x31)**2 + (m.x89 - m.x110)**2 + (m.x168 -
    m.x189)**2 >= 0.46785600000000005)
m.e688 = Constraint(expr= (m.x10 - m.x32)**2 + (m.x89 - m.x111)**2 + (m.x168 -
    m.x190)**2 >= 0.46785600000000005)
m.e689 = Constraint(expr= (m.x10 - m.x33)**2 + (m.x89 - m.x112)**2 + (m.x168 -
    m.x191)**2 >= 0.46785600000000005)
m.e690 = Constraint(expr= (m.x10 - m.x34)**2 + (m.x89 - m.x113)**2 + (m.x168 -
    m.x192)**2 >= 0.46785600000000005)
m.e691 = Constraint(expr= (m.x10 - m.x35)**2 + (m.x89 - m.x114)**2 + (m.x168 -
    m.x193)**2 >= 0.46785600000000005)
m.e692 = Constraint(expr= (m.x10 - m.x36)**2 + (m.x89 - m.x115)**2 + (m.x168 -
    m.x194)**2 >= 0.46785600000000005)
m.e693 = Constraint(expr= (m.x10 - m.x37)**2 + (m.x89 - m.x116)**2 + (m.x168 -
    m.x195)**2 >= 0.46785600000000005)
m.e694 = Constraint(expr= (m.x10 - m.x38)**2 + (m.x89 - m.x117)**2 + (m.x168 -
    m.x196)**2 >= 0.46785600000000005)
m.e695 = Constraint(expr= (m.x10 - m.x39)**2 + (m.x89 - m.x118)**2 + (m.x168 -
    m.x197)**2 >= 0.46785600000000005)
m.e696 = Constraint(expr= (m.x10 - m.x40)**2 + (m.x89 - m.x119)**2 + (m.x168 -
    m.x198)**2 >= 0.46785600000000005)
m.e697 = Constraint(expr= (m.x10 - m.x41)**2 + (m.x89 - m.x120)**2 + (m.x168 -
    m.x199)**2 >= 0.46785600000000005)
m.e698 = Constraint(expr= (m.x10 - m.x42)**2 + (m.x89 - m.x121)**2 + (m.x168 -
    m.x200)**2 >= 0.46785600000000005)
m.e699 = Constraint(expr= (m.x10 - m.x43)**2 + (m.x89 - m.x122)**2 + (m.x168 -
    m.x201)**2 >= 0.46785600000000005)
m.e700 = Constraint(expr= (m.x10 - m.x44)**2 + (m.x89 - m.x123)**2 + (m.x168 -
    m.x202)**2 >= 0.46785600000000005)
m.e701 = Constraint(expr= (m.x10 - m.x45)**2 + (m.x89 - m.x124)**2 + (m.x168 -
    m.x203)**2 >= 0.46785600000000005)
m.e702 = Constraint(expr= (m.x10 - m.x46)**2 + (m.x89 - m.x125)**2 + (m.x168 -
    m.x204)**2 >= 0.46785600000000005)
m.e703 = Constraint(expr= (m.x10 - m.x47)**2 + (m.x89 - m.x126)**2 + (m.x168 -
    m.x205)**2 >= 0.46785600000000005)
m.e704 = Constraint(expr= (m.x10 - m.x48)**2 + (m.x89 - m.x127)**2 + (m.x168 -
    m.x206)**2 >= 0.46785600000000005)
m.e705 = Constraint(expr= (m.x10 - m.x49)**2 + (m.x89 - m.x128)**2 + (m.x168 -
    m.x207)**2 >= 0.46785600000000005)
m.e706 = Constraint(expr= (m.x10 - m.x50)**2 + (m.x89 - m.x129)**2 + (m.x168 -
    m.x208)**2 >= 0.46785600000000005)
m.e707 = Constraint(expr= (m.x10 - m.x51)**2 + (m.x89 - m.x130)**2 + (m.x168 -
    m.x209)**2 >= 0.46785600000000005)
m.e708 = Constraint(expr= (m.x10 - m.x52)**2 + (m.x89 - m.x131)**2 + (m.x168 -
    m.x210)**2 >= 0.46785600000000005)
m.e709 = Constraint(expr= (m.x10 - m.x53)**2 + (m.x89 - m.x132)**2 + (m.x168 -
    m.x211)**2 >= 0.46785600000000005)
m.e710 = Constraint(expr= (m.x10 - m.x54)**2 + (m.x89 - m.x133)**2 + (m.x168 -
    m.x212)**2 >= 0.46785600000000005)
m.e711 = Constraint(expr= (m.x10 - m.x55)**2 + (m.x89 - m.x134)**2 + (m.x168 -
    m.x213)**2 >= 0.46785600000000005)
m.e712 = Constraint(expr= (m.x10 - m.x56)**2 + (m.x89 - m.x135)**2 + (m.x168 -
    m.x214)**2 >= 0.46785600000000005)
m.e713 = Constraint(expr= (m.x10 - m.x57)**2 + (m.x89 - m.x136)**2 + (m.x168 -
    m.x215)**2 >= 0.46785600000000005)
m.e714 = Constraint(expr= (m.x10 - m.x58)**2 + (m.x89 - m.x137)**2 + (m.x168 -
    m.x216)**2 >= 0.46785600000000005)
m.e715 = Constraint(expr= (m.x10 - m.x59)**2 + (m.x89 - m.x138)**2 + (m.x168 -
    m.x217)**2 >= 0.46785600000000005)
m.e716 = Constraint(expr= (m.x10 - m.x60)**2 + (m.x89 - m.x139)**2 + (m.x168 -
    m.x218)**2 >= 0.46785600000000005)
m.e717 = Constraint(expr= (m.x10 - m.x61)**2 + (m.x89 - m.x140)**2 + (m.x168 -
    m.x219)**2 >= 0.46785600000000005)
m.e718 = Constraint(expr= (m.x10 - m.x62)**2 + (m.x89 - m.x141)**2 + (m.x168 -
    m.x220)**2 >= 0.46785600000000005)
m.e719 = Constraint(expr= (m.x10 - m.x63)**2 + (m.x89 - m.x142)**2 + (m.x168 -
    m.x221)**2 >= 0.46785600000000005)
m.e720 = Constraint(expr= (m.x10 - m.x64)**2 + (m.x89 - m.x143)**2 + (m.x168 -
    m.x222)**2 >= 0.46785600000000005)
m.e721 = Constraint(expr= (m.x10 - m.x65)**2 + (m.x89 - m.x144)**2 + (m.x168 -
    m.x223)**2 >= 0.46785600000000005)
m.e722 = Constraint(expr= (m.x10 - m.x66)**2 + (m.x89 - m.x145)**2 + (m.x168 -
    m.x224)**2 >= 0.46785600000000005)
m.e723 = Constraint(expr= (m.x10 - m.x67)**2 + (m.x89 - m.x146)**2 + (m.x168 -
    m.x225)**2 >= 0.46785600000000005)
m.e724 = Constraint(expr= (m.x10 - m.x68)**2 + (m.x89 - m.x147)**2 + (m.x168 -
    m.x226)**2 >= 0.46785600000000005)
m.e725 = Constraint(expr= (m.x10 - m.x69)**2 + (m.x89 - m.x148)**2 + (m.x168 -
    m.x227)**2 >= 0.46785600000000005)
m.e726 = Constraint(expr= (m.x10 - m.x70)**2 + (m.x89 - m.x149)**2 + (m.x168 -
    m.x228)**2 >= 0.46785600000000005)
m.e727 = Constraint(expr= (m.x10 - m.x71)**2 + (m.x89 - m.x150)**2 + (m.x168 -
    m.x229)**2 >= 0.46785600000000005)
m.e728 = Constraint(expr= (m.x10 - m.x72)**2 + (m.x89 - m.x151)**2 + (m.x168 -
    m.x230)**2 >= 0.46785600000000005)
m.e729 = Constraint(expr= (m.x10 - m.x73)**2 + (m.x89 - m.x152)**2 + (m.x168 -
    m.x231)**2 >= 0.46785600000000005)
m.e730 = Constraint(expr= (m.x10 - m.x74)**2 + (m.x89 - m.x153)**2 + (m.x168 -
    m.x232)**2 >= 0.46785600000000005)
m.e731 = Constraint(expr= (m.x10 - m.x75)**2 + (m.x89 - m.x154)**2 + (m.x168 -
    m.x233)**2 >= 0.46785600000000005)
m.e732 = Constraint(expr= (m.x10 - m.x76)**2 + (m.x89 - m.x155)**2 + (m.x168 -
    m.x234)**2 >= 0.46785600000000005)
m.e733 = Constraint(expr= (m.x10 - m.x77)**2 + (m.x89 - m.x156)**2 + (m.x168 -
    m.x235)**2 >= 0.46785600000000005)
m.e734 = Constraint(expr= (m.x10 - m.x78)**2 + (m.x89 - m.x157)**2 + (m.x168 -
    m.x236)**2 >= 0.46785600000000005)
m.e735 = Constraint(expr= (m.x10 - m.x79)**2 + (m.x89 - m.x158)**2 + (m.x168 -
    m.x237)**2 >= 0.46785600000000005)
m.e736 = Constraint(expr= (m.x11 - m.x12)**2 + (m.x90 - m.x91)**2 + (m.x169 -
    m.x170)**2 >= 0.46785600000000005)
m.e737 = Constraint(expr= (m.x11 - m.x13)**2 + (m.x90 - m.x92)**2 + (m.x169 -
    m.x171)**2 >= 0.46785600000000005)
m.e738 = Constraint(expr= (m.x11 - m.x14)**2 + (m.x90 - m.x93)**2 + (m.x169 -
    m.x172)**2 >= 0.46785600000000005)
m.e739 = Constraint(expr= (m.x11 - m.x15)**2 + (m.x90 - m.x94)**2 + (m.x169 -
    m.x173)**2 >= 0.46785600000000005)
m.e740 = Constraint(expr= (m.x11 - m.x16)**2 + (m.x90 - m.x95)**2 + (m.x169 -
    m.x174)**2 >= 0.46785600000000005)
m.e741 = Constraint(expr= (m.x11 - m.x17)**2 + (m.x90 - m.x96)**2 + (m.x169 -
    m.x175)**2 >= 0.46785600000000005)
m.e742 = Constraint(expr= (m.x11 - m.x18)**2 + (m.x90 - m.x97)**2 + (m.x169 -
    m.x176)**2 >= 0.46785600000000005)
m.e743 = Constraint(expr= (m.x11 - m.x19)**2 + (m.x90 - m.x98)**2 + (m.x169 -
    m.x177)**2 >= 0.46785600000000005)
m.e744 = Constraint(expr= (m.x11 - m.x20)**2 + (m.x90 - m.x99)**2 + (m.x169 -
    m.x178)**2 >= 0.46785600000000005)
m.e745 = Constraint(expr= (m.x11 - m.x21)**2 + (m.x90 - m.x100)**2 + (m.x169 -
    m.x179)**2 >= 0.46785600000000005)
m.e746 = Constraint(expr= (m.x11 - m.x22)**2 + (m.x90 - m.x101)**2 + (m.x169 -
    m.x180)**2 >= 0.46785600000000005)
m.e747 = Constraint(expr= (m.x11 - m.x23)**2 + (m.x90 - m.x102)**2 + (m.x169 -
    m.x181)**2 >= 0.46785600000000005)
m.e748 = Constraint(expr= (m.x11 - m.x24)**2 + (m.x90 - m.x103)**2 + (m.x169 -
    m.x182)**2 >= 0.46785600000000005)
m.e749 = Constraint(expr= (m.x11 - m.x25)**2 + (m.x90 - m.x104)**2 + (m.x169 -
    m.x183)**2 >= 0.46785600000000005)
m.e750 = Constraint(expr= (m.x11 - m.x26)**2 + (m.x90 - m.x105)**2 + (m.x169 -
    m.x184)**2 >= 0.46785600000000005)
m.e751 = Constraint(expr= (m.x11 - m.x27)**2 + (m.x90 - m.x106)**2 + (m.x169 -
    m.x185)**2 >= 0.46785600000000005)
m.e752 = Constraint(expr= (m.x11 - m.x28)**2 + (m.x90 - m.x107)**2 + (m.x169 -
    m.x186)**2 >= 0.46785600000000005)
m.e753 = Constraint(expr= (m.x11 - m.x29)**2 + (m.x90 - m.x108)**2 + (m.x169 -
    m.x187)**2 >= 0.46785600000000005)
m.e754 = Constraint(expr= (m.x11 - m.x30)**2 + (m.x90 - m.x109)**2 + (m.x169 -
    m.x188)**2 >= 0.46785600000000005)
m.e755 = Constraint(expr= (m.x11 - m.x31)**2 + (m.x90 - m.x110)**2 + (m.x169 -
    m.x189)**2 >= 0.46785600000000005)
m.e756 = Constraint(expr= (m.x11 - m.x32)**2 + (m.x90 - m.x111)**2 + (m.x169 -
    m.x190)**2 >= 0.46785600000000005)
m.e757 = Constraint(expr= (m.x11 - m.x33)**2 + (m.x90 - m.x112)**2 + (m.x169 -
    m.x191)**2 >= 0.46785600000000005)
m.e758 = Constraint(expr= (m.x11 - m.x34)**2 + (m.x90 - m.x113)**2 + (m.x169 -
    m.x192)**2 >= 0.46785600000000005)
m.e759 = Constraint(expr= (m.x11 - m.x35)**2 + (m.x90 - m.x114)**2 + (m.x169 -
    m.x193)**2 >= 0.46785600000000005)
m.e760 = Constraint(expr= (m.x11 - m.x36)**2 + (m.x90 - m.x115)**2 + (m.x169 -
    m.x194)**2 >= 0.46785600000000005)
m.e761 = Constraint(expr= (m.x11 - m.x37)**2 + (m.x90 - m.x116)**2 + (m.x169 -
    m.x195)**2 >= 0.46785600000000005)
m.e762 = Constraint(expr= (m.x11 - m.x38)**2 + (m.x90 - m.x117)**2 + (m.x169 -
    m.x196)**2 >= 0.46785600000000005)
m.e763 = Constraint(expr= (m.x11 - m.x39)**2 + (m.x90 - m.x118)**2 + (m.x169 -
    m.x197)**2 >= 0.46785600000000005)
m.e764 = Constraint(expr= (m.x11 - m.x40)**2 + (m.x90 - m.x119)**2 + (m.x169 -
    m.x198)**2 >= 0.46785600000000005)
m.e765 = Constraint(expr= (m.x11 - m.x41)**2 + (m.x90 - m.x120)**2 + (m.x169 -
    m.x199)**2 >= 0.46785600000000005)
m.e766 = Constraint(expr= (m.x11 - m.x42)**2 + (m.x90 - m.x121)**2 + (m.x169 -
    m.x200)**2 >= 0.46785600000000005)
m.e767 = Constraint(expr= (m.x11 - m.x43)**2 + (m.x90 - m.x122)**2 + (m.x169 -
    m.x201)**2 >= 0.46785600000000005)
m.e768 = Constraint(expr= (m.x11 - m.x44)**2 + (m.x90 - m.x123)**2 + (m.x169 -
    m.x202)**2 >= 0.46785600000000005)
m.e769 = Constraint(expr= (m.x11 - m.x45)**2 + (m.x90 - m.x124)**2 + (m.x169 -
    m.x203)**2 >= 0.46785600000000005)
m.e770 = Constraint(expr= (m.x11 - m.x46)**2 + (m.x90 - m.x125)**2 + (m.x169 -
    m.x204)**2 >= 0.46785600000000005)
m.e771 = Constraint(expr= (m.x11 - m.x47)**2 + (m.x90 - m.x126)**2 + (m.x169 -
    m.x205)**2 >= 0.46785600000000005)
m.e772 = Constraint(expr= (m.x11 - m.x48)**2 + (m.x90 - m.x127)**2 + (m.x169 -
    m.x206)**2 >= 0.46785600000000005)
m.e773 = Constraint(expr= (m.x11 - m.x49)**2 + (m.x90 - m.x128)**2 + (m.x169 -
    m.x207)**2 >= 0.46785600000000005)
m.e774 = Constraint(expr= (m.x11 - m.x50)**2 + (m.x90 - m.x129)**2 + (m.x169 -
    m.x208)**2 >= 0.46785600000000005)
m.e775 = Constraint(expr= (m.x11 - m.x51)**2 + (m.x90 - m.x130)**2 + (m.x169 -
    m.x209)**2 >= 0.46785600000000005)
m.e776 = Constraint(expr= (m.x11 - m.x52)**2 + (m.x90 - m.x131)**2 + (m.x169 -
    m.x210)**2 >= 0.46785600000000005)
m.e777 = Constraint(expr= (m.x11 - m.x53)**2 + (m.x90 - m.x132)**2 + (m.x169 -
    m.x211)**2 >= 0.46785600000000005)
m.e778 = Constraint(expr= (m.x11 - m.x54)**2 + (m.x90 - m.x133)**2 + (m.x169 -
    m.x212)**2 >= 0.46785600000000005)
m.e779 = Constraint(expr= (m.x11 - m.x55)**2 + (m.x90 - m.x134)**2 + (m.x169 -
    m.x213)**2 >= 0.46785600000000005)
m.e780 = Constraint(expr= (m.x11 - m.x56)**2 + (m.x90 - m.x135)**2 + (m.x169 -
    m.x214)**2 >= 0.46785600000000005)
m.e781 = Constraint(expr= (m.x11 - m.x57)**2 + (m.x90 - m.x136)**2 + (m.x169 -
    m.x215)**2 >= 0.46785600000000005)
m.e782 = Constraint(expr= (m.x11 - m.x58)**2 + (m.x90 - m.x137)**2 + (m.x169 -
    m.x216)**2 >= 0.46785600000000005)
m.e783 = Constraint(expr= (m.x11 - m.x59)**2 + (m.x90 - m.x138)**2 + (m.x169 -
    m.x217)**2 >= 0.46785600000000005)
m.e784 = Constraint(expr= (m.x11 - m.x60)**2 + (m.x90 - m.x139)**2 + (m.x169 -
    m.x218)**2 >= 0.46785600000000005)
m.e785 = Constraint(expr= (m.x11 - m.x61)**2 + (m.x90 - m.x140)**2 + (m.x169 -
    m.x219)**2 >= 0.46785600000000005)
m.e786 = Constraint(expr= (m.x11 - m.x62)**2 + (m.x90 - m.x141)**2 + (m.x169 -
    m.x220)**2 >= 0.46785600000000005)
m.e787 = Constraint(expr= (m.x11 - m.x63)**2 + (m.x90 - m.x142)**2 + (m.x169 -
    m.x221)**2 >= 0.46785600000000005)
m.e788 = Constraint(expr= (m.x11 - m.x64)**2 + (m.x90 - m.x143)**2 + (m.x169 -
    m.x222)**2 >= 0.46785600000000005)
m.e789 = Constraint(expr= (m.x11 - m.x65)**2 + (m.x90 - m.x144)**2 + (m.x169 -
    m.x223)**2 >= 0.46785600000000005)
m.e790 = Constraint(expr= (m.x11 - m.x66)**2 + (m.x90 - m.x145)**2 + (m.x169 -
    m.x224)**2 >= 0.46785600000000005)
m.e791 = Constraint(expr= (m.x11 - m.x67)**2 + (m.x90 - m.x146)**2 + (m.x169 -
    m.x225)**2 >= 0.46785600000000005)
m.e792 = Constraint(expr= (m.x11 - m.x68)**2 + (m.x90 - m.x147)**2 + (m.x169 -
    m.x226)**2 >= 0.46785600000000005)
m.e793 = Constraint(expr= (m.x11 - m.x69)**2 + (m.x90 - m.x148)**2 + (m.x169 -
    m.x227)**2 >= 0.46785600000000005)
m.e794 = Constraint(expr= (m.x11 - m.x70)**2 + (m.x90 - m.x149)**2 + (m.x169 -
    m.x228)**2 >= 0.46785600000000005)
m.e795 = Constraint(expr= (m.x11 - m.x71)**2 + (m.x90 - m.x150)**2 + (m.x169 -
    m.x229)**2 >= 0.46785600000000005)
m.e796 = Constraint(expr= (m.x11 - m.x72)**2 + (m.x90 - m.x151)**2 + (m.x169 -
    m.x230)**2 >= 0.46785600000000005)
m.e797 = Constraint(expr= (m.x11 - m.x73)**2 + (m.x90 - m.x152)**2 + (m.x169 -
    m.x231)**2 >= 0.46785600000000005)
m.e798 = Constraint(expr= (m.x11 - m.x74)**2 + (m.x90 - m.x153)**2 + (m.x169 -
    m.x232)**2 >= 0.46785600000000005)
m.e799 = Constraint(expr= (m.x11 - m.x75)**2 + (m.x90 - m.x154)**2 + (m.x169 -
    m.x233)**2 >= 0.46785600000000005)
m.e800 = Constraint(expr= (m.x11 - m.x76)**2 + (m.x90 - m.x155)**2 + (m.x169 -
    m.x234)**2 >= 0.46785600000000005)
m.e801 = Constraint(expr= (m.x11 - m.x77)**2 + (m.x90 - m.x156)**2 + (m.x169 -
    m.x235)**2 >= 0.46785600000000005)
m.e802 = Constraint(expr= (m.x11 - m.x78)**2 + (m.x90 - m.x157)**2 + (m.x169 -
    m.x236)**2 >= 0.46785600000000005)
m.e803 = Constraint(expr= (m.x11 - m.x79)**2 + (m.x90 - m.x158)**2 + (m.x169 -
    m.x237)**2 >= 0.46785600000000005)
m.e804 = Constraint(expr= (m.x12 - m.x13)**2 + (m.x91 - m.x92)**2 + (m.x170 -
    m.x171)**2 >= 0.46785600000000005)
m.e805 = Constraint(expr= (m.x12 - m.x14)**2 + (m.x91 - m.x93)**2 + (m.x170 -
    m.x172)**2 >= 0.46785600000000005)
m.e806 = Constraint(expr= (m.x12 - m.x15)**2 + (m.x91 - m.x94)**2 + (m.x170 -
    m.x173)**2 >= 0.46785600000000005)
m.e807 = Constraint(expr= (m.x12 - m.x16)**2 + (m.x91 - m.x95)**2 + (m.x170 -
    m.x174)**2 >= 0.46785600000000005)
m.e808 = Constraint(expr= (m.x12 - m.x17)**2 + (m.x91 - m.x96)**2 + (m.x170 -
    m.x175)**2 >= 0.46785600000000005)
m.e809 = Constraint(expr= (m.x12 - m.x18)**2 + (m.x91 - m.x97)**2 + (m.x170 -
    m.x176)**2 >= 0.46785600000000005)
m.e810 = Constraint(expr= (m.x12 - m.x19)**2 + (m.x91 - m.x98)**2 + (m.x170 -
    m.x177)**2 >= 0.46785600000000005)
m.e811 = Constraint(expr= (m.x12 - m.x20)**2 + (m.x91 - m.x99)**2 + (m.x170 -
    m.x178)**2 >= 0.46785600000000005)
m.e812 = Constraint(expr= (m.x12 - m.x21)**2 + (m.x91 - m.x100)**2 + (m.x170 -
    m.x179)**2 >= 0.46785600000000005)
m.e813 = Constraint(expr= (m.x12 - m.x22)**2 + (m.x91 - m.x101)**2 + (m.x170 -
    m.x180)**2 >= 0.46785600000000005)
m.e814 = Constraint(expr= (m.x12 - m.x23)**2 + (m.x91 - m.x102)**2 + (m.x170 -
    m.x181)**2 >= 0.46785600000000005)
m.e815 = Constraint(expr= (m.x12 - m.x24)**2 + (m.x91 - m.x103)**2 + (m.x170 -
    m.x182)**2 >= 0.46785600000000005)
m.e816 = Constraint(expr= (m.x12 - m.x25)**2 + (m.x91 - m.x104)**2 + (m.x170 -
    m.x183)**2 >= 0.46785600000000005)
m.e817 = Constraint(expr= (m.x12 - m.x26)**2 + (m.x91 - m.x105)**2 + (m.x170 -
    m.x184)**2 >= 0.46785600000000005)
m.e818 = Constraint(expr= (m.x12 - m.x27)**2 + (m.x91 - m.x106)**2 + (m.x170 -
    m.x185)**2 >= 0.46785600000000005)
m.e819 = Constraint(expr= (m.x12 - m.x28)**2 + (m.x91 - m.x107)**2 + (m.x170 -
    m.x186)**2 >= 0.46785600000000005)
m.e820 = Constraint(expr= (m.x12 - m.x29)**2 + (m.x91 - m.x108)**2 + (m.x170 -
    m.x187)**2 >= 0.46785600000000005)
m.e821 = Constraint(expr= (m.x12 - m.x30)**2 + (m.x91 - m.x109)**2 + (m.x170 -
    m.x188)**2 >= 0.46785600000000005)
m.e822 = Constraint(expr= (m.x12 - m.x31)**2 + (m.x91 - m.x110)**2 + (m.x170 -
    m.x189)**2 >= 0.46785600000000005)
m.e823 = Constraint(expr= (m.x12 - m.x32)**2 + (m.x91 - m.x111)**2 + (m.x170 -
    m.x190)**2 >= 0.46785600000000005)
m.e824 = Constraint(expr= (m.x12 - m.x33)**2 + (m.x91 - m.x112)**2 + (m.x170 -
    m.x191)**2 >= 0.46785600000000005)
m.e825 = Constraint(expr= (m.x12 - m.x34)**2 + (m.x91 - m.x113)**2 + (m.x170 -
    m.x192)**2 >= 0.46785600000000005)
m.e826 = Constraint(expr= (m.x12 - m.x35)**2 + (m.x91 - m.x114)**2 + (m.x170 -
    m.x193)**2 >= 0.46785600000000005)
m.e827 = Constraint(expr= (m.x12 - m.x36)**2 + (m.x91 - m.x115)**2 + (m.x170 -
    m.x194)**2 >= 0.46785600000000005)
m.e828 = Constraint(expr= (m.x12 - m.x37)**2 + (m.x91 - m.x116)**2 + (m.x170 -
    m.x195)**2 >= 0.46785600000000005)
m.e829 = Constraint(expr= (m.x12 - m.x38)**2 + (m.x91 - m.x117)**2 + (m.x170 -
    m.x196)**2 >= 0.46785600000000005)
m.e830 = Constraint(expr= (m.x12 - m.x39)**2 + (m.x91 - m.x118)**2 + (m.x170 -
    m.x197)**2 >= 0.46785600000000005)
m.e831 = Constraint(expr= (m.x12 - m.x40)**2 + (m.x91 - m.x119)**2 + (m.x170 -
    m.x198)**2 >= 0.46785600000000005)
m.e832 = Constraint(expr= (m.x12 - m.x41)**2 + (m.x91 - m.x120)**2 + (m.x170 -
    m.x199)**2 >= 0.46785600000000005)
m.e833 = Constraint(expr= (m.x12 - m.x42)**2 + (m.x91 - m.x121)**2 + (m.x170 -
    m.x200)**2 >= 0.46785600000000005)
m.e834 = Constraint(expr= (m.x12 - m.x43)**2 + (m.x91 - m.x122)**2 + (m.x170 -
    m.x201)**2 >= 0.46785600000000005)
m.e835 = Constraint(expr= (m.x12 - m.x44)**2 + (m.x91 - m.x123)**2 + (m.x170 -
    m.x202)**2 >= 0.46785600000000005)
m.e836 = Constraint(expr= (m.x12 - m.x45)**2 + (m.x91 - m.x124)**2 + (m.x170 -
    m.x203)**2 >= 0.46785600000000005)
m.e837 = Constraint(expr= (m.x12 - m.x46)**2 + (m.x91 - m.x125)**2 + (m.x170 -
    m.x204)**2 >= 0.46785600000000005)
m.e838 = Constraint(expr= (m.x12 - m.x47)**2 + (m.x91 - m.x126)**2 + (m.x170 -
    m.x205)**2 >= 0.46785600000000005)
m.e839 = Constraint(expr= (m.x12 - m.x48)**2 + (m.x91 - m.x127)**2 + (m.x170 -
    m.x206)**2 >= 0.46785600000000005)
m.e840 = Constraint(expr= (m.x12 - m.x49)**2 + (m.x91 - m.x128)**2 + (m.x170 -
    m.x207)**2 >= 0.46785600000000005)
m.e841 = Constraint(expr= (m.x12 - m.x50)**2 + (m.x91 - m.x129)**2 + (m.x170 -
    m.x208)**2 >= 0.46785600000000005)
m.e842 = Constraint(expr= (m.x12 - m.x51)**2 + (m.x91 - m.x130)**2 + (m.x170 -
    m.x209)**2 >= 0.46785600000000005)
m.e843 = Constraint(expr= (m.x12 - m.x52)**2 + (m.x91 - m.x131)**2 + (m.x170 -
    m.x210)**2 >= 0.46785600000000005)
m.e844 = Constraint(expr= (m.x12 - m.x53)**2 + (m.x91 - m.x132)**2 + (m.x170 -
    m.x211)**2 >= 0.46785600000000005)
m.e845 = Constraint(expr= (m.x12 - m.x54)**2 + (m.x91 - m.x133)**2 + (m.x170 -
    m.x212)**2 >= 0.46785600000000005)
m.e846 = Constraint(expr= (m.x12 - m.x55)**2 + (m.x91 - m.x134)**2 + (m.x170 -
    m.x213)**2 >= 0.46785600000000005)
m.e847 = Constraint(expr= (m.x12 - m.x56)**2 + (m.x91 - m.x135)**2 + (m.x170 -
    m.x214)**2 >= 0.46785600000000005)
m.e848 = Constraint(expr= (m.x12 - m.x57)**2 + (m.x91 - m.x136)**2 + (m.x170 -
    m.x215)**2 >= 0.46785600000000005)
m.e849 = Constraint(expr= (m.x12 - m.x58)**2 + (m.x91 - m.x137)**2 + (m.x170 -
    m.x216)**2 >= 0.46785600000000005)
m.e850 = Constraint(expr= (m.x12 - m.x59)**2 + (m.x91 - m.x138)**2 + (m.x170 -
    m.x217)**2 >= 0.46785600000000005)
m.e851 = Constraint(expr= (m.x12 - m.x60)**2 + (m.x91 - m.x139)**2 + (m.x170 -
    m.x218)**2 >= 0.46785600000000005)
m.e852 = Constraint(expr= (m.x12 - m.x61)**2 + (m.x91 - m.x140)**2 + (m.x170 -
    m.x219)**2 >= 0.46785600000000005)
m.e853 = Constraint(expr= (m.x12 - m.x62)**2 + (m.x91 - m.x141)**2 + (m.x170 -
    m.x220)**2 >= 0.46785600000000005)
m.e854 = Constraint(expr= (m.x12 - m.x63)**2 + (m.x91 - m.x142)**2 + (m.x170 -
    m.x221)**2 >= 0.46785600000000005)
m.e855 = Constraint(expr= (m.x12 - m.x64)**2 + (m.x91 - m.x143)**2 + (m.x170 -
    m.x222)**2 >= 0.46785600000000005)
m.e856 = Constraint(expr= (m.x12 - m.x65)**2 + (m.x91 - m.x144)**2 + (m.x170 -
    m.x223)**2 >= 0.46785600000000005)
m.e857 = Constraint(expr= (m.x12 - m.x66)**2 + (m.x91 - m.x145)**2 + (m.x170 -
    m.x224)**2 >= 0.46785600000000005)
m.e858 = Constraint(expr= (m.x12 - m.x67)**2 + (m.x91 - m.x146)**2 + (m.x170 -
    m.x225)**2 >= 0.46785600000000005)
m.e859 = Constraint(expr= (m.x12 - m.x68)**2 + (m.x91 - m.x147)**2 + (m.x170 -
    m.x226)**2 >= 0.46785600000000005)
m.e860 = Constraint(expr= (m.x12 - m.x69)**2 + (m.x91 - m.x148)**2 + (m.x170 -
    m.x227)**2 >= 0.46785600000000005)
m.e861 = Constraint(expr= (m.x12 - m.x70)**2 + (m.x91 - m.x149)**2 + (m.x170 -
    m.x228)**2 >= 0.46785600000000005)
m.e862 = Constraint(expr= (m.x12 - m.x71)**2 + (m.x91 - m.x150)**2 + (m.x170 -
    m.x229)**2 >= 0.46785600000000005)
m.e863 = Constraint(expr= (m.x12 - m.x72)**2 + (m.x91 - m.x151)**2 + (m.x170 -
    m.x230)**2 >= 0.46785600000000005)
m.e864 = Constraint(expr= (m.x12 - m.x73)**2 + (m.x91 - m.x152)**2 + (m.x170 -
    m.x231)**2 >= 0.46785600000000005)
m.e865 = Constraint(expr= (m.x12 - m.x74)**2 + (m.x91 - m.x153)**2 + (m.x170 -
    m.x232)**2 >= 0.46785600000000005)
m.e866 = Constraint(expr= (m.x12 - m.x75)**2 + (m.x91 - m.x154)**2 + (m.x170 -
    m.x233)**2 >= 0.46785600000000005)
m.e867 = Constraint(expr= (m.x12 - m.x76)**2 + (m.x91 - m.x155)**2 + (m.x170 -
    m.x234)**2 >= 0.46785600000000005)
m.e868 = Constraint(expr= (m.x12 - m.x77)**2 + (m.x91 - m.x156)**2 + (m.x170 -
    m.x235)**2 >= 0.46785600000000005)
m.e869 = Constraint(expr= (m.x12 - m.x78)**2 + (m.x91 - m.x157)**2 + (m.x170 -
    m.x236)**2 >= 0.46785600000000005)
m.e870 = Constraint(expr= (m.x12 - m.x79)**2 + (m.x91 - m.x158)**2 + (m.x170 -
    m.x237)**2 >= 0.46785600000000005)
m.e871 = Constraint(expr= (m.x13 - m.x14)**2 + (m.x92 - m.x93)**2 + (m.x171 -
    m.x172)**2 >= 0.46785600000000005)
m.e872 = Constraint(expr= (m.x13 - m.x15)**2 + (m.x92 - m.x94)**2 + (m.x171 -
    m.x173)**2 >= 0.46785600000000005)
m.e873 = Constraint(expr= (m.x13 - m.x16)**2 + (m.x92 - m.x95)**2 + (m.x171 -
    m.x174)**2 >= 0.46785600000000005)
m.e874 = Constraint(expr= (m.x13 - m.x17)**2 + (m.x92 - m.x96)**2 + (m.x171 -
    m.x175)**2 >= 0.46785600000000005)
m.e875 = Constraint(expr= (m.x13 - m.x18)**2 + (m.x92 - m.x97)**2 + (m.x171 -
    m.x176)**2 >= 0.46785600000000005)
m.e876 = Constraint(expr= (m.x13 - m.x19)**2 + (m.x92 - m.x98)**2 + (m.x171 -
    m.x177)**2 >= 0.46785600000000005)
m.e877 = Constraint(expr= (m.x13 - m.x20)**2 + (m.x92 - m.x99)**2 + (m.x171 -
    m.x178)**2 >= 0.46785600000000005)
m.e878 = Constraint(expr= (m.x13 - m.x21)**2 + (m.x92 - m.x100)**2 + (m.x171 -
    m.x179)**2 >= 0.46785600000000005)
m.e879 = Constraint(expr= (m.x13 - m.x22)**2 + (m.x92 - m.x101)**2 + (m.x171 -
    m.x180)**2 >= 0.46785600000000005)
m.e880 = Constraint(expr= (m.x13 - m.x23)**2 + (m.x92 - m.x102)**2 + (m.x171 -
    m.x181)**2 >= 0.46785600000000005)
m.e881 = Constraint(expr= (m.x13 - m.x24)**2 + (m.x92 - m.x103)**2 + (m.x171 -
    m.x182)**2 >= 0.46785600000000005)
m.e882 = Constraint(expr= (m.x13 - m.x25)**2 + (m.x92 - m.x104)**2 + (m.x171 -
    m.x183)**2 >= 0.46785600000000005)
m.e883 = Constraint(expr= (m.x13 - m.x26)**2 + (m.x92 - m.x105)**2 + (m.x171 -
    m.x184)**2 >= 0.46785600000000005)
m.e884 = Constraint(expr= (m.x13 - m.x27)**2 + (m.x92 - m.x106)**2 + (m.x171 -
    m.x185)**2 >= 0.46785600000000005)
m.e885 = Constraint(expr= (m.x13 - m.x28)**2 + (m.x92 - m.x107)**2 + (m.x171 -
    m.x186)**2 >= 0.46785600000000005)
m.e886 = Constraint(expr= (m.x13 - m.x29)**2 + (m.x92 - m.x108)**2 + (m.x171 -
    m.x187)**2 >= 0.46785600000000005)
m.e887 = Constraint(expr= (m.x13 - m.x30)**2 + (m.x92 - m.x109)**2 + (m.x171 -
    m.x188)**2 >= 0.46785600000000005)
m.e888 = Constraint(expr= (m.x13 - m.x31)**2 + (m.x92 - m.x110)**2 + (m.x171 -
    m.x189)**2 >= 0.46785600000000005)
m.e889 = Constraint(expr= (m.x13 - m.x32)**2 + (m.x92 - m.x111)**2 + (m.x171 -
    m.x190)**2 >= 0.46785600000000005)
m.e890 = Constraint(expr= (m.x13 - m.x33)**2 + (m.x92 - m.x112)**2 + (m.x171 -
    m.x191)**2 >= 0.46785600000000005)
m.e891 = Constraint(expr= (m.x13 - m.x34)**2 + (m.x92 - m.x113)**2 + (m.x171 -
    m.x192)**2 >= 0.46785600000000005)
m.e892 = Constraint(expr= (m.x13 - m.x35)**2 + (m.x92 - m.x114)**2 + (m.x171 -
    m.x193)**2 >= 0.46785600000000005)
m.e893 = Constraint(expr= (m.x13 - m.x36)**2 + (m.x92 - m.x115)**2 + (m.x171 -
    m.x194)**2 >= 0.46785600000000005)
m.e894 = Constraint(expr= (m.x13 - m.x37)**2 + (m.x92 - m.x116)**2 + (m.x171 -
    m.x195)**2 >= 0.46785600000000005)
m.e895 = Constraint(expr= (m.x13 - m.x38)**2 + (m.x92 - m.x117)**2 + (m.x171 -
    m.x196)**2 >= 0.46785600000000005)
m.e896 = Constraint(expr= (m.x13 - m.x39)**2 + (m.x92 - m.x118)**2 + (m.x171 -
    m.x197)**2 >= 0.46785600000000005)
m.e897 = Constraint(expr= (m.x13 - m.x40)**2 + (m.x92 - m.x119)**2 + (m.x171 -
    m.x198)**2 >= 0.46785600000000005)
m.e898 = Constraint(expr= (m.x13 - m.x41)**2 + (m.x92 - m.x120)**2 + (m.x171 -
    m.x199)**2 >= 0.46785600000000005)
m.e899 = Constraint(expr= (m.x13 - m.x42)**2 + (m.x92 - m.x121)**2 + (m.x171 -
    m.x200)**2 >= 0.46785600000000005)
m.e900 = Constraint(expr= (m.x13 - m.x43)**2 + (m.x92 - m.x122)**2 + (m.x171 -
    m.x201)**2 >= 0.46785600000000005)
m.e901 = Constraint(expr= (m.x13 - m.x44)**2 + (m.x92 - m.x123)**2 + (m.x171 -
    m.x202)**2 >= 0.46785600000000005)
m.e902 = Constraint(expr= (m.x13 - m.x45)**2 + (m.x92 - m.x124)**2 + (m.x171 -
    m.x203)**2 >= 0.46785600000000005)
m.e903 = Constraint(expr= (m.x13 - m.x46)**2 + (m.x92 - m.x125)**2 + (m.x171 -
    m.x204)**2 >= 0.46785600000000005)
m.e904 = Constraint(expr= (m.x13 - m.x47)**2 + (m.x92 - m.x126)**2 + (m.x171 -
    m.x205)**2 >= 0.46785600000000005)
m.e905 = Constraint(expr= (m.x13 - m.x48)**2 + (m.x92 - m.x127)**2 + (m.x171 -
    m.x206)**2 >= 0.46785600000000005)
m.e906 = Constraint(expr= (m.x13 - m.x49)**2 + (m.x92 - m.x128)**2 + (m.x171 -
    m.x207)**2 >= 0.46785600000000005)
m.e907 = Constraint(expr= (m.x13 - m.x50)**2 + (m.x92 - m.x129)**2 + (m.x171 -
    m.x208)**2 >= 0.46785600000000005)
m.e908 = Constraint(expr= (m.x13 - m.x51)**2 + (m.x92 - m.x130)**2 + (m.x171 -
    m.x209)**2 >= 0.46785600000000005)
m.e909 = Constraint(expr= (m.x13 - m.x52)**2 + (m.x92 - m.x131)**2 + (m.x171 -
    m.x210)**2 >= 0.46785600000000005)
m.e910 = Constraint(expr= (m.x13 - m.x53)**2 + (m.x92 - m.x132)**2 + (m.x171 -
    m.x211)**2 >= 0.46785600000000005)
m.e911 = Constraint(expr= (m.x13 - m.x54)**2 + (m.x92 - m.x133)**2 + (m.x171 -
    m.x212)**2 >= 0.46785600000000005)
m.e912 = Constraint(expr= (m.x13 - m.x55)**2 + (m.x92 - m.x134)**2 + (m.x171 -
    m.x213)**2 >= 0.46785600000000005)
m.e913 = Constraint(expr= (m.x13 - m.x56)**2 + (m.x92 - m.x135)**2 + (m.x171 -
    m.x214)**2 >= 0.46785600000000005)
m.e914 = Constraint(expr= (m.x13 - m.x57)**2 + (m.x92 - m.x136)**2 + (m.x171 -
    m.x215)**2 >= 0.46785600000000005)
m.e915 = Constraint(expr= (m.x13 - m.x58)**2 + (m.x92 - m.x137)**2 + (m.x171 -
    m.x216)**2 >= 0.46785600000000005)
m.e916 = Constraint(expr= (m.x13 - m.x59)**2 + (m.x92 - m.x138)**2 + (m.x171 -
    m.x217)**2 >= 0.46785600000000005)
m.e917 = Constraint(expr= (m.x13 - m.x60)**2 + (m.x92 - m.x139)**2 + (m.x171 -
    m.x218)**2 >= 0.46785600000000005)
m.e918 = Constraint(expr= (m.x13 - m.x61)**2 + (m.x92 - m.x140)**2 + (m.x171 -
    m.x219)**2 >= 0.46785600000000005)
m.e919 = Constraint(expr= (m.x13 - m.x62)**2 + (m.x92 - m.x141)**2 + (m.x171 -
    m.x220)**2 >= 0.46785600000000005)
m.e920 = Constraint(expr= (m.x13 - m.x63)**2 + (m.x92 - m.x142)**2 + (m.x171 -
    m.x221)**2 >= 0.46785600000000005)
m.e921 = Constraint(expr= (m.x13 - m.x64)**2 + (m.x92 - m.x143)**2 + (m.x171 -
    m.x222)**2 >= 0.46785600000000005)
m.e922 = Constraint(expr= (m.x13 - m.x65)**2 + (m.x92 - m.x144)**2 + (m.x171 -
    m.x223)**2 >= 0.46785600000000005)
m.e923 = Constraint(expr= (m.x13 - m.x66)**2 + (m.x92 - m.x145)**2 + (m.x171 -
    m.x224)**2 >= 0.46785600000000005)
m.e924 = Constraint(expr= (m.x13 - m.x67)**2 + (m.x92 - m.x146)**2 + (m.x171 -
    m.x225)**2 >= 0.46785600000000005)
m.e925 = Constraint(expr= (m.x13 - m.x68)**2 + (m.x92 - m.x147)**2 + (m.x171 -
    m.x226)**2 >= 0.46785600000000005)
m.e926 = Constraint(expr= (m.x13 - m.x69)**2 + (m.x92 - m.x148)**2 + (m.x171 -
    m.x227)**2 >= 0.46785600000000005)
m.e927 = Constraint(expr= (m.x13 - m.x70)**2 + (m.x92 - m.x149)**2 + (m.x171 -
    m.x228)**2 >= 0.46785600000000005)
m.e928 = Constraint(expr= (m.x13 - m.x71)**2 + (m.x92 - m.x150)**2 + (m.x171 -
    m.x229)**2 >= 0.46785600000000005)
m.e929 = Constraint(expr= (m.x13 - m.x72)**2 + (m.x92 - m.x151)**2 + (m.x171 -
    m.x230)**2 >= 0.46785600000000005)
m.e930 = Constraint(expr= (m.x13 - m.x73)**2 + (m.x92 - m.x152)**2 + (m.x171 -
    m.x231)**2 >= 0.46785600000000005)
m.e931 = Constraint(expr= (m.x13 - m.x74)**2 + (m.x92 - m.x153)**2 + (m.x171 -
    m.x232)**2 >= 0.46785600000000005)
m.e932 = Constraint(expr= (m.x13 - m.x75)**2 + (m.x92 - m.x154)**2 + (m.x171 -
    m.x233)**2 >= 0.46785600000000005)
m.e933 = Constraint(expr= (m.x13 - m.x76)**2 + (m.x92 - m.x155)**2 + (m.x171 -
    m.x234)**2 >= 0.46785600000000005)
m.e934 = Constraint(expr= (m.x13 - m.x77)**2 + (m.x92 - m.x156)**2 + (m.x171 -
    m.x235)**2 >= 0.46785600000000005)
m.e935 = Constraint(expr= (m.x13 - m.x78)**2 + (m.x92 - m.x157)**2 + (m.x171 -
    m.x236)**2 >= 0.46785600000000005)
m.e936 = Constraint(expr= (m.x13 - m.x79)**2 + (m.x92 - m.x158)**2 + (m.x171 -
    m.x237)**2 >= 0.46785600000000005)
m.e937 = Constraint(expr= (m.x14 - m.x15)**2 + (m.x93 - m.x94)**2 + (m.x172 -
    m.x173)**2 >= 0.46785600000000005)
m.e938 = Constraint(expr= (m.x14 - m.x16)**2 + (m.x93 - m.x95)**2 + (m.x172 -
    m.x174)**2 >= 0.46785600000000005)
m.e939 = Constraint(expr= (m.x14 - m.x17)**2 + (m.x93 - m.x96)**2 + (m.x172 -
    m.x175)**2 >= 0.46785600000000005)
m.e940 = Constraint(expr= (m.x14 - m.x18)**2 + (m.x93 - m.x97)**2 + (m.x172 -
    m.x176)**2 >= 0.46785600000000005)
m.e941 = Constraint(expr= (m.x14 - m.x19)**2 + (m.x93 - m.x98)**2 + (m.x172 -
    m.x177)**2 >= 0.46785600000000005)
m.e942 = Constraint(expr= (m.x14 - m.x20)**2 + (m.x93 - m.x99)**2 + (m.x172 -
    m.x178)**2 >= 0.46785600000000005)
m.e943 = Constraint(expr= (m.x14 - m.x21)**2 + (m.x93 - m.x100)**2 + (m.x172 -
    m.x179)**2 >= 0.46785600000000005)
m.e944 = Constraint(expr= (m.x14 - m.x22)**2 + (m.x93 - m.x101)**2 + (m.x172 -
    m.x180)**2 >= 0.46785600000000005)
m.e945 = Constraint(expr= (m.x14 - m.x23)**2 + (m.x93 - m.x102)**2 + (m.x172 -
    m.x181)**2 >= 0.46785600000000005)
m.e946 = Constraint(expr= (m.x14 - m.x24)**2 + (m.x93 - m.x103)**2 + (m.x172 -
    m.x182)**2 >= 0.46785600000000005)
m.e947 = Constraint(expr= (m.x14 - m.x25)**2 + (m.x93 - m.x104)**2 + (m.x172 -
    m.x183)**2 >= 0.46785600000000005)
m.e948 = Constraint(expr= (m.x14 - m.x26)**2 + (m.x93 - m.x105)**2 + (m.x172 -
    m.x184)**2 >= 0.46785600000000005)
m.e949 = Constraint(expr= (m.x14 - m.x27)**2 + (m.x93 - m.x106)**2 + (m.x172 -
    m.x185)**2 >= 0.46785600000000005)
m.e950 = Constraint(expr= (m.x14 - m.x28)**2 + (m.x93 - m.x107)**2 + (m.x172 -
    m.x186)**2 >= 0.46785600000000005)
m.e951 = Constraint(expr= (m.x14 - m.x29)**2 + (m.x93 - m.x108)**2 + (m.x172 -
    m.x187)**2 >= 0.46785600000000005)
m.e952 = Constraint(expr= (m.x14 - m.x30)**2 + (m.x93 - m.x109)**2 + (m.x172 -
    m.x188)**2 >= 0.46785600000000005)
m.e953 = Constraint(expr= (m.x14 - m.x31)**2 + (m.x93 - m.x110)**2 + (m.x172 -
    m.x189)**2 >= 0.46785600000000005)
m.e954 = Constraint(expr= (m.x14 - m.x32)**2 + (m.x93 - m.x111)**2 + (m.x172 -
    m.x190)**2 >= 0.46785600000000005)
m.e955 = Constraint(expr= (m.x14 - m.x33)**2 + (m.x93 - m.x112)**2 + (m.x172 -
    m.x191)**2 >= 0.46785600000000005)
m.e956 = Constraint(expr= (m.x14 - m.x34)**2 + (m.x93 - m.x113)**2 + (m.x172 -
    m.x192)**2 >= 0.46785600000000005)
m.e957 = Constraint(expr= (m.x14 - m.x35)**2 + (m.x93 - m.x114)**2 + (m.x172 -
    m.x193)**2 >= 0.46785600000000005)
m.e958 = Constraint(expr= (m.x14 - m.x36)**2 + (m.x93 - m.x115)**2 + (m.x172 -
    m.x194)**2 >= 0.46785600000000005)
m.e959 = Constraint(expr= (m.x14 - m.x37)**2 + (m.x93 - m.x116)**2 + (m.x172 -
    m.x195)**2 >= 0.46785600000000005)
m.e960 = Constraint(expr= (m.x14 - m.x38)**2 + (m.x93 - m.x117)**2 + (m.x172 -
    m.x196)**2 >= 0.46785600000000005)
m.e961 = Constraint(expr= (m.x14 - m.x39)**2 + (m.x93 - m.x118)**2 + (m.x172 -
    m.x197)**2 >= 0.46785600000000005)
m.e962 = Constraint(expr= (m.x14 - m.x40)**2 + (m.x93 - m.x119)**2 + (m.x172 -
    m.x198)**2 >= 0.46785600000000005)
m.e963 = Constraint(expr= (m.x14 - m.x41)**2 + (m.x93 - m.x120)**2 + (m.x172 -
    m.x199)**2 >= 0.46785600000000005)
m.e964 = Constraint(expr= (m.x14 - m.x42)**2 + (m.x93 - m.x121)**2 + (m.x172 -
    m.x200)**2 >= 0.46785600000000005)
m.e965 = Constraint(expr= (m.x14 - m.x43)**2 + (m.x93 - m.x122)**2 + (m.x172 -
    m.x201)**2 >= 0.46785600000000005)
m.e966 = Constraint(expr= (m.x14 - m.x44)**2 + (m.x93 - m.x123)**2 + (m.x172 -
    m.x202)**2 >= 0.46785600000000005)
m.e967 = Constraint(expr= (m.x14 - m.x45)**2 + (m.x93 - m.x124)**2 + (m.x172 -
    m.x203)**2 >= 0.46785600000000005)
m.e968 = Constraint(expr= (m.x14 - m.x46)**2 + (m.x93 - m.x125)**2 + (m.x172 -
    m.x204)**2 >= 0.46785600000000005)
m.e969 = Constraint(expr= (m.x14 - m.x47)**2 + (m.x93 - m.x126)**2 + (m.x172 -
    m.x205)**2 >= 0.46785600000000005)
m.e970 = Constraint(expr= (m.x14 - m.x48)**2 + (m.x93 - m.x127)**2 + (m.x172 -
    m.x206)**2 >= 0.46785600000000005)
m.e971 = Constraint(expr= (m.x14 - m.x49)**2 + (m.x93 - m.x128)**2 + (m.x172 -
    m.x207)**2 >= 0.46785600000000005)
m.e972 = Constraint(expr= (m.x14 - m.x50)**2 + (m.x93 - m.x129)**2 + (m.x172 -
    m.x208)**2 >= 0.46785600000000005)
m.e973 = Constraint(expr= (m.x14 - m.x51)**2 + (m.x93 - m.x130)**2 + (m.x172 -
    m.x209)**2 >= 0.46785600000000005)
m.e974 = Constraint(expr= (m.x14 - m.x52)**2 + (m.x93 - m.x131)**2 + (m.x172 -
    m.x210)**2 >= 0.46785600000000005)
m.e975 = Constraint(expr= (m.x14 - m.x53)**2 + (m.x93 - m.x132)**2 + (m.x172 -
    m.x211)**2 >= 0.46785600000000005)
m.e976 = Constraint(expr= (m.x14 - m.x54)**2 + (m.x93 - m.x133)**2 + (m.x172 -
    m.x212)**2 >= 0.46785600000000005)
m.e977 = Constraint(expr= (m.x14 - m.x55)**2 + (m.x93 - m.x134)**2 + (m.x172 -
    m.x213)**2 >= 0.46785600000000005)
m.e978 = Constraint(expr= (m.x14 - m.x56)**2 + (m.x93 - m.x135)**2 + (m.x172 -
    m.x214)**2 >= 0.46785600000000005)
m.e979 = Constraint(expr= (m.x14 - m.x57)**2 + (m.x93 - m.x136)**2 + (m.x172 -
    m.x215)**2 >= 0.46785600000000005)
m.e980 = Constraint(expr= (m.x14 - m.x58)**2 + (m.x93 - m.x137)**2 + (m.x172 -
    m.x216)**2 >= 0.46785600000000005)
m.e981 = Constraint(expr= (m.x14 - m.x59)**2 + (m.x93 - m.x138)**2 + (m.x172 -
    m.x217)**2 >= 0.46785600000000005)
m.e982 = Constraint(expr= (m.x14 - m.x60)**2 + (m.x93 - m.x139)**2 + (m.x172 -
    m.x218)**2 >= 0.46785600000000005)
m.e983 = Constraint(expr= (m.x14 - m.x61)**2 + (m.x93 - m.x140)**2 + (m.x172 -
    m.x219)**2 >= 0.46785600000000005)
m.e984 = Constraint(expr= (m.x14 - m.x62)**2 + (m.x93 - m.x141)**2 + (m.x172 -
    m.x220)**2 >= 0.46785600000000005)
m.e985 = Constraint(expr= (m.x14 - m.x63)**2 + (m.x93 - m.x142)**2 + (m.x172 -
    m.x221)**2 >= 0.46785600000000005)
m.e986 = Constraint(expr= (m.x14 - m.x64)**2 + (m.x93 - m.x143)**2 + (m.x172 -
    m.x222)**2 >= 0.46785600000000005)
m.e987 = Constraint(expr= (m.x14 - m.x65)**2 + (m.x93 - m.x144)**2 + (m.x172 -
    m.x223)**2 >= 0.46785600000000005)
m.e988 = Constraint(expr= (m.x14 - m.x66)**2 + (m.x93 - m.x145)**2 + (m.x172 -
    m.x224)**2 >= 0.46785600000000005)
m.e989 = Constraint(expr= (m.x14 - m.x67)**2 + (m.x93 - m.x146)**2 + (m.x172 -
    m.x225)**2 >= 0.46785600000000005)
m.e990 = Constraint(expr= (m.x14 - m.x68)**2 + (m.x93 - m.x147)**2 + (m.x172 -
    m.x226)**2 >= 0.46785600000000005)
m.e991 = Constraint(expr= (m.x14 - m.x69)**2 + (m.x93 - m.x148)**2 + (m.x172 -
    m.x227)**2 >= 0.46785600000000005)
m.e992 = Constraint(expr= (m.x14 - m.x70)**2 + (m.x93 - m.x149)**2 + (m.x172 -
    m.x228)**2 >= 0.46785600000000005)
m.e993 = Constraint(expr= (m.x14 - m.x71)**2 + (m.x93 - m.x150)**2 + (m.x172 -
    m.x229)**2 >= 0.46785600000000005)
m.e994 = Constraint(expr= (m.x14 - m.x72)**2 + (m.x93 - m.x151)**2 + (m.x172 -
    m.x230)**2 >= 0.46785600000000005)
m.e995 = Constraint(expr= (m.x14 - m.x73)**2 + (m.x93 - m.x152)**2 + (m.x172 -
    m.x231)**2 >= 0.46785600000000005)
m.e996 = Constraint(expr= (m.x14 - m.x74)**2 + (m.x93 - m.x153)**2 + (m.x172 -
    m.x232)**2 >= 0.46785600000000005)
m.e997 = Constraint(expr= (m.x14 - m.x75)**2 + (m.x93 - m.x154)**2 + (m.x172 -
    m.x233)**2 >= 0.46785600000000005)
m.e998 = Constraint(expr= (m.x14 - m.x76)**2 + (m.x93 - m.x155)**2 + (m.x172 -
    m.x234)**2 >= 0.46785600000000005)
m.e999 = Constraint(expr= (m.x14 - m.x77)**2 + (m.x93 - m.x156)**2 + (m.x172 -
    m.x235)**2 >= 0.46785600000000005)
m.e1000 = Constraint(expr= (m.x14 - m.x78)**2 + (m.x93 - m.x157)**2 + (m.x172
    - m.x236)**2 >= 0.46785600000000005)
m.e1001 = Constraint(expr= (m.x14 - m.x79)**2 + (m.x93 - m.x158)**2 + (m.x172
    - m.x237)**2 >= 0.46785600000000005)
m.e1002 = Constraint(expr= (m.x15 - m.x16)**2 + (m.x94 - m.x95)**2 + (m.x173 -
    m.x174)**2 >= 0.46785600000000005)
m.e1003 = Constraint(expr= (m.x15 - m.x17)**2 + (m.x94 - m.x96)**2 + (m.x173 -
    m.x175)**2 >= 0.46785600000000005)
m.e1004 = Constraint(expr= (m.x15 - m.x18)**2 + (m.x94 - m.x97)**2 + (m.x173 -
    m.x176)**2 >= 0.46785600000000005)
m.e1005 = Constraint(expr= (m.x15 - m.x19)**2 + (m.x94 - m.x98)**2 + (m.x173 -
    m.x177)**2 >= 0.46785600000000005)
m.e1006 = Constraint(expr= (m.x15 - m.x20)**2 + (m.x94 - m.x99)**2 + (m.x173 -
    m.x178)**2 >= 0.46785600000000005)
m.e1007 = Constraint(expr= (m.x15 - m.x21)**2 + (m.x94 - m.x100)**2 + (m.x173
    - m.x179)**2 >= 0.46785600000000005)
m.e1008 = Constraint(expr= (m.x15 - m.x22)**2 + (m.x94 - m.x101)**2 + (m.x173
    - m.x180)**2 >= 0.46785600000000005)
m.e1009 = Constraint(expr= (m.x15 - m.x23)**2 + (m.x94 - m.x102)**2 + (m.x173
    - m.x181)**2 >= 0.46785600000000005)
m.e1010 = Constraint(expr= (m.x15 - m.x24)**2 + (m.x94 - m.x103)**2 + (m.x173
    - m.x182)**2 >= 0.46785600000000005)
m.e1011 = Constraint(expr= (m.x15 - m.x25)**2 + (m.x94 - m.x104)**2 + (m.x173
    - m.x183)**2 >= 0.46785600000000005)
m.e1012 = Constraint(expr= (m.x15 - m.x26)**2 + (m.x94 - m.x105)**2 + (m.x173
    - m.x184)**2 >= 0.46785600000000005)
m.e1013 = Constraint(expr= (m.x15 - m.x27)**2 + (m.x94 - m.x106)**2 + (m.x173
    - m.x185)**2 >= 0.46785600000000005)
m.e1014 = Constraint(expr= (m.x15 - m.x28)**2 + (m.x94 - m.x107)**2 + (m.x173
    - m.x186)**2 >= 0.46785600000000005)
m.e1015 = Constraint(expr= (m.x15 - m.x29)**2 + (m.x94 - m.x108)**2 + (m.x173
    - m.x187)**2 >= 0.46785600000000005)
m.e1016 = Constraint(expr= (m.x15 - m.x30)**2 + (m.x94 - m.x109)**2 + (m.x173
    - m.x188)**2 >= 0.46785600000000005)
m.e1017 = Constraint(expr= (m.x15 - m.x31)**2 + (m.x94 - m.x110)**2 + (m.x173
    - m.x189)**2 >= 0.46785600000000005)
m.e1018 = Constraint(expr= (m.x15 - m.x32)**2 + (m.x94 - m.x111)**2 + (m.x173
    - m.x190)**2 >= 0.46785600000000005)
m.e1019 = Constraint(expr= (m.x15 - m.x33)**2 + (m.x94 - m.x112)**2 + (m.x173
    - m.x191)**2 >= 0.46785600000000005)
m.e1020 = Constraint(expr= (m.x15 - m.x34)**2 + (m.x94 - m.x113)**2 + (m.x173
    - m.x192)**2 >= 0.46785600000000005)
m.e1021 = Constraint(expr= (m.x15 - m.x35)**2 + (m.x94 - m.x114)**2 + (m.x173
    - m.x193)**2 >= 0.46785600000000005)
m.e1022 = Constraint(expr= (m.x15 - m.x36)**2 + (m.x94 - m.x115)**2 + (m.x173
    - m.x194)**2 >= 0.46785600000000005)
m.e1023 = Constraint(expr= (m.x15 - m.x37)**2 + (m.x94 - m.x116)**2 + (m.x173
    - m.x195)**2 >= 0.46785600000000005)
m.e1024 = Constraint(expr= (m.x15 - m.x38)**2 + (m.x94 - m.x117)**2 + (m.x173
    - m.x196)**2 >= 0.46785600000000005)
m.e1025 = Constraint(expr= (m.x15 - m.x39)**2 + (m.x94 - m.x118)**2 + (m.x173
    - m.x197)**2 >= 0.46785600000000005)
m.e1026 = Constraint(expr= (m.x15 - m.x40)**2 + (m.x94 - m.x119)**2 + (m.x173
    - m.x198)**2 >= 0.46785600000000005)
m.e1027 = Constraint(expr= (m.x15 - m.x41)**2 + (m.x94 - m.x120)**2 + (m.x173
    - m.x199)**2 >= 0.46785600000000005)
m.e1028 = Constraint(expr= (m.x15 - m.x42)**2 + (m.x94 - m.x121)**2 + (m.x173
    - m.x200)**2 >= 0.46785600000000005)
m.e1029 = Constraint(expr= (m.x15 - m.x43)**2 + (m.x94 - m.x122)**2 + (m.x173
    - m.x201)**2 >= 0.46785600000000005)
m.e1030 = Constraint(expr= (m.x15 - m.x44)**2 + (m.x94 - m.x123)**2 + (m.x173
    - m.x202)**2 >= 0.46785600000000005)
m.e1031 = Constraint(expr= (m.x15 - m.x45)**2 + (m.x94 - m.x124)**2 + (m.x173
    - m.x203)**2 >= 0.46785600000000005)
m.e1032 = Constraint(expr= (m.x15 - m.x46)**2 + (m.x94 - m.x125)**2 + (m.x173
    - m.x204)**2 >= 0.46785600000000005)
m.e1033 = Constraint(expr= (m.x15 - m.x47)**2 + (m.x94 - m.x126)**2 + (m.x173
    - m.x205)**2 >= 0.46785600000000005)
m.e1034 = Constraint(expr= (m.x15 - m.x48)**2 + (m.x94 - m.x127)**2 + (m.x173
    - m.x206)**2 >= 0.46785600000000005)
m.e1035 = Constraint(expr= (m.x15 - m.x49)**2 + (m.x94 - m.x128)**2 + (m.x173
    - m.x207)**2 >= 0.46785600000000005)
m.e1036 = Constraint(expr= (m.x15 - m.x50)**2 + (m.x94 - m.x129)**2 + (m.x173
    - m.x208)**2 >= 0.46785600000000005)
m.e1037 = Constraint(expr= (m.x15 - m.x51)**2 + (m.x94 - m.x130)**2 + (m.x173
    - m.x209)**2 >= 0.46785600000000005)
m.e1038 = Constraint(expr= (m.x15 - m.x52)**2 + (m.x94 - m.x131)**2 + (m.x173
    - m.x210)**2 >= 0.46785600000000005)
m.e1039 = Constraint(expr= (m.x15 - m.x53)**2 + (m.x94 - m.x132)**2 + (m.x173
    - m.x211)**2 >= 0.46785600000000005)
m.e1040 = Constraint(expr= (m.x15 - m.x54)**2 + (m.x94 - m.x133)**2 + (m.x173
    - m.x212)**2 >= 0.46785600000000005)
m.e1041 = Constraint(expr= (m.x15 - m.x55)**2 + (m.x94 - m.x134)**2 + (m.x173
    - m.x213)**2 >= 0.46785600000000005)
m.e1042 = Constraint(expr= (m.x15 - m.x56)**2 + (m.x94 - m.x135)**2 + (m.x173
    - m.x214)**2 >= 0.46785600000000005)
m.e1043 = Constraint(expr= (m.x15 - m.x57)**2 + (m.x94 - m.x136)**2 + (m.x173
    - m.x215)**2 >= 0.46785600000000005)
m.e1044 = Constraint(expr= (m.x15 - m.x58)**2 + (m.x94 - m.x137)**2 + (m.x173
    - m.x216)**2 >= 0.46785600000000005)
m.e1045 = Constraint(expr= (m.x15 - m.x59)**2 + (m.x94 - m.x138)**2 + (m.x173
    - m.x217)**2 >= 0.46785600000000005)
m.e1046 = Constraint(expr= (m.x15 - m.x60)**2 + (m.x94 - m.x139)**2 + (m.x173
    - m.x218)**2 >= 0.46785600000000005)
m.e1047 = Constraint(expr= (m.x15 - m.x61)**2 + (m.x94 - m.x140)**2 + (m.x173
    - m.x219)**2 >= 0.46785600000000005)
m.e1048 = Constraint(expr= (m.x15 - m.x62)**2 + (m.x94 - m.x141)**2 + (m.x173
    - m.x220)**2 >= 0.46785600000000005)
m.e1049 = Constraint(expr= (m.x15 - m.x63)**2 + (m.x94 - m.x142)**2 + (m.x173
    - m.x221)**2 >= 0.46785600000000005)
m.e1050 = Constraint(expr= (m.x15 - m.x64)**2 + (m.x94 - m.x143)**2 + (m.x173
    - m.x222)**2 >= 0.46785600000000005)
m.e1051 = Constraint(expr= (m.x15 - m.x65)**2 + (m.x94 - m.x144)**2 + (m.x173
    - m.x223)**2 >= 0.46785600000000005)
m.e1052 = Constraint(expr= (m.x15 - m.x66)**2 + (m.x94 - m.x145)**2 + (m.x173
    - m.x224)**2 >= 0.46785600000000005)
m.e1053 = Constraint(expr= (m.x15 - m.x67)**2 + (m.x94 - m.x146)**2 + (m.x173
    - m.x225)**2 >= 0.46785600000000005)
m.e1054 = Constraint(expr= (m.x15 - m.x68)**2 + (m.x94 - m.x147)**2 + (m.x173
    - m.x226)**2 >= 0.46785600000000005)
m.e1055 = Constraint(expr= (m.x15 - m.x69)**2 + (m.x94 - m.x148)**2 + (m.x173
    - m.x227)**2 >= 0.46785600000000005)
m.e1056 = Constraint(expr= (m.x15 - m.x70)**2 + (m.x94 - m.x149)**2 + (m.x173
    - m.x228)**2 >= 0.46785600000000005)
m.e1057 = Constraint(expr= (m.x15 - m.x71)**2 + (m.x94 - m.x150)**2 + (m.x173
    - m.x229)**2 >= 0.46785600000000005)
m.e1058 = Constraint(expr= (m.x15 - m.x72)**2 + (m.x94 - m.x151)**2 + (m.x173
    - m.x230)**2 >= 0.46785600000000005)
m.e1059 = Constraint(expr= (m.x15 - m.x73)**2 + (m.x94 - m.x152)**2 + (m.x173
    - m.x231)**2 >= 0.46785600000000005)
m.e1060 = Constraint(expr= (m.x15 - m.x74)**2 + (m.x94 - m.x153)**2 + (m.x173
    - m.x232)**2 >= 0.46785600000000005)
m.e1061 = Constraint(expr= (m.x15 - m.x75)**2 + (m.x94 - m.x154)**2 + (m.x173
    - m.x233)**2 >= 0.46785600000000005)
m.e1062 = Constraint(expr= (m.x15 - m.x76)**2 + (m.x94 - m.x155)**2 + (m.x173
    - m.x234)**2 >= 0.46785600000000005)
m.e1063 = Constraint(expr= (m.x15 - m.x77)**2 + (m.x94 - m.x156)**2 + (m.x173
    - m.x235)**2 >= 0.46785600000000005)
m.e1064 = Constraint(expr= (m.x15 - m.x78)**2 + (m.x94 - m.x157)**2 + (m.x173
    - m.x236)**2 >= 0.46785600000000005)
m.e1065 = Constraint(expr= (m.x15 - m.x79)**2 + (m.x94 - m.x158)**2 + (m.x173
    - m.x237)**2 >= 0.46785600000000005)
m.e1066 = Constraint(expr= (m.x16 - m.x17)**2 + (m.x95 - m.x96)**2 + (m.x174 -
    m.x175)**2 >= 0.46785600000000005)
m.e1067 = Constraint(expr= (m.x16 - m.x18)**2 + (m.x95 - m.x97)**2 + (m.x174 -
    m.x176)**2 >= 0.46785600000000005)
m.e1068 = Constraint(expr= (m.x16 - m.x19)**2 + (m.x95 - m.x98)**2 + (m.x174 -
    m.x177)**2 >= 0.46785600000000005)
m.e1069 = Constraint(expr= (m.x16 - m.x20)**2 + (m.x95 - m.x99)**2 + (m.x174 -
    m.x178)**2 >= 0.46785600000000005)
m.e1070 = Constraint(expr= (m.x16 - m.x21)**2 + (m.x95 - m.x100)**2 + (m.x174
    - m.x179)**2 >= 0.46785600000000005)
m.e1071 = Constraint(expr= (m.x16 - m.x22)**2 + (m.x95 - m.x101)**2 + (m.x174
    - m.x180)**2 >= 0.46785600000000005)
m.e1072 = Constraint(expr= (m.x16 - m.x23)**2 + (m.x95 - m.x102)**2 + (m.x174
    - m.x181)**2 >= 0.46785600000000005)
m.e1073 = Constraint(expr= (m.x16 - m.x24)**2 + (m.x95 - m.x103)**2 + (m.x174
    - m.x182)**2 >= 0.46785600000000005)
m.e1074 = Constraint(expr= (m.x16 - m.x25)**2 + (m.x95 - m.x104)**2 + (m.x174
    - m.x183)**2 >= 0.46785600000000005)
m.e1075 = Constraint(expr= (m.x16 - m.x26)**2 + (m.x95 - m.x105)**2 + (m.x174
    - m.x184)**2 >= 0.46785600000000005)
m.e1076 = Constraint(expr= (m.x16 - m.x27)**2 + (m.x95 - m.x106)**2 + (m.x174
    - m.x185)**2 >= 0.46785600000000005)
m.e1077 = Constraint(expr= (m.x16 - m.x28)**2 + (m.x95 - m.x107)**2 + (m.x174
    - m.x186)**2 >= 0.46785600000000005)
m.e1078 = Constraint(expr= (m.x16 - m.x29)**2 + (m.x95 - m.x108)**2 + (m.x174
    - m.x187)**2 >= 0.46785600000000005)
m.e1079 = Constraint(expr= (m.x16 - m.x30)**2 + (m.x95 - m.x109)**2 + (m.x174
    - m.x188)**2 >= 0.46785600000000005)
m.e1080 = Constraint(expr= (m.x16 - m.x31)**2 + (m.x95 - m.x110)**2 + (m.x174
    - m.x189)**2 >= 0.46785600000000005)
m.e1081 = Constraint(expr= (m.x16 - m.x32)**2 + (m.x95 - m.x111)**2 + (m.x174
    - m.x190)**2 >= 0.46785600000000005)
m.e1082 = Constraint(expr= (m.x16 - m.x33)**2 + (m.x95 - m.x112)**2 + (m.x174
    - m.x191)**2 >= 0.46785600000000005)
m.e1083 = Constraint(expr= (m.x16 - m.x34)**2 + (m.x95 - m.x113)**2 + (m.x174
    - m.x192)**2 >= 0.46785600000000005)
m.e1084 = Constraint(expr= (m.x16 - m.x35)**2 + (m.x95 - m.x114)**2 + (m.x174
    - m.x193)**2 >= 0.46785600000000005)
m.e1085 = Constraint(expr= (m.x16 - m.x36)**2 + (m.x95 - m.x115)**2 + (m.x174
    - m.x194)**2 >= 0.46785600000000005)
m.e1086 = Constraint(expr= (m.x16 - m.x37)**2 + (m.x95 - m.x116)**2 + (m.x174
    - m.x195)**2 >= 0.46785600000000005)
m.e1087 = Constraint(expr= (m.x16 - m.x38)**2 + (m.x95 - m.x117)**2 + (m.x174
    - m.x196)**2 >= 0.46785600000000005)
m.e1088 = Constraint(expr= (m.x16 - m.x39)**2 + (m.x95 - m.x118)**2 + (m.x174
    - m.x197)**2 >= 0.46785600000000005)
m.e1089 = Constraint(expr= (m.x16 - m.x40)**2 + (m.x95 - m.x119)**2 + (m.x174
    - m.x198)**2 >= 0.46785600000000005)
m.e1090 = Constraint(expr= (m.x16 - m.x41)**2 + (m.x95 - m.x120)**2 + (m.x174
    - m.x199)**2 >= 0.46785600000000005)
m.e1091 = Constraint(expr= (m.x16 - m.x42)**2 + (m.x95 - m.x121)**2 + (m.x174
    - m.x200)**2 >= 0.46785600000000005)
m.e1092 = Constraint(expr= (m.x16 - m.x43)**2 + (m.x95 - m.x122)**2 + (m.x174
    - m.x201)**2 >= 0.46785600000000005)
m.e1093 = Constraint(expr= (m.x16 - m.x44)**2 + (m.x95 - m.x123)**2 + (m.x174
    - m.x202)**2 >= 0.46785600000000005)
m.e1094 = Constraint(expr= (m.x16 - m.x45)**2 + (m.x95 - m.x124)**2 + (m.x174
    - m.x203)**2 >= 0.46785600000000005)
m.e1095 = Constraint(expr= (m.x16 - m.x46)**2 + (m.x95 - m.x125)**2 + (m.x174
    - m.x204)**2 >= 0.46785600000000005)
m.e1096 = Constraint(expr= (m.x16 - m.x47)**2 + (m.x95 - m.x126)**2 + (m.x174
    - m.x205)**2 >= 0.46785600000000005)
m.e1097 = Constraint(expr= (m.x16 - m.x48)**2 + (m.x95 - m.x127)**2 + (m.x174
    - m.x206)**2 >= 0.46785600000000005)
m.e1098 = Constraint(expr= (m.x16 - m.x49)**2 + (m.x95 - m.x128)**2 + (m.x174
    - m.x207)**2 >= 0.46785600000000005)
m.e1099 = Constraint(expr= (m.x16 - m.x50)**2 + (m.x95 - m.x129)**2 + (m.x174
    - m.x208)**2 >= 0.46785600000000005)
m.e1100 = Constraint(expr= (m.x16 - m.x51)**2 + (m.x95 - m.x130)**2 + (m.x174
    - m.x209)**2 >= 0.46785600000000005)
m.e1101 = Constraint(expr= (m.x16 - m.x52)**2 + (m.x95 - m.x131)**2 + (m.x174
    - m.x210)**2 >= 0.46785600000000005)
m.e1102 = Constraint(expr= (m.x16 - m.x53)**2 + (m.x95 - m.x132)**2 + (m.x174
    - m.x211)**2 >= 0.46785600000000005)
m.e1103 = Constraint(expr= (m.x16 - m.x54)**2 + (m.x95 - m.x133)**2 + (m.x174
    - m.x212)**2 >= 0.46785600000000005)
m.e1104 = Constraint(expr= (m.x16 - m.x55)**2 + (m.x95 - m.x134)**2 + (m.x174
    - m.x213)**2 >= 0.46785600000000005)
m.e1105 = Constraint(expr= (m.x16 - m.x56)**2 + (m.x95 - m.x135)**2 + (m.x174
    - m.x214)**2 >= 0.46785600000000005)
m.e1106 = Constraint(expr= (m.x16 - m.x57)**2 + (m.x95 - m.x136)**2 + (m.x174
    - m.x215)**2 >= 0.46785600000000005)
m.e1107 = Constraint(expr= (m.x16 - m.x58)**2 + (m.x95 - m.x137)**2 + (m.x174
    - m.x216)**2 >= 0.46785600000000005)
m.e1108 = Constraint(expr= (m.x16 - m.x59)**2 + (m.x95 - m.x138)**2 + (m.x174
    - m.x217)**2 >= 0.46785600000000005)
m.e1109 = Constraint(expr= (m.x16 - m.x60)**2 + (m.x95 - m.x139)**2 + (m.x174
    - m.x218)**2 >= 0.46785600000000005)
m.e1110 = Constraint(expr= (m.x16 - m.x61)**2 + (m.x95 - m.x140)**2 + (m.x174
    - m.x219)**2 >= 0.46785600000000005)
m.e1111 = Constraint(expr= (m.x16 - m.x62)**2 + (m.x95 - m.x141)**2 + (m.x174
    - m.x220)**2 >= 0.46785600000000005)
m.e1112 = Constraint(expr= (m.x16 - m.x63)**2 + (m.x95 - m.x142)**2 + (m.x174
    - m.x221)**2 >= 0.46785600000000005)
m.e1113 = Constraint(expr= (m.x16 - m.x64)**2 + (m.x95 - m.x143)**2 + (m.x174
    - m.x222)**2 >= 0.46785600000000005)
m.e1114 = Constraint(expr= (m.x16 - m.x65)**2 + (m.x95 - m.x144)**2 + (m.x174
    - m.x223)**2 >= 0.46785600000000005)
m.e1115 = Constraint(expr= (m.x16 - m.x66)**2 + (m.x95 - m.x145)**2 + (m.x174
    - m.x224)**2 >= 0.46785600000000005)
m.e1116 = Constraint(expr= (m.x16 - m.x67)**2 + (m.x95 - m.x146)**2 + (m.x174
    - m.x225)**2 >= 0.46785600000000005)
m.e1117 = Constraint(expr= (m.x16 - m.x68)**2 + (m.x95 - m.x147)**2 + (m.x174
    - m.x226)**2 >= 0.46785600000000005)
m.e1118 = Constraint(expr= (m.x16 - m.x69)**2 + (m.x95 - m.x148)**2 + (m.x174
    - m.x227)**2 >= 0.46785600000000005)
m.e1119 = Constraint(expr= (m.x16 - m.x70)**2 + (m.x95 - m.x149)**2 + (m.x174
    - m.x228)**2 >= 0.46785600000000005)
m.e1120 = Constraint(expr= (m.x16 - m.x71)**2 + (m.x95 - m.x150)**2 + (m.x174
    - m.x229)**2 >= 0.46785600000000005)
m.e1121 = Constraint(expr= (m.x16 - m.x72)**2 + (m.x95 - m.x151)**2 + (m.x174
    - m.x230)**2 >= 0.46785600000000005)
m.e1122 = Constraint(expr= (m.x16 - m.x73)**2 + (m.x95 - m.x152)**2 + (m.x174
    - m.x231)**2 >= 0.46785600000000005)
m.e1123 = Constraint(expr= (m.x16 - m.x74)**2 + (m.x95 - m.x153)**2 + (m.x174
    - m.x232)**2 >= 0.46785600000000005)
m.e1124 = Constraint(expr= (m.x16 - m.x75)**2 + (m.x95 - m.x154)**2 + (m.x174
    - m.x233)**2 >= 0.46785600000000005)
m.e1125 = Constraint(expr= (m.x16 - m.x76)**2 + (m.x95 - m.x155)**2 + (m.x174
    - m.x234)**2 >= 0.46785600000000005)
m.e1126 = Constraint(expr= (m.x16 - m.x77)**2 + (m.x95 - m.x156)**2 + (m.x174
    - m.x235)**2 >= 0.46785600000000005)
m.e1127 = Constraint(expr= (m.x16 - m.x78)**2 + (m.x95 - m.x157)**2 + (m.x174
    - m.x236)**2 >= 0.46785600000000005)
m.e1128 = Constraint(expr= (m.x16 - m.x79)**2 + (m.x95 - m.x158)**2 + (m.x174
    - m.x237)**2 >= 0.46785600000000005)
m.e1129 = Constraint(expr= (m.x17 - m.x18)**2 + (m.x96 - m.x97)**2 + (m.x175 -
    m.x176)**2 >= 0.46785600000000005)
m.e1130 = Constraint(expr= (m.x17 - m.x19)**2 + (m.x96 - m.x98)**2 + (m.x175 -
    m.x177)**2 >= 0.46785600000000005)
m.e1131 = Constraint(expr= (m.x17 - m.x20)**2 + (m.x96 - m.x99)**2 + (m.x175 -
    m.x178)**2 >= 0.46785600000000005)
m.e1132 = Constraint(expr= (m.x17 - m.x21)**2 + (m.x96 - m.x100)**2 + (m.x175
    - m.x179)**2 >= 0.46785600000000005)
m.e1133 = Constraint(expr= (m.x17 - m.x22)**2 + (m.x96 - m.x101)**2 + (m.x175
    - m.x180)**2 >= 0.46785600000000005)
m.e1134 = Constraint(expr= (m.x17 - m.x23)**2 + (m.x96 - m.x102)**2 + (m.x175
    - m.x181)**2 >= 0.46785600000000005)
m.e1135 = Constraint(expr= (m.x17 - m.x24)**2 + (m.x96 - m.x103)**2 + (m.x175
    - m.x182)**2 >= 0.46785600000000005)
m.e1136 = Constraint(expr= (m.x17 - m.x25)**2 + (m.x96 - m.x104)**2 + (m.x175
    - m.x183)**2 >= 0.46785600000000005)
m.e1137 = Constraint(expr= (m.x17 - m.x26)**2 + (m.x96 - m.x105)**2 + (m.x175
    - m.x184)**2 >= 0.46785600000000005)
m.e1138 = Constraint(expr= (m.x17 - m.x27)**2 + (m.x96 - m.x106)**2 + (m.x175
    - m.x185)**2 >= 0.46785600000000005)
m.e1139 = Constraint(expr= (m.x17 - m.x28)**2 + (m.x96 - m.x107)**2 + (m.x175
    - m.x186)**2 >= 0.46785600000000005)
m.e1140 = Constraint(expr= (m.x17 - m.x29)**2 + (m.x96 - m.x108)**2 + (m.x175
    - m.x187)**2 >= 0.46785600000000005)
m.e1141 = Constraint(expr= (m.x17 - m.x30)**2 + (m.x96 - m.x109)**2 + (m.x175
    - m.x188)**2 >= 0.46785600000000005)
m.e1142 = Constraint(expr= (m.x17 - m.x31)**2 + (m.x96 - m.x110)**2 + (m.x175
    - m.x189)**2 >= 0.46785600000000005)
m.e1143 = Constraint(expr= (m.x17 - m.x32)**2 + (m.x96 - m.x111)**2 + (m.x175
    - m.x190)**2 >= 0.46785600000000005)
m.e1144 = Constraint(expr= (m.x17 - m.x33)**2 + (m.x96 - m.x112)**2 + (m.x175
    - m.x191)**2 >= 0.46785600000000005)
m.e1145 = Constraint(expr= (m.x17 - m.x34)**2 + (m.x96 - m.x113)**2 + (m.x175
    - m.x192)**2 >= 0.46785600000000005)
m.e1146 = Constraint(expr= (m.x17 - m.x35)**2 + (m.x96 - m.x114)**2 + (m.x175
    - m.x193)**2 >= 0.46785600000000005)
m.e1147 = Constraint(expr= (m.x17 - m.x36)**2 + (m.x96 - m.x115)**2 + (m.x175
    - m.x194)**2 >= 0.46785600000000005)
m.e1148 = Constraint(expr= (m.x17 - m.x37)**2 + (m.x96 - m.x116)**2 + (m.x175
    - m.x195)**2 >= 0.46785600000000005)
m.e1149 = Constraint(expr= (m.x17 - m.x38)**2 + (m.x96 - m.x117)**2 + (m.x175
    - m.x196)**2 >= 0.46785600000000005)
m.e1150 = Constraint(expr= (m.x17 - m.x39)**2 + (m.x96 - m.x118)**2 + (m.x175
    - m.x197)**2 >= 0.46785600000000005)
m.e1151 = Constraint(expr= (m.x17 - m.x40)**2 + (m.x96 - m.x119)**2 + (m.x175
    - m.x198)**2 >= 0.46785600000000005)
m.e1152 = Constraint(expr= (m.x17 - m.x41)**2 + (m.x96 - m.x120)**2 + (m.x175
    - m.x199)**2 >= 0.46785600000000005)
m.e1153 = Constraint(expr= (m.x17 - m.x42)**2 + (m.x96 - m.x121)**2 + (m.x175
    - m.x200)**2 >= 0.46785600000000005)
m.e1154 = Constraint(expr= (m.x17 - m.x43)**2 + (m.x96 - m.x122)**2 + (m.x175
    - m.x201)**2 >= 0.46785600000000005)
m.e1155 = Constraint(expr= (m.x17 - m.x44)**2 + (m.x96 - m.x123)**2 + (m.x175
    - m.x202)**2 >= 0.46785600000000005)
m.e1156 = Constraint(expr= (m.x17 - m.x45)**2 + (m.x96 - m.x124)**2 + (m.x175
    - m.x203)**2 >= 0.46785600000000005)
m.e1157 = Constraint(expr= (m.x17 - m.x46)**2 + (m.x96 - m.x125)**2 + (m.x175
    - m.x204)**2 >= 0.46785600000000005)
m.e1158 = Constraint(expr= (m.x17 - m.x47)**2 + (m.x96 - m.x126)**2 + (m.x175
    - m.x205)**2 >= 0.46785600000000005)
m.e1159 = Constraint(expr= (m.x17 - m.x48)**2 + (m.x96 - m.x127)**2 + (m.x175
    - m.x206)**2 >= 0.46785600000000005)
m.e1160 = Constraint(expr= (m.x17 - m.x49)**2 + (m.x96 - m.x128)**2 + (m.x175
    - m.x207)**2 >= 0.46785600000000005)
m.e1161 = Constraint(expr= (m.x17 - m.x50)**2 + (m.x96 - m.x129)**2 + (m.x175
    - m.x208)**2 >= 0.46785600000000005)
m.e1162 = Constraint(expr= (m.x17 - m.x51)**2 + (m.x96 - m.x130)**2 + (m.x175
    - m.x209)**2 >= 0.46785600000000005)
m.e1163 = Constraint(expr= (m.x17 - m.x52)**2 + (m.x96 - m.x131)**2 + (m.x175
    - m.x210)**2 >= 0.46785600000000005)
m.e1164 = Constraint(expr= (m.x17 - m.x53)**2 + (m.x96 - m.x132)**2 + (m.x175
    - m.x211)**2 >= 0.46785600000000005)
m.e1165 = Constraint(expr= (m.x17 - m.x54)**2 + (m.x96 - m.x133)**2 + (m.x175
    - m.x212)**2 >= 0.46785600000000005)
m.e1166 = Constraint(expr= (m.x17 - m.x55)**2 + (m.x96 - m.x134)**2 + (m.x175
    - m.x213)**2 >= 0.46785600000000005)
m.e1167 = Constraint(expr= (m.x17 - m.x56)**2 + (m.x96 - m.x135)**2 + (m.x175
    - m.x214)**2 >= 0.46785600000000005)
m.e1168 = Constraint(expr= (m.x17 - m.x57)**2 + (m.x96 - m.x136)**2 + (m.x175
    - m.x215)**2 >= 0.46785600000000005)
m.e1169 = Constraint(expr= (m.x17 - m.x58)**2 + (m.x96 - m.x137)**2 + (m.x175
    - m.x216)**2 >= 0.46785600000000005)
m.e1170 = Constraint(expr= (m.x17 - m.x59)**2 + (m.x96 - m.x138)**2 + (m.x175
    - m.x217)**2 >= 0.46785600000000005)
m.e1171 = Constraint(expr= (m.x17 - m.x60)**2 + (m.x96 - m.x139)**2 + (m.x175
    - m.x218)**2 >= 0.46785600000000005)
m.e1172 = Constraint(expr= (m.x17 - m.x61)**2 + (m.x96 - m.x140)**2 + (m.x175
    - m.x219)**2 >= 0.46785600000000005)
m.e1173 = Constraint(expr= (m.x17 - m.x62)**2 + (m.x96 - m.x141)**2 + (m.x175
    - m.x220)**2 >= 0.46785600000000005)
m.e1174 = Constraint(expr= (m.x17 - m.x63)**2 + (m.x96 - m.x142)**2 + (m.x175
    - m.x221)**2 >= 0.46785600000000005)
m.e1175 = Constraint(expr= (m.x17 - m.x64)**2 + (m.x96 - m.x143)**2 + (m.x175
    - m.x222)**2 >= 0.46785600000000005)
m.e1176 = Constraint(expr= (m.x17 - m.x65)**2 + (m.x96 - m.x144)**2 + (m.x175
    - m.x223)**2 >= 0.46785600000000005)
m.e1177 = Constraint(expr= (m.x17 - m.x66)**2 + (m.x96 - m.x145)**2 + (m.x175
    - m.x224)**2 >= 0.46785600000000005)
m.e1178 = Constraint(expr= (m.x17 - m.x67)**2 + (m.x96 - m.x146)**2 + (m.x175
    - m.x225)**2 >= 0.46785600000000005)
m.e1179 = Constraint(expr= (m.x17 - m.x68)**2 + (m.x96 - m.x147)**2 + (m.x175
    - m.x226)**2 >= 0.46785600000000005)
m.e1180 = Constraint(expr= (m.x17 - m.x69)**2 + (m.x96 - m.x148)**2 + (m.x175
    - m.x227)**2 >= 0.46785600000000005)
m.e1181 = Constraint(expr= (m.x17 - m.x70)**2 + (m.x96 - m.x149)**2 + (m.x175
    - m.x228)**2 >= 0.46785600000000005)
m.e1182 = Constraint(expr= (m.x17 - m.x71)**2 + (m.x96 - m.x150)**2 + (m.x175
    - m.x229)**2 >= 0.46785600000000005)
m.e1183 = Constraint(expr= (m.x17 - m.x72)**2 + (m.x96 - m.x151)**2 + (m.x175
    - m.x230)**2 >= 0.46785600000000005)
m.e1184 = Constraint(expr= (m.x17 - m.x73)**2 + (m.x96 - m.x152)**2 + (m.x175
    - m.x231)**2 >= 0.46785600000000005)
m.e1185 = Constraint(expr= (m.x17 - m.x74)**2 + (m.x96 - m.x153)**2 + (m.x175
    - m.x232)**2 >= 0.46785600000000005)
m.e1186 = Constraint(expr= (m.x17 - m.x75)**2 + (m.x96 - m.x154)**2 + (m.x175
    - m.x233)**2 >= 0.46785600000000005)
m.e1187 = Constraint(expr= (m.x17 - m.x76)**2 + (m.x96 - m.x155)**2 + (m.x175
    - m.x234)**2 >= 0.46785600000000005)
m.e1188 = Constraint(expr= (m.x17 - m.x77)**2 + (m.x96 - m.x156)**2 + (m.x175
    - m.x235)**2 >= 0.46785600000000005)
m.e1189 = Constraint(expr= (m.x17 - m.x78)**2 + (m.x96 - m.x157)**2 + (m.x175
    - m.x236)**2 >= 0.46785600000000005)
m.e1190 = Constraint(expr= (m.x17 - m.x79)**2 + (m.x96 - m.x158)**2 + (m.x175
    - m.x237)**2 >= 0.46785600000000005)
m.e1191 = Constraint(expr= (m.x18 - m.x19)**2 + (m.x97 - m.x98)**2 + (m.x176 -
    m.x177)**2 >= 0.46785600000000005)
m.e1192 = Constraint(expr= (m.x18 - m.x20)**2 + (m.x97 - m.x99)**2 + (m.x176 -
    m.x178)**2 >= 0.46785600000000005)
m.e1193 = Constraint(expr= (m.x18 - m.x21)**2 + (m.x97 - m.x100)**2 + (m.x176
    - m.x179)**2 >= 0.46785600000000005)
m.e1194 = Constraint(expr= (m.x18 - m.x22)**2 + (m.x97 - m.x101)**2 + (m.x176
    - m.x180)**2 >= 0.46785600000000005)
m.e1195 = Constraint(expr= (m.x18 - m.x23)**2 + (m.x97 - m.x102)**2 + (m.x176
    - m.x181)**2 >= 0.46785600000000005)
m.e1196 = Constraint(expr= (m.x18 - m.x24)**2 + (m.x97 - m.x103)**2 + (m.x176
    - m.x182)**2 >= 0.46785600000000005)
m.e1197 = Constraint(expr= (m.x18 - m.x25)**2 + (m.x97 - m.x104)**2 + (m.x176
    - m.x183)**2 >= 0.46785600000000005)
m.e1198 = Constraint(expr= (m.x18 - m.x26)**2 + (m.x97 - m.x105)**2 + (m.x176
    - m.x184)**2 >= 0.46785600000000005)
m.e1199 = Constraint(expr= (m.x18 - m.x27)**2 + (m.x97 - m.x106)**2 + (m.x176
    - m.x185)**2 >= 0.46785600000000005)
m.e1200 = Constraint(expr= (m.x18 - m.x28)**2 + (m.x97 - m.x107)**2 + (m.x176
    - m.x186)**2 >= 0.46785600000000005)
m.e1201 = Constraint(expr= (m.x18 - m.x29)**2 + (m.x97 - m.x108)**2 + (m.x176
    - m.x187)**2 >= 0.46785600000000005)
m.e1202 = Constraint(expr= (m.x18 - m.x30)**2 + (m.x97 - m.x109)**2 + (m.x176
    - m.x188)**2 >= 0.46785600000000005)
m.e1203 = Constraint(expr= (m.x18 - m.x31)**2 + (m.x97 - m.x110)**2 + (m.x176
    - m.x189)**2 >= 0.46785600000000005)
m.e1204 = Constraint(expr= (m.x18 - m.x32)**2 + (m.x97 - m.x111)**2 + (m.x176
    - m.x190)**2 >= 0.46785600000000005)
m.e1205 = Constraint(expr= (m.x18 - m.x33)**2 + (m.x97 - m.x112)**2 + (m.x176
    - m.x191)**2 >= 0.46785600000000005)
m.e1206 = Constraint(expr= (m.x18 - m.x34)**2 + (m.x97 - m.x113)**2 + (m.x176
    - m.x192)**2 >= 0.46785600000000005)
m.e1207 = Constraint(expr= (m.x18 - m.x35)**2 + (m.x97 - m.x114)**2 + (m.x176
    - m.x193)**2 >= 0.46785600000000005)
m.e1208 = Constraint(expr= (m.x18 - m.x36)**2 + (m.x97 - m.x115)**2 + (m.x176
    - m.x194)**2 >= 0.46785600000000005)
m.e1209 = Constraint(expr= (m.x18 - m.x37)**2 + (m.x97 - m.x116)**2 + (m.x176
    - m.x195)**2 >= 0.46785600000000005)
m.e1210 = Constraint(expr= (m.x18 - m.x38)**2 + (m.x97 - m.x117)**2 + (m.x176
    - m.x196)**2 >= 0.46785600000000005)
m.e1211 = Constraint(expr= (m.x18 - m.x39)**2 + (m.x97 - m.x118)**2 + (m.x176
    - m.x197)**2 >= 0.46785600000000005)
m.e1212 = Constraint(expr= (m.x18 - m.x40)**2 + (m.x97 - m.x119)**2 + (m.x176
    - m.x198)**2 >= 0.46785600000000005)
m.e1213 = Constraint(expr= (m.x18 - m.x41)**2 + (m.x97 - m.x120)**2 + (m.x176
    - m.x199)**2 >= 0.46785600000000005)
m.e1214 = Constraint(expr= (m.x18 - m.x42)**2 + (m.x97 - m.x121)**2 + (m.x176
    - m.x200)**2 >= 0.46785600000000005)
m.e1215 = Constraint(expr= (m.x18 - m.x43)**2 + (m.x97 - m.x122)**2 + (m.x176
    - m.x201)**2 >= 0.46785600000000005)
m.e1216 = Constraint(expr= (m.x18 - m.x44)**2 + (m.x97 - m.x123)**2 + (m.x176
    - m.x202)**2 >= 0.46785600000000005)
m.e1217 = Constraint(expr= (m.x18 - m.x45)**2 + (m.x97 - m.x124)**2 + (m.x176
    - m.x203)**2 >= 0.46785600000000005)
m.e1218 = Constraint(expr= (m.x18 - m.x46)**2 + (m.x97 - m.x125)**2 + (m.x176
    - m.x204)**2 >= 0.46785600000000005)
m.e1219 = Constraint(expr= (m.x18 - m.x47)**2 + (m.x97 - m.x126)**2 + (m.x176
    - m.x205)**2 >= 0.46785600000000005)
m.e1220 = Constraint(expr= (m.x18 - m.x48)**2 + (m.x97 - m.x127)**2 + (m.x176
    - m.x206)**2 >= 0.46785600000000005)
m.e1221 = Constraint(expr= (m.x18 - m.x49)**2 + (m.x97 - m.x128)**2 + (m.x176
    - m.x207)**2 >= 0.46785600000000005)
m.e1222 = Constraint(expr= (m.x18 - m.x50)**2 + (m.x97 - m.x129)**2 + (m.x176
    - m.x208)**2 >= 0.46785600000000005)
m.e1223 = Constraint(expr= (m.x18 - m.x51)**2 + (m.x97 - m.x130)**2 + (m.x176
    - m.x209)**2 >= 0.46785600000000005)
m.e1224 = Constraint(expr= (m.x18 - m.x52)**2 + (m.x97 - m.x131)**2 + (m.x176
    - m.x210)**2 >= 0.46785600000000005)
m.e1225 = Constraint(expr= (m.x18 - m.x53)**2 + (m.x97 - m.x132)**2 + (m.x176
    - m.x211)**2 >= 0.46785600000000005)
m.e1226 = Constraint(expr= (m.x18 - m.x54)**2 + (m.x97 - m.x133)**2 + (m.x176
    - m.x212)**2 >= 0.46785600000000005)
m.e1227 = Constraint(expr= (m.x18 - m.x55)**2 + (m.x97 - m.x134)**2 + (m.x176
    - m.x213)**2 >= 0.46785600000000005)
m.e1228 = Constraint(expr= (m.x18 - m.x56)**2 + (m.x97 - m.x135)**2 + (m.x176
    - m.x214)**2 >= 0.46785600000000005)
m.e1229 = Constraint(expr= (m.x18 - m.x57)**2 + (m.x97 - m.x136)**2 + (m.x176
    - m.x215)**2 >= 0.46785600000000005)
m.e1230 = Constraint(expr= (m.x18 - m.x58)**2 + (m.x97 - m.x137)**2 + (m.x176
    - m.x216)**2 >= 0.46785600000000005)
m.e1231 = Constraint(expr= (m.x18 - m.x59)**2 + (m.x97 - m.x138)**2 + (m.x176
    - m.x217)**2 >= 0.46785600000000005)
m.e1232 = Constraint(expr= (m.x18 - m.x60)**2 + (m.x97 - m.x139)**2 + (m.x176
    - m.x218)**2 >= 0.46785600000000005)
m.e1233 = Constraint(expr= (m.x18 - m.x61)**2 + (m.x97 - m.x140)**2 + (m.x176
    - m.x219)**2 >= 0.46785600000000005)
m.e1234 = Constraint(expr= (m.x18 - m.x62)**2 + (m.x97 - m.x141)**2 + (m.x176
    - m.x220)**2 >= 0.46785600000000005)
m.e1235 = Constraint(expr= (m.x18 - m.x63)**2 + (m.x97 - m.x142)**2 + (m.x176
    - m.x221)**2 >= 0.46785600000000005)
m.e1236 = Constraint(expr= (m.x18 - m.x64)**2 + (m.x97 - m.x143)**2 + (m.x176
    - m.x222)**2 >= 0.46785600000000005)
m.e1237 = Constraint(expr= (m.x18 - m.x65)**2 + (m.x97 - m.x144)**2 + (m.x176
    - m.x223)**2 >= 0.46785600000000005)
m.e1238 = Constraint(expr= (m.x18 - m.x66)**2 + (m.x97 - m.x145)**2 + (m.x176
    - m.x224)**2 >= 0.46785600000000005)
m.e1239 = Constraint(expr= (m.x18 - m.x67)**2 + (m.x97 - m.x146)**2 + (m.x176
    - m.x225)**2 >= 0.46785600000000005)
m.e1240 = Constraint(expr= (m.x18 - m.x68)**2 + (m.x97 - m.x147)**2 + (m.x176
    - m.x226)**2 >= 0.46785600000000005)
m.e1241 = Constraint(expr= (m.x18 - m.x69)**2 + (m.x97 - m.x148)**2 + (m.x176
    - m.x227)**2 >= 0.46785600000000005)
m.e1242 = Constraint(expr= (m.x18 - m.x70)**2 + (m.x97 - m.x149)**2 + (m.x176
    - m.x228)**2 >= 0.46785600000000005)
m.e1243 = Constraint(expr= (m.x18 - m.x71)**2 + (m.x97 - m.x150)**2 + (m.x176
    - m.x229)**2 >= 0.46785600000000005)
m.e1244 = Constraint(expr= (m.x18 - m.x72)**2 + (m.x97 - m.x151)**2 + (m.x176
    - m.x230)**2 >= 0.46785600000000005)
m.e1245 = Constraint(expr= (m.x18 - m.x73)**2 + (m.x97 - m.x152)**2 + (m.x176
    - m.x231)**2 >= 0.46785600000000005)
m.e1246 = Constraint(expr= (m.x18 - m.x74)**2 + (m.x97 - m.x153)**2 + (m.x176
    - m.x232)**2 >= 0.46785600000000005)
m.e1247 = Constraint(expr= (m.x18 - m.x75)**2 + (m.x97 - m.x154)**2 + (m.x176
    - m.x233)**2 >= 0.46785600000000005)
m.e1248 = Constraint(expr= (m.x18 - m.x76)**2 + (m.x97 - m.x155)**2 + (m.x176
    - m.x234)**2 >= 0.46785600000000005)
m.e1249 = Constraint(expr= (m.x18 - m.x77)**2 + (m.x97 - m.x156)**2 + (m.x176
    - m.x235)**2 >= 0.46785600000000005)
m.e1250 = Constraint(expr= (m.x18 - m.x78)**2 + (m.x97 - m.x157)**2 + (m.x176
    - m.x236)**2 >= 0.46785600000000005)
m.e1251 = Constraint(expr= (m.x18 - m.x79)**2 + (m.x97 - m.x158)**2 + (m.x176
    - m.x237)**2 >= 0.46785600000000005)
m.e1252 = Constraint(expr= (m.x19 - m.x20)**2 + (m.x98 - m.x99)**2 + (m.x177 -
    m.x178)**2 >= 0.46785600000000005)
m.e1253 = Constraint(expr= (m.x19 - m.x21)**2 + (m.x98 - m.x100)**2 + (m.x177
    - m.x179)**2 >= 0.46785600000000005)
m.e1254 = Constraint(expr= (m.x19 - m.x22)**2 + (m.x98 - m.x101)**2 + (m.x177
    - m.x180)**2 >= 0.46785600000000005)
m.e1255 = Constraint(expr= (m.x19 - m.x23)**2 + (m.x98 - m.x102)**2 + (m.x177
    - m.x181)**2 >= 0.46785600000000005)
m.e1256 = Constraint(expr= (m.x19 - m.x24)**2 + (m.x98 - m.x103)**2 + (m.x177
    - m.x182)**2 >= 0.46785600000000005)
m.e1257 = Constraint(expr= (m.x19 - m.x25)**2 + (m.x98 - m.x104)**2 + (m.x177
    - m.x183)**2 >= 0.46785600000000005)
m.e1258 = Constraint(expr= (m.x19 - m.x26)**2 + (m.x98 - m.x105)**2 + (m.x177
    - m.x184)**2 >= 0.46785600000000005)
m.e1259 = Constraint(expr= (m.x19 - m.x27)**2 + (m.x98 - m.x106)**2 + (m.x177
    - m.x185)**2 >= 0.46785600000000005)
m.e1260 = Constraint(expr= (m.x19 - m.x28)**2 + (m.x98 - m.x107)**2 + (m.x177
    - m.x186)**2 >= 0.46785600000000005)
m.e1261 = Constraint(expr= (m.x19 - m.x29)**2 + (m.x98 - m.x108)**2 + (m.x177
    - m.x187)**2 >= 0.46785600000000005)
m.e1262 = Constraint(expr= (m.x19 - m.x30)**2 + (m.x98 - m.x109)**2 + (m.x177
    - m.x188)**2 >= 0.46785600000000005)
m.e1263 = Constraint(expr= (m.x19 - m.x31)**2 + (m.x98 - m.x110)**2 + (m.x177
    - m.x189)**2 >= 0.46785600000000005)
m.e1264 = Constraint(expr= (m.x19 - m.x32)**2 + (m.x98 - m.x111)**2 + (m.x177
    - m.x190)**2 >= 0.46785600000000005)
m.e1265 = Constraint(expr= (m.x19 - m.x33)**2 + (m.x98 - m.x112)**2 + (m.x177
    - m.x191)**2 >= 0.46785600000000005)
m.e1266 = Constraint(expr= (m.x19 - m.x34)**2 + (m.x98 - m.x113)**2 + (m.x177
    - m.x192)**2 >= 0.46785600000000005)
m.e1267 = Constraint(expr= (m.x19 - m.x35)**2 + (m.x98 - m.x114)**2 + (m.x177
    - m.x193)**2 >= 0.46785600000000005)
m.e1268 = Constraint(expr= (m.x19 - m.x36)**2 + (m.x98 - m.x115)**2 + (m.x177
    - m.x194)**2 >= 0.46785600000000005)
m.e1269 = Constraint(expr= (m.x19 - m.x37)**2 + (m.x98 - m.x116)**2 + (m.x177
    - m.x195)**2 >= 0.46785600000000005)
m.e1270 = Constraint(expr= (m.x19 - m.x38)**2 + (m.x98 - m.x117)**2 + (m.x177
    - m.x196)**2 >= 0.46785600000000005)
m.e1271 = Constraint(expr= (m.x19 - m.x39)**2 + (m.x98 - m.x118)**2 + (m.x177
    - m.x197)**2 >= 0.46785600000000005)
m.e1272 = Constraint(expr= (m.x19 - m.x40)**2 + (m.x98 - m.x119)**2 + (m.x177
    - m.x198)**2 >= 0.46785600000000005)
m.e1273 = Constraint(expr= (m.x19 - m.x41)**2 + (m.x98 - m.x120)**2 + (m.x177
    - m.x199)**2 >= 0.46785600000000005)
m.e1274 = Constraint(expr= (m.x19 - m.x42)**2 + (m.x98 - m.x121)**2 + (m.x177
    - m.x200)**2 >= 0.46785600000000005)
m.e1275 = Constraint(expr= (m.x19 - m.x43)**2 + (m.x98 - m.x122)**2 + (m.x177
    - m.x201)**2 >= 0.46785600000000005)
m.e1276 = Constraint(expr= (m.x19 - m.x44)**2 + (m.x98 - m.x123)**2 + (m.x177
    - m.x202)**2 >= 0.46785600000000005)
m.e1277 = Constraint(expr= (m.x19 - m.x45)**2 + (m.x98 - m.x124)**2 + (m.x177
    - m.x203)**2 >= 0.46785600000000005)
m.e1278 = Constraint(expr= (m.x19 - m.x46)**2 + (m.x98 - m.x125)**2 + (m.x177
    - m.x204)**2 >= 0.46785600000000005)
m.e1279 = Constraint(expr= (m.x19 - m.x47)**2 + (m.x98 - m.x126)**2 + (m.x177
    - m.x205)**2 >= 0.46785600000000005)
m.e1280 = Constraint(expr= (m.x19 - m.x48)**2 + (m.x98 - m.x127)**2 + (m.x177
    - m.x206)**2 >= 0.46785600000000005)
m.e1281 = Constraint(expr= (m.x19 - m.x49)**2 + (m.x98 - m.x128)**2 + (m.x177
    - m.x207)**2 >= 0.46785600000000005)
m.e1282 = Constraint(expr= (m.x19 - m.x50)**2 + (m.x98 - m.x129)**2 + (m.x177
    - m.x208)**2 >= 0.46785600000000005)
m.e1283 = Constraint(expr= (m.x19 - m.x51)**2 + (m.x98 - m.x130)**2 + (m.x177
    - m.x209)**2 >= 0.46785600000000005)
m.e1284 = Constraint(expr= (m.x19 - m.x52)**2 + (m.x98 - m.x131)**2 + (m.x177
    - m.x210)**2 >= 0.46785600000000005)
m.e1285 = Constraint(expr= (m.x19 - m.x53)**2 + (m.x98 - m.x132)**2 + (m.x177
    - m.x211)**2 >= 0.46785600000000005)
m.e1286 = Constraint(expr= (m.x19 - m.x54)**2 + (m.x98 - m.x133)**2 + (m.x177
    - m.x212)**2 >= 0.46785600000000005)
m.e1287 = Constraint(expr= (m.x19 - m.x55)**2 + (m.x98 - m.x134)**2 + (m.x177
    - m.x213)**2 >= 0.46785600000000005)
m.e1288 = Constraint(expr= (m.x19 - m.x56)**2 + (m.x98 - m.x135)**2 + (m.x177
    - m.x214)**2 >= 0.46785600000000005)
m.e1289 = Constraint(expr= (m.x19 - m.x57)**2 + (m.x98 - m.x136)**2 + (m.x177
    - m.x215)**2 >= 0.46785600000000005)
m.e1290 = Constraint(expr= (m.x19 - m.x58)**2 + (m.x98 - m.x137)**2 + (m.x177
    - m.x216)**2 >= 0.46785600000000005)
m.e1291 = Constraint(expr= (m.x19 - m.x59)**2 + (m.x98 - m.x138)**2 + (m.x177
    - m.x217)**2 >= 0.46785600000000005)
m.e1292 = Constraint(expr= (m.x19 - m.x60)**2 + (m.x98 - m.x139)**2 + (m.x177
    - m.x218)**2 >= 0.46785600000000005)
m.e1293 = Constraint(expr= (m.x19 - m.x61)**2 + (m.x98 - m.x140)**2 + (m.x177
    - m.x219)**2 >= 0.46785600000000005)
m.e1294 = Constraint(expr= (m.x19 - m.x62)**2 + (m.x98 - m.x141)**2 + (m.x177
    - m.x220)**2 >= 0.46785600000000005)
m.e1295 = Constraint(expr= (m.x19 - m.x63)**2 + (m.x98 - m.x142)**2 + (m.x177
    - m.x221)**2 >= 0.46785600000000005)
m.e1296 = Constraint(expr= (m.x19 - m.x64)**2 + (m.x98 - m.x143)**2 + (m.x177
    - m.x222)**2 >= 0.46785600000000005)
m.e1297 = Constraint(expr= (m.x19 - m.x65)**2 + (m.x98 - m.x144)**2 + (m.x177
    - m.x223)**2 >= 0.46785600000000005)
m.e1298 = Constraint(expr= (m.x19 - m.x66)**2 + (m.x98 - m.x145)**2 + (m.x177
    - m.x224)**2 >= 0.46785600000000005)
m.e1299 = Constraint(expr= (m.x19 - m.x67)**2 + (m.x98 - m.x146)**2 + (m.x177
    - m.x225)**2 >= 0.46785600000000005)
m.e1300 = Constraint(expr= (m.x19 - m.x68)**2 + (m.x98 - m.x147)**2 + (m.x177
    - m.x226)**2 >= 0.46785600000000005)
m.e1301 = Constraint(expr= (m.x19 - m.x69)**2 + (m.x98 - m.x148)**2 + (m.x177
    - m.x227)**2 >= 0.46785600000000005)
m.e1302 = Constraint(expr= (m.x19 - m.x70)**2 + (m.x98 - m.x149)**2 + (m.x177
    - m.x228)**2 >= 0.46785600000000005)
m.e1303 = Constraint(expr= (m.x19 - m.x71)**2 + (m.x98 - m.x150)**2 + (m.x177
    - m.x229)**2 >= 0.46785600000000005)
m.e1304 = Constraint(expr= (m.x19 - m.x72)**2 + (m.x98 - m.x151)**2 + (m.x177
    - m.x230)**2 >= 0.46785600000000005)
m.e1305 = Constraint(expr= (m.x19 - m.x73)**2 + (m.x98 - m.x152)**2 + (m.x177
    - m.x231)**2 >= 0.46785600000000005)
m.e1306 = Constraint(expr= (m.x19 - m.x74)**2 + (m.x98 - m.x153)**2 + (m.x177
    - m.x232)**2 >= 0.46785600000000005)
m.e1307 = Constraint(expr= (m.x19 - m.x75)**2 + (m.x98 - m.x154)**2 + (m.x177
    - m.x233)**2 >= 0.46785600000000005)
m.e1308 = Constraint(expr= (m.x19 - m.x76)**2 + (m.x98 - m.x155)**2 + (m.x177
    - m.x234)**2 >= 0.46785600000000005)
m.e1309 = Constraint(expr= (m.x19 - m.x77)**2 + (m.x98 - m.x156)**2 + (m.x177
    - m.x235)**2 >= 0.46785600000000005)
m.e1310 = Constraint(expr= (m.x19 - m.x78)**2 + (m.x98 - m.x157)**2 + (m.x177
    - m.x236)**2 >= 0.46785600000000005)
m.e1311 = Constraint(expr= (m.x19 - m.x79)**2 + (m.x98 - m.x158)**2 + (m.x177
    - m.x237)**2 >= 0.46785600000000005)
m.e1312 = Constraint(expr= (m.x20 - m.x21)**2 + (m.x99 - m.x100)**2 + (m.x178
    - m.x179)**2 >= 0.46785600000000005)
m.e1313 = Constraint(expr= (m.x20 - m.x22)**2 + (m.x99 - m.x101)**2 + (m.x178
    - m.x180)**2 >= 0.46785600000000005)
m.e1314 = Constraint(expr= (m.x20 - m.x23)**2 + (m.x99 - m.x102)**2 + (m.x178
    - m.x181)**2 >= 0.46785600000000005)
m.e1315 = Constraint(expr= (m.x20 - m.x24)**2 + (m.x99 - m.x103)**2 + (m.x178
    - m.x182)**2 >= 0.46785600000000005)
m.e1316 = Constraint(expr= (m.x20 - m.x25)**2 + (m.x99 - m.x104)**2 + (m.x178
    - m.x183)**2 >= 0.46785600000000005)
m.e1317 = Constraint(expr= (m.x20 - m.x26)**2 + (m.x99 - m.x105)**2 + (m.x178
    - m.x184)**2 >= 0.46785600000000005)
m.e1318 = Constraint(expr= (m.x20 - m.x27)**2 + (m.x99 - m.x106)**2 + (m.x178
    - m.x185)**2 >= 0.46785600000000005)
m.e1319 = Constraint(expr= (m.x20 - m.x28)**2 + (m.x99 - m.x107)**2 + (m.x178
    - m.x186)**2 >= 0.46785600000000005)
m.e1320 = Constraint(expr= (m.x20 - m.x29)**2 + (m.x99 - m.x108)**2 + (m.x178
    - m.x187)**2 >= 0.46785600000000005)
m.e1321 = Constraint(expr= (m.x20 - m.x30)**2 + (m.x99 - m.x109)**2 + (m.x178
    - m.x188)**2 >= 0.46785600000000005)
m.e1322 = Constraint(expr= (m.x20 - m.x31)**2 + (m.x99 - m.x110)**2 + (m.x178
    - m.x189)**2 >= 0.46785600000000005)
m.e1323 = Constraint(expr= (m.x20 - m.x32)**2 + (m.x99 - m.x111)**2 + (m.x178
    - m.x190)**2 >= 0.46785600000000005)
m.e1324 = Constraint(expr= (m.x20 - m.x33)**2 + (m.x99 - m.x112)**2 + (m.x178
    - m.x191)**2 >= 0.46785600000000005)
m.e1325 = Constraint(expr= (m.x20 - m.x34)**2 + (m.x99 - m.x113)**2 + (m.x178
    - m.x192)**2 >= 0.46785600000000005)
m.e1326 = Constraint(expr= (m.x20 - m.x35)**2 + (m.x99 - m.x114)**2 + (m.x178
    - m.x193)**2 >= 0.46785600000000005)
m.e1327 = Constraint(expr= (m.x20 - m.x36)**2 + (m.x99 - m.x115)**2 + (m.x178
    - m.x194)**2 >= 0.46785600000000005)
m.e1328 = Constraint(expr= (m.x20 - m.x37)**2 + (m.x99 - m.x116)**2 + (m.x178
    - m.x195)**2 >= 0.46785600000000005)
m.e1329 = Constraint(expr= (m.x20 - m.x38)**2 + (m.x99 - m.x117)**2 + (m.x178
    - m.x196)**2 >= 0.46785600000000005)
m.e1330 = Constraint(expr= (m.x20 - m.x39)**2 + (m.x99 - m.x118)**2 + (m.x178
    - m.x197)**2 >= 0.46785600000000005)
m.e1331 = Constraint(expr= (m.x20 - m.x40)**2 + (m.x99 - m.x119)**2 + (m.x178
    - m.x198)**2 >= 0.46785600000000005)
m.e1332 = Constraint(expr= (m.x20 - m.x41)**2 + (m.x99 - m.x120)**2 + (m.x178
    - m.x199)**2 >= 0.46785600000000005)
m.e1333 = Constraint(expr= (m.x20 - m.x42)**2 + (m.x99 - m.x121)**2 + (m.x178
    - m.x200)**2 >= 0.46785600000000005)
m.e1334 = Constraint(expr= (m.x20 - m.x43)**2 + (m.x99 - m.x122)**2 + (m.x178
    - m.x201)**2 >= 0.46785600000000005)
m.e1335 = Constraint(expr= (m.x20 - m.x44)**2 + (m.x99 - m.x123)**2 + (m.x178
    - m.x202)**2 >= 0.46785600000000005)
m.e1336 = Constraint(expr= (m.x20 - m.x45)**2 + (m.x99 - m.x124)**2 + (m.x178
    - m.x203)**2 >= 0.46785600000000005)
m.e1337 = Constraint(expr= (m.x20 - m.x46)**2 + (m.x99 - m.x125)**2 + (m.x178
    - m.x204)**2 >= 0.46785600000000005)
m.e1338 = Constraint(expr= (m.x20 - m.x47)**2 + (m.x99 - m.x126)**2 + (m.x178
    - m.x205)**2 >= 0.46785600000000005)
m.e1339 = Constraint(expr= (m.x20 - m.x48)**2 + (m.x99 - m.x127)**2 + (m.x178
    - m.x206)**2 >= 0.46785600000000005)
m.e1340 = Constraint(expr= (m.x20 - m.x49)**2 + (m.x99 - m.x128)**2 + (m.x178
    - m.x207)**2 >= 0.46785600000000005)
m.e1341 = Constraint(expr= (m.x20 - m.x50)**2 + (m.x99 - m.x129)**2 + (m.x178
    - m.x208)**2 >= 0.46785600000000005)
m.e1342 = Constraint(expr= (m.x20 - m.x51)**2 + (m.x99 - m.x130)**2 + (m.x178
    - m.x209)**2 >= 0.46785600000000005)
m.e1343 = Constraint(expr= (m.x20 - m.x52)**2 + (m.x99 - m.x131)**2 + (m.x178
    - m.x210)**2 >= 0.46785600000000005)
m.e1344 = Constraint(expr= (m.x20 - m.x53)**2 + (m.x99 - m.x132)**2 + (m.x178
    - m.x211)**2 >= 0.46785600000000005)
m.e1345 = Constraint(expr= (m.x20 - m.x54)**2 + (m.x99 - m.x133)**2 + (m.x178
    - m.x212)**2 >= 0.46785600000000005)
m.e1346 = Constraint(expr= (m.x20 - m.x55)**2 + (m.x99 - m.x134)**2 + (m.x178
    - m.x213)**2 >= 0.46785600000000005)
m.e1347 = Constraint(expr= (m.x20 - m.x56)**2 + (m.x99 - m.x135)**2 + (m.x178
    - m.x214)**2 >= 0.46785600000000005)
m.e1348 = Constraint(expr= (m.x20 - m.x57)**2 + (m.x99 - m.x136)**2 + (m.x178
    - m.x215)**2 >= 0.46785600000000005)
m.e1349 = Constraint(expr= (m.x20 - m.x58)**2 + (m.x99 - m.x137)**2 + (m.x178
    - m.x216)**2 >= 0.46785600000000005)
m.e1350 = Constraint(expr= (m.x20 - m.x59)**2 + (m.x99 - m.x138)**2 + (m.x178
    - m.x217)**2 >= 0.46785600000000005)
m.e1351 = Constraint(expr= (m.x20 - m.x60)**2 + (m.x99 - m.x139)**2 + (m.x178
    - m.x218)**2 >= 0.46785600000000005)
m.e1352 = Constraint(expr= (m.x20 - m.x61)**2 + (m.x99 - m.x140)**2 + (m.x178
    - m.x219)**2 >= 0.46785600000000005)
m.e1353 = Constraint(expr= (m.x20 - m.x62)**2 + (m.x99 - m.x141)**2 + (m.x178
    - m.x220)**2 >= 0.46785600000000005)
m.e1354 = Constraint(expr= (m.x20 - m.x63)**2 + (m.x99 - m.x142)**2 + (m.x178
    - m.x221)**2 >= 0.46785600000000005)
m.e1355 = Constraint(expr= (m.x20 - m.x64)**2 + (m.x99 - m.x143)**2 + (m.x178
    - m.x222)**2 >= 0.46785600000000005)
m.e1356 = Constraint(expr= (m.x20 - m.x65)**2 + (m.x99 - m.x144)**2 + (m.x178
    - m.x223)**2 >= 0.46785600000000005)
m.e1357 = Constraint(expr= (m.x20 - m.x66)**2 + (m.x99 - m.x145)**2 + (m.x178
    - m.x224)**2 >= 0.46785600000000005)
m.e1358 = Constraint(expr= (m.x20 - m.x67)**2 + (m.x99 - m.x146)**2 + (m.x178
    - m.x225)**2 >= 0.46785600000000005)
m.e1359 = Constraint(expr= (m.x20 - m.x68)**2 + (m.x99 - m.x147)**2 + (m.x178
    - m.x226)**2 >= 0.46785600000000005)
m.e1360 = Constraint(expr= (m.x20 - m.x69)**2 + (m.x99 - m.x148)**2 + (m.x178
    - m.x227)**2 >= 0.46785600000000005)
m.e1361 = Constraint(expr= (m.x20 - m.x70)**2 + (m.x99 - m.x149)**2 + (m.x178
    - m.x228)**2 >= 0.46785600000000005)
m.e1362 = Constraint(expr= (m.x20 - m.x71)**2 + (m.x99 - m.x150)**2 + (m.x178
    - m.x229)**2 >= 0.46785600000000005)
m.e1363 = Constraint(expr= (m.x20 - m.x72)**2 + (m.x99 - m.x151)**2 + (m.x178
    - m.x230)**2 >= 0.46785600000000005)
m.e1364 = Constraint(expr= (m.x20 - m.x73)**2 + (m.x99 - m.x152)**2 + (m.x178
    - m.x231)**2 >= 0.46785600000000005)
m.e1365 = Constraint(expr= (m.x20 - m.x74)**2 + (m.x99 - m.x153)**2 + (m.x178
    - m.x232)**2 >= 0.46785600000000005)
m.e1366 = Constraint(expr= (m.x20 - m.x75)**2 + (m.x99 - m.x154)**2 + (m.x178
    - m.x233)**2 >= 0.46785600000000005)
m.e1367 = Constraint(expr= (m.x20 - m.x76)**2 + (m.x99 - m.x155)**2 + (m.x178
    - m.x234)**2 >= 0.46785600000000005)
m.e1368 = Constraint(expr= (m.x20 - m.x77)**2 + (m.x99 - m.x156)**2 + (m.x178
    - m.x235)**2 >= 0.46785600000000005)
m.e1369 = Constraint(expr= (m.x20 - m.x78)**2 + (m.x99 - m.x157)**2 + (m.x178
    - m.x236)**2 >= 0.46785600000000005)
m.e1370 = Constraint(expr= (m.x20 - m.x79)**2 + (m.x99 - m.x158)**2 + (m.x178
    - m.x237)**2 >= 0.46785600000000005)
m.e1371 = Constraint(expr= (m.x21 - m.x22)**2 + (m.x100 - m.x101)**2 + (m.x179
    - m.x180)**2 >= 0.46785600000000005)
m.e1372 = Constraint(expr= (m.x21 - m.x23)**2 + (m.x100 - m.x102)**2 + (m.x179
    - m.x181)**2 >= 0.46785600000000005)
m.e1373 = Constraint(expr= (m.x21 - m.x24)**2 + (m.x100 - m.x103)**2 + (m.x179
    - m.x182)**2 >= 0.46785600000000005)
m.e1374 = Constraint(expr= (m.x21 - m.x25)**2 + (m.x100 - m.x104)**2 + (m.x179
    - m.x183)**2 >= 0.46785600000000005)
m.e1375 = Constraint(expr= (m.x21 - m.x26)**2 + (m.x100 - m.x105)**2 + (m.x179
    - m.x184)**2 >= 0.46785600000000005)
m.e1376 = Constraint(expr= (m.x21 - m.x27)**2 + (m.x100 - m.x106)**2 + (m.x179
    - m.x185)**2 >= 0.46785600000000005)
m.e1377 = Constraint(expr= (m.x21 - m.x28)**2 + (m.x100 - m.x107)**2 + (m.x179
    - m.x186)**2 >= 0.46785600000000005)
m.e1378 = Constraint(expr= (m.x21 - m.x29)**2 + (m.x100 - m.x108)**2 + (m.x179
    - m.x187)**2 >= 0.46785600000000005)
m.e1379 = Constraint(expr= (m.x21 - m.x30)**2 + (m.x100 - m.x109)**2 + (m.x179
    - m.x188)**2 >= 0.46785600000000005)
m.e1380 = Constraint(expr= (m.x21 - m.x31)**2 + (m.x100 - m.x110)**2 + (m.x179
    - m.x189)**2 >= 0.46785600000000005)
m.e1381 = Constraint(expr= (m.x21 - m.x32)**2 + (m.x100 - m.x111)**2 + (m.x179
    - m.x190)**2 >= 0.46785600000000005)
m.e1382 = Constraint(expr= (m.x21 - m.x33)**2 + (m.x100 - m.x112)**2 + (m.x179
    - m.x191)**2 >= 0.46785600000000005)
m.e1383 = Constraint(expr= (m.x21 - m.x34)**2 + (m.x100 - m.x113)**2 + (m.x179
    - m.x192)**2 >= 0.46785600000000005)
m.e1384 = Constraint(expr= (m.x21 - m.x35)**2 + (m.x100 - m.x114)**2 + (m.x179
    - m.x193)**2 >= 0.46785600000000005)
m.e1385 = Constraint(expr= (m.x21 - m.x36)**2 + (m.x100 - m.x115)**2 + (m.x179
    - m.x194)**2 >= 0.46785600000000005)
m.e1386 = Constraint(expr= (m.x21 - m.x37)**2 + (m.x100 - m.x116)**2 + (m.x179
    - m.x195)**2 >= 0.46785600000000005)
m.e1387 = Constraint(expr= (m.x21 - m.x38)**2 + (m.x100 - m.x117)**2 + (m.x179
    - m.x196)**2 >= 0.46785600000000005)
m.e1388 = Constraint(expr= (m.x21 - m.x39)**2 + (m.x100 - m.x118)**2 + (m.x179
    - m.x197)**2 >= 0.46785600000000005)
m.e1389 = Constraint(expr= (m.x21 - m.x40)**2 + (m.x100 - m.x119)**2 + (m.x179
    - m.x198)**2 >= 0.46785600000000005)
m.e1390 = Constraint(expr= (m.x21 - m.x41)**2 + (m.x100 - m.x120)**2 + (m.x179
    - m.x199)**2 >= 0.46785600000000005)
m.e1391 = Constraint(expr= (m.x21 - m.x42)**2 + (m.x100 - m.x121)**2 + (m.x179
    - m.x200)**2 >= 0.46785600000000005)
m.e1392 = Constraint(expr= (m.x21 - m.x43)**2 + (m.x100 - m.x122)**2 + (m.x179
    - m.x201)**2 >= 0.46785600000000005)
m.e1393 = Constraint(expr= (m.x21 - m.x44)**2 + (m.x100 - m.x123)**2 + (m.x179
    - m.x202)**2 >= 0.46785600000000005)
m.e1394 = Constraint(expr= (m.x21 - m.x45)**2 + (m.x100 - m.x124)**2 + (m.x179
    - m.x203)**2 >= 0.46785600000000005)
m.e1395 = Constraint(expr= (m.x21 - m.x46)**2 + (m.x100 - m.x125)**2 + (m.x179
    - m.x204)**2 >= 0.46785600000000005)
m.e1396 = Constraint(expr= (m.x21 - m.x47)**2 + (m.x100 - m.x126)**2 + (m.x179
    - m.x205)**2 >= 0.46785600000000005)
m.e1397 = Constraint(expr= (m.x21 - m.x48)**2 + (m.x100 - m.x127)**2 + (m.x179
    - m.x206)**2 >= 0.46785600000000005)
m.e1398 = Constraint(expr= (m.x21 - m.x49)**2 + (m.x100 - m.x128)**2 + (m.x179
    - m.x207)**2 >= 0.46785600000000005)
m.e1399 = Constraint(expr= (m.x21 - m.x50)**2 + (m.x100 - m.x129)**2 + (m.x179
    - m.x208)**2 >= 0.46785600000000005)
m.e1400 = Constraint(expr= (m.x21 - m.x51)**2 + (m.x100 - m.x130)**2 + (m.x179
    - m.x209)**2 >= 0.46785600000000005)
m.e1401 = Constraint(expr= (m.x21 - m.x52)**2 + (m.x100 - m.x131)**2 + (m.x179
    - m.x210)**2 >= 0.46785600000000005)
m.e1402 = Constraint(expr= (m.x21 - m.x53)**2 + (m.x100 - m.x132)**2 + (m.x179
    - m.x211)**2 >= 0.46785600000000005)
m.e1403 = Constraint(expr= (m.x21 - m.x54)**2 + (m.x100 - m.x133)**2 + (m.x179
    - m.x212)**2 >= 0.46785600000000005)
m.e1404 = Constraint(expr= (m.x21 - m.x55)**2 + (m.x100 - m.x134)**2 + (m.x179
    - m.x213)**2 >= 0.46785600000000005)
m.e1405 = Constraint(expr= (m.x21 - m.x56)**2 + (m.x100 - m.x135)**2 + (m.x179
    - m.x214)**2 >= 0.46785600000000005)
m.e1406 = Constraint(expr= (m.x21 - m.x57)**2 + (m.x100 - m.x136)**2 + (m.x179
    - m.x215)**2 >= 0.46785600000000005)
m.e1407 = Constraint(expr= (m.x21 - m.x58)**2 + (m.x100 - m.x137)**2 + (m.x179
    - m.x216)**2 >= 0.46785600000000005)
m.e1408 = Constraint(expr= (m.x21 - m.x59)**2 + (m.x100 - m.x138)**2 + (m.x179
    - m.x217)**2 >= 0.46785600000000005)
m.e1409 = Constraint(expr= (m.x21 - m.x60)**2 + (m.x100 - m.x139)**2 + (m.x179
    - m.x218)**2 >= 0.46785600000000005)
m.e1410 = Constraint(expr= (m.x21 - m.x61)**2 + (m.x100 - m.x140)**2 + (m.x179
    - m.x219)**2 >= 0.46785600000000005)
m.e1411 = Constraint(expr= (m.x21 - m.x62)**2 + (m.x100 - m.x141)**2 + (m.x179
    - m.x220)**2 >= 0.46785600000000005)
m.e1412 = Constraint(expr= (m.x21 - m.x63)**2 + (m.x100 - m.x142)**2 + (m.x179
    - m.x221)**2 >= 0.46785600000000005)
m.e1413 = Constraint(expr= (m.x21 - m.x64)**2 + (m.x100 - m.x143)**2 + (m.x179
    - m.x222)**2 >= 0.46785600000000005)
m.e1414 = Constraint(expr= (m.x21 - m.x65)**2 + (m.x100 - m.x144)**2 + (m.x179
    - m.x223)**2 >= 0.46785600000000005)
m.e1415 = Constraint(expr= (m.x21 - m.x66)**2 + (m.x100 - m.x145)**2 + (m.x179
    - m.x224)**2 >= 0.46785600000000005)
m.e1416 = Constraint(expr= (m.x21 - m.x67)**2 + (m.x100 - m.x146)**2 + (m.x179
    - m.x225)**2 >= 0.46785600000000005)
m.e1417 = Constraint(expr= (m.x21 - m.x68)**2 + (m.x100 - m.x147)**2 + (m.x179
    - m.x226)**2 >= 0.46785600000000005)
m.e1418 = Constraint(expr= (m.x21 - m.x69)**2 + (m.x100 - m.x148)**2 + (m.x179
    - m.x227)**2 >= 0.46785600000000005)
m.e1419 = Constraint(expr= (m.x21 - m.x70)**2 + (m.x100 - m.x149)**2 + (m.x179
    - m.x228)**2 >= 0.46785600000000005)
m.e1420 = Constraint(expr= (m.x21 - m.x71)**2 + (m.x100 - m.x150)**2 + (m.x179
    - m.x229)**2 >= 0.46785600000000005)
m.e1421 = Constraint(expr= (m.x21 - m.x72)**2 + (m.x100 - m.x151)**2 + (m.x179
    - m.x230)**2 >= 0.46785600000000005)
m.e1422 = Constraint(expr= (m.x21 - m.x73)**2 + (m.x100 - m.x152)**2 + (m.x179
    - m.x231)**2 >= 0.46785600000000005)
m.e1423 = Constraint(expr= (m.x21 - m.x74)**2 + (m.x100 - m.x153)**2 + (m.x179
    - m.x232)**2 >= 0.46785600000000005)
m.e1424 = Constraint(expr= (m.x21 - m.x75)**2 + (m.x100 - m.x154)**2 + (m.x179
    - m.x233)**2 >= 0.46785600000000005)
m.e1425 = Constraint(expr= (m.x21 - m.x76)**2 + (m.x100 - m.x155)**2 + (m.x179
    - m.x234)**2 >= 0.46785600000000005)
m.e1426 = Constraint(expr= (m.x21 - m.x77)**2 + (m.x100 - m.x156)**2 + (m.x179
    - m.x235)**2 >= 0.46785600000000005)
m.e1427 = Constraint(expr= (m.x21 - m.x78)**2 + (m.x100 - m.x157)**2 + (m.x179
    - m.x236)**2 >= 0.46785600000000005)
m.e1428 = Constraint(expr= (m.x21 - m.x79)**2 + (m.x100 - m.x158)**2 + (m.x179
    - m.x237)**2 >= 0.46785600000000005)
m.e1429 = Constraint(expr= (m.x22 - m.x23)**2 + (m.x101 - m.x102)**2 + (m.x180
    - m.x181)**2 >= 0.46785600000000005)
m.e1430 = Constraint(expr= (m.x22 - m.x24)**2 + (m.x101 - m.x103)**2 + (m.x180
    - m.x182)**2 >= 0.46785600000000005)
m.e1431 = Constraint(expr= (m.x22 - m.x25)**2 + (m.x101 - m.x104)**2 + (m.x180
    - m.x183)**2 >= 0.46785600000000005)
m.e1432 = Constraint(expr= (m.x22 - m.x26)**2 + (m.x101 - m.x105)**2 + (m.x180
    - m.x184)**2 >= 0.46785600000000005)
m.e1433 = Constraint(expr= (m.x22 - m.x27)**2 + (m.x101 - m.x106)**2 + (m.x180
    - m.x185)**2 >= 0.46785600000000005)
m.e1434 = Constraint(expr= (m.x22 - m.x28)**2 + (m.x101 - m.x107)**2 + (m.x180
    - m.x186)**2 >= 0.46785600000000005)
m.e1435 = Constraint(expr= (m.x22 - m.x29)**2 + (m.x101 - m.x108)**2 + (m.x180
    - m.x187)**2 >= 0.46785600000000005)
m.e1436 = Constraint(expr= (m.x22 - m.x30)**2 + (m.x101 - m.x109)**2 + (m.x180
    - m.x188)**2 >= 0.46785600000000005)
m.e1437 = Constraint(expr= (m.x22 - m.x31)**2 + (m.x101 - m.x110)**2 + (m.x180
    - m.x189)**2 >= 0.46785600000000005)
m.e1438 = Constraint(expr= (m.x22 - m.x32)**2 + (m.x101 - m.x111)**2 + (m.x180
    - m.x190)**2 >= 0.46785600000000005)
m.e1439 = Constraint(expr= (m.x22 - m.x33)**2 + (m.x101 - m.x112)**2 + (m.x180
    - m.x191)**2 >= 0.46785600000000005)
m.e1440 = Constraint(expr= (m.x22 - m.x34)**2 + (m.x101 - m.x113)**2 + (m.x180
    - m.x192)**2 >= 0.46785600000000005)
m.e1441 = Constraint(expr= (m.x22 - m.x35)**2 + (m.x101 - m.x114)**2 + (m.x180
    - m.x193)**2 >= 0.46785600000000005)
m.e1442 = Constraint(expr= (m.x22 - m.x36)**2 + (m.x101 - m.x115)**2 + (m.x180
    - m.x194)**2 >= 0.46785600000000005)
m.e1443 = Constraint(expr= (m.x22 - m.x37)**2 + (m.x101 - m.x116)**2 + (m.x180
    - m.x195)**2 >= 0.46785600000000005)
m.e1444 = Constraint(expr= (m.x22 - m.x38)**2 + (m.x101 - m.x117)**2 + (m.x180
    - m.x196)**2 >= 0.46785600000000005)
m.e1445 = Constraint(expr= (m.x22 - m.x39)**2 + (m.x101 - m.x118)**2 + (m.x180
    - m.x197)**2 >= 0.46785600000000005)
m.e1446 = Constraint(expr= (m.x22 - m.x40)**2 + (m.x101 - m.x119)**2 + (m.x180
    - m.x198)**2 >= 0.46785600000000005)
m.e1447 = Constraint(expr= (m.x22 - m.x41)**2 + (m.x101 - m.x120)**2 + (m.x180
    - m.x199)**2 >= 0.46785600000000005)
m.e1448 = Constraint(expr= (m.x22 - m.x42)**2 + (m.x101 - m.x121)**2 + (m.x180
    - m.x200)**2 >= 0.46785600000000005)
m.e1449 = Constraint(expr= (m.x22 - m.x43)**2 + (m.x101 - m.x122)**2 + (m.x180
    - m.x201)**2 >= 0.46785600000000005)
m.e1450 = Constraint(expr= (m.x22 - m.x44)**2 + (m.x101 - m.x123)**2 + (m.x180
    - m.x202)**2 >= 0.46785600000000005)
m.e1451 = Constraint(expr= (m.x22 - m.x45)**2 + (m.x101 - m.x124)**2 + (m.x180
    - m.x203)**2 >= 0.46785600000000005)
m.e1452 = Constraint(expr= (m.x22 - m.x46)**2 + (m.x101 - m.x125)**2 + (m.x180
    - m.x204)**2 >= 0.46785600000000005)
m.e1453 = Constraint(expr= (m.x22 - m.x47)**2 + (m.x101 - m.x126)**2 + (m.x180
    - m.x205)**2 >= 0.46785600000000005)
m.e1454 = Constraint(expr= (m.x22 - m.x48)**2 + (m.x101 - m.x127)**2 + (m.x180
    - m.x206)**2 >= 0.46785600000000005)
m.e1455 = Constraint(expr= (m.x22 - m.x49)**2 + (m.x101 - m.x128)**2 + (m.x180
    - m.x207)**2 >= 0.46785600000000005)
m.e1456 = Constraint(expr= (m.x22 - m.x50)**2 + (m.x101 - m.x129)**2 + (m.x180
    - m.x208)**2 >= 0.46785600000000005)
m.e1457 = Constraint(expr= (m.x22 - m.x51)**2 + (m.x101 - m.x130)**2 + (m.x180
    - m.x209)**2 >= 0.46785600000000005)
m.e1458 = Constraint(expr= (m.x22 - m.x52)**2 + (m.x101 - m.x131)**2 + (m.x180
    - m.x210)**2 >= 0.46785600000000005)
m.e1459 = Constraint(expr= (m.x22 - m.x53)**2 + (m.x101 - m.x132)**2 + (m.x180
    - m.x211)**2 >= 0.46785600000000005)
m.e1460 = Constraint(expr= (m.x22 - m.x54)**2 + (m.x101 - m.x133)**2 + (m.x180
    - m.x212)**2 >= 0.46785600000000005)
m.e1461 = Constraint(expr= (m.x22 - m.x55)**2 + (m.x101 - m.x134)**2 + (m.x180
    - m.x213)**2 >= 0.46785600000000005)
m.e1462 = Constraint(expr= (m.x22 - m.x56)**2 + (m.x101 - m.x135)**2 + (m.x180
    - m.x214)**2 >= 0.46785600000000005)
m.e1463 = Constraint(expr= (m.x22 - m.x57)**2 + (m.x101 - m.x136)**2 + (m.x180
    - m.x215)**2 >= 0.46785600000000005)
m.e1464 = Constraint(expr= (m.x22 - m.x58)**2 + (m.x101 - m.x137)**2 + (m.x180
    - m.x216)**2 >= 0.46785600000000005)
m.e1465 = Constraint(expr= (m.x22 - m.x59)**2 + (m.x101 - m.x138)**2 + (m.x180
    - m.x217)**2 >= 0.46785600000000005)
m.e1466 = Constraint(expr= (m.x22 - m.x60)**2 + (m.x101 - m.x139)**2 + (m.x180
    - m.x218)**2 >= 0.46785600000000005)
m.e1467 = Constraint(expr= (m.x22 - m.x61)**2 + (m.x101 - m.x140)**2 + (m.x180
    - m.x219)**2 >= 0.46785600000000005)
m.e1468 = Constraint(expr= (m.x22 - m.x62)**2 + (m.x101 - m.x141)**2 + (m.x180
    - m.x220)**2 >= 0.46785600000000005)
m.e1469 = Constraint(expr= (m.x22 - m.x63)**2 + (m.x101 - m.x142)**2 + (m.x180
    - m.x221)**2 >= 0.46785600000000005)
m.e1470 = Constraint(expr= (m.x22 - m.x64)**2 + (m.x101 - m.x143)**2 + (m.x180
    - m.x222)**2 >= 0.46785600000000005)
m.e1471 = Constraint(expr= (m.x22 - m.x65)**2 + (m.x101 - m.x144)**2 + (m.x180
    - m.x223)**2 >= 0.46785600000000005)
m.e1472 = Constraint(expr= (m.x22 - m.x66)**2 + (m.x101 - m.x145)**2 + (m.x180
    - m.x224)**2 >= 0.46785600000000005)
m.e1473 = Constraint(expr= (m.x22 - m.x67)**2 + (m.x101 - m.x146)**2 + (m.x180
    - m.x225)**2 >= 0.46785600000000005)
m.e1474 = Constraint(expr= (m.x22 - m.x68)**2 + (m.x101 - m.x147)**2 + (m.x180
    - m.x226)**2 >= 0.46785600000000005)
m.e1475 = Constraint(expr= (m.x22 - m.x69)**2 + (m.x101 - m.x148)**2 + (m.x180
    - m.x227)**2 >= 0.46785600000000005)
m.e1476 = Constraint(expr= (m.x22 - m.x70)**2 + (m.x101 - m.x149)**2 + (m.x180
    - m.x228)**2 >= 0.46785600000000005)
m.e1477 = Constraint(expr= (m.x22 - m.x71)**2 + (m.x101 - m.x150)**2 + (m.x180
    - m.x229)**2 >= 0.46785600000000005)
m.e1478 = Constraint(expr= (m.x22 - m.x72)**2 + (m.x101 - m.x151)**2 + (m.x180
    - m.x230)**2 >= 0.46785600000000005)
m.e1479 = Constraint(expr= (m.x22 - m.x73)**2 + (m.x101 - m.x152)**2 + (m.x180
    - m.x231)**2 >= 0.46785600000000005)
m.e1480 = Constraint(expr= (m.x22 - m.x74)**2 + (m.x101 - m.x153)**2 + (m.x180
    - m.x232)**2 >= 0.46785600000000005)
m.e1481 = Constraint(expr= (m.x22 - m.x75)**2 + (m.x101 - m.x154)**2 + (m.x180
    - m.x233)**2 >= 0.46785600000000005)
m.e1482 = Constraint(expr= (m.x22 - m.x76)**2 + (m.x101 - m.x155)**2 + (m.x180
    - m.x234)**2 >= 0.46785600000000005)
m.e1483 = Constraint(expr= (m.x22 - m.x77)**2 + (m.x101 - m.x156)**2 + (m.x180
    - m.x235)**2 >= 0.46785600000000005)
m.e1484 = Constraint(expr= (m.x22 - m.x78)**2 + (m.x101 - m.x157)**2 + (m.x180
    - m.x236)**2 >= 0.46785600000000005)
m.e1485 = Constraint(expr= (m.x22 - m.x79)**2 + (m.x101 - m.x158)**2 + (m.x180
    - m.x237)**2 >= 0.46785600000000005)
m.e1486 = Constraint(expr= (m.x23 - m.x24)**2 + (m.x102 - m.x103)**2 + (m.x181
    - m.x182)**2 >= 0.46785600000000005)
m.e1487 = Constraint(expr= (m.x23 - m.x25)**2 + (m.x102 - m.x104)**2 + (m.x181
    - m.x183)**2 >= 0.46785600000000005)
m.e1488 = Constraint(expr= (m.x23 - m.x26)**2 + (m.x102 - m.x105)**2 + (m.x181
    - m.x184)**2 >= 0.46785600000000005)
m.e1489 = Constraint(expr= (m.x23 - m.x27)**2 + (m.x102 - m.x106)**2 + (m.x181
    - m.x185)**2 >= 0.46785600000000005)
m.e1490 = Constraint(expr= (m.x23 - m.x28)**2 + (m.x102 - m.x107)**2 + (m.x181
    - m.x186)**2 >= 0.46785600000000005)
m.e1491 = Constraint(expr= (m.x23 - m.x29)**2 + (m.x102 - m.x108)**2 + (m.x181
    - m.x187)**2 >= 0.46785600000000005)
m.e1492 = Constraint(expr= (m.x23 - m.x30)**2 + (m.x102 - m.x109)**2 + (m.x181
    - m.x188)**2 >= 0.46785600000000005)
m.e1493 = Constraint(expr= (m.x23 - m.x31)**2 + (m.x102 - m.x110)**2 + (m.x181
    - m.x189)**2 >= 0.46785600000000005)
m.e1494 = Constraint(expr= (m.x23 - m.x32)**2 + (m.x102 - m.x111)**2 + (m.x181
    - m.x190)**2 >= 0.46785600000000005)
m.e1495 = Constraint(expr= (m.x23 - m.x33)**2 + (m.x102 - m.x112)**2 + (m.x181
    - m.x191)**2 >= 0.46785600000000005)
m.e1496 = Constraint(expr= (m.x23 - m.x34)**2 + (m.x102 - m.x113)**2 + (m.x181
    - m.x192)**2 >= 0.46785600000000005)
m.e1497 = Constraint(expr= (m.x23 - m.x35)**2 + (m.x102 - m.x114)**2 + (m.x181
    - m.x193)**2 >= 0.46785600000000005)
m.e1498 = Constraint(expr= (m.x23 - m.x36)**2 + (m.x102 - m.x115)**2 + (m.x181
    - m.x194)**2 >= 0.46785600000000005)
m.e1499 = Constraint(expr= (m.x23 - m.x37)**2 + (m.x102 - m.x116)**2 + (m.x181
    - m.x195)**2 >= 0.46785600000000005)
m.e1500 = Constraint(expr= (m.x23 - m.x38)**2 + (m.x102 - m.x117)**2 + (m.x181
    - m.x196)**2 >= 0.46785600000000005)
m.e1501 = Constraint(expr= (m.x23 - m.x39)**2 + (m.x102 - m.x118)**2 + (m.x181
    - m.x197)**2 >= 0.46785600000000005)
m.e1502 = Constraint(expr= (m.x23 - m.x40)**2 + (m.x102 - m.x119)**2 + (m.x181
    - m.x198)**2 >= 0.46785600000000005)
m.e1503 = Constraint(expr= (m.x23 - m.x41)**2 + (m.x102 - m.x120)**2 + (m.x181
    - m.x199)**2 >= 0.46785600000000005)
m.e1504 = Constraint(expr= (m.x23 - m.x42)**2 + (m.x102 - m.x121)**2 + (m.x181
    - m.x200)**2 >= 0.46785600000000005)
m.e1505 = Constraint(expr= (m.x23 - m.x43)**2 + (m.x102 - m.x122)**2 + (m.x181
    - m.x201)**2 >= 0.46785600000000005)
m.e1506 = Constraint(expr= (m.x23 - m.x44)**2 + (m.x102 - m.x123)**2 + (m.x181
    - m.x202)**2 >= 0.46785600000000005)
m.e1507 = Constraint(expr= (m.x23 - m.x45)**2 + (m.x102 - m.x124)**2 + (m.x181
    - m.x203)**2 >= 0.46785600000000005)
m.e1508 = Constraint(expr= (m.x23 - m.x46)**2 + (m.x102 - m.x125)**2 + (m.x181
    - m.x204)**2 >= 0.46785600000000005)
m.e1509 = Constraint(expr= (m.x23 - m.x47)**2 + (m.x102 - m.x126)**2 + (m.x181
    - m.x205)**2 >= 0.46785600000000005)
m.e1510 = Constraint(expr= (m.x23 - m.x48)**2 + (m.x102 - m.x127)**2 + (m.x181
    - m.x206)**2 >= 0.46785600000000005)
m.e1511 = Constraint(expr= (m.x23 - m.x49)**2 + (m.x102 - m.x128)**2 + (m.x181
    - m.x207)**2 >= 0.46785600000000005)
m.e1512 = Constraint(expr= (m.x23 - m.x50)**2 + (m.x102 - m.x129)**2 + (m.x181
    - m.x208)**2 >= 0.46785600000000005)
m.e1513 = Constraint(expr= (m.x23 - m.x51)**2 + (m.x102 - m.x130)**2 + (m.x181
    - m.x209)**2 >= 0.46785600000000005)
m.e1514 = Constraint(expr= (m.x23 - m.x52)**2 + (m.x102 - m.x131)**2 + (m.x181
    - m.x210)**2 >= 0.46785600000000005)
m.e1515 = Constraint(expr= (m.x23 - m.x53)**2 + (m.x102 - m.x132)**2 + (m.x181
    - m.x211)**2 >= 0.46785600000000005)
m.e1516 = Constraint(expr= (m.x23 - m.x54)**2 + (m.x102 - m.x133)**2 + (m.x181
    - m.x212)**2 >= 0.46785600000000005)
m.e1517 = Constraint(expr= (m.x23 - m.x55)**2 + (m.x102 - m.x134)**2 + (m.x181
    - m.x213)**2 >= 0.46785600000000005)
m.e1518 = Constraint(expr= (m.x23 - m.x56)**2 + (m.x102 - m.x135)**2 + (m.x181
    - m.x214)**2 >= 0.46785600000000005)
m.e1519 = Constraint(expr= (m.x23 - m.x57)**2 + (m.x102 - m.x136)**2 + (m.x181
    - m.x215)**2 >= 0.46785600000000005)
m.e1520 = Constraint(expr= (m.x23 - m.x58)**2 + (m.x102 - m.x137)**2 + (m.x181
    - m.x216)**2 >= 0.46785600000000005)
m.e1521 = Constraint(expr= (m.x23 - m.x59)**2 + (m.x102 - m.x138)**2 + (m.x181
    - m.x217)**2 >= 0.46785600000000005)
m.e1522 = Constraint(expr= (m.x23 - m.x60)**2 + (m.x102 - m.x139)**2 + (m.x181
    - m.x218)**2 >= 0.46785600000000005)
m.e1523 = Constraint(expr= (m.x23 - m.x61)**2 + (m.x102 - m.x140)**2 + (m.x181
    - m.x219)**2 >= 0.46785600000000005)
m.e1524 = Constraint(expr= (m.x23 - m.x62)**2 + (m.x102 - m.x141)**2 + (m.x181
    - m.x220)**2 >= 0.46785600000000005)
m.e1525 = Constraint(expr= (m.x23 - m.x63)**2 + (m.x102 - m.x142)**2 + (m.x181
    - m.x221)**2 >= 0.46785600000000005)
m.e1526 = Constraint(expr= (m.x23 - m.x64)**2 + (m.x102 - m.x143)**2 + (m.x181
    - m.x222)**2 >= 0.46785600000000005)
m.e1527 = Constraint(expr= (m.x23 - m.x65)**2 + (m.x102 - m.x144)**2 + (m.x181
    - m.x223)**2 >= 0.46785600000000005)
m.e1528 = Constraint(expr= (m.x23 - m.x66)**2 + (m.x102 - m.x145)**2 + (m.x181
    - m.x224)**2 >= 0.46785600000000005)
m.e1529 = Constraint(expr= (m.x23 - m.x67)**2 + (m.x102 - m.x146)**2 + (m.x181
    - m.x225)**2 >= 0.46785600000000005)
m.e1530 = Constraint(expr= (m.x23 - m.x68)**2 + (m.x102 - m.x147)**2 + (m.x181
    - m.x226)**2 >= 0.46785600000000005)
m.e1531 = Constraint(expr= (m.x23 - m.x69)**2 + (m.x102 - m.x148)**2 + (m.x181
    - m.x227)**2 >= 0.46785600000000005)
m.e1532 = Constraint(expr= (m.x23 - m.x70)**2 + (m.x102 - m.x149)**2 + (m.x181
    - m.x228)**2 >= 0.46785600000000005)
m.e1533 = Constraint(expr= (m.x23 - m.x71)**2 + (m.x102 - m.x150)**2 + (m.x181
    - m.x229)**2 >= 0.46785600000000005)
m.e1534 = Constraint(expr= (m.x23 - m.x72)**2 + (m.x102 - m.x151)**2 + (m.x181
    - m.x230)**2 >= 0.46785600000000005)
m.e1535 = Constraint(expr= (m.x23 - m.x73)**2 + (m.x102 - m.x152)**2 + (m.x181
    - m.x231)**2 >= 0.46785600000000005)
m.e1536 = Constraint(expr= (m.x23 - m.x74)**2 + (m.x102 - m.x153)**2 + (m.x181
    - m.x232)**2 >= 0.46785600000000005)
m.e1537 = Constraint(expr= (m.x23 - m.x75)**2 + (m.x102 - m.x154)**2 + (m.x181
    - m.x233)**2 >= 0.46785600000000005)
m.e1538 = Constraint(expr= (m.x23 - m.x76)**2 + (m.x102 - m.x155)**2 + (m.x181
    - m.x234)**2 >= 0.46785600000000005)
m.e1539 = Constraint(expr= (m.x23 - m.x77)**2 + (m.x102 - m.x156)**2 + (m.x181
    - m.x235)**2 >= 0.46785600000000005)
m.e1540 = Constraint(expr= (m.x23 - m.x78)**2 + (m.x102 - m.x157)**2 + (m.x181
    - m.x236)**2 >= 0.46785600000000005)
m.e1541 = Constraint(expr= (m.x23 - m.x79)**2 + (m.x102 - m.x158)**2 + (m.x181
    - m.x237)**2 >= 0.46785600000000005)
m.e1542 = Constraint(expr= (m.x24 - m.x25)**2 + (m.x103 - m.x104)**2 + (m.x182
    - m.x183)**2 >= 0.46785600000000005)
m.e1543 = Constraint(expr= (m.x24 - m.x26)**2 + (m.x103 - m.x105)**2 + (m.x182
    - m.x184)**2 >= 0.46785600000000005)
m.e1544 = Constraint(expr= (m.x24 - m.x27)**2 + (m.x103 - m.x106)**2 + (m.x182
    - m.x185)**2 >= 0.46785600000000005)
m.e1545 = Constraint(expr= (m.x24 - m.x28)**2 + (m.x103 - m.x107)**2 + (m.x182
    - m.x186)**2 >= 0.46785600000000005)
m.e1546 = Constraint(expr= (m.x24 - m.x29)**2 + (m.x103 - m.x108)**2 + (m.x182
    - m.x187)**2 >= 0.46785600000000005)
m.e1547 = Constraint(expr= (m.x24 - m.x30)**2 + (m.x103 - m.x109)**2 + (m.x182
    - m.x188)**2 >= 0.46785600000000005)
m.e1548 = Constraint(expr= (m.x24 - m.x31)**2 + (m.x103 - m.x110)**2 + (m.x182
    - m.x189)**2 >= 0.46785600000000005)
m.e1549 = Constraint(expr= (m.x24 - m.x32)**2 + (m.x103 - m.x111)**2 + (m.x182
    - m.x190)**2 >= 0.46785600000000005)
m.e1550 = Constraint(expr= (m.x24 - m.x33)**2 + (m.x103 - m.x112)**2 + (m.x182
    - m.x191)**2 >= 0.46785600000000005)
m.e1551 = Constraint(expr= (m.x24 - m.x34)**2 + (m.x103 - m.x113)**2 + (m.x182
    - m.x192)**2 >= 0.46785600000000005)
m.e1552 = Constraint(expr= (m.x24 - m.x35)**2 + (m.x103 - m.x114)**2 + (m.x182
    - m.x193)**2 >= 0.46785600000000005)
m.e1553 = Constraint(expr= (m.x24 - m.x36)**2 + (m.x103 - m.x115)**2 + (m.x182
    - m.x194)**2 >= 0.46785600000000005)
m.e1554 = Constraint(expr= (m.x24 - m.x37)**2 + (m.x103 - m.x116)**2 + (m.x182
    - m.x195)**2 >= 0.46785600000000005)
m.e1555 = Constraint(expr= (m.x24 - m.x38)**2 + (m.x103 - m.x117)**2 + (m.x182
    - m.x196)**2 >= 0.46785600000000005)
m.e1556 = Constraint(expr= (m.x24 - m.x39)**2 + (m.x103 - m.x118)**2 + (m.x182
    - m.x197)**2 >= 0.46785600000000005)
m.e1557 = Constraint(expr= (m.x24 - m.x40)**2 + (m.x103 - m.x119)**2 + (m.x182
    - m.x198)**2 >= 0.46785600000000005)
m.e1558 = Constraint(expr= (m.x24 - m.x41)**2 + (m.x103 - m.x120)**2 + (m.x182
    - m.x199)**2 >= 0.46785600000000005)
m.e1559 = Constraint(expr= (m.x24 - m.x42)**2 + (m.x103 - m.x121)**2 + (m.x182
    - m.x200)**2 >= 0.46785600000000005)
m.e1560 = Constraint(expr= (m.x24 - m.x43)**2 + (m.x103 - m.x122)**2 + (m.x182
    - m.x201)**2 >= 0.46785600000000005)
m.e1561 = Constraint(expr= (m.x24 - m.x44)**2 + (m.x103 - m.x123)**2 + (m.x182
    - m.x202)**2 >= 0.46785600000000005)
m.e1562 = Constraint(expr= (m.x24 - m.x45)**2 + (m.x103 - m.x124)**2 + (m.x182
    - m.x203)**2 >= 0.46785600000000005)
m.e1563 = Constraint(expr= (m.x24 - m.x46)**2 + (m.x103 - m.x125)**2 + (m.x182
    - m.x204)**2 >= 0.46785600000000005)
m.e1564 = Constraint(expr= (m.x24 - m.x47)**2 + (m.x103 - m.x126)**2 + (m.x182
    - m.x205)**2 >= 0.46785600000000005)
m.e1565 = Constraint(expr= (m.x24 - m.x48)**2 + (m.x103 - m.x127)**2 + (m.x182
    - m.x206)**2 >= 0.46785600000000005)
m.e1566 = Constraint(expr= (m.x24 - m.x49)**2 + (m.x103 - m.x128)**2 + (m.x182
    - m.x207)**2 >= 0.46785600000000005)
m.e1567 = Constraint(expr= (m.x24 - m.x50)**2 + (m.x103 - m.x129)**2 + (m.x182
    - m.x208)**2 >= 0.46785600000000005)
m.e1568 = Constraint(expr= (m.x24 - m.x51)**2 + (m.x103 - m.x130)**2 + (m.x182
    - m.x209)**2 >= 0.46785600000000005)
m.e1569 = Constraint(expr= (m.x24 - m.x52)**2 + (m.x103 - m.x131)**2 + (m.x182
    - m.x210)**2 >= 0.46785600000000005)
m.e1570 = Constraint(expr= (m.x24 - m.x53)**2 + (m.x103 - m.x132)**2 + (m.x182
    - m.x211)**2 >= 0.46785600000000005)
m.e1571 = Constraint(expr= (m.x24 - m.x54)**2 + (m.x103 - m.x133)**2 + (m.x182
    - m.x212)**2 >= 0.46785600000000005)
m.e1572 = Constraint(expr= (m.x24 - m.x55)**2 + (m.x103 - m.x134)**2 + (m.x182
    - m.x213)**2 >= 0.46785600000000005)
m.e1573 = Constraint(expr= (m.x24 - m.x56)**2 + (m.x103 - m.x135)**2 + (m.x182
    - m.x214)**2 >= 0.46785600000000005)
m.e1574 = Constraint(expr= (m.x24 - m.x57)**2 + (m.x103 - m.x136)**2 + (m.x182
    - m.x215)**2 >= 0.46785600000000005)
m.e1575 = Constraint(expr= (m.x24 - m.x58)**2 + (m.x103 - m.x137)**2 + (m.x182
    - m.x216)**2 >= 0.46785600000000005)
m.e1576 = Constraint(expr= (m.x24 - m.x59)**2 + (m.x103 - m.x138)**2 + (m.x182
    - m.x217)**2 >= 0.46785600000000005)
m.e1577 = Constraint(expr= (m.x24 - m.x60)**2 + (m.x103 - m.x139)**2 + (m.x182
    - m.x218)**2 >= 0.46785600000000005)
m.e1578 = Constraint(expr= (m.x24 - m.x61)**2 + (m.x103 - m.x140)**2 + (m.x182
    - m.x219)**2 >= 0.46785600000000005)
m.e1579 = Constraint(expr= (m.x24 - m.x62)**2 + (m.x103 - m.x141)**2 + (m.x182
    - m.x220)**2 >= 0.46785600000000005)
m.e1580 = Constraint(expr= (m.x24 - m.x63)**2 + (m.x103 - m.x142)**2 + (m.x182
    - m.x221)**2 >= 0.46785600000000005)
m.e1581 = Constraint(expr= (m.x24 - m.x64)**2 + (m.x103 - m.x143)**2 + (m.x182
    - m.x222)**2 >= 0.46785600000000005)
m.e1582 = Constraint(expr= (m.x24 - m.x65)**2 + (m.x103 - m.x144)**2 + (m.x182
    - m.x223)**2 >= 0.46785600000000005)
m.e1583 = Constraint(expr= (m.x24 - m.x66)**2 + (m.x103 - m.x145)**2 + (m.x182
    - m.x224)**2 >= 0.46785600000000005)
m.e1584 = Constraint(expr= (m.x24 - m.x67)**2 + (m.x103 - m.x146)**2 + (m.x182
    - m.x225)**2 >= 0.46785600000000005)
m.e1585 = Constraint(expr= (m.x24 - m.x68)**2 + (m.x103 - m.x147)**2 + (m.x182
    - m.x226)**2 >= 0.46785600000000005)
m.e1586 = Constraint(expr= (m.x24 - m.x69)**2 + (m.x103 - m.x148)**2 + (m.x182
    - m.x227)**2 >= 0.46785600000000005)
m.e1587 = Constraint(expr= (m.x24 - m.x70)**2 + (m.x103 - m.x149)**2 + (m.x182
    - m.x228)**2 >= 0.46785600000000005)
m.e1588 = Constraint(expr= (m.x24 - m.x71)**2 + (m.x103 - m.x150)**2 + (m.x182
    - m.x229)**2 >= 0.46785600000000005)
m.e1589 = Constraint(expr= (m.x24 - m.x72)**2 + (m.x103 - m.x151)**2 + (m.x182
    - m.x230)**2 >= 0.46785600000000005)
m.e1590 = Constraint(expr= (m.x24 - m.x73)**2 + (m.x103 - m.x152)**2 + (m.x182
    - m.x231)**2 >= 0.46785600000000005)
m.e1591 = Constraint(expr= (m.x24 - m.x74)**2 + (m.x103 - m.x153)**2 + (m.x182
    - m.x232)**2 >= 0.46785600000000005)
m.e1592 = Constraint(expr= (m.x24 - m.x75)**2 + (m.x103 - m.x154)**2 + (m.x182
    - m.x233)**2 >= 0.46785600000000005)
m.e1593 = Constraint(expr= (m.x24 - m.x76)**2 + (m.x103 - m.x155)**2 + (m.x182
    - m.x234)**2 >= 0.46785600000000005)
m.e1594 = Constraint(expr= (m.x24 - m.x77)**2 + (m.x103 - m.x156)**2 + (m.x182
    - m.x235)**2 >= 0.46785600000000005)
m.e1595 = Constraint(expr= (m.x24 - m.x78)**2 + (m.x103 - m.x157)**2 + (m.x182
    - m.x236)**2 >= 0.46785600000000005)
m.e1596 = Constraint(expr= (m.x24 - m.x79)**2 + (m.x103 - m.x158)**2 + (m.x182
    - m.x237)**2 >= 0.46785600000000005)
m.e1597 = Constraint(expr= (m.x25 - m.x26)**2 + (m.x104 - m.x105)**2 + (m.x183
    - m.x184)**2 >= 0.46785600000000005)
m.e1598 = Constraint(expr= (m.x25 - m.x27)**2 + (m.x104 - m.x106)**2 + (m.x183
    - m.x185)**2 >= 0.46785600000000005)
m.e1599 = Constraint(expr= (m.x25 - m.x28)**2 + (m.x104 - m.x107)**2 + (m.x183
    - m.x186)**2 >= 0.46785600000000005)
m.e1600 = Constraint(expr= (m.x25 - m.x29)**2 + (m.x104 - m.x108)**2 + (m.x183
    - m.x187)**2 >= 0.46785600000000005)
m.e1601 = Constraint(expr= (m.x25 - m.x30)**2 + (m.x104 - m.x109)**2 + (m.x183
    - m.x188)**2 >= 0.46785600000000005)
m.e1602 = Constraint(expr= (m.x25 - m.x31)**2 + (m.x104 - m.x110)**2 + (m.x183
    - m.x189)**2 >= 0.46785600000000005)
m.e1603 = Constraint(expr= (m.x25 - m.x32)**2 + (m.x104 - m.x111)**2 + (m.x183
    - m.x190)**2 >= 0.46785600000000005)
m.e1604 = Constraint(expr= (m.x25 - m.x33)**2 + (m.x104 - m.x112)**2 + (m.x183
    - m.x191)**2 >= 0.46785600000000005)
m.e1605 = Constraint(expr= (m.x25 - m.x34)**2 + (m.x104 - m.x113)**2 + (m.x183
    - m.x192)**2 >= 0.46785600000000005)
m.e1606 = Constraint(expr= (m.x25 - m.x35)**2 + (m.x104 - m.x114)**2 + (m.x183
    - m.x193)**2 >= 0.46785600000000005)
m.e1607 = Constraint(expr= (m.x25 - m.x36)**2 + (m.x104 - m.x115)**2 + (m.x183
    - m.x194)**2 >= 0.46785600000000005)
m.e1608 = Constraint(expr= (m.x25 - m.x37)**2 + (m.x104 - m.x116)**2 + (m.x183
    - m.x195)**2 >= 0.46785600000000005)
m.e1609 = Constraint(expr= (m.x25 - m.x38)**2 + (m.x104 - m.x117)**2 + (m.x183
    - m.x196)**2 >= 0.46785600000000005)
m.e1610 = Constraint(expr= (m.x25 - m.x39)**2 + (m.x104 - m.x118)**2 + (m.x183
    - m.x197)**2 >= 0.46785600000000005)
m.e1611 = Constraint(expr= (m.x25 - m.x40)**2 + (m.x104 - m.x119)**2 + (m.x183
    - m.x198)**2 >= 0.46785600000000005)
m.e1612 = Constraint(expr= (m.x25 - m.x41)**2 + (m.x104 - m.x120)**2 + (m.x183
    - m.x199)**2 >= 0.46785600000000005)
m.e1613 = Constraint(expr= (m.x25 - m.x42)**2 + (m.x104 - m.x121)**2 + (m.x183
    - m.x200)**2 >= 0.46785600000000005)
m.e1614 = Constraint(expr= (m.x25 - m.x43)**2 + (m.x104 - m.x122)**2 + (m.x183
    - m.x201)**2 >= 0.46785600000000005)
m.e1615 = Constraint(expr= (m.x25 - m.x44)**2 + (m.x104 - m.x123)**2 + (m.x183
    - m.x202)**2 >= 0.46785600000000005)
m.e1616 = Constraint(expr= (m.x25 - m.x45)**2 + (m.x104 - m.x124)**2 + (m.x183
    - m.x203)**2 >= 0.46785600000000005)
m.e1617 = Constraint(expr= (m.x25 - m.x46)**2 + (m.x104 - m.x125)**2 + (m.x183
    - m.x204)**2 >= 0.46785600000000005)
m.e1618 = Constraint(expr= (m.x25 - m.x47)**2 + (m.x104 - m.x126)**2 + (m.x183
    - m.x205)**2 >= 0.46785600000000005)
m.e1619 = Constraint(expr= (m.x25 - m.x48)**2 + (m.x104 - m.x127)**2 + (m.x183
    - m.x206)**2 >= 0.46785600000000005)
m.e1620 = Constraint(expr= (m.x25 - m.x49)**2 + (m.x104 - m.x128)**2 + (m.x183
    - m.x207)**2 >= 0.46785600000000005)
m.e1621 = Constraint(expr= (m.x25 - m.x50)**2 + (m.x104 - m.x129)**2 + (m.x183
    - m.x208)**2 >= 0.46785600000000005)
m.e1622 = Constraint(expr= (m.x25 - m.x51)**2 + (m.x104 - m.x130)**2 + (m.x183
    - m.x209)**2 >= 0.46785600000000005)
m.e1623 = Constraint(expr= (m.x25 - m.x52)**2 + (m.x104 - m.x131)**2 + (m.x183
    - m.x210)**2 >= 0.46785600000000005)
m.e1624 = Constraint(expr= (m.x25 - m.x53)**2 + (m.x104 - m.x132)**2 + (m.x183
    - m.x211)**2 >= 0.46785600000000005)
m.e1625 = Constraint(expr= (m.x25 - m.x54)**2 + (m.x104 - m.x133)**2 + (m.x183
    - m.x212)**2 >= 0.46785600000000005)
m.e1626 = Constraint(expr= (m.x25 - m.x55)**2 + (m.x104 - m.x134)**2 + (m.x183
    - m.x213)**2 >= 0.46785600000000005)
m.e1627 = Constraint(expr= (m.x25 - m.x56)**2 + (m.x104 - m.x135)**2 + (m.x183
    - m.x214)**2 >= 0.46785600000000005)
m.e1628 = Constraint(expr= (m.x25 - m.x57)**2 + (m.x104 - m.x136)**2 + (m.x183
    - m.x215)**2 >= 0.46785600000000005)
m.e1629 = Constraint(expr= (m.x25 - m.x58)**2 + (m.x104 - m.x137)**2 + (m.x183
    - m.x216)**2 >= 0.46785600000000005)
m.e1630 = Constraint(expr= (m.x25 - m.x59)**2 + (m.x104 - m.x138)**2 + (m.x183
    - m.x217)**2 >= 0.46785600000000005)
m.e1631 = Constraint(expr= (m.x25 - m.x60)**2 + (m.x104 - m.x139)**2 + (m.x183
    - m.x218)**2 >= 0.46785600000000005)
m.e1632 = Constraint(expr= (m.x25 - m.x61)**2 + (m.x104 - m.x140)**2 + (m.x183
    - m.x219)**2 >= 0.46785600000000005)
m.e1633 = Constraint(expr= (m.x25 - m.x62)**2 + (m.x104 - m.x141)**2 + (m.x183
    - m.x220)**2 >= 0.46785600000000005)
m.e1634 = Constraint(expr= (m.x25 - m.x63)**2 + (m.x104 - m.x142)**2 + (m.x183
    - m.x221)**2 >= 0.46785600000000005)
m.e1635 = Constraint(expr= (m.x25 - m.x64)**2 + (m.x104 - m.x143)**2 + (m.x183
    - m.x222)**2 >= 0.46785600000000005)
m.e1636 = Constraint(expr= (m.x25 - m.x65)**2 + (m.x104 - m.x144)**2 + (m.x183
    - m.x223)**2 >= 0.46785600000000005)
m.e1637 = Constraint(expr= (m.x25 - m.x66)**2 + (m.x104 - m.x145)**2 + (m.x183
    - m.x224)**2 >= 0.46785600000000005)
m.e1638 = Constraint(expr= (m.x25 - m.x67)**2 + (m.x104 - m.x146)**2 + (m.x183
    - m.x225)**2 >= 0.46785600000000005)
m.e1639 = Constraint(expr= (m.x25 - m.x68)**2 + (m.x104 - m.x147)**2 + (m.x183
    - m.x226)**2 >= 0.46785600000000005)
m.e1640 = Constraint(expr= (m.x25 - m.x69)**2 + (m.x104 - m.x148)**2 + (m.x183
    - m.x227)**2 >= 0.46785600000000005)
m.e1641 = Constraint(expr= (m.x25 - m.x70)**2 + (m.x104 - m.x149)**2 + (m.x183
    - m.x228)**2 >= 0.46785600000000005)
m.e1642 = Constraint(expr= (m.x25 - m.x71)**2 + (m.x104 - m.x150)**2 + (m.x183
    - m.x229)**2 >= 0.46785600000000005)
m.e1643 = Constraint(expr= (m.x25 - m.x72)**2 + (m.x104 - m.x151)**2 + (m.x183
    - m.x230)**2 >= 0.46785600000000005)
m.e1644 = Constraint(expr= (m.x25 - m.x73)**2 + (m.x104 - m.x152)**2 + (m.x183
    - m.x231)**2 >= 0.46785600000000005)
m.e1645 = Constraint(expr= (m.x25 - m.x74)**2 + (m.x104 - m.x153)**2 + (m.x183
    - m.x232)**2 >= 0.46785600000000005)
m.e1646 = Constraint(expr= (m.x25 - m.x75)**2 + (m.x104 - m.x154)**2 + (m.x183
    - m.x233)**2 >= 0.46785600000000005)
m.e1647 = Constraint(expr= (m.x25 - m.x76)**2 + (m.x104 - m.x155)**2 + (m.x183
    - m.x234)**2 >= 0.46785600000000005)
m.e1648 = Constraint(expr= (m.x25 - m.x77)**2 + (m.x104 - m.x156)**2 + (m.x183
    - m.x235)**2 >= 0.46785600000000005)
m.e1649 = Constraint(expr= (m.x25 - m.x78)**2 + (m.x104 - m.x157)**2 + (m.x183
    - m.x236)**2 >= 0.46785600000000005)
m.e1650 = Constraint(expr= (m.x25 - m.x79)**2 + (m.x104 - m.x158)**2 + (m.x183
    - m.x237)**2 >= 0.46785600000000005)
m.e1651 = Constraint(expr= (m.x26 - m.x27)**2 + (m.x105 - m.x106)**2 + (m.x184
    - m.x185)**2 >= 0.46785600000000005)
m.e1652 = Constraint(expr= (m.x26 - m.x28)**2 + (m.x105 - m.x107)**2 + (m.x184
    - m.x186)**2 >= 0.46785600000000005)
m.e1653 = Constraint(expr= (m.x26 - m.x29)**2 + (m.x105 - m.x108)**2 + (m.x184
    - m.x187)**2 >= 0.46785600000000005)
m.e1654 = Constraint(expr= (m.x26 - m.x30)**2 + (m.x105 - m.x109)**2 + (m.x184
    - m.x188)**2 >= 0.46785600000000005)
m.e1655 = Constraint(expr= (m.x26 - m.x31)**2 + (m.x105 - m.x110)**2 + (m.x184
    - m.x189)**2 >= 0.46785600000000005)
m.e1656 = Constraint(expr= (m.x26 - m.x32)**2 + (m.x105 - m.x111)**2 + (m.x184
    - m.x190)**2 >= 0.46785600000000005)
m.e1657 = Constraint(expr= (m.x26 - m.x33)**2 + (m.x105 - m.x112)**2 + (m.x184
    - m.x191)**2 >= 0.46785600000000005)
m.e1658 = Constraint(expr= (m.x26 - m.x34)**2 + (m.x105 - m.x113)**2 + (m.x184
    - m.x192)**2 >= 0.46785600000000005)
m.e1659 = Constraint(expr= (m.x26 - m.x35)**2 + (m.x105 - m.x114)**2 + (m.x184
    - m.x193)**2 >= 0.46785600000000005)
m.e1660 = Constraint(expr= (m.x26 - m.x36)**2 + (m.x105 - m.x115)**2 + (m.x184
    - m.x194)**2 >= 0.46785600000000005)
m.e1661 = Constraint(expr= (m.x26 - m.x37)**2 + (m.x105 - m.x116)**2 + (m.x184
    - m.x195)**2 >= 0.46785600000000005)
m.e1662 = Constraint(expr= (m.x26 - m.x38)**2 + (m.x105 - m.x117)**2 + (m.x184
    - m.x196)**2 >= 0.46785600000000005)
m.e1663 = Constraint(expr= (m.x26 - m.x39)**2 + (m.x105 - m.x118)**2 + (m.x184
    - m.x197)**2 >= 0.46785600000000005)
m.e1664 = Constraint(expr= (m.x26 - m.x40)**2 + (m.x105 - m.x119)**2 + (m.x184
    - m.x198)**2 >= 0.46785600000000005)
m.e1665 = Constraint(expr= (m.x26 - m.x41)**2 + (m.x105 - m.x120)**2 + (m.x184
    - m.x199)**2 >= 0.46785600000000005)
m.e1666 = Constraint(expr= (m.x26 - m.x42)**2 + (m.x105 - m.x121)**2 + (m.x184
    - m.x200)**2 >= 0.46785600000000005)
m.e1667 = Constraint(expr= (m.x26 - m.x43)**2 + (m.x105 - m.x122)**2 + (m.x184
    - m.x201)**2 >= 0.46785600000000005)
m.e1668 = Constraint(expr= (m.x26 - m.x44)**2 + (m.x105 - m.x123)**2 + (m.x184
    - m.x202)**2 >= 0.46785600000000005)
m.e1669 = Constraint(expr= (m.x26 - m.x45)**2 + (m.x105 - m.x124)**2 + (m.x184
    - m.x203)**2 >= 0.46785600000000005)
m.e1670 = Constraint(expr= (m.x26 - m.x46)**2 + (m.x105 - m.x125)**2 + (m.x184
    - m.x204)**2 >= 0.46785600000000005)
m.e1671 = Constraint(expr= (m.x26 - m.x47)**2 + (m.x105 - m.x126)**2 + (m.x184
    - m.x205)**2 >= 0.46785600000000005)
m.e1672 = Constraint(expr= (m.x26 - m.x48)**2 + (m.x105 - m.x127)**2 + (m.x184
    - m.x206)**2 >= 0.46785600000000005)
m.e1673 = Constraint(expr= (m.x26 - m.x49)**2 + (m.x105 - m.x128)**2 + (m.x184
    - m.x207)**2 >= 0.46785600000000005)
m.e1674 = Constraint(expr= (m.x26 - m.x50)**2 + (m.x105 - m.x129)**2 + (m.x184
    - m.x208)**2 >= 0.46785600000000005)
m.e1675 = Constraint(expr= (m.x26 - m.x51)**2 + (m.x105 - m.x130)**2 + (m.x184
    - m.x209)**2 >= 0.46785600000000005)
m.e1676 = Constraint(expr= (m.x26 - m.x52)**2 + (m.x105 - m.x131)**2 + (m.x184
    - m.x210)**2 >= 0.46785600000000005)
m.e1677 = Constraint(expr= (m.x26 - m.x53)**2 + (m.x105 - m.x132)**2 + (m.x184
    - m.x211)**2 >= 0.46785600000000005)
m.e1678 = Constraint(expr= (m.x26 - m.x54)**2 + (m.x105 - m.x133)**2 + (m.x184
    - m.x212)**2 >= 0.46785600000000005)
m.e1679 = Constraint(expr= (m.x26 - m.x55)**2 + (m.x105 - m.x134)**2 + (m.x184
    - m.x213)**2 >= 0.46785600000000005)
m.e1680 = Constraint(expr= (m.x26 - m.x56)**2 + (m.x105 - m.x135)**2 + (m.x184
    - m.x214)**2 >= 0.46785600000000005)
m.e1681 = Constraint(expr= (m.x26 - m.x57)**2 + (m.x105 - m.x136)**2 + (m.x184
    - m.x215)**2 >= 0.46785600000000005)
m.e1682 = Constraint(expr= (m.x26 - m.x58)**2 + (m.x105 - m.x137)**2 + (m.x184
    - m.x216)**2 >= 0.46785600000000005)
m.e1683 = Constraint(expr= (m.x26 - m.x59)**2 + (m.x105 - m.x138)**2 + (m.x184
    - m.x217)**2 >= 0.46785600000000005)
m.e1684 = Constraint(expr= (m.x26 - m.x60)**2 + (m.x105 - m.x139)**2 + (m.x184
    - m.x218)**2 >= 0.46785600000000005)
m.e1685 = Constraint(expr= (m.x26 - m.x61)**2 + (m.x105 - m.x140)**2 + (m.x184
    - m.x219)**2 >= 0.46785600000000005)
m.e1686 = Constraint(expr= (m.x26 - m.x62)**2 + (m.x105 - m.x141)**2 + (m.x184
    - m.x220)**2 >= 0.46785600000000005)
m.e1687 = Constraint(expr= (m.x26 - m.x63)**2 + (m.x105 - m.x142)**2 + (m.x184
    - m.x221)**2 >= 0.46785600000000005)
m.e1688 = Constraint(expr= (m.x26 - m.x64)**2 + (m.x105 - m.x143)**2 + (m.x184
    - m.x222)**2 >= 0.46785600000000005)
m.e1689 = Constraint(expr= (m.x26 - m.x65)**2 + (m.x105 - m.x144)**2 + (m.x184
    - m.x223)**2 >= 0.46785600000000005)
m.e1690 = Constraint(expr= (m.x26 - m.x66)**2 + (m.x105 - m.x145)**2 + (m.x184
    - m.x224)**2 >= 0.46785600000000005)
m.e1691 = Constraint(expr= (m.x26 - m.x67)**2 + (m.x105 - m.x146)**2 + (m.x184
    - m.x225)**2 >= 0.46785600000000005)
m.e1692 = Constraint(expr= (m.x26 - m.x68)**2 + (m.x105 - m.x147)**2 + (m.x184
    - m.x226)**2 >= 0.46785600000000005)
m.e1693 = Constraint(expr= (m.x26 - m.x69)**2 + (m.x105 - m.x148)**2 + (m.x184
    - m.x227)**2 >= 0.46785600000000005)
m.e1694 = Constraint(expr= (m.x26 - m.x70)**2 + (m.x105 - m.x149)**2 + (m.x184
    - m.x228)**2 >= 0.46785600000000005)
m.e1695 = Constraint(expr= (m.x26 - m.x71)**2 + (m.x105 - m.x150)**2 + (m.x184
    - m.x229)**2 >= 0.46785600000000005)
m.e1696 = Constraint(expr= (m.x26 - m.x72)**2 + (m.x105 - m.x151)**2 + (m.x184
    - m.x230)**2 >= 0.46785600000000005)
m.e1697 = Constraint(expr= (m.x26 - m.x73)**2 + (m.x105 - m.x152)**2 + (m.x184
    - m.x231)**2 >= 0.46785600000000005)
m.e1698 = Constraint(expr= (m.x26 - m.x74)**2 + (m.x105 - m.x153)**2 + (m.x184
    - m.x232)**2 >= 0.46785600000000005)
m.e1699 = Constraint(expr= (m.x26 - m.x75)**2 + (m.x105 - m.x154)**2 + (m.x184
    - m.x233)**2 >= 0.46785600000000005)
m.e1700 = Constraint(expr= (m.x26 - m.x76)**2 + (m.x105 - m.x155)**2 + (m.x184
    - m.x234)**2 >= 0.46785600000000005)
m.e1701 = Constraint(expr= (m.x26 - m.x77)**2 + (m.x105 - m.x156)**2 + (m.x184
    - m.x235)**2 >= 0.46785600000000005)
m.e1702 = Constraint(expr= (m.x26 - m.x78)**2 + (m.x105 - m.x157)**2 + (m.x184
    - m.x236)**2 >= 0.46785600000000005)
m.e1703 = Constraint(expr= (m.x26 - m.x79)**2 + (m.x105 - m.x158)**2 + (m.x184
    - m.x237)**2 >= 0.46785600000000005)
m.e1704 = Constraint(expr= (m.x27 - m.x28)**2 + (m.x106 - m.x107)**2 + (m.x185
    - m.x186)**2 >= 0.46785600000000005)
m.e1705 = Constraint(expr= (m.x27 - m.x29)**2 + (m.x106 - m.x108)**2 + (m.x185
    - m.x187)**2 >= 0.46785600000000005)
m.e1706 = Constraint(expr= (m.x27 - m.x30)**2 + (m.x106 - m.x109)**2 + (m.x185
    - m.x188)**2 >= 0.46785600000000005)
m.e1707 = Constraint(expr= (m.x27 - m.x31)**2 + (m.x106 - m.x110)**2 + (m.x185
    - m.x189)**2 >= 0.46785600000000005)
m.e1708 = Constraint(expr= (m.x27 - m.x32)**2 + (m.x106 - m.x111)**2 + (m.x185
    - m.x190)**2 >= 0.46785600000000005)
m.e1709 = Constraint(expr= (m.x27 - m.x33)**2 + (m.x106 - m.x112)**2 + (m.x185
    - m.x191)**2 >= 0.46785600000000005)
m.e1710 = Constraint(expr= (m.x27 - m.x34)**2 + (m.x106 - m.x113)**2 + (m.x185
    - m.x192)**2 >= 0.46785600000000005)
m.e1711 = Constraint(expr= (m.x27 - m.x35)**2 + (m.x106 - m.x114)**2 + (m.x185
    - m.x193)**2 >= 0.46785600000000005)
m.e1712 = Constraint(expr= (m.x27 - m.x36)**2 + (m.x106 - m.x115)**2 + (m.x185
    - m.x194)**2 >= 0.46785600000000005)
m.e1713 = Constraint(expr= (m.x27 - m.x37)**2 + (m.x106 - m.x116)**2 + (m.x185
    - m.x195)**2 >= 0.46785600000000005)
m.e1714 = Constraint(expr= (m.x27 - m.x38)**2 + (m.x106 - m.x117)**2 + (m.x185
    - m.x196)**2 >= 0.46785600000000005)
m.e1715 = Constraint(expr= (m.x27 - m.x39)**2 + (m.x106 - m.x118)**2 + (m.x185
    - m.x197)**2 >= 0.46785600000000005)
m.e1716 = Constraint(expr= (m.x27 - m.x40)**2 + (m.x106 - m.x119)**2 + (m.x185
    - m.x198)**2 >= 0.46785600000000005)
m.e1717 = Constraint(expr= (m.x27 - m.x41)**2 + (m.x106 - m.x120)**2 + (m.x185
    - m.x199)**2 >= 0.46785600000000005)
m.e1718 = Constraint(expr= (m.x27 - m.x42)**2 + (m.x106 - m.x121)**2 + (m.x185
    - m.x200)**2 >= 0.46785600000000005)
m.e1719 = Constraint(expr= (m.x27 - m.x43)**2 + (m.x106 - m.x122)**2 + (m.x185
    - m.x201)**2 >= 0.46785600000000005)
m.e1720 = Constraint(expr= (m.x27 - m.x44)**2 + (m.x106 - m.x123)**2 + (m.x185
    - m.x202)**2 >= 0.46785600000000005)
m.e1721 = Constraint(expr= (m.x27 - m.x45)**2 + (m.x106 - m.x124)**2 + (m.x185
    - m.x203)**2 >= 0.46785600000000005)
m.e1722 = Constraint(expr= (m.x27 - m.x46)**2 + (m.x106 - m.x125)**2 + (m.x185
    - m.x204)**2 >= 0.46785600000000005)
m.e1723 = Constraint(expr= (m.x27 - m.x47)**2 + (m.x106 - m.x126)**2 + (m.x185
    - m.x205)**2 >= 0.46785600000000005)
m.e1724 = Constraint(expr= (m.x27 - m.x48)**2 + (m.x106 - m.x127)**2 + (m.x185
    - m.x206)**2 >= 0.46785600000000005)
m.e1725 = Constraint(expr= (m.x27 - m.x49)**2 + (m.x106 - m.x128)**2 + (m.x185
    - m.x207)**2 >= 0.46785600000000005)
m.e1726 = Constraint(expr= (m.x27 - m.x50)**2 + (m.x106 - m.x129)**2 + (m.x185
    - m.x208)**2 >= 0.46785600000000005)
m.e1727 = Constraint(expr= (m.x27 - m.x51)**2 + (m.x106 - m.x130)**2 + (m.x185
    - m.x209)**2 >= 0.46785600000000005)
m.e1728 = Constraint(expr= (m.x27 - m.x52)**2 + (m.x106 - m.x131)**2 + (m.x185
    - m.x210)**2 >= 0.46785600000000005)
m.e1729 = Constraint(expr= (m.x27 - m.x53)**2 + (m.x106 - m.x132)**2 + (m.x185
    - m.x211)**2 >= 0.46785600000000005)
m.e1730 = Constraint(expr= (m.x27 - m.x54)**2 + (m.x106 - m.x133)**2 + (m.x185
    - m.x212)**2 >= 0.46785600000000005)
m.e1731 = Constraint(expr= (m.x27 - m.x55)**2 + (m.x106 - m.x134)**2 + (m.x185
    - m.x213)**2 >= 0.46785600000000005)
m.e1732 = Constraint(expr= (m.x27 - m.x56)**2 + (m.x106 - m.x135)**2 + (m.x185
    - m.x214)**2 >= 0.46785600000000005)
m.e1733 = Constraint(expr= (m.x27 - m.x57)**2 + (m.x106 - m.x136)**2 + (m.x185
    - m.x215)**2 >= 0.46785600000000005)
m.e1734 = Constraint(expr= (m.x27 - m.x58)**2 + (m.x106 - m.x137)**2 + (m.x185
    - m.x216)**2 >= 0.46785600000000005)
m.e1735 = Constraint(expr= (m.x27 - m.x59)**2 + (m.x106 - m.x138)**2 + (m.x185
    - m.x217)**2 >= 0.46785600000000005)
m.e1736 = Constraint(expr= (m.x27 - m.x60)**2 + (m.x106 - m.x139)**2 + (m.x185
    - m.x218)**2 >= 0.46785600000000005)
m.e1737 = Constraint(expr= (m.x27 - m.x61)**2 + (m.x106 - m.x140)**2 + (m.x185
    - m.x219)**2 >= 0.46785600000000005)
m.e1738 = Constraint(expr= (m.x27 - m.x62)**2 + (m.x106 - m.x141)**2 + (m.x185
    - m.x220)**2 >= 0.46785600000000005)
m.e1739 = Constraint(expr= (m.x27 - m.x63)**2 + (m.x106 - m.x142)**2 + (m.x185
    - m.x221)**2 >= 0.46785600000000005)
m.e1740 = Constraint(expr= (m.x27 - m.x64)**2 + (m.x106 - m.x143)**2 + (m.x185
    - m.x222)**2 >= 0.46785600000000005)
m.e1741 = Constraint(expr= (m.x27 - m.x65)**2 + (m.x106 - m.x144)**2 + (m.x185
    - m.x223)**2 >= 0.46785600000000005)
m.e1742 = Constraint(expr= (m.x27 - m.x66)**2 + (m.x106 - m.x145)**2 + (m.x185
    - m.x224)**2 >= 0.46785600000000005)
m.e1743 = Constraint(expr= (m.x27 - m.x67)**2 + (m.x106 - m.x146)**2 + (m.x185
    - m.x225)**2 >= 0.46785600000000005)
m.e1744 = Constraint(expr= (m.x27 - m.x68)**2 + (m.x106 - m.x147)**2 + (m.x185
    - m.x226)**2 >= 0.46785600000000005)
m.e1745 = Constraint(expr= (m.x27 - m.x69)**2 + (m.x106 - m.x148)**2 + (m.x185
    - m.x227)**2 >= 0.46785600000000005)
m.e1746 = Constraint(expr= (m.x27 - m.x70)**2 + (m.x106 - m.x149)**2 + (m.x185
    - m.x228)**2 >= 0.46785600000000005)
m.e1747 = Constraint(expr= (m.x27 - m.x71)**2 + (m.x106 - m.x150)**2 + (m.x185
    - m.x229)**2 >= 0.46785600000000005)
m.e1748 = Constraint(expr= (m.x27 - m.x72)**2 + (m.x106 - m.x151)**2 + (m.x185
    - m.x230)**2 >= 0.46785600000000005)
m.e1749 = Constraint(expr= (m.x27 - m.x73)**2 + (m.x106 - m.x152)**2 + (m.x185
    - m.x231)**2 >= 0.46785600000000005)
m.e1750 = Constraint(expr= (m.x27 - m.x74)**2 + (m.x106 - m.x153)**2 + (m.x185
    - m.x232)**2 >= 0.46785600000000005)
m.e1751 = Constraint(expr= (m.x27 - m.x75)**2 + (m.x106 - m.x154)**2 + (m.x185
    - m.x233)**2 >= 0.46785600000000005)
m.e1752 = Constraint(expr= (m.x27 - m.x76)**2 + (m.x106 - m.x155)**2 + (m.x185
    - m.x234)**2 >= 0.46785600000000005)
m.e1753 = Constraint(expr= (m.x27 - m.x77)**2 + (m.x106 - m.x156)**2 + (m.x185
    - m.x235)**2 >= 0.46785600000000005)
m.e1754 = Constraint(expr= (m.x27 - m.x78)**2 + (m.x106 - m.x157)**2 + (m.x185
    - m.x236)**2 >= 0.46785600000000005)
m.e1755 = Constraint(expr= (m.x27 - m.x79)**2 + (m.x106 - m.x158)**2 + (m.x185
    - m.x237)**2 >= 0.46785600000000005)
m.e1756 = Constraint(expr= (m.x28 - m.x29)**2 + (m.x107 - m.x108)**2 + (m.x186
    - m.x187)**2 >= 0.46785600000000005)
m.e1757 = Constraint(expr= (m.x28 - m.x30)**2 + (m.x107 - m.x109)**2 + (m.x186
    - m.x188)**2 >= 0.46785600000000005)
m.e1758 = Constraint(expr= (m.x28 - m.x31)**2 + (m.x107 - m.x110)**2 + (m.x186
    - m.x189)**2 >= 0.46785600000000005)
m.e1759 = Constraint(expr= (m.x28 - m.x32)**2 + (m.x107 - m.x111)**2 + (m.x186
    - m.x190)**2 >= 0.46785600000000005)
m.e1760 = Constraint(expr= (m.x28 - m.x33)**2 + (m.x107 - m.x112)**2 + (m.x186
    - m.x191)**2 >= 0.46785600000000005)
m.e1761 = Constraint(expr= (m.x28 - m.x34)**2 + (m.x107 - m.x113)**2 + (m.x186
    - m.x192)**2 >= 0.46785600000000005)
m.e1762 = Constraint(expr= (m.x28 - m.x35)**2 + (m.x107 - m.x114)**2 + (m.x186
    - m.x193)**2 >= 0.46785600000000005)
m.e1763 = Constraint(expr= (m.x28 - m.x36)**2 + (m.x107 - m.x115)**2 + (m.x186
    - m.x194)**2 >= 0.46785600000000005)
m.e1764 = Constraint(expr= (m.x28 - m.x37)**2 + (m.x107 - m.x116)**2 + (m.x186
    - m.x195)**2 >= 0.46785600000000005)
m.e1765 = Constraint(expr= (m.x28 - m.x38)**2 + (m.x107 - m.x117)**2 + (m.x186
    - m.x196)**2 >= 0.46785600000000005)
m.e1766 = Constraint(expr= (m.x28 - m.x39)**2 + (m.x107 - m.x118)**2 + (m.x186
    - m.x197)**2 >= 0.46785600000000005)
m.e1767 = Constraint(expr= (m.x28 - m.x40)**2 + (m.x107 - m.x119)**2 + (m.x186
    - m.x198)**2 >= 0.46785600000000005)
m.e1768 = Constraint(expr= (m.x28 - m.x41)**2 + (m.x107 - m.x120)**2 + (m.x186
    - m.x199)**2 >= 0.46785600000000005)
m.e1769 = Constraint(expr= (m.x28 - m.x42)**2 + (m.x107 - m.x121)**2 + (m.x186
    - m.x200)**2 >= 0.46785600000000005)
m.e1770 = Constraint(expr= (m.x28 - m.x43)**2 + (m.x107 - m.x122)**2 + (m.x186
    - m.x201)**2 >= 0.46785600000000005)
m.e1771 = Constraint(expr= (m.x28 - m.x44)**2 + (m.x107 - m.x123)**2 + (m.x186
    - m.x202)**2 >= 0.46785600000000005)
m.e1772 = Constraint(expr= (m.x28 - m.x45)**2 + (m.x107 - m.x124)**2 + (m.x186
    - m.x203)**2 >= 0.46785600000000005)
m.e1773 = Constraint(expr= (m.x28 - m.x46)**2 + (m.x107 - m.x125)**2 + (m.x186
    - m.x204)**2 >= 0.46785600000000005)
m.e1774 = Constraint(expr= (m.x28 - m.x47)**2 + (m.x107 - m.x126)**2 + (m.x186
    - m.x205)**2 >= 0.46785600000000005)
m.e1775 = Constraint(expr= (m.x28 - m.x48)**2 + (m.x107 - m.x127)**2 + (m.x186
    - m.x206)**2 >= 0.46785600000000005)
m.e1776 = Constraint(expr= (m.x28 - m.x49)**2 + (m.x107 - m.x128)**2 + (m.x186
    - m.x207)**2 >= 0.46785600000000005)
m.e1777 = Constraint(expr= (m.x28 - m.x50)**2 + (m.x107 - m.x129)**2 + (m.x186
    - m.x208)**2 >= 0.46785600000000005)
m.e1778 = Constraint(expr= (m.x28 - m.x51)**2 + (m.x107 - m.x130)**2 + (m.x186
    - m.x209)**2 >= 0.46785600000000005)
m.e1779 = Constraint(expr= (m.x28 - m.x52)**2 + (m.x107 - m.x131)**2 + (m.x186
    - m.x210)**2 >= 0.46785600000000005)
m.e1780 = Constraint(expr= (m.x28 - m.x53)**2 + (m.x107 - m.x132)**2 + (m.x186
    - m.x211)**2 >= 0.46785600000000005)
m.e1781 = Constraint(expr= (m.x28 - m.x54)**2 + (m.x107 - m.x133)**2 + (m.x186
    - m.x212)**2 >= 0.46785600000000005)
m.e1782 = Constraint(expr= (m.x28 - m.x55)**2 + (m.x107 - m.x134)**2 + (m.x186
    - m.x213)**2 >= 0.46785600000000005)
m.e1783 = Constraint(expr= (m.x28 - m.x56)**2 + (m.x107 - m.x135)**2 + (m.x186
    - m.x214)**2 >= 0.46785600000000005)
m.e1784 = Constraint(expr= (m.x28 - m.x57)**2 + (m.x107 - m.x136)**2 + (m.x186
    - m.x215)**2 >= 0.46785600000000005)
m.e1785 = Constraint(expr= (m.x28 - m.x58)**2 + (m.x107 - m.x137)**2 + (m.x186
    - m.x216)**2 >= 0.46785600000000005)
m.e1786 = Constraint(expr= (m.x28 - m.x59)**2 + (m.x107 - m.x138)**2 + (m.x186
    - m.x217)**2 >= 0.46785600000000005)
m.e1787 = Constraint(expr= (m.x28 - m.x60)**2 + (m.x107 - m.x139)**2 + (m.x186
    - m.x218)**2 >= 0.46785600000000005)
m.e1788 = Constraint(expr= (m.x28 - m.x61)**2 + (m.x107 - m.x140)**2 + (m.x186
    - m.x219)**2 >= 0.46785600000000005)
m.e1789 = Constraint(expr= (m.x28 - m.x62)**2 + (m.x107 - m.x141)**2 + (m.x186
    - m.x220)**2 >= 0.46785600000000005)
m.e1790 = Constraint(expr= (m.x28 - m.x63)**2 + (m.x107 - m.x142)**2 + (m.x186
    - m.x221)**2 >= 0.46785600000000005)
m.e1791 = Constraint(expr= (m.x28 - m.x64)**2 + (m.x107 - m.x143)**2 + (m.x186
    - m.x222)**2 >= 0.46785600000000005)
m.e1792 = Constraint(expr= (m.x28 - m.x65)**2 + (m.x107 - m.x144)**2 + (m.x186
    - m.x223)**2 >= 0.46785600000000005)
m.e1793 = Constraint(expr= (m.x28 - m.x66)**2 + (m.x107 - m.x145)**2 + (m.x186
    - m.x224)**2 >= 0.46785600000000005)
m.e1794 = Constraint(expr= (m.x28 - m.x67)**2 + (m.x107 - m.x146)**2 + (m.x186
    - m.x225)**2 >= 0.46785600000000005)
m.e1795 = Constraint(expr= (m.x28 - m.x68)**2 + (m.x107 - m.x147)**2 + (m.x186
    - m.x226)**2 >= 0.46785600000000005)
m.e1796 = Constraint(expr= (m.x28 - m.x69)**2 + (m.x107 - m.x148)**2 + (m.x186
    - m.x227)**2 >= 0.46785600000000005)
m.e1797 = Constraint(expr= (m.x28 - m.x70)**2 + (m.x107 - m.x149)**2 + (m.x186
    - m.x228)**2 >= 0.46785600000000005)
m.e1798 = Constraint(expr= (m.x28 - m.x71)**2 + (m.x107 - m.x150)**2 + (m.x186
    - m.x229)**2 >= 0.46785600000000005)
m.e1799 = Constraint(expr= (m.x28 - m.x72)**2 + (m.x107 - m.x151)**2 + (m.x186
    - m.x230)**2 >= 0.46785600000000005)
m.e1800 = Constraint(expr= (m.x28 - m.x73)**2 + (m.x107 - m.x152)**2 + (m.x186
    - m.x231)**2 >= 0.46785600000000005)
m.e1801 = Constraint(expr= (m.x28 - m.x74)**2 + (m.x107 - m.x153)**2 + (m.x186
    - m.x232)**2 >= 0.46785600000000005)
m.e1802 = Constraint(expr= (m.x28 - m.x75)**2 + (m.x107 - m.x154)**2 + (m.x186
    - m.x233)**2 >= 0.46785600000000005)
m.e1803 = Constraint(expr= (m.x28 - m.x76)**2 + (m.x107 - m.x155)**2 + (m.x186
    - m.x234)**2 >= 0.46785600000000005)
m.e1804 = Constraint(expr= (m.x28 - m.x77)**2 + (m.x107 - m.x156)**2 + (m.x186
    - m.x235)**2 >= 0.46785600000000005)
m.e1805 = Constraint(expr= (m.x28 - m.x78)**2 + (m.x107 - m.x157)**2 + (m.x186
    - m.x236)**2 >= 0.46785600000000005)
m.e1806 = Constraint(expr= (m.x28 - m.x79)**2 + (m.x107 - m.x158)**2 + (m.x186
    - m.x237)**2 >= 0.46785600000000005)
m.e1807 = Constraint(expr= (m.x29 - m.x30)**2 + (m.x108 - m.x109)**2 + (m.x187
    - m.x188)**2 >= 0.46785600000000005)
m.e1808 = Constraint(expr= (m.x29 - m.x31)**2 + (m.x108 - m.x110)**2 + (m.x187
    - m.x189)**2 >= 0.46785600000000005)
m.e1809 = Constraint(expr= (m.x29 - m.x32)**2 + (m.x108 - m.x111)**2 + (m.x187
    - m.x190)**2 >= 0.46785600000000005)
m.e1810 = Constraint(expr= (m.x29 - m.x33)**2 + (m.x108 - m.x112)**2 + (m.x187
    - m.x191)**2 >= 0.46785600000000005)
m.e1811 = Constraint(expr= (m.x29 - m.x34)**2 + (m.x108 - m.x113)**2 + (m.x187
    - m.x192)**2 >= 0.46785600000000005)
m.e1812 = Constraint(expr= (m.x29 - m.x35)**2 + (m.x108 - m.x114)**2 + (m.x187
    - m.x193)**2 >= 0.46785600000000005)
m.e1813 = Constraint(expr= (m.x29 - m.x36)**2 + (m.x108 - m.x115)**2 + (m.x187
    - m.x194)**2 >= 0.46785600000000005)
m.e1814 = Constraint(expr= (m.x29 - m.x37)**2 + (m.x108 - m.x116)**2 + (m.x187
    - m.x195)**2 >= 0.46785600000000005)
m.e1815 = Constraint(expr= (m.x29 - m.x38)**2 + (m.x108 - m.x117)**2 + (m.x187
    - m.x196)**2 >= 0.46785600000000005)
m.e1816 = Constraint(expr= (m.x29 - m.x39)**2 + (m.x108 - m.x118)**2 + (m.x187
    - m.x197)**2 >= 0.46785600000000005)
m.e1817 = Constraint(expr= (m.x29 - m.x40)**2 + (m.x108 - m.x119)**2 + (m.x187
    - m.x198)**2 >= 0.46785600000000005)
m.e1818 = Constraint(expr= (m.x29 - m.x41)**2 + (m.x108 - m.x120)**2 + (m.x187
    - m.x199)**2 >= 0.46785600000000005)
m.e1819 = Constraint(expr= (m.x29 - m.x42)**2 + (m.x108 - m.x121)**2 + (m.x187
    - m.x200)**2 >= 0.46785600000000005)
m.e1820 = Constraint(expr= (m.x29 - m.x43)**2 + (m.x108 - m.x122)**2 + (m.x187
    - m.x201)**2 >= 0.46785600000000005)
m.e1821 = Constraint(expr= (m.x29 - m.x44)**2 + (m.x108 - m.x123)**2 + (m.x187
    - m.x202)**2 >= 0.46785600000000005)
m.e1822 = Constraint(expr= (m.x29 - m.x45)**2 + (m.x108 - m.x124)**2 + (m.x187
    - m.x203)**2 >= 0.46785600000000005)
m.e1823 = Constraint(expr= (m.x29 - m.x46)**2 + (m.x108 - m.x125)**2 + (m.x187
    - m.x204)**2 >= 0.46785600000000005)
m.e1824 = Constraint(expr= (m.x29 - m.x47)**2 + (m.x108 - m.x126)**2 + (m.x187
    - m.x205)**2 >= 0.46785600000000005)
m.e1825 = Constraint(expr= (m.x29 - m.x48)**2 + (m.x108 - m.x127)**2 + (m.x187
    - m.x206)**2 >= 0.46785600000000005)
m.e1826 = Constraint(expr= (m.x29 - m.x49)**2 + (m.x108 - m.x128)**2 + (m.x187
    - m.x207)**2 >= 0.46785600000000005)
m.e1827 = Constraint(expr= (m.x29 - m.x50)**2 + (m.x108 - m.x129)**2 + (m.x187
    - m.x208)**2 >= 0.46785600000000005)
m.e1828 = Constraint(expr= (m.x29 - m.x51)**2 + (m.x108 - m.x130)**2 + (m.x187
    - m.x209)**2 >= 0.46785600000000005)
m.e1829 = Constraint(expr= (m.x29 - m.x52)**2 + (m.x108 - m.x131)**2 + (m.x187
    - m.x210)**2 >= 0.46785600000000005)
m.e1830 = Constraint(expr= (m.x29 - m.x53)**2 + (m.x108 - m.x132)**2 + (m.x187
    - m.x211)**2 >= 0.46785600000000005)
m.e1831 = Constraint(expr= (m.x29 - m.x54)**2 + (m.x108 - m.x133)**2 + (m.x187
    - m.x212)**2 >= 0.46785600000000005)
m.e1832 = Constraint(expr= (m.x29 - m.x55)**2 + (m.x108 - m.x134)**2 + (m.x187
    - m.x213)**2 >= 0.46785600000000005)
m.e1833 = Constraint(expr= (m.x29 - m.x56)**2 + (m.x108 - m.x135)**2 + (m.x187
    - m.x214)**2 >= 0.46785600000000005)
m.e1834 = Constraint(expr= (m.x29 - m.x57)**2 + (m.x108 - m.x136)**2 + (m.x187
    - m.x215)**2 >= 0.46785600000000005)
m.e1835 = Constraint(expr= (m.x29 - m.x58)**2 + (m.x108 - m.x137)**2 + (m.x187
    - m.x216)**2 >= 0.46785600000000005)
m.e1836 = Constraint(expr= (m.x29 - m.x59)**2 + (m.x108 - m.x138)**2 + (m.x187
    - m.x217)**2 >= 0.46785600000000005)
m.e1837 = Constraint(expr= (m.x29 - m.x60)**2 + (m.x108 - m.x139)**2 + (m.x187
    - m.x218)**2 >= 0.46785600000000005)
m.e1838 = Constraint(expr= (m.x29 - m.x61)**2 + (m.x108 - m.x140)**2 + (m.x187
    - m.x219)**2 >= 0.46785600000000005)
m.e1839 = Constraint(expr= (m.x29 - m.x62)**2 + (m.x108 - m.x141)**2 + (m.x187
    - m.x220)**2 >= 0.46785600000000005)
m.e1840 = Constraint(expr= (m.x29 - m.x63)**2 + (m.x108 - m.x142)**2 + (m.x187
    - m.x221)**2 >= 0.46785600000000005)
m.e1841 = Constraint(expr= (m.x29 - m.x64)**2 + (m.x108 - m.x143)**2 + (m.x187
    - m.x222)**2 >= 0.46785600000000005)
m.e1842 = Constraint(expr= (m.x29 - m.x65)**2 + (m.x108 - m.x144)**2 + (m.x187
    - m.x223)**2 >= 0.46785600000000005)
m.e1843 = Constraint(expr= (m.x29 - m.x66)**2 + (m.x108 - m.x145)**2 + (m.x187
    - m.x224)**2 >= 0.46785600000000005)
m.e1844 = Constraint(expr= (m.x29 - m.x67)**2 + (m.x108 - m.x146)**2 + (m.x187
    - m.x225)**2 >= 0.46785600000000005)
m.e1845 = Constraint(expr= (m.x29 - m.x68)**2 + (m.x108 - m.x147)**2 + (m.x187
    - m.x226)**2 >= 0.46785600000000005)
m.e1846 = Constraint(expr= (m.x29 - m.x69)**2 + (m.x108 - m.x148)**2 + (m.x187
    - m.x227)**2 >= 0.46785600000000005)
m.e1847 = Constraint(expr= (m.x29 - m.x70)**2 + (m.x108 - m.x149)**2 + (m.x187
    - m.x228)**2 >= 0.46785600000000005)
m.e1848 = Constraint(expr= (m.x29 - m.x71)**2 + (m.x108 - m.x150)**2 + (m.x187
    - m.x229)**2 >= 0.46785600000000005)
m.e1849 = Constraint(expr= (m.x29 - m.x72)**2 + (m.x108 - m.x151)**2 + (m.x187
    - m.x230)**2 >= 0.46785600000000005)
m.e1850 = Constraint(expr= (m.x29 - m.x73)**2 + (m.x108 - m.x152)**2 + (m.x187
    - m.x231)**2 >= 0.46785600000000005)
m.e1851 = Constraint(expr= (m.x29 - m.x74)**2 + (m.x108 - m.x153)**2 + (m.x187
    - m.x232)**2 >= 0.46785600000000005)
m.e1852 = Constraint(expr= (m.x29 - m.x75)**2 + (m.x108 - m.x154)**2 + (m.x187
    - m.x233)**2 >= 0.46785600000000005)
m.e1853 = Constraint(expr= (m.x29 - m.x76)**2 + (m.x108 - m.x155)**2 + (m.x187
    - m.x234)**2 >= 0.46785600000000005)
m.e1854 = Constraint(expr= (m.x29 - m.x77)**2 + (m.x108 - m.x156)**2 + (m.x187
    - m.x235)**2 >= 0.46785600000000005)
m.e1855 = Constraint(expr= (m.x29 - m.x78)**2 + (m.x108 - m.x157)**2 + (m.x187
    - m.x236)**2 >= 0.46785600000000005)
m.e1856 = Constraint(expr= (m.x29 - m.x79)**2 + (m.x108 - m.x158)**2 + (m.x187
    - m.x237)**2 >= 0.46785600000000005)
m.e1857 = Constraint(expr= (m.x30 - m.x31)**2 + (m.x109 - m.x110)**2 + (m.x188
    - m.x189)**2 >= 0.46785600000000005)
m.e1858 = Constraint(expr= (m.x30 - m.x32)**2 + (m.x109 - m.x111)**2 + (m.x188
    - m.x190)**2 >= 0.46785600000000005)
m.e1859 = Constraint(expr= (m.x30 - m.x33)**2 + (m.x109 - m.x112)**2 + (m.x188
    - m.x191)**2 >= 0.46785600000000005)
m.e1860 = Constraint(expr= (m.x30 - m.x34)**2 + (m.x109 - m.x113)**2 + (m.x188
    - m.x192)**2 >= 0.46785600000000005)
m.e1861 = Constraint(expr= (m.x30 - m.x35)**2 + (m.x109 - m.x114)**2 + (m.x188
    - m.x193)**2 >= 0.46785600000000005)
m.e1862 = Constraint(expr= (m.x30 - m.x36)**2 + (m.x109 - m.x115)**2 + (m.x188
    - m.x194)**2 >= 0.46785600000000005)
m.e1863 = Constraint(expr= (m.x30 - m.x37)**2 + (m.x109 - m.x116)**2 + (m.x188
    - m.x195)**2 >= 0.46785600000000005)
m.e1864 = Constraint(expr= (m.x30 - m.x38)**2 + (m.x109 - m.x117)**2 + (m.x188
    - m.x196)**2 >= 0.46785600000000005)
m.e1865 = Constraint(expr= (m.x30 - m.x39)**2 + (m.x109 - m.x118)**2 + (m.x188
    - m.x197)**2 >= 0.46785600000000005)
m.e1866 = Constraint(expr= (m.x30 - m.x40)**2 + (m.x109 - m.x119)**2 + (m.x188
    - m.x198)**2 >= 0.46785600000000005)
m.e1867 = Constraint(expr= (m.x30 - m.x41)**2 + (m.x109 - m.x120)**2 + (m.x188
    - m.x199)**2 >= 0.46785600000000005)
m.e1868 = Constraint(expr= (m.x30 - m.x42)**2 + (m.x109 - m.x121)**2 + (m.x188
    - m.x200)**2 >= 0.46785600000000005)
m.e1869 = Constraint(expr= (m.x30 - m.x43)**2 + (m.x109 - m.x122)**2 + (m.x188
    - m.x201)**2 >= 0.46785600000000005)
m.e1870 = Constraint(expr= (m.x30 - m.x44)**2 + (m.x109 - m.x123)**2 + (m.x188
    - m.x202)**2 >= 0.46785600000000005)
m.e1871 = Constraint(expr= (m.x30 - m.x45)**2 + (m.x109 - m.x124)**2 + (m.x188
    - m.x203)**2 >= 0.46785600000000005)
m.e1872 = Constraint(expr= (m.x30 - m.x46)**2 + (m.x109 - m.x125)**2 + (m.x188
    - m.x204)**2 >= 0.46785600000000005)
m.e1873 = Constraint(expr= (m.x30 - m.x47)**2 + (m.x109 - m.x126)**2 + (m.x188
    - m.x205)**2 >= 0.46785600000000005)
m.e1874 = Constraint(expr= (m.x30 - m.x48)**2 + (m.x109 - m.x127)**2 + (m.x188
    - m.x206)**2 >= 0.46785600000000005)
m.e1875 = Constraint(expr= (m.x30 - m.x49)**2 + (m.x109 - m.x128)**2 + (m.x188
    - m.x207)**2 >= 0.46785600000000005)
m.e1876 = Constraint(expr= (m.x30 - m.x50)**2 + (m.x109 - m.x129)**2 + (m.x188
    - m.x208)**2 >= 0.46785600000000005)
m.e1877 = Constraint(expr= (m.x30 - m.x51)**2 + (m.x109 - m.x130)**2 + (m.x188
    - m.x209)**2 >= 0.46785600000000005)
m.e1878 = Constraint(expr= (m.x30 - m.x52)**2 + (m.x109 - m.x131)**2 + (m.x188
    - m.x210)**2 >= 0.46785600000000005)
m.e1879 = Constraint(expr= (m.x30 - m.x53)**2 + (m.x109 - m.x132)**2 + (m.x188
    - m.x211)**2 >= 0.46785600000000005)
m.e1880 = Constraint(expr= (m.x30 - m.x54)**2 + (m.x109 - m.x133)**2 + (m.x188
    - m.x212)**2 >= 0.46785600000000005)
m.e1881 = Constraint(expr= (m.x30 - m.x55)**2 + (m.x109 - m.x134)**2 + (m.x188
    - m.x213)**2 >= 0.46785600000000005)
m.e1882 = Constraint(expr= (m.x30 - m.x56)**2 + (m.x109 - m.x135)**2 + (m.x188
    - m.x214)**2 >= 0.46785600000000005)
m.e1883 = Constraint(expr= (m.x30 - m.x57)**2 + (m.x109 - m.x136)**2 + (m.x188
    - m.x215)**2 >= 0.46785600000000005)
m.e1884 = Constraint(expr= (m.x30 - m.x58)**2 + (m.x109 - m.x137)**2 + (m.x188
    - m.x216)**2 >= 0.46785600000000005)
m.e1885 = Constraint(expr= (m.x30 - m.x59)**2 + (m.x109 - m.x138)**2 + (m.x188
    - m.x217)**2 >= 0.46785600000000005)
m.e1886 = Constraint(expr= (m.x30 - m.x60)**2 + (m.x109 - m.x139)**2 + (m.x188
    - m.x218)**2 >= 0.46785600000000005)
m.e1887 = Constraint(expr= (m.x30 - m.x61)**2 + (m.x109 - m.x140)**2 + (m.x188
    - m.x219)**2 >= 0.46785600000000005)
m.e1888 = Constraint(expr= (m.x30 - m.x62)**2 + (m.x109 - m.x141)**2 + (m.x188
    - m.x220)**2 >= 0.46785600000000005)
m.e1889 = Constraint(expr= (m.x30 - m.x63)**2 + (m.x109 - m.x142)**2 + (m.x188
    - m.x221)**2 >= 0.46785600000000005)
m.e1890 = Constraint(expr= (m.x30 - m.x64)**2 + (m.x109 - m.x143)**2 + (m.x188
    - m.x222)**2 >= 0.46785600000000005)
m.e1891 = Constraint(expr= (m.x30 - m.x65)**2 + (m.x109 - m.x144)**2 + (m.x188
    - m.x223)**2 >= 0.46785600000000005)
m.e1892 = Constraint(expr= (m.x30 - m.x66)**2 + (m.x109 - m.x145)**2 + (m.x188
    - m.x224)**2 >= 0.46785600000000005)
m.e1893 = Constraint(expr= (m.x30 - m.x67)**2 + (m.x109 - m.x146)**2 + (m.x188
    - m.x225)**2 >= 0.46785600000000005)
m.e1894 = Constraint(expr= (m.x30 - m.x68)**2 + (m.x109 - m.x147)**2 + (m.x188
    - m.x226)**2 >= 0.46785600000000005)
m.e1895 = Constraint(expr= (m.x30 - m.x69)**2 + (m.x109 - m.x148)**2 + (m.x188
    - m.x227)**2 >= 0.46785600000000005)
m.e1896 = Constraint(expr= (m.x30 - m.x70)**2 + (m.x109 - m.x149)**2 + (m.x188
    - m.x228)**2 >= 0.46785600000000005)
m.e1897 = Constraint(expr= (m.x30 - m.x71)**2 + (m.x109 - m.x150)**2 + (m.x188
    - m.x229)**2 >= 0.46785600000000005)
m.e1898 = Constraint(expr= (m.x30 - m.x72)**2 + (m.x109 - m.x151)**2 + (m.x188
    - m.x230)**2 >= 0.46785600000000005)
m.e1899 = Constraint(expr= (m.x30 - m.x73)**2 + (m.x109 - m.x152)**2 + (m.x188
    - m.x231)**2 >= 0.46785600000000005)
m.e1900 = Constraint(expr= (m.x30 - m.x74)**2 + (m.x109 - m.x153)**2 + (m.x188
    - m.x232)**2 >= 0.46785600000000005)
m.e1901 = Constraint(expr= (m.x30 - m.x75)**2 + (m.x109 - m.x154)**2 + (m.x188
    - m.x233)**2 >= 0.46785600000000005)
m.e1902 = Constraint(expr= (m.x30 - m.x76)**2 + (m.x109 - m.x155)**2 + (m.x188
    - m.x234)**2 >= 0.46785600000000005)
m.e1903 = Constraint(expr= (m.x30 - m.x77)**2 + (m.x109 - m.x156)**2 + (m.x188
    - m.x235)**2 >= 0.46785600000000005)
m.e1904 = Constraint(expr= (m.x30 - m.x78)**2 + (m.x109 - m.x157)**2 + (m.x188
    - m.x236)**2 >= 0.46785600000000005)
m.e1905 = Constraint(expr= (m.x30 - m.x79)**2 + (m.x109 - m.x158)**2 + (m.x188
    - m.x237)**2 >= 0.46785600000000005)
m.e1906 = Constraint(expr= (m.x31 - m.x32)**2 + (m.x110 - m.x111)**2 + (m.x189
    - m.x190)**2 >= 0.46785600000000005)
m.e1907 = Constraint(expr= (m.x31 - m.x33)**2 + (m.x110 - m.x112)**2 + (m.x189
    - m.x191)**2 >= 0.46785600000000005)
m.e1908 = Constraint(expr= (m.x31 - m.x34)**2 + (m.x110 - m.x113)**2 + (m.x189
    - m.x192)**2 >= 0.46785600000000005)
m.e1909 = Constraint(expr= (m.x31 - m.x35)**2 + (m.x110 - m.x114)**2 + (m.x189
    - m.x193)**2 >= 0.46785600000000005)
m.e1910 = Constraint(expr= (m.x31 - m.x36)**2 + (m.x110 - m.x115)**2 + (m.x189
    - m.x194)**2 >= 0.46785600000000005)
m.e1911 = Constraint(expr= (m.x31 - m.x37)**2 + (m.x110 - m.x116)**2 + (m.x189
    - m.x195)**2 >= 0.46785600000000005)
m.e1912 = Constraint(expr= (m.x31 - m.x38)**2 + (m.x110 - m.x117)**2 + (m.x189
    - m.x196)**2 >= 0.46785600000000005)
m.e1913 = Constraint(expr= (m.x31 - m.x39)**2 + (m.x110 - m.x118)**2 + (m.x189
    - m.x197)**2 >= 0.46785600000000005)
m.e1914 = Constraint(expr= (m.x31 - m.x40)**2 + (m.x110 - m.x119)**2 + (m.x189
    - m.x198)**2 >= 0.46785600000000005)
m.e1915 = Constraint(expr= (m.x31 - m.x41)**2 + (m.x110 - m.x120)**2 + (m.x189
    - m.x199)**2 >= 0.46785600000000005)
m.e1916 = Constraint(expr= (m.x31 - m.x42)**2 + (m.x110 - m.x121)**2 + (m.x189
    - m.x200)**2 >= 0.46785600000000005)
m.e1917 = Constraint(expr= (m.x31 - m.x43)**2 + (m.x110 - m.x122)**2 + (m.x189
    - m.x201)**2 >= 0.46785600000000005)
m.e1918 = Constraint(expr= (m.x31 - m.x44)**2 + (m.x110 - m.x123)**2 + (m.x189
    - m.x202)**2 >= 0.46785600000000005)
m.e1919 = Constraint(expr= (m.x31 - m.x45)**2 + (m.x110 - m.x124)**2 + (m.x189
    - m.x203)**2 >= 0.46785600000000005)
m.e1920 = Constraint(expr= (m.x31 - m.x46)**2 + (m.x110 - m.x125)**2 + (m.x189
    - m.x204)**2 >= 0.46785600000000005)
m.e1921 = Constraint(expr= (m.x31 - m.x47)**2 + (m.x110 - m.x126)**2 + (m.x189
    - m.x205)**2 >= 0.46785600000000005)
m.e1922 = Constraint(expr= (m.x31 - m.x48)**2 + (m.x110 - m.x127)**2 + (m.x189
    - m.x206)**2 >= 0.46785600000000005)
m.e1923 = Constraint(expr= (m.x31 - m.x49)**2 + (m.x110 - m.x128)**2 + (m.x189
    - m.x207)**2 >= 0.46785600000000005)
m.e1924 = Constraint(expr= (m.x31 - m.x50)**2 + (m.x110 - m.x129)**2 + (m.x189
    - m.x208)**2 >= 0.46785600000000005)
m.e1925 = Constraint(expr= (m.x31 - m.x51)**2 + (m.x110 - m.x130)**2 + (m.x189
    - m.x209)**2 >= 0.46785600000000005)
m.e1926 = Constraint(expr= (m.x31 - m.x52)**2 + (m.x110 - m.x131)**2 + (m.x189
    - m.x210)**2 >= 0.46785600000000005)
m.e1927 = Constraint(expr= (m.x31 - m.x53)**2 + (m.x110 - m.x132)**2 + (m.x189
    - m.x211)**2 >= 0.46785600000000005)
m.e1928 = Constraint(expr= (m.x31 - m.x54)**2 + (m.x110 - m.x133)**2 + (m.x189
    - m.x212)**2 >= 0.46785600000000005)
m.e1929 = Constraint(expr= (m.x31 - m.x55)**2 + (m.x110 - m.x134)**2 + (m.x189
    - m.x213)**2 >= 0.46785600000000005)
m.e1930 = Constraint(expr= (m.x31 - m.x56)**2 + (m.x110 - m.x135)**2 + (m.x189
    - m.x214)**2 >= 0.46785600000000005)
m.e1931 = Constraint(expr= (m.x31 - m.x57)**2 + (m.x110 - m.x136)**2 + (m.x189
    - m.x215)**2 >= 0.46785600000000005)
m.e1932 = Constraint(expr= (m.x31 - m.x58)**2 + (m.x110 - m.x137)**2 + (m.x189
    - m.x216)**2 >= 0.46785600000000005)
m.e1933 = Constraint(expr= (m.x31 - m.x59)**2 + (m.x110 - m.x138)**2 + (m.x189
    - m.x217)**2 >= 0.46785600000000005)
m.e1934 = Constraint(expr= (m.x31 - m.x60)**2 + (m.x110 - m.x139)**2 + (m.x189
    - m.x218)**2 >= 0.46785600000000005)
m.e1935 = Constraint(expr= (m.x31 - m.x61)**2 + (m.x110 - m.x140)**2 + (m.x189
    - m.x219)**2 >= 0.46785600000000005)
m.e1936 = Constraint(expr= (m.x31 - m.x62)**2 + (m.x110 - m.x141)**2 + (m.x189
    - m.x220)**2 >= 0.46785600000000005)
m.e1937 = Constraint(expr= (m.x31 - m.x63)**2 + (m.x110 - m.x142)**2 + (m.x189
    - m.x221)**2 >= 0.46785600000000005)
m.e1938 = Constraint(expr= (m.x31 - m.x64)**2 + (m.x110 - m.x143)**2 + (m.x189
    - m.x222)**2 >= 0.46785600000000005)
m.e1939 = Constraint(expr= (m.x31 - m.x65)**2 + (m.x110 - m.x144)**2 + (m.x189
    - m.x223)**2 >= 0.46785600000000005)
m.e1940 = Constraint(expr= (m.x31 - m.x66)**2 + (m.x110 - m.x145)**2 + (m.x189
    - m.x224)**2 >= 0.46785600000000005)
m.e1941 = Constraint(expr= (m.x31 - m.x67)**2 + (m.x110 - m.x146)**2 + (m.x189
    - m.x225)**2 >= 0.46785600000000005)
m.e1942 = Constraint(expr= (m.x31 - m.x68)**2 + (m.x110 - m.x147)**2 + (m.x189
    - m.x226)**2 >= 0.46785600000000005)
m.e1943 = Constraint(expr= (m.x31 - m.x69)**2 + (m.x110 - m.x148)**2 + (m.x189
    - m.x227)**2 >= 0.46785600000000005)
m.e1944 = Constraint(expr= (m.x31 - m.x70)**2 + (m.x110 - m.x149)**2 + (m.x189
    - m.x228)**2 >= 0.46785600000000005)
m.e1945 = Constraint(expr= (m.x31 - m.x71)**2 + (m.x110 - m.x150)**2 + (m.x189
    - m.x229)**2 >= 0.46785600000000005)
m.e1946 = Constraint(expr= (m.x31 - m.x72)**2 + (m.x110 - m.x151)**2 + (m.x189
    - m.x230)**2 >= 0.46785600000000005)
m.e1947 = Constraint(expr= (m.x31 - m.x73)**2 + (m.x110 - m.x152)**2 + (m.x189
    - m.x231)**2 >= 0.46785600000000005)
m.e1948 = Constraint(expr= (m.x31 - m.x74)**2 + (m.x110 - m.x153)**2 + (m.x189
    - m.x232)**2 >= 0.46785600000000005)
m.e1949 = Constraint(expr= (m.x31 - m.x75)**2 + (m.x110 - m.x154)**2 + (m.x189
    - m.x233)**2 >= 0.46785600000000005)
m.e1950 = Constraint(expr= (m.x31 - m.x76)**2 + (m.x110 - m.x155)**2 + (m.x189
    - m.x234)**2 >= 0.46785600000000005)
m.e1951 = Constraint(expr= (m.x31 - m.x77)**2 + (m.x110 - m.x156)**2 + (m.x189
    - m.x235)**2 >= 0.46785600000000005)
m.e1952 = Constraint(expr= (m.x31 - m.x78)**2 + (m.x110 - m.x157)**2 + (m.x189
    - m.x236)**2 >= 0.46785600000000005)
m.e1953 = Constraint(expr= (m.x31 - m.x79)**2 + (m.x110 - m.x158)**2 + (m.x189
    - m.x237)**2 >= 0.46785600000000005)
m.e1954 = Constraint(expr= (m.x32 - m.x33)**2 + (m.x111 - m.x112)**2 + (m.x190
    - m.x191)**2 >= 0.46785600000000005)
m.e1955 = Constraint(expr= (m.x32 - m.x34)**2 + (m.x111 - m.x113)**2 + (m.x190
    - m.x192)**2 >= 0.46785600000000005)
m.e1956 = Constraint(expr= (m.x32 - m.x35)**2 + (m.x111 - m.x114)**2 + (m.x190
    - m.x193)**2 >= 0.46785600000000005)
m.e1957 = Constraint(expr= (m.x32 - m.x36)**2 + (m.x111 - m.x115)**2 + (m.x190
    - m.x194)**2 >= 0.46785600000000005)
m.e1958 = Constraint(expr= (m.x32 - m.x37)**2 + (m.x111 - m.x116)**2 + (m.x190
    - m.x195)**2 >= 0.46785600000000005)
m.e1959 = Constraint(expr= (m.x32 - m.x38)**2 + (m.x111 - m.x117)**2 + (m.x190
    - m.x196)**2 >= 0.46785600000000005)
m.e1960 = Constraint(expr= (m.x32 - m.x39)**2 + (m.x111 - m.x118)**2 + (m.x190
    - m.x197)**2 >= 0.46785600000000005)
m.e1961 = Constraint(expr= (m.x32 - m.x40)**2 + (m.x111 - m.x119)**2 + (m.x190
    - m.x198)**2 >= 0.46785600000000005)
m.e1962 = Constraint(expr= (m.x32 - m.x41)**2 + (m.x111 - m.x120)**2 + (m.x190
    - m.x199)**2 >= 0.46785600000000005)
m.e1963 = Constraint(expr= (m.x32 - m.x42)**2 + (m.x111 - m.x121)**2 + (m.x190
    - m.x200)**2 >= 0.46785600000000005)
m.e1964 = Constraint(expr= (m.x32 - m.x43)**2 + (m.x111 - m.x122)**2 + (m.x190
    - m.x201)**2 >= 0.46785600000000005)
m.e1965 = Constraint(expr= (m.x32 - m.x44)**2 + (m.x111 - m.x123)**2 + (m.x190
    - m.x202)**2 >= 0.46785600000000005)
m.e1966 = Constraint(expr= (m.x32 - m.x45)**2 + (m.x111 - m.x124)**2 + (m.x190
    - m.x203)**2 >= 0.46785600000000005)
m.e1967 = Constraint(expr= (m.x32 - m.x46)**2 + (m.x111 - m.x125)**2 + (m.x190
    - m.x204)**2 >= 0.46785600000000005)
m.e1968 = Constraint(expr= (m.x32 - m.x47)**2 + (m.x111 - m.x126)**2 + (m.x190
    - m.x205)**2 >= 0.46785600000000005)
m.e1969 = Constraint(expr= (m.x32 - m.x48)**2 + (m.x111 - m.x127)**2 + (m.x190
    - m.x206)**2 >= 0.46785600000000005)
m.e1970 = Constraint(expr= (m.x32 - m.x49)**2 + (m.x111 - m.x128)**2 + (m.x190
    - m.x207)**2 >= 0.46785600000000005)
m.e1971 = Constraint(expr= (m.x32 - m.x50)**2 + (m.x111 - m.x129)**2 + (m.x190
    - m.x208)**2 >= 0.46785600000000005)
m.e1972 = Constraint(expr= (m.x32 - m.x51)**2 + (m.x111 - m.x130)**2 + (m.x190
    - m.x209)**2 >= 0.46785600000000005)
m.e1973 = Constraint(expr= (m.x32 - m.x52)**2 + (m.x111 - m.x131)**2 + (m.x190
    - m.x210)**2 >= 0.46785600000000005)
m.e1974 = Constraint(expr= (m.x32 - m.x53)**2 + (m.x111 - m.x132)**2 + (m.x190
    - m.x211)**2 >= 0.46785600000000005)
m.e1975 = Constraint(expr= (m.x32 - m.x54)**2 + (m.x111 - m.x133)**2 + (m.x190
    - m.x212)**2 >= 0.46785600000000005)
m.e1976 = Constraint(expr= (m.x32 - m.x55)**2 + (m.x111 - m.x134)**2 + (m.x190
    - m.x213)**2 >= 0.46785600000000005)
m.e1977 = Constraint(expr= (m.x32 - m.x56)**2 + (m.x111 - m.x135)**2 + (m.x190
    - m.x214)**2 >= 0.46785600000000005)
m.e1978 = Constraint(expr= (m.x32 - m.x57)**2 + (m.x111 - m.x136)**2 + (m.x190
    - m.x215)**2 >= 0.46785600000000005)
m.e1979 = Constraint(expr= (m.x32 - m.x58)**2 + (m.x111 - m.x137)**2 + (m.x190
    - m.x216)**2 >= 0.46785600000000005)
m.e1980 = Constraint(expr= (m.x32 - m.x59)**2 + (m.x111 - m.x138)**2 + (m.x190
    - m.x217)**2 >= 0.46785600000000005)
m.e1981 = Constraint(expr= (m.x32 - m.x60)**2 + (m.x111 - m.x139)**2 + (m.x190
    - m.x218)**2 >= 0.46785600000000005)
m.e1982 = Constraint(expr= (m.x32 - m.x61)**2 + (m.x111 - m.x140)**2 + (m.x190
    - m.x219)**2 >= 0.46785600000000005)
m.e1983 = Constraint(expr= (m.x32 - m.x62)**2 + (m.x111 - m.x141)**2 + (m.x190
    - m.x220)**2 >= 0.46785600000000005)
m.e1984 = Constraint(expr= (m.x32 - m.x63)**2 + (m.x111 - m.x142)**2 + (m.x190
    - m.x221)**2 >= 0.46785600000000005)
m.e1985 = Constraint(expr= (m.x32 - m.x64)**2 + (m.x111 - m.x143)**2 + (m.x190
    - m.x222)**2 >= 0.46785600000000005)
m.e1986 = Constraint(expr= (m.x32 - m.x65)**2 + (m.x111 - m.x144)**2 + (m.x190
    - m.x223)**2 >= 0.46785600000000005)
m.e1987 = Constraint(expr= (m.x32 - m.x66)**2 + (m.x111 - m.x145)**2 + (m.x190
    - m.x224)**2 >= 0.46785600000000005)
m.e1988 = Constraint(expr= (m.x32 - m.x67)**2 + (m.x111 - m.x146)**2 + (m.x190
    - m.x225)**2 >= 0.46785600000000005)
m.e1989 = Constraint(expr= (m.x32 - m.x68)**2 + (m.x111 - m.x147)**2 + (m.x190
    - m.x226)**2 >= 0.46785600000000005)
m.e1990 = Constraint(expr= (m.x32 - m.x69)**2 + (m.x111 - m.x148)**2 + (m.x190
    - m.x227)**2 >= 0.46785600000000005)
m.e1991 = Constraint(expr= (m.x32 - m.x70)**2 + (m.x111 - m.x149)**2 + (m.x190
    - m.x228)**2 >= 0.46785600000000005)
m.e1992 = Constraint(expr= (m.x32 - m.x71)**2 + (m.x111 - m.x150)**2 + (m.x190
    - m.x229)**2 >= 0.46785600000000005)
m.e1993 = Constraint(expr= (m.x32 - m.x72)**2 + (m.x111 - m.x151)**2 + (m.x190
    - m.x230)**2 >= 0.46785600000000005)
m.e1994 = Constraint(expr= (m.x32 - m.x73)**2 + (m.x111 - m.x152)**2 + (m.x190
    - m.x231)**2 >= 0.46785600000000005)
m.e1995 = Constraint(expr= (m.x32 - m.x74)**2 + (m.x111 - m.x153)**2 + (m.x190
    - m.x232)**2 >= 0.46785600000000005)
m.e1996 = Constraint(expr= (m.x32 - m.x75)**2 + (m.x111 - m.x154)**2 + (m.x190
    - m.x233)**2 >= 0.46785600000000005)
m.e1997 = Constraint(expr= (m.x32 - m.x76)**2 + (m.x111 - m.x155)**2 + (m.x190
    - m.x234)**2 >= 0.46785600000000005)
m.e1998 = Constraint(expr= (m.x32 - m.x77)**2 + (m.x111 - m.x156)**2 + (m.x190
    - m.x235)**2 >= 0.46785600000000005)
m.e1999 = Constraint(expr= (m.x32 - m.x78)**2 + (m.x111 - m.x157)**2 + (m.x190
    - m.x236)**2 >= 0.46785600000000005)
m.e2000 = Constraint(expr= (m.x32 - m.x79)**2 + (m.x111 - m.x158)**2 + (m.x190
    - m.x237)**2 >= 0.46785600000000005)
m.e2001 = Constraint(expr= (m.x33 - m.x34)**2 + (m.x112 - m.x113)**2 + (m.x191
    - m.x192)**2 >= 0.46785600000000005)
m.e2002 = Constraint(expr= (m.x33 - m.x35)**2 + (m.x112 - m.x114)**2 + (m.x191
    - m.x193)**2 >= 0.46785600000000005)
m.e2003 = Constraint(expr= (m.x33 - m.x36)**2 + (m.x112 - m.x115)**2 + (m.x191
    - m.x194)**2 >= 0.46785600000000005)
m.e2004 = Constraint(expr= (m.x33 - m.x37)**2 + (m.x112 - m.x116)**2 + (m.x191
    - m.x195)**2 >= 0.46785600000000005)
m.e2005 = Constraint(expr= (m.x33 - m.x38)**2 + (m.x112 - m.x117)**2 + (m.x191
    - m.x196)**2 >= 0.46785600000000005)
m.e2006 = Constraint(expr= (m.x33 - m.x39)**2 + (m.x112 - m.x118)**2 + (m.x191
    - m.x197)**2 >= 0.46785600000000005)
m.e2007 = Constraint(expr= (m.x33 - m.x40)**2 + (m.x112 - m.x119)**2 + (m.x191
    - m.x198)**2 >= 0.46785600000000005)
m.e2008 = Constraint(expr= (m.x33 - m.x41)**2 + (m.x112 - m.x120)**2 + (m.x191
    - m.x199)**2 >= 0.46785600000000005)
m.e2009 = Constraint(expr= (m.x33 - m.x42)**2 + (m.x112 - m.x121)**2 + (m.x191
    - m.x200)**2 >= 0.46785600000000005)
m.e2010 = Constraint(expr= (m.x33 - m.x43)**2 + (m.x112 - m.x122)**2 + (m.x191
    - m.x201)**2 >= 0.46785600000000005)
m.e2011 = Constraint(expr= (m.x33 - m.x44)**2 + (m.x112 - m.x123)**2 + (m.x191
    - m.x202)**2 >= 0.46785600000000005)
m.e2012 = Constraint(expr= (m.x33 - m.x45)**2 + (m.x112 - m.x124)**2 + (m.x191
    - m.x203)**2 >= 0.46785600000000005)
m.e2013 = Constraint(expr= (m.x33 - m.x46)**2 + (m.x112 - m.x125)**2 + (m.x191
    - m.x204)**2 >= 0.46785600000000005)
m.e2014 = Constraint(expr= (m.x33 - m.x47)**2 + (m.x112 - m.x126)**2 + (m.x191
    - m.x205)**2 >= 0.46785600000000005)
m.e2015 = Constraint(expr= (m.x33 - m.x48)**2 + (m.x112 - m.x127)**2 + (m.x191
    - m.x206)**2 >= 0.46785600000000005)
m.e2016 = Constraint(expr= (m.x33 - m.x49)**2 + (m.x112 - m.x128)**2 + (m.x191
    - m.x207)**2 >= 0.46785600000000005)
m.e2017 = Constraint(expr= (m.x33 - m.x50)**2 + (m.x112 - m.x129)**2 + (m.x191
    - m.x208)**2 >= 0.46785600000000005)
m.e2018 = Constraint(expr= (m.x33 - m.x51)**2 + (m.x112 - m.x130)**2 + (m.x191
    - m.x209)**2 >= 0.46785600000000005)
m.e2019 = Constraint(expr= (m.x33 - m.x52)**2 + (m.x112 - m.x131)**2 + (m.x191
    - m.x210)**2 >= 0.46785600000000005)
m.e2020 = Constraint(expr= (m.x33 - m.x53)**2 + (m.x112 - m.x132)**2 + (m.x191
    - m.x211)**2 >= 0.46785600000000005)
m.e2021 = Constraint(expr= (m.x33 - m.x54)**2 + (m.x112 - m.x133)**2 + (m.x191
    - m.x212)**2 >= 0.46785600000000005)
m.e2022 = Constraint(expr= (m.x33 - m.x55)**2 + (m.x112 - m.x134)**2 + (m.x191
    - m.x213)**2 >= 0.46785600000000005)
m.e2023 = Constraint(expr= (m.x33 - m.x56)**2 + (m.x112 - m.x135)**2 + (m.x191
    - m.x214)**2 >= 0.46785600000000005)
m.e2024 = Constraint(expr= (m.x33 - m.x57)**2 + (m.x112 - m.x136)**2 + (m.x191
    - m.x215)**2 >= 0.46785600000000005)
m.e2025 = Constraint(expr= (m.x33 - m.x58)**2 + (m.x112 - m.x137)**2 + (m.x191
    - m.x216)**2 >= 0.46785600000000005)
m.e2026 = Constraint(expr= (m.x33 - m.x59)**2 + (m.x112 - m.x138)**2 + (m.x191
    - m.x217)**2 >= 0.46785600000000005)
m.e2027 = Constraint(expr= (m.x33 - m.x60)**2 + (m.x112 - m.x139)**2 + (m.x191
    - m.x218)**2 >= 0.46785600000000005)
m.e2028 = Constraint(expr= (m.x33 - m.x61)**2 + (m.x112 - m.x140)**2 + (m.x191
    - m.x219)**2 >= 0.46785600000000005)
m.e2029 = Constraint(expr= (m.x33 - m.x62)**2 + (m.x112 - m.x141)**2 + (m.x191
    - m.x220)**2 >= 0.46785600000000005)
m.e2030 = Constraint(expr= (m.x33 - m.x63)**2 + (m.x112 - m.x142)**2 + (m.x191
    - m.x221)**2 >= 0.46785600000000005)
m.e2031 = Constraint(expr= (m.x33 - m.x64)**2 + (m.x112 - m.x143)**2 + (m.x191
    - m.x222)**2 >= 0.46785600000000005)
m.e2032 = Constraint(expr= (m.x33 - m.x65)**2 + (m.x112 - m.x144)**2 + (m.x191
    - m.x223)**2 >= 0.46785600000000005)
m.e2033 = Constraint(expr= (m.x33 - m.x66)**2 + (m.x112 - m.x145)**2 + (m.x191
    - m.x224)**2 >= 0.46785600000000005)
m.e2034 = Constraint(expr= (m.x33 - m.x67)**2 + (m.x112 - m.x146)**2 + (m.x191
    - m.x225)**2 >= 0.46785600000000005)
m.e2035 = Constraint(expr= (m.x33 - m.x68)**2 + (m.x112 - m.x147)**2 + (m.x191
    - m.x226)**2 >= 0.46785600000000005)
m.e2036 = Constraint(expr= (m.x33 - m.x69)**2 + (m.x112 - m.x148)**2 + (m.x191
    - m.x227)**2 >= 0.46785600000000005)
m.e2037 = Constraint(expr= (m.x33 - m.x70)**2 + (m.x112 - m.x149)**2 + (m.x191
    - m.x228)**2 >= 0.46785600000000005)
m.e2038 = Constraint(expr= (m.x33 - m.x71)**2 + (m.x112 - m.x150)**2 + (m.x191
    - m.x229)**2 >= 0.46785600000000005)
m.e2039 = Constraint(expr= (m.x33 - m.x72)**2 + (m.x112 - m.x151)**2 + (m.x191
    - m.x230)**2 >= 0.46785600000000005)
m.e2040 = Constraint(expr= (m.x33 - m.x73)**2 + (m.x112 - m.x152)**2 + (m.x191
    - m.x231)**2 >= 0.46785600000000005)
m.e2041 = Constraint(expr= (m.x33 - m.x74)**2 + (m.x112 - m.x153)**2 + (m.x191
    - m.x232)**2 >= 0.46785600000000005)
m.e2042 = Constraint(expr= (m.x33 - m.x75)**2 + (m.x112 - m.x154)**2 + (m.x191
    - m.x233)**2 >= 0.46785600000000005)
m.e2043 = Constraint(expr= (m.x33 - m.x76)**2 + (m.x112 - m.x155)**2 + (m.x191
    - m.x234)**2 >= 0.46785600000000005)
m.e2044 = Constraint(expr= (m.x33 - m.x77)**2 + (m.x112 - m.x156)**2 + (m.x191
    - m.x235)**2 >= 0.46785600000000005)
m.e2045 = Constraint(expr= (m.x33 - m.x78)**2 + (m.x112 - m.x157)**2 + (m.x191
    - m.x236)**2 >= 0.46785600000000005)
m.e2046 = Constraint(expr= (m.x33 - m.x79)**2 + (m.x112 - m.x158)**2 + (m.x191
    - m.x237)**2 >= 0.46785600000000005)
m.e2047 = Constraint(expr= (m.x34 - m.x35)**2 + (m.x113 - m.x114)**2 + (m.x192
    - m.x193)**2 >= 0.46785600000000005)
m.e2048 = Constraint(expr= (m.x34 - m.x36)**2 + (m.x113 - m.x115)**2 + (m.x192
    - m.x194)**2 >= 0.46785600000000005)
m.e2049 = Constraint(expr= (m.x34 - m.x37)**2 + (m.x113 - m.x116)**2 + (m.x192
    - m.x195)**2 >= 0.46785600000000005)
m.e2050 = Constraint(expr= (m.x34 - m.x38)**2 + (m.x113 - m.x117)**2 + (m.x192
    - m.x196)**2 >= 0.46785600000000005)
m.e2051 = Constraint(expr= (m.x34 - m.x39)**2 + (m.x113 - m.x118)**2 + (m.x192
    - m.x197)**2 >= 0.46785600000000005)
m.e2052 = Constraint(expr= (m.x34 - m.x40)**2 + (m.x113 - m.x119)**2 + (m.x192
    - m.x198)**2 >= 0.46785600000000005)
m.e2053 = Constraint(expr= (m.x34 - m.x41)**2 + (m.x113 - m.x120)**2 + (m.x192
    - m.x199)**2 >= 0.46785600000000005)
m.e2054 = Constraint(expr= (m.x34 - m.x42)**2 + (m.x113 - m.x121)**2 + (m.x192
    - m.x200)**2 >= 0.46785600000000005)
m.e2055 = Constraint(expr= (m.x34 - m.x43)**2 + (m.x113 - m.x122)**2 + (m.x192
    - m.x201)**2 >= 0.46785600000000005)
m.e2056 = Constraint(expr= (m.x34 - m.x44)**2 + (m.x113 - m.x123)**2 + (m.x192
    - m.x202)**2 >= 0.46785600000000005)
m.e2057 = Constraint(expr= (m.x34 - m.x45)**2 + (m.x113 - m.x124)**2 + (m.x192
    - m.x203)**2 >= 0.46785600000000005)
m.e2058 = Constraint(expr= (m.x34 - m.x46)**2 + (m.x113 - m.x125)**2 + (m.x192
    - m.x204)**2 >= 0.46785600000000005)
m.e2059 = Constraint(expr= (m.x34 - m.x47)**2 + (m.x113 - m.x126)**2 + (m.x192
    - m.x205)**2 >= 0.46785600000000005)
m.e2060 = Constraint(expr= (m.x34 - m.x48)**2 + (m.x113 - m.x127)**2 + (m.x192
    - m.x206)**2 >= 0.46785600000000005)
m.e2061 = Constraint(expr= (m.x34 - m.x49)**2 + (m.x113 - m.x128)**2 + (m.x192
    - m.x207)**2 >= 0.46785600000000005)
m.e2062 = Constraint(expr= (m.x34 - m.x50)**2 + (m.x113 - m.x129)**2 + (m.x192
    - m.x208)**2 >= 0.46785600000000005)
m.e2063 = Constraint(expr= (m.x34 - m.x51)**2 + (m.x113 - m.x130)**2 + (m.x192
    - m.x209)**2 >= 0.46785600000000005)
m.e2064 = Constraint(expr= (m.x34 - m.x52)**2 + (m.x113 - m.x131)**2 + (m.x192
    - m.x210)**2 >= 0.46785600000000005)
m.e2065 = Constraint(expr= (m.x34 - m.x53)**2 + (m.x113 - m.x132)**2 + (m.x192
    - m.x211)**2 >= 0.46785600000000005)
m.e2066 = Constraint(expr= (m.x34 - m.x54)**2 + (m.x113 - m.x133)**2 + (m.x192
    - m.x212)**2 >= 0.46785600000000005)
m.e2067 = Constraint(expr= (m.x34 - m.x55)**2 + (m.x113 - m.x134)**2 + (m.x192
    - m.x213)**2 >= 0.46785600000000005)
m.e2068 = Constraint(expr= (m.x34 - m.x56)**2 + (m.x113 - m.x135)**2 + (m.x192
    - m.x214)**2 >= 0.46785600000000005)
m.e2069 = Constraint(expr= (m.x34 - m.x57)**2 + (m.x113 - m.x136)**2 + (m.x192
    - m.x215)**2 >= 0.46785600000000005)
m.e2070 = Constraint(expr= (m.x34 - m.x58)**2 + (m.x113 - m.x137)**2 + (m.x192
    - m.x216)**2 >= 0.46785600000000005)
m.e2071 = Constraint(expr= (m.x34 - m.x59)**2 + (m.x113 - m.x138)**2 + (m.x192
    - m.x217)**2 >= 0.46785600000000005)
m.e2072 = Constraint(expr= (m.x34 - m.x60)**2 + (m.x113 - m.x139)**2 + (m.x192
    - m.x218)**2 >= 0.46785600000000005)
m.e2073 = Constraint(expr= (m.x34 - m.x61)**2 + (m.x113 - m.x140)**2 + (m.x192
    - m.x219)**2 >= 0.46785600000000005)
m.e2074 = Constraint(expr= (m.x34 - m.x62)**2 + (m.x113 - m.x141)**2 + (m.x192
    - m.x220)**2 >= 0.46785600000000005)
m.e2075 = Constraint(expr= (m.x34 - m.x63)**2 + (m.x113 - m.x142)**2 + (m.x192
    - m.x221)**2 >= 0.46785600000000005)
m.e2076 = Constraint(expr= (m.x34 - m.x64)**2 + (m.x113 - m.x143)**2 + (m.x192
    - m.x222)**2 >= 0.46785600000000005)
m.e2077 = Constraint(expr= (m.x34 - m.x65)**2 + (m.x113 - m.x144)**2 + (m.x192
    - m.x223)**2 >= 0.46785600000000005)
m.e2078 = Constraint(expr= (m.x34 - m.x66)**2 + (m.x113 - m.x145)**2 + (m.x192
    - m.x224)**2 >= 0.46785600000000005)
m.e2079 = Constraint(expr= (m.x34 - m.x67)**2 + (m.x113 - m.x146)**2 + (m.x192
    - m.x225)**2 >= 0.46785600000000005)
m.e2080 = Constraint(expr= (m.x34 - m.x68)**2 + (m.x113 - m.x147)**2 + (m.x192
    - m.x226)**2 >= 0.46785600000000005)
m.e2081 = Constraint(expr= (m.x34 - m.x69)**2 + (m.x113 - m.x148)**2 + (m.x192
    - m.x227)**2 >= 0.46785600000000005)
m.e2082 = Constraint(expr= (m.x34 - m.x70)**2 + (m.x113 - m.x149)**2 + (m.x192
    - m.x228)**2 >= 0.46785600000000005)
m.e2083 = Constraint(expr= (m.x34 - m.x71)**2 + (m.x113 - m.x150)**2 + (m.x192
    - m.x229)**2 >= 0.46785600000000005)
m.e2084 = Constraint(expr= (m.x34 - m.x72)**2 + (m.x113 - m.x151)**2 + (m.x192
    - m.x230)**2 >= 0.46785600000000005)
m.e2085 = Constraint(expr= (m.x34 - m.x73)**2 + (m.x113 - m.x152)**2 + (m.x192
    - m.x231)**2 >= 0.46785600000000005)
m.e2086 = Constraint(expr= (m.x34 - m.x74)**2 + (m.x113 - m.x153)**2 + (m.x192
    - m.x232)**2 >= 0.46785600000000005)
m.e2087 = Constraint(expr= (m.x34 - m.x75)**2 + (m.x113 - m.x154)**2 + (m.x192
    - m.x233)**2 >= 0.46785600000000005)
m.e2088 = Constraint(expr= (m.x34 - m.x76)**2 + (m.x113 - m.x155)**2 + (m.x192
    - m.x234)**2 >= 0.46785600000000005)
m.e2089 = Constraint(expr= (m.x34 - m.x77)**2 + (m.x113 - m.x156)**2 + (m.x192
    - m.x235)**2 >= 0.46785600000000005)
m.e2090 = Constraint(expr= (m.x34 - m.x78)**2 + (m.x113 - m.x157)**2 + (m.x192
    - m.x236)**2 >= 0.46785600000000005)
m.e2091 = Constraint(expr= (m.x34 - m.x79)**2 + (m.x113 - m.x158)**2 + (m.x192
    - m.x237)**2 >= 0.46785600000000005)
m.e2092 = Constraint(expr= (m.x35 - m.x36)**2 + (m.x114 - m.x115)**2 + (m.x193
    - m.x194)**2 >= 0.46785600000000005)
m.e2093 = Constraint(expr= (m.x35 - m.x37)**2 + (m.x114 - m.x116)**2 + (m.x193
    - m.x195)**2 >= 0.46785600000000005)
m.e2094 = Constraint(expr= (m.x35 - m.x38)**2 + (m.x114 - m.x117)**2 + (m.x193
    - m.x196)**2 >= 0.46785600000000005)
m.e2095 = Constraint(expr= (m.x35 - m.x39)**2 + (m.x114 - m.x118)**2 + (m.x193
    - m.x197)**2 >= 0.46785600000000005)
m.e2096 = Constraint(expr= (m.x35 - m.x40)**2 + (m.x114 - m.x119)**2 + (m.x193
    - m.x198)**2 >= 0.46785600000000005)
m.e2097 = Constraint(expr= (m.x35 - m.x41)**2 + (m.x114 - m.x120)**2 + (m.x193
    - m.x199)**2 >= 0.46785600000000005)
m.e2098 = Constraint(expr= (m.x35 - m.x42)**2 + (m.x114 - m.x121)**2 + (m.x193
    - m.x200)**2 >= 0.46785600000000005)
m.e2099 = Constraint(expr= (m.x35 - m.x43)**2 + (m.x114 - m.x122)**2 + (m.x193
    - m.x201)**2 >= 0.46785600000000005)
m.e2100 = Constraint(expr= (m.x35 - m.x44)**2 + (m.x114 - m.x123)**2 + (m.x193
    - m.x202)**2 >= 0.46785600000000005)
m.e2101 = Constraint(expr= (m.x35 - m.x45)**2 + (m.x114 - m.x124)**2 + (m.x193
    - m.x203)**2 >= 0.46785600000000005)
m.e2102 = Constraint(expr= (m.x35 - m.x46)**2 + (m.x114 - m.x125)**2 + (m.x193
    - m.x204)**2 >= 0.46785600000000005)
m.e2103 = Constraint(expr= (m.x35 - m.x47)**2 + (m.x114 - m.x126)**2 + (m.x193
    - m.x205)**2 >= 0.46785600000000005)
m.e2104 = Constraint(expr= (m.x35 - m.x48)**2 + (m.x114 - m.x127)**2 + (m.x193
    - m.x206)**2 >= 0.46785600000000005)
m.e2105 = Constraint(expr= (m.x35 - m.x49)**2 + (m.x114 - m.x128)**2 + (m.x193
    - m.x207)**2 >= 0.46785600000000005)
m.e2106 = Constraint(expr= (m.x35 - m.x50)**2 + (m.x114 - m.x129)**2 + (m.x193
    - m.x208)**2 >= 0.46785600000000005)
m.e2107 = Constraint(expr= (m.x35 - m.x51)**2 + (m.x114 - m.x130)**2 + (m.x193
    - m.x209)**2 >= 0.46785600000000005)
m.e2108 = Constraint(expr= (m.x35 - m.x52)**2 + (m.x114 - m.x131)**2 + (m.x193
    - m.x210)**2 >= 0.46785600000000005)
m.e2109 = Constraint(expr= (m.x35 - m.x53)**2 + (m.x114 - m.x132)**2 + (m.x193
    - m.x211)**2 >= 0.46785600000000005)
m.e2110 = Constraint(expr= (m.x35 - m.x54)**2 + (m.x114 - m.x133)**2 + (m.x193
    - m.x212)**2 >= 0.46785600000000005)
m.e2111 = Constraint(expr= (m.x35 - m.x55)**2 + (m.x114 - m.x134)**2 + (m.x193
    - m.x213)**2 >= 0.46785600000000005)
m.e2112 = Constraint(expr= (m.x35 - m.x56)**2 + (m.x114 - m.x135)**2 + (m.x193
    - m.x214)**2 >= 0.46785600000000005)
m.e2113 = Constraint(expr= (m.x35 - m.x57)**2 + (m.x114 - m.x136)**2 + (m.x193
    - m.x215)**2 >= 0.46785600000000005)
m.e2114 = Constraint(expr= (m.x35 - m.x58)**2 + (m.x114 - m.x137)**2 + (m.x193
    - m.x216)**2 >= 0.46785600000000005)
m.e2115 = Constraint(expr= (m.x35 - m.x59)**2 + (m.x114 - m.x138)**2 + (m.x193
    - m.x217)**2 >= 0.46785600000000005)
m.e2116 = Constraint(expr= (m.x35 - m.x60)**2 + (m.x114 - m.x139)**2 + (m.x193
    - m.x218)**2 >= 0.46785600000000005)
m.e2117 = Constraint(expr= (m.x35 - m.x61)**2 + (m.x114 - m.x140)**2 + (m.x193
    - m.x219)**2 >= 0.46785600000000005)
m.e2118 = Constraint(expr= (m.x35 - m.x62)**2 + (m.x114 - m.x141)**2 + (m.x193
    - m.x220)**2 >= 0.46785600000000005)
m.e2119 = Constraint(expr= (m.x35 - m.x63)**2 + (m.x114 - m.x142)**2 + (m.x193
    - m.x221)**2 >= 0.46785600000000005)
m.e2120 = Constraint(expr= (m.x35 - m.x64)**2 + (m.x114 - m.x143)**2 + (m.x193
    - m.x222)**2 >= 0.46785600000000005)
m.e2121 = Constraint(expr= (m.x35 - m.x65)**2 + (m.x114 - m.x144)**2 + (m.x193
    - m.x223)**2 >= 0.46785600000000005)
m.e2122 = Constraint(expr= (m.x35 - m.x66)**2 + (m.x114 - m.x145)**2 + (m.x193
    - m.x224)**2 >= 0.46785600000000005)
m.e2123 = Constraint(expr= (m.x35 - m.x67)**2 + (m.x114 - m.x146)**2 + (m.x193
    - m.x225)**2 >= 0.46785600000000005)
m.e2124 = Constraint(expr= (m.x35 - m.x68)**2 + (m.x114 - m.x147)**2 + (m.x193
    - m.x226)**2 >= 0.46785600000000005)
m.e2125 = Constraint(expr= (m.x35 - m.x69)**2 + (m.x114 - m.x148)**2 + (m.x193
    - m.x227)**2 >= 0.46785600000000005)
m.e2126 = Constraint(expr= (m.x35 - m.x70)**2 + (m.x114 - m.x149)**2 + (m.x193
    - m.x228)**2 >= 0.46785600000000005)
m.e2127 = Constraint(expr= (m.x35 - m.x71)**2 + (m.x114 - m.x150)**2 + (m.x193
    - m.x229)**2 >= 0.46785600000000005)
m.e2128 = Constraint(expr= (m.x35 - m.x72)**2 + (m.x114 - m.x151)**2 + (m.x193
    - m.x230)**2 >= 0.46785600000000005)
m.e2129 = Constraint(expr= (m.x35 - m.x73)**2 + (m.x114 - m.x152)**2 + (m.x193
    - m.x231)**2 >= 0.46785600000000005)
m.e2130 = Constraint(expr= (m.x35 - m.x74)**2 + (m.x114 - m.x153)**2 + (m.x193
    - m.x232)**2 >= 0.46785600000000005)
m.e2131 = Constraint(expr= (m.x35 - m.x75)**2 + (m.x114 - m.x154)**2 + (m.x193
    - m.x233)**2 >= 0.46785600000000005)
m.e2132 = Constraint(expr= (m.x35 - m.x76)**2 + (m.x114 - m.x155)**2 + (m.x193
    - m.x234)**2 >= 0.46785600000000005)
m.e2133 = Constraint(expr= (m.x35 - m.x77)**2 + (m.x114 - m.x156)**2 + (m.x193
    - m.x235)**2 >= 0.46785600000000005)
m.e2134 = Constraint(expr= (m.x35 - m.x78)**2 + (m.x114 - m.x157)**2 + (m.x193
    - m.x236)**2 >= 0.46785600000000005)
m.e2135 = Constraint(expr= (m.x35 - m.x79)**2 + (m.x114 - m.x158)**2 + (m.x193
    - m.x237)**2 >= 0.46785600000000005)
m.e2136 = Constraint(expr= (m.x36 - m.x37)**2 + (m.x115 - m.x116)**2 + (m.x194
    - m.x195)**2 >= 0.46785600000000005)
m.e2137 = Constraint(expr= (m.x36 - m.x38)**2 + (m.x115 - m.x117)**2 + (m.x194
    - m.x196)**2 >= 0.46785600000000005)
m.e2138 = Constraint(expr= (m.x36 - m.x39)**2 + (m.x115 - m.x118)**2 + (m.x194
    - m.x197)**2 >= 0.46785600000000005)
m.e2139 = Constraint(expr= (m.x36 - m.x40)**2 + (m.x115 - m.x119)**2 + (m.x194
    - m.x198)**2 >= 0.46785600000000005)
m.e2140 = Constraint(expr= (m.x36 - m.x41)**2 + (m.x115 - m.x120)**2 + (m.x194
    - m.x199)**2 >= 0.46785600000000005)
m.e2141 = Constraint(expr= (m.x36 - m.x42)**2 + (m.x115 - m.x121)**2 + (m.x194
    - m.x200)**2 >= 0.46785600000000005)
m.e2142 = Constraint(expr= (m.x36 - m.x43)**2 + (m.x115 - m.x122)**2 + (m.x194
    - m.x201)**2 >= 0.46785600000000005)
m.e2143 = Constraint(expr= (m.x36 - m.x44)**2 + (m.x115 - m.x123)**2 + (m.x194
    - m.x202)**2 >= 0.46785600000000005)
m.e2144 = Constraint(expr= (m.x36 - m.x45)**2 + (m.x115 - m.x124)**2 + (m.x194
    - m.x203)**2 >= 0.46785600000000005)
m.e2145 = Constraint(expr= (m.x36 - m.x46)**2 + (m.x115 - m.x125)**2 + (m.x194
    - m.x204)**2 >= 0.46785600000000005)
m.e2146 = Constraint(expr= (m.x36 - m.x47)**2 + (m.x115 - m.x126)**2 + (m.x194
    - m.x205)**2 >= 0.46785600000000005)
m.e2147 = Constraint(expr= (m.x36 - m.x48)**2 + (m.x115 - m.x127)**2 + (m.x194
    - m.x206)**2 >= 0.46785600000000005)
m.e2148 = Constraint(expr= (m.x36 - m.x49)**2 + (m.x115 - m.x128)**2 + (m.x194
    - m.x207)**2 >= 0.46785600000000005)
m.e2149 = Constraint(expr= (m.x36 - m.x50)**2 + (m.x115 - m.x129)**2 + (m.x194
    - m.x208)**2 >= 0.46785600000000005)
m.e2150 = Constraint(expr= (m.x36 - m.x51)**2 + (m.x115 - m.x130)**2 + (m.x194
    - m.x209)**2 >= 0.46785600000000005)
m.e2151 = Constraint(expr= (m.x36 - m.x52)**2 + (m.x115 - m.x131)**2 + (m.x194
    - m.x210)**2 >= 0.46785600000000005)
m.e2152 = Constraint(expr= (m.x36 - m.x53)**2 + (m.x115 - m.x132)**2 + (m.x194
    - m.x211)**2 >= 0.46785600000000005)
m.e2153 = Constraint(expr= (m.x36 - m.x54)**2 + (m.x115 - m.x133)**2 + (m.x194
    - m.x212)**2 >= 0.46785600000000005)
m.e2154 = Constraint(expr= (m.x36 - m.x55)**2 + (m.x115 - m.x134)**2 + (m.x194
    - m.x213)**2 >= 0.46785600000000005)
m.e2155 = Constraint(expr= (m.x36 - m.x56)**2 + (m.x115 - m.x135)**2 + (m.x194
    - m.x214)**2 >= 0.46785600000000005)
m.e2156 = Constraint(expr= (m.x36 - m.x57)**2 + (m.x115 - m.x136)**2 + (m.x194
    - m.x215)**2 >= 0.46785600000000005)
m.e2157 = Constraint(expr= (m.x36 - m.x58)**2 + (m.x115 - m.x137)**2 + (m.x194
    - m.x216)**2 >= 0.46785600000000005)
m.e2158 = Constraint(expr= (m.x36 - m.x59)**2 + (m.x115 - m.x138)**2 + (m.x194
    - m.x217)**2 >= 0.46785600000000005)
m.e2159 = Constraint(expr= (m.x36 - m.x60)**2 + (m.x115 - m.x139)**2 + (m.x194
    - m.x218)**2 >= 0.46785600000000005)
m.e2160 = Constraint(expr= (m.x36 - m.x61)**2 + (m.x115 - m.x140)**2 + (m.x194
    - m.x219)**2 >= 0.46785600000000005)
m.e2161 = Constraint(expr= (m.x36 - m.x62)**2 + (m.x115 - m.x141)**2 + (m.x194
    - m.x220)**2 >= 0.46785600000000005)
m.e2162 = Constraint(expr= (m.x36 - m.x63)**2 + (m.x115 - m.x142)**2 + (m.x194
    - m.x221)**2 >= 0.46785600000000005)
m.e2163 = Constraint(expr= (m.x36 - m.x64)**2 + (m.x115 - m.x143)**2 + (m.x194
    - m.x222)**2 >= 0.46785600000000005)
m.e2164 = Constraint(expr= (m.x36 - m.x65)**2 + (m.x115 - m.x144)**2 + (m.x194
    - m.x223)**2 >= 0.46785600000000005)
m.e2165 = Constraint(expr= (m.x36 - m.x66)**2 + (m.x115 - m.x145)**2 + (m.x194
    - m.x224)**2 >= 0.46785600000000005)
m.e2166 = Constraint(expr= (m.x36 - m.x67)**2 + (m.x115 - m.x146)**2 + (m.x194
    - m.x225)**2 >= 0.46785600000000005)
m.e2167 = Constraint(expr= (m.x36 - m.x68)**2 + (m.x115 - m.x147)**2 + (m.x194
    - m.x226)**2 >= 0.46785600000000005)
m.e2168 = Constraint(expr= (m.x36 - m.x69)**2 + (m.x115 - m.x148)**2 + (m.x194
    - m.x227)**2 >= 0.46785600000000005)
m.e2169 = Constraint(expr= (m.x36 - m.x70)**2 + (m.x115 - m.x149)**2 + (m.x194
    - m.x228)**2 >= 0.46785600000000005)
m.e2170 = Constraint(expr= (m.x36 - m.x71)**2 + (m.x115 - m.x150)**2 + (m.x194
    - m.x229)**2 >= 0.46785600000000005)
m.e2171 = Constraint(expr= (m.x36 - m.x72)**2 + (m.x115 - m.x151)**2 + (m.x194
    - m.x230)**2 >= 0.46785600000000005)
m.e2172 = Constraint(expr= (m.x36 - m.x73)**2 + (m.x115 - m.x152)**2 + (m.x194
    - m.x231)**2 >= 0.46785600000000005)
m.e2173 = Constraint(expr= (m.x36 - m.x74)**2 + (m.x115 - m.x153)**2 + (m.x194
    - m.x232)**2 >= 0.46785600000000005)
m.e2174 = Constraint(expr= (m.x36 - m.x75)**2 + (m.x115 - m.x154)**2 + (m.x194
    - m.x233)**2 >= 0.46785600000000005)
m.e2175 = Constraint(expr= (m.x36 - m.x76)**2 + (m.x115 - m.x155)**2 + (m.x194
    - m.x234)**2 >= 0.46785600000000005)
m.e2176 = Constraint(expr= (m.x36 - m.x77)**2 + (m.x115 - m.x156)**2 + (m.x194
    - m.x235)**2 >= 0.46785600000000005)
m.e2177 = Constraint(expr= (m.x36 - m.x78)**2 + (m.x115 - m.x157)**2 + (m.x194
    - m.x236)**2 >= 0.46785600000000005)
m.e2178 = Constraint(expr= (m.x36 - m.x79)**2 + (m.x115 - m.x158)**2 + (m.x194
    - m.x237)**2 >= 0.46785600000000005)
m.e2179 = Constraint(expr= (m.x37 - m.x38)**2 + (m.x116 - m.x117)**2 + (m.x195
    - m.x196)**2 >= 0.46785600000000005)
m.e2180 = Constraint(expr= (m.x37 - m.x39)**2 + (m.x116 - m.x118)**2 + (m.x195
    - m.x197)**2 >= 0.46785600000000005)
m.e2181 = Constraint(expr= (m.x37 - m.x40)**2 + (m.x116 - m.x119)**2 + (m.x195
    - m.x198)**2 >= 0.46785600000000005)
m.e2182 = Constraint(expr= (m.x37 - m.x41)**2 + (m.x116 - m.x120)**2 + (m.x195
    - m.x199)**2 >= 0.46785600000000005)
m.e2183 = Constraint(expr= (m.x37 - m.x42)**2 + (m.x116 - m.x121)**2 + (m.x195
    - m.x200)**2 >= 0.46785600000000005)
m.e2184 = Constraint(expr= (m.x37 - m.x43)**2 + (m.x116 - m.x122)**2 + (m.x195
    - m.x201)**2 >= 0.46785600000000005)
m.e2185 = Constraint(expr= (m.x37 - m.x44)**2 + (m.x116 - m.x123)**2 + (m.x195
    - m.x202)**2 >= 0.46785600000000005)
m.e2186 = Constraint(expr= (m.x37 - m.x45)**2 + (m.x116 - m.x124)**2 + (m.x195
    - m.x203)**2 >= 0.46785600000000005)
m.e2187 = Constraint(expr= (m.x37 - m.x46)**2 + (m.x116 - m.x125)**2 + (m.x195
    - m.x204)**2 >= 0.46785600000000005)
m.e2188 = Constraint(expr= (m.x37 - m.x47)**2 + (m.x116 - m.x126)**2 + (m.x195
    - m.x205)**2 >= 0.46785600000000005)
m.e2189 = Constraint(expr= (m.x37 - m.x48)**2 + (m.x116 - m.x127)**2 + (m.x195
    - m.x206)**2 >= 0.46785600000000005)
m.e2190 = Constraint(expr= (m.x37 - m.x49)**2 + (m.x116 - m.x128)**2 + (m.x195
    - m.x207)**2 >= 0.46785600000000005)
m.e2191 = Constraint(expr= (m.x37 - m.x50)**2 + (m.x116 - m.x129)**2 + (m.x195
    - m.x208)**2 >= 0.46785600000000005)
m.e2192 = Constraint(expr= (m.x37 - m.x51)**2 + (m.x116 - m.x130)**2 + (m.x195
    - m.x209)**2 >= 0.46785600000000005)
m.e2193 = Constraint(expr= (m.x37 - m.x52)**2 + (m.x116 - m.x131)**2 + (m.x195
    - m.x210)**2 >= 0.46785600000000005)
m.e2194 = Constraint(expr= (m.x37 - m.x53)**2 + (m.x116 - m.x132)**2 + (m.x195
    - m.x211)**2 >= 0.46785600000000005)
m.e2195 = Constraint(expr= (m.x37 - m.x54)**2 + (m.x116 - m.x133)**2 + (m.x195
    - m.x212)**2 >= 0.46785600000000005)
m.e2196 = Constraint(expr= (m.x37 - m.x55)**2 + (m.x116 - m.x134)**2 + (m.x195
    - m.x213)**2 >= 0.46785600000000005)
m.e2197 = Constraint(expr= (m.x37 - m.x56)**2 + (m.x116 - m.x135)**2 + (m.x195
    - m.x214)**2 >= 0.46785600000000005)
m.e2198 = Constraint(expr= (m.x37 - m.x57)**2 + (m.x116 - m.x136)**2 + (m.x195
    - m.x215)**2 >= 0.46785600000000005)
m.e2199 = Constraint(expr= (m.x37 - m.x58)**2 + (m.x116 - m.x137)**2 + (m.x195
    - m.x216)**2 >= 0.46785600000000005)
m.e2200 = Constraint(expr= (m.x37 - m.x59)**2 + (m.x116 - m.x138)**2 + (m.x195
    - m.x217)**2 >= 0.46785600000000005)
m.e2201 = Constraint(expr= (m.x37 - m.x60)**2 + (m.x116 - m.x139)**2 + (m.x195
    - m.x218)**2 >= 0.46785600000000005)
m.e2202 = Constraint(expr= (m.x37 - m.x61)**2 + (m.x116 - m.x140)**2 + (m.x195
    - m.x219)**2 >= 0.46785600000000005)
m.e2203 = Constraint(expr= (m.x37 - m.x62)**2 + (m.x116 - m.x141)**2 + (m.x195
    - m.x220)**2 >= 0.46785600000000005)
m.e2204 = Constraint(expr= (m.x37 - m.x63)**2 + (m.x116 - m.x142)**2 + (m.x195
    - m.x221)**2 >= 0.46785600000000005)
m.e2205 = Constraint(expr= (m.x37 - m.x64)**2 + (m.x116 - m.x143)**2 + (m.x195
    - m.x222)**2 >= 0.46785600000000005)
m.e2206 = Constraint(expr= (m.x37 - m.x65)**2 + (m.x116 - m.x144)**2 + (m.x195
    - m.x223)**2 >= 0.46785600000000005)
m.e2207 = Constraint(expr= (m.x37 - m.x66)**2 + (m.x116 - m.x145)**2 + (m.x195
    - m.x224)**2 >= 0.46785600000000005)
m.e2208 = Constraint(expr= (m.x37 - m.x67)**2 + (m.x116 - m.x146)**2 + (m.x195
    - m.x225)**2 >= 0.46785600000000005)
m.e2209 = Constraint(expr= (m.x37 - m.x68)**2 + (m.x116 - m.x147)**2 + (m.x195
    - m.x226)**2 >= 0.46785600000000005)
m.e2210 = Constraint(expr= (m.x37 - m.x69)**2 + (m.x116 - m.x148)**2 + (m.x195
    - m.x227)**2 >= 0.46785600000000005)
m.e2211 = Constraint(expr= (m.x37 - m.x70)**2 + (m.x116 - m.x149)**2 + (m.x195
    - m.x228)**2 >= 0.46785600000000005)
m.e2212 = Constraint(expr= (m.x37 - m.x71)**2 + (m.x116 - m.x150)**2 + (m.x195
    - m.x229)**2 >= 0.46785600000000005)
m.e2213 = Constraint(expr= (m.x37 - m.x72)**2 + (m.x116 - m.x151)**2 + (m.x195
    - m.x230)**2 >= 0.46785600000000005)
m.e2214 = Constraint(expr= (m.x37 - m.x73)**2 + (m.x116 - m.x152)**2 + (m.x195
    - m.x231)**2 >= 0.46785600000000005)
m.e2215 = Constraint(expr= (m.x37 - m.x74)**2 + (m.x116 - m.x153)**2 + (m.x195
    - m.x232)**2 >= 0.46785600000000005)
m.e2216 = Constraint(expr= (m.x37 - m.x75)**2 + (m.x116 - m.x154)**2 + (m.x195
    - m.x233)**2 >= 0.46785600000000005)
m.e2217 = Constraint(expr= (m.x37 - m.x76)**2 + (m.x116 - m.x155)**2 + (m.x195
    - m.x234)**2 >= 0.46785600000000005)
m.e2218 = Constraint(expr= (m.x37 - m.x77)**2 + (m.x116 - m.x156)**2 + (m.x195
    - m.x235)**2 >= 0.46785600000000005)
m.e2219 = Constraint(expr= (m.x37 - m.x78)**2 + (m.x116 - m.x157)**2 + (m.x195
    - m.x236)**2 >= 0.46785600000000005)
m.e2220 = Constraint(expr= (m.x37 - m.x79)**2 + (m.x116 - m.x158)**2 + (m.x195
    - m.x237)**2 >= 0.46785600000000005)
m.e2221 = Constraint(expr= (m.x38 - m.x39)**2 + (m.x117 - m.x118)**2 + (m.x196
    - m.x197)**2 >= 0.46785600000000005)
m.e2222 = Constraint(expr= (m.x38 - m.x40)**2 + (m.x117 - m.x119)**2 + (m.x196
    - m.x198)**2 >= 0.46785600000000005)
m.e2223 = Constraint(expr= (m.x38 - m.x41)**2 + (m.x117 - m.x120)**2 + (m.x196
    - m.x199)**2 >= 0.46785600000000005)
m.e2224 = Constraint(expr= (m.x38 - m.x42)**2 + (m.x117 - m.x121)**2 + (m.x196
    - m.x200)**2 >= 0.46785600000000005)
m.e2225 = Constraint(expr= (m.x38 - m.x43)**2 + (m.x117 - m.x122)**2 + (m.x196
    - m.x201)**2 >= 0.46785600000000005)
m.e2226 = Constraint(expr= (m.x38 - m.x44)**2 + (m.x117 - m.x123)**2 + (m.x196
    - m.x202)**2 >= 0.46785600000000005)
m.e2227 = Constraint(expr= (m.x38 - m.x45)**2 + (m.x117 - m.x124)**2 + (m.x196
    - m.x203)**2 >= 0.46785600000000005)
m.e2228 = Constraint(expr= (m.x38 - m.x46)**2 + (m.x117 - m.x125)**2 + (m.x196
    - m.x204)**2 >= 0.46785600000000005)
m.e2229 = Constraint(expr= (m.x38 - m.x47)**2 + (m.x117 - m.x126)**2 + (m.x196
    - m.x205)**2 >= 0.46785600000000005)
m.e2230 = Constraint(expr= (m.x38 - m.x48)**2 + (m.x117 - m.x127)**2 + (m.x196
    - m.x206)**2 >= 0.46785600000000005)
m.e2231 = Constraint(expr= (m.x38 - m.x49)**2 + (m.x117 - m.x128)**2 + (m.x196
    - m.x207)**2 >= 0.46785600000000005)
m.e2232 = Constraint(expr= (m.x38 - m.x50)**2 + (m.x117 - m.x129)**2 + (m.x196
    - m.x208)**2 >= 0.46785600000000005)
m.e2233 = Constraint(expr= (m.x38 - m.x51)**2 + (m.x117 - m.x130)**2 + (m.x196
    - m.x209)**2 >= 0.46785600000000005)
m.e2234 = Constraint(expr= (m.x38 - m.x52)**2 + (m.x117 - m.x131)**2 + (m.x196
    - m.x210)**2 >= 0.46785600000000005)
m.e2235 = Constraint(expr= (m.x38 - m.x53)**2 + (m.x117 - m.x132)**2 + (m.x196
    - m.x211)**2 >= 0.46785600000000005)
m.e2236 = Constraint(expr= (m.x38 - m.x54)**2 + (m.x117 - m.x133)**2 + (m.x196
    - m.x212)**2 >= 0.46785600000000005)
m.e2237 = Constraint(expr= (m.x38 - m.x55)**2 + (m.x117 - m.x134)**2 + (m.x196
    - m.x213)**2 >= 0.46785600000000005)
m.e2238 = Constraint(expr= (m.x38 - m.x56)**2 + (m.x117 - m.x135)**2 + (m.x196
    - m.x214)**2 >= 0.46785600000000005)
m.e2239 = Constraint(expr= (m.x38 - m.x57)**2 + (m.x117 - m.x136)**2 + (m.x196
    - m.x215)**2 >= 0.46785600000000005)
m.e2240 = Constraint(expr= (m.x38 - m.x58)**2 + (m.x117 - m.x137)**2 + (m.x196
    - m.x216)**2 >= 0.46785600000000005)
m.e2241 = Constraint(expr= (m.x38 - m.x59)**2 + (m.x117 - m.x138)**2 + (m.x196
    - m.x217)**2 >= 0.46785600000000005)
m.e2242 = Constraint(expr= (m.x38 - m.x60)**2 + (m.x117 - m.x139)**2 + (m.x196
    - m.x218)**2 >= 0.46785600000000005)
m.e2243 = Constraint(expr= (m.x38 - m.x61)**2 + (m.x117 - m.x140)**2 + (m.x196
    - m.x219)**2 >= 0.46785600000000005)
m.e2244 = Constraint(expr= (m.x38 - m.x62)**2 + (m.x117 - m.x141)**2 + (m.x196
    - m.x220)**2 >= 0.46785600000000005)
m.e2245 = Constraint(expr= (m.x38 - m.x63)**2 + (m.x117 - m.x142)**2 + (m.x196
    - m.x221)**2 >= 0.46785600000000005)
m.e2246 = Constraint(expr= (m.x38 - m.x64)**2 + (m.x117 - m.x143)**2 + (m.x196
    - m.x222)**2 >= 0.46785600000000005)
m.e2247 = Constraint(expr= (m.x38 - m.x65)**2 + (m.x117 - m.x144)**2 + (m.x196
    - m.x223)**2 >= 0.46785600000000005)
m.e2248 = Constraint(expr= (m.x38 - m.x66)**2 + (m.x117 - m.x145)**2 + (m.x196
    - m.x224)**2 >= 0.46785600000000005)
m.e2249 = Constraint(expr= (m.x38 - m.x67)**2 + (m.x117 - m.x146)**2 + (m.x196
    - m.x225)**2 >= 0.46785600000000005)
m.e2250 = Constraint(expr= (m.x38 - m.x68)**2 + (m.x117 - m.x147)**2 + (m.x196
    - m.x226)**2 >= 0.46785600000000005)
m.e2251 = Constraint(expr= (m.x38 - m.x69)**2 + (m.x117 - m.x148)**2 + (m.x196
    - m.x227)**2 >= 0.46785600000000005)
m.e2252 = Constraint(expr= (m.x38 - m.x70)**2 + (m.x117 - m.x149)**2 + (m.x196
    - m.x228)**2 >= 0.46785600000000005)
m.e2253 = Constraint(expr= (m.x38 - m.x71)**2 + (m.x117 - m.x150)**2 + (m.x196
    - m.x229)**2 >= 0.46785600000000005)
m.e2254 = Constraint(expr= (m.x38 - m.x72)**2 + (m.x117 - m.x151)**2 + (m.x196
    - m.x230)**2 >= 0.46785600000000005)
m.e2255 = Constraint(expr= (m.x38 - m.x73)**2 + (m.x117 - m.x152)**2 + (m.x196
    - m.x231)**2 >= 0.46785600000000005)
m.e2256 = Constraint(expr= (m.x38 - m.x74)**2 + (m.x117 - m.x153)**2 + (m.x196
    - m.x232)**2 >= 0.46785600000000005)
m.e2257 = Constraint(expr= (m.x38 - m.x75)**2 + (m.x117 - m.x154)**2 + (m.x196
    - m.x233)**2 >= 0.46785600000000005)
m.e2258 = Constraint(expr= (m.x38 - m.x76)**2 + (m.x117 - m.x155)**2 + (m.x196
    - m.x234)**2 >= 0.46785600000000005)
m.e2259 = Constraint(expr= (m.x38 - m.x77)**2 + (m.x117 - m.x156)**2 + (m.x196
    - m.x235)**2 >= 0.46785600000000005)
m.e2260 = Constraint(expr= (m.x38 - m.x78)**2 + (m.x117 - m.x157)**2 + (m.x196
    - m.x236)**2 >= 0.46785600000000005)
m.e2261 = Constraint(expr= (m.x38 - m.x79)**2 + (m.x117 - m.x158)**2 + (m.x196
    - m.x237)**2 >= 0.46785600000000005)
m.e2262 = Constraint(expr= (m.x39 - m.x40)**2 + (m.x118 - m.x119)**2 + (m.x197
    - m.x198)**2 >= 0.46785600000000005)
m.e2263 = Constraint(expr= (m.x39 - m.x41)**2 + (m.x118 - m.x120)**2 + (m.x197
    - m.x199)**2 >= 0.46785600000000005)
m.e2264 = Constraint(expr= (m.x39 - m.x42)**2 + (m.x118 - m.x121)**2 + (m.x197
    - m.x200)**2 >= 0.46785600000000005)
m.e2265 = Constraint(expr= (m.x39 - m.x43)**2 + (m.x118 - m.x122)**2 + (m.x197
    - m.x201)**2 >= 0.46785600000000005)
m.e2266 = Constraint(expr= (m.x39 - m.x44)**2 + (m.x118 - m.x123)**2 + (m.x197
    - m.x202)**2 >= 0.46785600000000005)
m.e2267 = Constraint(expr= (m.x39 - m.x45)**2 + (m.x118 - m.x124)**2 + (m.x197
    - m.x203)**2 >= 0.46785600000000005)
m.e2268 = Constraint(expr= (m.x39 - m.x46)**2 + (m.x118 - m.x125)**2 + (m.x197
    - m.x204)**2 >= 0.46785600000000005)
m.e2269 = Constraint(expr= (m.x39 - m.x47)**2 + (m.x118 - m.x126)**2 + (m.x197
    - m.x205)**2 >= 0.46785600000000005)
m.e2270 = Constraint(expr= (m.x39 - m.x48)**2 + (m.x118 - m.x127)**2 + (m.x197
    - m.x206)**2 >= 0.46785600000000005)
m.e2271 = Constraint(expr= (m.x39 - m.x49)**2 + (m.x118 - m.x128)**2 + (m.x197
    - m.x207)**2 >= 0.46785600000000005)
m.e2272 = Constraint(expr= (m.x39 - m.x50)**2 + (m.x118 - m.x129)**2 + (m.x197
    - m.x208)**2 >= 0.46785600000000005)
m.e2273 = Constraint(expr= (m.x39 - m.x51)**2 + (m.x118 - m.x130)**2 + (m.x197
    - m.x209)**2 >= 0.46785600000000005)
m.e2274 = Constraint(expr= (m.x39 - m.x52)**2 + (m.x118 - m.x131)**2 + (m.x197
    - m.x210)**2 >= 0.46785600000000005)
m.e2275 = Constraint(expr= (m.x39 - m.x53)**2 + (m.x118 - m.x132)**2 + (m.x197
    - m.x211)**2 >= 0.46785600000000005)
m.e2276 = Constraint(expr= (m.x39 - m.x54)**2 + (m.x118 - m.x133)**2 + (m.x197
    - m.x212)**2 >= 0.46785600000000005)
m.e2277 = Constraint(expr= (m.x39 - m.x55)**2 + (m.x118 - m.x134)**2 + (m.x197
    - m.x213)**2 >= 0.46785600000000005)
m.e2278 = Constraint(expr= (m.x39 - m.x56)**2 + (m.x118 - m.x135)**2 + (m.x197
    - m.x214)**2 >= 0.46785600000000005)
m.e2279 = Constraint(expr= (m.x39 - m.x57)**2 + (m.x118 - m.x136)**2 + (m.x197
    - m.x215)**2 >= 0.46785600000000005)
m.e2280 = Constraint(expr= (m.x39 - m.x58)**2 + (m.x118 - m.x137)**2 + (m.x197
    - m.x216)**2 >= 0.46785600000000005)
m.e2281 = Constraint(expr= (m.x39 - m.x59)**2 + (m.x118 - m.x138)**2 + (m.x197
    - m.x217)**2 >= 0.46785600000000005)
m.e2282 = Constraint(expr= (m.x39 - m.x60)**2 + (m.x118 - m.x139)**2 + (m.x197
    - m.x218)**2 >= 0.46785600000000005)
m.e2283 = Constraint(expr= (m.x39 - m.x61)**2 + (m.x118 - m.x140)**2 + (m.x197
    - m.x219)**2 >= 0.46785600000000005)
m.e2284 = Constraint(expr= (m.x39 - m.x62)**2 + (m.x118 - m.x141)**2 + (m.x197
    - m.x220)**2 >= 0.46785600000000005)
m.e2285 = Constraint(expr= (m.x39 - m.x63)**2 + (m.x118 - m.x142)**2 + (m.x197
    - m.x221)**2 >= 0.46785600000000005)
m.e2286 = Constraint(expr= (m.x39 - m.x64)**2 + (m.x118 - m.x143)**2 + (m.x197
    - m.x222)**2 >= 0.46785600000000005)
m.e2287 = Constraint(expr= (m.x39 - m.x65)**2 + (m.x118 - m.x144)**2 + (m.x197
    - m.x223)**2 >= 0.46785600000000005)
m.e2288 = Constraint(expr= (m.x39 - m.x66)**2 + (m.x118 - m.x145)**2 + (m.x197
    - m.x224)**2 >= 0.46785600000000005)
m.e2289 = Constraint(expr= (m.x39 - m.x67)**2 + (m.x118 - m.x146)**2 + (m.x197
    - m.x225)**2 >= 0.46785600000000005)
m.e2290 = Constraint(expr= (m.x39 - m.x68)**2 + (m.x118 - m.x147)**2 + (m.x197
    - m.x226)**2 >= 0.46785600000000005)
m.e2291 = Constraint(expr= (m.x39 - m.x69)**2 + (m.x118 - m.x148)**2 + (m.x197
    - m.x227)**2 >= 0.46785600000000005)
m.e2292 = Constraint(expr= (m.x39 - m.x70)**2 + (m.x118 - m.x149)**2 + (m.x197
    - m.x228)**2 >= 0.46785600000000005)
m.e2293 = Constraint(expr= (m.x39 - m.x71)**2 + (m.x118 - m.x150)**2 + (m.x197
    - m.x229)**2 >= 0.46785600000000005)
m.e2294 = Constraint(expr= (m.x39 - m.x72)**2 + (m.x118 - m.x151)**2 + (m.x197
    - m.x230)**2 >= 0.46785600000000005)
m.e2295 = Constraint(expr= (m.x39 - m.x73)**2 + (m.x118 - m.x152)**2 + (m.x197
    - m.x231)**2 >= 0.46785600000000005)
m.e2296 = Constraint(expr= (m.x39 - m.x74)**2 + (m.x118 - m.x153)**2 + (m.x197
    - m.x232)**2 >= 0.46785600000000005)
m.e2297 = Constraint(expr= (m.x39 - m.x75)**2 + (m.x118 - m.x154)**2 + (m.x197
    - m.x233)**2 >= 0.46785600000000005)
m.e2298 = Constraint(expr= (m.x39 - m.x76)**2 + (m.x118 - m.x155)**2 + (m.x197
    - m.x234)**2 >= 0.46785600000000005)
m.e2299 = Constraint(expr= (m.x39 - m.x77)**2 + (m.x118 - m.x156)**2 + (m.x197
    - m.x235)**2 >= 0.46785600000000005)
m.e2300 = Constraint(expr= (m.x39 - m.x78)**2 + (m.x118 - m.x157)**2 + (m.x197
    - m.x236)**2 >= 0.46785600000000005)
m.e2301 = Constraint(expr= (m.x39 - m.x79)**2 + (m.x118 - m.x158)**2 + (m.x197
    - m.x237)**2 >= 0.46785600000000005)
m.e2302 = Constraint(expr= (m.x40 - m.x41)**2 + (m.x119 - m.x120)**2 + (m.x198
    - m.x199)**2 >= 0.46785600000000005)
m.e2303 = Constraint(expr= (m.x40 - m.x42)**2 + (m.x119 - m.x121)**2 + (m.x198
    - m.x200)**2 >= 0.46785600000000005)
m.e2304 = Constraint(expr= (m.x40 - m.x43)**2 + (m.x119 - m.x122)**2 + (m.x198
    - m.x201)**2 >= 0.46785600000000005)
m.e2305 = Constraint(expr= (m.x40 - m.x44)**2 + (m.x119 - m.x123)**2 + (m.x198
    - m.x202)**2 >= 0.46785600000000005)
m.e2306 = Constraint(expr= (m.x40 - m.x45)**2 + (m.x119 - m.x124)**2 + (m.x198
    - m.x203)**2 >= 0.46785600000000005)
m.e2307 = Constraint(expr= (m.x40 - m.x46)**2 + (m.x119 - m.x125)**2 + (m.x198
    - m.x204)**2 >= 0.46785600000000005)
m.e2308 = Constraint(expr= (m.x40 - m.x47)**2 + (m.x119 - m.x126)**2 + (m.x198
    - m.x205)**2 >= 0.46785600000000005)
m.e2309 = Constraint(expr= (m.x40 - m.x48)**2 + (m.x119 - m.x127)**2 + (m.x198
    - m.x206)**2 >= 0.46785600000000005)
m.e2310 = Constraint(expr= (m.x40 - m.x49)**2 + (m.x119 - m.x128)**2 + (m.x198
    - m.x207)**2 >= 0.46785600000000005)
m.e2311 = Constraint(expr= (m.x40 - m.x50)**2 + (m.x119 - m.x129)**2 + (m.x198
    - m.x208)**2 >= 0.46785600000000005)
m.e2312 = Constraint(expr= (m.x40 - m.x51)**2 + (m.x119 - m.x130)**2 + (m.x198
    - m.x209)**2 >= 0.46785600000000005)
m.e2313 = Constraint(expr= (m.x40 - m.x52)**2 + (m.x119 - m.x131)**2 + (m.x198
    - m.x210)**2 >= 0.46785600000000005)
m.e2314 = Constraint(expr= (m.x40 - m.x53)**2 + (m.x119 - m.x132)**2 + (m.x198
    - m.x211)**2 >= 0.46785600000000005)
m.e2315 = Constraint(expr= (m.x40 - m.x54)**2 + (m.x119 - m.x133)**2 + (m.x198
    - m.x212)**2 >= 0.46785600000000005)
m.e2316 = Constraint(expr= (m.x40 - m.x55)**2 + (m.x119 - m.x134)**2 + (m.x198
    - m.x213)**2 >= 0.46785600000000005)
m.e2317 = Constraint(expr= (m.x40 - m.x56)**2 + (m.x119 - m.x135)**2 + (m.x198
    - m.x214)**2 >= 0.46785600000000005)
m.e2318 = Constraint(expr= (m.x40 - m.x57)**2 + (m.x119 - m.x136)**2 + (m.x198
    - m.x215)**2 >= 0.46785600000000005)
m.e2319 = Constraint(expr= (m.x40 - m.x58)**2 + (m.x119 - m.x137)**2 + (m.x198
    - m.x216)**2 >= 0.46785600000000005)
m.e2320 = Constraint(expr= (m.x40 - m.x59)**2 + (m.x119 - m.x138)**2 + (m.x198
    - m.x217)**2 >= 0.46785600000000005)
m.e2321 = Constraint(expr= (m.x40 - m.x60)**2 + (m.x119 - m.x139)**2 + (m.x198
    - m.x218)**2 >= 0.46785600000000005)
m.e2322 = Constraint(expr= (m.x40 - m.x61)**2 + (m.x119 - m.x140)**2 + (m.x198
    - m.x219)**2 >= 0.46785600000000005)
m.e2323 = Constraint(expr= (m.x40 - m.x62)**2 + (m.x119 - m.x141)**2 + (m.x198
    - m.x220)**2 >= 0.46785600000000005)
m.e2324 = Constraint(expr= (m.x40 - m.x63)**2 + (m.x119 - m.x142)**2 + (m.x198
    - m.x221)**2 >= 0.46785600000000005)
m.e2325 = Constraint(expr= (m.x40 - m.x64)**2 + (m.x119 - m.x143)**2 + (m.x198
    - m.x222)**2 >= 0.46785600000000005)
m.e2326 = Constraint(expr= (m.x40 - m.x65)**2 + (m.x119 - m.x144)**2 + (m.x198
    - m.x223)**2 >= 0.46785600000000005)
m.e2327 = Constraint(expr= (m.x40 - m.x66)**2 + (m.x119 - m.x145)**2 + (m.x198
    - m.x224)**2 >= 0.46785600000000005)
m.e2328 = Constraint(expr= (m.x40 - m.x67)**2 + (m.x119 - m.x146)**2 + (m.x198
    - m.x225)**2 >= 0.46785600000000005)
m.e2329 = Constraint(expr= (m.x40 - m.x68)**2 + (m.x119 - m.x147)**2 + (m.x198
    - m.x226)**2 >= 0.46785600000000005)
m.e2330 = Constraint(expr= (m.x40 - m.x69)**2 + (m.x119 - m.x148)**2 + (m.x198
    - m.x227)**2 >= 0.46785600000000005)
m.e2331 = Constraint(expr= (m.x40 - m.x70)**2 + (m.x119 - m.x149)**2 + (m.x198
    - m.x228)**2 >= 0.46785600000000005)
m.e2332 = Constraint(expr= (m.x40 - m.x71)**2 + (m.x119 - m.x150)**2 + (m.x198
    - m.x229)**2 >= 0.46785600000000005)
m.e2333 = Constraint(expr= (m.x40 - m.x72)**2 + (m.x119 - m.x151)**2 + (m.x198
    - m.x230)**2 >= 0.46785600000000005)
m.e2334 = Constraint(expr= (m.x40 - m.x73)**2 + (m.x119 - m.x152)**2 + (m.x198
    - m.x231)**2 >= 0.46785600000000005)
m.e2335 = Constraint(expr= (m.x40 - m.x74)**2 + (m.x119 - m.x153)**2 + (m.x198
    - m.x232)**2 >= 0.46785600000000005)
m.e2336 = Constraint(expr= (m.x40 - m.x75)**2 + (m.x119 - m.x154)**2 + (m.x198
    - m.x233)**2 >= 0.46785600000000005)
m.e2337 = Constraint(expr= (m.x40 - m.x76)**2 + (m.x119 - m.x155)**2 + (m.x198
    - m.x234)**2 >= 0.46785600000000005)
m.e2338 = Constraint(expr= (m.x40 - m.x77)**2 + (m.x119 - m.x156)**2 + (m.x198
    - m.x235)**2 >= 0.46785600000000005)
m.e2339 = Constraint(expr= (m.x40 - m.x78)**2 + (m.x119 - m.x157)**2 + (m.x198
    - m.x236)**2 >= 0.46785600000000005)
m.e2340 = Constraint(expr= (m.x40 - m.x79)**2 + (m.x119 - m.x158)**2 + (m.x198
    - m.x237)**2 >= 0.46785600000000005)
m.e2341 = Constraint(expr= (m.x41 - m.x42)**2 + (m.x120 - m.x121)**2 + (m.x199
    - m.x200)**2 >= 0.46785600000000005)
m.e2342 = Constraint(expr= (m.x41 - m.x43)**2 + (m.x120 - m.x122)**2 + (m.x199
    - m.x201)**2 >= 0.46785600000000005)
m.e2343 = Constraint(expr= (m.x41 - m.x44)**2 + (m.x120 - m.x123)**2 + (m.x199
    - m.x202)**2 >= 0.46785600000000005)
m.e2344 = Constraint(expr= (m.x41 - m.x45)**2 + (m.x120 - m.x124)**2 + (m.x199
    - m.x203)**2 >= 0.46785600000000005)
m.e2345 = Constraint(expr= (m.x41 - m.x46)**2 + (m.x120 - m.x125)**2 + (m.x199
    - m.x204)**2 >= 0.46785600000000005)
m.e2346 = Constraint(expr= (m.x41 - m.x47)**2 + (m.x120 - m.x126)**2 + (m.x199
    - m.x205)**2 >= 0.46785600000000005)
m.e2347 = Constraint(expr= (m.x41 - m.x48)**2 + (m.x120 - m.x127)**2 + (m.x199
    - m.x206)**2 >= 0.46785600000000005)
m.e2348 = Constraint(expr= (m.x41 - m.x49)**2 + (m.x120 - m.x128)**2 + (m.x199
    - m.x207)**2 >= 0.46785600000000005)
m.e2349 = Constraint(expr= (m.x41 - m.x50)**2 + (m.x120 - m.x129)**2 + (m.x199
    - m.x208)**2 >= 0.46785600000000005)
m.e2350 = Constraint(expr= (m.x41 - m.x51)**2 + (m.x120 - m.x130)**2 + (m.x199
    - m.x209)**2 >= 0.46785600000000005)
m.e2351 = Constraint(expr= (m.x41 - m.x52)**2 + (m.x120 - m.x131)**2 + (m.x199
    - m.x210)**2 >= 0.46785600000000005)
m.e2352 = Constraint(expr= (m.x41 - m.x53)**2 + (m.x120 - m.x132)**2 + (m.x199
    - m.x211)**2 >= 0.46785600000000005)
m.e2353 = Constraint(expr= (m.x41 - m.x54)**2 + (m.x120 - m.x133)**2 + (m.x199
    - m.x212)**2 >= 0.46785600000000005)
m.e2354 = Constraint(expr= (m.x41 - m.x55)**2 + (m.x120 - m.x134)**2 + (m.x199
    - m.x213)**2 >= 0.46785600000000005)
m.e2355 = Constraint(expr= (m.x41 - m.x56)**2 + (m.x120 - m.x135)**2 + (m.x199
    - m.x214)**2 >= 0.46785600000000005)
m.e2356 = Constraint(expr= (m.x41 - m.x57)**2 + (m.x120 - m.x136)**2 + (m.x199
    - m.x215)**2 >= 0.46785600000000005)
m.e2357 = Constraint(expr= (m.x41 - m.x58)**2 + (m.x120 - m.x137)**2 + (m.x199
    - m.x216)**2 >= 0.46785600000000005)
m.e2358 = Constraint(expr= (m.x41 - m.x59)**2 + (m.x120 - m.x138)**2 + (m.x199
    - m.x217)**2 >= 0.46785600000000005)
m.e2359 = Constraint(expr= (m.x41 - m.x60)**2 + (m.x120 - m.x139)**2 + (m.x199
    - m.x218)**2 >= 0.46785600000000005)
m.e2360 = Constraint(expr= (m.x41 - m.x61)**2 + (m.x120 - m.x140)**2 + (m.x199
    - m.x219)**2 >= 0.46785600000000005)
m.e2361 = Constraint(expr= (m.x41 - m.x62)**2 + (m.x120 - m.x141)**2 + (m.x199
    - m.x220)**2 >= 0.46785600000000005)
m.e2362 = Constraint(expr= (m.x41 - m.x63)**2 + (m.x120 - m.x142)**2 + (m.x199
    - m.x221)**2 >= 0.46785600000000005)
m.e2363 = Constraint(expr= (m.x41 - m.x64)**2 + (m.x120 - m.x143)**2 + (m.x199
    - m.x222)**2 >= 0.46785600000000005)
m.e2364 = Constraint(expr= (m.x41 - m.x65)**2 + (m.x120 - m.x144)**2 + (m.x199
    - m.x223)**2 >= 0.46785600000000005)
m.e2365 = Constraint(expr= (m.x41 - m.x66)**2 + (m.x120 - m.x145)**2 + (m.x199
    - m.x224)**2 >= 0.46785600000000005)
m.e2366 = Constraint(expr= (m.x41 - m.x67)**2 + (m.x120 - m.x146)**2 + (m.x199
    - m.x225)**2 >= 0.46785600000000005)
m.e2367 = Constraint(expr= (m.x41 - m.x68)**2 + (m.x120 - m.x147)**2 + (m.x199
    - m.x226)**2 >= 0.46785600000000005)
m.e2368 = Constraint(expr= (m.x41 - m.x69)**2 + (m.x120 - m.x148)**2 + (m.x199
    - m.x227)**2 >= 0.46785600000000005)
m.e2369 = Constraint(expr= (m.x41 - m.x70)**2 + (m.x120 - m.x149)**2 + (m.x199
    - m.x228)**2 >= 0.46785600000000005)
m.e2370 = Constraint(expr= (m.x41 - m.x71)**2 + (m.x120 - m.x150)**2 + (m.x199
    - m.x229)**2 >= 0.46785600000000005)
m.e2371 = Constraint(expr= (m.x41 - m.x72)**2 + (m.x120 - m.x151)**2 + (m.x199
    - m.x230)**2 >= 0.46785600000000005)
m.e2372 = Constraint(expr= (m.x41 - m.x73)**2 + (m.x120 - m.x152)**2 + (m.x199
    - m.x231)**2 >= 0.46785600000000005)
m.e2373 = Constraint(expr= (m.x41 - m.x74)**2 + (m.x120 - m.x153)**2 + (m.x199
    - m.x232)**2 >= 0.46785600000000005)
m.e2374 = Constraint(expr= (m.x41 - m.x75)**2 + (m.x120 - m.x154)**2 + (m.x199
    - m.x233)**2 >= 0.46785600000000005)
m.e2375 = Constraint(expr= (m.x41 - m.x76)**2 + (m.x120 - m.x155)**2 + (m.x199
    - m.x234)**2 >= 0.46785600000000005)
m.e2376 = Constraint(expr= (m.x41 - m.x77)**2 + (m.x120 - m.x156)**2 + (m.x199
    - m.x235)**2 >= 0.46785600000000005)
m.e2377 = Constraint(expr= (m.x41 - m.x78)**2 + (m.x120 - m.x157)**2 + (m.x199
    - m.x236)**2 >= 0.46785600000000005)
m.e2378 = Constraint(expr= (m.x41 - m.x79)**2 + (m.x120 - m.x158)**2 + (m.x199
    - m.x237)**2 >= 0.46785600000000005)
m.e2379 = Constraint(expr= (m.x42 - m.x43)**2 + (m.x121 - m.x122)**2 + (m.x200
    - m.x201)**2 >= 0.46785600000000005)
m.e2380 = Constraint(expr= (m.x42 - m.x44)**2 + (m.x121 - m.x123)**2 + (m.x200
    - m.x202)**2 >= 0.46785600000000005)
m.e2381 = Constraint(expr= (m.x42 - m.x45)**2 + (m.x121 - m.x124)**2 + (m.x200
    - m.x203)**2 >= 0.46785600000000005)
m.e2382 = Constraint(expr= (m.x42 - m.x46)**2 + (m.x121 - m.x125)**2 + (m.x200
    - m.x204)**2 >= 0.46785600000000005)
m.e2383 = Constraint(expr= (m.x42 - m.x47)**2 + (m.x121 - m.x126)**2 + (m.x200
    - m.x205)**2 >= 0.46785600000000005)
m.e2384 = Constraint(expr= (m.x42 - m.x48)**2 + (m.x121 - m.x127)**2 + (m.x200
    - m.x206)**2 >= 0.46785600000000005)
m.e2385 = Constraint(expr= (m.x42 - m.x49)**2 + (m.x121 - m.x128)**2 + (m.x200
    - m.x207)**2 >= 0.46785600000000005)
m.e2386 = Constraint(expr= (m.x42 - m.x50)**2 + (m.x121 - m.x129)**2 + (m.x200
    - m.x208)**2 >= 0.46785600000000005)
m.e2387 = Constraint(expr= (m.x42 - m.x51)**2 + (m.x121 - m.x130)**2 + (m.x200
    - m.x209)**2 >= 0.46785600000000005)
m.e2388 = Constraint(expr= (m.x42 - m.x52)**2 + (m.x121 - m.x131)**2 + (m.x200
    - m.x210)**2 >= 0.46785600000000005)
m.e2389 = Constraint(expr= (m.x42 - m.x53)**2 + (m.x121 - m.x132)**2 + (m.x200
    - m.x211)**2 >= 0.46785600000000005)
m.e2390 = Constraint(expr= (m.x42 - m.x54)**2 + (m.x121 - m.x133)**2 + (m.x200
    - m.x212)**2 >= 0.46785600000000005)
m.e2391 = Constraint(expr= (m.x42 - m.x55)**2 + (m.x121 - m.x134)**2 + (m.x200
    - m.x213)**2 >= 0.46785600000000005)
m.e2392 = Constraint(expr= (m.x42 - m.x56)**2 + (m.x121 - m.x135)**2 + (m.x200
    - m.x214)**2 >= 0.46785600000000005)
m.e2393 = Constraint(expr= (m.x42 - m.x57)**2 + (m.x121 - m.x136)**2 + (m.x200
    - m.x215)**2 >= 0.46785600000000005)
m.e2394 = Constraint(expr= (m.x42 - m.x58)**2 + (m.x121 - m.x137)**2 + (m.x200
    - m.x216)**2 >= 0.46785600000000005)
m.e2395 = Constraint(expr= (m.x42 - m.x59)**2 + (m.x121 - m.x138)**2 + (m.x200
    - m.x217)**2 >= 0.46785600000000005)
m.e2396 = Constraint(expr= (m.x42 - m.x60)**2 + (m.x121 - m.x139)**2 + (m.x200
    - m.x218)**2 >= 0.46785600000000005)
m.e2397 = Constraint(expr= (m.x42 - m.x61)**2 + (m.x121 - m.x140)**2 + (m.x200
    - m.x219)**2 >= 0.46785600000000005)
m.e2398 = Constraint(expr= (m.x42 - m.x62)**2 + (m.x121 - m.x141)**2 + (m.x200
    - m.x220)**2 >= 0.46785600000000005)
m.e2399 = Constraint(expr= (m.x42 - m.x63)**2 + (m.x121 - m.x142)**2 + (m.x200
    - m.x221)**2 >= 0.46785600000000005)
m.e2400 = Constraint(expr= (m.x42 - m.x64)**2 + (m.x121 - m.x143)**2 + (m.x200
    - m.x222)**2 >= 0.46785600000000005)
m.e2401 = Constraint(expr= (m.x42 - m.x65)**2 + (m.x121 - m.x144)**2 + (m.x200
    - m.x223)**2 >= 0.46785600000000005)
m.e2402 = Constraint(expr= (m.x42 - m.x66)**2 + (m.x121 - m.x145)**2 + (m.x200
    - m.x224)**2 >= 0.46785600000000005)
m.e2403 = Constraint(expr= (m.x42 - m.x67)**2 + (m.x121 - m.x146)**2 + (m.x200
    - m.x225)**2 >= 0.46785600000000005)
m.e2404 = Constraint(expr= (m.x42 - m.x68)**2 + (m.x121 - m.x147)**2 + (m.x200
    - m.x226)**2 >= 0.46785600000000005)
m.e2405 = Constraint(expr= (m.x42 - m.x69)**2 + (m.x121 - m.x148)**2 + (m.x200
    - m.x227)**2 >= 0.46785600000000005)
m.e2406 = Constraint(expr= (m.x42 - m.x70)**2 + (m.x121 - m.x149)**2 + (m.x200
    - m.x228)**2 >= 0.46785600000000005)
m.e2407 = Constraint(expr= (m.x42 - m.x71)**2 + (m.x121 - m.x150)**2 + (m.x200
    - m.x229)**2 >= 0.46785600000000005)
m.e2408 = Constraint(expr= (m.x42 - m.x72)**2 + (m.x121 - m.x151)**2 + (m.x200
    - m.x230)**2 >= 0.46785600000000005)
m.e2409 = Constraint(expr= (m.x42 - m.x73)**2 + (m.x121 - m.x152)**2 + (m.x200
    - m.x231)**2 >= 0.46785600000000005)
m.e2410 = Constraint(expr= (m.x42 - m.x74)**2 + (m.x121 - m.x153)**2 + (m.x200
    - m.x232)**2 >= 0.46785600000000005)
m.e2411 = Constraint(expr= (m.x42 - m.x75)**2 + (m.x121 - m.x154)**2 + (m.x200
    - m.x233)**2 >= 0.46785600000000005)
m.e2412 = Constraint(expr= (m.x42 - m.x76)**2 + (m.x121 - m.x155)**2 + (m.x200
    - m.x234)**2 >= 0.46785600000000005)
m.e2413 = Constraint(expr= (m.x42 - m.x77)**2 + (m.x121 - m.x156)**2 + (m.x200
    - m.x235)**2 >= 0.46785600000000005)
m.e2414 = Constraint(expr= (m.x42 - m.x78)**2 + (m.x121 - m.x157)**2 + (m.x200
    - m.x236)**2 >= 0.46785600000000005)
m.e2415 = Constraint(expr= (m.x42 - m.x79)**2 + (m.x121 - m.x158)**2 + (m.x200
    - m.x237)**2 >= 0.46785600000000005)
m.e2416 = Constraint(expr= (m.x43 - m.x44)**2 + (m.x122 - m.x123)**2 + (m.x201
    - m.x202)**2 >= 0.46785600000000005)
m.e2417 = Constraint(expr= (m.x43 - m.x45)**2 + (m.x122 - m.x124)**2 + (m.x201
    - m.x203)**2 >= 0.46785600000000005)
m.e2418 = Constraint(expr= (m.x43 - m.x46)**2 + (m.x122 - m.x125)**2 + (m.x201
    - m.x204)**2 >= 0.46785600000000005)
m.e2419 = Constraint(expr= (m.x43 - m.x47)**2 + (m.x122 - m.x126)**2 + (m.x201
    - m.x205)**2 >= 0.46785600000000005)
m.e2420 = Constraint(expr= (m.x43 - m.x48)**2 + (m.x122 - m.x127)**2 + (m.x201
    - m.x206)**2 >= 0.46785600000000005)
m.e2421 = Constraint(expr= (m.x43 - m.x49)**2 + (m.x122 - m.x128)**2 + (m.x201
    - m.x207)**2 >= 0.46785600000000005)
m.e2422 = Constraint(expr= (m.x43 - m.x50)**2 + (m.x122 - m.x129)**2 + (m.x201
    - m.x208)**2 >= 0.46785600000000005)
m.e2423 = Constraint(expr= (m.x43 - m.x51)**2 + (m.x122 - m.x130)**2 + (m.x201
    - m.x209)**2 >= 0.46785600000000005)
m.e2424 = Constraint(expr= (m.x43 - m.x52)**2 + (m.x122 - m.x131)**2 + (m.x201
    - m.x210)**2 >= 0.46785600000000005)
m.e2425 = Constraint(expr= (m.x43 - m.x53)**2 + (m.x122 - m.x132)**2 + (m.x201
    - m.x211)**2 >= 0.46785600000000005)
m.e2426 = Constraint(expr= (m.x43 - m.x54)**2 + (m.x122 - m.x133)**2 + (m.x201
    - m.x212)**2 >= 0.46785600000000005)
m.e2427 = Constraint(expr= (m.x43 - m.x55)**2 + (m.x122 - m.x134)**2 + (m.x201
    - m.x213)**2 >= 0.46785600000000005)
m.e2428 = Constraint(expr= (m.x43 - m.x56)**2 + (m.x122 - m.x135)**2 + (m.x201
    - m.x214)**2 >= 0.46785600000000005)
m.e2429 = Constraint(expr= (m.x43 - m.x57)**2 + (m.x122 - m.x136)**2 + (m.x201
    - m.x215)**2 >= 0.46785600000000005)
m.e2430 = Constraint(expr= (m.x43 - m.x58)**2 + (m.x122 - m.x137)**2 + (m.x201
    - m.x216)**2 >= 0.46785600000000005)
m.e2431 = Constraint(expr= (m.x43 - m.x59)**2 + (m.x122 - m.x138)**2 + (m.x201
    - m.x217)**2 >= 0.46785600000000005)
m.e2432 = Constraint(expr= (m.x43 - m.x60)**2 + (m.x122 - m.x139)**2 + (m.x201
    - m.x218)**2 >= 0.46785600000000005)
m.e2433 = Constraint(expr= (m.x43 - m.x61)**2 + (m.x122 - m.x140)**2 + (m.x201
    - m.x219)**2 >= 0.46785600000000005)
m.e2434 = Constraint(expr= (m.x43 - m.x62)**2 + (m.x122 - m.x141)**2 + (m.x201
    - m.x220)**2 >= 0.46785600000000005)
m.e2435 = Constraint(expr= (m.x43 - m.x63)**2 + (m.x122 - m.x142)**2 + (m.x201
    - m.x221)**2 >= 0.46785600000000005)
m.e2436 = Constraint(expr= (m.x43 - m.x64)**2 + (m.x122 - m.x143)**2 + (m.x201
    - m.x222)**2 >= 0.46785600000000005)
m.e2437 = Constraint(expr= (m.x43 - m.x65)**2 + (m.x122 - m.x144)**2 + (m.x201
    - m.x223)**2 >= 0.46785600000000005)
m.e2438 = Constraint(expr= (m.x43 - m.x66)**2 + (m.x122 - m.x145)**2 + (m.x201
    - m.x224)**2 >= 0.46785600000000005)
m.e2439 = Constraint(expr= (m.x43 - m.x67)**2 + (m.x122 - m.x146)**2 + (m.x201
    - m.x225)**2 >= 0.46785600000000005)
m.e2440 = Constraint(expr= (m.x43 - m.x68)**2 + (m.x122 - m.x147)**2 + (m.x201
    - m.x226)**2 >= 0.46785600000000005)
m.e2441 = Constraint(expr= (m.x43 - m.x69)**2 + (m.x122 - m.x148)**2 + (m.x201
    - m.x227)**2 >= 0.46785600000000005)
m.e2442 = Constraint(expr= (m.x43 - m.x70)**2 + (m.x122 - m.x149)**2 + (m.x201
    - m.x228)**2 >= 0.46785600000000005)
m.e2443 = Constraint(expr= (m.x43 - m.x71)**2 + (m.x122 - m.x150)**2 + (m.x201
    - m.x229)**2 >= 0.46785600000000005)
m.e2444 = Constraint(expr= (m.x43 - m.x72)**2 + (m.x122 - m.x151)**2 + (m.x201
    - m.x230)**2 >= 0.46785600000000005)
m.e2445 = Constraint(expr= (m.x43 - m.x73)**2 + (m.x122 - m.x152)**2 + (m.x201
    - m.x231)**2 >= 0.46785600000000005)
m.e2446 = Constraint(expr= (m.x43 - m.x74)**2 + (m.x122 - m.x153)**2 + (m.x201
    - m.x232)**2 >= 0.46785600000000005)
m.e2447 = Constraint(expr= (m.x43 - m.x75)**2 + (m.x122 - m.x154)**2 + (m.x201
    - m.x233)**2 >= 0.46785600000000005)
m.e2448 = Constraint(expr= (m.x43 - m.x76)**2 + (m.x122 - m.x155)**2 + (m.x201
    - m.x234)**2 >= 0.46785600000000005)
m.e2449 = Constraint(expr= (m.x43 - m.x77)**2 + (m.x122 - m.x156)**2 + (m.x201
    - m.x235)**2 >= 0.46785600000000005)
m.e2450 = Constraint(expr= (m.x43 - m.x78)**2 + (m.x122 - m.x157)**2 + (m.x201
    - m.x236)**2 >= 0.46785600000000005)
m.e2451 = Constraint(expr= (m.x43 - m.x79)**2 + (m.x122 - m.x158)**2 + (m.x201
    - m.x237)**2 >= 0.46785600000000005)
m.e2452 = Constraint(expr= (m.x44 - m.x45)**2 + (m.x123 - m.x124)**2 + (m.x202
    - m.x203)**2 >= 0.46785600000000005)
m.e2453 = Constraint(expr= (m.x44 - m.x46)**2 + (m.x123 - m.x125)**2 + (m.x202
    - m.x204)**2 >= 0.46785600000000005)
m.e2454 = Constraint(expr= (m.x44 - m.x47)**2 + (m.x123 - m.x126)**2 + (m.x202
    - m.x205)**2 >= 0.46785600000000005)
m.e2455 = Constraint(expr= (m.x44 - m.x48)**2 + (m.x123 - m.x127)**2 + (m.x202
    - m.x206)**2 >= 0.46785600000000005)
m.e2456 = Constraint(expr= (m.x44 - m.x49)**2 + (m.x123 - m.x128)**2 + (m.x202
    - m.x207)**2 >= 0.46785600000000005)
m.e2457 = Constraint(expr= (m.x44 - m.x50)**2 + (m.x123 - m.x129)**2 + (m.x202
    - m.x208)**2 >= 0.46785600000000005)
m.e2458 = Constraint(expr= (m.x44 - m.x51)**2 + (m.x123 - m.x130)**2 + (m.x202
    - m.x209)**2 >= 0.46785600000000005)
m.e2459 = Constraint(expr= (m.x44 - m.x52)**2 + (m.x123 - m.x131)**2 + (m.x202
    - m.x210)**2 >= 0.46785600000000005)
m.e2460 = Constraint(expr= (m.x44 - m.x53)**2 + (m.x123 - m.x132)**2 + (m.x202
    - m.x211)**2 >= 0.46785600000000005)
m.e2461 = Constraint(expr= (m.x44 - m.x54)**2 + (m.x123 - m.x133)**2 + (m.x202
    - m.x212)**2 >= 0.46785600000000005)
m.e2462 = Constraint(expr= (m.x44 - m.x55)**2 + (m.x123 - m.x134)**2 + (m.x202
    - m.x213)**2 >= 0.46785600000000005)
m.e2463 = Constraint(expr= (m.x44 - m.x56)**2 + (m.x123 - m.x135)**2 + (m.x202
    - m.x214)**2 >= 0.46785600000000005)
m.e2464 = Constraint(expr= (m.x44 - m.x57)**2 + (m.x123 - m.x136)**2 + (m.x202
    - m.x215)**2 >= 0.46785600000000005)
m.e2465 = Constraint(expr= (m.x44 - m.x58)**2 + (m.x123 - m.x137)**2 + (m.x202
    - m.x216)**2 >= 0.46785600000000005)
m.e2466 = Constraint(expr= (m.x44 - m.x59)**2 + (m.x123 - m.x138)**2 + (m.x202
    - m.x217)**2 >= 0.46785600000000005)
m.e2467 = Constraint(expr= (m.x44 - m.x60)**2 + (m.x123 - m.x139)**2 + (m.x202
    - m.x218)**2 >= 0.46785600000000005)
m.e2468 = Constraint(expr= (m.x44 - m.x61)**2 + (m.x123 - m.x140)**2 + (m.x202
    - m.x219)**2 >= 0.46785600000000005)
m.e2469 = Constraint(expr= (m.x44 - m.x62)**2 + (m.x123 - m.x141)**2 + (m.x202
    - m.x220)**2 >= 0.46785600000000005)
m.e2470 = Constraint(expr= (m.x44 - m.x63)**2 + (m.x123 - m.x142)**2 + (m.x202
    - m.x221)**2 >= 0.46785600000000005)
m.e2471 = Constraint(expr= (m.x44 - m.x64)**2 + (m.x123 - m.x143)**2 + (m.x202
    - m.x222)**2 >= 0.46785600000000005)
m.e2472 = Constraint(expr= (m.x44 - m.x65)**2 + (m.x123 - m.x144)**2 + (m.x202
    - m.x223)**2 >= 0.46785600000000005)
m.e2473 = Constraint(expr= (m.x44 - m.x66)**2 + (m.x123 - m.x145)**2 + (m.x202
    - m.x224)**2 >= 0.46785600000000005)
m.e2474 = Constraint(expr= (m.x44 - m.x67)**2 + (m.x123 - m.x146)**2 + (m.x202
    - m.x225)**2 >= 0.46785600000000005)
m.e2475 = Constraint(expr= (m.x44 - m.x68)**2 + (m.x123 - m.x147)**2 + (m.x202
    - m.x226)**2 >= 0.46785600000000005)
m.e2476 = Constraint(expr= (m.x44 - m.x69)**2 + (m.x123 - m.x148)**2 + (m.x202
    - m.x227)**2 >= 0.46785600000000005)
m.e2477 = Constraint(expr= (m.x44 - m.x70)**2 + (m.x123 - m.x149)**2 + (m.x202
    - m.x228)**2 >= 0.46785600000000005)
m.e2478 = Constraint(expr= (m.x44 - m.x71)**2 + (m.x123 - m.x150)**2 + (m.x202
    - m.x229)**2 >= 0.46785600000000005)
m.e2479 = Constraint(expr= (m.x44 - m.x72)**2 + (m.x123 - m.x151)**2 + (m.x202
    - m.x230)**2 >= 0.46785600000000005)
m.e2480 = Constraint(expr= (m.x44 - m.x73)**2 + (m.x123 - m.x152)**2 + (m.x202
    - m.x231)**2 >= 0.46785600000000005)
m.e2481 = Constraint(expr= (m.x44 - m.x74)**2 + (m.x123 - m.x153)**2 + (m.x202
    - m.x232)**2 >= 0.46785600000000005)
m.e2482 = Constraint(expr= (m.x44 - m.x75)**2 + (m.x123 - m.x154)**2 + (m.x202
    - m.x233)**2 >= 0.46785600000000005)
m.e2483 = Constraint(expr= (m.x44 - m.x76)**2 + (m.x123 - m.x155)**2 + (m.x202
    - m.x234)**2 >= 0.46785600000000005)
m.e2484 = Constraint(expr= (m.x44 - m.x77)**2 + (m.x123 - m.x156)**2 + (m.x202
    - m.x235)**2 >= 0.46785600000000005)
m.e2485 = Constraint(expr= (m.x44 - m.x78)**2 + (m.x123 - m.x157)**2 + (m.x202
    - m.x236)**2 >= 0.46785600000000005)
m.e2486 = Constraint(expr= (m.x44 - m.x79)**2 + (m.x123 - m.x158)**2 + (m.x202
    - m.x237)**2 >= 0.46785600000000005)
m.e2487 = Constraint(expr= (m.x45 - m.x46)**2 + (m.x124 - m.x125)**2 + (m.x203
    - m.x204)**2 >= 0.46785600000000005)
m.e2488 = Constraint(expr= (m.x45 - m.x47)**2 + (m.x124 - m.x126)**2 + (m.x203
    - m.x205)**2 >= 0.46785600000000005)
m.e2489 = Constraint(expr= (m.x45 - m.x48)**2 + (m.x124 - m.x127)**2 + (m.x203
    - m.x206)**2 >= 0.46785600000000005)
m.e2490 = Constraint(expr= (m.x45 - m.x49)**2 + (m.x124 - m.x128)**2 + (m.x203
    - m.x207)**2 >= 0.46785600000000005)
m.e2491 = Constraint(expr= (m.x45 - m.x50)**2 + (m.x124 - m.x129)**2 + (m.x203
    - m.x208)**2 >= 0.46785600000000005)
m.e2492 = Constraint(expr= (m.x45 - m.x51)**2 + (m.x124 - m.x130)**2 + (m.x203
    - m.x209)**2 >= 0.46785600000000005)
m.e2493 = Constraint(expr= (m.x45 - m.x52)**2 + (m.x124 - m.x131)**2 + (m.x203
    - m.x210)**2 >= 0.46785600000000005)
m.e2494 = Constraint(expr= (m.x45 - m.x53)**2 + (m.x124 - m.x132)**2 + (m.x203
    - m.x211)**2 >= 0.46785600000000005)
m.e2495 = Constraint(expr= (m.x45 - m.x54)**2 + (m.x124 - m.x133)**2 + (m.x203
    - m.x212)**2 >= 0.46785600000000005)
m.e2496 = Constraint(expr= (m.x45 - m.x55)**2 + (m.x124 - m.x134)**2 + (m.x203
    - m.x213)**2 >= 0.46785600000000005)
m.e2497 = Constraint(expr= (m.x45 - m.x56)**2 + (m.x124 - m.x135)**2 + (m.x203
    - m.x214)**2 >= 0.46785600000000005)
m.e2498 = Constraint(expr= (m.x45 - m.x57)**2 + (m.x124 - m.x136)**2 + (m.x203
    - m.x215)**2 >= 0.46785600000000005)
m.e2499 = Constraint(expr= (m.x45 - m.x58)**2 + (m.x124 - m.x137)**2 + (m.x203
    - m.x216)**2 >= 0.46785600000000005)
m.e2500 = Constraint(expr= (m.x45 - m.x59)**2 + (m.x124 - m.x138)**2 + (m.x203
    - m.x217)**2 >= 0.46785600000000005)
m.e2501 = Constraint(expr= (m.x45 - m.x60)**2 + (m.x124 - m.x139)**2 + (m.x203
    - m.x218)**2 >= 0.46785600000000005)
m.e2502 = Constraint(expr= (m.x45 - m.x61)**2 + (m.x124 - m.x140)**2 + (m.x203
    - m.x219)**2 >= 0.46785600000000005)
m.e2503 = Constraint(expr= (m.x45 - m.x62)**2 + (m.x124 - m.x141)**2 + (m.x203
    - m.x220)**2 >= 0.46785600000000005)
m.e2504 = Constraint(expr= (m.x45 - m.x63)**2 + (m.x124 - m.x142)**2 + (m.x203
    - m.x221)**2 >= 0.46785600000000005)
m.e2505 = Constraint(expr= (m.x45 - m.x64)**2 + (m.x124 - m.x143)**2 + (m.x203
    - m.x222)**2 >= 0.46785600000000005)
m.e2506 = Constraint(expr= (m.x45 - m.x65)**2 + (m.x124 - m.x144)**2 + (m.x203
    - m.x223)**2 >= 0.46785600000000005)
m.e2507 = Constraint(expr= (m.x45 - m.x66)**2 + (m.x124 - m.x145)**2 + (m.x203
    - m.x224)**2 >= 0.46785600000000005)
m.e2508 = Constraint(expr= (m.x45 - m.x67)**2 + (m.x124 - m.x146)**2 + (m.x203
    - m.x225)**2 >= 0.46785600000000005)
m.e2509 = Constraint(expr= (m.x45 - m.x68)**2 + (m.x124 - m.x147)**2 + (m.x203
    - m.x226)**2 >= 0.46785600000000005)
m.e2510 = Constraint(expr= (m.x45 - m.x69)**2 + (m.x124 - m.x148)**2 + (m.x203
    - m.x227)**2 >= 0.46785600000000005)
m.e2511 = Constraint(expr= (m.x45 - m.x70)**2 + (m.x124 - m.x149)**2 + (m.x203
    - m.x228)**2 >= 0.46785600000000005)
m.e2512 = Constraint(expr= (m.x45 - m.x71)**2 + (m.x124 - m.x150)**2 + (m.x203
    - m.x229)**2 >= 0.46785600000000005)
m.e2513 = Constraint(expr= (m.x45 - m.x72)**2 + (m.x124 - m.x151)**2 + (m.x203
    - m.x230)**2 >= 0.46785600000000005)
m.e2514 = Constraint(expr= (m.x45 - m.x73)**2 + (m.x124 - m.x152)**2 + (m.x203
    - m.x231)**2 >= 0.46785600000000005)
m.e2515 = Constraint(expr= (m.x45 - m.x74)**2 + (m.x124 - m.x153)**2 + (m.x203
    - m.x232)**2 >= 0.46785600000000005)
m.e2516 = Constraint(expr= (m.x45 - m.x75)**2 + (m.x124 - m.x154)**2 + (m.x203
    - m.x233)**2 >= 0.46785600000000005)
m.e2517 = Constraint(expr= (m.x45 - m.x76)**2 + (m.x124 - m.x155)**2 + (m.x203
    - m.x234)**2 >= 0.46785600000000005)
m.e2518 = Constraint(expr= (m.x45 - m.x77)**2 + (m.x124 - m.x156)**2 + (m.x203
    - m.x235)**2 >= 0.46785600000000005)
m.e2519 = Constraint(expr= (m.x45 - m.x78)**2 + (m.x124 - m.x157)**2 + (m.x203
    - m.x236)**2 >= 0.46785600000000005)
m.e2520 = Constraint(expr= (m.x45 - m.x79)**2 + (m.x124 - m.x158)**2 + (m.x203
    - m.x237)**2 >= 0.46785600000000005)
m.e2521 = Constraint(expr= (m.x46 - m.x47)**2 + (m.x125 - m.x126)**2 + (m.x204
    - m.x205)**2 >= 0.46785600000000005)
m.e2522 = Constraint(expr= (m.x46 - m.x48)**2 + (m.x125 - m.x127)**2 + (m.x204
    - m.x206)**2 >= 0.46785600000000005)
m.e2523 = Constraint(expr= (m.x46 - m.x49)**2 + (m.x125 - m.x128)**2 + (m.x204
    - m.x207)**2 >= 0.46785600000000005)
m.e2524 = Constraint(expr= (m.x46 - m.x50)**2 + (m.x125 - m.x129)**2 + (m.x204
    - m.x208)**2 >= 0.46785600000000005)
m.e2525 = Constraint(expr= (m.x46 - m.x51)**2 + (m.x125 - m.x130)**2 + (m.x204
    - m.x209)**2 >= 0.46785600000000005)
m.e2526 = Constraint(expr= (m.x46 - m.x52)**2 + (m.x125 - m.x131)**2 + (m.x204
    - m.x210)**2 >= 0.46785600000000005)
m.e2527 = Constraint(expr= (m.x46 - m.x53)**2 + (m.x125 - m.x132)**2 + (m.x204
    - m.x211)**2 >= 0.46785600000000005)
m.e2528 = Constraint(expr= (m.x46 - m.x54)**2 + (m.x125 - m.x133)**2 + (m.x204
    - m.x212)**2 >= 0.46785600000000005)
m.e2529 = Constraint(expr= (m.x46 - m.x55)**2 + (m.x125 - m.x134)**2 + (m.x204
    - m.x213)**2 >= 0.46785600000000005)
m.e2530 = Constraint(expr= (m.x46 - m.x56)**2 + (m.x125 - m.x135)**2 + (m.x204
    - m.x214)**2 >= 0.46785600000000005)
m.e2531 = Constraint(expr= (m.x46 - m.x57)**2 + (m.x125 - m.x136)**2 + (m.x204
    - m.x215)**2 >= 0.46785600000000005)
m.e2532 = Constraint(expr= (m.x46 - m.x58)**2 + (m.x125 - m.x137)**2 + (m.x204
    - m.x216)**2 >= 0.46785600000000005)
m.e2533 = Constraint(expr= (m.x46 - m.x59)**2 + (m.x125 - m.x138)**2 + (m.x204
    - m.x217)**2 >= 0.46785600000000005)
m.e2534 = Constraint(expr= (m.x46 - m.x60)**2 + (m.x125 - m.x139)**2 + (m.x204
    - m.x218)**2 >= 0.46785600000000005)
m.e2535 = Constraint(expr= (m.x46 - m.x61)**2 + (m.x125 - m.x140)**2 + (m.x204
    - m.x219)**2 >= 0.46785600000000005)
m.e2536 = Constraint(expr= (m.x46 - m.x62)**2 + (m.x125 - m.x141)**2 + (m.x204
    - m.x220)**2 >= 0.46785600000000005)
m.e2537 = Constraint(expr= (m.x46 - m.x63)**2 + (m.x125 - m.x142)**2 + (m.x204
    - m.x221)**2 >= 0.46785600000000005)
m.e2538 = Constraint(expr= (m.x46 - m.x64)**2 + (m.x125 - m.x143)**2 + (m.x204
    - m.x222)**2 >= 0.46785600000000005)
m.e2539 = Constraint(expr= (m.x46 - m.x65)**2 + (m.x125 - m.x144)**2 + (m.x204
    - m.x223)**2 >= 0.46785600000000005)
m.e2540 = Constraint(expr= (m.x46 - m.x66)**2 + (m.x125 - m.x145)**2 + (m.x204
    - m.x224)**2 >= 0.46785600000000005)
m.e2541 = Constraint(expr= (m.x46 - m.x67)**2 + (m.x125 - m.x146)**2 + (m.x204
    - m.x225)**2 >= 0.46785600000000005)
m.e2542 = Constraint(expr= (m.x46 - m.x68)**2 + (m.x125 - m.x147)**2 + (m.x204
    - m.x226)**2 >= 0.46785600000000005)
m.e2543 = Constraint(expr= (m.x46 - m.x69)**2 + (m.x125 - m.x148)**2 + (m.x204
    - m.x227)**2 >= 0.46785600000000005)
m.e2544 = Constraint(expr= (m.x46 - m.x70)**2 + (m.x125 - m.x149)**2 + (m.x204
    - m.x228)**2 >= 0.46785600000000005)
m.e2545 = Constraint(expr= (m.x46 - m.x71)**2 + (m.x125 - m.x150)**2 + (m.x204
    - m.x229)**2 >= 0.46785600000000005)
m.e2546 = Constraint(expr= (m.x46 - m.x72)**2 + (m.x125 - m.x151)**2 + (m.x204
    - m.x230)**2 >= 0.46785600000000005)
m.e2547 = Constraint(expr= (m.x46 - m.x73)**2 + (m.x125 - m.x152)**2 + (m.x204
    - m.x231)**2 >= 0.46785600000000005)
m.e2548 = Constraint(expr= (m.x46 - m.x74)**2 + (m.x125 - m.x153)**2 + (m.x204
    - m.x232)**2 >= 0.46785600000000005)
m.e2549 = Constraint(expr= (m.x46 - m.x75)**2 + (m.x125 - m.x154)**2 + (m.x204
    - m.x233)**2 >= 0.46785600000000005)
m.e2550 = Constraint(expr= (m.x46 - m.x76)**2 + (m.x125 - m.x155)**2 + (m.x204
    - m.x234)**2 >= 0.46785600000000005)
m.e2551 = Constraint(expr= (m.x46 - m.x77)**2 + (m.x125 - m.x156)**2 + (m.x204
    - m.x235)**2 >= 0.46785600000000005)
m.e2552 = Constraint(expr= (m.x46 - m.x78)**2 + (m.x125 - m.x157)**2 + (m.x204
    - m.x236)**2 >= 0.46785600000000005)
m.e2553 = Constraint(expr= (m.x46 - m.x79)**2 + (m.x125 - m.x158)**2 + (m.x204
    - m.x237)**2 >= 0.46785600000000005)
m.e2554 = Constraint(expr= (m.x47 - m.x48)**2 + (m.x126 - m.x127)**2 + (m.x205
    - m.x206)**2 >= 0.46785600000000005)
m.e2555 = Constraint(expr= (m.x47 - m.x49)**2 + (m.x126 - m.x128)**2 + (m.x205
    - m.x207)**2 >= 0.46785600000000005)
m.e2556 = Constraint(expr= (m.x47 - m.x50)**2 + (m.x126 - m.x129)**2 + (m.x205
    - m.x208)**2 >= 0.46785600000000005)
m.e2557 = Constraint(expr= (m.x47 - m.x51)**2 + (m.x126 - m.x130)**2 + (m.x205
    - m.x209)**2 >= 0.46785600000000005)
m.e2558 = Constraint(expr= (m.x47 - m.x52)**2 + (m.x126 - m.x131)**2 + (m.x205
    - m.x210)**2 >= 0.46785600000000005)
m.e2559 = Constraint(expr= (m.x47 - m.x53)**2 + (m.x126 - m.x132)**2 + (m.x205
    - m.x211)**2 >= 0.46785600000000005)
m.e2560 = Constraint(expr= (m.x47 - m.x54)**2 + (m.x126 - m.x133)**2 + (m.x205
    - m.x212)**2 >= 0.46785600000000005)
m.e2561 = Constraint(expr= (m.x47 - m.x55)**2 + (m.x126 - m.x134)**2 + (m.x205
    - m.x213)**2 >= 0.46785600000000005)
m.e2562 = Constraint(expr= (m.x47 - m.x56)**2 + (m.x126 - m.x135)**2 + (m.x205
    - m.x214)**2 >= 0.46785600000000005)
m.e2563 = Constraint(expr= (m.x47 - m.x57)**2 + (m.x126 - m.x136)**2 + (m.x205
    - m.x215)**2 >= 0.46785600000000005)
m.e2564 = Constraint(expr= (m.x47 - m.x58)**2 + (m.x126 - m.x137)**2 + (m.x205
    - m.x216)**2 >= 0.46785600000000005)
m.e2565 = Constraint(expr= (m.x47 - m.x59)**2 + (m.x126 - m.x138)**2 + (m.x205
    - m.x217)**2 >= 0.46785600000000005)
m.e2566 = Constraint(expr= (m.x47 - m.x60)**2 + (m.x126 - m.x139)**2 + (m.x205
    - m.x218)**2 >= 0.46785600000000005)
m.e2567 = Constraint(expr= (m.x47 - m.x61)**2 + (m.x126 - m.x140)**2 + (m.x205
    - m.x219)**2 >= 0.46785600000000005)
m.e2568 = Constraint(expr= (m.x47 - m.x62)**2 + (m.x126 - m.x141)**2 + (m.x205
    - m.x220)**2 >= 0.46785600000000005)
m.e2569 = Constraint(expr= (m.x47 - m.x63)**2 + (m.x126 - m.x142)**2 + (m.x205
    - m.x221)**2 >= 0.46785600000000005)
m.e2570 = Constraint(expr= (m.x47 - m.x64)**2 + (m.x126 - m.x143)**2 + (m.x205
    - m.x222)**2 >= 0.46785600000000005)
m.e2571 = Constraint(expr= (m.x47 - m.x65)**2 + (m.x126 - m.x144)**2 + (m.x205
    - m.x223)**2 >= 0.46785600000000005)
m.e2572 = Constraint(expr= (m.x47 - m.x66)**2 + (m.x126 - m.x145)**2 + (m.x205
    - m.x224)**2 >= 0.46785600000000005)
m.e2573 = Constraint(expr= (m.x47 - m.x67)**2 + (m.x126 - m.x146)**2 + (m.x205
    - m.x225)**2 >= 0.46785600000000005)
m.e2574 = Constraint(expr= (m.x47 - m.x68)**2 + (m.x126 - m.x147)**2 + (m.x205
    - m.x226)**2 >= 0.46785600000000005)
m.e2575 = Constraint(expr= (m.x47 - m.x69)**2 + (m.x126 - m.x148)**2 + (m.x205
    - m.x227)**2 >= 0.46785600000000005)
m.e2576 = Constraint(expr= (m.x47 - m.x70)**2 + (m.x126 - m.x149)**2 + (m.x205
    - m.x228)**2 >= 0.46785600000000005)
m.e2577 = Constraint(expr= (m.x47 - m.x71)**2 + (m.x126 - m.x150)**2 + (m.x205
    - m.x229)**2 >= 0.46785600000000005)
m.e2578 = Constraint(expr= (m.x47 - m.x72)**2 + (m.x126 - m.x151)**2 + (m.x205
    - m.x230)**2 >= 0.46785600000000005)
m.e2579 = Constraint(expr= (m.x47 - m.x73)**2 + (m.x126 - m.x152)**2 + (m.x205
    - m.x231)**2 >= 0.46785600000000005)
m.e2580 = Constraint(expr= (m.x47 - m.x74)**2 + (m.x126 - m.x153)**2 + (m.x205
    - m.x232)**2 >= 0.46785600000000005)
m.e2581 = Constraint(expr= (m.x47 - m.x75)**2 + (m.x126 - m.x154)**2 + (m.x205
    - m.x233)**2 >= 0.46785600000000005)
m.e2582 = Constraint(expr= (m.x47 - m.x76)**2 + (m.x126 - m.x155)**2 + (m.x205
    - m.x234)**2 >= 0.46785600000000005)
m.e2583 = Constraint(expr= (m.x47 - m.x77)**2 + (m.x126 - m.x156)**2 + (m.x205
    - m.x235)**2 >= 0.46785600000000005)
m.e2584 = Constraint(expr= (m.x47 - m.x78)**2 + (m.x126 - m.x157)**2 + (m.x205
    - m.x236)**2 >= 0.46785600000000005)
m.e2585 = Constraint(expr= (m.x47 - m.x79)**2 + (m.x126 - m.x158)**2 + (m.x205
    - m.x237)**2 >= 0.46785600000000005)
m.e2586 = Constraint(expr= (m.x48 - m.x49)**2 + (m.x127 - m.x128)**2 + (m.x206
    - m.x207)**2 >= 0.46785600000000005)
m.e2587 = Constraint(expr= (m.x48 - m.x50)**2 + (m.x127 - m.x129)**2 + (m.x206
    - m.x208)**2 >= 0.46785600000000005)
m.e2588 = Constraint(expr= (m.x48 - m.x51)**2 + (m.x127 - m.x130)**2 + (m.x206
    - m.x209)**2 >= 0.46785600000000005)
m.e2589 = Constraint(expr= (m.x48 - m.x52)**2 + (m.x127 - m.x131)**2 + (m.x206
    - m.x210)**2 >= 0.46785600000000005)
m.e2590 = Constraint(expr= (m.x48 - m.x53)**2 + (m.x127 - m.x132)**2 + (m.x206
    - m.x211)**2 >= 0.46785600000000005)
m.e2591 = Constraint(expr= (m.x48 - m.x54)**2 + (m.x127 - m.x133)**2 + (m.x206
    - m.x212)**2 >= 0.46785600000000005)
m.e2592 = Constraint(expr= (m.x48 - m.x55)**2 + (m.x127 - m.x134)**2 + (m.x206
    - m.x213)**2 >= 0.46785600000000005)
m.e2593 = Constraint(expr= (m.x48 - m.x56)**2 + (m.x127 - m.x135)**2 + (m.x206
    - m.x214)**2 >= 0.46785600000000005)
m.e2594 = Constraint(expr= (m.x48 - m.x57)**2 + (m.x127 - m.x136)**2 + (m.x206
    - m.x215)**2 >= 0.46785600000000005)
m.e2595 = Constraint(expr= (m.x48 - m.x58)**2 + (m.x127 - m.x137)**2 + (m.x206
    - m.x216)**2 >= 0.46785600000000005)
m.e2596 = Constraint(expr= (m.x48 - m.x59)**2 + (m.x127 - m.x138)**2 + (m.x206
    - m.x217)**2 >= 0.46785600000000005)
m.e2597 = Constraint(expr= (m.x48 - m.x60)**2 + (m.x127 - m.x139)**2 + (m.x206
    - m.x218)**2 >= 0.46785600000000005)
m.e2598 = Constraint(expr= (m.x48 - m.x61)**2 + (m.x127 - m.x140)**2 + (m.x206
    - m.x219)**2 >= 0.46785600000000005)
m.e2599 = Constraint(expr= (m.x48 - m.x62)**2 + (m.x127 - m.x141)**2 + (m.x206
    - m.x220)**2 >= 0.46785600000000005)
m.e2600 = Constraint(expr= (m.x48 - m.x63)**2 + (m.x127 - m.x142)**2 + (m.x206
    - m.x221)**2 >= 0.46785600000000005)
m.e2601 = Constraint(expr= (m.x48 - m.x64)**2 + (m.x127 - m.x143)**2 + (m.x206
    - m.x222)**2 >= 0.46785600000000005)
m.e2602 = Constraint(expr= (m.x48 - m.x65)**2 + (m.x127 - m.x144)**2 + (m.x206
    - m.x223)**2 >= 0.46785600000000005)
m.e2603 = Constraint(expr= (m.x48 - m.x66)**2 + (m.x127 - m.x145)**2 + (m.x206
    - m.x224)**2 >= 0.46785600000000005)
m.e2604 = Constraint(expr= (m.x48 - m.x67)**2 + (m.x127 - m.x146)**2 + (m.x206
    - m.x225)**2 >= 0.46785600000000005)
m.e2605 = Constraint(expr= (m.x48 - m.x68)**2 + (m.x127 - m.x147)**2 + (m.x206
    - m.x226)**2 >= 0.46785600000000005)
m.e2606 = Constraint(expr= (m.x48 - m.x69)**2 + (m.x127 - m.x148)**2 + (m.x206
    - m.x227)**2 >= 0.46785600000000005)
m.e2607 = Constraint(expr= (m.x48 - m.x70)**2 + (m.x127 - m.x149)**2 + (m.x206
    - m.x228)**2 >= 0.46785600000000005)
m.e2608 = Constraint(expr= (m.x48 - m.x71)**2 + (m.x127 - m.x150)**2 + (m.x206
    - m.x229)**2 >= 0.46785600000000005)
m.e2609 = Constraint(expr= (m.x48 - m.x72)**2 + (m.x127 - m.x151)**2 + (m.x206
    - m.x230)**2 >= 0.46785600000000005)
m.e2610 = Constraint(expr= (m.x48 - m.x73)**2 + (m.x127 - m.x152)**2 + (m.x206
    - m.x231)**2 >= 0.46785600000000005)
m.e2611 = Constraint(expr= (m.x48 - m.x74)**2 + (m.x127 - m.x153)**2 + (m.x206
    - m.x232)**2 >= 0.46785600000000005)
m.e2612 = Constraint(expr= (m.x48 - m.x75)**2 + (m.x127 - m.x154)**2 + (m.x206
    - m.x233)**2 >= 0.46785600000000005)
m.e2613 = Constraint(expr= (m.x48 - m.x76)**2 + (m.x127 - m.x155)**2 + (m.x206
    - m.x234)**2 >= 0.46785600000000005)
m.e2614 = Constraint(expr= (m.x48 - m.x77)**2 + (m.x127 - m.x156)**2 + (m.x206
    - m.x235)**2 >= 0.46785600000000005)
m.e2615 = Constraint(expr= (m.x48 - m.x78)**2 + (m.x127 - m.x157)**2 + (m.x206
    - m.x236)**2 >= 0.46785600000000005)
m.e2616 = Constraint(expr= (m.x48 - m.x79)**2 + (m.x127 - m.x158)**2 + (m.x206
    - m.x237)**2 >= 0.46785600000000005)
m.e2617 = Constraint(expr= (m.x49 - m.x50)**2 + (m.x128 - m.x129)**2 + (m.x207
    - m.x208)**2 >= 0.46785600000000005)
m.e2618 = Constraint(expr= (m.x49 - m.x51)**2 + (m.x128 - m.x130)**2 + (m.x207
    - m.x209)**2 >= 0.46785600000000005)
m.e2619 = Constraint(expr= (m.x49 - m.x52)**2 + (m.x128 - m.x131)**2 + (m.x207
    - m.x210)**2 >= 0.46785600000000005)
m.e2620 = Constraint(expr= (m.x49 - m.x53)**2 + (m.x128 - m.x132)**2 + (m.x207
    - m.x211)**2 >= 0.46785600000000005)
m.e2621 = Constraint(expr= (m.x49 - m.x54)**2 + (m.x128 - m.x133)**2 + (m.x207
    - m.x212)**2 >= 0.46785600000000005)
m.e2622 = Constraint(expr= (m.x49 - m.x55)**2 + (m.x128 - m.x134)**2 + (m.x207
    - m.x213)**2 >= 0.46785600000000005)
m.e2623 = Constraint(expr= (m.x49 - m.x56)**2 + (m.x128 - m.x135)**2 + (m.x207
    - m.x214)**2 >= 0.46785600000000005)
m.e2624 = Constraint(expr= (m.x49 - m.x57)**2 + (m.x128 - m.x136)**2 + (m.x207
    - m.x215)**2 >= 0.46785600000000005)
m.e2625 = Constraint(expr= (m.x49 - m.x58)**2 + (m.x128 - m.x137)**2 + (m.x207
    - m.x216)**2 >= 0.46785600000000005)
m.e2626 = Constraint(expr= (m.x49 - m.x59)**2 + (m.x128 - m.x138)**2 + (m.x207
    - m.x217)**2 >= 0.46785600000000005)
m.e2627 = Constraint(expr= (m.x49 - m.x60)**2 + (m.x128 - m.x139)**2 + (m.x207
    - m.x218)**2 >= 0.46785600000000005)
m.e2628 = Constraint(expr= (m.x49 - m.x61)**2 + (m.x128 - m.x140)**2 + (m.x207
    - m.x219)**2 >= 0.46785600000000005)
m.e2629 = Constraint(expr= (m.x49 - m.x62)**2 + (m.x128 - m.x141)**2 + (m.x207
    - m.x220)**2 >= 0.46785600000000005)
m.e2630 = Constraint(expr= (m.x49 - m.x63)**2 + (m.x128 - m.x142)**2 + (m.x207
    - m.x221)**2 >= 0.46785600000000005)
m.e2631 = Constraint(expr= (m.x49 - m.x64)**2 + (m.x128 - m.x143)**2 + (m.x207
    - m.x222)**2 >= 0.46785600000000005)
m.e2632 = Constraint(expr= (m.x49 - m.x65)**2 + (m.x128 - m.x144)**2 + (m.x207
    - m.x223)**2 >= 0.46785600000000005)
m.e2633 = Constraint(expr= (m.x49 - m.x66)**2 + (m.x128 - m.x145)**2 + (m.x207
    - m.x224)**2 >= 0.46785600000000005)
m.e2634 = Constraint(expr= (m.x49 - m.x67)**2 + (m.x128 - m.x146)**2 + (m.x207
    - m.x225)**2 >= 0.46785600000000005)
m.e2635 = Constraint(expr= (m.x49 - m.x68)**2 + (m.x128 - m.x147)**2 + (m.x207
    - m.x226)**2 >= 0.46785600000000005)
m.e2636 = Constraint(expr= (m.x49 - m.x69)**2 + (m.x128 - m.x148)**2 + (m.x207
    - m.x227)**2 >= 0.46785600000000005)
m.e2637 = Constraint(expr= (m.x49 - m.x70)**2 + (m.x128 - m.x149)**2 + (m.x207
    - m.x228)**2 >= 0.46785600000000005)
m.e2638 = Constraint(expr= (m.x49 - m.x71)**2 + (m.x128 - m.x150)**2 + (m.x207
    - m.x229)**2 >= 0.46785600000000005)
m.e2639 = Constraint(expr= (m.x49 - m.x72)**2 + (m.x128 - m.x151)**2 + (m.x207
    - m.x230)**2 >= 0.46785600000000005)
m.e2640 = Constraint(expr= (m.x49 - m.x73)**2 + (m.x128 - m.x152)**2 + (m.x207
    - m.x231)**2 >= 0.46785600000000005)
m.e2641 = Constraint(expr= (m.x49 - m.x74)**2 + (m.x128 - m.x153)**2 + (m.x207
    - m.x232)**2 >= 0.46785600000000005)
m.e2642 = Constraint(expr= (m.x49 - m.x75)**2 + (m.x128 - m.x154)**2 + (m.x207
    - m.x233)**2 >= 0.46785600000000005)
m.e2643 = Constraint(expr= (m.x49 - m.x76)**2 + (m.x128 - m.x155)**2 + (m.x207
    - m.x234)**2 >= 0.46785600000000005)
m.e2644 = Constraint(expr= (m.x49 - m.x77)**2 + (m.x128 - m.x156)**2 + (m.x207
    - m.x235)**2 >= 0.46785600000000005)
m.e2645 = Constraint(expr= (m.x49 - m.x78)**2 + (m.x128 - m.x157)**2 + (m.x207
    - m.x236)**2 >= 0.46785600000000005)
m.e2646 = Constraint(expr= (m.x49 - m.x79)**2 + (m.x128 - m.x158)**2 + (m.x207
    - m.x237)**2 >= 0.46785600000000005)
m.e2647 = Constraint(expr= (m.x50 - m.x51)**2 + (m.x129 - m.x130)**2 + (m.x208
    - m.x209)**2 >= 0.46785600000000005)
m.e2648 = Constraint(expr= (m.x50 - m.x52)**2 + (m.x129 - m.x131)**2 + (m.x208
    - m.x210)**2 >= 0.46785600000000005)
m.e2649 = Constraint(expr= (m.x50 - m.x53)**2 + (m.x129 - m.x132)**2 + (m.x208
    - m.x211)**2 >= 0.46785600000000005)
m.e2650 = Constraint(expr= (m.x50 - m.x54)**2 + (m.x129 - m.x133)**2 + (m.x208
    - m.x212)**2 >= 0.46785600000000005)
m.e2651 = Constraint(expr= (m.x50 - m.x55)**2 + (m.x129 - m.x134)**2 + (m.x208
    - m.x213)**2 >= 0.46785600000000005)
m.e2652 = Constraint(expr= (m.x50 - m.x56)**2 + (m.x129 - m.x135)**2 + (m.x208
    - m.x214)**2 >= 0.46785600000000005)
m.e2653 = Constraint(expr= (m.x50 - m.x57)**2 + (m.x129 - m.x136)**2 + (m.x208
    - m.x215)**2 >= 0.46785600000000005)
m.e2654 = Constraint(expr= (m.x50 - m.x58)**2 + (m.x129 - m.x137)**2 + (m.x208
    - m.x216)**2 >= 0.46785600000000005)
m.e2655 = Constraint(expr= (m.x50 - m.x59)**2 + (m.x129 - m.x138)**2 + (m.x208
    - m.x217)**2 >= 0.46785600000000005)
m.e2656 = Constraint(expr= (m.x50 - m.x60)**2 + (m.x129 - m.x139)**2 + (m.x208
    - m.x218)**2 >= 0.46785600000000005)
m.e2657 = Constraint(expr= (m.x50 - m.x61)**2 + (m.x129 - m.x140)**2 + (m.x208
    - m.x219)**2 >= 0.46785600000000005)
m.e2658 = Constraint(expr= (m.x50 - m.x62)**2 + (m.x129 - m.x141)**2 + (m.x208
    - m.x220)**2 >= 0.46785600000000005)
m.e2659 = Constraint(expr= (m.x50 - m.x63)**2 + (m.x129 - m.x142)**2 + (m.x208
    - m.x221)**2 >= 0.46785600000000005)
m.e2660 = Constraint(expr= (m.x50 - m.x64)**2 + (m.x129 - m.x143)**2 + (m.x208
    - m.x222)**2 >= 0.46785600000000005)
m.e2661 = Constraint(expr= (m.x50 - m.x65)**2 + (m.x129 - m.x144)**2 + (m.x208
    - m.x223)**2 >= 0.46785600000000005)
m.e2662 = Constraint(expr= (m.x50 - m.x66)**2 + (m.x129 - m.x145)**2 + (m.x208
    - m.x224)**2 >= 0.46785600000000005)
m.e2663 = Constraint(expr= (m.x50 - m.x67)**2 + (m.x129 - m.x146)**2 + (m.x208
    - m.x225)**2 >= 0.46785600000000005)
m.e2664 = Constraint(expr= (m.x50 - m.x68)**2 + (m.x129 - m.x147)**2 + (m.x208
    - m.x226)**2 >= 0.46785600000000005)
m.e2665 = Constraint(expr= (m.x50 - m.x69)**2 + (m.x129 - m.x148)**2 + (m.x208
    - m.x227)**2 >= 0.46785600000000005)
m.e2666 = Constraint(expr= (m.x50 - m.x70)**2 + (m.x129 - m.x149)**2 + (m.x208
    - m.x228)**2 >= 0.46785600000000005)
m.e2667 = Constraint(expr= (m.x50 - m.x71)**2 + (m.x129 - m.x150)**2 + (m.x208
    - m.x229)**2 >= 0.46785600000000005)
m.e2668 = Constraint(expr= (m.x50 - m.x72)**2 + (m.x129 - m.x151)**2 + (m.x208
    - m.x230)**2 >= 0.46785600000000005)
m.e2669 = Constraint(expr= (m.x50 - m.x73)**2 + (m.x129 - m.x152)**2 + (m.x208
    - m.x231)**2 >= 0.46785600000000005)
m.e2670 = Constraint(expr= (m.x50 - m.x74)**2 + (m.x129 - m.x153)**2 + (m.x208
    - m.x232)**2 >= 0.46785600000000005)
m.e2671 = Constraint(expr= (m.x50 - m.x75)**2 + (m.x129 - m.x154)**2 + (m.x208
    - m.x233)**2 >= 0.46785600000000005)
m.e2672 = Constraint(expr= (m.x50 - m.x76)**2 + (m.x129 - m.x155)**2 + (m.x208
    - m.x234)**2 >= 0.46785600000000005)
m.e2673 = Constraint(expr= (m.x50 - m.x77)**2 + (m.x129 - m.x156)**2 + (m.x208
    - m.x235)**2 >= 0.46785600000000005)
m.e2674 = Constraint(expr= (m.x50 - m.x78)**2 + (m.x129 - m.x157)**2 + (m.x208
    - m.x236)**2 >= 0.46785600000000005)
m.e2675 = Constraint(expr= (m.x50 - m.x79)**2 + (m.x129 - m.x158)**2 + (m.x208
    - m.x237)**2 >= 0.46785600000000005)
m.e2676 = Constraint(expr= (m.x51 - m.x52)**2 + (m.x130 - m.x131)**2 + (m.x209
    - m.x210)**2 >= 0.46785600000000005)
m.e2677 = Constraint(expr= (m.x51 - m.x53)**2 + (m.x130 - m.x132)**2 + (m.x209
    - m.x211)**2 >= 0.46785600000000005)
m.e2678 = Constraint(expr= (m.x51 - m.x54)**2 + (m.x130 - m.x133)**2 + (m.x209
    - m.x212)**2 >= 0.46785600000000005)
m.e2679 = Constraint(expr= (m.x51 - m.x55)**2 + (m.x130 - m.x134)**2 + (m.x209
    - m.x213)**2 >= 0.46785600000000005)
m.e2680 = Constraint(expr= (m.x51 - m.x56)**2 + (m.x130 - m.x135)**2 + (m.x209
    - m.x214)**2 >= 0.46785600000000005)
m.e2681 = Constraint(expr= (m.x51 - m.x57)**2 + (m.x130 - m.x136)**2 + (m.x209
    - m.x215)**2 >= 0.46785600000000005)
m.e2682 = Constraint(expr= (m.x51 - m.x58)**2 + (m.x130 - m.x137)**2 + (m.x209
    - m.x216)**2 >= 0.46785600000000005)
m.e2683 = Constraint(expr= (m.x51 - m.x59)**2 + (m.x130 - m.x138)**2 + (m.x209
    - m.x217)**2 >= 0.46785600000000005)
m.e2684 = Constraint(expr= (m.x51 - m.x60)**2 + (m.x130 - m.x139)**2 + (m.x209
    - m.x218)**2 >= 0.46785600000000005)
m.e2685 = Constraint(expr= (m.x51 - m.x61)**2 + (m.x130 - m.x140)**2 + (m.x209
    - m.x219)**2 >= 0.46785600000000005)
m.e2686 = Constraint(expr= (m.x51 - m.x62)**2 + (m.x130 - m.x141)**2 + (m.x209
    - m.x220)**2 >= 0.46785600000000005)
m.e2687 = Constraint(expr= (m.x51 - m.x63)**2 + (m.x130 - m.x142)**2 + (m.x209
    - m.x221)**2 >= 0.46785600000000005)
m.e2688 = Constraint(expr= (m.x51 - m.x64)**2 + (m.x130 - m.x143)**2 + (m.x209
    - m.x222)**2 >= 0.46785600000000005)
m.e2689 = Constraint(expr= (m.x51 - m.x65)**2 + (m.x130 - m.x144)**2 + (m.x209
    - m.x223)**2 >= 0.46785600000000005)
m.e2690 = Constraint(expr= (m.x51 - m.x66)**2 + (m.x130 - m.x145)**2 + (m.x209
    - m.x224)**2 >= 0.46785600000000005)
m.e2691 = Constraint(expr= (m.x51 - m.x67)**2 + (m.x130 - m.x146)**2 + (m.x209
    - m.x225)**2 >= 0.46785600000000005)
m.e2692 = Constraint(expr= (m.x51 - m.x68)**2 + (m.x130 - m.x147)**2 + (m.x209
    - m.x226)**2 >= 0.46785600000000005)
m.e2693 = Constraint(expr= (m.x51 - m.x69)**2 + (m.x130 - m.x148)**2 + (m.x209
    - m.x227)**2 >= 0.46785600000000005)
m.e2694 = Constraint(expr= (m.x51 - m.x70)**2 + (m.x130 - m.x149)**2 + (m.x209
    - m.x228)**2 >= 0.46785600000000005)
m.e2695 = Constraint(expr= (m.x51 - m.x71)**2 + (m.x130 - m.x150)**2 + (m.x209
    - m.x229)**2 >= 0.46785600000000005)
m.e2696 = Constraint(expr= (m.x51 - m.x72)**2 + (m.x130 - m.x151)**2 + (m.x209
    - m.x230)**2 >= 0.46785600000000005)
m.e2697 = Constraint(expr= (m.x51 - m.x73)**2 + (m.x130 - m.x152)**2 + (m.x209
    - m.x231)**2 >= 0.46785600000000005)
m.e2698 = Constraint(expr= (m.x51 - m.x74)**2 + (m.x130 - m.x153)**2 + (m.x209
    - m.x232)**2 >= 0.46785600000000005)
m.e2699 = Constraint(expr= (m.x51 - m.x75)**2 + (m.x130 - m.x154)**2 + (m.x209
    - m.x233)**2 >= 0.46785600000000005)
m.e2700 = Constraint(expr= (m.x51 - m.x76)**2 + (m.x130 - m.x155)**2 + (m.x209
    - m.x234)**2 >= 0.46785600000000005)
m.e2701 = Constraint(expr= (m.x51 - m.x77)**2 + (m.x130 - m.x156)**2 + (m.x209
    - m.x235)**2 >= 0.46785600000000005)
m.e2702 = Constraint(expr= (m.x51 - m.x78)**2 + (m.x130 - m.x157)**2 + (m.x209
    - m.x236)**2 >= 0.46785600000000005)
m.e2703 = Constraint(expr= (m.x51 - m.x79)**2 + (m.x130 - m.x158)**2 + (m.x209
    - m.x237)**2 >= 0.46785600000000005)
m.e2704 = Constraint(expr= (m.x52 - m.x53)**2 + (m.x131 - m.x132)**2 + (m.x210
    - m.x211)**2 >= 0.46785600000000005)
m.e2705 = Constraint(expr= (m.x52 - m.x54)**2 + (m.x131 - m.x133)**2 + (m.x210
    - m.x212)**2 >= 0.46785600000000005)
m.e2706 = Constraint(expr= (m.x52 - m.x55)**2 + (m.x131 - m.x134)**2 + (m.x210
    - m.x213)**2 >= 0.46785600000000005)
m.e2707 = Constraint(expr= (m.x52 - m.x56)**2 + (m.x131 - m.x135)**2 + (m.x210
    - m.x214)**2 >= 0.46785600000000005)
m.e2708 = Constraint(expr= (m.x52 - m.x57)**2 + (m.x131 - m.x136)**2 + (m.x210
    - m.x215)**2 >= 0.46785600000000005)
m.e2709 = Constraint(expr= (m.x52 - m.x58)**2 + (m.x131 - m.x137)**2 + (m.x210
    - m.x216)**2 >= 0.46785600000000005)
m.e2710 = Constraint(expr= (m.x52 - m.x59)**2 + (m.x131 - m.x138)**2 + (m.x210
    - m.x217)**2 >= 0.46785600000000005)
m.e2711 = Constraint(expr= (m.x52 - m.x60)**2 + (m.x131 - m.x139)**2 + (m.x210
    - m.x218)**2 >= 0.46785600000000005)
m.e2712 = Constraint(expr= (m.x52 - m.x61)**2 + (m.x131 - m.x140)**2 + (m.x210
    - m.x219)**2 >= 0.46785600000000005)
m.e2713 = Constraint(expr= (m.x52 - m.x62)**2 + (m.x131 - m.x141)**2 + (m.x210
    - m.x220)**2 >= 0.46785600000000005)
m.e2714 = Constraint(expr= (m.x52 - m.x63)**2 + (m.x131 - m.x142)**2 + (m.x210
    - m.x221)**2 >= 0.46785600000000005)
m.e2715 = Constraint(expr= (m.x52 - m.x64)**2 + (m.x131 - m.x143)**2 + (m.x210
    - m.x222)**2 >= 0.46785600000000005)
m.e2716 = Constraint(expr= (m.x52 - m.x65)**2 + (m.x131 - m.x144)**2 + (m.x210
    - m.x223)**2 >= 0.46785600000000005)
m.e2717 = Constraint(expr= (m.x52 - m.x66)**2 + (m.x131 - m.x145)**2 + (m.x210
    - m.x224)**2 >= 0.46785600000000005)
m.e2718 = Constraint(expr= (m.x52 - m.x67)**2 + (m.x131 - m.x146)**2 + (m.x210
    - m.x225)**2 >= 0.46785600000000005)
m.e2719 = Constraint(expr= (m.x52 - m.x68)**2 + (m.x131 - m.x147)**2 + (m.x210
    - m.x226)**2 >= 0.46785600000000005)
m.e2720 = Constraint(expr= (m.x52 - m.x69)**2 + (m.x131 - m.x148)**2 + (m.x210
    - m.x227)**2 >= 0.46785600000000005)
m.e2721 = Constraint(expr= (m.x52 - m.x70)**2 + (m.x131 - m.x149)**2 + (m.x210
    - m.x228)**2 >= 0.46785600000000005)
m.e2722 = Constraint(expr= (m.x52 - m.x71)**2 + (m.x131 - m.x150)**2 + (m.x210
    - m.x229)**2 >= 0.46785600000000005)
m.e2723 = Constraint(expr= (m.x52 - m.x72)**2 + (m.x131 - m.x151)**2 + (m.x210
    - m.x230)**2 >= 0.46785600000000005)
m.e2724 = Constraint(expr= (m.x52 - m.x73)**2 + (m.x131 - m.x152)**2 + (m.x210
    - m.x231)**2 >= 0.46785600000000005)
m.e2725 = Constraint(expr= (m.x52 - m.x74)**2 + (m.x131 - m.x153)**2 + (m.x210
    - m.x232)**2 >= 0.46785600000000005)
m.e2726 = Constraint(expr= (m.x52 - m.x75)**2 + (m.x131 - m.x154)**2 + (m.x210
    - m.x233)**2 >= 0.46785600000000005)
m.e2727 = Constraint(expr= (m.x52 - m.x76)**2 + (m.x131 - m.x155)**2 + (m.x210
    - m.x234)**2 >= 0.46785600000000005)
m.e2728 = Constraint(expr= (m.x52 - m.x77)**2 + (m.x131 - m.x156)**2 + (m.x210
    - m.x235)**2 >= 0.46785600000000005)
m.e2729 = Constraint(expr= (m.x52 - m.x78)**2 + (m.x131 - m.x157)**2 + (m.x210
    - m.x236)**2 >= 0.46785600000000005)
m.e2730 = Constraint(expr= (m.x52 - m.x79)**2 + (m.x131 - m.x158)**2 + (m.x210
    - m.x237)**2 >= 0.46785600000000005)
m.e2731 = Constraint(expr= (m.x53 - m.x54)**2 + (m.x132 - m.x133)**2 + (m.x211
    - m.x212)**2 >= 0.46785600000000005)
m.e2732 = Constraint(expr= (m.x53 - m.x55)**2 + (m.x132 - m.x134)**2 + (m.x211
    - m.x213)**2 >= 0.46785600000000005)
m.e2733 = Constraint(expr= (m.x53 - m.x56)**2 + (m.x132 - m.x135)**2 + (m.x211
    - m.x214)**2 >= 0.46785600000000005)
m.e2734 = Constraint(expr= (m.x53 - m.x57)**2 + (m.x132 - m.x136)**2 + (m.x211
    - m.x215)**2 >= 0.46785600000000005)
m.e2735 = Constraint(expr= (m.x53 - m.x58)**2 + (m.x132 - m.x137)**2 + (m.x211
    - m.x216)**2 >= 0.46785600000000005)
m.e2736 = Constraint(expr= (m.x53 - m.x59)**2 + (m.x132 - m.x138)**2 + (m.x211
    - m.x217)**2 >= 0.46785600000000005)
m.e2737 = Constraint(expr= (m.x53 - m.x60)**2 + (m.x132 - m.x139)**2 + (m.x211
    - m.x218)**2 >= 0.46785600000000005)
m.e2738 = Constraint(expr= (m.x53 - m.x61)**2 + (m.x132 - m.x140)**2 + (m.x211
    - m.x219)**2 >= 0.46785600000000005)
m.e2739 = Constraint(expr= (m.x53 - m.x62)**2 + (m.x132 - m.x141)**2 + (m.x211
    - m.x220)**2 >= 0.46785600000000005)
m.e2740 = Constraint(expr= (m.x53 - m.x63)**2 + (m.x132 - m.x142)**2 + (m.x211
    - m.x221)**2 >= 0.46785600000000005)
m.e2741 = Constraint(expr= (m.x53 - m.x64)**2 + (m.x132 - m.x143)**2 + (m.x211
    - m.x222)**2 >= 0.46785600000000005)
m.e2742 = Constraint(expr= (m.x53 - m.x65)**2 + (m.x132 - m.x144)**2 + (m.x211
    - m.x223)**2 >= 0.46785600000000005)
m.e2743 = Constraint(expr= (m.x53 - m.x66)**2 + (m.x132 - m.x145)**2 + (m.x211
    - m.x224)**2 >= 0.46785600000000005)
m.e2744 = Constraint(expr= (m.x53 - m.x67)**2 + (m.x132 - m.x146)**2 + (m.x211
    - m.x225)**2 >= 0.46785600000000005)
m.e2745 = Constraint(expr= (m.x53 - m.x68)**2 + (m.x132 - m.x147)**2 + (m.x211
    - m.x226)**2 >= 0.46785600000000005)
m.e2746 = Constraint(expr= (m.x53 - m.x69)**2 + (m.x132 - m.x148)**2 + (m.x211
    - m.x227)**2 >= 0.46785600000000005)
m.e2747 = Constraint(expr= (m.x53 - m.x70)**2 + (m.x132 - m.x149)**2 + (m.x211
    - m.x228)**2 >= 0.46785600000000005)
m.e2748 = Constraint(expr= (m.x53 - m.x71)**2 + (m.x132 - m.x150)**2 + (m.x211
    - m.x229)**2 >= 0.46785600000000005)
m.e2749 = Constraint(expr= (m.x53 - m.x72)**2 + (m.x132 - m.x151)**2 + (m.x211
    - m.x230)**2 >= 0.46785600000000005)
m.e2750 = Constraint(expr= (m.x53 - m.x73)**2 + (m.x132 - m.x152)**2 + (m.x211
    - m.x231)**2 >= 0.46785600000000005)
m.e2751 = Constraint(expr= (m.x53 - m.x74)**2 + (m.x132 - m.x153)**2 + (m.x211
    - m.x232)**2 >= 0.46785600000000005)
m.e2752 = Constraint(expr= (m.x53 - m.x75)**2 + (m.x132 - m.x154)**2 + (m.x211
    - m.x233)**2 >= 0.46785600000000005)
m.e2753 = Constraint(expr= (m.x53 - m.x76)**2 + (m.x132 - m.x155)**2 + (m.x211
    - m.x234)**2 >= 0.46785600000000005)
m.e2754 = Constraint(expr= (m.x53 - m.x77)**2 + (m.x132 - m.x156)**2 + (m.x211
    - m.x235)**2 >= 0.46785600000000005)
m.e2755 = Constraint(expr= (m.x53 - m.x78)**2 + (m.x132 - m.x157)**2 + (m.x211
    - m.x236)**2 >= 0.46785600000000005)
m.e2756 = Constraint(expr= (m.x53 - m.x79)**2 + (m.x132 - m.x158)**2 + (m.x211
    - m.x237)**2 >= 0.46785600000000005)
m.e2757 = Constraint(expr= (m.x54 - m.x55)**2 + (m.x133 - m.x134)**2 + (m.x212
    - m.x213)**2 >= 0.46785600000000005)
m.e2758 = Constraint(expr= (m.x54 - m.x56)**2 + (m.x133 - m.x135)**2 + (m.x212
    - m.x214)**2 >= 0.46785600000000005)
m.e2759 = Constraint(expr= (m.x54 - m.x57)**2 + (m.x133 - m.x136)**2 + (m.x212
    - m.x215)**2 >= 0.46785600000000005)
m.e2760 = Constraint(expr= (m.x54 - m.x58)**2 + (m.x133 - m.x137)**2 + (m.x212
    - m.x216)**2 >= 0.46785600000000005)
m.e2761 = Constraint(expr= (m.x54 - m.x59)**2 + (m.x133 - m.x138)**2 + (m.x212
    - m.x217)**2 >= 0.46785600000000005)
m.e2762 = Constraint(expr= (m.x54 - m.x60)**2 + (m.x133 - m.x139)**2 + (m.x212
    - m.x218)**2 >= 0.46785600000000005)
m.e2763 = Constraint(expr= (m.x54 - m.x61)**2 + (m.x133 - m.x140)**2 + (m.x212
    - m.x219)**2 >= 0.46785600000000005)
m.e2764 = Constraint(expr= (m.x54 - m.x62)**2 + (m.x133 - m.x141)**2 + (m.x212
    - m.x220)**2 >= 0.46785600000000005)
m.e2765 = Constraint(expr= (m.x54 - m.x63)**2 + (m.x133 - m.x142)**2 + (m.x212
    - m.x221)**2 >= 0.46785600000000005)
m.e2766 = Constraint(expr= (m.x54 - m.x64)**2 + (m.x133 - m.x143)**2 + (m.x212
    - m.x222)**2 >= 0.46785600000000005)
m.e2767 = Constraint(expr= (m.x54 - m.x65)**2 + (m.x133 - m.x144)**2 + (m.x212
    - m.x223)**2 >= 0.46785600000000005)
m.e2768 = Constraint(expr= (m.x54 - m.x66)**2 + (m.x133 - m.x145)**2 + (m.x212
    - m.x224)**2 >= 0.46785600000000005)
m.e2769 = Constraint(expr= (m.x54 - m.x67)**2 + (m.x133 - m.x146)**2 + (m.x212
    - m.x225)**2 >= 0.46785600000000005)
m.e2770 = Constraint(expr= (m.x54 - m.x68)**2 + (m.x133 - m.x147)**2 + (m.x212
    - m.x226)**2 >= 0.46785600000000005)
m.e2771 = Constraint(expr= (m.x54 - m.x69)**2 + (m.x133 - m.x148)**2 + (m.x212
    - m.x227)**2 >= 0.46785600000000005)
m.e2772 = Constraint(expr= (m.x54 - m.x70)**2 + (m.x133 - m.x149)**2 + (m.x212
    - m.x228)**2 >= 0.46785600000000005)
m.e2773 = Constraint(expr= (m.x54 - m.x71)**2 + (m.x133 - m.x150)**2 + (m.x212
    - m.x229)**2 >= 0.46785600000000005)
m.e2774 = Constraint(expr= (m.x54 - m.x72)**2 + (m.x133 - m.x151)**2 + (m.x212
    - m.x230)**2 >= 0.46785600000000005)
m.e2775 = Constraint(expr= (m.x54 - m.x73)**2 + (m.x133 - m.x152)**2 + (m.x212
    - m.x231)**2 >= 0.46785600000000005)
m.e2776 = Constraint(expr= (m.x54 - m.x74)**2 + (m.x133 - m.x153)**2 + (m.x212
    - m.x232)**2 >= 0.46785600000000005)
m.e2777 = Constraint(expr= (m.x54 - m.x75)**2 + (m.x133 - m.x154)**2 + (m.x212
    - m.x233)**2 >= 0.46785600000000005)
m.e2778 = Constraint(expr= (m.x54 - m.x76)**2 + (m.x133 - m.x155)**2 + (m.x212
    - m.x234)**2 >= 0.46785600000000005)
m.e2779 = Constraint(expr= (m.x54 - m.x77)**2 + (m.x133 - m.x156)**2 + (m.x212
    - m.x235)**2 >= 0.46785600000000005)
m.e2780 = Constraint(expr= (m.x54 - m.x78)**2 + (m.x133 - m.x157)**2 + (m.x212
    - m.x236)**2 >= 0.46785600000000005)
m.e2781 = Constraint(expr= (m.x54 - m.x79)**2 + (m.x133 - m.x158)**2 + (m.x212
    - m.x237)**2 >= 0.46785600000000005)
m.e2782 = Constraint(expr= (m.x55 - m.x56)**2 + (m.x134 - m.x135)**2 + (m.x213
    - m.x214)**2 >= 0.46785600000000005)
m.e2783 = Constraint(expr= (m.x55 - m.x57)**2 + (m.x134 - m.x136)**2 + (m.x213
    - m.x215)**2 >= 0.46785600000000005)
m.e2784 = Constraint(expr= (m.x55 - m.x58)**2 + (m.x134 - m.x137)**2 + (m.x213
    - m.x216)**2 >= 0.46785600000000005)
m.e2785 = Constraint(expr= (m.x55 - m.x59)**2 + (m.x134 - m.x138)**2 + (m.x213
    - m.x217)**2 >= 0.46785600000000005)
m.e2786 = Constraint(expr= (m.x55 - m.x60)**2 + (m.x134 - m.x139)**2 + (m.x213
    - m.x218)**2 >= 0.46785600000000005)
m.e2787 = Constraint(expr= (m.x55 - m.x61)**2 + (m.x134 - m.x140)**2 + (m.x213
    - m.x219)**2 >= 0.46785600000000005)
m.e2788 = Constraint(expr= (m.x55 - m.x62)**2 + (m.x134 - m.x141)**2 + (m.x213
    - m.x220)**2 >= 0.46785600000000005)
m.e2789 = Constraint(expr= (m.x55 - m.x63)**2 + (m.x134 - m.x142)**2 + (m.x213
    - m.x221)**2 >= 0.46785600000000005)
m.e2790 = Constraint(expr= (m.x55 - m.x64)**2 + (m.x134 - m.x143)**2 + (m.x213
    - m.x222)**2 >= 0.46785600000000005)
m.e2791 = Constraint(expr= (m.x55 - m.x65)**2 + (m.x134 - m.x144)**2 + (m.x213
    - m.x223)**2 >= 0.46785600000000005)
m.e2792 = Constraint(expr= (m.x55 - m.x66)**2 + (m.x134 - m.x145)**2 + (m.x213
    - m.x224)**2 >= 0.46785600000000005)
m.e2793 = Constraint(expr= (m.x55 - m.x67)**2 + (m.x134 - m.x146)**2 + (m.x213
    - m.x225)**2 >= 0.46785600000000005)
m.e2794 = Constraint(expr= (m.x55 - m.x68)**2 + (m.x134 - m.x147)**2 + (m.x213
    - m.x226)**2 >= 0.46785600000000005)
m.e2795 = Constraint(expr= (m.x55 - m.x69)**2 + (m.x134 - m.x148)**2 + (m.x213
    - m.x227)**2 >= 0.46785600000000005)
m.e2796 = Constraint(expr= (m.x55 - m.x70)**2 + (m.x134 - m.x149)**2 + (m.x213
    - m.x228)**2 >= 0.46785600000000005)
m.e2797 = Constraint(expr= (m.x55 - m.x71)**2 + (m.x134 - m.x150)**2 + (m.x213
    - m.x229)**2 >= 0.46785600000000005)
m.e2798 = Constraint(expr= (m.x55 - m.x72)**2 + (m.x134 - m.x151)**2 + (m.x213
    - m.x230)**2 >= 0.46785600000000005)
m.e2799 = Constraint(expr= (m.x55 - m.x73)**2 + (m.x134 - m.x152)**2 + (m.x213
    - m.x231)**2 >= 0.46785600000000005)
m.e2800 = Constraint(expr= (m.x55 - m.x74)**2 + (m.x134 - m.x153)**2 + (m.x213
    - m.x232)**2 >= 0.46785600000000005)
m.e2801 = Constraint(expr= (m.x55 - m.x75)**2 + (m.x134 - m.x154)**2 + (m.x213
    - m.x233)**2 >= 0.46785600000000005)
m.e2802 = Constraint(expr= (m.x55 - m.x76)**2 + (m.x134 - m.x155)**2 + (m.x213
    - m.x234)**2 >= 0.46785600000000005)
m.e2803 = Constraint(expr= (m.x55 - m.x77)**2 + (m.x134 - m.x156)**2 + (m.x213
    - m.x235)**2 >= 0.46785600000000005)
m.e2804 = Constraint(expr= (m.x55 - m.x78)**2 + (m.x134 - m.x157)**2 + (m.x213
    - m.x236)**2 >= 0.46785600000000005)
m.e2805 = Constraint(expr= (m.x55 - m.x79)**2 + (m.x134 - m.x158)**2 + (m.x213
    - m.x237)**2 >= 0.46785600000000005)
m.e2806 = Constraint(expr= (m.x56 - m.x57)**2 + (m.x135 - m.x136)**2 + (m.x214
    - m.x215)**2 >= 0.46785600000000005)
m.e2807 = Constraint(expr= (m.x56 - m.x58)**2 + (m.x135 - m.x137)**2 + (m.x214
    - m.x216)**2 >= 0.46785600000000005)
m.e2808 = Constraint(expr= (m.x56 - m.x59)**2 + (m.x135 - m.x138)**2 + (m.x214
    - m.x217)**2 >= 0.46785600000000005)
m.e2809 = Constraint(expr= (m.x56 - m.x60)**2 + (m.x135 - m.x139)**2 + (m.x214
    - m.x218)**2 >= 0.46785600000000005)
m.e2810 = Constraint(expr= (m.x56 - m.x61)**2 + (m.x135 - m.x140)**2 + (m.x214
    - m.x219)**2 >= 0.46785600000000005)
m.e2811 = Constraint(expr= (m.x56 - m.x62)**2 + (m.x135 - m.x141)**2 + (m.x214
    - m.x220)**2 >= 0.46785600000000005)
m.e2812 = Constraint(expr= (m.x56 - m.x63)**2 + (m.x135 - m.x142)**2 + (m.x214
    - m.x221)**2 >= 0.46785600000000005)
m.e2813 = Constraint(expr= (m.x56 - m.x64)**2 + (m.x135 - m.x143)**2 + (m.x214
    - m.x222)**2 >= 0.46785600000000005)
m.e2814 = Constraint(expr= (m.x56 - m.x65)**2 + (m.x135 - m.x144)**2 + (m.x214
    - m.x223)**2 >= 0.46785600000000005)
m.e2815 = Constraint(expr= (m.x56 - m.x66)**2 + (m.x135 - m.x145)**2 + (m.x214
    - m.x224)**2 >= 0.46785600000000005)
m.e2816 = Constraint(expr= (m.x56 - m.x67)**2 + (m.x135 - m.x146)**2 + (m.x214
    - m.x225)**2 >= 0.46785600000000005)
m.e2817 = Constraint(expr= (m.x56 - m.x68)**2 + (m.x135 - m.x147)**2 + (m.x214
    - m.x226)**2 >= 0.46785600000000005)
m.e2818 = Constraint(expr= (m.x56 - m.x69)**2 + (m.x135 - m.x148)**2 + (m.x214
    - m.x227)**2 >= 0.46785600000000005)
m.e2819 = Constraint(expr= (m.x56 - m.x70)**2 + (m.x135 - m.x149)**2 + (m.x214
    - m.x228)**2 >= 0.46785600000000005)
m.e2820 = Constraint(expr= (m.x56 - m.x71)**2 + (m.x135 - m.x150)**2 + (m.x214
    - m.x229)**2 >= 0.46785600000000005)
m.e2821 = Constraint(expr= (m.x56 - m.x72)**2 + (m.x135 - m.x151)**2 + (m.x214
    - m.x230)**2 >= 0.46785600000000005)
m.e2822 = Constraint(expr= (m.x56 - m.x73)**2 + (m.x135 - m.x152)**2 + (m.x214
    - m.x231)**2 >= 0.46785600000000005)
m.e2823 = Constraint(expr= (m.x56 - m.x74)**2 + (m.x135 - m.x153)**2 + (m.x214
    - m.x232)**2 >= 0.46785600000000005)
m.e2824 = Constraint(expr= (m.x56 - m.x75)**2 + (m.x135 - m.x154)**2 + (m.x214
    - m.x233)**2 >= 0.46785600000000005)
m.e2825 = Constraint(expr= (m.x56 - m.x76)**2 + (m.x135 - m.x155)**2 + (m.x214
    - m.x234)**2 >= 0.46785600000000005)
m.e2826 = Constraint(expr= (m.x56 - m.x77)**2 + (m.x135 - m.x156)**2 + (m.x214
    - m.x235)**2 >= 0.46785600000000005)
m.e2827 = Constraint(expr= (m.x56 - m.x78)**2 + (m.x135 - m.x157)**2 + (m.x214
    - m.x236)**2 >= 0.46785600000000005)
m.e2828 = Constraint(expr= (m.x56 - m.x79)**2 + (m.x135 - m.x158)**2 + (m.x214
    - m.x237)**2 >= 0.46785600000000005)
m.e2829 = Constraint(expr= (m.x57 - m.x58)**2 + (m.x136 - m.x137)**2 + (m.x215
    - m.x216)**2 >= 0.46785600000000005)
m.e2830 = Constraint(expr= (m.x57 - m.x59)**2 + (m.x136 - m.x138)**2 + (m.x215
    - m.x217)**2 >= 0.46785600000000005)
m.e2831 = Constraint(expr= (m.x57 - m.x60)**2 + (m.x136 - m.x139)**2 + (m.x215
    - m.x218)**2 >= 0.46785600000000005)
m.e2832 = Constraint(expr= (m.x57 - m.x61)**2 + (m.x136 - m.x140)**2 + (m.x215
    - m.x219)**2 >= 0.46785600000000005)
m.e2833 = Constraint(expr= (m.x57 - m.x62)**2 + (m.x136 - m.x141)**2 + (m.x215
    - m.x220)**2 >= 0.46785600000000005)
m.e2834 = Constraint(expr= (m.x57 - m.x63)**2 + (m.x136 - m.x142)**2 + (m.x215
    - m.x221)**2 >= 0.46785600000000005)
m.e2835 = Constraint(expr= (m.x57 - m.x64)**2 + (m.x136 - m.x143)**2 + (m.x215
    - m.x222)**2 >= 0.46785600000000005)
m.e2836 = Constraint(expr= (m.x57 - m.x65)**2 + (m.x136 - m.x144)**2 + (m.x215
    - m.x223)**2 >= 0.46785600000000005)
m.e2837 = Constraint(expr= (m.x57 - m.x66)**2 + (m.x136 - m.x145)**2 + (m.x215
    - m.x224)**2 >= 0.46785600000000005)
m.e2838 = Constraint(expr= (m.x57 - m.x67)**2 + (m.x136 - m.x146)**2 + (m.x215
    - m.x225)**2 >= 0.46785600000000005)
m.e2839 = Constraint(expr= (m.x57 - m.x68)**2 + (m.x136 - m.x147)**2 + (m.x215
    - m.x226)**2 >= 0.46785600000000005)
m.e2840 = Constraint(expr= (m.x57 - m.x69)**2 + (m.x136 - m.x148)**2 + (m.x215
    - m.x227)**2 >= 0.46785600000000005)
m.e2841 = Constraint(expr= (m.x57 - m.x70)**2 + (m.x136 - m.x149)**2 + (m.x215
    - m.x228)**2 >= 0.46785600000000005)
m.e2842 = Constraint(expr= (m.x57 - m.x71)**2 + (m.x136 - m.x150)**2 + (m.x215
    - m.x229)**2 >= 0.46785600000000005)
m.e2843 = Constraint(expr= (m.x57 - m.x72)**2 + (m.x136 - m.x151)**2 + (m.x215
    - m.x230)**2 >= 0.46785600000000005)
m.e2844 = Constraint(expr= (m.x57 - m.x73)**2 + (m.x136 - m.x152)**2 + (m.x215
    - m.x231)**2 >= 0.46785600000000005)
m.e2845 = Constraint(expr= (m.x57 - m.x74)**2 + (m.x136 - m.x153)**2 + (m.x215
    - m.x232)**2 >= 0.46785600000000005)
m.e2846 = Constraint(expr= (m.x57 - m.x75)**2 + (m.x136 - m.x154)**2 + (m.x215
    - m.x233)**2 >= 0.46785600000000005)
m.e2847 = Constraint(expr= (m.x57 - m.x76)**2 + (m.x136 - m.x155)**2 + (m.x215
    - m.x234)**2 >= 0.46785600000000005)
m.e2848 = Constraint(expr= (m.x57 - m.x77)**2 + (m.x136 - m.x156)**2 + (m.x215
    - m.x235)**2 >= 0.46785600000000005)
m.e2849 = Constraint(expr= (m.x57 - m.x78)**2 + (m.x136 - m.x157)**2 + (m.x215
    - m.x236)**2 >= 0.46785600000000005)
m.e2850 = Constraint(expr= (m.x57 - m.x79)**2 + (m.x136 - m.x158)**2 + (m.x215
    - m.x237)**2 >= 0.46785600000000005)
m.e2851 = Constraint(expr= (m.x58 - m.x59)**2 + (m.x137 - m.x138)**2 + (m.x216
    - m.x217)**2 >= 0.46785600000000005)
m.e2852 = Constraint(expr= (m.x58 - m.x60)**2 + (m.x137 - m.x139)**2 + (m.x216
    - m.x218)**2 >= 0.46785600000000005)
m.e2853 = Constraint(expr= (m.x58 - m.x61)**2 + (m.x137 - m.x140)**2 + (m.x216
    - m.x219)**2 >= 0.46785600000000005)
m.e2854 = Constraint(expr= (m.x58 - m.x62)**2 + (m.x137 - m.x141)**2 + (m.x216
    - m.x220)**2 >= 0.46785600000000005)
m.e2855 = Constraint(expr= (m.x58 - m.x63)**2 + (m.x137 - m.x142)**2 + (m.x216
    - m.x221)**2 >= 0.46785600000000005)
m.e2856 = Constraint(expr= (m.x58 - m.x64)**2 + (m.x137 - m.x143)**2 + (m.x216
    - m.x222)**2 >= 0.46785600000000005)
m.e2857 = Constraint(expr= (m.x58 - m.x65)**2 + (m.x137 - m.x144)**2 + (m.x216
    - m.x223)**2 >= 0.46785600000000005)
m.e2858 = Constraint(expr= (m.x58 - m.x66)**2 + (m.x137 - m.x145)**2 + (m.x216
    - m.x224)**2 >= 0.46785600000000005)
m.e2859 = Constraint(expr= (m.x58 - m.x67)**2 + (m.x137 - m.x146)**2 + (m.x216
    - m.x225)**2 >= 0.46785600000000005)
m.e2860 = Constraint(expr= (m.x58 - m.x68)**2 + (m.x137 - m.x147)**2 + (m.x216
    - m.x226)**2 >= 0.46785600000000005)
m.e2861 = Constraint(expr= (m.x58 - m.x69)**2 + (m.x137 - m.x148)**2 + (m.x216
    - m.x227)**2 >= 0.46785600000000005)
m.e2862 = Constraint(expr= (m.x58 - m.x70)**2 + (m.x137 - m.x149)**2 + (m.x216
    - m.x228)**2 >= 0.46785600000000005)
m.e2863 = Constraint(expr= (m.x58 - m.x71)**2 + (m.x137 - m.x150)**2 + (m.x216
    - m.x229)**2 >= 0.46785600000000005)
m.e2864 = Constraint(expr= (m.x58 - m.x72)**2 + (m.x137 - m.x151)**2 + (m.x216
    - m.x230)**2 >= 0.46785600000000005)
m.e2865 = Constraint(expr= (m.x58 - m.x73)**2 + (m.x137 - m.x152)**2 + (m.x216
    - m.x231)**2 >= 0.46785600000000005)
m.e2866 = Constraint(expr= (m.x58 - m.x74)**2 + (m.x137 - m.x153)**2 + (m.x216
    - m.x232)**2 >= 0.46785600000000005)
m.e2867 = Constraint(expr= (m.x58 - m.x75)**2 + (m.x137 - m.x154)**2 + (m.x216
    - m.x233)**2 >= 0.46785600000000005)
m.e2868 = Constraint(expr= (m.x58 - m.x76)**2 + (m.x137 - m.x155)**2 + (m.x216
    - m.x234)**2 >= 0.46785600000000005)
m.e2869 = Constraint(expr= (m.x58 - m.x77)**2 + (m.x137 - m.x156)**2 + (m.x216
    - m.x235)**2 >= 0.46785600000000005)
m.e2870 = Constraint(expr= (m.x58 - m.x78)**2 + (m.x137 - m.x157)**2 + (m.x216
    - m.x236)**2 >= 0.46785600000000005)
m.e2871 = Constraint(expr= (m.x58 - m.x79)**2 + (m.x137 - m.x158)**2 + (m.x216
    - m.x237)**2 >= 0.46785600000000005)
m.e2872 = Constraint(expr= (m.x59 - m.x60)**2 + (m.x138 - m.x139)**2 + (m.x217
    - m.x218)**2 >= 0.46785600000000005)
m.e2873 = Constraint(expr= (m.x59 - m.x61)**2 + (m.x138 - m.x140)**2 + (m.x217
    - m.x219)**2 >= 0.46785600000000005)
m.e2874 = Constraint(expr= (m.x59 - m.x62)**2 + (m.x138 - m.x141)**2 + (m.x217
    - m.x220)**2 >= 0.46785600000000005)
m.e2875 = Constraint(expr= (m.x59 - m.x63)**2 + (m.x138 - m.x142)**2 + (m.x217
    - m.x221)**2 >= 0.46785600000000005)
m.e2876 = Constraint(expr= (m.x59 - m.x64)**2 + (m.x138 - m.x143)**2 + (m.x217
    - m.x222)**2 >= 0.46785600000000005)
m.e2877 = Constraint(expr= (m.x59 - m.x65)**2 + (m.x138 - m.x144)**2 + (m.x217
    - m.x223)**2 >= 0.46785600000000005)
m.e2878 = Constraint(expr= (m.x59 - m.x66)**2 + (m.x138 - m.x145)**2 + (m.x217
    - m.x224)**2 >= 0.46785600000000005)
m.e2879 = Constraint(expr= (m.x59 - m.x67)**2 + (m.x138 - m.x146)**2 + (m.x217
    - m.x225)**2 >= 0.46785600000000005)
m.e2880 = Constraint(expr= (m.x59 - m.x68)**2 + (m.x138 - m.x147)**2 + (m.x217
    - m.x226)**2 >= 0.46785600000000005)
m.e2881 = Constraint(expr= (m.x59 - m.x69)**2 + (m.x138 - m.x148)**2 + (m.x217
    - m.x227)**2 >= 0.46785600000000005)
m.e2882 = Constraint(expr= (m.x59 - m.x70)**2 + (m.x138 - m.x149)**2 + (m.x217
    - m.x228)**2 >= 0.46785600000000005)
m.e2883 = Constraint(expr= (m.x59 - m.x71)**2 + (m.x138 - m.x150)**2 + (m.x217
    - m.x229)**2 >= 0.46785600000000005)
m.e2884 = Constraint(expr= (m.x59 - m.x72)**2 + (m.x138 - m.x151)**2 + (m.x217
    - m.x230)**2 >= 0.46785600000000005)
m.e2885 = Constraint(expr= (m.x59 - m.x73)**2 + (m.x138 - m.x152)**2 + (m.x217
    - m.x231)**2 >= 0.46785600000000005)
m.e2886 = Constraint(expr= (m.x59 - m.x74)**2 + (m.x138 - m.x153)**2 + (m.x217
    - m.x232)**2 >= 0.46785600000000005)
m.e2887 = Constraint(expr= (m.x59 - m.x75)**2 + (m.x138 - m.x154)**2 + (m.x217
    - m.x233)**2 >= 0.46785600000000005)
m.e2888 = Constraint(expr= (m.x59 - m.x76)**2 + (m.x138 - m.x155)**2 + (m.x217
    - m.x234)**2 >= 0.46785600000000005)
m.e2889 = Constraint(expr= (m.x59 - m.x77)**2 + (m.x138 - m.x156)**2 + (m.x217
    - m.x235)**2 >= 0.46785600000000005)
m.e2890 = Constraint(expr= (m.x59 - m.x78)**2 + (m.x138 - m.x157)**2 + (m.x217
    - m.x236)**2 >= 0.46785600000000005)
m.e2891 = Constraint(expr= (m.x59 - m.x79)**2 + (m.x138 - m.x158)**2 + (m.x217
    - m.x237)**2 >= 0.46785600000000005)
m.e2892 = Constraint(expr= (m.x60 - m.x61)**2 + (m.x139 - m.x140)**2 + (m.x218
    - m.x219)**2 >= 0.46785600000000005)
m.e2893 = Constraint(expr= (m.x60 - m.x62)**2 + (m.x139 - m.x141)**2 + (m.x218
    - m.x220)**2 >= 0.46785600000000005)
m.e2894 = Constraint(expr= (m.x60 - m.x63)**2 + (m.x139 - m.x142)**2 + (m.x218
    - m.x221)**2 >= 0.46785600000000005)
m.e2895 = Constraint(expr= (m.x60 - m.x64)**2 + (m.x139 - m.x143)**2 + (m.x218
    - m.x222)**2 >= 0.46785600000000005)
m.e2896 = Constraint(expr= (m.x60 - m.x65)**2 + (m.x139 - m.x144)**2 + (m.x218
    - m.x223)**2 >= 0.46785600000000005)
m.e2897 = Constraint(expr= (m.x60 - m.x66)**2 + (m.x139 - m.x145)**2 + (m.x218
    - m.x224)**2 >= 0.46785600000000005)
m.e2898 = Constraint(expr= (m.x60 - m.x67)**2 + (m.x139 - m.x146)**2 + (m.x218
    - m.x225)**2 >= 0.46785600000000005)
m.e2899 = Constraint(expr= (m.x60 - m.x68)**2 + (m.x139 - m.x147)**2 + (m.x218
    - m.x226)**2 >= 0.46785600000000005)
m.e2900 = Constraint(expr= (m.x60 - m.x69)**2 + (m.x139 - m.x148)**2 + (m.x218
    - m.x227)**2 >= 0.46785600000000005)
m.e2901 = Constraint(expr= (m.x60 - m.x70)**2 + (m.x139 - m.x149)**2 + (m.x218
    - m.x228)**2 >= 0.46785600000000005)
m.e2902 = Constraint(expr= (m.x60 - m.x71)**2 + (m.x139 - m.x150)**2 + (m.x218
    - m.x229)**2 >= 0.46785600000000005)
m.e2903 = Constraint(expr= (m.x60 - m.x72)**2 + (m.x139 - m.x151)**2 + (m.x218
    - m.x230)**2 >= 0.46785600000000005)
m.e2904 = Constraint(expr= (m.x60 - m.x73)**2 + (m.x139 - m.x152)**2 + (m.x218
    - m.x231)**2 >= 0.46785600000000005)
m.e2905 = Constraint(expr= (m.x60 - m.x74)**2 + (m.x139 - m.x153)**2 + (m.x218
    - m.x232)**2 >= 0.46785600000000005)
m.e2906 = Constraint(expr= (m.x60 - m.x75)**2 + (m.x139 - m.x154)**2 + (m.x218
    - m.x233)**2 >= 0.46785600000000005)
m.e2907 = Constraint(expr= (m.x60 - m.x76)**2 + (m.x139 - m.x155)**2 + (m.x218
    - m.x234)**2 >= 0.46785600000000005)
m.e2908 = Constraint(expr= (m.x60 - m.x77)**2 + (m.x139 - m.x156)**2 + (m.x218
    - m.x235)**2 >= 0.46785600000000005)
m.e2909 = Constraint(expr= (m.x60 - m.x78)**2 + (m.x139 - m.x157)**2 + (m.x218
    - m.x236)**2 >= 0.46785600000000005)
m.e2910 = Constraint(expr= (m.x60 - m.x79)**2 + (m.x139 - m.x158)**2 + (m.x218
    - m.x237)**2 >= 0.46785600000000005)
m.e2911 = Constraint(expr= (m.x61 - m.x62)**2 + (m.x140 - m.x141)**2 + (m.x219
    - m.x220)**2 >= 0.46785600000000005)
m.e2912 = Constraint(expr= (m.x61 - m.x63)**2 + (m.x140 - m.x142)**2 + (m.x219
    - m.x221)**2 >= 0.46785600000000005)
m.e2913 = Constraint(expr= (m.x61 - m.x64)**2 + (m.x140 - m.x143)**2 + (m.x219
    - m.x222)**2 >= 0.46785600000000005)
m.e2914 = Constraint(expr= (m.x61 - m.x65)**2 + (m.x140 - m.x144)**2 + (m.x219
    - m.x223)**2 >= 0.46785600000000005)
m.e2915 = Constraint(expr= (m.x61 - m.x66)**2 + (m.x140 - m.x145)**2 + (m.x219
    - m.x224)**2 >= 0.46785600000000005)
m.e2916 = Constraint(expr= (m.x61 - m.x67)**2 + (m.x140 - m.x146)**2 + (m.x219
    - m.x225)**2 >= 0.46785600000000005)
m.e2917 = Constraint(expr= (m.x61 - m.x68)**2 + (m.x140 - m.x147)**2 + (m.x219
    - m.x226)**2 >= 0.46785600000000005)
m.e2918 = Constraint(expr= (m.x61 - m.x69)**2 + (m.x140 - m.x148)**2 + (m.x219
    - m.x227)**2 >= 0.46785600000000005)
m.e2919 = Constraint(expr= (m.x61 - m.x70)**2 + (m.x140 - m.x149)**2 + (m.x219
    - m.x228)**2 >= 0.46785600000000005)
m.e2920 = Constraint(expr= (m.x61 - m.x71)**2 + (m.x140 - m.x150)**2 + (m.x219
    - m.x229)**2 >= 0.46785600000000005)
m.e2921 = Constraint(expr= (m.x61 - m.x72)**2 + (m.x140 - m.x151)**2 + (m.x219
    - m.x230)**2 >= 0.46785600000000005)
m.e2922 = Constraint(expr= (m.x61 - m.x73)**2 + (m.x140 - m.x152)**2 + (m.x219
    - m.x231)**2 >= 0.46785600000000005)
m.e2923 = Constraint(expr= (m.x61 - m.x74)**2 + (m.x140 - m.x153)**2 + (m.x219
    - m.x232)**2 >= 0.46785600000000005)
m.e2924 = Constraint(expr= (m.x61 - m.x75)**2 + (m.x140 - m.x154)**2 + (m.x219
    - m.x233)**2 >= 0.46785600000000005)
m.e2925 = Constraint(expr= (m.x61 - m.x76)**2 + (m.x140 - m.x155)**2 + (m.x219
    - m.x234)**2 >= 0.46785600000000005)
m.e2926 = Constraint(expr= (m.x61 - m.x77)**2 + (m.x140 - m.x156)**2 + (m.x219
    - m.x235)**2 >= 0.46785600000000005)
m.e2927 = Constraint(expr= (m.x61 - m.x78)**2 + (m.x140 - m.x157)**2 + (m.x219
    - m.x236)**2 >= 0.46785600000000005)
m.e2928 = Constraint(expr= (m.x61 - m.x79)**2 + (m.x140 - m.x158)**2 + (m.x219
    - m.x237)**2 >= 0.46785600000000005)
m.e2929 = Constraint(expr= (m.x62 - m.x63)**2 + (m.x141 - m.x142)**2 + (m.x220
    - m.x221)**2 >= 0.46785600000000005)
m.e2930 = Constraint(expr= (m.x62 - m.x64)**2 + (m.x141 - m.x143)**2 + (m.x220
    - m.x222)**2 >= 0.46785600000000005)
m.e2931 = Constraint(expr= (m.x62 - m.x65)**2 + (m.x141 - m.x144)**2 + (m.x220
    - m.x223)**2 >= 0.46785600000000005)
m.e2932 = Constraint(expr= (m.x62 - m.x66)**2 + (m.x141 - m.x145)**2 + (m.x220
    - m.x224)**2 >= 0.46785600000000005)
m.e2933 = Constraint(expr= (m.x62 - m.x67)**2 + (m.x141 - m.x146)**2 + (m.x220
    - m.x225)**2 >= 0.46785600000000005)
m.e2934 = Constraint(expr= (m.x62 - m.x68)**2 + (m.x141 - m.x147)**2 + (m.x220
    - m.x226)**2 >= 0.46785600000000005)
m.e2935 = Constraint(expr= (m.x62 - m.x69)**2 + (m.x141 - m.x148)**2 + (m.x220
    - m.x227)**2 >= 0.46785600000000005)
m.e2936 = Constraint(expr= (m.x62 - m.x70)**2 + (m.x141 - m.x149)**2 + (m.x220
    - m.x228)**2 >= 0.46785600000000005)
m.e2937 = Constraint(expr= (m.x62 - m.x71)**2 + (m.x141 - m.x150)**2 + (m.x220
    - m.x229)**2 >= 0.46785600000000005)
m.e2938 = Constraint(expr= (m.x62 - m.x72)**2 + (m.x141 - m.x151)**2 + (m.x220
    - m.x230)**2 >= 0.46785600000000005)
m.e2939 = Constraint(expr= (m.x62 - m.x73)**2 + (m.x141 - m.x152)**2 + (m.x220
    - m.x231)**2 >= 0.46785600000000005)
m.e2940 = Constraint(expr= (m.x62 - m.x74)**2 + (m.x141 - m.x153)**2 + (m.x220
    - m.x232)**2 >= 0.46785600000000005)
m.e2941 = Constraint(expr= (m.x62 - m.x75)**2 + (m.x141 - m.x154)**2 + (m.x220
    - m.x233)**2 >= 0.46785600000000005)
m.e2942 = Constraint(expr= (m.x62 - m.x76)**2 + (m.x141 - m.x155)**2 + (m.x220
    - m.x234)**2 >= 0.46785600000000005)
m.e2943 = Constraint(expr= (m.x62 - m.x77)**2 + (m.x141 - m.x156)**2 + (m.x220
    - m.x235)**2 >= 0.46785600000000005)
m.e2944 = Constraint(expr= (m.x62 - m.x78)**2 + (m.x141 - m.x157)**2 + (m.x220
    - m.x236)**2 >= 0.46785600000000005)
m.e2945 = Constraint(expr= (m.x62 - m.x79)**2 + (m.x141 - m.x158)**2 + (m.x220
    - m.x237)**2 >= 0.46785600000000005)
m.e2946 = Constraint(expr= (m.x63 - m.x64)**2 + (m.x142 - m.x143)**2 + (m.x221
    - m.x222)**2 >= 0.46785600000000005)
m.e2947 = Constraint(expr= (m.x63 - m.x65)**2 + (m.x142 - m.x144)**2 + (m.x221
    - m.x223)**2 >= 0.46785600000000005)
m.e2948 = Constraint(expr= (m.x63 - m.x66)**2 + (m.x142 - m.x145)**2 + (m.x221
    - m.x224)**2 >= 0.46785600000000005)
m.e2949 = Constraint(expr= (m.x63 - m.x67)**2 + (m.x142 - m.x146)**2 + (m.x221
    - m.x225)**2 >= 0.46785600000000005)
m.e2950 = Constraint(expr= (m.x63 - m.x68)**2 + (m.x142 - m.x147)**2 + (m.x221
    - m.x226)**2 >= 0.46785600000000005)
m.e2951 = Constraint(expr= (m.x63 - m.x69)**2 + (m.x142 - m.x148)**2 + (m.x221
    - m.x227)**2 >= 0.46785600000000005)
m.e2952 = Constraint(expr= (m.x63 - m.x70)**2 + (m.x142 - m.x149)**2 + (m.x221
    - m.x228)**2 >= 0.46785600000000005)
m.e2953 = Constraint(expr= (m.x63 - m.x71)**2 + (m.x142 - m.x150)**2 + (m.x221
    - m.x229)**2 >= 0.46785600000000005)
m.e2954 = Constraint(expr= (m.x63 - m.x72)**2 + (m.x142 - m.x151)**2 + (m.x221
    - m.x230)**2 >= 0.46785600000000005)
m.e2955 = Constraint(expr= (m.x63 - m.x73)**2 + (m.x142 - m.x152)**2 + (m.x221
    - m.x231)**2 >= 0.46785600000000005)
m.e2956 = Constraint(expr= (m.x63 - m.x74)**2 + (m.x142 - m.x153)**2 + (m.x221
    - m.x232)**2 >= 0.46785600000000005)
m.e2957 = Constraint(expr= (m.x63 - m.x75)**2 + (m.x142 - m.x154)**2 + (m.x221
    - m.x233)**2 >= 0.46785600000000005)
m.e2958 = Constraint(expr= (m.x63 - m.x76)**2 + (m.x142 - m.x155)**2 + (m.x221
    - m.x234)**2 >= 0.46785600000000005)
m.e2959 = Constraint(expr= (m.x63 - m.x77)**2 + (m.x142 - m.x156)**2 + (m.x221
    - m.x235)**2 >= 0.46785600000000005)
m.e2960 = Constraint(expr= (m.x63 - m.x78)**2 + (m.x142 - m.x157)**2 + (m.x221
    - m.x236)**2 >= 0.46785600000000005)
m.e2961 = Constraint(expr= (m.x63 - m.x79)**2 + (m.x142 - m.x158)**2 + (m.x221
    - m.x237)**2 >= 0.46785600000000005)
m.e2962 = Constraint(expr= (m.x64 - m.x65)**2 + (m.x143 - m.x144)**2 + (m.x222
    - m.x223)**2 >= 0.46785600000000005)
m.e2963 = Constraint(expr= (m.x64 - m.x66)**2 + (m.x143 - m.x145)**2 + (m.x222
    - m.x224)**2 >= 0.46785600000000005)
m.e2964 = Constraint(expr= (m.x64 - m.x67)**2 + (m.x143 - m.x146)**2 + (m.x222
    - m.x225)**2 >= 0.46785600000000005)
m.e2965 = Constraint(expr= (m.x64 - m.x68)**2 + (m.x143 - m.x147)**2 + (m.x222
    - m.x226)**2 >= 0.46785600000000005)
m.e2966 = Constraint(expr= (m.x64 - m.x69)**2 + (m.x143 - m.x148)**2 + (m.x222
    - m.x227)**2 >= 0.46785600000000005)
m.e2967 = Constraint(expr= (m.x64 - m.x70)**2 + (m.x143 - m.x149)**2 + (m.x222
    - m.x228)**2 >= 0.46785600000000005)
m.e2968 = Constraint(expr= (m.x64 - m.x71)**2 + (m.x143 - m.x150)**2 + (m.x222
    - m.x229)**2 >= 0.46785600000000005)
m.e2969 = Constraint(expr= (m.x64 - m.x72)**2 + (m.x143 - m.x151)**2 + (m.x222
    - m.x230)**2 >= 0.46785600000000005)
m.e2970 = Constraint(expr= (m.x64 - m.x73)**2 + (m.x143 - m.x152)**2 + (m.x222
    - m.x231)**2 >= 0.46785600000000005)
m.e2971 = Constraint(expr= (m.x64 - m.x74)**2 + (m.x143 - m.x153)**2 + (m.x222
    - m.x232)**2 >= 0.46785600000000005)
m.e2972 = Constraint(expr= (m.x64 - m.x75)**2 + (m.x143 - m.x154)**2 + (m.x222
    - m.x233)**2 >= 0.46785600000000005)
m.e2973 = Constraint(expr= (m.x64 - m.x76)**2 + (m.x143 - m.x155)**2 + (m.x222
    - m.x234)**2 >= 0.46785600000000005)
m.e2974 = Constraint(expr= (m.x64 - m.x77)**2 + (m.x143 - m.x156)**2 + (m.x222
    - m.x235)**2 >= 0.46785600000000005)
m.e2975 = Constraint(expr= (m.x64 - m.x78)**2 + (m.x143 - m.x157)**2 + (m.x222
    - m.x236)**2 >= 0.46785600000000005)
m.e2976 = Constraint(expr= (m.x64 - m.x79)**2 + (m.x143 - m.x158)**2 + (m.x222
    - m.x237)**2 >= 0.46785600000000005)
m.e2977 = Constraint(expr= (m.x65 - m.x66)**2 + (m.x144 - m.x145)**2 + (m.x223
    - m.x224)**2 >= 0.46785600000000005)
m.e2978 = Constraint(expr= (m.x65 - m.x67)**2 + (m.x144 - m.x146)**2 + (m.x223
    - m.x225)**2 >= 0.46785600000000005)
m.e2979 = Constraint(expr= (m.x65 - m.x68)**2 + (m.x144 - m.x147)**2 + (m.x223
    - m.x226)**2 >= 0.46785600000000005)
m.e2980 = Constraint(expr= (m.x65 - m.x69)**2 + (m.x144 - m.x148)**2 + (m.x223
    - m.x227)**2 >= 0.46785600000000005)
m.e2981 = Constraint(expr= (m.x65 - m.x70)**2 + (m.x144 - m.x149)**2 + (m.x223
    - m.x228)**2 >= 0.46785600000000005)
m.e2982 = Constraint(expr= (m.x65 - m.x71)**2 + (m.x144 - m.x150)**2 + (m.x223
    - m.x229)**2 >= 0.46785600000000005)
m.e2983 = Constraint(expr= (m.x65 - m.x72)**2 + (m.x144 - m.x151)**2 + (m.x223
    - m.x230)**2 >= 0.46785600000000005)
m.e2984 = Constraint(expr= (m.x65 - m.x73)**2 + (m.x144 - m.x152)**2 + (m.x223
    - m.x231)**2 >= 0.46785600000000005)
m.e2985 = Constraint(expr= (m.x65 - m.x74)**2 + (m.x144 - m.x153)**2 + (m.x223
    - m.x232)**2 >= 0.46785600000000005)
m.e2986 = Constraint(expr= (m.x65 - m.x75)**2 + (m.x144 - m.x154)**2 + (m.x223
    - m.x233)**2 >= 0.46785600000000005)
m.e2987 = Constraint(expr= (m.x65 - m.x76)**2 + (m.x144 - m.x155)**2 + (m.x223
    - m.x234)**2 >= 0.46785600000000005)
m.e2988 = Constraint(expr= (m.x65 - m.x77)**2 + (m.x144 - m.x156)**2 + (m.x223
    - m.x235)**2 >= 0.46785600000000005)
m.e2989 = Constraint(expr= (m.x65 - m.x78)**2 + (m.x144 - m.x157)**2 + (m.x223
    - m.x236)**2 >= 0.46785600000000005)
m.e2990 = Constraint(expr= (m.x65 - m.x79)**2 + (m.x144 - m.x158)**2 + (m.x223
    - m.x237)**2 >= 0.46785600000000005)
m.e2991 = Constraint(expr= (m.x66 - m.x67)**2 + (m.x145 - m.x146)**2 + (m.x224
    - m.x225)**2 >= 0.46785600000000005)
m.e2992 = Constraint(expr= (m.x66 - m.x68)**2 + (m.x145 - m.x147)**2 + (m.x224
    - m.x226)**2 >= 0.46785600000000005)
m.e2993 = Constraint(expr= (m.x66 - m.x69)**2 + (m.x145 - m.x148)**2 + (m.x224
    - m.x227)**2 >= 0.46785600000000005)
m.e2994 = Constraint(expr= (m.x66 - m.x70)**2 + (m.x145 - m.x149)**2 + (m.x224
    - m.x228)**2 >= 0.46785600000000005)
m.e2995 = Constraint(expr= (m.x66 - m.x71)**2 + (m.x145 - m.x150)**2 + (m.x224
    - m.x229)**2 >= 0.46785600000000005)
m.e2996 = Constraint(expr= (m.x66 - m.x72)**2 + (m.x145 - m.x151)**2 + (m.x224
    - m.x230)**2 >= 0.46785600000000005)
m.e2997 = Constraint(expr= (m.x66 - m.x73)**2 + (m.x145 - m.x152)**2 + (m.x224
    - m.x231)**2 >= 0.46785600000000005)
m.e2998 = Constraint(expr= (m.x66 - m.x74)**2 + (m.x145 - m.x153)**2 + (m.x224
    - m.x232)**2 >= 0.46785600000000005)
m.e2999 = Constraint(expr= (m.x66 - m.x75)**2 + (m.x145 - m.x154)**2 + (m.x224
    - m.x233)**2 >= 0.46785600000000005)
m.e3000 = Constraint(expr= (m.x66 - m.x76)**2 + (m.x145 - m.x155)**2 + (m.x224
    - m.x234)**2 >= 0.46785600000000005)
m.e3001 = Constraint(expr= (m.x66 - m.x77)**2 + (m.x145 - m.x156)**2 + (m.x224
    - m.x235)**2 >= 0.46785600000000005)
m.e3002 = Constraint(expr= (m.x66 - m.x78)**2 + (m.x145 - m.x157)**2 + (m.x224
    - m.x236)**2 >= 0.46785600000000005)
m.e3003 = Constraint(expr= (m.x66 - m.x79)**2 + (m.x145 - m.x158)**2 + (m.x224
    - m.x237)**2 >= 0.46785600000000005)
m.e3004 = Constraint(expr= (m.x67 - m.x68)**2 + (m.x146 - m.x147)**2 + (m.x225
    - m.x226)**2 >= 0.46785600000000005)
m.e3005 = Constraint(expr= (m.x67 - m.x69)**2 + (m.x146 - m.x148)**2 + (m.x225
    - m.x227)**2 >= 0.46785600000000005)
m.e3006 = Constraint(expr= (m.x67 - m.x70)**2 + (m.x146 - m.x149)**2 + (m.x225
    - m.x228)**2 >= 0.46785600000000005)
m.e3007 = Constraint(expr= (m.x67 - m.x71)**2 + (m.x146 - m.x150)**2 + (m.x225
    - m.x229)**2 >= 0.46785600000000005)
m.e3008 = Constraint(expr= (m.x67 - m.x72)**2 + (m.x146 - m.x151)**2 + (m.x225
    - m.x230)**2 >= 0.46785600000000005)
m.e3009 = Constraint(expr= (m.x67 - m.x73)**2 + (m.x146 - m.x152)**2 + (m.x225
    - m.x231)**2 >= 0.46785600000000005)
m.e3010 = Constraint(expr= (m.x67 - m.x74)**2 + (m.x146 - m.x153)**2 + (m.x225
    - m.x232)**2 >= 0.46785600000000005)
m.e3011 = Constraint(expr= (m.x67 - m.x75)**2 + (m.x146 - m.x154)**2 + (m.x225
    - m.x233)**2 >= 0.46785600000000005)
m.e3012 = Constraint(expr= (m.x67 - m.x76)**2 + (m.x146 - m.x155)**2 + (m.x225
    - m.x234)**2 >= 0.46785600000000005)
m.e3013 = Constraint(expr= (m.x67 - m.x77)**2 + (m.x146 - m.x156)**2 + (m.x225
    - m.x235)**2 >= 0.46785600000000005)
m.e3014 = Constraint(expr= (m.x67 - m.x78)**2 + (m.x146 - m.x157)**2 + (m.x225
    - m.x236)**2 >= 0.46785600000000005)
m.e3015 = Constraint(expr= (m.x67 - m.x79)**2 + (m.x146 - m.x158)**2 + (m.x225
    - m.x237)**2 >= 0.46785600000000005)
m.e3016 = Constraint(expr= (m.x68 - m.x69)**2 + (m.x147 - m.x148)**2 + (m.x226
    - m.x227)**2 >= 0.46785600000000005)
m.e3017 = Constraint(expr= (m.x68 - m.x70)**2 + (m.x147 - m.x149)**2 + (m.x226
    - m.x228)**2 >= 0.46785600000000005)
m.e3018 = Constraint(expr= (m.x68 - m.x71)**2 + (m.x147 - m.x150)**2 + (m.x226
    - m.x229)**2 >= 0.46785600000000005)
m.e3019 = Constraint(expr= (m.x68 - m.x72)**2 + (m.x147 - m.x151)**2 + (m.x226
    - m.x230)**2 >= 0.46785600000000005)
m.e3020 = Constraint(expr= (m.x68 - m.x73)**2 + (m.x147 - m.x152)**2 + (m.x226
    - m.x231)**2 >= 0.46785600000000005)
m.e3021 = Constraint(expr= (m.x68 - m.x74)**2 + (m.x147 - m.x153)**2 + (m.x226
    - m.x232)**2 >= 0.46785600000000005)
m.e3022 = Constraint(expr= (m.x68 - m.x75)**2 + (m.x147 - m.x154)**2 + (m.x226
    - m.x233)**2 >= 0.46785600000000005)
m.e3023 = Constraint(expr= (m.x68 - m.x76)**2 + (m.x147 - m.x155)**2 + (m.x226
    - m.x234)**2 >= 0.46785600000000005)
m.e3024 = Constraint(expr= (m.x68 - m.x77)**2 + (m.x147 - m.x156)**2 + (m.x226
    - m.x235)**2 >= 0.46785600000000005)
m.e3025 = Constraint(expr= (m.x68 - m.x78)**2 + (m.x147 - m.x157)**2 + (m.x226
    - m.x236)**2 >= 0.46785600000000005)
m.e3026 = Constraint(expr= (m.x68 - m.x79)**2 + (m.x147 - m.x158)**2 + (m.x226
    - m.x237)**2 >= 0.46785600000000005)
m.e3027 = Constraint(expr= (m.x69 - m.x70)**2 + (m.x148 - m.x149)**2 + (m.x227
    - m.x228)**2 >= 0.46785600000000005)
m.e3028 = Constraint(expr= (m.x69 - m.x71)**2 + (m.x148 - m.x150)**2 + (m.x227
    - m.x229)**2 >= 0.46785600000000005)
m.e3029 = Constraint(expr= (m.x69 - m.x72)**2 + (m.x148 - m.x151)**2 + (m.x227
    - m.x230)**2 >= 0.46785600000000005)
m.e3030 = Constraint(expr= (m.x69 - m.x73)**2 + (m.x148 - m.x152)**2 + (m.x227
    - m.x231)**2 >= 0.46785600000000005)
m.e3031 = Constraint(expr= (m.x69 - m.x74)**2 + (m.x148 - m.x153)**2 + (m.x227
    - m.x232)**2 >= 0.46785600000000005)
m.e3032 = Constraint(expr= (m.x69 - m.x75)**2 + (m.x148 - m.x154)**2 + (m.x227
    - m.x233)**2 >= 0.46785600000000005)
m.e3033 = Constraint(expr= (m.x69 - m.x76)**2 + (m.x148 - m.x155)**2 + (m.x227
    - m.x234)**2 >= 0.46785600000000005)
m.e3034 = Constraint(expr= (m.x69 - m.x77)**2 + (m.x148 - m.x156)**2 + (m.x227
    - m.x235)**2 >= 0.46785600000000005)
m.e3035 = Constraint(expr= (m.x69 - m.x78)**2 + (m.x148 - m.x157)**2 + (m.x227
    - m.x236)**2 >= 0.46785600000000005)
m.e3036 = Constraint(expr= (m.x69 - m.x79)**2 + (m.x148 - m.x158)**2 + (m.x227
    - m.x237)**2 >= 0.46785600000000005)
m.e3037 = Constraint(expr= (m.x70 - m.x71)**2 + (m.x149 - m.x150)**2 + (m.x228
    - m.x229)**2 >= 0.46785600000000005)
m.e3038 = Constraint(expr= (m.x70 - m.x72)**2 + (m.x149 - m.x151)**2 + (m.x228
    - m.x230)**2 >= 0.46785600000000005)
m.e3039 = Constraint(expr= (m.x70 - m.x73)**2 + (m.x149 - m.x152)**2 + (m.x228
    - m.x231)**2 >= 0.46785600000000005)
m.e3040 = Constraint(expr= (m.x70 - m.x74)**2 + (m.x149 - m.x153)**2 + (m.x228
    - m.x232)**2 >= 0.46785600000000005)
m.e3041 = Constraint(expr= (m.x70 - m.x75)**2 + (m.x149 - m.x154)**2 + (m.x228
    - m.x233)**2 >= 0.46785600000000005)
m.e3042 = Constraint(expr= (m.x70 - m.x76)**2 + (m.x149 - m.x155)**2 + (m.x228
    - m.x234)**2 >= 0.46785600000000005)
m.e3043 = Constraint(expr= (m.x70 - m.x77)**2 + (m.x149 - m.x156)**2 + (m.x228
    - m.x235)**2 >= 0.46785600000000005)
m.e3044 = Constraint(expr= (m.x70 - m.x78)**2 + (m.x149 - m.x157)**2 + (m.x228
    - m.x236)**2 >= 0.46785600000000005)
m.e3045 = Constraint(expr= (m.x70 - m.x79)**2 + (m.x149 - m.x158)**2 + (m.x228
    - m.x237)**2 >= 0.46785600000000005)
m.e3046 = Constraint(expr= (m.x71 - m.x72)**2 + (m.x150 - m.x151)**2 + (m.x229
    - m.x230)**2 >= 0.46785600000000005)
m.e3047 = Constraint(expr= (m.x71 - m.x73)**2 + (m.x150 - m.x152)**2 + (m.x229
    - m.x231)**2 >= 0.46785600000000005)
m.e3048 = Constraint(expr= (m.x71 - m.x74)**2 + (m.x150 - m.x153)**2 + (m.x229
    - m.x232)**2 >= 0.46785600000000005)
m.e3049 = Constraint(expr= (m.x71 - m.x75)**2 + (m.x150 - m.x154)**2 + (m.x229
    - m.x233)**2 >= 0.46785600000000005)
m.e3050 = Constraint(expr= (m.x71 - m.x76)**2 + (m.x150 - m.x155)**2 + (m.x229
    - m.x234)**2 >= 0.46785600000000005)
m.e3051 = Constraint(expr= (m.x71 - m.x77)**2 + (m.x150 - m.x156)**2 + (m.x229
    - m.x235)**2 >= 0.46785600000000005)
m.e3052 = Constraint(expr= (m.x71 - m.x78)**2 + (m.x150 - m.x157)**2 + (m.x229
    - m.x236)**2 >= 0.46785600000000005)
m.e3053 = Constraint(expr= (m.x71 - m.x79)**2 + (m.x150 - m.x158)**2 + (m.x229
    - m.x237)**2 >= 0.46785600000000005)
m.e3054 = Constraint(expr= (m.x72 - m.x73)**2 + (m.x151 - m.x152)**2 + (m.x230
    - m.x231)**2 >= 0.46785600000000005)
m.e3055 = Constraint(expr= (m.x72 - m.x74)**2 + (m.x151 - m.x153)**2 + (m.x230
    - m.x232)**2 >= 0.46785600000000005)
m.e3056 = Constraint(expr= (m.x72 - m.x75)**2 + (m.x151 - m.x154)**2 + (m.x230
    - m.x233)**2 >= 0.46785600000000005)
m.e3057 = Constraint(expr= (m.x72 - m.x76)**2 + (m.x151 - m.x155)**2 + (m.x230
    - m.x234)**2 >= 0.46785600000000005)
m.e3058 = Constraint(expr= (m.x72 - m.x77)**2 + (m.x151 - m.x156)**2 + (m.x230
    - m.x235)**2 >= 0.46785600000000005)
m.e3059 = Constraint(expr= (m.x72 - m.x78)**2 + (m.x151 - m.x157)**2 + (m.x230
    - m.x236)**2 >= 0.46785600000000005)
m.e3060 = Constraint(expr= (m.x72 - m.x79)**2 + (m.x151 - m.x158)**2 + (m.x230
    - m.x237)**2 >= 0.46785600000000005)
m.e3061 = Constraint(expr= (m.x73 - m.x74)**2 + (m.x152 - m.x153)**2 + (m.x231
    - m.x232)**2 >= 0.46785600000000005)
m.e3062 = Constraint(expr= (m.x73 - m.x75)**2 + (m.x152 - m.x154)**2 + (m.x231
    - m.x233)**2 >= 0.46785600000000005)
m.e3063 = Constraint(expr= (m.x73 - m.x76)**2 + (m.x152 - m.x155)**2 + (m.x231
    - m.x234)**2 >= 0.46785600000000005)
m.e3064 = Constraint(expr= (m.x73 - m.x77)**2 + (m.x152 - m.x156)**2 + (m.x231
    - m.x235)**2 >= 0.46785600000000005)
m.e3065 = Constraint(expr= (m.x73 - m.x78)**2 + (m.x152 - m.x157)**2 + (m.x231
    - m.x236)**2 >= 0.46785600000000005)
m.e3066 = Constraint(expr= (m.x73 - m.x79)**2 + (m.x152 - m.x158)**2 + (m.x231
    - m.x237)**2 >= 0.46785600000000005)
m.e3067 = Constraint(expr= (m.x74 - m.x75)**2 + (m.x153 - m.x154)**2 + (m.x232
    - m.x233)**2 >= 0.46785600000000005)
m.e3068 = Constraint(expr= (m.x74 - m.x76)**2 + (m.x153 - m.x155)**2 + (m.x232
    - m.x234)**2 >= 0.46785600000000005)
m.e3069 = Constraint(expr= (m.x74 - m.x77)**2 + (m.x153 - m.x156)**2 + (m.x232
    - m.x235)**2 >= 0.46785600000000005)
m.e3070 = Constraint(expr= (m.x74 - m.x78)**2 + (m.x153 - m.x157)**2 + (m.x232
    - m.x236)**2 >= 0.46785600000000005)
m.e3071 = Constraint(expr= (m.x74 - m.x79)**2 + (m.x153 - m.x158)**2 + (m.x232
    - m.x237)**2 >= 0.46785600000000005)
m.e3072 = Constraint(expr= (m.x75 - m.x76)**2 + (m.x154 - m.x155)**2 + (m.x233
    - m.x234)**2 >= 0.46785600000000005)
m.e3073 = Constraint(expr= (m.x75 - m.x77)**2 + (m.x154 - m.x156)**2 + (m.x233
    - m.x235)**2 >= 0.46785600000000005)
m.e3074 = Constraint(expr= (m.x75 - m.x78)**2 + (m.x154 - m.x157)**2 + (m.x233
    - m.x236)**2 >= 0.46785600000000005)
m.e3075 = Constraint(expr= (m.x75 - m.x79)**2 + (m.x154 - m.x158)**2 + (m.x233
    - m.x237)**2 >= 0.46785600000000005)
m.e3076 = Constraint(expr= (m.x76 - m.x77)**2 + (m.x155 - m.x156)**2 + (m.x234
    - m.x235)**2 >= 0.46785600000000005)
m.e3077 = Constraint(expr= (m.x76 - m.x78)**2 + (m.x155 - m.x157)**2 + (m.x234
    - m.x236)**2 >= 0.46785600000000005)
m.e3078 = Constraint(expr= (m.x76 - m.x79)**2 + (m.x155 - m.x158)**2 + (m.x234
    - m.x237)**2 >= 0.46785600000000005)
m.e3079 = Constraint(expr= (m.x77 - m.x78)**2 + (m.x156 - m.x157)**2 + (m.x235
    - m.x236)**2 >= 0.46785600000000005)
m.e3080 = Constraint(expr= (m.x77 - m.x79)**2 + (m.x156 - m.x158)**2 + (m.x235
    - m.x237)**2 >= 0.46785600000000005)
m.e3081 = Constraint(expr= (m.x78 - m.x79)**2 + (m.x157 - m.x158)**2 + (m.x236
    - m.x237)**2 >= 0.46785600000000005)