# NLP written by GAMS Convert at 05/15/24 11:48:02
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       100      100        0        0        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#       412      412        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       400      400        0
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

m.obj = Objective(sense=minimize, expr= m.x13 * ((-0.13387794947057807 + m.x1)
    **2 + (-0.42690367626117476 + m.x2)**2 + (-0.8521089176944486 + m.x3)**2)
    + m.x14 * ((-0.45141195547240787 + m.x1)**2 + (-0.23276575500936336 + m.x2)
    **2 + (-0.6685549968499559 + m.x3)**2) + m.x15 * ((-0.30597774121727117 +
    m.x1)**2 + (-0.5840851347084063 + m.x2)**2 + (-0.23012065877141608 + m.x3)
    **2) + m.x16 * ((-0.7558902791058655 + m.x1)**2 + (-0.05068872162955207 +
    m.x2)**2 + (-0.2892456744905897 + m.x3)**2) + m.x17 * ((-0.9295624768475662
    + m.x1)**2 + (-0.08669869080122583 + m.x2)**2 + (-0.39032407209267084 +
    m.x3)**2) + m.x18 * ((-0.1863721754637978 + m.x1)**2 + (
    -0.38136078758188585 + m.x2)**2 + (-0.5651584668070776 + m.x3)**2) + m.x19
    * ((-0.9543949857543553 + m.x1)**2 + (-0.9477493256969005 + m.x2)**2 + (
    -0.3092150209147405 + m.x3)**2) + m.x20 * ((-0.7646939426560075 + m.x1)**2
    + (-0.45895458252245525 + m.x2)**2 + (-0.10132366541532778 + m.x3)**2) +
    m.x21 * ((-0.26830114127671023 + m.x1)**2 + (-0.3175192066975744 + m.x2)**2
    + (-0.3971628150686213 + m.x3)**2) + m.x22 * ((-0.9976402405070389 + m.x1)
    **2 + (-0.8007630756489261 + m.x2)**2 + (-0.0955548312751 + m.x3)**2) +
    m.x23 * ((-0.5798696146044355 + m.x1)**2 + (-0.29183525723503223 + m.x2)**2
    + (-0.2600774464034179 + m.x3)**2) + m.x24 * ((-0.8733014194727232 + m.x1)
    **2 + (-0.0675353393368775 + m.x2)**2 + (-0.7346449916245452 + m.x3)**2) +
    m.x25 * ((-0.8879347151978697 + m.x1)**2 + (-0.0021441037308813637 + m.x2)
    **2 + (-0.29381156314304335 + m.x3)**2) + m.x26 * ((-0.7899560554306205 +
    m.x1)**2 + (-0.0470096870959813 + m.x2)**2 + (-0.36444750704939977 + m.x3)
    **2) + m.x27 * ((-0.2351423218255354 + m.x1)**2 + (-0.8860741867255272 +
    m.x2)**2 + (-0.8105571816203839 + m.x3)**2) + m.x28 * ((-0.7645699915307779
    + m.x1)**2 + (-0.2760450725864 + m.x2)**2 + (-0.112450897270851 + m.x3)**2)
    + m.x29 * ((-0.9042505623462239 + m.x1)**2 + (-0.22535684423096647 + m.x2)
    **2 + (-0.21601015353281194 + m.x3)**2) + m.x30 * ((-0.08142911761899607 +
    m.x1)**2 + (-0.8238662250465241 + m.x2)**2 + (-0.446656737627519 + m.x3)**2)
    + m.x31 * ((-0.17654844392892022 + m.x1)**2 + (-0.021661992025399646 +
    m.x2)**2 + (-0.458266931812237 + m.x3)**2) + m.x32 * ((-0.04161872249986398
    + m.x1)**2 + (-0.0023468770072303524 + m.x2)**2 + (-0.4757688536944913 +
    m.x3)**2) + m.x33 * ((-0.5636261500141898 + m.x1)**2 + (-0.5412243430430387
    + m.x2)**2 + (-0.9185262483505648 + m.x3)**2) + m.x34 * ((
    -0.04435102264542612 + m.x1)**2 + (-0.0664744839067668 + m.x2)**2 + (
    -0.09363032822552941 + m.x3)**2) + m.x35 * ((-0.6135920539700436 + m.x1)**2
    + (-0.6579236134549653 + m.x2)**2 + (-0.22712348289109685 + m.x3)**2) +
    m.x36 * ((-0.5743364963980989 + m.x1)**2 + (-0.05458134438985984 + m.x2)**2
    + (-0.12848471239608783 + m.x3)**2) + m.x37 * ((-0.27515857398419474 +
    m.x1)**2 + (-0.13553939615470956 + m.x2)**2 + (-0.2684559472460377 + m.x3)
    **2) + m.x38 * ((-0.2963470374342595 + m.x1)**2 + (-0.4095584319942964 +
    m.x2)**2 + (-0.8587587782336636 + m.x3)**2) + m.x39 * ((-0.7570885365520854
    + m.x1)**2 + (-0.8084347935423373 + m.x2)**2 + (-0.15715607299634216 +
    m.x3)**2) + m.x40 * ((-0.7938896644580142 + m.x1)**2 + (-0.3799882464987978
    + m.x2)**2 + (-0.9093771971095738 + m.x3)**2) + m.x41 * ((
    -0.6186079969859057 + m.x1)**2 + (-0.681062414997789 + m.x2)**2 + (
    -0.5860106249361481 + m.x3)**2) + m.x42 * ((-0.02194259412307442 + m.x1)**2
    + (-0.29702774354519546 + m.x2)**2 + (-0.175829273138026 + m.x3)**2) +
    m.x43 * ((-0.26447905881026157 + m.x1)**2 + (-0.7593566218800504 + m.x2)**2
    + (-0.39760960835759773 + m.x3)**2) + m.x44 * ((-0.13515510461378977 +
    m.x1)**2 + (-0.7972471604464993 + m.x2)**2 + (-0.28558211151639634 + m.x3)
    **2) + m.x45 * ((-0.10772008929383248 + m.x1)**2 + (-0.3773106522010563 +
    m.x2)**2 + (-0.35383902467655304 + m.x3)**2) + m.x46 * ((
    -0.5414010097257086 + m.x1)**2 + (-0.6549307552517842 + m.x2)**2 + (
    -0.7837403296992593 + m.x3)**2) + m.x47 * ((-0.5871205288256559 + m.x1)**2
    + (-0.4756887184289059 + m.x2)**2 + (-0.30355558496980317 + m.x3)**2) +
    m.x48 * ((-0.6709600289238528 + m.x1)**2 + (-0.7252859209840705 + m.x2)**2
    + (-0.8981223672754907 + m.x3)**2) + m.x49 * ((-0.656856404570921 + m.x1)
    **2 + (-0.8715951155421182 + m.x2)**2 + (-0.02388898086555402 + m.x3)**2)
    + m.x50 * ((-0.3192345609602486 + m.x1)**2 + (-0.31488479193964825 + m.x2)
    **2 + (-0.6614613888474193 + m.x3)**2) + m.x51 * ((-0.8417019897428525 +
    m.x1)**2 + (-0.616228537066301 + m.x2)**2 + (-0.26274228070501626 + m.x3)**
    2) + m.x52 * ((-0.5937030725992497 + m.x1)**2 + (-0.19842794521568063 +
    m.x2)**2 + (-0.5345101523423981 + m.x3)**2) + m.x53 * ((
    -0.03339359470546732 + m.x1)**2 + (-0.8108524191133987 + m.x2)**2 + (
    -0.9601346984817665 + m.x3)**2) + m.x54 * ((-0.19103752285334574 + m.x1)**2
    + (-0.6614849523412465 + m.x2)**2 + (-0.05950865757889012 + m.x3)**2) +
    m.x55 * ((-0.10783825889829635 + m.x1)**2 + (-0.5990086159395481 + m.x2)**2
    + (-0.06584564659599657 + m.x3)**2) + m.x56 * ((-0.41280452109378574 +
    m.x1)**2 + (-0.45708251074315276 + m.x2)**2 + (-0.788130361791057 + m.x3)**
    2) + m.x57 * ((-0.9077561322759368 + m.x1)**2 + (-0.4688875536818434 + m.x2)
    **2 + (-0.033133508346345764 + m.x3)**2) + m.x58 * ((-0.3273136285473489 +
    m.x1)**2 + (-0.15390437722631856 + m.x2)**2 + (-0.5114603037727307 + m.x3)
    **2) + m.x59 * ((-0.32464063107132457 + m.x1)**2 + (-0.318610062289566 +
    m.x2)**2 + (-0.5123014054919054 + m.x3)**2) + m.x60 * ((
    -0.39959901922907715 + m.x1)**2 + (-0.10577012066519309 + m.x2)**2 + (
    -0.8726622650936464 + m.x3)**2) + m.x61 * ((-0.35635136524528255 + m.x1)**2
    + (-0.1784345686896175 + m.x2)**2 + (-0.42289696970042434 + m.x3)**2) +
    m.x62 * ((-0.782747925998671 + m.x1)**2 + (-0.34740318908265166 + m.x2)**2
    + (-0.05029454996396343 + m.x3)**2) + m.x63 * ((-0.6181863895365817 + m.x1)
    **2 + (-0.8036374719444359 + m.x2)**2 + (-0.6267008774134815 + m.x3)**2) +
    m.x64 * ((-0.43827940620543104 + m.x1)**2 + (-0.2137204019393636 + m.x2)**2
    + (-0.06448972709664114 + m.x3)**2) + m.x65 * ((-0.6225649008635937 + m.x1)
    **2 + (-0.1486871314984446 + m.x2)**2 + (-0.9412847777465005 + m.x3)**2) +
    m.x66 * ((-0.35378600592620435 + m.x1)**2 + (-0.5094259314535285 + m.x2)**2
    + (-0.15017963251455024 + m.x3)**2) + m.x67 * ((-0.547736164631361 + m.x1)
    **2 + (-0.48529334266922364 + m.x2)**2 + (-0.7587795640672863 + m.x3)**2)
    + m.x68 * ((-0.975084772405915 + m.x1)**2 + (-0.13939912017193878 + m.x2)
    **2 + (-0.8727337834248664 + m.x3)**2) + m.x69 * ((-0.22427676001904484 +
    m.x1)**2 + (-0.5063957190827062 + m.x2)**2 + (-0.8854241674425338 + m.x3)**
    2) + m.x70 * ((-0.3810832957260354 + m.x1)**2 + (-0.34581416755281436 +
    m.x2)**2 + (-0.4406420710521176 + m.x3)**2) + m.x71 * ((-0.3499756386974382
    + m.x1)**2 + (-0.3566588105401399 + m.x2)**2 + (-0.44732858159739897 +
    m.x3)**2) + m.x72 * ((-0.5924763772089162 + m.x1)**2 + (-0.6286013706430164
    + m.x2)**2 + (-0.09398685721518818 + m.x3)**2) + m.x73 * ((
    -0.1689853036818748 + m.x1)**2 + (-0.30514010727298835 + m.x2)**2 + (
    -0.33603142248790296 + m.x3)**2) + m.x74 * ((-0.42582040151330736 + m.x1)**
    2 + (-0.5474773915330942 + m.x2)**2 + (-0.9968031768737334 + m.x3)**2) +
    m.x75 * ((-0.8310835234714565 + m.x1)**2 + (-0.900242213872515 + m.x2)**2
    + (-0.33176437156580707 + m.x3)**2) + m.x76 * ((-0.37583737986341104 +
    m.x1)**2 + (-0.7466408422154486 + m.x2)**2 + (-0.07941747226014839 + m.x3)
    **2) + m.x77 * ((-0.9322489792585174 + m.x1)**2 + (-0.5627545887233887 +
    m.x2)**2 + (-0.34051255992551555 + m.x3)**2) + m.x78 * ((
    -0.8322172992726823 + m.x1)**2 + (-0.7916032068893061 + m.x2)**2 + (
    -0.6267324024166224 + m.x3)**2) + m.x79 * ((-0.8270530442833851 + m.x1)**2
    + (-0.3943946960481908 + m.x2)**2 + (-0.19553764761383285 + m.x3)**2) +
    m.x80 * ((-0.18052910743135464 + m.x1)**2 + (-0.9897273639149909 + m.x2)**2
    + (-0.3977740348052199 + m.x3)**2) + m.x81 * ((-0.992075644189053 + m.x1)
    **2 + (-0.9013344575593397 + m.x2)**2 + (-0.9953811176046844 + m.x3)**2) +
    m.x82 * ((-0.37780737996640323 + m.x1)**2 + (-0.8839873246439367 + m.x2)**2
    + (-0.4632132536984095 + m.x3)**2) + m.x83 * ((-0.4156450632457209 + m.x1)
    **2 + (-0.5431767983808783 + m.x2)**2 + (-0.8023913074476225 + m.x3)**2) +
    m.x84 * ((-0.15352263703085378 + m.x1)**2 + (-0.10973315963577568 + m.x2)**
    2 + (-0.6454564663352736 + m.x3)**2) + m.x85 * ((-0.9145284924960414 + m.x1)
    **2 + (-0.9227933160830081 + m.x2)**2 + (-0.6810127986564416 + m.x3)**2) +
    m.x86 * ((-0.10615315400359326 + m.x1)**2 + (-0.5475134158722265 + m.x2)**2
    + (-0.1648548505370927 + m.x3)**2) + m.x87 * ((-0.026255737640514587 +
    m.x1)**2 + (-0.5596725842620359 + m.x2)**2 + (-0.2866191584187715 + m.x3)**
    2) + m.x88 * ((-0.336345726418656 + m.x1)**2 + (-0.17634404223572997 + m.x2)
    **2 + (-0.6202789464201214 + m.x3)**2) + m.x89 * ((-0.3046590255465387 +
    m.x1)**2 + (-0.4429200521217548 + m.x2)**2 + (-0.20698763213399418 + m.x3)
    **2) + m.x90 * ((-0.1874619228105564 + m.x1)**2 + (-0.4998350114658221 +
    m.x2)**2 + (-0.7615173896019674 + m.x3)**2) + m.x91 * ((-0.9066861882230548
    + m.x1)**2 + (-0.7195603347677635 + m.x2)**2 + (-0.06522609137561508 +
    m.x3)**2) + m.x92 * ((-0.7911200820552159 + m.x1)**2 + (-0.7315905893669585
    + m.x2)**2 + (-0.6317765913446202 + m.x3)**2) + m.x93 * ((
    -0.31382737215555745 + m.x1)**2 + (-0.7715540347231861 + m.x2)**2 + (
    -0.47573360893638406 + m.x3)**2) + m.x94 * ((-0.5397580555083911 + m.x1)**2
    + (-0.0663564438985641 + m.x2)**2 + (-0.8579557631163671 + m.x3)**2) +
    m.x95 * ((-0.14885341468069002 + m.x1)**2 + (-0.3011673371506899 + m.x2)**2
    + (-0.8781667094774749 + m.x3)**2) + m.x96 * ((-0.9135956838011015 + m.x1)
    **2 + (-0.8672955274928783 + m.x2)**2 + (-0.8369181521121158 + m.x3)**2) +
    m.x97 * ((-0.970025910323361 + m.x1)**2 + (-0.051039365966057626 + m.x2)**2
    + (-0.33776762446434627 + m.x3)**2) + m.x98 * ((-0.15627515420259408 +
    m.x1)**2 + (-0.04035561224618667 + m.x2)**2 + (-0.9808630027608929 + m.x3)
    **2) + m.x99 * ((-0.5997238405427903 + m.x1)**2 + (-0.6340595771156888 +
    m.x2)**2 + (-0.03244563724419325 + m.x3)**2) + m.x100 * ((
    -0.48170623571049465 + m.x1)**2 + (-0.36217785579647566 + m.x2)**2 + (
    -0.9890880708785992 + m.x3)**2) + m.x101 * ((-0.41432137103971445 + m.x1)**
    2 + (-0.19729280755091372 + m.x2)**2 + (-0.6779738469638877 + m.x3)**2) +
    m.x102 * ((-0.44474166469461696 + m.x1)**2 + (-0.2643829797481405 + m.x2)**
    2 + (-0.6562475297685736 + m.x3)**2) + m.x103 * ((-0.6275499840460776 +
    m.x1)**2 + (-0.6100027667466603 + m.x2)**2 + (-0.7498874717615438 + m.x3)**
    2) + m.x104 * ((-0.7377870812034109 + m.x1)**2 + (-0.8635522742958053 +
    m.x2)**2 + (-0.8191133594808159 + m.x3)**2) + m.x105 * ((
    -0.07163384061097833 + m.x1)**2 + (-0.02997713929225343 + m.x2)**2 + (
    -0.27725110161661115 + m.x3)**2) + m.x106 * ((-0.5441338528113598 + m.x1)**
    2 + (-0.0030790728595536665 + m.x2)**2 + (-0.04235938308887821 + m.x3)**2)
    + m.x107 * ((-0.2235362539846405 + m.x1)**2 + (-0.942738774197919 + m.x2)
    **2 + (-0.727537913915035 + m.x3)**2) + m.x108 * ((-0.530616616437767 +
    m.x1)**2 + (-0.07076562154177557 + m.x2)**2 + (-0.5662780949982541 + m.x3)
    **2) + m.x109 * ((-0.985894167192254 + m.x1)**2 + (-0.10185959622013296 +
    m.x2)**2 + (-0.5697892250475037 + m.x3)**2) + m.x110 * ((
    -0.1384396368632138 + m.x1)**2 + (-0.784842787064432 + m.x2)**2 + (
    -0.2014860384245054 + m.x3)**2) + m.x111 * ((-0.025313323494474682 + m.x1)
    **2 + (-0.25046029857714547 + m.x2)**2 + (-0.61170855488363 + m.x3)**2) +
    m.x112 * ((-0.16543698841012866 + m.x1)**2 + (-0.6004755305634034 + m.x2)**
    2 + (-0.8627316624555801 + m.x3)**2) + m.x113 * ((-0.13387794947057807 +
    m.x4)**2 + (-0.42690367626117476 + m.x5)**2 + (-0.8521089176944486 + m.x6)
    **2) + m.x114 * ((-0.45141195547240787 + m.x4)**2 + (-0.23276575500936336
    + m.x5)**2 + (-0.6685549968499559 + m.x6)**2) + m.x115 * ((
    -0.30597774121727117 + m.x4)**2 + (-0.5840851347084063 + m.x5)**2 + (
    -0.23012065877141608 + m.x6)**2) + m.x116 * ((-0.7558902791058655 + m.x4)**
    2 + (-0.05068872162955207 + m.x5)**2 + (-0.2892456744905897 + m.x6)**2) +
    m.x117 * ((-0.9295624768475662 + m.x4)**2 + (-0.08669869080122583 + m.x5)**
    2 + (-0.39032407209267084 + m.x6)**2) + m.x118 * ((-0.1863721754637978 +
    m.x4)**2 + (-0.38136078758188585 + m.x5)**2 + (-0.5651584668070776 + m.x6)
    **2) + m.x119 * ((-0.9543949857543553 + m.x4)**2 + (-0.9477493256969005 +
    m.x5)**2 + (-0.3092150209147405 + m.x6)**2) + m.x120 * ((
    -0.7646939426560075 + m.x4)**2 + (-0.45895458252245525 + m.x5)**2 + (
    -0.10132366541532778 + m.x6)**2) + m.x121 * ((-0.26830114127671023 + m.x4)
    **2 + (-0.3175192066975744 + m.x5)**2 + (-0.3971628150686213 + m.x6)**2) +
    m.x122 * ((-0.9976402405070389 + m.x4)**2 + (-0.8007630756489261 + m.x5)**2
    + (-0.0955548312751 + m.x6)**2) + m.x123 * ((-0.5798696146044355 + m.x4)**
    2 + (-0.29183525723503223 + m.x5)**2 + (-0.2600774464034179 + m.x6)**2) +
    m.x124 * ((-0.8733014194727232 + m.x4)**2 + (-0.0675353393368775 + m.x5)**2
    + (-0.7346449916245452 + m.x6)**2) + m.x125 * ((-0.8879347151978697 + m.x4)
    **2 + (-0.0021441037308813637 + m.x5)**2 + (-0.29381156314304335 + m.x6)**2)
    + m.x126 * ((-0.7899560554306205 + m.x4)**2 + (-0.0470096870959813 + m.x5)
    **2 + (-0.36444750704939977 + m.x6)**2) + m.x127 * ((-0.2351423218255354 +
    m.x4)**2 + (-0.8860741867255272 + m.x5)**2 + (-0.8105571816203839 + m.x6)**
    2) + m.x128 * ((-0.7645699915307779 + m.x4)**2 + (-0.2760450725864 + m.x5)
    **2 + (-0.112450897270851 + m.x6)**2) + m.x129 * ((-0.9042505623462239 +
    m.x4)**2 + (-0.22535684423096647 + m.x5)**2 + (-0.21601015353281194 + m.x6)
    **2) + m.x130 * ((-0.08142911761899607 + m.x4)**2 + (-0.8238662250465241 +
    m.x5)**2 + (-0.446656737627519 + m.x6)**2) + m.x131 * ((
    -0.17654844392892022 + m.x4)**2 + (-0.021661992025399646 + m.x5)**2 + (
    -0.458266931812237 + m.x6)**2) + m.x132 * ((-0.04161872249986398 + m.x4)**2
    + (-0.0023468770072303524 + m.x5)**2 + (-0.4757688536944913 + m.x6)**2) +
    m.x133 * ((-0.5636261500141898 + m.x4)**2 + (-0.5412243430430387 + m.x5)**2
    + (-0.9185262483505648 + m.x6)**2) + m.x134 * ((-0.04435102264542612 +
    m.x4)**2 + (-0.0664744839067668 + m.x5)**2 + (-0.09363032822552941 + m.x6)
    **2) + m.x135 * ((-0.6135920539700436 + m.x4)**2 + (-0.6579236134549653 +
    m.x5)**2 + (-0.22712348289109685 + m.x6)**2) + m.x136 * ((
    -0.5743364963980989 + m.x4)**2 + (-0.05458134438985984 + m.x5)**2 + (
    -0.12848471239608783 + m.x6)**2) + m.x137 * ((-0.27515857398419474 + m.x4)
    **2 + (-0.13553939615470956 + m.x5)**2 + (-0.2684559472460377 + m.x6)**2)
    + m.x138 * ((-0.2963470374342595 + m.x4)**2 + (-0.4095584319942964 + m.x5)
    **2 + (-0.8587587782336636 + m.x6)**2) + m.x139 * ((-0.7570885365520854 +
    m.x4)**2 + (-0.8084347935423373 + m.x5)**2 + (-0.15715607299634216 + m.x6)
    **2) + m.x140 * ((-0.7938896644580142 + m.x4)**2 + (-0.3799882464987978 +
    m.x5)**2 + (-0.9093771971095738 + m.x6)**2) + m.x141 * ((
    -0.6186079969859057 + m.x4)**2 + (-0.681062414997789 + m.x5)**2 + (
    -0.5860106249361481 + m.x6)**2) + m.x142 * ((-0.02194259412307442 + m.x4)**
    2 + (-0.29702774354519546 + m.x5)**2 + (-0.175829273138026 + m.x6)**2) +
    m.x143 * ((-0.26447905881026157 + m.x4)**2 + (-0.7593566218800504 + m.x5)**
    2 + (-0.39760960835759773 + m.x6)**2) + m.x144 * ((-0.13515510461378977 +
    m.x4)**2 + (-0.7972471604464993 + m.x5)**2 + (-0.28558211151639634 + m.x6)
    **2) + m.x145 * ((-0.10772008929383248 + m.x4)**2 + (-0.3773106522010563 +
    m.x5)**2 + (-0.35383902467655304 + m.x6)**2) + m.x146 * ((
    -0.5414010097257086 + m.x4)**2 + (-0.6549307552517842 + m.x5)**2 + (
    -0.7837403296992593 + m.x6)**2) + m.x147 * ((-0.5871205288256559 + m.x4)**2
    + (-0.4756887184289059 + m.x5)**2 + (-0.30355558496980317 + m.x6)**2) +
    m.x148 * ((-0.6709600289238528 + m.x4)**2 + (-0.7252859209840705 + m.x5)**2
    + (-0.8981223672754907 + m.x6)**2) + m.x149 * ((-0.656856404570921 + m.x4)
    **2 + (-0.8715951155421182 + m.x5)**2 + (-0.02388898086555402 + m.x6)**2)
    + m.x150 * ((-0.3192345609602486 + m.x4)**2 + (-0.31488479193964825 + m.x5)
    **2 + (-0.6614613888474193 + m.x6)**2) + m.x151 * ((-0.8417019897428525 +
    m.x4)**2 + (-0.616228537066301 + m.x5)**2 + (-0.26274228070501626 + m.x6)**
    2) + m.x152 * ((-0.5937030725992497 + m.x4)**2 + (-0.19842794521568063 +
    m.x5)**2 + (-0.5345101523423981 + m.x6)**2) + m.x153 * ((
    -0.03339359470546732 + m.x4)**2 + (-0.8108524191133987 + m.x5)**2 + (
    -0.9601346984817665 + m.x6)**2) + m.x154 * ((-0.19103752285334574 + m.x4)**
    2 + (-0.6614849523412465 + m.x5)**2 + (-0.05950865757889012 + m.x6)**2) +
    m.x155 * ((-0.10783825889829635 + m.x4)**2 + (-0.5990086159395481 + m.x5)**
    2 + (-0.06584564659599657 + m.x6)**2) + m.x156 * ((-0.41280452109378574 +
    m.x4)**2 + (-0.45708251074315276 + m.x5)**2 + (-0.788130361791057 + m.x6)**
    2) + m.x157 * ((-0.9077561322759368 + m.x4)**2 + (-0.4688875536818434 +
    m.x5)**2 + (-0.033133508346345764 + m.x6)**2) + m.x158 * ((
    -0.3273136285473489 + m.x4)**2 + (-0.15390437722631856 + m.x5)**2 + (
    -0.5114603037727307 + m.x6)**2) + m.x159 * ((-0.32464063107132457 + m.x4)**
    2 + (-0.318610062289566 + m.x5)**2 + (-0.5123014054919054 + m.x6)**2) +
    m.x160 * ((-0.39959901922907715 + m.x4)**2 + (-0.10577012066519309 + m.x5)
    **2 + (-0.8726622650936464 + m.x6)**2) + m.x161 * ((-0.35635136524528255 +
    m.x4)**2 + (-0.1784345686896175 + m.x5)**2 + (-0.42289696970042434 + m.x6)
    **2) + m.x162 * ((-0.782747925998671 + m.x4)**2 + (-0.34740318908265166 +
    m.x5)**2 + (-0.05029454996396343 + m.x6)**2) + m.x163 * ((
    -0.6181863895365817 + m.x4)**2 + (-0.8036374719444359 + m.x5)**2 + (
    -0.6267008774134815 + m.x6)**2) + m.x164 * ((-0.43827940620543104 + m.x4)**
    2 + (-0.2137204019393636 + m.x5)**2 + (-0.06448972709664114 + m.x6)**2) +
    m.x165 * ((-0.6225649008635937 + m.x4)**2 + (-0.1486871314984446 + m.x5)**2
    + (-0.9412847777465005 + m.x6)**2) + m.x166 * ((-0.35378600592620435 +
    m.x4)**2 + (-0.5094259314535285 + m.x5)**2 + (-0.15017963251455024 + m.x6)
    **2) + m.x167 * ((-0.547736164631361 + m.x4)**2 + (-0.48529334266922364 +
    m.x5)**2 + (-0.7587795640672863 + m.x6)**2) + m.x168 * ((-0.975084772405915
    + m.x4)**2 + (-0.13939912017193878 + m.x5)**2 + (-0.8727337834248664 +
    m.x6)**2) + m.x169 * ((-0.22427676001904484 + m.x4)**2 + (
    -0.5063957190827062 + m.x5)**2 + (-0.8854241674425338 + m.x6)**2) + m.x170
    * ((-0.3810832957260354 + m.x4)**2 + (-0.34581416755281436 + m.x5)**2 + (
    -0.4406420710521176 + m.x6)**2) + m.x171 * ((-0.3499756386974382 + m.x4)**2
    + (-0.3566588105401399 + m.x5)**2 + (-0.44732858159739897 + m.x6)**2) +
    m.x172 * ((-0.5924763772089162 + m.x4)**2 + (-0.6286013706430164 + m.x5)**2
    + (-0.09398685721518818 + m.x6)**2) + m.x173 * ((-0.1689853036818748 +
    m.x4)**2 + (-0.30514010727298835 + m.x5)**2 + (-0.33603142248790296 + m.x6)
    **2) + m.x174 * ((-0.42582040151330736 + m.x4)**2 + (-0.5474773915330942 +
    m.x5)**2 + (-0.9968031768737334 + m.x6)**2) + m.x175 * ((
    -0.8310835234714565 + m.x4)**2 + (-0.900242213872515 + m.x5)**2 + (
    -0.33176437156580707 + m.x6)**2) + m.x176 * ((-0.37583737986341104 + m.x4)
    **2 + (-0.7466408422154486 + m.x5)**2 + (-0.07941747226014839 + m.x6)**2)
    + m.x177 * ((-0.9322489792585174 + m.x4)**2 + (-0.5627545887233887 + m.x5)
    **2 + (-0.34051255992551555 + m.x6)**2) + m.x178 * ((-0.8322172992726823 +
    m.x4)**2 + (-0.7916032068893061 + m.x5)**2 + (-0.6267324024166224 + m.x6)**
    2) + m.x179 * ((-0.8270530442833851 + m.x4)**2 + (-0.3943946960481908 +
    m.x5)**2 + (-0.19553764761383285 + m.x6)**2) + m.x180 * ((
    -0.18052910743135464 + m.x4)**2 + (-0.9897273639149909 + m.x5)**2 + (
    -0.3977740348052199 + m.x6)**2) + m.x181 * ((-0.992075644189053 + m.x4)**2
    + (-0.9013344575593397 + m.x5)**2 + (-0.9953811176046844 + m.x6)**2) +
    m.x182 * ((-0.37780737996640323 + m.x4)**2 + (-0.8839873246439367 + m.x5)**
    2 + (-0.4632132536984095 + m.x6)**2) + m.x183 * ((-0.4156450632457209 +
    m.x4)**2 + (-0.5431767983808783 + m.x5)**2 + (-0.8023913074476225 + m.x6)**
    2) + m.x184 * ((-0.15352263703085378 + m.x4)**2 + (-0.10973315963577568 +
    m.x5)**2 + (-0.6454564663352736 + m.x6)**2) + m.x185 * ((
    -0.9145284924960414 + m.x4)**2 + (-0.9227933160830081 + m.x5)**2 + (
    -0.6810127986564416 + m.x6)**2) + m.x186 * ((-0.10615315400359326 + m.x4)**
    2 + (-0.5475134158722265 + m.x5)**2 + (-0.1648548505370927 + m.x6)**2) +
    m.x187 * ((-0.026255737640514587 + m.x4)**2 + (-0.5596725842620359 + m.x5)
    **2 + (-0.2866191584187715 + m.x6)**2) + m.x188 * ((-0.336345726418656 +
    m.x4)**2 + (-0.17634404223572997 + m.x5)**2 + (-0.6202789464201214 + m.x6)
    **2) + m.x189 * ((-0.3046590255465387 + m.x4)**2 + (-0.4429200521217548 +
    m.x5)**2 + (-0.20698763213399418 + m.x6)**2) + m.x190 * ((
    -0.1874619228105564 + m.x4)**2 + (-0.4998350114658221 + m.x5)**2 + (
    -0.7615173896019674 + m.x6)**2) + m.x191 * ((-0.9066861882230548 + m.x4)**2
    + (-0.7195603347677635 + m.x5)**2 + (-0.06522609137561508 + m.x6)**2) +
    m.x192 * ((-0.7911200820552159 + m.x4)**2 + (-0.7315905893669585 + m.x5)**2
    + (-0.6317765913446202 + m.x6)**2) + m.x193 * ((-0.31382737215555745 +
    m.x4)**2 + (-0.7715540347231861 + m.x5)**2 + (-0.47573360893638406 + m.x6)
    **2) + m.x194 * ((-0.5397580555083911 + m.x4)**2 + (-0.0663564438985641 +
    m.x5)**2 + (-0.8579557631163671 + m.x6)**2) + m.x195 * ((
    -0.14885341468069002 + m.x4)**2 + (-0.3011673371506899 + m.x5)**2 + (
    -0.8781667094774749 + m.x6)**2) + m.x196 * ((-0.9135956838011015 + m.x4)**2
    + (-0.8672955274928783 + m.x5)**2 + (-0.8369181521121158 + m.x6)**2) +
    m.x197 * ((-0.970025910323361 + m.x4)**2 + (-0.051039365966057626 + m.x5)**
    2 + (-0.33776762446434627 + m.x6)**2) + m.x198 * ((-0.15627515420259408 +
    m.x4)**2 + (-0.04035561224618667 + m.x5)**2 + (-0.9808630027608929 + m.x6)
    **2) + m.x199 * ((-0.5997238405427903 + m.x4)**2 + (-0.6340595771156888 +
    m.x5)**2 + (-0.03244563724419325 + m.x6)**2) + m.x200 * ((
    -0.48170623571049465 + m.x4)**2 + (-0.36217785579647566 + m.x5)**2 + (
    -0.9890880708785992 + m.x6)**2) + m.x201 * ((-0.41432137103971445 + m.x4)**
    2 + (-0.19729280755091372 + m.x5)**2 + (-0.6779738469638877 + m.x6)**2) +
    m.x202 * ((-0.44474166469461696 + m.x4)**2 + (-0.2643829797481405 + m.x5)**
    2 + (-0.6562475297685736 + m.x6)**2) + m.x203 * ((-0.6275499840460776 +
    m.x4)**2 + (-0.6100027667466603 + m.x5)**2 + (-0.7498874717615438 + m.x6)**
    2) + m.x204 * ((-0.7377870812034109 + m.x4)**2 + (-0.8635522742958053 +
    m.x5)**2 + (-0.8191133594808159 + m.x6)**2) + m.x205 * ((
    -0.07163384061097833 + m.x4)**2 + (-0.02997713929225343 + m.x5)**2 + (
    -0.27725110161661115 + m.x6)**2) + m.x206 * ((-0.5441338528113598 + m.x4)**
    2 + (-0.0030790728595536665 + m.x5)**2 + (-0.04235938308887821 + m.x6)**2)
    + m.x207 * ((-0.2235362539846405 + m.x4)**2 + (-0.942738774197919 + m.x5)
    **2 + (-0.727537913915035 + m.x6)**2) + m.x208 * ((-0.530616616437767 +
    m.x4)**2 + (-0.07076562154177557 + m.x5)**2 + (-0.5662780949982541 + m.x6)
    **2) + m.x209 * ((-0.985894167192254 + m.x4)**2 + (-0.10185959622013296 +
    m.x5)**2 + (-0.5697892250475037 + m.x6)**2) + m.x210 * ((
    -0.1384396368632138 + m.x4)**2 + (-0.784842787064432 + m.x5)**2 + (
    -0.2014860384245054 + m.x6)**2) + m.x211 * ((-0.025313323494474682 + m.x4)
    **2 + (-0.25046029857714547 + m.x5)**2 + (-0.61170855488363 + m.x6)**2) +
    m.x212 * ((-0.16543698841012866 + m.x4)**2 + (-0.6004755305634034 + m.x5)**
    2 + (-0.8627316624555801 + m.x6)**2) + m.x213 * ((-0.13387794947057807 +
    m.x7)**2 + (-0.42690367626117476 + m.x8)**2 + (-0.8521089176944486 + m.x9)
    **2) + m.x214 * ((-0.45141195547240787 + m.x7)**2 + (-0.23276575500936336
    + m.x8)**2 + (-0.6685549968499559 + m.x9)**2) + m.x215 * ((
    -0.30597774121727117 + m.x7)**2 + (-0.5840851347084063 + m.x8)**2 + (
    -0.23012065877141608 + m.x9)**2) + m.x216 * ((-0.7558902791058655 + m.x7)**
    2 + (-0.05068872162955207 + m.x8)**2 + (-0.2892456744905897 + m.x9)**2) +
    m.x217 * ((-0.9295624768475662 + m.x7)**2 + (-0.08669869080122583 + m.x8)**
    2 + (-0.39032407209267084 + m.x9)**2) + m.x218 * ((-0.1863721754637978 +
    m.x7)**2 + (-0.38136078758188585 + m.x8)**2 + (-0.5651584668070776 + m.x9)
    **2) + m.x219 * ((-0.9543949857543553 + m.x7)**2 + (-0.9477493256969005 +
    m.x8)**2 + (-0.3092150209147405 + m.x9)**2) + m.x220 * ((
    -0.7646939426560075 + m.x7)**2 + (-0.45895458252245525 + m.x8)**2 + (
    -0.10132366541532778 + m.x9)**2) + m.x221 * ((-0.26830114127671023 + m.x7)
    **2 + (-0.3175192066975744 + m.x8)**2 + (-0.3971628150686213 + m.x9)**2) +
    m.x222 * ((-0.9976402405070389 + m.x7)**2 + (-0.8007630756489261 + m.x8)**2
    + (-0.0955548312751 + m.x9)**2) + m.x223 * ((-0.5798696146044355 + m.x7)**
    2 + (-0.29183525723503223 + m.x8)**2 + (-0.2600774464034179 + m.x9)**2) +
    m.x224 * ((-0.8733014194727232 + m.x7)**2 + (-0.0675353393368775 + m.x8)**2
    + (-0.7346449916245452 + m.x9)**2) + m.x225 * ((-0.8879347151978697 + m.x7)
    **2 + (-0.0021441037308813637 + m.x8)**2 + (-0.29381156314304335 + m.x9)**2)
    + m.x226 * ((-0.7899560554306205 + m.x7)**2 + (-0.0470096870959813 + m.x8)
    **2 + (-0.36444750704939977 + m.x9)**2) + m.x227 * ((-0.2351423218255354 +
    m.x7)**2 + (-0.8860741867255272 + m.x8)**2 + (-0.8105571816203839 + m.x9)**
    2) + m.x228 * ((-0.7645699915307779 + m.x7)**2 + (-0.2760450725864 + m.x8)
    **2 + (-0.112450897270851 + m.x9)**2) + m.x229 * ((-0.9042505623462239 +
    m.x7)**2 + (-0.22535684423096647 + m.x8)**2 + (-0.21601015353281194 + m.x9)
    **2) + m.x230 * ((-0.08142911761899607 + m.x7)**2 + (-0.8238662250465241 +
    m.x8)**2 + (-0.446656737627519 + m.x9)**2) + m.x231 * ((
    -0.17654844392892022 + m.x7)**2 + (-0.021661992025399646 + m.x8)**2 + (
    -0.458266931812237 + m.x9)**2) + m.x232 * ((-0.04161872249986398 + m.x7)**2
    + (-0.0023468770072303524 + m.x8)**2 + (-0.4757688536944913 + m.x9)**2) +
    m.x233 * ((-0.5636261500141898 + m.x7)**2 + (-0.5412243430430387 + m.x8)**2
    + (-0.9185262483505648 + m.x9)**2) + m.x234 * ((-0.04435102264542612 +
    m.x7)**2 + (-0.0664744839067668 + m.x8)**2 + (-0.09363032822552941 + m.x9)
    **2) + m.x235 * ((-0.6135920539700436 + m.x7)**2 + (-0.6579236134549653 +
    m.x8)**2 + (-0.22712348289109685 + m.x9)**2) + m.x236 * ((
    -0.5743364963980989 + m.x7)**2 + (-0.05458134438985984 + m.x8)**2 + (
    -0.12848471239608783 + m.x9)**2) + m.x237 * ((-0.27515857398419474 + m.x7)
    **2 + (-0.13553939615470956 + m.x8)**2 + (-0.2684559472460377 + m.x9)**2)
    + m.x238 * ((-0.2963470374342595 + m.x7)**2 + (-0.4095584319942964 + m.x8)
    **2 + (-0.8587587782336636 + m.x9)**2) + m.x239 * ((-0.7570885365520854 +
    m.x7)**2 + (-0.8084347935423373 + m.x8)**2 + (-0.15715607299634216 + m.x9)
    **2) + m.x240 * ((-0.7938896644580142 + m.x7)**2 + (-0.3799882464987978 +
    m.x8)**2 + (-0.9093771971095738 + m.x9)**2) + m.x241 * ((
    -0.6186079969859057 + m.x7)**2 + (-0.681062414997789 + m.x8)**2 + (
    -0.5860106249361481 + m.x9)**2) + m.x242 * ((-0.02194259412307442 + m.x7)**
    2 + (-0.29702774354519546 + m.x8)**2 + (-0.175829273138026 + m.x9)**2) +
    m.x243 * ((-0.26447905881026157 + m.x7)**2 + (-0.7593566218800504 + m.x8)**
    2 + (-0.39760960835759773 + m.x9)**2) + m.x244 * ((-0.13515510461378977 +
    m.x7)**2 + (-0.7972471604464993 + m.x8)**2 + (-0.28558211151639634 + m.x9)
    **2) + m.x245 * ((-0.10772008929383248 + m.x7)**2 + (-0.3773106522010563 +
    m.x8)**2 + (-0.35383902467655304 + m.x9)**2) + m.x246 * ((
    -0.5414010097257086 + m.x7)**2 + (-0.6549307552517842 + m.x8)**2 + (
    -0.7837403296992593 + m.x9)**2) + m.x247 * ((-0.5871205288256559 + m.x7)**2
    + (-0.4756887184289059 + m.x8)**2 + (-0.30355558496980317 + m.x9)**2) +
    m.x248 * ((-0.6709600289238528 + m.x7)**2 + (-0.7252859209840705 + m.x8)**2
    + (-0.8981223672754907 + m.x9)**2) + m.x249 * ((-0.656856404570921 + m.x7)
    **2 + (-0.8715951155421182 + m.x8)**2 + (-0.02388898086555402 + m.x9)**2)
    + m.x250 * ((-0.3192345609602486 + m.x7)**2 + (-0.31488479193964825 + m.x8)
    **2 + (-0.6614613888474193 + m.x9)**2) + m.x251 * ((-0.8417019897428525 +
    m.x7)**2 + (-0.616228537066301 + m.x8)**2 + (-0.26274228070501626 + m.x9)**
    2) + m.x252 * ((-0.5937030725992497 + m.x7)**2 + (-0.19842794521568063 +
    m.x8)**2 + (-0.5345101523423981 + m.x9)**2) + m.x253 * ((
    -0.03339359470546732 + m.x7)**2 + (-0.8108524191133987 + m.x8)**2 + (
    -0.9601346984817665 + m.x9)**2) + m.x254 * ((-0.19103752285334574 + m.x7)**
    2 + (-0.6614849523412465 + m.x8)**2 + (-0.05950865757889012 + m.x9)**2) +
    m.x255 * ((-0.10783825889829635 + m.x7)**2 + (-0.5990086159395481 + m.x8)**
    2 + (-0.06584564659599657 + m.x9)**2) + m.x256 * ((-0.41280452109378574 +
    m.x7)**2 + (-0.45708251074315276 + m.x8)**2 + (-0.788130361791057 + m.x9)**
    2) + m.x257 * ((-0.9077561322759368 + m.x7)**2 + (-0.4688875536818434 +
    m.x8)**2 + (-0.033133508346345764 + m.x9)**2) + m.x258 * ((
    -0.3273136285473489 + m.x7)**2 + (-0.15390437722631856 + m.x8)**2 + (
    -0.5114603037727307 + m.x9)**2) + m.x259 * ((-0.32464063107132457 + m.x7)**
    2 + (-0.318610062289566 + m.x8)**2 + (-0.5123014054919054 + m.x9)**2) +
    m.x260 * ((-0.39959901922907715 + m.x7)**2 + (-0.10577012066519309 + m.x8)
    **2 + (-0.8726622650936464 + m.x9)**2) + m.x261 * ((-0.35635136524528255 +
    m.x7)**2 + (-0.1784345686896175 + m.x8)**2 + (-0.42289696970042434 + m.x9)
    **2) + m.x262 * ((-0.782747925998671 + m.x7)**2 + (-0.34740318908265166 +
    m.x8)**2 + (-0.05029454996396343 + m.x9)**2) + m.x263 * ((
    -0.6181863895365817 + m.x7)**2 + (-0.8036374719444359 + m.x8)**2 + (
    -0.6267008774134815 + m.x9)**2) + m.x264 * ((-0.43827940620543104 + m.x7)**
    2 + (-0.2137204019393636 + m.x8)**2 + (-0.06448972709664114 + m.x9)**2) +
    m.x265 * ((-0.6225649008635937 + m.x7)**2 + (-0.1486871314984446 + m.x8)**2
    + (-0.9412847777465005 + m.x9)**2) + m.x266 * ((-0.35378600592620435 +
    m.x7)**2 + (-0.5094259314535285 + m.x8)**2 + (-0.15017963251455024 + m.x9)
    **2) + m.x267 * ((-0.547736164631361 + m.x7)**2 + (-0.48529334266922364 +
    m.x8)**2 + (-0.7587795640672863 + m.x9)**2) + m.x268 * ((-0.975084772405915
    + m.x7)**2 + (-0.13939912017193878 + m.x8)**2 + (-0.8727337834248664 +
    m.x9)**2) + m.x269 * ((-0.22427676001904484 + m.x7)**2 + (
    -0.5063957190827062 + m.x8)**2 + (-0.8854241674425338 + m.x9)**2) + m.x270
    * ((-0.3810832957260354 + m.x7)**2 + (-0.34581416755281436 + m.x8)**2 + (
    -0.4406420710521176 + m.x9)**2) + m.x271 * ((-0.3499756386974382 + m.x7)**2
    + (-0.3566588105401399 + m.x8)**2 + (-0.44732858159739897 + m.x9)**2) +
    m.x272 * ((-0.5924763772089162 + m.x7)**2 + (-0.6286013706430164 + m.x8)**2
    + (-0.09398685721518818 + m.x9)**2) + m.x273 * ((-0.1689853036818748 +
    m.x7)**2 + (-0.30514010727298835 + m.x8)**2 + (-0.33603142248790296 + m.x9)
    **2) + m.x274 * ((-0.42582040151330736 + m.x7)**2 + (-0.5474773915330942 +
    m.x8)**2 + (-0.9968031768737334 + m.x9)**2) + m.x275 * ((
    -0.8310835234714565 + m.x7)**2 + (-0.900242213872515 + m.x8)**2 + (
    -0.33176437156580707 + m.x9)**2) + m.x276 * ((-0.37583737986341104 + m.x7)
    **2 + (-0.7466408422154486 + m.x8)**2 + (-0.07941747226014839 + m.x9)**2)
    + m.x277 * ((-0.9322489792585174 + m.x7)**2 + (-0.5627545887233887 + m.x8)
    **2 + (-0.34051255992551555 + m.x9)**2) + m.x278 * ((-0.8322172992726823 +
    m.x7)**2 + (-0.7916032068893061 + m.x8)**2 + (-0.6267324024166224 + m.x9)**
    2) + m.x279 * ((-0.8270530442833851 + m.x7)**2 + (-0.3943946960481908 +
    m.x8)**2 + (-0.19553764761383285 + m.x9)**2) + m.x280 * ((
    -0.18052910743135464 + m.x7)**2 + (-0.9897273639149909 + m.x8)**2 + (
    -0.3977740348052199 + m.x9)**2) + m.x281 * ((-0.992075644189053 + m.x7)**2
    + (-0.9013344575593397 + m.x8)**2 + (-0.9953811176046844 + m.x9)**2) +
    m.x282 * ((-0.37780737996640323 + m.x7)**2 + (-0.8839873246439367 + m.x8)**
    2 + (-0.4632132536984095 + m.x9)**2) + m.x283 * ((-0.4156450632457209 +
    m.x7)**2 + (-0.5431767983808783 + m.x8)**2 + (-0.8023913074476225 + m.x9)**
    2) + m.x284 * ((-0.15352263703085378 + m.x7)**2 + (-0.10973315963577568 +
    m.x8)**2 + (-0.6454564663352736 + m.x9)**2) + m.x285 * ((
    -0.9145284924960414 + m.x7)**2 + (-0.9227933160830081 + m.x8)**2 + (
    -0.6810127986564416 + m.x9)**2) + m.x286 * ((-0.10615315400359326 + m.x7)**
    2 + (-0.5475134158722265 + m.x8)**2 + (-0.1648548505370927 + m.x9)**2) +
    m.x287 * ((-0.026255737640514587 + m.x7)**2 + (-0.5596725842620359 + m.x8)
    **2 + (-0.2866191584187715 + m.x9)**2) + m.x288 * ((-0.336345726418656 +
    m.x7)**2 + (-0.17634404223572997 + m.x8)**2 + (-0.6202789464201214 + m.x9)
    **2) + m.x289 * ((-0.3046590255465387 + m.x7)**2 + (-0.4429200521217548 +
    m.x8)**2 + (-0.20698763213399418 + m.x9)**2) + m.x290 * ((
    -0.1874619228105564 + m.x7)**2 + (-0.4998350114658221 + m.x8)**2 + (
    -0.7615173896019674 + m.x9)**2) + m.x291 * ((-0.9066861882230548 + m.x7)**2
    + (-0.7195603347677635 + m.x8)**2 + (-0.06522609137561508 + m.x9)**2) +
    m.x292 * ((-0.7911200820552159 + m.x7)**2 + (-0.7315905893669585 + m.x8)**2
    + (-0.6317765913446202 + m.x9)**2) + m.x293 * ((-0.31382737215555745 +
    m.x7)**2 + (-0.7715540347231861 + m.x8)**2 + (-0.47573360893638406 + m.x9)
    **2) + m.x294 * ((-0.5397580555083911 + m.x7)**2 + (-0.0663564438985641 +
    m.x8)**2 + (-0.8579557631163671 + m.x9)**2) + m.x295 * ((
    -0.14885341468069002 + m.x7)**2 + (-0.3011673371506899 + m.x8)**2 + (
    -0.8781667094774749 + m.x9)**2) + m.x296 * ((-0.9135956838011015 + m.x7)**2
    + (-0.8672955274928783 + m.x8)**2 + (-0.8369181521121158 + m.x9)**2) +
    m.x297 * ((-0.970025910323361 + m.x7)**2 + (-0.051039365966057626 + m.x8)**
    2 + (-0.33776762446434627 + m.x9)**2) + m.x298 * ((-0.15627515420259408 +
    m.x7)**2 + (-0.04035561224618667 + m.x8)**2 + (-0.9808630027608929 + m.x9)
    **2) + m.x299 * ((-0.5997238405427903 + m.x7)**2 + (-0.6340595771156888 +
    m.x8)**2 + (-0.03244563724419325 + m.x9)**2) + m.x300 * ((
    -0.48170623571049465 + m.x7)**2 + (-0.36217785579647566 + m.x8)**2 + (
    -0.9890880708785992 + m.x9)**2) + m.x301 * ((-0.41432137103971445 + m.x7)**
    2 + (-0.19729280755091372 + m.x8)**2 + (-0.6779738469638877 + m.x9)**2) +
    m.x302 * ((-0.44474166469461696 + m.x7)**2 + (-0.2643829797481405 + m.x8)**
    2 + (-0.6562475297685736 + m.x9)**2) + m.x303 * ((-0.6275499840460776 +
    m.x7)**2 + (-0.6100027667466603 + m.x8)**2 + (-0.7498874717615438 + m.x9)**
    2) + m.x304 * ((-0.7377870812034109 + m.x7)**2 + (-0.8635522742958053 +
    m.x8)**2 + (-0.8191133594808159 + m.x9)**2) + m.x305 * ((
    -0.07163384061097833 + m.x7)**2 + (-0.02997713929225343 + m.x8)**2 + (
    -0.27725110161661115 + m.x9)**2) + m.x306 * ((-0.5441338528113598 + m.x7)**
    2 + (-0.0030790728595536665 + m.x8)**2 + (-0.04235938308887821 + m.x9)**2)
    + m.x307 * ((-0.2235362539846405 + m.x7)**2 + (-0.942738774197919 + m.x8)
    **2 + (-0.727537913915035 + m.x9)**2) + m.x308 * ((-0.530616616437767 +
    m.x7)**2 + (-0.07076562154177557 + m.x8)**2 + (-0.5662780949982541 + m.x9)
    **2) + m.x309 * ((-0.985894167192254 + m.x7)**2 + (-0.10185959622013296 +
    m.x8)**2 + (-0.5697892250475037 + m.x9)**2) + m.x310 * ((
    -0.1384396368632138 + m.x7)**2 + (-0.784842787064432 + m.x8)**2 + (
    -0.2014860384245054 + m.x9)**2) + m.x311 * ((-0.025313323494474682 + m.x7)
    **2 + (-0.25046029857714547 + m.x8)**2 + (-0.61170855488363 + m.x9)**2) +
    m.x312 * ((-0.16543698841012866 + m.x7)**2 + (-0.6004755305634034 + m.x8)**
    2 + (-0.8627316624555801 + m.x9)**2) + m.x313 * ((-0.13387794947057807 +
    m.x10)**2 + (-0.42690367626117476 + m.x11)**2 + (-0.8521089176944486 +
    m.x12)**2) + m.x314 * ((-0.45141195547240787 + m.x10)**2 + (
    -0.23276575500936336 + m.x11)**2 + (-0.6685549968499559 + m.x12)**2) +
    m.x315 * ((-0.30597774121727117 + m.x10)**2 + (-0.5840851347084063 + m.x11)
    **2 + (-0.23012065877141608 + m.x12)**2) + m.x316 * ((-0.7558902791058655
    + m.x10)**2 + (-0.05068872162955207 + m.x11)**2 + (-0.2892456744905897 +
    m.x12)**2) + m.x317 * ((-0.9295624768475662 + m.x10)**2 + (
    -0.08669869080122583 + m.x11)**2 + (-0.39032407209267084 + m.x12)**2) +
    m.x318 * ((-0.1863721754637978 + m.x10)**2 + (-0.38136078758188585 + m.x11)
    **2 + (-0.5651584668070776 + m.x12)**2) + m.x319 * ((-0.9543949857543553 +
    m.x10)**2 + (-0.9477493256969005 + m.x11)**2 + (-0.3092150209147405 + m.x12)
    **2) + m.x320 * ((-0.7646939426560075 + m.x10)**2 + (-0.45895458252245525
    + m.x11)**2 + (-0.10132366541532778 + m.x12)**2) + m.x321 * ((
    -0.26830114127671023 + m.x10)**2 + (-0.3175192066975744 + m.x11)**2 + (
    -0.3971628150686213 + m.x12)**2) + m.x322 * ((-0.9976402405070389 + m.x10)
    **2 + (-0.8007630756489261 + m.x11)**2 + (-0.0955548312751 + m.x12)**2) +
    m.x323 * ((-0.5798696146044355 + m.x10)**2 + (-0.29183525723503223 + m.x11)
    **2 + (-0.2600774464034179 + m.x12)**2) + m.x324 * ((-0.8733014194727232 +
    m.x10)**2 + (-0.0675353393368775 + m.x11)**2 + (-0.7346449916245452 + m.x12)
    **2) + m.x325 * ((-0.8879347151978697 + m.x10)**2 + (-0.0021441037308813637
    + m.x11)**2 + (-0.29381156314304335 + m.x12)**2) + m.x326 * ((
    -0.7899560554306205 + m.x10)**2 + (-0.0470096870959813 + m.x11)**2 + (
    -0.36444750704939977 + m.x12)**2) + m.x327 * ((-0.2351423218255354 + m.x10)
    **2 + (-0.8860741867255272 + m.x11)**2 + (-0.8105571816203839 + m.x12)**2)
    + m.x328 * ((-0.7645699915307779 + m.x10)**2 + (-0.2760450725864 + m.x11)
    **2 + (-0.112450897270851 + m.x12)**2) + m.x329 * ((-0.9042505623462239 +
    m.x10)**2 + (-0.22535684423096647 + m.x11)**2 + (-0.21601015353281194 +
    m.x12)**2) + m.x330 * ((-0.08142911761899607 + m.x10)**2 + (
    -0.8238662250465241 + m.x11)**2 + (-0.446656737627519 + m.x12)**2) + m.x331
    * ((-0.17654844392892022 + m.x10)**2 + (-0.021661992025399646 + m.x11)**2
    + (-0.458266931812237 + m.x12)**2) + m.x332 * ((-0.04161872249986398 +
    m.x10)**2 + (-0.0023468770072303524 + m.x11)**2 + (-0.4757688536944913 +
    m.x12)**2) + m.x333 * ((-0.5636261500141898 + m.x10)**2 + (
    -0.5412243430430387 + m.x11)**2 + (-0.9185262483505648 + m.x12)**2) +
    m.x334 * ((-0.04435102264542612 + m.x10)**2 + (-0.0664744839067668 + m.x11)
    **2 + (-0.09363032822552941 + m.x12)**2) + m.x335 * ((-0.6135920539700436
    + m.x10)**2 + (-0.6579236134549653 + m.x11)**2 + (-0.22712348289109685 +
    m.x12)**2) + m.x336 * ((-0.5743364963980989 + m.x10)**2 + (
    -0.05458134438985984 + m.x11)**2 + (-0.12848471239608783 + m.x12)**2) +
    m.x337 * ((-0.27515857398419474 + m.x10)**2 + (-0.13553939615470956 + m.x11)
    **2 + (-0.2684559472460377 + m.x12)**2) + m.x338 * ((-0.2963470374342595 +
    m.x10)**2 + (-0.4095584319942964 + m.x11)**2 + (-0.8587587782336636 + m.x12)
    **2) + m.x339 * ((-0.7570885365520854 + m.x10)**2 + (-0.8084347935423373 +
    m.x11)**2 + (-0.15715607299634216 + m.x12)**2) + m.x340 * ((
    -0.7938896644580142 + m.x10)**2 + (-0.3799882464987978 + m.x11)**2 + (
    -0.9093771971095738 + m.x12)**2) + m.x341 * ((-0.6186079969859057 + m.x10)
    **2 + (-0.681062414997789 + m.x11)**2 + (-0.5860106249361481 + m.x12)**2)
    + m.x342 * ((-0.02194259412307442 + m.x10)**2 + (-0.29702774354519546 +
    m.x11)**2 + (-0.175829273138026 + m.x12)**2) + m.x343 * ((
    -0.26447905881026157 + m.x10)**2 + (-0.7593566218800504 + m.x11)**2 + (
    -0.39760960835759773 + m.x12)**2) + m.x344 * ((-0.13515510461378977 + m.x10)
    **2 + (-0.7972471604464993 + m.x11)**2 + (-0.28558211151639634 + m.x12)**2)
    + m.x345 * ((-0.10772008929383248 + m.x10)**2 + (-0.3773106522010563 +
    m.x11)**2 + (-0.35383902467655304 + m.x12)**2) + m.x346 * ((
    -0.5414010097257086 + m.x10)**2 + (-0.6549307552517842 + m.x11)**2 + (
    -0.7837403296992593 + m.x12)**2) + m.x347 * ((-0.5871205288256559 + m.x10)
    **2 + (-0.4756887184289059 + m.x11)**2 + (-0.30355558496980317 + m.x12)**2)
    + m.x348 * ((-0.6709600289238528 + m.x10)**2 + (-0.7252859209840705 +
    m.x11)**2 + (-0.8981223672754907 + m.x12)**2) + m.x349 * ((
    -0.656856404570921 + m.x10)**2 + (-0.8715951155421182 + m.x11)**2 + (
    -0.02388898086555402 + m.x12)**2) + m.x350 * ((-0.3192345609602486 + m.x10)
    **2 + (-0.31488479193964825 + m.x11)**2 + (-0.6614613888474193 + m.x12)**2)
    + m.x351 * ((-0.8417019897428525 + m.x10)**2 + (-0.616228537066301 + m.x11)
    **2 + (-0.26274228070501626 + m.x12)**2) + m.x352 * ((-0.5937030725992497
    + m.x10)**2 + (-0.19842794521568063 + m.x11)**2 + (-0.5345101523423981 +
    m.x12)**2) + m.x353 * ((-0.03339359470546732 + m.x10)**2 + (
    -0.8108524191133987 + m.x11)**2 + (-0.9601346984817665 + m.x12)**2) +
    m.x354 * ((-0.19103752285334574 + m.x10)**2 + (-0.6614849523412465 + m.x11)
    **2 + (-0.05950865757889012 + m.x12)**2) + m.x355 * ((-0.10783825889829635
    + m.x10)**2 + (-0.5990086159395481 + m.x11)**2 + (-0.06584564659599657 +
    m.x12)**2) + m.x356 * ((-0.41280452109378574 + m.x10)**2 + (
    -0.45708251074315276 + m.x11)**2 + (-0.788130361791057 + m.x12)**2) +
    m.x357 * ((-0.9077561322759368 + m.x10)**2 + (-0.4688875536818434 + m.x11)
    **2 + (-0.033133508346345764 + m.x12)**2) + m.x358 * ((-0.3273136285473489
    + m.x10)**2 + (-0.15390437722631856 + m.x11)**2 + (-0.5114603037727307 +
    m.x12)**2) + m.x359 * ((-0.32464063107132457 + m.x10)**2 + (
    -0.318610062289566 + m.x11)**2 + (-0.5123014054919054 + m.x12)**2) + m.x360
    * ((-0.39959901922907715 + m.x10)**2 + (-0.10577012066519309 + m.x11)**2
    + (-0.8726622650936464 + m.x12)**2) + m.x361 * ((-0.35635136524528255 +
    m.x10)**2 + (-0.1784345686896175 + m.x11)**2 + (-0.42289696970042434 +
    m.x12)**2) + m.x362 * ((-0.782747925998671 + m.x10)**2 + (
    -0.34740318908265166 + m.x11)**2 + (-0.05029454996396343 + m.x12)**2) +
    m.x363 * ((-0.6181863895365817 + m.x10)**2 + (-0.8036374719444359 + m.x11)
    **2 + (-0.6267008774134815 + m.x12)**2) + m.x364 * ((-0.43827940620543104
    + m.x10)**2 + (-0.2137204019393636 + m.x11)**2 + (-0.06448972709664114 +
    m.x12)**2) + m.x365 * ((-0.6225649008635937 + m.x10)**2 + (
    -0.1486871314984446 + m.x11)**2 + (-0.9412847777465005 + m.x12)**2) +
    m.x366 * ((-0.35378600592620435 + m.x10)**2 + (-0.5094259314535285 + m.x11)
    **2 + (-0.15017963251455024 + m.x12)**2) + m.x367 * ((-0.547736164631361 +
    m.x10)**2 + (-0.48529334266922364 + m.x11)**2 + (-0.7587795640672863 +
    m.x12)**2) + m.x368 * ((-0.975084772405915 + m.x10)**2 + (
    -0.13939912017193878 + m.x11)**2 + (-0.8727337834248664 + m.x12)**2) +
    m.x369 * ((-0.22427676001904484 + m.x10)**2 + (-0.5063957190827062 + m.x11)
    **2 + (-0.8854241674425338 + m.x12)**2) + m.x370 * ((-0.3810832957260354 +
    m.x10)**2 + (-0.34581416755281436 + m.x11)**2 + (-0.4406420710521176 +
    m.x12)**2) + m.x371 * ((-0.3499756386974382 + m.x10)**2 + (
    -0.3566588105401399 + m.x11)**2 + (-0.44732858159739897 + m.x12)**2) +
    m.x372 * ((-0.5924763772089162 + m.x10)**2 + (-0.6286013706430164 + m.x11)
    **2 + (-0.09398685721518818 + m.x12)**2) + m.x373 * ((-0.1689853036818748
    + m.x10)**2 + (-0.30514010727298835 + m.x11)**2 + (-0.33603142248790296 +
    m.x12)**2) + m.x374 * ((-0.42582040151330736 + m.x10)**2 + (
    -0.5474773915330942 + m.x11)**2 + (-0.9968031768737334 + m.x12)**2) +
    m.x375 * ((-0.8310835234714565 + m.x10)**2 + (-0.900242213872515 + m.x11)**
    2 + (-0.33176437156580707 + m.x12)**2) + m.x376 * ((-0.37583737986341104 +
    m.x10)**2 + (-0.7466408422154486 + m.x11)**2 + (-0.07941747226014839 +
    m.x12)**2) + m.x377 * ((-0.9322489792585174 + m.x10)**2 + (
    -0.5627545887233887 + m.x11)**2 + (-0.34051255992551555 + m.x12)**2) +
    m.x378 * ((-0.8322172992726823 + m.x10)**2 + (-0.7916032068893061 + m.x11)
    **2 + (-0.6267324024166224 + m.x12)**2) + m.x379 * ((-0.8270530442833851 +
    m.x10)**2 + (-0.3943946960481908 + m.x11)**2 + (-0.19553764761383285 +
    m.x12)**2) + m.x380 * ((-0.18052910743135464 + m.x10)**2 + (
    -0.9897273639149909 + m.x11)**2 + (-0.3977740348052199 + m.x12)**2) +
    m.x381 * ((-0.992075644189053 + m.x10)**2 + (-0.9013344575593397 + m.x11)**
    2 + (-0.9953811176046844 + m.x12)**2) + m.x382 * ((-0.37780737996640323 +
    m.x10)**2 + (-0.8839873246439367 + m.x11)**2 + (-0.4632132536984095 + m.x12)
    **2) + m.x383 * ((-0.4156450632457209 + m.x10)**2 + (-0.5431767983808783 +
    m.x11)**2 + (-0.8023913074476225 + m.x12)**2) + m.x384 * ((
    -0.15352263703085378 + m.x10)**2 + (-0.10973315963577568 + m.x11)**2 + (
    -0.6454564663352736 + m.x12)**2) + m.x385 * ((-0.9145284924960414 + m.x10)
    **2 + (-0.9227933160830081 + m.x11)**2 + (-0.6810127986564416 + m.x12)**2)
    + m.x386 * ((-0.10615315400359326 + m.x10)**2 + (-0.5475134158722265 +
    m.x11)**2 + (-0.1648548505370927 + m.x12)**2) + m.x387 * ((
    -0.026255737640514587 + m.x10)**2 + (-0.5596725842620359 + m.x11)**2 + (
    -0.2866191584187715 + m.x12)**2) + m.x388 * ((-0.336345726418656 + m.x10)**
    2 + (-0.17634404223572997 + m.x11)**2 + (-0.6202789464201214 + m.x12)**2)
    + m.x389 * ((-0.3046590255465387 + m.x10)**2 + (-0.4429200521217548 +
    m.x11)**2 + (-0.20698763213399418 + m.x12)**2) + m.x390 * ((
    -0.1874619228105564 + m.x10)**2 + (-0.4998350114658221 + m.x11)**2 + (
    -0.7615173896019674 + m.x12)**2) + m.x391 * ((-0.9066861882230548 + m.x10)
    **2 + (-0.7195603347677635 + m.x11)**2 + (-0.06522609137561508 + m.x12)**2)
    + m.x392 * ((-0.7911200820552159 + m.x10)**2 + (-0.7315905893669585 +
    m.x11)**2 + (-0.6317765913446202 + m.x12)**2) + m.x393 * ((
    -0.31382737215555745 + m.x10)**2 + (-0.7715540347231861 + m.x11)**2 + (
    -0.47573360893638406 + m.x12)**2) + m.x394 * ((-0.5397580555083911 + m.x10)
    **2 + (-0.0663564438985641 + m.x11)**2 + (-0.8579557631163671 + m.x12)**2)
    + m.x395 * ((-0.14885341468069002 + m.x10)**2 + (-0.3011673371506899 +
    m.x11)**2 + (-0.8781667094774749 + m.x12)**2) + m.x396 * ((
    -0.9135956838011015 + m.x10)**2 + (-0.8672955274928783 + m.x11)**2 + (
    -0.8369181521121158 + m.x12)**2) + m.x397 * ((-0.970025910323361 + m.x10)**
    2 + (-0.051039365966057626 + m.x11)**2 + (-0.33776762446434627 + m.x12)**2)
    + m.x398 * ((-0.15627515420259408 + m.x10)**2 + (-0.04035561224618667 +
    m.x11)**2 + (-0.9808630027608929 + m.x12)**2) + m.x399 * ((
    -0.5997238405427903 + m.x10)**2 + (-0.6340595771156888 + m.x11)**2 + (
    -0.03244563724419325 + m.x12)**2) + m.x400 * ((-0.48170623571049465 + m.x10)
    **2 + (-0.36217785579647566 + m.x11)**2 + (-0.9890880708785992 + m.x12)**2)
    + m.x401 * ((-0.41432137103971445 + m.x10)**2 + (-0.19729280755091372 +
    m.x11)**2 + (-0.6779738469638877 + m.x12)**2) + m.x402 * ((
    -0.44474166469461696 + m.x10)**2 + (-0.2643829797481405 + m.x11)**2 + (
    -0.6562475297685736 + m.x12)**2) + m.x403 * ((-0.6275499840460776 + m.x10)
    **2 + (-0.6100027667466603 + m.x11)**2 + (-0.7498874717615438 + m.x12)**2)
    + m.x404 * ((-0.7377870812034109 + m.x10)**2 + (-0.8635522742958053 +
    m.x11)**2 + (-0.8191133594808159 + m.x12)**2) + m.x405 * ((
    -0.07163384061097833 + m.x10)**2 + (-0.02997713929225343 + m.x11)**2 + (
    -0.27725110161661115 + m.x12)**2) + m.x406 * ((-0.5441338528113598 + m.x10)
    **2 + (-0.0030790728595536665 + m.x11)**2 + (-0.04235938308887821 + m.x12)
    **2) + m.x407 * ((-0.2235362539846405 + m.x10)**2 + (-0.942738774197919 +
    m.x11)**2 + (-0.727537913915035 + m.x12)**2) + m.x408 * ((
    -0.530616616437767 + m.x10)**2 + (-0.07076562154177557 + m.x11)**2 + (
    -0.5662780949982541 + m.x12)**2) + m.x409 * ((-0.985894167192254 + m.x10)**
    2 + (-0.10185959622013296 + m.x11)**2 + (-0.5697892250475037 + m.x12)**2)
    + m.x410 * ((-0.1384396368632138 + m.x10)**2 + (-0.784842787064432 + m.x11)
    **2 + (-0.2014860384245054 + m.x12)**2) + m.x411 * ((-0.025313323494474682
    + m.x10)**2 + (-0.25046029857714547 + m.x11)**2 + (-0.61170855488363 +
    m.x12)**2) + m.x412 * ((-0.16543698841012866 + m.x10)**2 + (
    -0.6004755305634034 + m.x11)**2 + (-0.8627316624555801 + m.x12)**2))

m.e1 = Constraint(expr= m.x13 + m.x113 + m.x213 + m.x313 == 1)
m.e2 = Constraint(expr= m.x14 + m.x114 + m.x214 + m.x314 == 1)
m.e3 = Constraint(expr= m.x15 + m.x115 + m.x215 + m.x315 == 1)
m.e4 = Constraint(expr= m.x16 + m.x116 + m.x216 + m.x316 == 1)
m.e5 = Constraint(expr= m.x17 + m.x117 + m.x217 + m.x317 == 1)
m.e6 = Constraint(expr= m.x18 + m.x118 + m.x218 + m.x318 == 1)
m.e7 = Constraint(expr= m.x19 + m.x119 + m.x219 + m.x319 == 1)
m.e8 = Constraint(expr= m.x20 + m.x120 + m.x220 + m.x320 == 1)
m.e9 = Constraint(expr= m.x21 + m.x121 + m.x221 + m.x321 == 1)
m.e10 = Constraint(expr= m.x22 + m.x122 + m.x222 + m.x322 == 1)
m.e11 = Constraint(expr= m.x23 + m.x123 + m.x223 + m.x323 == 1)
m.e12 = Constraint(expr= m.x24 + m.x124 + m.x224 + m.x324 == 1)
m.e13 = Constraint(expr= m.x25 + m.x125 + m.x225 + m.x325 == 1)
m.e14 = Constraint(expr= m.x26 + m.x126 + m.x226 + m.x326 == 1)
m.e15 = Constraint(expr= m.x27 + m.x127 + m.x227 + m.x327 == 1)
m.e16 = Constraint(expr= m.x28 + m.x128 + m.x228 + m.x328 == 1)
m.e17 = Constraint(expr= m.x29 + m.x129 + m.x229 + m.x329 == 1)
m.e18 = Constraint(expr= m.x30 + m.x130 + m.x230 + m.x330 == 1)
m.e19 = Constraint(expr= m.x31 + m.x131 + m.x231 + m.x331 == 1)
m.e20 = Constraint(expr= m.x32 + m.x132 + m.x232 + m.x332 == 1)
m.e21 = Constraint(expr= m.x33 + m.x133 + m.x233 + m.x333 == 1)
m.e22 = Constraint(expr= m.x34 + m.x134 + m.x234 + m.x334 == 1)
m.e23 = Constraint(expr= m.x35 + m.x135 + m.x235 + m.x335 == 1)
m.e24 = Constraint(expr= m.x36 + m.x136 + m.x236 + m.x336 == 1)
m.e25 = Constraint(expr= m.x37 + m.x137 + m.x237 + m.x337 == 1)
m.e26 = Constraint(expr= m.x38 + m.x138 + m.x238 + m.x338 == 1)
m.e27 = Constraint(expr= m.x39 + m.x139 + m.x239 + m.x339 == 1)
m.e28 = Constraint(expr= m.x40 + m.x140 + m.x240 + m.x340 == 1)
m.e29 = Constraint(expr= m.x41 + m.x141 + m.x241 + m.x341 == 1)
m.e30 = Constraint(expr= m.x42 + m.x142 + m.x242 + m.x342 == 1)
m.e31 = Constraint(expr= m.x43 + m.x143 + m.x243 + m.x343 == 1)
m.e32 = Constraint(expr= m.x44 + m.x144 + m.x244 + m.x344 == 1)
m.e33 = Constraint(expr= m.x45 + m.x145 + m.x245 + m.x345 == 1)
m.e34 = Constraint(expr= m.x46 + m.x146 + m.x246 + m.x346 == 1)
m.e35 = Constraint(expr= m.x47 + m.x147 + m.x247 + m.x347 == 1)
m.e36 = Constraint(expr= m.x48 + m.x148 + m.x248 + m.x348 == 1)
m.e37 = Constraint(expr= m.x49 + m.x149 + m.x249 + m.x349 == 1)
m.e38 = Constraint(expr= m.x50 + m.x150 + m.x250 + m.x350 == 1)
m.e39 = Constraint(expr= m.x51 + m.x151 + m.x251 + m.x351 == 1)
m.e40 = Constraint(expr= m.x52 + m.x152 + m.x252 + m.x352 == 1)
m.e41 = Constraint(expr= m.x53 + m.x153 + m.x253 + m.x353 == 1)
m.e42 = Constraint(expr= m.x54 + m.x154 + m.x254 + m.x354 == 1)
m.e43 = Constraint(expr= m.x55 + m.x155 + m.x255 + m.x355 == 1)
m.e44 = Constraint(expr= m.x56 + m.x156 + m.x256 + m.x356 == 1)
m.e45 = Constraint(expr= m.x57 + m.x157 + m.x257 + m.x357 == 1)
m.e46 = Constraint(expr= m.x58 + m.x158 + m.x258 + m.x358 == 1)
m.e47 = Constraint(expr= m.x59 + m.x159 + m.x259 + m.x359 == 1)
m.e48 = Constraint(expr= m.x60 + m.x160 + m.x260 + m.x360 == 1)
m.e49 = Constraint(expr= m.x61 + m.x161 + m.x261 + m.x361 == 1)
m.e50 = Constraint(expr= m.x62 + m.x162 + m.x262 + m.x362 == 1)
m.e51 = Constraint(expr= m.x63 + m.x163 + m.x263 + m.x363 == 1)
m.e52 = Constraint(expr= m.x64 + m.x164 + m.x264 + m.x364 == 1)
m.e53 = Constraint(expr= m.x65 + m.x165 + m.x265 + m.x365 == 1)
m.e54 = Constraint(expr= m.x66 + m.x166 + m.x266 + m.x366 == 1)
m.e55 = Constraint(expr= m.x67 + m.x167 + m.x267 + m.x367 == 1)
m.e56 = Constraint(expr= m.x68 + m.x168 + m.x268 + m.x368 == 1)
m.e57 = Constraint(expr= m.x69 + m.x169 + m.x269 + m.x369 == 1)
m.e58 = Constraint(expr= m.x70 + m.x170 + m.x270 + m.x370 == 1)
m.e59 = Constraint(expr= m.x71 + m.x171 + m.x271 + m.x371 == 1)
m.e60 = Constraint(expr= m.x72 + m.x172 + m.x272 + m.x372 == 1)
m.e61 = Constraint(expr= m.x73 + m.x173 + m.x273 + m.x373 == 1)
m.e62 = Constraint(expr= m.x74 + m.x174 + m.x274 + m.x374 == 1)
m.e63 = Constraint(expr= m.x75 + m.x175 + m.x275 + m.x375 == 1)
m.e64 = Constraint(expr= m.x76 + m.x176 + m.x276 + m.x376 == 1)
m.e65 = Constraint(expr= m.x77 + m.x177 + m.x277 + m.x377 == 1)
m.e66 = Constraint(expr= m.x78 + m.x178 + m.x278 + m.x378 == 1)
m.e67 = Constraint(expr= m.x79 + m.x179 + m.x279 + m.x379 == 1)
m.e68 = Constraint(expr= m.x80 + m.x180 + m.x280 + m.x380 == 1)
m.e69 = Constraint(expr= m.x81 + m.x181 + m.x281 + m.x381 == 1)
m.e70 = Constraint(expr= m.x82 + m.x182 + m.x282 + m.x382 == 1)
m.e71 = Constraint(expr= m.x83 + m.x183 + m.x283 + m.x383 == 1)
m.e72 = Constraint(expr= m.x84 + m.x184 + m.x284 + m.x384 == 1)
m.e73 = Constraint(expr= m.x85 + m.x185 + m.x285 + m.x385 == 1)
m.e74 = Constraint(expr= m.x86 + m.x186 + m.x286 + m.x386 == 1)
m.e75 = Constraint(expr= m.x87 + m.x187 + m.x287 + m.x387 == 1)
m.e76 = Constraint(expr= m.x88 + m.x188 + m.x288 + m.x388 == 1)
m.e77 = Constraint(expr= m.x89 + m.x189 + m.x289 + m.x389 == 1)
m.e78 = Constraint(expr= m.x90 + m.x190 + m.x290 + m.x390 == 1)
m.e79 = Constraint(expr= m.x91 + m.x191 + m.x291 + m.x391 == 1)
m.e80 = Constraint(expr= m.x92 + m.x192 + m.x292 + m.x392 == 1)
m.e81 = Constraint(expr= m.x93 + m.x193 + m.x293 + m.x393 == 1)
m.e82 = Constraint(expr= m.x94 + m.x194 + m.x294 + m.x394 == 1)
m.e83 = Constraint(expr= m.x95 + m.x195 + m.x295 + m.x395 == 1)
m.e84 = Constraint(expr= m.x96 + m.x196 + m.x296 + m.x396 == 1)
m.e85 = Constraint(expr= m.x97 + m.x197 + m.x297 + m.x397 == 1)
m.e86 = Constraint(expr= m.x98 + m.x198 + m.x298 + m.x398 == 1)
m.e87 = Constraint(expr= m.x99 + m.x199 + m.x299 + m.x399 == 1)
m.e88 = Constraint(expr= m.x100 + m.x200 + m.x300 + m.x400 == 1)
m.e89 = Constraint(expr= m.x101 + m.x201 + m.x301 + m.x401 == 1)
m.e90 = Constraint(expr= m.x102 + m.x202 + m.x302 + m.x402 == 1)
m.e91 = Constraint(expr= m.x103 + m.x203 + m.x303 + m.x403 == 1)
m.e92 = Constraint(expr= m.x104 + m.x204 + m.x304 + m.x404 == 1)
m.e93 = Constraint(expr= m.x105 + m.x205 + m.x305 + m.x405 == 1)
m.e94 = Constraint(expr= m.x106 + m.x206 + m.x306 + m.x406 == 1)
m.e95 = Constraint(expr= m.x107 + m.x207 + m.x307 + m.x407 == 1)
m.e96 = Constraint(expr= m.x108 + m.x208 + m.x308 + m.x408 == 1)
m.e97 = Constraint(expr= m.x109 + m.x209 + m.x309 + m.x409 == 1)
m.e98 = Constraint(expr= m.x110 + m.x210 + m.x310 + m.x410 == 1)
m.e99 = Constraint(expr= m.x111 + m.x211 + m.x311 + m.x411 == 1)
m.e100 = Constraint(expr= m.x112 + m.x212 + m.x312 + m.x412 == 1)
