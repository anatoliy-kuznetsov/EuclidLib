# MINLP written by GAMS Convert at 05/15/24 11:58:01
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       313       40      273        0        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#       585      312      273        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#      2223     1170     1053
#
# Reformulation has removed 1 variable and 1 equation

using JuMP
using MathOptInterface
const MOI = MathOptInterface

model = m = Model()

@variable(m, 0 <= x1 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x2 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x3 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x4 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x5 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x6 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x7 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x8 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x9 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x10 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x11 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x12 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x13 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x14 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x15 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x16 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x17 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x18 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x19 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x20 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x21 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x22 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x23 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x24 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x25 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x26 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x27 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x28 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x29 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x30 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x31 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x32 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x33 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x34 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x35 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x36 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x37 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x38 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x39 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x40 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x41 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x42 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x43 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x44 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x45 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x46 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x47 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x48 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x49 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x50 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x51 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x52 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x53 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x54 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x55 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x56 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x57 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x58 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x59 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x60 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x61 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x62 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x63 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x64 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x65 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x66 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x67 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x68 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x69 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x70 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x71 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x72 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x73 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x74 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x75 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x76 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x77 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x78 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x79 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x80 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x81 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x82 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x83 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x84 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x85 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x86 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x87 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x88 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x89 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x90 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x91 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x92 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x93 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x94 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x95 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x96 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x97 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x98 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x99 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x100 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x101 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x102 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x103 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x104 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x105 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x106 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x107 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x108 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x109 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x110 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x111 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x112 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x113 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x114 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x115 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x116 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x117 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x118 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x119 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x120 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x121 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x122 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x123 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x124 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x125 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x126 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x127 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x128 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x129 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x130 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x131 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x132 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x133 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x134 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x135 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x136 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x137 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x138 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x139 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x140 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x141 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x142 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x143 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x144 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x145 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x146 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x147 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x148 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x149 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x150 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x151 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x152 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x153 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x154 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x155 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x156 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x157 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x158 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x159 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x160 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x161 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x162 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x163 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x164 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x165 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x166 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x167 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x168 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x169 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x170 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x171 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x172 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x173 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x174 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x175 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x176 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x177 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x178 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x179 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x180 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x181 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x182 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x183 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x184 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x185 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x186 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x187 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x188 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x189 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x190 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x191 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x192 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x193 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x194 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x195 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x196 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x197 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x198 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x199 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x200 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x201 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x202 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x203 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x204 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x205 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x206 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x207 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x208 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x209 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x210 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x211 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x212 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x213 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x214 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x215 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x216 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x217 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x218 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x219 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x220 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x221 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x222 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x223 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x224 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x225 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x226 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x227 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x228 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x229 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x230 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x231 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x232 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x233 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x234 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x235 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x236 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x237 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x238 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x239 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x240 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x241 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x242 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x243 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x244 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x245 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x246 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x247 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x248 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x249 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x250 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x251 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x252 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x253 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x254 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x255 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x256 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x257 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x258 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x259 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x260 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x261 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x262 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x263 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x264 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x265 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x266 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x267 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x268 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x269 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x270 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x271 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x272 <= 1.7320508075688772, start=0)
@variable(m, 0 <= x273 <= 1.7320508075688772, start=0)
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
@variable(m, 0 <= b313 <= 1, binary=true, start=0)
@variable(m, 0 <= b314 <= 1, binary=true, start=0)
@variable(m, 0 <= b315 <= 1, binary=true, start=0)
@variable(m, 0 <= b316 <= 1, binary=true, start=0)
@variable(m, 0 <= b317 <= 1, binary=true, start=0)
@variable(m, 0 <= b318 <= 1, binary=true, start=0)
@variable(m, 0 <= b319 <= 1, binary=true, start=0)
@variable(m, 0 <= b320 <= 1, binary=true, start=0)
@variable(m, 0 <= b321 <= 1, binary=true, start=0)
@variable(m, 0 <= b322 <= 1, binary=true, start=0)
@variable(m, 0 <= b323 <= 1, binary=true, start=0)
@variable(m, 0 <= b324 <= 1, binary=true, start=0)
@variable(m, 0 <= b325 <= 1, binary=true, start=0)
@variable(m, 0 <= b326 <= 1, binary=true, start=0)
@variable(m, 0 <= b327 <= 1, binary=true, start=0)
@variable(m, 0 <= b328 <= 1, binary=true, start=0)
@variable(m, 0 <= b329 <= 1, binary=true, start=0)
@variable(m, 0 <= b330 <= 1, binary=true, start=0)
@variable(m, 0 <= b331 <= 1, binary=true, start=0)
@variable(m, 0 <= b332 <= 1, binary=true, start=0)
@variable(m, 0 <= b333 <= 1, binary=true, start=0)
@variable(m, 0 <= b334 <= 1, binary=true, start=0)
@variable(m, 0 <= b335 <= 1, binary=true, start=0)
@variable(m, 0 <= b336 <= 1, binary=true, start=0)
@variable(m, 0 <= b337 <= 1, binary=true, start=0)
@variable(m, 0 <= b338 <= 1, binary=true, start=0)
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

@NLconstraint(m, e1, -sqrt((x274 - x277)^2 + (x275 - x278)^2 + (x276 - x279)^2)
    + x1 - 1.7320508075688772 * b313 >= -1.7320508075688772)
@NLconstraint(m, e2, -sqrt((x274 - x280)^2 + (x275 - x281)^2 + (x276 - x282)^2)
    + x2 - 1.7320508075688772 * b314 >= -1.7320508075688772)
@NLconstraint(m, e3, -sqrt((x274 - x283)^2 + (x275 - x284)^2 + (x276 - x285)^2)
    + x3 - 1.7320508075688772 * b315 >= -1.7320508075688772)
@NLconstraint(m, e4, -sqrt((x274 - x286)^2 + (x275 - x287)^2 + (x276 - x288)^2)
    + x4 - 1.7320508075688772 * b316 >= -1.7320508075688772)
@NLconstraint(m, e5, -sqrt((x274 - x289)^2 + (x275 - x290)^2 + (x276 - x291)^2)
    + x5 - 1.7320508075688772 * b317 >= -1.7320508075688772)
@NLconstraint(m, e6, -sqrt((x274 - x292)^2 + (x275 - x293)^2 + (x276 - x294)^2)
    + x6 - 1.7320508075688772 * b318 >= -1.7320508075688772)
@NLconstraint(m, e7, -sqrt((x274 - x295)^2 + (x275 - x296)^2 + (x276 - x297)^2)
    + x7 - 1.7320508075688772 * b319 >= -1.7320508075688772)
@NLconstraint(m, e8, -sqrt((x274 - x298)^2 + (x275 - x299)^2 + (x276 - x300)^2)
    + x8 - 1.7320508075688772 * b320 >= -1.7320508075688772)
@NLconstraint(m, e9, -sqrt((x274 - x301)^2 + (x275 - x302)^2 + (x276 - x303)^2)
    + x9 - 1.7320508075688772 * b321 >= -1.7320508075688772)
@NLconstraint(m, e10, -sqrt((x274 - x304)^2 + (x275 - x305)^2 + (x276 - x306)^2)
    + x10 - 1.7320508075688772 * b322 >= -1.7320508075688772)
@NLconstraint(m, e11, -sqrt((x274 - x307)^2 + (x275 - x308)^2 + (x276 - x309)^2)
    + x11 - 1.7320508075688772 * b323 >= -1.7320508075688772)
@NLconstraint(m, e12, -sqrt((x274 - x310)^2 + (x275 - x311)^2 + (x276 - x312)^2)
    + x12 - 1.7320508075688772 * b324 >= -1.7320508075688772)
@NLconstraint(m, e13, -sqrt((x277 - x280)^2 + (x278 - x281)^2 + (x279 - x282)^2)
    + x13 - 1.7320508075688772 * b325 >= -1.7320508075688772)
@NLconstraint(m, e14, -sqrt((x277 - x283)^2 + (x278 - x284)^2 + (x279 - x285)^2)
    + x14 - 1.7320508075688772 * b326 >= -1.7320508075688772)
@NLconstraint(m, e15, -sqrt((x277 - x286)^2 + (x278 - x287)^2 + (x279 - x288)^2)
    + x15 - 1.7320508075688772 * b327 >= -1.7320508075688772)
@NLconstraint(m, e16, -sqrt((x277 - x289)^2 + (x278 - x290)^2 + (x279 - x291)^2)
    + x16 - 1.7320508075688772 * b328 >= -1.7320508075688772)
@NLconstraint(m, e17, -sqrt((x277 - x292)^2 + (x278 - x293)^2 + (x279 - x294)^2)
    + x17 - 1.7320508075688772 * b329 >= -1.7320508075688772)
@NLconstraint(m, e18, -sqrt((x277 - x295)^2 + (x278 - x296)^2 + (x279 - x297)^2)
    + x18 - 1.7320508075688772 * b330 >= -1.7320508075688772)
@NLconstraint(m, e19, -sqrt((x277 - x298)^2 + (x278 - x299)^2 + (x279 - x300)^2)
    + x19 - 1.7320508075688772 * b331 >= -1.7320508075688772)
@NLconstraint(m, e20, -sqrt((x277 - x301)^2 + (x278 - x302)^2 + (x279 - x303)^2)
    + x20 - 1.7320508075688772 * b332 >= -1.7320508075688772)
@NLconstraint(m, e21, -sqrt((x277 - x304)^2 + (x278 - x305)^2 + (x279 - x306)^2)
    + x21 - 1.7320508075688772 * b333 >= -1.7320508075688772)
@NLconstraint(m, e22, -sqrt((x277 - x307)^2 + (x278 - x308)^2 + (x279 - x309)^2)
    + x22 - 1.7320508075688772 * b334 >= -1.7320508075688772)
@NLconstraint(m, e23, -sqrt((x277 - x310)^2 + (x278 - x311)^2 + (x279 - x312)^2)
    + x23 - 1.7320508075688772 * b335 >= -1.7320508075688772)
@NLconstraint(m, e24, -sqrt((x280 - x283)^2 + (x281 - x284)^2 + (x282 - x285)^2)
    + x24 - 1.7320508075688772 * b336 >= -1.7320508075688772)
@NLconstraint(m, e25, -sqrt((x280 - x286)^2 + (x281 - x287)^2 + (x282 - x288)^2)
    + x25 - 1.7320508075688772 * b337 >= -1.7320508075688772)
@NLconstraint(m, e26, -sqrt((x280 - x289)^2 + (x281 - x290)^2 + (x282 - x291)^2)
    + x26 - 1.7320508075688772 * b338 >= -1.7320508075688772)
@NLconstraint(m, e27, -sqrt((x280 - x292)^2 + (x281 - x293)^2 + (x282 - x294)^2)
    + x27 - 1.7320508075688772 * b339 >= -1.7320508075688772)
@NLconstraint(m, e28, -sqrt((x280 - x295)^2 + (x281 - x296)^2 + (x282 - x297)^2)
    + x28 - 1.7320508075688772 * b340 >= -1.7320508075688772)
@NLconstraint(m, e29, -sqrt((x280 - x298)^2 + (x281 - x299)^2 + (x282 - x300)^2)
    + x29 - 1.7320508075688772 * b341 >= -1.7320508075688772)
@NLconstraint(m, e30, -sqrt((x280 - x301)^2 + (x281 - x302)^2 + (x282 - x303)^2)
    + x30 - 1.7320508075688772 * b342 >= -1.7320508075688772)
@NLconstraint(m, e31, -sqrt((x280 - x304)^2 + (x281 - x305)^2 + (x282 - x306)^2)
    + x31 - 1.7320508075688772 * b343 >= -1.7320508075688772)
@NLconstraint(m, e32, -sqrt((x280 - x307)^2 + (x281 - x308)^2 + (x282 - x309)^2)
    + x32 - 1.7320508075688772 * b344 >= -1.7320508075688772)
@NLconstraint(m, e33, -sqrt((x280 - x310)^2 + (x281 - x311)^2 + (x282 - x312)^2)
    + x33 - 1.7320508075688772 * b345 >= -1.7320508075688772)
@NLconstraint(m, e34, -sqrt((x283 - x286)^2 + (x284 - x287)^2 + (x285 - x288)^2)
    + x34 - 1.7320508075688772 * b346 >= -1.7320508075688772)
@NLconstraint(m, e35, -sqrt((x283 - x289)^2 + (x284 - x290)^2 + (x285 - x291)^2)
    + x35 - 1.7320508075688772 * b347 >= -1.7320508075688772)
@NLconstraint(m, e36, -sqrt((x283 - x292)^2 + (x284 - x293)^2 + (x285 - x294)^2)
    + x36 - 1.7320508075688772 * b348 >= -1.7320508075688772)
@NLconstraint(m, e37, -sqrt((x283 - x295)^2 + (x284 - x296)^2 + (x285 - x297)^2)
    + x37 - 1.7320508075688772 * b349 >= -1.7320508075688772)
@NLconstraint(m, e38, -sqrt((x283 - x298)^2 + (x284 - x299)^2 + (x285 - x300)^2)
    + x38 - 1.7320508075688772 * b350 >= -1.7320508075688772)
@NLconstraint(m, e39, -sqrt((x283 - x301)^2 + (x284 - x302)^2 + (x285 - x303)^2)
    + x39 - 1.7320508075688772 * b351 >= -1.7320508075688772)
@NLconstraint(m, e40, -sqrt((x283 - x304)^2 + (x284 - x305)^2 + (x285 - x306)^2)
    + x40 - 1.7320508075688772 * b352 >= -1.7320508075688772)
@NLconstraint(m, e41, -sqrt((x283 - x307)^2 + (x284 - x308)^2 + (x285 - x309)^2)
    + x41 - 1.7320508075688772 * b353 >= -1.7320508075688772)
@NLconstraint(m, e42, -sqrt((x283 - x310)^2 + (x284 - x311)^2 + (x285 - x312)^2)
    + x42 - 1.7320508075688772 * b354 >= -1.7320508075688772)
@NLconstraint(m, e43, -sqrt((x286 - x289)^2 + (x287 - x290)^2 + (x288 - x291)^2)
    + x43 - 1.7320508075688772 * b355 >= -1.7320508075688772)
@NLconstraint(m, e44, -sqrt((x286 - x292)^2 + (x287 - x293)^2 + (x288 - x294)^2)
    + x44 - 1.7320508075688772 * b356 >= -1.7320508075688772)
@NLconstraint(m, e45, -sqrt((x286 - x295)^2 + (x287 - x296)^2 + (x288 - x297)^2)
    + x45 - 1.7320508075688772 * b357 >= -1.7320508075688772)
@NLconstraint(m, e46, -sqrt((x286 - x298)^2 + (x287 - x299)^2 + (x288 - x300)^2)
    + x46 - 1.7320508075688772 * b358 >= -1.7320508075688772)
@NLconstraint(m, e47, -sqrt((x286 - x301)^2 + (x287 - x302)^2 + (x288 - x303)^2)
    + x47 - 1.7320508075688772 * b359 >= -1.7320508075688772)
@NLconstraint(m, e48, -sqrt((x286 - x304)^2 + (x287 - x305)^2 + (x288 - x306)^2)
    + x48 - 1.7320508075688772 * b360 >= -1.7320508075688772)
@NLconstraint(m, e49, -sqrt((x286 - x307)^2 + (x287 - x308)^2 + (x288 - x309)^2)
    + x49 - 1.7320508075688772 * b361 >= -1.7320508075688772)
@NLconstraint(m, e50, -sqrt((x286 - x310)^2 + (x287 - x311)^2 + (x288 - x312)^2)
    + x50 - 1.7320508075688772 * b362 >= -1.7320508075688772)
@NLconstraint(m, e51, -sqrt((x289 - x292)^2 + (x290 - x293)^2 + (x291 - x294)^2)
    + x51 - 1.7320508075688772 * b363 >= -1.7320508075688772)
@NLconstraint(m, e52, -sqrt((x289 - x295)^2 + (x290 - x296)^2 + (x291 - x297)^2)
    + x52 - 1.7320508075688772 * b364 >= -1.7320508075688772)
@NLconstraint(m, e53, -sqrt((x289 - x298)^2 + (x290 - x299)^2 + (x291 - x300)^2)
    + x53 - 1.7320508075688772 * b365 >= -1.7320508075688772)
@NLconstraint(m, e54, -sqrt((x289 - x301)^2 + (x290 - x302)^2 + (x291 - x303)^2)
    + x54 - 1.7320508075688772 * b366 >= -1.7320508075688772)
@NLconstraint(m, e55, -sqrt((x289 - x304)^2 + (x290 - x305)^2 + (x291 - x306)^2)
    + x55 - 1.7320508075688772 * b367 >= -1.7320508075688772)
@NLconstraint(m, e56, -sqrt((x289 - x307)^2 + (x290 - x308)^2 + (x291 - x309)^2)
    + x56 - 1.7320508075688772 * b368 >= -1.7320508075688772)
@NLconstraint(m, e57, -sqrt((x289 - x310)^2 + (x290 - x311)^2 + (x291 - x312)^2)
    + x57 - 1.7320508075688772 * b369 >= -1.7320508075688772)
@NLconstraint(m, e58, -sqrt((x292 - x295)^2 + (x293 - x296)^2 + (x294 - x297)^2)
    + x58 - 1.7320508075688772 * b370 >= -1.7320508075688772)
@NLconstraint(m, e59, -sqrt((x292 - x298)^2 + (x293 - x299)^2 + (x294 - x300)^2)
    + x59 - 1.7320508075688772 * b371 >= -1.7320508075688772)
@NLconstraint(m, e60, -sqrt((x292 - x301)^2 + (x293 - x302)^2 + (x294 - x303)^2)
    + x60 - 1.7320508075688772 * b372 >= -1.7320508075688772)
@NLconstraint(m, e61, -sqrt((x292 - x304)^2 + (x293 - x305)^2 + (x294 - x306)^2)
    + x61 - 1.7320508075688772 * b373 >= -1.7320508075688772)
@NLconstraint(m, e62, -sqrt((x292 - x307)^2 + (x293 - x308)^2 + (x294 - x309)^2)
    + x62 - 1.7320508075688772 * b374 >= -1.7320508075688772)
@NLconstraint(m, e63, -sqrt((x292 - x310)^2 + (x293 - x311)^2 + (x294 - x312)^2)
    + x63 - 1.7320508075688772 * b375 >= -1.7320508075688772)
@NLconstraint(m, e64, -sqrt((x295 - x298)^2 + (x296 - x299)^2 + (x297 - x300)^2)
    + x64 - 1.7320508075688772 * b376 >= -1.7320508075688772)
@NLconstraint(m, e65, -sqrt((x295 - x301)^2 + (x296 - x302)^2 + (x297 - x303)^2)
    + x65 - 1.7320508075688772 * b377 >= -1.7320508075688772)
@NLconstraint(m, e66, -sqrt((x295 - x304)^2 + (x296 - x305)^2 + (x297 - x306)^2)
    + x66 - 1.7320508075688772 * b378 >= -1.7320508075688772)
@NLconstraint(m, e67, -sqrt((x295 - x307)^2 + (x296 - x308)^2 + (x297 - x309)^2)
    + x67 - 1.7320508075688772 * b379 >= -1.7320508075688772)
@NLconstraint(m, e68, -sqrt((x295 - x310)^2 + (x296 - x311)^2 + (x297 - x312)^2)
    + x68 - 1.7320508075688772 * b380 >= -1.7320508075688772)
@NLconstraint(m, e69, -sqrt((x298 - x301)^2 + (x299 - x302)^2 + (x300 - x303)^2)
    + x69 - 1.7320508075688772 * b381 >= -1.7320508075688772)
@NLconstraint(m, e70, -sqrt((x298 - x304)^2 + (x299 - x305)^2 + (x300 - x306)^2)
    + x70 - 1.7320508075688772 * b382 >= -1.7320508075688772)
@NLconstraint(m, e71, -sqrt((x298 - x307)^2 + (x299 - x308)^2 + (x300 - x309)^2)
    + x71 - 1.7320508075688772 * b383 >= -1.7320508075688772)
@NLconstraint(m, e72, -sqrt((x298 - x310)^2 + (x299 - x311)^2 + (x300 - x312)^2)
    + x72 - 1.7320508075688772 * b384 >= -1.7320508075688772)
@NLconstraint(m, e73, -sqrt((x301 - x304)^2 + (x302 - x305)^2 + (x303 - x306)^2)
    + x73 - 1.7320508075688772 * b385 >= -1.7320508075688772)
@NLconstraint(m, e74, -sqrt((x301 - x307)^2 + (x302 - x308)^2 + (x303 - x309)^2)
    + x74 - 1.7320508075688772 * b386 >= -1.7320508075688772)
@NLconstraint(m, e75, -sqrt((x301 - x310)^2 + (x302 - x311)^2 + (x303 - x312)^2)
    + x75 - 1.7320508075688772 * b387 >= -1.7320508075688772)
@NLconstraint(m, e76, -sqrt((x304 - x307)^2 + (x305 - x308)^2 + (x306 - x309)^2)
    + x76 - 1.7320508075688772 * b388 >= -1.7320508075688772)
@NLconstraint(m, e77, -sqrt((x304 - x310)^2 + (x305 - x311)^2 + (x306 - x312)^2)
    + x77 - 1.7320508075688772 * b389 >= -1.7320508075688772)
@NLconstraint(m, e78, -sqrt((x307 - x310)^2 + (x308 - x311)^2 + (x309 - x312)^2)
    + x78 - 1.7320508075688772 * b390 >= -1.7320508075688772)
@NLconstraint(m, e79, -sqrt((-0.2718754143840908 + x274)^2 + (
    -0.48802820785090784 + x275)^2 + (-0.08187934237116656 + x276)^2) + x79 -
    1.7320508075688772 * b391 >= -1.7320508075688772)
@NLconstraint(m, e80, -sqrt((-0.33873348699206973 + x274)^2 + (
    -0.07233360770535402 + x275)^2 + (-0.011036367079899967 + x276)^2) + x80 -
    1.7320508075688772 * b392 >= -1.7320508075688772)
@NLconstraint(m, e81, -sqrt((-0.28385029589876865 + x274)^2 + (
    -0.11770636555802805 + x275)^2 + (-0.3110382248120007 + x276)^2) + x81 -
    1.7320508075688772 * b393 >= -1.7320508075688772)
@NLconstraint(m, e82, -sqrt((-0.7434707928397064 + x274)^2 + (
    -0.0357557155126923 + x275)^2 + (-0.6249375571804716 + x276)^2) + x82 -
    1.7320508075688772 * b394 >= -1.7320508075688772)
@NLconstraint(m, e83, -sqrt((-0.13501116090704035 + x274)^2 + (
    -0.7950712434655829 + x275)^2 + (-0.7369676243821022 + x276)^2) + x83 -
    1.7320508075688772 * b395 >= -1.7320508075688772)
@NLconstraint(m, e84, -sqrt((-0.21101029956774453 + x274)^2 + (
    -0.8480765801722641 + x275)^2 + (-0.7173017220824032 + x276)^2) + x84 -
    1.7320508075688772 * b396 >= -1.7320508075688772)
@NLconstraint(m, e85, -sqrt((-0.07495132545320449 + x274)^2 + (
    -0.4081313844234159 + x275)^2 + (-0.7004510913580178 + x276)^2) + x85 -
    1.7320508075688772 * b397 >= -1.7320508075688772)
@NLconstraint(m, e86, -sqrt((-0.9229582476032371 + x274)^2 + (
    -0.17221119493742953 + x275)^2 + (-0.2518629905323574 + x276)^2) + x86 -
    1.7320508075688772 * b398 >= -1.7320508075688772)
@NLconstraint(m, e87, -sqrt((-0.7750929946094214 + x274)^2 + (
    -0.9626723030210862 + x275)^2 + (-0.09375460752394849 + x276)^2) + x87 -
    1.7320508075688772 * b399 >= -1.7320508075688772)
@NLconstraint(m, e88, -sqrt((-0.08982827530229975 + x274)^2 + (
    -0.7511793846525663 + x275)^2 + (-0.3169893159261734 + x276)^2) + x88 -
    1.7320508075688772 * b400 >= -1.7320508075688772)
@NLconstraint(m, e89, -sqrt((-0.38677647485720235 + x274)^2 + (
    -0.87633207391825 + x275)^2 + (-0.7457995156246497 + x276)^2) + x89 -
    1.7320508075688772 * b401 >= -1.7320508075688772)
@NLconstraint(m, e90, -sqrt((-0.6607159863179267 + x274)^2 + (
    -0.8676520260577261 + x275)^2 + (-0.7320438297162596 + x276)^2) + x90 -
    1.7320508075688772 * b402 >= -1.7320508075688772)
@NLconstraint(m, e91, -sqrt((-0.8102488868102232 + x274)^2 + (
    -0.6432507057061979 + x275)^2 + (-0.5931582872810908 + x276)^2) + x91 -
    1.7320508075688772 * b403 >= -1.7320508075688772)
@NLconstraint(m, e92, -sqrt((-0.05986505368858752 + x274)^2 + (
    -0.909611607891918 + x275)^2 + (-0.9117643699770345 + x276)^2) + x92 -
    1.7320508075688772 * b404 >= -1.7320508075688772)
@NLconstraint(m, e93, -sqrt((-0.35134351369704286 + x274)^2 + (
    -0.6263463928446534 + x275)^2 + (-0.01689904369168782 + x276)^2) + x93 -
    1.7320508075688772 * b405 >= -1.7320508075688772)
@NLconstraint(m, e94, -sqrt((-0.2718754143840908 + x277)^2 + (
    -0.48802820785090784 + x278)^2 + (-0.08187934237116656 + x279)^2) + x94 -
    1.7320508075688772 * b406 >= -1.7320508075688772)
@NLconstraint(m, e95, -sqrt((-0.33873348699206973 + x277)^2 + (
    -0.07233360770535402 + x278)^2 + (-0.011036367079899967 + x279)^2) + x95 -
    1.7320508075688772 * b407 >= -1.7320508075688772)
@NLconstraint(m, e96, -sqrt((-0.28385029589876865 + x277)^2 + (
    -0.11770636555802805 + x278)^2 + (-0.3110382248120007 + x279)^2) + x96 -
    1.7320508075688772 * b408 >= -1.7320508075688772)
@NLconstraint(m, e97, -sqrt((-0.7434707928397064 + x277)^2 + (
    -0.0357557155126923 + x278)^2 + (-0.6249375571804716 + x279)^2) + x97 -
    1.7320508075688772 * b409 >= -1.7320508075688772)
@NLconstraint(m, e98, -sqrt((-0.13501116090704035 + x277)^2 + (
    -0.7950712434655829 + x278)^2 + (-0.7369676243821022 + x279)^2) + x98 -
    1.7320508075688772 * b410 >= -1.7320508075688772)
@NLconstraint(m, e99, -sqrt((-0.21101029956774453 + x277)^2 + (
    -0.8480765801722641 + x278)^2 + (-0.7173017220824032 + x279)^2) + x99 -
    1.7320508075688772 * b411 >= -1.7320508075688772)
@NLconstraint(m, e100, -sqrt((-0.07495132545320449 + x277)^2 + (
    -0.4081313844234159 + x278)^2 + (-0.7004510913580178 + x279)^2) + x100 -
    1.7320508075688772 * b412 >= -1.7320508075688772)
@NLconstraint(m, e101, -sqrt((-0.9229582476032371 + x277)^2 + (
    -0.17221119493742953 + x278)^2 + (-0.2518629905323574 + x279)^2) + x101 -
    1.7320508075688772 * b413 >= -1.7320508075688772)
@NLconstraint(m, e102, -sqrt((-0.7750929946094214 + x277)^2 + (
    -0.9626723030210862 + x278)^2 + (-0.09375460752394849 + x279)^2) + x102 -
    1.7320508075688772 * b414 >= -1.7320508075688772)
@NLconstraint(m, e103, -sqrt((-0.08982827530229975 + x277)^2 + (
    -0.7511793846525663 + x278)^2 + (-0.3169893159261734 + x279)^2) + x103 -
    1.7320508075688772 * b415 >= -1.7320508075688772)
@NLconstraint(m, e104, -sqrt((-0.38677647485720235 + x277)^2 + (
    -0.87633207391825 + x278)^2 + (-0.7457995156246497 + x279)^2) + x104 -
    1.7320508075688772 * b416 >= -1.7320508075688772)
@NLconstraint(m, e105, -sqrt((-0.6607159863179267 + x277)^2 + (
    -0.8676520260577261 + x278)^2 + (-0.7320438297162596 + x279)^2) + x105 -
    1.7320508075688772 * b417 >= -1.7320508075688772)
@NLconstraint(m, e106, -sqrt((-0.8102488868102232 + x277)^2 + (
    -0.6432507057061979 + x278)^2 + (-0.5931582872810908 + x279)^2) + x106 -
    1.7320508075688772 * b418 >= -1.7320508075688772)
@NLconstraint(m, e107, -sqrt((-0.05986505368858752 + x277)^2 + (
    -0.909611607891918 + x278)^2 + (-0.9117643699770345 + x279)^2) + x107 -
    1.7320508075688772 * b419 >= -1.7320508075688772)
@NLconstraint(m, e108, -sqrt((-0.35134351369704286 + x277)^2 + (
    -0.6263463928446534 + x278)^2 + (-0.01689904369168782 + x279)^2) + x108 -
    1.7320508075688772 * b420 >= -1.7320508075688772)
@NLconstraint(m, e109, -sqrt((-0.2718754143840908 + x280)^2 + (
    -0.48802820785090784 + x281)^2 + (-0.08187934237116656 + x282)^2) + x109 -
    1.7320508075688772 * b421 >= -1.7320508075688772)
@NLconstraint(m, e110, -sqrt((-0.33873348699206973 + x280)^2 + (
    -0.07233360770535402 + x281)^2 + (-0.011036367079899967 + x282)^2) + x110
    - 1.7320508075688772 * b422 >= -1.7320508075688772)
@NLconstraint(m, e111, -sqrt((-0.28385029589876865 + x280)^2 + (
    -0.11770636555802805 + x281)^2 + (-0.3110382248120007 + x282)^2) + x111 -
    1.7320508075688772 * b423 >= -1.7320508075688772)
@NLconstraint(m, e112, -sqrt((-0.7434707928397064 + x280)^2 + (
    -0.0357557155126923 + x281)^2 + (-0.6249375571804716 + x282)^2) + x112 -
    1.7320508075688772 * b424 >= -1.7320508075688772)
@NLconstraint(m, e113, -sqrt((-0.13501116090704035 + x280)^2 + (
    -0.7950712434655829 + x281)^2 + (-0.7369676243821022 + x282)^2) + x113 -
    1.7320508075688772 * b425 >= -1.7320508075688772)
@NLconstraint(m, e114, -sqrt((-0.21101029956774453 + x280)^2 + (
    -0.8480765801722641 + x281)^2 + (-0.7173017220824032 + x282)^2) + x114 -
    1.7320508075688772 * b426 >= -1.7320508075688772)
@NLconstraint(m, e115, -sqrt((-0.07495132545320449 + x280)^2 + (
    -0.4081313844234159 + x281)^2 + (-0.7004510913580178 + x282)^2) + x115 -
    1.7320508075688772 * b427 >= -1.7320508075688772)
@NLconstraint(m, e116, -sqrt((-0.9229582476032371 + x280)^2 + (
    -0.17221119493742953 + x281)^2 + (-0.2518629905323574 + x282)^2) + x116 -
    1.7320508075688772 * b428 >= -1.7320508075688772)
@NLconstraint(m, e117, -sqrt((-0.7750929946094214 + x280)^2 + (
    -0.9626723030210862 + x281)^2 + (-0.09375460752394849 + x282)^2) + x117 -
    1.7320508075688772 * b429 >= -1.7320508075688772)
@NLconstraint(m, e118, -sqrt((-0.08982827530229975 + x280)^2 + (
    -0.7511793846525663 + x281)^2 + (-0.3169893159261734 + x282)^2) + x118 -
    1.7320508075688772 * b430 >= -1.7320508075688772)
@NLconstraint(m, e119, -sqrt((-0.38677647485720235 + x280)^2 + (
    -0.87633207391825 + x281)^2 + (-0.7457995156246497 + x282)^2) + x119 -
    1.7320508075688772 * b431 >= -1.7320508075688772)
@NLconstraint(m, e120, -sqrt((-0.6607159863179267 + x280)^2 + (
    -0.8676520260577261 + x281)^2 + (-0.7320438297162596 + x282)^2) + x120 -
    1.7320508075688772 * b432 >= -1.7320508075688772)
@NLconstraint(m, e121, -sqrt((-0.8102488868102232 + x280)^2 + (
    -0.6432507057061979 + x281)^2 + (-0.5931582872810908 + x282)^2) + x121 -
    1.7320508075688772 * b433 >= -1.7320508075688772)
@NLconstraint(m, e122, -sqrt((-0.05986505368858752 + x280)^2 + (
    -0.909611607891918 + x281)^2 + (-0.9117643699770345 + x282)^2) + x122 -
    1.7320508075688772 * b434 >= -1.7320508075688772)
@NLconstraint(m, e123, -sqrt((-0.35134351369704286 + x280)^2 + (
    -0.6263463928446534 + x281)^2 + (-0.01689904369168782 + x282)^2) + x123 -
    1.7320508075688772 * b435 >= -1.7320508075688772)
@NLconstraint(m, e124, -sqrt((-0.2718754143840908 + x283)^2 + (
    -0.48802820785090784 + x284)^2 + (-0.08187934237116656 + x285)^2) + x124 -
    1.7320508075688772 * b436 >= -1.7320508075688772)
@NLconstraint(m, e125, -sqrt((-0.33873348699206973 + x283)^2 + (
    -0.07233360770535402 + x284)^2 + (-0.011036367079899967 + x285)^2) + x125
    - 1.7320508075688772 * b437 >= -1.7320508075688772)
@NLconstraint(m, e126, -sqrt((-0.28385029589876865 + x283)^2 + (
    -0.11770636555802805 + x284)^2 + (-0.3110382248120007 + x285)^2) + x126 -
    1.7320508075688772 * b438 >= -1.7320508075688772)
@NLconstraint(m, e127, -sqrt((-0.7434707928397064 + x283)^2 + (
    -0.0357557155126923 + x284)^2 + (-0.6249375571804716 + x285)^2) + x127 -
    1.7320508075688772 * b439 >= -1.7320508075688772)
@NLconstraint(m, e128, -sqrt((-0.13501116090704035 + x283)^2 + (
    -0.7950712434655829 + x284)^2 + (-0.7369676243821022 + x285)^2) + x128 -
    1.7320508075688772 * b440 >= -1.7320508075688772)
@NLconstraint(m, e129, -sqrt((-0.21101029956774453 + x283)^2 + (
    -0.8480765801722641 + x284)^2 + (-0.7173017220824032 + x285)^2) + x129 -
    1.7320508075688772 * b441 >= -1.7320508075688772)
@NLconstraint(m, e130, -sqrt((-0.07495132545320449 + x283)^2 + (
    -0.4081313844234159 + x284)^2 + (-0.7004510913580178 + x285)^2) + x130 -
    1.7320508075688772 * b442 >= -1.7320508075688772)
@NLconstraint(m, e131, -sqrt((-0.9229582476032371 + x283)^2 + (
    -0.17221119493742953 + x284)^2 + (-0.2518629905323574 + x285)^2) + x131 -
    1.7320508075688772 * b443 >= -1.7320508075688772)
@NLconstraint(m, e132, -sqrt((-0.7750929946094214 + x283)^2 + (
    -0.9626723030210862 + x284)^2 + (-0.09375460752394849 + x285)^2) + x132 -
    1.7320508075688772 * b444 >= -1.7320508075688772)
@NLconstraint(m, e133, -sqrt((-0.08982827530229975 + x283)^2 + (
    -0.7511793846525663 + x284)^2 + (-0.3169893159261734 + x285)^2) + x133 -
    1.7320508075688772 * b445 >= -1.7320508075688772)
@NLconstraint(m, e134, -sqrt((-0.38677647485720235 + x283)^2 + (
    -0.87633207391825 + x284)^2 + (-0.7457995156246497 + x285)^2) + x134 -
    1.7320508075688772 * b446 >= -1.7320508075688772)
@NLconstraint(m, e135, -sqrt((-0.6607159863179267 + x283)^2 + (
    -0.8676520260577261 + x284)^2 + (-0.7320438297162596 + x285)^2) + x135 -
    1.7320508075688772 * b447 >= -1.7320508075688772)
@NLconstraint(m, e136, -sqrt((-0.8102488868102232 + x283)^2 + (
    -0.6432507057061979 + x284)^2 + (-0.5931582872810908 + x285)^2) + x136 -
    1.7320508075688772 * b448 >= -1.7320508075688772)
@NLconstraint(m, e137, -sqrt((-0.05986505368858752 + x283)^2 + (
    -0.909611607891918 + x284)^2 + (-0.9117643699770345 + x285)^2) + x137 -
    1.7320508075688772 * b449 >= -1.7320508075688772)
@NLconstraint(m, e138, -sqrt((-0.35134351369704286 + x283)^2 + (
    -0.6263463928446534 + x284)^2 + (-0.01689904369168782 + x285)^2) + x138 -
    1.7320508075688772 * b450 >= -1.7320508075688772)
@NLconstraint(m, e139, -sqrt((-0.2718754143840908 + x286)^2 + (
    -0.48802820785090784 + x287)^2 + (-0.08187934237116656 + x288)^2) + x139 -
    1.7320508075688772 * b451 >= -1.7320508075688772)
@NLconstraint(m, e140, -sqrt((-0.33873348699206973 + x286)^2 + (
    -0.07233360770535402 + x287)^2 + (-0.011036367079899967 + x288)^2) + x140
    - 1.7320508075688772 * b452 >= -1.7320508075688772)
@NLconstraint(m, e141, -sqrt((-0.28385029589876865 + x286)^2 + (
    -0.11770636555802805 + x287)^2 + (-0.3110382248120007 + x288)^2) + x141 -
    1.7320508075688772 * b453 >= -1.7320508075688772)
@NLconstraint(m, e142, -sqrt((-0.7434707928397064 + x286)^2 + (
    -0.0357557155126923 + x287)^2 + (-0.6249375571804716 + x288)^2) + x142 -
    1.7320508075688772 * b454 >= -1.7320508075688772)
@NLconstraint(m, e143, -sqrt((-0.13501116090704035 + x286)^2 + (
    -0.7950712434655829 + x287)^2 + (-0.7369676243821022 + x288)^2) + x143 -
    1.7320508075688772 * b455 >= -1.7320508075688772)
@NLconstraint(m, e144, -sqrt((-0.21101029956774453 + x286)^2 + (
    -0.8480765801722641 + x287)^2 + (-0.7173017220824032 + x288)^2) + x144 -
    1.7320508075688772 * b456 >= -1.7320508075688772)
@NLconstraint(m, e145, -sqrt((-0.07495132545320449 + x286)^2 + (
    -0.4081313844234159 + x287)^2 + (-0.7004510913580178 + x288)^2) + x145 -
    1.7320508075688772 * b457 >= -1.7320508075688772)
@NLconstraint(m, e146, -sqrt((-0.9229582476032371 + x286)^2 + (
    -0.17221119493742953 + x287)^2 + (-0.2518629905323574 + x288)^2) + x146 -
    1.7320508075688772 * b458 >= -1.7320508075688772)
@NLconstraint(m, e147, -sqrt((-0.7750929946094214 + x286)^2 + (
    -0.9626723030210862 + x287)^2 + (-0.09375460752394849 + x288)^2) + x147 -
    1.7320508075688772 * b459 >= -1.7320508075688772)
@NLconstraint(m, e148, -sqrt((-0.08982827530229975 + x286)^2 + (
    -0.7511793846525663 + x287)^2 + (-0.3169893159261734 + x288)^2) + x148 -
    1.7320508075688772 * b460 >= -1.7320508075688772)
@NLconstraint(m, e149, -sqrt((-0.38677647485720235 + x286)^2 + (
    -0.87633207391825 + x287)^2 + (-0.7457995156246497 + x288)^2) + x149 -
    1.7320508075688772 * b461 >= -1.7320508075688772)
@NLconstraint(m, e150, -sqrt((-0.6607159863179267 + x286)^2 + (
    -0.8676520260577261 + x287)^2 + (-0.7320438297162596 + x288)^2) + x150 -
    1.7320508075688772 * b462 >= -1.7320508075688772)
@NLconstraint(m, e151, -sqrt((-0.8102488868102232 + x286)^2 + (
    -0.6432507057061979 + x287)^2 + (-0.5931582872810908 + x288)^2) + x151 -
    1.7320508075688772 * b463 >= -1.7320508075688772)
@NLconstraint(m, e152, -sqrt((-0.05986505368858752 + x286)^2 + (
    -0.909611607891918 + x287)^2 + (-0.9117643699770345 + x288)^2) + x152 -
    1.7320508075688772 * b464 >= -1.7320508075688772)
@NLconstraint(m, e153, -sqrt((-0.35134351369704286 + x286)^2 + (
    -0.6263463928446534 + x287)^2 + (-0.01689904369168782 + x288)^2) + x153 -
    1.7320508075688772 * b465 >= -1.7320508075688772)
@NLconstraint(m, e154, -sqrt((-0.2718754143840908 + x289)^2 + (
    -0.48802820785090784 + x290)^2 + (-0.08187934237116656 + x291)^2) + x154 -
    1.7320508075688772 * b466 >= -1.7320508075688772)
@NLconstraint(m, e155, -sqrt((-0.33873348699206973 + x289)^2 + (
    -0.07233360770535402 + x290)^2 + (-0.011036367079899967 + x291)^2) + x155
    - 1.7320508075688772 * b467 >= -1.7320508075688772)
@NLconstraint(m, e156, -sqrt((-0.28385029589876865 + x289)^2 + (
    -0.11770636555802805 + x290)^2 + (-0.3110382248120007 + x291)^2) + x156 -
    1.7320508075688772 * b468 >= -1.7320508075688772)
@NLconstraint(m, e157, -sqrt((-0.7434707928397064 + x289)^2 + (
    -0.0357557155126923 + x290)^2 + (-0.6249375571804716 + x291)^2) + x157 -
    1.7320508075688772 * b469 >= -1.7320508075688772)
@NLconstraint(m, e158, -sqrt((-0.13501116090704035 + x289)^2 + (
    -0.7950712434655829 + x290)^2 + (-0.7369676243821022 + x291)^2) + x158 -
    1.7320508075688772 * b470 >= -1.7320508075688772)
@NLconstraint(m, e159, -sqrt((-0.21101029956774453 + x289)^2 + (
    -0.8480765801722641 + x290)^2 + (-0.7173017220824032 + x291)^2) + x159 -
    1.7320508075688772 * b471 >= -1.7320508075688772)
@NLconstraint(m, e160, -sqrt((-0.07495132545320449 + x289)^2 + (
    -0.4081313844234159 + x290)^2 + (-0.7004510913580178 + x291)^2) + x160 -
    1.7320508075688772 * b472 >= -1.7320508075688772)
@NLconstraint(m, e161, -sqrt((-0.9229582476032371 + x289)^2 + (
    -0.17221119493742953 + x290)^2 + (-0.2518629905323574 + x291)^2) + x161 -
    1.7320508075688772 * b473 >= -1.7320508075688772)
@NLconstraint(m, e162, -sqrt((-0.7750929946094214 + x289)^2 + (
    -0.9626723030210862 + x290)^2 + (-0.09375460752394849 + x291)^2) + x162 -
    1.7320508075688772 * b474 >= -1.7320508075688772)
@NLconstraint(m, e163, -sqrt((-0.08982827530229975 + x289)^2 + (
    -0.7511793846525663 + x290)^2 + (-0.3169893159261734 + x291)^2) + x163 -
    1.7320508075688772 * b475 >= -1.7320508075688772)
@NLconstraint(m, e164, -sqrt((-0.38677647485720235 + x289)^2 + (
    -0.87633207391825 + x290)^2 + (-0.7457995156246497 + x291)^2) + x164 -
    1.7320508075688772 * b476 >= -1.7320508075688772)
@NLconstraint(m, e165, -sqrt((-0.6607159863179267 + x289)^2 + (
    -0.8676520260577261 + x290)^2 + (-0.7320438297162596 + x291)^2) + x165 -
    1.7320508075688772 * b477 >= -1.7320508075688772)
@NLconstraint(m, e166, -sqrt((-0.8102488868102232 + x289)^2 + (
    -0.6432507057061979 + x290)^2 + (-0.5931582872810908 + x291)^2) + x166 -
    1.7320508075688772 * b478 >= -1.7320508075688772)
@NLconstraint(m, e167, -sqrt((-0.05986505368858752 + x289)^2 + (
    -0.909611607891918 + x290)^2 + (-0.9117643699770345 + x291)^2) + x167 -
    1.7320508075688772 * b479 >= -1.7320508075688772)
@NLconstraint(m, e168, -sqrt((-0.35134351369704286 + x289)^2 + (
    -0.6263463928446534 + x290)^2 + (-0.01689904369168782 + x291)^2) + x168 -
    1.7320508075688772 * b480 >= -1.7320508075688772)
@NLconstraint(m, e169, -sqrt((-0.2718754143840908 + x292)^2 + (
    -0.48802820785090784 + x293)^2 + (-0.08187934237116656 + x294)^2) + x169 -
    1.7320508075688772 * b481 >= -1.7320508075688772)
@NLconstraint(m, e170, -sqrt((-0.33873348699206973 + x292)^2 + (
    -0.07233360770535402 + x293)^2 + (-0.011036367079899967 + x294)^2) + x170
    - 1.7320508075688772 * b482 >= -1.7320508075688772)
@NLconstraint(m, e171, -sqrt((-0.28385029589876865 + x292)^2 + (
    -0.11770636555802805 + x293)^2 + (-0.3110382248120007 + x294)^2) + x171 -
    1.7320508075688772 * b483 >= -1.7320508075688772)
@NLconstraint(m, e172, -sqrt((-0.7434707928397064 + x292)^2 + (
    -0.0357557155126923 + x293)^2 + (-0.6249375571804716 + x294)^2) + x172 -
    1.7320508075688772 * b484 >= -1.7320508075688772)
@NLconstraint(m, e173, -sqrt((-0.13501116090704035 + x292)^2 + (
    -0.7950712434655829 + x293)^2 + (-0.7369676243821022 + x294)^2) + x173 -
    1.7320508075688772 * b485 >= -1.7320508075688772)
@NLconstraint(m, e174, -sqrt((-0.21101029956774453 + x292)^2 + (
    -0.8480765801722641 + x293)^2 + (-0.7173017220824032 + x294)^2) + x174 -
    1.7320508075688772 * b486 >= -1.7320508075688772)
@NLconstraint(m, e175, -sqrt((-0.07495132545320449 + x292)^2 + (
    -0.4081313844234159 + x293)^2 + (-0.7004510913580178 + x294)^2) + x175 -
    1.7320508075688772 * b487 >= -1.7320508075688772)
@NLconstraint(m, e176, -sqrt((-0.9229582476032371 + x292)^2 + (
    -0.17221119493742953 + x293)^2 + (-0.2518629905323574 + x294)^2) + x176 -
    1.7320508075688772 * b488 >= -1.7320508075688772)
@NLconstraint(m, e177, -sqrt((-0.7750929946094214 + x292)^2 + (
    -0.9626723030210862 + x293)^2 + (-0.09375460752394849 + x294)^2) + x177 -
    1.7320508075688772 * b489 >= -1.7320508075688772)
@NLconstraint(m, e178, -sqrt((-0.08982827530229975 + x292)^2 + (
    -0.7511793846525663 + x293)^2 + (-0.3169893159261734 + x294)^2) + x178 -
    1.7320508075688772 * b490 >= -1.7320508075688772)
@NLconstraint(m, e179, -sqrt((-0.38677647485720235 + x292)^2 + (
    -0.87633207391825 + x293)^2 + (-0.7457995156246497 + x294)^2) + x179 -
    1.7320508075688772 * b491 >= -1.7320508075688772)
@NLconstraint(m, e180, -sqrt((-0.6607159863179267 + x292)^2 + (
    -0.8676520260577261 + x293)^2 + (-0.7320438297162596 + x294)^2) + x180 -
    1.7320508075688772 * b492 >= -1.7320508075688772)
@NLconstraint(m, e181, -sqrt((-0.8102488868102232 + x292)^2 + (
    -0.6432507057061979 + x293)^2 + (-0.5931582872810908 + x294)^2) + x181 -
    1.7320508075688772 * b493 >= -1.7320508075688772)
@NLconstraint(m, e182, -sqrt((-0.05986505368858752 + x292)^2 + (
    -0.909611607891918 + x293)^2 + (-0.9117643699770345 + x294)^2) + x182 -
    1.7320508075688772 * b494 >= -1.7320508075688772)
@NLconstraint(m, e183, -sqrt((-0.35134351369704286 + x292)^2 + (
    -0.6263463928446534 + x293)^2 + (-0.01689904369168782 + x294)^2) + x183 -
    1.7320508075688772 * b495 >= -1.7320508075688772)
@NLconstraint(m, e184, -sqrt((-0.2718754143840908 + x295)^2 + (
    -0.48802820785090784 + x296)^2 + (-0.08187934237116656 + x297)^2) + x184 -
    1.7320508075688772 * b496 >= -1.7320508075688772)
@NLconstraint(m, e185, -sqrt((-0.33873348699206973 + x295)^2 + (
    -0.07233360770535402 + x296)^2 + (-0.011036367079899967 + x297)^2) + x185
    - 1.7320508075688772 * b497 >= -1.7320508075688772)
@NLconstraint(m, e186, -sqrt((-0.28385029589876865 + x295)^2 + (
    -0.11770636555802805 + x296)^2 + (-0.3110382248120007 + x297)^2) + x186 -
    1.7320508075688772 * b498 >= -1.7320508075688772)
@NLconstraint(m, e187, -sqrt((-0.7434707928397064 + x295)^2 + (
    -0.0357557155126923 + x296)^2 + (-0.6249375571804716 + x297)^2) + x187 -
    1.7320508075688772 * b499 >= -1.7320508075688772)
@NLconstraint(m, e188, -sqrt((-0.13501116090704035 + x295)^2 + (
    -0.7950712434655829 + x296)^2 + (-0.7369676243821022 + x297)^2) + x188 -
    1.7320508075688772 * b500 >= -1.7320508075688772)
@NLconstraint(m, e189, -sqrt((-0.21101029956774453 + x295)^2 + (
    -0.8480765801722641 + x296)^2 + (-0.7173017220824032 + x297)^2) + x189 -
    1.7320508075688772 * b501 >= -1.7320508075688772)
@NLconstraint(m, e190, -sqrt((-0.07495132545320449 + x295)^2 + (
    -0.4081313844234159 + x296)^2 + (-0.7004510913580178 + x297)^2) + x190 -
    1.7320508075688772 * b502 >= -1.7320508075688772)
@NLconstraint(m, e191, -sqrt((-0.9229582476032371 + x295)^2 + (
    -0.17221119493742953 + x296)^2 + (-0.2518629905323574 + x297)^2) + x191 -
    1.7320508075688772 * b503 >= -1.7320508075688772)
@NLconstraint(m, e192, -sqrt((-0.7750929946094214 + x295)^2 + (
    -0.9626723030210862 + x296)^2 + (-0.09375460752394849 + x297)^2) + x192 -
    1.7320508075688772 * b504 >= -1.7320508075688772)
@NLconstraint(m, e193, -sqrt((-0.08982827530229975 + x295)^2 + (
    -0.7511793846525663 + x296)^2 + (-0.3169893159261734 + x297)^2) + x193 -
    1.7320508075688772 * b505 >= -1.7320508075688772)
@NLconstraint(m, e194, -sqrt((-0.38677647485720235 + x295)^2 + (
    -0.87633207391825 + x296)^2 + (-0.7457995156246497 + x297)^2) + x194 -
    1.7320508075688772 * b506 >= -1.7320508075688772)
@NLconstraint(m, e195, -sqrt((-0.6607159863179267 + x295)^2 + (
    -0.8676520260577261 + x296)^2 + (-0.7320438297162596 + x297)^2) + x195 -
    1.7320508075688772 * b507 >= -1.7320508075688772)
@NLconstraint(m, e196, -sqrt((-0.8102488868102232 + x295)^2 + (
    -0.6432507057061979 + x296)^2 + (-0.5931582872810908 + x297)^2) + x196 -
    1.7320508075688772 * b508 >= -1.7320508075688772)
@NLconstraint(m, e197, -sqrt((-0.05986505368858752 + x295)^2 + (
    -0.909611607891918 + x296)^2 + (-0.9117643699770345 + x297)^2) + x197 -
    1.7320508075688772 * b509 >= -1.7320508075688772)
@NLconstraint(m, e198, -sqrt((-0.35134351369704286 + x295)^2 + (
    -0.6263463928446534 + x296)^2 + (-0.01689904369168782 + x297)^2) + x198 -
    1.7320508075688772 * b510 >= -1.7320508075688772)
@NLconstraint(m, e199, -sqrt((-0.2718754143840908 + x298)^2 + (
    -0.48802820785090784 + x299)^2 + (-0.08187934237116656 + x300)^2) + x199 -
    1.7320508075688772 * b511 >= -1.7320508075688772)
@NLconstraint(m, e200, -sqrt((-0.33873348699206973 + x298)^2 + (
    -0.07233360770535402 + x299)^2 + (-0.011036367079899967 + x300)^2) + x200
    - 1.7320508075688772 * b512 >= -1.7320508075688772)
@NLconstraint(m, e201, -sqrt((-0.28385029589876865 + x298)^2 + (
    -0.11770636555802805 + x299)^2 + (-0.3110382248120007 + x300)^2) + x201 -
    1.7320508075688772 * b513 >= -1.7320508075688772)
@NLconstraint(m, e202, -sqrt((-0.7434707928397064 + x298)^2 + (
    -0.0357557155126923 + x299)^2 + (-0.6249375571804716 + x300)^2) + x202 -
    1.7320508075688772 * b514 >= -1.7320508075688772)
@NLconstraint(m, e203, -sqrt((-0.13501116090704035 + x298)^2 + (
    -0.7950712434655829 + x299)^2 + (-0.7369676243821022 + x300)^2) + x203 -
    1.7320508075688772 * b515 >= -1.7320508075688772)
@NLconstraint(m, e204, -sqrt((-0.21101029956774453 + x298)^2 + (
    -0.8480765801722641 + x299)^2 + (-0.7173017220824032 + x300)^2) + x204 -
    1.7320508075688772 * b516 >= -1.7320508075688772)
@NLconstraint(m, e205, -sqrt((-0.07495132545320449 + x298)^2 + (
    -0.4081313844234159 + x299)^2 + (-0.7004510913580178 + x300)^2) + x205 -
    1.7320508075688772 * b517 >= -1.7320508075688772)
@NLconstraint(m, e206, -sqrt((-0.9229582476032371 + x298)^2 + (
    -0.17221119493742953 + x299)^2 + (-0.2518629905323574 + x300)^2) + x206 -
    1.7320508075688772 * b518 >= -1.7320508075688772)
@NLconstraint(m, e207, -sqrt((-0.7750929946094214 + x298)^2 + (
    -0.9626723030210862 + x299)^2 + (-0.09375460752394849 + x300)^2) + x207 -
    1.7320508075688772 * b519 >= -1.7320508075688772)
@NLconstraint(m, e208, -sqrt((-0.08982827530229975 + x298)^2 + (
    -0.7511793846525663 + x299)^2 + (-0.3169893159261734 + x300)^2) + x208 -
    1.7320508075688772 * b520 >= -1.7320508075688772)
@NLconstraint(m, e209, -sqrt((-0.38677647485720235 + x298)^2 + (
    -0.87633207391825 + x299)^2 + (-0.7457995156246497 + x300)^2) + x209 -
    1.7320508075688772 * b521 >= -1.7320508075688772)
@NLconstraint(m, e210, -sqrt((-0.6607159863179267 + x298)^2 + (
    -0.8676520260577261 + x299)^2 + (-0.7320438297162596 + x300)^2) + x210 -
    1.7320508075688772 * b522 >= -1.7320508075688772)
@NLconstraint(m, e211, -sqrt((-0.8102488868102232 + x298)^2 + (
    -0.6432507057061979 + x299)^2 + (-0.5931582872810908 + x300)^2) + x211 -
    1.7320508075688772 * b523 >= -1.7320508075688772)
@NLconstraint(m, e212, -sqrt((-0.05986505368858752 + x298)^2 + (
    -0.909611607891918 + x299)^2 + (-0.9117643699770345 + x300)^2) + x212 -
    1.7320508075688772 * b524 >= -1.7320508075688772)
@NLconstraint(m, e213, -sqrt((-0.35134351369704286 + x298)^2 + (
    -0.6263463928446534 + x299)^2 + (-0.01689904369168782 + x300)^2) + x213 -
    1.7320508075688772 * b525 >= -1.7320508075688772)
@NLconstraint(m, e214, -sqrt((-0.2718754143840908 + x301)^2 + (
    -0.48802820785090784 + x302)^2 + (-0.08187934237116656 + x303)^2) + x214 -
    1.7320508075688772 * b526 >= -1.7320508075688772)
@NLconstraint(m, e215, -sqrt((-0.33873348699206973 + x301)^2 + (
    -0.07233360770535402 + x302)^2 + (-0.011036367079899967 + x303)^2) + x215
    - 1.7320508075688772 * b527 >= -1.7320508075688772)
@NLconstraint(m, e216, -sqrt((-0.28385029589876865 + x301)^2 + (
    -0.11770636555802805 + x302)^2 + (-0.3110382248120007 + x303)^2) + x216 -
    1.7320508075688772 * b528 >= -1.7320508075688772)
@NLconstraint(m, e217, -sqrt((-0.7434707928397064 + x301)^2 + (
    -0.0357557155126923 + x302)^2 + (-0.6249375571804716 + x303)^2) + x217 -
    1.7320508075688772 * b529 >= -1.7320508075688772)
@NLconstraint(m, e218, -sqrt((-0.13501116090704035 + x301)^2 + (
    -0.7950712434655829 + x302)^2 + (-0.7369676243821022 + x303)^2) + x218 -
    1.7320508075688772 * b530 >= -1.7320508075688772)
@NLconstraint(m, e219, -sqrt((-0.21101029956774453 + x301)^2 + (
    -0.8480765801722641 + x302)^2 + (-0.7173017220824032 + x303)^2) + x219 -
    1.7320508075688772 * b531 >= -1.7320508075688772)
@NLconstraint(m, e220, -sqrt((-0.07495132545320449 + x301)^2 + (
    -0.4081313844234159 + x302)^2 + (-0.7004510913580178 + x303)^2) + x220 -
    1.7320508075688772 * b532 >= -1.7320508075688772)
@NLconstraint(m, e221, -sqrt((-0.9229582476032371 + x301)^2 + (
    -0.17221119493742953 + x302)^2 + (-0.2518629905323574 + x303)^2) + x221 -
    1.7320508075688772 * b533 >= -1.7320508075688772)
@NLconstraint(m, e222, -sqrt((-0.7750929946094214 + x301)^2 + (
    -0.9626723030210862 + x302)^2 + (-0.09375460752394849 + x303)^2) + x222 -
    1.7320508075688772 * b534 >= -1.7320508075688772)
@NLconstraint(m, e223, -sqrt((-0.08982827530229975 + x301)^2 + (
    -0.7511793846525663 + x302)^2 + (-0.3169893159261734 + x303)^2) + x223 -
    1.7320508075688772 * b535 >= -1.7320508075688772)
@NLconstraint(m, e224, -sqrt((-0.38677647485720235 + x301)^2 + (
    -0.87633207391825 + x302)^2 + (-0.7457995156246497 + x303)^2) + x224 -
    1.7320508075688772 * b536 >= -1.7320508075688772)
@NLconstraint(m, e225, -sqrt((-0.6607159863179267 + x301)^2 + (
    -0.8676520260577261 + x302)^2 + (-0.7320438297162596 + x303)^2) + x225 -
    1.7320508075688772 * b537 >= -1.7320508075688772)
@NLconstraint(m, e226, -sqrt((-0.8102488868102232 + x301)^2 + (
    -0.6432507057061979 + x302)^2 + (-0.5931582872810908 + x303)^2) + x226 -
    1.7320508075688772 * b538 >= -1.7320508075688772)
@NLconstraint(m, e227, -sqrt((-0.05986505368858752 + x301)^2 + (
    -0.909611607891918 + x302)^2 + (-0.9117643699770345 + x303)^2) + x227 -
    1.7320508075688772 * b539 >= -1.7320508075688772)
@NLconstraint(m, e228, -sqrt((-0.35134351369704286 + x301)^2 + (
    -0.6263463928446534 + x302)^2 + (-0.01689904369168782 + x303)^2) + x228 -
    1.7320508075688772 * b540 >= -1.7320508075688772)
@NLconstraint(m, e229, -sqrt((-0.2718754143840908 + x304)^2 + (
    -0.48802820785090784 + x305)^2 + (-0.08187934237116656 + x306)^2) + x229 -
    1.7320508075688772 * b541 >= -1.7320508075688772)
@NLconstraint(m, e230, -sqrt((-0.33873348699206973 + x304)^2 + (
    -0.07233360770535402 + x305)^2 + (-0.011036367079899967 + x306)^2) + x230
    - 1.7320508075688772 * b542 >= -1.7320508075688772)
@NLconstraint(m, e231, -sqrt((-0.28385029589876865 + x304)^2 + (
    -0.11770636555802805 + x305)^2 + (-0.3110382248120007 + x306)^2) + x231 -
    1.7320508075688772 * b543 >= -1.7320508075688772)
@NLconstraint(m, e232, -sqrt((-0.7434707928397064 + x304)^2 + (
    -0.0357557155126923 + x305)^2 + (-0.6249375571804716 + x306)^2) + x232 -
    1.7320508075688772 * b544 >= -1.7320508075688772)
@NLconstraint(m, e233, -sqrt((-0.13501116090704035 + x304)^2 + (
    -0.7950712434655829 + x305)^2 + (-0.7369676243821022 + x306)^2) + x233 -
    1.7320508075688772 * b545 >= -1.7320508075688772)
@NLconstraint(m, e234, -sqrt((-0.21101029956774453 + x304)^2 + (
    -0.8480765801722641 + x305)^2 + (-0.7173017220824032 + x306)^2) + x234 -
    1.7320508075688772 * b546 >= -1.7320508075688772)
@NLconstraint(m, e235, -sqrt((-0.07495132545320449 + x304)^2 + (
    -0.4081313844234159 + x305)^2 + (-0.7004510913580178 + x306)^2) + x235 -
    1.7320508075688772 * b547 >= -1.7320508075688772)
@NLconstraint(m, e236, -sqrt((-0.9229582476032371 + x304)^2 + (
    -0.17221119493742953 + x305)^2 + (-0.2518629905323574 + x306)^2) + x236 -
    1.7320508075688772 * b548 >= -1.7320508075688772)
@NLconstraint(m, e237, -sqrt((-0.7750929946094214 + x304)^2 + (
    -0.9626723030210862 + x305)^2 + (-0.09375460752394849 + x306)^2) + x237 -
    1.7320508075688772 * b549 >= -1.7320508075688772)
@NLconstraint(m, e238, -sqrt((-0.08982827530229975 + x304)^2 + (
    -0.7511793846525663 + x305)^2 + (-0.3169893159261734 + x306)^2) + x238 -
    1.7320508075688772 * b550 >= -1.7320508075688772)
@NLconstraint(m, e239, -sqrt((-0.38677647485720235 + x304)^2 + (
    -0.87633207391825 + x305)^2 + (-0.7457995156246497 + x306)^2) + x239 -
    1.7320508075688772 * b551 >= -1.7320508075688772)
@NLconstraint(m, e240, -sqrt((-0.6607159863179267 + x304)^2 + (
    -0.8676520260577261 + x305)^2 + (-0.7320438297162596 + x306)^2) + x240 -
    1.7320508075688772 * b552 >= -1.7320508075688772)
@NLconstraint(m, e241, -sqrt((-0.8102488868102232 + x304)^2 + (
    -0.6432507057061979 + x305)^2 + (-0.5931582872810908 + x306)^2) + x241 -
    1.7320508075688772 * b553 >= -1.7320508075688772)
@NLconstraint(m, e242, -sqrt((-0.05986505368858752 + x304)^2 + (
    -0.909611607891918 + x305)^2 + (-0.9117643699770345 + x306)^2) + x242 -
    1.7320508075688772 * b554 >= -1.7320508075688772)
@NLconstraint(m, e243, -sqrt((-0.35134351369704286 + x304)^2 + (
    -0.6263463928446534 + x305)^2 + (-0.01689904369168782 + x306)^2) + x243 -
    1.7320508075688772 * b555 >= -1.7320508075688772)
@NLconstraint(m, e244, -sqrt((-0.2718754143840908 + x307)^2 + (
    -0.48802820785090784 + x308)^2 + (-0.08187934237116656 + x309)^2) + x244 -
    1.7320508075688772 * b556 >= -1.7320508075688772)
@NLconstraint(m, e245, -sqrt((-0.33873348699206973 + x307)^2 + (
    -0.07233360770535402 + x308)^2 + (-0.011036367079899967 + x309)^2) + x245
    - 1.7320508075688772 * b557 >= -1.7320508075688772)
@NLconstraint(m, e246, -sqrt((-0.28385029589876865 + x307)^2 + (
    -0.11770636555802805 + x308)^2 + (-0.3110382248120007 + x309)^2) + x246 -
    1.7320508075688772 * b558 >= -1.7320508075688772)
@NLconstraint(m, e247, -sqrt((-0.7434707928397064 + x307)^2 + (
    -0.0357557155126923 + x308)^2 + (-0.6249375571804716 + x309)^2) + x247 -
    1.7320508075688772 * b559 >= -1.7320508075688772)
@NLconstraint(m, e248, -sqrt((-0.13501116090704035 + x307)^2 + (
    -0.7950712434655829 + x308)^2 + (-0.7369676243821022 + x309)^2) + x248 -
    1.7320508075688772 * b560 >= -1.7320508075688772)
@NLconstraint(m, e249, -sqrt((-0.21101029956774453 + x307)^2 + (
    -0.8480765801722641 + x308)^2 + (-0.7173017220824032 + x309)^2) + x249 -
    1.7320508075688772 * b561 >= -1.7320508075688772)
@NLconstraint(m, e250, -sqrt((-0.07495132545320449 + x307)^2 + (
    -0.4081313844234159 + x308)^2 + (-0.7004510913580178 + x309)^2) + x250 -
    1.7320508075688772 * b562 >= -1.7320508075688772)
@NLconstraint(m, e251, -sqrt((-0.9229582476032371 + x307)^2 + (
    -0.17221119493742953 + x308)^2 + (-0.2518629905323574 + x309)^2) + x251 -
    1.7320508075688772 * b563 >= -1.7320508075688772)
@NLconstraint(m, e252, -sqrt((-0.7750929946094214 + x307)^2 + (
    -0.9626723030210862 + x308)^2 + (-0.09375460752394849 + x309)^2) + x252 -
    1.7320508075688772 * b564 >= -1.7320508075688772)
@NLconstraint(m, e253, -sqrt((-0.08982827530229975 + x307)^2 + (
    -0.7511793846525663 + x308)^2 + (-0.3169893159261734 + x309)^2) + x253 -
    1.7320508075688772 * b565 >= -1.7320508075688772)
@NLconstraint(m, e254, -sqrt((-0.38677647485720235 + x307)^2 + (
    -0.87633207391825 + x308)^2 + (-0.7457995156246497 + x309)^2) + x254 -
    1.7320508075688772 * b566 >= -1.7320508075688772)
@NLconstraint(m, e255, -sqrt((-0.6607159863179267 + x307)^2 + (
    -0.8676520260577261 + x308)^2 + (-0.7320438297162596 + x309)^2) + x255 -
    1.7320508075688772 * b567 >= -1.7320508075688772)
@NLconstraint(m, e256, -sqrt((-0.8102488868102232 + x307)^2 + (
    -0.6432507057061979 + x308)^2 + (-0.5931582872810908 + x309)^2) + x256 -
    1.7320508075688772 * b568 >= -1.7320508075688772)
@NLconstraint(m, e257, -sqrt((-0.05986505368858752 + x307)^2 + (
    -0.909611607891918 + x308)^2 + (-0.9117643699770345 + x309)^2) + x257 -
    1.7320508075688772 * b569 >= -1.7320508075688772)
@NLconstraint(m, e258, -sqrt((-0.35134351369704286 + x307)^2 + (
    -0.6263463928446534 + x308)^2 + (-0.01689904369168782 + x309)^2) + x258 -
    1.7320508075688772 * b570 >= -1.7320508075688772)
@NLconstraint(m, e259, -sqrt((-0.2718754143840908 + x310)^2 + (
    -0.48802820785090784 + x311)^2 + (-0.08187934237116656 + x312)^2) + x259 -
    1.7320508075688772 * b571 >= -1.7320508075688772)
@NLconstraint(m, e260, -sqrt((-0.33873348699206973 + x310)^2 + (
    -0.07233360770535402 + x311)^2 + (-0.011036367079899967 + x312)^2) + x260
    - 1.7320508075688772 * b572 >= -1.7320508075688772)
@NLconstraint(m, e261, -sqrt((-0.28385029589876865 + x310)^2 + (
    -0.11770636555802805 + x311)^2 + (-0.3110382248120007 + x312)^2) + x261 -
    1.7320508075688772 * b573 >= -1.7320508075688772)
@NLconstraint(m, e262, -sqrt((-0.7434707928397064 + x310)^2 + (
    -0.0357557155126923 + x311)^2 + (-0.6249375571804716 + x312)^2) + x262 -
    1.7320508075688772 * b574 >= -1.7320508075688772)
@NLconstraint(m, e263, -sqrt((-0.13501116090704035 + x310)^2 + (
    -0.7950712434655829 + x311)^2 + (-0.7369676243821022 + x312)^2) + x263 -
    1.7320508075688772 * b575 >= -1.7320508075688772)
@NLconstraint(m, e264, -sqrt((-0.21101029956774453 + x310)^2 + (
    -0.8480765801722641 + x311)^2 + (-0.7173017220824032 + x312)^2) + x264 -
    1.7320508075688772 * b576 >= -1.7320508075688772)
@NLconstraint(m, e265, -sqrt((-0.07495132545320449 + x310)^2 + (
    -0.4081313844234159 + x311)^2 + (-0.7004510913580178 + x312)^2) + x265 -
    1.7320508075688772 * b577 >= -1.7320508075688772)
@NLconstraint(m, e266, -sqrt((-0.9229582476032371 + x310)^2 + (
    -0.17221119493742953 + x311)^2 + (-0.2518629905323574 + x312)^2) + x266 -
    1.7320508075688772 * b578 >= -1.7320508075688772)
@NLconstraint(m, e267, -sqrt((-0.7750929946094214 + x310)^2 + (
    -0.9626723030210862 + x311)^2 + (-0.09375460752394849 + x312)^2) + x267 -
    1.7320508075688772 * b579 >= -1.7320508075688772)
@NLconstraint(m, e268, -sqrt((-0.08982827530229975 + x310)^2 + (
    -0.7511793846525663 + x311)^2 + (-0.3169893159261734 + x312)^2) + x268 -
    1.7320508075688772 * b580 >= -1.7320508075688772)
@NLconstraint(m, e269, -sqrt((-0.38677647485720235 + x310)^2 + (
    -0.87633207391825 + x311)^2 + (-0.7457995156246497 + x312)^2) + x269 -
    1.7320508075688772 * b581 >= -1.7320508075688772)
@NLconstraint(m, e270, -sqrt((-0.6607159863179267 + x310)^2 + (
    -0.8676520260577261 + x311)^2 + (-0.7320438297162596 + x312)^2) + x270 -
    1.7320508075688772 * b582 >= -1.7320508075688772)
@NLconstraint(m, e271, -sqrt((-0.8102488868102232 + x310)^2 + (
    -0.6432507057061979 + x311)^2 + (-0.5931582872810908 + x312)^2) + x271 -
    1.7320508075688772 * b583 >= -1.7320508075688772)
@NLconstraint(m, e272, -sqrt((-0.05986505368858752 + x310)^2 + (
    -0.909611607891918 + x311)^2 + (-0.9117643699770345 + x312)^2) + x272 -
    1.7320508075688772 * b584 >= -1.7320508075688772)
@NLconstraint(m, e273, -sqrt((-0.35134351369704286 + x310)^2 + (
    -0.6263463928446534 + x311)^2 + (-0.01689904369168782 + x312)^2) + x273 -
    1.7320508075688772 * b585 >= -1.7320508075688772)
@constraint(m, e274, b391 + b406 + b421 + b436 + b451 + b466 + b481 + b496 +
    b511 + b526 + b541 + b556 + b571 == 1)
@constraint(m, e275, b392 + b407 + b422 + b437 + b452 + b467 + b482 + b497 +
    b512 + b527 + b542 + b557 + b572 == 1)
@constraint(m, e276, b393 + b408 + b423 + b438 + b453 + b468 + b483 + b498 +
    b513 + b528 + b543 + b558 + b573 == 1)
@constraint(m, e277, b394 + b409 + b424 + b439 + b454 + b469 + b484 + b499 +
    b514 + b529 + b544 + b559 + b574 == 1)
@constraint(m, e278, b395 + b410 + b425 + b440 + b455 + b470 + b485 + b500 +
    b515 + b530 + b545 + b560 + b575 == 1)
@constraint(m, e279, b396 + b411 + b426 + b441 + b456 + b471 + b486 + b501 +
    b516 + b531 + b546 + b561 + b576 == 1)
@constraint(m, e280, b397 + b412 + b427 + b442 + b457 + b472 + b487 + b502 +
    b517 + b532 + b547 + b562 + b577 == 1)
@constraint(m, e281, b398 + b413 + b428 + b443 + b458 + b473 + b488 + b503 +
    b518 + b533 + b548 + b563 + b578 == 1)
@constraint(m, e282, b399 + b414 + b429 + b444 + b459 + b474 + b489 + b504 +
    b519 + b534 + b549 + b564 + b579 == 1)
@constraint(m, e283, b400 + b415 + b430 + b445 + b460 + b475 + b490 + b505 +
    b520 + b535 + b550 + b565 + b580 == 1)
@constraint(m, e284, b401 + b416 + b431 + b446 + b461 + b476 + b491 + b506 +
    b521 + b536 + b551 + b566 + b581 == 1)
@constraint(m, e285, b402 + b417 + b432 + b447 + b462 + b477 + b492 + b507 +
    b522 + b537 + b552 + b567 + b582 == 1)
@constraint(m, e286, b403 + b418 + b433 + b448 + b463 + b478 + b493 + b508 +
    b523 + b538 + b553 + b568 + b583 == 1)
@constraint(m, e287, b404 + b419 + b434 + b449 + b464 + b479 + b494 + b509 +
    b524 + b539 + b554 + b569 + b584 == 1)
@constraint(m, e288, b405 + b420 + b435 + b450 + b465 + b480 + b495 + b510 +
    b525 + b540 + b555 + b570 + b585 == 1)
@constraint(m, e289, b313 + b314 + b315 + b316 + b317 + b318 + b319 + b320 +
    b321 + b322 + b323 + b324 + b391 + b392 + b393 + b394 + b395 + b396 + b397
    + b398 + b399 + b400 + b401 + b402 + b403 + b404 + b405 == 3)
@constraint(m, e290, b313 + b325 + b326 + b327 + b328 + b329 + b330 + b331 +
    b332 + b333 + b334 + b335 + b406 + b407 + b408 + b409 + b410 + b411 + b412
    + b413 + b414 + b415 + b416 + b417 + b418 + b419 + b420 == 3)
@constraint(m, e291, b314 + b325 + b336 + b337 + b338 + b339 + b340 + b341 +
    b342 + b343 + b344 + b345 + b421 + b422 + b423 + b424 + b425 + b426 + b427
    + b428 + b429 + b430 + b431 + b432 + b433 + b434 + b435 == 3)
@constraint(m, e292, b315 + b326 + b336 + b346 + b347 + b348 + b349 + b350 +
    b351 + b352 + b353 + b354 + b436 + b437 + b438 + b439 + b440 + b441 + b442
    + b443 + b444 + b445 + b446 + b447 + b448 + b449 + b450 == 3)
@constraint(m, e293, b316 + b327 + b337 + b346 + b355 + b356 + b357 + b358 +
    b359 + b360 + b361 + b362 + b451 + b452 + b453 + b454 + b455 + b456 + b457
    + b458 + b459 + b460 + b461 + b462 + b463 + b464 + b465 == 3)
@constraint(m, e294, b317 + b328 + b338 + b347 + b355 + b363 + b364 + b365 +
    b366 + b367 + b368 + b369 + b466 + b467 + b468 + b469 + b470 + b471 + b472
    + b473 + b474 + b475 + b476 + b477 + b478 + b479 + b480 == 3)
@constraint(m, e295, b318 + b329 + b339 + b348 + b356 + b363 + b370 + b371 +
    b372 + b373 + b374 + b375 + b481 + b482 + b483 + b484 + b485 + b486 + b487
    + b488 + b489 + b490 + b491 + b492 + b493 + b494 + b495 == 3)
@constraint(m, e296, b319 + b330 + b340 + b349 + b357 + b364 + b370 + b376 +
    b377 + b378 + b379 + b380 + b496 + b497 + b498 + b499 + b500 + b501 + b502
    + b503 + b504 + b505 + b506 + b507 + b508 + b509 + b510 == 3)
@constraint(m, e297, b320 + b331 + b341 + b350 + b358 + b365 + b371 + b376 +
    b381 + b382 + b383 + b384 + b511 + b512 + b513 + b514 + b515 + b516 + b517
    + b518 + b519 + b520 + b521 + b522 + b523 + b524 + b525 == 3)
@constraint(m, e298, b321 + b332 + b342 + b351 + b359 + b366 + b372 + b377 +
    b381 + b385 + b386 + b387 + b526 + b527 + b528 + b529 + b530 + b531 + b532
    + b533 + b534 + b535 + b536 + b537 + b538 + b539 + b540 == 3)
@constraint(m, e299, b322 + b333 + b343 + b352 + b360 + b367 + b373 + b378 +
    b382 + b385 + b388 + b389 + b541 + b542 + b543 + b544 + b545 + b546 + b547
    + b548 + b549 + b550 + b551 + b552 + b553 + b554 + b555 == 3)
@constraint(m, e300, b323 + b334 + b344 + b353 + b361 + b368 + b374 + b379 +
    b383 + b386 + b388 + b390 + b556 + b557 + b558 + b559 + b560 + b561 + b562
    + b563 + b564 + b565 + b566 + b567 + b568 + b569 + b570 == 3)
@constraint(m, e301, b324 + b335 + b345 + b354 + b362 + b369 + b375 + b380 +
    b384 + b387 + b389 + b390 + b571 + b572 + b573 + b574 + b575 + b576 + b577
    + b578 + b579 + b580 + b581 + b582 + b583 + b584 + b585 == 3)
@constraint(m, e302, b313 == 1)
@constraint(m, e303, b314 + b325 == 1)
@constraint(m, e304, b315 + b326 + b336 == 1)
@constraint(m, e305, b316 + b327 + b337 + b346 == 1)
@constraint(m, e306, b317 + b328 + b338 + b347 + b355 == 1)
@constraint(m, e307, b318 + b329 + b339 + b348 + b356 + b363 == 1)
@constraint(m, e308, b319 + b330 + b340 + b349 + b357 + b364 + b370 == 1)
@constraint(m, e309, b320 + b331 + b341 + b350 + b358 + b365 + b371 + b376
    == 1)
@constraint(m, e310, b321 + b332 + b342 + b351 + b359 + b366 + b372 + b377 +
    b381 == 1)
@constraint(m, e311, b322 + b333 + b343 + b352 + b360 + b367 + b373 + b378 +
    b382 + b385 == 1)
@constraint(m, e312, b323 + b334 + b344 + b353 + b361 + b368 + b374 + b379 +
    b383 + b386 + b388 == 1)
@constraint(m, e313, b324 + b335 + b345 + b354 + b362 + b369 + b375 + b380 +
    b384 + b387 + b389 + b390 == 1)
