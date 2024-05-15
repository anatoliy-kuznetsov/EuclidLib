# NLP written by GAMS Convert at 05/15/24 11:43:15
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       100      100        0        0        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#       515      515        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       500      500        0
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
m.x307 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x308 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x309 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x310 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x311 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x312 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x313 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x314 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x315 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x316 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x317 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x318 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x319 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x320 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x321 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x322 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x323 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x324 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x325 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x326 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x327 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x328 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x329 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x330 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x331 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x332 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x333 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x334 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x335 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x336 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x337 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x338 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x339 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x340 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x341 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x342 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x343 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x344 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x345 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x346 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x347 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x348 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x349 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x350 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x351 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x352 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x353 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x354 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x355 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x356 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x357 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x358 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x359 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x360 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x361 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x362 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x363 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x364 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x365 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x366 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x367 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x368 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x369 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x370 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x371 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x372 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x373 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x374 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x375 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x376 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x377 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x378 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x379 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x380 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x381 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x382 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x383 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x384 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x385 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x386 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x387 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x388 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x389 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x390 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x391 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x392 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x393 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x394 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x395 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x396 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x397 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x398 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x399 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x400 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x401 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x402 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x403 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x404 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x405 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x406 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x407 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x408 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x409 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x410 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x411 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x412 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x413 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x414 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x415 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x416 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x417 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x418 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x419 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x420 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x421 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x422 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x423 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x424 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x425 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x426 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x427 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x428 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x429 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x430 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x431 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x432 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x433 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x434 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x435 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x436 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x437 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x438 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x439 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x440 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x441 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x442 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x443 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x444 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x445 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x446 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x447 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x448 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x449 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x450 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x451 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x452 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x453 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x454 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x455 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x456 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x457 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x458 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x459 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x460 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x461 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x462 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x463 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x464 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x465 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x466 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x467 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x468 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x469 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x470 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x471 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x472 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x473 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x474 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x475 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x476 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x477 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x478 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x479 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x480 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x481 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x482 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x483 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x484 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x485 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x486 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x487 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x488 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x489 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x490 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x491 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x492 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x493 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x494 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x495 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x496 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x497 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x498 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x499 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x500 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x501 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x502 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x503 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x504 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x505 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x506 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x507 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x508 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x509 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x510 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x511 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x512 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x513 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x514 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x515 = Var(within=Reals, bounds=(0,1), initialize=0)

m.obj = Objective(sense=minimize, expr= m.x16 * ((-0.182590973189231 + m.x1)**2
    + (-0.5665714918882914 + m.x2)**2 + (-0.6312292714676417 + m.x3)**2) +
    m.x17 * ((-0.2832671889632007 + m.x1)**2 + (-0.17321967122047943 + m.x2)**2
    + (-0.7759213801035818 + m.x3)**2) + m.x18 * ((-0.6166835514333678 + m.x1)
    **2 + (-0.18472992234217067 + m.x2)**2 + (-0.5668962918559568 + m.x3)**2)
    + m.x19 * ((-0.6928413524617497 + m.x1)**2 + (-0.7010280503630747 + m.x2)
    **2 + (-0.8235168163439104 + m.x3)**2) + m.x20 * ((-0.9521446875464642 +
    m.x1)**2 + (-0.6827797104282454 + m.x2)**2 + (-0.9742345929865083 + m.x3)**
    2) + m.x21 * ((-0.49339806451491164 + m.x1)**2 + (-0.2601889128277658 +
    m.x2)**2 + (-0.9240562933514055 + m.x3)**2) + m.x22 * ((-0.2671371624959298
    + m.x1)**2 + (-0.14765536014617142 + m.x2)**2 + (-0.1308517721620952 +
    m.x3)**2) + m.x23 * ((-0.5387635518822207 + m.x1)**2 + (-0.9091794865893283
    + m.x2)**2 + (-0.35329464443498004 + m.x3)**2) + m.x24 * ((
    -0.9543934932393079 + m.x1)**2 + (-0.8829919769976778 + m.x2)**2 + (
    -0.24953811957625105 + m.x3)**2) + m.x25 * ((-0.49673865851653387 + m.x1)**
    2 + (-0.5915750015273571 + m.x2)**2 + (-0.6540508311901382 + m.x3)**2) +
    m.x26 * ((-0.6851778848421465 + m.x1)**2 + (-0.06546979118233476 + m.x2)**2
    + (-0.6973311320502895 + m.x3)**2) + m.x27 * ((-0.16455684099822276 + m.x1)
    **2 + (-0.4945110210794651 + m.x2)**2 + (-0.5302168748506974 + m.x3)**2) +
    m.x28 * ((-0.10845237413301334 + m.x1)**2 + (-0.640284214221513 + m.x2)**2
    + (-0.5696805351079286 + m.x3)**2) + m.x29 * ((-0.23716596315745875 + m.x1)
    **2 + (-0.7582428735081286 + m.x2)**2 + (-0.14219912975075677 + m.x3)**2)
    + m.x30 * ((-0.9234692794617353 + m.x1)**2 + (-0.0778901924184836 + m.x2)
    **2 + (-0.8075967020017696 + m.x3)**2) + m.x31 * ((-0.540866816090371 +
    m.x1)**2 + (-0.14399747110118288 + m.x2)**2 + (-0.27481763904074175 + m.x3)
    **2) + m.x32 * ((-0.9668344449551666 + m.x1)**2 + (-0.6728169766961944 +
    m.x2)**2 + (-0.5957407662223678 + m.x3)**2) + m.x33 * ((-0.7078504643054941
    + m.x1)**2 + (-0.15971028625085149 + m.x2)**2 + (-0.5302963826027993 +
    m.x3)**2) + m.x34 * ((-0.8837023252340255 + m.x1)**2 + (
    -0.29928440722639893 + m.x2)**2 + (-0.44169026690300495 + m.x3)**2) + m.x35
    * ((-0.9988349888534216 + m.x1)**2 + (-0.9108542073862229 + m.x2)**2 + (
    -0.3076571036413186 + m.x3)**2) + m.x36 * ((-0.9347820308317397 + m.x1)**2
    + (-0.008277334533312586 + m.x2)**2 + (-0.5493915389372619 + m.x3)**2) +
    m.x37 * ((-0.8463388658403949 + m.x1)**2 + (-0.7189544434255234 + m.x2)**2
    + (-0.6058316717442289 + m.x3)**2) + m.x38 * ((-0.28002015412253 + m.x1)**
    2 + (-0.9634485414492736 + m.x2)**2 + (-0.5628416900899014 + m.x3)**2) +
    m.x39 * ((-0.9058009322708488 + m.x1)**2 + (-0.9215478966214675 + m.x2)**2
    + (-0.693970532541882 + m.x3)**2) + m.x40 * ((-0.48234013355525474 + m.x1)
    **2 + (-0.6704565562300323 + m.x2)**2 + (-0.17108667007034573 + m.x3)**2)
    + m.x41 * ((-0.35039670467264805 + m.x1)**2 + (-0.9730227072363548 + m.x2)
    **2 + (-0.16164836217963152 + m.x3)**2) + m.x42 * ((-0.032853727849101344
    + m.x1)**2 + (-0.8972914472060697 + m.x2)**2 + (-0.5002344554243207 + m.x3)
    **2) + m.x43 * ((-0.2788175585600441 + m.x1)**2 + (-0.925751731057649 +
    m.x2)**2 + (-0.7670404625118962 + m.x3)**2) + m.x44 * ((-0.4497791511222945
    + m.x1)**2 + (-0.48620903327713016 + m.x2)**2 + (-0.3154941664955949 +
    m.x3)**2) + m.x45 * ((-0.479795503546542 + m.x1)**2 + (-0.6708482470175294
    + m.x2)**2 + (-0.6732217870137864 + m.x3)**2) + m.x46 * ((
    -0.3124285024815808 + m.x1)**2 + (-0.9048786174799557 + m.x2)**2 + (
    -0.07517130917071779 + m.x3)**2) + m.x47 * ((-0.9758976938691616 + m.x1)**2
    + (-0.7548191430644975 + m.x2)**2 + (-0.17206520112879609 + m.x3)**2) +
    m.x48 * ((-0.7014387290695361 + m.x1)**2 + (-0.9629369136587164 + m.x2)**2
    + (-0.6705450578414445 + m.x3)**2) + m.x49 * ((-0.4008827939787283 + m.x1)
    **2 + (-0.827645026992737 + m.x2)**2 + (-0.5996187050142987 + m.x3)**2) +
    m.x50 * ((-0.7695006716313056 + m.x1)**2 + (-0.0304732644411716 + m.x2)**2
    + (-0.43726762258665086 + m.x3)**2) + m.x51 * ((-0.8536091145712932 + m.x1)
    **2 + (-0.47221565503791474 + m.x2)**2 + (-0.9530780172694218 + m.x3)**2)
    + m.x52 * ((-0.5188203591441234 + m.x1)**2 + (-0.1281672582217266 + m.x2)
    **2 + (-0.6943094553894391 + m.x3)**2) + m.x53 * ((-0.08010782288058038 +
    m.x1)**2 + (-0.24152490637399082 + m.x2)**2 + (-0.8281358660983907 + m.x3)
    **2) + m.x54 * ((-0.6421940815386412 + m.x1)**2 + (-0.12649912077368797 +
    m.x2)**2 + (-0.02816586075065286 + m.x3)**2) + m.x55 * ((
    -0.49834091606095776 + m.x1)**2 + (-0.05385179230503356 + m.x2)**2 + (
    -0.16649560036120326 + m.x3)**2) + m.x56 * ((-0.44749939041222264 + m.x1)**
    2 + (-0.38094481309529127 + m.x2)**2 + (-0.4244480931198653 + m.x3)**2) +
    m.x57 * ((-0.6615144607793271 + m.x1)**2 + (-0.28647547516475624 + m.x2)**2
    + (-0.5938317138915002 + m.x3)**2) + m.x58 * ((-0.16412983035791717 + m.x1)
    **2 + (-0.7315916404115455 + m.x2)**2 + (-0.7945041523159543 + m.x3)**2) +
    m.x59 * ((-0.8406929484324254 + m.x1)**2 + (-0.1768935596158654 + m.x2)**2
    + (-0.9610393111972642 + m.x3)**2) + m.x60 * ((-0.7568320576996023 + m.x1)
    **2 + (-0.8546272679432373 + m.x2)**2 + (-0.47261297066126495 + m.x3)**2)
    + m.x61 * ((-0.6482257394415872 + m.x1)**2 + (-0.07605513871045355 + m.x2)
    **2 + (-0.9632360437660454 + m.x3)**2) + m.x62 * ((-0.04709405204952222 +
    m.x1)**2 + (-0.485851180307163 + m.x2)**2 + (-0.2023313958130618 + m.x3)**2)
    + m.x63 * ((-0.9943387951600927 + m.x1)**2 + (-0.561661529271997 + m.x2)**
    2 + (-0.41120790568861443 + m.x3)**2) + m.x64 * ((-0.5689039680629383 +
    m.x1)**2 + (-0.7331999848252405 + m.x2)**2 + (-0.06524623840128607 + m.x3)
    **2) + m.x65 * ((-0.3157591979227248 + m.x1)**2 + (-0.36032648332547135 +
    m.x2)**2 + (-0.6231552244780812 + m.x3)**2) + m.x66 * ((
    -0.09241374392362178 + m.x1)**2 + (-0.6343499642335877 + m.x2)**2 + (
    -0.4649079471250238 + m.x3)**2) + m.x67 * ((-0.688999295800091 + m.x1)**2
    + (-0.41235973103252466 + m.x2)**2 + (-0.06858188095070694 + m.x3)**2) +
    m.x68 * ((-0.5368752167875853 + m.x1)**2 + (-0.07061782991482157 + m.x2)**2
    + (-0.3905327318657953 + m.x3)**2) + m.x69 * ((-0.09236084144989976 + m.x1)
    **2 + (-0.8966749133315102 + m.x2)**2 + (-0.6119569273762655 + m.x3)**2) +
    m.x70 * ((-0.36671410401176074 + m.x1)**2 + (-0.22867661994729294 + m.x2)**
    2 + (-0.34205809393406117 + m.x3)**2) + m.x71 * ((-0.2884689151866864 +
    m.x1)**2 + (-0.8245188787565171 + m.x2)**2 + (-0.5471817452899417 + m.x3)**
    2) + m.x72 * ((-0.3095681539176819 + m.x1)**2 + (-0.24650073053553823 +
    m.x2)**2 + (-0.7075429829955994 + m.x3)**2) + m.x73 * ((
    -0.24085416793099568 + m.x1)**2 + (-0.9209114031548099 + m.x2)**2 + (
    -0.7121452348711909 + m.x3)**2) + m.x74 * ((-0.6097813059476557 + m.x1)**2
    + (-0.13509746247515075 + m.x2)**2 + (-0.9576415267519117 + m.x3)**2) +
    m.x75 * ((-0.39311391559059083 + m.x1)**2 + (-0.6802374509278515 + m.x2)**2
    + (-0.8564222091336956 + m.x3)**2) + m.x76 * ((-0.9189964545477477 + m.x1)
    **2 + (-0.26148532247210654 + m.x2)**2 + (-0.9509249567269127 + m.x3)**2)
    + m.x77 * ((-0.02208444426023015 + m.x1)**2 + (-0.1576091196577002 + m.x2)
    **2 + (-0.7074191023951775 + m.x3)**2) + m.x78 * ((-0.650480284651522 +
    m.x1)**2 + (-0.9428001755748773 + m.x2)**2 + (-0.12491415562242869 + m.x3)
    **2) + m.x79 * ((-0.2619140159334036 + m.x1)**2 + (-0.1777418278918652 +
    m.x2)**2 + (-0.3249343841798372 + m.x3)**2) + m.x80 * ((
    -0.012299809392943395 + m.x1)**2 + (-0.4826364643146488 + m.x2)**2 + (
    -0.877608971013956 + m.x3)**2) + m.x81 * ((-0.9278995012468446 + m.x1)**2
    + (-0.29658116106747157 + m.x2)**2 + (-0.4139069448025193 + m.x3)**2) +
    m.x82 * ((-0.1783104387827067 + m.x1)**2 + (-0.523247944850848 + m.x2)**2
    + (-0.7592637122950673 + m.x3)**2) + m.x83 * ((-0.6885309028690637 + m.x1)
    **2 + (-0.069836660702157 + m.x2)**2 + (-0.27844283434957473 + m.x3)**2) +
    m.x84 * ((-0.3628069626450744 + m.x1)**2 + (-0.4524112032480545 + m.x2)**2
    + (-0.9091077636574432 + m.x3)**2) + m.x85 * ((-0.19545965240891594 + m.x1)
    **2 + (-0.8349228826970087 + m.x2)**2 + (-0.2600240764929378 + m.x3)**2) +
    m.x86 * ((-0.8136957237985446 + m.x1)**2 + (-0.8440312039370582 + m.x2)**2
    + (-0.18657993159673503 + m.x3)**2) + m.x87 * ((-0.7332761233575051 + m.x1)
    **2 + (-0.9938264339064263 + m.x2)**2 + (-0.848810907941449 + m.x3)**2) +
    m.x88 * ((-0.6625468543751725 + m.x1)**2 + (-0.8649355655149289 + m.x2)**2
    + (-0.5267141542502073 + m.x3)**2) + m.x89 * ((-0.4152755489969038 + m.x1)
    **2 + (-0.8771524784813198 + m.x2)**2 + (-0.30733079492573634 + m.x3)**2)
    + m.x90 * ((-0.35755808475562567 + m.x1)**2 + (-0.949115491768236 + m.x2)
    **2 + (-0.15156928782779888 + m.x3)**2) + m.x91 * ((-0.5058696724084709 +
    m.x1)**2 + (-0.6421669787387695 + m.x2)**2 + (-0.2704977371827102 + m.x3)**
    2) + m.x92 * ((-0.02314501086665055 + m.x1)**2 + (-0.797073612921973 + m.x2)
    **2 + (-0.6718295177964552 + m.x3)**2) + m.x93 * ((-0.6674227026324897 +
    m.x1)**2 + (-0.28533905171646934 + m.x2)**2 + (-0.6530875341797157 + m.x3)
    **2) + m.x94 * ((-0.49802163179869985 + m.x1)**2 + (-0.9159175310463538 +
    m.x2)**2 + (-0.8511170311594338 + m.x3)**2) + m.x95 * ((-0.921121885282289
    + m.x1)**2 + (-0.29110498439296717 + m.x2)**2 + (-0.07095961947687046 +
    m.x3)**2) + m.x96 * ((-0.5066223599150115 + m.x1)**2 + (-0.8365869947893311
    + m.x2)**2 + (-0.37136067431457864 + m.x3)**2) + m.x97 * ((
    -0.7282642906004309 + m.x1)**2 + (-0.8076127746397918 + m.x2)**2 + (
    -0.23700100631040355 + m.x3)**2) + m.x98 * ((-0.17793281956808304 + m.x1)**
    2 + (-0.8729572789960333 + m.x2)**2 + (-0.17550679028027727 + m.x3)**2) +
    m.x99 * ((-0.28160869151209356 + m.x1)**2 + (-0.21027420689223564 + m.x2)**
    2 + (-0.5801863384871276 + m.x3)**2) + m.x100 * ((-0.703680099800644 + m.x1)
    **2 + (-0.7954020654414685 + m.x2)**2 + (-0.037273161155704004 + m.x3)**2)
    + m.x101 * ((-0.8494522028293213 + m.x1)**2 + (-0.6755785367429551 + m.x2)
    **2 + (-0.3545484132724107 + m.x3)**2) + m.x102 * ((-0.38765300434187966 +
    m.x1)**2 + (-0.3029441042054243 + m.x2)**2 + (-0.9073082164213291 + m.x3)**
    2) + m.x103 * ((-0.8478833426449218 + m.x1)**2 + (-0.5190242383318947 +
    m.x2)**2 + (-0.890475723079222 + m.x3)**2) + m.x104 * ((
    -0.08526574189471425 + m.x1)**2 + (-0.08433063147801656 + m.x2)**2 + (
    -0.34038923400741616 + m.x3)**2) + m.x105 * ((-0.3819102188291116 + m.x1)**
    2 + (-0.368719462749436 + m.x2)**2 + (-0.5059825484936955 + m.x3)**2) +
    m.x106 * ((-0.7491328863462429 + m.x1)**2 + (-0.4007415312530962 + m.x2)**2
    + (-0.8795211427493239 + m.x3)**2) + m.x107 * ((-0.7741279705885629 + m.x1)
    **2 + (-0.8856116737594064 + m.x2)**2 + (-0.2651355164571192 + m.x3)**2) +
    m.x108 * ((-0.9047294977974201 + m.x1)**2 + (-0.7357904800445998 + m.x2)**2
    + (-0.2819553446129277 + m.x3)**2) + m.x109 * ((-0.7274677561703813 + m.x1)
    **2 + (-0.6080547644274223 + m.x2)**2 + (-0.4688320743625637 + m.x3)**2) +
    m.x110 * ((-0.2549577045934236 + m.x1)**2 + (-0.11411488345784182 + m.x2)**
    2 + (-0.22595928823071643 + m.x3)**2) + m.x111 * ((-0.9849257452304463 +
    m.x1)**2 + (-0.9402085696377348 + m.x2)**2 + (-0.41737974889498053 + m.x3)
    **2) + m.x112 * ((-0.3062096299151559 + m.x1)**2 + (-0.5781338903934966 +
    m.x2)**2 + (-0.5836695539809419 + m.x3)**2) + m.x113 * ((
    -0.6555223295998597 + m.x1)**2 + (-0.11627198084637425 + m.x2)**2 + (
    -0.5340643666314074 + m.x3)**2) + m.x114 * ((-0.8167955181907369 + m.x1)**2
    + (-0.6648304662656255 + m.x2)**2 + (-0.4344445572683132 + m.x3)**2) +
    m.x115 * ((-0.2627634068526804 + m.x1)**2 + (-0.8719643810841551 + m.x2)**2
    + (-0.2782753479255554 + m.x3)**2) + m.x116 * ((-0.182590973189231 + m.x4)
    **2 + (-0.5665714918882914 + m.x5)**2 + (-0.6312292714676417 + m.x6)**2) +
    m.x117 * ((-0.2832671889632007 + m.x4)**2 + (-0.17321967122047943 + m.x5)**
    2 + (-0.7759213801035818 + m.x6)**2) + m.x118 * ((-0.6166835514333678 +
    m.x4)**2 + (-0.18472992234217067 + m.x5)**2 + (-0.5668962918559568 + m.x6)
    **2) + m.x119 * ((-0.6928413524617497 + m.x4)**2 + (-0.7010280503630747 +
    m.x5)**2 + (-0.8235168163439104 + m.x6)**2) + m.x120 * ((
    -0.9521446875464642 + m.x4)**2 + (-0.6827797104282454 + m.x5)**2 + (
    -0.9742345929865083 + m.x6)**2) + m.x121 * ((-0.49339806451491164 + m.x4)**
    2 + (-0.2601889128277658 + m.x5)**2 + (-0.9240562933514055 + m.x6)**2) +
    m.x122 * ((-0.2671371624959298 + m.x4)**2 + (-0.14765536014617142 + m.x5)**
    2 + (-0.1308517721620952 + m.x6)**2) + m.x123 * ((-0.5387635518822207 +
    m.x4)**2 + (-0.9091794865893283 + m.x5)**2 + (-0.35329464443498004 + m.x6)
    **2) + m.x124 * ((-0.9543934932393079 + m.x4)**2 + (-0.8829919769976778 +
    m.x5)**2 + (-0.24953811957625105 + m.x6)**2) + m.x125 * ((
    -0.49673865851653387 + m.x4)**2 + (-0.5915750015273571 + m.x5)**2 + (
    -0.6540508311901382 + m.x6)**2) + m.x126 * ((-0.6851778848421465 + m.x4)**2
    + (-0.06546979118233476 + m.x5)**2 + (-0.6973311320502895 + m.x6)**2) +
    m.x127 * ((-0.16455684099822276 + m.x4)**2 + (-0.4945110210794651 + m.x5)**
    2 + (-0.5302168748506974 + m.x6)**2) + m.x128 * ((-0.10845237413301334 +
    m.x4)**2 + (-0.640284214221513 + m.x5)**2 + (-0.5696805351079286 + m.x6)**2)
    + m.x129 * ((-0.23716596315745875 + m.x4)**2 + (-0.7582428735081286 + m.x5)
    **2 + (-0.14219912975075677 + m.x6)**2) + m.x130 * ((-0.9234692794617353 +
    m.x4)**2 + (-0.0778901924184836 + m.x5)**2 + (-0.8075967020017696 + m.x6)**
    2) + m.x131 * ((-0.540866816090371 + m.x4)**2 + (-0.14399747110118288 +
    m.x5)**2 + (-0.27481763904074175 + m.x6)**2) + m.x132 * ((
    -0.9668344449551666 + m.x4)**2 + (-0.6728169766961944 + m.x5)**2 + (
    -0.5957407662223678 + m.x6)**2) + m.x133 * ((-0.7078504643054941 + m.x4)**2
    + (-0.15971028625085149 + m.x5)**2 + (-0.5302963826027993 + m.x6)**2) +
    m.x134 * ((-0.8837023252340255 + m.x4)**2 + (-0.29928440722639893 + m.x5)**
    2 + (-0.44169026690300495 + m.x6)**2) + m.x135 * ((-0.9988349888534216 +
    m.x4)**2 + (-0.9108542073862229 + m.x5)**2 + (-0.3076571036413186 + m.x6)**
    2) + m.x136 * ((-0.9347820308317397 + m.x4)**2 + (-0.008277334533312586 +
    m.x5)**2 + (-0.5493915389372619 + m.x6)**2) + m.x137 * ((
    -0.8463388658403949 + m.x4)**2 + (-0.7189544434255234 + m.x5)**2 + (
    -0.6058316717442289 + m.x6)**2) + m.x138 * ((-0.28002015412253 + m.x4)**2
    + (-0.9634485414492736 + m.x5)**2 + (-0.5628416900899014 + m.x6)**2) +
    m.x139 * ((-0.9058009322708488 + m.x4)**2 + (-0.9215478966214675 + m.x5)**2
    + (-0.693970532541882 + m.x6)**2) + m.x140 * ((-0.48234013355525474 + m.x4)
    **2 + (-0.6704565562300323 + m.x5)**2 + (-0.17108667007034573 + m.x6)**2)
    + m.x141 * ((-0.35039670467264805 + m.x4)**2 + (-0.9730227072363548 + m.x5)
    **2 + (-0.16164836217963152 + m.x6)**2) + m.x142 * ((-0.032853727849101344
    + m.x4)**2 + (-0.8972914472060697 + m.x5)**2 + (-0.5002344554243207 + m.x6)
    **2) + m.x143 * ((-0.2788175585600441 + m.x4)**2 + (-0.925751731057649 +
    m.x5)**2 + (-0.7670404625118962 + m.x6)**2) + m.x144 * ((
    -0.4497791511222945 + m.x4)**2 + (-0.48620903327713016 + m.x5)**2 + (
    -0.3154941664955949 + m.x6)**2) + m.x145 * ((-0.479795503546542 + m.x4)**2
    + (-0.6708482470175294 + m.x5)**2 + (-0.6732217870137864 + m.x6)**2) +
    m.x146 * ((-0.3124285024815808 + m.x4)**2 + (-0.9048786174799557 + m.x5)**2
    + (-0.07517130917071779 + m.x6)**2) + m.x147 * ((-0.9758976938691616 +
    m.x4)**2 + (-0.7548191430644975 + m.x5)**2 + (-0.17206520112879609 + m.x6)
    **2) + m.x148 * ((-0.7014387290695361 + m.x4)**2 + (-0.9629369136587164 +
    m.x5)**2 + (-0.6705450578414445 + m.x6)**2) + m.x149 * ((
    -0.4008827939787283 + m.x4)**2 + (-0.827645026992737 + m.x5)**2 + (
    -0.5996187050142987 + m.x6)**2) + m.x150 * ((-0.7695006716313056 + m.x4)**2
    + (-0.0304732644411716 + m.x5)**2 + (-0.43726762258665086 + m.x6)**2) +
    m.x151 * ((-0.8536091145712932 + m.x4)**2 + (-0.47221565503791474 + m.x5)**
    2 + (-0.9530780172694218 + m.x6)**2) + m.x152 * ((-0.5188203591441234 +
    m.x4)**2 + (-0.1281672582217266 + m.x5)**2 + (-0.6943094553894391 + m.x6)**
    2) + m.x153 * ((-0.08010782288058038 + m.x4)**2 + (-0.24152490637399082 +
    m.x5)**2 + (-0.8281358660983907 + m.x6)**2) + m.x154 * ((
    -0.6421940815386412 + m.x4)**2 + (-0.12649912077368797 + m.x5)**2 + (
    -0.02816586075065286 + m.x6)**2) + m.x155 * ((-0.49834091606095776 + m.x4)
    **2 + (-0.05385179230503356 + m.x5)**2 + (-0.16649560036120326 + m.x6)**2)
    + m.x156 * ((-0.44749939041222264 + m.x4)**2 + (-0.38094481309529127 +
    m.x5)**2 + (-0.4244480931198653 + m.x6)**2) + m.x157 * ((
    -0.6615144607793271 + m.x4)**2 + (-0.28647547516475624 + m.x5)**2 + (
    -0.5938317138915002 + m.x6)**2) + m.x158 * ((-0.16412983035791717 + m.x4)**
    2 + (-0.7315916404115455 + m.x5)**2 + (-0.7945041523159543 + m.x6)**2) +
    m.x159 * ((-0.8406929484324254 + m.x4)**2 + (-0.1768935596158654 + m.x5)**2
    + (-0.9610393111972642 + m.x6)**2) + m.x160 * ((-0.7568320576996023 + m.x4)
    **2 + (-0.8546272679432373 + m.x5)**2 + (-0.47261297066126495 + m.x6)**2)
    + m.x161 * ((-0.6482257394415872 + m.x4)**2 + (-0.07605513871045355 + m.x5)
    **2 + (-0.9632360437660454 + m.x6)**2) + m.x162 * ((-0.04709405204952222 +
    m.x4)**2 + (-0.485851180307163 + m.x5)**2 + (-0.2023313958130618 + m.x6)**2)
    + m.x163 * ((-0.9943387951600927 + m.x4)**2 + (-0.561661529271997 + m.x5)
    **2 + (-0.41120790568861443 + m.x6)**2) + m.x164 * ((-0.5689039680629383 +
    m.x4)**2 + (-0.7331999848252405 + m.x5)**2 + (-0.06524623840128607 + m.x6)
    **2) + m.x165 * ((-0.3157591979227248 + m.x4)**2 + (-0.36032648332547135 +
    m.x5)**2 + (-0.6231552244780812 + m.x6)**2) + m.x166 * ((
    -0.09241374392362178 + m.x4)**2 + (-0.6343499642335877 + m.x5)**2 + (
    -0.4649079471250238 + m.x6)**2) + m.x167 * ((-0.688999295800091 + m.x4)**2
    + (-0.41235973103252466 + m.x5)**2 + (-0.06858188095070694 + m.x6)**2) +
    m.x168 * ((-0.5368752167875853 + m.x4)**2 + (-0.07061782991482157 + m.x5)**
    2 + (-0.3905327318657953 + m.x6)**2) + m.x169 * ((-0.09236084144989976 +
    m.x4)**2 + (-0.8966749133315102 + m.x5)**2 + (-0.6119569273762655 + m.x6)**
    2) + m.x170 * ((-0.36671410401176074 + m.x4)**2 + (-0.22867661994729294 +
    m.x5)**2 + (-0.34205809393406117 + m.x6)**2) + m.x171 * ((
    -0.2884689151866864 + m.x4)**2 + (-0.8245188787565171 + m.x5)**2 + (
    -0.5471817452899417 + m.x6)**2) + m.x172 * ((-0.3095681539176819 + m.x4)**2
    + (-0.24650073053553823 + m.x5)**2 + (-0.7075429829955994 + m.x6)**2) +
    m.x173 * ((-0.24085416793099568 + m.x4)**2 + (-0.9209114031548099 + m.x5)**
    2 + (-0.7121452348711909 + m.x6)**2) + m.x174 * ((-0.6097813059476557 +
    m.x4)**2 + (-0.13509746247515075 + m.x5)**2 + (-0.9576415267519117 + m.x6)
    **2) + m.x175 * ((-0.39311391559059083 + m.x4)**2 + (-0.6802374509278515 +
    m.x5)**2 + (-0.8564222091336956 + m.x6)**2) + m.x176 * ((
    -0.9189964545477477 + m.x4)**2 + (-0.26148532247210654 + m.x5)**2 + (
    -0.9509249567269127 + m.x6)**2) + m.x177 * ((-0.02208444426023015 + m.x4)**
    2 + (-0.1576091196577002 + m.x5)**2 + (-0.7074191023951775 + m.x6)**2) +
    m.x178 * ((-0.650480284651522 + m.x4)**2 + (-0.9428001755748773 + m.x5)**2
    + (-0.12491415562242869 + m.x6)**2) + m.x179 * ((-0.2619140159334036 +
    m.x4)**2 + (-0.1777418278918652 + m.x5)**2 + (-0.3249343841798372 + m.x6)**
    2) + m.x180 * ((-0.012299809392943395 + m.x4)**2 + (-0.4826364643146488 +
    m.x5)**2 + (-0.877608971013956 + m.x6)**2) + m.x181 * ((-0.9278995012468446
    + m.x4)**2 + (-0.29658116106747157 + m.x5)**2 + (-0.4139069448025193 +
    m.x6)**2) + m.x182 * ((-0.1783104387827067 + m.x4)**2 + (-0.523247944850848
    + m.x5)**2 + (-0.7592637122950673 + m.x6)**2) + m.x183 * ((
    -0.6885309028690637 + m.x4)**2 + (-0.069836660702157 + m.x5)**2 + (
    -0.27844283434957473 + m.x6)**2) + m.x184 * ((-0.3628069626450744 + m.x4)**
    2 + (-0.4524112032480545 + m.x5)**2 + (-0.9091077636574432 + m.x6)**2) +
    m.x185 * ((-0.19545965240891594 + m.x4)**2 + (-0.8349228826970087 + m.x5)**
    2 + (-0.2600240764929378 + m.x6)**2) + m.x186 * ((-0.8136957237985446 +
    m.x4)**2 + (-0.8440312039370582 + m.x5)**2 + (-0.18657993159673503 + m.x6)
    **2) + m.x187 * ((-0.7332761233575051 + m.x4)**2 + (-0.9938264339064263 +
    m.x5)**2 + (-0.848810907941449 + m.x6)**2) + m.x188 * ((-0.6625468543751725
    + m.x4)**2 + (-0.8649355655149289 + m.x5)**2 + (-0.5267141542502073 + m.x6)
    **2) + m.x189 * ((-0.4152755489969038 + m.x4)**2 + (-0.8771524784813198 +
    m.x5)**2 + (-0.30733079492573634 + m.x6)**2) + m.x190 * ((
    -0.35755808475562567 + m.x4)**2 + (-0.949115491768236 + m.x5)**2 + (
    -0.15156928782779888 + m.x6)**2) + m.x191 * ((-0.5058696724084709 + m.x4)**
    2 + (-0.6421669787387695 + m.x5)**2 + (-0.2704977371827102 + m.x6)**2) +
    m.x192 * ((-0.02314501086665055 + m.x4)**2 + (-0.797073612921973 + m.x5)**2
    + (-0.6718295177964552 + m.x6)**2) + m.x193 * ((-0.6674227026324897 + m.x4)
    **2 + (-0.28533905171646934 + m.x5)**2 + (-0.6530875341797157 + m.x6)**2)
    + m.x194 * ((-0.49802163179869985 + m.x4)**2 + (-0.9159175310463538 + m.x5)
    **2 + (-0.8511170311594338 + m.x6)**2) + m.x195 * ((-0.921121885282289 +
    m.x4)**2 + (-0.29110498439296717 + m.x5)**2 + (-0.07095961947687046 + m.x6)
    **2) + m.x196 * ((-0.5066223599150115 + m.x4)**2 + (-0.8365869947893311 +
    m.x5)**2 + (-0.37136067431457864 + m.x6)**2) + m.x197 * ((
    -0.7282642906004309 + m.x4)**2 + (-0.8076127746397918 + m.x5)**2 + (
    -0.23700100631040355 + m.x6)**2) + m.x198 * ((-0.17793281956808304 + m.x4)
    **2 + (-0.8729572789960333 + m.x5)**2 + (-0.17550679028027727 + m.x6)**2)
    + m.x199 * ((-0.28160869151209356 + m.x4)**2 + (-0.21027420689223564 +
    m.x5)**2 + (-0.5801863384871276 + m.x6)**2) + m.x200 * ((-0.703680099800644
    + m.x4)**2 + (-0.7954020654414685 + m.x5)**2 + (-0.037273161155704004 +
    m.x6)**2) + m.x201 * ((-0.8494522028293213 + m.x4)**2 + (
    -0.6755785367429551 + m.x5)**2 + (-0.3545484132724107 + m.x6)**2) + m.x202
    * ((-0.38765300434187966 + m.x4)**2 + (-0.3029441042054243 + m.x5)**2 + (
    -0.9073082164213291 + m.x6)**2) + m.x203 * ((-0.8478833426449218 + m.x4)**2
    + (-0.5190242383318947 + m.x5)**2 + (-0.890475723079222 + m.x6)**2) +
    m.x204 * ((-0.08526574189471425 + m.x4)**2 + (-0.08433063147801656 + m.x5)
    **2 + (-0.34038923400741616 + m.x6)**2) + m.x205 * ((-0.3819102188291116 +
    m.x4)**2 + (-0.368719462749436 + m.x5)**2 + (-0.5059825484936955 + m.x6)**2)
    + m.x206 * ((-0.7491328863462429 + m.x4)**2 + (-0.4007415312530962 + m.x5)
    **2 + (-0.8795211427493239 + m.x6)**2) + m.x207 * ((-0.7741279705885629 +
    m.x4)**2 + (-0.8856116737594064 + m.x5)**2 + (-0.2651355164571192 + m.x6)**
    2) + m.x208 * ((-0.9047294977974201 + m.x4)**2 + (-0.7357904800445998 +
    m.x5)**2 + (-0.2819553446129277 + m.x6)**2) + m.x209 * ((
    -0.7274677561703813 + m.x4)**2 + (-0.6080547644274223 + m.x5)**2 + (
    -0.4688320743625637 + m.x6)**2) + m.x210 * ((-0.2549577045934236 + m.x4)**2
    + (-0.11411488345784182 + m.x5)**2 + (-0.22595928823071643 + m.x6)**2) +
    m.x211 * ((-0.9849257452304463 + m.x4)**2 + (-0.9402085696377348 + m.x5)**2
    + (-0.41737974889498053 + m.x6)**2) + m.x212 * ((-0.3062096299151559 +
    m.x4)**2 + (-0.5781338903934966 + m.x5)**2 + (-0.5836695539809419 + m.x6)**
    2) + m.x213 * ((-0.6555223295998597 + m.x4)**2 + (-0.11627198084637425 +
    m.x5)**2 + (-0.5340643666314074 + m.x6)**2) + m.x214 * ((
    -0.8167955181907369 + m.x4)**2 + (-0.6648304662656255 + m.x5)**2 + (
    -0.4344445572683132 + m.x6)**2) + m.x215 * ((-0.2627634068526804 + m.x4)**2
    + (-0.8719643810841551 + m.x5)**2 + (-0.2782753479255554 + m.x6)**2) +
    m.x216 * ((-0.182590973189231 + m.x7)**2 + (-0.5665714918882914 + m.x8)**2
    + (-0.6312292714676417 + m.x9)**2) + m.x217 * ((-0.2832671889632007 + m.x7)
    **2 + (-0.17321967122047943 + m.x8)**2 + (-0.7759213801035818 + m.x9)**2)
    + m.x218 * ((-0.6166835514333678 + m.x7)**2 + (-0.18472992234217067 + m.x8)
    **2 + (-0.5668962918559568 + m.x9)**2) + m.x219 * ((-0.6928413524617497 +
    m.x7)**2 + (-0.7010280503630747 + m.x8)**2 + (-0.8235168163439104 + m.x9)**
    2) + m.x220 * ((-0.9521446875464642 + m.x7)**2 + (-0.6827797104282454 +
    m.x8)**2 + (-0.9742345929865083 + m.x9)**2) + m.x221 * ((
    -0.49339806451491164 + m.x7)**2 + (-0.2601889128277658 + m.x8)**2 + (
    -0.9240562933514055 + m.x9)**2) + m.x222 * ((-0.2671371624959298 + m.x7)**2
    + (-0.14765536014617142 + m.x8)**2 + (-0.1308517721620952 + m.x9)**2) +
    m.x223 * ((-0.5387635518822207 + m.x7)**2 + (-0.9091794865893283 + m.x8)**2
    + (-0.35329464443498004 + m.x9)**2) + m.x224 * ((-0.9543934932393079 +
    m.x7)**2 + (-0.8829919769976778 + m.x8)**2 + (-0.24953811957625105 + m.x9)
    **2) + m.x225 * ((-0.49673865851653387 + m.x7)**2 + (-0.5915750015273571 +
    m.x8)**2 + (-0.6540508311901382 + m.x9)**2) + m.x226 * ((
    -0.6851778848421465 + m.x7)**2 + (-0.06546979118233476 + m.x8)**2 + (
    -0.6973311320502895 + m.x9)**2) + m.x227 * ((-0.16455684099822276 + m.x7)**
    2 + (-0.4945110210794651 + m.x8)**2 + (-0.5302168748506974 + m.x9)**2) +
    m.x228 * ((-0.10845237413301334 + m.x7)**2 + (-0.640284214221513 + m.x8)**2
    + (-0.5696805351079286 + m.x9)**2) + m.x229 * ((-0.23716596315745875 +
    m.x7)**2 + (-0.7582428735081286 + m.x8)**2 + (-0.14219912975075677 + m.x9)
    **2) + m.x230 * ((-0.9234692794617353 + m.x7)**2 + (-0.0778901924184836 +
    m.x8)**2 + (-0.8075967020017696 + m.x9)**2) + m.x231 * ((-0.540866816090371
    + m.x7)**2 + (-0.14399747110118288 + m.x8)**2 + (-0.27481763904074175 +
    m.x9)**2) + m.x232 * ((-0.9668344449551666 + m.x7)**2 + (
    -0.6728169766961944 + m.x8)**2 + (-0.5957407662223678 + m.x9)**2) + m.x233
    * ((-0.7078504643054941 + m.x7)**2 + (-0.15971028625085149 + m.x8)**2 + (
    -0.5302963826027993 + m.x9)**2) + m.x234 * ((-0.8837023252340255 + m.x7)**2
    + (-0.29928440722639893 + m.x8)**2 + (-0.44169026690300495 + m.x9)**2) +
    m.x235 * ((-0.9988349888534216 + m.x7)**2 + (-0.9108542073862229 + m.x8)**2
    + (-0.3076571036413186 + m.x9)**2) + m.x236 * ((-0.9347820308317397 + m.x7)
    **2 + (-0.008277334533312586 + m.x8)**2 + (-0.5493915389372619 + m.x9)**2)
    + m.x237 * ((-0.8463388658403949 + m.x7)**2 + (-0.7189544434255234 + m.x8)
    **2 + (-0.6058316717442289 + m.x9)**2) + m.x238 * ((-0.28002015412253 +
    m.x7)**2 + (-0.9634485414492736 + m.x8)**2 + (-0.5628416900899014 + m.x9)**
    2) + m.x239 * ((-0.9058009322708488 + m.x7)**2 + (-0.9215478966214675 +
    m.x8)**2 + (-0.693970532541882 + m.x9)**2) + m.x240 * ((
    -0.48234013355525474 + m.x7)**2 + (-0.6704565562300323 + m.x8)**2 + (
    -0.17108667007034573 + m.x9)**2) + m.x241 * ((-0.35039670467264805 + m.x7)
    **2 + (-0.9730227072363548 + m.x8)**2 + (-0.16164836217963152 + m.x9)**2)
    + m.x242 * ((-0.032853727849101344 + m.x7)**2 + (-0.8972914472060697 +
    m.x8)**2 + (-0.5002344554243207 + m.x9)**2) + m.x243 * ((
    -0.2788175585600441 + m.x7)**2 + (-0.925751731057649 + m.x8)**2 + (
    -0.7670404625118962 + m.x9)**2) + m.x244 * ((-0.4497791511222945 + m.x7)**2
    + (-0.48620903327713016 + m.x8)**2 + (-0.3154941664955949 + m.x9)**2) +
    m.x245 * ((-0.479795503546542 + m.x7)**2 + (-0.6708482470175294 + m.x8)**2
    + (-0.6732217870137864 + m.x9)**2) + m.x246 * ((-0.3124285024815808 + m.x7)
    **2 + (-0.9048786174799557 + m.x8)**2 + (-0.07517130917071779 + m.x9)**2)
    + m.x247 * ((-0.9758976938691616 + m.x7)**2 + (-0.7548191430644975 + m.x8)
    **2 + (-0.17206520112879609 + m.x9)**2) + m.x248 * ((-0.7014387290695361 +
    m.x7)**2 + (-0.9629369136587164 + m.x8)**2 + (-0.6705450578414445 + m.x9)**
    2) + m.x249 * ((-0.4008827939787283 + m.x7)**2 + (-0.827645026992737 + m.x8)
    **2 + (-0.5996187050142987 + m.x9)**2) + m.x250 * ((-0.7695006716313056 +
    m.x7)**2 + (-0.0304732644411716 + m.x8)**2 + (-0.43726762258665086 + m.x9)
    **2) + m.x251 * ((-0.8536091145712932 + m.x7)**2 + (-0.47221565503791474 +
    m.x8)**2 + (-0.9530780172694218 + m.x9)**2) + m.x252 * ((
    -0.5188203591441234 + m.x7)**2 + (-0.1281672582217266 + m.x8)**2 + (
    -0.6943094553894391 + m.x9)**2) + m.x253 * ((-0.08010782288058038 + m.x7)**
    2 + (-0.24152490637399082 + m.x8)**2 + (-0.8281358660983907 + m.x9)**2) +
    m.x254 * ((-0.6421940815386412 + m.x7)**2 + (-0.12649912077368797 + m.x8)**
    2 + (-0.02816586075065286 + m.x9)**2) + m.x255 * ((-0.49834091606095776 +
    m.x7)**2 + (-0.05385179230503356 + m.x8)**2 + (-0.16649560036120326 + m.x9)
    **2) + m.x256 * ((-0.44749939041222264 + m.x7)**2 + (-0.38094481309529127
    + m.x8)**2 + (-0.4244480931198653 + m.x9)**2) + m.x257 * ((
    -0.6615144607793271 + m.x7)**2 + (-0.28647547516475624 + m.x8)**2 + (
    -0.5938317138915002 + m.x9)**2) + m.x258 * ((-0.16412983035791717 + m.x7)**
    2 + (-0.7315916404115455 + m.x8)**2 + (-0.7945041523159543 + m.x9)**2) +
    m.x259 * ((-0.8406929484324254 + m.x7)**2 + (-0.1768935596158654 + m.x8)**2
    + (-0.9610393111972642 + m.x9)**2) + m.x260 * ((-0.7568320576996023 + m.x7)
    **2 + (-0.8546272679432373 + m.x8)**2 + (-0.47261297066126495 + m.x9)**2)
    + m.x261 * ((-0.6482257394415872 + m.x7)**2 + (-0.07605513871045355 + m.x8)
    **2 + (-0.9632360437660454 + m.x9)**2) + m.x262 * ((-0.04709405204952222 +
    m.x7)**2 + (-0.485851180307163 + m.x8)**2 + (-0.2023313958130618 + m.x9)**2)
    + m.x263 * ((-0.9943387951600927 + m.x7)**2 + (-0.561661529271997 + m.x8)
    **2 + (-0.41120790568861443 + m.x9)**2) + m.x264 * ((-0.5689039680629383 +
    m.x7)**2 + (-0.7331999848252405 + m.x8)**2 + (-0.06524623840128607 + m.x9)
    **2) + m.x265 * ((-0.3157591979227248 + m.x7)**2 + (-0.36032648332547135 +
    m.x8)**2 + (-0.6231552244780812 + m.x9)**2) + m.x266 * ((
    -0.09241374392362178 + m.x7)**2 + (-0.6343499642335877 + m.x8)**2 + (
    -0.4649079471250238 + m.x9)**2) + m.x267 * ((-0.688999295800091 + m.x7)**2
    + (-0.41235973103252466 + m.x8)**2 + (-0.06858188095070694 + m.x9)**2) +
    m.x268 * ((-0.5368752167875853 + m.x7)**2 + (-0.07061782991482157 + m.x8)**
    2 + (-0.3905327318657953 + m.x9)**2) + m.x269 * ((-0.09236084144989976 +
    m.x7)**2 + (-0.8966749133315102 + m.x8)**2 + (-0.6119569273762655 + m.x9)**
    2) + m.x270 * ((-0.36671410401176074 + m.x7)**2 + (-0.22867661994729294 +
    m.x8)**2 + (-0.34205809393406117 + m.x9)**2) + m.x271 * ((
    -0.2884689151866864 + m.x7)**2 + (-0.8245188787565171 + m.x8)**2 + (
    -0.5471817452899417 + m.x9)**2) + m.x272 * ((-0.3095681539176819 + m.x7)**2
    + (-0.24650073053553823 + m.x8)**2 + (-0.7075429829955994 + m.x9)**2) +
    m.x273 * ((-0.24085416793099568 + m.x7)**2 + (-0.9209114031548099 + m.x8)**
    2 + (-0.7121452348711909 + m.x9)**2) + m.x274 * ((-0.6097813059476557 +
    m.x7)**2 + (-0.13509746247515075 + m.x8)**2 + (-0.9576415267519117 + m.x9)
    **2) + m.x275 * ((-0.39311391559059083 + m.x7)**2 + (-0.6802374509278515 +
    m.x8)**2 + (-0.8564222091336956 + m.x9)**2) + m.x276 * ((
    -0.9189964545477477 + m.x7)**2 + (-0.26148532247210654 + m.x8)**2 + (
    -0.9509249567269127 + m.x9)**2) + m.x277 * ((-0.02208444426023015 + m.x7)**
    2 + (-0.1576091196577002 + m.x8)**2 + (-0.7074191023951775 + m.x9)**2) +
    m.x278 * ((-0.650480284651522 + m.x7)**2 + (-0.9428001755748773 + m.x8)**2
    + (-0.12491415562242869 + m.x9)**2) + m.x279 * ((-0.2619140159334036 +
    m.x7)**2 + (-0.1777418278918652 + m.x8)**2 + (-0.3249343841798372 + m.x9)**
    2) + m.x280 * ((-0.012299809392943395 + m.x7)**2 + (-0.4826364643146488 +
    m.x8)**2 + (-0.877608971013956 + m.x9)**2) + m.x281 * ((-0.9278995012468446
    + m.x7)**2 + (-0.29658116106747157 + m.x8)**2 + (-0.4139069448025193 +
    m.x9)**2) + m.x282 * ((-0.1783104387827067 + m.x7)**2 + (-0.523247944850848
    + m.x8)**2 + (-0.7592637122950673 + m.x9)**2) + m.x283 * ((
    -0.6885309028690637 + m.x7)**2 + (-0.069836660702157 + m.x8)**2 + (
    -0.27844283434957473 + m.x9)**2) + m.x284 * ((-0.3628069626450744 + m.x7)**
    2 + (-0.4524112032480545 + m.x8)**2 + (-0.9091077636574432 + m.x9)**2) +
    m.x285 * ((-0.19545965240891594 + m.x7)**2 + (-0.8349228826970087 + m.x8)**
    2 + (-0.2600240764929378 + m.x9)**2) + m.x286 * ((-0.8136957237985446 +
    m.x7)**2 + (-0.8440312039370582 + m.x8)**2 + (-0.18657993159673503 + m.x9)
    **2) + m.x287 * ((-0.7332761233575051 + m.x7)**2 + (-0.9938264339064263 +
    m.x8)**2 + (-0.848810907941449 + m.x9)**2) + m.x288 * ((-0.6625468543751725
    + m.x7)**2 + (-0.8649355655149289 + m.x8)**2 + (-0.5267141542502073 + m.x9)
    **2) + m.x289 * ((-0.4152755489969038 + m.x7)**2 + (-0.8771524784813198 +
    m.x8)**2 + (-0.30733079492573634 + m.x9)**2) + m.x290 * ((
    -0.35755808475562567 + m.x7)**2 + (-0.949115491768236 + m.x8)**2 + (
    -0.15156928782779888 + m.x9)**2) + m.x291 * ((-0.5058696724084709 + m.x7)**
    2 + (-0.6421669787387695 + m.x8)**2 + (-0.2704977371827102 + m.x9)**2) +
    m.x292 * ((-0.02314501086665055 + m.x7)**2 + (-0.797073612921973 + m.x8)**2
    + (-0.6718295177964552 + m.x9)**2) + m.x293 * ((-0.6674227026324897 + m.x7)
    **2 + (-0.28533905171646934 + m.x8)**2 + (-0.6530875341797157 + m.x9)**2)
    + m.x294 * ((-0.49802163179869985 + m.x7)**2 + (-0.9159175310463538 + m.x8)
    **2 + (-0.8511170311594338 + m.x9)**2) + m.x295 * ((-0.921121885282289 +
    m.x7)**2 + (-0.29110498439296717 + m.x8)**2 + (-0.07095961947687046 + m.x9)
    **2) + m.x296 * ((-0.5066223599150115 + m.x7)**2 + (-0.8365869947893311 +
    m.x8)**2 + (-0.37136067431457864 + m.x9)**2) + m.x297 * ((
    -0.7282642906004309 + m.x7)**2 + (-0.8076127746397918 + m.x8)**2 + (
    -0.23700100631040355 + m.x9)**2) + m.x298 * ((-0.17793281956808304 + m.x7)
    **2 + (-0.8729572789960333 + m.x8)**2 + (-0.17550679028027727 + m.x9)**2)
    + m.x299 * ((-0.28160869151209356 + m.x7)**2 + (-0.21027420689223564 +
    m.x8)**2 + (-0.5801863384871276 + m.x9)**2) + m.x300 * ((-0.703680099800644
    + m.x7)**2 + (-0.7954020654414685 + m.x8)**2 + (-0.037273161155704004 +
    m.x9)**2) + m.x301 * ((-0.8494522028293213 + m.x7)**2 + (
    -0.6755785367429551 + m.x8)**2 + (-0.3545484132724107 + m.x9)**2) + m.x302
    * ((-0.38765300434187966 + m.x7)**2 + (-0.3029441042054243 + m.x8)**2 + (
    -0.9073082164213291 + m.x9)**2) + m.x303 * ((-0.8478833426449218 + m.x7)**2
    + (-0.5190242383318947 + m.x8)**2 + (-0.890475723079222 + m.x9)**2) +
    m.x304 * ((-0.08526574189471425 + m.x7)**2 + (-0.08433063147801656 + m.x8)
    **2 + (-0.34038923400741616 + m.x9)**2) + m.x305 * ((-0.3819102188291116 +
    m.x7)**2 + (-0.368719462749436 + m.x8)**2 + (-0.5059825484936955 + m.x9)**2)
    + m.x306 * ((-0.7491328863462429 + m.x7)**2 + (-0.4007415312530962 + m.x8)
    **2 + (-0.8795211427493239 + m.x9)**2) + m.x307 * ((-0.7741279705885629 +
    m.x7)**2 + (-0.8856116737594064 + m.x8)**2 + (-0.2651355164571192 + m.x9)**
    2) + m.x308 * ((-0.9047294977974201 + m.x7)**2 + (-0.7357904800445998 +
    m.x8)**2 + (-0.2819553446129277 + m.x9)**2) + m.x309 * ((
    -0.7274677561703813 + m.x7)**2 + (-0.6080547644274223 + m.x8)**2 + (
    -0.4688320743625637 + m.x9)**2) + m.x310 * ((-0.2549577045934236 + m.x7)**2
    + (-0.11411488345784182 + m.x8)**2 + (-0.22595928823071643 + m.x9)**2) +
    m.x311 * ((-0.9849257452304463 + m.x7)**2 + (-0.9402085696377348 + m.x8)**2
    + (-0.41737974889498053 + m.x9)**2) + m.x312 * ((-0.3062096299151559 +
    m.x7)**2 + (-0.5781338903934966 + m.x8)**2 + (-0.5836695539809419 + m.x9)**
    2) + m.x313 * ((-0.6555223295998597 + m.x7)**2 + (-0.11627198084637425 +
    m.x8)**2 + (-0.5340643666314074 + m.x9)**2) + m.x314 * ((
    -0.8167955181907369 + m.x7)**2 + (-0.6648304662656255 + m.x8)**2 + (
    -0.4344445572683132 + m.x9)**2) + m.x315 * ((-0.2627634068526804 + m.x7)**2
    + (-0.8719643810841551 + m.x8)**2 + (-0.2782753479255554 + m.x9)**2) +
    m.x316 * ((-0.182590973189231 + m.x10)**2 + (-0.5665714918882914 + m.x11)**
    2 + (-0.6312292714676417 + m.x12)**2) + m.x317 * ((-0.2832671889632007 +
    m.x10)**2 + (-0.17321967122047943 + m.x11)**2 + (-0.7759213801035818 +
    m.x12)**2) + m.x318 * ((-0.6166835514333678 + m.x10)**2 + (
    -0.18472992234217067 + m.x11)**2 + (-0.5668962918559568 + m.x12)**2) +
    m.x319 * ((-0.6928413524617497 + m.x10)**2 + (-0.7010280503630747 + m.x11)
    **2 + (-0.8235168163439104 + m.x12)**2) + m.x320 * ((-0.9521446875464642 +
    m.x10)**2 + (-0.6827797104282454 + m.x11)**2 + (-0.9742345929865083 + m.x12)
    **2) + m.x321 * ((-0.49339806451491164 + m.x10)**2 + (-0.2601889128277658
    + m.x11)**2 + (-0.9240562933514055 + m.x12)**2) + m.x322 * ((
    -0.2671371624959298 + m.x10)**2 + (-0.14765536014617142 + m.x11)**2 + (
    -0.1308517721620952 + m.x12)**2) + m.x323 * ((-0.5387635518822207 + m.x10)
    **2 + (-0.9091794865893283 + m.x11)**2 + (-0.35329464443498004 + m.x12)**2)
    + m.x324 * ((-0.9543934932393079 + m.x10)**2 + (-0.8829919769976778 +
    m.x11)**2 + (-0.24953811957625105 + m.x12)**2) + m.x325 * ((
    -0.49673865851653387 + m.x10)**2 + (-0.5915750015273571 + m.x11)**2 + (
    -0.6540508311901382 + m.x12)**2) + m.x326 * ((-0.6851778848421465 + m.x10)
    **2 + (-0.06546979118233476 + m.x11)**2 + (-0.6973311320502895 + m.x12)**2)
    + m.x327 * ((-0.16455684099822276 + m.x10)**2 + (-0.4945110210794651 +
    m.x11)**2 + (-0.5302168748506974 + m.x12)**2) + m.x328 * ((
    -0.10845237413301334 + m.x10)**2 + (-0.640284214221513 + m.x11)**2 + (
    -0.5696805351079286 + m.x12)**2) + m.x329 * ((-0.23716596315745875 + m.x10)
    **2 + (-0.7582428735081286 + m.x11)**2 + (-0.14219912975075677 + m.x12)**2)
    + m.x330 * ((-0.9234692794617353 + m.x10)**2 + (-0.0778901924184836 +
    m.x11)**2 + (-0.8075967020017696 + m.x12)**2) + m.x331 * ((
    -0.540866816090371 + m.x10)**2 + (-0.14399747110118288 + m.x11)**2 + (
    -0.27481763904074175 + m.x12)**2) + m.x332 * ((-0.9668344449551666 + m.x10)
    **2 + (-0.6728169766961944 + m.x11)**2 + (-0.5957407662223678 + m.x12)**2)
    + m.x333 * ((-0.7078504643054941 + m.x10)**2 + (-0.15971028625085149 +
    m.x11)**2 + (-0.5302963826027993 + m.x12)**2) + m.x334 * ((
    -0.8837023252340255 + m.x10)**2 + (-0.29928440722639893 + m.x11)**2 + (
    -0.44169026690300495 + m.x12)**2) + m.x335 * ((-0.9988349888534216 + m.x10)
    **2 + (-0.9108542073862229 + m.x11)**2 + (-0.3076571036413186 + m.x12)**2)
    + m.x336 * ((-0.9347820308317397 + m.x10)**2 + (-0.008277334533312586 +
    m.x11)**2 + (-0.5493915389372619 + m.x12)**2) + m.x337 * ((
    -0.8463388658403949 + m.x10)**2 + (-0.7189544434255234 + m.x11)**2 + (
    -0.6058316717442289 + m.x12)**2) + m.x338 * ((-0.28002015412253 + m.x10)**2
    + (-0.9634485414492736 + m.x11)**2 + (-0.5628416900899014 + m.x12)**2) +
    m.x339 * ((-0.9058009322708488 + m.x10)**2 + (-0.9215478966214675 + m.x11)
    **2 + (-0.693970532541882 + m.x12)**2) + m.x340 * ((-0.48234013355525474 +
    m.x10)**2 + (-0.6704565562300323 + m.x11)**2 + (-0.17108667007034573 +
    m.x12)**2) + m.x341 * ((-0.35039670467264805 + m.x10)**2 + (
    -0.9730227072363548 + m.x11)**2 + (-0.16164836217963152 + m.x12)**2) +
    m.x342 * ((-0.032853727849101344 + m.x10)**2 + (-0.8972914472060697 + m.x11)
    **2 + (-0.5002344554243207 + m.x12)**2) + m.x343 * ((-0.2788175585600441 +
    m.x10)**2 + (-0.925751731057649 + m.x11)**2 + (-0.7670404625118962 + m.x12)
    **2) + m.x344 * ((-0.4497791511222945 + m.x10)**2 + (-0.48620903327713016
    + m.x11)**2 + (-0.3154941664955949 + m.x12)**2) + m.x345 * ((
    -0.479795503546542 + m.x10)**2 + (-0.6708482470175294 + m.x11)**2 + (
    -0.6732217870137864 + m.x12)**2) + m.x346 * ((-0.3124285024815808 + m.x10)
    **2 + (-0.9048786174799557 + m.x11)**2 + (-0.07517130917071779 + m.x12)**2)
    + m.x347 * ((-0.9758976938691616 + m.x10)**2 + (-0.7548191430644975 +
    m.x11)**2 + (-0.17206520112879609 + m.x12)**2) + m.x348 * ((
    -0.7014387290695361 + m.x10)**2 + (-0.9629369136587164 + m.x11)**2 + (
    -0.6705450578414445 + m.x12)**2) + m.x349 * ((-0.4008827939787283 + m.x10)
    **2 + (-0.827645026992737 + m.x11)**2 + (-0.5996187050142987 + m.x12)**2)
    + m.x350 * ((-0.7695006716313056 + m.x10)**2 + (-0.0304732644411716 +
    m.x11)**2 + (-0.43726762258665086 + m.x12)**2) + m.x351 * ((
    -0.8536091145712932 + m.x10)**2 + (-0.47221565503791474 + m.x11)**2 + (
    -0.9530780172694218 + m.x12)**2) + m.x352 * ((-0.5188203591441234 + m.x10)
    **2 + (-0.1281672582217266 + m.x11)**2 + (-0.6943094553894391 + m.x12)**2)
    + m.x353 * ((-0.08010782288058038 + m.x10)**2 + (-0.24152490637399082 +
    m.x11)**2 + (-0.8281358660983907 + m.x12)**2) + m.x354 * ((
    -0.6421940815386412 + m.x10)**2 + (-0.12649912077368797 + m.x11)**2 + (
    -0.02816586075065286 + m.x12)**2) + m.x355 * ((-0.49834091606095776 + m.x10)
    **2 + (-0.05385179230503356 + m.x11)**2 + (-0.16649560036120326 + m.x12)**2)
    + m.x356 * ((-0.44749939041222264 + m.x10)**2 + (-0.38094481309529127 +
    m.x11)**2 + (-0.4244480931198653 + m.x12)**2) + m.x357 * ((
    -0.6615144607793271 + m.x10)**2 + (-0.28647547516475624 + m.x11)**2 + (
    -0.5938317138915002 + m.x12)**2) + m.x358 * ((-0.16412983035791717 + m.x10)
    **2 + (-0.7315916404115455 + m.x11)**2 + (-0.7945041523159543 + m.x12)**2)
    + m.x359 * ((-0.8406929484324254 + m.x10)**2 + (-0.1768935596158654 +
    m.x11)**2 + (-0.9610393111972642 + m.x12)**2) + m.x360 * ((
    -0.7568320576996023 + m.x10)**2 + (-0.8546272679432373 + m.x11)**2 + (
    -0.47261297066126495 + m.x12)**2) + m.x361 * ((-0.6482257394415872 + m.x10)
    **2 + (-0.07605513871045355 + m.x11)**2 + (-0.9632360437660454 + m.x12)**2)
    + m.x362 * ((-0.04709405204952222 + m.x10)**2 + (-0.485851180307163 +
    m.x11)**2 + (-0.2023313958130618 + m.x12)**2) + m.x363 * ((
    -0.9943387951600927 + m.x10)**2 + (-0.561661529271997 + m.x11)**2 + (
    -0.41120790568861443 + m.x12)**2) + m.x364 * ((-0.5689039680629383 + m.x10)
    **2 + (-0.7331999848252405 + m.x11)**2 + (-0.06524623840128607 + m.x12)**2)
    + m.x365 * ((-0.3157591979227248 + m.x10)**2 + (-0.36032648332547135 +
    m.x11)**2 + (-0.6231552244780812 + m.x12)**2) + m.x366 * ((
    -0.09241374392362178 + m.x10)**2 + (-0.6343499642335877 + m.x11)**2 + (
    -0.4649079471250238 + m.x12)**2) + m.x367 * ((-0.688999295800091 + m.x10)**
    2 + (-0.41235973103252466 + m.x11)**2 + (-0.06858188095070694 + m.x12)**2)
    + m.x368 * ((-0.5368752167875853 + m.x10)**2 + (-0.07061782991482157 +
    m.x11)**2 + (-0.3905327318657953 + m.x12)**2) + m.x369 * ((
    -0.09236084144989976 + m.x10)**2 + (-0.8966749133315102 + m.x11)**2 + (
    -0.6119569273762655 + m.x12)**2) + m.x370 * ((-0.36671410401176074 + m.x10)
    **2 + (-0.22867661994729294 + m.x11)**2 + (-0.34205809393406117 + m.x12)**2)
    + m.x371 * ((-0.2884689151866864 + m.x10)**2 + (-0.8245188787565171 +
    m.x11)**2 + (-0.5471817452899417 + m.x12)**2) + m.x372 * ((
    -0.3095681539176819 + m.x10)**2 + (-0.24650073053553823 + m.x11)**2 + (
    -0.7075429829955994 + m.x12)**2) + m.x373 * ((-0.24085416793099568 + m.x10)
    **2 + (-0.9209114031548099 + m.x11)**2 + (-0.7121452348711909 + m.x12)**2)
    + m.x374 * ((-0.6097813059476557 + m.x10)**2 + (-0.13509746247515075 +
    m.x11)**2 + (-0.9576415267519117 + m.x12)**2) + m.x375 * ((
    -0.39311391559059083 + m.x10)**2 + (-0.6802374509278515 + m.x11)**2 + (
    -0.8564222091336956 + m.x12)**2) + m.x376 * ((-0.9189964545477477 + m.x10)
    **2 + (-0.26148532247210654 + m.x11)**2 + (-0.9509249567269127 + m.x12)**2)
    + m.x377 * ((-0.02208444426023015 + m.x10)**2 + (-0.1576091196577002 +
    m.x11)**2 + (-0.7074191023951775 + m.x12)**2) + m.x378 * ((
    -0.650480284651522 + m.x10)**2 + (-0.9428001755748773 + m.x11)**2 + (
    -0.12491415562242869 + m.x12)**2) + m.x379 * ((-0.2619140159334036 + m.x10)
    **2 + (-0.1777418278918652 + m.x11)**2 + (-0.3249343841798372 + m.x12)**2)
    + m.x380 * ((-0.012299809392943395 + m.x10)**2 + (-0.4826364643146488 +
    m.x11)**2 + (-0.877608971013956 + m.x12)**2) + m.x381 * ((
    -0.9278995012468446 + m.x10)**2 + (-0.29658116106747157 + m.x11)**2 + (
    -0.4139069448025193 + m.x12)**2) + m.x382 * ((-0.1783104387827067 + m.x10)
    **2 + (-0.523247944850848 + m.x11)**2 + (-0.7592637122950673 + m.x12)**2)
    + m.x383 * ((-0.6885309028690637 + m.x10)**2 + (-0.069836660702157 + m.x11)
    **2 + (-0.27844283434957473 + m.x12)**2) + m.x384 * ((-0.3628069626450744
    + m.x10)**2 + (-0.4524112032480545 + m.x11)**2 + (-0.9091077636574432 +
    m.x12)**2) + m.x385 * ((-0.19545965240891594 + m.x10)**2 + (
    -0.8349228826970087 + m.x11)**2 + (-0.2600240764929378 + m.x12)**2) +
    m.x386 * ((-0.8136957237985446 + m.x10)**2 + (-0.8440312039370582 + m.x11)
    **2 + (-0.18657993159673503 + m.x12)**2) + m.x387 * ((-0.7332761233575051
    + m.x10)**2 + (-0.9938264339064263 + m.x11)**2 + (-0.848810907941449 +
    m.x12)**2) + m.x388 * ((-0.6625468543751725 + m.x10)**2 + (
    -0.8649355655149289 + m.x11)**2 + (-0.5267141542502073 + m.x12)**2) +
    m.x389 * ((-0.4152755489969038 + m.x10)**2 + (-0.8771524784813198 + m.x11)
    **2 + (-0.30733079492573634 + m.x12)**2) + m.x390 * ((-0.35755808475562567
    + m.x10)**2 + (-0.949115491768236 + m.x11)**2 + (-0.15156928782779888 +
    m.x12)**2) + m.x391 * ((-0.5058696724084709 + m.x10)**2 + (
    -0.6421669787387695 + m.x11)**2 + (-0.2704977371827102 + m.x12)**2) +
    m.x392 * ((-0.02314501086665055 + m.x10)**2 + (-0.797073612921973 + m.x11)
    **2 + (-0.6718295177964552 + m.x12)**2) + m.x393 * ((-0.6674227026324897 +
    m.x10)**2 + (-0.28533905171646934 + m.x11)**2 + (-0.6530875341797157 +
    m.x12)**2) + m.x394 * ((-0.49802163179869985 + m.x10)**2 + (
    -0.9159175310463538 + m.x11)**2 + (-0.8511170311594338 + m.x12)**2) +
    m.x395 * ((-0.921121885282289 + m.x10)**2 + (-0.29110498439296717 + m.x11)
    **2 + (-0.07095961947687046 + m.x12)**2) + m.x396 * ((-0.5066223599150115
    + m.x10)**2 + (-0.8365869947893311 + m.x11)**2 + (-0.37136067431457864 +
    m.x12)**2) + m.x397 * ((-0.7282642906004309 + m.x10)**2 + (
    -0.8076127746397918 + m.x11)**2 + (-0.23700100631040355 + m.x12)**2) +
    m.x398 * ((-0.17793281956808304 + m.x10)**2 + (-0.8729572789960333 + m.x11)
    **2 + (-0.17550679028027727 + m.x12)**2) + m.x399 * ((-0.28160869151209356
    + m.x10)**2 + (-0.21027420689223564 + m.x11)**2 + (-0.5801863384871276 +
    m.x12)**2) + m.x400 * ((-0.703680099800644 + m.x10)**2 + (
    -0.7954020654414685 + m.x11)**2 + (-0.037273161155704004 + m.x12)**2) +
    m.x401 * ((-0.8494522028293213 + m.x10)**2 + (-0.6755785367429551 + m.x11)
    **2 + (-0.3545484132724107 + m.x12)**2) + m.x402 * ((-0.38765300434187966
    + m.x10)**2 + (-0.3029441042054243 + m.x11)**2 + (-0.9073082164213291 +
    m.x12)**2) + m.x403 * ((-0.8478833426449218 + m.x10)**2 + (
    -0.5190242383318947 + m.x11)**2 + (-0.890475723079222 + m.x12)**2) + m.x404
    * ((-0.08526574189471425 + m.x10)**2 + (-0.08433063147801656 + m.x11)**2
    + (-0.34038923400741616 + m.x12)**2) + m.x405 * ((-0.3819102188291116 +
    m.x10)**2 + (-0.368719462749436 + m.x11)**2 + (-0.5059825484936955 + m.x12)
    **2) + m.x406 * ((-0.7491328863462429 + m.x10)**2 + (-0.4007415312530962 +
    m.x11)**2 + (-0.8795211427493239 + m.x12)**2) + m.x407 * ((
    -0.7741279705885629 + m.x10)**2 + (-0.8856116737594064 + m.x11)**2 + (
    -0.2651355164571192 + m.x12)**2) + m.x408 * ((-0.9047294977974201 + m.x10)
    **2 + (-0.7357904800445998 + m.x11)**2 + (-0.2819553446129277 + m.x12)**2)
    + m.x409 * ((-0.7274677561703813 + m.x10)**2 + (-0.6080547644274223 +
    m.x11)**2 + (-0.4688320743625637 + m.x12)**2) + m.x410 * ((
    -0.2549577045934236 + m.x10)**2 + (-0.11411488345784182 + m.x11)**2 + (
    -0.22595928823071643 + m.x12)**2) + m.x411 * ((-0.9849257452304463 + m.x10)
    **2 + (-0.9402085696377348 + m.x11)**2 + (-0.41737974889498053 + m.x12)**2)
    + m.x412 * ((-0.3062096299151559 + m.x10)**2 + (-0.5781338903934966 +
    m.x11)**2 + (-0.5836695539809419 + m.x12)**2) + m.x413 * ((
    -0.6555223295998597 + m.x10)**2 + (-0.11627198084637425 + m.x11)**2 + (
    -0.5340643666314074 + m.x12)**2) + m.x414 * ((-0.8167955181907369 + m.x10)
    **2 + (-0.6648304662656255 + m.x11)**2 + (-0.4344445572683132 + m.x12)**2)
    + m.x415 * ((-0.2627634068526804 + m.x10)**2 + (-0.8719643810841551 +
    m.x11)**2 + (-0.2782753479255554 + m.x12)**2) + m.x416 * ((
    -0.182590973189231 + m.x13)**2 + (-0.5665714918882914 + m.x14)**2 + (
    -0.6312292714676417 + m.x15)**2) + m.x417 * ((-0.2832671889632007 + m.x13)
    **2 + (-0.17321967122047943 + m.x14)**2 + (-0.7759213801035818 + m.x15)**2)
    + m.x418 * ((-0.6166835514333678 + m.x13)**2 + (-0.18472992234217067 +
    m.x14)**2 + (-0.5668962918559568 + m.x15)**2) + m.x419 * ((
    -0.6928413524617497 + m.x13)**2 + (-0.7010280503630747 + m.x14)**2 + (
    -0.8235168163439104 + m.x15)**2) + m.x420 * ((-0.9521446875464642 + m.x13)
    **2 + (-0.6827797104282454 + m.x14)**2 + (-0.9742345929865083 + m.x15)**2)
    + m.x421 * ((-0.49339806451491164 + m.x13)**2 + (-0.2601889128277658 +
    m.x14)**2 + (-0.9240562933514055 + m.x15)**2) + m.x422 * ((
    -0.2671371624959298 + m.x13)**2 + (-0.14765536014617142 + m.x14)**2 + (
    -0.1308517721620952 + m.x15)**2) + m.x423 * ((-0.5387635518822207 + m.x13)
    **2 + (-0.9091794865893283 + m.x14)**2 + (-0.35329464443498004 + m.x15)**2)
    + m.x424 * ((-0.9543934932393079 + m.x13)**2 + (-0.8829919769976778 +
    m.x14)**2 + (-0.24953811957625105 + m.x15)**2) + m.x425 * ((
    -0.49673865851653387 + m.x13)**2 + (-0.5915750015273571 + m.x14)**2 + (
    -0.6540508311901382 + m.x15)**2) + m.x426 * ((-0.6851778848421465 + m.x13)
    **2 + (-0.06546979118233476 + m.x14)**2 + (-0.6973311320502895 + m.x15)**2)
    + m.x427 * ((-0.16455684099822276 + m.x13)**2 + (-0.4945110210794651 +
    m.x14)**2 + (-0.5302168748506974 + m.x15)**2) + m.x428 * ((
    -0.10845237413301334 + m.x13)**2 + (-0.640284214221513 + m.x14)**2 + (
    -0.5696805351079286 + m.x15)**2) + m.x429 * ((-0.23716596315745875 + m.x13)
    **2 + (-0.7582428735081286 + m.x14)**2 + (-0.14219912975075677 + m.x15)**2)
    + m.x430 * ((-0.9234692794617353 + m.x13)**2 + (-0.0778901924184836 +
    m.x14)**2 + (-0.8075967020017696 + m.x15)**2) + m.x431 * ((
    -0.540866816090371 + m.x13)**2 + (-0.14399747110118288 + m.x14)**2 + (
    -0.27481763904074175 + m.x15)**2) + m.x432 * ((-0.9668344449551666 + m.x13)
    **2 + (-0.6728169766961944 + m.x14)**2 + (-0.5957407662223678 + m.x15)**2)
    + m.x433 * ((-0.7078504643054941 + m.x13)**2 + (-0.15971028625085149 +
    m.x14)**2 + (-0.5302963826027993 + m.x15)**2) + m.x434 * ((
    -0.8837023252340255 + m.x13)**2 + (-0.29928440722639893 + m.x14)**2 + (
    -0.44169026690300495 + m.x15)**2) + m.x435 * ((-0.9988349888534216 + m.x13)
    **2 + (-0.9108542073862229 + m.x14)**2 + (-0.3076571036413186 + m.x15)**2)
    + m.x436 * ((-0.9347820308317397 + m.x13)**2 + (-0.008277334533312586 +
    m.x14)**2 + (-0.5493915389372619 + m.x15)**2) + m.x437 * ((
    -0.8463388658403949 + m.x13)**2 + (-0.7189544434255234 + m.x14)**2 + (
    -0.6058316717442289 + m.x15)**2) + m.x438 * ((-0.28002015412253 + m.x13)**2
    + (-0.9634485414492736 + m.x14)**2 + (-0.5628416900899014 + m.x15)**2) +
    m.x439 * ((-0.9058009322708488 + m.x13)**2 + (-0.9215478966214675 + m.x14)
    **2 + (-0.693970532541882 + m.x15)**2) + m.x440 * ((-0.48234013355525474 +
    m.x13)**2 + (-0.6704565562300323 + m.x14)**2 + (-0.17108667007034573 +
    m.x15)**2) + m.x441 * ((-0.35039670467264805 + m.x13)**2 + (
    -0.9730227072363548 + m.x14)**2 + (-0.16164836217963152 + m.x15)**2) +
    m.x442 * ((-0.032853727849101344 + m.x13)**2 + (-0.8972914472060697 + m.x14)
    **2 + (-0.5002344554243207 + m.x15)**2) + m.x443 * ((-0.2788175585600441 +
    m.x13)**2 + (-0.925751731057649 + m.x14)**2 + (-0.7670404625118962 + m.x15)
    **2) + m.x444 * ((-0.4497791511222945 + m.x13)**2 + (-0.48620903327713016
    + m.x14)**2 + (-0.3154941664955949 + m.x15)**2) + m.x445 * ((
    -0.479795503546542 + m.x13)**2 + (-0.6708482470175294 + m.x14)**2 + (
    -0.6732217870137864 + m.x15)**2) + m.x446 * ((-0.3124285024815808 + m.x13)
    **2 + (-0.9048786174799557 + m.x14)**2 + (-0.07517130917071779 + m.x15)**2)
    + m.x447 * ((-0.9758976938691616 + m.x13)**2 + (-0.7548191430644975 +
    m.x14)**2 + (-0.17206520112879609 + m.x15)**2) + m.x448 * ((
    -0.7014387290695361 + m.x13)**2 + (-0.9629369136587164 + m.x14)**2 + (
    -0.6705450578414445 + m.x15)**2) + m.x449 * ((-0.4008827939787283 + m.x13)
    **2 + (-0.827645026992737 + m.x14)**2 + (-0.5996187050142987 + m.x15)**2)
    + m.x450 * ((-0.7695006716313056 + m.x13)**2 + (-0.0304732644411716 +
    m.x14)**2 + (-0.43726762258665086 + m.x15)**2) + m.x451 * ((
    -0.8536091145712932 + m.x13)**2 + (-0.47221565503791474 + m.x14)**2 + (
    -0.9530780172694218 + m.x15)**2) + m.x452 * ((-0.5188203591441234 + m.x13)
    **2 + (-0.1281672582217266 + m.x14)**2 + (-0.6943094553894391 + m.x15)**2)
    + m.x453 * ((-0.08010782288058038 + m.x13)**2 + (-0.24152490637399082 +
    m.x14)**2 + (-0.8281358660983907 + m.x15)**2) + m.x454 * ((
    -0.6421940815386412 + m.x13)**2 + (-0.12649912077368797 + m.x14)**2 + (
    -0.02816586075065286 + m.x15)**2) + m.x455 * ((-0.49834091606095776 + m.x13)
    **2 + (-0.05385179230503356 + m.x14)**2 + (-0.16649560036120326 + m.x15)**2)
    + m.x456 * ((-0.44749939041222264 + m.x13)**2 + (-0.38094481309529127 +
    m.x14)**2 + (-0.4244480931198653 + m.x15)**2) + m.x457 * ((
    -0.6615144607793271 + m.x13)**2 + (-0.28647547516475624 + m.x14)**2 + (
    -0.5938317138915002 + m.x15)**2) + m.x458 * ((-0.16412983035791717 + m.x13)
    **2 + (-0.7315916404115455 + m.x14)**2 + (-0.7945041523159543 + m.x15)**2)
    + m.x459 * ((-0.8406929484324254 + m.x13)**2 + (-0.1768935596158654 +
    m.x14)**2 + (-0.9610393111972642 + m.x15)**2) + m.x460 * ((
    -0.7568320576996023 + m.x13)**2 + (-0.8546272679432373 + m.x14)**2 + (
    -0.47261297066126495 + m.x15)**2) + m.x461 * ((-0.6482257394415872 + m.x13)
    **2 + (-0.07605513871045355 + m.x14)**2 + (-0.9632360437660454 + m.x15)**2)
    + m.x462 * ((-0.04709405204952222 + m.x13)**2 + (-0.485851180307163 +
    m.x14)**2 + (-0.2023313958130618 + m.x15)**2) + m.x463 * ((
    -0.9943387951600927 + m.x13)**2 + (-0.561661529271997 + m.x14)**2 + (
    -0.41120790568861443 + m.x15)**2) + m.x464 * ((-0.5689039680629383 + m.x13)
    **2 + (-0.7331999848252405 + m.x14)**2 + (-0.06524623840128607 + m.x15)**2)
    + m.x465 * ((-0.3157591979227248 + m.x13)**2 + (-0.36032648332547135 +
    m.x14)**2 + (-0.6231552244780812 + m.x15)**2) + m.x466 * ((
    -0.09241374392362178 + m.x13)**2 + (-0.6343499642335877 + m.x14)**2 + (
    -0.4649079471250238 + m.x15)**2) + m.x467 * ((-0.688999295800091 + m.x13)**
    2 + (-0.41235973103252466 + m.x14)**2 + (-0.06858188095070694 + m.x15)**2)
    + m.x468 * ((-0.5368752167875853 + m.x13)**2 + (-0.07061782991482157 +
    m.x14)**2 + (-0.3905327318657953 + m.x15)**2) + m.x469 * ((
    -0.09236084144989976 + m.x13)**2 + (-0.8966749133315102 + m.x14)**2 + (
    -0.6119569273762655 + m.x15)**2) + m.x470 * ((-0.36671410401176074 + m.x13)
    **2 + (-0.22867661994729294 + m.x14)**2 + (-0.34205809393406117 + m.x15)**2)
    + m.x471 * ((-0.2884689151866864 + m.x13)**2 + (-0.8245188787565171 +
    m.x14)**2 + (-0.5471817452899417 + m.x15)**2) + m.x472 * ((
    -0.3095681539176819 + m.x13)**2 + (-0.24650073053553823 + m.x14)**2 + (
    -0.7075429829955994 + m.x15)**2) + m.x473 * ((-0.24085416793099568 + m.x13)
    **2 + (-0.9209114031548099 + m.x14)**2 + (-0.7121452348711909 + m.x15)**2)
    + m.x474 * ((-0.6097813059476557 + m.x13)**2 + (-0.13509746247515075 +
    m.x14)**2 + (-0.9576415267519117 + m.x15)**2) + m.x475 * ((
    -0.39311391559059083 + m.x13)**2 + (-0.6802374509278515 + m.x14)**2 + (
    -0.8564222091336956 + m.x15)**2) + m.x476 * ((-0.9189964545477477 + m.x13)
    **2 + (-0.26148532247210654 + m.x14)**2 + (-0.9509249567269127 + m.x15)**2)
    + m.x477 * ((-0.02208444426023015 + m.x13)**2 + (-0.1576091196577002 +
    m.x14)**2 + (-0.7074191023951775 + m.x15)**2) + m.x478 * ((
    -0.650480284651522 + m.x13)**2 + (-0.9428001755748773 + m.x14)**2 + (
    -0.12491415562242869 + m.x15)**2) + m.x479 * ((-0.2619140159334036 + m.x13)
    **2 + (-0.1777418278918652 + m.x14)**2 + (-0.3249343841798372 + m.x15)**2)
    + m.x480 * ((-0.012299809392943395 + m.x13)**2 + (-0.4826364643146488 +
    m.x14)**2 + (-0.877608971013956 + m.x15)**2) + m.x481 * ((
    -0.9278995012468446 + m.x13)**2 + (-0.29658116106747157 + m.x14)**2 + (
    -0.4139069448025193 + m.x15)**2) + m.x482 * ((-0.1783104387827067 + m.x13)
    **2 + (-0.523247944850848 + m.x14)**2 + (-0.7592637122950673 + m.x15)**2)
    + m.x483 * ((-0.6885309028690637 + m.x13)**2 + (-0.069836660702157 + m.x14)
    **2 + (-0.27844283434957473 + m.x15)**2) + m.x484 * ((-0.3628069626450744
    + m.x13)**2 + (-0.4524112032480545 + m.x14)**2 + (-0.9091077636574432 +
    m.x15)**2) + m.x485 * ((-0.19545965240891594 + m.x13)**2 + (
    -0.8349228826970087 + m.x14)**2 + (-0.2600240764929378 + m.x15)**2) +
    m.x486 * ((-0.8136957237985446 + m.x13)**2 + (-0.8440312039370582 + m.x14)
    **2 + (-0.18657993159673503 + m.x15)**2) + m.x487 * ((-0.7332761233575051
    + m.x13)**2 + (-0.9938264339064263 + m.x14)**2 + (-0.848810907941449 +
    m.x15)**2) + m.x488 * ((-0.6625468543751725 + m.x13)**2 + (
    -0.8649355655149289 + m.x14)**2 + (-0.5267141542502073 + m.x15)**2) +
    m.x489 * ((-0.4152755489969038 + m.x13)**2 + (-0.8771524784813198 + m.x14)
    **2 + (-0.30733079492573634 + m.x15)**2) + m.x490 * ((-0.35755808475562567
    + m.x13)**2 + (-0.949115491768236 + m.x14)**2 + (-0.15156928782779888 +
    m.x15)**2) + m.x491 * ((-0.5058696724084709 + m.x13)**2 + (
    -0.6421669787387695 + m.x14)**2 + (-0.2704977371827102 + m.x15)**2) +
    m.x492 * ((-0.02314501086665055 + m.x13)**2 + (-0.797073612921973 + m.x14)
    **2 + (-0.6718295177964552 + m.x15)**2) + m.x493 * ((-0.6674227026324897 +
    m.x13)**2 + (-0.28533905171646934 + m.x14)**2 + (-0.6530875341797157 +
    m.x15)**2) + m.x494 * ((-0.49802163179869985 + m.x13)**2 + (
    -0.9159175310463538 + m.x14)**2 + (-0.8511170311594338 + m.x15)**2) +
    m.x495 * ((-0.921121885282289 + m.x13)**2 + (-0.29110498439296717 + m.x14)
    **2 + (-0.07095961947687046 + m.x15)**2) + m.x496 * ((-0.5066223599150115
    + m.x13)**2 + (-0.8365869947893311 + m.x14)**2 + (-0.37136067431457864 +
    m.x15)**2) + m.x497 * ((-0.7282642906004309 + m.x13)**2 + (
    -0.8076127746397918 + m.x14)**2 + (-0.23700100631040355 + m.x15)**2) +
    m.x498 * ((-0.17793281956808304 + m.x13)**2 + (-0.8729572789960333 + m.x14)
    **2 + (-0.17550679028027727 + m.x15)**2) + m.x499 * ((-0.28160869151209356
    + m.x13)**2 + (-0.21027420689223564 + m.x14)**2 + (-0.5801863384871276 +
    m.x15)**2) + m.x500 * ((-0.703680099800644 + m.x13)**2 + (
    -0.7954020654414685 + m.x14)**2 + (-0.037273161155704004 + m.x15)**2) +
    m.x501 * ((-0.8494522028293213 + m.x13)**2 + (-0.6755785367429551 + m.x14)
    **2 + (-0.3545484132724107 + m.x15)**2) + m.x502 * ((-0.38765300434187966
    + m.x13)**2 + (-0.3029441042054243 + m.x14)**2 + (-0.9073082164213291 +
    m.x15)**2) + m.x503 * ((-0.8478833426449218 + m.x13)**2 + (
    -0.5190242383318947 + m.x14)**2 + (-0.890475723079222 + m.x15)**2) + m.x504
    * ((-0.08526574189471425 + m.x13)**2 + (-0.08433063147801656 + m.x14)**2
    + (-0.34038923400741616 + m.x15)**2) + m.x505 * ((-0.3819102188291116 +
    m.x13)**2 + (-0.368719462749436 + m.x14)**2 + (-0.5059825484936955 + m.x15)
    **2) + m.x506 * ((-0.7491328863462429 + m.x13)**2 + (-0.4007415312530962 +
    m.x14)**2 + (-0.8795211427493239 + m.x15)**2) + m.x507 * ((
    -0.7741279705885629 + m.x13)**2 + (-0.8856116737594064 + m.x14)**2 + (
    -0.2651355164571192 + m.x15)**2) + m.x508 * ((-0.9047294977974201 + m.x13)
    **2 + (-0.7357904800445998 + m.x14)**2 + (-0.2819553446129277 + m.x15)**2)
    + m.x509 * ((-0.7274677561703813 + m.x13)**2 + (-0.6080547644274223 +
    m.x14)**2 + (-0.4688320743625637 + m.x15)**2) + m.x510 * ((
    -0.2549577045934236 + m.x13)**2 + (-0.11411488345784182 + m.x14)**2 + (
    -0.22595928823071643 + m.x15)**2) + m.x511 * ((-0.9849257452304463 + m.x13)
    **2 + (-0.9402085696377348 + m.x14)**2 + (-0.41737974889498053 + m.x15)**2)
    + m.x512 * ((-0.3062096299151559 + m.x13)**2 + (-0.5781338903934966 +
    m.x14)**2 + (-0.5836695539809419 + m.x15)**2) + m.x513 * ((
    -0.6555223295998597 + m.x13)**2 + (-0.11627198084637425 + m.x14)**2 + (
    -0.5340643666314074 + m.x15)**2) + m.x514 * ((-0.8167955181907369 + m.x13)
    **2 + (-0.6648304662656255 + m.x14)**2 + (-0.4344445572683132 + m.x15)**2)
    + m.x515 * ((-0.2627634068526804 + m.x13)**2 + (-0.8719643810841551 +
    m.x14)**2 + (-0.2782753479255554 + m.x15)**2))

m.e1 = Constraint(expr= m.x16 + m.x116 + m.x216 + m.x316 + m.x416 == 1)
m.e2 = Constraint(expr= m.x17 + m.x117 + m.x217 + m.x317 + m.x417 == 1)
m.e3 = Constraint(expr= m.x18 + m.x118 + m.x218 + m.x318 + m.x418 == 1)
m.e4 = Constraint(expr= m.x19 + m.x119 + m.x219 + m.x319 + m.x419 == 1)
m.e5 = Constraint(expr= m.x20 + m.x120 + m.x220 + m.x320 + m.x420 == 1)
m.e6 = Constraint(expr= m.x21 + m.x121 + m.x221 + m.x321 + m.x421 == 1)
m.e7 = Constraint(expr= m.x22 + m.x122 + m.x222 + m.x322 + m.x422 == 1)
m.e8 = Constraint(expr= m.x23 + m.x123 + m.x223 + m.x323 + m.x423 == 1)
m.e9 = Constraint(expr= m.x24 + m.x124 + m.x224 + m.x324 + m.x424 == 1)
m.e10 = Constraint(expr= m.x25 + m.x125 + m.x225 + m.x325 + m.x425 == 1)
m.e11 = Constraint(expr= m.x26 + m.x126 + m.x226 + m.x326 + m.x426 == 1)
m.e12 = Constraint(expr= m.x27 + m.x127 + m.x227 + m.x327 + m.x427 == 1)
m.e13 = Constraint(expr= m.x28 + m.x128 + m.x228 + m.x328 + m.x428 == 1)
m.e14 = Constraint(expr= m.x29 + m.x129 + m.x229 + m.x329 + m.x429 == 1)
m.e15 = Constraint(expr= m.x30 + m.x130 + m.x230 + m.x330 + m.x430 == 1)
m.e16 = Constraint(expr= m.x31 + m.x131 + m.x231 + m.x331 + m.x431 == 1)
m.e17 = Constraint(expr= m.x32 + m.x132 + m.x232 + m.x332 + m.x432 == 1)
m.e18 = Constraint(expr= m.x33 + m.x133 + m.x233 + m.x333 + m.x433 == 1)
m.e19 = Constraint(expr= m.x34 + m.x134 + m.x234 + m.x334 + m.x434 == 1)
m.e20 = Constraint(expr= m.x35 + m.x135 + m.x235 + m.x335 + m.x435 == 1)
m.e21 = Constraint(expr= m.x36 + m.x136 + m.x236 + m.x336 + m.x436 == 1)
m.e22 = Constraint(expr= m.x37 + m.x137 + m.x237 + m.x337 + m.x437 == 1)
m.e23 = Constraint(expr= m.x38 + m.x138 + m.x238 + m.x338 + m.x438 == 1)
m.e24 = Constraint(expr= m.x39 + m.x139 + m.x239 + m.x339 + m.x439 == 1)
m.e25 = Constraint(expr= m.x40 + m.x140 + m.x240 + m.x340 + m.x440 == 1)
m.e26 = Constraint(expr= m.x41 + m.x141 + m.x241 + m.x341 + m.x441 == 1)
m.e27 = Constraint(expr= m.x42 + m.x142 + m.x242 + m.x342 + m.x442 == 1)
m.e28 = Constraint(expr= m.x43 + m.x143 + m.x243 + m.x343 + m.x443 == 1)
m.e29 = Constraint(expr= m.x44 + m.x144 + m.x244 + m.x344 + m.x444 == 1)
m.e30 = Constraint(expr= m.x45 + m.x145 + m.x245 + m.x345 + m.x445 == 1)
m.e31 = Constraint(expr= m.x46 + m.x146 + m.x246 + m.x346 + m.x446 == 1)
m.e32 = Constraint(expr= m.x47 + m.x147 + m.x247 + m.x347 + m.x447 == 1)
m.e33 = Constraint(expr= m.x48 + m.x148 + m.x248 + m.x348 + m.x448 == 1)
m.e34 = Constraint(expr= m.x49 + m.x149 + m.x249 + m.x349 + m.x449 == 1)
m.e35 = Constraint(expr= m.x50 + m.x150 + m.x250 + m.x350 + m.x450 == 1)
m.e36 = Constraint(expr= m.x51 + m.x151 + m.x251 + m.x351 + m.x451 == 1)
m.e37 = Constraint(expr= m.x52 + m.x152 + m.x252 + m.x352 + m.x452 == 1)
m.e38 = Constraint(expr= m.x53 + m.x153 + m.x253 + m.x353 + m.x453 == 1)
m.e39 = Constraint(expr= m.x54 + m.x154 + m.x254 + m.x354 + m.x454 == 1)
m.e40 = Constraint(expr= m.x55 + m.x155 + m.x255 + m.x355 + m.x455 == 1)
m.e41 = Constraint(expr= m.x56 + m.x156 + m.x256 + m.x356 + m.x456 == 1)
m.e42 = Constraint(expr= m.x57 + m.x157 + m.x257 + m.x357 + m.x457 == 1)
m.e43 = Constraint(expr= m.x58 + m.x158 + m.x258 + m.x358 + m.x458 == 1)
m.e44 = Constraint(expr= m.x59 + m.x159 + m.x259 + m.x359 + m.x459 == 1)
m.e45 = Constraint(expr= m.x60 + m.x160 + m.x260 + m.x360 + m.x460 == 1)
m.e46 = Constraint(expr= m.x61 + m.x161 + m.x261 + m.x361 + m.x461 == 1)
m.e47 = Constraint(expr= m.x62 + m.x162 + m.x262 + m.x362 + m.x462 == 1)
m.e48 = Constraint(expr= m.x63 + m.x163 + m.x263 + m.x363 + m.x463 == 1)
m.e49 = Constraint(expr= m.x64 + m.x164 + m.x264 + m.x364 + m.x464 == 1)
m.e50 = Constraint(expr= m.x65 + m.x165 + m.x265 + m.x365 + m.x465 == 1)
m.e51 = Constraint(expr= m.x66 + m.x166 + m.x266 + m.x366 + m.x466 == 1)
m.e52 = Constraint(expr= m.x67 + m.x167 + m.x267 + m.x367 + m.x467 == 1)
m.e53 = Constraint(expr= m.x68 + m.x168 + m.x268 + m.x368 + m.x468 == 1)
m.e54 = Constraint(expr= m.x69 + m.x169 + m.x269 + m.x369 + m.x469 == 1)
m.e55 = Constraint(expr= m.x70 + m.x170 + m.x270 + m.x370 + m.x470 == 1)
m.e56 = Constraint(expr= m.x71 + m.x171 + m.x271 + m.x371 + m.x471 == 1)
m.e57 = Constraint(expr= m.x72 + m.x172 + m.x272 + m.x372 + m.x472 == 1)
m.e58 = Constraint(expr= m.x73 + m.x173 + m.x273 + m.x373 + m.x473 == 1)
m.e59 = Constraint(expr= m.x74 + m.x174 + m.x274 + m.x374 + m.x474 == 1)
m.e60 = Constraint(expr= m.x75 + m.x175 + m.x275 + m.x375 + m.x475 == 1)
m.e61 = Constraint(expr= m.x76 + m.x176 + m.x276 + m.x376 + m.x476 == 1)
m.e62 = Constraint(expr= m.x77 + m.x177 + m.x277 + m.x377 + m.x477 == 1)
m.e63 = Constraint(expr= m.x78 + m.x178 + m.x278 + m.x378 + m.x478 == 1)
m.e64 = Constraint(expr= m.x79 + m.x179 + m.x279 + m.x379 + m.x479 == 1)
m.e65 = Constraint(expr= m.x80 + m.x180 + m.x280 + m.x380 + m.x480 == 1)
m.e66 = Constraint(expr= m.x81 + m.x181 + m.x281 + m.x381 + m.x481 == 1)
m.e67 = Constraint(expr= m.x82 + m.x182 + m.x282 + m.x382 + m.x482 == 1)
m.e68 = Constraint(expr= m.x83 + m.x183 + m.x283 + m.x383 + m.x483 == 1)
m.e69 = Constraint(expr= m.x84 + m.x184 + m.x284 + m.x384 + m.x484 == 1)
m.e70 = Constraint(expr= m.x85 + m.x185 + m.x285 + m.x385 + m.x485 == 1)
m.e71 = Constraint(expr= m.x86 + m.x186 + m.x286 + m.x386 + m.x486 == 1)
m.e72 = Constraint(expr= m.x87 + m.x187 + m.x287 + m.x387 + m.x487 == 1)
m.e73 = Constraint(expr= m.x88 + m.x188 + m.x288 + m.x388 + m.x488 == 1)
m.e74 = Constraint(expr= m.x89 + m.x189 + m.x289 + m.x389 + m.x489 == 1)
m.e75 = Constraint(expr= m.x90 + m.x190 + m.x290 + m.x390 + m.x490 == 1)
m.e76 = Constraint(expr= m.x91 + m.x191 + m.x291 + m.x391 + m.x491 == 1)
m.e77 = Constraint(expr= m.x92 + m.x192 + m.x292 + m.x392 + m.x492 == 1)
m.e78 = Constraint(expr= m.x93 + m.x193 + m.x293 + m.x393 + m.x493 == 1)
m.e79 = Constraint(expr= m.x94 + m.x194 + m.x294 + m.x394 + m.x494 == 1)
m.e80 = Constraint(expr= m.x95 + m.x195 + m.x295 + m.x395 + m.x495 == 1)
m.e81 = Constraint(expr= m.x96 + m.x196 + m.x296 + m.x396 + m.x496 == 1)
m.e82 = Constraint(expr= m.x97 + m.x197 + m.x297 + m.x397 + m.x497 == 1)
m.e83 = Constraint(expr= m.x98 + m.x198 + m.x298 + m.x398 + m.x498 == 1)
m.e84 = Constraint(expr= m.x99 + m.x199 + m.x299 + m.x399 + m.x499 == 1)
m.e85 = Constraint(expr= m.x100 + m.x200 + m.x300 + m.x400 + m.x500 == 1)
m.e86 = Constraint(expr= m.x101 + m.x201 + m.x301 + m.x401 + m.x501 == 1)
m.e87 = Constraint(expr= m.x102 + m.x202 + m.x302 + m.x402 + m.x502 == 1)
m.e88 = Constraint(expr= m.x103 + m.x203 + m.x303 + m.x403 + m.x503 == 1)
m.e89 = Constraint(expr= m.x104 + m.x204 + m.x304 + m.x404 + m.x504 == 1)
m.e90 = Constraint(expr= m.x105 + m.x205 + m.x305 + m.x405 + m.x505 == 1)
m.e91 = Constraint(expr= m.x106 + m.x206 + m.x306 + m.x406 + m.x506 == 1)
m.e92 = Constraint(expr= m.x107 + m.x207 + m.x307 + m.x407 + m.x507 == 1)
m.e93 = Constraint(expr= m.x108 + m.x208 + m.x308 + m.x408 + m.x508 == 1)
m.e94 = Constraint(expr= m.x109 + m.x209 + m.x309 + m.x409 + m.x509 == 1)
m.e95 = Constraint(expr= m.x110 + m.x210 + m.x310 + m.x410 + m.x510 == 1)
m.e96 = Constraint(expr= m.x111 + m.x211 + m.x311 + m.x411 + m.x511 == 1)
m.e97 = Constraint(expr= m.x112 + m.x212 + m.x312 + m.x412 + m.x512 == 1)
m.e98 = Constraint(expr= m.x113 + m.x213 + m.x313 + m.x413 + m.x513 == 1)
m.e99 = Constraint(expr= m.x114 + m.x214 + m.x314 + m.x414 + m.x514 == 1)
m.e100 = Constraint(expr= m.x115 + m.x215 + m.x315 + m.x415 + m.x515 == 1)
