# NLP written by GAMS Convert at 05/15/24 11:49:59
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       500      500        0        0        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#      1006     1006        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#      1000     1000        0
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
m.x516 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x517 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x518 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x519 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x520 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x521 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x522 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x523 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x524 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x525 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x526 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x527 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x528 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x529 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x530 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x531 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x532 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x533 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x534 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x535 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x536 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x537 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x538 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x539 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x540 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x541 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x542 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x543 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x544 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x545 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x546 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x547 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x548 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x549 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x550 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x551 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x552 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x553 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x554 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x555 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x556 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x557 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x558 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x559 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x560 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x561 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x562 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x563 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x564 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x565 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x566 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x567 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x568 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x569 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x570 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x571 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x572 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x573 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x574 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x575 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x576 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x577 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x578 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x579 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x580 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x581 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x582 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x583 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x584 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x585 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x586 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x587 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x588 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x589 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x590 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x591 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x592 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x593 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x594 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x595 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x596 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x597 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x598 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x599 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x600 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x601 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x602 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x603 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x604 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x605 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x606 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x607 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x608 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x609 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x610 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x611 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x612 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x613 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x614 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x615 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x616 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x617 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x618 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x619 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x620 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x621 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x622 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x623 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x624 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x625 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x626 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x627 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x628 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x629 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x630 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x631 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x632 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x633 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x634 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x635 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x636 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x637 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x638 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x639 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x640 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x641 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x642 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x643 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x644 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x645 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x646 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x647 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x648 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x649 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x650 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x651 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x652 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x653 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x654 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x655 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x656 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x657 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x658 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x659 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x660 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x661 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x662 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x663 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x664 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x665 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x666 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x667 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x668 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x669 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x670 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x671 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x672 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x673 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x674 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x675 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x676 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x677 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x678 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x679 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x680 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x681 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x682 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x683 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x684 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x685 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x686 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x687 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x688 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x689 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x690 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x691 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x692 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x693 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x694 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x695 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x696 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x697 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x698 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x699 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x700 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x701 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x702 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x703 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x704 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x705 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x706 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x707 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x708 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x709 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x710 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x711 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x712 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x713 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x714 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x715 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x716 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x717 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x718 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x719 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x720 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x721 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x722 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x723 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x724 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x725 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x726 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x727 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x728 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x729 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x730 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x731 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x732 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x733 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x734 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x735 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x736 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x737 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x738 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x739 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x740 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x741 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x742 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x743 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x744 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x745 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x746 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x747 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x748 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x749 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x750 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x751 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x752 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x753 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x754 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x755 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x756 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x757 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x758 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x759 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x760 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x761 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x762 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x763 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x764 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x765 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x766 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x767 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x768 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x769 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x770 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x771 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x772 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x773 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x774 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x775 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x776 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x777 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x778 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x779 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x780 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x781 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x782 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x783 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x784 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x785 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x786 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x787 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x788 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x789 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x790 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x791 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x792 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x793 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x794 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x795 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x796 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x797 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x798 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x799 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x800 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x801 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x802 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x803 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x804 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x805 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x806 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x807 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x808 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x809 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x810 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x811 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x812 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x813 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x814 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x815 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x816 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x817 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x818 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x819 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x820 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x821 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x822 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x823 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x824 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x825 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x826 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x827 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x828 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x829 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x830 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x831 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x832 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x833 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x834 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x835 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x836 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x837 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x838 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x839 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x840 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x841 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x842 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x843 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x844 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x845 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x846 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x847 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x848 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x849 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x850 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x851 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x852 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x853 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x854 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x855 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x856 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x857 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x858 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x859 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x860 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x861 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x862 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x863 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x864 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x865 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x866 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x867 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x868 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x869 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x870 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x871 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x872 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x873 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x874 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x875 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x876 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x877 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x878 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x879 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x880 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x881 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x882 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x883 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x884 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x885 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x886 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x887 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x888 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x889 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x890 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x891 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x892 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x893 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x894 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x895 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x896 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x897 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x898 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x899 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x900 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x901 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x902 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x903 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x904 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x905 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x906 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x907 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x908 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x909 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x910 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x911 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x912 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x913 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x914 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x915 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x916 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x917 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x918 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x919 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x920 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x921 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x922 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x923 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x924 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x925 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x926 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x927 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x928 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x929 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x930 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x931 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x932 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x933 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x934 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x935 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x936 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x937 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x938 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x939 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x940 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x941 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x942 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x943 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x944 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x945 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x946 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x947 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x948 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x949 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x950 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x951 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x952 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x953 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x954 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x955 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x956 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x957 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x958 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x959 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x960 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x961 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x962 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x963 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x964 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x965 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x966 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x967 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x968 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x969 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x970 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x971 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x972 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x973 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x974 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x975 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x976 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x977 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x978 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x979 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x980 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x981 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x982 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x983 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x984 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x985 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x986 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x987 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x988 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x989 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x990 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x991 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x992 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x993 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x994 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x995 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x996 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x997 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x998 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x999 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x1000 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x1001 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x1002 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x1003 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x1004 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x1005 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x1006 = Var(within=Reals, bounds=(0,1), initialize=0)

m.obj = Objective(sense=minimize, expr= m.x7 * ((-0.1692498439422696 + m.x1)**2
    + (-0.594909962110926 + m.x2)**2 + (-0.2649627397072344 + m.x3)**2) + m.x8
    * ((-0.4299773164971996 + m.x1)**2 + (-0.8599590238209864 + m.x2)**2 + (
    -0.5477886873552766 + m.x3)**2) + m.x9 * ((-0.5826003170056784 + m.x1)**2
    + (-0.941883448057164 + m.x2)**2 + (-0.30867313678242836 + m.x3)**2) +
    m.x10 * ((-0.6888712108376565 + m.x1)**2 + (-0.46694321374927916 + m.x2)**2
    + (-0.20339940372771748 + m.x3)**2) + m.x11 * ((-0.4405711594738192 + m.x1)
    **2 + (-0.5080910724835329 + m.x2)**2 + (-0.18540147512570138 + m.x3)**2)
    + m.x12 * ((-0.36908840219684824 + m.x1)**2 + (-0.9606901577735717 + m.x2)
    **2 + (-0.1579661214699748 + m.x3)**2) + m.x13 * ((-0.39554390595886324 +
    m.x1)**2 + (-0.95517234425623 + m.x2)**2 + (-0.4357037242101963 + m.x3)**2)
    + m.x14 * ((-0.11324062660745182 + m.x1)**2 + (-0.1127227477493824 + m.x2)
    **2 + (-0.6775531466862447 + m.x3)**2) + m.x15 * ((-0.37207880369117297 +
    m.x1)**2 + (-0.4429785978155648 + m.x2)**2 + (-0.6160286803397987 + m.x3)**
    2) + m.x16 * ((-0.2361959619384585 + m.x1)**2 + (-0.6356037312017463 + m.x2)
    **2 + (-0.5117112742751293 + m.x3)**2) + m.x17 * ((-0.4447865236645254 +
    m.x1)**2 + (-0.33736132166151467 + m.x2)**2 + (-0.5880068862255667 + m.x3)
    **2) + m.x18 * ((-0.1880644612037895 + m.x1)**2 + (-0.8339460457426732 +
    m.x2)**2 + (-0.4642760100333919 + m.x3)**2) + m.x19 * ((-0.809678525848048
    + m.x1)**2 + (-0.9810714270884835 + m.x2)**2 + (-0.22329339192222197 +
    m.x3)**2) + m.x20 * ((-0.9103106601121644 + m.x1)**2 + (-0.7530889196828001
    + m.x2)**2 + (-0.2687229232888456 + m.x3)**2) + m.x21 * ((
    -0.2506681687047203 + m.x1)**2 + (-0.14874655132318948 + m.x2)**2 + (
    -0.7961773337916473 + m.x3)**2) + m.x22 * ((-0.5877634400149608 + m.x1)**2
    + (-0.7175654971518651 + m.x2)**2 + (-0.6356627690183453 + m.x3)**2) +
    m.x23 * ((-0.7974452543446829 + m.x1)**2 + (-0.5323927624309212 + m.x2)**2
    + (-0.9572021040304207 + m.x3)**2) + m.x24 * ((-0.5949737079161318 + m.x1)
    **2 + (-0.41675919028038244 + m.x2)**2 + (-0.25549007713931127 + m.x3)**2)
    + m.x25 * ((-0.05224072110626399 + m.x1)**2 + (-0.9684253307041065 + m.x2)
    **2 + (-0.03621367660020813 + m.x3)**2) + m.x26 * ((-0.9347003609994666 +
    m.x1)**2 + (-0.64358152389621 + m.x2)**2 + (-0.059814343789942215 + m.x3)**
    2) + m.x27 * ((-0.7935538449770041 + m.x1)**2 + (-0.11540895271984875 +
    m.x2)**2 + (-0.3946769068499303 + m.x3)**2) + m.x28 * ((
    -0.17385809015950826 + m.x1)**2 + (-0.45921932138562505 + m.x2)**2 + (
    -0.8256339099174179 + m.x3)**2) + m.x29 * ((-0.03835739793505788 + m.x1)**2
    + (-0.6113872567578748 + m.x2)**2 + (-0.8718964927106821 + m.x3)**2) +
    m.x30 * ((-0.5739391076092649 + m.x1)**2 + (-0.5247196687429146 + m.x2)**2
    + (-0.8533462318828052 + m.x3)**2) + m.x31 * ((-0.971075259349222 + m.x1)
    **2 + (-0.9104965674152667 + m.x2)**2 + (-0.7708929958995743 + m.x3)**2) +
    m.x32 * ((-0.5645353295297807 + m.x1)**2 + (-0.8584342772586054 + m.x2)**2
    + (-0.8718267224700634 + m.x3)**2) + m.x33 * ((-0.6297483558228558 + m.x1)
    **2 + (-0.04014715139597247 + m.x2)**2 + (-0.09844847603361628 + m.x3)**2)
    + m.x34 * ((-0.5189119183247188 + m.x1)**2 + (-0.9474326272844581 + m.x2)
    **2 + (-0.5266109715772231 + m.x3)**2) + m.x35 * ((-0.6527900351730098 +
    m.x1)**2 + (-0.11052190591595967 + m.x2)**2 + (-0.5191880622085426 + m.x3)
    **2) + m.x36 * ((-0.10854173782735999 + m.x1)**2 + (-0.42093142780593973 +
    m.x2)**2 + (-0.31276103054202575 + m.x3)**2) + m.x37 * ((
    -0.3561489249032288 + m.x1)**2 + (-0.8268627589482757 + m.x2)**2 + (
    -0.1956453729075287 + m.x3)**2) + m.x38 * ((-0.4670221520529523 + m.x1)**2
    + (-0.8891113977897892 + m.x2)**2 + (-0.27241504986579945 + m.x3)**2) +
    m.x39 * ((-0.35771749803339015 + m.x1)**2 + (-0.6044481060569854 + m.x2)**2
    + (-0.7643630258273018 + m.x3)**2) + m.x40 * ((-0.04418354837503591 + m.x1)
    **2 + (-0.3102075900230633 + m.x2)**2 + (-0.8330809639446761 + m.x3)**2) +
    m.x41 * ((-0.8743744462324157 + m.x1)**2 + (-0.845910325959314 + m.x2)**2
    + (-0.7140310051973626 + m.x3)**2) + m.x42 * ((-0.716502442685945 + m.x1)
    **2 + (-0.9515475221689099 + m.x2)**2 + (-0.6188065408222541 + m.x3)**2) +
    m.x43 * ((-0.06835345835265683 + m.x1)**2 + (-0.823370938809925 + m.x2)**2
    + (-0.3389455123551257 + m.x3)**2) + m.x44 * ((-0.7757415343504088 + m.x1)
    **2 + (-0.7958264649791436 + m.x2)**2 + (-0.625436707143751 + m.x3)**2) +
    m.x45 * ((-0.9142760468526993 + m.x1)**2 + (-0.970911085347618 + m.x2)**2
    + (-0.5429674014732869 + m.x3)**2) + m.x46 * ((-0.2096014409776199 + m.x1)
    **2 + (-0.9025289375492106 + m.x2)**2 + (-0.5287699855976883 + m.x3)**2) +
    m.x47 * ((-0.011619538885734193 + m.x1)**2 + (-0.12056474702179032 + m.x2)
    **2 + (-0.5981092250808783 + m.x3)**2) + m.x48 * ((-0.08114659947993563 +
    m.x1)**2 + (-0.441063194519585 + m.x2)**2 + (-0.9642109110625849 + m.x3)**2)
    + m.x49 * ((-0.3788010313673167 + m.x1)**2 + (-0.19367862019710247 + m.x2)
    **2 + (-0.7345907587139372 + m.x3)**2) + m.x50 * ((-0.02680831453838972 +
    m.x1)**2 + (-0.5010595635551833 + m.x2)**2 + (-0.5697272305278913 + m.x3)**
    2) + m.x51 * ((-0.9408661364624531 + m.x1)**2 + (-0.4084534281255007 + m.x2)
    **2 + (-0.5124759778704364 + m.x3)**2) + m.x52 * ((-0.7655175499270966 +
    m.x1)**2 + (-0.9482620910201023 + m.x2)**2 + (-0.27827134564381706 + m.x3)
    **2) + m.x53 * ((-0.8265432701686128 + m.x1)**2 + (-0.14848837551074712 +
    m.x2)**2 + (-0.20089309175503667 + m.x3)**2) + m.x54 * ((
    -0.8000481609994606 + m.x1)**2 + (-0.2539853139751347 + m.x2)**2 + (
    -0.20829630707197233 + m.x3)**2) + m.x55 * ((-0.26855105737847407 + m.x1)**
    2 + (-0.44920136283845336 + m.x2)**2 + (-0.41629666515596175 + m.x3)**2) +
    m.x56 * ((-0.7182882087805578 + m.x1)**2 + (-0.3793592905729698 + m.x2)**2
    + (-0.17883837272616077 + m.x3)**2) + m.x57 * ((-0.19581024445686512 +
    m.x1)**2 + (-0.27181382773049567 + m.x2)**2 + (-0.322427225040845 + m.x3)**
    2) + m.x58 * ((-0.38658358127338854 + m.x1)**2 + (-0.7529124327703216 +
    m.x2)**2 + (-0.41910049255232174 + m.x3)**2) + m.x59 * ((
    -0.19143734810557733 + m.x1)**2 + (-0.48208401520816846 + m.x2)**2 + (
    -0.045061252030364485 + m.x3)**2) + m.x60 * ((-0.05682593455420182 + m.x1)
    **2 + (-0.7233915176300436 + m.x2)**2 + (-0.705103104979348 + m.x3)**2) +
    m.x61 * ((-0.9042027840926966 + m.x1)**2 + (-0.6938960112447266 + m.x2)**2
    + (-0.3354994737557092 + m.x3)**2) + m.x62 * ((-0.7894861443951544 + m.x1)
    **2 + (-0.15244186536727333 + m.x2)**2 + (-0.5005398248336654 + m.x3)**2)
    + m.x63 * ((-0.34446185593752554 + m.x1)**2 + (-0.6772836129498278 + m.x2)
    **2 + (-0.7336734830314701 + m.x3)**2) + m.x64 * ((-0.20741666474163767 +
    m.x1)**2 + (-0.8202921977271875 + m.x2)**2 + (-0.5506009695439275 + m.x3)**
    2) + m.x65 * ((-0.5402923097092933 + m.x1)**2 + (-0.2675342734369003 + m.x2)
    **2 + (-0.7992890751698145 + m.x3)**2) + m.x66 * ((-0.27967022339776526 +
    m.x1)**2 + (-0.7979911425034355 + m.x2)**2 + (-0.46452645725265274 + m.x3)
    **2) + m.x67 * ((-0.9595819947527509 + m.x1)**2 + (-0.5232034354155645 +
    m.x2)**2 + (-0.2389966098134152 + m.x3)**2) + m.x68 * ((
    -0.07608991534038712 + m.x1)**2 + (-0.5736418691521828 + m.x2)**2 + (
    -0.019986186505803083 + m.x3)**2) + m.x69 * ((-0.42700398197897205 + m.x1)
    **2 + (-0.8010918625105746 + m.x2)**2 + (-0.8805692849635621 + m.x3)**2) +
    m.x70 * ((-0.5579869928092586 + m.x1)**2 + (-0.389498674450649 + m.x2)**2
    + (-0.0748048271612155 + m.x3)**2) + m.x71 * ((-0.4070102263571985 + m.x1)
    **2 + (-0.7554593095435335 + m.x2)**2 + (-0.5904356558483927 + m.x3)**2) +
    m.x72 * ((-0.1364891447316846 + m.x1)**2 + (-0.8468918307965907 + m.x2)**2
    + (-0.28700620952460276 + m.x3)**2) + m.x73 * ((-0.3367232340241588 + m.x1)
    **2 + (-0.8929968819838374 + m.x2)**2 + (-0.7484026014198896 + m.x3)**2) +
    m.x74 * ((-0.7635235105485991 + m.x1)**2 + (-0.5708091732053739 + m.x2)**2
    + (-0.6753411475376285 + m.x3)**2) + m.x75 * ((-0.3651268993409923 + m.x1)
    **2 + (-0.12289882343337766 + m.x2)**2 + (-0.964009065158759 + m.x3)**2) +
    m.x76 * ((-0.8750166259121633 + m.x1)**2 + (-0.41383609996893045 + m.x2)**2
    + (-0.29800741171032363 + m.x3)**2) + m.x77 * ((-0.40013800173743697 +
    m.x1)**2 + (-0.7249247652248746 + m.x2)**2 + (-0.6355874704603257 + m.x3)**
    2) + m.x78 * ((-0.18348856582977036 + m.x1)**2 + (-0.025854052500041358 +
    m.x2)**2 + (-0.2534534001576054 + m.x3)**2) + m.x79 * ((-0.9435154017754898
    + m.x1)**2 + (-0.4392260710197824 + m.x2)**2 + (-0.4691516281413123 + m.x3)
    **2) + m.x80 * ((-0.7385168925807722 + m.x1)**2 + (-0.24644193646352752 +
    m.x2)**2 + (-0.17061742663080026 + m.x3)**2) + m.x81 * ((
    -0.05605633605668536 + m.x1)**2 + (-0.4912081682781063 + m.x2)**2 + (
    -0.5699993572568407 + m.x3)**2) + m.x82 * ((-0.15757181258844644 + m.x1)**2
    + (-0.7303751725186297 + m.x2)**2 + (-0.9121598657835175 + m.x3)**2) +
    m.x83 * ((-0.33215497925633675 + m.x1)**2 + (-0.17028080871532403 + m.x2)**
    2 + (-0.3930063113045501 + m.x3)**2) + m.x84 * ((-0.7786941002157438 + m.x1)
    **2 + (-0.7405380151215268 + m.x2)**2 + (-0.9154339959764618 + m.x3)**2) +
    m.x85 * ((-0.7508193852295587 + m.x1)**2 + (-0.3803573428649786 + m.x2)**2
    + (-0.22138614519182764 + m.x3)**2) + m.x86 * ((-0.9264682682309922 + m.x1)
    **2 + (-0.8873603073342023 + m.x2)**2 + (-0.864950588785591 + m.x3)**2) +
    m.x87 * ((-0.908267042284869 + m.x1)**2 + (-0.10298312771159246 + m.x2)**2
    + (-0.6124646113776369 + m.x3)**2) + m.x88 * ((-0.16426882492973371 + m.x1)
    **2 + (-0.9869331956455133 + m.x2)**2 + (-0.719818452386762 + m.x3)**2) +
    m.x89 * ((-0.8825086613164931 + m.x1)**2 + (-0.08300173420348822 + m.x2)**2
    + (-0.44087052443558905 + m.x3)**2) + m.x90 * ((-0.5130371082699586 + m.x1)
    **2 + (-0.7805872451248177 + m.x2)**2 + (-0.914693570552897 + m.x3)**2) +
    m.x91 * ((-0.12650358912449233 + m.x1)**2 + (-0.5342711885242658 + m.x2)**2
    + (-0.3859086811884249 + m.x3)**2) + m.x92 * ((-0.021894498188813283 +
    m.x1)**2 + (-0.0027246625913778244 + m.x2)**2 + (-0.626856809181304 + m.x3)
    **2) + m.x93 * ((-0.8441678193498758 + m.x1)**2 + (-0.3509107664369997 +
    m.x2)**2 + (-0.23930665191922518 + m.x3)**2) + m.x94 * ((
    -0.9191544458905686 + m.x1)**2 + (-0.9295699343849126 + m.x2)**2 + (
    -0.5569494475068902 + m.x3)**2) + m.x95 * ((-0.35271055808467555 + m.x1)**2
    + (-0.14001703168123492 + m.x2)**2 + (-0.4307833453831681 + m.x3)**2) +
    m.x96 * ((-0.015927077871251027 + m.x1)**2 + (-0.7944117141411271 + m.x2)**
    2 + (-0.0663323600363589 + m.x3)**2) + m.x97 * ((-0.06700957837304222 +
    m.x1)**2 + (-0.7245424124926254 + m.x2)**2 + (-0.04136030199658791 + m.x3)
    **2) + m.x98 * ((-0.6435908765286936 + m.x1)**2 + (-0.5608885129918921 +
    m.x2)**2 + (-0.29840288844009555 + m.x3)**2) + m.x99 * ((
    -0.0017744407035030774 + m.x1)**2 + (-0.5302888132806858 + m.x2)**2 + (
    -0.1070197893246232 + m.x3)**2) + m.x100 * ((-0.9960876588948411 + m.x1)**2
    + (-0.5297980608672969 + m.x2)**2 + (-0.0967898406969584 + m.x3)**2) +
    m.x101 * ((-0.2966788147123718 + m.x1)**2 + (-0.4535896653892114 + m.x2)**2
    + (-0.12490644679443152 + m.x3)**2) + m.x102 * ((-0.33141143322070366 +
    m.x1)**2 + (-0.28744907554291355 + m.x2)**2 + (-0.06994447154054817 + m.x3)
    **2) + m.x103 * ((-0.047933403792797424 + m.x1)**2 + (-0.8415471101830639
    + m.x2)**2 + (-0.5955840833322725 + m.x3)**2) + m.x104 * ((
    -0.9171613034104257 + m.x1)**2 + (-0.6459943002822387 + m.x2)**2 + (
    -0.4152591826204478 + m.x3)**2) + m.x105 * ((-0.32790075407957764 + m.x1)**
    2 + (-0.4939517226351521 + m.x2)**2 + (-0.22989356871245614 + m.x3)**2) +
    m.x106 * ((-0.5844775505927844 + m.x1)**2 + (-0.7114551136263754 + m.x2)**2
    + (-0.2605304125555207 + m.x3)**2) + m.x107 * ((-0.5855724678597634 + m.x1)
    **2 + (-0.5384124176079916 + m.x2)**2 + (-0.22873430477860057 + m.x3)**2)
    + m.x108 * ((-0.27448502514988804 + m.x1)**2 + (-0.8811058000942367 + m.x2)
    **2 + (-0.1084432011985692 + m.x3)**2) + m.x109 * ((-0.8087191675490594 +
    m.x1)**2 + (-0.36365530737786633 + m.x2)**2 + (-0.2551582076272405 + m.x3)
    **2) + m.x110 * ((-0.4692805537583873 + m.x1)**2 + (-0.1094763815311296 +
    m.x2)**2 + (-0.03308747009705737 + m.x3)**2) + m.x111 * ((
    -0.1414596675245341 + m.x1)**2 + (-0.05264608531324155 + m.x2)**2 + (
    -0.16232407961452555 + m.x3)**2) + m.x112 * ((-0.09502702610585512 + m.x1)
    **2 + (-0.6088439913367978 + m.x2)**2 + (-0.5808332695355897 + m.x3)**2) +
    m.x113 * ((-0.03790513829711473 + m.x1)**2 + (-0.5080181668023536 + m.x2)**
    2 + (-0.6682482244944306 + m.x3)**2) + m.x114 * ((-0.2398098003882162 +
    m.x1)**2 + (-0.40854299334338917 + m.x2)**2 + (-0.6265561387473995 + m.x3)
    **2) + m.x115 * ((-0.41352866202283534 + m.x1)**2 + (-0.13735597150040624
    + m.x2)**2 + (-0.6575650750157317 + m.x3)**2) + m.x116 * ((
    -0.5918024287760949 + m.x1)**2 + (-0.9046254255858704 + m.x2)**2 + (
    -0.35259988628306405 + m.x3)**2) + m.x117 * ((-0.6163737698105297 + m.x1)**
    2 + (-0.7338484828210599 + m.x2)**2 + (-0.2552037957856732 + m.x3)**2) +
    m.x118 * ((-0.7481226352197995 + m.x1)**2 + (-0.6103864936538574 + m.x2)**2
    + (-0.29319537619297076 + m.x3)**2) + m.x119 * ((-0.3817477016118834 +
    m.x1)**2 + (-0.28367233078996257 + m.x2)**2 + (-0.9065136963715262 + m.x3)
    **2) + m.x120 * ((-0.5387913922968426 + m.x1)**2 + (-0.9587122385639283 +
    m.x2)**2 + (-0.2849034277289415 + m.x3)**2) + m.x121 * ((
    -0.016896910716011626 + m.x1)**2 + (-0.542247494752311 + m.x2)**2 + (
    -0.35702504416839875 + m.x3)**2) + m.x122 * ((-0.0400792611431785 + m.x1)**
    2 + (-0.06003526247003277 + m.x2)**2 + (-0.8531074258574137 + m.x3)**2) +
    m.x123 * ((-0.6026500310542549 + m.x1)**2 + (-0.6934852370637312 + m.x2)**2
    + (-0.3460238114357763 + m.x3)**2) + m.x124 * ((-0.55902762581076 + m.x1)
    **2 + (-0.9459788231528541 + m.x2)**2 + (-0.1290887862399902 + m.x3)**2) +
    m.x125 * ((-0.3837617695459321 + m.x1)**2 + (-0.3879093486846117 + m.x2)**2
    + (-0.8849022163547949 + m.x3)**2) + m.x126 * ((-0.7720525818822013 + m.x1)
    **2 + (-0.1111500101946098 + m.x2)**2 + (-0.7661918097646079 + m.x3)**2) +
    m.x127 * ((-0.6344378078488477 + m.x1)**2 + (-0.38920253281074113 + m.x2)**
    2 + (-0.2569532307428819 + m.x3)**2) + m.x128 * ((-0.8429682238542169 +
    m.x1)**2 + (-0.28809038931293773 + m.x2)**2 + (-0.19175063574452433 + m.x3)
    **2) + m.x129 * ((-0.2672995256303895 + m.x1)**2 + (-0.03242383874322041 +
    m.x2)**2 + (-0.9842571124991794 + m.x3)**2) + m.x130 * ((
    -0.06540387850476659 + m.x1)**2 + (-0.24128518865484905 + m.x2)**2 + (
    -0.20517012144871016 + m.x3)**2) + m.x131 * ((-0.18621511189629547 + m.x1)
    **2 + (-0.30267745952007064 + m.x2)**2 + (-0.7114604662427862 + m.x3)**2)
    + m.x132 * ((-0.7893034114918972 + m.x1)**2 + (-0.0955677714501183 + m.x2)
    **2 + (-0.5821952996736662 + m.x3)**2) + m.x133 * ((-0.20739251640515832 +
    m.x1)**2 + (-0.8432910091332453 + m.x2)**2 + (-0.2586107102872377 + m.x3)**
    2) + m.x134 * ((-0.5530346239832239 + m.x1)**2 + (-0.37827958857876165 +
    m.x2)**2 + (-0.7781403692754599 + m.x3)**2) + m.x135 * ((
    -0.28092860002809394 + m.x1)**2 + (-0.8298897623230604 + m.x2)**2 + (
    -0.2719103553554957 + m.x3)**2) + m.x136 * ((-0.014925126786705656 + m.x1)
    **2 + (-0.12777278988662366 + m.x2)**2 + (-0.10588450075658606 + m.x3)**2)
    + m.x137 * ((-0.11668619210388753 + m.x1)**2 + (-0.3820666367049661 + m.x2)
    **2 + (-0.7791195974948653 + m.x3)**2) + m.x138 * ((-0.4344431981739817 +
    m.x1)**2 + (-0.1080485799315768 + m.x2)**2 + (-0.08340127233732786 + m.x3)
    **2) + m.x139 * ((-0.1793620960414819 + m.x1)**2 + (-0.3419484974871717 +
    m.x2)**2 + (-0.7820789010033935 + m.x3)**2) + m.x140 * ((
    -0.7165429642851615 + m.x1)**2 + (-0.9026914605710601 + m.x2)**2 + (
    -0.6935163617983727 + m.x3)**2) + m.x141 * ((-0.30965035870898905 + m.x1)**
    2 + (-0.6763312865753088 + m.x2)**2 + (-0.10472903251267174 + m.x3)**2) +
    m.x142 * ((-0.10216516132313902 + m.x1)**2 + (-0.5490230377748015 + m.x2)**
    2 + (-0.7352888807492108 + m.x3)**2) + m.x143 * ((-0.8651135909998409 +
    m.x1)**2 + (-0.29254598308074753 + m.x2)**2 + (-0.11864176567670415 + m.x3)
    **2) + m.x144 * ((-0.2101013503923751 + m.x1)**2 + (-0.8522411631472961 +
    m.x2)**2 + (-0.7212132885792959 + m.x3)**2) + m.x145 * ((
    -0.11131146834606975 + m.x1)**2 + (-0.09341511900076704 + m.x2)**2 + (
    -0.22436226860606978 + m.x3)**2) + m.x146 * ((-0.09589381898256144 + m.x1)
    **2 + (-0.62983098343096 + m.x2)**2 + (-0.236862989417864 + m.x3)**2) +
    m.x147 * ((-0.17134746819256785 + m.x1)**2 + (-0.0022191294485545132 + m.x2)
    **2 + (-0.5719632904418379 + m.x3)**2) + m.x148 * ((-0.1437717819667449 +
    m.x1)**2 + (-0.693066215236063 + m.x2)**2 + (-0.47910832437053097 + m.x3)**
    2) + m.x149 * ((-0.21326957505198796 + m.x1)**2 + (-0.5389938925764525 +
    m.x2)**2 + (-0.8985814053123515 + m.x3)**2) + m.x150 * ((
    -0.5267034399227511 + m.x1)**2 + (-0.16272083595464992 + m.x2)**2 + (
    -0.4424485927629499 + m.x3)**2) + m.x151 * ((-0.010171844468493396 + m.x1)
    **2 + (-0.8225385611520942 + m.x2)**2 + (-0.850081594460415 + m.x3)**2) +
    m.x152 * ((-0.9099126006489431 + m.x1)**2 + (-0.7117592498159224 + m.x2)**2
    + (-0.24535211640166132 + m.x3)**2) + m.x153 * ((-0.8933095434728399 +
    m.x1)**2 + (-0.18696555428084993 + m.x2)**2 + (-0.14126880443170386 + m.x3)
    **2) + m.x154 * ((-0.05060465423810745 + m.x1)**2 + (-0.35889935243868054
    + m.x2)**2 + (-0.9898462690273427 + m.x3)**2) + m.x155 * ((
    -0.28435588276815815 + m.x1)**2 + (-0.144413444054048 + m.x2)**2 + (
    -0.4912506689862507 + m.x3)**2) + m.x156 * ((-0.02377989350983456 + m.x1)**
    2 + (-0.4850739766720621 + m.x2)**2 + (-0.014220358160159874 + m.x3)**2) +
    m.x157 * ((-0.10685228340662356 + m.x1)**2 + (-0.4306857431033353 + m.x2)**
    2 + (-0.899717945016438 + m.x3)**2) + m.x158 * ((-0.7958123415938076 + m.x1)
    **2 + (-0.1567416212397551 + m.x2)**2 + (-0.4381463784299796 + m.x3)**2) +
    m.x159 * ((-0.20239323873555803 + m.x1)**2 + (-0.6688370928332699 + m.x2)**
    2 + (-0.8908782840570669 + m.x3)**2) + m.x160 * ((-0.8162377020493878 +
    m.x1)**2 + (-0.5538462537896983 + m.x2)**2 + (-0.46332413492756175 + m.x3)
    **2) + m.x161 * ((-0.3285436588025977 + m.x1)**2 + (-0.18234363029763911 +
    m.x2)**2 + (-0.9652199890334622 + m.x3)**2) + m.x162 * ((
    -0.1833756016631104 + m.x1)**2 + (-0.6191845385278278 + m.x2)**2 + (
    -0.3823840339936617 + m.x3)**2) + m.x163 * ((-0.9451306347207963 + m.x1)**2
    + (-0.05696563611612815 + m.x2)**2 + (-0.31872989911510674 + m.x3)**2) +
    m.x164 * ((-0.1876172330243875 + m.x1)**2 + (-0.21273318417844989 + m.x2)**
    2 + (-0.7951342088420695 + m.x3)**2) + m.x165 * ((-0.6813385906412783 +
    m.x1)**2 + (-0.7795130804133624 + m.x2)**2 + (-0.8121251523108964 + m.x3)**
    2) + m.x166 * ((-0.5476385802163356 + m.x1)**2 + (-0.47082012503804105 +
    m.x2)**2 + (-0.1875779928301533 + m.x3)**2) + m.x167 * ((
    -0.4418603491118567 + m.x1)**2 + (-0.47814259051556174 + m.x2)**2 + (
    -0.843868091243698 + m.x3)**2) + m.x168 * ((-0.7227490532707296 + m.x1)**2
    + (-0.6305946284321624 + m.x2)**2 + (-0.7778431141977471 + m.x3)**2) +
    m.x169 * ((-0.44449821578332316 + m.x1)**2 + (-0.7010434784223998 + m.x2)**
    2 + (-0.4562440307525807 + m.x3)**2) + m.x170 * ((-0.8207794357127131 +
    m.x1)**2 + (-0.2715928586111269 + m.x2)**2 + (-0.8111077485955768 + m.x3)**
    2) + m.x171 * ((-0.06913168314217966 + m.x1)**2 + (-0.17062534115061545 +
    m.x2)**2 + (-0.7186204035119522 + m.x3)**2) + m.x172 * ((
    -0.9356572299847938 + m.x1)**2 + (-0.25247506111569284 + m.x2)**2 + (
    -0.3766500744907605 + m.x3)**2) + m.x173 * ((-0.053183850751484685 + m.x1)
    **2 + (-0.503319761819413 + m.x2)**2 + (-0.3988792529665396 + m.x3)**2) +
    m.x174 * ((-0.6348345247106641 + m.x1)**2 + (-0.7372264972225206 + m.x2)**2
    + (-0.2816805911685105 + m.x3)**2) + m.x175 * ((-0.4922332187206825 + m.x1)
    **2 + (-0.12955383972526402 + m.x2)**2 + (-0.6759110290426272 + m.x3)**2)
    + m.x176 * ((-0.3039899015675839 + m.x1)**2 + (-0.8701136133070226 + m.x2)
    **2 + (-0.3415605267108113 + m.x3)**2) + m.x177 * ((-0.19249833111625447 +
    m.x1)**2 + (-0.289199436536963 + m.x2)**2 + (-0.17001661008163982 + m.x3)**
    2) + m.x178 * ((-0.41498929870378265 + m.x1)**2 + (-0.6714872892529845 +
    m.x2)**2 + (-0.7734373760087199 + m.x3)**2) + m.x179 * ((
    -0.6414826763544017 + m.x1)**2 + (-0.833907205124963 + m.x2)**2 + (
    -0.5454186218286011 + m.x3)**2) + m.x180 * ((-0.8018985643443416 + m.x1)**2
    + (-0.18267498327347076 + m.x2)**2 + (-0.6248398639397298 + m.x3)**2) +
    m.x181 * ((-0.011710686297021211 + m.x1)**2 + (-0.7293978925979899 + m.x2)
    **2 + (-0.062110132255305706 + m.x3)**2) + m.x182 * ((-0.3522173993348232
    + m.x1)**2 + (-0.07284835414901125 + m.x2)**2 + (-0.6849529919886285 +
    m.x3)**2) + m.x183 * ((-0.12185440522884461 + m.x1)**2 + (
    -0.6687199057889921 + m.x2)**2 + (-0.13946873559425443 + m.x3)**2) + m.x184
    * ((-0.8925626716041768 + m.x1)**2 + (-0.5507535962948702 + m.x2)**2 + (
    -0.7754292445803886 + m.x3)**2) + m.x185 * ((-0.6737722608457104 + m.x1)**2
    + (-0.6835956974473757 + m.x2)**2 + (-0.11220963763590197 + m.x3)**2) +
    m.x186 * ((-0.2056780683513766 + m.x1)**2 + (-0.7777969577351744 + m.x2)**2
    + (-0.7818523629215165 + m.x3)**2) + m.x187 * ((-0.35040653667397936 +
    m.x1)**2 + (-0.7218237888483313 + m.x2)**2 + (-0.24223482432840604 + m.x3)
    **2) + m.x188 * ((-0.045519582549019444 + m.x1)**2 + (-0.2468399938697886
    + m.x2)**2 + (-0.5509847497355672 + m.x3)**2) + m.x189 * ((
    -0.7625095428789862 + m.x1)**2 + (-0.38693097091538686 + m.x2)**2 + (
    -0.8447744154325253 + m.x3)**2) + m.x190 * ((-0.47706955962867537 + m.x1)**
    2 + (-0.9048825326627299 + m.x2)**2 + (-0.6698420394228831 + m.x3)**2) +
    m.x191 * ((-0.9220722254195256 + m.x1)**2 + (-0.9093919260950618 + m.x2)**2
    + (-0.3585536965409931 + m.x3)**2) + m.x192 * ((-0.42421741345016817 +
    m.x1)**2 + (-0.1810097690077137 + m.x2)**2 + (-0.11838106532964576 + m.x3)
    **2) + m.x193 * ((-0.7909025678257156 + m.x1)**2 + (-0.6683526078945575 +
    m.x2)**2 + (-0.5109886309751906 + m.x3)**2) + m.x194 * ((
    -0.28703506025246406 + m.x1)**2 + (-0.6439491320749008 + m.x2)**2 + (
    -0.7706022456077256 + m.x3)**2) + m.x195 * ((-0.13459246208619924 + m.x1)**
    2 + (-0.28097209258600253 + m.x2)**2 + (-0.10489080047801336 + m.x3)**2) +
    m.x196 * ((-0.3523855983171982 + m.x1)**2 + (-0.4248157381430815 + m.x2)**2
    + (-0.6906133929926649 + m.x3)**2) + m.x197 * ((-0.1583698558934198 + m.x1)
    **2 + (-0.9210909019600683 + m.x2)**2 + (-0.6395026018640236 + m.x3)**2) +
    m.x198 * ((-0.7869061505221948 + m.x1)**2 + (-0.7078900011730935 + m.x2)**2
    + (-0.6196010572637488 + m.x3)**2) + m.x199 * ((-0.5687640083646678 + m.x1)
    **2 + (-0.5772192111740503 + m.x2)**2 + (-0.6138822482643156 + m.x3)**2) +
    m.x200 * ((-0.7139842499777261 + m.x1)**2 + (-0.11680023910927528 + m.x2)**
    2 + (-0.2506224434653087 + m.x3)**2) + m.x201 * ((-0.805568392008547 + m.x1)
    **2 + (-0.06545005124609204 + m.x2)**2 + (-0.032700612578027144 + m.x3)**2)
    + m.x202 * ((-0.8672418514729174 + m.x1)**2 + (-0.9495334316535684 + m.x2)
    **2 + (-0.9506671434655545 + m.x3)**2) + m.x203 * ((-0.8428186951044521 +
    m.x1)**2 + (-0.2491784563178132 + m.x2)**2 + (-0.8574700961978342 + m.x3)**
    2) + m.x204 * ((-0.3871201049109313 + m.x1)**2 + (-0.9738876810785931 +
    m.x2)**2 + (-0.613114261845513 + m.x3)**2) + m.x205 * ((-0.9150831066517291
    + m.x1)**2 + (-0.8126407462368724 + m.x2)**2 + (-0.32527791429850705 +
    m.x3)**2) + m.x206 * ((-0.13884237948432931 + m.x1)**2 + (
    -0.05350519336412973 + m.x2)**2 + (-0.24780684370452688 + m.x3)**2) +
    m.x207 * ((-0.7923572326382577 + m.x1)**2 + (-0.16987369545737896 + m.x2)**
    2 + (-0.9459861441672113 + m.x3)**2) + m.x208 * ((-0.8287350086957515 +
    m.x1)**2 + (-0.2701283953407778 + m.x2)**2 + (-0.38893185458031276 + m.x3)
    **2) + m.x209 * ((-0.8419989467911838 + m.x1)**2 + (-0.36305399780969094 +
    m.x2)**2 + (-0.5097745885449746 + m.x3)**2) + m.x210 * ((
    -0.9328252563464429 + m.x1)**2 + (-0.6938288661186377 + m.x2)**2 + (
    -0.5178576561761775 + m.x3)**2) + m.x211 * ((-0.13394390692618663 + m.x1)**
    2 + (-0.1707402476262171 + m.x2)**2 + (-0.049978421880908175 + m.x3)**2) +
    m.x212 * ((-0.9344145063124553 + m.x1)**2 + (-0.5642986722348461 + m.x2)**2
    + (-0.9742283497162917 + m.x3)**2) + m.x213 * ((-0.12917904997198593 +
    m.x1)**2 + (-0.8291714054039813 + m.x2)**2 + (-0.1461208778099089 + m.x3)**
    2) + m.x214 * ((-0.49297041535442676 + m.x1)**2 + (-0.9997056001066135 +
    m.x2)**2 + (-0.9984805276449421 + m.x3)**2) + m.x215 * ((
    -0.9443406401848632 + m.x1)**2 + (-0.9556643724533576 + m.x2)**2 + (
    -0.7626439658137829 + m.x3)**2) + m.x216 * ((-0.4927277418379675 + m.x1)**2
    + (-0.24978712865953823 + m.x2)**2 + (-0.33279356513981784 + m.x3)**2) +
    m.x217 * ((-0.6628894265876931 + m.x1)**2 + (-0.08815384447750985 + m.x2)**
    2 + (-0.02837052028209286 + m.x3)**2) + m.x218 * ((-0.5951215974793173 +
    m.x1)**2 + (-0.6709917301275213 + m.x2)**2 + (-0.5228016909019687 + m.x3)**
    2) + m.x219 * ((-0.3628434072386518 + m.x1)**2 + (-0.5648955285747782 +
    m.x2)**2 + (-0.14037475292742752 + m.x3)**2) + m.x220 * ((
    -0.6315358621764737 + m.x1)**2 + (-0.4940040944835772 + m.x2)**2 + (
    -0.39393981108383724 + m.x3)**2) + m.x221 * ((-0.23895764723651125 + m.x1)
    **2 + (-0.4925466699958012 + m.x2)**2 + (-0.6798787131541073 + m.x3)**2) +
    m.x222 * ((-0.33431465619738565 + m.x1)**2 + (-0.02990879062461249 + m.x2)
    **2 + (-0.98627846080786 + m.x3)**2) + m.x223 * ((-0.20138845604638655 +
    m.x1)**2 + (-0.07286113290687579 + m.x2)**2 + (-0.7389461293858135 + m.x3)
    **2) + m.x224 * ((-0.22043310505100588 + m.x1)**2 + (-0.6921624888940164 +
    m.x2)**2 + (-0.7390910692714129 + m.x3)**2) + m.x225 * ((
    -0.1794768509914445 + m.x1)**2 + (-0.19971018619617786 + m.x2)**2 + (
    -0.1252179745377201 + m.x3)**2) + m.x226 * ((-0.4316525971751499 + m.x1)**2
    + (-0.9293948927573288 + m.x2)**2 + (-0.6357217625876419 + m.x3)**2) +
    m.x227 * ((-0.19054858574619327 + m.x1)**2 + (-0.6597186703227657 + m.x2)**
    2 + (-0.7437070343450088 + m.x3)**2) + m.x228 * ((-0.5401665990210613 +
    m.x1)**2 + (-0.31975882224981744 + m.x2)**2 + (-0.7676783575559698 + m.x3)
    **2) + m.x229 * ((-0.7141585569819535 + m.x1)**2 + (-0.5821205832955013 +
    m.x2)**2 + (-0.9414136448749184 + m.x3)**2) + m.x230 * ((
    -0.44737341471901404 + m.x1)**2 + (-0.9048222764719899 + m.x2)**2 + (
    -0.7461921038282987 + m.x3)**2) + m.x231 * ((-0.6074944823231694 + m.x1)**2
    + (-0.4144292990749079 + m.x2)**2 + (-0.9448146796490002 + m.x3)**2) +
    m.x232 * ((-0.7711535942806756 + m.x1)**2 + (-0.18386931660223416 + m.x2)**
    2 + (-0.9382198399195494 + m.x3)**2) + m.x233 * ((-0.6654811389399782 +
    m.x1)**2 + (-0.7664480958655735 + m.x2)**2 + (-0.8043855734520027 + m.x3)**
    2) + m.x234 * ((-0.13574356640083862 + m.x1)**2 + (-0.8006073394818852 +
    m.x2)**2 + (-0.4293460234558568 + m.x3)**2) + m.x235 * ((-0.88109422081292
    + m.x1)**2 + (-0.2521523305664952 + m.x2)**2 + (-0.2783612988957984 + m.x3)
    **2) + m.x236 * ((-0.21098683574670196 + m.x1)**2 + (-0.5793487573072326 +
    m.x2)**2 + (-0.1400427387047346 + m.x3)**2) + m.x237 * ((
    -0.5287988551538474 + m.x1)**2 + (-0.9641191628237653 + m.x2)**2 + (
    -0.9601811389639257 + m.x3)**2) + m.x238 * ((-0.6356835687091966 + m.x1)**2
    + (-0.5035384241376479 + m.x2)**2 + (-0.912561201496254 + m.x3)**2) +
    m.x239 * ((-0.07022860689714527 + m.x1)**2 + (-0.7272172999901972 + m.x2)**
    2 + (-0.813209953545937 + m.x3)**2) + m.x240 * ((-0.8817216558635385 + m.x1)
    **2 + (-0.1961060970257913 + m.x2)**2 + (-0.4807253834719928 + m.x3)**2) +
    m.x241 * ((-0.8346893143895587 + m.x1)**2 + (-0.45391356191841836 + m.x2)**
    2 + (-0.03689848229389647 + m.x3)**2) + m.x242 * ((-0.4425064296341201 +
    m.x1)**2 + (-0.23133455702646433 + m.x2)**2 + (-0.4119733748205944 + m.x3)
    **2) + m.x243 * ((-0.48695930579230606 + m.x1)**2 + (-0.7723781894795173 +
    m.x2)**2 + (-0.7896048032875119 + m.x3)**2) + m.x244 * ((
    -0.6213072525945529 + m.x1)**2 + (-0.7463861427401226 + m.x2)**2 + (
    -0.19336124087532391 + m.x3)**2) + m.x245 * ((-0.9407434249412069 + m.x1)**
    2 + (-0.3157287888226875 + m.x2)**2 + (-0.19110493027237785 + m.x3)**2) +
    m.x246 * ((-0.5838103888478602 + m.x1)**2 + (-0.21478748867734254 + m.x2)**
    2 + (-0.8827349895451565 + m.x3)**2) + m.x247 * ((-0.03393239301609985 +
    m.x1)**2 + (-0.34669040395859996 + m.x2)**2 + (-0.6798250093428466 + m.x3)
    **2) + m.x248 * ((-0.9597035244408724 + m.x1)**2 + (-0.32286881217800434 +
    m.x2)**2 + (-0.4444196733141058 + m.x3)**2) + m.x249 * ((
    -0.9457000140765058 + m.x1)**2 + (-0.5068775796046029 + m.x2)**2 + (
    -0.3144273334897483 + m.x3)**2) + m.x250 * ((-0.044943238020383025 + m.x1)
    **2 + (-0.6614992336502294 + m.x2)**2 + (-0.8388656671250995 + m.x3)**2) +
    m.x251 * ((-0.49927342074497827 + m.x1)**2 + (-0.13468517272379243 + m.x2)
    **2 + (-0.4296515446930951 + m.x3)**2) + m.x252 * ((-0.9841852779169674 +
    m.x1)**2 + (-0.9843149988050245 + m.x2)**2 + (-0.47713010572283376 + m.x3)
    **2) + m.x253 * ((-0.4009300133770608 + m.x1)**2 + (-0.0042534179821622775
    + m.x2)**2 + (-0.4175816329130312 + m.x3)**2) + m.x254 * ((
    -0.4885283879651544 + m.x1)**2 + (-0.9079239735865996 + m.x2)**2 + (
    -0.21031335265116158 + m.x3)**2) + m.x255 * ((-0.9849314196407067 + m.x1)**
    2 + (-0.11685357326709411 + m.x2)**2 + (-0.017369390966105014 + m.x3)**2)
    + m.x256 * ((-0.35446426043635526 + m.x1)**2 + (-0.2596023514638419 + m.x2)
    **2 + (-0.32096060367647117 + m.x3)**2) + m.x257 * ((-0.4352313328405867 +
    m.x1)**2 + (-0.6746955457244538 + m.x2)**2 + (-0.25563185786498377 + m.x3)
    **2) + m.x258 * ((-0.699315061557881 + m.x1)**2 + (-0.5915408096298286 +
    m.x2)**2 + (-0.44607763336915063 + m.x3)**2) + m.x259 * ((
    -0.6592318565406342 + m.x1)**2 + (-0.6133226566520651 + m.x2)**2 + (
    -0.5961918051667695 + m.x3)**2) + m.x260 * ((-0.2354774655941887 + m.x1)**2
    + (-0.26243234628674394 + m.x2)**2 + (-0.312388269065189 + m.x3)**2) +
    m.x261 * ((-0.2200373888643452 + m.x1)**2 + (-0.41332951956449515 + m.x2)**
    2 + (-0.9109131978387711 + m.x3)**2) + m.x262 * ((-0.9487139910966843 +
    m.x1)**2 + (-0.5437246273285123 + m.x2)**2 + (-0.07874373064662499 + m.x3)
    **2) + m.x263 * ((-0.5964830453719224 + m.x1)**2 + (-0.0619742726091832 +
    m.x2)**2 + (-0.19927236817826444 + m.x3)**2) + m.x264 * ((
    -0.02759692117192214 + m.x1)**2 + (-0.2966943519059587 + m.x2)**2 + (
    -0.1436425270697561 + m.x3)**2) + m.x265 * ((-0.5605238341170351 + m.x1)**2
    + (-0.16705196889000828 + m.x2)**2 + (-0.4596742351263795 + m.x3)**2) +
    m.x266 * ((-0.9861110555193163 + m.x1)**2 + (-0.8752990513886425 + m.x2)**2
    + (-0.485142331599836 + m.x3)**2) + m.x267 * ((-0.27161250758957267 + m.x1)
    **2 + (-0.9946863069500006 + m.x2)**2 + (-0.439561525186691 + m.x3)**2) +
    m.x268 * ((-0.4836297090054381 + m.x1)**2 + (-0.2114798303676434 + m.x2)**2
    + (-0.1278618145726882 + m.x3)**2) + m.x269 * ((-0.024736008778174612 +
    m.x1)**2 + (-0.9205199923700449 + m.x2)**2 + (-0.8484339940268846 + m.x3)**
    2) + m.x270 * ((-0.5626615620602874 + m.x1)**2 + (-0.034989370194508096 +
    m.x2)**2 + (-0.6632186742091526 + m.x3)**2) + m.x271 * ((
    -0.6438064560050359 + m.x1)**2 + (-0.4889465681575601 + m.x2)**2 + (
    -0.26934659936523253 + m.x3)**2) + m.x272 * ((-0.5261992201164788 + m.x1)**
    2 + (-0.08595932986749422 + m.x2)**2 + (-0.08488216145362637 + m.x3)**2) +
    m.x273 * ((-0.1409322982901524 + m.x1)**2 + (-0.11290088677205301 + m.x2)**
    2 + (-0.1848610267768337 + m.x3)**2) + m.x274 * ((-0.9062469407729168 +
    m.x1)**2 + (-0.443642723519166 + m.x2)**2 + (-0.16301234345822146 + m.x3)**
    2) + m.x275 * ((-0.26280187243977027 + m.x1)**2 + (-0.5791906957767239 +
    m.x2)**2 + (-0.09189211557137555 + m.x3)**2) + m.x276 * ((
    -0.7819362020918313 + m.x1)**2 + (-0.8107913530336736 + m.x2)**2 + (
    -0.08589261011414395 + m.x3)**2) + m.x277 * ((-0.12202077612002771 + m.x1)
    **2 + (-0.09381851826448306 + m.x2)**2 + (-0.9946687189369333 + m.x3)**2)
    + m.x278 * ((-0.7449921585503891 + m.x1)**2 + (-0.44616399084793734 + m.x2)
    **2 + (-0.14733396356242667 + m.x3)**2) + m.x279 * ((-0.8013267039644335 +
    m.x1)**2 + (-0.12726406694941528 + m.x2)**2 + (-0.30755184402270597 + m.x3)
    **2) + m.x280 * ((-0.7129868679977376 + m.x1)**2 + (-0.5624403504682522 +
    m.x2)**2 + (-0.5194087287496278 + m.x3)**2) + m.x281 * ((-0.702605402074762
    + m.x1)**2 + (-0.696542187378441 + m.x2)**2 + (-0.9050186102050559 + m.x3)
    **2) + m.x282 * ((-0.48579654846686027 + m.x1)**2 + (-0.9865716657785814 +
    m.x2)**2 + (-0.7488638018945105 + m.x3)**2) + m.x283 * ((
    -0.14273183621265262 + m.x1)**2 + (-0.16961426380712896 + m.x2)**2 + (
    -0.7336118920897162 + m.x3)**2) + m.x284 * ((-0.508565000330308 + m.x1)**2
    + (-0.0008598073433415676 + m.x2)**2 + (-0.4878861682744219 + m.x3)**2) +
    m.x285 * ((-0.37778026211733495 + m.x1)**2 + (-0.7302042173061916 + m.x2)**
    2 + (-0.658072993274222 + m.x3)**2) + m.x286 * ((-0.5859039531200585 + m.x1)
    **2 + (-0.28185196746339947 + m.x2)**2 + (-0.07351170392618223 + m.x3)**2)
    + m.x287 * ((-0.437816105636769 + m.x1)**2 + (-0.9381650700676218 + m.x2)
    **2 + (-0.7532133630650687 + m.x3)**2) + m.x288 * ((-0.9111142352615409 +
    m.x1)**2 + (-0.9188611987954707 + m.x2)**2 + (-0.7097765364993713 + m.x3)**
    2) + m.x289 * ((-0.6070364816449836 + m.x1)**2 + (-0.6368688399261839 +
    m.x2)**2 + (-0.8097201734033257 + m.x3)**2) + m.x290 * ((
    -0.6984482644711556 + m.x1)**2 + (-0.8822045583167333 + m.x2)**2 + (
    -0.5762293092462573 + m.x3)**2) + m.x291 * ((-0.05085683485354919 + m.x1)**
    2 + (-0.9999183826637328 + m.x2)**2 + (-0.4287782578354542 + m.x3)**2) +
    m.x292 * ((-0.7615905094162454 + m.x1)**2 + (-0.1421067735442294 + m.x2)**2
    + (-0.5006086214169991 + m.x3)**2) + m.x293 * ((-0.9305602823426583 + m.x1)
    **2 + (-0.9752940115114439 + m.x2)**2 + (-0.1631253855890934 + m.x3)**2) +
    m.x294 * ((-0.26027159077598117 + m.x1)**2 + (-0.8467561936966935 + m.x2)**
    2 + (-0.42577439882602497 + m.x3)**2) + m.x295 * ((-0.08104856848069275 +
    m.x1)**2 + (-0.9886967089077169 + m.x2)**2 + (-0.08146796574801807 + m.x3)
    **2) + m.x296 * ((-0.48005659566609715 + m.x1)**2 + (-0.9974410345330987 +
    m.x2)**2 + (-0.48571859403846973 + m.x3)**2) + m.x297 * ((
    -0.4706070697040865 + m.x1)**2 + (-0.22633844473105058 + m.x2)**2 + (
    -0.8430722417451099 + m.x3)**2) + m.x298 * ((-0.6581283586576836 + m.x1)**2
    + (-0.2988361857206986 + m.x2)**2 + (-0.5248717962910134 + m.x3)**2) +
    m.x299 * ((-0.4139397565643148 + m.x1)**2 + (-0.7947219857264776 + m.x2)**2
    + (-0.9714023432927014 + m.x3)**2) + m.x300 * ((-0.29895041273047895 +
    m.x1)**2 + (-0.20934319073619012 + m.x2)**2 + (-0.12799433802173388 + m.x3)
    **2) + m.x301 * ((-0.7416051505394204 + m.x1)**2 + (-0.8610181415202831 +
    m.x2)**2 + (-0.8203512359906585 + m.x3)**2) + m.x302 * ((
    -0.8539442696762753 + m.x1)**2 + (-0.6440119856376406 + m.x2)**2 + (
    -0.04768006379778733 + m.x3)**2) + m.x303 * ((-0.8078856580669804 + m.x1)**
    2 + (-0.0811738770099133 + m.x2)**2 + (-0.42296333968011834 + m.x3)**2) +
    m.x304 * ((-0.11293172487506897 + m.x1)**2 + (-0.10190845514217972 + m.x2)
    **2 + (-0.025155476939746846 + m.x3)**2) + m.x305 * ((-0.6774554514175933
    + m.x1)**2 + (-0.28953130741751354 + m.x2)**2 + (-0.7231890256224531 +
    m.x3)**2) + m.x306 * ((-0.9658389665612165 + m.x1)**2 + (
    -0.8012920581552374 + m.x2)**2 + (-0.6871461962217258 + m.x3)**2) + m.x307
    * ((-0.5345563351474161 + m.x1)**2 + (-0.11378244706430707 + m.x2)**2 + (
    -0.7915828478976272 + m.x3)**2) + m.x308 * ((-0.9997767651100092 + m.x1)**2
    + (-0.5574720960939473 + m.x2)**2 + (-0.7410926285969115 + m.x3)**2) +
    m.x309 * ((-0.29777709756222204 + m.x1)**2 + (-0.13420768997570653 + m.x2)
    **2 + (-0.41098786274229304 + m.x3)**2) + m.x310 * ((-0.4890881424574446 +
    m.x1)**2 + (-0.404669840371118 + m.x2)**2 + (-0.6839329573384761 + m.x3)**2)
    + m.x311 * ((-0.9275207698350674 + m.x1)**2 + (-0.6349688118385305 + m.x2)
    **2 + (-0.16211201636277606 + m.x3)**2) + m.x312 * ((-0.31185430455711194
    + m.x1)**2 + (-0.9609480087595885 + m.x2)**2 + (-0.48506492880423546 +
    m.x3)**2) + m.x313 * ((-0.7594140721620825 + m.x1)**2 + (
    -0.9263148514595829 + m.x2)**2 + (-0.8648033086118 + m.x3)**2) + m.x314 * (
    (-0.6479304574703105 + m.x1)**2 + (-0.8228423329287321 + m.x2)**2 + (
    -0.7551761939784829 + m.x3)**2) + m.x315 * ((-0.8231579504797958 + m.x1)**2
    + (-0.05635445777892223 + m.x2)**2 + (-0.02468508246924883 + m.x3)**2) +
    m.x316 * ((-0.5969304027180449 + m.x1)**2 + (-0.8273519061055513 + m.x2)**2
    + (-0.8975627019214554 + m.x3)**2) + m.x317 * ((-0.47032986801594845 +
    m.x1)**2 + (-0.03758087479779437 + m.x2)**2 + (-0.956428581402661 + m.x3)**
    2) + m.x318 * ((-0.058484373437283965 + m.x1)**2 + (-0.7224332485058074 +
    m.x2)**2 + (-0.36656511074725406 + m.x3)**2) + m.x319 * ((
    -0.8067441195220981 + m.x1)**2 + (-0.6939130038104055 + m.x2)**2 + (
    -0.6650852436958627 + m.x3)**2) + m.x320 * ((-0.14316346421133996 + m.x1)**
    2 + (-0.8833335241651658 + m.x2)**2 + (-0.33873721710142757 + m.x3)**2) +
    m.x321 * ((-0.16663405286282917 + m.x1)**2 + (-0.1361097149511954 + m.x2)**
    2 + (-0.4167589692247934 + m.x3)**2) + m.x322 * ((-0.3533518801743728 +
    m.x1)**2 + (-0.7864769418639855 + m.x2)**2 + (-0.5700369360657614 + m.x3)**
    2) + m.x323 * ((-0.9940450532017178 + m.x1)**2 + (-0.8709964325378182 +
    m.x2)**2 + (-0.05370495768985595 + m.x3)**2) + m.x324 * ((-0.43669423470125
    + m.x1)**2 + (-0.7826943195653798 + m.x2)**2 + (-0.08246841776453673 +
    m.x3)**2) + m.x325 * ((-0.31217298303878716 + m.x1)**2 + (
    -0.12873842883308007 + m.x2)**2 + (-0.4120375477605329 + m.x3)**2) + m.x326
    * ((-0.04729057034546036 + m.x1)**2 + (-0.615848875622511 + m.x2)**2 + (
    -0.09028092669134402 + m.x3)**2) + m.x327 * ((-0.05579397155334043 + m.x1)
    **2 + (-0.45731350085562406 + m.x2)**2 + (-0.5113200354339912 + m.x3)**2)
    + m.x328 * ((-0.24317770299974573 + m.x1)**2 + (-0.31432958156550617 +
    m.x2)**2 + (-0.29916426285821995 + m.x3)**2) + m.x329 * ((
    -0.6647683703847979 + m.x1)**2 + (-0.5720315504033884 + m.x2)**2 + (
    -0.3330271930609998 + m.x3)**2) + m.x330 * ((-0.0671508784075493 + m.x1)**2
    + (-0.7427046256777622 + m.x2)**2 + (-0.3842554432358185 + m.x3)**2) +
    m.x331 * ((-0.5142618830032626 + m.x1)**2 + (-0.37920880558154235 + m.x2)**
    2 + (-0.17375109475213701 + m.x3)**2) + m.x332 * ((-0.039030898150579474 +
    m.x1)**2 + (-0.416088697819994 + m.x2)**2 + (-0.23777905803288724 + m.x3)**
    2) + m.x333 * ((-0.4717971485183111 + m.x1)**2 + (-0.3383860380066811 +
    m.x2)**2 + (-0.460200523195855 + m.x3)**2) + m.x334 * ((-0.5900378880204267
    + m.x1)**2 + (-0.7255901375319337 + m.x2)**2 + (-0.9154170002928985 + m.x3)
    **2) + m.x335 * ((-0.13093900398824065 + m.x1)**2 + (-0.4052139060110297 +
    m.x2)**2 + (-0.49962194728297327 + m.x3)**2) + m.x336 * ((
    -0.5001698078829642 + m.x1)**2 + (-0.7979303589649438 + m.x2)**2 + (
    -0.2739293646511145 + m.x3)**2) + m.x337 * ((-0.41855315898554013 + m.x1)**
    2 + (-0.998699983121554 + m.x2)**2 + (-0.2010058221141684 + m.x3)**2) +
    m.x338 * ((-0.7496871098706305 + m.x1)**2 + (-0.8235726845357767 + m.x2)**2
    + (-0.37015198039038577 + m.x3)**2) + m.x339 * ((-0.28403104119909195 +
    m.x1)**2 + (-0.6420274479177237 + m.x2)**2 + (-0.4574273157370161 + m.x3)**
    2) + m.x340 * ((-0.46685731585307466 + m.x1)**2 + (-0.26906412522677103 +
    m.x2)**2 + (-0.6656657277253054 + m.x3)**2) + m.x341 * ((
    -0.2504282905612786 + m.x1)**2 + (-0.15851796206472113 + m.x2)**2 + (
    -0.4726147469986297 + m.x3)**2) + m.x342 * ((-0.21194510336903394 + m.x1)**
    2 + (-0.7789673451440703 + m.x2)**2 + (-0.09841245851637492 + m.x3)**2) +
    m.x343 * ((-0.2349671005207027 + m.x1)**2 + (-0.0221927931737832 + m.x2)**2
    + (-0.5712554822182071 + m.x3)**2) + m.x344 * ((-0.0009451790835207641 +
    m.x1)**2 + (-0.2408337245798331 + m.x2)**2 + (-0.6211924391868702 + m.x3)**
    2) + m.x345 * ((-0.6707250517356161 + m.x1)**2 + (-0.5984637186180205 +
    m.x2)**2 + (-0.0668641338162419 + m.x3)**2) + m.x346 * ((
    -0.5511472131778885 + m.x1)**2 + (-0.07350867542191697 + m.x2)**2 + (
    -0.767739792767608 + m.x3)**2) + m.x347 * ((-0.9501581392192964 + m.x1)**2
    + (-0.7233163389390355 + m.x2)**2 + (-0.5166844510344849 + m.x3)**2) +
    m.x348 * ((-0.9060156230362852 + m.x1)**2 + (-0.3113487821639962 + m.x2)**2
    + (-0.20778084543419917 + m.x3)**2) + m.x349 * ((-0.5288680482784139 +
    m.x1)**2 + (-0.2934145990378463 + m.x2)**2 + (-0.4804974743654282 + m.x3)**
    2) + m.x350 * ((-0.09966115943905263 + m.x1)**2 + (-0.3938725699296275 +
    m.x2)**2 + (-0.32444318785821924 + m.x3)**2) + m.x351 * ((
    -0.6520321563540667 + m.x1)**2 + (-0.8056068500183343 + m.x2)**2 + (
    -0.0835838533559482 + m.x3)**2) + m.x352 * ((-0.8166208988287386 + m.x1)**2
    + (-0.3518761684344235 + m.x2)**2 + (-0.7464113961140431 + m.x3)**2) +
    m.x353 * ((-0.1311593203796163 + m.x1)**2 + (-0.7160405481109373 + m.x2)**2
    + (-0.09952132645843448 + m.x3)**2) + m.x354 * ((-0.04779808112037798 +
    m.x1)**2 + (-0.28884699291713234 + m.x2)**2 + (-0.10250649388727473 + m.x3)
    **2) + m.x355 * ((-0.9791729605203251 + m.x1)**2 + (-0.6726875461066422 +
    m.x2)**2 + (-0.9283118905188722 + m.x3)**2) + m.x356 * ((
    -0.13471412533270244 + m.x1)**2 + (-0.7071806165289065 + m.x2)**2 + (
    -0.9043216254262293 + m.x3)**2) + m.x357 * ((-0.5735353939945473 + m.x1)**2
    + (-0.5273208712530736 + m.x2)**2 + (-0.6875628347914862 + m.x3)**2) +
    m.x358 * ((-0.9582137553329777 + m.x1)**2 + (-0.4500040273602035 + m.x2)**2
    + (-0.26668127604253744 + m.x3)**2) + m.x359 * ((-0.35515505710029105 +
    m.x1)**2 + (-0.8998261443565795 + m.x2)**2 + (-0.5147227718297207 + m.x3)**
    2) + m.x360 * ((-0.9340214668622013 + m.x1)**2 + (-0.3503931266703305 +
    m.x2)**2 + (-0.22213442770583658 + m.x3)**2) + m.x361 * ((
    -0.30063857818433126 + m.x1)**2 + (-0.9781639681666726 + m.x2)**2 + (
    -0.5737192124395999 + m.x3)**2) + m.x362 * ((-0.9694287446674323 + m.x1)**2
    + (-0.9139936410886877 + m.x2)**2 + (-0.16757766484105074 + m.x3)**2) +
    m.x363 * ((-0.040594150617694 + m.x1)**2 + (-0.43898895567045837 + m.x2)**2
    + (-0.6978737824797022 + m.x3)**2) + m.x364 * ((-0.9047320599530371 + m.x1)
    **2 + (-0.4912564771269612 + m.x2)**2 + (-0.6733487941467664 + m.x3)**2) +
    m.x365 * ((-0.9549617147031715 + m.x1)**2 + (-0.6678649305928561 + m.x2)**2
    + (-0.8834928821311292 + m.x3)**2) + m.x366 * ((-0.4395498573390294 + m.x1)
    **2 + (-0.30627811842262354 + m.x2)**2 + (-0.9750459496357505 + m.x3)**2)
    + m.x367 * ((-0.1870595942163641 + m.x1)**2 + (-0.151585797566554 + m.x2)
    **2 + (-0.6096114448910821 + m.x3)**2) + m.x368 * ((-0.8951229638762037 +
    m.x1)**2 + (-0.5978267742373706 + m.x2)**2 + (-0.5837237511628297 + m.x3)**
    2) + m.x369 * ((-0.9979607832682635 + m.x1)**2 + (-0.2544630128273442 +
    m.x2)**2 + (-0.7553436617442503 + m.x3)**2) + m.x370 * ((
    -0.18874920320016164 + m.x1)**2 + (-0.6216165758809351 + m.x2)**2 + (
    -0.8529149249653111 + m.x3)**2) + m.x371 * ((-0.6373429941144889 + m.x1)**2
    + (-0.03524085604839855 + m.x2)**2 + (-0.2902922940078507 + m.x3)**2) +
    m.x372 * ((-0.1493240329654184 + m.x1)**2 + (-0.773610378940084 + m.x2)**2
    + (-0.16800156102583386 + m.x3)**2) + m.x373 * ((-0.45959660687249615 +
    m.x1)**2 + (-0.8091285040534932 + m.x2)**2 + (-0.3286890399482034 + m.x3)**
    2) + m.x374 * ((-0.7478644912889102 + m.x1)**2 + (-0.014858297372218665 +
    m.x2)**2 + (-0.6866332635878059 + m.x3)**2) + m.x375 * ((
    -0.7646420573532026 + m.x1)**2 + (-0.9447630530244876 + m.x2)**2 + (
    -0.8190368275925283 + m.x3)**2) + m.x376 * ((-0.9924396130442916 + m.x1)**2
    + (-0.6082265831465189 + m.x2)**2 + (-0.5057251733236754 + m.x3)**2) +
    m.x377 * ((-0.7721758593783997 + m.x1)**2 + (-0.8129769760490057 + m.x2)**2
    + (-0.4066778113300017 + m.x3)**2) + m.x378 * ((-0.5586622471964208 + m.x1)
    **2 + (-0.7449498935310548 + m.x2)**2 + (-0.5133001652292216 + m.x3)**2) +
    m.x379 * ((-0.2606143437838706 + m.x1)**2 + (-0.9157831128583509 + m.x2)**2
    + (-0.7725742539135185 + m.x3)**2) + m.x380 * ((-0.08665312749944609 +
    m.x1)**2 + (-0.20774241016302275 + m.x2)**2 + (-0.392846511749778 + m.x3)**
    2) + m.x381 * ((-0.02318360583183654 + m.x1)**2 + (-0.12136671002398913 +
    m.x2)**2 + (-0.4592804310959082 + m.x3)**2) + m.x382 * ((
    -0.9376542898841029 + m.x1)**2 + (-0.7296259410537214 + m.x2)**2 + (
    -0.43830339602774704 + m.x3)**2) + m.x383 * ((-0.7366058903091773 + m.x1)**
    2 + (-0.4416494908995052 + m.x2)**2 + (-0.8513541067232596 + m.x3)**2) +
    m.x384 * ((-0.2583528714273713 + m.x1)**2 + (-0.8887871795539201 + m.x2)**2
    + (-0.7248310640320087 + m.x3)**2) + m.x385 * ((-0.13907399568052925 +
    m.x1)**2 + (-0.5677374171942082 + m.x2)**2 + (-0.7157625382944803 + m.x3)**
    2) + m.x386 * ((-0.4868142512204441 + m.x1)**2 + (-0.8622063298179061 +
    m.x2)**2 + (-0.4912823321311274 + m.x3)**2) + m.x387 * ((
    -0.5544960376270748 + m.x1)**2 + (-0.8879916713525825 + m.x2)**2 + (
    -0.558510394418158 + m.x3)**2) + m.x388 * ((-0.5629250097194626 + m.x1)**2
    + (-0.02440020191041392 + m.x2)**2 + (-0.3505563159384506 + m.x3)**2) +
    m.x389 * ((-0.5644814229596812 + m.x1)**2 + (-0.9167284919592144 + m.x2)**2
    + (-0.39495515159248495 + m.x3)**2) + m.x390 * ((-0.15293694448570427 +
    m.x1)**2 + (-0.24201305054502364 + m.x2)**2 + (-0.09871933794597176 + m.x3)
    **2) + m.x391 * ((-0.04093761196800816 + m.x1)**2 + (-0.25111569049272453
    + m.x2)**2 + (-0.8857385934563612 + m.x3)**2) + m.x392 * ((
    -0.6455628697859762 + m.x1)**2 + (-0.4324293933492942 + m.x2)**2 + (
    -0.3789568433740764 + m.x3)**2) + m.x393 * ((-0.4496937933648343 + m.x1)**2
    + (-0.5667328853687145 + m.x2)**2 + (-0.40691835531776066 + m.x3)**2) +
    m.x394 * ((-0.5064964841495636 + m.x1)**2 + (-0.9231662667070567 + m.x2)**2
    + (-0.9418870813951559 + m.x3)**2) + m.x395 * ((-0.7546510193031142 + m.x1)
    **2 + (-0.6290717885174039 + m.x2)**2 + (-0.9053863219371039 + m.x3)**2) +
    m.x396 * ((-0.1252499507413295 + m.x1)**2 + (-0.7291266598331314 + m.x2)**2
    + (-0.06287245807908282 + m.x3)**2) + m.x397 * ((-0.975079670779934 + m.x1)
    **2 + (-0.8476261704965108 + m.x2)**2 + (-0.3613523225014157 + m.x3)**2) +
    m.x398 * ((-0.4786145006916671 + m.x1)**2 + (-0.7562794398860281 + m.x2)**2
    + (-0.3246606771087578 + m.x3)**2) + m.x399 * ((-0.37211638738323183 +
    m.x1)**2 + (-0.5285143564556392 + m.x2)**2 + (-0.9473677259758877 + m.x3)**
    2) + m.x400 * ((-0.7747359569068005 + m.x1)**2 + (-0.5606816325734337 +
    m.x2)**2 + (-0.5023744358753353 + m.x3)**2) + m.x401 * ((
    -0.35934929189237974 + m.x1)**2 + (-0.2138842746533064 + m.x2)**2 + (
    -0.47940265124118275 + m.x3)**2) + m.x402 * ((-0.034039058901423114 + m.x1)
    **2 + (-0.8692672460914023 + m.x2)**2 + (-0.7367556473491849 + m.x3)**2) +
    m.x403 * ((-0.7282365643923602 + m.x1)**2 + (-0.6873407784728088 + m.x2)**2
    + (-0.40274097414378485 + m.x3)**2) + m.x404 * ((-0.734857721471257 + m.x1)
    **2 + (-0.262970187892116 + m.x2)**2 + (-0.20961569008988468 + m.x3)**2) +
    m.x405 * ((-0.6525308383090344 + m.x1)**2 + (-0.19608022401263447 + m.x2)**
    2 + (-0.3870236183372049 + m.x3)**2) + m.x406 * ((-0.5645012980468977 +
    m.x1)**2 + (-0.6341191192370838 + m.x2)**2 + (-0.46196225878784536 + m.x3)
    **2) + m.x407 * ((-0.2930551852644451 + m.x1)**2 + (-0.9177900459954397 +
    m.x2)**2 + (-0.5732383676108328 + m.x3)**2) + m.x408 * ((
    -0.5092355531007602 + m.x1)**2 + (-0.18305497891779976 + m.x2)**2 + (
    -0.09370849097948963 + m.x3)**2) + m.x409 * ((-0.9512334177368659 + m.x1)**
    2 + (-0.07342868658441148 + m.x2)**2 + (-0.9395727539085917 + m.x3)**2) +
    m.x410 * ((-0.8094970632512009 + m.x1)**2 + (-0.7305977116464875 + m.x2)**2
    + (-0.8070135155255885 + m.x3)**2) + m.x411 * ((-0.8962127199770125 + m.x1)
    **2 + (-0.24616592065326037 + m.x2)**2 + (-0.5849517947792571 + m.x3)**2)
    + m.x412 * ((-0.7052505213025646 + m.x1)**2 + (-0.0796535796359964 + m.x2)
    **2 + (-0.20277742799437048 + m.x3)**2) + m.x413 * ((-0.6267785193143974 +
    m.x1)**2 + (-0.10746876474982292 + m.x2)**2 + (-0.6494432790830167 + m.x3)
    **2) + m.x414 * ((-0.015520366623647752 + m.x1)**2 + (-0.5842081993611541
    + m.x2)**2 + (-0.2744519446961057 + m.x3)**2) + m.x415 * ((
    -0.9793566236203548 + m.x1)**2 + (-0.22394521684566593 + m.x2)**2 + (
    -0.9058719953285858 + m.x3)**2) + m.x416 * ((-0.3542633017907568 + m.x1)**2
    + (-0.44060726802651784 + m.x2)**2 + (-0.3997128293238619 + m.x3)**2) +
    m.x417 * ((-0.482866380882348 + m.x1)**2 + (-0.18588499288268157 + m.x2)**2
    + (-0.07945614131161916 + m.x3)**2) + m.x418 * ((-0.10608910682131378 +
    m.x1)**2 + (-0.26438328524024857 + m.x2)**2 + (-0.2864127662313217 + m.x3)
    **2) + m.x419 * ((-0.39587823045804427 + m.x1)**2 + (-0.5695813324890586 +
    m.x2)**2 + (-0.1920662220868672 + m.x3)**2) + m.x420 * ((
    -0.06159942259296125 + m.x1)**2 + (-0.24020437828961405 + m.x2)**2 + (
    -0.3840367843355983 + m.x3)**2) + m.x421 * ((-0.7362258383939748 + m.x1)**2
    + (-0.7652235683510016 + m.x2)**2 + (-0.5080623929895395 + m.x3)**2) +
    m.x422 * ((-0.6717905352420465 + m.x1)**2 + (-0.13175135938896554 + m.x2)**
    2 + (-0.8733829715017289 + m.x3)**2) + m.x423 * ((-0.5087936806553548 +
    m.x1)**2 + (-0.9895784354332001 + m.x2)**2 + (-0.5235243911248123 + m.x3)**
    2) + m.x424 * ((-0.5687248806674255 + m.x1)**2 + (-0.4800426470754785 +
    m.x2)**2 + (-0.66476015670848 + m.x3)**2) + m.x425 * ((-0.01879712601243244
    + m.x1)**2 + (-0.9597300904119254 + m.x2)**2 + (-0.6400022174824137 + m.x3)
    **2) + m.x426 * ((-0.4546748066299232 + m.x1)**2 + (-0.08414046444682621 +
    m.x2)**2 + (-0.39949639976218343 + m.x3)**2) + m.x427 * ((
    -0.17854814031575228 + m.x1)**2 + (-0.24423555096632876 + m.x2)**2 + (
    -0.31176738263506176 + m.x3)**2) + m.x428 * ((-0.9738568400798214 + m.x1)**
    2 + (-0.9761211517297564 + m.x2)**2 + (-0.12716216361863075 + m.x3)**2) +
    m.x429 * ((-0.10905660727366906 + m.x1)**2 + (-0.9795748590019786 + m.x2)**
    2 + (-0.7440984394159507 + m.x3)**2) + m.x430 * ((-0.7666642751173116 +
    m.x1)**2 + (-0.3496890268415409 + m.x2)**2 + (-0.7178355854854029 + m.x3)**
    2) + m.x431 * ((-0.013742724746700241 + m.x1)**2 + (-0.43305298229497435 +
    m.x2)**2 + (-0.7254669199672814 + m.x3)**2) + m.x432 * ((
    -0.3275886542048829 + m.x1)**2 + (-0.8378680301704793 + m.x2)**2 + (
    -0.8349975326026666 + m.x3)**2) + m.x433 * ((-0.060805710429040816 + m.x1)
    **2 + (-0.656788371625089 + m.x2)**2 + (-0.2732796886924793 + m.x3)**2) +
    m.x434 * ((-0.9053177349583378 + m.x1)**2 + (-0.16127902677760553 + m.x2)**
    2 + (-0.32227488757718703 + m.x3)**2) + m.x435 * ((-0.9764291442509151 +
    m.x1)**2 + (-0.4200251729022414 + m.x2)**2 + (-0.19500625315790188 + m.x3)
    **2) + m.x436 * ((-0.17071396326782584 + m.x1)**2 + (-0.5019541154498613 +
    m.x2)**2 + (-0.6526843192881269 + m.x3)**2) + m.x437 * ((
    -0.9126755236735188 + m.x1)**2 + (-0.28940415967047584 + m.x2)**2 + (
    -0.1552734500527927 + m.x3)**2) + m.x438 * ((-0.5606535962065278 + m.x1)**2
    + (-0.6342833304382927 + m.x2)**2 + (-0.8585431561155562 + m.x3)**2) +
    m.x439 * ((-0.11687570322670404 + m.x1)**2 + (-0.42299970942250387 + m.x2)
    **2 + (-0.4170059716014207 + m.x3)**2) + m.x440 * ((-0.5142371687254527 +
    m.x1)**2 + (-0.9857105100813118 + m.x2)**2 + (-0.5015291171995875 + m.x3)**
    2) + m.x441 * ((-0.32100216013315164 + m.x1)**2 + (-0.45572573844602215 +
    m.x2)**2 + (-0.48798435784356275 + m.x3)**2) + m.x442 * ((
    -0.597784767358479 + m.x1)**2 + (-0.05186929074401203 + m.x2)**2 + (
    -0.226366390881664 + m.x3)**2) + m.x443 * ((-0.8457016489109802 + m.x1)**2
    + (-0.5554063005937154 + m.x2)**2 + (-0.41321444364538085 + m.x3)**2) +
    m.x444 * ((-0.9475471193586129 + m.x1)**2 + (-0.3121559515841179 + m.x2)**2
    + (-0.14073436444324727 + m.x3)**2) + m.x445 * ((-0.7462797111675085 +
    m.x1)**2 + (-0.0832491058608037 + m.x2)**2 + (-0.16991972648761744 + m.x3)
    **2) + m.x446 * ((-0.6283905422614516 + m.x1)**2 + (-0.3473036441315591 +
    m.x2)**2 + (-0.6256420116557863 + m.x3)**2) + m.x447 * ((
    -0.47557752055186076 + m.x1)**2 + (-0.13087273477706074 + m.x2)**2 + (
    -0.566009659206059 + m.x3)**2) + m.x448 * ((-0.3811223652765986 + m.x1)**2
    + (-0.3419162921570369 + m.x2)**2 + (-0.42670986021880697 + m.x3)**2) +
    m.x449 * ((-0.45276296485818746 + m.x1)**2 + (-0.7292869084688621 + m.x2)**
    2 + (-0.9219484257715016 + m.x3)**2) + m.x450 * ((-0.2944563711575213 +
    m.x1)**2 + (-0.9768141635311406 + m.x2)**2 + (-0.9139907883287979 + m.x3)**
    2) + m.x451 * ((-0.2045693815413957 + m.x1)**2 + (-0.6083069865306869 +
    m.x2)**2 + (-0.5354494090536733 + m.x3)**2) + m.x452 * ((
    -0.9092286101623649 + m.x1)**2 + (-0.19827382634748447 + m.x2)**2 + (
    -0.5692289216759975 + m.x3)**2) + m.x453 * ((-0.4428119569466705 + m.x1)**2
    + (-0.3322800930778397 + m.x2)**2 + (-0.5707107027562174 + m.x3)**2) +
    m.x454 * ((-0.419027742190789 + m.x1)**2 + (-0.4618756991792069 + m.x2)**2
    + (-0.07896233563766164 + m.x3)**2) + m.x455 * ((-0.6584988862725016 +
    m.x1)**2 + (-0.6148209199675768 + m.x2)**2 + (-0.24819109836653064 + m.x3)
    **2) + m.x456 * ((-0.7067453957053103 + m.x1)**2 + (-0.16400947550811773 +
    m.x2)**2 + (-0.2404675897181846 + m.x3)**2) + m.x457 * ((
    -0.6059340157584386 + m.x1)**2 + (-0.368724454571691 + m.x2)**2 + (
    -0.3166424342634133 + m.x3)**2) + m.x458 * ((-0.1505689967926862 + m.x1)**2
    + (-0.625369145400853 + m.x2)**2 + (-0.8732323044478142 + m.x3)**2) +
    m.x459 * ((-0.4387938575304804 + m.x1)**2 + (-0.6686693605208012 + m.x2)**2
    + (-0.5707959366759914 + m.x3)**2) + m.x460 * ((-0.7576333064836764 + m.x1)
    **2 + (-0.15002688954303656 + m.x2)**2 + (-0.15547993353000245 + m.x3)**2)
    + m.x461 * ((-0.666581715107795 + m.x1)**2 + (-0.8984605497623024 + m.x2)
    **2 + (-0.3096514261621284 + m.x3)**2) + m.x462 * ((-0.8387444625970372 +
    m.x1)**2 + (-0.16015110460364135 + m.x2)**2 + (-0.17793311971345638 + m.x3)
    **2) + m.x463 * ((-0.7961300734270524 + m.x1)**2 + (-0.06315804030987215 +
    m.x2)**2 + (-0.2886538911688289 + m.x3)**2) + m.x464 * ((
    -0.09882382311717897 + m.x1)**2 + (-0.9562490103711244 + m.x2)**2 + (
    -0.3979053832361369 + m.x3)**2) + m.x465 * ((-0.1313503761972874 + m.x1)**2
    + (-0.1784477941922571 + m.x2)**2 + (-0.26652042199603243 + m.x3)**2) +
    m.x466 * ((-0.5560596702183167 + m.x1)**2 + (-0.776379609944948 + m.x2)**2
    + (-0.4248340064314263 + m.x3)**2) + m.x467 * ((-0.061904031651977 + m.x1)
    **2 + (-0.6153844859790686 + m.x2)**2 + (-0.9267629321786096 + m.x3)**2) +
    m.x468 * ((-0.22406567435416147 + m.x1)**2 + (-0.16598467807059802 + m.x2)
    **2 + (-0.631039868789005 + m.x3)**2) + m.x469 * ((-0.2067711913915432 +
    m.x1)**2 + (-0.9546739138625829 + m.x2)**2 + (-0.6132888596828534 + m.x3)**
    2) + m.x470 * ((-0.698359896593753 + m.x1)**2 + (-0.09633791817043569 +
    m.x2)**2 + (-0.7767762514491409 + m.x3)**2) + m.x471 * ((
    -0.5495935658571374 + m.x1)**2 + (-0.08474290481778801 + m.x2)**2 + (
    -0.6612846791750243 + m.x3)**2) + m.x472 * ((-0.3161875292045071 + m.x1)**2
    + (-0.6387922458536845 + m.x2)**2 + (-0.7653392459044 + m.x3)**2) + m.x473
    * ((-0.7319358324745259 + m.x1)**2 + (-0.992182632521313 + m.x2)**2 + (
    -0.6863923077018874 + m.x3)**2) + m.x474 * ((-0.6019092920263115 + m.x1)**2
    + (-0.7773860008024426 + m.x2)**2 + (-0.696651134077001 + m.x3)**2) +
    m.x475 * ((-0.8049096869634418 + m.x1)**2 + (-0.0732355551315873 + m.x2)**2
    + (-0.5890554014646376 + m.x3)**2) + m.x476 * ((-0.2400029979216146 + m.x1)
    **2 + (-0.9945676004924368 + m.x2)**2 + (-0.5289410390414967 + m.x3)**2) +
    m.x477 * ((-0.2766431455253143 + m.x1)**2 + (-0.8539068538716186 + m.x2)**2
    + (-0.20627516491122866 + m.x3)**2) + m.x478 * ((-0.35956937240024434 +
    m.x1)**2 + (-0.1564680965685581 + m.x2)**2 + (-0.13254723904140797 + m.x3)
    **2) + m.x479 * ((-0.6851905938616645 + m.x1)**2 + (-0.92350145756233 +
    m.x2)**2 + (-0.12850409116051253 + m.x3)**2) + m.x480 * ((
    -0.8530335314027025 + m.x1)**2 + (-0.014728381555152992 + m.x2)**2 + (
    -0.3823239089970707 + m.x3)**2) + m.x481 * ((-0.20793230117071493 + m.x1)**
    2 + (-0.16676956450110558 + m.x2)**2 + (-0.34228112340343475 + m.x3)**2) +
    m.x482 * ((-0.6234604214732817 + m.x1)**2 + (-0.2502728265106259 + m.x2)**2
    + (-0.3410768048568552 + m.x3)**2) + m.x483 * ((-0.32574485718659996 +
    m.x1)**2 + (-0.49133487411842436 + m.x2)**2 + (-0.9269586652185272 + m.x3)
    **2) + m.x484 * ((-0.8074001332885633 + m.x1)**2 + (-0.436124135331206 +
    m.x2)**2 + (-0.6967988731368366 + m.x3)**2) + m.x485 * ((
    -0.0885078496198809 + m.x1)**2 + (-0.06383953819167731 + m.x2)**2 + (
    -0.12724142698377883 + m.x3)**2) + m.x486 * ((-0.2337562876270498 + m.x1)**
    2 + (-0.17694669799647322 + m.x2)**2 + (-0.24213277883073392 + m.x3)**2) +
    m.x487 * ((-0.4489386544210575 + m.x1)**2 + (-0.39350049538525844 + m.x2)**
    2 + (-0.2766646939987202 + m.x3)**2) + m.x488 * ((-0.6295217224500858 +
    m.x1)**2 + (-0.2004219022799547 + m.x2)**2 + (-0.34401008781100983 + m.x3)
    **2) + m.x489 * ((-0.7178536888350097 + m.x1)**2 + (-0.4777123128107543 +
    m.x2)**2 + (-0.020254499193558706 + m.x3)**2) + m.x490 * ((
    -0.11689305631558389 + m.x1)**2 + (-0.7921096764850253 + m.x2)**2 + (
    -0.0018493281679282658 + m.x3)**2) + m.x491 * ((-0.42252861541271625 + m.x1)
    **2 + (-0.7365281026729076 + m.x2)**2 + (-0.24208265132422635 + m.x3)**2)
    + m.x492 * ((-0.7215969240513533 + m.x1)**2 + (-0.3256843299668196 + m.x2)
    **2 + (-0.3698108298221342 + m.x3)**2) + m.x493 * ((-0.2595423236714335 +
    m.x1)**2 + (-0.2589559818665762 + m.x2)**2 + (-0.18615386799497224 + m.x3)
    **2) + m.x494 * ((-0.9984305905352117 + m.x1)**2 + (-0.7165229939904344 +
    m.x2)**2 + (-0.1285692611907402 + m.x3)**2) + m.x495 * ((
    -0.8872140808683944 + m.x1)**2 + (-0.5011145036032805 + m.x2)**2 + (
    -0.3883708507632184 + m.x3)**2) + m.x496 * ((-0.3924529848246979 + m.x1)**2
    + (-0.22348565481301363 + m.x2)**2 + (-0.2061044173907518 + m.x3)**2) +
    m.x497 * ((-0.9112329633612304 + m.x1)**2 + (-0.3163218232655004 + m.x2)**2
    + (-0.20302411889796268 + m.x3)**2) + m.x498 * ((-0.6097913445881256 +
    m.x1)**2 + (-0.4542976898151134 + m.x2)**2 + (-0.6195483822905107 + m.x3)**
    2) + m.x499 * ((-0.15522553621050394 + m.x1)**2 + (-0.01999404860523235 +
    m.x2)**2 + (-0.23442286593451234 + m.x3)**2) + m.x500 * ((
    -0.9199134838866957 + m.x1)**2 + (-0.7868442189111334 + m.x2)**2 + (
    -0.34080460170453486 + m.x3)**2) + m.x501 * ((-0.8166348595782067 + m.x1)**
    2 + (-0.7614497805023087 + m.x2)**2 + (-0.5452680081023854 + m.x3)**2) +
    m.x502 * ((-0.7603340178252571 + m.x1)**2 + (-0.08882941137693179 + m.x2)**
    2 + (-0.31747640494684937 + m.x3)**2) + m.x503 * ((-0.5390106156174557 +
    m.x1)**2 + (-0.4032399762516905 + m.x2)**2 + (-0.034174294693909646 + m.x3)
    **2) + m.x504 * ((-0.6762581280338263 + m.x1)**2 + (-0.1341686429284461 +
    m.x2)**2 + (-0.6300346342580874 + m.x3)**2) + m.x505 * ((
    -0.5985705326875344 + m.x1)**2 + (-0.6782117564373487 + m.x2)**2 + (
    -0.9723972807848017 + m.x3)**2) + m.x506 * ((-0.9582896782474865 + m.x1)**2
    + (-0.647483553547818 + m.x2)**2 + (-0.2553574307779871 + m.x3)**2) +
    m.x507 * ((-0.1692498439422696 + m.x4)**2 + (-0.594909962110926 + m.x5)**2
    + (-0.2649627397072344 + m.x6)**2) + m.x508 * ((-0.4299773164971996 + m.x4)
    **2 + (-0.8599590238209864 + m.x5)**2 + (-0.5477886873552766 + m.x6)**2) +
    m.x509 * ((-0.5826003170056784 + m.x4)**2 + (-0.941883448057164 + m.x5)**2
    + (-0.30867313678242836 + m.x6)**2) + m.x510 * ((-0.6888712108376565 +
    m.x4)**2 + (-0.46694321374927916 + m.x5)**2 + (-0.20339940372771748 + m.x6)
    **2) + m.x511 * ((-0.4405711594738192 + m.x4)**2 + (-0.5080910724835329 +
    m.x5)**2 + (-0.18540147512570138 + m.x6)**2) + m.x512 * ((
    -0.36908840219684824 + m.x4)**2 + (-0.9606901577735717 + m.x5)**2 + (
    -0.1579661214699748 + m.x6)**2) + m.x513 * ((-0.39554390595886324 + m.x4)**
    2 + (-0.95517234425623 + m.x5)**2 + (-0.4357037242101963 + m.x6)**2) +
    m.x514 * ((-0.11324062660745182 + m.x4)**2 + (-0.1127227477493824 + m.x5)**
    2 + (-0.6775531466862447 + m.x6)**2) + m.x515 * ((-0.37207880369117297 +
    m.x4)**2 + (-0.4429785978155648 + m.x5)**2 + (-0.6160286803397987 + m.x6)**
    2) + m.x516 * ((-0.2361959619384585 + m.x4)**2 + (-0.6356037312017463 +
    m.x5)**2 + (-0.5117112742751293 + m.x6)**2) + m.x517 * ((
    -0.4447865236645254 + m.x4)**2 + (-0.33736132166151467 + m.x5)**2 + (
    -0.5880068862255667 + m.x6)**2) + m.x518 * ((-0.1880644612037895 + m.x4)**2
    + (-0.8339460457426732 + m.x5)**2 + (-0.4642760100333919 + m.x6)**2) +
    m.x519 * ((-0.809678525848048 + m.x4)**2 + (-0.9810714270884835 + m.x5)**2
    + (-0.22329339192222197 + m.x6)**2) + m.x520 * ((-0.9103106601121644 +
    m.x4)**2 + (-0.7530889196828001 + m.x5)**2 + (-0.2687229232888456 + m.x6)**
    2) + m.x521 * ((-0.2506681687047203 + m.x4)**2 + (-0.14874655132318948 +
    m.x5)**2 + (-0.7961773337916473 + m.x6)**2) + m.x522 * ((
    -0.5877634400149608 + m.x4)**2 + (-0.7175654971518651 + m.x5)**2 + (
    -0.6356627690183453 + m.x6)**2) + m.x523 * ((-0.7974452543446829 + m.x4)**2
    + (-0.5323927624309212 + m.x5)**2 + (-0.9572021040304207 + m.x6)**2) +
    m.x524 * ((-0.5949737079161318 + m.x4)**2 + (-0.41675919028038244 + m.x5)**
    2 + (-0.25549007713931127 + m.x6)**2) + m.x525 * ((-0.05224072110626399 +
    m.x4)**2 + (-0.9684253307041065 + m.x5)**2 + (-0.03621367660020813 + m.x6)
    **2) + m.x526 * ((-0.9347003609994666 + m.x4)**2 + (-0.64358152389621 +
    m.x5)**2 + (-0.059814343789942215 + m.x6)**2) + m.x527 * ((
    -0.7935538449770041 + m.x4)**2 + (-0.11540895271984875 + m.x5)**2 + (
    -0.3946769068499303 + m.x6)**2) + m.x528 * ((-0.17385809015950826 + m.x4)**
    2 + (-0.45921932138562505 + m.x5)**2 + (-0.8256339099174179 + m.x6)**2) +
    m.x529 * ((-0.03835739793505788 + m.x4)**2 + (-0.6113872567578748 + m.x5)**
    2 + (-0.8718964927106821 + m.x6)**2) + m.x530 * ((-0.5739391076092649 +
    m.x4)**2 + (-0.5247196687429146 + m.x5)**2 + (-0.8533462318828052 + m.x6)**
    2) + m.x531 * ((-0.971075259349222 + m.x4)**2 + (-0.9104965674152667 + m.x5)
    **2 + (-0.7708929958995743 + m.x6)**2) + m.x532 * ((-0.5645353295297807 +
    m.x4)**2 + (-0.8584342772586054 + m.x5)**2 + (-0.8718267224700634 + m.x6)**
    2) + m.x533 * ((-0.6297483558228558 + m.x4)**2 + (-0.04014715139597247 +
    m.x5)**2 + (-0.09844847603361628 + m.x6)**2) + m.x534 * ((
    -0.5189119183247188 + m.x4)**2 + (-0.9474326272844581 + m.x5)**2 + (
    -0.5266109715772231 + m.x6)**2) + m.x535 * ((-0.6527900351730098 + m.x4)**2
    + (-0.11052190591595967 + m.x5)**2 + (-0.5191880622085426 + m.x6)**2) +
    m.x536 * ((-0.10854173782735999 + m.x4)**2 + (-0.42093142780593973 + m.x5)
    **2 + (-0.31276103054202575 + m.x6)**2) + m.x537 * ((-0.3561489249032288 +
    m.x4)**2 + (-0.8268627589482757 + m.x5)**2 + (-0.1956453729075287 + m.x6)**
    2) + m.x538 * ((-0.4670221520529523 + m.x4)**2 + (-0.8891113977897892 +
    m.x5)**2 + (-0.27241504986579945 + m.x6)**2) + m.x539 * ((
    -0.35771749803339015 + m.x4)**2 + (-0.6044481060569854 + m.x5)**2 + (
    -0.7643630258273018 + m.x6)**2) + m.x540 * ((-0.04418354837503591 + m.x4)**
    2 + (-0.3102075900230633 + m.x5)**2 + (-0.8330809639446761 + m.x6)**2) +
    m.x541 * ((-0.8743744462324157 + m.x4)**2 + (-0.845910325959314 + m.x5)**2
    + (-0.7140310051973626 + m.x6)**2) + m.x542 * ((-0.716502442685945 + m.x4)
    **2 + (-0.9515475221689099 + m.x5)**2 + (-0.6188065408222541 + m.x6)**2) +
    m.x543 * ((-0.06835345835265683 + m.x4)**2 + (-0.823370938809925 + m.x5)**2
    + (-0.3389455123551257 + m.x6)**2) + m.x544 * ((-0.7757415343504088 + m.x4)
    **2 + (-0.7958264649791436 + m.x5)**2 + (-0.625436707143751 + m.x6)**2) +
    m.x545 * ((-0.9142760468526993 + m.x4)**2 + (-0.970911085347618 + m.x5)**2
    + (-0.5429674014732869 + m.x6)**2) + m.x546 * ((-0.2096014409776199 + m.x4)
    **2 + (-0.9025289375492106 + m.x5)**2 + (-0.5287699855976883 + m.x6)**2) +
    m.x547 * ((-0.011619538885734193 + m.x4)**2 + (-0.12056474702179032 + m.x5)
    **2 + (-0.5981092250808783 + m.x6)**2) + m.x548 * ((-0.08114659947993563 +
    m.x4)**2 + (-0.441063194519585 + m.x5)**2 + (-0.9642109110625849 + m.x6)**2)
    + m.x549 * ((-0.3788010313673167 + m.x4)**2 + (-0.19367862019710247 + m.x5)
    **2 + (-0.7345907587139372 + m.x6)**2) + m.x550 * ((-0.02680831453838972 +
    m.x4)**2 + (-0.5010595635551833 + m.x5)**2 + (-0.5697272305278913 + m.x6)**
    2) + m.x551 * ((-0.9408661364624531 + m.x4)**2 + (-0.4084534281255007 +
    m.x5)**2 + (-0.5124759778704364 + m.x6)**2) + m.x552 * ((
    -0.7655175499270966 + m.x4)**2 + (-0.9482620910201023 + m.x5)**2 + (
    -0.27827134564381706 + m.x6)**2) + m.x553 * ((-0.8265432701686128 + m.x4)**
    2 + (-0.14848837551074712 + m.x5)**2 + (-0.20089309175503667 + m.x6)**2) +
    m.x554 * ((-0.8000481609994606 + m.x4)**2 + (-0.2539853139751347 + m.x5)**2
    + (-0.20829630707197233 + m.x6)**2) + m.x555 * ((-0.26855105737847407 +
    m.x4)**2 + (-0.44920136283845336 + m.x5)**2 + (-0.41629666515596175 + m.x6)
    **2) + m.x556 * ((-0.7182882087805578 + m.x4)**2 + (-0.3793592905729698 +
    m.x5)**2 + (-0.17883837272616077 + m.x6)**2) + m.x557 * ((
    -0.19581024445686512 + m.x4)**2 + (-0.27181382773049567 + m.x5)**2 + (
    -0.322427225040845 + m.x6)**2) + m.x558 * ((-0.38658358127338854 + m.x4)**2
    + (-0.7529124327703216 + m.x5)**2 + (-0.41910049255232174 + m.x6)**2) +
    m.x559 * ((-0.19143734810557733 + m.x4)**2 + (-0.48208401520816846 + m.x5)
    **2 + (-0.045061252030364485 + m.x6)**2) + m.x560 * ((-0.05682593455420182
    + m.x4)**2 + (-0.7233915176300436 + m.x5)**2 + (-0.705103104979348 + m.x6)
    **2) + m.x561 * ((-0.9042027840926966 + m.x4)**2 + (-0.6938960112447266 +
    m.x5)**2 + (-0.3354994737557092 + m.x6)**2) + m.x562 * ((
    -0.7894861443951544 + m.x4)**2 + (-0.15244186536727333 + m.x5)**2 + (
    -0.5005398248336654 + m.x6)**2) + m.x563 * ((-0.34446185593752554 + m.x4)**
    2 + (-0.6772836129498278 + m.x5)**2 + (-0.7336734830314701 + m.x6)**2) +
    m.x564 * ((-0.20741666474163767 + m.x4)**2 + (-0.8202921977271875 + m.x5)**
    2 + (-0.5506009695439275 + m.x6)**2) + m.x565 * ((-0.5402923097092933 +
    m.x4)**2 + (-0.2675342734369003 + m.x5)**2 + (-0.7992890751698145 + m.x6)**
    2) + m.x566 * ((-0.27967022339776526 + m.x4)**2 + (-0.7979911425034355 +
    m.x5)**2 + (-0.46452645725265274 + m.x6)**2) + m.x567 * ((
    -0.9595819947527509 + m.x4)**2 + (-0.5232034354155645 + m.x5)**2 + (
    -0.2389966098134152 + m.x6)**2) + m.x568 * ((-0.07608991534038712 + m.x4)**
    2 + (-0.5736418691521828 + m.x5)**2 + (-0.019986186505803083 + m.x6)**2) +
    m.x569 * ((-0.42700398197897205 + m.x4)**2 + (-0.8010918625105746 + m.x5)**
    2 + (-0.8805692849635621 + m.x6)**2) + m.x570 * ((-0.5579869928092586 +
    m.x4)**2 + (-0.389498674450649 + m.x5)**2 + (-0.0748048271612155 + m.x6)**2)
    + m.x571 * ((-0.4070102263571985 + m.x4)**2 + (-0.7554593095435335 + m.x5)
    **2 + (-0.5904356558483927 + m.x6)**2) + m.x572 * ((-0.1364891447316846 +
    m.x4)**2 + (-0.8468918307965907 + m.x5)**2 + (-0.28700620952460276 + m.x6)
    **2) + m.x573 * ((-0.3367232340241588 + m.x4)**2 + (-0.8929968819838374 +
    m.x5)**2 + (-0.7484026014198896 + m.x6)**2) + m.x574 * ((
    -0.7635235105485991 + m.x4)**2 + (-0.5708091732053739 + m.x5)**2 + (
    -0.6753411475376285 + m.x6)**2) + m.x575 * ((-0.3651268993409923 + m.x4)**2
    + (-0.12289882343337766 + m.x5)**2 + (-0.964009065158759 + m.x6)**2) +
    m.x576 * ((-0.8750166259121633 + m.x4)**2 + (-0.41383609996893045 + m.x5)**
    2 + (-0.29800741171032363 + m.x6)**2) + m.x577 * ((-0.40013800173743697 +
    m.x4)**2 + (-0.7249247652248746 + m.x5)**2 + (-0.6355874704603257 + m.x6)**
    2) + m.x578 * ((-0.18348856582977036 + m.x4)**2 + (-0.025854052500041358 +
    m.x5)**2 + (-0.2534534001576054 + m.x6)**2) + m.x579 * ((
    -0.9435154017754898 + m.x4)**2 + (-0.4392260710197824 + m.x5)**2 + (
    -0.4691516281413123 + m.x6)**2) + m.x580 * ((-0.7385168925807722 + m.x4)**2
    + (-0.24644193646352752 + m.x5)**2 + (-0.17061742663080026 + m.x6)**2) +
    m.x581 * ((-0.05605633605668536 + m.x4)**2 + (-0.4912081682781063 + m.x5)**
    2 + (-0.5699993572568407 + m.x6)**2) + m.x582 * ((-0.15757181258844644 +
    m.x4)**2 + (-0.7303751725186297 + m.x5)**2 + (-0.9121598657835175 + m.x6)**
    2) + m.x583 * ((-0.33215497925633675 + m.x4)**2 + (-0.17028080871532403 +
    m.x5)**2 + (-0.3930063113045501 + m.x6)**2) + m.x584 * ((
    -0.7786941002157438 + m.x4)**2 + (-0.7405380151215268 + m.x5)**2 + (
    -0.9154339959764618 + m.x6)**2) + m.x585 * ((-0.7508193852295587 + m.x4)**2
    + (-0.3803573428649786 + m.x5)**2 + (-0.22138614519182764 + m.x6)**2) +
    m.x586 * ((-0.9264682682309922 + m.x4)**2 + (-0.8873603073342023 + m.x5)**2
    + (-0.864950588785591 + m.x6)**2) + m.x587 * ((-0.908267042284869 + m.x4)
    **2 + (-0.10298312771159246 + m.x5)**2 + (-0.6124646113776369 + m.x6)**2)
    + m.x588 * ((-0.16426882492973371 + m.x4)**2 + (-0.9869331956455133 + m.x5)
    **2 + (-0.719818452386762 + m.x6)**2) + m.x589 * ((-0.8825086613164931 +
    m.x4)**2 + (-0.08300173420348822 + m.x5)**2 + (-0.44087052443558905 + m.x6)
    **2) + m.x590 * ((-0.5130371082699586 + m.x4)**2 + (-0.7805872451248177 +
    m.x5)**2 + (-0.914693570552897 + m.x6)**2) + m.x591 * ((
    -0.12650358912449233 + m.x4)**2 + (-0.5342711885242658 + m.x5)**2 + (
    -0.3859086811884249 + m.x6)**2) + m.x592 * ((-0.021894498188813283 + m.x4)
    **2 + (-0.0027246625913778244 + m.x5)**2 + (-0.626856809181304 + m.x6)**2)
    + m.x593 * ((-0.8441678193498758 + m.x4)**2 + (-0.3509107664369997 + m.x5)
    **2 + (-0.23930665191922518 + m.x6)**2) + m.x594 * ((-0.9191544458905686 +
    m.x4)**2 + (-0.9295699343849126 + m.x5)**2 + (-0.5569494475068902 + m.x6)**
    2) + m.x595 * ((-0.35271055808467555 + m.x4)**2 + (-0.14001703168123492 +
    m.x5)**2 + (-0.4307833453831681 + m.x6)**2) + m.x596 * ((
    -0.015927077871251027 + m.x4)**2 + (-0.7944117141411271 + m.x5)**2 + (
    -0.0663323600363589 + m.x6)**2) + m.x597 * ((-0.06700957837304222 + m.x4)**
    2 + (-0.7245424124926254 + m.x5)**2 + (-0.04136030199658791 + m.x6)**2) +
    m.x598 * ((-0.6435908765286936 + m.x4)**2 + (-0.5608885129918921 + m.x5)**2
    + (-0.29840288844009555 + m.x6)**2) + m.x599 * ((-0.0017744407035030774 +
    m.x4)**2 + (-0.5302888132806858 + m.x5)**2 + (-0.1070197893246232 + m.x6)**
    2) + m.x600 * ((-0.9960876588948411 + m.x4)**2 + (-0.5297980608672969 +
    m.x5)**2 + (-0.0967898406969584 + m.x6)**2) + m.x601 * ((
    -0.2966788147123718 + m.x4)**2 + (-0.4535896653892114 + m.x5)**2 + (
    -0.12490644679443152 + m.x6)**2) + m.x602 * ((-0.33141143322070366 + m.x4)
    **2 + (-0.28744907554291355 + m.x5)**2 + (-0.06994447154054817 + m.x6)**2)
    + m.x603 * ((-0.047933403792797424 + m.x4)**2 + (-0.8415471101830639 +
    m.x5)**2 + (-0.5955840833322725 + m.x6)**2) + m.x604 * ((
    -0.9171613034104257 + m.x4)**2 + (-0.6459943002822387 + m.x5)**2 + (
    -0.4152591826204478 + m.x6)**2) + m.x605 * ((-0.32790075407957764 + m.x4)**
    2 + (-0.4939517226351521 + m.x5)**2 + (-0.22989356871245614 + m.x6)**2) +
    m.x606 * ((-0.5844775505927844 + m.x4)**2 + (-0.7114551136263754 + m.x5)**2
    + (-0.2605304125555207 + m.x6)**2) + m.x607 * ((-0.5855724678597634 + m.x4)
    **2 + (-0.5384124176079916 + m.x5)**2 + (-0.22873430477860057 + m.x6)**2)
    + m.x608 * ((-0.27448502514988804 + m.x4)**2 + (-0.8811058000942367 + m.x5)
    **2 + (-0.1084432011985692 + m.x6)**2) + m.x609 * ((-0.8087191675490594 +
    m.x4)**2 + (-0.36365530737786633 + m.x5)**2 + (-0.2551582076272405 + m.x6)
    **2) + m.x610 * ((-0.4692805537583873 + m.x4)**2 + (-0.1094763815311296 +
    m.x5)**2 + (-0.03308747009705737 + m.x6)**2) + m.x611 * ((
    -0.1414596675245341 + m.x4)**2 + (-0.05264608531324155 + m.x5)**2 + (
    -0.16232407961452555 + m.x6)**2) + m.x612 * ((-0.09502702610585512 + m.x4)
    **2 + (-0.6088439913367978 + m.x5)**2 + (-0.5808332695355897 + m.x6)**2) +
    m.x613 * ((-0.03790513829711473 + m.x4)**2 + (-0.5080181668023536 + m.x5)**
    2 + (-0.6682482244944306 + m.x6)**2) + m.x614 * ((-0.2398098003882162 +
    m.x4)**2 + (-0.40854299334338917 + m.x5)**2 + (-0.6265561387473995 + m.x6)
    **2) + m.x615 * ((-0.41352866202283534 + m.x4)**2 + (-0.13735597150040624
    + m.x5)**2 + (-0.6575650750157317 + m.x6)**2) + m.x616 * ((
    -0.5918024287760949 + m.x4)**2 + (-0.9046254255858704 + m.x5)**2 + (
    -0.35259988628306405 + m.x6)**2) + m.x617 * ((-0.6163737698105297 + m.x4)**
    2 + (-0.7338484828210599 + m.x5)**2 + (-0.2552037957856732 + m.x6)**2) +
    m.x618 * ((-0.7481226352197995 + m.x4)**2 + (-0.6103864936538574 + m.x5)**2
    + (-0.29319537619297076 + m.x6)**2) + m.x619 * ((-0.3817477016118834 +
    m.x4)**2 + (-0.28367233078996257 + m.x5)**2 + (-0.9065136963715262 + m.x6)
    **2) + m.x620 * ((-0.5387913922968426 + m.x4)**2 + (-0.9587122385639283 +
    m.x5)**2 + (-0.2849034277289415 + m.x6)**2) + m.x621 * ((
    -0.016896910716011626 + m.x4)**2 + (-0.542247494752311 + m.x5)**2 + (
    -0.35702504416839875 + m.x6)**2) + m.x622 * ((-0.0400792611431785 + m.x4)**
    2 + (-0.06003526247003277 + m.x5)**2 + (-0.8531074258574137 + m.x6)**2) +
    m.x623 * ((-0.6026500310542549 + m.x4)**2 + (-0.6934852370637312 + m.x5)**2
    + (-0.3460238114357763 + m.x6)**2) + m.x624 * ((-0.55902762581076 + m.x4)
    **2 + (-0.9459788231528541 + m.x5)**2 + (-0.1290887862399902 + m.x6)**2) +
    m.x625 * ((-0.3837617695459321 + m.x4)**2 + (-0.3879093486846117 + m.x5)**2
    + (-0.8849022163547949 + m.x6)**2) + m.x626 * ((-0.7720525818822013 + m.x4)
    **2 + (-0.1111500101946098 + m.x5)**2 + (-0.7661918097646079 + m.x6)**2) +
    m.x627 * ((-0.6344378078488477 + m.x4)**2 + (-0.38920253281074113 + m.x5)**
    2 + (-0.2569532307428819 + m.x6)**2) + m.x628 * ((-0.8429682238542169 +
    m.x4)**2 + (-0.28809038931293773 + m.x5)**2 + (-0.19175063574452433 + m.x6)
    **2) + m.x629 * ((-0.2672995256303895 + m.x4)**2 + (-0.03242383874322041 +
    m.x5)**2 + (-0.9842571124991794 + m.x6)**2) + m.x630 * ((
    -0.06540387850476659 + m.x4)**2 + (-0.24128518865484905 + m.x5)**2 + (
    -0.20517012144871016 + m.x6)**2) + m.x631 * ((-0.18621511189629547 + m.x4)
    **2 + (-0.30267745952007064 + m.x5)**2 + (-0.7114604662427862 + m.x6)**2)
    + m.x632 * ((-0.7893034114918972 + m.x4)**2 + (-0.0955677714501183 + m.x5)
    **2 + (-0.5821952996736662 + m.x6)**2) + m.x633 * ((-0.20739251640515832 +
    m.x4)**2 + (-0.8432910091332453 + m.x5)**2 + (-0.2586107102872377 + m.x6)**
    2) + m.x634 * ((-0.5530346239832239 + m.x4)**2 + (-0.37827958857876165 +
    m.x5)**2 + (-0.7781403692754599 + m.x6)**2) + m.x635 * ((
    -0.28092860002809394 + m.x4)**2 + (-0.8298897623230604 + m.x5)**2 + (
    -0.2719103553554957 + m.x6)**2) + m.x636 * ((-0.014925126786705656 + m.x4)
    **2 + (-0.12777278988662366 + m.x5)**2 + (-0.10588450075658606 + m.x6)**2)
    + m.x637 * ((-0.11668619210388753 + m.x4)**2 + (-0.3820666367049661 + m.x5)
    **2 + (-0.7791195974948653 + m.x6)**2) + m.x638 * ((-0.4344431981739817 +
    m.x4)**2 + (-0.1080485799315768 + m.x5)**2 + (-0.08340127233732786 + m.x6)
    **2) + m.x639 * ((-0.1793620960414819 + m.x4)**2 + (-0.3419484974871717 +
    m.x5)**2 + (-0.7820789010033935 + m.x6)**2) + m.x640 * ((
    -0.7165429642851615 + m.x4)**2 + (-0.9026914605710601 + m.x5)**2 + (
    -0.6935163617983727 + m.x6)**2) + m.x641 * ((-0.30965035870898905 + m.x4)**
    2 + (-0.6763312865753088 + m.x5)**2 + (-0.10472903251267174 + m.x6)**2) +
    m.x642 * ((-0.10216516132313902 + m.x4)**2 + (-0.5490230377748015 + m.x5)**
    2 + (-0.7352888807492108 + m.x6)**2) + m.x643 * ((-0.8651135909998409 +
    m.x4)**2 + (-0.29254598308074753 + m.x5)**2 + (-0.11864176567670415 + m.x6)
    **2) + m.x644 * ((-0.2101013503923751 + m.x4)**2 + (-0.8522411631472961 +
    m.x5)**2 + (-0.7212132885792959 + m.x6)**2) + m.x645 * ((
    -0.11131146834606975 + m.x4)**2 + (-0.09341511900076704 + m.x5)**2 + (
    -0.22436226860606978 + m.x6)**2) + m.x646 * ((-0.09589381898256144 + m.x4)
    **2 + (-0.62983098343096 + m.x5)**2 + (-0.236862989417864 + m.x6)**2) +
    m.x647 * ((-0.17134746819256785 + m.x4)**2 + (-0.0022191294485545132 + m.x5)
    **2 + (-0.5719632904418379 + m.x6)**2) + m.x648 * ((-0.1437717819667449 +
    m.x4)**2 + (-0.693066215236063 + m.x5)**2 + (-0.47910832437053097 + m.x6)**
    2) + m.x649 * ((-0.21326957505198796 + m.x4)**2 + (-0.5389938925764525 +
    m.x5)**2 + (-0.8985814053123515 + m.x6)**2) + m.x650 * ((
    -0.5267034399227511 + m.x4)**2 + (-0.16272083595464992 + m.x5)**2 + (
    -0.4424485927629499 + m.x6)**2) + m.x651 * ((-0.010171844468493396 + m.x4)
    **2 + (-0.8225385611520942 + m.x5)**2 + (-0.850081594460415 + m.x6)**2) +
    m.x652 * ((-0.9099126006489431 + m.x4)**2 + (-0.7117592498159224 + m.x5)**2
    + (-0.24535211640166132 + m.x6)**2) + m.x653 * ((-0.8933095434728399 +
    m.x4)**2 + (-0.18696555428084993 + m.x5)**2 + (-0.14126880443170386 + m.x6)
    **2) + m.x654 * ((-0.05060465423810745 + m.x4)**2 + (-0.35889935243868054
    + m.x5)**2 + (-0.9898462690273427 + m.x6)**2) + m.x655 * ((
    -0.28435588276815815 + m.x4)**2 + (-0.144413444054048 + m.x5)**2 + (
    -0.4912506689862507 + m.x6)**2) + m.x656 * ((-0.02377989350983456 + m.x4)**
    2 + (-0.4850739766720621 + m.x5)**2 + (-0.014220358160159874 + m.x6)**2) +
    m.x657 * ((-0.10685228340662356 + m.x4)**2 + (-0.4306857431033353 + m.x5)**
    2 + (-0.899717945016438 + m.x6)**2) + m.x658 * ((-0.7958123415938076 + m.x4)
    **2 + (-0.1567416212397551 + m.x5)**2 + (-0.4381463784299796 + m.x6)**2) +
    m.x659 * ((-0.20239323873555803 + m.x4)**2 + (-0.6688370928332699 + m.x5)**
    2 + (-0.8908782840570669 + m.x6)**2) + m.x660 * ((-0.8162377020493878 +
    m.x4)**2 + (-0.5538462537896983 + m.x5)**2 + (-0.46332413492756175 + m.x6)
    **2) + m.x661 * ((-0.3285436588025977 + m.x4)**2 + (-0.18234363029763911 +
    m.x5)**2 + (-0.9652199890334622 + m.x6)**2) + m.x662 * ((
    -0.1833756016631104 + m.x4)**2 + (-0.6191845385278278 + m.x5)**2 + (
    -0.3823840339936617 + m.x6)**2) + m.x663 * ((-0.9451306347207963 + m.x4)**2
    + (-0.05696563611612815 + m.x5)**2 + (-0.31872989911510674 + m.x6)**2) +
    m.x664 * ((-0.1876172330243875 + m.x4)**2 + (-0.21273318417844989 + m.x5)**
    2 + (-0.7951342088420695 + m.x6)**2) + m.x665 * ((-0.6813385906412783 +
    m.x4)**2 + (-0.7795130804133624 + m.x5)**2 + (-0.8121251523108964 + m.x6)**
    2) + m.x666 * ((-0.5476385802163356 + m.x4)**2 + (-0.47082012503804105 +
    m.x5)**2 + (-0.1875779928301533 + m.x6)**2) + m.x667 * ((
    -0.4418603491118567 + m.x4)**2 + (-0.47814259051556174 + m.x5)**2 + (
    -0.843868091243698 + m.x6)**2) + m.x668 * ((-0.7227490532707296 + m.x4)**2
    + (-0.6305946284321624 + m.x5)**2 + (-0.7778431141977471 + m.x6)**2) +
    m.x669 * ((-0.44449821578332316 + m.x4)**2 + (-0.7010434784223998 + m.x5)**
    2 + (-0.4562440307525807 + m.x6)**2) + m.x670 * ((-0.8207794357127131 +
    m.x4)**2 + (-0.2715928586111269 + m.x5)**2 + (-0.8111077485955768 + m.x6)**
    2) + m.x671 * ((-0.06913168314217966 + m.x4)**2 + (-0.17062534115061545 +
    m.x5)**2 + (-0.7186204035119522 + m.x6)**2) + m.x672 * ((
    -0.9356572299847938 + m.x4)**2 + (-0.25247506111569284 + m.x5)**2 + (
    -0.3766500744907605 + m.x6)**2) + m.x673 * ((-0.053183850751484685 + m.x4)
    **2 + (-0.503319761819413 + m.x5)**2 + (-0.3988792529665396 + m.x6)**2) +
    m.x674 * ((-0.6348345247106641 + m.x4)**2 + (-0.7372264972225206 + m.x5)**2
    + (-0.2816805911685105 + m.x6)**2) + m.x675 * ((-0.4922332187206825 + m.x4)
    **2 + (-0.12955383972526402 + m.x5)**2 + (-0.6759110290426272 + m.x6)**2)
    + m.x676 * ((-0.3039899015675839 + m.x4)**2 + (-0.8701136133070226 + m.x5)
    **2 + (-0.3415605267108113 + m.x6)**2) + m.x677 * ((-0.19249833111625447 +
    m.x4)**2 + (-0.289199436536963 + m.x5)**2 + (-0.17001661008163982 + m.x6)**
    2) + m.x678 * ((-0.41498929870378265 + m.x4)**2 + (-0.6714872892529845 +
    m.x5)**2 + (-0.7734373760087199 + m.x6)**2) + m.x679 * ((
    -0.6414826763544017 + m.x4)**2 + (-0.833907205124963 + m.x5)**2 + (
    -0.5454186218286011 + m.x6)**2) + m.x680 * ((-0.8018985643443416 + m.x4)**2
    + (-0.18267498327347076 + m.x5)**2 + (-0.6248398639397298 + m.x6)**2) +
    m.x681 * ((-0.011710686297021211 + m.x4)**2 + (-0.7293978925979899 + m.x5)
    **2 + (-0.062110132255305706 + m.x6)**2) + m.x682 * ((-0.3522173993348232
    + m.x4)**2 + (-0.07284835414901125 + m.x5)**2 + (-0.6849529919886285 +
    m.x6)**2) + m.x683 * ((-0.12185440522884461 + m.x4)**2 + (
    -0.6687199057889921 + m.x5)**2 + (-0.13946873559425443 + m.x6)**2) + m.x684
    * ((-0.8925626716041768 + m.x4)**2 + (-0.5507535962948702 + m.x5)**2 + (
    -0.7754292445803886 + m.x6)**2) + m.x685 * ((-0.6737722608457104 + m.x4)**2
    + (-0.6835956974473757 + m.x5)**2 + (-0.11220963763590197 + m.x6)**2) +
    m.x686 * ((-0.2056780683513766 + m.x4)**2 + (-0.7777969577351744 + m.x5)**2
    + (-0.7818523629215165 + m.x6)**2) + m.x687 * ((-0.35040653667397936 +
    m.x4)**2 + (-0.7218237888483313 + m.x5)**2 + (-0.24223482432840604 + m.x6)
    **2) + m.x688 * ((-0.045519582549019444 + m.x4)**2 + (-0.2468399938697886
    + m.x5)**2 + (-0.5509847497355672 + m.x6)**2) + m.x689 * ((
    -0.7625095428789862 + m.x4)**2 + (-0.38693097091538686 + m.x5)**2 + (
    -0.8447744154325253 + m.x6)**2) + m.x690 * ((-0.47706955962867537 + m.x4)**
    2 + (-0.9048825326627299 + m.x5)**2 + (-0.6698420394228831 + m.x6)**2) +
    m.x691 * ((-0.9220722254195256 + m.x4)**2 + (-0.9093919260950618 + m.x5)**2
    + (-0.3585536965409931 + m.x6)**2) + m.x692 * ((-0.42421741345016817 +
    m.x4)**2 + (-0.1810097690077137 + m.x5)**2 + (-0.11838106532964576 + m.x6)
    **2) + m.x693 * ((-0.7909025678257156 + m.x4)**2 + (-0.6683526078945575 +
    m.x5)**2 + (-0.5109886309751906 + m.x6)**2) + m.x694 * ((
    -0.28703506025246406 + m.x4)**2 + (-0.6439491320749008 + m.x5)**2 + (
    -0.7706022456077256 + m.x6)**2) + m.x695 * ((-0.13459246208619924 + m.x4)**
    2 + (-0.28097209258600253 + m.x5)**2 + (-0.10489080047801336 + m.x6)**2) +
    m.x696 * ((-0.3523855983171982 + m.x4)**2 + (-0.4248157381430815 + m.x5)**2
    + (-0.6906133929926649 + m.x6)**2) + m.x697 * ((-0.1583698558934198 + m.x4)
    **2 + (-0.9210909019600683 + m.x5)**2 + (-0.6395026018640236 + m.x6)**2) +
    m.x698 * ((-0.7869061505221948 + m.x4)**2 + (-0.7078900011730935 + m.x5)**2
    + (-0.6196010572637488 + m.x6)**2) + m.x699 * ((-0.5687640083646678 + m.x4)
    **2 + (-0.5772192111740503 + m.x5)**2 + (-0.6138822482643156 + m.x6)**2) +
    m.x700 * ((-0.7139842499777261 + m.x4)**2 + (-0.11680023910927528 + m.x5)**
    2 + (-0.2506224434653087 + m.x6)**2) + m.x701 * ((-0.805568392008547 + m.x4)
    **2 + (-0.06545005124609204 + m.x5)**2 + (-0.032700612578027144 + m.x6)**2)
    + m.x702 * ((-0.8672418514729174 + m.x4)**2 + (-0.9495334316535684 + m.x5)
    **2 + (-0.9506671434655545 + m.x6)**2) + m.x703 * ((-0.8428186951044521 +
    m.x4)**2 + (-0.2491784563178132 + m.x5)**2 + (-0.8574700961978342 + m.x6)**
    2) + m.x704 * ((-0.3871201049109313 + m.x4)**2 + (-0.9738876810785931 +
    m.x5)**2 + (-0.613114261845513 + m.x6)**2) + m.x705 * ((-0.9150831066517291
    + m.x4)**2 + (-0.8126407462368724 + m.x5)**2 + (-0.32527791429850705 +
    m.x6)**2) + m.x706 * ((-0.13884237948432931 + m.x4)**2 + (
    -0.05350519336412973 + m.x5)**2 + (-0.24780684370452688 + m.x6)**2) +
    m.x707 * ((-0.7923572326382577 + m.x4)**2 + (-0.16987369545737896 + m.x5)**
    2 + (-0.9459861441672113 + m.x6)**2) + m.x708 * ((-0.8287350086957515 +
    m.x4)**2 + (-0.2701283953407778 + m.x5)**2 + (-0.38893185458031276 + m.x6)
    **2) + m.x709 * ((-0.8419989467911838 + m.x4)**2 + (-0.36305399780969094 +
    m.x5)**2 + (-0.5097745885449746 + m.x6)**2) + m.x710 * ((
    -0.9328252563464429 + m.x4)**2 + (-0.6938288661186377 + m.x5)**2 + (
    -0.5178576561761775 + m.x6)**2) + m.x711 * ((-0.13394390692618663 + m.x4)**
    2 + (-0.1707402476262171 + m.x5)**2 + (-0.049978421880908175 + m.x6)**2) +
    m.x712 * ((-0.9344145063124553 + m.x4)**2 + (-0.5642986722348461 + m.x5)**2
    + (-0.9742283497162917 + m.x6)**2) + m.x713 * ((-0.12917904997198593 +
    m.x4)**2 + (-0.8291714054039813 + m.x5)**2 + (-0.1461208778099089 + m.x6)**
    2) + m.x714 * ((-0.49297041535442676 + m.x4)**2 + (-0.9997056001066135 +
    m.x5)**2 + (-0.9984805276449421 + m.x6)**2) + m.x715 * ((
    -0.9443406401848632 + m.x4)**2 + (-0.9556643724533576 + m.x5)**2 + (
    -0.7626439658137829 + m.x6)**2) + m.x716 * ((-0.4927277418379675 + m.x4)**2
    + (-0.24978712865953823 + m.x5)**2 + (-0.33279356513981784 + m.x6)**2) +
    m.x717 * ((-0.6628894265876931 + m.x4)**2 + (-0.08815384447750985 + m.x5)**
    2 + (-0.02837052028209286 + m.x6)**2) + m.x718 * ((-0.5951215974793173 +
    m.x4)**2 + (-0.6709917301275213 + m.x5)**2 + (-0.5228016909019687 + m.x6)**
    2) + m.x719 * ((-0.3628434072386518 + m.x4)**2 + (-0.5648955285747782 +
    m.x5)**2 + (-0.14037475292742752 + m.x6)**2) + m.x720 * ((
    -0.6315358621764737 + m.x4)**2 + (-0.4940040944835772 + m.x5)**2 + (
    -0.39393981108383724 + m.x6)**2) + m.x721 * ((-0.23895764723651125 + m.x4)
    **2 + (-0.4925466699958012 + m.x5)**2 + (-0.6798787131541073 + m.x6)**2) +
    m.x722 * ((-0.33431465619738565 + m.x4)**2 + (-0.02990879062461249 + m.x5)
    **2 + (-0.98627846080786 + m.x6)**2) + m.x723 * ((-0.20138845604638655 +
    m.x4)**2 + (-0.07286113290687579 + m.x5)**2 + (-0.7389461293858135 + m.x6)
    **2) + m.x724 * ((-0.22043310505100588 + m.x4)**2 + (-0.6921624888940164 +
    m.x5)**2 + (-0.7390910692714129 + m.x6)**2) + m.x725 * ((
    -0.1794768509914445 + m.x4)**2 + (-0.19971018619617786 + m.x5)**2 + (
    -0.1252179745377201 + m.x6)**2) + m.x726 * ((-0.4316525971751499 + m.x4)**2
    + (-0.9293948927573288 + m.x5)**2 + (-0.6357217625876419 + m.x6)**2) +
    m.x727 * ((-0.19054858574619327 + m.x4)**2 + (-0.6597186703227657 + m.x5)**
    2 + (-0.7437070343450088 + m.x6)**2) + m.x728 * ((-0.5401665990210613 +
    m.x4)**2 + (-0.31975882224981744 + m.x5)**2 + (-0.7676783575559698 + m.x6)
    **2) + m.x729 * ((-0.7141585569819535 + m.x4)**2 + (-0.5821205832955013 +
    m.x5)**2 + (-0.9414136448749184 + m.x6)**2) + m.x730 * ((
    -0.44737341471901404 + m.x4)**2 + (-0.9048222764719899 + m.x5)**2 + (
    -0.7461921038282987 + m.x6)**2) + m.x731 * ((-0.6074944823231694 + m.x4)**2
    + (-0.4144292990749079 + m.x5)**2 + (-0.9448146796490002 + m.x6)**2) +
    m.x732 * ((-0.7711535942806756 + m.x4)**2 + (-0.18386931660223416 + m.x5)**
    2 + (-0.9382198399195494 + m.x6)**2) + m.x733 * ((-0.6654811389399782 +
    m.x4)**2 + (-0.7664480958655735 + m.x5)**2 + (-0.8043855734520027 + m.x6)**
    2) + m.x734 * ((-0.13574356640083862 + m.x4)**2 + (-0.8006073394818852 +
    m.x5)**2 + (-0.4293460234558568 + m.x6)**2) + m.x735 * ((-0.88109422081292
    + m.x4)**2 + (-0.2521523305664952 + m.x5)**2 + (-0.2783612988957984 + m.x6)
    **2) + m.x736 * ((-0.21098683574670196 + m.x4)**2 + (-0.5793487573072326 +
    m.x5)**2 + (-0.1400427387047346 + m.x6)**2) + m.x737 * ((
    -0.5287988551538474 + m.x4)**2 + (-0.9641191628237653 + m.x5)**2 + (
    -0.9601811389639257 + m.x6)**2) + m.x738 * ((-0.6356835687091966 + m.x4)**2
    + (-0.5035384241376479 + m.x5)**2 + (-0.912561201496254 + m.x6)**2) +
    m.x739 * ((-0.07022860689714527 + m.x4)**2 + (-0.7272172999901972 + m.x5)**
    2 + (-0.813209953545937 + m.x6)**2) + m.x740 * ((-0.8817216558635385 + m.x4)
    **2 + (-0.1961060970257913 + m.x5)**2 + (-0.4807253834719928 + m.x6)**2) +
    m.x741 * ((-0.8346893143895587 + m.x4)**2 + (-0.45391356191841836 + m.x5)**
    2 + (-0.03689848229389647 + m.x6)**2) + m.x742 * ((-0.4425064296341201 +
    m.x4)**2 + (-0.23133455702646433 + m.x5)**2 + (-0.4119733748205944 + m.x6)
    **2) + m.x743 * ((-0.48695930579230606 + m.x4)**2 + (-0.7723781894795173 +
    m.x5)**2 + (-0.7896048032875119 + m.x6)**2) + m.x744 * ((
    -0.6213072525945529 + m.x4)**2 + (-0.7463861427401226 + m.x5)**2 + (
    -0.19336124087532391 + m.x6)**2) + m.x745 * ((-0.9407434249412069 + m.x4)**
    2 + (-0.3157287888226875 + m.x5)**2 + (-0.19110493027237785 + m.x6)**2) +
    m.x746 * ((-0.5838103888478602 + m.x4)**2 + (-0.21478748867734254 + m.x5)**
    2 + (-0.8827349895451565 + m.x6)**2) + m.x747 * ((-0.03393239301609985 +
    m.x4)**2 + (-0.34669040395859996 + m.x5)**2 + (-0.6798250093428466 + m.x6)
    **2) + m.x748 * ((-0.9597035244408724 + m.x4)**2 + (-0.32286881217800434 +
    m.x5)**2 + (-0.4444196733141058 + m.x6)**2) + m.x749 * ((
    -0.9457000140765058 + m.x4)**2 + (-0.5068775796046029 + m.x5)**2 + (
    -0.3144273334897483 + m.x6)**2) + m.x750 * ((-0.044943238020383025 + m.x4)
    **2 + (-0.6614992336502294 + m.x5)**2 + (-0.8388656671250995 + m.x6)**2) +
    m.x751 * ((-0.49927342074497827 + m.x4)**2 + (-0.13468517272379243 + m.x5)
    **2 + (-0.4296515446930951 + m.x6)**2) + m.x752 * ((-0.9841852779169674 +
    m.x4)**2 + (-0.9843149988050245 + m.x5)**2 + (-0.47713010572283376 + m.x6)
    **2) + m.x753 * ((-0.4009300133770608 + m.x4)**2 + (-0.0042534179821622775
    + m.x5)**2 + (-0.4175816329130312 + m.x6)**2) + m.x754 * ((
    -0.4885283879651544 + m.x4)**2 + (-0.9079239735865996 + m.x5)**2 + (
    -0.21031335265116158 + m.x6)**2) + m.x755 * ((-0.9849314196407067 + m.x4)**
    2 + (-0.11685357326709411 + m.x5)**2 + (-0.017369390966105014 + m.x6)**2)
    + m.x756 * ((-0.35446426043635526 + m.x4)**2 + (-0.2596023514638419 + m.x5)
    **2 + (-0.32096060367647117 + m.x6)**2) + m.x757 * ((-0.4352313328405867 +
    m.x4)**2 + (-0.6746955457244538 + m.x5)**2 + (-0.25563185786498377 + m.x6)
    **2) + m.x758 * ((-0.699315061557881 + m.x4)**2 + (-0.5915408096298286 +
    m.x5)**2 + (-0.44607763336915063 + m.x6)**2) + m.x759 * ((
    -0.6592318565406342 + m.x4)**2 + (-0.6133226566520651 + m.x5)**2 + (
    -0.5961918051667695 + m.x6)**2) + m.x760 * ((-0.2354774655941887 + m.x4)**2
    + (-0.26243234628674394 + m.x5)**2 + (-0.312388269065189 + m.x6)**2) +
    m.x761 * ((-0.2200373888643452 + m.x4)**2 + (-0.41332951956449515 + m.x5)**
    2 + (-0.9109131978387711 + m.x6)**2) + m.x762 * ((-0.9487139910966843 +
    m.x4)**2 + (-0.5437246273285123 + m.x5)**2 + (-0.07874373064662499 + m.x6)
    **2) + m.x763 * ((-0.5964830453719224 + m.x4)**2 + (-0.0619742726091832 +
    m.x5)**2 + (-0.19927236817826444 + m.x6)**2) + m.x764 * ((
    -0.02759692117192214 + m.x4)**2 + (-0.2966943519059587 + m.x5)**2 + (
    -0.1436425270697561 + m.x6)**2) + m.x765 * ((-0.5605238341170351 + m.x4)**2
    + (-0.16705196889000828 + m.x5)**2 + (-0.4596742351263795 + m.x6)**2) +
    m.x766 * ((-0.9861110555193163 + m.x4)**2 + (-0.8752990513886425 + m.x5)**2
    + (-0.485142331599836 + m.x6)**2) + m.x767 * ((-0.27161250758957267 + m.x4)
    **2 + (-0.9946863069500006 + m.x5)**2 + (-0.439561525186691 + m.x6)**2) +
    m.x768 * ((-0.4836297090054381 + m.x4)**2 + (-0.2114798303676434 + m.x5)**2
    + (-0.1278618145726882 + m.x6)**2) + m.x769 * ((-0.024736008778174612 +
    m.x4)**2 + (-0.9205199923700449 + m.x5)**2 + (-0.8484339940268846 + m.x6)**
    2) + m.x770 * ((-0.5626615620602874 + m.x4)**2 + (-0.034989370194508096 +
    m.x5)**2 + (-0.6632186742091526 + m.x6)**2) + m.x771 * ((
    -0.6438064560050359 + m.x4)**2 + (-0.4889465681575601 + m.x5)**2 + (
    -0.26934659936523253 + m.x6)**2) + m.x772 * ((-0.5261992201164788 + m.x4)**
    2 + (-0.08595932986749422 + m.x5)**2 + (-0.08488216145362637 + m.x6)**2) +
    m.x773 * ((-0.1409322982901524 + m.x4)**2 + (-0.11290088677205301 + m.x5)**
    2 + (-0.1848610267768337 + m.x6)**2) + m.x774 * ((-0.9062469407729168 +
    m.x4)**2 + (-0.443642723519166 + m.x5)**2 + (-0.16301234345822146 + m.x6)**
    2) + m.x775 * ((-0.26280187243977027 + m.x4)**2 + (-0.5791906957767239 +
    m.x5)**2 + (-0.09189211557137555 + m.x6)**2) + m.x776 * ((
    -0.7819362020918313 + m.x4)**2 + (-0.8107913530336736 + m.x5)**2 + (
    -0.08589261011414395 + m.x6)**2) + m.x777 * ((-0.12202077612002771 + m.x4)
    **2 + (-0.09381851826448306 + m.x5)**2 + (-0.9946687189369333 + m.x6)**2)
    + m.x778 * ((-0.7449921585503891 + m.x4)**2 + (-0.44616399084793734 + m.x5)
    **2 + (-0.14733396356242667 + m.x6)**2) + m.x779 * ((-0.8013267039644335 +
    m.x4)**2 + (-0.12726406694941528 + m.x5)**2 + (-0.30755184402270597 + m.x6)
    **2) + m.x780 * ((-0.7129868679977376 + m.x4)**2 + (-0.5624403504682522 +
    m.x5)**2 + (-0.5194087287496278 + m.x6)**2) + m.x781 * ((-0.702605402074762
    + m.x4)**2 + (-0.696542187378441 + m.x5)**2 + (-0.9050186102050559 + m.x6)
    **2) + m.x782 * ((-0.48579654846686027 + m.x4)**2 + (-0.9865716657785814 +
    m.x5)**2 + (-0.7488638018945105 + m.x6)**2) + m.x783 * ((
    -0.14273183621265262 + m.x4)**2 + (-0.16961426380712896 + m.x5)**2 + (
    -0.7336118920897162 + m.x6)**2) + m.x784 * ((-0.508565000330308 + m.x4)**2
    + (-0.0008598073433415676 + m.x5)**2 + (-0.4878861682744219 + m.x6)**2) +
    m.x785 * ((-0.37778026211733495 + m.x4)**2 + (-0.7302042173061916 + m.x5)**
    2 + (-0.658072993274222 + m.x6)**2) + m.x786 * ((-0.5859039531200585 + m.x4)
    **2 + (-0.28185196746339947 + m.x5)**2 + (-0.07351170392618223 + m.x6)**2)
    + m.x787 * ((-0.437816105636769 + m.x4)**2 + (-0.9381650700676218 + m.x5)
    **2 + (-0.7532133630650687 + m.x6)**2) + m.x788 * ((-0.9111142352615409 +
    m.x4)**2 + (-0.9188611987954707 + m.x5)**2 + (-0.7097765364993713 + m.x6)**
    2) + m.x789 * ((-0.6070364816449836 + m.x4)**2 + (-0.6368688399261839 +
    m.x5)**2 + (-0.8097201734033257 + m.x6)**2) + m.x790 * ((
    -0.6984482644711556 + m.x4)**2 + (-0.8822045583167333 + m.x5)**2 + (
    -0.5762293092462573 + m.x6)**2) + m.x791 * ((-0.05085683485354919 + m.x4)**
    2 + (-0.9999183826637328 + m.x5)**2 + (-0.4287782578354542 + m.x6)**2) +
    m.x792 * ((-0.7615905094162454 + m.x4)**2 + (-0.1421067735442294 + m.x5)**2
    + (-0.5006086214169991 + m.x6)**2) + m.x793 * ((-0.9305602823426583 + m.x4)
    **2 + (-0.9752940115114439 + m.x5)**2 + (-0.1631253855890934 + m.x6)**2) +
    m.x794 * ((-0.26027159077598117 + m.x4)**2 + (-0.8467561936966935 + m.x5)**
    2 + (-0.42577439882602497 + m.x6)**2) + m.x795 * ((-0.08104856848069275 +
    m.x4)**2 + (-0.9886967089077169 + m.x5)**2 + (-0.08146796574801807 + m.x6)
    **2) + m.x796 * ((-0.48005659566609715 + m.x4)**2 + (-0.9974410345330987 +
    m.x5)**2 + (-0.48571859403846973 + m.x6)**2) + m.x797 * ((
    -0.4706070697040865 + m.x4)**2 + (-0.22633844473105058 + m.x5)**2 + (
    -0.8430722417451099 + m.x6)**2) + m.x798 * ((-0.6581283586576836 + m.x4)**2
    + (-0.2988361857206986 + m.x5)**2 + (-0.5248717962910134 + m.x6)**2) +
    m.x799 * ((-0.4139397565643148 + m.x4)**2 + (-0.7947219857264776 + m.x5)**2
    + (-0.9714023432927014 + m.x6)**2) + m.x800 * ((-0.29895041273047895 +
    m.x4)**2 + (-0.20934319073619012 + m.x5)**2 + (-0.12799433802173388 + m.x6)
    **2) + m.x801 * ((-0.7416051505394204 + m.x4)**2 + (-0.8610181415202831 +
    m.x5)**2 + (-0.8203512359906585 + m.x6)**2) + m.x802 * ((
    -0.8539442696762753 + m.x4)**2 + (-0.6440119856376406 + m.x5)**2 + (
    -0.04768006379778733 + m.x6)**2) + m.x803 * ((-0.8078856580669804 + m.x4)**
    2 + (-0.0811738770099133 + m.x5)**2 + (-0.42296333968011834 + m.x6)**2) +
    m.x804 * ((-0.11293172487506897 + m.x4)**2 + (-0.10190845514217972 + m.x5)
    **2 + (-0.025155476939746846 + m.x6)**2) + m.x805 * ((-0.6774554514175933
    + m.x4)**2 + (-0.28953130741751354 + m.x5)**2 + (-0.7231890256224531 +
    m.x6)**2) + m.x806 * ((-0.9658389665612165 + m.x4)**2 + (
    -0.8012920581552374 + m.x5)**2 + (-0.6871461962217258 + m.x6)**2) + m.x807
    * ((-0.5345563351474161 + m.x4)**2 + (-0.11378244706430707 + m.x5)**2 + (
    -0.7915828478976272 + m.x6)**2) + m.x808 * ((-0.9997767651100092 + m.x4)**2
    + (-0.5574720960939473 + m.x5)**2 + (-0.7410926285969115 + m.x6)**2) +
    m.x809 * ((-0.29777709756222204 + m.x4)**2 + (-0.13420768997570653 + m.x5)
    **2 + (-0.41098786274229304 + m.x6)**2) + m.x810 * ((-0.4890881424574446 +
    m.x4)**2 + (-0.404669840371118 + m.x5)**2 + (-0.6839329573384761 + m.x6)**2)
    + m.x811 * ((-0.9275207698350674 + m.x4)**2 + (-0.6349688118385305 + m.x5)
    **2 + (-0.16211201636277606 + m.x6)**2) + m.x812 * ((-0.31185430455711194
    + m.x4)**2 + (-0.9609480087595885 + m.x5)**2 + (-0.48506492880423546 +
    m.x6)**2) + m.x813 * ((-0.7594140721620825 + m.x4)**2 + (
    -0.9263148514595829 + m.x5)**2 + (-0.8648033086118 + m.x6)**2) + m.x814 * (
    (-0.6479304574703105 + m.x4)**2 + (-0.8228423329287321 + m.x5)**2 + (
    -0.7551761939784829 + m.x6)**2) + m.x815 * ((-0.8231579504797958 + m.x4)**2
    + (-0.05635445777892223 + m.x5)**2 + (-0.02468508246924883 + m.x6)**2) +
    m.x816 * ((-0.5969304027180449 + m.x4)**2 + (-0.8273519061055513 + m.x5)**2
    + (-0.8975627019214554 + m.x6)**2) + m.x817 * ((-0.47032986801594845 +
    m.x4)**2 + (-0.03758087479779437 + m.x5)**2 + (-0.956428581402661 + m.x6)**
    2) + m.x818 * ((-0.058484373437283965 + m.x4)**2 + (-0.7224332485058074 +
    m.x5)**2 + (-0.36656511074725406 + m.x6)**2) + m.x819 * ((
    -0.8067441195220981 + m.x4)**2 + (-0.6939130038104055 + m.x5)**2 + (
    -0.6650852436958627 + m.x6)**2) + m.x820 * ((-0.14316346421133996 + m.x4)**
    2 + (-0.8833335241651658 + m.x5)**2 + (-0.33873721710142757 + m.x6)**2) +
    m.x821 * ((-0.16663405286282917 + m.x4)**2 + (-0.1361097149511954 + m.x5)**
    2 + (-0.4167589692247934 + m.x6)**2) + m.x822 * ((-0.3533518801743728 +
    m.x4)**2 + (-0.7864769418639855 + m.x5)**2 + (-0.5700369360657614 + m.x6)**
    2) + m.x823 * ((-0.9940450532017178 + m.x4)**2 + (-0.8709964325378182 +
    m.x5)**2 + (-0.05370495768985595 + m.x6)**2) + m.x824 * ((-0.43669423470125
    + m.x4)**2 + (-0.7826943195653798 + m.x5)**2 + (-0.08246841776453673 +
    m.x6)**2) + m.x825 * ((-0.31217298303878716 + m.x4)**2 + (
    -0.12873842883308007 + m.x5)**2 + (-0.4120375477605329 + m.x6)**2) + m.x826
    * ((-0.04729057034546036 + m.x4)**2 + (-0.615848875622511 + m.x5)**2 + (
    -0.09028092669134402 + m.x6)**2) + m.x827 * ((-0.05579397155334043 + m.x4)
    **2 + (-0.45731350085562406 + m.x5)**2 + (-0.5113200354339912 + m.x6)**2)
    + m.x828 * ((-0.24317770299974573 + m.x4)**2 + (-0.31432958156550617 +
    m.x5)**2 + (-0.29916426285821995 + m.x6)**2) + m.x829 * ((
    -0.6647683703847979 + m.x4)**2 + (-0.5720315504033884 + m.x5)**2 + (
    -0.3330271930609998 + m.x6)**2) + m.x830 * ((-0.0671508784075493 + m.x4)**2
    + (-0.7427046256777622 + m.x5)**2 + (-0.3842554432358185 + m.x6)**2) +
    m.x831 * ((-0.5142618830032626 + m.x4)**2 + (-0.37920880558154235 + m.x5)**
    2 + (-0.17375109475213701 + m.x6)**2) + m.x832 * ((-0.039030898150579474 +
    m.x4)**2 + (-0.416088697819994 + m.x5)**2 + (-0.23777905803288724 + m.x6)**
    2) + m.x833 * ((-0.4717971485183111 + m.x4)**2 + (-0.3383860380066811 +
    m.x5)**2 + (-0.460200523195855 + m.x6)**2) + m.x834 * ((-0.5900378880204267
    + m.x4)**2 + (-0.7255901375319337 + m.x5)**2 + (-0.9154170002928985 + m.x6)
    **2) + m.x835 * ((-0.13093900398824065 + m.x4)**2 + (-0.4052139060110297 +
    m.x5)**2 + (-0.49962194728297327 + m.x6)**2) + m.x836 * ((
    -0.5001698078829642 + m.x4)**2 + (-0.7979303589649438 + m.x5)**2 + (
    -0.2739293646511145 + m.x6)**2) + m.x837 * ((-0.41855315898554013 + m.x4)**
    2 + (-0.998699983121554 + m.x5)**2 + (-0.2010058221141684 + m.x6)**2) +
    m.x838 * ((-0.7496871098706305 + m.x4)**2 + (-0.8235726845357767 + m.x5)**2
    + (-0.37015198039038577 + m.x6)**2) + m.x839 * ((-0.28403104119909195 +
    m.x4)**2 + (-0.6420274479177237 + m.x5)**2 + (-0.4574273157370161 + m.x6)**
    2) + m.x840 * ((-0.46685731585307466 + m.x4)**2 + (-0.26906412522677103 +
    m.x5)**2 + (-0.6656657277253054 + m.x6)**2) + m.x841 * ((
    -0.2504282905612786 + m.x4)**2 + (-0.15851796206472113 + m.x5)**2 + (
    -0.4726147469986297 + m.x6)**2) + m.x842 * ((-0.21194510336903394 + m.x4)**
    2 + (-0.7789673451440703 + m.x5)**2 + (-0.09841245851637492 + m.x6)**2) +
    m.x843 * ((-0.2349671005207027 + m.x4)**2 + (-0.0221927931737832 + m.x5)**2
    + (-0.5712554822182071 + m.x6)**2) + m.x844 * ((-0.0009451790835207641 +
    m.x4)**2 + (-0.2408337245798331 + m.x5)**2 + (-0.6211924391868702 + m.x6)**
    2) + m.x845 * ((-0.6707250517356161 + m.x4)**2 + (-0.5984637186180205 +
    m.x5)**2 + (-0.0668641338162419 + m.x6)**2) + m.x846 * ((
    -0.5511472131778885 + m.x4)**2 + (-0.07350867542191697 + m.x5)**2 + (
    -0.767739792767608 + m.x6)**2) + m.x847 * ((-0.9501581392192964 + m.x4)**2
    + (-0.7233163389390355 + m.x5)**2 + (-0.5166844510344849 + m.x6)**2) +
    m.x848 * ((-0.9060156230362852 + m.x4)**2 + (-0.3113487821639962 + m.x5)**2
    + (-0.20778084543419917 + m.x6)**2) + m.x849 * ((-0.5288680482784139 +
    m.x4)**2 + (-0.2934145990378463 + m.x5)**2 + (-0.4804974743654282 + m.x6)**
    2) + m.x850 * ((-0.09966115943905263 + m.x4)**2 + (-0.3938725699296275 +
    m.x5)**2 + (-0.32444318785821924 + m.x6)**2) + m.x851 * ((
    -0.6520321563540667 + m.x4)**2 + (-0.8056068500183343 + m.x5)**2 + (
    -0.0835838533559482 + m.x6)**2) + m.x852 * ((-0.8166208988287386 + m.x4)**2
    + (-0.3518761684344235 + m.x5)**2 + (-0.7464113961140431 + m.x6)**2) +
    m.x853 * ((-0.1311593203796163 + m.x4)**2 + (-0.7160405481109373 + m.x5)**2
    + (-0.09952132645843448 + m.x6)**2) + m.x854 * ((-0.04779808112037798 +
    m.x4)**2 + (-0.28884699291713234 + m.x5)**2 + (-0.10250649388727473 + m.x6)
    **2) + m.x855 * ((-0.9791729605203251 + m.x4)**2 + (-0.6726875461066422 +
    m.x5)**2 + (-0.9283118905188722 + m.x6)**2) + m.x856 * ((
    -0.13471412533270244 + m.x4)**2 + (-0.7071806165289065 + m.x5)**2 + (
    -0.9043216254262293 + m.x6)**2) + m.x857 * ((-0.5735353939945473 + m.x4)**2
    + (-0.5273208712530736 + m.x5)**2 + (-0.6875628347914862 + m.x6)**2) +
    m.x858 * ((-0.9582137553329777 + m.x4)**2 + (-0.4500040273602035 + m.x5)**2
    + (-0.26668127604253744 + m.x6)**2) + m.x859 * ((-0.35515505710029105 +
    m.x4)**2 + (-0.8998261443565795 + m.x5)**2 + (-0.5147227718297207 + m.x6)**
    2) + m.x860 * ((-0.9340214668622013 + m.x4)**2 + (-0.3503931266703305 +
    m.x5)**2 + (-0.22213442770583658 + m.x6)**2) + m.x861 * ((
    -0.30063857818433126 + m.x4)**2 + (-0.9781639681666726 + m.x5)**2 + (
    -0.5737192124395999 + m.x6)**2) + m.x862 * ((-0.9694287446674323 + m.x4)**2
    + (-0.9139936410886877 + m.x5)**2 + (-0.16757766484105074 + m.x6)**2) +
    m.x863 * ((-0.040594150617694 + m.x4)**2 + (-0.43898895567045837 + m.x5)**2
    + (-0.6978737824797022 + m.x6)**2) + m.x864 * ((-0.9047320599530371 + m.x4)
    **2 + (-0.4912564771269612 + m.x5)**2 + (-0.6733487941467664 + m.x6)**2) +
    m.x865 * ((-0.9549617147031715 + m.x4)**2 + (-0.6678649305928561 + m.x5)**2
    + (-0.8834928821311292 + m.x6)**2) + m.x866 * ((-0.4395498573390294 + m.x4)
    **2 + (-0.30627811842262354 + m.x5)**2 + (-0.9750459496357505 + m.x6)**2)
    + m.x867 * ((-0.1870595942163641 + m.x4)**2 + (-0.151585797566554 + m.x5)
    **2 + (-0.6096114448910821 + m.x6)**2) + m.x868 * ((-0.8951229638762037 +
    m.x4)**2 + (-0.5978267742373706 + m.x5)**2 + (-0.5837237511628297 + m.x6)**
    2) + m.x869 * ((-0.9979607832682635 + m.x4)**2 + (-0.2544630128273442 +
    m.x5)**2 + (-0.7553436617442503 + m.x6)**2) + m.x870 * ((
    -0.18874920320016164 + m.x4)**2 + (-0.6216165758809351 + m.x5)**2 + (
    -0.8529149249653111 + m.x6)**2) + m.x871 * ((-0.6373429941144889 + m.x4)**2
    + (-0.03524085604839855 + m.x5)**2 + (-0.2902922940078507 + m.x6)**2) +
    m.x872 * ((-0.1493240329654184 + m.x4)**2 + (-0.773610378940084 + m.x5)**2
    + (-0.16800156102583386 + m.x6)**2) + m.x873 * ((-0.45959660687249615 +
    m.x4)**2 + (-0.8091285040534932 + m.x5)**2 + (-0.3286890399482034 + m.x6)**
    2) + m.x874 * ((-0.7478644912889102 + m.x4)**2 + (-0.014858297372218665 +
    m.x5)**2 + (-0.6866332635878059 + m.x6)**2) + m.x875 * ((
    -0.7646420573532026 + m.x4)**2 + (-0.9447630530244876 + m.x5)**2 + (
    -0.8190368275925283 + m.x6)**2) + m.x876 * ((-0.9924396130442916 + m.x4)**2
    + (-0.6082265831465189 + m.x5)**2 + (-0.5057251733236754 + m.x6)**2) +
    m.x877 * ((-0.7721758593783997 + m.x4)**2 + (-0.8129769760490057 + m.x5)**2
    + (-0.4066778113300017 + m.x6)**2) + m.x878 * ((-0.5586622471964208 + m.x4)
    **2 + (-0.7449498935310548 + m.x5)**2 + (-0.5133001652292216 + m.x6)**2) +
    m.x879 * ((-0.2606143437838706 + m.x4)**2 + (-0.9157831128583509 + m.x5)**2
    + (-0.7725742539135185 + m.x6)**2) + m.x880 * ((-0.08665312749944609 +
    m.x4)**2 + (-0.20774241016302275 + m.x5)**2 + (-0.392846511749778 + m.x6)**
    2) + m.x881 * ((-0.02318360583183654 + m.x4)**2 + (-0.12136671002398913 +
    m.x5)**2 + (-0.4592804310959082 + m.x6)**2) + m.x882 * ((
    -0.9376542898841029 + m.x4)**2 + (-0.7296259410537214 + m.x5)**2 + (
    -0.43830339602774704 + m.x6)**2) + m.x883 * ((-0.7366058903091773 + m.x4)**
    2 + (-0.4416494908995052 + m.x5)**2 + (-0.8513541067232596 + m.x6)**2) +
    m.x884 * ((-0.2583528714273713 + m.x4)**2 + (-0.8887871795539201 + m.x5)**2
    + (-0.7248310640320087 + m.x6)**2) + m.x885 * ((-0.13907399568052925 +
    m.x4)**2 + (-0.5677374171942082 + m.x5)**2 + (-0.7157625382944803 + m.x6)**
    2) + m.x886 * ((-0.4868142512204441 + m.x4)**2 + (-0.8622063298179061 +
    m.x5)**2 + (-0.4912823321311274 + m.x6)**2) + m.x887 * ((
    -0.5544960376270748 + m.x4)**2 + (-0.8879916713525825 + m.x5)**2 + (
    -0.558510394418158 + m.x6)**2) + m.x888 * ((-0.5629250097194626 + m.x4)**2
    + (-0.02440020191041392 + m.x5)**2 + (-0.3505563159384506 + m.x6)**2) +
    m.x889 * ((-0.5644814229596812 + m.x4)**2 + (-0.9167284919592144 + m.x5)**2
    + (-0.39495515159248495 + m.x6)**2) + m.x890 * ((-0.15293694448570427 +
    m.x4)**2 + (-0.24201305054502364 + m.x5)**2 + (-0.09871933794597176 + m.x6)
    **2) + m.x891 * ((-0.04093761196800816 + m.x4)**2 + (-0.25111569049272453
    + m.x5)**2 + (-0.8857385934563612 + m.x6)**2) + m.x892 * ((
    -0.6455628697859762 + m.x4)**2 + (-0.4324293933492942 + m.x5)**2 + (
    -0.3789568433740764 + m.x6)**2) + m.x893 * ((-0.4496937933648343 + m.x4)**2
    + (-0.5667328853687145 + m.x5)**2 + (-0.40691835531776066 + m.x6)**2) +
    m.x894 * ((-0.5064964841495636 + m.x4)**2 + (-0.9231662667070567 + m.x5)**2
    + (-0.9418870813951559 + m.x6)**2) + m.x895 * ((-0.7546510193031142 + m.x4)
    **2 + (-0.6290717885174039 + m.x5)**2 + (-0.9053863219371039 + m.x6)**2) +
    m.x896 * ((-0.1252499507413295 + m.x4)**2 + (-0.7291266598331314 + m.x5)**2
    + (-0.06287245807908282 + m.x6)**2) + m.x897 * ((-0.975079670779934 + m.x4)
    **2 + (-0.8476261704965108 + m.x5)**2 + (-0.3613523225014157 + m.x6)**2) +
    m.x898 * ((-0.4786145006916671 + m.x4)**2 + (-0.7562794398860281 + m.x5)**2
    + (-0.3246606771087578 + m.x6)**2) + m.x899 * ((-0.37211638738323183 +
    m.x4)**2 + (-0.5285143564556392 + m.x5)**2 + (-0.9473677259758877 + m.x6)**
    2) + m.x900 * ((-0.7747359569068005 + m.x4)**2 + (-0.5606816325734337 +
    m.x5)**2 + (-0.5023744358753353 + m.x6)**2) + m.x901 * ((
    -0.35934929189237974 + m.x4)**2 + (-0.2138842746533064 + m.x5)**2 + (
    -0.47940265124118275 + m.x6)**2) + m.x902 * ((-0.034039058901423114 + m.x4)
    **2 + (-0.8692672460914023 + m.x5)**2 + (-0.7367556473491849 + m.x6)**2) +
    m.x903 * ((-0.7282365643923602 + m.x4)**2 + (-0.6873407784728088 + m.x5)**2
    + (-0.40274097414378485 + m.x6)**2) + m.x904 * ((-0.734857721471257 + m.x4)
    **2 + (-0.262970187892116 + m.x5)**2 + (-0.20961569008988468 + m.x6)**2) +
    m.x905 * ((-0.6525308383090344 + m.x4)**2 + (-0.19608022401263447 + m.x5)**
    2 + (-0.3870236183372049 + m.x6)**2) + m.x906 * ((-0.5645012980468977 +
    m.x4)**2 + (-0.6341191192370838 + m.x5)**2 + (-0.46196225878784536 + m.x6)
    **2) + m.x907 * ((-0.2930551852644451 + m.x4)**2 + (-0.9177900459954397 +
    m.x5)**2 + (-0.5732383676108328 + m.x6)**2) + m.x908 * ((
    -0.5092355531007602 + m.x4)**2 + (-0.18305497891779976 + m.x5)**2 + (
    -0.09370849097948963 + m.x6)**2) + m.x909 * ((-0.9512334177368659 + m.x4)**
    2 + (-0.07342868658441148 + m.x5)**2 + (-0.9395727539085917 + m.x6)**2) +
    m.x910 * ((-0.8094970632512009 + m.x4)**2 + (-0.7305977116464875 + m.x5)**2
    + (-0.8070135155255885 + m.x6)**2) + m.x911 * ((-0.8962127199770125 + m.x4)
    **2 + (-0.24616592065326037 + m.x5)**2 + (-0.5849517947792571 + m.x6)**2)
    + m.x912 * ((-0.7052505213025646 + m.x4)**2 + (-0.0796535796359964 + m.x5)
    **2 + (-0.20277742799437048 + m.x6)**2) + m.x913 * ((-0.6267785193143974 +
    m.x4)**2 + (-0.10746876474982292 + m.x5)**2 + (-0.6494432790830167 + m.x6)
    **2) + m.x914 * ((-0.015520366623647752 + m.x4)**2 + (-0.5842081993611541
    + m.x5)**2 + (-0.2744519446961057 + m.x6)**2) + m.x915 * ((
    -0.9793566236203548 + m.x4)**2 + (-0.22394521684566593 + m.x5)**2 + (
    -0.9058719953285858 + m.x6)**2) + m.x916 * ((-0.3542633017907568 + m.x4)**2
    + (-0.44060726802651784 + m.x5)**2 + (-0.3997128293238619 + m.x6)**2) +
    m.x917 * ((-0.482866380882348 + m.x4)**2 + (-0.18588499288268157 + m.x5)**2
    + (-0.07945614131161916 + m.x6)**2) + m.x918 * ((-0.10608910682131378 +
    m.x4)**2 + (-0.26438328524024857 + m.x5)**2 + (-0.2864127662313217 + m.x6)
    **2) + m.x919 * ((-0.39587823045804427 + m.x4)**2 + (-0.5695813324890586 +
    m.x5)**2 + (-0.1920662220868672 + m.x6)**2) + m.x920 * ((
    -0.06159942259296125 + m.x4)**2 + (-0.24020437828961405 + m.x5)**2 + (
    -0.3840367843355983 + m.x6)**2) + m.x921 * ((-0.7362258383939748 + m.x4)**2
    + (-0.7652235683510016 + m.x5)**2 + (-0.5080623929895395 + m.x6)**2) +
    m.x922 * ((-0.6717905352420465 + m.x4)**2 + (-0.13175135938896554 + m.x5)**
    2 + (-0.8733829715017289 + m.x6)**2) + m.x923 * ((-0.5087936806553548 +
    m.x4)**2 + (-0.9895784354332001 + m.x5)**2 + (-0.5235243911248123 + m.x6)**
    2) + m.x924 * ((-0.5687248806674255 + m.x4)**2 + (-0.4800426470754785 +
    m.x5)**2 + (-0.66476015670848 + m.x6)**2) + m.x925 * ((-0.01879712601243244
    + m.x4)**2 + (-0.9597300904119254 + m.x5)**2 + (-0.6400022174824137 + m.x6)
    **2) + m.x926 * ((-0.4546748066299232 + m.x4)**2 + (-0.08414046444682621 +
    m.x5)**2 + (-0.39949639976218343 + m.x6)**2) + m.x927 * ((
    -0.17854814031575228 + m.x4)**2 + (-0.24423555096632876 + m.x5)**2 + (
    -0.31176738263506176 + m.x6)**2) + m.x928 * ((-0.9738568400798214 + m.x4)**
    2 + (-0.9761211517297564 + m.x5)**2 + (-0.12716216361863075 + m.x6)**2) +
    m.x929 * ((-0.10905660727366906 + m.x4)**2 + (-0.9795748590019786 + m.x5)**
    2 + (-0.7440984394159507 + m.x6)**2) + m.x930 * ((-0.7666642751173116 +
    m.x4)**2 + (-0.3496890268415409 + m.x5)**2 + (-0.7178355854854029 + m.x6)**
    2) + m.x931 * ((-0.013742724746700241 + m.x4)**2 + (-0.43305298229497435 +
    m.x5)**2 + (-0.7254669199672814 + m.x6)**2) + m.x932 * ((
    -0.3275886542048829 + m.x4)**2 + (-0.8378680301704793 + m.x5)**2 + (
    -0.8349975326026666 + m.x6)**2) + m.x933 * ((-0.060805710429040816 + m.x4)
    **2 + (-0.656788371625089 + m.x5)**2 + (-0.2732796886924793 + m.x6)**2) +
    m.x934 * ((-0.9053177349583378 + m.x4)**2 + (-0.16127902677760553 + m.x5)**
    2 + (-0.32227488757718703 + m.x6)**2) + m.x935 * ((-0.9764291442509151 +
    m.x4)**2 + (-0.4200251729022414 + m.x5)**2 + (-0.19500625315790188 + m.x6)
    **2) + m.x936 * ((-0.17071396326782584 + m.x4)**2 + (-0.5019541154498613 +
    m.x5)**2 + (-0.6526843192881269 + m.x6)**2) + m.x937 * ((
    -0.9126755236735188 + m.x4)**2 + (-0.28940415967047584 + m.x5)**2 + (
    -0.1552734500527927 + m.x6)**2) + m.x938 * ((-0.5606535962065278 + m.x4)**2
    + (-0.6342833304382927 + m.x5)**2 + (-0.8585431561155562 + m.x6)**2) +
    m.x939 * ((-0.11687570322670404 + m.x4)**2 + (-0.42299970942250387 + m.x5)
    **2 + (-0.4170059716014207 + m.x6)**2) + m.x940 * ((-0.5142371687254527 +
    m.x4)**2 + (-0.9857105100813118 + m.x5)**2 + (-0.5015291171995875 + m.x6)**
    2) + m.x941 * ((-0.32100216013315164 + m.x4)**2 + (-0.45572573844602215 +
    m.x5)**2 + (-0.48798435784356275 + m.x6)**2) + m.x942 * ((
    -0.597784767358479 + m.x4)**2 + (-0.05186929074401203 + m.x5)**2 + (
    -0.226366390881664 + m.x6)**2) + m.x943 * ((-0.8457016489109802 + m.x4)**2
    + (-0.5554063005937154 + m.x5)**2 + (-0.41321444364538085 + m.x6)**2) +
    m.x944 * ((-0.9475471193586129 + m.x4)**2 + (-0.3121559515841179 + m.x5)**2
    + (-0.14073436444324727 + m.x6)**2) + m.x945 * ((-0.7462797111675085 +
    m.x4)**2 + (-0.0832491058608037 + m.x5)**2 + (-0.16991972648761744 + m.x6)
    **2) + m.x946 * ((-0.6283905422614516 + m.x4)**2 + (-0.3473036441315591 +
    m.x5)**2 + (-0.6256420116557863 + m.x6)**2) + m.x947 * ((
    -0.47557752055186076 + m.x4)**2 + (-0.13087273477706074 + m.x5)**2 + (
    -0.566009659206059 + m.x6)**2) + m.x948 * ((-0.3811223652765986 + m.x4)**2
    + (-0.3419162921570369 + m.x5)**2 + (-0.42670986021880697 + m.x6)**2) +
    m.x949 * ((-0.45276296485818746 + m.x4)**2 + (-0.7292869084688621 + m.x5)**
    2 + (-0.9219484257715016 + m.x6)**2) + m.x950 * ((-0.2944563711575213 +
    m.x4)**2 + (-0.9768141635311406 + m.x5)**2 + (-0.9139907883287979 + m.x6)**
    2) + m.x951 * ((-0.2045693815413957 + m.x4)**2 + (-0.6083069865306869 +
    m.x5)**2 + (-0.5354494090536733 + m.x6)**2) + m.x952 * ((
    -0.9092286101623649 + m.x4)**2 + (-0.19827382634748447 + m.x5)**2 + (
    -0.5692289216759975 + m.x6)**2) + m.x953 * ((-0.4428119569466705 + m.x4)**2
    + (-0.3322800930778397 + m.x5)**2 + (-0.5707107027562174 + m.x6)**2) +
    m.x954 * ((-0.419027742190789 + m.x4)**2 + (-0.4618756991792069 + m.x5)**2
    + (-0.07896233563766164 + m.x6)**2) + m.x955 * ((-0.6584988862725016 +
    m.x4)**2 + (-0.6148209199675768 + m.x5)**2 + (-0.24819109836653064 + m.x6)
    **2) + m.x956 * ((-0.7067453957053103 + m.x4)**2 + (-0.16400947550811773 +
    m.x5)**2 + (-0.2404675897181846 + m.x6)**2) + m.x957 * ((
    -0.6059340157584386 + m.x4)**2 + (-0.368724454571691 + m.x5)**2 + (
    -0.3166424342634133 + m.x6)**2) + m.x958 * ((-0.1505689967926862 + m.x4)**2
    + (-0.625369145400853 + m.x5)**2 + (-0.8732323044478142 + m.x6)**2) +
    m.x959 * ((-0.4387938575304804 + m.x4)**2 + (-0.6686693605208012 + m.x5)**2
    + (-0.5707959366759914 + m.x6)**2) + m.x960 * ((-0.7576333064836764 + m.x4)
    **2 + (-0.15002688954303656 + m.x5)**2 + (-0.15547993353000245 + m.x6)**2)
    + m.x961 * ((-0.666581715107795 + m.x4)**2 + (-0.8984605497623024 + m.x5)
    **2 + (-0.3096514261621284 + m.x6)**2) + m.x962 * ((-0.8387444625970372 +
    m.x4)**2 + (-0.16015110460364135 + m.x5)**2 + (-0.17793311971345638 + m.x6)
    **2) + m.x963 * ((-0.7961300734270524 + m.x4)**2 + (-0.06315804030987215 +
    m.x5)**2 + (-0.2886538911688289 + m.x6)**2) + m.x964 * ((
    -0.09882382311717897 + m.x4)**2 + (-0.9562490103711244 + m.x5)**2 + (
    -0.3979053832361369 + m.x6)**2) + m.x965 * ((-0.1313503761972874 + m.x4)**2
    + (-0.1784477941922571 + m.x5)**2 + (-0.26652042199603243 + m.x6)**2) +
    m.x966 * ((-0.5560596702183167 + m.x4)**2 + (-0.776379609944948 + m.x5)**2
    + (-0.4248340064314263 + m.x6)**2) + m.x967 * ((-0.061904031651977 + m.x4)
    **2 + (-0.6153844859790686 + m.x5)**2 + (-0.9267629321786096 + m.x6)**2) +
    m.x968 * ((-0.22406567435416147 + m.x4)**2 + (-0.16598467807059802 + m.x5)
    **2 + (-0.631039868789005 + m.x6)**2) + m.x969 * ((-0.2067711913915432 +
    m.x4)**2 + (-0.9546739138625829 + m.x5)**2 + (-0.6132888596828534 + m.x6)**
    2) + m.x970 * ((-0.698359896593753 + m.x4)**2 + (-0.09633791817043569 +
    m.x5)**2 + (-0.7767762514491409 + m.x6)**2) + m.x971 * ((
    -0.5495935658571374 + m.x4)**2 + (-0.08474290481778801 + m.x5)**2 + (
    -0.6612846791750243 + m.x6)**2) + m.x972 * ((-0.3161875292045071 + m.x4)**2
    + (-0.6387922458536845 + m.x5)**2 + (-0.7653392459044 + m.x6)**2) + m.x973
    * ((-0.7319358324745259 + m.x4)**2 + (-0.992182632521313 + m.x5)**2 + (
    -0.6863923077018874 + m.x6)**2) + m.x974 * ((-0.6019092920263115 + m.x4)**2
    + (-0.7773860008024426 + m.x5)**2 + (-0.696651134077001 + m.x6)**2) +
    m.x975 * ((-0.8049096869634418 + m.x4)**2 + (-0.0732355551315873 + m.x5)**2
    + (-0.5890554014646376 + m.x6)**2) + m.x976 * ((-0.2400029979216146 + m.x4)
    **2 + (-0.9945676004924368 + m.x5)**2 + (-0.5289410390414967 + m.x6)**2) +
    m.x977 * ((-0.2766431455253143 + m.x4)**2 + (-0.8539068538716186 + m.x5)**2
    + (-0.20627516491122866 + m.x6)**2) + m.x978 * ((-0.35956937240024434 +
    m.x4)**2 + (-0.1564680965685581 + m.x5)**2 + (-0.13254723904140797 + m.x6)
    **2) + m.x979 * ((-0.6851905938616645 + m.x4)**2 + (-0.92350145756233 +
    m.x5)**2 + (-0.12850409116051253 + m.x6)**2) + m.x980 * ((
    -0.8530335314027025 + m.x4)**2 + (-0.014728381555152992 + m.x5)**2 + (
    -0.3823239089970707 + m.x6)**2) + m.x981 * ((-0.20793230117071493 + m.x4)**
    2 + (-0.16676956450110558 + m.x5)**2 + (-0.34228112340343475 + m.x6)**2) +
    m.x982 * ((-0.6234604214732817 + m.x4)**2 + (-0.2502728265106259 + m.x5)**2
    + (-0.3410768048568552 + m.x6)**2) + m.x983 * ((-0.32574485718659996 +
    m.x4)**2 + (-0.49133487411842436 + m.x5)**2 + (-0.9269586652185272 + m.x6)
    **2) + m.x984 * ((-0.8074001332885633 + m.x4)**2 + (-0.436124135331206 +
    m.x5)**2 + (-0.6967988731368366 + m.x6)**2) + m.x985 * ((
    -0.0885078496198809 + m.x4)**2 + (-0.06383953819167731 + m.x5)**2 + (
    -0.12724142698377883 + m.x6)**2) + m.x986 * ((-0.2337562876270498 + m.x4)**
    2 + (-0.17694669799647322 + m.x5)**2 + (-0.24213277883073392 + m.x6)**2) +
    m.x987 * ((-0.4489386544210575 + m.x4)**2 + (-0.39350049538525844 + m.x5)**
    2 + (-0.2766646939987202 + m.x6)**2) + m.x988 * ((-0.6295217224500858 +
    m.x4)**2 + (-0.2004219022799547 + m.x5)**2 + (-0.34401008781100983 + m.x6)
    **2) + m.x989 * ((-0.7178536888350097 + m.x4)**2 + (-0.4777123128107543 +
    m.x5)**2 + (-0.020254499193558706 + m.x6)**2) + m.x990 * ((
    -0.11689305631558389 + m.x4)**2 + (-0.7921096764850253 + m.x5)**2 + (
    -0.0018493281679282658 + m.x6)**2) + m.x991 * ((-0.42252861541271625 + m.x4)
    **2 + (-0.7365281026729076 + m.x5)**2 + (-0.24208265132422635 + m.x6)**2)
    + m.x992 * ((-0.7215969240513533 + m.x4)**2 + (-0.3256843299668196 + m.x5)
    **2 + (-0.3698108298221342 + m.x6)**2) + m.x993 * ((-0.2595423236714335 +
    m.x4)**2 + (-0.2589559818665762 + m.x5)**2 + (-0.18615386799497224 + m.x6)
    **2) + m.x994 * ((-0.9984305905352117 + m.x4)**2 + (-0.7165229939904344 +
    m.x5)**2 + (-0.1285692611907402 + m.x6)**2) + m.x995 * ((
    -0.8872140808683944 + m.x4)**2 + (-0.5011145036032805 + m.x5)**2 + (
    -0.3883708507632184 + m.x6)**2) + m.x996 * ((-0.3924529848246979 + m.x4)**2
    + (-0.22348565481301363 + m.x5)**2 + (-0.2061044173907518 + m.x6)**2) +
    m.x997 * ((-0.9112329633612304 + m.x4)**2 + (-0.3163218232655004 + m.x5)**2
    + (-0.20302411889796268 + m.x6)**2) + m.x998 * ((-0.6097913445881256 +
    m.x4)**2 + (-0.4542976898151134 + m.x5)**2 + (-0.6195483822905107 + m.x6)**
    2) + m.x999 * ((-0.15522553621050394 + m.x4)**2 + (-0.01999404860523235 +
    m.x5)**2 + (-0.23442286593451234 + m.x6)**2) + m.x1000 * ((
    -0.9199134838866957 + m.x4)**2 + (-0.7868442189111334 + m.x5)**2 + (
    -0.34080460170453486 + m.x6)**2) + m.x1001 * ((-0.8166348595782067 + m.x4)
    **2 + (-0.7614497805023087 + m.x5)**2 + (-0.5452680081023854 + m.x6)**2) +
    m.x1002 * ((-0.7603340178252571 + m.x4)**2 + (-0.08882941137693179 + m.x5)
    **2 + (-0.31747640494684937 + m.x6)**2) + m.x1003 * ((-0.5390106156174557
    + m.x4)**2 + (-0.4032399762516905 + m.x5)**2 + (-0.034174294693909646 +
    m.x6)**2) + m.x1004 * ((-0.6762581280338263 + m.x4)**2 + (
    -0.1341686429284461 + m.x5)**2 + (-0.6300346342580874 + m.x6)**2) + m.x1005
    * ((-0.5985705326875344 + m.x4)**2 + (-0.6782117564373487 + m.x5)**2 + (
    -0.9723972807848017 + m.x6)**2) + m.x1006 * ((-0.9582896782474865 + m.x4)**
    2 + (-0.647483553547818 + m.x5)**2 + (-0.2553574307779871 + m.x6)**2))

m.e1 = Constraint(expr= m.x7 + m.x507 == 1)
m.e2 = Constraint(expr= m.x8 + m.x508 == 1)
m.e3 = Constraint(expr= m.x9 + m.x509 == 1)
m.e4 = Constraint(expr= m.x10 + m.x510 == 1)
m.e5 = Constraint(expr= m.x11 + m.x511 == 1)
m.e6 = Constraint(expr= m.x12 + m.x512 == 1)
m.e7 = Constraint(expr= m.x13 + m.x513 == 1)
m.e8 = Constraint(expr= m.x14 + m.x514 == 1)
m.e9 = Constraint(expr= m.x15 + m.x515 == 1)
m.e10 = Constraint(expr= m.x16 + m.x516 == 1)
m.e11 = Constraint(expr= m.x17 + m.x517 == 1)
m.e12 = Constraint(expr= m.x18 + m.x518 == 1)
m.e13 = Constraint(expr= m.x19 + m.x519 == 1)
m.e14 = Constraint(expr= m.x20 + m.x520 == 1)
m.e15 = Constraint(expr= m.x21 + m.x521 == 1)
m.e16 = Constraint(expr= m.x22 + m.x522 == 1)
m.e17 = Constraint(expr= m.x23 + m.x523 == 1)
m.e18 = Constraint(expr= m.x24 + m.x524 == 1)
m.e19 = Constraint(expr= m.x25 + m.x525 == 1)
m.e20 = Constraint(expr= m.x26 + m.x526 == 1)
m.e21 = Constraint(expr= m.x27 + m.x527 == 1)
m.e22 = Constraint(expr= m.x28 + m.x528 == 1)
m.e23 = Constraint(expr= m.x29 + m.x529 == 1)
m.e24 = Constraint(expr= m.x30 + m.x530 == 1)
m.e25 = Constraint(expr= m.x31 + m.x531 == 1)
m.e26 = Constraint(expr= m.x32 + m.x532 == 1)
m.e27 = Constraint(expr= m.x33 + m.x533 == 1)
m.e28 = Constraint(expr= m.x34 + m.x534 == 1)
m.e29 = Constraint(expr= m.x35 + m.x535 == 1)
m.e30 = Constraint(expr= m.x36 + m.x536 == 1)
m.e31 = Constraint(expr= m.x37 + m.x537 == 1)
m.e32 = Constraint(expr= m.x38 + m.x538 == 1)
m.e33 = Constraint(expr= m.x39 + m.x539 == 1)
m.e34 = Constraint(expr= m.x40 + m.x540 == 1)
m.e35 = Constraint(expr= m.x41 + m.x541 == 1)
m.e36 = Constraint(expr= m.x42 + m.x542 == 1)
m.e37 = Constraint(expr= m.x43 + m.x543 == 1)
m.e38 = Constraint(expr= m.x44 + m.x544 == 1)
m.e39 = Constraint(expr= m.x45 + m.x545 == 1)
m.e40 = Constraint(expr= m.x46 + m.x546 == 1)
m.e41 = Constraint(expr= m.x47 + m.x547 == 1)
m.e42 = Constraint(expr= m.x48 + m.x548 == 1)
m.e43 = Constraint(expr= m.x49 + m.x549 == 1)
m.e44 = Constraint(expr= m.x50 + m.x550 == 1)
m.e45 = Constraint(expr= m.x51 + m.x551 == 1)
m.e46 = Constraint(expr= m.x52 + m.x552 == 1)
m.e47 = Constraint(expr= m.x53 + m.x553 == 1)
m.e48 = Constraint(expr= m.x54 + m.x554 == 1)
m.e49 = Constraint(expr= m.x55 + m.x555 == 1)
m.e50 = Constraint(expr= m.x56 + m.x556 == 1)
m.e51 = Constraint(expr= m.x57 + m.x557 == 1)
m.e52 = Constraint(expr= m.x58 + m.x558 == 1)
m.e53 = Constraint(expr= m.x59 + m.x559 == 1)
m.e54 = Constraint(expr= m.x60 + m.x560 == 1)
m.e55 = Constraint(expr= m.x61 + m.x561 == 1)
m.e56 = Constraint(expr= m.x62 + m.x562 == 1)
m.e57 = Constraint(expr= m.x63 + m.x563 == 1)
m.e58 = Constraint(expr= m.x64 + m.x564 == 1)
m.e59 = Constraint(expr= m.x65 + m.x565 == 1)
m.e60 = Constraint(expr= m.x66 + m.x566 == 1)
m.e61 = Constraint(expr= m.x67 + m.x567 == 1)
m.e62 = Constraint(expr= m.x68 + m.x568 == 1)
m.e63 = Constraint(expr= m.x69 + m.x569 == 1)
m.e64 = Constraint(expr= m.x70 + m.x570 == 1)
m.e65 = Constraint(expr= m.x71 + m.x571 == 1)
m.e66 = Constraint(expr= m.x72 + m.x572 == 1)
m.e67 = Constraint(expr= m.x73 + m.x573 == 1)
m.e68 = Constraint(expr= m.x74 + m.x574 == 1)
m.e69 = Constraint(expr= m.x75 + m.x575 == 1)
m.e70 = Constraint(expr= m.x76 + m.x576 == 1)
m.e71 = Constraint(expr= m.x77 + m.x577 == 1)
m.e72 = Constraint(expr= m.x78 + m.x578 == 1)
m.e73 = Constraint(expr= m.x79 + m.x579 == 1)
m.e74 = Constraint(expr= m.x80 + m.x580 == 1)
m.e75 = Constraint(expr= m.x81 + m.x581 == 1)
m.e76 = Constraint(expr= m.x82 + m.x582 == 1)
m.e77 = Constraint(expr= m.x83 + m.x583 == 1)
m.e78 = Constraint(expr= m.x84 + m.x584 == 1)
m.e79 = Constraint(expr= m.x85 + m.x585 == 1)
m.e80 = Constraint(expr= m.x86 + m.x586 == 1)
m.e81 = Constraint(expr= m.x87 + m.x587 == 1)
m.e82 = Constraint(expr= m.x88 + m.x588 == 1)
m.e83 = Constraint(expr= m.x89 + m.x589 == 1)
m.e84 = Constraint(expr= m.x90 + m.x590 == 1)
m.e85 = Constraint(expr= m.x91 + m.x591 == 1)
m.e86 = Constraint(expr= m.x92 + m.x592 == 1)
m.e87 = Constraint(expr= m.x93 + m.x593 == 1)
m.e88 = Constraint(expr= m.x94 + m.x594 == 1)
m.e89 = Constraint(expr= m.x95 + m.x595 == 1)
m.e90 = Constraint(expr= m.x96 + m.x596 == 1)
m.e91 = Constraint(expr= m.x97 + m.x597 == 1)
m.e92 = Constraint(expr= m.x98 + m.x598 == 1)
m.e93 = Constraint(expr= m.x99 + m.x599 == 1)
m.e94 = Constraint(expr= m.x100 + m.x600 == 1)
m.e95 = Constraint(expr= m.x101 + m.x601 == 1)
m.e96 = Constraint(expr= m.x102 + m.x602 == 1)
m.e97 = Constraint(expr= m.x103 + m.x603 == 1)
m.e98 = Constraint(expr= m.x104 + m.x604 == 1)
m.e99 = Constraint(expr= m.x105 + m.x605 == 1)
m.e100 = Constraint(expr= m.x106 + m.x606 == 1)
m.e101 = Constraint(expr= m.x107 + m.x607 == 1)
m.e102 = Constraint(expr= m.x108 + m.x608 == 1)
m.e103 = Constraint(expr= m.x109 + m.x609 == 1)
m.e104 = Constraint(expr= m.x110 + m.x610 == 1)
m.e105 = Constraint(expr= m.x111 + m.x611 == 1)
m.e106 = Constraint(expr= m.x112 + m.x612 == 1)
m.e107 = Constraint(expr= m.x113 + m.x613 == 1)
m.e108 = Constraint(expr= m.x114 + m.x614 == 1)
m.e109 = Constraint(expr= m.x115 + m.x615 == 1)
m.e110 = Constraint(expr= m.x116 + m.x616 == 1)
m.e111 = Constraint(expr= m.x117 + m.x617 == 1)
m.e112 = Constraint(expr= m.x118 + m.x618 == 1)
m.e113 = Constraint(expr= m.x119 + m.x619 == 1)
m.e114 = Constraint(expr= m.x120 + m.x620 == 1)
m.e115 = Constraint(expr= m.x121 + m.x621 == 1)
m.e116 = Constraint(expr= m.x122 + m.x622 == 1)
m.e117 = Constraint(expr= m.x123 + m.x623 == 1)
m.e118 = Constraint(expr= m.x124 + m.x624 == 1)
m.e119 = Constraint(expr= m.x125 + m.x625 == 1)
m.e120 = Constraint(expr= m.x126 + m.x626 == 1)
m.e121 = Constraint(expr= m.x127 + m.x627 == 1)
m.e122 = Constraint(expr= m.x128 + m.x628 == 1)
m.e123 = Constraint(expr= m.x129 + m.x629 == 1)
m.e124 = Constraint(expr= m.x130 + m.x630 == 1)
m.e125 = Constraint(expr= m.x131 + m.x631 == 1)
m.e126 = Constraint(expr= m.x132 + m.x632 == 1)
m.e127 = Constraint(expr= m.x133 + m.x633 == 1)
m.e128 = Constraint(expr= m.x134 + m.x634 == 1)
m.e129 = Constraint(expr= m.x135 + m.x635 == 1)
m.e130 = Constraint(expr= m.x136 + m.x636 == 1)
m.e131 = Constraint(expr= m.x137 + m.x637 == 1)
m.e132 = Constraint(expr= m.x138 + m.x638 == 1)
m.e133 = Constraint(expr= m.x139 + m.x639 == 1)
m.e134 = Constraint(expr= m.x140 + m.x640 == 1)
m.e135 = Constraint(expr= m.x141 + m.x641 == 1)
m.e136 = Constraint(expr= m.x142 + m.x642 == 1)
m.e137 = Constraint(expr= m.x143 + m.x643 == 1)
m.e138 = Constraint(expr= m.x144 + m.x644 == 1)
m.e139 = Constraint(expr= m.x145 + m.x645 == 1)
m.e140 = Constraint(expr= m.x146 + m.x646 == 1)
m.e141 = Constraint(expr= m.x147 + m.x647 == 1)
m.e142 = Constraint(expr= m.x148 + m.x648 == 1)
m.e143 = Constraint(expr= m.x149 + m.x649 == 1)
m.e144 = Constraint(expr= m.x150 + m.x650 == 1)
m.e145 = Constraint(expr= m.x151 + m.x651 == 1)
m.e146 = Constraint(expr= m.x152 + m.x652 == 1)
m.e147 = Constraint(expr= m.x153 + m.x653 == 1)
m.e148 = Constraint(expr= m.x154 + m.x654 == 1)
m.e149 = Constraint(expr= m.x155 + m.x655 == 1)
m.e150 = Constraint(expr= m.x156 + m.x656 == 1)
m.e151 = Constraint(expr= m.x157 + m.x657 == 1)
m.e152 = Constraint(expr= m.x158 + m.x658 == 1)
m.e153 = Constraint(expr= m.x159 + m.x659 == 1)
m.e154 = Constraint(expr= m.x160 + m.x660 == 1)
m.e155 = Constraint(expr= m.x161 + m.x661 == 1)
m.e156 = Constraint(expr= m.x162 + m.x662 == 1)
m.e157 = Constraint(expr= m.x163 + m.x663 == 1)
m.e158 = Constraint(expr= m.x164 + m.x664 == 1)
m.e159 = Constraint(expr= m.x165 + m.x665 == 1)
m.e160 = Constraint(expr= m.x166 + m.x666 == 1)
m.e161 = Constraint(expr= m.x167 + m.x667 == 1)
m.e162 = Constraint(expr= m.x168 + m.x668 == 1)
m.e163 = Constraint(expr= m.x169 + m.x669 == 1)
m.e164 = Constraint(expr= m.x170 + m.x670 == 1)
m.e165 = Constraint(expr= m.x171 + m.x671 == 1)
m.e166 = Constraint(expr= m.x172 + m.x672 == 1)
m.e167 = Constraint(expr= m.x173 + m.x673 == 1)
m.e168 = Constraint(expr= m.x174 + m.x674 == 1)
m.e169 = Constraint(expr= m.x175 + m.x675 == 1)
m.e170 = Constraint(expr= m.x176 + m.x676 == 1)
m.e171 = Constraint(expr= m.x177 + m.x677 == 1)
m.e172 = Constraint(expr= m.x178 + m.x678 == 1)
m.e173 = Constraint(expr= m.x179 + m.x679 == 1)
m.e174 = Constraint(expr= m.x180 + m.x680 == 1)
m.e175 = Constraint(expr= m.x181 + m.x681 == 1)
m.e176 = Constraint(expr= m.x182 + m.x682 == 1)
m.e177 = Constraint(expr= m.x183 + m.x683 == 1)
m.e178 = Constraint(expr= m.x184 + m.x684 == 1)
m.e179 = Constraint(expr= m.x185 + m.x685 == 1)
m.e180 = Constraint(expr= m.x186 + m.x686 == 1)
m.e181 = Constraint(expr= m.x187 + m.x687 == 1)
m.e182 = Constraint(expr= m.x188 + m.x688 == 1)
m.e183 = Constraint(expr= m.x189 + m.x689 == 1)
m.e184 = Constraint(expr= m.x190 + m.x690 == 1)
m.e185 = Constraint(expr= m.x191 + m.x691 == 1)
m.e186 = Constraint(expr= m.x192 + m.x692 == 1)
m.e187 = Constraint(expr= m.x193 + m.x693 == 1)
m.e188 = Constraint(expr= m.x194 + m.x694 == 1)
m.e189 = Constraint(expr= m.x195 + m.x695 == 1)
m.e190 = Constraint(expr= m.x196 + m.x696 == 1)
m.e191 = Constraint(expr= m.x197 + m.x697 == 1)
m.e192 = Constraint(expr= m.x198 + m.x698 == 1)
m.e193 = Constraint(expr= m.x199 + m.x699 == 1)
m.e194 = Constraint(expr= m.x200 + m.x700 == 1)
m.e195 = Constraint(expr= m.x201 + m.x701 == 1)
m.e196 = Constraint(expr= m.x202 + m.x702 == 1)
m.e197 = Constraint(expr= m.x203 + m.x703 == 1)
m.e198 = Constraint(expr= m.x204 + m.x704 == 1)
m.e199 = Constraint(expr= m.x205 + m.x705 == 1)
m.e200 = Constraint(expr= m.x206 + m.x706 == 1)
m.e201 = Constraint(expr= m.x207 + m.x707 == 1)
m.e202 = Constraint(expr= m.x208 + m.x708 == 1)
m.e203 = Constraint(expr= m.x209 + m.x709 == 1)
m.e204 = Constraint(expr= m.x210 + m.x710 == 1)
m.e205 = Constraint(expr= m.x211 + m.x711 == 1)
m.e206 = Constraint(expr= m.x212 + m.x712 == 1)
m.e207 = Constraint(expr= m.x213 + m.x713 == 1)
m.e208 = Constraint(expr= m.x214 + m.x714 == 1)
m.e209 = Constraint(expr= m.x215 + m.x715 == 1)
m.e210 = Constraint(expr= m.x216 + m.x716 == 1)
m.e211 = Constraint(expr= m.x217 + m.x717 == 1)
m.e212 = Constraint(expr= m.x218 + m.x718 == 1)
m.e213 = Constraint(expr= m.x219 + m.x719 == 1)
m.e214 = Constraint(expr= m.x220 + m.x720 == 1)
m.e215 = Constraint(expr= m.x221 + m.x721 == 1)
m.e216 = Constraint(expr= m.x222 + m.x722 == 1)
m.e217 = Constraint(expr= m.x223 + m.x723 == 1)
m.e218 = Constraint(expr= m.x224 + m.x724 == 1)
m.e219 = Constraint(expr= m.x225 + m.x725 == 1)
m.e220 = Constraint(expr= m.x226 + m.x726 == 1)
m.e221 = Constraint(expr= m.x227 + m.x727 == 1)
m.e222 = Constraint(expr= m.x228 + m.x728 == 1)
m.e223 = Constraint(expr= m.x229 + m.x729 == 1)
m.e224 = Constraint(expr= m.x230 + m.x730 == 1)
m.e225 = Constraint(expr= m.x231 + m.x731 == 1)
m.e226 = Constraint(expr= m.x232 + m.x732 == 1)
m.e227 = Constraint(expr= m.x233 + m.x733 == 1)
m.e228 = Constraint(expr= m.x234 + m.x734 == 1)
m.e229 = Constraint(expr= m.x235 + m.x735 == 1)
m.e230 = Constraint(expr= m.x236 + m.x736 == 1)
m.e231 = Constraint(expr= m.x237 + m.x737 == 1)
m.e232 = Constraint(expr= m.x238 + m.x738 == 1)
m.e233 = Constraint(expr= m.x239 + m.x739 == 1)
m.e234 = Constraint(expr= m.x240 + m.x740 == 1)
m.e235 = Constraint(expr= m.x241 + m.x741 == 1)
m.e236 = Constraint(expr= m.x242 + m.x742 == 1)
m.e237 = Constraint(expr= m.x243 + m.x743 == 1)
m.e238 = Constraint(expr= m.x244 + m.x744 == 1)
m.e239 = Constraint(expr= m.x245 + m.x745 == 1)
m.e240 = Constraint(expr= m.x246 + m.x746 == 1)
m.e241 = Constraint(expr= m.x247 + m.x747 == 1)
m.e242 = Constraint(expr= m.x248 + m.x748 == 1)
m.e243 = Constraint(expr= m.x249 + m.x749 == 1)
m.e244 = Constraint(expr= m.x250 + m.x750 == 1)
m.e245 = Constraint(expr= m.x251 + m.x751 == 1)
m.e246 = Constraint(expr= m.x252 + m.x752 == 1)
m.e247 = Constraint(expr= m.x253 + m.x753 == 1)
m.e248 = Constraint(expr= m.x254 + m.x754 == 1)
m.e249 = Constraint(expr= m.x255 + m.x755 == 1)
m.e250 = Constraint(expr= m.x256 + m.x756 == 1)
m.e251 = Constraint(expr= m.x257 + m.x757 == 1)
m.e252 = Constraint(expr= m.x258 + m.x758 == 1)
m.e253 = Constraint(expr= m.x259 + m.x759 == 1)
m.e254 = Constraint(expr= m.x260 + m.x760 == 1)
m.e255 = Constraint(expr= m.x261 + m.x761 == 1)
m.e256 = Constraint(expr= m.x262 + m.x762 == 1)
m.e257 = Constraint(expr= m.x263 + m.x763 == 1)
m.e258 = Constraint(expr= m.x264 + m.x764 == 1)
m.e259 = Constraint(expr= m.x265 + m.x765 == 1)
m.e260 = Constraint(expr= m.x266 + m.x766 == 1)
m.e261 = Constraint(expr= m.x267 + m.x767 == 1)
m.e262 = Constraint(expr= m.x268 + m.x768 == 1)
m.e263 = Constraint(expr= m.x269 + m.x769 == 1)
m.e264 = Constraint(expr= m.x270 + m.x770 == 1)
m.e265 = Constraint(expr= m.x271 + m.x771 == 1)
m.e266 = Constraint(expr= m.x272 + m.x772 == 1)
m.e267 = Constraint(expr= m.x273 + m.x773 == 1)
m.e268 = Constraint(expr= m.x274 + m.x774 == 1)
m.e269 = Constraint(expr= m.x275 + m.x775 == 1)
m.e270 = Constraint(expr= m.x276 + m.x776 == 1)
m.e271 = Constraint(expr= m.x277 + m.x777 == 1)
m.e272 = Constraint(expr= m.x278 + m.x778 == 1)
m.e273 = Constraint(expr= m.x279 + m.x779 == 1)
m.e274 = Constraint(expr= m.x280 + m.x780 == 1)
m.e275 = Constraint(expr= m.x281 + m.x781 == 1)
m.e276 = Constraint(expr= m.x282 + m.x782 == 1)
m.e277 = Constraint(expr= m.x283 + m.x783 == 1)
m.e278 = Constraint(expr= m.x284 + m.x784 == 1)
m.e279 = Constraint(expr= m.x285 + m.x785 == 1)
m.e280 = Constraint(expr= m.x286 + m.x786 == 1)
m.e281 = Constraint(expr= m.x287 + m.x787 == 1)
m.e282 = Constraint(expr= m.x288 + m.x788 == 1)
m.e283 = Constraint(expr= m.x289 + m.x789 == 1)
m.e284 = Constraint(expr= m.x290 + m.x790 == 1)
m.e285 = Constraint(expr= m.x291 + m.x791 == 1)
m.e286 = Constraint(expr= m.x292 + m.x792 == 1)
m.e287 = Constraint(expr= m.x293 + m.x793 == 1)
m.e288 = Constraint(expr= m.x294 + m.x794 == 1)
m.e289 = Constraint(expr= m.x295 + m.x795 == 1)
m.e290 = Constraint(expr= m.x296 + m.x796 == 1)
m.e291 = Constraint(expr= m.x297 + m.x797 == 1)
m.e292 = Constraint(expr= m.x298 + m.x798 == 1)
m.e293 = Constraint(expr= m.x299 + m.x799 == 1)
m.e294 = Constraint(expr= m.x300 + m.x800 == 1)
m.e295 = Constraint(expr= m.x301 + m.x801 == 1)
m.e296 = Constraint(expr= m.x302 + m.x802 == 1)
m.e297 = Constraint(expr= m.x303 + m.x803 == 1)
m.e298 = Constraint(expr= m.x304 + m.x804 == 1)
m.e299 = Constraint(expr= m.x305 + m.x805 == 1)
m.e300 = Constraint(expr= m.x306 + m.x806 == 1)
m.e301 = Constraint(expr= m.x307 + m.x807 == 1)
m.e302 = Constraint(expr= m.x308 + m.x808 == 1)
m.e303 = Constraint(expr= m.x309 + m.x809 == 1)
m.e304 = Constraint(expr= m.x310 + m.x810 == 1)
m.e305 = Constraint(expr= m.x311 + m.x811 == 1)
m.e306 = Constraint(expr= m.x312 + m.x812 == 1)
m.e307 = Constraint(expr= m.x313 + m.x813 == 1)
m.e308 = Constraint(expr= m.x314 + m.x814 == 1)
m.e309 = Constraint(expr= m.x315 + m.x815 == 1)
m.e310 = Constraint(expr= m.x316 + m.x816 == 1)
m.e311 = Constraint(expr= m.x317 + m.x817 == 1)
m.e312 = Constraint(expr= m.x318 + m.x818 == 1)
m.e313 = Constraint(expr= m.x319 + m.x819 == 1)
m.e314 = Constraint(expr= m.x320 + m.x820 == 1)
m.e315 = Constraint(expr= m.x321 + m.x821 == 1)
m.e316 = Constraint(expr= m.x322 + m.x822 == 1)
m.e317 = Constraint(expr= m.x323 + m.x823 == 1)
m.e318 = Constraint(expr= m.x324 + m.x824 == 1)
m.e319 = Constraint(expr= m.x325 + m.x825 == 1)
m.e320 = Constraint(expr= m.x326 + m.x826 == 1)
m.e321 = Constraint(expr= m.x327 + m.x827 == 1)
m.e322 = Constraint(expr= m.x328 + m.x828 == 1)
m.e323 = Constraint(expr= m.x329 + m.x829 == 1)
m.e324 = Constraint(expr= m.x330 + m.x830 == 1)
m.e325 = Constraint(expr= m.x331 + m.x831 == 1)
m.e326 = Constraint(expr= m.x332 + m.x832 == 1)
m.e327 = Constraint(expr= m.x333 + m.x833 == 1)
m.e328 = Constraint(expr= m.x334 + m.x834 == 1)
m.e329 = Constraint(expr= m.x335 + m.x835 == 1)
m.e330 = Constraint(expr= m.x336 + m.x836 == 1)
m.e331 = Constraint(expr= m.x337 + m.x837 == 1)
m.e332 = Constraint(expr= m.x338 + m.x838 == 1)
m.e333 = Constraint(expr= m.x339 + m.x839 == 1)
m.e334 = Constraint(expr= m.x340 + m.x840 == 1)
m.e335 = Constraint(expr= m.x341 + m.x841 == 1)
m.e336 = Constraint(expr= m.x342 + m.x842 == 1)
m.e337 = Constraint(expr= m.x343 + m.x843 == 1)
m.e338 = Constraint(expr= m.x344 + m.x844 == 1)
m.e339 = Constraint(expr= m.x345 + m.x845 == 1)
m.e340 = Constraint(expr= m.x346 + m.x846 == 1)
m.e341 = Constraint(expr= m.x347 + m.x847 == 1)
m.e342 = Constraint(expr= m.x348 + m.x848 == 1)
m.e343 = Constraint(expr= m.x349 + m.x849 == 1)
m.e344 = Constraint(expr= m.x350 + m.x850 == 1)
m.e345 = Constraint(expr= m.x351 + m.x851 == 1)
m.e346 = Constraint(expr= m.x352 + m.x852 == 1)
m.e347 = Constraint(expr= m.x353 + m.x853 == 1)
m.e348 = Constraint(expr= m.x354 + m.x854 == 1)
m.e349 = Constraint(expr= m.x355 + m.x855 == 1)
m.e350 = Constraint(expr= m.x356 + m.x856 == 1)
m.e351 = Constraint(expr= m.x357 + m.x857 == 1)
m.e352 = Constraint(expr= m.x358 + m.x858 == 1)
m.e353 = Constraint(expr= m.x359 + m.x859 == 1)
m.e354 = Constraint(expr= m.x360 + m.x860 == 1)
m.e355 = Constraint(expr= m.x361 + m.x861 == 1)
m.e356 = Constraint(expr= m.x362 + m.x862 == 1)
m.e357 = Constraint(expr= m.x363 + m.x863 == 1)
m.e358 = Constraint(expr= m.x364 + m.x864 == 1)
m.e359 = Constraint(expr= m.x365 + m.x865 == 1)
m.e360 = Constraint(expr= m.x366 + m.x866 == 1)
m.e361 = Constraint(expr= m.x367 + m.x867 == 1)
m.e362 = Constraint(expr= m.x368 + m.x868 == 1)
m.e363 = Constraint(expr= m.x369 + m.x869 == 1)
m.e364 = Constraint(expr= m.x370 + m.x870 == 1)
m.e365 = Constraint(expr= m.x371 + m.x871 == 1)
m.e366 = Constraint(expr= m.x372 + m.x872 == 1)
m.e367 = Constraint(expr= m.x373 + m.x873 == 1)
m.e368 = Constraint(expr= m.x374 + m.x874 == 1)
m.e369 = Constraint(expr= m.x375 + m.x875 == 1)
m.e370 = Constraint(expr= m.x376 + m.x876 == 1)
m.e371 = Constraint(expr= m.x377 + m.x877 == 1)
m.e372 = Constraint(expr= m.x378 + m.x878 == 1)
m.e373 = Constraint(expr= m.x379 + m.x879 == 1)
m.e374 = Constraint(expr= m.x380 + m.x880 == 1)
m.e375 = Constraint(expr= m.x381 + m.x881 == 1)
m.e376 = Constraint(expr= m.x382 + m.x882 == 1)
m.e377 = Constraint(expr= m.x383 + m.x883 == 1)
m.e378 = Constraint(expr= m.x384 + m.x884 == 1)
m.e379 = Constraint(expr= m.x385 + m.x885 == 1)
m.e380 = Constraint(expr= m.x386 + m.x886 == 1)
m.e381 = Constraint(expr= m.x387 + m.x887 == 1)
m.e382 = Constraint(expr= m.x388 + m.x888 == 1)
m.e383 = Constraint(expr= m.x389 + m.x889 == 1)
m.e384 = Constraint(expr= m.x390 + m.x890 == 1)
m.e385 = Constraint(expr= m.x391 + m.x891 == 1)
m.e386 = Constraint(expr= m.x392 + m.x892 == 1)
m.e387 = Constraint(expr= m.x393 + m.x893 == 1)
m.e388 = Constraint(expr= m.x394 + m.x894 == 1)
m.e389 = Constraint(expr= m.x395 + m.x895 == 1)
m.e390 = Constraint(expr= m.x396 + m.x896 == 1)
m.e391 = Constraint(expr= m.x397 + m.x897 == 1)
m.e392 = Constraint(expr= m.x398 + m.x898 == 1)
m.e393 = Constraint(expr= m.x399 + m.x899 == 1)
m.e394 = Constraint(expr= m.x400 + m.x900 == 1)
m.e395 = Constraint(expr= m.x401 + m.x901 == 1)
m.e396 = Constraint(expr= m.x402 + m.x902 == 1)
m.e397 = Constraint(expr= m.x403 + m.x903 == 1)
m.e398 = Constraint(expr= m.x404 + m.x904 == 1)
m.e399 = Constraint(expr= m.x405 + m.x905 == 1)
m.e400 = Constraint(expr= m.x406 + m.x906 == 1)
m.e401 = Constraint(expr= m.x407 + m.x907 == 1)
m.e402 = Constraint(expr= m.x408 + m.x908 == 1)
m.e403 = Constraint(expr= m.x409 + m.x909 == 1)
m.e404 = Constraint(expr= m.x410 + m.x910 == 1)
m.e405 = Constraint(expr= m.x411 + m.x911 == 1)
m.e406 = Constraint(expr= m.x412 + m.x912 == 1)
m.e407 = Constraint(expr= m.x413 + m.x913 == 1)
m.e408 = Constraint(expr= m.x414 + m.x914 == 1)
m.e409 = Constraint(expr= m.x415 + m.x915 == 1)
m.e410 = Constraint(expr= m.x416 + m.x916 == 1)
m.e411 = Constraint(expr= m.x417 + m.x917 == 1)
m.e412 = Constraint(expr= m.x418 + m.x918 == 1)
m.e413 = Constraint(expr= m.x419 + m.x919 == 1)
m.e414 = Constraint(expr= m.x420 + m.x920 == 1)
m.e415 = Constraint(expr= m.x421 + m.x921 == 1)
m.e416 = Constraint(expr= m.x422 + m.x922 == 1)
m.e417 = Constraint(expr= m.x423 + m.x923 == 1)
m.e418 = Constraint(expr= m.x424 + m.x924 == 1)
m.e419 = Constraint(expr= m.x425 + m.x925 == 1)
m.e420 = Constraint(expr= m.x426 + m.x926 == 1)
m.e421 = Constraint(expr= m.x427 + m.x927 == 1)
m.e422 = Constraint(expr= m.x428 + m.x928 == 1)
m.e423 = Constraint(expr= m.x429 + m.x929 == 1)
m.e424 = Constraint(expr= m.x430 + m.x930 == 1)
m.e425 = Constraint(expr= m.x431 + m.x931 == 1)
m.e426 = Constraint(expr= m.x432 + m.x932 == 1)
m.e427 = Constraint(expr= m.x433 + m.x933 == 1)
m.e428 = Constraint(expr= m.x434 + m.x934 == 1)
m.e429 = Constraint(expr= m.x435 + m.x935 == 1)
m.e430 = Constraint(expr= m.x436 + m.x936 == 1)
m.e431 = Constraint(expr= m.x437 + m.x937 == 1)
m.e432 = Constraint(expr= m.x438 + m.x938 == 1)
m.e433 = Constraint(expr= m.x439 + m.x939 == 1)
m.e434 = Constraint(expr= m.x440 + m.x940 == 1)
m.e435 = Constraint(expr= m.x441 + m.x941 == 1)
m.e436 = Constraint(expr= m.x442 + m.x942 == 1)
m.e437 = Constraint(expr= m.x443 + m.x943 == 1)
m.e438 = Constraint(expr= m.x444 + m.x944 == 1)
m.e439 = Constraint(expr= m.x445 + m.x945 == 1)
m.e440 = Constraint(expr= m.x446 + m.x946 == 1)
m.e441 = Constraint(expr= m.x447 + m.x947 == 1)
m.e442 = Constraint(expr= m.x448 + m.x948 == 1)
m.e443 = Constraint(expr= m.x449 + m.x949 == 1)
m.e444 = Constraint(expr= m.x450 + m.x950 == 1)
m.e445 = Constraint(expr= m.x451 + m.x951 == 1)
m.e446 = Constraint(expr= m.x452 + m.x952 == 1)
m.e447 = Constraint(expr= m.x453 + m.x953 == 1)
m.e448 = Constraint(expr= m.x454 + m.x954 == 1)
m.e449 = Constraint(expr= m.x455 + m.x955 == 1)
m.e450 = Constraint(expr= m.x456 + m.x956 == 1)
m.e451 = Constraint(expr= m.x457 + m.x957 == 1)
m.e452 = Constraint(expr= m.x458 + m.x958 == 1)
m.e453 = Constraint(expr= m.x459 + m.x959 == 1)
m.e454 = Constraint(expr= m.x460 + m.x960 == 1)
m.e455 = Constraint(expr= m.x461 + m.x961 == 1)
m.e456 = Constraint(expr= m.x462 + m.x962 == 1)
m.e457 = Constraint(expr= m.x463 + m.x963 == 1)
m.e458 = Constraint(expr= m.x464 + m.x964 == 1)
m.e459 = Constraint(expr= m.x465 + m.x965 == 1)
m.e460 = Constraint(expr= m.x466 + m.x966 == 1)
m.e461 = Constraint(expr= m.x467 + m.x967 == 1)
m.e462 = Constraint(expr= m.x468 + m.x968 == 1)
m.e463 = Constraint(expr= m.x469 + m.x969 == 1)
m.e464 = Constraint(expr= m.x470 + m.x970 == 1)
m.e465 = Constraint(expr= m.x471 + m.x971 == 1)
m.e466 = Constraint(expr= m.x472 + m.x972 == 1)
m.e467 = Constraint(expr= m.x473 + m.x973 == 1)
m.e468 = Constraint(expr= m.x474 + m.x974 == 1)
m.e469 = Constraint(expr= m.x475 + m.x975 == 1)
m.e470 = Constraint(expr= m.x476 + m.x976 == 1)
m.e471 = Constraint(expr= m.x477 + m.x977 == 1)
m.e472 = Constraint(expr= m.x478 + m.x978 == 1)
m.e473 = Constraint(expr= m.x479 + m.x979 == 1)
m.e474 = Constraint(expr= m.x480 + m.x980 == 1)
m.e475 = Constraint(expr= m.x481 + m.x981 == 1)
m.e476 = Constraint(expr= m.x482 + m.x982 == 1)
m.e477 = Constraint(expr= m.x483 + m.x983 == 1)
m.e478 = Constraint(expr= m.x484 + m.x984 == 1)
m.e479 = Constraint(expr= m.x485 + m.x985 == 1)
m.e480 = Constraint(expr= m.x486 + m.x986 == 1)
m.e481 = Constraint(expr= m.x487 + m.x987 == 1)
m.e482 = Constraint(expr= m.x488 + m.x988 == 1)
m.e483 = Constraint(expr= m.x489 + m.x989 == 1)
m.e484 = Constraint(expr= m.x490 + m.x990 == 1)
m.e485 = Constraint(expr= m.x491 + m.x991 == 1)
m.e486 = Constraint(expr= m.x492 + m.x992 == 1)
m.e487 = Constraint(expr= m.x493 + m.x993 == 1)
m.e488 = Constraint(expr= m.x494 + m.x994 == 1)
m.e489 = Constraint(expr= m.x495 + m.x995 == 1)
m.e490 = Constraint(expr= m.x496 + m.x996 == 1)
m.e491 = Constraint(expr= m.x497 + m.x997 == 1)
m.e492 = Constraint(expr= m.x498 + m.x998 == 1)
m.e493 = Constraint(expr= m.x499 + m.x999 == 1)
m.e494 = Constraint(expr= m.x500 + m.x1000 == 1)
m.e495 = Constraint(expr= m.x501 + m.x1001 == 1)
m.e496 = Constraint(expr= m.x502 + m.x1002 == 1)
m.e497 = Constraint(expr= m.x503 + m.x1003 == 1)
m.e498 = Constraint(expr= m.x504 + m.x1004 == 1)
m.e499 = Constraint(expr= m.x505 + m.x1005 == 1)
m.e500 = Constraint(expr= m.x506 + m.x1006 == 1)
