# NLP written by GAMS Convert at 05/15/24 11:36:53
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

@NLobjective(m, Min, x7 * ((-0.1692498439422696 + x1)^2 + (-0.594909962110926
    + x2)^2 + (-0.2649627397072344 + x3)^2) + x8 * ((-0.4299773164971996 + x1)
    ^2 + (-0.8599590238209864 + x2)^2 + (-0.5477886873552766 + x3)^2) + x9 * ((
    -0.5826003170056784 + x1)^2 + (-0.941883448057164 + x2)^2 + (
    -0.30867313678242836 + x3)^2) + x10 * ((-0.6888712108376565 + x1)^2 + (
    -0.46694321374927916 + x2)^2 + (-0.20339940372771748 + x3)^2) + x11 * ((
    -0.4405711594738192 + x1)^2 + (-0.5080910724835329 + x2)^2 + (
    -0.18540147512570138 + x3)^2) + x12 * ((-0.36908840219684824 + x1)^2 + (
    -0.9606901577735717 + x2)^2 + (-0.1579661214699748 + x3)^2) + x13 * ((
    -0.39554390595886324 + x1)^2 + (-0.95517234425623 + x2)^2 + (
    -0.4357037242101963 + x3)^2) + x14 * ((-0.11324062660745182 + x1)^2 + (
    -0.1127227477493824 + x2)^2 + (-0.6775531466862447 + x3)^2) + x15 * ((
    -0.37207880369117297 + x1)^2 + (-0.4429785978155648 + x2)^2 + (
    -0.6160286803397987 + x3)^2) + x16 * ((-0.2361959619384585 + x1)^2 + (
    -0.6356037312017463 + x2)^2 + (-0.5117112742751293 + x3)^2) + x17 * ((
    -0.4447865236645254 + x1)^2 + (-0.33736132166151467 + x2)^2 + (
    -0.5880068862255667 + x3)^2) + x18 * ((-0.1880644612037895 + x1)^2 + (
    -0.8339460457426732 + x2)^2 + (-0.4642760100333919 + x3)^2) + x19 * ((
    -0.809678525848048 + x1)^2 + (-0.9810714270884835 + x2)^2 + (
    -0.22329339192222197 + x3)^2) + x20 * ((-0.9103106601121644 + x1)^2 + (
    -0.7530889196828001 + x2)^2 + (-0.2687229232888456 + x3)^2) + x21 * ((
    -0.2506681687047203 + x1)^2 + (-0.14874655132318948 + x2)^2 + (
    -0.7961773337916473 + x3)^2) + x22 * ((-0.5877634400149608 + x1)^2 + (
    -0.7175654971518651 + x2)^2 + (-0.6356627690183453 + x3)^2) + x23 * ((
    -0.7974452543446829 + x1)^2 + (-0.5323927624309212 + x2)^2 + (
    -0.9572021040304207 + x3)^2) + x24 * ((-0.5949737079161318 + x1)^2 + (
    -0.41675919028038244 + x2)^2 + (-0.25549007713931127 + x3)^2) + x25 * ((
    -0.05224072110626399 + x1)^2 + (-0.9684253307041065 + x2)^2 + (
    -0.03621367660020813 + x3)^2) + x26 * ((-0.9347003609994666 + x1)^2 + (
    -0.64358152389621 + x2)^2 + (-0.059814343789942215 + x3)^2) + x27 * ((
    -0.7935538449770041 + x1)^2 + (-0.11540895271984875 + x2)^2 + (
    -0.3946769068499303 + x3)^2) + x28 * ((-0.17385809015950826 + x1)^2 + (
    -0.45921932138562505 + x2)^2 + (-0.8256339099174179 + x3)^2) + x29 * ((
    -0.03835739793505788 + x1)^2 + (-0.6113872567578748 + x2)^2 + (
    -0.8718964927106821 + x3)^2) + x30 * ((-0.5739391076092649 + x1)^2 + (
    -0.5247196687429146 + x2)^2 + (-0.8533462318828052 + x3)^2) + x31 * ((
    -0.971075259349222 + x1)^2 + (-0.9104965674152667 + x2)^2 + (
    -0.7708929958995743 + x3)^2) + x32 * ((-0.5645353295297807 + x1)^2 + (
    -0.8584342772586054 + x2)^2 + (-0.8718267224700634 + x3)^2) + x33 * ((
    -0.6297483558228558 + x1)^2 + (-0.04014715139597247 + x2)^2 + (
    -0.09844847603361628 + x3)^2) + x34 * ((-0.5189119183247188 + x1)^2 + (
    -0.9474326272844581 + x2)^2 + (-0.5266109715772231 + x3)^2) + x35 * ((
    -0.6527900351730098 + x1)^2 + (-0.11052190591595967 + x2)^2 + (
    -0.5191880622085426 + x3)^2) + x36 * ((-0.10854173782735999 + x1)^2 + (
    -0.42093142780593973 + x2)^2 + (-0.31276103054202575 + x3)^2) + x37 * ((
    -0.3561489249032288 + x1)^2 + (-0.8268627589482757 + x2)^2 + (
    -0.1956453729075287 + x3)^2) + x38 * ((-0.4670221520529523 + x1)^2 + (
    -0.8891113977897892 + x2)^2 + (-0.27241504986579945 + x3)^2) + x39 * ((
    -0.35771749803339015 + x1)^2 + (-0.6044481060569854 + x2)^2 + (
    -0.7643630258273018 + x3)^2) + x40 * ((-0.04418354837503591 + x1)^2 + (
    -0.3102075900230633 + x2)^2 + (-0.8330809639446761 + x3)^2) + x41 * ((
    -0.8743744462324157 + x1)^2 + (-0.845910325959314 + x2)^2 + (
    -0.7140310051973626 + x3)^2) + x42 * ((-0.716502442685945 + x1)^2 + (
    -0.9515475221689099 + x2)^2 + (-0.6188065408222541 + x3)^2) + x43 * ((
    -0.06835345835265683 + x1)^2 + (-0.823370938809925 + x2)^2 + (
    -0.3389455123551257 + x3)^2) + x44 * ((-0.7757415343504088 + x1)^2 + (
    -0.7958264649791436 + x2)^2 + (-0.625436707143751 + x3)^2) + x45 * ((
    -0.9142760468526993 + x1)^2 + (-0.970911085347618 + x2)^2 + (
    -0.5429674014732869 + x3)^2) + x46 * ((-0.2096014409776199 + x1)^2 + (
    -0.9025289375492106 + x2)^2 + (-0.5287699855976883 + x3)^2) + x47 * ((
    -0.011619538885734193 + x1)^2 + (-0.12056474702179032 + x2)^2 + (
    -0.5981092250808783 + x3)^2) + x48 * ((-0.08114659947993563 + x1)^2 + (
    -0.441063194519585 + x2)^2 + (-0.9642109110625849 + x3)^2) + x49 * ((
    -0.3788010313673167 + x1)^2 + (-0.19367862019710247 + x2)^2 + (
    -0.7345907587139372 + x3)^2) + x50 * ((-0.02680831453838972 + x1)^2 + (
    -0.5010595635551833 + x2)^2 + (-0.5697272305278913 + x3)^2) + x51 * ((
    -0.9408661364624531 + x1)^2 + (-0.4084534281255007 + x2)^2 + (
    -0.5124759778704364 + x3)^2) + x52 * ((-0.7655175499270966 + x1)^2 + (
    -0.9482620910201023 + x2)^2 + (-0.27827134564381706 + x3)^2) + x53 * ((
    -0.8265432701686128 + x1)^2 + (-0.14848837551074712 + x2)^2 + (
    -0.20089309175503667 + x3)^2) + x54 * ((-0.8000481609994606 + x1)^2 + (
    -0.2539853139751347 + x2)^2 + (-0.20829630707197233 + x3)^2) + x55 * ((
    -0.26855105737847407 + x1)^2 + (-0.44920136283845336 + x2)^2 + (
    -0.41629666515596175 + x3)^2) + x56 * ((-0.7182882087805578 + x1)^2 + (
    -0.3793592905729698 + x2)^2 + (-0.17883837272616077 + x3)^2) + x57 * ((
    -0.19581024445686512 + x1)^2 + (-0.27181382773049567 + x2)^2 + (
    -0.322427225040845 + x3)^2) + x58 * ((-0.38658358127338854 + x1)^2 + (
    -0.7529124327703216 + x2)^2 + (-0.41910049255232174 + x3)^2) + x59 * ((
    -0.19143734810557733 + x1)^2 + (-0.48208401520816846 + x2)^2 + (
    -0.045061252030364485 + x3)^2) + x60 * ((-0.05682593455420182 + x1)^2 + (
    -0.7233915176300436 + x2)^2 + (-0.705103104979348 + x3)^2) + x61 * ((
    -0.9042027840926966 + x1)^2 + (-0.6938960112447266 + x2)^2 + (
    -0.3354994737557092 + x3)^2) + x62 * ((-0.7894861443951544 + x1)^2 + (
    -0.15244186536727333 + x2)^2 + (-0.5005398248336654 + x3)^2) + x63 * ((
    -0.34446185593752554 + x1)^2 + (-0.6772836129498278 + x2)^2 + (
    -0.7336734830314701 + x3)^2) + x64 * ((-0.20741666474163767 + x1)^2 + (
    -0.8202921977271875 + x2)^2 + (-0.5506009695439275 + x3)^2) + x65 * ((
    -0.5402923097092933 + x1)^2 + (-0.2675342734369003 + x2)^2 + (
    -0.7992890751698145 + x3)^2) + x66 * ((-0.27967022339776526 + x1)^2 + (
    -0.7979911425034355 + x2)^2 + (-0.46452645725265274 + x3)^2) + x67 * ((
    -0.9595819947527509 + x1)^2 + (-0.5232034354155645 + x2)^2 + (
    -0.2389966098134152 + x3)^2) + x68 * ((-0.07608991534038712 + x1)^2 + (
    -0.5736418691521828 + x2)^2 + (-0.019986186505803083 + x3)^2) + x69 * ((
    -0.42700398197897205 + x1)^2 + (-0.8010918625105746 + x2)^2 + (
    -0.8805692849635621 + x3)^2) + x70 * ((-0.5579869928092586 + x1)^2 + (
    -0.389498674450649 + x2)^2 + (-0.0748048271612155 + x3)^2) + x71 * ((
    -0.4070102263571985 + x1)^2 + (-0.7554593095435335 + x2)^2 + (
    -0.5904356558483927 + x3)^2) + x72 * ((-0.1364891447316846 + x1)^2 + (
    -0.8468918307965907 + x2)^2 + (-0.28700620952460276 + x3)^2) + x73 * ((
    -0.3367232340241588 + x1)^2 + (-0.8929968819838374 + x2)^2 + (
    -0.7484026014198896 + x3)^2) + x74 * ((-0.7635235105485991 + x1)^2 + (
    -0.5708091732053739 + x2)^2 + (-0.6753411475376285 + x3)^2) + x75 * ((
    -0.3651268993409923 + x1)^2 + (-0.12289882343337766 + x2)^2 + (
    -0.964009065158759 + x3)^2) + x76 * ((-0.8750166259121633 + x1)^2 + (
    -0.41383609996893045 + x2)^2 + (-0.29800741171032363 + x3)^2) + x77 * ((
    -0.40013800173743697 + x1)^2 + (-0.7249247652248746 + x2)^2 + (
    -0.6355874704603257 + x3)^2) + x78 * ((-0.18348856582977036 + x1)^2 + (
    -0.025854052500041358 + x2)^2 + (-0.2534534001576054 + x3)^2) + x79 * ((
    -0.9435154017754898 + x1)^2 + (-0.4392260710197824 + x2)^2 + (
    -0.4691516281413123 + x3)^2) + x80 * ((-0.7385168925807722 + x1)^2 + (
    -0.24644193646352752 + x2)^2 + (-0.17061742663080026 + x3)^2) + x81 * ((
    -0.05605633605668536 + x1)^2 + (-0.4912081682781063 + x2)^2 + (
    -0.5699993572568407 + x3)^2) + x82 * ((-0.15757181258844644 + x1)^2 + (
    -0.7303751725186297 + x2)^2 + (-0.9121598657835175 + x3)^2) + x83 * ((
    -0.33215497925633675 + x1)^2 + (-0.17028080871532403 + x2)^2 + (
    -0.3930063113045501 + x3)^2) + x84 * ((-0.7786941002157438 + x1)^2 + (
    -0.7405380151215268 + x2)^2 + (-0.9154339959764618 + x3)^2) + x85 * ((
    -0.7508193852295587 + x1)^2 + (-0.3803573428649786 + x2)^2 + (
    -0.22138614519182764 + x3)^2) + x86 * ((-0.9264682682309922 + x1)^2 + (
    -0.8873603073342023 + x2)^2 + (-0.864950588785591 + x3)^2) + x87 * ((
    -0.908267042284869 + x1)^2 + (-0.10298312771159246 + x2)^2 + (
    -0.6124646113776369 + x3)^2) + x88 * ((-0.16426882492973371 + x1)^2 + (
    -0.9869331956455133 + x2)^2 + (-0.719818452386762 + x3)^2) + x89 * ((
    -0.8825086613164931 + x1)^2 + (-0.08300173420348822 + x2)^2 + (
    -0.44087052443558905 + x3)^2) + x90 * ((-0.5130371082699586 + x1)^2 + (
    -0.7805872451248177 + x2)^2 + (-0.914693570552897 + x3)^2) + x91 * ((
    -0.12650358912449233 + x1)^2 + (-0.5342711885242658 + x2)^2 + (
    -0.3859086811884249 + x3)^2) + x92 * ((-0.021894498188813283 + x1)^2 + (
    -0.0027246625913778244 + x2)^2 + (-0.626856809181304 + x3)^2) + x93 * ((
    -0.8441678193498758 + x1)^2 + (-0.3509107664369997 + x2)^2 + (
    -0.23930665191922518 + x3)^2) + x94 * ((-0.9191544458905686 + x1)^2 + (
    -0.9295699343849126 + x2)^2 + (-0.5569494475068902 + x3)^2) + x95 * ((
    -0.35271055808467555 + x1)^2 + (-0.14001703168123492 + x2)^2 + (
    -0.4307833453831681 + x3)^2) + x96 * ((-0.015927077871251027 + x1)^2 + (
    -0.7944117141411271 + x2)^2 + (-0.0663323600363589 + x3)^2) + x97 * ((
    -0.06700957837304222 + x1)^2 + (-0.7245424124926254 + x2)^2 + (
    -0.04136030199658791 + x3)^2) + x98 * ((-0.6435908765286936 + x1)^2 + (
    -0.5608885129918921 + x2)^2 + (-0.29840288844009555 + x3)^2) + x99 * ((
    -0.0017744407035030774 + x1)^2 + (-0.5302888132806858 + x2)^2 + (
    -0.1070197893246232 + x3)^2) + x100 * ((-0.9960876588948411 + x1)^2 + (
    -0.5297980608672969 + x2)^2 + (-0.0967898406969584 + x3)^2) + x101 * ((
    -0.2966788147123718 + x1)^2 + (-0.4535896653892114 + x2)^2 + (
    -0.12490644679443152 + x3)^2) + x102 * ((-0.33141143322070366 + x1)^2 + (
    -0.28744907554291355 + x2)^2 + (-0.06994447154054817 + x3)^2) + x103 * ((
    -0.047933403792797424 + x1)^2 + (-0.8415471101830639 + x2)^2 + (
    -0.5955840833322725 + x3)^2) + x104 * ((-0.9171613034104257 + x1)^2 + (
    -0.6459943002822387 + x2)^2 + (-0.4152591826204478 + x3)^2) + x105 * ((
    -0.32790075407957764 + x1)^2 + (-0.4939517226351521 + x2)^2 + (
    -0.22989356871245614 + x3)^2) + x106 * ((-0.5844775505927844 + x1)^2 + (
    -0.7114551136263754 + x2)^2 + (-0.2605304125555207 + x3)^2) + x107 * ((
    -0.5855724678597634 + x1)^2 + (-0.5384124176079916 + x2)^2 + (
    -0.22873430477860057 + x3)^2) + x108 * ((-0.27448502514988804 + x1)^2 + (
    -0.8811058000942367 + x2)^2 + (-0.1084432011985692 + x3)^2) + x109 * ((
    -0.8087191675490594 + x1)^2 + (-0.36365530737786633 + x2)^2 + (
    -0.2551582076272405 + x3)^2) + x110 * ((-0.4692805537583873 + x1)^2 + (
    -0.1094763815311296 + x2)^2 + (-0.03308747009705737 + x3)^2) + x111 * ((
    -0.1414596675245341 + x1)^2 + (-0.05264608531324155 + x2)^2 + (
    -0.16232407961452555 + x3)^2) + x112 * ((-0.09502702610585512 + x1)^2 + (
    -0.6088439913367978 + x2)^2 + (-0.5808332695355897 + x3)^2) + x113 * ((
    -0.03790513829711473 + x1)^2 + (-0.5080181668023536 + x2)^2 + (
    -0.6682482244944306 + x3)^2) + x114 * ((-0.2398098003882162 + x1)^2 + (
    -0.40854299334338917 + x2)^2 + (-0.6265561387473995 + x3)^2) + x115 * ((
    -0.41352866202283534 + x1)^2 + (-0.13735597150040624 + x2)^2 + (
    -0.6575650750157317 + x3)^2) + x116 * ((-0.5918024287760949 + x1)^2 + (
    -0.9046254255858704 + x2)^2 + (-0.35259988628306405 + x3)^2) + x117 * ((
    -0.6163737698105297 + x1)^2 + (-0.7338484828210599 + x2)^2 + (
    -0.2552037957856732 + x3)^2) + x118 * ((-0.7481226352197995 + x1)^2 + (
    -0.6103864936538574 + x2)^2 + (-0.29319537619297076 + x3)^2) + x119 * ((
    -0.3817477016118834 + x1)^2 + (-0.28367233078996257 + x2)^2 + (
    -0.9065136963715262 + x3)^2) + x120 * ((-0.5387913922968426 + x1)^2 + (
    -0.9587122385639283 + x2)^2 + (-0.2849034277289415 + x3)^2) + x121 * ((
    -0.016896910716011626 + x1)^2 + (-0.542247494752311 + x2)^2 + (
    -0.35702504416839875 + x3)^2) + x122 * ((-0.0400792611431785 + x1)^2 + (
    -0.06003526247003277 + x2)^2 + (-0.8531074258574137 + x3)^2) + x123 * ((
    -0.6026500310542549 + x1)^2 + (-0.6934852370637312 + x2)^2 + (
    -0.3460238114357763 + x3)^2) + x124 * ((-0.55902762581076 + x1)^2 + (
    -0.9459788231528541 + x2)^2 + (-0.1290887862399902 + x3)^2) + x125 * ((
    -0.3837617695459321 + x1)^2 + (-0.3879093486846117 + x2)^2 + (
    -0.8849022163547949 + x3)^2) + x126 * ((-0.7720525818822013 + x1)^2 + (
    -0.1111500101946098 + x2)^2 + (-0.7661918097646079 + x3)^2) + x127 * ((
    -0.6344378078488477 + x1)^2 + (-0.38920253281074113 + x2)^2 + (
    -0.2569532307428819 + x3)^2) + x128 * ((-0.8429682238542169 + x1)^2 + (
    -0.28809038931293773 + x2)^2 + (-0.19175063574452433 + x3)^2) + x129 * ((
    -0.2672995256303895 + x1)^2 + (-0.03242383874322041 + x2)^2 + (
    -0.9842571124991794 + x3)^2) + x130 * ((-0.06540387850476659 + x1)^2 + (
    -0.24128518865484905 + x2)^2 + (-0.20517012144871016 + x3)^2) + x131 * ((
    -0.18621511189629547 + x1)^2 + (-0.30267745952007064 + x2)^2 + (
    -0.7114604662427862 + x3)^2) + x132 * ((-0.7893034114918972 + x1)^2 + (
    -0.0955677714501183 + x2)^2 + (-0.5821952996736662 + x3)^2) + x133 * ((
    -0.20739251640515832 + x1)^2 + (-0.8432910091332453 + x2)^2 + (
    -0.2586107102872377 + x3)^2) + x134 * ((-0.5530346239832239 + x1)^2 + (
    -0.37827958857876165 + x2)^2 + (-0.7781403692754599 + x3)^2) + x135 * ((
    -0.28092860002809394 + x1)^2 + (-0.8298897623230604 + x2)^2 + (
    -0.2719103553554957 + x3)^2) + x136 * ((-0.014925126786705656 + x1)^2 + (
    -0.12777278988662366 + x2)^2 + (-0.10588450075658606 + x3)^2) + x137 * ((
    -0.11668619210388753 + x1)^2 + (-0.3820666367049661 + x2)^2 + (
    -0.7791195974948653 + x3)^2) + x138 * ((-0.4344431981739817 + x1)^2 + (
    -0.1080485799315768 + x2)^2 + (-0.08340127233732786 + x3)^2) + x139 * ((
    -0.1793620960414819 + x1)^2 + (-0.3419484974871717 + x2)^2 + (
    -0.7820789010033935 + x3)^2) + x140 * ((-0.7165429642851615 + x1)^2 + (
    -0.9026914605710601 + x2)^2 + (-0.6935163617983727 + x3)^2) + x141 * ((
    -0.30965035870898905 + x1)^2 + (-0.6763312865753088 + x2)^2 + (
    -0.10472903251267174 + x3)^2) + x142 * ((-0.10216516132313902 + x1)^2 + (
    -0.5490230377748015 + x2)^2 + (-0.7352888807492108 + x3)^2) + x143 * ((
    -0.8651135909998409 + x1)^2 + (-0.29254598308074753 + x2)^2 + (
    -0.11864176567670415 + x3)^2) + x144 * ((-0.2101013503923751 + x1)^2 + (
    -0.8522411631472961 + x2)^2 + (-0.7212132885792959 + x3)^2) + x145 * ((
    -0.11131146834606975 + x1)^2 + (-0.09341511900076704 + x2)^2 + (
    -0.22436226860606978 + x3)^2) + x146 * ((-0.09589381898256144 + x1)^2 + (
    -0.62983098343096 + x2)^2 + (-0.236862989417864 + x3)^2) + x147 * ((
    -0.17134746819256785 + x1)^2 + (-0.0022191294485545132 + x2)^2 + (
    -0.5719632904418379 + x3)^2) + x148 * ((-0.1437717819667449 + x1)^2 + (
    -0.693066215236063 + x2)^2 + (-0.47910832437053097 + x3)^2) + x149 * ((
    -0.21326957505198796 + x1)^2 + (-0.5389938925764525 + x2)^2 + (
    -0.8985814053123515 + x3)^2) + x150 * ((-0.5267034399227511 + x1)^2 + (
    -0.16272083595464992 + x2)^2 + (-0.4424485927629499 + x3)^2) + x151 * ((
    -0.010171844468493396 + x1)^2 + (-0.8225385611520942 + x2)^2 + (
    -0.850081594460415 + x3)^2) + x152 * ((-0.9099126006489431 + x1)^2 + (
    -0.7117592498159224 + x2)^2 + (-0.24535211640166132 + x3)^2) + x153 * ((
    -0.8933095434728399 + x1)^2 + (-0.18696555428084993 + x2)^2 + (
    -0.14126880443170386 + x3)^2) + x154 * ((-0.05060465423810745 + x1)^2 + (
    -0.35889935243868054 + x2)^2 + (-0.9898462690273427 + x3)^2) + x155 * ((
    -0.28435588276815815 + x1)^2 + (-0.144413444054048 + x2)^2 + (
    -0.4912506689862507 + x3)^2) + x156 * ((-0.02377989350983456 + x1)^2 + (
    -0.4850739766720621 + x2)^2 + (-0.014220358160159874 + x3)^2) + x157 * ((
    -0.10685228340662356 + x1)^2 + (-0.4306857431033353 + x2)^2 + (
    -0.899717945016438 + x3)^2) + x158 * ((-0.7958123415938076 + x1)^2 + (
    -0.1567416212397551 + x2)^2 + (-0.4381463784299796 + x3)^2) + x159 * ((
    -0.20239323873555803 + x1)^2 + (-0.6688370928332699 + x2)^2 + (
    -0.8908782840570669 + x3)^2) + x160 * ((-0.8162377020493878 + x1)^2 + (
    -0.5538462537896983 + x2)^2 + (-0.46332413492756175 + x3)^2) + x161 * ((
    -0.3285436588025977 + x1)^2 + (-0.18234363029763911 + x2)^2 + (
    -0.9652199890334622 + x3)^2) + x162 * ((-0.1833756016631104 + x1)^2 + (
    -0.6191845385278278 + x2)^2 + (-0.3823840339936617 + x3)^2) + x163 * ((
    -0.9451306347207963 + x1)^2 + (-0.05696563611612815 + x2)^2 + (
    -0.31872989911510674 + x3)^2) + x164 * ((-0.1876172330243875 + x1)^2 + (
    -0.21273318417844989 + x2)^2 + (-0.7951342088420695 + x3)^2) + x165 * ((
    -0.6813385906412783 + x1)^2 + (-0.7795130804133624 + x2)^2 + (
    -0.8121251523108964 + x3)^2) + x166 * ((-0.5476385802163356 + x1)^2 + (
    -0.47082012503804105 + x2)^2 + (-0.1875779928301533 + x3)^2) + x167 * ((
    -0.4418603491118567 + x1)^2 + (-0.47814259051556174 + x2)^2 + (
    -0.843868091243698 + x3)^2) + x168 * ((-0.7227490532707296 + x1)^2 + (
    -0.6305946284321624 + x2)^2 + (-0.7778431141977471 + x3)^2) + x169 * ((
    -0.44449821578332316 + x1)^2 + (-0.7010434784223998 + x2)^2 + (
    -0.4562440307525807 + x3)^2) + x170 * ((-0.8207794357127131 + x1)^2 + (
    -0.2715928586111269 + x2)^2 + (-0.8111077485955768 + x3)^2) + x171 * ((
    -0.06913168314217966 + x1)^2 + (-0.17062534115061545 + x2)^2 + (
    -0.7186204035119522 + x3)^2) + x172 * ((-0.9356572299847938 + x1)^2 + (
    -0.25247506111569284 + x2)^2 + (-0.3766500744907605 + x3)^2) + x173 * ((
    -0.053183850751484685 + x1)^2 + (-0.503319761819413 + x2)^2 + (
    -0.3988792529665396 + x3)^2) + x174 * ((-0.6348345247106641 + x1)^2 + (
    -0.7372264972225206 + x2)^2 + (-0.2816805911685105 + x3)^2) + x175 * ((
    -0.4922332187206825 + x1)^2 + (-0.12955383972526402 + x2)^2 + (
    -0.6759110290426272 + x3)^2) + x176 * ((-0.3039899015675839 + x1)^2 + (
    -0.8701136133070226 + x2)^2 + (-0.3415605267108113 + x3)^2) + x177 * ((
    -0.19249833111625447 + x1)^2 + (-0.289199436536963 + x2)^2 + (
    -0.17001661008163982 + x3)^2) + x178 * ((-0.41498929870378265 + x1)^2 + (
    -0.6714872892529845 + x2)^2 + (-0.7734373760087199 + x3)^2) + x179 * ((
    -0.6414826763544017 + x1)^2 + (-0.833907205124963 + x2)^2 + (
    -0.5454186218286011 + x3)^2) + x180 * ((-0.8018985643443416 + x1)^2 + (
    -0.18267498327347076 + x2)^2 + (-0.6248398639397298 + x3)^2) + x181 * ((
    -0.011710686297021211 + x1)^2 + (-0.7293978925979899 + x2)^2 + (
    -0.062110132255305706 + x3)^2) + x182 * ((-0.3522173993348232 + x1)^2 + (
    -0.07284835414901125 + x2)^2 + (-0.6849529919886285 + x3)^2) + x183 * ((
    -0.12185440522884461 + x1)^2 + (-0.6687199057889921 + x2)^2 + (
    -0.13946873559425443 + x3)^2) + x184 * ((-0.8925626716041768 + x1)^2 + (
    -0.5507535962948702 + x2)^2 + (-0.7754292445803886 + x3)^2) + x185 * ((
    -0.6737722608457104 + x1)^2 + (-0.6835956974473757 + x2)^2 + (
    -0.11220963763590197 + x3)^2) + x186 * ((-0.2056780683513766 + x1)^2 + (
    -0.7777969577351744 + x2)^2 + (-0.7818523629215165 + x3)^2) + x187 * ((
    -0.35040653667397936 + x1)^2 + (-0.7218237888483313 + x2)^2 + (
    -0.24223482432840604 + x3)^2) + x188 * ((-0.045519582549019444 + x1)^2 + (
    -0.2468399938697886 + x2)^2 + (-0.5509847497355672 + x3)^2) + x189 * ((
    -0.7625095428789862 + x1)^2 + (-0.38693097091538686 + x2)^2 + (
    -0.8447744154325253 + x3)^2) + x190 * ((-0.47706955962867537 + x1)^2 + (
    -0.9048825326627299 + x2)^2 + (-0.6698420394228831 + x3)^2) + x191 * ((
    -0.9220722254195256 + x1)^2 + (-0.9093919260950618 + x2)^2 + (
    -0.3585536965409931 + x3)^2) + x192 * ((-0.42421741345016817 + x1)^2 + (
    -0.1810097690077137 + x2)^2 + (-0.11838106532964576 + x3)^2) + x193 * ((
    -0.7909025678257156 + x1)^2 + (-0.6683526078945575 + x2)^2 + (
    -0.5109886309751906 + x3)^2) + x194 * ((-0.28703506025246406 + x1)^2 + (
    -0.6439491320749008 + x2)^2 + (-0.7706022456077256 + x3)^2) + x195 * ((
    -0.13459246208619924 + x1)^2 + (-0.28097209258600253 + x2)^2 + (
    -0.10489080047801336 + x3)^2) + x196 * ((-0.3523855983171982 + x1)^2 + (
    -0.4248157381430815 + x2)^2 + (-0.6906133929926649 + x3)^2) + x197 * ((
    -0.1583698558934198 + x1)^2 + (-0.9210909019600683 + x2)^2 + (
    -0.6395026018640236 + x3)^2) + x198 * ((-0.7869061505221948 + x1)^2 + (
    -0.7078900011730935 + x2)^2 + (-0.6196010572637488 + x3)^2) + x199 * ((
    -0.5687640083646678 + x1)^2 + (-0.5772192111740503 + x2)^2 + (
    -0.6138822482643156 + x3)^2) + x200 * ((-0.7139842499777261 + x1)^2 + (
    -0.11680023910927528 + x2)^2 + (-0.2506224434653087 + x3)^2) + x201 * ((
    -0.805568392008547 + x1)^2 + (-0.06545005124609204 + x2)^2 + (
    -0.032700612578027144 + x3)^2) + x202 * ((-0.8672418514729174 + x1)^2 + (
    -0.9495334316535684 + x2)^2 + (-0.9506671434655545 + x3)^2) + x203 * ((
    -0.8428186951044521 + x1)^2 + (-0.2491784563178132 + x2)^2 + (
    -0.8574700961978342 + x3)^2) + x204 * ((-0.3871201049109313 + x1)^2 + (
    -0.9738876810785931 + x2)^2 + (-0.613114261845513 + x3)^2) + x205 * ((
    -0.9150831066517291 + x1)^2 + (-0.8126407462368724 + x2)^2 + (
    -0.32527791429850705 + x3)^2) + x206 * ((-0.13884237948432931 + x1)^2 + (
    -0.05350519336412973 + x2)^2 + (-0.24780684370452688 + x3)^2) + x207 * ((
    -0.7923572326382577 + x1)^2 + (-0.16987369545737896 + x2)^2 + (
    -0.9459861441672113 + x3)^2) + x208 * ((-0.8287350086957515 + x1)^2 + (
    -0.2701283953407778 + x2)^2 + (-0.38893185458031276 + x3)^2) + x209 * ((
    -0.8419989467911838 + x1)^2 + (-0.36305399780969094 + x2)^2 + (
    -0.5097745885449746 + x3)^2) + x210 * ((-0.9328252563464429 + x1)^2 + (
    -0.6938288661186377 + x2)^2 + (-0.5178576561761775 + x3)^2) + x211 * ((
    -0.13394390692618663 + x1)^2 + (-0.1707402476262171 + x2)^2 + (
    -0.049978421880908175 + x3)^2) + x212 * ((-0.9344145063124553 + x1)^2 + (
    -0.5642986722348461 + x2)^2 + (-0.9742283497162917 + x3)^2) + x213 * ((
    -0.12917904997198593 + x1)^2 + (-0.8291714054039813 + x2)^2 + (
    -0.1461208778099089 + x3)^2) + x214 * ((-0.49297041535442676 + x1)^2 + (
    -0.9997056001066135 + x2)^2 + (-0.9984805276449421 + x3)^2) + x215 * ((
    -0.9443406401848632 + x1)^2 + (-0.9556643724533576 + x2)^2 + (
    -0.7626439658137829 + x3)^2) + x216 * ((-0.4927277418379675 + x1)^2 + (
    -0.24978712865953823 + x2)^2 + (-0.33279356513981784 + x3)^2) + x217 * ((
    -0.6628894265876931 + x1)^2 + (-0.08815384447750985 + x2)^2 + (
    -0.02837052028209286 + x3)^2) + x218 * ((-0.5951215974793173 + x1)^2 + (
    -0.6709917301275213 + x2)^2 + (-0.5228016909019687 + x3)^2) + x219 * ((
    -0.3628434072386518 + x1)^2 + (-0.5648955285747782 + x2)^2 + (
    -0.14037475292742752 + x3)^2) + x220 * ((-0.6315358621764737 + x1)^2 + (
    -0.4940040944835772 + x2)^2 + (-0.39393981108383724 + x3)^2) + x221 * ((
    -0.23895764723651125 + x1)^2 + (-0.4925466699958012 + x2)^2 + (
    -0.6798787131541073 + x3)^2) + x222 * ((-0.33431465619738565 + x1)^2 + (
    -0.02990879062461249 + x2)^2 + (-0.98627846080786 + x3)^2) + x223 * ((
    -0.20138845604638655 + x1)^2 + (-0.07286113290687579 + x2)^2 + (
    -0.7389461293858135 + x3)^2) + x224 * ((-0.22043310505100588 + x1)^2 + (
    -0.6921624888940164 + x2)^2 + (-0.7390910692714129 + x3)^2) + x225 * ((
    -0.1794768509914445 + x1)^2 + (-0.19971018619617786 + x2)^2 + (
    -0.1252179745377201 + x3)^2) + x226 * ((-0.4316525971751499 + x1)^2 + (
    -0.9293948927573288 + x2)^2 + (-0.6357217625876419 + x3)^2) + x227 * ((
    -0.19054858574619327 + x1)^2 + (-0.6597186703227657 + x2)^2 + (
    -0.7437070343450088 + x3)^2) + x228 * ((-0.5401665990210613 + x1)^2 + (
    -0.31975882224981744 + x2)^2 + (-0.7676783575559698 + x3)^2) + x229 * ((
    -0.7141585569819535 + x1)^2 + (-0.5821205832955013 + x2)^2 + (
    -0.9414136448749184 + x3)^2) + x230 * ((-0.44737341471901404 + x1)^2 + (
    -0.9048222764719899 + x2)^2 + (-0.7461921038282987 + x3)^2) + x231 * ((
    -0.6074944823231694 + x1)^2 + (-0.4144292990749079 + x2)^2 + (
    -0.9448146796490002 + x3)^2) + x232 * ((-0.7711535942806756 + x1)^2 + (
    -0.18386931660223416 + x2)^2 + (-0.9382198399195494 + x3)^2) + x233 * ((
    -0.6654811389399782 + x1)^2 + (-0.7664480958655735 + x2)^2 + (
    -0.8043855734520027 + x3)^2) + x234 * ((-0.13574356640083862 + x1)^2 + (
    -0.8006073394818852 + x2)^2 + (-0.4293460234558568 + x3)^2) + x235 * ((
    -0.88109422081292 + x1)^2 + (-0.2521523305664952 + x2)^2 + (
    -0.2783612988957984 + x3)^2) + x236 * ((-0.21098683574670196 + x1)^2 + (
    -0.5793487573072326 + x2)^2 + (-0.1400427387047346 + x3)^2) + x237 * ((
    -0.5287988551538474 + x1)^2 + (-0.9641191628237653 + x2)^2 + (
    -0.9601811389639257 + x3)^2) + x238 * ((-0.6356835687091966 + x1)^2 + (
    -0.5035384241376479 + x2)^2 + (-0.912561201496254 + x3)^2) + x239 * ((
    -0.07022860689714527 + x1)^2 + (-0.7272172999901972 + x2)^2 + (
    -0.813209953545937 + x3)^2) + x240 * ((-0.8817216558635385 + x1)^2 + (
    -0.1961060970257913 + x2)^2 + (-0.4807253834719928 + x3)^2) + x241 * ((
    -0.8346893143895587 + x1)^2 + (-0.45391356191841836 + x2)^2 + (
    -0.03689848229389647 + x3)^2) + x242 * ((-0.4425064296341201 + x1)^2 + (
    -0.23133455702646433 + x2)^2 + (-0.4119733748205944 + x3)^2) + x243 * ((
    -0.48695930579230606 + x1)^2 + (-0.7723781894795173 + x2)^2 + (
    -0.7896048032875119 + x3)^2) + x244 * ((-0.6213072525945529 + x1)^2 + (
    -0.7463861427401226 + x2)^2 + (-0.19336124087532391 + x3)^2) + x245 * ((
    -0.9407434249412069 + x1)^2 + (-0.3157287888226875 + x2)^2 + (
    -0.19110493027237785 + x3)^2) + x246 * ((-0.5838103888478602 + x1)^2 + (
    -0.21478748867734254 + x2)^2 + (-0.8827349895451565 + x3)^2) + x247 * ((
    -0.03393239301609985 + x1)^2 + (-0.34669040395859996 + x2)^2 + (
    -0.6798250093428466 + x3)^2) + x248 * ((-0.9597035244408724 + x1)^2 + (
    -0.32286881217800434 + x2)^2 + (-0.4444196733141058 + x3)^2) + x249 * ((
    -0.9457000140765058 + x1)^2 + (-0.5068775796046029 + x2)^2 + (
    -0.3144273334897483 + x3)^2) + x250 * ((-0.044943238020383025 + x1)^2 + (
    -0.6614992336502294 + x2)^2 + (-0.8388656671250995 + x3)^2) + x251 * ((
    -0.49927342074497827 + x1)^2 + (-0.13468517272379243 + x2)^2 + (
    -0.4296515446930951 + x3)^2) + x252 * ((-0.9841852779169674 + x1)^2 + (
    -0.9843149988050245 + x2)^2 + (-0.47713010572283376 + x3)^2) + x253 * ((
    -0.4009300133770608 + x1)^2 + (-0.0042534179821622775 + x2)^2 + (
    -0.4175816329130312 + x3)^2) + x254 * ((-0.4885283879651544 + x1)^2 + (
    -0.9079239735865996 + x2)^2 + (-0.21031335265116158 + x3)^2) + x255 * ((
    -0.9849314196407067 + x1)^2 + (-0.11685357326709411 + x2)^2 + (
    -0.017369390966105014 + x3)^2) + x256 * ((-0.35446426043635526 + x1)^2 + (
    -0.2596023514638419 + x2)^2 + (-0.32096060367647117 + x3)^2) + x257 * ((
    -0.4352313328405867 + x1)^2 + (-0.6746955457244538 + x2)^2 + (
    -0.25563185786498377 + x3)^2) + x258 * ((-0.699315061557881 + x1)^2 + (
    -0.5915408096298286 + x2)^2 + (-0.44607763336915063 + x3)^2) + x259 * ((
    -0.6592318565406342 + x1)^2 + (-0.6133226566520651 + x2)^2 + (
    -0.5961918051667695 + x3)^2) + x260 * ((-0.2354774655941887 + x1)^2 + (
    -0.26243234628674394 + x2)^2 + (-0.312388269065189 + x3)^2) + x261 * ((
    -0.2200373888643452 + x1)^2 + (-0.41332951956449515 + x2)^2 + (
    -0.9109131978387711 + x3)^2) + x262 * ((-0.9487139910966843 + x1)^2 + (
    -0.5437246273285123 + x2)^2 + (-0.07874373064662499 + x3)^2) + x263 * ((
    -0.5964830453719224 + x1)^2 + (-0.0619742726091832 + x2)^2 + (
    -0.19927236817826444 + x3)^2) + x264 * ((-0.02759692117192214 + x1)^2 + (
    -0.2966943519059587 + x2)^2 + (-0.1436425270697561 + x3)^2) + x265 * ((
    -0.5605238341170351 + x1)^2 + (-0.16705196889000828 + x2)^2 + (
    -0.4596742351263795 + x3)^2) + x266 * ((-0.9861110555193163 + x1)^2 + (
    -0.8752990513886425 + x2)^2 + (-0.485142331599836 + x3)^2) + x267 * ((
    -0.27161250758957267 + x1)^2 + (-0.9946863069500006 + x2)^2 + (
    -0.439561525186691 + x3)^2) + x268 * ((-0.4836297090054381 + x1)^2 + (
    -0.2114798303676434 + x2)^2 + (-0.1278618145726882 + x3)^2) + x269 * ((
    -0.024736008778174612 + x1)^2 + (-0.9205199923700449 + x2)^2 + (
    -0.8484339940268846 + x3)^2) + x270 * ((-0.5626615620602874 + x1)^2 + (
    -0.034989370194508096 + x2)^2 + (-0.6632186742091526 + x3)^2) + x271 * ((
    -0.6438064560050359 + x1)^2 + (-0.4889465681575601 + x2)^2 + (
    -0.26934659936523253 + x3)^2) + x272 * ((-0.5261992201164788 + x1)^2 + (
    -0.08595932986749422 + x2)^2 + (-0.08488216145362637 + x3)^2) + x273 * ((
    -0.1409322982901524 + x1)^2 + (-0.11290088677205301 + x2)^2 + (
    -0.1848610267768337 + x3)^2) + x274 * ((-0.9062469407729168 + x1)^2 + (
    -0.443642723519166 + x2)^2 + (-0.16301234345822146 + x3)^2) + x275 * ((
    -0.26280187243977027 + x1)^2 + (-0.5791906957767239 + x2)^2 + (
    -0.09189211557137555 + x3)^2) + x276 * ((-0.7819362020918313 + x1)^2 + (
    -0.8107913530336736 + x2)^2 + (-0.08589261011414395 + x3)^2) + x277 * ((
    -0.12202077612002771 + x1)^2 + (-0.09381851826448306 + x2)^2 + (
    -0.9946687189369333 + x3)^2) + x278 * ((-0.7449921585503891 + x1)^2 + (
    -0.44616399084793734 + x2)^2 + (-0.14733396356242667 + x3)^2) + x279 * ((
    -0.8013267039644335 + x1)^2 + (-0.12726406694941528 + x2)^2 + (
    -0.30755184402270597 + x3)^2) + x280 * ((-0.7129868679977376 + x1)^2 + (
    -0.5624403504682522 + x2)^2 + (-0.5194087287496278 + x3)^2) + x281 * ((
    -0.702605402074762 + x1)^2 + (-0.696542187378441 + x2)^2 + (
    -0.9050186102050559 + x3)^2) + x282 * ((-0.48579654846686027 + x1)^2 + (
    -0.9865716657785814 + x2)^2 + (-0.7488638018945105 + x3)^2) + x283 * ((
    -0.14273183621265262 + x1)^2 + (-0.16961426380712896 + x2)^2 + (
    -0.7336118920897162 + x3)^2) + x284 * ((-0.508565000330308 + x1)^2 + (
    -0.0008598073433415676 + x2)^2 + (-0.4878861682744219 + x3)^2) + x285 * ((
    -0.37778026211733495 + x1)^2 + (-0.7302042173061916 + x2)^2 + (
    -0.658072993274222 + x3)^2) + x286 * ((-0.5859039531200585 + x1)^2 + (
    -0.28185196746339947 + x2)^2 + (-0.07351170392618223 + x3)^2) + x287 * ((
    -0.437816105636769 + x1)^2 + (-0.9381650700676218 + x2)^2 + (
    -0.7532133630650687 + x3)^2) + x288 * ((-0.9111142352615409 + x1)^2 + (
    -0.9188611987954707 + x2)^2 + (-0.7097765364993713 + x3)^2) + x289 * ((
    -0.6070364816449836 + x1)^2 + (-0.6368688399261839 + x2)^2 + (
    -0.8097201734033257 + x3)^2) + x290 * ((-0.6984482644711556 + x1)^2 + (
    -0.8822045583167333 + x2)^2 + (-0.5762293092462573 + x3)^2) + x291 * ((
    -0.05085683485354919 + x1)^2 + (-0.9999183826637328 + x2)^2 + (
    -0.4287782578354542 + x3)^2) + x292 * ((-0.7615905094162454 + x1)^2 + (
    -0.1421067735442294 + x2)^2 + (-0.5006086214169991 + x3)^2) + x293 * ((
    -0.9305602823426583 + x1)^2 + (-0.9752940115114439 + x2)^2 + (
    -0.1631253855890934 + x3)^2) + x294 * ((-0.26027159077598117 + x1)^2 + (
    -0.8467561936966935 + x2)^2 + (-0.42577439882602497 + x3)^2) + x295 * ((
    -0.08104856848069275 + x1)^2 + (-0.9886967089077169 + x2)^2 + (
    -0.08146796574801807 + x3)^2) + x296 * ((-0.48005659566609715 + x1)^2 + (
    -0.9974410345330987 + x2)^2 + (-0.48571859403846973 + x3)^2) + x297 * ((
    -0.4706070697040865 + x1)^2 + (-0.22633844473105058 + x2)^2 + (
    -0.8430722417451099 + x3)^2) + x298 * ((-0.6581283586576836 + x1)^2 + (
    -0.2988361857206986 + x2)^2 + (-0.5248717962910134 + x3)^2) + x299 * ((
    -0.4139397565643148 + x1)^2 + (-0.7947219857264776 + x2)^2 + (
    -0.9714023432927014 + x3)^2) + x300 * ((-0.29895041273047895 + x1)^2 + (
    -0.20934319073619012 + x2)^2 + (-0.12799433802173388 + x3)^2) + x301 * ((
    -0.7416051505394204 + x1)^2 + (-0.8610181415202831 + x2)^2 + (
    -0.8203512359906585 + x3)^2) + x302 * ((-0.8539442696762753 + x1)^2 + (
    -0.6440119856376406 + x2)^2 + (-0.04768006379778733 + x3)^2) + x303 * ((
    -0.8078856580669804 + x1)^2 + (-0.0811738770099133 + x2)^2 + (
    -0.42296333968011834 + x3)^2) + x304 * ((-0.11293172487506897 + x1)^2 + (
    -0.10190845514217972 + x2)^2 + (-0.025155476939746846 + x3)^2) + x305 * ((
    -0.6774554514175933 + x1)^2 + (-0.28953130741751354 + x2)^2 + (
    -0.7231890256224531 + x3)^2) + x306 * ((-0.9658389665612165 + x1)^2 + (
    -0.8012920581552374 + x2)^2 + (-0.6871461962217258 + x3)^2) + x307 * ((
    -0.5345563351474161 + x1)^2 + (-0.11378244706430707 + x2)^2 + (
    -0.7915828478976272 + x3)^2) + x308 * ((-0.9997767651100092 + x1)^2 + (
    -0.5574720960939473 + x2)^2 + (-0.7410926285969115 + x3)^2) + x309 * ((
    -0.29777709756222204 + x1)^2 + (-0.13420768997570653 + x2)^2 + (
    -0.41098786274229304 + x3)^2) + x310 * ((-0.4890881424574446 + x1)^2 + (
    -0.404669840371118 + x2)^2 + (-0.6839329573384761 + x3)^2) + x311 * ((
    -0.9275207698350674 + x1)^2 + (-0.6349688118385305 + x2)^2 + (
    -0.16211201636277606 + x3)^2) + x312 * ((-0.31185430455711194 + x1)^2 + (
    -0.9609480087595885 + x2)^2 + (-0.48506492880423546 + x3)^2) + x313 * ((
    -0.7594140721620825 + x1)^2 + (-0.9263148514595829 + x2)^2 + (
    -0.8648033086118 + x3)^2) + x314 * ((-0.6479304574703105 + x1)^2 + (
    -0.8228423329287321 + x2)^2 + (-0.7551761939784829 + x3)^2) + x315 * ((
    -0.8231579504797958 + x1)^2 + (-0.05635445777892223 + x2)^2 + (
    -0.02468508246924883 + x3)^2) + x316 * ((-0.5969304027180449 + x1)^2 + (
    -0.8273519061055513 + x2)^2 + (-0.8975627019214554 + x3)^2) + x317 * ((
    -0.47032986801594845 + x1)^2 + (-0.03758087479779437 + x2)^2 + (
    -0.956428581402661 + x3)^2) + x318 * ((-0.058484373437283965 + x1)^2 + (
    -0.7224332485058074 + x2)^2 + (-0.36656511074725406 + x3)^2) + x319 * ((
    -0.8067441195220981 + x1)^2 + (-0.6939130038104055 + x2)^2 + (
    -0.6650852436958627 + x3)^2) + x320 * ((-0.14316346421133996 + x1)^2 + (
    -0.8833335241651658 + x2)^2 + (-0.33873721710142757 + x3)^2) + x321 * ((
    -0.16663405286282917 + x1)^2 + (-0.1361097149511954 + x2)^2 + (
    -0.4167589692247934 + x3)^2) + x322 * ((-0.3533518801743728 + x1)^2 + (
    -0.7864769418639855 + x2)^2 + (-0.5700369360657614 + x3)^2) + x323 * ((
    -0.9940450532017178 + x1)^2 + (-0.8709964325378182 + x2)^2 + (
    -0.05370495768985595 + x3)^2) + x324 * ((-0.43669423470125 + x1)^2 + (
    -0.7826943195653798 + x2)^2 + (-0.08246841776453673 + x3)^2) + x325 * ((
    -0.31217298303878716 + x1)^2 + (-0.12873842883308007 + x2)^2 + (
    -0.4120375477605329 + x3)^2) + x326 * ((-0.04729057034546036 + x1)^2 + (
    -0.615848875622511 + x2)^2 + (-0.09028092669134402 + x3)^2) + x327 * ((
    -0.05579397155334043 + x1)^2 + (-0.45731350085562406 + x2)^2 + (
    -0.5113200354339912 + x3)^2) + x328 * ((-0.24317770299974573 + x1)^2 + (
    -0.31432958156550617 + x2)^2 + (-0.29916426285821995 + x3)^2) + x329 * ((
    -0.6647683703847979 + x1)^2 + (-0.5720315504033884 + x2)^2 + (
    -0.3330271930609998 + x3)^2) + x330 * ((-0.0671508784075493 + x1)^2 + (
    -0.7427046256777622 + x2)^2 + (-0.3842554432358185 + x3)^2) + x331 * ((
    -0.5142618830032626 + x1)^2 + (-0.37920880558154235 + x2)^2 + (
    -0.17375109475213701 + x3)^2) + x332 * ((-0.039030898150579474 + x1)^2 + (
    -0.416088697819994 + x2)^2 + (-0.23777905803288724 + x3)^2) + x333 * ((
    -0.4717971485183111 + x1)^2 + (-0.3383860380066811 + x2)^2 + (
    -0.460200523195855 + x3)^2) + x334 * ((-0.5900378880204267 + x1)^2 + (
    -0.7255901375319337 + x2)^2 + (-0.9154170002928985 + x3)^2) + x335 * ((
    -0.13093900398824065 + x1)^2 + (-0.4052139060110297 + x2)^2 + (
    -0.49962194728297327 + x3)^2) + x336 * ((-0.5001698078829642 + x1)^2 + (
    -0.7979303589649438 + x2)^2 + (-0.2739293646511145 + x3)^2) + x337 * ((
    -0.41855315898554013 + x1)^2 + (-0.998699983121554 + x2)^2 + (
    -0.2010058221141684 + x3)^2) + x338 * ((-0.7496871098706305 + x1)^2 + (
    -0.8235726845357767 + x2)^2 + (-0.37015198039038577 + x3)^2) + x339 * ((
    -0.28403104119909195 + x1)^2 + (-0.6420274479177237 + x2)^2 + (
    -0.4574273157370161 + x3)^2) + x340 * ((-0.46685731585307466 + x1)^2 + (
    -0.26906412522677103 + x2)^2 + (-0.6656657277253054 + x3)^2) + x341 * ((
    -0.2504282905612786 + x1)^2 + (-0.15851796206472113 + x2)^2 + (
    -0.4726147469986297 + x3)^2) + x342 * ((-0.21194510336903394 + x1)^2 + (
    -0.7789673451440703 + x2)^2 + (-0.09841245851637492 + x3)^2) + x343 * ((
    -0.2349671005207027 + x1)^2 + (-0.0221927931737832 + x2)^2 + (
    -0.5712554822182071 + x3)^2) + x344 * ((-0.0009451790835207641 + x1)^2 + (
    -0.2408337245798331 + x2)^2 + (-0.6211924391868702 + x3)^2) + x345 * ((
    -0.6707250517356161 + x1)^2 + (-0.5984637186180205 + x2)^2 + (
    -0.0668641338162419 + x3)^2) + x346 * ((-0.5511472131778885 + x1)^2 + (
    -0.07350867542191697 + x2)^2 + (-0.767739792767608 + x3)^2) + x347 * ((
    -0.9501581392192964 + x1)^2 + (-0.7233163389390355 + x2)^2 + (
    -0.5166844510344849 + x3)^2) + x348 * ((-0.9060156230362852 + x1)^2 + (
    -0.3113487821639962 + x2)^2 + (-0.20778084543419917 + x3)^2) + x349 * ((
    -0.5288680482784139 + x1)^2 + (-0.2934145990378463 + x2)^2 + (
    -0.4804974743654282 + x3)^2) + x350 * ((-0.09966115943905263 + x1)^2 + (
    -0.3938725699296275 + x2)^2 + (-0.32444318785821924 + x3)^2) + x351 * ((
    -0.6520321563540667 + x1)^2 + (-0.8056068500183343 + x2)^2 + (
    -0.0835838533559482 + x3)^2) + x352 * ((-0.8166208988287386 + x1)^2 + (
    -0.3518761684344235 + x2)^2 + (-0.7464113961140431 + x3)^2) + x353 * ((
    -0.1311593203796163 + x1)^2 + (-0.7160405481109373 + x2)^2 + (
    -0.09952132645843448 + x3)^2) + x354 * ((-0.04779808112037798 + x1)^2 + (
    -0.28884699291713234 + x2)^2 + (-0.10250649388727473 + x3)^2) + x355 * ((
    -0.9791729605203251 + x1)^2 + (-0.6726875461066422 + x2)^2 + (
    -0.9283118905188722 + x3)^2) + x356 * ((-0.13471412533270244 + x1)^2 + (
    -0.7071806165289065 + x2)^2 + (-0.9043216254262293 + x3)^2) + x357 * ((
    -0.5735353939945473 + x1)^2 + (-0.5273208712530736 + x2)^2 + (
    -0.6875628347914862 + x3)^2) + x358 * ((-0.9582137553329777 + x1)^2 + (
    -0.4500040273602035 + x2)^2 + (-0.26668127604253744 + x3)^2) + x359 * ((
    -0.35515505710029105 + x1)^2 + (-0.8998261443565795 + x2)^2 + (
    -0.5147227718297207 + x3)^2) + x360 * ((-0.9340214668622013 + x1)^2 + (
    -0.3503931266703305 + x2)^2 + (-0.22213442770583658 + x3)^2) + x361 * ((
    -0.30063857818433126 + x1)^2 + (-0.9781639681666726 + x2)^2 + (
    -0.5737192124395999 + x3)^2) + x362 * ((-0.9694287446674323 + x1)^2 + (
    -0.9139936410886877 + x2)^2 + (-0.16757766484105074 + x3)^2) + x363 * ((
    -0.040594150617694 + x1)^2 + (-0.43898895567045837 + x2)^2 + (
    -0.6978737824797022 + x3)^2) + x364 * ((-0.9047320599530371 + x1)^2 + (
    -0.4912564771269612 + x2)^2 + (-0.6733487941467664 + x3)^2) + x365 * ((
    -0.9549617147031715 + x1)^2 + (-0.6678649305928561 + x2)^2 + (
    -0.8834928821311292 + x3)^2) + x366 * ((-0.4395498573390294 + x1)^2 + (
    -0.30627811842262354 + x2)^2 + (-0.9750459496357505 + x3)^2) + x367 * ((
    -0.1870595942163641 + x1)^2 + (-0.151585797566554 + x2)^2 + (
    -0.6096114448910821 + x3)^2) + x368 * ((-0.8951229638762037 + x1)^2 + (
    -0.5978267742373706 + x2)^2 + (-0.5837237511628297 + x3)^2) + x369 * ((
    -0.9979607832682635 + x1)^2 + (-0.2544630128273442 + x2)^2 + (
    -0.7553436617442503 + x3)^2) + x370 * ((-0.18874920320016164 + x1)^2 + (
    -0.6216165758809351 + x2)^2 + (-0.8529149249653111 + x3)^2) + x371 * ((
    -0.6373429941144889 + x1)^2 + (-0.03524085604839855 + x2)^2 + (
    -0.2902922940078507 + x3)^2) + x372 * ((-0.1493240329654184 + x1)^2 + (
    -0.773610378940084 + x2)^2 + (-0.16800156102583386 + x3)^2) + x373 * ((
    -0.45959660687249615 + x1)^2 + (-0.8091285040534932 + x2)^2 + (
    -0.3286890399482034 + x3)^2) + x374 * ((-0.7478644912889102 + x1)^2 + (
    -0.014858297372218665 + x2)^2 + (-0.6866332635878059 + x3)^2) + x375 * ((
    -0.7646420573532026 + x1)^2 + (-0.9447630530244876 + x2)^2 + (
    -0.8190368275925283 + x3)^2) + x376 * ((-0.9924396130442916 + x1)^2 + (
    -0.6082265831465189 + x2)^2 + (-0.5057251733236754 + x3)^2) + x377 * ((
    -0.7721758593783997 + x1)^2 + (-0.8129769760490057 + x2)^2 + (
    -0.4066778113300017 + x3)^2) + x378 * ((-0.5586622471964208 + x1)^2 + (
    -0.7449498935310548 + x2)^2 + (-0.5133001652292216 + x3)^2) + x379 * ((
    -0.2606143437838706 + x1)^2 + (-0.9157831128583509 + x2)^2 + (
    -0.7725742539135185 + x3)^2) + x380 * ((-0.08665312749944609 + x1)^2 + (
    -0.20774241016302275 + x2)^2 + (-0.392846511749778 + x3)^2) + x381 * ((
    -0.02318360583183654 + x1)^2 + (-0.12136671002398913 + x2)^2 + (
    -0.4592804310959082 + x3)^2) + x382 * ((-0.9376542898841029 + x1)^2 + (
    -0.7296259410537214 + x2)^2 + (-0.43830339602774704 + x3)^2) + x383 * ((
    -0.7366058903091773 + x1)^2 + (-0.4416494908995052 + x2)^2 + (
    -0.8513541067232596 + x3)^2) + x384 * ((-0.2583528714273713 + x1)^2 + (
    -0.8887871795539201 + x2)^2 + (-0.7248310640320087 + x3)^2) + x385 * ((
    -0.13907399568052925 + x1)^2 + (-0.5677374171942082 + x2)^2 + (
    -0.7157625382944803 + x3)^2) + x386 * ((-0.4868142512204441 + x1)^2 + (
    -0.8622063298179061 + x2)^2 + (-0.4912823321311274 + x3)^2) + x387 * ((
    -0.5544960376270748 + x1)^2 + (-0.8879916713525825 + x2)^2 + (
    -0.558510394418158 + x3)^2) + x388 * ((-0.5629250097194626 + x1)^2 + (
    -0.02440020191041392 + x2)^2 + (-0.3505563159384506 + x3)^2) + x389 * ((
    -0.5644814229596812 + x1)^2 + (-0.9167284919592144 + x2)^2 + (
    -0.39495515159248495 + x3)^2) + x390 * ((-0.15293694448570427 + x1)^2 + (
    -0.24201305054502364 + x2)^2 + (-0.09871933794597176 + x3)^2) + x391 * ((
    -0.04093761196800816 + x1)^2 + (-0.25111569049272453 + x2)^2 + (
    -0.8857385934563612 + x3)^2) + x392 * ((-0.6455628697859762 + x1)^2 + (
    -0.4324293933492942 + x2)^2 + (-0.3789568433740764 + x3)^2) + x393 * ((
    -0.4496937933648343 + x1)^2 + (-0.5667328853687145 + x2)^2 + (
    -0.40691835531776066 + x3)^2) + x394 * ((-0.5064964841495636 + x1)^2 + (
    -0.9231662667070567 + x2)^2 + (-0.9418870813951559 + x3)^2) + x395 * ((
    -0.7546510193031142 + x1)^2 + (-0.6290717885174039 + x2)^2 + (
    -0.9053863219371039 + x3)^2) + x396 * ((-0.1252499507413295 + x1)^2 + (
    -0.7291266598331314 + x2)^2 + (-0.06287245807908282 + x3)^2) + x397 * ((
    -0.975079670779934 + x1)^2 + (-0.8476261704965108 + x2)^2 + (
    -0.3613523225014157 + x3)^2) + x398 * ((-0.4786145006916671 + x1)^2 + (
    -0.7562794398860281 + x2)^2 + (-0.3246606771087578 + x3)^2) + x399 * ((
    -0.37211638738323183 + x1)^2 + (-0.5285143564556392 + x2)^2 + (
    -0.9473677259758877 + x3)^2) + x400 * ((-0.7747359569068005 + x1)^2 + (
    -0.5606816325734337 + x2)^2 + (-0.5023744358753353 + x3)^2) + x401 * ((
    -0.35934929189237974 + x1)^2 + (-0.2138842746533064 + x2)^2 + (
    -0.47940265124118275 + x3)^2) + x402 * ((-0.034039058901423114 + x1)^2 + (
    -0.8692672460914023 + x2)^2 + (-0.7367556473491849 + x3)^2) + x403 * ((
    -0.7282365643923602 + x1)^2 + (-0.6873407784728088 + x2)^2 + (
    -0.40274097414378485 + x3)^2) + x404 * ((-0.734857721471257 + x1)^2 + (
    -0.262970187892116 + x2)^2 + (-0.20961569008988468 + x3)^2) + x405 * ((
    -0.6525308383090344 + x1)^2 + (-0.19608022401263447 + x2)^2 + (
    -0.3870236183372049 + x3)^2) + x406 * ((-0.5645012980468977 + x1)^2 + (
    -0.6341191192370838 + x2)^2 + (-0.46196225878784536 + x3)^2) + x407 * ((
    -0.2930551852644451 + x1)^2 + (-0.9177900459954397 + x2)^2 + (
    -0.5732383676108328 + x3)^2) + x408 * ((-0.5092355531007602 + x1)^2 + (
    -0.18305497891779976 + x2)^2 + (-0.09370849097948963 + x3)^2) + x409 * ((
    -0.9512334177368659 + x1)^2 + (-0.07342868658441148 + x2)^2 + (
    -0.9395727539085917 + x3)^2) + x410 * ((-0.8094970632512009 + x1)^2 + (
    -0.7305977116464875 + x2)^2 + (-0.8070135155255885 + x3)^2) + x411 * ((
    -0.8962127199770125 + x1)^2 + (-0.24616592065326037 + x2)^2 + (
    -0.5849517947792571 + x3)^2) + x412 * ((-0.7052505213025646 + x1)^2 + (
    -0.0796535796359964 + x2)^2 + (-0.20277742799437048 + x3)^2) + x413 * ((
    -0.6267785193143974 + x1)^2 + (-0.10746876474982292 + x2)^2 + (
    -0.6494432790830167 + x3)^2) + x414 * ((-0.015520366623647752 + x1)^2 + (
    -0.5842081993611541 + x2)^2 + (-0.2744519446961057 + x3)^2) + x415 * ((
    -0.9793566236203548 + x1)^2 + (-0.22394521684566593 + x2)^2 + (
    -0.9058719953285858 + x3)^2) + x416 * ((-0.3542633017907568 + x1)^2 + (
    -0.44060726802651784 + x2)^2 + (-0.3997128293238619 + x3)^2) + x417 * ((
    -0.482866380882348 + x1)^2 + (-0.18588499288268157 + x2)^2 + (
    -0.07945614131161916 + x3)^2) + x418 * ((-0.10608910682131378 + x1)^2 + (
    -0.26438328524024857 + x2)^2 + (-0.2864127662313217 + x3)^2) + x419 * ((
    -0.39587823045804427 + x1)^2 + (-0.5695813324890586 + x2)^2 + (
    -0.1920662220868672 + x3)^2) + x420 * ((-0.06159942259296125 + x1)^2 + (
    -0.24020437828961405 + x2)^2 + (-0.3840367843355983 + x3)^2) + x421 * ((
    -0.7362258383939748 + x1)^2 + (-0.7652235683510016 + x2)^2 + (
    -0.5080623929895395 + x3)^2) + x422 * ((-0.6717905352420465 + x1)^2 + (
    -0.13175135938896554 + x2)^2 + (-0.8733829715017289 + x3)^2) + x423 * ((
    -0.5087936806553548 + x1)^2 + (-0.9895784354332001 + x2)^2 + (
    -0.5235243911248123 + x3)^2) + x424 * ((-0.5687248806674255 + x1)^2 + (
    -0.4800426470754785 + x2)^2 + (-0.66476015670848 + x3)^2) + x425 * ((
    -0.01879712601243244 + x1)^2 + (-0.9597300904119254 + x2)^2 + (
    -0.6400022174824137 + x3)^2) + x426 * ((-0.4546748066299232 + x1)^2 + (
    -0.08414046444682621 + x2)^2 + (-0.39949639976218343 + x3)^2) + x427 * ((
    -0.17854814031575228 + x1)^2 + (-0.24423555096632876 + x2)^2 + (
    -0.31176738263506176 + x3)^2) + x428 * ((-0.9738568400798214 + x1)^2 + (
    -0.9761211517297564 + x2)^2 + (-0.12716216361863075 + x3)^2) + x429 * ((
    -0.10905660727366906 + x1)^2 + (-0.9795748590019786 + x2)^2 + (
    -0.7440984394159507 + x3)^2) + x430 * ((-0.7666642751173116 + x1)^2 + (
    -0.3496890268415409 + x2)^2 + (-0.7178355854854029 + x3)^2) + x431 * ((
    -0.013742724746700241 + x1)^2 + (-0.43305298229497435 + x2)^2 + (
    -0.7254669199672814 + x3)^2) + x432 * ((-0.3275886542048829 + x1)^2 + (
    -0.8378680301704793 + x2)^2 + (-0.8349975326026666 + x3)^2) + x433 * ((
    -0.060805710429040816 + x1)^2 + (-0.656788371625089 + x2)^2 + (
    -0.2732796886924793 + x3)^2) + x434 * ((-0.9053177349583378 + x1)^2 + (
    -0.16127902677760553 + x2)^2 + (-0.32227488757718703 + x3)^2) + x435 * ((
    -0.9764291442509151 + x1)^2 + (-0.4200251729022414 + x2)^2 + (
    -0.19500625315790188 + x3)^2) + x436 * ((-0.17071396326782584 + x1)^2 + (
    -0.5019541154498613 + x2)^2 + (-0.6526843192881269 + x3)^2) + x437 * ((
    -0.9126755236735188 + x1)^2 + (-0.28940415967047584 + x2)^2 + (
    -0.1552734500527927 + x3)^2) + x438 * ((-0.5606535962065278 + x1)^2 + (
    -0.6342833304382927 + x2)^2 + (-0.8585431561155562 + x3)^2) + x439 * ((
    -0.11687570322670404 + x1)^2 + (-0.42299970942250387 + x2)^2 + (
    -0.4170059716014207 + x3)^2) + x440 * ((-0.5142371687254527 + x1)^2 + (
    -0.9857105100813118 + x2)^2 + (-0.5015291171995875 + x3)^2) + x441 * ((
    -0.32100216013315164 + x1)^2 + (-0.45572573844602215 + x2)^2 + (
    -0.48798435784356275 + x3)^2) + x442 * ((-0.597784767358479 + x1)^2 + (
    -0.05186929074401203 + x2)^2 + (-0.226366390881664 + x3)^2) + x443 * ((
    -0.8457016489109802 + x1)^2 + (-0.5554063005937154 + x2)^2 + (
    -0.41321444364538085 + x3)^2) + x444 * ((-0.9475471193586129 + x1)^2 + (
    -0.3121559515841179 + x2)^2 + (-0.14073436444324727 + x3)^2) + x445 * ((
    -0.7462797111675085 + x1)^2 + (-0.0832491058608037 + x2)^2 + (
    -0.16991972648761744 + x3)^2) + x446 * ((-0.6283905422614516 + x1)^2 + (
    -0.3473036441315591 + x2)^2 + (-0.6256420116557863 + x3)^2) + x447 * ((
    -0.47557752055186076 + x1)^2 + (-0.13087273477706074 + x2)^2 + (
    -0.566009659206059 + x3)^2) + x448 * ((-0.3811223652765986 + x1)^2 + (
    -0.3419162921570369 + x2)^2 + (-0.42670986021880697 + x3)^2) + x449 * ((
    -0.45276296485818746 + x1)^2 + (-0.7292869084688621 + x2)^2 + (
    -0.9219484257715016 + x3)^2) + x450 * ((-0.2944563711575213 + x1)^2 + (
    -0.9768141635311406 + x2)^2 + (-0.9139907883287979 + x3)^2) + x451 * ((
    -0.2045693815413957 + x1)^2 + (-0.6083069865306869 + x2)^2 + (
    -0.5354494090536733 + x3)^2) + x452 * ((-0.9092286101623649 + x1)^2 + (
    -0.19827382634748447 + x2)^2 + (-0.5692289216759975 + x3)^2) + x453 * ((
    -0.4428119569466705 + x1)^2 + (-0.3322800930778397 + x2)^2 + (
    -0.5707107027562174 + x3)^2) + x454 * ((-0.419027742190789 + x1)^2 + (
    -0.4618756991792069 + x2)^2 + (-0.07896233563766164 + x3)^2) + x455 * ((
    -0.6584988862725016 + x1)^2 + (-0.6148209199675768 + x2)^2 + (
    -0.24819109836653064 + x3)^2) + x456 * ((-0.7067453957053103 + x1)^2 + (
    -0.16400947550811773 + x2)^2 + (-0.2404675897181846 + x3)^2) + x457 * ((
    -0.6059340157584386 + x1)^2 + (-0.368724454571691 + x2)^2 + (
    -0.3166424342634133 + x3)^2) + x458 * ((-0.1505689967926862 + x1)^2 + (
    -0.625369145400853 + x2)^2 + (-0.8732323044478142 + x3)^2) + x459 * ((
    -0.4387938575304804 + x1)^2 + (-0.6686693605208012 + x2)^2 + (
    -0.5707959366759914 + x3)^2) + x460 * ((-0.7576333064836764 + x1)^2 + (
    -0.15002688954303656 + x2)^2 + (-0.15547993353000245 + x3)^2) + x461 * ((
    -0.666581715107795 + x1)^2 + (-0.8984605497623024 + x2)^2 + (
    -0.3096514261621284 + x3)^2) + x462 * ((-0.8387444625970372 + x1)^2 + (
    -0.16015110460364135 + x2)^2 + (-0.17793311971345638 + x3)^2) + x463 * ((
    -0.7961300734270524 + x1)^2 + (-0.06315804030987215 + x2)^2 + (
    -0.2886538911688289 + x3)^2) + x464 * ((-0.09882382311717897 + x1)^2 + (
    -0.9562490103711244 + x2)^2 + (-0.3979053832361369 + x3)^2) + x465 * ((
    -0.1313503761972874 + x1)^2 + (-0.1784477941922571 + x2)^2 + (
    -0.26652042199603243 + x3)^2) + x466 * ((-0.5560596702183167 + x1)^2 + (
    -0.776379609944948 + x2)^2 + (-0.4248340064314263 + x3)^2) + x467 * ((
    -0.061904031651977 + x1)^2 + (-0.6153844859790686 + x2)^2 + (
    -0.9267629321786096 + x3)^2) + x468 * ((-0.22406567435416147 + x1)^2 + (
    -0.16598467807059802 + x2)^2 + (-0.631039868789005 + x3)^2) + x469 * ((
    -0.2067711913915432 + x1)^2 + (-0.9546739138625829 + x2)^2 + (
    -0.6132888596828534 + x3)^2) + x470 * ((-0.698359896593753 + x1)^2 + (
    -0.09633791817043569 + x2)^2 + (-0.7767762514491409 + x3)^2) + x471 * ((
    -0.5495935658571374 + x1)^2 + (-0.08474290481778801 + x2)^2 + (
    -0.6612846791750243 + x3)^2) + x472 * ((-0.3161875292045071 + x1)^2 + (
    -0.6387922458536845 + x2)^2 + (-0.7653392459044 + x3)^2) + x473 * ((
    -0.7319358324745259 + x1)^2 + (-0.992182632521313 + x2)^2 + (
    -0.6863923077018874 + x3)^2) + x474 * ((-0.6019092920263115 + x1)^2 + (
    -0.7773860008024426 + x2)^2 + (-0.696651134077001 + x3)^2) + x475 * ((
    -0.8049096869634418 + x1)^2 + (-0.0732355551315873 + x2)^2 + (
    -0.5890554014646376 + x3)^2) + x476 * ((-0.2400029979216146 + x1)^2 + (
    -0.9945676004924368 + x2)^2 + (-0.5289410390414967 + x3)^2) + x477 * ((
    -0.2766431455253143 + x1)^2 + (-0.8539068538716186 + x2)^2 + (
    -0.20627516491122866 + x3)^2) + x478 * ((-0.35956937240024434 + x1)^2 + (
    -0.1564680965685581 + x2)^2 + (-0.13254723904140797 + x3)^2) + x479 * ((
    -0.6851905938616645 + x1)^2 + (-0.92350145756233 + x2)^2 + (
    -0.12850409116051253 + x3)^2) + x480 * ((-0.8530335314027025 + x1)^2 + (
    -0.014728381555152992 + x2)^2 + (-0.3823239089970707 + x3)^2) + x481 * ((
    -0.20793230117071493 + x1)^2 + (-0.16676956450110558 + x2)^2 + (
    -0.34228112340343475 + x3)^2) + x482 * ((-0.6234604214732817 + x1)^2 + (
    -0.2502728265106259 + x2)^2 + (-0.3410768048568552 + x3)^2) + x483 * ((
    -0.32574485718659996 + x1)^2 + (-0.49133487411842436 + x2)^2 + (
    -0.9269586652185272 + x3)^2) + x484 * ((-0.8074001332885633 + x1)^2 + (
    -0.436124135331206 + x2)^2 + (-0.6967988731368366 + x3)^2) + x485 * ((
    -0.0885078496198809 + x1)^2 + (-0.06383953819167731 + x2)^2 + (
    -0.12724142698377883 + x3)^2) + x486 * ((-0.2337562876270498 + x1)^2 + (
    -0.17694669799647322 + x2)^2 + (-0.24213277883073392 + x3)^2) + x487 * ((
    -0.4489386544210575 + x1)^2 + (-0.39350049538525844 + x2)^2 + (
    -0.2766646939987202 + x3)^2) + x488 * ((-0.6295217224500858 + x1)^2 + (
    -0.2004219022799547 + x2)^2 + (-0.34401008781100983 + x3)^2) + x489 * ((
    -0.7178536888350097 + x1)^2 + (-0.4777123128107543 + x2)^2 + (
    -0.020254499193558706 + x3)^2) + x490 * ((-0.11689305631558389 + x1)^2 + (
    -0.7921096764850253 + x2)^2 + (-0.0018493281679282658 + x3)^2) + x491 * ((
    -0.42252861541271625 + x1)^2 + (-0.7365281026729076 + x2)^2 + (
    -0.24208265132422635 + x3)^2) + x492 * ((-0.7215969240513533 + x1)^2 + (
    -0.3256843299668196 + x2)^2 + (-0.3698108298221342 + x3)^2) + x493 * ((
    -0.2595423236714335 + x1)^2 + (-0.2589559818665762 + x2)^2 + (
    -0.18615386799497224 + x3)^2) + x494 * ((-0.9984305905352117 + x1)^2 + (
    -0.7165229939904344 + x2)^2 + (-0.1285692611907402 + x3)^2) + x495 * ((
    -0.8872140808683944 + x1)^2 + (-0.5011145036032805 + x2)^2 + (
    -0.3883708507632184 + x3)^2) + x496 * ((-0.3924529848246979 + x1)^2 + (
    -0.22348565481301363 + x2)^2 + (-0.2061044173907518 + x3)^2) + x497 * ((
    -0.9112329633612304 + x1)^2 + (-0.3163218232655004 + x2)^2 + (
    -0.20302411889796268 + x3)^2) + x498 * ((-0.6097913445881256 + x1)^2 + (
    -0.4542976898151134 + x2)^2 + (-0.6195483822905107 + x3)^2) + x499 * ((
    -0.15522553621050394 + x1)^2 + (-0.01999404860523235 + x2)^2 + (
    -0.23442286593451234 + x3)^2) + x500 * ((-0.9199134838866957 + x1)^2 + (
    -0.7868442189111334 + x2)^2 + (-0.34080460170453486 + x3)^2) + x501 * ((
    -0.8166348595782067 + x1)^2 + (-0.7614497805023087 + x2)^2 + (
    -0.5452680081023854 + x3)^2) + x502 * ((-0.7603340178252571 + x1)^2 + (
    -0.08882941137693179 + x2)^2 + (-0.31747640494684937 + x3)^2) + x503 * ((
    -0.5390106156174557 + x1)^2 + (-0.4032399762516905 + x2)^2 + (
    -0.034174294693909646 + x3)^2) + x504 * ((-0.6762581280338263 + x1)^2 + (
    -0.1341686429284461 + x2)^2 + (-0.6300346342580874 + x3)^2) + x505 * ((
    -0.5985705326875344 + x1)^2 + (-0.6782117564373487 + x2)^2 + (
    -0.9723972807848017 + x3)^2) + x506 * ((-0.9582896782474865 + x1)^2 + (
    -0.647483553547818 + x2)^2 + (-0.2553574307779871 + x3)^2) + x507 * ((
    -0.1692498439422696 + x4)^2 + (-0.594909962110926 + x5)^2 + (
    -0.2649627397072344 + x6)^2) + x508 * ((-0.4299773164971996 + x4)^2 + (
    -0.8599590238209864 + x5)^2 + (-0.5477886873552766 + x6)^2) + x509 * ((
    -0.5826003170056784 + x4)^2 + (-0.941883448057164 + x5)^2 + (
    -0.30867313678242836 + x6)^2) + x510 * ((-0.6888712108376565 + x4)^2 + (
    -0.46694321374927916 + x5)^2 + (-0.20339940372771748 + x6)^2) + x511 * ((
    -0.4405711594738192 + x4)^2 + (-0.5080910724835329 + x5)^2 + (
    -0.18540147512570138 + x6)^2) + x512 * ((-0.36908840219684824 + x4)^2 + (
    -0.9606901577735717 + x5)^2 + (-0.1579661214699748 + x6)^2) + x513 * ((
    -0.39554390595886324 + x4)^2 + (-0.95517234425623 + x5)^2 + (
    -0.4357037242101963 + x6)^2) + x514 * ((-0.11324062660745182 + x4)^2 + (
    -0.1127227477493824 + x5)^2 + (-0.6775531466862447 + x6)^2) + x515 * ((
    -0.37207880369117297 + x4)^2 + (-0.4429785978155648 + x5)^2 + (
    -0.6160286803397987 + x6)^2) + x516 * ((-0.2361959619384585 + x4)^2 + (
    -0.6356037312017463 + x5)^2 + (-0.5117112742751293 + x6)^2) + x517 * ((
    -0.4447865236645254 + x4)^2 + (-0.33736132166151467 + x5)^2 + (
    -0.5880068862255667 + x6)^2) + x518 * ((-0.1880644612037895 + x4)^2 + (
    -0.8339460457426732 + x5)^2 + (-0.4642760100333919 + x6)^2) + x519 * ((
    -0.809678525848048 + x4)^2 + (-0.9810714270884835 + x5)^2 + (
    -0.22329339192222197 + x6)^2) + x520 * ((-0.9103106601121644 + x4)^2 + (
    -0.7530889196828001 + x5)^2 + (-0.2687229232888456 + x6)^2) + x521 * ((
    -0.2506681687047203 + x4)^2 + (-0.14874655132318948 + x5)^2 + (
    -0.7961773337916473 + x6)^2) + x522 * ((-0.5877634400149608 + x4)^2 + (
    -0.7175654971518651 + x5)^2 + (-0.6356627690183453 + x6)^2) + x523 * ((
    -0.7974452543446829 + x4)^2 + (-0.5323927624309212 + x5)^2 + (
    -0.9572021040304207 + x6)^2) + x524 * ((-0.5949737079161318 + x4)^2 + (
    -0.41675919028038244 + x5)^2 + (-0.25549007713931127 + x6)^2) + x525 * ((
    -0.05224072110626399 + x4)^2 + (-0.9684253307041065 + x5)^2 + (
    -0.03621367660020813 + x6)^2) + x526 * ((-0.9347003609994666 + x4)^2 + (
    -0.64358152389621 + x5)^2 + (-0.059814343789942215 + x6)^2) + x527 * ((
    -0.7935538449770041 + x4)^2 + (-0.11540895271984875 + x5)^2 + (
    -0.3946769068499303 + x6)^2) + x528 * ((-0.17385809015950826 + x4)^2 + (
    -0.45921932138562505 + x5)^2 + (-0.8256339099174179 + x6)^2) + x529 * ((
    -0.03835739793505788 + x4)^2 + (-0.6113872567578748 + x5)^2 + (
    -0.8718964927106821 + x6)^2) + x530 * ((-0.5739391076092649 + x4)^2 + (
    -0.5247196687429146 + x5)^2 + (-0.8533462318828052 + x6)^2) + x531 * ((
    -0.971075259349222 + x4)^2 + (-0.9104965674152667 + x5)^2 + (
    -0.7708929958995743 + x6)^2) + x532 * ((-0.5645353295297807 + x4)^2 + (
    -0.8584342772586054 + x5)^2 + (-0.8718267224700634 + x6)^2) + x533 * ((
    -0.6297483558228558 + x4)^2 + (-0.04014715139597247 + x5)^2 + (
    -0.09844847603361628 + x6)^2) + x534 * ((-0.5189119183247188 + x4)^2 + (
    -0.9474326272844581 + x5)^2 + (-0.5266109715772231 + x6)^2) + x535 * ((
    -0.6527900351730098 + x4)^2 + (-0.11052190591595967 + x5)^2 + (
    -0.5191880622085426 + x6)^2) + x536 * ((-0.10854173782735999 + x4)^2 + (
    -0.42093142780593973 + x5)^2 + (-0.31276103054202575 + x6)^2) + x537 * ((
    -0.3561489249032288 + x4)^2 + (-0.8268627589482757 + x5)^2 + (
    -0.1956453729075287 + x6)^2) + x538 * ((-0.4670221520529523 + x4)^2 + (
    -0.8891113977897892 + x5)^2 + (-0.27241504986579945 + x6)^2) + x539 * ((
    -0.35771749803339015 + x4)^2 + (-0.6044481060569854 + x5)^2 + (
    -0.7643630258273018 + x6)^2) + x540 * ((-0.04418354837503591 + x4)^2 + (
    -0.3102075900230633 + x5)^2 + (-0.8330809639446761 + x6)^2) + x541 * ((
    -0.8743744462324157 + x4)^2 + (-0.845910325959314 + x5)^2 + (
    -0.7140310051973626 + x6)^2) + x542 * ((-0.716502442685945 + x4)^2 + (
    -0.9515475221689099 + x5)^2 + (-0.6188065408222541 + x6)^2) + x543 * ((
    -0.06835345835265683 + x4)^2 + (-0.823370938809925 + x5)^2 + (
    -0.3389455123551257 + x6)^2) + x544 * ((-0.7757415343504088 + x4)^2 + (
    -0.7958264649791436 + x5)^2 + (-0.625436707143751 + x6)^2) + x545 * ((
    -0.9142760468526993 + x4)^2 + (-0.970911085347618 + x5)^2 + (
    -0.5429674014732869 + x6)^2) + x546 * ((-0.2096014409776199 + x4)^2 + (
    -0.9025289375492106 + x5)^2 + (-0.5287699855976883 + x6)^2) + x547 * ((
    -0.011619538885734193 + x4)^2 + (-0.12056474702179032 + x5)^2 + (
    -0.5981092250808783 + x6)^2) + x548 * ((-0.08114659947993563 + x4)^2 + (
    -0.441063194519585 + x5)^2 + (-0.9642109110625849 + x6)^2) + x549 * ((
    -0.3788010313673167 + x4)^2 + (-0.19367862019710247 + x5)^2 + (
    -0.7345907587139372 + x6)^2) + x550 * ((-0.02680831453838972 + x4)^2 + (
    -0.5010595635551833 + x5)^2 + (-0.5697272305278913 + x6)^2) + x551 * ((
    -0.9408661364624531 + x4)^2 + (-0.4084534281255007 + x5)^2 + (
    -0.5124759778704364 + x6)^2) + x552 * ((-0.7655175499270966 + x4)^2 + (
    -0.9482620910201023 + x5)^2 + (-0.27827134564381706 + x6)^2) + x553 * ((
    -0.8265432701686128 + x4)^2 + (-0.14848837551074712 + x5)^2 + (
    -0.20089309175503667 + x6)^2) + x554 * ((-0.8000481609994606 + x4)^2 + (
    -0.2539853139751347 + x5)^2 + (-0.20829630707197233 + x6)^2) + x555 * ((
    -0.26855105737847407 + x4)^2 + (-0.44920136283845336 + x5)^2 + (
    -0.41629666515596175 + x6)^2) + x556 * ((-0.7182882087805578 + x4)^2 + (
    -0.3793592905729698 + x5)^2 + (-0.17883837272616077 + x6)^2) + x557 * ((
    -0.19581024445686512 + x4)^2 + (-0.27181382773049567 + x5)^2 + (
    -0.322427225040845 + x6)^2) + x558 * ((-0.38658358127338854 + x4)^2 + (
    -0.7529124327703216 + x5)^2 + (-0.41910049255232174 + x6)^2) + x559 * ((
    -0.19143734810557733 + x4)^2 + (-0.48208401520816846 + x5)^2 + (
    -0.045061252030364485 + x6)^2) + x560 * ((-0.05682593455420182 + x4)^2 + (
    -0.7233915176300436 + x5)^2 + (-0.705103104979348 + x6)^2) + x561 * ((
    -0.9042027840926966 + x4)^2 + (-0.6938960112447266 + x5)^2 + (
    -0.3354994737557092 + x6)^2) + x562 * ((-0.7894861443951544 + x4)^2 + (
    -0.15244186536727333 + x5)^2 + (-0.5005398248336654 + x6)^2) + x563 * ((
    -0.34446185593752554 + x4)^2 + (-0.6772836129498278 + x5)^2 + (
    -0.7336734830314701 + x6)^2) + x564 * ((-0.20741666474163767 + x4)^2 + (
    -0.8202921977271875 + x5)^2 + (-0.5506009695439275 + x6)^2) + x565 * ((
    -0.5402923097092933 + x4)^2 + (-0.2675342734369003 + x5)^2 + (
    -0.7992890751698145 + x6)^2) + x566 * ((-0.27967022339776526 + x4)^2 + (
    -0.7979911425034355 + x5)^2 + (-0.46452645725265274 + x6)^2) + x567 * ((
    -0.9595819947527509 + x4)^2 + (-0.5232034354155645 + x5)^2 + (
    -0.2389966098134152 + x6)^2) + x568 * ((-0.07608991534038712 + x4)^2 + (
    -0.5736418691521828 + x5)^2 + (-0.019986186505803083 + x6)^2) + x569 * ((
    -0.42700398197897205 + x4)^2 + (-0.8010918625105746 + x5)^2 + (
    -0.8805692849635621 + x6)^2) + x570 * ((-0.5579869928092586 + x4)^2 + (
    -0.389498674450649 + x5)^2 + (-0.0748048271612155 + x6)^2) + x571 * ((
    -0.4070102263571985 + x4)^2 + (-0.7554593095435335 + x5)^2 + (
    -0.5904356558483927 + x6)^2) + x572 * ((-0.1364891447316846 + x4)^2 + (
    -0.8468918307965907 + x5)^2 + (-0.28700620952460276 + x6)^2) + x573 * ((
    -0.3367232340241588 + x4)^2 + (-0.8929968819838374 + x5)^2 + (
    -0.7484026014198896 + x6)^2) + x574 * ((-0.7635235105485991 + x4)^2 + (
    -0.5708091732053739 + x5)^2 + (-0.6753411475376285 + x6)^2) + x575 * ((
    -0.3651268993409923 + x4)^2 + (-0.12289882343337766 + x5)^2 + (
    -0.964009065158759 + x6)^2) + x576 * ((-0.8750166259121633 + x4)^2 + (
    -0.41383609996893045 + x5)^2 + (-0.29800741171032363 + x6)^2) + x577 * ((
    -0.40013800173743697 + x4)^2 + (-0.7249247652248746 + x5)^2 + (
    -0.6355874704603257 + x6)^2) + x578 * ((-0.18348856582977036 + x4)^2 + (
    -0.025854052500041358 + x5)^2 + (-0.2534534001576054 + x6)^2) + x579 * ((
    -0.9435154017754898 + x4)^2 + (-0.4392260710197824 + x5)^2 + (
    -0.4691516281413123 + x6)^2) + x580 * ((-0.7385168925807722 + x4)^2 + (
    -0.24644193646352752 + x5)^2 + (-0.17061742663080026 + x6)^2) + x581 * ((
    -0.05605633605668536 + x4)^2 + (-0.4912081682781063 + x5)^2 + (
    -0.5699993572568407 + x6)^2) + x582 * ((-0.15757181258844644 + x4)^2 + (
    -0.7303751725186297 + x5)^2 + (-0.9121598657835175 + x6)^2) + x583 * ((
    -0.33215497925633675 + x4)^2 + (-0.17028080871532403 + x5)^2 + (
    -0.3930063113045501 + x6)^2) + x584 * ((-0.7786941002157438 + x4)^2 + (
    -0.7405380151215268 + x5)^2 + (-0.9154339959764618 + x6)^2) + x585 * ((
    -0.7508193852295587 + x4)^2 + (-0.3803573428649786 + x5)^2 + (
    -0.22138614519182764 + x6)^2) + x586 * ((-0.9264682682309922 + x4)^2 + (
    -0.8873603073342023 + x5)^2 + (-0.864950588785591 + x6)^2) + x587 * ((
    -0.908267042284869 + x4)^2 + (-0.10298312771159246 + x5)^2 + (
    -0.6124646113776369 + x6)^2) + x588 * ((-0.16426882492973371 + x4)^2 + (
    -0.9869331956455133 + x5)^2 + (-0.719818452386762 + x6)^2) + x589 * ((
    -0.8825086613164931 + x4)^2 + (-0.08300173420348822 + x5)^2 + (
    -0.44087052443558905 + x6)^2) + x590 * ((-0.5130371082699586 + x4)^2 + (
    -0.7805872451248177 + x5)^2 + (-0.914693570552897 + x6)^2) + x591 * ((
    -0.12650358912449233 + x4)^2 + (-0.5342711885242658 + x5)^2 + (
    -0.3859086811884249 + x6)^2) + x592 * ((-0.021894498188813283 + x4)^2 + (
    -0.0027246625913778244 + x5)^2 + (-0.626856809181304 + x6)^2) + x593 * ((
    -0.8441678193498758 + x4)^2 + (-0.3509107664369997 + x5)^2 + (
    -0.23930665191922518 + x6)^2) + x594 * ((-0.9191544458905686 + x4)^2 + (
    -0.9295699343849126 + x5)^2 + (-0.5569494475068902 + x6)^2) + x595 * ((
    -0.35271055808467555 + x4)^2 + (-0.14001703168123492 + x5)^2 + (
    -0.4307833453831681 + x6)^2) + x596 * ((-0.015927077871251027 + x4)^2 + (
    -0.7944117141411271 + x5)^2 + (-0.0663323600363589 + x6)^2) + x597 * ((
    -0.06700957837304222 + x4)^2 + (-0.7245424124926254 + x5)^2 + (
    -0.04136030199658791 + x6)^2) + x598 * ((-0.6435908765286936 + x4)^2 + (
    -0.5608885129918921 + x5)^2 + (-0.29840288844009555 + x6)^2) + x599 * ((
    -0.0017744407035030774 + x4)^2 + (-0.5302888132806858 + x5)^2 + (
    -0.1070197893246232 + x6)^2) + x600 * ((-0.9960876588948411 + x4)^2 + (
    -0.5297980608672969 + x5)^2 + (-0.0967898406969584 + x6)^2) + x601 * ((
    -0.2966788147123718 + x4)^2 + (-0.4535896653892114 + x5)^2 + (
    -0.12490644679443152 + x6)^2) + x602 * ((-0.33141143322070366 + x4)^2 + (
    -0.28744907554291355 + x5)^2 + (-0.06994447154054817 + x6)^2) + x603 * ((
    -0.047933403792797424 + x4)^2 + (-0.8415471101830639 + x5)^2 + (
    -0.5955840833322725 + x6)^2) + x604 * ((-0.9171613034104257 + x4)^2 + (
    -0.6459943002822387 + x5)^2 + (-0.4152591826204478 + x6)^2) + x605 * ((
    -0.32790075407957764 + x4)^2 + (-0.4939517226351521 + x5)^2 + (
    -0.22989356871245614 + x6)^2) + x606 * ((-0.5844775505927844 + x4)^2 + (
    -0.7114551136263754 + x5)^2 + (-0.2605304125555207 + x6)^2) + x607 * ((
    -0.5855724678597634 + x4)^2 + (-0.5384124176079916 + x5)^2 + (
    -0.22873430477860057 + x6)^2) + x608 * ((-0.27448502514988804 + x4)^2 + (
    -0.8811058000942367 + x5)^2 + (-0.1084432011985692 + x6)^2) + x609 * ((
    -0.8087191675490594 + x4)^2 + (-0.36365530737786633 + x5)^2 + (
    -0.2551582076272405 + x6)^2) + x610 * ((-0.4692805537583873 + x4)^2 + (
    -0.1094763815311296 + x5)^2 + (-0.03308747009705737 + x6)^2) + x611 * ((
    -0.1414596675245341 + x4)^2 + (-0.05264608531324155 + x5)^2 + (
    -0.16232407961452555 + x6)^2) + x612 * ((-0.09502702610585512 + x4)^2 + (
    -0.6088439913367978 + x5)^2 + (-0.5808332695355897 + x6)^2) + x613 * ((
    -0.03790513829711473 + x4)^2 + (-0.5080181668023536 + x5)^2 + (
    -0.6682482244944306 + x6)^2) + x614 * ((-0.2398098003882162 + x4)^2 + (
    -0.40854299334338917 + x5)^2 + (-0.6265561387473995 + x6)^2) + x615 * ((
    -0.41352866202283534 + x4)^2 + (-0.13735597150040624 + x5)^2 + (
    -0.6575650750157317 + x6)^2) + x616 * ((-0.5918024287760949 + x4)^2 + (
    -0.9046254255858704 + x5)^2 + (-0.35259988628306405 + x6)^2) + x617 * ((
    -0.6163737698105297 + x4)^2 + (-0.7338484828210599 + x5)^2 + (
    -0.2552037957856732 + x6)^2) + x618 * ((-0.7481226352197995 + x4)^2 + (
    -0.6103864936538574 + x5)^2 + (-0.29319537619297076 + x6)^2) + x619 * ((
    -0.3817477016118834 + x4)^2 + (-0.28367233078996257 + x5)^2 + (
    -0.9065136963715262 + x6)^2) + x620 * ((-0.5387913922968426 + x4)^2 + (
    -0.9587122385639283 + x5)^2 + (-0.2849034277289415 + x6)^2) + x621 * ((
    -0.016896910716011626 + x4)^2 + (-0.542247494752311 + x5)^2 + (
    -0.35702504416839875 + x6)^2) + x622 * ((-0.0400792611431785 + x4)^2 + (
    -0.06003526247003277 + x5)^2 + (-0.8531074258574137 + x6)^2) + x623 * ((
    -0.6026500310542549 + x4)^2 + (-0.6934852370637312 + x5)^2 + (
    -0.3460238114357763 + x6)^2) + x624 * ((-0.55902762581076 + x4)^2 + (
    -0.9459788231528541 + x5)^2 + (-0.1290887862399902 + x6)^2) + x625 * ((
    -0.3837617695459321 + x4)^2 + (-0.3879093486846117 + x5)^2 + (
    -0.8849022163547949 + x6)^2) + x626 * ((-0.7720525818822013 + x4)^2 + (
    -0.1111500101946098 + x5)^2 + (-0.7661918097646079 + x6)^2) + x627 * ((
    -0.6344378078488477 + x4)^2 + (-0.38920253281074113 + x5)^2 + (
    -0.2569532307428819 + x6)^2) + x628 * ((-0.8429682238542169 + x4)^2 + (
    -0.28809038931293773 + x5)^2 + (-0.19175063574452433 + x6)^2) + x629 * ((
    -0.2672995256303895 + x4)^2 + (-0.03242383874322041 + x5)^2 + (
    -0.9842571124991794 + x6)^2) + x630 * ((-0.06540387850476659 + x4)^2 + (
    -0.24128518865484905 + x5)^2 + (-0.20517012144871016 + x6)^2) + x631 * ((
    -0.18621511189629547 + x4)^2 + (-0.30267745952007064 + x5)^2 + (
    -0.7114604662427862 + x6)^2) + x632 * ((-0.7893034114918972 + x4)^2 + (
    -0.0955677714501183 + x5)^2 + (-0.5821952996736662 + x6)^2) + x633 * ((
    -0.20739251640515832 + x4)^2 + (-0.8432910091332453 + x5)^2 + (
    -0.2586107102872377 + x6)^2) + x634 * ((-0.5530346239832239 + x4)^2 + (
    -0.37827958857876165 + x5)^2 + (-0.7781403692754599 + x6)^2) + x635 * ((
    -0.28092860002809394 + x4)^2 + (-0.8298897623230604 + x5)^2 + (
    -0.2719103553554957 + x6)^2) + x636 * ((-0.014925126786705656 + x4)^2 + (
    -0.12777278988662366 + x5)^2 + (-0.10588450075658606 + x6)^2) + x637 * ((
    -0.11668619210388753 + x4)^2 + (-0.3820666367049661 + x5)^2 + (
    -0.7791195974948653 + x6)^2) + x638 * ((-0.4344431981739817 + x4)^2 + (
    -0.1080485799315768 + x5)^2 + (-0.08340127233732786 + x6)^2) + x639 * ((
    -0.1793620960414819 + x4)^2 + (-0.3419484974871717 + x5)^2 + (
    -0.7820789010033935 + x6)^2) + x640 * ((-0.7165429642851615 + x4)^2 + (
    -0.9026914605710601 + x5)^2 + (-0.6935163617983727 + x6)^2) + x641 * ((
    -0.30965035870898905 + x4)^2 + (-0.6763312865753088 + x5)^2 + (
    -0.10472903251267174 + x6)^2) + x642 * ((-0.10216516132313902 + x4)^2 + (
    -0.5490230377748015 + x5)^2 + (-0.7352888807492108 + x6)^2) + x643 * ((
    -0.8651135909998409 + x4)^2 + (-0.29254598308074753 + x5)^2 + (
    -0.11864176567670415 + x6)^2) + x644 * ((-0.2101013503923751 + x4)^2 + (
    -0.8522411631472961 + x5)^2 + (-0.7212132885792959 + x6)^2) + x645 * ((
    -0.11131146834606975 + x4)^2 + (-0.09341511900076704 + x5)^2 + (
    -0.22436226860606978 + x6)^2) + x646 * ((-0.09589381898256144 + x4)^2 + (
    -0.62983098343096 + x5)^2 + (-0.236862989417864 + x6)^2) + x647 * ((
    -0.17134746819256785 + x4)^2 + (-0.0022191294485545132 + x5)^2 + (
    -0.5719632904418379 + x6)^2) + x648 * ((-0.1437717819667449 + x4)^2 + (
    -0.693066215236063 + x5)^2 + (-0.47910832437053097 + x6)^2) + x649 * ((
    -0.21326957505198796 + x4)^2 + (-0.5389938925764525 + x5)^2 + (
    -0.8985814053123515 + x6)^2) + x650 * ((-0.5267034399227511 + x4)^2 + (
    -0.16272083595464992 + x5)^2 + (-0.4424485927629499 + x6)^2) + x651 * ((
    -0.010171844468493396 + x4)^2 + (-0.8225385611520942 + x5)^2 + (
    -0.850081594460415 + x6)^2) + x652 * ((-0.9099126006489431 + x4)^2 + (
    -0.7117592498159224 + x5)^2 + (-0.24535211640166132 + x6)^2) + x653 * ((
    -0.8933095434728399 + x4)^2 + (-0.18696555428084993 + x5)^2 + (
    -0.14126880443170386 + x6)^2) + x654 * ((-0.05060465423810745 + x4)^2 + (
    -0.35889935243868054 + x5)^2 + (-0.9898462690273427 + x6)^2) + x655 * ((
    -0.28435588276815815 + x4)^2 + (-0.144413444054048 + x5)^2 + (
    -0.4912506689862507 + x6)^2) + x656 * ((-0.02377989350983456 + x4)^2 + (
    -0.4850739766720621 + x5)^2 + (-0.014220358160159874 + x6)^2) + x657 * ((
    -0.10685228340662356 + x4)^2 + (-0.4306857431033353 + x5)^2 + (
    -0.899717945016438 + x6)^2) + x658 * ((-0.7958123415938076 + x4)^2 + (
    -0.1567416212397551 + x5)^2 + (-0.4381463784299796 + x6)^2) + x659 * ((
    -0.20239323873555803 + x4)^2 + (-0.6688370928332699 + x5)^2 + (
    -0.8908782840570669 + x6)^2) + x660 * ((-0.8162377020493878 + x4)^2 + (
    -0.5538462537896983 + x5)^2 + (-0.46332413492756175 + x6)^2) + x661 * ((
    -0.3285436588025977 + x4)^2 + (-0.18234363029763911 + x5)^2 + (
    -0.9652199890334622 + x6)^2) + x662 * ((-0.1833756016631104 + x4)^2 + (
    -0.6191845385278278 + x5)^2 + (-0.3823840339936617 + x6)^2) + x663 * ((
    -0.9451306347207963 + x4)^2 + (-0.05696563611612815 + x5)^2 + (
    -0.31872989911510674 + x6)^2) + x664 * ((-0.1876172330243875 + x4)^2 + (
    -0.21273318417844989 + x5)^2 + (-0.7951342088420695 + x6)^2) + x665 * ((
    -0.6813385906412783 + x4)^2 + (-0.7795130804133624 + x5)^2 + (
    -0.8121251523108964 + x6)^2) + x666 * ((-0.5476385802163356 + x4)^2 + (
    -0.47082012503804105 + x5)^2 + (-0.1875779928301533 + x6)^2) + x667 * ((
    -0.4418603491118567 + x4)^2 + (-0.47814259051556174 + x5)^2 + (
    -0.843868091243698 + x6)^2) + x668 * ((-0.7227490532707296 + x4)^2 + (
    -0.6305946284321624 + x5)^2 + (-0.7778431141977471 + x6)^2) + x669 * ((
    -0.44449821578332316 + x4)^2 + (-0.7010434784223998 + x5)^2 + (
    -0.4562440307525807 + x6)^2) + x670 * ((-0.8207794357127131 + x4)^2 + (
    -0.2715928586111269 + x5)^2 + (-0.8111077485955768 + x6)^2) + x671 * ((
    -0.06913168314217966 + x4)^2 + (-0.17062534115061545 + x5)^2 + (
    -0.7186204035119522 + x6)^2) + x672 * ((-0.9356572299847938 + x4)^2 + (
    -0.25247506111569284 + x5)^2 + (-0.3766500744907605 + x6)^2) + x673 * ((
    -0.053183850751484685 + x4)^2 + (-0.503319761819413 + x5)^2 + (
    -0.3988792529665396 + x6)^2) + x674 * ((-0.6348345247106641 + x4)^2 + (
    -0.7372264972225206 + x5)^2 + (-0.2816805911685105 + x6)^2) + x675 * ((
    -0.4922332187206825 + x4)^2 + (-0.12955383972526402 + x5)^2 + (
    -0.6759110290426272 + x6)^2) + x676 * ((-0.3039899015675839 + x4)^2 + (
    -0.8701136133070226 + x5)^2 + (-0.3415605267108113 + x6)^2) + x677 * ((
    -0.19249833111625447 + x4)^2 + (-0.289199436536963 + x5)^2 + (
    -0.17001661008163982 + x6)^2) + x678 * ((-0.41498929870378265 + x4)^2 + (
    -0.6714872892529845 + x5)^2 + (-0.7734373760087199 + x6)^2) + x679 * ((
    -0.6414826763544017 + x4)^2 + (-0.833907205124963 + x5)^2 + (
    -0.5454186218286011 + x6)^2) + x680 * ((-0.8018985643443416 + x4)^2 + (
    -0.18267498327347076 + x5)^2 + (-0.6248398639397298 + x6)^2) + x681 * ((
    -0.011710686297021211 + x4)^2 + (-0.7293978925979899 + x5)^2 + (
    -0.062110132255305706 + x6)^2) + x682 * ((-0.3522173993348232 + x4)^2 + (
    -0.07284835414901125 + x5)^2 + (-0.6849529919886285 + x6)^2) + x683 * ((
    -0.12185440522884461 + x4)^2 + (-0.6687199057889921 + x5)^2 + (
    -0.13946873559425443 + x6)^2) + x684 * ((-0.8925626716041768 + x4)^2 + (
    -0.5507535962948702 + x5)^2 + (-0.7754292445803886 + x6)^2) + x685 * ((
    -0.6737722608457104 + x4)^2 + (-0.6835956974473757 + x5)^2 + (
    -0.11220963763590197 + x6)^2) + x686 * ((-0.2056780683513766 + x4)^2 + (
    -0.7777969577351744 + x5)^2 + (-0.7818523629215165 + x6)^2) + x687 * ((
    -0.35040653667397936 + x4)^2 + (-0.7218237888483313 + x5)^2 + (
    -0.24223482432840604 + x6)^2) + x688 * ((-0.045519582549019444 + x4)^2 + (
    -0.2468399938697886 + x5)^2 + (-0.5509847497355672 + x6)^2) + x689 * ((
    -0.7625095428789862 + x4)^2 + (-0.38693097091538686 + x5)^2 + (
    -0.8447744154325253 + x6)^2) + x690 * ((-0.47706955962867537 + x4)^2 + (
    -0.9048825326627299 + x5)^2 + (-0.6698420394228831 + x6)^2) + x691 * ((
    -0.9220722254195256 + x4)^2 + (-0.9093919260950618 + x5)^2 + (
    -0.3585536965409931 + x6)^2) + x692 * ((-0.42421741345016817 + x4)^2 + (
    -0.1810097690077137 + x5)^2 + (-0.11838106532964576 + x6)^2) + x693 * ((
    -0.7909025678257156 + x4)^2 + (-0.6683526078945575 + x5)^2 + (
    -0.5109886309751906 + x6)^2) + x694 * ((-0.28703506025246406 + x4)^2 + (
    -0.6439491320749008 + x5)^2 + (-0.7706022456077256 + x6)^2) + x695 * ((
    -0.13459246208619924 + x4)^2 + (-0.28097209258600253 + x5)^2 + (
    -0.10489080047801336 + x6)^2) + x696 * ((-0.3523855983171982 + x4)^2 + (
    -0.4248157381430815 + x5)^2 + (-0.6906133929926649 + x6)^2) + x697 * ((
    -0.1583698558934198 + x4)^2 + (-0.9210909019600683 + x5)^2 + (
    -0.6395026018640236 + x6)^2) + x698 * ((-0.7869061505221948 + x4)^2 + (
    -0.7078900011730935 + x5)^2 + (-0.6196010572637488 + x6)^2) + x699 * ((
    -0.5687640083646678 + x4)^2 + (-0.5772192111740503 + x5)^2 + (
    -0.6138822482643156 + x6)^2) + x700 * ((-0.7139842499777261 + x4)^2 + (
    -0.11680023910927528 + x5)^2 + (-0.2506224434653087 + x6)^2) + x701 * ((
    -0.805568392008547 + x4)^2 + (-0.06545005124609204 + x5)^2 + (
    -0.032700612578027144 + x6)^2) + x702 * ((-0.8672418514729174 + x4)^2 + (
    -0.9495334316535684 + x5)^2 + (-0.9506671434655545 + x6)^2) + x703 * ((
    -0.8428186951044521 + x4)^2 + (-0.2491784563178132 + x5)^2 + (
    -0.8574700961978342 + x6)^2) + x704 * ((-0.3871201049109313 + x4)^2 + (
    -0.9738876810785931 + x5)^2 + (-0.613114261845513 + x6)^2) + x705 * ((
    -0.9150831066517291 + x4)^2 + (-0.8126407462368724 + x5)^2 + (
    -0.32527791429850705 + x6)^2) + x706 * ((-0.13884237948432931 + x4)^2 + (
    -0.05350519336412973 + x5)^2 + (-0.24780684370452688 + x6)^2) + x707 * ((
    -0.7923572326382577 + x4)^2 + (-0.16987369545737896 + x5)^2 + (
    -0.9459861441672113 + x6)^2) + x708 * ((-0.8287350086957515 + x4)^2 + (
    -0.2701283953407778 + x5)^2 + (-0.38893185458031276 + x6)^2) + x709 * ((
    -0.8419989467911838 + x4)^2 + (-0.36305399780969094 + x5)^2 + (
    -0.5097745885449746 + x6)^2) + x710 * ((-0.9328252563464429 + x4)^2 + (
    -0.6938288661186377 + x5)^2 + (-0.5178576561761775 + x6)^2) + x711 * ((
    -0.13394390692618663 + x4)^2 + (-0.1707402476262171 + x5)^2 + (
    -0.049978421880908175 + x6)^2) + x712 * ((-0.9344145063124553 + x4)^2 + (
    -0.5642986722348461 + x5)^2 + (-0.9742283497162917 + x6)^2) + x713 * ((
    -0.12917904997198593 + x4)^2 + (-0.8291714054039813 + x5)^2 + (
    -0.1461208778099089 + x6)^2) + x714 * ((-0.49297041535442676 + x4)^2 + (
    -0.9997056001066135 + x5)^2 + (-0.9984805276449421 + x6)^2) + x715 * ((
    -0.9443406401848632 + x4)^2 + (-0.9556643724533576 + x5)^2 + (
    -0.7626439658137829 + x6)^2) + x716 * ((-0.4927277418379675 + x4)^2 + (
    -0.24978712865953823 + x5)^2 + (-0.33279356513981784 + x6)^2) + x717 * ((
    -0.6628894265876931 + x4)^2 + (-0.08815384447750985 + x5)^2 + (
    -0.02837052028209286 + x6)^2) + x718 * ((-0.5951215974793173 + x4)^2 + (
    -0.6709917301275213 + x5)^2 + (-0.5228016909019687 + x6)^2) + x719 * ((
    -0.3628434072386518 + x4)^2 + (-0.5648955285747782 + x5)^2 + (
    -0.14037475292742752 + x6)^2) + x720 * ((-0.6315358621764737 + x4)^2 + (
    -0.4940040944835772 + x5)^2 + (-0.39393981108383724 + x6)^2) + x721 * ((
    -0.23895764723651125 + x4)^2 + (-0.4925466699958012 + x5)^2 + (
    -0.6798787131541073 + x6)^2) + x722 * ((-0.33431465619738565 + x4)^2 + (
    -0.02990879062461249 + x5)^2 + (-0.98627846080786 + x6)^2) + x723 * ((
    -0.20138845604638655 + x4)^2 + (-0.07286113290687579 + x5)^2 + (
    -0.7389461293858135 + x6)^2) + x724 * ((-0.22043310505100588 + x4)^2 + (
    -0.6921624888940164 + x5)^2 + (-0.7390910692714129 + x6)^2) + x725 * ((
    -0.1794768509914445 + x4)^2 + (-0.19971018619617786 + x5)^2 + (
    -0.1252179745377201 + x6)^2) + x726 * ((-0.4316525971751499 + x4)^2 + (
    -0.9293948927573288 + x5)^2 + (-0.6357217625876419 + x6)^2) + x727 * ((
    -0.19054858574619327 + x4)^2 + (-0.6597186703227657 + x5)^2 + (
    -0.7437070343450088 + x6)^2) + x728 * ((-0.5401665990210613 + x4)^2 + (
    -0.31975882224981744 + x5)^2 + (-0.7676783575559698 + x6)^2) + x729 * ((
    -0.7141585569819535 + x4)^2 + (-0.5821205832955013 + x5)^2 + (
    -0.9414136448749184 + x6)^2) + x730 * ((-0.44737341471901404 + x4)^2 + (
    -0.9048222764719899 + x5)^2 + (-0.7461921038282987 + x6)^2) + x731 * ((
    -0.6074944823231694 + x4)^2 + (-0.4144292990749079 + x5)^2 + (
    -0.9448146796490002 + x6)^2) + x732 * ((-0.7711535942806756 + x4)^2 + (
    -0.18386931660223416 + x5)^2 + (-0.9382198399195494 + x6)^2) + x733 * ((
    -0.6654811389399782 + x4)^2 + (-0.7664480958655735 + x5)^2 + (
    -0.8043855734520027 + x6)^2) + x734 * ((-0.13574356640083862 + x4)^2 + (
    -0.8006073394818852 + x5)^2 + (-0.4293460234558568 + x6)^2) + x735 * ((
    -0.88109422081292 + x4)^2 + (-0.2521523305664952 + x5)^2 + (
    -0.2783612988957984 + x6)^2) + x736 * ((-0.21098683574670196 + x4)^2 + (
    -0.5793487573072326 + x5)^2 + (-0.1400427387047346 + x6)^2) + x737 * ((
    -0.5287988551538474 + x4)^2 + (-0.9641191628237653 + x5)^2 + (
    -0.9601811389639257 + x6)^2) + x738 * ((-0.6356835687091966 + x4)^2 + (
    -0.5035384241376479 + x5)^2 + (-0.912561201496254 + x6)^2) + x739 * ((
    -0.07022860689714527 + x4)^2 + (-0.7272172999901972 + x5)^2 + (
    -0.813209953545937 + x6)^2) + x740 * ((-0.8817216558635385 + x4)^2 + (
    -0.1961060970257913 + x5)^2 + (-0.4807253834719928 + x6)^2) + x741 * ((
    -0.8346893143895587 + x4)^2 + (-0.45391356191841836 + x5)^2 + (
    -0.03689848229389647 + x6)^2) + x742 * ((-0.4425064296341201 + x4)^2 + (
    -0.23133455702646433 + x5)^2 + (-0.4119733748205944 + x6)^2) + x743 * ((
    -0.48695930579230606 + x4)^2 + (-0.7723781894795173 + x5)^2 + (
    -0.7896048032875119 + x6)^2) + x744 * ((-0.6213072525945529 + x4)^2 + (
    -0.7463861427401226 + x5)^2 + (-0.19336124087532391 + x6)^2) + x745 * ((
    -0.9407434249412069 + x4)^2 + (-0.3157287888226875 + x5)^2 + (
    -0.19110493027237785 + x6)^2) + x746 * ((-0.5838103888478602 + x4)^2 + (
    -0.21478748867734254 + x5)^2 + (-0.8827349895451565 + x6)^2) + x747 * ((
    -0.03393239301609985 + x4)^2 + (-0.34669040395859996 + x5)^2 + (
    -0.6798250093428466 + x6)^2) + x748 * ((-0.9597035244408724 + x4)^2 + (
    -0.32286881217800434 + x5)^2 + (-0.4444196733141058 + x6)^2) + x749 * ((
    -0.9457000140765058 + x4)^2 + (-0.5068775796046029 + x5)^2 + (
    -0.3144273334897483 + x6)^2) + x750 * ((-0.044943238020383025 + x4)^2 + (
    -0.6614992336502294 + x5)^2 + (-0.8388656671250995 + x6)^2) + x751 * ((
    -0.49927342074497827 + x4)^2 + (-0.13468517272379243 + x5)^2 + (
    -0.4296515446930951 + x6)^2) + x752 * ((-0.9841852779169674 + x4)^2 + (
    -0.9843149988050245 + x5)^2 + (-0.47713010572283376 + x6)^2) + x753 * ((
    -0.4009300133770608 + x4)^2 + (-0.0042534179821622775 + x5)^2 + (
    -0.4175816329130312 + x6)^2) + x754 * ((-0.4885283879651544 + x4)^2 + (
    -0.9079239735865996 + x5)^2 + (-0.21031335265116158 + x6)^2) + x755 * ((
    -0.9849314196407067 + x4)^2 + (-0.11685357326709411 + x5)^2 + (
    -0.017369390966105014 + x6)^2) + x756 * ((-0.35446426043635526 + x4)^2 + (
    -0.2596023514638419 + x5)^2 + (-0.32096060367647117 + x6)^2) + x757 * ((
    -0.4352313328405867 + x4)^2 + (-0.6746955457244538 + x5)^2 + (
    -0.25563185786498377 + x6)^2) + x758 * ((-0.699315061557881 + x4)^2 + (
    -0.5915408096298286 + x5)^2 + (-0.44607763336915063 + x6)^2) + x759 * ((
    -0.6592318565406342 + x4)^2 + (-0.6133226566520651 + x5)^2 + (
    -0.5961918051667695 + x6)^2) + x760 * ((-0.2354774655941887 + x4)^2 + (
    -0.26243234628674394 + x5)^2 + (-0.312388269065189 + x6)^2) + x761 * ((
    -0.2200373888643452 + x4)^2 + (-0.41332951956449515 + x5)^2 + (
    -0.9109131978387711 + x6)^2) + x762 * ((-0.9487139910966843 + x4)^2 + (
    -0.5437246273285123 + x5)^2 + (-0.07874373064662499 + x6)^2) + x763 * ((
    -0.5964830453719224 + x4)^2 + (-0.0619742726091832 + x5)^2 + (
    -0.19927236817826444 + x6)^2) + x764 * ((-0.02759692117192214 + x4)^2 + (
    -0.2966943519059587 + x5)^2 + (-0.1436425270697561 + x6)^2) + x765 * ((
    -0.5605238341170351 + x4)^2 + (-0.16705196889000828 + x5)^2 + (
    -0.4596742351263795 + x6)^2) + x766 * ((-0.9861110555193163 + x4)^2 + (
    -0.8752990513886425 + x5)^2 + (-0.485142331599836 + x6)^2) + x767 * ((
    -0.27161250758957267 + x4)^2 + (-0.9946863069500006 + x5)^2 + (
    -0.439561525186691 + x6)^2) + x768 * ((-0.4836297090054381 + x4)^2 + (
    -0.2114798303676434 + x5)^2 + (-0.1278618145726882 + x6)^2) + x769 * ((
    -0.024736008778174612 + x4)^2 + (-0.9205199923700449 + x5)^2 + (
    -0.8484339940268846 + x6)^2) + x770 * ((-0.5626615620602874 + x4)^2 + (
    -0.034989370194508096 + x5)^2 + (-0.6632186742091526 + x6)^2) + x771 * ((
    -0.6438064560050359 + x4)^2 + (-0.4889465681575601 + x5)^2 + (
    -0.26934659936523253 + x6)^2) + x772 * ((-0.5261992201164788 + x4)^2 + (
    -0.08595932986749422 + x5)^2 + (-0.08488216145362637 + x6)^2) + x773 * ((
    -0.1409322982901524 + x4)^2 + (-0.11290088677205301 + x5)^2 + (
    -0.1848610267768337 + x6)^2) + x774 * ((-0.9062469407729168 + x4)^2 + (
    -0.443642723519166 + x5)^2 + (-0.16301234345822146 + x6)^2) + x775 * ((
    -0.26280187243977027 + x4)^2 + (-0.5791906957767239 + x5)^2 + (
    -0.09189211557137555 + x6)^2) + x776 * ((-0.7819362020918313 + x4)^2 + (
    -0.8107913530336736 + x5)^2 + (-0.08589261011414395 + x6)^2) + x777 * ((
    -0.12202077612002771 + x4)^2 + (-0.09381851826448306 + x5)^2 + (
    -0.9946687189369333 + x6)^2) + x778 * ((-0.7449921585503891 + x4)^2 + (
    -0.44616399084793734 + x5)^2 + (-0.14733396356242667 + x6)^2) + x779 * ((
    -0.8013267039644335 + x4)^2 + (-0.12726406694941528 + x5)^2 + (
    -0.30755184402270597 + x6)^2) + x780 * ((-0.7129868679977376 + x4)^2 + (
    -0.5624403504682522 + x5)^2 + (-0.5194087287496278 + x6)^2) + x781 * ((
    -0.702605402074762 + x4)^2 + (-0.696542187378441 + x5)^2 + (
    -0.9050186102050559 + x6)^2) + x782 * ((-0.48579654846686027 + x4)^2 + (
    -0.9865716657785814 + x5)^2 + (-0.7488638018945105 + x6)^2) + x783 * ((
    -0.14273183621265262 + x4)^2 + (-0.16961426380712896 + x5)^2 + (
    -0.7336118920897162 + x6)^2) + x784 * ((-0.508565000330308 + x4)^2 + (
    -0.0008598073433415676 + x5)^2 + (-0.4878861682744219 + x6)^2) + x785 * ((
    -0.37778026211733495 + x4)^2 + (-0.7302042173061916 + x5)^2 + (
    -0.658072993274222 + x6)^2) + x786 * ((-0.5859039531200585 + x4)^2 + (
    -0.28185196746339947 + x5)^2 + (-0.07351170392618223 + x6)^2) + x787 * ((
    -0.437816105636769 + x4)^2 + (-0.9381650700676218 + x5)^2 + (
    -0.7532133630650687 + x6)^2) + x788 * ((-0.9111142352615409 + x4)^2 + (
    -0.9188611987954707 + x5)^2 + (-0.7097765364993713 + x6)^2) + x789 * ((
    -0.6070364816449836 + x4)^2 + (-0.6368688399261839 + x5)^2 + (
    -0.8097201734033257 + x6)^2) + x790 * ((-0.6984482644711556 + x4)^2 + (
    -0.8822045583167333 + x5)^2 + (-0.5762293092462573 + x6)^2) + x791 * ((
    -0.05085683485354919 + x4)^2 + (-0.9999183826637328 + x5)^2 + (
    -0.4287782578354542 + x6)^2) + x792 * ((-0.7615905094162454 + x4)^2 + (
    -0.1421067735442294 + x5)^2 + (-0.5006086214169991 + x6)^2) + x793 * ((
    -0.9305602823426583 + x4)^2 + (-0.9752940115114439 + x5)^2 + (
    -0.1631253855890934 + x6)^2) + x794 * ((-0.26027159077598117 + x4)^2 + (
    -0.8467561936966935 + x5)^2 + (-0.42577439882602497 + x6)^2) + x795 * ((
    -0.08104856848069275 + x4)^2 + (-0.9886967089077169 + x5)^2 + (
    -0.08146796574801807 + x6)^2) + x796 * ((-0.48005659566609715 + x4)^2 + (
    -0.9974410345330987 + x5)^2 + (-0.48571859403846973 + x6)^2) + x797 * ((
    -0.4706070697040865 + x4)^2 + (-0.22633844473105058 + x5)^2 + (
    -0.8430722417451099 + x6)^2) + x798 * ((-0.6581283586576836 + x4)^2 + (
    -0.2988361857206986 + x5)^2 + (-0.5248717962910134 + x6)^2) + x799 * ((
    -0.4139397565643148 + x4)^2 + (-0.7947219857264776 + x5)^2 + (
    -0.9714023432927014 + x6)^2) + x800 * ((-0.29895041273047895 + x4)^2 + (
    -0.20934319073619012 + x5)^2 + (-0.12799433802173388 + x6)^2) + x801 * ((
    -0.7416051505394204 + x4)^2 + (-0.8610181415202831 + x5)^2 + (
    -0.8203512359906585 + x6)^2) + x802 * ((-0.8539442696762753 + x4)^2 + (
    -0.6440119856376406 + x5)^2 + (-0.04768006379778733 + x6)^2) + x803 * ((
    -0.8078856580669804 + x4)^2 + (-0.0811738770099133 + x5)^2 + (
    -0.42296333968011834 + x6)^2) + x804 * ((-0.11293172487506897 + x4)^2 + (
    -0.10190845514217972 + x5)^2 + (-0.025155476939746846 + x6)^2) + x805 * ((
    -0.6774554514175933 + x4)^2 + (-0.28953130741751354 + x5)^2 + (
    -0.7231890256224531 + x6)^2) + x806 * ((-0.9658389665612165 + x4)^2 + (
    -0.8012920581552374 + x5)^2 + (-0.6871461962217258 + x6)^2) + x807 * ((
    -0.5345563351474161 + x4)^2 + (-0.11378244706430707 + x5)^2 + (
    -0.7915828478976272 + x6)^2) + x808 * ((-0.9997767651100092 + x4)^2 + (
    -0.5574720960939473 + x5)^2 + (-0.7410926285969115 + x6)^2) + x809 * ((
    -0.29777709756222204 + x4)^2 + (-0.13420768997570653 + x5)^2 + (
    -0.41098786274229304 + x6)^2) + x810 * ((-0.4890881424574446 + x4)^2 + (
    -0.404669840371118 + x5)^2 + (-0.6839329573384761 + x6)^2) + x811 * ((
    -0.9275207698350674 + x4)^2 + (-0.6349688118385305 + x5)^2 + (
    -0.16211201636277606 + x6)^2) + x812 * ((-0.31185430455711194 + x4)^2 + (
    -0.9609480087595885 + x5)^2 + (-0.48506492880423546 + x6)^2) + x813 * ((
    -0.7594140721620825 + x4)^2 + (-0.9263148514595829 + x5)^2 + (
    -0.8648033086118 + x6)^2) + x814 * ((-0.6479304574703105 + x4)^2 + (
    -0.8228423329287321 + x5)^2 + (-0.7551761939784829 + x6)^2) + x815 * ((
    -0.8231579504797958 + x4)^2 + (-0.05635445777892223 + x5)^2 + (
    -0.02468508246924883 + x6)^2) + x816 * ((-0.5969304027180449 + x4)^2 + (
    -0.8273519061055513 + x5)^2 + (-0.8975627019214554 + x6)^2) + x817 * ((
    -0.47032986801594845 + x4)^2 + (-0.03758087479779437 + x5)^2 + (
    -0.956428581402661 + x6)^2) + x818 * ((-0.058484373437283965 + x4)^2 + (
    -0.7224332485058074 + x5)^2 + (-0.36656511074725406 + x6)^2) + x819 * ((
    -0.8067441195220981 + x4)^2 + (-0.6939130038104055 + x5)^2 + (
    -0.6650852436958627 + x6)^2) + x820 * ((-0.14316346421133996 + x4)^2 + (
    -0.8833335241651658 + x5)^2 + (-0.33873721710142757 + x6)^2) + x821 * ((
    -0.16663405286282917 + x4)^2 + (-0.1361097149511954 + x5)^2 + (
    -0.4167589692247934 + x6)^2) + x822 * ((-0.3533518801743728 + x4)^2 + (
    -0.7864769418639855 + x5)^2 + (-0.5700369360657614 + x6)^2) + x823 * ((
    -0.9940450532017178 + x4)^2 + (-0.8709964325378182 + x5)^2 + (
    -0.05370495768985595 + x6)^2) + x824 * ((-0.43669423470125 + x4)^2 + (
    -0.7826943195653798 + x5)^2 + (-0.08246841776453673 + x6)^2) + x825 * ((
    -0.31217298303878716 + x4)^2 + (-0.12873842883308007 + x5)^2 + (
    -0.4120375477605329 + x6)^2) + x826 * ((-0.04729057034546036 + x4)^2 + (
    -0.615848875622511 + x5)^2 + (-0.09028092669134402 + x6)^2) + x827 * ((
    -0.05579397155334043 + x4)^2 + (-0.45731350085562406 + x5)^2 + (
    -0.5113200354339912 + x6)^2) + x828 * ((-0.24317770299974573 + x4)^2 + (
    -0.31432958156550617 + x5)^2 + (-0.29916426285821995 + x6)^2) + x829 * ((
    -0.6647683703847979 + x4)^2 + (-0.5720315504033884 + x5)^2 + (
    -0.3330271930609998 + x6)^2) + x830 * ((-0.0671508784075493 + x4)^2 + (
    -0.7427046256777622 + x5)^2 + (-0.3842554432358185 + x6)^2) + x831 * ((
    -0.5142618830032626 + x4)^2 + (-0.37920880558154235 + x5)^2 + (
    -0.17375109475213701 + x6)^2) + x832 * ((-0.039030898150579474 + x4)^2 + (
    -0.416088697819994 + x5)^2 + (-0.23777905803288724 + x6)^2) + x833 * ((
    -0.4717971485183111 + x4)^2 + (-0.3383860380066811 + x5)^2 + (
    -0.460200523195855 + x6)^2) + x834 * ((-0.5900378880204267 + x4)^2 + (
    -0.7255901375319337 + x5)^2 + (-0.9154170002928985 + x6)^2) + x835 * ((
    -0.13093900398824065 + x4)^2 + (-0.4052139060110297 + x5)^2 + (
    -0.49962194728297327 + x6)^2) + x836 * ((-0.5001698078829642 + x4)^2 + (
    -0.7979303589649438 + x5)^2 + (-0.2739293646511145 + x6)^2) + x837 * ((
    -0.41855315898554013 + x4)^2 + (-0.998699983121554 + x5)^2 + (
    -0.2010058221141684 + x6)^2) + x838 * ((-0.7496871098706305 + x4)^2 + (
    -0.8235726845357767 + x5)^2 + (-0.37015198039038577 + x6)^2) + x839 * ((
    -0.28403104119909195 + x4)^2 + (-0.6420274479177237 + x5)^2 + (
    -0.4574273157370161 + x6)^2) + x840 * ((-0.46685731585307466 + x4)^2 + (
    -0.26906412522677103 + x5)^2 + (-0.6656657277253054 + x6)^2) + x841 * ((
    -0.2504282905612786 + x4)^2 + (-0.15851796206472113 + x5)^2 + (
    -0.4726147469986297 + x6)^2) + x842 * ((-0.21194510336903394 + x4)^2 + (
    -0.7789673451440703 + x5)^2 + (-0.09841245851637492 + x6)^2) + x843 * ((
    -0.2349671005207027 + x4)^2 + (-0.0221927931737832 + x5)^2 + (
    -0.5712554822182071 + x6)^2) + x844 * ((-0.0009451790835207641 + x4)^2 + (
    -0.2408337245798331 + x5)^2 + (-0.6211924391868702 + x6)^2) + x845 * ((
    -0.6707250517356161 + x4)^2 + (-0.5984637186180205 + x5)^2 + (
    -0.0668641338162419 + x6)^2) + x846 * ((-0.5511472131778885 + x4)^2 + (
    -0.07350867542191697 + x5)^2 + (-0.767739792767608 + x6)^2) + x847 * ((
    -0.9501581392192964 + x4)^2 + (-0.7233163389390355 + x5)^2 + (
    -0.5166844510344849 + x6)^2) + x848 * ((-0.9060156230362852 + x4)^2 + (
    -0.3113487821639962 + x5)^2 + (-0.20778084543419917 + x6)^2) + x849 * ((
    -0.5288680482784139 + x4)^2 + (-0.2934145990378463 + x5)^2 + (
    -0.4804974743654282 + x6)^2) + x850 * ((-0.09966115943905263 + x4)^2 + (
    -0.3938725699296275 + x5)^2 + (-0.32444318785821924 + x6)^2) + x851 * ((
    -0.6520321563540667 + x4)^2 + (-0.8056068500183343 + x5)^2 + (
    -0.0835838533559482 + x6)^2) + x852 * ((-0.8166208988287386 + x4)^2 + (
    -0.3518761684344235 + x5)^2 + (-0.7464113961140431 + x6)^2) + x853 * ((
    -0.1311593203796163 + x4)^2 + (-0.7160405481109373 + x5)^2 + (
    -0.09952132645843448 + x6)^2) + x854 * ((-0.04779808112037798 + x4)^2 + (
    -0.28884699291713234 + x5)^2 + (-0.10250649388727473 + x6)^2) + x855 * ((
    -0.9791729605203251 + x4)^2 + (-0.6726875461066422 + x5)^2 + (
    -0.9283118905188722 + x6)^2) + x856 * ((-0.13471412533270244 + x4)^2 + (
    -0.7071806165289065 + x5)^2 + (-0.9043216254262293 + x6)^2) + x857 * ((
    -0.5735353939945473 + x4)^2 + (-0.5273208712530736 + x5)^2 + (
    -0.6875628347914862 + x6)^2) + x858 * ((-0.9582137553329777 + x4)^2 + (
    -0.4500040273602035 + x5)^2 + (-0.26668127604253744 + x6)^2) + x859 * ((
    -0.35515505710029105 + x4)^2 + (-0.8998261443565795 + x5)^2 + (
    -0.5147227718297207 + x6)^2) + x860 * ((-0.9340214668622013 + x4)^2 + (
    -0.3503931266703305 + x5)^2 + (-0.22213442770583658 + x6)^2) + x861 * ((
    -0.30063857818433126 + x4)^2 + (-0.9781639681666726 + x5)^2 + (
    -0.5737192124395999 + x6)^2) + x862 * ((-0.9694287446674323 + x4)^2 + (
    -0.9139936410886877 + x5)^2 + (-0.16757766484105074 + x6)^2) + x863 * ((
    -0.040594150617694 + x4)^2 + (-0.43898895567045837 + x5)^2 + (
    -0.6978737824797022 + x6)^2) + x864 * ((-0.9047320599530371 + x4)^2 + (
    -0.4912564771269612 + x5)^2 + (-0.6733487941467664 + x6)^2) + x865 * ((
    -0.9549617147031715 + x4)^2 + (-0.6678649305928561 + x5)^2 + (
    -0.8834928821311292 + x6)^2) + x866 * ((-0.4395498573390294 + x4)^2 + (
    -0.30627811842262354 + x5)^2 + (-0.9750459496357505 + x6)^2) + x867 * ((
    -0.1870595942163641 + x4)^2 + (-0.151585797566554 + x5)^2 + (
    -0.6096114448910821 + x6)^2) + x868 * ((-0.8951229638762037 + x4)^2 + (
    -0.5978267742373706 + x5)^2 + (-0.5837237511628297 + x6)^2) + x869 * ((
    -0.9979607832682635 + x4)^2 + (-0.2544630128273442 + x5)^2 + (
    -0.7553436617442503 + x6)^2) + x870 * ((-0.18874920320016164 + x4)^2 + (
    -0.6216165758809351 + x5)^2 + (-0.8529149249653111 + x6)^2) + x871 * ((
    -0.6373429941144889 + x4)^2 + (-0.03524085604839855 + x5)^2 + (
    -0.2902922940078507 + x6)^2) + x872 * ((-0.1493240329654184 + x4)^2 + (
    -0.773610378940084 + x5)^2 + (-0.16800156102583386 + x6)^2) + x873 * ((
    -0.45959660687249615 + x4)^2 + (-0.8091285040534932 + x5)^2 + (
    -0.3286890399482034 + x6)^2) + x874 * ((-0.7478644912889102 + x4)^2 + (
    -0.014858297372218665 + x5)^2 + (-0.6866332635878059 + x6)^2) + x875 * ((
    -0.7646420573532026 + x4)^2 + (-0.9447630530244876 + x5)^2 + (
    -0.8190368275925283 + x6)^2) + x876 * ((-0.9924396130442916 + x4)^2 + (
    -0.6082265831465189 + x5)^2 + (-0.5057251733236754 + x6)^2) + x877 * ((
    -0.7721758593783997 + x4)^2 + (-0.8129769760490057 + x5)^2 + (
    -0.4066778113300017 + x6)^2) + x878 * ((-0.5586622471964208 + x4)^2 + (
    -0.7449498935310548 + x5)^2 + (-0.5133001652292216 + x6)^2) + x879 * ((
    -0.2606143437838706 + x4)^2 + (-0.9157831128583509 + x5)^2 + (
    -0.7725742539135185 + x6)^2) + x880 * ((-0.08665312749944609 + x4)^2 + (
    -0.20774241016302275 + x5)^2 + (-0.392846511749778 + x6)^2) + x881 * ((
    -0.02318360583183654 + x4)^2 + (-0.12136671002398913 + x5)^2 + (
    -0.4592804310959082 + x6)^2) + x882 * ((-0.9376542898841029 + x4)^2 + (
    -0.7296259410537214 + x5)^2 + (-0.43830339602774704 + x6)^2) + x883 * ((
    -0.7366058903091773 + x4)^2 + (-0.4416494908995052 + x5)^2 + (
    -0.8513541067232596 + x6)^2) + x884 * ((-0.2583528714273713 + x4)^2 + (
    -0.8887871795539201 + x5)^2 + (-0.7248310640320087 + x6)^2) + x885 * ((
    -0.13907399568052925 + x4)^2 + (-0.5677374171942082 + x5)^2 + (
    -0.7157625382944803 + x6)^2) + x886 * ((-0.4868142512204441 + x4)^2 + (
    -0.8622063298179061 + x5)^2 + (-0.4912823321311274 + x6)^2) + x887 * ((
    -0.5544960376270748 + x4)^2 + (-0.8879916713525825 + x5)^2 + (
    -0.558510394418158 + x6)^2) + x888 * ((-0.5629250097194626 + x4)^2 + (
    -0.02440020191041392 + x5)^2 + (-0.3505563159384506 + x6)^2) + x889 * ((
    -0.5644814229596812 + x4)^2 + (-0.9167284919592144 + x5)^2 + (
    -0.39495515159248495 + x6)^2) + x890 * ((-0.15293694448570427 + x4)^2 + (
    -0.24201305054502364 + x5)^2 + (-0.09871933794597176 + x6)^2) + x891 * ((
    -0.04093761196800816 + x4)^2 + (-0.25111569049272453 + x5)^2 + (
    -0.8857385934563612 + x6)^2) + x892 * ((-0.6455628697859762 + x4)^2 + (
    -0.4324293933492942 + x5)^2 + (-0.3789568433740764 + x6)^2) + x893 * ((
    -0.4496937933648343 + x4)^2 + (-0.5667328853687145 + x5)^2 + (
    -0.40691835531776066 + x6)^2) + x894 * ((-0.5064964841495636 + x4)^2 + (
    -0.9231662667070567 + x5)^2 + (-0.9418870813951559 + x6)^2) + x895 * ((
    -0.7546510193031142 + x4)^2 + (-0.6290717885174039 + x5)^2 + (
    -0.9053863219371039 + x6)^2) + x896 * ((-0.1252499507413295 + x4)^2 + (
    -0.7291266598331314 + x5)^2 + (-0.06287245807908282 + x6)^2) + x897 * ((
    -0.975079670779934 + x4)^2 + (-0.8476261704965108 + x5)^2 + (
    -0.3613523225014157 + x6)^2) + x898 * ((-0.4786145006916671 + x4)^2 + (
    -0.7562794398860281 + x5)^2 + (-0.3246606771087578 + x6)^2) + x899 * ((
    -0.37211638738323183 + x4)^2 + (-0.5285143564556392 + x5)^2 + (
    -0.9473677259758877 + x6)^2) + x900 * ((-0.7747359569068005 + x4)^2 + (
    -0.5606816325734337 + x5)^2 + (-0.5023744358753353 + x6)^2) + x901 * ((
    -0.35934929189237974 + x4)^2 + (-0.2138842746533064 + x5)^2 + (
    -0.47940265124118275 + x6)^2) + x902 * ((-0.034039058901423114 + x4)^2 + (
    -0.8692672460914023 + x5)^2 + (-0.7367556473491849 + x6)^2) + x903 * ((
    -0.7282365643923602 + x4)^2 + (-0.6873407784728088 + x5)^2 + (
    -0.40274097414378485 + x6)^2) + x904 * ((-0.734857721471257 + x4)^2 + (
    -0.262970187892116 + x5)^2 + (-0.20961569008988468 + x6)^2) + x905 * ((
    -0.6525308383090344 + x4)^2 + (-0.19608022401263447 + x5)^2 + (
    -0.3870236183372049 + x6)^2) + x906 * ((-0.5645012980468977 + x4)^2 + (
    -0.6341191192370838 + x5)^2 + (-0.46196225878784536 + x6)^2) + x907 * ((
    -0.2930551852644451 + x4)^2 + (-0.9177900459954397 + x5)^2 + (
    -0.5732383676108328 + x6)^2) + x908 * ((-0.5092355531007602 + x4)^2 + (
    -0.18305497891779976 + x5)^2 + (-0.09370849097948963 + x6)^2) + x909 * ((
    -0.9512334177368659 + x4)^2 + (-0.07342868658441148 + x5)^2 + (
    -0.9395727539085917 + x6)^2) + x910 * ((-0.8094970632512009 + x4)^2 + (
    -0.7305977116464875 + x5)^2 + (-0.8070135155255885 + x6)^2) + x911 * ((
    -0.8962127199770125 + x4)^2 + (-0.24616592065326037 + x5)^2 + (
    -0.5849517947792571 + x6)^2) + x912 * ((-0.7052505213025646 + x4)^2 + (
    -0.0796535796359964 + x5)^2 + (-0.20277742799437048 + x6)^2) + x913 * ((
    -0.6267785193143974 + x4)^2 + (-0.10746876474982292 + x5)^2 + (
    -0.6494432790830167 + x6)^2) + x914 * ((-0.015520366623647752 + x4)^2 + (
    -0.5842081993611541 + x5)^2 + (-0.2744519446961057 + x6)^2) + x915 * ((
    -0.9793566236203548 + x4)^2 + (-0.22394521684566593 + x5)^2 + (
    -0.9058719953285858 + x6)^2) + x916 * ((-0.3542633017907568 + x4)^2 + (
    -0.44060726802651784 + x5)^2 + (-0.3997128293238619 + x6)^2) + x917 * ((
    -0.482866380882348 + x4)^2 + (-0.18588499288268157 + x5)^2 + (
    -0.07945614131161916 + x6)^2) + x918 * ((-0.10608910682131378 + x4)^2 + (
    -0.26438328524024857 + x5)^2 + (-0.2864127662313217 + x6)^2) + x919 * ((
    -0.39587823045804427 + x4)^2 + (-0.5695813324890586 + x5)^2 + (
    -0.1920662220868672 + x6)^2) + x920 * ((-0.06159942259296125 + x4)^2 + (
    -0.24020437828961405 + x5)^2 + (-0.3840367843355983 + x6)^2) + x921 * ((
    -0.7362258383939748 + x4)^2 + (-0.7652235683510016 + x5)^2 + (
    -0.5080623929895395 + x6)^2) + x922 * ((-0.6717905352420465 + x4)^2 + (
    -0.13175135938896554 + x5)^2 + (-0.8733829715017289 + x6)^2) + x923 * ((
    -0.5087936806553548 + x4)^2 + (-0.9895784354332001 + x5)^2 + (
    -0.5235243911248123 + x6)^2) + x924 * ((-0.5687248806674255 + x4)^2 + (
    -0.4800426470754785 + x5)^2 + (-0.66476015670848 + x6)^2) + x925 * ((
    -0.01879712601243244 + x4)^2 + (-0.9597300904119254 + x5)^2 + (
    -0.6400022174824137 + x6)^2) + x926 * ((-0.4546748066299232 + x4)^2 + (
    -0.08414046444682621 + x5)^2 + (-0.39949639976218343 + x6)^2) + x927 * ((
    -0.17854814031575228 + x4)^2 + (-0.24423555096632876 + x5)^2 + (
    -0.31176738263506176 + x6)^2) + x928 * ((-0.9738568400798214 + x4)^2 + (
    -0.9761211517297564 + x5)^2 + (-0.12716216361863075 + x6)^2) + x929 * ((
    -0.10905660727366906 + x4)^2 + (-0.9795748590019786 + x5)^2 + (
    -0.7440984394159507 + x6)^2) + x930 * ((-0.7666642751173116 + x4)^2 + (
    -0.3496890268415409 + x5)^2 + (-0.7178355854854029 + x6)^2) + x931 * ((
    -0.013742724746700241 + x4)^2 + (-0.43305298229497435 + x5)^2 + (
    -0.7254669199672814 + x6)^2) + x932 * ((-0.3275886542048829 + x4)^2 + (
    -0.8378680301704793 + x5)^2 + (-0.8349975326026666 + x6)^2) + x933 * ((
    -0.060805710429040816 + x4)^2 + (-0.656788371625089 + x5)^2 + (
    -0.2732796886924793 + x6)^2) + x934 * ((-0.9053177349583378 + x4)^2 + (
    -0.16127902677760553 + x5)^2 + (-0.32227488757718703 + x6)^2) + x935 * ((
    -0.9764291442509151 + x4)^2 + (-0.4200251729022414 + x5)^2 + (
    -0.19500625315790188 + x6)^2) + x936 * ((-0.17071396326782584 + x4)^2 + (
    -0.5019541154498613 + x5)^2 + (-0.6526843192881269 + x6)^2) + x937 * ((
    -0.9126755236735188 + x4)^2 + (-0.28940415967047584 + x5)^2 + (
    -0.1552734500527927 + x6)^2) + x938 * ((-0.5606535962065278 + x4)^2 + (
    -0.6342833304382927 + x5)^2 + (-0.8585431561155562 + x6)^2) + x939 * ((
    -0.11687570322670404 + x4)^2 + (-0.42299970942250387 + x5)^2 + (
    -0.4170059716014207 + x6)^2) + x940 * ((-0.5142371687254527 + x4)^2 + (
    -0.9857105100813118 + x5)^2 + (-0.5015291171995875 + x6)^2) + x941 * ((
    -0.32100216013315164 + x4)^2 + (-0.45572573844602215 + x5)^2 + (
    -0.48798435784356275 + x6)^2) + x942 * ((-0.597784767358479 + x4)^2 + (
    -0.05186929074401203 + x5)^2 + (-0.226366390881664 + x6)^2) + x943 * ((
    -0.8457016489109802 + x4)^2 + (-0.5554063005937154 + x5)^2 + (
    -0.41321444364538085 + x6)^2) + x944 * ((-0.9475471193586129 + x4)^2 + (
    -0.3121559515841179 + x5)^2 + (-0.14073436444324727 + x6)^2) + x945 * ((
    -0.7462797111675085 + x4)^2 + (-0.0832491058608037 + x5)^2 + (
    -0.16991972648761744 + x6)^2) + x946 * ((-0.6283905422614516 + x4)^2 + (
    -0.3473036441315591 + x5)^2 + (-0.6256420116557863 + x6)^2) + x947 * ((
    -0.47557752055186076 + x4)^2 + (-0.13087273477706074 + x5)^2 + (
    -0.566009659206059 + x6)^2) + x948 * ((-0.3811223652765986 + x4)^2 + (
    -0.3419162921570369 + x5)^2 + (-0.42670986021880697 + x6)^2) + x949 * ((
    -0.45276296485818746 + x4)^2 + (-0.7292869084688621 + x5)^2 + (
    -0.9219484257715016 + x6)^2) + x950 * ((-0.2944563711575213 + x4)^2 + (
    -0.9768141635311406 + x5)^2 + (-0.9139907883287979 + x6)^2) + x951 * ((
    -0.2045693815413957 + x4)^2 + (-0.6083069865306869 + x5)^2 + (
    -0.5354494090536733 + x6)^2) + x952 * ((-0.9092286101623649 + x4)^2 + (
    -0.19827382634748447 + x5)^2 + (-0.5692289216759975 + x6)^2) + x953 * ((
    -0.4428119569466705 + x4)^2 + (-0.3322800930778397 + x5)^2 + (
    -0.5707107027562174 + x6)^2) + x954 * ((-0.419027742190789 + x4)^2 + (
    -0.4618756991792069 + x5)^2 + (-0.07896233563766164 + x6)^2) + x955 * ((
    -0.6584988862725016 + x4)^2 + (-0.6148209199675768 + x5)^2 + (
    -0.24819109836653064 + x6)^2) + x956 * ((-0.7067453957053103 + x4)^2 + (
    -0.16400947550811773 + x5)^2 + (-0.2404675897181846 + x6)^2) + x957 * ((
    -0.6059340157584386 + x4)^2 + (-0.368724454571691 + x5)^2 + (
    -0.3166424342634133 + x6)^2) + x958 * ((-0.1505689967926862 + x4)^2 + (
    -0.625369145400853 + x5)^2 + (-0.8732323044478142 + x6)^2) + x959 * ((
    -0.4387938575304804 + x4)^2 + (-0.6686693605208012 + x5)^2 + (
    -0.5707959366759914 + x6)^2) + x960 * ((-0.7576333064836764 + x4)^2 + (
    -0.15002688954303656 + x5)^2 + (-0.15547993353000245 + x6)^2) + x961 * ((
    -0.666581715107795 + x4)^2 + (-0.8984605497623024 + x5)^2 + (
    -0.3096514261621284 + x6)^2) + x962 * ((-0.8387444625970372 + x4)^2 + (
    -0.16015110460364135 + x5)^2 + (-0.17793311971345638 + x6)^2) + x963 * ((
    -0.7961300734270524 + x4)^2 + (-0.06315804030987215 + x5)^2 + (
    -0.2886538911688289 + x6)^2) + x964 * ((-0.09882382311717897 + x4)^2 + (
    -0.9562490103711244 + x5)^2 + (-0.3979053832361369 + x6)^2) + x965 * ((
    -0.1313503761972874 + x4)^2 + (-0.1784477941922571 + x5)^2 + (
    -0.26652042199603243 + x6)^2) + x966 * ((-0.5560596702183167 + x4)^2 + (
    -0.776379609944948 + x5)^2 + (-0.4248340064314263 + x6)^2) + x967 * ((
    -0.061904031651977 + x4)^2 + (-0.6153844859790686 + x5)^2 + (
    -0.9267629321786096 + x6)^2) + x968 * ((-0.22406567435416147 + x4)^2 + (
    -0.16598467807059802 + x5)^2 + (-0.631039868789005 + x6)^2) + x969 * ((
    -0.2067711913915432 + x4)^2 + (-0.9546739138625829 + x5)^2 + (
    -0.6132888596828534 + x6)^2) + x970 * ((-0.698359896593753 + x4)^2 + (
    -0.09633791817043569 + x5)^2 + (-0.7767762514491409 + x6)^2) + x971 * ((
    -0.5495935658571374 + x4)^2 + (-0.08474290481778801 + x5)^2 + (
    -0.6612846791750243 + x6)^2) + x972 * ((-0.3161875292045071 + x4)^2 + (
    -0.6387922458536845 + x5)^2 + (-0.7653392459044 + x6)^2) + x973 * ((
    -0.7319358324745259 + x4)^2 + (-0.992182632521313 + x5)^2 + (
    -0.6863923077018874 + x6)^2) + x974 * ((-0.6019092920263115 + x4)^2 + (
    -0.7773860008024426 + x5)^2 + (-0.696651134077001 + x6)^2) + x975 * ((
    -0.8049096869634418 + x4)^2 + (-0.0732355551315873 + x5)^2 + (
    -0.5890554014646376 + x6)^2) + x976 * ((-0.2400029979216146 + x4)^2 + (
    -0.9945676004924368 + x5)^2 + (-0.5289410390414967 + x6)^2) + x977 * ((
    -0.2766431455253143 + x4)^2 + (-0.8539068538716186 + x5)^2 + (
    -0.20627516491122866 + x6)^2) + x978 * ((-0.35956937240024434 + x4)^2 + (
    -0.1564680965685581 + x5)^2 + (-0.13254723904140797 + x6)^2) + x979 * ((
    -0.6851905938616645 + x4)^2 + (-0.92350145756233 + x5)^2 + (
    -0.12850409116051253 + x6)^2) + x980 * ((-0.8530335314027025 + x4)^2 + (
    -0.014728381555152992 + x5)^2 + (-0.3823239089970707 + x6)^2) + x981 * ((
    -0.20793230117071493 + x4)^2 + (-0.16676956450110558 + x5)^2 + (
    -0.34228112340343475 + x6)^2) + x982 * ((-0.6234604214732817 + x4)^2 + (
    -0.2502728265106259 + x5)^2 + (-0.3410768048568552 + x6)^2) + x983 * ((
    -0.32574485718659996 + x4)^2 + (-0.49133487411842436 + x5)^2 + (
    -0.9269586652185272 + x6)^2) + x984 * ((-0.8074001332885633 + x4)^2 + (
    -0.436124135331206 + x5)^2 + (-0.6967988731368366 + x6)^2) + x985 * ((
    -0.0885078496198809 + x4)^2 + (-0.06383953819167731 + x5)^2 + (
    -0.12724142698377883 + x6)^2) + x986 * ((-0.2337562876270498 + x4)^2 + (
    -0.17694669799647322 + x5)^2 + (-0.24213277883073392 + x6)^2) + x987 * ((
    -0.4489386544210575 + x4)^2 + (-0.39350049538525844 + x5)^2 + (
    -0.2766646939987202 + x6)^2) + x988 * ((-0.6295217224500858 + x4)^2 + (
    -0.2004219022799547 + x5)^2 + (-0.34401008781100983 + x6)^2) + x989 * ((
    -0.7178536888350097 + x4)^2 + (-0.4777123128107543 + x5)^2 + (
    -0.020254499193558706 + x6)^2) + x990 * ((-0.11689305631558389 + x4)^2 + (
    -0.7921096764850253 + x5)^2 + (-0.0018493281679282658 + x6)^2) + x991 * ((
    -0.42252861541271625 + x4)^2 + (-0.7365281026729076 + x5)^2 + (
    -0.24208265132422635 + x6)^2) + x992 * ((-0.7215969240513533 + x4)^2 + (
    -0.3256843299668196 + x5)^2 + (-0.3698108298221342 + x6)^2) + x993 * ((
    -0.2595423236714335 + x4)^2 + (-0.2589559818665762 + x5)^2 + (
    -0.18615386799497224 + x6)^2) + x994 * ((-0.9984305905352117 + x4)^2 + (
    -0.7165229939904344 + x5)^2 + (-0.1285692611907402 + x6)^2) + x995 * ((
    -0.8872140808683944 + x4)^2 + (-0.5011145036032805 + x5)^2 + (
    -0.3883708507632184 + x6)^2) + x996 * ((-0.3924529848246979 + x4)^2 + (
    -0.22348565481301363 + x5)^2 + (-0.2061044173907518 + x6)^2) + x997 * ((
    -0.9112329633612304 + x4)^2 + (-0.3163218232655004 + x5)^2 + (
    -0.20302411889796268 + x6)^2) + x998 * ((-0.6097913445881256 + x4)^2 + (
    -0.4542976898151134 + x5)^2 + (-0.6195483822905107 + x6)^2) + x999 * ((
    -0.15522553621050394 + x4)^2 + (-0.01999404860523235 + x5)^2 + (
    -0.23442286593451234 + x6)^2) + x1000 * ((-0.9199134838866957 + x4)^2 + (
    -0.7868442189111334 + x5)^2 + (-0.34080460170453486 + x6)^2) + x1001 * ((
    -0.8166348595782067 + x4)^2 + (-0.7614497805023087 + x5)^2 + (
    -0.5452680081023854 + x6)^2) + x1002 * ((-0.7603340178252571 + x4)^2 + (
    -0.08882941137693179 + x5)^2 + (-0.31747640494684937 + x6)^2) + x1003 * ((
    -0.5390106156174557 + x4)^2 + (-0.4032399762516905 + x5)^2 + (
    -0.034174294693909646 + x6)^2) + x1004 * ((-0.6762581280338263 + x4)^2 + (
    -0.1341686429284461 + x5)^2 + (-0.6300346342580874 + x6)^2) + x1005 * ((
    -0.5985705326875344 + x4)^2 + (-0.6782117564373487 + x5)^2 + (
    -0.9723972807848017 + x6)^2) + x1006 * ((-0.9582896782474865 + x4)^2 + (
    -0.647483553547818 + x5)^2 + (-0.2553574307779871 + x6)^2))

@constraint(m, e1, x7 + x507 == 1)
@constraint(m, e2, x8 + x508 == 1)
@constraint(m, e3, x9 + x509 == 1)
@constraint(m, e4, x10 + x510 == 1)
@constraint(m, e5, x11 + x511 == 1)
@constraint(m, e6, x12 + x512 == 1)
@constraint(m, e7, x13 + x513 == 1)
@constraint(m, e8, x14 + x514 == 1)
@constraint(m, e9, x15 + x515 == 1)
@constraint(m, e10, x16 + x516 == 1)
@constraint(m, e11, x17 + x517 == 1)
@constraint(m, e12, x18 + x518 == 1)
@constraint(m, e13, x19 + x519 == 1)
@constraint(m, e14, x20 + x520 == 1)
@constraint(m, e15, x21 + x521 == 1)
@constraint(m, e16, x22 + x522 == 1)
@constraint(m, e17, x23 + x523 == 1)
@constraint(m, e18, x24 + x524 == 1)
@constraint(m, e19, x25 + x525 == 1)
@constraint(m, e20, x26 + x526 == 1)
@constraint(m, e21, x27 + x527 == 1)
@constraint(m, e22, x28 + x528 == 1)
@constraint(m, e23, x29 + x529 == 1)
@constraint(m, e24, x30 + x530 == 1)
@constraint(m, e25, x31 + x531 == 1)
@constraint(m, e26, x32 + x532 == 1)
@constraint(m, e27, x33 + x533 == 1)
@constraint(m, e28, x34 + x534 == 1)
@constraint(m, e29, x35 + x535 == 1)
@constraint(m, e30, x36 + x536 == 1)
@constraint(m, e31, x37 + x537 == 1)
@constraint(m, e32, x38 + x538 == 1)
@constraint(m, e33, x39 + x539 == 1)
@constraint(m, e34, x40 + x540 == 1)
@constraint(m, e35, x41 + x541 == 1)
@constraint(m, e36, x42 + x542 == 1)
@constraint(m, e37, x43 + x543 == 1)
@constraint(m, e38, x44 + x544 == 1)
@constraint(m, e39, x45 + x545 == 1)
@constraint(m, e40, x46 + x546 == 1)
@constraint(m, e41, x47 + x547 == 1)
@constraint(m, e42, x48 + x548 == 1)
@constraint(m, e43, x49 + x549 == 1)
@constraint(m, e44, x50 + x550 == 1)
@constraint(m, e45, x51 + x551 == 1)
@constraint(m, e46, x52 + x552 == 1)
@constraint(m, e47, x53 + x553 == 1)
@constraint(m, e48, x54 + x554 == 1)
@constraint(m, e49, x55 + x555 == 1)
@constraint(m, e50, x56 + x556 == 1)
@constraint(m, e51, x57 + x557 == 1)
@constraint(m, e52, x58 + x558 == 1)
@constraint(m, e53, x59 + x559 == 1)
@constraint(m, e54, x60 + x560 == 1)
@constraint(m, e55, x61 + x561 == 1)
@constraint(m, e56, x62 + x562 == 1)
@constraint(m, e57, x63 + x563 == 1)
@constraint(m, e58, x64 + x564 == 1)
@constraint(m, e59, x65 + x565 == 1)
@constraint(m, e60, x66 + x566 == 1)
@constraint(m, e61, x67 + x567 == 1)
@constraint(m, e62, x68 + x568 == 1)
@constraint(m, e63, x69 + x569 == 1)
@constraint(m, e64, x70 + x570 == 1)
@constraint(m, e65, x71 + x571 == 1)
@constraint(m, e66, x72 + x572 == 1)
@constraint(m, e67, x73 + x573 == 1)
@constraint(m, e68, x74 + x574 == 1)
@constraint(m, e69, x75 + x575 == 1)
@constraint(m, e70, x76 + x576 == 1)
@constraint(m, e71, x77 + x577 == 1)
@constraint(m, e72, x78 + x578 == 1)
@constraint(m, e73, x79 + x579 == 1)
@constraint(m, e74, x80 + x580 == 1)
@constraint(m, e75, x81 + x581 == 1)
@constraint(m, e76, x82 + x582 == 1)
@constraint(m, e77, x83 + x583 == 1)
@constraint(m, e78, x84 + x584 == 1)
@constraint(m, e79, x85 + x585 == 1)
@constraint(m, e80, x86 + x586 == 1)
@constraint(m, e81, x87 + x587 == 1)
@constraint(m, e82, x88 + x588 == 1)
@constraint(m, e83, x89 + x589 == 1)
@constraint(m, e84, x90 + x590 == 1)
@constraint(m, e85, x91 + x591 == 1)
@constraint(m, e86, x92 + x592 == 1)
@constraint(m, e87, x93 + x593 == 1)
@constraint(m, e88, x94 + x594 == 1)
@constraint(m, e89, x95 + x595 == 1)
@constraint(m, e90, x96 + x596 == 1)
@constraint(m, e91, x97 + x597 == 1)
@constraint(m, e92, x98 + x598 == 1)
@constraint(m, e93, x99 + x599 == 1)
@constraint(m, e94, x100 + x600 == 1)
@constraint(m, e95, x101 + x601 == 1)
@constraint(m, e96, x102 + x602 == 1)
@constraint(m, e97, x103 + x603 == 1)
@constraint(m, e98, x104 + x604 == 1)
@constraint(m, e99, x105 + x605 == 1)
@constraint(m, e100, x106 + x606 == 1)
@constraint(m, e101, x107 + x607 == 1)
@constraint(m, e102, x108 + x608 == 1)
@constraint(m, e103, x109 + x609 == 1)
@constraint(m, e104, x110 + x610 == 1)
@constraint(m, e105, x111 + x611 == 1)
@constraint(m, e106, x112 + x612 == 1)
@constraint(m, e107, x113 + x613 == 1)
@constraint(m, e108, x114 + x614 == 1)
@constraint(m, e109, x115 + x615 == 1)
@constraint(m, e110, x116 + x616 == 1)
@constraint(m, e111, x117 + x617 == 1)
@constraint(m, e112, x118 + x618 == 1)
@constraint(m, e113, x119 + x619 == 1)
@constraint(m, e114, x120 + x620 == 1)
@constraint(m, e115, x121 + x621 == 1)
@constraint(m, e116, x122 + x622 == 1)
@constraint(m, e117, x123 + x623 == 1)
@constraint(m, e118, x124 + x624 == 1)
@constraint(m, e119, x125 + x625 == 1)
@constraint(m, e120, x126 + x626 == 1)
@constraint(m, e121, x127 + x627 == 1)
@constraint(m, e122, x128 + x628 == 1)
@constraint(m, e123, x129 + x629 == 1)
@constraint(m, e124, x130 + x630 == 1)
@constraint(m, e125, x131 + x631 == 1)
@constraint(m, e126, x132 + x632 == 1)
@constraint(m, e127, x133 + x633 == 1)
@constraint(m, e128, x134 + x634 == 1)
@constraint(m, e129, x135 + x635 == 1)
@constraint(m, e130, x136 + x636 == 1)
@constraint(m, e131, x137 + x637 == 1)
@constraint(m, e132, x138 + x638 == 1)
@constraint(m, e133, x139 + x639 == 1)
@constraint(m, e134, x140 + x640 == 1)
@constraint(m, e135, x141 + x641 == 1)
@constraint(m, e136, x142 + x642 == 1)
@constraint(m, e137, x143 + x643 == 1)
@constraint(m, e138, x144 + x644 == 1)
@constraint(m, e139, x145 + x645 == 1)
@constraint(m, e140, x146 + x646 == 1)
@constraint(m, e141, x147 + x647 == 1)
@constraint(m, e142, x148 + x648 == 1)
@constraint(m, e143, x149 + x649 == 1)
@constraint(m, e144, x150 + x650 == 1)
@constraint(m, e145, x151 + x651 == 1)
@constraint(m, e146, x152 + x652 == 1)
@constraint(m, e147, x153 + x653 == 1)
@constraint(m, e148, x154 + x654 == 1)
@constraint(m, e149, x155 + x655 == 1)
@constraint(m, e150, x156 + x656 == 1)
@constraint(m, e151, x157 + x657 == 1)
@constraint(m, e152, x158 + x658 == 1)
@constraint(m, e153, x159 + x659 == 1)
@constraint(m, e154, x160 + x660 == 1)
@constraint(m, e155, x161 + x661 == 1)
@constraint(m, e156, x162 + x662 == 1)
@constraint(m, e157, x163 + x663 == 1)
@constraint(m, e158, x164 + x664 == 1)
@constraint(m, e159, x165 + x665 == 1)
@constraint(m, e160, x166 + x666 == 1)
@constraint(m, e161, x167 + x667 == 1)
@constraint(m, e162, x168 + x668 == 1)
@constraint(m, e163, x169 + x669 == 1)
@constraint(m, e164, x170 + x670 == 1)
@constraint(m, e165, x171 + x671 == 1)
@constraint(m, e166, x172 + x672 == 1)
@constraint(m, e167, x173 + x673 == 1)
@constraint(m, e168, x174 + x674 == 1)
@constraint(m, e169, x175 + x675 == 1)
@constraint(m, e170, x176 + x676 == 1)
@constraint(m, e171, x177 + x677 == 1)
@constraint(m, e172, x178 + x678 == 1)
@constraint(m, e173, x179 + x679 == 1)
@constraint(m, e174, x180 + x680 == 1)
@constraint(m, e175, x181 + x681 == 1)
@constraint(m, e176, x182 + x682 == 1)
@constraint(m, e177, x183 + x683 == 1)
@constraint(m, e178, x184 + x684 == 1)
@constraint(m, e179, x185 + x685 == 1)
@constraint(m, e180, x186 + x686 == 1)
@constraint(m, e181, x187 + x687 == 1)
@constraint(m, e182, x188 + x688 == 1)
@constraint(m, e183, x189 + x689 == 1)
@constraint(m, e184, x190 + x690 == 1)
@constraint(m, e185, x191 + x691 == 1)
@constraint(m, e186, x192 + x692 == 1)
@constraint(m, e187, x193 + x693 == 1)
@constraint(m, e188, x194 + x694 == 1)
@constraint(m, e189, x195 + x695 == 1)
@constraint(m, e190, x196 + x696 == 1)
@constraint(m, e191, x197 + x697 == 1)
@constraint(m, e192, x198 + x698 == 1)
@constraint(m, e193, x199 + x699 == 1)
@constraint(m, e194, x200 + x700 == 1)
@constraint(m, e195, x201 + x701 == 1)
@constraint(m, e196, x202 + x702 == 1)
@constraint(m, e197, x203 + x703 == 1)
@constraint(m, e198, x204 + x704 == 1)
@constraint(m, e199, x205 + x705 == 1)
@constraint(m, e200, x206 + x706 == 1)
@constraint(m, e201, x207 + x707 == 1)
@constraint(m, e202, x208 + x708 == 1)
@constraint(m, e203, x209 + x709 == 1)
@constraint(m, e204, x210 + x710 == 1)
@constraint(m, e205, x211 + x711 == 1)
@constraint(m, e206, x212 + x712 == 1)
@constraint(m, e207, x213 + x713 == 1)
@constraint(m, e208, x214 + x714 == 1)
@constraint(m, e209, x215 + x715 == 1)
@constraint(m, e210, x216 + x716 == 1)
@constraint(m, e211, x217 + x717 == 1)
@constraint(m, e212, x218 + x718 == 1)
@constraint(m, e213, x219 + x719 == 1)
@constraint(m, e214, x220 + x720 == 1)
@constraint(m, e215, x221 + x721 == 1)
@constraint(m, e216, x222 + x722 == 1)
@constraint(m, e217, x223 + x723 == 1)
@constraint(m, e218, x224 + x724 == 1)
@constraint(m, e219, x225 + x725 == 1)
@constraint(m, e220, x226 + x726 == 1)
@constraint(m, e221, x227 + x727 == 1)
@constraint(m, e222, x228 + x728 == 1)
@constraint(m, e223, x229 + x729 == 1)
@constraint(m, e224, x230 + x730 == 1)
@constraint(m, e225, x231 + x731 == 1)
@constraint(m, e226, x232 + x732 == 1)
@constraint(m, e227, x233 + x733 == 1)
@constraint(m, e228, x234 + x734 == 1)
@constraint(m, e229, x235 + x735 == 1)
@constraint(m, e230, x236 + x736 == 1)
@constraint(m, e231, x237 + x737 == 1)
@constraint(m, e232, x238 + x738 == 1)
@constraint(m, e233, x239 + x739 == 1)
@constraint(m, e234, x240 + x740 == 1)
@constraint(m, e235, x241 + x741 == 1)
@constraint(m, e236, x242 + x742 == 1)
@constraint(m, e237, x243 + x743 == 1)
@constraint(m, e238, x244 + x744 == 1)
@constraint(m, e239, x245 + x745 == 1)
@constraint(m, e240, x246 + x746 == 1)
@constraint(m, e241, x247 + x747 == 1)
@constraint(m, e242, x248 + x748 == 1)
@constraint(m, e243, x249 + x749 == 1)
@constraint(m, e244, x250 + x750 == 1)
@constraint(m, e245, x251 + x751 == 1)
@constraint(m, e246, x252 + x752 == 1)
@constraint(m, e247, x253 + x753 == 1)
@constraint(m, e248, x254 + x754 == 1)
@constraint(m, e249, x255 + x755 == 1)
@constraint(m, e250, x256 + x756 == 1)
@constraint(m, e251, x257 + x757 == 1)
@constraint(m, e252, x258 + x758 == 1)
@constraint(m, e253, x259 + x759 == 1)
@constraint(m, e254, x260 + x760 == 1)
@constraint(m, e255, x261 + x761 == 1)
@constraint(m, e256, x262 + x762 == 1)
@constraint(m, e257, x263 + x763 == 1)
@constraint(m, e258, x264 + x764 == 1)
@constraint(m, e259, x265 + x765 == 1)
@constraint(m, e260, x266 + x766 == 1)
@constraint(m, e261, x267 + x767 == 1)
@constraint(m, e262, x268 + x768 == 1)
@constraint(m, e263, x269 + x769 == 1)
@constraint(m, e264, x270 + x770 == 1)
@constraint(m, e265, x271 + x771 == 1)
@constraint(m, e266, x272 + x772 == 1)
@constraint(m, e267, x273 + x773 == 1)
@constraint(m, e268, x274 + x774 == 1)
@constraint(m, e269, x275 + x775 == 1)
@constraint(m, e270, x276 + x776 == 1)
@constraint(m, e271, x277 + x777 == 1)
@constraint(m, e272, x278 + x778 == 1)
@constraint(m, e273, x279 + x779 == 1)
@constraint(m, e274, x280 + x780 == 1)
@constraint(m, e275, x281 + x781 == 1)
@constraint(m, e276, x282 + x782 == 1)
@constraint(m, e277, x283 + x783 == 1)
@constraint(m, e278, x284 + x784 == 1)
@constraint(m, e279, x285 + x785 == 1)
@constraint(m, e280, x286 + x786 == 1)
@constraint(m, e281, x287 + x787 == 1)
@constraint(m, e282, x288 + x788 == 1)
@constraint(m, e283, x289 + x789 == 1)
@constraint(m, e284, x290 + x790 == 1)
@constraint(m, e285, x291 + x791 == 1)
@constraint(m, e286, x292 + x792 == 1)
@constraint(m, e287, x293 + x793 == 1)
@constraint(m, e288, x294 + x794 == 1)
@constraint(m, e289, x295 + x795 == 1)
@constraint(m, e290, x296 + x796 == 1)
@constraint(m, e291, x297 + x797 == 1)
@constraint(m, e292, x298 + x798 == 1)
@constraint(m, e293, x299 + x799 == 1)
@constraint(m, e294, x300 + x800 == 1)
@constraint(m, e295, x301 + x801 == 1)
@constraint(m, e296, x302 + x802 == 1)
@constraint(m, e297, x303 + x803 == 1)
@constraint(m, e298, x304 + x804 == 1)
@constraint(m, e299, x305 + x805 == 1)
@constraint(m, e300, x306 + x806 == 1)
@constraint(m, e301, x307 + x807 == 1)
@constraint(m, e302, x308 + x808 == 1)
@constraint(m, e303, x309 + x809 == 1)
@constraint(m, e304, x310 + x810 == 1)
@constraint(m, e305, x311 + x811 == 1)
@constraint(m, e306, x312 + x812 == 1)
@constraint(m, e307, x313 + x813 == 1)
@constraint(m, e308, x314 + x814 == 1)
@constraint(m, e309, x315 + x815 == 1)
@constraint(m, e310, x316 + x816 == 1)
@constraint(m, e311, x317 + x817 == 1)
@constraint(m, e312, x318 + x818 == 1)
@constraint(m, e313, x319 + x819 == 1)
@constraint(m, e314, x320 + x820 == 1)
@constraint(m, e315, x321 + x821 == 1)
@constraint(m, e316, x322 + x822 == 1)
@constraint(m, e317, x323 + x823 == 1)
@constraint(m, e318, x324 + x824 == 1)
@constraint(m, e319, x325 + x825 == 1)
@constraint(m, e320, x326 + x826 == 1)
@constraint(m, e321, x327 + x827 == 1)
@constraint(m, e322, x328 + x828 == 1)
@constraint(m, e323, x329 + x829 == 1)
@constraint(m, e324, x330 + x830 == 1)
@constraint(m, e325, x331 + x831 == 1)
@constraint(m, e326, x332 + x832 == 1)
@constraint(m, e327, x333 + x833 == 1)
@constraint(m, e328, x334 + x834 == 1)
@constraint(m, e329, x335 + x835 == 1)
@constraint(m, e330, x336 + x836 == 1)
@constraint(m, e331, x337 + x837 == 1)
@constraint(m, e332, x338 + x838 == 1)
@constraint(m, e333, x339 + x839 == 1)
@constraint(m, e334, x340 + x840 == 1)
@constraint(m, e335, x341 + x841 == 1)
@constraint(m, e336, x342 + x842 == 1)
@constraint(m, e337, x343 + x843 == 1)
@constraint(m, e338, x344 + x844 == 1)
@constraint(m, e339, x345 + x845 == 1)
@constraint(m, e340, x346 + x846 == 1)
@constraint(m, e341, x347 + x847 == 1)
@constraint(m, e342, x348 + x848 == 1)
@constraint(m, e343, x349 + x849 == 1)
@constraint(m, e344, x350 + x850 == 1)
@constraint(m, e345, x351 + x851 == 1)
@constraint(m, e346, x352 + x852 == 1)
@constraint(m, e347, x353 + x853 == 1)
@constraint(m, e348, x354 + x854 == 1)
@constraint(m, e349, x355 + x855 == 1)
@constraint(m, e350, x356 + x856 == 1)
@constraint(m, e351, x357 + x857 == 1)
@constraint(m, e352, x358 + x858 == 1)
@constraint(m, e353, x359 + x859 == 1)
@constraint(m, e354, x360 + x860 == 1)
@constraint(m, e355, x361 + x861 == 1)
@constraint(m, e356, x362 + x862 == 1)
@constraint(m, e357, x363 + x863 == 1)
@constraint(m, e358, x364 + x864 == 1)
@constraint(m, e359, x365 + x865 == 1)
@constraint(m, e360, x366 + x866 == 1)
@constraint(m, e361, x367 + x867 == 1)
@constraint(m, e362, x368 + x868 == 1)
@constraint(m, e363, x369 + x869 == 1)
@constraint(m, e364, x370 + x870 == 1)
@constraint(m, e365, x371 + x871 == 1)
@constraint(m, e366, x372 + x872 == 1)
@constraint(m, e367, x373 + x873 == 1)
@constraint(m, e368, x374 + x874 == 1)
@constraint(m, e369, x375 + x875 == 1)
@constraint(m, e370, x376 + x876 == 1)
@constraint(m, e371, x377 + x877 == 1)
@constraint(m, e372, x378 + x878 == 1)
@constraint(m, e373, x379 + x879 == 1)
@constraint(m, e374, x380 + x880 == 1)
@constraint(m, e375, x381 + x881 == 1)
@constraint(m, e376, x382 + x882 == 1)
@constraint(m, e377, x383 + x883 == 1)
@constraint(m, e378, x384 + x884 == 1)
@constraint(m, e379, x385 + x885 == 1)
@constraint(m, e380, x386 + x886 == 1)
@constraint(m, e381, x387 + x887 == 1)
@constraint(m, e382, x388 + x888 == 1)
@constraint(m, e383, x389 + x889 == 1)
@constraint(m, e384, x390 + x890 == 1)
@constraint(m, e385, x391 + x891 == 1)
@constraint(m, e386, x392 + x892 == 1)
@constraint(m, e387, x393 + x893 == 1)
@constraint(m, e388, x394 + x894 == 1)
@constraint(m, e389, x395 + x895 == 1)
@constraint(m, e390, x396 + x896 == 1)
@constraint(m, e391, x397 + x897 == 1)
@constraint(m, e392, x398 + x898 == 1)
@constraint(m, e393, x399 + x899 == 1)
@constraint(m, e394, x400 + x900 == 1)
@constraint(m, e395, x401 + x901 == 1)
@constraint(m, e396, x402 + x902 == 1)
@constraint(m, e397, x403 + x903 == 1)
@constraint(m, e398, x404 + x904 == 1)
@constraint(m, e399, x405 + x905 == 1)
@constraint(m, e400, x406 + x906 == 1)
@constraint(m, e401, x407 + x907 == 1)
@constraint(m, e402, x408 + x908 == 1)
@constraint(m, e403, x409 + x909 == 1)
@constraint(m, e404, x410 + x910 == 1)
@constraint(m, e405, x411 + x911 == 1)
@constraint(m, e406, x412 + x912 == 1)
@constraint(m, e407, x413 + x913 == 1)
@constraint(m, e408, x414 + x914 == 1)
@constraint(m, e409, x415 + x915 == 1)
@constraint(m, e410, x416 + x916 == 1)
@constraint(m, e411, x417 + x917 == 1)
@constraint(m, e412, x418 + x918 == 1)
@constraint(m, e413, x419 + x919 == 1)
@constraint(m, e414, x420 + x920 == 1)
@constraint(m, e415, x421 + x921 == 1)
@constraint(m, e416, x422 + x922 == 1)
@constraint(m, e417, x423 + x923 == 1)
@constraint(m, e418, x424 + x924 == 1)
@constraint(m, e419, x425 + x925 == 1)
@constraint(m, e420, x426 + x926 == 1)
@constraint(m, e421, x427 + x927 == 1)
@constraint(m, e422, x428 + x928 == 1)
@constraint(m, e423, x429 + x929 == 1)
@constraint(m, e424, x430 + x930 == 1)
@constraint(m, e425, x431 + x931 == 1)
@constraint(m, e426, x432 + x932 == 1)
@constraint(m, e427, x433 + x933 == 1)
@constraint(m, e428, x434 + x934 == 1)
@constraint(m, e429, x435 + x935 == 1)
@constraint(m, e430, x436 + x936 == 1)
@constraint(m, e431, x437 + x937 == 1)
@constraint(m, e432, x438 + x938 == 1)
@constraint(m, e433, x439 + x939 == 1)
@constraint(m, e434, x440 + x940 == 1)
@constraint(m, e435, x441 + x941 == 1)
@constraint(m, e436, x442 + x942 == 1)
@constraint(m, e437, x443 + x943 == 1)
@constraint(m, e438, x444 + x944 == 1)
@constraint(m, e439, x445 + x945 == 1)
@constraint(m, e440, x446 + x946 == 1)
@constraint(m, e441, x447 + x947 == 1)
@constraint(m, e442, x448 + x948 == 1)
@constraint(m, e443, x449 + x949 == 1)
@constraint(m, e444, x450 + x950 == 1)
@constraint(m, e445, x451 + x951 == 1)
@constraint(m, e446, x452 + x952 == 1)
@constraint(m, e447, x453 + x953 == 1)
@constraint(m, e448, x454 + x954 == 1)
@constraint(m, e449, x455 + x955 == 1)
@constraint(m, e450, x456 + x956 == 1)
@constraint(m, e451, x457 + x957 == 1)
@constraint(m, e452, x458 + x958 == 1)
@constraint(m, e453, x459 + x959 == 1)
@constraint(m, e454, x460 + x960 == 1)
@constraint(m, e455, x461 + x961 == 1)
@constraint(m, e456, x462 + x962 == 1)
@constraint(m, e457, x463 + x963 == 1)
@constraint(m, e458, x464 + x964 == 1)
@constraint(m, e459, x465 + x965 == 1)
@constraint(m, e460, x466 + x966 == 1)
@constraint(m, e461, x467 + x967 == 1)
@constraint(m, e462, x468 + x968 == 1)
@constraint(m, e463, x469 + x969 == 1)
@constraint(m, e464, x470 + x970 == 1)
@constraint(m, e465, x471 + x971 == 1)
@constraint(m, e466, x472 + x972 == 1)
@constraint(m, e467, x473 + x973 == 1)
@constraint(m, e468, x474 + x974 == 1)
@constraint(m, e469, x475 + x975 == 1)
@constraint(m, e470, x476 + x976 == 1)
@constraint(m, e471, x477 + x977 == 1)
@constraint(m, e472, x478 + x978 == 1)
@constraint(m, e473, x479 + x979 == 1)
@constraint(m, e474, x480 + x980 == 1)
@constraint(m, e475, x481 + x981 == 1)
@constraint(m, e476, x482 + x982 == 1)
@constraint(m, e477, x483 + x983 == 1)
@constraint(m, e478, x484 + x984 == 1)
@constraint(m, e479, x485 + x985 == 1)
@constraint(m, e480, x486 + x986 == 1)
@constraint(m, e481, x487 + x987 == 1)
@constraint(m, e482, x488 + x988 == 1)
@constraint(m, e483, x489 + x989 == 1)
@constraint(m, e484, x490 + x990 == 1)
@constraint(m, e485, x491 + x991 == 1)
@constraint(m, e486, x492 + x992 == 1)
@constraint(m, e487, x493 + x993 == 1)
@constraint(m, e488, x494 + x994 == 1)
@constraint(m, e489, x495 + x995 == 1)
@constraint(m, e490, x496 + x996 == 1)
@constraint(m, e491, x497 + x997 == 1)
@constraint(m, e492, x498 + x998 == 1)
@constraint(m, e493, x499 + x999 == 1)
@constraint(m, e494, x500 + x1000 == 1)
@constraint(m, e495, x501 + x1001 == 1)
@constraint(m, e496, x502 + x1002 == 1)
@constraint(m, e497, x503 + x1003 == 1)
@constraint(m, e498, x504 + x1004 == 1)
@constraint(m, e499, x505 + x1005 == 1)
@constraint(m, e500, x506 + x1006 == 1)
