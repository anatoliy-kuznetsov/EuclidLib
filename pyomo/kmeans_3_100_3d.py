# NLP written by GAMS Convert at 05/15/24 11:38:39
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       100      100        0        0        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#       309      309        0        0        0        0        0        0
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

m.obj = Objective(sense=minimize, expr= m.x10 * ((-0.03165747404234709 + m.x1)
    **2 + (-0.9688037614558638 + m.x2)**2 + (-0.194905594675844 + m.x3)**2) +
    m.x11 * ((-0.994404983268671 + m.x1)**2 + (-0.9467435823614155 + m.x2)**2
    + (-0.2586761829758428 + m.x3)**2) + m.x12 * ((-0.5162664278327235 + m.x1)
    **2 + (-0.3982793402500453 + m.x2)**2 + (-0.40970912928025993 + m.x3)**2)
    + m.x13 * ((-0.7896862520479686 + m.x1)**2 + (-0.8277301347873149 + m.x2)
    **2 + (-0.25653942323136325 + m.x3)**2) + m.x14 * ((-0.5439125654987014 +
    m.x1)**2 + (-0.6860092880739965 + m.x2)**2 + (-0.5938661979256709 + m.x3)**
    2) + m.x15 * ((-0.12145860265901365 + m.x1)**2 + (-0.39111450417437643 +
    m.x2)**2 + (-0.4928847200416665 + m.x3)**2) + m.x16 * ((-0.9241028428385594
    + m.x1)**2 + (-0.8224281118826651 + m.x2)**2 + (-0.674823652303014 + m.x3)
    **2) + m.x17 * ((-0.28018573452261986 + m.x1)**2 + (-0.9387375342731106 +
    m.x2)**2 + (-0.22921703916265213 + m.x3)**2) + m.x18 * ((
    -0.33782732597445464 + m.x1)**2 + (-0.1569657415747544 + m.x2)**2 + (
    -0.5890088103246424 + m.x3)**2) + m.x19 * ((-0.7956363045257931 + m.x1)**2
    + (-0.7018138263270055 + m.x2)**2 + (-0.827204195503925 + m.x3)**2) +
    m.x20 * ((-0.7024344542903443 + m.x1)**2 + (-0.6531462663458645 + m.x2)**2
    + (-0.25148549322484737 + m.x3)**2) + m.x21 * ((-0.9585188794829803 + m.x1)
    **2 + (-0.9904845118748664 + m.x2)**2 + (-0.7326374193712811 + m.x3)**2) +
    m.x22 * ((-0.9969942571314364 + m.x1)**2 + (-0.8835504075311506 + m.x2)**2
    + (-0.8772673971146973 + m.x3)**2) + m.x23 * ((-0.7568188479193806 + m.x1)
    **2 + (-0.8118073567007532 + m.x2)**2 + (-0.691020784028435 + m.x3)**2) +
    m.x24 * ((-0.12763593187242794 + m.x1)**2 + (-0.8373067805693528 + m.x2)**2
    + (-0.35242278927521786 + m.x3)**2) + m.x25 * ((-0.6436739189615287 + m.x1)
    **2 + (-0.8993202141020306 + m.x2)**2 + (-0.49329897886966445 + m.x3)**2)
    + m.x26 * ((-0.2704172505123661 + m.x1)**2 + (-0.5533199618789462 + m.x2)
    **2 + (-0.8757319534050035 + m.x3)**2) + m.x27 * ((-0.8408449490729443 +
    m.x1)**2 + (-0.9938527400105247 + m.x2)**2 + (-0.9078205126634532 + m.x3)**
    2) + m.x28 * ((-0.8048628358106328 + m.x1)**2 + (-0.48485118220454304 +
    m.x2)**2 + (-0.18268576976148887 + m.x3)**2) + m.x29 * ((
    -0.9327863184767982 + m.x1)**2 + (-0.03845948966269497 + m.x2)**2 + (
    -0.9470512611806989 + m.x3)**2) + m.x30 * ((-0.639261595397489 + m.x1)**2
    + (-0.23603710481675744 + m.x2)**2 + (-0.1660094109394994 + m.x3)**2) +
    m.x31 * ((-0.7169414805312546 + m.x1)**2 + (-0.07229070145966299 + m.x2)**2
    + (-0.431045837716155 + m.x3)**2) + m.x32 * ((-0.10668296608426875 + m.x1)
    **2 + (-0.1348668647474297 + m.x2)**2 + (-0.2514322339876659 + m.x3)**2) +
    m.x33 * ((-0.6526799327386067 + m.x1)**2 + (-0.026932475138882972 + m.x2)**
    2 + (-0.8536420651804307 + m.x3)**2) + m.x34 * ((-0.6302165389370114 + m.x1)
    **2 + (-0.25833853732983525 + m.x2)**2 + (-0.7144829483905738 + m.x3)**2)
    + m.x35 * ((-0.0630491076625409 + m.x1)**2 + (-0.2533861860136738 + m.x2)
    **2 + (-0.5039058975045216 + m.x3)**2) + m.x36 * ((-0.8542315079472844 +
    m.x1)**2 + (-0.6752218855677596 + m.x2)**2 + (-0.03975458066767401 + m.x3)
    **2) + m.x37 * ((-0.9588366784175165 + m.x1)**2 + (-0.15399304462715124 +
    m.x2)**2 + (-0.18453488984672461 + m.x3)**2) + m.x38 * ((-0.577837467669182
    + m.x1)**2 + (-0.07039723161872768 + m.x2)**2 + (-0.4109540294871704 +
    m.x3)**2) + m.x39 * ((-0.21154639509694562 + m.x1)**2 + (-0.450594996440561
    + m.x2)**2 + (-0.3493784703429885 + m.x3)**2) + m.x40 * ((
    -0.42089798204034234 + m.x1)**2 + (-0.3399961668152647 + m.x2)**2 + (
    -0.4798458658941379 + m.x3)**2) + m.x41 * ((-0.6572382708452076 + m.x1)**2
    + (-0.4203009532797096 + m.x2)**2 + (-0.5288398250165213 + m.x3)**2) +
    m.x42 * ((-0.29665432034913075 + m.x1)**2 + (-0.3973578619430581 + m.x2)**2
    + (-0.07783691735217746 + m.x3)**2) + m.x43 * ((-0.45792662283881924 +
    m.x1)**2 + (-0.5041791032851748 + m.x2)**2 + (-0.1594779036498647 + m.x3)**
    2) + m.x44 * ((-0.3173596228621427 + m.x1)**2 + (-0.5563727830980914 + m.x2)
    **2 + (-0.4860010038140109 + m.x3)**2) + m.x45 * ((-0.6310766569169546 +
    m.x1)**2 + (-0.25588647042147916 + m.x2)**2 + (-0.8198772382408238 + m.x3)
    **2) + m.x46 * ((-0.1488692223404685 + m.x1)**2 + (-0.9193686903702157 +
    m.x2)**2 + (-0.34023040415812167 + m.x3)**2) + m.x47 * ((
    -0.2697960633307809 + m.x1)**2 + (-0.335907091585785 + m.x2)**2 + (
    -0.9467428317615326 + m.x3)**2) + m.x48 * ((-0.6938343635759197 + m.x1)**2
    + (-0.9436133968451139 + m.x2)**2 + (-0.991021501717515 + m.x3)**2) +
    m.x49 * ((-0.4642219155925973 + m.x1)**2 + (-0.8029654939972901 + m.x2)**2
    + (-0.043919917836081845 + m.x3)**2) + m.x50 * ((-0.8127682269274624 +
    m.x1)**2 + (-0.25601168886588366 + m.x2)**2 + (-0.3341736569353614 + m.x3)
    **2) + m.x51 * ((-0.6705401412001404 + m.x1)**2 + (-0.5087249365112236 +
    m.x2)**2 + (-0.5517555972411828 + m.x3)**2) + m.x52 * ((
    -0.32032448244190315 + m.x1)**2 + (-0.39296980599158504 + m.x2)**2 + (
    -0.9198001088344934 + m.x3)**2) + m.x53 * ((-0.026348361043022406 + m.x1)**
    2 + (-0.020629924903295738 + m.x2)**2 + (-0.6435466838744265 + m.x3)**2) +
    m.x54 * ((-0.08245094736473269 + m.x1)**2 + (-0.25631060193284183 + m.x2)**
    2 + (-0.27184690982879867 + m.x3)**2) + m.x55 * ((-0.026175964022221 + m.x1)
    **2 + (-0.39001844671412356 + m.x2)**2 + (-0.9734667628650259 + m.x3)**2)
    + m.x56 * ((-0.8602811534294952 + m.x1)**2 + (-0.04192541019078189 + m.x2)
    **2 + (-0.9890062597661148 + m.x3)**2) + m.x57 * ((-0.9024392311723397 +
    m.x1)**2 + (-0.8587679231141961 + m.x2)**2 + (-0.17748882176540326 + m.x3)
    **2) + m.x58 * ((-0.31753107996501695 + m.x1)**2 + (-0.16045141716999045 +
    m.x2)**2 + (-0.7376965692150161 + m.x3)**2) + m.x59 * ((-0.7179847110204995
    + m.x1)**2 + (-0.27649224925146654 + m.x2)**2 + (-0.9595943343831328 +
    m.x3)**2) + m.x60 * ((-0.7273508397885963 + m.x1)**2 + (-0.7141464054238915
    + m.x2)**2 + (-0.4236328365996608 + m.x3)**2) + m.x61 * ((
    -0.8568474154217326 + m.x1)**2 + (-0.5493004484843343 + m.x2)**2 + (
    -0.7790605542975685 + m.x3)**2) + m.x62 * ((-0.91416162569631 + m.x1)**2 +
    (-0.07083595559092482 + m.x2)**2 + (-0.04758287958281404 + m.x3)**2) +
    m.x63 * ((-0.23610671226901814 + m.x1)**2 + (-0.9222887291303542 + m.x2)**2
    + (-0.3289139546862677 + m.x3)**2) + m.x64 * ((-0.3772829976803017 + m.x1)
    **2 + (-0.5557643900196702 + m.x2)**2 + (-0.5481909082805208 + m.x3)**2) +
    m.x65 * ((-0.4494533670891915 + m.x1)**2 + (-0.8186667716158522 + m.x2)**2
    + (-0.4636653461366691 + m.x3)**2) + m.x66 * ((-0.7654192246719118 + m.x1)
    **2 + (-0.13587703107223248 + m.x2)**2 + (-0.7498343196419972 + m.x3)**2)
    + m.x67 * ((-0.4652456377047164 + m.x1)**2 + (-0.5077984771377264 + m.x2)
    **2 + (-0.1348926417621431 + m.x3)**2) + m.x68 * ((-0.8699578841310688 +
    m.x1)**2 + (-0.14273661142672123 + m.x2)**2 + (-0.763817129937746 + m.x3)**
    2) + m.x69 * ((-0.5216108578277676 + m.x1)**2 + (-0.011154425913213695 +
    m.x2)**2 + (-0.9567874437000136 + m.x3)**2) + m.x70 * ((-0.7485755829859556
    + m.x1)**2 + (-0.10118542234301908 + m.x2)**2 + (-0.1783837759059177 +
    m.x3)**2) + m.x71 * ((-0.9360375934197785 + m.x1)**2 + (-0.4538524923598969
    + m.x2)**2 + (-0.569108208025147 + m.x3)**2) + m.x72 * ((
    -0.4192122693219924 + m.x1)**2 + (-0.005472324326698974 + m.x2)**2 + (
    -0.07528239578511564 + m.x3)**2) + m.x73 * ((-0.26940299166354387 + m.x1)**
    2 + (-0.12687373219539666 + m.x2)**2 + (-0.40516803979431204 + m.x3)**2) +
    m.x74 * ((-0.3914652811474665 + m.x1)**2 + (-0.7630816647003282 + m.x2)**2
    + (-0.029978234429024586 + m.x3)**2) + m.x75 * ((-0.6668476332988318 +
    m.x1)**2 + (-0.24997798690844042 + m.x2)**2 + (-0.6265370286243447 + m.x3)
    **2) + m.x76 * ((-0.34120258424029504 + m.x1)**2 + (-0.07403590994489917 +
    m.x2)**2 + (-0.720744885669365 + m.x3)**2) + m.x77 * ((-0.06868736363853345
    + m.x1)**2 + (-0.816362121123889 + m.x2)**2 + (-0.3244522597036481 + m.x3)
    **2) + m.x78 * ((-0.1133957787796036 + m.x1)**2 + (-0.5910142596485125 +
    m.x2)**2 + (-0.6723456801786042 + m.x3)**2) + m.x79 * ((-0.9887438686593106
    + m.x1)**2 + (-0.21533727799458513 + m.x2)**2 + (-0.09743238299874801 +
    m.x3)**2) + m.x80 * ((-0.9246438240807238 + m.x1)**2 + (-0.2700464496762641
    + m.x2)**2 + (-0.6245624095989588 + m.x3)**2) + m.x81 * ((
    -0.5656126537021211 + m.x1)**2 + (-0.9818699763888468 + m.x2)**2 + (
    -0.5940226943946902 + m.x3)**2) + m.x82 * ((-0.8113977745952538 + m.x1)**2
    + (-0.18585378085900206 + m.x2)**2 + (-0.7952249374713821 + m.x3)**2) +
    m.x83 * ((-0.48313873546297303 + m.x1)**2 + (-0.7631917439270134 + m.x2)**2
    + (-0.6364111963610009 + m.x3)**2) + m.x84 * ((-0.1381908613661963 + m.x1)
    **2 + (-0.402990641918228 + m.x2)**2 + (-0.6133309405917241 + m.x3)**2) +
    m.x85 * ((-0.18888139540069937 + m.x1)**2 + (-0.3239340910426727 + m.x2)**2
    + (-0.29122420662372395 + m.x3)**2) + m.x86 * ((-0.45971525577369654 +
    m.x1)**2 + (-0.8781315029877753 + m.x2)**2 + (-0.9416973480122568 + m.x3)**
    2) + m.x87 * ((-0.6421070423802201 + m.x1)**2 + (-0.6746002536392893 + m.x2)
    **2 + (-0.9366116957484414 + m.x3)**2) + m.x88 * ((-0.8617718322773262 +
    m.x1)**2 + (-0.5752590469218912 + m.x2)**2 + (-0.03643977625783423 + m.x3)
    **2) + m.x89 * ((-0.3461122806124808 + m.x1)**2 + (-0.26939444151917924 +
    m.x2)**2 + (-0.6117048154287927 + m.x3)**2) + m.x90 * ((-0.3980802568243521
    + m.x1)**2 + (-0.12833605403046588 + m.x2)**2 + (-0.6550699173363765 +
    m.x3)**2) + m.x91 * ((-0.4212633224085762 + m.x1)**2 + (
    -0.47619338990426596 + m.x2)**2 + (-0.8818640470300284 + m.x3)**2) + m.x92
    * ((-0.8142723498986452 + m.x1)**2 + (-0.13221974575018447 + m.x2)**2 + (
    -0.5081218602846138 + m.x3)**2) + m.x93 * ((-0.685821187895152 + m.x1)**2
    + (-0.20701052275270038 + m.x2)**2 + (-0.3313231056883219 + m.x3)**2) +
    m.x94 * ((-0.7924211927213229 + m.x1)**2 + (-0.952886214580272 + m.x2)**2
    + (-0.7066600392250384 + m.x3)**2) + m.x95 * ((-0.42315244032379085 + m.x1)
    **2 + (-0.6728665404780181 + m.x2)**2 + (-0.8975501502435518 + m.x3)**2) +
    m.x96 * ((-0.09020963855365849 + m.x1)**2 + (-0.06884955005383797 + m.x2)**
    2 + (-0.6063153645701168 + m.x3)**2) + m.x97 * ((-0.9409437143153465 + m.x1)
    **2 + (-0.923342757310195 + m.x2)**2 + (-0.22548223250540067 + m.x3)**2) +
    m.x98 * ((-0.3513754397940918 + m.x1)**2 + (-0.7535548231462733 + m.x2)**2
    + (-0.4061213664901868 + m.x3)**2) + m.x99 * ((-0.1700085446697267 + m.x1)
    **2 + (-0.4807483144944905 + m.x2)**2 + (-0.594505660789073 + m.x3)**2) +
    m.x100 * ((-0.28626909028581915 + m.x1)**2 + (-0.7328949881609186 + m.x2)**
    2 + (-0.575200065494123 + m.x3)**2) + m.x101 * ((-0.4600939889912965 + m.x1)
    **2 + (-0.2734112416210206 + m.x2)**2 + (-0.9696488694706376 + m.x3)**2) +
    m.x102 * ((-0.0599901823942226 + m.x1)**2 + (-0.31564380122598423 + m.x2)**
    2 + (-0.38196492233652524 + m.x3)**2) + m.x103 * ((-0.4628907639211667 +
    m.x1)**2 + (-0.259219253775281 + m.x2)**2 + (-0.9040810700491898 + m.x3)**2)
    + m.x104 * ((-0.27505708621291713 + m.x1)**2 + (-0.8080101091456343 + m.x2)
    **2 + (-0.5596605748627325 + m.x3)**2) + m.x105 * ((-0.7306989058987445 +
    m.x1)**2 + (-0.8522360958952263 + m.x2)**2 + (-0.4341637539475691 + m.x3)**
    2) + m.x106 * ((-0.03719257808592946 + m.x1)**2 + (-0.4185738968989311 +
    m.x2)**2 + (-0.018070376182406256 + m.x3)**2) + m.x107 * ((
    -0.01111267193250065 + m.x1)**2 + (-0.07583080853002788 + m.x2)**2 + (
    -0.11976514020331952 + m.x3)**2) + m.x108 * ((-0.881774057941981 + m.x1)**2
    + (-0.7524457238077544 + m.x2)**2 + (-0.25066589761985636 + m.x3)**2) +
    m.x109 * ((-0.07955690537673044 + m.x1)**2 + (-0.030539082027751907 + m.x2)
    **2 + (-0.42975368767560174 + m.x3)**2) + m.x110 * ((-0.03165747404234709
    + m.x4)**2 + (-0.9688037614558638 + m.x5)**2 + (-0.194905594675844 + m.x6)
    **2) + m.x111 * ((-0.994404983268671 + m.x4)**2 + (-0.9467435823614155 +
    m.x5)**2 + (-0.2586761829758428 + m.x6)**2) + m.x112 * ((
    -0.5162664278327235 + m.x4)**2 + (-0.3982793402500453 + m.x5)**2 + (
    -0.40970912928025993 + m.x6)**2) + m.x113 * ((-0.7896862520479686 + m.x4)**
    2 + (-0.8277301347873149 + m.x5)**2 + (-0.25653942323136325 + m.x6)**2) +
    m.x114 * ((-0.5439125654987014 + m.x4)**2 + (-0.6860092880739965 + m.x5)**2
    + (-0.5938661979256709 + m.x6)**2) + m.x115 * ((-0.12145860265901365 +
    m.x4)**2 + (-0.39111450417437643 + m.x5)**2 + (-0.4928847200416665 + m.x6)
    **2) + m.x116 * ((-0.9241028428385594 + m.x4)**2 + (-0.8224281118826651 +
    m.x5)**2 + (-0.674823652303014 + m.x6)**2) + m.x117 * ((
    -0.28018573452261986 + m.x4)**2 + (-0.9387375342731106 + m.x5)**2 + (
    -0.22921703916265213 + m.x6)**2) + m.x118 * ((-0.33782732597445464 + m.x4)
    **2 + (-0.1569657415747544 + m.x5)**2 + (-0.5890088103246424 + m.x6)**2) +
    m.x119 * ((-0.7956363045257931 + m.x4)**2 + (-0.7018138263270055 + m.x5)**2
    + (-0.827204195503925 + m.x6)**2) + m.x120 * ((-0.7024344542903443 + m.x4)
    **2 + (-0.6531462663458645 + m.x5)**2 + (-0.25148549322484737 + m.x6)**2)
    + m.x121 * ((-0.9585188794829803 + m.x4)**2 + (-0.9904845118748664 + m.x5)
    **2 + (-0.7326374193712811 + m.x6)**2) + m.x122 * ((-0.9969942571314364 +
    m.x4)**2 + (-0.8835504075311506 + m.x5)**2 + (-0.8772673971146973 + m.x6)**
    2) + m.x123 * ((-0.7568188479193806 + m.x4)**2 + (-0.8118073567007532 +
    m.x5)**2 + (-0.691020784028435 + m.x6)**2) + m.x124 * ((
    -0.12763593187242794 + m.x4)**2 + (-0.8373067805693528 + m.x5)**2 + (
    -0.35242278927521786 + m.x6)**2) + m.x125 * ((-0.6436739189615287 + m.x4)**
    2 + (-0.8993202141020306 + m.x5)**2 + (-0.49329897886966445 + m.x6)**2) +
    m.x126 * ((-0.2704172505123661 + m.x4)**2 + (-0.5533199618789462 + m.x5)**2
    + (-0.8757319534050035 + m.x6)**2) + m.x127 * ((-0.8408449490729443 + m.x4)
    **2 + (-0.9938527400105247 + m.x5)**2 + (-0.9078205126634532 + m.x6)**2) +
    m.x128 * ((-0.8048628358106328 + m.x4)**2 + (-0.48485118220454304 + m.x5)**
    2 + (-0.18268576976148887 + m.x6)**2) + m.x129 * ((-0.9327863184767982 +
    m.x4)**2 + (-0.03845948966269497 + m.x5)**2 + (-0.9470512611806989 + m.x6)
    **2) + m.x130 * ((-0.639261595397489 + m.x4)**2 + (-0.23603710481675744 +
    m.x5)**2 + (-0.1660094109394994 + m.x6)**2) + m.x131 * ((
    -0.7169414805312546 + m.x4)**2 + (-0.07229070145966299 + m.x5)**2 + (
    -0.431045837716155 + m.x6)**2) + m.x132 * ((-0.10668296608426875 + m.x4)**2
    + (-0.1348668647474297 + m.x5)**2 + (-0.2514322339876659 + m.x6)**2) +
    m.x133 * ((-0.6526799327386067 + m.x4)**2 + (-0.026932475138882972 + m.x5)
    **2 + (-0.8536420651804307 + m.x6)**2) + m.x134 * ((-0.6302165389370114 +
    m.x4)**2 + (-0.25833853732983525 + m.x5)**2 + (-0.7144829483905738 + m.x6)
    **2) + m.x135 * ((-0.0630491076625409 + m.x4)**2 + (-0.2533861860136738 +
    m.x5)**2 + (-0.5039058975045216 + m.x6)**2) + m.x136 * ((
    -0.8542315079472844 + m.x4)**2 + (-0.6752218855677596 + m.x5)**2 + (
    -0.03975458066767401 + m.x6)**2) + m.x137 * ((-0.9588366784175165 + m.x4)**
    2 + (-0.15399304462715124 + m.x5)**2 + (-0.18453488984672461 + m.x6)**2) +
    m.x138 * ((-0.577837467669182 + m.x4)**2 + (-0.07039723161872768 + m.x5)**2
    + (-0.4109540294871704 + m.x6)**2) + m.x139 * ((-0.21154639509694562 +
    m.x4)**2 + (-0.450594996440561 + m.x5)**2 + (-0.3493784703429885 + m.x6)**2)
    + m.x140 * ((-0.42089798204034234 + m.x4)**2 + (-0.3399961668152647 + m.x5)
    **2 + (-0.4798458658941379 + m.x6)**2) + m.x141 * ((-0.6572382708452076 +
    m.x4)**2 + (-0.4203009532797096 + m.x5)**2 + (-0.5288398250165213 + m.x6)**
    2) + m.x142 * ((-0.29665432034913075 + m.x4)**2 + (-0.3973578619430581 +
    m.x5)**2 + (-0.07783691735217746 + m.x6)**2) + m.x143 * ((
    -0.45792662283881924 + m.x4)**2 + (-0.5041791032851748 + m.x5)**2 + (
    -0.1594779036498647 + m.x6)**2) + m.x144 * ((-0.3173596228621427 + m.x4)**2
    + (-0.5563727830980914 + m.x5)**2 + (-0.4860010038140109 + m.x6)**2) +
    m.x145 * ((-0.6310766569169546 + m.x4)**2 + (-0.25588647042147916 + m.x5)**
    2 + (-0.8198772382408238 + m.x6)**2) + m.x146 * ((-0.1488692223404685 +
    m.x4)**2 + (-0.9193686903702157 + m.x5)**2 + (-0.34023040415812167 + m.x6)
    **2) + m.x147 * ((-0.2697960633307809 + m.x4)**2 + (-0.335907091585785 +
    m.x5)**2 + (-0.9467428317615326 + m.x6)**2) + m.x148 * ((
    -0.6938343635759197 + m.x4)**2 + (-0.9436133968451139 + m.x5)**2 + (
    -0.991021501717515 + m.x6)**2) + m.x149 * ((-0.4642219155925973 + m.x4)**2
    + (-0.8029654939972901 + m.x5)**2 + (-0.043919917836081845 + m.x6)**2) +
    m.x150 * ((-0.8127682269274624 + m.x4)**2 + (-0.25601168886588366 + m.x5)**
    2 + (-0.3341736569353614 + m.x6)**2) + m.x151 * ((-0.6705401412001404 +
    m.x4)**2 + (-0.5087249365112236 + m.x5)**2 + (-0.5517555972411828 + m.x6)**
    2) + m.x152 * ((-0.32032448244190315 + m.x4)**2 + (-0.39296980599158504 +
    m.x5)**2 + (-0.9198001088344934 + m.x6)**2) + m.x153 * ((
    -0.026348361043022406 + m.x4)**2 + (-0.020629924903295738 + m.x5)**2 + (
    -0.6435466838744265 + m.x6)**2) + m.x154 * ((-0.08245094736473269 + m.x4)**
    2 + (-0.25631060193284183 + m.x5)**2 + (-0.27184690982879867 + m.x6)**2) +
    m.x155 * ((-0.026175964022221 + m.x4)**2 + (-0.39001844671412356 + m.x5)**2
    + (-0.9734667628650259 + m.x6)**2) + m.x156 * ((-0.8602811534294952 + m.x4)
    **2 + (-0.04192541019078189 + m.x5)**2 + (-0.9890062597661148 + m.x6)**2)
    + m.x157 * ((-0.9024392311723397 + m.x4)**2 + (-0.8587679231141961 + m.x5)
    **2 + (-0.17748882176540326 + m.x6)**2) + m.x158 * ((-0.31753107996501695
    + m.x4)**2 + (-0.16045141716999045 + m.x5)**2 + (-0.7376965692150161 +
    m.x6)**2) + m.x159 * ((-0.7179847110204995 + m.x4)**2 + (
    -0.27649224925146654 + m.x5)**2 + (-0.9595943343831328 + m.x6)**2) + m.x160
    * ((-0.7273508397885963 + m.x4)**2 + (-0.7141464054238915 + m.x5)**2 + (
    -0.4236328365996608 + m.x6)**2) + m.x161 * ((-0.8568474154217326 + m.x4)**2
    + (-0.5493004484843343 + m.x5)**2 + (-0.7790605542975685 + m.x6)**2) +
    m.x162 * ((-0.91416162569631 + m.x4)**2 + (-0.07083595559092482 + m.x5)**2
    + (-0.04758287958281404 + m.x6)**2) + m.x163 * ((-0.23610671226901814 +
    m.x4)**2 + (-0.9222887291303542 + m.x5)**2 + (-0.3289139546862677 + m.x6)**
    2) + m.x164 * ((-0.3772829976803017 + m.x4)**2 + (-0.5557643900196702 +
    m.x5)**2 + (-0.5481909082805208 + m.x6)**2) + m.x165 * ((
    -0.4494533670891915 + m.x4)**2 + (-0.8186667716158522 + m.x5)**2 + (
    -0.4636653461366691 + m.x6)**2) + m.x166 * ((-0.7654192246719118 + m.x4)**2
    + (-0.13587703107223248 + m.x5)**2 + (-0.7498343196419972 + m.x6)**2) +
    m.x167 * ((-0.4652456377047164 + m.x4)**2 + (-0.5077984771377264 + m.x5)**2
    + (-0.1348926417621431 + m.x6)**2) + m.x168 * ((-0.8699578841310688 + m.x4)
    **2 + (-0.14273661142672123 + m.x5)**2 + (-0.763817129937746 + m.x6)**2) +
    m.x169 * ((-0.5216108578277676 + m.x4)**2 + (-0.011154425913213695 + m.x5)
    **2 + (-0.9567874437000136 + m.x6)**2) + m.x170 * ((-0.7485755829859556 +
    m.x4)**2 + (-0.10118542234301908 + m.x5)**2 + (-0.1783837759059177 + m.x6)
    **2) + m.x171 * ((-0.9360375934197785 + m.x4)**2 + (-0.4538524923598969 +
    m.x5)**2 + (-0.569108208025147 + m.x6)**2) + m.x172 * ((-0.4192122693219924
    + m.x4)**2 + (-0.005472324326698974 + m.x5)**2 + (-0.07528239578511564 +
    m.x6)**2) + m.x173 * ((-0.26940299166354387 + m.x4)**2 + (
    -0.12687373219539666 + m.x5)**2 + (-0.40516803979431204 + m.x6)**2) +
    m.x174 * ((-0.3914652811474665 + m.x4)**2 + (-0.7630816647003282 + m.x5)**2
    + (-0.029978234429024586 + m.x6)**2) + m.x175 * ((-0.6668476332988318 +
    m.x4)**2 + (-0.24997798690844042 + m.x5)**2 + (-0.6265370286243447 + m.x6)
    **2) + m.x176 * ((-0.34120258424029504 + m.x4)**2 + (-0.07403590994489917
    + m.x5)**2 + (-0.720744885669365 + m.x6)**2) + m.x177 * ((
    -0.06868736363853345 + m.x4)**2 + (-0.816362121123889 + m.x5)**2 + (
    -0.3244522597036481 + m.x6)**2) + m.x178 * ((-0.1133957787796036 + m.x4)**2
    + (-0.5910142596485125 + m.x5)**2 + (-0.6723456801786042 + m.x6)**2) +
    m.x179 * ((-0.9887438686593106 + m.x4)**2 + (-0.21533727799458513 + m.x5)**
    2 + (-0.09743238299874801 + m.x6)**2) + m.x180 * ((-0.9246438240807238 +
    m.x4)**2 + (-0.2700464496762641 + m.x5)**2 + (-0.6245624095989588 + m.x6)**
    2) + m.x181 * ((-0.5656126537021211 + m.x4)**2 + (-0.9818699763888468 +
    m.x5)**2 + (-0.5940226943946902 + m.x6)**2) + m.x182 * ((
    -0.8113977745952538 + m.x4)**2 + (-0.18585378085900206 + m.x5)**2 + (
    -0.7952249374713821 + m.x6)**2) + m.x183 * ((-0.48313873546297303 + m.x4)**
    2 + (-0.7631917439270134 + m.x5)**2 + (-0.6364111963610009 + m.x6)**2) +
    m.x184 * ((-0.1381908613661963 + m.x4)**2 + (-0.402990641918228 + m.x5)**2
    + (-0.6133309405917241 + m.x6)**2) + m.x185 * ((-0.18888139540069937 +
    m.x4)**2 + (-0.3239340910426727 + m.x5)**2 + (-0.29122420662372395 + m.x6)
    **2) + m.x186 * ((-0.45971525577369654 + m.x4)**2 + (-0.8781315029877753 +
    m.x5)**2 + (-0.9416973480122568 + m.x6)**2) + m.x187 * ((
    -0.6421070423802201 + m.x4)**2 + (-0.6746002536392893 + m.x5)**2 + (
    -0.9366116957484414 + m.x6)**2) + m.x188 * ((-0.8617718322773262 + m.x4)**2
    + (-0.5752590469218912 + m.x5)**2 + (-0.03643977625783423 + m.x6)**2) +
    m.x189 * ((-0.3461122806124808 + m.x4)**2 + (-0.26939444151917924 + m.x5)**
    2 + (-0.6117048154287927 + m.x6)**2) + m.x190 * ((-0.3980802568243521 +
    m.x4)**2 + (-0.12833605403046588 + m.x5)**2 + (-0.6550699173363765 + m.x6)
    **2) + m.x191 * ((-0.4212633224085762 + m.x4)**2 + (-0.47619338990426596 +
    m.x5)**2 + (-0.8818640470300284 + m.x6)**2) + m.x192 * ((
    -0.8142723498986452 + m.x4)**2 + (-0.13221974575018447 + m.x5)**2 + (
    -0.5081218602846138 + m.x6)**2) + m.x193 * ((-0.685821187895152 + m.x4)**2
    + (-0.20701052275270038 + m.x5)**2 + (-0.3313231056883219 + m.x6)**2) +
    m.x194 * ((-0.7924211927213229 + m.x4)**2 + (-0.952886214580272 + m.x5)**2
    + (-0.7066600392250384 + m.x6)**2) + m.x195 * ((-0.42315244032379085 +
    m.x4)**2 + (-0.6728665404780181 + m.x5)**2 + (-0.8975501502435518 + m.x6)**
    2) + m.x196 * ((-0.09020963855365849 + m.x4)**2 + (-0.06884955005383797 +
    m.x5)**2 + (-0.6063153645701168 + m.x6)**2) + m.x197 * ((
    -0.9409437143153465 + m.x4)**2 + (-0.923342757310195 + m.x5)**2 + (
    -0.22548223250540067 + m.x6)**2) + m.x198 * ((-0.3513754397940918 + m.x4)**
    2 + (-0.7535548231462733 + m.x5)**2 + (-0.4061213664901868 + m.x6)**2) +
    m.x199 * ((-0.1700085446697267 + m.x4)**2 + (-0.4807483144944905 + m.x5)**2
    + (-0.594505660789073 + m.x6)**2) + m.x200 * ((-0.28626909028581915 + m.x4)
    **2 + (-0.7328949881609186 + m.x5)**2 + (-0.575200065494123 + m.x6)**2) +
    m.x201 * ((-0.4600939889912965 + m.x4)**2 + (-0.2734112416210206 + m.x5)**2
    + (-0.9696488694706376 + m.x6)**2) + m.x202 * ((-0.0599901823942226 + m.x4)
    **2 + (-0.31564380122598423 + m.x5)**2 + (-0.38196492233652524 + m.x6)**2)
    + m.x203 * ((-0.4628907639211667 + m.x4)**2 + (-0.259219253775281 + m.x5)
    **2 + (-0.9040810700491898 + m.x6)**2) + m.x204 * ((-0.27505708621291713 +
    m.x4)**2 + (-0.8080101091456343 + m.x5)**2 + (-0.5596605748627325 + m.x6)**
    2) + m.x205 * ((-0.7306989058987445 + m.x4)**2 + (-0.8522360958952263 +
    m.x5)**2 + (-0.4341637539475691 + m.x6)**2) + m.x206 * ((
    -0.03719257808592946 + m.x4)**2 + (-0.4185738968989311 + m.x5)**2 + (
    -0.018070376182406256 + m.x6)**2) + m.x207 * ((-0.01111267193250065 + m.x4)
    **2 + (-0.07583080853002788 + m.x5)**2 + (-0.11976514020331952 + m.x6)**2)
    + m.x208 * ((-0.881774057941981 + m.x4)**2 + (-0.7524457238077544 + m.x5)
    **2 + (-0.25066589761985636 + m.x6)**2) + m.x209 * ((-0.07955690537673044
    + m.x4)**2 + (-0.030539082027751907 + m.x5)**2 + (-0.42975368767560174 +
    m.x6)**2) + m.x210 * ((-0.03165747404234709 + m.x7)**2 + (
    -0.9688037614558638 + m.x8)**2 + (-0.194905594675844 + m.x9)**2) + m.x211
    * ((-0.994404983268671 + m.x7)**2 + (-0.9467435823614155 + m.x8)**2 + (
    -0.2586761829758428 + m.x9)**2) + m.x212 * ((-0.5162664278327235 + m.x7)**2
    + (-0.3982793402500453 + m.x8)**2 + (-0.40970912928025993 + m.x9)**2) +
    m.x213 * ((-0.7896862520479686 + m.x7)**2 + (-0.8277301347873149 + m.x8)**2
    + (-0.25653942323136325 + m.x9)**2) + m.x214 * ((-0.5439125654987014 +
    m.x7)**2 + (-0.6860092880739965 + m.x8)**2 + (-0.5938661979256709 + m.x9)**
    2) + m.x215 * ((-0.12145860265901365 + m.x7)**2 + (-0.39111450417437643 +
    m.x8)**2 + (-0.4928847200416665 + m.x9)**2) + m.x216 * ((
    -0.9241028428385594 + m.x7)**2 + (-0.8224281118826651 + m.x8)**2 + (
    -0.674823652303014 + m.x9)**2) + m.x217 * ((-0.28018573452261986 + m.x7)**2
    + (-0.9387375342731106 + m.x8)**2 + (-0.22921703916265213 + m.x9)**2) +
    m.x218 * ((-0.33782732597445464 + m.x7)**2 + (-0.1569657415747544 + m.x8)**
    2 + (-0.5890088103246424 + m.x9)**2) + m.x219 * ((-0.7956363045257931 +
    m.x7)**2 + (-0.7018138263270055 + m.x8)**2 + (-0.827204195503925 + m.x9)**2)
    + m.x220 * ((-0.7024344542903443 + m.x7)**2 + (-0.6531462663458645 + m.x8)
    **2 + (-0.25148549322484737 + m.x9)**2) + m.x221 * ((-0.9585188794829803 +
    m.x7)**2 + (-0.9904845118748664 + m.x8)**2 + (-0.7326374193712811 + m.x9)**
    2) + m.x222 * ((-0.9969942571314364 + m.x7)**2 + (-0.8835504075311506 +
    m.x8)**2 + (-0.8772673971146973 + m.x9)**2) + m.x223 * ((
    -0.7568188479193806 + m.x7)**2 + (-0.8118073567007532 + m.x8)**2 + (
    -0.691020784028435 + m.x9)**2) + m.x224 * ((-0.12763593187242794 + m.x7)**2
    + (-0.8373067805693528 + m.x8)**2 + (-0.35242278927521786 + m.x9)**2) +
    m.x225 * ((-0.6436739189615287 + m.x7)**2 + (-0.8993202141020306 + m.x8)**2
    + (-0.49329897886966445 + m.x9)**2) + m.x226 * ((-0.2704172505123661 +
    m.x7)**2 + (-0.5533199618789462 + m.x8)**2 + (-0.8757319534050035 + m.x9)**
    2) + m.x227 * ((-0.8408449490729443 + m.x7)**2 + (-0.9938527400105247 +
    m.x8)**2 + (-0.9078205126634532 + m.x9)**2) + m.x228 * ((
    -0.8048628358106328 + m.x7)**2 + (-0.48485118220454304 + m.x8)**2 + (
    -0.18268576976148887 + m.x9)**2) + m.x229 * ((-0.9327863184767982 + m.x7)**
    2 + (-0.03845948966269497 + m.x8)**2 + (-0.9470512611806989 + m.x9)**2) +
    m.x230 * ((-0.639261595397489 + m.x7)**2 + (-0.23603710481675744 + m.x8)**2
    + (-0.1660094109394994 + m.x9)**2) + m.x231 * ((-0.7169414805312546 + m.x7)
    **2 + (-0.07229070145966299 + m.x8)**2 + (-0.431045837716155 + m.x9)**2) +
    m.x232 * ((-0.10668296608426875 + m.x7)**2 + (-0.1348668647474297 + m.x8)**
    2 + (-0.2514322339876659 + m.x9)**2) + m.x233 * ((-0.6526799327386067 +
    m.x7)**2 + (-0.026932475138882972 + m.x8)**2 + (-0.8536420651804307 + m.x9)
    **2) + m.x234 * ((-0.6302165389370114 + m.x7)**2 + (-0.25833853732983525 +
    m.x8)**2 + (-0.7144829483905738 + m.x9)**2) + m.x235 * ((
    -0.0630491076625409 + m.x7)**2 + (-0.2533861860136738 + m.x8)**2 + (
    -0.5039058975045216 + m.x9)**2) + m.x236 * ((-0.8542315079472844 + m.x7)**2
    + (-0.6752218855677596 + m.x8)**2 + (-0.03975458066767401 + m.x9)**2) +
    m.x237 * ((-0.9588366784175165 + m.x7)**2 + (-0.15399304462715124 + m.x8)**
    2 + (-0.18453488984672461 + m.x9)**2) + m.x238 * ((-0.577837467669182 +
    m.x7)**2 + (-0.07039723161872768 + m.x8)**2 + (-0.4109540294871704 + m.x9)
    **2) + m.x239 * ((-0.21154639509694562 + m.x7)**2 + (-0.450594996440561 +
    m.x8)**2 + (-0.3493784703429885 + m.x9)**2) + m.x240 * ((
    -0.42089798204034234 + m.x7)**2 + (-0.3399961668152647 + m.x8)**2 + (
    -0.4798458658941379 + m.x9)**2) + m.x241 * ((-0.6572382708452076 + m.x7)**2
    + (-0.4203009532797096 + m.x8)**2 + (-0.5288398250165213 + m.x9)**2) +
    m.x242 * ((-0.29665432034913075 + m.x7)**2 + (-0.3973578619430581 + m.x8)**
    2 + (-0.07783691735217746 + m.x9)**2) + m.x243 * ((-0.45792662283881924 +
    m.x7)**2 + (-0.5041791032851748 + m.x8)**2 + (-0.1594779036498647 + m.x9)**
    2) + m.x244 * ((-0.3173596228621427 + m.x7)**2 + (-0.5563727830980914 +
    m.x8)**2 + (-0.4860010038140109 + m.x9)**2) + m.x245 * ((
    -0.6310766569169546 + m.x7)**2 + (-0.25588647042147916 + m.x8)**2 + (
    -0.8198772382408238 + m.x9)**2) + m.x246 * ((-0.1488692223404685 + m.x7)**2
    + (-0.9193686903702157 + m.x8)**2 + (-0.34023040415812167 + m.x9)**2) +
    m.x247 * ((-0.2697960633307809 + m.x7)**2 + (-0.335907091585785 + m.x8)**2
    + (-0.9467428317615326 + m.x9)**2) + m.x248 * ((-0.6938343635759197 + m.x7)
    **2 + (-0.9436133968451139 + m.x8)**2 + (-0.991021501717515 + m.x9)**2) +
    m.x249 * ((-0.4642219155925973 + m.x7)**2 + (-0.8029654939972901 + m.x8)**2
    + (-0.043919917836081845 + m.x9)**2) + m.x250 * ((-0.8127682269274624 +
    m.x7)**2 + (-0.25601168886588366 + m.x8)**2 + (-0.3341736569353614 + m.x9)
    **2) + m.x251 * ((-0.6705401412001404 + m.x7)**2 + (-0.5087249365112236 +
    m.x8)**2 + (-0.5517555972411828 + m.x9)**2) + m.x252 * ((
    -0.32032448244190315 + m.x7)**2 + (-0.39296980599158504 + m.x8)**2 + (
    -0.9198001088344934 + m.x9)**2) + m.x253 * ((-0.026348361043022406 + m.x7)
    **2 + (-0.020629924903295738 + m.x8)**2 + (-0.6435466838744265 + m.x9)**2)
    + m.x254 * ((-0.08245094736473269 + m.x7)**2 + (-0.25631060193284183 +
    m.x8)**2 + (-0.27184690982879867 + m.x9)**2) + m.x255 * ((
    -0.026175964022221 + m.x7)**2 + (-0.39001844671412356 + m.x8)**2 + (
    -0.9734667628650259 + m.x9)**2) + m.x256 * ((-0.8602811534294952 + m.x7)**2
    + (-0.04192541019078189 + m.x8)**2 + (-0.9890062597661148 + m.x9)**2) +
    m.x257 * ((-0.9024392311723397 + m.x7)**2 + (-0.8587679231141961 + m.x8)**2
    + (-0.17748882176540326 + m.x9)**2) + m.x258 * ((-0.31753107996501695 +
    m.x7)**2 + (-0.16045141716999045 + m.x8)**2 + (-0.7376965692150161 + m.x9)
    **2) + m.x259 * ((-0.7179847110204995 + m.x7)**2 + (-0.27649224925146654 +
    m.x8)**2 + (-0.9595943343831328 + m.x9)**2) + m.x260 * ((
    -0.7273508397885963 + m.x7)**2 + (-0.7141464054238915 + m.x8)**2 + (
    -0.4236328365996608 + m.x9)**2) + m.x261 * ((-0.8568474154217326 + m.x7)**2
    + (-0.5493004484843343 + m.x8)**2 + (-0.7790605542975685 + m.x9)**2) +
    m.x262 * ((-0.91416162569631 + m.x7)**2 + (-0.07083595559092482 + m.x8)**2
    + (-0.04758287958281404 + m.x9)**2) + m.x263 * ((-0.23610671226901814 +
    m.x7)**2 + (-0.9222887291303542 + m.x8)**2 + (-0.3289139546862677 + m.x9)**
    2) + m.x264 * ((-0.3772829976803017 + m.x7)**2 + (-0.5557643900196702 +
    m.x8)**2 + (-0.5481909082805208 + m.x9)**2) + m.x265 * ((
    -0.4494533670891915 + m.x7)**2 + (-0.8186667716158522 + m.x8)**2 + (
    -0.4636653461366691 + m.x9)**2) + m.x266 * ((-0.7654192246719118 + m.x7)**2
    + (-0.13587703107223248 + m.x8)**2 + (-0.7498343196419972 + m.x9)**2) +
    m.x267 * ((-0.4652456377047164 + m.x7)**2 + (-0.5077984771377264 + m.x8)**2
    + (-0.1348926417621431 + m.x9)**2) + m.x268 * ((-0.8699578841310688 + m.x7)
    **2 + (-0.14273661142672123 + m.x8)**2 + (-0.763817129937746 + m.x9)**2) +
    m.x269 * ((-0.5216108578277676 + m.x7)**2 + (-0.011154425913213695 + m.x8)
    **2 + (-0.9567874437000136 + m.x9)**2) + m.x270 * ((-0.7485755829859556 +
    m.x7)**2 + (-0.10118542234301908 + m.x8)**2 + (-0.1783837759059177 + m.x9)
    **2) + m.x271 * ((-0.9360375934197785 + m.x7)**2 + (-0.4538524923598969 +
    m.x8)**2 + (-0.569108208025147 + m.x9)**2) + m.x272 * ((-0.4192122693219924
    + m.x7)**2 + (-0.005472324326698974 + m.x8)**2 + (-0.07528239578511564 +
    m.x9)**2) + m.x273 * ((-0.26940299166354387 + m.x7)**2 + (
    -0.12687373219539666 + m.x8)**2 + (-0.40516803979431204 + m.x9)**2) +
    m.x274 * ((-0.3914652811474665 + m.x7)**2 + (-0.7630816647003282 + m.x8)**2
    + (-0.029978234429024586 + m.x9)**2) + m.x275 * ((-0.6668476332988318 +
    m.x7)**2 + (-0.24997798690844042 + m.x8)**2 + (-0.6265370286243447 + m.x9)
    **2) + m.x276 * ((-0.34120258424029504 + m.x7)**2 + (-0.07403590994489917
    + m.x8)**2 + (-0.720744885669365 + m.x9)**2) + m.x277 * ((
    -0.06868736363853345 + m.x7)**2 + (-0.816362121123889 + m.x8)**2 + (
    -0.3244522597036481 + m.x9)**2) + m.x278 * ((-0.1133957787796036 + m.x7)**2
    + (-0.5910142596485125 + m.x8)**2 + (-0.6723456801786042 + m.x9)**2) +
    m.x279 * ((-0.9887438686593106 + m.x7)**2 + (-0.21533727799458513 + m.x8)**
    2 + (-0.09743238299874801 + m.x9)**2) + m.x280 * ((-0.9246438240807238 +
    m.x7)**2 + (-0.2700464496762641 + m.x8)**2 + (-0.6245624095989588 + m.x9)**
    2) + m.x281 * ((-0.5656126537021211 + m.x7)**2 + (-0.9818699763888468 +
    m.x8)**2 + (-0.5940226943946902 + m.x9)**2) + m.x282 * ((
    -0.8113977745952538 + m.x7)**2 + (-0.18585378085900206 + m.x8)**2 + (
    -0.7952249374713821 + m.x9)**2) + m.x283 * ((-0.48313873546297303 + m.x7)**
    2 + (-0.7631917439270134 + m.x8)**2 + (-0.6364111963610009 + m.x9)**2) +
    m.x284 * ((-0.1381908613661963 + m.x7)**2 + (-0.402990641918228 + m.x8)**2
    + (-0.6133309405917241 + m.x9)**2) + m.x285 * ((-0.18888139540069937 +
    m.x7)**2 + (-0.3239340910426727 + m.x8)**2 + (-0.29122420662372395 + m.x9)
    **2) + m.x286 * ((-0.45971525577369654 + m.x7)**2 + (-0.8781315029877753 +
    m.x8)**2 + (-0.9416973480122568 + m.x9)**2) + m.x287 * ((
    -0.6421070423802201 + m.x7)**2 + (-0.6746002536392893 + m.x8)**2 + (
    -0.9366116957484414 + m.x9)**2) + m.x288 * ((-0.8617718322773262 + m.x7)**2
    + (-0.5752590469218912 + m.x8)**2 + (-0.03643977625783423 + m.x9)**2) +
    m.x289 * ((-0.3461122806124808 + m.x7)**2 + (-0.26939444151917924 + m.x8)**
    2 + (-0.6117048154287927 + m.x9)**2) + m.x290 * ((-0.3980802568243521 +
    m.x7)**2 + (-0.12833605403046588 + m.x8)**2 + (-0.6550699173363765 + m.x9)
    **2) + m.x291 * ((-0.4212633224085762 + m.x7)**2 + (-0.47619338990426596 +
    m.x8)**2 + (-0.8818640470300284 + m.x9)**2) + m.x292 * ((
    -0.8142723498986452 + m.x7)**2 + (-0.13221974575018447 + m.x8)**2 + (
    -0.5081218602846138 + m.x9)**2) + m.x293 * ((-0.685821187895152 + m.x7)**2
    + (-0.20701052275270038 + m.x8)**2 + (-0.3313231056883219 + m.x9)**2) +
    m.x294 * ((-0.7924211927213229 + m.x7)**2 + (-0.952886214580272 + m.x8)**2
    + (-0.7066600392250384 + m.x9)**2) + m.x295 * ((-0.42315244032379085 +
    m.x7)**2 + (-0.6728665404780181 + m.x8)**2 + (-0.8975501502435518 + m.x9)**
    2) + m.x296 * ((-0.09020963855365849 + m.x7)**2 + (-0.06884955005383797 +
    m.x8)**2 + (-0.6063153645701168 + m.x9)**2) + m.x297 * ((
    -0.9409437143153465 + m.x7)**2 + (-0.923342757310195 + m.x8)**2 + (
    -0.22548223250540067 + m.x9)**2) + m.x298 * ((-0.3513754397940918 + m.x7)**
    2 + (-0.7535548231462733 + m.x8)**2 + (-0.4061213664901868 + m.x9)**2) +
    m.x299 * ((-0.1700085446697267 + m.x7)**2 + (-0.4807483144944905 + m.x8)**2
    + (-0.594505660789073 + m.x9)**2) + m.x300 * ((-0.28626909028581915 + m.x7)
    **2 + (-0.7328949881609186 + m.x8)**2 + (-0.575200065494123 + m.x9)**2) +
    m.x301 * ((-0.4600939889912965 + m.x7)**2 + (-0.2734112416210206 + m.x8)**2
    + (-0.9696488694706376 + m.x9)**2) + m.x302 * ((-0.0599901823942226 + m.x7)
    **2 + (-0.31564380122598423 + m.x8)**2 + (-0.38196492233652524 + m.x9)**2)
    + m.x303 * ((-0.4628907639211667 + m.x7)**2 + (-0.259219253775281 + m.x8)
    **2 + (-0.9040810700491898 + m.x9)**2) + m.x304 * ((-0.27505708621291713 +
    m.x7)**2 + (-0.8080101091456343 + m.x8)**2 + (-0.5596605748627325 + m.x9)**
    2) + m.x305 * ((-0.7306989058987445 + m.x7)**2 + (-0.8522360958952263 +
    m.x8)**2 + (-0.4341637539475691 + m.x9)**2) + m.x306 * ((
    -0.03719257808592946 + m.x7)**2 + (-0.4185738968989311 + m.x8)**2 + (
    -0.018070376182406256 + m.x9)**2) + m.x307 * ((-0.01111267193250065 + m.x7)
    **2 + (-0.07583080853002788 + m.x8)**2 + (-0.11976514020331952 + m.x9)**2)
    + m.x308 * ((-0.881774057941981 + m.x7)**2 + (-0.7524457238077544 + m.x8)
    **2 + (-0.25066589761985636 + m.x9)**2) + m.x309 * ((-0.07955690537673044
    + m.x7)**2 + (-0.030539082027751907 + m.x8)**2 + (-0.42975368767560174 +
    m.x9)**2))

m.e1 = Constraint(expr= m.x10 + m.x110 + m.x210 == 1)
m.e2 = Constraint(expr= m.x11 + m.x111 + m.x211 == 1)
m.e3 = Constraint(expr= m.x12 + m.x112 + m.x212 == 1)
m.e4 = Constraint(expr= m.x13 + m.x113 + m.x213 == 1)
m.e5 = Constraint(expr= m.x14 + m.x114 + m.x214 == 1)
m.e6 = Constraint(expr= m.x15 + m.x115 + m.x215 == 1)
m.e7 = Constraint(expr= m.x16 + m.x116 + m.x216 == 1)
m.e8 = Constraint(expr= m.x17 + m.x117 + m.x217 == 1)
m.e9 = Constraint(expr= m.x18 + m.x118 + m.x218 == 1)
m.e10 = Constraint(expr= m.x19 + m.x119 + m.x219 == 1)
m.e11 = Constraint(expr= m.x20 + m.x120 + m.x220 == 1)
m.e12 = Constraint(expr= m.x21 + m.x121 + m.x221 == 1)
m.e13 = Constraint(expr= m.x22 + m.x122 + m.x222 == 1)
m.e14 = Constraint(expr= m.x23 + m.x123 + m.x223 == 1)
m.e15 = Constraint(expr= m.x24 + m.x124 + m.x224 == 1)
m.e16 = Constraint(expr= m.x25 + m.x125 + m.x225 == 1)
m.e17 = Constraint(expr= m.x26 + m.x126 + m.x226 == 1)
m.e18 = Constraint(expr= m.x27 + m.x127 + m.x227 == 1)
m.e19 = Constraint(expr= m.x28 + m.x128 + m.x228 == 1)
m.e20 = Constraint(expr= m.x29 + m.x129 + m.x229 == 1)
m.e21 = Constraint(expr= m.x30 + m.x130 + m.x230 == 1)
m.e22 = Constraint(expr= m.x31 + m.x131 + m.x231 == 1)
m.e23 = Constraint(expr= m.x32 + m.x132 + m.x232 == 1)
m.e24 = Constraint(expr= m.x33 + m.x133 + m.x233 == 1)
m.e25 = Constraint(expr= m.x34 + m.x134 + m.x234 == 1)
m.e26 = Constraint(expr= m.x35 + m.x135 + m.x235 == 1)
m.e27 = Constraint(expr= m.x36 + m.x136 + m.x236 == 1)
m.e28 = Constraint(expr= m.x37 + m.x137 + m.x237 == 1)
m.e29 = Constraint(expr= m.x38 + m.x138 + m.x238 == 1)
m.e30 = Constraint(expr= m.x39 + m.x139 + m.x239 == 1)
m.e31 = Constraint(expr= m.x40 + m.x140 + m.x240 == 1)
m.e32 = Constraint(expr= m.x41 + m.x141 + m.x241 == 1)
m.e33 = Constraint(expr= m.x42 + m.x142 + m.x242 == 1)
m.e34 = Constraint(expr= m.x43 + m.x143 + m.x243 == 1)
m.e35 = Constraint(expr= m.x44 + m.x144 + m.x244 == 1)
m.e36 = Constraint(expr= m.x45 + m.x145 + m.x245 == 1)
m.e37 = Constraint(expr= m.x46 + m.x146 + m.x246 == 1)
m.e38 = Constraint(expr= m.x47 + m.x147 + m.x247 == 1)
m.e39 = Constraint(expr= m.x48 + m.x148 + m.x248 == 1)
m.e40 = Constraint(expr= m.x49 + m.x149 + m.x249 == 1)
m.e41 = Constraint(expr= m.x50 + m.x150 + m.x250 == 1)
m.e42 = Constraint(expr= m.x51 + m.x151 + m.x251 == 1)
m.e43 = Constraint(expr= m.x52 + m.x152 + m.x252 == 1)
m.e44 = Constraint(expr= m.x53 + m.x153 + m.x253 == 1)
m.e45 = Constraint(expr= m.x54 + m.x154 + m.x254 == 1)
m.e46 = Constraint(expr= m.x55 + m.x155 + m.x255 == 1)
m.e47 = Constraint(expr= m.x56 + m.x156 + m.x256 == 1)
m.e48 = Constraint(expr= m.x57 + m.x157 + m.x257 == 1)
m.e49 = Constraint(expr= m.x58 + m.x158 + m.x258 == 1)
m.e50 = Constraint(expr= m.x59 + m.x159 + m.x259 == 1)
m.e51 = Constraint(expr= m.x60 + m.x160 + m.x260 == 1)
m.e52 = Constraint(expr= m.x61 + m.x161 + m.x261 == 1)
m.e53 = Constraint(expr= m.x62 + m.x162 + m.x262 == 1)
m.e54 = Constraint(expr= m.x63 + m.x163 + m.x263 == 1)
m.e55 = Constraint(expr= m.x64 + m.x164 + m.x264 == 1)
m.e56 = Constraint(expr= m.x65 + m.x165 + m.x265 == 1)
m.e57 = Constraint(expr= m.x66 + m.x166 + m.x266 == 1)
m.e58 = Constraint(expr= m.x67 + m.x167 + m.x267 == 1)
m.e59 = Constraint(expr= m.x68 + m.x168 + m.x268 == 1)
m.e60 = Constraint(expr= m.x69 + m.x169 + m.x269 == 1)
m.e61 = Constraint(expr= m.x70 + m.x170 + m.x270 == 1)
m.e62 = Constraint(expr= m.x71 + m.x171 + m.x271 == 1)
m.e63 = Constraint(expr= m.x72 + m.x172 + m.x272 == 1)
m.e64 = Constraint(expr= m.x73 + m.x173 + m.x273 == 1)
m.e65 = Constraint(expr= m.x74 + m.x174 + m.x274 == 1)
m.e66 = Constraint(expr= m.x75 + m.x175 + m.x275 == 1)
m.e67 = Constraint(expr= m.x76 + m.x176 + m.x276 == 1)
m.e68 = Constraint(expr= m.x77 + m.x177 + m.x277 == 1)
m.e69 = Constraint(expr= m.x78 + m.x178 + m.x278 == 1)
m.e70 = Constraint(expr= m.x79 + m.x179 + m.x279 == 1)
m.e71 = Constraint(expr= m.x80 + m.x180 + m.x280 == 1)
m.e72 = Constraint(expr= m.x81 + m.x181 + m.x281 == 1)
m.e73 = Constraint(expr= m.x82 + m.x182 + m.x282 == 1)
m.e74 = Constraint(expr= m.x83 + m.x183 + m.x283 == 1)
m.e75 = Constraint(expr= m.x84 + m.x184 + m.x284 == 1)
m.e76 = Constraint(expr= m.x85 + m.x185 + m.x285 == 1)
m.e77 = Constraint(expr= m.x86 + m.x186 + m.x286 == 1)
m.e78 = Constraint(expr= m.x87 + m.x187 + m.x287 == 1)
m.e79 = Constraint(expr= m.x88 + m.x188 + m.x288 == 1)
m.e80 = Constraint(expr= m.x89 + m.x189 + m.x289 == 1)
m.e81 = Constraint(expr= m.x90 + m.x190 + m.x290 == 1)
m.e82 = Constraint(expr= m.x91 + m.x191 + m.x291 == 1)
m.e83 = Constraint(expr= m.x92 + m.x192 + m.x292 == 1)
m.e84 = Constraint(expr= m.x93 + m.x193 + m.x293 == 1)
m.e85 = Constraint(expr= m.x94 + m.x194 + m.x294 == 1)
m.e86 = Constraint(expr= m.x95 + m.x195 + m.x295 == 1)
m.e87 = Constraint(expr= m.x96 + m.x196 + m.x296 == 1)
m.e88 = Constraint(expr= m.x97 + m.x197 + m.x297 == 1)
m.e89 = Constraint(expr= m.x98 + m.x198 + m.x298 == 1)
m.e90 = Constraint(expr= m.x99 + m.x199 + m.x299 == 1)
m.e91 = Constraint(expr= m.x100 + m.x200 + m.x300 == 1)
m.e92 = Constraint(expr= m.x101 + m.x201 + m.x301 == 1)
m.e93 = Constraint(expr= m.x102 + m.x202 + m.x302 == 1)
m.e94 = Constraint(expr= m.x103 + m.x203 + m.x303 == 1)
m.e95 = Constraint(expr= m.x104 + m.x204 + m.x304 == 1)
m.e96 = Constraint(expr= m.x105 + m.x205 + m.x305 == 1)
m.e97 = Constraint(expr= m.x106 + m.x206 + m.x306 == 1)
m.e98 = Constraint(expr= m.x107 + m.x207 + m.x307 == 1)
m.e99 = Constraint(expr= m.x108 + m.x208 + m.x308 == 1)
m.e100 = Constraint(expr= m.x109 + m.x209 + m.x309 == 1)
