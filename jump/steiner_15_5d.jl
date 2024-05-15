# MINLP written by GAMS Convert at 05/15/24 11:55:03
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       313       40      273        0        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#       611      338      273        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#      2925     1170     1755
#
# Reformulation has removed 1 variable and 1 equation

using JuMP
using MathOptInterface
const MOI = MathOptInterface

model = m = Model()

@variable(m, 0 <= x1 <= 2.23606797749979, start=0)
@variable(m, 0 <= x2 <= 2.23606797749979, start=0)
@variable(m, 0 <= x3 <= 2.23606797749979, start=0)
@variable(m, 0 <= x4 <= 2.23606797749979, start=0)
@variable(m, 0 <= x5 <= 2.23606797749979, start=0)
@variable(m, 0 <= x6 <= 2.23606797749979, start=0)
@variable(m, 0 <= x7 <= 2.23606797749979, start=0)
@variable(m, 0 <= x8 <= 2.23606797749979, start=0)
@variable(m, 0 <= x9 <= 2.23606797749979, start=0)
@variable(m, 0 <= x10 <= 2.23606797749979, start=0)
@variable(m, 0 <= x11 <= 2.23606797749979, start=0)
@variable(m, 0 <= x12 <= 2.23606797749979, start=0)
@variable(m, 0 <= x13 <= 2.23606797749979, start=0)
@variable(m, 0 <= x14 <= 2.23606797749979, start=0)
@variable(m, 0 <= x15 <= 2.23606797749979, start=0)
@variable(m, 0 <= x16 <= 2.23606797749979, start=0)
@variable(m, 0 <= x17 <= 2.23606797749979, start=0)
@variable(m, 0 <= x18 <= 2.23606797749979, start=0)
@variable(m, 0 <= x19 <= 2.23606797749979, start=0)
@variable(m, 0 <= x20 <= 2.23606797749979, start=0)
@variable(m, 0 <= x21 <= 2.23606797749979, start=0)
@variable(m, 0 <= x22 <= 2.23606797749979, start=0)
@variable(m, 0 <= x23 <= 2.23606797749979, start=0)
@variable(m, 0 <= x24 <= 2.23606797749979, start=0)
@variable(m, 0 <= x25 <= 2.23606797749979, start=0)
@variable(m, 0 <= x26 <= 2.23606797749979, start=0)
@variable(m, 0 <= x27 <= 2.23606797749979, start=0)
@variable(m, 0 <= x28 <= 2.23606797749979, start=0)
@variable(m, 0 <= x29 <= 2.23606797749979, start=0)
@variable(m, 0 <= x30 <= 2.23606797749979, start=0)
@variable(m, 0 <= x31 <= 2.23606797749979, start=0)
@variable(m, 0 <= x32 <= 2.23606797749979, start=0)
@variable(m, 0 <= x33 <= 2.23606797749979, start=0)
@variable(m, 0 <= x34 <= 2.23606797749979, start=0)
@variable(m, 0 <= x35 <= 2.23606797749979, start=0)
@variable(m, 0 <= x36 <= 2.23606797749979, start=0)
@variable(m, 0 <= x37 <= 2.23606797749979, start=0)
@variable(m, 0 <= x38 <= 2.23606797749979, start=0)
@variable(m, 0 <= x39 <= 2.23606797749979, start=0)
@variable(m, 0 <= x40 <= 2.23606797749979, start=0)
@variable(m, 0 <= x41 <= 2.23606797749979, start=0)
@variable(m, 0 <= x42 <= 2.23606797749979, start=0)
@variable(m, 0 <= x43 <= 2.23606797749979, start=0)
@variable(m, 0 <= x44 <= 2.23606797749979, start=0)
@variable(m, 0 <= x45 <= 2.23606797749979, start=0)
@variable(m, 0 <= x46 <= 2.23606797749979, start=0)
@variable(m, 0 <= x47 <= 2.23606797749979, start=0)
@variable(m, 0 <= x48 <= 2.23606797749979, start=0)
@variable(m, 0 <= x49 <= 2.23606797749979, start=0)
@variable(m, 0 <= x50 <= 2.23606797749979, start=0)
@variable(m, 0 <= x51 <= 2.23606797749979, start=0)
@variable(m, 0 <= x52 <= 2.23606797749979, start=0)
@variable(m, 0 <= x53 <= 2.23606797749979, start=0)
@variable(m, 0 <= x54 <= 2.23606797749979, start=0)
@variable(m, 0 <= x55 <= 2.23606797749979, start=0)
@variable(m, 0 <= x56 <= 2.23606797749979, start=0)
@variable(m, 0 <= x57 <= 2.23606797749979, start=0)
@variable(m, 0 <= x58 <= 2.23606797749979, start=0)
@variable(m, 0 <= x59 <= 2.23606797749979, start=0)
@variable(m, 0 <= x60 <= 2.23606797749979, start=0)
@variable(m, 0 <= x61 <= 2.23606797749979, start=0)
@variable(m, 0 <= x62 <= 2.23606797749979, start=0)
@variable(m, 0 <= x63 <= 2.23606797749979, start=0)
@variable(m, 0 <= x64 <= 2.23606797749979, start=0)
@variable(m, 0 <= x65 <= 2.23606797749979, start=0)
@variable(m, 0 <= x66 <= 2.23606797749979, start=0)
@variable(m, 0 <= x67 <= 2.23606797749979, start=0)
@variable(m, 0 <= x68 <= 2.23606797749979, start=0)
@variable(m, 0 <= x69 <= 2.23606797749979, start=0)
@variable(m, 0 <= x70 <= 2.23606797749979, start=0)
@variable(m, 0 <= x71 <= 2.23606797749979, start=0)
@variable(m, 0 <= x72 <= 2.23606797749979, start=0)
@variable(m, 0 <= x73 <= 2.23606797749979, start=0)
@variable(m, 0 <= x74 <= 2.23606797749979, start=0)
@variable(m, 0 <= x75 <= 2.23606797749979, start=0)
@variable(m, 0 <= x76 <= 2.23606797749979, start=0)
@variable(m, 0 <= x77 <= 2.23606797749979, start=0)
@variable(m, 0 <= x78 <= 2.23606797749979, start=0)
@variable(m, 0 <= x79 <= 2.23606797749979, start=0)
@variable(m, 0 <= x80 <= 2.23606797749979, start=0)
@variable(m, 0 <= x81 <= 2.23606797749979, start=0)
@variable(m, 0 <= x82 <= 2.23606797749979, start=0)
@variable(m, 0 <= x83 <= 2.23606797749979, start=0)
@variable(m, 0 <= x84 <= 2.23606797749979, start=0)
@variable(m, 0 <= x85 <= 2.23606797749979, start=0)
@variable(m, 0 <= x86 <= 2.23606797749979, start=0)
@variable(m, 0 <= x87 <= 2.23606797749979, start=0)
@variable(m, 0 <= x88 <= 2.23606797749979, start=0)
@variable(m, 0 <= x89 <= 2.23606797749979, start=0)
@variable(m, 0 <= x90 <= 2.23606797749979, start=0)
@variable(m, 0 <= x91 <= 2.23606797749979, start=0)
@variable(m, 0 <= x92 <= 2.23606797749979, start=0)
@variable(m, 0 <= x93 <= 2.23606797749979, start=0)
@variable(m, 0 <= x94 <= 2.23606797749979, start=0)
@variable(m, 0 <= x95 <= 2.23606797749979, start=0)
@variable(m, 0 <= x96 <= 2.23606797749979, start=0)
@variable(m, 0 <= x97 <= 2.23606797749979, start=0)
@variable(m, 0 <= x98 <= 2.23606797749979, start=0)
@variable(m, 0 <= x99 <= 2.23606797749979, start=0)
@variable(m, 0 <= x100 <= 2.23606797749979, start=0)
@variable(m, 0 <= x101 <= 2.23606797749979, start=0)
@variable(m, 0 <= x102 <= 2.23606797749979, start=0)
@variable(m, 0 <= x103 <= 2.23606797749979, start=0)
@variable(m, 0 <= x104 <= 2.23606797749979, start=0)
@variable(m, 0 <= x105 <= 2.23606797749979, start=0)
@variable(m, 0 <= x106 <= 2.23606797749979, start=0)
@variable(m, 0 <= x107 <= 2.23606797749979, start=0)
@variable(m, 0 <= x108 <= 2.23606797749979, start=0)
@variable(m, 0 <= x109 <= 2.23606797749979, start=0)
@variable(m, 0 <= x110 <= 2.23606797749979, start=0)
@variable(m, 0 <= x111 <= 2.23606797749979, start=0)
@variable(m, 0 <= x112 <= 2.23606797749979, start=0)
@variable(m, 0 <= x113 <= 2.23606797749979, start=0)
@variable(m, 0 <= x114 <= 2.23606797749979, start=0)
@variable(m, 0 <= x115 <= 2.23606797749979, start=0)
@variable(m, 0 <= x116 <= 2.23606797749979, start=0)
@variable(m, 0 <= x117 <= 2.23606797749979, start=0)
@variable(m, 0 <= x118 <= 2.23606797749979, start=0)
@variable(m, 0 <= x119 <= 2.23606797749979, start=0)
@variable(m, 0 <= x120 <= 2.23606797749979, start=0)
@variable(m, 0 <= x121 <= 2.23606797749979, start=0)
@variable(m, 0 <= x122 <= 2.23606797749979, start=0)
@variable(m, 0 <= x123 <= 2.23606797749979, start=0)
@variable(m, 0 <= x124 <= 2.23606797749979, start=0)
@variable(m, 0 <= x125 <= 2.23606797749979, start=0)
@variable(m, 0 <= x126 <= 2.23606797749979, start=0)
@variable(m, 0 <= x127 <= 2.23606797749979, start=0)
@variable(m, 0 <= x128 <= 2.23606797749979, start=0)
@variable(m, 0 <= x129 <= 2.23606797749979, start=0)
@variable(m, 0 <= x130 <= 2.23606797749979, start=0)
@variable(m, 0 <= x131 <= 2.23606797749979, start=0)
@variable(m, 0 <= x132 <= 2.23606797749979, start=0)
@variable(m, 0 <= x133 <= 2.23606797749979, start=0)
@variable(m, 0 <= x134 <= 2.23606797749979, start=0)
@variable(m, 0 <= x135 <= 2.23606797749979, start=0)
@variable(m, 0 <= x136 <= 2.23606797749979, start=0)
@variable(m, 0 <= x137 <= 2.23606797749979, start=0)
@variable(m, 0 <= x138 <= 2.23606797749979, start=0)
@variable(m, 0 <= x139 <= 2.23606797749979, start=0)
@variable(m, 0 <= x140 <= 2.23606797749979, start=0)
@variable(m, 0 <= x141 <= 2.23606797749979, start=0)
@variable(m, 0 <= x142 <= 2.23606797749979, start=0)
@variable(m, 0 <= x143 <= 2.23606797749979, start=0)
@variable(m, 0 <= x144 <= 2.23606797749979, start=0)
@variable(m, 0 <= x145 <= 2.23606797749979, start=0)
@variable(m, 0 <= x146 <= 2.23606797749979, start=0)
@variable(m, 0 <= x147 <= 2.23606797749979, start=0)
@variable(m, 0 <= x148 <= 2.23606797749979, start=0)
@variable(m, 0 <= x149 <= 2.23606797749979, start=0)
@variable(m, 0 <= x150 <= 2.23606797749979, start=0)
@variable(m, 0 <= x151 <= 2.23606797749979, start=0)
@variable(m, 0 <= x152 <= 2.23606797749979, start=0)
@variable(m, 0 <= x153 <= 2.23606797749979, start=0)
@variable(m, 0 <= x154 <= 2.23606797749979, start=0)
@variable(m, 0 <= x155 <= 2.23606797749979, start=0)
@variable(m, 0 <= x156 <= 2.23606797749979, start=0)
@variable(m, 0 <= x157 <= 2.23606797749979, start=0)
@variable(m, 0 <= x158 <= 2.23606797749979, start=0)
@variable(m, 0 <= x159 <= 2.23606797749979, start=0)
@variable(m, 0 <= x160 <= 2.23606797749979, start=0)
@variable(m, 0 <= x161 <= 2.23606797749979, start=0)
@variable(m, 0 <= x162 <= 2.23606797749979, start=0)
@variable(m, 0 <= x163 <= 2.23606797749979, start=0)
@variable(m, 0 <= x164 <= 2.23606797749979, start=0)
@variable(m, 0 <= x165 <= 2.23606797749979, start=0)
@variable(m, 0 <= x166 <= 2.23606797749979, start=0)
@variable(m, 0 <= x167 <= 2.23606797749979, start=0)
@variable(m, 0 <= x168 <= 2.23606797749979, start=0)
@variable(m, 0 <= x169 <= 2.23606797749979, start=0)
@variable(m, 0 <= x170 <= 2.23606797749979, start=0)
@variable(m, 0 <= x171 <= 2.23606797749979, start=0)
@variable(m, 0 <= x172 <= 2.23606797749979, start=0)
@variable(m, 0 <= x173 <= 2.23606797749979, start=0)
@variable(m, 0 <= x174 <= 2.23606797749979, start=0)
@variable(m, 0 <= x175 <= 2.23606797749979, start=0)
@variable(m, 0 <= x176 <= 2.23606797749979, start=0)
@variable(m, 0 <= x177 <= 2.23606797749979, start=0)
@variable(m, 0 <= x178 <= 2.23606797749979, start=0)
@variable(m, 0 <= x179 <= 2.23606797749979, start=0)
@variable(m, 0 <= x180 <= 2.23606797749979, start=0)
@variable(m, 0 <= x181 <= 2.23606797749979, start=0)
@variable(m, 0 <= x182 <= 2.23606797749979, start=0)
@variable(m, 0 <= x183 <= 2.23606797749979, start=0)
@variable(m, 0 <= x184 <= 2.23606797749979, start=0)
@variable(m, 0 <= x185 <= 2.23606797749979, start=0)
@variable(m, 0 <= x186 <= 2.23606797749979, start=0)
@variable(m, 0 <= x187 <= 2.23606797749979, start=0)
@variable(m, 0 <= x188 <= 2.23606797749979, start=0)
@variable(m, 0 <= x189 <= 2.23606797749979, start=0)
@variable(m, 0 <= x190 <= 2.23606797749979, start=0)
@variable(m, 0 <= x191 <= 2.23606797749979, start=0)
@variable(m, 0 <= x192 <= 2.23606797749979, start=0)
@variable(m, 0 <= x193 <= 2.23606797749979, start=0)
@variable(m, 0 <= x194 <= 2.23606797749979, start=0)
@variable(m, 0 <= x195 <= 2.23606797749979, start=0)
@variable(m, 0 <= x196 <= 2.23606797749979, start=0)
@variable(m, 0 <= x197 <= 2.23606797749979, start=0)
@variable(m, 0 <= x198 <= 2.23606797749979, start=0)
@variable(m, 0 <= x199 <= 2.23606797749979, start=0)
@variable(m, 0 <= x200 <= 2.23606797749979, start=0)
@variable(m, 0 <= x201 <= 2.23606797749979, start=0)
@variable(m, 0 <= x202 <= 2.23606797749979, start=0)
@variable(m, 0 <= x203 <= 2.23606797749979, start=0)
@variable(m, 0 <= x204 <= 2.23606797749979, start=0)
@variable(m, 0 <= x205 <= 2.23606797749979, start=0)
@variable(m, 0 <= x206 <= 2.23606797749979, start=0)
@variable(m, 0 <= x207 <= 2.23606797749979, start=0)
@variable(m, 0 <= x208 <= 2.23606797749979, start=0)
@variable(m, 0 <= x209 <= 2.23606797749979, start=0)
@variable(m, 0 <= x210 <= 2.23606797749979, start=0)
@variable(m, 0 <= x211 <= 2.23606797749979, start=0)
@variable(m, 0 <= x212 <= 2.23606797749979, start=0)
@variable(m, 0 <= x213 <= 2.23606797749979, start=0)
@variable(m, 0 <= x214 <= 2.23606797749979, start=0)
@variable(m, 0 <= x215 <= 2.23606797749979, start=0)
@variable(m, 0 <= x216 <= 2.23606797749979, start=0)
@variable(m, 0 <= x217 <= 2.23606797749979, start=0)
@variable(m, 0 <= x218 <= 2.23606797749979, start=0)
@variable(m, 0 <= x219 <= 2.23606797749979, start=0)
@variable(m, 0 <= x220 <= 2.23606797749979, start=0)
@variable(m, 0 <= x221 <= 2.23606797749979, start=0)
@variable(m, 0 <= x222 <= 2.23606797749979, start=0)
@variable(m, 0 <= x223 <= 2.23606797749979, start=0)
@variable(m, 0 <= x224 <= 2.23606797749979, start=0)
@variable(m, 0 <= x225 <= 2.23606797749979, start=0)
@variable(m, 0 <= x226 <= 2.23606797749979, start=0)
@variable(m, 0 <= x227 <= 2.23606797749979, start=0)
@variable(m, 0 <= x228 <= 2.23606797749979, start=0)
@variable(m, 0 <= x229 <= 2.23606797749979, start=0)
@variable(m, 0 <= x230 <= 2.23606797749979, start=0)
@variable(m, 0 <= x231 <= 2.23606797749979, start=0)
@variable(m, 0 <= x232 <= 2.23606797749979, start=0)
@variable(m, 0 <= x233 <= 2.23606797749979, start=0)
@variable(m, 0 <= x234 <= 2.23606797749979, start=0)
@variable(m, 0 <= x235 <= 2.23606797749979, start=0)
@variable(m, 0 <= x236 <= 2.23606797749979, start=0)
@variable(m, 0 <= x237 <= 2.23606797749979, start=0)
@variable(m, 0 <= x238 <= 2.23606797749979, start=0)
@variable(m, 0 <= x239 <= 2.23606797749979, start=0)
@variable(m, 0 <= x240 <= 2.23606797749979, start=0)
@variable(m, 0 <= x241 <= 2.23606797749979, start=0)
@variable(m, 0 <= x242 <= 2.23606797749979, start=0)
@variable(m, 0 <= x243 <= 2.23606797749979, start=0)
@variable(m, 0 <= x244 <= 2.23606797749979, start=0)
@variable(m, 0 <= x245 <= 2.23606797749979, start=0)
@variable(m, 0 <= x246 <= 2.23606797749979, start=0)
@variable(m, 0 <= x247 <= 2.23606797749979, start=0)
@variable(m, 0 <= x248 <= 2.23606797749979, start=0)
@variable(m, 0 <= x249 <= 2.23606797749979, start=0)
@variable(m, 0 <= x250 <= 2.23606797749979, start=0)
@variable(m, 0 <= x251 <= 2.23606797749979, start=0)
@variable(m, 0 <= x252 <= 2.23606797749979, start=0)
@variable(m, 0 <= x253 <= 2.23606797749979, start=0)
@variable(m, 0 <= x254 <= 2.23606797749979, start=0)
@variable(m, 0 <= x255 <= 2.23606797749979, start=0)
@variable(m, 0 <= x256 <= 2.23606797749979, start=0)
@variable(m, 0 <= x257 <= 2.23606797749979, start=0)
@variable(m, 0 <= x258 <= 2.23606797749979, start=0)
@variable(m, 0 <= x259 <= 2.23606797749979, start=0)
@variable(m, 0 <= x260 <= 2.23606797749979, start=0)
@variable(m, 0 <= x261 <= 2.23606797749979, start=0)
@variable(m, 0 <= x262 <= 2.23606797749979, start=0)
@variable(m, 0 <= x263 <= 2.23606797749979, start=0)
@variable(m, 0 <= x264 <= 2.23606797749979, start=0)
@variable(m, 0 <= x265 <= 2.23606797749979, start=0)
@variable(m, 0 <= x266 <= 2.23606797749979, start=0)
@variable(m, 0 <= x267 <= 2.23606797749979, start=0)
@variable(m, 0 <= x268 <= 2.23606797749979, start=0)
@variable(m, 0 <= x269 <= 2.23606797749979, start=0)
@variable(m, 0 <= x270 <= 2.23606797749979, start=0)
@variable(m, 0 <= x271 <= 2.23606797749979, start=0)
@variable(m, 0 <= x272 <= 2.23606797749979, start=0)
@variable(m, 0 <= x273 <= 2.23606797749979, start=0)
@variable(m, 0 <= x274 <= 1, start=0)
@variable(m, 0 <= x275 <= 1, start=0)
@variable(m, 0 <= x276 <= 1, start=0)
@variable(m, 0 <= x277 <= 1, start=0)
@variable(m, 0 <= x278 <= 1, start=0)
@variable(m, 0 <= x279 <= 1, start=0)
@variable(m, 0 <= x280 <= 1, start=0)
@variable(m, 0 <= x281 <= 1, start=0)
@variable(m, 0 <= x282 <= 1, start=0)
@variable(m, 0 <= x283 <= 1, start=0)
@variable(m, 0 <= x284 <= 1, start=0)
@variable(m, 0 <= x285 <= 1, start=0)
@variable(m, 0 <= x286 <= 1, start=0)
@variable(m, 0 <= x287 <= 1, start=0)
@variable(m, 0 <= x288 <= 1, start=0)
@variable(m, 0 <= x289 <= 1, start=0)
@variable(m, 0 <= x290 <= 1, start=0)
@variable(m, 0 <= x291 <= 1, start=0)
@variable(m, 0 <= x292 <= 1, start=0)
@variable(m, 0 <= x293 <= 1, start=0)
@variable(m, 0 <= x294 <= 1, start=0)
@variable(m, 0 <= x295 <= 1, start=0)
@variable(m, 0 <= x296 <= 1, start=0)
@variable(m, 0 <= x297 <= 1, start=0)
@variable(m, 0 <= x298 <= 1, start=0)
@variable(m, 0 <= x299 <= 1, start=0)
@variable(m, 0 <= x300 <= 1, start=0)
@variable(m, 0 <= x301 <= 1, start=0)
@variable(m, 0 <= x302 <= 1, start=0)
@variable(m, 0 <= x303 <= 1, start=0)
@variable(m, 0 <= x304 <= 1, start=0)
@variable(m, 0 <= x305 <= 1, start=0)
@variable(m, 0 <= x306 <= 1, start=0)
@variable(m, 0 <= x307 <= 1, start=0)
@variable(m, 0 <= x308 <= 1, start=0)
@variable(m, 0 <= x309 <= 1, start=0)
@variable(m, 0 <= x310 <= 1, start=0)
@variable(m, 0 <= x311 <= 1, start=0)
@variable(m, 0 <= x312 <= 1, start=0)
@variable(m, 0 <= x313 <= 1, start=0)
@variable(m, 0 <= x314 <= 1, start=0)
@variable(m, 0 <= x315 <= 1, start=0)
@variable(m, 0 <= x316 <= 1, start=0)
@variable(m, 0 <= x317 <= 1, start=0)
@variable(m, 0 <= x318 <= 1, start=0)
@variable(m, 0 <= x319 <= 1, start=0)
@variable(m, 0 <= x320 <= 1, start=0)
@variable(m, 0 <= x321 <= 1, start=0)
@variable(m, 0 <= x322 <= 1, start=0)
@variable(m, 0 <= x323 <= 1, start=0)
@variable(m, 0 <= x324 <= 1, start=0)
@variable(m, 0 <= x325 <= 1, start=0)
@variable(m, 0 <= x326 <= 1, start=0)
@variable(m, 0 <= x327 <= 1, start=0)
@variable(m, 0 <= x328 <= 1, start=0)
@variable(m, 0 <= x329 <= 1, start=0)
@variable(m, 0 <= x330 <= 1, start=0)
@variable(m, 0 <= x331 <= 1, start=0)
@variable(m, 0 <= x332 <= 1, start=0)
@variable(m, 0 <= x333 <= 1, start=0)
@variable(m, 0 <= x334 <= 1, start=0)
@variable(m, 0 <= x335 <= 1, start=0)
@variable(m, 0 <= x336 <= 1, start=0)
@variable(m, 0 <= x337 <= 1, start=0)
@variable(m, 0 <= x338 <= 1, start=0)
@variable(m, 0 <= b339 <= 1, binary=true, start=0)
@variable(m, 0 <= b340 <= 1, binary=true, start=0)
@variable(m, 0 <= b341 <= 1, binary=true, start=0)
@variable(m, 0 <= b342 <= 1, binary=true, start=0)
@variable(m, 0 <= b343 <= 1, binary=true, start=0)
@variable(m, 0 <= b344 <= 1, binary=true, start=0)
@variable(m, 0 <= b345 <= 1, binary=true, start=0)
@variable(m, 0 <= b346 <= 1, binary=true, start=0)
@variable(m, 0 <= b347 <= 1, binary=true, start=0)
@variable(m, 0 <= b348 <= 1, binary=true, start=0)
@variable(m, 0 <= b349 <= 1, binary=true, start=0)
@variable(m, 0 <= b350 <= 1, binary=true, start=0)
@variable(m, 0 <= b351 <= 1, binary=true, start=0)
@variable(m, 0 <= b352 <= 1, binary=true, start=0)
@variable(m, 0 <= b353 <= 1, binary=true, start=0)
@variable(m, 0 <= b354 <= 1, binary=true, start=0)
@variable(m, 0 <= b355 <= 1, binary=true, start=0)
@variable(m, 0 <= b356 <= 1, binary=true, start=0)
@variable(m, 0 <= b357 <= 1, binary=true, start=0)
@variable(m, 0 <= b358 <= 1, binary=true, start=0)
@variable(m, 0 <= b359 <= 1, binary=true, start=0)
@variable(m, 0 <= b360 <= 1, binary=true, start=0)
@variable(m, 0 <= b361 <= 1, binary=true, start=0)
@variable(m, 0 <= b362 <= 1, binary=true, start=0)
@variable(m, 0 <= b363 <= 1, binary=true, start=0)
@variable(m, 0 <= b364 <= 1, binary=true, start=0)
@variable(m, 0 <= b365 <= 1, binary=true, start=0)
@variable(m, 0 <= b366 <= 1, binary=true, start=0)
@variable(m, 0 <= b367 <= 1, binary=true, start=0)
@variable(m, 0 <= b368 <= 1, binary=true, start=0)
@variable(m, 0 <= b369 <= 1, binary=true, start=0)
@variable(m, 0 <= b370 <= 1, binary=true, start=0)
@variable(m, 0 <= b371 <= 1, binary=true, start=0)
@variable(m, 0 <= b372 <= 1, binary=true, start=0)
@variable(m, 0 <= b373 <= 1, binary=true, start=0)
@variable(m, 0 <= b374 <= 1, binary=true, start=0)
@variable(m, 0 <= b375 <= 1, binary=true, start=0)
@variable(m, 0 <= b376 <= 1, binary=true, start=0)
@variable(m, 0 <= b377 <= 1, binary=true, start=0)
@variable(m, 0 <= b378 <= 1, binary=true, start=0)
@variable(m, 0 <= b379 <= 1, binary=true, start=0)
@variable(m, 0 <= b380 <= 1, binary=true, start=0)
@variable(m, 0 <= b381 <= 1, binary=true, start=0)
@variable(m, 0 <= b382 <= 1, binary=true, start=0)
@variable(m, 0 <= b383 <= 1, binary=true, start=0)
@variable(m, 0 <= b384 <= 1, binary=true, start=0)
@variable(m, 0 <= b385 <= 1, binary=true, start=0)
@variable(m, 0 <= b386 <= 1, binary=true, start=0)
@variable(m, 0 <= b387 <= 1, binary=true, start=0)
@variable(m, 0 <= b388 <= 1, binary=true, start=0)
@variable(m, 0 <= b389 <= 1, binary=true, start=0)
@variable(m, 0 <= b390 <= 1, binary=true, start=0)
@variable(m, 0 <= b391 <= 1, binary=true, start=0)
@variable(m, 0 <= b392 <= 1, binary=true, start=0)
@variable(m, 0 <= b393 <= 1, binary=true, start=0)
@variable(m, 0 <= b394 <= 1, binary=true, start=0)
@variable(m, 0 <= b395 <= 1, binary=true, start=0)
@variable(m, 0 <= b396 <= 1, binary=true, start=0)
@variable(m, 0 <= b397 <= 1, binary=true, start=0)
@variable(m, 0 <= b398 <= 1, binary=true, start=0)
@variable(m, 0 <= b399 <= 1, binary=true, start=0)
@variable(m, 0 <= b400 <= 1, binary=true, start=0)
@variable(m, 0 <= b401 <= 1, binary=true, start=0)
@variable(m, 0 <= b402 <= 1, binary=true, start=0)
@variable(m, 0 <= b403 <= 1, binary=true, start=0)
@variable(m, 0 <= b404 <= 1, binary=true, start=0)
@variable(m, 0 <= b405 <= 1, binary=true, start=0)
@variable(m, 0 <= b406 <= 1, binary=true, start=0)
@variable(m, 0 <= b407 <= 1, binary=true, start=0)
@variable(m, 0 <= b408 <= 1, binary=true, start=0)
@variable(m, 0 <= b409 <= 1, binary=true, start=0)
@variable(m, 0 <= b410 <= 1, binary=true, start=0)
@variable(m, 0 <= b411 <= 1, binary=true, start=0)
@variable(m, 0 <= b412 <= 1, binary=true, start=0)
@variable(m, 0 <= b413 <= 1, binary=true, start=0)
@variable(m, 0 <= b414 <= 1, binary=true, start=0)
@variable(m, 0 <= b415 <= 1, binary=true, start=0)
@variable(m, 0 <= b416 <= 1, binary=true, start=0)
@variable(m, 0 <= b417 <= 1, binary=true, start=0)
@variable(m, 0 <= b418 <= 1, binary=true, start=0)
@variable(m, 0 <= b419 <= 1, binary=true, start=0)
@variable(m, 0 <= b420 <= 1, binary=true, start=0)
@variable(m, 0 <= b421 <= 1, binary=true, start=0)
@variable(m, 0 <= b422 <= 1, binary=true, start=0)
@variable(m, 0 <= b423 <= 1, binary=true, start=0)
@variable(m, 0 <= b424 <= 1, binary=true, start=0)
@variable(m, 0 <= b425 <= 1, binary=true, start=0)
@variable(m, 0 <= b426 <= 1, binary=true, start=0)
@variable(m, 0 <= b427 <= 1, binary=true, start=0)
@variable(m, 0 <= b428 <= 1, binary=true, start=0)
@variable(m, 0 <= b429 <= 1, binary=true, start=0)
@variable(m, 0 <= b430 <= 1, binary=true, start=0)
@variable(m, 0 <= b431 <= 1, binary=true, start=0)
@variable(m, 0 <= b432 <= 1, binary=true, start=0)
@variable(m, 0 <= b433 <= 1, binary=true, start=0)
@variable(m, 0 <= b434 <= 1, binary=true, start=0)
@variable(m, 0 <= b435 <= 1, binary=true, start=0)
@variable(m, 0 <= b436 <= 1, binary=true, start=0)
@variable(m, 0 <= b437 <= 1, binary=true, start=0)
@variable(m, 0 <= b438 <= 1, binary=true, start=0)
@variable(m, 0 <= b439 <= 1, binary=true, start=0)
@variable(m, 0 <= b440 <= 1, binary=true, start=0)
@variable(m, 0 <= b441 <= 1, binary=true, start=0)
@variable(m, 0 <= b442 <= 1, binary=true, start=0)
@variable(m, 0 <= b443 <= 1, binary=true, start=0)
@variable(m, 0 <= b444 <= 1, binary=true, start=0)
@variable(m, 0 <= b445 <= 1, binary=true, start=0)
@variable(m, 0 <= b446 <= 1, binary=true, start=0)
@variable(m, 0 <= b447 <= 1, binary=true, start=0)
@variable(m, 0 <= b448 <= 1, binary=true, start=0)
@variable(m, 0 <= b449 <= 1, binary=true, start=0)
@variable(m, 0 <= b450 <= 1, binary=true, start=0)
@variable(m, 0 <= b451 <= 1, binary=true, start=0)
@variable(m, 0 <= b452 <= 1, binary=true, start=0)
@variable(m, 0 <= b453 <= 1, binary=true, start=0)
@variable(m, 0 <= b454 <= 1, binary=true, start=0)
@variable(m, 0 <= b455 <= 1, binary=true, start=0)
@variable(m, 0 <= b456 <= 1, binary=true, start=0)
@variable(m, 0 <= b457 <= 1, binary=true, start=0)
@variable(m, 0 <= b458 <= 1, binary=true, start=0)
@variable(m, 0 <= b459 <= 1, binary=true, start=0)
@variable(m, 0 <= b460 <= 1, binary=true, start=0)
@variable(m, 0 <= b461 <= 1, binary=true, start=0)
@variable(m, 0 <= b462 <= 1, binary=true, start=0)
@variable(m, 0 <= b463 <= 1, binary=true, start=0)
@variable(m, 0 <= b464 <= 1, binary=true, start=0)
@variable(m, 0 <= b465 <= 1, binary=true, start=0)
@variable(m, 0 <= b466 <= 1, binary=true, start=0)
@variable(m, 0 <= b467 <= 1, binary=true, start=0)
@variable(m, 0 <= b468 <= 1, binary=true, start=0)
@variable(m, 0 <= b469 <= 1, binary=true, start=0)
@variable(m, 0 <= b470 <= 1, binary=true, start=0)
@variable(m, 0 <= b471 <= 1, binary=true, start=0)
@variable(m, 0 <= b472 <= 1, binary=true, start=0)
@variable(m, 0 <= b473 <= 1, binary=true, start=0)
@variable(m, 0 <= b474 <= 1, binary=true, start=0)
@variable(m, 0 <= b475 <= 1, binary=true, start=0)
@variable(m, 0 <= b476 <= 1, binary=true, start=0)
@variable(m, 0 <= b477 <= 1, binary=true, start=0)
@variable(m, 0 <= b478 <= 1, binary=true, start=0)
@variable(m, 0 <= b479 <= 1, binary=true, start=0)
@variable(m, 0 <= b480 <= 1, binary=true, start=0)
@variable(m, 0 <= b481 <= 1, binary=true, start=0)
@variable(m, 0 <= b482 <= 1, binary=true, start=0)
@variable(m, 0 <= b483 <= 1, binary=true, start=0)
@variable(m, 0 <= b484 <= 1, binary=true, start=0)
@variable(m, 0 <= b485 <= 1, binary=true, start=0)
@variable(m, 0 <= b486 <= 1, binary=true, start=0)
@variable(m, 0 <= b487 <= 1, binary=true, start=0)
@variable(m, 0 <= b488 <= 1, binary=true, start=0)
@variable(m, 0 <= b489 <= 1, binary=true, start=0)
@variable(m, 0 <= b490 <= 1, binary=true, start=0)
@variable(m, 0 <= b491 <= 1, binary=true, start=0)
@variable(m, 0 <= b492 <= 1, binary=true, start=0)
@variable(m, 0 <= b493 <= 1, binary=true, start=0)
@variable(m, 0 <= b494 <= 1, binary=true, start=0)
@variable(m, 0 <= b495 <= 1, binary=true, start=0)
@variable(m, 0 <= b496 <= 1, binary=true, start=0)
@variable(m, 0 <= b497 <= 1, binary=true, start=0)
@variable(m, 0 <= b498 <= 1, binary=true, start=0)
@variable(m, 0 <= b499 <= 1, binary=true, start=0)
@variable(m, 0 <= b500 <= 1, binary=true, start=0)
@variable(m, 0 <= b501 <= 1, binary=true, start=0)
@variable(m, 0 <= b502 <= 1, binary=true, start=0)
@variable(m, 0 <= b503 <= 1, binary=true, start=0)
@variable(m, 0 <= b504 <= 1, binary=true, start=0)
@variable(m, 0 <= b505 <= 1, binary=true, start=0)
@variable(m, 0 <= b506 <= 1, binary=true, start=0)
@variable(m, 0 <= b507 <= 1, binary=true, start=0)
@variable(m, 0 <= b508 <= 1, binary=true, start=0)
@variable(m, 0 <= b509 <= 1, binary=true, start=0)
@variable(m, 0 <= b510 <= 1, binary=true, start=0)
@variable(m, 0 <= b511 <= 1, binary=true, start=0)
@variable(m, 0 <= b512 <= 1, binary=true, start=0)
@variable(m, 0 <= b513 <= 1, binary=true, start=0)
@variable(m, 0 <= b514 <= 1, binary=true, start=0)
@variable(m, 0 <= b515 <= 1, binary=true, start=0)
@variable(m, 0 <= b516 <= 1, binary=true, start=0)
@variable(m, 0 <= b517 <= 1, binary=true, start=0)
@variable(m, 0 <= b518 <= 1, binary=true, start=0)
@variable(m, 0 <= b519 <= 1, binary=true, start=0)
@variable(m, 0 <= b520 <= 1, binary=true, start=0)
@variable(m, 0 <= b521 <= 1, binary=true, start=0)
@variable(m, 0 <= b522 <= 1, binary=true, start=0)
@variable(m, 0 <= b523 <= 1, binary=true, start=0)
@variable(m, 0 <= b524 <= 1, binary=true, start=0)
@variable(m, 0 <= b525 <= 1, binary=true, start=0)
@variable(m, 0 <= b526 <= 1, binary=true, start=0)
@variable(m, 0 <= b527 <= 1, binary=true, start=0)
@variable(m, 0 <= b528 <= 1, binary=true, start=0)
@variable(m, 0 <= b529 <= 1, binary=true, start=0)
@variable(m, 0 <= b530 <= 1, binary=true, start=0)
@variable(m, 0 <= b531 <= 1, binary=true, start=0)
@variable(m, 0 <= b532 <= 1, binary=true, start=0)
@variable(m, 0 <= b533 <= 1, binary=true, start=0)
@variable(m, 0 <= b534 <= 1, binary=true, start=0)
@variable(m, 0 <= b535 <= 1, binary=true, start=0)
@variable(m, 0 <= b536 <= 1, binary=true, start=0)
@variable(m, 0 <= b537 <= 1, binary=true, start=0)
@variable(m, 0 <= b538 <= 1, binary=true, start=0)
@variable(m, 0 <= b539 <= 1, binary=true, start=0)
@variable(m, 0 <= b540 <= 1, binary=true, start=0)
@variable(m, 0 <= b541 <= 1, binary=true, start=0)
@variable(m, 0 <= b542 <= 1, binary=true, start=0)
@variable(m, 0 <= b543 <= 1, binary=true, start=0)
@variable(m, 0 <= b544 <= 1, binary=true, start=0)
@variable(m, 0 <= b545 <= 1, binary=true, start=0)
@variable(m, 0 <= b546 <= 1, binary=true, start=0)
@variable(m, 0 <= b547 <= 1, binary=true, start=0)
@variable(m, 0 <= b548 <= 1, binary=true, start=0)
@variable(m, 0 <= b549 <= 1, binary=true, start=0)
@variable(m, 0 <= b550 <= 1, binary=true, start=0)
@variable(m, 0 <= b551 <= 1, binary=true, start=0)
@variable(m, 0 <= b552 <= 1, binary=true, start=0)
@variable(m, 0 <= b553 <= 1, binary=true, start=0)
@variable(m, 0 <= b554 <= 1, binary=true, start=0)
@variable(m, 0 <= b555 <= 1, binary=true, start=0)
@variable(m, 0 <= b556 <= 1, binary=true, start=0)
@variable(m, 0 <= b557 <= 1, binary=true, start=0)
@variable(m, 0 <= b558 <= 1, binary=true, start=0)
@variable(m, 0 <= b559 <= 1, binary=true, start=0)
@variable(m, 0 <= b560 <= 1, binary=true, start=0)
@variable(m, 0 <= b561 <= 1, binary=true, start=0)
@variable(m, 0 <= b562 <= 1, binary=true, start=0)
@variable(m, 0 <= b563 <= 1, binary=true, start=0)
@variable(m, 0 <= b564 <= 1, binary=true, start=0)
@variable(m, 0 <= b565 <= 1, binary=true, start=0)
@variable(m, 0 <= b566 <= 1, binary=true, start=0)
@variable(m, 0 <= b567 <= 1, binary=true, start=0)
@variable(m, 0 <= b568 <= 1, binary=true, start=0)
@variable(m, 0 <= b569 <= 1, binary=true, start=0)
@variable(m, 0 <= b570 <= 1, binary=true, start=0)
@variable(m, 0 <= b571 <= 1, binary=true, start=0)
@variable(m, 0 <= b572 <= 1, binary=true, start=0)
@variable(m, 0 <= b573 <= 1, binary=true, start=0)
@variable(m, 0 <= b574 <= 1, binary=true, start=0)
@variable(m, 0 <= b575 <= 1, binary=true, start=0)
@variable(m, 0 <= b576 <= 1, binary=true, start=0)
@variable(m, 0 <= b577 <= 1, binary=true, start=0)
@variable(m, 0 <= b578 <= 1, binary=true, start=0)
@variable(m, 0 <= b579 <= 1, binary=true, start=0)
@variable(m, 0 <= b580 <= 1, binary=true, start=0)
@variable(m, 0 <= b581 <= 1, binary=true, start=0)
@variable(m, 0 <= b582 <= 1, binary=true, start=0)
@variable(m, 0 <= b583 <= 1, binary=true, start=0)
@variable(m, 0 <= b584 <= 1, binary=true, start=0)
@variable(m, 0 <= b585 <= 1, binary=true, start=0)
@variable(m, 0 <= b586 <= 1, binary=true, start=0)
@variable(m, 0 <= b587 <= 1, binary=true, start=0)
@variable(m, 0 <= b588 <= 1, binary=true, start=0)
@variable(m, 0 <= b589 <= 1, binary=true, start=0)
@variable(m, 0 <= b590 <= 1, binary=true, start=0)
@variable(m, 0 <= b591 <= 1, binary=true, start=0)
@variable(m, 0 <= b592 <= 1, binary=true, start=0)
@variable(m, 0 <= b593 <= 1, binary=true, start=0)
@variable(m, 0 <= b594 <= 1, binary=true, start=0)
@variable(m, 0 <= b595 <= 1, binary=true, start=0)
@variable(m, 0 <= b596 <= 1, binary=true, start=0)
@variable(m, 0 <= b597 <= 1, binary=true, start=0)
@variable(m, 0 <= b598 <= 1, binary=true, start=0)
@variable(m, 0 <= b599 <= 1, binary=true, start=0)
@variable(m, 0 <= b600 <= 1, binary=true, start=0)
@variable(m, 0 <= b601 <= 1, binary=true, start=0)
@variable(m, 0 <= b602 <= 1, binary=true, start=0)
@variable(m, 0 <= b603 <= 1, binary=true, start=0)
@variable(m, 0 <= b604 <= 1, binary=true, start=0)
@variable(m, 0 <= b605 <= 1, binary=true, start=0)
@variable(m, 0 <= b606 <= 1, binary=true, start=0)
@variable(m, 0 <= b607 <= 1, binary=true, start=0)
@variable(m, 0 <= b608 <= 1, binary=true, start=0)
@variable(m, 0 <= b609 <= 1, binary=true, start=0)
@variable(m, 0 <= b610 <= 1, binary=true, start=0)
@variable(m, 0 <= b611 <= 1, binary=true, start=0)

@objective(m, Min, x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x10 + x11 + x12
    + x13 + x14 + x15 + x16 + x17 + x18 + x19 + x20 + x21 + x22 + x23 + x24 +
    x25 + x26 + x27 + x28 + x29 + x30 + x31 + x32 + x33 + x34 + x35 + x36 + x37
    + x38 + x39 + x40 + x41 + x42 + x43 + x44 + x45 + x46 + x47 + x48 + x49 +
    x50 + x51 + x52 + x53 + x54 + x55 + x56 + x57 + x58 + x59 + x60 + x61 + x62
    + x63 + x64 + x65 + x66 + x67 + x68 + x69 + x70 + x71 + x72 + x73 + x74 +
    x75 + x76 + x77 + x78 + x79 + x80 + x81 + x82 + x83 + x84 + x85 + x86 + x87
    + x88 + x89 + x90 + x91 + x92 + x93 + x94 + x95 + x96 + x97 + x98 + x99 +
    x100 + x101 + x102 + x103 + x104 + x105 + x106 + x107 + x108 + x109 + x110
    + x111 + x112 + x113 + x114 + x115 + x116 + x117 + x118 + x119 + x120 +
    x121 + x122 + x123 + x124 + x125 + x126 + x127 + x128 + x129 + x130 + x131
    + x132 + x133 + x134 + x135 + x136 + x137 + x138 + x139 + x140 + x141 +
    x142 + x143 + x144 + x145 + x146 + x147 + x148 + x149 + x150 + x151 + x152
    + x153 + x154 + x155 + x156 + x157 + x158 + x159 + x160 + x161 + x162 +
    x163 + x164 + x165 + x166 + x167 + x168 + x169 + x170 + x171 + x172 + x173
    + x174 + x175 + x176 + x177 + x178 + x179 + x180 + x181 + x182 + x183 +
    x184 + x185 + x186 + x187 + x188 + x189 + x190 + x191 + x192 + x193 + x194
    + x195 + x196 + x197 + x198 + x199 + x200 + x201 + x202 + x203 + x204 +
    x205 + x206 + x207 + x208 + x209 + x210 + x211 + x212 + x213 + x214 + x215
    + x216 + x217 + x218 + x219 + x220 + x221 + x222 + x223 + x224 + x225 +
    x226 + x227 + x228 + x229 + x230 + x231 + x232 + x233 + x234 + x235 + x236
    + x237 + x238 + x239 + x240 + x241 + x242 + x243 + x244 + x245 + x246 +
    x247 + x248 + x249 + x250 + x251 + x252 + x253 + x254 + x255 + x256 + x257
    + x258 + x259 + x260 + x261 + x262 + x263 + x264 + x265 + x266 + x267 +
    x268 + x269 + x270 + x271 + x272 + x273)

@NLconstraint(m, e1, -sqrt((x274 - x279)^2 + (x275 - x280)^2 + (x276 - x281)^2
    + (x277 - x282)^2 + (x278 - x283)^2) + x1 - 2.23606797749979 * b339
    >= -2.23606797749979)
@NLconstraint(m, e2, -sqrt((x274 - x284)^2 + (x275 - x285)^2 + (x276 - x286)^2
    + (x277 - x287)^2 + (x278 - x288)^2) + x2 - 2.23606797749979 * b340
    >= -2.23606797749979)
@NLconstraint(m, e3, -sqrt((x274 - x289)^2 + (x275 - x290)^2 + (x276 - x291)^2
    + (x277 - x292)^2 + (x278 - x293)^2) + x3 - 2.23606797749979 * b341
    >= -2.23606797749979)
@NLconstraint(m, e4, -sqrt((x274 - x294)^2 + (x275 - x295)^2 + (x276 - x296)^2
    + (x277 - x297)^2 + (x278 - x298)^2) + x4 - 2.23606797749979 * b342
    >= -2.23606797749979)
@NLconstraint(m, e5, -sqrt((x274 - x299)^2 + (x275 - x300)^2 + (x276 - x301)^2
    + (x277 - x302)^2 + (x278 - x303)^2) + x5 - 2.23606797749979 * b343
    >= -2.23606797749979)
@NLconstraint(m, e6, -sqrt((x274 - x304)^2 + (x275 - x305)^2 + (x276 - x306)^2
    + (x277 - x307)^2 + (x278 - x308)^2) + x6 - 2.23606797749979 * b344
    >= -2.23606797749979)
@NLconstraint(m, e7, -sqrt((x274 - x309)^2 + (x275 - x310)^2 + (x276 - x311)^2
    + (x277 - x312)^2 + (x278 - x313)^2) + x7 - 2.23606797749979 * b345
    >= -2.23606797749979)
@NLconstraint(m, e8, -sqrt((x274 - x314)^2 + (x275 - x315)^2 + (x276 - x316)^2
    + (x277 - x317)^2 + (x278 - x318)^2) + x8 - 2.23606797749979 * b346
    >= -2.23606797749979)
@NLconstraint(m, e9, -sqrt((x274 - x319)^2 + (x275 - x320)^2 + (x276 - x321)^2
    + (x277 - x322)^2 + (x278 - x323)^2) + x9 - 2.23606797749979 * b347
    >= -2.23606797749979)
@NLconstraint(m, e10, -sqrt((x274 - x324)^2 + (x275 - x325)^2 + (x276 - x326)^2
    + (x277 - x327)^2 + (x278 - x328)^2) + x10 - 2.23606797749979 * b348
    >= -2.23606797749979)
@NLconstraint(m, e11, -sqrt((x274 - x329)^2 + (x275 - x330)^2 + (x276 - x331)^2
    + (x277 - x332)^2 + (x278 - x333)^2) + x11 - 2.23606797749979 * b349
    >= -2.23606797749979)
@NLconstraint(m, e12, -sqrt((x274 - x334)^2 + (x275 - x335)^2 + (x276 - x336)^2
    + (x277 - x337)^2 + (x278 - x338)^2) + x12 - 2.23606797749979 * b350
    >= -2.23606797749979)
@NLconstraint(m, e13, -sqrt((x279 - x284)^2 + (x280 - x285)^2 + (x281 - x286)^2
    + (x282 - x287)^2 + (x283 - x288)^2) + x13 - 2.23606797749979 * b351
    >= -2.23606797749979)
@NLconstraint(m, e14, -sqrt((x279 - x289)^2 + (x280 - x290)^2 + (x281 - x291)^2
    + (x282 - x292)^2 + (x283 - x293)^2) + x14 - 2.23606797749979 * b352
    >= -2.23606797749979)
@NLconstraint(m, e15, -sqrt((x279 - x294)^2 + (x280 - x295)^2 + (x281 - x296)^2
    + (x282 - x297)^2 + (x283 - x298)^2) + x15 - 2.23606797749979 * b353
    >= -2.23606797749979)
@NLconstraint(m, e16, -sqrt((x279 - x299)^2 + (x280 - x300)^2 + (x281 - x301)^2
    + (x282 - x302)^2 + (x283 - x303)^2) + x16 - 2.23606797749979 * b354
    >= -2.23606797749979)
@NLconstraint(m, e17, -sqrt((x279 - x304)^2 + (x280 - x305)^2 + (x281 - x306)^2
    + (x282 - x307)^2 + (x283 - x308)^2) + x17 - 2.23606797749979 * b355
    >= -2.23606797749979)
@NLconstraint(m, e18, -sqrt((x279 - x309)^2 + (x280 - x310)^2 + (x281 - x311)^2
    + (x282 - x312)^2 + (x283 - x313)^2) + x18 - 2.23606797749979 * b356
    >= -2.23606797749979)
@NLconstraint(m, e19, -sqrt((x279 - x314)^2 + (x280 - x315)^2 + (x281 - x316)^2
    + (x282 - x317)^2 + (x283 - x318)^2) + x19 - 2.23606797749979 * b357
    >= -2.23606797749979)
@NLconstraint(m, e20, -sqrt((x279 - x319)^2 + (x280 - x320)^2 + (x281 - x321)^2
    + (x282 - x322)^2 + (x283 - x323)^2) + x20 - 2.23606797749979 * b358
    >= -2.23606797749979)
@NLconstraint(m, e21, -sqrt((x279 - x324)^2 + (x280 - x325)^2 + (x281 - x326)^2
    + (x282 - x327)^2 + (x283 - x328)^2) + x21 - 2.23606797749979 * b359
    >= -2.23606797749979)
@NLconstraint(m, e22, -sqrt((x279 - x329)^2 + (x280 - x330)^2 + (x281 - x331)^2
    + (x282 - x332)^2 + (x283 - x333)^2) + x22 - 2.23606797749979 * b360
    >= -2.23606797749979)
@NLconstraint(m, e23, -sqrt((x279 - x334)^2 + (x280 - x335)^2 + (x281 - x336)^2
    + (x282 - x337)^2 + (x283 - x338)^2) + x23 - 2.23606797749979 * b361
    >= -2.23606797749979)
@NLconstraint(m, e24, -sqrt((x284 - x289)^2 + (x285 - x290)^2 + (x286 - x291)^2
    + (x287 - x292)^2 + (x288 - x293)^2) + x24 - 2.23606797749979 * b362
    >= -2.23606797749979)
@NLconstraint(m, e25, -sqrt((x284 - x294)^2 + (x285 - x295)^2 + (x286 - x296)^2
    + (x287 - x297)^2 + (x288 - x298)^2) + x25 - 2.23606797749979 * b363
    >= -2.23606797749979)
@NLconstraint(m, e26, -sqrt((x284 - x299)^2 + (x285 - x300)^2 + (x286 - x301)^2
    + (x287 - x302)^2 + (x288 - x303)^2) + x26 - 2.23606797749979 * b364
    >= -2.23606797749979)
@NLconstraint(m, e27, -sqrt((x284 - x304)^2 + (x285 - x305)^2 + (x286 - x306)^2
    + (x287 - x307)^2 + (x288 - x308)^2) + x27 - 2.23606797749979 * b365
    >= -2.23606797749979)
@NLconstraint(m, e28, -sqrt((x284 - x309)^2 + (x285 - x310)^2 + (x286 - x311)^2
    + (x287 - x312)^2 + (x288 - x313)^2) + x28 - 2.23606797749979 * b366
    >= -2.23606797749979)
@NLconstraint(m, e29, -sqrt((x284 - x314)^2 + (x285 - x315)^2 + (x286 - x316)^2
    + (x287 - x317)^2 + (x288 - x318)^2) + x29 - 2.23606797749979 * b367
    >= -2.23606797749979)
@NLconstraint(m, e30, -sqrt((x284 - x319)^2 + (x285 - x320)^2 + (x286 - x321)^2
    + (x287 - x322)^2 + (x288 - x323)^2) + x30 - 2.23606797749979 * b368
    >= -2.23606797749979)
@NLconstraint(m, e31, -sqrt((x284 - x324)^2 + (x285 - x325)^2 + (x286 - x326)^2
    + (x287 - x327)^2 + (x288 - x328)^2) + x31 - 2.23606797749979 * b369
    >= -2.23606797749979)
@NLconstraint(m, e32, -sqrt((x284 - x329)^2 + (x285 - x330)^2 + (x286 - x331)^2
    + (x287 - x332)^2 + (x288 - x333)^2) + x32 - 2.23606797749979 * b370
    >= -2.23606797749979)
@NLconstraint(m, e33, -sqrt((x284 - x334)^2 + (x285 - x335)^2 + (x286 - x336)^2
    + (x287 - x337)^2 + (x288 - x338)^2) + x33 - 2.23606797749979 * b371
    >= -2.23606797749979)
@NLconstraint(m, e34, -sqrt((x289 - x294)^2 + (x290 - x295)^2 + (x291 - x296)^2
    + (x292 - x297)^2 + (x293 - x298)^2) + x34 - 2.23606797749979 * b372
    >= -2.23606797749979)
@NLconstraint(m, e35, -sqrt((x289 - x299)^2 + (x290 - x300)^2 + (x291 - x301)^2
    + (x292 - x302)^2 + (x293 - x303)^2) + x35 - 2.23606797749979 * b373
    >= -2.23606797749979)
@NLconstraint(m, e36, -sqrt((x289 - x304)^2 + (x290 - x305)^2 + (x291 - x306)^2
    + (x292 - x307)^2 + (x293 - x308)^2) + x36 - 2.23606797749979 * b374
    >= -2.23606797749979)
@NLconstraint(m, e37, -sqrt((x289 - x309)^2 + (x290 - x310)^2 + (x291 - x311)^2
    + (x292 - x312)^2 + (x293 - x313)^2) + x37 - 2.23606797749979 * b375
    >= -2.23606797749979)
@NLconstraint(m, e38, -sqrt((x289 - x314)^2 + (x290 - x315)^2 + (x291 - x316)^2
    + (x292 - x317)^2 + (x293 - x318)^2) + x38 - 2.23606797749979 * b376
    >= -2.23606797749979)
@NLconstraint(m, e39, -sqrt((x289 - x319)^2 + (x290 - x320)^2 + (x291 - x321)^2
    + (x292 - x322)^2 + (x293 - x323)^2) + x39 - 2.23606797749979 * b377
    >= -2.23606797749979)
@NLconstraint(m, e40, -sqrt((x289 - x324)^2 + (x290 - x325)^2 + (x291 - x326)^2
    + (x292 - x327)^2 + (x293 - x328)^2) + x40 - 2.23606797749979 * b378
    >= -2.23606797749979)
@NLconstraint(m, e41, -sqrt((x289 - x329)^2 + (x290 - x330)^2 + (x291 - x331)^2
    + (x292 - x332)^2 + (x293 - x333)^2) + x41 - 2.23606797749979 * b379
    >= -2.23606797749979)
@NLconstraint(m, e42, -sqrt((x289 - x334)^2 + (x290 - x335)^2 + (x291 - x336)^2
    + (x292 - x337)^2 + (x293 - x338)^2) + x42 - 2.23606797749979 * b380
    >= -2.23606797749979)
@NLconstraint(m, e43, -sqrt((x294 - x299)^2 + (x295 - x300)^2 + (x296 - x301)^2
    + (x297 - x302)^2 + (x298 - x303)^2) + x43 - 2.23606797749979 * b381
    >= -2.23606797749979)
@NLconstraint(m, e44, -sqrt((x294 - x304)^2 + (x295 - x305)^2 + (x296 - x306)^2
    + (x297 - x307)^2 + (x298 - x308)^2) + x44 - 2.23606797749979 * b382
    >= -2.23606797749979)
@NLconstraint(m, e45, -sqrt((x294 - x309)^2 + (x295 - x310)^2 + (x296 - x311)^2
    + (x297 - x312)^2 + (x298 - x313)^2) + x45 - 2.23606797749979 * b383
    >= -2.23606797749979)
@NLconstraint(m, e46, -sqrt((x294 - x314)^2 + (x295 - x315)^2 + (x296 - x316)^2
    + (x297 - x317)^2 + (x298 - x318)^2) + x46 - 2.23606797749979 * b384
    >= -2.23606797749979)
@NLconstraint(m, e47, -sqrt((x294 - x319)^2 + (x295 - x320)^2 + (x296 - x321)^2
    + (x297 - x322)^2 + (x298 - x323)^2) + x47 - 2.23606797749979 * b385
    >= -2.23606797749979)
@NLconstraint(m, e48, -sqrt((x294 - x324)^2 + (x295 - x325)^2 + (x296 - x326)^2
    + (x297 - x327)^2 + (x298 - x328)^2) + x48 - 2.23606797749979 * b386
    >= -2.23606797749979)
@NLconstraint(m, e49, -sqrt((x294 - x329)^2 + (x295 - x330)^2 + (x296 - x331)^2
    + (x297 - x332)^2 + (x298 - x333)^2) + x49 - 2.23606797749979 * b387
    >= -2.23606797749979)
@NLconstraint(m, e50, -sqrt((x294 - x334)^2 + (x295 - x335)^2 + (x296 - x336)^2
    + (x297 - x337)^2 + (x298 - x338)^2) + x50 - 2.23606797749979 * b388
    >= -2.23606797749979)
@NLconstraint(m, e51, -sqrt((x299 - x304)^2 + (x300 - x305)^2 + (x301 - x306)^2
    + (x302 - x307)^2 + (x303 - x308)^2) + x51 - 2.23606797749979 * b389
    >= -2.23606797749979)
@NLconstraint(m, e52, -sqrt((x299 - x309)^2 + (x300 - x310)^2 + (x301 - x311)^2
    + (x302 - x312)^2 + (x303 - x313)^2) + x52 - 2.23606797749979 * b390
    >= -2.23606797749979)
@NLconstraint(m, e53, -sqrt((x299 - x314)^2 + (x300 - x315)^2 + (x301 - x316)^2
    + (x302 - x317)^2 + (x303 - x318)^2) + x53 - 2.23606797749979 * b391
    >= -2.23606797749979)
@NLconstraint(m, e54, -sqrt((x299 - x319)^2 + (x300 - x320)^2 + (x301 - x321)^2
    + (x302 - x322)^2 + (x303 - x323)^2) + x54 - 2.23606797749979 * b392
    >= -2.23606797749979)
@NLconstraint(m, e55, -sqrt((x299 - x324)^2 + (x300 - x325)^2 + (x301 - x326)^2
    + (x302 - x327)^2 + (x303 - x328)^2) + x55 - 2.23606797749979 * b393
    >= -2.23606797749979)
@NLconstraint(m, e56, -sqrt((x299 - x329)^2 + (x300 - x330)^2 + (x301 - x331)^2
    + (x302 - x332)^2 + (x303 - x333)^2) + x56 - 2.23606797749979 * b394
    >= -2.23606797749979)
@NLconstraint(m, e57, -sqrt((x299 - x334)^2 + (x300 - x335)^2 + (x301 - x336)^2
    + (x302 - x337)^2 + (x303 - x338)^2) + x57 - 2.23606797749979 * b395
    >= -2.23606797749979)
@NLconstraint(m, e58, -sqrt((x304 - x309)^2 + (x305 - x310)^2 + (x306 - x311)^2
    + (x307 - x312)^2 + (x308 - x313)^2) + x58 - 2.23606797749979 * b396
    >= -2.23606797749979)
@NLconstraint(m, e59, -sqrt((x304 - x314)^2 + (x305 - x315)^2 + (x306 - x316)^2
    + (x307 - x317)^2 + (x308 - x318)^2) + x59 - 2.23606797749979 * b397
    >= -2.23606797749979)
@NLconstraint(m, e60, -sqrt((x304 - x319)^2 + (x305 - x320)^2 + (x306 - x321)^2
    + (x307 - x322)^2 + (x308 - x323)^2) + x60 - 2.23606797749979 * b398
    >= -2.23606797749979)
@NLconstraint(m, e61, -sqrt((x304 - x324)^2 + (x305 - x325)^2 + (x306 - x326)^2
    + (x307 - x327)^2 + (x308 - x328)^2) + x61 - 2.23606797749979 * b399
    >= -2.23606797749979)
@NLconstraint(m, e62, -sqrt((x304 - x329)^2 + (x305 - x330)^2 + (x306 - x331)^2
    + (x307 - x332)^2 + (x308 - x333)^2) + x62 - 2.23606797749979 * b400
    >= -2.23606797749979)
@NLconstraint(m, e63, -sqrt((x304 - x334)^2 + (x305 - x335)^2 + (x306 - x336)^2
    + (x307 - x337)^2 + (x308 - x338)^2) + x63 - 2.23606797749979 * b401
    >= -2.23606797749979)
@NLconstraint(m, e64, -sqrt((x309 - x314)^2 + (x310 - x315)^2 + (x311 - x316)^2
    + (x312 - x317)^2 + (x313 - x318)^2) + x64 - 2.23606797749979 * b402
    >= -2.23606797749979)
@NLconstraint(m, e65, -sqrt((x309 - x319)^2 + (x310 - x320)^2 + (x311 - x321)^2
    + (x312 - x322)^2 + (x313 - x323)^2) + x65 - 2.23606797749979 * b403
    >= -2.23606797749979)
@NLconstraint(m, e66, -sqrt((x309 - x324)^2 + (x310 - x325)^2 + (x311 - x326)^2
    + (x312 - x327)^2 + (x313 - x328)^2) + x66 - 2.23606797749979 * b404
    >= -2.23606797749979)
@NLconstraint(m, e67, -sqrt((x309 - x329)^2 + (x310 - x330)^2 + (x311 - x331)^2
    + (x312 - x332)^2 + (x313 - x333)^2) + x67 - 2.23606797749979 * b405
    >= -2.23606797749979)
@NLconstraint(m, e68, -sqrt((x309 - x334)^2 + (x310 - x335)^2 + (x311 - x336)^2
    + (x312 - x337)^2 + (x313 - x338)^2) + x68 - 2.23606797749979 * b406
    >= -2.23606797749979)
@NLconstraint(m, e69, -sqrt((x314 - x319)^2 + (x315 - x320)^2 + (x316 - x321)^2
    + (x317 - x322)^2 + (x318 - x323)^2) + x69 - 2.23606797749979 * b407
    >= -2.23606797749979)
@NLconstraint(m, e70, -sqrt((x314 - x324)^2 + (x315 - x325)^2 + (x316 - x326)^2
    + (x317 - x327)^2 + (x318 - x328)^2) + x70 - 2.23606797749979 * b408
    >= -2.23606797749979)
@NLconstraint(m, e71, -sqrt((x314 - x329)^2 + (x315 - x330)^2 + (x316 - x331)^2
    + (x317 - x332)^2 + (x318 - x333)^2) + x71 - 2.23606797749979 * b409
    >= -2.23606797749979)
@NLconstraint(m, e72, -sqrt((x314 - x334)^2 + (x315 - x335)^2 + (x316 - x336)^2
    + (x317 - x337)^2 + (x318 - x338)^2) + x72 - 2.23606797749979 * b410
    >= -2.23606797749979)
@NLconstraint(m, e73, -sqrt((x319 - x324)^2 + (x320 - x325)^2 + (x321 - x326)^2
    + (x322 - x327)^2 + (x323 - x328)^2) + x73 - 2.23606797749979 * b411
    >= -2.23606797749979)
@NLconstraint(m, e74, -sqrt((x319 - x329)^2 + (x320 - x330)^2 + (x321 - x331)^2
    + (x322 - x332)^2 + (x323 - x333)^2) + x74 - 2.23606797749979 * b412
    >= -2.23606797749979)
@NLconstraint(m, e75, -sqrt((x319 - x334)^2 + (x320 - x335)^2 + (x321 - x336)^2
    + (x322 - x337)^2 + (x323 - x338)^2) + x75 - 2.23606797749979 * b413
    >= -2.23606797749979)
@NLconstraint(m, e76, -sqrt((x324 - x329)^2 + (x325 - x330)^2 + (x326 - x331)^2
    + (x327 - x332)^2 + (x328 - x333)^2) + x76 - 2.23606797749979 * b414
    >= -2.23606797749979)
@NLconstraint(m, e77, -sqrt((x324 - x334)^2 + (x325 - x335)^2 + (x326 - x336)^2
    + (x327 - x337)^2 + (x328 - x338)^2) + x77 - 2.23606797749979 * b415
    >= -2.23606797749979)
@NLconstraint(m, e78, -sqrt((x329 - x334)^2 + (x330 - x335)^2 + (x331 - x336)^2
    + (x332 - x337)^2 + (x333 - x338)^2) + x78 - 2.23606797749979 * b416
    >= -2.23606797749979)
@NLconstraint(m, e79, -sqrt((-0.45084513414500904 + x274)^2 + (
    -0.4366195682760844 + x275)^2 + (-0.04163444585203002 + x276)^2 + (
    -0.7676272579584664 + x277)^2 + (-0.6734553564483233 + x278)^2) + x79 -
    2.23606797749979 * b417 >= -2.23606797749979)
@NLconstraint(m, e80, -sqrt((-0.670857540712527 + x274)^2 + (-0.472665488047444
    + x275)^2 + (-0.672731114024884 + x276)^2 + (-0.8824812534975449 + x277)^2
    + (-0.6920224414883532 + x278)^2) + x80 - 2.23606797749979 * b418
    >= -2.23606797749979)
@NLconstraint(m, e81, -sqrt((-0.3456424258652263 + x274)^2 + (
    -0.897323531600062 + x275)^2 + (-0.3169943908371815 + x276)^2 + (
    -0.08378401217902964 + x277)^2 + (-0.2511840930177276 + x278)^2) + x81 -
    2.23606797749979 * b419 >= -2.23606797749979)
@NLconstraint(m, e82, -sqrt((-0.49653521716587157 + x274)^2 + (
    -0.8612924863730758 + x275)^2 + (-0.3477168575425721 + x276)^2 + (
    -0.6615424192381595 + x277)^2 + (-0.2680635035686557 + x278)^2) + x82 -
    2.23606797749979 * b420 >= -2.23606797749979)
@NLconstraint(m, e83, -sqrt((-0.027492190735120214 + x274)^2 + (
    -0.975830678205581 + x275)^2 + (-0.5725079974762737 + x276)^2 + (
    -0.4627928206739904 + x277)^2 + (-0.676105217625283 + x278)^2) + x83 -
    2.23606797749979 * b421 >= -2.23606797749979)
@NLconstraint(m, e84, -sqrt((-0.13167765137927434 + x274)^2 + (
    -0.8772422533001436 + x275)^2 + (-0.30212459335273456 + x276)^2 + (
    -0.9589299306054163 + x277)^2 + (-0.1684676992378059 + x278)^2) + x84 -
    2.23606797749979 * b422 >= -2.23606797749979)
@NLconstraint(m, e85, -sqrt((-0.4631605820201776 + x274)^2 + (
    -0.3075046464306209 + x275)^2 + (-0.6161047422348818 + x276)^2 + (
    -0.06036679498995601 + x277)^2 + (-0.055585229920206314 + x278)^2) + x85 -
    2.23606797749979 * b423 >= -2.23606797749979)
@NLconstraint(m, e86, -sqrt((-0.32388656731438237 + x274)^2 + (
    -0.05792786993199972 + x275)^2 + (-0.8135525615007164 + x276)^2 + (
    -0.11918904488489845 + x277)^2 + (-0.3074172166187361 + x278)^2) + x86 -
    2.23606797749979 * b424 >= -2.23606797749979)
@NLconstraint(m, e87, -sqrt((-0.5224218716951496 + x274)^2 + (
    -0.11445496716294967 + x275)^2 + (-0.9526471232336744 + x276)^2 + (
    -0.29191369035574544 + x277)^2 + (-0.5653246839270838 + x278)^2) + x87 -
    2.23606797749979 * b425 >= -2.23606797749979)
@NLconstraint(m, e88, -sqrt((-0.21125847741287684 + x274)^2 + (
    -0.24527434539791804 + x275)^2 + (-0.6289970479606978 + x276)^2 + (
    -0.7068457529300446 + x277)^2 + (-0.7943561377121612 + x278)^2) + x88 -
    2.23606797749979 * b426 >= -2.23606797749979)
@NLconstraint(m, e89, -sqrt((-0.9522420339595141 + x274)^2 + (
    -0.9326354363859527 + x275)^2 + (-0.4449382446418748 + x276)^2 + (
    -0.018772017414026565 + x277)^2 + (-0.1570753065990531 + x278)^2) + x89 -
    2.23606797749979 * b427 >= -2.23606797749979)
@NLconstraint(m, e90, -sqrt((-0.8796213188443197 + x274)^2 + (
    -0.9757325913906182 + x275)^2 + (-0.5478578093651233 + x276)^2 + (
    -0.00973548730106566 + x277)^2 + (-0.27048086044812103 + x278)^2) + x90 -
    2.23606797749979 * b428 >= -2.23606797749979)
@NLconstraint(m, e91, -sqrt((-0.7382526421375969 + x274)^2 + (
    -0.18734997029644274 + x275)^2 + (-0.2597432271723712 + x276)^2 + (
    -0.42962015792230956 + x277)^2 + (-0.7073477915737445 + x278)^2) + x91 -
    2.23606797749979 * b429 >= -2.23606797749979)
@NLconstraint(m, e92, -sqrt((-0.7480253586345234 + x274)^2 + (
    -0.39775488720466023 + x275)^2 + (-0.3653805995645427 + x276)^2 + (
    -0.5146776625112836 + x277)^2 + (-0.46172129982047827 + x278)^2) + x92 -
    2.23606797749979 * b430 >= -2.23606797749979)
@NLconstraint(m, e93, -sqrt((-0.9807955797704826 + x274)^2 + (
    -0.09734685184548297 + x275)^2 + (-0.38645671601793696 + x276)^2 + (
    -0.33263947083044576 + x277)^2 + (-0.5052803496499273 + x278)^2) + x93 -
    2.23606797749979 * b431 >= -2.23606797749979)
@NLconstraint(m, e94, -sqrt((-0.45084513414500904 + x279)^2 + (
    -0.4366195682760844 + x280)^2 + (-0.04163444585203002 + x281)^2 + (
    -0.7676272579584664 + x282)^2 + (-0.6734553564483233 + x283)^2) + x94 -
    2.23606797749979 * b432 >= -2.23606797749979)
@NLconstraint(m, e95, -sqrt((-0.670857540712527 + x279)^2 + (-0.472665488047444
    + x280)^2 + (-0.672731114024884 + x281)^2 + (-0.8824812534975449 + x282)^2
    + (-0.6920224414883532 + x283)^2) + x95 - 2.23606797749979 * b433
    >= -2.23606797749979)
@NLconstraint(m, e96, -sqrt((-0.3456424258652263 + x279)^2 + (
    -0.897323531600062 + x280)^2 + (-0.3169943908371815 + x281)^2 + (
    -0.08378401217902964 + x282)^2 + (-0.2511840930177276 + x283)^2) + x96 -
    2.23606797749979 * b434 >= -2.23606797749979)
@NLconstraint(m, e97, -sqrt((-0.49653521716587157 + x279)^2 + (
    -0.8612924863730758 + x280)^2 + (-0.3477168575425721 + x281)^2 + (
    -0.6615424192381595 + x282)^2 + (-0.2680635035686557 + x283)^2) + x97 -
    2.23606797749979 * b435 >= -2.23606797749979)
@NLconstraint(m, e98, -sqrt((-0.027492190735120214 + x279)^2 + (
    -0.975830678205581 + x280)^2 + (-0.5725079974762737 + x281)^2 + (
    -0.4627928206739904 + x282)^2 + (-0.676105217625283 + x283)^2) + x98 -
    2.23606797749979 * b436 >= -2.23606797749979)
@NLconstraint(m, e99, -sqrt((-0.13167765137927434 + x279)^2 + (
    -0.8772422533001436 + x280)^2 + (-0.30212459335273456 + x281)^2 + (
    -0.9589299306054163 + x282)^2 + (-0.1684676992378059 + x283)^2) + x99 -
    2.23606797749979 * b437 >= -2.23606797749979)
@NLconstraint(m, e100, -sqrt((-0.4631605820201776 + x279)^2 + (
    -0.3075046464306209 + x280)^2 + (-0.6161047422348818 + x281)^2 + (
    -0.06036679498995601 + x282)^2 + (-0.055585229920206314 + x283)^2) + x100
    - 2.23606797749979 * b438 >= -2.23606797749979)
@NLconstraint(m, e101, -sqrt((-0.32388656731438237 + x279)^2 + (
    -0.05792786993199972 + x280)^2 + (-0.8135525615007164 + x281)^2 + (
    -0.11918904488489845 + x282)^2 + (-0.3074172166187361 + x283)^2) + x101 -
    2.23606797749979 * b439 >= -2.23606797749979)
@NLconstraint(m, e102, -sqrt((-0.5224218716951496 + x279)^2 + (
    -0.11445496716294967 + x280)^2 + (-0.9526471232336744 + x281)^2 + (
    -0.29191369035574544 + x282)^2 + (-0.5653246839270838 + x283)^2) + x102 -
    2.23606797749979 * b440 >= -2.23606797749979)
@NLconstraint(m, e103, -sqrt((-0.21125847741287684 + x279)^2 + (
    -0.24527434539791804 + x280)^2 + (-0.6289970479606978 + x281)^2 + (
    -0.7068457529300446 + x282)^2 + (-0.7943561377121612 + x283)^2) + x103 -
    2.23606797749979 * b441 >= -2.23606797749979)
@NLconstraint(m, e104, -sqrt((-0.9522420339595141 + x279)^2 + (
    -0.9326354363859527 + x280)^2 + (-0.4449382446418748 + x281)^2 + (
    -0.018772017414026565 + x282)^2 + (-0.1570753065990531 + x283)^2) + x104 -
    2.23606797749979 * b442 >= -2.23606797749979)
@NLconstraint(m, e105, -sqrt((-0.8796213188443197 + x279)^2 + (
    -0.9757325913906182 + x280)^2 + (-0.5478578093651233 + x281)^2 + (
    -0.00973548730106566 + x282)^2 + (-0.27048086044812103 + x283)^2) + x105 -
    2.23606797749979 * b443 >= -2.23606797749979)
@NLconstraint(m, e106, -sqrt((-0.7382526421375969 + x279)^2 + (
    -0.18734997029644274 + x280)^2 + (-0.2597432271723712 + x281)^2 + (
    -0.42962015792230956 + x282)^2 + (-0.7073477915737445 + x283)^2) + x106 -
    2.23606797749979 * b444 >= -2.23606797749979)
@NLconstraint(m, e107, -sqrt((-0.7480253586345234 + x279)^2 + (
    -0.39775488720466023 + x280)^2 + (-0.3653805995645427 + x281)^2 + (
    -0.5146776625112836 + x282)^2 + (-0.46172129982047827 + x283)^2) + x107 -
    2.23606797749979 * b445 >= -2.23606797749979)
@NLconstraint(m, e108, -sqrt((-0.9807955797704826 + x279)^2 + (
    -0.09734685184548297 + x280)^2 + (-0.38645671601793696 + x281)^2 + (
    -0.33263947083044576 + x282)^2 + (-0.5052803496499273 + x283)^2) + x108 -
    2.23606797749979 * b446 >= -2.23606797749979)
@NLconstraint(m, e109, -sqrt((-0.45084513414500904 + x284)^2 + (
    -0.4366195682760844 + x285)^2 + (-0.04163444585203002 + x286)^2 + (
    -0.7676272579584664 + x287)^2 + (-0.6734553564483233 + x288)^2) + x109 -
    2.23606797749979 * b447 >= -2.23606797749979)
@NLconstraint(m, e110, -sqrt((-0.670857540712527 + x284)^2 + (
    -0.472665488047444 + x285)^2 + (-0.672731114024884 + x286)^2 + (
    -0.8824812534975449 + x287)^2 + (-0.6920224414883532 + x288)^2) + x110 -
    2.23606797749979 * b448 >= -2.23606797749979)
@NLconstraint(m, e111, -sqrt((-0.3456424258652263 + x284)^2 + (
    -0.897323531600062 + x285)^2 + (-0.3169943908371815 + x286)^2 + (
    -0.08378401217902964 + x287)^2 + (-0.2511840930177276 + x288)^2) + x111 -
    2.23606797749979 * b449 >= -2.23606797749979)
@NLconstraint(m, e112, -sqrt((-0.49653521716587157 + x284)^2 + (
    -0.8612924863730758 + x285)^2 + (-0.3477168575425721 + x286)^2 + (
    -0.6615424192381595 + x287)^2 + (-0.2680635035686557 + x288)^2) + x112 -
    2.23606797749979 * b450 >= -2.23606797749979)
@NLconstraint(m, e113, -sqrt((-0.027492190735120214 + x284)^2 + (
    -0.975830678205581 + x285)^2 + (-0.5725079974762737 + x286)^2 + (
    -0.4627928206739904 + x287)^2 + (-0.676105217625283 + x288)^2) + x113 -
    2.23606797749979 * b451 >= -2.23606797749979)
@NLconstraint(m, e114, -sqrt((-0.13167765137927434 + x284)^2 + (
    -0.8772422533001436 + x285)^2 + (-0.30212459335273456 + x286)^2 + (
    -0.9589299306054163 + x287)^2 + (-0.1684676992378059 + x288)^2) + x114 -
    2.23606797749979 * b452 >= -2.23606797749979)
@NLconstraint(m, e115, -sqrt((-0.4631605820201776 + x284)^2 + (
    -0.3075046464306209 + x285)^2 + (-0.6161047422348818 + x286)^2 + (
    -0.06036679498995601 + x287)^2 + (-0.055585229920206314 + x288)^2) + x115
    - 2.23606797749979 * b453 >= -2.23606797749979)
@NLconstraint(m, e116, -sqrt((-0.32388656731438237 + x284)^2 + (
    -0.05792786993199972 + x285)^2 + (-0.8135525615007164 + x286)^2 + (
    -0.11918904488489845 + x287)^2 + (-0.3074172166187361 + x288)^2) + x116 -
    2.23606797749979 * b454 >= -2.23606797749979)
@NLconstraint(m, e117, -sqrt((-0.5224218716951496 + x284)^2 + (
    -0.11445496716294967 + x285)^2 + (-0.9526471232336744 + x286)^2 + (
    -0.29191369035574544 + x287)^2 + (-0.5653246839270838 + x288)^2) + x117 -
    2.23606797749979 * b455 >= -2.23606797749979)
@NLconstraint(m, e118, -sqrt((-0.21125847741287684 + x284)^2 + (
    -0.24527434539791804 + x285)^2 + (-0.6289970479606978 + x286)^2 + (
    -0.7068457529300446 + x287)^2 + (-0.7943561377121612 + x288)^2) + x118 -
    2.23606797749979 * b456 >= -2.23606797749979)
@NLconstraint(m, e119, -sqrt((-0.9522420339595141 + x284)^2 + (
    -0.9326354363859527 + x285)^2 + (-0.4449382446418748 + x286)^2 + (
    -0.018772017414026565 + x287)^2 + (-0.1570753065990531 + x288)^2) + x119 -
    2.23606797749979 * b457 >= -2.23606797749979)
@NLconstraint(m, e120, -sqrt((-0.8796213188443197 + x284)^2 + (
    -0.9757325913906182 + x285)^2 + (-0.5478578093651233 + x286)^2 + (
    -0.00973548730106566 + x287)^2 + (-0.27048086044812103 + x288)^2) + x120 -
    2.23606797749979 * b458 >= -2.23606797749979)
@NLconstraint(m, e121, -sqrt((-0.7382526421375969 + x284)^2 + (
    -0.18734997029644274 + x285)^2 + (-0.2597432271723712 + x286)^2 + (
    -0.42962015792230956 + x287)^2 + (-0.7073477915737445 + x288)^2) + x121 -
    2.23606797749979 * b459 >= -2.23606797749979)
@NLconstraint(m, e122, -sqrt((-0.7480253586345234 + x284)^2 + (
    -0.39775488720466023 + x285)^2 + (-0.3653805995645427 + x286)^2 + (
    -0.5146776625112836 + x287)^2 + (-0.46172129982047827 + x288)^2) + x122 -
    2.23606797749979 * b460 >= -2.23606797749979)
@NLconstraint(m, e123, -sqrt((-0.9807955797704826 + x284)^2 + (
    -0.09734685184548297 + x285)^2 + (-0.38645671601793696 + x286)^2 + (
    -0.33263947083044576 + x287)^2 + (-0.5052803496499273 + x288)^2) + x123 -
    2.23606797749979 * b461 >= -2.23606797749979)
@NLconstraint(m, e124, -sqrt((-0.45084513414500904 + x289)^2 + (
    -0.4366195682760844 + x290)^2 + (-0.04163444585203002 + x291)^2 + (
    -0.7676272579584664 + x292)^2 + (-0.6734553564483233 + x293)^2) + x124 -
    2.23606797749979 * b462 >= -2.23606797749979)
@NLconstraint(m, e125, -sqrt((-0.670857540712527 + x289)^2 + (
    -0.472665488047444 + x290)^2 + (-0.672731114024884 + x291)^2 + (
    -0.8824812534975449 + x292)^2 + (-0.6920224414883532 + x293)^2) + x125 -
    2.23606797749979 * b463 >= -2.23606797749979)
@NLconstraint(m, e126, -sqrt((-0.3456424258652263 + x289)^2 + (
    -0.897323531600062 + x290)^2 + (-0.3169943908371815 + x291)^2 + (
    -0.08378401217902964 + x292)^2 + (-0.2511840930177276 + x293)^2) + x126 -
    2.23606797749979 * b464 >= -2.23606797749979)
@NLconstraint(m, e127, -sqrt((-0.49653521716587157 + x289)^2 + (
    -0.8612924863730758 + x290)^2 + (-0.3477168575425721 + x291)^2 + (
    -0.6615424192381595 + x292)^2 + (-0.2680635035686557 + x293)^2) + x127 -
    2.23606797749979 * b465 >= -2.23606797749979)
@NLconstraint(m, e128, -sqrt((-0.027492190735120214 + x289)^2 + (
    -0.975830678205581 + x290)^2 + (-0.5725079974762737 + x291)^2 + (
    -0.4627928206739904 + x292)^2 + (-0.676105217625283 + x293)^2) + x128 -
    2.23606797749979 * b466 >= -2.23606797749979)
@NLconstraint(m, e129, -sqrt((-0.13167765137927434 + x289)^2 + (
    -0.8772422533001436 + x290)^2 + (-0.30212459335273456 + x291)^2 + (
    -0.9589299306054163 + x292)^2 + (-0.1684676992378059 + x293)^2) + x129 -
    2.23606797749979 * b467 >= -2.23606797749979)
@NLconstraint(m, e130, -sqrt((-0.4631605820201776 + x289)^2 + (
    -0.3075046464306209 + x290)^2 + (-0.6161047422348818 + x291)^2 + (
    -0.06036679498995601 + x292)^2 + (-0.055585229920206314 + x293)^2) + x130
    - 2.23606797749979 * b468 >= -2.23606797749979)
@NLconstraint(m, e131, -sqrt((-0.32388656731438237 + x289)^2 + (
    -0.05792786993199972 + x290)^2 + (-0.8135525615007164 + x291)^2 + (
    -0.11918904488489845 + x292)^2 + (-0.3074172166187361 + x293)^2) + x131 -
    2.23606797749979 * b469 >= -2.23606797749979)
@NLconstraint(m, e132, -sqrt((-0.5224218716951496 + x289)^2 + (
    -0.11445496716294967 + x290)^2 + (-0.9526471232336744 + x291)^2 + (
    -0.29191369035574544 + x292)^2 + (-0.5653246839270838 + x293)^2) + x132 -
    2.23606797749979 * b470 >= -2.23606797749979)
@NLconstraint(m, e133, -sqrt((-0.21125847741287684 + x289)^2 + (
    -0.24527434539791804 + x290)^2 + (-0.6289970479606978 + x291)^2 + (
    -0.7068457529300446 + x292)^2 + (-0.7943561377121612 + x293)^2) + x133 -
    2.23606797749979 * b471 >= -2.23606797749979)
@NLconstraint(m, e134, -sqrt((-0.9522420339595141 + x289)^2 + (
    -0.9326354363859527 + x290)^2 + (-0.4449382446418748 + x291)^2 + (
    -0.018772017414026565 + x292)^2 + (-0.1570753065990531 + x293)^2) + x134 -
    2.23606797749979 * b472 >= -2.23606797749979)
@NLconstraint(m, e135, -sqrt((-0.8796213188443197 + x289)^2 + (
    -0.9757325913906182 + x290)^2 + (-0.5478578093651233 + x291)^2 + (
    -0.00973548730106566 + x292)^2 + (-0.27048086044812103 + x293)^2) + x135 -
    2.23606797749979 * b473 >= -2.23606797749979)
@NLconstraint(m, e136, -sqrt((-0.7382526421375969 + x289)^2 + (
    -0.18734997029644274 + x290)^2 + (-0.2597432271723712 + x291)^2 + (
    -0.42962015792230956 + x292)^2 + (-0.7073477915737445 + x293)^2) + x136 -
    2.23606797749979 * b474 >= -2.23606797749979)
@NLconstraint(m, e137, -sqrt((-0.7480253586345234 + x289)^2 + (
    -0.39775488720466023 + x290)^2 + (-0.3653805995645427 + x291)^2 + (
    -0.5146776625112836 + x292)^2 + (-0.46172129982047827 + x293)^2) + x137 -
    2.23606797749979 * b475 >= -2.23606797749979)
@NLconstraint(m, e138, -sqrt((-0.9807955797704826 + x289)^2 + (
    -0.09734685184548297 + x290)^2 + (-0.38645671601793696 + x291)^2 + (
    -0.33263947083044576 + x292)^2 + (-0.5052803496499273 + x293)^2) + x138 -
    2.23606797749979 * b476 >= -2.23606797749979)
@NLconstraint(m, e139, -sqrt((-0.45084513414500904 + x294)^2 + (
    -0.4366195682760844 + x295)^2 + (-0.04163444585203002 + x296)^2 + (
    -0.7676272579584664 + x297)^2 + (-0.6734553564483233 + x298)^2) + x139 -
    2.23606797749979 * b477 >= -2.23606797749979)
@NLconstraint(m, e140, -sqrt((-0.670857540712527 + x294)^2 + (
    -0.472665488047444 + x295)^2 + (-0.672731114024884 + x296)^2 + (
    -0.8824812534975449 + x297)^2 + (-0.6920224414883532 + x298)^2) + x140 -
    2.23606797749979 * b478 >= -2.23606797749979)
@NLconstraint(m, e141, -sqrt((-0.3456424258652263 + x294)^2 + (
    -0.897323531600062 + x295)^2 + (-0.3169943908371815 + x296)^2 + (
    -0.08378401217902964 + x297)^2 + (-0.2511840930177276 + x298)^2) + x141 -
    2.23606797749979 * b479 >= -2.23606797749979)
@NLconstraint(m, e142, -sqrt((-0.49653521716587157 + x294)^2 + (
    -0.8612924863730758 + x295)^2 + (-0.3477168575425721 + x296)^2 + (
    -0.6615424192381595 + x297)^2 + (-0.2680635035686557 + x298)^2) + x142 -
    2.23606797749979 * b480 >= -2.23606797749979)
@NLconstraint(m, e143, -sqrt((-0.027492190735120214 + x294)^2 + (
    -0.975830678205581 + x295)^2 + (-0.5725079974762737 + x296)^2 + (
    -0.4627928206739904 + x297)^2 + (-0.676105217625283 + x298)^2) + x143 -
    2.23606797749979 * b481 >= -2.23606797749979)
@NLconstraint(m, e144, -sqrt((-0.13167765137927434 + x294)^2 + (
    -0.8772422533001436 + x295)^2 + (-0.30212459335273456 + x296)^2 + (
    -0.9589299306054163 + x297)^2 + (-0.1684676992378059 + x298)^2) + x144 -
    2.23606797749979 * b482 >= -2.23606797749979)
@NLconstraint(m, e145, -sqrt((-0.4631605820201776 + x294)^2 + (
    -0.3075046464306209 + x295)^2 + (-0.6161047422348818 + x296)^2 + (
    -0.06036679498995601 + x297)^2 + (-0.055585229920206314 + x298)^2) + x145
    - 2.23606797749979 * b483 >= -2.23606797749979)
@NLconstraint(m, e146, -sqrt((-0.32388656731438237 + x294)^2 + (
    -0.05792786993199972 + x295)^2 + (-0.8135525615007164 + x296)^2 + (
    -0.11918904488489845 + x297)^2 + (-0.3074172166187361 + x298)^2) + x146 -
    2.23606797749979 * b484 >= -2.23606797749979)
@NLconstraint(m, e147, -sqrt((-0.5224218716951496 + x294)^2 + (
    -0.11445496716294967 + x295)^2 + (-0.9526471232336744 + x296)^2 + (
    -0.29191369035574544 + x297)^2 + (-0.5653246839270838 + x298)^2) + x147 -
    2.23606797749979 * b485 >= -2.23606797749979)
@NLconstraint(m, e148, -sqrt((-0.21125847741287684 + x294)^2 + (
    -0.24527434539791804 + x295)^2 + (-0.6289970479606978 + x296)^2 + (
    -0.7068457529300446 + x297)^2 + (-0.7943561377121612 + x298)^2) + x148 -
    2.23606797749979 * b486 >= -2.23606797749979)
@NLconstraint(m, e149, -sqrt((-0.9522420339595141 + x294)^2 + (
    -0.9326354363859527 + x295)^2 + (-0.4449382446418748 + x296)^2 + (
    -0.018772017414026565 + x297)^2 + (-0.1570753065990531 + x298)^2) + x149 -
    2.23606797749979 * b487 >= -2.23606797749979)
@NLconstraint(m, e150, -sqrt((-0.8796213188443197 + x294)^2 + (
    -0.9757325913906182 + x295)^2 + (-0.5478578093651233 + x296)^2 + (
    -0.00973548730106566 + x297)^2 + (-0.27048086044812103 + x298)^2) + x150 -
    2.23606797749979 * b488 >= -2.23606797749979)
@NLconstraint(m, e151, -sqrt((-0.7382526421375969 + x294)^2 + (
    -0.18734997029644274 + x295)^2 + (-0.2597432271723712 + x296)^2 + (
    -0.42962015792230956 + x297)^2 + (-0.7073477915737445 + x298)^2) + x151 -
    2.23606797749979 * b489 >= -2.23606797749979)
@NLconstraint(m, e152, -sqrt((-0.7480253586345234 + x294)^2 + (
    -0.39775488720466023 + x295)^2 + (-0.3653805995645427 + x296)^2 + (
    -0.5146776625112836 + x297)^2 + (-0.46172129982047827 + x298)^2) + x152 -
    2.23606797749979 * b490 >= -2.23606797749979)
@NLconstraint(m, e153, -sqrt((-0.9807955797704826 + x294)^2 + (
    -0.09734685184548297 + x295)^2 + (-0.38645671601793696 + x296)^2 + (
    -0.33263947083044576 + x297)^2 + (-0.5052803496499273 + x298)^2) + x153 -
    2.23606797749979 * b491 >= -2.23606797749979)
@NLconstraint(m, e154, -sqrt((-0.45084513414500904 + x299)^2 + (
    -0.4366195682760844 + x300)^2 + (-0.04163444585203002 + x301)^2 + (
    -0.7676272579584664 + x302)^2 + (-0.6734553564483233 + x303)^2) + x154 -
    2.23606797749979 * b492 >= -2.23606797749979)
@NLconstraint(m, e155, -sqrt((-0.670857540712527 + x299)^2 + (
    -0.472665488047444 + x300)^2 + (-0.672731114024884 + x301)^2 + (
    -0.8824812534975449 + x302)^2 + (-0.6920224414883532 + x303)^2) + x155 -
    2.23606797749979 * b493 >= -2.23606797749979)
@NLconstraint(m, e156, -sqrt((-0.3456424258652263 + x299)^2 + (
    -0.897323531600062 + x300)^2 + (-0.3169943908371815 + x301)^2 + (
    -0.08378401217902964 + x302)^2 + (-0.2511840930177276 + x303)^2) + x156 -
    2.23606797749979 * b494 >= -2.23606797749979)
@NLconstraint(m, e157, -sqrt((-0.49653521716587157 + x299)^2 + (
    -0.8612924863730758 + x300)^2 + (-0.3477168575425721 + x301)^2 + (
    -0.6615424192381595 + x302)^2 + (-0.2680635035686557 + x303)^2) + x157 -
    2.23606797749979 * b495 >= -2.23606797749979)
@NLconstraint(m, e158, -sqrt((-0.027492190735120214 + x299)^2 + (
    -0.975830678205581 + x300)^2 + (-0.5725079974762737 + x301)^2 + (
    -0.4627928206739904 + x302)^2 + (-0.676105217625283 + x303)^2) + x158 -
    2.23606797749979 * b496 >= -2.23606797749979)
@NLconstraint(m, e159, -sqrt((-0.13167765137927434 + x299)^2 + (
    -0.8772422533001436 + x300)^2 + (-0.30212459335273456 + x301)^2 + (
    -0.9589299306054163 + x302)^2 + (-0.1684676992378059 + x303)^2) + x159 -
    2.23606797749979 * b497 >= -2.23606797749979)
@NLconstraint(m, e160, -sqrt((-0.4631605820201776 + x299)^2 + (
    -0.3075046464306209 + x300)^2 + (-0.6161047422348818 + x301)^2 + (
    -0.06036679498995601 + x302)^2 + (-0.055585229920206314 + x303)^2) + x160
    - 2.23606797749979 * b498 >= -2.23606797749979)
@NLconstraint(m, e161, -sqrt((-0.32388656731438237 + x299)^2 + (
    -0.05792786993199972 + x300)^2 + (-0.8135525615007164 + x301)^2 + (
    -0.11918904488489845 + x302)^2 + (-0.3074172166187361 + x303)^2) + x161 -
    2.23606797749979 * b499 >= -2.23606797749979)
@NLconstraint(m, e162, -sqrt((-0.5224218716951496 + x299)^2 + (
    -0.11445496716294967 + x300)^2 + (-0.9526471232336744 + x301)^2 + (
    -0.29191369035574544 + x302)^2 + (-0.5653246839270838 + x303)^2) + x162 -
    2.23606797749979 * b500 >= -2.23606797749979)
@NLconstraint(m, e163, -sqrt((-0.21125847741287684 + x299)^2 + (
    -0.24527434539791804 + x300)^2 + (-0.6289970479606978 + x301)^2 + (
    -0.7068457529300446 + x302)^2 + (-0.7943561377121612 + x303)^2) + x163 -
    2.23606797749979 * b501 >= -2.23606797749979)
@NLconstraint(m, e164, -sqrt((-0.9522420339595141 + x299)^2 + (
    -0.9326354363859527 + x300)^2 + (-0.4449382446418748 + x301)^2 + (
    -0.018772017414026565 + x302)^2 + (-0.1570753065990531 + x303)^2) + x164 -
    2.23606797749979 * b502 >= -2.23606797749979)
@NLconstraint(m, e165, -sqrt((-0.8796213188443197 + x299)^2 + (
    -0.9757325913906182 + x300)^2 + (-0.5478578093651233 + x301)^2 + (
    -0.00973548730106566 + x302)^2 + (-0.27048086044812103 + x303)^2) + x165 -
    2.23606797749979 * b503 >= -2.23606797749979)
@NLconstraint(m, e166, -sqrt((-0.7382526421375969 + x299)^2 + (
    -0.18734997029644274 + x300)^2 + (-0.2597432271723712 + x301)^2 + (
    -0.42962015792230956 + x302)^2 + (-0.7073477915737445 + x303)^2) + x166 -
    2.23606797749979 * b504 >= -2.23606797749979)
@NLconstraint(m, e167, -sqrt((-0.7480253586345234 + x299)^2 + (
    -0.39775488720466023 + x300)^2 + (-0.3653805995645427 + x301)^2 + (
    -0.5146776625112836 + x302)^2 + (-0.46172129982047827 + x303)^2) + x167 -
    2.23606797749979 * b505 >= -2.23606797749979)
@NLconstraint(m, e168, -sqrt((-0.9807955797704826 + x299)^2 + (
    -0.09734685184548297 + x300)^2 + (-0.38645671601793696 + x301)^2 + (
    -0.33263947083044576 + x302)^2 + (-0.5052803496499273 + x303)^2) + x168 -
    2.23606797749979 * b506 >= -2.23606797749979)
@NLconstraint(m, e169, -sqrt((-0.45084513414500904 + x304)^2 + (
    -0.4366195682760844 + x305)^2 + (-0.04163444585203002 + x306)^2 + (
    -0.7676272579584664 + x307)^2 + (-0.6734553564483233 + x308)^2) + x169 -
    2.23606797749979 * b507 >= -2.23606797749979)
@NLconstraint(m, e170, -sqrt((-0.670857540712527 + x304)^2 + (
    -0.472665488047444 + x305)^2 + (-0.672731114024884 + x306)^2 + (
    -0.8824812534975449 + x307)^2 + (-0.6920224414883532 + x308)^2) + x170 -
    2.23606797749979 * b508 >= -2.23606797749979)
@NLconstraint(m, e171, -sqrt((-0.3456424258652263 + x304)^2 + (
    -0.897323531600062 + x305)^2 + (-0.3169943908371815 + x306)^2 + (
    -0.08378401217902964 + x307)^2 + (-0.2511840930177276 + x308)^2) + x171 -
    2.23606797749979 * b509 >= -2.23606797749979)
@NLconstraint(m, e172, -sqrt((-0.49653521716587157 + x304)^2 + (
    -0.8612924863730758 + x305)^2 + (-0.3477168575425721 + x306)^2 + (
    -0.6615424192381595 + x307)^2 + (-0.2680635035686557 + x308)^2) + x172 -
    2.23606797749979 * b510 >= -2.23606797749979)
@NLconstraint(m, e173, -sqrt((-0.027492190735120214 + x304)^2 + (
    -0.975830678205581 + x305)^2 + (-0.5725079974762737 + x306)^2 + (
    -0.4627928206739904 + x307)^2 + (-0.676105217625283 + x308)^2) + x173 -
    2.23606797749979 * b511 >= -2.23606797749979)
@NLconstraint(m, e174, -sqrt((-0.13167765137927434 + x304)^2 + (
    -0.8772422533001436 + x305)^2 + (-0.30212459335273456 + x306)^2 + (
    -0.9589299306054163 + x307)^2 + (-0.1684676992378059 + x308)^2) + x174 -
    2.23606797749979 * b512 >= -2.23606797749979)
@NLconstraint(m, e175, -sqrt((-0.4631605820201776 + x304)^2 + (
    -0.3075046464306209 + x305)^2 + (-0.6161047422348818 + x306)^2 + (
    -0.06036679498995601 + x307)^2 + (-0.055585229920206314 + x308)^2) + x175
    - 2.23606797749979 * b513 >= -2.23606797749979)
@NLconstraint(m, e176, -sqrt((-0.32388656731438237 + x304)^2 + (
    -0.05792786993199972 + x305)^2 + (-0.8135525615007164 + x306)^2 + (
    -0.11918904488489845 + x307)^2 + (-0.3074172166187361 + x308)^2) + x176 -
    2.23606797749979 * b514 >= -2.23606797749979)
@NLconstraint(m, e177, -sqrt((-0.5224218716951496 + x304)^2 + (
    -0.11445496716294967 + x305)^2 + (-0.9526471232336744 + x306)^2 + (
    -0.29191369035574544 + x307)^2 + (-0.5653246839270838 + x308)^2) + x177 -
    2.23606797749979 * b515 >= -2.23606797749979)
@NLconstraint(m, e178, -sqrt((-0.21125847741287684 + x304)^2 + (
    -0.24527434539791804 + x305)^2 + (-0.6289970479606978 + x306)^2 + (
    -0.7068457529300446 + x307)^2 + (-0.7943561377121612 + x308)^2) + x178 -
    2.23606797749979 * b516 >= -2.23606797749979)
@NLconstraint(m, e179, -sqrt((-0.9522420339595141 + x304)^2 + (
    -0.9326354363859527 + x305)^2 + (-0.4449382446418748 + x306)^2 + (
    -0.018772017414026565 + x307)^2 + (-0.1570753065990531 + x308)^2) + x179 -
    2.23606797749979 * b517 >= -2.23606797749979)
@NLconstraint(m, e180, -sqrt((-0.8796213188443197 + x304)^2 + (
    -0.9757325913906182 + x305)^2 + (-0.5478578093651233 + x306)^2 + (
    -0.00973548730106566 + x307)^2 + (-0.27048086044812103 + x308)^2) + x180 -
    2.23606797749979 * b518 >= -2.23606797749979)
@NLconstraint(m, e181, -sqrt((-0.7382526421375969 + x304)^2 + (
    -0.18734997029644274 + x305)^2 + (-0.2597432271723712 + x306)^2 + (
    -0.42962015792230956 + x307)^2 + (-0.7073477915737445 + x308)^2) + x181 -
    2.23606797749979 * b519 >= -2.23606797749979)
@NLconstraint(m, e182, -sqrt((-0.7480253586345234 + x304)^2 + (
    -0.39775488720466023 + x305)^2 + (-0.3653805995645427 + x306)^2 + (
    -0.5146776625112836 + x307)^2 + (-0.46172129982047827 + x308)^2) + x182 -
    2.23606797749979 * b520 >= -2.23606797749979)
@NLconstraint(m, e183, -sqrt((-0.9807955797704826 + x304)^2 + (
    -0.09734685184548297 + x305)^2 + (-0.38645671601793696 + x306)^2 + (
    -0.33263947083044576 + x307)^2 + (-0.5052803496499273 + x308)^2) + x183 -
    2.23606797749979 * b521 >= -2.23606797749979)
@NLconstraint(m, e184, -sqrt((-0.45084513414500904 + x309)^2 + (
    -0.4366195682760844 + x310)^2 + (-0.04163444585203002 + x311)^2 + (
    -0.7676272579584664 + x312)^2 + (-0.6734553564483233 + x313)^2) + x184 -
    2.23606797749979 * b522 >= -2.23606797749979)
@NLconstraint(m, e185, -sqrt((-0.670857540712527 + x309)^2 + (
    -0.472665488047444 + x310)^2 + (-0.672731114024884 + x311)^2 + (
    -0.8824812534975449 + x312)^2 + (-0.6920224414883532 + x313)^2) + x185 -
    2.23606797749979 * b523 >= -2.23606797749979)
@NLconstraint(m, e186, -sqrt((-0.3456424258652263 + x309)^2 + (
    -0.897323531600062 + x310)^2 + (-0.3169943908371815 + x311)^2 + (
    -0.08378401217902964 + x312)^2 + (-0.2511840930177276 + x313)^2) + x186 -
    2.23606797749979 * b524 >= -2.23606797749979)
@NLconstraint(m, e187, -sqrt((-0.49653521716587157 + x309)^2 + (
    -0.8612924863730758 + x310)^2 + (-0.3477168575425721 + x311)^2 + (
    -0.6615424192381595 + x312)^2 + (-0.2680635035686557 + x313)^2) + x187 -
    2.23606797749979 * b525 >= -2.23606797749979)
@NLconstraint(m, e188, -sqrt((-0.027492190735120214 + x309)^2 + (
    -0.975830678205581 + x310)^2 + (-0.5725079974762737 + x311)^2 + (
    -0.4627928206739904 + x312)^2 + (-0.676105217625283 + x313)^2) + x188 -
    2.23606797749979 * b526 >= -2.23606797749979)
@NLconstraint(m, e189, -sqrt((-0.13167765137927434 + x309)^2 + (
    -0.8772422533001436 + x310)^2 + (-0.30212459335273456 + x311)^2 + (
    -0.9589299306054163 + x312)^2 + (-0.1684676992378059 + x313)^2) + x189 -
    2.23606797749979 * b527 >= -2.23606797749979)
@NLconstraint(m, e190, -sqrt((-0.4631605820201776 + x309)^2 + (
    -0.3075046464306209 + x310)^2 + (-0.6161047422348818 + x311)^2 + (
    -0.06036679498995601 + x312)^2 + (-0.055585229920206314 + x313)^2) + x190
    - 2.23606797749979 * b528 >= -2.23606797749979)
@NLconstraint(m, e191, -sqrt((-0.32388656731438237 + x309)^2 + (
    -0.05792786993199972 + x310)^2 + (-0.8135525615007164 + x311)^2 + (
    -0.11918904488489845 + x312)^2 + (-0.3074172166187361 + x313)^2) + x191 -
    2.23606797749979 * b529 >= -2.23606797749979)
@NLconstraint(m, e192, -sqrt((-0.5224218716951496 + x309)^2 + (
    -0.11445496716294967 + x310)^2 + (-0.9526471232336744 + x311)^2 + (
    -0.29191369035574544 + x312)^2 + (-0.5653246839270838 + x313)^2) + x192 -
    2.23606797749979 * b530 >= -2.23606797749979)
@NLconstraint(m, e193, -sqrt((-0.21125847741287684 + x309)^2 + (
    -0.24527434539791804 + x310)^2 + (-0.6289970479606978 + x311)^2 + (
    -0.7068457529300446 + x312)^2 + (-0.7943561377121612 + x313)^2) + x193 -
    2.23606797749979 * b531 >= -2.23606797749979)
@NLconstraint(m, e194, -sqrt((-0.9522420339595141 + x309)^2 + (
    -0.9326354363859527 + x310)^2 + (-0.4449382446418748 + x311)^2 + (
    -0.018772017414026565 + x312)^2 + (-0.1570753065990531 + x313)^2) + x194 -
    2.23606797749979 * b532 >= -2.23606797749979)
@NLconstraint(m, e195, -sqrt((-0.8796213188443197 + x309)^2 + (
    -0.9757325913906182 + x310)^2 + (-0.5478578093651233 + x311)^2 + (
    -0.00973548730106566 + x312)^2 + (-0.27048086044812103 + x313)^2) + x195 -
    2.23606797749979 * b533 >= -2.23606797749979)
@NLconstraint(m, e196, -sqrt((-0.7382526421375969 + x309)^2 + (
    -0.18734997029644274 + x310)^2 + (-0.2597432271723712 + x311)^2 + (
    -0.42962015792230956 + x312)^2 + (-0.7073477915737445 + x313)^2) + x196 -
    2.23606797749979 * b534 >= -2.23606797749979)
@NLconstraint(m, e197, -sqrt((-0.7480253586345234 + x309)^2 + (
    -0.39775488720466023 + x310)^2 + (-0.3653805995645427 + x311)^2 + (
    -0.5146776625112836 + x312)^2 + (-0.46172129982047827 + x313)^2) + x197 -
    2.23606797749979 * b535 >= -2.23606797749979)
@NLconstraint(m, e198, -sqrt((-0.9807955797704826 + x309)^2 + (
    -0.09734685184548297 + x310)^2 + (-0.38645671601793696 + x311)^2 + (
    -0.33263947083044576 + x312)^2 + (-0.5052803496499273 + x313)^2) + x198 -
    2.23606797749979 * b536 >= -2.23606797749979)
@NLconstraint(m, e199, -sqrt((-0.45084513414500904 + x314)^2 + (
    -0.4366195682760844 + x315)^2 + (-0.04163444585203002 + x316)^2 + (
    -0.7676272579584664 + x317)^2 + (-0.6734553564483233 + x318)^2) + x199 -
    2.23606797749979 * b537 >= -2.23606797749979)
@NLconstraint(m, e200, -sqrt((-0.670857540712527 + x314)^2 + (
    -0.472665488047444 + x315)^2 + (-0.672731114024884 + x316)^2 + (
    -0.8824812534975449 + x317)^2 + (-0.6920224414883532 + x318)^2) + x200 -
    2.23606797749979 * b538 >= -2.23606797749979)
@NLconstraint(m, e201, -sqrt((-0.3456424258652263 + x314)^2 + (
    -0.897323531600062 + x315)^2 + (-0.3169943908371815 + x316)^2 + (
    -0.08378401217902964 + x317)^2 + (-0.2511840930177276 + x318)^2) + x201 -
    2.23606797749979 * b539 >= -2.23606797749979)
@NLconstraint(m, e202, -sqrt((-0.49653521716587157 + x314)^2 + (
    -0.8612924863730758 + x315)^2 + (-0.3477168575425721 + x316)^2 + (
    -0.6615424192381595 + x317)^2 + (-0.2680635035686557 + x318)^2) + x202 -
    2.23606797749979 * b540 >= -2.23606797749979)
@NLconstraint(m, e203, -sqrt((-0.027492190735120214 + x314)^2 + (
    -0.975830678205581 + x315)^2 + (-0.5725079974762737 + x316)^2 + (
    -0.4627928206739904 + x317)^2 + (-0.676105217625283 + x318)^2) + x203 -
    2.23606797749979 * b541 >= -2.23606797749979)
@NLconstraint(m, e204, -sqrt((-0.13167765137927434 + x314)^2 + (
    -0.8772422533001436 + x315)^2 + (-0.30212459335273456 + x316)^2 + (
    -0.9589299306054163 + x317)^2 + (-0.1684676992378059 + x318)^2) + x204 -
    2.23606797749979 * b542 >= -2.23606797749979)
@NLconstraint(m, e205, -sqrt((-0.4631605820201776 + x314)^2 + (
    -0.3075046464306209 + x315)^2 + (-0.6161047422348818 + x316)^2 + (
    -0.06036679498995601 + x317)^2 + (-0.055585229920206314 + x318)^2) + x205
    - 2.23606797749979 * b543 >= -2.23606797749979)
@NLconstraint(m, e206, -sqrt((-0.32388656731438237 + x314)^2 + (
    -0.05792786993199972 + x315)^2 + (-0.8135525615007164 + x316)^2 + (
    -0.11918904488489845 + x317)^2 + (-0.3074172166187361 + x318)^2) + x206 -
    2.23606797749979 * b544 >= -2.23606797749979)
@NLconstraint(m, e207, -sqrt((-0.5224218716951496 + x314)^2 + (
    -0.11445496716294967 + x315)^2 + (-0.9526471232336744 + x316)^2 + (
    -0.29191369035574544 + x317)^2 + (-0.5653246839270838 + x318)^2) + x207 -
    2.23606797749979 * b545 >= -2.23606797749979)
@NLconstraint(m, e208, -sqrt((-0.21125847741287684 + x314)^2 + (
    -0.24527434539791804 + x315)^2 + (-0.6289970479606978 + x316)^2 + (
    -0.7068457529300446 + x317)^2 + (-0.7943561377121612 + x318)^2) + x208 -
    2.23606797749979 * b546 >= -2.23606797749979)
@NLconstraint(m, e209, -sqrt((-0.9522420339595141 + x314)^2 + (
    -0.9326354363859527 + x315)^2 + (-0.4449382446418748 + x316)^2 + (
    -0.018772017414026565 + x317)^2 + (-0.1570753065990531 + x318)^2) + x209 -
    2.23606797749979 * b547 >= -2.23606797749979)
@NLconstraint(m, e210, -sqrt((-0.8796213188443197 + x314)^2 + (
    -0.9757325913906182 + x315)^2 + (-0.5478578093651233 + x316)^2 + (
    -0.00973548730106566 + x317)^2 + (-0.27048086044812103 + x318)^2) + x210 -
    2.23606797749979 * b548 >= -2.23606797749979)
@NLconstraint(m, e211, -sqrt((-0.7382526421375969 + x314)^2 + (
    -0.18734997029644274 + x315)^2 + (-0.2597432271723712 + x316)^2 + (
    -0.42962015792230956 + x317)^2 + (-0.7073477915737445 + x318)^2) + x211 -
    2.23606797749979 * b549 >= -2.23606797749979)
@NLconstraint(m, e212, -sqrt((-0.7480253586345234 + x314)^2 + (
    -0.39775488720466023 + x315)^2 + (-0.3653805995645427 + x316)^2 + (
    -0.5146776625112836 + x317)^2 + (-0.46172129982047827 + x318)^2) + x212 -
    2.23606797749979 * b550 >= -2.23606797749979)
@NLconstraint(m, e213, -sqrt((-0.9807955797704826 + x314)^2 + (
    -0.09734685184548297 + x315)^2 + (-0.38645671601793696 + x316)^2 + (
    -0.33263947083044576 + x317)^2 + (-0.5052803496499273 + x318)^2) + x213 -
    2.23606797749979 * b551 >= -2.23606797749979)
@NLconstraint(m, e214, -sqrt((-0.45084513414500904 + x319)^2 + (
    -0.4366195682760844 + x320)^2 + (-0.04163444585203002 + x321)^2 + (
    -0.7676272579584664 + x322)^2 + (-0.6734553564483233 + x323)^2) + x214 -
    2.23606797749979 * b552 >= -2.23606797749979)
@NLconstraint(m, e215, -sqrt((-0.670857540712527 + x319)^2 + (
    -0.472665488047444 + x320)^2 + (-0.672731114024884 + x321)^2 + (
    -0.8824812534975449 + x322)^2 + (-0.6920224414883532 + x323)^2) + x215 -
    2.23606797749979 * b553 >= -2.23606797749979)
@NLconstraint(m, e216, -sqrt((-0.3456424258652263 + x319)^2 + (
    -0.897323531600062 + x320)^2 + (-0.3169943908371815 + x321)^2 + (
    -0.08378401217902964 + x322)^2 + (-0.2511840930177276 + x323)^2) + x216 -
    2.23606797749979 * b554 >= -2.23606797749979)
@NLconstraint(m, e217, -sqrt((-0.49653521716587157 + x319)^2 + (
    -0.8612924863730758 + x320)^2 + (-0.3477168575425721 + x321)^2 + (
    -0.6615424192381595 + x322)^2 + (-0.2680635035686557 + x323)^2) + x217 -
    2.23606797749979 * b555 >= -2.23606797749979)
@NLconstraint(m, e218, -sqrt((-0.027492190735120214 + x319)^2 + (
    -0.975830678205581 + x320)^2 + (-0.5725079974762737 + x321)^2 + (
    -0.4627928206739904 + x322)^2 + (-0.676105217625283 + x323)^2) + x218 -
    2.23606797749979 * b556 >= -2.23606797749979)
@NLconstraint(m, e219, -sqrt((-0.13167765137927434 + x319)^2 + (
    -0.8772422533001436 + x320)^2 + (-0.30212459335273456 + x321)^2 + (
    -0.9589299306054163 + x322)^2 + (-0.1684676992378059 + x323)^2) + x219 -
    2.23606797749979 * b557 >= -2.23606797749979)
@NLconstraint(m, e220, -sqrt((-0.4631605820201776 + x319)^2 + (
    -0.3075046464306209 + x320)^2 + (-0.6161047422348818 + x321)^2 + (
    -0.06036679498995601 + x322)^2 + (-0.055585229920206314 + x323)^2) + x220
    - 2.23606797749979 * b558 >= -2.23606797749979)
@NLconstraint(m, e221, -sqrt((-0.32388656731438237 + x319)^2 + (
    -0.05792786993199972 + x320)^2 + (-0.8135525615007164 + x321)^2 + (
    -0.11918904488489845 + x322)^2 + (-0.3074172166187361 + x323)^2) + x221 -
    2.23606797749979 * b559 >= -2.23606797749979)
@NLconstraint(m, e222, -sqrt((-0.5224218716951496 + x319)^2 + (
    -0.11445496716294967 + x320)^2 + (-0.9526471232336744 + x321)^2 + (
    -0.29191369035574544 + x322)^2 + (-0.5653246839270838 + x323)^2) + x222 -
    2.23606797749979 * b560 >= -2.23606797749979)
@NLconstraint(m, e223, -sqrt((-0.21125847741287684 + x319)^2 + (
    -0.24527434539791804 + x320)^2 + (-0.6289970479606978 + x321)^2 + (
    -0.7068457529300446 + x322)^2 + (-0.7943561377121612 + x323)^2) + x223 -
    2.23606797749979 * b561 >= -2.23606797749979)
@NLconstraint(m, e224, -sqrt((-0.9522420339595141 + x319)^2 + (
    -0.9326354363859527 + x320)^2 + (-0.4449382446418748 + x321)^2 + (
    -0.018772017414026565 + x322)^2 + (-0.1570753065990531 + x323)^2) + x224 -
    2.23606797749979 * b562 >= -2.23606797749979)
@NLconstraint(m, e225, -sqrt((-0.8796213188443197 + x319)^2 + (
    -0.9757325913906182 + x320)^2 + (-0.5478578093651233 + x321)^2 + (
    -0.00973548730106566 + x322)^2 + (-0.27048086044812103 + x323)^2) + x225 -
    2.23606797749979 * b563 >= -2.23606797749979)
@NLconstraint(m, e226, -sqrt((-0.7382526421375969 + x319)^2 + (
    -0.18734997029644274 + x320)^2 + (-0.2597432271723712 + x321)^2 + (
    -0.42962015792230956 + x322)^2 + (-0.7073477915737445 + x323)^2) + x226 -
    2.23606797749979 * b564 >= -2.23606797749979)
@NLconstraint(m, e227, -sqrt((-0.7480253586345234 + x319)^2 + (
    -0.39775488720466023 + x320)^2 + (-0.3653805995645427 + x321)^2 + (
    -0.5146776625112836 + x322)^2 + (-0.46172129982047827 + x323)^2) + x227 -
    2.23606797749979 * b565 >= -2.23606797749979)
@NLconstraint(m, e228, -sqrt((-0.9807955797704826 + x319)^2 + (
    -0.09734685184548297 + x320)^2 + (-0.38645671601793696 + x321)^2 + (
    -0.33263947083044576 + x322)^2 + (-0.5052803496499273 + x323)^2) + x228 -
    2.23606797749979 * b566 >= -2.23606797749979)
@NLconstraint(m, e229, -sqrt((-0.45084513414500904 + x324)^2 + (
    -0.4366195682760844 + x325)^2 + (-0.04163444585203002 + x326)^2 + (
    -0.7676272579584664 + x327)^2 + (-0.6734553564483233 + x328)^2) + x229 -
    2.23606797749979 * b567 >= -2.23606797749979)
@NLconstraint(m, e230, -sqrt((-0.670857540712527 + x324)^2 + (
    -0.472665488047444 + x325)^2 + (-0.672731114024884 + x326)^2 + (
    -0.8824812534975449 + x327)^2 + (-0.6920224414883532 + x328)^2) + x230 -
    2.23606797749979 * b568 >= -2.23606797749979)
@NLconstraint(m, e231, -sqrt((-0.3456424258652263 + x324)^2 + (
    -0.897323531600062 + x325)^2 + (-0.3169943908371815 + x326)^2 + (
    -0.08378401217902964 + x327)^2 + (-0.2511840930177276 + x328)^2) + x231 -
    2.23606797749979 * b569 >= -2.23606797749979)
@NLconstraint(m, e232, -sqrt((-0.49653521716587157 + x324)^2 + (
    -0.8612924863730758 + x325)^2 + (-0.3477168575425721 + x326)^2 + (
    -0.6615424192381595 + x327)^2 + (-0.2680635035686557 + x328)^2) + x232 -
    2.23606797749979 * b570 >= -2.23606797749979)
@NLconstraint(m, e233, -sqrt((-0.027492190735120214 + x324)^2 + (
    -0.975830678205581 + x325)^2 + (-0.5725079974762737 + x326)^2 + (
    -0.4627928206739904 + x327)^2 + (-0.676105217625283 + x328)^2) + x233 -
    2.23606797749979 * b571 >= -2.23606797749979)
@NLconstraint(m, e234, -sqrt((-0.13167765137927434 + x324)^2 + (
    -0.8772422533001436 + x325)^2 + (-0.30212459335273456 + x326)^2 + (
    -0.9589299306054163 + x327)^2 + (-0.1684676992378059 + x328)^2) + x234 -
    2.23606797749979 * b572 >= -2.23606797749979)
@NLconstraint(m, e235, -sqrt((-0.4631605820201776 + x324)^2 + (
    -0.3075046464306209 + x325)^2 + (-0.6161047422348818 + x326)^2 + (
    -0.06036679498995601 + x327)^2 + (-0.055585229920206314 + x328)^2) + x235
    - 2.23606797749979 * b573 >= -2.23606797749979)
@NLconstraint(m, e236, -sqrt((-0.32388656731438237 + x324)^2 + (
    -0.05792786993199972 + x325)^2 + (-0.8135525615007164 + x326)^2 + (
    -0.11918904488489845 + x327)^2 + (-0.3074172166187361 + x328)^2) + x236 -
    2.23606797749979 * b574 >= -2.23606797749979)
@NLconstraint(m, e237, -sqrt((-0.5224218716951496 + x324)^2 + (
    -0.11445496716294967 + x325)^2 + (-0.9526471232336744 + x326)^2 + (
    -0.29191369035574544 + x327)^2 + (-0.5653246839270838 + x328)^2) + x237 -
    2.23606797749979 * b575 >= -2.23606797749979)
@NLconstraint(m, e238, -sqrt((-0.21125847741287684 + x324)^2 + (
    -0.24527434539791804 + x325)^2 + (-0.6289970479606978 + x326)^2 + (
    -0.7068457529300446 + x327)^2 + (-0.7943561377121612 + x328)^2) + x238 -
    2.23606797749979 * b576 >= -2.23606797749979)
@NLconstraint(m, e239, -sqrt((-0.9522420339595141 + x324)^2 + (
    -0.9326354363859527 + x325)^2 + (-0.4449382446418748 + x326)^2 + (
    -0.018772017414026565 + x327)^2 + (-0.1570753065990531 + x328)^2) + x239 -
    2.23606797749979 * b577 >= -2.23606797749979)
@NLconstraint(m, e240, -sqrt((-0.8796213188443197 + x324)^2 + (
    -0.9757325913906182 + x325)^2 + (-0.5478578093651233 + x326)^2 + (
    -0.00973548730106566 + x327)^2 + (-0.27048086044812103 + x328)^2) + x240 -
    2.23606797749979 * b578 >= -2.23606797749979)
@NLconstraint(m, e241, -sqrt((-0.7382526421375969 + x324)^2 + (
    -0.18734997029644274 + x325)^2 + (-0.2597432271723712 + x326)^2 + (
    -0.42962015792230956 + x327)^2 + (-0.7073477915737445 + x328)^2) + x241 -
    2.23606797749979 * b579 >= -2.23606797749979)
@NLconstraint(m, e242, -sqrt((-0.7480253586345234 + x324)^2 + (
    -0.39775488720466023 + x325)^2 + (-0.3653805995645427 + x326)^2 + (
    -0.5146776625112836 + x327)^2 + (-0.46172129982047827 + x328)^2) + x242 -
    2.23606797749979 * b580 >= -2.23606797749979)
@NLconstraint(m, e243, -sqrt((-0.9807955797704826 + x324)^2 + (
    -0.09734685184548297 + x325)^2 + (-0.38645671601793696 + x326)^2 + (
    -0.33263947083044576 + x327)^2 + (-0.5052803496499273 + x328)^2) + x243 -
    2.23606797749979 * b581 >= -2.23606797749979)
@NLconstraint(m, e244, -sqrt((-0.45084513414500904 + x329)^2 + (
    -0.4366195682760844 + x330)^2 + (-0.04163444585203002 + x331)^2 + (
    -0.7676272579584664 + x332)^2 + (-0.6734553564483233 + x333)^2) + x244 -
    2.23606797749979 * b582 >= -2.23606797749979)
@NLconstraint(m, e245, -sqrt((-0.670857540712527 + x329)^2 + (
    -0.472665488047444 + x330)^2 + (-0.672731114024884 + x331)^2 + (
    -0.8824812534975449 + x332)^2 + (-0.6920224414883532 + x333)^2) + x245 -
    2.23606797749979 * b583 >= -2.23606797749979)
@NLconstraint(m, e246, -sqrt((-0.3456424258652263 + x329)^2 + (
    -0.897323531600062 + x330)^2 + (-0.3169943908371815 + x331)^2 + (
    -0.08378401217902964 + x332)^2 + (-0.2511840930177276 + x333)^2) + x246 -
    2.23606797749979 * b584 >= -2.23606797749979)
@NLconstraint(m, e247, -sqrt((-0.49653521716587157 + x329)^2 + (
    -0.8612924863730758 + x330)^2 + (-0.3477168575425721 + x331)^2 + (
    -0.6615424192381595 + x332)^2 + (-0.2680635035686557 + x333)^2) + x247 -
    2.23606797749979 * b585 >= -2.23606797749979)
@NLconstraint(m, e248, -sqrt((-0.027492190735120214 + x329)^2 + (
    -0.975830678205581 + x330)^2 + (-0.5725079974762737 + x331)^2 + (
    -0.4627928206739904 + x332)^2 + (-0.676105217625283 + x333)^2) + x248 -
    2.23606797749979 * b586 >= -2.23606797749979)
@NLconstraint(m, e249, -sqrt((-0.13167765137927434 + x329)^2 + (
    -0.8772422533001436 + x330)^2 + (-0.30212459335273456 + x331)^2 + (
    -0.9589299306054163 + x332)^2 + (-0.1684676992378059 + x333)^2) + x249 -
    2.23606797749979 * b587 >= -2.23606797749979)
@NLconstraint(m, e250, -sqrt((-0.4631605820201776 + x329)^2 + (
    -0.3075046464306209 + x330)^2 + (-0.6161047422348818 + x331)^2 + (
    -0.06036679498995601 + x332)^2 + (-0.055585229920206314 + x333)^2) + x250
    - 2.23606797749979 * b588 >= -2.23606797749979)
@NLconstraint(m, e251, -sqrt((-0.32388656731438237 + x329)^2 + (
    -0.05792786993199972 + x330)^2 + (-0.8135525615007164 + x331)^2 + (
    -0.11918904488489845 + x332)^2 + (-0.3074172166187361 + x333)^2) + x251 -
    2.23606797749979 * b589 >= -2.23606797749979)
@NLconstraint(m, e252, -sqrt((-0.5224218716951496 + x329)^2 + (
    -0.11445496716294967 + x330)^2 + (-0.9526471232336744 + x331)^2 + (
    -0.29191369035574544 + x332)^2 + (-0.5653246839270838 + x333)^2) + x252 -
    2.23606797749979 * b590 >= -2.23606797749979)
@NLconstraint(m, e253, -sqrt((-0.21125847741287684 + x329)^2 + (
    -0.24527434539791804 + x330)^2 + (-0.6289970479606978 + x331)^2 + (
    -0.7068457529300446 + x332)^2 + (-0.7943561377121612 + x333)^2) + x253 -
    2.23606797749979 * b591 >= -2.23606797749979)
@NLconstraint(m, e254, -sqrt((-0.9522420339595141 + x329)^2 + (
    -0.9326354363859527 + x330)^2 + (-0.4449382446418748 + x331)^2 + (
    -0.018772017414026565 + x332)^2 + (-0.1570753065990531 + x333)^2) + x254 -
    2.23606797749979 * b592 >= -2.23606797749979)
@NLconstraint(m, e255, -sqrt((-0.8796213188443197 + x329)^2 + (
    -0.9757325913906182 + x330)^2 + (-0.5478578093651233 + x331)^2 + (
    -0.00973548730106566 + x332)^2 + (-0.27048086044812103 + x333)^2) + x255 -
    2.23606797749979 * b593 >= -2.23606797749979)
@NLconstraint(m, e256, -sqrt((-0.7382526421375969 + x329)^2 + (
    -0.18734997029644274 + x330)^2 + (-0.2597432271723712 + x331)^2 + (
    -0.42962015792230956 + x332)^2 + (-0.7073477915737445 + x333)^2) + x256 -
    2.23606797749979 * b594 >= -2.23606797749979)
@NLconstraint(m, e257, -sqrt((-0.7480253586345234 + x329)^2 + (
    -0.39775488720466023 + x330)^2 + (-0.3653805995645427 + x331)^2 + (
    -0.5146776625112836 + x332)^2 + (-0.46172129982047827 + x333)^2) + x257 -
    2.23606797749979 * b595 >= -2.23606797749979)
@NLconstraint(m, e258, -sqrt((-0.9807955797704826 + x329)^2 + (
    -0.09734685184548297 + x330)^2 + (-0.38645671601793696 + x331)^2 + (
    -0.33263947083044576 + x332)^2 + (-0.5052803496499273 + x333)^2) + x258 -
    2.23606797749979 * b596 >= -2.23606797749979)
@NLconstraint(m, e259, -sqrt((-0.45084513414500904 + x334)^2 + (
    -0.4366195682760844 + x335)^2 + (-0.04163444585203002 + x336)^2 + (
    -0.7676272579584664 + x337)^2 + (-0.6734553564483233 + x338)^2) + x259 -
    2.23606797749979 * b597 >= -2.23606797749979)
@NLconstraint(m, e260, -sqrt((-0.670857540712527 + x334)^2 + (
    -0.472665488047444 + x335)^2 + (-0.672731114024884 + x336)^2 + (
    -0.8824812534975449 + x337)^2 + (-0.6920224414883532 + x338)^2) + x260 -
    2.23606797749979 * b598 >= -2.23606797749979)
@NLconstraint(m, e261, -sqrt((-0.3456424258652263 + x334)^2 + (
    -0.897323531600062 + x335)^2 + (-0.3169943908371815 + x336)^2 + (
    -0.08378401217902964 + x337)^2 + (-0.2511840930177276 + x338)^2) + x261 -
    2.23606797749979 * b599 >= -2.23606797749979)
@NLconstraint(m, e262, -sqrt((-0.49653521716587157 + x334)^2 + (
    -0.8612924863730758 + x335)^2 + (-0.3477168575425721 + x336)^2 + (
    -0.6615424192381595 + x337)^2 + (-0.2680635035686557 + x338)^2) + x262 -
    2.23606797749979 * b600 >= -2.23606797749979)
@NLconstraint(m, e263, -sqrt((-0.027492190735120214 + x334)^2 + (
    -0.975830678205581 + x335)^2 + (-0.5725079974762737 + x336)^2 + (
    -0.4627928206739904 + x337)^2 + (-0.676105217625283 + x338)^2) + x263 -
    2.23606797749979 * b601 >= -2.23606797749979)
@NLconstraint(m, e264, -sqrt((-0.13167765137927434 + x334)^2 + (
    -0.8772422533001436 + x335)^2 + (-0.30212459335273456 + x336)^2 + (
    -0.9589299306054163 + x337)^2 + (-0.1684676992378059 + x338)^2) + x264 -
    2.23606797749979 * b602 >= -2.23606797749979)
@NLconstraint(m, e265, -sqrt((-0.4631605820201776 + x334)^2 + (
    -0.3075046464306209 + x335)^2 + (-0.6161047422348818 + x336)^2 + (
    -0.06036679498995601 + x337)^2 + (-0.055585229920206314 + x338)^2) + x265
    - 2.23606797749979 * b603 >= -2.23606797749979)
@NLconstraint(m, e266, -sqrt((-0.32388656731438237 + x334)^2 + (
    -0.05792786993199972 + x335)^2 + (-0.8135525615007164 + x336)^2 + (
    -0.11918904488489845 + x337)^2 + (-0.3074172166187361 + x338)^2) + x266 -
    2.23606797749979 * b604 >= -2.23606797749979)
@NLconstraint(m, e267, -sqrt((-0.5224218716951496 + x334)^2 + (
    -0.11445496716294967 + x335)^2 + (-0.9526471232336744 + x336)^2 + (
    -0.29191369035574544 + x337)^2 + (-0.5653246839270838 + x338)^2) + x267 -
    2.23606797749979 * b605 >= -2.23606797749979)
@NLconstraint(m, e268, -sqrt((-0.21125847741287684 + x334)^2 + (
    -0.24527434539791804 + x335)^2 + (-0.6289970479606978 + x336)^2 + (
    -0.7068457529300446 + x337)^2 + (-0.7943561377121612 + x338)^2) + x268 -
    2.23606797749979 * b606 >= -2.23606797749979)
@NLconstraint(m, e269, -sqrt((-0.9522420339595141 + x334)^2 + (
    -0.9326354363859527 + x335)^2 + (-0.4449382446418748 + x336)^2 + (
    -0.018772017414026565 + x337)^2 + (-0.1570753065990531 + x338)^2) + x269 -
    2.23606797749979 * b607 >= -2.23606797749979)
@NLconstraint(m, e270, -sqrt((-0.8796213188443197 + x334)^2 + (
    -0.9757325913906182 + x335)^2 + (-0.5478578093651233 + x336)^2 + (
    -0.00973548730106566 + x337)^2 + (-0.27048086044812103 + x338)^2) + x270 -
    2.23606797749979 * b608 >= -2.23606797749979)
@NLconstraint(m, e271, -sqrt((-0.7382526421375969 + x334)^2 + (
    -0.18734997029644274 + x335)^2 + (-0.2597432271723712 + x336)^2 + (
    -0.42962015792230956 + x337)^2 + (-0.7073477915737445 + x338)^2) + x271 -
    2.23606797749979 * b609 >= -2.23606797749979)
@NLconstraint(m, e272, -sqrt((-0.7480253586345234 + x334)^2 + (
    -0.39775488720466023 + x335)^2 + (-0.3653805995645427 + x336)^2 + (
    -0.5146776625112836 + x337)^2 + (-0.46172129982047827 + x338)^2) + x272 -
    2.23606797749979 * b610 >= -2.23606797749979)
@NLconstraint(m, e273, -sqrt((-0.9807955797704826 + x334)^2 + (
    -0.09734685184548297 + x335)^2 + (-0.38645671601793696 + x336)^2 + (
    -0.33263947083044576 + x337)^2 + (-0.5052803496499273 + x338)^2) + x273 -
    2.23606797749979 * b611 >= -2.23606797749979)
@constraint(m, e274, b417 + b432 + b447 + b462 + b477 + b492 + b507 + b522 +
    b537 + b552 + b567 + b582 + b597 == 1)
@constraint(m, e275, b418 + b433 + b448 + b463 + b478 + b493 + b508 + b523 +
    b538 + b553 + b568 + b583 + b598 == 1)
@constraint(m, e276, b419 + b434 + b449 + b464 + b479 + b494 + b509 + b524 +
    b539 + b554 + b569 + b584 + b599 == 1)
@constraint(m, e277, b420 + b435 + b450 + b465 + b480 + b495 + b510 + b525 +
    b540 + b555 + b570 + b585 + b600 == 1)
@constraint(m, e278, b421 + b436 + b451 + b466 + b481 + b496 + b511 + b526 +
    b541 + b556 + b571 + b586 + b601 == 1)
@constraint(m, e279, b422 + b437 + b452 + b467 + b482 + b497 + b512 + b527 +
    b542 + b557 + b572 + b587 + b602 == 1)
@constraint(m, e280, b423 + b438 + b453 + b468 + b483 + b498 + b513 + b528 +
    b543 + b558 + b573 + b588 + b603 == 1)
@constraint(m, e281, b424 + b439 + b454 + b469 + b484 + b499 + b514 + b529 +
    b544 + b559 + b574 + b589 + b604 == 1)
@constraint(m, e282, b425 + b440 + b455 + b470 + b485 + b500 + b515 + b530 +
    b545 + b560 + b575 + b590 + b605 == 1)
@constraint(m, e283, b426 + b441 + b456 + b471 + b486 + b501 + b516 + b531 +
    b546 + b561 + b576 + b591 + b606 == 1)
@constraint(m, e284, b427 + b442 + b457 + b472 + b487 + b502 + b517 + b532 +
    b547 + b562 + b577 + b592 + b607 == 1)
@constraint(m, e285, b428 + b443 + b458 + b473 + b488 + b503 + b518 + b533 +
    b548 + b563 + b578 + b593 + b608 == 1)
@constraint(m, e286, b429 + b444 + b459 + b474 + b489 + b504 + b519 + b534 +
    b549 + b564 + b579 + b594 + b609 == 1)
@constraint(m, e287, b430 + b445 + b460 + b475 + b490 + b505 + b520 + b535 +
    b550 + b565 + b580 + b595 + b610 == 1)
@constraint(m, e288, b431 + b446 + b461 + b476 + b491 + b506 + b521 + b536 +
    b551 + b566 + b581 + b596 + b611 == 1)
@constraint(m, e289, b339 + b340 + b341 + b342 + b343 + b344 + b345 + b346 +
    b347 + b348 + b349 + b350 + b417 + b418 + b419 + b420 + b421 + b422 + b423
    + b424 + b425 + b426 + b427 + b428 + b429 + b430 + b431 == 3)
@constraint(m, e290, b339 + b351 + b352 + b353 + b354 + b355 + b356 + b357 +
    b358 + b359 + b360 + b361 + b432 + b433 + b434 + b435 + b436 + b437 + b438
    + b439 + b440 + b441 + b442 + b443 + b444 + b445 + b446 == 3)
@constraint(m, e291, b340 + b351 + b362 + b363 + b364 + b365 + b366 + b367 +
    b368 + b369 + b370 + b371 + b447 + b448 + b449 + b450 + b451 + b452 + b453
    + b454 + b455 + b456 + b457 + b458 + b459 + b460 + b461 == 3)
@constraint(m, e292, b341 + b352 + b362 + b372 + b373 + b374 + b375 + b376 +
    b377 + b378 + b379 + b380 + b462 + b463 + b464 + b465 + b466 + b467 + b468
    + b469 + b470 + b471 + b472 + b473 + b474 + b475 + b476 == 3)
@constraint(m, e293, b342 + b353 + b363 + b372 + b381 + b382 + b383 + b384 +
    b385 + b386 + b387 + b388 + b477 + b478 + b479 + b480 + b481 + b482 + b483
    + b484 + b485 + b486 + b487 + b488 + b489 + b490 + b491 == 3)
@constraint(m, e294, b343 + b354 + b364 + b373 + b381 + b389 + b390 + b391 +
    b392 + b393 + b394 + b395 + b492 + b493 + b494 + b495 + b496 + b497 + b498
    + b499 + b500 + b501 + b502 + b503 + b504 + b505 + b506 == 3)
@constraint(m, e295, b344 + b355 + b365 + b374 + b382 + b389 + b396 + b397 +
    b398 + b399 + b400 + b401 + b507 + b508 + b509 + b510 + b511 + b512 + b513
    + b514 + b515 + b516 + b517 + b518 + b519 + b520 + b521 == 3)
@constraint(m, e296, b345 + b356 + b366 + b375 + b383 + b390 + b396 + b402 +
    b403 + b404 + b405 + b406 + b522 + b523 + b524 + b525 + b526 + b527 + b528
    + b529 + b530 + b531 + b532 + b533 + b534 + b535 + b536 == 3)
@constraint(m, e297, b346 + b357 + b367 + b376 + b384 + b391 + b397 + b402 +
    b407 + b408 + b409 + b410 + b537 + b538 + b539 + b540 + b541 + b542 + b543
    + b544 + b545 + b546 + b547 + b548 + b549 + b550 + b551 == 3)
@constraint(m, e298, b347 + b358 + b368 + b377 + b385 + b392 + b398 + b403 +
    b407 + b411 + b412 + b413 + b552 + b553 + b554 + b555 + b556 + b557 + b558
    + b559 + b560 + b561 + b562 + b563 + b564 + b565 + b566 == 3)
@constraint(m, e299, b348 + b359 + b369 + b378 + b386 + b393 + b399 + b404 +
    b408 + b411 + b414 + b415 + b567 + b568 + b569 + b570 + b571 + b572 + b573
    + b574 + b575 + b576 + b577 + b578 + b579 + b580 + b581 == 3)
@constraint(m, e300, b349 + b360 + b370 + b379 + b387 + b394 + b400 + b405 +
    b409 + b412 + b414 + b416 + b582 + b583 + b584 + b585 + b586 + b587 + b588
    + b589 + b590 + b591 + b592 + b593 + b594 + b595 + b596 == 3)
@constraint(m, e301, b350 + b361 + b371 + b380 + b388 + b395 + b401 + b406 +
    b410 + b413 + b415 + b416 + b597 + b598 + b599 + b600 + b601 + b602 + b603
    + b604 + b605 + b606 + b607 + b608 + b609 + b610 + b611 == 3)
@constraint(m, e302, b339 == 1)
@constraint(m, e303, b340 + b351 == 1)
@constraint(m, e304, b341 + b352 + b362 == 1)
@constraint(m, e305, b342 + b353 + b363 + b372 == 1)
@constraint(m, e306, b343 + b354 + b364 + b373 + b381 == 1)
@constraint(m, e307, b344 + b355 + b365 + b374 + b382 + b389 == 1)
@constraint(m, e308, b345 + b356 + b366 + b375 + b383 + b390 + b396 == 1)
@constraint(m, e309, b346 + b357 + b367 + b376 + b384 + b391 + b397 + b402
    == 1)
@constraint(m, e310, b347 + b358 + b368 + b377 + b385 + b392 + b398 + b403 +
    b407 == 1)
@constraint(m, e311, b348 + b359 + b369 + b378 + b386 + b393 + b399 + b404 +
    b408 + b411 == 1)
@constraint(m, e312, b349 + b360 + b370 + b379 + b387 + b394 + b400 + b405 +
    b409 + b412 + b414 == 1)
@constraint(m, e313, b350 + b361 + b371 + b380 + b388 + b395 + b401 + b406 +
    b410 + b413 + b415 + b416 == 1)
