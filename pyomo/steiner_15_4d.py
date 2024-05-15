# MINLP written by GAMS Convert at 05/15/24 11:59:18
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       313       40      273        0        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#       598      325      273        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#      2574     1170     1404
#
# Reformulation has removed 1 variable and 1 equation

from pyomo.environ import *

model = m = ConcreteModel()

m.x1 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x2 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x3 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x4 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x5 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x6 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x7 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x8 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x9 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x10 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x11 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x12 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x13 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x14 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x15 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x16 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x17 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x18 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x19 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x20 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x21 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x22 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x23 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x24 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x25 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x26 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x27 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x28 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x29 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x30 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x31 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x32 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x33 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x34 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x35 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x36 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x37 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x38 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x39 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x40 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x41 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x42 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x43 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x44 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x45 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x46 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x47 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x48 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x49 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x50 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x51 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x52 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x53 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x54 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x55 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x56 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x57 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x58 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x59 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x60 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x61 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x62 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x63 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x64 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x65 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x66 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x67 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x68 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x69 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x70 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x71 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x72 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x73 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x74 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x75 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x76 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x77 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x78 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x79 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x80 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x81 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x82 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x83 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x84 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x85 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x86 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x87 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x88 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x89 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x90 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x91 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x92 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x93 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x94 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x95 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x96 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x97 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x98 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x99 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x100 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x101 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x102 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x103 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x104 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x105 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x106 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x107 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x108 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x109 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x110 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x111 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x112 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x113 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x114 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x115 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x116 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x117 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x118 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x119 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x120 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x121 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x122 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x123 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x124 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x125 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x126 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x127 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x128 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x129 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x130 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x131 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x132 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x133 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x134 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x135 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x136 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x137 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x138 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x139 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x140 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x141 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x142 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x143 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x144 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x145 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x146 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x147 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x148 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x149 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x150 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x151 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x152 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x153 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x154 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x155 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x156 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x157 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x158 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x159 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x160 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x161 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x162 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x163 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x164 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x165 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x166 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x167 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x168 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x169 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x170 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x171 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x172 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x173 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x174 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x175 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x176 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x177 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x178 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x179 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x180 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x181 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x182 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x183 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x184 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x185 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x186 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x187 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x188 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x189 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x190 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x191 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x192 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x193 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x194 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x195 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x196 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x197 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x198 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x199 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x200 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x201 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x202 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x203 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x204 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x205 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x206 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x207 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x208 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x209 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x210 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x211 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x212 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x213 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x214 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x215 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x216 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x217 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x218 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x219 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x220 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x221 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x222 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x223 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x224 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x225 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x226 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x227 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x228 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x229 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x230 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x231 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x232 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x233 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x234 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x235 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x236 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x237 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x238 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x239 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x240 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x241 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x242 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x243 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x244 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x245 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x246 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x247 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x248 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x249 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x250 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x251 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x252 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x253 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x254 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x255 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x256 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x257 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x258 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x259 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x260 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x261 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x262 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x263 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x264 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x265 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x266 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x267 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x268 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x269 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x270 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x271 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x272 = Var(within=Reals, bounds=(0,2), initialize=0)
m.x273 = Var(within=Reals, bounds=(0,2), initialize=0)
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
m.b326 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b327 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b328 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b329 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b330 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b331 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b332 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b333 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b334 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b335 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b336 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b337 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b338 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b339 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b340 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b341 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b342 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b343 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b344 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b345 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b346 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b347 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b348 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b349 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b350 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b351 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b352 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b353 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b354 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b355 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b356 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b357 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b358 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b359 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b360 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b361 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b362 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b363 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b364 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b365 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b366 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b367 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b368 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b369 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b370 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b371 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b372 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b373 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b374 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b375 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b376 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b377 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b378 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b379 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b380 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b381 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b382 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b383 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b384 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b385 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b386 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b387 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b388 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b389 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b390 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b391 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b392 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b393 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b394 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b395 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b396 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b397 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b398 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b399 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b400 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b401 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b402 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b403 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b404 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b405 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b406 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b407 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b408 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b409 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b410 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b411 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b412 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b413 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b414 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b415 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b416 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b417 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b418 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b419 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b420 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b421 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b422 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b423 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b424 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b425 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b426 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b427 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b428 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b429 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b430 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b431 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b432 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b433 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b434 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b435 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b436 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b437 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b438 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b439 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b440 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b441 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b442 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b443 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b444 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b445 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b446 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b447 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b448 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b449 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b450 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b451 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b452 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b453 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b454 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b455 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b456 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b457 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b458 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b459 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b460 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b461 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b462 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b463 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b464 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b465 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b466 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b467 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b468 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b469 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b470 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b471 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b472 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b473 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b474 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b475 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b476 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b477 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b478 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b479 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b480 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b481 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b482 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b483 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b484 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b485 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b486 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b487 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b488 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b489 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b490 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b491 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b492 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b493 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b494 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b495 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b496 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b497 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b498 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b499 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b500 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b501 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b502 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b503 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b504 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b505 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b506 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b507 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b508 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b509 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b510 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b511 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b512 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b513 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b514 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b515 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b516 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b517 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b518 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b519 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b520 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b521 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b522 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b523 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b524 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b525 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b526 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b527 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b528 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b529 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b530 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b531 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b532 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b533 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b534 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b535 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b536 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b537 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b538 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b539 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b540 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b541 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b542 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b543 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b544 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b545 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b546 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b547 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b548 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b549 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b550 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b551 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b552 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b553 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b554 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b555 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b556 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b557 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b558 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b559 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b560 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b561 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b562 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b563 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b564 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b565 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b566 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b567 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b568 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b569 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b570 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b571 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b572 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b573 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b574 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b575 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b576 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b577 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b578 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b579 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b580 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b581 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b582 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b583 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b584 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b585 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b586 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b587 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b588 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b589 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b590 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b591 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b592 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b593 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b594 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b595 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b596 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b597 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b598 = Var(within=Binary, bounds=(0,1), initialize=0)

m.obj = Objective(sense=minimize, expr= m.x1 + m.x2 + m.x3 + m.x4 + m.x5 + m.x6
    + m.x7 + m.x8 + m.x9 + m.x10 + m.x11 + m.x12 + m.x13 + m.x14 + m.x15 +
    m.x16 + m.x17 + m.x18 + m.x19 + m.x20 + m.x21 + m.x22 + m.x23 + m.x24 +
    m.x25 + m.x26 + m.x27 + m.x28 + m.x29 + m.x30 + m.x31 + m.x32 + m.x33 +
    m.x34 + m.x35 + m.x36 + m.x37 + m.x38 + m.x39 + m.x40 + m.x41 + m.x42 +
    m.x43 + m.x44 + m.x45 + m.x46 + m.x47 + m.x48 + m.x49 + m.x50 + m.x51 +
    m.x52 + m.x53 + m.x54 + m.x55 + m.x56 + m.x57 + m.x58 + m.x59 + m.x60 +
    m.x61 + m.x62 + m.x63 + m.x64 + m.x65 + m.x66 + m.x67 + m.x68 + m.x69 +
    m.x70 + m.x71 + m.x72 + m.x73 + m.x74 + m.x75 + m.x76 + m.x77 + m.x78 +
    m.x79 + m.x80 + m.x81 + m.x82 + m.x83 + m.x84 + m.x85 + m.x86 + m.x87 +
    m.x88 + m.x89 + m.x90 + m.x91 + m.x92 + m.x93 + m.x94 + m.x95 + m.x96 +
    m.x97 + m.x98 + m.x99 + m.x100 + m.x101 + m.x102 + m.x103 + m.x104 + m.x105
    + m.x106 + m.x107 + m.x108 + m.x109 + m.x110 + m.x111 + m.x112 + m.x113 +
    m.x114 + m.x115 + m.x116 + m.x117 + m.x118 + m.x119 + m.x120 + m.x121 +
    m.x122 + m.x123 + m.x124 + m.x125 + m.x126 + m.x127 + m.x128 + m.x129 +
    m.x130 + m.x131 + m.x132 + m.x133 + m.x134 + m.x135 + m.x136 + m.x137 +
    m.x138 + m.x139 + m.x140 + m.x141 + m.x142 + m.x143 + m.x144 + m.x145 +
    m.x146 + m.x147 + m.x148 + m.x149 + m.x150 + m.x151 + m.x152 + m.x153 +
    m.x154 + m.x155 + m.x156 + m.x157 + m.x158 + m.x159 + m.x160 + m.x161 +
    m.x162 + m.x163 + m.x164 + m.x165 + m.x166 + m.x167 + m.x168 + m.x169 +
    m.x170 + m.x171 + m.x172 + m.x173 + m.x174 + m.x175 + m.x176 + m.x177 +
    m.x178 + m.x179 + m.x180 + m.x181 + m.x182 + m.x183 + m.x184 + m.x185 +
    m.x186 + m.x187 + m.x188 + m.x189 + m.x190 + m.x191 + m.x192 + m.x193 +
    m.x194 + m.x195 + m.x196 + m.x197 + m.x198 + m.x199 + m.x200 + m.x201 +
    m.x202 + m.x203 + m.x204 + m.x205 + m.x206 + m.x207 + m.x208 + m.x209 +
    m.x210 + m.x211 + m.x212 + m.x213 + m.x214 + m.x215 + m.x216 + m.x217 +
    m.x218 + m.x219 + m.x220 + m.x221 + m.x222 + m.x223 + m.x224 + m.x225 +
    m.x226 + m.x227 + m.x228 + m.x229 + m.x230 + m.x231 + m.x232 + m.x233 +
    m.x234 + m.x235 + m.x236 + m.x237 + m.x238 + m.x239 + m.x240 + m.x241 +
    m.x242 + m.x243 + m.x244 + m.x245 + m.x246 + m.x247 + m.x248 + m.x249 +
    m.x250 + m.x251 + m.x252 + m.x253 + m.x254 + m.x255 + m.x256 + m.x257 +
    m.x258 + m.x259 + m.x260 + m.x261 + m.x262 + m.x263 + m.x264 + m.x265 +
    m.x266 + m.x267 + m.x268 + m.x269 + m.x270 + m.x271 + m.x272 + m.x273)

m.e1 = Constraint(expr= -sqrt((m.x274 - m.x278)**2 + (m.x275 - m.x279)**2 + (
    m.x276 - m.x280)**2 + (m.x277 - m.x281)**2) + m.x1 - 2 * m.b326 >= -2)
m.e2 = Constraint(expr= -sqrt((m.x274 - m.x282)**2 + (m.x275 - m.x283)**2 + (
    m.x276 - m.x284)**2 + (m.x277 - m.x285)**2) + m.x2 - 2 * m.b327 >= -2)
m.e3 = Constraint(expr= -sqrt((m.x274 - m.x286)**2 + (m.x275 - m.x287)**2 + (
    m.x276 - m.x288)**2 + (m.x277 - m.x289)**2) + m.x3 - 2 * m.b328 >= -2)
m.e4 = Constraint(expr= -sqrt((m.x274 - m.x290)**2 + (m.x275 - m.x291)**2 + (
    m.x276 - m.x292)**2 + (m.x277 - m.x293)**2) + m.x4 - 2 * m.b329 >= -2)
m.e5 = Constraint(expr= -sqrt((m.x274 - m.x294)**2 + (m.x275 - m.x295)**2 + (
    m.x276 - m.x296)**2 + (m.x277 - m.x297)**2) + m.x5 - 2 * m.b330 >= -2)
m.e6 = Constraint(expr= -sqrt((m.x274 - m.x298)**2 + (m.x275 - m.x299)**2 + (
    m.x276 - m.x300)**2 + (m.x277 - m.x301)**2) + m.x6 - 2 * m.b331 >= -2)
m.e7 = Constraint(expr= -sqrt((m.x274 - m.x302)**2 + (m.x275 - m.x303)**2 + (
    m.x276 - m.x304)**2 + (m.x277 - m.x305)**2) + m.x7 - 2 * m.b332 >= -2)
m.e8 = Constraint(expr= -sqrt((m.x274 - m.x306)**2 + (m.x275 - m.x307)**2 + (
    m.x276 - m.x308)**2 + (m.x277 - m.x309)**2) + m.x8 - 2 * m.b333 >= -2)
m.e9 = Constraint(expr= -sqrt((m.x274 - m.x310)**2 + (m.x275 - m.x311)**2 + (
    m.x276 - m.x312)**2 + (m.x277 - m.x313)**2) + m.x9 - 2 * m.b334 >= -2)
m.e10 = Constraint(expr= -sqrt((m.x274 - m.x314)**2 + (m.x275 - m.x315)**2 + (
    m.x276 - m.x316)**2 + (m.x277 - m.x317)**2) + m.x10 - 2 * m.b335 >= -2)
m.e11 = Constraint(expr= -sqrt((m.x274 - m.x318)**2 + (m.x275 - m.x319)**2 + (
    m.x276 - m.x320)**2 + (m.x277 - m.x321)**2) + m.x11 - 2 * m.b336 >= -2)
m.e12 = Constraint(expr= -sqrt((m.x274 - m.x322)**2 + (m.x275 - m.x323)**2 + (
    m.x276 - m.x324)**2 + (m.x277 - m.x325)**2) + m.x12 - 2 * m.b337 >= -2)
m.e13 = Constraint(expr= -sqrt((m.x278 - m.x282)**2 + (m.x279 - m.x283)**2 + (
    m.x280 - m.x284)**2 + (m.x281 - m.x285)**2) + m.x13 - 2 * m.b338 >= -2)
m.e14 = Constraint(expr= -sqrt((m.x278 - m.x286)**2 + (m.x279 - m.x287)**2 + (
    m.x280 - m.x288)**2 + (m.x281 - m.x289)**2) + m.x14 - 2 * m.b339 >= -2)
m.e15 = Constraint(expr= -sqrt((m.x278 - m.x290)**2 + (m.x279 - m.x291)**2 + (
    m.x280 - m.x292)**2 + (m.x281 - m.x293)**2) + m.x15 - 2 * m.b340 >= -2)
m.e16 = Constraint(expr= -sqrt((m.x278 - m.x294)**2 + (m.x279 - m.x295)**2 + (
    m.x280 - m.x296)**2 + (m.x281 - m.x297)**2) + m.x16 - 2 * m.b341 >= -2)
m.e17 = Constraint(expr= -sqrt((m.x278 - m.x298)**2 + (m.x279 - m.x299)**2 + (
    m.x280 - m.x300)**2 + (m.x281 - m.x301)**2) + m.x17 - 2 * m.b342 >= -2)
m.e18 = Constraint(expr= -sqrt((m.x278 - m.x302)**2 + (m.x279 - m.x303)**2 + (
    m.x280 - m.x304)**2 + (m.x281 - m.x305)**2) + m.x18 - 2 * m.b343 >= -2)
m.e19 = Constraint(expr= -sqrt((m.x278 - m.x306)**2 + (m.x279 - m.x307)**2 + (
    m.x280 - m.x308)**2 + (m.x281 - m.x309)**2) + m.x19 - 2 * m.b344 >= -2)
m.e20 = Constraint(expr= -sqrt((m.x278 - m.x310)**2 + (m.x279 - m.x311)**2 + (
    m.x280 - m.x312)**2 + (m.x281 - m.x313)**2) + m.x20 - 2 * m.b345 >= -2)
m.e21 = Constraint(expr= -sqrt((m.x278 - m.x314)**2 + (m.x279 - m.x315)**2 + (
    m.x280 - m.x316)**2 + (m.x281 - m.x317)**2) + m.x21 - 2 * m.b346 >= -2)
m.e22 = Constraint(expr= -sqrt((m.x278 - m.x318)**2 + (m.x279 - m.x319)**2 + (
    m.x280 - m.x320)**2 + (m.x281 - m.x321)**2) + m.x22 - 2 * m.b347 >= -2)
m.e23 = Constraint(expr= -sqrt((m.x278 - m.x322)**2 + (m.x279 - m.x323)**2 + (
    m.x280 - m.x324)**2 + (m.x281 - m.x325)**2) + m.x23 - 2 * m.b348 >= -2)
m.e24 = Constraint(expr= -sqrt((m.x282 - m.x286)**2 + (m.x283 - m.x287)**2 + (
    m.x284 - m.x288)**2 + (m.x285 - m.x289)**2) + m.x24 - 2 * m.b349 >= -2)
m.e25 = Constraint(expr= -sqrt((m.x282 - m.x290)**2 + (m.x283 - m.x291)**2 + (
    m.x284 - m.x292)**2 + (m.x285 - m.x293)**2) + m.x25 - 2 * m.b350 >= -2)
m.e26 = Constraint(expr= -sqrt((m.x282 - m.x294)**2 + (m.x283 - m.x295)**2 + (
    m.x284 - m.x296)**2 + (m.x285 - m.x297)**2) + m.x26 - 2 * m.b351 >= -2)
m.e27 = Constraint(expr= -sqrt((m.x282 - m.x298)**2 + (m.x283 - m.x299)**2 + (
    m.x284 - m.x300)**2 + (m.x285 - m.x301)**2) + m.x27 - 2 * m.b352 >= -2)
m.e28 = Constraint(expr= -sqrt((m.x282 - m.x302)**2 + (m.x283 - m.x303)**2 + (
    m.x284 - m.x304)**2 + (m.x285 - m.x305)**2) + m.x28 - 2 * m.b353 >= -2)
m.e29 = Constraint(expr= -sqrt((m.x282 - m.x306)**2 + (m.x283 - m.x307)**2 + (
    m.x284 - m.x308)**2 + (m.x285 - m.x309)**2) + m.x29 - 2 * m.b354 >= -2)
m.e30 = Constraint(expr= -sqrt((m.x282 - m.x310)**2 + (m.x283 - m.x311)**2 + (
    m.x284 - m.x312)**2 + (m.x285 - m.x313)**2) + m.x30 - 2 * m.b355 >= -2)
m.e31 = Constraint(expr= -sqrt((m.x282 - m.x314)**2 + (m.x283 - m.x315)**2 + (
    m.x284 - m.x316)**2 + (m.x285 - m.x317)**2) + m.x31 - 2 * m.b356 >= -2)
m.e32 = Constraint(expr= -sqrt((m.x282 - m.x318)**2 + (m.x283 - m.x319)**2 + (
    m.x284 - m.x320)**2 + (m.x285 - m.x321)**2) + m.x32 - 2 * m.b357 >= -2)
m.e33 = Constraint(expr= -sqrt((m.x282 - m.x322)**2 + (m.x283 - m.x323)**2 + (
    m.x284 - m.x324)**2 + (m.x285 - m.x325)**2) + m.x33 - 2 * m.b358 >= -2)
m.e34 = Constraint(expr= -sqrt((m.x286 - m.x290)**2 + (m.x287 - m.x291)**2 + (
    m.x288 - m.x292)**2 + (m.x289 - m.x293)**2) + m.x34 - 2 * m.b359 >= -2)
m.e35 = Constraint(expr= -sqrt((m.x286 - m.x294)**2 + (m.x287 - m.x295)**2 + (
    m.x288 - m.x296)**2 + (m.x289 - m.x297)**2) + m.x35 - 2 * m.b360 >= -2)
m.e36 = Constraint(expr= -sqrt((m.x286 - m.x298)**2 + (m.x287 - m.x299)**2 + (
    m.x288 - m.x300)**2 + (m.x289 - m.x301)**2) + m.x36 - 2 * m.b361 >= -2)
m.e37 = Constraint(expr= -sqrt((m.x286 - m.x302)**2 + (m.x287 - m.x303)**2 + (
    m.x288 - m.x304)**2 + (m.x289 - m.x305)**2) + m.x37 - 2 * m.b362 >= -2)
m.e38 = Constraint(expr= -sqrt((m.x286 - m.x306)**2 + (m.x287 - m.x307)**2 + (
    m.x288 - m.x308)**2 + (m.x289 - m.x309)**2) + m.x38 - 2 * m.b363 >= -2)
m.e39 = Constraint(expr= -sqrt((m.x286 - m.x310)**2 + (m.x287 - m.x311)**2 + (
    m.x288 - m.x312)**2 + (m.x289 - m.x313)**2) + m.x39 - 2 * m.b364 >= -2)
m.e40 = Constraint(expr= -sqrt((m.x286 - m.x314)**2 + (m.x287 - m.x315)**2 + (
    m.x288 - m.x316)**2 + (m.x289 - m.x317)**2) + m.x40 - 2 * m.b365 >= -2)
m.e41 = Constraint(expr= -sqrt((m.x286 - m.x318)**2 + (m.x287 - m.x319)**2 + (
    m.x288 - m.x320)**2 + (m.x289 - m.x321)**2) + m.x41 - 2 * m.b366 >= -2)
m.e42 = Constraint(expr= -sqrt((m.x286 - m.x322)**2 + (m.x287 - m.x323)**2 + (
    m.x288 - m.x324)**2 + (m.x289 - m.x325)**2) + m.x42 - 2 * m.b367 >= -2)
m.e43 = Constraint(expr= -sqrt((m.x290 - m.x294)**2 + (m.x291 - m.x295)**2 + (
    m.x292 - m.x296)**2 + (m.x293 - m.x297)**2) + m.x43 - 2 * m.b368 >= -2)
m.e44 = Constraint(expr= -sqrt((m.x290 - m.x298)**2 + (m.x291 - m.x299)**2 + (
    m.x292 - m.x300)**2 + (m.x293 - m.x301)**2) + m.x44 - 2 * m.b369 >= -2)
m.e45 = Constraint(expr= -sqrt((m.x290 - m.x302)**2 + (m.x291 - m.x303)**2 + (
    m.x292 - m.x304)**2 + (m.x293 - m.x305)**2) + m.x45 - 2 * m.b370 >= -2)
m.e46 = Constraint(expr= -sqrt((m.x290 - m.x306)**2 + (m.x291 - m.x307)**2 + (
    m.x292 - m.x308)**2 + (m.x293 - m.x309)**2) + m.x46 - 2 * m.b371 >= -2)
m.e47 = Constraint(expr= -sqrt((m.x290 - m.x310)**2 + (m.x291 - m.x311)**2 + (
    m.x292 - m.x312)**2 + (m.x293 - m.x313)**2) + m.x47 - 2 * m.b372 >= -2)
m.e48 = Constraint(expr= -sqrt((m.x290 - m.x314)**2 + (m.x291 - m.x315)**2 + (
    m.x292 - m.x316)**2 + (m.x293 - m.x317)**2) + m.x48 - 2 * m.b373 >= -2)
m.e49 = Constraint(expr= -sqrt((m.x290 - m.x318)**2 + (m.x291 - m.x319)**2 + (
    m.x292 - m.x320)**2 + (m.x293 - m.x321)**2) + m.x49 - 2 * m.b374 >= -2)
m.e50 = Constraint(expr= -sqrt((m.x290 - m.x322)**2 + (m.x291 - m.x323)**2 + (
    m.x292 - m.x324)**2 + (m.x293 - m.x325)**2) + m.x50 - 2 * m.b375 >= -2)
m.e51 = Constraint(expr= -sqrt((m.x294 - m.x298)**2 + (m.x295 - m.x299)**2 + (
    m.x296 - m.x300)**2 + (m.x297 - m.x301)**2) + m.x51 - 2 * m.b376 >= -2)
m.e52 = Constraint(expr= -sqrt((m.x294 - m.x302)**2 + (m.x295 - m.x303)**2 + (
    m.x296 - m.x304)**2 + (m.x297 - m.x305)**2) + m.x52 - 2 * m.b377 >= -2)
m.e53 = Constraint(expr= -sqrt((m.x294 - m.x306)**2 + (m.x295 - m.x307)**2 + (
    m.x296 - m.x308)**2 + (m.x297 - m.x309)**2) + m.x53 - 2 * m.b378 >= -2)
m.e54 = Constraint(expr= -sqrt((m.x294 - m.x310)**2 + (m.x295 - m.x311)**2 + (
    m.x296 - m.x312)**2 + (m.x297 - m.x313)**2) + m.x54 - 2 * m.b379 >= -2)
m.e55 = Constraint(expr= -sqrt((m.x294 - m.x314)**2 + (m.x295 - m.x315)**2 + (
    m.x296 - m.x316)**2 + (m.x297 - m.x317)**2) + m.x55 - 2 * m.b380 >= -2)
m.e56 = Constraint(expr= -sqrt((m.x294 - m.x318)**2 + (m.x295 - m.x319)**2 + (
    m.x296 - m.x320)**2 + (m.x297 - m.x321)**2) + m.x56 - 2 * m.b381 >= -2)
m.e57 = Constraint(expr= -sqrt((m.x294 - m.x322)**2 + (m.x295 - m.x323)**2 + (
    m.x296 - m.x324)**2 + (m.x297 - m.x325)**2) + m.x57 - 2 * m.b382 >= -2)
m.e58 = Constraint(expr= -sqrt((m.x298 - m.x302)**2 + (m.x299 - m.x303)**2 + (
    m.x300 - m.x304)**2 + (m.x301 - m.x305)**2) + m.x58 - 2 * m.b383 >= -2)
m.e59 = Constraint(expr= -sqrt((m.x298 - m.x306)**2 + (m.x299 - m.x307)**2 + (
    m.x300 - m.x308)**2 + (m.x301 - m.x309)**2) + m.x59 - 2 * m.b384 >= -2)
m.e60 = Constraint(expr= -sqrt((m.x298 - m.x310)**2 + (m.x299 - m.x311)**2 + (
    m.x300 - m.x312)**2 + (m.x301 - m.x313)**2) + m.x60 - 2 * m.b385 >= -2)
m.e61 = Constraint(expr= -sqrt((m.x298 - m.x314)**2 + (m.x299 - m.x315)**2 + (
    m.x300 - m.x316)**2 + (m.x301 - m.x317)**2) + m.x61 - 2 * m.b386 >= -2)
m.e62 = Constraint(expr= -sqrt((m.x298 - m.x318)**2 + (m.x299 - m.x319)**2 + (
    m.x300 - m.x320)**2 + (m.x301 - m.x321)**2) + m.x62 - 2 * m.b387 >= -2)
m.e63 = Constraint(expr= -sqrt((m.x298 - m.x322)**2 + (m.x299 - m.x323)**2 + (
    m.x300 - m.x324)**2 + (m.x301 - m.x325)**2) + m.x63 - 2 * m.b388 >= -2)
m.e64 = Constraint(expr= -sqrt((m.x302 - m.x306)**2 + (m.x303 - m.x307)**2 + (
    m.x304 - m.x308)**2 + (m.x305 - m.x309)**2) + m.x64 - 2 * m.b389 >= -2)
m.e65 = Constraint(expr= -sqrt((m.x302 - m.x310)**2 + (m.x303 - m.x311)**2 + (
    m.x304 - m.x312)**2 + (m.x305 - m.x313)**2) + m.x65 - 2 * m.b390 >= -2)
m.e66 = Constraint(expr= -sqrt((m.x302 - m.x314)**2 + (m.x303 - m.x315)**2 + (
    m.x304 - m.x316)**2 + (m.x305 - m.x317)**2) + m.x66 - 2 * m.b391 >= -2)
m.e67 = Constraint(expr= -sqrt((m.x302 - m.x318)**2 + (m.x303 - m.x319)**2 + (
    m.x304 - m.x320)**2 + (m.x305 - m.x321)**2) + m.x67 - 2 * m.b392 >= -2)
m.e68 = Constraint(expr= -sqrt((m.x302 - m.x322)**2 + (m.x303 - m.x323)**2 + (
    m.x304 - m.x324)**2 + (m.x305 - m.x325)**2) + m.x68 - 2 * m.b393 >= -2)
m.e69 = Constraint(expr= -sqrt((m.x306 - m.x310)**2 + (m.x307 - m.x311)**2 + (
    m.x308 - m.x312)**2 + (m.x309 - m.x313)**2) + m.x69 - 2 * m.b394 >= -2)
m.e70 = Constraint(expr= -sqrt((m.x306 - m.x314)**2 + (m.x307 - m.x315)**2 + (
    m.x308 - m.x316)**2 + (m.x309 - m.x317)**2) + m.x70 - 2 * m.b395 >= -2)
m.e71 = Constraint(expr= -sqrt((m.x306 - m.x318)**2 + (m.x307 - m.x319)**2 + (
    m.x308 - m.x320)**2 + (m.x309 - m.x321)**2) + m.x71 - 2 * m.b396 >= -2)
m.e72 = Constraint(expr= -sqrt((m.x306 - m.x322)**2 + (m.x307 - m.x323)**2 + (
    m.x308 - m.x324)**2 + (m.x309 - m.x325)**2) + m.x72 - 2 * m.b397 >= -2)
m.e73 = Constraint(expr= -sqrt((m.x310 - m.x314)**2 + (m.x311 - m.x315)**2 + (
    m.x312 - m.x316)**2 + (m.x313 - m.x317)**2) + m.x73 - 2 * m.b398 >= -2)
m.e74 = Constraint(expr= -sqrt((m.x310 - m.x318)**2 + (m.x311 - m.x319)**2 + (
    m.x312 - m.x320)**2 + (m.x313 - m.x321)**2) + m.x74 - 2 * m.b399 >= -2)
m.e75 = Constraint(expr= -sqrt((m.x310 - m.x322)**2 + (m.x311 - m.x323)**2 + (
    m.x312 - m.x324)**2 + (m.x313 - m.x325)**2) + m.x75 - 2 * m.b400 >= -2)
m.e76 = Constraint(expr= -sqrt((m.x314 - m.x318)**2 + (m.x315 - m.x319)**2 + (
    m.x316 - m.x320)**2 + (m.x317 - m.x321)**2) + m.x76 - 2 * m.b401 >= -2)
m.e77 = Constraint(expr= -sqrt((m.x314 - m.x322)**2 + (m.x315 - m.x323)**2 + (
    m.x316 - m.x324)**2 + (m.x317 - m.x325)**2) + m.x77 - 2 * m.b402 >= -2)
m.e78 = Constraint(expr= -sqrt((m.x318 - m.x322)**2 + (m.x319 - m.x323)**2 + (
    m.x320 - m.x324)**2 + (m.x321 - m.x325)**2) + m.x78 - 2 * m.b403 >= -2)
m.e79 = Constraint(expr= -sqrt((-0.3078067547337774 + m.x274)**2 + (
    -0.5779578771750392 + m.x275)**2 + (-0.26561803541817575 + m.x276)**2 + (
    -0.8078960514329893 + m.x277)**2) + m.x79 - 2 * m.b404 >= -2)
m.e80 = Constraint(expr= -sqrt((-0.4672172210012604 + m.x274)**2 + (
    -0.33251980673741144 + m.x275)**2 + (-0.8967525962082569 + m.x276)**2 + (
    -0.7924119898695275 + m.x277)**2) + m.x80 - 2 * m.b405 >= -2)
m.e81 = Constraint(expr= -sqrt((-0.8596136949374525 + m.x274)**2 + (
    -0.6658137355569159 + m.x275)**2 + (-0.1854598161134392 + m.x276)**2 + (
    -0.3899285200718041 + m.x277)**2) + m.x81 - 2 * m.b406 >= -2)
m.e82 = Constraint(expr= -sqrt((-0.23942936687819738 + m.x274)**2 + (
    -0.7931287877223899 + m.x275)**2 + (-0.009184110257544176 + m.x276)**2 + (
    -0.7905476817951573 + m.x277)**2) + m.x82 - 2 * m.b407 >= -2)
m.e83 = Constraint(expr= -sqrt((-0.1667763675050825 + m.x274)**2 + (
    -0.30614199209589266 + m.x275)**2 + (-0.6286784916754126 + m.x276)**2 + (
    -0.6749145697726233 + m.x277)**2) + m.x83 - 2 * m.b408 >= -2)
m.e84 = Constraint(expr= -sqrt((-0.5123965188595846 + m.x274)**2 + (
    -0.556215195448374 + m.x275)**2 + (-0.5888863209509851 + m.x276)**2 + (
    -0.6003058073162648 + m.x277)**2) + m.x84 - 2 * m.b409 >= -2)
m.e85 = Constraint(expr= -sqrt((-0.10830095398871686 + m.x274)**2 + (
    -0.301870958131248 + m.x275)**2 + (-0.020499027923741364 + m.x276)**2 + (
    -0.5668022276384451 + m.x277)**2) + m.x85 - 2 * m.b410 >= -2)
m.e86 = Constraint(expr= -sqrt((-0.29450295704025886 + m.x274)**2 + (
    -0.24215631594412912 + m.x275)**2 + (-0.2744568069724159 + m.x276)**2 + (
    -0.9412593709117075 + m.x277)**2) + m.x86 - 2 * m.b411 >= -2)
m.e87 = Constraint(expr= -sqrt((-0.1282338254681593 + m.x274)**2 + (
    -0.9019460548181631 + m.x275)**2 + (-0.9031736614711603 + m.x276)**2 + (
    -0.2037984038273466 + m.x277)**2) + m.x87 - 2 * m.b412 >= -2)
m.e88 = Constraint(expr= -sqrt((-0.829797266931312 + m.x274)**2 + (
    -0.19575994148177733 + m.x275)**2 + (-0.645872503285497 + m.x276)**2 + (
    -0.12203855440196454 + m.x277)**2) + m.x88 - 2 * m.b413 >= -2)
m.e89 = Constraint(expr= -sqrt((-0.318405760895906 + m.x274)**2 + (
    -0.4938036901276964 + m.x275)**2 + (-0.37642068481077395 + m.x276)**2 + (
    -0.8256324717799948 + m.x277)**2) + m.x89 - 2 * m.b414 >= -2)
m.e90 = Constraint(expr= -sqrt((-0.6465433247102469 + m.x274)**2 + (
    -0.033522650784374886 + m.x275)**2 + (-0.5581254938339517 + m.x276)**2 + (
    -0.0912916889874551 + m.x277)**2) + m.x90 - 2 * m.b415 >= -2)
m.e91 = Constraint(expr= -sqrt((-0.17497888842654896 + m.x274)**2 + (
    -0.38968471952782524 + m.x275)**2 + (-0.3152812984667659 + m.x276)**2 + (
    -0.5561379670293034 + m.x277)**2) + m.x91 - 2 * m.b416 >= -2)
m.e92 = Constraint(expr= -sqrt((-0.9831483568003972 + m.x274)**2 + (
    -0.7793186335882816 + m.x275)**2 + (-0.545443726285844 + m.x276)**2 + (
    -0.8394599012498352 + m.x277)**2) + m.x92 - 2 * m.b417 >= -2)
m.e93 = Constraint(expr= -sqrt((-0.16871130717858907 + m.x274)**2 + (
    -0.7158922205435296 + m.x275)**2 + (-0.9716203470560987 + m.x276)**2 + (
    -0.9419601863446189 + m.x277)**2) + m.x93 - 2 * m.b418 >= -2)
m.e94 = Constraint(expr= -sqrt((-0.3078067547337774 + m.x278)**2 + (
    -0.5779578771750392 + m.x279)**2 + (-0.26561803541817575 + m.x280)**2 + (
    -0.8078960514329893 + m.x281)**2) + m.x94 - 2 * m.b419 >= -2)
m.e95 = Constraint(expr= -sqrt((-0.4672172210012604 + m.x278)**2 + (
    -0.33251980673741144 + m.x279)**2 + (-0.8967525962082569 + m.x280)**2 + (
    -0.7924119898695275 + m.x281)**2) + m.x95 - 2 * m.b420 >= -2)
m.e96 = Constraint(expr= -sqrt((-0.8596136949374525 + m.x278)**2 + (
    -0.6658137355569159 + m.x279)**2 + (-0.1854598161134392 + m.x280)**2 + (
    -0.3899285200718041 + m.x281)**2) + m.x96 - 2 * m.b421 >= -2)
m.e97 = Constraint(expr= -sqrt((-0.23942936687819738 + m.x278)**2 + (
    -0.7931287877223899 + m.x279)**2 + (-0.009184110257544176 + m.x280)**2 + (
    -0.7905476817951573 + m.x281)**2) + m.x97 - 2 * m.b422 >= -2)
m.e98 = Constraint(expr= -sqrt((-0.1667763675050825 + m.x278)**2 + (
    -0.30614199209589266 + m.x279)**2 + (-0.6286784916754126 + m.x280)**2 + (
    -0.6749145697726233 + m.x281)**2) + m.x98 - 2 * m.b423 >= -2)
m.e99 = Constraint(expr= -sqrt((-0.5123965188595846 + m.x278)**2 + (
    -0.556215195448374 + m.x279)**2 + (-0.5888863209509851 + m.x280)**2 + (
    -0.6003058073162648 + m.x281)**2) + m.x99 - 2 * m.b424 >= -2)
m.e100 = Constraint(expr= -sqrt((-0.10830095398871686 + m.x278)**2 + (
    -0.301870958131248 + m.x279)**2 + (-0.020499027923741364 + m.x280)**2 + (
    -0.5668022276384451 + m.x281)**2) + m.x100 - 2 * m.b425 >= -2)
m.e101 = Constraint(expr= -sqrt((-0.29450295704025886 + m.x278)**2 + (
    -0.24215631594412912 + m.x279)**2 + (-0.2744568069724159 + m.x280)**2 + (
    -0.9412593709117075 + m.x281)**2) + m.x101 - 2 * m.b426 >= -2)
m.e102 = Constraint(expr= -sqrt((-0.1282338254681593 + m.x278)**2 + (
    -0.9019460548181631 + m.x279)**2 + (-0.9031736614711603 + m.x280)**2 + (
    -0.2037984038273466 + m.x281)**2) + m.x102 - 2 * m.b427 >= -2)
m.e103 = Constraint(expr= -sqrt((-0.829797266931312 + m.x278)**2 + (
    -0.19575994148177733 + m.x279)**2 + (-0.645872503285497 + m.x280)**2 + (
    -0.12203855440196454 + m.x281)**2) + m.x103 - 2 * m.b428 >= -2)
m.e104 = Constraint(expr= -sqrt((-0.318405760895906 + m.x278)**2 + (
    -0.4938036901276964 + m.x279)**2 + (-0.37642068481077395 + m.x280)**2 + (
    -0.8256324717799948 + m.x281)**2) + m.x104 - 2 * m.b429 >= -2)
m.e105 = Constraint(expr= -sqrt((-0.6465433247102469 + m.x278)**2 + (
    -0.033522650784374886 + m.x279)**2 + (-0.5581254938339517 + m.x280)**2 + (
    -0.0912916889874551 + m.x281)**2) + m.x105 - 2 * m.b430 >= -2)
m.e106 = Constraint(expr= -sqrt((-0.17497888842654896 + m.x278)**2 + (
    -0.38968471952782524 + m.x279)**2 + (-0.3152812984667659 + m.x280)**2 + (
    -0.5561379670293034 + m.x281)**2) + m.x106 - 2 * m.b431 >= -2)
m.e107 = Constraint(expr= -sqrt((-0.9831483568003972 + m.x278)**2 + (
    -0.7793186335882816 + m.x279)**2 + (-0.545443726285844 + m.x280)**2 + (
    -0.8394599012498352 + m.x281)**2) + m.x107 - 2 * m.b432 >= -2)
m.e108 = Constraint(expr= -sqrt((-0.16871130717858907 + m.x278)**2 + (
    -0.7158922205435296 + m.x279)**2 + (-0.9716203470560987 + m.x280)**2 + (
    -0.9419601863446189 + m.x281)**2) + m.x108 - 2 * m.b433 >= -2)
m.e109 = Constraint(expr= -sqrt((-0.3078067547337774 + m.x282)**2 + (
    -0.5779578771750392 + m.x283)**2 + (-0.26561803541817575 + m.x284)**2 + (
    -0.8078960514329893 + m.x285)**2) + m.x109 - 2 * m.b434 >= -2)
m.e110 = Constraint(expr= -sqrt((-0.4672172210012604 + m.x282)**2 + (
    -0.33251980673741144 + m.x283)**2 + (-0.8967525962082569 + m.x284)**2 + (
    -0.7924119898695275 + m.x285)**2) + m.x110 - 2 * m.b435 >= -2)
m.e111 = Constraint(expr= -sqrt((-0.8596136949374525 + m.x282)**2 + (
    -0.6658137355569159 + m.x283)**2 + (-0.1854598161134392 + m.x284)**2 + (
    -0.3899285200718041 + m.x285)**2) + m.x111 - 2 * m.b436 >= -2)
m.e112 = Constraint(expr= -sqrt((-0.23942936687819738 + m.x282)**2 + (
    -0.7931287877223899 + m.x283)**2 + (-0.009184110257544176 + m.x284)**2 + (
    -0.7905476817951573 + m.x285)**2) + m.x112 - 2 * m.b437 >= -2)
m.e113 = Constraint(expr= -sqrt((-0.1667763675050825 + m.x282)**2 + (
    -0.30614199209589266 + m.x283)**2 + (-0.6286784916754126 + m.x284)**2 + (
    -0.6749145697726233 + m.x285)**2) + m.x113 - 2 * m.b438 >= -2)
m.e114 = Constraint(expr= -sqrt((-0.5123965188595846 + m.x282)**2 + (
    -0.556215195448374 + m.x283)**2 + (-0.5888863209509851 + m.x284)**2 + (
    -0.6003058073162648 + m.x285)**2) + m.x114 - 2 * m.b439 >= -2)
m.e115 = Constraint(expr= -sqrt((-0.10830095398871686 + m.x282)**2 + (
    -0.301870958131248 + m.x283)**2 + (-0.020499027923741364 + m.x284)**2 + (
    -0.5668022276384451 + m.x285)**2) + m.x115 - 2 * m.b440 >= -2)
m.e116 = Constraint(expr= -sqrt((-0.29450295704025886 + m.x282)**2 + (
    -0.24215631594412912 + m.x283)**2 + (-0.2744568069724159 + m.x284)**2 + (
    -0.9412593709117075 + m.x285)**2) + m.x116 - 2 * m.b441 >= -2)
m.e117 = Constraint(expr= -sqrt((-0.1282338254681593 + m.x282)**2 + (
    -0.9019460548181631 + m.x283)**2 + (-0.9031736614711603 + m.x284)**2 + (
    -0.2037984038273466 + m.x285)**2) + m.x117 - 2 * m.b442 >= -2)
m.e118 = Constraint(expr= -sqrt((-0.829797266931312 + m.x282)**2 + (
    -0.19575994148177733 + m.x283)**2 + (-0.645872503285497 + m.x284)**2 + (
    -0.12203855440196454 + m.x285)**2) + m.x118 - 2 * m.b443 >= -2)
m.e119 = Constraint(expr= -sqrt((-0.318405760895906 + m.x282)**2 + (
    -0.4938036901276964 + m.x283)**2 + (-0.37642068481077395 + m.x284)**2 + (
    -0.8256324717799948 + m.x285)**2) + m.x119 - 2 * m.b444 >= -2)
m.e120 = Constraint(expr= -sqrt((-0.6465433247102469 + m.x282)**2 + (
    -0.033522650784374886 + m.x283)**2 + (-0.5581254938339517 + m.x284)**2 + (
    -0.0912916889874551 + m.x285)**2) + m.x120 - 2 * m.b445 >= -2)
m.e121 = Constraint(expr= -sqrt((-0.17497888842654896 + m.x282)**2 + (
    -0.38968471952782524 + m.x283)**2 + (-0.3152812984667659 + m.x284)**2 + (
    -0.5561379670293034 + m.x285)**2) + m.x121 - 2 * m.b446 >= -2)
m.e122 = Constraint(expr= -sqrt((-0.9831483568003972 + m.x282)**2 + (
    -0.7793186335882816 + m.x283)**2 + (-0.545443726285844 + m.x284)**2 + (
    -0.8394599012498352 + m.x285)**2) + m.x122 - 2 * m.b447 >= -2)
m.e123 = Constraint(expr= -sqrt((-0.16871130717858907 + m.x282)**2 + (
    -0.7158922205435296 + m.x283)**2 + (-0.9716203470560987 + m.x284)**2 + (
    -0.9419601863446189 + m.x285)**2) + m.x123 - 2 * m.b448 >= -2)
m.e124 = Constraint(expr= -sqrt((-0.3078067547337774 + m.x286)**2 + (
    -0.5779578771750392 + m.x287)**2 + (-0.26561803541817575 + m.x288)**2 + (
    -0.8078960514329893 + m.x289)**2) + m.x124 - 2 * m.b449 >= -2)
m.e125 = Constraint(expr= -sqrt((-0.4672172210012604 + m.x286)**2 + (
    -0.33251980673741144 + m.x287)**2 + (-0.8967525962082569 + m.x288)**2 + (
    -0.7924119898695275 + m.x289)**2) + m.x125 - 2 * m.b450 >= -2)
m.e126 = Constraint(expr= -sqrt((-0.8596136949374525 + m.x286)**2 + (
    -0.6658137355569159 + m.x287)**2 + (-0.1854598161134392 + m.x288)**2 + (
    -0.3899285200718041 + m.x289)**2) + m.x126 - 2 * m.b451 >= -2)
m.e127 = Constraint(expr= -sqrt((-0.23942936687819738 + m.x286)**2 + (
    -0.7931287877223899 + m.x287)**2 + (-0.009184110257544176 + m.x288)**2 + (
    -0.7905476817951573 + m.x289)**2) + m.x127 - 2 * m.b452 >= -2)
m.e128 = Constraint(expr= -sqrt((-0.1667763675050825 + m.x286)**2 + (
    -0.30614199209589266 + m.x287)**2 + (-0.6286784916754126 + m.x288)**2 + (
    -0.6749145697726233 + m.x289)**2) + m.x128 - 2 * m.b453 >= -2)
m.e129 = Constraint(expr= -sqrt((-0.5123965188595846 + m.x286)**2 + (
    -0.556215195448374 + m.x287)**2 + (-0.5888863209509851 + m.x288)**2 + (
    -0.6003058073162648 + m.x289)**2) + m.x129 - 2 * m.b454 >= -2)
m.e130 = Constraint(expr= -sqrt((-0.10830095398871686 + m.x286)**2 + (
    -0.301870958131248 + m.x287)**2 + (-0.020499027923741364 + m.x288)**2 + (
    -0.5668022276384451 + m.x289)**2) + m.x130 - 2 * m.b455 >= -2)
m.e131 = Constraint(expr= -sqrt((-0.29450295704025886 + m.x286)**2 + (
    -0.24215631594412912 + m.x287)**2 + (-0.2744568069724159 + m.x288)**2 + (
    -0.9412593709117075 + m.x289)**2) + m.x131 - 2 * m.b456 >= -2)
m.e132 = Constraint(expr= -sqrt((-0.1282338254681593 + m.x286)**2 + (
    -0.9019460548181631 + m.x287)**2 + (-0.9031736614711603 + m.x288)**2 + (
    -0.2037984038273466 + m.x289)**2) + m.x132 - 2 * m.b457 >= -2)
m.e133 = Constraint(expr= -sqrt((-0.829797266931312 + m.x286)**2 + (
    -0.19575994148177733 + m.x287)**2 + (-0.645872503285497 + m.x288)**2 + (
    -0.12203855440196454 + m.x289)**2) + m.x133 - 2 * m.b458 >= -2)
m.e134 = Constraint(expr= -sqrt((-0.318405760895906 + m.x286)**2 + (
    -0.4938036901276964 + m.x287)**2 + (-0.37642068481077395 + m.x288)**2 + (
    -0.8256324717799948 + m.x289)**2) + m.x134 - 2 * m.b459 >= -2)
m.e135 = Constraint(expr= -sqrt((-0.6465433247102469 + m.x286)**2 + (
    -0.033522650784374886 + m.x287)**2 + (-0.5581254938339517 + m.x288)**2 + (
    -0.0912916889874551 + m.x289)**2) + m.x135 - 2 * m.b460 >= -2)
m.e136 = Constraint(expr= -sqrt((-0.17497888842654896 + m.x286)**2 + (
    -0.38968471952782524 + m.x287)**2 + (-0.3152812984667659 + m.x288)**2 + (
    -0.5561379670293034 + m.x289)**2) + m.x136 - 2 * m.b461 >= -2)
m.e137 = Constraint(expr= -sqrt((-0.9831483568003972 + m.x286)**2 + (
    -0.7793186335882816 + m.x287)**2 + (-0.545443726285844 + m.x288)**2 + (
    -0.8394599012498352 + m.x289)**2) + m.x137 - 2 * m.b462 >= -2)
m.e138 = Constraint(expr= -sqrt((-0.16871130717858907 + m.x286)**2 + (
    -0.7158922205435296 + m.x287)**2 + (-0.9716203470560987 + m.x288)**2 + (
    -0.9419601863446189 + m.x289)**2) + m.x138 - 2 * m.b463 >= -2)
m.e139 = Constraint(expr= -sqrt((-0.3078067547337774 + m.x290)**2 + (
    -0.5779578771750392 + m.x291)**2 + (-0.26561803541817575 + m.x292)**2 + (
    -0.8078960514329893 + m.x293)**2) + m.x139 - 2 * m.b464 >= -2)
m.e140 = Constraint(expr= -sqrt((-0.4672172210012604 + m.x290)**2 + (
    -0.33251980673741144 + m.x291)**2 + (-0.8967525962082569 + m.x292)**2 + (
    -0.7924119898695275 + m.x293)**2) + m.x140 - 2 * m.b465 >= -2)
m.e141 = Constraint(expr= -sqrt((-0.8596136949374525 + m.x290)**2 + (
    -0.6658137355569159 + m.x291)**2 + (-0.1854598161134392 + m.x292)**2 + (
    -0.3899285200718041 + m.x293)**2) + m.x141 - 2 * m.b466 >= -2)
m.e142 = Constraint(expr= -sqrt((-0.23942936687819738 + m.x290)**2 + (
    -0.7931287877223899 + m.x291)**2 + (-0.009184110257544176 + m.x292)**2 + (
    -0.7905476817951573 + m.x293)**2) + m.x142 - 2 * m.b467 >= -2)
m.e143 = Constraint(expr= -sqrt((-0.1667763675050825 + m.x290)**2 + (
    -0.30614199209589266 + m.x291)**2 + (-0.6286784916754126 + m.x292)**2 + (
    -0.6749145697726233 + m.x293)**2) + m.x143 - 2 * m.b468 >= -2)
m.e144 = Constraint(expr= -sqrt((-0.5123965188595846 + m.x290)**2 + (
    -0.556215195448374 + m.x291)**2 + (-0.5888863209509851 + m.x292)**2 + (
    -0.6003058073162648 + m.x293)**2) + m.x144 - 2 * m.b469 >= -2)
m.e145 = Constraint(expr= -sqrt((-0.10830095398871686 + m.x290)**2 + (
    -0.301870958131248 + m.x291)**2 + (-0.020499027923741364 + m.x292)**2 + (
    -0.5668022276384451 + m.x293)**2) + m.x145 - 2 * m.b470 >= -2)
m.e146 = Constraint(expr= -sqrt((-0.29450295704025886 + m.x290)**2 + (
    -0.24215631594412912 + m.x291)**2 + (-0.2744568069724159 + m.x292)**2 + (
    -0.9412593709117075 + m.x293)**2) + m.x146 - 2 * m.b471 >= -2)
m.e147 = Constraint(expr= -sqrt((-0.1282338254681593 + m.x290)**2 + (
    -0.9019460548181631 + m.x291)**2 + (-0.9031736614711603 + m.x292)**2 + (
    -0.2037984038273466 + m.x293)**2) + m.x147 - 2 * m.b472 >= -2)
m.e148 = Constraint(expr= -sqrt((-0.829797266931312 + m.x290)**2 + (
    -0.19575994148177733 + m.x291)**2 + (-0.645872503285497 + m.x292)**2 + (
    -0.12203855440196454 + m.x293)**2) + m.x148 - 2 * m.b473 >= -2)
m.e149 = Constraint(expr= -sqrt((-0.318405760895906 + m.x290)**2 + (
    -0.4938036901276964 + m.x291)**2 + (-0.37642068481077395 + m.x292)**2 + (
    -0.8256324717799948 + m.x293)**2) + m.x149 - 2 * m.b474 >= -2)
m.e150 = Constraint(expr= -sqrt((-0.6465433247102469 + m.x290)**2 + (
    -0.033522650784374886 + m.x291)**2 + (-0.5581254938339517 + m.x292)**2 + (
    -0.0912916889874551 + m.x293)**2) + m.x150 - 2 * m.b475 >= -2)
m.e151 = Constraint(expr= -sqrt((-0.17497888842654896 + m.x290)**2 + (
    -0.38968471952782524 + m.x291)**2 + (-0.3152812984667659 + m.x292)**2 + (
    -0.5561379670293034 + m.x293)**2) + m.x151 - 2 * m.b476 >= -2)
m.e152 = Constraint(expr= -sqrt((-0.9831483568003972 + m.x290)**2 + (
    -0.7793186335882816 + m.x291)**2 + (-0.545443726285844 + m.x292)**2 + (
    -0.8394599012498352 + m.x293)**2) + m.x152 - 2 * m.b477 >= -2)
m.e153 = Constraint(expr= -sqrt((-0.16871130717858907 + m.x290)**2 + (
    -0.7158922205435296 + m.x291)**2 + (-0.9716203470560987 + m.x292)**2 + (
    -0.9419601863446189 + m.x293)**2) + m.x153 - 2 * m.b478 >= -2)
m.e154 = Constraint(expr= -sqrt((-0.3078067547337774 + m.x294)**2 + (
    -0.5779578771750392 + m.x295)**2 + (-0.26561803541817575 + m.x296)**2 + (
    -0.8078960514329893 + m.x297)**2) + m.x154 - 2 * m.b479 >= -2)
m.e155 = Constraint(expr= -sqrt((-0.4672172210012604 + m.x294)**2 + (
    -0.33251980673741144 + m.x295)**2 + (-0.8967525962082569 + m.x296)**2 + (
    -0.7924119898695275 + m.x297)**2) + m.x155 - 2 * m.b480 >= -2)
m.e156 = Constraint(expr= -sqrt((-0.8596136949374525 + m.x294)**2 + (
    -0.6658137355569159 + m.x295)**2 + (-0.1854598161134392 + m.x296)**2 + (
    -0.3899285200718041 + m.x297)**2) + m.x156 - 2 * m.b481 >= -2)
m.e157 = Constraint(expr= -sqrt((-0.23942936687819738 + m.x294)**2 + (
    -0.7931287877223899 + m.x295)**2 + (-0.009184110257544176 + m.x296)**2 + (
    -0.7905476817951573 + m.x297)**2) + m.x157 - 2 * m.b482 >= -2)
m.e158 = Constraint(expr= -sqrt((-0.1667763675050825 + m.x294)**2 + (
    -0.30614199209589266 + m.x295)**2 + (-0.6286784916754126 + m.x296)**2 + (
    -0.6749145697726233 + m.x297)**2) + m.x158 - 2 * m.b483 >= -2)
m.e159 = Constraint(expr= -sqrt((-0.5123965188595846 + m.x294)**2 + (
    -0.556215195448374 + m.x295)**2 + (-0.5888863209509851 + m.x296)**2 + (
    -0.6003058073162648 + m.x297)**2) + m.x159 - 2 * m.b484 >= -2)
m.e160 = Constraint(expr= -sqrt((-0.10830095398871686 + m.x294)**2 + (
    -0.301870958131248 + m.x295)**2 + (-0.020499027923741364 + m.x296)**2 + (
    -0.5668022276384451 + m.x297)**2) + m.x160 - 2 * m.b485 >= -2)
m.e161 = Constraint(expr= -sqrt((-0.29450295704025886 + m.x294)**2 + (
    -0.24215631594412912 + m.x295)**2 + (-0.2744568069724159 + m.x296)**2 + (
    -0.9412593709117075 + m.x297)**2) + m.x161 - 2 * m.b486 >= -2)
m.e162 = Constraint(expr= -sqrt((-0.1282338254681593 + m.x294)**2 + (
    -0.9019460548181631 + m.x295)**2 + (-0.9031736614711603 + m.x296)**2 + (
    -0.2037984038273466 + m.x297)**2) + m.x162 - 2 * m.b487 >= -2)
m.e163 = Constraint(expr= -sqrt((-0.829797266931312 + m.x294)**2 + (
    -0.19575994148177733 + m.x295)**2 + (-0.645872503285497 + m.x296)**2 + (
    -0.12203855440196454 + m.x297)**2) + m.x163 - 2 * m.b488 >= -2)
m.e164 = Constraint(expr= -sqrt((-0.318405760895906 + m.x294)**2 + (
    -0.4938036901276964 + m.x295)**2 + (-0.37642068481077395 + m.x296)**2 + (
    -0.8256324717799948 + m.x297)**2) + m.x164 - 2 * m.b489 >= -2)
m.e165 = Constraint(expr= -sqrt((-0.6465433247102469 + m.x294)**2 + (
    -0.033522650784374886 + m.x295)**2 + (-0.5581254938339517 + m.x296)**2 + (
    -0.0912916889874551 + m.x297)**2) + m.x165 - 2 * m.b490 >= -2)
m.e166 = Constraint(expr= -sqrt((-0.17497888842654896 + m.x294)**2 + (
    -0.38968471952782524 + m.x295)**2 + (-0.3152812984667659 + m.x296)**2 + (
    -0.5561379670293034 + m.x297)**2) + m.x166 - 2 * m.b491 >= -2)
m.e167 = Constraint(expr= -sqrt((-0.9831483568003972 + m.x294)**2 + (
    -0.7793186335882816 + m.x295)**2 + (-0.545443726285844 + m.x296)**2 + (
    -0.8394599012498352 + m.x297)**2) + m.x167 - 2 * m.b492 >= -2)
m.e168 = Constraint(expr= -sqrt((-0.16871130717858907 + m.x294)**2 + (
    -0.7158922205435296 + m.x295)**2 + (-0.9716203470560987 + m.x296)**2 + (
    -0.9419601863446189 + m.x297)**2) + m.x168 - 2 * m.b493 >= -2)
m.e169 = Constraint(expr= -sqrt((-0.3078067547337774 + m.x298)**2 + (
    -0.5779578771750392 + m.x299)**2 + (-0.26561803541817575 + m.x300)**2 + (
    -0.8078960514329893 + m.x301)**2) + m.x169 - 2 * m.b494 >= -2)
m.e170 = Constraint(expr= -sqrt((-0.4672172210012604 + m.x298)**2 + (
    -0.33251980673741144 + m.x299)**2 + (-0.8967525962082569 + m.x300)**2 + (
    -0.7924119898695275 + m.x301)**2) + m.x170 - 2 * m.b495 >= -2)
m.e171 = Constraint(expr= -sqrt((-0.8596136949374525 + m.x298)**2 + (
    -0.6658137355569159 + m.x299)**2 + (-0.1854598161134392 + m.x300)**2 + (
    -0.3899285200718041 + m.x301)**2) + m.x171 - 2 * m.b496 >= -2)
m.e172 = Constraint(expr= -sqrt((-0.23942936687819738 + m.x298)**2 + (
    -0.7931287877223899 + m.x299)**2 + (-0.009184110257544176 + m.x300)**2 + (
    -0.7905476817951573 + m.x301)**2) + m.x172 - 2 * m.b497 >= -2)
m.e173 = Constraint(expr= -sqrt((-0.1667763675050825 + m.x298)**2 + (
    -0.30614199209589266 + m.x299)**2 + (-0.6286784916754126 + m.x300)**2 + (
    -0.6749145697726233 + m.x301)**2) + m.x173 - 2 * m.b498 >= -2)
m.e174 = Constraint(expr= -sqrt((-0.5123965188595846 + m.x298)**2 + (
    -0.556215195448374 + m.x299)**2 + (-0.5888863209509851 + m.x300)**2 + (
    -0.6003058073162648 + m.x301)**2) + m.x174 - 2 * m.b499 >= -2)
m.e175 = Constraint(expr= -sqrt((-0.10830095398871686 + m.x298)**2 + (
    -0.301870958131248 + m.x299)**2 + (-0.020499027923741364 + m.x300)**2 + (
    -0.5668022276384451 + m.x301)**2) + m.x175 - 2 * m.b500 >= -2)
m.e176 = Constraint(expr= -sqrt((-0.29450295704025886 + m.x298)**2 + (
    -0.24215631594412912 + m.x299)**2 + (-0.2744568069724159 + m.x300)**2 + (
    -0.9412593709117075 + m.x301)**2) + m.x176 - 2 * m.b501 >= -2)
m.e177 = Constraint(expr= -sqrt((-0.1282338254681593 + m.x298)**2 + (
    -0.9019460548181631 + m.x299)**2 + (-0.9031736614711603 + m.x300)**2 + (
    -0.2037984038273466 + m.x301)**2) + m.x177 - 2 * m.b502 >= -2)
m.e178 = Constraint(expr= -sqrt((-0.829797266931312 + m.x298)**2 + (
    -0.19575994148177733 + m.x299)**2 + (-0.645872503285497 + m.x300)**2 + (
    -0.12203855440196454 + m.x301)**2) + m.x178 - 2 * m.b503 >= -2)
m.e179 = Constraint(expr= -sqrt((-0.318405760895906 + m.x298)**2 + (
    -0.4938036901276964 + m.x299)**2 + (-0.37642068481077395 + m.x300)**2 + (
    -0.8256324717799948 + m.x301)**2) + m.x179 - 2 * m.b504 >= -2)
m.e180 = Constraint(expr= -sqrt((-0.6465433247102469 + m.x298)**2 + (
    -0.033522650784374886 + m.x299)**2 + (-0.5581254938339517 + m.x300)**2 + (
    -0.0912916889874551 + m.x301)**2) + m.x180 - 2 * m.b505 >= -2)
m.e181 = Constraint(expr= -sqrt((-0.17497888842654896 + m.x298)**2 + (
    -0.38968471952782524 + m.x299)**2 + (-0.3152812984667659 + m.x300)**2 + (
    -0.5561379670293034 + m.x301)**2) + m.x181 - 2 * m.b506 >= -2)
m.e182 = Constraint(expr= -sqrt((-0.9831483568003972 + m.x298)**2 + (
    -0.7793186335882816 + m.x299)**2 + (-0.545443726285844 + m.x300)**2 + (
    -0.8394599012498352 + m.x301)**2) + m.x182 - 2 * m.b507 >= -2)
m.e183 = Constraint(expr= -sqrt((-0.16871130717858907 + m.x298)**2 + (
    -0.7158922205435296 + m.x299)**2 + (-0.9716203470560987 + m.x300)**2 + (
    -0.9419601863446189 + m.x301)**2) + m.x183 - 2 * m.b508 >= -2)
m.e184 = Constraint(expr= -sqrt((-0.3078067547337774 + m.x302)**2 + (
    -0.5779578771750392 + m.x303)**2 + (-0.26561803541817575 + m.x304)**2 + (
    -0.8078960514329893 + m.x305)**2) + m.x184 - 2 * m.b509 >= -2)
m.e185 = Constraint(expr= -sqrt((-0.4672172210012604 + m.x302)**2 + (
    -0.33251980673741144 + m.x303)**2 + (-0.8967525962082569 + m.x304)**2 + (
    -0.7924119898695275 + m.x305)**2) + m.x185 - 2 * m.b510 >= -2)
m.e186 = Constraint(expr= -sqrt((-0.8596136949374525 + m.x302)**2 + (
    -0.6658137355569159 + m.x303)**2 + (-0.1854598161134392 + m.x304)**2 + (
    -0.3899285200718041 + m.x305)**2) + m.x186 - 2 * m.b511 >= -2)
m.e187 = Constraint(expr= -sqrt((-0.23942936687819738 + m.x302)**2 + (
    -0.7931287877223899 + m.x303)**2 + (-0.009184110257544176 + m.x304)**2 + (
    -0.7905476817951573 + m.x305)**2) + m.x187 - 2 * m.b512 >= -2)
m.e188 = Constraint(expr= -sqrt((-0.1667763675050825 + m.x302)**2 + (
    -0.30614199209589266 + m.x303)**2 + (-0.6286784916754126 + m.x304)**2 + (
    -0.6749145697726233 + m.x305)**2) + m.x188 - 2 * m.b513 >= -2)
m.e189 = Constraint(expr= -sqrt((-0.5123965188595846 + m.x302)**2 + (
    -0.556215195448374 + m.x303)**2 + (-0.5888863209509851 + m.x304)**2 + (
    -0.6003058073162648 + m.x305)**2) + m.x189 - 2 * m.b514 >= -2)
m.e190 = Constraint(expr= -sqrt((-0.10830095398871686 + m.x302)**2 + (
    -0.301870958131248 + m.x303)**2 + (-0.020499027923741364 + m.x304)**2 + (
    -0.5668022276384451 + m.x305)**2) + m.x190 - 2 * m.b515 >= -2)
m.e191 = Constraint(expr= -sqrt((-0.29450295704025886 + m.x302)**2 + (
    -0.24215631594412912 + m.x303)**2 + (-0.2744568069724159 + m.x304)**2 + (
    -0.9412593709117075 + m.x305)**2) + m.x191 - 2 * m.b516 >= -2)
m.e192 = Constraint(expr= -sqrt((-0.1282338254681593 + m.x302)**2 + (
    -0.9019460548181631 + m.x303)**2 + (-0.9031736614711603 + m.x304)**2 + (
    -0.2037984038273466 + m.x305)**2) + m.x192 - 2 * m.b517 >= -2)
m.e193 = Constraint(expr= -sqrt((-0.829797266931312 + m.x302)**2 + (
    -0.19575994148177733 + m.x303)**2 + (-0.645872503285497 + m.x304)**2 + (
    -0.12203855440196454 + m.x305)**2) + m.x193 - 2 * m.b518 >= -2)
m.e194 = Constraint(expr= -sqrt((-0.318405760895906 + m.x302)**2 + (
    -0.4938036901276964 + m.x303)**2 + (-0.37642068481077395 + m.x304)**2 + (
    -0.8256324717799948 + m.x305)**2) + m.x194 - 2 * m.b519 >= -2)
m.e195 = Constraint(expr= -sqrt((-0.6465433247102469 + m.x302)**2 + (
    -0.033522650784374886 + m.x303)**2 + (-0.5581254938339517 + m.x304)**2 + (
    -0.0912916889874551 + m.x305)**2) + m.x195 - 2 * m.b520 >= -2)
m.e196 = Constraint(expr= -sqrt((-0.17497888842654896 + m.x302)**2 + (
    -0.38968471952782524 + m.x303)**2 + (-0.3152812984667659 + m.x304)**2 + (
    -0.5561379670293034 + m.x305)**2) + m.x196 - 2 * m.b521 >= -2)
m.e197 = Constraint(expr= -sqrt((-0.9831483568003972 + m.x302)**2 + (
    -0.7793186335882816 + m.x303)**2 + (-0.545443726285844 + m.x304)**2 + (
    -0.8394599012498352 + m.x305)**2) + m.x197 - 2 * m.b522 >= -2)
m.e198 = Constraint(expr= -sqrt((-0.16871130717858907 + m.x302)**2 + (
    -0.7158922205435296 + m.x303)**2 + (-0.9716203470560987 + m.x304)**2 + (
    -0.9419601863446189 + m.x305)**2) + m.x198 - 2 * m.b523 >= -2)
m.e199 = Constraint(expr= -sqrt((-0.3078067547337774 + m.x306)**2 + (
    -0.5779578771750392 + m.x307)**2 + (-0.26561803541817575 + m.x308)**2 + (
    -0.8078960514329893 + m.x309)**2) + m.x199 - 2 * m.b524 >= -2)
m.e200 = Constraint(expr= -sqrt((-0.4672172210012604 + m.x306)**2 + (
    -0.33251980673741144 + m.x307)**2 + (-0.8967525962082569 + m.x308)**2 + (
    -0.7924119898695275 + m.x309)**2) + m.x200 - 2 * m.b525 >= -2)
m.e201 = Constraint(expr= -sqrt((-0.8596136949374525 + m.x306)**2 + (
    -0.6658137355569159 + m.x307)**2 + (-0.1854598161134392 + m.x308)**2 + (
    -0.3899285200718041 + m.x309)**2) + m.x201 - 2 * m.b526 >= -2)
m.e202 = Constraint(expr= -sqrt((-0.23942936687819738 + m.x306)**2 + (
    -0.7931287877223899 + m.x307)**2 + (-0.009184110257544176 + m.x308)**2 + (
    -0.7905476817951573 + m.x309)**2) + m.x202 - 2 * m.b527 >= -2)
m.e203 = Constraint(expr= -sqrt((-0.1667763675050825 + m.x306)**2 + (
    -0.30614199209589266 + m.x307)**2 + (-0.6286784916754126 + m.x308)**2 + (
    -0.6749145697726233 + m.x309)**2) + m.x203 - 2 * m.b528 >= -2)
m.e204 = Constraint(expr= -sqrt((-0.5123965188595846 + m.x306)**2 + (
    -0.556215195448374 + m.x307)**2 + (-0.5888863209509851 + m.x308)**2 + (
    -0.6003058073162648 + m.x309)**2) + m.x204 - 2 * m.b529 >= -2)
m.e205 = Constraint(expr= -sqrt((-0.10830095398871686 + m.x306)**2 + (
    -0.301870958131248 + m.x307)**2 + (-0.020499027923741364 + m.x308)**2 + (
    -0.5668022276384451 + m.x309)**2) + m.x205 - 2 * m.b530 >= -2)
m.e206 = Constraint(expr= -sqrt((-0.29450295704025886 + m.x306)**2 + (
    -0.24215631594412912 + m.x307)**2 + (-0.2744568069724159 + m.x308)**2 + (
    -0.9412593709117075 + m.x309)**2) + m.x206 - 2 * m.b531 >= -2)
m.e207 = Constraint(expr= -sqrt((-0.1282338254681593 + m.x306)**2 + (
    -0.9019460548181631 + m.x307)**2 + (-0.9031736614711603 + m.x308)**2 + (
    -0.2037984038273466 + m.x309)**2) + m.x207 - 2 * m.b532 >= -2)
m.e208 = Constraint(expr= -sqrt((-0.829797266931312 + m.x306)**2 + (
    -0.19575994148177733 + m.x307)**2 + (-0.645872503285497 + m.x308)**2 + (
    -0.12203855440196454 + m.x309)**2) + m.x208 - 2 * m.b533 >= -2)
m.e209 = Constraint(expr= -sqrt((-0.318405760895906 + m.x306)**2 + (
    -0.4938036901276964 + m.x307)**2 + (-0.37642068481077395 + m.x308)**2 + (
    -0.8256324717799948 + m.x309)**2) + m.x209 - 2 * m.b534 >= -2)
m.e210 = Constraint(expr= -sqrt((-0.6465433247102469 + m.x306)**2 + (
    -0.033522650784374886 + m.x307)**2 + (-0.5581254938339517 + m.x308)**2 + (
    -0.0912916889874551 + m.x309)**2) + m.x210 - 2 * m.b535 >= -2)
m.e211 = Constraint(expr= -sqrt((-0.17497888842654896 + m.x306)**2 + (
    -0.38968471952782524 + m.x307)**2 + (-0.3152812984667659 + m.x308)**2 + (
    -0.5561379670293034 + m.x309)**2) + m.x211 - 2 * m.b536 >= -2)
m.e212 = Constraint(expr= -sqrt((-0.9831483568003972 + m.x306)**2 + (
    -0.7793186335882816 + m.x307)**2 + (-0.545443726285844 + m.x308)**2 + (
    -0.8394599012498352 + m.x309)**2) + m.x212 - 2 * m.b537 >= -2)
m.e213 = Constraint(expr= -sqrt((-0.16871130717858907 + m.x306)**2 + (
    -0.7158922205435296 + m.x307)**2 + (-0.9716203470560987 + m.x308)**2 + (
    -0.9419601863446189 + m.x309)**2) + m.x213 - 2 * m.b538 >= -2)
m.e214 = Constraint(expr= -sqrt((-0.3078067547337774 + m.x310)**2 + (
    -0.5779578771750392 + m.x311)**2 + (-0.26561803541817575 + m.x312)**2 + (
    -0.8078960514329893 + m.x313)**2) + m.x214 - 2 * m.b539 >= -2)
m.e215 = Constraint(expr= -sqrt((-0.4672172210012604 + m.x310)**2 + (
    -0.33251980673741144 + m.x311)**2 + (-0.8967525962082569 + m.x312)**2 + (
    -0.7924119898695275 + m.x313)**2) + m.x215 - 2 * m.b540 >= -2)
m.e216 = Constraint(expr= -sqrt((-0.8596136949374525 + m.x310)**2 + (
    -0.6658137355569159 + m.x311)**2 + (-0.1854598161134392 + m.x312)**2 + (
    -0.3899285200718041 + m.x313)**2) + m.x216 - 2 * m.b541 >= -2)
m.e217 = Constraint(expr= -sqrt((-0.23942936687819738 + m.x310)**2 + (
    -0.7931287877223899 + m.x311)**2 + (-0.009184110257544176 + m.x312)**2 + (
    -0.7905476817951573 + m.x313)**2) + m.x217 - 2 * m.b542 >= -2)
m.e218 = Constraint(expr= -sqrt((-0.1667763675050825 + m.x310)**2 + (
    -0.30614199209589266 + m.x311)**2 + (-0.6286784916754126 + m.x312)**2 + (
    -0.6749145697726233 + m.x313)**2) + m.x218 - 2 * m.b543 >= -2)
m.e219 = Constraint(expr= -sqrt((-0.5123965188595846 + m.x310)**2 + (
    -0.556215195448374 + m.x311)**2 + (-0.5888863209509851 + m.x312)**2 + (
    -0.6003058073162648 + m.x313)**2) + m.x219 - 2 * m.b544 >= -2)
m.e220 = Constraint(expr= -sqrt((-0.10830095398871686 + m.x310)**2 + (
    -0.301870958131248 + m.x311)**2 + (-0.020499027923741364 + m.x312)**2 + (
    -0.5668022276384451 + m.x313)**2) + m.x220 - 2 * m.b545 >= -2)
m.e221 = Constraint(expr= -sqrt((-0.29450295704025886 + m.x310)**2 + (
    -0.24215631594412912 + m.x311)**2 + (-0.2744568069724159 + m.x312)**2 + (
    -0.9412593709117075 + m.x313)**2) + m.x221 - 2 * m.b546 >= -2)
m.e222 = Constraint(expr= -sqrt((-0.1282338254681593 + m.x310)**2 + (
    -0.9019460548181631 + m.x311)**2 + (-0.9031736614711603 + m.x312)**2 + (
    -0.2037984038273466 + m.x313)**2) + m.x222 - 2 * m.b547 >= -2)
m.e223 = Constraint(expr= -sqrt((-0.829797266931312 + m.x310)**2 + (
    -0.19575994148177733 + m.x311)**2 + (-0.645872503285497 + m.x312)**2 + (
    -0.12203855440196454 + m.x313)**2) + m.x223 - 2 * m.b548 >= -2)
m.e224 = Constraint(expr= -sqrt((-0.318405760895906 + m.x310)**2 + (
    -0.4938036901276964 + m.x311)**2 + (-0.37642068481077395 + m.x312)**2 + (
    -0.8256324717799948 + m.x313)**2) + m.x224 - 2 * m.b549 >= -2)
m.e225 = Constraint(expr= -sqrt((-0.6465433247102469 + m.x310)**2 + (
    -0.033522650784374886 + m.x311)**2 + (-0.5581254938339517 + m.x312)**2 + (
    -0.0912916889874551 + m.x313)**2) + m.x225 - 2 * m.b550 >= -2)
m.e226 = Constraint(expr= -sqrt((-0.17497888842654896 + m.x310)**2 + (
    -0.38968471952782524 + m.x311)**2 + (-0.3152812984667659 + m.x312)**2 + (
    -0.5561379670293034 + m.x313)**2) + m.x226 - 2 * m.b551 >= -2)
m.e227 = Constraint(expr= -sqrt((-0.9831483568003972 + m.x310)**2 + (
    -0.7793186335882816 + m.x311)**2 + (-0.545443726285844 + m.x312)**2 + (
    -0.8394599012498352 + m.x313)**2) + m.x227 - 2 * m.b552 >= -2)
m.e228 = Constraint(expr= -sqrt((-0.16871130717858907 + m.x310)**2 + (
    -0.7158922205435296 + m.x311)**2 + (-0.9716203470560987 + m.x312)**2 + (
    -0.9419601863446189 + m.x313)**2) + m.x228 - 2 * m.b553 >= -2)
m.e229 = Constraint(expr= -sqrt((-0.3078067547337774 + m.x314)**2 + (
    -0.5779578771750392 + m.x315)**2 + (-0.26561803541817575 + m.x316)**2 + (
    -0.8078960514329893 + m.x317)**2) + m.x229 - 2 * m.b554 >= -2)
m.e230 = Constraint(expr= -sqrt((-0.4672172210012604 + m.x314)**2 + (
    -0.33251980673741144 + m.x315)**2 + (-0.8967525962082569 + m.x316)**2 + (
    -0.7924119898695275 + m.x317)**2) + m.x230 - 2 * m.b555 >= -2)
m.e231 = Constraint(expr= -sqrt((-0.8596136949374525 + m.x314)**2 + (
    -0.6658137355569159 + m.x315)**2 + (-0.1854598161134392 + m.x316)**2 + (
    -0.3899285200718041 + m.x317)**2) + m.x231 - 2 * m.b556 >= -2)
m.e232 = Constraint(expr= -sqrt((-0.23942936687819738 + m.x314)**2 + (
    -0.7931287877223899 + m.x315)**2 + (-0.009184110257544176 + m.x316)**2 + (
    -0.7905476817951573 + m.x317)**2) + m.x232 - 2 * m.b557 >= -2)
m.e233 = Constraint(expr= -sqrt((-0.1667763675050825 + m.x314)**2 + (
    -0.30614199209589266 + m.x315)**2 + (-0.6286784916754126 + m.x316)**2 + (
    -0.6749145697726233 + m.x317)**2) + m.x233 - 2 * m.b558 >= -2)
m.e234 = Constraint(expr= -sqrt((-0.5123965188595846 + m.x314)**2 + (
    -0.556215195448374 + m.x315)**2 + (-0.5888863209509851 + m.x316)**2 + (
    -0.6003058073162648 + m.x317)**2) + m.x234 - 2 * m.b559 >= -2)
m.e235 = Constraint(expr= -sqrt((-0.10830095398871686 + m.x314)**2 + (
    -0.301870958131248 + m.x315)**2 + (-0.020499027923741364 + m.x316)**2 + (
    -0.5668022276384451 + m.x317)**2) + m.x235 - 2 * m.b560 >= -2)
m.e236 = Constraint(expr= -sqrt((-0.29450295704025886 + m.x314)**2 + (
    -0.24215631594412912 + m.x315)**2 + (-0.2744568069724159 + m.x316)**2 + (
    -0.9412593709117075 + m.x317)**2) + m.x236 - 2 * m.b561 >= -2)
m.e237 = Constraint(expr= -sqrt((-0.1282338254681593 + m.x314)**2 + (
    -0.9019460548181631 + m.x315)**2 + (-0.9031736614711603 + m.x316)**2 + (
    -0.2037984038273466 + m.x317)**2) + m.x237 - 2 * m.b562 >= -2)
m.e238 = Constraint(expr= -sqrt((-0.829797266931312 + m.x314)**2 + (
    -0.19575994148177733 + m.x315)**2 + (-0.645872503285497 + m.x316)**2 + (
    -0.12203855440196454 + m.x317)**2) + m.x238 - 2 * m.b563 >= -2)
m.e239 = Constraint(expr= -sqrt((-0.318405760895906 + m.x314)**2 + (
    -0.4938036901276964 + m.x315)**2 + (-0.37642068481077395 + m.x316)**2 + (
    -0.8256324717799948 + m.x317)**2) + m.x239 - 2 * m.b564 >= -2)
m.e240 = Constraint(expr= -sqrt((-0.6465433247102469 + m.x314)**2 + (
    -0.033522650784374886 + m.x315)**2 + (-0.5581254938339517 + m.x316)**2 + (
    -0.0912916889874551 + m.x317)**2) + m.x240 - 2 * m.b565 >= -2)
m.e241 = Constraint(expr= -sqrt((-0.17497888842654896 + m.x314)**2 + (
    -0.38968471952782524 + m.x315)**2 + (-0.3152812984667659 + m.x316)**2 + (
    -0.5561379670293034 + m.x317)**2) + m.x241 - 2 * m.b566 >= -2)
m.e242 = Constraint(expr= -sqrt((-0.9831483568003972 + m.x314)**2 + (
    -0.7793186335882816 + m.x315)**2 + (-0.545443726285844 + m.x316)**2 + (
    -0.8394599012498352 + m.x317)**2) + m.x242 - 2 * m.b567 >= -2)
m.e243 = Constraint(expr= -sqrt((-0.16871130717858907 + m.x314)**2 + (
    -0.7158922205435296 + m.x315)**2 + (-0.9716203470560987 + m.x316)**2 + (
    -0.9419601863446189 + m.x317)**2) + m.x243 - 2 * m.b568 >= -2)
m.e244 = Constraint(expr= -sqrt((-0.3078067547337774 + m.x318)**2 + (
    -0.5779578771750392 + m.x319)**2 + (-0.26561803541817575 + m.x320)**2 + (
    -0.8078960514329893 + m.x321)**2) + m.x244 - 2 * m.b569 >= -2)
m.e245 = Constraint(expr= -sqrt((-0.4672172210012604 + m.x318)**2 + (
    -0.33251980673741144 + m.x319)**2 + (-0.8967525962082569 + m.x320)**2 + (
    -0.7924119898695275 + m.x321)**2) + m.x245 - 2 * m.b570 >= -2)
m.e246 = Constraint(expr= -sqrt((-0.8596136949374525 + m.x318)**2 + (
    -0.6658137355569159 + m.x319)**2 + (-0.1854598161134392 + m.x320)**2 + (
    -0.3899285200718041 + m.x321)**2) + m.x246 - 2 * m.b571 >= -2)
m.e247 = Constraint(expr= -sqrt((-0.23942936687819738 + m.x318)**2 + (
    -0.7931287877223899 + m.x319)**2 + (-0.009184110257544176 + m.x320)**2 + (
    -0.7905476817951573 + m.x321)**2) + m.x247 - 2 * m.b572 >= -2)
m.e248 = Constraint(expr= -sqrt((-0.1667763675050825 + m.x318)**2 + (
    -0.30614199209589266 + m.x319)**2 + (-0.6286784916754126 + m.x320)**2 + (
    -0.6749145697726233 + m.x321)**2) + m.x248 - 2 * m.b573 >= -2)
m.e249 = Constraint(expr= -sqrt((-0.5123965188595846 + m.x318)**2 + (
    -0.556215195448374 + m.x319)**2 + (-0.5888863209509851 + m.x320)**2 + (
    -0.6003058073162648 + m.x321)**2) + m.x249 - 2 * m.b574 >= -2)
m.e250 = Constraint(expr= -sqrt((-0.10830095398871686 + m.x318)**2 + (
    -0.301870958131248 + m.x319)**2 + (-0.020499027923741364 + m.x320)**2 + (
    -0.5668022276384451 + m.x321)**2) + m.x250 - 2 * m.b575 >= -2)
m.e251 = Constraint(expr= -sqrt((-0.29450295704025886 + m.x318)**2 + (
    -0.24215631594412912 + m.x319)**2 + (-0.2744568069724159 + m.x320)**2 + (
    -0.9412593709117075 + m.x321)**2) + m.x251 - 2 * m.b576 >= -2)
m.e252 = Constraint(expr= -sqrt((-0.1282338254681593 + m.x318)**2 + (
    -0.9019460548181631 + m.x319)**2 + (-0.9031736614711603 + m.x320)**2 + (
    -0.2037984038273466 + m.x321)**2) + m.x252 - 2 * m.b577 >= -2)
m.e253 = Constraint(expr= -sqrt((-0.829797266931312 + m.x318)**2 + (
    -0.19575994148177733 + m.x319)**2 + (-0.645872503285497 + m.x320)**2 + (
    -0.12203855440196454 + m.x321)**2) + m.x253 - 2 * m.b578 >= -2)
m.e254 = Constraint(expr= -sqrt((-0.318405760895906 + m.x318)**2 + (
    -0.4938036901276964 + m.x319)**2 + (-0.37642068481077395 + m.x320)**2 + (
    -0.8256324717799948 + m.x321)**2) + m.x254 - 2 * m.b579 >= -2)
m.e255 = Constraint(expr= -sqrt((-0.6465433247102469 + m.x318)**2 + (
    -0.033522650784374886 + m.x319)**2 + (-0.5581254938339517 + m.x320)**2 + (
    -0.0912916889874551 + m.x321)**2) + m.x255 - 2 * m.b580 >= -2)
m.e256 = Constraint(expr= -sqrt((-0.17497888842654896 + m.x318)**2 + (
    -0.38968471952782524 + m.x319)**2 + (-0.3152812984667659 + m.x320)**2 + (
    -0.5561379670293034 + m.x321)**2) + m.x256 - 2 * m.b581 >= -2)
m.e257 = Constraint(expr= -sqrt((-0.9831483568003972 + m.x318)**2 + (
    -0.7793186335882816 + m.x319)**2 + (-0.545443726285844 + m.x320)**2 + (
    -0.8394599012498352 + m.x321)**2) + m.x257 - 2 * m.b582 >= -2)
m.e258 = Constraint(expr= -sqrt((-0.16871130717858907 + m.x318)**2 + (
    -0.7158922205435296 + m.x319)**2 + (-0.9716203470560987 + m.x320)**2 + (
    -0.9419601863446189 + m.x321)**2) + m.x258 - 2 * m.b583 >= -2)
m.e259 = Constraint(expr= -sqrt((-0.3078067547337774 + m.x322)**2 + (
    -0.5779578771750392 + m.x323)**2 + (-0.26561803541817575 + m.x324)**2 + (
    -0.8078960514329893 + m.x325)**2) + m.x259 - 2 * m.b584 >= -2)
m.e260 = Constraint(expr= -sqrt((-0.4672172210012604 + m.x322)**2 + (
    -0.33251980673741144 + m.x323)**2 + (-0.8967525962082569 + m.x324)**2 + (
    -0.7924119898695275 + m.x325)**2) + m.x260 - 2 * m.b585 >= -2)
m.e261 = Constraint(expr= -sqrt((-0.8596136949374525 + m.x322)**2 + (
    -0.6658137355569159 + m.x323)**2 + (-0.1854598161134392 + m.x324)**2 + (
    -0.3899285200718041 + m.x325)**2) + m.x261 - 2 * m.b586 >= -2)
m.e262 = Constraint(expr= -sqrt((-0.23942936687819738 + m.x322)**2 + (
    -0.7931287877223899 + m.x323)**2 + (-0.009184110257544176 + m.x324)**2 + (
    -0.7905476817951573 + m.x325)**2) + m.x262 - 2 * m.b587 >= -2)
m.e263 = Constraint(expr= -sqrt((-0.1667763675050825 + m.x322)**2 + (
    -0.30614199209589266 + m.x323)**2 + (-0.6286784916754126 + m.x324)**2 + (
    -0.6749145697726233 + m.x325)**2) + m.x263 - 2 * m.b588 >= -2)
m.e264 = Constraint(expr= -sqrt((-0.5123965188595846 + m.x322)**2 + (
    -0.556215195448374 + m.x323)**2 + (-0.5888863209509851 + m.x324)**2 + (
    -0.6003058073162648 + m.x325)**2) + m.x264 - 2 * m.b589 >= -2)
m.e265 = Constraint(expr= -sqrt((-0.10830095398871686 + m.x322)**2 + (
    -0.301870958131248 + m.x323)**2 + (-0.020499027923741364 + m.x324)**2 + (
    -0.5668022276384451 + m.x325)**2) + m.x265 - 2 * m.b590 >= -2)
m.e266 = Constraint(expr= -sqrt((-0.29450295704025886 + m.x322)**2 + (
    -0.24215631594412912 + m.x323)**2 + (-0.2744568069724159 + m.x324)**2 + (
    -0.9412593709117075 + m.x325)**2) + m.x266 - 2 * m.b591 >= -2)
m.e267 = Constraint(expr= -sqrt((-0.1282338254681593 + m.x322)**2 + (
    -0.9019460548181631 + m.x323)**2 + (-0.9031736614711603 + m.x324)**2 + (
    -0.2037984038273466 + m.x325)**2) + m.x267 - 2 * m.b592 >= -2)
m.e268 = Constraint(expr= -sqrt((-0.829797266931312 + m.x322)**2 + (
    -0.19575994148177733 + m.x323)**2 + (-0.645872503285497 + m.x324)**2 + (
    -0.12203855440196454 + m.x325)**2) + m.x268 - 2 * m.b593 >= -2)
m.e269 = Constraint(expr= -sqrt((-0.318405760895906 + m.x322)**2 + (
    -0.4938036901276964 + m.x323)**2 + (-0.37642068481077395 + m.x324)**2 + (
    -0.8256324717799948 + m.x325)**2) + m.x269 - 2 * m.b594 >= -2)
m.e270 = Constraint(expr= -sqrt((-0.6465433247102469 + m.x322)**2 + (
    -0.033522650784374886 + m.x323)**2 + (-0.5581254938339517 + m.x324)**2 + (
    -0.0912916889874551 + m.x325)**2) + m.x270 - 2 * m.b595 >= -2)
m.e271 = Constraint(expr= -sqrt((-0.17497888842654896 + m.x322)**2 + (
    -0.38968471952782524 + m.x323)**2 + (-0.3152812984667659 + m.x324)**2 + (
    -0.5561379670293034 + m.x325)**2) + m.x271 - 2 * m.b596 >= -2)
m.e272 = Constraint(expr= -sqrt((-0.9831483568003972 + m.x322)**2 + (
    -0.7793186335882816 + m.x323)**2 + (-0.545443726285844 + m.x324)**2 + (
    -0.8394599012498352 + m.x325)**2) + m.x272 - 2 * m.b597 >= -2)
m.e273 = Constraint(expr= -sqrt((-0.16871130717858907 + m.x322)**2 + (
    -0.7158922205435296 + m.x323)**2 + (-0.9716203470560987 + m.x324)**2 + (
    -0.9419601863446189 + m.x325)**2) + m.x273 - 2 * m.b598 >= -2)
m.e274 = Constraint(expr= m.b404 + m.b419 + m.b434 + m.b449 + m.b464 + m.b479
    + m.b494 + m.b509 + m.b524 + m.b539 + m.b554 + m.b569 + m.b584 == 1)
m.e275 = Constraint(expr= m.b405 + m.b420 + m.b435 + m.b450 + m.b465 + m.b480
    + m.b495 + m.b510 + m.b525 + m.b540 + m.b555 + m.b570 + m.b585 == 1)
m.e276 = Constraint(expr= m.b406 + m.b421 + m.b436 + m.b451 + m.b466 + m.b481
    + m.b496 + m.b511 + m.b526 + m.b541 + m.b556 + m.b571 + m.b586 == 1)
m.e277 = Constraint(expr= m.b407 + m.b422 + m.b437 + m.b452 + m.b467 + m.b482
    + m.b497 + m.b512 + m.b527 + m.b542 + m.b557 + m.b572 + m.b587 == 1)
m.e278 = Constraint(expr= m.b408 + m.b423 + m.b438 + m.b453 + m.b468 + m.b483
    + m.b498 + m.b513 + m.b528 + m.b543 + m.b558 + m.b573 + m.b588 == 1)
m.e279 = Constraint(expr= m.b409 + m.b424 + m.b439 + m.b454 + m.b469 + m.b484
    + m.b499 + m.b514 + m.b529 + m.b544 + m.b559 + m.b574 + m.b589 == 1)
m.e280 = Constraint(expr= m.b410 + m.b425 + m.b440 + m.b455 + m.b470 + m.b485
    + m.b500 + m.b515 + m.b530 + m.b545 + m.b560 + m.b575 + m.b590 == 1)
m.e281 = Constraint(expr= m.b411 + m.b426 + m.b441 + m.b456 + m.b471 + m.b486
    + m.b501 + m.b516 + m.b531 + m.b546 + m.b561 + m.b576 + m.b591 == 1)
m.e282 = Constraint(expr= m.b412 + m.b427 + m.b442 + m.b457 + m.b472 + m.b487
    + m.b502 + m.b517 + m.b532 + m.b547 + m.b562 + m.b577 + m.b592 == 1)
m.e283 = Constraint(expr= m.b413 + m.b428 + m.b443 + m.b458 + m.b473 + m.b488
    + m.b503 + m.b518 + m.b533 + m.b548 + m.b563 + m.b578 + m.b593 == 1)
m.e284 = Constraint(expr= m.b414 + m.b429 + m.b444 + m.b459 + m.b474 + m.b489
    + m.b504 + m.b519 + m.b534 + m.b549 + m.b564 + m.b579 + m.b594 == 1)
m.e285 = Constraint(expr= m.b415 + m.b430 + m.b445 + m.b460 + m.b475 + m.b490
    + m.b505 + m.b520 + m.b535 + m.b550 + m.b565 + m.b580 + m.b595 == 1)
m.e286 = Constraint(expr= m.b416 + m.b431 + m.b446 + m.b461 + m.b476 + m.b491
    + m.b506 + m.b521 + m.b536 + m.b551 + m.b566 + m.b581 + m.b596 == 1)
m.e287 = Constraint(expr= m.b417 + m.b432 + m.b447 + m.b462 + m.b477 + m.b492
    + m.b507 + m.b522 + m.b537 + m.b552 + m.b567 + m.b582 + m.b597 == 1)
m.e288 = Constraint(expr= m.b418 + m.b433 + m.b448 + m.b463 + m.b478 + m.b493
    + m.b508 + m.b523 + m.b538 + m.b553 + m.b568 + m.b583 + m.b598 == 1)
m.e289 = Constraint(expr= m.b326 + m.b327 + m.b328 + m.b329 + m.b330 + m.b331
    + m.b332 + m.b333 + m.b334 + m.b335 + m.b336 + m.b337 + m.b404 + m.b405 +
    m.b406 + m.b407 + m.b408 + m.b409 + m.b410 + m.b411 + m.b412 + m.b413 +
    m.b414 + m.b415 + m.b416 + m.b417 + m.b418 == 3)
m.e290 = Constraint(expr= m.b326 + m.b338 + m.b339 + m.b340 + m.b341 + m.b342
    + m.b343 + m.b344 + m.b345 + m.b346 + m.b347 + m.b348 + m.b419 + m.b420 +
    m.b421 + m.b422 + m.b423 + m.b424 + m.b425 + m.b426 + m.b427 + m.b428 +
    m.b429 + m.b430 + m.b431 + m.b432 + m.b433 == 3)
m.e291 = Constraint(expr= m.b327 + m.b338 + m.b349 + m.b350 + m.b351 + m.b352
    + m.b353 + m.b354 + m.b355 + m.b356 + m.b357 + m.b358 + m.b434 + m.b435 +
    m.b436 + m.b437 + m.b438 + m.b439 + m.b440 + m.b441 + m.b442 + m.b443 +
    m.b444 + m.b445 + m.b446 + m.b447 + m.b448 == 3)
m.e292 = Constraint(expr= m.b328 + m.b339 + m.b349 + m.b359 + m.b360 + m.b361
    + m.b362 + m.b363 + m.b364 + m.b365 + m.b366 + m.b367 + m.b449 + m.b450 +
    m.b451 + m.b452 + m.b453 + m.b454 + m.b455 + m.b456 + m.b457 + m.b458 +
    m.b459 + m.b460 + m.b461 + m.b462 + m.b463 == 3)
m.e293 = Constraint(expr= m.b329 + m.b340 + m.b350 + m.b359 + m.b368 + m.b369
    + m.b370 + m.b371 + m.b372 + m.b373 + m.b374 + m.b375 + m.b464 + m.b465 +
    m.b466 + m.b467 + m.b468 + m.b469 + m.b470 + m.b471 + m.b472 + m.b473 +
    m.b474 + m.b475 + m.b476 + m.b477 + m.b478 == 3)
m.e294 = Constraint(expr= m.b330 + m.b341 + m.b351 + m.b360 + m.b368 + m.b376
    + m.b377 + m.b378 + m.b379 + m.b380 + m.b381 + m.b382 + m.b479 + m.b480 +
    m.b481 + m.b482 + m.b483 + m.b484 + m.b485 + m.b486 + m.b487 + m.b488 +
    m.b489 + m.b490 + m.b491 + m.b492 + m.b493 == 3)
m.e295 = Constraint(expr= m.b331 + m.b342 + m.b352 + m.b361 + m.b369 + m.b376
    + m.b383 + m.b384 + m.b385 + m.b386 + m.b387 + m.b388 + m.b494 + m.b495 +
    m.b496 + m.b497 + m.b498 + m.b499 + m.b500 + m.b501 + m.b502 + m.b503 +
    m.b504 + m.b505 + m.b506 + m.b507 + m.b508 == 3)
m.e296 = Constraint(expr= m.b332 + m.b343 + m.b353 + m.b362 + m.b370 + m.b377
    + m.b383 + m.b389 + m.b390 + m.b391 + m.b392 + m.b393 + m.b509 + m.b510 +
    m.b511 + m.b512 + m.b513 + m.b514 + m.b515 + m.b516 + m.b517 + m.b518 +
    m.b519 + m.b520 + m.b521 + m.b522 + m.b523 == 3)
m.e297 = Constraint(expr= m.b333 + m.b344 + m.b354 + m.b363 + m.b371 + m.b378
    + m.b384 + m.b389 + m.b394 + m.b395 + m.b396 + m.b397 + m.b524 + m.b525 +
    m.b526 + m.b527 + m.b528 + m.b529 + m.b530 + m.b531 + m.b532 + m.b533 +
    m.b534 + m.b535 + m.b536 + m.b537 + m.b538 == 3)
m.e298 = Constraint(expr= m.b334 + m.b345 + m.b355 + m.b364 + m.b372 + m.b379
    + m.b385 + m.b390 + m.b394 + m.b398 + m.b399 + m.b400 + m.b539 + m.b540 +
    m.b541 + m.b542 + m.b543 + m.b544 + m.b545 + m.b546 + m.b547 + m.b548 +
    m.b549 + m.b550 + m.b551 + m.b552 + m.b553 == 3)
m.e299 = Constraint(expr= m.b335 + m.b346 + m.b356 + m.b365 + m.b373 + m.b380
    + m.b386 + m.b391 + m.b395 + m.b398 + m.b401 + m.b402 + m.b554 + m.b555 +
    m.b556 + m.b557 + m.b558 + m.b559 + m.b560 + m.b561 + m.b562 + m.b563 +
    m.b564 + m.b565 + m.b566 + m.b567 + m.b568 == 3)
m.e300 = Constraint(expr= m.b336 + m.b347 + m.b357 + m.b366 + m.b374 + m.b381
    + m.b387 + m.b392 + m.b396 + m.b399 + m.b401 + m.b403 + m.b569 + m.b570 +
    m.b571 + m.b572 + m.b573 + m.b574 + m.b575 + m.b576 + m.b577 + m.b578 +
    m.b579 + m.b580 + m.b581 + m.b582 + m.b583 == 3)
m.e301 = Constraint(expr= m.b337 + m.b348 + m.b358 + m.b367 + m.b375 + m.b382
    + m.b388 + m.b393 + m.b397 + m.b400 + m.b402 + m.b403 + m.b584 + m.b585 +
    m.b586 + m.b587 + m.b588 + m.b589 + m.b590 + m.b591 + m.b592 + m.b593 +
    m.b594 + m.b595 + m.b596 + m.b597 + m.b598 == 3)
m.e302 = Constraint(expr= m.b326 == 1)
m.e303 = Constraint(expr= m.b327 + m.b338 == 1)
m.e304 = Constraint(expr= m.b328 + m.b339 + m.b349 == 1)
m.e305 = Constraint(expr= m.b329 + m.b340 + m.b350 + m.b359 == 1)
m.e306 = Constraint(expr= m.b330 + m.b341 + m.b351 + m.b360 + m.b368 == 1)
m.e307 = Constraint(expr= m.b331 + m.b342 + m.b352 + m.b361 + m.b369 + m.b376
    == 1)
m.e308 = Constraint(expr= m.b332 + m.b343 + m.b353 + m.b362 + m.b370 + m.b377
    + m.b383 == 1)
m.e309 = Constraint(expr= m.b333 + m.b344 + m.b354 + m.b363 + m.b371 + m.b378
    + m.b384 + m.b389 == 1)
m.e310 = Constraint(expr= m.b334 + m.b345 + m.b355 + m.b364 + m.b372 + m.b379
    + m.b385 + m.b390 + m.b394 == 1)
m.e311 = Constraint(expr= m.b335 + m.b346 + m.b356 + m.b365 + m.b373 + m.b380
    + m.b386 + m.b391 + m.b395 + m.b398 == 1)
m.e312 = Constraint(expr= m.b336 + m.b347 + m.b357 + m.b366 + m.b374 + m.b381
    + m.b387 + m.b392 + m.b396 + m.b399 + m.b401 == 1)
m.e313 = Constraint(expr= m.b337 + m.b348 + m.b358 + m.b367 + m.b375 + m.b382
    + m.b388 + m.b393 + m.b397 + m.b400 + m.b402 + m.b403 == 1)
