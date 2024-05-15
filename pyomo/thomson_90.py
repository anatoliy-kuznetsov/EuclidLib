# NLP written by GAMS Convert at 05/15/24 11:47:04
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#        90       90        0        0        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#       270      270        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       270        0      270
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
m.x211 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x212 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x213 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x214 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x215 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x216 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x217 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x218 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x219 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x220 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x221 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x222 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x223 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x224 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x225 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x226 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x227 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x228 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x229 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x230 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x231 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x232 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x233 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x234 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x235 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x236 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x237 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x238 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x239 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x240 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x241 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x242 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x243 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x244 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x245 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x246 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x247 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x248 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x249 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x250 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x251 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x252 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x253 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x254 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x255 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x256 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x257 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x258 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x259 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x260 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x261 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x262 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x263 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x264 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x265 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x266 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x267 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x268 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x269 = Var(within=Reals, bounds=(-1,1), initialize=0)
m.x270 = Var(within=Reals, bounds=(-1,1), initialize=0)

m.obj = Objective(sense=minimize, expr= 1 / sqrt((m.x1 - m.x2)**2 + (m.x91 -
    m.x92)**2 + (m.x181 - m.x182)**2) + 1 / sqrt((m.x1 - m.x3)**2 + (m.x91 -
    m.x93)**2 + (m.x181 - m.x183)**2) + 1 / sqrt((m.x1 - m.x4)**2 + (m.x91 -
    m.x94)**2 + (m.x181 - m.x184)**2) + 1 / sqrt((m.x1 - m.x5)**2 + (m.x91 -
    m.x95)**2 + (m.x181 - m.x185)**2) + 1 / sqrt((m.x1 - m.x6)**2 + (m.x91 -
    m.x96)**2 + (m.x181 - m.x186)**2) + 1 / sqrt((m.x1 - m.x7)**2 + (m.x91 -
    m.x97)**2 + (m.x181 - m.x187)**2) + 1 / sqrt((m.x1 - m.x8)**2 + (m.x91 -
    m.x98)**2 + (m.x181 - m.x188)**2) + 1 / sqrt((m.x1 - m.x9)**2 + (m.x91 -
    m.x99)**2 + (m.x181 - m.x189)**2) + 1 / sqrt((m.x1 - m.x10)**2 + (m.x91 -
    m.x100)**2 + (m.x181 - m.x190)**2) + 1 / sqrt((m.x1 - m.x11)**2 + (m.x91 -
    m.x101)**2 + (m.x181 - m.x191)**2) + 1 / sqrt((m.x1 - m.x12)**2 + (m.x91 -
    m.x102)**2 + (m.x181 - m.x192)**2) + 1 / sqrt((m.x1 - m.x13)**2 + (m.x91 -
    m.x103)**2 + (m.x181 - m.x193)**2) + 1 / sqrt((m.x1 - m.x14)**2 + (m.x91 -
    m.x104)**2 + (m.x181 - m.x194)**2) + 1 / sqrt((m.x1 - m.x15)**2 + (m.x91 -
    m.x105)**2 + (m.x181 - m.x195)**2) + 1 / sqrt((m.x1 - m.x16)**2 + (m.x91 -
    m.x106)**2 + (m.x181 - m.x196)**2) + 1 / sqrt((m.x1 - m.x17)**2 + (m.x91 -
    m.x107)**2 + (m.x181 - m.x197)**2) + 1 / sqrt((m.x1 - m.x18)**2 + (m.x91 -
    m.x108)**2 + (m.x181 - m.x198)**2) + 1 / sqrt((m.x1 - m.x19)**2 + (m.x91 -
    m.x109)**2 + (m.x181 - m.x199)**2) + 1 / sqrt((m.x1 - m.x20)**2 + (m.x91 -
    m.x110)**2 + (m.x181 - m.x200)**2) + 1 / sqrt((m.x1 - m.x21)**2 + (m.x91 -
    m.x111)**2 + (m.x181 - m.x201)**2) + 1 / sqrt((m.x1 - m.x22)**2 + (m.x91 -
    m.x112)**2 + (m.x181 - m.x202)**2) + 1 / sqrt((m.x1 - m.x23)**2 + (m.x91 -
    m.x113)**2 + (m.x181 - m.x203)**2) + 1 / sqrt((m.x1 - m.x24)**2 + (m.x91 -
    m.x114)**2 + (m.x181 - m.x204)**2) + 1 / sqrt((m.x1 - m.x25)**2 + (m.x91 -
    m.x115)**2 + (m.x181 - m.x205)**2) + 1 / sqrt((m.x1 - m.x26)**2 + (m.x91 -
    m.x116)**2 + (m.x181 - m.x206)**2) + 1 / sqrt((m.x1 - m.x27)**2 + (m.x91 -
    m.x117)**2 + (m.x181 - m.x207)**2) + 1 / sqrt((m.x1 - m.x28)**2 + (m.x91 -
    m.x118)**2 + (m.x181 - m.x208)**2) + 1 / sqrt((m.x1 - m.x29)**2 + (m.x91 -
    m.x119)**2 + (m.x181 - m.x209)**2) + 1 / sqrt((m.x1 - m.x30)**2 + (m.x91 -
    m.x120)**2 + (m.x181 - m.x210)**2) + 1 / sqrt((m.x1 - m.x31)**2 + (m.x91 -
    m.x121)**2 + (m.x181 - m.x211)**2) + 1 / sqrt((m.x1 - m.x32)**2 + (m.x91 -
    m.x122)**2 + (m.x181 - m.x212)**2) + 1 / sqrt((m.x1 - m.x33)**2 + (m.x91 -
    m.x123)**2 + (m.x181 - m.x213)**2) + 1 / sqrt((m.x1 - m.x34)**2 + (m.x91 -
    m.x124)**2 + (m.x181 - m.x214)**2) + 1 / sqrt((m.x1 - m.x35)**2 + (m.x91 -
    m.x125)**2 + (m.x181 - m.x215)**2) + 1 / sqrt((m.x1 - m.x36)**2 + (m.x91 -
    m.x126)**2 + (m.x181 - m.x216)**2) + 1 / sqrt((m.x1 - m.x37)**2 + (m.x91 -
    m.x127)**2 + (m.x181 - m.x217)**2) + 1 / sqrt((m.x1 - m.x38)**2 + (m.x91 -
    m.x128)**2 + (m.x181 - m.x218)**2) + 1 / sqrt((m.x1 - m.x39)**2 + (m.x91 -
    m.x129)**2 + (m.x181 - m.x219)**2) + 1 / sqrt((m.x1 - m.x40)**2 + (m.x91 -
    m.x130)**2 + (m.x181 - m.x220)**2) + 1 / sqrt((m.x1 - m.x41)**2 + (m.x91 -
    m.x131)**2 + (m.x181 - m.x221)**2) + 1 / sqrt((m.x1 - m.x42)**2 + (m.x91 -
    m.x132)**2 + (m.x181 - m.x222)**2) + 1 / sqrt((m.x1 - m.x43)**2 + (m.x91 -
    m.x133)**2 + (m.x181 - m.x223)**2) + 1 / sqrt((m.x1 - m.x44)**2 + (m.x91 -
    m.x134)**2 + (m.x181 - m.x224)**2) + 1 / sqrt((m.x1 - m.x45)**2 + (m.x91 -
    m.x135)**2 + (m.x181 - m.x225)**2) + 1 / sqrt((m.x1 - m.x46)**2 + (m.x91 -
    m.x136)**2 + (m.x181 - m.x226)**2) + 1 / sqrt((m.x1 - m.x47)**2 + (m.x91 -
    m.x137)**2 + (m.x181 - m.x227)**2) + 1 / sqrt((m.x1 - m.x48)**2 + (m.x91 -
    m.x138)**2 + (m.x181 - m.x228)**2) + 1 / sqrt((m.x1 - m.x49)**2 + (m.x91 -
    m.x139)**2 + (m.x181 - m.x229)**2) + 1 / sqrt((m.x1 - m.x50)**2 + (m.x91 -
    m.x140)**2 + (m.x181 - m.x230)**2) + 1 / sqrt((m.x1 - m.x51)**2 + (m.x91 -
    m.x141)**2 + (m.x181 - m.x231)**2) + 1 / sqrt((m.x1 - m.x52)**2 + (m.x91 -
    m.x142)**2 + (m.x181 - m.x232)**2) + 1 / sqrt((m.x1 - m.x53)**2 + (m.x91 -
    m.x143)**2 + (m.x181 - m.x233)**2) + 1 / sqrt((m.x1 - m.x54)**2 + (m.x91 -
    m.x144)**2 + (m.x181 - m.x234)**2) + 1 / sqrt((m.x1 - m.x55)**2 + (m.x91 -
    m.x145)**2 + (m.x181 - m.x235)**2) + 1 / sqrt((m.x1 - m.x56)**2 + (m.x91 -
    m.x146)**2 + (m.x181 - m.x236)**2) + 1 / sqrt((m.x1 - m.x57)**2 + (m.x91 -
    m.x147)**2 + (m.x181 - m.x237)**2) + 1 / sqrt((m.x1 - m.x58)**2 + (m.x91 -
    m.x148)**2 + (m.x181 - m.x238)**2) + 1 / sqrt((m.x1 - m.x59)**2 + (m.x91 -
    m.x149)**2 + (m.x181 - m.x239)**2) + 1 / sqrt((m.x1 - m.x60)**2 + (m.x91 -
    m.x150)**2 + (m.x181 - m.x240)**2) + 1 / sqrt((m.x1 - m.x61)**2 + (m.x91 -
    m.x151)**2 + (m.x181 - m.x241)**2) + 1 / sqrt((m.x1 - m.x62)**2 + (m.x91 -
    m.x152)**2 + (m.x181 - m.x242)**2) + 1 / sqrt((m.x1 - m.x63)**2 + (m.x91 -
    m.x153)**2 + (m.x181 - m.x243)**2) + 1 / sqrt((m.x1 - m.x64)**2 + (m.x91 -
    m.x154)**2 + (m.x181 - m.x244)**2) + 1 / sqrt((m.x1 - m.x65)**2 + (m.x91 -
    m.x155)**2 + (m.x181 - m.x245)**2) + 1 / sqrt((m.x1 - m.x66)**2 + (m.x91 -
    m.x156)**2 + (m.x181 - m.x246)**2) + 1 / sqrt((m.x1 - m.x67)**2 + (m.x91 -
    m.x157)**2 + (m.x181 - m.x247)**2) + 1 / sqrt((m.x1 - m.x68)**2 + (m.x91 -
    m.x158)**2 + (m.x181 - m.x248)**2) + 1 / sqrt((m.x1 - m.x69)**2 + (m.x91 -
    m.x159)**2 + (m.x181 - m.x249)**2) + 1 / sqrt((m.x1 - m.x70)**2 + (m.x91 -
    m.x160)**2 + (m.x181 - m.x250)**2) + 1 / sqrt((m.x1 - m.x71)**2 + (m.x91 -
    m.x161)**2 + (m.x181 - m.x251)**2) + 1 / sqrt((m.x1 - m.x72)**2 + (m.x91 -
    m.x162)**2 + (m.x181 - m.x252)**2) + 1 / sqrt((m.x1 - m.x73)**2 + (m.x91 -
    m.x163)**2 + (m.x181 - m.x253)**2) + 1 / sqrt((m.x1 - m.x74)**2 + (m.x91 -
    m.x164)**2 + (m.x181 - m.x254)**2) + 1 / sqrt((m.x1 - m.x75)**2 + (m.x91 -
    m.x165)**2 + (m.x181 - m.x255)**2) + 1 / sqrt((m.x1 - m.x76)**2 + (m.x91 -
    m.x166)**2 + (m.x181 - m.x256)**2) + 1 / sqrt((m.x1 - m.x77)**2 + (m.x91 -
    m.x167)**2 + (m.x181 - m.x257)**2) + 1 / sqrt((m.x1 - m.x78)**2 + (m.x91 -
    m.x168)**2 + (m.x181 - m.x258)**2) + 1 / sqrt((m.x1 - m.x79)**2 + (m.x91 -
    m.x169)**2 + (m.x181 - m.x259)**2) + 1 / sqrt((m.x1 - m.x80)**2 + (m.x91 -
    m.x170)**2 + (m.x181 - m.x260)**2) + 1 / sqrt((m.x1 - m.x81)**2 + (m.x91 -
    m.x171)**2 + (m.x181 - m.x261)**2) + 1 / sqrt((m.x1 - m.x82)**2 + (m.x91 -
    m.x172)**2 + (m.x181 - m.x262)**2) + 1 / sqrt((m.x1 - m.x83)**2 + (m.x91 -
    m.x173)**2 + (m.x181 - m.x263)**2) + 1 / sqrt((m.x1 - m.x84)**2 + (m.x91 -
    m.x174)**2 + (m.x181 - m.x264)**2) + 1 / sqrt((m.x1 - m.x85)**2 + (m.x91 -
    m.x175)**2 + (m.x181 - m.x265)**2) + 1 / sqrt((m.x1 - m.x86)**2 + (m.x91 -
    m.x176)**2 + (m.x181 - m.x266)**2) + 1 / sqrt((m.x1 - m.x87)**2 + (m.x91 -
    m.x177)**2 + (m.x181 - m.x267)**2) + 1 / sqrt((m.x1 - m.x88)**2 + (m.x91 -
    m.x178)**2 + (m.x181 - m.x268)**2) + 1 / sqrt((m.x1 - m.x89)**2 + (m.x91 -
    m.x179)**2 + (m.x181 - m.x269)**2) + 1 / sqrt((m.x1 - m.x90)**2 + (m.x91 -
    m.x180)**2 + (m.x181 - m.x270)**2) + 1 / sqrt((m.x2 - m.x3)**2 + (m.x92 -
    m.x93)**2 + (m.x182 - m.x183)**2) + 1 / sqrt((m.x2 - m.x4)**2 + (m.x92 -
    m.x94)**2 + (m.x182 - m.x184)**2) + 1 / sqrt((m.x2 - m.x5)**2 + (m.x92 -
    m.x95)**2 + (m.x182 - m.x185)**2) + 1 / sqrt((m.x2 - m.x6)**2 + (m.x92 -
    m.x96)**2 + (m.x182 - m.x186)**2) + 1 / sqrt((m.x2 - m.x7)**2 + (m.x92 -
    m.x97)**2 + (m.x182 - m.x187)**2) + 1 / sqrt((m.x2 - m.x8)**2 + (m.x92 -
    m.x98)**2 + (m.x182 - m.x188)**2) + 1 / sqrt((m.x2 - m.x9)**2 + (m.x92 -
    m.x99)**2 + (m.x182 - m.x189)**2) + 1 / sqrt((m.x2 - m.x10)**2 + (m.x92 -
    m.x100)**2 + (m.x182 - m.x190)**2) + 1 / sqrt((m.x2 - m.x11)**2 + (m.x92 -
    m.x101)**2 + (m.x182 - m.x191)**2) + 1 / sqrt((m.x2 - m.x12)**2 + (m.x92 -
    m.x102)**2 + (m.x182 - m.x192)**2) + 1 / sqrt((m.x2 - m.x13)**2 + (m.x92 -
    m.x103)**2 + (m.x182 - m.x193)**2) + 1 / sqrt((m.x2 - m.x14)**2 + (m.x92 -
    m.x104)**2 + (m.x182 - m.x194)**2) + 1 / sqrt((m.x2 - m.x15)**2 + (m.x92 -
    m.x105)**2 + (m.x182 - m.x195)**2) + 1 / sqrt((m.x2 - m.x16)**2 + (m.x92 -
    m.x106)**2 + (m.x182 - m.x196)**2) + 1 / sqrt((m.x2 - m.x17)**2 + (m.x92 -
    m.x107)**2 + (m.x182 - m.x197)**2) + 1 / sqrt((m.x2 - m.x18)**2 + (m.x92 -
    m.x108)**2 + (m.x182 - m.x198)**2) + 1 / sqrt((m.x2 - m.x19)**2 + (m.x92 -
    m.x109)**2 + (m.x182 - m.x199)**2) + 1 / sqrt((m.x2 - m.x20)**2 + (m.x92 -
    m.x110)**2 + (m.x182 - m.x200)**2) + 1 / sqrt((m.x2 - m.x21)**2 + (m.x92 -
    m.x111)**2 + (m.x182 - m.x201)**2) + 1 / sqrt((m.x2 - m.x22)**2 + (m.x92 -
    m.x112)**2 + (m.x182 - m.x202)**2) + 1 / sqrt((m.x2 - m.x23)**2 + (m.x92 -
    m.x113)**2 + (m.x182 - m.x203)**2) + 1 / sqrt((m.x2 - m.x24)**2 + (m.x92 -
    m.x114)**2 + (m.x182 - m.x204)**2) + 1 / sqrt((m.x2 - m.x25)**2 + (m.x92 -
    m.x115)**2 + (m.x182 - m.x205)**2) + 1 / sqrt((m.x2 - m.x26)**2 + (m.x92 -
    m.x116)**2 + (m.x182 - m.x206)**2) + 1 / sqrt((m.x2 - m.x27)**2 + (m.x92 -
    m.x117)**2 + (m.x182 - m.x207)**2) + 1 / sqrt((m.x2 - m.x28)**2 + (m.x92 -
    m.x118)**2 + (m.x182 - m.x208)**2) + 1 / sqrt((m.x2 - m.x29)**2 + (m.x92 -
    m.x119)**2 + (m.x182 - m.x209)**2) + 1 / sqrt((m.x2 - m.x30)**2 + (m.x92 -
    m.x120)**2 + (m.x182 - m.x210)**2) + 1 / sqrt((m.x2 - m.x31)**2 + (m.x92 -
    m.x121)**2 + (m.x182 - m.x211)**2) + 1 / sqrt((m.x2 - m.x32)**2 + (m.x92 -
    m.x122)**2 + (m.x182 - m.x212)**2) + 1 / sqrt((m.x2 - m.x33)**2 + (m.x92 -
    m.x123)**2 + (m.x182 - m.x213)**2) + 1 / sqrt((m.x2 - m.x34)**2 + (m.x92 -
    m.x124)**2 + (m.x182 - m.x214)**2) + 1 / sqrt((m.x2 - m.x35)**2 + (m.x92 -
    m.x125)**2 + (m.x182 - m.x215)**2) + 1 / sqrt((m.x2 - m.x36)**2 + (m.x92 -
    m.x126)**2 + (m.x182 - m.x216)**2) + 1 / sqrt((m.x2 - m.x37)**2 + (m.x92 -
    m.x127)**2 + (m.x182 - m.x217)**2) + 1 / sqrt((m.x2 - m.x38)**2 + (m.x92 -
    m.x128)**2 + (m.x182 - m.x218)**2) + 1 / sqrt((m.x2 - m.x39)**2 + (m.x92 -
    m.x129)**2 + (m.x182 - m.x219)**2) + 1 / sqrt((m.x2 - m.x40)**2 + (m.x92 -
    m.x130)**2 + (m.x182 - m.x220)**2) + 1 / sqrt((m.x2 - m.x41)**2 + (m.x92 -
    m.x131)**2 + (m.x182 - m.x221)**2) + 1 / sqrt((m.x2 - m.x42)**2 + (m.x92 -
    m.x132)**2 + (m.x182 - m.x222)**2) + 1 / sqrt((m.x2 - m.x43)**2 + (m.x92 -
    m.x133)**2 + (m.x182 - m.x223)**2) + 1 / sqrt((m.x2 - m.x44)**2 + (m.x92 -
    m.x134)**2 + (m.x182 - m.x224)**2) + 1 / sqrt((m.x2 - m.x45)**2 + (m.x92 -
    m.x135)**2 + (m.x182 - m.x225)**2) + 1 / sqrt((m.x2 - m.x46)**2 + (m.x92 -
    m.x136)**2 + (m.x182 - m.x226)**2) + 1 / sqrt((m.x2 - m.x47)**2 + (m.x92 -
    m.x137)**2 + (m.x182 - m.x227)**2) + 1 / sqrt((m.x2 - m.x48)**2 + (m.x92 -
    m.x138)**2 + (m.x182 - m.x228)**2) + 1 / sqrt((m.x2 - m.x49)**2 + (m.x92 -
    m.x139)**2 + (m.x182 - m.x229)**2) + 1 / sqrt((m.x2 - m.x50)**2 + (m.x92 -
    m.x140)**2 + (m.x182 - m.x230)**2) + 1 / sqrt((m.x2 - m.x51)**2 + (m.x92 -
    m.x141)**2 + (m.x182 - m.x231)**2) + 1 / sqrt((m.x2 - m.x52)**2 + (m.x92 -
    m.x142)**2 + (m.x182 - m.x232)**2) + 1 / sqrt((m.x2 - m.x53)**2 + (m.x92 -
    m.x143)**2 + (m.x182 - m.x233)**2) + 1 / sqrt((m.x2 - m.x54)**2 + (m.x92 -
    m.x144)**2 + (m.x182 - m.x234)**2) + 1 / sqrt((m.x2 - m.x55)**2 + (m.x92 -
    m.x145)**2 + (m.x182 - m.x235)**2) + 1 / sqrt((m.x2 - m.x56)**2 + (m.x92 -
    m.x146)**2 + (m.x182 - m.x236)**2) + 1 / sqrt((m.x2 - m.x57)**2 + (m.x92 -
    m.x147)**2 + (m.x182 - m.x237)**2) + 1 / sqrt((m.x2 - m.x58)**2 + (m.x92 -
    m.x148)**2 + (m.x182 - m.x238)**2) + 1 / sqrt((m.x2 - m.x59)**2 + (m.x92 -
    m.x149)**2 + (m.x182 - m.x239)**2) + 1 / sqrt((m.x2 - m.x60)**2 + (m.x92 -
    m.x150)**2 + (m.x182 - m.x240)**2) + 1 / sqrt((m.x2 - m.x61)**2 + (m.x92 -
    m.x151)**2 + (m.x182 - m.x241)**2) + 1 / sqrt((m.x2 - m.x62)**2 + (m.x92 -
    m.x152)**2 + (m.x182 - m.x242)**2) + 1 / sqrt((m.x2 - m.x63)**2 + (m.x92 -
    m.x153)**2 + (m.x182 - m.x243)**2) + 1 / sqrt((m.x2 - m.x64)**2 + (m.x92 -
    m.x154)**2 + (m.x182 - m.x244)**2) + 1 / sqrt((m.x2 - m.x65)**2 + (m.x92 -
    m.x155)**2 + (m.x182 - m.x245)**2) + 1 / sqrt((m.x2 - m.x66)**2 + (m.x92 -
    m.x156)**2 + (m.x182 - m.x246)**2) + 1 / sqrt((m.x2 - m.x67)**2 + (m.x92 -
    m.x157)**2 + (m.x182 - m.x247)**2) + 1 / sqrt((m.x2 - m.x68)**2 + (m.x92 -
    m.x158)**2 + (m.x182 - m.x248)**2) + 1 / sqrt((m.x2 - m.x69)**2 + (m.x92 -
    m.x159)**2 + (m.x182 - m.x249)**2) + 1 / sqrt((m.x2 - m.x70)**2 + (m.x92 -
    m.x160)**2 + (m.x182 - m.x250)**2) + 1 / sqrt((m.x2 - m.x71)**2 + (m.x92 -
    m.x161)**2 + (m.x182 - m.x251)**2) + 1 / sqrt((m.x2 - m.x72)**2 + (m.x92 -
    m.x162)**2 + (m.x182 - m.x252)**2) + 1 / sqrt((m.x2 - m.x73)**2 + (m.x92 -
    m.x163)**2 + (m.x182 - m.x253)**2) + 1 / sqrt((m.x2 - m.x74)**2 + (m.x92 -
    m.x164)**2 + (m.x182 - m.x254)**2) + 1 / sqrt((m.x2 - m.x75)**2 + (m.x92 -
    m.x165)**2 + (m.x182 - m.x255)**2) + 1 / sqrt((m.x2 - m.x76)**2 + (m.x92 -
    m.x166)**2 + (m.x182 - m.x256)**2) + 1 / sqrt((m.x2 - m.x77)**2 + (m.x92 -
    m.x167)**2 + (m.x182 - m.x257)**2) + 1 / sqrt((m.x2 - m.x78)**2 + (m.x92 -
    m.x168)**2 + (m.x182 - m.x258)**2) + 1 / sqrt((m.x2 - m.x79)**2 + (m.x92 -
    m.x169)**2 + (m.x182 - m.x259)**2) + 1 / sqrt((m.x2 - m.x80)**2 + (m.x92 -
    m.x170)**2 + (m.x182 - m.x260)**2) + 1 / sqrt((m.x2 - m.x81)**2 + (m.x92 -
    m.x171)**2 + (m.x182 - m.x261)**2) + 1 / sqrt((m.x2 - m.x82)**2 + (m.x92 -
    m.x172)**2 + (m.x182 - m.x262)**2) + 1 / sqrt((m.x2 - m.x83)**2 + (m.x92 -
    m.x173)**2 + (m.x182 - m.x263)**2) + 1 / sqrt((m.x2 - m.x84)**2 + (m.x92 -
    m.x174)**2 + (m.x182 - m.x264)**2) + 1 / sqrt((m.x2 - m.x85)**2 + (m.x92 -
    m.x175)**2 + (m.x182 - m.x265)**2) + 1 / sqrt((m.x2 - m.x86)**2 + (m.x92 -
    m.x176)**2 + (m.x182 - m.x266)**2) + 1 / sqrt((m.x2 - m.x87)**2 + (m.x92 -
    m.x177)**2 + (m.x182 - m.x267)**2) + 1 / sqrt((m.x2 - m.x88)**2 + (m.x92 -
    m.x178)**2 + (m.x182 - m.x268)**2) + 1 / sqrt((m.x2 - m.x89)**2 + (m.x92 -
    m.x179)**2 + (m.x182 - m.x269)**2) + 1 / sqrt((m.x2 - m.x90)**2 + (m.x92 -
    m.x180)**2 + (m.x182 - m.x270)**2) + 1 / sqrt((m.x3 - m.x4)**2 + (m.x93 -
    m.x94)**2 + (m.x183 - m.x184)**2) + 1 / sqrt((m.x3 - m.x5)**2 + (m.x93 -
    m.x95)**2 + (m.x183 - m.x185)**2) + 1 / sqrt((m.x3 - m.x6)**2 + (m.x93 -
    m.x96)**2 + (m.x183 - m.x186)**2) + 1 / sqrt((m.x3 - m.x7)**2 + (m.x93 -
    m.x97)**2 + (m.x183 - m.x187)**2) + 1 / sqrt((m.x3 - m.x8)**2 + (m.x93 -
    m.x98)**2 + (m.x183 - m.x188)**2) + 1 / sqrt((m.x3 - m.x9)**2 + (m.x93 -
    m.x99)**2 + (m.x183 - m.x189)**2) + 1 / sqrt((m.x3 - m.x10)**2 + (m.x93 -
    m.x100)**2 + (m.x183 - m.x190)**2) + 1 / sqrt((m.x3 - m.x11)**2 + (m.x93 -
    m.x101)**2 + (m.x183 - m.x191)**2) + 1 / sqrt((m.x3 - m.x12)**2 + (m.x93 -
    m.x102)**2 + (m.x183 - m.x192)**2) + 1 / sqrt((m.x3 - m.x13)**2 + (m.x93 -
    m.x103)**2 + (m.x183 - m.x193)**2) + 1 / sqrt((m.x3 - m.x14)**2 + (m.x93 -
    m.x104)**2 + (m.x183 - m.x194)**2) + 1 / sqrt((m.x3 - m.x15)**2 + (m.x93 -
    m.x105)**2 + (m.x183 - m.x195)**2) + 1 / sqrt((m.x3 - m.x16)**2 + (m.x93 -
    m.x106)**2 + (m.x183 - m.x196)**2) + 1 / sqrt((m.x3 - m.x17)**2 + (m.x93 -
    m.x107)**2 + (m.x183 - m.x197)**2) + 1 / sqrt((m.x3 - m.x18)**2 + (m.x93 -
    m.x108)**2 + (m.x183 - m.x198)**2) + 1 / sqrt((m.x3 - m.x19)**2 + (m.x93 -
    m.x109)**2 + (m.x183 - m.x199)**2) + 1 / sqrt((m.x3 - m.x20)**2 + (m.x93 -
    m.x110)**2 + (m.x183 - m.x200)**2) + 1 / sqrt((m.x3 - m.x21)**2 + (m.x93 -
    m.x111)**2 + (m.x183 - m.x201)**2) + 1 / sqrt((m.x3 - m.x22)**2 + (m.x93 -
    m.x112)**2 + (m.x183 - m.x202)**2) + 1 / sqrt((m.x3 - m.x23)**2 + (m.x93 -
    m.x113)**2 + (m.x183 - m.x203)**2) + 1 / sqrt((m.x3 - m.x24)**2 + (m.x93 -
    m.x114)**2 + (m.x183 - m.x204)**2) + 1 / sqrt((m.x3 - m.x25)**2 + (m.x93 -
    m.x115)**2 + (m.x183 - m.x205)**2) + 1 / sqrt((m.x3 - m.x26)**2 + (m.x93 -
    m.x116)**2 + (m.x183 - m.x206)**2) + 1 / sqrt((m.x3 - m.x27)**2 + (m.x93 -
    m.x117)**2 + (m.x183 - m.x207)**2) + 1 / sqrt((m.x3 - m.x28)**2 + (m.x93 -
    m.x118)**2 + (m.x183 - m.x208)**2) + 1 / sqrt((m.x3 - m.x29)**2 + (m.x93 -
    m.x119)**2 + (m.x183 - m.x209)**2) + 1 / sqrt((m.x3 - m.x30)**2 + (m.x93 -
    m.x120)**2 + (m.x183 - m.x210)**2) + 1 / sqrt((m.x3 - m.x31)**2 + (m.x93 -
    m.x121)**2 + (m.x183 - m.x211)**2) + 1 / sqrt((m.x3 - m.x32)**2 + (m.x93 -
    m.x122)**2 + (m.x183 - m.x212)**2) + 1 / sqrt((m.x3 - m.x33)**2 + (m.x93 -
    m.x123)**2 + (m.x183 - m.x213)**2) + 1 / sqrt((m.x3 - m.x34)**2 + (m.x93 -
    m.x124)**2 + (m.x183 - m.x214)**2) + 1 / sqrt((m.x3 - m.x35)**2 + (m.x93 -
    m.x125)**2 + (m.x183 - m.x215)**2) + 1 / sqrt((m.x3 - m.x36)**2 + (m.x93 -
    m.x126)**2 + (m.x183 - m.x216)**2) + 1 / sqrt((m.x3 - m.x37)**2 + (m.x93 -
    m.x127)**2 + (m.x183 - m.x217)**2) + 1 / sqrt((m.x3 - m.x38)**2 + (m.x93 -
    m.x128)**2 + (m.x183 - m.x218)**2) + 1 / sqrt((m.x3 - m.x39)**2 + (m.x93 -
    m.x129)**2 + (m.x183 - m.x219)**2) + 1 / sqrt((m.x3 - m.x40)**2 + (m.x93 -
    m.x130)**2 + (m.x183 - m.x220)**2) + 1 / sqrt((m.x3 - m.x41)**2 + (m.x93 -
    m.x131)**2 + (m.x183 - m.x221)**2) + 1 / sqrt((m.x3 - m.x42)**2 + (m.x93 -
    m.x132)**2 + (m.x183 - m.x222)**2) + 1 / sqrt((m.x3 - m.x43)**2 + (m.x93 -
    m.x133)**2 + (m.x183 - m.x223)**2) + 1 / sqrt((m.x3 - m.x44)**2 + (m.x93 -
    m.x134)**2 + (m.x183 - m.x224)**2) + 1 / sqrt((m.x3 - m.x45)**2 + (m.x93 -
    m.x135)**2 + (m.x183 - m.x225)**2) + 1 / sqrt((m.x3 - m.x46)**2 + (m.x93 -
    m.x136)**2 + (m.x183 - m.x226)**2) + 1 / sqrt((m.x3 - m.x47)**2 + (m.x93 -
    m.x137)**2 + (m.x183 - m.x227)**2) + 1 / sqrt((m.x3 - m.x48)**2 + (m.x93 -
    m.x138)**2 + (m.x183 - m.x228)**2) + 1 / sqrt((m.x3 - m.x49)**2 + (m.x93 -
    m.x139)**2 + (m.x183 - m.x229)**2) + 1 / sqrt((m.x3 - m.x50)**2 + (m.x93 -
    m.x140)**2 + (m.x183 - m.x230)**2) + 1 / sqrt((m.x3 - m.x51)**2 + (m.x93 -
    m.x141)**2 + (m.x183 - m.x231)**2) + 1 / sqrt((m.x3 - m.x52)**2 + (m.x93 -
    m.x142)**2 + (m.x183 - m.x232)**2) + 1 / sqrt((m.x3 - m.x53)**2 + (m.x93 -
    m.x143)**2 + (m.x183 - m.x233)**2) + 1 / sqrt((m.x3 - m.x54)**2 + (m.x93 -
    m.x144)**2 + (m.x183 - m.x234)**2) + 1 / sqrt((m.x3 - m.x55)**2 + (m.x93 -
    m.x145)**2 + (m.x183 - m.x235)**2) + 1 / sqrt((m.x3 - m.x56)**2 + (m.x93 -
    m.x146)**2 + (m.x183 - m.x236)**2) + 1 / sqrt((m.x3 - m.x57)**2 + (m.x93 -
    m.x147)**2 + (m.x183 - m.x237)**2) + 1 / sqrt((m.x3 - m.x58)**2 + (m.x93 -
    m.x148)**2 + (m.x183 - m.x238)**2) + 1 / sqrt((m.x3 - m.x59)**2 + (m.x93 -
    m.x149)**2 + (m.x183 - m.x239)**2) + 1 / sqrt((m.x3 - m.x60)**2 + (m.x93 -
    m.x150)**2 + (m.x183 - m.x240)**2) + 1 / sqrt((m.x3 - m.x61)**2 + (m.x93 -
    m.x151)**2 + (m.x183 - m.x241)**2) + 1 / sqrt((m.x3 - m.x62)**2 + (m.x93 -
    m.x152)**2 + (m.x183 - m.x242)**2) + 1 / sqrt((m.x3 - m.x63)**2 + (m.x93 -
    m.x153)**2 + (m.x183 - m.x243)**2) + 1 / sqrt((m.x3 - m.x64)**2 + (m.x93 -
    m.x154)**2 + (m.x183 - m.x244)**2) + 1 / sqrt((m.x3 - m.x65)**2 + (m.x93 -
    m.x155)**2 + (m.x183 - m.x245)**2) + 1 / sqrt((m.x3 - m.x66)**2 + (m.x93 -
    m.x156)**2 + (m.x183 - m.x246)**2) + 1 / sqrt((m.x3 - m.x67)**2 + (m.x93 -
    m.x157)**2 + (m.x183 - m.x247)**2) + 1 / sqrt((m.x3 - m.x68)**2 + (m.x93 -
    m.x158)**2 + (m.x183 - m.x248)**2) + 1 / sqrt((m.x3 - m.x69)**2 + (m.x93 -
    m.x159)**2 + (m.x183 - m.x249)**2) + 1 / sqrt((m.x3 - m.x70)**2 + (m.x93 -
    m.x160)**2 + (m.x183 - m.x250)**2) + 1 / sqrt((m.x3 - m.x71)**2 + (m.x93 -
    m.x161)**2 + (m.x183 - m.x251)**2) + 1 / sqrt((m.x3 - m.x72)**2 + (m.x93 -
    m.x162)**2 + (m.x183 - m.x252)**2) + 1 / sqrt((m.x3 - m.x73)**2 + (m.x93 -
    m.x163)**2 + (m.x183 - m.x253)**2) + 1 / sqrt((m.x3 - m.x74)**2 + (m.x93 -
    m.x164)**2 + (m.x183 - m.x254)**2) + 1 / sqrt((m.x3 - m.x75)**2 + (m.x93 -
    m.x165)**2 + (m.x183 - m.x255)**2) + 1 / sqrt((m.x3 - m.x76)**2 + (m.x93 -
    m.x166)**2 + (m.x183 - m.x256)**2) + 1 / sqrt((m.x3 - m.x77)**2 + (m.x93 -
    m.x167)**2 + (m.x183 - m.x257)**2) + 1 / sqrt((m.x3 - m.x78)**2 + (m.x93 -
    m.x168)**2 + (m.x183 - m.x258)**2) + 1 / sqrt((m.x3 - m.x79)**2 + (m.x93 -
    m.x169)**2 + (m.x183 - m.x259)**2) + 1 / sqrt((m.x3 - m.x80)**2 + (m.x93 -
    m.x170)**2 + (m.x183 - m.x260)**2) + 1 / sqrt((m.x3 - m.x81)**2 + (m.x93 -
    m.x171)**2 + (m.x183 - m.x261)**2) + 1 / sqrt((m.x3 - m.x82)**2 + (m.x93 -
    m.x172)**2 + (m.x183 - m.x262)**2) + 1 / sqrt((m.x3 - m.x83)**2 + (m.x93 -
    m.x173)**2 + (m.x183 - m.x263)**2) + 1 / sqrt((m.x3 - m.x84)**2 + (m.x93 -
    m.x174)**2 + (m.x183 - m.x264)**2) + 1 / sqrt((m.x3 - m.x85)**2 + (m.x93 -
    m.x175)**2 + (m.x183 - m.x265)**2) + 1 / sqrt((m.x3 - m.x86)**2 + (m.x93 -
    m.x176)**2 + (m.x183 - m.x266)**2) + 1 / sqrt((m.x3 - m.x87)**2 + (m.x93 -
    m.x177)**2 + (m.x183 - m.x267)**2) + 1 / sqrt((m.x3 - m.x88)**2 + (m.x93 -
    m.x178)**2 + (m.x183 - m.x268)**2) + 1 / sqrt((m.x3 - m.x89)**2 + (m.x93 -
    m.x179)**2 + (m.x183 - m.x269)**2) + 1 / sqrt((m.x3 - m.x90)**2 + (m.x93 -
    m.x180)**2 + (m.x183 - m.x270)**2) + 1 / sqrt((m.x4 - m.x5)**2 + (m.x94 -
    m.x95)**2 + (m.x184 - m.x185)**2) + 1 / sqrt((m.x4 - m.x6)**2 + (m.x94 -
    m.x96)**2 + (m.x184 - m.x186)**2) + 1 / sqrt((m.x4 - m.x7)**2 + (m.x94 -
    m.x97)**2 + (m.x184 - m.x187)**2) + 1 / sqrt((m.x4 - m.x8)**2 + (m.x94 -
    m.x98)**2 + (m.x184 - m.x188)**2) + 1 / sqrt((m.x4 - m.x9)**2 + (m.x94 -
    m.x99)**2 + (m.x184 - m.x189)**2) + 1 / sqrt((m.x4 - m.x10)**2 + (m.x94 -
    m.x100)**2 + (m.x184 - m.x190)**2) + 1 / sqrt((m.x4 - m.x11)**2 + (m.x94 -
    m.x101)**2 + (m.x184 - m.x191)**2) + 1 / sqrt((m.x4 - m.x12)**2 + (m.x94 -
    m.x102)**2 + (m.x184 - m.x192)**2) + 1 / sqrt((m.x4 - m.x13)**2 + (m.x94 -
    m.x103)**2 + (m.x184 - m.x193)**2) + 1 / sqrt((m.x4 - m.x14)**2 + (m.x94 -
    m.x104)**2 + (m.x184 - m.x194)**2) + 1 / sqrt((m.x4 - m.x15)**2 + (m.x94 -
    m.x105)**2 + (m.x184 - m.x195)**2) + 1 / sqrt((m.x4 - m.x16)**2 + (m.x94 -
    m.x106)**2 + (m.x184 - m.x196)**2) + 1 / sqrt((m.x4 - m.x17)**2 + (m.x94 -
    m.x107)**2 + (m.x184 - m.x197)**2) + 1 / sqrt((m.x4 - m.x18)**2 + (m.x94 -
    m.x108)**2 + (m.x184 - m.x198)**2) + 1 / sqrt((m.x4 - m.x19)**2 + (m.x94 -
    m.x109)**2 + (m.x184 - m.x199)**2) + 1 / sqrt((m.x4 - m.x20)**2 + (m.x94 -
    m.x110)**2 + (m.x184 - m.x200)**2) + 1 / sqrt((m.x4 - m.x21)**2 + (m.x94 -
    m.x111)**2 + (m.x184 - m.x201)**2) + 1 / sqrt((m.x4 - m.x22)**2 + (m.x94 -
    m.x112)**2 + (m.x184 - m.x202)**2) + 1 / sqrt((m.x4 - m.x23)**2 + (m.x94 -
    m.x113)**2 + (m.x184 - m.x203)**2) + 1 / sqrt((m.x4 - m.x24)**2 + (m.x94 -
    m.x114)**2 + (m.x184 - m.x204)**2) + 1 / sqrt((m.x4 - m.x25)**2 + (m.x94 -
    m.x115)**2 + (m.x184 - m.x205)**2) + 1 / sqrt((m.x4 - m.x26)**2 + (m.x94 -
    m.x116)**2 + (m.x184 - m.x206)**2) + 1 / sqrt((m.x4 - m.x27)**2 + (m.x94 -
    m.x117)**2 + (m.x184 - m.x207)**2) + 1 / sqrt((m.x4 - m.x28)**2 + (m.x94 -
    m.x118)**2 + (m.x184 - m.x208)**2) + 1 / sqrt((m.x4 - m.x29)**2 + (m.x94 -
    m.x119)**2 + (m.x184 - m.x209)**2) + 1 / sqrt((m.x4 - m.x30)**2 + (m.x94 -
    m.x120)**2 + (m.x184 - m.x210)**2) + 1 / sqrt((m.x4 - m.x31)**2 + (m.x94 -
    m.x121)**2 + (m.x184 - m.x211)**2) + 1 / sqrt((m.x4 - m.x32)**2 + (m.x94 -
    m.x122)**2 + (m.x184 - m.x212)**2) + 1 / sqrt((m.x4 - m.x33)**2 + (m.x94 -
    m.x123)**2 + (m.x184 - m.x213)**2) + 1 / sqrt((m.x4 - m.x34)**2 + (m.x94 -
    m.x124)**2 + (m.x184 - m.x214)**2) + 1 / sqrt((m.x4 - m.x35)**2 + (m.x94 -
    m.x125)**2 + (m.x184 - m.x215)**2) + 1 / sqrt((m.x4 - m.x36)**2 + (m.x94 -
    m.x126)**2 + (m.x184 - m.x216)**2) + 1 / sqrt((m.x4 - m.x37)**2 + (m.x94 -
    m.x127)**2 + (m.x184 - m.x217)**2) + 1 / sqrt((m.x4 - m.x38)**2 + (m.x94 -
    m.x128)**2 + (m.x184 - m.x218)**2) + 1 / sqrt((m.x4 - m.x39)**2 + (m.x94 -
    m.x129)**2 + (m.x184 - m.x219)**2) + 1 / sqrt((m.x4 - m.x40)**2 + (m.x94 -
    m.x130)**2 + (m.x184 - m.x220)**2) + 1 / sqrt((m.x4 - m.x41)**2 + (m.x94 -
    m.x131)**2 + (m.x184 - m.x221)**2) + 1 / sqrt((m.x4 - m.x42)**2 + (m.x94 -
    m.x132)**2 + (m.x184 - m.x222)**2) + 1 / sqrt((m.x4 - m.x43)**2 + (m.x94 -
    m.x133)**2 + (m.x184 - m.x223)**2) + 1 / sqrt((m.x4 - m.x44)**2 + (m.x94 -
    m.x134)**2 + (m.x184 - m.x224)**2) + 1 / sqrt((m.x4 - m.x45)**2 + (m.x94 -
    m.x135)**2 + (m.x184 - m.x225)**2) + 1 / sqrt((m.x4 - m.x46)**2 + (m.x94 -
    m.x136)**2 + (m.x184 - m.x226)**2) + 1 / sqrt((m.x4 - m.x47)**2 + (m.x94 -
    m.x137)**2 + (m.x184 - m.x227)**2) + 1 / sqrt((m.x4 - m.x48)**2 + (m.x94 -
    m.x138)**2 + (m.x184 - m.x228)**2) + 1 / sqrt((m.x4 - m.x49)**2 + (m.x94 -
    m.x139)**2 + (m.x184 - m.x229)**2) + 1 / sqrt((m.x4 - m.x50)**2 + (m.x94 -
    m.x140)**2 + (m.x184 - m.x230)**2) + 1 / sqrt((m.x4 - m.x51)**2 + (m.x94 -
    m.x141)**2 + (m.x184 - m.x231)**2) + 1 / sqrt((m.x4 - m.x52)**2 + (m.x94 -
    m.x142)**2 + (m.x184 - m.x232)**2) + 1 / sqrt((m.x4 - m.x53)**2 + (m.x94 -
    m.x143)**2 + (m.x184 - m.x233)**2) + 1 / sqrt((m.x4 - m.x54)**2 + (m.x94 -
    m.x144)**2 + (m.x184 - m.x234)**2) + 1 / sqrt((m.x4 - m.x55)**2 + (m.x94 -
    m.x145)**2 + (m.x184 - m.x235)**2) + 1 / sqrt((m.x4 - m.x56)**2 + (m.x94 -
    m.x146)**2 + (m.x184 - m.x236)**2) + 1 / sqrt((m.x4 - m.x57)**2 + (m.x94 -
    m.x147)**2 + (m.x184 - m.x237)**2) + 1 / sqrt((m.x4 - m.x58)**2 + (m.x94 -
    m.x148)**2 + (m.x184 - m.x238)**2) + 1 / sqrt((m.x4 - m.x59)**2 + (m.x94 -
    m.x149)**2 + (m.x184 - m.x239)**2) + 1 / sqrt((m.x4 - m.x60)**2 + (m.x94 -
    m.x150)**2 + (m.x184 - m.x240)**2) + 1 / sqrt((m.x4 - m.x61)**2 + (m.x94 -
    m.x151)**2 + (m.x184 - m.x241)**2) + 1 / sqrt((m.x4 - m.x62)**2 + (m.x94 -
    m.x152)**2 + (m.x184 - m.x242)**2) + 1 / sqrt((m.x4 - m.x63)**2 + (m.x94 -
    m.x153)**2 + (m.x184 - m.x243)**2) + 1 / sqrt((m.x4 - m.x64)**2 + (m.x94 -
    m.x154)**2 + (m.x184 - m.x244)**2) + 1 / sqrt((m.x4 - m.x65)**2 + (m.x94 -
    m.x155)**2 + (m.x184 - m.x245)**2) + 1 / sqrt((m.x4 - m.x66)**2 + (m.x94 -
    m.x156)**2 + (m.x184 - m.x246)**2) + 1 / sqrt((m.x4 - m.x67)**2 + (m.x94 -
    m.x157)**2 + (m.x184 - m.x247)**2) + 1 / sqrt((m.x4 - m.x68)**2 + (m.x94 -
    m.x158)**2 + (m.x184 - m.x248)**2) + 1 / sqrt((m.x4 - m.x69)**2 + (m.x94 -
    m.x159)**2 + (m.x184 - m.x249)**2) + 1 / sqrt((m.x4 - m.x70)**2 + (m.x94 -
    m.x160)**2 + (m.x184 - m.x250)**2) + 1 / sqrt((m.x4 - m.x71)**2 + (m.x94 -
    m.x161)**2 + (m.x184 - m.x251)**2) + 1 / sqrt((m.x4 - m.x72)**2 + (m.x94 -
    m.x162)**2 + (m.x184 - m.x252)**2) + 1 / sqrt((m.x4 - m.x73)**2 + (m.x94 -
    m.x163)**2 + (m.x184 - m.x253)**2) + 1 / sqrt((m.x4 - m.x74)**2 + (m.x94 -
    m.x164)**2 + (m.x184 - m.x254)**2) + 1 / sqrt((m.x4 - m.x75)**2 + (m.x94 -
    m.x165)**2 + (m.x184 - m.x255)**2) + 1 / sqrt((m.x4 - m.x76)**2 + (m.x94 -
    m.x166)**2 + (m.x184 - m.x256)**2) + 1 / sqrt((m.x4 - m.x77)**2 + (m.x94 -
    m.x167)**2 + (m.x184 - m.x257)**2) + 1 / sqrt((m.x4 - m.x78)**2 + (m.x94 -
    m.x168)**2 + (m.x184 - m.x258)**2) + 1 / sqrt((m.x4 - m.x79)**2 + (m.x94 -
    m.x169)**2 + (m.x184 - m.x259)**2) + 1 / sqrt((m.x4 - m.x80)**2 + (m.x94 -
    m.x170)**2 + (m.x184 - m.x260)**2) + 1 / sqrt((m.x4 - m.x81)**2 + (m.x94 -
    m.x171)**2 + (m.x184 - m.x261)**2) + 1 / sqrt((m.x4 - m.x82)**2 + (m.x94 -
    m.x172)**2 + (m.x184 - m.x262)**2) + 1 / sqrt((m.x4 - m.x83)**2 + (m.x94 -
    m.x173)**2 + (m.x184 - m.x263)**2) + 1 / sqrt((m.x4 - m.x84)**2 + (m.x94 -
    m.x174)**2 + (m.x184 - m.x264)**2) + 1 / sqrt((m.x4 - m.x85)**2 + (m.x94 -
    m.x175)**2 + (m.x184 - m.x265)**2) + 1 / sqrt((m.x4 - m.x86)**2 + (m.x94 -
    m.x176)**2 + (m.x184 - m.x266)**2) + 1 / sqrt((m.x4 - m.x87)**2 + (m.x94 -
    m.x177)**2 + (m.x184 - m.x267)**2) + 1 / sqrt((m.x4 - m.x88)**2 + (m.x94 -
    m.x178)**2 + (m.x184 - m.x268)**2) + 1 / sqrt((m.x4 - m.x89)**2 + (m.x94 -
    m.x179)**2 + (m.x184 - m.x269)**2) + 1 / sqrt((m.x4 - m.x90)**2 + (m.x94 -
    m.x180)**2 + (m.x184 - m.x270)**2) + 1 / sqrt((m.x5 - m.x6)**2 + (m.x95 -
    m.x96)**2 + (m.x185 - m.x186)**2) + 1 / sqrt((m.x5 - m.x7)**2 + (m.x95 -
    m.x97)**2 + (m.x185 - m.x187)**2) + 1 / sqrt((m.x5 - m.x8)**2 + (m.x95 -
    m.x98)**2 + (m.x185 - m.x188)**2) + 1 / sqrt((m.x5 - m.x9)**2 + (m.x95 -
    m.x99)**2 + (m.x185 - m.x189)**2) + 1 / sqrt((m.x5 - m.x10)**2 + (m.x95 -
    m.x100)**2 + (m.x185 - m.x190)**2) + 1 / sqrt((m.x5 - m.x11)**2 + (m.x95 -
    m.x101)**2 + (m.x185 - m.x191)**2) + 1 / sqrt((m.x5 - m.x12)**2 + (m.x95 -
    m.x102)**2 + (m.x185 - m.x192)**2) + 1 / sqrt((m.x5 - m.x13)**2 + (m.x95 -
    m.x103)**2 + (m.x185 - m.x193)**2) + 1 / sqrt((m.x5 - m.x14)**2 + (m.x95 -
    m.x104)**2 + (m.x185 - m.x194)**2) + 1 / sqrt((m.x5 - m.x15)**2 + (m.x95 -
    m.x105)**2 + (m.x185 - m.x195)**2) + 1 / sqrt((m.x5 - m.x16)**2 + (m.x95 -
    m.x106)**2 + (m.x185 - m.x196)**2) + 1 / sqrt((m.x5 - m.x17)**2 + (m.x95 -
    m.x107)**2 + (m.x185 - m.x197)**2) + 1 / sqrt((m.x5 - m.x18)**2 + (m.x95 -
    m.x108)**2 + (m.x185 - m.x198)**2) + 1 / sqrt((m.x5 - m.x19)**2 + (m.x95 -
    m.x109)**2 + (m.x185 - m.x199)**2) + 1 / sqrt((m.x5 - m.x20)**2 + (m.x95 -
    m.x110)**2 + (m.x185 - m.x200)**2) + 1 / sqrt((m.x5 - m.x21)**2 + (m.x95 -
    m.x111)**2 + (m.x185 - m.x201)**2) + 1 / sqrt((m.x5 - m.x22)**2 + (m.x95 -
    m.x112)**2 + (m.x185 - m.x202)**2) + 1 / sqrt((m.x5 - m.x23)**2 + (m.x95 -
    m.x113)**2 + (m.x185 - m.x203)**2) + 1 / sqrt((m.x5 - m.x24)**2 + (m.x95 -
    m.x114)**2 + (m.x185 - m.x204)**2) + 1 / sqrt((m.x5 - m.x25)**2 + (m.x95 -
    m.x115)**2 + (m.x185 - m.x205)**2) + 1 / sqrt((m.x5 - m.x26)**2 + (m.x95 -
    m.x116)**2 + (m.x185 - m.x206)**2) + 1 / sqrt((m.x5 - m.x27)**2 + (m.x95 -
    m.x117)**2 + (m.x185 - m.x207)**2) + 1 / sqrt((m.x5 - m.x28)**2 + (m.x95 -
    m.x118)**2 + (m.x185 - m.x208)**2) + 1 / sqrt((m.x5 - m.x29)**2 + (m.x95 -
    m.x119)**2 + (m.x185 - m.x209)**2) + 1 / sqrt((m.x5 - m.x30)**2 + (m.x95 -
    m.x120)**2 + (m.x185 - m.x210)**2) + 1 / sqrt((m.x5 - m.x31)**2 + (m.x95 -
    m.x121)**2 + (m.x185 - m.x211)**2) + 1 / sqrt((m.x5 - m.x32)**2 + (m.x95 -
    m.x122)**2 + (m.x185 - m.x212)**2) + 1 / sqrt((m.x5 - m.x33)**2 + (m.x95 -
    m.x123)**2 + (m.x185 - m.x213)**2) + 1 / sqrt((m.x5 - m.x34)**2 + (m.x95 -
    m.x124)**2 + (m.x185 - m.x214)**2) + 1 / sqrt((m.x5 - m.x35)**2 + (m.x95 -
    m.x125)**2 + (m.x185 - m.x215)**2) + 1 / sqrt((m.x5 - m.x36)**2 + (m.x95 -
    m.x126)**2 + (m.x185 - m.x216)**2) + 1 / sqrt((m.x5 - m.x37)**2 + (m.x95 -
    m.x127)**2 + (m.x185 - m.x217)**2) + 1 / sqrt((m.x5 - m.x38)**2 + (m.x95 -
    m.x128)**2 + (m.x185 - m.x218)**2) + 1 / sqrt((m.x5 - m.x39)**2 + (m.x95 -
    m.x129)**2 + (m.x185 - m.x219)**2) + 1 / sqrt((m.x5 - m.x40)**2 + (m.x95 -
    m.x130)**2 + (m.x185 - m.x220)**2) + 1 / sqrt((m.x5 - m.x41)**2 + (m.x95 -
    m.x131)**2 + (m.x185 - m.x221)**2) + 1 / sqrt((m.x5 - m.x42)**2 + (m.x95 -
    m.x132)**2 + (m.x185 - m.x222)**2) + 1 / sqrt((m.x5 - m.x43)**2 + (m.x95 -
    m.x133)**2 + (m.x185 - m.x223)**2) + 1 / sqrt((m.x5 - m.x44)**2 + (m.x95 -
    m.x134)**2 + (m.x185 - m.x224)**2) + 1 / sqrt((m.x5 - m.x45)**2 + (m.x95 -
    m.x135)**2 + (m.x185 - m.x225)**2) + 1 / sqrt((m.x5 - m.x46)**2 + (m.x95 -
    m.x136)**2 + (m.x185 - m.x226)**2) + 1 / sqrt((m.x5 - m.x47)**2 + (m.x95 -
    m.x137)**2 + (m.x185 - m.x227)**2) + 1 / sqrt((m.x5 - m.x48)**2 + (m.x95 -
    m.x138)**2 + (m.x185 - m.x228)**2) + 1 / sqrt((m.x5 - m.x49)**2 + (m.x95 -
    m.x139)**2 + (m.x185 - m.x229)**2) + 1 / sqrt((m.x5 - m.x50)**2 + (m.x95 -
    m.x140)**2 + (m.x185 - m.x230)**2) + 1 / sqrt((m.x5 - m.x51)**2 + (m.x95 -
    m.x141)**2 + (m.x185 - m.x231)**2) + 1 / sqrt((m.x5 - m.x52)**2 + (m.x95 -
    m.x142)**2 + (m.x185 - m.x232)**2) + 1 / sqrt((m.x5 - m.x53)**2 + (m.x95 -
    m.x143)**2 + (m.x185 - m.x233)**2) + 1 / sqrt((m.x5 - m.x54)**2 + (m.x95 -
    m.x144)**2 + (m.x185 - m.x234)**2) + 1 / sqrt((m.x5 - m.x55)**2 + (m.x95 -
    m.x145)**2 + (m.x185 - m.x235)**2) + 1 / sqrt((m.x5 - m.x56)**2 + (m.x95 -
    m.x146)**2 + (m.x185 - m.x236)**2) + 1 / sqrt((m.x5 - m.x57)**2 + (m.x95 -
    m.x147)**2 + (m.x185 - m.x237)**2) + 1 / sqrt((m.x5 - m.x58)**2 + (m.x95 -
    m.x148)**2 + (m.x185 - m.x238)**2) + 1 / sqrt((m.x5 - m.x59)**2 + (m.x95 -
    m.x149)**2 + (m.x185 - m.x239)**2) + 1 / sqrt((m.x5 - m.x60)**2 + (m.x95 -
    m.x150)**2 + (m.x185 - m.x240)**2) + 1 / sqrt((m.x5 - m.x61)**2 + (m.x95 -
    m.x151)**2 + (m.x185 - m.x241)**2) + 1 / sqrt((m.x5 - m.x62)**2 + (m.x95 -
    m.x152)**2 + (m.x185 - m.x242)**2) + 1 / sqrt((m.x5 - m.x63)**2 + (m.x95 -
    m.x153)**2 + (m.x185 - m.x243)**2) + 1 / sqrt((m.x5 - m.x64)**2 + (m.x95 -
    m.x154)**2 + (m.x185 - m.x244)**2) + 1 / sqrt((m.x5 - m.x65)**2 + (m.x95 -
    m.x155)**2 + (m.x185 - m.x245)**2) + 1 / sqrt((m.x5 - m.x66)**2 + (m.x95 -
    m.x156)**2 + (m.x185 - m.x246)**2) + 1 / sqrt((m.x5 - m.x67)**2 + (m.x95 -
    m.x157)**2 + (m.x185 - m.x247)**2) + 1 / sqrt((m.x5 - m.x68)**2 + (m.x95 -
    m.x158)**2 + (m.x185 - m.x248)**2) + 1 / sqrt((m.x5 - m.x69)**2 + (m.x95 -
    m.x159)**2 + (m.x185 - m.x249)**2) + 1 / sqrt((m.x5 - m.x70)**2 + (m.x95 -
    m.x160)**2 + (m.x185 - m.x250)**2) + 1 / sqrt((m.x5 - m.x71)**2 + (m.x95 -
    m.x161)**2 + (m.x185 - m.x251)**2) + 1 / sqrt((m.x5 - m.x72)**2 + (m.x95 -
    m.x162)**2 + (m.x185 - m.x252)**2) + 1 / sqrt((m.x5 - m.x73)**2 + (m.x95 -
    m.x163)**2 + (m.x185 - m.x253)**2) + 1 / sqrt((m.x5 - m.x74)**2 + (m.x95 -
    m.x164)**2 + (m.x185 - m.x254)**2) + 1 / sqrt((m.x5 - m.x75)**2 + (m.x95 -
    m.x165)**2 + (m.x185 - m.x255)**2) + 1 / sqrt((m.x5 - m.x76)**2 + (m.x95 -
    m.x166)**2 + (m.x185 - m.x256)**2) + 1 / sqrt((m.x5 - m.x77)**2 + (m.x95 -
    m.x167)**2 + (m.x185 - m.x257)**2) + 1 / sqrt((m.x5 - m.x78)**2 + (m.x95 -
    m.x168)**2 + (m.x185 - m.x258)**2) + 1 / sqrt((m.x5 - m.x79)**2 + (m.x95 -
    m.x169)**2 + (m.x185 - m.x259)**2) + 1 / sqrt((m.x5 - m.x80)**2 + (m.x95 -
    m.x170)**2 + (m.x185 - m.x260)**2) + 1 / sqrt((m.x5 - m.x81)**2 + (m.x95 -
    m.x171)**2 + (m.x185 - m.x261)**2) + 1 / sqrt((m.x5 - m.x82)**2 + (m.x95 -
    m.x172)**2 + (m.x185 - m.x262)**2) + 1 / sqrt((m.x5 - m.x83)**2 + (m.x95 -
    m.x173)**2 + (m.x185 - m.x263)**2) + 1 / sqrt((m.x5 - m.x84)**2 + (m.x95 -
    m.x174)**2 + (m.x185 - m.x264)**2) + 1 / sqrt((m.x5 - m.x85)**2 + (m.x95 -
    m.x175)**2 + (m.x185 - m.x265)**2) + 1 / sqrt((m.x5 - m.x86)**2 + (m.x95 -
    m.x176)**2 + (m.x185 - m.x266)**2) + 1 / sqrt((m.x5 - m.x87)**2 + (m.x95 -
    m.x177)**2 + (m.x185 - m.x267)**2) + 1 / sqrt((m.x5 - m.x88)**2 + (m.x95 -
    m.x178)**2 + (m.x185 - m.x268)**2) + 1 / sqrt((m.x5 - m.x89)**2 + (m.x95 -
    m.x179)**2 + (m.x185 - m.x269)**2) + 1 / sqrt((m.x5 - m.x90)**2 + (m.x95 -
    m.x180)**2 + (m.x185 - m.x270)**2) + 1 / sqrt((m.x6 - m.x7)**2 + (m.x96 -
    m.x97)**2 + (m.x186 - m.x187)**2) + 1 / sqrt((m.x6 - m.x8)**2 + (m.x96 -
    m.x98)**2 + (m.x186 - m.x188)**2) + 1 / sqrt((m.x6 - m.x9)**2 + (m.x96 -
    m.x99)**2 + (m.x186 - m.x189)**2) + 1 / sqrt((m.x6 - m.x10)**2 + (m.x96 -
    m.x100)**2 + (m.x186 - m.x190)**2) + 1 / sqrt((m.x6 - m.x11)**2 + (m.x96 -
    m.x101)**2 + (m.x186 - m.x191)**2) + 1 / sqrt((m.x6 - m.x12)**2 + (m.x96 -
    m.x102)**2 + (m.x186 - m.x192)**2) + 1 / sqrt((m.x6 - m.x13)**2 + (m.x96 -
    m.x103)**2 + (m.x186 - m.x193)**2) + 1 / sqrt((m.x6 - m.x14)**2 + (m.x96 -
    m.x104)**2 + (m.x186 - m.x194)**2) + 1 / sqrt((m.x6 - m.x15)**2 + (m.x96 -
    m.x105)**2 + (m.x186 - m.x195)**2) + 1 / sqrt((m.x6 - m.x16)**2 + (m.x96 -
    m.x106)**2 + (m.x186 - m.x196)**2) + 1 / sqrt((m.x6 - m.x17)**2 + (m.x96 -
    m.x107)**2 + (m.x186 - m.x197)**2) + 1 / sqrt((m.x6 - m.x18)**2 + (m.x96 -
    m.x108)**2 + (m.x186 - m.x198)**2) + 1 / sqrt((m.x6 - m.x19)**2 + (m.x96 -
    m.x109)**2 + (m.x186 - m.x199)**2) + 1 / sqrt((m.x6 - m.x20)**2 + (m.x96 -
    m.x110)**2 + (m.x186 - m.x200)**2) + 1 / sqrt((m.x6 - m.x21)**2 + (m.x96 -
    m.x111)**2 + (m.x186 - m.x201)**2) + 1 / sqrt((m.x6 - m.x22)**2 + (m.x96 -
    m.x112)**2 + (m.x186 - m.x202)**2) + 1 / sqrt((m.x6 - m.x23)**2 + (m.x96 -
    m.x113)**2 + (m.x186 - m.x203)**2) + 1 / sqrt((m.x6 - m.x24)**2 + (m.x96 -
    m.x114)**2 + (m.x186 - m.x204)**2) + 1 / sqrt((m.x6 - m.x25)**2 + (m.x96 -
    m.x115)**2 + (m.x186 - m.x205)**2) + 1 / sqrt((m.x6 - m.x26)**2 + (m.x96 -
    m.x116)**2 + (m.x186 - m.x206)**2) + 1 / sqrt((m.x6 - m.x27)**2 + (m.x96 -
    m.x117)**2 + (m.x186 - m.x207)**2) + 1 / sqrt((m.x6 - m.x28)**2 + (m.x96 -
    m.x118)**2 + (m.x186 - m.x208)**2) + 1 / sqrt((m.x6 - m.x29)**2 + (m.x96 -
    m.x119)**2 + (m.x186 - m.x209)**2) + 1 / sqrt((m.x6 - m.x30)**2 + (m.x96 -
    m.x120)**2 + (m.x186 - m.x210)**2) + 1 / sqrt((m.x6 - m.x31)**2 + (m.x96 -
    m.x121)**2 + (m.x186 - m.x211)**2) + 1 / sqrt((m.x6 - m.x32)**2 + (m.x96 -
    m.x122)**2 + (m.x186 - m.x212)**2) + 1 / sqrt((m.x6 - m.x33)**2 + (m.x96 -
    m.x123)**2 + (m.x186 - m.x213)**2) + 1 / sqrt((m.x6 - m.x34)**2 + (m.x96 -
    m.x124)**2 + (m.x186 - m.x214)**2) + 1 / sqrt((m.x6 - m.x35)**2 + (m.x96 -
    m.x125)**2 + (m.x186 - m.x215)**2) + 1 / sqrt((m.x6 - m.x36)**2 + (m.x96 -
    m.x126)**2 + (m.x186 - m.x216)**2) + 1 / sqrt((m.x6 - m.x37)**2 + (m.x96 -
    m.x127)**2 + (m.x186 - m.x217)**2) + 1 / sqrt((m.x6 - m.x38)**2 + (m.x96 -
    m.x128)**2 + (m.x186 - m.x218)**2) + 1 / sqrt((m.x6 - m.x39)**2 + (m.x96 -
    m.x129)**2 + (m.x186 - m.x219)**2) + 1 / sqrt((m.x6 - m.x40)**2 + (m.x96 -
    m.x130)**2 + (m.x186 - m.x220)**2) + 1 / sqrt((m.x6 - m.x41)**2 + (m.x96 -
    m.x131)**2 + (m.x186 - m.x221)**2) + 1 / sqrt((m.x6 - m.x42)**2 + (m.x96 -
    m.x132)**2 + (m.x186 - m.x222)**2) + 1 / sqrt((m.x6 - m.x43)**2 + (m.x96 -
    m.x133)**2 + (m.x186 - m.x223)**2) + 1 / sqrt((m.x6 - m.x44)**2 + (m.x96 -
    m.x134)**2 + (m.x186 - m.x224)**2) + 1 / sqrt((m.x6 - m.x45)**2 + (m.x96 -
    m.x135)**2 + (m.x186 - m.x225)**2) + 1 / sqrt((m.x6 - m.x46)**2 + (m.x96 -
    m.x136)**2 + (m.x186 - m.x226)**2) + 1 / sqrt((m.x6 - m.x47)**2 + (m.x96 -
    m.x137)**2 + (m.x186 - m.x227)**2) + 1 / sqrt((m.x6 - m.x48)**2 + (m.x96 -
    m.x138)**2 + (m.x186 - m.x228)**2) + 1 / sqrt((m.x6 - m.x49)**2 + (m.x96 -
    m.x139)**2 + (m.x186 - m.x229)**2) + 1 / sqrt((m.x6 - m.x50)**2 + (m.x96 -
    m.x140)**2 + (m.x186 - m.x230)**2) + 1 / sqrt((m.x6 - m.x51)**2 + (m.x96 -
    m.x141)**2 + (m.x186 - m.x231)**2) + 1 / sqrt((m.x6 - m.x52)**2 + (m.x96 -
    m.x142)**2 + (m.x186 - m.x232)**2) + 1 / sqrt((m.x6 - m.x53)**2 + (m.x96 -
    m.x143)**2 + (m.x186 - m.x233)**2) + 1 / sqrt((m.x6 - m.x54)**2 + (m.x96 -
    m.x144)**2 + (m.x186 - m.x234)**2) + 1 / sqrt((m.x6 - m.x55)**2 + (m.x96 -
    m.x145)**2 + (m.x186 - m.x235)**2) + 1 / sqrt((m.x6 - m.x56)**2 + (m.x96 -
    m.x146)**2 + (m.x186 - m.x236)**2) + 1 / sqrt((m.x6 - m.x57)**2 + (m.x96 -
    m.x147)**2 + (m.x186 - m.x237)**2) + 1 / sqrt((m.x6 - m.x58)**2 + (m.x96 -
    m.x148)**2 + (m.x186 - m.x238)**2) + 1 / sqrt((m.x6 - m.x59)**2 + (m.x96 -
    m.x149)**2 + (m.x186 - m.x239)**2) + 1 / sqrt((m.x6 - m.x60)**2 + (m.x96 -
    m.x150)**2 + (m.x186 - m.x240)**2) + 1 / sqrt((m.x6 - m.x61)**2 + (m.x96 -
    m.x151)**2 + (m.x186 - m.x241)**2) + 1 / sqrt((m.x6 - m.x62)**2 + (m.x96 -
    m.x152)**2 + (m.x186 - m.x242)**2) + 1 / sqrt((m.x6 - m.x63)**2 + (m.x96 -
    m.x153)**2 + (m.x186 - m.x243)**2) + 1 / sqrt((m.x6 - m.x64)**2 + (m.x96 -
    m.x154)**2 + (m.x186 - m.x244)**2) + 1 / sqrt((m.x6 - m.x65)**2 + (m.x96 -
    m.x155)**2 + (m.x186 - m.x245)**2) + 1 / sqrt((m.x6 - m.x66)**2 + (m.x96 -
    m.x156)**2 + (m.x186 - m.x246)**2) + 1 / sqrt((m.x6 - m.x67)**2 + (m.x96 -
    m.x157)**2 + (m.x186 - m.x247)**2) + 1 / sqrt((m.x6 - m.x68)**2 + (m.x96 -
    m.x158)**2 + (m.x186 - m.x248)**2) + 1 / sqrt((m.x6 - m.x69)**2 + (m.x96 -
    m.x159)**2 + (m.x186 - m.x249)**2) + 1 / sqrt((m.x6 - m.x70)**2 + (m.x96 -
    m.x160)**2 + (m.x186 - m.x250)**2) + 1 / sqrt((m.x6 - m.x71)**2 + (m.x96 -
    m.x161)**2 + (m.x186 - m.x251)**2) + 1 / sqrt((m.x6 - m.x72)**2 + (m.x96 -
    m.x162)**2 + (m.x186 - m.x252)**2) + 1 / sqrt((m.x6 - m.x73)**2 + (m.x96 -
    m.x163)**2 + (m.x186 - m.x253)**2) + 1 / sqrt((m.x6 - m.x74)**2 + (m.x96 -
    m.x164)**2 + (m.x186 - m.x254)**2) + 1 / sqrt((m.x6 - m.x75)**2 + (m.x96 -
    m.x165)**2 + (m.x186 - m.x255)**2) + 1 / sqrt((m.x6 - m.x76)**2 + (m.x96 -
    m.x166)**2 + (m.x186 - m.x256)**2) + 1 / sqrt((m.x6 - m.x77)**2 + (m.x96 -
    m.x167)**2 + (m.x186 - m.x257)**2) + 1 / sqrt((m.x6 - m.x78)**2 + (m.x96 -
    m.x168)**2 + (m.x186 - m.x258)**2) + 1 / sqrt((m.x6 - m.x79)**2 + (m.x96 -
    m.x169)**2 + (m.x186 - m.x259)**2) + 1 / sqrt((m.x6 - m.x80)**2 + (m.x96 -
    m.x170)**2 + (m.x186 - m.x260)**2) + 1 / sqrt((m.x6 - m.x81)**2 + (m.x96 -
    m.x171)**2 + (m.x186 - m.x261)**2) + 1 / sqrt((m.x6 - m.x82)**2 + (m.x96 -
    m.x172)**2 + (m.x186 - m.x262)**2) + 1 / sqrt((m.x6 - m.x83)**2 + (m.x96 -
    m.x173)**2 + (m.x186 - m.x263)**2) + 1 / sqrt((m.x6 - m.x84)**2 + (m.x96 -
    m.x174)**2 + (m.x186 - m.x264)**2) + 1 / sqrt((m.x6 - m.x85)**2 + (m.x96 -
    m.x175)**2 + (m.x186 - m.x265)**2) + 1 / sqrt((m.x6 - m.x86)**2 + (m.x96 -
    m.x176)**2 + (m.x186 - m.x266)**2) + 1 / sqrt((m.x6 - m.x87)**2 + (m.x96 -
    m.x177)**2 + (m.x186 - m.x267)**2) + 1 / sqrt((m.x6 - m.x88)**2 + (m.x96 -
    m.x178)**2 + (m.x186 - m.x268)**2) + 1 / sqrt((m.x6 - m.x89)**2 + (m.x96 -
    m.x179)**2 + (m.x186 - m.x269)**2) + 1 / sqrt((m.x6 - m.x90)**2 + (m.x96 -
    m.x180)**2 + (m.x186 - m.x270)**2) + 1 / sqrt((m.x7 - m.x8)**2 + (m.x97 -
    m.x98)**2 + (m.x187 - m.x188)**2) + 1 / sqrt((m.x7 - m.x9)**2 + (m.x97 -
    m.x99)**2 + (m.x187 - m.x189)**2) + 1 / sqrt((m.x7 - m.x10)**2 + (m.x97 -
    m.x100)**2 + (m.x187 - m.x190)**2) + 1 / sqrt((m.x7 - m.x11)**2 + (m.x97 -
    m.x101)**2 + (m.x187 - m.x191)**2) + 1 / sqrt((m.x7 - m.x12)**2 + (m.x97 -
    m.x102)**2 + (m.x187 - m.x192)**2) + 1 / sqrt((m.x7 - m.x13)**2 + (m.x97 -
    m.x103)**2 + (m.x187 - m.x193)**2) + 1 / sqrt((m.x7 - m.x14)**2 + (m.x97 -
    m.x104)**2 + (m.x187 - m.x194)**2) + 1 / sqrt((m.x7 - m.x15)**2 + (m.x97 -
    m.x105)**2 + (m.x187 - m.x195)**2) + 1 / sqrt((m.x7 - m.x16)**2 + (m.x97 -
    m.x106)**2 + (m.x187 - m.x196)**2) + 1 / sqrt((m.x7 - m.x17)**2 + (m.x97 -
    m.x107)**2 + (m.x187 - m.x197)**2) + 1 / sqrt((m.x7 - m.x18)**2 + (m.x97 -
    m.x108)**2 + (m.x187 - m.x198)**2) + 1 / sqrt((m.x7 - m.x19)**2 + (m.x97 -
    m.x109)**2 + (m.x187 - m.x199)**2) + 1 / sqrt((m.x7 - m.x20)**2 + (m.x97 -
    m.x110)**2 + (m.x187 - m.x200)**2) + 1 / sqrt((m.x7 - m.x21)**2 + (m.x97 -
    m.x111)**2 + (m.x187 - m.x201)**2) + 1 / sqrt((m.x7 - m.x22)**2 + (m.x97 -
    m.x112)**2 + (m.x187 - m.x202)**2) + 1 / sqrt((m.x7 - m.x23)**2 + (m.x97 -
    m.x113)**2 + (m.x187 - m.x203)**2) + 1 / sqrt((m.x7 - m.x24)**2 + (m.x97 -
    m.x114)**2 + (m.x187 - m.x204)**2) + 1 / sqrt((m.x7 - m.x25)**2 + (m.x97 -
    m.x115)**2 + (m.x187 - m.x205)**2) + 1 / sqrt((m.x7 - m.x26)**2 + (m.x97 -
    m.x116)**2 + (m.x187 - m.x206)**2) + 1 / sqrt((m.x7 - m.x27)**2 + (m.x97 -
    m.x117)**2 + (m.x187 - m.x207)**2) + 1 / sqrt((m.x7 - m.x28)**2 + (m.x97 -
    m.x118)**2 + (m.x187 - m.x208)**2) + 1 / sqrt((m.x7 - m.x29)**2 + (m.x97 -
    m.x119)**2 + (m.x187 - m.x209)**2) + 1 / sqrt((m.x7 - m.x30)**2 + (m.x97 -
    m.x120)**2 + (m.x187 - m.x210)**2) + 1 / sqrt((m.x7 - m.x31)**2 + (m.x97 -
    m.x121)**2 + (m.x187 - m.x211)**2) + 1 / sqrt((m.x7 - m.x32)**2 + (m.x97 -
    m.x122)**2 + (m.x187 - m.x212)**2) + 1 / sqrt((m.x7 - m.x33)**2 + (m.x97 -
    m.x123)**2 + (m.x187 - m.x213)**2) + 1 / sqrt((m.x7 - m.x34)**2 + (m.x97 -
    m.x124)**2 + (m.x187 - m.x214)**2) + 1 / sqrt((m.x7 - m.x35)**2 + (m.x97 -
    m.x125)**2 + (m.x187 - m.x215)**2) + 1 / sqrt((m.x7 - m.x36)**2 + (m.x97 -
    m.x126)**2 + (m.x187 - m.x216)**2) + 1 / sqrt((m.x7 - m.x37)**2 + (m.x97 -
    m.x127)**2 + (m.x187 - m.x217)**2) + 1 / sqrt((m.x7 - m.x38)**2 + (m.x97 -
    m.x128)**2 + (m.x187 - m.x218)**2) + 1 / sqrt((m.x7 - m.x39)**2 + (m.x97 -
    m.x129)**2 + (m.x187 - m.x219)**2) + 1 / sqrt((m.x7 - m.x40)**2 + (m.x97 -
    m.x130)**2 + (m.x187 - m.x220)**2) + 1 / sqrt((m.x7 - m.x41)**2 + (m.x97 -
    m.x131)**2 + (m.x187 - m.x221)**2) + 1 / sqrt((m.x7 - m.x42)**2 + (m.x97 -
    m.x132)**2 + (m.x187 - m.x222)**2) + 1 / sqrt((m.x7 - m.x43)**2 + (m.x97 -
    m.x133)**2 + (m.x187 - m.x223)**2) + 1 / sqrt((m.x7 - m.x44)**2 + (m.x97 -
    m.x134)**2 + (m.x187 - m.x224)**2) + 1 / sqrt((m.x7 - m.x45)**2 + (m.x97 -
    m.x135)**2 + (m.x187 - m.x225)**2) + 1 / sqrt((m.x7 - m.x46)**2 + (m.x97 -
    m.x136)**2 + (m.x187 - m.x226)**2) + 1 / sqrt((m.x7 - m.x47)**2 + (m.x97 -
    m.x137)**2 + (m.x187 - m.x227)**2) + 1 / sqrt((m.x7 - m.x48)**2 + (m.x97 -
    m.x138)**2 + (m.x187 - m.x228)**2) + 1 / sqrt((m.x7 - m.x49)**2 + (m.x97 -
    m.x139)**2 + (m.x187 - m.x229)**2) + 1 / sqrt((m.x7 - m.x50)**2 + (m.x97 -
    m.x140)**2 + (m.x187 - m.x230)**2) + 1 / sqrt((m.x7 - m.x51)**2 + (m.x97 -
    m.x141)**2 + (m.x187 - m.x231)**2) + 1 / sqrt((m.x7 - m.x52)**2 + (m.x97 -
    m.x142)**2 + (m.x187 - m.x232)**2) + 1 / sqrt((m.x7 - m.x53)**2 + (m.x97 -
    m.x143)**2 + (m.x187 - m.x233)**2) + 1 / sqrt((m.x7 - m.x54)**2 + (m.x97 -
    m.x144)**2 + (m.x187 - m.x234)**2) + 1 / sqrt((m.x7 - m.x55)**2 + (m.x97 -
    m.x145)**2 + (m.x187 - m.x235)**2) + 1 / sqrt((m.x7 - m.x56)**2 + (m.x97 -
    m.x146)**2 + (m.x187 - m.x236)**2) + 1 / sqrt((m.x7 - m.x57)**2 + (m.x97 -
    m.x147)**2 + (m.x187 - m.x237)**2) + 1 / sqrt((m.x7 - m.x58)**2 + (m.x97 -
    m.x148)**2 + (m.x187 - m.x238)**2) + 1 / sqrt((m.x7 - m.x59)**2 + (m.x97 -
    m.x149)**2 + (m.x187 - m.x239)**2) + 1 / sqrt((m.x7 - m.x60)**2 + (m.x97 -
    m.x150)**2 + (m.x187 - m.x240)**2) + 1 / sqrt((m.x7 - m.x61)**2 + (m.x97 -
    m.x151)**2 + (m.x187 - m.x241)**2) + 1 / sqrt((m.x7 - m.x62)**2 + (m.x97 -
    m.x152)**2 + (m.x187 - m.x242)**2) + 1 / sqrt((m.x7 - m.x63)**2 + (m.x97 -
    m.x153)**2 + (m.x187 - m.x243)**2) + 1 / sqrt((m.x7 - m.x64)**2 + (m.x97 -
    m.x154)**2 + (m.x187 - m.x244)**2) + 1 / sqrt((m.x7 - m.x65)**2 + (m.x97 -
    m.x155)**2 + (m.x187 - m.x245)**2) + 1 / sqrt((m.x7 - m.x66)**2 + (m.x97 -
    m.x156)**2 + (m.x187 - m.x246)**2) + 1 / sqrt((m.x7 - m.x67)**2 + (m.x97 -
    m.x157)**2 + (m.x187 - m.x247)**2) + 1 / sqrt((m.x7 - m.x68)**2 + (m.x97 -
    m.x158)**2 + (m.x187 - m.x248)**2) + 1 / sqrt((m.x7 - m.x69)**2 + (m.x97 -
    m.x159)**2 + (m.x187 - m.x249)**2) + 1 / sqrt((m.x7 - m.x70)**2 + (m.x97 -
    m.x160)**2 + (m.x187 - m.x250)**2) + 1 / sqrt((m.x7 - m.x71)**2 + (m.x97 -
    m.x161)**2 + (m.x187 - m.x251)**2) + 1 / sqrt((m.x7 - m.x72)**2 + (m.x97 -
    m.x162)**2 + (m.x187 - m.x252)**2) + 1 / sqrt((m.x7 - m.x73)**2 + (m.x97 -
    m.x163)**2 + (m.x187 - m.x253)**2) + 1 / sqrt((m.x7 - m.x74)**2 + (m.x97 -
    m.x164)**2 + (m.x187 - m.x254)**2) + 1 / sqrt((m.x7 - m.x75)**2 + (m.x97 -
    m.x165)**2 + (m.x187 - m.x255)**2) + 1 / sqrt((m.x7 - m.x76)**2 + (m.x97 -
    m.x166)**2 + (m.x187 - m.x256)**2) + 1 / sqrt((m.x7 - m.x77)**2 + (m.x97 -
    m.x167)**2 + (m.x187 - m.x257)**2) + 1 / sqrt((m.x7 - m.x78)**2 + (m.x97 -
    m.x168)**2 + (m.x187 - m.x258)**2) + 1 / sqrt((m.x7 - m.x79)**2 + (m.x97 -
    m.x169)**2 + (m.x187 - m.x259)**2) + 1 / sqrt((m.x7 - m.x80)**2 + (m.x97 -
    m.x170)**2 + (m.x187 - m.x260)**2) + 1 / sqrt((m.x7 - m.x81)**2 + (m.x97 -
    m.x171)**2 + (m.x187 - m.x261)**2) + 1 / sqrt((m.x7 - m.x82)**2 + (m.x97 -
    m.x172)**2 + (m.x187 - m.x262)**2) + 1 / sqrt((m.x7 - m.x83)**2 + (m.x97 -
    m.x173)**2 + (m.x187 - m.x263)**2) + 1 / sqrt((m.x7 - m.x84)**2 + (m.x97 -
    m.x174)**2 + (m.x187 - m.x264)**2) + 1 / sqrt((m.x7 - m.x85)**2 + (m.x97 -
    m.x175)**2 + (m.x187 - m.x265)**2) + 1 / sqrt((m.x7 - m.x86)**2 + (m.x97 -
    m.x176)**2 + (m.x187 - m.x266)**2) + 1 / sqrt((m.x7 - m.x87)**2 + (m.x97 -
    m.x177)**2 + (m.x187 - m.x267)**2) + 1 / sqrt((m.x7 - m.x88)**2 + (m.x97 -
    m.x178)**2 + (m.x187 - m.x268)**2) + 1 / sqrt((m.x7 - m.x89)**2 + (m.x97 -
    m.x179)**2 + (m.x187 - m.x269)**2) + 1 / sqrt((m.x7 - m.x90)**2 + (m.x97 -
    m.x180)**2 + (m.x187 - m.x270)**2) + 1 / sqrt((m.x8 - m.x9)**2 + (m.x98 -
    m.x99)**2 + (m.x188 - m.x189)**2) + 1 / sqrt((m.x8 - m.x10)**2 + (m.x98 -
    m.x100)**2 + (m.x188 - m.x190)**2) + 1 / sqrt((m.x8 - m.x11)**2 + (m.x98 -
    m.x101)**2 + (m.x188 - m.x191)**2) + 1 / sqrt((m.x8 - m.x12)**2 + (m.x98 -
    m.x102)**2 + (m.x188 - m.x192)**2) + 1 / sqrt((m.x8 - m.x13)**2 + (m.x98 -
    m.x103)**2 + (m.x188 - m.x193)**2) + 1 / sqrt((m.x8 - m.x14)**2 + (m.x98 -
    m.x104)**2 + (m.x188 - m.x194)**2) + 1 / sqrt((m.x8 - m.x15)**2 + (m.x98 -
    m.x105)**2 + (m.x188 - m.x195)**2) + 1 / sqrt((m.x8 - m.x16)**2 + (m.x98 -
    m.x106)**2 + (m.x188 - m.x196)**2) + 1 / sqrt((m.x8 - m.x17)**2 + (m.x98 -
    m.x107)**2 + (m.x188 - m.x197)**2) + 1 / sqrt((m.x8 - m.x18)**2 + (m.x98 -
    m.x108)**2 + (m.x188 - m.x198)**2) + 1 / sqrt((m.x8 - m.x19)**2 + (m.x98 -
    m.x109)**2 + (m.x188 - m.x199)**2) + 1 / sqrt((m.x8 - m.x20)**2 + (m.x98 -
    m.x110)**2 + (m.x188 - m.x200)**2) + 1 / sqrt((m.x8 - m.x21)**2 + (m.x98 -
    m.x111)**2 + (m.x188 - m.x201)**2) + 1 / sqrt((m.x8 - m.x22)**2 + (m.x98 -
    m.x112)**2 + (m.x188 - m.x202)**2) + 1 / sqrt((m.x8 - m.x23)**2 + (m.x98 -
    m.x113)**2 + (m.x188 - m.x203)**2) + 1 / sqrt((m.x8 - m.x24)**2 + (m.x98 -
    m.x114)**2 + (m.x188 - m.x204)**2) + 1 / sqrt((m.x8 - m.x25)**2 + (m.x98 -
    m.x115)**2 + (m.x188 - m.x205)**2) + 1 / sqrt((m.x8 - m.x26)**2 + (m.x98 -
    m.x116)**2 + (m.x188 - m.x206)**2) + 1 / sqrt((m.x8 - m.x27)**2 + (m.x98 -
    m.x117)**2 + (m.x188 - m.x207)**2) + 1 / sqrt((m.x8 - m.x28)**2 + (m.x98 -
    m.x118)**2 + (m.x188 - m.x208)**2) + 1 / sqrt((m.x8 - m.x29)**2 + (m.x98 -
    m.x119)**2 + (m.x188 - m.x209)**2) + 1 / sqrt((m.x8 - m.x30)**2 + (m.x98 -
    m.x120)**2 + (m.x188 - m.x210)**2) + 1 / sqrt((m.x8 - m.x31)**2 + (m.x98 -
    m.x121)**2 + (m.x188 - m.x211)**2) + 1 / sqrt((m.x8 - m.x32)**2 + (m.x98 -
    m.x122)**2 + (m.x188 - m.x212)**2) + 1 / sqrt((m.x8 - m.x33)**2 + (m.x98 -
    m.x123)**2 + (m.x188 - m.x213)**2) + 1 / sqrt((m.x8 - m.x34)**2 + (m.x98 -
    m.x124)**2 + (m.x188 - m.x214)**2) + 1 / sqrt((m.x8 - m.x35)**2 + (m.x98 -
    m.x125)**2 + (m.x188 - m.x215)**2) + 1 / sqrt((m.x8 - m.x36)**2 + (m.x98 -
    m.x126)**2 + (m.x188 - m.x216)**2) + 1 / sqrt((m.x8 - m.x37)**2 + (m.x98 -
    m.x127)**2 + (m.x188 - m.x217)**2) + 1 / sqrt((m.x8 - m.x38)**2 + (m.x98 -
    m.x128)**2 + (m.x188 - m.x218)**2) + 1 / sqrt((m.x8 - m.x39)**2 + (m.x98 -
    m.x129)**2 + (m.x188 - m.x219)**2) + 1 / sqrt((m.x8 - m.x40)**2 + (m.x98 -
    m.x130)**2 + (m.x188 - m.x220)**2) + 1 / sqrt((m.x8 - m.x41)**2 + (m.x98 -
    m.x131)**2 + (m.x188 - m.x221)**2) + 1 / sqrt((m.x8 - m.x42)**2 + (m.x98 -
    m.x132)**2 + (m.x188 - m.x222)**2) + 1 / sqrt((m.x8 - m.x43)**2 + (m.x98 -
    m.x133)**2 + (m.x188 - m.x223)**2) + 1 / sqrt((m.x8 - m.x44)**2 + (m.x98 -
    m.x134)**2 + (m.x188 - m.x224)**2) + 1 / sqrt((m.x8 - m.x45)**2 + (m.x98 -
    m.x135)**2 + (m.x188 - m.x225)**2) + 1 / sqrt((m.x8 - m.x46)**2 + (m.x98 -
    m.x136)**2 + (m.x188 - m.x226)**2) + 1 / sqrt((m.x8 - m.x47)**2 + (m.x98 -
    m.x137)**2 + (m.x188 - m.x227)**2) + 1 / sqrt((m.x8 - m.x48)**2 + (m.x98 -
    m.x138)**2 + (m.x188 - m.x228)**2) + 1 / sqrt((m.x8 - m.x49)**2 + (m.x98 -
    m.x139)**2 + (m.x188 - m.x229)**2) + 1 / sqrt((m.x8 - m.x50)**2 + (m.x98 -
    m.x140)**2 + (m.x188 - m.x230)**2) + 1 / sqrt((m.x8 - m.x51)**2 + (m.x98 -
    m.x141)**2 + (m.x188 - m.x231)**2) + 1 / sqrt((m.x8 - m.x52)**2 + (m.x98 -
    m.x142)**2 + (m.x188 - m.x232)**2) + 1 / sqrt((m.x8 - m.x53)**2 + (m.x98 -
    m.x143)**2 + (m.x188 - m.x233)**2) + 1 / sqrt((m.x8 - m.x54)**2 + (m.x98 -
    m.x144)**2 + (m.x188 - m.x234)**2) + 1 / sqrt((m.x8 - m.x55)**2 + (m.x98 -
    m.x145)**2 + (m.x188 - m.x235)**2) + 1 / sqrt((m.x8 - m.x56)**2 + (m.x98 -
    m.x146)**2 + (m.x188 - m.x236)**2) + 1 / sqrt((m.x8 - m.x57)**2 + (m.x98 -
    m.x147)**2 + (m.x188 - m.x237)**2) + 1 / sqrt((m.x8 - m.x58)**2 + (m.x98 -
    m.x148)**2 + (m.x188 - m.x238)**2) + 1 / sqrt((m.x8 - m.x59)**2 + (m.x98 -
    m.x149)**2 + (m.x188 - m.x239)**2) + 1 / sqrt((m.x8 - m.x60)**2 + (m.x98 -
    m.x150)**2 + (m.x188 - m.x240)**2) + 1 / sqrt((m.x8 - m.x61)**2 + (m.x98 -
    m.x151)**2 + (m.x188 - m.x241)**2) + 1 / sqrt((m.x8 - m.x62)**2 + (m.x98 -
    m.x152)**2 + (m.x188 - m.x242)**2) + 1 / sqrt((m.x8 - m.x63)**2 + (m.x98 -
    m.x153)**2 + (m.x188 - m.x243)**2) + 1 / sqrt((m.x8 - m.x64)**2 + (m.x98 -
    m.x154)**2 + (m.x188 - m.x244)**2) + 1 / sqrt((m.x8 - m.x65)**2 + (m.x98 -
    m.x155)**2 + (m.x188 - m.x245)**2) + 1 / sqrt((m.x8 - m.x66)**2 + (m.x98 -
    m.x156)**2 + (m.x188 - m.x246)**2) + 1 / sqrt((m.x8 - m.x67)**2 + (m.x98 -
    m.x157)**2 + (m.x188 - m.x247)**2) + 1 / sqrt((m.x8 - m.x68)**2 + (m.x98 -
    m.x158)**2 + (m.x188 - m.x248)**2) + 1 / sqrt((m.x8 - m.x69)**2 + (m.x98 -
    m.x159)**2 + (m.x188 - m.x249)**2) + 1 / sqrt((m.x8 - m.x70)**2 + (m.x98 -
    m.x160)**2 + (m.x188 - m.x250)**2) + 1 / sqrt((m.x8 - m.x71)**2 + (m.x98 -
    m.x161)**2 + (m.x188 - m.x251)**2) + 1 / sqrt((m.x8 - m.x72)**2 + (m.x98 -
    m.x162)**2 + (m.x188 - m.x252)**2) + 1 / sqrt((m.x8 - m.x73)**2 + (m.x98 -
    m.x163)**2 + (m.x188 - m.x253)**2) + 1 / sqrt((m.x8 - m.x74)**2 + (m.x98 -
    m.x164)**2 + (m.x188 - m.x254)**2) + 1 / sqrt((m.x8 - m.x75)**2 + (m.x98 -
    m.x165)**2 + (m.x188 - m.x255)**2) + 1 / sqrt((m.x8 - m.x76)**2 + (m.x98 -
    m.x166)**2 + (m.x188 - m.x256)**2) + 1 / sqrt((m.x8 - m.x77)**2 + (m.x98 -
    m.x167)**2 + (m.x188 - m.x257)**2) + 1 / sqrt((m.x8 - m.x78)**2 + (m.x98 -
    m.x168)**2 + (m.x188 - m.x258)**2) + 1 / sqrt((m.x8 - m.x79)**2 + (m.x98 -
    m.x169)**2 + (m.x188 - m.x259)**2) + 1 / sqrt((m.x8 - m.x80)**2 + (m.x98 -
    m.x170)**2 + (m.x188 - m.x260)**2) + 1 / sqrt((m.x8 - m.x81)**2 + (m.x98 -
    m.x171)**2 + (m.x188 - m.x261)**2) + 1 / sqrt((m.x8 - m.x82)**2 + (m.x98 -
    m.x172)**2 + (m.x188 - m.x262)**2) + 1 / sqrt((m.x8 - m.x83)**2 + (m.x98 -
    m.x173)**2 + (m.x188 - m.x263)**2) + 1 / sqrt((m.x8 - m.x84)**2 + (m.x98 -
    m.x174)**2 + (m.x188 - m.x264)**2) + 1 / sqrt((m.x8 - m.x85)**2 + (m.x98 -
    m.x175)**2 + (m.x188 - m.x265)**2) + 1 / sqrt((m.x8 - m.x86)**2 + (m.x98 -
    m.x176)**2 + (m.x188 - m.x266)**2) + 1 / sqrt((m.x8 - m.x87)**2 + (m.x98 -
    m.x177)**2 + (m.x188 - m.x267)**2) + 1 / sqrt((m.x8 - m.x88)**2 + (m.x98 -
    m.x178)**2 + (m.x188 - m.x268)**2) + 1 / sqrt((m.x8 - m.x89)**2 + (m.x98 -
    m.x179)**2 + (m.x188 - m.x269)**2) + 1 / sqrt((m.x8 - m.x90)**2 + (m.x98 -
    m.x180)**2 + (m.x188 - m.x270)**2) + 1 / sqrt((m.x9 - m.x10)**2 + (m.x99 -
    m.x100)**2 + (m.x189 - m.x190)**2) + 1 / sqrt((m.x9 - m.x11)**2 + (m.x99 -
    m.x101)**2 + (m.x189 - m.x191)**2) + 1 / sqrt((m.x9 - m.x12)**2 + (m.x99 -
    m.x102)**2 + (m.x189 - m.x192)**2) + 1 / sqrt((m.x9 - m.x13)**2 + (m.x99 -
    m.x103)**2 + (m.x189 - m.x193)**2) + 1 / sqrt((m.x9 - m.x14)**2 + (m.x99 -
    m.x104)**2 + (m.x189 - m.x194)**2) + 1 / sqrt((m.x9 - m.x15)**2 + (m.x99 -
    m.x105)**2 + (m.x189 - m.x195)**2) + 1 / sqrt((m.x9 - m.x16)**2 + (m.x99 -
    m.x106)**2 + (m.x189 - m.x196)**2) + 1 / sqrt((m.x9 - m.x17)**2 + (m.x99 -
    m.x107)**2 + (m.x189 - m.x197)**2) + 1 / sqrt((m.x9 - m.x18)**2 + (m.x99 -
    m.x108)**2 + (m.x189 - m.x198)**2) + 1 / sqrt((m.x9 - m.x19)**2 + (m.x99 -
    m.x109)**2 + (m.x189 - m.x199)**2) + 1 / sqrt((m.x9 - m.x20)**2 + (m.x99 -
    m.x110)**2 + (m.x189 - m.x200)**2) + 1 / sqrt((m.x9 - m.x21)**2 + (m.x99 -
    m.x111)**2 + (m.x189 - m.x201)**2) + 1 / sqrt((m.x9 - m.x22)**2 + (m.x99 -
    m.x112)**2 + (m.x189 - m.x202)**2) + 1 / sqrt((m.x9 - m.x23)**2 + (m.x99 -
    m.x113)**2 + (m.x189 - m.x203)**2) + 1 / sqrt((m.x9 - m.x24)**2 + (m.x99 -
    m.x114)**2 + (m.x189 - m.x204)**2) + 1 / sqrt((m.x9 - m.x25)**2 + (m.x99 -
    m.x115)**2 + (m.x189 - m.x205)**2) + 1 / sqrt((m.x9 - m.x26)**2 + (m.x99 -
    m.x116)**2 + (m.x189 - m.x206)**2) + 1 / sqrt((m.x9 - m.x27)**2 + (m.x99 -
    m.x117)**2 + (m.x189 - m.x207)**2) + 1 / sqrt((m.x9 - m.x28)**2 + (m.x99 -
    m.x118)**2 + (m.x189 - m.x208)**2) + 1 / sqrt((m.x9 - m.x29)**2 + (m.x99 -
    m.x119)**2 + (m.x189 - m.x209)**2) + 1 / sqrt((m.x9 - m.x30)**2 + (m.x99 -
    m.x120)**2 + (m.x189 - m.x210)**2) + 1 / sqrt((m.x9 - m.x31)**2 + (m.x99 -
    m.x121)**2 + (m.x189 - m.x211)**2) + 1 / sqrt((m.x9 - m.x32)**2 + (m.x99 -
    m.x122)**2 + (m.x189 - m.x212)**2) + 1 / sqrt((m.x9 - m.x33)**2 + (m.x99 -
    m.x123)**2 + (m.x189 - m.x213)**2) + 1 / sqrt((m.x9 - m.x34)**2 + (m.x99 -
    m.x124)**2 + (m.x189 - m.x214)**2) + 1 / sqrt((m.x9 - m.x35)**2 + (m.x99 -
    m.x125)**2 + (m.x189 - m.x215)**2) + 1 / sqrt((m.x9 - m.x36)**2 + (m.x99 -
    m.x126)**2 + (m.x189 - m.x216)**2) + 1 / sqrt((m.x9 - m.x37)**2 + (m.x99 -
    m.x127)**2 + (m.x189 - m.x217)**2) + 1 / sqrt((m.x9 - m.x38)**2 + (m.x99 -
    m.x128)**2 + (m.x189 - m.x218)**2) + 1 / sqrt((m.x9 - m.x39)**2 + (m.x99 -
    m.x129)**2 + (m.x189 - m.x219)**2) + 1 / sqrt((m.x9 - m.x40)**2 + (m.x99 -
    m.x130)**2 + (m.x189 - m.x220)**2) + 1 / sqrt((m.x9 - m.x41)**2 + (m.x99 -
    m.x131)**2 + (m.x189 - m.x221)**2) + 1 / sqrt((m.x9 - m.x42)**2 + (m.x99 -
    m.x132)**2 + (m.x189 - m.x222)**2) + 1 / sqrt((m.x9 - m.x43)**2 + (m.x99 -
    m.x133)**2 + (m.x189 - m.x223)**2) + 1 / sqrt((m.x9 - m.x44)**2 + (m.x99 -
    m.x134)**2 + (m.x189 - m.x224)**2) + 1 / sqrt((m.x9 - m.x45)**2 + (m.x99 -
    m.x135)**2 + (m.x189 - m.x225)**2) + 1 / sqrt((m.x9 - m.x46)**2 + (m.x99 -
    m.x136)**2 + (m.x189 - m.x226)**2) + 1 / sqrt((m.x9 - m.x47)**2 + (m.x99 -
    m.x137)**2 + (m.x189 - m.x227)**2) + 1 / sqrt((m.x9 - m.x48)**2 + (m.x99 -
    m.x138)**2 + (m.x189 - m.x228)**2) + 1 / sqrt((m.x9 - m.x49)**2 + (m.x99 -
    m.x139)**2 + (m.x189 - m.x229)**2) + 1 / sqrt((m.x9 - m.x50)**2 + (m.x99 -
    m.x140)**2 + (m.x189 - m.x230)**2) + 1 / sqrt((m.x9 - m.x51)**2 + (m.x99 -
    m.x141)**2 + (m.x189 - m.x231)**2) + 1 / sqrt((m.x9 - m.x52)**2 + (m.x99 -
    m.x142)**2 + (m.x189 - m.x232)**2) + 1 / sqrt((m.x9 - m.x53)**2 + (m.x99 -
    m.x143)**2 + (m.x189 - m.x233)**2) + 1 / sqrt((m.x9 - m.x54)**2 + (m.x99 -
    m.x144)**2 + (m.x189 - m.x234)**2) + 1 / sqrt((m.x9 - m.x55)**2 + (m.x99 -
    m.x145)**2 + (m.x189 - m.x235)**2) + 1 / sqrt((m.x9 - m.x56)**2 + (m.x99 -
    m.x146)**2 + (m.x189 - m.x236)**2) + 1 / sqrt((m.x9 - m.x57)**2 + (m.x99 -
    m.x147)**2 + (m.x189 - m.x237)**2) + 1 / sqrt((m.x9 - m.x58)**2 + (m.x99 -
    m.x148)**2 + (m.x189 - m.x238)**2) + 1 / sqrt((m.x9 - m.x59)**2 + (m.x99 -
    m.x149)**2 + (m.x189 - m.x239)**2) + 1 / sqrt((m.x9 - m.x60)**2 + (m.x99 -
    m.x150)**2 + (m.x189 - m.x240)**2) + 1 / sqrt((m.x9 - m.x61)**2 + (m.x99 -
    m.x151)**2 + (m.x189 - m.x241)**2) + 1 / sqrt((m.x9 - m.x62)**2 + (m.x99 -
    m.x152)**2 + (m.x189 - m.x242)**2) + 1 / sqrt((m.x9 - m.x63)**2 + (m.x99 -
    m.x153)**2 + (m.x189 - m.x243)**2) + 1 / sqrt((m.x9 - m.x64)**2 + (m.x99 -
    m.x154)**2 + (m.x189 - m.x244)**2) + 1 / sqrt((m.x9 - m.x65)**2 + (m.x99 -
    m.x155)**2 + (m.x189 - m.x245)**2) + 1 / sqrt((m.x9 - m.x66)**2 + (m.x99 -
    m.x156)**2 + (m.x189 - m.x246)**2) + 1 / sqrt((m.x9 - m.x67)**2 + (m.x99 -
    m.x157)**2 + (m.x189 - m.x247)**2) + 1 / sqrt((m.x9 - m.x68)**2 + (m.x99 -
    m.x158)**2 + (m.x189 - m.x248)**2) + 1 / sqrt((m.x9 - m.x69)**2 + (m.x99 -
    m.x159)**2 + (m.x189 - m.x249)**2) + 1 / sqrt((m.x9 - m.x70)**2 + (m.x99 -
    m.x160)**2 + (m.x189 - m.x250)**2) + 1 / sqrt((m.x9 - m.x71)**2 + (m.x99 -
    m.x161)**2 + (m.x189 - m.x251)**2) + 1 / sqrt((m.x9 - m.x72)**2 + (m.x99 -
    m.x162)**2 + (m.x189 - m.x252)**2) + 1 / sqrt((m.x9 - m.x73)**2 + (m.x99 -
    m.x163)**2 + (m.x189 - m.x253)**2) + 1 / sqrt((m.x9 - m.x74)**2 + (m.x99 -
    m.x164)**2 + (m.x189 - m.x254)**2) + 1 / sqrt((m.x9 - m.x75)**2 + (m.x99 -
    m.x165)**2 + (m.x189 - m.x255)**2) + 1 / sqrt((m.x9 - m.x76)**2 + (m.x99 -
    m.x166)**2 + (m.x189 - m.x256)**2) + 1 / sqrt((m.x9 - m.x77)**2 + (m.x99 -
    m.x167)**2 + (m.x189 - m.x257)**2) + 1 / sqrt((m.x9 - m.x78)**2 + (m.x99 -
    m.x168)**2 + (m.x189 - m.x258)**2) + 1 / sqrt((m.x9 - m.x79)**2 + (m.x99 -
    m.x169)**2 + (m.x189 - m.x259)**2) + 1 / sqrt((m.x9 - m.x80)**2 + (m.x99 -
    m.x170)**2 + (m.x189 - m.x260)**2) + 1 / sqrt((m.x9 - m.x81)**2 + (m.x99 -
    m.x171)**2 + (m.x189 - m.x261)**2) + 1 / sqrt((m.x9 - m.x82)**2 + (m.x99 -
    m.x172)**2 + (m.x189 - m.x262)**2) + 1 / sqrt((m.x9 - m.x83)**2 + (m.x99 -
    m.x173)**2 + (m.x189 - m.x263)**2) + 1 / sqrt((m.x9 - m.x84)**2 + (m.x99 -
    m.x174)**2 + (m.x189 - m.x264)**2) + 1 / sqrt((m.x9 - m.x85)**2 + (m.x99 -
    m.x175)**2 + (m.x189 - m.x265)**2) + 1 / sqrt((m.x9 - m.x86)**2 + (m.x99 -
    m.x176)**2 + (m.x189 - m.x266)**2) + 1 / sqrt((m.x9 - m.x87)**2 + (m.x99 -
    m.x177)**2 + (m.x189 - m.x267)**2) + 1 / sqrt((m.x9 - m.x88)**2 + (m.x99 -
    m.x178)**2 + (m.x189 - m.x268)**2) + 1 / sqrt((m.x9 - m.x89)**2 + (m.x99 -
    m.x179)**2 + (m.x189 - m.x269)**2) + 1 / sqrt((m.x9 - m.x90)**2 + (m.x99 -
    m.x180)**2 + (m.x189 - m.x270)**2) + 1 / sqrt((m.x10 - m.x11)**2 + (m.x100
    - m.x101)**2 + (m.x190 - m.x191)**2) + 1 / sqrt((m.x10 - m.x12)**2 + (
    m.x100 - m.x102)**2 + (m.x190 - m.x192)**2) + 1 / sqrt((m.x10 - m.x13)**2
    + (m.x100 - m.x103)**2 + (m.x190 - m.x193)**2) + 1 / sqrt((m.x10 - m.x14)
    **2 + (m.x100 - m.x104)**2 + (m.x190 - m.x194)**2) + 1 / sqrt((m.x10 -
    m.x15)**2 + (m.x100 - m.x105)**2 + (m.x190 - m.x195)**2) + 1 / sqrt((m.x10
    - m.x16)**2 + (m.x100 - m.x106)**2 + (m.x190 - m.x196)**2) + 1 / sqrt((
    m.x10 - m.x17)**2 + (m.x100 - m.x107)**2 + (m.x190 - m.x197)**2) + 1 /
    sqrt((m.x10 - m.x18)**2 + (m.x100 - m.x108)**2 + (m.x190 - m.x198)**2) + 1
    / sqrt((m.x10 - m.x19)**2 + (m.x100 - m.x109)**2 + (m.x190 - m.x199)**2)
    + 1 / sqrt((m.x10 - m.x20)**2 + (m.x100 - m.x110)**2 + (m.x190 - m.x200)**
    2) + 1 / sqrt((m.x10 - m.x21)**2 + (m.x100 - m.x111)**2 + (m.x190 - m.x201)
    **2) + 1 / sqrt((m.x10 - m.x22)**2 + (m.x100 - m.x112)**2 + (m.x190 -
    m.x202)**2) + 1 / sqrt((m.x10 - m.x23)**2 + (m.x100 - m.x113)**2 + (m.x190
    - m.x203)**2) + 1 / sqrt((m.x10 - m.x24)**2 + (m.x100 - m.x114)**2 + (
    m.x190 - m.x204)**2) + 1 / sqrt((m.x10 - m.x25)**2 + (m.x100 - m.x115)**2
    + (m.x190 - m.x205)**2) + 1 / sqrt((m.x10 - m.x26)**2 + (m.x100 - m.x116)
    **2 + (m.x190 - m.x206)**2) + 1 / sqrt((m.x10 - m.x27)**2 + (m.x100 -
    m.x117)**2 + (m.x190 - m.x207)**2) + 1 / sqrt((m.x10 - m.x28)**2 + (m.x100
    - m.x118)**2 + (m.x190 - m.x208)**2) + 1 / sqrt((m.x10 - m.x29)**2 + (
    m.x100 - m.x119)**2 + (m.x190 - m.x209)**2) + 1 / sqrt((m.x10 - m.x30)**2
    + (m.x100 - m.x120)**2 + (m.x190 - m.x210)**2) + 1 / sqrt((m.x10 - m.x31)
    **2 + (m.x100 - m.x121)**2 + (m.x190 - m.x211)**2) + 1 / sqrt((m.x10 -
    m.x32)**2 + (m.x100 - m.x122)**2 + (m.x190 - m.x212)**2) + 1 / sqrt((m.x10
    - m.x33)**2 + (m.x100 - m.x123)**2 + (m.x190 - m.x213)**2) + 1 / sqrt((
    m.x10 - m.x34)**2 + (m.x100 - m.x124)**2 + (m.x190 - m.x214)**2) + 1 /
    sqrt((m.x10 - m.x35)**2 + (m.x100 - m.x125)**2 + (m.x190 - m.x215)**2) + 1
    / sqrt((m.x10 - m.x36)**2 + (m.x100 - m.x126)**2 + (m.x190 - m.x216)**2)
    + 1 / sqrt((m.x10 - m.x37)**2 + (m.x100 - m.x127)**2 + (m.x190 - m.x217)**
    2) + 1 / sqrt((m.x10 - m.x38)**2 + (m.x100 - m.x128)**2 + (m.x190 - m.x218)
    **2) + 1 / sqrt((m.x10 - m.x39)**2 + (m.x100 - m.x129)**2 + (m.x190 -
    m.x219)**2) + 1 / sqrt((m.x10 - m.x40)**2 + (m.x100 - m.x130)**2 + (m.x190
    - m.x220)**2) + 1 / sqrt((m.x10 - m.x41)**2 + (m.x100 - m.x131)**2 + (
    m.x190 - m.x221)**2) + 1 / sqrt((m.x10 - m.x42)**2 + (m.x100 - m.x132)**2
    + (m.x190 - m.x222)**2) + 1 / sqrt((m.x10 - m.x43)**2 + (m.x100 - m.x133)
    **2 + (m.x190 - m.x223)**2) + 1 / sqrt((m.x10 - m.x44)**2 + (m.x100 -
    m.x134)**2 + (m.x190 - m.x224)**2) + 1 / sqrt((m.x10 - m.x45)**2 + (m.x100
    - m.x135)**2 + (m.x190 - m.x225)**2) + 1 / sqrt((m.x10 - m.x46)**2 + (
    m.x100 - m.x136)**2 + (m.x190 - m.x226)**2) + 1 / sqrt((m.x10 - m.x47)**2
    + (m.x100 - m.x137)**2 + (m.x190 - m.x227)**2) + 1 / sqrt((m.x10 - m.x48)
    **2 + (m.x100 - m.x138)**2 + (m.x190 - m.x228)**2) + 1 / sqrt((m.x10 -
    m.x49)**2 + (m.x100 - m.x139)**2 + (m.x190 - m.x229)**2) + 1 / sqrt((m.x10
    - m.x50)**2 + (m.x100 - m.x140)**2 + (m.x190 - m.x230)**2) + 1 / sqrt((
    m.x10 - m.x51)**2 + (m.x100 - m.x141)**2 + (m.x190 - m.x231)**2) + 1 /
    sqrt((m.x10 - m.x52)**2 + (m.x100 - m.x142)**2 + (m.x190 - m.x232)**2) + 1
    / sqrt((m.x10 - m.x53)**2 + (m.x100 - m.x143)**2 + (m.x190 - m.x233)**2)
    + 1 / sqrt((m.x10 - m.x54)**2 + (m.x100 - m.x144)**2 + (m.x190 - m.x234)**
    2) + 1 / sqrt((m.x10 - m.x55)**2 + (m.x100 - m.x145)**2 + (m.x190 - m.x235)
    **2) + 1 / sqrt((m.x10 - m.x56)**2 + (m.x100 - m.x146)**2 + (m.x190 -
    m.x236)**2) + 1 / sqrt((m.x10 - m.x57)**2 + (m.x100 - m.x147)**2 + (m.x190
    - m.x237)**2) + 1 / sqrt((m.x10 - m.x58)**2 + (m.x100 - m.x148)**2 + (
    m.x190 - m.x238)**2) + 1 / sqrt((m.x10 - m.x59)**2 + (m.x100 - m.x149)**2
    + (m.x190 - m.x239)**2) + 1 / sqrt((m.x10 - m.x60)**2 + (m.x100 - m.x150)
    **2 + (m.x190 - m.x240)**2) + 1 / sqrt((m.x10 - m.x61)**2 + (m.x100 -
    m.x151)**2 + (m.x190 - m.x241)**2) + 1 / sqrt((m.x10 - m.x62)**2 + (m.x100
    - m.x152)**2 + (m.x190 - m.x242)**2) + 1 / sqrt((m.x10 - m.x63)**2 + (
    m.x100 - m.x153)**2 + (m.x190 - m.x243)**2) + 1 / sqrt((m.x10 - m.x64)**2
    + (m.x100 - m.x154)**2 + (m.x190 - m.x244)**2) + 1 / sqrt((m.x10 - m.x65)
    **2 + (m.x100 - m.x155)**2 + (m.x190 - m.x245)**2) + 1 / sqrt((m.x10 -
    m.x66)**2 + (m.x100 - m.x156)**2 + (m.x190 - m.x246)**2) + 1 / sqrt((m.x10
    - m.x67)**2 + (m.x100 - m.x157)**2 + (m.x190 - m.x247)**2) + 1 / sqrt((
    m.x10 - m.x68)**2 + (m.x100 - m.x158)**2 + (m.x190 - m.x248)**2) + 1 /
    sqrt((m.x10 - m.x69)**2 + (m.x100 - m.x159)**2 + (m.x190 - m.x249)**2) + 1
    / sqrt((m.x10 - m.x70)**2 + (m.x100 - m.x160)**2 + (m.x190 - m.x250)**2)
    + 1 / sqrt((m.x10 - m.x71)**2 + (m.x100 - m.x161)**2 + (m.x190 - m.x251)**
    2) + 1 / sqrt((m.x10 - m.x72)**2 + (m.x100 - m.x162)**2 + (m.x190 - m.x252)
    **2) + 1 / sqrt((m.x10 - m.x73)**2 + (m.x100 - m.x163)**2 + (m.x190 -
    m.x253)**2) + 1 / sqrt((m.x10 - m.x74)**2 + (m.x100 - m.x164)**2 + (m.x190
    - m.x254)**2) + 1 / sqrt((m.x10 - m.x75)**2 + (m.x100 - m.x165)**2 + (
    m.x190 - m.x255)**2) + 1 / sqrt((m.x10 - m.x76)**2 + (m.x100 - m.x166)**2
    + (m.x190 - m.x256)**2) + 1 / sqrt((m.x10 - m.x77)**2 + (m.x100 - m.x167)
    **2 + (m.x190 - m.x257)**2) + 1 / sqrt((m.x10 - m.x78)**2 + (m.x100 -
    m.x168)**2 + (m.x190 - m.x258)**2) + 1 / sqrt((m.x10 - m.x79)**2 + (m.x100
    - m.x169)**2 + (m.x190 - m.x259)**2) + 1 / sqrt((m.x10 - m.x80)**2 + (
    m.x100 - m.x170)**2 + (m.x190 - m.x260)**2) + 1 / sqrt((m.x10 - m.x81)**2
    + (m.x100 - m.x171)**2 + (m.x190 - m.x261)**2) + 1 / sqrt((m.x10 - m.x82)
    **2 + (m.x100 - m.x172)**2 + (m.x190 - m.x262)**2) + 1 / sqrt((m.x10 -
    m.x83)**2 + (m.x100 - m.x173)**2 + (m.x190 - m.x263)**2) + 1 / sqrt((m.x10
    - m.x84)**2 + (m.x100 - m.x174)**2 + (m.x190 - m.x264)**2) + 1 / sqrt((
    m.x10 - m.x85)**2 + (m.x100 - m.x175)**2 + (m.x190 - m.x265)**2) + 1 /
    sqrt((m.x10 - m.x86)**2 + (m.x100 - m.x176)**2 + (m.x190 - m.x266)**2) + 1
    / sqrt((m.x10 - m.x87)**2 + (m.x100 - m.x177)**2 + (m.x190 - m.x267)**2)
    + 1 / sqrt((m.x10 - m.x88)**2 + (m.x100 - m.x178)**2 + (m.x190 - m.x268)**
    2) + 1 / sqrt((m.x10 - m.x89)**2 + (m.x100 - m.x179)**2 + (m.x190 - m.x269)
    **2) + 1 / sqrt((m.x10 - m.x90)**2 + (m.x100 - m.x180)**2 + (m.x190 -
    m.x270)**2) + 1 / sqrt((m.x11 - m.x12)**2 + (m.x101 - m.x102)**2 + (m.x191
    - m.x192)**2) + 1 / sqrt((m.x11 - m.x13)**2 + (m.x101 - m.x103)**2 + (
    m.x191 - m.x193)**2) + 1 / sqrt((m.x11 - m.x14)**2 + (m.x101 - m.x104)**2
    + (m.x191 - m.x194)**2) + 1 / sqrt((m.x11 - m.x15)**2 + (m.x101 - m.x105)
    **2 + (m.x191 - m.x195)**2) + 1 / sqrt((m.x11 - m.x16)**2 + (m.x101 -
    m.x106)**2 + (m.x191 - m.x196)**2) + 1 / sqrt((m.x11 - m.x17)**2 + (m.x101
    - m.x107)**2 + (m.x191 - m.x197)**2) + 1 / sqrt((m.x11 - m.x18)**2 + (
    m.x101 - m.x108)**2 + (m.x191 - m.x198)**2) + 1 / sqrt((m.x11 - m.x19)**2
    + (m.x101 - m.x109)**2 + (m.x191 - m.x199)**2) + 1 / sqrt((m.x11 - m.x20)
    **2 + (m.x101 - m.x110)**2 + (m.x191 - m.x200)**2) + 1 / sqrt((m.x11 -
    m.x21)**2 + (m.x101 - m.x111)**2 + (m.x191 - m.x201)**2) + 1 / sqrt((m.x11
    - m.x22)**2 + (m.x101 - m.x112)**2 + (m.x191 - m.x202)**2) + 1 / sqrt((
    m.x11 - m.x23)**2 + (m.x101 - m.x113)**2 + (m.x191 - m.x203)**2) + 1 /
    sqrt((m.x11 - m.x24)**2 + (m.x101 - m.x114)**2 + (m.x191 - m.x204)**2) + 1
    / sqrt((m.x11 - m.x25)**2 + (m.x101 - m.x115)**2 + (m.x191 - m.x205)**2)
    + 1 / sqrt((m.x11 - m.x26)**2 + (m.x101 - m.x116)**2 + (m.x191 - m.x206)**
    2) + 1 / sqrt((m.x11 - m.x27)**2 + (m.x101 - m.x117)**2 + (m.x191 - m.x207)
    **2) + 1 / sqrt((m.x11 - m.x28)**2 + (m.x101 - m.x118)**2 + (m.x191 -
    m.x208)**2) + 1 / sqrt((m.x11 - m.x29)**2 + (m.x101 - m.x119)**2 + (m.x191
    - m.x209)**2) + 1 / sqrt((m.x11 - m.x30)**2 + (m.x101 - m.x120)**2 + (
    m.x191 - m.x210)**2) + 1 / sqrt((m.x11 - m.x31)**2 + (m.x101 - m.x121)**2
    + (m.x191 - m.x211)**2) + 1 / sqrt((m.x11 - m.x32)**2 + (m.x101 - m.x122)
    **2 + (m.x191 - m.x212)**2) + 1 / sqrt((m.x11 - m.x33)**2 + (m.x101 -
    m.x123)**2 + (m.x191 - m.x213)**2) + 1 / sqrt((m.x11 - m.x34)**2 + (m.x101
    - m.x124)**2 + (m.x191 - m.x214)**2) + 1 / sqrt((m.x11 - m.x35)**2 + (
    m.x101 - m.x125)**2 + (m.x191 - m.x215)**2) + 1 / sqrt((m.x11 - m.x36)**2
    + (m.x101 - m.x126)**2 + (m.x191 - m.x216)**2) + 1 / sqrt((m.x11 - m.x37)
    **2 + (m.x101 - m.x127)**2 + (m.x191 - m.x217)**2) + 1 / sqrt((m.x11 -
    m.x38)**2 + (m.x101 - m.x128)**2 + (m.x191 - m.x218)**2) + 1 / sqrt((m.x11
    - m.x39)**2 + (m.x101 - m.x129)**2 + (m.x191 - m.x219)**2) + 1 / sqrt((
    m.x11 - m.x40)**2 + (m.x101 - m.x130)**2 + (m.x191 - m.x220)**2) + 1 /
    sqrt((m.x11 - m.x41)**2 + (m.x101 - m.x131)**2 + (m.x191 - m.x221)**2) + 1
    / sqrt((m.x11 - m.x42)**2 + (m.x101 - m.x132)**2 + (m.x191 - m.x222)**2)
    + 1 / sqrt((m.x11 - m.x43)**2 + (m.x101 - m.x133)**2 + (m.x191 - m.x223)**
    2) + 1 / sqrt((m.x11 - m.x44)**2 + (m.x101 - m.x134)**2 + (m.x191 - m.x224)
    **2) + 1 / sqrt((m.x11 - m.x45)**2 + (m.x101 - m.x135)**2 + (m.x191 -
    m.x225)**2) + 1 / sqrt((m.x11 - m.x46)**2 + (m.x101 - m.x136)**2 + (m.x191
    - m.x226)**2) + 1 / sqrt((m.x11 - m.x47)**2 + (m.x101 - m.x137)**2 + (
    m.x191 - m.x227)**2) + 1 / sqrt((m.x11 - m.x48)**2 + (m.x101 - m.x138)**2
    + (m.x191 - m.x228)**2) + 1 / sqrt((m.x11 - m.x49)**2 + (m.x101 - m.x139)
    **2 + (m.x191 - m.x229)**2) + 1 / sqrt((m.x11 - m.x50)**2 + (m.x101 -
    m.x140)**2 + (m.x191 - m.x230)**2) + 1 / sqrt((m.x11 - m.x51)**2 + (m.x101
    - m.x141)**2 + (m.x191 - m.x231)**2) + 1 / sqrt((m.x11 - m.x52)**2 + (
    m.x101 - m.x142)**2 + (m.x191 - m.x232)**2) + 1 / sqrt((m.x11 - m.x53)**2
    + (m.x101 - m.x143)**2 + (m.x191 - m.x233)**2) + 1 / sqrt((m.x11 - m.x54)
    **2 + (m.x101 - m.x144)**2 + (m.x191 - m.x234)**2) + 1 / sqrt((m.x11 -
    m.x55)**2 + (m.x101 - m.x145)**2 + (m.x191 - m.x235)**2) + 1 / sqrt((m.x11
    - m.x56)**2 + (m.x101 - m.x146)**2 + (m.x191 - m.x236)**2) + 1 / sqrt((
    m.x11 - m.x57)**2 + (m.x101 - m.x147)**2 + (m.x191 - m.x237)**2) + 1 /
    sqrt((m.x11 - m.x58)**2 + (m.x101 - m.x148)**2 + (m.x191 - m.x238)**2) + 1
    / sqrt((m.x11 - m.x59)**2 + (m.x101 - m.x149)**2 + (m.x191 - m.x239)**2)
    + 1 / sqrt((m.x11 - m.x60)**2 + (m.x101 - m.x150)**2 + (m.x191 - m.x240)**
    2) + 1 / sqrt((m.x11 - m.x61)**2 + (m.x101 - m.x151)**2 + (m.x191 - m.x241)
    **2) + 1 / sqrt((m.x11 - m.x62)**2 + (m.x101 - m.x152)**2 + (m.x191 -
    m.x242)**2) + 1 / sqrt((m.x11 - m.x63)**2 + (m.x101 - m.x153)**2 + (m.x191
    - m.x243)**2) + 1 / sqrt((m.x11 - m.x64)**2 + (m.x101 - m.x154)**2 + (
    m.x191 - m.x244)**2) + 1 / sqrt((m.x11 - m.x65)**2 + (m.x101 - m.x155)**2
    + (m.x191 - m.x245)**2) + 1 / sqrt((m.x11 - m.x66)**2 + (m.x101 - m.x156)
    **2 + (m.x191 - m.x246)**2) + 1 / sqrt((m.x11 - m.x67)**2 + (m.x101 -
    m.x157)**2 + (m.x191 - m.x247)**2) + 1 / sqrt((m.x11 - m.x68)**2 + (m.x101
    - m.x158)**2 + (m.x191 - m.x248)**2) + 1 / sqrt((m.x11 - m.x69)**2 + (
    m.x101 - m.x159)**2 + (m.x191 - m.x249)**2) + 1 / sqrt((m.x11 - m.x70)**2
    + (m.x101 - m.x160)**2 + (m.x191 - m.x250)**2) + 1 / sqrt((m.x11 - m.x71)
    **2 + (m.x101 - m.x161)**2 + (m.x191 - m.x251)**2) + 1 / sqrt((m.x11 -
    m.x72)**2 + (m.x101 - m.x162)**2 + (m.x191 - m.x252)**2) + 1 / sqrt((m.x11
    - m.x73)**2 + (m.x101 - m.x163)**2 + (m.x191 - m.x253)**2) + 1 / sqrt((
    m.x11 - m.x74)**2 + (m.x101 - m.x164)**2 + (m.x191 - m.x254)**2) + 1 /
    sqrt((m.x11 - m.x75)**2 + (m.x101 - m.x165)**2 + (m.x191 - m.x255)**2) + 1
    / sqrt((m.x11 - m.x76)**2 + (m.x101 - m.x166)**2 + (m.x191 - m.x256)**2)
    + 1 / sqrt((m.x11 - m.x77)**2 + (m.x101 - m.x167)**2 + (m.x191 - m.x257)**
    2) + 1 / sqrt((m.x11 - m.x78)**2 + (m.x101 - m.x168)**2 + (m.x191 - m.x258)
    **2) + 1 / sqrt((m.x11 - m.x79)**2 + (m.x101 - m.x169)**2 + (m.x191 -
    m.x259)**2) + 1 / sqrt((m.x11 - m.x80)**2 + (m.x101 - m.x170)**2 + (m.x191
    - m.x260)**2) + 1 / sqrt((m.x11 - m.x81)**2 + (m.x101 - m.x171)**2 + (
    m.x191 - m.x261)**2) + 1 / sqrt((m.x11 - m.x82)**2 + (m.x101 - m.x172)**2
    + (m.x191 - m.x262)**2) + 1 / sqrt((m.x11 - m.x83)**2 + (m.x101 - m.x173)
    **2 + (m.x191 - m.x263)**2) + 1 / sqrt((m.x11 - m.x84)**2 + (m.x101 -
    m.x174)**2 + (m.x191 - m.x264)**2) + 1 / sqrt((m.x11 - m.x85)**2 + (m.x101
    - m.x175)**2 + (m.x191 - m.x265)**2) + 1 / sqrt((m.x11 - m.x86)**2 + (
    m.x101 - m.x176)**2 + (m.x191 - m.x266)**2) + 1 / sqrt((m.x11 - m.x87)**2
    + (m.x101 - m.x177)**2 + (m.x191 - m.x267)**2) + 1 / sqrt((m.x11 - m.x88)
    **2 + (m.x101 - m.x178)**2 + (m.x191 - m.x268)**2) + 1 / sqrt((m.x11 -
    m.x89)**2 + (m.x101 - m.x179)**2 + (m.x191 - m.x269)**2) + 1 / sqrt((m.x11
    - m.x90)**2 + (m.x101 - m.x180)**2 + (m.x191 - m.x270)**2) + 1 / sqrt((
    m.x12 - m.x13)**2 + (m.x102 - m.x103)**2 + (m.x192 - m.x193)**2) + 1 /
    sqrt((m.x12 - m.x14)**2 + (m.x102 - m.x104)**2 + (m.x192 - m.x194)**2) + 1
    / sqrt((m.x12 - m.x15)**2 + (m.x102 - m.x105)**2 + (m.x192 - m.x195)**2)
    + 1 / sqrt((m.x12 - m.x16)**2 + (m.x102 - m.x106)**2 + (m.x192 - m.x196)**
    2) + 1 / sqrt((m.x12 - m.x17)**2 + (m.x102 - m.x107)**2 + (m.x192 - m.x197)
    **2) + 1 / sqrt((m.x12 - m.x18)**2 + (m.x102 - m.x108)**2 + (m.x192 -
    m.x198)**2) + 1 / sqrt((m.x12 - m.x19)**2 + (m.x102 - m.x109)**2 + (m.x192
    - m.x199)**2) + 1 / sqrt((m.x12 - m.x20)**2 + (m.x102 - m.x110)**2 + (
    m.x192 - m.x200)**2) + 1 / sqrt((m.x12 - m.x21)**2 + (m.x102 - m.x111)**2
    + (m.x192 - m.x201)**2) + 1 / sqrt((m.x12 - m.x22)**2 + (m.x102 - m.x112)
    **2 + (m.x192 - m.x202)**2) + 1 / sqrt((m.x12 - m.x23)**2 + (m.x102 -
    m.x113)**2 + (m.x192 - m.x203)**2) + 1 / sqrt((m.x12 - m.x24)**2 + (m.x102
    - m.x114)**2 + (m.x192 - m.x204)**2) + 1 / sqrt((m.x12 - m.x25)**2 + (
    m.x102 - m.x115)**2 + (m.x192 - m.x205)**2) + 1 / sqrt((m.x12 - m.x26)**2
    + (m.x102 - m.x116)**2 + (m.x192 - m.x206)**2) + 1 / sqrt((m.x12 - m.x27)
    **2 + (m.x102 - m.x117)**2 + (m.x192 - m.x207)**2) + 1 / sqrt((m.x12 -
    m.x28)**2 + (m.x102 - m.x118)**2 + (m.x192 - m.x208)**2) + 1 / sqrt((m.x12
    - m.x29)**2 + (m.x102 - m.x119)**2 + (m.x192 - m.x209)**2) + 1 / sqrt((
    m.x12 - m.x30)**2 + (m.x102 - m.x120)**2 + (m.x192 - m.x210)**2) + 1 /
    sqrt((m.x12 - m.x31)**2 + (m.x102 - m.x121)**2 + (m.x192 - m.x211)**2) + 1
    / sqrt((m.x12 - m.x32)**2 + (m.x102 - m.x122)**2 + (m.x192 - m.x212)**2)
    + 1 / sqrt((m.x12 - m.x33)**2 + (m.x102 - m.x123)**2 + (m.x192 - m.x213)**
    2) + 1 / sqrt((m.x12 - m.x34)**2 + (m.x102 - m.x124)**2 + (m.x192 - m.x214)
    **2) + 1 / sqrt((m.x12 - m.x35)**2 + (m.x102 - m.x125)**2 + (m.x192 -
    m.x215)**2) + 1 / sqrt((m.x12 - m.x36)**2 + (m.x102 - m.x126)**2 + (m.x192
    - m.x216)**2) + 1 / sqrt((m.x12 - m.x37)**2 + (m.x102 - m.x127)**2 + (
    m.x192 - m.x217)**2) + 1 / sqrt((m.x12 - m.x38)**2 + (m.x102 - m.x128)**2
    + (m.x192 - m.x218)**2) + 1 / sqrt((m.x12 - m.x39)**2 + (m.x102 - m.x129)
    **2 + (m.x192 - m.x219)**2) + 1 / sqrt((m.x12 - m.x40)**2 + (m.x102 -
    m.x130)**2 + (m.x192 - m.x220)**2) + 1 / sqrt((m.x12 - m.x41)**2 + (m.x102
    - m.x131)**2 + (m.x192 - m.x221)**2) + 1 / sqrt((m.x12 - m.x42)**2 + (
    m.x102 - m.x132)**2 + (m.x192 - m.x222)**2) + 1 / sqrt((m.x12 - m.x43)**2
    + (m.x102 - m.x133)**2 + (m.x192 - m.x223)**2) + 1 / sqrt((m.x12 - m.x44)
    **2 + (m.x102 - m.x134)**2 + (m.x192 - m.x224)**2) + 1 / sqrt((m.x12 -
    m.x45)**2 + (m.x102 - m.x135)**2 + (m.x192 - m.x225)**2) + 1 / sqrt((m.x12
    - m.x46)**2 + (m.x102 - m.x136)**2 + (m.x192 - m.x226)**2) + 1 / sqrt((
    m.x12 - m.x47)**2 + (m.x102 - m.x137)**2 + (m.x192 - m.x227)**2) + 1 /
    sqrt((m.x12 - m.x48)**2 + (m.x102 - m.x138)**2 + (m.x192 - m.x228)**2) + 1
    / sqrt((m.x12 - m.x49)**2 + (m.x102 - m.x139)**2 + (m.x192 - m.x229)**2)
    + 1 / sqrt((m.x12 - m.x50)**2 + (m.x102 - m.x140)**2 + (m.x192 - m.x230)**
    2) + 1 / sqrt((m.x12 - m.x51)**2 + (m.x102 - m.x141)**2 + (m.x192 - m.x231)
    **2) + 1 / sqrt((m.x12 - m.x52)**2 + (m.x102 - m.x142)**2 + (m.x192 -
    m.x232)**2) + 1 / sqrt((m.x12 - m.x53)**2 + (m.x102 - m.x143)**2 + (m.x192
    - m.x233)**2) + 1 / sqrt((m.x12 - m.x54)**2 + (m.x102 - m.x144)**2 + (
    m.x192 - m.x234)**2) + 1 / sqrt((m.x12 - m.x55)**2 + (m.x102 - m.x145)**2
    + (m.x192 - m.x235)**2) + 1 / sqrt((m.x12 - m.x56)**2 + (m.x102 - m.x146)
    **2 + (m.x192 - m.x236)**2) + 1 / sqrt((m.x12 - m.x57)**2 + (m.x102 -
    m.x147)**2 + (m.x192 - m.x237)**2) + 1 / sqrt((m.x12 - m.x58)**2 + (m.x102
    - m.x148)**2 + (m.x192 - m.x238)**2) + 1 / sqrt((m.x12 - m.x59)**2 + (
    m.x102 - m.x149)**2 + (m.x192 - m.x239)**2) + 1 / sqrt((m.x12 - m.x60)**2
    + (m.x102 - m.x150)**2 + (m.x192 - m.x240)**2) + 1 / sqrt((m.x12 - m.x61)
    **2 + (m.x102 - m.x151)**2 + (m.x192 - m.x241)**2) + 1 / sqrt((m.x12 -
    m.x62)**2 + (m.x102 - m.x152)**2 + (m.x192 - m.x242)**2) + 1 / sqrt((m.x12
    - m.x63)**2 + (m.x102 - m.x153)**2 + (m.x192 - m.x243)**2) + 1 / sqrt((
    m.x12 - m.x64)**2 + (m.x102 - m.x154)**2 + (m.x192 - m.x244)**2) + 1 /
    sqrt((m.x12 - m.x65)**2 + (m.x102 - m.x155)**2 + (m.x192 - m.x245)**2) + 1
    / sqrt((m.x12 - m.x66)**2 + (m.x102 - m.x156)**2 + (m.x192 - m.x246)**2)
    + 1 / sqrt((m.x12 - m.x67)**2 + (m.x102 - m.x157)**2 + (m.x192 - m.x247)**
    2) + 1 / sqrt((m.x12 - m.x68)**2 + (m.x102 - m.x158)**2 + (m.x192 - m.x248)
    **2) + 1 / sqrt((m.x12 - m.x69)**2 + (m.x102 - m.x159)**2 + (m.x192 -
    m.x249)**2) + 1 / sqrt((m.x12 - m.x70)**2 + (m.x102 - m.x160)**2 + (m.x192
    - m.x250)**2) + 1 / sqrt((m.x12 - m.x71)**2 + (m.x102 - m.x161)**2 + (
    m.x192 - m.x251)**2) + 1 / sqrt((m.x12 - m.x72)**2 + (m.x102 - m.x162)**2
    + (m.x192 - m.x252)**2) + 1 / sqrt((m.x12 - m.x73)**2 + (m.x102 - m.x163)
    **2 + (m.x192 - m.x253)**2) + 1 / sqrt((m.x12 - m.x74)**2 + (m.x102 -
    m.x164)**2 + (m.x192 - m.x254)**2) + 1 / sqrt((m.x12 - m.x75)**2 + (m.x102
    - m.x165)**2 + (m.x192 - m.x255)**2) + 1 / sqrt((m.x12 - m.x76)**2 + (
    m.x102 - m.x166)**2 + (m.x192 - m.x256)**2) + 1 / sqrt((m.x12 - m.x77)**2
    + (m.x102 - m.x167)**2 + (m.x192 - m.x257)**2) + 1 / sqrt((m.x12 - m.x78)
    **2 + (m.x102 - m.x168)**2 + (m.x192 - m.x258)**2) + 1 / sqrt((m.x12 -
    m.x79)**2 + (m.x102 - m.x169)**2 + (m.x192 - m.x259)**2) + 1 / sqrt((m.x12
    - m.x80)**2 + (m.x102 - m.x170)**2 + (m.x192 - m.x260)**2) + 1 / sqrt((
    m.x12 - m.x81)**2 + (m.x102 - m.x171)**2 + (m.x192 - m.x261)**2) + 1 /
    sqrt((m.x12 - m.x82)**2 + (m.x102 - m.x172)**2 + (m.x192 - m.x262)**2) + 1
    / sqrt((m.x12 - m.x83)**2 + (m.x102 - m.x173)**2 + (m.x192 - m.x263)**2)
    + 1 / sqrt((m.x12 - m.x84)**2 + (m.x102 - m.x174)**2 + (m.x192 - m.x264)**
    2) + 1 / sqrt((m.x12 - m.x85)**2 + (m.x102 - m.x175)**2 + (m.x192 - m.x265)
    **2) + 1 / sqrt((m.x12 - m.x86)**2 + (m.x102 - m.x176)**2 + (m.x192 -
    m.x266)**2) + 1 / sqrt((m.x12 - m.x87)**2 + (m.x102 - m.x177)**2 + (m.x192
    - m.x267)**2) + 1 / sqrt((m.x12 - m.x88)**2 + (m.x102 - m.x178)**2 + (
    m.x192 - m.x268)**2) + 1 / sqrt((m.x12 - m.x89)**2 + (m.x102 - m.x179)**2
    + (m.x192 - m.x269)**2) + 1 / sqrt((m.x12 - m.x90)**2 + (m.x102 - m.x180)
    **2 + (m.x192 - m.x270)**2) + 1 / sqrt((m.x13 - m.x14)**2 + (m.x103 -
    m.x104)**2 + (m.x193 - m.x194)**2) + 1 / sqrt((m.x13 - m.x15)**2 + (m.x103
    - m.x105)**2 + (m.x193 - m.x195)**2) + 1 / sqrt((m.x13 - m.x16)**2 + (
    m.x103 - m.x106)**2 + (m.x193 - m.x196)**2) + 1 / sqrt((m.x13 - m.x17)**2
    + (m.x103 - m.x107)**2 + (m.x193 - m.x197)**2) + 1 / sqrt((m.x13 - m.x18)
    **2 + (m.x103 - m.x108)**2 + (m.x193 - m.x198)**2) + 1 / sqrt((m.x13 -
    m.x19)**2 + (m.x103 - m.x109)**2 + (m.x193 - m.x199)**2) + 1 / sqrt((m.x13
    - m.x20)**2 + (m.x103 - m.x110)**2 + (m.x193 - m.x200)**2) + 1 / sqrt((
    m.x13 - m.x21)**2 + (m.x103 - m.x111)**2 + (m.x193 - m.x201)**2) + 1 /
    sqrt((m.x13 - m.x22)**2 + (m.x103 - m.x112)**2 + (m.x193 - m.x202)**2) + 1
    / sqrt((m.x13 - m.x23)**2 + (m.x103 - m.x113)**2 + (m.x193 - m.x203)**2)
    + 1 / sqrt((m.x13 - m.x24)**2 + (m.x103 - m.x114)**2 + (m.x193 - m.x204)**
    2) + 1 / sqrt((m.x13 - m.x25)**2 + (m.x103 - m.x115)**2 + (m.x193 - m.x205)
    **2) + 1 / sqrt((m.x13 - m.x26)**2 + (m.x103 - m.x116)**2 + (m.x193 -
    m.x206)**2) + 1 / sqrt((m.x13 - m.x27)**2 + (m.x103 - m.x117)**2 + (m.x193
    - m.x207)**2) + 1 / sqrt((m.x13 - m.x28)**2 + (m.x103 - m.x118)**2 + (
    m.x193 - m.x208)**2) + 1 / sqrt((m.x13 - m.x29)**2 + (m.x103 - m.x119)**2
    + (m.x193 - m.x209)**2) + 1 / sqrt((m.x13 - m.x30)**2 + (m.x103 - m.x120)
    **2 + (m.x193 - m.x210)**2) + 1 / sqrt((m.x13 - m.x31)**2 + (m.x103 -
    m.x121)**2 + (m.x193 - m.x211)**2) + 1 / sqrt((m.x13 - m.x32)**2 + (m.x103
    - m.x122)**2 + (m.x193 - m.x212)**2) + 1 / sqrt((m.x13 - m.x33)**2 + (
    m.x103 - m.x123)**2 + (m.x193 - m.x213)**2) + 1 / sqrt((m.x13 - m.x34)**2
    + (m.x103 - m.x124)**2 + (m.x193 - m.x214)**2) + 1 / sqrt((m.x13 - m.x35)
    **2 + (m.x103 - m.x125)**2 + (m.x193 - m.x215)**2) + 1 / sqrt((m.x13 -
    m.x36)**2 + (m.x103 - m.x126)**2 + (m.x193 - m.x216)**2) + 1 / sqrt((m.x13
    - m.x37)**2 + (m.x103 - m.x127)**2 + (m.x193 - m.x217)**2) + 1 / sqrt((
    m.x13 - m.x38)**2 + (m.x103 - m.x128)**2 + (m.x193 - m.x218)**2) + 1 /
    sqrt((m.x13 - m.x39)**2 + (m.x103 - m.x129)**2 + (m.x193 - m.x219)**2) + 1
    / sqrt((m.x13 - m.x40)**2 + (m.x103 - m.x130)**2 + (m.x193 - m.x220)**2)
    + 1 / sqrt((m.x13 - m.x41)**2 + (m.x103 - m.x131)**2 + (m.x193 - m.x221)**
    2) + 1 / sqrt((m.x13 - m.x42)**2 + (m.x103 - m.x132)**2 + (m.x193 - m.x222)
    **2) + 1 / sqrt((m.x13 - m.x43)**2 + (m.x103 - m.x133)**2 + (m.x193 -
    m.x223)**2) + 1 / sqrt((m.x13 - m.x44)**2 + (m.x103 - m.x134)**2 + (m.x193
    - m.x224)**2) + 1 / sqrt((m.x13 - m.x45)**2 + (m.x103 - m.x135)**2 + (
    m.x193 - m.x225)**2) + 1 / sqrt((m.x13 - m.x46)**2 + (m.x103 - m.x136)**2
    + (m.x193 - m.x226)**2) + 1 / sqrt((m.x13 - m.x47)**2 + (m.x103 - m.x137)
    **2 + (m.x193 - m.x227)**2) + 1 / sqrt((m.x13 - m.x48)**2 + (m.x103 -
    m.x138)**2 + (m.x193 - m.x228)**2) + 1 / sqrt((m.x13 - m.x49)**2 + (m.x103
    - m.x139)**2 + (m.x193 - m.x229)**2) + 1 / sqrt((m.x13 - m.x50)**2 + (
    m.x103 - m.x140)**2 + (m.x193 - m.x230)**2) + 1 / sqrt((m.x13 - m.x51)**2
    + (m.x103 - m.x141)**2 + (m.x193 - m.x231)**2) + 1 / sqrt((m.x13 - m.x52)
    **2 + (m.x103 - m.x142)**2 + (m.x193 - m.x232)**2) + 1 / sqrt((m.x13 -
    m.x53)**2 + (m.x103 - m.x143)**2 + (m.x193 - m.x233)**2) + 1 / sqrt((m.x13
    - m.x54)**2 + (m.x103 - m.x144)**2 + (m.x193 - m.x234)**2) + 1 / sqrt((
    m.x13 - m.x55)**2 + (m.x103 - m.x145)**2 + (m.x193 - m.x235)**2) + 1 /
    sqrt((m.x13 - m.x56)**2 + (m.x103 - m.x146)**2 + (m.x193 - m.x236)**2) + 1
    / sqrt((m.x13 - m.x57)**2 + (m.x103 - m.x147)**2 + (m.x193 - m.x237)**2)
    + 1 / sqrt((m.x13 - m.x58)**2 + (m.x103 - m.x148)**2 + (m.x193 - m.x238)**
    2) + 1 / sqrt((m.x13 - m.x59)**2 + (m.x103 - m.x149)**2 + (m.x193 - m.x239)
    **2) + 1 / sqrt((m.x13 - m.x60)**2 + (m.x103 - m.x150)**2 + (m.x193 -
    m.x240)**2) + 1 / sqrt((m.x13 - m.x61)**2 + (m.x103 - m.x151)**2 + (m.x193
    - m.x241)**2) + 1 / sqrt((m.x13 - m.x62)**2 + (m.x103 - m.x152)**2 + (
    m.x193 - m.x242)**2) + 1 / sqrt((m.x13 - m.x63)**2 + (m.x103 - m.x153)**2
    + (m.x193 - m.x243)**2) + 1 / sqrt((m.x13 - m.x64)**2 + (m.x103 - m.x154)
    **2 + (m.x193 - m.x244)**2) + 1 / sqrt((m.x13 - m.x65)**2 + (m.x103 -
    m.x155)**2 + (m.x193 - m.x245)**2) + 1 / sqrt((m.x13 - m.x66)**2 + (m.x103
    - m.x156)**2 + (m.x193 - m.x246)**2) + 1 / sqrt((m.x13 - m.x67)**2 + (
    m.x103 - m.x157)**2 + (m.x193 - m.x247)**2) + 1 / sqrt((m.x13 - m.x68)**2
    + (m.x103 - m.x158)**2 + (m.x193 - m.x248)**2) + 1 / sqrt((m.x13 - m.x69)
    **2 + (m.x103 - m.x159)**2 + (m.x193 - m.x249)**2) + 1 / sqrt((m.x13 -
    m.x70)**2 + (m.x103 - m.x160)**2 + (m.x193 - m.x250)**2) + 1 / sqrt((m.x13
    - m.x71)**2 + (m.x103 - m.x161)**2 + (m.x193 - m.x251)**2) + 1 / sqrt((
    m.x13 - m.x72)**2 + (m.x103 - m.x162)**2 + (m.x193 - m.x252)**2) + 1 /
    sqrt((m.x13 - m.x73)**2 + (m.x103 - m.x163)**2 + (m.x193 - m.x253)**2) + 1
    / sqrt((m.x13 - m.x74)**2 + (m.x103 - m.x164)**2 + (m.x193 - m.x254)**2)
    + 1 / sqrt((m.x13 - m.x75)**2 + (m.x103 - m.x165)**2 + (m.x193 - m.x255)**
    2) + 1 / sqrt((m.x13 - m.x76)**2 + (m.x103 - m.x166)**2 + (m.x193 - m.x256)
    **2) + 1 / sqrt((m.x13 - m.x77)**2 + (m.x103 - m.x167)**2 + (m.x193 -
    m.x257)**2) + 1 / sqrt((m.x13 - m.x78)**2 + (m.x103 - m.x168)**2 + (m.x193
    - m.x258)**2) + 1 / sqrt((m.x13 - m.x79)**2 + (m.x103 - m.x169)**2 + (
    m.x193 - m.x259)**2) + 1 / sqrt((m.x13 - m.x80)**2 + (m.x103 - m.x170)**2
    + (m.x193 - m.x260)**2) + 1 / sqrt((m.x13 - m.x81)**2 + (m.x103 - m.x171)
    **2 + (m.x193 - m.x261)**2) + 1 / sqrt((m.x13 - m.x82)**2 + (m.x103 -
    m.x172)**2 + (m.x193 - m.x262)**2) + 1 / sqrt((m.x13 - m.x83)**2 + (m.x103
    - m.x173)**2 + (m.x193 - m.x263)**2) + 1 / sqrt((m.x13 - m.x84)**2 + (
    m.x103 - m.x174)**2 + (m.x193 - m.x264)**2) + 1 / sqrt((m.x13 - m.x85)**2
    + (m.x103 - m.x175)**2 + (m.x193 - m.x265)**2) + 1 / sqrt((m.x13 - m.x86)
    **2 + (m.x103 - m.x176)**2 + (m.x193 - m.x266)**2) + 1 / sqrt((m.x13 -
    m.x87)**2 + (m.x103 - m.x177)**2 + (m.x193 - m.x267)**2) + 1 / sqrt((m.x13
    - m.x88)**2 + (m.x103 - m.x178)**2 + (m.x193 - m.x268)**2) + 1 / sqrt((
    m.x13 - m.x89)**2 + (m.x103 - m.x179)**2 + (m.x193 - m.x269)**2) + 1 /
    sqrt((m.x13 - m.x90)**2 + (m.x103 - m.x180)**2 + (m.x193 - m.x270)**2) + 1
    / sqrt((m.x14 - m.x15)**2 + (m.x104 - m.x105)**2 + (m.x194 - m.x195)**2)
    + 1 / sqrt((m.x14 - m.x16)**2 + (m.x104 - m.x106)**2 + (m.x194 - m.x196)**
    2) + 1 / sqrt((m.x14 - m.x17)**2 + (m.x104 - m.x107)**2 + (m.x194 - m.x197)
    **2) + 1 / sqrt((m.x14 - m.x18)**2 + (m.x104 - m.x108)**2 + (m.x194 -
    m.x198)**2) + 1 / sqrt((m.x14 - m.x19)**2 + (m.x104 - m.x109)**2 + (m.x194
    - m.x199)**2) + 1 / sqrt((m.x14 - m.x20)**2 + (m.x104 - m.x110)**2 + (
    m.x194 - m.x200)**2) + 1 / sqrt((m.x14 - m.x21)**2 + (m.x104 - m.x111)**2
    + (m.x194 - m.x201)**2) + 1 / sqrt((m.x14 - m.x22)**2 + (m.x104 - m.x112)
    **2 + (m.x194 - m.x202)**2) + 1 / sqrt((m.x14 - m.x23)**2 + (m.x104 -
    m.x113)**2 + (m.x194 - m.x203)**2) + 1 / sqrt((m.x14 - m.x24)**2 + (m.x104
    - m.x114)**2 + (m.x194 - m.x204)**2) + 1 / sqrt((m.x14 - m.x25)**2 + (
    m.x104 - m.x115)**2 + (m.x194 - m.x205)**2) + 1 / sqrt((m.x14 - m.x26)**2
    + (m.x104 - m.x116)**2 + (m.x194 - m.x206)**2) + 1 / sqrt((m.x14 - m.x27)
    **2 + (m.x104 - m.x117)**2 + (m.x194 - m.x207)**2) + 1 / sqrt((m.x14 -
    m.x28)**2 + (m.x104 - m.x118)**2 + (m.x194 - m.x208)**2) + 1 / sqrt((m.x14
    - m.x29)**2 + (m.x104 - m.x119)**2 + (m.x194 - m.x209)**2) + 1 / sqrt((
    m.x14 - m.x30)**2 + (m.x104 - m.x120)**2 + (m.x194 - m.x210)**2) + 1 /
    sqrt((m.x14 - m.x31)**2 + (m.x104 - m.x121)**2 + (m.x194 - m.x211)**2) + 1
    / sqrt((m.x14 - m.x32)**2 + (m.x104 - m.x122)**2 + (m.x194 - m.x212)**2)
    + 1 / sqrt((m.x14 - m.x33)**2 + (m.x104 - m.x123)**2 + (m.x194 - m.x213)**
    2) + 1 / sqrt((m.x14 - m.x34)**2 + (m.x104 - m.x124)**2 + (m.x194 - m.x214)
    **2) + 1 / sqrt((m.x14 - m.x35)**2 + (m.x104 - m.x125)**2 + (m.x194 -
    m.x215)**2) + 1 / sqrt((m.x14 - m.x36)**2 + (m.x104 - m.x126)**2 + (m.x194
    - m.x216)**2) + 1 / sqrt((m.x14 - m.x37)**2 + (m.x104 - m.x127)**2 + (
    m.x194 - m.x217)**2) + 1 / sqrt((m.x14 - m.x38)**2 + (m.x104 - m.x128)**2
    + (m.x194 - m.x218)**2) + 1 / sqrt((m.x14 - m.x39)**2 + (m.x104 - m.x129)
    **2 + (m.x194 - m.x219)**2) + 1 / sqrt((m.x14 - m.x40)**2 + (m.x104 -
    m.x130)**2 + (m.x194 - m.x220)**2) + 1 / sqrt((m.x14 - m.x41)**2 + (m.x104
    - m.x131)**2 + (m.x194 - m.x221)**2) + 1 / sqrt((m.x14 - m.x42)**2 + (
    m.x104 - m.x132)**2 + (m.x194 - m.x222)**2) + 1 / sqrt((m.x14 - m.x43)**2
    + (m.x104 - m.x133)**2 + (m.x194 - m.x223)**2) + 1 / sqrt((m.x14 - m.x44)
    **2 + (m.x104 - m.x134)**2 + (m.x194 - m.x224)**2) + 1 / sqrt((m.x14 -
    m.x45)**2 + (m.x104 - m.x135)**2 + (m.x194 - m.x225)**2) + 1 / sqrt((m.x14
    - m.x46)**2 + (m.x104 - m.x136)**2 + (m.x194 - m.x226)**2) + 1 / sqrt((
    m.x14 - m.x47)**2 + (m.x104 - m.x137)**2 + (m.x194 - m.x227)**2) + 1 /
    sqrt((m.x14 - m.x48)**2 + (m.x104 - m.x138)**2 + (m.x194 - m.x228)**2) + 1
    / sqrt((m.x14 - m.x49)**2 + (m.x104 - m.x139)**2 + (m.x194 - m.x229)**2)
    + 1 / sqrt((m.x14 - m.x50)**2 + (m.x104 - m.x140)**2 + (m.x194 - m.x230)**
    2) + 1 / sqrt((m.x14 - m.x51)**2 + (m.x104 - m.x141)**2 + (m.x194 - m.x231)
    **2) + 1 / sqrt((m.x14 - m.x52)**2 + (m.x104 - m.x142)**2 + (m.x194 -
    m.x232)**2) + 1 / sqrt((m.x14 - m.x53)**2 + (m.x104 - m.x143)**2 + (m.x194
    - m.x233)**2) + 1 / sqrt((m.x14 - m.x54)**2 + (m.x104 - m.x144)**2 + (
    m.x194 - m.x234)**2) + 1 / sqrt((m.x14 - m.x55)**2 + (m.x104 - m.x145)**2
    + (m.x194 - m.x235)**2) + 1 / sqrt((m.x14 - m.x56)**2 + (m.x104 - m.x146)
    **2 + (m.x194 - m.x236)**2) + 1 / sqrt((m.x14 - m.x57)**2 + (m.x104 -
    m.x147)**2 + (m.x194 - m.x237)**2) + 1 / sqrt((m.x14 - m.x58)**2 + (m.x104
    - m.x148)**2 + (m.x194 - m.x238)**2) + 1 / sqrt((m.x14 - m.x59)**2 + (
    m.x104 - m.x149)**2 + (m.x194 - m.x239)**2) + 1 / sqrt((m.x14 - m.x60)**2
    + (m.x104 - m.x150)**2 + (m.x194 - m.x240)**2) + 1 / sqrt((m.x14 - m.x61)
    **2 + (m.x104 - m.x151)**2 + (m.x194 - m.x241)**2) + 1 / sqrt((m.x14 -
    m.x62)**2 + (m.x104 - m.x152)**2 + (m.x194 - m.x242)**2) + 1 / sqrt((m.x14
    - m.x63)**2 + (m.x104 - m.x153)**2 + (m.x194 - m.x243)**2) + 1 / sqrt((
    m.x14 - m.x64)**2 + (m.x104 - m.x154)**2 + (m.x194 - m.x244)**2) + 1 /
    sqrt((m.x14 - m.x65)**2 + (m.x104 - m.x155)**2 + (m.x194 - m.x245)**2) + 1
    / sqrt((m.x14 - m.x66)**2 + (m.x104 - m.x156)**2 + (m.x194 - m.x246)**2)
    + 1 / sqrt((m.x14 - m.x67)**2 + (m.x104 - m.x157)**2 + (m.x194 - m.x247)**
    2) + 1 / sqrt((m.x14 - m.x68)**2 + (m.x104 - m.x158)**2 + (m.x194 - m.x248)
    **2) + 1 / sqrt((m.x14 - m.x69)**2 + (m.x104 - m.x159)**2 + (m.x194 -
    m.x249)**2) + 1 / sqrt((m.x14 - m.x70)**2 + (m.x104 - m.x160)**2 + (m.x194
    - m.x250)**2) + 1 / sqrt((m.x14 - m.x71)**2 + (m.x104 - m.x161)**2 + (
    m.x194 - m.x251)**2) + 1 / sqrt((m.x14 - m.x72)**2 + (m.x104 - m.x162)**2
    + (m.x194 - m.x252)**2) + 1 / sqrt((m.x14 - m.x73)**2 + (m.x104 - m.x163)
    **2 + (m.x194 - m.x253)**2) + 1 / sqrt((m.x14 - m.x74)**2 + (m.x104 -
    m.x164)**2 + (m.x194 - m.x254)**2) + 1 / sqrt((m.x14 - m.x75)**2 + (m.x104
    - m.x165)**2 + (m.x194 - m.x255)**2) + 1 / sqrt((m.x14 - m.x76)**2 + (
    m.x104 - m.x166)**2 + (m.x194 - m.x256)**2) + 1 / sqrt((m.x14 - m.x77)**2
    + (m.x104 - m.x167)**2 + (m.x194 - m.x257)**2) + 1 / sqrt((m.x14 - m.x78)
    **2 + (m.x104 - m.x168)**2 + (m.x194 - m.x258)**2) + 1 / sqrt((m.x14 -
    m.x79)**2 + (m.x104 - m.x169)**2 + (m.x194 - m.x259)**2) + 1 / sqrt((m.x14
    - m.x80)**2 + (m.x104 - m.x170)**2 + (m.x194 - m.x260)**2) + 1 / sqrt((
    m.x14 - m.x81)**2 + (m.x104 - m.x171)**2 + (m.x194 - m.x261)**2) + 1 /
    sqrt((m.x14 - m.x82)**2 + (m.x104 - m.x172)**2 + (m.x194 - m.x262)**2) + 1
    / sqrt((m.x14 - m.x83)**2 + (m.x104 - m.x173)**2 + (m.x194 - m.x263)**2)
    + 1 / sqrt((m.x14 - m.x84)**2 + (m.x104 - m.x174)**2 + (m.x194 - m.x264)**
    2) + 1 / sqrt((m.x14 - m.x85)**2 + (m.x104 - m.x175)**2 + (m.x194 - m.x265)
    **2) + 1 / sqrt((m.x14 - m.x86)**2 + (m.x104 - m.x176)**2 + (m.x194 -
    m.x266)**2) + 1 / sqrt((m.x14 - m.x87)**2 + (m.x104 - m.x177)**2 + (m.x194
    - m.x267)**2) + 1 / sqrt((m.x14 - m.x88)**2 + (m.x104 - m.x178)**2 + (
    m.x194 - m.x268)**2) + 1 / sqrt((m.x14 - m.x89)**2 + (m.x104 - m.x179)**2
    + (m.x194 - m.x269)**2) + 1 / sqrt((m.x14 - m.x90)**2 + (m.x104 - m.x180)
    **2 + (m.x194 - m.x270)**2) + 1 / sqrt((m.x15 - m.x16)**2 + (m.x105 -
    m.x106)**2 + (m.x195 - m.x196)**2) + 1 / sqrt((m.x15 - m.x17)**2 + (m.x105
    - m.x107)**2 + (m.x195 - m.x197)**2) + 1 / sqrt((m.x15 - m.x18)**2 + (
    m.x105 - m.x108)**2 + (m.x195 - m.x198)**2) + 1 / sqrt((m.x15 - m.x19)**2
    + (m.x105 - m.x109)**2 + (m.x195 - m.x199)**2) + 1 / sqrt((m.x15 - m.x20)
    **2 + (m.x105 - m.x110)**2 + (m.x195 - m.x200)**2) + 1 / sqrt((m.x15 -
    m.x21)**2 + (m.x105 - m.x111)**2 + (m.x195 - m.x201)**2) + 1 / sqrt((m.x15
    - m.x22)**2 + (m.x105 - m.x112)**2 + (m.x195 - m.x202)**2) + 1 / sqrt((
    m.x15 - m.x23)**2 + (m.x105 - m.x113)**2 + (m.x195 - m.x203)**2) + 1 /
    sqrt((m.x15 - m.x24)**2 + (m.x105 - m.x114)**2 + (m.x195 - m.x204)**2) + 1
    / sqrt((m.x15 - m.x25)**2 + (m.x105 - m.x115)**2 + (m.x195 - m.x205)**2)
    + 1 / sqrt((m.x15 - m.x26)**2 + (m.x105 - m.x116)**2 + (m.x195 - m.x206)**
    2) + 1 / sqrt((m.x15 - m.x27)**2 + (m.x105 - m.x117)**2 + (m.x195 - m.x207)
    **2) + 1 / sqrt((m.x15 - m.x28)**2 + (m.x105 - m.x118)**2 + (m.x195 -
    m.x208)**2) + 1 / sqrt((m.x15 - m.x29)**2 + (m.x105 - m.x119)**2 + (m.x195
    - m.x209)**2) + 1 / sqrt((m.x15 - m.x30)**2 + (m.x105 - m.x120)**2 + (
    m.x195 - m.x210)**2) + 1 / sqrt((m.x15 - m.x31)**2 + (m.x105 - m.x121)**2
    + (m.x195 - m.x211)**2) + 1 / sqrt((m.x15 - m.x32)**2 + (m.x105 - m.x122)
    **2 + (m.x195 - m.x212)**2) + 1 / sqrt((m.x15 - m.x33)**2 + (m.x105 -
    m.x123)**2 + (m.x195 - m.x213)**2) + 1 / sqrt((m.x15 - m.x34)**2 + (m.x105
    - m.x124)**2 + (m.x195 - m.x214)**2) + 1 / sqrt((m.x15 - m.x35)**2 + (
    m.x105 - m.x125)**2 + (m.x195 - m.x215)**2) + 1 / sqrt((m.x15 - m.x36)**2
    + (m.x105 - m.x126)**2 + (m.x195 - m.x216)**2) + 1 / sqrt((m.x15 - m.x37)
    **2 + (m.x105 - m.x127)**2 + (m.x195 - m.x217)**2) + 1 / sqrt((m.x15 -
    m.x38)**2 + (m.x105 - m.x128)**2 + (m.x195 - m.x218)**2) + 1 / sqrt((m.x15
    - m.x39)**2 + (m.x105 - m.x129)**2 + (m.x195 - m.x219)**2) + 1 / sqrt((
    m.x15 - m.x40)**2 + (m.x105 - m.x130)**2 + (m.x195 - m.x220)**2) + 1 /
    sqrt((m.x15 - m.x41)**2 + (m.x105 - m.x131)**2 + (m.x195 - m.x221)**2) + 1
    / sqrt((m.x15 - m.x42)**2 + (m.x105 - m.x132)**2 + (m.x195 - m.x222)**2)
    + 1 / sqrt((m.x15 - m.x43)**2 + (m.x105 - m.x133)**2 + (m.x195 - m.x223)**
    2) + 1 / sqrt((m.x15 - m.x44)**2 + (m.x105 - m.x134)**2 + (m.x195 - m.x224)
    **2) + 1 / sqrt((m.x15 - m.x45)**2 + (m.x105 - m.x135)**2 + (m.x195 -
    m.x225)**2) + 1 / sqrt((m.x15 - m.x46)**2 + (m.x105 - m.x136)**2 + (m.x195
    - m.x226)**2) + 1 / sqrt((m.x15 - m.x47)**2 + (m.x105 - m.x137)**2 + (
    m.x195 - m.x227)**2) + 1 / sqrt((m.x15 - m.x48)**2 + (m.x105 - m.x138)**2
    + (m.x195 - m.x228)**2) + 1 / sqrt((m.x15 - m.x49)**2 + (m.x105 - m.x139)
    **2 + (m.x195 - m.x229)**2) + 1 / sqrt((m.x15 - m.x50)**2 + (m.x105 -
    m.x140)**2 + (m.x195 - m.x230)**2) + 1 / sqrt((m.x15 - m.x51)**2 + (m.x105
    - m.x141)**2 + (m.x195 - m.x231)**2) + 1 / sqrt((m.x15 - m.x52)**2 + (
    m.x105 - m.x142)**2 + (m.x195 - m.x232)**2) + 1 / sqrt((m.x15 - m.x53)**2
    + (m.x105 - m.x143)**2 + (m.x195 - m.x233)**2) + 1 / sqrt((m.x15 - m.x54)
    **2 + (m.x105 - m.x144)**2 + (m.x195 - m.x234)**2) + 1 / sqrt((m.x15 -
    m.x55)**2 + (m.x105 - m.x145)**2 + (m.x195 - m.x235)**2) + 1 / sqrt((m.x15
    - m.x56)**2 + (m.x105 - m.x146)**2 + (m.x195 - m.x236)**2) + 1 / sqrt((
    m.x15 - m.x57)**2 + (m.x105 - m.x147)**2 + (m.x195 - m.x237)**2) + 1 /
    sqrt((m.x15 - m.x58)**2 + (m.x105 - m.x148)**2 + (m.x195 - m.x238)**2) + 1
    / sqrt((m.x15 - m.x59)**2 + (m.x105 - m.x149)**2 + (m.x195 - m.x239)**2)
    + 1 / sqrt((m.x15 - m.x60)**2 + (m.x105 - m.x150)**2 + (m.x195 - m.x240)**
    2) + 1 / sqrt((m.x15 - m.x61)**2 + (m.x105 - m.x151)**2 + (m.x195 - m.x241)
    **2) + 1 / sqrt((m.x15 - m.x62)**2 + (m.x105 - m.x152)**2 + (m.x195 -
    m.x242)**2) + 1 / sqrt((m.x15 - m.x63)**2 + (m.x105 - m.x153)**2 + (m.x195
    - m.x243)**2) + 1 / sqrt((m.x15 - m.x64)**2 + (m.x105 - m.x154)**2 + (
    m.x195 - m.x244)**2) + 1 / sqrt((m.x15 - m.x65)**2 + (m.x105 - m.x155)**2
    + (m.x195 - m.x245)**2) + 1 / sqrt((m.x15 - m.x66)**2 + (m.x105 - m.x156)
    **2 + (m.x195 - m.x246)**2) + 1 / sqrt((m.x15 - m.x67)**2 + (m.x105 -
    m.x157)**2 + (m.x195 - m.x247)**2) + 1 / sqrt((m.x15 - m.x68)**2 + (m.x105
    - m.x158)**2 + (m.x195 - m.x248)**2) + 1 / sqrt((m.x15 - m.x69)**2 + (
    m.x105 - m.x159)**2 + (m.x195 - m.x249)**2) + 1 / sqrt((m.x15 - m.x70)**2
    + (m.x105 - m.x160)**2 + (m.x195 - m.x250)**2) + 1 / sqrt((m.x15 - m.x71)
    **2 + (m.x105 - m.x161)**2 + (m.x195 - m.x251)**2) + 1 / sqrt((m.x15 -
    m.x72)**2 + (m.x105 - m.x162)**2 + (m.x195 - m.x252)**2) + 1 / sqrt((m.x15
    - m.x73)**2 + (m.x105 - m.x163)**2 + (m.x195 - m.x253)**2) + 1 / sqrt((
    m.x15 - m.x74)**2 + (m.x105 - m.x164)**2 + (m.x195 - m.x254)**2) + 1 /
    sqrt((m.x15 - m.x75)**2 + (m.x105 - m.x165)**2 + (m.x195 - m.x255)**2) + 1
    / sqrt((m.x15 - m.x76)**2 + (m.x105 - m.x166)**2 + (m.x195 - m.x256)**2)
    + 1 / sqrt((m.x15 - m.x77)**2 + (m.x105 - m.x167)**2 + (m.x195 - m.x257)**
    2) + 1 / sqrt((m.x15 - m.x78)**2 + (m.x105 - m.x168)**2 + (m.x195 - m.x258)
    **2) + 1 / sqrt((m.x15 - m.x79)**2 + (m.x105 - m.x169)**2 + (m.x195 -
    m.x259)**2) + 1 / sqrt((m.x15 - m.x80)**2 + (m.x105 - m.x170)**2 + (m.x195
    - m.x260)**2) + 1 / sqrt((m.x15 - m.x81)**2 + (m.x105 - m.x171)**2 + (
    m.x195 - m.x261)**2) + 1 / sqrt((m.x15 - m.x82)**2 + (m.x105 - m.x172)**2
    + (m.x195 - m.x262)**2) + 1 / sqrt((m.x15 - m.x83)**2 + (m.x105 - m.x173)
    **2 + (m.x195 - m.x263)**2) + 1 / sqrt((m.x15 - m.x84)**2 + (m.x105 -
    m.x174)**2 + (m.x195 - m.x264)**2) + 1 / sqrt((m.x15 - m.x85)**2 + (m.x105
    - m.x175)**2 + (m.x195 - m.x265)**2) + 1 / sqrt((m.x15 - m.x86)**2 + (
    m.x105 - m.x176)**2 + (m.x195 - m.x266)**2) + 1 / sqrt((m.x15 - m.x87)**2
    + (m.x105 - m.x177)**2 + (m.x195 - m.x267)**2) + 1 / sqrt((m.x15 - m.x88)
    **2 + (m.x105 - m.x178)**2 + (m.x195 - m.x268)**2) + 1 / sqrt((m.x15 -
    m.x89)**2 + (m.x105 - m.x179)**2 + (m.x195 - m.x269)**2) + 1 / sqrt((m.x15
    - m.x90)**2 + (m.x105 - m.x180)**2 + (m.x195 - m.x270)**2) + 1 / sqrt((
    m.x16 - m.x17)**2 + (m.x106 - m.x107)**2 + (m.x196 - m.x197)**2) + 1 /
    sqrt((m.x16 - m.x18)**2 + (m.x106 - m.x108)**2 + (m.x196 - m.x198)**2) + 1
    / sqrt((m.x16 - m.x19)**2 + (m.x106 - m.x109)**2 + (m.x196 - m.x199)**2)
    + 1 / sqrt((m.x16 - m.x20)**2 + (m.x106 - m.x110)**2 + (m.x196 - m.x200)**
    2) + 1 / sqrt((m.x16 - m.x21)**2 + (m.x106 - m.x111)**2 + (m.x196 - m.x201)
    **2) + 1 / sqrt((m.x16 - m.x22)**2 + (m.x106 - m.x112)**2 + (m.x196 -
    m.x202)**2) + 1 / sqrt((m.x16 - m.x23)**2 + (m.x106 - m.x113)**2 + (m.x196
    - m.x203)**2) + 1 / sqrt((m.x16 - m.x24)**2 + (m.x106 - m.x114)**2 + (
    m.x196 - m.x204)**2) + 1 / sqrt((m.x16 - m.x25)**2 + (m.x106 - m.x115)**2
    + (m.x196 - m.x205)**2) + 1 / sqrt((m.x16 - m.x26)**2 + (m.x106 - m.x116)
    **2 + (m.x196 - m.x206)**2) + 1 / sqrt((m.x16 - m.x27)**2 + (m.x106 -
    m.x117)**2 + (m.x196 - m.x207)**2) + 1 / sqrt((m.x16 - m.x28)**2 + (m.x106
    - m.x118)**2 + (m.x196 - m.x208)**2) + 1 / sqrt((m.x16 - m.x29)**2 + (
    m.x106 - m.x119)**2 + (m.x196 - m.x209)**2) + 1 / sqrt((m.x16 - m.x30)**2
    + (m.x106 - m.x120)**2 + (m.x196 - m.x210)**2) + 1 / sqrt((m.x16 - m.x31)
    **2 + (m.x106 - m.x121)**2 + (m.x196 - m.x211)**2) + 1 / sqrt((m.x16 -
    m.x32)**2 + (m.x106 - m.x122)**2 + (m.x196 - m.x212)**2) + 1 / sqrt((m.x16
    - m.x33)**2 + (m.x106 - m.x123)**2 + (m.x196 - m.x213)**2) + 1 / sqrt((
    m.x16 - m.x34)**2 + (m.x106 - m.x124)**2 + (m.x196 - m.x214)**2) + 1 /
    sqrt((m.x16 - m.x35)**2 + (m.x106 - m.x125)**2 + (m.x196 - m.x215)**2) + 1
    / sqrt((m.x16 - m.x36)**2 + (m.x106 - m.x126)**2 + (m.x196 - m.x216)**2)
    + 1 / sqrt((m.x16 - m.x37)**2 + (m.x106 - m.x127)**2 + (m.x196 - m.x217)**
    2) + 1 / sqrt((m.x16 - m.x38)**2 + (m.x106 - m.x128)**2 + (m.x196 - m.x218)
    **2) + 1 / sqrt((m.x16 - m.x39)**2 + (m.x106 - m.x129)**2 + (m.x196 -
    m.x219)**2) + 1 / sqrt((m.x16 - m.x40)**2 + (m.x106 - m.x130)**2 + (m.x196
    - m.x220)**2) + 1 / sqrt((m.x16 - m.x41)**2 + (m.x106 - m.x131)**2 + (
    m.x196 - m.x221)**2) + 1 / sqrt((m.x16 - m.x42)**2 + (m.x106 - m.x132)**2
    + (m.x196 - m.x222)**2) + 1 / sqrt((m.x16 - m.x43)**2 + (m.x106 - m.x133)
    **2 + (m.x196 - m.x223)**2) + 1 / sqrt((m.x16 - m.x44)**2 + (m.x106 -
    m.x134)**2 + (m.x196 - m.x224)**2) + 1 / sqrt((m.x16 - m.x45)**2 + (m.x106
    - m.x135)**2 + (m.x196 - m.x225)**2) + 1 / sqrt((m.x16 - m.x46)**2 + (
    m.x106 - m.x136)**2 + (m.x196 - m.x226)**2) + 1 / sqrt((m.x16 - m.x47)**2
    + (m.x106 - m.x137)**2 + (m.x196 - m.x227)**2) + 1 / sqrt((m.x16 - m.x48)
    **2 + (m.x106 - m.x138)**2 + (m.x196 - m.x228)**2) + 1 / sqrt((m.x16 -
    m.x49)**2 + (m.x106 - m.x139)**2 + (m.x196 - m.x229)**2) + 1 / sqrt((m.x16
    - m.x50)**2 + (m.x106 - m.x140)**2 + (m.x196 - m.x230)**2) + 1 / sqrt((
    m.x16 - m.x51)**2 + (m.x106 - m.x141)**2 + (m.x196 - m.x231)**2) + 1 /
    sqrt((m.x16 - m.x52)**2 + (m.x106 - m.x142)**2 + (m.x196 - m.x232)**2) + 1
    / sqrt((m.x16 - m.x53)**2 + (m.x106 - m.x143)**2 + (m.x196 - m.x233)**2)
    + 1 / sqrt((m.x16 - m.x54)**2 + (m.x106 - m.x144)**2 + (m.x196 - m.x234)**
    2) + 1 / sqrt((m.x16 - m.x55)**2 + (m.x106 - m.x145)**2 + (m.x196 - m.x235)
    **2) + 1 / sqrt((m.x16 - m.x56)**2 + (m.x106 - m.x146)**2 + (m.x196 -
    m.x236)**2) + 1 / sqrt((m.x16 - m.x57)**2 + (m.x106 - m.x147)**2 + (m.x196
    - m.x237)**2) + 1 / sqrt((m.x16 - m.x58)**2 + (m.x106 - m.x148)**2 + (
    m.x196 - m.x238)**2) + 1 / sqrt((m.x16 - m.x59)**2 + (m.x106 - m.x149)**2
    + (m.x196 - m.x239)**2) + 1 / sqrt((m.x16 - m.x60)**2 + (m.x106 - m.x150)
    **2 + (m.x196 - m.x240)**2) + 1 / sqrt((m.x16 - m.x61)**2 + (m.x106 -
    m.x151)**2 + (m.x196 - m.x241)**2) + 1 / sqrt((m.x16 - m.x62)**2 + (m.x106
    - m.x152)**2 + (m.x196 - m.x242)**2) + 1 / sqrt((m.x16 - m.x63)**2 + (
    m.x106 - m.x153)**2 + (m.x196 - m.x243)**2) + 1 / sqrt((m.x16 - m.x64)**2
    + (m.x106 - m.x154)**2 + (m.x196 - m.x244)**2) + 1 / sqrt((m.x16 - m.x65)
    **2 + (m.x106 - m.x155)**2 + (m.x196 - m.x245)**2) + 1 / sqrt((m.x16 -
    m.x66)**2 + (m.x106 - m.x156)**2 + (m.x196 - m.x246)**2) + 1 / sqrt((m.x16
    - m.x67)**2 + (m.x106 - m.x157)**2 + (m.x196 - m.x247)**2) + 1 / sqrt((
    m.x16 - m.x68)**2 + (m.x106 - m.x158)**2 + (m.x196 - m.x248)**2) + 1 /
    sqrt((m.x16 - m.x69)**2 + (m.x106 - m.x159)**2 + (m.x196 - m.x249)**2) + 1
    / sqrt((m.x16 - m.x70)**2 + (m.x106 - m.x160)**2 + (m.x196 - m.x250)**2)
    + 1 / sqrt((m.x16 - m.x71)**2 + (m.x106 - m.x161)**2 + (m.x196 - m.x251)**
    2) + 1 / sqrt((m.x16 - m.x72)**2 + (m.x106 - m.x162)**2 + (m.x196 - m.x252)
    **2) + 1 / sqrt((m.x16 - m.x73)**2 + (m.x106 - m.x163)**2 + (m.x196 -
    m.x253)**2) + 1 / sqrt((m.x16 - m.x74)**2 + (m.x106 - m.x164)**2 + (m.x196
    - m.x254)**2) + 1 / sqrt((m.x16 - m.x75)**2 + (m.x106 - m.x165)**2 + (
    m.x196 - m.x255)**2) + 1 / sqrt((m.x16 - m.x76)**2 + (m.x106 - m.x166)**2
    + (m.x196 - m.x256)**2) + 1 / sqrt((m.x16 - m.x77)**2 + (m.x106 - m.x167)
    **2 + (m.x196 - m.x257)**2) + 1 / sqrt((m.x16 - m.x78)**2 + (m.x106 -
    m.x168)**2 + (m.x196 - m.x258)**2) + 1 / sqrt((m.x16 - m.x79)**2 + (m.x106
    - m.x169)**2 + (m.x196 - m.x259)**2) + 1 / sqrt((m.x16 - m.x80)**2 + (
    m.x106 - m.x170)**2 + (m.x196 - m.x260)**2) + 1 / sqrt((m.x16 - m.x81)**2
    + (m.x106 - m.x171)**2 + (m.x196 - m.x261)**2) + 1 / sqrt((m.x16 - m.x82)
    **2 + (m.x106 - m.x172)**2 + (m.x196 - m.x262)**2) + 1 / sqrt((m.x16 -
    m.x83)**2 + (m.x106 - m.x173)**2 + (m.x196 - m.x263)**2) + 1 / sqrt((m.x16
    - m.x84)**2 + (m.x106 - m.x174)**2 + (m.x196 - m.x264)**2) + 1 / sqrt((
    m.x16 - m.x85)**2 + (m.x106 - m.x175)**2 + (m.x196 - m.x265)**2) + 1 /
    sqrt((m.x16 - m.x86)**2 + (m.x106 - m.x176)**2 + (m.x196 - m.x266)**2) + 1
    / sqrt((m.x16 - m.x87)**2 + (m.x106 - m.x177)**2 + (m.x196 - m.x267)**2)
    + 1 / sqrt((m.x16 - m.x88)**2 + (m.x106 - m.x178)**2 + (m.x196 - m.x268)**
    2) + 1 / sqrt((m.x16 - m.x89)**2 + (m.x106 - m.x179)**2 + (m.x196 - m.x269)
    **2) + 1 / sqrt((m.x16 - m.x90)**2 + (m.x106 - m.x180)**2 + (m.x196 -
    m.x270)**2) + 1 / sqrt((m.x17 - m.x18)**2 + (m.x107 - m.x108)**2 + (m.x197
    - m.x198)**2) + 1 / sqrt((m.x17 - m.x19)**2 + (m.x107 - m.x109)**2 + (
    m.x197 - m.x199)**2) + 1 / sqrt((m.x17 - m.x20)**2 + (m.x107 - m.x110)**2
    + (m.x197 - m.x200)**2) + 1 / sqrt((m.x17 - m.x21)**2 + (m.x107 - m.x111)
    **2 + (m.x197 - m.x201)**2) + 1 / sqrt((m.x17 - m.x22)**2 + (m.x107 -
    m.x112)**2 + (m.x197 - m.x202)**2) + 1 / sqrt((m.x17 - m.x23)**2 + (m.x107
    - m.x113)**2 + (m.x197 - m.x203)**2) + 1 / sqrt((m.x17 - m.x24)**2 + (
    m.x107 - m.x114)**2 + (m.x197 - m.x204)**2) + 1 / sqrt((m.x17 - m.x25)**2
    + (m.x107 - m.x115)**2 + (m.x197 - m.x205)**2) + 1 / sqrt((m.x17 - m.x26)
    **2 + (m.x107 - m.x116)**2 + (m.x197 - m.x206)**2) + 1 / sqrt((m.x17 -
    m.x27)**2 + (m.x107 - m.x117)**2 + (m.x197 - m.x207)**2) + 1 / sqrt((m.x17
    - m.x28)**2 + (m.x107 - m.x118)**2 + (m.x197 - m.x208)**2) + 1 / sqrt((
    m.x17 - m.x29)**2 + (m.x107 - m.x119)**2 + (m.x197 - m.x209)**2) + 1 /
    sqrt((m.x17 - m.x30)**2 + (m.x107 - m.x120)**2 + (m.x197 - m.x210)**2) + 1
    / sqrt((m.x17 - m.x31)**2 + (m.x107 - m.x121)**2 + (m.x197 - m.x211)**2)
    + 1 / sqrt((m.x17 - m.x32)**2 + (m.x107 - m.x122)**2 + (m.x197 - m.x212)**
    2) + 1 / sqrt((m.x17 - m.x33)**2 + (m.x107 - m.x123)**2 + (m.x197 - m.x213)
    **2) + 1 / sqrt((m.x17 - m.x34)**2 + (m.x107 - m.x124)**2 + (m.x197 -
    m.x214)**2) + 1 / sqrt((m.x17 - m.x35)**2 + (m.x107 - m.x125)**2 + (m.x197
    - m.x215)**2) + 1 / sqrt((m.x17 - m.x36)**2 + (m.x107 - m.x126)**2 + (
    m.x197 - m.x216)**2) + 1 / sqrt((m.x17 - m.x37)**2 + (m.x107 - m.x127)**2
    + (m.x197 - m.x217)**2) + 1 / sqrt((m.x17 - m.x38)**2 + (m.x107 - m.x128)
    **2 + (m.x197 - m.x218)**2) + 1 / sqrt((m.x17 - m.x39)**2 + (m.x107 -
    m.x129)**2 + (m.x197 - m.x219)**2) + 1 / sqrt((m.x17 - m.x40)**2 + (m.x107
    - m.x130)**2 + (m.x197 - m.x220)**2) + 1 / sqrt((m.x17 - m.x41)**2 + (
    m.x107 - m.x131)**2 + (m.x197 - m.x221)**2) + 1 / sqrt((m.x17 - m.x42)**2
    + (m.x107 - m.x132)**2 + (m.x197 - m.x222)**2) + 1 / sqrt((m.x17 - m.x43)
    **2 + (m.x107 - m.x133)**2 + (m.x197 - m.x223)**2) + 1 / sqrt((m.x17 -
    m.x44)**2 + (m.x107 - m.x134)**2 + (m.x197 - m.x224)**2) + 1 / sqrt((m.x17
    - m.x45)**2 + (m.x107 - m.x135)**2 + (m.x197 - m.x225)**2) + 1 / sqrt((
    m.x17 - m.x46)**2 + (m.x107 - m.x136)**2 + (m.x197 - m.x226)**2) + 1 /
    sqrt((m.x17 - m.x47)**2 + (m.x107 - m.x137)**2 + (m.x197 - m.x227)**2) + 1
    / sqrt((m.x17 - m.x48)**2 + (m.x107 - m.x138)**2 + (m.x197 - m.x228)**2)
    + 1 / sqrt((m.x17 - m.x49)**2 + (m.x107 - m.x139)**2 + (m.x197 - m.x229)**
    2) + 1 / sqrt((m.x17 - m.x50)**2 + (m.x107 - m.x140)**2 + (m.x197 - m.x230)
    **2) + 1 / sqrt((m.x17 - m.x51)**2 + (m.x107 - m.x141)**2 + (m.x197 -
    m.x231)**2) + 1 / sqrt((m.x17 - m.x52)**2 + (m.x107 - m.x142)**2 + (m.x197
    - m.x232)**2) + 1 / sqrt((m.x17 - m.x53)**2 + (m.x107 - m.x143)**2 + (
    m.x197 - m.x233)**2) + 1 / sqrt((m.x17 - m.x54)**2 + (m.x107 - m.x144)**2
    + (m.x197 - m.x234)**2) + 1 / sqrt((m.x17 - m.x55)**2 + (m.x107 - m.x145)
    **2 + (m.x197 - m.x235)**2) + 1 / sqrt((m.x17 - m.x56)**2 + (m.x107 -
    m.x146)**2 + (m.x197 - m.x236)**2) + 1 / sqrt((m.x17 - m.x57)**2 + (m.x107
    - m.x147)**2 + (m.x197 - m.x237)**2) + 1 / sqrt((m.x17 - m.x58)**2 + (
    m.x107 - m.x148)**2 + (m.x197 - m.x238)**2) + 1 / sqrt((m.x17 - m.x59)**2
    + (m.x107 - m.x149)**2 + (m.x197 - m.x239)**2) + 1 / sqrt((m.x17 - m.x60)
    **2 + (m.x107 - m.x150)**2 + (m.x197 - m.x240)**2) + 1 / sqrt((m.x17 -
    m.x61)**2 + (m.x107 - m.x151)**2 + (m.x197 - m.x241)**2) + 1 / sqrt((m.x17
    - m.x62)**2 + (m.x107 - m.x152)**2 + (m.x197 - m.x242)**2) + 1 / sqrt((
    m.x17 - m.x63)**2 + (m.x107 - m.x153)**2 + (m.x197 - m.x243)**2) + 1 /
    sqrt((m.x17 - m.x64)**2 + (m.x107 - m.x154)**2 + (m.x197 - m.x244)**2) + 1
    / sqrt((m.x17 - m.x65)**2 + (m.x107 - m.x155)**2 + (m.x197 - m.x245)**2)
    + 1 / sqrt((m.x17 - m.x66)**2 + (m.x107 - m.x156)**2 + (m.x197 - m.x246)**
    2) + 1 / sqrt((m.x17 - m.x67)**2 + (m.x107 - m.x157)**2 + (m.x197 - m.x247)
    **2) + 1 / sqrt((m.x17 - m.x68)**2 + (m.x107 - m.x158)**2 + (m.x197 -
    m.x248)**2) + 1 / sqrt((m.x17 - m.x69)**2 + (m.x107 - m.x159)**2 + (m.x197
    - m.x249)**2) + 1 / sqrt((m.x17 - m.x70)**2 + (m.x107 - m.x160)**2 + (
    m.x197 - m.x250)**2) + 1 / sqrt((m.x17 - m.x71)**2 + (m.x107 - m.x161)**2
    + (m.x197 - m.x251)**2) + 1 / sqrt((m.x17 - m.x72)**2 + (m.x107 - m.x162)
    **2 + (m.x197 - m.x252)**2) + 1 / sqrt((m.x17 - m.x73)**2 + (m.x107 -
    m.x163)**2 + (m.x197 - m.x253)**2) + 1 / sqrt((m.x17 - m.x74)**2 + (m.x107
    - m.x164)**2 + (m.x197 - m.x254)**2) + 1 / sqrt((m.x17 - m.x75)**2 + (
    m.x107 - m.x165)**2 + (m.x197 - m.x255)**2) + 1 / sqrt((m.x17 - m.x76)**2
    + (m.x107 - m.x166)**2 + (m.x197 - m.x256)**2) + 1 / sqrt((m.x17 - m.x77)
    **2 + (m.x107 - m.x167)**2 + (m.x197 - m.x257)**2) + 1 / sqrt((m.x17 -
    m.x78)**2 + (m.x107 - m.x168)**2 + (m.x197 - m.x258)**2) + 1 / sqrt((m.x17
    - m.x79)**2 + (m.x107 - m.x169)**2 + (m.x197 - m.x259)**2) + 1 / sqrt((
    m.x17 - m.x80)**2 + (m.x107 - m.x170)**2 + (m.x197 - m.x260)**2) + 1 /
    sqrt((m.x17 - m.x81)**2 + (m.x107 - m.x171)**2 + (m.x197 - m.x261)**2) + 1
    / sqrt((m.x17 - m.x82)**2 + (m.x107 - m.x172)**2 + (m.x197 - m.x262)**2)
    + 1 / sqrt((m.x17 - m.x83)**2 + (m.x107 - m.x173)**2 + (m.x197 - m.x263)**
    2) + 1 / sqrt((m.x17 - m.x84)**2 + (m.x107 - m.x174)**2 + (m.x197 - m.x264)
    **2) + 1 / sqrt((m.x17 - m.x85)**2 + (m.x107 - m.x175)**2 + (m.x197 -
    m.x265)**2) + 1 / sqrt((m.x17 - m.x86)**2 + (m.x107 - m.x176)**2 + (m.x197
    - m.x266)**2) + 1 / sqrt((m.x17 - m.x87)**2 + (m.x107 - m.x177)**2 + (
    m.x197 - m.x267)**2) + 1 / sqrt((m.x17 - m.x88)**2 + (m.x107 - m.x178)**2
    + (m.x197 - m.x268)**2) + 1 / sqrt((m.x17 - m.x89)**2 + (m.x107 - m.x179)
    **2 + (m.x197 - m.x269)**2) + 1 / sqrt((m.x17 - m.x90)**2 + (m.x107 -
    m.x180)**2 + (m.x197 - m.x270)**2) + 1 / sqrt((m.x18 - m.x19)**2 + (m.x108
    - m.x109)**2 + (m.x198 - m.x199)**2) + 1 / sqrt((m.x18 - m.x20)**2 + (
    m.x108 - m.x110)**2 + (m.x198 - m.x200)**2) + 1 / sqrt((m.x18 - m.x21)**2
    + (m.x108 - m.x111)**2 + (m.x198 - m.x201)**2) + 1 / sqrt((m.x18 - m.x22)
    **2 + (m.x108 - m.x112)**2 + (m.x198 - m.x202)**2) + 1 / sqrt((m.x18 -
    m.x23)**2 + (m.x108 - m.x113)**2 + (m.x198 - m.x203)**2) + 1 / sqrt((m.x18
    - m.x24)**2 + (m.x108 - m.x114)**2 + (m.x198 - m.x204)**2) + 1 / sqrt((
    m.x18 - m.x25)**2 + (m.x108 - m.x115)**2 + (m.x198 - m.x205)**2) + 1 /
    sqrt((m.x18 - m.x26)**2 + (m.x108 - m.x116)**2 + (m.x198 - m.x206)**2) + 1
    / sqrt((m.x18 - m.x27)**2 + (m.x108 - m.x117)**2 + (m.x198 - m.x207)**2)
    + 1 / sqrt((m.x18 - m.x28)**2 + (m.x108 - m.x118)**2 + (m.x198 - m.x208)**
    2) + 1 / sqrt((m.x18 - m.x29)**2 + (m.x108 - m.x119)**2 + (m.x198 - m.x209)
    **2) + 1 / sqrt((m.x18 - m.x30)**2 + (m.x108 - m.x120)**2 + (m.x198 -
    m.x210)**2) + 1 / sqrt((m.x18 - m.x31)**2 + (m.x108 - m.x121)**2 + (m.x198
    - m.x211)**2) + 1 / sqrt((m.x18 - m.x32)**2 + (m.x108 - m.x122)**2 + (
    m.x198 - m.x212)**2) + 1 / sqrt((m.x18 - m.x33)**2 + (m.x108 - m.x123)**2
    + (m.x198 - m.x213)**2) + 1 / sqrt((m.x18 - m.x34)**2 + (m.x108 - m.x124)
    **2 + (m.x198 - m.x214)**2) + 1 / sqrt((m.x18 - m.x35)**2 + (m.x108 -
    m.x125)**2 + (m.x198 - m.x215)**2) + 1 / sqrt((m.x18 - m.x36)**2 + (m.x108
    - m.x126)**2 + (m.x198 - m.x216)**2) + 1 / sqrt((m.x18 - m.x37)**2 + (
    m.x108 - m.x127)**2 + (m.x198 - m.x217)**2) + 1 / sqrt((m.x18 - m.x38)**2
    + (m.x108 - m.x128)**2 + (m.x198 - m.x218)**2) + 1 / sqrt((m.x18 - m.x39)
    **2 + (m.x108 - m.x129)**2 + (m.x198 - m.x219)**2) + 1 / sqrt((m.x18 -
    m.x40)**2 + (m.x108 - m.x130)**2 + (m.x198 - m.x220)**2) + 1 / sqrt((m.x18
    - m.x41)**2 + (m.x108 - m.x131)**2 + (m.x198 - m.x221)**2) + 1 / sqrt((
    m.x18 - m.x42)**2 + (m.x108 - m.x132)**2 + (m.x198 - m.x222)**2) + 1 /
    sqrt((m.x18 - m.x43)**2 + (m.x108 - m.x133)**2 + (m.x198 - m.x223)**2) + 1
    / sqrt((m.x18 - m.x44)**2 + (m.x108 - m.x134)**2 + (m.x198 - m.x224)**2)
    + 1 / sqrt((m.x18 - m.x45)**2 + (m.x108 - m.x135)**2 + (m.x198 - m.x225)**
    2) + 1 / sqrt((m.x18 - m.x46)**2 + (m.x108 - m.x136)**2 + (m.x198 - m.x226)
    **2) + 1 / sqrt((m.x18 - m.x47)**2 + (m.x108 - m.x137)**2 + (m.x198 -
    m.x227)**2) + 1 / sqrt((m.x18 - m.x48)**2 + (m.x108 - m.x138)**2 + (m.x198
    - m.x228)**2) + 1 / sqrt((m.x18 - m.x49)**2 + (m.x108 - m.x139)**2 + (
    m.x198 - m.x229)**2) + 1 / sqrt((m.x18 - m.x50)**2 + (m.x108 - m.x140)**2
    + (m.x198 - m.x230)**2) + 1 / sqrt((m.x18 - m.x51)**2 + (m.x108 - m.x141)
    **2 + (m.x198 - m.x231)**2) + 1 / sqrt((m.x18 - m.x52)**2 + (m.x108 -
    m.x142)**2 + (m.x198 - m.x232)**2) + 1 / sqrt((m.x18 - m.x53)**2 + (m.x108
    - m.x143)**2 + (m.x198 - m.x233)**2) + 1 / sqrt((m.x18 - m.x54)**2 + (
    m.x108 - m.x144)**2 + (m.x198 - m.x234)**2) + 1 / sqrt((m.x18 - m.x55)**2
    + (m.x108 - m.x145)**2 + (m.x198 - m.x235)**2) + 1 / sqrt((m.x18 - m.x56)
    **2 + (m.x108 - m.x146)**2 + (m.x198 - m.x236)**2) + 1 / sqrt((m.x18 -
    m.x57)**2 + (m.x108 - m.x147)**2 + (m.x198 - m.x237)**2) + 1 / sqrt((m.x18
    - m.x58)**2 + (m.x108 - m.x148)**2 + (m.x198 - m.x238)**2) + 1 / sqrt((
    m.x18 - m.x59)**2 + (m.x108 - m.x149)**2 + (m.x198 - m.x239)**2) + 1 /
    sqrt((m.x18 - m.x60)**2 + (m.x108 - m.x150)**2 + (m.x198 - m.x240)**2) + 1
    / sqrt((m.x18 - m.x61)**2 + (m.x108 - m.x151)**2 + (m.x198 - m.x241)**2)
    + 1 / sqrt((m.x18 - m.x62)**2 + (m.x108 - m.x152)**2 + (m.x198 - m.x242)**
    2) + 1 / sqrt((m.x18 - m.x63)**2 + (m.x108 - m.x153)**2 + (m.x198 - m.x243)
    **2) + 1 / sqrt((m.x18 - m.x64)**2 + (m.x108 - m.x154)**2 + (m.x198 -
    m.x244)**2) + 1 / sqrt((m.x18 - m.x65)**2 + (m.x108 - m.x155)**2 + (m.x198
    - m.x245)**2) + 1 / sqrt((m.x18 - m.x66)**2 + (m.x108 - m.x156)**2 + (
    m.x198 - m.x246)**2) + 1 / sqrt((m.x18 - m.x67)**2 + (m.x108 - m.x157)**2
    + (m.x198 - m.x247)**2) + 1 / sqrt((m.x18 - m.x68)**2 + (m.x108 - m.x158)
    **2 + (m.x198 - m.x248)**2) + 1 / sqrt((m.x18 - m.x69)**2 + (m.x108 -
    m.x159)**2 + (m.x198 - m.x249)**2) + 1 / sqrt((m.x18 - m.x70)**2 + (m.x108
    - m.x160)**2 + (m.x198 - m.x250)**2) + 1 / sqrt((m.x18 - m.x71)**2 + (
    m.x108 - m.x161)**2 + (m.x198 - m.x251)**2) + 1 / sqrt((m.x18 - m.x72)**2
    + (m.x108 - m.x162)**2 + (m.x198 - m.x252)**2) + 1 / sqrt((m.x18 - m.x73)
    **2 + (m.x108 - m.x163)**2 + (m.x198 - m.x253)**2) + 1 / sqrt((m.x18 -
    m.x74)**2 + (m.x108 - m.x164)**2 + (m.x198 - m.x254)**2) + 1 / sqrt((m.x18
    - m.x75)**2 + (m.x108 - m.x165)**2 + (m.x198 - m.x255)**2) + 1 / sqrt((
    m.x18 - m.x76)**2 + (m.x108 - m.x166)**2 + (m.x198 - m.x256)**2) + 1 /
    sqrt((m.x18 - m.x77)**2 + (m.x108 - m.x167)**2 + (m.x198 - m.x257)**2) + 1
    / sqrt((m.x18 - m.x78)**2 + (m.x108 - m.x168)**2 + (m.x198 - m.x258)**2)
    + 1 / sqrt((m.x18 - m.x79)**2 + (m.x108 - m.x169)**2 + (m.x198 - m.x259)**
    2) + 1 / sqrt((m.x18 - m.x80)**2 + (m.x108 - m.x170)**2 + (m.x198 - m.x260)
    **2) + 1 / sqrt((m.x18 - m.x81)**2 + (m.x108 - m.x171)**2 + (m.x198 -
    m.x261)**2) + 1 / sqrt((m.x18 - m.x82)**2 + (m.x108 - m.x172)**2 + (m.x198
    - m.x262)**2) + 1 / sqrt((m.x18 - m.x83)**2 + (m.x108 - m.x173)**2 + (
    m.x198 - m.x263)**2) + 1 / sqrt((m.x18 - m.x84)**2 + (m.x108 - m.x174)**2
    + (m.x198 - m.x264)**2) + 1 / sqrt((m.x18 - m.x85)**2 + (m.x108 - m.x175)
    **2 + (m.x198 - m.x265)**2) + 1 / sqrt((m.x18 - m.x86)**2 + (m.x108 -
    m.x176)**2 + (m.x198 - m.x266)**2) + 1 / sqrt((m.x18 - m.x87)**2 + (m.x108
    - m.x177)**2 + (m.x198 - m.x267)**2) + 1 / sqrt((m.x18 - m.x88)**2 + (
    m.x108 - m.x178)**2 + (m.x198 - m.x268)**2) + 1 / sqrt((m.x18 - m.x89)**2
    + (m.x108 - m.x179)**2 + (m.x198 - m.x269)**2) + 1 / sqrt((m.x18 - m.x90)
    **2 + (m.x108 - m.x180)**2 + (m.x198 - m.x270)**2) + 1 / sqrt((m.x19 -
    m.x20)**2 + (m.x109 - m.x110)**2 + (m.x199 - m.x200)**2) + 1 / sqrt((m.x19
    - m.x21)**2 + (m.x109 - m.x111)**2 + (m.x199 - m.x201)**2) + 1 / sqrt((
    m.x19 - m.x22)**2 + (m.x109 - m.x112)**2 + (m.x199 - m.x202)**2) + 1 /
    sqrt((m.x19 - m.x23)**2 + (m.x109 - m.x113)**2 + (m.x199 - m.x203)**2) + 1
    / sqrt((m.x19 - m.x24)**2 + (m.x109 - m.x114)**2 + (m.x199 - m.x204)**2)
    + 1 / sqrt((m.x19 - m.x25)**2 + (m.x109 - m.x115)**2 + (m.x199 - m.x205)**
    2) + 1 / sqrt((m.x19 - m.x26)**2 + (m.x109 - m.x116)**2 + (m.x199 - m.x206)
    **2) + 1 / sqrt((m.x19 - m.x27)**2 + (m.x109 - m.x117)**2 + (m.x199 -
    m.x207)**2) + 1 / sqrt((m.x19 - m.x28)**2 + (m.x109 - m.x118)**2 + (m.x199
    - m.x208)**2) + 1 / sqrt((m.x19 - m.x29)**2 + (m.x109 - m.x119)**2 + (
    m.x199 - m.x209)**2) + 1 / sqrt((m.x19 - m.x30)**2 + (m.x109 - m.x120)**2
    + (m.x199 - m.x210)**2) + 1 / sqrt((m.x19 - m.x31)**2 + (m.x109 - m.x121)
    **2 + (m.x199 - m.x211)**2) + 1 / sqrt((m.x19 - m.x32)**2 + (m.x109 -
    m.x122)**2 + (m.x199 - m.x212)**2) + 1 / sqrt((m.x19 - m.x33)**2 + (m.x109
    - m.x123)**2 + (m.x199 - m.x213)**2) + 1 / sqrt((m.x19 - m.x34)**2 + (
    m.x109 - m.x124)**2 + (m.x199 - m.x214)**2) + 1 / sqrt((m.x19 - m.x35)**2
    + (m.x109 - m.x125)**2 + (m.x199 - m.x215)**2) + 1 / sqrt((m.x19 - m.x36)
    **2 + (m.x109 - m.x126)**2 + (m.x199 - m.x216)**2) + 1 / sqrt((m.x19 -
    m.x37)**2 + (m.x109 - m.x127)**2 + (m.x199 - m.x217)**2) + 1 / sqrt((m.x19
    - m.x38)**2 + (m.x109 - m.x128)**2 + (m.x199 - m.x218)**2) + 1 / sqrt((
    m.x19 - m.x39)**2 + (m.x109 - m.x129)**2 + (m.x199 - m.x219)**2) + 1 /
    sqrt((m.x19 - m.x40)**2 + (m.x109 - m.x130)**2 + (m.x199 - m.x220)**2) + 1
    / sqrt((m.x19 - m.x41)**2 + (m.x109 - m.x131)**2 + (m.x199 - m.x221)**2)
    + 1 / sqrt((m.x19 - m.x42)**2 + (m.x109 - m.x132)**2 + (m.x199 - m.x222)**
    2) + 1 / sqrt((m.x19 - m.x43)**2 + (m.x109 - m.x133)**2 + (m.x199 - m.x223)
    **2) + 1 / sqrt((m.x19 - m.x44)**2 + (m.x109 - m.x134)**2 + (m.x199 -
    m.x224)**2) + 1 / sqrt((m.x19 - m.x45)**2 + (m.x109 - m.x135)**2 + (m.x199
    - m.x225)**2) + 1 / sqrt((m.x19 - m.x46)**2 + (m.x109 - m.x136)**2 + (
    m.x199 - m.x226)**2) + 1 / sqrt((m.x19 - m.x47)**2 + (m.x109 - m.x137)**2
    + (m.x199 - m.x227)**2) + 1 / sqrt((m.x19 - m.x48)**2 + (m.x109 - m.x138)
    **2 + (m.x199 - m.x228)**2) + 1 / sqrt((m.x19 - m.x49)**2 + (m.x109 -
    m.x139)**2 + (m.x199 - m.x229)**2) + 1 / sqrt((m.x19 - m.x50)**2 + (m.x109
    - m.x140)**2 + (m.x199 - m.x230)**2) + 1 / sqrt((m.x19 - m.x51)**2 + (
    m.x109 - m.x141)**2 + (m.x199 - m.x231)**2) + 1 / sqrt((m.x19 - m.x52)**2
    + (m.x109 - m.x142)**2 + (m.x199 - m.x232)**2) + 1 / sqrt((m.x19 - m.x53)
    **2 + (m.x109 - m.x143)**2 + (m.x199 - m.x233)**2) + 1 / sqrt((m.x19 -
    m.x54)**2 + (m.x109 - m.x144)**2 + (m.x199 - m.x234)**2) + 1 / sqrt((m.x19
    - m.x55)**2 + (m.x109 - m.x145)**2 + (m.x199 - m.x235)**2) + 1 / sqrt((
    m.x19 - m.x56)**2 + (m.x109 - m.x146)**2 + (m.x199 - m.x236)**2) + 1 /
    sqrt((m.x19 - m.x57)**2 + (m.x109 - m.x147)**2 + (m.x199 - m.x237)**2) + 1
    / sqrt((m.x19 - m.x58)**2 + (m.x109 - m.x148)**2 + (m.x199 - m.x238)**2)
    + 1 / sqrt((m.x19 - m.x59)**2 + (m.x109 - m.x149)**2 + (m.x199 - m.x239)**
    2) + 1 / sqrt((m.x19 - m.x60)**2 + (m.x109 - m.x150)**2 + (m.x199 - m.x240)
    **2) + 1 / sqrt((m.x19 - m.x61)**2 + (m.x109 - m.x151)**2 + (m.x199 -
    m.x241)**2) + 1 / sqrt((m.x19 - m.x62)**2 + (m.x109 - m.x152)**2 + (m.x199
    - m.x242)**2) + 1 / sqrt((m.x19 - m.x63)**2 + (m.x109 - m.x153)**2 + (
    m.x199 - m.x243)**2) + 1 / sqrt((m.x19 - m.x64)**2 + (m.x109 - m.x154)**2
    + (m.x199 - m.x244)**2) + 1 / sqrt((m.x19 - m.x65)**2 + (m.x109 - m.x155)
    **2 + (m.x199 - m.x245)**2) + 1 / sqrt((m.x19 - m.x66)**2 + (m.x109 -
    m.x156)**2 + (m.x199 - m.x246)**2) + 1 / sqrt((m.x19 - m.x67)**2 + (m.x109
    - m.x157)**2 + (m.x199 - m.x247)**2) + 1 / sqrt((m.x19 - m.x68)**2 + (
    m.x109 - m.x158)**2 + (m.x199 - m.x248)**2) + 1 / sqrt((m.x19 - m.x69)**2
    + (m.x109 - m.x159)**2 + (m.x199 - m.x249)**2) + 1 / sqrt((m.x19 - m.x70)
    **2 + (m.x109 - m.x160)**2 + (m.x199 - m.x250)**2) + 1 / sqrt((m.x19 -
    m.x71)**2 + (m.x109 - m.x161)**2 + (m.x199 - m.x251)**2) + 1 / sqrt((m.x19
    - m.x72)**2 + (m.x109 - m.x162)**2 + (m.x199 - m.x252)**2) + 1 / sqrt((
    m.x19 - m.x73)**2 + (m.x109 - m.x163)**2 + (m.x199 - m.x253)**2) + 1 /
    sqrt((m.x19 - m.x74)**2 + (m.x109 - m.x164)**2 + (m.x199 - m.x254)**2) + 1
    / sqrt((m.x19 - m.x75)**2 + (m.x109 - m.x165)**2 + (m.x199 - m.x255)**2)
    + 1 / sqrt((m.x19 - m.x76)**2 + (m.x109 - m.x166)**2 + (m.x199 - m.x256)**
    2) + 1 / sqrt((m.x19 - m.x77)**2 + (m.x109 - m.x167)**2 + (m.x199 - m.x257)
    **2) + 1 / sqrt((m.x19 - m.x78)**2 + (m.x109 - m.x168)**2 + (m.x199 -
    m.x258)**2) + 1 / sqrt((m.x19 - m.x79)**2 + (m.x109 - m.x169)**2 + (m.x199
    - m.x259)**2) + 1 / sqrt((m.x19 - m.x80)**2 + (m.x109 - m.x170)**2 + (
    m.x199 - m.x260)**2) + 1 / sqrt((m.x19 - m.x81)**2 + (m.x109 - m.x171)**2
    + (m.x199 - m.x261)**2) + 1 / sqrt((m.x19 - m.x82)**2 + (m.x109 - m.x172)
    **2 + (m.x199 - m.x262)**2) + 1 / sqrt((m.x19 - m.x83)**2 + (m.x109 -
    m.x173)**2 + (m.x199 - m.x263)**2) + 1 / sqrt((m.x19 - m.x84)**2 + (m.x109
    - m.x174)**2 + (m.x199 - m.x264)**2) + 1 / sqrt((m.x19 - m.x85)**2 + (
    m.x109 - m.x175)**2 + (m.x199 - m.x265)**2) + 1 / sqrt((m.x19 - m.x86)**2
    + (m.x109 - m.x176)**2 + (m.x199 - m.x266)**2) + 1 / sqrt((m.x19 - m.x87)
    **2 + (m.x109 - m.x177)**2 + (m.x199 - m.x267)**2) + 1 / sqrt((m.x19 -
    m.x88)**2 + (m.x109 - m.x178)**2 + (m.x199 - m.x268)**2) + 1 / sqrt((m.x19
    - m.x89)**2 + (m.x109 - m.x179)**2 + (m.x199 - m.x269)**2) + 1 / sqrt((
    m.x19 - m.x90)**2 + (m.x109 - m.x180)**2 + (m.x199 - m.x270)**2) + 1 /
    sqrt((m.x20 - m.x21)**2 + (m.x110 - m.x111)**2 + (m.x200 - m.x201)**2) + 1
    / sqrt((m.x20 - m.x22)**2 + (m.x110 - m.x112)**2 + (m.x200 - m.x202)**2)
    + 1 / sqrt((m.x20 - m.x23)**2 + (m.x110 - m.x113)**2 + (m.x200 - m.x203)**
    2) + 1 / sqrt((m.x20 - m.x24)**2 + (m.x110 - m.x114)**2 + (m.x200 - m.x204)
    **2) + 1 / sqrt((m.x20 - m.x25)**2 + (m.x110 - m.x115)**2 + (m.x200 -
    m.x205)**2) + 1 / sqrt((m.x20 - m.x26)**2 + (m.x110 - m.x116)**2 + (m.x200
    - m.x206)**2) + 1 / sqrt((m.x20 - m.x27)**2 + (m.x110 - m.x117)**2 + (
    m.x200 - m.x207)**2) + 1 / sqrt((m.x20 - m.x28)**2 + (m.x110 - m.x118)**2
    + (m.x200 - m.x208)**2) + 1 / sqrt((m.x20 - m.x29)**2 + (m.x110 - m.x119)
    **2 + (m.x200 - m.x209)**2) + 1 / sqrt((m.x20 - m.x30)**2 + (m.x110 -
    m.x120)**2 + (m.x200 - m.x210)**2) + 1 / sqrt((m.x20 - m.x31)**2 + (m.x110
    - m.x121)**2 + (m.x200 - m.x211)**2) + 1 / sqrt((m.x20 - m.x32)**2 + (
    m.x110 - m.x122)**2 + (m.x200 - m.x212)**2) + 1 / sqrt((m.x20 - m.x33)**2
    + (m.x110 - m.x123)**2 + (m.x200 - m.x213)**2) + 1 / sqrt((m.x20 - m.x34)
    **2 + (m.x110 - m.x124)**2 + (m.x200 - m.x214)**2) + 1 / sqrt((m.x20 -
    m.x35)**2 + (m.x110 - m.x125)**2 + (m.x200 - m.x215)**2) + 1 / sqrt((m.x20
    - m.x36)**2 + (m.x110 - m.x126)**2 + (m.x200 - m.x216)**2) + 1 / sqrt((
    m.x20 - m.x37)**2 + (m.x110 - m.x127)**2 + (m.x200 - m.x217)**2) + 1 /
    sqrt((m.x20 - m.x38)**2 + (m.x110 - m.x128)**2 + (m.x200 - m.x218)**2) + 1
    / sqrt((m.x20 - m.x39)**2 + (m.x110 - m.x129)**2 + (m.x200 - m.x219)**2)
    + 1 / sqrt((m.x20 - m.x40)**2 + (m.x110 - m.x130)**2 + (m.x200 - m.x220)**
    2) + 1 / sqrt((m.x20 - m.x41)**2 + (m.x110 - m.x131)**2 + (m.x200 - m.x221)
    **2) + 1 / sqrt((m.x20 - m.x42)**2 + (m.x110 - m.x132)**2 + (m.x200 -
    m.x222)**2) + 1 / sqrt((m.x20 - m.x43)**2 + (m.x110 - m.x133)**2 + (m.x200
    - m.x223)**2) + 1 / sqrt((m.x20 - m.x44)**2 + (m.x110 - m.x134)**2 + (
    m.x200 - m.x224)**2) + 1 / sqrt((m.x20 - m.x45)**2 + (m.x110 - m.x135)**2
    + (m.x200 - m.x225)**2) + 1 / sqrt((m.x20 - m.x46)**2 + (m.x110 - m.x136)
    **2 + (m.x200 - m.x226)**2) + 1 / sqrt((m.x20 - m.x47)**2 + (m.x110 -
    m.x137)**2 + (m.x200 - m.x227)**2) + 1 / sqrt((m.x20 - m.x48)**2 + (m.x110
    - m.x138)**2 + (m.x200 - m.x228)**2) + 1 / sqrt((m.x20 - m.x49)**2 + (
    m.x110 - m.x139)**2 + (m.x200 - m.x229)**2) + 1 / sqrt((m.x20 - m.x50)**2
    + (m.x110 - m.x140)**2 + (m.x200 - m.x230)**2) + 1 / sqrt((m.x20 - m.x51)
    **2 + (m.x110 - m.x141)**2 + (m.x200 - m.x231)**2) + 1 / sqrt((m.x20 -
    m.x52)**2 + (m.x110 - m.x142)**2 + (m.x200 - m.x232)**2) + 1 / sqrt((m.x20
    - m.x53)**2 + (m.x110 - m.x143)**2 + (m.x200 - m.x233)**2) + 1 / sqrt((
    m.x20 - m.x54)**2 + (m.x110 - m.x144)**2 + (m.x200 - m.x234)**2) + 1 /
    sqrt((m.x20 - m.x55)**2 + (m.x110 - m.x145)**2 + (m.x200 - m.x235)**2) + 1
    / sqrt((m.x20 - m.x56)**2 + (m.x110 - m.x146)**2 + (m.x200 - m.x236)**2)
    + 1 / sqrt((m.x20 - m.x57)**2 + (m.x110 - m.x147)**2 + (m.x200 - m.x237)**
    2) + 1 / sqrt((m.x20 - m.x58)**2 + (m.x110 - m.x148)**2 + (m.x200 - m.x238)
    **2) + 1 / sqrt((m.x20 - m.x59)**2 + (m.x110 - m.x149)**2 + (m.x200 -
    m.x239)**2) + 1 / sqrt((m.x20 - m.x60)**2 + (m.x110 - m.x150)**2 + (m.x200
    - m.x240)**2) + 1 / sqrt((m.x20 - m.x61)**2 + (m.x110 - m.x151)**2 + (
    m.x200 - m.x241)**2) + 1 / sqrt((m.x20 - m.x62)**2 + (m.x110 - m.x152)**2
    + (m.x200 - m.x242)**2) + 1 / sqrt((m.x20 - m.x63)**2 + (m.x110 - m.x153)
    **2 + (m.x200 - m.x243)**2) + 1 / sqrt((m.x20 - m.x64)**2 + (m.x110 -
    m.x154)**2 + (m.x200 - m.x244)**2) + 1 / sqrt((m.x20 - m.x65)**2 + (m.x110
    - m.x155)**2 + (m.x200 - m.x245)**2) + 1 / sqrt((m.x20 - m.x66)**2 + (
    m.x110 - m.x156)**2 + (m.x200 - m.x246)**2) + 1 / sqrt((m.x20 - m.x67)**2
    + (m.x110 - m.x157)**2 + (m.x200 - m.x247)**2) + 1 / sqrt((m.x20 - m.x68)
    **2 + (m.x110 - m.x158)**2 + (m.x200 - m.x248)**2) + 1 / sqrt((m.x20 -
    m.x69)**2 + (m.x110 - m.x159)**2 + (m.x200 - m.x249)**2) + 1 / sqrt((m.x20
    - m.x70)**2 + (m.x110 - m.x160)**2 + (m.x200 - m.x250)**2) + 1 / sqrt((
    m.x20 - m.x71)**2 + (m.x110 - m.x161)**2 + (m.x200 - m.x251)**2) + 1 /
    sqrt((m.x20 - m.x72)**2 + (m.x110 - m.x162)**2 + (m.x200 - m.x252)**2) + 1
    / sqrt((m.x20 - m.x73)**2 + (m.x110 - m.x163)**2 + (m.x200 - m.x253)**2)
    + 1 / sqrt((m.x20 - m.x74)**2 + (m.x110 - m.x164)**2 + (m.x200 - m.x254)**
    2) + 1 / sqrt((m.x20 - m.x75)**2 + (m.x110 - m.x165)**2 + (m.x200 - m.x255)
    **2) + 1 / sqrt((m.x20 - m.x76)**2 + (m.x110 - m.x166)**2 + (m.x200 -
    m.x256)**2) + 1 / sqrt((m.x20 - m.x77)**2 + (m.x110 - m.x167)**2 + (m.x200
    - m.x257)**2) + 1 / sqrt((m.x20 - m.x78)**2 + (m.x110 - m.x168)**2 + (
    m.x200 - m.x258)**2) + 1 / sqrt((m.x20 - m.x79)**2 + (m.x110 - m.x169)**2
    + (m.x200 - m.x259)**2) + 1 / sqrt((m.x20 - m.x80)**2 + (m.x110 - m.x170)
    **2 + (m.x200 - m.x260)**2) + 1 / sqrt((m.x20 - m.x81)**2 + (m.x110 -
    m.x171)**2 + (m.x200 - m.x261)**2) + 1 / sqrt((m.x20 - m.x82)**2 + (m.x110
    - m.x172)**2 + (m.x200 - m.x262)**2) + 1 / sqrt((m.x20 - m.x83)**2 + (
    m.x110 - m.x173)**2 + (m.x200 - m.x263)**2) + 1 / sqrt((m.x20 - m.x84)**2
    + (m.x110 - m.x174)**2 + (m.x200 - m.x264)**2) + 1 / sqrt((m.x20 - m.x85)
    **2 + (m.x110 - m.x175)**2 + (m.x200 - m.x265)**2) + 1 / sqrt((m.x20 -
    m.x86)**2 + (m.x110 - m.x176)**2 + (m.x200 - m.x266)**2) + 1 / sqrt((m.x20
    - m.x87)**2 + (m.x110 - m.x177)**2 + (m.x200 - m.x267)**2) + 1 / sqrt((
    m.x20 - m.x88)**2 + (m.x110 - m.x178)**2 + (m.x200 - m.x268)**2) + 1 /
    sqrt((m.x20 - m.x89)**2 + (m.x110 - m.x179)**2 + (m.x200 - m.x269)**2) + 1
    / sqrt((m.x20 - m.x90)**2 + (m.x110 - m.x180)**2 + (m.x200 - m.x270)**2)
    + 1 / sqrt((m.x21 - m.x22)**2 + (m.x111 - m.x112)**2 + (m.x201 - m.x202)**
    2) + 1 / sqrt((m.x21 - m.x23)**2 + (m.x111 - m.x113)**2 + (m.x201 - m.x203)
    **2) + 1 / sqrt((m.x21 - m.x24)**2 + (m.x111 - m.x114)**2 + (m.x201 -
    m.x204)**2) + 1 / sqrt((m.x21 - m.x25)**2 + (m.x111 - m.x115)**2 + (m.x201
    - m.x205)**2) + 1 / sqrt((m.x21 - m.x26)**2 + (m.x111 - m.x116)**2 + (
    m.x201 - m.x206)**2) + 1 / sqrt((m.x21 - m.x27)**2 + (m.x111 - m.x117)**2
    + (m.x201 - m.x207)**2) + 1 / sqrt((m.x21 - m.x28)**2 + (m.x111 - m.x118)
    **2 + (m.x201 - m.x208)**2) + 1 / sqrt((m.x21 - m.x29)**2 + (m.x111 -
    m.x119)**2 + (m.x201 - m.x209)**2) + 1 / sqrt((m.x21 - m.x30)**2 + (m.x111
    - m.x120)**2 + (m.x201 - m.x210)**2) + 1 / sqrt((m.x21 - m.x31)**2 + (
    m.x111 - m.x121)**2 + (m.x201 - m.x211)**2) + 1 / sqrt((m.x21 - m.x32)**2
    + (m.x111 - m.x122)**2 + (m.x201 - m.x212)**2) + 1 / sqrt((m.x21 - m.x33)
    **2 + (m.x111 - m.x123)**2 + (m.x201 - m.x213)**2) + 1 / sqrt((m.x21 -
    m.x34)**2 + (m.x111 - m.x124)**2 + (m.x201 - m.x214)**2) + 1 / sqrt((m.x21
    - m.x35)**2 + (m.x111 - m.x125)**2 + (m.x201 - m.x215)**2) + 1 / sqrt((
    m.x21 - m.x36)**2 + (m.x111 - m.x126)**2 + (m.x201 - m.x216)**2) + 1 /
    sqrt((m.x21 - m.x37)**2 + (m.x111 - m.x127)**2 + (m.x201 - m.x217)**2) + 1
    / sqrt((m.x21 - m.x38)**2 + (m.x111 - m.x128)**2 + (m.x201 - m.x218)**2)
    + 1 / sqrt((m.x21 - m.x39)**2 + (m.x111 - m.x129)**2 + (m.x201 - m.x219)**
    2) + 1 / sqrt((m.x21 - m.x40)**2 + (m.x111 - m.x130)**2 + (m.x201 - m.x220)
    **2) + 1 / sqrt((m.x21 - m.x41)**2 + (m.x111 - m.x131)**2 + (m.x201 -
    m.x221)**2) + 1 / sqrt((m.x21 - m.x42)**2 + (m.x111 - m.x132)**2 + (m.x201
    - m.x222)**2) + 1 / sqrt((m.x21 - m.x43)**2 + (m.x111 - m.x133)**2 + (
    m.x201 - m.x223)**2) + 1 / sqrt((m.x21 - m.x44)**2 + (m.x111 - m.x134)**2
    + (m.x201 - m.x224)**2) + 1 / sqrt((m.x21 - m.x45)**2 + (m.x111 - m.x135)
    **2 + (m.x201 - m.x225)**2) + 1 / sqrt((m.x21 - m.x46)**2 + (m.x111 -
    m.x136)**2 + (m.x201 - m.x226)**2) + 1 / sqrt((m.x21 - m.x47)**2 + (m.x111
    - m.x137)**2 + (m.x201 - m.x227)**2) + 1 / sqrt((m.x21 - m.x48)**2 + (
    m.x111 - m.x138)**2 + (m.x201 - m.x228)**2) + 1 / sqrt((m.x21 - m.x49)**2
    + (m.x111 - m.x139)**2 + (m.x201 - m.x229)**2) + 1 / sqrt((m.x21 - m.x50)
    **2 + (m.x111 - m.x140)**2 + (m.x201 - m.x230)**2) + 1 / sqrt((m.x21 -
    m.x51)**2 + (m.x111 - m.x141)**2 + (m.x201 - m.x231)**2) + 1 / sqrt((m.x21
    - m.x52)**2 + (m.x111 - m.x142)**2 + (m.x201 - m.x232)**2) + 1 / sqrt((
    m.x21 - m.x53)**2 + (m.x111 - m.x143)**2 + (m.x201 - m.x233)**2) + 1 /
    sqrt((m.x21 - m.x54)**2 + (m.x111 - m.x144)**2 + (m.x201 - m.x234)**2) + 1
    / sqrt((m.x21 - m.x55)**2 + (m.x111 - m.x145)**2 + (m.x201 - m.x235)**2)
    + 1 / sqrt((m.x21 - m.x56)**2 + (m.x111 - m.x146)**2 + (m.x201 - m.x236)**
    2) + 1 / sqrt((m.x21 - m.x57)**2 + (m.x111 - m.x147)**2 + (m.x201 - m.x237)
    **2) + 1 / sqrt((m.x21 - m.x58)**2 + (m.x111 - m.x148)**2 + (m.x201 -
    m.x238)**2) + 1 / sqrt((m.x21 - m.x59)**2 + (m.x111 - m.x149)**2 + (m.x201
    - m.x239)**2) + 1 / sqrt((m.x21 - m.x60)**2 + (m.x111 - m.x150)**2 + (
    m.x201 - m.x240)**2) + 1 / sqrt((m.x21 - m.x61)**2 + (m.x111 - m.x151)**2
    + (m.x201 - m.x241)**2) + 1 / sqrt((m.x21 - m.x62)**2 + (m.x111 - m.x152)
    **2 + (m.x201 - m.x242)**2) + 1 / sqrt((m.x21 - m.x63)**2 + (m.x111 -
    m.x153)**2 + (m.x201 - m.x243)**2) + 1 / sqrt((m.x21 - m.x64)**2 + (m.x111
    - m.x154)**2 + (m.x201 - m.x244)**2) + 1 / sqrt((m.x21 - m.x65)**2 + (
    m.x111 - m.x155)**2 + (m.x201 - m.x245)**2) + 1 / sqrt((m.x21 - m.x66)**2
    + (m.x111 - m.x156)**2 + (m.x201 - m.x246)**2) + 1 / sqrt((m.x21 - m.x67)
    **2 + (m.x111 - m.x157)**2 + (m.x201 - m.x247)**2) + 1 / sqrt((m.x21 -
    m.x68)**2 + (m.x111 - m.x158)**2 + (m.x201 - m.x248)**2) + 1 / sqrt((m.x21
    - m.x69)**2 + (m.x111 - m.x159)**2 + (m.x201 - m.x249)**2) + 1 / sqrt((
    m.x21 - m.x70)**2 + (m.x111 - m.x160)**2 + (m.x201 - m.x250)**2) + 1 /
    sqrt((m.x21 - m.x71)**2 + (m.x111 - m.x161)**2 + (m.x201 - m.x251)**2) + 1
    / sqrt((m.x21 - m.x72)**2 + (m.x111 - m.x162)**2 + (m.x201 - m.x252)**2)
    + 1 / sqrt((m.x21 - m.x73)**2 + (m.x111 - m.x163)**2 + (m.x201 - m.x253)**
    2) + 1 / sqrt((m.x21 - m.x74)**2 + (m.x111 - m.x164)**2 + (m.x201 - m.x254)
    **2) + 1 / sqrt((m.x21 - m.x75)**2 + (m.x111 - m.x165)**2 + (m.x201 -
    m.x255)**2) + 1 / sqrt((m.x21 - m.x76)**2 + (m.x111 - m.x166)**2 + (m.x201
    - m.x256)**2) + 1 / sqrt((m.x21 - m.x77)**2 + (m.x111 - m.x167)**2 + (
    m.x201 - m.x257)**2) + 1 / sqrt((m.x21 - m.x78)**2 + (m.x111 - m.x168)**2
    + (m.x201 - m.x258)**2) + 1 / sqrt((m.x21 - m.x79)**2 + (m.x111 - m.x169)
    **2 + (m.x201 - m.x259)**2) + 1 / sqrt((m.x21 - m.x80)**2 + (m.x111 -
    m.x170)**2 + (m.x201 - m.x260)**2) + 1 / sqrt((m.x21 - m.x81)**2 + (m.x111
    - m.x171)**2 + (m.x201 - m.x261)**2) + 1 / sqrt((m.x21 - m.x82)**2 + (
    m.x111 - m.x172)**2 + (m.x201 - m.x262)**2) + 1 / sqrt((m.x21 - m.x83)**2
    + (m.x111 - m.x173)**2 + (m.x201 - m.x263)**2) + 1 / sqrt((m.x21 - m.x84)
    **2 + (m.x111 - m.x174)**2 + (m.x201 - m.x264)**2) + 1 / sqrt((m.x21 -
    m.x85)**2 + (m.x111 - m.x175)**2 + (m.x201 - m.x265)**2) + 1 / sqrt((m.x21
    - m.x86)**2 + (m.x111 - m.x176)**2 + (m.x201 - m.x266)**2) + 1 / sqrt((
    m.x21 - m.x87)**2 + (m.x111 - m.x177)**2 + (m.x201 - m.x267)**2) + 1 /
    sqrt((m.x21 - m.x88)**2 + (m.x111 - m.x178)**2 + (m.x201 - m.x268)**2) + 1
    / sqrt((m.x21 - m.x89)**2 + (m.x111 - m.x179)**2 + (m.x201 - m.x269)**2)
    + 1 / sqrt((m.x21 - m.x90)**2 + (m.x111 - m.x180)**2 + (m.x201 - m.x270)**
    2) + 1 / sqrt((m.x22 - m.x23)**2 + (m.x112 - m.x113)**2 + (m.x202 - m.x203)
    **2) + 1 / sqrt((m.x22 - m.x24)**2 + (m.x112 - m.x114)**2 + (m.x202 -
    m.x204)**2) + 1 / sqrt((m.x22 - m.x25)**2 + (m.x112 - m.x115)**2 + (m.x202
    - m.x205)**2) + 1 / sqrt((m.x22 - m.x26)**2 + (m.x112 - m.x116)**2 + (
    m.x202 - m.x206)**2) + 1 / sqrt((m.x22 - m.x27)**2 + (m.x112 - m.x117)**2
    + (m.x202 - m.x207)**2) + 1 / sqrt((m.x22 - m.x28)**2 + (m.x112 - m.x118)
    **2 + (m.x202 - m.x208)**2) + 1 / sqrt((m.x22 - m.x29)**2 + (m.x112 -
    m.x119)**2 + (m.x202 - m.x209)**2) + 1 / sqrt((m.x22 - m.x30)**2 + (m.x112
    - m.x120)**2 + (m.x202 - m.x210)**2) + 1 / sqrt((m.x22 - m.x31)**2 + (
    m.x112 - m.x121)**2 + (m.x202 - m.x211)**2) + 1 / sqrt((m.x22 - m.x32)**2
    + (m.x112 - m.x122)**2 + (m.x202 - m.x212)**2) + 1 / sqrt((m.x22 - m.x33)
    **2 + (m.x112 - m.x123)**2 + (m.x202 - m.x213)**2) + 1 / sqrt((m.x22 -
    m.x34)**2 + (m.x112 - m.x124)**2 + (m.x202 - m.x214)**2) + 1 / sqrt((m.x22
    - m.x35)**2 + (m.x112 - m.x125)**2 + (m.x202 - m.x215)**2) + 1 / sqrt((
    m.x22 - m.x36)**2 + (m.x112 - m.x126)**2 + (m.x202 - m.x216)**2) + 1 /
    sqrt((m.x22 - m.x37)**2 + (m.x112 - m.x127)**2 + (m.x202 - m.x217)**2) + 1
    / sqrt((m.x22 - m.x38)**2 + (m.x112 - m.x128)**2 + (m.x202 - m.x218)**2)
    + 1 / sqrt((m.x22 - m.x39)**2 + (m.x112 - m.x129)**2 + (m.x202 - m.x219)**
    2) + 1 / sqrt((m.x22 - m.x40)**2 + (m.x112 - m.x130)**2 + (m.x202 - m.x220)
    **2) + 1 / sqrt((m.x22 - m.x41)**2 + (m.x112 - m.x131)**2 + (m.x202 -
    m.x221)**2) + 1 / sqrt((m.x22 - m.x42)**2 + (m.x112 - m.x132)**2 + (m.x202
    - m.x222)**2) + 1 / sqrt((m.x22 - m.x43)**2 + (m.x112 - m.x133)**2 + (
    m.x202 - m.x223)**2) + 1 / sqrt((m.x22 - m.x44)**2 + (m.x112 - m.x134)**2
    + (m.x202 - m.x224)**2) + 1 / sqrt((m.x22 - m.x45)**2 + (m.x112 - m.x135)
    **2 + (m.x202 - m.x225)**2) + 1 / sqrt((m.x22 - m.x46)**2 + (m.x112 -
    m.x136)**2 + (m.x202 - m.x226)**2) + 1 / sqrt((m.x22 - m.x47)**2 + (m.x112
    - m.x137)**2 + (m.x202 - m.x227)**2) + 1 / sqrt((m.x22 - m.x48)**2 + (
    m.x112 - m.x138)**2 + (m.x202 - m.x228)**2) + 1 / sqrt((m.x22 - m.x49)**2
    + (m.x112 - m.x139)**2 + (m.x202 - m.x229)**2) + 1 / sqrt((m.x22 - m.x50)
    **2 + (m.x112 - m.x140)**2 + (m.x202 - m.x230)**2) + 1 / sqrt((m.x22 -
    m.x51)**2 + (m.x112 - m.x141)**2 + (m.x202 - m.x231)**2) + 1 / sqrt((m.x22
    - m.x52)**2 + (m.x112 - m.x142)**2 + (m.x202 - m.x232)**2) + 1 / sqrt((
    m.x22 - m.x53)**2 + (m.x112 - m.x143)**2 + (m.x202 - m.x233)**2) + 1 /
    sqrt((m.x22 - m.x54)**2 + (m.x112 - m.x144)**2 + (m.x202 - m.x234)**2) + 1
    / sqrt((m.x22 - m.x55)**2 + (m.x112 - m.x145)**2 + (m.x202 - m.x235)**2)
    + 1 / sqrt((m.x22 - m.x56)**2 + (m.x112 - m.x146)**2 + (m.x202 - m.x236)**
    2) + 1 / sqrt((m.x22 - m.x57)**2 + (m.x112 - m.x147)**2 + (m.x202 - m.x237)
    **2) + 1 / sqrt((m.x22 - m.x58)**2 + (m.x112 - m.x148)**2 + (m.x202 -
    m.x238)**2) + 1 / sqrt((m.x22 - m.x59)**2 + (m.x112 - m.x149)**2 + (m.x202
    - m.x239)**2) + 1 / sqrt((m.x22 - m.x60)**2 + (m.x112 - m.x150)**2 + (
    m.x202 - m.x240)**2) + 1 / sqrt((m.x22 - m.x61)**2 + (m.x112 - m.x151)**2
    + (m.x202 - m.x241)**2) + 1 / sqrt((m.x22 - m.x62)**2 + (m.x112 - m.x152)
    **2 + (m.x202 - m.x242)**2) + 1 / sqrt((m.x22 - m.x63)**2 + (m.x112 -
    m.x153)**2 + (m.x202 - m.x243)**2) + 1 / sqrt((m.x22 - m.x64)**2 + (m.x112
    - m.x154)**2 + (m.x202 - m.x244)**2) + 1 / sqrt((m.x22 - m.x65)**2 + (
    m.x112 - m.x155)**2 + (m.x202 - m.x245)**2) + 1 / sqrt((m.x22 - m.x66)**2
    + (m.x112 - m.x156)**2 + (m.x202 - m.x246)**2) + 1 / sqrt((m.x22 - m.x67)
    **2 + (m.x112 - m.x157)**2 + (m.x202 - m.x247)**2) + 1 / sqrt((m.x22 -
    m.x68)**2 + (m.x112 - m.x158)**2 + (m.x202 - m.x248)**2) + 1 / sqrt((m.x22
    - m.x69)**2 + (m.x112 - m.x159)**2 + (m.x202 - m.x249)**2) + 1 / sqrt((
    m.x22 - m.x70)**2 + (m.x112 - m.x160)**2 + (m.x202 - m.x250)**2) + 1 /
    sqrt((m.x22 - m.x71)**2 + (m.x112 - m.x161)**2 + (m.x202 - m.x251)**2) + 1
    / sqrt((m.x22 - m.x72)**2 + (m.x112 - m.x162)**2 + (m.x202 - m.x252)**2)
    + 1 / sqrt((m.x22 - m.x73)**2 + (m.x112 - m.x163)**2 + (m.x202 - m.x253)**
    2) + 1 / sqrt((m.x22 - m.x74)**2 + (m.x112 - m.x164)**2 + (m.x202 - m.x254)
    **2) + 1 / sqrt((m.x22 - m.x75)**2 + (m.x112 - m.x165)**2 + (m.x202 -
    m.x255)**2) + 1 / sqrt((m.x22 - m.x76)**2 + (m.x112 - m.x166)**2 + (m.x202
    - m.x256)**2) + 1 / sqrt((m.x22 - m.x77)**2 + (m.x112 - m.x167)**2 + (
    m.x202 - m.x257)**2) + 1 / sqrt((m.x22 - m.x78)**2 + (m.x112 - m.x168)**2
    + (m.x202 - m.x258)**2) + 1 / sqrt((m.x22 - m.x79)**2 + (m.x112 - m.x169)
    **2 + (m.x202 - m.x259)**2) + 1 / sqrt((m.x22 - m.x80)**2 + (m.x112 -
    m.x170)**2 + (m.x202 - m.x260)**2) + 1 / sqrt((m.x22 - m.x81)**2 + (m.x112
    - m.x171)**2 + (m.x202 - m.x261)**2) + 1 / sqrt((m.x22 - m.x82)**2 + (
    m.x112 - m.x172)**2 + (m.x202 - m.x262)**2) + 1 / sqrt((m.x22 - m.x83)**2
    + (m.x112 - m.x173)**2 + (m.x202 - m.x263)**2) + 1 / sqrt((m.x22 - m.x84)
    **2 + (m.x112 - m.x174)**2 + (m.x202 - m.x264)**2) + 1 / sqrt((m.x22 -
    m.x85)**2 + (m.x112 - m.x175)**2 + (m.x202 - m.x265)**2) + 1 / sqrt((m.x22
    - m.x86)**2 + (m.x112 - m.x176)**2 + (m.x202 - m.x266)**2) + 1 / sqrt((
    m.x22 - m.x87)**2 + (m.x112 - m.x177)**2 + (m.x202 - m.x267)**2) + 1 /
    sqrt((m.x22 - m.x88)**2 + (m.x112 - m.x178)**2 + (m.x202 - m.x268)**2) + 1
    / sqrt((m.x22 - m.x89)**2 + (m.x112 - m.x179)**2 + (m.x202 - m.x269)**2)
    + 1 / sqrt((m.x22 - m.x90)**2 + (m.x112 - m.x180)**2 + (m.x202 - m.x270)**
    2) + 1 / sqrt((m.x23 - m.x24)**2 + (m.x113 - m.x114)**2 + (m.x203 - m.x204)
    **2) + 1 / sqrt((m.x23 - m.x25)**2 + (m.x113 - m.x115)**2 + (m.x203 -
    m.x205)**2) + 1 / sqrt((m.x23 - m.x26)**2 + (m.x113 - m.x116)**2 + (m.x203
    - m.x206)**2) + 1 / sqrt((m.x23 - m.x27)**2 + (m.x113 - m.x117)**2 + (
    m.x203 - m.x207)**2) + 1 / sqrt((m.x23 - m.x28)**2 + (m.x113 - m.x118)**2
    + (m.x203 - m.x208)**2) + 1 / sqrt((m.x23 - m.x29)**2 + (m.x113 - m.x119)
    **2 + (m.x203 - m.x209)**2) + 1 / sqrt((m.x23 - m.x30)**2 + (m.x113 -
    m.x120)**2 + (m.x203 - m.x210)**2) + 1 / sqrt((m.x23 - m.x31)**2 + (m.x113
    - m.x121)**2 + (m.x203 - m.x211)**2) + 1 / sqrt((m.x23 - m.x32)**2 + (
    m.x113 - m.x122)**2 + (m.x203 - m.x212)**2) + 1 / sqrt((m.x23 - m.x33)**2
    + (m.x113 - m.x123)**2 + (m.x203 - m.x213)**2) + 1 / sqrt((m.x23 - m.x34)
    **2 + (m.x113 - m.x124)**2 + (m.x203 - m.x214)**2) + 1 / sqrt((m.x23 -
    m.x35)**2 + (m.x113 - m.x125)**2 + (m.x203 - m.x215)**2) + 1 / sqrt((m.x23
    - m.x36)**2 + (m.x113 - m.x126)**2 + (m.x203 - m.x216)**2) + 1 / sqrt((
    m.x23 - m.x37)**2 + (m.x113 - m.x127)**2 + (m.x203 - m.x217)**2) + 1 /
    sqrt((m.x23 - m.x38)**2 + (m.x113 - m.x128)**2 + (m.x203 - m.x218)**2) + 1
    / sqrt((m.x23 - m.x39)**2 + (m.x113 - m.x129)**2 + (m.x203 - m.x219)**2)
    + 1 / sqrt((m.x23 - m.x40)**2 + (m.x113 - m.x130)**2 + (m.x203 - m.x220)**
    2) + 1 / sqrt((m.x23 - m.x41)**2 + (m.x113 - m.x131)**2 + (m.x203 - m.x221)
    **2) + 1 / sqrt((m.x23 - m.x42)**2 + (m.x113 - m.x132)**2 + (m.x203 -
    m.x222)**2) + 1 / sqrt((m.x23 - m.x43)**2 + (m.x113 - m.x133)**2 + (m.x203
    - m.x223)**2) + 1 / sqrt((m.x23 - m.x44)**2 + (m.x113 - m.x134)**2 + (
    m.x203 - m.x224)**2) + 1 / sqrt((m.x23 - m.x45)**2 + (m.x113 - m.x135)**2
    + (m.x203 - m.x225)**2) + 1 / sqrt((m.x23 - m.x46)**2 + (m.x113 - m.x136)
    **2 + (m.x203 - m.x226)**2) + 1 / sqrt((m.x23 - m.x47)**2 + (m.x113 -
    m.x137)**2 + (m.x203 - m.x227)**2) + 1 / sqrt((m.x23 - m.x48)**2 + (m.x113
    - m.x138)**2 + (m.x203 - m.x228)**2) + 1 / sqrt((m.x23 - m.x49)**2 + (
    m.x113 - m.x139)**2 + (m.x203 - m.x229)**2) + 1 / sqrt((m.x23 - m.x50)**2
    + (m.x113 - m.x140)**2 + (m.x203 - m.x230)**2) + 1 / sqrt((m.x23 - m.x51)
    **2 + (m.x113 - m.x141)**2 + (m.x203 - m.x231)**2) + 1 / sqrt((m.x23 -
    m.x52)**2 + (m.x113 - m.x142)**2 + (m.x203 - m.x232)**2) + 1 / sqrt((m.x23
    - m.x53)**2 + (m.x113 - m.x143)**2 + (m.x203 - m.x233)**2) + 1 / sqrt((
    m.x23 - m.x54)**2 + (m.x113 - m.x144)**2 + (m.x203 - m.x234)**2) + 1 /
    sqrt((m.x23 - m.x55)**2 + (m.x113 - m.x145)**2 + (m.x203 - m.x235)**2) + 1
    / sqrt((m.x23 - m.x56)**2 + (m.x113 - m.x146)**2 + (m.x203 - m.x236)**2)
    + 1 / sqrt((m.x23 - m.x57)**2 + (m.x113 - m.x147)**2 + (m.x203 - m.x237)**
    2) + 1 / sqrt((m.x23 - m.x58)**2 + (m.x113 - m.x148)**2 + (m.x203 - m.x238)
    **2) + 1 / sqrt((m.x23 - m.x59)**2 + (m.x113 - m.x149)**2 + (m.x203 -
    m.x239)**2) + 1 / sqrt((m.x23 - m.x60)**2 + (m.x113 - m.x150)**2 + (m.x203
    - m.x240)**2) + 1 / sqrt((m.x23 - m.x61)**2 + (m.x113 - m.x151)**2 + (
    m.x203 - m.x241)**2) + 1 / sqrt((m.x23 - m.x62)**2 + (m.x113 - m.x152)**2
    + (m.x203 - m.x242)**2) + 1 / sqrt((m.x23 - m.x63)**2 + (m.x113 - m.x153)
    **2 + (m.x203 - m.x243)**2) + 1 / sqrt((m.x23 - m.x64)**2 + (m.x113 -
    m.x154)**2 + (m.x203 - m.x244)**2) + 1 / sqrt((m.x23 - m.x65)**2 + (m.x113
    - m.x155)**2 + (m.x203 - m.x245)**2) + 1 / sqrt((m.x23 - m.x66)**2 + (
    m.x113 - m.x156)**2 + (m.x203 - m.x246)**2) + 1 / sqrt((m.x23 - m.x67)**2
    + (m.x113 - m.x157)**2 + (m.x203 - m.x247)**2) + 1 / sqrt((m.x23 - m.x68)
    **2 + (m.x113 - m.x158)**2 + (m.x203 - m.x248)**2) + 1 / sqrt((m.x23 -
    m.x69)**2 + (m.x113 - m.x159)**2 + (m.x203 - m.x249)**2) + 1 / sqrt((m.x23
    - m.x70)**2 + (m.x113 - m.x160)**2 + (m.x203 - m.x250)**2) + 1 / sqrt((
    m.x23 - m.x71)**2 + (m.x113 - m.x161)**2 + (m.x203 - m.x251)**2) + 1 /
    sqrt((m.x23 - m.x72)**2 + (m.x113 - m.x162)**2 + (m.x203 - m.x252)**2) + 1
    / sqrt((m.x23 - m.x73)**2 + (m.x113 - m.x163)**2 + (m.x203 - m.x253)**2)
    + 1 / sqrt((m.x23 - m.x74)**2 + (m.x113 - m.x164)**2 + (m.x203 - m.x254)**
    2) + 1 / sqrt((m.x23 - m.x75)**2 + (m.x113 - m.x165)**2 + (m.x203 - m.x255)
    **2) + 1 / sqrt((m.x23 - m.x76)**2 + (m.x113 - m.x166)**2 + (m.x203 -
    m.x256)**2) + 1 / sqrt((m.x23 - m.x77)**2 + (m.x113 - m.x167)**2 + (m.x203
    - m.x257)**2) + 1 / sqrt((m.x23 - m.x78)**2 + (m.x113 - m.x168)**2 + (
    m.x203 - m.x258)**2) + 1 / sqrt((m.x23 - m.x79)**2 + (m.x113 - m.x169)**2
    + (m.x203 - m.x259)**2) + 1 / sqrt((m.x23 - m.x80)**2 + (m.x113 - m.x170)
    **2 + (m.x203 - m.x260)**2) + 1 / sqrt((m.x23 - m.x81)**2 + (m.x113 -
    m.x171)**2 + (m.x203 - m.x261)**2) + 1 / sqrt((m.x23 - m.x82)**2 + (m.x113
    - m.x172)**2 + (m.x203 - m.x262)**2) + 1 / sqrt((m.x23 - m.x83)**2 + (
    m.x113 - m.x173)**2 + (m.x203 - m.x263)**2) + 1 / sqrt((m.x23 - m.x84)**2
    + (m.x113 - m.x174)**2 + (m.x203 - m.x264)**2) + 1 / sqrt((m.x23 - m.x85)
    **2 + (m.x113 - m.x175)**2 + (m.x203 - m.x265)**2) + 1 / sqrt((m.x23 -
    m.x86)**2 + (m.x113 - m.x176)**2 + (m.x203 - m.x266)**2) + 1 / sqrt((m.x23
    - m.x87)**2 + (m.x113 - m.x177)**2 + (m.x203 - m.x267)**2) + 1 / sqrt((
    m.x23 - m.x88)**2 + (m.x113 - m.x178)**2 + (m.x203 - m.x268)**2) + 1 /
    sqrt((m.x23 - m.x89)**2 + (m.x113 - m.x179)**2 + (m.x203 - m.x269)**2) + 1
    / sqrt((m.x23 - m.x90)**2 + (m.x113 - m.x180)**2 + (m.x203 - m.x270)**2)
    + 1 / sqrt((m.x24 - m.x25)**2 + (m.x114 - m.x115)**2 + (m.x204 - m.x205)**
    2) + 1 / sqrt((m.x24 - m.x26)**2 + (m.x114 - m.x116)**2 + (m.x204 - m.x206)
    **2) + 1 / sqrt((m.x24 - m.x27)**2 + (m.x114 - m.x117)**2 + (m.x204 -
    m.x207)**2) + 1 / sqrt((m.x24 - m.x28)**2 + (m.x114 - m.x118)**2 + (m.x204
    - m.x208)**2) + 1 / sqrt((m.x24 - m.x29)**2 + (m.x114 - m.x119)**2 + (
    m.x204 - m.x209)**2) + 1 / sqrt((m.x24 - m.x30)**2 + (m.x114 - m.x120)**2
    + (m.x204 - m.x210)**2) + 1 / sqrt((m.x24 - m.x31)**2 + (m.x114 - m.x121)
    **2 + (m.x204 - m.x211)**2) + 1 / sqrt((m.x24 - m.x32)**2 + (m.x114 -
    m.x122)**2 + (m.x204 - m.x212)**2) + 1 / sqrt((m.x24 - m.x33)**2 + (m.x114
    - m.x123)**2 + (m.x204 - m.x213)**2) + 1 / sqrt((m.x24 - m.x34)**2 + (
    m.x114 - m.x124)**2 + (m.x204 - m.x214)**2) + 1 / sqrt((m.x24 - m.x35)**2
    + (m.x114 - m.x125)**2 + (m.x204 - m.x215)**2) + 1 / sqrt((m.x24 - m.x36)
    **2 + (m.x114 - m.x126)**2 + (m.x204 - m.x216)**2) + 1 / sqrt((m.x24 -
    m.x37)**2 + (m.x114 - m.x127)**2 + (m.x204 - m.x217)**2) + 1 / sqrt((m.x24
    - m.x38)**2 + (m.x114 - m.x128)**2 + (m.x204 - m.x218)**2) + 1 / sqrt((
    m.x24 - m.x39)**2 + (m.x114 - m.x129)**2 + (m.x204 - m.x219)**2) + 1 /
    sqrt((m.x24 - m.x40)**2 + (m.x114 - m.x130)**2 + (m.x204 - m.x220)**2) + 1
    / sqrt((m.x24 - m.x41)**2 + (m.x114 - m.x131)**2 + (m.x204 - m.x221)**2)
    + 1 / sqrt((m.x24 - m.x42)**2 + (m.x114 - m.x132)**2 + (m.x204 - m.x222)**
    2) + 1 / sqrt((m.x24 - m.x43)**2 + (m.x114 - m.x133)**2 + (m.x204 - m.x223)
    **2) + 1 / sqrt((m.x24 - m.x44)**2 + (m.x114 - m.x134)**2 + (m.x204 -
    m.x224)**2) + 1 / sqrt((m.x24 - m.x45)**2 + (m.x114 - m.x135)**2 + (m.x204
    - m.x225)**2) + 1 / sqrt((m.x24 - m.x46)**2 + (m.x114 - m.x136)**2 + (
    m.x204 - m.x226)**2) + 1 / sqrt((m.x24 - m.x47)**2 + (m.x114 - m.x137)**2
    + (m.x204 - m.x227)**2) + 1 / sqrt((m.x24 - m.x48)**2 + (m.x114 - m.x138)
    **2 + (m.x204 - m.x228)**2) + 1 / sqrt((m.x24 - m.x49)**2 + (m.x114 -
    m.x139)**2 + (m.x204 - m.x229)**2) + 1 / sqrt((m.x24 - m.x50)**2 + (m.x114
    - m.x140)**2 + (m.x204 - m.x230)**2) + 1 / sqrt((m.x24 - m.x51)**2 + (
    m.x114 - m.x141)**2 + (m.x204 - m.x231)**2) + 1 / sqrt((m.x24 - m.x52)**2
    + (m.x114 - m.x142)**2 + (m.x204 - m.x232)**2) + 1 / sqrt((m.x24 - m.x53)
    **2 + (m.x114 - m.x143)**2 + (m.x204 - m.x233)**2) + 1 / sqrt((m.x24 -
    m.x54)**2 + (m.x114 - m.x144)**2 + (m.x204 - m.x234)**2) + 1 / sqrt((m.x24
    - m.x55)**2 + (m.x114 - m.x145)**2 + (m.x204 - m.x235)**2) + 1 / sqrt((
    m.x24 - m.x56)**2 + (m.x114 - m.x146)**2 + (m.x204 - m.x236)**2) + 1 /
    sqrt((m.x24 - m.x57)**2 + (m.x114 - m.x147)**2 + (m.x204 - m.x237)**2) + 1
    / sqrt((m.x24 - m.x58)**2 + (m.x114 - m.x148)**2 + (m.x204 - m.x238)**2)
    + 1 / sqrt((m.x24 - m.x59)**2 + (m.x114 - m.x149)**2 + (m.x204 - m.x239)**
    2) + 1 / sqrt((m.x24 - m.x60)**2 + (m.x114 - m.x150)**2 + (m.x204 - m.x240)
    **2) + 1 / sqrt((m.x24 - m.x61)**2 + (m.x114 - m.x151)**2 + (m.x204 -
    m.x241)**2) + 1 / sqrt((m.x24 - m.x62)**2 + (m.x114 - m.x152)**2 + (m.x204
    - m.x242)**2) + 1 / sqrt((m.x24 - m.x63)**2 + (m.x114 - m.x153)**2 + (
    m.x204 - m.x243)**2) + 1 / sqrt((m.x24 - m.x64)**2 + (m.x114 - m.x154)**2
    + (m.x204 - m.x244)**2) + 1 / sqrt((m.x24 - m.x65)**2 + (m.x114 - m.x155)
    **2 + (m.x204 - m.x245)**2) + 1 / sqrt((m.x24 - m.x66)**2 + (m.x114 -
    m.x156)**2 + (m.x204 - m.x246)**2) + 1 / sqrt((m.x24 - m.x67)**2 + (m.x114
    - m.x157)**2 + (m.x204 - m.x247)**2) + 1 / sqrt((m.x24 - m.x68)**2 + (
    m.x114 - m.x158)**2 + (m.x204 - m.x248)**2) + 1 / sqrt((m.x24 - m.x69)**2
    + (m.x114 - m.x159)**2 + (m.x204 - m.x249)**2) + 1 / sqrt((m.x24 - m.x70)
    **2 + (m.x114 - m.x160)**2 + (m.x204 - m.x250)**2) + 1 / sqrt((m.x24 -
    m.x71)**2 + (m.x114 - m.x161)**2 + (m.x204 - m.x251)**2) + 1 / sqrt((m.x24
    - m.x72)**2 + (m.x114 - m.x162)**2 + (m.x204 - m.x252)**2) + 1 / sqrt((
    m.x24 - m.x73)**2 + (m.x114 - m.x163)**2 + (m.x204 - m.x253)**2) + 1 /
    sqrt((m.x24 - m.x74)**2 + (m.x114 - m.x164)**2 + (m.x204 - m.x254)**2) + 1
    / sqrt((m.x24 - m.x75)**2 + (m.x114 - m.x165)**2 + (m.x204 - m.x255)**2)
    + 1 / sqrt((m.x24 - m.x76)**2 + (m.x114 - m.x166)**2 + (m.x204 - m.x256)**
    2) + 1 / sqrt((m.x24 - m.x77)**2 + (m.x114 - m.x167)**2 + (m.x204 - m.x257)
    **2) + 1 / sqrt((m.x24 - m.x78)**2 + (m.x114 - m.x168)**2 + (m.x204 -
    m.x258)**2) + 1 / sqrt((m.x24 - m.x79)**2 + (m.x114 - m.x169)**2 + (m.x204
    - m.x259)**2) + 1 / sqrt((m.x24 - m.x80)**2 + (m.x114 - m.x170)**2 + (
    m.x204 - m.x260)**2) + 1 / sqrt((m.x24 - m.x81)**2 + (m.x114 - m.x171)**2
    + (m.x204 - m.x261)**2) + 1 / sqrt((m.x24 - m.x82)**2 + (m.x114 - m.x172)
    **2 + (m.x204 - m.x262)**2) + 1 / sqrt((m.x24 - m.x83)**2 + (m.x114 -
    m.x173)**2 + (m.x204 - m.x263)**2) + 1 / sqrt((m.x24 - m.x84)**2 + (m.x114
    - m.x174)**2 + (m.x204 - m.x264)**2) + 1 / sqrt((m.x24 - m.x85)**2 + (
    m.x114 - m.x175)**2 + (m.x204 - m.x265)**2) + 1 / sqrt((m.x24 - m.x86)**2
    + (m.x114 - m.x176)**2 + (m.x204 - m.x266)**2) + 1 / sqrt((m.x24 - m.x87)
    **2 + (m.x114 - m.x177)**2 + (m.x204 - m.x267)**2) + 1 / sqrt((m.x24 -
    m.x88)**2 + (m.x114 - m.x178)**2 + (m.x204 - m.x268)**2) + 1 / sqrt((m.x24
    - m.x89)**2 + (m.x114 - m.x179)**2 + (m.x204 - m.x269)**2) + 1 / sqrt((
    m.x24 - m.x90)**2 + (m.x114 - m.x180)**2 + (m.x204 - m.x270)**2) + 1 /
    sqrt((m.x25 - m.x26)**2 + (m.x115 - m.x116)**2 + (m.x205 - m.x206)**2) + 1
    / sqrt((m.x25 - m.x27)**2 + (m.x115 - m.x117)**2 + (m.x205 - m.x207)**2)
    + 1 / sqrt((m.x25 - m.x28)**2 + (m.x115 - m.x118)**2 + (m.x205 - m.x208)**
    2) + 1 / sqrt((m.x25 - m.x29)**2 + (m.x115 - m.x119)**2 + (m.x205 - m.x209)
    **2) + 1 / sqrt((m.x25 - m.x30)**2 + (m.x115 - m.x120)**2 + (m.x205 -
    m.x210)**2) + 1 / sqrt((m.x25 - m.x31)**2 + (m.x115 - m.x121)**2 + (m.x205
    - m.x211)**2) + 1 / sqrt((m.x25 - m.x32)**2 + (m.x115 - m.x122)**2 + (
    m.x205 - m.x212)**2) + 1 / sqrt((m.x25 - m.x33)**2 + (m.x115 - m.x123)**2
    + (m.x205 - m.x213)**2) + 1 / sqrt((m.x25 - m.x34)**2 + (m.x115 - m.x124)
    **2 + (m.x205 - m.x214)**2) + 1 / sqrt((m.x25 - m.x35)**2 + (m.x115 -
    m.x125)**2 + (m.x205 - m.x215)**2) + 1 / sqrt((m.x25 - m.x36)**2 + (m.x115
    - m.x126)**2 + (m.x205 - m.x216)**2) + 1 / sqrt((m.x25 - m.x37)**2 + (
    m.x115 - m.x127)**2 + (m.x205 - m.x217)**2) + 1 / sqrt((m.x25 - m.x38)**2
    + (m.x115 - m.x128)**2 + (m.x205 - m.x218)**2) + 1 / sqrt((m.x25 - m.x39)
    **2 + (m.x115 - m.x129)**2 + (m.x205 - m.x219)**2) + 1 / sqrt((m.x25 -
    m.x40)**2 + (m.x115 - m.x130)**2 + (m.x205 - m.x220)**2) + 1 / sqrt((m.x25
    - m.x41)**2 + (m.x115 - m.x131)**2 + (m.x205 - m.x221)**2) + 1 / sqrt((
    m.x25 - m.x42)**2 + (m.x115 - m.x132)**2 + (m.x205 - m.x222)**2) + 1 /
    sqrt((m.x25 - m.x43)**2 + (m.x115 - m.x133)**2 + (m.x205 - m.x223)**2) + 1
    / sqrt((m.x25 - m.x44)**2 + (m.x115 - m.x134)**2 + (m.x205 - m.x224)**2)
    + 1 / sqrt((m.x25 - m.x45)**2 + (m.x115 - m.x135)**2 + (m.x205 - m.x225)**
    2) + 1 / sqrt((m.x25 - m.x46)**2 + (m.x115 - m.x136)**2 + (m.x205 - m.x226)
    **2) + 1 / sqrt((m.x25 - m.x47)**2 + (m.x115 - m.x137)**2 + (m.x205 -
    m.x227)**2) + 1 / sqrt((m.x25 - m.x48)**2 + (m.x115 - m.x138)**2 + (m.x205
    - m.x228)**2) + 1 / sqrt((m.x25 - m.x49)**2 + (m.x115 - m.x139)**2 + (
    m.x205 - m.x229)**2) + 1 / sqrt((m.x25 - m.x50)**2 + (m.x115 - m.x140)**2
    + (m.x205 - m.x230)**2) + 1 / sqrt((m.x25 - m.x51)**2 + (m.x115 - m.x141)
    **2 + (m.x205 - m.x231)**2) + 1 / sqrt((m.x25 - m.x52)**2 + (m.x115 -
    m.x142)**2 + (m.x205 - m.x232)**2) + 1 / sqrt((m.x25 - m.x53)**2 + (m.x115
    - m.x143)**2 + (m.x205 - m.x233)**2) + 1 / sqrt((m.x25 - m.x54)**2 + (
    m.x115 - m.x144)**2 + (m.x205 - m.x234)**2) + 1 / sqrt((m.x25 - m.x55)**2
    + (m.x115 - m.x145)**2 + (m.x205 - m.x235)**2) + 1 / sqrt((m.x25 - m.x56)
    **2 + (m.x115 - m.x146)**2 + (m.x205 - m.x236)**2) + 1 / sqrt((m.x25 -
    m.x57)**2 + (m.x115 - m.x147)**2 + (m.x205 - m.x237)**2) + 1 / sqrt((m.x25
    - m.x58)**2 + (m.x115 - m.x148)**2 + (m.x205 - m.x238)**2) + 1 / sqrt((
    m.x25 - m.x59)**2 + (m.x115 - m.x149)**2 + (m.x205 - m.x239)**2) + 1 /
    sqrt((m.x25 - m.x60)**2 + (m.x115 - m.x150)**2 + (m.x205 - m.x240)**2) + 1
    / sqrt((m.x25 - m.x61)**2 + (m.x115 - m.x151)**2 + (m.x205 - m.x241)**2)
    + 1 / sqrt((m.x25 - m.x62)**2 + (m.x115 - m.x152)**2 + (m.x205 - m.x242)**
    2) + 1 / sqrt((m.x25 - m.x63)**2 + (m.x115 - m.x153)**2 + (m.x205 - m.x243)
    **2) + 1 / sqrt((m.x25 - m.x64)**2 + (m.x115 - m.x154)**2 + (m.x205 -
    m.x244)**2) + 1 / sqrt((m.x25 - m.x65)**2 + (m.x115 - m.x155)**2 + (m.x205
    - m.x245)**2) + 1 / sqrt((m.x25 - m.x66)**2 + (m.x115 - m.x156)**2 + (
    m.x205 - m.x246)**2) + 1 / sqrt((m.x25 - m.x67)**2 + (m.x115 - m.x157)**2
    + (m.x205 - m.x247)**2) + 1 / sqrt((m.x25 - m.x68)**2 + (m.x115 - m.x158)
    **2 + (m.x205 - m.x248)**2) + 1 / sqrt((m.x25 - m.x69)**2 + (m.x115 -
    m.x159)**2 + (m.x205 - m.x249)**2) + 1 / sqrt((m.x25 - m.x70)**2 + (m.x115
    - m.x160)**2 + (m.x205 - m.x250)**2) + 1 / sqrt((m.x25 - m.x71)**2 + (
    m.x115 - m.x161)**2 + (m.x205 - m.x251)**2) + 1 / sqrt((m.x25 - m.x72)**2
    + (m.x115 - m.x162)**2 + (m.x205 - m.x252)**2) + 1 / sqrt((m.x25 - m.x73)
    **2 + (m.x115 - m.x163)**2 + (m.x205 - m.x253)**2) + 1 / sqrt((m.x25 -
    m.x74)**2 + (m.x115 - m.x164)**2 + (m.x205 - m.x254)**2) + 1 / sqrt((m.x25
    - m.x75)**2 + (m.x115 - m.x165)**2 + (m.x205 - m.x255)**2) + 1 / sqrt((
    m.x25 - m.x76)**2 + (m.x115 - m.x166)**2 + (m.x205 - m.x256)**2) + 1 /
    sqrt((m.x25 - m.x77)**2 + (m.x115 - m.x167)**2 + (m.x205 - m.x257)**2) + 1
    / sqrt((m.x25 - m.x78)**2 + (m.x115 - m.x168)**2 + (m.x205 - m.x258)**2)
    + 1 / sqrt((m.x25 - m.x79)**2 + (m.x115 - m.x169)**2 + (m.x205 - m.x259)**
    2) + 1 / sqrt((m.x25 - m.x80)**2 + (m.x115 - m.x170)**2 + (m.x205 - m.x260)
    **2) + 1 / sqrt((m.x25 - m.x81)**2 + (m.x115 - m.x171)**2 + (m.x205 -
    m.x261)**2) + 1 / sqrt((m.x25 - m.x82)**2 + (m.x115 - m.x172)**2 + (m.x205
    - m.x262)**2) + 1 / sqrt((m.x25 - m.x83)**2 + (m.x115 - m.x173)**2 + (
    m.x205 - m.x263)**2) + 1 / sqrt((m.x25 - m.x84)**2 + (m.x115 - m.x174)**2
    + (m.x205 - m.x264)**2) + 1 / sqrt((m.x25 - m.x85)**2 + (m.x115 - m.x175)
    **2 + (m.x205 - m.x265)**2) + 1 / sqrt((m.x25 - m.x86)**2 + (m.x115 -
    m.x176)**2 + (m.x205 - m.x266)**2) + 1 / sqrt((m.x25 - m.x87)**2 + (m.x115
    - m.x177)**2 + (m.x205 - m.x267)**2) + 1 / sqrt((m.x25 - m.x88)**2 + (
    m.x115 - m.x178)**2 + (m.x205 - m.x268)**2) + 1 / sqrt((m.x25 - m.x89)**2
    + (m.x115 - m.x179)**2 + (m.x205 - m.x269)**2) + 1 / sqrt((m.x25 - m.x90)
    **2 + (m.x115 - m.x180)**2 + (m.x205 - m.x270)**2) + 1 / sqrt((m.x26 -
    m.x27)**2 + (m.x116 - m.x117)**2 + (m.x206 - m.x207)**2) + 1 / sqrt((m.x26
    - m.x28)**2 + (m.x116 - m.x118)**2 + (m.x206 - m.x208)**2) + 1 / sqrt((
    m.x26 - m.x29)**2 + (m.x116 - m.x119)**2 + (m.x206 - m.x209)**2) + 1 /
    sqrt((m.x26 - m.x30)**2 + (m.x116 - m.x120)**2 + (m.x206 - m.x210)**2) + 1
    / sqrt((m.x26 - m.x31)**2 + (m.x116 - m.x121)**2 + (m.x206 - m.x211)**2)
    + 1 / sqrt((m.x26 - m.x32)**2 + (m.x116 - m.x122)**2 + (m.x206 - m.x212)**
    2) + 1 / sqrt((m.x26 - m.x33)**2 + (m.x116 - m.x123)**2 + (m.x206 - m.x213)
    **2) + 1 / sqrt((m.x26 - m.x34)**2 + (m.x116 - m.x124)**2 + (m.x206 -
    m.x214)**2) + 1 / sqrt((m.x26 - m.x35)**2 + (m.x116 - m.x125)**2 + (m.x206
    - m.x215)**2) + 1 / sqrt((m.x26 - m.x36)**2 + (m.x116 - m.x126)**2 + (
    m.x206 - m.x216)**2) + 1 / sqrt((m.x26 - m.x37)**2 + (m.x116 - m.x127)**2
    + (m.x206 - m.x217)**2) + 1 / sqrt((m.x26 - m.x38)**2 + (m.x116 - m.x128)
    **2 + (m.x206 - m.x218)**2) + 1 / sqrt((m.x26 - m.x39)**2 + (m.x116 -
    m.x129)**2 + (m.x206 - m.x219)**2) + 1 / sqrt((m.x26 - m.x40)**2 + (m.x116
    - m.x130)**2 + (m.x206 - m.x220)**2) + 1 / sqrt((m.x26 - m.x41)**2 + (
    m.x116 - m.x131)**2 + (m.x206 - m.x221)**2) + 1 / sqrt((m.x26 - m.x42)**2
    + (m.x116 - m.x132)**2 + (m.x206 - m.x222)**2) + 1 / sqrt((m.x26 - m.x43)
    **2 + (m.x116 - m.x133)**2 + (m.x206 - m.x223)**2) + 1 / sqrt((m.x26 -
    m.x44)**2 + (m.x116 - m.x134)**2 + (m.x206 - m.x224)**2) + 1 / sqrt((m.x26
    - m.x45)**2 + (m.x116 - m.x135)**2 + (m.x206 - m.x225)**2) + 1 / sqrt((
    m.x26 - m.x46)**2 + (m.x116 - m.x136)**2 + (m.x206 - m.x226)**2) + 1 /
    sqrt((m.x26 - m.x47)**2 + (m.x116 - m.x137)**2 + (m.x206 - m.x227)**2) + 1
    / sqrt((m.x26 - m.x48)**2 + (m.x116 - m.x138)**2 + (m.x206 - m.x228)**2)
    + 1 / sqrt((m.x26 - m.x49)**2 + (m.x116 - m.x139)**2 + (m.x206 - m.x229)**
    2) + 1 / sqrt((m.x26 - m.x50)**2 + (m.x116 - m.x140)**2 + (m.x206 - m.x230)
    **2) + 1 / sqrt((m.x26 - m.x51)**2 + (m.x116 - m.x141)**2 + (m.x206 -
    m.x231)**2) + 1 / sqrt((m.x26 - m.x52)**2 + (m.x116 - m.x142)**2 + (m.x206
    - m.x232)**2) + 1 / sqrt((m.x26 - m.x53)**2 + (m.x116 - m.x143)**2 + (
    m.x206 - m.x233)**2) + 1 / sqrt((m.x26 - m.x54)**2 + (m.x116 - m.x144)**2
    + (m.x206 - m.x234)**2) + 1 / sqrt((m.x26 - m.x55)**2 + (m.x116 - m.x145)
    **2 + (m.x206 - m.x235)**2) + 1 / sqrt((m.x26 - m.x56)**2 + (m.x116 -
    m.x146)**2 + (m.x206 - m.x236)**2) + 1 / sqrt((m.x26 - m.x57)**2 + (m.x116
    - m.x147)**2 + (m.x206 - m.x237)**2) + 1 / sqrt((m.x26 - m.x58)**2 + (
    m.x116 - m.x148)**2 + (m.x206 - m.x238)**2) + 1 / sqrt((m.x26 - m.x59)**2
    + (m.x116 - m.x149)**2 + (m.x206 - m.x239)**2) + 1 / sqrt((m.x26 - m.x60)
    **2 + (m.x116 - m.x150)**2 + (m.x206 - m.x240)**2) + 1 / sqrt((m.x26 -
    m.x61)**2 + (m.x116 - m.x151)**2 + (m.x206 - m.x241)**2) + 1 / sqrt((m.x26
    - m.x62)**2 + (m.x116 - m.x152)**2 + (m.x206 - m.x242)**2) + 1 / sqrt((
    m.x26 - m.x63)**2 + (m.x116 - m.x153)**2 + (m.x206 - m.x243)**2) + 1 /
    sqrt((m.x26 - m.x64)**2 + (m.x116 - m.x154)**2 + (m.x206 - m.x244)**2) + 1
    / sqrt((m.x26 - m.x65)**2 + (m.x116 - m.x155)**2 + (m.x206 - m.x245)**2)
    + 1 / sqrt((m.x26 - m.x66)**2 + (m.x116 - m.x156)**2 + (m.x206 - m.x246)**
    2) + 1 / sqrt((m.x26 - m.x67)**2 + (m.x116 - m.x157)**2 + (m.x206 - m.x247)
    **2) + 1 / sqrt((m.x26 - m.x68)**2 + (m.x116 - m.x158)**2 + (m.x206 -
    m.x248)**2) + 1 / sqrt((m.x26 - m.x69)**2 + (m.x116 - m.x159)**2 + (m.x206
    - m.x249)**2) + 1 / sqrt((m.x26 - m.x70)**2 + (m.x116 - m.x160)**2 + (
    m.x206 - m.x250)**2) + 1 / sqrt((m.x26 - m.x71)**2 + (m.x116 - m.x161)**2
    + (m.x206 - m.x251)**2) + 1 / sqrt((m.x26 - m.x72)**2 + (m.x116 - m.x162)
    **2 + (m.x206 - m.x252)**2) + 1 / sqrt((m.x26 - m.x73)**2 + (m.x116 -
    m.x163)**2 + (m.x206 - m.x253)**2) + 1 / sqrt((m.x26 - m.x74)**2 + (m.x116
    - m.x164)**2 + (m.x206 - m.x254)**2) + 1 / sqrt((m.x26 - m.x75)**2 + (
    m.x116 - m.x165)**2 + (m.x206 - m.x255)**2) + 1 / sqrt((m.x26 - m.x76)**2
    + (m.x116 - m.x166)**2 + (m.x206 - m.x256)**2) + 1 / sqrt((m.x26 - m.x77)
    **2 + (m.x116 - m.x167)**2 + (m.x206 - m.x257)**2) + 1 / sqrt((m.x26 -
    m.x78)**2 + (m.x116 - m.x168)**2 + (m.x206 - m.x258)**2) + 1 / sqrt((m.x26
    - m.x79)**2 + (m.x116 - m.x169)**2 + (m.x206 - m.x259)**2) + 1 / sqrt((
    m.x26 - m.x80)**2 + (m.x116 - m.x170)**2 + (m.x206 - m.x260)**2) + 1 /
    sqrt((m.x26 - m.x81)**2 + (m.x116 - m.x171)**2 + (m.x206 - m.x261)**2) + 1
    / sqrt((m.x26 - m.x82)**2 + (m.x116 - m.x172)**2 + (m.x206 - m.x262)**2)
    + 1 / sqrt((m.x26 - m.x83)**2 + (m.x116 - m.x173)**2 + (m.x206 - m.x263)**
    2) + 1 / sqrt((m.x26 - m.x84)**2 + (m.x116 - m.x174)**2 + (m.x206 - m.x264)
    **2) + 1 / sqrt((m.x26 - m.x85)**2 + (m.x116 - m.x175)**2 + (m.x206 -
    m.x265)**2) + 1 / sqrt((m.x26 - m.x86)**2 + (m.x116 - m.x176)**2 + (m.x206
    - m.x266)**2) + 1 / sqrt((m.x26 - m.x87)**2 + (m.x116 - m.x177)**2 + (
    m.x206 - m.x267)**2) + 1 / sqrt((m.x26 - m.x88)**2 + (m.x116 - m.x178)**2
    + (m.x206 - m.x268)**2) + 1 / sqrt((m.x26 - m.x89)**2 + (m.x116 - m.x179)
    **2 + (m.x206 - m.x269)**2) + 1 / sqrt((m.x26 - m.x90)**2 + (m.x116 -
    m.x180)**2 + (m.x206 - m.x270)**2) + 1 / sqrt((m.x27 - m.x28)**2 + (m.x117
    - m.x118)**2 + (m.x207 - m.x208)**2) + 1 / sqrt((m.x27 - m.x29)**2 + (
    m.x117 - m.x119)**2 + (m.x207 - m.x209)**2) + 1 / sqrt((m.x27 - m.x30)**2
    + (m.x117 - m.x120)**2 + (m.x207 - m.x210)**2) + 1 / sqrt((m.x27 - m.x31)
    **2 + (m.x117 - m.x121)**2 + (m.x207 - m.x211)**2) + 1 / sqrt((m.x27 -
    m.x32)**2 + (m.x117 - m.x122)**2 + (m.x207 - m.x212)**2) + 1 / sqrt((m.x27
    - m.x33)**2 + (m.x117 - m.x123)**2 + (m.x207 - m.x213)**2) + 1 / sqrt((
    m.x27 - m.x34)**2 + (m.x117 - m.x124)**2 + (m.x207 - m.x214)**2) + 1 /
    sqrt((m.x27 - m.x35)**2 + (m.x117 - m.x125)**2 + (m.x207 - m.x215)**2) + 1
    / sqrt((m.x27 - m.x36)**2 + (m.x117 - m.x126)**2 + (m.x207 - m.x216)**2)
    + 1 / sqrt((m.x27 - m.x37)**2 + (m.x117 - m.x127)**2 + (m.x207 - m.x217)**
    2) + 1 / sqrt((m.x27 - m.x38)**2 + (m.x117 - m.x128)**2 + (m.x207 - m.x218)
    **2) + 1 / sqrt((m.x27 - m.x39)**2 + (m.x117 - m.x129)**2 + (m.x207 -
    m.x219)**2) + 1 / sqrt((m.x27 - m.x40)**2 + (m.x117 - m.x130)**2 + (m.x207
    - m.x220)**2) + 1 / sqrt((m.x27 - m.x41)**2 + (m.x117 - m.x131)**2 + (
    m.x207 - m.x221)**2) + 1 / sqrt((m.x27 - m.x42)**2 + (m.x117 - m.x132)**2
    + (m.x207 - m.x222)**2) + 1 / sqrt((m.x27 - m.x43)**2 + (m.x117 - m.x133)
    **2 + (m.x207 - m.x223)**2) + 1 / sqrt((m.x27 - m.x44)**2 + (m.x117 -
    m.x134)**2 + (m.x207 - m.x224)**2) + 1 / sqrt((m.x27 - m.x45)**2 + (m.x117
    - m.x135)**2 + (m.x207 - m.x225)**2) + 1 / sqrt((m.x27 - m.x46)**2 + (
    m.x117 - m.x136)**2 + (m.x207 - m.x226)**2) + 1 / sqrt((m.x27 - m.x47)**2
    + (m.x117 - m.x137)**2 + (m.x207 - m.x227)**2) + 1 / sqrt((m.x27 - m.x48)
    **2 + (m.x117 - m.x138)**2 + (m.x207 - m.x228)**2) + 1 / sqrt((m.x27 -
    m.x49)**2 + (m.x117 - m.x139)**2 + (m.x207 - m.x229)**2) + 1 / sqrt((m.x27
    - m.x50)**2 + (m.x117 - m.x140)**2 + (m.x207 - m.x230)**2) + 1 / sqrt((
    m.x27 - m.x51)**2 + (m.x117 - m.x141)**2 + (m.x207 - m.x231)**2) + 1 /
    sqrt((m.x27 - m.x52)**2 + (m.x117 - m.x142)**2 + (m.x207 - m.x232)**2) + 1
    / sqrt((m.x27 - m.x53)**2 + (m.x117 - m.x143)**2 + (m.x207 - m.x233)**2)
    + 1 / sqrt((m.x27 - m.x54)**2 + (m.x117 - m.x144)**2 + (m.x207 - m.x234)**
    2) + 1 / sqrt((m.x27 - m.x55)**2 + (m.x117 - m.x145)**2 + (m.x207 - m.x235)
    **2) + 1 / sqrt((m.x27 - m.x56)**2 + (m.x117 - m.x146)**2 + (m.x207 -
    m.x236)**2) + 1 / sqrt((m.x27 - m.x57)**2 + (m.x117 - m.x147)**2 + (m.x207
    - m.x237)**2) + 1 / sqrt((m.x27 - m.x58)**2 + (m.x117 - m.x148)**2 + (
    m.x207 - m.x238)**2) + 1 / sqrt((m.x27 - m.x59)**2 + (m.x117 - m.x149)**2
    + (m.x207 - m.x239)**2) + 1 / sqrt((m.x27 - m.x60)**2 + (m.x117 - m.x150)
    **2 + (m.x207 - m.x240)**2) + 1 / sqrt((m.x27 - m.x61)**2 + (m.x117 -
    m.x151)**2 + (m.x207 - m.x241)**2) + 1 / sqrt((m.x27 - m.x62)**2 + (m.x117
    - m.x152)**2 + (m.x207 - m.x242)**2) + 1 / sqrt((m.x27 - m.x63)**2 + (
    m.x117 - m.x153)**2 + (m.x207 - m.x243)**2) + 1 / sqrt((m.x27 - m.x64)**2
    + (m.x117 - m.x154)**2 + (m.x207 - m.x244)**2) + 1 / sqrt((m.x27 - m.x65)
    **2 + (m.x117 - m.x155)**2 + (m.x207 - m.x245)**2) + 1 / sqrt((m.x27 -
    m.x66)**2 + (m.x117 - m.x156)**2 + (m.x207 - m.x246)**2) + 1 / sqrt((m.x27
    - m.x67)**2 + (m.x117 - m.x157)**2 + (m.x207 - m.x247)**2) + 1 / sqrt((
    m.x27 - m.x68)**2 + (m.x117 - m.x158)**2 + (m.x207 - m.x248)**2) + 1 /
    sqrt((m.x27 - m.x69)**2 + (m.x117 - m.x159)**2 + (m.x207 - m.x249)**2) + 1
    / sqrt((m.x27 - m.x70)**2 + (m.x117 - m.x160)**2 + (m.x207 - m.x250)**2)
    + 1 / sqrt((m.x27 - m.x71)**2 + (m.x117 - m.x161)**2 + (m.x207 - m.x251)**
    2) + 1 / sqrt((m.x27 - m.x72)**2 + (m.x117 - m.x162)**2 + (m.x207 - m.x252)
    **2) + 1 / sqrt((m.x27 - m.x73)**2 + (m.x117 - m.x163)**2 + (m.x207 -
    m.x253)**2) + 1 / sqrt((m.x27 - m.x74)**2 + (m.x117 - m.x164)**2 + (m.x207
    - m.x254)**2) + 1 / sqrt((m.x27 - m.x75)**2 + (m.x117 - m.x165)**2 + (
    m.x207 - m.x255)**2) + 1 / sqrt((m.x27 - m.x76)**2 + (m.x117 - m.x166)**2
    + (m.x207 - m.x256)**2) + 1 / sqrt((m.x27 - m.x77)**2 + (m.x117 - m.x167)
    **2 + (m.x207 - m.x257)**2) + 1 / sqrt((m.x27 - m.x78)**2 + (m.x117 -
    m.x168)**2 + (m.x207 - m.x258)**2) + 1 / sqrt((m.x27 - m.x79)**2 + (m.x117
    - m.x169)**2 + (m.x207 - m.x259)**2) + 1 / sqrt((m.x27 - m.x80)**2 + (
    m.x117 - m.x170)**2 + (m.x207 - m.x260)**2) + 1 / sqrt((m.x27 - m.x81)**2
    + (m.x117 - m.x171)**2 + (m.x207 - m.x261)**2) + 1 / sqrt((m.x27 - m.x82)
    **2 + (m.x117 - m.x172)**2 + (m.x207 - m.x262)**2) + 1 / sqrt((m.x27 -
    m.x83)**2 + (m.x117 - m.x173)**2 + (m.x207 - m.x263)**2) + 1 / sqrt((m.x27
    - m.x84)**2 + (m.x117 - m.x174)**2 + (m.x207 - m.x264)**2) + 1 / sqrt((
    m.x27 - m.x85)**2 + (m.x117 - m.x175)**2 + (m.x207 - m.x265)**2) + 1 /
    sqrt((m.x27 - m.x86)**2 + (m.x117 - m.x176)**2 + (m.x207 - m.x266)**2) + 1
    / sqrt((m.x27 - m.x87)**2 + (m.x117 - m.x177)**2 + (m.x207 - m.x267)**2)
    + 1 / sqrt((m.x27 - m.x88)**2 + (m.x117 - m.x178)**2 + (m.x207 - m.x268)**
    2) + 1 / sqrt((m.x27 - m.x89)**2 + (m.x117 - m.x179)**2 + (m.x207 - m.x269)
    **2) + 1 / sqrt((m.x27 - m.x90)**2 + (m.x117 - m.x180)**2 + (m.x207 -
    m.x270)**2) + 1 / sqrt((m.x28 - m.x29)**2 + (m.x118 - m.x119)**2 + (m.x208
    - m.x209)**2) + 1 / sqrt((m.x28 - m.x30)**2 + (m.x118 - m.x120)**2 + (
    m.x208 - m.x210)**2) + 1 / sqrt((m.x28 - m.x31)**2 + (m.x118 - m.x121)**2
    + (m.x208 - m.x211)**2) + 1 / sqrt((m.x28 - m.x32)**2 + (m.x118 - m.x122)
    **2 + (m.x208 - m.x212)**2) + 1 / sqrt((m.x28 - m.x33)**2 + (m.x118 -
    m.x123)**2 + (m.x208 - m.x213)**2) + 1 / sqrt((m.x28 - m.x34)**2 + (m.x118
    - m.x124)**2 + (m.x208 - m.x214)**2) + 1 / sqrt((m.x28 - m.x35)**2 + (
    m.x118 - m.x125)**2 + (m.x208 - m.x215)**2) + 1 / sqrt((m.x28 - m.x36)**2
    + (m.x118 - m.x126)**2 + (m.x208 - m.x216)**2) + 1 / sqrt((m.x28 - m.x37)
    **2 + (m.x118 - m.x127)**2 + (m.x208 - m.x217)**2) + 1 / sqrt((m.x28 -
    m.x38)**2 + (m.x118 - m.x128)**2 + (m.x208 - m.x218)**2) + 1 / sqrt((m.x28
    - m.x39)**2 + (m.x118 - m.x129)**2 + (m.x208 - m.x219)**2) + 1 / sqrt((
    m.x28 - m.x40)**2 + (m.x118 - m.x130)**2 + (m.x208 - m.x220)**2) + 1 /
    sqrt((m.x28 - m.x41)**2 + (m.x118 - m.x131)**2 + (m.x208 - m.x221)**2) + 1
    / sqrt((m.x28 - m.x42)**2 + (m.x118 - m.x132)**2 + (m.x208 - m.x222)**2)
    + 1 / sqrt((m.x28 - m.x43)**2 + (m.x118 - m.x133)**2 + (m.x208 - m.x223)**
    2) + 1 / sqrt((m.x28 - m.x44)**2 + (m.x118 - m.x134)**2 + (m.x208 - m.x224)
    **2) + 1 / sqrt((m.x28 - m.x45)**2 + (m.x118 - m.x135)**2 + (m.x208 -
    m.x225)**2) + 1 / sqrt((m.x28 - m.x46)**2 + (m.x118 - m.x136)**2 + (m.x208
    - m.x226)**2) + 1 / sqrt((m.x28 - m.x47)**2 + (m.x118 - m.x137)**2 + (
    m.x208 - m.x227)**2) + 1 / sqrt((m.x28 - m.x48)**2 + (m.x118 - m.x138)**2
    + (m.x208 - m.x228)**2) + 1 / sqrt((m.x28 - m.x49)**2 + (m.x118 - m.x139)
    **2 + (m.x208 - m.x229)**2) + 1 / sqrt((m.x28 - m.x50)**2 + (m.x118 -
    m.x140)**2 + (m.x208 - m.x230)**2) + 1 / sqrt((m.x28 - m.x51)**2 + (m.x118
    - m.x141)**2 + (m.x208 - m.x231)**2) + 1 / sqrt((m.x28 - m.x52)**2 + (
    m.x118 - m.x142)**2 + (m.x208 - m.x232)**2) + 1 / sqrt((m.x28 - m.x53)**2
    + (m.x118 - m.x143)**2 + (m.x208 - m.x233)**2) + 1 / sqrt((m.x28 - m.x54)
    **2 + (m.x118 - m.x144)**2 + (m.x208 - m.x234)**2) + 1 / sqrt((m.x28 -
    m.x55)**2 + (m.x118 - m.x145)**2 + (m.x208 - m.x235)**2) + 1 / sqrt((m.x28
    - m.x56)**2 + (m.x118 - m.x146)**2 + (m.x208 - m.x236)**2) + 1 / sqrt((
    m.x28 - m.x57)**2 + (m.x118 - m.x147)**2 + (m.x208 - m.x237)**2) + 1 /
    sqrt((m.x28 - m.x58)**2 + (m.x118 - m.x148)**2 + (m.x208 - m.x238)**2) + 1
    / sqrt((m.x28 - m.x59)**2 + (m.x118 - m.x149)**2 + (m.x208 - m.x239)**2)
    + 1 / sqrt((m.x28 - m.x60)**2 + (m.x118 - m.x150)**2 + (m.x208 - m.x240)**
    2) + 1 / sqrt((m.x28 - m.x61)**2 + (m.x118 - m.x151)**2 + (m.x208 - m.x241)
    **2) + 1 / sqrt((m.x28 - m.x62)**2 + (m.x118 - m.x152)**2 + (m.x208 -
    m.x242)**2) + 1 / sqrt((m.x28 - m.x63)**2 + (m.x118 - m.x153)**2 + (m.x208
    - m.x243)**2) + 1 / sqrt((m.x28 - m.x64)**2 + (m.x118 - m.x154)**2 + (
    m.x208 - m.x244)**2) + 1 / sqrt((m.x28 - m.x65)**2 + (m.x118 - m.x155)**2
    + (m.x208 - m.x245)**2) + 1 / sqrt((m.x28 - m.x66)**2 + (m.x118 - m.x156)
    **2 + (m.x208 - m.x246)**2) + 1 / sqrt((m.x28 - m.x67)**2 + (m.x118 -
    m.x157)**2 + (m.x208 - m.x247)**2) + 1 / sqrt((m.x28 - m.x68)**2 + (m.x118
    - m.x158)**2 + (m.x208 - m.x248)**2) + 1 / sqrt((m.x28 - m.x69)**2 + (
    m.x118 - m.x159)**2 + (m.x208 - m.x249)**2) + 1 / sqrt((m.x28 - m.x70)**2
    + (m.x118 - m.x160)**2 + (m.x208 - m.x250)**2) + 1 / sqrt((m.x28 - m.x71)
    **2 + (m.x118 - m.x161)**2 + (m.x208 - m.x251)**2) + 1 / sqrt((m.x28 -
    m.x72)**2 + (m.x118 - m.x162)**2 + (m.x208 - m.x252)**2) + 1 / sqrt((m.x28
    - m.x73)**2 + (m.x118 - m.x163)**2 + (m.x208 - m.x253)**2) + 1 / sqrt((
    m.x28 - m.x74)**2 + (m.x118 - m.x164)**2 + (m.x208 - m.x254)**2) + 1 /
    sqrt((m.x28 - m.x75)**2 + (m.x118 - m.x165)**2 + (m.x208 - m.x255)**2) + 1
    / sqrt((m.x28 - m.x76)**2 + (m.x118 - m.x166)**2 + (m.x208 - m.x256)**2)
    + 1 / sqrt((m.x28 - m.x77)**2 + (m.x118 - m.x167)**2 + (m.x208 - m.x257)**
    2) + 1 / sqrt((m.x28 - m.x78)**2 + (m.x118 - m.x168)**2 + (m.x208 - m.x258)
    **2) + 1 / sqrt((m.x28 - m.x79)**2 + (m.x118 - m.x169)**2 + (m.x208 -
    m.x259)**2) + 1 / sqrt((m.x28 - m.x80)**2 + (m.x118 - m.x170)**2 + (m.x208
    - m.x260)**2) + 1 / sqrt((m.x28 - m.x81)**2 + (m.x118 - m.x171)**2 + (
    m.x208 - m.x261)**2) + 1 / sqrt((m.x28 - m.x82)**2 + (m.x118 - m.x172)**2
    + (m.x208 - m.x262)**2) + 1 / sqrt((m.x28 - m.x83)**2 + (m.x118 - m.x173)
    **2 + (m.x208 - m.x263)**2) + 1 / sqrt((m.x28 - m.x84)**2 + (m.x118 -
    m.x174)**2 + (m.x208 - m.x264)**2) + 1 / sqrt((m.x28 - m.x85)**2 + (m.x118
    - m.x175)**2 + (m.x208 - m.x265)**2) + 1 / sqrt((m.x28 - m.x86)**2 + (
    m.x118 - m.x176)**2 + (m.x208 - m.x266)**2) + 1 / sqrt((m.x28 - m.x87)**2
    + (m.x118 - m.x177)**2 + (m.x208 - m.x267)**2) + 1 / sqrt((m.x28 - m.x88)
    **2 + (m.x118 - m.x178)**2 + (m.x208 - m.x268)**2) + 1 / sqrt((m.x28 -
    m.x89)**2 + (m.x118 - m.x179)**2 + (m.x208 - m.x269)**2) + 1 / sqrt((m.x28
    - m.x90)**2 + (m.x118 - m.x180)**2 + (m.x208 - m.x270)**2) + 1 / sqrt((
    m.x29 - m.x30)**2 + (m.x119 - m.x120)**2 + (m.x209 - m.x210)**2) + 1 /
    sqrt((m.x29 - m.x31)**2 + (m.x119 - m.x121)**2 + (m.x209 - m.x211)**2) + 1
    / sqrt((m.x29 - m.x32)**2 + (m.x119 - m.x122)**2 + (m.x209 - m.x212)**2)
    + 1 / sqrt((m.x29 - m.x33)**2 + (m.x119 - m.x123)**2 + (m.x209 - m.x213)**
    2) + 1 / sqrt((m.x29 - m.x34)**2 + (m.x119 - m.x124)**2 + (m.x209 - m.x214)
    **2) + 1 / sqrt((m.x29 - m.x35)**2 + (m.x119 - m.x125)**2 + (m.x209 -
    m.x215)**2) + 1 / sqrt((m.x29 - m.x36)**2 + (m.x119 - m.x126)**2 + (m.x209
    - m.x216)**2) + 1 / sqrt((m.x29 - m.x37)**2 + (m.x119 - m.x127)**2 + (
    m.x209 - m.x217)**2) + 1 / sqrt((m.x29 - m.x38)**2 + (m.x119 - m.x128)**2
    + (m.x209 - m.x218)**2) + 1 / sqrt((m.x29 - m.x39)**2 + (m.x119 - m.x129)
    **2 + (m.x209 - m.x219)**2) + 1 / sqrt((m.x29 - m.x40)**2 + (m.x119 -
    m.x130)**2 + (m.x209 - m.x220)**2) + 1 / sqrt((m.x29 - m.x41)**2 + (m.x119
    - m.x131)**2 + (m.x209 - m.x221)**2) + 1 / sqrt((m.x29 - m.x42)**2 + (
    m.x119 - m.x132)**2 + (m.x209 - m.x222)**2) + 1 / sqrt((m.x29 - m.x43)**2
    + (m.x119 - m.x133)**2 + (m.x209 - m.x223)**2) + 1 / sqrt((m.x29 - m.x44)
    **2 + (m.x119 - m.x134)**2 + (m.x209 - m.x224)**2) + 1 / sqrt((m.x29 -
    m.x45)**2 + (m.x119 - m.x135)**2 + (m.x209 - m.x225)**2) + 1 / sqrt((m.x29
    - m.x46)**2 + (m.x119 - m.x136)**2 + (m.x209 - m.x226)**2) + 1 / sqrt((
    m.x29 - m.x47)**2 + (m.x119 - m.x137)**2 + (m.x209 - m.x227)**2) + 1 /
    sqrt((m.x29 - m.x48)**2 + (m.x119 - m.x138)**2 + (m.x209 - m.x228)**2) + 1
    / sqrt((m.x29 - m.x49)**2 + (m.x119 - m.x139)**2 + (m.x209 - m.x229)**2)
    + 1 / sqrt((m.x29 - m.x50)**2 + (m.x119 - m.x140)**2 + (m.x209 - m.x230)**
    2) + 1 / sqrt((m.x29 - m.x51)**2 + (m.x119 - m.x141)**2 + (m.x209 - m.x231)
    **2) + 1 / sqrt((m.x29 - m.x52)**2 + (m.x119 - m.x142)**2 + (m.x209 -
    m.x232)**2) + 1 / sqrt((m.x29 - m.x53)**2 + (m.x119 - m.x143)**2 + (m.x209
    - m.x233)**2) + 1 / sqrt((m.x29 - m.x54)**2 + (m.x119 - m.x144)**2 + (
    m.x209 - m.x234)**2) + 1 / sqrt((m.x29 - m.x55)**2 + (m.x119 - m.x145)**2
    + (m.x209 - m.x235)**2) + 1 / sqrt((m.x29 - m.x56)**2 + (m.x119 - m.x146)
    **2 + (m.x209 - m.x236)**2) + 1 / sqrt((m.x29 - m.x57)**2 + (m.x119 -
    m.x147)**2 + (m.x209 - m.x237)**2) + 1 / sqrt((m.x29 - m.x58)**2 + (m.x119
    - m.x148)**2 + (m.x209 - m.x238)**2) + 1 / sqrt((m.x29 - m.x59)**2 + (
    m.x119 - m.x149)**2 + (m.x209 - m.x239)**2) + 1 / sqrt((m.x29 - m.x60)**2
    + (m.x119 - m.x150)**2 + (m.x209 - m.x240)**2) + 1 / sqrt((m.x29 - m.x61)
    **2 + (m.x119 - m.x151)**2 + (m.x209 - m.x241)**2) + 1 / sqrt((m.x29 -
    m.x62)**2 + (m.x119 - m.x152)**2 + (m.x209 - m.x242)**2) + 1 / sqrt((m.x29
    - m.x63)**2 + (m.x119 - m.x153)**2 + (m.x209 - m.x243)**2) + 1 / sqrt((
    m.x29 - m.x64)**2 + (m.x119 - m.x154)**2 + (m.x209 - m.x244)**2) + 1 /
    sqrt((m.x29 - m.x65)**2 + (m.x119 - m.x155)**2 + (m.x209 - m.x245)**2) + 1
    / sqrt((m.x29 - m.x66)**2 + (m.x119 - m.x156)**2 + (m.x209 - m.x246)**2)
    + 1 / sqrt((m.x29 - m.x67)**2 + (m.x119 - m.x157)**2 + (m.x209 - m.x247)**
    2) + 1 / sqrt((m.x29 - m.x68)**2 + (m.x119 - m.x158)**2 + (m.x209 - m.x248)
    **2) + 1 / sqrt((m.x29 - m.x69)**2 + (m.x119 - m.x159)**2 + (m.x209 -
    m.x249)**2) + 1 / sqrt((m.x29 - m.x70)**2 + (m.x119 - m.x160)**2 + (m.x209
    - m.x250)**2) + 1 / sqrt((m.x29 - m.x71)**2 + (m.x119 - m.x161)**2 + (
    m.x209 - m.x251)**2) + 1 / sqrt((m.x29 - m.x72)**2 + (m.x119 - m.x162)**2
    + (m.x209 - m.x252)**2) + 1 / sqrt((m.x29 - m.x73)**2 + (m.x119 - m.x163)
    **2 + (m.x209 - m.x253)**2) + 1 / sqrt((m.x29 - m.x74)**2 + (m.x119 -
    m.x164)**2 + (m.x209 - m.x254)**2) + 1 / sqrt((m.x29 - m.x75)**2 + (m.x119
    - m.x165)**2 + (m.x209 - m.x255)**2) + 1 / sqrt((m.x29 - m.x76)**2 + (
    m.x119 - m.x166)**2 + (m.x209 - m.x256)**2) + 1 / sqrt((m.x29 - m.x77)**2
    + (m.x119 - m.x167)**2 + (m.x209 - m.x257)**2) + 1 / sqrt((m.x29 - m.x78)
    **2 + (m.x119 - m.x168)**2 + (m.x209 - m.x258)**2) + 1 / sqrt((m.x29 -
    m.x79)**2 + (m.x119 - m.x169)**2 + (m.x209 - m.x259)**2) + 1 / sqrt((m.x29
    - m.x80)**2 + (m.x119 - m.x170)**2 + (m.x209 - m.x260)**2) + 1 / sqrt((
    m.x29 - m.x81)**2 + (m.x119 - m.x171)**2 + (m.x209 - m.x261)**2) + 1 /
    sqrt((m.x29 - m.x82)**2 + (m.x119 - m.x172)**2 + (m.x209 - m.x262)**2) + 1
    / sqrt((m.x29 - m.x83)**2 + (m.x119 - m.x173)**2 + (m.x209 - m.x263)**2)
    + 1 / sqrt((m.x29 - m.x84)**2 + (m.x119 - m.x174)**2 + (m.x209 - m.x264)**
    2) + 1 / sqrt((m.x29 - m.x85)**2 + (m.x119 - m.x175)**2 + (m.x209 - m.x265)
    **2) + 1 / sqrt((m.x29 - m.x86)**2 + (m.x119 - m.x176)**2 + (m.x209 -
    m.x266)**2) + 1 / sqrt((m.x29 - m.x87)**2 + (m.x119 - m.x177)**2 + (m.x209
    - m.x267)**2) + 1 / sqrt((m.x29 - m.x88)**2 + (m.x119 - m.x178)**2 + (
    m.x209 - m.x268)**2) + 1 / sqrt((m.x29 - m.x89)**2 + (m.x119 - m.x179)**2
    + (m.x209 - m.x269)**2) + 1 / sqrt((m.x29 - m.x90)**2 + (m.x119 - m.x180)
    **2 + (m.x209 - m.x270)**2) + 1 / sqrt((m.x30 - m.x31)**2 + (m.x120 -
    m.x121)**2 + (m.x210 - m.x211)**2) + 1 / sqrt((m.x30 - m.x32)**2 + (m.x120
    - m.x122)**2 + (m.x210 - m.x212)**2) + 1 / sqrt((m.x30 - m.x33)**2 + (
    m.x120 - m.x123)**2 + (m.x210 - m.x213)**2) + 1 / sqrt((m.x30 - m.x34)**2
    + (m.x120 - m.x124)**2 + (m.x210 - m.x214)**2) + 1 / sqrt((m.x30 - m.x35)
    **2 + (m.x120 - m.x125)**2 + (m.x210 - m.x215)**2) + 1 / sqrt((m.x30 -
    m.x36)**2 + (m.x120 - m.x126)**2 + (m.x210 - m.x216)**2) + 1 / sqrt((m.x30
    - m.x37)**2 + (m.x120 - m.x127)**2 + (m.x210 - m.x217)**2) + 1 / sqrt((
    m.x30 - m.x38)**2 + (m.x120 - m.x128)**2 + (m.x210 - m.x218)**2) + 1 /
    sqrt((m.x30 - m.x39)**2 + (m.x120 - m.x129)**2 + (m.x210 - m.x219)**2) + 1
    / sqrt((m.x30 - m.x40)**2 + (m.x120 - m.x130)**2 + (m.x210 - m.x220)**2)
    + 1 / sqrt((m.x30 - m.x41)**2 + (m.x120 - m.x131)**2 + (m.x210 - m.x221)**
    2) + 1 / sqrt((m.x30 - m.x42)**2 + (m.x120 - m.x132)**2 + (m.x210 - m.x222)
    **2) + 1 / sqrt((m.x30 - m.x43)**2 + (m.x120 - m.x133)**2 + (m.x210 -
    m.x223)**2) + 1 / sqrt((m.x30 - m.x44)**2 + (m.x120 - m.x134)**2 + (m.x210
    - m.x224)**2) + 1 / sqrt((m.x30 - m.x45)**2 + (m.x120 - m.x135)**2 + (
    m.x210 - m.x225)**2) + 1 / sqrt((m.x30 - m.x46)**2 + (m.x120 - m.x136)**2
    + (m.x210 - m.x226)**2) + 1 / sqrt((m.x30 - m.x47)**2 + (m.x120 - m.x137)
    **2 + (m.x210 - m.x227)**2) + 1 / sqrt((m.x30 - m.x48)**2 + (m.x120 -
    m.x138)**2 + (m.x210 - m.x228)**2) + 1 / sqrt((m.x30 - m.x49)**2 + (m.x120
    - m.x139)**2 + (m.x210 - m.x229)**2) + 1 / sqrt((m.x30 - m.x50)**2 + (
    m.x120 - m.x140)**2 + (m.x210 - m.x230)**2) + 1 / sqrt((m.x30 - m.x51)**2
    + (m.x120 - m.x141)**2 + (m.x210 - m.x231)**2) + 1 / sqrt((m.x30 - m.x52)
    **2 + (m.x120 - m.x142)**2 + (m.x210 - m.x232)**2) + 1 / sqrt((m.x30 -
    m.x53)**2 + (m.x120 - m.x143)**2 + (m.x210 - m.x233)**2) + 1 / sqrt((m.x30
    - m.x54)**2 + (m.x120 - m.x144)**2 + (m.x210 - m.x234)**2) + 1 / sqrt((
    m.x30 - m.x55)**2 + (m.x120 - m.x145)**2 + (m.x210 - m.x235)**2) + 1 /
    sqrt((m.x30 - m.x56)**2 + (m.x120 - m.x146)**2 + (m.x210 - m.x236)**2) + 1
    / sqrt((m.x30 - m.x57)**2 + (m.x120 - m.x147)**2 + (m.x210 - m.x237)**2)
    + 1 / sqrt((m.x30 - m.x58)**2 + (m.x120 - m.x148)**2 + (m.x210 - m.x238)**
    2) + 1 / sqrt((m.x30 - m.x59)**2 + (m.x120 - m.x149)**2 + (m.x210 - m.x239)
    **2) + 1 / sqrt((m.x30 - m.x60)**2 + (m.x120 - m.x150)**2 + (m.x210 -
    m.x240)**2) + 1 / sqrt((m.x30 - m.x61)**2 + (m.x120 - m.x151)**2 + (m.x210
    - m.x241)**2) + 1 / sqrt((m.x30 - m.x62)**2 + (m.x120 - m.x152)**2 + (
    m.x210 - m.x242)**2) + 1 / sqrt((m.x30 - m.x63)**2 + (m.x120 - m.x153)**2
    + (m.x210 - m.x243)**2) + 1 / sqrt((m.x30 - m.x64)**2 + (m.x120 - m.x154)
    **2 + (m.x210 - m.x244)**2) + 1 / sqrt((m.x30 - m.x65)**2 + (m.x120 -
    m.x155)**2 + (m.x210 - m.x245)**2) + 1 / sqrt((m.x30 - m.x66)**2 + (m.x120
    - m.x156)**2 + (m.x210 - m.x246)**2) + 1 / sqrt((m.x30 - m.x67)**2 + (
    m.x120 - m.x157)**2 + (m.x210 - m.x247)**2) + 1 / sqrt((m.x30 - m.x68)**2
    + (m.x120 - m.x158)**2 + (m.x210 - m.x248)**2) + 1 / sqrt((m.x30 - m.x69)
    **2 + (m.x120 - m.x159)**2 + (m.x210 - m.x249)**2) + 1 / sqrt((m.x30 -
    m.x70)**2 + (m.x120 - m.x160)**2 + (m.x210 - m.x250)**2) + 1 / sqrt((m.x30
    - m.x71)**2 + (m.x120 - m.x161)**2 + (m.x210 - m.x251)**2) + 1 / sqrt((
    m.x30 - m.x72)**2 + (m.x120 - m.x162)**2 + (m.x210 - m.x252)**2) + 1 /
    sqrt((m.x30 - m.x73)**2 + (m.x120 - m.x163)**2 + (m.x210 - m.x253)**2) + 1
    / sqrt((m.x30 - m.x74)**2 + (m.x120 - m.x164)**2 + (m.x210 - m.x254)**2)
    + 1 / sqrt((m.x30 - m.x75)**2 + (m.x120 - m.x165)**2 + (m.x210 - m.x255)**
    2) + 1 / sqrt((m.x30 - m.x76)**2 + (m.x120 - m.x166)**2 + (m.x210 - m.x256)
    **2) + 1 / sqrt((m.x30 - m.x77)**2 + (m.x120 - m.x167)**2 + (m.x210 -
    m.x257)**2) + 1 / sqrt((m.x30 - m.x78)**2 + (m.x120 - m.x168)**2 + (m.x210
    - m.x258)**2) + 1 / sqrt((m.x30 - m.x79)**2 + (m.x120 - m.x169)**2 + (
    m.x210 - m.x259)**2) + 1 / sqrt((m.x30 - m.x80)**2 + (m.x120 - m.x170)**2
    + (m.x210 - m.x260)**2) + 1 / sqrt((m.x30 - m.x81)**2 + (m.x120 - m.x171)
    **2 + (m.x210 - m.x261)**2) + 1 / sqrt((m.x30 - m.x82)**2 + (m.x120 -
    m.x172)**2 + (m.x210 - m.x262)**2) + 1 / sqrt((m.x30 - m.x83)**2 + (m.x120
    - m.x173)**2 + (m.x210 - m.x263)**2) + 1 / sqrt((m.x30 - m.x84)**2 + (
    m.x120 - m.x174)**2 + (m.x210 - m.x264)**2) + 1 / sqrt((m.x30 - m.x85)**2
    + (m.x120 - m.x175)**2 + (m.x210 - m.x265)**2) + 1 / sqrt((m.x30 - m.x86)
    **2 + (m.x120 - m.x176)**2 + (m.x210 - m.x266)**2) + 1 / sqrt((m.x30 -
    m.x87)**2 + (m.x120 - m.x177)**2 + (m.x210 - m.x267)**2) + 1 / sqrt((m.x30
    - m.x88)**2 + (m.x120 - m.x178)**2 + (m.x210 - m.x268)**2) + 1 / sqrt((
    m.x30 - m.x89)**2 + (m.x120 - m.x179)**2 + (m.x210 - m.x269)**2) + 1 /
    sqrt((m.x30 - m.x90)**2 + (m.x120 - m.x180)**2 + (m.x210 - m.x270)**2) + 1
    / sqrt((m.x31 - m.x32)**2 + (m.x121 - m.x122)**2 + (m.x211 - m.x212)**2)
    + 1 / sqrt((m.x31 - m.x33)**2 + (m.x121 - m.x123)**2 + (m.x211 - m.x213)**
    2) + 1 / sqrt((m.x31 - m.x34)**2 + (m.x121 - m.x124)**2 + (m.x211 - m.x214)
    **2) + 1 / sqrt((m.x31 - m.x35)**2 + (m.x121 - m.x125)**2 + (m.x211 -
    m.x215)**2) + 1 / sqrt((m.x31 - m.x36)**2 + (m.x121 - m.x126)**2 + (m.x211
    - m.x216)**2) + 1 / sqrt((m.x31 - m.x37)**2 + (m.x121 - m.x127)**2 + (
    m.x211 - m.x217)**2) + 1 / sqrt((m.x31 - m.x38)**2 + (m.x121 - m.x128)**2
    + (m.x211 - m.x218)**2) + 1 / sqrt((m.x31 - m.x39)**2 + (m.x121 - m.x129)
    **2 + (m.x211 - m.x219)**2) + 1 / sqrt((m.x31 - m.x40)**2 + (m.x121 -
    m.x130)**2 + (m.x211 - m.x220)**2) + 1 / sqrt((m.x31 - m.x41)**2 + (m.x121
    - m.x131)**2 + (m.x211 - m.x221)**2) + 1 / sqrt((m.x31 - m.x42)**2 + (
    m.x121 - m.x132)**2 + (m.x211 - m.x222)**2) + 1 / sqrt((m.x31 - m.x43)**2
    + (m.x121 - m.x133)**2 + (m.x211 - m.x223)**2) + 1 / sqrt((m.x31 - m.x44)
    **2 + (m.x121 - m.x134)**2 + (m.x211 - m.x224)**2) + 1 / sqrt((m.x31 -
    m.x45)**2 + (m.x121 - m.x135)**2 + (m.x211 - m.x225)**2) + 1 / sqrt((m.x31
    - m.x46)**2 + (m.x121 - m.x136)**2 + (m.x211 - m.x226)**2) + 1 / sqrt((
    m.x31 - m.x47)**2 + (m.x121 - m.x137)**2 + (m.x211 - m.x227)**2) + 1 /
    sqrt((m.x31 - m.x48)**2 + (m.x121 - m.x138)**2 + (m.x211 - m.x228)**2) + 1
    / sqrt((m.x31 - m.x49)**2 + (m.x121 - m.x139)**2 + (m.x211 - m.x229)**2)
    + 1 / sqrt((m.x31 - m.x50)**2 + (m.x121 - m.x140)**2 + (m.x211 - m.x230)**
    2) + 1 / sqrt((m.x31 - m.x51)**2 + (m.x121 - m.x141)**2 + (m.x211 - m.x231)
    **2) + 1 / sqrt((m.x31 - m.x52)**2 + (m.x121 - m.x142)**2 + (m.x211 -
    m.x232)**2) + 1 / sqrt((m.x31 - m.x53)**2 + (m.x121 - m.x143)**2 + (m.x211
    - m.x233)**2) + 1 / sqrt((m.x31 - m.x54)**2 + (m.x121 - m.x144)**2 + (
    m.x211 - m.x234)**2) + 1 / sqrt((m.x31 - m.x55)**2 + (m.x121 - m.x145)**2
    + (m.x211 - m.x235)**2) + 1 / sqrt((m.x31 - m.x56)**2 + (m.x121 - m.x146)
    **2 + (m.x211 - m.x236)**2) + 1 / sqrt((m.x31 - m.x57)**2 + (m.x121 -
    m.x147)**2 + (m.x211 - m.x237)**2) + 1 / sqrt((m.x31 - m.x58)**2 + (m.x121
    - m.x148)**2 + (m.x211 - m.x238)**2) + 1 / sqrt((m.x31 - m.x59)**2 + (
    m.x121 - m.x149)**2 + (m.x211 - m.x239)**2) + 1 / sqrt((m.x31 - m.x60)**2
    + (m.x121 - m.x150)**2 + (m.x211 - m.x240)**2) + 1 / sqrt((m.x31 - m.x61)
    **2 + (m.x121 - m.x151)**2 + (m.x211 - m.x241)**2) + 1 / sqrt((m.x31 -
    m.x62)**2 + (m.x121 - m.x152)**2 + (m.x211 - m.x242)**2) + 1 / sqrt((m.x31
    - m.x63)**2 + (m.x121 - m.x153)**2 + (m.x211 - m.x243)**2) + 1 / sqrt((
    m.x31 - m.x64)**2 + (m.x121 - m.x154)**2 + (m.x211 - m.x244)**2) + 1 /
    sqrt((m.x31 - m.x65)**2 + (m.x121 - m.x155)**2 + (m.x211 - m.x245)**2) + 1
    / sqrt((m.x31 - m.x66)**2 + (m.x121 - m.x156)**2 + (m.x211 - m.x246)**2)
    + 1 / sqrt((m.x31 - m.x67)**2 + (m.x121 - m.x157)**2 + (m.x211 - m.x247)**
    2) + 1 / sqrt((m.x31 - m.x68)**2 + (m.x121 - m.x158)**2 + (m.x211 - m.x248)
    **2) + 1 / sqrt((m.x31 - m.x69)**2 + (m.x121 - m.x159)**2 + (m.x211 -
    m.x249)**2) + 1 / sqrt((m.x31 - m.x70)**2 + (m.x121 - m.x160)**2 + (m.x211
    - m.x250)**2) + 1 / sqrt((m.x31 - m.x71)**2 + (m.x121 - m.x161)**2 + (
    m.x211 - m.x251)**2) + 1 / sqrt((m.x31 - m.x72)**2 + (m.x121 - m.x162)**2
    + (m.x211 - m.x252)**2) + 1 / sqrt((m.x31 - m.x73)**2 + (m.x121 - m.x163)
    **2 + (m.x211 - m.x253)**2) + 1 / sqrt((m.x31 - m.x74)**2 + (m.x121 -
    m.x164)**2 + (m.x211 - m.x254)**2) + 1 / sqrt((m.x31 - m.x75)**2 + (m.x121
    - m.x165)**2 + (m.x211 - m.x255)**2) + 1 / sqrt((m.x31 - m.x76)**2 + (
    m.x121 - m.x166)**2 + (m.x211 - m.x256)**2) + 1 / sqrt((m.x31 - m.x77)**2
    + (m.x121 - m.x167)**2 + (m.x211 - m.x257)**2) + 1 / sqrt((m.x31 - m.x78)
    **2 + (m.x121 - m.x168)**2 + (m.x211 - m.x258)**2) + 1 / sqrt((m.x31 -
    m.x79)**2 + (m.x121 - m.x169)**2 + (m.x211 - m.x259)**2) + 1 / sqrt((m.x31
    - m.x80)**2 + (m.x121 - m.x170)**2 + (m.x211 - m.x260)**2) + 1 / sqrt((
    m.x31 - m.x81)**2 + (m.x121 - m.x171)**2 + (m.x211 - m.x261)**2) + 1 /
    sqrt((m.x31 - m.x82)**2 + (m.x121 - m.x172)**2 + (m.x211 - m.x262)**2) + 1
    / sqrt((m.x31 - m.x83)**2 + (m.x121 - m.x173)**2 + (m.x211 - m.x263)**2)
    + 1 / sqrt((m.x31 - m.x84)**2 + (m.x121 - m.x174)**2 + (m.x211 - m.x264)**
    2) + 1 / sqrt((m.x31 - m.x85)**2 + (m.x121 - m.x175)**2 + (m.x211 - m.x265)
    **2) + 1 / sqrt((m.x31 - m.x86)**2 + (m.x121 - m.x176)**2 + (m.x211 -
    m.x266)**2) + 1 / sqrt((m.x31 - m.x87)**2 + (m.x121 - m.x177)**2 + (m.x211
    - m.x267)**2) + 1 / sqrt((m.x31 - m.x88)**2 + (m.x121 - m.x178)**2 + (
    m.x211 - m.x268)**2) + 1 / sqrt((m.x31 - m.x89)**2 + (m.x121 - m.x179)**2
    + (m.x211 - m.x269)**2) + 1 / sqrt((m.x31 - m.x90)**2 + (m.x121 - m.x180)
    **2 + (m.x211 - m.x270)**2) + 1 / sqrt((m.x32 - m.x33)**2 + (m.x122 -
    m.x123)**2 + (m.x212 - m.x213)**2) + 1 / sqrt((m.x32 - m.x34)**2 + (m.x122
    - m.x124)**2 + (m.x212 - m.x214)**2) + 1 / sqrt((m.x32 - m.x35)**2 + (
    m.x122 - m.x125)**2 + (m.x212 - m.x215)**2) + 1 / sqrt((m.x32 - m.x36)**2
    + (m.x122 - m.x126)**2 + (m.x212 - m.x216)**2) + 1 / sqrt((m.x32 - m.x37)
    **2 + (m.x122 - m.x127)**2 + (m.x212 - m.x217)**2) + 1 / sqrt((m.x32 -
    m.x38)**2 + (m.x122 - m.x128)**2 + (m.x212 - m.x218)**2) + 1 / sqrt((m.x32
    - m.x39)**2 + (m.x122 - m.x129)**2 + (m.x212 - m.x219)**2) + 1 / sqrt((
    m.x32 - m.x40)**2 + (m.x122 - m.x130)**2 + (m.x212 - m.x220)**2) + 1 /
    sqrt((m.x32 - m.x41)**2 + (m.x122 - m.x131)**2 + (m.x212 - m.x221)**2) + 1
    / sqrt((m.x32 - m.x42)**2 + (m.x122 - m.x132)**2 + (m.x212 - m.x222)**2)
    + 1 / sqrt((m.x32 - m.x43)**2 + (m.x122 - m.x133)**2 + (m.x212 - m.x223)**
    2) + 1 / sqrt((m.x32 - m.x44)**2 + (m.x122 - m.x134)**2 + (m.x212 - m.x224)
    **2) + 1 / sqrt((m.x32 - m.x45)**2 + (m.x122 - m.x135)**2 + (m.x212 -
    m.x225)**2) + 1 / sqrt((m.x32 - m.x46)**2 + (m.x122 - m.x136)**2 + (m.x212
    - m.x226)**2) + 1 / sqrt((m.x32 - m.x47)**2 + (m.x122 - m.x137)**2 + (
    m.x212 - m.x227)**2) + 1 / sqrt((m.x32 - m.x48)**2 + (m.x122 - m.x138)**2
    + (m.x212 - m.x228)**2) + 1 / sqrt((m.x32 - m.x49)**2 + (m.x122 - m.x139)
    **2 + (m.x212 - m.x229)**2) + 1 / sqrt((m.x32 - m.x50)**2 + (m.x122 -
    m.x140)**2 + (m.x212 - m.x230)**2) + 1 / sqrt((m.x32 - m.x51)**2 + (m.x122
    - m.x141)**2 + (m.x212 - m.x231)**2) + 1 / sqrt((m.x32 - m.x52)**2 + (
    m.x122 - m.x142)**2 + (m.x212 - m.x232)**2) + 1 / sqrt((m.x32 - m.x53)**2
    + (m.x122 - m.x143)**2 + (m.x212 - m.x233)**2) + 1 / sqrt((m.x32 - m.x54)
    **2 + (m.x122 - m.x144)**2 + (m.x212 - m.x234)**2) + 1 / sqrt((m.x32 -
    m.x55)**2 + (m.x122 - m.x145)**2 + (m.x212 - m.x235)**2) + 1 / sqrt((m.x32
    - m.x56)**2 + (m.x122 - m.x146)**2 + (m.x212 - m.x236)**2) + 1 / sqrt((
    m.x32 - m.x57)**2 + (m.x122 - m.x147)**2 + (m.x212 - m.x237)**2) + 1 /
    sqrt((m.x32 - m.x58)**2 + (m.x122 - m.x148)**2 + (m.x212 - m.x238)**2) + 1
    / sqrt((m.x32 - m.x59)**2 + (m.x122 - m.x149)**2 + (m.x212 - m.x239)**2)
    + 1 / sqrt((m.x32 - m.x60)**2 + (m.x122 - m.x150)**2 + (m.x212 - m.x240)**
    2) + 1 / sqrt((m.x32 - m.x61)**2 + (m.x122 - m.x151)**2 + (m.x212 - m.x241)
    **2) + 1 / sqrt((m.x32 - m.x62)**2 + (m.x122 - m.x152)**2 + (m.x212 -
    m.x242)**2) + 1 / sqrt((m.x32 - m.x63)**2 + (m.x122 - m.x153)**2 + (m.x212
    - m.x243)**2) + 1 / sqrt((m.x32 - m.x64)**2 + (m.x122 - m.x154)**2 + (
    m.x212 - m.x244)**2) + 1 / sqrt((m.x32 - m.x65)**2 + (m.x122 - m.x155)**2
    + (m.x212 - m.x245)**2) + 1 / sqrt((m.x32 - m.x66)**2 + (m.x122 - m.x156)
    **2 + (m.x212 - m.x246)**2) + 1 / sqrt((m.x32 - m.x67)**2 + (m.x122 -
    m.x157)**2 + (m.x212 - m.x247)**2) + 1 / sqrt((m.x32 - m.x68)**2 + (m.x122
    - m.x158)**2 + (m.x212 - m.x248)**2) + 1 / sqrt((m.x32 - m.x69)**2 + (
    m.x122 - m.x159)**2 + (m.x212 - m.x249)**2) + 1 / sqrt((m.x32 - m.x70)**2
    + (m.x122 - m.x160)**2 + (m.x212 - m.x250)**2) + 1 / sqrt((m.x32 - m.x71)
    **2 + (m.x122 - m.x161)**2 + (m.x212 - m.x251)**2) + 1 / sqrt((m.x32 -
    m.x72)**2 + (m.x122 - m.x162)**2 + (m.x212 - m.x252)**2) + 1 / sqrt((m.x32
    - m.x73)**2 + (m.x122 - m.x163)**2 + (m.x212 - m.x253)**2) + 1 / sqrt((
    m.x32 - m.x74)**2 + (m.x122 - m.x164)**2 + (m.x212 - m.x254)**2) + 1 /
    sqrt((m.x32 - m.x75)**2 + (m.x122 - m.x165)**2 + (m.x212 - m.x255)**2) + 1
    / sqrt((m.x32 - m.x76)**2 + (m.x122 - m.x166)**2 + (m.x212 - m.x256)**2)
    + 1 / sqrt((m.x32 - m.x77)**2 + (m.x122 - m.x167)**2 + (m.x212 - m.x257)**
    2) + 1 / sqrt((m.x32 - m.x78)**2 + (m.x122 - m.x168)**2 + (m.x212 - m.x258)
    **2) + 1 / sqrt((m.x32 - m.x79)**2 + (m.x122 - m.x169)**2 + (m.x212 -
    m.x259)**2) + 1 / sqrt((m.x32 - m.x80)**2 + (m.x122 - m.x170)**2 + (m.x212
    - m.x260)**2) + 1 / sqrt((m.x32 - m.x81)**2 + (m.x122 - m.x171)**2 + (
    m.x212 - m.x261)**2) + 1 / sqrt((m.x32 - m.x82)**2 + (m.x122 - m.x172)**2
    + (m.x212 - m.x262)**2) + 1 / sqrt((m.x32 - m.x83)**2 + (m.x122 - m.x173)
    **2 + (m.x212 - m.x263)**2) + 1 / sqrt((m.x32 - m.x84)**2 + (m.x122 -
    m.x174)**2 + (m.x212 - m.x264)**2) + 1 / sqrt((m.x32 - m.x85)**2 + (m.x122
    - m.x175)**2 + (m.x212 - m.x265)**2) + 1 / sqrt((m.x32 - m.x86)**2 + (
    m.x122 - m.x176)**2 + (m.x212 - m.x266)**2) + 1 / sqrt((m.x32 - m.x87)**2
    + (m.x122 - m.x177)**2 + (m.x212 - m.x267)**2) + 1 / sqrt((m.x32 - m.x88)
    **2 + (m.x122 - m.x178)**2 + (m.x212 - m.x268)**2) + 1 / sqrt((m.x32 -
    m.x89)**2 + (m.x122 - m.x179)**2 + (m.x212 - m.x269)**2) + 1 / sqrt((m.x32
    - m.x90)**2 + (m.x122 - m.x180)**2 + (m.x212 - m.x270)**2) + 1 / sqrt((
    m.x33 - m.x34)**2 + (m.x123 - m.x124)**2 + (m.x213 - m.x214)**2) + 1 /
    sqrt((m.x33 - m.x35)**2 + (m.x123 - m.x125)**2 + (m.x213 - m.x215)**2) + 1
    / sqrt((m.x33 - m.x36)**2 + (m.x123 - m.x126)**2 + (m.x213 - m.x216)**2)
    + 1 / sqrt((m.x33 - m.x37)**2 + (m.x123 - m.x127)**2 + (m.x213 - m.x217)**
    2) + 1 / sqrt((m.x33 - m.x38)**2 + (m.x123 - m.x128)**2 + (m.x213 - m.x218)
    **2) + 1 / sqrt((m.x33 - m.x39)**2 + (m.x123 - m.x129)**2 + (m.x213 -
    m.x219)**2) + 1 / sqrt((m.x33 - m.x40)**2 + (m.x123 - m.x130)**2 + (m.x213
    - m.x220)**2) + 1 / sqrt((m.x33 - m.x41)**2 + (m.x123 - m.x131)**2 + (
    m.x213 - m.x221)**2) + 1 / sqrt((m.x33 - m.x42)**2 + (m.x123 - m.x132)**2
    + (m.x213 - m.x222)**2) + 1 / sqrt((m.x33 - m.x43)**2 + (m.x123 - m.x133)
    **2 + (m.x213 - m.x223)**2) + 1 / sqrt((m.x33 - m.x44)**2 + (m.x123 -
    m.x134)**2 + (m.x213 - m.x224)**2) + 1 / sqrt((m.x33 - m.x45)**2 + (m.x123
    - m.x135)**2 + (m.x213 - m.x225)**2) + 1 / sqrt((m.x33 - m.x46)**2 + (
    m.x123 - m.x136)**2 + (m.x213 - m.x226)**2) + 1 / sqrt((m.x33 - m.x47)**2
    + (m.x123 - m.x137)**2 + (m.x213 - m.x227)**2) + 1 / sqrt((m.x33 - m.x48)
    **2 + (m.x123 - m.x138)**2 + (m.x213 - m.x228)**2) + 1 / sqrt((m.x33 -
    m.x49)**2 + (m.x123 - m.x139)**2 + (m.x213 - m.x229)**2) + 1 / sqrt((m.x33
    - m.x50)**2 + (m.x123 - m.x140)**2 + (m.x213 - m.x230)**2) + 1 / sqrt((
    m.x33 - m.x51)**2 + (m.x123 - m.x141)**2 + (m.x213 - m.x231)**2) + 1 /
    sqrt((m.x33 - m.x52)**2 + (m.x123 - m.x142)**2 + (m.x213 - m.x232)**2) + 1
    / sqrt((m.x33 - m.x53)**2 + (m.x123 - m.x143)**2 + (m.x213 - m.x233)**2)
    + 1 / sqrt((m.x33 - m.x54)**2 + (m.x123 - m.x144)**2 + (m.x213 - m.x234)**
    2) + 1 / sqrt((m.x33 - m.x55)**2 + (m.x123 - m.x145)**2 + (m.x213 - m.x235)
    **2) + 1 / sqrt((m.x33 - m.x56)**2 + (m.x123 - m.x146)**2 + (m.x213 -
    m.x236)**2) + 1 / sqrt((m.x33 - m.x57)**2 + (m.x123 - m.x147)**2 + (m.x213
    - m.x237)**2) + 1 / sqrt((m.x33 - m.x58)**2 + (m.x123 - m.x148)**2 + (
    m.x213 - m.x238)**2) + 1 / sqrt((m.x33 - m.x59)**2 + (m.x123 - m.x149)**2
    + (m.x213 - m.x239)**2) + 1 / sqrt((m.x33 - m.x60)**2 + (m.x123 - m.x150)
    **2 + (m.x213 - m.x240)**2) + 1 / sqrt((m.x33 - m.x61)**2 + (m.x123 -
    m.x151)**2 + (m.x213 - m.x241)**2) + 1 / sqrt((m.x33 - m.x62)**2 + (m.x123
    - m.x152)**2 + (m.x213 - m.x242)**2) + 1 / sqrt((m.x33 - m.x63)**2 + (
    m.x123 - m.x153)**2 + (m.x213 - m.x243)**2) + 1 / sqrt((m.x33 - m.x64)**2
    + (m.x123 - m.x154)**2 + (m.x213 - m.x244)**2) + 1 / sqrt((m.x33 - m.x65)
    **2 + (m.x123 - m.x155)**2 + (m.x213 - m.x245)**2) + 1 / sqrt((m.x33 -
    m.x66)**2 + (m.x123 - m.x156)**2 + (m.x213 - m.x246)**2) + 1 / sqrt((m.x33
    - m.x67)**2 + (m.x123 - m.x157)**2 + (m.x213 - m.x247)**2) + 1 / sqrt((
    m.x33 - m.x68)**2 + (m.x123 - m.x158)**2 + (m.x213 - m.x248)**2) + 1 /
    sqrt((m.x33 - m.x69)**2 + (m.x123 - m.x159)**2 + (m.x213 - m.x249)**2) + 1
    / sqrt((m.x33 - m.x70)**2 + (m.x123 - m.x160)**2 + (m.x213 - m.x250)**2)
    + 1 / sqrt((m.x33 - m.x71)**2 + (m.x123 - m.x161)**2 + (m.x213 - m.x251)**
    2) + 1 / sqrt((m.x33 - m.x72)**2 + (m.x123 - m.x162)**2 + (m.x213 - m.x252)
    **2) + 1 / sqrt((m.x33 - m.x73)**2 + (m.x123 - m.x163)**2 + (m.x213 -
    m.x253)**2) + 1 / sqrt((m.x33 - m.x74)**2 + (m.x123 - m.x164)**2 + (m.x213
    - m.x254)**2) + 1 / sqrt((m.x33 - m.x75)**2 + (m.x123 - m.x165)**2 + (
    m.x213 - m.x255)**2) + 1 / sqrt((m.x33 - m.x76)**2 + (m.x123 - m.x166)**2
    + (m.x213 - m.x256)**2) + 1 / sqrt((m.x33 - m.x77)**2 + (m.x123 - m.x167)
    **2 + (m.x213 - m.x257)**2) + 1 / sqrt((m.x33 - m.x78)**2 + (m.x123 -
    m.x168)**2 + (m.x213 - m.x258)**2) + 1 / sqrt((m.x33 - m.x79)**2 + (m.x123
    - m.x169)**2 + (m.x213 - m.x259)**2) + 1 / sqrt((m.x33 - m.x80)**2 + (
    m.x123 - m.x170)**2 + (m.x213 - m.x260)**2) + 1 / sqrt((m.x33 - m.x81)**2
    + (m.x123 - m.x171)**2 + (m.x213 - m.x261)**2) + 1 / sqrt((m.x33 - m.x82)
    **2 + (m.x123 - m.x172)**2 + (m.x213 - m.x262)**2) + 1 / sqrt((m.x33 -
    m.x83)**2 + (m.x123 - m.x173)**2 + (m.x213 - m.x263)**2) + 1 / sqrt((m.x33
    - m.x84)**2 + (m.x123 - m.x174)**2 + (m.x213 - m.x264)**2) + 1 / sqrt((
    m.x33 - m.x85)**2 + (m.x123 - m.x175)**2 + (m.x213 - m.x265)**2) + 1 /
    sqrt((m.x33 - m.x86)**2 + (m.x123 - m.x176)**2 + (m.x213 - m.x266)**2) + 1
    / sqrt((m.x33 - m.x87)**2 + (m.x123 - m.x177)**2 + (m.x213 - m.x267)**2)
    + 1 / sqrt((m.x33 - m.x88)**2 + (m.x123 - m.x178)**2 + (m.x213 - m.x268)**
    2) + 1 / sqrt((m.x33 - m.x89)**2 + (m.x123 - m.x179)**2 + (m.x213 - m.x269)
    **2) + 1 / sqrt((m.x33 - m.x90)**2 + (m.x123 - m.x180)**2 + (m.x213 -
    m.x270)**2) + 1 / sqrt((m.x34 - m.x35)**2 + (m.x124 - m.x125)**2 + (m.x214
    - m.x215)**2) + 1 / sqrt((m.x34 - m.x36)**2 + (m.x124 - m.x126)**2 + (
    m.x214 - m.x216)**2) + 1 / sqrt((m.x34 - m.x37)**2 + (m.x124 - m.x127)**2
    + (m.x214 - m.x217)**2) + 1 / sqrt((m.x34 - m.x38)**2 + (m.x124 - m.x128)
    **2 + (m.x214 - m.x218)**2) + 1 / sqrt((m.x34 - m.x39)**2 + (m.x124 -
    m.x129)**2 + (m.x214 - m.x219)**2) + 1 / sqrt((m.x34 - m.x40)**2 + (m.x124
    - m.x130)**2 + (m.x214 - m.x220)**2) + 1 / sqrt((m.x34 - m.x41)**2 + (
    m.x124 - m.x131)**2 + (m.x214 - m.x221)**2) + 1 / sqrt((m.x34 - m.x42)**2
    + (m.x124 - m.x132)**2 + (m.x214 - m.x222)**2) + 1 / sqrt((m.x34 - m.x43)
    **2 + (m.x124 - m.x133)**2 + (m.x214 - m.x223)**2) + 1 / sqrt((m.x34 -
    m.x44)**2 + (m.x124 - m.x134)**2 + (m.x214 - m.x224)**2) + 1 / sqrt((m.x34
    - m.x45)**2 + (m.x124 - m.x135)**2 + (m.x214 - m.x225)**2) + 1 / sqrt((
    m.x34 - m.x46)**2 + (m.x124 - m.x136)**2 + (m.x214 - m.x226)**2) + 1 /
    sqrt((m.x34 - m.x47)**2 + (m.x124 - m.x137)**2 + (m.x214 - m.x227)**2) + 1
    / sqrt((m.x34 - m.x48)**2 + (m.x124 - m.x138)**2 + (m.x214 - m.x228)**2)
    + 1 / sqrt((m.x34 - m.x49)**2 + (m.x124 - m.x139)**2 + (m.x214 - m.x229)**
    2) + 1 / sqrt((m.x34 - m.x50)**2 + (m.x124 - m.x140)**2 + (m.x214 - m.x230)
    **2) + 1 / sqrt((m.x34 - m.x51)**2 + (m.x124 - m.x141)**2 + (m.x214 -
    m.x231)**2) + 1 / sqrt((m.x34 - m.x52)**2 + (m.x124 - m.x142)**2 + (m.x214
    - m.x232)**2) + 1 / sqrt((m.x34 - m.x53)**2 + (m.x124 - m.x143)**2 + (
    m.x214 - m.x233)**2) + 1 / sqrt((m.x34 - m.x54)**2 + (m.x124 - m.x144)**2
    + (m.x214 - m.x234)**2) + 1 / sqrt((m.x34 - m.x55)**2 + (m.x124 - m.x145)
    **2 + (m.x214 - m.x235)**2) + 1 / sqrt((m.x34 - m.x56)**2 + (m.x124 -
    m.x146)**2 + (m.x214 - m.x236)**2) + 1 / sqrt((m.x34 - m.x57)**2 + (m.x124
    - m.x147)**2 + (m.x214 - m.x237)**2) + 1 / sqrt((m.x34 - m.x58)**2 + (
    m.x124 - m.x148)**2 + (m.x214 - m.x238)**2) + 1 / sqrt((m.x34 - m.x59)**2
    + (m.x124 - m.x149)**2 + (m.x214 - m.x239)**2) + 1 / sqrt((m.x34 - m.x60)
    **2 + (m.x124 - m.x150)**2 + (m.x214 - m.x240)**2) + 1 / sqrt((m.x34 -
    m.x61)**2 + (m.x124 - m.x151)**2 + (m.x214 - m.x241)**2) + 1 / sqrt((m.x34
    - m.x62)**2 + (m.x124 - m.x152)**2 + (m.x214 - m.x242)**2) + 1 / sqrt((
    m.x34 - m.x63)**2 + (m.x124 - m.x153)**2 + (m.x214 - m.x243)**2) + 1 /
    sqrt((m.x34 - m.x64)**2 + (m.x124 - m.x154)**2 + (m.x214 - m.x244)**2) + 1
    / sqrt((m.x34 - m.x65)**2 + (m.x124 - m.x155)**2 + (m.x214 - m.x245)**2)
    + 1 / sqrt((m.x34 - m.x66)**2 + (m.x124 - m.x156)**2 + (m.x214 - m.x246)**
    2) + 1 / sqrt((m.x34 - m.x67)**2 + (m.x124 - m.x157)**2 + (m.x214 - m.x247)
    **2) + 1 / sqrt((m.x34 - m.x68)**2 + (m.x124 - m.x158)**2 + (m.x214 -
    m.x248)**2) + 1 / sqrt((m.x34 - m.x69)**2 + (m.x124 - m.x159)**2 + (m.x214
    - m.x249)**2) + 1 / sqrt((m.x34 - m.x70)**2 + (m.x124 - m.x160)**2 + (
    m.x214 - m.x250)**2) + 1 / sqrt((m.x34 - m.x71)**2 + (m.x124 - m.x161)**2
    + (m.x214 - m.x251)**2) + 1 / sqrt((m.x34 - m.x72)**2 + (m.x124 - m.x162)
    **2 + (m.x214 - m.x252)**2) + 1 / sqrt((m.x34 - m.x73)**2 + (m.x124 -
    m.x163)**2 + (m.x214 - m.x253)**2) + 1 / sqrt((m.x34 - m.x74)**2 + (m.x124
    - m.x164)**2 + (m.x214 - m.x254)**2) + 1 / sqrt((m.x34 - m.x75)**2 + (
    m.x124 - m.x165)**2 + (m.x214 - m.x255)**2) + 1 / sqrt((m.x34 - m.x76)**2
    + (m.x124 - m.x166)**2 + (m.x214 - m.x256)**2) + 1 / sqrt((m.x34 - m.x77)
    **2 + (m.x124 - m.x167)**2 + (m.x214 - m.x257)**2) + 1 / sqrt((m.x34 -
    m.x78)**2 + (m.x124 - m.x168)**2 + (m.x214 - m.x258)**2) + 1 / sqrt((m.x34
    - m.x79)**2 + (m.x124 - m.x169)**2 + (m.x214 - m.x259)**2) + 1 / sqrt((
    m.x34 - m.x80)**2 + (m.x124 - m.x170)**2 + (m.x214 - m.x260)**2) + 1 /
    sqrt((m.x34 - m.x81)**2 + (m.x124 - m.x171)**2 + (m.x214 - m.x261)**2) + 1
    / sqrt((m.x34 - m.x82)**2 + (m.x124 - m.x172)**2 + (m.x214 - m.x262)**2)
    + 1 / sqrt((m.x34 - m.x83)**2 + (m.x124 - m.x173)**2 + (m.x214 - m.x263)**
    2) + 1 / sqrt((m.x34 - m.x84)**2 + (m.x124 - m.x174)**2 + (m.x214 - m.x264)
    **2) + 1 / sqrt((m.x34 - m.x85)**2 + (m.x124 - m.x175)**2 + (m.x214 -
    m.x265)**2) + 1 / sqrt((m.x34 - m.x86)**2 + (m.x124 - m.x176)**2 + (m.x214
    - m.x266)**2) + 1 / sqrt((m.x34 - m.x87)**2 + (m.x124 - m.x177)**2 + (
    m.x214 - m.x267)**2) + 1 / sqrt((m.x34 - m.x88)**2 + (m.x124 - m.x178)**2
    + (m.x214 - m.x268)**2) + 1 / sqrt((m.x34 - m.x89)**2 + (m.x124 - m.x179)
    **2 + (m.x214 - m.x269)**2) + 1 / sqrt((m.x34 - m.x90)**2 + (m.x124 -
    m.x180)**2 + (m.x214 - m.x270)**2) + 1 / sqrt((m.x35 - m.x36)**2 + (m.x125
    - m.x126)**2 + (m.x215 - m.x216)**2) + 1 / sqrt((m.x35 - m.x37)**2 + (
    m.x125 - m.x127)**2 + (m.x215 - m.x217)**2) + 1 / sqrt((m.x35 - m.x38)**2
    + (m.x125 - m.x128)**2 + (m.x215 - m.x218)**2) + 1 / sqrt((m.x35 - m.x39)
    **2 + (m.x125 - m.x129)**2 + (m.x215 - m.x219)**2) + 1 / sqrt((m.x35 -
    m.x40)**2 + (m.x125 - m.x130)**2 + (m.x215 - m.x220)**2) + 1 / sqrt((m.x35
    - m.x41)**2 + (m.x125 - m.x131)**2 + (m.x215 - m.x221)**2) + 1 / sqrt((
    m.x35 - m.x42)**2 + (m.x125 - m.x132)**2 + (m.x215 - m.x222)**2) + 1 /
    sqrt((m.x35 - m.x43)**2 + (m.x125 - m.x133)**2 + (m.x215 - m.x223)**2) + 1
    / sqrt((m.x35 - m.x44)**2 + (m.x125 - m.x134)**2 + (m.x215 - m.x224)**2)
    + 1 / sqrt((m.x35 - m.x45)**2 + (m.x125 - m.x135)**2 + (m.x215 - m.x225)**
    2) + 1 / sqrt((m.x35 - m.x46)**2 + (m.x125 - m.x136)**2 + (m.x215 - m.x226)
    **2) + 1 / sqrt((m.x35 - m.x47)**2 + (m.x125 - m.x137)**2 + (m.x215 -
    m.x227)**2) + 1 / sqrt((m.x35 - m.x48)**2 + (m.x125 - m.x138)**2 + (m.x215
    - m.x228)**2) + 1 / sqrt((m.x35 - m.x49)**2 + (m.x125 - m.x139)**2 + (
    m.x215 - m.x229)**2) + 1 / sqrt((m.x35 - m.x50)**2 + (m.x125 - m.x140)**2
    + (m.x215 - m.x230)**2) + 1 / sqrt((m.x35 - m.x51)**2 + (m.x125 - m.x141)
    **2 + (m.x215 - m.x231)**2) + 1 / sqrt((m.x35 - m.x52)**2 + (m.x125 -
    m.x142)**2 + (m.x215 - m.x232)**2) + 1 / sqrt((m.x35 - m.x53)**2 + (m.x125
    - m.x143)**2 + (m.x215 - m.x233)**2) + 1 / sqrt((m.x35 - m.x54)**2 + (
    m.x125 - m.x144)**2 + (m.x215 - m.x234)**2) + 1 / sqrt((m.x35 - m.x55)**2
    + (m.x125 - m.x145)**2 + (m.x215 - m.x235)**2) + 1 / sqrt((m.x35 - m.x56)
    **2 + (m.x125 - m.x146)**2 + (m.x215 - m.x236)**2) + 1 / sqrt((m.x35 -
    m.x57)**2 + (m.x125 - m.x147)**2 + (m.x215 - m.x237)**2) + 1 / sqrt((m.x35
    - m.x58)**2 + (m.x125 - m.x148)**2 + (m.x215 - m.x238)**2) + 1 / sqrt((
    m.x35 - m.x59)**2 + (m.x125 - m.x149)**2 + (m.x215 - m.x239)**2) + 1 /
    sqrt((m.x35 - m.x60)**2 + (m.x125 - m.x150)**2 + (m.x215 - m.x240)**2) + 1
    / sqrt((m.x35 - m.x61)**2 + (m.x125 - m.x151)**2 + (m.x215 - m.x241)**2)
    + 1 / sqrt((m.x35 - m.x62)**2 + (m.x125 - m.x152)**2 + (m.x215 - m.x242)**
    2) + 1 / sqrt((m.x35 - m.x63)**2 + (m.x125 - m.x153)**2 + (m.x215 - m.x243)
    **2) + 1 / sqrt((m.x35 - m.x64)**2 + (m.x125 - m.x154)**2 + (m.x215 -
    m.x244)**2) + 1 / sqrt((m.x35 - m.x65)**2 + (m.x125 - m.x155)**2 + (m.x215
    - m.x245)**2) + 1 / sqrt((m.x35 - m.x66)**2 + (m.x125 - m.x156)**2 + (
    m.x215 - m.x246)**2) + 1 / sqrt((m.x35 - m.x67)**2 + (m.x125 - m.x157)**2
    + (m.x215 - m.x247)**2) + 1 / sqrt((m.x35 - m.x68)**2 + (m.x125 - m.x158)
    **2 + (m.x215 - m.x248)**2) + 1 / sqrt((m.x35 - m.x69)**2 + (m.x125 -
    m.x159)**2 + (m.x215 - m.x249)**2) + 1 / sqrt((m.x35 - m.x70)**2 + (m.x125
    - m.x160)**2 + (m.x215 - m.x250)**2) + 1 / sqrt((m.x35 - m.x71)**2 + (
    m.x125 - m.x161)**2 + (m.x215 - m.x251)**2) + 1 / sqrt((m.x35 - m.x72)**2
    + (m.x125 - m.x162)**2 + (m.x215 - m.x252)**2) + 1 / sqrt((m.x35 - m.x73)
    **2 + (m.x125 - m.x163)**2 + (m.x215 - m.x253)**2) + 1 / sqrt((m.x35 -
    m.x74)**2 + (m.x125 - m.x164)**2 + (m.x215 - m.x254)**2) + 1 / sqrt((m.x35
    - m.x75)**2 + (m.x125 - m.x165)**2 + (m.x215 - m.x255)**2) + 1 / sqrt((
    m.x35 - m.x76)**2 + (m.x125 - m.x166)**2 + (m.x215 - m.x256)**2) + 1 /
    sqrt((m.x35 - m.x77)**2 + (m.x125 - m.x167)**2 + (m.x215 - m.x257)**2) + 1
    / sqrt((m.x35 - m.x78)**2 + (m.x125 - m.x168)**2 + (m.x215 - m.x258)**2)
    + 1 / sqrt((m.x35 - m.x79)**2 + (m.x125 - m.x169)**2 + (m.x215 - m.x259)**
    2) + 1 / sqrt((m.x35 - m.x80)**2 + (m.x125 - m.x170)**2 + (m.x215 - m.x260)
    **2) + 1 / sqrt((m.x35 - m.x81)**2 + (m.x125 - m.x171)**2 + (m.x215 -
    m.x261)**2) + 1 / sqrt((m.x35 - m.x82)**2 + (m.x125 - m.x172)**2 + (m.x215
    - m.x262)**2) + 1 / sqrt((m.x35 - m.x83)**2 + (m.x125 - m.x173)**2 + (
    m.x215 - m.x263)**2) + 1 / sqrt((m.x35 - m.x84)**2 + (m.x125 - m.x174)**2
    + (m.x215 - m.x264)**2) + 1 / sqrt((m.x35 - m.x85)**2 + (m.x125 - m.x175)
    **2 + (m.x215 - m.x265)**2) + 1 / sqrt((m.x35 - m.x86)**2 + (m.x125 -
    m.x176)**2 + (m.x215 - m.x266)**2) + 1 / sqrt((m.x35 - m.x87)**2 + (m.x125
    - m.x177)**2 + (m.x215 - m.x267)**2) + 1 / sqrt((m.x35 - m.x88)**2 + (
    m.x125 - m.x178)**2 + (m.x215 - m.x268)**2) + 1 / sqrt((m.x35 - m.x89)**2
    + (m.x125 - m.x179)**2 + (m.x215 - m.x269)**2) + 1 / sqrt((m.x35 - m.x90)
    **2 + (m.x125 - m.x180)**2 + (m.x215 - m.x270)**2) + 1 / sqrt((m.x36 -
    m.x37)**2 + (m.x126 - m.x127)**2 + (m.x216 - m.x217)**2) + 1 / sqrt((m.x36
    - m.x38)**2 + (m.x126 - m.x128)**2 + (m.x216 - m.x218)**2) + 1 / sqrt((
    m.x36 - m.x39)**2 + (m.x126 - m.x129)**2 + (m.x216 - m.x219)**2) + 1 /
    sqrt((m.x36 - m.x40)**2 + (m.x126 - m.x130)**2 + (m.x216 - m.x220)**2) + 1
    / sqrt((m.x36 - m.x41)**2 + (m.x126 - m.x131)**2 + (m.x216 - m.x221)**2)
    + 1 / sqrt((m.x36 - m.x42)**2 + (m.x126 - m.x132)**2 + (m.x216 - m.x222)**
    2) + 1 / sqrt((m.x36 - m.x43)**2 + (m.x126 - m.x133)**2 + (m.x216 - m.x223)
    **2) + 1 / sqrt((m.x36 - m.x44)**2 + (m.x126 - m.x134)**2 + (m.x216 -
    m.x224)**2) + 1 / sqrt((m.x36 - m.x45)**2 + (m.x126 - m.x135)**2 + (m.x216
    - m.x225)**2) + 1 / sqrt((m.x36 - m.x46)**2 + (m.x126 - m.x136)**2 + (
    m.x216 - m.x226)**2) + 1 / sqrt((m.x36 - m.x47)**2 + (m.x126 - m.x137)**2
    + (m.x216 - m.x227)**2) + 1 / sqrt((m.x36 - m.x48)**2 + (m.x126 - m.x138)
    **2 + (m.x216 - m.x228)**2) + 1 / sqrt((m.x36 - m.x49)**2 + (m.x126 -
    m.x139)**2 + (m.x216 - m.x229)**2) + 1 / sqrt((m.x36 - m.x50)**2 + (m.x126
    - m.x140)**2 + (m.x216 - m.x230)**2) + 1 / sqrt((m.x36 - m.x51)**2 + (
    m.x126 - m.x141)**2 + (m.x216 - m.x231)**2) + 1 / sqrt((m.x36 - m.x52)**2
    + (m.x126 - m.x142)**2 + (m.x216 - m.x232)**2) + 1 / sqrt((m.x36 - m.x53)
    **2 + (m.x126 - m.x143)**2 + (m.x216 - m.x233)**2) + 1 / sqrt((m.x36 -
    m.x54)**2 + (m.x126 - m.x144)**2 + (m.x216 - m.x234)**2) + 1 / sqrt((m.x36
    - m.x55)**2 + (m.x126 - m.x145)**2 + (m.x216 - m.x235)**2) + 1 / sqrt((
    m.x36 - m.x56)**2 + (m.x126 - m.x146)**2 + (m.x216 - m.x236)**2) + 1 /
    sqrt((m.x36 - m.x57)**2 + (m.x126 - m.x147)**2 + (m.x216 - m.x237)**2) + 1
    / sqrt((m.x36 - m.x58)**2 + (m.x126 - m.x148)**2 + (m.x216 - m.x238)**2)
    + 1 / sqrt((m.x36 - m.x59)**2 + (m.x126 - m.x149)**2 + (m.x216 - m.x239)**
    2) + 1 / sqrt((m.x36 - m.x60)**2 + (m.x126 - m.x150)**2 + (m.x216 - m.x240)
    **2) + 1 / sqrt((m.x36 - m.x61)**2 + (m.x126 - m.x151)**2 + (m.x216 -
    m.x241)**2) + 1 / sqrt((m.x36 - m.x62)**2 + (m.x126 - m.x152)**2 + (m.x216
    - m.x242)**2) + 1 / sqrt((m.x36 - m.x63)**2 + (m.x126 - m.x153)**2 + (
    m.x216 - m.x243)**2) + 1 / sqrt((m.x36 - m.x64)**2 + (m.x126 - m.x154)**2
    + (m.x216 - m.x244)**2) + 1 / sqrt((m.x36 - m.x65)**2 + (m.x126 - m.x155)
    **2 + (m.x216 - m.x245)**2) + 1 / sqrt((m.x36 - m.x66)**2 + (m.x126 -
    m.x156)**2 + (m.x216 - m.x246)**2) + 1 / sqrt((m.x36 - m.x67)**2 + (m.x126
    - m.x157)**2 + (m.x216 - m.x247)**2) + 1 / sqrt((m.x36 - m.x68)**2 + (
    m.x126 - m.x158)**2 + (m.x216 - m.x248)**2) + 1 / sqrt((m.x36 - m.x69)**2
    + (m.x126 - m.x159)**2 + (m.x216 - m.x249)**2) + 1 / sqrt((m.x36 - m.x70)
    **2 + (m.x126 - m.x160)**2 + (m.x216 - m.x250)**2) + 1 / sqrt((m.x36 -
    m.x71)**2 + (m.x126 - m.x161)**2 + (m.x216 - m.x251)**2) + 1 / sqrt((m.x36
    - m.x72)**2 + (m.x126 - m.x162)**2 + (m.x216 - m.x252)**2) + 1 / sqrt((
    m.x36 - m.x73)**2 + (m.x126 - m.x163)**2 + (m.x216 - m.x253)**2) + 1 /
    sqrt((m.x36 - m.x74)**2 + (m.x126 - m.x164)**2 + (m.x216 - m.x254)**2) + 1
    / sqrt((m.x36 - m.x75)**2 + (m.x126 - m.x165)**2 + (m.x216 - m.x255)**2)
    + 1 / sqrt((m.x36 - m.x76)**2 + (m.x126 - m.x166)**2 + (m.x216 - m.x256)**
    2) + 1 / sqrt((m.x36 - m.x77)**2 + (m.x126 - m.x167)**2 + (m.x216 - m.x257)
    **2) + 1 / sqrt((m.x36 - m.x78)**2 + (m.x126 - m.x168)**2 + (m.x216 -
    m.x258)**2) + 1 / sqrt((m.x36 - m.x79)**2 + (m.x126 - m.x169)**2 + (m.x216
    - m.x259)**2) + 1 / sqrt((m.x36 - m.x80)**2 + (m.x126 - m.x170)**2 + (
    m.x216 - m.x260)**2) + 1 / sqrt((m.x36 - m.x81)**2 + (m.x126 - m.x171)**2
    + (m.x216 - m.x261)**2) + 1 / sqrt((m.x36 - m.x82)**2 + (m.x126 - m.x172)
    **2 + (m.x216 - m.x262)**2) + 1 / sqrt((m.x36 - m.x83)**2 + (m.x126 -
    m.x173)**2 + (m.x216 - m.x263)**2) + 1 / sqrt((m.x36 - m.x84)**2 + (m.x126
    - m.x174)**2 + (m.x216 - m.x264)**2) + 1 / sqrt((m.x36 - m.x85)**2 + (
    m.x126 - m.x175)**2 + (m.x216 - m.x265)**2) + 1 / sqrt((m.x36 - m.x86)**2
    + (m.x126 - m.x176)**2 + (m.x216 - m.x266)**2) + 1 / sqrt((m.x36 - m.x87)
    **2 + (m.x126 - m.x177)**2 + (m.x216 - m.x267)**2) + 1 / sqrt((m.x36 -
    m.x88)**2 + (m.x126 - m.x178)**2 + (m.x216 - m.x268)**2) + 1 / sqrt((m.x36
    - m.x89)**2 + (m.x126 - m.x179)**2 + (m.x216 - m.x269)**2) + 1 / sqrt((
    m.x36 - m.x90)**2 + (m.x126 - m.x180)**2 + (m.x216 - m.x270)**2) + 1 /
    sqrt((m.x37 - m.x38)**2 + (m.x127 - m.x128)**2 + (m.x217 - m.x218)**2) + 1
    / sqrt((m.x37 - m.x39)**2 + (m.x127 - m.x129)**2 + (m.x217 - m.x219)**2)
    + 1 / sqrt((m.x37 - m.x40)**2 + (m.x127 - m.x130)**2 + (m.x217 - m.x220)**
    2) + 1 / sqrt((m.x37 - m.x41)**2 + (m.x127 - m.x131)**2 + (m.x217 - m.x221)
    **2) + 1 / sqrt((m.x37 - m.x42)**2 + (m.x127 - m.x132)**2 + (m.x217 -
    m.x222)**2) + 1 / sqrt((m.x37 - m.x43)**2 + (m.x127 - m.x133)**2 + (m.x217
    - m.x223)**2) + 1 / sqrt((m.x37 - m.x44)**2 + (m.x127 - m.x134)**2 + (
    m.x217 - m.x224)**2) + 1 / sqrt((m.x37 - m.x45)**2 + (m.x127 - m.x135)**2
    + (m.x217 - m.x225)**2) + 1 / sqrt((m.x37 - m.x46)**2 + (m.x127 - m.x136)
    **2 + (m.x217 - m.x226)**2) + 1 / sqrt((m.x37 - m.x47)**2 + (m.x127 -
    m.x137)**2 + (m.x217 - m.x227)**2) + 1 / sqrt((m.x37 - m.x48)**2 + (m.x127
    - m.x138)**2 + (m.x217 - m.x228)**2) + 1 / sqrt((m.x37 - m.x49)**2 + (
    m.x127 - m.x139)**2 + (m.x217 - m.x229)**2) + 1 / sqrt((m.x37 - m.x50)**2
    + (m.x127 - m.x140)**2 + (m.x217 - m.x230)**2) + 1 / sqrt((m.x37 - m.x51)
    **2 + (m.x127 - m.x141)**2 + (m.x217 - m.x231)**2) + 1 / sqrt((m.x37 -
    m.x52)**2 + (m.x127 - m.x142)**2 + (m.x217 - m.x232)**2) + 1 / sqrt((m.x37
    - m.x53)**2 + (m.x127 - m.x143)**2 + (m.x217 - m.x233)**2) + 1 / sqrt((
    m.x37 - m.x54)**2 + (m.x127 - m.x144)**2 + (m.x217 - m.x234)**2) + 1 /
    sqrt((m.x37 - m.x55)**2 + (m.x127 - m.x145)**2 + (m.x217 - m.x235)**2) + 1
    / sqrt((m.x37 - m.x56)**2 + (m.x127 - m.x146)**2 + (m.x217 - m.x236)**2)
    + 1 / sqrt((m.x37 - m.x57)**2 + (m.x127 - m.x147)**2 + (m.x217 - m.x237)**
    2) + 1 / sqrt((m.x37 - m.x58)**2 + (m.x127 - m.x148)**2 + (m.x217 - m.x238)
    **2) + 1 / sqrt((m.x37 - m.x59)**2 + (m.x127 - m.x149)**2 + (m.x217 -
    m.x239)**2) + 1 / sqrt((m.x37 - m.x60)**2 + (m.x127 - m.x150)**2 + (m.x217
    - m.x240)**2) + 1 / sqrt((m.x37 - m.x61)**2 + (m.x127 - m.x151)**2 + (
    m.x217 - m.x241)**2) + 1 / sqrt((m.x37 - m.x62)**2 + (m.x127 - m.x152)**2
    + (m.x217 - m.x242)**2) + 1 / sqrt((m.x37 - m.x63)**2 + (m.x127 - m.x153)
    **2 + (m.x217 - m.x243)**2) + 1 / sqrt((m.x37 - m.x64)**2 + (m.x127 -
    m.x154)**2 + (m.x217 - m.x244)**2) + 1 / sqrt((m.x37 - m.x65)**2 + (m.x127
    - m.x155)**2 + (m.x217 - m.x245)**2) + 1 / sqrt((m.x37 - m.x66)**2 + (
    m.x127 - m.x156)**2 + (m.x217 - m.x246)**2) + 1 / sqrt((m.x37 - m.x67)**2
    + (m.x127 - m.x157)**2 + (m.x217 - m.x247)**2) + 1 / sqrt((m.x37 - m.x68)
    **2 + (m.x127 - m.x158)**2 + (m.x217 - m.x248)**2) + 1 / sqrt((m.x37 -
    m.x69)**2 + (m.x127 - m.x159)**2 + (m.x217 - m.x249)**2) + 1 / sqrt((m.x37
    - m.x70)**2 + (m.x127 - m.x160)**2 + (m.x217 - m.x250)**2) + 1 / sqrt((
    m.x37 - m.x71)**2 + (m.x127 - m.x161)**2 + (m.x217 - m.x251)**2) + 1 /
    sqrt((m.x37 - m.x72)**2 + (m.x127 - m.x162)**2 + (m.x217 - m.x252)**2) + 1
    / sqrt((m.x37 - m.x73)**2 + (m.x127 - m.x163)**2 + (m.x217 - m.x253)**2)
    + 1 / sqrt((m.x37 - m.x74)**2 + (m.x127 - m.x164)**2 + (m.x217 - m.x254)**
    2) + 1 / sqrt((m.x37 - m.x75)**2 + (m.x127 - m.x165)**2 + (m.x217 - m.x255)
    **2) + 1 / sqrt((m.x37 - m.x76)**2 + (m.x127 - m.x166)**2 + (m.x217 -
    m.x256)**2) + 1 / sqrt((m.x37 - m.x77)**2 + (m.x127 - m.x167)**2 + (m.x217
    - m.x257)**2) + 1 / sqrt((m.x37 - m.x78)**2 + (m.x127 - m.x168)**2 + (
    m.x217 - m.x258)**2) + 1 / sqrt((m.x37 - m.x79)**2 + (m.x127 - m.x169)**2
    + (m.x217 - m.x259)**2) + 1 / sqrt((m.x37 - m.x80)**2 + (m.x127 - m.x170)
    **2 + (m.x217 - m.x260)**2) + 1 / sqrt((m.x37 - m.x81)**2 + (m.x127 -
    m.x171)**2 + (m.x217 - m.x261)**2) + 1 / sqrt((m.x37 - m.x82)**2 + (m.x127
    - m.x172)**2 + (m.x217 - m.x262)**2) + 1 / sqrt((m.x37 - m.x83)**2 + (
    m.x127 - m.x173)**2 + (m.x217 - m.x263)**2) + 1 / sqrt((m.x37 - m.x84)**2
    + (m.x127 - m.x174)**2 + (m.x217 - m.x264)**2) + 1 / sqrt((m.x37 - m.x85)
    **2 + (m.x127 - m.x175)**2 + (m.x217 - m.x265)**2) + 1 / sqrt((m.x37 -
    m.x86)**2 + (m.x127 - m.x176)**2 + (m.x217 - m.x266)**2) + 1 / sqrt((m.x37
    - m.x87)**2 + (m.x127 - m.x177)**2 + (m.x217 - m.x267)**2) + 1 / sqrt((
    m.x37 - m.x88)**2 + (m.x127 - m.x178)**2 + (m.x217 - m.x268)**2) + 1 /
    sqrt((m.x37 - m.x89)**2 + (m.x127 - m.x179)**2 + (m.x217 - m.x269)**2) + 1
    / sqrt((m.x37 - m.x90)**2 + (m.x127 - m.x180)**2 + (m.x217 - m.x270)**2)
    + 1 / sqrt((m.x38 - m.x39)**2 + (m.x128 - m.x129)**2 + (m.x218 - m.x219)**
    2) + 1 / sqrt((m.x38 - m.x40)**2 + (m.x128 - m.x130)**2 + (m.x218 - m.x220)
    **2) + 1 / sqrt((m.x38 - m.x41)**2 + (m.x128 - m.x131)**2 + (m.x218 -
    m.x221)**2) + 1 / sqrt((m.x38 - m.x42)**2 + (m.x128 - m.x132)**2 + (m.x218
    - m.x222)**2) + 1 / sqrt((m.x38 - m.x43)**2 + (m.x128 - m.x133)**2 + (
    m.x218 - m.x223)**2) + 1 / sqrt((m.x38 - m.x44)**2 + (m.x128 - m.x134)**2
    + (m.x218 - m.x224)**2) + 1 / sqrt((m.x38 - m.x45)**2 + (m.x128 - m.x135)
    **2 + (m.x218 - m.x225)**2) + 1 / sqrt((m.x38 - m.x46)**2 + (m.x128 -
    m.x136)**2 + (m.x218 - m.x226)**2) + 1 / sqrt((m.x38 - m.x47)**2 + (m.x128
    - m.x137)**2 + (m.x218 - m.x227)**2) + 1 / sqrt((m.x38 - m.x48)**2 + (
    m.x128 - m.x138)**2 + (m.x218 - m.x228)**2) + 1 / sqrt((m.x38 - m.x49)**2
    + (m.x128 - m.x139)**2 + (m.x218 - m.x229)**2) + 1 / sqrt((m.x38 - m.x50)
    **2 + (m.x128 - m.x140)**2 + (m.x218 - m.x230)**2) + 1 / sqrt((m.x38 -
    m.x51)**2 + (m.x128 - m.x141)**2 + (m.x218 - m.x231)**2) + 1 / sqrt((m.x38
    - m.x52)**2 + (m.x128 - m.x142)**2 + (m.x218 - m.x232)**2) + 1 / sqrt((
    m.x38 - m.x53)**2 + (m.x128 - m.x143)**2 + (m.x218 - m.x233)**2) + 1 /
    sqrt((m.x38 - m.x54)**2 + (m.x128 - m.x144)**2 + (m.x218 - m.x234)**2) + 1
    / sqrt((m.x38 - m.x55)**2 + (m.x128 - m.x145)**2 + (m.x218 - m.x235)**2)
    + 1 / sqrt((m.x38 - m.x56)**2 + (m.x128 - m.x146)**2 + (m.x218 - m.x236)**
    2) + 1 / sqrt((m.x38 - m.x57)**2 + (m.x128 - m.x147)**2 + (m.x218 - m.x237)
    **2) + 1 / sqrt((m.x38 - m.x58)**2 + (m.x128 - m.x148)**2 + (m.x218 -
    m.x238)**2) + 1 / sqrt((m.x38 - m.x59)**2 + (m.x128 - m.x149)**2 + (m.x218
    - m.x239)**2) + 1 / sqrt((m.x38 - m.x60)**2 + (m.x128 - m.x150)**2 + (
    m.x218 - m.x240)**2) + 1 / sqrt((m.x38 - m.x61)**2 + (m.x128 - m.x151)**2
    + (m.x218 - m.x241)**2) + 1 / sqrt((m.x38 - m.x62)**2 + (m.x128 - m.x152)
    **2 + (m.x218 - m.x242)**2) + 1 / sqrt((m.x38 - m.x63)**2 + (m.x128 -
    m.x153)**2 + (m.x218 - m.x243)**2) + 1 / sqrt((m.x38 - m.x64)**2 + (m.x128
    - m.x154)**2 + (m.x218 - m.x244)**2) + 1 / sqrt((m.x38 - m.x65)**2 + (
    m.x128 - m.x155)**2 + (m.x218 - m.x245)**2) + 1 / sqrt((m.x38 - m.x66)**2
    + (m.x128 - m.x156)**2 + (m.x218 - m.x246)**2) + 1 / sqrt((m.x38 - m.x67)
    **2 + (m.x128 - m.x157)**2 + (m.x218 - m.x247)**2) + 1 / sqrt((m.x38 -
    m.x68)**2 + (m.x128 - m.x158)**2 + (m.x218 - m.x248)**2) + 1 / sqrt((m.x38
    - m.x69)**2 + (m.x128 - m.x159)**2 + (m.x218 - m.x249)**2) + 1 / sqrt((
    m.x38 - m.x70)**2 + (m.x128 - m.x160)**2 + (m.x218 - m.x250)**2) + 1 /
    sqrt((m.x38 - m.x71)**2 + (m.x128 - m.x161)**2 + (m.x218 - m.x251)**2) + 1
    / sqrt((m.x38 - m.x72)**2 + (m.x128 - m.x162)**2 + (m.x218 - m.x252)**2)
    + 1 / sqrt((m.x38 - m.x73)**2 + (m.x128 - m.x163)**2 + (m.x218 - m.x253)**
    2) + 1 / sqrt((m.x38 - m.x74)**2 + (m.x128 - m.x164)**2 + (m.x218 - m.x254)
    **2) + 1 / sqrt((m.x38 - m.x75)**2 + (m.x128 - m.x165)**2 + (m.x218 -
    m.x255)**2) + 1 / sqrt((m.x38 - m.x76)**2 + (m.x128 - m.x166)**2 + (m.x218
    - m.x256)**2) + 1 / sqrt((m.x38 - m.x77)**2 + (m.x128 - m.x167)**2 + (
    m.x218 - m.x257)**2) + 1 / sqrt((m.x38 - m.x78)**2 + (m.x128 - m.x168)**2
    + (m.x218 - m.x258)**2) + 1 / sqrt((m.x38 - m.x79)**2 + (m.x128 - m.x169)
    **2 + (m.x218 - m.x259)**2) + 1 / sqrt((m.x38 - m.x80)**2 + (m.x128 -
    m.x170)**2 + (m.x218 - m.x260)**2) + 1 / sqrt((m.x38 - m.x81)**2 + (m.x128
    - m.x171)**2 + (m.x218 - m.x261)**2) + 1 / sqrt((m.x38 - m.x82)**2 + (
    m.x128 - m.x172)**2 + (m.x218 - m.x262)**2) + 1 / sqrt((m.x38 - m.x83)**2
    + (m.x128 - m.x173)**2 + (m.x218 - m.x263)**2) + 1 / sqrt((m.x38 - m.x84)
    **2 + (m.x128 - m.x174)**2 + (m.x218 - m.x264)**2) + 1 / sqrt((m.x38 -
    m.x85)**2 + (m.x128 - m.x175)**2 + (m.x218 - m.x265)**2) + 1 / sqrt((m.x38
    - m.x86)**2 + (m.x128 - m.x176)**2 + (m.x218 - m.x266)**2) + 1 / sqrt((
    m.x38 - m.x87)**2 + (m.x128 - m.x177)**2 + (m.x218 - m.x267)**2) + 1 /
    sqrt((m.x38 - m.x88)**2 + (m.x128 - m.x178)**2 + (m.x218 - m.x268)**2) + 1
    / sqrt((m.x38 - m.x89)**2 + (m.x128 - m.x179)**2 + (m.x218 - m.x269)**2)
    + 1 / sqrt((m.x38 - m.x90)**2 + (m.x128 - m.x180)**2 + (m.x218 - m.x270)**
    2) + 1 / sqrt((m.x39 - m.x40)**2 + (m.x129 - m.x130)**2 + (m.x219 - m.x220)
    **2) + 1 / sqrt((m.x39 - m.x41)**2 + (m.x129 - m.x131)**2 + (m.x219 -
    m.x221)**2) + 1 / sqrt((m.x39 - m.x42)**2 + (m.x129 - m.x132)**2 + (m.x219
    - m.x222)**2) + 1 / sqrt((m.x39 - m.x43)**2 + (m.x129 - m.x133)**2 + (
    m.x219 - m.x223)**2) + 1 / sqrt((m.x39 - m.x44)**2 + (m.x129 - m.x134)**2
    + (m.x219 - m.x224)**2) + 1 / sqrt((m.x39 - m.x45)**2 + (m.x129 - m.x135)
    **2 + (m.x219 - m.x225)**2) + 1 / sqrt((m.x39 - m.x46)**2 + (m.x129 -
    m.x136)**2 + (m.x219 - m.x226)**2) + 1 / sqrt((m.x39 - m.x47)**2 + (m.x129
    - m.x137)**2 + (m.x219 - m.x227)**2) + 1 / sqrt((m.x39 - m.x48)**2 + (
    m.x129 - m.x138)**2 + (m.x219 - m.x228)**2) + 1 / sqrt((m.x39 - m.x49)**2
    + (m.x129 - m.x139)**2 + (m.x219 - m.x229)**2) + 1 / sqrt((m.x39 - m.x50)
    **2 + (m.x129 - m.x140)**2 + (m.x219 - m.x230)**2) + 1 / sqrt((m.x39 -
    m.x51)**2 + (m.x129 - m.x141)**2 + (m.x219 - m.x231)**2) + 1 / sqrt((m.x39
    - m.x52)**2 + (m.x129 - m.x142)**2 + (m.x219 - m.x232)**2) + 1 / sqrt((
    m.x39 - m.x53)**2 + (m.x129 - m.x143)**2 + (m.x219 - m.x233)**2) + 1 /
    sqrt((m.x39 - m.x54)**2 + (m.x129 - m.x144)**2 + (m.x219 - m.x234)**2) + 1
    / sqrt((m.x39 - m.x55)**2 + (m.x129 - m.x145)**2 + (m.x219 - m.x235)**2)
    + 1 / sqrt((m.x39 - m.x56)**2 + (m.x129 - m.x146)**2 + (m.x219 - m.x236)**
    2) + 1 / sqrt((m.x39 - m.x57)**2 + (m.x129 - m.x147)**2 + (m.x219 - m.x237)
    **2) + 1 / sqrt((m.x39 - m.x58)**2 + (m.x129 - m.x148)**2 + (m.x219 -
    m.x238)**2) + 1 / sqrt((m.x39 - m.x59)**2 + (m.x129 - m.x149)**2 + (m.x219
    - m.x239)**2) + 1 / sqrt((m.x39 - m.x60)**2 + (m.x129 - m.x150)**2 + (
    m.x219 - m.x240)**2) + 1 / sqrt((m.x39 - m.x61)**2 + (m.x129 - m.x151)**2
    + (m.x219 - m.x241)**2) + 1 / sqrt((m.x39 - m.x62)**2 + (m.x129 - m.x152)
    **2 + (m.x219 - m.x242)**2) + 1 / sqrt((m.x39 - m.x63)**2 + (m.x129 -
    m.x153)**2 + (m.x219 - m.x243)**2) + 1 / sqrt((m.x39 - m.x64)**2 + (m.x129
    - m.x154)**2 + (m.x219 - m.x244)**2) + 1 / sqrt((m.x39 - m.x65)**2 + (
    m.x129 - m.x155)**2 + (m.x219 - m.x245)**2) + 1 / sqrt((m.x39 - m.x66)**2
    + (m.x129 - m.x156)**2 + (m.x219 - m.x246)**2) + 1 / sqrt((m.x39 - m.x67)
    **2 + (m.x129 - m.x157)**2 + (m.x219 - m.x247)**2) + 1 / sqrt((m.x39 -
    m.x68)**2 + (m.x129 - m.x158)**2 + (m.x219 - m.x248)**2) + 1 / sqrt((m.x39
    - m.x69)**2 + (m.x129 - m.x159)**2 + (m.x219 - m.x249)**2) + 1 / sqrt((
    m.x39 - m.x70)**2 + (m.x129 - m.x160)**2 + (m.x219 - m.x250)**2) + 1 /
    sqrt((m.x39 - m.x71)**2 + (m.x129 - m.x161)**2 + (m.x219 - m.x251)**2) + 1
    / sqrt((m.x39 - m.x72)**2 + (m.x129 - m.x162)**2 + (m.x219 - m.x252)**2)
    + 1 / sqrt((m.x39 - m.x73)**2 + (m.x129 - m.x163)**2 + (m.x219 - m.x253)**
    2) + 1 / sqrt((m.x39 - m.x74)**2 + (m.x129 - m.x164)**2 + (m.x219 - m.x254)
    **2) + 1 / sqrt((m.x39 - m.x75)**2 + (m.x129 - m.x165)**2 + (m.x219 -
    m.x255)**2) + 1 / sqrt((m.x39 - m.x76)**2 + (m.x129 - m.x166)**2 + (m.x219
    - m.x256)**2) + 1 / sqrt((m.x39 - m.x77)**2 + (m.x129 - m.x167)**2 + (
    m.x219 - m.x257)**2) + 1 / sqrt((m.x39 - m.x78)**2 + (m.x129 - m.x168)**2
    + (m.x219 - m.x258)**2) + 1 / sqrt((m.x39 - m.x79)**2 + (m.x129 - m.x169)
    **2 + (m.x219 - m.x259)**2) + 1 / sqrt((m.x39 - m.x80)**2 + (m.x129 -
    m.x170)**2 + (m.x219 - m.x260)**2) + 1 / sqrt((m.x39 - m.x81)**2 + (m.x129
    - m.x171)**2 + (m.x219 - m.x261)**2) + 1 / sqrt((m.x39 - m.x82)**2 + (
    m.x129 - m.x172)**2 + (m.x219 - m.x262)**2) + 1 / sqrt((m.x39 - m.x83)**2
    + (m.x129 - m.x173)**2 + (m.x219 - m.x263)**2) + 1 / sqrt((m.x39 - m.x84)
    **2 + (m.x129 - m.x174)**2 + (m.x219 - m.x264)**2) + 1 / sqrt((m.x39 -
    m.x85)**2 + (m.x129 - m.x175)**2 + (m.x219 - m.x265)**2) + 1 / sqrt((m.x39
    - m.x86)**2 + (m.x129 - m.x176)**2 + (m.x219 - m.x266)**2) + 1 / sqrt((
    m.x39 - m.x87)**2 + (m.x129 - m.x177)**2 + (m.x219 - m.x267)**2) + 1 /
    sqrt((m.x39 - m.x88)**2 + (m.x129 - m.x178)**2 + (m.x219 - m.x268)**2) + 1
    / sqrt((m.x39 - m.x89)**2 + (m.x129 - m.x179)**2 + (m.x219 - m.x269)**2)
    + 1 / sqrt((m.x39 - m.x90)**2 + (m.x129 - m.x180)**2 + (m.x219 - m.x270)**
    2) + 1 / sqrt((m.x40 - m.x41)**2 + (m.x130 - m.x131)**2 + (m.x220 - m.x221)
    **2) + 1 / sqrt((m.x40 - m.x42)**2 + (m.x130 - m.x132)**2 + (m.x220 -
    m.x222)**2) + 1 / sqrt((m.x40 - m.x43)**2 + (m.x130 - m.x133)**2 + (m.x220
    - m.x223)**2) + 1 / sqrt((m.x40 - m.x44)**2 + (m.x130 - m.x134)**2 + (
    m.x220 - m.x224)**2) + 1 / sqrt((m.x40 - m.x45)**2 + (m.x130 - m.x135)**2
    + (m.x220 - m.x225)**2) + 1 / sqrt((m.x40 - m.x46)**2 + (m.x130 - m.x136)
    **2 + (m.x220 - m.x226)**2) + 1 / sqrt((m.x40 - m.x47)**2 + (m.x130 -
    m.x137)**2 + (m.x220 - m.x227)**2) + 1 / sqrt((m.x40 - m.x48)**2 + (m.x130
    - m.x138)**2 + (m.x220 - m.x228)**2) + 1 / sqrt((m.x40 - m.x49)**2 + (
    m.x130 - m.x139)**2 + (m.x220 - m.x229)**2) + 1 / sqrt((m.x40 - m.x50)**2
    + (m.x130 - m.x140)**2 + (m.x220 - m.x230)**2) + 1 / sqrt((m.x40 - m.x51)
    **2 + (m.x130 - m.x141)**2 + (m.x220 - m.x231)**2) + 1 / sqrt((m.x40 -
    m.x52)**2 + (m.x130 - m.x142)**2 + (m.x220 - m.x232)**2) + 1 / sqrt((m.x40
    - m.x53)**2 + (m.x130 - m.x143)**2 + (m.x220 - m.x233)**2) + 1 / sqrt((
    m.x40 - m.x54)**2 + (m.x130 - m.x144)**2 + (m.x220 - m.x234)**2) + 1 /
    sqrt((m.x40 - m.x55)**2 + (m.x130 - m.x145)**2 + (m.x220 - m.x235)**2) + 1
    / sqrt((m.x40 - m.x56)**2 + (m.x130 - m.x146)**2 + (m.x220 - m.x236)**2)
    + 1 / sqrt((m.x40 - m.x57)**2 + (m.x130 - m.x147)**2 + (m.x220 - m.x237)**
    2) + 1 / sqrt((m.x40 - m.x58)**2 + (m.x130 - m.x148)**2 + (m.x220 - m.x238)
    **2) + 1 / sqrt((m.x40 - m.x59)**2 + (m.x130 - m.x149)**2 + (m.x220 -
    m.x239)**2) + 1 / sqrt((m.x40 - m.x60)**2 + (m.x130 - m.x150)**2 + (m.x220
    - m.x240)**2) + 1 / sqrt((m.x40 - m.x61)**2 + (m.x130 - m.x151)**2 + (
    m.x220 - m.x241)**2) + 1 / sqrt((m.x40 - m.x62)**2 + (m.x130 - m.x152)**2
    + (m.x220 - m.x242)**2) + 1 / sqrt((m.x40 - m.x63)**2 + (m.x130 - m.x153)
    **2 + (m.x220 - m.x243)**2) + 1 / sqrt((m.x40 - m.x64)**2 + (m.x130 -
    m.x154)**2 + (m.x220 - m.x244)**2) + 1 / sqrt((m.x40 - m.x65)**2 + (m.x130
    - m.x155)**2 + (m.x220 - m.x245)**2) + 1 / sqrt((m.x40 - m.x66)**2 + (
    m.x130 - m.x156)**2 + (m.x220 - m.x246)**2) + 1 / sqrt((m.x40 - m.x67)**2
    + (m.x130 - m.x157)**2 + (m.x220 - m.x247)**2) + 1 / sqrt((m.x40 - m.x68)
    **2 + (m.x130 - m.x158)**2 + (m.x220 - m.x248)**2) + 1 / sqrt((m.x40 -
    m.x69)**2 + (m.x130 - m.x159)**2 + (m.x220 - m.x249)**2) + 1 / sqrt((m.x40
    - m.x70)**2 + (m.x130 - m.x160)**2 + (m.x220 - m.x250)**2) + 1 / sqrt((
    m.x40 - m.x71)**2 + (m.x130 - m.x161)**2 + (m.x220 - m.x251)**2) + 1 /
    sqrt((m.x40 - m.x72)**2 + (m.x130 - m.x162)**2 + (m.x220 - m.x252)**2) + 1
    / sqrt((m.x40 - m.x73)**2 + (m.x130 - m.x163)**2 + (m.x220 - m.x253)**2)
    + 1 / sqrt((m.x40 - m.x74)**2 + (m.x130 - m.x164)**2 + (m.x220 - m.x254)**
    2) + 1 / sqrt((m.x40 - m.x75)**2 + (m.x130 - m.x165)**2 + (m.x220 - m.x255)
    **2) + 1 / sqrt((m.x40 - m.x76)**2 + (m.x130 - m.x166)**2 + (m.x220 -
    m.x256)**2) + 1 / sqrt((m.x40 - m.x77)**2 + (m.x130 - m.x167)**2 + (m.x220
    - m.x257)**2) + 1 / sqrt((m.x40 - m.x78)**2 + (m.x130 - m.x168)**2 + (
    m.x220 - m.x258)**2) + 1 / sqrt((m.x40 - m.x79)**2 + (m.x130 - m.x169)**2
    + (m.x220 - m.x259)**2) + 1 / sqrt((m.x40 - m.x80)**2 + (m.x130 - m.x170)
    **2 + (m.x220 - m.x260)**2) + 1 / sqrt((m.x40 - m.x81)**2 + (m.x130 -
    m.x171)**2 + (m.x220 - m.x261)**2) + 1 / sqrt((m.x40 - m.x82)**2 + (m.x130
    - m.x172)**2 + (m.x220 - m.x262)**2) + 1 / sqrt((m.x40 - m.x83)**2 + (
    m.x130 - m.x173)**2 + (m.x220 - m.x263)**2) + 1 / sqrt((m.x40 - m.x84)**2
    + (m.x130 - m.x174)**2 + (m.x220 - m.x264)**2) + 1 / sqrt((m.x40 - m.x85)
    **2 + (m.x130 - m.x175)**2 + (m.x220 - m.x265)**2) + 1 / sqrt((m.x40 -
    m.x86)**2 + (m.x130 - m.x176)**2 + (m.x220 - m.x266)**2) + 1 / sqrt((m.x40
    - m.x87)**2 + (m.x130 - m.x177)**2 + (m.x220 - m.x267)**2) + 1 / sqrt((
    m.x40 - m.x88)**2 + (m.x130 - m.x178)**2 + (m.x220 - m.x268)**2) + 1 /
    sqrt((m.x40 - m.x89)**2 + (m.x130 - m.x179)**2 + (m.x220 - m.x269)**2) + 1
    / sqrt((m.x40 - m.x90)**2 + (m.x130 - m.x180)**2 + (m.x220 - m.x270)**2)
    + 1 / sqrt((m.x41 - m.x42)**2 + (m.x131 - m.x132)**2 + (m.x221 - m.x222)**
    2) + 1 / sqrt((m.x41 - m.x43)**2 + (m.x131 - m.x133)**2 + (m.x221 - m.x223)
    **2) + 1 / sqrt((m.x41 - m.x44)**2 + (m.x131 - m.x134)**2 + (m.x221 -
    m.x224)**2) + 1 / sqrt((m.x41 - m.x45)**2 + (m.x131 - m.x135)**2 + (m.x221
    - m.x225)**2) + 1 / sqrt((m.x41 - m.x46)**2 + (m.x131 - m.x136)**2 + (
    m.x221 - m.x226)**2) + 1 / sqrt((m.x41 - m.x47)**2 + (m.x131 - m.x137)**2
    + (m.x221 - m.x227)**2) + 1 / sqrt((m.x41 - m.x48)**2 + (m.x131 - m.x138)
    **2 + (m.x221 - m.x228)**2) + 1 / sqrt((m.x41 - m.x49)**2 + (m.x131 -
    m.x139)**2 + (m.x221 - m.x229)**2) + 1 / sqrt((m.x41 - m.x50)**2 + (m.x131
    - m.x140)**2 + (m.x221 - m.x230)**2) + 1 / sqrt((m.x41 - m.x51)**2 + (
    m.x131 - m.x141)**2 + (m.x221 - m.x231)**2) + 1 / sqrt((m.x41 - m.x52)**2
    + (m.x131 - m.x142)**2 + (m.x221 - m.x232)**2) + 1 / sqrt((m.x41 - m.x53)
    **2 + (m.x131 - m.x143)**2 + (m.x221 - m.x233)**2) + 1 / sqrt((m.x41 -
    m.x54)**2 + (m.x131 - m.x144)**2 + (m.x221 - m.x234)**2) + 1 / sqrt((m.x41
    - m.x55)**2 + (m.x131 - m.x145)**2 + (m.x221 - m.x235)**2) + 1 / sqrt((
    m.x41 - m.x56)**2 + (m.x131 - m.x146)**2 + (m.x221 - m.x236)**2) + 1 /
    sqrt((m.x41 - m.x57)**2 + (m.x131 - m.x147)**2 + (m.x221 - m.x237)**2) + 1
    / sqrt((m.x41 - m.x58)**2 + (m.x131 - m.x148)**2 + (m.x221 - m.x238)**2)
    + 1 / sqrt((m.x41 - m.x59)**2 + (m.x131 - m.x149)**2 + (m.x221 - m.x239)**
    2) + 1 / sqrt((m.x41 - m.x60)**2 + (m.x131 - m.x150)**2 + (m.x221 - m.x240)
    **2) + 1 / sqrt((m.x41 - m.x61)**2 + (m.x131 - m.x151)**2 + (m.x221 -
    m.x241)**2) + 1 / sqrt((m.x41 - m.x62)**2 + (m.x131 - m.x152)**2 + (m.x221
    - m.x242)**2) + 1 / sqrt((m.x41 - m.x63)**2 + (m.x131 - m.x153)**2 + (
    m.x221 - m.x243)**2) + 1 / sqrt((m.x41 - m.x64)**2 + (m.x131 - m.x154)**2
    + (m.x221 - m.x244)**2) + 1 / sqrt((m.x41 - m.x65)**2 + (m.x131 - m.x155)
    **2 + (m.x221 - m.x245)**2) + 1 / sqrt((m.x41 - m.x66)**2 + (m.x131 -
    m.x156)**2 + (m.x221 - m.x246)**2) + 1 / sqrt((m.x41 - m.x67)**2 + (m.x131
    - m.x157)**2 + (m.x221 - m.x247)**2) + 1 / sqrt((m.x41 - m.x68)**2 + (
    m.x131 - m.x158)**2 + (m.x221 - m.x248)**2) + 1 / sqrt((m.x41 - m.x69)**2
    + (m.x131 - m.x159)**2 + (m.x221 - m.x249)**2) + 1 / sqrt((m.x41 - m.x70)
    **2 + (m.x131 - m.x160)**2 + (m.x221 - m.x250)**2) + 1 / sqrt((m.x41 -
    m.x71)**2 + (m.x131 - m.x161)**2 + (m.x221 - m.x251)**2) + 1 / sqrt((m.x41
    - m.x72)**2 + (m.x131 - m.x162)**2 + (m.x221 - m.x252)**2) + 1 / sqrt((
    m.x41 - m.x73)**2 + (m.x131 - m.x163)**2 + (m.x221 - m.x253)**2) + 1 /
    sqrt((m.x41 - m.x74)**2 + (m.x131 - m.x164)**2 + (m.x221 - m.x254)**2) + 1
    / sqrt((m.x41 - m.x75)**2 + (m.x131 - m.x165)**2 + (m.x221 - m.x255)**2)
    + 1 / sqrt((m.x41 - m.x76)**2 + (m.x131 - m.x166)**2 + (m.x221 - m.x256)**
    2) + 1 / sqrt((m.x41 - m.x77)**2 + (m.x131 - m.x167)**2 + (m.x221 - m.x257)
    **2) + 1 / sqrt((m.x41 - m.x78)**2 + (m.x131 - m.x168)**2 + (m.x221 -
    m.x258)**2) + 1 / sqrt((m.x41 - m.x79)**2 + (m.x131 - m.x169)**2 + (m.x221
    - m.x259)**2) + 1 / sqrt((m.x41 - m.x80)**2 + (m.x131 - m.x170)**2 + (
    m.x221 - m.x260)**2) + 1 / sqrt((m.x41 - m.x81)**2 + (m.x131 - m.x171)**2
    + (m.x221 - m.x261)**2) + 1 / sqrt((m.x41 - m.x82)**2 + (m.x131 - m.x172)
    **2 + (m.x221 - m.x262)**2) + 1 / sqrt((m.x41 - m.x83)**2 + (m.x131 -
    m.x173)**2 + (m.x221 - m.x263)**2) + 1 / sqrt((m.x41 - m.x84)**2 + (m.x131
    - m.x174)**2 + (m.x221 - m.x264)**2) + 1 / sqrt((m.x41 - m.x85)**2 + (
    m.x131 - m.x175)**2 + (m.x221 - m.x265)**2) + 1 / sqrt((m.x41 - m.x86)**2
    + (m.x131 - m.x176)**2 + (m.x221 - m.x266)**2) + 1 / sqrt((m.x41 - m.x87)
    **2 + (m.x131 - m.x177)**2 + (m.x221 - m.x267)**2) + 1 / sqrt((m.x41 -
    m.x88)**2 + (m.x131 - m.x178)**2 + (m.x221 - m.x268)**2) + 1 / sqrt((m.x41
    - m.x89)**2 + (m.x131 - m.x179)**2 + (m.x221 - m.x269)**2) + 1 / sqrt((
    m.x41 - m.x90)**2 + (m.x131 - m.x180)**2 + (m.x221 - m.x270)**2) + 1 /
    sqrt((m.x42 - m.x43)**2 + (m.x132 - m.x133)**2 + (m.x222 - m.x223)**2) + 1
    / sqrt((m.x42 - m.x44)**2 + (m.x132 - m.x134)**2 + (m.x222 - m.x224)**2)
    + 1 / sqrt((m.x42 - m.x45)**2 + (m.x132 - m.x135)**2 + (m.x222 - m.x225)**
    2) + 1 / sqrt((m.x42 - m.x46)**2 + (m.x132 - m.x136)**2 + (m.x222 - m.x226)
    **2) + 1 / sqrt((m.x42 - m.x47)**2 + (m.x132 - m.x137)**2 + (m.x222 -
    m.x227)**2) + 1 / sqrt((m.x42 - m.x48)**2 + (m.x132 - m.x138)**2 + (m.x222
    - m.x228)**2) + 1 / sqrt((m.x42 - m.x49)**2 + (m.x132 - m.x139)**2 + (
    m.x222 - m.x229)**2) + 1 / sqrt((m.x42 - m.x50)**2 + (m.x132 - m.x140)**2
    + (m.x222 - m.x230)**2) + 1 / sqrt((m.x42 - m.x51)**2 + (m.x132 - m.x141)
    **2 + (m.x222 - m.x231)**2) + 1 / sqrt((m.x42 - m.x52)**2 + (m.x132 -
    m.x142)**2 + (m.x222 - m.x232)**2) + 1 / sqrt((m.x42 - m.x53)**2 + (m.x132
    - m.x143)**2 + (m.x222 - m.x233)**2) + 1 / sqrt((m.x42 - m.x54)**2 + (
    m.x132 - m.x144)**2 + (m.x222 - m.x234)**2) + 1 / sqrt((m.x42 - m.x55)**2
    + (m.x132 - m.x145)**2 + (m.x222 - m.x235)**2) + 1 / sqrt((m.x42 - m.x56)
    **2 + (m.x132 - m.x146)**2 + (m.x222 - m.x236)**2) + 1 / sqrt((m.x42 -
    m.x57)**2 + (m.x132 - m.x147)**2 + (m.x222 - m.x237)**2) + 1 / sqrt((m.x42
    - m.x58)**2 + (m.x132 - m.x148)**2 + (m.x222 - m.x238)**2) + 1 / sqrt((
    m.x42 - m.x59)**2 + (m.x132 - m.x149)**2 + (m.x222 - m.x239)**2) + 1 /
    sqrt((m.x42 - m.x60)**2 + (m.x132 - m.x150)**2 + (m.x222 - m.x240)**2) + 1
    / sqrt((m.x42 - m.x61)**2 + (m.x132 - m.x151)**2 + (m.x222 - m.x241)**2)
    + 1 / sqrt((m.x42 - m.x62)**2 + (m.x132 - m.x152)**2 + (m.x222 - m.x242)**
    2) + 1 / sqrt((m.x42 - m.x63)**2 + (m.x132 - m.x153)**2 + (m.x222 - m.x243)
    **2) + 1 / sqrt((m.x42 - m.x64)**2 + (m.x132 - m.x154)**2 + (m.x222 -
    m.x244)**2) + 1 / sqrt((m.x42 - m.x65)**2 + (m.x132 - m.x155)**2 + (m.x222
    - m.x245)**2) + 1 / sqrt((m.x42 - m.x66)**2 + (m.x132 - m.x156)**2 + (
    m.x222 - m.x246)**2) + 1 / sqrt((m.x42 - m.x67)**2 + (m.x132 - m.x157)**2
    + (m.x222 - m.x247)**2) + 1 / sqrt((m.x42 - m.x68)**2 + (m.x132 - m.x158)
    **2 + (m.x222 - m.x248)**2) + 1 / sqrt((m.x42 - m.x69)**2 + (m.x132 -
    m.x159)**2 + (m.x222 - m.x249)**2) + 1 / sqrt((m.x42 - m.x70)**2 + (m.x132
    - m.x160)**2 + (m.x222 - m.x250)**2) + 1 / sqrt((m.x42 - m.x71)**2 + (
    m.x132 - m.x161)**2 + (m.x222 - m.x251)**2) + 1 / sqrt((m.x42 - m.x72)**2
    + (m.x132 - m.x162)**2 + (m.x222 - m.x252)**2) + 1 / sqrt((m.x42 - m.x73)
    **2 + (m.x132 - m.x163)**2 + (m.x222 - m.x253)**2) + 1 / sqrt((m.x42 -
    m.x74)**2 + (m.x132 - m.x164)**2 + (m.x222 - m.x254)**2) + 1 / sqrt((m.x42
    - m.x75)**2 + (m.x132 - m.x165)**2 + (m.x222 - m.x255)**2) + 1 / sqrt((
    m.x42 - m.x76)**2 + (m.x132 - m.x166)**2 + (m.x222 - m.x256)**2) + 1 /
    sqrt((m.x42 - m.x77)**2 + (m.x132 - m.x167)**2 + (m.x222 - m.x257)**2) + 1
    / sqrt((m.x42 - m.x78)**2 + (m.x132 - m.x168)**2 + (m.x222 - m.x258)**2)
    + 1 / sqrt((m.x42 - m.x79)**2 + (m.x132 - m.x169)**2 + (m.x222 - m.x259)**
    2) + 1 / sqrt((m.x42 - m.x80)**2 + (m.x132 - m.x170)**2 + (m.x222 - m.x260)
    **2) + 1 / sqrt((m.x42 - m.x81)**2 + (m.x132 - m.x171)**2 + (m.x222 -
    m.x261)**2) + 1 / sqrt((m.x42 - m.x82)**2 + (m.x132 - m.x172)**2 + (m.x222
    - m.x262)**2) + 1 / sqrt((m.x42 - m.x83)**2 + (m.x132 - m.x173)**2 + (
    m.x222 - m.x263)**2) + 1 / sqrt((m.x42 - m.x84)**2 + (m.x132 - m.x174)**2
    + (m.x222 - m.x264)**2) + 1 / sqrt((m.x42 - m.x85)**2 + (m.x132 - m.x175)
    **2 + (m.x222 - m.x265)**2) + 1 / sqrt((m.x42 - m.x86)**2 + (m.x132 -
    m.x176)**2 + (m.x222 - m.x266)**2) + 1 / sqrt((m.x42 - m.x87)**2 + (m.x132
    - m.x177)**2 + (m.x222 - m.x267)**2) + 1 / sqrt((m.x42 - m.x88)**2 + (
    m.x132 - m.x178)**2 + (m.x222 - m.x268)**2) + 1 / sqrt((m.x42 - m.x89)**2
    + (m.x132 - m.x179)**2 + (m.x222 - m.x269)**2) + 1 / sqrt((m.x42 - m.x90)
    **2 + (m.x132 - m.x180)**2 + (m.x222 - m.x270)**2) + 1 / sqrt((m.x43 -
    m.x44)**2 + (m.x133 - m.x134)**2 + (m.x223 - m.x224)**2) + 1 / sqrt((m.x43
    - m.x45)**2 + (m.x133 - m.x135)**2 + (m.x223 - m.x225)**2) + 1 / sqrt((
    m.x43 - m.x46)**2 + (m.x133 - m.x136)**2 + (m.x223 - m.x226)**2) + 1 /
    sqrt((m.x43 - m.x47)**2 + (m.x133 - m.x137)**2 + (m.x223 - m.x227)**2) + 1
    / sqrt((m.x43 - m.x48)**2 + (m.x133 - m.x138)**2 + (m.x223 - m.x228)**2)
    + 1 / sqrt((m.x43 - m.x49)**2 + (m.x133 - m.x139)**2 + (m.x223 - m.x229)**
    2) + 1 / sqrt((m.x43 - m.x50)**2 + (m.x133 - m.x140)**2 + (m.x223 - m.x230)
    **2) + 1 / sqrt((m.x43 - m.x51)**2 + (m.x133 - m.x141)**2 + (m.x223 -
    m.x231)**2) + 1 / sqrt((m.x43 - m.x52)**2 + (m.x133 - m.x142)**2 + (m.x223
    - m.x232)**2) + 1 / sqrt((m.x43 - m.x53)**2 + (m.x133 - m.x143)**2 + (
    m.x223 - m.x233)**2) + 1 / sqrt((m.x43 - m.x54)**2 + (m.x133 - m.x144)**2
    + (m.x223 - m.x234)**2) + 1 / sqrt((m.x43 - m.x55)**2 + (m.x133 - m.x145)
    **2 + (m.x223 - m.x235)**2) + 1 / sqrt((m.x43 - m.x56)**2 + (m.x133 -
    m.x146)**2 + (m.x223 - m.x236)**2) + 1 / sqrt((m.x43 - m.x57)**2 + (m.x133
    - m.x147)**2 + (m.x223 - m.x237)**2) + 1 / sqrt((m.x43 - m.x58)**2 + (
    m.x133 - m.x148)**2 + (m.x223 - m.x238)**2) + 1 / sqrt((m.x43 - m.x59)**2
    + (m.x133 - m.x149)**2 + (m.x223 - m.x239)**2) + 1 / sqrt((m.x43 - m.x60)
    **2 + (m.x133 - m.x150)**2 + (m.x223 - m.x240)**2) + 1 / sqrt((m.x43 -
    m.x61)**2 + (m.x133 - m.x151)**2 + (m.x223 - m.x241)**2) + 1 / sqrt((m.x43
    - m.x62)**2 + (m.x133 - m.x152)**2 + (m.x223 - m.x242)**2) + 1 / sqrt((
    m.x43 - m.x63)**2 + (m.x133 - m.x153)**2 + (m.x223 - m.x243)**2) + 1 /
    sqrt((m.x43 - m.x64)**2 + (m.x133 - m.x154)**2 + (m.x223 - m.x244)**2) + 1
    / sqrt((m.x43 - m.x65)**2 + (m.x133 - m.x155)**2 + (m.x223 - m.x245)**2)
    + 1 / sqrt((m.x43 - m.x66)**2 + (m.x133 - m.x156)**2 + (m.x223 - m.x246)**
    2) + 1 / sqrt((m.x43 - m.x67)**2 + (m.x133 - m.x157)**2 + (m.x223 - m.x247)
    **2) + 1 / sqrt((m.x43 - m.x68)**2 + (m.x133 - m.x158)**2 + (m.x223 -
    m.x248)**2) + 1 / sqrt((m.x43 - m.x69)**2 + (m.x133 - m.x159)**2 + (m.x223
    - m.x249)**2) + 1 / sqrt((m.x43 - m.x70)**2 + (m.x133 - m.x160)**2 + (
    m.x223 - m.x250)**2) + 1 / sqrt((m.x43 - m.x71)**2 + (m.x133 - m.x161)**2
    + (m.x223 - m.x251)**2) + 1 / sqrt((m.x43 - m.x72)**2 + (m.x133 - m.x162)
    **2 + (m.x223 - m.x252)**2) + 1 / sqrt((m.x43 - m.x73)**2 + (m.x133 -
    m.x163)**2 + (m.x223 - m.x253)**2) + 1 / sqrt((m.x43 - m.x74)**2 + (m.x133
    - m.x164)**2 + (m.x223 - m.x254)**2) + 1 / sqrt((m.x43 - m.x75)**2 + (
    m.x133 - m.x165)**2 + (m.x223 - m.x255)**2) + 1 / sqrt((m.x43 - m.x76)**2
    + (m.x133 - m.x166)**2 + (m.x223 - m.x256)**2) + 1 / sqrt((m.x43 - m.x77)
    **2 + (m.x133 - m.x167)**2 + (m.x223 - m.x257)**2) + 1 / sqrt((m.x43 -
    m.x78)**2 + (m.x133 - m.x168)**2 + (m.x223 - m.x258)**2) + 1 / sqrt((m.x43
    - m.x79)**2 + (m.x133 - m.x169)**2 + (m.x223 - m.x259)**2) + 1 / sqrt((
    m.x43 - m.x80)**2 + (m.x133 - m.x170)**2 + (m.x223 - m.x260)**2) + 1 /
    sqrt((m.x43 - m.x81)**2 + (m.x133 - m.x171)**2 + (m.x223 - m.x261)**2) + 1
    / sqrt((m.x43 - m.x82)**2 + (m.x133 - m.x172)**2 + (m.x223 - m.x262)**2)
    + 1 / sqrt((m.x43 - m.x83)**2 + (m.x133 - m.x173)**2 + (m.x223 - m.x263)**
    2) + 1 / sqrt((m.x43 - m.x84)**2 + (m.x133 - m.x174)**2 + (m.x223 - m.x264)
    **2) + 1 / sqrt((m.x43 - m.x85)**2 + (m.x133 - m.x175)**2 + (m.x223 -
    m.x265)**2) + 1 / sqrt((m.x43 - m.x86)**2 + (m.x133 - m.x176)**2 + (m.x223
    - m.x266)**2) + 1 / sqrt((m.x43 - m.x87)**2 + (m.x133 - m.x177)**2 + (
    m.x223 - m.x267)**2) + 1 / sqrt((m.x43 - m.x88)**2 + (m.x133 - m.x178)**2
    + (m.x223 - m.x268)**2) + 1 / sqrt((m.x43 - m.x89)**2 + (m.x133 - m.x179)
    **2 + (m.x223 - m.x269)**2) + 1 / sqrt((m.x43 - m.x90)**2 + (m.x133 -
    m.x180)**2 + (m.x223 - m.x270)**2) + 1 / sqrt((m.x44 - m.x45)**2 + (m.x134
    - m.x135)**2 + (m.x224 - m.x225)**2) + 1 / sqrt((m.x44 - m.x46)**2 + (
    m.x134 - m.x136)**2 + (m.x224 - m.x226)**2) + 1 / sqrt((m.x44 - m.x47)**2
    + (m.x134 - m.x137)**2 + (m.x224 - m.x227)**2) + 1 / sqrt((m.x44 - m.x48)
    **2 + (m.x134 - m.x138)**2 + (m.x224 - m.x228)**2) + 1 / sqrt((m.x44 -
    m.x49)**2 + (m.x134 - m.x139)**2 + (m.x224 - m.x229)**2) + 1 / sqrt((m.x44
    - m.x50)**2 + (m.x134 - m.x140)**2 + (m.x224 - m.x230)**2) + 1 / sqrt((
    m.x44 - m.x51)**2 + (m.x134 - m.x141)**2 + (m.x224 - m.x231)**2) + 1 /
    sqrt((m.x44 - m.x52)**2 + (m.x134 - m.x142)**2 + (m.x224 - m.x232)**2) + 1
    / sqrt((m.x44 - m.x53)**2 + (m.x134 - m.x143)**2 + (m.x224 - m.x233)**2)
    + 1 / sqrt((m.x44 - m.x54)**2 + (m.x134 - m.x144)**2 + (m.x224 - m.x234)**
    2) + 1 / sqrt((m.x44 - m.x55)**2 + (m.x134 - m.x145)**2 + (m.x224 - m.x235)
    **2) + 1 / sqrt((m.x44 - m.x56)**2 + (m.x134 - m.x146)**2 + (m.x224 -
    m.x236)**2) + 1 / sqrt((m.x44 - m.x57)**2 + (m.x134 - m.x147)**2 + (m.x224
    - m.x237)**2) + 1 / sqrt((m.x44 - m.x58)**2 + (m.x134 - m.x148)**2 + (
    m.x224 - m.x238)**2) + 1 / sqrt((m.x44 - m.x59)**2 + (m.x134 - m.x149)**2
    + (m.x224 - m.x239)**2) + 1 / sqrt((m.x44 - m.x60)**2 + (m.x134 - m.x150)
    **2 + (m.x224 - m.x240)**2) + 1 / sqrt((m.x44 - m.x61)**2 + (m.x134 -
    m.x151)**2 + (m.x224 - m.x241)**2) + 1 / sqrt((m.x44 - m.x62)**2 + (m.x134
    - m.x152)**2 + (m.x224 - m.x242)**2) + 1 / sqrt((m.x44 - m.x63)**2 + (
    m.x134 - m.x153)**2 + (m.x224 - m.x243)**2) + 1 / sqrt((m.x44 - m.x64)**2
    + (m.x134 - m.x154)**2 + (m.x224 - m.x244)**2) + 1 / sqrt((m.x44 - m.x65)
    **2 + (m.x134 - m.x155)**2 + (m.x224 - m.x245)**2) + 1 / sqrt((m.x44 -
    m.x66)**2 + (m.x134 - m.x156)**2 + (m.x224 - m.x246)**2) + 1 / sqrt((m.x44
    - m.x67)**2 + (m.x134 - m.x157)**2 + (m.x224 - m.x247)**2) + 1 / sqrt((
    m.x44 - m.x68)**2 + (m.x134 - m.x158)**2 + (m.x224 - m.x248)**2) + 1 /
    sqrt((m.x44 - m.x69)**2 + (m.x134 - m.x159)**2 + (m.x224 - m.x249)**2) + 1
    / sqrt((m.x44 - m.x70)**2 + (m.x134 - m.x160)**2 + (m.x224 - m.x250)**2)
    + 1 / sqrt((m.x44 - m.x71)**2 + (m.x134 - m.x161)**2 + (m.x224 - m.x251)**
    2) + 1 / sqrt((m.x44 - m.x72)**2 + (m.x134 - m.x162)**2 + (m.x224 - m.x252)
    **2) + 1 / sqrt((m.x44 - m.x73)**2 + (m.x134 - m.x163)**2 + (m.x224 -
    m.x253)**2) + 1 / sqrt((m.x44 - m.x74)**2 + (m.x134 - m.x164)**2 + (m.x224
    - m.x254)**2) + 1 / sqrt((m.x44 - m.x75)**2 + (m.x134 - m.x165)**2 + (
    m.x224 - m.x255)**2) + 1 / sqrt((m.x44 - m.x76)**2 + (m.x134 - m.x166)**2
    + (m.x224 - m.x256)**2) + 1 / sqrt((m.x44 - m.x77)**2 + (m.x134 - m.x167)
    **2 + (m.x224 - m.x257)**2) + 1 / sqrt((m.x44 - m.x78)**2 + (m.x134 -
    m.x168)**2 + (m.x224 - m.x258)**2) + 1 / sqrt((m.x44 - m.x79)**2 + (m.x134
    - m.x169)**2 + (m.x224 - m.x259)**2) + 1 / sqrt((m.x44 - m.x80)**2 + (
    m.x134 - m.x170)**2 + (m.x224 - m.x260)**2) + 1 / sqrt((m.x44 - m.x81)**2
    + (m.x134 - m.x171)**2 + (m.x224 - m.x261)**2) + 1 / sqrt((m.x44 - m.x82)
    **2 + (m.x134 - m.x172)**2 + (m.x224 - m.x262)**2) + 1 / sqrt((m.x44 -
    m.x83)**2 + (m.x134 - m.x173)**2 + (m.x224 - m.x263)**2) + 1 / sqrt((m.x44
    - m.x84)**2 + (m.x134 - m.x174)**2 + (m.x224 - m.x264)**2) + 1 / sqrt((
    m.x44 - m.x85)**2 + (m.x134 - m.x175)**2 + (m.x224 - m.x265)**2) + 1 /
    sqrt((m.x44 - m.x86)**2 + (m.x134 - m.x176)**2 + (m.x224 - m.x266)**2) + 1
    / sqrt((m.x44 - m.x87)**2 + (m.x134 - m.x177)**2 + (m.x224 - m.x267)**2)
    + 1 / sqrt((m.x44 - m.x88)**2 + (m.x134 - m.x178)**2 + (m.x224 - m.x268)**
    2) + 1 / sqrt((m.x44 - m.x89)**2 + (m.x134 - m.x179)**2 + (m.x224 - m.x269)
    **2) + 1 / sqrt((m.x44 - m.x90)**2 + (m.x134 - m.x180)**2 + (m.x224 -
    m.x270)**2) + 1 / sqrt((m.x45 - m.x46)**2 + (m.x135 - m.x136)**2 + (m.x225
    - m.x226)**2) + 1 / sqrt((m.x45 - m.x47)**2 + (m.x135 - m.x137)**2 + (
    m.x225 - m.x227)**2) + 1 / sqrt((m.x45 - m.x48)**2 + (m.x135 - m.x138)**2
    + (m.x225 - m.x228)**2) + 1 / sqrt((m.x45 - m.x49)**2 + (m.x135 - m.x139)
    **2 + (m.x225 - m.x229)**2) + 1 / sqrt((m.x45 - m.x50)**2 + (m.x135 -
    m.x140)**2 + (m.x225 - m.x230)**2) + 1 / sqrt((m.x45 - m.x51)**2 + (m.x135
    - m.x141)**2 + (m.x225 - m.x231)**2) + 1 / sqrt((m.x45 - m.x52)**2 + (
    m.x135 - m.x142)**2 + (m.x225 - m.x232)**2) + 1 / sqrt((m.x45 - m.x53)**2
    + (m.x135 - m.x143)**2 + (m.x225 - m.x233)**2) + 1 / sqrt((m.x45 - m.x54)
    **2 + (m.x135 - m.x144)**2 + (m.x225 - m.x234)**2) + 1 / sqrt((m.x45 -
    m.x55)**2 + (m.x135 - m.x145)**2 + (m.x225 - m.x235)**2) + 1 / sqrt((m.x45
    - m.x56)**2 + (m.x135 - m.x146)**2 + (m.x225 - m.x236)**2) + 1 / sqrt((
    m.x45 - m.x57)**2 + (m.x135 - m.x147)**2 + (m.x225 - m.x237)**2) + 1 /
    sqrt((m.x45 - m.x58)**2 + (m.x135 - m.x148)**2 + (m.x225 - m.x238)**2) + 1
    / sqrt((m.x45 - m.x59)**2 + (m.x135 - m.x149)**2 + (m.x225 - m.x239)**2)
    + 1 / sqrt((m.x45 - m.x60)**2 + (m.x135 - m.x150)**2 + (m.x225 - m.x240)**
    2) + 1 / sqrt((m.x45 - m.x61)**2 + (m.x135 - m.x151)**2 + (m.x225 - m.x241)
    **2) + 1 / sqrt((m.x45 - m.x62)**2 + (m.x135 - m.x152)**2 + (m.x225 -
    m.x242)**2) + 1 / sqrt((m.x45 - m.x63)**2 + (m.x135 - m.x153)**2 + (m.x225
    - m.x243)**2) + 1 / sqrt((m.x45 - m.x64)**2 + (m.x135 - m.x154)**2 + (
    m.x225 - m.x244)**2) + 1 / sqrt((m.x45 - m.x65)**2 + (m.x135 - m.x155)**2
    + (m.x225 - m.x245)**2) + 1 / sqrt((m.x45 - m.x66)**2 + (m.x135 - m.x156)
    **2 + (m.x225 - m.x246)**2) + 1 / sqrt((m.x45 - m.x67)**2 + (m.x135 -
    m.x157)**2 + (m.x225 - m.x247)**2) + 1 / sqrt((m.x45 - m.x68)**2 + (m.x135
    - m.x158)**2 + (m.x225 - m.x248)**2) + 1 / sqrt((m.x45 - m.x69)**2 + (
    m.x135 - m.x159)**2 + (m.x225 - m.x249)**2) + 1 / sqrt((m.x45 - m.x70)**2
    + (m.x135 - m.x160)**2 + (m.x225 - m.x250)**2) + 1 / sqrt((m.x45 - m.x71)
    **2 + (m.x135 - m.x161)**2 + (m.x225 - m.x251)**2) + 1 / sqrt((m.x45 -
    m.x72)**2 + (m.x135 - m.x162)**2 + (m.x225 - m.x252)**2) + 1 / sqrt((m.x45
    - m.x73)**2 + (m.x135 - m.x163)**2 + (m.x225 - m.x253)**2) + 1 / sqrt((
    m.x45 - m.x74)**2 + (m.x135 - m.x164)**2 + (m.x225 - m.x254)**2) + 1 /
    sqrt((m.x45 - m.x75)**2 + (m.x135 - m.x165)**2 + (m.x225 - m.x255)**2) + 1
    / sqrt((m.x45 - m.x76)**2 + (m.x135 - m.x166)**2 + (m.x225 - m.x256)**2)
    + 1 / sqrt((m.x45 - m.x77)**2 + (m.x135 - m.x167)**2 + (m.x225 - m.x257)**
    2) + 1 / sqrt((m.x45 - m.x78)**2 + (m.x135 - m.x168)**2 + (m.x225 - m.x258)
    **2) + 1 / sqrt((m.x45 - m.x79)**2 + (m.x135 - m.x169)**2 + (m.x225 -
    m.x259)**2) + 1 / sqrt((m.x45 - m.x80)**2 + (m.x135 - m.x170)**2 + (m.x225
    - m.x260)**2) + 1 / sqrt((m.x45 - m.x81)**2 + (m.x135 - m.x171)**2 + (
    m.x225 - m.x261)**2) + 1 / sqrt((m.x45 - m.x82)**2 + (m.x135 - m.x172)**2
    + (m.x225 - m.x262)**2) + 1 / sqrt((m.x45 - m.x83)**2 + (m.x135 - m.x173)
    **2 + (m.x225 - m.x263)**2) + 1 / sqrt((m.x45 - m.x84)**2 + (m.x135 -
    m.x174)**2 + (m.x225 - m.x264)**2) + 1 / sqrt((m.x45 - m.x85)**2 + (m.x135
    - m.x175)**2 + (m.x225 - m.x265)**2) + 1 / sqrt((m.x45 - m.x86)**2 + (
    m.x135 - m.x176)**2 + (m.x225 - m.x266)**2) + 1 / sqrt((m.x45 - m.x87)**2
    + (m.x135 - m.x177)**2 + (m.x225 - m.x267)**2) + 1 / sqrt((m.x45 - m.x88)
    **2 + (m.x135 - m.x178)**2 + (m.x225 - m.x268)**2) + 1 / sqrt((m.x45 -
    m.x89)**2 + (m.x135 - m.x179)**2 + (m.x225 - m.x269)**2) + 1 / sqrt((m.x45
    - m.x90)**2 + (m.x135 - m.x180)**2 + (m.x225 - m.x270)**2) + 1 / sqrt((
    m.x46 - m.x47)**2 + (m.x136 - m.x137)**2 + (m.x226 - m.x227)**2) + 1 /
    sqrt((m.x46 - m.x48)**2 + (m.x136 - m.x138)**2 + (m.x226 - m.x228)**2) + 1
    / sqrt((m.x46 - m.x49)**2 + (m.x136 - m.x139)**2 + (m.x226 - m.x229)**2)
    + 1 / sqrt((m.x46 - m.x50)**2 + (m.x136 - m.x140)**2 + (m.x226 - m.x230)**
    2) + 1 / sqrt((m.x46 - m.x51)**2 + (m.x136 - m.x141)**2 + (m.x226 - m.x231)
    **2) + 1 / sqrt((m.x46 - m.x52)**2 + (m.x136 - m.x142)**2 + (m.x226 -
    m.x232)**2) + 1 / sqrt((m.x46 - m.x53)**2 + (m.x136 - m.x143)**2 + (m.x226
    - m.x233)**2) + 1 / sqrt((m.x46 - m.x54)**2 + (m.x136 - m.x144)**2 + (
    m.x226 - m.x234)**2) + 1 / sqrt((m.x46 - m.x55)**2 + (m.x136 - m.x145)**2
    + (m.x226 - m.x235)**2) + 1 / sqrt((m.x46 - m.x56)**2 + (m.x136 - m.x146)
    **2 + (m.x226 - m.x236)**2) + 1 / sqrt((m.x46 - m.x57)**2 + (m.x136 -
    m.x147)**2 + (m.x226 - m.x237)**2) + 1 / sqrt((m.x46 - m.x58)**2 + (m.x136
    - m.x148)**2 + (m.x226 - m.x238)**2) + 1 / sqrt((m.x46 - m.x59)**2 + (
    m.x136 - m.x149)**2 + (m.x226 - m.x239)**2) + 1 / sqrt((m.x46 - m.x60)**2
    + (m.x136 - m.x150)**2 + (m.x226 - m.x240)**2) + 1 / sqrt((m.x46 - m.x61)
    **2 + (m.x136 - m.x151)**2 + (m.x226 - m.x241)**2) + 1 / sqrt((m.x46 -
    m.x62)**2 + (m.x136 - m.x152)**2 + (m.x226 - m.x242)**2) + 1 / sqrt((m.x46
    - m.x63)**2 + (m.x136 - m.x153)**2 + (m.x226 - m.x243)**2) + 1 / sqrt((
    m.x46 - m.x64)**2 + (m.x136 - m.x154)**2 + (m.x226 - m.x244)**2) + 1 /
    sqrt((m.x46 - m.x65)**2 + (m.x136 - m.x155)**2 + (m.x226 - m.x245)**2) + 1
    / sqrt((m.x46 - m.x66)**2 + (m.x136 - m.x156)**2 + (m.x226 - m.x246)**2)
    + 1 / sqrt((m.x46 - m.x67)**2 + (m.x136 - m.x157)**2 + (m.x226 - m.x247)**
    2) + 1 / sqrt((m.x46 - m.x68)**2 + (m.x136 - m.x158)**2 + (m.x226 - m.x248)
    **2) + 1 / sqrt((m.x46 - m.x69)**2 + (m.x136 - m.x159)**2 + (m.x226 -
    m.x249)**2) + 1 / sqrt((m.x46 - m.x70)**2 + (m.x136 - m.x160)**2 + (m.x226
    - m.x250)**2) + 1 / sqrt((m.x46 - m.x71)**2 + (m.x136 - m.x161)**2 + (
    m.x226 - m.x251)**2) + 1 / sqrt((m.x46 - m.x72)**2 + (m.x136 - m.x162)**2
    + (m.x226 - m.x252)**2) + 1 / sqrt((m.x46 - m.x73)**2 + (m.x136 - m.x163)
    **2 + (m.x226 - m.x253)**2) + 1 / sqrt((m.x46 - m.x74)**2 + (m.x136 -
    m.x164)**2 + (m.x226 - m.x254)**2) + 1 / sqrt((m.x46 - m.x75)**2 + (m.x136
    - m.x165)**2 + (m.x226 - m.x255)**2) + 1 / sqrt((m.x46 - m.x76)**2 + (
    m.x136 - m.x166)**2 + (m.x226 - m.x256)**2) + 1 / sqrt((m.x46 - m.x77)**2
    + (m.x136 - m.x167)**2 + (m.x226 - m.x257)**2) + 1 / sqrt((m.x46 - m.x78)
    **2 + (m.x136 - m.x168)**2 + (m.x226 - m.x258)**2) + 1 / sqrt((m.x46 -
    m.x79)**2 + (m.x136 - m.x169)**2 + (m.x226 - m.x259)**2) + 1 / sqrt((m.x46
    - m.x80)**2 + (m.x136 - m.x170)**2 + (m.x226 - m.x260)**2) + 1 / sqrt((
    m.x46 - m.x81)**2 + (m.x136 - m.x171)**2 + (m.x226 - m.x261)**2) + 1 /
    sqrt((m.x46 - m.x82)**2 + (m.x136 - m.x172)**2 + (m.x226 - m.x262)**2) + 1
    / sqrt((m.x46 - m.x83)**2 + (m.x136 - m.x173)**2 + (m.x226 - m.x263)**2)
    + 1 / sqrt((m.x46 - m.x84)**2 + (m.x136 - m.x174)**2 + (m.x226 - m.x264)**
    2) + 1 / sqrt((m.x46 - m.x85)**2 + (m.x136 - m.x175)**2 + (m.x226 - m.x265)
    **2) + 1 / sqrt((m.x46 - m.x86)**2 + (m.x136 - m.x176)**2 + (m.x226 -
    m.x266)**2) + 1 / sqrt((m.x46 - m.x87)**2 + (m.x136 - m.x177)**2 + (m.x226
    - m.x267)**2) + 1 / sqrt((m.x46 - m.x88)**2 + (m.x136 - m.x178)**2 + (
    m.x226 - m.x268)**2) + 1 / sqrt((m.x46 - m.x89)**2 + (m.x136 - m.x179)**2
    + (m.x226 - m.x269)**2) + 1 / sqrt((m.x46 - m.x90)**2 + (m.x136 - m.x180)
    **2 + (m.x226 - m.x270)**2) + 1 / sqrt((m.x47 - m.x48)**2 + (m.x137 -
    m.x138)**2 + (m.x227 - m.x228)**2) + 1 / sqrt((m.x47 - m.x49)**2 + (m.x137
    - m.x139)**2 + (m.x227 - m.x229)**2) + 1 / sqrt((m.x47 - m.x50)**2 + (
    m.x137 - m.x140)**2 + (m.x227 - m.x230)**2) + 1 / sqrt((m.x47 - m.x51)**2
    + (m.x137 - m.x141)**2 + (m.x227 - m.x231)**2) + 1 / sqrt((m.x47 - m.x52)
    **2 + (m.x137 - m.x142)**2 + (m.x227 - m.x232)**2) + 1 / sqrt((m.x47 -
    m.x53)**2 + (m.x137 - m.x143)**2 + (m.x227 - m.x233)**2) + 1 / sqrt((m.x47
    - m.x54)**2 + (m.x137 - m.x144)**2 + (m.x227 - m.x234)**2) + 1 / sqrt((
    m.x47 - m.x55)**2 + (m.x137 - m.x145)**2 + (m.x227 - m.x235)**2) + 1 /
    sqrt((m.x47 - m.x56)**2 + (m.x137 - m.x146)**2 + (m.x227 - m.x236)**2) + 1
    / sqrt((m.x47 - m.x57)**2 + (m.x137 - m.x147)**2 + (m.x227 - m.x237)**2)
    + 1 / sqrt((m.x47 - m.x58)**2 + (m.x137 - m.x148)**2 + (m.x227 - m.x238)**
    2) + 1 / sqrt((m.x47 - m.x59)**2 + (m.x137 - m.x149)**2 + (m.x227 - m.x239)
    **2) + 1 / sqrt((m.x47 - m.x60)**2 + (m.x137 - m.x150)**2 + (m.x227 -
    m.x240)**2) + 1 / sqrt((m.x47 - m.x61)**2 + (m.x137 - m.x151)**2 + (m.x227
    - m.x241)**2) + 1 / sqrt((m.x47 - m.x62)**2 + (m.x137 - m.x152)**2 + (
    m.x227 - m.x242)**2) + 1 / sqrt((m.x47 - m.x63)**2 + (m.x137 - m.x153)**2
    + (m.x227 - m.x243)**2) + 1 / sqrt((m.x47 - m.x64)**2 + (m.x137 - m.x154)
    **2 + (m.x227 - m.x244)**2) + 1 / sqrt((m.x47 - m.x65)**2 + (m.x137 -
    m.x155)**2 + (m.x227 - m.x245)**2) + 1 / sqrt((m.x47 - m.x66)**2 + (m.x137
    - m.x156)**2 + (m.x227 - m.x246)**2) + 1 / sqrt((m.x47 - m.x67)**2 + (
    m.x137 - m.x157)**2 + (m.x227 - m.x247)**2) + 1 / sqrt((m.x47 - m.x68)**2
    + (m.x137 - m.x158)**2 + (m.x227 - m.x248)**2) + 1 / sqrt((m.x47 - m.x69)
    **2 + (m.x137 - m.x159)**2 + (m.x227 - m.x249)**2) + 1 / sqrt((m.x47 -
    m.x70)**2 + (m.x137 - m.x160)**2 + (m.x227 - m.x250)**2) + 1 / sqrt((m.x47
    - m.x71)**2 + (m.x137 - m.x161)**2 + (m.x227 - m.x251)**2) + 1 / sqrt((
    m.x47 - m.x72)**2 + (m.x137 - m.x162)**2 + (m.x227 - m.x252)**2) + 1 /
    sqrt((m.x47 - m.x73)**2 + (m.x137 - m.x163)**2 + (m.x227 - m.x253)**2) + 1
    / sqrt((m.x47 - m.x74)**2 + (m.x137 - m.x164)**2 + (m.x227 - m.x254)**2)
    + 1 / sqrt((m.x47 - m.x75)**2 + (m.x137 - m.x165)**2 + (m.x227 - m.x255)**
    2) + 1 / sqrt((m.x47 - m.x76)**2 + (m.x137 - m.x166)**2 + (m.x227 - m.x256)
    **2) + 1 / sqrt((m.x47 - m.x77)**2 + (m.x137 - m.x167)**2 + (m.x227 -
    m.x257)**2) + 1 / sqrt((m.x47 - m.x78)**2 + (m.x137 - m.x168)**2 + (m.x227
    - m.x258)**2) + 1 / sqrt((m.x47 - m.x79)**2 + (m.x137 - m.x169)**2 + (
    m.x227 - m.x259)**2) + 1 / sqrt((m.x47 - m.x80)**2 + (m.x137 - m.x170)**2
    + (m.x227 - m.x260)**2) + 1 / sqrt((m.x47 - m.x81)**2 + (m.x137 - m.x171)
    **2 + (m.x227 - m.x261)**2) + 1 / sqrt((m.x47 - m.x82)**2 + (m.x137 -
    m.x172)**2 + (m.x227 - m.x262)**2) + 1 / sqrt((m.x47 - m.x83)**2 + (m.x137
    - m.x173)**2 + (m.x227 - m.x263)**2) + 1 / sqrt((m.x47 - m.x84)**2 + (
    m.x137 - m.x174)**2 + (m.x227 - m.x264)**2) + 1 / sqrt((m.x47 - m.x85)**2
    + (m.x137 - m.x175)**2 + (m.x227 - m.x265)**2) + 1 / sqrt((m.x47 - m.x86)
    **2 + (m.x137 - m.x176)**2 + (m.x227 - m.x266)**2) + 1 / sqrt((m.x47 -
    m.x87)**2 + (m.x137 - m.x177)**2 + (m.x227 - m.x267)**2) + 1 / sqrt((m.x47
    - m.x88)**2 + (m.x137 - m.x178)**2 + (m.x227 - m.x268)**2) + 1 / sqrt((
    m.x47 - m.x89)**2 + (m.x137 - m.x179)**2 + (m.x227 - m.x269)**2) + 1 /
    sqrt((m.x47 - m.x90)**2 + (m.x137 - m.x180)**2 + (m.x227 - m.x270)**2) + 1
    / sqrt((m.x48 - m.x49)**2 + (m.x138 - m.x139)**2 + (m.x228 - m.x229)**2)
    + 1 / sqrt((m.x48 - m.x50)**2 + (m.x138 - m.x140)**2 + (m.x228 - m.x230)**
    2) + 1 / sqrt((m.x48 - m.x51)**2 + (m.x138 - m.x141)**2 + (m.x228 - m.x231)
    **2) + 1 / sqrt((m.x48 - m.x52)**2 + (m.x138 - m.x142)**2 + (m.x228 -
    m.x232)**2) + 1 / sqrt((m.x48 - m.x53)**2 + (m.x138 - m.x143)**2 + (m.x228
    - m.x233)**2) + 1 / sqrt((m.x48 - m.x54)**2 + (m.x138 - m.x144)**2 + (
    m.x228 - m.x234)**2) + 1 / sqrt((m.x48 - m.x55)**2 + (m.x138 - m.x145)**2
    + (m.x228 - m.x235)**2) + 1 / sqrt((m.x48 - m.x56)**2 + (m.x138 - m.x146)
    **2 + (m.x228 - m.x236)**2) + 1 / sqrt((m.x48 - m.x57)**2 + (m.x138 -
    m.x147)**2 + (m.x228 - m.x237)**2) + 1 / sqrt((m.x48 - m.x58)**2 + (m.x138
    - m.x148)**2 + (m.x228 - m.x238)**2) + 1 / sqrt((m.x48 - m.x59)**2 + (
    m.x138 - m.x149)**2 + (m.x228 - m.x239)**2) + 1 / sqrt((m.x48 - m.x60)**2
    + (m.x138 - m.x150)**2 + (m.x228 - m.x240)**2) + 1 / sqrt((m.x48 - m.x61)
    **2 + (m.x138 - m.x151)**2 + (m.x228 - m.x241)**2) + 1 / sqrt((m.x48 -
    m.x62)**2 + (m.x138 - m.x152)**2 + (m.x228 - m.x242)**2) + 1 / sqrt((m.x48
    - m.x63)**2 + (m.x138 - m.x153)**2 + (m.x228 - m.x243)**2) + 1 / sqrt((
    m.x48 - m.x64)**2 + (m.x138 - m.x154)**2 + (m.x228 - m.x244)**2) + 1 /
    sqrt((m.x48 - m.x65)**2 + (m.x138 - m.x155)**2 + (m.x228 - m.x245)**2) + 1
    / sqrt((m.x48 - m.x66)**2 + (m.x138 - m.x156)**2 + (m.x228 - m.x246)**2)
    + 1 / sqrt((m.x48 - m.x67)**2 + (m.x138 - m.x157)**2 + (m.x228 - m.x247)**
    2) + 1 / sqrt((m.x48 - m.x68)**2 + (m.x138 - m.x158)**2 + (m.x228 - m.x248)
    **2) + 1 / sqrt((m.x48 - m.x69)**2 + (m.x138 - m.x159)**2 + (m.x228 -
    m.x249)**2) + 1 / sqrt((m.x48 - m.x70)**2 + (m.x138 - m.x160)**2 + (m.x228
    - m.x250)**2) + 1 / sqrt((m.x48 - m.x71)**2 + (m.x138 - m.x161)**2 + (
    m.x228 - m.x251)**2) + 1 / sqrt((m.x48 - m.x72)**2 + (m.x138 - m.x162)**2
    + (m.x228 - m.x252)**2) + 1 / sqrt((m.x48 - m.x73)**2 + (m.x138 - m.x163)
    **2 + (m.x228 - m.x253)**2) + 1 / sqrt((m.x48 - m.x74)**2 + (m.x138 -
    m.x164)**2 + (m.x228 - m.x254)**2) + 1 / sqrt((m.x48 - m.x75)**2 + (m.x138
    - m.x165)**2 + (m.x228 - m.x255)**2) + 1 / sqrt((m.x48 - m.x76)**2 + (
    m.x138 - m.x166)**2 + (m.x228 - m.x256)**2) + 1 / sqrt((m.x48 - m.x77)**2
    + (m.x138 - m.x167)**2 + (m.x228 - m.x257)**2) + 1 / sqrt((m.x48 - m.x78)
    **2 + (m.x138 - m.x168)**2 + (m.x228 - m.x258)**2) + 1 / sqrt((m.x48 -
    m.x79)**2 + (m.x138 - m.x169)**2 + (m.x228 - m.x259)**2) + 1 / sqrt((m.x48
    - m.x80)**2 + (m.x138 - m.x170)**2 + (m.x228 - m.x260)**2) + 1 / sqrt((
    m.x48 - m.x81)**2 + (m.x138 - m.x171)**2 + (m.x228 - m.x261)**2) + 1 /
    sqrt((m.x48 - m.x82)**2 + (m.x138 - m.x172)**2 + (m.x228 - m.x262)**2) + 1
    / sqrt((m.x48 - m.x83)**2 + (m.x138 - m.x173)**2 + (m.x228 - m.x263)**2)
    + 1 / sqrt((m.x48 - m.x84)**2 + (m.x138 - m.x174)**2 + (m.x228 - m.x264)**
    2) + 1 / sqrt((m.x48 - m.x85)**2 + (m.x138 - m.x175)**2 + (m.x228 - m.x265)
    **2) + 1 / sqrt((m.x48 - m.x86)**2 + (m.x138 - m.x176)**2 + (m.x228 -
    m.x266)**2) + 1 / sqrt((m.x48 - m.x87)**2 + (m.x138 - m.x177)**2 + (m.x228
    - m.x267)**2) + 1 / sqrt((m.x48 - m.x88)**2 + (m.x138 - m.x178)**2 + (
    m.x228 - m.x268)**2) + 1 / sqrt((m.x48 - m.x89)**2 + (m.x138 - m.x179)**2
    + (m.x228 - m.x269)**2) + 1 / sqrt((m.x48 - m.x90)**2 + (m.x138 - m.x180)
    **2 + (m.x228 - m.x270)**2) + 1 / sqrt((m.x49 - m.x50)**2 + (m.x139 -
    m.x140)**2 + (m.x229 - m.x230)**2) + 1 / sqrt((m.x49 - m.x51)**2 + (m.x139
    - m.x141)**2 + (m.x229 - m.x231)**2) + 1 / sqrt((m.x49 - m.x52)**2 + (
    m.x139 - m.x142)**2 + (m.x229 - m.x232)**2) + 1 / sqrt((m.x49 - m.x53)**2
    + (m.x139 - m.x143)**2 + (m.x229 - m.x233)**2) + 1 / sqrt((m.x49 - m.x54)
    **2 + (m.x139 - m.x144)**2 + (m.x229 - m.x234)**2) + 1 / sqrt((m.x49 -
    m.x55)**2 + (m.x139 - m.x145)**2 + (m.x229 - m.x235)**2) + 1 / sqrt((m.x49
    - m.x56)**2 + (m.x139 - m.x146)**2 + (m.x229 - m.x236)**2) + 1 / sqrt((
    m.x49 - m.x57)**2 + (m.x139 - m.x147)**2 + (m.x229 - m.x237)**2) + 1 /
    sqrt((m.x49 - m.x58)**2 + (m.x139 - m.x148)**2 + (m.x229 - m.x238)**2) + 1
    / sqrt((m.x49 - m.x59)**2 + (m.x139 - m.x149)**2 + (m.x229 - m.x239)**2)
    + 1 / sqrt((m.x49 - m.x60)**2 + (m.x139 - m.x150)**2 + (m.x229 - m.x240)**
    2) + 1 / sqrt((m.x49 - m.x61)**2 + (m.x139 - m.x151)**2 + (m.x229 - m.x241)
    **2) + 1 / sqrt((m.x49 - m.x62)**2 + (m.x139 - m.x152)**2 + (m.x229 -
    m.x242)**2) + 1 / sqrt((m.x49 - m.x63)**2 + (m.x139 - m.x153)**2 + (m.x229
    - m.x243)**2) + 1 / sqrt((m.x49 - m.x64)**2 + (m.x139 - m.x154)**2 + (
    m.x229 - m.x244)**2) + 1 / sqrt((m.x49 - m.x65)**2 + (m.x139 - m.x155)**2
    + (m.x229 - m.x245)**2) + 1 / sqrt((m.x49 - m.x66)**2 + (m.x139 - m.x156)
    **2 + (m.x229 - m.x246)**2) + 1 / sqrt((m.x49 - m.x67)**2 + (m.x139 -
    m.x157)**2 + (m.x229 - m.x247)**2) + 1 / sqrt((m.x49 - m.x68)**2 + (m.x139
    - m.x158)**2 + (m.x229 - m.x248)**2) + 1 / sqrt((m.x49 - m.x69)**2 + (
    m.x139 - m.x159)**2 + (m.x229 - m.x249)**2) + 1 / sqrt((m.x49 - m.x70)**2
    + (m.x139 - m.x160)**2 + (m.x229 - m.x250)**2) + 1 / sqrt((m.x49 - m.x71)
    **2 + (m.x139 - m.x161)**2 + (m.x229 - m.x251)**2) + 1 / sqrt((m.x49 -
    m.x72)**2 + (m.x139 - m.x162)**2 + (m.x229 - m.x252)**2) + 1 / sqrt((m.x49
    - m.x73)**2 + (m.x139 - m.x163)**2 + (m.x229 - m.x253)**2) + 1 / sqrt((
    m.x49 - m.x74)**2 + (m.x139 - m.x164)**2 + (m.x229 - m.x254)**2) + 1 /
    sqrt((m.x49 - m.x75)**2 + (m.x139 - m.x165)**2 + (m.x229 - m.x255)**2) + 1
    / sqrt((m.x49 - m.x76)**2 + (m.x139 - m.x166)**2 + (m.x229 - m.x256)**2)
    + 1 / sqrt((m.x49 - m.x77)**2 + (m.x139 - m.x167)**2 + (m.x229 - m.x257)**
    2) + 1 / sqrt((m.x49 - m.x78)**2 + (m.x139 - m.x168)**2 + (m.x229 - m.x258)
    **2) + 1 / sqrt((m.x49 - m.x79)**2 + (m.x139 - m.x169)**2 + (m.x229 -
    m.x259)**2) + 1 / sqrt((m.x49 - m.x80)**2 + (m.x139 - m.x170)**2 + (m.x229
    - m.x260)**2) + 1 / sqrt((m.x49 - m.x81)**2 + (m.x139 - m.x171)**2 + (
    m.x229 - m.x261)**2) + 1 / sqrt((m.x49 - m.x82)**2 + (m.x139 - m.x172)**2
    + (m.x229 - m.x262)**2) + 1 / sqrt((m.x49 - m.x83)**2 + (m.x139 - m.x173)
    **2 + (m.x229 - m.x263)**2) + 1 / sqrt((m.x49 - m.x84)**2 + (m.x139 -
    m.x174)**2 + (m.x229 - m.x264)**2) + 1 / sqrt((m.x49 - m.x85)**2 + (m.x139
    - m.x175)**2 + (m.x229 - m.x265)**2) + 1 / sqrt((m.x49 - m.x86)**2 + (
    m.x139 - m.x176)**2 + (m.x229 - m.x266)**2) + 1 / sqrt((m.x49 - m.x87)**2
    + (m.x139 - m.x177)**2 + (m.x229 - m.x267)**2) + 1 / sqrt((m.x49 - m.x88)
    **2 + (m.x139 - m.x178)**2 + (m.x229 - m.x268)**2) + 1 / sqrt((m.x49 -
    m.x89)**2 + (m.x139 - m.x179)**2 + (m.x229 - m.x269)**2) + 1 / sqrt((m.x49
    - m.x90)**2 + (m.x139 - m.x180)**2 + (m.x229 - m.x270)**2) + 1 / sqrt((
    m.x50 - m.x51)**2 + (m.x140 - m.x141)**2 + (m.x230 - m.x231)**2) + 1 /
    sqrt((m.x50 - m.x52)**2 + (m.x140 - m.x142)**2 + (m.x230 - m.x232)**2) + 1
    / sqrt((m.x50 - m.x53)**2 + (m.x140 - m.x143)**2 + (m.x230 - m.x233)**2)
    + 1 / sqrt((m.x50 - m.x54)**2 + (m.x140 - m.x144)**2 + (m.x230 - m.x234)**
    2) + 1 / sqrt((m.x50 - m.x55)**2 + (m.x140 - m.x145)**2 + (m.x230 - m.x235)
    **2) + 1 / sqrt((m.x50 - m.x56)**2 + (m.x140 - m.x146)**2 + (m.x230 -
    m.x236)**2) + 1 / sqrt((m.x50 - m.x57)**2 + (m.x140 - m.x147)**2 + (m.x230
    - m.x237)**2) + 1 / sqrt((m.x50 - m.x58)**2 + (m.x140 - m.x148)**2 + (
    m.x230 - m.x238)**2) + 1 / sqrt((m.x50 - m.x59)**2 + (m.x140 - m.x149)**2
    + (m.x230 - m.x239)**2) + 1 / sqrt((m.x50 - m.x60)**2 + (m.x140 - m.x150)
    **2 + (m.x230 - m.x240)**2) + 1 / sqrt((m.x50 - m.x61)**2 + (m.x140 -
    m.x151)**2 + (m.x230 - m.x241)**2) + 1 / sqrt((m.x50 - m.x62)**2 + (m.x140
    - m.x152)**2 + (m.x230 - m.x242)**2) + 1 / sqrt((m.x50 - m.x63)**2 + (
    m.x140 - m.x153)**2 + (m.x230 - m.x243)**2) + 1 / sqrt((m.x50 - m.x64)**2
    + (m.x140 - m.x154)**2 + (m.x230 - m.x244)**2) + 1 / sqrt((m.x50 - m.x65)
    **2 + (m.x140 - m.x155)**2 + (m.x230 - m.x245)**2) + 1 / sqrt((m.x50 -
    m.x66)**2 + (m.x140 - m.x156)**2 + (m.x230 - m.x246)**2) + 1 / sqrt((m.x50
    - m.x67)**2 + (m.x140 - m.x157)**2 + (m.x230 - m.x247)**2) + 1 / sqrt((
    m.x50 - m.x68)**2 + (m.x140 - m.x158)**2 + (m.x230 - m.x248)**2) + 1 /
    sqrt((m.x50 - m.x69)**2 + (m.x140 - m.x159)**2 + (m.x230 - m.x249)**2) + 1
    / sqrt((m.x50 - m.x70)**2 + (m.x140 - m.x160)**2 + (m.x230 - m.x250)**2)
    + 1 / sqrt((m.x50 - m.x71)**2 + (m.x140 - m.x161)**2 + (m.x230 - m.x251)**
    2) + 1 / sqrt((m.x50 - m.x72)**2 + (m.x140 - m.x162)**2 + (m.x230 - m.x252)
    **2) + 1 / sqrt((m.x50 - m.x73)**2 + (m.x140 - m.x163)**2 + (m.x230 -
    m.x253)**2) + 1 / sqrt((m.x50 - m.x74)**2 + (m.x140 - m.x164)**2 + (m.x230
    - m.x254)**2) + 1 / sqrt((m.x50 - m.x75)**2 + (m.x140 - m.x165)**2 + (
    m.x230 - m.x255)**2) + 1 / sqrt((m.x50 - m.x76)**2 + (m.x140 - m.x166)**2
    + (m.x230 - m.x256)**2) + 1 / sqrt((m.x50 - m.x77)**2 + (m.x140 - m.x167)
    **2 + (m.x230 - m.x257)**2) + 1 / sqrt((m.x50 - m.x78)**2 + (m.x140 -
    m.x168)**2 + (m.x230 - m.x258)**2) + 1 / sqrt((m.x50 - m.x79)**2 + (m.x140
    - m.x169)**2 + (m.x230 - m.x259)**2) + 1 / sqrt((m.x50 - m.x80)**2 + (
    m.x140 - m.x170)**2 + (m.x230 - m.x260)**2) + 1 / sqrt((m.x50 - m.x81)**2
    + (m.x140 - m.x171)**2 + (m.x230 - m.x261)**2) + 1 / sqrt((m.x50 - m.x82)
    **2 + (m.x140 - m.x172)**2 + (m.x230 - m.x262)**2) + 1 / sqrt((m.x50 -
    m.x83)**2 + (m.x140 - m.x173)**2 + (m.x230 - m.x263)**2) + 1 / sqrt((m.x50
    - m.x84)**2 + (m.x140 - m.x174)**2 + (m.x230 - m.x264)**2) + 1 / sqrt((
    m.x50 - m.x85)**2 + (m.x140 - m.x175)**2 + (m.x230 - m.x265)**2) + 1 /
    sqrt((m.x50 - m.x86)**2 + (m.x140 - m.x176)**2 + (m.x230 - m.x266)**2) + 1
    / sqrt((m.x50 - m.x87)**2 + (m.x140 - m.x177)**2 + (m.x230 - m.x267)**2)
    + 1 / sqrt((m.x50 - m.x88)**2 + (m.x140 - m.x178)**2 + (m.x230 - m.x268)**
    2) + 1 / sqrt((m.x50 - m.x89)**2 + (m.x140 - m.x179)**2 + (m.x230 - m.x269)
    **2) + 1 / sqrt((m.x50 - m.x90)**2 + (m.x140 - m.x180)**2 + (m.x230 -
    m.x270)**2) + 1 / sqrt((m.x51 - m.x52)**2 + (m.x141 - m.x142)**2 + (m.x231
    - m.x232)**2) + 1 / sqrt((m.x51 - m.x53)**2 + (m.x141 - m.x143)**2 + (
    m.x231 - m.x233)**2) + 1 / sqrt((m.x51 - m.x54)**2 + (m.x141 - m.x144)**2
    + (m.x231 - m.x234)**2) + 1 / sqrt((m.x51 - m.x55)**2 + (m.x141 - m.x145)
    **2 + (m.x231 - m.x235)**2) + 1 / sqrt((m.x51 - m.x56)**2 + (m.x141 -
    m.x146)**2 + (m.x231 - m.x236)**2) + 1 / sqrt((m.x51 - m.x57)**2 + (m.x141
    - m.x147)**2 + (m.x231 - m.x237)**2) + 1 / sqrt((m.x51 - m.x58)**2 + (
    m.x141 - m.x148)**2 + (m.x231 - m.x238)**2) + 1 / sqrt((m.x51 - m.x59)**2
    + (m.x141 - m.x149)**2 + (m.x231 - m.x239)**2) + 1 / sqrt((m.x51 - m.x60)
    **2 + (m.x141 - m.x150)**2 + (m.x231 - m.x240)**2) + 1 / sqrt((m.x51 -
    m.x61)**2 + (m.x141 - m.x151)**2 + (m.x231 - m.x241)**2) + 1 / sqrt((m.x51
    - m.x62)**2 + (m.x141 - m.x152)**2 + (m.x231 - m.x242)**2) + 1 / sqrt((
    m.x51 - m.x63)**2 + (m.x141 - m.x153)**2 + (m.x231 - m.x243)**2) + 1 /
    sqrt((m.x51 - m.x64)**2 + (m.x141 - m.x154)**2 + (m.x231 - m.x244)**2) + 1
    / sqrt((m.x51 - m.x65)**2 + (m.x141 - m.x155)**2 + (m.x231 - m.x245)**2)
    + 1 / sqrt((m.x51 - m.x66)**2 + (m.x141 - m.x156)**2 + (m.x231 - m.x246)**
    2) + 1 / sqrt((m.x51 - m.x67)**2 + (m.x141 - m.x157)**2 + (m.x231 - m.x247)
    **2) + 1 / sqrt((m.x51 - m.x68)**2 + (m.x141 - m.x158)**2 + (m.x231 -
    m.x248)**2) + 1 / sqrt((m.x51 - m.x69)**2 + (m.x141 - m.x159)**2 + (m.x231
    - m.x249)**2) + 1 / sqrt((m.x51 - m.x70)**2 + (m.x141 - m.x160)**2 + (
    m.x231 - m.x250)**2) + 1 / sqrt((m.x51 - m.x71)**2 + (m.x141 - m.x161)**2
    + (m.x231 - m.x251)**2) + 1 / sqrt((m.x51 - m.x72)**2 + (m.x141 - m.x162)
    **2 + (m.x231 - m.x252)**2) + 1 / sqrt((m.x51 - m.x73)**2 + (m.x141 -
    m.x163)**2 + (m.x231 - m.x253)**2) + 1 / sqrt((m.x51 - m.x74)**2 + (m.x141
    - m.x164)**2 + (m.x231 - m.x254)**2) + 1 / sqrt((m.x51 - m.x75)**2 + (
    m.x141 - m.x165)**2 + (m.x231 - m.x255)**2) + 1 / sqrt((m.x51 - m.x76)**2
    + (m.x141 - m.x166)**2 + (m.x231 - m.x256)**2) + 1 / sqrt((m.x51 - m.x77)
    **2 + (m.x141 - m.x167)**2 + (m.x231 - m.x257)**2) + 1 / sqrt((m.x51 -
    m.x78)**2 + (m.x141 - m.x168)**2 + (m.x231 - m.x258)**2) + 1 / sqrt((m.x51
    - m.x79)**2 + (m.x141 - m.x169)**2 + (m.x231 - m.x259)**2) + 1 / sqrt((
    m.x51 - m.x80)**2 + (m.x141 - m.x170)**2 + (m.x231 - m.x260)**2) + 1 /
    sqrt((m.x51 - m.x81)**2 + (m.x141 - m.x171)**2 + (m.x231 - m.x261)**2) + 1
    / sqrt((m.x51 - m.x82)**2 + (m.x141 - m.x172)**2 + (m.x231 - m.x262)**2)
    + 1 / sqrt((m.x51 - m.x83)**2 + (m.x141 - m.x173)**2 + (m.x231 - m.x263)**
    2) + 1 / sqrt((m.x51 - m.x84)**2 + (m.x141 - m.x174)**2 + (m.x231 - m.x264)
    **2) + 1 / sqrt((m.x51 - m.x85)**2 + (m.x141 - m.x175)**2 + (m.x231 -
    m.x265)**2) + 1 / sqrt((m.x51 - m.x86)**2 + (m.x141 - m.x176)**2 + (m.x231
    - m.x266)**2) + 1 / sqrt((m.x51 - m.x87)**2 + (m.x141 - m.x177)**2 + (
    m.x231 - m.x267)**2) + 1 / sqrt((m.x51 - m.x88)**2 + (m.x141 - m.x178)**2
    + (m.x231 - m.x268)**2) + 1 / sqrt((m.x51 - m.x89)**2 + (m.x141 - m.x179)
    **2 + (m.x231 - m.x269)**2) + 1 / sqrt((m.x51 - m.x90)**2 + (m.x141 -
    m.x180)**2 + (m.x231 - m.x270)**2) + 1 / sqrt((m.x52 - m.x53)**2 + (m.x142
    - m.x143)**2 + (m.x232 - m.x233)**2) + 1 / sqrt((m.x52 - m.x54)**2 + (
    m.x142 - m.x144)**2 + (m.x232 - m.x234)**2) + 1 / sqrt((m.x52 - m.x55)**2
    + (m.x142 - m.x145)**2 + (m.x232 - m.x235)**2) + 1 / sqrt((m.x52 - m.x56)
    **2 + (m.x142 - m.x146)**2 + (m.x232 - m.x236)**2) + 1 / sqrt((m.x52 -
    m.x57)**2 + (m.x142 - m.x147)**2 + (m.x232 - m.x237)**2) + 1 / sqrt((m.x52
    - m.x58)**2 + (m.x142 - m.x148)**2 + (m.x232 - m.x238)**2) + 1 / sqrt((
    m.x52 - m.x59)**2 + (m.x142 - m.x149)**2 + (m.x232 - m.x239)**2) + 1 /
    sqrt((m.x52 - m.x60)**2 + (m.x142 - m.x150)**2 + (m.x232 - m.x240)**2) + 1
    / sqrt((m.x52 - m.x61)**2 + (m.x142 - m.x151)**2 + (m.x232 - m.x241)**2)
    + 1 / sqrt((m.x52 - m.x62)**2 + (m.x142 - m.x152)**2 + (m.x232 - m.x242)**
    2) + 1 / sqrt((m.x52 - m.x63)**2 + (m.x142 - m.x153)**2 + (m.x232 - m.x243)
    **2) + 1 / sqrt((m.x52 - m.x64)**2 + (m.x142 - m.x154)**2 + (m.x232 -
    m.x244)**2) + 1 / sqrt((m.x52 - m.x65)**2 + (m.x142 - m.x155)**2 + (m.x232
    - m.x245)**2) + 1 / sqrt((m.x52 - m.x66)**2 + (m.x142 - m.x156)**2 + (
    m.x232 - m.x246)**2) + 1 / sqrt((m.x52 - m.x67)**2 + (m.x142 - m.x157)**2
    + (m.x232 - m.x247)**2) + 1 / sqrt((m.x52 - m.x68)**2 + (m.x142 - m.x158)
    **2 + (m.x232 - m.x248)**2) + 1 / sqrt((m.x52 - m.x69)**2 + (m.x142 -
    m.x159)**2 + (m.x232 - m.x249)**2) + 1 / sqrt((m.x52 - m.x70)**2 + (m.x142
    - m.x160)**2 + (m.x232 - m.x250)**2) + 1 / sqrt((m.x52 - m.x71)**2 + (
    m.x142 - m.x161)**2 + (m.x232 - m.x251)**2) + 1 / sqrt((m.x52 - m.x72)**2
    + (m.x142 - m.x162)**2 + (m.x232 - m.x252)**2) + 1 / sqrt((m.x52 - m.x73)
    **2 + (m.x142 - m.x163)**2 + (m.x232 - m.x253)**2) + 1 / sqrt((m.x52 -
    m.x74)**2 + (m.x142 - m.x164)**2 + (m.x232 - m.x254)**2) + 1 / sqrt((m.x52
    - m.x75)**2 + (m.x142 - m.x165)**2 + (m.x232 - m.x255)**2) + 1 / sqrt((
    m.x52 - m.x76)**2 + (m.x142 - m.x166)**2 + (m.x232 - m.x256)**2) + 1 /
    sqrt((m.x52 - m.x77)**2 + (m.x142 - m.x167)**2 + (m.x232 - m.x257)**2) + 1
    / sqrt((m.x52 - m.x78)**2 + (m.x142 - m.x168)**2 + (m.x232 - m.x258)**2)
    + 1 / sqrt((m.x52 - m.x79)**2 + (m.x142 - m.x169)**2 + (m.x232 - m.x259)**
    2) + 1 / sqrt((m.x52 - m.x80)**2 + (m.x142 - m.x170)**2 + (m.x232 - m.x260)
    **2) + 1 / sqrt((m.x52 - m.x81)**2 + (m.x142 - m.x171)**2 + (m.x232 -
    m.x261)**2) + 1 / sqrt((m.x52 - m.x82)**2 + (m.x142 - m.x172)**2 + (m.x232
    - m.x262)**2) + 1 / sqrt((m.x52 - m.x83)**2 + (m.x142 - m.x173)**2 + (
    m.x232 - m.x263)**2) + 1 / sqrt((m.x52 - m.x84)**2 + (m.x142 - m.x174)**2
    + (m.x232 - m.x264)**2) + 1 / sqrt((m.x52 - m.x85)**2 + (m.x142 - m.x175)
    **2 + (m.x232 - m.x265)**2) + 1 / sqrt((m.x52 - m.x86)**2 + (m.x142 -
    m.x176)**2 + (m.x232 - m.x266)**2) + 1 / sqrt((m.x52 - m.x87)**2 + (m.x142
    - m.x177)**2 + (m.x232 - m.x267)**2) + 1 / sqrt((m.x52 - m.x88)**2 + (
    m.x142 - m.x178)**2 + (m.x232 - m.x268)**2) + 1 / sqrt((m.x52 - m.x89)**2
    + (m.x142 - m.x179)**2 + (m.x232 - m.x269)**2) + 1 / sqrt((m.x52 - m.x90)
    **2 + (m.x142 - m.x180)**2 + (m.x232 - m.x270)**2) + 1 / sqrt((m.x53 -
    m.x54)**2 + (m.x143 - m.x144)**2 + (m.x233 - m.x234)**2) + 1 / sqrt((m.x53
    - m.x55)**2 + (m.x143 - m.x145)**2 + (m.x233 - m.x235)**2) + 1 / sqrt((
    m.x53 - m.x56)**2 + (m.x143 - m.x146)**2 + (m.x233 - m.x236)**2) + 1 /
    sqrt((m.x53 - m.x57)**2 + (m.x143 - m.x147)**2 + (m.x233 - m.x237)**2) + 1
    / sqrt((m.x53 - m.x58)**2 + (m.x143 - m.x148)**2 + (m.x233 - m.x238)**2)
    + 1 / sqrt((m.x53 - m.x59)**2 + (m.x143 - m.x149)**2 + (m.x233 - m.x239)**
    2) + 1 / sqrt((m.x53 - m.x60)**2 + (m.x143 - m.x150)**2 + (m.x233 - m.x240)
    **2) + 1 / sqrt((m.x53 - m.x61)**2 + (m.x143 - m.x151)**2 + (m.x233 -
    m.x241)**2) + 1 / sqrt((m.x53 - m.x62)**2 + (m.x143 - m.x152)**2 + (m.x233
    - m.x242)**2) + 1 / sqrt((m.x53 - m.x63)**2 + (m.x143 - m.x153)**2 + (
    m.x233 - m.x243)**2) + 1 / sqrt((m.x53 - m.x64)**2 + (m.x143 - m.x154)**2
    + (m.x233 - m.x244)**2) + 1 / sqrt((m.x53 - m.x65)**2 + (m.x143 - m.x155)
    **2 + (m.x233 - m.x245)**2) + 1 / sqrt((m.x53 - m.x66)**2 + (m.x143 -
    m.x156)**2 + (m.x233 - m.x246)**2) + 1 / sqrt((m.x53 - m.x67)**2 + (m.x143
    - m.x157)**2 + (m.x233 - m.x247)**2) + 1 / sqrt((m.x53 - m.x68)**2 + (
    m.x143 - m.x158)**2 + (m.x233 - m.x248)**2) + 1 / sqrt((m.x53 - m.x69)**2
    + (m.x143 - m.x159)**2 + (m.x233 - m.x249)**2) + 1 / sqrt((m.x53 - m.x70)
    **2 + (m.x143 - m.x160)**2 + (m.x233 - m.x250)**2) + 1 / sqrt((m.x53 -
    m.x71)**2 + (m.x143 - m.x161)**2 + (m.x233 - m.x251)**2) + 1 / sqrt((m.x53
    - m.x72)**2 + (m.x143 - m.x162)**2 + (m.x233 - m.x252)**2) + 1 / sqrt((
    m.x53 - m.x73)**2 + (m.x143 - m.x163)**2 + (m.x233 - m.x253)**2) + 1 /
    sqrt((m.x53 - m.x74)**2 + (m.x143 - m.x164)**2 + (m.x233 - m.x254)**2) + 1
    / sqrt((m.x53 - m.x75)**2 + (m.x143 - m.x165)**2 + (m.x233 - m.x255)**2)
    + 1 / sqrt((m.x53 - m.x76)**2 + (m.x143 - m.x166)**2 + (m.x233 - m.x256)**
    2) + 1 / sqrt((m.x53 - m.x77)**2 + (m.x143 - m.x167)**2 + (m.x233 - m.x257)
    **2) + 1 / sqrt((m.x53 - m.x78)**2 + (m.x143 - m.x168)**2 + (m.x233 -
    m.x258)**2) + 1 / sqrt((m.x53 - m.x79)**2 + (m.x143 - m.x169)**2 + (m.x233
    - m.x259)**2) + 1 / sqrt((m.x53 - m.x80)**2 + (m.x143 - m.x170)**2 + (
    m.x233 - m.x260)**2) + 1 / sqrt((m.x53 - m.x81)**2 + (m.x143 - m.x171)**2
    + (m.x233 - m.x261)**2) + 1 / sqrt((m.x53 - m.x82)**2 + (m.x143 - m.x172)
    **2 + (m.x233 - m.x262)**2) + 1 / sqrt((m.x53 - m.x83)**2 + (m.x143 -
    m.x173)**2 + (m.x233 - m.x263)**2) + 1 / sqrt((m.x53 - m.x84)**2 + (m.x143
    - m.x174)**2 + (m.x233 - m.x264)**2) + 1 / sqrt((m.x53 - m.x85)**2 + (
    m.x143 - m.x175)**2 + (m.x233 - m.x265)**2) + 1 / sqrt((m.x53 - m.x86)**2
    + (m.x143 - m.x176)**2 + (m.x233 - m.x266)**2) + 1 / sqrt((m.x53 - m.x87)
    **2 + (m.x143 - m.x177)**2 + (m.x233 - m.x267)**2) + 1 / sqrt((m.x53 -
    m.x88)**2 + (m.x143 - m.x178)**2 + (m.x233 - m.x268)**2) + 1 / sqrt((m.x53
    - m.x89)**2 + (m.x143 - m.x179)**2 + (m.x233 - m.x269)**2) + 1 / sqrt((
    m.x53 - m.x90)**2 + (m.x143 - m.x180)**2 + (m.x233 - m.x270)**2) + 1 /
    sqrt((m.x54 - m.x55)**2 + (m.x144 - m.x145)**2 + (m.x234 - m.x235)**2) + 1
    / sqrt((m.x54 - m.x56)**2 + (m.x144 - m.x146)**2 + (m.x234 - m.x236)**2)
    + 1 / sqrt((m.x54 - m.x57)**2 + (m.x144 - m.x147)**2 + (m.x234 - m.x237)**
    2) + 1 / sqrt((m.x54 - m.x58)**2 + (m.x144 - m.x148)**2 + (m.x234 - m.x238)
    **2) + 1 / sqrt((m.x54 - m.x59)**2 + (m.x144 - m.x149)**2 + (m.x234 -
    m.x239)**2) + 1 / sqrt((m.x54 - m.x60)**2 + (m.x144 - m.x150)**2 + (m.x234
    - m.x240)**2) + 1 / sqrt((m.x54 - m.x61)**2 + (m.x144 - m.x151)**2 + (
    m.x234 - m.x241)**2) + 1 / sqrt((m.x54 - m.x62)**2 + (m.x144 - m.x152)**2
    + (m.x234 - m.x242)**2) + 1 / sqrt((m.x54 - m.x63)**2 + (m.x144 - m.x153)
    **2 + (m.x234 - m.x243)**2) + 1 / sqrt((m.x54 - m.x64)**2 + (m.x144 -
    m.x154)**2 + (m.x234 - m.x244)**2) + 1 / sqrt((m.x54 - m.x65)**2 + (m.x144
    - m.x155)**2 + (m.x234 - m.x245)**2) + 1 / sqrt((m.x54 - m.x66)**2 + (
    m.x144 - m.x156)**2 + (m.x234 - m.x246)**2) + 1 / sqrt((m.x54 - m.x67)**2
    + (m.x144 - m.x157)**2 + (m.x234 - m.x247)**2) + 1 / sqrt((m.x54 - m.x68)
    **2 + (m.x144 - m.x158)**2 + (m.x234 - m.x248)**2) + 1 / sqrt((m.x54 -
    m.x69)**2 + (m.x144 - m.x159)**2 + (m.x234 - m.x249)**2) + 1 / sqrt((m.x54
    - m.x70)**2 + (m.x144 - m.x160)**2 + (m.x234 - m.x250)**2) + 1 / sqrt((
    m.x54 - m.x71)**2 + (m.x144 - m.x161)**2 + (m.x234 - m.x251)**2) + 1 /
    sqrt((m.x54 - m.x72)**2 + (m.x144 - m.x162)**2 + (m.x234 - m.x252)**2) + 1
    / sqrt((m.x54 - m.x73)**2 + (m.x144 - m.x163)**2 + (m.x234 - m.x253)**2)
    + 1 / sqrt((m.x54 - m.x74)**2 + (m.x144 - m.x164)**2 + (m.x234 - m.x254)**
    2) + 1 / sqrt((m.x54 - m.x75)**2 + (m.x144 - m.x165)**2 + (m.x234 - m.x255)
    **2) + 1 / sqrt((m.x54 - m.x76)**2 + (m.x144 - m.x166)**2 + (m.x234 -
    m.x256)**2) + 1 / sqrt((m.x54 - m.x77)**2 + (m.x144 - m.x167)**2 + (m.x234
    - m.x257)**2) + 1 / sqrt((m.x54 - m.x78)**2 + (m.x144 - m.x168)**2 + (
    m.x234 - m.x258)**2) + 1 / sqrt((m.x54 - m.x79)**2 + (m.x144 - m.x169)**2
    + (m.x234 - m.x259)**2) + 1 / sqrt((m.x54 - m.x80)**2 + (m.x144 - m.x170)
    **2 + (m.x234 - m.x260)**2) + 1 / sqrt((m.x54 - m.x81)**2 + (m.x144 -
    m.x171)**2 + (m.x234 - m.x261)**2) + 1 / sqrt((m.x54 - m.x82)**2 + (m.x144
    - m.x172)**2 + (m.x234 - m.x262)**2) + 1 / sqrt((m.x54 - m.x83)**2 + (
    m.x144 - m.x173)**2 + (m.x234 - m.x263)**2) + 1 / sqrt((m.x54 - m.x84)**2
    + (m.x144 - m.x174)**2 + (m.x234 - m.x264)**2) + 1 / sqrt((m.x54 - m.x85)
    **2 + (m.x144 - m.x175)**2 + (m.x234 - m.x265)**2) + 1 / sqrt((m.x54 -
    m.x86)**2 + (m.x144 - m.x176)**2 + (m.x234 - m.x266)**2) + 1 / sqrt((m.x54
    - m.x87)**2 + (m.x144 - m.x177)**2 + (m.x234 - m.x267)**2) + 1 / sqrt((
    m.x54 - m.x88)**2 + (m.x144 - m.x178)**2 + (m.x234 - m.x268)**2) + 1 /
    sqrt((m.x54 - m.x89)**2 + (m.x144 - m.x179)**2 + (m.x234 - m.x269)**2) + 1
    / sqrt((m.x54 - m.x90)**2 + (m.x144 - m.x180)**2 + (m.x234 - m.x270)**2)
    + 1 / sqrt((m.x55 - m.x56)**2 + (m.x145 - m.x146)**2 + (m.x235 - m.x236)**
    2) + 1 / sqrt((m.x55 - m.x57)**2 + (m.x145 - m.x147)**2 + (m.x235 - m.x237)
    **2) + 1 / sqrt((m.x55 - m.x58)**2 + (m.x145 - m.x148)**2 + (m.x235 -
    m.x238)**2) + 1 / sqrt((m.x55 - m.x59)**2 + (m.x145 - m.x149)**2 + (m.x235
    - m.x239)**2) + 1 / sqrt((m.x55 - m.x60)**2 + (m.x145 - m.x150)**2 + (
    m.x235 - m.x240)**2) + 1 / sqrt((m.x55 - m.x61)**2 + (m.x145 - m.x151)**2
    + (m.x235 - m.x241)**2) + 1 / sqrt((m.x55 - m.x62)**2 + (m.x145 - m.x152)
    **2 + (m.x235 - m.x242)**2) + 1 / sqrt((m.x55 - m.x63)**2 + (m.x145 -
    m.x153)**2 + (m.x235 - m.x243)**2) + 1 / sqrt((m.x55 - m.x64)**2 + (m.x145
    - m.x154)**2 + (m.x235 - m.x244)**2) + 1 / sqrt((m.x55 - m.x65)**2 + (
    m.x145 - m.x155)**2 + (m.x235 - m.x245)**2) + 1 / sqrt((m.x55 - m.x66)**2
    + (m.x145 - m.x156)**2 + (m.x235 - m.x246)**2) + 1 / sqrt((m.x55 - m.x67)
    **2 + (m.x145 - m.x157)**2 + (m.x235 - m.x247)**2) + 1 / sqrt((m.x55 -
    m.x68)**2 + (m.x145 - m.x158)**2 + (m.x235 - m.x248)**2) + 1 / sqrt((m.x55
    - m.x69)**2 + (m.x145 - m.x159)**2 + (m.x235 - m.x249)**2) + 1 / sqrt((
    m.x55 - m.x70)**2 + (m.x145 - m.x160)**2 + (m.x235 - m.x250)**2) + 1 /
    sqrt((m.x55 - m.x71)**2 + (m.x145 - m.x161)**2 + (m.x235 - m.x251)**2) + 1
    / sqrt((m.x55 - m.x72)**2 + (m.x145 - m.x162)**2 + (m.x235 - m.x252)**2)
    + 1 / sqrt((m.x55 - m.x73)**2 + (m.x145 - m.x163)**2 + (m.x235 - m.x253)**
    2) + 1 / sqrt((m.x55 - m.x74)**2 + (m.x145 - m.x164)**2 + (m.x235 - m.x254)
    **2) + 1 / sqrt((m.x55 - m.x75)**2 + (m.x145 - m.x165)**2 + (m.x235 -
    m.x255)**2) + 1 / sqrt((m.x55 - m.x76)**2 + (m.x145 - m.x166)**2 + (m.x235
    - m.x256)**2) + 1 / sqrt((m.x55 - m.x77)**2 + (m.x145 - m.x167)**2 + (
    m.x235 - m.x257)**2) + 1 / sqrt((m.x55 - m.x78)**2 + (m.x145 - m.x168)**2
    + (m.x235 - m.x258)**2) + 1 / sqrt((m.x55 - m.x79)**2 + (m.x145 - m.x169)
    **2 + (m.x235 - m.x259)**2) + 1 / sqrt((m.x55 - m.x80)**2 + (m.x145 -
    m.x170)**2 + (m.x235 - m.x260)**2) + 1 / sqrt((m.x55 - m.x81)**2 + (m.x145
    - m.x171)**2 + (m.x235 - m.x261)**2) + 1 / sqrt((m.x55 - m.x82)**2 + (
    m.x145 - m.x172)**2 + (m.x235 - m.x262)**2) + 1 / sqrt((m.x55 - m.x83)**2
    + (m.x145 - m.x173)**2 + (m.x235 - m.x263)**2) + 1 / sqrt((m.x55 - m.x84)
    **2 + (m.x145 - m.x174)**2 + (m.x235 - m.x264)**2) + 1 / sqrt((m.x55 -
    m.x85)**2 + (m.x145 - m.x175)**2 + (m.x235 - m.x265)**2) + 1 / sqrt((m.x55
    - m.x86)**2 + (m.x145 - m.x176)**2 + (m.x235 - m.x266)**2) + 1 / sqrt((
    m.x55 - m.x87)**2 + (m.x145 - m.x177)**2 + (m.x235 - m.x267)**2) + 1 /
    sqrt((m.x55 - m.x88)**2 + (m.x145 - m.x178)**2 + (m.x235 - m.x268)**2) + 1
    / sqrt((m.x55 - m.x89)**2 + (m.x145 - m.x179)**2 + (m.x235 - m.x269)**2)
    + 1 / sqrt((m.x55 - m.x90)**2 + (m.x145 - m.x180)**2 + (m.x235 - m.x270)**
    2) + 1 / sqrt((m.x56 - m.x57)**2 + (m.x146 - m.x147)**2 + (m.x236 - m.x237)
    **2) + 1 / sqrt((m.x56 - m.x58)**2 + (m.x146 - m.x148)**2 + (m.x236 -
    m.x238)**2) + 1 / sqrt((m.x56 - m.x59)**2 + (m.x146 - m.x149)**2 + (m.x236
    - m.x239)**2) + 1 / sqrt((m.x56 - m.x60)**2 + (m.x146 - m.x150)**2 + (
    m.x236 - m.x240)**2) + 1 / sqrt((m.x56 - m.x61)**2 + (m.x146 - m.x151)**2
    + (m.x236 - m.x241)**2) + 1 / sqrt((m.x56 - m.x62)**2 + (m.x146 - m.x152)
    **2 + (m.x236 - m.x242)**2) + 1 / sqrt((m.x56 - m.x63)**2 + (m.x146 -
    m.x153)**2 + (m.x236 - m.x243)**2) + 1 / sqrt((m.x56 - m.x64)**2 + (m.x146
    - m.x154)**2 + (m.x236 - m.x244)**2) + 1 / sqrt((m.x56 - m.x65)**2 + (
    m.x146 - m.x155)**2 + (m.x236 - m.x245)**2) + 1 / sqrt((m.x56 - m.x66)**2
    + (m.x146 - m.x156)**2 + (m.x236 - m.x246)**2) + 1 / sqrt((m.x56 - m.x67)
    **2 + (m.x146 - m.x157)**2 + (m.x236 - m.x247)**2) + 1 / sqrt((m.x56 -
    m.x68)**2 + (m.x146 - m.x158)**2 + (m.x236 - m.x248)**2) + 1 / sqrt((m.x56
    - m.x69)**2 + (m.x146 - m.x159)**2 + (m.x236 - m.x249)**2) + 1 / sqrt((
    m.x56 - m.x70)**2 + (m.x146 - m.x160)**2 + (m.x236 - m.x250)**2) + 1 /
    sqrt((m.x56 - m.x71)**2 + (m.x146 - m.x161)**2 + (m.x236 - m.x251)**2) + 1
    / sqrt((m.x56 - m.x72)**2 + (m.x146 - m.x162)**2 + (m.x236 - m.x252)**2)
    + 1 / sqrt((m.x56 - m.x73)**2 + (m.x146 - m.x163)**2 + (m.x236 - m.x253)**
    2) + 1 / sqrt((m.x56 - m.x74)**2 + (m.x146 - m.x164)**2 + (m.x236 - m.x254)
    **2) + 1 / sqrt((m.x56 - m.x75)**2 + (m.x146 - m.x165)**2 + (m.x236 -
    m.x255)**2) + 1 / sqrt((m.x56 - m.x76)**2 + (m.x146 - m.x166)**2 + (m.x236
    - m.x256)**2) + 1 / sqrt((m.x56 - m.x77)**2 + (m.x146 - m.x167)**2 + (
    m.x236 - m.x257)**2) + 1 / sqrt((m.x56 - m.x78)**2 + (m.x146 - m.x168)**2
    + (m.x236 - m.x258)**2) + 1 / sqrt((m.x56 - m.x79)**2 + (m.x146 - m.x169)
    **2 + (m.x236 - m.x259)**2) + 1 / sqrt((m.x56 - m.x80)**2 + (m.x146 -
    m.x170)**2 + (m.x236 - m.x260)**2) + 1 / sqrt((m.x56 - m.x81)**2 + (m.x146
    - m.x171)**2 + (m.x236 - m.x261)**2) + 1 / sqrt((m.x56 - m.x82)**2 + (
    m.x146 - m.x172)**2 + (m.x236 - m.x262)**2) + 1 / sqrt((m.x56 - m.x83)**2
    + (m.x146 - m.x173)**2 + (m.x236 - m.x263)**2) + 1 / sqrt((m.x56 - m.x84)
    **2 + (m.x146 - m.x174)**2 + (m.x236 - m.x264)**2) + 1 / sqrt((m.x56 -
    m.x85)**2 + (m.x146 - m.x175)**2 + (m.x236 - m.x265)**2) + 1 / sqrt((m.x56
    - m.x86)**2 + (m.x146 - m.x176)**2 + (m.x236 - m.x266)**2) + 1 / sqrt((
    m.x56 - m.x87)**2 + (m.x146 - m.x177)**2 + (m.x236 - m.x267)**2) + 1 /
    sqrt((m.x56 - m.x88)**2 + (m.x146 - m.x178)**2 + (m.x236 - m.x268)**2) + 1
    / sqrt((m.x56 - m.x89)**2 + (m.x146 - m.x179)**2 + (m.x236 - m.x269)**2)
    + 1 / sqrt((m.x56 - m.x90)**2 + (m.x146 - m.x180)**2 + (m.x236 - m.x270)**
    2) + 1 / sqrt((m.x57 - m.x58)**2 + (m.x147 - m.x148)**2 + (m.x237 - m.x238)
    **2) + 1 / sqrt((m.x57 - m.x59)**2 + (m.x147 - m.x149)**2 + (m.x237 -
    m.x239)**2) + 1 / sqrt((m.x57 - m.x60)**2 + (m.x147 - m.x150)**2 + (m.x237
    - m.x240)**2) + 1 / sqrt((m.x57 - m.x61)**2 + (m.x147 - m.x151)**2 + (
    m.x237 - m.x241)**2) + 1 / sqrt((m.x57 - m.x62)**2 + (m.x147 - m.x152)**2
    + (m.x237 - m.x242)**2) + 1 / sqrt((m.x57 - m.x63)**2 + (m.x147 - m.x153)
    **2 + (m.x237 - m.x243)**2) + 1 / sqrt((m.x57 - m.x64)**2 + (m.x147 -
    m.x154)**2 + (m.x237 - m.x244)**2) + 1 / sqrt((m.x57 - m.x65)**2 + (m.x147
    - m.x155)**2 + (m.x237 - m.x245)**2) + 1 / sqrt((m.x57 - m.x66)**2 + (
    m.x147 - m.x156)**2 + (m.x237 - m.x246)**2) + 1 / sqrt((m.x57 - m.x67)**2
    + (m.x147 - m.x157)**2 + (m.x237 - m.x247)**2) + 1 / sqrt((m.x57 - m.x68)
    **2 + (m.x147 - m.x158)**2 + (m.x237 - m.x248)**2) + 1 / sqrt((m.x57 -
    m.x69)**2 + (m.x147 - m.x159)**2 + (m.x237 - m.x249)**2) + 1 / sqrt((m.x57
    - m.x70)**2 + (m.x147 - m.x160)**2 + (m.x237 - m.x250)**2) + 1 / sqrt((
    m.x57 - m.x71)**2 + (m.x147 - m.x161)**2 + (m.x237 - m.x251)**2) + 1 /
    sqrt((m.x57 - m.x72)**2 + (m.x147 - m.x162)**2 + (m.x237 - m.x252)**2) + 1
    / sqrt((m.x57 - m.x73)**2 + (m.x147 - m.x163)**2 + (m.x237 - m.x253)**2)
    + 1 / sqrt((m.x57 - m.x74)**2 + (m.x147 - m.x164)**2 + (m.x237 - m.x254)**
    2) + 1 / sqrt((m.x57 - m.x75)**2 + (m.x147 - m.x165)**2 + (m.x237 - m.x255)
    **2) + 1 / sqrt((m.x57 - m.x76)**2 + (m.x147 - m.x166)**2 + (m.x237 -
    m.x256)**2) + 1 / sqrt((m.x57 - m.x77)**2 + (m.x147 - m.x167)**2 + (m.x237
    - m.x257)**2) + 1 / sqrt((m.x57 - m.x78)**2 + (m.x147 - m.x168)**2 + (
    m.x237 - m.x258)**2) + 1 / sqrt((m.x57 - m.x79)**2 + (m.x147 - m.x169)**2
    + (m.x237 - m.x259)**2) + 1 / sqrt((m.x57 - m.x80)**2 + (m.x147 - m.x170)
    **2 + (m.x237 - m.x260)**2) + 1 / sqrt((m.x57 - m.x81)**2 + (m.x147 -
    m.x171)**2 + (m.x237 - m.x261)**2) + 1 / sqrt((m.x57 - m.x82)**2 + (m.x147
    - m.x172)**2 + (m.x237 - m.x262)**2) + 1 / sqrt((m.x57 - m.x83)**2 + (
    m.x147 - m.x173)**2 + (m.x237 - m.x263)**2) + 1 / sqrt((m.x57 - m.x84)**2
    + (m.x147 - m.x174)**2 + (m.x237 - m.x264)**2) + 1 / sqrt((m.x57 - m.x85)
    **2 + (m.x147 - m.x175)**2 + (m.x237 - m.x265)**2) + 1 / sqrt((m.x57 -
    m.x86)**2 + (m.x147 - m.x176)**2 + (m.x237 - m.x266)**2) + 1 / sqrt((m.x57
    - m.x87)**2 + (m.x147 - m.x177)**2 + (m.x237 - m.x267)**2) + 1 / sqrt((
    m.x57 - m.x88)**2 + (m.x147 - m.x178)**2 + (m.x237 - m.x268)**2) + 1 /
    sqrt((m.x57 - m.x89)**2 + (m.x147 - m.x179)**2 + (m.x237 - m.x269)**2) + 1
    / sqrt((m.x57 - m.x90)**2 + (m.x147 - m.x180)**2 + (m.x237 - m.x270)**2)
    + 1 / sqrt((m.x58 - m.x59)**2 + (m.x148 - m.x149)**2 + (m.x238 - m.x239)**
    2) + 1 / sqrt((m.x58 - m.x60)**2 + (m.x148 - m.x150)**2 + (m.x238 - m.x240)
    **2) + 1 / sqrt((m.x58 - m.x61)**2 + (m.x148 - m.x151)**2 + (m.x238 -
    m.x241)**2) + 1 / sqrt((m.x58 - m.x62)**2 + (m.x148 - m.x152)**2 + (m.x238
    - m.x242)**2) + 1 / sqrt((m.x58 - m.x63)**2 + (m.x148 - m.x153)**2 + (
    m.x238 - m.x243)**2) + 1 / sqrt((m.x58 - m.x64)**2 + (m.x148 - m.x154)**2
    + (m.x238 - m.x244)**2) + 1 / sqrt((m.x58 - m.x65)**2 + (m.x148 - m.x155)
    **2 + (m.x238 - m.x245)**2) + 1 / sqrt((m.x58 - m.x66)**2 + (m.x148 -
    m.x156)**2 + (m.x238 - m.x246)**2) + 1 / sqrt((m.x58 - m.x67)**2 + (m.x148
    - m.x157)**2 + (m.x238 - m.x247)**2) + 1 / sqrt((m.x58 - m.x68)**2 + (
    m.x148 - m.x158)**2 + (m.x238 - m.x248)**2) + 1 / sqrt((m.x58 - m.x69)**2
    + (m.x148 - m.x159)**2 + (m.x238 - m.x249)**2) + 1 / sqrt((m.x58 - m.x70)
    **2 + (m.x148 - m.x160)**2 + (m.x238 - m.x250)**2) + 1 / sqrt((m.x58 -
    m.x71)**2 + (m.x148 - m.x161)**2 + (m.x238 - m.x251)**2) + 1 / sqrt((m.x58
    - m.x72)**2 + (m.x148 - m.x162)**2 + (m.x238 - m.x252)**2) + 1 / sqrt((
    m.x58 - m.x73)**2 + (m.x148 - m.x163)**2 + (m.x238 - m.x253)**2) + 1 /
    sqrt((m.x58 - m.x74)**2 + (m.x148 - m.x164)**2 + (m.x238 - m.x254)**2) + 1
    / sqrt((m.x58 - m.x75)**2 + (m.x148 - m.x165)**2 + (m.x238 - m.x255)**2)
    + 1 / sqrt((m.x58 - m.x76)**2 + (m.x148 - m.x166)**2 + (m.x238 - m.x256)**
    2) + 1 / sqrt((m.x58 - m.x77)**2 + (m.x148 - m.x167)**2 + (m.x238 - m.x257)
    **2) + 1 / sqrt((m.x58 - m.x78)**2 + (m.x148 - m.x168)**2 + (m.x238 -
    m.x258)**2) + 1 / sqrt((m.x58 - m.x79)**2 + (m.x148 - m.x169)**2 + (m.x238
    - m.x259)**2) + 1 / sqrt((m.x58 - m.x80)**2 + (m.x148 - m.x170)**2 + (
    m.x238 - m.x260)**2) + 1 / sqrt((m.x58 - m.x81)**2 + (m.x148 - m.x171)**2
    + (m.x238 - m.x261)**2) + 1 / sqrt((m.x58 - m.x82)**2 + (m.x148 - m.x172)
    **2 + (m.x238 - m.x262)**2) + 1 / sqrt((m.x58 - m.x83)**2 + (m.x148 -
    m.x173)**2 + (m.x238 - m.x263)**2) + 1 / sqrt((m.x58 - m.x84)**2 + (m.x148
    - m.x174)**2 + (m.x238 - m.x264)**2) + 1 / sqrt((m.x58 - m.x85)**2 + (
    m.x148 - m.x175)**2 + (m.x238 - m.x265)**2) + 1 / sqrt((m.x58 - m.x86)**2
    + (m.x148 - m.x176)**2 + (m.x238 - m.x266)**2) + 1 / sqrt((m.x58 - m.x87)
    **2 + (m.x148 - m.x177)**2 + (m.x238 - m.x267)**2) + 1 / sqrt((m.x58 -
    m.x88)**2 + (m.x148 - m.x178)**2 + (m.x238 - m.x268)**2) + 1 / sqrt((m.x58
    - m.x89)**2 + (m.x148 - m.x179)**2 + (m.x238 - m.x269)**2) + 1 / sqrt((
    m.x58 - m.x90)**2 + (m.x148 - m.x180)**2 + (m.x238 - m.x270)**2) + 1 /
    sqrt((m.x59 - m.x60)**2 + (m.x149 - m.x150)**2 + (m.x239 - m.x240)**2) + 1
    / sqrt((m.x59 - m.x61)**2 + (m.x149 - m.x151)**2 + (m.x239 - m.x241)**2)
    + 1 / sqrt((m.x59 - m.x62)**2 + (m.x149 - m.x152)**2 + (m.x239 - m.x242)**
    2) + 1 / sqrt((m.x59 - m.x63)**2 + (m.x149 - m.x153)**2 + (m.x239 - m.x243)
    **2) + 1 / sqrt((m.x59 - m.x64)**2 + (m.x149 - m.x154)**2 + (m.x239 -
    m.x244)**2) + 1 / sqrt((m.x59 - m.x65)**2 + (m.x149 - m.x155)**2 + (m.x239
    - m.x245)**2) + 1 / sqrt((m.x59 - m.x66)**2 + (m.x149 - m.x156)**2 + (
    m.x239 - m.x246)**2) + 1 / sqrt((m.x59 - m.x67)**2 + (m.x149 - m.x157)**2
    + (m.x239 - m.x247)**2) + 1 / sqrt((m.x59 - m.x68)**2 + (m.x149 - m.x158)
    **2 + (m.x239 - m.x248)**2) + 1 / sqrt((m.x59 - m.x69)**2 + (m.x149 -
    m.x159)**2 + (m.x239 - m.x249)**2) + 1 / sqrt((m.x59 - m.x70)**2 + (m.x149
    - m.x160)**2 + (m.x239 - m.x250)**2) + 1 / sqrt((m.x59 - m.x71)**2 + (
    m.x149 - m.x161)**2 + (m.x239 - m.x251)**2) + 1 / sqrt((m.x59 - m.x72)**2
    + (m.x149 - m.x162)**2 + (m.x239 - m.x252)**2) + 1 / sqrt((m.x59 - m.x73)
    **2 + (m.x149 - m.x163)**2 + (m.x239 - m.x253)**2) + 1 / sqrt((m.x59 -
    m.x74)**2 + (m.x149 - m.x164)**2 + (m.x239 - m.x254)**2) + 1 / sqrt((m.x59
    - m.x75)**2 + (m.x149 - m.x165)**2 + (m.x239 - m.x255)**2) + 1 / sqrt((
    m.x59 - m.x76)**2 + (m.x149 - m.x166)**2 + (m.x239 - m.x256)**2) + 1 /
    sqrt((m.x59 - m.x77)**2 + (m.x149 - m.x167)**2 + (m.x239 - m.x257)**2) + 1
    / sqrt((m.x59 - m.x78)**2 + (m.x149 - m.x168)**2 + (m.x239 - m.x258)**2)
    + 1 / sqrt((m.x59 - m.x79)**2 + (m.x149 - m.x169)**2 + (m.x239 - m.x259)**
    2) + 1 / sqrt((m.x59 - m.x80)**2 + (m.x149 - m.x170)**2 + (m.x239 - m.x260)
    **2) + 1 / sqrt((m.x59 - m.x81)**2 + (m.x149 - m.x171)**2 + (m.x239 -
    m.x261)**2) + 1 / sqrt((m.x59 - m.x82)**2 + (m.x149 - m.x172)**2 + (m.x239
    - m.x262)**2) + 1 / sqrt((m.x59 - m.x83)**2 + (m.x149 - m.x173)**2 + (
    m.x239 - m.x263)**2) + 1 / sqrt((m.x59 - m.x84)**2 + (m.x149 - m.x174)**2
    + (m.x239 - m.x264)**2) + 1 / sqrt((m.x59 - m.x85)**2 + (m.x149 - m.x175)
    **2 + (m.x239 - m.x265)**2) + 1 / sqrt((m.x59 - m.x86)**2 + (m.x149 -
    m.x176)**2 + (m.x239 - m.x266)**2) + 1 / sqrt((m.x59 - m.x87)**2 + (m.x149
    - m.x177)**2 + (m.x239 - m.x267)**2) + 1 / sqrt((m.x59 - m.x88)**2 + (
    m.x149 - m.x178)**2 + (m.x239 - m.x268)**2) + 1 / sqrt((m.x59 - m.x89)**2
    + (m.x149 - m.x179)**2 + (m.x239 - m.x269)**2) + 1 / sqrt((m.x59 - m.x90)
    **2 + (m.x149 - m.x180)**2 + (m.x239 - m.x270)**2) + 1 / sqrt((m.x60 -
    m.x61)**2 + (m.x150 - m.x151)**2 + (m.x240 - m.x241)**2) + 1 / sqrt((m.x60
    - m.x62)**2 + (m.x150 - m.x152)**2 + (m.x240 - m.x242)**2) + 1 / sqrt((
    m.x60 - m.x63)**2 + (m.x150 - m.x153)**2 + (m.x240 - m.x243)**2) + 1 /
    sqrt((m.x60 - m.x64)**2 + (m.x150 - m.x154)**2 + (m.x240 - m.x244)**2) + 1
    / sqrt((m.x60 - m.x65)**2 + (m.x150 - m.x155)**2 + (m.x240 - m.x245)**2)
    + 1 / sqrt((m.x60 - m.x66)**2 + (m.x150 - m.x156)**2 + (m.x240 - m.x246)**
    2) + 1 / sqrt((m.x60 - m.x67)**2 + (m.x150 - m.x157)**2 + (m.x240 - m.x247)
    **2) + 1 / sqrt((m.x60 - m.x68)**2 + (m.x150 - m.x158)**2 + (m.x240 -
    m.x248)**2) + 1 / sqrt((m.x60 - m.x69)**2 + (m.x150 - m.x159)**2 + (m.x240
    - m.x249)**2) + 1 / sqrt((m.x60 - m.x70)**2 + (m.x150 - m.x160)**2 + (
    m.x240 - m.x250)**2) + 1 / sqrt((m.x60 - m.x71)**2 + (m.x150 - m.x161)**2
    + (m.x240 - m.x251)**2) + 1 / sqrt((m.x60 - m.x72)**2 + (m.x150 - m.x162)
    **2 + (m.x240 - m.x252)**2) + 1 / sqrt((m.x60 - m.x73)**2 + (m.x150 -
    m.x163)**2 + (m.x240 - m.x253)**2) + 1 / sqrt((m.x60 - m.x74)**2 + (m.x150
    - m.x164)**2 + (m.x240 - m.x254)**2) + 1 / sqrt((m.x60 - m.x75)**2 + (
    m.x150 - m.x165)**2 + (m.x240 - m.x255)**2) + 1 / sqrt((m.x60 - m.x76)**2
    + (m.x150 - m.x166)**2 + (m.x240 - m.x256)**2) + 1 / sqrt((m.x60 - m.x77)
    **2 + (m.x150 - m.x167)**2 + (m.x240 - m.x257)**2) + 1 / sqrt((m.x60 -
    m.x78)**2 + (m.x150 - m.x168)**2 + (m.x240 - m.x258)**2) + 1 / sqrt((m.x60
    - m.x79)**2 + (m.x150 - m.x169)**2 + (m.x240 - m.x259)**2) + 1 / sqrt((
    m.x60 - m.x80)**2 + (m.x150 - m.x170)**2 + (m.x240 - m.x260)**2) + 1 /
    sqrt((m.x60 - m.x81)**2 + (m.x150 - m.x171)**2 + (m.x240 - m.x261)**2) + 1
    / sqrt((m.x60 - m.x82)**2 + (m.x150 - m.x172)**2 + (m.x240 - m.x262)**2)
    + 1 / sqrt((m.x60 - m.x83)**2 + (m.x150 - m.x173)**2 + (m.x240 - m.x263)**
    2) + 1 / sqrt((m.x60 - m.x84)**2 + (m.x150 - m.x174)**2 + (m.x240 - m.x264)
    **2) + 1 / sqrt((m.x60 - m.x85)**2 + (m.x150 - m.x175)**2 + (m.x240 -
    m.x265)**2) + 1 / sqrt((m.x60 - m.x86)**2 + (m.x150 - m.x176)**2 + (m.x240
    - m.x266)**2) + 1 / sqrt((m.x60 - m.x87)**2 + (m.x150 - m.x177)**2 + (
    m.x240 - m.x267)**2) + 1 / sqrt((m.x60 - m.x88)**2 + (m.x150 - m.x178)**2
    + (m.x240 - m.x268)**2) + 1 / sqrt((m.x60 - m.x89)**2 + (m.x150 - m.x179)
    **2 + (m.x240 - m.x269)**2) + 1 / sqrt((m.x60 - m.x90)**2 + (m.x150 -
    m.x180)**2 + (m.x240 - m.x270)**2) + 1 / sqrt((m.x61 - m.x62)**2 + (m.x151
    - m.x152)**2 + (m.x241 - m.x242)**2) + 1 / sqrt((m.x61 - m.x63)**2 + (
    m.x151 - m.x153)**2 + (m.x241 - m.x243)**2) + 1 / sqrt((m.x61 - m.x64)**2
    + (m.x151 - m.x154)**2 + (m.x241 - m.x244)**2) + 1 / sqrt((m.x61 - m.x65)
    **2 + (m.x151 - m.x155)**2 + (m.x241 - m.x245)**2) + 1 / sqrt((m.x61 -
    m.x66)**2 + (m.x151 - m.x156)**2 + (m.x241 - m.x246)**2) + 1 / sqrt((m.x61
    - m.x67)**2 + (m.x151 - m.x157)**2 + (m.x241 - m.x247)**2) + 1 / sqrt((
    m.x61 - m.x68)**2 + (m.x151 - m.x158)**2 + (m.x241 - m.x248)**2) + 1 /
    sqrt((m.x61 - m.x69)**2 + (m.x151 - m.x159)**2 + (m.x241 - m.x249)**2) + 1
    / sqrt((m.x61 - m.x70)**2 + (m.x151 - m.x160)**2 + (m.x241 - m.x250)**2)
    + 1 / sqrt((m.x61 - m.x71)**2 + (m.x151 - m.x161)**2 + (m.x241 - m.x251)**
    2) + 1 / sqrt((m.x61 - m.x72)**2 + (m.x151 - m.x162)**2 + (m.x241 - m.x252)
    **2) + 1 / sqrt((m.x61 - m.x73)**2 + (m.x151 - m.x163)**2 + (m.x241 -
    m.x253)**2) + 1 / sqrt((m.x61 - m.x74)**2 + (m.x151 - m.x164)**2 + (m.x241
    - m.x254)**2) + 1 / sqrt((m.x61 - m.x75)**2 + (m.x151 - m.x165)**2 + (
    m.x241 - m.x255)**2) + 1 / sqrt((m.x61 - m.x76)**2 + (m.x151 - m.x166)**2
    + (m.x241 - m.x256)**2) + 1 / sqrt((m.x61 - m.x77)**2 + (m.x151 - m.x167)
    **2 + (m.x241 - m.x257)**2) + 1 / sqrt((m.x61 - m.x78)**2 + (m.x151 -
    m.x168)**2 + (m.x241 - m.x258)**2) + 1 / sqrt((m.x61 - m.x79)**2 + (m.x151
    - m.x169)**2 + (m.x241 - m.x259)**2) + 1 / sqrt((m.x61 - m.x80)**2 + (
    m.x151 - m.x170)**2 + (m.x241 - m.x260)**2) + 1 / sqrt((m.x61 - m.x81)**2
    + (m.x151 - m.x171)**2 + (m.x241 - m.x261)**2) + 1 / sqrt((m.x61 - m.x82)
    **2 + (m.x151 - m.x172)**2 + (m.x241 - m.x262)**2) + 1 / sqrt((m.x61 -
    m.x83)**2 + (m.x151 - m.x173)**2 + (m.x241 - m.x263)**2) + 1 / sqrt((m.x61
    - m.x84)**2 + (m.x151 - m.x174)**2 + (m.x241 - m.x264)**2) + 1 / sqrt((
    m.x61 - m.x85)**2 + (m.x151 - m.x175)**2 + (m.x241 - m.x265)**2) + 1 /
    sqrt((m.x61 - m.x86)**2 + (m.x151 - m.x176)**2 + (m.x241 - m.x266)**2) + 1
    / sqrt((m.x61 - m.x87)**2 + (m.x151 - m.x177)**2 + (m.x241 - m.x267)**2)
    + 1 / sqrt((m.x61 - m.x88)**2 + (m.x151 - m.x178)**2 + (m.x241 - m.x268)**
    2) + 1 / sqrt((m.x61 - m.x89)**2 + (m.x151 - m.x179)**2 + (m.x241 - m.x269)
    **2) + 1 / sqrt((m.x61 - m.x90)**2 + (m.x151 - m.x180)**2 + (m.x241 -
    m.x270)**2) + 1 / sqrt((m.x62 - m.x63)**2 + (m.x152 - m.x153)**2 + (m.x242
    - m.x243)**2) + 1 / sqrt((m.x62 - m.x64)**2 + (m.x152 - m.x154)**2 + (
    m.x242 - m.x244)**2) + 1 / sqrt((m.x62 - m.x65)**2 + (m.x152 - m.x155)**2
    + (m.x242 - m.x245)**2) + 1 / sqrt((m.x62 - m.x66)**2 + (m.x152 - m.x156)
    **2 + (m.x242 - m.x246)**2) + 1 / sqrt((m.x62 - m.x67)**2 + (m.x152 -
    m.x157)**2 + (m.x242 - m.x247)**2) + 1 / sqrt((m.x62 - m.x68)**2 + (m.x152
    - m.x158)**2 + (m.x242 - m.x248)**2) + 1 / sqrt((m.x62 - m.x69)**2 + (
    m.x152 - m.x159)**2 + (m.x242 - m.x249)**2) + 1 / sqrt((m.x62 - m.x70)**2
    + (m.x152 - m.x160)**2 + (m.x242 - m.x250)**2) + 1 / sqrt((m.x62 - m.x71)
    **2 + (m.x152 - m.x161)**2 + (m.x242 - m.x251)**2) + 1 / sqrt((m.x62 -
    m.x72)**2 + (m.x152 - m.x162)**2 + (m.x242 - m.x252)**2) + 1 / sqrt((m.x62
    - m.x73)**2 + (m.x152 - m.x163)**2 + (m.x242 - m.x253)**2) + 1 / sqrt((
    m.x62 - m.x74)**2 + (m.x152 - m.x164)**2 + (m.x242 - m.x254)**2) + 1 /
    sqrt((m.x62 - m.x75)**2 + (m.x152 - m.x165)**2 + (m.x242 - m.x255)**2) + 1
    / sqrt((m.x62 - m.x76)**2 + (m.x152 - m.x166)**2 + (m.x242 - m.x256)**2)
    + 1 / sqrt((m.x62 - m.x77)**2 + (m.x152 - m.x167)**2 + (m.x242 - m.x257)**
    2) + 1 / sqrt((m.x62 - m.x78)**2 + (m.x152 - m.x168)**2 + (m.x242 - m.x258)
    **2) + 1 / sqrt((m.x62 - m.x79)**2 + (m.x152 - m.x169)**2 + (m.x242 -
    m.x259)**2) + 1 / sqrt((m.x62 - m.x80)**2 + (m.x152 - m.x170)**2 + (m.x242
    - m.x260)**2) + 1 / sqrt((m.x62 - m.x81)**2 + (m.x152 - m.x171)**2 + (
    m.x242 - m.x261)**2) + 1 / sqrt((m.x62 - m.x82)**2 + (m.x152 - m.x172)**2
    + (m.x242 - m.x262)**2) + 1 / sqrt((m.x62 - m.x83)**2 + (m.x152 - m.x173)
    **2 + (m.x242 - m.x263)**2) + 1 / sqrt((m.x62 - m.x84)**2 + (m.x152 -
    m.x174)**2 + (m.x242 - m.x264)**2) + 1 / sqrt((m.x62 - m.x85)**2 + (m.x152
    - m.x175)**2 + (m.x242 - m.x265)**2) + 1 / sqrt((m.x62 - m.x86)**2 + (
    m.x152 - m.x176)**2 + (m.x242 - m.x266)**2) + 1 / sqrt((m.x62 - m.x87)**2
    + (m.x152 - m.x177)**2 + (m.x242 - m.x267)**2) + 1 / sqrt((m.x62 - m.x88)
    **2 + (m.x152 - m.x178)**2 + (m.x242 - m.x268)**2) + 1 / sqrt((m.x62 -
    m.x89)**2 + (m.x152 - m.x179)**2 + (m.x242 - m.x269)**2) + 1 / sqrt((m.x62
    - m.x90)**2 + (m.x152 - m.x180)**2 + (m.x242 - m.x270)**2) + 1 / sqrt((
    m.x63 - m.x64)**2 + (m.x153 - m.x154)**2 + (m.x243 - m.x244)**2) + 1 /
    sqrt((m.x63 - m.x65)**2 + (m.x153 - m.x155)**2 + (m.x243 - m.x245)**2) + 1
    / sqrt((m.x63 - m.x66)**2 + (m.x153 - m.x156)**2 + (m.x243 - m.x246)**2)
    + 1 / sqrt((m.x63 - m.x67)**2 + (m.x153 - m.x157)**2 + (m.x243 - m.x247)**
    2) + 1 / sqrt((m.x63 - m.x68)**2 + (m.x153 - m.x158)**2 + (m.x243 - m.x248)
    **2) + 1 / sqrt((m.x63 - m.x69)**2 + (m.x153 - m.x159)**2 + (m.x243 -
    m.x249)**2) + 1 / sqrt((m.x63 - m.x70)**2 + (m.x153 - m.x160)**2 + (m.x243
    - m.x250)**2) + 1 / sqrt((m.x63 - m.x71)**2 + (m.x153 - m.x161)**2 + (
    m.x243 - m.x251)**2) + 1 / sqrt((m.x63 - m.x72)**2 + (m.x153 - m.x162)**2
    + (m.x243 - m.x252)**2) + 1 / sqrt((m.x63 - m.x73)**2 + (m.x153 - m.x163)
    **2 + (m.x243 - m.x253)**2) + 1 / sqrt((m.x63 - m.x74)**2 + (m.x153 -
    m.x164)**2 + (m.x243 - m.x254)**2) + 1 / sqrt((m.x63 - m.x75)**2 + (m.x153
    - m.x165)**2 + (m.x243 - m.x255)**2) + 1 / sqrt((m.x63 - m.x76)**2 + (
    m.x153 - m.x166)**2 + (m.x243 - m.x256)**2) + 1 / sqrt((m.x63 - m.x77)**2
    + (m.x153 - m.x167)**2 + (m.x243 - m.x257)**2) + 1 / sqrt((m.x63 - m.x78)
    **2 + (m.x153 - m.x168)**2 + (m.x243 - m.x258)**2) + 1 / sqrt((m.x63 -
    m.x79)**2 + (m.x153 - m.x169)**2 + (m.x243 - m.x259)**2) + 1 / sqrt((m.x63
    - m.x80)**2 + (m.x153 - m.x170)**2 + (m.x243 - m.x260)**2) + 1 / sqrt((
    m.x63 - m.x81)**2 + (m.x153 - m.x171)**2 + (m.x243 - m.x261)**2) + 1 /
    sqrt((m.x63 - m.x82)**2 + (m.x153 - m.x172)**2 + (m.x243 - m.x262)**2) + 1
    / sqrt((m.x63 - m.x83)**2 + (m.x153 - m.x173)**2 + (m.x243 - m.x263)**2)
    + 1 / sqrt((m.x63 - m.x84)**2 + (m.x153 - m.x174)**2 + (m.x243 - m.x264)**
    2) + 1 / sqrt((m.x63 - m.x85)**2 + (m.x153 - m.x175)**2 + (m.x243 - m.x265)
    **2) + 1 / sqrt((m.x63 - m.x86)**2 + (m.x153 - m.x176)**2 + (m.x243 -
    m.x266)**2) + 1 / sqrt((m.x63 - m.x87)**2 + (m.x153 - m.x177)**2 + (m.x243
    - m.x267)**2) + 1 / sqrt((m.x63 - m.x88)**2 + (m.x153 - m.x178)**2 + (
    m.x243 - m.x268)**2) + 1 / sqrt((m.x63 - m.x89)**2 + (m.x153 - m.x179)**2
    + (m.x243 - m.x269)**2) + 1 / sqrt((m.x63 - m.x90)**2 + (m.x153 - m.x180)
    **2 + (m.x243 - m.x270)**2) + 1 / sqrt((m.x64 - m.x65)**2 + (m.x154 -
    m.x155)**2 + (m.x244 - m.x245)**2) + 1 / sqrt((m.x64 - m.x66)**2 + (m.x154
    - m.x156)**2 + (m.x244 - m.x246)**2) + 1 / sqrt((m.x64 - m.x67)**2 + (
    m.x154 - m.x157)**2 + (m.x244 - m.x247)**2) + 1 / sqrt((m.x64 - m.x68)**2
    + (m.x154 - m.x158)**2 + (m.x244 - m.x248)**2) + 1 / sqrt((m.x64 - m.x69)
    **2 + (m.x154 - m.x159)**2 + (m.x244 - m.x249)**2) + 1 / sqrt((m.x64 -
    m.x70)**2 + (m.x154 - m.x160)**2 + (m.x244 - m.x250)**2) + 1 / sqrt((m.x64
    - m.x71)**2 + (m.x154 - m.x161)**2 + (m.x244 - m.x251)**2) + 1 / sqrt((
    m.x64 - m.x72)**2 + (m.x154 - m.x162)**2 + (m.x244 - m.x252)**2) + 1 /
    sqrt((m.x64 - m.x73)**2 + (m.x154 - m.x163)**2 + (m.x244 - m.x253)**2) + 1
    / sqrt((m.x64 - m.x74)**2 + (m.x154 - m.x164)**2 + (m.x244 - m.x254)**2)
    + 1 / sqrt((m.x64 - m.x75)**2 + (m.x154 - m.x165)**2 + (m.x244 - m.x255)**
    2) + 1 / sqrt((m.x64 - m.x76)**2 + (m.x154 - m.x166)**2 + (m.x244 - m.x256)
    **2) + 1 / sqrt((m.x64 - m.x77)**2 + (m.x154 - m.x167)**2 + (m.x244 -
    m.x257)**2) + 1 / sqrt((m.x64 - m.x78)**2 + (m.x154 - m.x168)**2 + (m.x244
    - m.x258)**2) + 1 / sqrt((m.x64 - m.x79)**2 + (m.x154 - m.x169)**2 + (
    m.x244 - m.x259)**2) + 1 / sqrt((m.x64 - m.x80)**2 + (m.x154 - m.x170)**2
    + (m.x244 - m.x260)**2) + 1 / sqrt((m.x64 - m.x81)**2 + (m.x154 - m.x171)
    **2 + (m.x244 - m.x261)**2) + 1 / sqrt((m.x64 - m.x82)**2 + (m.x154 -
    m.x172)**2 + (m.x244 - m.x262)**2) + 1 / sqrt((m.x64 - m.x83)**2 + (m.x154
    - m.x173)**2 + (m.x244 - m.x263)**2) + 1 / sqrt((m.x64 - m.x84)**2 + (
    m.x154 - m.x174)**2 + (m.x244 - m.x264)**2) + 1 / sqrt((m.x64 - m.x85)**2
    + (m.x154 - m.x175)**2 + (m.x244 - m.x265)**2) + 1 / sqrt((m.x64 - m.x86)
    **2 + (m.x154 - m.x176)**2 + (m.x244 - m.x266)**2) + 1 / sqrt((m.x64 -
    m.x87)**2 + (m.x154 - m.x177)**2 + (m.x244 - m.x267)**2) + 1 / sqrt((m.x64
    - m.x88)**2 + (m.x154 - m.x178)**2 + (m.x244 - m.x268)**2) + 1 / sqrt((
    m.x64 - m.x89)**2 + (m.x154 - m.x179)**2 + (m.x244 - m.x269)**2) + 1 /
    sqrt((m.x64 - m.x90)**2 + (m.x154 - m.x180)**2 + (m.x244 - m.x270)**2) + 1
    / sqrt((m.x65 - m.x66)**2 + (m.x155 - m.x156)**2 + (m.x245 - m.x246)**2)
    + 1 / sqrt((m.x65 - m.x67)**2 + (m.x155 - m.x157)**2 + (m.x245 - m.x247)**
    2) + 1 / sqrt((m.x65 - m.x68)**2 + (m.x155 - m.x158)**2 + (m.x245 - m.x248)
    **2) + 1 / sqrt((m.x65 - m.x69)**2 + (m.x155 - m.x159)**2 + (m.x245 -
    m.x249)**2) + 1 / sqrt((m.x65 - m.x70)**2 + (m.x155 - m.x160)**2 + (m.x245
    - m.x250)**2) + 1 / sqrt((m.x65 - m.x71)**2 + (m.x155 - m.x161)**2 + (
    m.x245 - m.x251)**2) + 1 / sqrt((m.x65 - m.x72)**2 + (m.x155 - m.x162)**2
    + (m.x245 - m.x252)**2) + 1 / sqrt((m.x65 - m.x73)**2 + (m.x155 - m.x163)
    **2 + (m.x245 - m.x253)**2) + 1 / sqrt((m.x65 - m.x74)**2 + (m.x155 -
    m.x164)**2 + (m.x245 - m.x254)**2) + 1 / sqrt((m.x65 - m.x75)**2 + (m.x155
    - m.x165)**2 + (m.x245 - m.x255)**2) + 1 / sqrt((m.x65 - m.x76)**2 + (
    m.x155 - m.x166)**2 + (m.x245 - m.x256)**2) + 1 / sqrt((m.x65 - m.x77)**2
    + (m.x155 - m.x167)**2 + (m.x245 - m.x257)**2) + 1 / sqrt((m.x65 - m.x78)
    **2 + (m.x155 - m.x168)**2 + (m.x245 - m.x258)**2) + 1 / sqrt((m.x65 -
    m.x79)**2 + (m.x155 - m.x169)**2 + (m.x245 - m.x259)**2) + 1 / sqrt((m.x65
    - m.x80)**2 + (m.x155 - m.x170)**2 + (m.x245 - m.x260)**2) + 1 / sqrt((
    m.x65 - m.x81)**2 + (m.x155 - m.x171)**2 + (m.x245 - m.x261)**2) + 1 /
    sqrt((m.x65 - m.x82)**2 + (m.x155 - m.x172)**2 + (m.x245 - m.x262)**2) + 1
    / sqrt((m.x65 - m.x83)**2 + (m.x155 - m.x173)**2 + (m.x245 - m.x263)**2)
    + 1 / sqrt((m.x65 - m.x84)**2 + (m.x155 - m.x174)**2 + (m.x245 - m.x264)**
    2) + 1 / sqrt((m.x65 - m.x85)**2 + (m.x155 - m.x175)**2 + (m.x245 - m.x265)
    **2) + 1 / sqrt((m.x65 - m.x86)**2 + (m.x155 - m.x176)**2 + (m.x245 -
    m.x266)**2) + 1 / sqrt((m.x65 - m.x87)**2 + (m.x155 - m.x177)**2 + (m.x245
    - m.x267)**2) + 1 / sqrt((m.x65 - m.x88)**2 + (m.x155 - m.x178)**2 + (
    m.x245 - m.x268)**2) + 1 / sqrt((m.x65 - m.x89)**2 + (m.x155 - m.x179)**2
    + (m.x245 - m.x269)**2) + 1 / sqrt((m.x65 - m.x90)**2 + (m.x155 - m.x180)
    **2 + (m.x245 - m.x270)**2) + 1 / sqrt((m.x66 - m.x67)**2 + (m.x156 -
    m.x157)**2 + (m.x246 - m.x247)**2) + 1 / sqrt((m.x66 - m.x68)**2 + (m.x156
    - m.x158)**2 + (m.x246 - m.x248)**2) + 1 / sqrt((m.x66 - m.x69)**2 + (
    m.x156 - m.x159)**2 + (m.x246 - m.x249)**2) + 1 / sqrt((m.x66 - m.x70)**2
    + (m.x156 - m.x160)**2 + (m.x246 - m.x250)**2) + 1 / sqrt((m.x66 - m.x71)
    **2 + (m.x156 - m.x161)**2 + (m.x246 - m.x251)**2) + 1 / sqrt((m.x66 -
    m.x72)**2 + (m.x156 - m.x162)**2 + (m.x246 - m.x252)**2) + 1 / sqrt((m.x66
    - m.x73)**2 + (m.x156 - m.x163)**2 + (m.x246 - m.x253)**2) + 1 / sqrt((
    m.x66 - m.x74)**2 + (m.x156 - m.x164)**2 + (m.x246 - m.x254)**2) + 1 /
    sqrt((m.x66 - m.x75)**2 + (m.x156 - m.x165)**2 + (m.x246 - m.x255)**2) + 1
    / sqrt((m.x66 - m.x76)**2 + (m.x156 - m.x166)**2 + (m.x246 - m.x256)**2)
    + 1 / sqrt((m.x66 - m.x77)**2 + (m.x156 - m.x167)**2 + (m.x246 - m.x257)**
    2) + 1 / sqrt((m.x66 - m.x78)**2 + (m.x156 - m.x168)**2 + (m.x246 - m.x258)
    **2) + 1 / sqrt((m.x66 - m.x79)**2 + (m.x156 - m.x169)**2 + (m.x246 -
    m.x259)**2) + 1 / sqrt((m.x66 - m.x80)**2 + (m.x156 - m.x170)**2 + (m.x246
    - m.x260)**2) + 1 / sqrt((m.x66 - m.x81)**2 + (m.x156 - m.x171)**2 + (
    m.x246 - m.x261)**2) + 1 / sqrt((m.x66 - m.x82)**2 + (m.x156 - m.x172)**2
    + (m.x246 - m.x262)**2) + 1 / sqrt((m.x66 - m.x83)**2 + (m.x156 - m.x173)
    **2 + (m.x246 - m.x263)**2) + 1 / sqrt((m.x66 - m.x84)**2 + (m.x156 -
    m.x174)**2 + (m.x246 - m.x264)**2) + 1 / sqrt((m.x66 - m.x85)**2 + (m.x156
    - m.x175)**2 + (m.x246 - m.x265)**2) + 1 / sqrt((m.x66 - m.x86)**2 + (
    m.x156 - m.x176)**2 + (m.x246 - m.x266)**2) + 1 / sqrt((m.x66 - m.x87)**2
    + (m.x156 - m.x177)**2 + (m.x246 - m.x267)**2) + 1 / sqrt((m.x66 - m.x88)
    **2 + (m.x156 - m.x178)**2 + (m.x246 - m.x268)**2) + 1 / sqrt((m.x66 -
    m.x89)**2 + (m.x156 - m.x179)**2 + (m.x246 - m.x269)**2) + 1 / sqrt((m.x66
    - m.x90)**2 + (m.x156 - m.x180)**2 + (m.x246 - m.x270)**2) + 1 / sqrt((
    m.x67 - m.x68)**2 + (m.x157 - m.x158)**2 + (m.x247 - m.x248)**2) + 1 /
    sqrt((m.x67 - m.x69)**2 + (m.x157 - m.x159)**2 + (m.x247 - m.x249)**2) + 1
    / sqrt((m.x67 - m.x70)**2 + (m.x157 - m.x160)**2 + (m.x247 - m.x250)**2)
    + 1 / sqrt((m.x67 - m.x71)**2 + (m.x157 - m.x161)**2 + (m.x247 - m.x251)**
    2) + 1 / sqrt((m.x67 - m.x72)**2 + (m.x157 - m.x162)**2 + (m.x247 - m.x252)
    **2) + 1 / sqrt((m.x67 - m.x73)**2 + (m.x157 - m.x163)**2 + (m.x247 -
    m.x253)**2) + 1 / sqrt((m.x67 - m.x74)**2 + (m.x157 - m.x164)**2 + (m.x247
    - m.x254)**2) + 1 / sqrt((m.x67 - m.x75)**2 + (m.x157 - m.x165)**2 + (
    m.x247 - m.x255)**2) + 1 / sqrt((m.x67 - m.x76)**2 + (m.x157 - m.x166)**2
    + (m.x247 - m.x256)**2) + 1 / sqrt((m.x67 - m.x77)**2 + (m.x157 - m.x167)
    **2 + (m.x247 - m.x257)**2) + 1 / sqrt((m.x67 - m.x78)**2 + (m.x157 -
    m.x168)**2 + (m.x247 - m.x258)**2) + 1 / sqrt((m.x67 - m.x79)**2 + (m.x157
    - m.x169)**2 + (m.x247 - m.x259)**2) + 1 / sqrt((m.x67 - m.x80)**2 + (
    m.x157 - m.x170)**2 + (m.x247 - m.x260)**2) + 1 / sqrt((m.x67 - m.x81)**2
    + (m.x157 - m.x171)**2 + (m.x247 - m.x261)**2) + 1 / sqrt((m.x67 - m.x82)
    **2 + (m.x157 - m.x172)**2 + (m.x247 - m.x262)**2) + 1 / sqrt((m.x67 -
    m.x83)**2 + (m.x157 - m.x173)**2 + (m.x247 - m.x263)**2) + 1 / sqrt((m.x67
    - m.x84)**2 + (m.x157 - m.x174)**2 + (m.x247 - m.x264)**2) + 1 / sqrt((
    m.x67 - m.x85)**2 + (m.x157 - m.x175)**2 + (m.x247 - m.x265)**2) + 1 /
    sqrt((m.x67 - m.x86)**2 + (m.x157 - m.x176)**2 + (m.x247 - m.x266)**2) + 1
    / sqrt((m.x67 - m.x87)**2 + (m.x157 - m.x177)**2 + (m.x247 - m.x267)**2)
    + 1 / sqrt((m.x67 - m.x88)**2 + (m.x157 - m.x178)**2 + (m.x247 - m.x268)**
    2) + 1 / sqrt((m.x67 - m.x89)**2 + (m.x157 - m.x179)**2 + (m.x247 - m.x269)
    **2) + 1 / sqrt((m.x67 - m.x90)**2 + (m.x157 - m.x180)**2 + (m.x247 -
    m.x270)**2) + 1 / sqrt((m.x68 - m.x69)**2 + (m.x158 - m.x159)**2 + (m.x248
    - m.x249)**2) + 1 / sqrt((m.x68 - m.x70)**2 + (m.x158 - m.x160)**2 + (
    m.x248 - m.x250)**2) + 1 / sqrt((m.x68 - m.x71)**2 + (m.x158 - m.x161)**2
    + (m.x248 - m.x251)**2) + 1 / sqrt((m.x68 - m.x72)**2 + (m.x158 - m.x162)
    **2 + (m.x248 - m.x252)**2) + 1 / sqrt((m.x68 - m.x73)**2 + (m.x158 -
    m.x163)**2 + (m.x248 - m.x253)**2) + 1 / sqrt((m.x68 - m.x74)**2 + (m.x158
    - m.x164)**2 + (m.x248 - m.x254)**2) + 1 / sqrt((m.x68 - m.x75)**2 + (
    m.x158 - m.x165)**2 + (m.x248 - m.x255)**2) + 1 / sqrt((m.x68 - m.x76)**2
    + (m.x158 - m.x166)**2 + (m.x248 - m.x256)**2) + 1 / sqrt((m.x68 - m.x77)
    **2 + (m.x158 - m.x167)**2 + (m.x248 - m.x257)**2) + 1 / sqrt((m.x68 -
    m.x78)**2 + (m.x158 - m.x168)**2 + (m.x248 - m.x258)**2) + 1 / sqrt((m.x68
    - m.x79)**2 + (m.x158 - m.x169)**2 + (m.x248 - m.x259)**2) + 1 / sqrt((
    m.x68 - m.x80)**2 + (m.x158 - m.x170)**2 + (m.x248 - m.x260)**2) + 1 /
    sqrt((m.x68 - m.x81)**2 + (m.x158 - m.x171)**2 + (m.x248 - m.x261)**2) + 1
    / sqrt((m.x68 - m.x82)**2 + (m.x158 - m.x172)**2 + (m.x248 - m.x262)**2)
    + 1 / sqrt((m.x68 - m.x83)**2 + (m.x158 - m.x173)**2 + (m.x248 - m.x263)**
    2) + 1 / sqrt((m.x68 - m.x84)**2 + (m.x158 - m.x174)**2 + (m.x248 - m.x264)
    **2) + 1 / sqrt((m.x68 - m.x85)**2 + (m.x158 - m.x175)**2 + (m.x248 -
    m.x265)**2) + 1 / sqrt((m.x68 - m.x86)**2 + (m.x158 - m.x176)**2 + (m.x248
    - m.x266)**2) + 1 / sqrt((m.x68 - m.x87)**2 + (m.x158 - m.x177)**2 + (
    m.x248 - m.x267)**2) + 1 / sqrt((m.x68 - m.x88)**2 + (m.x158 - m.x178)**2
    + (m.x248 - m.x268)**2) + 1 / sqrt((m.x68 - m.x89)**2 + (m.x158 - m.x179)
    **2 + (m.x248 - m.x269)**2) + 1 / sqrt((m.x68 - m.x90)**2 + (m.x158 -
    m.x180)**2 + (m.x248 - m.x270)**2) + 1 / sqrt((m.x69 - m.x70)**2 + (m.x159
    - m.x160)**2 + (m.x249 - m.x250)**2) + 1 / sqrt((m.x69 - m.x71)**2 + (
    m.x159 - m.x161)**2 + (m.x249 - m.x251)**2) + 1 / sqrt((m.x69 - m.x72)**2
    + (m.x159 - m.x162)**2 + (m.x249 - m.x252)**2) + 1 / sqrt((m.x69 - m.x73)
    **2 + (m.x159 - m.x163)**2 + (m.x249 - m.x253)**2) + 1 / sqrt((m.x69 -
    m.x74)**2 + (m.x159 - m.x164)**2 + (m.x249 - m.x254)**2) + 1 / sqrt((m.x69
    - m.x75)**2 + (m.x159 - m.x165)**2 + (m.x249 - m.x255)**2) + 1 / sqrt((
    m.x69 - m.x76)**2 + (m.x159 - m.x166)**2 + (m.x249 - m.x256)**2) + 1 /
    sqrt((m.x69 - m.x77)**2 + (m.x159 - m.x167)**2 + (m.x249 - m.x257)**2) + 1
    / sqrt((m.x69 - m.x78)**2 + (m.x159 - m.x168)**2 + (m.x249 - m.x258)**2)
    + 1 / sqrt((m.x69 - m.x79)**2 + (m.x159 - m.x169)**2 + (m.x249 - m.x259)**
    2) + 1 / sqrt((m.x69 - m.x80)**2 + (m.x159 - m.x170)**2 + (m.x249 - m.x260)
    **2) + 1 / sqrt((m.x69 - m.x81)**2 + (m.x159 - m.x171)**2 + (m.x249 -
    m.x261)**2) + 1 / sqrt((m.x69 - m.x82)**2 + (m.x159 - m.x172)**2 + (m.x249
    - m.x262)**2) + 1 / sqrt((m.x69 - m.x83)**2 + (m.x159 - m.x173)**2 + (
    m.x249 - m.x263)**2) + 1 / sqrt((m.x69 - m.x84)**2 + (m.x159 - m.x174)**2
    + (m.x249 - m.x264)**2) + 1 / sqrt((m.x69 - m.x85)**2 + (m.x159 - m.x175)
    **2 + (m.x249 - m.x265)**2) + 1 / sqrt((m.x69 - m.x86)**2 + (m.x159 -
    m.x176)**2 + (m.x249 - m.x266)**2) + 1 / sqrt((m.x69 - m.x87)**2 + (m.x159
    - m.x177)**2 + (m.x249 - m.x267)**2) + 1 / sqrt((m.x69 - m.x88)**2 + (
    m.x159 - m.x178)**2 + (m.x249 - m.x268)**2) + 1 / sqrt((m.x69 - m.x89)**2
    + (m.x159 - m.x179)**2 + (m.x249 - m.x269)**2) + 1 / sqrt((m.x69 - m.x90)
    **2 + (m.x159 - m.x180)**2 + (m.x249 - m.x270)**2) + 1 / sqrt((m.x70 -
    m.x71)**2 + (m.x160 - m.x161)**2 + (m.x250 - m.x251)**2) + 1 / sqrt((m.x70
    - m.x72)**2 + (m.x160 - m.x162)**2 + (m.x250 - m.x252)**2) + 1 / sqrt((
    m.x70 - m.x73)**2 + (m.x160 - m.x163)**2 + (m.x250 - m.x253)**2) + 1 /
    sqrt((m.x70 - m.x74)**2 + (m.x160 - m.x164)**2 + (m.x250 - m.x254)**2) + 1
    / sqrt((m.x70 - m.x75)**2 + (m.x160 - m.x165)**2 + (m.x250 - m.x255)**2)
    + 1 / sqrt((m.x70 - m.x76)**2 + (m.x160 - m.x166)**2 + (m.x250 - m.x256)**
    2) + 1 / sqrt((m.x70 - m.x77)**2 + (m.x160 - m.x167)**2 + (m.x250 - m.x257)
    **2) + 1 / sqrt((m.x70 - m.x78)**2 + (m.x160 - m.x168)**2 + (m.x250 -
    m.x258)**2) + 1 / sqrt((m.x70 - m.x79)**2 + (m.x160 - m.x169)**2 + (m.x250
    - m.x259)**2) + 1 / sqrt((m.x70 - m.x80)**2 + (m.x160 - m.x170)**2 + (
    m.x250 - m.x260)**2) + 1 / sqrt((m.x70 - m.x81)**2 + (m.x160 - m.x171)**2
    + (m.x250 - m.x261)**2) + 1 / sqrt((m.x70 - m.x82)**2 + (m.x160 - m.x172)
    **2 + (m.x250 - m.x262)**2) + 1 / sqrt((m.x70 - m.x83)**2 + (m.x160 -
    m.x173)**2 + (m.x250 - m.x263)**2) + 1 / sqrt((m.x70 - m.x84)**2 + (m.x160
    - m.x174)**2 + (m.x250 - m.x264)**2) + 1 / sqrt((m.x70 - m.x85)**2 + (
    m.x160 - m.x175)**2 + (m.x250 - m.x265)**2) + 1 / sqrt((m.x70 - m.x86)**2
    + (m.x160 - m.x176)**2 + (m.x250 - m.x266)**2) + 1 / sqrt((m.x70 - m.x87)
    **2 + (m.x160 - m.x177)**2 + (m.x250 - m.x267)**2) + 1 / sqrt((m.x70 -
    m.x88)**2 + (m.x160 - m.x178)**2 + (m.x250 - m.x268)**2) + 1 / sqrt((m.x70
    - m.x89)**2 + (m.x160 - m.x179)**2 + (m.x250 - m.x269)**2) + 1 / sqrt((
    m.x70 - m.x90)**2 + (m.x160 - m.x180)**2 + (m.x250 - m.x270)**2) + 1 /
    sqrt((m.x71 - m.x72)**2 + (m.x161 - m.x162)**2 + (m.x251 - m.x252)**2) + 1
    / sqrt((m.x71 - m.x73)**2 + (m.x161 - m.x163)**2 + (m.x251 - m.x253)**2)
    + 1 / sqrt((m.x71 - m.x74)**2 + (m.x161 - m.x164)**2 + (m.x251 - m.x254)**
    2) + 1 / sqrt((m.x71 - m.x75)**2 + (m.x161 - m.x165)**2 + (m.x251 - m.x255)
    **2) + 1 / sqrt((m.x71 - m.x76)**2 + (m.x161 - m.x166)**2 + (m.x251 -
    m.x256)**2) + 1 / sqrt((m.x71 - m.x77)**2 + (m.x161 - m.x167)**2 + (m.x251
    - m.x257)**2) + 1 / sqrt((m.x71 - m.x78)**2 + (m.x161 - m.x168)**2 + (
    m.x251 - m.x258)**2) + 1 / sqrt((m.x71 - m.x79)**2 + (m.x161 - m.x169)**2
    + (m.x251 - m.x259)**2) + 1 / sqrt((m.x71 - m.x80)**2 + (m.x161 - m.x170)
    **2 + (m.x251 - m.x260)**2) + 1 / sqrt((m.x71 - m.x81)**2 + (m.x161 -
    m.x171)**2 + (m.x251 - m.x261)**2) + 1 / sqrt((m.x71 - m.x82)**2 + (m.x161
    - m.x172)**2 + (m.x251 - m.x262)**2) + 1 / sqrt((m.x71 - m.x83)**2 + (
    m.x161 - m.x173)**2 + (m.x251 - m.x263)**2) + 1 / sqrt((m.x71 - m.x84)**2
    + (m.x161 - m.x174)**2 + (m.x251 - m.x264)**2) + 1 / sqrt((m.x71 - m.x85)
    **2 + (m.x161 - m.x175)**2 + (m.x251 - m.x265)**2) + 1 / sqrt((m.x71 -
    m.x86)**2 + (m.x161 - m.x176)**2 + (m.x251 - m.x266)**2) + 1 / sqrt((m.x71
    - m.x87)**2 + (m.x161 - m.x177)**2 + (m.x251 - m.x267)**2) + 1 / sqrt((
    m.x71 - m.x88)**2 + (m.x161 - m.x178)**2 + (m.x251 - m.x268)**2) + 1 /
    sqrt((m.x71 - m.x89)**2 + (m.x161 - m.x179)**2 + (m.x251 - m.x269)**2) + 1
    / sqrt((m.x71 - m.x90)**2 + (m.x161 - m.x180)**2 + (m.x251 - m.x270)**2)
    + 1 / sqrt((m.x72 - m.x73)**2 + (m.x162 - m.x163)**2 + (m.x252 - m.x253)**
    2) + 1 / sqrt((m.x72 - m.x74)**2 + (m.x162 - m.x164)**2 + (m.x252 - m.x254)
    **2) + 1 / sqrt((m.x72 - m.x75)**2 + (m.x162 - m.x165)**2 + (m.x252 -
    m.x255)**2) + 1 / sqrt((m.x72 - m.x76)**2 + (m.x162 - m.x166)**2 + (m.x252
    - m.x256)**2) + 1 / sqrt((m.x72 - m.x77)**2 + (m.x162 - m.x167)**2 + (
    m.x252 - m.x257)**2) + 1 / sqrt((m.x72 - m.x78)**2 + (m.x162 - m.x168)**2
    + (m.x252 - m.x258)**2) + 1 / sqrt((m.x72 - m.x79)**2 + (m.x162 - m.x169)
    **2 + (m.x252 - m.x259)**2) + 1 / sqrt((m.x72 - m.x80)**2 + (m.x162 -
    m.x170)**2 + (m.x252 - m.x260)**2) + 1 / sqrt((m.x72 - m.x81)**2 + (m.x162
    - m.x171)**2 + (m.x252 - m.x261)**2) + 1 / sqrt((m.x72 - m.x82)**2 + (
    m.x162 - m.x172)**2 + (m.x252 - m.x262)**2) + 1 / sqrt((m.x72 - m.x83)**2
    + (m.x162 - m.x173)**2 + (m.x252 - m.x263)**2) + 1 / sqrt((m.x72 - m.x84)
    **2 + (m.x162 - m.x174)**2 + (m.x252 - m.x264)**2) + 1 / sqrt((m.x72 -
    m.x85)**2 + (m.x162 - m.x175)**2 + (m.x252 - m.x265)**2) + 1 / sqrt((m.x72
    - m.x86)**2 + (m.x162 - m.x176)**2 + (m.x252 - m.x266)**2) + 1 / sqrt((
    m.x72 - m.x87)**2 + (m.x162 - m.x177)**2 + (m.x252 - m.x267)**2) + 1 /
    sqrt((m.x72 - m.x88)**2 + (m.x162 - m.x178)**2 + (m.x252 - m.x268)**2) + 1
    / sqrt((m.x72 - m.x89)**2 + (m.x162 - m.x179)**2 + (m.x252 - m.x269)**2)
    + 1 / sqrt((m.x72 - m.x90)**2 + (m.x162 - m.x180)**2 + (m.x252 - m.x270)**
    2) + 1 / sqrt((m.x73 - m.x74)**2 + (m.x163 - m.x164)**2 + (m.x253 - m.x254)
    **2) + 1 / sqrt((m.x73 - m.x75)**2 + (m.x163 - m.x165)**2 + (m.x253 -
    m.x255)**2) + 1 / sqrt((m.x73 - m.x76)**2 + (m.x163 - m.x166)**2 + (m.x253
    - m.x256)**2) + 1 / sqrt((m.x73 - m.x77)**2 + (m.x163 - m.x167)**2 + (
    m.x253 - m.x257)**2) + 1 / sqrt((m.x73 - m.x78)**2 + (m.x163 - m.x168)**2
    + (m.x253 - m.x258)**2) + 1 / sqrt((m.x73 - m.x79)**2 + (m.x163 - m.x169)
    **2 + (m.x253 - m.x259)**2) + 1 / sqrt((m.x73 - m.x80)**2 + (m.x163 -
    m.x170)**2 + (m.x253 - m.x260)**2) + 1 / sqrt((m.x73 - m.x81)**2 + (m.x163
    - m.x171)**2 + (m.x253 - m.x261)**2) + 1 / sqrt((m.x73 - m.x82)**2 + (
    m.x163 - m.x172)**2 + (m.x253 - m.x262)**2) + 1 / sqrt((m.x73 - m.x83)**2
    + (m.x163 - m.x173)**2 + (m.x253 - m.x263)**2) + 1 / sqrt((m.x73 - m.x84)
    **2 + (m.x163 - m.x174)**2 + (m.x253 - m.x264)**2) + 1 / sqrt((m.x73 -
    m.x85)**2 + (m.x163 - m.x175)**2 + (m.x253 - m.x265)**2) + 1 / sqrt((m.x73
    - m.x86)**2 + (m.x163 - m.x176)**2 + (m.x253 - m.x266)**2) + 1 / sqrt((
    m.x73 - m.x87)**2 + (m.x163 - m.x177)**2 + (m.x253 - m.x267)**2) + 1 /
    sqrt((m.x73 - m.x88)**2 + (m.x163 - m.x178)**2 + (m.x253 - m.x268)**2) + 1
    / sqrt((m.x73 - m.x89)**2 + (m.x163 - m.x179)**2 + (m.x253 - m.x269)**2)
    + 1 / sqrt((m.x73 - m.x90)**2 + (m.x163 - m.x180)**2 + (m.x253 - m.x270)**
    2) + 1 / sqrt((m.x74 - m.x75)**2 + (m.x164 - m.x165)**2 + (m.x254 - m.x255)
    **2) + 1 / sqrt((m.x74 - m.x76)**2 + (m.x164 - m.x166)**2 + (m.x254 -
    m.x256)**2) + 1 / sqrt((m.x74 - m.x77)**2 + (m.x164 - m.x167)**2 + (m.x254
    - m.x257)**2) + 1 / sqrt((m.x74 - m.x78)**2 + (m.x164 - m.x168)**2 + (
    m.x254 - m.x258)**2) + 1 / sqrt((m.x74 - m.x79)**2 + (m.x164 - m.x169)**2
    + (m.x254 - m.x259)**2) + 1 / sqrt((m.x74 - m.x80)**2 + (m.x164 - m.x170)
    **2 + (m.x254 - m.x260)**2) + 1 / sqrt((m.x74 - m.x81)**2 + (m.x164 -
    m.x171)**2 + (m.x254 - m.x261)**2) + 1 / sqrt((m.x74 - m.x82)**2 + (m.x164
    - m.x172)**2 + (m.x254 - m.x262)**2) + 1 / sqrt((m.x74 - m.x83)**2 + (
    m.x164 - m.x173)**2 + (m.x254 - m.x263)**2) + 1 / sqrt((m.x74 - m.x84)**2
    + (m.x164 - m.x174)**2 + (m.x254 - m.x264)**2) + 1 / sqrt((m.x74 - m.x85)
    **2 + (m.x164 - m.x175)**2 + (m.x254 - m.x265)**2) + 1 / sqrt((m.x74 -
    m.x86)**2 + (m.x164 - m.x176)**2 + (m.x254 - m.x266)**2) + 1 / sqrt((m.x74
    - m.x87)**2 + (m.x164 - m.x177)**2 + (m.x254 - m.x267)**2) + 1 / sqrt((
    m.x74 - m.x88)**2 + (m.x164 - m.x178)**2 + (m.x254 - m.x268)**2) + 1 /
    sqrt((m.x74 - m.x89)**2 + (m.x164 - m.x179)**2 + (m.x254 - m.x269)**2) + 1
    / sqrt((m.x74 - m.x90)**2 + (m.x164 - m.x180)**2 + (m.x254 - m.x270)**2)
    + 1 / sqrt((m.x75 - m.x76)**2 + (m.x165 - m.x166)**2 + (m.x255 - m.x256)**
    2) + 1 / sqrt((m.x75 - m.x77)**2 + (m.x165 - m.x167)**2 + (m.x255 - m.x257)
    **2) + 1 / sqrt((m.x75 - m.x78)**2 + (m.x165 - m.x168)**2 + (m.x255 -
    m.x258)**2) + 1 / sqrt((m.x75 - m.x79)**2 + (m.x165 - m.x169)**2 + (m.x255
    - m.x259)**2) + 1 / sqrt((m.x75 - m.x80)**2 + (m.x165 - m.x170)**2 + (
    m.x255 - m.x260)**2) + 1 / sqrt((m.x75 - m.x81)**2 + (m.x165 - m.x171)**2
    + (m.x255 - m.x261)**2) + 1 / sqrt((m.x75 - m.x82)**2 + (m.x165 - m.x172)
    **2 + (m.x255 - m.x262)**2) + 1 / sqrt((m.x75 - m.x83)**2 + (m.x165 -
    m.x173)**2 + (m.x255 - m.x263)**2) + 1 / sqrt((m.x75 - m.x84)**2 + (m.x165
    - m.x174)**2 + (m.x255 - m.x264)**2) + 1 / sqrt((m.x75 - m.x85)**2 + (
    m.x165 - m.x175)**2 + (m.x255 - m.x265)**2) + 1 / sqrt((m.x75 - m.x86)**2
    + (m.x165 - m.x176)**2 + (m.x255 - m.x266)**2) + 1 / sqrt((m.x75 - m.x87)
    **2 + (m.x165 - m.x177)**2 + (m.x255 - m.x267)**2) + 1 / sqrt((m.x75 -
    m.x88)**2 + (m.x165 - m.x178)**2 + (m.x255 - m.x268)**2) + 1 / sqrt((m.x75
    - m.x89)**2 + (m.x165 - m.x179)**2 + (m.x255 - m.x269)**2) + 1 / sqrt((
    m.x75 - m.x90)**2 + (m.x165 - m.x180)**2 + (m.x255 - m.x270)**2) + 1 /
    sqrt((m.x76 - m.x77)**2 + (m.x166 - m.x167)**2 + (m.x256 - m.x257)**2) + 1
    / sqrt((m.x76 - m.x78)**2 + (m.x166 - m.x168)**2 + (m.x256 - m.x258)**2)
    + 1 / sqrt((m.x76 - m.x79)**2 + (m.x166 - m.x169)**2 + (m.x256 - m.x259)**
    2) + 1 / sqrt((m.x76 - m.x80)**2 + (m.x166 - m.x170)**2 + (m.x256 - m.x260)
    **2) + 1 / sqrt((m.x76 - m.x81)**2 + (m.x166 - m.x171)**2 + (m.x256 -
    m.x261)**2) + 1 / sqrt((m.x76 - m.x82)**2 + (m.x166 - m.x172)**2 + (m.x256
    - m.x262)**2) + 1 / sqrt((m.x76 - m.x83)**2 + (m.x166 - m.x173)**2 + (
    m.x256 - m.x263)**2) + 1 / sqrt((m.x76 - m.x84)**2 + (m.x166 - m.x174)**2
    + (m.x256 - m.x264)**2) + 1 / sqrt((m.x76 - m.x85)**2 + (m.x166 - m.x175)
    **2 + (m.x256 - m.x265)**2) + 1 / sqrt((m.x76 - m.x86)**2 + (m.x166 -
    m.x176)**2 + (m.x256 - m.x266)**2) + 1 / sqrt((m.x76 - m.x87)**2 + (m.x166
    - m.x177)**2 + (m.x256 - m.x267)**2) + 1 / sqrt((m.x76 - m.x88)**2 + (
    m.x166 - m.x178)**2 + (m.x256 - m.x268)**2) + 1 / sqrt((m.x76 - m.x89)**2
    + (m.x166 - m.x179)**2 + (m.x256 - m.x269)**2) + 1 / sqrt((m.x76 - m.x90)
    **2 + (m.x166 - m.x180)**2 + (m.x256 - m.x270)**2) + 1 / sqrt((m.x77 -
    m.x78)**2 + (m.x167 - m.x168)**2 + (m.x257 - m.x258)**2) + 1 / sqrt((m.x77
    - m.x79)**2 + (m.x167 - m.x169)**2 + (m.x257 - m.x259)**2) + 1 / sqrt((
    m.x77 - m.x80)**2 + (m.x167 - m.x170)**2 + (m.x257 - m.x260)**2) + 1 /
    sqrt((m.x77 - m.x81)**2 + (m.x167 - m.x171)**2 + (m.x257 - m.x261)**2) + 1
    / sqrt((m.x77 - m.x82)**2 + (m.x167 - m.x172)**2 + (m.x257 - m.x262)**2)
    + 1 / sqrt((m.x77 - m.x83)**2 + (m.x167 - m.x173)**2 + (m.x257 - m.x263)**
    2) + 1 / sqrt((m.x77 - m.x84)**2 + (m.x167 - m.x174)**2 + (m.x257 - m.x264)
    **2) + 1 / sqrt((m.x77 - m.x85)**2 + (m.x167 - m.x175)**2 + (m.x257 -
    m.x265)**2) + 1 / sqrt((m.x77 - m.x86)**2 + (m.x167 - m.x176)**2 + (m.x257
    - m.x266)**2) + 1 / sqrt((m.x77 - m.x87)**2 + (m.x167 - m.x177)**2 + (
    m.x257 - m.x267)**2) + 1 / sqrt((m.x77 - m.x88)**2 + (m.x167 - m.x178)**2
    + (m.x257 - m.x268)**2) + 1 / sqrt((m.x77 - m.x89)**2 + (m.x167 - m.x179)
    **2 + (m.x257 - m.x269)**2) + 1 / sqrt((m.x77 - m.x90)**2 + (m.x167 -
    m.x180)**2 + (m.x257 - m.x270)**2) + 1 / sqrt((m.x78 - m.x79)**2 + (m.x168
    - m.x169)**2 + (m.x258 - m.x259)**2) + 1 / sqrt((m.x78 - m.x80)**2 + (
    m.x168 - m.x170)**2 + (m.x258 - m.x260)**2) + 1 / sqrt((m.x78 - m.x81)**2
    + (m.x168 - m.x171)**2 + (m.x258 - m.x261)**2) + 1 / sqrt((m.x78 - m.x82)
    **2 + (m.x168 - m.x172)**2 + (m.x258 - m.x262)**2) + 1 / sqrt((m.x78 -
    m.x83)**2 + (m.x168 - m.x173)**2 + (m.x258 - m.x263)**2) + 1 / sqrt((m.x78
    - m.x84)**2 + (m.x168 - m.x174)**2 + (m.x258 - m.x264)**2) + 1 / sqrt((
    m.x78 - m.x85)**2 + (m.x168 - m.x175)**2 + (m.x258 - m.x265)**2) + 1 /
    sqrt((m.x78 - m.x86)**2 + (m.x168 - m.x176)**2 + (m.x258 - m.x266)**2) + 1
    / sqrt((m.x78 - m.x87)**2 + (m.x168 - m.x177)**2 + (m.x258 - m.x267)**2)
    + 1 / sqrt((m.x78 - m.x88)**2 + (m.x168 - m.x178)**2 + (m.x258 - m.x268)**
    2) + 1 / sqrt((m.x78 - m.x89)**2 + (m.x168 - m.x179)**2 + (m.x258 - m.x269)
    **2) + 1 / sqrt((m.x78 - m.x90)**2 + (m.x168 - m.x180)**2 + (m.x258 -
    m.x270)**2) + 1 / sqrt((m.x79 - m.x80)**2 + (m.x169 - m.x170)**2 + (m.x259
    - m.x260)**2) + 1 / sqrt((m.x79 - m.x81)**2 + (m.x169 - m.x171)**2 + (
    m.x259 - m.x261)**2) + 1 / sqrt((m.x79 - m.x82)**2 + (m.x169 - m.x172)**2
    + (m.x259 - m.x262)**2) + 1 / sqrt((m.x79 - m.x83)**2 + (m.x169 - m.x173)
    **2 + (m.x259 - m.x263)**2) + 1 / sqrt((m.x79 - m.x84)**2 + (m.x169 -
    m.x174)**2 + (m.x259 - m.x264)**2) + 1 / sqrt((m.x79 - m.x85)**2 + (m.x169
    - m.x175)**2 + (m.x259 - m.x265)**2) + 1 / sqrt((m.x79 - m.x86)**2 + (
    m.x169 - m.x176)**2 + (m.x259 - m.x266)**2) + 1 / sqrt((m.x79 - m.x87)**2
    + (m.x169 - m.x177)**2 + (m.x259 - m.x267)**2) + 1 / sqrt((m.x79 - m.x88)
    **2 + (m.x169 - m.x178)**2 + (m.x259 - m.x268)**2) + 1 / sqrt((m.x79 -
    m.x89)**2 + (m.x169 - m.x179)**2 + (m.x259 - m.x269)**2) + 1 / sqrt((m.x79
    - m.x90)**2 + (m.x169 - m.x180)**2 + (m.x259 - m.x270)**2) + 1 / sqrt((
    m.x80 - m.x81)**2 + (m.x170 - m.x171)**2 + (m.x260 - m.x261)**2) + 1 /
    sqrt((m.x80 - m.x82)**2 + (m.x170 - m.x172)**2 + (m.x260 - m.x262)**2) + 1
    / sqrt((m.x80 - m.x83)**2 + (m.x170 - m.x173)**2 + (m.x260 - m.x263)**2)
    + 1 / sqrt((m.x80 - m.x84)**2 + (m.x170 - m.x174)**2 + (m.x260 - m.x264)**
    2) + 1 / sqrt((m.x80 - m.x85)**2 + (m.x170 - m.x175)**2 + (m.x260 - m.x265)
    **2) + 1 / sqrt((m.x80 - m.x86)**2 + (m.x170 - m.x176)**2 + (m.x260 -
    m.x266)**2) + 1 / sqrt((m.x80 - m.x87)**2 + (m.x170 - m.x177)**2 + (m.x260
    - m.x267)**2) + 1 / sqrt((m.x80 - m.x88)**2 + (m.x170 - m.x178)**2 + (
    m.x260 - m.x268)**2) + 1 / sqrt((m.x80 - m.x89)**2 + (m.x170 - m.x179)**2
    + (m.x260 - m.x269)**2) + 1 / sqrt((m.x80 - m.x90)**2 + (m.x170 - m.x180)
    **2 + (m.x260 - m.x270)**2) + 1 / sqrt((m.x81 - m.x82)**2 + (m.x171 -
    m.x172)**2 + (m.x261 - m.x262)**2) + 1 / sqrt((m.x81 - m.x83)**2 + (m.x171
    - m.x173)**2 + (m.x261 - m.x263)**2) + 1 / sqrt((m.x81 - m.x84)**2 + (
    m.x171 - m.x174)**2 + (m.x261 - m.x264)**2) + 1 / sqrt((m.x81 - m.x85)**2
    + (m.x171 - m.x175)**2 + (m.x261 - m.x265)**2) + 1 / sqrt((m.x81 - m.x86)
    **2 + (m.x171 - m.x176)**2 + (m.x261 - m.x266)**2) + 1 / sqrt((m.x81 -
    m.x87)**2 + (m.x171 - m.x177)**2 + (m.x261 - m.x267)**2) + 1 / sqrt((m.x81
    - m.x88)**2 + (m.x171 - m.x178)**2 + (m.x261 - m.x268)**2) + 1 / sqrt((
    m.x81 - m.x89)**2 + (m.x171 - m.x179)**2 + (m.x261 - m.x269)**2) + 1 /
    sqrt((m.x81 - m.x90)**2 + (m.x171 - m.x180)**2 + (m.x261 - m.x270)**2) + 1
    / sqrt((m.x82 - m.x83)**2 + (m.x172 - m.x173)**2 + (m.x262 - m.x263)**2)
    + 1 / sqrt((m.x82 - m.x84)**2 + (m.x172 - m.x174)**2 + (m.x262 - m.x264)**
    2) + 1 / sqrt((m.x82 - m.x85)**2 + (m.x172 - m.x175)**2 + (m.x262 - m.x265)
    **2) + 1 / sqrt((m.x82 - m.x86)**2 + (m.x172 - m.x176)**2 + (m.x262 -
    m.x266)**2) + 1 / sqrt((m.x82 - m.x87)**2 + (m.x172 - m.x177)**2 + (m.x262
    - m.x267)**2) + 1 / sqrt((m.x82 - m.x88)**2 + (m.x172 - m.x178)**2 + (
    m.x262 - m.x268)**2) + 1 / sqrt((m.x82 - m.x89)**2 + (m.x172 - m.x179)**2
    + (m.x262 - m.x269)**2) + 1 / sqrt((m.x82 - m.x90)**2 + (m.x172 - m.x180)
    **2 + (m.x262 - m.x270)**2) + 1 / sqrt((m.x83 - m.x84)**2 + (m.x173 -
    m.x174)**2 + (m.x263 - m.x264)**2) + 1 / sqrt((m.x83 - m.x85)**2 + (m.x173
    - m.x175)**2 + (m.x263 - m.x265)**2) + 1 / sqrt((m.x83 - m.x86)**2 + (
    m.x173 - m.x176)**2 + (m.x263 - m.x266)**2) + 1 / sqrt((m.x83 - m.x87)**2
    + (m.x173 - m.x177)**2 + (m.x263 - m.x267)**2) + 1 / sqrt((m.x83 - m.x88)
    **2 + (m.x173 - m.x178)**2 + (m.x263 - m.x268)**2) + 1 / sqrt((m.x83 -
    m.x89)**2 + (m.x173 - m.x179)**2 + (m.x263 - m.x269)**2) + 1 / sqrt((m.x83
    - m.x90)**2 + (m.x173 - m.x180)**2 + (m.x263 - m.x270)**2) + 1 / sqrt((
    m.x84 - m.x85)**2 + (m.x174 - m.x175)**2 + (m.x264 - m.x265)**2) + 1 /
    sqrt((m.x84 - m.x86)**2 + (m.x174 - m.x176)**2 + (m.x264 - m.x266)**2) + 1
    / sqrt((m.x84 - m.x87)**2 + (m.x174 - m.x177)**2 + (m.x264 - m.x267)**2)
    + 1 / sqrt((m.x84 - m.x88)**2 + (m.x174 - m.x178)**2 + (m.x264 - m.x268)**
    2) + 1 / sqrt((m.x84 - m.x89)**2 + (m.x174 - m.x179)**2 + (m.x264 - m.x269)
    **2) + 1 / sqrt((m.x84 - m.x90)**2 + (m.x174 - m.x180)**2 + (m.x264 -
    m.x270)**2) + 1 / sqrt((m.x85 - m.x86)**2 + (m.x175 - m.x176)**2 + (m.x265
    - m.x266)**2) + 1 / sqrt((m.x85 - m.x87)**2 + (m.x175 - m.x177)**2 + (
    m.x265 - m.x267)**2) + 1 / sqrt((m.x85 - m.x88)**2 + (m.x175 - m.x178)**2
    + (m.x265 - m.x268)**2) + 1 / sqrt((m.x85 - m.x89)**2 + (m.x175 - m.x179)
    **2 + (m.x265 - m.x269)**2) + 1 / sqrt((m.x85 - m.x90)**2 + (m.x175 -
    m.x180)**2 + (m.x265 - m.x270)**2) + 1 / sqrt((m.x86 - m.x87)**2 + (m.x176
    - m.x177)**2 + (m.x266 - m.x267)**2) + 1 / sqrt((m.x86 - m.x88)**2 + (
    m.x176 - m.x178)**2 + (m.x266 - m.x268)**2) + 1 / sqrt((m.x86 - m.x89)**2
    + (m.x176 - m.x179)**2 + (m.x266 - m.x269)**2) + 1 / sqrt((m.x86 - m.x90)
    **2 + (m.x176 - m.x180)**2 + (m.x266 - m.x270)**2) + 1 / sqrt((m.x87 -
    m.x88)**2 + (m.x177 - m.x178)**2 + (m.x267 - m.x268)**2) + 1 / sqrt((m.x87
    - m.x89)**2 + (m.x177 - m.x179)**2 + (m.x267 - m.x269)**2) + 1 / sqrt((
    m.x87 - m.x90)**2 + (m.x177 - m.x180)**2 + (m.x267 - m.x270)**2) + 1 /
    sqrt((m.x88 - m.x89)**2 + (m.x178 - m.x179)**2 + (m.x268 - m.x269)**2) + 1
    / sqrt((m.x88 - m.x90)**2 + (m.x178 - m.x180)**2 + (m.x268 - m.x270)**2)
    + 1 / sqrt((m.x89 - m.x90)**2 + (m.x179 - m.x180)**2 + (m.x269 - m.x270)**
    2))

m.e1 = Constraint(expr= m.x1**2 + m.x91**2 + m.x181**2 == 1)
m.e2 = Constraint(expr= m.x2**2 + m.x92**2 + m.x182**2 == 1)
m.e3 = Constraint(expr= m.x3**2 + m.x93**2 + m.x183**2 == 1)
m.e4 = Constraint(expr= m.x4**2 + m.x94**2 + m.x184**2 == 1)
m.e5 = Constraint(expr= m.x5**2 + m.x95**2 + m.x185**2 == 1)
m.e6 = Constraint(expr= m.x6**2 + m.x96**2 + m.x186**2 == 1)
m.e7 = Constraint(expr= m.x7**2 + m.x97**2 + m.x187**2 == 1)
m.e8 = Constraint(expr= m.x8**2 + m.x98**2 + m.x188**2 == 1)
m.e9 = Constraint(expr= m.x9**2 + m.x99**2 + m.x189**2 == 1)
m.e10 = Constraint(expr= m.x10**2 + m.x100**2 + m.x190**2 == 1)
m.e11 = Constraint(expr= m.x11**2 + m.x101**2 + m.x191**2 == 1)
m.e12 = Constraint(expr= m.x12**2 + m.x102**2 + m.x192**2 == 1)
m.e13 = Constraint(expr= m.x13**2 + m.x103**2 + m.x193**2 == 1)
m.e14 = Constraint(expr= m.x14**2 + m.x104**2 + m.x194**2 == 1)
m.e15 = Constraint(expr= m.x15**2 + m.x105**2 + m.x195**2 == 1)
m.e16 = Constraint(expr= m.x16**2 + m.x106**2 + m.x196**2 == 1)
m.e17 = Constraint(expr= m.x17**2 + m.x107**2 + m.x197**2 == 1)
m.e18 = Constraint(expr= m.x18**2 + m.x108**2 + m.x198**2 == 1)
m.e19 = Constraint(expr= m.x19**2 + m.x109**2 + m.x199**2 == 1)
m.e20 = Constraint(expr= m.x20**2 + m.x110**2 + m.x200**2 == 1)
m.e21 = Constraint(expr= m.x21**2 + m.x111**2 + m.x201**2 == 1)
m.e22 = Constraint(expr= m.x22**2 + m.x112**2 + m.x202**2 == 1)
m.e23 = Constraint(expr= m.x23**2 + m.x113**2 + m.x203**2 == 1)
m.e24 = Constraint(expr= m.x24**2 + m.x114**2 + m.x204**2 == 1)
m.e25 = Constraint(expr= m.x25**2 + m.x115**2 + m.x205**2 == 1)
m.e26 = Constraint(expr= m.x26**2 + m.x116**2 + m.x206**2 == 1)
m.e27 = Constraint(expr= m.x27**2 + m.x117**2 + m.x207**2 == 1)
m.e28 = Constraint(expr= m.x28**2 + m.x118**2 + m.x208**2 == 1)
m.e29 = Constraint(expr= m.x29**2 + m.x119**2 + m.x209**2 == 1)
m.e30 = Constraint(expr= m.x30**2 + m.x120**2 + m.x210**2 == 1)
m.e31 = Constraint(expr= m.x31**2 + m.x121**2 + m.x211**2 == 1)
m.e32 = Constraint(expr= m.x32**2 + m.x122**2 + m.x212**2 == 1)
m.e33 = Constraint(expr= m.x33**2 + m.x123**2 + m.x213**2 == 1)
m.e34 = Constraint(expr= m.x34**2 + m.x124**2 + m.x214**2 == 1)
m.e35 = Constraint(expr= m.x35**2 + m.x125**2 + m.x215**2 == 1)
m.e36 = Constraint(expr= m.x36**2 + m.x126**2 + m.x216**2 == 1)
m.e37 = Constraint(expr= m.x37**2 + m.x127**2 + m.x217**2 == 1)
m.e38 = Constraint(expr= m.x38**2 + m.x128**2 + m.x218**2 == 1)
m.e39 = Constraint(expr= m.x39**2 + m.x129**2 + m.x219**2 == 1)
m.e40 = Constraint(expr= m.x40**2 + m.x130**2 + m.x220**2 == 1)
m.e41 = Constraint(expr= m.x41**2 + m.x131**2 + m.x221**2 == 1)
m.e42 = Constraint(expr= m.x42**2 + m.x132**2 + m.x222**2 == 1)
m.e43 = Constraint(expr= m.x43**2 + m.x133**2 + m.x223**2 == 1)
m.e44 = Constraint(expr= m.x44**2 + m.x134**2 + m.x224**2 == 1)
m.e45 = Constraint(expr= m.x45**2 + m.x135**2 + m.x225**2 == 1)
m.e46 = Constraint(expr= m.x46**2 + m.x136**2 + m.x226**2 == 1)
m.e47 = Constraint(expr= m.x47**2 + m.x137**2 + m.x227**2 == 1)
m.e48 = Constraint(expr= m.x48**2 + m.x138**2 + m.x228**2 == 1)
m.e49 = Constraint(expr= m.x49**2 + m.x139**2 + m.x229**2 == 1)
m.e50 = Constraint(expr= m.x50**2 + m.x140**2 + m.x230**2 == 1)
m.e51 = Constraint(expr= m.x51**2 + m.x141**2 + m.x231**2 == 1)
m.e52 = Constraint(expr= m.x52**2 + m.x142**2 + m.x232**2 == 1)
m.e53 = Constraint(expr= m.x53**2 + m.x143**2 + m.x233**2 == 1)
m.e54 = Constraint(expr= m.x54**2 + m.x144**2 + m.x234**2 == 1)
m.e55 = Constraint(expr= m.x55**2 + m.x145**2 + m.x235**2 == 1)
m.e56 = Constraint(expr= m.x56**2 + m.x146**2 + m.x236**2 == 1)
m.e57 = Constraint(expr= m.x57**2 + m.x147**2 + m.x237**2 == 1)
m.e58 = Constraint(expr= m.x58**2 + m.x148**2 + m.x238**2 == 1)
m.e59 = Constraint(expr= m.x59**2 + m.x149**2 + m.x239**2 == 1)
m.e60 = Constraint(expr= m.x60**2 + m.x150**2 + m.x240**2 == 1)
m.e61 = Constraint(expr= m.x61**2 + m.x151**2 + m.x241**2 == 1)
m.e62 = Constraint(expr= m.x62**2 + m.x152**2 + m.x242**2 == 1)
m.e63 = Constraint(expr= m.x63**2 + m.x153**2 + m.x243**2 == 1)
m.e64 = Constraint(expr= m.x64**2 + m.x154**2 + m.x244**2 == 1)
m.e65 = Constraint(expr= m.x65**2 + m.x155**2 + m.x245**2 == 1)
m.e66 = Constraint(expr= m.x66**2 + m.x156**2 + m.x246**2 == 1)
m.e67 = Constraint(expr= m.x67**2 + m.x157**2 + m.x247**2 == 1)
m.e68 = Constraint(expr= m.x68**2 + m.x158**2 + m.x248**2 == 1)
m.e69 = Constraint(expr= m.x69**2 + m.x159**2 + m.x249**2 == 1)
m.e70 = Constraint(expr= m.x70**2 + m.x160**2 + m.x250**2 == 1)
m.e71 = Constraint(expr= m.x71**2 + m.x161**2 + m.x251**2 == 1)
m.e72 = Constraint(expr= m.x72**2 + m.x162**2 + m.x252**2 == 1)
m.e73 = Constraint(expr= m.x73**2 + m.x163**2 + m.x253**2 == 1)
m.e74 = Constraint(expr= m.x74**2 + m.x164**2 + m.x254**2 == 1)
m.e75 = Constraint(expr= m.x75**2 + m.x165**2 + m.x255**2 == 1)
m.e76 = Constraint(expr= m.x76**2 + m.x166**2 + m.x256**2 == 1)
m.e77 = Constraint(expr= m.x77**2 + m.x167**2 + m.x257**2 == 1)
m.e78 = Constraint(expr= m.x78**2 + m.x168**2 + m.x258**2 == 1)
m.e79 = Constraint(expr= m.x79**2 + m.x169**2 + m.x259**2 == 1)
m.e80 = Constraint(expr= m.x80**2 + m.x170**2 + m.x260**2 == 1)
m.e81 = Constraint(expr= m.x81**2 + m.x171**2 + m.x261**2 == 1)
m.e82 = Constraint(expr= m.x82**2 + m.x172**2 + m.x262**2 == 1)
m.e83 = Constraint(expr= m.x83**2 + m.x173**2 + m.x263**2 == 1)
m.e84 = Constraint(expr= m.x84**2 + m.x174**2 + m.x264**2 == 1)
m.e85 = Constraint(expr= m.x85**2 + m.x175**2 + m.x265**2 == 1)
m.e86 = Constraint(expr= m.x86**2 + m.x176**2 + m.x266**2 == 1)
m.e87 = Constraint(expr= m.x87**2 + m.x177**2 + m.x267**2 == 1)
m.e88 = Constraint(expr= m.x88**2 + m.x178**2 + m.x268**2 == 1)
m.e89 = Constraint(expr= m.x89**2 + m.x179**2 + m.x269**2 == 1)
m.e90 = Constraint(expr= m.x90**2 + m.x180**2 + m.x270**2 == 1)
