# NLP written by GAMS Convert at 05/15/24 11:44:36
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       103      100        0        3        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#       306      306        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       600      600        0
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
m.x7 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x8 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x9 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x10 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x11 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x12 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x13 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x14 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x15 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x16 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x17 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x18 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x19 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x20 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x21 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x22 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x23 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x24 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x25 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x26 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x27 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x28 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x29 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x30 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x31 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x32 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x33 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x34 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x35 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x36 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x37 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x38 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x39 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x40 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x41 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x42 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x43 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x44 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x45 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x46 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x47 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x48 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x49 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x50 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x51 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x52 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x53 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x54 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x55 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x56 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x57 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x58 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x59 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x60 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x61 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x62 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x63 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x64 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x65 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x66 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x67 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x68 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x69 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x70 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x71 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x72 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x73 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x74 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x75 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x76 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x77 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x78 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x79 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x80 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x81 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x82 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x83 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x84 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x85 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x86 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x87 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x88 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x89 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x90 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x91 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x92 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x93 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x94 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x95 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x96 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x97 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x98 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x99 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x100 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x101 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x102 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x103 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x104 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x105 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x106 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x107 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x108 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x109 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x110 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x111 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x112 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x113 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x114 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x115 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x116 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x117 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x118 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x119 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x120 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x121 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x122 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x123 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x124 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x125 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x126 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x127 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x128 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x129 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x130 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x131 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x132 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x133 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x134 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x135 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x136 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x137 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x138 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x139 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x140 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x141 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x142 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x143 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x144 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x145 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x146 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x147 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x148 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x149 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x150 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x151 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x152 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x153 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x154 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x155 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x156 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x157 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x158 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x159 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x160 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x161 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x162 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x163 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x164 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x165 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x166 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x167 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x168 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x169 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x170 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x171 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x172 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x173 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x174 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x175 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x176 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x177 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x178 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x179 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x180 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x181 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x182 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x183 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x184 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x185 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x186 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x187 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x188 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x189 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x190 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x191 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x192 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x193 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x194 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x195 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x196 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x197 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x198 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x199 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x200 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x201 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x202 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x203 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x204 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x205 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x206 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x207 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x208 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x209 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x210 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x211 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x212 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x213 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x214 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x215 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x216 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x217 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x218 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x219 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x220 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x221 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x222 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x223 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x224 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x225 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x226 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x227 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x228 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x229 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x230 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x231 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x232 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x233 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x234 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x235 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x236 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x237 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x238 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x239 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x240 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x241 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x242 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x243 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x244 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x245 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x246 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x247 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x248 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x249 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x250 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x251 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x252 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x253 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x254 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x255 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x256 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x257 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x258 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x259 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x260 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x261 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x262 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x263 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x264 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x265 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x266 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x267 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x268 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x269 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x270 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x271 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x272 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x273 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x274 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x275 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x276 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x277 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x278 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x279 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x280 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x281 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x282 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x283 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x284 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x285 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x286 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x287 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x288 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x289 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x290 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x291 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x292 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x293 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x294 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x295 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x296 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x297 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x298 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x299 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x300 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x301 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x302 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x303 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x304 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x305 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x306 = Var(within=Reals, bounds=(0,None), initialize=0)

m.obj = Objective(sense=minimize, expr= m.x7 * ((-0.9790501200727744 + m.x1)**2
    + (-0.6311424951878402 + m.x4)**2) + m.x8 * ((-0.45629827629184827 + m.x1)
    **2 + (-0.06672245148451761 + m.x4)**2) + m.x9 * ((-0.7188470341002364 +
    m.x1)**2 + (-0.02813370989019326 + m.x4)**2) + m.x10 * ((
    -0.7348862425853395 + m.x1)**2 + (-0.8816599278452203 + m.x4)**2) + m.x11
    * ((-0.21490166849706338 + m.x1)**2 + (-0.6269013861862501 + m.x4)**2) +
    m.x12 * ((-0.07803796911512406 + m.x1)**2 + (-0.16286095537542633 + m.x4)**
    2) + m.x13 * ((-0.6027432362671394 + m.x1)**2 + (-0.42873962092903517 +
    m.x4)**2) + m.x14 * ((-0.12191950272268226 + m.x1)**2 + (
    -0.2890755666151287 + m.x4)**2) + m.x15 * ((-0.382226634481309 + m.x1)**2
    + (-0.8692874521904679 + m.x4)**2) + m.x16 * ((-0.8897028218070439 + m.x1)
    **2 + (-0.28624094722515714 + m.x4)**2) + m.x17 * ((-0.8721502920634506 +
    m.x1)**2 + (-0.7244247415495613 + m.x4)**2) + m.x18 * ((-0.1186890489541742
    + m.x1)**2 + (-0.7437850500651989 + m.x4)**2) + m.x19 * ((
    -0.08223395893075858 + m.x1)**2 + (-0.31875884096460017 + m.x4)**2) + m.x20
    * ((-0.22248607563414302 + m.x1)**2 + (-0.2521011029699466 + m.x4)**2) +
    m.x21 * ((-0.8280911145578295 + m.x1)**2 + (-0.521112501873431 + m.x4)**2)
    + m.x22 * ((-0.02472447636767583 + m.x1)**2 + (-0.3997225002105538 + m.x4)
    **2) + m.x23 * ((-0.2251828459038958 + m.x1)**2 + (-0.5939809266576113 +
    m.x4)**2) + m.x24 * ((-0.10723676302623708 + m.x1)**2 + (
    -0.32815695404043954 + m.x4)**2) + m.x25 * ((-0.12763824766271537 + m.x1)**
    2 + (-0.7945040151126441 + m.x4)**2) + m.x26 * ((-0.5234249852126434 + m.x1)
    **2 + (-0.42030230269801994 + m.x4)**2) + m.x27 * ((-0.18343173523148326 +
    m.x1)**2 + (-0.136143099207385 + m.x4)**2) + m.x28 * ((-0.40944334015947625
    + m.x1)**2 + (-0.774531308143275 + m.x4)**2) + m.x29 * ((
    -0.7331857650038027 + m.x1)**2 + (-0.8950296042756412 + m.x4)**2) + m.x30
    * ((-0.7229955321011505 + m.x1)**2 + (-0.6811637100991619 + m.x4)**2) +
    m.x31 * ((-0.41503758152257597 + m.x1)**2 + (-0.5465191428386663 + m.x4)**2)
    + m.x32 * ((-0.7861348290536645 + m.x1)**2 + (-0.87178894698042 + m.x4)**2)
    + m.x33 * ((-0.5725075138461647 + m.x1)**2 + (-0.9337948530254415 + m.x4)
    **2) + m.x34 * ((-0.8269601510284041 + m.x1)**2 + (-0.009262756401185124 +
    m.x4)**2) + m.x35 * ((-0.2488818696593572 + m.x1)**2 + (-0.4876950675248043
    + m.x4)**2) + m.x36 * ((-0.36912357958085673 + m.x1)**2 + (
    -0.018982468776048256 + m.x4)**2) + m.x37 * ((-0.5803349928449376 + m.x1)**
    2 + (-0.3335241239631539 + m.x4)**2) + m.x38 * ((-0.9458939112226394 + m.x1)
    **2 + (-0.24183404147594545 + m.x4)**2) + m.x39 * ((-0.618339929803488 +
    m.x1)**2 + (-0.4613823719890262 + m.x4)**2) + m.x40 * ((-0.4747024910574612
    + m.x1)**2 + (-0.677298801963296 + m.x4)**2) + m.x41 * ((
    -0.25095823937637995 + m.x1)**2 + (-0.8608494707743931 + m.x4)**2) + m.x42
    * ((-0.2813337214794214 + m.x1)**2 + (-0.260828760842044 + m.x4)**2) +
    m.x43 * ((-0.21578669367558911 + m.x1)**2 + (-0.011735861364977063 + m.x4)
    **2) + m.x44 * ((-0.9863645026702189 + m.x1)**2 + (-0.9990458234862235 +
    m.x4)**2) + m.x45 * ((-0.8865853309878791 + m.x1)**2 + (-0.7821203148917139
    + m.x4)**2) + m.x46 * ((-0.8945620392234958 + m.x1)**2 + (
    -0.5503418933063282 + m.x4)**2) + m.x47 * ((-0.5285688951098176 + m.x1)**2
    + (-0.11239191602793763 + m.x4)**2) + m.x48 * ((-0.708384487952824 + m.x1)
    **2 + (-0.052377433607805 + m.x4)**2) + m.x49 * ((-0.29648914964070017 +
    m.x1)**2 + (-0.9341294850788631 + m.x4)**2) + m.x50 * ((
    -0.48157049590943335 + m.x1)**2 + (-0.5293556030905174 + m.x4)**2) + m.x51
    * ((-0.14554146029922255 + m.x1)**2 + (-0.8600456625304761 + m.x4)**2) +
    m.x52 * ((-0.420140098875878 + m.x1)**2 + (-0.7836717817794422 + m.x4)**2)
    + m.x53 * ((-0.252703353163125 + m.x1)**2 + (-0.7511054492094982 + m.x4)**
    2) + m.x54 * ((-0.09997671456057478 + m.x1)**2 + (-0.8052510810051834 +
    m.x4)**2) + m.x55 * ((-0.9194440793102199 + m.x1)**2 + (-0.2533792755981428
    + m.x4)**2) + m.x56 * ((-0.09668337434887231 + m.x1)**2 + (
    -0.24611947874178752 + m.x4)**2) + m.x57 * ((-0.8129312296053264 + m.x1)**2
    + (-0.43371140947157627 + m.x4)**2) + m.x58 * ((-0.69957905129295 + m.x1)
    **2 + (-0.7676310918513006 + m.x4)**2) + m.x59 * ((-0.0900544025434653 +
    m.x1)**2 + (-0.7942401639657729 + m.x4)**2) + m.x60 * ((
    -0.48515271892966294 + m.x1)**2 + (-0.7574483929568191 + m.x4)**2) + m.x61
    * ((-0.9958643028455554 + m.x1)**2 + (-0.5795352889383328 + m.x4)**2) +
    m.x62 * ((-0.9868623533325966 + m.x1)**2 + (-0.4767439909083834 + m.x4)**2)
    + m.x63 * ((-0.5633005482415795 + m.x1)**2 + (-0.19425040789890158 + m.x4)
    **2) + m.x64 * ((-0.7718094743437608 + m.x1)**2 + (-0.6666443342600646 +
    m.x4)**2) + m.x65 * ((-0.7086747540781035 + m.x1)**2 + (-0.6536254702356696
    + m.x4)**2) + m.x66 * ((-0.29177285745744364 + m.x1)**2 + (
    -0.5144679134132856 + m.x4)**2) + m.x67 * ((-0.5499369537631748 + m.x1)**2
    + (-0.726777937936861 + m.x4)**2) + m.x68 * ((-0.596939821696328 + m.x1)**
    2 + (-0.9792846384007238 + m.x4)**2) + m.x69 * ((-0.39405641988972406 +
    m.x1)**2 + (-0.9435855472981566 + m.x4)**2) + m.x70 * ((-0.8189990872832278
    + m.x1)**2 + (-0.10714435097363662 + m.x4)**2) + m.x71 * ((
    -0.44421356366434817 + m.x1)**2 + (-0.2874586706743091 + m.x4)**2) + m.x72
    * ((-0.7494891352136963 + m.x1)**2 + (-0.6129812821515095 + m.x4)**2) +
    m.x73 * ((-0.06468637419158274 + m.x1)**2 + (-0.6897257530243619 + m.x4)**2)
    + m.x74 * ((-0.4448860941734385 + m.x1)**2 + (-0.28449710521756644 + m.x4)
    **2) + m.x75 * ((-0.04443656150056341 + m.x1)**2 + (-0.9307717790464919 +
    m.x4)**2) + m.x76 * ((-0.6468354932652288 + m.x1)**2 + (-0.4608658507473642
    + m.x4)**2) + m.x77 * ((-0.8726582006369804 + m.x1)**2 + (
    -0.7652199544751623 + m.x4)**2) + m.x78 * ((-0.5434607583258384 + m.x1)**2
    + (-0.052316469397973964 + m.x4)**2) + m.x79 * ((-0.5653919967842793 +
    m.x1)**2 + (-0.27910238121665565 + m.x4)**2) + m.x80 * ((
    -0.6224904598210145 + m.x1)**2 + (-0.02247631649979287 + m.x4)**2) + m.x81
    * ((-0.229051149892618 + m.x1)**2 + (-0.7910496903784138 + m.x4)**2) +
    m.x82 * ((-0.38625690455774275 + m.x1)**2 + (-0.5219004509746287 + m.x4)**2)
    + m.x83 * ((-0.5785186297030117 + m.x1)**2 + (-0.9528110034877589 + m.x4)
    **2) + m.x84 * ((-0.6462821339816298 + m.x1)**2 + (-0.6067764925944034 +
    m.x4)**2) + m.x85 * ((-0.38006243875752277 + m.x1)**2 + (
    -0.32501439221768036 + m.x4)**2) + m.x86 * ((-0.4773778129689302 + m.x1)**2
    + (-0.3565933083195064 + m.x4)**2) + m.x87 * ((-0.33078861302885243 + m.x1)
    **2 + (-0.37500196195238944 + m.x4)**2) + m.x88 * ((-0.5542981262906839 +
    m.x1)**2 + (-0.19803228322354316 + m.x4)**2) + m.x89 * ((
    -0.6759728791955966 + m.x1)**2 + (-0.10790031453323568 + m.x4)**2) + m.x90
    * ((-0.32776733692609294 + m.x1)**2 + (-0.649698771312504 + m.x4)**2) +
    m.x91 * ((-0.6849969003224811 + m.x1)**2 + (-0.31383818211836345 + m.x4)**2)
    + m.x92 * ((-0.8489741551279321 + m.x1)**2 + (-0.4536251040305358 + m.x4)
    **2) + m.x93 * ((-0.5364380411417772 + m.x1)**2 + (-0.7091773891838592 +
    m.x4)**2) + m.x94 * ((-0.9803725216985771 + m.x1)**2 + (-0.2741220008365026
    + m.x4)**2) + m.x95 * ((-0.30949991491899753 + m.x1)**2 + (
    -0.4397462597339806 + m.x4)**2) + m.x96 * ((-0.9195632575532574 + m.x1)**2
    + (-0.3235817691663315 + m.x4)**2) + m.x97 * ((-0.18190096518085497 + m.x1)
    **2 + (-0.32411302414330956 + m.x4)**2) + m.x98 * ((-0.36343488491763387 +
    m.x1)**2 + (-0.6663092097253003 + m.x4)**2) + m.x99 * ((-0.8168528198966378
    + m.x1)**2 + (-0.09851383090888444 + m.x4)**2) + m.x100 * ((
    -0.0325822956804418 + m.x1)**2 + (-0.3995952149437163 + m.x4)**2) + m.x101
    * ((-0.6144908043611289 + m.x1)**2 + (-0.10979848578730689 + m.x4)**2) +
    m.x102 * ((-0.8713165943427151 + m.x1)**2 + (-0.6699384226962937 + m.x4)**2)
    + m.x103 * ((-0.9439947803244484 + m.x1)**2 + (-0.29790397105454614 + m.x4)
    **2) + m.x104 * ((-0.68218233799177 + m.x1)**2 + (-0.9650579074996485 +
    m.x4)**2) + m.x105 * ((-0.3455598885840183 + m.x1)**2 + (
    -0.4827230523144219 + m.x4)**2) + m.x106 * ((-0.3322933066434728 + m.x1)**2
    + (-0.6618767361640094 + m.x4)**2) + m.x107 * ((-0.9790501200727744 + m.x2)
    **2 + (-0.6311424951878402 + m.x5)**2) + m.x108 * ((-0.45629827629184827 +
    m.x2)**2 + (-0.06672245148451761 + m.x5)**2) + m.x109 * ((
    -0.7188470341002364 + m.x2)**2 + (-0.02813370989019326 + m.x5)**2) + m.x110
    * ((-0.7348862425853395 + m.x2)**2 + (-0.8816599278452203 + m.x5)**2) +
    m.x111 * ((-0.21490166849706338 + m.x2)**2 + (-0.6269013861862501 + m.x5)**
    2) + m.x112 * ((-0.07803796911512406 + m.x2)**2 + (-0.16286095537542633 +
    m.x5)**2) + m.x113 * ((-0.6027432362671394 + m.x2)**2 + (
    -0.42873962092903517 + m.x5)**2) + m.x114 * ((-0.12191950272268226 + m.x2)
    **2 + (-0.2890755666151287 + m.x5)**2) + m.x115 * ((-0.382226634481309 +
    m.x2)**2 + (-0.8692874521904679 + m.x5)**2) + m.x116 * ((
    -0.8897028218070439 + m.x2)**2 + (-0.28624094722515714 + m.x5)**2) + m.x117
    * ((-0.8721502920634506 + m.x2)**2 + (-0.7244247415495613 + m.x5)**2) +
    m.x118 * ((-0.1186890489541742 + m.x2)**2 + (-0.7437850500651989 + m.x5)**2)
    + m.x119 * ((-0.08223395893075858 + m.x2)**2 + (-0.31875884096460017 +
    m.x5)**2) + m.x120 * ((-0.22248607563414302 + m.x2)**2 + (
    -0.2521011029699466 + m.x5)**2) + m.x121 * ((-0.8280911145578295 + m.x2)**2
    + (-0.521112501873431 + m.x5)**2) + m.x122 * ((-0.02472447636767583 + m.x2)
    **2 + (-0.3997225002105538 + m.x5)**2) + m.x123 * ((-0.2251828459038958 +
    m.x2)**2 + (-0.5939809266576113 + m.x5)**2) + m.x124 * ((
    -0.10723676302623708 + m.x2)**2 + (-0.32815695404043954 + m.x5)**2) +
    m.x125 * ((-0.12763824766271537 + m.x2)**2 + (-0.7945040151126441 + m.x5)**
    2) + m.x126 * ((-0.5234249852126434 + m.x2)**2 + (-0.42030230269801994 +
    m.x5)**2) + m.x127 * ((-0.18343173523148326 + m.x2)**2 + (
    -0.136143099207385 + m.x5)**2) + m.x128 * ((-0.40944334015947625 + m.x2)**2
    + (-0.774531308143275 + m.x5)**2) + m.x129 * ((-0.7331857650038027 + m.x2)
    **2 + (-0.8950296042756412 + m.x5)**2) + m.x130 * ((-0.7229955321011505 +
    m.x2)**2 + (-0.6811637100991619 + m.x5)**2) + m.x131 * ((
    -0.41503758152257597 + m.x2)**2 + (-0.5465191428386663 + m.x5)**2) + m.x132
    * ((-0.7861348290536645 + m.x2)**2 + (-0.87178894698042 + m.x5)**2) +
    m.x133 * ((-0.5725075138461647 + m.x2)**2 + (-0.9337948530254415 + m.x5)**2)
    + m.x134 * ((-0.8269601510284041 + m.x2)**2 + (-0.009262756401185124 +
    m.x5)**2) + m.x135 * ((-0.2488818696593572 + m.x2)**2 + (
    -0.4876950675248043 + m.x5)**2) + m.x136 * ((-0.36912357958085673 + m.x2)**
    2 + (-0.018982468776048256 + m.x5)**2) + m.x137 * ((-0.5803349928449376 +
    m.x2)**2 + (-0.3335241239631539 + m.x5)**2) + m.x138 * ((
    -0.9458939112226394 + m.x2)**2 + (-0.24183404147594545 + m.x5)**2) + m.x139
    * ((-0.618339929803488 + m.x2)**2 + (-0.4613823719890262 + m.x5)**2) +
    m.x140 * ((-0.4747024910574612 + m.x2)**2 + (-0.677298801963296 + m.x5)**2)
    + m.x141 * ((-0.25095823937637995 + m.x2)**2 + (-0.8608494707743931 + m.x5)
    **2) + m.x142 * ((-0.2813337214794214 + m.x2)**2 + (-0.260828760842044 +
    m.x5)**2) + m.x143 * ((-0.21578669367558911 + m.x2)**2 + (
    -0.011735861364977063 + m.x5)**2) + m.x144 * ((-0.9863645026702189 + m.x2)
    **2 + (-0.9990458234862235 + m.x5)**2) + m.x145 * ((-0.8865853309878791 +
    m.x2)**2 + (-0.7821203148917139 + m.x5)**2) + m.x146 * ((
    -0.8945620392234958 + m.x2)**2 + (-0.5503418933063282 + m.x5)**2) + m.x147
    * ((-0.5285688951098176 + m.x2)**2 + (-0.11239191602793763 + m.x5)**2) +
    m.x148 * ((-0.708384487952824 + m.x2)**2 + (-0.052377433607805 + m.x5)**2)
    + m.x149 * ((-0.29648914964070017 + m.x2)**2 + (-0.9341294850788631 + m.x5)
    **2) + m.x150 * ((-0.48157049590943335 + m.x2)**2 + (-0.5293556030905174 +
    m.x5)**2) + m.x151 * ((-0.14554146029922255 + m.x2)**2 + (
    -0.8600456625304761 + m.x5)**2) + m.x152 * ((-0.420140098875878 + m.x2)**2
    + (-0.7836717817794422 + m.x5)**2) + m.x153 * ((-0.252703353163125 + m.x2)
    **2 + (-0.7511054492094982 + m.x5)**2) + m.x154 * ((-0.09997671456057478 +
    m.x2)**2 + (-0.8052510810051834 + m.x5)**2) + m.x155 * ((
    -0.9194440793102199 + m.x2)**2 + (-0.2533792755981428 + m.x5)**2) + m.x156
    * ((-0.09668337434887231 + m.x2)**2 + (-0.24611947874178752 + m.x5)**2) +
    m.x157 * ((-0.8129312296053264 + m.x2)**2 + (-0.43371140947157627 + m.x5)**
    2) + m.x158 * ((-0.69957905129295 + m.x2)**2 + (-0.7676310918513006 + m.x5)
    **2) + m.x159 * ((-0.0900544025434653 + m.x2)**2 + (-0.7942401639657729 +
    m.x5)**2) + m.x160 * ((-0.48515271892966294 + m.x2)**2 + (
    -0.7574483929568191 + m.x5)**2) + m.x161 * ((-0.9958643028455554 + m.x2)**2
    + (-0.5795352889383328 + m.x5)**2) + m.x162 * ((-0.9868623533325966 + m.x2)
    **2 + (-0.4767439909083834 + m.x5)**2) + m.x163 * ((-0.5633005482415795 +
    m.x2)**2 + (-0.19425040789890158 + m.x5)**2) + m.x164 * ((
    -0.7718094743437608 + m.x2)**2 + (-0.6666443342600646 + m.x5)**2) + m.x165
    * ((-0.7086747540781035 + m.x2)**2 + (-0.6536254702356696 + m.x5)**2) +
    m.x166 * ((-0.29177285745744364 + m.x2)**2 + (-0.5144679134132856 + m.x5)**
    2) + m.x167 * ((-0.5499369537631748 + m.x2)**2 + (-0.726777937936861 + m.x5)
    **2) + m.x168 * ((-0.596939821696328 + m.x2)**2 + (-0.9792846384007238 +
    m.x5)**2) + m.x169 * ((-0.39405641988972406 + m.x2)**2 + (
    -0.9435855472981566 + m.x5)**2) + m.x170 * ((-0.8189990872832278 + m.x2)**2
    + (-0.10714435097363662 + m.x5)**2) + m.x171 * ((-0.44421356366434817 +
    m.x2)**2 + (-0.2874586706743091 + m.x5)**2) + m.x172 * ((
    -0.7494891352136963 + m.x2)**2 + (-0.6129812821515095 + m.x5)**2) + m.x173
    * ((-0.06468637419158274 + m.x2)**2 + (-0.6897257530243619 + m.x5)**2) +
    m.x174 * ((-0.4448860941734385 + m.x2)**2 + (-0.28449710521756644 + m.x5)**
    2) + m.x175 * ((-0.04443656150056341 + m.x2)**2 + (-0.9307717790464919 +
    m.x5)**2) + m.x176 * ((-0.6468354932652288 + m.x2)**2 + (
    -0.4608658507473642 + m.x5)**2) + m.x177 * ((-0.8726582006369804 + m.x2)**2
    + (-0.7652199544751623 + m.x5)**2) + m.x178 * ((-0.5434607583258384 + m.x2)
    **2 + (-0.052316469397973964 + m.x5)**2) + m.x179 * ((-0.5653919967842793
    + m.x2)**2 + (-0.27910238121665565 + m.x5)**2) + m.x180 * ((
    -0.6224904598210145 + m.x2)**2 + (-0.02247631649979287 + m.x5)**2) + m.x181
    * ((-0.229051149892618 + m.x2)**2 + (-0.7910496903784138 + m.x5)**2) +
    m.x182 * ((-0.38625690455774275 + m.x2)**2 + (-0.5219004509746287 + m.x5)**
    2) + m.x183 * ((-0.5785186297030117 + m.x2)**2 + (-0.9528110034877589 +
    m.x5)**2) + m.x184 * ((-0.6462821339816298 + m.x2)**2 + (
    -0.6067764925944034 + m.x5)**2) + m.x185 * ((-0.38006243875752277 + m.x2)**
    2 + (-0.32501439221768036 + m.x5)**2) + m.x186 * ((-0.4773778129689302 +
    m.x2)**2 + (-0.3565933083195064 + m.x5)**2) + m.x187 * ((
    -0.33078861302885243 + m.x2)**2 + (-0.37500196195238944 + m.x5)**2) +
    m.x188 * ((-0.5542981262906839 + m.x2)**2 + (-0.19803228322354316 + m.x5)**
    2) + m.x189 * ((-0.6759728791955966 + m.x2)**2 + (-0.10790031453323568 +
    m.x5)**2) + m.x190 * ((-0.32776733692609294 + m.x2)**2 + (
    -0.649698771312504 + m.x5)**2) + m.x191 * ((-0.6849969003224811 + m.x2)**2
    + (-0.31383818211836345 + m.x5)**2) + m.x192 * ((-0.8489741551279321 +
    m.x2)**2 + (-0.4536251040305358 + m.x5)**2) + m.x193 * ((
    -0.5364380411417772 + m.x2)**2 + (-0.7091773891838592 + m.x5)**2) + m.x194
    * ((-0.9803725216985771 + m.x2)**2 + (-0.2741220008365026 + m.x5)**2) +
    m.x195 * ((-0.30949991491899753 + m.x2)**2 + (-0.4397462597339806 + m.x5)**
    2) + m.x196 * ((-0.9195632575532574 + m.x2)**2 + (-0.3235817691663315 +
    m.x5)**2) + m.x197 * ((-0.18190096518085497 + m.x2)**2 + (
    -0.32411302414330956 + m.x5)**2) + m.x198 * ((-0.36343488491763387 + m.x2)
    **2 + (-0.6663092097253003 + m.x5)**2) + m.x199 * ((-0.8168528198966378 +
    m.x2)**2 + (-0.09851383090888444 + m.x5)**2) + m.x200 * ((
    -0.0325822956804418 + m.x2)**2 + (-0.3995952149437163 + m.x5)**2) + m.x201
    * ((-0.6144908043611289 + m.x2)**2 + (-0.10979848578730689 + m.x5)**2) +
    m.x202 * ((-0.8713165943427151 + m.x2)**2 + (-0.6699384226962937 + m.x5)**2)
    + m.x203 * ((-0.9439947803244484 + m.x2)**2 + (-0.29790397105454614 + m.x5)
    **2) + m.x204 * ((-0.68218233799177 + m.x2)**2 + (-0.9650579074996485 +
    m.x5)**2) + m.x205 * ((-0.3455598885840183 + m.x2)**2 + (
    -0.4827230523144219 + m.x5)**2) + m.x206 * ((-0.3322933066434728 + m.x2)**2
    + (-0.6618767361640094 + m.x5)**2) + m.x207 * ((-0.9790501200727744 + m.x3)
    **2 + (-0.6311424951878402 + m.x6)**2) + m.x208 * ((-0.45629827629184827 +
    m.x3)**2 + (-0.06672245148451761 + m.x6)**2) + m.x209 * ((
    -0.7188470341002364 + m.x3)**2 + (-0.02813370989019326 + m.x6)**2) + m.x210
    * ((-0.7348862425853395 + m.x3)**2 + (-0.8816599278452203 + m.x6)**2) +
    m.x211 * ((-0.21490166849706338 + m.x3)**2 + (-0.6269013861862501 + m.x6)**
    2) + m.x212 * ((-0.07803796911512406 + m.x3)**2 + (-0.16286095537542633 +
    m.x6)**2) + m.x213 * ((-0.6027432362671394 + m.x3)**2 + (
    -0.42873962092903517 + m.x6)**2) + m.x214 * ((-0.12191950272268226 + m.x3)
    **2 + (-0.2890755666151287 + m.x6)**2) + m.x215 * ((-0.382226634481309 +
    m.x3)**2 + (-0.8692874521904679 + m.x6)**2) + m.x216 * ((
    -0.8897028218070439 + m.x3)**2 + (-0.28624094722515714 + m.x6)**2) + m.x217
    * ((-0.8721502920634506 + m.x3)**2 + (-0.7244247415495613 + m.x6)**2) +
    m.x218 * ((-0.1186890489541742 + m.x3)**2 + (-0.7437850500651989 + m.x6)**2)
    + m.x219 * ((-0.08223395893075858 + m.x3)**2 + (-0.31875884096460017 +
    m.x6)**2) + m.x220 * ((-0.22248607563414302 + m.x3)**2 + (
    -0.2521011029699466 + m.x6)**2) + m.x221 * ((-0.8280911145578295 + m.x3)**2
    + (-0.521112501873431 + m.x6)**2) + m.x222 * ((-0.02472447636767583 + m.x3)
    **2 + (-0.3997225002105538 + m.x6)**2) + m.x223 * ((-0.2251828459038958 +
    m.x3)**2 + (-0.5939809266576113 + m.x6)**2) + m.x224 * ((
    -0.10723676302623708 + m.x3)**2 + (-0.32815695404043954 + m.x6)**2) +
    m.x225 * ((-0.12763824766271537 + m.x3)**2 + (-0.7945040151126441 + m.x6)**
    2) + m.x226 * ((-0.5234249852126434 + m.x3)**2 + (-0.42030230269801994 +
    m.x6)**2) + m.x227 * ((-0.18343173523148326 + m.x3)**2 + (
    -0.136143099207385 + m.x6)**2) + m.x228 * ((-0.40944334015947625 + m.x3)**2
    + (-0.774531308143275 + m.x6)**2) + m.x229 * ((-0.7331857650038027 + m.x3)
    **2 + (-0.8950296042756412 + m.x6)**2) + m.x230 * ((-0.7229955321011505 +
    m.x3)**2 + (-0.6811637100991619 + m.x6)**2) + m.x231 * ((
    -0.41503758152257597 + m.x3)**2 + (-0.5465191428386663 + m.x6)**2) + m.x232
    * ((-0.7861348290536645 + m.x3)**2 + (-0.87178894698042 + m.x6)**2) +
    m.x233 * ((-0.5725075138461647 + m.x3)**2 + (-0.9337948530254415 + m.x6)**2)
    + m.x234 * ((-0.8269601510284041 + m.x3)**2 + (-0.009262756401185124 +
    m.x6)**2) + m.x235 * ((-0.2488818696593572 + m.x3)**2 + (
    -0.4876950675248043 + m.x6)**2) + m.x236 * ((-0.36912357958085673 + m.x3)**
    2 + (-0.018982468776048256 + m.x6)**2) + m.x237 * ((-0.5803349928449376 +
    m.x3)**2 + (-0.3335241239631539 + m.x6)**2) + m.x238 * ((
    -0.9458939112226394 + m.x3)**2 + (-0.24183404147594545 + m.x6)**2) + m.x239
    * ((-0.618339929803488 + m.x3)**2 + (-0.4613823719890262 + m.x6)**2) +
    m.x240 * ((-0.4747024910574612 + m.x3)**2 + (-0.677298801963296 + m.x6)**2)
    + m.x241 * ((-0.25095823937637995 + m.x3)**2 + (-0.8608494707743931 + m.x6)
    **2) + m.x242 * ((-0.2813337214794214 + m.x3)**2 + (-0.260828760842044 +
    m.x6)**2) + m.x243 * ((-0.21578669367558911 + m.x3)**2 + (
    -0.011735861364977063 + m.x6)**2) + m.x244 * ((-0.9863645026702189 + m.x3)
    **2 + (-0.9990458234862235 + m.x6)**2) + m.x245 * ((-0.8865853309878791 +
    m.x3)**2 + (-0.7821203148917139 + m.x6)**2) + m.x246 * ((
    -0.8945620392234958 + m.x3)**2 + (-0.5503418933063282 + m.x6)**2) + m.x247
    * ((-0.5285688951098176 + m.x3)**2 + (-0.11239191602793763 + m.x6)**2) +
    m.x248 * ((-0.708384487952824 + m.x3)**2 + (-0.052377433607805 + m.x6)**2)
    + m.x249 * ((-0.29648914964070017 + m.x3)**2 + (-0.9341294850788631 + m.x6)
    **2) + m.x250 * ((-0.48157049590943335 + m.x3)**2 + (-0.5293556030905174 +
    m.x6)**2) + m.x251 * ((-0.14554146029922255 + m.x3)**2 + (
    -0.8600456625304761 + m.x6)**2) + m.x252 * ((-0.420140098875878 + m.x3)**2
    + (-0.7836717817794422 + m.x6)**2) + m.x253 * ((-0.252703353163125 + m.x3)
    **2 + (-0.7511054492094982 + m.x6)**2) + m.x254 * ((-0.09997671456057478 +
    m.x3)**2 + (-0.8052510810051834 + m.x6)**2) + m.x255 * ((
    -0.9194440793102199 + m.x3)**2 + (-0.2533792755981428 + m.x6)**2) + m.x256
    * ((-0.09668337434887231 + m.x3)**2 + (-0.24611947874178752 + m.x6)**2) +
    m.x257 * ((-0.8129312296053264 + m.x3)**2 + (-0.43371140947157627 + m.x6)**
    2) + m.x258 * ((-0.69957905129295 + m.x3)**2 + (-0.7676310918513006 + m.x6)
    **2) + m.x259 * ((-0.0900544025434653 + m.x3)**2 + (-0.7942401639657729 +
    m.x6)**2) + m.x260 * ((-0.48515271892966294 + m.x3)**2 + (
    -0.7574483929568191 + m.x6)**2) + m.x261 * ((-0.9958643028455554 + m.x3)**2
    + (-0.5795352889383328 + m.x6)**2) + m.x262 * ((-0.9868623533325966 + m.x3)
    **2 + (-0.4767439909083834 + m.x6)**2) + m.x263 * ((-0.5633005482415795 +
    m.x3)**2 + (-0.19425040789890158 + m.x6)**2) + m.x264 * ((
    -0.7718094743437608 + m.x3)**2 + (-0.6666443342600646 + m.x6)**2) + m.x265
    * ((-0.7086747540781035 + m.x3)**2 + (-0.6536254702356696 + m.x6)**2) +
    m.x266 * ((-0.29177285745744364 + m.x3)**2 + (-0.5144679134132856 + m.x6)**
    2) + m.x267 * ((-0.5499369537631748 + m.x3)**2 + (-0.726777937936861 + m.x6)
    **2) + m.x268 * ((-0.596939821696328 + m.x3)**2 + (-0.9792846384007238 +
    m.x6)**2) + m.x269 * ((-0.39405641988972406 + m.x3)**2 + (
    -0.9435855472981566 + m.x6)**2) + m.x270 * ((-0.8189990872832278 + m.x3)**2
    + (-0.10714435097363662 + m.x6)**2) + m.x271 * ((-0.44421356366434817 +
    m.x3)**2 + (-0.2874586706743091 + m.x6)**2) + m.x272 * ((
    -0.7494891352136963 + m.x3)**2 + (-0.6129812821515095 + m.x6)**2) + m.x273
    * ((-0.06468637419158274 + m.x3)**2 + (-0.6897257530243619 + m.x6)**2) +
    m.x274 * ((-0.4448860941734385 + m.x3)**2 + (-0.28449710521756644 + m.x6)**
    2) + m.x275 * ((-0.04443656150056341 + m.x3)**2 + (-0.9307717790464919 +
    m.x6)**2) + m.x276 * ((-0.6468354932652288 + m.x3)**2 + (
    -0.4608658507473642 + m.x6)**2) + m.x277 * ((-0.8726582006369804 + m.x3)**2
    + (-0.7652199544751623 + m.x6)**2) + m.x278 * ((-0.5434607583258384 + m.x3)
    **2 + (-0.052316469397973964 + m.x6)**2) + m.x279 * ((-0.5653919967842793
    + m.x3)**2 + (-0.27910238121665565 + m.x6)**2) + m.x280 * ((
    -0.6224904598210145 + m.x3)**2 + (-0.02247631649979287 + m.x6)**2) + m.x281
    * ((-0.229051149892618 + m.x3)**2 + (-0.7910496903784138 + m.x6)**2) +
    m.x282 * ((-0.38625690455774275 + m.x3)**2 + (-0.5219004509746287 + m.x6)**
    2) + m.x283 * ((-0.5785186297030117 + m.x3)**2 + (-0.9528110034877589 +
    m.x6)**2) + m.x284 * ((-0.6462821339816298 + m.x3)**2 + (
    -0.6067764925944034 + m.x6)**2) + m.x285 * ((-0.38006243875752277 + m.x3)**
    2 + (-0.32501439221768036 + m.x6)**2) + m.x286 * ((-0.4773778129689302 +
    m.x3)**2 + (-0.3565933083195064 + m.x6)**2) + m.x287 * ((
    -0.33078861302885243 + m.x3)**2 + (-0.37500196195238944 + m.x6)**2) +
    m.x288 * ((-0.5542981262906839 + m.x3)**2 + (-0.19803228322354316 + m.x6)**
    2) + m.x289 * ((-0.6759728791955966 + m.x3)**2 + (-0.10790031453323568 +
    m.x6)**2) + m.x290 * ((-0.32776733692609294 + m.x3)**2 + (
    -0.649698771312504 + m.x6)**2) + m.x291 * ((-0.6849969003224811 + m.x3)**2
    + (-0.31383818211836345 + m.x6)**2) + m.x292 * ((-0.8489741551279321 +
    m.x3)**2 + (-0.4536251040305358 + m.x6)**2) + m.x293 * ((
    -0.5364380411417772 + m.x3)**2 + (-0.7091773891838592 + m.x6)**2) + m.x294
    * ((-0.9803725216985771 + m.x3)**2 + (-0.2741220008365026 + m.x6)**2) +
    m.x295 * ((-0.30949991491899753 + m.x3)**2 + (-0.4397462597339806 + m.x6)**
    2) + m.x296 * ((-0.9195632575532574 + m.x3)**2 + (-0.3235817691663315 +
    m.x6)**2) + m.x297 * ((-0.18190096518085497 + m.x3)**2 + (
    -0.32411302414330956 + m.x6)**2) + m.x298 * ((-0.36343488491763387 + m.x3)
    **2 + (-0.6663092097253003 + m.x6)**2) + m.x299 * ((-0.8168528198966378 +
    m.x3)**2 + (-0.09851383090888444 + m.x6)**2) + m.x300 * ((
    -0.0325822956804418 + m.x3)**2 + (-0.3995952149437163 + m.x6)**2) + m.x301
    * ((-0.6144908043611289 + m.x3)**2 + (-0.10979848578730689 + m.x6)**2) +
    m.x302 * ((-0.8713165943427151 + m.x3)**2 + (-0.6699384226962937 + m.x6)**2)
    + m.x303 * ((-0.9439947803244484 + m.x3)**2 + (-0.29790397105454614 + m.x6)
    **2) + m.x304 * ((-0.68218233799177 + m.x3)**2 + (-0.9650579074996485 +
    m.x6)**2) + m.x305 * ((-0.3455598885840183 + m.x3)**2 + (
    -0.4827230523144219 + m.x6)**2) + m.x306 * ((-0.3322933066434728 + m.x3)**2
    + (-0.6618767361640094 + m.x6)**2))

m.e1 = Constraint(expr= m.x7 + m.x8 + m.x9 + m.x10 + m.x11 + m.x12 + m.x13 +
    m.x14 + m.x15 + m.x16 + m.x17 + m.x18 + m.x19 + m.x20 + m.x21 + m.x22 +
    m.x23 + m.x24 + m.x25 + m.x26 + m.x27 + m.x28 + m.x29 + m.x30 + m.x31 +
    m.x32 + m.x33 + m.x34 + m.x35 + m.x36 + m.x37 + m.x38 + m.x39 + m.x40 +
    m.x41 + m.x42 + m.x43 + m.x44 + m.x45 + m.x46 + m.x47 + m.x48 + m.x49 +
    m.x50 + m.x51 + m.x52 + m.x53 + m.x54 + m.x55 + m.x56 + m.x57 + m.x58 +
    m.x59 + m.x60 + m.x61 + m.x62 + m.x63 + m.x64 + m.x65 + m.x66 + m.x67 +
    m.x68 + m.x69 + m.x70 + m.x71 + m.x72 + m.x73 + m.x74 + m.x75 + m.x76 +
    m.x77 + m.x78 + m.x79 + m.x80 + m.x81 + m.x82 + m.x83 + m.x84 + m.x85 +
    m.x86 + m.x87 + m.x88 + m.x89 + m.x90 + m.x91 + m.x92 + m.x93 + m.x94 +
    m.x95 + m.x96 + m.x97 + m.x98 + m.x99 + m.x100 + m.x101 + m.x102 + m.x103
    + m.x104 + m.x105 + m.x106 <= 23.312517949055152)
m.e2 = Constraint(expr= m.x107 + m.x108 + m.x109 + m.x110 + m.x111 + m.x112 +
    m.x113 + m.x114 + m.x115 + m.x116 + m.x117 + m.x118 + m.x119 + m.x120 +
    m.x121 + m.x122 + m.x123 + m.x124 + m.x125 + m.x126 + m.x127 + m.x128 +
    m.x129 + m.x130 + m.x131 + m.x132 + m.x133 + m.x134 + m.x135 + m.x136 +
    m.x137 + m.x138 + m.x139 + m.x140 + m.x141 + m.x142 + m.x143 + m.x144 +
    m.x145 + m.x146 + m.x147 + m.x148 + m.x149 + m.x150 + m.x151 + m.x152 +
    m.x153 + m.x154 + m.x155 + m.x156 + m.x157 + m.x158 + m.x159 + m.x160 +
    m.x161 + m.x162 + m.x163 + m.x164 + m.x165 + m.x166 + m.x167 + m.x168 +
    m.x169 + m.x170 + m.x171 + m.x172 + m.x173 + m.x174 + m.x175 + m.x176 +
    m.x177 + m.x178 + m.x179 + m.x180 + m.x181 + m.x182 + m.x183 + m.x184 +
    m.x185 + m.x186 + m.x187 + m.x188 + m.x189 + m.x190 + m.x191 + m.x192 +
    m.x193 + m.x194 + m.x195 + m.x196 + m.x197 + m.x198 + m.x199 + m.x200 +
    m.x201 + m.x202 + m.x203 + m.x204 + m.x205 + m.x206 <= 7.992202539773037)
m.e3 = Constraint(expr= m.x207 + m.x208 + m.x209 + m.x210 + m.x211 + m.x212 +
    m.x213 + m.x214 + m.x215 + m.x216 + m.x217 + m.x218 + m.x219 + m.x220 +
    m.x221 + m.x222 + m.x223 + m.x224 + m.x225 + m.x226 + m.x227 + m.x228 +
    m.x229 + m.x230 + m.x231 + m.x232 + m.x233 + m.x234 + m.x235 + m.x236 +
    m.x237 + m.x238 + m.x239 + m.x240 + m.x241 + m.x242 + m.x243 + m.x244 +
    m.x245 + m.x246 + m.x247 + m.x248 + m.x249 + m.x250 + m.x251 + m.x252 +
    m.x253 + m.x254 + m.x255 + m.x256 + m.x257 + m.x258 + m.x259 + m.x260 +
    m.x261 + m.x262 + m.x263 + m.x264 + m.x265 + m.x266 + m.x267 + m.x268 +
    m.x269 + m.x270 + m.x271 + m.x272 + m.x273 + m.x274 + m.x275 + m.x276 +
    m.x277 + m.x278 + m.x279 + m.x280 + m.x281 + m.x282 + m.x283 + m.x284 +
    m.x285 + m.x286 + m.x287 + m.x288 + m.x289 + m.x290 + m.x291 + m.x292 +
    m.x293 + m.x294 + m.x295 + m.x296 + m.x297 + m.x298 + m.x299 + m.x300 +
    m.x301 + m.x302 + m.x303 + m.x304 + m.x305 + m.x306 <= 21.185769723741828)
m.e4 = Constraint(expr= m.x7 + m.x107 + m.x207 == 0.5237887153058475)
m.e5 = Constraint(expr= m.x8 + m.x108 + m.x208 == 0.8197390395798249)
m.e6 = Constraint(expr= m.x9 + m.x109 + m.x209 == 0.7007263939907505)
m.e7 = Constraint(expr= m.x10 + m.x110 + m.x210 == 0.6410987769885296)
m.e8 = Constraint(expr= m.x11 + m.x111 + m.x211 == 0.03204625622688584)
m.e9 = Constraint(expr= m.x12 + m.x112 + m.x212 == 0.14194025464772142)
m.e10 = Constraint(expr= m.x13 + m.x113 + m.x213 == 0.7509195444036073)
m.e11 = Constraint(expr= m.x14 + m.x114 + m.x214 == 0.41195428382398813)
m.e12 = Constraint(expr= m.x15 + m.x115 + m.x215 == 0.9756599461150395)
m.e13 = Constraint(expr= m.x16 + m.x116 + m.x216 == 0.6357147387563624)
m.e14 = Constraint(expr= m.x17 + m.x117 + m.x217 == 0.8233027143964848)
m.e15 = Constraint(expr= m.x18 + m.x118 + m.x218 == 0.7452009388692579)
m.e16 = Constraint(expr= m.x19 + m.x119 + m.x219 == 0.9631027403432417)
m.e17 = Constraint(expr= m.x20 + m.x120 + m.x220 == 0.6577949997144603)
m.e18 = Constraint(expr= m.x21 + m.x121 + m.x221 == 0.9376831647822127)
m.e19 = Constraint(expr= m.x22 + m.x122 + m.x222 == 0.425695099698429)
m.e20 = Constraint(expr= m.x23 + m.x123 + m.x223 == 0.26740170533468643)
m.e21 = Constraint(expr= m.x24 + m.x124 + m.x224 == 0.11020267546426676)
m.e22 = Constraint(expr= m.x25 + m.x125 + m.x225 == 0.2525432086770847)
m.e23 = Constraint(expr= m.x26 + m.x126 + m.x226 == 0.8942483853587863)
m.e24 = Constraint(expr= m.x27 + m.x127 + m.x227 == 0.6581184862557082)
m.e25 = Constraint(expr= m.x28 + m.x128 + m.x228 == 0.043388423870278414)
m.e26 = Constraint(expr= m.x29 + m.x129 + m.x229 == 0.02784903972043573)
m.e27 = Constraint(expr= m.x30 + m.x130 + m.x230 == 0.4605444818560932)
m.e28 = Constraint(expr= m.x31 + m.x131 + m.x231 == 0.5444604172760558)
m.e29 = Constraint(expr= m.x32 + m.x132 + m.x232 == 0.360908160238246)
m.e30 = Constraint(expr= m.x33 + m.x133 + m.x233 == 0.01974758753890249)
m.e31 = Constraint(expr= m.x34 + m.x134 + m.x234 == 0.261690766412771)
m.e32 = Constraint(expr= m.x35 + m.x135 + m.x235 == 0.8768752468271519)
m.e33 = Constraint(expr= m.x36 + m.x136 + m.x236 == 0.7253373936361994)
m.e34 = Constraint(expr= m.x37 + m.x137 + m.x237 == 0.8184306443986822)
m.e35 = Constraint(expr= m.x38 + m.x138 + m.x238 == 0.26956781260883733)
m.e36 = Constraint(expr= m.x39 + m.x139 + m.x239 == 0.6677646127017136)
m.e37 = Constraint(expr= m.x40 + m.x140 + m.x240 == 0.1973038945815052)
m.e38 = Constraint(expr= m.x41 + m.x141 + m.x241 == 0.30173239417617304)
m.e39 = Constraint(expr= m.x42 + m.x142 + m.x242 == 0.9562559069121392)
m.e40 = Constraint(expr= m.x43 + m.x143 + m.x243 == 0.2133897446379358)
m.e41 = Constraint(expr= m.x44 + m.x144 + m.x244 == 0.29251857536512504)
m.e42 = Constraint(expr= m.x45 + m.x145 + m.x245 == 0.21768828301524978)
m.e43 = Constraint(expr= m.x46 + m.x146 + m.x246 == 0.8682755976738481)
m.e44 = Constraint(expr= m.x47 + m.x147 + m.x247 == 0.6872984300075072)
m.e45 = Constraint(expr= m.x48 + m.x148 + m.x248 == 0.5908896312970385)
m.e46 = Constraint(expr= m.x49 + m.x149 + m.x249 == 0.8509936318171801)
m.e47 = Constraint(expr= m.x50 + m.x150 + m.x250 == 0.46358344201862645)
m.e48 = Constraint(expr= m.x51 + m.x151 + m.x251 == 0.9159377819602287)
m.e49 = Constraint(expr= m.x52 + m.x152 + m.x252 == 0.7770447743622878)
m.e50 = Constraint(expr= m.x53 + m.x153 + m.x253 == 0.2994183334407492)
m.e51 = Constraint(expr= m.x54 + m.x154 + m.x254 == 0.2360050852422244)
m.e52 = Constraint(expr= m.x55 + m.x155 + m.x255 == 0.5372592299067787)
m.e53 = Constraint(expr= m.x56 + m.x156 + m.x256 == 0.44610399507715515)
m.e54 = Constraint(expr= m.x57 + m.x157 + m.x257 == 0.7898243499882375)
m.e55 = Constraint(expr= m.x58 + m.x158 + m.x258 == 0.6522657638435604)
m.e56 = Constraint(expr= m.x59 + m.x159 + m.x259 == 0.7425812431395556)
m.e57 = Constraint(expr= m.x60 + m.x160 + m.x260 == 0.6031796991143933)
m.e58 = Constraint(expr= m.x61 + m.x161 + m.x261 == 0.2639004122672084)
m.e59 = Constraint(expr= m.x62 + m.x162 + m.x262 == 0.7439534045650983)
m.e60 = Constraint(expr= m.x63 + m.x163 + m.x263 == 0.9815323874305582)
m.e61 = Constraint(expr= m.x64 + m.x164 + m.x264 == 0.6372056988661013)
m.e62 = Constraint(expr= m.x65 + m.x165 + m.x265 == 0.7109468078437314)
m.e63 = Constraint(expr= m.x66 + m.x166 + m.x266 == 0.23347002717786247)
m.e64 = Constraint(expr= m.x67 + m.x167 + m.x267 == 0.11797083635514338)
m.e65 = Constraint(expr= m.x68 + m.x168 + m.x268 == 0.4480248363035305)
m.e66 = Constraint(expr= m.x69 + m.x169 + m.x269 == 0.5936042501232476)
m.e67 = Constraint(expr= m.x70 + m.x170 + m.x270 == 0.7272096632515725)
m.e68 = Constraint(expr= m.x71 + m.x171 + m.x271 == 0.47404919245899513)
m.e69 = Constraint(expr= m.x72 + m.x172 + m.x272 == 0.5437181913812397)
m.e70 = Constraint(expr= m.x73 + m.x173 + m.x273 == 0.08849299861942617)
m.e71 = Constraint(expr= m.x74 + m.x174 + m.x274 == 0.04795823025964907)
m.e72 = Constraint(expr= m.x75 + m.x175 + m.x275 == 0.12163746373450335)
m.e73 = Constraint(expr= m.x76 + m.x176 + m.x276 == 0.31873169940318014)
m.e74 = Constraint(expr= m.x77 + m.x177 + m.x277 == 0.24323151557893374)
m.e75 = Constraint(expr= m.x78 + m.x178 + m.x278 == 0.1428790443921223)
m.e76 = Constraint(expr= m.x79 + m.x179 + m.x279 == 0.33845342083585306)
m.e77 = Constraint(expr= m.x80 + m.x180 + m.x280 == 0.336854070335152)
m.e78 = Constraint(expr= m.x81 + m.x181 + m.x281 == 0.8241728384960878)
m.e79 = Constraint(expr= m.x82 + m.x182 + m.x282 == 0.9351733693903606)
m.e80 = Constraint(expr= m.x83 + m.x183 + m.x283 == 0.993790312953735)
m.e81 = Constraint(expr= m.x84 + m.x184 + m.x284 == 0.7373173791804193)
m.e82 = Constraint(expr= m.x85 + m.x185 + m.x285 == 0.011236594114943932)
m.e83 = Constraint(expr= m.x86 + m.x186 + m.x286 == 0.2380112043077156)
m.e84 = Constraint(expr= m.x87 + m.x187 + m.x287 == 0.9989619309272509)
m.e85 = Constraint(expr= m.x88 + m.x188 + m.x288 == 0.6958783695578226)
m.e86 = Constraint(expr= m.x89 + m.x189 + m.x289 == 0.857856239292848)
m.e87 = Constraint(expr= m.x90 + m.x190 + m.x290 == 0.1997091610618259)
m.e88 = Constraint(expr= m.x91 + m.x191 + m.x291 == 0.2403669141527106)
m.e89 = Constraint(expr= m.x92 + m.x192 + m.x292 == 0.09814473768311915)
m.e90 = Constraint(expr= m.x93 + m.x193 + m.x293 == 0.5248518543198755)
m.e91 = Constraint(expr= m.x94 + m.x194 + m.x294 == 0.3657755152940917)
m.e92 = Constraint(expr= m.x95 + m.x195 + m.x295 == 0.47078288049219363)
m.e93 = Constraint(expr= m.x96 + m.x196 + m.x296 == 0.1383236543919154)
m.e94 = Constraint(expr= m.x97 + m.x197 + m.x297 == 0.025699495194813293)
m.e95 = Constraint(expr= m.x98 + m.x198 + m.x298 == 0.38619486280807336)
m.e96 = Constraint(expr= m.x99 + m.x199 + m.x299 == 0.9265393344860128)
m.e97 = Constraint(expr= m.x100 + m.x200 + m.x300 == 0.6526024687304363)
m.e98 = Constraint(expr= m.x101 + m.x201 + m.x301 == 0.571630959084446)
m.e99 = Constraint(expr= m.x102 + m.x202 + m.x302 == 0.06307829508913498)
m.e100 = Constraint(expr= m.x103 + m.x203 + m.x303 == 0.43344211320173276)
m.e101 = Constraint(expr= m.x104 + m.x204 + m.x304 == 0.36912668590229003)
m.e102 = Constraint(expr= m.x105 + m.x205 + m.x305 == 0.6306101492650494)
m.e103 = Constraint(expr= m.x106 + m.x206 + m.x306 == 0.40284514563242635)
