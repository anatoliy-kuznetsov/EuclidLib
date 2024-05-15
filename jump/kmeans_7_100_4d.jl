# NLP written by GAMS Convert at 05/15/24 11:31:42
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       100      100        0        0        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#       728      728        0        0        0        0        0        0
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
@variable(m, 0 <= x722 <= 1, start=0)
@variable(m, 0 <= x723 <= 1, start=0)
@variable(m, 0 <= x724 <= 1, start=0)
@variable(m, 0 <= x725 <= 1, start=0)
@variable(m, 0 <= x726 <= 1, start=0)
@variable(m, 0 <= x727 <= 1, start=0)
@variable(m, 0 <= x728 <= 1, start=0)

@NLobjective(m, Min, x29 * ((-0.6582625122649799 + x1)^2 + (
    -0.10362896941145872 + x2)^2 + (-0.8195797598856802 + x3)^2 + (
    -0.5422289997742272 + x4)^2) + x30 * ((-0.3661207081728268 + x1)^2 + (
    -0.7480408210929997 + x2)^2 + (-0.6813605839850432 + x3)^2 + (
    -0.5056692315871436 + x4)^2) + x31 * ((-0.07046798157590661 + x1)^2 + (
    -0.5775220724425275 + x2)^2 + (-0.7916097196998284 + x3)^2 + (
    -0.9106301943747759 + x4)^2) + x32 * ((-0.9143624080891343 + x1)^2 + (
    -0.5102176451888726 + x2)^2 + (-0.46023708546130926 + x3)^2 + (
    -0.21559477969887786 + x4)^2) + x33 * ((-0.2152968191062874 + x1)^2 + (
    -0.40849216327387305 + x2)^2 + (-0.20734483145145233 + x3)^2 + (
    -0.29299530170003807 + x4)^2) + x34 * ((-0.753381482947803 + x1)^2 + (
    -0.569021356481719 + x2)^2 + (-0.825772931187451 + x3)^2 + (
    -0.6717803623991925 + x4)^2) + x35 * ((-0.22558272825834902 + x1)^2 + (
    -0.1431433457263549 + x2)^2 + (-0.36496670173321977 + x3)^2 + (
    -0.8283121504397382 + x4)^2) + x36 * ((-0.1043150551410561 + x1)^2 + (
    -0.5878900110989006 + x2)^2 + (-0.9303409193762857 + x3)^2 + (
    -0.1857245451574967 + x4)^2) + x37 * ((-0.2569777266497605 + x1)^2 + (
    -0.44043166993274085 + x2)^2 + (-0.15843257127556898 + x3)^2 + (
    -0.952596167014909 + x4)^2) + x38 * ((-0.767248128715498 + x1)^2 + (
    -0.16237189449331368 + x2)^2 + (-0.06342633508651152 + x3)^2 + (
    -0.8024171562438219 + x4)^2) + x39 * ((-0.7172302300642502 + x1)^2 + (
    -0.3391758201292703 + x2)^2 + (-0.030384935563099513 + x3)^2 + (
    -0.06493483472263029 + x4)^2) + x40 * ((-0.3661672203776154 + x1)^2 + (
    -0.9542180221871335 + x2)^2 + (-0.5308186536817474 + x3)^2 + (
    -0.16997124480838255 + x4)^2) + x41 * ((-0.23659736779603846 + x1)^2 + (
    -0.6214607353719023 + x2)^2 + (-0.3081993619295993 + x3)^2 + (
    -0.3526409606385007 + x4)^2) + x42 * ((-0.9752782586626233 + x1)^2 + (
    -0.5844650261883885 + x2)^2 + (-0.37649426913773276 + x3)^2 + (
    -0.10816991983567104 + x4)^2) + x43 * ((-0.45932686546602697 + x1)^2 + (
    -0.21233217626711853 + x2)^2 + (-0.9164032346567896 + x3)^2 + (
    -0.37108439943759797 + x4)^2) + x44 * ((-0.6867210427728082 + x1)^2 + (
    -0.7796854955112769 + x2)^2 + (-0.11982168093807799 + x3)^2 + (
    -0.6159743897209107 + x4)^2) + x45 * ((-0.985368764646874 + x1)^2 + (
    -0.07384180286280495 + x2)^2 + (-0.12212817800129094 + x3)^2 + (
    -0.2984771462799074 + x4)^2) + x46 * ((-0.7476106092305221 + x1)^2 + (
    -0.4411310968444404 + x2)^2 + (-0.5921500130284744 + x3)^2 + (
    -0.4842613828145912 + x4)^2) + x47 * ((-0.9737472353802095 + x1)^2 + (
    -0.09330122936543495 + x2)^2 + (-0.6050695157211611 + x3)^2 + (
    -0.07252152451660332 + x4)^2) + x48 * ((-0.09013540585240642 + x1)^2 + (
    -0.31276776356555547 + x2)^2 + (-0.7994057211441843 + x3)^2 + (
    -0.22689981649412638 + x4)^2) + x49 * ((-0.6283164056152335 + x1)^2 + (
    -0.3785737682752087 + x2)^2 + (-0.0024714258559164204 + x3)^2 + (
    -0.8148514253118784 + x4)^2) + x50 * ((-0.45370880893982724 + x1)^2 + (
    -0.10391203375848834 + x2)^2 + (-0.24027615267372093 + x3)^2 + (
    -0.2552645467206819 + x4)^2) + x51 * ((-0.4061008020592297 + x1)^2 + (
    -0.9396418294747921 + x2)^2 + (-0.5690658238794261 + x3)^2 + (
    -0.16866076993955403 + x4)^2) + x52 * ((-0.2314528417813161 + x1)^2 + (
    -0.5525474743329635 + x2)^2 + (-0.24649406583643063 + x3)^2 + (
    -0.9613520728571585 + x4)^2) + x53 * ((-0.5139605500157903 + x1)^2 + (
    -0.6815512588331698 + x2)^2 + (-0.16796296820903867 + x3)^2 + (
    -0.7162074865739461 + x4)^2) + x54 * ((-0.7706393889182662 + x1)^2 + (
    -0.43003110845525816 + x2)^2 + (-0.9356475551939986 + x3)^2 + (
    -0.5933795966331403 + x4)^2) + x55 * ((-0.5249118669899329 + x1)^2 + (
    -0.04056638284243541 + x2)^2 + (-0.0768970587722112 + x3)^2 + (
    -0.8247484594687006 + x4)^2) + x56 * ((-0.824923342468354 + x1)^2 + (
    -0.24405019701972253 + x2)^2 + (-0.38404505866575367 + x3)^2 + (
    -0.8313733189621139 + x4)^2) + x57 * ((-0.33950374022026997 + x1)^2 + (
    -0.5976095637618721 + x2)^2 + (-0.7602631636886854 + x3)^2 + (
    -0.4500249936588927 + x4)^2) + x58 * ((-0.523162910024812 + x1)^2 + (
    -0.3436248527141411 + x2)^2 + (-0.4561418310928951 + x3)^2 + (
    -0.8742103555752229 + x4)^2) + x59 * ((-0.3337530963427443 + x1)^2 + (
    -0.9855745242910374 + x2)^2 + (-0.9617621389771519 + x3)^2 + (
    -0.22441530334931115 + x4)^2) + x60 * ((-0.25477260253407985 + x1)^2 + (
    -0.3657617338278605 + x2)^2 + (-0.4599755066722203 + x3)^2 + (
    -0.488019659535353 + x4)^2) + x61 * ((-0.2663904007493795 + x1)^2 + (
    -0.27222258016843315 + x2)^2 + (-0.2880874179930988 + x3)^2 + (
    -0.02481848847156809 + x4)^2) + x62 * ((-0.2075297065152052 + x1)^2 + (
    -0.7022983060607665 + x2)^2 + (-0.47827086724608314 + x3)^2 + (
    -0.28622027057302846 + x4)^2) + x63 * ((-0.7047452543816871 + x1)^2 + (
    -0.6996554684275655 + x2)^2 + (-0.16578869005033847 + x3)^2 + (
    -0.5179151157105838 + x4)^2) + x64 * ((-0.7436571093571753 + x1)^2 + (
    -0.8723672259073825 + x2)^2 + (-0.9145540584909153 + x3)^2 + (
    -0.4616843537475913 + x4)^2) + x65 * ((-0.40078313938185106 + x1)^2 + (
    -0.7616315326378316 + x2)^2 + (-0.0624885237314553 + x3)^2 + (
    -0.33349386555475435 + x4)^2) + x66 * ((-0.47083964839087056 + x1)^2 + (
    -0.7540812887396847 + x2)^2 + (-0.7698437223374434 + x3)^2 + (
    -0.7260097297577066 + x4)^2) + x67 * ((-0.470591984548581 + x1)^2 + (
    -0.21419699662552538 + x2)^2 + (-0.8214784727628405 + x3)^2 + (
    -0.9327146275722538 + x4)^2) + x68 * ((-0.6694092237740207 + x1)^2 + (
    -0.40188436538160965 + x2)^2 + (-0.9078829021652501 + x3)^2 + (
    -0.28882880291122615 + x4)^2) + x69 * ((-0.8012821680592233 + x1)^2 + (
    -0.26764801084685064 + x2)^2 + (-0.8907563902239161 + x3)^2 + (
    -0.022670562427511642 + x4)^2) + x70 * ((-0.3149563708936517 + x1)^2 + (
    -0.4013573755930997 + x2)^2 + (-0.16444723142036033 + x3)^2 + (
    -0.8783064548569166 + x4)^2) + x71 * ((-0.0452536291694966 + x1)^2 + (
    -0.6030683870184952 + x2)^2 + (-0.12061018849928773 + x3)^2 + (
    -0.6161186728209969 + x4)^2) + x72 * ((-0.8303237648967787 + x1)^2 + (
    -0.7542211701244139 + x2)^2 + (-0.47189785643150806 + x3)^2 + (
    -0.7928252514256884 + x4)^2) + x73 * ((-0.6429343022480377 + x1)^2 + (
    -0.6021334537878723 + x2)^2 + (-0.2852218418361189 + x3)^2 + (
    -0.29825945641738283 + x4)^2) + x74 * ((-0.11776074988832852 + x1)^2 + (
    -0.8643957197110975 + x2)^2 + (-0.03338227312045139 + x3)^2 + (
    -0.593939114377175 + x4)^2) + x75 * ((-0.418497245301816 + x1)^2 + (
    -0.3081055339744846 + x2)^2 + (-0.38130196746434064 + x3)^2 + (
    -0.6612469720321472 + x4)^2) + x76 * ((-0.5815493986252239 + x1)^2 + (
    -0.6811102264085155 + x2)^2 + (-0.1453934105814335 + x3)^2 + (
    -0.8013757499531303 + x4)^2) + x77 * ((-0.00607035083945795 + x1)^2 + (
    -0.053561905123383324 + x2)^2 + (-0.7817703845300363 + x3)^2 + (
    -0.5662212686106933 + x4)^2) + x78 * ((-0.6950221994466669 + x1)^2 + (
    -0.2105034885347269 + x2)^2 + (-0.11287315442891777 + x3)^2 + (
    -0.010597472308638611 + x4)^2) + x79 * ((-0.5311582701895528 + x1)^2 + (
    -0.4320063664214896 + x2)^2 + (-0.2729049031820855 + x3)^2 + (
    -0.2214949427555688 + x4)^2) + x80 * ((-0.48150146533157034 + x1)^2 + (
    -0.46067276862424755 + x2)^2 + (-0.0056974073880511344 + x3)^2 + (
    -0.35728414461795144 + x4)^2) + x81 * ((-0.9429852300228826 + x1)^2 + (
    -0.39303494745904877 + x2)^2 + (-0.31011214177569657 + x3)^2 + (
    -0.018438339560493344 + x4)^2) + x82 * ((-0.5322977536893222 + x1)^2 + (
    -0.9652470893187132 + x2)^2 + (-0.21135139952422877 + x3)^2 + (
    -0.8156809600304314 + x4)^2) + x83 * ((-0.03401283459710902 + x1)^2 + (
    -0.806892267442106 + x2)^2 + (-0.8489758888126404 + x3)^2 + (
    -0.6111483840787582 + x4)^2) + x84 * ((-0.9264484533738693 + x1)^2 + (
    -0.14876976743207326 + x2)^2 + (-0.9758190264647324 + x3)^2 + (
    -0.6811285636971497 + x4)^2) + x85 * ((-0.9647303094099035 + x1)^2 + (
    -0.7010206460934956 + x2)^2 + (-0.30943177373448516 + x3)^2 + (
    -0.1891022383766483 + x4)^2) + x86 * ((-0.4769220240119476 + x1)^2 + (
    -0.822318413841706 + x2)^2 + (-0.1393694419930549 + x3)^2 + (
    -0.9724217562379036 + x4)^2) + x87 * ((-0.7455477334590928 + x1)^2 + (
    -0.563396428008588 + x2)^2 + (-0.22992430827076737 + x3)^2 + (
    -0.2370557772132338 + x4)^2) + x88 * ((-0.16535109726174313 + x1)^2 + (
    -0.9547852441919761 + x2)^2 + (-0.3203072223564828 + x3)^2 + (
    -0.42492616349386114 + x4)^2) + x89 * ((-0.7834231836651542 + x1)^2 + (
    -0.24935541853121224 + x2)^2 + (-0.8297208826099771 + x3)^2 + (
    -0.23563563513419228 + x4)^2) + x90 * ((-0.8373741924252092 + x1)^2 + (
    -0.36970144853956455 + x2)^2 + (-0.5671956111716981 + x3)^2 + (
    -0.3691960678174552 + x4)^2) + x91 * ((-0.39886787270583346 + x1)^2 + (
    -0.650964776918859 + x2)^2 + (-0.640819546256607 + x3)^2 + (
    -0.09882188475998765 + x4)^2) + x92 * ((-0.5157745663985024 + x1)^2 + (
    -0.5435336580091097 + x2)^2 + (-0.27430425498315725 + x3)^2 + (
    -0.7274939676197051 + x4)^2) + x93 * ((-0.537162865589002 + x1)^2 + (
    -0.5913784936821398 + x2)^2 + (-0.45466522772907525 + x3)^2 + (
    -0.1047184477665718 + x4)^2) + x94 * ((-0.04102323848681244 + x1)^2 + (
    -0.5377574929590462 + x2)^2 + (-0.9782258268406425 + x3)^2 + (
    -0.9716171817066379 + x4)^2) + x95 * ((-0.6871600172780726 + x1)^2 + (
    -0.8418720435526559 + x2)^2 + (-0.83052769064337 + x3)^2 + (
    -0.8985953589244926 + x4)^2) + x96 * ((-0.10160325017586314 + x1)^2 + (
    -0.8817097435158873 + x2)^2 + (-0.2972532110491476 + x3)^2 + (
    -0.34330327059943233 + x4)^2) + x97 * ((-0.276256004491218 + x1)^2 + (
    -0.9717101669718731 + x2)^2 + (-0.2984317666596268 + x3)^2 + (
    -0.4440796331949195 + x4)^2) + x98 * ((-0.9523516045369547 + x1)^2 + (
    -0.6811203295261851 + x2)^2 + (-0.17487173576269888 + x3)^2 + (
    -0.264608767198526 + x4)^2) + x99 * ((-0.5950072414516107 + x1)^2 + (
    -0.19863608495271834 + x2)^2 + (-0.3254107876389821 + x3)^2 + (
    -0.8432385372383167 + x4)^2) + x100 * ((-0.8468632268868022 + x1)^2 + (
    -0.07323866891200903 + x2)^2 + (-0.8068985989515749 + x3)^2 + (
    -0.6810798779677064 + x4)^2) + x101 * ((-0.4712188830735816 + x1)^2 + (
    -0.4135054120302819 + x2)^2 + (-0.3077078179033642 + x3)^2 + (
    -0.3353457462826305 + x4)^2) + x102 * ((-0.31701343040014285 + x1)^2 + (
    -0.6308301684094946 + x2)^2 + (-0.5476747635071102 + x3)^2 + (
    -0.26992487329332904 + x4)^2) + x103 * ((-0.19701342670354327 + x1)^2 + (
    -0.4781921949933534 + x2)^2 + (-0.7057141592764116 + x3)^2 + (
    -0.0896309852595556 + x4)^2) + x104 * ((-0.8038878371618275 + x1)^2 + (
    -0.044329635856571015 + x2)^2 + (-0.898513730220423 + x3)^2 + (
    -0.5600362942589316 + x4)^2) + x105 * ((-0.14961294077862985 + x1)^2 + (
    -0.9772469188459079 + x2)^2 + (-0.12015140801504265 + x3)^2 + (
    -0.521329056759319 + x4)^2) + x106 * ((-0.03381103052182122 + x1)^2 + (
    -0.527498561244566 + x2)^2 + (-0.44345060645273227 + x3)^2 + (
    -0.006260254814196675 + x4)^2) + x107 * ((-0.8219788276317623 + x1)^2 + (
    -0.3852922260631585 + x2)^2 + (-0.9620135163986219 + x3)^2 + (
    -0.18635183396741328 + x4)^2) + x108 * ((-0.7389415908359858 + x1)^2 + (
    -0.523761972701124 + x2)^2 + (-0.46623643584676433 + x3)^2 + (
    -0.0580789763043309 + x4)^2) + x109 * ((-0.5180391196124703 + x1)^2 + (
    -0.125977305519825 + x2)^2 + (-0.7141405174792315 + x3)^2 + (
    -0.6913703129848836 + x4)^2) + x110 * ((-0.26351088593273375 + x1)^2 + (
    -0.45761632800962093 + x2)^2 + (-0.7832055136876419 + x3)^2 + (
    -0.13621640940288493 + x4)^2) + x111 * ((-0.471522719293638 + x1)^2 + (
    -0.6233304917288576 + x2)^2 + (-0.9541794868794985 + x3)^2 + (
    -0.8015112028077606 + x4)^2) + x112 * ((-0.602523335859397 + x1)^2 + (
    -0.9632346106061206 + x2)^2 + (-0.9904964428766339 + x3)^2 + (
    -0.051156798506716616 + x4)^2) + x113 * ((-0.5884363239423929 + x1)^2 + (
    -0.9712278123715459 + x2)^2 + (-0.39988158182711386 + x3)^2 + (
    -0.41099930765106685 + x4)^2) + x114 * ((-0.5312213971906167 + x1)^2 + (
    -0.81785083419928 + x2)^2 + (-0.11725286157727799 + x3)^2 + (
    -0.47116385459902677 + x4)^2) + x115 * ((-0.9276992489134009 + x1)^2 + (
    -0.276293095414863 + x2)^2 + (-0.694461598585542 + x3)^2 + (
    -0.24661724253663275 + x4)^2) + x116 * ((-0.8984827464797928 + x1)^2 + (
    -0.8392110392495009 + x2)^2 + (-0.29003442507035804 + x3)^2 + (
    -0.7169574587131787 + x4)^2) + x117 * ((-0.7178579817600614 + x1)^2 + (
    -0.5442760502478915 + x2)^2 + (-0.3613660892547932 + x3)^2 + (
    -0.8887949357847075 + x4)^2) + x118 * ((-0.20832626177371294 + x1)^2 + (
    -0.6155556242775743 + x2)^2 + (-0.24252949041723848 + x3)^2 + (
    -0.5435125865130096 + x4)^2) + x119 * ((-0.6309807709209095 + x1)^2 + (
    -0.3784634566348025 + x2)^2 + (-0.39906901089542124 + x3)^2 + (
    -0.4255257271419496 + x4)^2) + x120 * ((-0.2531527659499414 + x1)^2 + (
    -0.3939338403635574 + x2)^2 + (-0.24367103431275294 + x3)^2 + (
    -0.09965076327279909 + x4)^2) + x121 * ((-0.4613429383834692 + x1)^2 + (
    -0.3270734410373959 + x2)^2 + (-0.3721913332914448 + x3)^2 + (
    -0.8397998489632109 + x4)^2) + x122 * ((-0.38125619155081125 + x1)^2 + (
    -0.38637355155860587 + x2)^2 + (-0.48242666628327 + x3)^2 + (
    -0.09841931704125129 + x4)^2) + x123 * ((-0.8312772318196014 + x1)^2 + (
    -0.8386805111720071 + x2)^2 + (-0.7116803614743081 + x3)^2 + (
    -0.1685702196156904 + x4)^2) + x124 * ((-0.9799547522897909 + x1)^2 + (
    -0.833448605810144 + x2)^2 + (-0.8740694081049383 + x3)^2 + (
    -0.6506828607108437 + x4)^2) + x125 * ((-0.1607430602427229 + x1)^2 + (
    -0.9407888153270746 + x2)^2 + (-0.6263933433327887 + x3)^2 + (
    -0.749780063323727 + x4)^2) + x126 * ((-0.7159349886520615 + x1)^2 + (
    -0.5782176711798136 + x2)^2 + (-0.2549127897200829 + x3)^2 + (
    -0.2942758616813056 + x4)^2) + x127 * ((-0.2937946995191628 + x1)^2 + (
    -0.7467755231646197 + x2)^2 + (-0.12056041976861509 + x3)^2 + (
    -0.6656163636347733 + x4)^2) + x128 * ((-0.1391657590641412 + x1)^2 + (
    -0.7998527624894191 + x2)^2 + (-0.8268662401101857 + x3)^2 + (
    -0.33882597292525984 + x4)^2) + x129 * ((-0.6582625122649799 + x5)^2 + (
    -0.10362896941145872 + x6)^2 + (-0.8195797598856802 + x7)^2 + (
    -0.5422289997742272 + x8)^2) + x130 * ((-0.3661207081728268 + x5)^2 + (
    -0.7480408210929997 + x6)^2 + (-0.6813605839850432 + x7)^2 + (
    -0.5056692315871436 + x8)^2) + x131 * ((-0.07046798157590661 + x5)^2 + (
    -0.5775220724425275 + x6)^2 + (-0.7916097196998284 + x7)^2 + (
    -0.9106301943747759 + x8)^2) + x132 * ((-0.9143624080891343 + x5)^2 + (
    -0.5102176451888726 + x6)^2 + (-0.46023708546130926 + x7)^2 + (
    -0.21559477969887786 + x8)^2) + x133 * ((-0.2152968191062874 + x5)^2 + (
    -0.40849216327387305 + x6)^2 + (-0.20734483145145233 + x7)^2 + (
    -0.29299530170003807 + x8)^2) + x134 * ((-0.753381482947803 + x5)^2 + (
    -0.569021356481719 + x6)^2 + (-0.825772931187451 + x7)^2 + (
    -0.6717803623991925 + x8)^2) + x135 * ((-0.22558272825834902 + x5)^2 + (
    -0.1431433457263549 + x6)^2 + (-0.36496670173321977 + x7)^2 + (
    -0.8283121504397382 + x8)^2) + x136 * ((-0.1043150551410561 + x5)^2 + (
    -0.5878900110989006 + x6)^2 + (-0.9303409193762857 + x7)^2 + (
    -0.1857245451574967 + x8)^2) + x137 * ((-0.2569777266497605 + x5)^2 + (
    -0.44043166993274085 + x6)^2 + (-0.15843257127556898 + x7)^2 + (
    -0.952596167014909 + x8)^2) + x138 * ((-0.767248128715498 + x5)^2 + (
    -0.16237189449331368 + x6)^2 + (-0.06342633508651152 + x7)^2 + (
    -0.8024171562438219 + x8)^2) + x139 * ((-0.7172302300642502 + x5)^2 + (
    -0.3391758201292703 + x6)^2 + (-0.030384935563099513 + x7)^2 + (
    -0.06493483472263029 + x8)^2) + x140 * ((-0.3661672203776154 + x5)^2 + (
    -0.9542180221871335 + x6)^2 + (-0.5308186536817474 + x7)^2 + (
    -0.16997124480838255 + x8)^2) + x141 * ((-0.23659736779603846 + x5)^2 + (
    -0.6214607353719023 + x6)^2 + (-0.3081993619295993 + x7)^2 + (
    -0.3526409606385007 + x8)^2) + x142 * ((-0.9752782586626233 + x5)^2 + (
    -0.5844650261883885 + x6)^2 + (-0.37649426913773276 + x7)^2 + (
    -0.10816991983567104 + x8)^2) + x143 * ((-0.45932686546602697 + x5)^2 + (
    -0.21233217626711853 + x6)^2 + (-0.9164032346567896 + x7)^2 + (
    -0.37108439943759797 + x8)^2) + x144 * ((-0.6867210427728082 + x5)^2 + (
    -0.7796854955112769 + x6)^2 + (-0.11982168093807799 + x7)^2 + (
    -0.6159743897209107 + x8)^2) + x145 * ((-0.985368764646874 + x5)^2 + (
    -0.07384180286280495 + x6)^2 + (-0.12212817800129094 + x7)^2 + (
    -0.2984771462799074 + x8)^2) + x146 * ((-0.7476106092305221 + x5)^2 + (
    -0.4411310968444404 + x6)^2 + (-0.5921500130284744 + x7)^2 + (
    -0.4842613828145912 + x8)^2) + x147 * ((-0.9737472353802095 + x5)^2 + (
    -0.09330122936543495 + x6)^2 + (-0.6050695157211611 + x7)^2 + (
    -0.07252152451660332 + x8)^2) + x148 * ((-0.09013540585240642 + x5)^2 + (
    -0.31276776356555547 + x6)^2 + (-0.7994057211441843 + x7)^2 + (
    -0.22689981649412638 + x8)^2) + x149 * ((-0.6283164056152335 + x5)^2 + (
    -0.3785737682752087 + x6)^2 + (-0.0024714258559164204 + x7)^2 + (
    -0.8148514253118784 + x8)^2) + x150 * ((-0.45370880893982724 + x5)^2 + (
    -0.10391203375848834 + x6)^2 + (-0.24027615267372093 + x7)^2 + (
    -0.2552645467206819 + x8)^2) + x151 * ((-0.4061008020592297 + x5)^2 + (
    -0.9396418294747921 + x6)^2 + (-0.5690658238794261 + x7)^2 + (
    -0.16866076993955403 + x8)^2) + x152 * ((-0.2314528417813161 + x5)^2 + (
    -0.5525474743329635 + x6)^2 + (-0.24649406583643063 + x7)^2 + (
    -0.9613520728571585 + x8)^2) + x153 * ((-0.5139605500157903 + x5)^2 + (
    -0.6815512588331698 + x6)^2 + (-0.16796296820903867 + x7)^2 + (
    -0.7162074865739461 + x8)^2) + x154 * ((-0.7706393889182662 + x5)^2 + (
    -0.43003110845525816 + x6)^2 + (-0.9356475551939986 + x7)^2 + (
    -0.5933795966331403 + x8)^2) + x155 * ((-0.5249118669899329 + x5)^2 + (
    -0.04056638284243541 + x6)^2 + (-0.0768970587722112 + x7)^2 + (
    -0.8247484594687006 + x8)^2) + x156 * ((-0.824923342468354 + x5)^2 + (
    -0.24405019701972253 + x6)^2 + (-0.38404505866575367 + x7)^2 + (
    -0.8313733189621139 + x8)^2) + x157 * ((-0.33950374022026997 + x5)^2 + (
    -0.5976095637618721 + x6)^2 + (-0.7602631636886854 + x7)^2 + (
    -0.4500249936588927 + x8)^2) + x158 * ((-0.523162910024812 + x5)^2 + (
    -0.3436248527141411 + x6)^2 + (-0.4561418310928951 + x7)^2 + (
    -0.8742103555752229 + x8)^2) + x159 * ((-0.3337530963427443 + x5)^2 + (
    -0.9855745242910374 + x6)^2 + (-0.9617621389771519 + x7)^2 + (
    -0.22441530334931115 + x8)^2) + x160 * ((-0.25477260253407985 + x5)^2 + (
    -0.3657617338278605 + x6)^2 + (-0.4599755066722203 + x7)^2 + (
    -0.488019659535353 + x8)^2) + x161 * ((-0.2663904007493795 + x5)^2 + (
    -0.27222258016843315 + x6)^2 + (-0.2880874179930988 + x7)^2 + (
    -0.02481848847156809 + x8)^2) + x162 * ((-0.2075297065152052 + x5)^2 + (
    -0.7022983060607665 + x6)^2 + (-0.47827086724608314 + x7)^2 + (
    -0.28622027057302846 + x8)^2) + x163 * ((-0.7047452543816871 + x5)^2 + (
    -0.6996554684275655 + x6)^2 + (-0.16578869005033847 + x7)^2 + (
    -0.5179151157105838 + x8)^2) + x164 * ((-0.7436571093571753 + x5)^2 + (
    -0.8723672259073825 + x6)^2 + (-0.9145540584909153 + x7)^2 + (
    -0.4616843537475913 + x8)^2) + x165 * ((-0.40078313938185106 + x5)^2 + (
    -0.7616315326378316 + x6)^2 + (-0.0624885237314553 + x7)^2 + (
    -0.33349386555475435 + x8)^2) + x166 * ((-0.47083964839087056 + x5)^2 + (
    -0.7540812887396847 + x6)^2 + (-0.7698437223374434 + x7)^2 + (
    -0.7260097297577066 + x8)^2) + x167 * ((-0.470591984548581 + x5)^2 + (
    -0.21419699662552538 + x6)^2 + (-0.8214784727628405 + x7)^2 + (
    -0.9327146275722538 + x8)^2) + x168 * ((-0.6694092237740207 + x5)^2 + (
    -0.40188436538160965 + x6)^2 + (-0.9078829021652501 + x7)^2 + (
    -0.28882880291122615 + x8)^2) + x169 * ((-0.8012821680592233 + x5)^2 + (
    -0.26764801084685064 + x6)^2 + (-0.8907563902239161 + x7)^2 + (
    -0.022670562427511642 + x8)^2) + x170 * ((-0.3149563708936517 + x5)^2 + (
    -0.4013573755930997 + x6)^2 + (-0.16444723142036033 + x7)^2 + (
    -0.8783064548569166 + x8)^2) + x171 * ((-0.0452536291694966 + x5)^2 + (
    -0.6030683870184952 + x6)^2 + (-0.12061018849928773 + x7)^2 + (
    -0.6161186728209969 + x8)^2) + x172 * ((-0.8303237648967787 + x5)^2 + (
    -0.7542211701244139 + x6)^2 + (-0.47189785643150806 + x7)^2 + (
    -0.7928252514256884 + x8)^2) + x173 * ((-0.6429343022480377 + x5)^2 + (
    -0.6021334537878723 + x6)^2 + (-0.2852218418361189 + x7)^2 + (
    -0.29825945641738283 + x8)^2) + x174 * ((-0.11776074988832852 + x5)^2 + (
    -0.8643957197110975 + x6)^2 + (-0.03338227312045139 + x7)^2 + (
    -0.593939114377175 + x8)^2) + x175 * ((-0.418497245301816 + x5)^2 + (
    -0.3081055339744846 + x6)^2 + (-0.38130196746434064 + x7)^2 + (
    -0.6612469720321472 + x8)^2) + x176 * ((-0.5815493986252239 + x5)^2 + (
    -0.6811102264085155 + x6)^2 + (-0.1453934105814335 + x7)^2 + (
    -0.8013757499531303 + x8)^2) + x177 * ((-0.00607035083945795 + x5)^2 + (
    -0.053561905123383324 + x6)^2 + (-0.7817703845300363 + x7)^2 + (
    -0.5662212686106933 + x8)^2) + x178 * ((-0.6950221994466669 + x5)^2 + (
    -0.2105034885347269 + x6)^2 + (-0.11287315442891777 + x7)^2 + (
    -0.010597472308638611 + x8)^2) + x179 * ((-0.5311582701895528 + x5)^2 + (
    -0.4320063664214896 + x6)^2 + (-0.2729049031820855 + x7)^2 + (
    -0.2214949427555688 + x8)^2) + x180 * ((-0.48150146533157034 + x5)^2 + (
    -0.46067276862424755 + x6)^2 + (-0.0056974073880511344 + x7)^2 + (
    -0.35728414461795144 + x8)^2) + x181 * ((-0.9429852300228826 + x5)^2 + (
    -0.39303494745904877 + x6)^2 + (-0.31011214177569657 + x7)^2 + (
    -0.018438339560493344 + x8)^2) + x182 * ((-0.5322977536893222 + x5)^2 + (
    -0.9652470893187132 + x6)^2 + (-0.21135139952422877 + x7)^2 + (
    -0.8156809600304314 + x8)^2) + x183 * ((-0.03401283459710902 + x5)^2 + (
    -0.806892267442106 + x6)^2 + (-0.8489758888126404 + x7)^2 + (
    -0.6111483840787582 + x8)^2) + x184 * ((-0.9264484533738693 + x5)^2 + (
    -0.14876976743207326 + x6)^2 + (-0.9758190264647324 + x7)^2 + (
    -0.6811285636971497 + x8)^2) + x185 * ((-0.9647303094099035 + x5)^2 + (
    -0.7010206460934956 + x6)^2 + (-0.30943177373448516 + x7)^2 + (
    -0.1891022383766483 + x8)^2) + x186 * ((-0.4769220240119476 + x5)^2 + (
    -0.822318413841706 + x6)^2 + (-0.1393694419930549 + x7)^2 + (
    -0.9724217562379036 + x8)^2) + x187 * ((-0.7455477334590928 + x5)^2 + (
    -0.563396428008588 + x6)^2 + (-0.22992430827076737 + x7)^2 + (
    -0.2370557772132338 + x8)^2) + x188 * ((-0.16535109726174313 + x5)^2 + (
    -0.9547852441919761 + x6)^2 + (-0.3203072223564828 + x7)^2 + (
    -0.42492616349386114 + x8)^2) + x189 * ((-0.7834231836651542 + x5)^2 + (
    -0.24935541853121224 + x6)^2 + (-0.8297208826099771 + x7)^2 + (
    -0.23563563513419228 + x8)^2) + x190 * ((-0.8373741924252092 + x5)^2 + (
    -0.36970144853956455 + x6)^2 + (-0.5671956111716981 + x7)^2 + (
    -0.3691960678174552 + x8)^2) + x191 * ((-0.39886787270583346 + x5)^2 + (
    -0.650964776918859 + x6)^2 + (-0.640819546256607 + x7)^2 + (
    -0.09882188475998765 + x8)^2) + x192 * ((-0.5157745663985024 + x5)^2 + (
    -0.5435336580091097 + x6)^2 + (-0.27430425498315725 + x7)^2 + (
    -0.7274939676197051 + x8)^2) + x193 * ((-0.537162865589002 + x5)^2 + (
    -0.5913784936821398 + x6)^2 + (-0.45466522772907525 + x7)^2 + (
    -0.1047184477665718 + x8)^2) + x194 * ((-0.04102323848681244 + x5)^2 + (
    -0.5377574929590462 + x6)^2 + (-0.9782258268406425 + x7)^2 + (
    -0.9716171817066379 + x8)^2) + x195 * ((-0.6871600172780726 + x5)^2 + (
    -0.8418720435526559 + x6)^2 + (-0.83052769064337 + x7)^2 + (
    -0.8985953589244926 + x8)^2) + x196 * ((-0.10160325017586314 + x5)^2 + (
    -0.8817097435158873 + x6)^2 + (-0.2972532110491476 + x7)^2 + (
    -0.34330327059943233 + x8)^2) + x197 * ((-0.276256004491218 + x5)^2 + (
    -0.9717101669718731 + x6)^2 + (-0.2984317666596268 + x7)^2 + (
    -0.4440796331949195 + x8)^2) + x198 * ((-0.9523516045369547 + x5)^2 + (
    -0.6811203295261851 + x6)^2 + (-0.17487173576269888 + x7)^2 + (
    -0.264608767198526 + x8)^2) + x199 * ((-0.5950072414516107 + x5)^2 + (
    -0.19863608495271834 + x6)^2 + (-0.3254107876389821 + x7)^2 + (
    -0.8432385372383167 + x8)^2) + x200 * ((-0.8468632268868022 + x5)^2 + (
    -0.07323866891200903 + x6)^2 + (-0.8068985989515749 + x7)^2 + (
    -0.6810798779677064 + x8)^2) + x201 * ((-0.4712188830735816 + x5)^2 + (
    -0.4135054120302819 + x6)^2 + (-0.3077078179033642 + x7)^2 + (
    -0.3353457462826305 + x8)^2) + x202 * ((-0.31701343040014285 + x5)^2 + (
    -0.6308301684094946 + x6)^2 + (-0.5476747635071102 + x7)^2 + (
    -0.26992487329332904 + x8)^2) + x203 * ((-0.19701342670354327 + x5)^2 + (
    -0.4781921949933534 + x6)^2 + (-0.7057141592764116 + x7)^2 + (
    -0.0896309852595556 + x8)^2) + x204 * ((-0.8038878371618275 + x5)^2 + (
    -0.044329635856571015 + x6)^2 + (-0.898513730220423 + x7)^2 + (
    -0.5600362942589316 + x8)^2) + x205 * ((-0.14961294077862985 + x5)^2 + (
    -0.9772469188459079 + x6)^2 + (-0.12015140801504265 + x7)^2 + (
    -0.521329056759319 + x8)^2) + x206 * ((-0.03381103052182122 + x5)^2 + (
    -0.527498561244566 + x6)^2 + (-0.44345060645273227 + x7)^2 + (
    -0.006260254814196675 + x8)^2) + x207 * ((-0.8219788276317623 + x5)^2 + (
    -0.3852922260631585 + x6)^2 + (-0.9620135163986219 + x7)^2 + (
    -0.18635183396741328 + x8)^2) + x208 * ((-0.7389415908359858 + x5)^2 + (
    -0.523761972701124 + x6)^2 + (-0.46623643584676433 + x7)^2 + (
    -0.0580789763043309 + x8)^2) + x209 * ((-0.5180391196124703 + x5)^2 + (
    -0.125977305519825 + x6)^2 + (-0.7141405174792315 + x7)^2 + (
    -0.6913703129848836 + x8)^2) + x210 * ((-0.26351088593273375 + x5)^2 + (
    -0.45761632800962093 + x6)^2 + (-0.7832055136876419 + x7)^2 + (
    -0.13621640940288493 + x8)^2) + x211 * ((-0.471522719293638 + x5)^2 + (
    -0.6233304917288576 + x6)^2 + (-0.9541794868794985 + x7)^2 + (
    -0.8015112028077606 + x8)^2) + x212 * ((-0.602523335859397 + x5)^2 + (
    -0.9632346106061206 + x6)^2 + (-0.9904964428766339 + x7)^2 + (
    -0.051156798506716616 + x8)^2) + x213 * ((-0.5884363239423929 + x5)^2 + (
    -0.9712278123715459 + x6)^2 + (-0.39988158182711386 + x7)^2 + (
    -0.41099930765106685 + x8)^2) + x214 * ((-0.5312213971906167 + x5)^2 + (
    -0.81785083419928 + x6)^2 + (-0.11725286157727799 + x7)^2 + (
    -0.47116385459902677 + x8)^2) + x215 * ((-0.9276992489134009 + x5)^2 + (
    -0.276293095414863 + x6)^2 + (-0.694461598585542 + x7)^2 + (
    -0.24661724253663275 + x8)^2) + x216 * ((-0.8984827464797928 + x5)^2 + (
    -0.8392110392495009 + x6)^2 + (-0.29003442507035804 + x7)^2 + (
    -0.7169574587131787 + x8)^2) + x217 * ((-0.7178579817600614 + x5)^2 + (
    -0.5442760502478915 + x6)^2 + (-0.3613660892547932 + x7)^2 + (
    -0.8887949357847075 + x8)^2) + x218 * ((-0.20832626177371294 + x5)^2 + (
    -0.6155556242775743 + x6)^2 + (-0.24252949041723848 + x7)^2 + (
    -0.5435125865130096 + x8)^2) + x219 * ((-0.6309807709209095 + x5)^2 + (
    -0.3784634566348025 + x6)^2 + (-0.39906901089542124 + x7)^2 + (
    -0.4255257271419496 + x8)^2) + x220 * ((-0.2531527659499414 + x5)^2 + (
    -0.3939338403635574 + x6)^2 + (-0.24367103431275294 + x7)^2 + (
    -0.09965076327279909 + x8)^2) + x221 * ((-0.4613429383834692 + x5)^2 + (
    -0.3270734410373959 + x6)^2 + (-0.3721913332914448 + x7)^2 + (
    -0.8397998489632109 + x8)^2) + x222 * ((-0.38125619155081125 + x5)^2 + (
    -0.38637355155860587 + x6)^2 + (-0.48242666628327 + x7)^2 + (
    -0.09841931704125129 + x8)^2) + x223 * ((-0.8312772318196014 + x5)^2 + (
    -0.8386805111720071 + x6)^2 + (-0.7116803614743081 + x7)^2 + (
    -0.1685702196156904 + x8)^2) + x224 * ((-0.9799547522897909 + x5)^2 + (
    -0.833448605810144 + x6)^2 + (-0.8740694081049383 + x7)^2 + (
    -0.6506828607108437 + x8)^2) + x225 * ((-0.1607430602427229 + x5)^2 + (
    -0.9407888153270746 + x6)^2 + (-0.6263933433327887 + x7)^2 + (
    -0.749780063323727 + x8)^2) + x226 * ((-0.7159349886520615 + x5)^2 + (
    -0.5782176711798136 + x6)^2 + (-0.2549127897200829 + x7)^2 + (
    -0.2942758616813056 + x8)^2) + x227 * ((-0.2937946995191628 + x5)^2 + (
    -0.7467755231646197 + x6)^2 + (-0.12056041976861509 + x7)^2 + (
    -0.6656163636347733 + x8)^2) + x228 * ((-0.1391657590641412 + x5)^2 + (
    -0.7998527624894191 + x6)^2 + (-0.8268662401101857 + x7)^2 + (
    -0.33882597292525984 + x8)^2) + x229 * ((-0.6582625122649799 + x9)^2 + (
    -0.10362896941145872 + x10)^2 + (-0.8195797598856802 + x11)^2 + (
    -0.5422289997742272 + x12)^2) + x230 * ((-0.3661207081728268 + x9)^2 + (
    -0.7480408210929997 + x10)^2 + (-0.6813605839850432 + x11)^2 + (
    -0.5056692315871436 + x12)^2) + x231 * ((-0.07046798157590661 + x9)^2 + (
    -0.5775220724425275 + x10)^2 + (-0.7916097196998284 + x11)^2 + (
    -0.9106301943747759 + x12)^2) + x232 * ((-0.9143624080891343 + x9)^2 + (
    -0.5102176451888726 + x10)^2 + (-0.46023708546130926 + x11)^2 + (
    -0.21559477969887786 + x12)^2) + x233 * ((-0.2152968191062874 + x9)^2 + (
    -0.40849216327387305 + x10)^2 + (-0.20734483145145233 + x11)^2 + (
    -0.29299530170003807 + x12)^2) + x234 * ((-0.753381482947803 + x9)^2 + (
    -0.569021356481719 + x10)^2 + (-0.825772931187451 + x11)^2 + (
    -0.6717803623991925 + x12)^2) + x235 * ((-0.22558272825834902 + x9)^2 + (
    -0.1431433457263549 + x10)^2 + (-0.36496670173321977 + x11)^2 + (
    -0.8283121504397382 + x12)^2) + x236 * ((-0.1043150551410561 + x9)^2 + (
    -0.5878900110989006 + x10)^2 + (-0.9303409193762857 + x11)^2 + (
    -0.1857245451574967 + x12)^2) + x237 * ((-0.2569777266497605 + x9)^2 + (
    -0.44043166993274085 + x10)^2 + (-0.15843257127556898 + x11)^2 + (
    -0.952596167014909 + x12)^2) + x238 * ((-0.767248128715498 + x9)^2 + (
    -0.16237189449331368 + x10)^2 + (-0.06342633508651152 + x11)^2 + (
    -0.8024171562438219 + x12)^2) + x239 * ((-0.7172302300642502 + x9)^2 + (
    -0.3391758201292703 + x10)^2 + (-0.030384935563099513 + x11)^2 + (
    -0.06493483472263029 + x12)^2) + x240 * ((-0.3661672203776154 + x9)^2 + (
    -0.9542180221871335 + x10)^2 + (-0.5308186536817474 + x11)^2 + (
    -0.16997124480838255 + x12)^2) + x241 * ((-0.23659736779603846 + x9)^2 + (
    -0.6214607353719023 + x10)^2 + (-0.3081993619295993 + x11)^2 + (
    -0.3526409606385007 + x12)^2) + x242 * ((-0.9752782586626233 + x9)^2 + (
    -0.5844650261883885 + x10)^2 + (-0.37649426913773276 + x11)^2 + (
    -0.10816991983567104 + x12)^2) + x243 * ((-0.45932686546602697 + x9)^2 + (
    -0.21233217626711853 + x10)^2 + (-0.9164032346567896 + x11)^2 + (
    -0.37108439943759797 + x12)^2) + x244 * ((-0.6867210427728082 + x9)^2 + (
    -0.7796854955112769 + x10)^2 + (-0.11982168093807799 + x11)^2 + (
    -0.6159743897209107 + x12)^2) + x245 * ((-0.985368764646874 + x9)^2 + (
    -0.07384180286280495 + x10)^2 + (-0.12212817800129094 + x11)^2 + (
    -0.2984771462799074 + x12)^2) + x246 * ((-0.7476106092305221 + x9)^2 + (
    -0.4411310968444404 + x10)^2 + (-0.5921500130284744 + x11)^2 + (
    -0.4842613828145912 + x12)^2) + x247 * ((-0.9737472353802095 + x9)^2 + (
    -0.09330122936543495 + x10)^2 + (-0.6050695157211611 + x11)^2 + (
    -0.07252152451660332 + x12)^2) + x248 * ((-0.09013540585240642 + x9)^2 + (
    -0.31276776356555547 + x10)^2 + (-0.7994057211441843 + x11)^2 + (
    -0.22689981649412638 + x12)^2) + x249 * ((-0.6283164056152335 + x9)^2 + (
    -0.3785737682752087 + x10)^2 + (-0.0024714258559164204 + x11)^2 + (
    -0.8148514253118784 + x12)^2) + x250 * ((-0.45370880893982724 + x9)^2 + (
    -0.10391203375848834 + x10)^2 + (-0.24027615267372093 + x11)^2 + (
    -0.2552645467206819 + x12)^2) + x251 * ((-0.4061008020592297 + x9)^2 + (
    -0.9396418294747921 + x10)^2 + (-0.5690658238794261 + x11)^2 + (
    -0.16866076993955403 + x12)^2) + x252 * ((-0.2314528417813161 + x9)^2 + (
    -0.5525474743329635 + x10)^2 + (-0.24649406583643063 + x11)^2 + (
    -0.9613520728571585 + x12)^2) + x253 * ((-0.5139605500157903 + x9)^2 + (
    -0.6815512588331698 + x10)^2 + (-0.16796296820903867 + x11)^2 + (
    -0.7162074865739461 + x12)^2) + x254 * ((-0.7706393889182662 + x9)^2 + (
    -0.43003110845525816 + x10)^2 + (-0.9356475551939986 + x11)^2 + (
    -0.5933795966331403 + x12)^2) + x255 * ((-0.5249118669899329 + x9)^2 + (
    -0.04056638284243541 + x10)^2 + (-0.0768970587722112 + x11)^2 + (
    -0.8247484594687006 + x12)^2) + x256 * ((-0.824923342468354 + x9)^2 + (
    -0.24405019701972253 + x10)^2 + (-0.38404505866575367 + x11)^2 + (
    -0.8313733189621139 + x12)^2) + x257 * ((-0.33950374022026997 + x9)^2 + (
    -0.5976095637618721 + x10)^2 + (-0.7602631636886854 + x11)^2 + (
    -0.4500249936588927 + x12)^2) + x258 * ((-0.523162910024812 + x9)^2 + (
    -0.3436248527141411 + x10)^2 + (-0.4561418310928951 + x11)^2 + (
    -0.8742103555752229 + x12)^2) + x259 * ((-0.3337530963427443 + x9)^2 + (
    -0.9855745242910374 + x10)^2 + (-0.9617621389771519 + x11)^2 + (
    -0.22441530334931115 + x12)^2) + x260 * ((-0.25477260253407985 + x9)^2 + (
    -0.3657617338278605 + x10)^2 + (-0.4599755066722203 + x11)^2 + (
    -0.488019659535353 + x12)^2) + x261 * ((-0.2663904007493795 + x9)^2 + (
    -0.27222258016843315 + x10)^2 + (-0.2880874179930988 + x11)^2 + (
    -0.02481848847156809 + x12)^2) + x262 * ((-0.2075297065152052 + x9)^2 + (
    -0.7022983060607665 + x10)^2 + (-0.47827086724608314 + x11)^2 + (
    -0.28622027057302846 + x12)^2) + x263 * ((-0.7047452543816871 + x9)^2 + (
    -0.6996554684275655 + x10)^2 + (-0.16578869005033847 + x11)^2 + (
    -0.5179151157105838 + x12)^2) + x264 * ((-0.7436571093571753 + x9)^2 + (
    -0.8723672259073825 + x10)^2 + (-0.9145540584909153 + x11)^2 + (
    -0.4616843537475913 + x12)^2) + x265 * ((-0.40078313938185106 + x9)^2 + (
    -0.7616315326378316 + x10)^2 + (-0.0624885237314553 + x11)^2 + (
    -0.33349386555475435 + x12)^2) + x266 * ((-0.47083964839087056 + x9)^2 + (
    -0.7540812887396847 + x10)^2 + (-0.7698437223374434 + x11)^2 + (
    -0.7260097297577066 + x12)^2) + x267 * ((-0.470591984548581 + x9)^2 + (
    -0.21419699662552538 + x10)^2 + (-0.8214784727628405 + x11)^2 + (
    -0.9327146275722538 + x12)^2) + x268 * ((-0.6694092237740207 + x9)^2 + (
    -0.40188436538160965 + x10)^2 + (-0.9078829021652501 + x11)^2 + (
    -0.28882880291122615 + x12)^2) + x269 * ((-0.8012821680592233 + x9)^2 + (
    -0.26764801084685064 + x10)^2 + (-0.8907563902239161 + x11)^2 + (
    -0.022670562427511642 + x12)^2) + x270 * ((-0.3149563708936517 + x9)^2 + (
    -0.4013573755930997 + x10)^2 + (-0.16444723142036033 + x11)^2 + (
    -0.8783064548569166 + x12)^2) + x271 * ((-0.0452536291694966 + x9)^2 + (
    -0.6030683870184952 + x10)^2 + (-0.12061018849928773 + x11)^2 + (
    -0.6161186728209969 + x12)^2) + x272 * ((-0.8303237648967787 + x9)^2 + (
    -0.7542211701244139 + x10)^2 + (-0.47189785643150806 + x11)^2 + (
    -0.7928252514256884 + x12)^2) + x273 * ((-0.6429343022480377 + x9)^2 + (
    -0.6021334537878723 + x10)^2 + (-0.2852218418361189 + x11)^2 + (
    -0.29825945641738283 + x12)^2) + x274 * ((-0.11776074988832852 + x9)^2 + (
    -0.8643957197110975 + x10)^2 + (-0.03338227312045139 + x11)^2 + (
    -0.593939114377175 + x12)^2) + x275 * ((-0.418497245301816 + x9)^2 + (
    -0.3081055339744846 + x10)^2 + (-0.38130196746434064 + x11)^2 + (
    -0.6612469720321472 + x12)^2) + x276 * ((-0.5815493986252239 + x9)^2 + (
    -0.6811102264085155 + x10)^2 + (-0.1453934105814335 + x11)^2 + (
    -0.8013757499531303 + x12)^2) + x277 * ((-0.00607035083945795 + x9)^2 + (
    -0.053561905123383324 + x10)^2 + (-0.7817703845300363 + x11)^2 + (
    -0.5662212686106933 + x12)^2) + x278 * ((-0.6950221994466669 + x9)^2 + (
    -0.2105034885347269 + x10)^2 + (-0.11287315442891777 + x11)^2 + (
    -0.010597472308638611 + x12)^2) + x279 * ((-0.5311582701895528 + x9)^2 + (
    -0.4320063664214896 + x10)^2 + (-0.2729049031820855 + x11)^2 + (
    -0.2214949427555688 + x12)^2) + x280 * ((-0.48150146533157034 + x9)^2 + (
    -0.46067276862424755 + x10)^2 + (-0.0056974073880511344 + x11)^2 + (
    -0.35728414461795144 + x12)^2) + x281 * ((-0.9429852300228826 + x9)^2 + (
    -0.39303494745904877 + x10)^2 + (-0.31011214177569657 + x11)^2 + (
    -0.018438339560493344 + x12)^2) + x282 * ((-0.5322977536893222 + x9)^2 + (
    -0.9652470893187132 + x10)^2 + (-0.21135139952422877 + x11)^2 + (
    -0.8156809600304314 + x12)^2) + x283 * ((-0.03401283459710902 + x9)^2 + (
    -0.806892267442106 + x10)^2 + (-0.8489758888126404 + x11)^2 + (
    -0.6111483840787582 + x12)^2) + x284 * ((-0.9264484533738693 + x9)^2 + (
    -0.14876976743207326 + x10)^2 + (-0.9758190264647324 + x11)^2 + (
    -0.6811285636971497 + x12)^2) + x285 * ((-0.9647303094099035 + x9)^2 + (
    -0.7010206460934956 + x10)^2 + (-0.30943177373448516 + x11)^2 + (
    -0.1891022383766483 + x12)^2) + x286 * ((-0.4769220240119476 + x9)^2 + (
    -0.822318413841706 + x10)^2 + (-0.1393694419930549 + x11)^2 + (
    -0.9724217562379036 + x12)^2) + x287 * ((-0.7455477334590928 + x9)^2 + (
    -0.563396428008588 + x10)^2 + (-0.22992430827076737 + x11)^2 + (
    -0.2370557772132338 + x12)^2) + x288 * ((-0.16535109726174313 + x9)^2 + (
    -0.9547852441919761 + x10)^2 + (-0.3203072223564828 + x11)^2 + (
    -0.42492616349386114 + x12)^2) + x289 * ((-0.7834231836651542 + x9)^2 + (
    -0.24935541853121224 + x10)^2 + (-0.8297208826099771 + x11)^2 + (
    -0.23563563513419228 + x12)^2) + x290 * ((-0.8373741924252092 + x9)^2 + (
    -0.36970144853956455 + x10)^2 + (-0.5671956111716981 + x11)^2 + (
    -0.3691960678174552 + x12)^2) + x291 * ((-0.39886787270583346 + x9)^2 + (
    -0.650964776918859 + x10)^2 + (-0.640819546256607 + x11)^2 + (
    -0.09882188475998765 + x12)^2) + x292 * ((-0.5157745663985024 + x9)^2 + (
    -0.5435336580091097 + x10)^2 + (-0.27430425498315725 + x11)^2 + (
    -0.7274939676197051 + x12)^2) + x293 * ((-0.537162865589002 + x9)^2 + (
    -0.5913784936821398 + x10)^2 + (-0.45466522772907525 + x11)^2 + (
    -0.1047184477665718 + x12)^2) + x294 * ((-0.04102323848681244 + x9)^2 + (
    -0.5377574929590462 + x10)^2 + (-0.9782258268406425 + x11)^2 + (
    -0.9716171817066379 + x12)^2) + x295 * ((-0.6871600172780726 + x9)^2 + (
    -0.8418720435526559 + x10)^2 + (-0.83052769064337 + x11)^2 + (
    -0.8985953589244926 + x12)^2) + x296 * ((-0.10160325017586314 + x9)^2 + (
    -0.8817097435158873 + x10)^2 + (-0.2972532110491476 + x11)^2 + (
    -0.34330327059943233 + x12)^2) + x297 * ((-0.276256004491218 + x9)^2 + (
    -0.9717101669718731 + x10)^2 + (-0.2984317666596268 + x11)^2 + (
    -0.4440796331949195 + x12)^2) + x298 * ((-0.9523516045369547 + x9)^2 + (
    -0.6811203295261851 + x10)^2 + (-0.17487173576269888 + x11)^2 + (
    -0.264608767198526 + x12)^2) + x299 * ((-0.5950072414516107 + x9)^2 + (
    -0.19863608495271834 + x10)^2 + (-0.3254107876389821 + x11)^2 + (
    -0.8432385372383167 + x12)^2) + x300 * ((-0.8468632268868022 + x9)^2 + (
    -0.07323866891200903 + x10)^2 + (-0.8068985989515749 + x11)^2 + (
    -0.6810798779677064 + x12)^2) + x301 * ((-0.4712188830735816 + x9)^2 + (
    -0.4135054120302819 + x10)^2 + (-0.3077078179033642 + x11)^2 + (
    -0.3353457462826305 + x12)^2) + x302 * ((-0.31701343040014285 + x9)^2 + (
    -0.6308301684094946 + x10)^2 + (-0.5476747635071102 + x11)^2 + (
    -0.26992487329332904 + x12)^2) + x303 * ((-0.19701342670354327 + x9)^2 + (
    -0.4781921949933534 + x10)^2 + (-0.7057141592764116 + x11)^2 + (
    -0.0896309852595556 + x12)^2) + x304 * ((-0.8038878371618275 + x9)^2 + (
    -0.044329635856571015 + x10)^2 + (-0.898513730220423 + x11)^2 + (
    -0.5600362942589316 + x12)^2) + x305 * ((-0.14961294077862985 + x9)^2 + (
    -0.9772469188459079 + x10)^2 + (-0.12015140801504265 + x11)^2 + (
    -0.521329056759319 + x12)^2) + x306 * ((-0.03381103052182122 + x9)^2 + (
    -0.527498561244566 + x10)^2 + (-0.44345060645273227 + x11)^2 + (
    -0.006260254814196675 + x12)^2) + x307 * ((-0.8219788276317623 + x9)^2 + (
    -0.3852922260631585 + x10)^2 + (-0.9620135163986219 + x11)^2 + (
    -0.18635183396741328 + x12)^2) + x308 * ((-0.7389415908359858 + x9)^2 + (
    -0.523761972701124 + x10)^2 + (-0.46623643584676433 + x11)^2 + (
    -0.0580789763043309 + x12)^2) + x309 * ((-0.5180391196124703 + x9)^2 + (
    -0.125977305519825 + x10)^2 + (-0.7141405174792315 + x11)^2 + (
    -0.6913703129848836 + x12)^2) + x310 * ((-0.26351088593273375 + x9)^2 + (
    -0.45761632800962093 + x10)^2 + (-0.7832055136876419 + x11)^2 + (
    -0.13621640940288493 + x12)^2) + x311 * ((-0.471522719293638 + x9)^2 + (
    -0.6233304917288576 + x10)^2 + (-0.9541794868794985 + x11)^2 + (
    -0.8015112028077606 + x12)^2) + x312 * ((-0.602523335859397 + x9)^2 + (
    -0.9632346106061206 + x10)^2 + (-0.9904964428766339 + x11)^2 + (
    -0.051156798506716616 + x12)^2) + x313 * ((-0.5884363239423929 + x9)^2 + (
    -0.9712278123715459 + x10)^2 + (-0.39988158182711386 + x11)^2 + (
    -0.41099930765106685 + x12)^2) + x314 * ((-0.5312213971906167 + x9)^2 + (
    -0.81785083419928 + x10)^2 + (-0.11725286157727799 + x11)^2 + (
    -0.47116385459902677 + x12)^2) + x315 * ((-0.9276992489134009 + x9)^2 + (
    -0.276293095414863 + x10)^2 + (-0.694461598585542 + x11)^2 + (
    -0.24661724253663275 + x12)^2) + x316 * ((-0.8984827464797928 + x9)^2 + (
    -0.8392110392495009 + x10)^2 + (-0.29003442507035804 + x11)^2 + (
    -0.7169574587131787 + x12)^2) + x317 * ((-0.7178579817600614 + x9)^2 + (
    -0.5442760502478915 + x10)^2 + (-0.3613660892547932 + x11)^2 + (
    -0.8887949357847075 + x12)^2) + x318 * ((-0.20832626177371294 + x9)^2 + (
    -0.6155556242775743 + x10)^2 + (-0.24252949041723848 + x11)^2 + (
    -0.5435125865130096 + x12)^2) + x319 * ((-0.6309807709209095 + x9)^2 + (
    -0.3784634566348025 + x10)^2 + (-0.39906901089542124 + x11)^2 + (
    -0.4255257271419496 + x12)^2) + x320 * ((-0.2531527659499414 + x9)^2 + (
    -0.3939338403635574 + x10)^2 + (-0.24367103431275294 + x11)^2 + (
    -0.09965076327279909 + x12)^2) + x321 * ((-0.4613429383834692 + x9)^2 + (
    -0.3270734410373959 + x10)^2 + (-0.3721913332914448 + x11)^2 + (
    -0.8397998489632109 + x12)^2) + x322 * ((-0.38125619155081125 + x9)^2 + (
    -0.38637355155860587 + x10)^2 + (-0.48242666628327 + x11)^2 + (
    -0.09841931704125129 + x12)^2) + x323 * ((-0.8312772318196014 + x9)^2 + (
    -0.8386805111720071 + x10)^2 + (-0.7116803614743081 + x11)^2 + (
    -0.1685702196156904 + x12)^2) + x324 * ((-0.9799547522897909 + x9)^2 + (
    -0.833448605810144 + x10)^2 + (-0.8740694081049383 + x11)^2 + (
    -0.6506828607108437 + x12)^2) + x325 * ((-0.1607430602427229 + x9)^2 + (
    -0.9407888153270746 + x10)^2 + (-0.6263933433327887 + x11)^2 + (
    -0.749780063323727 + x12)^2) + x326 * ((-0.7159349886520615 + x9)^2 + (
    -0.5782176711798136 + x10)^2 + (-0.2549127897200829 + x11)^2 + (
    -0.2942758616813056 + x12)^2) + x327 * ((-0.2937946995191628 + x9)^2 + (
    -0.7467755231646197 + x10)^2 + (-0.12056041976861509 + x11)^2 + (
    -0.6656163636347733 + x12)^2) + x328 * ((-0.1391657590641412 + x9)^2 + (
    -0.7998527624894191 + x10)^2 + (-0.8268662401101857 + x11)^2 + (
    -0.33882597292525984 + x12)^2) + x329 * ((-0.6582625122649799 + x13)^2 + (
    -0.10362896941145872 + x14)^2 + (-0.8195797598856802 + x15)^2 + (
    -0.5422289997742272 + x16)^2) + x330 * ((-0.3661207081728268 + x13)^2 + (
    -0.7480408210929997 + x14)^2 + (-0.6813605839850432 + x15)^2 + (
    -0.5056692315871436 + x16)^2) + x331 * ((-0.07046798157590661 + x13)^2 + (
    -0.5775220724425275 + x14)^2 + (-0.7916097196998284 + x15)^2 + (
    -0.9106301943747759 + x16)^2) + x332 * ((-0.9143624080891343 + x13)^2 + (
    -0.5102176451888726 + x14)^2 + (-0.46023708546130926 + x15)^2 + (
    -0.21559477969887786 + x16)^2) + x333 * ((-0.2152968191062874 + x13)^2 + (
    -0.40849216327387305 + x14)^2 + (-0.20734483145145233 + x15)^2 + (
    -0.29299530170003807 + x16)^2) + x334 * ((-0.753381482947803 + x13)^2 + (
    -0.569021356481719 + x14)^2 + (-0.825772931187451 + x15)^2 + (
    -0.6717803623991925 + x16)^2) + x335 * ((-0.22558272825834902 + x13)^2 + (
    -0.1431433457263549 + x14)^2 + (-0.36496670173321977 + x15)^2 + (
    -0.8283121504397382 + x16)^2) + x336 * ((-0.1043150551410561 + x13)^2 + (
    -0.5878900110989006 + x14)^2 + (-0.9303409193762857 + x15)^2 + (
    -0.1857245451574967 + x16)^2) + x337 * ((-0.2569777266497605 + x13)^2 + (
    -0.44043166993274085 + x14)^2 + (-0.15843257127556898 + x15)^2 + (
    -0.952596167014909 + x16)^2) + x338 * ((-0.767248128715498 + x13)^2 + (
    -0.16237189449331368 + x14)^2 + (-0.06342633508651152 + x15)^2 + (
    -0.8024171562438219 + x16)^2) + x339 * ((-0.7172302300642502 + x13)^2 + (
    -0.3391758201292703 + x14)^2 + (-0.030384935563099513 + x15)^2 + (
    -0.06493483472263029 + x16)^2) + x340 * ((-0.3661672203776154 + x13)^2 + (
    -0.9542180221871335 + x14)^2 + (-0.5308186536817474 + x15)^2 + (
    -0.16997124480838255 + x16)^2) + x341 * ((-0.23659736779603846 + x13)^2 + (
    -0.6214607353719023 + x14)^2 + (-0.3081993619295993 + x15)^2 + (
    -0.3526409606385007 + x16)^2) + x342 * ((-0.9752782586626233 + x13)^2 + (
    -0.5844650261883885 + x14)^2 + (-0.37649426913773276 + x15)^2 + (
    -0.10816991983567104 + x16)^2) + x343 * ((-0.45932686546602697 + x13)^2 + (
    -0.21233217626711853 + x14)^2 + (-0.9164032346567896 + x15)^2 + (
    -0.37108439943759797 + x16)^2) + x344 * ((-0.6867210427728082 + x13)^2 + (
    -0.7796854955112769 + x14)^2 + (-0.11982168093807799 + x15)^2 + (
    -0.6159743897209107 + x16)^2) + x345 * ((-0.985368764646874 + x13)^2 + (
    -0.07384180286280495 + x14)^2 + (-0.12212817800129094 + x15)^2 + (
    -0.2984771462799074 + x16)^2) + x346 * ((-0.7476106092305221 + x13)^2 + (
    -0.4411310968444404 + x14)^2 + (-0.5921500130284744 + x15)^2 + (
    -0.4842613828145912 + x16)^2) + x347 * ((-0.9737472353802095 + x13)^2 + (
    -0.09330122936543495 + x14)^2 + (-0.6050695157211611 + x15)^2 + (
    -0.07252152451660332 + x16)^2) + x348 * ((-0.09013540585240642 + x13)^2 + (
    -0.31276776356555547 + x14)^2 + (-0.7994057211441843 + x15)^2 + (
    -0.22689981649412638 + x16)^2) + x349 * ((-0.6283164056152335 + x13)^2 + (
    -0.3785737682752087 + x14)^2 + (-0.0024714258559164204 + x15)^2 + (
    -0.8148514253118784 + x16)^2) + x350 * ((-0.45370880893982724 + x13)^2 + (
    -0.10391203375848834 + x14)^2 + (-0.24027615267372093 + x15)^2 + (
    -0.2552645467206819 + x16)^2) + x351 * ((-0.4061008020592297 + x13)^2 + (
    -0.9396418294747921 + x14)^2 + (-0.5690658238794261 + x15)^2 + (
    -0.16866076993955403 + x16)^2) + x352 * ((-0.2314528417813161 + x13)^2 + (
    -0.5525474743329635 + x14)^2 + (-0.24649406583643063 + x15)^2 + (
    -0.9613520728571585 + x16)^2) + x353 * ((-0.5139605500157903 + x13)^2 + (
    -0.6815512588331698 + x14)^2 + (-0.16796296820903867 + x15)^2 + (
    -0.7162074865739461 + x16)^2) + x354 * ((-0.7706393889182662 + x13)^2 + (
    -0.43003110845525816 + x14)^2 + (-0.9356475551939986 + x15)^2 + (
    -0.5933795966331403 + x16)^2) + x355 * ((-0.5249118669899329 + x13)^2 + (
    -0.04056638284243541 + x14)^2 + (-0.0768970587722112 + x15)^2 + (
    -0.8247484594687006 + x16)^2) + x356 * ((-0.824923342468354 + x13)^2 + (
    -0.24405019701972253 + x14)^2 + (-0.38404505866575367 + x15)^2 + (
    -0.8313733189621139 + x16)^2) + x357 * ((-0.33950374022026997 + x13)^2 + (
    -0.5976095637618721 + x14)^2 + (-0.7602631636886854 + x15)^2 + (
    -0.4500249936588927 + x16)^2) + x358 * ((-0.523162910024812 + x13)^2 + (
    -0.3436248527141411 + x14)^2 + (-0.4561418310928951 + x15)^2 + (
    -0.8742103555752229 + x16)^2) + x359 * ((-0.3337530963427443 + x13)^2 + (
    -0.9855745242910374 + x14)^2 + (-0.9617621389771519 + x15)^2 + (
    -0.22441530334931115 + x16)^2) + x360 * ((-0.25477260253407985 + x13)^2 + (
    -0.3657617338278605 + x14)^2 + (-0.4599755066722203 + x15)^2 + (
    -0.488019659535353 + x16)^2) + x361 * ((-0.2663904007493795 + x13)^2 + (
    -0.27222258016843315 + x14)^2 + (-0.2880874179930988 + x15)^2 + (
    -0.02481848847156809 + x16)^2) + x362 * ((-0.2075297065152052 + x13)^2 + (
    -0.7022983060607665 + x14)^2 + (-0.47827086724608314 + x15)^2 + (
    -0.28622027057302846 + x16)^2) + x363 * ((-0.7047452543816871 + x13)^2 + (
    -0.6996554684275655 + x14)^2 + (-0.16578869005033847 + x15)^2 + (
    -0.5179151157105838 + x16)^2) + x364 * ((-0.7436571093571753 + x13)^2 + (
    -0.8723672259073825 + x14)^2 + (-0.9145540584909153 + x15)^2 + (
    -0.4616843537475913 + x16)^2) + x365 * ((-0.40078313938185106 + x13)^2 + (
    -0.7616315326378316 + x14)^2 + (-0.0624885237314553 + x15)^2 + (
    -0.33349386555475435 + x16)^2) + x366 * ((-0.47083964839087056 + x13)^2 + (
    -0.7540812887396847 + x14)^2 + (-0.7698437223374434 + x15)^2 + (
    -0.7260097297577066 + x16)^2) + x367 * ((-0.470591984548581 + x13)^2 + (
    -0.21419699662552538 + x14)^2 + (-0.8214784727628405 + x15)^2 + (
    -0.9327146275722538 + x16)^2) + x368 * ((-0.6694092237740207 + x13)^2 + (
    -0.40188436538160965 + x14)^2 + (-0.9078829021652501 + x15)^2 + (
    -0.28882880291122615 + x16)^2) + x369 * ((-0.8012821680592233 + x13)^2 + (
    -0.26764801084685064 + x14)^2 + (-0.8907563902239161 + x15)^2 + (
    -0.022670562427511642 + x16)^2) + x370 * ((-0.3149563708936517 + x13)^2 + (
    -0.4013573755930997 + x14)^2 + (-0.16444723142036033 + x15)^2 + (
    -0.8783064548569166 + x16)^2) + x371 * ((-0.0452536291694966 + x13)^2 + (
    -0.6030683870184952 + x14)^2 + (-0.12061018849928773 + x15)^2 + (
    -0.6161186728209969 + x16)^2) + x372 * ((-0.8303237648967787 + x13)^2 + (
    -0.7542211701244139 + x14)^2 + (-0.47189785643150806 + x15)^2 + (
    -0.7928252514256884 + x16)^2) + x373 * ((-0.6429343022480377 + x13)^2 + (
    -0.6021334537878723 + x14)^2 + (-0.2852218418361189 + x15)^2 + (
    -0.29825945641738283 + x16)^2) + x374 * ((-0.11776074988832852 + x13)^2 + (
    -0.8643957197110975 + x14)^2 + (-0.03338227312045139 + x15)^2 + (
    -0.593939114377175 + x16)^2) + x375 * ((-0.418497245301816 + x13)^2 + (
    -0.3081055339744846 + x14)^2 + (-0.38130196746434064 + x15)^2 + (
    -0.6612469720321472 + x16)^2) + x376 * ((-0.5815493986252239 + x13)^2 + (
    -0.6811102264085155 + x14)^2 + (-0.1453934105814335 + x15)^2 + (
    -0.8013757499531303 + x16)^2) + x377 * ((-0.00607035083945795 + x13)^2 + (
    -0.053561905123383324 + x14)^2 + (-0.7817703845300363 + x15)^2 + (
    -0.5662212686106933 + x16)^2) + x378 * ((-0.6950221994466669 + x13)^2 + (
    -0.2105034885347269 + x14)^2 + (-0.11287315442891777 + x15)^2 + (
    -0.010597472308638611 + x16)^2) + x379 * ((-0.5311582701895528 + x13)^2 + (
    -0.4320063664214896 + x14)^2 + (-0.2729049031820855 + x15)^2 + (
    -0.2214949427555688 + x16)^2) + x380 * ((-0.48150146533157034 + x13)^2 + (
    -0.46067276862424755 + x14)^2 + (-0.0056974073880511344 + x15)^2 + (
    -0.35728414461795144 + x16)^2) + x381 * ((-0.9429852300228826 + x13)^2 + (
    -0.39303494745904877 + x14)^2 + (-0.31011214177569657 + x15)^2 + (
    -0.018438339560493344 + x16)^2) + x382 * ((-0.5322977536893222 + x13)^2 + (
    -0.9652470893187132 + x14)^2 + (-0.21135139952422877 + x15)^2 + (
    -0.8156809600304314 + x16)^2) + x383 * ((-0.03401283459710902 + x13)^2 + (
    -0.806892267442106 + x14)^2 + (-0.8489758888126404 + x15)^2 + (
    -0.6111483840787582 + x16)^2) + x384 * ((-0.9264484533738693 + x13)^2 + (
    -0.14876976743207326 + x14)^2 + (-0.9758190264647324 + x15)^2 + (
    -0.6811285636971497 + x16)^2) + x385 * ((-0.9647303094099035 + x13)^2 + (
    -0.7010206460934956 + x14)^2 + (-0.30943177373448516 + x15)^2 + (
    -0.1891022383766483 + x16)^2) + x386 * ((-0.4769220240119476 + x13)^2 + (
    -0.822318413841706 + x14)^2 + (-0.1393694419930549 + x15)^2 + (
    -0.9724217562379036 + x16)^2) + x387 * ((-0.7455477334590928 + x13)^2 + (
    -0.563396428008588 + x14)^2 + (-0.22992430827076737 + x15)^2 + (
    -0.2370557772132338 + x16)^2) + x388 * ((-0.16535109726174313 + x13)^2 + (
    -0.9547852441919761 + x14)^2 + (-0.3203072223564828 + x15)^2 + (
    -0.42492616349386114 + x16)^2) + x389 * ((-0.7834231836651542 + x13)^2 + (
    -0.24935541853121224 + x14)^2 + (-0.8297208826099771 + x15)^2 + (
    -0.23563563513419228 + x16)^2) + x390 * ((-0.8373741924252092 + x13)^2 + (
    -0.36970144853956455 + x14)^2 + (-0.5671956111716981 + x15)^2 + (
    -0.3691960678174552 + x16)^2) + x391 * ((-0.39886787270583346 + x13)^2 + (
    -0.650964776918859 + x14)^2 + (-0.640819546256607 + x15)^2 + (
    -0.09882188475998765 + x16)^2) + x392 * ((-0.5157745663985024 + x13)^2 + (
    -0.5435336580091097 + x14)^2 + (-0.27430425498315725 + x15)^2 + (
    -0.7274939676197051 + x16)^2) + x393 * ((-0.537162865589002 + x13)^2 + (
    -0.5913784936821398 + x14)^2 + (-0.45466522772907525 + x15)^2 + (
    -0.1047184477665718 + x16)^2) + x394 * ((-0.04102323848681244 + x13)^2 + (
    -0.5377574929590462 + x14)^2 + (-0.9782258268406425 + x15)^2 + (
    -0.9716171817066379 + x16)^2) + x395 * ((-0.6871600172780726 + x13)^2 + (
    -0.8418720435526559 + x14)^2 + (-0.83052769064337 + x15)^2 + (
    -0.8985953589244926 + x16)^2) + x396 * ((-0.10160325017586314 + x13)^2 + (
    -0.8817097435158873 + x14)^2 + (-0.2972532110491476 + x15)^2 + (
    -0.34330327059943233 + x16)^2) + x397 * ((-0.276256004491218 + x13)^2 + (
    -0.9717101669718731 + x14)^2 + (-0.2984317666596268 + x15)^2 + (
    -0.4440796331949195 + x16)^2) + x398 * ((-0.9523516045369547 + x13)^2 + (
    -0.6811203295261851 + x14)^2 + (-0.17487173576269888 + x15)^2 + (
    -0.264608767198526 + x16)^2) + x399 * ((-0.5950072414516107 + x13)^2 + (
    -0.19863608495271834 + x14)^2 + (-0.3254107876389821 + x15)^2 + (
    -0.8432385372383167 + x16)^2) + x400 * ((-0.8468632268868022 + x13)^2 + (
    -0.07323866891200903 + x14)^2 + (-0.8068985989515749 + x15)^2 + (
    -0.6810798779677064 + x16)^2) + x401 * ((-0.4712188830735816 + x13)^2 + (
    -0.4135054120302819 + x14)^2 + (-0.3077078179033642 + x15)^2 + (
    -0.3353457462826305 + x16)^2) + x402 * ((-0.31701343040014285 + x13)^2 + (
    -0.6308301684094946 + x14)^2 + (-0.5476747635071102 + x15)^2 + (
    -0.26992487329332904 + x16)^2) + x403 * ((-0.19701342670354327 + x13)^2 + (
    -0.4781921949933534 + x14)^2 + (-0.7057141592764116 + x15)^2 + (
    -0.0896309852595556 + x16)^2) + x404 * ((-0.8038878371618275 + x13)^2 + (
    -0.044329635856571015 + x14)^2 + (-0.898513730220423 + x15)^2 + (
    -0.5600362942589316 + x16)^2) + x405 * ((-0.14961294077862985 + x13)^2 + (
    -0.9772469188459079 + x14)^2 + (-0.12015140801504265 + x15)^2 + (
    -0.521329056759319 + x16)^2) + x406 * ((-0.03381103052182122 + x13)^2 + (
    -0.527498561244566 + x14)^2 + (-0.44345060645273227 + x15)^2 + (
    -0.006260254814196675 + x16)^2) + x407 * ((-0.8219788276317623 + x13)^2 + (
    -0.3852922260631585 + x14)^2 + (-0.9620135163986219 + x15)^2 + (
    -0.18635183396741328 + x16)^2) + x408 * ((-0.7389415908359858 + x13)^2 + (
    -0.523761972701124 + x14)^2 + (-0.46623643584676433 + x15)^2 + (
    -0.0580789763043309 + x16)^2) + x409 * ((-0.5180391196124703 + x13)^2 + (
    -0.125977305519825 + x14)^2 + (-0.7141405174792315 + x15)^2 + (
    -0.6913703129848836 + x16)^2) + x410 * ((-0.26351088593273375 + x13)^2 + (
    -0.45761632800962093 + x14)^2 + (-0.7832055136876419 + x15)^2 + (
    -0.13621640940288493 + x16)^2) + x411 * ((-0.471522719293638 + x13)^2 + (
    -0.6233304917288576 + x14)^2 + (-0.9541794868794985 + x15)^2 + (
    -0.8015112028077606 + x16)^2) + x412 * ((-0.602523335859397 + x13)^2 + (
    -0.9632346106061206 + x14)^2 + (-0.9904964428766339 + x15)^2 + (
    -0.051156798506716616 + x16)^2) + x413 * ((-0.5884363239423929 + x13)^2 + (
    -0.9712278123715459 + x14)^2 + (-0.39988158182711386 + x15)^2 + (
    -0.41099930765106685 + x16)^2) + x414 * ((-0.5312213971906167 + x13)^2 + (
    -0.81785083419928 + x14)^2 + (-0.11725286157727799 + x15)^2 + (
    -0.47116385459902677 + x16)^2) + x415 * ((-0.9276992489134009 + x13)^2 + (
    -0.276293095414863 + x14)^2 + (-0.694461598585542 + x15)^2 + (
    -0.24661724253663275 + x16)^2) + x416 * ((-0.8984827464797928 + x13)^2 + (
    -0.8392110392495009 + x14)^2 + (-0.29003442507035804 + x15)^2 + (
    -0.7169574587131787 + x16)^2) + x417 * ((-0.7178579817600614 + x13)^2 + (
    -0.5442760502478915 + x14)^2 + (-0.3613660892547932 + x15)^2 + (
    -0.8887949357847075 + x16)^2) + x418 * ((-0.20832626177371294 + x13)^2 + (
    -0.6155556242775743 + x14)^2 + (-0.24252949041723848 + x15)^2 + (
    -0.5435125865130096 + x16)^2) + x419 * ((-0.6309807709209095 + x13)^2 + (
    -0.3784634566348025 + x14)^2 + (-0.39906901089542124 + x15)^2 + (
    -0.4255257271419496 + x16)^2) + x420 * ((-0.2531527659499414 + x13)^2 + (
    -0.3939338403635574 + x14)^2 + (-0.24367103431275294 + x15)^2 + (
    -0.09965076327279909 + x16)^2) + x421 * ((-0.4613429383834692 + x13)^2 + (
    -0.3270734410373959 + x14)^2 + (-0.3721913332914448 + x15)^2 + (
    -0.8397998489632109 + x16)^2) + x422 * ((-0.38125619155081125 + x13)^2 + (
    -0.38637355155860587 + x14)^2 + (-0.48242666628327 + x15)^2 + (
    -0.09841931704125129 + x16)^2) + x423 * ((-0.8312772318196014 + x13)^2 + (
    -0.8386805111720071 + x14)^2 + (-0.7116803614743081 + x15)^2 + (
    -0.1685702196156904 + x16)^2) + x424 * ((-0.9799547522897909 + x13)^2 + (
    -0.833448605810144 + x14)^2 + (-0.8740694081049383 + x15)^2 + (
    -0.6506828607108437 + x16)^2) + x425 * ((-0.1607430602427229 + x13)^2 + (
    -0.9407888153270746 + x14)^2 + (-0.6263933433327887 + x15)^2 + (
    -0.749780063323727 + x16)^2) + x426 * ((-0.7159349886520615 + x13)^2 + (
    -0.5782176711798136 + x14)^2 + (-0.2549127897200829 + x15)^2 + (
    -0.2942758616813056 + x16)^2) + x427 * ((-0.2937946995191628 + x13)^2 + (
    -0.7467755231646197 + x14)^2 + (-0.12056041976861509 + x15)^2 + (
    -0.6656163636347733 + x16)^2) + x428 * ((-0.1391657590641412 + x13)^2 + (
    -0.7998527624894191 + x14)^2 + (-0.8268662401101857 + x15)^2 + (
    -0.33882597292525984 + x16)^2) + x429 * ((-0.6582625122649799 + x17)^2 + (
    -0.10362896941145872 + x18)^2 + (-0.8195797598856802 + x19)^2 + (
    -0.5422289997742272 + x20)^2) + x430 * ((-0.3661207081728268 + x17)^2 + (
    -0.7480408210929997 + x18)^2 + (-0.6813605839850432 + x19)^2 + (
    -0.5056692315871436 + x20)^2) + x431 * ((-0.07046798157590661 + x17)^2 + (
    -0.5775220724425275 + x18)^2 + (-0.7916097196998284 + x19)^2 + (
    -0.9106301943747759 + x20)^2) + x432 * ((-0.9143624080891343 + x17)^2 + (
    -0.5102176451888726 + x18)^2 + (-0.46023708546130926 + x19)^2 + (
    -0.21559477969887786 + x20)^2) + x433 * ((-0.2152968191062874 + x17)^2 + (
    -0.40849216327387305 + x18)^2 + (-0.20734483145145233 + x19)^2 + (
    -0.29299530170003807 + x20)^2) + x434 * ((-0.753381482947803 + x17)^2 + (
    -0.569021356481719 + x18)^2 + (-0.825772931187451 + x19)^2 + (
    -0.6717803623991925 + x20)^2) + x435 * ((-0.22558272825834902 + x17)^2 + (
    -0.1431433457263549 + x18)^2 + (-0.36496670173321977 + x19)^2 + (
    -0.8283121504397382 + x20)^2) + x436 * ((-0.1043150551410561 + x17)^2 + (
    -0.5878900110989006 + x18)^2 + (-0.9303409193762857 + x19)^2 + (
    -0.1857245451574967 + x20)^2) + x437 * ((-0.2569777266497605 + x17)^2 + (
    -0.44043166993274085 + x18)^2 + (-0.15843257127556898 + x19)^2 + (
    -0.952596167014909 + x20)^2) + x438 * ((-0.767248128715498 + x17)^2 + (
    -0.16237189449331368 + x18)^2 + (-0.06342633508651152 + x19)^2 + (
    -0.8024171562438219 + x20)^2) + x439 * ((-0.7172302300642502 + x17)^2 + (
    -0.3391758201292703 + x18)^2 + (-0.030384935563099513 + x19)^2 + (
    -0.06493483472263029 + x20)^2) + x440 * ((-0.3661672203776154 + x17)^2 + (
    -0.9542180221871335 + x18)^2 + (-0.5308186536817474 + x19)^2 + (
    -0.16997124480838255 + x20)^2) + x441 * ((-0.23659736779603846 + x17)^2 + (
    -0.6214607353719023 + x18)^2 + (-0.3081993619295993 + x19)^2 + (
    -0.3526409606385007 + x20)^2) + x442 * ((-0.9752782586626233 + x17)^2 + (
    -0.5844650261883885 + x18)^2 + (-0.37649426913773276 + x19)^2 + (
    -0.10816991983567104 + x20)^2) + x443 * ((-0.45932686546602697 + x17)^2 + (
    -0.21233217626711853 + x18)^2 + (-0.9164032346567896 + x19)^2 + (
    -0.37108439943759797 + x20)^2) + x444 * ((-0.6867210427728082 + x17)^2 + (
    -0.7796854955112769 + x18)^2 + (-0.11982168093807799 + x19)^2 + (
    -0.6159743897209107 + x20)^2) + x445 * ((-0.985368764646874 + x17)^2 + (
    -0.07384180286280495 + x18)^2 + (-0.12212817800129094 + x19)^2 + (
    -0.2984771462799074 + x20)^2) + x446 * ((-0.7476106092305221 + x17)^2 + (
    -0.4411310968444404 + x18)^2 + (-0.5921500130284744 + x19)^2 + (
    -0.4842613828145912 + x20)^2) + x447 * ((-0.9737472353802095 + x17)^2 + (
    -0.09330122936543495 + x18)^2 + (-0.6050695157211611 + x19)^2 + (
    -0.07252152451660332 + x20)^2) + x448 * ((-0.09013540585240642 + x17)^2 + (
    -0.31276776356555547 + x18)^2 + (-0.7994057211441843 + x19)^2 + (
    -0.22689981649412638 + x20)^2) + x449 * ((-0.6283164056152335 + x17)^2 + (
    -0.3785737682752087 + x18)^2 + (-0.0024714258559164204 + x19)^2 + (
    -0.8148514253118784 + x20)^2) + x450 * ((-0.45370880893982724 + x17)^2 + (
    -0.10391203375848834 + x18)^2 + (-0.24027615267372093 + x19)^2 + (
    -0.2552645467206819 + x20)^2) + x451 * ((-0.4061008020592297 + x17)^2 + (
    -0.9396418294747921 + x18)^2 + (-0.5690658238794261 + x19)^2 + (
    -0.16866076993955403 + x20)^2) + x452 * ((-0.2314528417813161 + x17)^2 + (
    -0.5525474743329635 + x18)^2 + (-0.24649406583643063 + x19)^2 + (
    -0.9613520728571585 + x20)^2) + x453 * ((-0.5139605500157903 + x17)^2 + (
    -0.6815512588331698 + x18)^2 + (-0.16796296820903867 + x19)^2 + (
    -0.7162074865739461 + x20)^2) + x454 * ((-0.7706393889182662 + x17)^2 + (
    -0.43003110845525816 + x18)^2 + (-0.9356475551939986 + x19)^2 + (
    -0.5933795966331403 + x20)^2) + x455 * ((-0.5249118669899329 + x17)^2 + (
    -0.04056638284243541 + x18)^2 + (-0.0768970587722112 + x19)^2 + (
    -0.8247484594687006 + x20)^2) + x456 * ((-0.824923342468354 + x17)^2 + (
    -0.24405019701972253 + x18)^2 + (-0.38404505866575367 + x19)^2 + (
    -0.8313733189621139 + x20)^2) + x457 * ((-0.33950374022026997 + x17)^2 + (
    -0.5976095637618721 + x18)^2 + (-0.7602631636886854 + x19)^2 + (
    -0.4500249936588927 + x20)^2) + x458 * ((-0.523162910024812 + x17)^2 + (
    -0.3436248527141411 + x18)^2 + (-0.4561418310928951 + x19)^2 + (
    -0.8742103555752229 + x20)^2) + x459 * ((-0.3337530963427443 + x17)^2 + (
    -0.9855745242910374 + x18)^2 + (-0.9617621389771519 + x19)^2 + (
    -0.22441530334931115 + x20)^2) + x460 * ((-0.25477260253407985 + x17)^2 + (
    -0.3657617338278605 + x18)^2 + (-0.4599755066722203 + x19)^2 + (
    -0.488019659535353 + x20)^2) + x461 * ((-0.2663904007493795 + x17)^2 + (
    -0.27222258016843315 + x18)^2 + (-0.2880874179930988 + x19)^2 + (
    -0.02481848847156809 + x20)^2) + x462 * ((-0.2075297065152052 + x17)^2 + (
    -0.7022983060607665 + x18)^2 + (-0.47827086724608314 + x19)^2 + (
    -0.28622027057302846 + x20)^2) + x463 * ((-0.7047452543816871 + x17)^2 + (
    -0.6996554684275655 + x18)^2 + (-0.16578869005033847 + x19)^2 + (
    -0.5179151157105838 + x20)^2) + x464 * ((-0.7436571093571753 + x17)^2 + (
    -0.8723672259073825 + x18)^2 + (-0.9145540584909153 + x19)^2 + (
    -0.4616843537475913 + x20)^2) + x465 * ((-0.40078313938185106 + x17)^2 + (
    -0.7616315326378316 + x18)^2 + (-0.0624885237314553 + x19)^2 + (
    -0.33349386555475435 + x20)^2) + x466 * ((-0.47083964839087056 + x17)^2 + (
    -0.7540812887396847 + x18)^2 + (-0.7698437223374434 + x19)^2 + (
    -0.7260097297577066 + x20)^2) + x467 * ((-0.470591984548581 + x17)^2 + (
    -0.21419699662552538 + x18)^2 + (-0.8214784727628405 + x19)^2 + (
    -0.9327146275722538 + x20)^2) + x468 * ((-0.6694092237740207 + x17)^2 + (
    -0.40188436538160965 + x18)^2 + (-0.9078829021652501 + x19)^2 + (
    -0.28882880291122615 + x20)^2) + x469 * ((-0.8012821680592233 + x17)^2 + (
    -0.26764801084685064 + x18)^2 + (-0.8907563902239161 + x19)^2 + (
    -0.022670562427511642 + x20)^2) + x470 * ((-0.3149563708936517 + x17)^2 + (
    -0.4013573755930997 + x18)^2 + (-0.16444723142036033 + x19)^2 + (
    -0.8783064548569166 + x20)^2) + x471 * ((-0.0452536291694966 + x17)^2 + (
    -0.6030683870184952 + x18)^2 + (-0.12061018849928773 + x19)^2 + (
    -0.6161186728209969 + x20)^2) + x472 * ((-0.8303237648967787 + x17)^2 + (
    -0.7542211701244139 + x18)^2 + (-0.47189785643150806 + x19)^2 + (
    -0.7928252514256884 + x20)^2) + x473 * ((-0.6429343022480377 + x17)^2 + (
    -0.6021334537878723 + x18)^2 + (-0.2852218418361189 + x19)^2 + (
    -0.29825945641738283 + x20)^2) + x474 * ((-0.11776074988832852 + x17)^2 + (
    -0.8643957197110975 + x18)^2 + (-0.03338227312045139 + x19)^2 + (
    -0.593939114377175 + x20)^2) + x475 * ((-0.418497245301816 + x17)^2 + (
    -0.3081055339744846 + x18)^2 + (-0.38130196746434064 + x19)^2 + (
    -0.6612469720321472 + x20)^2) + x476 * ((-0.5815493986252239 + x17)^2 + (
    -0.6811102264085155 + x18)^2 + (-0.1453934105814335 + x19)^2 + (
    -0.8013757499531303 + x20)^2) + x477 * ((-0.00607035083945795 + x17)^2 + (
    -0.053561905123383324 + x18)^2 + (-0.7817703845300363 + x19)^2 + (
    -0.5662212686106933 + x20)^2) + x478 * ((-0.6950221994466669 + x17)^2 + (
    -0.2105034885347269 + x18)^2 + (-0.11287315442891777 + x19)^2 + (
    -0.010597472308638611 + x20)^2) + x479 * ((-0.5311582701895528 + x17)^2 + (
    -0.4320063664214896 + x18)^2 + (-0.2729049031820855 + x19)^2 + (
    -0.2214949427555688 + x20)^2) + x480 * ((-0.48150146533157034 + x17)^2 + (
    -0.46067276862424755 + x18)^2 + (-0.0056974073880511344 + x19)^2 + (
    -0.35728414461795144 + x20)^2) + x481 * ((-0.9429852300228826 + x17)^2 + (
    -0.39303494745904877 + x18)^2 + (-0.31011214177569657 + x19)^2 + (
    -0.018438339560493344 + x20)^2) + x482 * ((-0.5322977536893222 + x17)^2 + (
    -0.9652470893187132 + x18)^2 + (-0.21135139952422877 + x19)^2 + (
    -0.8156809600304314 + x20)^2) + x483 * ((-0.03401283459710902 + x17)^2 + (
    -0.806892267442106 + x18)^2 + (-0.8489758888126404 + x19)^2 + (
    -0.6111483840787582 + x20)^2) + x484 * ((-0.9264484533738693 + x17)^2 + (
    -0.14876976743207326 + x18)^2 + (-0.9758190264647324 + x19)^2 + (
    -0.6811285636971497 + x20)^2) + x485 * ((-0.9647303094099035 + x17)^2 + (
    -0.7010206460934956 + x18)^2 + (-0.30943177373448516 + x19)^2 + (
    -0.1891022383766483 + x20)^2) + x486 * ((-0.4769220240119476 + x17)^2 + (
    -0.822318413841706 + x18)^2 + (-0.1393694419930549 + x19)^2 + (
    -0.9724217562379036 + x20)^2) + x487 * ((-0.7455477334590928 + x17)^2 + (
    -0.563396428008588 + x18)^2 + (-0.22992430827076737 + x19)^2 + (
    -0.2370557772132338 + x20)^2) + x488 * ((-0.16535109726174313 + x17)^2 + (
    -0.9547852441919761 + x18)^2 + (-0.3203072223564828 + x19)^2 + (
    -0.42492616349386114 + x20)^2) + x489 * ((-0.7834231836651542 + x17)^2 + (
    -0.24935541853121224 + x18)^2 + (-0.8297208826099771 + x19)^2 + (
    -0.23563563513419228 + x20)^2) + x490 * ((-0.8373741924252092 + x17)^2 + (
    -0.36970144853956455 + x18)^2 + (-0.5671956111716981 + x19)^2 + (
    -0.3691960678174552 + x20)^2) + x491 * ((-0.39886787270583346 + x17)^2 + (
    -0.650964776918859 + x18)^2 + (-0.640819546256607 + x19)^2 + (
    -0.09882188475998765 + x20)^2) + x492 * ((-0.5157745663985024 + x17)^2 + (
    -0.5435336580091097 + x18)^2 + (-0.27430425498315725 + x19)^2 + (
    -0.7274939676197051 + x20)^2) + x493 * ((-0.537162865589002 + x17)^2 + (
    -0.5913784936821398 + x18)^2 + (-0.45466522772907525 + x19)^2 + (
    -0.1047184477665718 + x20)^2) + x494 * ((-0.04102323848681244 + x17)^2 + (
    -0.5377574929590462 + x18)^2 + (-0.9782258268406425 + x19)^2 + (
    -0.9716171817066379 + x20)^2) + x495 * ((-0.6871600172780726 + x17)^2 + (
    -0.8418720435526559 + x18)^2 + (-0.83052769064337 + x19)^2 + (
    -0.8985953589244926 + x20)^2) + x496 * ((-0.10160325017586314 + x17)^2 + (
    -0.8817097435158873 + x18)^2 + (-0.2972532110491476 + x19)^2 + (
    -0.34330327059943233 + x20)^2) + x497 * ((-0.276256004491218 + x17)^2 + (
    -0.9717101669718731 + x18)^2 + (-0.2984317666596268 + x19)^2 + (
    -0.4440796331949195 + x20)^2) + x498 * ((-0.9523516045369547 + x17)^2 + (
    -0.6811203295261851 + x18)^2 + (-0.17487173576269888 + x19)^2 + (
    -0.264608767198526 + x20)^2) + x499 * ((-0.5950072414516107 + x17)^2 + (
    -0.19863608495271834 + x18)^2 + (-0.3254107876389821 + x19)^2 + (
    -0.8432385372383167 + x20)^2) + x500 * ((-0.8468632268868022 + x17)^2 + (
    -0.07323866891200903 + x18)^2 + (-0.8068985989515749 + x19)^2 + (
    -0.6810798779677064 + x20)^2) + x501 * ((-0.4712188830735816 + x17)^2 + (
    -0.4135054120302819 + x18)^2 + (-0.3077078179033642 + x19)^2 + (
    -0.3353457462826305 + x20)^2) + x502 * ((-0.31701343040014285 + x17)^2 + (
    -0.6308301684094946 + x18)^2 + (-0.5476747635071102 + x19)^2 + (
    -0.26992487329332904 + x20)^2) + x503 * ((-0.19701342670354327 + x17)^2 + (
    -0.4781921949933534 + x18)^2 + (-0.7057141592764116 + x19)^2 + (
    -0.0896309852595556 + x20)^2) + x504 * ((-0.8038878371618275 + x17)^2 + (
    -0.044329635856571015 + x18)^2 + (-0.898513730220423 + x19)^2 + (
    -0.5600362942589316 + x20)^2) + x505 * ((-0.14961294077862985 + x17)^2 + (
    -0.9772469188459079 + x18)^2 + (-0.12015140801504265 + x19)^2 + (
    -0.521329056759319 + x20)^2) + x506 * ((-0.03381103052182122 + x17)^2 + (
    -0.527498561244566 + x18)^2 + (-0.44345060645273227 + x19)^2 + (
    -0.006260254814196675 + x20)^2) + x507 * ((-0.8219788276317623 + x17)^2 + (
    -0.3852922260631585 + x18)^2 + (-0.9620135163986219 + x19)^2 + (
    -0.18635183396741328 + x20)^2) + x508 * ((-0.7389415908359858 + x17)^2 + (
    -0.523761972701124 + x18)^2 + (-0.46623643584676433 + x19)^2 + (
    -0.0580789763043309 + x20)^2) + x509 * ((-0.5180391196124703 + x17)^2 + (
    -0.125977305519825 + x18)^2 + (-0.7141405174792315 + x19)^2 + (
    -0.6913703129848836 + x20)^2) + x510 * ((-0.26351088593273375 + x17)^2 + (
    -0.45761632800962093 + x18)^2 + (-0.7832055136876419 + x19)^2 + (
    -0.13621640940288493 + x20)^2) + x511 * ((-0.471522719293638 + x17)^2 + (
    -0.6233304917288576 + x18)^2 + (-0.9541794868794985 + x19)^2 + (
    -0.8015112028077606 + x20)^2) + x512 * ((-0.602523335859397 + x17)^2 + (
    -0.9632346106061206 + x18)^2 + (-0.9904964428766339 + x19)^2 + (
    -0.051156798506716616 + x20)^2) + x513 * ((-0.5884363239423929 + x17)^2 + (
    -0.9712278123715459 + x18)^2 + (-0.39988158182711386 + x19)^2 + (
    -0.41099930765106685 + x20)^2) + x514 * ((-0.5312213971906167 + x17)^2 + (
    -0.81785083419928 + x18)^2 + (-0.11725286157727799 + x19)^2 + (
    -0.47116385459902677 + x20)^2) + x515 * ((-0.9276992489134009 + x17)^2 + (
    -0.276293095414863 + x18)^2 + (-0.694461598585542 + x19)^2 + (
    -0.24661724253663275 + x20)^2) + x516 * ((-0.8984827464797928 + x17)^2 + (
    -0.8392110392495009 + x18)^2 + (-0.29003442507035804 + x19)^2 + (
    -0.7169574587131787 + x20)^2) + x517 * ((-0.7178579817600614 + x17)^2 + (
    -0.5442760502478915 + x18)^2 + (-0.3613660892547932 + x19)^2 + (
    -0.8887949357847075 + x20)^2) + x518 * ((-0.20832626177371294 + x17)^2 + (
    -0.6155556242775743 + x18)^2 + (-0.24252949041723848 + x19)^2 + (
    -0.5435125865130096 + x20)^2) + x519 * ((-0.6309807709209095 + x17)^2 + (
    -0.3784634566348025 + x18)^2 + (-0.39906901089542124 + x19)^2 + (
    -0.4255257271419496 + x20)^2) + x520 * ((-0.2531527659499414 + x17)^2 + (
    -0.3939338403635574 + x18)^2 + (-0.24367103431275294 + x19)^2 + (
    -0.09965076327279909 + x20)^2) + x521 * ((-0.4613429383834692 + x17)^2 + (
    -0.3270734410373959 + x18)^2 + (-0.3721913332914448 + x19)^2 + (
    -0.8397998489632109 + x20)^2) + x522 * ((-0.38125619155081125 + x17)^2 + (
    -0.38637355155860587 + x18)^2 + (-0.48242666628327 + x19)^2 + (
    -0.09841931704125129 + x20)^2) + x523 * ((-0.8312772318196014 + x17)^2 + (
    -0.8386805111720071 + x18)^2 + (-0.7116803614743081 + x19)^2 + (
    -0.1685702196156904 + x20)^2) + x524 * ((-0.9799547522897909 + x17)^2 + (
    -0.833448605810144 + x18)^2 + (-0.8740694081049383 + x19)^2 + (
    -0.6506828607108437 + x20)^2) + x525 * ((-0.1607430602427229 + x17)^2 + (
    -0.9407888153270746 + x18)^2 + (-0.6263933433327887 + x19)^2 + (
    -0.749780063323727 + x20)^2) + x526 * ((-0.7159349886520615 + x17)^2 + (
    -0.5782176711798136 + x18)^2 + (-0.2549127897200829 + x19)^2 + (
    -0.2942758616813056 + x20)^2) + x527 * ((-0.2937946995191628 + x17)^2 + (
    -0.7467755231646197 + x18)^2 + (-0.12056041976861509 + x19)^2 + (
    -0.6656163636347733 + x20)^2) + x528 * ((-0.1391657590641412 + x17)^2 + (
    -0.7998527624894191 + x18)^2 + (-0.8268662401101857 + x19)^2 + (
    -0.33882597292525984 + x20)^2) + x529 * ((-0.6582625122649799 + x21)^2 + (
    -0.10362896941145872 + x22)^2 + (-0.8195797598856802 + x23)^2 + (
    -0.5422289997742272 + x24)^2) + x530 * ((-0.3661207081728268 + x21)^2 + (
    -0.7480408210929997 + x22)^2 + (-0.6813605839850432 + x23)^2 + (
    -0.5056692315871436 + x24)^2) + x531 * ((-0.07046798157590661 + x21)^2 + (
    -0.5775220724425275 + x22)^2 + (-0.7916097196998284 + x23)^2 + (
    -0.9106301943747759 + x24)^2) + x532 * ((-0.9143624080891343 + x21)^2 + (
    -0.5102176451888726 + x22)^2 + (-0.46023708546130926 + x23)^2 + (
    -0.21559477969887786 + x24)^2) + x533 * ((-0.2152968191062874 + x21)^2 + (
    -0.40849216327387305 + x22)^2 + (-0.20734483145145233 + x23)^2 + (
    -0.29299530170003807 + x24)^2) + x534 * ((-0.753381482947803 + x21)^2 + (
    -0.569021356481719 + x22)^2 + (-0.825772931187451 + x23)^2 + (
    -0.6717803623991925 + x24)^2) + x535 * ((-0.22558272825834902 + x21)^2 + (
    -0.1431433457263549 + x22)^2 + (-0.36496670173321977 + x23)^2 + (
    -0.8283121504397382 + x24)^2) + x536 * ((-0.1043150551410561 + x21)^2 + (
    -0.5878900110989006 + x22)^2 + (-0.9303409193762857 + x23)^2 + (
    -0.1857245451574967 + x24)^2) + x537 * ((-0.2569777266497605 + x21)^2 + (
    -0.44043166993274085 + x22)^2 + (-0.15843257127556898 + x23)^2 + (
    -0.952596167014909 + x24)^2) + x538 * ((-0.767248128715498 + x21)^2 + (
    -0.16237189449331368 + x22)^2 + (-0.06342633508651152 + x23)^2 + (
    -0.8024171562438219 + x24)^2) + x539 * ((-0.7172302300642502 + x21)^2 + (
    -0.3391758201292703 + x22)^2 + (-0.030384935563099513 + x23)^2 + (
    -0.06493483472263029 + x24)^2) + x540 * ((-0.3661672203776154 + x21)^2 + (
    -0.9542180221871335 + x22)^2 + (-0.5308186536817474 + x23)^2 + (
    -0.16997124480838255 + x24)^2) + x541 * ((-0.23659736779603846 + x21)^2 + (
    -0.6214607353719023 + x22)^2 + (-0.3081993619295993 + x23)^2 + (
    -0.3526409606385007 + x24)^2) + x542 * ((-0.9752782586626233 + x21)^2 + (
    -0.5844650261883885 + x22)^2 + (-0.37649426913773276 + x23)^2 + (
    -0.10816991983567104 + x24)^2) + x543 * ((-0.45932686546602697 + x21)^2 + (
    -0.21233217626711853 + x22)^2 + (-0.9164032346567896 + x23)^2 + (
    -0.37108439943759797 + x24)^2) + x544 * ((-0.6867210427728082 + x21)^2 + (
    -0.7796854955112769 + x22)^2 + (-0.11982168093807799 + x23)^2 + (
    -0.6159743897209107 + x24)^2) + x545 * ((-0.985368764646874 + x21)^2 + (
    -0.07384180286280495 + x22)^2 + (-0.12212817800129094 + x23)^2 + (
    -0.2984771462799074 + x24)^2) + x546 * ((-0.7476106092305221 + x21)^2 + (
    -0.4411310968444404 + x22)^2 + (-0.5921500130284744 + x23)^2 + (
    -0.4842613828145912 + x24)^2) + x547 * ((-0.9737472353802095 + x21)^2 + (
    -0.09330122936543495 + x22)^2 + (-0.6050695157211611 + x23)^2 + (
    -0.07252152451660332 + x24)^2) + x548 * ((-0.09013540585240642 + x21)^2 + (
    -0.31276776356555547 + x22)^2 + (-0.7994057211441843 + x23)^2 + (
    -0.22689981649412638 + x24)^2) + x549 * ((-0.6283164056152335 + x21)^2 + (
    -0.3785737682752087 + x22)^2 + (-0.0024714258559164204 + x23)^2 + (
    -0.8148514253118784 + x24)^2) + x550 * ((-0.45370880893982724 + x21)^2 + (
    -0.10391203375848834 + x22)^2 + (-0.24027615267372093 + x23)^2 + (
    -0.2552645467206819 + x24)^2) + x551 * ((-0.4061008020592297 + x21)^2 + (
    -0.9396418294747921 + x22)^2 + (-0.5690658238794261 + x23)^2 + (
    -0.16866076993955403 + x24)^2) + x552 * ((-0.2314528417813161 + x21)^2 + (
    -0.5525474743329635 + x22)^2 + (-0.24649406583643063 + x23)^2 + (
    -0.9613520728571585 + x24)^2) + x553 * ((-0.5139605500157903 + x21)^2 + (
    -0.6815512588331698 + x22)^2 + (-0.16796296820903867 + x23)^2 + (
    -0.7162074865739461 + x24)^2) + x554 * ((-0.7706393889182662 + x21)^2 + (
    -0.43003110845525816 + x22)^2 + (-0.9356475551939986 + x23)^2 + (
    -0.5933795966331403 + x24)^2) + x555 * ((-0.5249118669899329 + x21)^2 + (
    -0.04056638284243541 + x22)^2 + (-0.0768970587722112 + x23)^2 + (
    -0.8247484594687006 + x24)^2) + x556 * ((-0.824923342468354 + x21)^2 + (
    -0.24405019701972253 + x22)^2 + (-0.38404505866575367 + x23)^2 + (
    -0.8313733189621139 + x24)^2) + x557 * ((-0.33950374022026997 + x21)^2 + (
    -0.5976095637618721 + x22)^2 + (-0.7602631636886854 + x23)^2 + (
    -0.4500249936588927 + x24)^2) + x558 * ((-0.523162910024812 + x21)^2 + (
    -0.3436248527141411 + x22)^2 + (-0.4561418310928951 + x23)^2 + (
    -0.8742103555752229 + x24)^2) + x559 * ((-0.3337530963427443 + x21)^2 + (
    -0.9855745242910374 + x22)^2 + (-0.9617621389771519 + x23)^2 + (
    -0.22441530334931115 + x24)^2) + x560 * ((-0.25477260253407985 + x21)^2 + (
    -0.3657617338278605 + x22)^2 + (-0.4599755066722203 + x23)^2 + (
    -0.488019659535353 + x24)^2) + x561 * ((-0.2663904007493795 + x21)^2 + (
    -0.27222258016843315 + x22)^2 + (-0.2880874179930988 + x23)^2 + (
    -0.02481848847156809 + x24)^2) + x562 * ((-0.2075297065152052 + x21)^2 + (
    -0.7022983060607665 + x22)^2 + (-0.47827086724608314 + x23)^2 + (
    -0.28622027057302846 + x24)^2) + x563 * ((-0.7047452543816871 + x21)^2 + (
    -0.6996554684275655 + x22)^2 + (-0.16578869005033847 + x23)^2 + (
    -0.5179151157105838 + x24)^2) + x564 * ((-0.7436571093571753 + x21)^2 + (
    -0.8723672259073825 + x22)^2 + (-0.9145540584909153 + x23)^2 + (
    -0.4616843537475913 + x24)^2) + x565 * ((-0.40078313938185106 + x21)^2 + (
    -0.7616315326378316 + x22)^2 + (-0.0624885237314553 + x23)^2 + (
    -0.33349386555475435 + x24)^2) + x566 * ((-0.47083964839087056 + x21)^2 + (
    -0.7540812887396847 + x22)^2 + (-0.7698437223374434 + x23)^2 + (
    -0.7260097297577066 + x24)^2) + x567 * ((-0.470591984548581 + x21)^2 + (
    -0.21419699662552538 + x22)^2 + (-0.8214784727628405 + x23)^2 + (
    -0.9327146275722538 + x24)^2) + x568 * ((-0.6694092237740207 + x21)^2 + (
    -0.40188436538160965 + x22)^2 + (-0.9078829021652501 + x23)^2 + (
    -0.28882880291122615 + x24)^2) + x569 * ((-0.8012821680592233 + x21)^2 + (
    -0.26764801084685064 + x22)^2 + (-0.8907563902239161 + x23)^2 + (
    -0.022670562427511642 + x24)^2) + x570 * ((-0.3149563708936517 + x21)^2 + (
    -0.4013573755930997 + x22)^2 + (-0.16444723142036033 + x23)^2 + (
    -0.8783064548569166 + x24)^2) + x571 * ((-0.0452536291694966 + x21)^2 + (
    -0.6030683870184952 + x22)^2 + (-0.12061018849928773 + x23)^2 + (
    -0.6161186728209969 + x24)^2) + x572 * ((-0.8303237648967787 + x21)^2 + (
    -0.7542211701244139 + x22)^2 + (-0.47189785643150806 + x23)^2 + (
    -0.7928252514256884 + x24)^2) + x573 * ((-0.6429343022480377 + x21)^2 + (
    -0.6021334537878723 + x22)^2 + (-0.2852218418361189 + x23)^2 + (
    -0.29825945641738283 + x24)^2) + x574 * ((-0.11776074988832852 + x21)^2 + (
    -0.8643957197110975 + x22)^2 + (-0.03338227312045139 + x23)^2 + (
    -0.593939114377175 + x24)^2) + x575 * ((-0.418497245301816 + x21)^2 + (
    -0.3081055339744846 + x22)^2 + (-0.38130196746434064 + x23)^2 + (
    -0.6612469720321472 + x24)^2) + x576 * ((-0.5815493986252239 + x21)^2 + (
    -0.6811102264085155 + x22)^2 + (-0.1453934105814335 + x23)^2 + (
    -0.8013757499531303 + x24)^2) + x577 * ((-0.00607035083945795 + x21)^2 + (
    -0.053561905123383324 + x22)^2 + (-0.7817703845300363 + x23)^2 + (
    -0.5662212686106933 + x24)^2) + x578 * ((-0.6950221994466669 + x21)^2 + (
    -0.2105034885347269 + x22)^2 + (-0.11287315442891777 + x23)^2 + (
    -0.010597472308638611 + x24)^2) + x579 * ((-0.5311582701895528 + x21)^2 + (
    -0.4320063664214896 + x22)^2 + (-0.2729049031820855 + x23)^2 + (
    -0.2214949427555688 + x24)^2) + x580 * ((-0.48150146533157034 + x21)^2 + (
    -0.46067276862424755 + x22)^2 + (-0.0056974073880511344 + x23)^2 + (
    -0.35728414461795144 + x24)^2) + x581 * ((-0.9429852300228826 + x21)^2 + (
    -0.39303494745904877 + x22)^2 + (-0.31011214177569657 + x23)^2 + (
    -0.018438339560493344 + x24)^2) + x582 * ((-0.5322977536893222 + x21)^2 + (
    -0.9652470893187132 + x22)^2 + (-0.21135139952422877 + x23)^2 + (
    -0.8156809600304314 + x24)^2) + x583 * ((-0.03401283459710902 + x21)^2 + (
    -0.806892267442106 + x22)^2 + (-0.8489758888126404 + x23)^2 + (
    -0.6111483840787582 + x24)^2) + x584 * ((-0.9264484533738693 + x21)^2 + (
    -0.14876976743207326 + x22)^2 + (-0.9758190264647324 + x23)^2 + (
    -0.6811285636971497 + x24)^2) + x585 * ((-0.9647303094099035 + x21)^2 + (
    -0.7010206460934956 + x22)^2 + (-0.30943177373448516 + x23)^2 + (
    -0.1891022383766483 + x24)^2) + x586 * ((-0.4769220240119476 + x21)^2 + (
    -0.822318413841706 + x22)^2 + (-0.1393694419930549 + x23)^2 + (
    -0.9724217562379036 + x24)^2) + x587 * ((-0.7455477334590928 + x21)^2 + (
    -0.563396428008588 + x22)^2 + (-0.22992430827076737 + x23)^2 + (
    -0.2370557772132338 + x24)^2) + x588 * ((-0.16535109726174313 + x21)^2 + (
    -0.9547852441919761 + x22)^2 + (-0.3203072223564828 + x23)^2 + (
    -0.42492616349386114 + x24)^2) + x589 * ((-0.7834231836651542 + x21)^2 + (
    -0.24935541853121224 + x22)^2 + (-0.8297208826099771 + x23)^2 + (
    -0.23563563513419228 + x24)^2) + x590 * ((-0.8373741924252092 + x21)^2 + (
    -0.36970144853956455 + x22)^2 + (-0.5671956111716981 + x23)^2 + (
    -0.3691960678174552 + x24)^2) + x591 * ((-0.39886787270583346 + x21)^2 + (
    -0.650964776918859 + x22)^2 + (-0.640819546256607 + x23)^2 + (
    -0.09882188475998765 + x24)^2) + x592 * ((-0.5157745663985024 + x21)^2 + (
    -0.5435336580091097 + x22)^2 + (-0.27430425498315725 + x23)^2 + (
    -0.7274939676197051 + x24)^2) + x593 * ((-0.537162865589002 + x21)^2 + (
    -0.5913784936821398 + x22)^2 + (-0.45466522772907525 + x23)^2 + (
    -0.1047184477665718 + x24)^2) + x594 * ((-0.04102323848681244 + x21)^2 + (
    -0.5377574929590462 + x22)^2 + (-0.9782258268406425 + x23)^2 + (
    -0.9716171817066379 + x24)^2) + x595 * ((-0.6871600172780726 + x21)^2 + (
    -0.8418720435526559 + x22)^2 + (-0.83052769064337 + x23)^2 + (
    -0.8985953589244926 + x24)^2) + x596 * ((-0.10160325017586314 + x21)^2 + (
    -0.8817097435158873 + x22)^2 + (-0.2972532110491476 + x23)^2 + (
    -0.34330327059943233 + x24)^2) + x597 * ((-0.276256004491218 + x21)^2 + (
    -0.9717101669718731 + x22)^2 + (-0.2984317666596268 + x23)^2 + (
    -0.4440796331949195 + x24)^2) + x598 * ((-0.9523516045369547 + x21)^2 + (
    -0.6811203295261851 + x22)^2 + (-0.17487173576269888 + x23)^2 + (
    -0.264608767198526 + x24)^2) + x599 * ((-0.5950072414516107 + x21)^2 + (
    -0.19863608495271834 + x22)^2 + (-0.3254107876389821 + x23)^2 + (
    -0.8432385372383167 + x24)^2) + x600 * ((-0.8468632268868022 + x21)^2 + (
    -0.07323866891200903 + x22)^2 + (-0.8068985989515749 + x23)^2 + (
    -0.6810798779677064 + x24)^2) + x601 * ((-0.4712188830735816 + x21)^2 + (
    -0.4135054120302819 + x22)^2 + (-0.3077078179033642 + x23)^2 + (
    -0.3353457462826305 + x24)^2) + x602 * ((-0.31701343040014285 + x21)^2 + (
    -0.6308301684094946 + x22)^2 + (-0.5476747635071102 + x23)^2 + (
    -0.26992487329332904 + x24)^2) + x603 * ((-0.19701342670354327 + x21)^2 + (
    -0.4781921949933534 + x22)^2 + (-0.7057141592764116 + x23)^2 + (
    -0.0896309852595556 + x24)^2) + x604 * ((-0.8038878371618275 + x21)^2 + (
    -0.044329635856571015 + x22)^2 + (-0.898513730220423 + x23)^2 + (
    -0.5600362942589316 + x24)^2) + x605 * ((-0.14961294077862985 + x21)^2 + (
    -0.9772469188459079 + x22)^2 + (-0.12015140801504265 + x23)^2 + (
    -0.521329056759319 + x24)^2) + x606 * ((-0.03381103052182122 + x21)^2 + (
    -0.527498561244566 + x22)^2 + (-0.44345060645273227 + x23)^2 + (
    -0.006260254814196675 + x24)^2) + x607 * ((-0.8219788276317623 + x21)^2 + (
    -0.3852922260631585 + x22)^2 + (-0.9620135163986219 + x23)^2 + (
    -0.18635183396741328 + x24)^2) + x608 * ((-0.7389415908359858 + x21)^2 + (
    -0.523761972701124 + x22)^2 + (-0.46623643584676433 + x23)^2 + (
    -0.0580789763043309 + x24)^2) + x609 * ((-0.5180391196124703 + x21)^2 + (
    -0.125977305519825 + x22)^2 + (-0.7141405174792315 + x23)^2 + (
    -0.6913703129848836 + x24)^2) + x610 * ((-0.26351088593273375 + x21)^2 + (
    -0.45761632800962093 + x22)^2 + (-0.7832055136876419 + x23)^2 + (
    -0.13621640940288493 + x24)^2) + x611 * ((-0.471522719293638 + x21)^2 + (
    -0.6233304917288576 + x22)^2 + (-0.9541794868794985 + x23)^2 + (
    -0.8015112028077606 + x24)^2) + x612 * ((-0.602523335859397 + x21)^2 + (
    -0.9632346106061206 + x22)^2 + (-0.9904964428766339 + x23)^2 + (
    -0.051156798506716616 + x24)^2) + x613 * ((-0.5884363239423929 + x21)^2 + (
    -0.9712278123715459 + x22)^2 + (-0.39988158182711386 + x23)^2 + (
    -0.41099930765106685 + x24)^2) + x614 * ((-0.5312213971906167 + x21)^2 + (
    -0.81785083419928 + x22)^2 + (-0.11725286157727799 + x23)^2 + (
    -0.47116385459902677 + x24)^2) + x615 * ((-0.9276992489134009 + x21)^2 + (
    -0.276293095414863 + x22)^2 + (-0.694461598585542 + x23)^2 + (
    -0.24661724253663275 + x24)^2) + x616 * ((-0.8984827464797928 + x21)^2 + (
    -0.8392110392495009 + x22)^2 + (-0.29003442507035804 + x23)^2 + (
    -0.7169574587131787 + x24)^2) + x617 * ((-0.7178579817600614 + x21)^2 + (
    -0.5442760502478915 + x22)^2 + (-0.3613660892547932 + x23)^2 + (
    -0.8887949357847075 + x24)^2) + x618 * ((-0.20832626177371294 + x21)^2 + (
    -0.6155556242775743 + x22)^2 + (-0.24252949041723848 + x23)^2 + (
    -0.5435125865130096 + x24)^2) + x619 * ((-0.6309807709209095 + x21)^2 + (
    -0.3784634566348025 + x22)^2 + (-0.39906901089542124 + x23)^2 + (
    -0.4255257271419496 + x24)^2) + x620 * ((-0.2531527659499414 + x21)^2 + (
    -0.3939338403635574 + x22)^2 + (-0.24367103431275294 + x23)^2 + (
    -0.09965076327279909 + x24)^2) + x621 * ((-0.4613429383834692 + x21)^2 + (
    -0.3270734410373959 + x22)^2 + (-0.3721913332914448 + x23)^2 + (
    -0.8397998489632109 + x24)^2) + x622 * ((-0.38125619155081125 + x21)^2 + (
    -0.38637355155860587 + x22)^2 + (-0.48242666628327 + x23)^2 + (
    -0.09841931704125129 + x24)^2) + x623 * ((-0.8312772318196014 + x21)^2 + (
    -0.8386805111720071 + x22)^2 + (-0.7116803614743081 + x23)^2 + (
    -0.1685702196156904 + x24)^2) + x624 * ((-0.9799547522897909 + x21)^2 + (
    -0.833448605810144 + x22)^2 + (-0.8740694081049383 + x23)^2 + (
    -0.6506828607108437 + x24)^2) + x625 * ((-0.1607430602427229 + x21)^2 + (
    -0.9407888153270746 + x22)^2 + (-0.6263933433327887 + x23)^2 + (
    -0.749780063323727 + x24)^2) + x626 * ((-0.7159349886520615 + x21)^2 + (
    -0.5782176711798136 + x22)^2 + (-0.2549127897200829 + x23)^2 + (
    -0.2942758616813056 + x24)^2) + x627 * ((-0.2937946995191628 + x21)^2 + (
    -0.7467755231646197 + x22)^2 + (-0.12056041976861509 + x23)^2 + (
    -0.6656163636347733 + x24)^2) + x628 * ((-0.1391657590641412 + x21)^2 + (
    -0.7998527624894191 + x22)^2 + (-0.8268662401101857 + x23)^2 + (
    -0.33882597292525984 + x24)^2) + x629 * ((-0.6582625122649799 + x25)^2 + (
    -0.10362896941145872 + x26)^2 + (-0.8195797598856802 + x27)^2 + (
    -0.5422289997742272 + x28)^2) + x630 * ((-0.3661207081728268 + x25)^2 + (
    -0.7480408210929997 + x26)^2 + (-0.6813605839850432 + x27)^2 + (
    -0.5056692315871436 + x28)^2) + x631 * ((-0.07046798157590661 + x25)^2 + (
    -0.5775220724425275 + x26)^2 + (-0.7916097196998284 + x27)^2 + (
    -0.9106301943747759 + x28)^2) + x632 * ((-0.9143624080891343 + x25)^2 + (
    -0.5102176451888726 + x26)^2 + (-0.46023708546130926 + x27)^2 + (
    -0.21559477969887786 + x28)^2) + x633 * ((-0.2152968191062874 + x25)^2 + (
    -0.40849216327387305 + x26)^2 + (-0.20734483145145233 + x27)^2 + (
    -0.29299530170003807 + x28)^2) + x634 * ((-0.753381482947803 + x25)^2 + (
    -0.569021356481719 + x26)^2 + (-0.825772931187451 + x27)^2 + (
    -0.6717803623991925 + x28)^2) + x635 * ((-0.22558272825834902 + x25)^2 + (
    -0.1431433457263549 + x26)^2 + (-0.36496670173321977 + x27)^2 + (
    -0.8283121504397382 + x28)^2) + x636 * ((-0.1043150551410561 + x25)^2 + (
    -0.5878900110989006 + x26)^2 + (-0.9303409193762857 + x27)^2 + (
    -0.1857245451574967 + x28)^2) + x637 * ((-0.2569777266497605 + x25)^2 + (
    -0.44043166993274085 + x26)^2 + (-0.15843257127556898 + x27)^2 + (
    -0.952596167014909 + x28)^2) + x638 * ((-0.767248128715498 + x25)^2 + (
    -0.16237189449331368 + x26)^2 + (-0.06342633508651152 + x27)^2 + (
    -0.8024171562438219 + x28)^2) + x639 * ((-0.7172302300642502 + x25)^2 + (
    -0.3391758201292703 + x26)^2 + (-0.030384935563099513 + x27)^2 + (
    -0.06493483472263029 + x28)^2) + x640 * ((-0.3661672203776154 + x25)^2 + (
    -0.9542180221871335 + x26)^2 + (-0.5308186536817474 + x27)^2 + (
    -0.16997124480838255 + x28)^2) + x641 * ((-0.23659736779603846 + x25)^2 + (
    -0.6214607353719023 + x26)^2 + (-0.3081993619295993 + x27)^2 + (
    -0.3526409606385007 + x28)^2) + x642 * ((-0.9752782586626233 + x25)^2 + (
    -0.5844650261883885 + x26)^2 + (-0.37649426913773276 + x27)^2 + (
    -0.10816991983567104 + x28)^2) + x643 * ((-0.45932686546602697 + x25)^2 + (
    -0.21233217626711853 + x26)^2 + (-0.9164032346567896 + x27)^2 + (
    -0.37108439943759797 + x28)^2) + x644 * ((-0.6867210427728082 + x25)^2 + (
    -0.7796854955112769 + x26)^2 + (-0.11982168093807799 + x27)^2 + (
    -0.6159743897209107 + x28)^2) + x645 * ((-0.985368764646874 + x25)^2 + (
    -0.07384180286280495 + x26)^2 + (-0.12212817800129094 + x27)^2 + (
    -0.2984771462799074 + x28)^2) + x646 * ((-0.7476106092305221 + x25)^2 + (
    -0.4411310968444404 + x26)^2 + (-0.5921500130284744 + x27)^2 + (
    -0.4842613828145912 + x28)^2) + x647 * ((-0.9737472353802095 + x25)^2 + (
    -0.09330122936543495 + x26)^2 + (-0.6050695157211611 + x27)^2 + (
    -0.07252152451660332 + x28)^2) + x648 * ((-0.09013540585240642 + x25)^2 + (
    -0.31276776356555547 + x26)^2 + (-0.7994057211441843 + x27)^2 + (
    -0.22689981649412638 + x28)^2) + x649 * ((-0.6283164056152335 + x25)^2 + (
    -0.3785737682752087 + x26)^2 + (-0.0024714258559164204 + x27)^2 + (
    -0.8148514253118784 + x28)^2) + x650 * ((-0.45370880893982724 + x25)^2 + (
    -0.10391203375848834 + x26)^2 + (-0.24027615267372093 + x27)^2 + (
    -0.2552645467206819 + x28)^2) + x651 * ((-0.4061008020592297 + x25)^2 + (
    -0.9396418294747921 + x26)^2 + (-0.5690658238794261 + x27)^2 + (
    -0.16866076993955403 + x28)^2) + x652 * ((-0.2314528417813161 + x25)^2 + (
    -0.5525474743329635 + x26)^2 + (-0.24649406583643063 + x27)^2 + (
    -0.9613520728571585 + x28)^2) + x653 * ((-0.5139605500157903 + x25)^2 + (
    -0.6815512588331698 + x26)^2 + (-0.16796296820903867 + x27)^2 + (
    -0.7162074865739461 + x28)^2) + x654 * ((-0.7706393889182662 + x25)^2 + (
    -0.43003110845525816 + x26)^2 + (-0.9356475551939986 + x27)^2 + (
    -0.5933795966331403 + x28)^2) + x655 * ((-0.5249118669899329 + x25)^2 + (
    -0.04056638284243541 + x26)^2 + (-0.0768970587722112 + x27)^2 + (
    -0.8247484594687006 + x28)^2) + x656 * ((-0.824923342468354 + x25)^2 + (
    -0.24405019701972253 + x26)^2 + (-0.38404505866575367 + x27)^2 + (
    -0.8313733189621139 + x28)^2) + x657 * ((-0.33950374022026997 + x25)^2 + (
    -0.5976095637618721 + x26)^2 + (-0.7602631636886854 + x27)^2 + (
    -0.4500249936588927 + x28)^2) + x658 * ((-0.523162910024812 + x25)^2 + (
    -0.3436248527141411 + x26)^2 + (-0.4561418310928951 + x27)^2 + (
    -0.8742103555752229 + x28)^2) + x659 * ((-0.3337530963427443 + x25)^2 + (
    -0.9855745242910374 + x26)^2 + (-0.9617621389771519 + x27)^2 + (
    -0.22441530334931115 + x28)^2) + x660 * ((-0.25477260253407985 + x25)^2 + (
    -0.3657617338278605 + x26)^2 + (-0.4599755066722203 + x27)^2 + (
    -0.488019659535353 + x28)^2) + x661 * ((-0.2663904007493795 + x25)^2 + (
    -0.27222258016843315 + x26)^2 + (-0.2880874179930988 + x27)^2 + (
    -0.02481848847156809 + x28)^2) + x662 * ((-0.2075297065152052 + x25)^2 + (
    -0.7022983060607665 + x26)^2 + (-0.47827086724608314 + x27)^2 + (
    -0.28622027057302846 + x28)^2) + x663 * ((-0.7047452543816871 + x25)^2 + (
    -0.6996554684275655 + x26)^2 + (-0.16578869005033847 + x27)^2 + (
    -0.5179151157105838 + x28)^2) + x664 * ((-0.7436571093571753 + x25)^2 + (
    -0.8723672259073825 + x26)^2 + (-0.9145540584909153 + x27)^2 + (
    -0.4616843537475913 + x28)^2) + x665 * ((-0.40078313938185106 + x25)^2 + (
    -0.7616315326378316 + x26)^2 + (-0.0624885237314553 + x27)^2 + (
    -0.33349386555475435 + x28)^2) + x666 * ((-0.47083964839087056 + x25)^2 + (
    -0.7540812887396847 + x26)^2 + (-0.7698437223374434 + x27)^2 + (
    -0.7260097297577066 + x28)^2) + x667 * ((-0.470591984548581 + x25)^2 + (
    -0.21419699662552538 + x26)^2 + (-0.8214784727628405 + x27)^2 + (
    -0.9327146275722538 + x28)^2) + x668 * ((-0.6694092237740207 + x25)^2 + (
    -0.40188436538160965 + x26)^2 + (-0.9078829021652501 + x27)^2 + (
    -0.28882880291122615 + x28)^2) + x669 * ((-0.8012821680592233 + x25)^2 + (
    -0.26764801084685064 + x26)^2 + (-0.8907563902239161 + x27)^2 + (
    -0.022670562427511642 + x28)^2) + x670 * ((-0.3149563708936517 + x25)^2 + (
    -0.4013573755930997 + x26)^2 + (-0.16444723142036033 + x27)^2 + (
    -0.8783064548569166 + x28)^2) + x671 * ((-0.0452536291694966 + x25)^2 + (
    -0.6030683870184952 + x26)^2 + (-0.12061018849928773 + x27)^2 + (
    -0.6161186728209969 + x28)^2) + x672 * ((-0.8303237648967787 + x25)^2 + (
    -0.7542211701244139 + x26)^2 + (-0.47189785643150806 + x27)^2 + (
    -0.7928252514256884 + x28)^2) + x673 * ((-0.6429343022480377 + x25)^2 + (
    -0.6021334537878723 + x26)^2 + (-0.2852218418361189 + x27)^2 + (
    -0.29825945641738283 + x28)^2) + x674 * ((-0.11776074988832852 + x25)^2 + (
    -0.8643957197110975 + x26)^2 + (-0.03338227312045139 + x27)^2 + (
    -0.593939114377175 + x28)^2) + x675 * ((-0.418497245301816 + x25)^2 + (
    -0.3081055339744846 + x26)^2 + (-0.38130196746434064 + x27)^2 + (
    -0.6612469720321472 + x28)^2) + x676 * ((-0.5815493986252239 + x25)^2 + (
    -0.6811102264085155 + x26)^2 + (-0.1453934105814335 + x27)^2 + (
    -0.8013757499531303 + x28)^2) + x677 * ((-0.00607035083945795 + x25)^2 + (
    -0.053561905123383324 + x26)^2 + (-0.7817703845300363 + x27)^2 + (
    -0.5662212686106933 + x28)^2) + x678 * ((-0.6950221994466669 + x25)^2 + (
    -0.2105034885347269 + x26)^2 + (-0.11287315442891777 + x27)^2 + (
    -0.010597472308638611 + x28)^2) + x679 * ((-0.5311582701895528 + x25)^2 + (
    -0.4320063664214896 + x26)^2 + (-0.2729049031820855 + x27)^2 + (
    -0.2214949427555688 + x28)^2) + x680 * ((-0.48150146533157034 + x25)^2 + (
    -0.46067276862424755 + x26)^2 + (-0.0056974073880511344 + x27)^2 + (
    -0.35728414461795144 + x28)^2) + x681 * ((-0.9429852300228826 + x25)^2 + (
    -0.39303494745904877 + x26)^2 + (-0.31011214177569657 + x27)^2 + (
    -0.018438339560493344 + x28)^2) + x682 * ((-0.5322977536893222 + x25)^2 + (
    -0.9652470893187132 + x26)^2 + (-0.21135139952422877 + x27)^2 + (
    -0.8156809600304314 + x28)^2) + x683 * ((-0.03401283459710902 + x25)^2 + (
    -0.806892267442106 + x26)^2 + (-0.8489758888126404 + x27)^2 + (
    -0.6111483840787582 + x28)^2) + x684 * ((-0.9264484533738693 + x25)^2 + (
    -0.14876976743207326 + x26)^2 + (-0.9758190264647324 + x27)^2 + (
    -0.6811285636971497 + x28)^2) + x685 * ((-0.9647303094099035 + x25)^2 + (
    -0.7010206460934956 + x26)^2 + (-0.30943177373448516 + x27)^2 + (
    -0.1891022383766483 + x28)^2) + x686 * ((-0.4769220240119476 + x25)^2 + (
    -0.822318413841706 + x26)^2 + (-0.1393694419930549 + x27)^2 + (
    -0.9724217562379036 + x28)^2) + x687 * ((-0.7455477334590928 + x25)^2 + (
    -0.563396428008588 + x26)^2 + (-0.22992430827076737 + x27)^2 + (
    -0.2370557772132338 + x28)^2) + x688 * ((-0.16535109726174313 + x25)^2 + (
    -0.9547852441919761 + x26)^2 + (-0.3203072223564828 + x27)^2 + (
    -0.42492616349386114 + x28)^2) + x689 * ((-0.7834231836651542 + x25)^2 + (
    -0.24935541853121224 + x26)^2 + (-0.8297208826099771 + x27)^2 + (
    -0.23563563513419228 + x28)^2) + x690 * ((-0.8373741924252092 + x25)^2 + (
    -0.36970144853956455 + x26)^2 + (-0.5671956111716981 + x27)^2 + (
    -0.3691960678174552 + x28)^2) + x691 * ((-0.39886787270583346 + x25)^2 + (
    -0.650964776918859 + x26)^2 + (-0.640819546256607 + x27)^2 + (
    -0.09882188475998765 + x28)^2) + x692 * ((-0.5157745663985024 + x25)^2 + (
    -0.5435336580091097 + x26)^2 + (-0.27430425498315725 + x27)^2 + (
    -0.7274939676197051 + x28)^2) + x693 * ((-0.537162865589002 + x25)^2 + (
    -0.5913784936821398 + x26)^2 + (-0.45466522772907525 + x27)^2 + (
    -0.1047184477665718 + x28)^2) + x694 * ((-0.04102323848681244 + x25)^2 + (
    -0.5377574929590462 + x26)^2 + (-0.9782258268406425 + x27)^2 + (
    -0.9716171817066379 + x28)^2) + x695 * ((-0.6871600172780726 + x25)^2 + (
    -0.8418720435526559 + x26)^2 + (-0.83052769064337 + x27)^2 + (
    -0.8985953589244926 + x28)^2) + x696 * ((-0.10160325017586314 + x25)^2 + (
    -0.8817097435158873 + x26)^2 + (-0.2972532110491476 + x27)^2 + (
    -0.34330327059943233 + x28)^2) + x697 * ((-0.276256004491218 + x25)^2 + (
    -0.9717101669718731 + x26)^2 + (-0.2984317666596268 + x27)^2 + (
    -0.4440796331949195 + x28)^2) + x698 * ((-0.9523516045369547 + x25)^2 + (
    -0.6811203295261851 + x26)^2 + (-0.17487173576269888 + x27)^2 + (
    -0.264608767198526 + x28)^2) + x699 * ((-0.5950072414516107 + x25)^2 + (
    -0.19863608495271834 + x26)^2 + (-0.3254107876389821 + x27)^2 + (
    -0.8432385372383167 + x28)^2) + x700 * ((-0.8468632268868022 + x25)^2 + (
    -0.07323866891200903 + x26)^2 + (-0.8068985989515749 + x27)^2 + (
    -0.6810798779677064 + x28)^2) + x701 * ((-0.4712188830735816 + x25)^2 + (
    -0.4135054120302819 + x26)^2 + (-0.3077078179033642 + x27)^2 + (
    -0.3353457462826305 + x28)^2) + x702 * ((-0.31701343040014285 + x25)^2 + (
    -0.6308301684094946 + x26)^2 + (-0.5476747635071102 + x27)^2 + (
    -0.26992487329332904 + x28)^2) + x703 * ((-0.19701342670354327 + x25)^2 + (
    -0.4781921949933534 + x26)^2 + (-0.7057141592764116 + x27)^2 + (
    -0.0896309852595556 + x28)^2) + x704 * ((-0.8038878371618275 + x25)^2 + (
    -0.044329635856571015 + x26)^2 + (-0.898513730220423 + x27)^2 + (
    -0.5600362942589316 + x28)^2) + x705 * ((-0.14961294077862985 + x25)^2 + (
    -0.9772469188459079 + x26)^2 + (-0.12015140801504265 + x27)^2 + (
    -0.521329056759319 + x28)^2) + x706 * ((-0.03381103052182122 + x25)^2 + (
    -0.527498561244566 + x26)^2 + (-0.44345060645273227 + x27)^2 + (
    -0.006260254814196675 + x28)^2) + x707 * ((-0.8219788276317623 + x25)^2 + (
    -0.3852922260631585 + x26)^2 + (-0.9620135163986219 + x27)^2 + (
    -0.18635183396741328 + x28)^2) + x708 * ((-0.7389415908359858 + x25)^2 + (
    -0.523761972701124 + x26)^2 + (-0.46623643584676433 + x27)^2 + (
    -0.0580789763043309 + x28)^2) + x709 * ((-0.5180391196124703 + x25)^2 + (
    -0.125977305519825 + x26)^2 + (-0.7141405174792315 + x27)^2 + (
    -0.6913703129848836 + x28)^2) + x710 * ((-0.26351088593273375 + x25)^2 + (
    -0.45761632800962093 + x26)^2 + (-0.7832055136876419 + x27)^2 + (
    -0.13621640940288493 + x28)^2) + x711 * ((-0.471522719293638 + x25)^2 + (
    -0.6233304917288576 + x26)^2 + (-0.9541794868794985 + x27)^2 + (
    -0.8015112028077606 + x28)^2) + x712 * ((-0.602523335859397 + x25)^2 + (
    -0.9632346106061206 + x26)^2 + (-0.9904964428766339 + x27)^2 + (
    -0.051156798506716616 + x28)^2) + x713 * ((-0.5884363239423929 + x25)^2 + (
    -0.9712278123715459 + x26)^2 + (-0.39988158182711386 + x27)^2 + (
    -0.41099930765106685 + x28)^2) + x714 * ((-0.5312213971906167 + x25)^2 + (
    -0.81785083419928 + x26)^2 + (-0.11725286157727799 + x27)^2 + (
    -0.47116385459902677 + x28)^2) + x715 * ((-0.9276992489134009 + x25)^2 + (
    -0.276293095414863 + x26)^2 + (-0.694461598585542 + x27)^2 + (
    -0.24661724253663275 + x28)^2) + x716 * ((-0.8984827464797928 + x25)^2 + (
    -0.8392110392495009 + x26)^2 + (-0.29003442507035804 + x27)^2 + (
    -0.7169574587131787 + x28)^2) + x717 * ((-0.7178579817600614 + x25)^2 + (
    -0.5442760502478915 + x26)^2 + (-0.3613660892547932 + x27)^2 + (
    -0.8887949357847075 + x28)^2) + x718 * ((-0.20832626177371294 + x25)^2 + (
    -0.6155556242775743 + x26)^2 + (-0.24252949041723848 + x27)^2 + (
    -0.5435125865130096 + x28)^2) + x719 * ((-0.6309807709209095 + x25)^2 + (
    -0.3784634566348025 + x26)^2 + (-0.39906901089542124 + x27)^2 + (
    -0.4255257271419496 + x28)^2) + x720 * ((-0.2531527659499414 + x25)^2 + (
    -0.3939338403635574 + x26)^2 + (-0.24367103431275294 + x27)^2 + (
    -0.09965076327279909 + x28)^2) + x721 * ((-0.4613429383834692 + x25)^2 + (
    -0.3270734410373959 + x26)^2 + (-0.3721913332914448 + x27)^2 + (
    -0.8397998489632109 + x28)^2) + x722 * ((-0.38125619155081125 + x25)^2 + (
    -0.38637355155860587 + x26)^2 + (-0.48242666628327 + x27)^2 + (
    -0.09841931704125129 + x28)^2) + x723 * ((-0.8312772318196014 + x25)^2 + (
    -0.8386805111720071 + x26)^2 + (-0.7116803614743081 + x27)^2 + (
    -0.1685702196156904 + x28)^2) + x724 * ((-0.9799547522897909 + x25)^2 + (
    -0.833448605810144 + x26)^2 + (-0.8740694081049383 + x27)^2 + (
    -0.6506828607108437 + x28)^2) + x725 * ((-0.1607430602427229 + x25)^2 + (
    -0.9407888153270746 + x26)^2 + (-0.6263933433327887 + x27)^2 + (
    -0.749780063323727 + x28)^2) + x726 * ((-0.7159349886520615 + x25)^2 + (
    -0.5782176711798136 + x26)^2 + (-0.2549127897200829 + x27)^2 + (
    -0.2942758616813056 + x28)^2) + x727 * ((-0.2937946995191628 + x25)^2 + (
    -0.7467755231646197 + x26)^2 + (-0.12056041976861509 + x27)^2 + (
    -0.6656163636347733 + x28)^2) + x728 * ((-0.1391657590641412 + x25)^2 + (
    -0.7998527624894191 + x26)^2 + (-0.8268662401101857 + x27)^2 + (
    -0.33882597292525984 + x28)^2))

@constraint(m, e1, x29 + x129 + x229 + x329 + x429 + x529 + x629 == 1)
@constraint(m, e2, x30 + x130 + x230 + x330 + x430 + x530 + x630 == 1)
@constraint(m, e3, x31 + x131 + x231 + x331 + x431 + x531 + x631 == 1)
@constraint(m, e4, x32 + x132 + x232 + x332 + x432 + x532 + x632 == 1)
@constraint(m, e5, x33 + x133 + x233 + x333 + x433 + x533 + x633 == 1)
@constraint(m, e6, x34 + x134 + x234 + x334 + x434 + x534 + x634 == 1)
@constraint(m, e7, x35 + x135 + x235 + x335 + x435 + x535 + x635 == 1)
@constraint(m, e8, x36 + x136 + x236 + x336 + x436 + x536 + x636 == 1)
@constraint(m, e9, x37 + x137 + x237 + x337 + x437 + x537 + x637 == 1)
@constraint(m, e10, x38 + x138 + x238 + x338 + x438 + x538 + x638 == 1)
@constraint(m, e11, x39 + x139 + x239 + x339 + x439 + x539 + x639 == 1)
@constraint(m, e12, x40 + x140 + x240 + x340 + x440 + x540 + x640 == 1)
@constraint(m, e13, x41 + x141 + x241 + x341 + x441 + x541 + x641 == 1)
@constraint(m, e14, x42 + x142 + x242 + x342 + x442 + x542 + x642 == 1)
@constraint(m, e15, x43 + x143 + x243 + x343 + x443 + x543 + x643 == 1)
@constraint(m, e16, x44 + x144 + x244 + x344 + x444 + x544 + x644 == 1)
@constraint(m, e17, x45 + x145 + x245 + x345 + x445 + x545 + x645 == 1)
@constraint(m, e18, x46 + x146 + x246 + x346 + x446 + x546 + x646 == 1)
@constraint(m, e19, x47 + x147 + x247 + x347 + x447 + x547 + x647 == 1)
@constraint(m, e20, x48 + x148 + x248 + x348 + x448 + x548 + x648 == 1)
@constraint(m, e21, x49 + x149 + x249 + x349 + x449 + x549 + x649 == 1)
@constraint(m, e22, x50 + x150 + x250 + x350 + x450 + x550 + x650 == 1)
@constraint(m, e23, x51 + x151 + x251 + x351 + x451 + x551 + x651 == 1)
@constraint(m, e24, x52 + x152 + x252 + x352 + x452 + x552 + x652 == 1)
@constraint(m, e25, x53 + x153 + x253 + x353 + x453 + x553 + x653 == 1)
@constraint(m, e26, x54 + x154 + x254 + x354 + x454 + x554 + x654 == 1)
@constraint(m, e27, x55 + x155 + x255 + x355 + x455 + x555 + x655 == 1)
@constraint(m, e28, x56 + x156 + x256 + x356 + x456 + x556 + x656 == 1)
@constraint(m, e29, x57 + x157 + x257 + x357 + x457 + x557 + x657 == 1)
@constraint(m, e30, x58 + x158 + x258 + x358 + x458 + x558 + x658 == 1)
@constraint(m, e31, x59 + x159 + x259 + x359 + x459 + x559 + x659 == 1)
@constraint(m, e32, x60 + x160 + x260 + x360 + x460 + x560 + x660 == 1)
@constraint(m, e33, x61 + x161 + x261 + x361 + x461 + x561 + x661 == 1)
@constraint(m, e34, x62 + x162 + x262 + x362 + x462 + x562 + x662 == 1)
@constraint(m, e35, x63 + x163 + x263 + x363 + x463 + x563 + x663 == 1)
@constraint(m, e36, x64 + x164 + x264 + x364 + x464 + x564 + x664 == 1)
@constraint(m, e37, x65 + x165 + x265 + x365 + x465 + x565 + x665 == 1)
@constraint(m, e38, x66 + x166 + x266 + x366 + x466 + x566 + x666 == 1)
@constraint(m, e39, x67 + x167 + x267 + x367 + x467 + x567 + x667 == 1)
@constraint(m, e40, x68 + x168 + x268 + x368 + x468 + x568 + x668 == 1)
@constraint(m, e41, x69 + x169 + x269 + x369 + x469 + x569 + x669 == 1)
@constraint(m, e42, x70 + x170 + x270 + x370 + x470 + x570 + x670 == 1)
@constraint(m, e43, x71 + x171 + x271 + x371 + x471 + x571 + x671 == 1)
@constraint(m, e44, x72 + x172 + x272 + x372 + x472 + x572 + x672 == 1)
@constraint(m, e45, x73 + x173 + x273 + x373 + x473 + x573 + x673 == 1)
@constraint(m, e46, x74 + x174 + x274 + x374 + x474 + x574 + x674 == 1)
@constraint(m, e47, x75 + x175 + x275 + x375 + x475 + x575 + x675 == 1)
@constraint(m, e48, x76 + x176 + x276 + x376 + x476 + x576 + x676 == 1)
@constraint(m, e49, x77 + x177 + x277 + x377 + x477 + x577 + x677 == 1)
@constraint(m, e50, x78 + x178 + x278 + x378 + x478 + x578 + x678 == 1)
@constraint(m, e51, x79 + x179 + x279 + x379 + x479 + x579 + x679 == 1)
@constraint(m, e52, x80 + x180 + x280 + x380 + x480 + x580 + x680 == 1)
@constraint(m, e53, x81 + x181 + x281 + x381 + x481 + x581 + x681 == 1)
@constraint(m, e54, x82 + x182 + x282 + x382 + x482 + x582 + x682 == 1)
@constraint(m, e55, x83 + x183 + x283 + x383 + x483 + x583 + x683 == 1)
@constraint(m, e56, x84 + x184 + x284 + x384 + x484 + x584 + x684 == 1)
@constraint(m, e57, x85 + x185 + x285 + x385 + x485 + x585 + x685 == 1)
@constraint(m, e58, x86 + x186 + x286 + x386 + x486 + x586 + x686 == 1)
@constraint(m, e59, x87 + x187 + x287 + x387 + x487 + x587 + x687 == 1)
@constraint(m, e60, x88 + x188 + x288 + x388 + x488 + x588 + x688 == 1)
@constraint(m, e61, x89 + x189 + x289 + x389 + x489 + x589 + x689 == 1)
@constraint(m, e62, x90 + x190 + x290 + x390 + x490 + x590 + x690 == 1)
@constraint(m, e63, x91 + x191 + x291 + x391 + x491 + x591 + x691 == 1)
@constraint(m, e64, x92 + x192 + x292 + x392 + x492 + x592 + x692 == 1)
@constraint(m, e65, x93 + x193 + x293 + x393 + x493 + x593 + x693 == 1)
@constraint(m, e66, x94 + x194 + x294 + x394 + x494 + x594 + x694 == 1)
@constraint(m, e67, x95 + x195 + x295 + x395 + x495 + x595 + x695 == 1)
@constraint(m, e68, x96 + x196 + x296 + x396 + x496 + x596 + x696 == 1)
@constraint(m, e69, x97 + x197 + x297 + x397 + x497 + x597 + x697 == 1)
@constraint(m, e70, x98 + x198 + x298 + x398 + x498 + x598 + x698 == 1)
@constraint(m, e71, x99 + x199 + x299 + x399 + x499 + x599 + x699 == 1)
@constraint(m, e72, x100 + x200 + x300 + x400 + x500 + x600 + x700 == 1)
@constraint(m, e73, x101 + x201 + x301 + x401 + x501 + x601 + x701 == 1)
@constraint(m, e74, x102 + x202 + x302 + x402 + x502 + x602 + x702 == 1)
@constraint(m, e75, x103 + x203 + x303 + x403 + x503 + x603 + x703 == 1)
@constraint(m, e76, x104 + x204 + x304 + x404 + x504 + x604 + x704 == 1)
@constraint(m, e77, x105 + x205 + x305 + x405 + x505 + x605 + x705 == 1)
@constraint(m, e78, x106 + x206 + x306 + x406 + x506 + x606 + x706 == 1)
@constraint(m, e79, x107 + x207 + x307 + x407 + x507 + x607 + x707 == 1)
@constraint(m, e80, x108 + x208 + x308 + x408 + x508 + x608 + x708 == 1)
@constraint(m, e81, x109 + x209 + x309 + x409 + x509 + x609 + x709 == 1)
@constraint(m, e82, x110 + x210 + x310 + x410 + x510 + x610 + x710 == 1)
@constraint(m, e83, x111 + x211 + x311 + x411 + x511 + x611 + x711 == 1)
@constraint(m, e84, x112 + x212 + x312 + x412 + x512 + x612 + x712 == 1)
@constraint(m, e85, x113 + x213 + x313 + x413 + x513 + x613 + x713 == 1)
@constraint(m, e86, x114 + x214 + x314 + x414 + x514 + x614 + x714 == 1)
@constraint(m, e87, x115 + x215 + x315 + x415 + x515 + x615 + x715 == 1)
@constraint(m, e88, x116 + x216 + x316 + x416 + x516 + x616 + x716 == 1)
@constraint(m, e89, x117 + x217 + x317 + x417 + x517 + x617 + x717 == 1)
@constraint(m, e90, x118 + x218 + x318 + x418 + x518 + x618 + x718 == 1)
@constraint(m, e91, x119 + x219 + x319 + x419 + x519 + x619 + x719 == 1)
@constraint(m, e92, x120 + x220 + x320 + x420 + x520 + x620 + x720 == 1)
@constraint(m, e93, x121 + x221 + x321 + x421 + x521 + x621 + x721 == 1)
@constraint(m, e94, x122 + x222 + x322 + x422 + x522 + x622 + x722 == 1)
@constraint(m, e95, x123 + x223 + x323 + x423 + x523 + x623 + x723 == 1)
@constraint(m, e96, x124 + x224 + x324 + x424 + x524 + x624 + x724 == 1)
@constraint(m, e97, x125 + x225 + x325 + x425 + x525 + x625 + x725 == 1)
@constraint(m, e98, x126 + x226 + x326 + x426 + x526 + x626 + x726 == 1)
@constraint(m, e99, x127 + x227 + x327 + x427 + x527 + x627 + x727 == 1)
@constraint(m, e100, x128 + x228 + x328 + x428 + x528 + x628 + x728 == 1)
