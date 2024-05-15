# NLP written by GAMS Convert at 05/15/24 11:39:08
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       100      100        0        0        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#       315      315        0        0        0        0        0        0
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
m.x307 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x308 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x309 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x310 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x311 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x312 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x313 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x314 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x315 = Var(within=Reals, bounds=(0,1), initialize=0)

m.obj = Objective(sense=minimize, expr= m.x16 * ((-0.17096518838221464 + m.x1)
    **2 + (-0.3539539554905695 + m.x2)**2 + (-0.19212984574956804 + m.x3)**2 +
    (-0.31093309922025913 + m.x4)**2 + (-0.8943387690720166 + m.x5)**2) + m.x17
    * ((-0.018828012355377455 + m.x1)**2 + (-0.7880981297934468 + m.x2)**2 + (
    -0.6996918925920503 + m.x3)**2 + (-0.028987063793156076 + m.x4)**2 + (
    -0.034447608478336944 + m.x5)**2) + m.x18 * ((-0.5573241467934712 + m.x1)**
    2 + (-0.897784854941806 + m.x2)**2 + (-0.4201677960470528 + m.x3)**2 + (
    -0.7280076372544978 + m.x4)**2 + (-0.8326343229990296 + m.x5)**2) + m.x19
    * ((-0.9898560699677655 + m.x1)**2 + (-0.6428545826724662 + m.x2)**2 + (
    -0.3732067332955028 + m.x3)**2 + (-0.7528251444378341 + m.x4)**2 + (
    -0.5970205099887091 + m.x5)**2) + m.x20 * ((-0.4734754317564236 + m.x1)**2
    + (-0.8347207850106029 + m.x2)**2 + (-0.42135161032518165 + m.x3)**2 + (
    -0.6441960132217912 + m.x4)**2 + (-0.7118006346496409 + m.x5)**2) + m.x21
    * ((-0.8781295008093332 + m.x1)**2 + (-0.1350742597800767 + m.x2)**2 + (
    -0.8259423512797124 + m.x3)**2 + (-0.9120256404102223 + m.x4)**2 + (
    -0.07482692922519063 + m.x5)**2) + m.x22 * ((-0.22105074665989766 + m.x1)**
    2 + (-0.5282495008475223 + m.x2)**2 + (-0.43057239753144083 + m.x3)**2 + (
    -0.891962723035 + m.x4)**2 + (-0.06570105867985598 + m.x5)**2) + m.x23 * ((
    -0.01593844738850414 + m.x1)**2 + (-0.8537832887898165 + m.x2)**2 + (
    -0.694829384684303 + m.x3)**2 + (-0.4786260720566252 + m.x4)**2 + (
    -0.2952082242771479 + m.x5)**2) + m.x24 * ((-0.5354933766160289 + m.x1)**2
    + (-0.8981336347295595 + m.x2)**2 + (-0.7403435788556595 + m.x3)**2 + (
    -0.4832569212868495 + m.x4)**2 + (-0.14216622760934627 + m.x5)**2) + m.x25
    * ((-0.33913429966639796 + m.x1)**2 + (-0.4639391435318122 + m.x2)**2 + (
    -0.7361773006616134 + m.x3)**2 + (-0.885016314090374 + m.x4)**2 + (
    -0.7344241656192795 + m.x5)**2) + m.x26 * ((-0.7718872374904752 + m.x1)**2
    + (-0.8601903318039009 + m.x2)**2 + (-0.5577505527271379 + m.x3)**2 + (
    -0.1702289344207658 + m.x4)**2 + (-0.927183278310071 + m.x5)**2) + m.x27 *
    ((-0.4815507586274824 + m.x1)**2 + (-0.8751920471506961 + m.x2)**2 + (
    -0.6151239164288107 + m.x3)**2 + (-0.5694516966089088 + m.x4)**2 + (
    -0.5017027514432043 + m.x5)**2) + m.x28 * ((-0.21683048854338138 + m.x1)**2
    + (-0.7723104873058465 + m.x2)**2 + (-0.11970279885982482 + m.x3)**2 + (
    -0.5790138957442343 + m.x4)**2 + (-0.17073936578279503 + m.x5)**2) + m.x29
    * ((-0.1669307223876363 + m.x1)**2 + (-0.659036089282866 + m.x2)**2 + (
    -0.9836819998680296 + m.x3)**2 + (-0.665100612892975 + m.x4)**2 + (
    -0.419768128555414 + m.x5)**2) + m.x30 * ((-0.2950812596152129 + m.x1)**2
    + (-0.8004991049482514 + m.x2)**2 + (-0.7206014257009317 + m.x3)**2 + (
    -0.7104749762968393 + m.x4)**2 + (-0.9272819300288276 + m.x5)**2) + m.x31
    * ((-0.25600874337592816 + m.x1)**2 + (-0.9587167956857237 + m.x2)**2 + (
    -0.39418152552956054 + m.x3)**2 + (-0.5662398831983819 + m.x4)**2 + (
    -0.04051246125944574 + m.x5)**2) + m.x32 * ((-0.6078951670837176 + m.x1)**2
    + (-0.8681542654162734 + m.x2)**2 + (-0.309925177056653 + m.x3)**2 + (
    -0.06837787686534591 + m.x4)**2 + (-0.527630236581432 + m.x5)**2) + m.x33
    * ((-0.7708371929465418 + m.x1)**2 + (-0.28628814034332417 + m.x2)**2 + (
    -0.2591022133181735 + m.x3)**2 + (-0.14276934459283064 + m.x4)**2 + (
    -0.5459059738021105 + m.x5)**2) + m.x34 * ((-0.6683158538450498 + m.x1)**2
    + (-0.4086103155648628 + m.x2)**2 + (-0.8943565585131906 + m.x3)**2 + (
    -0.5225892617659481 + m.x4)**2 + (-0.9350785739042261 + m.x5)**2) + m.x35
    * ((-0.6719085392531746 + m.x1)**2 + (-0.1595580192638525 + m.x2)**2 + (
    -0.7996368926355352 + m.x3)**2 + (-0.1170487194891564 + m.x4)**2 + (
    -0.8556385470684972 + m.x5)**2) + m.x36 * ((-0.5673763644241014 + m.x1)**2
    + (-0.12886518012400539 + m.x2)**2 + (-0.2976950509739491 + m.x3)**2 + (
    -0.35188031801434383 + m.x4)**2 + (-0.40235087115405954 + m.x5)**2) + m.x37
    * ((-0.24123138283819046 + m.x1)**2 + (-0.07969639495751146 + m.x2)**2 + (
    -0.28769126271160295 + m.x3)**2 + (-0.8430126815495746 + m.x4)**2 + (
    -0.4788854416921867 + m.x5)**2) + m.x38 * ((-0.33764655611727357 + m.x1)**2
    + (-0.18954859334554786 + m.x2)**2 + (-0.9791044601940113 + m.x3)**2 + (
    -0.018904413890015515 + m.x4)**2 + (-0.11475792017439879 + m.x5)**2) +
    m.x39 * ((-0.005654765265108552 + m.x1)**2 + (-0.6853106971417494 + m.x2)**
    2 + (-0.12455384772841716 + m.x3)**2 + (-0.06687957240368247 + m.x4)**2 + (
    -0.934150214848742 + m.x5)**2) + m.x40 * ((-0.1323884439723766 + m.x1)**2
    + (-0.4002255360844076 + m.x2)**2 + (-0.24066989364546 + m.x3)**2 + (
    -0.945366685362128 + m.x4)**2 + (-0.65053971319981 + m.x5)**2) + m.x41 * ((
    -0.26563188809602445 + m.x1)**2 + (-0.0328938955101008 + m.x2)**2 + (
    -0.14187150467912335 + m.x3)**2 + (-0.634991730787894 + m.x4)**2 + (
    -0.33973681934786837 + m.x5)**2) + m.x42 * ((-0.6550995080796584 + m.x1)**2
    + (-0.4656447339776387 + m.x2)**2 + (-0.4611025454092932 + m.x3)**2 + (
    -0.45959811280817553 + m.x4)**2 + (-0.34369088674503745 + m.x5)**2) + m.x43
    * ((-0.36116183026309645 + m.x1)**2 + (-0.1444276403258442 + m.x2)**2 + (
    -0.2922222809013374 + m.x3)**2 + (-0.8214266803118353 + m.x4)**2 + (
    -0.1792305896322195 + m.x5)**2) + m.x44 * ((-0.19773742916176262 + m.x1)**2
    + (-0.6417101368368979 + m.x2)**2 + (-0.6975286780303436 + m.x3)**2 + (
    -0.07146814534942347 + m.x4)**2 + (-0.7115759726559094 + m.x5)**2) + m.x45
    * ((-0.5228732762327684 + m.x1)**2 + (-0.9355763771287255 + m.x2)**2 + (
    -0.015977994016611374 + m.x3)**2 + (-0.20126940227556622 + m.x4)**2 + (
    -0.8333217160134744 + m.x5)**2) + m.x46 * ((-0.6481207461536673 + m.x1)**2
    + (-0.8833578204316509 + m.x2)**2 + (-0.32372701373603463 + m.x3)**2 + (
    -0.9757337987961168 + m.x4)**2 + (-0.40618630241322307 + m.x5)**2) + m.x47
    * ((-0.8803675998856332 + m.x1)**2 + (-0.03754825468665535 + m.x2)**2 + (
    -0.5372499977068816 + m.x3)**2 + (-0.36897287526065137 + m.x4)**2 + (
    -0.5083363567534844 + m.x5)**2) + m.x48 * ((-0.9083739075063708 + m.x1)**2
    + (-0.05921454037716023 + m.x2)**2 + (-0.6152689981846748 + m.x3)**2 + (
    -0.6412582931077976 + m.x4)**2 + (-0.7464633387457895 + m.x5)**2) + m.x49
    * ((-0.8771420385656269 + m.x1)**2 + (-0.3224137825046741 + m.x2)**2 + (
    -0.20501117185708329 + m.x3)**2 + (-0.2531106622854118 + m.x4)**2 + (
    -0.6560184288635266 + m.x5)**2) + m.x50 * ((-0.3430708584081765 + m.x1)**2
    + (-0.2686492674273111 + m.x2)**2 + (-0.09050046090329256 + m.x3)**2 + (
    -0.1537321695161551 + m.x4)**2 + (-0.7229937011651064 + m.x5)**2) + m.x51
    * ((-0.5920365965329157 + m.x1)**2 + (-0.48905522607855734 + m.x2)**2 + (
    -0.48295952954569 + m.x3)**2 + (-0.01915129814873251 + m.x4)**2 + (
    -0.995299737785757 + m.x5)**2) + m.x52 * ((-0.016064526958084024 + m.x1)**2
    + (-0.18034233085053286 + m.x2)**2 + (-0.2581396625917901 + m.x3)**2 + (
    -0.5036814451419693 + m.x4)**2 + (-0.8608747673883134 + m.x5)**2) + m.x53
    * ((-0.11045158992571158 + m.x1)**2 + (-0.3622497928230426 + m.x2)**2 + (
    -0.45952205728431283 + m.x3)**2 + (-0.0002471061856493817 + m.x4)**2 + (
    -0.757497030019815 + m.x5)**2) + m.x54 * ((-0.2695908127195076 + m.x1)**2
    + (-0.9377238001288556 + m.x2)**2 + (-0.9579075716037166 + m.x3)**2 + (
    -0.8957490843873757 + m.x4)**2 + (-0.5155981199297957 + m.x5)**2) + m.x55
    * ((-0.1996504177328149 + m.x1)**2 + (-0.0922668097451731 + m.x2)**2 + (
    -0.08911438778910774 + m.x3)**2 + (-0.8869692674970131 + m.x4)**2 + (
    -0.7514755222267686 + m.x5)**2) + m.x56 * ((-0.7172105707209647 + m.x1)**2
    + (-0.23244582628358135 + m.x2)**2 + (-0.15184477884001912 + m.x3)**2 + (
    -0.9545078066978725 + m.x4)**2 + (-0.7499904543899036 + m.x5)**2) + m.x57
    * ((-0.7132489235978078 + m.x1)**2 + (-0.9427565887470627 + m.x2)**2 + (
    -0.3960558700976604 + m.x3)**2 + (-0.6720409783910497 + m.x4)**2 + (
    -0.4670938392970526 + m.x5)**2) + m.x58 * ((-0.7397189086702454 + m.x1)**2
    + (-0.5229186910250551 + m.x2)**2 + (-0.6164411257495033 + m.x3)**2 + (
    -0.9401162132613612 + m.x4)**2 + (-0.37962647957961226 + m.x5)**2) + m.x59
    * ((-0.23014429727329677 + m.x1)**2 + (-0.9368004948448332 + m.x2)**2 + (
    -0.7294692942342981 + m.x3)**2 + (-0.5002098828954091 + m.x4)**2 + (
    -0.2127137051251451 + m.x5)**2) + m.x60 * ((-0.6485709496867776 + m.x1)**2
    + (-0.05284747687342617 + m.x2)**2 + (-0.5303355080923057 + m.x3)**2 + (
    -0.12555765265571328 + m.x4)**2 + (-0.7683088951884247 + m.x5)**2) + m.x61
    * ((-0.19020609944839817 + m.x1)**2 + (-0.4008706004716366 + m.x2)**2 + (
    -0.5407610291048321 + m.x3)**2 + (-0.8000549779835641 + m.x4)**2 + (
    -0.7754363156363911 + m.x5)**2) + m.x62 * ((-0.5953521882510386 + m.x1)**2
    + (-0.1323790589753776 + m.x2)**2 + (-0.674325798913709 + m.x3)**2 + (
    -0.6802743270136904 + m.x4)**2 + (-0.6883933097372661 + m.x5)**2) + m.x63
    * ((-0.0025493017098370263 + m.x1)**2 + (-0.5408609572630549 + m.x2)**2 +
    (-0.21056832640321543 + m.x3)**2 + (-0.031895597099028006 + m.x4)**2 + (
    -0.9985895136544211 + m.x5)**2) + m.x64 * ((-0.892560554551534 + m.x1)**2
    + (-0.40029433919218094 + m.x2)**2 + (-0.9701046642126923 + m.x3)**2 + (
    -0.5884238994048921 + m.x4)**2 + (-0.04492127078158925 + m.x5)**2) + m.x65
    * ((-0.9711532299798178 + m.x1)**2 + (-0.7241186041302273 + m.x2)**2 + (
    -0.9234336718225257 + m.x3)**2 + (-0.003826457398836247 + m.x4)**2 + (
    -0.3002972961786634 + m.x5)**2) + m.x66 * ((-0.15802096343337946 + m.x1)**2
    + (-0.4588369898224075 + m.x2)**2 + (-0.6765171167545904 + m.x3)**2 + (
    -0.17961210518975568 + m.x4)**2 + (-0.28429639692211905 + m.x5)**2) + m.x67
    * ((-0.1275427349595054 + m.x1)**2 + (-0.896178413967487 + m.x2)**2 + (
    -0.6857155096847544 + m.x3)**2 + (-0.20857237409144969 + m.x4)**2 + (
    -0.6593772608523063 + m.x5)**2) + m.x68 * ((-0.2518121214424135 + m.x1)**2
    + (-0.19634048416982464 + m.x2)**2 + (-0.2196605919477318 + m.x3)**2 + (
    -0.865875174260687 + m.x4)**2 + (-0.7362332660498551 + m.x5)**2) + m.x69 *
    ((-0.934483116823359 + m.x1)**2 + (-0.27077656486698387 + m.x2)**2 + (
    -0.13893908152756917 + m.x3)**2 + (-0.5480837183068329 + m.x4)**2 + (
    -0.8292665541893569 + m.x5)**2) + m.x70 * ((-0.5662267512605267 + m.x1)**2
    + (-0.5099376130769819 + m.x2)**2 + (-0.2783401593907391 + m.x3)**2 + (
    -0.8795236875792728 + m.x4)**2 + (-0.33198844026096497 + m.x5)**2) + m.x71
    * ((-0.11296146321165768 + m.x1)**2 + (-0.6813205222070685 + m.x2)**2 + (
    -0.22774906646074178 + m.x3)**2 + (-0.8784864778842033 + m.x4)**2 + (
    -0.8396296726708307 + m.x5)**2) + m.x72 * ((-0.15804249469097742 + m.x1)**2
    + (-0.15129563301525983 + m.x2)**2 + (-0.23341754619049626 + m.x3)**2 + (
    -0.7769582120439635 + m.x4)**2 + (-0.5384317246672141 + m.x5)**2) + m.x73
    * ((-0.5673150459473091 + m.x1)**2 + (-0.05014149052835315 + m.x2)**2 + (
    -0.17148121842456865 + m.x3)**2 + (-0.2810141473189889 + m.x4)**2 + (
    -0.9529181159762178 + m.x5)**2) + m.x74 * ((-0.2848837563876002 + m.x1)**2
    + (-0.8045194213858222 + m.x2)**2 + (-0.5682719027595411 + m.x3)**2 + (
    -0.6911634954580173 + m.x4)**2 + (-0.7839810486640113 + m.x5)**2) + m.x75
    * ((-0.5262875594913442 + m.x1)**2 + (-0.3665539509664488 + m.x2)**2 + (
    -0.37305902801355184 + m.x3)**2 + (-0.15221811233372107 + m.x4)**2 + (
    -0.8260586045664113 + m.x5)**2) + m.x76 * ((-0.16936346676074598 + m.x1)**2
    + (-0.8061630890365296 + m.x2)**2 + (-0.46125767117343186 + m.x3)**2 + (
    -0.9633530374089155 + m.x4)**2 + (-0.39455433477142554 + m.x5)**2) + m.x77
    * ((-0.04720272980003026 + m.x1)**2 + (-0.5423515001796103 + m.x2)**2 + (
    -0.6476785137633218 + m.x3)**2 + (-0.9771678211855662 + m.x4)**2 + (
    -0.09890495615065897 + m.x5)**2) + m.x78 * ((-0.7744956022252439 + m.x1)**2
    + (-0.8375885312694634 + m.x2)**2 + (-0.5467762179494536 + m.x3)**2 + (
    -0.8465780784820106 + m.x4)**2 + (-0.5651623293818131 + m.x5)**2) + m.x79
    * ((-0.9883458791190726 + m.x1)**2 + (-0.78960766333768 + m.x2)**2 + (
    -0.8907423797504631 + m.x3)**2 + (-0.5609054564815562 + m.x4)**2 + (
    -0.11178841876855738 + m.x5)**2) + m.x80 * ((-0.41454744963447077 + m.x1)**
    2 + (-0.8962451223260787 + m.x2)**2 + (-0.6225912810529636 + m.x3)**2 + (
    -0.42711413408897947 + m.x4)**2 + (-0.42194769116734065 + m.x5)**2) + m.x81
    * ((-0.38705619554376947 + m.x1)**2 + (-0.28436641527015727 + m.x2)**2 + (
    -0.28962805588226503 + m.x3)**2 + (-0.019398816297398036 + m.x4)**2 + (
    -0.43974457277505385 + m.x5)**2) + m.x82 * ((-0.46045133836211705 + m.x1)**
    2 + (-0.3178908083894423 + m.x2)**2 + (-0.9107204847423361 + m.x3)**2 + (
    -0.024132158913902413 + m.x4)**2 + (-0.850132577654732 + m.x5)**2) + m.x83
    * ((-0.8976765685484652 + m.x1)**2 + (-0.7980597430245149 + m.x2)**2 + (
    -0.348193168299762 + m.x3)**2 + (-0.6420465325576905 + m.x4)**2 + (
    -0.6796812519179917 + m.x5)**2) + m.x84 * ((-0.15285846774564793 + m.x1)**2
    + (-0.4347159732826844 + m.x2)**2 + (-0.8316008068895342 + m.x3)**2 + (
    -0.8965273852203728 + m.x4)**2 + (-0.9912538972487986 + m.x5)**2) + m.x85
    * ((-0.5369883922939439 + m.x1)**2 + (-0.4667840512773145 + m.x2)**2 + (
    -0.09728386761736485 + m.x3)**2 + (-0.7392757773313592 + m.x4)**2 + (
    -0.13153034052076962 + m.x5)**2) + m.x86 * ((-0.5171601875396525 + m.x1)**2
    + (-0.6501055077806779 + m.x2)**2 + (-0.4738783294442884 + m.x3)**2 + (
    -0.3059905276444237 + m.x4)**2 + (-0.4655403665248422 + m.x5)**2) + m.x87
    * ((-0.38769522192282246 + m.x1)**2 + (-0.9889925696368229 + m.x2)**2 + (
    -0.02462276265854113 + m.x3)**2 + (-0.5533833006798677 + m.x4)**2 + (
    -0.9049316659882748 + m.x5)**2) + m.x88 * ((-0.6476766247522808 + m.x1)**2
    + (-0.48861089343022013 + m.x2)**2 + (-0.4222074787200718 + m.x3)**2 + (
    -0.3336931215925991 + m.x4)**2 + (-0.2256832722919292 + m.x5)**2) + m.x89
    * ((-0.7074126149862657 + m.x1)**2 + (-0.24826058840938114 + m.x2)**2 + (
    -0.935855008312046 + m.x3)**2 + (-0.4531363616293268 + m.x4)**2 + (
    -0.2916105761611406 + m.x5)**2) + m.x90 * ((-0.14641966747166446 + m.x1)**2
    + (-0.2788408089755944 + m.x2)**2 + (-0.5445004171692817 + m.x3)**2 + (
    -0.7776763802122033 + m.x4)**2 + (-0.5886958457853472 + m.x5)**2) + m.x91
    * ((-0.22535164416260256 + m.x1)**2 + (-0.8648957992131536 + m.x2)**2 + (
    -0.31409985209738056 + m.x3)**2 + (-0.38674349351260584 + m.x4)**2 + (
    -0.9278581053708341 + m.x5)**2) + m.x92 * ((-0.6984113442379634 + m.x1)**2
    + (-0.5880319612907634 + m.x2)**2 + (-0.7055183537964272 + m.x3)**2 + (
    -0.052288634884028795 + m.x4)**2 + (-0.9540221980524576 + m.x5)**2) + m.x93
    * ((-0.6525901987545907 + m.x1)**2 + (-0.6324492441244804 + m.x2)**2 + (
    -0.41138748171911876 + m.x3)**2 + (-0.3346719309177193 + m.x4)**2 + (
    -0.16814397167586703 + m.x5)**2) + m.x94 * ((-0.967047497872221 + m.x1)**2
    + (-0.18063656917774573 + m.x2)**2 + (-0.2400182048559567 + m.x3)**2 + (
    -0.6691034304335645 + m.x4)**2 + (-0.5203600552914871 + m.x5)**2) + m.x95
    * ((-0.5133995855393014 + m.x1)**2 + (-0.682357221251084 + m.x2)**2 + (
    -0.22915213911098808 + m.x3)**2 + (-0.03240517485202765 + m.x4)**2 + (
    -0.30169291229505235 + m.x5)**2) + m.x96 * ((-0.5209867319058553 + m.x1)**2
    + (-0.4556272113241485 + m.x2)**2 + (-0.9348398039566677 + m.x3)**2 + (
    -0.4769297195138824 + m.x4)**2 + (-0.5441271791767697 + m.x5)**2) + m.x97
    * ((-0.05968232483167746 + m.x1)**2 + (-0.4047870938674545 + m.x2)**2 + (
    -0.5094808400454084 + m.x3)**2 + (-0.5133405099339715 + m.x4)**2 + (
    -0.8694173637603428 + m.x5)**2) + m.x98 * ((-0.7069125249619734 + m.x1)**2
    + (-0.7805582252528287 + m.x2)**2 + (-0.3622713115889995 + m.x3)**2 + (
    -0.18641714280195076 + m.x4)**2 + (-0.13146290481233758 + m.x5)**2) + m.x99
    * ((-0.6988866065066833 + m.x1)**2 + (-0.45397288260266866 + m.x2)**2 + (
    -0.45859107895122997 + m.x3)**2 + (-0.05137579962338035 + m.x4)**2 + (
    -0.04592955703454393 + m.x5)**2) + m.x100 * ((-0.2521200382154474 + m.x1)**
    2 + (-0.6536293489021203 + m.x2)**2 + (-0.5192181028685813 + m.x3)**2 + (
    -0.20358265360251637 + m.x4)**2 + (-0.05678264541333178 + m.x5)**2) +
    m.x101 * ((-0.7359000712721689 + m.x1)**2 + (-0.5285245765765676 + m.x2)**2
    + (-0.783746106047006 + m.x3)**2 + (-0.2072423999303571 + m.x4)**2 + (
    -0.9345165540918818 + m.x5)**2) + m.x102 * ((-0.0676233453727606 + m.x1)**2
    + (-0.15045515445014457 + m.x2)**2 + (-0.3631523266765533 + m.x3)**2 + (
    -0.06793304154668878 + m.x4)**2 + (-0.9177903450542778 + m.x5)**2) + m.x103
    * ((-0.9218805175952314 + m.x1)**2 + (-0.7879207544431588 + m.x2)**2 + (
    -0.6131320375628063 + m.x3)**2 + (-0.9794197292428298 + m.x4)**2 + (
    -0.6731862091841032 + m.x5)**2) + m.x104 * ((-0.5488460632188782 + m.x1)**2
    + (-0.8660152527377067 + m.x2)**2 + (-0.697256474689279 + m.x3)**2 + (
    -0.7403125785102036 + m.x4)**2 + (-0.9230110595772295 + m.x5)**2) + m.x105
    * ((-0.03349799947042298 + m.x1)**2 + (-0.013311552955958983 + m.x2)**2 +
    (-0.64790084232628 + m.x3)**2 + (-0.027327006271035903 + m.x4)**2 + (
    -0.45800635737351614 + m.x5)**2) + m.x106 * ((-0.3787875046692417 + m.x1)**
    2 + (-0.7756927089046994 + m.x2)**2 + (-0.08102978802889482 + m.x3)**2 + (
    -0.6885140630996159 + m.x4)**2 + (-0.258837614057293 + m.x5)**2) + m.x107
    * ((-0.926549979364291 + m.x1)**2 + (-0.6576775076711792 + m.x2)**2 + (
    -0.7185667900619702 + m.x3)**2 + (-0.8393281555178195 + m.x4)**2 + (
    -0.8790478271287436 + m.x5)**2) + m.x108 * ((-0.8538536880933677 + m.x1)**2
    + (-0.41093785441645236 + m.x2)**2 + (-0.821623842184094 + m.x3)**2 + (
    -0.3479518255783647 + m.x4)**2 + (-0.7092095860729987 + m.x5)**2) + m.x109
    * ((-0.36696518655512345 + m.x1)**2 + (-0.20091071029318852 + m.x2)**2 + (
    -0.077731695458928 + m.x3)**2 + (-0.5169327130336349 + m.x4)**2 + (
    -0.933512225646472 + m.x5)**2) + m.x110 * ((-0.12535873106543383 + m.x1)**2
    + (-0.20807091090575502 + m.x2)**2 + (-0.1737536300614485 + m.x3)**2 + (
    -0.9634306672730328 + m.x4)**2 + (-0.9058308480768769 + m.x5)**2) + m.x111
    * ((-0.1853802586369372 + m.x1)**2 + (-0.006662572599986594 + m.x2)**2 + (
    -0.010905690589545047 + m.x3)**2 + (-0.14902785082635217 + m.x4)**2 + (
    -0.22770558623177606 + m.x5)**2) + m.x112 * ((-0.4633514401824739 + m.x1)**
    2 + (-0.6547129104209288 + m.x2)**2 + (-0.5099212885026749 + m.x3)**2 + (
    -0.797446966803318 + m.x4)**2 + (-0.2962748229669455 + m.x5)**2) + m.x113
    * ((-0.36278221024643986 + m.x1)**2 + (-0.3277254622076904 + m.x2)**2 + (
    -0.7995480920087982 + m.x3)**2 + (-0.5823823799369167 + m.x4)**2 + (
    -0.880766278018624 + m.x5)**2) + m.x114 * ((-0.3223606530293073 + m.x1)**2
    + (-0.3211031767538892 + m.x2)**2 + (-0.8703147018545497 + m.x3)**2 + (
    -0.11319702691533051 + m.x4)**2 + (-0.16343459625058143 + m.x5)**2) +
    m.x115 * ((-0.7686159036050828 + m.x1)**2 + (-0.4198142721548951 + m.x2)**2
    + (-0.42491506406704316 + m.x3)**2 + (-0.45957758374218605 + m.x4)**2 + (
    -0.01631022121777903 + m.x5)**2) + m.x116 * ((-0.17096518838221464 + m.x6)
    **2 + (-0.3539539554905695 + m.x7)**2 + (-0.19212984574956804 + m.x8)**2 +
    (-0.31093309922025913 + m.x9)**2 + (-0.8943387690720166 + m.x10)**2) +
    m.x117 * ((-0.018828012355377455 + m.x6)**2 + (-0.7880981297934468 + m.x7)
    **2 + (-0.6996918925920503 + m.x8)**2 + (-0.028987063793156076 + m.x9)**2
    + (-0.034447608478336944 + m.x10)**2) + m.x118 * ((-0.5573241467934712 +
    m.x6)**2 + (-0.897784854941806 + m.x7)**2 + (-0.4201677960470528 + m.x8)**2
    + (-0.7280076372544978 + m.x9)**2 + (-0.8326343229990296 + m.x10)**2) +
    m.x119 * ((-0.9898560699677655 + m.x6)**2 + (-0.6428545826724662 + m.x7)**2
    + (-0.3732067332955028 + m.x8)**2 + (-0.7528251444378341 + m.x9)**2 + (
    -0.5970205099887091 + m.x10)**2) + m.x120 * ((-0.4734754317564236 + m.x6)**
    2 + (-0.8347207850106029 + m.x7)**2 + (-0.42135161032518165 + m.x8)**2 + (
    -0.6441960132217912 + m.x9)**2 + (-0.7118006346496409 + m.x10)**2) + m.x121
    * ((-0.8781295008093332 + m.x6)**2 + (-0.1350742597800767 + m.x7)**2 + (
    -0.8259423512797124 + m.x8)**2 + (-0.9120256404102223 + m.x9)**2 + (
    -0.07482692922519063 + m.x10)**2) + m.x122 * ((-0.22105074665989766 + m.x6)
    **2 + (-0.5282495008475223 + m.x7)**2 + (-0.43057239753144083 + m.x8)**2 +
    (-0.891962723035 + m.x9)**2 + (-0.06570105867985598 + m.x10)**2) + m.x123
    * ((-0.01593844738850414 + m.x6)**2 + (-0.8537832887898165 + m.x7)**2 + (
    -0.694829384684303 + m.x8)**2 + (-0.4786260720566252 + m.x9)**2 + (
    -0.2952082242771479 + m.x10)**2) + m.x124 * ((-0.5354933766160289 + m.x6)**
    2 + (-0.8981336347295595 + m.x7)**2 + (-0.7403435788556595 + m.x8)**2 + (
    -0.4832569212868495 + m.x9)**2 + (-0.14216622760934627 + m.x10)**2) +
    m.x125 * ((-0.33913429966639796 + m.x6)**2 + (-0.4639391435318122 + m.x7)**
    2 + (-0.7361773006616134 + m.x8)**2 + (-0.885016314090374 + m.x9)**2 + (
    -0.7344241656192795 + m.x10)**2) + m.x126 * ((-0.7718872374904752 + m.x6)**
    2 + (-0.8601903318039009 + m.x7)**2 + (-0.5577505527271379 + m.x8)**2 + (
    -0.1702289344207658 + m.x9)**2 + (-0.927183278310071 + m.x10)**2) + m.x127
    * ((-0.4815507586274824 + m.x6)**2 + (-0.8751920471506961 + m.x7)**2 + (
    -0.6151239164288107 + m.x8)**2 + (-0.5694516966089088 + m.x9)**2 + (
    -0.5017027514432043 + m.x10)**2) + m.x128 * ((-0.21683048854338138 + m.x6)
    **2 + (-0.7723104873058465 + m.x7)**2 + (-0.11970279885982482 + m.x8)**2 +
    (-0.5790138957442343 + m.x9)**2 + (-0.17073936578279503 + m.x10)**2) +
    m.x129 * ((-0.1669307223876363 + m.x6)**2 + (-0.659036089282866 + m.x7)**2
    + (-0.9836819998680296 + m.x8)**2 + (-0.665100612892975 + m.x9)**2 + (
    -0.419768128555414 + m.x10)**2) + m.x130 * ((-0.2950812596152129 + m.x6)**2
    + (-0.8004991049482514 + m.x7)**2 + (-0.7206014257009317 + m.x8)**2 + (
    -0.7104749762968393 + m.x9)**2 + (-0.9272819300288276 + m.x10)**2) + m.x131
    * ((-0.25600874337592816 + m.x6)**2 + (-0.9587167956857237 + m.x7)**2 + (
    -0.39418152552956054 + m.x8)**2 + (-0.5662398831983819 + m.x9)**2 + (
    -0.04051246125944574 + m.x10)**2) + m.x132 * ((-0.6078951670837176 + m.x6)
    **2 + (-0.8681542654162734 + m.x7)**2 + (-0.309925177056653 + m.x8)**2 + (
    -0.06837787686534591 + m.x9)**2 + (-0.527630236581432 + m.x10)**2) + m.x133
    * ((-0.7708371929465418 + m.x6)**2 + (-0.28628814034332417 + m.x7)**2 + (
    -0.2591022133181735 + m.x8)**2 + (-0.14276934459283064 + m.x9)**2 + (
    -0.5459059738021105 + m.x10)**2) + m.x134 * ((-0.6683158538450498 + m.x6)**
    2 + (-0.4086103155648628 + m.x7)**2 + (-0.8943565585131906 + m.x8)**2 + (
    -0.5225892617659481 + m.x9)**2 + (-0.9350785739042261 + m.x10)**2) + m.x135
    * ((-0.6719085392531746 + m.x6)**2 + (-0.1595580192638525 + m.x7)**2 + (
    -0.7996368926355352 + m.x8)**2 + (-0.1170487194891564 + m.x9)**2 + (
    -0.8556385470684972 + m.x10)**2) + m.x136 * ((-0.5673763644241014 + m.x6)**
    2 + (-0.12886518012400539 + m.x7)**2 + (-0.2976950509739491 + m.x8)**2 + (
    -0.35188031801434383 + m.x9)**2 + (-0.40235087115405954 + m.x10)**2) +
    m.x137 * ((-0.24123138283819046 + m.x6)**2 + (-0.07969639495751146 + m.x7)
    **2 + (-0.28769126271160295 + m.x8)**2 + (-0.8430126815495746 + m.x9)**2 +
    (-0.4788854416921867 + m.x10)**2) + m.x138 * ((-0.33764655611727357 + m.x6)
    **2 + (-0.18954859334554786 + m.x7)**2 + (-0.9791044601940113 + m.x8)**2 +
    (-0.018904413890015515 + m.x9)**2 + (-0.11475792017439879 + m.x10)**2) +
    m.x139 * ((-0.005654765265108552 + m.x6)**2 + (-0.6853106971417494 + m.x7)
    **2 + (-0.12455384772841716 + m.x8)**2 + (-0.06687957240368247 + m.x9)**2
    + (-0.934150214848742 + m.x10)**2) + m.x140 * ((-0.1323884439723766 + m.x6)
    **2 + (-0.4002255360844076 + m.x7)**2 + (-0.24066989364546 + m.x8)**2 + (
    -0.945366685362128 + m.x9)**2 + (-0.65053971319981 + m.x10)**2) + m.x141 *
    ((-0.26563188809602445 + m.x6)**2 + (-0.0328938955101008 + m.x7)**2 + (
    -0.14187150467912335 + m.x8)**2 + (-0.634991730787894 + m.x9)**2 + (
    -0.33973681934786837 + m.x10)**2) + m.x142 * ((-0.6550995080796584 + m.x6)
    **2 + (-0.4656447339776387 + m.x7)**2 + (-0.4611025454092932 + m.x8)**2 + (
    -0.45959811280817553 + m.x9)**2 + (-0.34369088674503745 + m.x10)**2) +
    m.x143 * ((-0.36116183026309645 + m.x6)**2 + (-0.1444276403258442 + m.x7)**
    2 + (-0.2922222809013374 + m.x8)**2 + (-0.8214266803118353 + m.x9)**2 + (
    -0.1792305896322195 + m.x10)**2) + m.x144 * ((-0.19773742916176262 + m.x6)
    **2 + (-0.6417101368368979 + m.x7)**2 + (-0.6975286780303436 + m.x8)**2 + (
    -0.07146814534942347 + m.x9)**2 + (-0.7115759726559094 + m.x10)**2) +
    m.x145 * ((-0.5228732762327684 + m.x6)**2 + (-0.9355763771287255 + m.x7)**2
    + (-0.015977994016611374 + m.x8)**2 + (-0.20126940227556622 + m.x9)**2 + (
    -0.8333217160134744 + m.x10)**2) + m.x146 * ((-0.6481207461536673 + m.x6)**
    2 + (-0.8833578204316509 + m.x7)**2 + (-0.32372701373603463 + m.x8)**2 + (
    -0.9757337987961168 + m.x9)**2 + (-0.40618630241322307 + m.x10)**2) +
    m.x147 * ((-0.8803675998856332 + m.x6)**2 + (-0.03754825468665535 + m.x7)**
    2 + (-0.5372499977068816 + m.x8)**2 + (-0.36897287526065137 + m.x9)**2 + (
    -0.5083363567534844 + m.x10)**2) + m.x148 * ((-0.9083739075063708 + m.x6)**
    2 + (-0.05921454037716023 + m.x7)**2 + (-0.6152689981846748 + m.x8)**2 + (
    -0.6412582931077976 + m.x9)**2 + (-0.7464633387457895 + m.x10)**2) + m.x149
    * ((-0.8771420385656269 + m.x6)**2 + (-0.3224137825046741 + m.x7)**2 + (
    -0.20501117185708329 + m.x8)**2 + (-0.2531106622854118 + m.x9)**2 + (
    -0.6560184288635266 + m.x10)**2) + m.x150 * ((-0.3430708584081765 + m.x6)**
    2 + (-0.2686492674273111 + m.x7)**2 + (-0.09050046090329256 + m.x8)**2 + (
    -0.1537321695161551 + m.x9)**2 + (-0.7229937011651064 + m.x10)**2) + m.x151
    * ((-0.5920365965329157 + m.x6)**2 + (-0.48905522607855734 + m.x7)**2 + (
    -0.48295952954569 + m.x8)**2 + (-0.01915129814873251 + m.x9)**2 + (
    -0.995299737785757 + m.x10)**2) + m.x152 * ((-0.016064526958084024 + m.x6)
    **2 + (-0.18034233085053286 + m.x7)**2 + (-0.2581396625917901 + m.x8)**2 +
    (-0.5036814451419693 + m.x9)**2 + (-0.8608747673883134 + m.x10)**2) +
    m.x153 * ((-0.11045158992571158 + m.x6)**2 + (-0.3622497928230426 + m.x7)**
    2 + (-0.45952205728431283 + m.x8)**2 + (-0.0002471061856493817 + m.x9)**2
    + (-0.757497030019815 + m.x10)**2) + m.x154 * ((-0.2695908127195076 + m.x6)
    **2 + (-0.9377238001288556 + m.x7)**2 + (-0.9579075716037166 + m.x8)**2 + (
    -0.8957490843873757 + m.x9)**2 + (-0.5155981199297957 + m.x10)**2) + m.x155
    * ((-0.1996504177328149 + m.x6)**2 + (-0.0922668097451731 + m.x7)**2 + (
    -0.08911438778910774 + m.x8)**2 + (-0.8869692674970131 + m.x9)**2 + (
    -0.7514755222267686 + m.x10)**2) + m.x156 * ((-0.7172105707209647 + m.x6)**
    2 + (-0.23244582628358135 + m.x7)**2 + (-0.15184477884001912 + m.x8)**2 + (
    -0.9545078066978725 + m.x9)**2 + (-0.7499904543899036 + m.x10)**2) + m.x157
    * ((-0.7132489235978078 + m.x6)**2 + (-0.9427565887470627 + m.x7)**2 + (
    -0.3960558700976604 + m.x8)**2 + (-0.6720409783910497 + m.x9)**2 + (
    -0.4670938392970526 + m.x10)**2) + m.x158 * ((-0.7397189086702454 + m.x6)**
    2 + (-0.5229186910250551 + m.x7)**2 + (-0.6164411257495033 + m.x8)**2 + (
    -0.9401162132613612 + m.x9)**2 + (-0.37962647957961226 + m.x10)**2) +
    m.x159 * ((-0.23014429727329677 + m.x6)**2 + (-0.9368004948448332 + m.x7)**
    2 + (-0.7294692942342981 + m.x8)**2 + (-0.5002098828954091 + m.x9)**2 + (
    -0.2127137051251451 + m.x10)**2) + m.x160 * ((-0.6485709496867776 + m.x6)**
    2 + (-0.05284747687342617 + m.x7)**2 + (-0.5303355080923057 + m.x8)**2 + (
    -0.12555765265571328 + m.x9)**2 + (-0.7683088951884247 + m.x10)**2) +
    m.x161 * ((-0.19020609944839817 + m.x6)**2 + (-0.4008706004716366 + m.x7)**
    2 + (-0.5407610291048321 + m.x8)**2 + (-0.8000549779835641 + m.x9)**2 + (
    -0.7754363156363911 + m.x10)**2) + m.x162 * ((-0.5953521882510386 + m.x6)**
    2 + (-0.1323790589753776 + m.x7)**2 + (-0.674325798913709 + m.x8)**2 + (
    -0.6802743270136904 + m.x9)**2 + (-0.6883933097372661 + m.x10)**2) + m.x163
    * ((-0.0025493017098370263 + m.x6)**2 + (-0.5408609572630549 + m.x7)**2 +
    (-0.21056832640321543 + m.x8)**2 + (-0.031895597099028006 + m.x9)**2 + (
    -0.9985895136544211 + m.x10)**2) + m.x164 * ((-0.892560554551534 + m.x6)**2
    + (-0.40029433919218094 + m.x7)**2 + (-0.9701046642126923 + m.x8)**2 + (
    -0.5884238994048921 + m.x9)**2 + (-0.04492127078158925 + m.x10)**2) +
    m.x165 * ((-0.9711532299798178 + m.x6)**2 + (-0.7241186041302273 + m.x7)**2
    + (-0.9234336718225257 + m.x8)**2 + (-0.003826457398836247 + m.x9)**2 + (
    -0.3002972961786634 + m.x10)**2) + m.x166 * ((-0.15802096343337946 + m.x6)
    **2 + (-0.4588369898224075 + m.x7)**2 + (-0.6765171167545904 + m.x8)**2 + (
    -0.17961210518975568 + m.x9)**2 + (-0.28429639692211905 + m.x10)**2) +
    m.x167 * ((-0.1275427349595054 + m.x6)**2 + (-0.896178413967487 + m.x7)**2
    + (-0.6857155096847544 + m.x8)**2 + (-0.20857237409144969 + m.x9)**2 + (
    -0.6593772608523063 + m.x10)**2) + m.x168 * ((-0.2518121214424135 + m.x6)**
    2 + (-0.19634048416982464 + m.x7)**2 + (-0.2196605919477318 + m.x8)**2 + (
    -0.865875174260687 + m.x9)**2 + (-0.7362332660498551 + m.x10)**2) + m.x169
    * ((-0.934483116823359 + m.x6)**2 + (-0.27077656486698387 + m.x7)**2 + (
    -0.13893908152756917 + m.x8)**2 + (-0.5480837183068329 + m.x9)**2 + (
    -0.8292665541893569 + m.x10)**2) + m.x170 * ((-0.5662267512605267 + m.x6)**
    2 + (-0.5099376130769819 + m.x7)**2 + (-0.2783401593907391 + m.x8)**2 + (
    -0.8795236875792728 + m.x9)**2 + (-0.33198844026096497 + m.x10)**2) +
    m.x171 * ((-0.11296146321165768 + m.x6)**2 + (-0.6813205222070685 + m.x7)**
    2 + (-0.22774906646074178 + m.x8)**2 + (-0.8784864778842033 + m.x9)**2 + (
    -0.8396296726708307 + m.x10)**2) + m.x172 * ((-0.15804249469097742 + m.x6)
    **2 + (-0.15129563301525983 + m.x7)**2 + (-0.23341754619049626 + m.x8)**2
    + (-0.7769582120439635 + m.x9)**2 + (-0.5384317246672141 + m.x10)**2) +
    m.x173 * ((-0.5673150459473091 + m.x6)**2 + (-0.05014149052835315 + m.x7)**
    2 + (-0.17148121842456865 + m.x8)**2 + (-0.2810141473189889 + m.x9)**2 + (
    -0.9529181159762178 + m.x10)**2) + m.x174 * ((-0.2848837563876002 + m.x6)**
    2 + (-0.8045194213858222 + m.x7)**2 + (-0.5682719027595411 + m.x8)**2 + (
    -0.6911634954580173 + m.x9)**2 + (-0.7839810486640113 + m.x10)**2) + m.x175
    * ((-0.5262875594913442 + m.x6)**2 + (-0.3665539509664488 + m.x7)**2 + (
    -0.37305902801355184 + m.x8)**2 + (-0.15221811233372107 + m.x9)**2 + (
    -0.8260586045664113 + m.x10)**2) + m.x176 * ((-0.16936346676074598 + m.x6)
    **2 + (-0.8061630890365296 + m.x7)**2 + (-0.46125767117343186 + m.x8)**2 +
    (-0.9633530374089155 + m.x9)**2 + (-0.39455433477142554 + m.x10)**2) +
    m.x177 * ((-0.04720272980003026 + m.x6)**2 + (-0.5423515001796103 + m.x7)**
    2 + (-0.6476785137633218 + m.x8)**2 + (-0.9771678211855662 + m.x9)**2 + (
    -0.09890495615065897 + m.x10)**2) + m.x178 * ((-0.7744956022252439 + m.x6)
    **2 + (-0.8375885312694634 + m.x7)**2 + (-0.5467762179494536 + m.x8)**2 + (
    -0.8465780784820106 + m.x9)**2 + (-0.5651623293818131 + m.x10)**2) + m.x179
    * ((-0.9883458791190726 + m.x6)**2 + (-0.78960766333768 + m.x7)**2 + (
    -0.8907423797504631 + m.x8)**2 + (-0.5609054564815562 + m.x9)**2 + (
    -0.11178841876855738 + m.x10)**2) + m.x180 * ((-0.41454744963447077 + m.x6)
    **2 + (-0.8962451223260787 + m.x7)**2 + (-0.6225912810529636 + m.x8)**2 + (
    -0.42711413408897947 + m.x9)**2 + (-0.42194769116734065 + m.x10)**2) +
    m.x181 * ((-0.38705619554376947 + m.x6)**2 + (-0.28436641527015727 + m.x7)
    **2 + (-0.28962805588226503 + m.x8)**2 + (-0.019398816297398036 + m.x9)**2
    + (-0.43974457277505385 + m.x10)**2) + m.x182 * ((-0.46045133836211705 +
    m.x6)**2 + (-0.3178908083894423 + m.x7)**2 + (-0.9107204847423361 + m.x8)**
    2 + (-0.024132158913902413 + m.x9)**2 + (-0.850132577654732 + m.x10)**2) +
    m.x183 * ((-0.8976765685484652 + m.x6)**2 + (-0.7980597430245149 + m.x7)**2
    + (-0.348193168299762 + m.x8)**2 + (-0.6420465325576905 + m.x9)**2 + (
    -0.6796812519179917 + m.x10)**2) + m.x184 * ((-0.15285846774564793 + m.x6)
    **2 + (-0.4347159732826844 + m.x7)**2 + (-0.8316008068895342 + m.x8)**2 + (
    -0.8965273852203728 + m.x9)**2 + (-0.9912538972487986 + m.x10)**2) + m.x185
    * ((-0.5369883922939439 + m.x6)**2 + (-0.4667840512773145 + m.x7)**2 + (
    -0.09728386761736485 + m.x8)**2 + (-0.7392757773313592 + m.x9)**2 + (
    -0.13153034052076962 + m.x10)**2) + m.x186 * ((-0.5171601875396525 + m.x6)
    **2 + (-0.6501055077806779 + m.x7)**2 + (-0.4738783294442884 + m.x8)**2 + (
    -0.3059905276444237 + m.x9)**2 + (-0.4655403665248422 + m.x10)**2) + m.x187
    * ((-0.38769522192282246 + m.x6)**2 + (-0.9889925696368229 + m.x7)**2 + (
    -0.02462276265854113 + m.x8)**2 + (-0.5533833006798677 + m.x9)**2 + (
    -0.9049316659882748 + m.x10)**2) + m.x188 * ((-0.6476766247522808 + m.x6)**
    2 + (-0.48861089343022013 + m.x7)**2 + (-0.4222074787200718 + m.x8)**2 + (
    -0.3336931215925991 + m.x9)**2 + (-0.2256832722919292 + m.x10)**2) + m.x189
    * ((-0.7074126149862657 + m.x6)**2 + (-0.24826058840938114 + m.x7)**2 + (
    -0.935855008312046 + m.x8)**2 + (-0.4531363616293268 + m.x9)**2 + (
    -0.2916105761611406 + m.x10)**2) + m.x190 * ((-0.14641966747166446 + m.x6)
    **2 + (-0.2788408089755944 + m.x7)**2 + (-0.5445004171692817 + m.x8)**2 + (
    -0.7776763802122033 + m.x9)**2 + (-0.5886958457853472 + m.x10)**2) + m.x191
    * ((-0.22535164416260256 + m.x6)**2 + (-0.8648957992131536 + m.x7)**2 + (
    -0.31409985209738056 + m.x8)**2 + (-0.38674349351260584 + m.x9)**2 + (
    -0.9278581053708341 + m.x10)**2) + m.x192 * ((-0.6984113442379634 + m.x6)**
    2 + (-0.5880319612907634 + m.x7)**2 + (-0.7055183537964272 + m.x8)**2 + (
    -0.052288634884028795 + m.x9)**2 + (-0.9540221980524576 + m.x10)**2) +
    m.x193 * ((-0.6525901987545907 + m.x6)**2 + (-0.6324492441244804 + m.x7)**2
    + (-0.41138748171911876 + m.x8)**2 + (-0.3346719309177193 + m.x9)**2 + (
    -0.16814397167586703 + m.x10)**2) + m.x194 * ((-0.967047497872221 + m.x6)**
    2 + (-0.18063656917774573 + m.x7)**2 + (-0.2400182048559567 + m.x8)**2 + (
    -0.6691034304335645 + m.x9)**2 + (-0.5203600552914871 + m.x10)**2) + m.x195
    * ((-0.5133995855393014 + m.x6)**2 + (-0.682357221251084 + m.x7)**2 + (
    -0.22915213911098808 + m.x8)**2 + (-0.03240517485202765 + m.x9)**2 + (
    -0.30169291229505235 + m.x10)**2) + m.x196 * ((-0.5209867319058553 + m.x6)
    **2 + (-0.4556272113241485 + m.x7)**2 + (-0.9348398039566677 + m.x8)**2 + (
    -0.4769297195138824 + m.x9)**2 + (-0.5441271791767697 + m.x10)**2) + m.x197
    * ((-0.05968232483167746 + m.x6)**2 + (-0.4047870938674545 + m.x7)**2 + (
    -0.5094808400454084 + m.x8)**2 + (-0.5133405099339715 + m.x9)**2 + (
    -0.8694173637603428 + m.x10)**2) + m.x198 * ((-0.7069125249619734 + m.x6)**
    2 + (-0.7805582252528287 + m.x7)**2 + (-0.3622713115889995 + m.x8)**2 + (
    -0.18641714280195076 + m.x9)**2 + (-0.13146290481233758 + m.x10)**2) +
    m.x199 * ((-0.6988866065066833 + m.x6)**2 + (-0.45397288260266866 + m.x7)**
    2 + (-0.45859107895122997 + m.x8)**2 + (-0.05137579962338035 + m.x9)**2 + (
    -0.04592955703454393 + m.x10)**2) + m.x200 * ((-0.2521200382154474 + m.x6)
    **2 + (-0.6536293489021203 + m.x7)**2 + (-0.5192181028685813 + m.x8)**2 + (
    -0.20358265360251637 + m.x9)**2 + (-0.05678264541333178 + m.x10)**2) +
    m.x201 * ((-0.7359000712721689 + m.x6)**2 + (-0.5285245765765676 + m.x7)**2
    + (-0.783746106047006 + m.x8)**2 + (-0.2072423999303571 + m.x9)**2 + (
    -0.9345165540918818 + m.x10)**2) + m.x202 * ((-0.0676233453727606 + m.x6)**
    2 + (-0.15045515445014457 + m.x7)**2 + (-0.3631523266765533 + m.x8)**2 + (
    -0.06793304154668878 + m.x9)**2 + (-0.9177903450542778 + m.x10)**2) +
    m.x203 * ((-0.9218805175952314 + m.x6)**2 + (-0.7879207544431588 + m.x7)**2
    + (-0.6131320375628063 + m.x8)**2 + (-0.9794197292428298 + m.x9)**2 + (
    -0.6731862091841032 + m.x10)**2) + m.x204 * ((-0.5488460632188782 + m.x6)**
    2 + (-0.8660152527377067 + m.x7)**2 + (-0.697256474689279 + m.x8)**2 + (
    -0.7403125785102036 + m.x9)**2 + (-0.9230110595772295 + m.x10)**2) + m.x205
    * ((-0.03349799947042298 + m.x6)**2 + (-0.013311552955958983 + m.x7)**2 +
    (-0.64790084232628 + m.x8)**2 + (-0.027327006271035903 + m.x9)**2 + (
    -0.45800635737351614 + m.x10)**2) + m.x206 * ((-0.3787875046692417 + m.x6)
    **2 + (-0.7756927089046994 + m.x7)**2 + (-0.08102978802889482 + m.x8)**2 +
    (-0.6885140630996159 + m.x9)**2 + (-0.258837614057293 + m.x10)**2) + m.x207
    * ((-0.926549979364291 + m.x6)**2 + (-0.6576775076711792 + m.x7)**2 + (
    -0.7185667900619702 + m.x8)**2 + (-0.8393281555178195 + m.x9)**2 + (
    -0.8790478271287436 + m.x10)**2) + m.x208 * ((-0.8538536880933677 + m.x6)**
    2 + (-0.41093785441645236 + m.x7)**2 + (-0.821623842184094 + m.x8)**2 + (
    -0.3479518255783647 + m.x9)**2 + (-0.7092095860729987 + m.x10)**2) + m.x209
    * ((-0.36696518655512345 + m.x6)**2 + (-0.20091071029318852 + m.x7)**2 + (
    -0.077731695458928 + m.x8)**2 + (-0.5169327130336349 + m.x9)**2 + (
    -0.933512225646472 + m.x10)**2) + m.x210 * ((-0.12535873106543383 + m.x6)**
    2 + (-0.20807091090575502 + m.x7)**2 + (-0.1737536300614485 + m.x8)**2 + (
    -0.9634306672730328 + m.x9)**2 + (-0.9058308480768769 + m.x10)**2) + m.x211
    * ((-0.1853802586369372 + m.x6)**2 + (-0.006662572599986594 + m.x7)**2 + (
    -0.010905690589545047 + m.x8)**2 + (-0.14902785082635217 + m.x9)**2 + (
    -0.22770558623177606 + m.x10)**2) + m.x212 * ((-0.4633514401824739 + m.x6)
    **2 + (-0.6547129104209288 + m.x7)**2 + (-0.5099212885026749 + m.x8)**2 + (
    -0.797446966803318 + m.x9)**2 + (-0.2962748229669455 + m.x10)**2) + m.x213
    * ((-0.36278221024643986 + m.x6)**2 + (-0.3277254622076904 + m.x7)**2 + (
    -0.7995480920087982 + m.x8)**2 + (-0.5823823799369167 + m.x9)**2 + (
    -0.880766278018624 + m.x10)**2) + m.x214 * ((-0.3223606530293073 + m.x6)**2
    + (-0.3211031767538892 + m.x7)**2 + (-0.8703147018545497 + m.x8)**2 + (
    -0.11319702691533051 + m.x9)**2 + (-0.16343459625058143 + m.x10)**2) +
    m.x215 * ((-0.7686159036050828 + m.x6)**2 + (-0.4198142721548951 + m.x7)**2
    + (-0.42491506406704316 + m.x8)**2 + (-0.45957758374218605 + m.x9)**2 + (
    -0.01631022121777903 + m.x10)**2) + m.x216 * ((-0.17096518838221464 + m.x11)
    **2 + (-0.3539539554905695 + m.x12)**2 + (-0.19212984574956804 + m.x13)**2
    + (-0.31093309922025913 + m.x14)**2 + (-0.8943387690720166 + m.x15)**2) +
    m.x217 * ((-0.018828012355377455 + m.x11)**2 + (-0.7880981297934468 + m.x12)
    **2 + (-0.6996918925920503 + m.x13)**2 + (-0.028987063793156076 + m.x14)**2
    + (-0.034447608478336944 + m.x15)**2) + m.x218 * ((-0.5573241467934712 +
    m.x11)**2 + (-0.897784854941806 + m.x12)**2 + (-0.4201677960470528 + m.x13)
    **2 + (-0.7280076372544978 + m.x14)**2 + (-0.8326343229990296 + m.x15)**2)
    + m.x219 * ((-0.9898560699677655 + m.x11)**2 + (-0.6428545826724662 +
    m.x12)**2 + (-0.3732067332955028 + m.x13)**2 + (-0.7528251444378341 + m.x14)
    **2 + (-0.5970205099887091 + m.x15)**2) + m.x220 * ((-0.4734754317564236 +
    m.x11)**2 + (-0.8347207850106029 + m.x12)**2 + (-0.42135161032518165 +
    m.x13)**2 + (-0.6441960132217912 + m.x14)**2 + (-0.7118006346496409 + m.x15)
    **2) + m.x221 * ((-0.8781295008093332 + m.x11)**2 + (-0.1350742597800767 +
    m.x12)**2 + (-0.8259423512797124 + m.x13)**2 + (-0.9120256404102223 + m.x14)
    **2 + (-0.07482692922519063 + m.x15)**2) + m.x222 * ((-0.22105074665989766
    + m.x11)**2 + (-0.5282495008475223 + m.x12)**2 + (-0.43057239753144083 +
    m.x13)**2 + (-0.891962723035 + m.x14)**2 + (-0.06570105867985598 + m.x15)**
    2) + m.x223 * ((-0.01593844738850414 + m.x11)**2 + (-0.8537832887898165 +
    m.x12)**2 + (-0.694829384684303 + m.x13)**2 + (-0.4786260720566252 + m.x14)
    **2 + (-0.2952082242771479 + m.x15)**2) + m.x224 * ((-0.5354933766160289 +
    m.x11)**2 + (-0.8981336347295595 + m.x12)**2 + (-0.7403435788556595 + m.x13)
    **2 + (-0.4832569212868495 + m.x14)**2 + (-0.14216622760934627 + m.x15)**2)
    + m.x225 * ((-0.33913429966639796 + m.x11)**2 + (-0.4639391435318122 +
    m.x12)**2 + (-0.7361773006616134 + m.x13)**2 + (-0.885016314090374 + m.x14)
    **2 + (-0.7344241656192795 + m.x15)**2) + m.x226 * ((-0.7718872374904752 +
    m.x11)**2 + (-0.8601903318039009 + m.x12)**2 + (-0.5577505527271379 + m.x13)
    **2 + (-0.1702289344207658 + m.x14)**2 + (-0.927183278310071 + m.x15)**2)
    + m.x227 * ((-0.4815507586274824 + m.x11)**2 + (-0.8751920471506961 +
    m.x12)**2 + (-0.6151239164288107 + m.x13)**2 + (-0.5694516966089088 + m.x14)
    **2 + (-0.5017027514432043 + m.x15)**2) + m.x228 * ((-0.21683048854338138
    + m.x11)**2 + (-0.7723104873058465 + m.x12)**2 + (-0.11970279885982482 +
    m.x13)**2 + (-0.5790138957442343 + m.x14)**2 + (-0.17073936578279503 +
    m.x15)**2) + m.x229 * ((-0.1669307223876363 + m.x11)**2 + (
    -0.659036089282866 + m.x12)**2 + (-0.9836819998680296 + m.x13)**2 + (
    -0.665100612892975 + m.x14)**2 + (-0.419768128555414 + m.x15)**2) + m.x230
    * ((-0.2950812596152129 + m.x11)**2 + (-0.8004991049482514 + m.x12)**2 + (
    -0.7206014257009317 + m.x13)**2 + (-0.7104749762968393 + m.x14)**2 + (
    -0.9272819300288276 + m.x15)**2) + m.x231 * ((-0.25600874337592816 + m.x11)
    **2 + (-0.9587167956857237 + m.x12)**2 + (-0.39418152552956054 + m.x13)**2
    + (-0.5662398831983819 + m.x14)**2 + (-0.04051246125944574 + m.x15)**2) +
    m.x232 * ((-0.6078951670837176 + m.x11)**2 + (-0.8681542654162734 + m.x12)
    **2 + (-0.309925177056653 + m.x13)**2 + (-0.06837787686534591 + m.x14)**2
    + (-0.527630236581432 + m.x15)**2) + m.x233 * ((-0.7708371929465418 +
    m.x11)**2 + (-0.28628814034332417 + m.x12)**2 + (-0.2591022133181735 +
    m.x13)**2 + (-0.14276934459283064 + m.x14)**2 + (-0.5459059738021105 +
    m.x15)**2) + m.x234 * ((-0.6683158538450498 + m.x11)**2 + (
    -0.4086103155648628 + m.x12)**2 + (-0.8943565585131906 + m.x13)**2 + (
    -0.5225892617659481 + m.x14)**2 + (-0.9350785739042261 + m.x15)**2) +
    m.x235 * ((-0.6719085392531746 + m.x11)**2 + (-0.1595580192638525 + m.x12)
    **2 + (-0.7996368926355352 + m.x13)**2 + (-0.1170487194891564 + m.x14)**2
    + (-0.8556385470684972 + m.x15)**2) + m.x236 * ((-0.5673763644241014 +
    m.x11)**2 + (-0.12886518012400539 + m.x12)**2 + (-0.2976950509739491 +
    m.x13)**2 + (-0.35188031801434383 + m.x14)**2 + (-0.40235087115405954 +
    m.x15)**2) + m.x237 * ((-0.24123138283819046 + m.x11)**2 + (
    -0.07969639495751146 + m.x12)**2 + (-0.28769126271160295 + m.x13)**2 + (
    -0.8430126815495746 + m.x14)**2 + (-0.4788854416921867 + m.x15)**2) +
    m.x238 * ((-0.33764655611727357 + m.x11)**2 + (-0.18954859334554786 + m.x12)
    **2 + (-0.9791044601940113 + m.x13)**2 + (-0.018904413890015515 + m.x14)**2
    + (-0.11475792017439879 + m.x15)**2) + m.x239 * ((-0.005654765265108552 +
    m.x11)**2 + (-0.6853106971417494 + m.x12)**2 + (-0.12455384772841716 +
    m.x13)**2 + (-0.06687957240368247 + m.x14)**2 + (-0.934150214848742 + m.x15)
    **2) + m.x240 * ((-0.1323884439723766 + m.x11)**2 + (-0.4002255360844076 +
    m.x12)**2 + (-0.24066989364546 + m.x13)**2 + (-0.945366685362128 + m.x14)**
    2 + (-0.65053971319981 + m.x15)**2) + m.x241 * ((-0.26563188809602445 +
    m.x11)**2 + (-0.0328938955101008 + m.x12)**2 + (-0.14187150467912335 +
    m.x13)**2 + (-0.634991730787894 + m.x14)**2 + (-0.33973681934786837 + m.x15)
    **2) + m.x242 * ((-0.6550995080796584 + m.x11)**2 + (-0.4656447339776387 +
    m.x12)**2 + (-0.4611025454092932 + m.x13)**2 + (-0.45959811280817553 +
    m.x14)**2 + (-0.34369088674503745 + m.x15)**2) + m.x243 * ((
    -0.36116183026309645 + m.x11)**2 + (-0.1444276403258442 + m.x12)**2 + (
    -0.2922222809013374 + m.x13)**2 + (-0.8214266803118353 + m.x14)**2 + (
    -0.1792305896322195 + m.x15)**2) + m.x244 * ((-0.19773742916176262 + m.x11)
    **2 + (-0.6417101368368979 + m.x12)**2 + (-0.6975286780303436 + m.x13)**2
    + (-0.07146814534942347 + m.x14)**2 + (-0.7115759726559094 + m.x15)**2) +
    m.x245 * ((-0.5228732762327684 + m.x11)**2 + (-0.9355763771287255 + m.x12)
    **2 + (-0.015977994016611374 + m.x13)**2 + (-0.20126940227556622 + m.x14)**
    2 + (-0.8333217160134744 + m.x15)**2) + m.x246 * ((-0.6481207461536673 +
    m.x11)**2 + (-0.8833578204316509 + m.x12)**2 + (-0.32372701373603463 +
    m.x13)**2 + (-0.9757337987961168 + m.x14)**2 + (-0.40618630241322307 +
    m.x15)**2) + m.x247 * ((-0.8803675998856332 + m.x11)**2 + (
    -0.03754825468665535 + m.x12)**2 + (-0.5372499977068816 + m.x13)**2 + (
    -0.36897287526065137 + m.x14)**2 + (-0.5083363567534844 + m.x15)**2) +
    m.x248 * ((-0.9083739075063708 + m.x11)**2 + (-0.05921454037716023 + m.x12)
    **2 + (-0.6152689981846748 + m.x13)**2 + (-0.6412582931077976 + m.x14)**2
    + (-0.7464633387457895 + m.x15)**2) + m.x249 * ((-0.8771420385656269 +
    m.x11)**2 + (-0.3224137825046741 + m.x12)**2 + (-0.20501117185708329 +
    m.x13)**2 + (-0.2531106622854118 + m.x14)**2 + (-0.6560184288635266 + m.x15)
    **2) + m.x250 * ((-0.3430708584081765 + m.x11)**2 + (-0.2686492674273111 +
    m.x12)**2 + (-0.09050046090329256 + m.x13)**2 + (-0.1537321695161551 +
    m.x14)**2 + (-0.7229937011651064 + m.x15)**2) + m.x251 * ((
    -0.5920365965329157 + m.x11)**2 + (-0.48905522607855734 + m.x12)**2 + (
    -0.48295952954569 + m.x13)**2 + (-0.01915129814873251 + m.x14)**2 + (
    -0.995299737785757 + m.x15)**2) + m.x252 * ((-0.016064526958084024 + m.x11)
    **2 + (-0.18034233085053286 + m.x12)**2 + (-0.2581396625917901 + m.x13)**2
    + (-0.5036814451419693 + m.x14)**2 + (-0.8608747673883134 + m.x15)**2) +
    m.x253 * ((-0.11045158992571158 + m.x11)**2 + (-0.3622497928230426 + m.x12)
    **2 + (-0.45952205728431283 + m.x13)**2 + (-0.0002471061856493817 + m.x14)
    **2 + (-0.757497030019815 + m.x15)**2) + m.x254 * ((-0.2695908127195076 +
    m.x11)**2 + (-0.9377238001288556 + m.x12)**2 + (-0.9579075716037166 + m.x13)
    **2 + (-0.8957490843873757 + m.x14)**2 + (-0.5155981199297957 + m.x15)**2)
    + m.x255 * ((-0.1996504177328149 + m.x11)**2 + (-0.0922668097451731 +
    m.x12)**2 + (-0.08911438778910774 + m.x13)**2 + (-0.8869692674970131 +
    m.x14)**2 + (-0.7514755222267686 + m.x15)**2) + m.x256 * ((
    -0.7172105707209647 + m.x11)**2 + (-0.23244582628358135 + m.x12)**2 + (
    -0.15184477884001912 + m.x13)**2 + (-0.9545078066978725 + m.x14)**2 + (
    -0.7499904543899036 + m.x15)**2) + m.x257 * ((-0.7132489235978078 + m.x11)
    **2 + (-0.9427565887470627 + m.x12)**2 + (-0.3960558700976604 + m.x13)**2
    + (-0.6720409783910497 + m.x14)**2 + (-0.4670938392970526 + m.x15)**2) +
    m.x258 * ((-0.7397189086702454 + m.x11)**2 + (-0.5229186910250551 + m.x12)
    **2 + (-0.6164411257495033 + m.x13)**2 + (-0.9401162132613612 + m.x14)**2
    + (-0.37962647957961226 + m.x15)**2) + m.x259 * ((-0.23014429727329677 +
    m.x11)**2 + (-0.9368004948448332 + m.x12)**2 + (-0.7294692942342981 + m.x13)
    **2 + (-0.5002098828954091 + m.x14)**2 + (-0.2127137051251451 + m.x15)**2)
    + m.x260 * ((-0.6485709496867776 + m.x11)**2 + (-0.05284747687342617 +
    m.x12)**2 + (-0.5303355080923057 + m.x13)**2 + (-0.12555765265571328 +
    m.x14)**2 + (-0.7683088951884247 + m.x15)**2) + m.x261 * ((
    -0.19020609944839817 + m.x11)**2 + (-0.4008706004716366 + m.x12)**2 + (
    -0.5407610291048321 + m.x13)**2 + (-0.8000549779835641 + m.x14)**2 + (
    -0.7754363156363911 + m.x15)**2) + m.x262 * ((-0.5953521882510386 + m.x11)
    **2 + (-0.1323790589753776 + m.x12)**2 + (-0.674325798913709 + m.x13)**2 +
    (-0.6802743270136904 + m.x14)**2 + (-0.6883933097372661 + m.x15)**2) +
    m.x263 * ((-0.0025493017098370263 + m.x11)**2 + (-0.5408609572630549 +
    m.x12)**2 + (-0.21056832640321543 + m.x13)**2 + (-0.031895597099028006 +
    m.x14)**2 + (-0.9985895136544211 + m.x15)**2) + m.x264 * ((
    -0.892560554551534 + m.x11)**2 + (-0.40029433919218094 + m.x12)**2 + (
    -0.9701046642126923 + m.x13)**2 + (-0.5884238994048921 + m.x14)**2 + (
    -0.04492127078158925 + m.x15)**2) + m.x265 * ((-0.9711532299798178 + m.x11)
    **2 + (-0.7241186041302273 + m.x12)**2 + (-0.9234336718225257 + m.x13)**2
    + (-0.003826457398836247 + m.x14)**2 + (-0.3002972961786634 + m.x15)**2)
    + m.x266 * ((-0.15802096343337946 + m.x11)**2 + (-0.4588369898224075 +
    m.x12)**2 + (-0.6765171167545904 + m.x13)**2 + (-0.17961210518975568 +
    m.x14)**2 + (-0.28429639692211905 + m.x15)**2) + m.x267 * ((
    -0.1275427349595054 + m.x11)**2 + (-0.896178413967487 + m.x12)**2 + (
    -0.6857155096847544 + m.x13)**2 + (-0.20857237409144969 + m.x14)**2 + (
    -0.6593772608523063 + m.x15)**2) + m.x268 * ((-0.2518121214424135 + m.x11)
    **2 + (-0.19634048416982464 + m.x12)**2 + (-0.2196605919477318 + m.x13)**2
    + (-0.865875174260687 + m.x14)**2 + (-0.7362332660498551 + m.x15)**2) +
    m.x269 * ((-0.934483116823359 + m.x11)**2 + (-0.27077656486698387 + m.x12)
    **2 + (-0.13893908152756917 + m.x13)**2 + (-0.5480837183068329 + m.x14)**2
    + (-0.8292665541893569 + m.x15)**2) + m.x270 * ((-0.5662267512605267 +
    m.x11)**2 + (-0.5099376130769819 + m.x12)**2 + (-0.2783401593907391 + m.x13)
    **2 + (-0.8795236875792728 + m.x14)**2 + (-0.33198844026096497 + m.x15)**2)
    + m.x271 * ((-0.11296146321165768 + m.x11)**2 + (-0.6813205222070685 +
    m.x12)**2 + (-0.22774906646074178 + m.x13)**2 + (-0.8784864778842033 +
    m.x14)**2 + (-0.8396296726708307 + m.x15)**2) + m.x272 * ((
    -0.15804249469097742 + m.x11)**2 + (-0.15129563301525983 + m.x12)**2 + (
    -0.23341754619049626 + m.x13)**2 + (-0.7769582120439635 + m.x14)**2 + (
    -0.5384317246672141 + m.x15)**2) + m.x273 * ((-0.5673150459473091 + m.x11)
    **2 + (-0.05014149052835315 + m.x12)**2 + (-0.17148121842456865 + m.x13)**2
    + (-0.2810141473189889 + m.x14)**2 + (-0.9529181159762178 + m.x15)**2) +
    m.x274 * ((-0.2848837563876002 + m.x11)**2 + (-0.8045194213858222 + m.x12)
    **2 + (-0.5682719027595411 + m.x13)**2 + (-0.6911634954580173 + m.x14)**2
    + (-0.7839810486640113 + m.x15)**2) + m.x275 * ((-0.5262875594913442 +
    m.x11)**2 + (-0.3665539509664488 + m.x12)**2 + (-0.37305902801355184 +
    m.x13)**2 + (-0.15221811233372107 + m.x14)**2 + (-0.8260586045664113 +
    m.x15)**2) + m.x276 * ((-0.16936346676074598 + m.x11)**2 + (
    -0.8061630890365296 + m.x12)**2 + (-0.46125767117343186 + m.x13)**2 + (
    -0.9633530374089155 + m.x14)**2 + (-0.39455433477142554 + m.x15)**2) +
    m.x277 * ((-0.04720272980003026 + m.x11)**2 + (-0.5423515001796103 + m.x12)
    **2 + (-0.6476785137633218 + m.x13)**2 + (-0.9771678211855662 + m.x14)**2
    + (-0.09890495615065897 + m.x15)**2) + m.x278 * ((-0.7744956022252439 +
    m.x11)**2 + (-0.8375885312694634 + m.x12)**2 + (-0.5467762179494536 + m.x13)
    **2 + (-0.8465780784820106 + m.x14)**2 + (-0.5651623293818131 + m.x15)**2)
    + m.x279 * ((-0.9883458791190726 + m.x11)**2 + (-0.78960766333768 + m.x12)
    **2 + (-0.8907423797504631 + m.x13)**2 + (-0.5609054564815562 + m.x14)**2
    + (-0.11178841876855738 + m.x15)**2) + m.x280 * ((-0.41454744963447077 +
    m.x11)**2 + (-0.8962451223260787 + m.x12)**2 + (-0.6225912810529636 + m.x13)
    **2 + (-0.42711413408897947 + m.x14)**2 + (-0.42194769116734065 + m.x15)**2)
    + m.x281 * ((-0.38705619554376947 + m.x11)**2 + (-0.28436641527015727 +
    m.x12)**2 + (-0.28962805588226503 + m.x13)**2 + (-0.019398816297398036 +
    m.x14)**2 + (-0.43974457277505385 + m.x15)**2) + m.x282 * ((
    -0.46045133836211705 + m.x11)**2 + (-0.3178908083894423 + m.x12)**2 + (
    -0.9107204847423361 + m.x13)**2 + (-0.024132158913902413 + m.x14)**2 + (
    -0.850132577654732 + m.x15)**2) + m.x283 * ((-0.8976765685484652 + m.x11)**
    2 + (-0.7980597430245149 + m.x12)**2 + (-0.348193168299762 + m.x13)**2 + (
    -0.6420465325576905 + m.x14)**2 + (-0.6796812519179917 + m.x15)**2) +
    m.x284 * ((-0.15285846774564793 + m.x11)**2 + (-0.4347159732826844 + m.x12)
    **2 + (-0.8316008068895342 + m.x13)**2 + (-0.8965273852203728 + m.x14)**2
    + (-0.9912538972487986 + m.x15)**2) + m.x285 * ((-0.5369883922939439 +
    m.x11)**2 + (-0.4667840512773145 + m.x12)**2 + (-0.09728386761736485 +
    m.x13)**2 + (-0.7392757773313592 + m.x14)**2 + (-0.13153034052076962 +
    m.x15)**2) + m.x286 * ((-0.5171601875396525 + m.x11)**2 + (
    -0.6501055077806779 + m.x12)**2 + (-0.4738783294442884 + m.x13)**2 + (
    -0.3059905276444237 + m.x14)**2 + (-0.4655403665248422 + m.x15)**2) +
    m.x287 * ((-0.38769522192282246 + m.x11)**2 + (-0.9889925696368229 + m.x12)
    **2 + (-0.02462276265854113 + m.x13)**2 + (-0.5533833006798677 + m.x14)**2
    + (-0.9049316659882748 + m.x15)**2) + m.x288 * ((-0.6476766247522808 +
    m.x11)**2 + (-0.48861089343022013 + m.x12)**2 + (-0.4222074787200718 +
    m.x13)**2 + (-0.3336931215925991 + m.x14)**2 + (-0.2256832722919292 + m.x15)
    **2) + m.x289 * ((-0.7074126149862657 + m.x11)**2 + (-0.24826058840938114
    + m.x12)**2 + (-0.935855008312046 + m.x13)**2 + (-0.4531363616293268 +
    m.x14)**2 + (-0.2916105761611406 + m.x15)**2) + m.x290 * ((
    -0.14641966747166446 + m.x11)**2 + (-0.2788408089755944 + m.x12)**2 + (
    -0.5445004171692817 + m.x13)**2 + (-0.7776763802122033 + m.x14)**2 + (
    -0.5886958457853472 + m.x15)**2) + m.x291 * ((-0.22535164416260256 + m.x11)
    **2 + (-0.8648957992131536 + m.x12)**2 + (-0.31409985209738056 + m.x13)**2
    + (-0.38674349351260584 + m.x14)**2 + (-0.9278581053708341 + m.x15)**2) +
    m.x292 * ((-0.6984113442379634 + m.x11)**2 + (-0.5880319612907634 + m.x12)
    **2 + (-0.7055183537964272 + m.x13)**2 + (-0.052288634884028795 + m.x14)**2
    + (-0.9540221980524576 + m.x15)**2) + m.x293 * ((-0.6525901987545907 +
    m.x11)**2 + (-0.6324492441244804 + m.x12)**2 + (-0.41138748171911876 +
    m.x13)**2 + (-0.3346719309177193 + m.x14)**2 + (-0.16814397167586703 +
    m.x15)**2) + m.x294 * ((-0.967047497872221 + m.x11)**2 + (
    -0.18063656917774573 + m.x12)**2 + (-0.2400182048559567 + m.x13)**2 + (
    -0.6691034304335645 + m.x14)**2 + (-0.5203600552914871 + m.x15)**2) +
    m.x295 * ((-0.5133995855393014 + m.x11)**2 + (-0.682357221251084 + m.x12)**
    2 + (-0.22915213911098808 + m.x13)**2 + (-0.03240517485202765 + m.x14)**2
    + (-0.30169291229505235 + m.x15)**2) + m.x296 * ((-0.5209867319058553 +
    m.x11)**2 + (-0.4556272113241485 + m.x12)**2 + (-0.9348398039566677 + m.x13)
    **2 + (-0.4769297195138824 + m.x14)**2 + (-0.5441271791767697 + m.x15)**2)
    + m.x297 * ((-0.05968232483167746 + m.x11)**2 + (-0.4047870938674545 +
    m.x12)**2 + (-0.5094808400454084 + m.x13)**2 + (-0.5133405099339715 + m.x14)
    **2 + (-0.8694173637603428 + m.x15)**2) + m.x298 * ((-0.7069125249619734 +
    m.x11)**2 + (-0.7805582252528287 + m.x12)**2 + (-0.3622713115889995 + m.x13)
    **2 + (-0.18641714280195076 + m.x14)**2 + (-0.13146290481233758 + m.x15)**2)
    + m.x299 * ((-0.6988866065066833 + m.x11)**2 + (-0.45397288260266866 +
    m.x12)**2 + (-0.45859107895122997 + m.x13)**2 + (-0.05137579962338035 +
    m.x14)**2 + (-0.04592955703454393 + m.x15)**2) + m.x300 * ((
    -0.2521200382154474 + m.x11)**2 + (-0.6536293489021203 + m.x12)**2 + (
    -0.5192181028685813 + m.x13)**2 + (-0.20358265360251637 + m.x14)**2 + (
    -0.05678264541333178 + m.x15)**2) + m.x301 * ((-0.7359000712721689 + m.x11)
    **2 + (-0.5285245765765676 + m.x12)**2 + (-0.783746106047006 + m.x13)**2 +
    (-0.2072423999303571 + m.x14)**2 + (-0.9345165540918818 + m.x15)**2) +
    m.x302 * ((-0.0676233453727606 + m.x11)**2 + (-0.15045515445014457 + m.x12)
    **2 + (-0.3631523266765533 + m.x13)**2 + (-0.06793304154668878 + m.x14)**2
    + (-0.9177903450542778 + m.x15)**2) + m.x303 * ((-0.9218805175952314 +
    m.x11)**2 + (-0.7879207544431588 + m.x12)**2 + (-0.6131320375628063 + m.x13)
    **2 + (-0.9794197292428298 + m.x14)**2 + (-0.6731862091841032 + m.x15)**2)
    + m.x304 * ((-0.5488460632188782 + m.x11)**2 + (-0.8660152527377067 +
    m.x12)**2 + (-0.697256474689279 + m.x13)**2 + (-0.7403125785102036 + m.x14)
    **2 + (-0.9230110595772295 + m.x15)**2) + m.x305 * ((-0.03349799947042298
    + m.x11)**2 + (-0.013311552955958983 + m.x12)**2 + (-0.64790084232628 +
    m.x13)**2 + (-0.027327006271035903 + m.x14)**2 + (-0.45800635737351614 +
    m.x15)**2) + m.x306 * ((-0.3787875046692417 + m.x11)**2 + (
    -0.7756927089046994 + m.x12)**2 + (-0.08102978802889482 + m.x13)**2 + (
    -0.6885140630996159 + m.x14)**2 + (-0.258837614057293 + m.x15)**2) + m.x307
    * ((-0.926549979364291 + m.x11)**2 + (-0.6576775076711792 + m.x12)**2 + (
    -0.7185667900619702 + m.x13)**2 + (-0.8393281555178195 + m.x14)**2 + (
    -0.8790478271287436 + m.x15)**2) + m.x308 * ((-0.8538536880933677 + m.x11)
    **2 + (-0.41093785441645236 + m.x12)**2 + (-0.821623842184094 + m.x13)**2
    + (-0.3479518255783647 + m.x14)**2 + (-0.7092095860729987 + m.x15)**2) +
    m.x309 * ((-0.36696518655512345 + m.x11)**2 + (-0.20091071029318852 + m.x12)
    **2 + (-0.077731695458928 + m.x13)**2 + (-0.5169327130336349 + m.x14)**2 +
    (-0.933512225646472 + m.x15)**2) + m.x310 * ((-0.12535873106543383 + m.x11)
    **2 + (-0.20807091090575502 + m.x12)**2 + (-0.1737536300614485 + m.x13)**2
    + (-0.9634306672730328 + m.x14)**2 + (-0.9058308480768769 + m.x15)**2) +
    m.x311 * ((-0.1853802586369372 + m.x11)**2 + (-0.006662572599986594 + m.x12)
    **2 + (-0.010905690589545047 + m.x13)**2 + (-0.14902785082635217 + m.x14)**
    2 + (-0.22770558623177606 + m.x15)**2) + m.x312 * ((-0.4633514401824739 +
    m.x11)**2 + (-0.6547129104209288 + m.x12)**2 + (-0.5099212885026749 + m.x13)
    **2 + (-0.797446966803318 + m.x14)**2 + (-0.2962748229669455 + m.x15)**2)
    + m.x313 * ((-0.36278221024643986 + m.x11)**2 + (-0.3277254622076904 +
    m.x12)**2 + (-0.7995480920087982 + m.x13)**2 + (-0.5823823799369167 + m.x14)
    **2 + (-0.880766278018624 + m.x15)**2) + m.x314 * ((-0.3223606530293073 +
    m.x11)**2 + (-0.3211031767538892 + m.x12)**2 + (-0.8703147018545497 + m.x13)
    **2 + (-0.11319702691533051 + m.x14)**2 + (-0.16343459625058143 + m.x15)**2)
    + m.x315 * ((-0.7686159036050828 + m.x11)**2 + (-0.4198142721548951 +
    m.x12)**2 + (-0.42491506406704316 + m.x13)**2 + (-0.45957758374218605 +
    m.x14)**2 + (-0.01631022121777903 + m.x15)**2))

m.e1 = Constraint(expr= m.x16 + m.x116 + m.x216 == 1)
m.e2 = Constraint(expr= m.x17 + m.x117 + m.x217 == 1)
m.e3 = Constraint(expr= m.x18 + m.x118 + m.x218 == 1)
m.e4 = Constraint(expr= m.x19 + m.x119 + m.x219 == 1)
m.e5 = Constraint(expr= m.x20 + m.x120 + m.x220 == 1)
m.e6 = Constraint(expr= m.x21 + m.x121 + m.x221 == 1)
m.e7 = Constraint(expr= m.x22 + m.x122 + m.x222 == 1)
m.e8 = Constraint(expr= m.x23 + m.x123 + m.x223 == 1)
m.e9 = Constraint(expr= m.x24 + m.x124 + m.x224 == 1)
m.e10 = Constraint(expr= m.x25 + m.x125 + m.x225 == 1)
m.e11 = Constraint(expr= m.x26 + m.x126 + m.x226 == 1)
m.e12 = Constraint(expr= m.x27 + m.x127 + m.x227 == 1)
m.e13 = Constraint(expr= m.x28 + m.x128 + m.x228 == 1)
m.e14 = Constraint(expr= m.x29 + m.x129 + m.x229 == 1)
m.e15 = Constraint(expr= m.x30 + m.x130 + m.x230 == 1)
m.e16 = Constraint(expr= m.x31 + m.x131 + m.x231 == 1)
m.e17 = Constraint(expr= m.x32 + m.x132 + m.x232 == 1)
m.e18 = Constraint(expr= m.x33 + m.x133 + m.x233 == 1)
m.e19 = Constraint(expr= m.x34 + m.x134 + m.x234 == 1)
m.e20 = Constraint(expr= m.x35 + m.x135 + m.x235 == 1)
m.e21 = Constraint(expr= m.x36 + m.x136 + m.x236 == 1)
m.e22 = Constraint(expr= m.x37 + m.x137 + m.x237 == 1)
m.e23 = Constraint(expr= m.x38 + m.x138 + m.x238 == 1)
m.e24 = Constraint(expr= m.x39 + m.x139 + m.x239 == 1)
m.e25 = Constraint(expr= m.x40 + m.x140 + m.x240 == 1)
m.e26 = Constraint(expr= m.x41 + m.x141 + m.x241 == 1)
m.e27 = Constraint(expr= m.x42 + m.x142 + m.x242 == 1)
m.e28 = Constraint(expr= m.x43 + m.x143 + m.x243 == 1)
m.e29 = Constraint(expr= m.x44 + m.x144 + m.x244 == 1)
m.e30 = Constraint(expr= m.x45 + m.x145 + m.x245 == 1)
m.e31 = Constraint(expr= m.x46 + m.x146 + m.x246 == 1)
m.e32 = Constraint(expr= m.x47 + m.x147 + m.x247 == 1)
m.e33 = Constraint(expr= m.x48 + m.x148 + m.x248 == 1)
m.e34 = Constraint(expr= m.x49 + m.x149 + m.x249 == 1)
m.e35 = Constraint(expr= m.x50 + m.x150 + m.x250 == 1)
m.e36 = Constraint(expr= m.x51 + m.x151 + m.x251 == 1)
m.e37 = Constraint(expr= m.x52 + m.x152 + m.x252 == 1)
m.e38 = Constraint(expr= m.x53 + m.x153 + m.x253 == 1)
m.e39 = Constraint(expr= m.x54 + m.x154 + m.x254 == 1)
m.e40 = Constraint(expr= m.x55 + m.x155 + m.x255 == 1)
m.e41 = Constraint(expr= m.x56 + m.x156 + m.x256 == 1)
m.e42 = Constraint(expr= m.x57 + m.x157 + m.x257 == 1)
m.e43 = Constraint(expr= m.x58 + m.x158 + m.x258 == 1)
m.e44 = Constraint(expr= m.x59 + m.x159 + m.x259 == 1)
m.e45 = Constraint(expr= m.x60 + m.x160 + m.x260 == 1)
m.e46 = Constraint(expr= m.x61 + m.x161 + m.x261 == 1)
m.e47 = Constraint(expr= m.x62 + m.x162 + m.x262 == 1)
m.e48 = Constraint(expr= m.x63 + m.x163 + m.x263 == 1)
m.e49 = Constraint(expr= m.x64 + m.x164 + m.x264 == 1)
m.e50 = Constraint(expr= m.x65 + m.x165 + m.x265 == 1)
m.e51 = Constraint(expr= m.x66 + m.x166 + m.x266 == 1)
m.e52 = Constraint(expr= m.x67 + m.x167 + m.x267 == 1)
m.e53 = Constraint(expr= m.x68 + m.x168 + m.x268 == 1)
m.e54 = Constraint(expr= m.x69 + m.x169 + m.x269 == 1)
m.e55 = Constraint(expr= m.x70 + m.x170 + m.x270 == 1)
m.e56 = Constraint(expr= m.x71 + m.x171 + m.x271 == 1)
m.e57 = Constraint(expr= m.x72 + m.x172 + m.x272 == 1)
m.e58 = Constraint(expr= m.x73 + m.x173 + m.x273 == 1)
m.e59 = Constraint(expr= m.x74 + m.x174 + m.x274 == 1)
m.e60 = Constraint(expr= m.x75 + m.x175 + m.x275 == 1)
m.e61 = Constraint(expr= m.x76 + m.x176 + m.x276 == 1)
m.e62 = Constraint(expr= m.x77 + m.x177 + m.x277 == 1)
m.e63 = Constraint(expr= m.x78 + m.x178 + m.x278 == 1)
m.e64 = Constraint(expr= m.x79 + m.x179 + m.x279 == 1)
m.e65 = Constraint(expr= m.x80 + m.x180 + m.x280 == 1)
m.e66 = Constraint(expr= m.x81 + m.x181 + m.x281 == 1)
m.e67 = Constraint(expr= m.x82 + m.x182 + m.x282 == 1)
m.e68 = Constraint(expr= m.x83 + m.x183 + m.x283 == 1)
m.e69 = Constraint(expr= m.x84 + m.x184 + m.x284 == 1)
m.e70 = Constraint(expr= m.x85 + m.x185 + m.x285 == 1)
m.e71 = Constraint(expr= m.x86 + m.x186 + m.x286 == 1)
m.e72 = Constraint(expr= m.x87 + m.x187 + m.x287 == 1)
m.e73 = Constraint(expr= m.x88 + m.x188 + m.x288 == 1)
m.e74 = Constraint(expr= m.x89 + m.x189 + m.x289 == 1)
m.e75 = Constraint(expr= m.x90 + m.x190 + m.x290 == 1)
m.e76 = Constraint(expr= m.x91 + m.x191 + m.x291 == 1)
m.e77 = Constraint(expr= m.x92 + m.x192 + m.x292 == 1)
m.e78 = Constraint(expr= m.x93 + m.x193 + m.x293 == 1)
m.e79 = Constraint(expr= m.x94 + m.x194 + m.x294 == 1)
m.e80 = Constraint(expr= m.x95 + m.x195 + m.x295 == 1)
m.e81 = Constraint(expr= m.x96 + m.x196 + m.x296 == 1)
m.e82 = Constraint(expr= m.x97 + m.x197 + m.x297 == 1)
m.e83 = Constraint(expr= m.x98 + m.x198 + m.x298 == 1)
m.e84 = Constraint(expr= m.x99 + m.x199 + m.x299 == 1)
m.e85 = Constraint(expr= m.x100 + m.x200 + m.x300 == 1)
m.e86 = Constraint(expr= m.x101 + m.x201 + m.x301 == 1)
m.e87 = Constraint(expr= m.x102 + m.x202 + m.x302 == 1)
m.e88 = Constraint(expr= m.x103 + m.x203 + m.x303 == 1)
m.e89 = Constraint(expr= m.x104 + m.x204 + m.x304 == 1)
m.e90 = Constraint(expr= m.x105 + m.x205 + m.x305 == 1)
m.e91 = Constraint(expr= m.x106 + m.x206 + m.x306 == 1)
m.e92 = Constraint(expr= m.x107 + m.x207 + m.x307 == 1)
m.e93 = Constraint(expr= m.x108 + m.x208 + m.x308 == 1)
m.e94 = Constraint(expr= m.x109 + m.x209 + m.x309 == 1)
m.e95 = Constraint(expr= m.x110 + m.x210 + m.x310 == 1)
m.e96 = Constraint(expr= m.x111 + m.x211 + m.x311 == 1)
m.e97 = Constraint(expr= m.x112 + m.x212 + m.x312 == 1)
m.e98 = Constraint(expr= m.x113 + m.x213 + m.x313 == 1)
m.e99 = Constraint(expr= m.x114 + m.x214 + m.x314 == 1)
m.e100 = Constraint(expr= m.x115 + m.x215 + m.x315 == 1)
