# NLP written by GAMS Convert at 05/15/24 11:33:56
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       500      500        0        0        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#      1509     1509        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#      1500     1500        0
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
@variable(m, 0 <= x722 <= 1, start=0)
@variable(m, 0 <= x723 <= 1, start=0)
@variable(m, 0 <= x724 <= 1, start=0)
@variable(m, 0 <= x725 <= 1, start=0)
@variable(m, 0 <= x726 <= 1, start=0)
@variable(m, 0 <= x727 <= 1, start=0)
@variable(m, 0 <= x728 <= 1, start=0)
@variable(m, 0 <= x729 <= 1, start=0)
@variable(m, 0 <= x730 <= 1, start=0)
@variable(m, 0 <= x731 <= 1, start=0)
@variable(m, 0 <= x732 <= 1, start=0)
@variable(m, 0 <= x733 <= 1, start=0)
@variable(m, 0 <= x734 <= 1, start=0)
@variable(m, 0 <= x735 <= 1, start=0)
@variable(m, 0 <= x736 <= 1, start=0)
@variable(m, 0 <= x737 <= 1, start=0)
@variable(m, 0 <= x738 <= 1, start=0)
@variable(m, 0 <= x739 <= 1, start=0)
@variable(m, 0 <= x740 <= 1, start=0)
@variable(m, 0 <= x741 <= 1, start=0)
@variable(m, 0 <= x742 <= 1, start=0)
@variable(m, 0 <= x743 <= 1, start=0)
@variable(m, 0 <= x744 <= 1, start=0)
@variable(m, 0 <= x745 <= 1, start=0)
@variable(m, 0 <= x746 <= 1, start=0)
@variable(m, 0 <= x747 <= 1, start=0)
@variable(m, 0 <= x748 <= 1, start=0)
@variable(m, 0 <= x749 <= 1, start=0)
@variable(m, 0 <= x750 <= 1, start=0)
@variable(m, 0 <= x751 <= 1, start=0)
@variable(m, 0 <= x752 <= 1, start=0)
@variable(m, 0 <= x753 <= 1, start=0)
@variable(m, 0 <= x754 <= 1, start=0)
@variable(m, 0 <= x755 <= 1, start=0)
@variable(m, 0 <= x756 <= 1, start=0)
@variable(m, 0 <= x757 <= 1, start=0)
@variable(m, 0 <= x758 <= 1, start=0)
@variable(m, 0 <= x759 <= 1, start=0)
@variable(m, 0 <= x760 <= 1, start=0)
@variable(m, 0 <= x761 <= 1, start=0)
@variable(m, 0 <= x762 <= 1, start=0)
@variable(m, 0 <= x763 <= 1, start=0)
@variable(m, 0 <= x764 <= 1, start=0)
@variable(m, 0 <= x765 <= 1, start=0)
@variable(m, 0 <= x766 <= 1, start=0)
@variable(m, 0 <= x767 <= 1, start=0)
@variable(m, 0 <= x768 <= 1, start=0)
@variable(m, 0 <= x769 <= 1, start=0)
@variable(m, 0 <= x770 <= 1, start=0)
@variable(m, 0 <= x771 <= 1, start=0)
@variable(m, 0 <= x772 <= 1, start=0)
@variable(m, 0 <= x773 <= 1, start=0)
@variable(m, 0 <= x774 <= 1, start=0)
@variable(m, 0 <= x775 <= 1, start=0)
@variable(m, 0 <= x776 <= 1, start=0)
@variable(m, 0 <= x777 <= 1, start=0)
@variable(m, 0 <= x778 <= 1, start=0)
@variable(m, 0 <= x779 <= 1, start=0)
@variable(m, 0 <= x780 <= 1, start=0)
@variable(m, 0 <= x781 <= 1, start=0)
@variable(m, 0 <= x782 <= 1, start=0)
@variable(m, 0 <= x783 <= 1, start=0)
@variable(m, 0 <= x784 <= 1, start=0)
@variable(m, 0 <= x785 <= 1, start=0)
@variable(m, 0 <= x786 <= 1, start=0)
@variable(m, 0 <= x787 <= 1, start=0)
@variable(m, 0 <= x788 <= 1, start=0)
@variable(m, 0 <= x789 <= 1, start=0)
@variable(m, 0 <= x790 <= 1, start=0)
@variable(m, 0 <= x791 <= 1, start=0)
@variable(m, 0 <= x792 <= 1, start=0)
@variable(m, 0 <= x793 <= 1, start=0)
@variable(m, 0 <= x794 <= 1, start=0)
@variable(m, 0 <= x795 <= 1, start=0)
@variable(m, 0 <= x796 <= 1, start=0)
@variable(m, 0 <= x797 <= 1, start=0)
@variable(m, 0 <= x798 <= 1, start=0)
@variable(m, 0 <= x799 <= 1, start=0)
@variable(m, 0 <= x800 <= 1, start=0)
@variable(m, 0 <= x801 <= 1, start=0)
@variable(m, 0 <= x802 <= 1, start=0)
@variable(m, 0 <= x803 <= 1, start=0)
@variable(m, 0 <= x804 <= 1, start=0)
@variable(m, 0 <= x805 <= 1, start=0)
@variable(m, 0 <= x806 <= 1, start=0)
@variable(m, 0 <= x807 <= 1, start=0)
@variable(m, 0 <= x808 <= 1, start=0)
@variable(m, 0 <= x809 <= 1, start=0)
@variable(m, 0 <= x810 <= 1, start=0)
@variable(m, 0 <= x811 <= 1, start=0)
@variable(m, 0 <= x812 <= 1, start=0)
@variable(m, 0 <= x813 <= 1, start=0)
@variable(m, 0 <= x814 <= 1, start=0)
@variable(m, 0 <= x815 <= 1, start=0)
@variable(m, 0 <= x816 <= 1, start=0)
@variable(m, 0 <= x817 <= 1, start=0)
@variable(m, 0 <= x818 <= 1, start=0)
@variable(m, 0 <= x819 <= 1, start=0)
@variable(m, 0 <= x820 <= 1, start=0)
@variable(m, 0 <= x821 <= 1, start=0)
@variable(m, 0 <= x822 <= 1, start=0)
@variable(m, 0 <= x823 <= 1, start=0)
@variable(m, 0 <= x824 <= 1, start=0)
@variable(m, 0 <= x825 <= 1, start=0)
@variable(m, 0 <= x826 <= 1, start=0)
@variable(m, 0 <= x827 <= 1, start=0)
@variable(m, 0 <= x828 <= 1, start=0)
@variable(m, 0 <= x829 <= 1, start=0)
@variable(m, 0 <= x830 <= 1, start=0)
@variable(m, 0 <= x831 <= 1, start=0)
@variable(m, 0 <= x832 <= 1, start=0)
@variable(m, 0 <= x833 <= 1, start=0)
@variable(m, 0 <= x834 <= 1, start=0)
@variable(m, 0 <= x835 <= 1, start=0)
@variable(m, 0 <= x836 <= 1, start=0)
@variable(m, 0 <= x837 <= 1, start=0)
@variable(m, 0 <= x838 <= 1, start=0)
@variable(m, 0 <= x839 <= 1, start=0)
@variable(m, 0 <= x840 <= 1, start=0)
@variable(m, 0 <= x841 <= 1, start=0)
@variable(m, 0 <= x842 <= 1, start=0)
@variable(m, 0 <= x843 <= 1, start=0)
@variable(m, 0 <= x844 <= 1, start=0)
@variable(m, 0 <= x845 <= 1, start=0)
@variable(m, 0 <= x846 <= 1, start=0)
@variable(m, 0 <= x847 <= 1, start=0)
@variable(m, 0 <= x848 <= 1, start=0)
@variable(m, 0 <= x849 <= 1, start=0)
@variable(m, 0 <= x850 <= 1, start=0)
@variable(m, 0 <= x851 <= 1, start=0)
@variable(m, 0 <= x852 <= 1, start=0)
@variable(m, 0 <= x853 <= 1, start=0)
@variable(m, 0 <= x854 <= 1, start=0)
@variable(m, 0 <= x855 <= 1, start=0)
@variable(m, 0 <= x856 <= 1, start=0)
@variable(m, 0 <= x857 <= 1, start=0)
@variable(m, 0 <= x858 <= 1, start=0)
@variable(m, 0 <= x859 <= 1, start=0)
@variable(m, 0 <= x860 <= 1, start=0)
@variable(m, 0 <= x861 <= 1, start=0)
@variable(m, 0 <= x862 <= 1, start=0)
@variable(m, 0 <= x863 <= 1, start=0)
@variable(m, 0 <= x864 <= 1, start=0)
@variable(m, 0 <= x865 <= 1, start=0)
@variable(m, 0 <= x866 <= 1, start=0)
@variable(m, 0 <= x867 <= 1, start=0)
@variable(m, 0 <= x868 <= 1, start=0)
@variable(m, 0 <= x869 <= 1, start=0)
@variable(m, 0 <= x870 <= 1, start=0)
@variable(m, 0 <= x871 <= 1, start=0)
@variable(m, 0 <= x872 <= 1, start=0)
@variable(m, 0 <= x873 <= 1, start=0)
@variable(m, 0 <= x874 <= 1, start=0)
@variable(m, 0 <= x875 <= 1, start=0)
@variable(m, 0 <= x876 <= 1, start=0)
@variable(m, 0 <= x877 <= 1, start=0)
@variable(m, 0 <= x878 <= 1, start=0)
@variable(m, 0 <= x879 <= 1, start=0)
@variable(m, 0 <= x880 <= 1, start=0)
@variable(m, 0 <= x881 <= 1, start=0)
@variable(m, 0 <= x882 <= 1, start=0)
@variable(m, 0 <= x883 <= 1, start=0)
@variable(m, 0 <= x884 <= 1, start=0)
@variable(m, 0 <= x885 <= 1, start=0)
@variable(m, 0 <= x886 <= 1, start=0)
@variable(m, 0 <= x887 <= 1, start=0)
@variable(m, 0 <= x888 <= 1, start=0)
@variable(m, 0 <= x889 <= 1, start=0)
@variable(m, 0 <= x890 <= 1, start=0)
@variable(m, 0 <= x891 <= 1, start=0)
@variable(m, 0 <= x892 <= 1, start=0)
@variable(m, 0 <= x893 <= 1, start=0)
@variable(m, 0 <= x894 <= 1, start=0)
@variable(m, 0 <= x895 <= 1, start=0)
@variable(m, 0 <= x896 <= 1, start=0)
@variable(m, 0 <= x897 <= 1, start=0)
@variable(m, 0 <= x898 <= 1, start=0)
@variable(m, 0 <= x899 <= 1, start=0)
@variable(m, 0 <= x900 <= 1, start=0)
@variable(m, 0 <= x901 <= 1, start=0)
@variable(m, 0 <= x902 <= 1, start=0)
@variable(m, 0 <= x903 <= 1, start=0)
@variable(m, 0 <= x904 <= 1, start=0)
@variable(m, 0 <= x905 <= 1, start=0)
@variable(m, 0 <= x906 <= 1, start=0)
@variable(m, 0 <= x907 <= 1, start=0)
@variable(m, 0 <= x908 <= 1, start=0)
@variable(m, 0 <= x909 <= 1, start=0)
@variable(m, 0 <= x910 <= 1, start=0)
@variable(m, 0 <= x911 <= 1, start=0)
@variable(m, 0 <= x912 <= 1, start=0)
@variable(m, 0 <= x913 <= 1, start=0)
@variable(m, 0 <= x914 <= 1, start=0)
@variable(m, 0 <= x915 <= 1, start=0)
@variable(m, 0 <= x916 <= 1, start=0)
@variable(m, 0 <= x917 <= 1, start=0)
@variable(m, 0 <= x918 <= 1, start=0)
@variable(m, 0 <= x919 <= 1, start=0)
@variable(m, 0 <= x920 <= 1, start=0)
@variable(m, 0 <= x921 <= 1, start=0)
@variable(m, 0 <= x922 <= 1, start=0)
@variable(m, 0 <= x923 <= 1, start=0)
@variable(m, 0 <= x924 <= 1, start=0)
@variable(m, 0 <= x925 <= 1, start=0)
@variable(m, 0 <= x926 <= 1, start=0)
@variable(m, 0 <= x927 <= 1, start=0)
@variable(m, 0 <= x928 <= 1, start=0)
@variable(m, 0 <= x929 <= 1, start=0)
@variable(m, 0 <= x930 <= 1, start=0)
@variable(m, 0 <= x931 <= 1, start=0)
@variable(m, 0 <= x932 <= 1, start=0)
@variable(m, 0 <= x933 <= 1, start=0)
@variable(m, 0 <= x934 <= 1, start=0)
@variable(m, 0 <= x935 <= 1, start=0)
@variable(m, 0 <= x936 <= 1, start=0)
@variable(m, 0 <= x937 <= 1, start=0)
@variable(m, 0 <= x938 <= 1, start=0)
@variable(m, 0 <= x939 <= 1, start=0)
@variable(m, 0 <= x940 <= 1, start=0)
@variable(m, 0 <= x941 <= 1, start=0)
@variable(m, 0 <= x942 <= 1, start=0)
@variable(m, 0 <= x943 <= 1, start=0)
@variable(m, 0 <= x944 <= 1, start=0)
@variable(m, 0 <= x945 <= 1, start=0)
@variable(m, 0 <= x946 <= 1, start=0)
@variable(m, 0 <= x947 <= 1, start=0)
@variable(m, 0 <= x948 <= 1, start=0)
@variable(m, 0 <= x949 <= 1, start=0)
@variable(m, 0 <= x950 <= 1, start=0)
@variable(m, 0 <= x951 <= 1, start=0)
@variable(m, 0 <= x952 <= 1, start=0)
@variable(m, 0 <= x953 <= 1, start=0)
@variable(m, 0 <= x954 <= 1, start=0)
@variable(m, 0 <= x955 <= 1, start=0)
@variable(m, 0 <= x956 <= 1, start=0)
@variable(m, 0 <= x957 <= 1, start=0)
@variable(m, 0 <= x958 <= 1, start=0)
@variable(m, 0 <= x959 <= 1, start=0)
@variable(m, 0 <= x960 <= 1, start=0)
@variable(m, 0 <= x961 <= 1, start=0)
@variable(m, 0 <= x962 <= 1, start=0)
@variable(m, 0 <= x963 <= 1, start=0)
@variable(m, 0 <= x964 <= 1, start=0)
@variable(m, 0 <= x965 <= 1, start=0)
@variable(m, 0 <= x966 <= 1, start=0)
@variable(m, 0 <= x967 <= 1, start=0)
@variable(m, 0 <= x968 <= 1, start=0)
@variable(m, 0 <= x969 <= 1, start=0)
@variable(m, 0 <= x970 <= 1, start=0)
@variable(m, 0 <= x971 <= 1, start=0)
@variable(m, 0 <= x972 <= 1, start=0)
@variable(m, 0 <= x973 <= 1, start=0)
@variable(m, 0 <= x974 <= 1, start=0)
@variable(m, 0 <= x975 <= 1, start=0)
@variable(m, 0 <= x976 <= 1, start=0)
@variable(m, 0 <= x977 <= 1, start=0)
@variable(m, 0 <= x978 <= 1, start=0)
@variable(m, 0 <= x979 <= 1, start=0)
@variable(m, 0 <= x980 <= 1, start=0)
@variable(m, 0 <= x981 <= 1, start=0)
@variable(m, 0 <= x982 <= 1, start=0)
@variable(m, 0 <= x983 <= 1, start=0)
@variable(m, 0 <= x984 <= 1, start=0)
@variable(m, 0 <= x985 <= 1, start=0)
@variable(m, 0 <= x986 <= 1, start=0)
@variable(m, 0 <= x987 <= 1, start=0)
@variable(m, 0 <= x988 <= 1, start=0)
@variable(m, 0 <= x989 <= 1, start=0)
@variable(m, 0 <= x990 <= 1, start=0)
@variable(m, 0 <= x991 <= 1, start=0)
@variable(m, 0 <= x992 <= 1, start=0)
@variable(m, 0 <= x993 <= 1, start=0)
@variable(m, 0 <= x994 <= 1, start=0)
@variable(m, 0 <= x995 <= 1, start=0)
@variable(m, 0 <= x996 <= 1, start=0)
@variable(m, 0 <= x997 <= 1, start=0)
@variable(m, 0 <= x998 <= 1, start=0)
@variable(m, 0 <= x999 <= 1, start=0)
@variable(m, 0 <= x1000 <= 1, start=0)
@variable(m, 0 <= x1001 <= 1, start=0)
@variable(m, 0 <= x1002 <= 1, start=0)
@variable(m, 0 <= x1003 <= 1, start=0)
@variable(m, 0 <= x1004 <= 1, start=0)
@variable(m, 0 <= x1005 <= 1, start=0)
@variable(m, 0 <= x1006 <= 1, start=0)
@variable(m, 0 <= x1007 <= 1, start=0)
@variable(m, 0 <= x1008 <= 1, start=0)
@variable(m, 0 <= x1009 <= 1, start=0)
@variable(m, 0 <= x1010 <= 1, start=0)
@variable(m, 0 <= x1011 <= 1, start=0)
@variable(m, 0 <= x1012 <= 1, start=0)
@variable(m, 0 <= x1013 <= 1, start=0)
@variable(m, 0 <= x1014 <= 1, start=0)
@variable(m, 0 <= x1015 <= 1, start=0)
@variable(m, 0 <= x1016 <= 1, start=0)
@variable(m, 0 <= x1017 <= 1, start=0)
@variable(m, 0 <= x1018 <= 1, start=0)
@variable(m, 0 <= x1019 <= 1, start=0)
@variable(m, 0 <= x1020 <= 1, start=0)
@variable(m, 0 <= x1021 <= 1, start=0)
@variable(m, 0 <= x1022 <= 1, start=0)
@variable(m, 0 <= x1023 <= 1, start=0)
@variable(m, 0 <= x1024 <= 1, start=0)
@variable(m, 0 <= x1025 <= 1, start=0)
@variable(m, 0 <= x1026 <= 1, start=0)
@variable(m, 0 <= x1027 <= 1, start=0)
@variable(m, 0 <= x1028 <= 1, start=0)
@variable(m, 0 <= x1029 <= 1, start=0)
@variable(m, 0 <= x1030 <= 1, start=0)
@variable(m, 0 <= x1031 <= 1, start=0)
@variable(m, 0 <= x1032 <= 1, start=0)
@variable(m, 0 <= x1033 <= 1, start=0)
@variable(m, 0 <= x1034 <= 1, start=0)
@variable(m, 0 <= x1035 <= 1, start=0)
@variable(m, 0 <= x1036 <= 1, start=0)
@variable(m, 0 <= x1037 <= 1, start=0)
@variable(m, 0 <= x1038 <= 1, start=0)
@variable(m, 0 <= x1039 <= 1, start=0)
@variable(m, 0 <= x1040 <= 1, start=0)
@variable(m, 0 <= x1041 <= 1, start=0)
@variable(m, 0 <= x1042 <= 1, start=0)
@variable(m, 0 <= x1043 <= 1, start=0)
@variable(m, 0 <= x1044 <= 1, start=0)
@variable(m, 0 <= x1045 <= 1, start=0)
@variable(m, 0 <= x1046 <= 1, start=0)
@variable(m, 0 <= x1047 <= 1, start=0)
@variable(m, 0 <= x1048 <= 1, start=0)
@variable(m, 0 <= x1049 <= 1, start=0)
@variable(m, 0 <= x1050 <= 1, start=0)
@variable(m, 0 <= x1051 <= 1, start=0)
@variable(m, 0 <= x1052 <= 1, start=0)
@variable(m, 0 <= x1053 <= 1, start=0)
@variable(m, 0 <= x1054 <= 1, start=0)
@variable(m, 0 <= x1055 <= 1, start=0)
@variable(m, 0 <= x1056 <= 1, start=0)
@variable(m, 0 <= x1057 <= 1, start=0)
@variable(m, 0 <= x1058 <= 1, start=0)
@variable(m, 0 <= x1059 <= 1, start=0)
@variable(m, 0 <= x1060 <= 1, start=0)
@variable(m, 0 <= x1061 <= 1, start=0)
@variable(m, 0 <= x1062 <= 1, start=0)
@variable(m, 0 <= x1063 <= 1, start=0)
@variable(m, 0 <= x1064 <= 1, start=0)
@variable(m, 0 <= x1065 <= 1, start=0)
@variable(m, 0 <= x1066 <= 1, start=0)
@variable(m, 0 <= x1067 <= 1, start=0)
@variable(m, 0 <= x1068 <= 1, start=0)
@variable(m, 0 <= x1069 <= 1, start=0)
@variable(m, 0 <= x1070 <= 1, start=0)
@variable(m, 0 <= x1071 <= 1, start=0)
@variable(m, 0 <= x1072 <= 1, start=0)
@variable(m, 0 <= x1073 <= 1, start=0)
@variable(m, 0 <= x1074 <= 1, start=0)
@variable(m, 0 <= x1075 <= 1, start=0)
@variable(m, 0 <= x1076 <= 1, start=0)
@variable(m, 0 <= x1077 <= 1, start=0)
@variable(m, 0 <= x1078 <= 1, start=0)
@variable(m, 0 <= x1079 <= 1, start=0)
@variable(m, 0 <= x1080 <= 1, start=0)
@variable(m, 0 <= x1081 <= 1, start=0)
@variable(m, 0 <= x1082 <= 1, start=0)
@variable(m, 0 <= x1083 <= 1, start=0)
@variable(m, 0 <= x1084 <= 1, start=0)
@variable(m, 0 <= x1085 <= 1, start=0)
@variable(m, 0 <= x1086 <= 1, start=0)
@variable(m, 0 <= x1087 <= 1, start=0)
@variable(m, 0 <= x1088 <= 1, start=0)
@variable(m, 0 <= x1089 <= 1, start=0)
@variable(m, 0 <= x1090 <= 1, start=0)
@variable(m, 0 <= x1091 <= 1, start=0)
@variable(m, 0 <= x1092 <= 1, start=0)
@variable(m, 0 <= x1093 <= 1, start=0)
@variable(m, 0 <= x1094 <= 1, start=0)
@variable(m, 0 <= x1095 <= 1, start=0)
@variable(m, 0 <= x1096 <= 1, start=0)
@variable(m, 0 <= x1097 <= 1, start=0)
@variable(m, 0 <= x1098 <= 1, start=0)
@variable(m, 0 <= x1099 <= 1, start=0)
@variable(m, 0 <= x1100 <= 1, start=0)
@variable(m, 0 <= x1101 <= 1, start=0)
@variable(m, 0 <= x1102 <= 1, start=0)
@variable(m, 0 <= x1103 <= 1, start=0)
@variable(m, 0 <= x1104 <= 1, start=0)
@variable(m, 0 <= x1105 <= 1, start=0)
@variable(m, 0 <= x1106 <= 1, start=0)
@variable(m, 0 <= x1107 <= 1, start=0)
@variable(m, 0 <= x1108 <= 1, start=0)
@variable(m, 0 <= x1109 <= 1, start=0)
@variable(m, 0 <= x1110 <= 1, start=0)
@variable(m, 0 <= x1111 <= 1, start=0)
@variable(m, 0 <= x1112 <= 1, start=0)
@variable(m, 0 <= x1113 <= 1, start=0)
@variable(m, 0 <= x1114 <= 1, start=0)
@variable(m, 0 <= x1115 <= 1, start=0)
@variable(m, 0 <= x1116 <= 1, start=0)
@variable(m, 0 <= x1117 <= 1, start=0)
@variable(m, 0 <= x1118 <= 1, start=0)
@variable(m, 0 <= x1119 <= 1, start=0)
@variable(m, 0 <= x1120 <= 1, start=0)
@variable(m, 0 <= x1121 <= 1, start=0)
@variable(m, 0 <= x1122 <= 1, start=0)
@variable(m, 0 <= x1123 <= 1, start=0)
@variable(m, 0 <= x1124 <= 1, start=0)
@variable(m, 0 <= x1125 <= 1, start=0)
@variable(m, 0 <= x1126 <= 1, start=0)
@variable(m, 0 <= x1127 <= 1, start=0)
@variable(m, 0 <= x1128 <= 1, start=0)
@variable(m, 0 <= x1129 <= 1, start=0)
@variable(m, 0 <= x1130 <= 1, start=0)
@variable(m, 0 <= x1131 <= 1, start=0)
@variable(m, 0 <= x1132 <= 1, start=0)
@variable(m, 0 <= x1133 <= 1, start=0)
@variable(m, 0 <= x1134 <= 1, start=0)
@variable(m, 0 <= x1135 <= 1, start=0)
@variable(m, 0 <= x1136 <= 1, start=0)
@variable(m, 0 <= x1137 <= 1, start=0)
@variable(m, 0 <= x1138 <= 1, start=0)
@variable(m, 0 <= x1139 <= 1, start=0)
@variable(m, 0 <= x1140 <= 1, start=0)
@variable(m, 0 <= x1141 <= 1, start=0)
@variable(m, 0 <= x1142 <= 1, start=0)
@variable(m, 0 <= x1143 <= 1, start=0)
@variable(m, 0 <= x1144 <= 1, start=0)
@variable(m, 0 <= x1145 <= 1, start=0)
@variable(m, 0 <= x1146 <= 1, start=0)
@variable(m, 0 <= x1147 <= 1, start=0)
@variable(m, 0 <= x1148 <= 1, start=0)
@variable(m, 0 <= x1149 <= 1, start=0)
@variable(m, 0 <= x1150 <= 1, start=0)
@variable(m, 0 <= x1151 <= 1, start=0)
@variable(m, 0 <= x1152 <= 1, start=0)
@variable(m, 0 <= x1153 <= 1, start=0)
@variable(m, 0 <= x1154 <= 1, start=0)
@variable(m, 0 <= x1155 <= 1, start=0)
@variable(m, 0 <= x1156 <= 1, start=0)
@variable(m, 0 <= x1157 <= 1, start=0)
@variable(m, 0 <= x1158 <= 1, start=0)
@variable(m, 0 <= x1159 <= 1, start=0)
@variable(m, 0 <= x1160 <= 1, start=0)
@variable(m, 0 <= x1161 <= 1, start=0)
@variable(m, 0 <= x1162 <= 1, start=0)
@variable(m, 0 <= x1163 <= 1, start=0)
@variable(m, 0 <= x1164 <= 1, start=0)
@variable(m, 0 <= x1165 <= 1, start=0)
@variable(m, 0 <= x1166 <= 1, start=0)
@variable(m, 0 <= x1167 <= 1, start=0)
@variable(m, 0 <= x1168 <= 1, start=0)
@variable(m, 0 <= x1169 <= 1, start=0)
@variable(m, 0 <= x1170 <= 1, start=0)
@variable(m, 0 <= x1171 <= 1, start=0)
@variable(m, 0 <= x1172 <= 1, start=0)
@variable(m, 0 <= x1173 <= 1, start=0)
@variable(m, 0 <= x1174 <= 1, start=0)
@variable(m, 0 <= x1175 <= 1, start=0)
@variable(m, 0 <= x1176 <= 1, start=0)
@variable(m, 0 <= x1177 <= 1, start=0)
@variable(m, 0 <= x1178 <= 1, start=0)
@variable(m, 0 <= x1179 <= 1, start=0)
@variable(m, 0 <= x1180 <= 1, start=0)
@variable(m, 0 <= x1181 <= 1, start=0)
@variable(m, 0 <= x1182 <= 1, start=0)
@variable(m, 0 <= x1183 <= 1, start=0)
@variable(m, 0 <= x1184 <= 1, start=0)
@variable(m, 0 <= x1185 <= 1, start=0)
@variable(m, 0 <= x1186 <= 1, start=0)
@variable(m, 0 <= x1187 <= 1, start=0)
@variable(m, 0 <= x1188 <= 1, start=0)
@variable(m, 0 <= x1189 <= 1, start=0)
@variable(m, 0 <= x1190 <= 1, start=0)
@variable(m, 0 <= x1191 <= 1, start=0)
@variable(m, 0 <= x1192 <= 1, start=0)
@variable(m, 0 <= x1193 <= 1, start=0)
@variable(m, 0 <= x1194 <= 1, start=0)
@variable(m, 0 <= x1195 <= 1, start=0)
@variable(m, 0 <= x1196 <= 1, start=0)
@variable(m, 0 <= x1197 <= 1, start=0)
@variable(m, 0 <= x1198 <= 1, start=0)
@variable(m, 0 <= x1199 <= 1, start=0)
@variable(m, 0 <= x1200 <= 1, start=0)
@variable(m, 0 <= x1201 <= 1, start=0)
@variable(m, 0 <= x1202 <= 1, start=0)
@variable(m, 0 <= x1203 <= 1, start=0)
@variable(m, 0 <= x1204 <= 1, start=0)
@variable(m, 0 <= x1205 <= 1, start=0)
@variable(m, 0 <= x1206 <= 1, start=0)
@variable(m, 0 <= x1207 <= 1, start=0)
@variable(m, 0 <= x1208 <= 1, start=0)
@variable(m, 0 <= x1209 <= 1, start=0)
@variable(m, 0 <= x1210 <= 1, start=0)
@variable(m, 0 <= x1211 <= 1, start=0)
@variable(m, 0 <= x1212 <= 1, start=0)
@variable(m, 0 <= x1213 <= 1, start=0)
@variable(m, 0 <= x1214 <= 1, start=0)
@variable(m, 0 <= x1215 <= 1, start=0)
@variable(m, 0 <= x1216 <= 1, start=0)
@variable(m, 0 <= x1217 <= 1, start=0)
@variable(m, 0 <= x1218 <= 1, start=0)
@variable(m, 0 <= x1219 <= 1, start=0)
@variable(m, 0 <= x1220 <= 1, start=0)
@variable(m, 0 <= x1221 <= 1, start=0)
@variable(m, 0 <= x1222 <= 1, start=0)
@variable(m, 0 <= x1223 <= 1, start=0)
@variable(m, 0 <= x1224 <= 1, start=0)
@variable(m, 0 <= x1225 <= 1, start=0)
@variable(m, 0 <= x1226 <= 1, start=0)
@variable(m, 0 <= x1227 <= 1, start=0)
@variable(m, 0 <= x1228 <= 1, start=0)
@variable(m, 0 <= x1229 <= 1, start=0)
@variable(m, 0 <= x1230 <= 1, start=0)
@variable(m, 0 <= x1231 <= 1, start=0)
@variable(m, 0 <= x1232 <= 1, start=0)
@variable(m, 0 <= x1233 <= 1, start=0)
@variable(m, 0 <= x1234 <= 1, start=0)
@variable(m, 0 <= x1235 <= 1, start=0)
@variable(m, 0 <= x1236 <= 1, start=0)
@variable(m, 0 <= x1237 <= 1, start=0)
@variable(m, 0 <= x1238 <= 1, start=0)
@variable(m, 0 <= x1239 <= 1, start=0)
@variable(m, 0 <= x1240 <= 1, start=0)
@variable(m, 0 <= x1241 <= 1, start=0)
@variable(m, 0 <= x1242 <= 1, start=0)
@variable(m, 0 <= x1243 <= 1, start=0)
@variable(m, 0 <= x1244 <= 1, start=0)
@variable(m, 0 <= x1245 <= 1, start=0)
@variable(m, 0 <= x1246 <= 1, start=0)
@variable(m, 0 <= x1247 <= 1, start=0)
@variable(m, 0 <= x1248 <= 1, start=0)
@variable(m, 0 <= x1249 <= 1, start=0)
@variable(m, 0 <= x1250 <= 1, start=0)
@variable(m, 0 <= x1251 <= 1, start=0)
@variable(m, 0 <= x1252 <= 1, start=0)
@variable(m, 0 <= x1253 <= 1, start=0)
@variable(m, 0 <= x1254 <= 1, start=0)
@variable(m, 0 <= x1255 <= 1, start=0)
@variable(m, 0 <= x1256 <= 1, start=0)
@variable(m, 0 <= x1257 <= 1, start=0)
@variable(m, 0 <= x1258 <= 1, start=0)
@variable(m, 0 <= x1259 <= 1, start=0)
@variable(m, 0 <= x1260 <= 1, start=0)
@variable(m, 0 <= x1261 <= 1, start=0)
@variable(m, 0 <= x1262 <= 1, start=0)
@variable(m, 0 <= x1263 <= 1, start=0)
@variable(m, 0 <= x1264 <= 1, start=0)
@variable(m, 0 <= x1265 <= 1, start=0)
@variable(m, 0 <= x1266 <= 1, start=0)
@variable(m, 0 <= x1267 <= 1, start=0)
@variable(m, 0 <= x1268 <= 1, start=0)
@variable(m, 0 <= x1269 <= 1, start=0)
@variable(m, 0 <= x1270 <= 1, start=0)
@variable(m, 0 <= x1271 <= 1, start=0)
@variable(m, 0 <= x1272 <= 1, start=0)
@variable(m, 0 <= x1273 <= 1, start=0)
@variable(m, 0 <= x1274 <= 1, start=0)
@variable(m, 0 <= x1275 <= 1, start=0)
@variable(m, 0 <= x1276 <= 1, start=0)
@variable(m, 0 <= x1277 <= 1, start=0)
@variable(m, 0 <= x1278 <= 1, start=0)
@variable(m, 0 <= x1279 <= 1, start=0)
@variable(m, 0 <= x1280 <= 1, start=0)
@variable(m, 0 <= x1281 <= 1, start=0)
@variable(m, 0 <= x1282 <= 1, start=0)
@variable(m, 0 <= x1283 <= 1, start=0)
@variable(m, 0 <= x1284 <= 1, start=0)
@variable(m, 0 <= x1285 <= 1, start=0)
@variable(m, 0 <= x1286 <= 1, start=0)
@variable(m, 0 <= x1287 <= 1, start=0)
@variable(m, 0 <= x1288 <= 1, start=0)
@variable(m, 0 <= x1289 <= 1, start=0)
@variable(m, 0 <= x1290 <= 1, start=0)
@variable(m, 0 <= x1291 <= 1, start=0)
@variable(m, 0 <= x1292 <= 1, start=0)
@variable(m, 0 <= x1293 <= 1, start=0)
@variable(m, 0 <= x1294 <= 1, start=0)
@variable(m, 0 <= x1295 <= 1, start=0)
@variable(m, 0 <= x1296 <= 1, start=0)
@variable(m, 0 <= x1297 <= 1, start=0)
@variable(m, 0 <= x1298 <= 1, start=0)
@variable(m, 0 <= x1299 <= 1, start=0)
@variable(m, 0 <= x1300 <= 1, start=0)
@variable(m, 0 <= x1301 <= 1, start=0)
@variable(m, 0 <= x1302 <= 1, start=0)
@variable(m, 0 <= x1303 <= 1, start=0)
@variable(m, 0 <= x1304 <= 1, start=0)
@variable(m, 0 <= x1305 <= 1, start=0)
@variable(m, 0 <= x1306 <= 1, start=0)
@variable(m, 0 <= x1307 <= 1, start=0)
@variable(m, 0 <= x1308 <= 1, start=0)
@variable(m, 0 <= x1309 <= 1, start=0)
@variable(m, 0 <= x1310 <= 1, start=0)
@variable(m, 0 <= x1311 <= 1, start=0)
@variable(m, 0 <= x1312 <= 1, start=0)
@variable(m, 0 <= x1313 <= 1, start=0)
@variable(m, 0 <= x1314 <= 1, start=0)
@variable(m, 0 <= x1315 <= 1, start=0)
@variable(m, 0 <= x1316 <= 1, start=0)
@variable(m, 0 <= x1317 <= 1, start=0)
@variable(m, 0 <= x1318 <= 1, start=0)
@variable(m, 0 <= x1319 <= 1, start=0)
@variable(m, 0 <= x1320 <= 1, start=0)
@variable(m, 0 <= x1321 <= 1, start=0)
@variable(m, 0 <= x1322 <= 1, start=0)
@variable(m, 0 <= x1323 <= 1, start=0)
@variable(m, 0 <= x1324 <= 1, start=0)
@variable(m, 0 <= x1325 <= 1, start=0)
@variable(m, 0 <= x1326 <= 1, start=0)
@variable(m, 0 <= x1327 <= 1, start=0)
@variable(m, 0 <= x1328 <= 1, start=0)
@variable(m, 0 <= x1329 <= 1, start=0)
@variable(m, 0 <= x1330 <= 1, start=0)
@variable(m, 0 <= x1331 <= 1, start=0)
@variable(m, 0 <= x1332 <= 1, start=0)
@variable(m, 0 <= x1333 <= 1, start=0)
@variable(m, 0 <= x1334 <= 1, start=0)
@variable(m, 0 <= x1335 <= 1, start=0)
@variable(m, 0 <= x1336 <= 1, start=0)
@variable(m, 0 <= x1337 <= 1, start=0)
@variable(m, 0 <= x1338 <= 1, start=0)
@variable(m, 0 <= x1339 <= 1, start=0)
@variable(m, 0 <= x1340 <= 1, start=0)
@variable(m, 0 <= x1341 <= 1, start=0)
@variable(m, 0 <= x1342 <= 1, start=0)
@variable(m, 0 <= x1343 <= 1, start=0)
@variable(m, 0 <= x1344 <= 1, start=0)
@variable(m, 0 <= x1345 <= 1, start=0)
@variable(m, 0 <= x1346 <= 1, start=0)
@variable(m, 0 <= x1347 <= 1, start=0)
@variable(m, 0 <= x1348 <= 1, start=0)
@variable(m, 0 <= x1349 <= 1, start=0)
@variable(m, 0 <= x1350 <= 1, start=0)
@variable(m, 0 <= x1351 <= 1, start=0)
@variable(m, 0 <= x1352 <= 1, start=0)
@variable(m, 0 <= x1353 <= 1, start=0)
@variable(m, 0 <= x1354 <= 1, start=0)
@variable(m, 0 <= x1355 <= 1, start=0)
@variable(m, 0 <= x1356 <= 1, start=0)
@variable(m, 0 <= x1357 <= 1, start=0)
@variable(m, 0 <= x1358 <= 1, start=0)
@variable(m, 0 <= x1359 <= 1, start=0)
@variable(m, 0 <= x1360 <= 1, start=0)
@variable(m, 0 <= x1361 <= 1, start=0)
@variable(m, 0 <= x1362 <= 1, start=0)
@variable(m, 0 <= x1363 <= 1, start=0)
@variable(m, 0 <= x1364 <= 1, start=0)
@variable(m, 0 <= x1365 <= 1, start=0)
@variable(m, 0 <= x1366 <= 1, start=0)
@variable(m, 0 <= x1367 <= 1, start=0)
@variable(m, 0 <= x1368 <= 1, start=0)
@variable(m, 0 <= x1369 <= 1, start=0)
@variable(m, 0 <= x1370 <= 1, start=0)
@variable(m, 0 <= x1371 <= 1, start=0)
@variable(m, 0 <= x1372 <= 1, start=0)
@variable(m, 0 <= x1373 <= 1, start=0)
@variable(m, 0 <= x1374 <= 1, start=0)
@variable(m, 0 <= x1375 <= 1, start=0)
@variable(m, 0 <= x1376 <= 1, start=0)
@variable(m, 0 <= x1377 <= 1, start=0)
@variable(m, 0 <= x1378 <= 1, start=0)
@variable(m, 0 <= x1379 <= 1, start=0)
@variable(m, 0 <= x1380 <= 1, start=0)
@variable(m, 0 <= x1381 <= 1, start=0)
@variable(m, 0 <= x1382 <= 1, start=0)
@variable(m, 0 <= x1383 <= 1, start=0)
@variable(m, 0 <= x1384 <= 1, start=0)
@variable(m, 0 <= x1385 <= 1, start=0)
@variable(m, 0 <= x1386 <= 1, start=0)
@variable(m, 0 <= x1387 <= 1, start=0)
@variable(m, 0 <= x1388 <= 1, start=0)
@variable(m, 0 <= x1389 <= 1, start=0)
@variable(m, 0 <= x1390 <= 1, start=0)
@variable(m, 0 <= x1391 <= 1, start=0)
@variable(m, 0 <= x1392 <= 1, start=0)
@variable(m, 0 <= x1393 <= 1, start=0)
@variable(m, 0 <= x1394 <= 1, start=0)
@variable(m, 0 <= x1395 <= 1, start=0)
@variable(m, 0 <= x1396 <= 1, start=0)
@variable(m, 0 <= x1397 <= 1, start=0)
@variable(m, 0 <= x1398 <= 1, start=0)
@variable(m, 0 <= x1399 <= 1, start=0)
@variable(m, 0 <= x1400 <= 1, start=0)
@variable(m, 0 <= x1401 <= 1, start=0)
@variable(m, 0 <= x1402 <= 1, start=0)
@variable(m, 0 <= x1403 <= 1, start=0)
@variable(m, 0 <= x1404 <= 1, start=0)
@variable(m, 0 <= x1405 <= 1, start=0)
@variable(m, 0 <= x1406 <= 1, start=0)
@variable(m, 0 <= x1407 <= 1, start=0)
@variable(m, 0 <= x1408 <= 1, start=0)
@variable(m, 0 <= x1409 <= 1, start=0)
@variable(m, 0 <= x1410 <= 1, start=0)
@variable(m, 0 <= x1411 <= 1, start=0)
@variable(m, 0 <= x1412 <= 1, start=0)
@variable(m, 0 <= x1413 <= 1, start=0)
@variable(m, 0 <= x1414 <= 1, start=0)
@variable(m, 0 <= x1415 <= 1, start=0)
@variable(m, 0 <= x1416 <= 1, start=0)
@variable(m, 0 <= x1417 <= 1, start=0)
@variable(m, 0 <= x1418 <= 1, start=0)
@variable(m, 0 <= x1419 <= 1, start=0)
@variable(m, 0 <= x1420 <= 1, start=0)
@variable(m, 0 <= x1421 <= 1, start=0)
@variable(m, 0 <= x1422 <= 1, start=0)
@variable(m, 0 <= x1423 <= 1, start=0)
@variable(m, 0 <= x1424 <= 1, start=0)
@variable(m, 0 <= x1425 <= 1, start=0)
@variable(m, 0 <= x1426 <= 1, start=0)
@variable(m, 0 <= x1427 <= 1, start=0)
@variable(m, 0 <= x1428 <= 1, start=0)
@variable(m, 0 <= x1429 <= 1, start=0)
@variable(m, 0 <= x1430 <= 1, start=0)
@variable(m, 0 <= x1431 <= 1, start=0)
@variable(m, 0 <= x1432 <= 1, start=0)
@variable(m, 0 <= x1433 <= 1, start=0)
@variable(m, 0 <= x1434 <= 1, start=0)
@variable(m, 0 <= x1435 <= 1, start=0)
@variable(m, 0 <= x1436 <= 1, start=0)
@variable(m, 0 <= x1437 <= 1, start=0)
@variable(m, 0 <= x1438 <= 1, start=0)
@variable(m, 0 <= x1439 <= 1, start=0)
@variable(m, 0 <= x1440 <= 1, start=0)
@variable(m, 0 <= x1441 <= 1, start=0)
@variable(m, 0 <= x1442 <= 1, start=0)
@variable(m, 0 <= x1443 <= 1, start=0)
@variable(m, 0 <= x1444 <= 1, start=0)
@variable(m, 0 <= x1445 <= 1, start=0)
@variable(m, 0 <= x1446 <= 1, start=0)
@variable(m, 0 <= x1447 <= 1, start=0)
@variable(m, 0 <= x1448 <= 1, start=0)
@variable(m, 0 <= x1449 <= 1, start=0)
@variable(m, 0 <= x1450 <= 1, start=0)
@variable(m, 0 <= x1451 <= 1, start=0)
@variable(m, 0 <= x1452 <= 1, start=0)
@variable(m, 0 <= x1453 <= 1, start=0)
@variable(m, 0 <= x1454 <= 1, start=0)
@variable(m, 0 <= x1455 <= 1, start=0)
@variable(m, 0 <= x1456 <= 1, start=0)
@variable(m, 0 <= x1457 <= 1, start=0)
@variable(m, 0 <= x1458 <= 1, start=0)
@variable(m, 0 <= x1459 <= 1, start=0)
@variable(m, 0 <= x1460 <= 1, start=0)
@variable(m, 0 <= x1461 <= 1, start=0)
@variable(m, 0 <= x1462 <= 1, start=0)
@variable(m, 0 <= x1463 <= 1, start=0)
@variable(m, 0 <= x1464 <= 1, start=0)
@variable(m, 0 <= x1465 <= 1, start=0)
@variable(m, 0 <= x1466 <= 1, start=0)
@variable(m, 0 <= x1467 <= 1, start=0)
@variable(m, 0 <= x1468 <= 1, start=0)
@variable(m, 0 <= x1469 <= 1, start=0)
@variable(m, 0 <= x1470 <= 1, start=0)
@variable(m, 0 <= x1471 <= 1, start=0)
@variable(m, 0 <= x1472 <= 1, start=0)
@variable(m, 0 <= x1473 <= 1, start=0)
@variable(m, 0 <= x1474 <= 1, start=0)
@variable(m, 0 <= x1475 <= 1, start=0)
@variable(m, 0 <= x1476 <= 1, start=0)
@variable(m, 0 <= x1477 <= 1, start=0)
@variable(m, 0 <= x1478 <= 1, start=0)
@variable(m, 0 <= x1479 <= 1, start=0)
@variable(m, 0 <= x1480 <= 1, start=0)
@variable(m, 0 <= x1481 <= 1, start=0)
@variable(m, 0 <= x1482 <= 1, start=0)
@variable(m, 0 <= x1483 <= 1, start=0)
@variable(m, 0 <= x1484 <= 1, start=0)
@variable(m, 0 <= x1485 <= 1, start=0)
@variable(m, 0 <= x1486 <= 1, start=0)
@variable(m, 0 <= x1487 <= 1, start=0)
@variable(m, 0 <= x1488 <= 1, start=0)
@variable(m, 0 <= x1489 <= 1, start=0)
@variable(m, 0 <= x1490 <= 1, start=0)
@variable(m, 0 <= x1491 <= 1, start=0)
@variable(m, 0 <= x1492 <= 1, start=0)
@variable(m, 0 <= x1493 <= 1, start=0)
@variable(m, 0 <= x1494 <= 1, start=0)
@variable(m, 0 <= x1495 <= 1, start=0)
@variable(m, 0 <= x1496 <= 1, start=0)
@variable(m, 0 <= x1497 <= 1, start=0)
@variable(m, 0 <= x1498 <= 1, start=0)
@variable(m, 0 <= x1499 <= 1, start=0)
@variable(m, 0 <= x1500 <= 1, start=0)
@variable(m, 0 <= x1501 <= 1, start=0)
@variable(m, 0 <= x1502 <= 1, start=0)
@variable(m, 0 <= x1503 <= 1, start=0)
@variable(m, 0 <= x1504 <= 1, start=0)
@variable(m, 0 <= x1505 <= 1, start=0)
@variable(m, 0 <= x1506 <= 1, start=0)
@variable(m, 0 <= x1507 <= 1, start=0)
@variable(m, 0 <= x1508 <= 1, start=0)
@variable(m, 0 <= x1509 <= 1, start=0)

@NLobjective(m, Min, x10 * ((-0.4640463436541785 + x1)^2 + (-0.1293137886728929
    + x2)^2 + (-0.1717745705908742 + x3)^2) + x11 * ((-0.1099965161408738 + x1)
    ^2 + (-0.7288891997489471 + x2)^2 + (-0.5812974922633755 + x3)^2) + x12 * (
    (-0.6918497277391157 + x1)^2 + (-0.20973658549886454 + x2)^2 + (
    -0.9916376137682873 + x3)^2) + x13 * ((-0.10214895121638168 + x1)^2 + (
    -0.4471617317045655 + x2)^2 + (-0.16723720460096436 + x3)^2) + x14 * ((
    -0.6359500594742937 + x1)^2 + (-0.26061637443601726 + x2)^2 + (
    -0.2816795076287437 + x3)^2) + x15 * ((-0.25944505466517365 + x1)^2 + (
    -0.2692384663732923 + x2)^2 + (-0.8325610020895001 + x3)^2) + x16 * ((
    -0.6284388376892046 + x1)^2 + (-0.35949079717409593 + x2)^2 + (
    -0.07225999789103066 + x3)^2) + x17 * ((-0.16701728419415074 + x1)^2 + (
    -0.9347771993757961 + x2)^2 + (-0.7666223410197908 + x3)^2) + x18 * ((
    -0.4221693374712633 + x1)^2 + (-0.9535156771220886 + x2)^2 + (
    -0.7574192303318398 + x3)^2) + x19 * ((-0.3448801407104496 + x1)^2 + (
    -0.8832949398016634 + x2)^2 + (-0.662248567565667 + x3)^2) + x20 * ((
    -0.084155570651406 + x1)^2 + (-0.17890412424092283 + x2)^2 + (
    -0.17388950075062537 + x3)^2) + x21 * ((-0.3916313023443915 + x1)^2 + (
    -0.019818007213793787 + x2)^2 + (-0.4569740922310289 + x3)^2) + x22 * ((
    -0.43181385423845964 + x1)^2 + (-0.6207687709011839 + x2)^2 + (
    -0.8592520589918983 + x3)^2) + x23 * ((-0.6487284790511446 + x1)^2 + (
    -0.7777238632207397 + x2)^2 + (-0.754096902035809 + x3)^2) + x24 * ((
    -0.8220434639163084 + x1)^2 + (-0.3741317795920437 + x2)^2 + (
    -0.8521093203138362 + x3)^2) + x25 * ((-0.7925713002121476 + x1)^2 + (
    -0.6036194154368819 + x2)^2 + (-0.8738614104363204 + x3)^2) + x26 * ((
    -0.5277139763548169 + x1)^2 + (-0.1993819110558287 + x2)^2 + (
    -0.5740216578606483 + x3)^2) + x27 * ((-0.41586747380620337 + x1)^2 + (
    -0.42388302044291193 + x2)^2 + (-0.2343053950781021 + x3)^2) + x28 * ((
    -0.5023781980401871 + x1)^2 + (-0.03818303029571113 + x2)^2 + (
    -0.6686132837122916 + x3)^2) + x29 * ((-0.6771457634322402 + x1)^2 + (
    -0.670453003754532 + x2)^2 + (-0.7277047293890516 + x3)^2) + x30 * ((
    -0.21786809597676893 + x1)^2 + (-0.08609770624017898 + x2)^2 + (
    -0.5475714527010952 + x3)^2) + x31 * ((-0.49880230295506545 + x1)^2 + (
    -0.1221804789346802 + x2)^2 + (-0.6985432568115264 + x3)^2) + x32 * ((
    -0.8088595862488974 + x1)^2 + (-0.32195887839650494 + x2)^2 + (
    -0.03760891748311046 + x3)^2) + x33 * ((-0.32995615684874324 + x1)^2 + (
    -0.3886013644913259 + x2)^2 + (-0.8469692211045076 + x3)^2) + x34 * ((
    -0.28669724151775544 + x1)^2 + (-0.7807597500251693 + x2)^2 + (
    -0.25528553923429653 + x3)^2) + x35 * ((-0.9488635103141098 + x1)^2 + (
    -0.43736211954180315 + x2)^2 + (-0.5982886678243227 + x3)^2) + x36 * ((
    -0.4466622010152166 + x1)^2 + (-0.6090348194282511 + x2)^2 + (
    -0.8670075403112468 + x3)^2) + x37 * ((-0.951037074725791 + x1)^2 + (
    -0.1407161090628133 + x2)^2 + (-0.13092171611554282 + x3)^2) + x38 * ((
    -0.5541921779696605 + x1)^2 + (-0.8135752021382663 + x2)^2 + (
    -0.3027451108170902 + x3)^2) + x39 * ((-0.5305963246394046 + x1)^2 + (
    -0.23800490595118307 + x2)^2 + (-0.6735380224500424 + x3)^2) + x40 * ((
    -0.5909678409002741 + x1)^2 + (-0.48993330795236645 + x2)^2 + (
    -0.678288644059539 + x3)^2) + x41 * ((-0.43028464262572896 + x1)^2 + (
    -0.18942101979564563 + x2)^2 + (-0.5387520132500516 + x3)^2) + x42 * ((
    -0.9240763867641095 + x1)^2 + (-0.626146721604441 + x2)^2 + (
    -0.6874440043145749 + x3)^2) + x43 * ((-0.8160616417563322 + x1)^2 + (
    -0.8985769697407207 + x2)^2 + (-0.7069074935285429 + x3)^2) + x44 * ((
    -0.70100419051915 + x1)^2 + (-0.4569577862776859 + x2)^2 + (
    -0.1471193271794946 + x3)^2) + x45 * ((-0.4285718440951606 + x1)^2 + (
    -0.8609883932856427 + x2)^2 + (-0.1410876060058085 + x3)^2) + x46 * ((
    -0.6332293940657829 + x1)^2 + (-0.8525493047471094 + x2)^2 + (
    -0.7321100368238428 + x3)^2) + x47 * ((-0.29503916007091424 + x1)^2 + (
    -0.4380701575264203 + x2)^2 + (-0.820365575773603 + x3)^2) + x48 * ((
    -0.23227503662891036 + x1)^2 + (-0.05055428546369656 + x2)^2 + (
    -0.14176384941021558 + x3)^2) + x49 * ((-0.5635448791654668 + x1)^2 + (
    -0.3059173029907377 + x2)^2 + (-0.737377855421216 + x3)^2) + x50 * ((
    -0.22436900298779006 + x1)^2 + (-0.5838557597663682 + x2)^2 + (
    -0.12681037493434544 + x3)^2) + x51 * ((-0.36240169855712956 + x1)^2 + (
    -0.04857443538763084 + x2)^2 + (-0.9860358791315034 + x3)^2) + x52 * ((
    -0.08195695254594337 + x1)^2 + (-0.18885105382104828 + x2)^2 + (
    -0.8027553727917437 + x3)^2) + x53 * ((-0.3963885195949204 + x1)^2 + (
    -0.3241632475929923 + x2)^2 + (-0.853275456923333 + x3)^2) + x54 * ((
    -0.5908438916261783 + x1)^2 + (-0.7950112790507812 + x2)^2 + (
    -0.32740880277441486 + x3)^2) + x55 * ((-0.8432432133553496 + x1)^2 + (
    -0.05282798148772461 + x2)^2 + (-0.45546519649801565 + x3)^2) + x56 * ((
    -0.42236971119841793 + x1)^2 + (-0.8947757440038225 + x2)^2 + (
    -0.4695709175424789 + x3)^2) + x57 * ((-0.8247942497549123 + x1)^2 + (
    -0.5014330359845784 + x2)^2 + (-0.7470113565382576 + x3)^2) + x58 * ((
    -0.48834453204993566 + x1)^2 + (-0.5215169837629428 + x2)^2 + (
    -0.6466473117603931 + x3)^2) + x59 * ((-0.5539921888753628 + x1)^2 + (
    -0.3015288028980093 + x2)^2 + (-0.7614340990080889 + x3)^2) + x60 * ((
    -0.13405913842449635 + x1)^2 + (-0.010282913789367076 + x2)^2 + (
    -0.47341317441006114 + x3)^2) + x61 * ((-0.4844169330601604 + x1)^2 + (
    -0.6930522779489291 + x2)^2 + (-0.7621495736478611 + x3)^2) + x62 * ((
    -0.7740308764454359 + x1)^2 + (-0.03729224901817285 + x2)^2 + (
    -0.060792495607531416 + x3)^2) + x63 * ((-0.43017611384019483 + x1)^2 + (
    -0.7275353979377646 + x2)^2 + (-0.11228956220406072 + x3)^2) + x64 * ((
    -0.730207310114505 + x1)^2 + (-0.9753557541190604 + x2)^2 + (
    -0.046876482359277216 + x3)^2) + x65 * ((-0.24388528239994156 + x1)^2 + (
    -0.8253598309798788 + x2)^2 + (-0.5495236414774879 + x3)^2) + x66 * ((
    -0.9122699869151167 + x1)^2 + (-0.31915757121431776 + x2)^2 + (
    -0.7372813637720362 + x3)^2) + x67 * ((-0.7238338524735144 + x1)^2 + (
    -0.05489659548168713 + x2)^2 + (-0.3744471629501799 + x3)^2) + x68 * ((
    -0.7639916865325218 + x1)^2 + (-0.37213335483670207 + x2)^2 + (
    -0.15924084004650396 + x3)^2) + x69 * ((-0.02038252676112806 + x1)^2 + (
    -0.6941311922925457 + x2)^2 + (-0.8152379226615076 + x3)^2) + x70 * ((
    -0.2834980659872919 + x1)^2 + (-0.098062561074025 + x2)^2 + (
    -0.09504713494440098 + x3)^2) + x71 * ((-0.5777263686540078 + x1)^2 + (
    -0.6553186629601886 + x2)^2 + (-0.10852708184066717 + x3)^2) + x72 * ((
    -0.0504906548870141 + x1)^2 + (-0.01801577482327177 + x2)^2 + (
    -0.7073392283503382 + x3)^2) + x73 * ((-0.7320511478522743 + x1)^2 + (
    -0.2419803614589029 + x2)^2 + (-0.6026607994765517 + x3)^2) + x74 * ((
    -0.9681953946844297 + x1)^2 + (-0.6220011693963317 + x2)^2 + (
    -0.9192154721620333 + x3)^2) + x75 * ((-0.7449798611870608 + x1)^2 + (
    -0.618779704147399 + x2)^2 + (-0.9908068620931784 + x3)^2) + x76 * ((
    -0.04656000736284627 + x1)^2 + (-0.7622587439775123 + x2)^2 + (
    -0.5444825165905486 + x3)^2) + x77 * ((-0.5304149849270671 + x1)^2 + (
    -0.7853544629150807 + x2)^2 + (-0.6650413115686411 + x3)^2) + x78 * ((
    -0.4316006167167099 + x1)^2 + (-0.9564410998503826 + x2)^2 + (
    -0.2754654244349003 + x3)^2) + x79 * ((-0.8192654145647627 + x1)^2 + (
    -0.3449960317441789 + x2)^2 + (-0.4639588553586419 + x3)^2) + x80 * ((
    -0.4202896905773047 + x1)^2 + (-0.4903100277526028 + x2)^2 + (
    -0.4508730801904217 + x3)^2) + x81 * ((-0.7839805319619787 + x1)^2 + (
    -0.07624343650513432 + x2)^2 + (-0.010490453443519732 + x3)^2) + x82 * ((
    -0.716640229430628 + x1)^2 + (-0.3191301181101275 + x2)^2 + (
    -0.24084475450576515 + x3)^2) + x83 * ((-0.48973960110221293 + x1)^2 + (
    -0.19400622702592318 + x2)^2 + (-0.5586480098172433 + x3)^2) + x84 * ((
    -0.25765000251075176 + x1)^2 + (-0.3991120430135222 + x2)^2 + (
    -0.624261591485904 + x3)^2) + x85 * ((-0.2102936857169334 + x1)^2 + (
    -0.6048029406652995 + x2)^2 + (-0.527925854621275 + x3)^2) + x86 * ((
    -0.1418787545905994 + x1)^2 + (-0.0774930390726144 + x2)^2 + (
    -0.0249724785862947 + x3)^2) + x87 * ((-0.034877726496859385 + x1)^2 + (
    -0.6319560857501643 + x2)^2 + (-0.7242772960087813 + x3)^2) + x88 * ((
    -0.9433129608773202 + x1)^2 + (-0.3736070884724113 + x2)^2 + (
    -0.92947567244536 + x3)^2) + x89 * ((-0.19723347065034202 + x1)^2 + (
    -0.5757655498584185 + x2)^2 + (-0.4442676556771823 + x3)^2) + x90 * ((
    -0.08053094633012514 + x1)^2 + (-0.49597290071491906 + x2)^2 + (
    -0.68982692206069 + x3)^2) + x91 * ((-0.7371912517400753 + x1)^2 + (
    -0.4111907705168256 + x2)^2 + (-0.44596226596462496 + x3)^2) + x92 * ((
    -0.46785953968803606 + x1)^2 + (-0.45341953773271215 + x2)^2 + (
    -0.7283106962836612 + x3)^2) + x93 * ((-0.8261694191695272 + x1)^2 + (
    -0.41472831889096884 + x2)^2 + (-0.9106938093148554 + x3)^2) + x94 * ((
    -0.44683645298814745 + x1)^2 + (-0.6996104890042156 + x2)^2 + (
    -0.066679930798903 + x3)^2) + x95 * ((-0.9366613572848865 + x1)^2 + (
    -0.42199403399468605 + x2)^2 + (-0.10350991187036918 + x3)^2) + x96 * ((
    -0.9730815838375089 + x1)^2 + (-0.6831147433040942 + x2)^2 + (
    -0.09074649263643031 + x3)^2) + x97 * ((-0.19241596788927118 + x1)^2 + (
    -0.47076401046441096 + x2)^2 + (-0.15843960550460512 + x3)^2) + x98 * ((
    -0.04999694084986828 + x1)^2 + (-0.43552364112098474 + x2)^2 + (
    -0.317689183487498 + x3)^2) + x99 * ((-0.7805202520309815 + x1)^2 + (
    -0.07439424045077114 + x2)^2 + (-0.11817215106111634 + x3)^2) + x100 * ((
    -0.35732353691638374 + x1)^2 + (-0.729905338698986 + x2)^2 + (
    -0.5100765758088116 + x3)^2) + x101 * ((-0.4780015271753969 + x1)^2 + (
    -0.192158490869756 + x2)^2 + (-0.01693000121269117 + x3)^2) + x102 * ((
    -0.781318913473494 + x1)^2 + (-0.25445440893640614 + x2)^2 + (
    -0.7752207968553286 + x3)^2) + x103 * ((-0.8343131584256498 + x1)^2 + (
    -0.2904065598498118 + x2)^2 + (-0.44278123600229036 + x3)^2) + x104 * ((
    -0.9639849716170581 + x1)^2 + (-0.15550942759340902 + x2)^2 + (
    -0.12539074143986528 + x3)^2) + x105 * ((-0.9221783343065362 + x1)^2 + (
    -0.8425574910926684 + x2)^2 + (-0.9716597371554934 + x3)^2) + x106 * ((
    -0.46470646895314527 + x1)^2 + (-0.43245231227619974 + x2)^2 + (
    -0.5802228635322391 + x3)^2) + x107 * ((-0.271134180722319 + x1)^2 + (
    -0.36061003024560156 + x2)^2 + (-0.1471398510067108 + x3)^2) + x108 * ((
    -0.11520302100676727 + x1)^2 + (-0.663912716794071 + x2)^2 + (
    -0.5527561125387709 + x3)^2) + x109 * ((-0.6162912656168867 + x1)^2 + (
    -0.5377119910240235 + x2)^2 + (-0.5807063907096474 + x3)^2) + x110 * ((
    -0.37145013174802566 + x1)^2 + (-0.5345645332516239 + x2)^2 + (
    -0.510699989525291 + x3)^2) + x111 * ((-0.03393556960060573 + x1)^2 + (
    -0.0156666184663532 + x2)^2 + (-0.07624209854333597 + x3)^2) + x112 * ((
    -0.8270963072435799 + x1)^2 + (-0.7741889426436234 + x2)^2 + (
    -0.11760611435305912 + x3)^2) + x113 * ((-0.18357821030782528 + x1)^2 + (
    -0.9734815530389282 + x2)^2 + (-0.08722449406089927 + x3)^2) + x114 * ((
    -0.4006392450848354 + x1)^2 + (-0.9419621185211043 + x2)^2 + (
    -0.7043081992282076 + x3)^2) + x115 * ((-0.22556650178941084 + x1)^2 + (
    -0.6034598644180125 + x2)^2 + (-0.1696902160808953 + x3)^2) + x116 * ((
    -0.9825403553111026 + x1)^2 + (-0.35577808053830695 + x2)^2 + (
    -0.28203592489557505 + x3)^2) + x117 * ((-0.19474142388607596 + x1)^2 + (
    -0.8131107522988229 + x2)^2 + (-0.20189429638588874 + x3)^2) + x118 * ((
    -0.8965750056171701 + x1)^2 + (-0.681955506000223 + x2)^2 + (
    -0.1398601385146755 + x3)^2) + x119 * ((-0.6906419235208477 + x1)^2 + (
    -0.24426493995237364 + x2)^2 + (-0.47872107051865875 + x3)^2) + x120 * ((
    -0.4832440968672467 + x1)^2 + (-0.6969985518711306 + x2)^2 + (
    -0.9470893906754926 + x3)^2) + x121 * ((-0.10622876499073441 + x1)^2 + (
    -0.693441063669681 + x2)^2 + (-0.1652812026058289 + x3)^2) + x122 * ((
    -0.9897886682814803 + x1)^2 + (-0.599511795785779 + x2)^2 + (
    -0.8125758496836358 + x3)^2) + x123 * ((-0.8169198572273942 + x1)^2 + (
    -0.008813750148081168 + x2)^2 + (-0.26018856120218925 + x3)^2) + x124 * ((
    -0.7549634171088901 + x1)^2 + (-0.43078690581257384 + x2)^2 + (
    -0.7749777657255487 + x3)^2) + x125 * ((-0.49182605753605824 + x1)^2 + (
    -0.28246579300389185 + x2)^2 + (-0.5070642636215076 + x3)^2) + x126 * ((
    -0.5042598753977806 + x1)^2 + (-0.0022250490805308942 + x2)^2 + (
    -0.391688155748926 + x3)^2) + x127 * ((-0.876071155170606 + x1)^2 + (
    -0.5508423923993612 + x2)^2 + (-0.824559592123001 + x3)^2) + x128 * ((
    -0.11165887263159624 + x1)^2 + (-0.7085491226119169 + x2)^2 + (
    -0.8775234759634866 + x3)^2) + x129 * ((-0.06305425963412226 + x1)^2 + (
    -0.1692915986404735 + x2)^2 + (-0.1546726877920308 + x3)^2) + x130 * ((
    -0.9499620149510364 + x1)^2 + (-0.20812541109619742 + x2)^2 + (
    -0.34754918900968657 + x3)^2) + x131 * ((-0.5460977024824913 + x1)^2 + (
    -0.9637992932230987 + x2)^2 + (-0.6995797299071689 + x3)^2) + x132 * ((
    -0.25491459381765613 + x1)^2 + (-0.8070965237021143 + x2)^2 + (
    -0.8356296626230745 + x3)^2) + x133 * ((-0.1702497329876329 + x1)^2 + (
    -0.4046122894687497 + x2)^2 + (-0.983146211120638 + x3)^2) + x134 * ((
    -0.38494123369736066 + x1)^2 + (-0.0904492373848188 + x2)^2 + (
    -0.06525088803516699 + x3)^2) + x135 * ((-0.1342401664666969 + x1)^2 + (
    -0.6663416890145257 + x2)^2 + (-0.7438434658481744 + x3)^2) + x136 * ((
    -0.7253450049079363 + x1)^2 + (-0.4870006307057251 + x2)^2 + (
    -0.8740872298975312 + x3)^2) + x137 * ((-0.7328325422437689 + x1)^2 + (
    -0.8575177732697433 + x2)^2 + (-0.4765071623659649 + x3)^2) + x138 * ((
    -0.6783555500591814 + x1)^2 + (-0.9452264908498691 + x2)^2 + (
    -0.4009905455748076 + x3)^2) + x139 * ((-0.9645465696225488 + x1)^2 + (
    -0.8988121792155044 + x2)^2 + (-0.8693701035695635 + x3)^2) + x140 * ((
    -0.034109539793666044 + x1)^2 + (-0.7341228944483525 + x2)^2 + (
    -0.6711095074457485 + x3)^2) + x141 * ((-0.9925652875910469 + x1)^2 + (
    -0.9767372917892282 + x2)^2 + (-0.35119270893145604 + x3)^2) + x142 * ((
    -0.4335634471581603 + x1)^2 + (-0.9773387547384761 + x2)^2 + (
    -0.8638040489407179 + x3)^2) + x143 * ((-0.8298565888279448 + x1)^2 + (
    -0.26942544674381563 + x2)^2 + (-0.07762497635314547 + x3)^2) + x144 * ((
    -0.7541529640858855 + x1)^2 + (-0.5901288469645308 + x2)^2 + (
    -0.8131521214901242 + x3)^2) + x145 * ((-0.6175218139719055 + x1)^2 + (
    -0.9185690552704726 + x2)^2 + (-0.9584989171844233 + x3)^2) + x146 * ((
    -0.5426908933870604 + x1)^2 + (-0.9276924059348457 + x2)^2 + (
    -0.5088628864009217 + x3)^2) + x147 * ((-0.36674157946961816 + x1)^2 + (
    -0.9494397054589957 + x2)^2 + (-0.502673714811412 + x3)^2) + x148 * ((
    -0.7718452911924847 + x1)^2 + (-0.08932990709963073 + x2)^2 + (
    -0.8114836680773437 + x3)^2) + x149 * ((-0.626463542469553 + x1)^2 + (
    -0.5374333330491173 + x2)^2 + (-0.12893104003458555 + x3)^2) + x150 * ((
    -0.7425349118488094 + x1)^2 + (-0.1255983096608143 + x2)^2 + (
    -0.35251120977084616 + x3)^2) + x151 * ((-0.5763919417102015 + x1)^2 + (
    -0.8668165395935221 + x2)^2 + (-0.18418689718597303 + x3)^2) + x152 * ((
    -0.0842638329353742 + x1)^2 + (-0.22780453935881773 + x2)^2 + (
    -0.06751612916008864 + x3)^2) + x153 * ((-0.4752871340736414 + x1)^2 + (
    -0.569148110715716 + x2)^2 + (-0.825451649082575 + x3)^2) + x154 * ((
    -0.9331572175670021 + x1)^2 + (-0.13944078138289107 + x2)^2 + (
    -0.4974317423493232 + x3)^2) + x155 * ((-0.5801698170306864 + x1)^2 + (
    -0.09023678868466112 + x2)^2 + (-0.5350628309500659 + x3)^2) + x156 * ((
    -0.5007559134871579 + x1)^2 + (-0.9361289066528181 + x2)^2 + (
    -0.4876551928604236 + x3)^2) + x157 * ((-0.3331382694999312 + x1)^2 + (
    -0.8003640425360357 + x2)^2 + (-0.4456772103718464 + x3)^2) + x158 * ((
    -0.580897968874648 + x1)^2 + (-0.6875204337094218 + x2)^2 + (
    -0.23853575215395162 + x3)^2) + x159 * ((-0.26259058062087826 + x1)^2 + (
    -0.31607289532856375 + x2)^2 + (-0.08079831830446549 + x3)^2) + x160 * ((
    -0.8749384932019274 + x1)^2 + (-0.5978601364266924 + x2)^2 + (
    -0.2709722104839264 + x3)^2) + x161 * ((-0.3380164843711445 + x1)^2 + (
    -0.9620957935062617 + x2)^2 + (-0.5318755277541398 + x3)^2) + x162 * ((
    -0.19915462374899218 + x1)^2 + (-0.16745416979147543 + x2)^2 + (
    -0.8177983201819474 + x3)^2) + x163 * ((-0.8422569529306239 + x1)^2 + (
    -0.9503230877966571 + x2)^2 + (-0.27758371082708055 + x3)^2) + x164 * ((
    -0.44963143674100436 + x1)^2 + (-0.6298100336125453 + x2)^2 + (
    -0.6473187227829037 + x3)^2) + x165 * ((-0.5323794396752508 + x1)^2 + (
    -0.29195939691071726 + x2)^2 + (-0.3777205926486479 + x3)^2) + x166 * ((
    -0.08774633426227729 + x1)^2 + (-0.5103291813715215 + x2)^2 + (
    -0.21197701339206598 + x3)^2) + x167 * ((-0.1886462563105995 + x1)^2 + (
    -0.7166154370441229 + x2)^2 + (-0.8967828307834859 + x3)^2) + x168 * ((
    -0.9135151722699717 + x1)^2 + (-0.24518247233237755 + x2)^2 + (
    -0.22467871490663316 + x3)^2) + x169 * ((-0.4002656679601796 + x1)^2 + (
    -0.8075378016015988 + x2)^2 + (-0.9589722648623482 + x3)^2) + x170 * ((
    -0.350804850761565 + x1)^2 + (-0.2001510201677693 + x2)^2 + (
    -0.3847312652361822 + x3)^2) + x171 * ((-0.7092459191225206 + x1)^2 + (
    -0.3653825052791586 + x2)^2 + (-0.4100011123148736 + x3)^2) + x172 * ((
    -0.08924822462276016 + x1)^2 + (-0.2350022965537154 + x2)^2 + (
    -0.4724131123343983 + x3)^2) + x173 * ((-0.678878546266445 + x1)^2 + (
    -0.0024223731399833914 + x2)^2 + (-0.18719967650857738 + x3)^2) + x174 * ((
    -0.8949831170437572 + x1)^2 + (-0.6742418627601845 + x2)^2 + (
    -0.9659226960334533 + x3)^2) + x175 * ((-0.461298010620385 + x1)^2 + (
    -0.3515384955734874 + x2)^2 + (-0.1589819355604557 + x3)^2) + x176 * ((
    -0.4742180560695449 + x1)^2 + (-0.31128812059338673 + x2)^2 + (
    -0.16193285694593962 + x3)^2) + x177 * ((-0.9057373068507129 + x1)^2 + (
    -0.07169041620954708 + x2)^2 + (-0.24658295842854583 + x3)^2) + x178 * ((
    -0.042416932822683995 + x1)^2 + (-0.11901530250324566 + x2)^2 + (
    -0.8719607562434413 + x3)^2) + x179 * ((-0.3509796417311175 + x1)^2 + (
    -0.7261268633422199 + x2)^2 + (-0.37378698482516615 + x3)^2) + x180 * ((
    -0.48178722792919537 + x1)^2 + (-0.12507968740842412 + x2)^2 + (
    -0.1533291787002754 + x3)^2) + x181 * ((-0.690187452865442 + x1)^2 + (
    -0.06414157686780875 + x2)^2 + (-0.9184182999081079 + x3)^2) + x182 * ((
    -0.7601598471825683 + x1)^2 + (-0.39014455511239565 + x2)^2 + (
    -0.06643024228030481 + x3)^2) + x183 * ((-0.7648317386640142 + x1)^2 + (
    -0.8401096588730549 + x2)^2 + (-0.6476437320133126 + x3)^2) + x184 * ((
    -0.9157717582294775 + x1)^2 + (-0.7156353049895615 + x2)^2 + (
    -0.1779714150010886 + x3)^2) + x185 * ((-0.2914662714138311 + x1)^2 + (
    -0.8979506548155362 + x2)^2 + (-0.28370242601709506 + x3)^2) + x186 * ((
    -0.41299200861407237 + x1)^2 + (-0.5731791645656842 + x2)^2 + (
    -0.9880744442012739 + x3)^2) + x187 * ((-0.2773152437673355 + x1)^2 + (
    -0.5869730199299126 + x2)^2 + (-0.6503070600258439 + x3)^2) + x188 * ((
    -0.7054867170779409 + x1)^2 + (-0.38605289741051385 + x2)^2 + (
    -0.18161609983908555 + x3)^2) + x189 * ((-0.9858526028351562 + x1)^2 + (
    -0.11659661065988192 + x2)^2 + (-0.6328911420439645 + x3)^2) + x190 * ((
    -0.008586957495201109 + x1)^2 + (-0.6828361406835076 + x2)^2 + (
    -0.9383137951511125 + x3)^2) + x191 * ((-0.5535058192578067 + x1)^2 + (
    -0.007867554292018242 + x2)^2 + (-0.3880343478492315 + x3)^2) + x192 * ((
    -0.2998574271558311 + x1)^2 + (-0.5685060268070001 + x2)^2 + (
    -0.8612909410674978 + x3)^2) + x193 * ((-0.7279300554494663 + x1)^2 + (
    -0.8665137249506871 + x2)^2 + (-0.2425661607644104 + x3)^2) + x194 * ((
    -0.3674243260814667 + x1)^2 + (-0.6726025203611717 + x2)^2 + (
    -0.3019444385645804 + x3)^2) + x195 * ((-0.561221458088611 + x1)^2 + (
    -0.1252412923674795 + x2)^2 + (-0.7626531785557333 + x3)^2) + x196 * ((
    -0.7526982106932172 + x1)^2 + (-0.09811091554051077 + x2)^2 + (
    -0.8331863589378469 + x3)^2) + x197 * ((-0.7212209268256802 + x1)^2 + (
    -0.3347884192733733 + x2)^2 + (-0.34081278172854135 + x3)^2) + x198 * ((
    -0.38492684008888933 + x1)^2 + (-0.053573445724505286 + x2)^2 + (
    -0.45746291996264776 + x3)^2) + x199 * ((-0.17867755090980397 + x1)^2 + (
    -0.846403915886413 + x2)^2 + (-0.15238735379254842 + x3)^2) + x200 * ((
    -0.7342435428310872 + x1)^2 + (-0.35254162287667923 + x2)^2 + (
    -0.3649777944564463 + x3)^2) + x201 * ((-0.21121661378120005 + x1)^2 + (
    -0.8764333024482275 + x2)^2 + (-0.6905270652669678 + x3)^2) + x202 * ((
    -0.7454607699149387 + x1)^2 + (-0.5243311461762572 + x2)^2 + (
    -0.46847369630081737 + x3)^2) + x203 * ((-0.5777724524082414 + x1)^2 + (
    -0.9389607386881164 + x2)^2 + (-0.9490991772196733 + x3)^2) + x204 * ((
    -0.6953770563282883 + x1)^2 + (-0.30766167182637194 + x2)^2 + (
    -0.9947613161831723 + x3)^2) + x205 * ((-0.07322511345630467 + x1)^2 + (
    -0.11542967998046938 + x2)^2 + (-0.5551153181290245 + x3)^2) + x206 * ((
    -0.823466601595051 + x1)^2 + (-0.4761579425686089 + x2)^2 + (
    -0.7645792742638973 + x3)^2) + x207 * ((-0.3065558046367579 + x1)^2 + (
    -0.6489835149493414 + x2)^2 + (-0.24712630191036555 + x3)^2) + x208 * ((
    -0.42587171854139994 + x1)^2 + (-0.9609489628414893 + x2)^2 + (
    -0.34607854810703564 + x3)^2) + x209 * ((-0.22514530689258294 + x1)^2 + (
    -0.29572551314242157 + x2)^2 + (-0.04494292345454676 + x3)^2) + x210 * ((
    -0.733484242355372 + x1)^2 + (-0.7428655248132915 + x2)^2 + (
    -0.7982295536152093 + x3)^2) + x211 * ((-0.5007178891993553 + x1)^2 + (
    -0.18337867834916188 + x2)^2 + (-0.2867876649071047 + x3)^2) + x212 * ((
    -0.9062122087196477 + x1)^2 + (-0.5780300635857895 + x2)^2 + (
    -0.1538197962604425 + x3)^2) + x213 * ((-0.7863514275791065 + x1)^2 + (
    -0.047106972476383846 + x2)^2 + (-0.9442358046581198 + x3)^2) + x214 * ((
    -0.49327445076665244 + x1)^2 + (-0.7635057400072934 + x2)^2 + (
    -0.08977894732398484 + x3)^2) + x215 * ((-0.5885030216777958 + x1)^2 + (
    -0.31457737395890006 + x2)^2 + (-0.06769170169106442 + x3)^2) + x216 * ((
    -0.2624396116681811 + x1)^2 + (-0.8735241081831786 + x2)^2 + (
    -0.17009678211994406 + x3)^2) + x217 * ((-0.8745938616823902 + x1)^2 + (
    -0.6895313121315244 + x2)^2 + (-0.3798558733668982 + x3)^2) + x218 * ((
    -0.19470988963139768 + x1)^2 + (-0.7061159026040712 + x2)^2 + (
    -0.09540851729033883 + x3)^2) + x219 * ((-0.07281526695083318 + x1)^2 + (
    -0.5313755426899924 + x2)^2 + (-0.3281258830967686 + x3)^2) + x220 * ((
    -0.0050140137596184076 + x1)^2 + (-0.0571436713320036 + x2)^2 + (
    -0.7424653869787131 + x3)^2) + x221 * ((-0.7365729576101151 + x1)^2 + (
    -0.016411359906266965 + x2)^2 + (-0.6018392757598213 + x3)^2) + x222 * ((
    -0.9710402789360123 + x1)^2 + (-0.057905237168721646 + x2)^2 + (
    -0.1016804201191902 + x3)^2) + x223 * ((-0.886784750676047 + x1)^2 + (
    -0.5909509982566028 + x2)^2 + (-0.08207033376025652 + x3)^2) + x224 * ((
    -0.9456537388004167 + x1)^2 + (-0.10430429872917613 + x2)^2 + (
    -0.47980776700636785 + x3)^2) + x225 * ((-0.01703842580768944 + x1)^2 + (
    -0.3771031988756788 + x2)^2 + (-0.9126173043337085 + x3)^2) + x226 * ((
    -0.7473088625241339 + x1)^2 + (-0.1992639563893337 + x2)^2 + (
    -0.27259207689859966 + x3)^2) + x227 * ((-0.9866924203074965 + x1)^2 + (
    -0.02211001009510316 + x2)^2 + (-0.710715645336501 + x3)^2) + x228 * ((
    -0.22231763494264423 + x1)^2 + (-0.7222747879572179 + x2)^2 + (
    -0.48387331778539744 + x3)^2) + x229 * ((-0.5217371859514337 + x1)^2 + (
    -0.8145029375864773 + x2)^2 + (-0.5971133086187703 + x3)^2) + x230 * ((
    -0.16123590082773454 + x1)^2 + (-0.7338632807820815 + x2)^2 + (
    -0.9775931853783937 + x3)^2) + x231 * ((-0.15216767027450806 + x1)^2 + (
    -0.8194769982782 + x2)^2 + (-0.3798283273565146 + x3)^2) + x232 * ((
    -0.755130243908553 + x1)^2 + (-0.964046166903329 + x2)^2 + (
    -0.37287898957618804 + x3)^2) + x233 * ((-0.4515557009816349 + x1)^2 + (
    -0.5888415389238447 + x2)^2 + (-0.6268802444924639 + x3)^2) + x234 * ((
    -0.8339407401569209 + x1)^2 + (-0.3941136302934939 + x2)^2 + (
    -0.0011773452039460786 + x3)^2) + x235 * ((-0.03523664509745583 + x1)^2 + (
    -0.9282465013011052 + x2)^2 + (-0.10432387873774907 + x3)^2) + x236 * ((
    -0.5824740927361365 + x1)^2 + (-0.2830428234231407 + x2)^2 + (
    -0.2929978420181991 + x3)^2) + x237 * ((-0.3457319486786484 + x1)^2 + (
    -0.6369253498892743 + x2)^2 + (-0.35691844570607956 + x3)^2) + x238 * ((
    -0.42088037600595574 + x1)^2 + (-0.6312418989251471 + x2)^2 + (
    -0.8287246238964575 + x3)^2) + x239 * ((-0.021979693073987727 + x1)^2 + (
    -0.2773405353290628 + x2)^2 + (-0.029133052826545436 + x3)^2) + x240 * ((
    -0.5081863887708018 + x1)^2 + (-0.20601907370036388 + x2)^2 + (
    -0.9821208081223113 + x3)^2) + x241 * ((-0.0019048004425398224 + x1)^2 + (
    -0.9834147377960726 + x2)^2 + (-0.2723044658709237 + x3)^2) + x242 * ((
    -0.5500730095581713 + x1)^2 + (-0.9929315189942348 + x2)^2 + (
    -0.8008514847320088 + x3)^2) + x243 * ((-0.42236107077823737 + x1)^2 + (
    -0.8886238887911541 + x2)^2 + (-0.8222569499938951 + x3)^2) + x244 * ((
    -0.0672943459062394 + x1)^2 + (-0.2827538856518119 + x2)^2 + (
    -0.13430545927864412 + x3)^2) + x245 * ((-0.5677325188553733 + x1)^2 + (
    -0.938532426013799 + x2)^2 + (-0.7611389677471435 + x3)^2) + x246 * ((
    -0.8629019843437029 + x1)^2 + (-0.8826021988159478 + x2)^2 + (
    -0.7188638964511778 + x3)^2) + x247 * ((-0.5507464371836962 + x1)^2 + (
    -0.7611165241588504 + x2)^2 + (-0.02910037665638643 + x3)^2) + x248 * ((
    -0.34299191582875777 + x1)^2 + (-0.524901527819975 + x2)^2 + (
    -0.5781388484542243 + x3)^2) + x249 * ((-0.35151500287062976 + x1)^2 + (
    -0.21136430913659288 + x2)^2 + (-0.08857984066212443 + x3)^2) + x250 * ((
    -0.7675403347878336 + x1)^2 + (-0.532832695685235 + x2)^2 + (
    -0.2503117333896512 + x3)^2) + x251 * ((-0.23097591211896384 + x1)^2 + (
    -0.15477203487438085 + x2)^2 + (-0.5054800430556513 + x3)^2) + x252 * ((
    -0.7881833845877819 + x1)^2 + (-0.2758754119705751 + x2)^2 + (
    -0.9382258338204086 + x3)^2) + x253 * ((-0.9466477036942484 + x1)^2 + (
    -0.06948523439716237 + x2)^2 + (-0.7146827511615796 + x3)^2) + x254 * ((
    -0.5029417013633463 + x1)^2 + (-0.4785691085999849 + x2)^2 + (
    -0.6440855384208175 + x3)^2) + x255 * ((-0.5303135807201502 + x1)^2 + (
    -0.9039824414704006 + x2)^2 + (-0.33970470843348766 + x3)^2) + x256 * ((
    -0.3002120204313121 + x1)^2 + (-0.8293923954271605 + x2)^2 + (
    -0.09736075716511139 + x3)^2) + x257 * ((-0.30009287477399993 + x1)^2 + (
    -0.8977331200619989 + x2)^2 + (-0.6790360118322567 + x3)^2) + x258 * ((
    -0.949222817147212 + x1)^2 + (-0.4475514843804891 + x2)^2 + (
    -0.38135879431065867 + x3)^2) + x259 * ((-0.2064338949319181 + x1)^2 + (
    -0.2471618264138381 + x2)^2 + (-0.33404126801805556 + x3)^2) + x260 * ((
    -0.9469532157846159 + x1)^2 + (-0.12979939471251356 + x2)^2 + (
    -0.6308532308364203 + x3)^2) + x261 * ((-0.8160024772328773 + x1)^2 + (
    -0.8192673081264756 + x2)^2 + (-0.828617395442529 + x3)^2) + x262 * ((
    -0.043698145130302235 + x1)^2 + (-0.35823212196091736 + x2)^2 + (
    -0.6536017967379447 + x3)^2) + x263 * ((-0.31599796165138205 + x1)^2 + (
    -0.14269139738795444 + x2)^2 + (-0.5083854452577903 + x3)^2) + x264 * ((
    -0.1849721541921785 + x1)^2 + (-0.9379494054807923 + x2)^2 + (
    -0.750436849143862 + x3)^2) + x265 * ((-0.2216708088282653 + x1)^2 + (
    -0.23053899815258394 + x2)^2 + (-0.18897253793934143 + x3)^2) + x266 * ((
    -0.35548760077164 + x1)^2 + (-0.2106073810351573 + x2)^2 + (
    -0.8030904658404747 + x3)^2) + x267 * ((-0.7046242974214645 + x1)^2 + (
    -0.9747362717516234 + x2)^2 + (-0.8986311370033265 + x3)^2) + x268 * ((
    -0.6930115258414592 + x1)^2 + (-0.25226679460293766 + x2)^2 + (
    -0.2620829240380018 + x3)^2) + x269 * ((-0.5416746943288492 + x1)^2 + (
    -0.3587968851453698 + x2)^2 + (-0.8014083818825035 + x3)^2) + x270 * ((
    -0.709926799469957 + x1)^2 + (-0.42600195906405547 + x2)^2 + (
    -0.2918180254572945 + x3)^2) + x271 * ((-0.3511232970881478 + x1)^2 + (
    -0.7757451672244947 + x2)^2 + (-0.7859380648395401 + x3)^2) + x272 * ((
    -0.8803653019341091 + x1)^2 + (-0.6658465100092489 + x2)^2 + (
    -0.5112371462700493 + x3)^2) + x273 * ((-0.17144800814870276 + x1)^2 + (
    -0.4122257700328378 + x2)^2 + (-0.8076682711989561 + x3)^2) + x274 * ((
    -0.717380833423112 + x1)^2 + (-0.17998680267335054 + x2)^2 + (
    -0.9060156443877393 + x3)^2) + x275 * ((-0.5878000971753468 + x1)^2 + (
    -0.18065525183423758 + x2)^2 + (-0.15538360399442397 + x3)^2) + x276 * ((
    -0.8682299280341067 + x1)^2 + (-0.16346717895652563 + x2)^2 + (
    -0.4336582517475457 + x3)^2) + x277 * ((-0.3606702369630238 + x1)^2 + (
    -0.731242129687016 + x2)^2 + (-0.12043748947308242 + x3)^2) + x278 * ((
    -0.4815500944964639 + x1)^2 + (-0.6044620193979354 + x2)^2 + (
    -0.8210071600955915 + x3)^2) + x279 * ((-0.11954313893324364 + x1)^2 + (
    -0.1323053978820773 + x2)^2 + (-0.25050555092577165 + x3)^2) + x280 * ((
    -0.08542773014575478 + x1)^2 + (-0.18503314408239213 + x2)^2 + (
    -0.9115102242077784 + x3)^2) + x281 * ((-0.8095044154907116 + x1)^2 + (
    -0.2799202631109189 + x2)^2 + (-0.2880890539271259 + x3)^2) + x282 * ((
    -0.7212219319929314 + x1)^2 + (-0.5984506061652697 + x2)^2 + (
    -0.9365245987942612 + x3)^2) + x283 * ((-0.8994684258109723 + x1)^2 + (
    -0.22641415105010199 + x2)^2 + (-0.6913162899186059 + x3)^2) + x284 * ((
    -0.6581582771778646 + x1)^2 + (-0.197316973616537 + x2)^2 + (
    -0.43619331804872796 + x3)^2) + x285 * ((-0.4739659187865559 + x1)^2 + (
    -0.38646221151733806 + x2)^2 + (-0.10770286986963273 + x3)^2) + x286 * ((
    -0.8723979336469919 + x1)^2 + (-0.32335338168956085 + x2)^2 + (
    -0.5817075590285083 + x3)^2) + x287 * ((-0.061809683762981016 + x1)^2 + (
    -0.5389217377093763 + x2)^2 + (-0.5417597560087298 + x3)^2) + x288 * ((
    -0.07422322033257833 + x1)^2 + (-0.7097672901832104 + x2)^2 + (
    -0.06915026234774257 + x3)^2) + x289 * ((-0.8280486736764958 + x1)^2 + (
    -0.04022416242938687 + x2)^2 + (-0.19882373590113933 + x3)^2) + x290 * ((
    -0.029072146364669926 + x1)^2 + (-0.09653489205822285 + x2)^2 + (
    -0.049536244543501806 + x3)^2) + x291 * ((-0.7881624249773665 + x1)^2 + (
    -0.7566784959062068 + x2)^2 + (-0.3074666055810339 + x3)^2) + x292 * ((
    -0.7152259480390857 + x1)^2 + (-0.640956553515879 + x2)^2 + (
    -0.39814612324127086 + x3)^2) + x293 * ((-0.9043657495395202 + x1)^2 + (
    -0.5252156573640178 + x2)^2 + (-0.8199524482586914 + x3)^2) + x294 * ((
    -0.8601980724291697 + x1)^2 + (-0.31860765736788654 + x2)^2 + (
    -0.9089973811459461 + x3)^2) + x295 * ((-0.2086703107751542 + x1)^2 + (
    -0.006149788315085392 + x2)^2 + (-0.21513361748683668 + x3)^2) + x296 * ((
    -0.7823136762126888 + x1)^2 + (-0.416684189371502 + x2)^2 + (
    -0.4442685591428306 + x3)^2) + x297 * ((-0.7994879189101486 + x1)^2 + (
    -0.5003588036104756 + x2)^2 + (-0.6431108825964064 + x3)^2) + x298 * ((
    -0.2010796579746258 + x1)^2 + (-0.8170704549941877 + x2)^2 + (
    -0.2175952968667264 + x3)^2) + x299 * ((-0.7094682020793405 + x1)^2 + (
    -0.49279977787280593 + x2)^2 + (-0.6972766332766551 + x3)^2) + x300 * ((
    -0.8249820076123356 + x1)^2 + (-0.7551746481371484 + x2)^2 + (
    -0.3076678852974345 + x3)^2) + x301 * ((-0.4431291732786462 + x1)^2 + (
    -0.10790569968568664 + x2)^2 + (-0.8104337482413756 + x3)^2) + x302 * ((
    -0.12547352222190156 + x1)^2 + (-0.30712330696451673 + x2)^2 + (
    -0.6443221501233987 + x3)^2) + x303 * ((-0.43521055817778886 + x1)^2 + (
    -0.11823850858772755 + x2)^2 + (-0.4245893746746593 + x3)^2) + x304 * ((
    -0.1023807175165814 + x1)^2 + (-0.023476062383137597 + x2)^2 + (
    -0.7715459665761015 + x3)^2) + x305 * ((-0.6084243314221985 + x1)^2 + (
    -0.6767723713597806 + x2)^2 + (-0.15277477018392027 + x3)^2) + x306 * ((
    -0.07758513009101076 + x1)^2 + (-0.5193945915946692 + x2)^2 + (
    -0.13605100113112523 + x3)^2) + x307 * ((-0.05076479042333726 + x1)^2 + (
    -0.7472210261556415 + x2)^2 + (-0.6187487644673069 + x3)^2) + x308 * ((
    -0.5774530190962283 + x1)^2 + (-0.4625308284849895 + x2)^2 + (
    -0.8985951405862879 + x3)^2) + x309 * ((-0.41887571010203506 + x1)^2 + (
    -0.04213576565608468 + x2)^2 + (-0.3367107300411496 + x3)^2) + x310 * ((
    -0.5346587692815016 + x1)^2 + (-0.7514755753693055 + x2)^2 + (
    -0.16512273183076165 + x3)^2) + x311 * ((-0.3673579319044816 + x1)^2 + (
    -0.4132537275282224 + x2)^2 + (-0.34757755368510646 + x3)^2) + x312 * ((
    -0.5454982366155314 + x1)^2 + (-0.573439476172685 + x2)^2 + (
    -0.33123862062087006 + x3)^2) + x313 * ((-0.23915554947791118 + x1)^2 + (
    -0.9496426713944737 + x2)^2 + (-0.9047110021009291 + x3)^2) + x314 * ((
    -0.7835998720242816 + x1)^2 + (-0.5409585492652254 + x2)^2 + (
    -0.022604618704512136 + x3)^2) + x315 * ((-0.7447675570789921 + x1)^2 + (
    -0.06306009873408058 + x2)^2 + (-0.32450967602437086 + x3)^2) + x316 * ((
    -0.957050425001801 + x1)^2 + (-0.6908648583160039 + x2)^2 + (
    -0.6977383122594122 + x3)^2) + x317 * ((-0.9643413589347215 + x1)^2 + (
    -0.8038041971590639 + x2)^2 + (-0.30694917237409114 + x3)^2) + x318 * ((
    -0.16688443645138162 + x1)^2 + (-0.5498482774651414 + x2)^2 + (
    -0.7414582280194998 + x3)^2) + x319 * ((-0.2748697607402272 + x1)^2 + (
    -0.6274376652049733 + x2)^2 + (-0.35357014233175543 + x3)^2) + x320 * ((
    -0.5891376195472661 + x1)^2 + (-0.5661076738361366 + x2)^2 + (
    -0.6533215134864436 + x3)^2) + x321 * ((-0.8392486510086273 + x1)^2 + (
    -0.3115496822184768 + x2)^2 + (-0.146703446853646 + x3)^2) + x322 * ((
    -0.3738023028456101 + x1)^2 + (-0.7106592984968659 + x2)^2 + (
    -0.7581637572990693 + x3)^2) + x323 * ((-0.2801730794814168 + x1)^2 + (
    -0.2913280058906009 + x2)^2 + (-0.10015085446802086 + x3)^2) + x324 * ((
    -0.014051212285501768 + x1)^2 + (-0.3394766298985926 + x2)^2 + (
    -0.4278429675896249 + x3)^2) + x325 * ((-0.9378558356981184 + x1)^2 + (
    -0.15127486460420836 + x2)^2 + (-0.7493436444755507 + x3)^2) + x326 * ((
    -0.8297509765027676 + x1)^2 + (-0.08177655040140464 + x2)^2 + (
    -0.4494327397424498 + x3)^2) + x327 * ((-0.11029669990558244 + x1)^2 + (
    -0.582339311840151 + x2)^2 + (-0.06415846876984466 + x3)^2) + x328 * ((
    -0.9768471346651219 + x1)^2 + (-0.39696035406710384 + x2)^2 + (
    -0.23783616802647012 + x3)^2) + x329 * ((-0.3764501911849826 + x1)^2 + (
    -0.786987541945555 + x2)^2 + (-0.2970434016308823 + x3)^2) + x330 * ((
    -0.05618205629013939 + x1)^2 + (-0.4085438120067576 + x2)^2 + (
    -0.5645644728609109 + x3)^2) + x331 * ((-0.6746539089984576 + x1)^2 + (
    -0.8329192222789586 + x2)^2 + (-0.8171355492822672 + x3)^2) + x332 * ((
    -0.929134925271013 + x1)^2 + (-0.48607691575718226 + x2)^2 + (
    -0.14496601171482326 + x3)^2) + x333 * ((-0.2888049631111739 + x1)^2 + (
    -0.45169995457478385 + x2)^2 + (-0.7415931477217647 + x3)^2) + x334 * ((
    -0.8314270362626708 + x1)^2 + (-0.09391123252252986 + x2)^2 + (
    -0.6669146426368324 + x3)^2) + x335 * ((-0.5652735801231673 + x1)^2 + (
    -0.9329767078391193 + x2)^2 + (-0.9484705315852879 + x3)^2) + x336 * ((
    -0.3380979256818256 + x1)^2 + (-0.23035046064976195 + x2)^2 + (
    -0.5278605812355041 + x3)^2) + x337 * ((-0.8184575612577757 + x1)^2 + (
    -0.9258797310665887 + x2)^2 + (-0.2046467253589157 + x3)^2) + x338 * ((
    -0.40985008510077614 + x1)^2 + (-0.4757792482569193 + x2)^2 + (
    -0.8360188587690305 + x3)^2) + x339 * ((-0.8332701786998654 + x1)^2 + (
    -0.20495368326898378 + x2)^2 + (-0.47164667394744264 + x3)^2) + x340 * ((
    -0.0643880402156024 + x1)^2 + (-0.26358735356819285 + x2)^2 + (
    -0.13167880607810734 + x3)^2) + x341 * ((-0.0025821300592889784 + x1)^2 + (
    -0.9088622869025026 + x2)^2 + (-0.04233625722670664 + x3)^2) + x342 * ((
    -0.5236600684212673 + x1)^2 + (-0.27260080288022603 + x2)^2 + (
    -0.459442267827748 + x3)^2) + x343 * ((-0.7158972098447147 + x1)^2 + (
    -0.9489828100457257 + x2)^2 + (-0.6888872017363918 + x3)^2) + x344 * ((
    -0.7865559366849096 + x1)^2 + (-0.833267039226051 + x2)^2 + (
    -0.5747950642364967 + x3)^2) + x345 * ((-0.34415199178488665 + x1)^2 + (
    -0.18091957070795228 + x2)^2 + (-0.031579899788283905 + x3)^2) + x346 * ((
    -0.14471678962846113 + x1)^2 + (-0.30241060384916396 + x2)^2 + (
    -0.059993959720591294 + x3)^2) + x347 * ((-0.6824739375029841 + x1)^2 + (
    -0.5331181892609036 + x2)^2 + (-0.977166596891582 + x3)^2) + x348 * ((
    -0.20408398166030306 + x1)^2 + (-0.5154572139955655 + x2)^2 + (
    -0.4769277180629534 + x3)^2) + x349 * ((-0.050689484148662145 + x1)^2 + (
    -0.5527672407633779 + x2)^2 + (-0.32111189487270875 + x3)^2) + x350 * ((
    -0.23154418027475898 + x1)^2 + (-0.6700805221954127 + x2)^2 + (
    -0.9666075355371924 + x3)^2) + x351 * ((-0.008868281269836076 + x1)^2 + (
    -0.6338997437715709 + x2)^2 + (-0.26544426895590223 + x3)^2) + x352 * ((
    -0.6596209708459404 + x1)^2 + (-0.40168150668415104 + x2)^2 + (
    -0.4719673790088824 + x3)^2) + x353 * ((-0.11053129063988809 + x1)^2 + (
    -0.16664026665153386 + x2)^2 + (-0.8851714055017869 + x3)^2) + x354 * ((
    -0.5258408747918166 + x1)^2 + (-0.581125730214377 + x2)^2 + (
    -0.9734757162239656 + x3)^2) + x355 * ((-0.37505520940960313 + x1)^2 + (
    -0.8756917740425001 + x2)^2 + (-0.9752391810025125 + x3)^2) + x356 * ((
    -0.47118833747162414 + x1)^2 + (-0.3893334167798458 + x2)^2 + (
    -0.008212794912485166 + x3)^2) + x357 * ((-0.6402127761953015 + x1)^2 + (
    -0.1600123713040228 + x2)^2 + (-0.44094193106669577 + x3)^2) + x358 * ((
    -0.8231471689426597 + x1)^2 + (-0.7509513915820255 + x2)^2 + (
    -0.8921027170624262 + x3)^2) + x359 * ((-0.20030064944641757 + x1)^2 + (
    -0.21962903531540312 + x2)^2 + (-0.5970473550708151 + x3)^2) + x360 * ((
    -0.902808238265977 + x1)^2 + (-0.7562726465509134 + x2)^2 + (
    -0.24813085289058312 + x3)^2) + x361 * ((-0.21843016026229212 + x1)^2 + (
    -0.8059343949692039 + x2)^2 + (-0.3752989990533576 + x3)^2) + x362 * ((
    -0.14794288425068958 + x1)^2 + (-0.31328675165643205 + x2)^2 + (
    -0.8073941583373085 + x3)^2) + x363 * ((-0.5235088791774563 + x1)^2 + (
    -0.04578915338953027 + x2)^2 + (-0.10692118625425784 + x3)^2) + x364 * ((
    -0.5791900847638172 + x1)^2 + (-0.48532053702765365 + x2)^2 + (
    -0.3885259522950011 + x3)^2) + x365 * ((-0.8920363304658884 + x1)^2 + (
    -0.5151000888985628 + x2)^2 + (-0.6346096148059661 + x3)^2) + x366 * ((
    -0.9717009075640338 + x1)^2 + (-0.9907019955601769 + x2)^2 + (
    -0.85505344837673 + x3)^2) + x367 * ((-0.34445995140187446 + x1)^2 + (
    -0.6392373435519673 + x2)^2 + (-0.7819131287560607 + x3)^2) + x368 * ((
    -0.42109376750007577 + x1)^2 + (-0.7284707401745129 + x2)^2 + (
    -0.11077465817504761 + x3)^2) + x369 * ((-0.925635401235069 + x1)^2 + (
    -0.5685890877714631 + x2)^2 + (-0.9462095752137067 + x3)^2) + x370 * ((
    -0.7279111798696564 + x1)^2 + (-0.15487285858439592 + x2)^2 + (
    -0.7608763017869555 + x3)^2) + x371 * ((-0.12654655247031799 + x1)^2 + (
    -0.09026002005416467 + x2)^2 + (-0.8883114041715482 + x3)^2) + x372 * ((
    -0.6585295603176656 + x1)^2 + (-0.5624166650475771 + x2)^2 + (
    -0.5547559478222932 + x3)^2) + x373 * ((-0.24575106742741626 + x1)^2 + (
    -0.3042728268888242 + x2)^2 + (-0.896812031612661 + x3)^2) + x374 * ((
    -0.4606211642264276 + x1)^2 + (-0.5593289076408292 + x2)^2 + (
    -0.9885975772390854 + x3)^2) + x375 * ((-0.7347225956683001 + x1)^2 + (
    -0.5745816301727896 + x2)^2 + (-0.009825540222648477 + x3)^2) + x376 * ((
    -0.9978369871406716 + x1)^2 + (-0.9420017543770447 + x2)^2 + (
    -0.9484212753820023 + x3)^2) + x377 * ((-0.6579730335184849 + x1)^2 + (
    -0.01651993788019801 + x2)^2 + (-0.763022957071984 + x3)^2) + x378 * ((
    -0.9947489651588863 + x1)^2 + (-0.3224606084126759 + x2)^2 + (
    -0.7750668635617214 + x3)^2) + x379 * ((-0.17582348854944607 + x1)^2 + (
    -0.17352822759146402 + x2)^2 + (-0.22743984463314282 + x3)^2) + x380 * ((
    -0.4758203537795964 + x1)^2 + (-0.40834392828261223 + x2)^2 + (
    -0.05261570014523109 + x3)^2) + x381 * ((-0.36204048569723735 + x1)^2 + (
    -0.8641293232884356 + x2)^2 + (-0.1489285988376965 + x3)^2) + x382 * ((
    -0.6008467842262206 + x1)^2 + (-0.9039149091831002 + x2)^2 + (
    -0.36931294088336475 + x3)^2) + x383 * ((-0.030067960172246666 + x1)^2 + (
    -0.48471288146931457 + x2)^2 + (-0.5753432715823008 + x3)^2) + x384 * ((
    -0.1270532869152421 + x1)^2 + (-0.20492488058927516 + x2)^2 + (
    -0.2920819764108209 + x3)^2) + x385 * ((-0.057643356995719985 + x1)^2 + (
    -0.4024951698758521 + x2)^2 + (-0.5345507589362359 + x3)^2) + x386 * ((
    -0.9581878087034774 + x1)^2 + (-0.0800210963738257 + x2)^2 + (
    -0.677382890669299 + x3)^2) + x387 * ((-0.2047868034464274 + x1)^2 + (
    -0.7755295931481812 + x2)^2 + (-0.07132945936635726 + x3)^2) + x388 * ((
    -0.7829343091571344 + x1)^2 + (-0.8105545574565635 + x2)^2 + (
    -0.4991231549422569 + x3)^2) + x389 * ((-0.6258463311430302 + x1)^2 + (
    -0.5496595671750402 + x2)^2 + (-0.19154029772231573 + x3)^2) + x390 * ((
    -0.0272793485028624 + x1)^2 + (-0.011791358057427925 + x2)^2 + (
    -0.8057574736716172 + x3)^2) + x391 * ((-0.5414890284796168 + x1)^2 + (
    -0.945016615830951 + x2)^2 + (-0.8798725595210737 + x3)^2) + x392 * ((
    -0.05119780537656027 + x1)^2 + (-0.5031403231758489 + x2)^2 + (
    -0.11523583178307628 + x3)^2) + x393 * ((-0.27464505675722395 + x1)^2 + (
    -0.05754985857648509 + x2)^2 + (-0.1718986943714379 + x3)^2) + x394 * ((
    -0.563384014973976 + x1)^2 + (-0.4102870005309007 + x2)^2 + (
    -0.44867061677598474 + x3)^2) + x395 * ((-0.9554091045415013 + x1)^2 + (
    -0.3287768838698092 + x2)^2 + (-0.5079007221884251 + x3)^2) + x396 * ((
    -0.049015869567574866 + x1)^2 + (-0.7117888163278766 + x2)^2 + (
    -0.8523074296825538 + x3)^2) + x397 * ((-0.30979077869124183 + x1)^2 + (
    -0.4417160550189484 + x2)^2 + (-0.3302755586589736 + x3)^2) + x398 * ((
    -0.5591781894268806 + x1)^2 + (-0.8026089339206316 + x2)^2 + (
    -0.3713319195580873 + x3)^2) + x399 * ((-0.5840605834977219 + x1)^2 + (
    -0.4911685585761769 + x2)^2 + (-0.1816408065331926 + x3)^2) + x400 * ((
    -0.699915228142964 + x1)^2 + (-0.6846783090644426 + x2)^2 + (
    -0.5574598140568765 + x3)^2) + x401 * ((-0.6753730740440026 + x1)^2 + (
    -0.5489318129908483 + x2)^2 + (-0.10199137240931655 + x3)^2) + x402 * ((
    -0.11104797679961531 + x1)^2 + (-0.5472557486726254 + x2)^2 + (
    -0.9571846144505868 + x3)^2) + x403 * ((-0.4290104355078601 + x1)^2 + (
    -0.500625748131909 + x2)^2 + (-0.839875855861129 + x3)^2) + x404 * ((
    -0.8284104784524099 + x1)^2 + (-0.15168224190165258 + x2)^2 + (
    -0.7425205829813807 + x3)^2) + x405 * ((-0.7835845824065171 + x1)^2 + (
    -0.43892942409165736 + x2)^2 + (-0.9672883708633824 + x3)^2) + x406 * ((
    -0.9658474371081412 + x1)^2 + (-0.24521502946450435 + x2)^2 + (
    -0.19958521141831587 + x3)^2) + x407 * ((-0.6763699518851537 + x1)^2 + (
    -0.40784932714190725 + x2)^2 + (-0.9693530161050696 + x3)^2) + x408 * ((
    -0.015390131891825365 + x1)^2 + (-0.14588925853081935 + x2)^2 + (
    -0.5718899821316975 + x3)^2) + x409 * ((-0.6550458977158515 + x1)^2 + (
    -0.8097929221347935 + x2)^2 + (-0.4104406395267636 + x3)^2) + x410 * ((
    -0.7508103873205083 + x1)^2 + (-0.11532102750991224 + x2)^2 + (
    -0.6478368645129094 + x3)^2) + x411 * ((-0.9737229810910403 + x1)^2 + (
    -0.5163950909606659 + x2)^2 + (-0.6367061240819752 + x3)^2) + x412 * ((
    -0.5984140542435419 + x1)^2 + (-0.18984363054369258 + x2)^2 + (
    -0.027452684972157693 + x3)^2) + x413 * ((-0.9243666020019815 + x1)^2 + (
    -0.8145037925176214 + x2)^2 + (-0.6578177936970774 + x3)^2) + x414 * ((
    -0.9251327852082893 + x1)^2 + (-0.02218555315317494 + x2)^2 + (
    -0.4723664720086945 + x3)^2) + x415 * ((-0.6010677075600663 + x1)^2 + (
    -0.864007697540581 + x2)^2 + (-0.9271036737422498 + x3)^2) + x416 * ((
    -0.656591717593777 + x1)^2 + (-0.5134881016753086 + x2)^2 + (
    -0.1883008481102213 + x3)^2) + x417 * ((-0.7407314335715345 + x1)^2 + (
    -0.25458554896989405 + x2)^2 + (-0.556216069468436 + x3)^2) + x418 * ((
    -0.5120359138328312 + x1)^2 + (-0.8101978116075103 + x2)^2 + (
    -0.46638781967369414 + x3)^2) + x419 * ((-0.7135334348392973 + x1)^2 + (
    -0.1779541525794096 + x2)^2 + (-0.6317024521479767 + x3)^2) + x420 * ((
    -0.24177429627919167 + x1)^2 + (-0.6370581745682193 + x2)^2 + (
    -0.2710238175551406 + x3)^2) + x421 * ((-0.9997913560034266 + x1)^2 + (
    -0.48490318564542456 + x2)^2 + (-0.4160988220639955 + x3)^2) + x422 * ((
    -0.15980278916475676 + x1)^2 + (-0.06407095445485222 + x2)^2 + (
    -0.7249348271199497 + x3)^2) + x423 * ((-0.1411868189363079 + x1)^2 + (
    -0.3067431553565323 + x2)^2 + (-0.78575462849935 + x3)^2) + x424 * ((
    -0.5478827352853459 + x1)^2 + (-0.20291790816221889 + x2)^2 + (
    -0.8761980800539626 + x3)^2) + x425 * ((-0.9066224120947074 + x1)^2 + (
    -0.9518140343960166 + x2)^2 + (-0.5195535652548422 + x3)^2) + x426 * ((
    -0.4944497764703105 + x1)^2 + (-0.526178861965796 + x2)^2 + (
    -0.558537222910955 + x3)^2) + x427 * ((-0.2726667055675822 + x1)^2 + (
    -0.9345746694586428 + x2)^2 + (-0.8532831802582073 + x3)^2) + x428 * ((
    -0.9948056415771968 + x1)^2 + (-0.946100723693632 + x2)^2 + (
    -0.07095119487224366 + x3)^2) + x429 * ((-0.5213951586103635 + x1)^2 + (
    -0.8407112340244879 + x2)^2 + (-0.27895325936062443 + x3)^2) + x430 * ((
    -0.21494505782936268 + x1)^2 + (-0.7765096743882861 + x2)^2 + (
    -0.10254422951176734 + x3)^2) + x431 * ((-0.7120472016233632 + x1)^2 + (
    -0.49718927750005937 + x2)^2 + (-0.7541840771418643 + x3)^2) + x432 * ((
    -0.9685028423332537 + x1)^2 + (-0.5335345784258086 + x2)^2 + (
    -0.9890747374850164 + x3)^2) + x433 * ((-0.9230166234673173 + x1)^2 + (
    -0.6518475605727765 + x2)^2 + (-0.734854155976083 + x3)^2) + x434 * ((
    -0.06708623533817104 + x1)^2 + (-0.20172244637746983 + x2)^2 + (
    -0.2768060696570147 + x3)^2) + x435 * ((-0.4038888086617314 + x1)^2 + (
    -0.1486875332810369 + x2)^2 + (-0.0864364601708697 + x3)^2) + x436 * ((
    -0.4517085118551507 + x1)^2 + (-0.7765791454898151 + x2)^2 + (
    -0.18690810700205485 + x3)^2) + x437 * ((-0.6984051043122955 + x1)^2 + (
    -0.6903189697467437 + x2)^2 + (-0.040778131010728136 + x3)^2) + x438 * ((
    -0.6072448401148461 + x1)^2 + (-0.6438420452394027 + x2)^2 + (
    -0.6872356318162963 + x3)^2) + x439 * ((-0.3156326593340355 + x1)^2 + (
    -0.6507808794562617 + x2)^2 + (-0.6233647448682074 + x3)^2) + x440 * ((
    -0.4002818200993541 + x1)^2 + (-0.8997180632997818 + x2)^2 + (
    -0.14412431069924558 + x3)^2) + x441 * ((-0.4603826538409851 + x1)^2 + (
    -0.04233386015418239 + x2)^2 + (-0.7043950613308216 + x3)^2) + x442 * ((
    -0.870614516134697 + x1)^2 + (-0.8580337696409851 + x2)^2 + (
    -0.21857975143254016 + x3)^2) + x443 * ((-0.7885802541502687 + x1)^2 + (
    -0.983116728066409 + x2)^2 + (-0.6268381409191566 + x3)^2) + x444 * ((
    -0.453360688390823 + x1)^2 + (-0.17721212922523033 + x2)^2 + (
    -0.11369558618207087 + x3)^2) + x445 * ((-0.37622468340220194 + x1)^2 + (
    -0.10891294174292976 + x2)^2 + (-0.1499013005008839 + x3)^2) + x446 * ((
    -0.5160385921656351 + x1)^2 + (-0.5123193711182501 + x2)^2 + (
    -0.14661208983716012 + x3)^2) + x447 * ((-0.8318749644250042 + x1)^2 + (
    -0.9474430577714092 + x2)^2 + (-0.627935164487112 + x3)^2) + x448 * ((
    -0.1903852263517427 + x1)^2 + (-0.11470061584083246 + x2)^2 + (
    -0.44132933622437875 + x3)^2) + x449 * ((-0.7139609443452906 + x1)^2 + (
    -0.1662593335896707 + x2)^2 + (-0.206132946290832 + x3)^2) + x450 * ((
    -0.9287584108347345 + x1)^2 + (-0.4364542232297094 + x2)^2 + (
    -0.15930282013429242 + x3)^2) + x451 * ((-0.5438534099357585 + x1)^2 + (
    -0.6713389990511793 + x2)^2 + (-0.7515358561055495 + x3)^2) + x452 * ((
    -0.7953709431284481 + x1)^2 + (-0.09365706610576408 + x2)^2 + (
    -0.4729038737092427 + x3)^2) + x453 * ((-0.6834981451581077 + x1)^2 + (
    -0.5907013715726769 + x2)^2 + (-0.2177451536406989 + x3)^2) + x454 * ((
    -0.4631935234349823 + x1)^2 + (-0.8803533185868815 + x2)^2 + (
    -0.4273859435332188 + x3)^2) + x455 * ((-0.476785780348992 + x1)^2 + (
    -0.8869187769611843 + x2)^2 + (-0.7193029869652928 + x3)^2) + x456 * ((
    -0.31718143038215174 + x1)^2 + (-0.3262335948033561 + x2)^2 + (
    -0.9602949324145322 + x3)^2) + x457 * ((-0.5936199239050312 + x1)^2 + (
    -0.49552398966064715 + x2)^2 + (-0.49848694537003924 + x3)^2) + x458 * ((
    -0.9296199597347767 + x1)^2 + (-0.40889365057397287 + x2)^2 + (
    -0.8011545277509335 + x3)^2) + x459 * ((-0.7354055208486365 + x1)^2 + (
    -0.7799949232677478 + x2)^2 + (-0.22209643149708758 + x3)^2) + x460 * ((
    -0.8285174050295658 + x1)^2 + (-0.3399361044291944 + x2)^2 + (
    -0.5417626971057434 + x3)^2) + x461 * ((-0.4743970301387661 + x1)^2 + (
    -0.03968268525091545 + x2)^2 + (-0.7676276502511942 + x3)^2) + x462 * ((
    -0.9658526833599206 + x1)^2 + (-0.7769012618207594 + x2)^2 + (
    -0.30599222118777814 + x3)^2) + x463 * ((-0.48754823079065357 + x1)^2 + (
    -0.7322449135727448 + x2)^2 + (-0.6492327824562298 + x3)^2) + x464 * ((
    -0.9362650053761248 + x1)^2 + (-0.04268520093465755 + x2)^2 + (
    -0.7467628080743383 + x3)^2) + x465 * ((-0.9307916870383665 + x1)^2 + (
    -0.961756532300574 + x2)^2 + (-0.2155280011227615 + x3)^2) + x466 * ((
    -0.08912615918233224 + x1)^2 + (-0.6471821111714566 + x2)^2 + (
    -0.9913586544218587 + x3)^2) + x467 * ((-0.8358554991679754 + x1)^2 + (
    -0.08929161317162748 + x2)^2 + (-0.9647833465957737 + x3)^2) + x468 * ((
    -0.6273718862494942 + x1)^2 + (-0.7618805895251419 + x2)^2 + (
    -0.492165897853857 + x3)^2) + x469 * ((-0.6702555245476077 + x1)^2 + (
    -0.3610395370884728 + x2)^2 + (-0.766937565344216 + x3)^2) + x470 * ((
    -0.27485794231769844 + x1)^2 + (-0.5215206202220081 + x2)^2 + (
    -0.4889642491896449 + x3)^2) + x471 * ((-0.8463263789396861 + x1)^2 + (
    -0.4936221195625502 + x2)^2 + (-0.5709411193324385 + x3)^2) + x472 * ((
    -0.8054668308765568 + x1)^2 + (-0.2115365899248064 + x2)^2 + (
    -0.11566470511829063 + x3)^2) + x473 * ((-0.1943614935785951 + x1)^2 + (
    -0.8334718657316503 + x2)^2 + (-0.44326977139831436 + x3)^2) + x474 * ((
    -0.19480034368816324 + x1)^2 + (-0.8110564747660595 + x2)^2 + (
    -0.14302925781111175 + x3)^2) + x475 * ((-0.39190211653261664 + x1)^2 + (
    -0.9677972762274933 + x2)^2 + (-0.16271262210127324 + x3)^2) + x476 * ((
    -0.06731580772013712 + x1)^2 + (-0.6169831213923005 + x2)^2 + (
    -0.4027335514273457 + x3)^2) + x477 * ((-0.38110974958221877 + x1)^2 + (
    -0.519046146671436 + x2)^2 + (-0.5738902625301048 + x3)^2) + x478 * ((
    -0.9422399729911471 + x1)^2 + (-0.7184320029483544 + x2)^2 + (
    -0.9650701664096555 + x3)^2) + x479 * ((-0.36801794166483814 + x1)^2 + (
    -0.9368906012991046 + x2)^2 + (-0.75121049110894 + x3)^2) + x480 * ((
    -0.6630092172211279 + x1)^2 + (-0.20322311031211582 + x2)^2 + (
    -0.2887465568222305 + x3)^2) + x481 * ((-0.9706981704650441 + x1)^2 + (
    -0.08466082082361082 + x2)^2 + (-0.7247467660352114 + x3)^2) + x482 * ((
    -0.21059963791910552 + x1)^2 + (-0.49165647268816803 + x2)^2 + (
    -0.5804191839003714 + x3)^2) + x483 * ((-0.5236356611629658 + x1)^2 + (
    -0.07814696537946009 + x2)^2 + (-0.3132490429219894 + x3)^2) + x484 * ((
    -0.5026192836790041 + x1)^2 + (-0.6894528769723671 + x2)^2 + (
    -0.10662506884779244 + x3)^2) + x485 * ((-0.680171254701243 + x1)^2 + (
    -0.8794858932580393 + x2)^2 + (-0.1970105609325069 + x3)^2) + x486 * ((
    -0.653168096390829 + x1)^2 + (-0.8220713223404621 + x2)^2 + (
    -0.23312137565276492 + x3)^2) + x487 * ((-0.5945786510272542 + x1)^2 + (
    -0.6937129033829035 + x2)^2 + (-0.4629130124432773 + x3)^2) + x488 * ((
    -0.7366695477198858 + x1)^2 + (-0.10570699646360726 + x2)^2 + (
    -0.18565469991974215 + x3)^2) + x489 * ((-0.18743250673347933 + x1)^2 + (
    -0.8501799346529197 + x2)^2 + (-0.4455750149410902 + x3)^2) + x490 * ((
    -0.9211896892234244 + x1)^2 + (-0.8366465654279776 + x2)^2 + (
    -0.6201388866517694 + x3)^2) + x491 * ((-0.9891510966919514 + x1)^2 + (
    -0.6966082529523953 + x2)^2 + (-0.8133151377521731 + x3)^2) + x492 * ((
    -0.3902817623451159 + x1)^2 + (-0.24248773138219448 + x2)^2 + (
    -0.08078100456813775 + x3)^2) + x493 * ((-0.4298108705942121 + x1)^2 + (
    -0.45161887902165165 + x2)^2 + (-0.08388435410245021 + x3)^2) + x494 * ((
    -0.9073003783666486 + x1)^2 + (-0.48327373078316493 + x2)^2 + (
    -0.9910483026571903 + x3)^2) + x495 * ((-0.881651726906589 + x1)^2 + (
    -0.30048516094118216 + x2)^2 + (-0.9850698876652512 + x3)^2) + x496 * ((
    -0.6155649805033343 + x1)^2 + (-0.9348653805805935 + x2)^2 + (
    -0.6155415203207966 + x3)^2) + x497 * ((-0.8117253444866105 + x1)^2 + (
    -0.3734646122935913 + x2)^2 + (-0.5139722294737984 + x3)^2) + x498 * ((
    -0.3617901273059859 + x1)^2 + (-0.7565593293567897 + x2)^2 + (
    -0.8940449377670764 + x3)^2) + x499 * ((-0.9436103266245361 + x1)^2 + (
    -0.6770001466142013 + x2)^2 + (-0.7668347302572115 + x3)^2) + x500 * ((
    -0.4586541642719659 + x1)^2 + (-0.3840420830379708 + x2)^2 + (
    -0.6950693649611718 + x3)^2) + x501 * ((-0.7400622139264225 + x1)^2 + (
    -0.027543445911217934 + x2)^2 + (-0.3504023093298636 + x3)^2) + x502 * ((
    -0.8166839507821746 + x1)^2 + (-0.6985979465781534 + x2)^2 + (
    -0.136976908632233 + x3)^2) + x503 * ((-0.7247676574408647 + x1)^2 + (
    -0.7156252081799882 + x2)^2 + (-0.28421024086039204 + x3)^2) + x504 * ((
    -0.7116565008996277 + x1)^2 + (-0.19186706642009876 + x2)^2 + (
    -0.8309997111931379 + x3)^2) + x505 * ((-0.2257396195230682 + x1)^2 + (
    -0.14303777575075283 + x2)^2 + (-0.4801497799483495 + x3)^2) + x506 * ((
    -0.22699001220690018 + x1)^2 + (-0.28790414124402386 + x2)^2 + (
    -0.11035865916965082 + x3)^2) + x507 * ((-0.22002870473769487 + x1)^2 + (
    -0.5487022693999476 + x2)^2 + (-0.9866104667343789 + x3)^2) + x508 * ((
    -0.9091749596489073 + x1)^2 + (-0.34548122583324925 + x2)^2 + (
    -0.42621254666086883 + x3)^2) + x509 * ((-0.6236740823858687 + x1)^2 + (
    -0.9129273253173751 + x2)^2 + (-0.5002652562779129 + x3)^2) + x510 * ((
    -0.4640463436541785 + x4)^2 + (-0.1293137886728929 + x5)^2 + (
    -0.1717745705908742 + x6)^2) + x511 * ((-0.1099965161408738 + x4)^2 + (
    -0.7288891997489471 + x5)^2 + (-0.5812974922633755 + x6)^2) + x512 * ((
    -0.6918497277391157 + x4)^2 + (-0.20973658549886454 + x5)^2 + (
    -0.9916376137682873 + x6)^2) + x513 * ((-0.10214895121638168 + x4)^2 + (
    -0.4471617317045655 + x5)^2 + (-0.16723720460096436 + x6)^2) + x514 * ((
    -0.6359500594742937 + x4)^2 + (-0.26061637443601726 + x5)^2 + (
    -0.2816795076287437 + x6)^2) + x515 * ((-0.25944505466517365 + x4)^2 + (
    -0.2692384663732923 + x5)^2 + (-0.8325610020895001 + x6)^2) + x516 * ((
    -0.6284388376892046 + x4)^2 + (-0.35949079717409593 + x5)^2 + (
    -0.07225999789103066 + x6)^2) + x517 * ((-0.16701728419415074 + x4)^2 + (
    -0.9347771993757961 + x5)^2 + (-0.7666223410197908 + x6)^2) + x518 * ((
    -0.4221693374712633 + x4)^2 + (-0.9535156771220886 + x5)^2 + (
    -0.7574192303318398 + x6)^2) + x519 * ((-0.3448801407104496 + x4)^2 + (
    -0.8832949398016634 + x5)^2 + (-0.662248567565667 + x6)^2) + x520 * ((
    -0.084155570651406 + x4)^2 + (-0.17890412424092283 + x5)^2 + (
    -0.17388950075062537 + x6)^2) + x521 * ((-0.3916313023443915 + x4)^2 + (
    -0.019818007213793787 + x5)^2 + (-0.4569740922310289 + x6)^2) + x522 * ((
    -0.43181385423845964 + x4)^2 + (-0.6207687709011839 + x5)^2 + (
    -0.8592520589918983 + x6)^2) + x523 * ((-0.6487284790511446 + x4)^2 + (
    -0.7777238632207397 + x5)^2 + (-0.754096902035809 + x6)^2) + x524 * ((
    -0.8220434639163084 + x4)^2 + (-0.3741317795920437 + x5)^2 + (
    -0.8521093203138362 + x6)^2) + x525 * ((-0.7925713002121476 + x4)^2 + (
    -0.6036194154368819 + x5)^2 + (-0.8738614104363204 + x6)^2) + x526 * ((
    -0.5277139763548169 + x4)^2 + (-0.1993819110558287 + x5)^2 + (
    -0.5740216578606483 + x6)^2) + x527 * ((-0.41586747380620337 + x4)^2 + (
    -0.42388302044291193 + x5)^2 + (-0.2343053950781021 + x6)^2) + x528 * ((
    -0.5023781980401871 + x4)^2 + (-0.03818303029571113 + x5)^2 + (
    -0.6686132837122916 + x6)^2) + x529 * ((-0.6771457634322402 + x4)^2 + (
    -0.670453003754532 + x5)^2 + (-0.7277047293890516 + x6)^2) + x530 * ((
    -0.21786809597676893 + x4)^2 + (-0.08609770624017898 + x5)^2 + (
    -0.5475714527010952 + x6)^2) + x531 * ((-0.49880230295506545 + x4)^2 + (
    -0.1221804789346802 + x5)^2 + (-0.6985432568115264 + x6)^2) + x532 * ((
    -0.8088595862488974 + x4)^2 + (-0.32195887839650494 + x5)^2 + (
    -0.03760891748311046 + x6)^2) + x533 * ((-0.32995615684874324 + x4)^2 + (
    -0.3886013644913259 + x5)^2 + (-0.8469692211045076 + x6)^2) + x534 * ((
    -0.28669724151775544 + x4)^2 + (-0.7807597500251693 + x5)^2 + (
    -0.25528553923429653 + x6)^2) + x535 * ((-0.9488635103141098 + x4)^2 + (
    -0.43736211954180315 + x5)^2 + (-0.5982886678243227 + x6)^2) + x536 * ((
    -0.4466622010152166 + x4)^2 + (-0.6090348194282511 + x5)^2 + (
    -0.8670075403112468 + x6)^2) + x537 * ((-0.951037074725791 + x4)^2 + (
    -0.1407161090628133 + x5)^2 + (-0.13092171611554282 + x6)^2) + x538 * ((
    -0.5541921779696605 + x4)^2 + (-0.8135752021382663 + x5)^2 + (
    -0.3027451108170902 + x6)^2) + x539 * ((-0.5305963246394046 + x4)^2 + (
    -0.23800490595118307 + x5)^2 + (-0.6735380224500424 + x6)^2) + x540 * ((
    -0.5909678409002741 + x4)^2 + (-0.48993330795236645 + x5)^2 + (
    -0.678288644059539 + x6)^2) + x541 * ((-0.43028464262572896 + x4)^2 + (
    -0.18942101979564563 + x5)^2 + (-0.5387520132500516 + x6)^2) + x542 * ((
    -0.9240763867641095 + x4)^2 + (-0.626146721604441 + x5)^2 + (
    -0.6874440043145749 + x6)^2) + x543 * ((-0.8160616417563322 + x4)^2 + (
    -0.8985769697407207 + x5)^2 + (-0.7069074935285429 + x6)^2) + x544 * ((
    -0.70100419051915 + x4)^2 + (-0.4569577862776859 + x5)^2 + (
    -0.1471193271794946 + x6)^2) + x545 * ((-0.4285718440951606 + x4)^2 + (
    -0.8609883932856427 + x5)^2 + (-0.1410876060058085 + x6)^2) + x546 * ((
    -0.6332293940657829 + x4)^2 + (-0.8525493047471094 + x5)^2 + (
    -0.7321100368238428 + x6)^2) + x547 * ((-0.29503916007091424 + x4)^2 + (
    -0.4380701575264203 + x5)^2 + (-0.820365575773603 + x6)^2) + x548 * ((
    -0.23227503662891036 + x4)^2 + (-0.05055428546369656 + x5)^2 + (
    -0.14176384941021558 + x6)^2) + x549 * ((-0.5635448791654668 + x4)^2 + (
    -0.3059173029907377 + x5)^2 + (-0.737377855421216 + x6)^2) + x550 * ((
    -0.22436900298779006 + x4)^2 + (-0.5838557597663682 + x5)^2 + (
    -0.12681037493434544 + x6)^2) + x551 * ((-0.36240169855712956 + x4)^2 + (
    -0.04857443538763084 + x5)^2 + (-0.9860358791315034 + x6)^2) + x552 * ((
    -0.08195695254594337 + x4)^2 + (-0.18885105382104828 + x5)^2 + (
    -0.8027553727917437 + x6)^2) + x553 * ((-0.3963885195949204 + x4)^2 + (
    -0.3241632475929923 + x5)^2 + (-0.853275456923333 + x6)^2) + x554 * ((
    -0.5908438916261783 + x4)^2 + (-0.7950112790507812 + x5)^2 + (
    -0.32740880277441486 + x6)^2) + x555 * ((-0.8432432133553496 + x4)^2 + (
    -0.05282798148772461 + x5)^2 + (-0.45546519649801565 + x6)^2) + x556 * ((
    -0.42236971119841793 + x4)^2 + (-0.8947757440038225 + x5)^2 + (
    -0.4695709175424789 + x6)^2) + x557 * ((-0.8247942497549123 + x4)^2 + (
    -0.5014330359845784 + x5)^2 + (-0.7470113565382576 + x6)^2) + x558 * ((
    -0.48834453204993566 + x4)^2 + (-0.5215169837629428 + x5)^2 + (
    -0.6466473117603931 + x6)^2) + x559 * ((-0.5539921888753628 + x4)^2 + (
    -0.3015288028980093 + x5)^2 + (-0.7614340990080889 + x6)^2) + x560 * ((
    -0.13405913842449635 + x4)^2 + (-0.010282913789367076 + x5)^2 + (
    -0.47341317441006114 + x6)^2) + x561 * ((-0.4844169330601604 + x4)^2 + (
    -0.6930522779489291 + x5)^2 + (-0.7621495736478611 + x6)^2) + x562 * ((
    -0.7740308764454359 + x4)^2 + (-0.03729224901817285 + x5)^2 + (
    -0.060792495607531416 + x6)^2) + x563 * ((-0.43017611384019483 + x4)^2 + (
    -0.7275353979377646 + x5)^2 + (-0.11228956220406072 + x6)^2) + x564 * ((
    -0.730207310114505 + x4)^2 + (-0.9753557541190604 + x5)^2 + (
    -0.046876482359277216 + x6)^2) + x565 * ((-0.24388528239994156 + x4)^2 + (
    -0.8253598309798788 + x5)^2 + (-0.5495236414774879 + x6)^2) + x566 * ((
    -0.9122699869151167 + x4)^2 + (-0.31915757121431776 + x5)^2 + (
    -0.7372813637720362 + x6)^2) + x567 * ((-0.7238338524735144 + x4)^2 + (
    -0.05489659548168713 + x5)^2 + (-0.3744471629501799 + x6)^2) + x568 * ((
    -0.7639916865325218 + x4)^2 + (-0.37213335483670207 + x5)^2 + (
    -0.15924084004650396 + x6)^2) + x569 * ((-0.02038252676112806 + x4)^2 + (
    -0.6941311922925457 + x5)^2 + (-0.8152379226615076 + x6)^2) + x570 * ((
    -0.2834980659872919 + x4)^2 + (-0.098062561074025 + x5)^2 + (
    -0.09504713494440098 + x6)^2) + x571 * ((-0.5777263686540078 + x4)^2 + (
    -0.6553186629601886 + x5)^2 + (-0.10852708184066717 + x6)^2) + x572 * ((
    -0.0504906548870141 + x4)^2 + (-0.01801577482327177 + x5)^2 + (
    -0.7073392283503382 + x6)^2) + x573 * ((-0.7320511478522743 + x4)^2 + (
    -0.2419803614589029 + x5)^2 + (-0.6026607994765517 + x6)^2) + x574 * ((
    -0.9681953946844297 + x4)^2 + (-0.6220011693963317 + x5)^2 + (
    -0.9192154721620333 + x6)^2) + x575 * ((-0.7449798611870608 + x4)^2 + (
    -0.618779704147399 + x5)^2 + (-0.9908068620931784 + x6)^2) + x576 * ((
    -0.04656000736284627 + x4)^2 + (-0.7622587439775123 + x5)^2 + (
    -0.5444825165905486 + x6)^2) + x577 * ((-0.5304149849270671 + x4)^2 + (
    -0.7853544629150807 + x5)^2 + (-0.6650413115686411 + x6)^2) + x578 * ((
    -0.4316006167167099 + x4)^2 + (-0.9564410998503826 + x5)^2 + (
    -0.2754654244349003 + x6)^2) + x579 * ((-0.8192654145647627 + x4)^2 + (
    -0.3449960317441789 + x5)^2 + (-0.4639588553586419 + x6)^2) + x580 * ((
    -0.4202896905773047 + x4)^2 + (-0.4903100277526028 + x5)^2 + (
    -0.4508730801904217 + x6)^2) + x581 * ((-0.7839805319619787 + x4)^2 + (
    -0.07624343650513432 + x5)^2 + (-0.010490453443519732 + x6)^2) + x582 * ((
    -0.716640229430628 + x4)^2 + (-0.3191301181101275 + x5)^2 + (
    -0.24084475450576515 + x6)^2) + x583 * ((-0.48973960110221293 + x4)^2 + (
    -0.19400622702592318 + x5)^2 + (-0.5586480098172433 + x6)^2) + x584 * ((
    -0.25765000251075176 + x4)^2 + (-0.3991120430135222 + x5)^2 + (
    -0.624261591485904 + x6)^2) + x585 * ((-0.2102936857169334 + x4)^2 + (
    -0.6048029406652995 + x5)^2 + (-0.527925854621275 + x6)^2) + x586 * ((
    -0.1418787545905994 + x4)^2 + (-0.0774930390726144 + x5)^2 + (
    -0.0249724785862947 + x6)^2) + x587 * ((-0.034877726496859385 + x4)^2 + (
    -0.6319560857501643 + x5)^2 + (-0.7242772960087813 + x6)^2) + x588 * ((
    -0.9433129608773202 + x4)^2 + (-0.3736070884724113 + x5)^2 + (
    -0.92947567244536 + x6)^2) + x589 * ((-0.19723347065034202 + x4)^2 + (
    -0.5757655498584185 + x5)^2 + (-0.4442676556771823 + x6)^2) + x590 * ((
    -0.08053094633012514 + x4)^2 + (-0.49597290071491906 + x5)^2 + (
    -0.68982692206069 + x6)^2) + x591 * ((-0.7371912517400753 + x4)^2 + (
    -0.4111907705168256 + x5)^2 + (-0.44596226596462496 + x6)^2) + x592 * ((
    -0.46785953968803606 + x4)^2 + (-0.45341953773271215 + x5)^2 + (
    -0.7283106962836612 + x6)^2) + x593 * ((-0.8261694191695272 + x4)^2 + (
    -0.41472831889096884 + x5)^2 + (-0.9106938093148554 + x6)^2) + x594 * ((
    -0.44683645298814745 + x4)^2 + (-0.6996104890042156 + x5)^2 + (
    -0.066679930798903 + x6)^2) + x595 * ((-0.9366613572848865 + x4)^2 + (
    -0.42199403399468605 + x5)^2 + (-0.10350991187036918 + x6)^2) + x596 * ((
    -0.9730815838375089 + x4)^2 + (-0.6831147433040942 + x5)^2 + (
    -0.09074649263643031 + x6)^2) + x597 * ((-0.19241596788927118 + x4)^2 + (
    -0.47076401046441096 + x5)^2 + (-0.15843960550460512 + x6)^2) + x598 * ((
    -0.04999694084986828 + x4)^2 + (-0.43552364112098474 + x5)^2 + (
    -0.317689183487498 + x6)^2) + x599 * ((-0.7805202520309815 + x4)^2 + (
    -0.07439424045077114 + x5)^2 + (-0.11817215106111634 + x6)^2) + x600 * ((
    -0.35732353691638374 + x4)^2 + (-0.729905338698986 + x5)^2 + (
    -0.5100765758088116 + x6)^2) + x601 * ((-0.4780015271753969 + x4)^2 + (
    -0.192158490869756 + x5)^2 + (-0.01693000121269117 + x6)^2) + x602 * ((
    -0.781318913473494 + x4)^2 + (-0.25445440893640614 + x5)^2 + (
    -0.7752207968553286 + x6)^2) + x603 * ((-0.8343131584256498 + x4)^2 + (
    -0.2904065598498118 + x5)^2 + (-0.44278123600229036 + x6)^2) + x604 * ((
    -0.9639849716170581 + x4)^2 + (-0.15550942759340902 + x5)^2 + (
    -0.12539074143986528 + x6)^2) + x605 * ((-0.9221783343065362 + x4)^2 + (
    -0.8425574910926684 + x5)^2 + (-0.9716597371554934 + x6)^2) + x606 * ((
    -0.46470646895314527 + x4)^2 + (-0.43245231227619974 + x5)^2 + (
    -0.5802228635322391 + x6)^2) + x607 * ((-0.271134180722319 + x4)^2 + (
    -0.36061003024560156 + x5)^2 + (-0.1471398510067108 + x6)^2) + x608 * ((
    -0.11520302100676727 + x4)^2 + (-0.663912716794071 + x5)^2 + (
    -0.5527561125387709 + x6)^2) + x609 * ((-0.6162912656168867 + x4)^2 + (
    -0.5377119910240235 + x5)^2 + (-0.5807063907096474 + x6)^2) + x610 * ((
    -0.37145013174802566 + x4)^2 + (-0.5345645332516239 + x5)^2 + (
    -0.510699989525291 + x6)^2) + x611 * ((-0.03393556960060573 + x4)^2 + (
    -0.0156666184663532 + x5)^2 + (-0.07624209854333597 + x6)^2) + x612 * ((
    -0.8270963072435799 + x4)^2 + (-0.7741889426436234 + x5)^2 + (
    -0.11760611435305912 + x6)^2) + x613 * ((-0.18357821030782528 + x4)^2 + (
    -0.9734815530389282 + x5)^2 + (-0.08722449406089927 + x6)^2) + x614 * ((
    -0.4006392450848354 + x4)^2 + (-0.9419621185211043 + x5)^2 + (
    -0.7043081992282076 + x6)^2) + x615 * ((-0.22556650178941084 + x4)^2 + (
    -0.6034598644180125 + x5)^2 + (-0.1696902160808953 + x6)^2) + x616 * ((
    -0.9825403553111026 + x4)^2 + (-0.35577808053830695 + x5)^2 + (
    -0.28203592489557505 + x6)^2) + x617 * ((-0.19474142388607596 + x4)^2 + (
    -0.8131107522988229 + x5)^2 + (-0.20189429638588874 + x6)^2) + x618 * ((
    -0.8965750056171701 + x4)^2 + (-0.681955506000223 + x5)^2 + (
    -0.1398601385146755 + x6)^2) + x619 * ((-0.6906419235208477 + x4)^2 + (
    -0.24426493995237364 + x5)^2 + (-0.47872107051865875 + x6)^2) + x620 * ((
    -0.4832440968672467 + x4)^2 + (-0.6969985518711306 + x5)^2 + (
    -0.9470893906754926 + x6)^2) + x621 * ((-0.10622876499073441 + x4)^2 + (
    -0.693441063669681 + x5)^2 + (-0.1652812026058289 + x6)^2) + x622 * ((
    -0.9897886682814803 + x4)^2 + (-0.599511795785779 + x5)^2 + (
    -0.8125758496836358 + x6)^2) + x623 * ((-0.8169198572273942 + x4)^2 + (
    -0.008813750148081168 + x5)^2 + (-0.26018856120218925 + x6)^2) + x624 * ((
    -0.7549634171088901 + x4)^2 + (-0.43078690581257384 + x5)^2 + (
    -0.7749777657255487 + x6)^2) + x625 * ((-0.49182605753605824 + x4)^2 + (
    -0.28246579300389185 + x5)^2 + (-0.5070642636215076 + x6)^2) + x626 * ((
    -0.5042598753977806 + x4)^2 + (-0.0022250490805308942 + x5)^2 + (
    -0.391688155748926 + x6)^2) + x627 * ((-0.876071155170606 + x4)^2 + (
    -0.5508423923993612 + x5)^2 + (-0.824559592123001 + x6)^2) + x628 * ((
    -0.11165887263159624 + x4)^2 + (-0.7085491226119169 + x5)^2 + (
    -0.8775234759634866 + x6)^2) + x629 * ((-0.06305425963412226 + x4)^2 + (
    -0.1692915986404735 + x5)^2 + (-0.1546726877920308 + x6)^2) + x630 * ((
    -0.9499620149510364 + x4)^2 + (-0.20812541109619742 + x5)^2 + (
    -0.34754918900968657 + x6)^2) + x631 * ((-0.5460977024824913 + x4)^2 + (
    -0.9637992932230987 + x5)^2 + (-0.6995797299071689 + x6)^2) + x632 * ((
    -0.25491459381765613 + x4)^2 + (-0.8070965237021143 + x5)^2 + (
    -0.8356296626230745 + x6)^2) + x633 * ((-0.1702497329876329 + x4)^2 + (
    -0.4046122894687497 + x5)^2 + (-0.983146211120638 + x6)^2) + x634 * ((
    -0.38494123369736066 + x4)^2 + (-0.0904492373848188 + x5)^2 + (
    -0.06525088803516699 + x6)^2) + x635 * ((-0.1342401664666969 + x4)^2 + (
    -0.6663416890145257 + x5)^2 + (-0.7438434658481744 + x6)^2) + x636 * ((
    -0.7253450049079363 + x4)^2 + (-0.4870006307057251 + x5)^2 + (
    -0.8740872298975312 + x6)^2) + x637 * ((-0.7328325422437689 + x4)^2 + (
    -0.8575177732697433 + x5)^2 + (-0.4765071623659649 + x6)^2) + x638 * ((
    -0.6783555500591814 + x4)^2 + (-0.9452264908498691 + x5)^2 + (
    -0.4009905455748076 + x6)^2) + x639 * ((-0.9645465696225488 + x4)^2 + (
    -0.8988121792155044 + x5)^2 + (-0.8693701035695635 + x6)^2) + x640 * ((
    -0.034109539793666044 + x4)^2 + (-0.7341228944483525 + x5)^2 + (
    -0.6711095074457485 + x6)^2) + x641 * ((-0.9925652875910469 + x4)^2 + (
    -0.9767372917892282 + x5)^2 + (-0.35119270893145604 + x6)^2) + x642 * ((
    -0.4335634471581603 + x4)^2 + (-0.9773387547384761 + x5)^2 + (
    -0.8638040489407179 + x6)^2) + x643 * ((-0.8298565888279448 + x4)^2 + (
    -0.26942544674381563 + x5)^2 + (-0.07762497635314547 + x6)^2) + x644 * ((
    -0.7541529640858855 + x4)^2 + (-0.5901288469645308 + x5)^2 + (
    -0.8131521214901242 + x6)^2) + x645 * ((-0.6175218139719055 + x4)^2 + (
    -0.9185690552704726 + x5)^2 + (-0.9584989171844233 + x6)^2) + x646 * ((
    -0.5426908933870604 + x4)^2 + (-0.9276924059348457 + x5)^2 + (
    -0.5088628864009217 + x6)^2) + x647 * ((-0.36674157946961816 + x4)^2 + (
    -0.9494397054589957 + x5)^2 + (-0.502673714811412 + x6)^2) + x648 * ((
    -0.7718452911924847 + x4)^2 + (-0.08932990709963073 + x5)^2 + (
    -0.8114836680773437 + x6)^2) + x649 * ((-0.626463542469553 + x4)^2 + (
    -0.5374333330491173 + x5)^2 + (-0.12893104003458555 + x6)^2) + x650 * ((
    -0.7425349118488094 + x4)^2 + (-0.1255983096608143 + x5)^2 + (
    -0.35251120977084616 + x6)^2) + x651 * ((-0.5763919417102015 + x4)^2 + (
    -0.8668165395935221 + x5)^2 + (-0.18418689718597303 + x6)^2) + x652 * ((
    -0.0842638329353742 + x4)^2 + (-0.22780453935881773 + x5)^2 + (
    -0.06751612916008864 + x6)^2) + x653 * ((-0.4752871340736414 + x4)^2 + (
    -0.569148110715716 + x5)^2 + (-0.825451649082575 + x6)^2) + x654 * ((
    -0.9331572175670021 + x4)^2 + (-0.13944078138289107 + x5)^2 + (
    -0.4974317423493232 + x6)^2) + x655 * ((-0.5801698170306864 + x4)^2 + (
    -0.09023678868466112 + x5)^2 + (-0.5350628309500659 + x6)^2) + x656 * ((
    -0.5007559134871579 + x4)^2 + (-0.9361289066528181 + x5)^2 + (
    -0.4876551928604236 + x6)^2) + x657 * ((-0.3331382694999312 + x4)^2 + (
    -0.8003640425360357 + x5)^2 + (-0.4456772103718464 + x6)^2) + x658 * ((
    -0.580897968874648 + x4)^2 + (-0.6875204337094218 + x5)^2 + (
    -0.23853575215395162 + x6)^2) + x659 * ((-0.26259058062087826 + x4)^2 + (
    -0.31607289532856375 + x5)^2 + (-0.08079831830446549 + x6)^2) + x660 * ((
    -0.8749384932019274 + x4)^2 + (-0.5978601364266924 + x5)^2 + (
    -0.2709722104839264 + x6)^2) + x661 * ((-0.3380164843711445 + x4)^2 + (
    -0.9620957935062617 + x5)^2 + (-0.5318755277541398 + x6)^2) + x662 * ((
    -0.19915462374899218 + x4)^2 + (-0.16745416979147543 + x5)^2 + (
    -0.8177983201819474 + x6)^2) + x663 * ((-0.8422569529306239 + x4)^2 + (
    -0.9503230877966571 + x5)^2 + (-0.27758371082708055 + x6)^2) + x664 * ((
    -0.44963143674100436 + x4)^2 + (-0.6298100336125453 + x5)^2 + (
    -0.6473187227829037 + x6)^2) + x665 * ((-0.5323794396752508 + x4)^2 + (
    -0.29195939691071726 + x5)^2 + (-0.3777205926486479 + x6)^2) + x666 * ((
    -0.08774633426227729 + x4)^2 + (-0.5103291813715215 + x5)^2 + (
    -0.21197701339206598 + x6)^2) + x667 * ((-0.1886462563105995 + x4)^2 + (
    -0.7166154370441229 + x5)^2 + (-0.8967828307834859 + x6)^2) + x668 * ((
    -0.9135151722699717 + x4)^2 + (-0.24518247233237755 + x5)^2 + (
    -0.22467871490663316 + x6)^2) + x669 * ((-0.4002656679601796 + x4)^2 + (
    -0.8075378016015988 + x5)^2 + (-0.9589722648623482 + x6)^2) + x670 * ((
    -0.350804850761565 + x4)^2 + (-0.2001510201677693 + x5)^2 + (
    -0.3847312652361822 + x6)^2) + x671 * ((-0.7092459191225206 + x4)^2 + (
    -0.3653825052791586 + x5)^2 + (-0.4100011123148736 + x6)^2) + x672 * ((
    -0.08924822462276016 + x4)^2 + (-0.2350022965537154 + x5)^2 + (
    -0.4724131123343983 + x6)^2) + x673 * ((-0.678878546266445 + x4)^2 + (
    -0.0024223731399833914 + x5)^2 + (-0.18719967650857738 + x6)^2) + x674 * ((
    -0.8949831170437572 + x4)^2 + (-0.6742418627601845 + x5)^2 + (
    -0.9659226960334533 + x6)^2) + x675 * ((-0.461298010620385 + x4)^2 + (
    -0.3515384955734874 + x5)^2 + (-0.1589819355604557 + x6)^2) + x676 * ((
    -0.4742180560695449 + x4)^2 + (-0.31128812059338673 + x5)^2 + (
    -0.16193285694593962 + x6)^2) + x677 * ((-0.9057373068507129 + x4)^2 + (
    -0.07169041620954708 + x5)^2 + (-0.24658295842854583 + x6)^2) + x678 * ((
    -0.042416932822683995 + x4)^2 + (-0.11901530250324566 + x5)^2 + (
    -0.8719607562434413 + x6)^2) + x679 * ((-0.3509796417311175 + x4)^2 + (
    -0.7261268633422199 + x5)^2 + (-0.37378698482516615 + x6)^2) + x680 * ((
    -0.48178722792919537 + x4)^2 + (-0.12507968740842412 + x5)^2 + (
    -0.1533291787002754 + x6)^2) + x681 * ((-0.690187452865442 + x4)^2 + (
    -0.06414157686780875 + x5)^2 + (-0.9184182999081079 + x6)^2) + x682 * ((
    -0.7601598471825683 + x4)^2 + (-0.39014455511239565 + x5)^2 + (
    -0.06643024228030481 + x6)^2) + x683 * ((-0.7648317386640142 + x4)^2 + (
    -0.8401096588730549 + x5)^2 + (-0.6476437320133126 + x6)^2) + x684 * ((
    -0.9157717582294775 + x4)^2 + (-0.7156353049895615 + x5)^2 + (
    -0.1779714150010886 + x6)^2) + x685 * ((-0.2914662714138311 + x4)^2 + (
    -0.8979506548155362 + x5)^2 + (-0.28370242601709506 + x6)^2) + x686 * ((
    -0.41299200861407237 + x4)^2 + (-0.5731791645656842 + x5)^2 + (
    -0.9880744442012739 + x6)^2) + x687 * ((-0.2773152437673355 + x4)^2 + (
    -0.5869730199299126 + x5)^2 + (-0.6503070600258439 + x6)^2) + x688 * ((
    -0.7054867170779409 + x4)^2 + (-0.38605289741051385 + x5)^2 + (
    -0.18161609983908555 + x6)^2) + x689 * ((-0.9858526028351562 + x4)^2 + (
    -0.11659661065988192 + x5)^2 + (-0.6328911420439645 + x6)^2) + x690 * ((
    -0.008586957495201109 + x4)^2 + (-0.6828361406835076 + x5)^2 + (
    -0.9383137951511125 + x6)^2) + x691 * ((-0.5535058192578067 + x4)^2 + (
    -0.007867554292018242 + x5)^2 + (-0.3880343478492315 + x6)^2) + x692 * ((
    -0.2998574271558311 + x4)^2 + (-0.5685060268070001 + x5)^2 + (
    -0.8612909410674978 + x6)^2) + x693 * ((-0.7279300554494663 + x4)^2 + (
    -0.8665137249506871 + x5)^2 + (-0.2425661607644104 + x6)^2) + x694 * ((
    -0.3674243260814667 + x4)^2 + (-0.6726025203611717 + x5)^2 + (
    -0.3019444385645804 + x6)^2) + x695 * ((-0.561221458088611 + x4)^2 + (
    -0.1252412923674795 + x5)^2 + (-0.7626531785557333 + x6)^2) + x696 * ((
    -0.7526982106932172 + x4)^2 + (-0.09811091554051077 + x5)^2 + (
    -0.8331863589378469 + x6)^2) + x697 * ((-0.7212209268256802 + x4)^2 + (
    -0.3347884192733733 + x5)^2 + (-0.34081278172854135 + x6)^2) + x698 * ((
    -0.38492684008888933 + x4)^2 + (-0.053573445724505286 + x5)^2 + (
    -0.45746291996264776 + x6)^2) + x699 * ((-0.17867755090980397 + x4)^2 + (
    -0.846403915886413 + x5)^2 + (-0.15238735379254842 + x6)^2) + x700 * ((
    -0.7342435428310872 + x4)^2 + (-0.35254162287667923 + x5)^2 + (
    -0.3649777944564463 + x6)^2) + x701 * ((-0.21121661378120005 + x4)^2 + (
    -0.8764333024482275 + x5)^2 + (-0.6905270652669678 + x6)^2) + x702 * ((
    -0.7454607699149387 + x4)^2 + (-0.5243311461762572 + x5)^2 + (
    -0.46847369630081737 + x6)^2) + x703 * ((-0.5777724524082414 + x4)^2 + (
    -0.9389607386881164 + x5)^2 + (-0.9490991772196733 + x6)^2) + x704 * ((
    -0.6953770563282883 + x4)^2 + (-0.30766167182637194 + x5)^2 + (
    -0.9947613161831723 + x6)^2) + x705 * ((-0.07322511345630467 + x4)^2 + (
    -0.11542967998046938 + x5)^2 + (-0.5551153181290245 + x6)^2) + x706 * ((
    -0.823466601595051 + x4)^2 + (-0.4761579425686089 + x5)^2 + (
    -0.7645792742638973 + x6)^2) + x707 * ((-0.3065558046367579 + x4)^2 + (
    -0.6489835149493414 + x5)^2 + (-0.24712630191036555 + x6)^2) + x708 * ((
    -0.42587171854139994 + x4)^2 + (-0.9609489628414893 + x5)^2 + (
    -0.34607854810703564 + x6)^2) + x709 * ((-0.22514530689258294 + x4)^2 + (
    -0.29572551314242157 + x5)^2 + (-0.04494292345454676 + x6)^2) + x710 * ((
    -0.733484242355372 + x4)^2 + (-0.7428655248132915 + x5)^2 + (
    -0.7982295536152093 + x6)^2) + x711 * ((-0.5007178891993553 + x4)^2 + (
    -0.18337867834916188 + x5)^2 + (-0.2867876649071047 + x6)^2) + x712 * ((
    -0.9062122087196477 + x4)^2 + (-0.5780300635857895 + x5)^2 + (
    -0.1538197962604425 + x6)^2) + x713 * ((-0.7863514275791065 + x4)^2 + (
    -0.047106972476383846 + x5)^2 + (-0.9442358046581198 + x6)^2) + x714 * ((
    -0.49327445076665244 + x4)^2 + (-0.7635057400072934 + x5)^2 + (
    -0.08977894732398484 + x6)^2) + x715 * ((-0.5885030216777958 + x4)^2 + (
    -0.31457737395890006 + x5)^2 + (-0.06769170169106442 + x6)^2) + x716 * ((
    -0.2624396116681811 + x4)^2 + (-0.8735241081831786 + x5)^2 + (
    -0.17009678211994406 + x6)^2) + x717 * ((-0.8745938616823902 + x4)^2 + (
    -0.6895313121315244 + x5)^2 + (-0.3798558733668982 + x6)^2) + x718 * ((
    -0.19470988963139768 + x4)^2 + (-0.7061159026040712 + x5)^2 + (
    -0.09540851729033883 + x6)^2) + x719 * ((-0.07281526695083318 + x4)^2 + (
    -0.5313755426899924 + x5)^2 + (-0.3281258830967686 + x6)^2) + x720 * ((
    -0.0050140137596184076 + x4)^2 + (-0.0571436713320036 + x5)^2 + (
    -0.7424653869787131 + x6)^2) + x721 * ((-0.7365729576101151 + x4)^2 + (
    -0.016411359906266965 + x5)^2 + (-0.6018392757598213 + x6)^2) + x722 * ((
    -0.9710402789360123 + x4)^2 + (-0.057905237168721646 + x5)^2 + (
    -0.1016804201191902 + x6)^2) + x723 * ((-0.886784750676047 + x4)^2 + (
    -0.5909509982566028 + x5)^2 + (-0.08207033376025652 + x6)^2) + x724 * ((
    -0.9456537388004167 + x4)^2 + (-0.10430429872917613 + x5)^2 + (
    -0.47980776700636785 + x6)^2) + x725 * ((-0.01703842580768944 + x4)^2 + (
    -0.3771031988756788 + x5)^2 + (-0.9126173043337085 + x6)^2) + x726 * ((
    -0.7473088625241339 + x4)^2 + (-0.1992639563893337 + x5)^2 + (
    -0.27259207689859966 + x6)^2) + x727 * ((-0.9866924203074965 + x4)^2 + (
    -0.02211001009510316 + x5)^2 + (-0.710715645336501 + x6)^2) + x728 * ((
    -0.22231763494264423 + x4)^2 + (-0.7222747879572179 + x5)^2 + (
    -0.48387331778539744 + x6)^2) + x729 * ((-0.5217371859514337 + x4)^2 + (
    -0.8145029375864773 + x5)^2 + (-0.5971133086187703 + x6)^2) + x730 * ((
    -0.16123590082773454 + x4)^2 + (-0.7338632807820815 + x5)^2 + (
    -0.9775931853783937 + x6)^2) + x731 * ((-0.15216767027450806 + x4)^2 + (
    -0.8194769982782 + x5)^2 + (-0.3798283273565146 + x6)^2) + x732 * ((
    -0.755130243908553 + x4)^2 + (-0.964046166903329 + x5)^2 + (
    -0.37287898957618804 + x6)^2) + x733 * ((-0.4515557009816349 + x4)^2 + (
    -0.5888415389238447 + x5)^2 + (-0.6268802444924639 + x6)^2) + x734 * ((
    -0.8339407401569209 + x4)^2 + (-0.3941136302934939 + x5)^2 + (
    -0.0011773452039460786 + x6)^2) + x735 * ((-0.03523664509745583 + x4)^2 + (
    -0.9282465013011052 + x5)^2 + (-0.10432387873774907 + x6)^2) + x736 * ((
    -0.5824740927361365 + x4)^2 + (-0.2830428234231407 + x5)^2 + (
    -0.2929978420181991 + x6)^2) + x737 * ((-0.3457319486786484 + x4)^2 + (
    -0.6369253498892743 + x5)^2 + (-0.35691844570607956 + x6)^2) + x738 * ((
    -0.42088037600595574 + x4)^2 + (-0.6312418989251471 + x5)^2 + (
    -0.8287246238964575 + x6)^2) + x739 * ((-0.021979693073987727 + x4)^2 + (
    -0.2773405353290628 + x5)^2 + (-0.029133052826545436 + x6)^2) + x740 * ((
    -0.5081863887708018 + x4)^2 + (-0.20601907370036388 + x5)^2 + (
    -0.9821208081223113 + x6)^2) + x741 * ((-0.0019048004425398224 + x4)^2 + (
    -0.9834147377960726 + x5)^2 + (-0.2723044658709237 + x6)^2) + x742 * ((
    -0.5500730095581713 + x4)^2 + (-0.9929315189942348 + x5)^2 + (
    -0.8008514847320088 + x6)^2) + x743 * ((-0.42236107077823737 + x4)^2 + (
    -0.8886238887911541 + x5)^2 + (-0.8222569499938951 + x6)^2) + x744 * ((
    -0.0672943459062394 + x4)^2 + (-0.2827538856518119 + x5)^2 + (
    -0.13430545927864412 + x6)^2) + x745 * ((-0.5677325188553733 + x4)^2 + (
    -0.938532426013799 + x5)^2 + (-0.7611389677471435 + x6)^2) + x746 * ((
    -0.8629019843437029 + x4)^2 + (-0.8826021988159478 + x5)^2 + (
    -0.7188638964511778 + x6)^2) + x747 * ((-0.5507464371836962 + x4)^2 + (
    -0.7611165241588504 + x5)^2 + (-0.02910037665638643 + x6)^2) + x748 * ((
    -0.34299191582875777 + x4)^2 + (-0.524901527819975 + x5)^2 + (
    -0.5781388484542243 + x6)^2) + x749 * ((-0.35151500287062976 + x4)^2 + (
    -0.21136430913659288 + x5)^2 + (-0.08857984066212443 + x6)^2) + x750 * ((
    -0.7675403347878336 + x4)^2 + (-0.532832695685235 + x5)^2 + (
    -0.2503117333896512 + x6)^2) + x751 * ((-0.23097591211896384 + x4)^2 + (
    -0.15477203487438085 + x5)^2 + (-0.5054800430556513 + x6)^2) + x752 * ((
    -0.7881833845877819 + x4)^2 + (-0.2758754119705751 + x5)^2 + (
    -0.9382258338204086 + x6)^2) + x753 * ((-0.9466477036942484 + x4)^2 + (
    -0.06948523439716237 + x5)^2 + (-0.7146827511615796 + x6)^2) + x754 * ((
    -0.5029417013633463 + x4)^2 + (-0.4785691085999849 + x5)^2 + (
    -0.6440855384208175 + x6)^2) + x755 * ((-0.5303135807201502 + x4)^2 + (
    -0.9039824414704006 + x5)^2 + (-0.33970470843348766 + x6)^2) + x756 * ((
    -0.3002120204313121 + x4)^2 + (-0.8293923954271605 + x5)^2 + (
    -0.09736075716511139 + x6)^2) + x757 * ((-0.30009287477399993 + x4)^2 + (
    -0.8977331200619989 + x5)^2 + (-0.6790360118322567 + x6)^2) + x758 * ((
    -0.949222817147212 + x4)^2 + (-0.4475514843804891 + x5)^2 + (
    -0.38135879431065867 + x6)^2) + x759 * ((-0.2064338949319181 + x4)^2 + (
    -0.2471618264138381 + x5)^2 + (-0.33404126801805556 + x6)^2) + x760 * ((
    -0.9469532157846159 + x4)^2 + (-0.12979939471251356 + x5)^2 + (
    -0.6308532308364203 + x6)^2) + x761 * ((-0.8160024772328773 + x4)^2 + (
    -0.8192673081264756 + x5)^2 + (-0.828617395442529 + x6)^2) + x762 * ((
    -0.043698145130302235 + x4)^2 + (-0.35823212196091736 + x5)^2 + (
    -0.6536017967379447 + x6)^2) + x763 * ((-0.31599796165138205 + x4)^2 + (
    -0.14269139738795444 + x5)^2 + (-0.5083854452577903 + x6)^2) + x764 * ((
    -0.1849721541921785 + x4)^2 + (-0.9379494054807923 + x5)^2 + (
    -0.750436849143862 + x6)^2) + x765 * ((-0.2216708088282653 + x4)^2 + (
    -0.23053899815258394 + x5)^2 + (-0.18897253793934143 + x6)^2) + x766 * ((
    -0.35548760077164 + x4)^2 + (-0.2106073810351573 + x5)^2 + (
    -0.8030904658404747 + x6)^2) + x767 * ((-0.7046242974214645 + x4)^2 + (
    -0.9747362717516234 + x5)^2 + (-0.8986311370033265 + x6)^2) + x768 * ((
    -0.6930115258414592 + x4)^2 + (-0.25226679460293766 + x5)^2 + (
    -0.2620829240380018 + x6)^2) + x769 * ((-0.5416746943288492 + x4)^2 + (
    -0.3587968851453698 + x5)^2 + (-0.8014083818825035 + x6)^2) + x770 * ((
    -0.709926799469957 + x4)^2 + (-0.42600195906405547 + x5)^2 + (
    -0.2918180254572945 + x6)^2) + x771 * ((-0.3511232970881478 + x4)^2 + (
    -0.7757451672244947 + x5)^2 + (-0.7859380648395401 + x6)^2) + x772 * ((
    -0.8803653019341091 + x4)^2 + (-0.6658465100092489 + x5)^2 + (
    -0.5112371462700493 + x6)^2) + x773 * ((-0.17144800814870276 + x4)^2 + (
    -0.4122257700328378 + x5)^2 + (-0.8076682711989561 + x6)^2) + x774 * ((
    -0.717380833423112 + x4)^2 + (-0.17998680267335054 + x5)^2 + (
    -0.9060156443877393 + x6)^2) + x775 * ((-0.5878000971753468 + x4)^2 + (
    -0.18065525183423758 + x5)^2 + (-0.15538360399442397 + x6)^2) + x776 * ((
    -0.8682299280341067 + x4)^2 + (-0.16346717895652563 + x5)^2 + (
    -0.4336582517475457 + x6)^2) + x777 * ((-0.3606702369630238 + x4)^2 + (
    -0.731242129687016 + x5)^2 + (-0.12043748947308242 + x6)^2) + x778 * ((
    -0.4815500944964639 + x4)^2 + (-0.6044620193979354 + x5)^2 + (
    -0.8210071600955915 + x6)^2) + x779 * ((-0.11954313893324364 + x4)^2 + (
    -0.1323053978820773 + x5)^2 + (-0.25050555092577165 + x6)^2) + x780 * ((
    -0.08542773014575478 + x4)^2 + (-0.18503314408239213 + x5)^2 + (
    -0.9115102242077784 + x6)^2) + x781 * ((-0.8095044154907116 + x4)^2 + (
    -0.2799202631109189 + x5)^2 + (-0.2880890539271259 + x6)^2) + x782 * ((
    -0.7212219319929314 + x4)^2 + (-0.5984506061652697 + x5)^2 + (
    -0.9365245987942612 + x6)^2) + x783 * ((-0.8994684258109723 + x4)^2 + (
    -0.22641415105010199 + x5)^2 + (-0.6913162899186059 + x6)^2) + x784 * ((
    -0.6581582771778646 + x4)^2 + (-0.197316973616537 + x5)^2 + (
    -0.43619331804872796 + x6)^2) + x785 * ((-0.4739659187865559 + x4)^2 + (
    -0.38646221151733806 + x5)^2 + (-0.10770286986963273 + x6)^2) + x786 * ((
    -0.8723979336469919 + x4)^2 + (-0.32335338168956085 + x5)^2 + (
    -0.5817075590285083 + x6)^2) + x787 * ((-0.061809683762981016 + x4)^2 + (
    -0.5389217377093763 + x5)^2 + (-0.5417597560087298 + x6)^2) + x788 * ((
    -0.07422322033257833 + x4)^2 + (-0.7097672901832104 + x5)^2 + (
    -0.06915026234774257 + x6)^2) + x789 * ((-0.8280486736764958 + x4)^2 + (
    -0.04022416242938687 + x5)^2 + (-0.19882373590113933 + x6)^2) + x790 * ((
    -0.029072146364669926 + x4)^2 + (-0.09653489205822285 + x5)^2 + (
    -0.049536244543501806 + x6)^2) + x791 * ((-0.7881624249773665 + x4)^2 + (
    -0.7566784959062068 + x5)^2 + (-0.3074666055810339 + x6)^2) + x792 * ((
    -0.7152259480390857 + x4)^2 + (-0.640956553515879 + x5)^2 + (
    -0.39814612324127086 + x6)^2) + x793 * ((-0.9043657495395202 + x4)^2 + (
    -0.5252156573640178 + x5)^2 + (-0.8199524482586914 + x6)^2) + x794 * ((
    -0.8601980724291697 + x4)^2 + (-0.31860765736788654 + x5)^2 + (
    -0.9089973811459461 + x6)^2) + x795 * ((-0.2086703107751542 + x4)^2 + (
    -0.006149788315085392 + x5)^2 + (-0.21513361748683668 + x6)^2) + x796 * ((
    -0.7823136762126888 + x4)^2 + (-0.416684189371502 + x5)^2 + (
    -0.4442685591428306 + x6)^2) + x797 * ((-0.7994879189101486 + x4)^2 + (
    -0.5003588036104756 + x5)^2 + (-0.6431108825964064 + x6)^2) + x798 * ((
    -0.2010796579746258 + x4)^2 + (-0.8170704549941877 + x5)^2 + (
    -0.2175952968667264 + x6)^2) + x799 * ((-0.7094682020793405 + x4)^2 + (
    -0.49279977787280593 + x5)^2 + (-0.6972766332766551 + x6)^2) + x800 * ((
    -0.8249820076123356 + x4)^2 + (-0.7551746481371484 + x5)^2 + (
    -0.3076678852974345 + x6)^2) + x801 * ((-0.4431291732786462 + x4)^2 + (
    -0.10790569968568664 + x5)^2 + (-0.8104337482413756 + x6)^2) + x802 * ((
    -0.12547352222190156 + x4)^2 + (-0.30712330696451673 + x5)^2 + (
    -0.6443221501233987 + x6)^2) + x803 * ((-0.43521055817778886 + x4)^2 + (
    -0.11823850858772755 + x5)^2 + (-0.4245893746746593 + x6)^2) + x804 * ((
    -0.1023807175165814 + x4)^2 + (-0.023476062383137597 + x5)^2 + (
    -0.7715459665761015 + x6)^2) + x805 * ((-0.6084243314221985 + x4)^2 + (
    -0.6767723713597806 + x5)^2 + (-0.15277477018392027 + x6)^2) + x806 * ((
    -0.07758513009101076 + x4)^2 + (-0.5193945915946692 + x5)^2 + (
    -0.13605100113112523 + x6)^2) + x807 * ((-0.05076479042333726 + x4)^2 + (
    -0.7472210261556415 + x5)^2 + (-0.6187487644673069 + x6)^2) + x808 * ((
    -0.5774530190962283 + x4)^2 + (-0.4625308284849895 + x5)^2 + (
    -0.8985951405862879 + x6)^2) + x809 * ((-0.41887571010203506 + x4)^2 + (
    -0.04213576565608468 + x5)^2 + (-0.3367107300411496 + x6)^2) + x810 * ((
    -0.5346587692815016 + x4)^2 + (-0.7514755753693055 + x5)^2 + (
    -0.16512273183076165 + x6)^2) + x811 * ((-0.3673579319044816 + x4)^2 + (
    -0.4132537275282224 + x5)^2 + (-0.34757755368510646 + x6)^2) + x812 * ((
    -0.5454982366155314 + x4)^2 + (-0.573439476172685 + x5)^2 + (
    -0.33123862062087006 + x6)^2) + x813 * ((-0.23915554947791118 + x4)^2 + (
    -0.9496426713944737 + x5)^2 + (-0.9047110021009291 + x6)^2) + x814 * ((
    -0.7835998720242816 + x4)^2 + (-0.5409585492652254 + x5)^2 + (
    -0.022604618704512136 + x6)^2) + x815 * ((-0.7447675570789921 + x4)^2 + (
    -0.06306009873408058 + x5)^2 + (-0.32450967602437086 + x6)^2) + x816 * ((
    -0.957050425001801 + x4)^2 + (-0.6908648583160039 + x5)^2 + (
    -0.6977383122594122 + x6)^2) + x817 * ((-0.9643413589347215 + x4)^2 + (
    -0.8038041971590639 + x5)^2 + (-0.30694917237409114 + x6)^2) + x818 * ((
    -0.16688443645138162 + x4)^2 + (-0.5498482774651414 + x5)^2 + (
    -0.7414582280194998 + x6)^2) + x819 * ((-0.2748697607402272 + x4)^2 + (
    -0.6274376652049733 + x5)^2 + (-0.35357014233175543 + x6)^2) + x820 * ((
    -0.5891376195472661 + x4)^2 + (-0.5661076738361366 + x5)^2 + (
    -0.6533215134864436 + x6)^2) + x821 * ((-0.8392486510086273 + x4)^2 + (
    -0.3115496822184768 + x5)^2 + (-0.146703446853646 + x6)^2) + x822 * ((
    -0.3738023028456101 + x4)^2 + (-0.7106592984968659 + x5)^2 + (
    -0.7581637572990693 + x6)^2) + x823 * ((-0.2801730794814168 + x4)^2 + (
    -0.2913280058906009 + x5)^2 + (-0.10015085446802086 + x6)^2) + x824 * ((
    -0.014051212285501768 + x4)^2 + (-0.3394766298985926 + x5)^2 + (
    -0.4278429675896249 + x6)^2) + x825 * ((-0.9378558356981184 + x4)^2 + (
    -0.15127486460420836 + x5)^2 + (-0.7493436444755507 + x6)^2) + x826 * ((
    -0.8297509765027676 + x4)^2 + (-0.08177655040140464 + x5)^2 + (
    -0.4494327397424498 + x6)^2) + x827 * ((-0.11029669990558244 + x4)^2 + (
    -0.582339311840151 + x5)^2 + (-0.06415846876984466 + x6)^2) + x828 * ((
    -0.9768471346651219 + x4)^2 + (-0.39696035406710384 + x5)^2 + (
    -0.23783616802647012 + x6)^2) + x829 * ((-0.3764501911849826 + x4)^2 + (
    -0.786987541945555 + x5)^2 + (-0.2970434016308823 + x6)^2) + x830 * ((
    -0.05618205629013939 + x4)^2 + (-0.4085438120067576 + x5)^2 + (
    -0.5645644728609109 + x6)^2) + x831 * ((-0.6746539089984576 + x4)^2 + (
    -0.8329192222789586 + x5)^2 + (-0.8171355492822672 + x6)^2) + x832 * ((
    -0.929134925271013 + x4)^2 + (-0.48607691575718226 + x5)^2 + (
    -0.14496601171482326 + x6)^2) + x833 * ((-0.2888049631111739 + x4)^2 + (
    -0.45169995457478385 + x5)^2 + (-0.7415931477217647 + x6)^2) + x834 * ((
    -0.8314270362626708 + x4)^2 + (-0.09391123252252986 + x5)^2 + (
    -0.6669146426368324 + x6)^2) + x835 * ((-0.5652735801231673 + x4)^2 + (
    -0.9329767078391193 + x5)^2 + (-0.9484705315852879 + x6)^2) + x836 * ((
    -0.3380979256818256 + x4)^2 + (-0.23035046064976195 + x5)^2 + (
    -0.5278605812355041 + x6)^2) + x837 * ((-0.8184575612577757 + x4)^2 + (
    -0.9258797310665887 + x5)^2 + (-0.2046467253589157 + x6)^2) + x838 * ((
    -0.40985008510077614 + x4)^2 + (-0.4757792482569193 + x5)^2 + (
    -0.8360188587690305 + x6)^2) + x839 * ((-0.8332701786998654 + x4)^2 + (
    -0.20495368326898378 + x5)^2 + (-0.47164667394744264 + x6)^2) + x840 * ((
    -0.0643880402156024 + x4)^2 + (-0.26358735356819285 + x5)^2 + (
    -0.13167880607810734 + x6)^2) + x841 * ((-0.0025821300592889784 + x4)^2 + (
    -0.9088622869025026 + x5)^2 + (-0.04233625722670664 + x6)^2) + x842 * ((
    -0.5236600684212673 + x4)^2 + (-0.27260080288022603 + x5)^2 + (
    -0.459442267827748 + x6)^2) + x843 * ((-0.7158972098447147 + x4)^2 + (
    -0.9489828100457257 + x5)^2 + (-0.6888872017363918 + x6)^2) + x844 * ((
    -0.7865559366849096 + x4)^2 + (-0.833267039226051 + x5)^2 + (
    -0.5747950642364967 + x6)^2) + x845 * ((-0.34415199178488665 + x4)^2 + (
    -0.18091957070795228 + x5)^2 + (-0.031579899788283905 + x6)^2) + x846 * ((
    -0.14471678962846113 + x4)^2 + (-0.30241060384916396 + x5)^2 + (
    -0.059993959720591294 + x6)^2) + x847 * ((-0.6824739375029841 + x4)^2 + (
    -0.5331181892609036 + x5)^2 + (-0.977166596891582 + x6)^2) + x848 * ((
    -0.20408398166030306 + x4)^2 + (-0.5154572139955655 + x5)^2 + (
    -0.4769277180629534 + x6)^2) + x849 * ((-0.050689484148662145 + x4)^2 + (
    -0.5527672407633779 + x5)^2 + (-0.32111189487270875 + x6)^2) + x850 * ((
    -0.23154418027475898 + x4)^2 + (-0.6700805221954127 + x5)^2 + (
    -0.9666075355371924 + x6)^2) + x851 * ((-0.008868281269836076 + x4)^2 + (
    -0.6338997437715709 + x5)^2 + (-0.26544426895590223 + x6)^2) + x852 * ((
    -0.6596209708459404 + x4)^2 + (-0.40168150668415104 + x5)^2 + (
    -0.4719673790088824 + x6)^2) + x853 * ((-0.11053129063988809 + x4)^2 + (
    -0.16664026665153386 + x5)^2 + (-0.8851714055017869 + x6)^2) + x854 * ((
    -0.5258408747918166 + x4)^2 + (-0.581125730214377 + x5)^2 + (
    -0.9734757162239656 + x6)^2) + x855 * ((-0.37505520940960313 + x4)^2 + (
    -0.8756917740425001 + x5)^2 + (-0.9752391810025125 + x6)^2) + x856 * ((
    -0.47118833747162414 + x4)^2 + (-0.3893334167798458 + x5)^2 + (
    -0.008212794912485166 + x6)^2) + x857 * ((-0.6402127761953015 + x4)^2 + (
    -0.1600123713040228 + x5)^2 + (-0.44094193106669577 + x6)^2) + x858 * ((
    -0.8231471689426597 + x4)^2 + (-0.7509513915820255 + x5)^2 + (
    -0.8921027170624262 + x6)^2) + x859 * ((-0.20030064944641757 + x4)^2 + (
    -0.21962903531540312 + x5)^2 + (-0.5970473550708151 + x6)^2) + x860 * ((
    -0.902808238265977 + x4)^2 + (-0.7562726465509134 + x5)^2 + (
    -0.24813085289058312 + x6)^2) + x861 * ((-0.21843016026229212 + x4)^2 + (
    -0.8059343949692039 + x5)^2 + (-0.3752989990533576 + x6)^2) + x862 * ((
    -0.14794288425068958 + x4)^2 + (-0.31328675165643205 + x5)^2 + (
    -0.8073941583373085 + x6)^2) + x863 * ((-0.5235088791774563 + x4)^2 + (
    -0.04578915338953027 + x5)^2 + (-0.10692118625425784 + x6)^2) + x864 * ((
    -0.5791900847638172 + x4)^2 + (-0.48532053702765365 + x5)^2 + (
    -0.3885259522950011 + x6)^2) + x865 * ((-0.8920363304658884 + x4)^2 + (
    -0.5151000888985628 + x5)^2 + (-0.6346096148059661 + x6)^2) + x866 * ((
    -0.9717009075640338 + x4)^2 + (-0.9907019955601769 + x5)^2 + (
    -0.85505344837673 + x6)^2) + x867 * ((-0.34445995140187446 + x4)^2 + (
    -0.6392373435519673 + x5)^2 + (-0.7819131287560607 + x6)^2) + x868 * ((
    -0.42109376750007577 + x4)^2 + (-0.7284707401745129 + x5)^2 + (
    -0.11077465817504761 + x6)^2) + x869 * ((-0.925635401235069 + x4)^2 + (
    -0.5685890877714631 + x5)^2 + (-0.9462095752137067 + x6)^2) + x870 * ((
    -0.7279111798696564 + x4)^2 + (-0.15487285858439592 + x5)^2 + (
    -0.7608763017869555 + x6)^2) + x871 * ((-0.12654655247031799 + x4)^2 + (
    -0.09026002005416467 + x5)^2 + (-0.8883114041715482 + x6)^2) + x872 * ((
    -0.6585295603176656 + x4)^2 + (-0.5624166650475771 + x5)^2 + (
    -0.5547559478222932 + x6)^2) + x873 * ((-0.24575106742741626 + x4)^2 + (
    -0.3042728268888242 + x5)^2 + (-0.896812031612661 + x6)^2) + x874 * ((
    -0.4606211642264276 + x4)^2 + (-0.5593289076408292 + x5)^2 + (
    -0.9885975772390854 + x6)^2) + x875 * ((-0.7347225956683001 + x4)^2 + (
    -0.5745816301727896 + x5)^2 + (-0.009825540222648477 + x6)^2) + x876 * ((
    -0.9978369871406716 + x4)^2 + (-0.9420017543770447 + x5)^2 + (
    -0.9484212753820023 + x6)^2) + x877 * ((-0.6579730335184849 + x4)^2 + (
    -0.01651993788019801 + x5)^2 + (-0.763022957071984 + x6)^2) + x878 * ((
    -0.9947489651588863 + x4)^2 + (-0.3224606084126759 + x5)^2 + (
    -0.7750668635617214 + x6)^2) + x879 * ((-0.17582348854944607 + x4)^2 + (
    -0.17352822759146402 + x5)^2 + (-0.22743984463314282 + x6)^2) + x880 * ((
    -0.4758203537795964 + x4)^2 + (-0.40834392828261223 + x5)^2 + (
    -0.05261570014523109 + x6)^2) + x881 * ((-0.36204048569723735 + x4)^2 + (
    -0.8641293232884356 + x5)^2 + (-0.1489285988376965 + x6)^2) + x882 * ((
    -0.6008467842262206 + x4)^2 + (-0.9039149091831002 + x5)^2 + (
    -0.36931294088336475 + x6)^2) + x883 * ((-0.030067960172246666 + x4)^2 + (
    -0.48471288146931457 + x5)^2 + (-0.5753432715823008 + x6)^2) + x884 * ((
    -0.1270532869152421 + x4)^2 + (-0.20492488058927516 + x5)^2 + (
    -0.2920819764108209 + x6)^2) + x885 * ((-0.057643356995719985 + x4)^2 + (
    -0.4024951698758521 + x5)^2 + (-0.5345507589362359 + x6)^2) + x886 * ((
    -0.9581878087034774 + x4)^2 + (-0.0800210963738257 + x5)^2 + (
    -0.677382890669299 + x6)^2) + x887 * ((-0.2047868034464274 + x4)^2 + (
    -0.7755295931481812 + x5)^2 + (-0.07132945936635726 + x6)^2) + x888 * ((
    -0.7829343091571344 + x4)^2 + (-0.8105545574565635 + x5)^2 + (
    -0.4991231549422569 + x6)^2) + x889 * ((-0.6258463311430302 + x4)^2 + (
    -0.5496595671750402 + x5)^2 + (-0.19154029772231573 + x6)^2) + x890 * ((
    -0.0272793485028624 + x4)^2 + (-0.011791358057427925 + x5)^2 + (
    -0.8057574736716172 + x6)^2) + x891 * ((-0.5414890284796168 + x4)^2 + (
    -0.945016615830951 + x5)^2 + (-0.8798725595210737 + x6)^2) + x892 * ((
    -0.05119780537656027 + x4)^2 + (-0.5031403231758489 + x5)^2 + (
    -0.11523583178307628 + x6)^2) + x893 * ((-0.27464505675722395 + x4)^2 + (
    -0.05754985857648509 + x5)^2 + (-0.1718986943714379 + x6)^2) + x894 * ((
    -0.563384014973976 + x4)^2 + (-0.4102870005309007 + x5)^2 + (
    -0.44867061677598474 + x6)^2) + x895 * ((-0.9554091045415013 + x4)^2 + (
    -0.3287768838698092 + x5)^2 + (-0.5079007221884251 + x6)^2) + x896 * ((
    -0.049015869567574866 + x4)^2 + (-0.7117888163278766 + x5)^2 + (
    -0.8523074296825538 + x6)^2) + x897 * ((-0.30979077869124183 + x4)^2 + (
    -0.4417160550189484 + x5)^2 + (-0.3302755586589736 + x6)^2) + x898 * ((
    -0.5591781894268806 + x4)^2 + (-0.8026089339206316 + x5)^2 + (
    -0.3713319195580873 + x6)^2) + x899 * ((-0.5840605834977219 + x4)^2 + (
    -0.4911685585761769 + x5)^2 + (-0.1816408065331926 + x6)^2) + x900 * ((
    -0.699915228142964 + x4)^2 + (-0.6846783090644426 + x5)^2 + (
    -0.5574598140568765 + x6)^2) + x901 * ((-0.6753730740440026 + x4)^2 + (
    -0.5489318129908483 + x5)^2 + (-0.10199137240931655 + x6)^2) + x902 * ((
    -0.11104797679961531 + x4)^2 + (-0.5472557486726254 + x5)^2 + (
    -0.9571846144505868 + x6)^2) + x903 * ((-0.4290104355078601 + x4)^2 + (
    -0.500625748131909 + x5)^2 + (-0.839875855861129 + x6)^2) + x904 * ((
    -0.8284104784524099 + x4)^2 + (-0.15168224190165258 + x5)^2 + (
    -0.7425205829813807 + x6)^2) + x905 * ((-0.7835845824065171 + x4)^2 + (
    -0.43892942409165736 + x5)^2 + (-0.9672883708633824 + x6)^2) + x906 * ((
    -0.9658474371081412 + x4)^2 + (-0.24521502946450435 + x5)^2 + (
    -0.19958521141831587 + x6)^2) + x907 * ((-0.6763699518851537 + x4)^2 + (
    -0.40784932714190725 + x5)^2 + (-0.9693530161050696 + x6)^2) + x908 * ((
    -0.015390131891825365 + x4)^2 + (-0.14588925853081935 + x5)^2 + (
    -0.5718899821316975 + x6)^2) + x909 * ((-0.6550458977158515 + x4)^2 + (
    -0.8097929221347935 + x5)^2 + (-0.4104406395267636 + x6)^2) + x910 * ((
    -0.7508103873205083 + x4)^2 + (-0.11532102750991224 + x5)^2 + (
    -0.6478368645129094 + x6)^2) + x911 * ((-0.9737229810910403 + x4)^2 + (
    -0.5163950909606659 + x5)^2 + (-0.6367061240819752 + x6)^2) + x912 * ((
    -0.5984140542435419 + x4)^2 + (-0.18984363054369258 + x5)^2 + (
    -0.027452684972157693 + x6)^2) + x913 * ((-0.9243666020019815 + x4)^2 + (
    -0.8145037925176214 + x5)^2 + (-0.6578177936970774 + x6)^2) + x914 * ((
    -0.9251327852082893 + x4)^2 + (-0.02218555315317494 + x5)^2 + (
    -0.4723664720086945 + x6)^2) + x915 * ((-0.6010677075600663 + x4)^2 + (
    -0.864007697540581 + x5)^2 + (-0.9271036737422498 + x6)^2) + x916 * ((
    -0.656591717593777 + x4)^2 + (-0.5134881016753086 + x5)^2 + (
    -0.1883008481102213 + x6)^2) + x917 * ((-0.7407314335715345 + x4)^2 + (
    -0.25458554896989405 + x5)^2 + (-0.556216069468436 + x6)^2) + x918 * ((
    -0.5120359138328312 + x4)^2 + (-0.8101978116075103 + x5)^2 + (
    -0.46638781967369414 + x6)^2) + x919 * ((-0.7135334348392973 + x4)^2 + (
    -0.1779541525794096 + x5)^2 + (-0.6317024521479767 + x6)^2) + x920 * ((
    -0.24177429627919167 + x4)^2 + (-0.6370581745682193 + x5)^2 + (
    -0.2710238175551406 + x6)^2) + x921 * ((-0.9997913560034266 + x4)^2 + (
    -0.48490318564542456 + x5)^2 + (-0.4160988220639955 + x6)^2) + x922 * ((
    -0.15980278916475676 + x4)^2 + (-0.06407095445485222 + x5)^2 + (
    -0.7249348271199497 + x6)^2) + x923 * ((-0.1411868189363079 + x4)^2 + (
    -0.3067431553565323 + x5)^2 + (-0.78575462849935 + x6)^2) + x924 * ((
    -0.5478827352853459 + x4)^2 + (-0.20291790816221889 + x5)^2 + (
    -0.8761980800539626 + x6)^2) + x925 * ((-0.9066224120947074 + x4)^2 + (
    -0.9518140343960166 + x5)^2 + (-0.5195535652548422 + x6)^2) + x926 * ((
    -0.4944497764703105 + x4)^2 + (-0.526178861965796 + x5)^2 + (
    -0.558537222910955 + x6)^2) + x927 * ((-0.2726667055675822 + x4)^2 + (
    -0.9345746694586428 + x5)^2 + (-0.8532831802582073 + x6)^2) + x928 * ((
    -0.9948056415771968 + x4)^2 + (-0.946100723693632 + x5)^2 + (
    -0.07095119487224366 + x6)^2) + x929 * ((-0.5213951586103635 + x4)^2 + (
    -0.8407112340244879 + x5)^2 + (-0.27895325936062443 + x6)^2) + x930 * ((
    -0.21494505782936268 + x4)^2 + (-0.7765096743882861 + x5)^2 + (
    -0.10254422951176734 + x6)^2) + x931 * ((-0.7120472016233632 + x4)^2 + (
    -0.49718927750005937 + x5)^2 + (-0.7541840771418643 + x6)^2) + x932 * ((
    -0.9685028423332537 + x4)^2 + (-0.5335345784258086 + x5)^2 + (
    -0.9890747374850164 + x6)^2) + x933 * ((-0.9230166234673173 + x4)^2 + (
    -0.6518475605727765 + x5)^2 + (-0.734854155976083 + x6)^2) + x934 * ((
    -0.06708623533817104 + x4)^2 + (-0.20172244637746983 + x5)^2 + (
    -0.2768060696570147 + x6)^2) + x935 * ((-0.4038888086617314 + x4)^2 + (
    -0.1486875332810369 + x5)^2 + (-0.0864364601708697 + x6)^2) + x936 * ((
    -0.4517085118551507 + x4)^2 + (-0.7765791454898151 + x5)^2 + (
    -0.18690810700205485 + x6)^2) + x937 * ((-0.6984051043122955 + x4)^2 + (
    -0.6903189697467437 + x5)^2 + (-0.040778131010728136 + x6)^2) + x938 * ((
    -0.6072448401148461 + x4)^2 + (-0.6438420452394027 + x5)^2 + (
    -0.6872356318162963 + x6)^2) + x939 * ((-0.3156326593340355 + x4)^2 + (
    -0.6507808794562617 + x5)^2 + (-0.6233647448682074 + x6)^2) + x940 * ((
    -0.4002818200993541 + x4)^2 + (-0.8997180632997818 + x5)^2 + (
    -0.14412431069924558 + x6)^2) + x941 * ((-0.4603826538409851 + x4)^2 + (
    -0.04233386015418239 + x5)^2 + (-0.7043950613308216 + x6)^2) + x942 * ((
    -0.870614516134697 + x4)^2 + (-0.8580337696409851 + x5)^2 + (
    -0.21857975143254016 + x6)^2) + x943 * ((-0.7885802541502687 + x4)^2 + (
    -0.983116728066409 + x5)^2 + (-0.6268381409191566 + x6)^2) + x944 * ((
    -0.453360688390823 + x4)^2 + (-0.17721212922523033 + x5)^2 + (
    -0.11369558618207087 + x6)^2) + x945 * ((-0.37622468340220194 + x4)^2 + (
    -0.10891294174292976 + x5)^2 + (-0.1499013005008839 + x6)^2) + x946 * ((
    -0.5160385921656351 + x4)^2 + (-0.5123193711182501 + x5)^2 + (
    -0.14661208983716012 + x6)^2) + x947 * ((-0.8318749644250042 + x4)^2 + (
    -0.9474430577714092 + x5)^2 + (-0.627935164487112 + x6)^2) + x948 * ((
    -0.1903852263517427 + x4)^2 + (-0.11470061584083246 + x5)^2 + (
    -0.44132933622437875 + x6)^2) + x949 * ((-0.7139609443452906 + x4)^2 + (
    -0.1662593335896707 + x5)^2 + (-0.206132946290832 + x6)^2) + x950 * ((
    -0.9287584108347345 + x4)^2 + (-0.4364542232297094 + x5)^2 + (
    -0.15930282013429242 + x6)^2) + x951 * ((-0.5438534099357585 + x4)^2 + (
    -0.6713389990511793 + x5)^2 + (-0.7515358561055495 + x6)^2) + x952 * ((
    -0.7953709431284481 + x4)^2 + (-0.09365706610576408 + x5)^2 + (
    -0.4729038737092427 + x6)^2) + x953 * ((-0.6834981451581077 + x4)^2 + (
    -0.5907013715726769 + x5)^2 + (-0.2177451536406989 + x6)^2) + x954 * ((
    -0.4631935234349823 + x4)^2 + (-0.8803533185868815 + x5)^2 + (
    -0.4273859435332188 + x6)^2) + x955 * ((-0.476785780348992 + x4)^2 + (
    -0.8869187769611843 + x5)^2 + (-0.7193029869652928 + x6)^2) + x956 * ((
    -0.31718143038215174 + x4)^2 + (-0.3262335948033561 + x5)^2 + (
    -0.9602949324145322 + x6)^2) + x957 * ((-0.5936199239050312 + x4)^2 + (
    -0.49552398966064715 + x5)^2 + (-0.49848694537003924 + x6)^2) + x958 * ((
    -0.9296199597347767 + x4)^2 + (-0.40889365057397287 + x5)^2 + (
    -0.8011545277509335 + x6)^2) + x959 * ((-0.7354055208486365 + x4)^2 + (
    -0.7799949232677478 + x5)^2 + (-0.22209643149708758 + x6)^2) + x960 * ((
    -0.8285174050295658 + x4)^2 + (-0.3399361044291944 + x5)^2 + (
    -0.5417626971057434 + x6)^2) + x961 * ((-0.4743970301387661 + x4)^2 + (
    -0.03968268525091545 + x5)^2 + (-0.7676276502511942 + x6)^2) + x962 * ((
    -0.9658526833599206 + x4)^2 + (-0.7769012618207594 + x5)^2 + (
    -0.30599222118777814 + x6)^2) + x963 * ((-0.48754823079065357 + x4)^2 + (
    -0.7322449135727448 + x5)^2 + (-0.6492327824562298 + x6)^2) + x964 * ((
    -0.9362650053761248 + x4)^2 + (-0.04268520093465755 + x5)^2 + (
    -0.7467628080743383 + x6)^2) + x965 * ((-0.9307916870383665 + x4)^2 + (
    -0.961756532300574 + x5)^2 + (-0.2155280011227615 + x6)^2) + x966 * ((
    -0.08912615918233224 + x4)^2 + (-0.6471821111714566 + x5)^2 + (
    -0.9913586544218587 + x6)^2) + x967 * ((-0.8358554991679754 + x4)^2 + (
    -0.08929161317162748 + x5)^2 + (-0.9647833465957737 + x6)^2) + x968 * ((
    -0.6273718862494942 + x4)^2 + (-0.7618805895251419 + x5)^2 + (
    -0.492165897853857 + x6)^2) + x969 * ((-0.6702555245476077 + x4)^2 + (
    -0.3610395370884728 + x5)^2 + (-0.766937565344216 + x6)^2) + x970 * ((
    -0.27485794231769844 + x4)^2 + (-0.5215206202220081 + x5)^2 + (
    -0.4889642491896449 + x6)^2) + x971 * ((-0.8463263789396861 + x4)^2 + (
    -0.4936221195625502 + x5)^2 + (-0.5709411193324385 + x6)^2) + x972 * ((
    -0.8054668308765568 + x4)^2 + (-0.2115365899248064 + x5)^2 + (
    -0.11566470511829063 + x6)^2) + x973 * ((-0.1943614935785951 + x4)^2 + (
    -0.8334718657316503 + x5)^2 + (-0.44326977139831436 + x6)^2) + x974 * ((
    -0.19480034368816324 + x4)^2 + (-0.8110564747660595 + x5)^2 + (
    -0.14302925781111175 + x6)^2) + x975 * ((-0.39190211653261664 + x4)^2 + (
    -0.9677972762274933 + x5)^2 + (-0.16271262210127324 + x6)^2) + x976 * ((
    -0.06731580772013712 + x4)^2 + (-0.6169831213923005 + x5)^2 + (
    -0.4027335514273457 + x6)^2) + x977 * ((-0.38110974958221877 + x4)^2 + (
    -0.519046146671436 + x5)^2 + (-0.5738902625301048 + x6)^2) + x978 * ((
    -0.9422399729911471 + x4)^2 + (-0.7184320029483544 + x5)^2 + (
    -0.9650701664096555 + x6)^2) + x979 * ((-0.36801794166483814 + x4)^2 + (
    -0.9368906012991046 + x5)^2 + (-0.75121049110894 + x6)^2) + x980 * ((
    -0.6630092172211279 + x4)^2 + (-0.20322311031211582 + x5)^2 + (
    -0.2887465568222305 + x6)^2) + x981 * ((-0.9706981704650441 + x4)^2 + (
    -0.08466082082361082 + x5)^2 + (-0.7247467660352114 + x6)^2) + x982 * ((
    -0.21059963791910552 + x4)^2 + (-0.49165647268816803 + x5)^2 + (
    -0.5804191839003714 + x6)^2) + x983 * ((-0.5236356611629658 + x4)^2 + (
    -0.07814696537946009 + x5)^2 + (-0.3132490429219894 + x6)^2) + x984 * ((
    -0.5026192836790041 + x4)^2 + (-0.6894528769723671 + x5)^2 + (
    -0.10662506884779244 + x6)^2) + x985 * ((-0.680171254701243 + x4)^2 + (
    -0.8794858932580393 + x5)^2 + (-0.1970105609325069 + x6)^2) + x986 * ((
    -0.653168096390829 + x4)^2 + (-0.8220713223404621 + x5)^2 + (
    -0.23312137565276492 + x6)^2) + x987 * ((-0.5945786510272542 + x4)^2 + (
    -0.6937129033829035 + x5)^2 + (-0.4629130124432773 + x6)^2) + x988 * ((
    -0.7366695477198858 + x4)^2 + (-0.10570699646360726 + x5)^2 + (
    -0.18565469991974215 + x6)^2) + x989 * ((-0.18743250673347933 + x4)^2 + (
    -0.8501799346529197 + x5)^2 + (-0.4455750149410902 + x6)^2) + x990 * ((
    -0.9211896892234244 + x4)^2 + (-0.8366465654279776 + x5)^2 + (
    -0.6201388866517694 + x6)^2) + x991 * ((-0.9891510966919514 + x4)^2 + (
    -0.6966082529523953 + x5)^2 + (-0.8133151377521731 + x6)^2) + x992 * ((
    -0.3902817623451159 + x4)^2 + (-0.24248773138219448 + x5)^2 + (
    -0.08078100456813775 + x6)^2) + x993 * ((-0.4298108705942121 + x4)^2 + (
    -0.45161887902165165 + x5)^2 + (-0.08388435410245021 + x6)^2) + x994 * ((
    -0.9073003783666486 + x4)^2 + (-0.48327373078316493 + x5)^2 + (
    -0.9910483026571903 + x6)^2) + x995 * ((-0.881651726906589 + x4)^2 + (
    -0.30048516094118216 + x5)^2 + (-0.9850698876652512 + x6)^2) + x996 * ((
    -0.6155649805033343 + x4)^2 + (-0.9348653805805935 + x5)^2 + (
    -0.6155415203207966 + x6)^2) + x997 * ((-0.8117253444866105 + x4)^2 + (
    -0.3734646122935913 + x5)^2 + (-0.5139722294737984 + x6)^2) + x998 * ((
    -0.3617901273059859 + x4)^2 + (-0.7565593293567897 + x5)^2 + (
    -0.8940449377670764 + x6)^2) + x999 * ((-0.9436103266245361 + x4)^2 + (
    -0.6770001466142013 + x5)^2 + (-0.7668347302572115 + x6)^2) + x1000 * ((
    -0.4586541642719659 + x4)^2 + (-0.3840420830379708 + x5)^2 + (
    -0.6950693649611718 + x6)^2) + x1001 * ((-0.7400622139264225 + x4)^2 + (
    -0.027543445911217934 + x5)^2 + (-0.3504023093298636 + x6)^2) + x1002 * ((
    -0.8166839507821746 + x4)^2 + (-0.6985979465781534 + x5)^2 + (
    -0.136976908632233 + x6)^2) + x1003 * ((-0.7247676574408647 + x4)^2 + (
    -0.7156252081799882 + x5)^2 + (-0.28421024086039204 + x6)^2) + x1004 * ((
    -0.7116565008996277 + x4)^2 + (-0.19186706642009876 + x5)^2 + (
    -0.8309997111931379 + x6)^2) + x1005 * ((-0.2257396195230682 + x4)^2 + (
    -0.14303777575075283 + x5)^2 + (-0.4801497799483495 + x6)^2) + x1006 * ((
    -0.22699001220690018 + x4)^2 + (-0.28790414124402386 + x5)^2 + (
    -0.11035865916965082 + x6)^2) + x1007 * ((-0.22002870473769487 + x4)^2 + (
    -0.5487022693999476 + x5)^2 + (-0.9866104667343789 + x6)^2) + x1008 * ((
    -0.9091749596489073 + x4)^2 + (-0.34548122583324925 + x5)^2 + (
    -0.42621254666086883 + x6)^2) + x1009 * ((-0.6236740823858687 + x4)^2 + (
    -0.9129273253173751 + x5)^2 + (-0.5002652562779129 + x6)^2) + x1010 * ((
    -0.4640463436541785 + x7)^2 + (-0.1293137886728929 + x8)^2 + (
    -0.1717745705908742 + x9)^2) + x1011 * ((-0.1099965161408738 + x7)^2 + (
    -0.7288891997489471 + x8)^2 + (-0.5812974922633755 + x9)^2) + x1012 * ((
    -0.6918497277391157 + x7)^2 + (-0.20973658549886454 + x8)^2 + (
    -0.9916376137682873 + x9)^2) + x1013 * ((-0.10214895121638168 + x7)^2 + (
    -0.4471617317045655 + x8)^2 + (-0.16723720460096436 + x9)^2) + x1014 * ((
    -0.6359500594742937 + x7)^2 + (-0.26061637443601726 + x8)^2 + (
    -0.2816795076287437 + x9)^2) + x1015 * ((-0.25944505466517365 + x7)^2 + (
    -0.2692384663732923 + x8)^2 + (-0.8325610020895001 + x9)^2) + x1016 * ((
    -0.6284388376892046 + x7)^2 + (-0.35949079717409593 + x8)^2 + (
    -0.07225999789103066 + x9)^2) + x1017 * ((-0.16701728419415074 + x7)^2 + (
    -0.9347771993757961 + x8)^2 + (-0.7666223410197908 + x9)^2) + x1018 * ((
    -0.4221693374712633 + x7)^2 + (-0.9535156771220886 + x8)^2 + (
    -0.7574192303318398 + x9)^2) + x1019 * ((-0.3448801407104496 + x7)^2 + (
    -0.8832949398016634 + x8)^2 + (-0.662248567565667 + x9)^2) + x1020 * ((
    -0.084155570651406 + x7)^2 + (-0.17890412424092283 + x8)^2 + (
    -0.17388950075062537 + x9)^2) + x1021 * ((-0.3916313023443915 + x7)^2 + (
    -0.019818007213793787 + x8)^2 + (-0.4569740922310289 + x9)^2) + x1022 * ((
    -0.43181385423845964 + x7)^2 + (-0.6207687709011839 + x8)^2 + (
    -0.8592520589918983 + x9)^2) + x1023 * ((-0.6487284790511446 + x7)^2 + (
    -0.7777238632207397 + x8)^2 + (-0.754096902035809 + x9)^2) + x1024 * ((
    -0.8220434639163084 + x7)^2 + (-0.3741317795920437 + x8)^2 + (
    -0.8521093203138362 + x9)^2) + x1025 * ((-0.7925713002121476 + x7)^2 + (
    -0.6036194154368819 + x8)^2 + (-0.8738614104363204 + x9)^2) + x1026 * ((
    -0.5277139763548169 + x7)^2 + (-0.1993819110558287 + x8)^2 + (
    -0.5740216578606483 + x9)^2) + x1027 * ((-0.41586747380620337 + x7)^2 + (
    -0.42388302044291193 + x8)^2 + (-0.2343053950781021 + x9)^2) + x1028 * ((
    -0.5023781980401871 + x7)^2 + (-0.03818303029571113 + x8)^2 + (
    -0.6686132837122916 + x9)^2) + x1029 * ((-0.6771457634322402 + x7)^2 + (
    -0.670453003754532 + x8)^2 + (-0.7277047293890516 + x9)^2) + x1030 * ((
    -0.21786809597676893 + x7)^2 + (-0.08609770624017898 + x8)^2 + (
    -0.5475714527010952 + x9)^2) + x1031 * ((-0.49880230295506545 + x7)^2 + (
    -0.1221804789346802 + x8)^2 + (-0.6985432568115264 + x9)^2) + x1032 * ((
    -0.8088595862488974 + x7)^2 + (-0.32195887839650494 + x8)^2 + (
    -0.03760891748311046 + x9)^2) + x1033 * ((-0.32995615684874324 + x7)^2 + (
    -0.3886013644913259 + x8)^2 + (-0.8469692211045076 + x9)^2) + x1034 * ((
    -0.28669724151775544 + x7)^2 + (-0.7807597500251693 + x8)^2 + (
    -0.25528553923429653 + x9)^2) + x1035 * ((-0.9488635103141098 + x7)^2 + (
    -0.43736211954180315 + x8)^2 + (-0.5982886678243227 + x9)^2) + x1036 * ((
    -0.4466622010152166 + x7)^2 + (-0.6090348194282511 + x8)^2 + (
    -0.8670075403112468 + x9)^2) + x1037 * ((-0.951037074725791 + x7)^2 + (
    -0.1407161090628133 + x8)^2 + (-0.13092171611554282 + x9)^2) + x1038 * ((
    -0.5541921779696605 + x7)^2 + (-0.8135752021382663 + x8)^2 + (
    -0.3027451108170902 + x9)^2) + x1039 * ((-0.5305963246394046 + x7)^2 + (
    -0.23800490595118307 + x8)^2 + (-0.6735380224500424 + x9)^2) + x1040 * ((
    -0.5909678409002741 + x7)^2 + (-0.48993330795236645 + x8)^2 + (
    -0.678288644059539 + x9)^2) + x1041 * ((-0.43028464262572896 + x7)^2 + (
    -0.18942101979564563 + x8)^2 + (-0.5387520132500516 + x9)^2) + x1042 * ((
    -0.9240763867641095 + x7)^2 + (-0.626146721604441 + x8)^2 + (
    -0.6874440043145749 + x9)^2) + x1043 * ((-0.8160616417563322 + x7)^2 + (
    -0.8985769697407207 + x8)^2 + (-0.7069074935285429 + x9)^2) + x1044 * ((
    -0.70100419051915 + x7)^2 + (-0.4569577862776859 + x8)^2 + (
    -0.1471193271794946 + x9)^2) + x1045 * ((-0.4285718440951606 + x7)^2 + (
    -0.8609883932856427 + x8)^2 + (-0.1410876060058085 + x9)^2) + x1046 * ((
    -0.6332293940657829 + x7)^2 + (-0.8525493047471094 + x8)^2 + (
    -0.7321100368238428 + x9)^2) + x1047 * ((-0.29503916007091424 + x7)^2 + (
    -0.4380701575264203 + x8)^2 + (-0.820365575773603 + x9)^2) + x1048 * ((
    -0.23227503662891036 + x7)^2 + (-0.05055428546369656 + x8)^2 + (
    -0.14176384941021558 + x9)^2) + x1049 * ((-0.5635448791654668 + x7)^2 + (
    -0.3059173029907377 + x8)^2 + (-0.737377855421216 + x9)^2) + x1050 * ((
    -0.22436900298779006 + x7)^2 + (-0.5838557597663682 + x8)^2 + (
    -0.12681037493434544 + x9)^2) + x1051 * ((-0.36240169855712956 + x7)^2 + (
    -0.04857443538763084 + x8)^2 + (-0.9860358791315034 + x9)^2) + x1052 * ((
    -0.08195695254594337 + x7)^2 + (-0.18885105382104828 + x8)^2 + (
    -0.8027553727917437 + x9)^2) + x1053 * ((-0.3963885195949204 + x7)^2 + (
    -0.3241632475929923 + x8)^2 + (-0.853275456923333 + x9)^2) + x1054 * ((
    -0.5908438916261783 + x7)^2 + (-0.7950112790507812 + x8)^2 + (
    -0.32740880277441486 + x9)^2) + x1055 * ((-0.8432432133553496 + x7)^2 + (
    -0.05282798148772461 + x8)^2 + (-0.45546519649801565 + x9)^2) + x1056 * ((
    -0.42236971119841793 + x7)^2 + (-0.8947757440038225 + x8)^2 + (
    -0.4695709175424789 + x9)^2) + x1057 * ((-0.8247942497549123 + x7)^2 + (
    -0.5014330359845784 + x8)^2 + (-0.7470113565382576 + x9)^2) + x1058 * ((
    -0.48834453204993566 + x7)^2 + (-0.5215169837629428 + x8)^2 + (
    -0.6466473117603931 + x9)^2) + x1059 * ((-0.5539921888753628 + x7)^2 + (
    -0.3015288028980093 + x8)^2 + (-0.7614340990080889 + x9)^2) + x1060 * ((
    -0.13405913842449635 + x7)^2 + (-0.010282913789367076 + x8)^2 + (
    -0.47341317441006114 + x9)^2) + x1061 * ((-0.4844169330601604 + x7)^2 + (
    -0.6930522779489291 + x8)^2 + (-0.7621495736478611 + x9)^2) + x1062 * ((
    -0.7740308764454359 + x7)^2 + (-0.03729224901817285 + x8)^2 + (
    -0.060792495607531416 + x9)^2) + x1063 * ((-0.43017611384019483 + x7)^2 + (
    -0.7275353979377646 + x8)^2 + (-0.11228956220406072 + x9)^2) + x1064 * ((
    -0.730207310114505 + x7)^2 + (-0.9753557541190604 + x8)^2 + (
    -0.046876482359277216 + x9)^2) + x1065 * ((-0.24388528239994156 + x7)^2 + (
    -0.8253598309798788 + x8)^2 + (-0.5495236414774879 + x9)^2) + x1066 * ((
    -0.9122699869151167 + x7)^2 + (-0.31915757121431776 + x8)^2 + (
    -0.7372813637720362 + x9)^2) + x1067 * ((-0.7238338524735144 + x7)^2 + (
    -0.05489659548168713 + x8)^2 + (-0.3744471629501799 + x9)^2) + x1068 * ((
    -0.7639916865325218 + x7)^2 + (-0.37213335483670207 + x8)^2 + (
    -0.15924084004650396 + x9)^2) + x1069 * ((-0.02038252676112806 + x7)^2 + (
    -0.6941311922925457 + x8)^2 + (-0.8152379226615076 + x9)^2) + x1070 * ((
    -0.2834980659872919 + x7)^2 + (-0.098062561074025 + x8)^2 + (
    -0.09504713494440098 + x9)^2) + x1071 * ((-0.5777263686540078 + x7)^2 + (
    -0.6553186629601886 + x8)^2 + (-0.10852708184066717 + x9)^2) + x1072 * ((
    -0.0504906548870141 + x7)^2 + (-0.01801577482327177 + x8)^2 + (
    -0.7073392283503382 + x9)^2) + x1073 * ((-0.7320511478522743 + x7)^2 + (
    -0.2419803614589029 + x8)^2 + (-0.6026607994765517 + x9)^2) + x1074 * ((
    -0.9681953946844297 + x7)^2 + (-0.6220011693963317 + x8)^2 + (
    -0.9192154721620333 + x9)^2) + x1075 * ((-0.7449798611870608 + x7)^2 + (
    -0.618779704147399 + x8)^2 + (-0.9908068620931784 + x9)^2) + x1076 * ((
    -0.04656000736284627 + x7)^2 + (-0.7622587439775123 + x8)^2 + (
    -0.5444825165905486 + x9)^2) + x1077 * ((-0.5304149849270671 + x7)^2 + (
    -0.7853544629150807 + x8)^2 + (-0.6650413115686411 + x9)^2) + x1078 * ((
    -0.4316006167167099 + x7)^2 + (-0.9564410998503826 + x8)^2 + (
    -0.2754654244349003 + x9)^2) + x1079 * ((-0.8192654145647627 + x7)^2 + (
    -0.3449960317441789 + x8)^2 + (-0.4639588553586419 + x9)^2) + x1080 * ((
    -0.4202896905773047 + x7)^2 + (-0.4903100277526028 + x8)^2 + (
    -0.4508730801904217 + x9)^2) + x1081 * ((-0.7839805319619787 + x7)^2 + (
    -0.07624343650513432 + x8)^2 + (-0.010490453443519732 + x9)^2) + x1082 * ((
    -0.716640229430628 + x7)^2 + (-0.3191301181101275 + x8)^2 + (
    -0.24084475450576515 + x9)^2) + x1083 * ((-0.48973960110221293 + x7)^2 + (
    -0.19400622702592318 + x8)^2 + (-0.5586480098172433 + x9)^2) + x1084 * ((
    -0.25765000251075176 + x7)^2 + (-0.3991120430135222 + x8)^2 + (
    -0.624261591485904 + x9)^2) + x1085 * ((-0.2102936857169334 + x7)^2 + (
    -0.6048029406652995 + x8)^2 + (-0.527925854621275 + x9)^2) + x1086 * ((
    -0.1418787545905994 + x7)^2 + (-0.0774930390726144 + x8)^2 + (
    -0.0249724785862947 + x9)^2) + x1087 * ((-0.034877726496859385 + x7)^2 + (
    -0.6319560857501643 + x8)^2 + (-0.7242772960087813 + x9)^2) + x1088 * ((
    -0.9433129608773202 + x7)^2 + (-0.3736070884724113 + x8)^2 + (
    -0.92947567244536 + x9)^2) + x1089 * ((-0.19723347065034202 + x7)^2 + (
    -0.5757655498584185 + x8)^2 + (-0.4442676556771823 + x9)^2) + x1090 * ((
    -0.08053094633012514 + x7)^2 + (-0.49597290071491906 + x8)^2 + (
    -0.68982692206069 + x9)^2) + x1091 * ((-0.7371912517400753 + x7)^2 + (
    -0.4111907705168256 + x8)^2 + (-0.44596226596462496 + x9)^2) + x1092 * ((
    -0.46785953968803606 + x7)^2 + (-0.45341953773271215 + x8)^2 + (
    -0.7283106962836612 + x9)^2) + x1093 * ((-0.8261694191695272 + x7)^2 + (
    -0.41472831889096884 + x8)^2 + (-0.9106938093148554 + x9)^2) + x1094 * ((
    -0.44683645298814745 + x7)^2 + (-0.6996104890042156 + x8)^2 + (
    -0.066679930798903 + x9)^2) + x1095 * ((-0.9366613572848865 + x7)^2 + (
    -0.42199403399468605 + x8)^2 + (-0.10350991187036918 + x9)^2) + x1096 * ((
    -0.9730815838375089 + x7)^2 + (-0.6831147433040942 + x8)^2 + (
    -0.09074649263643031 + x9)^2) + x1097 * ((-0.19241596788927118 + x7)^2 + (
    -0.47076401046441096 + x8)^2 + (-0.15843960550460512 + x9)^2) + x1098 * ((
    -0.04999694084986828 + x7)^2 + (-0.43552364112098474 + x8)^2 + (
    -0.317689183487498 + x9)^2) + x1099 * ((-0.7805202520309815 + x7)^2 + (
    -0.07439424045077114 + x8)^2 + (-0.11817215106111634 + x9)^2) + x1100 * ((
    -0.35732353691638374 + x7)^2 + (-0.729905338698986 + x8)^2 + (
    -0.5100765758088116 + x9)^2) + x1101 * ((-0.4780015271753969 + x7)^2 + (
    -0.192158490869756 + x8)^2 + (-0.01693000121269117 + x9)^2) + x1102 * ((
    -0.781318913473494 + x7)^2 + (-0.25445440893640614 + x8)^2 + (
    -0.7752207968553286 + x9)^2) + x1103 * ((-0.8343131584256498 + x7)^2 + (
    -0.2904065598498118 + x8)^2 + (-0.44278123600229036 + x9)^2) + x1104 * ((
    -0.9639849716170581 + x7)^2 + (-0.15550942759340902 + x8)^2 + (
    -0.12539074143986528 + x9)^2) + x1105 * ((-0.9221783343065362 + x7)^2 + (
    -0.8425574910926684 + x8)^2 + (-0.9716597371554934 + x9)^2) + x1106 * ((
    -0.46470646895314527 + x7)^2 + (-0.43245231227619974 + x8)^2 + (
    -0.5802228635322391 + x9)^2) + x1107 * ((-0.271134180722319 + x7)^2 + (
    -0.36061003024560156 + x8)^2 + (-0.1471398510067108 + x9)^2) + x1108 * ((
    -0.11520302100676727 + x7)^2 + (-0.663912716794071 + x8)^2 + (
    -0.5527561125387709 + x9)^2) + x1109 * ((-0.6162912656168867 + x7)^2 + (
    -0.5377119910240235 + x8)^2 + (-0.5807063907096474 + x9)^2) + x1110 * ((
    -0.37145013174802566 + x7)^2 + (-0.5345645332516239 + x8)^2 + (
    -0.510699989525291 + x9)^2) + x1111 * ((-0.03393556960060573 + x7)^2 + (
    -0.0156666184663532 + x8)^2 + (-0.07624209854333597 + x9)^2) + x1112 * ((
    -0.8270963072435799 + x7)^2 + (-0.7741889426436234 + x8)^2 + (
    -0.11760611435305912 + x9)^2) + x1113 * ((-0.18357821030782528 + x7)^2 + (
    -0.9734815530389282 + x8)^2 + (-0.08722449406089927 + x9)^2) + x1114 * ((
    -0.4006392450848354 + x7)^2 + (-0.9419621185211043 + x8)^2 + (
    -0.7043081992282076 + x9)^2) + x1115 * ((-0.22556650178941084 + x7)^2 + (
    -0.6034598644180125 + x8)^2 + (-0.1696902160808953 + x9)^2) + x1116 * ((
    -0.9825403553111026 + x7)^2 + (-0.35577808053830695 + x8)^2 + (
    -0.28203592489557505 + x9)^2) + x1117 * ((-0.19474142388607596 + x7)^2 + (
    -0.8131107522988229 + x8)^2 + (-0.20189429638588874 + x9)^2) + x1118 * ((
    -0.8965750056171701 + x7)^2 + (-0.681955506000223 + x8)^2 + (
    -0.1398601385146755 + x9)^2) + x1119 * ((-0.6906419235208477 + x7)^2 + (
    -0.24426493995237364 + x8)^2 + (-0.47872107051865875 + x9)^2) + x1120 * ((
    -0.4832440968672467 + x7)^2 + (-0.6969985518711306 + x8)^2 + (
    -0.9470893906754926 + x9)^2) + x1121 * ((-0.10622876499073441 + x7)^2 + (
    -0.693441063669681 + x8)^2 + (-0.1652812026058289 + x9)^2) + x1122 * ((
    -0.9897886682814803 + x7)^2 + (-0.599511795785779 + x8)^2 + (
    -0.8125758496836358 + x9)^2) + x1123 * ((-0.8169198572273942 + x7)^2 + (
    -0.008813750148081168 + x8)^2 + (-0.26018856120218925 + x9)^2) + x1124 * ((
    -0.7549634171088901 + x7)^2 + (-0.43078690581257384 + x8)^2 + (
    -0.7749777657255487 + x9)^2) + x1125 * ((-0.49182605753605824 + x7)^2 + (
    -0.28246579300389185 + x8)^2 + (-0.5070642636215076 + x9)^2) + x1126 * ((
    -0.5042598753977806 + x7)^2 + (-0.0022250490805308942 + x8)^2 + (
    -0.391688155748926 + x9)^2) + x1127 * ((-0.876071155170606 + x7)^2 + (
    -0.5508423923993612 + x8)^2 + (-0.824559592123001 + x9)^2) + x1128 * ((
    -0.11165887263159624 + x7)^2 + (-0.7085491226119169 + x8)^2 + (
    -0.8775234759634866 + x9)^2) + x1129 * ((-0.06305425963412226 + x7)^2 + (
    -0.1692915986404735 + x8)^2 + (-0.1546726877920308 + x9)^2) + x1130 * ((
    -0.9499620149510364 + x7)^2 + (-0.20812541109619742 + x8)^2 + (
    -0.34754918900968657 + x9)^2) + x1131 * ((-0.5460977024824913 + x7)^2 + (
    -0.9637992932230987 + x8)^2 + (-0.6995797299071689 + x9)^2) + x1132 * ((
    -0.25491459381765613 + x7)^2 + (-0.8070965237021143 + x8)^2 + (
    -0.8356296626230745 + x9)^2) + x1133 * ((-0.1702497329876329 + x7)^2 + (
    -0.4046122894687497 + x8)^2 + (-0.983146211120638 + x9)^2) + x1134 * ((
    -0.38494123369736066 + x7)^2 + (-0.0904492373848188 + x8)^2 + (
    -0.06525088803516699 + x9)^2) + x1135 * ((-0.1342401664666969 + x7)^2 + (
    -0.6663416890145257 + x8)^2 + (-0.7438434658481744 + x9)^2) + x1136 * ((
    -0.7253450049079363 + x7)^2 + (-0.4870006307057251 + x8)^2 + (
    -0.8740872298975312 + x9)^2) + x1137 * ((-0.7328325422437689 + x7)^2 + (
    -0.8575177732697433 + x8)^2 + (-0.4765071623659649 + x9)^2) + x1138 * ((
    -0.6783555500591814 + x7)^2 + (-0.9452264908498691 + x8)^2 + (
    -0.4009905455748076 + x9)^2) + x1139 * ((-0.9645465696225488 + x7)^2 + (
    -0.8988121792155044 + x8)^2 + (-0.8693701035695635 + x9)^2) + x1140 * ((
    -0.034109539793666044 + x7)^2 + (-0.7341228944483525 + x8)^2 + (
    -0.6711095074457485 + x9)^2) + x1141 * ((-0.9925652875910469 + x7)^2 + (
    -0.9767372917892282 + x8)^2 + (-0.35119270893145604 + x9)^2) + x1142 * ((
    -0.4335634471581603 + x7)^2 + (-0.9773387547384761 + x8)^2 + (
    -0.8638040489407179 + x9)^2) + x1143 * ((-0.8298565888279448 + x7)^2 + (
    -0.26942544674381563 + x8)^2 + (-0.07762497635314547 + x9)^2) + x1144 * ((
    -0.7541529640858855 + x7)^2 + (-0.5901288469645308 + x8)^2 + (
    -0.8131521214901242 + x9)^2) + x1145 * ((-0.6175218139719055 + x7)^2 + (
    -0.9185690552704726 + x8)^2 + (-0.9584989171844233 + x9)^2) + x1146 * ((
    -0.5426908933870604 + x7)^2 + (-0.9276924059348457 + x8)^2 + (
    -0.5088628864009217 + x9)^2) + x1147 * ((-0.36674157946961816 + x7)^2 + (
    -0.9494397054589957 + x8)^2 + (-0.502673714811412 + x9)^2) + x1148 * ((
    -0.7718452911924847 + x7)^2 + (-0.08932990709963073 + x8)^2 + (
    -0.8114836680773437 + x9)^2) + x1149 * ((-0.626463542469553 + x7)^2 + (
    -0.5374333330491173 + x8)^2 + (-0.12893104003458555 + x9)^2) + x1150 * ((
    -0.7425349118488094 + x7)^2 + (-0.1255983096608143 + x8)^2 + (
    -0.35251120977084616 + x9)^2) + x1151 * ((-0.5763919417102015 + x7)^2 + (
    -0.8668165395935221 + x8)^2 + (-0.18418689718597303 + x9)^2) + x1152 * ((
    -0.0842638329353742 + x7)^2 + (-0.22780453935881773 + x8)^2 + (
    -0.06751612916008864 + x9)^2) + x1153 * ((-0.4752871340736414 + x7)^2 + (
    -0.569148110715716 + x8)^2 + (-0.825451649082575 + x9)^2) + x1154 * ((
    -0.9331572175670021 + x7)^2 + (-0.13944078138289107 + x8)^2 + (
    -0.4974317423493232 + x9)^2) + x1155 * ((-0.5801698170306864 + x7)^2 + (
    -0.09023678868466112 + x8)^2 + (-0.5350628309500659 + x9)^2) + x1156 * ((
    -0.5007559134871579 + x7)^2 + (-0.9361289066528181 + x8)^2 + (
    -0.4876551928604236 + x9)^2) + x1157 * ((-0.3331382694999312 + x7)^2 + (
    -0.8003640425360357 + x8)^2 + (-0.4456772103718464 + x9)^2) + x1158 * ((
    -0.580897968874648 + x7)^2 + (-0.6875204337094218 + x8)^2 + (
    -0.23853575215395162 + x9)^2) + x1159 * ((-0.26259058062087826 + x7)^2 + (
    -0.31607289532856375 + x8)^2 + (-0.08079831830446549 + x9)^2) + x1160 * ((
    -0.8749384932019274 + x7)^2 + (-0.5978601364266924 + x8)^2 + (
    -0.2709722104839264 + x9)^2) + x1161 * ((-0.3380164843711445 + x7)^2 + (
    -0.9620957935062617 + x8)^2 + (-0.5318755277541398 + x9)^2) + x1162 * ((
    -0.19915462374899218 + x7)^2 + (-0.16745416979147543 + x8)^2 + (
    -0.8177983201819474 + x9)^2) + x1163 * ((-0.8422569529306239 + x7)^2 + (
    -0.9503230877966571 + x8)^2 + (-0.27758371082708055 + x9)^2) + x1164 * ((
    -0.44963143674100436 + x7)^2 + (-0.6298100336125453 + x8)^2 + (
    -0.6473187227829037 + x9)^2) + x1165 * ((-0.5323794396752508 + x7)^2 + (
    -0.29195939691071726 + x8)^2 + (-0.3777205926486479 + x9)^2) + x1166 * ((
    -0.08774633426227729 + x7)^2 + (-0.5103291813715215 + x8)^2 + (
    -0.21197701339206598 + x9)^2) + x1167 * ((-0.1886462563105995 + x7)^2 + (
    -0.7166154370441229 + x8)^2 + (-0.8967828307834859 + x9)^2) + x1168 * ((
    -0.9135151722699717 + x7)^2 + (-0.24518247233237755 + x8)^2 + (
    -0.22467871490663316 + x9)^2) + x1169 * ((-0.4002656679601796 + x7)^2 + (
    -0.8075378016015988 + x8)^2 + (-0.9589722648623482 + x9)^2) + x1170 * ((
    -0.350804850761565 + x7)^2 + (-0.2001510201677693 + x8)^2 + (
    -0.3847312652361822 + x9)^2) + x1171 * ((-0.7092459191225206 + x7)^2 + (
    -0.3653825052791586 + x8)^2 + (-0.4100011123148736 + x9)^2) + x1172 * ((
    -0.08924822462276016 + x7)^2 + (-0.2350022965537154 + x8)^2 + (
    -0.4724131123343983 + x9)^2) + x1173 * ((-0.678878546266445 + x7)^2 + (
    -0.0024223731399833914 + x8)^2 + (-0.18719967650857738 + x9)^2) + x1174 * (
    (-0.8949831170437572 + x7)^2 + (-0.6742418627601845 + x8)^2 + (
    -0.9659226960334533 + x9)^2) + x1175 * ((-0.461298010620385 + x7)^2 + (
    -0.3515384955734874 + x8)^2 + (-0.1589819355604557 + x9)^2) + x1176 * ((
    -0.4742180560695449 + x7)^2 + (-0.31128812059338673 + x8)^2 + (
    -0.16193285694593962 + x9)^2) + x1177 * ((-0.9057373068507129 + x7)^2 + (
    -0.07169041620954708 + x8)^2 + (-0.24658295842854583 + x9)^2) + x1178 * ((
    -0.042416932822683995 + x7)^2 + (-0.11901530250324566 + x8)^2 + (
    -0.8719607562434413 + x9)^2) + x1179 * ((-0.3509796417311175 + x7)^2 + (
    -0.7261268633422199 + x8)^2 + (-0.37378698482516615 + x9)^2) + x1180 * ((
    -0.48178722792919537 + x7)^2 + (-0.12507968740842412 + x8)^2 + (
    -0.1533291787002754 + x9)^2) + x1181 * ((-0.690187452865442 + x7)^2 + (
    -0.06414157686780875 + x8)^2 + (-0.9184182999081079 + x9)^2) + x1182 * ((
    -0.7601598471825683 + x7)^2 + (-0.39014455511239565 + x8)^2 + (
    -0.06643024228030481 + x9)^2) + x1183 * ((-0.7648317386640142 + x7)^2 + (
    -0.8401096588730549 + x8)^2 + (-0.6476437320133126 + x9)^2) + x1184 * ((
    -0.9157717582294775 + x7)^2 + (-0.7156353049895615 + x8)^2 + (
    -0.1779714150010886 + x9)^2) + x1185 * ((-0.2914662714138311 + x7)^2 + (
    -0.8979506548155362 + x8)^2 + (-0.28370242601709506 + x9)^2) + x1186 * ((
    -0.41299200861407237 + x7)^2 + (-0.5731791645656842 + x8)^2 + (
    -0.9880744442012739 + x9)^2) + x1187 * ((-0.2773152437673355 + x7)^2 + (
    -0.5869730199299126 + x8)^2 + (-0.6503070600258439 + x9)^2) + x1188 * ((
    -0.7054867170779409 + x7)^2 + (-0.38605289741051385 + x8)^2 + (
    -0.18161609983908555 + x9)^2) + x1189 * ((-0.9858526028351562 + x7)^2 + (
    -0.11659661065988192 + x8)^2 + (-0.6328911420439645 + x9)^2) + x1190 * ((
    -0.008586957495201109 + x7)^2 + (-0.6828361406835076 + x8)^2 + (
    -0.9383137951511125 + x9)^2) + x1191 * ((-0.5535058192578067 + x7)^2 + (
    -0.007867554292018242 + x8)^2 + (-0.3880343478492315 + x9)^2) + x1192 * ((
    -0.2998574271558311 + x7)^2 + (-0.5685060268070001 + x8)^2 + (
    -0.8612909410674978 + x9)^2) + x1193 * ((-0.7279300554494663 + x7)^2 + (
    -0.8665137249506871 + x8)^2 + (-0.2425661607644104 + x9)^2) + x1194 * ((
    -0.3674243260814667 + x7)^2 + (-0.6726025203611717 + x8)^2 + (
    -0.3019444385645804 + x9)^2) + x1195 * ((-0.561221458088611 + x7)^2 + (
    -0.1252412923674795 + x8)^2 + (-0.7626531785557333 + x9)^2) + x1196 * ((
    -0.7526982106932172 + x7)^2 + (-0.09811091554051077 + x8)^2 + (
    -0.8331863589378469 + x9)^2) + x1197 * ((-0.7212209268256802 + x7)^2 + (
    -0.3347884192733733 + x8)^2 + (-0.34081278172854135 + x9)^2) + x1198 * ((
    -0.38492684008888933 + x7)^2 + (-0.053573445724505286 + x8)^2 + (
    -0.45746291996264776 + x9)^2) + x1199 * ((-0.17867755090980397 + x7)^2 + (
    -0.846403915886413 + x8)^2 + (-0.15238735379254842 + x9)^2) + x1200 * ((
    -0.7342435428310872 + x7)^2 + (-0.35254162287667923 + x8)^2 + (
    -0.3649777944564463 + x9)^2) + x1201 * ((-0.21121661378120005 + x7)^2 + (
    -0.8764333024482275 + x8)^2 + (-0.6905270652669678 + x9)^2) + x1202 * ((
    -0.7454607699149387 + x7)^2 + (-0.5243311461762572 + x8)^2 + (
    -0.46847369630081737 + x9)^2) + x1203 * ((-0.5777724524082414 + x7)^2 + (
    -0.9389607386881164 + x8)^2 + (-0.9490991772196733 + x9)^2) + x1204 * ((
    -0.6953770563282883 + x7)^2 + (-0.30766167182637194 + x8)^2 + (
    -0.9947613161831723 + x9)^2) + x1205 * ((-0.07322511345630467 + x7)^2 + (
    -0.11542967998046938 + x8)^2 + (-0.5551153181290245 + x9)^2) + x1206 * ((
    -0.823466601595051 + x7)^2 + (-0.4761579425686089 + x8)^2 + (
    -0.7645792742638973 + x9)^2) + x1207 * ((-0.3065558046367579 + x7)^2 + (
    -0.6489835149493414 + x8)^2 + (-0.24712630191036555 + x9)^2) + x1208 * ((
    -0.42587171854139994 + x7)^2 + (-0.9609489628414893 + x8)^2 + (
    -0.34607854810703564 + x9)^2) + x1209 * ((-0.22514530689258294 + x7)^2 + (
    -0.29572551314242157 + x8)^2 + (-0.04494292345454676 + x9)^2) + x1210 * ((
    -0.733484242355372 + x7)^2 + (-0.7428655248132915 + x8)^2 + (
    -0.7982295536152093 + x9)^2) + x1211 * ((-0.5007178891993553 + x7)^2 + (
    -0.18337867834916188 + x8)^2 + (-0.2867876649071047 + x9)^2) + x1212 * ((
    -0.9062122087196477 + x7)^2 + (-0.5780300635857895 + x8)^2 + (
    -0.1538197962604425 + x9)^2) + x1213 * ((-0.7863514275791065 + x7)^2 + (
    -0.047106972476383846 + x8)^2 + (-0.9442358046581198 + x9)^2) + x1214 * ((
    -0.49327445076665244 + x7)^2 + (-0.7635057400072934 + x8)^2 + (
    -0.08977894732398484 + x9)^2) + x1215 * ((-0.5885030216777958 + x7)^2 + (
    -0.31457737395890006 + x8)^2 + (-0.06769170169106442 + x9)^2) + x1216 * ((
    -0.2624396116681811 + x7)^2 + (-0.8735241081831786 + x8)^2 + (
    -0.17009678211994406 + x9)^2) + x1217 * ((-0.8745938616823902 + x7)^2 + (
    -0.6895313121315244 + x8)^2 + (-0.3798558733668982 + x9)^2) + x1218 * ((
    -0.19470988963139768 + x7)^2 + (-0.7061159026040712 + x8)^2 + (
    -0.09540851729033883 + x9)^2) + x1219 * ((-0.07281526695083318 + x7)^2 + (
    -0.5313755426899924 + x8)^2 + (-0.3281258830967686 + x9)^2) + x1220 * ((
    -0.0050140137596184076 + x7)^2 + (-0.0571436713320036 + x8)^2 + (
    -0.7424653869787131 + x9)^2) + x1221 * ((-0.7365729576101151 + x7)^2 + (
    -0.016411359906266965 + x8)^2 + (-0.6018392757598213 + x9)^2) + x1222 * ((
    -0.9710402789360123 + x7)^2 + (-0.057905237168721646 + x8)^2 + (
    -0.1016804201191902 + x9)^2) + x1223 * ((-0.886784750676047 + x7)^2 + (
    -0.5909509982566028 + x8)^2 + (-0.08207033376025652 + x9)^2) + x1224 * ((
    -0.9456537388004167 + x7)^2 + (-0.10430429872917613 + x8)^2 + (
    -0.47980776700636785 + x9)^2) + x1225 * ((-0.01703842580768944 + x7)^2 + (
    -0.3771031988756788 + x8)^2 + (-0.9126173043337085 + x9)^2) + x1226 * ((
    -0.7473088625241339 + x7)^2 + (-0.1992639563893337 + x8)^2 + (
    -0.27259207689859966 + x9)^2) + x1227 * ((-0.9866924203074965 + x7)^2 + (
    -0.02211001009510316 + x8)^2 + (-0.710715645336501 + x9)^2) + x1228 * ((
    -0.22231763494264423 + x7)^2 + (-0.7222747879572179 + x8)^2 + (
    -0.48387331778539744 + x9)^2) + x1229 * ((-0.5217371859514337 + x7)^2 + (
    -0.8145029375864773 + x8)^2 + (-0.5971133086187703 + x9)^2) + x1230 * ((
    -0.16123590082773454 + x7)^2 + (-0.7338632807820815 + x8)^2 + (
    -0.9775931853783937 + x9)^2) + x1231 * ((-0.15216767027450806 + x7)^2 + (
    -0.8194769982782 + x8)^2 + (-0.3798283273565146 + x9)^2) + x1232 * ((
    -0.755130243908553 + x7)^2 + (-0.964046166903329 + x8)^2 + (
    -0.37287898957618804 + x9)^2) + x1233 * ((-0.4515557009816349 + x7)^2 + (
    -0.5888415389238447 + x8)^2 + (-0.6268802444924639 + x9)^2) + x1234 * ((
    -0.8339407401569209 + x7)^2 + (-0.3941136302934939 + x8)^2 + (
    -0.0011773452039460786 + x9)^2) + x1235 * ((-0.03523664509745583 + x7)^2 +
    (-0.9282465013011052 + x8)^2 + (-0.10432387873774907 + x9)^2) + x1236 * ((
    -0.5824740927361365 + x7)^2 + (-0.2830428234231407 + x8)^2 + (
    -0.2929978420181991 + x9)^2) + x1237 * ((-0.3457319486786484 + x7)^2 + (
    -0.6369253498892743 + x8)^2 + (-0.35691844570607956 + x9)^2) + x1238 * ((
    -0.42088037600595574 + x7)^2 + (-0.6312418989251471 + x8)^2 + (
    -0.8287246238964575 + x9)^2) + x1239 * ((-0.021979693073987727 + x7)^2 + (
    -0.2773405353290628 + x8)^2 + (-0.029133052826545436 + x9)^2) + x1240 * ((
    -0.5081863887708018 + x7)^2 + (-0.20601907370036388 + x8)^2 + (
    -0.9821208081223113 + x9)^2) + x1241 * ((-0.0019048004425398224 + x7)^2 + (
    -0.9834147377960726 + x8)^2 + (-0.2723044658709237 + x9)^2) + x1242 * ((
    -0.5500730095581713 + x7)^2 + (-0.9929315189942348 + x8)^2 + (
    -0.8008514847320088 + x9)^2) + x1243 * ((-0.42236107077823737 + x7)^2 + (
    -0.8886238887911541 + x8)^2 + (-0.8222569499938951 + x9)^2) + x1244 * ((
    -0.0672943459062394 + x7)^2 + (-0.2827538856518119 + x8)^2 + (
    -0.13430545927864412 + x9)^2) + x1245 * ((-0.5677325188553733 + x7)^2 + (
    -0.938532426013799 + x8)^2 + (-0.7611389677471435 + x9)^2) + x1246 * ((
    -0.8629019843437029 + x7)^2 + (-0.8826021988159478 + x8)^2 + (
    -0.7188638964511778 + x9)^2) + x1247 * ((-0.5507464371836962 + x7)^2 + (
    -0.7611165241588504 + x8)^2 + (-0.02910037665638643 + x9)^2) + x1248 * ((
    -0.34299191582875777 + x7)^2 + (-0.524901527819975 + x8)^2 + (
    -0.5781388484542243 + x9)^2) + x1249 * ((-0.35151500287062976 + x7)^2 + (
    -0.21136430913659288 + x8)^2 + (-0.08857984066212443 + x9)^2) + x1250 * ((
    -0.7675403347878336 + x7)^2 + (-0.532832695685235 + x8)^2 + (
    -0.2503117333896512 + x9)^2) + x1251 * ((-0.23097591211896384 + x7)^2 + (
    -0.15477203487438085 + x8)^2 + (-0.5054800430556513 + x9)^2) + x1252 * ((
    -0.7881833845877819 + x7)^2 + (-0.2758754119705751 + x8)^2 + (
    -0.9382258338204086 + x9)^2) + x1253 * ((-0.9466477036942484 + x7)^2 + (
    -0.06948523439716237 + x8)^2 + (-0.7146827511615796 + x9)^2) + x1254 * ((
    -0.5029417013633463 + x7)^2 + (-0.4785691085999849 + x8)^2 + (
    -0.6440855384208175 + x9)^2) + x1255 * ((-0.5303135807201502 + x7)^2 + (
    -0.9039824414704006 + x8)^2 + (-0.33970470843348766 + x9)^2) + x1256 * ((
    -0.3002120204313121 + x7)^2 + (-0.8293923954271605 + x8)^2 + (
    -0.09736075716511139 + x9)^2) + x1257 * ((-0.30009287477399993 + x7)^2 + (
    -0.8977331200619989 + x8)^2 + (-0.6790360118322567 + x9)^2) + x1258 * ((
    -0.949222817147212 + x7)^2 + (-0.4475514843804891 + x8)^2 + (
    -0.38135879431065867 + x9)^2) + x1259 * ((-0.2064338949319181 + x7)^2 + (
    -0.2471618264138381 + x8)^2 + (-0.33404126801805556 + x9)^2) + x1260 * ((
    -0.9469532157846159 + x7)^2 + (-0.12979939471251356 + x8)^2 + (
    -0.6308532308364203 + x9)^2) + x1261 * ((-0.8160024772328773 + x7)^2 + (
    -0.8192673081264756 + x8)^2 + (-0.828617395442529 + x9)^2) + x1262 * ((
    -0.043698145130302235 + x7)^2 + (-0.35823212196091736 + x8)^2 + (
    -0.6536017967379447 + x9)^2) + x1263 * ((-0.31599796165138205 + x7)^2 + (
    -0.14269139738795444 + x8)^2 + (-0.5083854452577903 + x9)^2) + x1264 * ((
    -0.1849721541921785 + x7)^2 + (-0.9379494054807923 + x8)^2 + (
    -0.750436849143862 + x9)^2) + x1265 * ((-0.2216708088282653 + x7)^2 + (
    -0.23053899815258394 + x8)^2 + (-0.18897253793934143 + x9)^2) + x1266 * ((
    -0.35548760077164 + x7)^2 + (-0.2106073810351573 + x8)^2 + (
    -0.8030904658404747 + x9)^2) + x1267 * ((-0.7046242974214645 + x7)^2 + (
    -0.9747362717516234 + x8)^2 + (-0.8986311370033265 + x9)^2) + x1268 * ((
    -0.6930115258414592 + x7)^2 + (-0.25226679460293766 + x8)^2 + (
    -0.2620829240380018 + x9)^2) + x1269 * ((-0.5416746943288492 + x7)^2 + (
    -0.3587968851453698 + x8)^2 + (-0.8014083818825035 + x9)^2) + x1270 * ((
    -0.709926799469957 + x7)^2 + (-0.42600195906405547 + x8)^2 + (
    -0.2918180254572945 + x9)^2) + x1271 * ((-0.3511232970881478 + x7)^2 + (
    -0.7757451672244947 + x8)^2 + (-0.7859380648395401 + x9)^2) + x1272 * ((
    -0.8803653019341091 + x7)^2 + (-0.6658465100092489 + x8)^2 + (
    -0.5112371462700493 + x9)^2) + x1273 * ((-0.17144800814870276 + x7)^2 + (
    -0.4122257700328378 + x8)^2 + (-0.8076682711989561 + x9)^2) + x1274 * ((
    -0.717380833423112 + x7)^2 + (-0.17998680267335054 + x8)^2 + (
    -0.9060156443877393 + x9)^2) + x1275 * ((-0.5878000971753468 + x7)^2 + (
    -0.18065525183423758 + x8)^2 + (-0.15538360399442397 + x9)^2) + x1276 * ((
    -0.8682299280341067 + x7)^2 + (-0.16346717895652563 + x8)^2 + (
    -0.4336582517475457 + x9)^2) + x1277 * ((-0.3606702369630238 + x7)^2 + (
    -0.731242129687016 + x8)^2 + (-0.12043748947308242 + x9)^2) + x1278 * ((
    -0.4815500944964639 + x7)^2 + (-0.6044620193979354 + x8)^2 + (
    -0.8210071600955915 + x9)^2) + x1279 * ((-0.11954313893324364 + x7)^2 + (
    -0.1323053978820773 + x8)^2 + (-0.25050555092577165 + x9)^2) + x1280 * ((
    -0.08542773014575478 + x7)^2 + (-0.18503314408239213 + x8)^2 + (
    -0.9115102242077784 + x9)^2) + x1281 * ((-0.8095044154907116 + x7)^2 + (
    -0.2799202631109189 + x8)^2 + (-0.2880890539271259 + x9)^2) + x1282 * ((
    -0.7212219319929314 + x7)^2 + (-0.5984506061652697 + x8)^2 + (
    -0.9365245987942612 + x9)^2) + x1283 * ((-0.8994684258109723 + x7)^2 + (
    -0.22641415105010199 + x8)^2 + (-0.6913162899186059 + x9)^2) + x1284 * ((
    -0.6581582771778646 + x7)^2 + (-0.197316973616537 + x8)^2 + (
    -0.43619331804872796 + x9)^2) + x1285 * ((-0.4739659187865559 + x7)^2 + (
    -0.38646221151733806 + x8)^2 + (-0.10770286986963273 + x9)^2) + x1286 * ((
    -0.8723979336469919 + x7)^2 + (-0.32335338168956085 + x8)^2 + (
    -0.5817075590285083 + x9)^2) + x1287 * ((-0.061809683762981016 + x7)^2 + (
    -0.5389217377093763 + x8)^2 + (-0.5417597560087298 + x9)^2) + x1288 * ((
    -0.07422322033257833 + x7)^2 + (-0.7097672901832104 + x8)^2 + (
    -0.06915026234774257 + x9)^2) + x1289 * ((-0.8280486736764958 + x7)^2 + (
    -0.04022416242938687 + x8)^2 + (-0.19882373590113933 + x9)^2) + x1290 * ((
    -0.029072146364669926 + x7)^2 + (-0.09653489205822285 + x8)^2 + (
    -0.049536244543501806 + x9)^2) + x1291 * ((-0.7881624249773665 + x7)^2 + (
    -0.7566784959062068 + x8)^2 + (-0.3074666055810339 + x9)^2) + x1292 * ((
    -0.7152259480390857 + x7)^2 + (-0.640956553515879 + x8)^2 + (
    -0.39814612324127086 + x9)^2) + x1293 * ((-0.9043657495395202 + x7)^2 + (
    -0.5252156573640178 + x8)^2 + (-0.8199524482586914 + x9)^2) + x1294 * ((
    -0.8601980724291697 + x7)^2 + (-0.31860765736788654 + x8)^2 + (
    -0.9089973811459461 + x9)^2) + x1295 * ((-0.2086703107751542 + x7)^2 + (
    -0.006149788315085392 + x8)^2 + (-0.21513361748683668 + x9)^2) + x1296 * ((
    -0.7823136762126888 + x7)^2 + (-0.416684189371502 + x8)^2 + (
    -0.4442685591428306 + x9)^2) + x1297 * ((-0.7994879189101486 + x7)^2 + (
    -0.5003588036104756 + x8)^2 + (-0.6431108825964064 + x9)^2) + x1298 * ((
    -0.2010796579746258 + x7)^2 + (-0.8170704549941877 + x8)^2 + (
    -0.2175952968667264 + x9)^2) + x1299 * ((-0.7094682020793405 + x7)^2 + (
    -0.49279977787280593 + x8)^2 + (-0.6972766332766551 + x9)^2) + x1300 * ((
    -0.8249820076123356 + x7)^2 + (-0.7551746481371484 + x8)^2 + (
    -0.3076678852974345 + x9)^2) + x1301 * ((-0.4431291732786462 + x7)^2 + (
    -0.10790569968568664 + x8)^2 + (-0.8104337482413756 + x9)^2) + x1302 * ((
    -0.12547352222190156 + x7)^2 + (-0.30712330696451673 + x8)^2 + (
    -0.6443221501233987 + x9)^2) + x1303 * ((-0.43521055817778886 + x7)^2 + (
    -0.11823850858772755 + x8)^2 + (-0.4245893746746593 + x9)^2) + x1304 * ((
    -0.1023807175165814 + x7)^2 + (-0.023476062383137597 + x8)^2 + (
    -0.7715459665761015 + x9)^2) + x1305 * ((-0.6084243314221985 + x7)^2 + (
    -0.6767723713597806 + x8)^2 + (-0.15277477018392027 + x9)^2) + x1306 * ((
    -0.07758513009101076 + x7)^2 + (-0.5193945915946692 + x8)^2 + (
    -0.13605100113112523 + x9)^2) + x1307 * ((-0.05076479042333726 + x7)^2 + (
    -0.7472210261556415 + x8)^2 + (-0.6187487644673069 + x9)^2) + x1308 * ((
    -0.5774530190962283 + x7)^2 + (-0.4625308284849895 + x8)^2 + (
    -0.8985951405862879 + x9)^2) + x1309 * ((-0.41887571010203506 + x7)^2 + (
    -0.04213576565608468 + x8)^2 + (-0.3367107300411496 + x9)^2) + x1310 * ((
    -0.5346587692815016 + x7)^2 + (-0.7514755753693055 + x8)^2 + (
    -0.16512273183076165 + x9)^2) + x1311 * ((-0.3673579319044816 + x7)^2 + (
    -0.4132537275282224 + x8)^2 + (-0.34757755368510646 + x9)^2) + x1312 * ((
    -0.5454982366155314 + x7)^2 + (-0.573439476172685 + x8)^2 + (
    -0.33123862062087006 + x9)^2) + x1313 * ((-0.23915554947791118 + x7)^2 + (
    -0.9496426713944737 + x8)^2 + (-0.9047110021009291 + x9)^2) + x1314 * ((
    -0.7835998720242816 + x7)^2 + (-0.5409585492652254 + x8)^2 + (
    -0.022604618704512136 + x9)^2) + x1315 * ((-0.7447675570789921 + x7)^2 + (
    -0.06306009873408058 + x8)^2 + (-0.32450967602437086 + x9)^2) + x1316 * ((
    -0.957050425001801 + x7)^2 + (-0.6908648583160039 + x8)^2 + (
    -0.6977383122594122 + x9)^2) + x1317 * ((-0.9643413589347215 + x7)^2 + (
    -0.8038041971590639 + x8)^2 + (-0.30694917237409114 + x9)^2) + x1318 * ((
    -0.16688443645138162 + x7)^2 + (-0.5498482774651414 + x8)^2 + (
    -0.7414582280194998 + x9)^2) + x1319 * ((-0.2748697607402272 + x7)^2 + (
    -0.6274376652049733 + x8)^2 + (-0.35357014233175543 + x9)^2) + x1320 * ((
    -0.5891376195472661 + x7)^2 + (-0.5661076738361366 + x8)^2 + (
    -0.6533215134864436 + x9)^2) + x1321 * ((-0.8392486510086273 + x7)^2 + (
    -0.3115496822184768 + x8)^2 + (-0.146703446853646 + x9)^2) + x1322 * ((
    -0.3738023028456101 + x7)^2 + (-0.7106592984968659 + x8)^2 + (
    -0.7581637572990693 + x9)^2) + x1323 * ((-0.2801730794814168 + x7)^2 + (
    -0.2913280058906009 + x8)^2 + (-0.10015085446802086 + x9)^2) + x1324 * ((
    -0.014051212285501768 + x7)^2 + (-0.3394766298985926 + x8)^2 + (
    -0.4278429675896249 + x9)^2) + x1325 * ((-0.9378558356981184 + x7)^2 + (
    -0.15127486460420836 + x8)^2 + (-0.7493436444755507 + x9)^2) + x1326 * ((
    -0.8297509765027676 + x7)^2 + (-0.08177655040140464 + x8)^2 + (
    -0.4494327397424498 + x9)^2) + x1327 * ((-0.11029669990558244 + x7)^2 + (
    -0.582339311840151 + x8)^2 + (-0.06415846876984466 + x9)^2) + x1328 * ((
    -0.9768471346651219 + x7)^2 + (-0.39696035406710384 + x8)^2 + (
    -0.23783616802647012 + x9)^2) + x1329 * ((-0.3764501911849826 + x7)^2 + (
    -0.786987541945555 + x8)^2 + (-0.2970434016308823 + x9)^2) + x1330 * ((
    -0.05618205629013939 + x7)^2 + (-0.4085438120067576 + x8)^2 + (
    -0.5645644728609109 + x9)^2) + x1331 * ((-0.6746539089984576 + x7)^2 + (
    -0.8329192222789586 + x8)^2 + (-0.8171355492822672 + x9)^2) + x1332 * ((
    -0.929134925271013 + x7)^2 + (-0.48607691575718226 + x8)^2 + (
    -0.14496601171482326 + x9)^2) + x1333 * ((-0.2888049631111739 + x7)^2 + (
    -0.45169995457478385 + x8)^2 + (-0.7415931477217647 + x9)^2) + x1334 * ((
    -0.8314270362626708 + x7)^2 + (-0.09391123252252986 + x8)^2 + (
    -0.6669146426368324 + x9)^2) + x1335 * ((-0.5652735801231673 + x7)^2 + (
    -0.9329767078391193 + x8)^2 + (-0.9484705315852879 + x9)^2) + x1336 * ((
    -0.3380979256818256 + x7)^2 + (-0.23035046064976195 + x8)^2 + (
    -0.5278605812355041 + x9)^2) + x1337 * ((-0.8184575612577757 + x7)^2 + (
    -0.9258797310665887 + x8)^2 + (-0.2046467253589157 + x9)^2) + x1338 * ((
    -0.40985008510077614 + x7)^2 + (-0.4757792482569193 + x8)^2 + (
    -0.8360188587690305 + x9)^2) + x1339 * ((-0.8332701786998654 + x7)^2 + (
    -0.20495368326898378 + x8)^2 + (-0.47164667394744264 + x9)^2) + x1340 * ((
    -0.0643880402156024 + x7)^2 + (-0.26358735356819285 + x8)^2 + (
    -0.13167880607810734 + x9)^2) + x1341 * ((-0.0025821300592889784 + x7)^2 +
    (-0.9088622869025026 + x8)^2 + (-0.04233625722670664 + x9)^2) + x1342 * ((
    -0.5236600684212673 + x7)^2 + (-0.27260080288022603 + x8)^2 + (
    -0.459442267827748 + x9)^2) + x1343 * ((-0.7158972098447147 + x7)^2 + (
    -0.9489828100457257 + x8)^2 + (-0.6888872017363918 + x9)^2) + x1344 * ((
    -0.7865559366849096 + x7)^2 + (-0.833267039226051 + x8)^2 + (
    -0.5747950642364967 + x9)^2) + x1345 * ((-0.34415199178488665 + x7)^2 + (
    -0.18091957070795228 + x8)^2 + (-0.031579899788283905 + x9)^2) + x1346 * ((
    -0.14471678962846113 + x7)^2 + (-0.30241060384916396 + x8)^2 + (
    -0.059993959720591294 + x9)^2) + x1347 * ((-0.6824739375029841 + x7)^2 + (
    -0.5331181892609036 + x8)^2 + (-0.977166596891582 + x9)^2) + x1348 * ((
    -0.20408398166030306 + x7)^2 + (-0.5154572139955655 + x8)^2 + (
    -0.4769277180629534 + x9)^2) + x1349 * ((-0.050689484148662145 + x7)^2 + (
    -0.5527672407633779 + x8)^2 + (-0.32111189487270875 + x9)^2) + x1350 * ((
    -0.23154418027475898 + x7)^2 + (-0.6700805221954127 + x8)^2 + (
    -0.9666075355371924 + x9)^2) + x1351 * ((-0.008868281269836076 + x7)^2 + (
    -0.6338997437715709 + x8)^2 + (-0.26544426895590223 + x9)^2) + x1352 * ((
    -0.6596209708459404 + x7)^2 + (-0.40168150668415104 + x8)^2 + (
    -0.4719673790088824 + x9)^2) + x1353 * ((-0.11053129063988809 + x7)^2 + (
    -0.16664026665153386 + x8)^2 + (-0.8851714055017869 + x9)^2) + x1354 * ((
    -0.5258408747918166 + x7)^2 + (-0.581125730214377 + x8)^2 + (
    -0.9734757162239656 + x9)^2) + x1355 * ((-0.37505520940960313 + x7)^2 + (
    -0.8756917740425001 + x8)^2 + (-0.9752391810025125 + x9)^2) + x1356 * ((
    -0.47118833747162414 + x7)^2 + (-0.3893334167798458 + x8)^2 + (
    -0.008212794912485166 + x9)^2) + x1357 * ((-0.6402127761953015 + x7)^2 + (
    -0.1600123713040228 + x8)^2 + (-0.44094193106669577 + x9)^2) + x1358 * ((
    -0.8231471689426597 + x7)^2 + (-0.7509513915820255 + x8)^2 + (
    -0.8921027170624262 + x9)^2) + x1359 * ((-0.20030064944641757 + x7)^2 + (
    -0.21962903531540312 + x8)^2 + (-0.5970473550708151 + x9)^2) + x1360 * ((
    -0.902808238265977 + x7)^2 + (-0.7562726465509134 + x8)^2 + (
    -0.24813085289058312 + x9)^2) + x1361 * ((-0.21843016026229212 + x7)^2 + (
    -0.8059343949692039 + x8)^2 + (-0.3752989990533576 + x9)^2) + x1362 * ((
    -0.14794288425068958 + x7)^2 + (-0.31328675165643205 + x8)^2 + (
    -0.8073941583373085 + x9)^2) + x1363 * ((-0.5235088791774563 + x7)^2 + (
    -0.04578915338953027 + x8)^2 + (-0.10692118625425784 + x9)^2) + x1364 * ((
    -0.5791900847638172 + x7)^2 + (-0.48532053702765365 + x8)^2 + (
    -0.3885259522950011 + x9)^2) + x1365 * ((-0.8920363304658884 + x7)^2 + (
    -0.5151000888985628 + x8)^2 + (-0.6346096148059661 + x9)^2) + x1366 * ((
    -0.9717009075640338 + x7)^2 + (-0.9907019955601769 + x8)^2 + (
    -0.85505344837673 + x9)^2) + x1367 * ((-0.34445995140187446 + x7)^2 + (
    -0.6392373435519673 + x8)^2 + (-0.7819131287560607 + x9)^2) + x1368 * ((
    -0.42109376750007577 + x7)^2 + (-0.7284707401745129 + x8)^2 + (
    -0.11077465817504761 + x9)^2) + x1369 * ((-0.925635401235069 + x7)^2 + (
    -0.5685890877714631 + x8)^2 + (-0.9462095752137067 + x9)^2) + x1370 * ((
    -0.7279111798696564 + x7)^2 + (-0.15487285858439592 + x8)^2 + (
    -0.7608763017869555 + x9)^2) + x1371 * ((-0.12654655247031799 + x7)^2 + (
    -0.09026002005416467 + x8)^2 + (-0.8883114041715482 + x9)^2) + x1372 * ((
    -0.6585295603176656 + x7)^2 + (-0.5624166650475771 + x8)^2 + (
    -0.5547559478222932 + x9)^2) + x1373 * ((-0.24575106742741626 + x7)^2 + (
    -0.3042728268888242 + x8)^2 + (-0.896812031612661 + x9)^2) + x1374 * ((
    -0.4606211642264276 + x7)^2 + (-0.5593289076408292 + x8)^2 + (
    -0.9885975772390854 + x9)^2) + x1375 * ((-0.7347225956683001 + x7)^2 + (
    -0.5745816301727896 + x8)^2 + (-0.009825540222648477 + x9)^2) + x1376 * ((
    -0.9978369871406716 + x7)^2 + (-0.9420017543770447 + x8)^2 + (
    -0.9484212753820023 + x9)^2) + x1377 * ((-0.6579730335184849 + x7)^2 + (
    -0.01651993788019801 + x8)^2 + (-0.763022957071984 + x9)^2) + x1378 * ((
    -0.9947489651588863 + x7)^2 + (-0.3224606084126759 + x8)^2 + (
    -0.7750668635617214 + x9)^2) + x1379 * ((-0.17582348854944607 + x7)^2 + (
    -0.17352822759146402 + x8)^2 + (-0.22743984463314282 + x9)^2) + x1380 * ((
    -0.4758203537795964 + x7)^2 + (-0.40834392828261223 + x8)^2 + (
    -0.05261570014523109 + x9)^2) + x1381 * ((-0.36204048569723735 + x7)^2 + (
    -0.8641293232884356 + x8)^2 + (-0.1489285988376965 + x9)^2) + x1382 * ((
    -0.6008467842262206 + x7)^2 + (-0.9039149091831002 + x8)^2 + (
    -0.36931294088336475 + x9)^2) + x1383 * ((-0.030067960172246666 + x7)^2 + (
    -0.48471288146931457 + x8)^2 + (-0.5753432715823008 + x9)^2) + x1384 * ((
    -0.1270532869152421 + x7)^2 + (-0.20492488058927516 + x8)^2 + (
    -0.2920819764108209 + x9)^2) + x1385 * ((-0.057643356995719985 + x7)^2 + (
    -0.4024951698758521 + x8)^2 + (-0.5345507589362359 + x9)^2) + x1386 * ((
    -0.9581878087034774 + x7)^2 + (-0.0800210963738257 + x8)^2 + (
    -0.677382890669299 + x9)^2) + x1387 * ((-0.2047868034464274 + x7)^2 + (
    -0.7755295931481812 + x8)^2 + (-0.07132945936635726 + x9)^2) + x1388 * ((
    -0.7829343091571344 + x7)^2 + (-0.8105545574565635 + x8)^2 + (
    -0.4991231549422569 + x9)^2) + x1389 * ((-0.6258463311430302 + x7)^2 + (
    -0.5496595671750402 + x8)^2 + (-0.19154029772231573 + x9)^2) + x1390 * ((
    -0.0272793485028624 + x7)^2 + (-0.011791358057427925 + x8)^2 + (
    -0.8057574736716172 + x9)^2) + x1391 * ((-0.5414890284796168 + x7)^2 + (
    -0.945016615830951 + x8)^2 + (-0.8798725595210737 + x9)^2) + x1392 * ((
    -0.05119780537656027 + x7)^2 + (-0.5031403231758489 + x8)^2 + (
    -0.11523583178307628 + x9)^2) + x1393 * ((-0.27464505675722395 + x7)^2 + (
    -0.05754985857648509 + x8)^2 + (-0.1718986943714379 + x9)^2) + x1394 * ((
    -0.563384014973976 + x7)^2 + (-0.4102870005309007 + x8)^2 + (
    -0.44867061677598474 + x9)^2) + x1395 * ((-0.9554091045415013 + x7)^2 + (
    -0.3287768838698092 + x8)^2 + (-0.5079007221884251 + x9)^2) + x1396 * ((
    -0.049015869567574866 + x7)^2 + (-0.7117888163278766 + x8)^2 + (
    -0.8523074296825538 + x9)^2) + x1397 * ((-0.30979077869124183 + x7)^2 + (
    -0.4417160550189484 + x8)^2 + (-0.3302755586589736 + x9)^2) + x1398 * ((
    -0.5591781894268806 + x7)^2 + (-0.8026089339206316 + x8)^2 + (
    -0.3713319195580873 + x9)^2) + x1399 * ((-0.5840605834977219 + x7)^2 + (
    -0.4911685585761769 + x8)^2 + (-0.1816408065331926 + x9)^2) + x1400 * ((
    -0.699915228142964 + x7)^2 + (-0.6846783090644426 + x8)^2 + (
    -0.5574598140568765 + x9)^2) + x1401 * ((-0.6753730740440026 + x7)^2 + (
    -0.5489318129908483 + x8)^2 + (-0.10199137240931655 + x9)^2) + x1402 * ((
    -0.11104797679961531 + x7)^2 + (-0.5472557486726254 + x8)^2 + (
    -0.9571846144505868 + x9)^2) + x1403 * ((-0.4290104355078601 + x7)^2 + (
    -0.500625748131909 + x8)^2 + (-0.839875855861129 + x9)^2) + x1404 * ((
    -0.8284104784524099 + x7)^2 + (-0.15168224190165258 + x8)^2 + (
    -0.7425205829813807 + x9)^2) + x1405 * ((-0.7835845824065171 + x7)^2 + (
    -0.43892942409165736 + x8)^2 + (-0.9672883708633824 + x9)^2) + x1406 * ((
    -0.9658474371081412 + x7)^2 + (-0.24521502946450435 + x8)^2 + (
    -0.19958521141831587 + x9)^2) + x1407 * ((-0.6763699518851537 + x7)^2 + (
    -0.40784932714190725 + x8)^2 + (-0.9693530161050696 + x9)^2) + x1408 * ((
    -0.015390131891825365 + x7)^2 + (-0.14588925853081935 + x8)^2 + (
    -0.5718899821316975 + x9)^2) + x1409 * ((-0.6550458977158515 + x7)^2 + (
    -0.8097929221347935 + x8)^2 + (-0.4104406395267636 + x9)^2) + x1410 * ((
    -0.7508103873205083 + x7)^2 + (-0.11532102750991224 + x8)^2 + (
    -0.6478368645129094 + x9)^2) + x1411 * ((-0.9737229810910403 + x7)^2 + (
    -0.5163950909606659 + x8)^2 + (-0.6367061240819752 + x9)^2) + x1412 * ((
    -0.5984140542435419 + x7)^2 + (-0.18984363054369258 + x8)^2 + (
    -0.027452684972157693 + x9)^2) + x1413 * ((-0.9243666020019815 + x7)^2 + (
    -0.8145037925176214 + x8)^2 + (-0.6578177936970774 + x9)^2) + x1414 * ((
    -0.9251327852082893 + x7)^2 + (-0.02218555315317494 + x8)^2 + (
    -0.4723664720086945 + x9)^2) + x1415 * ((-0.6010677075600663 + x7)^2 + (
    -0.864007697540581 + x8)^2 + (-0.9271036737422498 + x9)^2) + x1416 * ((
    -0.656591717593777 + x7)^2 + (-0.5134881016753086 + x8)^2 + (
    -0.1883008481102213 + x9)^2) + x1417 * ((-0.7407314335715345 + x7)^2 + (
    -0.25458554896989405 + x8)^2 + (-0.556216069468436 + x9)^2) + x1418 * ((
    -0.5120359138328312 + x7)^2 + (-0.8101978116075103 + x8)^2 + (
    -0.46638781967369414 + x9)^2) + x1419 * ((-0.7135334348392973 + x7)^2 + (
    -0.1779541525794096 + x8)^2 + (-0.6317024521479767 + x9)^2) + x1420 * ((
    -0.24177429627919167 + x7)^2 + (-0.6370581745682193 + x8)^2 + (
    -0.2710238175551406 + x9)^2) + x1421 * ((-0.9997913560034266 + x7)^2 + (
    -0.48490318564542456 + x8)^2 + (-0.4160988220639955 + x9)^2) + x1422 * ((
    -0.15980278916475676 + x7)^2 + (-0.06407095445485222 + x8)^2 + (
    -0.7249348271199497 + x9)^2) + x1423 * ((-0.1411868189363079 + x7)^2 + (
    -0.3067431553565323 + x8)^2 + (-0.78575462849935 + x9)^2) + x1424 * ((
    -0.5478827352853459 + x7)^2 + (-0.20291790816221889 + x8)^2 + (
    -0.8761980800539626 + x9)^2) + x1425 * ((-0.9066224120947074 + x7)^2 + (
    -0.9518140343960166 + x8)^2 + (-0.5195535652548422 + x9)^2) + x1426 * ((
    -0.4944497764703105 + x7)^2 + (-0.526178861965796 + x8)^2 + (
    -0.558537222910955 + x9)^2) + x1427 * ((-0.2726667055675822 + x7)^2 + (
    -0.9345746694586428 + x8)^2 + (-0.8532831802582073 + x9)^2) + x1428 * ((
    -0.9948056415771968 + x7)^2 + (-0.946100723693632 + x8)^2 + (
    -0.07095119487224366 + x9)^2) + x1429 * ((-0.5213951586103635 + x7)^2 + (
    -0.8407112340244879 + x8)^2 + (-0.27895325936062443 + x9)^2) + x1430 * ((
    -0.21494505782936268 + x7)^2 + (-0.7765096743882861 + x8)^2 + (
    -0.10254422951176734 + x9)^2) + x1431 * ((-0.7120472016233632 + x7)^2 + (
    -0.49718927750005937 + x8)^2 + (-0.7541840771418643 + x9)^2) + x1432 * ((
    -0.9685028423332537 + x7)^2 + (-0.5335345784258086 + x8)^2 + (
    -0.9890747374850164 + x9)^2) + x1433 * ((-0.9230166234673173 + x7)^2 + (
    -0.6518475605727765 + x8)^2 + (-0.734854155976083 + x9)^2) + x1434 * ((
    -0.06708623533817104 + x7)^2 + (-0.20172244637746983 + x8)^2 + (
    -0.2768060696570147 + x9)^2) + x1435 * ((-0.4038888086617314 + x7)^2 + (
    -0.1486875332810369 + x8)^2 + (-0.0864364601708697 + x9)^2) + x1436 * ((
    -0.4517085118551507 + x7)^2 + (-0.7765791454898151 + x8)^2 + (
    -0.18690810700205485 + x9)^2) + x1437 * ((-0.6984051043122955 + x7)^2 + (
    -0.6903189697467437 + x8)^2 + (-0.040778131010728136 + x9)^2) + x1438 * ((
    -0.6072448401148461 + x7)^2 + (-0.6438420452394027 + x8)^2 + (
    -0.6872356318162963 + x9)^2) + x1439 * ((-0.3156326593340355 + x7)^2 + (
    -0.6507808794562617 + x8)^2 + (-0.6233647448682074 + x9)^2) + x1440 * ((
    -0.4002818200993541 + x7)^2 + (-0.8997180632997818 + x8)^2 + (
    -0.14412431069924558 + x9)^2) + x1441 * ((-0.4603826538409851 + x7)^2 + (
    -0.04233386015418239 + x8)^2 + (-0.7043950613308216 + x9)^2) + x1442 * ((
    -0.870614516134697 + x7)^2 + (-0.8580337696409851 + x8)^2 + (
    -0.21857975143254016 + x9)^2) + x1443 * ((-0.7885802541502687 + x7)^2 + (
    -0.983116728066409 + x8)^2 + (-0.6268381409191566 + x9)^2) + x1444 * ((
    -0.453360688390823 + x7)^2 + (-0.17721212922523033 + x8)^2 + (
    -0.11369558618207087 + x9)^2) + x1445 * ((-0.37622468340220194 + x7)^2 + (
    -0.10891294174292976 + x8)^2 + (-0.1499013005008839 + x9)^2) + x1446 * ((
    -0.5160385921656351 + x7)^2 + (-0.5123193711182501 + x8)^2 + (
    -0.14661208983716012 + x9)^2) + x1447 * ((-0.8318749644250042 + x7)^2 + (
    -0.9474430577714092 + x8)^2 + (-0.627935164487112 + x9)^2) + x1448 * ((
    -0.1903852263517427 + x7)^2 + (-0.11470061584083246 + x8)^2 + (
    -0.44132933622437875 + x9)^2) + x1449 * ((-0.7139609443452906 + x7)^2 + (
    -0.1662593335896707 + x8)^2 + (-0.206132946290832 + x9)^2) + x1450 * ((
    -0.9287584108347345 + x7)^2 + (-0.4364542232297094 + x8)^2 + (
    -0.15930282013429242 + x9)^2) + x1451 * ((-0.5438534099357585 + x7)^2 + (
    -0.6713389990511793 + x8)^2 + (-0.7515358561055495 + x9)^2) + x1452 * ((
    -0.7953709431284481 + x7)^2 + (-0.09365706610576408 + x8)^2 + (
    -0.4729038737092427 + x9)^2) + x1453 * ((-0.6834981451581077 + x7)^2 + (
    -0.5907013715726769 + x8)^2 + (-0.2177451536406989 + x9)^2) + x1454 * ((
    -0.4631935234349823 + x7)^2 + (-0.8803533185868815 + x8)^2 + (
    -0.4273859435332188 + x9)^2) + x1455 * ((-0.476785780348992 + x7)^2 + (
    -0.8869187769611843 + x8)^2 + (-0.7193029869652928 + x9)^2) + x1456 * ((
    -0.31718143038215174 + x7)^2 + (-0.3262335948033561 + x8)^2 + (
    -0.9602949324145322 + x9)^2) + x1457 * ((-0.5936199239050312 + x7)^2 + (
    -0.49552398966064715 + x8)^2 + (-0.49848694537003924 + x9)^2) + x1458 * ((
    -0.9296199597347767 + x7)^2 + (-0.40889365057397287 + x8)^2 + (
    -0.8011545277509335 + x9)^2) + x1459 * ((-0.7354055208486365 + x7)^2 + (
    -0.7799949232677478 + x8)^2 + (-0.22209643149708758 + x9)^2) + x1460 * ((
    -0.8285174050295658 + x7)^2 + (-0.3399361044291944 + x8)^2 + (
    -0.5417626971057434 + x9)^2) + x1461 * ((-0.4743970301387661 + x7)^2 + (
    -0.03968268525091545 + x8)^2 + (-0.7676276502511942 + x9)^2) + x1462 * ((
    -0.9658526833599206 + x7)^2 + (-0.7769012618207594 + x8)^2 + (
    -0.30599222118777814 + x9)^2) + x1463 * ((-0.48754823079065357 + x7)^2 + (
    -0.7322449135727448 + x8)^2 + (-0.6492327824562298 + x9)^2) + x1464 * ((
    -0.9362650053761248 + x7)^2 + (-0.04268520093465755 + x8)^2 + (
    -0.7467628080743383 + x9)^2) + x1465 * ((-0.9307916870383665 + x7)^2 + (
    -0.961756532300574 + x8)^2 + (-0.2155280011227615 + x9)^2) + x1466 * ((
    -0.08912615918233224 + x7)^2 + (-0.6471821111714566 + x8)^2 + (
    -0.9913586544218587 + x9)^2) + x1467 * ((-0.8358554991679754 + x7)^2 + (
    -0.08929161317162748 + x8)^2 + (-0.9647833465957737 + x9)^2) + x1468 * ((
    -0.6273718862494942 + x7)^2 + (-0.7618805895251419 + x8)^2 + (
    -0.492165897853857 + x9)^2) + x1469 * ((-0.6702555245476077 + x7)^2 + (
    -0.3610395370884728 + x8)^2 + (-0.766937565344216 + x9)^2) + x1470 * ((
    -0.27485794231769844 + x7)^2 + (-0.5215206202220081 + x8)^2 + (
    -0.4889642491896449 + x9)^2) + x1471 * ((-0.8463263789396861 + x7)^2 + (
    -0.4936221195625502 + x8)^2 + (-0.5709411193324385 + x9)^2) + x1472 * ((
    -0.8054668308765568 + x7)^2 + (-0.2115365899248064 + x8)^2 + (
    -0.11566470511829063 + x9)^2) + x1473 * ((-0.1943614935785951 + x7)^2 + (
    -0.8334718657316503 + x8)^2 + (-0.44326977139831436 + x9)^2) + x1474 * ((
    -0.19480034368816324 + x7)^2 + (-0.8110564747660595 + x8)^2 + (
    -0.14302925781111175 + x9)^2) + x1475 * ((-0.39190211653261664 + x7)^2 + (
    -0.9677972762274933 + x8)^2 + (-0.16271262210127324 + x9)^2) + x1476 * ((
    -0.06731580772013712 + x7)^2 + (-0.6169831213923005 + x8)^2 + (
    -0.4027335514273457 + x9)^2) + x1477 * ((-0.38110974958221877 + x7)^2 + (
    -0.519046146671436 + x8)^2 + (-0.5738902625301048 + x9)^2) + x1478 * ((
    -0.9422399729911471 + x7)^2 + (-0.7184320029483544 + x8)^2 + (
    -0.9650701664096555 + x9)^2) + x1479 * ((-0.36801794166483814 + x7)^2 + (
    -0.9368906012991046 + x8)^2 + (-0.75121049110894 + x9)^2) + x1480 * ((
    -0.6630092172211279 + x7)^2 + (-0.20322311031211582 + x8)^2 + (
    -0.2887465568222305 + x9)^2) + x1481 * ((-0.9706981704650441 + x7)^2 + (
    -0.08466082082361082 + x8)^2 + (-0.7247467660352114 + x9)^2) + x1482 * ((
    -0.21059963791910552 + x7)^2 + (-0.49165647268816803 + x8)^2 + (
    -0.5804191839003714 + x9)^2) + x1483 * ((-0.5236356611629658 + x7)^2 + (
    -0.07814696537946009 + x8)^2 + (-0.3132490429219894 + x9)^2) + x1484 * ((
    -0.5026192836790041 + x7)^2 + (-0.6894528769723671 + x8)^2 + (
    -0.10662506884779244 + x9)^2) + x1485 * ((-0.680171254701243 + x7)^2 + (
    -0.8794858932580393 + x8)^2 + (-0.1970105609325069 + x9)^2) + x1486 * ((
    -0.653168096390829 + x7)^2 + (-0.8220713223404621 + x8)^2 + (
    -0.23312137565276492 + x9)^2) + x1487 * ((-0.5945786510272542 + x7)^2 + (
    -0.6937129033829035 + x8)^2 + (-0.4629130124432773 + x9)^2) + x1488 * ((
    -0.7366695477198858 + x7)^2 + (-0.10570699646360726 + x8)^2 + (
    -0.18565469991974215 + x9)^2) + x1489 * ((-0.18743250673347933 + x7)^2 + (
    -0.8501799346529197 + x8)^2 + (-0.4455750149410902 + x9)^2) + x1490 * ((
    -0.9211896892234244 + x7)^2 + (-0.8366465654279776 + x8)^2 + (
    -0.6201388866517694 + x9)^2) + x1491 * ((-0.9891510966919514 + x7)^2 + (
    -0.6966082529523953 + x8)^2 + (-0.8133151377521731 + x9)^2) + x1492 * ((
    -0.3902817623451159 + x7)^2 + (-0.24248773138219448 + x8)^2 + (
    -0.08078100456813775 + x9)^2) + x1493 * ((-0.4298108705942121 + x7)^2 + (
    -0.45161887902165165 + x8)^2 + (-0.08388435410245021 + x9)^2) + x1494 * ((
    -0.9073003783666486 + x7)^2 + (-0.48327373078316493 + x8)^2 + (
    -0.9910483026571903 + x9)^2) + x1495 * ((-0.881651726906589 + x7)^2 + (
    -0.30048516094118216 + x8)^2 + (-0.9850698876652512 + x9)^2) + x1496 * ((
    -0.6155649805033343 + x7)^2 + (-0.9348653805805935 + x8)^2 + (
    -0.6155415203207966 + x9)^2) + x1497 * ((-0.8117253444866105 + x7)^2 + (
    -0.3734646122935913 + x8)^2 + (-0.5139722294737984 + x9)^2) + x1498 * ((
    -0.3617901273059859 + x7)^2 + (-0.7565593293567897 + x8)^2 + (
    -0.8940449377670764 + x9)^2) + x1499 * ((-0.9436103266245361 + x7)^2 + (
    -0.6770001466142013 + x8)^2 + (-0.7668347302572115 + x9)^2) + x1500 * ((
    -0.4586541642719659 + x7)^2 + (-0.3840420830379708 + x8)^2 + (
    -0.6950693649611718 + x9)^2) + x1501 * ((-0.7400622139264225 + x7)^2 + (
    -0.027543445911217934 + x8)^2 + (-0.3504023093298636 + x9)^2) + x1502 * ((
    -0.8166839507821746 + x7)^2 + (-0.6985979465781534 + x8)^2 + (
    -0.136976908632233 + x9)^2) + x1503 * ((-0.7247676574408647 + x7)^2 + (
    -0.7156252081799882 + x8)^2 + (-0.28421024086039204 + x9)^2) + x1504 * ((
    -0.7116565008996277 + x7)^2 + (-0.19186706642009876 + x8)^2 + (
    -0.8309997111931379 + x9)^2) + x1505 * ((-0.2257396195230682 + x7)^2 + (
    -0.14303777575075283 + x8)^2 + (-0.4801497799483495 + x9)^2) + x1506 * ((
    -0.22699001220690018 + x7)^2 + (-0.28790414124402386 + x8)^2 + (
    -0.11035865916965082 + x9)^2) + x1507 * ((-0.22002870473769487 + x7)^2 + (
    -0.5487022693999476 + x8)^2 + (-0.9866104667343789 + x9)^2) + x1508 * ((
    -0.9091749596489073 + x7)^2 + (-0.34548122583324925 + x8)^2 + (
    -0.42621254666086883 + x9)^2) + x1509 * ((-0.6236740823858687 + x7)^2 + (
    -0.9129273253173751 + x8)^2 + (-0.5002652562779129 + x9)^2))

@constraint(m, e1, x10 + x510 + x1010 == 1)
@constraint(m, e2, x11 + x511 + x1011 == 1)
@constraint(m, e3, x12 + x512 + x1012 == 1)
@constraint(m, e4, x13 + x513 + x1013 == 1)
@constraint(m, e5, x14 + x514 + x1014 == 1)
@constraint(m, e6, x15 + x515 + x1015 == 1)
@constraint(m, e7, x16 + x516 + x1016 == 1)
@constraint(m, e8, x17 + x517 + x1017 == 1)
@constraint(m, e9, x18 + x518 + x1018 == 1)
@constraint(m, e10, x19 + x519 + x1019 == 1)
@constraint(m, e11, x20 + x520 + x1020 == 1)
@constraint(m, e12, x21 + x521 + x1021 == 1)
@constraint(m, e13, x22 + x522 + x1022 == 1)
@constraint(m, e14, x23 + x523 + x1023 == 1)
@constraint(m, e15, x24 + x524 + x1024 == 1)
@constraint(m, e16, x25 + x525 + x1025 == 1)
@constraint(m, e17, x26 + x526 + x1026 == 1)
@constraint(m, e18, x27 + x527 + x1027 == 1)
@constraint(m, e19, x28 + x528 + x1028 == 1)
@constraint(m, e20, x29 + x529 + x1029 == 1)
@constraint(m, e21, x30 + x530 + x1030 == 1)
@constraint(m, e22, x31 + x531 + x1031 == 1)
@constraint(m, e23, x32 + x532 + x1032 == 1)
@constraint(m, e24, x33 + x533 + x1033 == 1)
@constraint(m, e25, x34 + x534 + x1034 == 1)
@constraint(m, e26, x35 + x535 + x1035 == 1)
@constraint(m, e27, x36 + x536 + x1036 == 1)
@constraint(m, e28, x37 + x537 + x1037 == 1)
@constraint(m, e29, x38 + x538 + x1038 == 1)
@constraint(m, e30, x39 + x539 + x1039 == 1)
@constraint(m, e31, x40 + x540 + x1040 == 1)
@constraint(m, e32, x41 + x541 + x1041 == 1)
@constraint(m, e33, x42 + x542 + x1042 == 1)
@constraint(m, e34, x43 + x543 + x1043 == 1)
@constraint(m, e35, x44 + x544 + x1044 == 1)
@constraint(m, e36, x45 + x545 + x1045 == 1)
@constraint(m, e37, x46 + x546 + x1046 == 1)
@constraint(m, e38, x47 + x547 + x1047 == 1)
@constraint(m, e39, x48 + x548 + x1048 == 1)
@constraint(m, e40, x49 + x549 + x1049 == 1)
@constraint(m, e41, x50 + x550 + x1050 == 1)
@constraint(m, e42, x51 + x551 + x1051 == 1)
@constraint(m, e43, x52 + x552 + x1052 == 1)
@constraint(m, e44, x53 + x553 + x1053 == 1)
@constraint(m, e45, x54 + x554 + x1054 == 1)
@constraint(m, e46, x55 + x555 + x1055 == 1)
@constraint(m, e47, x56 + x556 + x1056 == 1)
@constraint(m, e48, x57 + x557 + x1057 == 1)
@constraint(m, e49, x58 + x558 + x1058 == 1)
@constraint(m, e50, x59 + x559 + x1059 == 1)
@constraint(m, e51, x60 + x560 + x1060 == 1)
@constraint(m, e52, x61 + x561 + x1061 == 1)
@constraint(m, e53, x62 + x562 + x1062 == 1)
@constraint(m, e54, x63 + x563 + x1063 == 1)
@constraint(m, e55, x64 + x564 + x1064 == 1)
@constraint(m, e56, x65 + x565 + x1065 == 1)
@constraint(m, e57, x66 + x566 + x1066 == 1)
@constraint(m, e58, x67 + x567 + x1067 == 1)
@constraint(m, e59, x68 + x568 + x1068 == 1)
@constraint(m, e60, x69 + x569 + x1069 == 1)
@constraint(m, e61, x70 + x570 + x1070 == 1)
@constraint(m, e62, x71 + x571 + x1071 == 1)
@constraint(m, e63, x72 + x572 + x1072 == 1)
@constraint(m, e64, x73 + x573 + x1073 == 1)
@constraint(m, e65, x74 + x574 + x1074 == 1)
@constraint(m, e66, x75 + x575 + x1075 == 1)
@constraint(m, e67, x76 + x576 + x1076 == 1)
@constraint(m, e68, x77 + x577 + x1077 == 1)
@constraint(m, e69, x78 + x578 + x1078 == 1)
@constraint(m, e70, x79 + x579 + x1079 == 1)
@constraint(m, e71, x80 + x580 + x1080 == 1)
@constraint(m, e72, x81 + x581 + x1081 == 1)
@constraint(m, e73, x82 + x582 + x1082 == 1)
@constraint(m, e74, x83 + x583 + x1083 == 1)
@constraint(m, e75, x84 + x584 + x1084 == 1)
@constraint(m, e76, x85 + x585 + x1085 == 1)
@constraint(m, e77, x86 + x586 + x1086 == 1)
@constraint(m, e78, x87 + x587 + x1087 == 1)
@constraint(m, e79, x88 + x588 + x1088 == 1)
@constraint(m, e80, x89 + x589 + x1089 == 1)
@constraint(m, e81, x90 + x590 + x1090 == 1)
@constraint(m, e82, x91 + x591 + x1091 == 1)
@constraint(m, e83, x92 + x592 + x1092 == 1)
@constraint(m, e84, x93 + x593 + x1093 == 1)
@constraint(m, e85, x94 + x594 + x1094 == 1)
@constraint(m, e86, x95 + x595 + x1095 == 1)
@constraint(m, e87, x96 + x596 + x1096 == 1)
@constraint(m, e88, x97 + x597 + x1097 == 1)
@constraint(m, e89, x98 + x598 + x1098 == 1)
@constraint(m, e90, x99 + x599 + x1099 == 1)
@constraint(m, e91, x100 + x600 + x1100 == 1)
@constraint(m, e92, x101 + x601 + x1101 == 1)
@constraint(m, e93, x102 + x602 + x1102 == 1)
@constraint(m, e94, x103 + x603 + x1103 == 1)
@constraint(m, e95, x104 + x604 + x1104 == 1)
@constraint(m, e96, x105 + x605 + x1105 == 1)
@constraint(m, e97, x106 + x606 + x1106 == 1)
@constraint(m, e98, x107 + x607 + x1107 == 1)
@constraint(m, e99, x108 + x608 + x1108 == 1)
@constraint(m, e100, x109 + x609 + x1109 == 1)
@constraint(m, e101, x110 + x610 + x1110 == 1)
@constraint(m, e102, x111 + x611 + x1111 == 1)
@constraint(m, e103, x112 + x612 + x1112 == 1)
@constraint(m, e104, x113 + x613 + x1113 == 1)
@constraint(m, e105, x114 + x614 + x1114 == 1)
@constraint(m, e106, x115 + x615 + x1115 == 1)
@constraint(m, e107, x116 + x616 + x1116 == 1)
@constraint(m, e108, x117 + x617 + x1117 == 1)
@constraint(m, e109, x118 + x618 + x1118 == 1)
@constraint(m, e110, x119 + x619 + x1119 == 1)
@constraint(m, e111, x120 + x620 + x1120 == 1)
@constraint(m, e112, x121 + x621 + x1121 == 1)
@constraint(m, e113, x122 + x622 + x1122 == 1)
@constraint(m, e114, x123 + x623 + x1123 == 1)
@constraint(m, e115, x124 + x624 + x1124 == 1)
@constraint(m, e116, x125 + x625 + x1125 == 1)
@constraint(m, e117, x126 + x626 + x1126 == 1)
@constraint(m, e118, x127 + x627 + x1127 == 1)
@constraint(m, e119, x128 + x628 + x1128 == 1)
@constraint(m, e120, x129 + x629 + x1129 == 1)
@constraint(m, e121, x130 + x630 + x1130 == 1)
@constraint(m, e122, x131 + x631 + x1131 == 1)
@constraint(m, e123, x132 + x632 + x1132 == 1)
@constraint(m, e124, x133 + x633 + x1133 == 1)
@constraint(m, e125, x134 + x634 + x1134 == 1)
@constraint(m, e126, x135 + x635 + x1135 == 1)
@constraint(m, e127, x136 + x636 + x1136 == 1)
@constraint(m, e128, x137 + x637 + x1137 == 1)
@constraint(m, e129, x138 + x638 + x1138 == 1)
@constraint(m, e130, x139 + x639 + x1139 == 1)
@constraint(m, e131, x140 + x640 + x1140 == 1)
@constraint(m, e132, x141 + x641 + x1141 == 1)
@constraint(m, e133, x142 + x642 + x1142 == 1)
@constraint(m, e134, x143 + x643 + x1143 == 1)
@constraint(m, e135, x144 + x644 + x1144 == 1)
@constraint(m, e136, x145 + x645 + x1145 == 1)
@constraint(m, e137, x146 + x646 + x1146 == 1)
@constraint(m, e138, x147 + x647 + x1147 == 1)
@constraint(m, e139, x148 + x648 + x1148 == 1)
@constraint(m, e140, x149 + x649 + x1149 == 1)
@constraint(m, e141, x150 + x650 + x1150 == 1)
@constraint(m, e142, x151 + x651 + x1151 == 1)
@constraint(m, e143, x152 + x652 + x1152 == 1)
@constraint(m, e144, x153 + x653 + x1153 == 1)
@constraint(m, e145, x154 + x654 + x1154 == 1)
@constraint(m, e146, x155 + x655 + x1155 == 1)
@constraint(m, e147, x156 + x656 + x1156 == 1)
@constraint(m, e148, x157 + x657 + x1157 == 1)
@constraint(m, e149, x158 + x658 + x1158 == 1)
@constraint(m, e150, x159 + x659 + x1159 == 1)
@constraint(m, e151, x160 + x660 + x1160 == 1)
@constraint(m, e152, x161 + x661 + x1161 == 1)
@constraint(m, e153, x162 + x662 + x1162 == 1)
@constraint(m, e154, x163 + x663 + x1163 == 1)
@constraint(m, e155, x164 + x664 + x1164 == 1)
@constraint(m, e156, x165 + x665 + x1165 == 1)
@constraint(m, e157, x166 + x666 + x1166 == 1)
@constraint(m, e158, x167 + x667 + x1167 == 1)
@constraint(m, e159, x168 + x668 + x1168 == 1)
@constraint(m, e160, x169 + x669 + x1169 == 1)
@constraint(m, e161, x170 + x670 + x1170 == 1)
@constraint(m, e162, x171 + x671 + x1171 == 1)
@constraint(m, e163, x172 + x672 + x1172 == 1)
@constraint(m, e164, x173 + x673 + x1173 == 1)
@constraint(m, e165, x174 + x674 + x1174 == 1)
@constraint(m, e166, x175 + x675 + x1175 == 1)
@constraint(m, e167, x176 + x676 + x1176 == 1)
@constraint(m, e168, x177 + x677 + x1177 == 1)
@constraint(m, e169, x178 + x678 + x1178 == 1)
@constraint(m, e170, x179 + x679 + x1179 == 1)
@constraint(m, e171, x180 + x680 + x1180 == 1)
@constraint(m, e172, x181 + x681 + x1181 == 1)
@constraint(m, e173, x182 + x682 + x1182 == 1)
@constraint(m, e174, x183 + x683 + x1183 == 1)
@constraint(m, e175, x184 + x684 + x1184 == 1)
@constraint(m, e176, x185 + x685 + x1185 == 1)
@constraint(m, e177, x186 + x686 + x1186 == 1)
@constraint(m, e178, x187 + x687 + x1187 == 1)
@constraint(m, e179, x188 + x688 + x1188 == 1)
@constraint(m, e180, x189 + x689 + x1189 == 1)
@constraint(m, e181, x190 + x690 + x1190 == 1)
@constraint(m, e182, x191 + x691 + x1191 == 1)
@constraint(m, e183, x192 + x692 + x1192 == 1)
@constraint(m, e184, x193 + x693 + x1193 == 1)
@constraint(m, e185, x194 + x694 + x1194 == 1)
@constraint(m, e186, x195 + x695 + x1195 == 1)
@constraint(m, e187, x196 + x696 + x1196 == 1)
@constraint(m, e188, x197 + x697 + x1197 == 1)
@constraint(m, e189, x198 + x698 + x1198 == 1)
@constraint(m, e190, x199 + x699 + x1199 == 1)
@constraint(m, e191, x200 + x700 + x1200 == 1)
@constraint(m, e192, x201 + x701 + x1201 == 1)
@constraint(m, e193, x202 + x702 + x1202 == 1)
@constraint(m, e194, x203 + x703 + x1203 == 1)
@constraint(m, e195, x204 + x704 + x1204 == 1)
@constraint(m, e196, x205 + x705 + x1205 == 1)
@constraint(m, e197, x206 + x706 + x1206 == 1)
@constraint(m, e198, x207 + x707 + x1207 == 1)
@constraint(m, e199, x208 + x708 + x1208 == 1)
@constraint(m, e200, x209 + x709 + x1209 == 1)
@constraint(m, e201, x210 + x710 + x1210 == 1)
@constraint(m, e202, x211 + x711 + x1211 == 1)
@constraint(m, e203, x212 + x712 + x1212 == 1)
@constraint(m, e204, x213 + x713 + x1213 == 1)
@constraint(m, e205, x214 + x714 + x1214 == 1)
@constraint(m, e206, x215 + x715 + x1215 == 1)
@constraint(m, e207, x216 + x716 + x1216 == 1)
@constraint(m, e208, x217 + x717 + x1217 == 1)
@constraint(m, e209, x218 + x718 + x1218 == 1)
@constraint(m, e210, x219 + x719 + x1219 == 1)
@constraint(m, e211, x220 + x720 + x1220 == 1)
@constraint(m, e212, x221 + x721 + x1221 == 1)
@constraint(m, e213, x222 + x722 + x1222 == 1)
@constraint(m, e214, x223 + x723 + x1223 == 1)
@constraint(m, e215, x224 + x724 + x1224 == 1)
@constraint(m, e216, x225 + x725 + x1225 == 1)
@constraint(m, e217, x226 + x726 + x1226 == 1)
@constraint(m, e218, x227 + x727 + x1227 == 1)
@constraint(m, e219, x228 + x728 + x1228 == 1)
@constraint(m, e220, x229 + x729 + x1229 == 1)
@constraint(m, e221, x230 + x730 + x1230 == 1)
@constraint(m, e222, x231 + x731 + x1231 == 1)
@constraint(m, e223, x232 + x732 + x1232 == 1)
@constraint(m, e224, x233 + x733 + x1233 == 1)
@constraint(m, e225, x234 + x734 + x1234 == 1)
@constraint(m, e226, x235 + x735 + x1235 == 1)
@constraint(m, e227, x236 + x736 + x1236 == 1)
@constraint(m, e228, x237 + x737 + x1237 == 1)
@constraint(m, e229, x238 + x738 + x1238 == 1)
@constraint(m, e230, x239 + x739 + x1239 == 1)
@constraint(m, e231, x240 + x740 + x1240 == 1)
@constraint(m, e232, x241 + x741 + x1241 == 1)
@constraint(m, e233, x242 + x742 + x1242 == 1)
@constraint(m, e234, x243 + x743 + x1243 == 1)
@constraint(m, e235, x244 + x744 + x1244 == 1)
@constraint(m, e236, x245 + x745 + x1245 == 1)
@constraint(m, e237, x246 + x746 + x1246 == 1)
@constraint(m, e238, x247 + x747 + x1247 == 1)
@constraint(m, e239, x248 + x748 + x1248 == 1)
@constraint(m, e240, x249 + x749 + x1249 == 1)
@constraint(m, e241, x250 + x750 + x1250 == 1)
@constraint(m, e242, x251 + x751 + x1251 == 1)
@constraint(m, e243, x252 + x752 + x1252 == 1)
@constraint(m, e244, x253 + x753 + x1253 == 1)
@constraint(m, e245, x254 + x754 + x1254 == 1)
@constraint(m, e246, x255 + x755 + x1255 == 1)
@constraint(m, e247, x256 + x756 + x1256 == 1)
@constraint(m, e248, x257 + x757 + x1257 == 1)
@constraint(m, e249, x258 + x758 + x1258 == 1)
@constraint(m, e250, x259 + x759 + x1259 == 1)
@constraint(m, e251, x260 + x760 + x1260 == 1)
@constraint(m, e252, x261 + x761 + x1261 == 1)
@constraint(m, e253, x262 + x762 + x1262 == 1)
@constraint(m, e254, x263 + x763 + x1263 == 1)
@constraint(m, e255, x264 + x764 + x1264 == 1)
@constraint(m, e256, x265 + x765 + x1265 == 1)
@constraint(m, e257, x266 + x766 + x1266 == 1)
@constraint(m, e258, x267 + x767 + x1267 == 1)
@constraint(m, e259, x268 + x768 + x1268 == 1)
@constraint(m, e260, x269 + x769 + x1269 == 1)
@constraint(m, e261, x270 + x770 + x1270 == 1)
@constraint(m, e262, x271 + x771 + x1271 == 1)
@constraint(m, e263, x272 + x772 + x1272 == 1)
@constraint(m, e264, x273 + x773 + x1273 == 1)
@constraint(m, e265, x274 + x774 + x1274 == 1)
@constraint(m, e266, x275 + x775 + x1275 == 1)
@constraint(m, e267, x276 + x776 + x1276 == 1)
@constraint(m, e268, x277 + x777 + x1277 == 1)
@constraint(m, e269, x278 + x778 + x1278 == 1)
@constraint(m, e270, x279 + x779 + x1279 == 1)
@constraint(m, e271, x280 + x780 + x1280 == 1)
@constraint(m, e272, x281 + x781 + x1281 == 1)
@constraint(m, e273, x282 + x782 + x1282 == 1)
@constraint(m, e274, x283 + x783 + x1283 == 1)
@constraint(m, e275, x284 + x784 + x1284 == 1)
@constraint(m, e276, x285 + x785 + x1285 == 1)
@constraint(m, e277, x286 + x786 + x1286 == 1)
@constraint(m, e278, x287 + x787 + x1287 == 1)
@constraint(m, e279, x288 + x788 + x1288 == 1)
@constraint(m, e280, x289 + x789 + x1289 == 1)
@constraint(m, e281, x290 + x790 + x1290 == 1)
@constraint(m, e282, x291 + x791 + x1291 == 1)
@constraint(m, e283, x292 + x792 + x1292 == 1)
@constraint(m, e284, x293 + x793 + x1293 == 1)
@constraint(m, e285, x294 + x794 + x1294 == 1)
@constraint(m, e286, x295 + x795 + x1295 == 1)
@constraint(m, e287, x296 + x796 + x1296 == 1)
@constraint(m, e288, x297 + x797 + x1297 == 1)
@constraint(m, e289, x298 + x798 + x1298 == 1)
@constraint(m, e290, x299 + x799 + x1299 == 1)
@constraint(m, e291, x300 + x800 + x1300 == 1)
@constraint(m, e292, x301 + x801 + x1301 == 1)
@constraint(m, e293, x302 + x802 + x1302 == 1)
@constraint(m, e294, x303 + x803 + x1303 == 1)
@constraint(m, e295, x304 + x804 + x1304 == 1)
@constraint(m, e296, x305 + x805 + x1305 == 1)
@constraint(m, e297, x306 + x806 + x1306 == 1)
@constraint(m, e298, x307 + x807 + x1307 == 1)
@constraint(m, e299, x308 + x808 + x1308 == 1)
@constraint(m, e300, x309 + x809 + x1309 == 1)
@constraint(m, e301, x310 + x810 + x1310 == 1)
@constraint(m, e302, x311 + x811 + x1311 == 1)
@constraint(m, e303, x312 + x812 + x1312 == 1)
@constraint(m, e304, x313 + x813 + x1313 == 1)
@constraint(m, e305, x314 + x814 + x1314 == 1)
@constraint(m, e306, x315 + x815 + x1315 == 1)
@constraint(m, e307, x316 + x816 + x1316 == 1)
@constraint(m, e308, x317 + x817 + x1317 == 1)
@constraint(m, e309, x318 + x818 + x1318 == 1)
@constraint(m, e310, x319 + x819 + x1319 == 1)
@constraint(m, e311, x320 + x820 + x1320 == 1)
@constraint(m, e312, x321 + x821 + x1321 == 1)
@constraint(m, e313, x322 + x822 + x1322 == 1)
@constraint(m, e314, x323 + x823 + x1323 == 1)
@constraint(m, e315, x324 + x824 + x1324 == 1)
@constraint(m, e316, x325 + x825 + x1325 == 1)
@constraint(m, e317, x326 + x826 + x1326 == 1)
@constraint(m, e318, x327 + x827 + x1327 == 1)
@constraint(m, e319, x328 + x828 + x1328 == 1)
@constraint(m, e320, x329 + x829 + x1329 == 1)
@constraint(m, e321, x330 + x830 + x1330 == 1)
@constraint(m, e322, x331 + x831 + x1331 == 1)
@constraint(m, e323, x332 + x832 + x1332 == 1)
@constraint(m, e324, x333 + x833 + x1333 == 1)
@constraint(m, e325, x334 + x834 + x1334 == 1)
@constraint(m, e326, x335 + x835 + x1335 == 1)
@constraint(m, e327, x336 + x836 + x1336 == 1)
@constraint(m, e328, x337 + x837 + x1337 == 1)
@constraint(m, e329, x338 + x838 + x1338 == 1)
@constraint(m, e330, x339 + x839 + x1339 == 1)
@constraint(m, e331, x340 + x840 + x1340 == 1)
@constraint(m, e332, x341 + x841 + x1341 == 1)
@constraint(m, e333, x342 + x842 + x1342 == 1)
@constraint(m, e334, x343 + x843 + x1343 == 1)
@constraint(m, e335, x344 + x844 + x1344 == 1)
@constraint(m, e336, x345 + x845 + x1345 == 1)
@constraint(m, e337, x346 + x846 + x1346 == 1)
@constraint(m, e338, x347 + x847 + x1347 == 1)
@constraint(m, e339, x348 + x848 + x1348 == 1)
@constraint(m, e340, x349 + x849 + x1349 == 1)
@constraint(m, e341, x350 + x850 + x1350 == 1)
@constraint(m, e342, x351 + x851 + x1351 == 1)
@constraint(m, e343, x352 + x852 + x1352 == 1)
@constraint(m, e344, x353 + x853 + x1353 == 1)
@constraint(m, e345, x354 + x854 + x1354 == 1)
@constraint(m, e346, x355 + x855 + x1355 == 1)
@constraint(m, e347, x356 + x856 + x1356 == 1)
@constraint(m, e348, x357 + x857 + x1357 == 1)
@constraint(m, e349, x358 + x858 + x1358 == 1)
@constraint(m, e350, x359 + x859 + x1359 == 1)
@constraint(m, e351, x360 + x860 + x1360 == 1)
@constraint(m, e352, x361 + x861 + x1361 == 1)
@constraint(m, e353, x362 + x862 + x1362 == 1)
@constraint(m, e354, x363 + x863 + x1363 == 1)
@constraint(m, e355, x364 + x864 + x1364 == 1)
@constraint(m, e356, x365 + x865 + x1365 == 1)
@constraint(m, e357, x366 + x866 + x1366 == 1)
@constraint(m, e358, x367 + x867 + x1367 == 1)
@constraint(m, e359, x368 + x868 + x1368 == 1)
@constraint(m, e360, x369 + x869 + x1369 == 1)
@constraint(m, e361, x370 + x870 + x1370 == 1)
@constraint(m, e362, x371 + x871 + x1371 == 1)
@constraint(m, e363, x372 + x872 + x1372 == 1)
@constraint(m, e364, x373 + x873 + x1373 == 1)
@constraint(m, e365, x374 + x874 + x1374 == 1)
@constraint(m, e366, x375 + x875 + x1375 == 1)
@constraint(m, e367, x376 + x876 + x1376 == 1)
@constraint(m, e368, x377 + x877 + x1377 == 1)
@constraint(m, e369, x378 + x878 + x1378 == 1)
@constraint(m, e370, x379 + x879 + x1379 == 1)
@constraint(m, e371, x380 + x880 + x1380 == 1)
@constraint(m, e372, x381 + x881 + x1381 == 1)
@constraint(m, e373, x382 + x882 + x1382 == 1)
@constraint(m, e374, x383 + x883 + x1383 == 1)
@constraint(m, e375, x384 + x884 + x1384 == 1)
@constraint(m, e376, x385 + x885 + x1385 == 1)
@constraint(m, e377, x386 + x886 + x1386 == 1)
@constraint(m, e378, x387 + x887 + x1387 == 1)
@constraint(m, e379, x388 + x888 + x1388 == 1)
@constraint(m, e380, x389 + x889 + x1389 == 1)
@constraint(m, e381, x390 + x890 + x1390 == 1)
@constraint(m, e382, x391 + x891 + x1391 == 1)
@constraint(m, e383, x392 + x892 + x1392 == 1)
@constraint(m, e384, x393 + x893 + x1393 == 1)
@constraint(m, e385, x394 + x894 + x1394 == 1)
@constraint(m, e386, x395 + x895 + x1395 == 1)
@constraint(m, e387, x396 + x896 + x1396 == 1)
@constraint(m, e388, x397 + x897 + x1397 == 1)
@constraint(m, e389, x398 + x898 + x1398 == 1)
@constraint(m, e390, x399 + x899 + x1399 == 1)
@constraint(m, e391, x400 + x900 + x1400 == 1)
@constraint(m, e392, x401 + x901 + x1401 == 1)
@constraint(m, e393, x402 + x902 + x1402 == 1)
@constraint(m, e394, x403 + x903 + x1403 == 1)
@constraint(m, e395, x404 + x904 + x1404 == 1)
@constraint(m, e396, x405 + x905 + x1405 == 1)
@constraint(m, e397, x406 + x906 + x1406 == 1)
@constraint(m, e398, x407 + x907 + x1407 == 1)
@constraint(m, e399, x408 + x908 + x1408 == 1)
@constraint(m, e400, x409 + x909 + x1409 == 1)
@constraint(m, e401, x410 + x910 + x1410 == 1)
@constraint(m, e402, x411 + x911 + x1411 == 1)
@constraint(m, e403, x412 + x912 + x1412 == 1)
@constraint(m, e404, x413 + x913 + x1413 == 1)
@constraint(m, e405, x414 + x914 + x1414 == 1)
@constraint(m, e406, x415 + x915 + x1415 == 1)
@constraint(m, e407, x416 + x916 + x1416 == 1)
@constraint(m, e408, x417 + x917 + x1417 == 1)
@constraint(m, e409, x418 + x918 + x1418 == 1)
@constraint(m, e410, x419 + x919 + x1419 == 1)
@constraint(m, e411, x420 + x920 + x1420 == 1)
@constraint(m, e412, x421 + x921 + x1421 == 1)
@constraint(m, e413, x422 + x922 + x1422 == 1)
@constraint(m, e414, x423 + x923 + x1423 == 1)
@constraint(m, e415, x424 + x924 + x1424 == 1)
@constraint(m, e416, x425 + x925 + x1425 == 1)
@constraint(m, e417, x426 + x926 + x1426 == 1)
@constraint(m, e418, x427 + x927 + x1427 == 1)
@constraint(m, e419, x428 + x928 + x1428 == 1)
@constraint(m, e420, x429 + x929 + x1429 == 1)
@constraint(m, e421, x430 + x930 + x1430 == 1)
@constraint(m, e422, x431 + x931 + x1431 == 1)
@constraint(m, e423, x432 + x932 + x1432 == 1)
@constraint(m, e424, x433 + x933 + x1433 == 1)
@constraint(m, e425, x434 + x934 + x1434 == 1)
@constraint(m, e426, x435 + x935 + x1435 == 1)
@constraint(m, e427, x436 + x936 + x1436 == 1)
@constraint(m, e428, x437 + x937 + x1437 == 1)
@constraint(m, e429, x438 + x938 + x1438 == 1)
@constraint(m, e430, x439 + x939 + x1439 == 1)
@constraint(m, e431, x440 + x940 + x1440 == 1)
@constraint(m, e432, x441 + x941 + x1441 == 1)
@constraint(m, e433, x442 + x942 + x1442 == 1)
@constraint(m, e434, x443 + x943 + x1443 == 1)
@constraint(m, e435, x444 + x944 + x1444 == 1)
@constraint(m, e436, x445 + x945 + x1445 == 1)
@constraint(m, e437, x446 + x946 + x1446 == 1)
@constraint(m, e438, x447 + x947 + x1447 == 1)
@constraint(m, e439, x448 + x948 + x1448 == 1)
@constraint(m, e440, x449 + x949 + x1449 == 1)
@constraint(m, e441, x450 + x950 + x1450 == 1)
@constraint(m, e442, x451 + x951 + x1451 == 1)
@constraint(m, e443, x452 + x952 + x1452 == 1)
@constraint(m, e444, x453 + x953 + x1453 == 1)
@constraint(m, e445, x454 + x954 + x1454 == 1)
@constraint(m, e446, x455 + x955 + x1455 == 1)
@constraint(m, e447, x456 + x956 + x1456 == 1)
@constraint(m, e448, x457 + x957 + x1457 == 1)
@constraint(m, e449, x458 + x958 + x1458 == 1)
@constraint(m, e450, x459 + x959 + x1459 == 1)
@constraint(m, e451, x460 + x960 + x1460 == 1)
@constraint(m, e452, x461 + x961 + x1461 == 1)
@constraint(m, e453, x462 + x962 + x1462 == 1)
@constraint(m, e454, x463 + x963 + x1463 == 1)
@constraint(m, e455, x464 + x964 + x1464 == 1)
@constraint(m, e456, x465 + x965 + x1465 == 1)
@constraint(m, e457, x466 + x966 + x1466 == 1)
@constraint(m, e458, x467 + x967 + x1467 == 1)
@constraint(m, e459, x468 + x968 + x1468 == 1)
@constraint(m, e460, x469 + x969 + x1469 == 1)
@constraint(m, e461, x470 + x970 + x1470 == 1)
@constraint(m, e462, x471 + x971 + x1471 == 1)
@constraint(m, e463, x472 + x972 + x1472 == 1)
@constraint(m, e464, x473 + x973 + x1473 == 1)
@constraint(m, e465, x474 + x974 + x1474 == 1)
@constraint(m, e466, x475 + x975 + x1475 == 1)
@constraint(m, e467, x476 + x976 + x1476 == 1)
@constraint(m, e468, x477 + x977 + x1477 == 1)
@constraint(m, e469, x478 + x978 + x1478 == 1)
@constraint(m, e470, x479 + x979 + x1479 == 1)
@constraint(m, e471, x480 + x980 + x1480 == 1)
@constraint(m, e472, x481 + x981 + x1481 == 1)
@constraint(m, e473, x482 + x982 + x1482 == 1)
@constraint(m, e474, x483 + x983 + x1483 == 1)
@constraint(m, e475, x484 + x984 + x1484 == 1)
@constraint(m, e476, x485 + x985 + x1485 == 1)
@constraint(m, e477, x486 + x986 + x1486 == 1)
@constraint(m, e478, x487 + x987 + x1487 == 1)
@constraint(m, e479, x488 + x988 + x1488 == 1)
@constraint(m, e480, x489 + x989 + x1489 == 1)
@constraint(m, e481, x490 + x990 + x1490 == 1)
@constraint(m, e482, x491 + x991 + x1491 == 1)
@constraint(m, e483, x492 + x992 + x1492 == 1)
@constraint(m, e484, x493 + x993 + x1493 == 1)
@constraint(m, e485, x494 + x994 + x1494 == 1)
@constraint(m, e486, x495 + x995 + x1495 == 1)
@constraint(m, e487, x496 + x996 + x1496 == 1)
@constraint(m, e488, x497 + x997 + x1497 == 1)
@constraint(m, e489, x498 + x998 + x1498 == 1)
@constraint(m, e490, x499 + x999 + x1499 == 1)
@constraint(m, e491, x500 + x1000 + x1500 == 1)
@constraint(m, e492, x501 + x1001 + x1501 == 1)
@constraint(m, e493, x502 + x1002 + x1502 == 1)
@constraint(m, e494, x503 + x1003 + x1503 == 1)
@constraint(m, e495, x504 + x1004 + x1504 == 1)
@constraint(m, e496, x505 + x1005 + x1505 == 1)
@constraint(m, e497, x506 + x1006 + x1506 == 1)
@constraint(m, e498, x507 + x1007 + x1507 == 1)
@constraint(m, e499, x508 + x1008 + x1508 == 1)
@constraint(m, e500, x509 + x1009 + x1509 == 1)
