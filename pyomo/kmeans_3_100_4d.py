# NLP written by GAMS Convert at 05/15/24 11:42:33
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       100      100        0        0        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#       312      312        0        0        0        0        0        0
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

m.obj = Objective(sense=minimize, expr= m.x13 * ((-0.24964211601093333 + m.x1)
    **2 + (-0.3419590073492983 + m.x2)**2 + (-0.7844078180262489 + m.x3)**2 + (
    -0.8980095182941011 + m.x4)**2) + m.x14 * ((-0.9906481936698904 + m.x1)**2
    + (-0.7326615728808904 + m.x2)**2 + (-0.47742971889426833 + m.x3)**2 + (
    -0.9882689530295113 + m.x4)**2) + m.x15 * ((-0.878674436758325 + m.x1)**2
    + (-0.8431219933716559 + m.x2)**2 + (-0.7444675322325479 + m.x3)**2 + (
    -0.8947995704886033 + m.x4)**2) + m.x16 * ((-0.39792123548266745 + m.x1)**2
    + (-0.6943903328975947 + m.x2)**2 + (-0.9638520040807107 + m.x3)**2 + (
    -0.6532203052778046 + m.x4)**2) + m.x17 * ((-0.879929692712279 + m.x1)**2
    + (-0.9142412852129281 + m.x2)**2 + (-0.14924380524780467 + m.x3)**2 + (
    -0.15875028215543574 + m.x4)**2) + m.x18 * ((-0.7558521689801087 + m.x1)**2
    + (-0.96937066026867 + m.x2)**2 + (-0.5839777272740031 + m.x3)**2 + (
    -0.7969501600511153 + m.x4)**2) + m.x19 * ((-0.7347051533854345 + m.x1)**2
    + (-0.4635465370161904 + m.x2)**2 + (-0.8127541278993364 + m.x3)**2 + (
    -0.7589024492589898 + m.x4)**2) + m.x20 * ((-0.9688344853141951 + m.x1)**2
    + (-0.7464932815830481 + m.x2)**2 + (-0.003186774181423324 + m.x3)**2 + (
    -0.6772369828565289 + m.x4)**2) + m.x21 * ((-0.793653083717306 + m.x1)**2
    + (-0.7282246749807411 + m.x2)**2 + (-0.29096822481565987 + m.x3)**2 + (
    -0.35061900722179007 + m.x4)**2) + m.x22 * ((-0.3650927737246753 + m.x1)**2
    + (-0.8743012218695156 + m.x2)**2 + (-0.6610116252637358 + m.x3)**2 + (
    -0.9720383560062695 + m.x4)**2) + m.x23 * ((-0.11857317643292264 + m.x1)**2
    + (-0.5098381463134666 + m.x2)**2 + (-0.8563940821071722 + m.x3)**2 + (
    -0.41396821296440467 + m.x4)**2) + m.x24 * ((-0.9450588067897289 + m.x1)**2
    + (-0.5581578220274473 + m.x2)**2 + (-0.5424289764585019 + m.x3)**2 + (
    -0.6928432540969558 + m.x4)**2) + m.x25 * ((-0.4821759178166901 + m.x1)**2
    + (-0.7629902918678263 + m.x2)**2 + (-0.5641475698152943 + m.x3)**2 + (
    -0.746729687941132 + m.x4)**2) + m.x26 * ((-0.1051561315969578 + m.x1)**2
    + (-0.16782602220716114 + m.x2)**2 + (-0.07646679656792221 + m.x3)**2 + (
    -0.695001715764455 + m.x4)**2) + m.x27 * ((-0.9182186207603192 + m.x1)**2
    + (-0.735881375421758 + m.x2)**2 + (-0.7213080103672908 + m.x3)**2 + (
    -0.516683896129738 + m.x4)**2) + m.x28 * ((-0.7050551882909638 + m.x1)**2
    + (-0.3867088356880074 + m.x2)**2 + (-0.45777136543270736 + m.x3)**2 + (
    -0.9392949719785977 + m.x4)**2) + m.x29 * ((-0.6458967297664209 + m.x1)**2
    + (-0.3677351639713521 + m.x2)**2 + (-0.33278259039968205 + m.x3)**2 + (
    -0.3245964507574538 + m.x4)**2) + m.x30 * ((-0.47958996099068096 + m.x1)**2
    + (-0.13675416326859657 + m.x2)**2 + (-0.5053244185597753 + m.x3)**2 + (
    -0.0713446376543656 + m.x4)**2) + m.x31 * ((-0.15374285136226773 + m.x1)**2
    + (-0.3564271741066143 + m.x2)**2 + (-0.7338285906513359 + m.x3)**2 + (
    -0.37327140983569274 + m.x4)**2) + m.x32 * ((-0.5979369666516147 + m.x1)**2
    + (-0.6198492487129784 + m.x2)**2 + (-0.10349032792098445 + m.x3)**2 + (
    -0.10017095265374099 + m.x4)**2) + m.x33 * ((-0.3529369856530412 + m.x1)**2
    + (-0.8764108434001858 + m.x2)**2 + (-0.25901225657379046 + m.x3)**2 + (
    -0.9352790003379323 + m.x4)**2) + m.x34 * ((-0.2748015475947406 + m.x1)**2
    + (-0.7176302625191807 + m.x2)**2 + (-0.2438746811226472 + m.x3)**2 + (
    -0.6040784578069498 + m.x4)**2) + m.x35 * ((-0.17938272542204714 + m.x1)**2
    + (-0.38283303612264885 + m.x2)**2 + (-0.6940327920024909 + m.x3)**2 + (
    -0.9252059090045701 + m.x4)**2) + m.x36 * ((-0.445419775127494 + m.x1)**2
    + (-0.21848522689855698 + m.x2)**2 + (-0.9249830911190758 + m.x3)**2 + (
    -0.041725076906418246 + m.x4)**2) + m.x37 * ((-0.2690096255269243 + m.x1)**
    2 + (-0.8663058377192763 + m.x2)**2 + (-0.6606299559632439 + m.x3)**2 + (
    -0.8792065077623004 + m.x4)**2) + m.x38 * ((-0.8453599730102289 + m.x1)**2
    + (-0.3842106658773424 + m.x2)**2 + (-0.8604514302271566 + m.x3)**2 + (
    -0.3525936990974051 + m.x4)**2) + m.x39 * ((-0.32857756535672134 + m.x1)**2
    + (-0.7334509183341946 + m.x2)**2 + (-0.8983960670015203 + m.x3)**2 + (
    -0.38626315586131477 + m.x4)**2) + m.x40 * ((-0.387610966379205 + m.x1)**2
    + (-0.5564208703602945 + m.x2)**2 + (-0.3715036453977122 + m.x3)**2 + (
    -0.48133382594817853 + m.x4)**2) + m.x41 * ((-0.7772976052252489 + m.x1)**2
    + (-0.2985490119048263 + m.x2)**2 + (-0.9388694952604955 + m.x3)**2 + (
    -0.4705205737979742 + m.x4)**2) + m.x42 * ((-0.967667304325787 + m.x1)**2
    + (-0.6681893257652537 + m.x2)**2 + (-0.39836925905485454 + m.x3)**2 + (
    -0.2128045679697267 + m.x4)**2) + m.x43 * ((-0.1003844026114612 + m.x1)**2
    + (-0.06988208009742414 + m.x2)**2 + (-0.5660724747791598 + m.x3)**2 + (
    -0.49681482967935164 + m.x4)**2) + m.x44 * ((-0.5025696134250661 + m.x1)**2
    + (-0.4406022649004441 + m.x2)**2 + (-0.9640458629916471 + m.x3)**2 + (
    -0.6755819991424467 + m.x4)**2) + m.x45 * ((-0.6079930270271675 + m.x1)**2
    + (-0.8229436440461317 + m.x2)**2 + (-0.1720414683789765 + m.x3)**2 + (
    -0.9570171659063009 + m.x4)**2) + m.x46 * ((-0.6143003449233442 + m.x1)**2
    + (-0.46797578776836557 + m.x2)**2 + (-0.11380625741060058 + m.x3)**2 + (
    -0.850797580547296 + m.x4)**2) + m.x47 * ((-0.827981638726401 + m.x1)**2 +
    (-0.07954042483888257 + m.x2)**2 + (-0.01680442249315217 + m.x3)**2 + (
    -0.8358542825777697 + m.x4)**2) + m.x48 * ((-0.638728212928766 + m.x1)**2
    + (-0.1890580846177755 + m.x2)**2 + (-0.4323301757323722 + m.x3)**2 + (
    -0.612343913248689 + m.x4)**2) + m.x49 * ((-0.8665054187135142 + m.x1)**2
    + (-0.6845050451824157 + m.x2)**2 + (-0.23423526491011515 + m.x3)**2 + (
    -0.2210767325507148 + m.x4)**2) + m.x50 * ((-0.5491987365123153 + m.x1)**2
    + (-0.007751236999143818 + m.x2)**2 + (-0.5969443488095496 + m.x3)**2 + (
    -0.9802131870885314 + m.x4)**2) + m.x51 * ((-0.1121271337845755 + m.x1)**2
    + (-0.8154235467169008 + m.x2)**2 + (-0.6071728332788353 + m.x3)**2 + (
    -0.8775136969944712 + m.x4)**2) + m.x52 * ((-0.5732876192647763 + m.x1)**2
    + (-0.7273747273409799 + m.x2)**2 + (-0.5517332762204428 + m.x3)**2 + (
    -0.1351426714674251 + m.x4)**2) + m.x53 * ((-0.8086647204865384 + m.x1)**2
    + (-0.6407098237305914 + m.x2)**2 + (-0.6210964128069524 + m.x3)**2 + (
    -0.44992259520975386 + m.x4)**2) + m.x54 * ((-0.46738864751588893 + m.x1)**
    2 + (-0.16919548510060445 + m.x2)**2 + (-0.0023482587891267004 + m.x3)**2
    + (-0.14987671627442534 + m.x4)**2) + m.x55 * ((-0.28827211638077554 +
    m.x1)**2 + (-0.5861014268422324 + m.x2)**2 + (-0.5277416670647886 + m.x3)**
    2 + (-0.8409977485363904 + m.x4)**2) + m.x56 * ((-0.4413949832799582 + m.x1)
    **2 + (-0.49466756080627283 + m.x2)**2 + (-0.3465268094301722 + m.x3)**2 +
    (-0.5530665936223486 + m.x4)**2) + m.x57 * ((-0.9615961584090456 + m.x1)**2
    + (-0.856521243388868 + m.x2)**2 + (-0.9427784481260063 + m.x3)**2 + (
    -0.4046172659095718 + m.x4)**2) + m.x58 * ((-0.756523124185882 + m.x1)**2
    + (-0.5648078817661226 + m.x2)**2 + (-0.232985268912974 + m.x3)**2 + (
    -0.21179575968397046 + m.x4)**2) + m.x59 * ((-0.4961560863504364 + m.x1)**2
    + (-0.7110422459604598 + m.x2)**2 + (-0.5448790506605838 + m.x3)**2 + (
    -0.17594685300047463 + m.x4)**2) + m.x60 * ((-0.6299940584033505 + m.x1)**2
    + (-0.5292194115870585 + m.x2)**2 + (-0.8939464290699873 + m.x3)**2 + (
    -0.9197280302796716 + m.x4)**2) + m.x61 * ((-0.07389307370742115 + m.x1)**2
    + (-0.005735723177950569 + m.x2)**2 + (-0.4794008583889052 + m.x3)**2 + (
    -0.004539115586572273 + m.x4)**2) + m.x62 * ((-0.9996037605202052 + m.x1)**
    2 + (-0.9276346907826053 + m.x2)**2 + (-0.4785901017911528 + m.x3)**2 + (
    -0.6501272785240141 + m.x4)**2) + m.x63 * ((-0.38815804383589003 + m.x1)**2
    + (-0.18294181500662587 + m.x2)**2 + (-0.5947457416300388 + m.x3)**2 + (
    -0.2560278530547 + m.x4)**2) + m.x64 * ((-0.7881170540431139 + m.x1)**2 + (
    -0.7027070006950007 + m.x2)**2 + (-0.53074558377132 + m.x3)**2 + (
    -0.8168388416742828 + m.x4)**2) + m.x65 * ((-0.4453214297783231 + m.x1)**2
    + (-0.21574727014066197 + m.x2)**2 + (-0.6007833969220481 + m.x3)**2 + (
    -0.9855946507995996 + m.x4)**2) + m.x66 * ((-0.6485865176090697 + m.x1)**2
    + (-0.44908734974576303 + m.x2)**2 + (-0.4781220270372615 + m.x3)**2 + (
    -0.4293696203168158 + m.x4)**2) + m.x67 * ((-0.22720169504325616 + m.x1)**2
    + (-0.8587616013434994 + m.x2)**2 + (-0.7324051963668973 + m.x3)**2 + (
    -0.5094120193360402 + m.x4)**2) + m.x68 * ((-0.9823009891805424 + m.x1)**2
    + (-0.5232149021549913 + m.x2)**2 + (-0.412031878202064 + m.x3)**2 + (
    -0.6575192294028848 + m.x4)**2) + m.x69 * ((-0.3162742657914933 + m.x1)**2
    + (-0.01183887321919197 + m.x2)**2 + (-0.28279267276958464 + m.x3)**2 + (
    -0.7381955824555471 + m.x4)**2) + m.x70 * ((-0.10049965060750066 + m.x1)**2
    + (-0.6649212606311474 + m.x2)**2 + (-0.7422570709815918 + m.x3)**2 + (
    -0.9244921780023644 + m.x4)**2) + m.x71 * ((-0.25620601386823527 + m.x1)**2
    + (-0.6329104710864797 + m.x2)**2 + (-0.8978869916685618 + m.x3)**2 + (
    -0.2752974173020497 + m.x4)**2) + m.x72 * ((-0.9394985975398661 + m.x1)**2
    + (-0.7001974279314537 + m.x2)**2 + (-0.014560287694930452 + m.x3)**2 + (
    -0.9488908278115937 + m.x4)**2) + m.x73 * ((-0.7245223730309341 + m.x1)**2
    + (-0.6320884186727698 + m.x2)**2 + (-0.07010777947378477 + m.x3)**2 + (
    -0.8256332058949165 + m.x4)**2) + m.x74 * ((-0.46210092310001927 + m.x1)**2
    + (-0.9571118885702112 + m.x2)**2 + (-0.8776417657745464 + m.x3)**2 + (
    -0.794260774279357 + m.x4)**2) + m.x75 * ((-0.7164262383633992 + m.x1)**2
    + (-0.0023356372774379075 + m.x2)**2 + (-0.49018974871693954 + m.x3)**2 +
    (-0.6534816823658436 + m.x4)**2) + m.x76 * ((-0.8471452706051823 + m.x1)**2
    + (-0.5501371232455964 + m.x2)**2 + (-0.03173681195462197 + m.x3)**2 + (
    -0.6406988269865684 + m.x4)**2) + m.x77 * ((-0.1027082358959257 + m.x1)**2
    + (-0.6191886965358735 + m.x2)**2 + (-0.0396474941987105 + m.x3)**2 + (
    -0.5076488596145615 + m.x4)**2) + m.x78 * ((-0.8046269662709552 + m.x1)**2
    + (-0.3066096892409601 + m.x2)**2 + (-0.3302085960044877 + m.x3)**2 + (
    -0.08614880449239493 + m.x4)**2) + m.x79 * ((-0.3749077784219944 + m.x1)**2
    + (-0.5535904781787949 + m.x2)**2 + (-0.6638815042064388 + m.x3)**2 + (
    -0.6241565292654414 + m.x4)**2) + m.x80 * ((-0.13070697404601161 + m.x1)**2
    + (-0.8389058296424665 + m.x2)**2 + (-0.4279566452841579 + m.x3)**2 + (
    -0.7044875205084992 + m.x4)**2) + m.x81 * ((-0.984007187389949 + m.x1)**2
    + (-0.27224118643893513 + m.x2)**2 + (-0.8166665195844222 + m.x3)**2 + (
    -0.23429061330082435 + m.x4)**2) + m.x82 * ((-0.13371995393465497 + m.x1)**
    2 + (-0.09101629875551842 + m.x2)**2 + (-0.6358860889565332 + m.x3)**2 + (
    -0.7203605872479781 + m.x4)**2) + m.x83 * ((-0.21301210615938804 + m.x1)**2
    + (-0.374067813581458 + m.x2)**2 + (-0.4204551504954064 + m.x3)**2 + (
    -0.8226407438351983 + m.x4)**2) + m.x84 * ((-0.024944005840480177 + m.x1)**
    2 + (-0.3591318497945377 + m.x2)**2 + (-0.07212577811712384 + m.x3)**2 + (
    -0.23722064628808992 + m.x4)**2) + m.x85 * ((-0.9215935724830766 + m.x1)**2
    + (-0.48518992578278497 + m.x2)**2 + (-0.49296247697911844 + m.x3)**2 + (
    -0.6647712305347205 + m.x4)**2) + m.x86 * ((-0.3648502461028271 + m.x1)**2
    + (-0.06393967071399731 + m.x2)**2 + (-0.13444584514873015 + m.x3)**2 + (
    -0.7247538070080324 + m.x4)**2) + m.x87 * ((-0.5599549291170659 + m.x1)**2
    + (-0.7878758722959883 + m.x2)**2 + (-0.4050992214348107 + m.x3)**2 + (
    -0.33365852278703323 + m.x4)**2) + m.x88 * ((-0.22619084434070347 + m.x1)**
    2 + (-0.8363993872365526 + m.x2)**2 + (-0.5414171155333297 + m.x3)**2 + (
    -0.26081102137714807 + m.x4)**2) + m.x89 * ((-0.4106059415435207 + m.x1)**2
    + (-0.2449826470166595 + m.x2)**2 + (-0.7918909973693952 + m.x3)**2 + (
    -0.8322990701344364 + m.x4)**2) + m.x90 * ((-0.4423186620384577 + m.x1)**2
    + (-0.3434911833537476 + m.x2)**2 + (-0.4922586310817758 + m.x3)**2 + (
    -0.4156203194295037 + m.x4)**2) + m.x91 * ((-0.4100966305674565 + m.x1)**2
    + (-0.40889085523935376 + m.x2)**2 + (-0.29657851165390214 + m.x3)**2 + (
    -0.5620151372110709 + m.x4)**2) + m.x92 * ((-0.49476425027721505 + m.x1)**2
    + (-0.1515747996525948 + m.x2)**2 + (-0.5813822079576554 + m.x3)**2 + (
    -0.8550780240593364 + m.x4)**2) + m.x93 * ((-0.9607123393236836 + m.x1)**2
    + (-0.2115894693522845 + m.x2)**2 + (-0.5058202141411953 + m.x3)**2 + (
    -0.36558409447327245 + m.x4)**2) + m.x94 * ((-0.4144372056522482 + m.x1)**2
    + (-0.6814567356756777 + m.x2)**2 + (-0.5162762586199142 + m.x3)**2 + (
    -0.18355480250892797 + m.x4)**2) + m.x95 * ((-0.10369368475566454 + m.x1)**
    2 + (-0.3542475605882546 + m.x2)**2 + (-0.5761475235592133 + m.x3)**2 + (
    -0.10899138754717175 + m.x4)**2) + m.x96 * ((-0.9592221109557761 + m.x1)**2
    + (-0.08308007601483602 + m.x2)**2 + (-0.12971405470244857 + m.x3)**2 + (
    -0.7934713349037354 + m.x4)**2) + m.x97 * ((-0.16672769537617993 + m.x1)**2
    + (-0.4620486792178481 + m.x2)**2 + (-0.12578399113689387 + m.x3)**2 + (
    -0.38539713316318536 + m.x4)**2) + m.x98 * ((-0.5517536105490606 + m.x1)**2
    + (-0.2010712157545369 + m.x2)**2 + (-0.740004258537079 + m.x3)**2 + (
    -0.6120574660554547 + m.x4)**2) + m.x99 * ((-0.09216614481398766 + m.x1)**2
    + (-0.6715974069959548 + m.x2)**2 + (-0.9909036902685812 + m.x3)**2 + (
    -0.2910896406615172 + m.x4)**2) + m.x100 * ((-0.061660797878906215 + m.x1)
    **2 + (-0.8463868571925466 + m.x2)**2 + (-0.051301503700685314 + m.x3)**2
    + (-0.9114049336321431 + m.x4)**2) + m.x101 * ((-0.05679190664862688 +
    m.x1)**2 + (-0.013741958992455783 + m.x2)**2 + (-0.3782041975972922 + m.x3)
    **2 + (-0.9200396511054753 + m.x4)**2) + m.x102 * ((-0.8710324703596881 +
    m.x1)**2 + (-0.3075614026818573 + m.x2)**2 + (-0.32159528070353627 + m.x3)
    **2 + (-0.1311590448424651 + m.x4)**2) + m.x103 * ((-0.8511091944819653 +
    m.x1)**2 + (-0.6096768636784669 + m.x2)**2 + (-0.6976827163899586 + m.x3)**
    2 + (-0.09357395143425906 + m.x4)**2) + m.x104 * ((-0.44112774234868934 +
    m.x1)**2 + (-0.7819875023204081 + m.x2)**2 + (-0.19576206280698216 + m.x3)
    **2 + (-0.8498406151847044 + m.x4)**2) + m.x105 * ((-0.6525856858316694 +
    m.x1)**2 + (-0.2898780968579091 + m.x2)**2 + (-0.5478678762416052 + m.x3)**
    2 + (-0.19829736411561016 + m.x4)**2) + m.x106 * ((-0.5169426153592779 +
    m.x1)**2 + (-0.2849003652622095 + m.x2)**2 + (-0.7711713988613669 + m.x3)**
    2 + (-0.20962041020553912 + m.x4)**2) + m.x107 * ((-0.17885218632005317 +
    m.x1)**2 + (-0.30706440274562585 + m.x2)**2 + (-0.32500469655501785 + m.x3)
    **2 + (-0.11632561501008132 + m.x4)**2) + m.x108 * ((-0.7029414942629278 +
    m.x1)**2 + (-0.3203281757770885 + m.x2)**2 + (-0.29477293143107486 + m.x3)
    **2 + (-0.16701429916821842 + m.x4)**2) + m.x109 * ((-0.8638995245388986 +
    m.x1)**2 + (-0.8885001879695033 + m.x2)**2 + (-0.1769918520067385 + m.x3)**
    2 + (-0.23867597402221452 + m.x4)**2) + m.x110 * ((-0.725480288484516 +
    m.x1)**2 + (-0.6818807481769296 + m.x2)**2 + (-0.5330537870428049 + m.x3)**
    2 + (-0.09268399911119718 + m.x4)**2) + m.x111 * ((-0.13324778009309624 +
    m.x1)**2 + (-0.7980330434465137 + m.x2)**2 + (-0.8193288420633215 + m.x3)**
    2 + (-0.6273035394858574 + m.x4)**2) + m.x112 * ((-0.6796346159434266 +
    m.x1)**2 + (-0.17745837578198675 + m.x2)**2 + (-0.724534591197156 + m.x3)**
    2 + (-0.35264486204409173 + m.x4)**2) + m.x113 * ((-0.24964211601093333 +
    m.x5)**2 + (-0.3419590073492983 + m.x6)**2 + (-0.7844078180262489 + m.x7)**
    2 + (-0.8980095182941011 + m.x8)**2) + m.x114 * ((-0.9906481936698904 +
    m.x5)**2 + (-0.7326615728808904 + m.x6)**2 + (-0.47742971889426833 + m.x7)
    **2 + (-0.9882689530295113 + m.x8)**2) + m.x115 * ((-0.878674436758325 +
    m.x5)**2 + (-0.8431219933716559 + m.x6)**2 + (-0.7444675322325479 + m.x7)**
    2 + (-0.8947995704886033 + m.x8)**2) + m.x116 * ((-0.39792123548266745 +
    m.x5)**2 + (-0.6943903328975947 + m.x6)**2 + (-0.9638520040807107 + m.x7)**
    2 + (-0.6532203052778046 + m.x8)**2) + m.x117 * ((-0.879929692712279 + m.x5)
    **2 + (-0.9142412852129281 + m.x6)**2 + (-0.14924380524780467 + m.x7)**2 +
    (-0.15875028215543574 + m.x8)**2) + m.x118 * ((-0.7558521689801087 + m.x5)
    **2 + (-0.96937066026867 + m.x6)**2 + (-0.5839777272740031 + m.x7)**2 + (
    -0.7969501600511153 + m.x8)**2) + m.x119 * ((-0.7347051533854345 + m.x5)**2
    + (-0.4635465370161904 + m.x6)**2 + (-0.8127541278993364 + m.x7)**2 + (
    -0.7589024492589898 + m.x8)**2) + m.x120 * ((-0.9688344853141951 + m.x5)**2
    + (-0.7464932815830481 + m.x6)**2 + (-0.003186774181423324 + m.x7)**2 + (
    -0.6772369828565289 + m.x8)**2) + m.x121 * ((-0.793653083717306 + m.x5)**2
    + (-0.7282246749807411 + m.x6)**2 + (-0.29096822481565987 + m.x7)**2 + (
    -0.35061900722179007 + m.x8)**2) + m.x122 * ((-0.3650927737246753 + m.x5)**
    2 + (-0.8743012218695156 + m.x6)**2 + (-0.6610116252637358 + m.x7)**2 + (
    -0.9720383560062695 + m.x8)**2) + m.x123 * ((-0.11857317643292264 + m.x5)**
    2 + (-0.5098381463134666 + m.x6)**2 + (-0.8563940821071722 + m.x7)**2 + (
    -0.41396821296440467 + m.x8)**2) + m.x124 * ((-0.9450588067897289 + m.x5)**
    2 + (-0.5581578220274473 + m.x6)**2 + (-0.5424289764585019 + m.x7)**2 + (
    -0.6928432540969558 + m.x8)**2) + m.x125 * ((-0.4821759178166901 + m.x5)**2
    + (-0.7629902918678263 + m.x6)**2 + (-0.5641475698152943 + m.x7)**2 + (
    -0.746729687941132 + m.x8)**2) + m.x126 * ((-0.1051561315969578 + m.x5)**2
    + (-0.16782602220716114 + m.x6)**2 + (-0.07646679656792221 + m.x7)**2 + (
    -0.695001715764455 + m.x8)**2) + m.x127 * ((-0.9182186207603192 + m.x5)**2
    + (-0.735881375421758 + m.x6)**2 + (-0.7213080103672908 + m.x7)**2 + (
    -0.516683896129738 + m.x8)**2) + m.x128 * ((-0.7050551882909638 + m.x5)**2
    + (-0.3867088356880074 + m.x6)**2 + (-0.45777136543270736 + m.x7)**2 + (
    -0.9392949719785977 + m.x8)**2) + m.x129 * ((-0.6458967297664209 + m.x5)**2
    + (-0.3677351639713521 + m.x6)**2 + (-0.33278259039968205 + m.x7)**2 + (
    -0.3245964507574538 + m.x8)**2) + m.x130 * ((-0.47958996099068096 + m.x5)**
    2 + (-0.13675416326859657 + m.x6)**2 + (-0.5053244185597753 + m.x7)**2 + (
    -0.0713446376543656 + m.x8)**2) + m.x131 * ((-0.15374285136226773 + m.x5)**
    2 + (-0.3564271741066143 + m.x6)**2 + (-0.7338285906513359 + m.x7)**2 + (
    -0.37327140983569274 + m.x8)**2) + m.x132 * ((-0.5979369666516147 + m.x5)**
    2 + (-0.6198492487129784 + m.x6)**2 + (-0.10349032792098445 + m.x7)**2 + (
    -0.10017095265374099 + m.x8)**2) + m.x133 * ((-0.3529369856530412 + m.x5)**
    2 + (-0.8764108434001858 + m.x6)**2 + (-0.25901225657379046 + m.x7)**2 + (
    -0.9352790003379323 + m.x8)**2) + m.x134 * ((-0.2748015475947406 + m.x5)**2
    + (-0.7176302625191807 + m.x6)**2 + (-0.2438746811226472 + m.x7)**2 + (
    -0.6040784578069498 + m.x8)**2) + m.x135 * ((-0.17938272542204714 + m.x5)**
    2 + (-0.38283303612264885 + m.x6)**2 + (-0.6940327920024909 + m.x7)**2 + (
    -0.9252059090045701 + m.x8)**2) + m.x136 * ((-0.445419775127494 + m.x5)**2
    + (-0.21848522689855698 + m.x6)**2 + (-0.9249830911190758 + m.x7)**2 + (
    -0.041725076906418246 + m.x8)**2) + m.x137 * ((-0.2690096255269243 + m.x5)
    **2 + (-0.8663058377192763 + m.x6)**2 + (-0.6606299559632439 + m.x7)**2 + (
    -0.8792065077623004 + m.x8)**2) + m.x138 * ((-0.8453599730102289 + m.x5)**2
    + (-0.3842106658773424 + m.x6)**2 + (-0.8604514302271566 + m.x7)**2 + (
    -0.3525936990974051 + m.x8)**2) + m.x139 * ((-0.32857756535672134 + m.x5)**
    2 + (-0.7334509183341946 + m.x6)**2 + (-0.8983960670015203 + m.x7)**2 + (
    -0.38626315586131477 + m.x8)**2) + m.x140 * ((-0.387610966379205 + m.x5)**2
    + (-0.5564208703602945 + m.x6)**2 + (-0.3715036453977122 + m.x7)**2 + (
    -0.48133382594817853 + m.x8)**2) + m.x141 * ((-0.7772976052252489 + m.x5)**
    2 + (-0.2985490119048263 + m.x6)**2 + (-0.9388694952604955 + m.x7)**2 + (
    -0.4705205737979742 + m.x8)**2) + m.x142 * ((-0.967667304325787 + m.x5)**2
    + (-0.6681893257652537 + m.x6)**2 + (-0.39836925905485454 + m.x7)**2 + (
    -0.2128045679697267 + m.x8)**2) + m.x143 * ((-0.1003844026114612 + m.x5)**2
    + (-0.06988208009742414 + m.x6)**2 + (-0.5660724747791598 + m.x7)**2 + (
    -0.49681482967935164 + m.x8)**2) + m.x144 * ((-0.5025696134250661 + m.x5)**
    2 + (-0.4406022649004441 + m.x6)**2 + (-0.9640458629916471 + m.x7)**2 + (
    -0.6755819991424467 + m.x8)**2) + m.x145 * ((-0.6079930270271675 + m.x5)**2
    + (-0.8229436440461317 + m.x6)**2 + (-0.1720414683789765 + m.x7)**2 + (
    -0.9570171659063009 + m.x8)**2) + m.x146 * ((-0.6143003449233442 + m.x5)**2
    + (-0.46797578776836557 + m.x6)**2 + (-0.11380625741060058 + m.x7)**2 + (
    -0.850797580547296 + m.x8)**2) + m.x147 * ((-0.827981638726401 + m.x5)**2
    + (-0.07954042483888257 + m.x6)**2 + (-0.01680442249315217 + m.x7)**2 + (
    -0.8358542825777697 + m.x8)**2) + m.x148 * ((-0.638728212928766 + m.x5)**2
    + (-0.1890580846177755 + m.x6)**2 + (-0.4323301757323722 + m.x7)**2 + (
    -0.612343913248689 + m.x8)**2) + m.x149 * ((-0.8665054187135142 + m.x5)**2
    + (-0.6845050451824157 + m.x6)**2 + (-0.23423526491011515 + m.x7)**2 + (
    -0.2210767325507148 + m.x8)**2) + m.x150 * ((-0.5491987365123153 + m.x5)**2
    + (-0.007751236999143818 + m.x6)**2 + (-0.5969443488095496 + m.x7)**2 + (
    -0.9802131870885314 + m.x8)**2) + m.x151 * ((-0.1121271337845755 + m.x5)**2
    + (-0.8154235467169008 + m.x6)**2 + (-0.6071728332788353 + m.x7)**2 + (
    -0.8775136969944712 + m.x8)**2) + m.x152 * ((-0.5732876192647763 + m.x5)**2
    + (-0.7273747273409799 + m.x6)**2 + (-0.5517332762204428 + m.x7)**2 + (
    -0.1351426714674251 + m.x8)**2) + m.x153 * ((-0.8086647204865384 + m.x5)**2
    + (-0.6407098237305914 + m.x6)**2 + (-0.6210964128069524 + m.x7)**2 + (
    -0.44992259520975386 + m.x8)**2) + m.x154 * ((-0.46738864751588893 + m.x5)
    **2 + (-0.16919548510060445 + m.x6)**2 + (-0.0023482587891267004 + m.x7)**2
    + (-0.14987671627442534 + m.x8)**2) + m.x155 * ((-0.28827211638077554 +
    m.x5)**2 + (-0.5861014268422324 + m.x6)**2 + (-0.5277416670647886 + m.x7)**
    2 + (-0.8409977485363904 + m.x8)**2) + m.x156 * ((-0.4413949832799582 +
    m.x5)**2 + (-0.49466756080627283 + m.x6)**2 + (-0.3465268094301722 + m.x7)
    **2 + (-0.5530665936223486 + m.x8)**2) + m.x157 * ((-0.9615961584090456 +
    m.x5)**2 + (-0.856521243388868 + m.x6)**2 + (-0.9427784481260063 + m.x7)**2
    + (-0.4046172659095718 + m.x8)**2) + m.x158 * ((-0.756523124185882 + m.x5)
    **2 + (-0.5648078817661226 + m.x6)**2 + (-0.232985268912974 + m.x7)**2 + (
    -0.21179575968397046 + m.x8)**2) + m.x159 * ((-0.4961560863504364 + m.x5)**
    2 + (-0.7110422459604598 + m.x6)**2 + (-0.5448790506605838 + m.x7)**2 + (
    -0.17594685300047463 + m.x8)**2) + m.x160 * ((-0.6299940584033505 + m.x5)**
    2 + (-0.5292194115870585 + m.x6)**2 + (-0.8939464290699873 + m.x7)**2 + (
    -0.9197280302796716 + m.x8)**2) + m.x161 * ((-0.07389307370742115 + m.x5)**
    2 + (-0.005735723177950569 + m.x6)**2 + (-0.4794008583889052 + m.x7)**2 + (
    -0.004539115586572273 + m.x8)**2) + m.x162 * ((-0.9996037605202052 + m.x5)
    **2 + (-0.9276346907826053 + m.x6)**2 + (-0.4785901017911528 + m.x7)**2 + (
    -0.6501272785240141 + m.x8)**2) + m.x163 * ((-0.38815804383589003 + m.x5)**
    2 + (-0.18294181500662587 + m.x6)**2 + (-0.5947457416300388 + m.x7)**2 + (
    -0.2560278530547 + m.x8)**2) + m.x164 * ((-0.7881170540431139 + m.x5)**2 +
    (-0.7027070006950007 + m.x6)**2 + (-0.53074558377132 + m.x7)**2 + (
    -0.8168388416742828 + m.x8)**2) + m.x165 * ((-0.4453214297783231 + m.x5)**2
    + (-0.21574727014066197 + m.x6)**2 + (-0.6007833969220481 + m.x7)**2 + (
    -0.9855946507995996 + m.x8)**2) + m.x166 * ((-0.6485865176090697 + m.x5)**2
    + (-0.44908734974576303 + m.x6)**2 + (-0.4781220270372615 + m.x7)**2 + (
    -0.4293696203168158 + m.x8)**2) + m.x167 * ((-0.22720169504325616 + m.x5)**
    2 + (-0.8587616013434994 + m.x6)**2 + (-0.7324051963668973 + m.x7)**2 + (
    -0.5094120193360402 + m.x8)**2) + m.x168 * ((-0.9823009891805424 + m.x5)**2
    + (-0.5232149021549913 + m.x6)**2 + (-0.412031878202064 + m.x7)**2 + (
    -0.6575192294028848 + m.x8)**2) + m.x169 * ((-0.3162742657914933 + m.x5)**2
    + (-0.01183887321919197 + m.x6)**2 + (-0.28279267276958464 + m.x7)**2 + (
    -0.7381955824555471 + m.x8)**2) + m.x170 * ((-0.10049965060750066 + m.x5)**
    2 + (-0.6649212606311474 + m.x6)**2 + (-0.7422570709815918 + m.x7)**2 + (
    -0.9244921780023644 + m.x8)**2) + m.x171 * ((-0.25620601386823527 + m.x5)**
    2 + (-0.6329104710864797 + m.x6)**2 + (-0.8978869916685618 + m.x7)**2 + (
    -0.2752974173020497 + m.x8)**2) + m.x172 * ((-0.9394985975398661 + m.x5)**2
    + (-0.7001974279314537 + m.x6)**2 + (-0.014560287694930452 + m.x7)**2 + (
    -0.9488908278115937 + m.x8)**2) + m.x173 * ((-0.7245223730309341 + m.x5)**2
    + (-0.6320884186727698 + m.x6)**2 + (-0.07010777947378477 + m.x7)**2 + (
    -0.8256332058949165 + m.x8)**2) + m.x174 * ((-0.46210092310001927 + m.x5)**
    2 + (-0.9571118885702112 + m.x6)**2 + (-0.8776417657745464 + m.x7)**2 + (
    -0.794260774279357 + m.x8)**2) + m.x175 * ((-0.7164262383633992 + m.x5)**2
    + (-0.0023356372774379075 + m.x6)**2 + (-0.49018974871693954 + m.x7)**2 +
    (-0.6534816823658436 + m.x8)**2) + m.x176 * ((-0.8471452706051823 + m.x5)**
    2 + (-0.5501371232455964 + m.x6)**2 + (-0.03173681195462197 + m.x7)**2 + (
    -0.6406988269865684 + m.x8)**2) + m.x177 * ((-0.1027082358959257 + m.x5)**2
    + (-0.6191886965358735 + m.x6)**2 + (-0.0396474941987105 + m.x7)**2 + (
    -0.5076488596145615 + m.x8)**2) + m.x178 * ((-0.8046269662709552 + m.x5)**2
    + (-0.3066096892409601 + m.x6)**2 + (-0.3302085960044877 + m.x7)**2 + (
    -0.08614880449239493 + m.x8)**2) + m.x179 * ((-0.3749077784219944 + m.x5)**
    2 + (-0.5535904781787949 + m.x6)**2 + (-0.6638815042064388 + m.x7)**2 + (
    -0.6241565292654414 + m.x8)**2) + m.x180 * ((-0.13070697404601161 + m.x5)**
    2 + (-0.8389058296424665 + m.x6)**2 + (-0.4279566452841579 + m.x7)**2 + (
    -0.7044875205084992 + m.x8)**2) + m.x181 * ((-0.984007187389949 + m.x5)**2
    + (-0.27224118643893513 + m.x6)**2 + (-0.8166665195844222 + m.x7)**2 + (
    -0.23429061330082435 + m.x8)**2) + m.x182 * ((-0.13371995393465497 + m.x5)
    **2 + (-0.09101629875551842 + m.x6)**2 + (-0.6358860889565332 + m.x7)**2 +
    (-0.7203605872479781 + m.x8)**2) + m.x183 * ((-0.21301210615938804 + m.x5)
    **2 + (-0.374067813581458 + m.x6)**2 + (-0.4204551504954064 + m.x7)**2 + (
    -0.8226407438351983 + m.x8)**2) + m.x184 * ((-0.024944005840480177 + m.x5)
    **2 + (-0.3591318497945377 + m.x6)**2 + (-0.07212577811712384 + m.x7)**2 +
    (-0.23722064628808992 + m.x8)**2) + m.x185 * ((-0.9215935724830766 + m.x5)
    **2 + (-0.48518992578278497 + m.x6)**2 + (-0.49296247697911844 + m.x7)**2
    + (-0.6647712305347205 + m.x8)**2) + m.x186 * ((-0.3648502461028271 + m.x5)
    **2 + (-0.06393967071399731 + m.x6)**2 + (-0.13444584514873015 + m.x7)**2
    + (-0.7247538070080324 + m.x8)**2) + m.x187 * ((-0.5599549291170659 + m.x5)
    **2 + (-0.7878758722959883 + m.x6)**2 + (-0.4050992214348107 + m.x7)**2 + (
    -0.33365852278703323 + m.x8)**2) + m.x188 * ((-0.22619084434070347 + m.x5)
    **2 + (-0.8363993872365526 + m.x6)**2 + (-0.5414171155333297 + m.x7)**2 + (
    -0.26081102137714807 + m.x8)**2) + m.x189 * ((-0.4106059415435207 + m.x5)**
    2 + (-0.2449826470166595 + m.x6)**2 + (-0.7918909973693952 + m.x7)**2 + (
    -0.8322990701344364 + m.x8)**2) + m.x190 * ((-0.4423186620384577 + m.x5)**2
    + (-0.3434911833537476 + m.x6)**2 + (-0.4922586310817758 + m.x7)**2 + (
    -0.4156203194295037 + m.x8)**2) + m.x191 * ((-0.4100966305674565 + m.x5)**2
    + (-0.40889085523935376 + m.x6)**2 + (-0.29657851165390214 + m.x7)**2 + (
    -0.5620151372110709 + m.x8)**2) + m.x192 * ((-0.49476425027721505 + m.x5)**
    2 + (-0.1515747996525948 + m.x6)**2 + (-0.5813822079576554 + m.x7)**2 + (
    -0.8550780240593364 + m.x8)**2) + m.x193 * ((-0.9607123393236836 + m.x5)**2
    + (-0.2115894693522845 + m.x6)**2 + (-0.5058202141411953 + m.x7)**2 + (
    -0.36558409447327245 + m.x8)**2) + m.x194 * ((-0.4144372056522482 + m.x5)**
    2 + (-0.6814567356756777 + m.x6)**2 + (-0.5162762586199142 + m.x7)**2 + (
    -0.18355480250892797 + m.x8)**2) + m.x195 * ((-0.10369368475566454 + m.x5)
    **2 + (-0.3542475605882546 + m.x6)**2 + (-0.5761475235592133 + m.x7)**2 + (
    -0.10899138754717175 + m.x8)**2) + m.x196 * ((-0.9592221109557761 + m.x5)**
    2 + (-0.08308007601483602 + m.x6)**2 + (-0.12971405470244857 + m.x7)**2 + (
    -0.7934713349037354 + m.x8)**2) + m.x197 * ((-0.16672769537617993 + m.x5)**
    2 + (-0.4620486792178481 + m.x6)**2 + (-0.12578399113689387 + m.x7)**2 + (
    -0.38539713316318536 + m.x8)**2) + m.x198 * ((-0.5517536105490606 + m.x5)**
    2 + (-0.2010712157545369 + m.x6)**2 + (-0.740004258537079 + m.x7)**2 + (
    -0.6120574660554547 + m.x8)**2) + m.x199 * ((-0.09216614481398766 + m.x5)**
    2 + (-0.6715974069959548 + m.x6)**2 + (-0.9909036902685812 + m.x7)**2 + (
    -0.2910896406615172 + m.x8)**2) + m.x200 * ((-0.061660797878906215 + m.x5)
    **2 + (-0.8463868571925466 + m.x6)**2 + (-0.051301503700685314 + m.x7)**2
    + (-0.9114049336321431 + m.x8)**2) + m.x201 * ((-0.05679190664862688 +
    m.x5)**2 + (-0.013741958992455783 + m.x6)**2 + (-0.3782041975972922 + m.x7)
    **2 + (-0.9200396511054753 + m.x8)**2) + m.x202 * ((-0.8710324703596881 +
    m.x5)**2 + (-0.3075614026818573 + m.x6)**2 + (-0.32159528070353627 + m.x7)
    **2 + (-0.1311590448424651 + m.x8)**2) + m.x203 * ((-0.8511091944819653 +
    m.x5)**2 + (-0.6096768636784669 + m.x6)**2 + (-0.6976827163899586 + m.x7)**
    2 + (-0.09357395143425906 + m.x8)**2) + m.x204 * ((-0.44112774234868934 +
    m.x5)**2 + (-0.7819875023204081 + m.x6)**2 + (-0.19576206280698216 + m.x7)
    **2 + (-0.8498406151847044 + m.x8)**2) + m.x205 * ((-0.6525856858316694 +
    m.x5)**2 + (-0.2898780968579091 + m.x6)**2 + (-0.5478678762416052 + m.x7)**
    2 + (-0.19829736411561016 + m.x8)**2) + m.x206 * ((-0.5169426153592779 +
    m.x5)**2 + (-0.2849003652622095 + m.x6)**2 + (-0.7711713988613669 + m.x7)**
    2 + (-0.20962041020553912 + m.x8)**2) + m.x207 * ((-0.17885218632005317 +
    m.x5)**2 + (-0.30706440274562585 + m.x6)**2 + (-0.32500469655501785 + m.x7)
    **2 + (-0.11632561501008132 + m.x8)**2) + m.x208 * ((-0.7029414942629278 +
    m.x5)**2 + (-0.3203281757770885 + m.x6)**2 + (-0.29477293143107486 + m.x7)
    **2 + (-0.16701429916821842 + m.x8)**2) + m.x209 * ((-0.8638995245388986 +
    m.x5)**2 + (-0.8885001879695033 + m.x6)**2 + (-0.1769918520067385 + m.x7)**
    2 + (-0.23867597402221452 + m.x8)**2) + m.x210 * ((-0.725480288484516 +
    m.x5)**2 + (-0.6818807481769296 + m.x6)**2 + (-0.5330537870428049 + m.x7)**
    2 + (-0.09268399911119718 + m.x8)**2) + m.x211 * ((-0.13324778009309624 +
    m.x5)**2 + (-0.7980330434465137 + m.x6)**2 + (-0.8193288420633215 + m.x7)**
    2 + (-0.6273035394858574 + m.x8)**2) + m.x212 * ((-0.6796346159434266 +
    m.x5)**2 + (-0.17745837578198675 + m.x6)**2 + (-0.724534591197156 + m.x7)**
    2 + (-0.35264486204409173 + m.x8)**2) + m.x213 * ((-0.24964211601093333 +
    m.x9)**2 + (-0.3419590073492983 + m.x10)**2 + (-0.7844078180262489 + m.x11)
    **2 + (-0.8980095182941011 + m.x12)**2) + m.x214 * ((-0.9906481936698904 +
    m.x9)**2 + (-0.7326615728808904 + m.x10)**2 + (-0.47742971889426833 + m.x11)
    **2 + (-0.9882689530295113 + m.x12)**2) + m.x215 * ((-0.878674436758325 +
    m.x9)**2 + (-0.8431219933716559 + m.x10)**2 + (-0.7444675322325479 + m.x11)
    **2 + (-0.8947995704886033 + m.x12)**2) + m.x216 * ((-0.39792123548266745
    + m.x9)**2 + (-0.6943903328975947 + m.x10)**2 + (-0.9638520040807107 +
    m.x11)**2 + (-0.6532203052778046 + m.x12)**2) + m.x217 * ((
    -0.879929692712279 + m.x9)**2 + (-0.9142412852129281 + m.x10)**2 + (
    -0.14924380524780467 + m.x11)**2 + (-0.15875028215543574 + m.x12)**2) +
    m.x218 * ((-0.7558521689801087 + m.x9)**2 + (-0.96937066026867 + m.x10)**2
    + (-0.5839777272740031 + m.x11)**2 + (-0.7969501600511153 + m.x12)**2) +
    m.x219 * ((-0.7347051533854345 + m.x9)**2 + (-0.4635465370161904 + m.x10)**
    2 + (-0.8127541278993364 + m.x11)**2 + (-0.7589024492589898 + m.x12)**2) +
    m.x220 * ((-0.9688344853141951 + m.x9)**2 + (-0.7464932815830481 + m.x10)**
    2 + (-0.003186774181423324 + m.x11)**2 + (-0.6772369828565289 + m.x12)**2)
    + m.x221 * ((-0.793653083717306 + m.x9)**2 + (-0.7282246749807411 + m.x10)
    **2 + (-0.29096822481565987 + m.x11)**2 + (-0.35061900722179007 + m.x12)**2)
    + m.x222 * ((-0.3650927737246753 + m.x9)**2 + (-0.8743012218695156 + m.x10)
    **2 + (-0.6610116252637358 + m.x11)**2 + (-0.9720383560062695 + m.x12)**2)
    + m.x223 * ((-0.11857317643292264 + m.x9)**2 + (-0.5098381463134666 +
    m.x10)**2 + (-0.8563940821071722 + m.x11)**2 + (-0.41396821296440467 +
    m.x12)**2) + m.x224 * ((-0.9450588067897289 + m.x9)**2 + (
    -0.5581578220274473 + m.x10)**2 + (-0.5424289764585019 + m.x11)**2 + (
    -0.6928432540969558 + m.x12)**2) + m.x225 * ((-0.4821759178166901 + m.x9)**
    2 + (-0.7629902918678263 + m.x10)**2 + (-0.5641475698152943 + m.x11)**2 + (
    -0.746729687941132 + m.x12)**2) + m.x226 * ((-0.1051561315969578 + m.x9)**2
    + (-0.16782602220716114 + m.x10)**2 + (-0.07646679656792221 + m.x11)**2 +
    (-0.695001715764455 + m.x12)**2) + m.x227 * ((-0.9182186207603192 + m.x9)**
    2 + (-0.735881375421758 + m.x10)**2 + (-0.7213080103672908 + m.x11)**2 + (
    -0.516683896129738 + m.x12)**2) + m.x228 * ((-0.7050551882909638 + m.x9)**2
    + (-0.3867088356880074 + m.x10)**2 + (-0.45777136543270736 + m.x11)**2 + (
    -0.9392949719785977 + m.x12)**2) + m.x229 * ((-0.6458967297664209 + m.x9)**
    2 + (-0.3677351639713521 + m.x10)**2 + (-0.33278259039968205 + m.x11)**2 +
    (-0.3245964507574538 + m.x12)**2) + m.x230 * ((-0.47958996099068096 + m.x9)
    **2 + (-0.13675416326859657 + m.x10)**2 + (-0.5053244185597753 + m.x11)**2
    + (-0.0713446376543656 + m.x12)**2) + m.x231 * ((-0.15374285136226773 +
    m.x9)**2 + (-0.3564271741066143 + m.x10)**2 + (-0.7338285906513359 + m.x11)
    **2 + (-0.37327140983569274 + m.x12)**2) + m.x232 * ((-0.5979369666516147
    + m.x9)**2 + (-0.6198492487129784 + m.x10)**2 + (-0.10349032792098445 +
    m.x11)**2 + (-0.10017095265374099 + m.x12)**2) + m.x233 * ((
    -0.3529369856530412 + m.x9)**2 + (-0.8764108434001858 + m.x10)**2 + (
    -0.25901225657379046 + m.x11)**2 + (-0.9352790003379323 + m.x12)**2) +
    m.x234 * ((-0.2748015475947406 + m.x9)**2 + (-0.7176302625191807 + m.x10)**
    2 + (-0.2438746811226472 + m.x11)**2 + (-0.6040784578069498 + m.x12)**2) +
    m.x235 * ((-0.17938272542204714 + m.x9)**2 + (-0.38283303612264885 + m.x10)
    **2 + (-0.6940327920024909 + m.x11)**2 + (-0.9252059090045701 + m.x12)**2)
    + m.x236 * ((-0.445419775127494 + m.x9)**2 + (-0.21848522689855698 + m.x10)
    **2 + (-0.9249830911190758 + m.x11)**2 + (-0.041725076906418246 + m.x12)**2)
    + m.x237 * ((-0.2690096255269243 + m.x9)**2 + (-0.8663058377192763 + m.x10)
    **2 + (-0.6606299559632439 + m.x11)**2 + (-0.8792065077623004 + m.x12)**2)
    + m.x238 * ((-0.8453599730102289 + m.x9)**2 + (-0.3842106658773424 + m.x10)
    **2 + (-0.8604514302271566 + m.x11)**2 + (-0.3525936990974051 + m.x12)**2)
    + m.x239 * ((-0.32857756535672134 + m.x9)**2 + (-0.7334509183341946 +
    m.x10)**2 + (-0.8983960670015203 + m.x11)**2 + (-0.38626315586131477 +
    m.x12)**2) + m.x240 * ((-0.387610966379205 + m.x9)**2 + (
    -0.5564208703602945 + m.x10)**2 + (-0.3715036453977122 + m.x11)**2 + (
    -0.48133382594817853 + m.x12)**2) + m.x241 * ((-0.7772976052252489 + m.x9)
    **2 + (-0.2985490119048263 + m.x10)**2 + (-0.9388694952604955 + m.x11)**2
    + (-0.4705205737979742 + m.x12)**2) + m.x242 * ((-0.967667304325787 + m.x9)
    **2 + (-0.6681893257652537 + m.x10)**2 + (-0.39836925905485454 + m.x11)**2
    + (-0.2128045679697267 + m.x12)**2) + m.x243 * ((-0.1003844026114612 +
    m.x9)**2 + (-0.06988208009742414 + m.x10)**2 + (-0.5660724747791598 + m.x11)
    **2 + (-0.49681482967935164 + m.x12)**2) + m.x244 * ((-0.5025696134250661
    + m.x9)**2 + (-0.4406022649004441 + m.x10)**2 + (-0.9640458629916471 +
    m.x11)**2 + (-0.6755819991424467 + m.x12)**2) + m.x245 * ((
    -0.6079930270271675 + m.x9)**2 + (-0.8229436440461317 + m.x10)**2 + (
    -0.1720414683789765 + m.x11)**2 + (-0.9570171659063009 + m.x12)**2) +
    m.x246 * ((-0.6143003449233442 + m.x9)**2 + (-0.46797578776836557 + m.x10)
    **2 + (-0.11380625741060058 + m.x11)**2 + (-0.850797580547296 + m.x12)**2)
    + m.x247 * ((-0.827981638726401 + m.x9)**2 + (-0.07954042483888257 + m.x10)
    **2 + (-0.01680442249315217 + m.x11)**2 + (-0.8358542825777697 + m.x12)**2)
    + m.x248 * ((-0.638728212928766 + m.x9)**2 + (-0.1890580846177755 + m.x10)
    **2 + (-0.4323301757323722 + m.x11)**2 + (-0.612343913248689 + m.x12)**2)
    + m.x249 * ((-0.8665054187135142 + m.x9)**2 + (-0.6845050451824157 + m.x10)
    **2 + (-0.23423526491011515 + m.x11)**2 + (-0.2210767325507148 + m.x12)**2)
    + m.x250 * ((-0.5491987365123153 + m.x9)**2 + (-0.007751236999143818 +
    m.x10)**2 + (-0.5969443488095496 + m.x11)**2 + (-0.9802131870885314 + m.x12)
    **2) + m.x251 * ((-0.1121271337845755 + m.x9)**2 + (-0.8154235467169008 +
    m.x10)**2 + (-0.6071728332788353 + m.x11)**2 + (-0.8775136969944712 + m.x12)
    **2) + m.x252 * ((-0.5732876192647763 + m.x9)**2 + (-0.7273747273409799 +
    m.x10)**2 + (-0.5517332762204428 + m.x11)**2 + (-0.1351426714674251 + m.x12)
    **2) + m.x253 * ((-0.8086647204865384 + m.x9)**2 + (-0.6407098237305914 +
    m.x10)**2 + (-0.6210964128069524 + m.x11)**2 + (-0.44992259520975386 +
    m.x12)**2) + m.x254 * ((-0.46738864751588893 + m.x9)**2 + (
    -0.16919548510060445 + m.x10)**2 + (-0.0023482587891267004 + m.x11)**2 + (
    -0.14987671627442534 + m.x12)**2) + m.x255 * ((-0.28827211638077554 + m.x9)
    **2 + (-0.5861014268422324 + m.x10)**2 + (-0.5277416670647886 + m.x11)**2
    + (-0.8409977485363904 + m.x12)**2) + m.x256 * ((-0.4413949832799582 +
    m.x9)**2 + (-0.49466756080627283 + m.x10)**2 + (-0.3465268094301722 + m.x11)
    **2 + (-0.5530665936223486 + m.x12)**2) + m.x257 * ((-0.9615961584090456 +
    m.x9)**2 + (-0.856521243388868 + m.x10)**2 + (-0.9427784481260063 + m.x11)
    **2 + (-0.4046172659095718 + m.x12)**2) + m.x258 * ((-0.756523124185882 +
    m.x9)**2 + (-0.5648078817661226 + m.x10)**2 + (-0.232985268912974 + m.x11)
    **2 + (-0.21179575968397046 + m.x12)**2) + m.x259 * ((-0.4961560863504364
    + m.x9)**2 + (-0.7110422459604598 + m.x10)**2 + (-0.5448790506605838 +
    m.x11)**2 + (-0.17594685300047463 + m.x12)**2) + m.x260 * ((
    -0.6299940584033505 + m.x9)**2 + (-0.5292194115870585 + m.x10)**2 + (
    -0.8939464290699873 + m.x11)**2 + (-0.9197280302796716 + m.x12)**2) +
    m.x261 * ((-0.07389307370742115 + m.x9)**2 + (-0.005735723177950569 + m.x10)
    **2 + (-0.4794008583889052 + m.x11)**2 + (-0.004539115586572273 + m.x12)**2)
    + m.x262 * ((-0.9996037605202052 + m.x9)**2 + (-0.9276346907826053 + m.x10)
    **2 + (-0.4785901017911528 + m.x11)**2 + (-0.6501272785240141 + m.x12)**2)
    + m.x263 * ((-0.38815804383589003 + m.x9)**2 + (-0.18294181500662587 +
    m.x10)**2 + (-0.5947457416300388 + m.x11)**2 + (-0.2560278530547 + m.x12)**
    2) + m.x264 * ((-0.7881170540431139 + m.x9)**2 + (-0.7027070006950007 +
    m.x10)**2 + (-0.53074558377132 + m.x11)**2 + (-0.8168388416742828 + m.x12)
    **2) + m.x265 * ((-0.4453214297783231 + m.x9)**2 + (-0.21574727014066197 +
    m.x10)**2 + (-0.6007833969220481 + m.x11)**2 + (-0.9855946507995996 + m.x12)
    **2) + m.x266 * ((-0.6485865176090697 + m.x9)**2 + (-0.44908734974576303 +
    m.x10)**2 + (-0.4781220270372615 + m.x11)**2 + (-0.4293696203168158 + m.x12)
    **2) + m.x267 * ((-0.22720169504325616 + m.x9)**2 + (-0.8587616013434994 +
    m.x10)**2 + (-0.7324051963668973 + m.x11)**2 + (-0.5094120193360402 + m.x12)
    **2) + m.x268 * ((-0.9823009891805424 + m.x9)**2 + (-0.5232149021549913 +
    m.x10)**2 + (-0.412031878202064 + m.x11)**2 + (-0.6575192294028848 + m.x12)
    **2) + m.x269 * ((-0.3162742657914933 + m.x9)**2 + (-0.01183887321919197 +
    m.x10)**2 + (-0.28279267276958464 + m.x11)**2 + (-0.7381955824555471 +
    m.x12)**2) + m.x270 * ((-0.10049965060750066 + m.x9)**2 + (
    -0.6649212606311474 + m.x10)**2 + (-0.7422570709815918 + m.x11)**2 + (
    -0.9244921780023644 + m.x12)**2) + m.x271 * ((-0.25620601386823527 + m.x9)
    **2 + (-0.6329104710864797 + m.x10)**2 + (-0.8978869916685618 + m.x11)**2
    + (-0.2752974173020497 + m.x12)**2) + m.x272 * ((-0.9394985975398661 +
    m.x9)**2 + (-0.7001974279314537 + m.x10)**2 + (-0.014560287694930452 +
    m.x11)**2 + (-0.9488908278115937 + m.x12)**2) + m.x273 * ((
    -0.7245223730309341 + m.x9)**2 + (-0.6320884186727698 + m.x10)**2 + (
    -0.07010777947378477 + m.x11)**2 + (-0.8256332058949165 + m.x12)**2) +
    m.x274 * ((-0.46210092310001927 + m.x9)**2 + (-0.9571118885702112 + m.x10)
    **2 + (-0.8776417657745464 + m.x11)**2 + (-0.794260774279357 + m.x12)**2)
    + m.x275 * ((-0.7164262383633992 + m.x9)**2 + (-0.0023356372774379075 +
    m.x10)**2 + (-0.49018974871693954 + m.x11)**2 + (-0.6534816823658436 +
    m.x12)**2) + m.x276 * ((-0.8471452706051823 + m.x9)**2 + (
    -0.5501371232455964 + m.x10)**2 + (-0.03173681195462197 + m.x11)**2 + (
    -0.6406988269865684 + m.x12)**2) + m.x277 * ((-0.1027082358959257 + m.x9)**
    2 + (-0.6191886965358735 + m.x10)**2 + (-0.0396474941987105 + m.x11)**2 + (
    -0.5076488596145615 + m.x12)**2) + m.x278 * ((-0.8046269662709552 + m.x9)**
    2 + (-0.3066096892409601 + m.x10)**2 + (-0.3302085960044877 + m.x11)**2 + (
    -0.08614880449239493 + m.x12)**2) + m.x279 * ((-0.3749077784219944 + m.x9)
    **2 + (-0.5535904781787949 + m.x10)**2 + (-0.6638815042064388 + m.x11)**2
    + (-0.6241565292654414 + m.x12)**2) + m.x280 * ((-0.13070697404601161 +
    m.x9)**2 + (-0.8389058296424665 + m.x10)**2 + (-0.4279566452841579 + m.x11)
    **2 + (-0.7044875205084992 + m.x12)**2) + m.x281 * ((-0.984007187389949 +
    m.x9)**2 + (-0.27224118643893513 + m.x10)**2 + (-0.8166665195844222 + m.x11)
    **2 + (-0.23429061330082435 + m.x12)**2) + m.x282 * ((-0.13371995393465497
    + m.x9)**2 + (-0.09101629875551842 + m.x10)**2 + (-0.6358860889565332 +
    m.x11)**2 + (-0.7203605872479781 + m.x12)**2) + m.x283 * ((
    -0.21301210615938804 + m.x9)**2 + (-0.374067813581458 + m.x10)**2 + (
    -0.4204551504954064 + m.x11)**2 + (-0.8226407438351983 + m.x12)**2) +
    m.x284 * ((-0.024944005840480177 + m.x9)**2 + (-0.3591318497945377 + m.x10)
    **2 + (-0.07212577811712384 + m.x11)**2 + (-0.23722064628808992 + m.x12)**2)
    + m.x285 * ((-0.9215935724830766 + m.x9)**2 + (-0.48518992578278497 +
    m.x10)**2 + (-0.49296247697911844 + m.x11)**2 + (-0.6647712305347205 +
    m.x12)**2) + m.x286 * ((-0.3648502461028271 + m.x9)**2 + (
    -0.06393967071399731 + m.x10)**2 + (-0.13444584514873015 + m.x11)**2 + (
    -0.7247538070080324 + m.x12)**2) + m.x287 * ((-0.5599549291170659 + m.x9)**
    2 + (-0.7878758722959883 + m.x10)**2 + (-0.4050992214348107 + m.x11)**2 + (
    -0.33365852278703323 + m.x12)**2) + m.x288 * ((-0.22619084434070347 + m.x9)
    **2 + (-0.8363993872365526 + m.x10)**2 + (-0.5414171155333297 + m.x11)**2
    + (-0.26081102137714807 + m.x12)**2) + m.x289 * ((-0.4106059415435207 +
    m.x9)**2 + (-0.2449826470166595 + m.x10)**2 + (-0.7918909973693952 + m.x11)
    **2 + (-0.8322990701344364 + m.x12)**2) + m.x290 * ((-0.4423186620384577 +
    m.x9)**2 + (-0.3434911833537476 + m.x10)**2 + (-0.4922586310817758 + m.x11)
    **2 + (-0.4156203194295037 + m.x12)**2) + m.x291 * ((-0.4100966305674565 +
    m.x9)**2 + (-0.40889085523935376 + m.x10)**2 + (-0.29657851165390214 +
    m.x11)**2 + (-0.5620151372110709 + m.x12)**2) + m.x292 * ((
    -0.49476425027721505 + m.x9)**2 + (-0.1515747996525948 + m.x10)**2 + (
    -0.5813822079576554 + m.x11)**2 + (-0.8550780240593364 + m.x12)**2) +
    m.x293 * ((-0.9607123393236836 + m.x9)**2 + (-0.2115894693522845 + m.x10)**
    2 + (-0.5058202141411953 + m.x11)**2 + (-0.36558409447327245 + m.x12)**2)
    + m.x294 * ((-0.4144372056522482 + m.x9)**2 + (-0.6814567356756777 + m.x10)
    **2 + (-0.5162762586199142 + m.x11)**2 + (-0.18355480250892797 + m.x12)**2)
    + m.x295 * ((-0.10369368475566454 + m.x9)**2 + (-0.3542475605882546 +
    m.x10)**2 + (-0.5761475235592133 + m.x11)**2 + (-0.10899138754717175 +
    m.x12)**2) + m.x296 * ((-0.9592221109557761 + m.x9)**2 + (
    -0.08308007601483602 + m.x10)**2 + (-0.12971405470244857 + m.x11)**2 + (
    -0.7934713349037354 + m.x12)**2) + m.x297 * ((-0.16672769537617993 + m.x9)
    **2 + (-0.4620486792178481 + m.x10)**2 + (-0.12578399113689387 + m.x11)**2
    + (-0.38539713316318536 + m.x12)**2) + m.x298 * ((-0.5517536105490606 +
    m.x9)**2 + (-0.2010712157545369 + m.x10)**2 + (-0.740004258537079 + m.x11)
    **2 + (-0.6120574660554547 + m.x12)**2) + m.x299 * ((-0.09216614481398766
    + m.x9)**2 + (-0.6715974069959548 + m.x10)**2 + (-0.9909036902685812 +
    m.x11)**2 + (-0.2910896406615172 + m.x12)**2) + m.x300 * ((
    -0.061660797878906215 + m.x9)**2 + (-0.8463868571925466 + m.x10)**2 + (
    -0.051301503700685314 + m.x11)**2 + (-0.9114049336321431 + m.x12)**2) +
    m.x301 * ((-0.05679190664862688 + m.x9)**2 + (-0.013741958992455783 + m.x10)
    **2 + (-0.3782041975972922 + m.x11)**2 + (-0.9200396511054753 + m.x12)**2)
    + m.x302 * ((-0.8710324703596881 + m.x9)**2 + (-0.3075614026818573 + m.x10)
    **2 + (-0.32159528070353627 + m.x11)**2 + (-0.1311590448424651 + m.x12)**2)
    + m.x303 * ((-0.8511091944819653 + m.x9)**2 + (-0.6096768636784669 + m.x10)
    **2 + (-0.6976827163899586 + m.x11)**2 + (-0.09357395143425906 + m.x12)**2)
    + m.x304 * ((-0.44112774234868934 + m.x9)**2 + (-0.7819875023204081 +
    m.x10)**2 + (-0.19576206280698216 + m.x11)**2 + (-0.8498406151847044 +
    m.x12)**2) + m.x305 * ((-0.6525856858316694 + m.x9)**2 + (
    -0.2898780968579091 + m.x10)**2 + (-0.5478678762416052 + m.x11)**2 + (
    -0.19829736411561016 + m.x12)**2) + m.x306 * ((-0.5169426153592779 + m.x9)
    **2 + (-0.2849003652622095 + m.x10)**2 + (-0.7711713988613669 + m.x11)**2
    + (-0.20962041020553912 + m.x12)**2) + m.x307 * ((-0.17885218632005317 +
    m.x9)**2 + (-0.30706440274562585 + m.x10)**2 + (-0.32500469655501785 +
    m.x11)**2 + (-0.11632561501008132 + m.x12)**2) + m.x308 * ((
    -0.7029414942629278 + m.x9)**2 + (-0.3203281757770885 + m.x10)**2 + (
    -0.29477293143107486 + m.x11)**2 + (-0.16701429916821842 + m.x12)**2) +
    m.x309 * ((-0.8638995245388986 + m.x9)**2 + (-0.8885001879695033 + m.x10)**
    2 + (-0.1769918520067385 + m.x11)**2 + (-0.23867597402221452 + m.x12)**2)
    + m.x310 * ((-0.725480288484516 + m.x9)**2 + (-0.6818807481769296 + m.x10)
    **2 + (-0.5330537870428049 + m.x11)**2 + (-0.09268399911119718 + m.x12)**2)
    + m.x311 * ((-0.13324778009309624 + m.x9)**2 + (-0.7980330434465137 +
    m.x10)**2 + (-0.8193288420633215 + m.x11)**2 + (-0.6273035394858574 + m.x12)
    **2) + m.x312 * ((-0.6796346159434266 + m.x9)**2 + (-0.17745837578198675 +
    m.x10)**2 + (-0.724534591197156 + m.x11)**2 + (-0.35264486204409173 + m.x12)
    **2))

m.e1 = Constraint(expr= m.x13 + m.x113 + m.x213 == 1)
m.e2 = Constraint(expr= m.x14 + m.x114 + m.x214 == 1)
m.e3 = Constraint(expr= m.x15 + m.x115 + m.x215 == 1)
m.e4 = Constraint(expr= m.x16 + m.x116 + m.x216 == 1)
m.e5 = Constraint(expr= m.x17 + m.x117 + m.x217 == 1)
m.e6 = Constraint(expr= m.x18 + m.x118 + m.x218 == 1)
m.e7 = Constraint(expr= m.x19 + m.x119 + m.x219 == 1)
m.e8 = Constraint(expr= m.x20 + m.x120 + m.x220 == 1)
m.e9 = Constraint(expr= m.x21 + m.x121 + m.x221 == 1)
m.e10 = Constraint(expr= m.x22 + m.x122 + m.x222 == 1)
m.e11 = Constraint(expr= m.x23 + m.x123 + m.x223 == 1)
m.e12 = Constraint(expr= m.x24 + m.x124 + m.x224 == 1)
m.e13 = Constraint(expr= m.x25 + m.x125 + m.x225 == 1)
m.e14 = Constraint(expr= m.x26 + m.x126 + m.x226 == 1)
m.e15 = Constraint(expr= m.x27 + m.x127 + m.x227 == 1)
m.e16 = Constraint(expr= m.x28 + m.x128 + m.x228 == 1)
m.e17 = Constraint(expr= m.x29 + m.x129 + m.x229 == 1)
m.e18 = Constraint(expr= m.x30 + m.x130 + m.x230 == 1)
m.e19 = Constraint(expr= m.x31 + m.x131 + m.x231 == 1)
m.e20 = Constraint(expr= m.x32 + m.x132 + m.x232 == 1)
m.e21 = Constraint(expr= m.x33 + m.x133 + m.x233 == 1)
m.e22 = Constraint(expr= m.x34 + m.x134 + m.x234 == 1)
m.e23 = Constraint(expr= m.x35 + m.x135 + m.x235 == 1)
m.e24 = Constraint(expr= m.x36 + m.x136 + m.x236 == 1)
m.e25 = Constraint(expr= m.x37 + m.x137 + m.x237 == 1)
m.e26 = Constraint(expr= m.x38 + m.x138 + m.x238 == 1)
m.e27 = Constraint(expr= m.x39 + m.x139 + m.x239 == 1)
m.e28 = Constraint(expr= m.x40 + m.x140 + m.x240 == 1)
m.e29 = Constraint(expr= m.x41 + m.x141 + m.x241 == 1)
m.e30 = Constraint(expr= m.x42 + m.x142 + m.x242 == 1)
m.e31 = Constraint(expr= m.x43 + m.x143 + m.x243 == 1)
m.e32 = Constraint(expr= m.x44 + m.x144 + m.x244 == 1)
m.e33 = Constraint(expr= m.x45 + m.x145 + m.x245 == 1)
m.e34 = Constraint(expr= m.x46 + m.x146 + m.x246 == 1)
m.e35 = Constraint(expr= m.x47 + m.x147 + m.x247 == 1)
m.e36 = Constraint(expr= m.x48 + m.x148 + m.x248 == 1)
m.e37 = Constraint(expr= m.x49 + m.x149 + m.x249 == 1)
m.e38 = Constraint(expr= m.x50 + m.x150 + m.x250 == 1)
m.e39 = Constraint(expr= m.x51 + m.x151 + m.x251 == 1)
m.e40 = Constraint(expr= m.x52 + m.x152 + m.x252 == 1)
m.e41 = Constraint(expr= m.x53 + m.x153 + m.x253 == 1)
m.e42 = Constraint(expr= m.x54 + m.x154 + m.x254 == 1)
m.e43 = Constraint(expr= m.x55 + m.x155 + m.x255 == 1)
m.e44 = Constraint(expr= m.x56 + m.x156 + m.x256 == 1)
m.e45 = Constraint(expr= m.x57 + m.x157 + m.x257 == 1)
m.e46 = Constraint(expr= m.x58 + m.x158 + m.x258 == 1)
m.e47 = Constraint(expr= m.x59 + m.x159 + m.x259 == 1)
m.e48 = Constraint(expr= m.x60 + m.x160 + m.x260 == 1)
m.e49 = Constraint(expr= m.x61 + m.x161 + m.x261 == 1)
m.e50 = Constraint(expr= m.x62 + m.x162 + m.x262 == 1)
m.e51 = Constraint(expr= m.x63 + m.x163 + m.x263 == 1)
m.e52 = Constraint(expr= m.x64 + m.x164 + m.x264 == 1)
m.e53 = Constraint(expr= m.x65 + m.x165 + m.x265 == 1)
m.e54 = Constraint(expr= m.x66 + m.x166 + m.x266 == 1)
m.e55 = Constraint(expr= m.x67 + m.x167 + m.x267 == 1)
m.e56 = Constraint(expr= m.x68 + m.x168 + m.x268 == 1)
m.e57 = Constraint(expr= m.x69 + m.x169 + m.x269 == 1)
m.e58 = Constraint(expr= m.x70 + m.x170 + m.x270 == 1)
m.e59 = Constraint(expr= m.x71 + m.x171 + m.x271 == 1)
m.e60 = Constraint(expr= m.x72 + m.x172 + m.x272 == 1)
m.e61 = Constraint(expr= m.x73 + m.x173 + m.x273 == 1)
m.e62 = Constraint(expr= m.x74 + m.x174 + m.x274 == 1)
m.e63 = Constraint(expr= m.x75 + m.x175 + m.x275 == 1)
m.e64 = Constraint(expr= m.x76 + m.x176 + m.x276 == 1)
m.e65 = Constraint(expr= m.x77 + m.x177 + m.x277 == 1)
m.e66 = Constraint(expr= m.x78 + m.x178 + m.x278 == 1)
m.e67 = Constraint(expr= m.x79 + m.x179 + m.x279 == 1)
m.e68 = Constraint(expr= m.x80 + m.x180 + m.x280 == 1)
m.e69 = Constraint(expr= m.x81 + m.x181 + m.x281 == 1)
m.e70 = Constraint(expr= m.x82 + m.x182 + m.x282 == 1)
m.e71 = Constraint(expr= m.x83 + m.x183 + m.x283 == 1)
m.e72 = Constraint(expr= m.x84 + m.x184 + m.x284 == 1)
m.e73 = Constraint(expr= m.x85 + m.x185 + m.x285 == 1)
m.e74 = Constraint(expr= m.x86 + m.x186 + m.x286 == 1)
m.e75 = Constraint(expr= m.x87 + m.x187 + m.x287 == 1)
m.e76 = Constraint(expr= m.x88 + m.x188 + m.x288 == 1)
m.e77 = Constraint(expr= m.x89 + m.x189 + m.x289 == 1)
m.e78 = Constraint(expr= m.x90 + m.x190 + m.x290 == 1)
m.e79 = Constraint(expr= m.x91 + m.x191 + m.x291 == 1)
m.e80 = Constraint(expr= m.x92 + m.x192 + m.x292 == 1)
m.e81 = Constraint(expr= m.x93 + m.x193 + m.x293 == 1)
m.e82 = Constraint(expr= m.x94 + m.x194 + m.x294 == 1)
m.e83 = Constraint(expr= m.x95 + m.x195 + m.x295 == 1)
m.e84 = Constraint(expr= m.x96 + m.x196 + m.x296 == 1)
m.e85 = Constraint(expr= m.x97 + m.x197 + m.x297 == 1)
m.e86 = Constraint(expr= m.x98 + m.x198 + m.x298 == 1)
m.e87 = Constraint(expr= m.x99 + m.x199 + m.x299 == 1)
m.e88 = Constraint(expr= m.x100 + m.x200 + m.x300 == 1)
m.e89 = Constraint(expr= m.x101 + m.x201 + m.x301 == 1)
m.e90 = Constraint(expr= m.x102 + m.x202 + m.x302 == 1)
m.e91 = Constraint(expr= m.x103 + m.x203 + m.x303 == 1)
m.e92 = Constraint(expr= m.x104 + m.x204 + m.x304 == 1)
m.e93 = Constraint(expr= m.x105 + m.x205 + m.x305 == 1)
m.e94 = Constraint(expr= m.x106 + m.x206 + m.x306 == 1)
m.e95 = Constraint(expr= m.x107 + m.x207 + m.x307 == 1)
m.e96 = Constraint(expr= m.x108 + m.x208 + m.x308 == 1)
m.e97 = Constraint(expr= m.x109 + m.x209 + m.x309 == 1)
m.e98 = Constraint(expr= m.x110 + m.x210 + m.x310 == 1)
m.e99 = Constraint(expr= m.x111 + m.x211 + m.x311 == 1)
m.e100 = Constraint(expr= m.x112 + m.x212 + m.x312 == 1)
