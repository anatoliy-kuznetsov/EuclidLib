# NLP written by GAMS Convert at 05/15/24 11:34:58
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       100      100        0        0        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#       721      721        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       700      700        0
#
# Reformulation has removed 1 variable and 1 equation

using JuMP
using MathOptInterface
const MOI = MathOptInterface

model = m = Model()

@variable(m, 0 <= x1 <= 1, start=0)
@variable(m, 0 <= x2 <= 1, start=0)
@variable(m, 0 <= x3 <= 1, start=0)
@variable(m, 0 <= x4 <= 1, start=0)
@variable(m, 0 <= x5 <= 1, start=0)
@variable(m, 0 <= x6 <= 1, start=0)
@variable(m, 0 <= x7 <= 1, start=0)
@variable(m, 0 <= x8 <= 1, start=0)
@variable(m, 0 <= x9 <= 1, start=0)
@variable(m, 0 <= x10 <= 1, start=0)
@variable(m, 0 <= x11 <= 1, start=0)
@variable(m, 0 <= x12 <= 1, start=0)
@variable(m, 0 <= x13 <= 1, start=0)
@variable(m, 0 <= x14 <= 1, start=0)
@variable(m, 0 <= x15 <= 1, start=0)
@variable(m, 0 <= x16 <= 1, start=0)
@variable(m, 0 <= x17 <= 1, start=0)
@variable(m, 0 <= x18 <= 1, start=0)
@variable(m, 0 <= x19 <= 1, start=0)
@variable(m, 0 <= x20 <= 1, start=0)
@variable(m, 0 <= x21 <= 1, start=0)
@variable(m, 0 <= x22 <= 1, start=0)
@variable(m, 0 <= x23 <= 1, start=0)
@variable(m, 0 <= x24 <= 1, start=0)
@variable(m, 0 <= x25 <= 1, start=0)
@variable(m, 0 <= x26 <= 1, start=0)
@variable(m, 0 <= x27 <= 1, start=0)
@variable(m, 0 <= x28 <= 1, start=0)
@variable(m, 0 <= x29 <= 1, start=0)
@variable(m, 0 <= x30 <= 1, start=0)
@variable(m, 0 <= x31 <= 1, start=0)
@variable(m, 0 <= x32 <= 1, start=0)
@variable(m, 0 <= x33 <= 1, start=0)
@variable(m, 0 <= x34 <= 1, start=0)
@variable(m, 0 <= x35 <= 1, start=0)
@variable(m, 0 <= x36 <= 1, start=0)
@variable(m, 0 <= x37 <= 1, start=0)
@variable(m, 0 <= x38 <= 1, start=0)
@variable(m, 0 <= x39 <= 1, start=0)
@variable(m, 0 <= x40 <= 1, start=0)
@variable(m, 0 <= x41 <= 1, start=0)
@variable(m, 0 <= x42 <= 1, start=0)
@variable(m, 0 <= x43 <= 1, start=0)
@variable(m, 0 <= x44 <= 1, start=0)
@variable(m, 0 <= x45 <= 1, start=0)
@variable(m, 0 <= x46 <= 1, start=0)
@variable(m, 0 <= x47 <= 1, start=0)
@variable(m, 0 <= x48 <= 1, start=0)
@variable(m, 0 <= x49 <= 1, start=0)
@variable(m, 0 <= x50 <= 1, start=0)
@variable(m, 0 <= x51 <= 1, start=0)
@variable(m, 0 <= x52 <= 1, start=0)
@variable(m, 0 <= x53 <= 1, start=0)
@variable(m, 0 <= x54 <= 1, start=0)
@variable(m, 0 <= x55 <= 1, start=0)
@variable(m, 0 <= x56 <= 1, start=0)
@variable(m, 0 <= x57 <= 1, start=0)
@variable(m, 0 <= x58 <= 1, start=0)
@variable(m, 0 <= x59 <= 1, start=0)
@variable(m, 0 <= x60 <= 1, start=0)
@variable(m, 0 <= x61 <= 1, start=0)
@variable(m, 0 <= x62 <= 1, start=0)
@variable(m, 0 <= x63 <= 1, start=0)
@variable(m, 0 <= x64 <= 1, start=0)
@variable(m, 0 <= x65 <= 1, start=0)
@variable(m, 0 <= x66 <= 1, start=0)
@variable(m, 0 <= x67 <= 1, start=0)
@variable(m, 0 <= x68 <= 1, start=0)
@variable(m, 0 <= x69 <= 1, start=0)
@variable(m, 0 <= x70 <= 1, start=0)
@variable(m, 0 <= x71 <= 1, start=0)
@variable(m, 0 <= x72 <= 1, start=0)
@variable(m, 0 <= x73 <= 1, start=0)
@variable(m, 0 <= x74 <= 1, start=0)
@variable(m, 0 <= x75 <= 1, start=0)
@variable(m, 0 <= x76 <= 1, start=0)
@variable(m, 0 <= x77 <= 1, start=0)
@variable(m, 0 <= x78 <= 1, start=0)
@variable(m, 0 <= x79 <= 1, start=0)
@variable(m, 0 <= x80 <= 1, start=0)
@variable(m, 0 <= x81 <= 1, start=0)
@variable(m, 0 <= x82 <= 1, start=0)
@variable(m, 0 <= x83 <= 1, start=0)
@variable(m, 0 <= x84 <= 1, start=0)
@variable(m, 0 <= x85 <= 1, start=0)
@variable(m, 0 <= x86 <= 1, start=0)
@variable(m, 0 <= x87 <= 1, start=0)
@variable(m, 0 <= x88 <= 1, start=0)
@variable(m, 0 <= x89 <= 1, start=0)
@variable(m, 0 <= x90 <= 1, start=0)
@variable(m, 0 <= x91 <= 1, start=0)
@variable(m, 0 <= x92 <= 1, start=0)
@variable(m, 0 <= x93 <= 1, start=0)
@variable(m, 0 <= x94 <= 1, start=0)
@variable(m, 0 <= x95 <= 1, start=0)
@variable(m, 0 <= x96 <= 1, start=0)
@variable(m, 0 <= x97 <= 1, start=0)
@variable(m, 0 <= x98 <= 1, start=0)
@variable(m, 0 <= x99 <= 1, start=0)
@variable(m, 0 <= x100 <= 1, start=0)
@variable(m, 0 <= x101 <= 1, start=0)
@variable(m, 0 <= x102 <= 1, start=0)
@variable(m, 0 <= x103 <= 1, start=0)
@variable(m, 0 <= x104 <= 1, start=0)
@variable(m, 0 <= x105 <= 1, start=0)
@variable(m, 0 <= x106 <= 1, start=0)
@variable(m, 0 <= x107 <= 1, start=0)
@variable(m, 0 <= x108 <= 1, start=0)
@variable(m, 0 <= x109 <= 1, start=0)
@variable(m, 0 <= x110 <= 1, start=0)
@variable(m, 0 <= x111 <= 1, start=0)
@variable(m, 0 <= x112 <= 1, start=0)
@variable(m, 0 <= x113 <= 1, start=0)
@variable(m, 0 <= x114 <= 1, start=0)
@variable(m, 0 <= x115 <= 1, start=0)
@variable(m, 0 <= x116 <= 1, start=0)
@variable(m, 0 <= x117 <= 1, start=0)
@variable(m, 0 <= x118 <= 1, start=0)
@variable(m, 0 <= x119 <= 1, start=0)
@variable(m, 0 <= x120 <= 1, start=0)
@variable(m, 0 <= x121 <= 1, start=0)
@variable(m, 0 <= x122 <= 1, start=0)
@variable(m, 0 <= x123 <= 1, start=0)
@variable(m, 0 <= x124 <= 1, start=0)
@variable(m, 0 <= x125 <= 1, start=0)
@variable(m, 0 <= x126 <= 1, start=0)
@variable(m, 0 <= x127 <= 1, start=0)
@variable(m, 0 <= x128 <= 1, start=0)
@variable(m, 0 <= x129 <= 1, start=0)
@variable(m, 0 <= x130 <= 1, start=0)
@variable(m, 0 <= x131 <= 1, start=0)
@variable(m, 0 <= x132 <= 1, start=0)
@variable(m, 0 <= x133 <= 1, start=0)
@variable(m, 0 <= x134 <= 1, start=0)
@variable(m, 0 <= x135 <= 1, start=0)
@variable(m, 0 <= x136 <= 1, start=0)
@variable(m, 0 <= x137 <= 1, start=0)
@variable(m, 0 <= x138 <= 1, start=0)
@variable(m, 0 <= x139 <= 1, start=0)
@variable(m, 0 <= x140 <= 1, start=0)
@variable(m, 0 <= x141 <= 1, start=0)
@variable(m, 0 <= x142 <= 1, start=0)
@variable(m, 0 <= x143 <= 1, start=0)
@variable(m, 0 <= x144 <= 1, start=0)
@variable(m, 0 <= x145 <= 1, start=0)
@variable(m, 0 <= x146 <= 1, start=0)
@variable(m, 0 <= x147 <= 1, start=0)
@variable(m, 0 <= x148 <= 1, start=0)
@variable(m, 0 <= x149 <= 1, start=0)
@variable(m, 0 <= x150 <= 1, start=0)
@variable(m, 0 <= x151 <= 1, start=0)
@variable(m, 0 <= x152 <= 1, start=0)
@variable(m, 0 <= x153 <= 1, start=0)
@variable(m, 0 <= x154 <= 1, start=0)
@variable(m, 0 <= x155 <= 1, start=0)
@variable(m, 0 <= x156 <= 1, start=0)
@variable(m, 0 <= x157 <= 1, start=0)
@variable(m, 0 <= x158 <= 1, start=0)
@variable(m, 0 <= x159 <= 1, start=0)
@variable(m, 0 <= x160 <= 1, start=0)
@variable(m, 0 <= x161 <= 1, start=0)
@variable(m, 0 <= x162 <= 1, start=0)
@variable(m, 0 <= x163 <= 1, start=0)
@variable(m, 0 <= x164 <= 1, start=0)
@variable(m, 0 <= x165 <= 1, start=0)
@variable(m, 0 <= x166 <= 1, start=0)
@variable(m, 0 <= x167 <= 1, start=0)
@variable(m, 0 <= x168 <= 1, start=0)
@variable(m, 0 <= x169 <= 1, start=0)
@variable(m, 0 <= x170 <= 1, start=0)
@variable(m, 0 <= x171 <= 1, start=0)
@variable(m, 0 <= x172 <= 1, start=0)
@variable(m, 0 <= x173 <= 1, start=0)
@variable(m, 0 <= x174 <= 1, start=0)
@variable(m, 0 <= x175 <= 1, start=0)
@variable(m, 0 <= x176 <= 1, start=0)
@variable(m, 0 <= x177 <= 1, start=0)
@variable(m, 0 <= x178 <= 1, start=0)
@variable(m, 0 <= x179 <= 1, start=0)
@variable(m, 0 <= x180 <= 1, start=0)
@variable(m, 0 <= x181 <= 1, start=0)
@variable(m, 0 <= x182 <= 1, start=0)
@variable(m, 0 <= x183 <= 1, start=0)
@variable(m, 0 <= x184 <= 1, start=0)
@variable(m, 0 <= x185 <= 1, start=0)
@variable(m, 0 <= x186 <= 1, start=0)
@variable(m, 0 <= x187 <= 1, start=0)
@variable(m, 0 <= x188 <= 1, start=0)
@variable(m, 0 <= x189 <= 1, start=0)
@variable(m, 0 <= x190 <= 1, start=0)
@variable(m, 0 <= x191 <= 1, start=0)
@variable(m, 0 <= x192 <= 1, start=0)
@variable(m, 0 <= x193 <= 1, start=0)
@variable(m, 0 <= x194 <= 1, start=0)
@variable(m, 0 <= x195 <= 1, start=0)
@variable(m, 0 <= x196 <= 1, start=0)
@variable(m, 0 <= x197 <= 1, start=0)
@variable(m, 0 <= x198 <= 1, start=0)
@variable(m, 0 <= x199 <= 1, start=0)
@variable(m, 0 <= x200 <= 1, start=0)
@variable(m, 0 <= x201 <= 1, start=0)
@variable(m, 0 <= x202 <= 1, start=0)
@variable(m, 0 <= x203 <= 1, start=0)
@variable(m, 0 <= x204 <= 1, start=0)
@variable(m, 0 <= x205 <= 1, start=0)
@variable(m, 0 <= x206 <= 1, start=0)
@variable(m, 0 <= x207 <= 1, start=0)
@variable(m, 0 <= x208 <= 1, start=0)
@variable(m, 0 <= x209 <= 1, start=0)
@variable(m, 0 <= x210 <= 1, start=0)
@variable(m, 0 <= x211 <= 1, start=0)
@variable(m, 0 <= x212 <= 1, start=0)
@variable(m, 0 <= x213 <= 1, start=0)
@variable(m, 0 <= x214 <= 1, start=0)
@variable(m, 0 <= x215 <= 1, start=0)
@variable(m, 0 <= x216 <= 1, start=0)
@variable(m, 0 <= x217 <= 1, start=0)
@variable(m, 0 <= x218 <= 1, start=0)
@variable(m, 0 <= x219 <= 1, start=0)
@variable(m, 0 <= x220 <= 1, start=0)
@variable(m, 0 <= x221 <= 1, start=0)
@variable(m, 0 <= x222 <= 1, start=0)
@variable(m, 0 <= x223 <= 1, start=0)
@variable(m, 0 <= x224 <= 1, start=0)
@variable(m, 0 <= x225 <= 1, start=0)
@variable(m, 0 <= x226 <= 1, start=0)
@variable(m, 0 <= x227 <= 1, start=0)
@variable(m, 0 <= x228 <= 1, start=0)
@variable(m, 0 <= x229 <= 1, start=0)
@variable(m, 0 <= x230 <= 1, start=0)
@variable(m, 0 <= x231 <= 1, start=0)
@variable(m, 0 <= x232 <= 1, start=0)
@variable(m, 0 <= x233 <= 1, start=0)
@variable(m, 0 <= x234 <= 1, start=0)
@variable(m, 0 <= x235 <= 1, start=0)
@variable(m, 0 <= x236 <= 1, start=0)
@variable(m, 0 <= x237 <= 1, start=0)
@variable(m, 0 <= x238 <= 1, start=0)
@variable(m, 0 <= x239 <= 1, start=0)
@variable(m, 0 <= x240 <= 1, start=0)
@variable(m, 0 <= x241 <= 1, start=0)
@variable(m, 0 <= x242 <= 1, start=0)
@variable(m, 0 <= x243 <= 1, start=0)
@variable(m, 0 <= x244 <= 1, start=0)
@variable(m, 0 <= x245 <= 1, start=0)
@variable(m, 0 <= x246 <= 1, start=0)
@variable(m, 0 <= x247 <= 1, start=0)
@variable(m, 0 <= x248 <= 1, start=0)
@variable(m, 0 <= x249 <= 1, start=0)
@variable(m, 0 <= x250 <= 1, start=0)
@variable(m, 0 <= x251 <= 1, start=0)
@variable(m, 0 <= x252 <= 1, start=0)
@variable(m, 0 <= x253 <= 1, start=0)
@variable(m, 0 <= x254 <= 1, start=0)
@variable(m, 0 <= x255 <= 1, start=0)
@variable(m, 0 <= x256 <= 1, start=0)
@variable(m, 0 <= x257 <= 1, start=0)
@variable(m, 0 <= x258 <= 1, start=0)
@variable(m, 0 <= x259 <= 1, start=0)
@variable(m, 0 <= x260 <= 1, start=0)
@variable(m, 0 <= x261 <= 1, start=0)
@variable(m, 0 <= x262 <= 1, start=0)
@variable(m, 0 <= x263 <= 1, start=0)
@variable(m, 0 <= x264 <= 1, start=0)
@variable(m, 0 <= x265 <= 1, start=0)
@variable(m, 0 <= x266 <= 1, start=0)
@variable(m, 0 <= x267 <= 1, start=0)
@variable(m, 0 <= x268 <= 1, start=0)
@variable(m, 0 <= x269 <= 1, start=0)
@variable(m, 0 <= x270 <= 1, start=0)
@variable(m, 0 <= x271 <= 1, start=0)
@variable(m, 0 <= x272 <= 1, start=0)
@variable(m, 0 <= x273 <= 1, start=0)
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
@variable(m, 0 <= x339 <= 1, start=0)
@variable(m, 0 <= x340 <= 1, start=0)
@variable(m, 0 <= x341 <= 1, start=0)
@variable(m, 0 <= x342 <= 1, start=0)
@variable(m, 0 <= x343 <= 1, start=0)
@variable(m, 0 <= x344 <= 1, start=0)
@variable(m, 0 <= x345 <= 1, start=0)
@variable(m, 0 <= x346 <= 1, start=0)
@variable(m, 0 <= x347 <= 1, start=0)
@variable(m, 0 <= x348 <= 1, start=0)
@variable(m, 0 <= x349 <= 1, start=0)
@variable(m, 0 <= x350 <= 1, start=0)
@variable(m, 0 <= x351 <= 1, start=0)
@variable(m, 0 <= x352 <= 1, start=0)
@variable(m, 0 <= x353 <= 1, start=0)
@variable(m, 0 <= x354 <= 1, start=0)
@variable(m, 0 <= x355 <= 1, start=0)
@variable(m, 0 <= x356 <= 1, start=0)
@variable(m, 0 <= x357 <= 1, start=0)
@variable(m, 0 <= x358 <= 1, start=0)
@variable(m, 0 <= x359 <= 1, start=0)
@variable(m, 0 <= x360 <= 1, start=0)
@variable(m, 0 <= x361 <= 1, start=0)
@variable(m, 0 <= x362 <= 1, start=0)
@variable(m, 0 <= x363 <= 1, start=0)
@variable(m, 0 <= x364 <= 1, start=0)
@variable(m, 0 <= x365 <= 1, start=0)
@variable(m, 0 <= x366 <= 1, start=0)
@variable(m, 0 <= x367 <= 1, start=0)
@variable(m, 0 <= x368 <= 1, start=0)
@variable(m, 0 <= x369 <= 1, start=0)
@variable(m, 0 <= x370 <= 1, start=0)
@variable(m, 0 <= x371 <= 1, start=0)
@variable(m, 0 <= x372 <= 1, start=0)
@variable(m, 0 <= x373 <= 1, start=0)
@variable(m, 0 <= x374 <= 1, start=0)
@variable(m, 0 <= x375 <= 1, start=0)
@variable(m, 0 <= x376 <= 1, start=0)
@variable(m, 0 <= x377 <= 1, start=0)
@variable(m, 0 <= x378 <= 1, start=0)
@variable(m, 0 <= x379 <= 1, start=0)
@variable(m, 0 <= x380 <= 1, start=0)
@variable(m, 0 <= x381 <= 1, start=0)
@variable(m, 0 <= x382 <= 1, start=0)
@variable(m, 0 <= x383 <= 1, start=0)
@variable(m, 0 <= x384 <= 1, start=0)
@variable(m, 0 <= x385 <= 1, start=0)
@variable(m, 0 <= x386 <= 1, start=0)
@variable(m, 0 <= x387 <= 1, start=0)
@variable(m, 0 <= x388 <= 1, start=0)
@variable(m, 0 <= x389 <= 1, start=0)
@variable(m, 0 <= x390 <= 1, start=0)
@variable(m, 0 <= x391 <= 1, start=0)
@variable(m, 0 <= x392 <= 1, start=0)
@variable(m, 0 <= x393 <= 1, start=0)
@variable(m, 0 <= x394 <= 1, start=0)
@variable(m, 0 <= x395 <= 1, start=0)
@variable(m, 0 <= x396 <= 1, start=0)
@variable(m, 0 <= x397 <= 1, start=0)
@variable(m, 0 <= x398 <= 1, start=0)
@variable(m, 0 <= x399 <= 1, start=0)
@variable(m, 0 <= x400 <= 1, start=0)
@variable(m, 0 <= x401 <= 1, start=0)
@variable(m, 0 <= x402 <= 1, start=0)
@variable(m, 0 <= x403 <= 1, start=0)
@variable(m, 0 <= x404 <= 1, start=0)
@variable(m, 0 <= x405 <= 1, start=0)
@variable(m, 0 <= x406 <= 1, start=0)
@variable(m, 0 <= x407 <= 1, start=0)
@variable(m, 0 <= x408 <= 1, start=0)
@variable(m, 0 <= x409 <= 1, start=0)
@variable(m, 0 <= x410 <= 1, start=0)
@variable(m, 0 <= x411 <= 1, start=0)
@variable(m, 0 <= x412 <= 1, start=0)
@variable(m, 0 <= x413 <= 1, start=0)
@variable(m, 0 <= x414 <= 1, start=0)
@variable(m, 0 <= x415 <= 1, start=0)
@variable(m, 0 <= x416 <= 1, start=0)
@variable(m, 0 <= x417 <= 1, start=0)
@variable(m, 0 <= x418 <= 1, start=0)
@variable(m, 0 <= x419 <= 1, start=0)
@variable(m, 0 <= x420 <= 1, start=0)
@variable(m, 0 <= x421 <= 1, start=0)
@variable(m, 0 <= x422 <= 1, start=0)
@variable(m, 0 <= x423 <= 1, start=0)
@variable(m, 0 <= x424 <= 1, start=0)
@variable(m, 0 <= x425 <= 1, start=0)
@variable(m, 0 <= x426 <= 1, start=0)
@variable(m, 0 <= x427 <= 1, start=0)
@variable(m, 0 <= x428 <= 1, start=0)
@variable(m, 0 <= x429 <= 1, start=0)
@variable(m, 0 <= x430 <= 1, start=0)
@variable(m, 0 <= x431 <= 1, start=0)
@variable(m, 0 <= x432 <= 1, start=0)
@variable(m, 0 <= x433 <= 1, start=0)
@variable(m, 0 <= x434 <= 1, start=0)
@variable(m, 0 <= x435 <= 1, start=0)
@variable(m, 0 <= x436 <= 1, start=0)
@variable(m, 0 <= x437 <= 1, start=0)
@variable(m, 0 <= x438 <= 1, start=0)
@variable(m, 0 <= x439 <= 1, start=0)
@variable(m, 0 <= x440 <= 1, start=0)
@variable(m, 0 <= x441 <= 1, start=0)
@variable(m, 0 <= x442 <= 1, start=0)
@variable(m, 0 <= x443 <= 1, start=0)
@variable(m, 0 <= x444 <= 1, start=0)
@variable(m, 0 <= x445 <= 1, start=0)
@variable(m, 0 <= x446 <= 1, start=0)
@variable(m, 0 <= x447 <= 1, start=0)
@variable(m, 0 <= x448 <= 1, start=0)
@variable(m, 0 <= x449 <= 1, start=0)
@variable(m, 0 <= x450 <= 1, start=0)
@variable(m, 0 <= x451 <= 1, start=0)
@variable(m, 0 <= x452 <= 1, start=0)
@variable(m, 0 <= x453 <= 1, start=0)
@variable(m, 0 <= x454 <= 1, start=0)
@variable(m, 0 <= x455 <= 1, start=0)
@variable(m, 0 <= x456 <= 1, start=0)
@variable(m, 0 <= x457 <= 1, start=0)
@variable(m, 0 <= x458 <= 1, start=0)
@variable(m, 0 <= x459 <= 1, start=0)
@variable(m, 0 <= x460 <= 1, start=0)
@variable(m, 0 <= x461 <= 1, start=0)
@variable(m, 0 <= x462 <= 1, start=0)
@variable(m, 0 <= x463 <= 1, start=0)
@variable(m, 0 <= x464 <= 1, start=0)
@variable(m, 0 <= x465 <= 1, start=0)
@variable(m, 0 <= x466 <= 1, start=0)
@variable(m, 0 <= x467 <= 1, start=0)
@variable(m, 0 <= x468 <= 1, start=0)
@variable(m, 0 <= x469 <= 1, start=0)
@variable(m, 0 <= x470 <= 1, start=0)
@variable(m, 0 <= x471 <= 1, start=0)
@variable(m, 0 <= x472 <= 1, start=0)
@variable(m, 0 <= x473 <= 1, start=0)
@variable(m, 0 <= x474 <= 1, start=0)
@variable(m, 0 <= x475 <= 1, start=0)
@variable(m, 0 <= x476 <= 1, start=0)
@variable(m, 0 <= x477 <= 1, start=0)
@variable(m, 0 <= x478 <= 1, start=0)
@variable(m, 0 <= x479 <= 1, start=0)
@variable(m, 0 <= x480 <= 1, start=0)
@variable(m, 0 <= x481 <= 1, start=0)
@variable(m, 0 <= x482 <= 1, start=0)
@variable(m, 0 <= x483 <= 1, start=0)
@variable(m, 0 <= x484 <= 1, start=0)
@variable(m, 0 <= x485 <= 1, start=0)
@variable(m, 0 <= x486 <= 1, start=0)
@variable(m, 0 <= x487 <= 1, start=0)
@variable(m, 0 <= x488 <= 1, start=0)
@variable(m, 0 <= x489 <= 1, start=0)
@variable(m, 0 <= x490 <= 1, start=0)
@variable(m, 0 <= x491 <= 1, start=0)
@variable(m, 0 <= x492 <= 1, start=0)
@variable(m, 0 <= x493 <= 1, start=0)
@variable(m, 0 <= x494 <= 1, start=0)
@variable(m, 0 <= x495 <= 1, start=0)
@variable(m, 0 <= x496 <= 1, start=0)
@variable(m, 0 <= x497 <= 1, start=0)
@variable(m, 0 <= x498 <= 1, start=0)
@variable(m, 0 <= x499 <= 1, start=0)
@variable(m, 0 <= x500 <= 1, start=0)
@variable(m, 0 <= x501 <= 1, start=0)
@variable(m, 0 <= x502 <= 1, start=0)
@variable(m, 0 <= x503 <= 1, start=0)
@variable(m, 0 <= x504 <= 1, start=0)
@variable(m, 0 <= x505 <= 1, start=0)
@variable(m, 0 <= x506 <= 1, start=0)
@variable(m, 0 <= x507 <= 1, start=0)
@variable(m, 0 <= x508 <= 1, start=0)
@variable(m, 0 <= x509 <= 1, start=0)
@variable(m, 0 <= x510 <= 1, start=0)
@variable(m, 0 <= x511 <= 1, start=0)
@variable(m, 0 <= x512 <= 1, start=0)
@variable(m, 0 <= x513 <= 1, start=0)
@variable(m, 0 <= x514 <= 1, start=0)
@variable(m, 0 <= x515 <= 1, start=0)
@variable(m, 0 <= x516 <= 1, start=0)
@variable(m, 0 <= x517 <= 1, start=0)
@variable(m, 0 <= x518 <= 1, start=0)
@variable(m, 0 <= x519 <= 1, start=0)
@variable(m, 0 <= x520 <= 1, start=0)
@variable(m, 0 <= x521 <= 1, start=0)
@variable(m, 0 <= x522 <= 1, start=0)
@variable(m, 0 <= x523 <= 1, start=0)
@variable(m, 0 <= x524 <= 1, start=0)
@variable(m, 0 <= x525 <= 1, start=0)
@variable(m, 0 <= x526 <= 1, start=0)
@variable(m, 0 <= x527 <= 1, start=0)
@variable(m, 0 <= x528 <= 1, start=0)
@variable(m, 0 <= x529 <= 1, start=0)
@variable(m, 0 <= x530 <= 1, start=0)
@variable(m, 0 <= x531 <= 1, start=0)
@variable(m, 0 <= x532 <= 1, start=0)
@variable(m, 0 <= x533 <= 1, start=0)
@variable(m, 0 <= x534 <= 1, start=0)
@variable(m, 0 <= x535 <= 1, start=0)
@variable(m, 0 <= x536 <= 1, start=0)
@variable(m, 0 <= x537 <= 1, start=0)
@variable(m, 0 <= x538 <= 1, start=0)
@variable(m, 0 <= x539 <= 1, start=0)
@variable(m, 0 <= x540 <= 1, start=0)
@variable(m, 0 <= x541 <= 1, start=0)
@variable(m, 0 <= x542 <= 1, start=0)
@variable(m, 0 <= x543 <= 1, start=0)
@variable(m, 0 <= x544 <= 1, start=0)
@variable(m, 0 <= x545 <= 1, start=0)
@variable(m, 0 <= x546 <= 1, start=0)
@variable(m, 0 <= x547 <= 1, start=0)
@variable(m, 0 <= x548 <= 1, start=0)
@variable(m, 0 <= x549 <= 1, start=0)
@variable(m, 0 <= x550 <= 1, start=0)
@variable(m, 0 <= x551 <= 1, start=0)
@variable(m, 0 <= x552 <= 1, start=0)
@variable(m, 0 <= x553 <= 1, start=0)
@variable(m, 0 <= x554 <= 1, start=0)
@variable(m, 0 <= x555 <= 1, start=0)
@variable(m, 0 <= x556 <= 1, start=0)
@variable(m, 0 <= x557 <= 1, start=0)
@variable(m, 0 <= x558 <= 1, start=0)
@variable(m, 0 <= x559 <= 1, start=0)
@variable(m, 0 <= x560 <= 1, start=0)
@variable(m, 0 <= x561 <= 1, start=0)
@variable(m, 0 <= x562 <= 1, start=0)
@variable(m, 0 <= x563 <= 1, start=0)
@variable(m, 0 <= x564 <= 1, start=0)
@variable(m, 0 <= x565 <= 1, start=0)
@variable(m, 0 <= x566 <= 1, start=0)
@variable(m, 0 <= x567 <= 1, start=0)
@variable(m, 0 <= x568 <= 1, start=0)
@variable(m, 0 <= x569 <= 1, start=0)
@variable(m, 0 <= x570 <= 1, start=0)
@variable(m, 0 <= x571 <= 1, start=0)
@variable(m, 0 <= x572 <= 1, start=0)
@variable(m, 0 <= x573 <= 1, start=0)
@variable(m, 0 <= x574 <= 1, start=0)
@variable(m, 0 <= x575 <= 1, start=0)
@variable(m, 0 <= x576 <= 1, start=0)
@variable(m, 0 <= x577 <= 1, start=0)
@variable(m, 0 <= x578 <= 1, start=0)
@variable(m, 0 <= x579 <= 1, start=0)
@variable(m, 0 <= x580 <= 1, start=0)
@variable(m, 0 <= x581 <= 1, start=0)
@variable(m, 0 <= x582 <= 1, start=0)
@variable(m, 0 <= x583 <= 1, start=0)
@variable(m, 0 <= x584 <= 1, start=0)
@variable(m, 0 <= x585 <= 1, start=0)
@variable(m, 0 <= x586 <= 1, start=0)
@variable(m, 0 <= x587 <= 1, start=0)
@variable(m, 0 <= x588 <= 1, start=0)
@variable(m, 0 <= x589 <= 1, start=0)
@variable(m, 0 <= x590 <= 1, start=0)
@variable(m, 0 <= x591 <= 1, start=0)
@variable(m, 0 <= x592 <= 1, start=0)
@variable(m, 0 <= x593 <= 1, start=0)
@variable(m, 0 <= x594 <= 1, start=0)
@variable(m, 0 <= x595 <= 1, start=0)
@variable(m, 0 <= x596 <= 1, start=0)
@variable(m, 0 <= x597 <= 1, start=0)
@variable(m, 0 <= x598 <= 1, start=0)
@variable(m, 0 <= x599 <= 1, start=0)
@variable(m, 0 <= x600 <= 1, start=0)
@variable(m, 0 <= x601 <= 1, start=0)
@variable(m, 0 <= x602 <= 1, start=0)
@variable(m, 0 <= x603 <= 1, start=0)
@variable(m, 0 <= x604 <= 1, start=0)
@variable(m, 0 <= x605 <= 1, start=0)
@variable(m, 0 <= x606 <= 1, start=0)
@variable(m, 0 <= x607 <= 1, start=0)
@variable(m, 0 <= x608 <= 1, start=0)
@variable(m, 0 <= x609 <= 1, start=0)
@variable(m, 0 <= x610 <= 1, start=0)
@variable(m, 0 <= x611 <= 1, start=0)
@variable(m, 0 <= x612 <= 1, start=0)
@variable(m, 0 <= x613 <= 1, start=0)
@variable(m, 0 <= x614 <= 1, start=0)
@variable(m, 0 <= x615 <= 1, start=0)
@variable(m, 0 <= x616 <= 1, start=0)
@variable(m, 0 <= x617 <= 1, start=0)
@variable(m, 0 <= x618 <= 1, start=0)
@variable(m, 0 <= x619 <= 1, start=0)
@variable(m, 0 <= x620 <= 1, start=0)
@variable(m, 0 <= x621 <= 1, start=0)
@variable(m, 0 <= x622 <= 1, start=0)
@variable(m, 0 <= x623 <= 1, start=0)
@variable(m, 0 <= x624 <= 1, start=0)
@variable(m, 0 <= x625 <= 1, start=0)
@variable(m, 0 <= x626 <= 1, start=0)
@variable(m, 0 <= x627 <= 1, start=0)
@variable(m, 0 <= x628 <= 1, start=0)
@variable(m, 0 <= x629 <= 1, start=0)
@variable(m, 0 <= x630 <= 1, start=0)
@variable(m, 0 <= x631 <= 1, start=0)
@variable(m, 0 <= x632 <= 1, start=0)
@variable(m, 0 <= x633 <= 1, start=0)
@variable(m, 0 <= x634 <= 1, start=0)
@variable(m, 0 <= x635 <= 1, start=0)
@variable(m, 0 <= x636 <= 1, start=0)
@variable(m, 0 <= x637 <= 1, start=0)
@variable(m, 0 <= x638 <= 1, start=0)
@variable(m, 0 <= x639 <= 1, start=0)
@variable(m, 0 <= x640 <= 1, start=0)
@variable(m, 0 <= x641 <= 1, start=0)
@variable(m, 0 <= x642 <= 1, start=0)
@variable(m, 0 <= x643 <= 1, start=0)
@variable(m, 0 <= x644 <= 1, start=0)
@variable(m, 0 <= x645 <= 1, start=0)
@variable(m, 0 <= x646 <= 1, start=0)
@variable(m, 0 <= x647 <= 1, start=0)
@variable(m, 0 <= x648 <= 1, start=0)
@variable(m, 0 <= x649 <= 1, start=0)
@variable(m, 0 <= x650 <= 1, start=0)
@variable(m, 0 <= x651 <= 1, start=0)
@variable(m, 0 <= x652 <= 1, start=0)
@variable(m, 0 <= x653 <= 1, start=0)
@variable(m, 0 <= x654 <= 1, start=0)
@variable(m, 0 <= x655 <= 1, start=0)
@variable(m, 0 <= x656 <= 1, start=0)
@variable(m, 0 <= x657 <= 1, start=0)
@variable(m, 0 <= x658 <= 1, start=0)
@variable(m, 0 <= x659 <= 1, start=0)
@variable(m, 0 <= x660 <= 1, start=0)
@variable(m, 0 <= x661 <= 1, start=0)
@variable(m, 0 <= x662 <= 1, start=0)
@variable(m, 0 <= x663 <= 1, start=0)
@variable(m, 0 <= x664 <= 1, start=0)
@variable(m, 0 <= x665 <= 1, start=0)
@variable(m, 0 <= x666 <= 1, start=0)
@variable(m, 0 <= x667 <= 1, start=0)
@variable(m, 0 <= x668 <= 1, start=0)
@variable(m, 0 <= x669 <= 1, start=0)
@variable(m, 0 <= x670 <= 1, start=0)
@variable(m, 0 <= x671 <= 1, start=0)
@variable(m, 0 <= x672 <= 1, start=0)
@variable(m, 0 <= x673 <= 1, start=0)
@variable(m, 0 <= x674 <= 1, start=0)
@variable(m, 0 <= x675 <= 1, start=0)
@variable(m, 0 <= x676 <= 1, start=0)
@variable(m, 0 <= x677 <= 1, start=0)
@variable(m, 0 <= x678 <= 1, start=0)
@variable(m, 0 <= x679 <= 1, start=0)
@variable(m, 0 <= x680 <= 1, start=0)
@variable(m, 0 <= x681 <= 1, start=0)
@variable(m, 0 <= x682 <= 1, start=0)
@variable(m, 0 <= x683 <= 1, start=0)
@variable(m, 0 <= x684 <= 1, start=0)
@variable(m, 0 <= x685 <= 1, start=0)
@variable(m, 0 <= x686 <= 1, start=0)
@variable(m, 0 <= x687 <= 1, start=0)
@variable(m, 0 <= x688 <= 1, start=0)
@variable(m, 0 <= x689 <= 1, start=0)
@variable(m, 0 <= x690 <= 1, start=0)
@variable(m, 0 <= x691 <= 1, start=0)
@variable(m, 0 <= x692 <= 1, start=0)
@variable(m, 0 <= x693 <= 1, start=0)
@variable(m, 0 <= x694 <= 1, start=0)
@variable(m, 0 <= x695 <= 1, start=0)
@variable(m, 0 <= x696 <= 1, start=0)
@variable(m, 0 <= x697 <= 1, start=0)
@variable(m, 0 <= x698 <= 1, start=0)
@variable(m, 0 <= x699 <= 1, start=0)
@variable(m, 0 <= x700 <= 1, start=0)
@variable(m, 0 <= x701 <= 1, start=0)
@variable(m, 0 <= x702 <= 1, start=0)
@variable(m, 0 <= x703 <= 1, start=0)
@variable(m, 0 <= x704 <= 1, start=0)
@variable(m, 0 <= x705 <= 1, start=0)
@variable(m, 0 <= x706 <= 1, start=0)
@variable(m, 0 <= x707 <= 1, start=0)
@variable(m, 0 <= x708 <= 1, start=0)
@variable(m, 0 <= x709 <= 1, start=0)
@variable(m, 0 <= x710 <= 1, start=0)
@variable(m, 0 <= x711 <= 1, start=0)
@variable(m, 0 <= x712 <= 1, start=0)
@variable(m, 0 <= x713 <= 1, start=0)
@variable(m, 0 <= x714 <= 1, start=0)
@variable(m, 0 <= x715 <= 1, start=0)
@variable(m, 0 <= x716 <= 1, start=0)
@variable(m, 0 <= x717 <= 1, start=0)
@variable(m, 0 <= x718 <= 1, start=0)
@variable(m, 0 <= x719 <= 1, start=0)
@variable(m, 0 <= x720 <= 1, start=0)
@variable(m, 0 <= x721 <= 1, start=0)

@NLobjective(m, Min, x22 * ((-0.637732077469805 + x1)^2 + (-0.30061635945038845
    + x2)^2 + (-0.6924078188563045 + x3)^2) + x23 * ((-0.5204622036281865 + x1)
    ^2 + (-0.4262380695375112 + x2)^2 + (-0.019757804882570618 + x3)^2) + x24
    * ((-0.3877676795047561 + x1)^2 + (-0.6261603378186641 + x2)^2 + (
    -0.20807844834808797 + x3)^2) + x25 * ((-0.3455519385475 + x1)^2 + (
    -0.20721956099132388 + x2)^2 + (-0.7536751735394452 + x3)^2) + x26 * ((
    -0.7452291570426526 + x1)^2 + (-0.8288345290542969 + x2)^2 + (
    -0.9101818193634833 + x3)^2) + x27 * ((-0.7088715037487956 + x1)^2 + (
    -0.8675258967244885 + x2)^2 + (-0.04421039019838524 + x3)^2) + x28 * ((
    -0.33645524584418685 + x1)^2 + (-0.24931821641731888 + x2)^2 + (
    -0.24789447471906245 + x3)^2) + x29 * ((-0.39606323961214507 + x1)^2 + (
    -0.5092297648083476 + x2)^2 + (-0.8429822635539893 + x3)^2) + x30 * ((
    -0.3162888023664645 + x1)^2 + (-0.3537176609576351 + x2)^2 + (
    -0.8840601824506505 + x3)^2) + x31 * ((-0.042024431013358066 + x1)^2 + (
    -0.015648799035293925 + x2)^2 + (-0.028897199565620646 + x3)^2) + x32 * ((
    -0.7829982657179482 + x1)^2 + (-0.7604457448591289 + x2)^2 + (
    -0.597334909736347 + x3)^2) + x33 * ((-0.21464482455558387 + x1)^2 + (
    -0.7368895039728377 + x2)^2 + (-0.14158977662661187 + x3)^2) + x34 * ((
    -0.790895349248712 + x1)^2 + (-0.999859654218962 + x2)^2 + (
    -0.7994024450128572 + x3)^2) + x35 * ((-0.15089689559879838 + x1)^2 + (
    -0.2905434515528619 + x2)^2 + (-0.2886420160429456 + x3)^2) + x36 * ((
    -0.9157228230765573 + x1)^2 + (-0.7406305983646623 + x2)^2 + (
    -0.4142557316611599 + x3)^2) + x37 * ((-0.28767980872766563 + x1)^2 + (
    -0.0742772003595773 + x2)^2 + (-0.7235701139213052 + x3)^2) + x38 * ((
    -0.25465347672976957 + x1)^2 + (-0.6409023820345298 + x2)^2 + (
    -0.5494341492685579 + x3)^2) + x39 * ((-0.5541270607350097 + x1)^2 + (
    -0.9692776471334402 + x2)^2 + (-0.05355629576813248 + x3)^2) + x40 * ((
    -0.16592885733639762 + x1)^2 + (-0.6090998523529765 + x2)^2 + (
    -0.007633151339320965 + x3)^2) + x41 * ((-0.9035601490301819 + x1)^2 + (
    -0.09986398472275337 + x2)^2 + (-0.9904466067565432 + x3)^2) + x42 * ((
    -0.7453737555747959 + x1)^2 + (-0.8241163846060925 + x2)^2 + (
    -0.16259034239222492 + x3)^2) + x43 * ((-0.09286618285654225 + x1)^2 + (
    -0.9969692112075067 + x2)^2 + (-0.3842501245054024 + x3)^2) + x44 * ((
    -0.9386250621110139 + x1)^2 + (-0.05899573937535463 + x2)^2 + (
    -0.5280008662898733 + x3)^2) + x45 * ((-0.6095783722497654 + x1)^2 + (
    -0.749606887290718 + x2)^2 + (-0.2992084144849715 + x3)^2) + x46 * ((
    -0.3561536887712061 + x1)^2 + (-0.9094619964414011 + x2)^2 + (
    -0.9928171594872911 + x3)^2) + x47 * ((-0.19358485305198325 + x1)^2 + (
    -0.4001073394562492 + x2)^2 + (-0.23357534573815197 + x3)^2) + x48 * ((
    -0.20828547060477265 + x1)^2 + (-0.39644066721668225 + x2)^2 + (
    -0.7362172137618145 + x3)^2) + x49 * ((-0.6396998486147768 + x1)^2 + (
    -0.29482831919895647 + x2)^2 + (-0.14044899013637724 + x3)^2) + x50 * ((
    -0.765643882826654 + x1)^2 + (-0.5765369431382706 + x2)^2 + (
    -0.8522368868434231 + x3)^2) + x51 * ((-0.7690569563429381 + x1)^2 + (
    -0.7237003240191451 + x2)^2 + (-0.5067753597656566 + x3)^2) + x52 * ((
    -0.09159033164075236 + x1)^2 + (-0.6420961033284197 + x2)^2 + (
    -0.6589453156905065 + x3)^2) + x53 * ((-0.3833030263493107 + x1)^2 + (
    -0.3056213143837909 + x2)^2 + (-0.583572623296832 + x3)^2) + x54 * ((
    -0.8769909727391579 + x1)^2 + (-0.34887774782474446 + x2)^2 + (
    -0.23298275093711673 + x3)^2) + x55 * ((-0.9751015775615309 + x1)^2 + (
    -0.5948149927026103 + x2)^2 + (-0.5272848953564142 + x3)^2) + x56 * ((
    -0.8624756249262849 + x1)^2 + (-0.07157238066686311 + x2)^2 + (
    -0.18797844538700537 + x3)^2) + x57 * ((-0.5802216444923713 + x1)^2 + (
    -0.28154327923543976 + x2)^2 + (-0.7283287977057182 + x3)^2) + x58 * ((
    -0.5409120197839667 + x1)^2 + (-0.8821640261603486 + x2)^2 + (
    -0.5803615496795161 + x3)^2) + x59 * ((-0.6617311102373136 + x1)^2 + (
    -0.5654602727098792 + x2)^2 + (-0.3650460577920387 + x3)^2) + x60 * ((
    -0.2716965439825759 + x1)^2 + (-0.9508799282699234 + x2)^2 + (
    -0.9496043117263887 + x3)^2) + x61 * ((-0.2785367614524876 + x1)^2 + (
    -0.00888924443037975 + x2)^2 + (-0.07177626736776488 + x3)^2) + x62 * ((
    -0.9528365858687048 + x1)^2 + (-0.46905249514856384 + x2)^2 + (
    -0.6707205137575432 + x3)^2) + x63 * ((-0.7023602522347626 + x1)^2 + (
    -0.3427485320313549 + x2)^2 + (-0.22119785846142337 + x3)^2) + x64 * ((
    -0.6833230046951964 + x1)^2 + (-0.8900435359063438 + x2)^2 + (
    -0.7350211970604509 + x3)^2) + x65 * ((-0.8050749568015152 + x1)^2 + (
    -0.7744524580155722 + x2)^2 + (-0.048989640268086165 + x3)^2) + x66 * ((
    -0.5857577991141887 + x1)^2 + (-0.7471281757286079 + x2)^2 + (
    -0.7881481567288812 + x3)^2) + x67 * ((-0.05486641693701977 + x1)^2 + (
    -0.538803679037738 + x2)^2 + (-0.524902392193278 + x3)^2) + x68 * ((
    -0.5134214119260625 + x1)^2 + (-0.3442102797771712 + x2)^2 + (
    -0.47072026564786984 + x3)^2) + x69 * ((-0.05779414997019372 + x1)^2 + (
    -0.8020397940471327 + x2)^2 + (-0.9916207714238137 + x3)^2) + x70 * ((
    -0.4189467613554877 + x1)^2 + (-0.7772516522669752 + x2)^2 + (
    -0.9704673132297963 + x3)^2) + x71 * ((-0.6128277861035099 + x1)^2 + (
    -0.8396924728861128 + x2)^2 + (-0.9520573132120294 + x3)^2) + x72 * ((
    -0.8621488398744713 + x1)^2 + (-0.548789075237998 + x2)^2 + (
    -0.7426250614075574 + x3)^2) + x73 * ((-0.7117960119205797 + x1)^2 + (
    -0.39215512790380547 + x2)^2 + (-0.5105264232502463 + x3)^2) + x74 * ((
    -0.22791158112403864 + x1)^2 + (-0.20506688508822635 + x2)^2 + (
    -0.8766388628762738 + x3)^2) + x75 * ((-0.9599249268359679 + x1)^2 + (
    -0.44412520059958527 + x2)^2 + (-0.38557384126798033 + x3)^2) + x76 * ((
    -0.30099374789049604 + x1)^2 + (-0.7579715531726323 + x2)^2 + (
    -0.5127071980951092 + x3)^2) + x77 * ((-0.4484888554980201 + x1)^2 + (
    -0.779019983792056 + x2)^2 + (-0.025865261097519632 + x3)^2) + x78 * ((
    -0.46286867912812435 + x1)^2 + (-0.814167947119447 + x2)^2 + (
    -0.5631048411921744 + x3)^2) + x79 * ((-0.8635903858321241 + x1)^2 + (
    -0.3235246710193893 + x2)^2 + (-0.7181557552325112 + x3)^2) + x80 * ((
    -0.9280940957804614 + x1)^2 + (-0.3453479970944433 + x2)^2 + (
    -0.5613693536456217 + x3)^2) + x81 * ((-0.006316762129101594 + x1)^2 + (
    -0.6031783182970557 + x2)^2 + (-0.28642101465869185 + x3)^2) + x82 * ((
    -0.17739543038776617 + x1)^2 + (-0.5813029219491296 + x2)^2 + (
    -0.5641970476507019 + x3)^2) + x83 * ((-0.8399487209952288 + x1)^2 + (
    -0.09110424417895568 + x2)^2 + (-0.5447723086642006 + x3)^2) + x84 * ((
    -0.6452341591995936 + x1)^2 + (-0.28018562998161844 + x2)^2 + (
    -0.7603427072697793 + x3)^2) + x85 * ((-0.5156422347329462 + x1)^2 + (
    -0.4676899425348692 + x2)^2 + (-0.1136822111961231 + x3)^2) + x86 * ((
    -0.7163586985799302 + x1)^2 + (-0.3372610204232811 + x2)^2 + (
    -0.8370463626853907 + x3)^2) + x87 * ((-0.9756166041963694 + x1)^2 + (
    -0.9612868946752545 + x2)^2 + (-0.7693557667569642 + x3)^2) + x88 * ((
    -0.6113942302805346 + x1)^2 + (-0.13178576707624667 + x2)^2 + (
    -0.9344462725690739 + x3)^2) + x89 * ((-0.5572653802049189 + x1)^2 + (
    -0.5319487140712044 + x2)^2 + (-0.14765227978554551 + x3)^2) + x90 * ((
    -0.11654881530618821 + x1)^2 + (-0.8056950968280207 + x2)^2 + (
    -0.5748478662379017 + x3)^2) + x91 * ((-0.26238920654281517 + x1)^2 + (
    -0.5023734426594167 + x2)^2 + (-0.42130574709860624 + x3)^2) + x92 * ((
    -0.9921980059568194 + x1)^2 + (-0.24115116836317307 + x2)^2 + (
    -0.6976120599289645 + x3)^2) + x93 * ((-0.21728717784157947 + x1)^2 + (
    -0.6420201178343862 + x2)^2 + (-0.8044170696315894 + x3)^2) + x94 * ((
    -0.09611093912226154 + x1)^2 + (-0.9775867468698249 + x2)^2 + (
    -0.4210031582727407 + x3)^2) + x95 * ((-0.049923277911933295 + x1)^2 + (
    -0.25221711356829135 + x2)^2 + (-0.8441636605533569 + x3)^2) + x96 * ((
    -0.3471505964014068 + x1)^2 + (-0.6202794672510638 + x2)^2 + (
    -0.4131303738662405 + x3)^2) + x97 * ((-0.6197762940940301 + x1)^2 + (
    -0.1382483611577 + x2)^2 + (-0.15914304098193788 + x3)^2) + x98 * ((
    -0.6655892821016779 + x1)^2 + (-0.41046211318873815 + x2)^2 + (
    -0.1312748248619422 + x3)^2) + x99 * ((-0.9416510851731662 + x1)^2 + (
    -0.8272647528783726 + x2)^2 + (-0.2714383624447996 + x3)^2) + x100 * ((
    -0.42481890588155824 + x1)^2 + (-0.6159336614459853 + x2)^2 + (
    -0.23967538175236203 + x3)^2) + x101 * ((-0.0358045583876343 + x1)^2 + (
    -0.010894449482712232 + x2)^2 + (-0.6586854665563344 + x3)^2) + x102 * ((
    -0.3025008049226424 + x1)^2 + (-0.24040585456892405 + x2)^2 + (
    -0.7463403103342172 + x3)^2) + x103 * ((-0.6954430403957257 + x1)^2 + (
    -0.12206067459294412 + x2)^2 + (-0.024319631497581096 + x3)^2) + x104 * ((
    -0.25839843172072186 + x1)^2 + (-0.9375128189340426 + x2)^2 + (
    -0.4009543474510294 + x3)^2) + x105 * ((-0.45145378805413694 + x1)^2 + (
    -0.09788835418641062 + x2)^2 + (-0.04872105528074022 + x3)^2) + x106 * ((
    -0.11644110458205315 + x1)^2 + (-0.7605627627985284 + x2)^2 + (
    -0.1923577950664841 + x3)^2) + x107 * ((-0.48447066501151403 + x1)^2 + (
    -0.7509689748452502 + x2)^2 + (-0.9619942070930291 + x3)^2) + x108 * ((
    -0.03508459180153145 + x1)^2 + (-0.5728060027674883 + x2)^2 + (
    -0.7436208452281391 + x3)^2) + x109 * ((-0.032847711659638845 + x1)^2 + (
    -0.5831028234172577 + x2)^2 + (-0.8741038911594665 + x3)^2) + x110 * ((
    -0.46061295403096403 + x1)^2 + (-0.377008556605009 + x2)^2 + (
    -0.2679552753900981 + x3)^2) + x111 * ((-0.2888285878888258 + x1)^2 + (
    -0.034149496184561645 + x2)^2 + (-0.38163177855929187 + x3)^2) + x112 * ((
    -0.5296679821912563 + x1)^2 + (-0.026930445670703906 + x2)^2 + (
    -0.6515536507627563 + x3)^2) + x113 * ((-0.9505325433299335 + x1)^2 + (
    -0.8406353966762972 + x2)^2 + (-0.9979229595662881 + x3)^2) + x114 * ((
    -0.7006669698429467 + x1)^2 + (-0.15718723636793908 + x2)^2 + (
    -0.4324401609471473 + x3)^2) + x115 * ((-0.696521925668867 + x1)^2 + (
    -0.41652540414708084 + x2)^2 + (-0.8580977844829885 + x3)^2) + x116 * ((
    -0.12958880379487892 + x1)^2 + (-0.703981942287015 + x2)^2 + (
    -0.524146756250147 + x3)^2) + x117 * ((-0.9133718781890398 + x1)^2 + (
    -0.7403730745987471 + x2)^2 + (-0.2907239377440496 + x3)^2) + x118 * ((
    -0.19307972709388999 + x1)^2 + (-0.9700461568357024 + x2)^2 + (
    -0.735905755762969 + x3)^2) + x119 * ((-0.11538660650992527 + x1)^2 + (
    -0.2727670397875678 + x2)^2 + (-0.8870259171359532 + x3)^2) + x120 * ((
    -0.7257851436532815 + x1)^2 + (-0.07855129523777848 + x2)^2 + (
    -0.4006634238638799 + x3)^2) + x121 * ((-0.6731181683996974 + x1)^2 + (
    -0.2299158906679658 + x2)^2 + (-0.14224633267260467 + x3)^2) + x122 * ((
    -0.637732077469805 + x4)^2 + (-0.30061635945038845 + x5)^2 + (
    -0.6924078188563045 + x6)^2) + x123 * ((-0.5204622036281865 + x4)^2 + (
    -0.4262380695375112 + x5)^2 + (-0.019757804882570618 + x6)^2) + x124 * ((
    -0.3877676795047561 + x4)^2 + (-0.6261603378186641 + x5)^2 + (
    -0.20807844834808797 + x6)^2) + x125 * ((-0.3455519385475 + x4)^2 + (
    -0.20721956099132388 + x5)^2 + (-0.7536751735394452 + x6)^2) + x126 * ((
    -0.7452291570426526 + x4)^2 + (-0.8288345290542969 + x5)^2 + (
    -0.9101818193634833 + x6)^2) + x127 * ((-0.7088715037487956 + x4)^2 + (
    -0.8675258967244885 + x5)^2 + (-0.04421039019838524 + x6)^2) + x128 * ((
    -0.33645524584418685 + x4)^2 + (-0.24931821641731888 + x5)^2 + (
    -0.24789447471906245 + x6)^2) + x129 * ((-0.39606323961214507 + x4)^2 + (
    -0.5092297648083476 + x5)^2 + (-0.8429822635539893 + x6)^2) + x130 * ((
    -0.3162888023664645 + x4)^2 + (-0.3537176609576351 + x5)^2 + (
    -0.8840601824506505 + x6)^2) + x131 * ((-0.042024431013358066 + x4)^2 + (
    -0.015648799035293925 + x5)^2 + (-0.028897199565620646 + x6)^2) + x132 * ((
    -0.7829982657179482 + x4)^2 + (-0.7604457448591289 + x5)^2 + (
    -0.597334909736347 + x6)^2) + x133 * ((-0.21464482455558387 + x4)^2 + (
    -0.7368895039728377 + x5)^2 + (-0.14158977662661187 + x6)^2) + x134 * ((
    -0.790895349248712 + x4)^2 + (-0.999859654218962 + x5)^2 + (
    -0.7994024450128572 + x6)^2) + x135 * ((-0.15089689559879838 + x4)^2 + (
    -0.2905434515528619 + x5)^2 + (-0.2886420160429456 + x6)^2) + x136 * ((
    -0.9157228230765573 + x4)^2 + (-0.7406305983646623 + x5)^2 + (
    -0.4142557316611599 + x6)^2) + x137 * ((-0.28767980872766563 + x4)^2 + (
    -0.0742772003595773 + x5)^2 + (-0.7235701139213052 + x6)^2) + x138 * ((
    -0.25465347672976957 + x4)^2 + (-0.6409023820345298 + x5)^2 + (
    -0.5494341492685579 + x6)^2) + x139 * ((-0.5541270607350097 + x4)^2 + (
    -0.9692776471334402 + x5)^2 + (-0.05355629576813248 + x6)^2) + x140 * ((
    -0.16592885733639762 + x4)^2 + (-0.6090998523529765 + x5)^2 + (
    -0.007633151339320965 + x6)^2) + x141 * ((-0.9035601490301819 + x4)^2 + (
    -0.09986398472275337 + x5)^2 + (-0.9904466067565432 + x6)^2) + x142 * ((
    -0.7453737555747959 + x4)^2 + (-0.8241163846060925 + x5)^2 + (
    -0.16259034239222492 + x6)^2) + x143 * ((-0.09286618285654225 + x4)^2 + (
    -0.9969692112075067 + x5)^2 + (-0.3842501245054024 + x6)^2) + x144 * ((
    -0.9386250621110139 + x4)^2 + (-0.05899573937535463 + x5)^2 + (
    -0.5280008662898733 + x6)^2) + x145 * ((-0.6095783722497654 + x4)^2 + (
    -0.749606887290718 + x5)^2 + (-0.2992084144849715 + x6)^2) + x146 * ((
    -0.3561536887712061 + x4)^2 + (-0.9094619964414011 + x5)^2 + (
    -0.9928171594872911 + x6)^2) + x147 * ((-0.19358485305198325 + x4)^2 + (
    -0.4001073394562492 + x5)^2 + (-0.23357534573815197 + x6)^2) + x148 * ((
    -0.20828547060477265 + x4)^2 + (-0.39644066721668225 + x5)^2 + (
    -0.7362172137618145 + x6)^2) + x149 * ((-0.6396998486147768 + x4)^2 + (
    -0.29482831919895647 + x5)^2 + (-0.14044899013637724 + x6)^2) + x150 * ((
    -0.765643882826654 + x4)^2 + (-0.5765369431382706 + x5)^2 + (
    -0.8522368868434231 + x6)^2) + x151 * ((-0.7690569563429381 + x4)^2 + (
    -0.7237003240191451 + x5)^2 + (-0.5067753597656566 + x6)^2) + x152 * ((
    -0.09159033164075236 + x4)^2 + (-0.6420961033284197 + x5)^2 + (
    -0.6589453156905065 + x6)^2) + x153 * ((-0.3833030263493107 + x4)^2 + (
    -0.3056213143837909 + x5)^2 + (-0.583572623296832 + x6)^2) + x154 * ((
    -0.8769909727391579 + x4)^2 + (-0.34887774782474446 + x5)^2 + (
    -0.23298275093711673 + x6)^2) + x155 * ((-0.9751015775615309 + x4)^2 + (
    -0.5948149927026103 + x5)^2 + (-0.5272848953564142 + x6)^2) + x156 * ((
    -0.8624756249262849 + x4)^2 + (-0.07157238066686311 + x5)^2 + (
    -0.18797844538700537 + x6)^2) + x157 * ((-0.5802216444923713 + x4)^2 + (
    -0.28154327923543976 + x5)^2 + (-0.7283287977057182 + x6)^2) + x158 * ((
    -0.5409120197839667 + x4)^2 + (-0.8821640261603486 + x5)^2 + (
    -0.5803615496795161 + x6)^2) + x159 * ((-0.6617311102373136 + x4)^2 + (
    -0.5654602727098792 + x5)^2 + (-0.3650460577920387 + x6)^2) + x160 * ((
    -0.2716965439825759 + x4)^2 + (-0.9508799282699234 + x5)^2 + (
    -0.9496043117263887 + x6)^2) + x161 * ((-0.2785367614524876 + x4)^2 + (
    -0.00888924443037975 + x5)^2 + (-0.07177626736776488 + x6)^2) + x162 * ((
    -0.9528365858687048 + x4)^2 + (-0.46905249514856384 + x5)^2 + (
    -0.6707205137575432 + x6)^2) + x163 * ((-0.7023602522347626 + x4)^2 + (
    -0.3427485320313549 + x5)^2 + (-0.22119785846142337 + x6)^2) + x164 * ((
    -0.6833230046951964 + x4)^2 + (-0.8900435359063438 + x5)^2 + (
    -0.7350211970604509 + x6)^2) + x165 * ((-0.8050749568015152 + x4)^2 + (
    -0.7744524580155722 + x5)^2 + (-0.048989640268086165 + x6)^2) + x166 * ((
    -0.5857577991141887 + x4)^2 + (-0.7471281757286079 + x5)^2 + (
    -0.7881481567288812 + x6)^2) + x167 * ((-0.05486641693701977 + x4)^2 + (
    -0.538803679037738 + x5)^2 + (-0.524902392193278 + x6)^2) + x168 * ((
    -0.5134214119260625 + x4)^2 + (-0.3442102797771712 + x5)^2 + (
    -0.47072026564786984 + x6)^2) + x169 * ((-0.05779414997019372 + x4)^2 + (
    -0.8020397940471327 + x5)^2 + (-0.9916207714238137 + x6)^2) + x170 * ((
    -0.4189467613554877 + x4)^2 + (-0.7772516522669752 + x5)^2 + (
    -0.9704673132297963 + x6)^2) + x171 * ((-0.6128277861035099 + x4)^2 + (
    -0.8396924728861128 + x5)^2 + (-0.9520573132120294 + x6)^2) + x172 * ((
    -0.8621488398744713 + x4)^2 + (-0.548789075237998 + x5)^2 + (
    -0.7426250614075574 + x6)^2) + x173 * ((-0.7117960119205797 + x4)^2 + (
    -0.39215512790380547 + x5)^2 + (-0.5105264232502463 + x6)^2) + x174 * ((
    -0.22791158112403864 + x4)^2 + (-0.20506688508822635 + x5)^2 + (
    -0.8766388628762738 + x6)^2) + x175 * ((-0.9599249268359679 + x4)^2 + (
    -0.44412520059958527 + x5)^2 + (-0.38557384126798033 + x6)^2) + x176 * ((
    -0.30099374789049604 + x4)^2 + (-0.7579715531726323 + x5)^2 + (
    -0.5127071980951092 + x6)^2) + x177 * ((-0.4484888554980201 + x4)^2 + (
    -0.779019983792056 + x5)^2 + (-0.025865261097519632 + x6)^2) + x178 * ((
    -0.46286867912812435 + x4)^2 + (-0.814167947119447 + x5)^2 + (
    -0.5631048411921744 + x6)^2) + x179 * ((-0.8635903858321241 + x4)^2 + (
    -0.3235246710193893 + x5)^2 + (-0.7181557552325112 + x6)^2) + x180 * ((
    -0.9280940957804614 + x4)^2 + (-0.3453479970944433 + x5)^2 + (
    -0.5613693536456217 + x6)^2) + x181 * ((-0.006316762129101594 + x4)^2 + (
    -0.6031783182970557 + x5)^2 + (-0.28642101465869185 + x6)^2) + x182 * ((
    -0.17739543038776617 + x4)^2 + (-0.5813029219491296 + x5)^2 + (
    -0.5641970476507019 + x6)^2) + x183 * ((-0.8399487209952288 + x4)^2 + (
    -0.09110424417895568 + x5)^2 + (-0.5447723086642006 + x6)^2) + x184 * ((
    -0.6452341591995936 + x4)^2 + (-0.28018562998161844 + x5)^2 + (
    -0.7603427072697793 + x6)^2) + x185 * ((-0.5156422347329462 + x4)^2 + (
    -0.4676899425348692 + x5)^2 + (-0.1136822111961231 + x6)^2) + x186 * ((
    -0.7163586985799302 + x4)^2 + (-0.3372610204232811 + x5)^2 + (
    -0.8370463626853907 + x6)^2) + x187 * ((-0.9756166041963694 + x4)^2 + (
    -0.9612868946752545 + x5)^2 + (-0.7693557667569642 + x6)^2) + x188 * ((
    -0.6113942302805346 + x4)^2 + (-0.13178576707624667 + x5)^2 + (
    -0.9344462725690739 + x6)^2) + x189 * ((-0.5572653802049189 + x4)^2 + (
    -0.5319487140712044 + x5)^2 + (-0.14765227978554551 + x6)^2) + x190 * ((
    -0.11654881530618821 + x4)^2 + (-0.8056950968280207 + x5)^2 + (
    -0.5748478662379017 + x6)^2) + x191 * ((-0.26238920654281517 + x4)^2 + (
    -0.5023734426594167 + x5)^2 + (-0.42130574709860624 + x6)^2) + x192 * ((
    -0.9921980059568194 + x4)^2 + (-0.24115116836317307 + x5)^2 + (
    -0.6976120599289645 + x6)^2) + x193 * ((-0.21728717784157947 + x4)^2 + (
    -0.6420201178343862 + x5)^2 + (-0.8044170696315894 + x6)^2) + x194 * ((
    -0.09611093912226154 + x4)^2 + (-0.9775867468698249 + x5)^2 + (
    -0.4210031582727407 + x6)^2) + x195 * ((-0.049923277911933295 + x4)^2 + (
    -0.25221711356829135 + x5)^2 + (-0.8441636605533569 + x6)^2) + x196 * ((
    -0.3471505964014068 + x4)^2 + (-0.6202794672510638 + x5)^2 + (
    -0.4131303738662405 + x6)^2) + x197 * ((-0.6197762940940301 + x4)^2 + (
    -0.1382483611577 + x5)^2 + (-0.15914304098193788 + x6)^2) + x198 * ((
    -0.6655892821016779 + x4)^2 + (-0.41046211318873815 + x5)^2 + (
    -0.1312748248619422 + x6)^2) + x199 * ((-0.9416510851731662 + x4)^2 + (
    -0.8272647528783726 + x5)^2 + (-0.2714383624447996 + x6)^2) + x200 * ((
    -0.42481890588155824 + x4)^2 + (-0.6159336614459853 + x5)^2 + (
    -0.23967538175236203 + x6)^2) + x201 * ((-0.0358045583876343 + x4)^2 + (
    -0.010894449482712232 + x5)^2 + (-0.6586854665563344 + x6)^2) + x202 * ((
    -0.3025008049226424 + x4)^2 + (-0.24040585456892405 + x5)^2 + (
    -0.7463403103342172 + x6)^2) + x203 * ((-0.6954430403957257 + x4)^2 + (
    -0.12206067459294412 + x5)^2 + (-0.024319631497581096 + x6)^2) + x204 * ((
    -0.25839843172072186 + x4)^2 + (-0.9375128189340426 + x5)^2 + (
    -0.4009543474510294 + x6)^2) + x205 * ((-0.45145378805413694 + x4)^2 + (
    -0.09788835418641062 + x5)^2 + (-0.04872105528074022 + x6)^2) + x206 * ((
    -0.11644110458205315 + x4)^2 + (-0.7605627627985284 + x5)^2 + (
    -0.1923577950664841 + x6)^2) + x207 * ((-0.48447066501151403 + x4)^2 + (
    -0.7509689748452502 + x5)^2 + (-0.9619942070930291 + x6)^2) + x208 * ((
    -0.03508459180153145 + x4)^2 + (-0.5728060027674883 + x5)^2 + (
    -0.7436208452281391 + x6)^2) + x209 * ((-0.032847711659638845 + x4)^2 + (
    -0.5831028234172577 + x5)^2 + (-0.8741038911594665 + x6)^2) + x210 * ((
    -0.46061295403096403 + x4)^2 + (-0.377008556605009 + x5)^2 + (
    -0.2679552753900981 + x6)^2) + x211 * ((-0.2888285878888258 + x4)^2 + (
    -0.034149496184561645 + x5)^2 + (-0.38163177855929187 + x6)^2) + x212 * ((
    -0.5296679821912563 + x4)^2 + (-0.026930445670703906 + x5)^2 + (
    -0.6515536507627563 + x6)^2) + x213 * ((-0.9505325433299335 + x4)^2 + (
    -0.8406353966762972 + x5)^2 + (-0.9979229595662881 + x6)^2) + x214 * ((
    -0.7006669698429467 + x4)^2 + (-0.15718723636793908 + x5)^2 + (
    -0.4324401609471473 + x6)^2) + x215 * ((-0.696521925668867 + x4)^2 + (
    -0.41652540414708084 + x5)^2 + (-0.8580977844829885 + x6)^2) + x216 * ((
    -0.12958880379487892 + x4)^2 + (-0.703981942287015 + x5)^2 + (
    -0.524146756250147 + x6)^2) + x217 * ((-0.9133718781890398 + x4)^2 + (
    -0.7403730745987471 + x5)^2 + (-0.2907239377440496 + x6)^2) + x218 * ((
    -0.19307972709388999 + x4)^2 + (-0.9700461568357024 + x5)^2 + (
    -0.735905755762969 + x6)^2) + x219 * ((-0.11538660650992527 + x4)^2 + (
    -0.2727670397875678 + x5)^2 + (-0.8870259171359532 + x6)^2) + x220 * ((
    -0.7257851436532815 + x4)^2 + (-0.07855129523777848 + x5)^2 + (
    -0.4006634238638799 + x6)^2) + x221 * ((-0.6731181683996974 + x4)^2 + (
    -0.2299158906679658 + x5)^2 + (-0.14224633267260467 + x6)^2) + x222 * ((
    -0.637732077469805 + x7)^2 + (-0.30061635945038845 + x8)^2 + (
    -0.6924078188563045 + x9)^2) + x223 * ((-0.5204622036281865 + x7)^2 + (
    -0.4262380695375112 + x8)^2 + (-0.019757804882570618 + x9)^2) + x224 * ((
    -0.3877676795047561 + x7)^2 + (-0.6261603378186641 + x8)^2 + (
    -0.20807844834808797 + x9)^2) + x225 * ((-0.3455519385475 + x7)^2 + (
    -0.20721956099132388 + x8)^2 + (-0.7536751735394452 + x9)^2) + x226 * ((
    -0.7452291570426526 + x7)^2 + (-0.8288345290542969 + x8)^2 + (
    -0.9101818193634833 + x9)^2) + x227 * ((-0.7088715037487956 + x7)^2 + (
    -0.8675258967244885 + x8)^2 + (-0.04421039019838524 + x9)^2) + x228 * ((
    -0.33645524584418685 + x7)^2 + (-0.24931821641731888 + x8)^2 + (
    -0.24789447471906245 + x9)^2) + x229 * ((-0.39606323961214507 + x7)^2 + (
    -0.5092297648083476 + x8)^2 + (-0.8429822635539893 + x9)^2) + x230 * ((
    -0.3162888023664645 + x7)^2 + (-0.3537176609576351 + x8)^2 + (
    -0.8840601824506505 + x9)^2) + x231 * ((-0.042024431013358066 + x7)^2 + (
    -0.015648799035293925 + x8)^2 + (-0.028897199565620646 + x9)^2) + x232 * ((
    -0.7829982657179482 + x7)^2 + (-0.7604457448591289 + x8)^2 + (
    -0.597334909736347 + x9)^2) + x233 * ((-0.21464482455558387 + x7)^2 + (
    -0.7368895039728377 + x8)^2 + (-0.14158977662661187 + x9)^2) + x234 * ((
    -0.790895349248712 + x7)^2 + (-0.999859654218962 + x8)^2 + (
    -0.7994024450128572 + x9)^2) + x235 * ((-0.15089689559879838 + x7)^2 + (
    -0.2905434515528619 + x8)^2 + (-0.2886420160429456 + x9)^2) + x236 * ((
    -0.9157228230765573 + x7)^2 + (-0.7406305983646623 + x8)^2 + (
    -0.4142557316611599 + x9)^2) + x237 * ((-0.28767980872766563 + x7)^2 + (
    -0.0742772003595773 + x8)^2 + (-0.7235701139213052 + x9)^2) + x238 * ((
    -0.25465347672976957 + x7)^2 + (-0.6409023820345298 + x8)^2 + (
    -0.5494341492685579 + x9)^2) + x239 * ((-0.5541270607350097 + x7)^2 + (
    -0.9692776471334402 + x8)^2 + (-0.05355629576813248 + x9)^2) + x240 * ((
    -0.16592885733639762 + x7)^2 + (-0.6090998523529765 + x8)^2 + (
    -0.007633151339320965 + x9)^2) + x241 * ((-0.9035601490301819 + x7)^2 + (
    -0.09986398472275337 + x8)^2 + (-0.9904466067565432 + x9)^2) + x242 * ((
    -0.7453737555747959 + x7)^2 + (-0.8241163846060925 + x8)^2 + (
    -0.16259034239222492 + x9)^2) + x243 * ((-0.09286618285654225 + x7)^2 + (
    -0.9969692112075067 + x8)^2 + (-0.3842501245054024 + x9)^2) + x244 * ((
    -0.9386250621110139 + x7)^2 + (-0.05899573937535463 + x8)^2 + (
    -0.5280008662898733 + x9)^2) + x245 * ((-0.6095783722497654 + x7)^2 + (
    -0.749606887290718 + x8)^2 + (-0.2992084144849715 + x9)^2) + x246 * ((
    -0.3561536887712061 + x7)^2 + (-0.9094619964414011 + x8)^2 + (
    -0.9928171594872911 + x9)^2) + x247 * ((-0.19358485305198325 + x7)^2 + (
    -0.4001073394562492 + x8)^2 + (-0.23357534573815197 + x9)^2) + x248 * ((
    -0.20828547060477265 + x7)^2 + (-0.39644066721668225 + x8)^2 + (
    -0.7362172137618145 + x9)^2) + x249 * ((-0.6396998486147768 + x7)^2 + (
    -0.29482831919895647 + x8)^2 + (-0.14044899013637724 + x9)^2) + x250 * ((
    -0.765643882826654 + x7)^2 + (-0.5765369431382706 + x8)^2 + (
    -0.8522368868434231 + x9)^2) + x251 * ((-0.7690569563429381 + x7)^2 + (
    -0.7237003240191451 + x8)^2 + (-0.5067753597656566 + x9)^2) + x252 * ((
    -0.09159033164075236 + x7)^2 + (-0.6420961033284197 + x8)^2 + (
    -0.6589453156905065 + x9)^2) + x253 * ((-0.3833030263493107 + x7)^2 + (
    -0.3056213143837909 + x8)^2 + (-0.583572623296832 + x9)^2) + x254 * ((
    -0.8769909727391579 + x7)^2 + (-0.34887774782474446 + x8)^2 + (
    -0.23298275093711673 + x9)^2) + x255 * ((-0.9751015775615309 + x7)^2 + (
    -0.5948149927026103 + x8)^2 + (-0.5272848953564142 + x9)^2) + x256 * ((
    -0.8624756249262849 + x7)^2 + (-0.07157238066686311 + x8)^2 + (
    -0.18797844538700537 + x9)^2) + x257 * ((-0.5802216444923713 + x7)^2 + (
    -0.28154327923543976 + x8)^2 + (-0.7283287977057182 + x9)^2) + x258 * ((
    -0.5409120197839667 + x7)^2 + (-0.8821640261603486 + x8)^2 + (
    -0.5803615496795161 + x9)^2) + x259 * ((-0.6617311102373136 + x7)^2 + (
    -0.5654602727098792 + x8)^2 + (-0.3650460577920387 + x9)^2) + x260 * ((
    -0.2716965439825759 + x7)^2 + (-0.9508799282699234 + x8)^2 + (
    -0.9496043117263887 + x9)^2) + x261 * ((-0.2785367614524876 + x7)^2 + (
    -0.00888924443037975 + x8)^2 + (-0.07177626736776488 + x9)^2) + x262 * ((
    -0.9528365858687048 + x7)^2 + (-0.46905249514856384 + x8)^2 + (
    -0.6707205137575432 + x9)^2) + x263 * ((-0.7023602522347626 + x7)^2 + (
    -0.3427485320313549 + x8)^2 + (-0.22119785846142337 + x9)^2) + x264 * ((
    -0.6833230046951964 + x7)^2 + (-0.8900435359063438 + x8)^2 + (
    -0.7350211970604509 + x9)^2) + x265 * ((-0.8050749568015152 + x7)^2 + (
    -0.7744524580155722 + x8)^2 + (-0.048989640268086165 + x9)^2) + x266 * ((
    -0.5857577991141887 + x7)^2 + (-0.7471281757286079 + x8)^2 + (
    -0.7881481567288812 + x9)^2) + x267 * ((-0.05486641693701977 + x7)^2 + (
    -0.538803679037738 + x8)^2 + (-0.524902392193278 + x9)^2) + x268 * ((
    -0.5134214119260625 + x7)^2 + (-0.3442102797771712 + x8)^2 + (
    -0.47072026564786984 + x9)^2) + x269 * ((-0.05779414997019372 + x7)^2 + (
    -0.8020397940471327 + x8)^2 + (-0.9916207714238137 + x9)^2) + x270 * ((
    -0.4189467613554877 + x7)^2 + (-0.7772516522669752 + x8)^2 + (
    -0.9704673132297963 + x9)^2) + x271 * ((-0.6128277861035099 + x7)^2 + (
    -0.8396924728861128 + x8)^2 + (-0.9520573132120294 + x9)^2) + x272 * ((
    -0.8621488398744713 + x7)^2 + (-0.548789075237998 + x8)^2 + (
    -0.7426250614075574 + x9)^2) + x273 * ((-0.7117960119205797 + x7)^2 + (
    -0.39215512790380547 + x8)^2 + (-0.5105264232502463 + x9)^2) + x274 * ((
    -0.22791158112403864 + x7)^2 + (-0.20506688508822635 + x8)^2 + (
    -0.8766388628762738 + x9)^2) + x275 * ((-0.9599249268359679 + x7)^2 + (
    -0.44412520059958527 + x8)^2 + (-0.38557384126798033 + x9)^2) + x276 * ((
    -0.30099374789049604 + x7)^2 + (-0.7579715531726323 + x8)^2 + (
    -0.5127071980951092 + x9)^2) + x277 * ((-0.4484888554980201 + x7)^2 + (
    -0.779019983792056 + x8)^2 + (-0.025865261097519632 + x9)^2) + x278 * ((
    -0.46286867912812435 + x7)^2 + (-0.814167947119447 + x8)^2 + (
    -0.5631048411921744 + x9)^2) + x279 * ((-0.8635903858321241 + x7)^2 + (
    -0.3235246710193893 + x8)^2 + (-0.7181557552325112 + x9)^2) + x280 * ((
    -0.9280940957804614 + x7)^2 + (-0.3453479970944433 + x8)^2 + (
    -0.5613693536456217 + x9)^2) + x281 * ((-0.006316762129101594 + x7)^2 + (
    -0.6031783182970557 + x8)^2 + (-0.28642101465869185 + x9)^2) + x282 * ((
    -0.17739543038776617 + x7)^2 + (-0.5813029219491296 + x8)^2 + (
    -0.5641970476507019 + x9)^2) + x283 * ((-0.8399487209952288 + x7)^2 + (
    -0.09110424417895568 + x8)^2 + (-0.5447723086642006 + x9)^2) + x284 * ((
    -0.6452341591995936 + x7)^2 + (-0.28018562998161844 + x8)^2 + (
    -0.7603427072697793 + x9)^2) + x285 * ((-0.5156422347329462 + x7)^2 + (
    -0.4676899425348692 + x8)^2 + (-0.1136822111961231 + x9)^2) + x286 * ((
    -0.7163586985799302 + x7)^2 + (-0.3372610204232811 + x8)^2 + (
    -0.8370463626853907 + x9)^2) + x287 * ((-0.9756166041963694 + x7)^2 + (
    -0.9612868946752545 + x8)^2 + (-0.7693557667569642 + x9)^2) + x288 * ((
    -0.6113942302805346 + x7)^2 + (-0.13178576707624667 + x8)^2 + (
    -0.9344462725690739 + x9)^2) + x289 * ((-0.5572653802049189 + x7)^2 + (
    -0.5319487140712044 + x8)^2 + (-0.14765227978554551 + x9)^2) + x290 * ((
    -0.11654881530618821 + x7)^2 + (-0.8056950968280207 + x8)^2 + (
    -0.5748478662379017 + x9)^2) + x291 * ((-0.26238920654281517 + x7)^2 + (
    -0.5023734426594167 + x8)^2 + (-0.42130574709860624 + x9)^2) + x292 * ((
    -0.9921980059568194 + x7)^2 + (-0.24115116836317307 + x8)^2 + (
    -0.6976120599289645 + x9)^2) + x293 * ((-0.21728717784157947 + x7)^2 + (
    -0.6420201178343862 + x8)^2 + (-0.8044170696315894 + x9)^2) + x294 * ((
    -0.09611093912226154 + x7)^2 + (-0.9775867468698249 + x8)^2 + (
    -0.4210031582727407 + x9)^2) + x295 * ((-0.049923277911933295 + x7)^2 + (
    -0.25221711356829135 + x8)^2 + (-0.8441636605533569 + x9)^2) + x296 * ((
    -0.3471505964014068 + x7)^2 + (-0.6202794672510638 + x8)^2 + (
    -0.4131303738662405 + x9)^2) + x297 * ((-0.6197762940940301 + x7)^2 + (
    -0.1382483611577 + x8)^2 + (-0.15914304098193788 + x9)^2) + x298 * ((
    -0.6655892821016779 + x7)^2 + (-0.41046211318873815 + x8)^2 + (
    -0.1312748248619422 + x9)^2) + x299 * ((-0.9416510851731662 + x7)^2 + (
    -0.8272647528783726 + x8)^2 + (-0.2714383624447996 + x9)^2) + x300 * ((
    -0.42481890588155824 + x7)^2 + (-0.6159336614459853 + x8)^2 + (
    -0.23967538175236203 + x9)^2) + x301 * ((-0.0358045583876343 + x7)^2 + (
    -0.010894449482712232 + x8)^2 + (-0.6586854665563344 + x9)^2) + x302 * ((
    -0.3025008049226424 + x7)^2 + (-0.24040585456892405 + x8)^2 + (
    -0.7463403103342172 + x9)^2) + x303 * ((-0.6954430403957257 + x7)^2 + (
    -0.12206067459294412 + x8)^2 + (-0.024319631497581096 + x9)^2) + x304 * ((
    -0.25839843172072186 + x7)^2 + (-0.9375128189340426 + x8)^2 + (
    -0.4009543474510294 + x9)^2) + x305 * ((-0.45145378805413694 + x7)^2 + (
    -0.09788835418641062 + x8)^2 + (-0.04872105528074022 + x9)^2) + x306 * ((
    -0.11644110458205315 + x7)^2 + (-0.7605627627985284 + x8)^2 + (
    -0.1923577950664841 + x9)^2) + x307 * ((-0.48447066501151403 + x7)^2 + (
    -0.7509689748452502 + x8)^2 + (-0.9619942070930291 + x9)^2) + x308 * ((
    -0.03508459180153145 + x7)^2 + (-0.5728060027674883 + x8)^2 + (
    -0.7436208452281391 + x9)^2) + x309 * ((-0.032847711659638845 + x7)^2 + (
    -0.5831028234172577 + x8)^2 + (-0.8741038911594665 + x9)^2) + x310 * ((
    -0.46061295403096403 + x7)^2 + (-0.377008556605009 + x8)^2 + (
    -0.2679552753900981 + x9)^2) + x311 * ((-0.2888285878888258 + x7)^2 + (
    -0.034149496184561645 + x8)^2 + (-0.38163177855929187 + x9)^2) + x312 * ((
    -0.5296679821912563 + x7)^2 + (-0.026930445670703906 + x8)^2 + (
    -0.6515536507627563 + x9)^2) + x313 * ((-0.9505325433299335 + x7)^2 + (
    -0.8406353966762972 + x8)^2 + (-0.9979229595662881 + x9)^2) + x314 * ((
    -0.7006669698429467 + x7)^2 + (-0.15718723636793908 + x8)^2 + (
    -0.4324401609471473 + x9)^2) + x315 * ((-0.696521925668867 + x7)^2 + (
    -0.41652540414708084 + x8)^2 + (-0.8580977844829885 + x9)^2) + x316 * ((
    -0.12958880379487892 + x7)^2 + (-0.703981942287015 + x8)^2 + (
    -0.524146756250147 + x9)^2) + x317 * ((-0.9133718781890398 + x7)^2 + (
    -0.7403730745987471 + x8)^2 + (-0.2907239377440496 + x9)^2) + x318 * ((
    -0.19307972709388999 + x7)^2 + (-0.9700461568357024 + x8)^2 + (
    -0.735905755762969 + x9)^2) + x319 * ((-0.11538660650992527 + x7)^2 + (
    -0.2727670397875678 + x8)^2 + (-0.8870259171359532 + x9)^2) + x320 * ((
    -0.7257851436532815 + x7)^2 + (-0.07855129523777848 + x8)^2 + (
    -0.4006634238638799 + x9)^2) + x321 * ((-0.6731181683996974 + x7)^2 + (
    -0.2299158906679658 + x8)^2 + (-0.14224633267260467 + x9)^2) + x322 * ((
    -0.637732077469805 + x10)^2 + (-0.30061635945038845 + x11)^2 + (
    -0.6924078188563045 + x12)^2) + x323 * ((-0.5204622036281865 + x10)^2 + (
    -0.4262380695375112 + x11)^2 + (-0.019757804882570618 + x12)^2) + x324 * ((
    -0.3877676795047561 + x10)^2 + (-0.6261603378186641 + x11)^2 + (
    -0.20807844834808797 + x12)^2) + x325 * ((-0.3455519385475 + x10)^2 + (
    -0.20721956099132388 + x11)^2 + (-0.7536751735394452 + x12)^2) + x326 * ((
    -0.7452291570426526 + x10)^2 + (-0.8288345290542969 + x11)^2 + (
    -0.9101818193634833 + x12)^2) + x327 * ((-0.7088715037487956 + x10)^2 + (
    -0.8675258967244885 + x11)^2 + (-0.04421039019838524 + x12)^2) + x328 * ((
    -0.33645524584418685 + x10)^2 + (-0.24931821641731888 + x11)^2 + (
    -0.24789447471906245 + x12)^2) + x329 * ((-0.39606323961214507 + x10)^2 + (
    -0.5092297648083476 + x11)^2 + (-0.8429822635539893 + x12)^2) + x330 * ((
    -0.3162888023664645 + x10)^2 + (-0.3537176609576351 + x11)^2 + (
    -0.8840601824506505 + x12)^2) + x331 * ((-0.042024431013358066 + x10)^2 + (
    -0.015648799035293925 + x11)^2 + (-0.028897199565620646 + x12)^2) + x332 *
    ((-0.7829982657179482 + x10)^2 + (-0.7604457448591289 + x11)^2 + (
    -0.597334909736347 + x12)^2) + x333 * ((-0.21464482455558387 + x10)^2 + (
    -0.7368895039728377 + x11)^2 + (-0.14158977662661187 + x12)^2) + x334 * ((
    -0.790895349248712 + x10)^2 + (-0.999859654218962 + x11)^2 + (
    -0.7994024450128572 + x12)^2) + x335 * ((-0.15089689559879838 + x10)^2 + (
    -0.2905434515528619 + x11)^2 + (-0.2886420160429456 + x12)^2) + x336 * ((
    -0.9157228230765573 + x10)^2 + (-0.7406305983646623 + x11)^2 + (
    -0.4142557316611599 + x12)^2) + x337 * ((-0.28767980872766563 + x10)^2 + (
    -0.0742772003595773 + x11)^2 + (-0.7235701139213052 + x12)^2) + x338 * ((
    -0.25465347672976957 + x10)^2 + (-0.6409023820345298 + x11)^2 + (
    -0.5494341492685579 + x12)^2) + x339 * ((-0.5541270607350097 + x10)^2 + (
    -0.9692776471334402 + x11)^2 + (-0.05355629576813248 + x12)^2) + x340 * ((
    -0.16592885733639762 + x10)^2 + (-0.6090998523529765 + x11)^2 + (
    -0.007633151339320965 + x12)^2) + x341 * ((-0.9035601490301819 + x10)^2 + (
    -0.09986398472275337 + x11)^2 + (-0.9904466067565432 + x12)^2) + x342 * ((
    -0.7453737555747959 + x10)^2 + (-0.8241163846060925 + x11)^2 + (
    -0.16259034239222492 + x12)^2) + x343 * ((-0.09286618285654225 + x10)^2 + (
    -0.9969692112075067 + x11)^2 + (-0.3842501245054024 + x12)^2) + x344 * ((
    -0.9386250621110139 + x10)^2 + (-0.05899573937535463 + x11)^2 + (
    -0.5280008662898733 + x12)^2) + x345 * ((-0.6095783722497654 + x10)^2 + (
    -0.749606887290718 + x11)^2 + (-0.2992084144849715 + x12)^2) + x346 * ((
    -0.3561536887712061 + x10)^2 + (-0.9094619964414011 + x11)^2 + (
    -0.9928171594872911 + x12)^2) + x347 * ((-0.19358485305198325 + x10)^2 + (
    -0.4001073394562492 + x11)^2 + (-0.23357534573815197 + x12)^2) + x348 * ((
    -0.20828547060477265 + x10)^2 + (-0.39644066721668225 + x11)^2 + (
    -0.7362172137618145 + x12)^2) + x349 * ((-0.6396998486147768 + x10)^2 + (
    -0.29482831919895647 + x11)^2 + (-0.14044899013637724 + x12)^2) + x350 * ((
    -0.765643882826654 + x10)^2 + (-0.5765369431382706 + x11)^2 + (
    -0.8522368868434231 + x12)^2) + x351 * ((-0.7690569563429381 + x10)^2 + (
    -0.7237003240191451 + x11)^2 + (-0.5067753597656566 + x12)^2) + x352 * ((
    -0.09159033164075236 + x10)^2 + (-0.6420961033284197 + x11)^2 + (
    -0.6589453156905065 + x12)^2) + x353 * ((-0.3833030263493107 + x10)^2 + (
    -0.3056213143837909 + x11)^2 + (-0.583572623296832 + x12)^2) + x354 * ((
    -0.8769909727391579 + x10)^2 + (-0.34887774782474446 + x11)^2 + (
    -0.23298275093711673 + x12)^2) + x355 * ((-0.9751015775615309 + x10)^2 + (
    -0.5948149927026103 + x11)^2 + (-0.5272848953564142 + x12)^2) + x356 * ((
    -0.8624756249262849 + x10)^2 + (-0.07157238066686311 + x11)^2 + (
    -0.18797844538700537 + x12)^2) + x357 * ((-0.5802216444923713 + x10)^2 + (
    -0.28154327923543976 + x11)^2 + (-0.7283287977057182 + x12)^2) + x358 * ((
    -0.5409120197839667 + x10)^2 + (-0.8821640261603486 + x11)^2 + (
    -0.5803615496795161 + x12)^2) + x359 * ((-0.6617311102373136 + x10)^2 + (
    -0.5654602727098792 + x11)^2 + (-0.3650460577920387 + x12)^2) + x360 * ((
    -0.2716965439825759 + x10)^2 + (-0.9508799282699234 + x11)^2 + (
    -0.9496043117263887 + x12)^2) + x361 * ((-0.2785367614524876 + x10)^2 + (
    -0.00888924443037975 + x11)^2 + (-0.07177626736776488 + x12)^2) + x362 * ((
    -0.9528365858687048 + x10)^2 + (-0.46905249514856384 + x11)^2 + (
    -0.6707205137575432 + x12)^2) + x363 * ((-0.7023602522347626 + x10)^2 + (
    -0.3427485320313549 + x11)^2 + (-0.22119785846142337 + x12)^2) + x364 * ((
    -0.6833230046951964 + x10)^2 + (-0.8900435359063438 + x11)^2 + (
    -0.7350211970604509 + x12)^2) + x365 * ((-0.8050749568015152 + x10)^2 + (
    -0.7744524580155722 + x11)^2 + (-0.048989640268086165 + x12)^2) + x366 * ((
    -0.5857577991141887 + x10)^2 + (-0.7471281757286079 + x11)^2 + (
    -0.7881481567288812 + x12)^2) + x367 * ((-0.05486641693701977 + x10)^2 + (
    -0.538803679037738 + x11)^2 + (-0.524902392193278 + x12)^2) + x368 * ((
    -0.5134214119260625 + x10)^2 + (-0.3442102797771712 + x11)^2 + (
    -0.47072026564786984 + x12)^2) + x369 * ((-0.05779414997019372 + x10)^2 + (
    -0.8020397940471327 + x11)^2 + (-0.9916207714238137 + x12)^2) + x370 * ((
    -0.4189467613554877 + x10)^2 + (-0.7772516522669752 + x11)^2 + (
    -0.9704673132297963 + x12)^2) + x371 * ((-0.6128277861035099 + x10)^2 + (
    -0.8396924728861128 + x11)^2 + (-0.9520573132120294 + x12)^2) + x372 * ((
    -0.8621488398744713 + x10)^2 + (-0.548789075237998 + x11)^2 + (
    -0.7426250614075574 + x12)^2) + x373 * ((-0.7117960119205797 + x10)^2 + (
    -0.39215512790380547 + x11)^2 + (-0.5105264232502463 + x12)^2) + x374 * ((
    -0.22791158112403864 + x10)^2 + (-0.20506688508822635 + x11)^2 + (
    -0.8766388628762738 + x12)^2) + x375 * ((-0.9599249268359679 + x10)^2 + (
    -0.44412520059958527 + x11)^2 + (-0.38557384126798033 + x12)^2) + x376 * ((
    -0.30099374789049604 + x10)^2 + (-0.7579715531726323 + x11)^2 + (
    -0.5127071980951092 + x12)^2) + x377 * ((-0.4484888554980201 + x10)^2 + (
    -0.779019983792056 + x11)^2 + (-0.025865261097519632 + x12)^2) + x378 * ((
    -0.46286867912812435 + x10)^2 + (-0.814167947119447 + x11)^2 + (
    -0.5631048411921744 + x12)^2) + x379 * ((-0.8635903858321241 + x10)^2 + (
    -0.3235246710193893 + x11)^2 + (-0.7181557552325112 + x12)^2) + x380 * ((
    -0.9280940957804614 + x10)^2 + (-0.3453479970944433 + x11)^2 + (
    -0.5613693536456217 + x12)^2) + x381 * ((-0.006316762129101594 + x10)^2 + (
    -0.6031783182970557 + x11)^2 + (-0.28642101465869185 + x12)^2) + x382 * ((
    -0.17739543038776617 + x10)^2 + (-0.5813029219491296 + x11)^2 + (
    -0.5641970476507019 + x12)^2) + x383 * ((-0.8399487209952288 + x10)^2 + (
    -0.09110424417895568 + x11)^2 + (-0.5447723086642006 + x12)^2) + x384 * ((
    -0.6452341591995936 + x10)^2 + (-0.28018562998161844 + x11)^2 + (
    -0.7603427072697793 + x12)^2) + x385 * ((-0.5156422347329462 + x10)^2 + (
    -0.4676899425348692 + x11)^2 + (-0.1136822111961231 + x12)^2) + x386 * ((
    -0.7163586985799302 + x10)^2 + (-0.3372610204232811 + x11)^2 + (
    -0.8370463626853907 + x12)^2) + x387 * ((-0.9756166041963694 + x10)^2 + (
    -0.9612868946752545 + x11)^2 + (-0.7693557667569642 + x12)^2) + x388 * ((
    -0.6113942302805346 + x10)^2 + (-0.13178576707624667 + x11)^2 + (
    -0.9344462725690739 + x12)^2) + x389 * ((-0.5572653802049189 + x10)^2 + (
    -0.5319487140712044 + x11)^2 + (-0.14765227978554551 + x12)^2) + x390 * ((
    -0.11654881530618821 + x10)^2 + (-0.8056950968280207 + x11)^2 + (
    -0.5748478662379017 + x12)^2) + x391 * ((-0.26238920654281517 + x10)^2 + (
    -0.5023734426594167 + x11)^2 + (-0.42130574709860624 + x12)^2) + x392 * ((
    -0.9921980059568194 + x10)^2 + (-0.24115116836317307 + x11)^2 + (
    -0.6976120599289645 + x12)^2) + x393 * ((-0.21728717784157947 + x10)^2 + (
    -0.6420201178343862 + x11)^2 + (-0.8044170696315894 + x12)^2) + x394 * ((
    -0.09611093912226154 + x10)^2 + (-0.9775867468698249 + x11)^2 + (
    -0.4210031582727407 + x12)^2) + x395 * ((-0.049923277911933295 + x10)^2 + (
    -0.25221711356829135 + x11)^2 + (-0.8441636605533569 + x12)^2) + x396 * ((
    -0.3471505964014068 + x10)^2 + (-0.6202794672510638 + x11)^2 + (
    -0.4131303738662405 + x12)^2) + x397 * ((-0.6197762940940301 + x10)^2 + (
    -0.1382483611577 + x11)^2 + (-0.15914304098193788 + x12)^2) + x398 * ((
    -0.6655892821016779 + x10)^2 + (-0.41046211318873815 + x11)^2 + (
    -0.1312748248619422 + x12)^2) + x399 * ((-0.9416510851731662 + x10)^2 + (
    -0.8272647528783726 + x11)^2 + (-0.2714383624447996 + x12)^2) + x400 * ((
    -0.42481890588155824 + x10)^2 + (-0.6159336614459853 + x11)^2 + (
    -0.23967538175236203 + x12)^2) + x401 * ((-0.0358045583876343 + x10)^2 + (
    -0.010894449482712232 + x11)^2 + (-0.6586854665563344 + x12)^2) + x402 * ((
    -0.3025008049226424 + x10)^2 + (-0.24040585456892405 + x11)^2 + (
    -0.7463403103342172 + x12)^2) + x403 * ((-0.6954430403957257 + x10)^2 + (
    -0.12206067459294412 + x11)^2 + (-0.024319631497581096 + x12)^2) + x404 * (
    (-0.25839843172072186 + x10)^2 + (-0.9375128189340426 + x11)^2 + (
    -0.4009543474510294 + x12)^2) + x405 * ((-0.45145378805413694 + x10)^2 + (
    -0.09788835418641062 + x11)^2 + (-0.04872105528074022 + x12)^2) + x406 * ((
    -0.11644110458205315 + x10)^2 + (-0.7605627627985284 + x11)^2 + (
    -0.1923577950664841 + x12)^2) + x407 * ((-0.48447066501151403 + x10)^2 + (
    -0.7509689748452502 + x11)^2 + (-0.9619942070930291 + x12)^2) + x408 * ((
    -0.03508459180153145 + x10)^2 + (-0.5728060027674883 + x11)^2 + (
    -0.7436208452281391 + x12)^2) + x409 * ((-0.032847711659638845 + x10)^2 + (
    -0.5831028234172577 + x11)^2 + (-0.8741038911594665 + x12)^2) + x410 * ((
    -0.46061295403096403 + x10)^2 + (-0.377008556605009 + x11)^2 + (
    -0.2679552753900981 + x12)^2) + x411 * ((-0.2888285878888258 + x10)^2 + (
    -0.034149496184561645 + x11)^2 + (-0.38163177855929187 + x12)^2) + x412 * (
    (-0.5296679821912563 + x10)^2 + (-0.026930445670703906 + x11)^2 + (
    -0.6515536507627563 + x12)^2) + x413 * ((-0.9505325433299335 + x10)^2 + (
    -0.8406353966762972 + x11)^2 + (-0.9979229595662881 + x12)^2) + x414 * ((
    -0.7006669698429467 + x10)^2 + (-0.15718723636793908 + x11)^2 + (
    -0.4324401609471473 + x12)^2) + x415 * ((-0.696521925668867 + x10)^2 + (
    -0.41652540414708084 + x11)^2 + (-0.8580977844829885 + x12)^2) + x416 * ((
    -0.12958880379487892 + x10)^2 + (-0.703981942287015 + x11)^2 + (
    -0.524146756250147 + x12)^2) + x417 * ((-0.9133718781890398 + x10)^2 + (
    -0.7403730745987471 + x11)^2 + (-0.2907239377440496 + x12)^2) + x418 * ((
    -0.19307972709388999 + x10)^2 + (-0.9700461568357024 + x11)^2 + (
    -0.735905755762969 + x12)^2) + x419 * ((-0.11538660650992527 + x10)^2 + (
    -0.2727670397875678 + x11)^2 + (-0.8870259171359532 + x12)^2) + x420 * ((
    -0.7257851436532815 + x10)^2 + (-0.07855129523777848 + x11)^2 + (
    -0.4006634238638799 + x12)^2) + x421 * ((-0.6731181683996974 + x10)^2 + (
    -0.2299158906679658 + x11)^2 + (-0.14224633267260467 + x12)^2) + x422 * ((
    -0.637732077469805 + x13)^2 + (-0.30061635945038845 + x14)^2 + (
    -0.6924078188563045 + x15)^2) + x423 * ((-0.5204622036281865 + x13)^2 + (
    -0.4262380695375112 + x14)^2 + (-0.019757804882570618 + x15)^2) + x424 * ((
    -0.3877676795047561 + x13)^2 + (-0.6261603378186641 + x14)^2 + (
    -0.20807844834808797 + x15)^2) + x425 * ((-0.3455519385475 + x13)^2 + (
    -0.20721956099132388 + x14)^2 + (-0.7536751735394452 + x15)^2) + x426 * ((
    -0.7452291570426526 + x13)^2 + (-0.8288345290542969 + x14)^2 + (
    -0.9101818193634833 + x15)^2) + x427 * ((-0.7088715037487956 + x13)^2 + (
    -0.8675258967244885 + x14)^2 + (-0.04421039019838524 + x15)^2) + x428 * ((
    -0.33645524584418685 + x13)^2 + (-0.24931821641731888 + x14)^2 + (
    -0.24789447471906245 + x15)^2) + x429 * ((-0.39606323961214507 + x13)^2 + (
    -0.5092297648083476 + x14)^2 + (-0.8429822635539893 + x15)^2) + x430 * ((
    -0.3162888023664645 + x13)^2 + (-0.3537176609576351 + x14)^2 + (
    -0.8840601824506505 + x15)^2) + x431 * ((-0.042024431013358066 + x13)^2 + (
    -0.015648799035293925 + x14)^2 + (-0.028897199565620646 + x15)^2) + x432 *
    ((-0.7829982657179482 + x13)^2 + (-0.7604457448591289 + x14)^2 + (
    -0.597334909736347 + x15)^2) + x433 * ((-0.21464482455558387 + x13)^2 + (
    -0.7368895039728377 + x14)^2 + (-0.14158977662661187 + x15)^2) + x434 * ((
    -0.790895349248712 + x13)^2 + (-0.999859654218962 + x14)^2 + (
    -0.7994024450128572 + x15)^2) + x435 * ((-0.15089689559879838 + x13)^2 + (
    -0.2905434515528619 + x14)^2 + (-0.2886420160429456 + x15)^2) + x436 * ((
    -0.9157228230765573 + x13)^2 + (-0.7406305983646623 + x14)^2 + (
    -0.4142557316611599 + x15)^2) + x437 * ((-0.28767980872766563 + x13)^2 + (
    -0.0742772003595773 + x14)^2 + (-0.7235701139213052 + x15)^2) + x438 * ((
    -0.25465347672976957 + x13)^2 + (-0.6409023820345298 + x14)^2 + (
    -0.5494341492685579 + x15)^2) + x439 * ((-0.5541270607350097 + x13)^2 + (
    -0.9692776471334402 + x14)^2 + (-0.05355629576813248 + x15)^2) + x440 * ((
    -0.16592885733639762 + x13)^2 + (-0.6090998523529765 + x14)^2 + (
    -0.007633151339320965 + x15)^2) + x441 * ((-0.9035601490301819 + x13)^2 + (
    -0.09986398472275337 + x14)^2 + (-0.9904466067565432 + x15)^2) + x442 * ((
    -0.7453737555747959 + x13)^2 + (-0.8241163846060925 + x14)^2 + (
    -0.16259034239222492 + x15)^2) + x443 * ((-0.09286618285654225 + x13)^2 + (
    -0.9969692112075067 + x14)^2 + (-0.3842501245054024 + x15)^2) + x444 * ((
    -0.9386250621110139 + x13)^2 + (-0.05899573937535463 + x14)^2 + (
    -0.5280008662898733 + x15)^2) + x445 * ((-0.6095783722497654 + x13)^2 + (
    -0.749606887290718 + x14)^2 + (-0.2992084144849715 + x15)^2) + x446 * ((
    -0.3561536887712061 + x13)^2 + (-0.9094619964414011 + x14)^2 + (
    -0.9928171594872911 + x15)^2) + x447 * ((-0.19358485305198325 + x13)^2 + (
    -0.4001073394562492 + x14)^2 + (-0.23357534573815197 + x15)^2) + x448 * ((
    -0.20828547060477265 + x13)^2 + (-0.39644066721668225 + x14)^2 + (
    -0.7362172137618145 + x15)^2) + x449 * ((-0.6396998486147768 + x13)^2 + (
    -0.29482831919895647 + x14)^2 + (-0.14044899013637724 + x15)^2) + x450 * ((
    -0.765643882826654 + x13)^2 + (-0.5765369431382706 + x14)^2 + (
    -0.8522368868434231 + x15)^2) + x451 * ((-0.7690569563429381 + x13)^2 + (
    -0.7237003240191451 + x14)^2 + (-0.5067753597656566 + x15)^2) + x452 * ((
    -0.09159033164075236 + x13)^2 + (-0.6420961033284197 + x14)^2 + (
    -0.6589453156905065 + x15)^2) + x453 * ((-0.3833030263493107 + x13)^2 + (
    -0.3056213143837909 + x14)^2 + (-0.583572623296832 + x15)^2) + x454 * ((
    -0.8769909727391579 + x13)^2 + (-0.34887774782474446 + x14)^2 + (
    -0.23298275093711673 + x15)^2) + x455 * ((-0.9751015775615309 + x13)^2 + (
    -0.5948149927026103 + x14)^2 + (-0.5272848953564142 + x15)^2) + x456 * ((
    -0.8624756249262849 + x13)^2 + (-0.07157238066686311 + x14)^2 + (
    -0.18797844538700537 + x15)^2) + x457 * ((-0.5802216444923713 + x13)^2 + (
    -0.28154327923543976 + x14)^2 + (-0.7283287977057182 + x15)^2) + x458 * ((
    -0.5409120197839667 + x13)^2 + (-0.8821640261603486 + x14)^2 + (
    -0.5803615496795161 + x15)^2) + x459 * ((-0.6617311102373136 + x13)^2 + (
    -0.5654602727098792 + x14)^2 + (-0.3650460577920387 + x15)^2) + x460 * ((
    -0.2716965439825759 + x13)^2 + (-0.9508799282699234 + x14)^2 + (
    -0.9496043117263887 + x15)^2) + x461 * ((-0.2785367614524876 + x13)^2 + (
    -0.00888924443037975 + x14)^2 + (-0.07177626736776488 + x15)^2) + x462 * ((
    -0.9528365858687048 + x13)^2 + (-0.46905249514856384 + x14)^2 + (
    -0.6707205137575432 + x15)^2) + x463 * ((-0.7023602522347626 + x13)^2 + (
    -0.3427485320313549 + x14)^2 + (-0.22119785846142337 + x15)^2) + x464 * ((
    -0.6833230046951964 + x13)^2 + (-0.8900435359063438 + x14)^2 + (
    -0.7350211970604509 + x15)^2) + x465 * ((-0.8050749568015152 + x13)^2 + (
    -0.7744524580155722 + x14)^2 + (-0.048989640268086165 + x15)^2) + x466 * ((
    -0.5857577991141887 + x13)^2 + (-0.7471281757286079 + x14)^2 + (
    -0.7881481567288812 + x15)^2) + x467 * ((-0.05486641693701977 + x13)^2 + (
    -0.538803679037738 + x14)^2 + (-0.524902392193278 + x15)^2) + x468 * ((
    -0.5134214119260625 + x13)^2 + (-0.3442102797771712 + x14)^2 + (
    -0.47072026564786984 + x15)^2) + x469 * ((-0.05779414997019372 + x13)^2 + (
    -0.8020397940471327 + x14)^2 + (-0.9916207714238137 + x15)^2) + x470 * ((
    -0.4189467613554877 + x13)^2 + (-0.7772516522669752 + x14)^2 + (
    -0.9704673132297963 + x15)^2) + x471 * ((-0.6128277861035099 + x13)^2 + (
    -0.8396924728861128 + x14)^2 + (-0.9520573132120294 + x15)^2) + x472 * ((
    -0.8621488398744713 + x13)^2 + (-0.548789075237998 + x14)^2 + (
    -0.7426250614075574 + x15)^2) + x473 * ((-0.7117960119205797 + x13)^2 + (
    -0.39215512790380547 + x14)^2 + (-0.5105264232502463 + x15)^2) + x474 * ((
    -0.22791158112403864 + x13)^2 + (-0.20506688508822635 + x14)^2 + (
    -0.8766388628762738 + x15)^2) + x475 * ((-0.9599249268359679 + x13)^2 + (
    -0.44412520059958527 + x14)^2 + (-0.38557384126798033 + x15)^2) + x476 * ((
    -0.30099374789049604 + x13)^2 + (-0.7579715531726323 + x14)^2 + (
    -0.5127071980951092 + x15)^2) + x477 * ((-0.4484888554980201 + x13)^2 + (
    -0.779019983792056 + x14)^2 + (-0.025865261097519632 + x15)^2) + x478 * ((
    -0.46286867912812435 + x13)^2 + (-0.814167947119447 + x14)^2 + (
    -0.5631048411921744 + x15)^2) + x479 * ((-0.8635903858321241 + x13)^2 + (
    -0.3235246710193893 + x14)^2 + (-0.7181557552325112 + x15)^2) + x480 * ((
    -0.9280940957804614 + x13)^2 + (-0.3453479970944433 + x14)^2 + (
    -0.5613693536456217 + x15)^2) + x481 * ((-0.006316762129101594 + x13)^2 + (
    -0.6031783182970557 + x14)^2 + (-0.28642101465869185 + x15)^2) + x482 * ((
    -0.17739543038776617 + x13)^2 + (-0.5813029219491296 + x14)^2 + (
    -0.5641970476507019 + x15)^2) + x483 * ((-0.8399487209952288 + x13)^2 + (
    -0.09110424417895568 + x14)^2 + (-0.5447723086642006 + x15)^2) + x484 * ((
    -0.6452341591995936 + x13)^2 + (-0.28018562998161844 + x14)^2 + (
    -0.7603427072697793 + x15)^2) + x485 * ((-0.5156422347329462 + x13)^2 + (
    -0.4676899425348692 + x14)^2 + (-0.1136822111961231 + x15)^2) + x486 * ((
    -0.7163586985799302 + x13)^2 + (-0.3372610204232811 + x14)^2 + (
    -0.8370463626853907 + x15)^2) + x487 * ((-0.9756166041963694 + x13)^2 + (
    -0.9612868946752545 + x14)^2 + (-0.7693557667569642 + x15)^2) + x488 * ((
    -0.6113942302805346 + x13)^2 + (-0.13178576707624667 + x14)^2 + (
    -0.9344462725690739 + x15)^2) + x489 * ((-0.5572653802049189 + x13)^2 + (
    -0.5319487140712044 + x14)^2 + (-0.14765227978554551 + x15)^2) + x490 * ((
    -0.11654881530618821 + x13)^2 + (-0.8056950968280207 + x14)^2 + (
    -0.5748478662379017 + x15)^2) + x491 * ((-0.26238920654281517 + x13)^2 + (
    -0.5023734426594167 + x14)^2 + (-0.42130574709860624 + x15)^2) + x492 * ((
    -0.9921980059568194 + x13)^2 + (-0.24115116836317307 + x14)^2 + (
    -0.6976120599289645 + x15)^2) + x493 * ((-0.21728717784157947 + x13)^2 + (
    -0.6420201178343862 + x14)^2 + (-0.8044170696315894 + x15)^2) + x494 * ((
    -0.09611093912226154 + x13)^2 + (-0.9775867468698249 + x14)^2 + (
    -0.4210031582727407 + x15)^2) + x495 * ((-0.049923277911933295 + x13)^2 + (
    -0.25221711356829135 + x14)^2 + (-0.8441636605533569 + x15)^2) + x496 * ((
    -0.3471505964014068 + x13)^2 + (-0.6202794672510638 + x14)^2 + (
    -0.4131303738662405 + x15)^2) + x497 * ((-0.6197762940940301 + x13)^2 + (
    -0.1382483611577 + x14)^2 + (-0.15914304098193788 + x15)^2) + x498 * ((
    -0.6655892821016779 + x13)^2 + (-0.41046211318873815 + x14)^2 + (
    -0.1312748248619422 + x15)^2) + x499 * ((-0.9416510851731662 + x13)^2 + (
    -0.8272647528783726 + x14)^2 + (-0.2714383624447996 + x15)^2) + x500 * ((
    -0.42481890588155824 + x13)^2 + (-0.6159336614459853 + x14)^2 + (
    -0.23967538175236203 + x15)^2) + x501 * ((-0.0358045583876343 + x13)^2 + (
    -0.010894449482712232 + x14)^2 + (-0.6586854665563344 + x15)^2) + x502 * ((
    -0.3025008049226424 + x13)^2 + (-0.24040585456892405 + x14)^2 + (
    -0.7463403103342172 + x15)^2) + x503 * ((-0.6954430403957257 + x13)^2 + (
    -0.12206067459294412 + x14)^2 + (-0.024319631497581096 + x15)^2) + x504 * (
    (-0.25839843172072186 + x13)^2 + (-0.9375128189340426 + x14)^2 + (
    -0.4009543474510294 + x15)^2) + x505 * ((-0.45145378805413694 + x13)^2 + (
    -0.09788835418641062 + x14)^2 + (-0.04872105528074022 + x15)^2) + x506 * ((
    -0.11644110458205315 + x13)^2 + (-0.7605627627985284 + x14)^2 + (
    -0.1923577950664841 + x15)^2) + x507 * ((-0.48447066501151403 + x13)^2 + (
    -0.7509689748452502 + x14)^2 + (-0.9619942070930291 + x15)^2) + x508 * ((
    -0.03508459180153145 + x13)^2 + (-0.5728060027674883 + x14)^2 + (
    -0.7436208452281391 + x15)^2) + x509 * ((-0.032847711659638845 + x13)^2 + (
    -0.5831028234172577 + x14)^2 + (-0.8741038911594665 + x15)^2) + x510 * ((
    -0.46061295403096403 + x13)^2 + (-0.377008556605009 + x14)^2 + (
    -0.2679552753900981 + x15)^2) + x511 * ((-0.2888285878888258 + x13)^2 + (
    -0.034149496184561645 + x14)^2 + (-0.38163177855929187 + x15)^2) + x512 * (
    (-0.5296679821912563 + x13)^2 + (-0.026930445670703906 + x14)^2 + (
    -0.6515536507627563 + x15)^2) + x513 * ((-0.9505325433299335 + x13)^2 + (
    -0.8406353966762972 + x14)^2 + (-0.9979229595662881 + x15)^2) + x514 * ((
    -0.7006669698429467 + x13)^2 + (-0.15718723636793908 + x14)^2 + (
    -0.4324401609471473 + x15)^2) + x515 * ((-0.696521925668867 + x13)^2 + (
    -0.41652540414708084 + x14)^2 + (-0.8580977844829885 + x15)^2) + x516 * ((
    -0.12958880379487892 + x13)^2 + (-0.703981942287015 + x14)^2 + (
    -0.524146756250147 + x15)^2) + x517 * ((-0.9133718781890398 + x13)^2 + (
    -0.7403730745987471 + x14)^2 + (-0.2907239377440496 + x15)^2) + x518 * ((
    -0.19307972709388999 + x13)^2 + (-0.9700461568357024 + x14)^2 + (
    -0.735905755762969 + x15)^2) + x519 * ((-0.11538660650992527 + x13)^2 + (
    -0.2727670397875678 + x14)^2 + (-0.8870259171359532 + x15)^2) + x520 * ((
    -0.7257851436532815 + x13)^2 + (-0.07855129523777848 + x14)^2 + (
    -0.4006634238638799 + x15)^2) + x521 * ((-0.6731181683996974 + x13)^2 + (
    -0.2299158906679658 + x14)^2 + (-0.14224633267260467 + x15)^2) + x522 * ((
    -0.637732077469805 + x16)^2 + (-0.30061635945038845 + x17)^2 + (
    -0.6924078188563045 + x18)^2) + x523 * ((-0.5204622036281865 + x16)^2 + (
    -0.4262380695375112 + x17)^2 + (-0.019757804882570618 + x18)^2) + x524 * ((
    -0.3877676795047561 + x16)^2 + (-0.6261603378186641 + x17)^2 + (
    -0.20807844834808797 + x18)^2) + x525 * ((-0.3455519385475 + x16)^2 + (
    -0.20721956099132388 + x17)^2 + (-0.7536751735394452 + x18)^2) + x526 * ((
    -0.7452291570426526 + x16)^2 + (-0.8288345290542969 + x17)^2 + (
    -0.9101818193634833 + x18)^2) + x527 * ((-0.7088715037487956 + x16)^2 + (
    -0.8675258967244885 + x17)^2 + (-0.04421039019838524 + x18)^2) + x528 * ((
    -0.33645524584418685 + x16)^2 + (-0.24931821641731888 + x17)^2 + (
    -0.24789447471906245 + x18)^2) + x529 * ((-0.39606323961214507 + x16)^2 + (
    -0.5092297648083476 + x17)^2 + (-0.8429822635539893 + x18)^2) + x530 * ((
    -0.3162888023664645 + x16)^2 + (-0.3537176609576351 + x17)^2 + (
    -0.8840601824506505 + x18)^2) + x531 * ((-0.042024431013358066 + x16)^2 + (
    -0.015648799035293925 + x17)^2 + (-0.028897199565620646 + x18)^2) + x532 *
    ((-0.7829982657179482 + x16)^2 + (-0.7604457448591289 + x17)^2 + (
    -0.597334909736347 + x18)^2) + x533 * ((-0.21464482455558387 + x16)^2 + (
    -0.7368895039728377 + x17)^2 + (-0.14158977662661187 + x18)^2) + x534 * ((
    -0.790895349248712 + x16)^2 + (-0.999859654218962 + x17)^2 + (
    -0.7994024450128572 + x18)^2) + x535 * ((-0.15089689559879838 + x16)^2 + (
    -0.2905434515528619 + x17)^2 + (-0.2886420160429456 + x18)^2) + x536 * ((
    -0.9157228230765573 + x16)^2 + (-0.7406305983646623 + x17)^2 + (
    -0.4142557316611599 + x18)^2) + x537 * ((-0.28767980872766563 + x16)^2 + (
    -0.0742772003595773 + x17)^2 + (-0.7235701139213052 + x18)^2) + x538 * ((
    -0.25465347672976957 + x16)^2 + (-0.6409023820345298 + x17)^2 + (
    -0.5494341492685579 + x18)^2) + x539 * ((-0.5541270607350097 + x16)^2 + (
    -0.9692776471334402 + x17)^2 + (-0.05355629576813248 + x18)^2) + x540 * ((
    -0.16592885733639762 + x16)^2 + (-0.6090998523529765 + x17)^2 + (
    -0.007633151339320965 + x18)^2) + x541 * ((-0.9035601490301819 + x16)^2 + (
    -0.09986398472275337 + x17)^2 + (-0.9904466067565432 + x18)^2) + x542 * ((
    -0.7453737555747959 + x16)^2 + (-0.8241163846060925 + x17)^2 + (
    -0.16259034239222492 + x18)^2) + x543 * ((-0.09286618285654225 + x16)^2 + (
    -0.9969692112075067 + x17)^2 + (-0.3842501245054024 + x18)^2) + x544 * ((
    -0.9386250621110139 + x16)^2 + (-0.05899573937535463 + x17)^2 + (
    -0.5280008662898733 + x18)^2) + x545 * ((-0.6095783722497654 + x16)^2 + (
    -0.749606887290718 + x17)^2 + (-0.2992084144849715 + x18)^2) + x546 * ((
    -0.3561536887712061 + x16)^2 + (-0.9094619964414011 + x17)^2 + (
    -0.9928171594872911 + x18)^2) + x547 * ((-0.19358485305198325 + x16)^2 + (
    -0.4001073394562492 + x17)^2 + (-0.23357534573815197 + x18)^2) + x548 * ((
    -0.20828547060477265 + x16)^2 + (-0.39644066721668225 + x17)^2 + (
    -0.7362172137618145 + x18)^2) + x549 * ((-0.6396998486147768 + x16)^2 + (
    -0.29482831919895647 + x17)^2 + (-0.14044899013637724 + x18)^2) + x550 * ((
    -0.765643882826654 + x16)^2 + (-0.5765369431382706 + x17)^2 + (
    -0.8522368868434231 + x18)^2) + x551 * ((-0.7690569563429381 + x16)^2 + (
    -0.7237003240191451 + x17)^2 + (-0.5067753597656566 + x18)^2) + x552 * ((
    -0.09159033164075236 + x16)^2 + (-0.6420961033284197 + x17)^2 + (
    -0.6589453156905065 + x18)^2) + x553 * ((-0.3833030263493107 + x16)^2 + (
    -0.3056213143837909 + x17)^2 + (-0.583572623296832 + x18)^2) + x554 * ((
    -0.8769909727391579 + x16)^2 + (-0.34887774782474446 + x17)^2 + (
    -0.23298275093711673 + x18)^2) + x555 * ((-0.9751015775615309 + x16)^2 + (
    -0.5948149927026103 + x17)^2 + (-0.5272848953564142 + x18)^2) + x556 * ((
    -0.8624756249262849 + x16)^2 + (-0.07157238066686311 + x17)^2 + (
    -0.18797844538700537 + x18)^2) + x557 * ((-0.5802216444923713 + x16)^2 + (
    -0.28154327923543976 + x17)^2 + (-0.7283287977057182 + x18)^2) + x558 * ((
    -0.5409120197839667 + x16)^2 + (-0.8821640261603486 + x17)^2 + (
    -0.5803615496795161 + x18)^2) + x559 * ((-0.6617311102373136 + x16)^2 + (
    -0.5654602727098792 + x17)^2 + (-0.3650460577920387 + x18)^2) + x560 * ((
    -0.2716965439825759 + x16)^2 + (-0.9508799282699234 + x17)^2 + (
    -0.9496043117263887 + x18)^2) + x561 * ((-0.2785367614524876 + x16)^2 + (
    -0.00888924443037975 + x17)^2 + (-0.07177626736776488 + x18)^2) + x562 * ((
    -0.9528365858687048 + x16)^2 + (-0.46905249514856384 + x17)^2 + (
    -0.6707205137575432 + x18)^2) + x563 * ((-0.7023602522347626 + x16)^2 + (
    -0.3427485320313549 + x17)^2 + (-0.22119785846142337 + x18)^2) + x564 * ((
    -0.6833230046951964 + x16)^2 + (-0.8900435359063438 + x17)^2 + (
    -0.7350211970604509 + x18)^2) + x565 * ((-0.8050749568015152 + x16)^2 + (
    -0.7744524580155722 + x17)^2 + (-0.048989640268086165 + x18)^2) + x566 * ((
    -0.5857577991141887 + x16)^2 + (-0.7471281757286079 + x17)^2 + (
    -0.7881481567288812 + x18)^2) + x567 * ((-0.05486641693701977 + x16)^2 + (
    -0.538803679037738 + x17)^2 + (-0.524902392193278 + x18)^2) + x568 * ((
    -0.5134214119260625 + x16)^2 + (-0.3442102797771712 + x17)^2 + (
    -0.47072026564786984 + x18)^2) + x569 * ((-0.05779414997019372 + x16)^2 + (
    -0.8020397940471327 + x17)^2 + (-0.9916207714238137 + x18)^2) + x570 * ((
    -0.4189467613554877 + x16)^2 + (-0.7772516522669752 + x17)^2 + (
    -0.9704673132297963 + x18)^2) + x571 * ((-0.6128277861035099 + x16)^2 + (
    -0.8396924728861128 + x17)^2 + (-0.9520573132120294 + x18)^2) + x572 * ((
    -0.8621488398744713 + x16)^2 + (-0.548789075237998 + x17)^2 + (
    -0.7426250614075574 + x18)^2) + x573 * ((-0.7117960119205797 + x16)^2 + (
    -0.39215512790380547 + x17)^2 + (-0.5105264232502463 + x18)^2) + x574 * ((
    -0.22791158112403864 + x16)^2 + (-0.20506688508822635 + x17)^2 + (
    -0.8766388628762738 + x18)^2) + x575 * ((-0.9599249268359679 + x16)^2 + (
    -0.44412520059958527 + x17)^2 + (-0.38557384126798033 + x18)^2) + x576 * ((
    -0.30099374789049604 + x16)^2 + (-0.7579715531726323 + x17)^2 + (
    -0.5127071980951092 + x18)^2) + x577 * ((-0.4484888554980201 + x16)^2 + (
    -0.779019983792056 + x17)^2 + (-0.025865261097519632 + x18)^2) + x578 * ((
    -0.46286867912812435 + x16)^2 + (-0.814167947119447 + x17)^2 + (
    -0.5631048411921744 + x18)^2) + x579 * ((-0.8635903858321241 + x16)^2 + (
    -0.3235246710193893 + x17)^2 + (-0.7181557552325112 + x18)^2) + x580 * ((
    -0.9280940957804614 + x16)^2 + (-0.3453479970944433 + x17)^2 + (
    -0.5613693536456217 + x18)^2) + x581 * ((-0.006316762129101594 + x16)^2 + (
    -0.6031783182970557 + x17)^2 + (-0.28642101465869185 + x18)^2) + x582 * ((
    -0.17739543038776617 + x16)^2 + (-0.5813029219491296 + x17)^2 + (
    -0.5641970476507019 + x18)^2) + x583 * ((-0.8399487209952288 + x16)^2 + (
    -0.09110424417895568 + x17)^2 + (-0.5447723086642006 + x18)^2) + x584 * ((
    -0.6452341591995936 + x16)^2 + (-0.28018562998161844 + x17)^2 + (
    -0.7603427072697793 + x18)^2) + x585 * ((-0.5156422347329462 + x16)^2 + (
    -0.4676899425348692 + x17)^2 + (-0.1136822111961231 + x18)^2) + x586 * ((
    -0.7163586985799302 + x16)^2 + (-0.3372610204232811 + x17)^2 + (
    -0.8370463626853907 + x18)^2) + x587 * ((-0.9756166041963694 + x16)^2 + (
    -0.9612868946752545 + x17)^2 + (-0.7693557667569642 + x18)^2) + x588 * ((
    -0.6113942302805346 + x16)^2 + (-0.13178576707624667 + x17)^2 + (
    -0.9344462725690739 + x18)^2) + x589 * ((-0.5572653802049189 + x16)^2 + (
    -0.5319487140712044 + x17)^2 + (-0.14765227978554551 + x18)^2) + x590 * ((
    -0.11654881530618821 + x16)^2 + (-0.8056950968280207 + x17)^2 + (
    -0.5748478662379017 + x18)^2) + x591 * ((-0.26238920654281517 + x16)^2 + (
    -0.5023734426594167 + x17)^2 + (-0.42130574709860624 + x18)^2) + x592 * ((
    -0.9921980059568194 + x16)^2 + (-0.24115116836317307 + x17)^2 + (
    -0.6976120599289645 + x18)^2) + x593 * ((-0.21728717784157947 + x16)^2 + (
    -0.6420201178343862 + x17)^2 + (-0.8044170696315894 + x18)^2) + x594 * ((
    -0.09611093912226154 + x16)^2 + (-0.9775867468698249 + x17)^2 + (
    -0.4210031582727407 + x18)^2) + x595 * ((-0.049923277911933295 + x16)^2 + (
    -0.25221711356829135 + x17)^2 + (-0.8441636605533569 + x18)^2) + x596 * ((
    -0.3471505964014068 + x16)^2 + (-0.6202794672510638 + x17)^2 + (
    -0.4131303738662405 + x18)^2) + x597 * ((-0.6197762940940301 + x16)^2 + (
    -0.1382483611577 + x17)^2 + (-0.15914304098193788 + x18)^2) + x598 * ((
    -0.6655892821016779 + x16)^2 + (-0.41046211318873815 + x17)^2 + (
    -0.1312748248619422 + x18)^2) + x599 * ((-0.9416510851731662 + x16)^2 + (
    -0.8272647528783726 + x17)^2 + (-0.2714383624447996 + x18)^2) + x600 * ((
    -0.42481890588155824 + x16)^2 + (-0.6159336614459853 + x17)^2 + (
    -0.23967538175236203 + x18)^2) + x601 * ((-0.0358045583876343 + x16)^2 + (
    -0.010894449482712232 + x17)^2 + (-0.6586854665563344 + x18)^2) + x602 * ((
    -0.3025008049226424 + x16)^2 + (-0.24040585456892405 + x17)^2 + (
    -0.7463403103342172 + x18)^2) + x603 * ((-0.6954430403957257 + x16)^2 + (
    -0.12206067459294412 + x17)^2 + (-0.024319631497581096 + x18)^2) + x604 * (
    (-0.25839843172072186 + x16)^2 + (-0.9375128189340426 + x17)^2 + (
    -0.4009543474510294 + x18)^2) + x605 * ((-0.45145378805413694 + x16)^2 + (
    -0.09788835418641062 + x17)^2 + (-0.04872105528074022 + x18)^2) + x606 * ((
    -0.11644110458205315 + x16)^2 + (-0.7605627627985284 + x17)^2 + (
    -0.1923577950664841 + x18)^2) + x607 * ((-0.48447066501151403 + x16)^2 + (
    -0.7509689748452502 + x17)^2 + (-0.9619942070930291 + x18)^2) + x608 * ((
    -0.03508459180153145 + x16)^2 + (-0.5728060027674883 + x17)^2 + (
    -0.7436208452281391 + x18)^2) + x609 * ((-0.032847711659638845 + x16)^2 + (
    -0.5831028234172577 + x17)^2 + (-0.8741038911594665 + x18)^2) + x610 * ((
    -0.46061295403096403 + x16)^2 + (-0.377008556605009 + x17)^2 + (
    -0.2679552753900981 + x18)^2) + x611 * ((-0.2888285878888258 + x16)^2 + (
    -0.034149496184561645 + x17)^2 + (-0.38163177855929187 + x18)^2) + x612 * (
    (-0.5296679821912563 + x16)^2 + (-0.026930445670703906 + x17)^2 + (
    -0.6515536507627563 + x18)^2) + x613 * ((-0.9505325433299335 + x16)^2 + (
    -0.8406353966762972 + x17)^2 + (-0.9979229595662881 + x18)^2) + x614 * ((
    -0.7006669698429467 + x16)^2 + (-0.15718723636793908 + x17)^2 + (
    -0.4324401609471473 + x18)^2) + x615 * ((-0.696521925668867 + x16)^2 + (
    -0.41652540414708084 + x17)^2 + (-0.8580977844829885 + x18)^2) + x616 * ((
    -0.12958880379487892 + x16)^2 + (-0.703981942287015 + x17)^2 + (
    -0.524146756250147 + x18)^2) + x617 * ((-0.9133718781890398 + x16)^2 + (
    -0.7403730745987471 + x17)^2 + (-0.2907239377440496 + x18)^2) + x618 * ((
    -0.19307972709388999 + x16)^2 + (-0.9700461568357024 + x17)^2 + (
    -0.735905755762969 + x18)^2) + x619 * ((-0.11538660650992527 + x16)^2 + (
    -0.2727670397875678 + x17)^2 + (-0.8870259171359532 + x18)^2) + x620 * ((
    -0.7257851436532815 + x16)^2 + (-0.07855129523777848 + x17)^2 + (
    -0.4006634238638799 + x18)^2) + x621 * ((-0.6731181683996974 + x16)^2 + (
    -0.2299158906679658 + x17)^2 + (-0.14224633267260467 + x18)^2) + x622 * ((
    -0.637732077469805 + x19)^2 + (-0.30061635945038845 + x20)^2 + (
    -0.6924078188563045 + x21)^2) + x623 * ((-0.5204622036281865 + x19)^2 + (
    -0.4262380695375112 + x20)^2 + (-0.019757804882570618 + x21)^2) + x624 * ((
    -0.3877676795047561 + x19)^2 + (-0.6261603378186641 + x20)^2 + (
    -0.20807844834808797 + x21)^2) + x625 * ((-0.3455519385475 + x19)^2 + (
    -0.20721956099132388 + x20)^2 + (-0.7536751735394452 + x21)^2) + x626 * ((
    -0.7452291570426526 + x19)^2 + (-0.8288345290542969 + x20)^2 + (
    -0.9101818193634833 + x21)^2) + x627 * ((-0.7088715037487956 + x19)^2 + (
    -0.8675258967244885 + x20)^2 + (-0.04421039019838524 + x21)^2) + x628 * ((
    -0.33645524584418685 + x19)^2 + (-0.24931821641731888 + x20)^2 + (
    -0.24789447471906245 + x21)^2) + x629 * ((-0.39606323961214507 + x19)^2 + (
    -0.5092297648083476 + x20)^2 + (-0.8429822635539893 + x21)^2) + x630 * ((
    -0.3162888023664645 + x19)^2 + (-0.3537176609576351 + x20)^2 + (
    -0.8840601824506505 + x21)^2) + x631 * ((-0.042024431013358066 + x19)^2 + (
    -0.015648799035293925 + x20)^2 + (-0.028897199565620646 + x21)^2) + x632 *
    ((-0.7829982657179482 + x19)^2 + (-0.7604457448591289 + x20)^2 + (
    -0.597334909736347 + x21)^2) + x633 * ((-0.21464482455558387 + x19)^2 + (
    -0.7368895039728377 + x20)^2 + (-0.14158977662661187 + x21)^2) + x634 * ((
    -0.790895349248712 + x19)^2 + (-0.999859654218962 + x20)^2 + (
    -0.7994024450128572 + x21)^2) + x635 * ((-0.15089689559879838 + x19)^2 + (
    -0.2905434515528619 + x20)^2 + (-0.2886420160429456 + x21)^2) + x636 * ((
    -0.9157228230765573 + x19)^2 + (-0.7406305983646623 + x20)^2 + (
    -0.4142557316611599 + x21)^2) + x637 * ((-0.28767980872766563 + x19)^2 + (
    -0.0742772003595773 + x20)^2 + (-0.7235701139213052 + x21)^2) + x638 * ((
    -0.25465347672976957 + x19)^2 + (-0.6409023820345298 + x20)^2 + (
    -0.5494341492685579 + x21)^2) + x639 * ((-0.5541270607350097 + x19)^2 + (
    -0.9692776471334402 + x20)^2 + (-0.05355629576813248 + x21)^2) + x640 * ((
    -0.16592885733639762 + x19)^2 + (-0.6090998523529765 + x20)^2 + (
    -0.007633151339320965 + x21)^2) + x641 * ((-0.9035601490301819 + x19)^2 + (
    -0.09986398472275337 + x20)^2 + (-0.9904466067565432 + x21)^2) + x642 * ((
    -0.7453737555747959 + x19)^2 + (-0.8241163846060925 + x20)^2 + (
    -0.16259034239222492 + x21)^2) + x643 * ((-0.09286618285654225 + x19)^2 + (
    -0.9969692112075067 + x20)^2 + (-0.3842501245054024 + x21)^2) + x644 * ((
    -0.9386250621110139 + x19)^2 + (-0.05899573937535463 + x20)^2 + (
    -0.5280008662898733 + x21)^2) + x645 * ((-0.6095783722497654 + x19)^2 + (
    -0.749606887290718 + x20)^2 + (-0.2992084144849715 + x21)^2) + x646 * ((
    -0.3561536887712061 + x19)^2 + (-0.9094619964414011 + x20)^2 + (
    -0.9928171594872911 + x21)^2) + x647 * ((-0.19358485305198325 + x19)^2 + (
    -0.4001073394562492 + x20)^2 + (-0.23357534573815197 + x21)^2) + x648 * ((
    -0.20828547060477265 + x19)^2 + (-0.39644066721668225 + x20)^2 + (
    -0.7362172137618145 + x21)^2) + x649 * ((-0.6396998486147768 + x19)^2 + (
    -0.29482831919895647 + x20)^2 + (-0.14044899013637724 + x21)^2) + x650 * ((
    -0.765643882826654 + x19)^2 + (-0.5765369431382706 + x20)^2 + (
    -0.8522368868434231 + x21)^2) + x651 * ((-0.7690569563429381 + x19)^2 + (
    -0.7237003240191451 + x20)^2 + (-0.5067753597656566 + x21)^2) + x652 * ((
    -0.09159033164075236 + x19)^2 + (-0.6420961033284197 + x20)^2 + (
    -0.6589453156905065 + x21)^2) + x653 * ((-0.3833030263493107 + x19)^2 + (
    -0.3056213143837909 + x20)^2 + (-0.583572623296832 + x21)^2) + x654 * ((
    -0.8769909727391579 + x19)^2 + (-0.34887774782474446 + x20)^2 + (
    -0.23298275093711673 + x21)^2) + x655 * ((-0.9751015775615309 + x19)^2 + (
    -0.5948149927026103 + x20)^2 + (-0.5272848953564142 + x21)^2) + x656 * ((
    -0.8624756249262849 + x19)^2 + (-0.07157238066686311 + x20)^2 + (
    -0.18797844538700537 + x21)^2) + x657 * ((-0.5802216444923713 + x19)^2 + (
    -0.28154327923543976 + x20)^2 + (-0.7283287977057182 + x21)^2) + x658 * ((
    -0.5409120197839667 + x19)^2 + (-0.8821640261603486 + x20)^2 + (
    -0.5803615496795161 + x21)^2) + x659 * ((-0.6617311102373136 + x19)^2 + (
    -0.5654602727098792 + x20)^2 + (-0.3650460577920387 + x21)^2) + x660 * ((
    -0.2716965439825759 + x19)^2 + (-0.9508799282699234 + x20)^2 + (
    -0.9496043117263887 + x21)^2) + x661 * ((-0.2785367614524876 + x19)^2 + (
    -0.00888924443037975 + x20)^2 + (-0.07177626736776488 + x21)^2) + x662 * ((
    -0.9528365858687048 + x19)^2 + (-0.46905249514856384 + x20)^2 + (
    -0.6707205137575432 + x21)^2) + x663 * ((-0.7023602522347626 + x19)^2 + (
    -0.3427485320313549 + x20)^2 + (-0.22119785846142337 + x21)^2) + x664 * ((
    -0.6833230046951964 + x19)^2 + (-0.8900435359063438 + x20)^2 + (
    -0.7350211970604509 + x21)^2) + x665 * ((-0.8050749568015152 + x19)^2 + (
    -0.7744524580155722 + x20)^2 + (-0.048989640268086165 + x21)^2) + x666 * ((
    -0.5857577991141887 + x19)^2 + (-0.7471281757286079 + x20)^2 + (
    -0.7881481567288812 + x21)^2) + x667 * ((-0.05486641693701977 + x19)^2 + (
    -0.538803679037738 + x20)^2 + (-0.524902392193278 + x21)^2) + x668 * ((
    -0.5134214119260625 + x19)^2 + (-0.3442102797771712 + x20)^2 + (
    -0.47072026564786984 + x21)^2) + x669 * ((-0.05779414997019372 + x19)^2 + (
    -0.8020397940471327 + x20)^2 + (-0.9916207714238137 + x21)^2) + x670 * ((
    -0.4189467613554877 + x19)^2 + (-0.7772516522669752 + x20)^2 + (
    -0.9704673132297963 + x21)^2) + x671 * ((-0.6128277861035099 + x19)^2 + (
    -0.8396924728861128 + x20)^2 + (-0.9520573132120294 + x21)^2) + x672 * ((
    -0.8621488398744713 + x19)^2 + (-0.548789075237998 + x20)^2 + (
    -0.7426250614075574 + x21)^2) + x673 * ((-0.7117960119205797 + x19)^2 + (
    -0.39215512790380547 + x20)^2 + (-0.5105264232502463 + x21)^2) + x674 * ((
    -0.22791158112403864 + x19)^2 + (-0.20506688508822635 + x20)^2 + (
    -0.8766388628762738 + x21)^2) + x675 * ((-0.9599249268359679 + x19)^2 + (
    -0.44412520059958527 + x20)^2 + (-0.38557384126798033 + x21)^2) + x676 * ((
    -0.30099374789049604 + x19)^2 + (-0.7579715531726323 + x20)^2 + (
    -0.5127071980951092 + x21)^2) + x677 * ((-0.4484888554980201 + x19)^2 + (
    -0.779019983792056 + x20)^2 + (-0.025865261097519632 + x21)^2) + x678 * ((
    -0.46286867912812435 + x19)^2 + (-0.814167947119447 + x20)^2 + (
    -0.5631048411921744 + x21)^2) + x679 * ((-0.8635903858321241 + x19)^2 + (
    -0.3235246710193893 + x20)^2 + (-0.7181557552325112 + x21)^2) + x680 * ((
    -0.9280940957804614 + x19)^2 + (-0.3453479970944433 + x20)^2 + (
    -0.5613693536456217 + x21)^2) + x681 * ((-0.006316762129101594 + x19)^2 + (
    -0.6031783182970557 + x20)^2 + (-0.28642101465869185 + x21)^2) + x682 * ((
    -0.17739543038776617 + x19)^2 + (-0.5813029219491296 + x20)^2 + (
    -0.5641970476507019 + x21)^2) + x683 * ((-0.8399487209952288 + x19)^2 + (
    -0.09110424417895568 + x20)^2 + (-0.5447723086642006 + x21)^2) + x684 * ((
    -0.6452341591995936 + x19)^2 + (-0.28018562998161844 + x20)^2 + (
    -0.7603427072697793 + x21)^2) + x685 * ((-0.5156422347329462 + x19)^2 + (
    -0.4676899425348692 + x20)^2 + (-0.1136822111961231 + x21)^2) + x686 * ((
    -0.7163586985799302 + x19)^2 + (-0.3372610204232811 + x20)^2 + (
    -0.8370463626853907 + x21)^2) + x687 * ((-0.9756166041963694 + x19)^2 + (
    -0.9612868946752545 + x20)^2 + (-0.7693557667569642 + x21)^2) + x688 * ((
    -0.6113942302805346 + x19)^2 + (-0.13178576707624667 + x20)^2 + (
    -0.9344462725690739 + x21)^2) + x689 * ((-0.5572653802049189 + x19)^2 + (
    -0.5319487140712044 + x20)^2 + (-0.14765227978554551 + x21)^2) + x690 * ((
    -0.11654881530618821 + x19)^2 + (-0.8056950968280207 + x20)^2 + (
    -0.5748478662379017 + x21)^2) + x691 * ((-0.26238920654281517 + x19)^2 + (
    -0.5023734426594167 + x20)^2 + (-0.42130574709860624 + x21)^2) + x692 * ((
    -0.9921980059568194 + x19)^2 + (-0.24115116836317307 + x20)^2 + (
    -0.6976120599289645 + x21)^2) + x693 * ((-0.21728717784157947 + x19)^2 + (
    -0.6420201178343862 + x20)^2 + (-0.8044170696315894 + x21)^2) + x694 * ((
    -0.09611093912226154 + x19)^2 + (-0.9775867468698249 + x20)^2 + (
    -0.4210031582727407 + x21)^2) + x695 * ((-0.049923277911933295 + x19)^2 + (
    -0.25221711356829135 + x20)^2 + (-0.8441636605533569 + x21)^2) + x696 * ((
    -0.3471505964014068 + x19)^2 + (-0.6202794672510638 + x20)^2 + (
    -0.4131303738662405 + x21)^2) + x697 * ((-0.6197762940940301 + x19)^2 + (
    -0.1382483611577 + x20)^2 + (-0.15914304098193788 + x21)^2) + x698 * ((
    -0.6655892821016779 + x19)^2 + (-0.41046211318873815 + x20)^2 + (
    -0.1312748248619422 + x21)^2) + x699 * ((-0.9416510851731662 + x19)^2 + (
    -0.8272647528783726 + x20)^2 + (-0.2714383624447996 + x21)^2) + x700 * ((
    -0.42481890588155824 + x19)^2 + (-0.6159336614459853 + x20)^2 + (
    -0.23967538175236203 + x21)^2) + x701 * ((-0.0358045583876343 + x19)^2 + (
    -0.010894449482712232 + x20)^2 + (-0.6586854665563344 + x21)^2) + x702 * ((
    -0.3025008049226424 + x19)^2 + (-0.24040585456892405 + x20)^2 + (
    -0.7463403103342172 + x21)^2) + x703 * ((-0.6954430403957257 + x19)^2 + (
    -0.12206067459294412 + x20)^2 + (-0.024319631497581096 + x21)^2) + x704 * (
    (-0.25839843172072186 + x19)^2 + (-0.9375128189340426 + x20)^2 + (
    -0.4009543474510294 + x21)^2) + x705 * ((-0.45145378805413694 + x19)^2 + (
    -0.09788835418641062 + x20)^2 + (-0.04872105528074022 + x21)^2) + x706 * ((
    -0.11644110458205315 + x19)^2 + (-0.7605627627985284 + x20)^2 + (
    -0.1923577950664841 + x21)^2) + x707 * ((-0.48447066501151403 + x19)^2 + (
    -0.7509689748452502 + x20)^2 + (-0.9619942070930291 + x21)^2) + x708 * ((
    -0.03508459180153145 + x19)^2 + (-0.5728060027674883 + x20)^2 + (
    -0.7436208452281391 + x21)^2) + x709 * ((-0.032847711659638845 + x19)^2 + (
    -0.5831028234172577 + x20)^2 + (-0.8741038911594665 + x21)^2) + x710 * ((
    -0.46061295403096403 + x19)^2 + (-0.377008556605009 + x20)^2 + (
    -0.2679552753900981 + x21)^2) + x711 * ((-0.2888285878888258 + x19)^2 + (
    -0.034149496184561645 + x20)^2 + (-0.38163177855929187 + x21)^2) + x712 * (
    (-0.5296679821912563 + x19)^2 + (-0.026930445670703906 + x20)^2 + (
    -0.6515536507627563 + x21)^2) + x713 * ((-0.9505325433299335 + x19)^2 + (
    -0.8406353966762972 + x20)^2 + (-0.9979229595662881 + x21)^2) + x714 * ((
    -0.7006669698429467 + x19)^2 + (-0.15718723636793908 + x20)^2 + (
    -0.4324401609471473 + x21)^2) + x715 * ((-0.696521925668867 + x19)^2 + (
    -0.41652540414708084 + x20)^2 + (-0.8580977844829885 + x21)^2) + x716 * ((
    -0.12958880379487892 + x19)^2 + (-0.703981942287015 + x20)^2 + (
    -0.524146756250147 + x21)^2) + x717 * ((-0.9133718781890398 + x19)^2 + (
    -0.7403730745987471 + x20)^2 + (-0.2907239377440496 + x21)^2) + x718 * ((
    -0.19307972709388999 + x19)^2 + (-0.9700461568357024 + x20)^2 + (
    -0.735905755762969 + x21)^2) + x719 * ((-0.11538660650992527 + x19)^2 + (
    -0.2727670397875678 + x20)^2 + (-0.8870259171359532 + x21)^2) + x720 * ((
    -0.7257851436532815 + x19)^2 + (-0.07855129523777848 + x20)^2 + (
    -0.4006634238638799 + x21)^2) + x721 * ((-0.6731181683996974 + x19)^2 + (
    -0.2299158906679658 + x20)^2 + (-0.14224633267260467 + x21)^2))

@constraint(m, e1, x22 + x122 + x222 + x322 + x422 + x522 + x622 == 1)
@constraint(m, e2, x23 + x123 + x223 + x323 + x423 + x523 + x623 == 1)
@constraint(m, e3, x24 + x124 + x224 + x324 + x424 + x524 + x624 == 1)
@constraint(m, e4, x25 + x125 + x225 + x325 + x425 + x525 + x625 == 1)
@constraint(m, e5, x26 + x126 + x226 + x326 + x426 + x526 + x626 == 1)
@constraint(m, e6, x27 + x127 + x227 + x327 + x427 + x527 + x627 == 1)
@constraint(m, e7, x28 + x128 + x228 + x328 + x428 + x528 + x628 == 1)
@constraint(m, e8, x29 + x129 + x229 + x329 + x429 + x529 + x629 == 1)
@constraint(m, e9, x30 + x130 + x230 + x330 + x430 + x530 + x630 == 1)
@constraint(m, e10, x31 + x131 + x231 + x331 + x431 + x531 + x631 == 1)
@constraint(m, e11, x32 + x132 + x232 + x332 + x432 + x532 + x632 == 1)
@constraint(m, e12, x33 + x133 + x233 + x333 + x433 + x533 + x633 == 1)
@constraint(m, e13, x34 + x134 + x234 + x334 + x434 + x534 + x634 == 1)
@constraint(m, e14, x35 + x135 + x235 + x335 + x435 + x535 + x635 == 1)
@constraint(m, e15, x36 + x136 + x236 + x336 + x436 + x536 + x636 == 1)
@constraint(m, e16, x37 + x137 + x237 + x337 + x437 + x537 + x637 == 1)
@constraint(m, e17, x38 + x138 + x238 + x338 + x438 + x538 + x638 == 1)
@constraint(m, e18, x39 + x139 + x239 + x339 + x439 + x539 + x639 == 1)
@constraint(m, e19, x40 + x140 + x240 + x340 + x440 + x540 + x640 == 1)
@constraint(m, e20, x41 + x141 + x241 + x341 + x441 + x541 + x641 == 1)
@constraint(m, e21, x42 + x142 + x242 + x342 + x442 + x542 + x642 == 1)
@constraint(m, e22, x43 + x143 + x243 + x343 + x443 + x543 + x643 == 1)
@constraint(m, e23, x44 + x144 + x244 + x344 + x444 + x544 + x644 == 1)
@constraint(m, e24, x45 + x145 + x245 + x345 + x445 + x545 + x645 == 1)
@constraint(m, e25, x46 + x146 + x246 + x346 + x446 + x546 + x646 == 1)
@constraint(m, e26, x47 + x147 + x247 + x347 + x447 + x547 + x647 == 1)
@constraint(m, e27, x48 + x148 + x248 + x348 + x448 + x548 + x648 == 1)
@constraint(m, e28, x49 + x149 + x249 + x349 + x449 + x549 + x649 == 1)
@constraint(m, e29, x50 + x150 + x250 + x350 + x450 + x550 + x650 == 1)
@constraint(m, e30, x51 + x151 + x251 + x351 + x451 + x551 + x651 == 1)
@constraint(m, e31, x52 + x152 + x252 + x352 + x452 + x552 + x652 == 1)
@constraint(m, e32, x53 + x153 + x253 + x353 + x453 + x553 + x653 == 1)
@constraint(m, e33, x54 + x154 + x254 + x354 + x454 + x554 + x654 == 1)
@constraint(m, e34, x55 + x155 + x255 + x355 + x455 + x555 + x655 == 1)
@constraint(m, e35, x56 + x156 + x256 + x356 + x456 + x556 + x656 == 1)
@constraint(m, e36, x57 + x157 + x257 + x357 + x457 + x557 + x657 == 1)
@constraint(m, e37, x58 + x158 + x258 + x358 + x458 + x558 + x658 == 1)
@constraint(m, e38, x59 + x159 + x259 + x359 + x459 + x559 + x659 == 1)
@constraint(m, e39, x60 + x160 + x260 + x360 + x460 + x560 + x660 == 1)
@constraint(m, e40, x61 + x161 + x261 + x361 + x461 + x561 + x661 == 1)
@constraint(m, e41, x62 + x162 + x262 + x362 + x462 + x562 + x662 == 1)
@constraint(m, e42, x63 + x163 + x263 + x363 + x463 + x563 + x663 == 1)
@constraint(m, e43, x64 + x164 + x264 + x364 + x464 + x564 + x664 == 1)
@constraint(m, e44, x65 + x165 + x265 + x365 + x465 + x565 + x665 == 1)
@constraint(m, e45, x66 + x166 + x266 + x366 + x466 + x566 + x666 == 1)
@constraint(m, e46, x67 + x167 + x267 + x367 + x467 + x567 + x667 == 1)
@constraint(m, e47, x68 + x168 + x268 + x368 + x468 + x568 + x668 == 1)
@constraint(m, e48, x69 + x169 + x269 + x369 + x469 + x569 + x669 == 1)
@constraint(m, e49, x70 + x170 + x270 + x370 + x470 + x570 + x670 == 1)
@constraint(m, e50, x71 + x171 + x271 + x371 + x471 + x571 + x671 == 1)
@constraint(m, e51, x72 + x172 + x272 + x372 + x472 + x572 + x672 == 1)
@constraint(m, e52, x73 + x173 + x273 + x373 + x473 + x573 + x673 == 1)
@constraint(m, e53, x74 + x174 + x274 + x374 + x474 + x574 + x674 == 1)
@constraint(m, e54, x75 + x175 + x275 + x375 + x475 + x575 + x675 == 1)
@constraint(m, e55, x76 + x176 + x276 + x376 + x476 + x576 + x676 == 1)
@constraint(m, e56, x77 + x177 + x277 + x377 + x477 + x577 + x677 == 1)
@constraint(m, e57, x78 + x178 + x278 + x378 + x478 + x578 + x678 == 1)
@constraint(m, e58, x79 + x179 + x279 + x379 + x479 + x579 + x679 == 1)
@constraint(m, e59, x80 + x180 + x280 + x380 + x480 + x580 + x680 == 1)
@constraint(m, e60, x81 + x181 + x281 + x381 + x481 + x581 + x681 == 1)
@constraint(m, e61, x82 + x182 + x282 + x382 + x482 + x582 + x682 == 1)
@constraint(m, e62, x83 + x183 + x283 + x383 + x483 + x583 + x683 == 1)
@constraint(m, e63, x84 + x184 + x284 + x384 + x484 + x584 + x684 == 1)
@constraint(m, e64, x85 + x185 + x285 + x385 + x485 + x585 + x685 == 1)
@constraint(m, e65, x86 + x186 + x286 + x386 + x486 + x586 + x686 == 1)
@constraint(m, e66, x87 + x187 + x287 + x387 + x487 + x587 + x687 == 1)
@constraint(m, e67, x88 + x188 + x288 + x388 + x488 + x588 + x688 == 1)
@constraint(m, e68, x89 + x189 + x289 + x389 + x489 + x589 + x689 == 1)
@constraint(m, e69, x90 + x190 + x290 + x390 + x490 + x590 + x690 == 1)
@constraint(m, e70, x91 + x191 + x291 + x391 + x491 + x591 + x691 == 1)
@constraint(m, e71, x92 + x192 + x292 + x392 + x492 + x592 + x692 == 1)
@constraint(m, e72, x93 + x193 + x293 + x393 + x493 + x593 + x693 == 1)
@constraint(m, e73, x94 + x194 + x294 + x394 + x494 + x594 + x694 == 1)
@constraint(m, e74, x95 + x195 + x295 + x395 + x495 + x595 + x695 == 1)
@constraint(m, e75, x96 + x196 + x296 + x396 + x496 + x596 + x696 == 1)
@constraint(m, e76, x97 + x197 + x297 + x397 + x497 + x597 + x697 == 1)
@constraint(m, e77, x98 + x198 + x298 + x398 + x498 + x598 + x698 == 1)
@constraint(m, e78, x99 + x199 + x299 + x399 + x499 + x599 + x699 == 1)
@constraint(m, e79, x100 + x200 + x300 + x400 + x500 + x600 + x700 == 1)
@constraint(m, e80, x101 + x201 + x301 + x401 + x501 + x601 + x701 == 1)
@constraint(m, e81, x102 + x202 + x302 + x402 + x502 + x602 + x702 == 1)
@constraint(m, e82, x103 + x203 + x303 + x403 + x503 + x603 + x703 == 1)
@constraint(m, e83, x104 + x204 + x304 + x404 + x504 + x604 + x704 == 1)
@constraint(m, e84, x105 + x205 + x305 + x405 + x505 + x605 + x705 == 1)
@constraint(m, e85, x106 + x206 + x306 + x406 + x506 + x606 + x706 == 1)
@constraint(m, e86, x107 + x207 + x307 + x407 + x507 + x607 + x707 == 1)
@constraint(m, e87, x108 + x208 + x308 + x408 + x508 + x608 + x708 == 1)
@constraint(m, e88, x109 + x209 + x309 + x409 + x509 + x609 + x709 == 1)
@constraint(m, e89, x110 + x210 + x310 + x410 + x510 + x610 + x710 == 1)
@constraint(m, e90, x111 + x211 + x311 + x411 + x511 + x611 + x711 == 1)
@constraint(m, e91, x112 + x212 + x312 + x412 + x512 + x612 + x712 == 1)
@constraint(m, e92, x113 + x213 + x313 + x413 + x513 + x613 + x713 == 1)
@constraint(m, e93, x114 + x214 + x314 + x414 + x514 + x614 + x714 == 1)
@constraint(m, e94, x115 + x215 + x315 + x415 + x515 + x615 + x715 == 1)
@constraint(m, e95, x116 + x216 + x316 + x416 + x516 + x616 + x716 == 1)
@constraint(m, e96, x117 + x217 + x317 + x417 + x517 + x617 + x717 == 1)
@constraint(m, e97, x118 + x218 + x318 + x418 + x518 + x618 + x718 == 1)
@constraint(m, e98, x119 + x219 + x319 + x419 + x519 + x619 + x719 == 1)
@constraint(m, e99, x120 + x220 + x320 + x420 + x520 + x620 + x720 == 1)
@constraint(m, e100, x121 + x221 + x321 + x421 + x521 + x621 + x721 == 1)
