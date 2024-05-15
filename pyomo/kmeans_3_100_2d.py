# NLP written by GAMS Convert at 05/15/24 11:38:55
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       100      100        0        0        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#       306      306        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       300      300        0
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
m.x7 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x8 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x9 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x10 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x11 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x12 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x13 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x14 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x15 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x16 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x17 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x18 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x19 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x20 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x21 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x22 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x23 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x24 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x25 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x26 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x27 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x28 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x29 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x30 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x31 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x32 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x33 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x34 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x35 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x36 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x37 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x38 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x39 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x40 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x41 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x42 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x43 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x44 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x45 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x46 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x47 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x48 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x49 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x50 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x51 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x52 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x53 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x54 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x55 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x56 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x57 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x58 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x59 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x60 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x61 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x62 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x63 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x64 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x65 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x66 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x67 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x68 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x69 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x70 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x71 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x72 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x73 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x74 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x75 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x76 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x77 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x78 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x79 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x80 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x81 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x82 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x83 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x84 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x85 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x86 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x87 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x88 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x89 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x90 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x91 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x92 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x93 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x94 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x95 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x96 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x97 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x98 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x99 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x100 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x101 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x102 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x103 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x104 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x105 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x106 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x107 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x108 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x109 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x110 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x111 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x112 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x113 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x114 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x115 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x116 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x117 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x118 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x119 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x120 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x121 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x122 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x123 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x124 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x125 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x126 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x127 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x128 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x129 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x130 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x131 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x132 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x133 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x134 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x135 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x136 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x137 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x138 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x139 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x140 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x141 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x142 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x143 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x144 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x145 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x146 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x147 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x148 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x149 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x150 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x151 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x152 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x153 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x154 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x155 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x156 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x157 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x158 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x159 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x160 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x161 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x162 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x163 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x164 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x165 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x166 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x167 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x168 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x169 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x170 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x171 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x172 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x173 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x174 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x175 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x176 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x177 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x178 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x179 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x180 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x181 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x182 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x183 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x184 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x185 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x186 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x187 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x188 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x189 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x190 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x191 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x192 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x193 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x194 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x195 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x196 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x197 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x198 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x199 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x200 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x201 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x202 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x203 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x204 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x205 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x206 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x207 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x208 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x209 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x210 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x211 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x212 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x213 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x214 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x215 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x216 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x217 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x218 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x219 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x220 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x221 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x222 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x223 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x224 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x225 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x226 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x227 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x228 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x229 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x230 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x231 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x232 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x233 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x234 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x235 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x236 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x237 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x238 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x239 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x240 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x241 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x242 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x243 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x244 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x245 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x246 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x247 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x248 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x249 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x250 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x251 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x252 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x253 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x254 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x255 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x256 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x257 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x258 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x259 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x260 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x261 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x262 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x263 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x264 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x265 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x266 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x267 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x268 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x269 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x270 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x271 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x272 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x273 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x274 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x275 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x276 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x277 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x278 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x279 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x280 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x281 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x282 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x283 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x284 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x285 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x286 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x287 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x288 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x289 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x290 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x291 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x292 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x293 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x294 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x295 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x296 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x297 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x298 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x299 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x300 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x301 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x302 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x303 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x304 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x305 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x306 = Var(within=Reals, bounds=(0,1), initialize=0)

m.obj = Objective(sense=minimize, expr= m.x7 * ((-0.09075818242392208 + m.x1)**
    2 + (-0.8421079776592801 + m.x2)**2) + m.x8 * ((-0.6004522437099808 + m.x1)
    **2 + (-0.21263042858868297 + m.x2)**2) + m.x9 * ((-0.7796888052878697 +
    m.x1)**2 + (-0.594607792619549 + m.x2)**2) + m.x10 * ((-0.8280428816489178
    + m.x1)**2 + (-0.6117694619049227 + m.x2)**2) + m.x11 * ((
    -0.7232635246380339 + m.x1)**2 + (-0.775046380224854 + m.x2)**2) + m.x12 *
    ((-0.3441150906887649 + m.x1)**2 + (-0.09591837784379154 + m.x2)**2) +
    m.x13 * ((-0.8978018174450971 + m.x1)**2 + (-0.11743401812053855 + m.x2)**2)
    + m.x14 * ((-0.55682365402602 + m.x1)**2 + (-0.9913046724886798 + m.x2)**2)
    + m.x15 * ((-0.3505034340325558 + m.x1)**2 + (-0.2614391117299726 + m.x2)
    **2) + m.x16 * ((-0.3824468288111288 + m.x1)**2 + (-0.20220584044474332 +
    m.x2)**2) + m.x17 * ((-0.7498554818721458 + m.x1)**2 + (-0.2980988319317168
    + m.x2)**2) + m.x18 * ((-0.07321113686532232 + m.x1)**2 + (
    -0.5954543460403101 + m.x2)**2) + m.x19 * ((-0.2591946170455186 + m.x1)**2
    + (-0.17900103418991686 + m.x2)**2) + m.x20 * ((-0.01679199868038328 +
    m.x1)**2 + (-0.8388400298206995 + m.x2)**2) + m.x21 * ((
    -0.37772078666940234 + m.x1)**2 + (-0.5999660129800334 + m.x2)**2) + m.x22
    * ((-0.48068712289031845 + m.x1)**2 + (-0.869272912824029 + m.x2)**2) +
    m.x23 * ((-0.06731672306732117 + m.x1)**2 + (-0.633941896159872 + m.x2)**2)
    + m.x24 * ((-0.82972309353278 + m.x1)**2 + (-0.2819959347943841 + m.x2)**2)
    + m.x25 * ((-0.4336964173301845 + m.x1)**2 + (-0.3365710275789563 + m.x2)
    **2) + m.x26 * ((-0.32388608941489017 + m.x1)**2 + (-0.9453815506006258 +
    m.x2)**2) + m.x27 * ((-0.22860079388436005 + m.x1)**2 + (
    -0.7378173460947715 + m.x2)**2) + m.x28 * ((-0.044228036986523334 + m.x1)**
    2 + (-0.7815501177884507 + m.x2)**2) + m.x29 * ((-0.08043624219732093 +
    m.x1)**2 + (-0.7893569476421274 + m.x2)**2) + m.x30 * ((
    -0.06584041867144719 + m.x1)**2 + (-0.21534482582658754 + m.x2)**2) + m.x31
    * ((-0.2637962086928157 + m.x1)**2 + (-0.2815287894707502 + m.x2)**2) +
    m.x32 * ((-0.7768911997798632 + m.x1)**2 + (-0.5045725783219106 + m.x2)**2)
    + m.x33 * ((-0.04578282615703744 + m.x1)**2 + (-0.18267404955070377 + m.x2)
    **2) + m.x34 * ((-0.4189753804741293 + m.x1)**2 + (-0.7106072440375385 +
    m.x2)**2) + m.x35 * ((-0.6406679155857211 + m.x1)**2 + (
    -0.48003679153199974 + m.x2)**2) + m.x36 * ((-0.8075575156075806 + m.x1)**2
    + (-0.9463374617065154 + m.x2)**2) + m.x37 * ((-0.9494783754127006 + m.x1)
    **2 + (-0.991498001949757 + m.x2)**2) + m.x38 * ((-0.9193098198259494 +
    m.x1)**2 + (-0.9861536873250794 + m.x2)**2) + m.x39 * ((-0.7164219770083897
    + m.x1)**2 + (-0.6923582419906285 + m.x2)**2) + m.x40 * ((
    -0.5833953772276935 + m.x1)**2 + (-0.39111319713457526 + m.x2)**2) + m.x41
    * ((-0.837098292307243 + m.x1)**2 + (-0.38192022803643044 + m.x2)**2) +
    m.x42 * ((-0.9057165619357027 + m.x1)**2 + (-0.44142026666630774 + m.x2)**2)
    + m.x43 * ((-0.022143901365561658 + m.x1)**2 + (-0.8476360117762948 + m.x2)
    **2) + m.x44 * ((-0.48474449470792136 + m.x1)**2 + (-0.00459266186465912 +
    m.x2)**2) + m.x45 * ((-0.817975273750891 + m.x1)**2 + (-0.7943398076449755
    + m.x2)**2) + m.x46 * ((-0.8763576508107064 + m.x1)**2 + (
    -0.4641969432665859 + m.x2)**2) + m.x47 * ((-0.16768907807527522 + m.x1)**2
    + (-0.2170634659028503 + m.x2)**2) + m.x48 * ((-0.5373771347576884 + m.x1)
    **2 + (-0.6717398317968319 + m.x2)**2) + m.x49 * ((-0.5572182447521413 +
    m.x1)**2 + (-0.24059245819741681 + m.x2)**2) + m.x50 * ((
    -0.1478639049629319 + m.x1)**2 + (-0.9734391500956013 + m.x2)**2) + m.x51
    * ((-0.9978674296675508 + m.x1)**2 + (-0.940321306057178 + m.x2)**2) +
    m.x52 * ((-0.5198249152613603 + m.x1)**2 + (-0.07814164651753441 + m.x2)**2)
    + m.x53 * ((-0.2206544748113004 + m.x1)**2 + (-0.5529047264313456 + m.x2)
    **2) + m.x54 * ((-0.8708713492140824 + m.x1)**2 + (-0.6958022669870113 +
    m.x2)**2) + m.x55 * ((-0.10823774288352628 + m.x1)**2 + (-0.915893092354332
    + m.x2)**2) + m.x56 * ((-0.641766743884591 + m.x1)**2 + (
    -0.42982985602002743 + m.x2)**2) + m.x57 * ((-0.769965120581223 + m.x1)**2
    + (-0.4093180346858043 + m.x2)**2) + m.x58 * ((-0.5395061655932872 + m.x1)
    **2 + (-0.025554298316395885 + m.x2)**2) + m.x59 * ((-0.07610548086145708
    + m.x1)**2 + (-0.9300387630629019 + m.x2)**2) + m.x60 * ((
    -0.42188661474763056 + m.x1)**2 + (-0.7909513854242108 + m.x2)**2) + m.x61
    * ((-0.371398443903442 + m.x1)**2 + (-0.3924282936519774 + m.x2)**2) +
    m.x62 * ((-0.11106976179816641 + m.x1)**2 + (-0.8961539552567241 + m.x2)**2)
    + m.x63 * ((-0.25225491988669413 + m.x1)**2 + (-0.7663134725002734 + m.x2)
    **2) + m.x64 * ((-0.1778448829280641 + m.x1)**2 + (-0.3035505722762858 +
    m.x2)**2) + m.x65 * ((-0.08846844345193006 + m.x1)**2 + (-0.695683685601309
    + m.x2)**2) + m.x66 * ((-0.9178016597694366 + m.x1)**2 + (
    -0.627158371143039 + m.x2)**2) + m.x67 * ((-0.6443309388504812 + m.x1)**2
    + (-0.2486686334041649 + m.x2)**2) + m.x68 * ((-0.9524214315197214 + m.x1)
    **2 + (-0.11319191562464526 + m.x2)**2) + m.x69 * ((-0.2503629075652184 +
    m.x1)**2 + (-0.5661083721487875 + m.x2)**2) + m.x70 * ((-0.6399923314007278
    + m.x1)**2 + (-0.2871936662554734 + m.x2)**2) + m.x71 * ((
    -0.5909678451374885 + m.x1)**2 + (-0.11513193031994995 + m.x2)**2) + m.x72
    * ((-0.04877753856435085 + m.x1)**2 + (-0.42558284132001833 + m.x2)**2) +
    m.x73 * ((-0.5769401342223824 + m.x1)**2 + (-0.882886241480543 + m.x2)**2)
    + m.x74 * ((-0.46693829720314983 + m.x1)**2 + (-0.9356416589786831 + m.x2)
    **2) + m.x75 * ((-0.7666488385496458 + m.x1)**2 + (-0.9715298035824393 +
    m.x2)**2) + m.x76 * ((-0.7090808859061516 + m.x1)**2 + (-0.4227160317233293
    + m.x2)**2) + m.x77 * ((-0.6362788867985969 + m.x1)**2 + (
    -0.6897106599456068 + m.x2)**2) + m.x78 * ((-0.255234369371772 + m.x1)**2
    + (-0.17269883755498971 + m.x2)**2) + m.x79 * ((-0.32354052437441105 +
    m.x1)**2 + (-0.5414620932536305 + m.x2)**2) + m.x80 * ((
    -0.05061498170688461 + m.x1)**2 + (-0.35735103685050085 + m.x2)**2) + m.x81
    * ((-0.14474828789786598 + m.x1)**2 + (-0.935524701349798 + m.x2)**2) +
    m.x82 * ((-0.4521811868578507 + m.x1)**2 + (-0.5684301129850728 + m.x2)**2)
    + m.x83 * ((-0.1391588120468895 + m.x1)**2 + (-0.450912724117135 + m.x2)**
    2) + m.x84 * ((-0.9624575143884582 + m.x1)**2 + (-0.8342971742225577 + m.x2)
    **2) + m.x85 * ((-0.9119608671435646 + m.x1)**2 + (-0.16311646954688963 +
    m.x2)**2) + m.x86 * ((-0.8601502139251708 + m.x1)**2 + (-0.8094641566594614
    + m.x2)**2) + m.x87 * ((-0.3789359642178741 + m.x1)**2 + (
    -0.34458507559213336 + m.x2)**2) + m.x88 * ((-0.9114125110384265 + m.x1)**2
    + (-0.30087502888988404 + m.x2)**2) + m.x89 * ((-0.26441815851376227 +
    m.x1)**2 + (-0.6432639278749842 + m.x2)**2) + m.x90 * ((-0.5040138219051838
    + m.x1)**2 + (-0.436711978156451 + m.x2)**2) + m.x91 * ((
    -0.42408540833910613 + m.x1)**2 + (-0.7144533169040485 + m.x2)**2) + m.x92
    * ((-0.7222403067943077 + m.x1)**2 + (-0.44905804057404974 + m.x2)**2) +
    m.x93 * ((-0.9396234683501675 + m.x1)**2 + (-0.26913749666376663 + m.x2)**2)
    + m.x94 * ((-0.2790684514984879 + m.x1)**2 + (-0.38848808536128043 + m.x2)
    **2) + m.x95 * ((-0.0023428037609517505 + m.x1)**2 + (-0.5050951718570706
    + m.x2)**2) + m.x96 * ((-0.4770114774545686 + m.x1)**2 + (
    -0.2671796475851538 + m.x2)**2) + m.x97 * ((-0.4508813622466006 + m.x1)**2
    + (-0.4772479476478516 + m.x2)**2) + m.x98 * ((-0.5802987597800233 + m.x1)
    **2 + (-0.5447533523575115 + m.x2)**2) + m.x99 * ((-0.3417733382726399 +
    m.x1)**2 + (-0.36547565910865576 + m.x2)**2) + m.x100 * ((
    -0.8660746835055481 + m.x1)**2 + (-0.06852013071726426 + m.x2)**2) + m.x101
    * ((-0.8912654289001969 + m.x1)**2 + (-0.13480953224510595 + m.x2)**2) +
    m.x102 * ((-0.1717093974981898 + m.x1)**2 + (-0.4333331682797753 + m.x2)**2)
    + m.x103 * ((-0.9880935005856811 + m.x1)**2 + (-0.22149623450972045 + m.x2)
    **2) + m.x104 * ((-0.05074359135359818 + m.x1)**2 + (-0.7593065812217639 +
    m.x2)**2) + m.x105 * ((-0.5089474327061579 + m.x1)**2 + (
    -0.13233399599992335 + m.x2)**2) + m.x106 * ((-0.8898331485351556 + m.x1)**
    2 + (-0.5844278795567586 + m.x2)**2) + m.x107 * ((-0.09075818242392208 +
    m.x3)**2 + (-0.8421079776592801 + m.x4)**2) + m.x108 * ((
    -0.6004522437099808 + m.x3)**2 + (-0.21263042858868297 + m.x4)**2) + m.x109
    * ((-0.7796888052878697 + m.x3)**2 + (-0.594607792619549 + m.x4)**2) +
    m.x110 * ((-0.8280428816489178 + m.x3)**2 + (-0.6117694619049227 + m.x4)**2)
    + m.x111 * ((-0.7232635246380339 + m.x3)**2 + (-0.775046380224854 + m.x4)
    **2) + m.x112 * ((-0.3441150906887649 + m.x3)**2 + (-0.09591837784379154 +
    m.x4)**2) + m.x113 * ((-0.8978018174450971 + m.x3)**2 + (
    -0.11743401812053855 + m.x4)**2) + m.x114 * ((-0.55682365402602 + m.x3)**2
    + (-0.9913046724886798 + m.x4)**2) + m.x115 * ((-0.3505034340325558 + m.x3)
    **2 + (-0.2614391117299726 + m.x4)**2) + m.x116 * ((-0.3824468288111288 +
    m.x3)**2 + (-0.20220584044474332 + m.x4)**2) + m.x117 * ((
    -0.7498554818721458 + m.x3)**2 + (-0.2980988319317168 + m.x4)**2) + m.x118
    * ((-0.07321113686532232 + m.x3)**2 + (-0.5954543460403101 + m.x4)**2) +
    m.x119 * ((-0.2591946170455186 + m.x3)**2 + (-0.17900103418991686 + m.x4)**
    2) + m.x120 * ((-0.01679199868038328 + m.x3)**2 + (-0.8388400298206995 +
    m.x4)**2) + m.x121 * ((-0.37772078666940234 + m.x3)**2 + (
    -0.5999660129800334 + m.x4)**2) + m.x122 * ((-0.48068712289031845 + m.x3)**
    2 + (-0.869272912824029 + m.x4)**2) + m.x123 * ((-0.06731672306732117 +
    m.x3)**2 + (-0.633941896159872 + m.x4)**2) + m.x124 * ((-0.82972309353278
    + m.x3)**2 + (-0.2819959347943841 + m.x4)**2) + m.x125 * ((
    -0.4336964173301845 + m.x3)**2 + (-0.3365710275789563 + m.x4)**2) + m.x126
    * ((-0.32388608941489017 + m.x3)**2 + (-0.9453815506006258 + m.x4)**2) +
    m.x127 * ((-0.22860079388436005 + m.x3)**2 + (-0.7378173460947715 + m.x4)**
    2) + m.x128 * ((-0.044228036986523334 + m.x3)**2 + (-0.7815501177884507 +
    m.x4)**2) + m.x129 * ((-0.08043624219732093 + m.x3)**2 + (
    -0.7893569476421274 + m.x4)**2) + m.x130 * ((-0.06584041867144719 + m.x3)**
    2 + (-0.21534482582658754 + m.x4)**2) + m.x131 * ((-0.2637962086928157 +
    m.x3)**2 + (-0.2815287894707502 + m.x4)**2) + m.x132 * ((
    -0.7768911997798632 + m.x3)**2 + (-0.5045725783219106 + m.x4)**2) + m.x133
    * ((-0.04578282615703744 + m.x3)**2 + (-0.18267404955070377 + m.x4)**2) +
    m.x134 * ((-0.4189753804741293 + m.x3)**2 + (-0.7106072440375385 + m.x4)**2)
    + m.x135 * ((-0.6406679155857211 + m.x3)**2 + (-0.48003679153199974 + m.x4)
    **2) + m.x136 * ((-0.8075575156075806 + m.x3)**2 + (-0.9463374617065154 +
    m.x4)**2) + m.x137 * ((-0.9494783754127006 + m.x3)**2 + (-0.991498001949757
    + m.x4)**2) + m.x138 * ((-0.9193098198259494 + m.x3)**2 + (
    -0.9861536873250794 + m.x4)**2) + m.x139 * ((-0.7164219770083897 + m.x3)**2
    + (-0.6923582419906285 + m.x4)**2) + m.x140 * ((-0.5833953772276935 + m.x3)
    **2 + (-0.39111319713457526 + m.x4)**2) + m.x141 * ((-0.837098292307243 +
    m.x3)**2 + (-0.38192022803643044 + m.x4)**2) + m.x142 * ((
    -0.9057165619357027 + m.x3)**2 + (-0.44142026666630774 + m.x4)**2) + m.x143
    * ((-0.022143901365561658 + m.x3)**2 + (-0.8476360117762948 + m.x4)**2) +
    m.x144 * ((-0.48474449470792136 + m.x3)**2 + (-0.00459266186465912 + m.x4)
    **2) + m.x145 * ((-0.817975273750891 + m.x3)**2 + (-0.7943398076449755 +
    m.x4)**2) + m.x146 * ((-0.8763576508107064 + m.x3)**2 + (
    -0.4641969432665859 + m.x4)**2) + m.x147 * ((-0.16768907807527522 + m.x3)**
    2 + (-0.2170634659028503 + m.x4)**2) + m.x148 * ((-0.5373771347576884 +
    m.x3)**2 + (-0.6717398317968319 + m.x4)**2) + m.x149 * ((
    -0.5572182447521413 + m.x3)**2 + (-0.24059245819741681 + m.x4)**2) + m.x150
    * ((-0.1478639049629319 + m.x3)**2 + (-0.9734391500956013 + m.x4)**2) +
    m.x151 * ((-0.9978674296675508 + m.x3)**2 + (-0.940321306057178 + m.x4)**2)
    + m.x152 * ((-0.5198249152613603 + m.x3)**2 + (-0.07814164651753441 + m.x4)
    **2) + m.x153 * ((-0.2206544748113004 + m.x3)**2 + (-0.5529047264313456 +
    m.x4)**2) + m.x154 * ((-0.8708713492140824 + m.x3)**2 + (
    -0.6958022669870113 + m.x4)**2) + m.x155 * ((-0.10823774288352628 + m.x3)**
    2 + (-0.915893092354332 + m.x4)**2) + m.x156 * ((-0.641766743884591 + m.x3)
    **2 + (-0.42982985602002743 + m.x4)**2) + m.x157 * ((-0.769965120581223 +
    m.x3)**2 + (-0.4093180346858043 + m.x4)**2) + m.x158 * ((
    -0.5395061655932872 + m.x3)**2 + (-0.025554298316395885 + m.x4)**2) +
    m.x159 * ((-0.07610548086145708 + m.x3)**2 + (-0.9300387630629019 + m.x4)**
    2) + m.x160 * ((-0.42188661474763056 + m.x3)**2 + (-0.7909513854242108 +
    m.x4)**2) + m.x161 * ((-0.371398443903442 + m.x3)**2 + (-0.3924282936519774
    + m.x4)**2) + m.x162 * ((-0.11106976179816641 + m.x3)**2 + (
    -0.8961539552567241 + m.x4)**2) + m.x163 * ((-0.25225491988669413 + m.x3)**
    2 + (-0.7663134725002734 + m.x4)**2) + m.x164 * ((-0.1778448829280641 +
    m.x3)**2 + (-0.3035505722762858 + m.x4)**2) + m.x165 * ((
    -0.08846844345193006 + m.x3)**2 + (-0.695683685601309 + m.x4)**2) + m.x166
    * ((-0.9178016597694366 + m.x3)**2 + (-0.627158371143039 + m.x4)**2) +
    m.x167 * ((-0.6443309388504812 + m.x3)**2 + (-0.2486686334041649 + m.x4)**2)
    + m.x168 * ((-0.9524214315197214 + m.x3)**2 + (-0.11319191562464526 + m.x4)
    **2) + m.x169 * ((-0.2503629075652184 + m.x3)**2 + (-0.5661083721487875 +
    m.x4)**2) + m.x170 * ((-0.6399923314007278 + m.x3)**2 + (
    -0.2871936662554734 + m.x4)**2) + m.x171 * ((-0.5909678451374885 + m.x3)**2
    + (-0.11513193031994995 + m.x4)**2) + m.x172 * ((-0.04877753856435085 +
    m.x3)**2 + (-0.42558284132001833 + m.x4)**2) + m.x173 * ((
    -0.5769401342223824 + m.x3)**2 + (-0.882886241480543 + m.x4)**2) + m.x174
    * ((-0.46693829720314983 + m.x3)**2 + (-0.9356416589786831 + m.x4)**2) +
    m.x175 * ((-0.7666488385496458 + m.x3)**2 + (-0.9715298035824393 + m.x4)**2)
    + m.x176 * ((-0.7090808859061516 + m.x3)**2 + (-0.4227160317233293 + m.x4)
    **2) + m.x177 * ((-0.6362788867985969 + m.x3)**2 + (-0.6897106599456068 +
    m.x4)**2) + m.x178 * ((-0.255234369371772 + m.x3)**2 + (
    -0.17269883755498971 + m.x4)**2) + m.x179 * ((-0.32354052437441105 + m.x3)
    **2 + (-0.5414620932536305 + m.x4)**2) + m.x180 * ((-0.05061498170688461 +
    m.x3)**2 + (-0.35735103685050085 + m.x4)**2) + m.x181 * ((
    -0.14474828789786598 + m.x3)**2 + (-0.935524701349798 + m.x4)**2) + m.x182
    * ((-0.4521811868578507 + m.x3)**2 + (-0.5684301129850728 + m.x4)**2) +
    m.x183 * ((-0.1391588120468895 + m.x3)**2 + (-0.450912724117135 + m.x4)**2)
    + m.x184 * ((-0.9624575143884582 + m.x3)**2 + (-0.8342971742225577 + m.x4)
    **2) + m.x185 * ((-0.9119608671435646 + m.x3)**2 + (-0.16311646954688963 +
    m.x4)**2) + m.x186 * ((-0.8601502139251708 + m.x3)**2 + (
    -0.8094641566594614 + m.x4)**2) + m.x187 * ((-0.3789359642178741 + m.x3)**2
    + (-0.34458507559213336 + m.x4)**2) + m.x188 * ((-0.9114125110384265 +
    m.x3)**2 + (-0.30087502888988404 + m.x4)**2) + m.x189 * ((
    -0.26441815851376227 + m.x3)**2 + (-0.6432639278749842 + m.x4)**2) + m.x190
    * ((-0.5040138219051838 + m.x3)**2 + (-0.436711978156451 + m.x4)**2) +
    m.x191 * ((-0.42408540833910613 + m.x3)**2 + (-0.7144533169040485 + m.x4)**
    2) + m.x192 * ((-0.7222403067943077 + m.x3)**2 + (-0.44905804057404974 +
    m.x4)**2) + m.x193 * ((-0.9396234683501675 + m.x3)**2 + (
    -0.26913749666376663 + m.x4)**2) + m.x194 * ((-0.2790684514984879 + m.x3)**
    2 + (-0.38848808536128043 + m.x4)**2) + m.x195 * ((-0.0023428037609517505
    + m.x3)**2 + (-0.5050951718570706 + m.x4)**2) + m.x196 * ((
    -0.4770114774545686 + m.x3)**2 + (-0.2671796475851538 + m.x4)**2) + m.x197
    * ((-0.4508813622466006 + m.x3)**2 + (-0.4772479476478516 + m.x4)**2) +
    m.x198 * ((-0.5802987597800233 + m.x3)**2 + (-0.5447533523575115 + m.x4)**2)
    + m.x199 * ((-0.3417733382726399 + m.x3)**2 + (-0.36547565910865576 + m.x4)
    **2) + m.x200 * ((-0.8660746835055481 + m.x3)**2 + (-0.06852013071726426 +
    m.x4)**2) + m.x201 * ((-0.8912654289001969 + m.x3)**2 + (
    -0.13480953224510595 + m.x4)**2) + m.x202 * ((-0.1717093974981898 + m.x3)**
    2 + (-0.4333331682797753 + m.x4)**2) + m.x203 * ((-0.9880935005856811 +
    m.x3)**2 + (-0.22149623450972045 + m.x4)**2) + m.x204 * ((
    -0.05074359135359818 + m.x3)**2 + (-0.7593065812217639 + m.x4)**2) + m.x205
    * ((-0.5089474327061579 + m.x3)**2 + (-0.13233399599992335 + m.x4)**2) +
    m.x206 * ((-0.8898331485351556 + m.x3)**2 + (-0.5844278795567586 + m.x4)**2)
    + m.x207 * ((-0.09075818242392208 + m.x5)**2 + (-0.8421079776592801 + m.x6)
    **2) + m.x208 * ((-0.6004522437099808 + m.x5)**2 + (-0.21263042858868297 +
    m.x6)**2) + m.x209 * ((-0.7796888052878697 + m.x5)**2 + (-0.594607792619549
    + m.x6)**2) + m.x210 * ((-0.8280428816489178 + m.x5)**2 + (
    -0.6117694619049227 + m.x6)**2) + m.x211 * ((-0.7232635246380339 + m.x5)**2
    + (-0.775046380224854 + m.x6)**2) + m.x212 * ((-0.3441150906887649 + m.x5)
    **2 + (-0.09591837784379154 + m.x6)**2) + m.x213 * ((-0.8978018174450971 +
    m.x5)**2 + (-0.11743401812053855 + m.x6)**2) + m.x214 * ((-0.55682365402602
    + m.x5)**2 + (-0.9913046724886798 + m.x6)**2) + m.x215 * ((
    -0.3505034340325558 + m.x5)**2 + (-0.2614391117299726 + m.x6)**2) + m.x216
    * ((-0.3824468288111288 + m.x5)**2 + (-0.20220584044474332 + m.x6)**2) +
    m.x217 * ((-0.7498554818721458 + m.x5)**2 + (-0.2980988319317168 + m.x6)**2)
    + m.x218 * ((-0.07321113686532232 + m.x5)**2 + (-0.5954543460403101 + m.x6)
    **2) + m.x219 * ((-0.2591946170455186 + m.x5)**2 + (-0.17900103418991686 +
    m.x6)**2) + m.x220 * ((-0.01679199868038328 + m.x5)**2 + (
    -0.8388400298206995 + m.x6)**2) + m.x221 * ((-0.37772078666940234 + m.x5)**
    2 + (-0.5999660129800334 + m.x6)**2) + m.x222 * ((-0.48068712289031845 +
    m.x5)**2 + (-0.869272912824029 + m.x6)**2) + m.x223 * ((
    -0.06731672306732117 + m.x5)**2 + (-0.633941896159872 + m.x6)**2) + m.x224
    * ((-0.82972309353278 + m.x5)**2 + (-0.2819959347943841 + m.x6)**2) +
    m.x225 * ((-0.4336964173301845 + m.x5)**2 + (-0.3365710275789563 + m.x6)**2)
    + m.x226 * ((-0.32388608941489017 + m.x5)**2 + (-0.9453815506006258 + m.x6)
    **2) + m.x227 * ((-0.22860079388436005 + m.x5)**2 + (-0.7378173460947715 +
    m.x6)**2) + m.x228 * ((-0.044228036986523334 + m.x5)**2 + (
    -0.7815501177884507 + m.x6)**2) + m.x229 * ((-0.08043624219732093 + m.x5)**
    2 + (-0.7893569476421274 + m.x6)**2) + m.x230 * ((-0.06584041867144719 +
    m.x5)**2 + (-0.21534482582658754 + m.x6)**2) + m.x231 * ((
    -0.2637962086928157 + m.x5)**2 + (-0.2815287894707502 + m.x6)**2) + m.x232
    * ((-0.7768911997798632 + m.x5)**2 + (-0.5045725783219106 + m.x6)**2) +
    m.x233 * ((-0.04578282615703744 + m.x5)**2 + (-0.18267404955070377 + m.x6)
    **2) + m.x234 * ((-0.4189753804741293 + m.x5)**2 + (-0.7106072440375385 +
    m.x6)**2) + m.x235 * ((-0.6406679155857211 + m.x5)**2 + (
    -0.48003679153199974 + m.x6)**2) + m.x236 * ((-0.8075575156075806 + m.x5)**
    2 + (-0.9463374617065154 + m.x6)**2) + m.x237 * ((-0.9494783754127006 +
    m.x5)**2 + (-0.991498001949757 + m.x6)**2) + m.x238 * ((-0.9193098198259494
    + m.x5)**2 + (-0.9861536873250794 + m.x6)**2) + m.x239 * ((
    -0.7164219770083897 + m.x5)**2 + (-0.6923582419906285 + m.x6)**2) + m.x240
    * ((-0.5833953772276935 + m.x5)**2 + (-0.39111319713457526 + m.x6)**2) +
    m.x241 * ((-0.837098292307243 + m.x5)**2 + (-0.38192022803643044 + m.x6)**2)
    + m.x242 * ((-0.9057165619357027 + m.x5)**2 + (-0.44142026666630774 + m.x6)
    **2) + m.x243 * ((-0.022143901365561658 + m.x5)**2 + (-0.8476360117762948
    + m.x6)**2) + m.x244 * ((-0.48474449470792136 + m.x5)**2 + (
    -0.00459266186465912 + m.x6)**2) + m.x245 * ((-0.817975273750891 + m.x5)**2
    + (-0.7943398076449755 + m.x6)**2) + m.x246 * ((-0.8763576508107064 + m.x5)
    **2 + (-0.4641969432665859 + m.x6)**2) + m.x247 * ((-0.16768907807527522 +
    m.x5)**2 + (-0.2170634659028503 + m.x6)**2) + m.x248 * ((
    -0.5373771347576884 + m.x5)**2 + (-0.6717398317968319 + m.x6)**2) + m.x249
    * ((-0.5572182447521413 + m.x5)**2 + (-0.24059245819741681 + m.x6)**2) +
    m.x250 * ((-0.1478639049629319 + m.x5)**2 + (-0.9734391500956013 + m.x6)**2)
    + m.x251 * ((-0.9978674296675508 + m.x5)**2 + (-0.940321306057178 + m.x6)
    **2) + m.x252 * ((-0.5198249152613603 + m.x5)**2 + (-0.07814164651753441 +
    m.x6)**2) + m.x253 * ((-0.2206544748113004 + m.x5)**2 + (
    -0.5529047264313456 + m.x6)**2) + m.x254 * ((-0.8708713492140824 + m.x5)**2
    + (-0.6958022669870113 + m.x6)**2) + m.x255 * ((-0.10823774288352628 +
    m.x5)**2 + (-0.915893092354332 + m.x6)**2) + m.x256 * ((-0.641766743884591
    + m.x5)**2 + (-0.42982985602002743 + m.x6)**2) + m.x257 * ((
    -0.769965120581223 + m.x5)**2 + (-0.4093180346858043 + m.x6)**2) + m.x258
    * ((-0.5395061655932872 + m.x5)**2 + (-0.025554298316395885 + m.x6)**2) +
    m.x259 * ((-0.07610548086145708 + m.x5)**2 + (-0.9300387630629019 + m.x6)**
    2) + m.x260 * ((-0.42188661474763056 + m.x5)**2 + (-0.7909513854242108 +
    m.x6)**2) + m.x261 * ((-0.371398443903442 + m.x5)**2 + (-0.3924282936519774
    + m.x6)**2) + m.x262 * ((-0.11106976179816641 + m.x5)**2 + (
    -0.8961539552567241 + m.x6)**2) + m.x263 * ((-0.25225491988669413 + m.x5)**
    2 + (-0.7663134725002734 + m.x6)**2) + m.x264 * ((-0.1778448829280641 +
    m.x5)**2 + (-0.3035505722762858 + m.x6)**2) + m.x265 * ((
    -0.08846844345193006 + m.x5)**2 + (-0.695683685601309 + m.x6)**2) + m.x266
    * ((-0.9178016597694366 + m.x5)**2 + (-0.627158371143039 + m.x6)**2) +
    m.x267 * ((-0.6443309388504812 + m.x5)**2 + (-0.2486686334041649 + m.x6)**2)
    + m.x268 * ((-0.9524214315197214 + m.x5)**2 + (-0.11319191562464526 + m.x6)
    **2) + m.x269 * ((-0.2503629075652184 + m.x5)**2 + (-0.5661083721487875 +
    m.x6)**2) + m.x270 * ((-0.6399923314007278 + m.x5)**2 + (
    -0.2871936662554734 + m.x6)**2) + m.x271 * ((-0.5909678451374885 + m.x5)**2
    + (-0.11513193031994995 + m.x6)**2) + m.x272 * ((-0.04877753856435085 +
    m.x5)**2 + (-0.42558284132001833 + m.x6)**2) + m.x273 * ((
    -0.5769401342223824 + m.x5)**2 + (-0.882886241480543 + m.x6)**2) + m.x274
    * ((-0.46693829720314983 + m.x5)**2 + (-0.9356416589786831 + m.x6)**2) +
    m.x275 * ((-0.7666488385496458 + m.x5)**2 + (-0.9715298035824393 + m.x6)**2)
    + m.x276 * ((-0.7090808859061516 + m.x5)**2 + (-0.4227160317233293 + m.x6)
    **2) + m.x277 * ((-0.6362788867985969 + m.x5)**2 + (-0.6897106599456068 +
    m.x6)**2) + m.x278 * ((-0.255234369371772 + m.x5)**2 + (
    -0.17269883755498971 + m.x6)**2) + m.x279 * ((-0.32354052437441105 + m.x5)
    **2 + (-0.5414620932536305 + m.x6)**2) + m.x280 * ((-0.05061498170688461 +
    m.x5)**2 + (-0.35735103685050085 + m.x6)**2) + m.x281 * ((
    -0.14474828789786598 + m.x5)**2 + (-0.935524701349798 + m.x6)**2) + m.x282
    * ((-0.4521811868578507 + m.x5)**2 + (-0.5684301129850728 + m.x6)**2) +
    m.x283 * ((-0.1391588120468895 + m.x5)**2 + (-0.450912724117135 + m.x6)**2)
    + m.x284 * ((-0.9624575143884582 + m.x5)**2 + (-0.8342971742225577 + m.x6)
    **2) + m.x285 * ((-0.9119608671435646 + m.x5)**2 + (-0.16311646954688963 +
    m.x6)**2) + m.x286 * ((-0.8601502139251708 + m.x5)**2 + (
    -0.8094641566594614 + m.x6)**2) + m.x287 * ((-0.3789359642178741 + m.x5)**2
    + (-0.34458507559213336 + m.x6)**2) + m.x288 * ((-0.9114125110384265 +
    m.x5)**2 + (-0.30087502888988404 + m.x6)**2) + m.x289 * ((
    -0.26441815851376227 + m.x5)**2 + (-0.6432639278749842 + m.x6)**2) + m.x290
    * ((-0.5040138219051838 + m.x5)**2 + (-0.436711978156451 + m.x6)**2) +
    m.x291 * ((-0.42408540833910613 + m.x5)**2 + (-0.7144533169040485 + m.x6)**
    2) + m.x292 * ((-0.7222403067943077 + m.x5)**2 + (-0.44905804057404974 +
    m.x6)**2) + m.x293 * ((-0.9396234683501675 + m.x5)**2 + (
    -0.26913749666376663 + m.x6)**2) + m.x294 * ((-0.2790684514984879 + m.x5)**
    2 + (-0.38848808536128043 + m.x6)**2) + m.x295 * ((-0.0023428037609517505
    + m.x5)**2 + (-0.5050951718570706 + m.x6)**2) + m.x296 * ((
    -0.4770114774545686 + m.x5)**2 + (-0.2671796475851538 + m.x6)**2) + m.x297
    * ((-0.4508813622466006 + m.x5)**2 + (-0.4772479476478516 + m.x6)**2) +
    m.x298 * ((-0.5802987597800233 + m.x5)**2 + (-0.5447533523575115 + m.x6)**2)
    + m.x299 * ((-0.3417733382726399 + m.x5)**2 + (-0.36547565910865576 + m.x6)
    **2) + m.x300 * ((-0.8660746835055481 + m.x5)**2 + (-0.06852013071726426 +
    m.x6)**2) + m.x301 * ((-0.8912654289001969 + m.x5)**2 + (
    -0.13480953224510595 + m.x6)**2) + m.x302 * ((-0.1717093974981898 + m.x5)**
    2 + (-0.4333331682797753 + m.x6)**2) + m.x303 * ((-0.9880935005856811 +
    m.x5)**2 + (-0.22149623450972045 + m.x6)**2) + m.x304 * ((
    -0.05074359135359818 + m.x5)**2 + (-0.7593065812217639 + m.x6)**2) + m.x305
    * ((-0.5089474327061579 + m.x5)**2 + (-0.13233399599992335 + m.x6)**2) +
    m.x306 * ((-0.8898331485351556 + m.x5)**2 + (-0.5844278795567586 + m.x6)**2))


    m.e1 = Constraint(expr= m.x7 + m.x107 + m.x207 == 1)
m.e2 = Constraint(expr= m.x8 + m.x108 + m.x208 == 1)
m.e3 = Constraint(expr= m.x9 + m.x109 + m.x209 == 1)
m.e4 = Constraint(expr= m.x10 + m.x110 + m.x210 == 1)
m.e5 = Constraint(expr= m.x11 + m.x111 + m.x211 == 1)
m.e6 = Constraint(expr= m.x12 + m.x112 + m.x212 == 1)
m.e7 = Constraint(expr= m.x13 + m.x113 + m.x213 == 1)
m.e8 = Constraint(expr= m.x14 + m.x114 + m.x214 == 1)
m.e9 = Constraint(expr= m.x15 + m.x115 + m.x215 == 1)
m.e10 = Constraint(expr= m.x16 + m.x116 + m.x216 == 1)
m.e11 = Constraint(expr= m.x17 + m.x117 + m.x217 == 1)
m.e12 = Constraint(expr= m.x18 + m.x118 + m.x218 == 1)
m.e13 = Constraint(expr= m.x19 + m.x119 + m.x219 == 1)
m.e14 = Constraint(expr= m.x20 + m.x120 + m.x220 == 1)
m.e15 = Constraint(expr= m.x21 + m.x121 + m.x221 == 1)
m.e16 = Constraint(expr= m.x22 + m.x122 + m.x222 == 1)
m.e17 = Constraint(expr= m.x23 + m.x123 + m.x223 == 1)
m.e18 = Constraint(expr= m.x24 + m.x124 + m.x224 == 1)
m.e19 = Constraint(expr= m.x25 + m.x125 + m.x225 == 1)
m.e20 = Constraint(expr= m.x26 + m.x126 + m.x226 == 1)
m.e21 = Constraint(expr= m.x27 + m.x127 + m.x227 == 1)
m.e22 = Constraint(expr= m.x28 + m.x128 + m.x228 == 1)
m.e23 = Constraint(expr= m.x29 + m.x129 + m.x229 == 1)
m.e24 = Constraint(expr= m.x30 + m.x130 + m.x230 == 1)
m.e25 = Constraint(expr= m.x31 + m.x131 + m.x231 == 1)
m.e26 = Constraint(expr= m.x32 + m.x132 + m.x232 == 1)
m.e27 = Constraint(expr= m.x33 + m.x133 + m.x233 == 1)
m.e28 = Constraint(expr= m.x34 + m.x134 + m.x234 == 1)
m.e29 = Constraint(expr= m.x35 + m.x135 + m.x235 == 1)
m.e30 = Constraint(expr= m.x36 + m.x136 + m.x236 == 1)
m.e31 = Constraint(expr= m.x37 + m.x137 + m.x237 == 1)
m.e32 = Constraint(expr= m.x38 + m.x138 + m.x238 == 1)
m.e33 = Constraint(expr= m.x39 + m.x139 + m.x239 == 1)
m.e34 = Constraint(expr= m.x40 + m.x140 + m.x240 == 1)
m.e35 = Constraint(expr= m.x41 + m.x141 + m.x241 == 1)
m.e36 = Constraint(expr= m.x42 + m.x142 + m.x242 == 1)
m.e37 = Constraint(expr= m.x43 + m.x143 + m.x243 == 1)
m.e38 = Constraint(expr= m.x44 + m.x144 + m.x244 == 1)
m.e39 = Constraint(expr= m.x45 + m.x145 + m.x245 == 1)
m.e40 = Constraint(expr= m.x46 + m.x146 + m.x246 == 1)
m.e41 = Constraint(expr= m.x47 + m.x147 + m.x247 == 1)
m.e42 = Constraint(expr= m.x48 + m.x148 + m.x248 == 1)
m.e43 = Constraint(expr= m.x49 + m.x149 + m.x249 == 1)
m.e44 = Constraint(expr= m.x50 + m.x150 + m.x250 == 1)
m.e45 = Constraint(expr= m.x51 + m.x151 + m.x251 == 1)
m.e46 = Constraint(expr= m.x52 + m.x152 + m.x252 == 1)
m.e47 = Constraint(expr= m.x53 + m.x153 + m.x253 == 1)
m.e48 = Constraint(expr= m.x54 + m.x154 + m.x254 == 1)
m.e49 = Constraint(expr= m.x55 + m.x155 + m.x255 == 1)
m.e50 = Constraint(expr= m.x56 + m.x156 + m.x256 == 1)
m.e51 = Constraint(expr= m.x57 + m.x157 + m.x257 == 1)
m.e52 = Constraint(expr= m.x58 + m.x158 + m.x258 == 1)
m.e53 = Constraint(expr= m.x59 + m.x159 + m.x259 == 1)
m.e54 = Constraint(expr= m.x60 + m.x160 + m.x260 == 1)
m.e55 = Constraint(expr= m.x61 + m.x161 + m.x261 == 1)
m.e56 = Constraint(expr= m.x62 + m.x162 + m.x262 == 1)
m.e57 = Constraint(expr= m.x63 + m.x163 + m.x263 == 1)
m.e58 = Constraint(expr= m.x64 + m.x164 + m.x264 == 1)
m.e59 = Constraint(expr= m.x65 + m.x165 + m.x265 == 1)
m.e60 = Constraint(expr= m.x66 + m.x166 + m.x266 == 1)
m.e61 = Constraint(expr= m.x67 + m.x167 + m.x267 == 1)
m.e62 = Constraint(expr= m.x68 + m.x168 + m.x268 == 1)
m.e63 = Constraint(expr= m.x69 + m.x169 + m.x269 == 1)
m.e64 = Constraint(expr= m.x70 + m.x170 + m.x270 == 1)
m.e65 = Constraint(expr= m.x71 + m.x171 + m.x271 == 1)
m.e66 = Constraint(expr= m.x72 + m.x172 + m.x272 == 1)
m.e67 = Constraint(expr= m.x73 + m.x173 + m.x273 == 1)
m.e68 = Constraint(expr= m.x74 + m.x174 + m.x274 == 1)
m.e69 = Constraint(expr= m.x75 + m.x175 + m.x275 == 1)
m.e70 = Constraint(expr= m.x76 + m.x176 + m.x276 == 1)
m.e71 = Constraint(expr= m.x77 + m.x177 + m.x277 == 1)
m.e72 = Constraint(expr= m.x78 + m.x178 + m.x278 == 1)
m.e73 = Constraint(expr= m.x79 + m.x179 + m.x279 == 1)
m.e74 = Constraint(expr= m.x80 + m.x180 + m.x280 == 1)
m.e75 = Constraint(expr= m.x81 + m.x181 + m.x281 == 1)
m.e76 = Constraint(expr= m.x82 + m.x182 + m.x282 == 1)
m.e77 = Constraint(expr= m.x83 + m.x183 + m.x283 == 1)
m.e78 = Constraint(expr= m.x84 + m.x184 + m.x284 == 1)
m.e79 = Constraint(expr= m.x85 + m.x185 + m.x285 == 1)
m.e80 = Constraint(expr= m.x86 + m.x186 + m.x286 == 1)
m.e81 = Constraint(expr= m.x87 + m.x187 + m.x287 == 1)
m.e82 = Constraint(expr= m.x88 + m.x188 + m.x288 == 1)
m.e83 = Constraint(expr= m.x89 + m.x189 + m.x289 == 1)
m.e84 = Constraint(expr= m.x90 + m.x190 + m.x290 == 1)
m.e85 = Constraint(expr= m.x91 + m.x191 + m.x291 == 1)
m.e86 = Constraint(expr= m.x92 + m.x192 + m.x292 == 1)
m.e87 = Constraint(expr= m.x93 + m.x193 + m.x293 == 1)
m.e88 = Constraint(expr= m.x94 + m.x194 + m.x294 == 1)
m.e89 = Constraint(expr= m.x95 + m.x195 + m.x295 == 1)
m.e90 = Constraint(expr= m.x96 + m.x196 + m.x296 == 1)
m.e91 = Constraint(expr= m.x97 + m.x197 + m.x297 == 1)
m.e92 = Constraint(expr= m.x98 + m.x198 + m.x298 == 1)
m.e93 = Constraint(expr= m.x99 + m.x199 + m.x299 == 1)
m.e94 = Constraint(expr= m.x100 + m.x200 + m.x300 == 1)
m.e95 = Constraint(expr= m.x101 + m.x201 + m.x301 == 1)
m.e96 = Constraint(expr= m.x102 + m.x202 + m.x302 == 1)
m.e97 = Constraint(expr= m.x103 + m.x203 + m.x303 == 1)
m.e98 = Constraint(expr= m.x104 + m.x204 + m.x304 == 1)
m.e99 = Constraint(expr= m.x105 + m.x205 + m.x305 == 1)
m.e100 = Constraint(expr= m.x106 + m.x206 + m.x306 == 1)
