# NLP written by GAMS Convert at 05/15/24 11:36:20
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       100      100        0        0        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#       618      618        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       600      600        0
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

@NLobjective(m, Min, x19 * ((-0.42984003511582325 + x1)^2 + (
    -0.5248188211614745 + x2)^2 + (-0.18976547031166158 + x3)^2) + x20 * ((
    -0.7635437892676484 + x1)^2 + (-0.2087128118532261 + x2)^2 + (
    -0.7237865537648877 + x3)^2) + x21 * ((-0.37894209230263076 + x1)^2 + (
    -0.673972806556101 + x2)^2 + (-0.7804374363770062 + x3)^2) + x22 * ((
    -0.03600961414337911 + x1)^2 + (-0.9432908341465497 + x2)^2 + (
    -0.056683718162081176 + x3)^2) + x23 * ((-0.9007184159570817 + x1)^2 + (
    -0.0739499095247852 + x2)^2 + (-0.8655569455322819 + x3)^2) + x24 * ((
    -0.5768605519499145 + x1)^2 + (-0.5986981803675213 + x2)^2 + (
    -0.6570355091518676 + x3)^2) + x25 * ((-0.9745811766548338 + x1)^2 + (
    -0.41474680749048254 + x2)^2 + (-0.9237263978620873 + x3)^2) + x26 * ((
    -0.06206593318927589 + x1)^2 + (-0.2651214371091045 + x2)^2 + (
    -0.6015632454359485 + x3)^2) + x27 * ((-0.6112553172986112 + x1)^2 + (
    -0.8236130985530066 + x2)^2 + (-0.7552731749526171 + x3)^2) + x28 * ((
    -0.2824557711903295 + x1)^2 + (-0.3301346471734301 + x2)^2 + (
    -0.4003642371172418 + x3)^2) + x29 * ((-0.22380220476030066 + x1)^2 + (
    -0.8814483924491749 + x2)^2 + (-0.880102192625681 + x3)^2) + x30 * ((
    -0.5378330969721621 + x1)^2 + (-0.5263672319237694 + x2)^2 + (
    -0.008305374485281347 + x3)^2) + x31 * ((-0.8368636165739145 + x1)^2 + (
    -0.5178975931573176 + x2)^2 + (-0.19654398351590685 + x3)^2) + x32 * ((
    -0.8033599255036961 + x1)^2 + (-0.5470921616898407 + x2)^2 + (
    -0.05989580899877456 + x3)^2) + x33 * ((-0.5041669891441031 + x1)^2 + (
    -0.19483851577422762 + x2)^2 + (-0.04121006383916248 + x3)^2) + x34 * ((
    -0.2735550274413898 + x1)^2 + (-0.5771711903673603 + x2)^2 + (
    -0.8483920722526949 + x3)^2) + x35 * ((-0.16341280932131008 + x1)^2 + (
    -0.38595898916250637 + x2)^2 + (-0.7240527965923388 + x3)^2) + x36 * ((
    -0.184735914655195 + x1)^2 + (-0.9074851747165764 + x2)^2 + (
    -0.5092578035597556 + x3)^2) + x37 * ((-0.667717591753409 + x1)^2 + (
    -0.03611089878214757 + x2)^2 + (-0.5314088140520232 + x3)^2) + x38 * ((
    -0.22082508524283118 + x1)^2 + (-0.14591083104017755 + x2)^2 + (
    -0.4966365264689938 + x3)^2) + x39 * ((-0.8131501378134828 + x1)^2 + (
    -0.12233837490110344 + x2)^2 + (-0.6422164007166057 + x3)^2) + x40 * ((
    -0.5093801089140564 + x1)^2 + (-0.5913076324087453 + x2)^2 + (
    -0.22564192034703445 + x3)^2) + x41 * ((-0.5886418065986404 + x1)^2 + (
    -0.051216403584171344 + x2)^2 + (-0.21124855487984584 + x3)^2) + x42 * ((
    -0.2822083632452721 + x1)^2 + (-0.6609969862369512 + x2)^2 + (
    -0.629237720221342 + x3)^2) + x43 * ((-0.800850840990083 + x1)^2 + (
    -0.2946478937198632 + x2)^2 + (-0.9711075538538692 + x3)^2) + x44 * ((
    -0.18106474877236667 + x1)^2 + (-0.40222650110712255 + x2)^2 + (
    -0.8640061178144425 + x3)^2) + x45 * ((-0.275960867663125 + x1)^2 + (
    -0.8101752183427954 + x2)^2 + (-0.25463108721162286 + x3)^2) + x46 * ((
    -0.09762964668322405 + x1)^2 + (-0.5681164167758985 + x2)^2 + (
    -0.8522588975167438 + x3)^2) + x47 * ((-0.6792262546121857 + x1)^2 + (
    -0.5415479570871046 + x2)^2 + (-0.9198959530376973 + x3)^2) + x48 * ((
    -0.35974899392373416 + x1)^2 + (-0.9692174411067974 + x2)^2 + (
    -0.8173895217629372 + x3)^2) + x49 * ((-0.2775683808009408 + x1)^2 + (
    -0.07111011846817805 + x2)^2 + (-0.9119005527157927 + x3)^2) + x50 * ((
    -0.8728420280238173 + x1)^2 + (-0.4810753656025001 + x2)^2 + (
    -0.5690581714245571 + x3)^2) + x51 * ((-0.3697310611408884 + x1)^2 + (
    -0.8009586582771799 + x2)^2 + (-0.4509367154437284 + x3)^2) + x52 * ((
    -0.40344052086211035 + x1)^2 + (-0.4549860124364724 + x2)^2 + (
    -0.6928018828898217 + x3)^2) + x53 * ((-0.6361863652853047 + x1)^2 + (
    -0.08988225677383088 + x2)^2 + (-0.25890016105768476 + x3)^2) + x54 * ((
    -0.5670078574144451 + x1)^2 + (-0.11962369435126274 + x2)^2 + (
    -0.7694906824065785 + x3)^2) + x55 * ((-0.2970981185523963 + x1)^2 + (
    -0.07089711937031118 + x2)^2 + (-0.3726754551130945 + x3)^2) + x56 * ((
    -0.9463316541147765 + x1)^2 + (-0.5815980777027693 + x2)^2 + (
    -0.09183246305662951 + x3)^2) + x57 * ((-0.4971616963185841 + x1)^2 + (
    -0.5526690085093273 + x2)^2 + (-0.041586056367461044 + x3)^2) + x58 * ((
    -0.48472198232839325 + x1)^2 + (-0.5137822134278897 + x2)^2 + (
    -0.25761582576168296 + x3)^2) + x59 * ((-0.44694684190755307 + x1)^2 + (
    -0.9335294451364397 + x2)^2 + (-0.6212310214093625 + x3)^2) + x60 * ((
    -0.5456179874167029 + x1)^2 + (-0.6257723725570918 + x2)^2 + (
    -0.44030482106573443 + x3)^2) + x61 * ((-0.48291634635300573 + x1)^2 + (
    -0.8500599447417776 + x2)^2 + (-0.8150332638475819 + x3)^2) + x62 * ((
    -0.2076752515318323 + x1)^2 + (-0.851790218430218 + x2)^2 + (
    -0.03852729140159916 + x3)^2) + x63 * ((-0.6321580948524517 + x1)^2 + (
    -0.9837962600945337 + x2)^2 + (-0.6794575866782234 + x3)^2) + x64 * ((
    -0.4741167244817951 + x1)^2 + (-0.7294796721116216 + x2)^2 + (
    -0.320613514728746 + x3)^2) + x65 * ((-0.4456710628183016 + x1)^2 + (
    -0.7380410763666608 + x2)^2 + (-0.38742562758632604 + x3)^2) + x66 * ((
    -0.4265716203395923 + x1)^2 + (-0.7118497351712431 + x2)^2 + (
    -0.7471218555436548 + x3)^2) + x67 * ((-0.23627512847494803 + x1)^2 + (
    -0.5038323922445893 + x2)^2 + (-0.2680376794418369 + x3)^2) + x68 * ((
    -0.8404317556608962 + x1)^2 + (-0.04318546277231472 + x2)^2 + (
    -0.14297270654389005 + x3)^2) + x69 * ((-0.6081062742820188 + x1)^2 + (
    -0.05792573185555616 + x2)^2 + (-0.30572046931736474 + x3)^2) + x70 * ((
    -0.8279542917657221 + x1)^2 + (-0.40201952243043027 + x2)^2 + (
    -0.9469372713050586 + x3)^2) + x71 * ((-0.3415766860940366 + x1)^2 + (
    -0.7667328034595803 + x2)^2 + (-0.5561511348714728 + x3)^2) + x72 * ((
    -0.8766850760174327 + x1)^2 + (-0.47568865268531624 + x2)^2 + (
    -0.9457622702235593 + x3)^2) + x73 * ((-0.060732953253662125 + x1)^2 + (
    -0.43044333590426787 + x2)^2 + (-0.11068204021696582 + x3)^2) + x74 * ((
    -0.5599647447657621 + x1)^2 + (-0.20168813274597885 + x2)^2 + (
    -0.04901731419867861 + x3)^2) + x75 * ((-0.918340292529652 + x1)^2 + (
    -0.3592948253121985 + x2)^2 + (-0.27641861869779194 + x3)^2) + x76 * ((
    -0.2290803422518174 + x1)^2 + (-0.9550196585033648 + x2)^2 + (
    -0.18525883987424996 + x3)^2) + x77 * ((-0.07874295854309366 + x1)^2 + (
    -0.5872376176569806 + x2)^2 + (-0.9964507911035481 + x3)^2) + x78 * ((
    -0.8366839476155882 + x1)^2 + (-0.48096052774158937 + x2)^2 + (
    -0.06875812181004981 + x3)^2) + x79 * ((-0.1646012318827148 + x1)^2 + (
    -0.8255025770989258 + x2)^2 + (-0.5425920043205046 + x3)^2) + x80 * ((
    -0.01206407820830957 + x1)^2 + (-0.7715259933915151 + x2)^2 + (
    -0.8153035946330994 + x3)^2) + x81 * ((-0.656216971146405 + x1)^2 + (
    -0.5038530509474157 + x2)^2 + (-0.24858472460284653 + x3)^2) + x82 * ((
    -0.5909087410955904 + x1)^2 + (-0.24200083344880052 + x2)^2 + (
    -0.2773029284079601 + x3)^2) + x83 * ((-0.30683539741159116 + x1)^2 + (
    -0.1592566555556567 + x2)^2 + (-0.8741709441944726 + x3)^2) + x84 * ((
    -0.9696553356372961 + x1)^2 + (-0.5092140919799073 + x2)^2 + (
    -0.9667357424486342 + x3)^2) + x85 * ((-0.022500436859610784 + x1)^2 + (
    -0.09449938113730139 + x2)^2 + (-0.8914880525816652 + x3)^2) + x86 * ((
    -0.03312939739236054 + x1)^2 + (-0.901942581170032 + x2)^2 + (
    -0.4786651787509474 + x3)^2) + x87 * ((-0.9087943615369551 + x1)^2 + (
    -0.16708419935758345 + x2)^2 + (-0.49548708669584307 + x3)^2) + x88 * ((
    -0.2797850906327509 + x1)^2 + (-0.6710488947711567 + x2)^2 + (
    -0.9586698953495221 + x3)^2) + x89 * ((-0.7571140653627548 + x1)^2 + (
    -0.9772776196167088 + x2)^2 + (-0.545818457398843 + x3)^2) + x90 * ((
    -0.4393881718780316 + x1)^2 + (-0.30502275122869604 + x2)^2 + (
    -0.46993652125745644 + x3)^2) + x91 * ((-0.8328586457197023 + x1)^2 + (
    -0.4665403743372396 + x2)^2 + (-0.044871269867679975 + x3)^2) + x92 * ((
    -0.200399479778539 + x1)^2 + (-0.5930767654991737 + x2)^2 + (
    -0.8532214199144125 + x3)^2) + x93 * ((-0.6635666941849311 + x1)^2 + (
    -0.23391286076708295 + x2)^2 + (-0.4140175544317234 + x3)^2) + x94 * ((
    -0.8017608133257321 + x1)^2 + (-0.8877780696226963 + x2)^2 + (
    -0.7221004582069167 + x3)^2) + x95 * ((-0.7399476414219266 + x1)^2 + (
    -0.7138733629252807 + x2)^2 + (-0.40138791158993503 + x3)^2) + x96 * ((
    -0.505308046012709 + x1)^2 + (-0.050203195063672656 + x2)^2 + (
    -0.047366160401361546 + x3)^2) + x97 * ((-0.16774593722409648 + x1)^2 + (
    -0.6409647710984233 + x2)^2 + (-0.10357005758294846 + x3)^2) + x98 * ((
    -0.831240181700394 + x1)^2 + (-0.8086369689577492 + x2)^2 + (
    -0.8697211693425991 + x3)^2) + x99 * ((-0.9508107670055634 + x1)^2 + (
    -0.6593445284740111 + x2)^2 + (-0.9654494903581963 + x3)^2) + x100 * ((
    -0.9689135289592058 + x1)^2 + (-0.2919924557860033 + x2)^2 + (
    -0.674556583609974 + x3)^2) + x101 * ((-0.5755637731737744 + x1)^2 + (
    -0.029158659146738986 + x2)^2 + (-0.801474333934095 + x3)^2) + x102 * ((
    -0.8814332005944923 + x1)^2 + (-0.9388442894563516 + x2)^2 + (
    -0.2609463697280877 + x3)^2) + x103 * ((-0.21089837943522027 + x1)^2 + (
    -0.339246197282862 + x2)^2 + (-0.3206846661656354 + x3)^2) + x104 * ((
    -0.1546689851574372 + x1)^2 + (-0.9006244078114634 + x2)^2 + (
    -0.383032353156448 + x3)^2) + x105 * ((-0.8898729322311727 + x1)^2 + (
    -0.4755652980462777 + x2)^2 + (-0.22139675941977732 + x3)^2) + x106 * ((
    -0.09681202208693973 + x1)^2 + (-0.5759917076295475 + x2)^2 + (
    -0.5453594292179953 + x3)^2) + x107 * ((-0.22092996837157597 + x1)^2 + (
    -0.46898066660462867 + x2)^2 + (-0.586705478616356 + x3)^2) + x108 * ((
    -0.7772286323779445 + x1)^2 + (-0.19088116193826554 + x2)^2 + (
    -0.856917751975287 + x3)^2) + x109 * ((-0.5698804350762819 + x1)^2 + (
    -0.6223743600871902 + x2)^2 + (-0.8005394562016571 + x3)^2) + x110 * ((
    -0.8378639929136145 + x1)^2 + (-0.2593791410480174 + x2)^2 + (
    -0.952835706880077 + x3)^2) + x111 * ((-0.5664183009185346 + x1)^2 + (
    -0.6409573923329756 + x2)^2 + (-0.14836446543357706 + x3)^2) + x112 * ((
    -0.668276613592165 + x1)^2 + (-0.3935536704179623 + x2)^2 + (
    -0.7892941738310548 + x3)^2) + x113 * ((-0.5909840584373237 + x1)^2 + (
    -0.711000971518637 + x2)^2 + (-0.5102861967453806 + x3)^2) + x114 * ((
    -0.7504540204056493 + x1)^2 + (-0.28794681403074973 + x2)^2 + (
    -0.10805205635438697 + x3)^2) + x115 * ((-0.36208849153434675 + x1)^2 + (
    -0.8604979220194023 + x2)^2 + (-0.7543109859318823 + x3)^2) + x116 * ((
    -0.3204638627624359 + x1)^2 + (-0.6985597618075823 + x2)^2 + (
    -0.6884286859796227 + x3)^2) + x117 * ((-0.28040948702637747 + x1)^2 + (
    -0.09782856158952724 + x2)^2 + (-0.5554865157339168 + x3)^2) + x118 * ((
    -0.6650013860062475 + x1)^2 + (-0.4148870776087248 + x2)^2 + (
    -0.13580061730735504 + x3)^2) + x119 * ((-0.42984003511582325 + x4)^2 + (
    -0.5248188211614745 + x5)^2 + (-0.18976547031166158 + x6)^2) + x120 * ((
    -0.7635437892676484 + x4)^2 + (-0.2087128118532261 + x5)^2 + (
    -0.7237865537648877 + x6)^2) + x121 * ((-0.37894209230263076 + x4)^2 + (
    -0.673972806556101 + x5)^2 + (-0.7804374363770062 + x6)^2) + x122 * ((
    -0.03600961414337911 + x4)^2 + (-0.9432908341465497 + x5)^2 + (
    -0.056683718162081176 + x6)^2) + x123 * ((-0.9007184159570817 + x4)^2 + (
    -0.0739499095247852 + x5)^2 + (-0.8655569455322819 + x6)^2) + x124 * ((
    -0.5768605519499145 + x4)^2 + (-0.5986981803675213 + x5)^2 + (
    -0.6570355091518676 + x6)^2) + x125 * ((-0.9745811766548338 + x4)^2 + (
    -0.41474680749048254 + x5)^2 + (-0.9237263978620873 + x6)^2) + x126 * ((
    -0.06206593318927589 + x4)^2 + (-0.2651214371091045 + x5)^2 + (
    -0.6015632454359485 + x6)^2) + x127 * ((-0.6112553172986112 + x4)^2 + (
    -0.8236130985530066 + x5)^2 + (-0.7552731749526171 + x6)^2) + x128 * ((
    -0.2824557711903295 + x4)^2 + (-0.3301346471734301 + x5)^2 + (
    -0.4003642371172418 + x6)^2) + x129 * ((-0.22380220476030066 + x4)^2 + (
    -0.8814483924491749 + x5)^2 + (-0.880102192625681 + x6)^2) + x130 * ((
    -0.5378330969721621 + x4)^2 + (-0.5263672319237694 + x5)^2 + (
    -0.008305374485281347 + x6)^2) + x131 * ((-0.8368636165739145 + x4)^2 + (
    -0.5178975931573176 + x5)^2 + (-0.19654398351590685 + x6)^2) + x132 * ((
    -0.8033599255036961 + x4)^2 + (-0.5470921616898407 + x5)^2 + (
    -0.05989580899877456 + x6)^2) + x133 * ((-0.5041669891441031 + x4)^2 + (
    -0.19483851577422762 + x5)^2 + (-0.04121006383916248 + x6)^2) + x134 * ((
    -0.2735550274413898 + x4)^2 + (-0.5771711903673603 + x5)^2 + (
    -0.8483920722526949 + x6)^2) + x135 * ((-0.16341280932131008 + x4)^2 + (
    -0.38595898916250637 + x5)^2 + (-0.7240527965923388 + x6)^2) + x136 * ((
    -0.184735914655195 + x4)^2 + (-0.9074851747165764 + x5)^2 + (
    -0.5092578035597556 + x6)^2) + x137 * ((-0.667717591753409 + x4)^2 + (
    -0.03611089878214757 + x5)^2 + (-0.5314088140520232 + x6)^2) + x138 * ((
    -0.22082508524283118 + x4)^2 + (-0.14591083104017755 + x5)^2 + (
    -0.4966365264689938 + x6)^2) + x139 * ((-0.8131501378134828 + x4)^2 + (
    -0.12233837490110344 + x5)^2 + (-0.6422164007166057 + x6)^2) + x140 * ((
    -0.5093801089140564 + x4)^2 + (-0.5913076324087453 + x5)^2 + (
    -0.22564192034703445 + x6)^2) + x141 * ((-0.5886418065986404 + x4)^2 + (
    -0.051216403584171344 + x5)^2 + (-0.21124855487984584 + x6)^2) + x142 * ((
    -0.2822083632452721 + x4)^2 + (-0.6609969862369512 + x5)^2 + (
    -0.629237720221342 + x6)^2) + x143 * ((-0.800850840990083 + x4)^2 + (
    -0.2946478937198632 + x5)^2 + (-0.9711075538538692 + x6)^2) + x144 * ((
    -0.18106474877236667 + x4)^2 + (-0.40222650110712255 + x5)^2 + (
    -0.8640061178144425 + x6)^2) + x145 * ((-0.275960867663125 + x4)^2 + (
    -0.8101752183427954 + x5)^2 + (-0.25463108721162286 + x6)^2) + x146 * ((
    -0.09762964668322405 + x4)^2 + (-0.5681164167758985 + x5)^2 + (
    -0.8522588975167438 + x6)^2) + x147 * ((-0.6792262546121857 + x4)^2 + (
    -0.5415479570871046 + x5)^2 + (-0.9198959530376973 + x6)^2) + x148 * ((
    -0.35974899392373416 + x4)^2 + (-0.9692174411067974 + x5)^2 + (
    -0.8173895217629372 + x6)^2) + x149 * ((-0.2775683808009408 + x4)^2 + (
    -0.07111011846817805 + x5)^2 + (-0.9119005527157927 + x6)^2) + x150 * ((
    -0.8728420280238173 + x4)^2 + (-0.4810753656025001 + x5)^2 + (
    -0.5690581714245571 + x6)^2) + x151 * ((-0.3697310611408884 + x4)^2 + (
    -0.8009586582771799 + x5)^2 + (-0.4509367154437284 + x6)^2) + x152 * ((
    -0.40344052086211035 + x4)^2 + (-0.4549860124364724 + x5)^2 + (
    -0.6928018828898217 + x6)^2) + x153 * ((-0.6361863652853047 + x4)^2 + (
    -0.08988225677383088 + x5)^2 + (-0.25890016105768476 + x6)^2) + x154 * ((
    -0.5670078574144451 + x4)^2 + (-0.11962369435126274 + x5)^2 + (
    -0.7694906824065785 + x6)^2) + x155 * ((-0.2970981185523963 + x4)^2 + (
    -0.07089711937031118 + x5)^2 + (-0.3726754551130945 + x6)^2) + x156 * ((
    -0.9463316541147765 + x4)^2 + (-0.5815980777027693 + x5)^2 + (
    -0.09183246305662951 + x6)^2) + x157 * ((-0.4971616963185841 + x4)^2 + (
    -0.5526690085093273 + x5)^2 + (-0.041586056367461044 + x6)^2) + x158 * ((
    -0.48472198232839325 + x4)^2 + (-0.5137822134278897 + x5)^2 + (
    -0.25761582576168296 + x6)^2) + x159 * ((-0.44694684190755307 + x4)^2 + (
    -0.9335294451364397 + x5)^2 + (-0.6212310214093625 + x6)^2) + x160 * ((
    -0.5456179874167029 + x4)^2 + (-0.6257723725570918 + x5)^2 + (
    -0.44030482106573443 + x6)^2) + x161 * ((-0.48291634635300573 + x4)^2 + (
    -0.8500599447417776 + x5)^2 + (-0.8150332638475819 + x6)^2) + x162 * ((
    -0.2076752515318323 + x4)^2 + (-0.851790218430218 + x5)^2 + (
    -0.03852729140159916 + x6)^2) + x163 * ((-0.6321580948524517 + x4)^2 + (
    -0.9837962600945337 + x5)^2 + (-0.6794575866782234 + x6)^2) + x164 * ((
    -0.4741167244817951 + x4)^2 + (-0.7294796721116216 + x5)^2 + (
    -0.320613514728746 + x6)^2) + x165 * ((-0.4456710628183016 + x4)^2 + (
    -0.7380410763666608 + x5)^2 + (-0.38742562758632604 + x6)^2) + x166 * ((
    -0.4265716203395923 + x4)^2 + (-0.7118497351712431 + x5)^2 + (
    -0.7471218555436548 + x6)^2) + x167 * ((-0.23627512847494803 + x4)^2 + (
    -0.5038323922445893 + x5)^2 + (-0.2680376794418369 + x6)^2) + x168 * ((
    -0.8404317556608962 + x4)^2 + (-0.04318546277231472 + x5)^2 + (
    -0.14297270654389005 + x6)^2) + x169 * ((-0.6081062742820188 + x4)^2 + (
    -0.05792573185555616 + x5)^2 + (-0.30572046931736474 + x6)^2) + x170 * ((
    -0.8279542917657221 + x4)^2 + (-0.40201952243043027 + x5)^2 + (
    -0.9469372713050586 + x6)^2) + x171 * ((-0.3415766860940366 + x4)^2 + (
    -0.7667328034595803 + x5)^2 + (-0.5561511348714728 + x6)^2) + x172 * ((
    -0.8766850760174327 + x4)^2 + (-0.47568865268531624 + x5)^2 + (
    -0.9457622702235593 + x6)^2) + x173 * ((-0.060732953253662125 + x4)^2 + (
    -0.43044333590426787 + x5)^2 + (-0.11068204021696582 + x6)^2) + x174 * ((
    -0.5599647447657621 + x4)^2 + (-0.20168813274597885 + x5)^2 + (
    -0.04901731419867861 + x6)^2) + x175 * ((-0.918340292529652 + x4)^2 + (
    -0.3592948253121985 + x5)^2 + (-0.27641861869779194 + x6)^2) + x176 * ((
    -0.2290803422518174 + x4)^2 + (-0.9550196585033648 + x5)^2 + (
    -0.18525883987424996 + x6)^2) + x177 * ((-0.07874295854309366 + x4)^2 + (
    -0.5872376176569806 + x5)^2 + (-0.9964507911035481 + x6)^2) + x178 * ((
    -0.8366839476155882 + x4)^2 + (-0.48096052774158937 + x5)^2 + (
    -0.06875812181004981 + x6)^2) + x179 * ((-0.1646012318827148 + x4)^2 + (
    -0.8255025770989258 + x5)^2 + (-0.5425920043205046 + x6)^2) + x180 * ((
    -0.01206407820830957 + x4)^2 + (-0.7715259933915151 + x5)^2 + (
    -0.8153035946330994 + x6)^2) + x181 * ((-0.656216971146405 + x4)^2 + (
    -0.5038530509474157 + x5)^2 + (-0.24858472460284653 + x6)^2) + x182 * ((
    -0.5909087410955904 + x4)^2 + (-0.24200083344880052 + x5)^2 + (
    -0.2773029284079601 + x6)^2) + x183 * ((-0.30683539741159116 + x4)^2 + (
    -0.1592566555556567 + x5)^2 + (-0.8741709441944726 + x6)^2) + x184 * ((
    -0.9696553356372961 + x4)^2 + (-0.5092140919799073 + x5)^2 + (
    -0.9667357424486342 + x6)^2) + x185 * ((-0.022500436859610784 + x4)^2 + (
    -0.09449938113730139 + x5)^2 + (-0.8914880525816652 + x6)^2) + x186 * ((
    -0.03312939739236054 + x4)^2 + (-0.901942581170032 + x5)^2 + (
    -0.4786651787509474 + x6)^2) + x187 * ((-0.9087943615369551 + x4)^2 + (
    -0.16708419935758345 + x5)^2 + (-0.49548708669584307 + x6)^2) + x188 * ((
    -0.2797850906327509 + x4)^2 + (-0.6710488947711567 + x5)^2 + (
    -0.9586698953495221 + x6)^2) + x189 * ((-0.7571140653627548 + x4)^2 + (
    -0.9772776196167088 + x5)^2 + (-0.545818457398843 + x6)^2) + x190 * ((
    -0.4393881718780316 + x4)^2 + (-0.30502275122869604 + x5)^2 + (
    -0.46993652125745644 + x6)^2) + x191 * ((-0.8328586457197023 + x4)^2 + (
    -0.4665403743372396 + x5)^2 + (-0.044871269867679975 + x6)^2) + x192 * ((
    -0.200399479778539 + x4)^2 + (-0.5930767654991737 + x5)^2 + (
    -0.8532214199144125 + x6)^2) + x193 * ((-0.6635666941849311 + x4)^2 + (
    -0.23391286076708295 + x5)^2 + (-0.4140175544317234 + x6)^2) + x194 * ((
    -0.8017608133257321 + x4)^2 + (-0.8877780696226963 + x5)^2 + (
    -0.7221004582069167 + x6)^2) + x195 * ((-0.7399476414219266 + x4)^2 + (
    -0.7138733629252807 + x5)^2 + (-0.40138791158993503 + x6)^2) + x196 * ((
    -0.505308046012709 + x4)^2 + (-0.050203195063672656 + x5)^2 + (
    -0.047366160401361546 + x6)^2) + x197 * ((-0.16774593722409648 + x4)^2 + (
    -0.6409647710984233 + x5)^2 + (-0.10357005758294846 + x6)^2) + x198 * ((
    -0.831240181700394 + x4)^2 + (-0.8086369689577492 + x5)^2 + (
    -0.8697211693425991 + x6)^2) + x199 * ((-0.9508107670055634 + x4)^2 + (
    -0.6593445284740111 + x5)^2 + (-0.9654494903581963 + x6)^2) + x200 * ((
    -0.9689135289592058 + x4)^2 + (-0.2919924557860033 + x5)^2 + (
    -0.674556583609974 + x6)^2) + x201 * ((-0.5755637731737744 + x4)^2 + (
    -0.029158659146738986 + x5)^2 + (-0.801474333934095 + x6)^2) + x202 * ((
    -0.8814332005944923 + x4)^2 + (-0.9388442894563516 + x5)^2 + (
    -0.2609463697280877 + x6)^2) + x203 * ((-0.21089837943522027 + x4)^2 + (
    -0.339246197282862 + x5)^2 + (-0.3206846661656354 + x6)^2) + x204 * ((
    -0.1546689851574372 + x4)^2 + (-0.9006244078114634 + x5)^2 + (
    -0.383032353156448 + x6)^2) + x205 * ((-0.8898729322311727 + x4)^2 + (
    -0.4755652980462777 + x5)^2 + (-0.22139675941977732 + x6)^2) + x206 * ((
    -0.09681202208693973 + x4)^2 + (-0.5759917076295475 + x5)^2 + (
    -0.5453594292179953 + x6)^2) + x207 * ((-0.22092996837157597 + x4)^2 + (
    -0.46898066660462867 + x5)^2 + (-0.586705478616356 + x6)^2) + x208 * ((
    -0.7772286323779445 + x4)^2 + (-0.19088116193826554 + x5)^2 + (
    -0.856917751975287 + x6)^2) + x209 * ((-0.5698804350762819 + x4)^2 + (
    -0.6223743600871902 + x5)^2 + (-0.8005394562016571 + x6)^2) + x210 * ((
    -0.8378639929136145 + x4)^2 + (-0.2593791410480174 + x5)^2 + (
    -0.952835706880077 + x6)^2) + x211 * ((-0.5664183009185346 + x4)^2 + (
    -0.6409573923329756 + x5)^2 + (-0.14836446543357706 + x6)^2) + x212 * ((
    -0.668276613592165 + x4)^2 + (-0.3935536704179623 + x5)^2 + (
    -0.7892941738310548 + x6)^2) + x213 * ((-0.5909840584373237 + x4)^2 + (
    -0.711000971518637 + x5)^2 + (-0.5102861967453806 + x6)^2) + x214 * ((
    -0.7504540204056493 + x4)^2 + (-0.28794681403074973 + x5)^2 + (
    -0.10805205635438697 + x6)^2) + x215 * ((-0.36208849153434675 + x4)^2 + (
    -0.8604979220194023 + x5)^2 + (-0.7543109859318823 + x6)^2) + x216 * ((
    -0.3204638627624359 + x4)^2 + (-0.6985597618075823 + x5)^2 + (
    -0.6884286859796227 + x6)^2) + x217 * ((-0.28040948702637747 + x4)^2 + (
    -0.09782856158952724 + x5)^2 + (-0.5554865157339168 + x6)^2) + x218 * ((
    -0.6650013860062475 + x4)^2 + (-0.4148870776087248 + x5)^2 + (
    -0.13580061730735504 + x6)^2) + x219 * ((-0.42984003511582325 + x7)^2 + (
    -0.5248188211614745 + x8)^2 + (-0.18976547031166158 + x9)^2) + x220 * ((
    -0.7635437892676484 + x7)^2 + (-0.2087128118532261 + x8)^2 + (
    -0.7237865537648877 + x9)^2) + x221 * ((-0.37894209230263076 + x7)^2 + (
    -0.673972806556101 + x8)^2 + (-0.7804374363770062 + x9)^2) + x222 * ((
    -0.03600961414337911 + x7)^2 + (-0.9432908341465497 + x8)^2 + (
    -0.056683718162081176 + x9)^2) + x223 * ((-0.9007184159570817 + x7)^2 + (
    -0.0739499095247852 + x8)^2 + (-0.8655569455322819 + x9)^2) + x224 * ((
    -0.5768605519499145 + x7)^2 + (-0.5986981803675213 + x8)^2 + (
    -0.6570355091518676 + x9)^2) + x225 * ((-0.9745811766548338 + x7)^2 + (
    -0.41474680749048254 + x8)^2 + (-0.9237263978620873 + x9)^2) + x226 * ((
    -0.06206593318927589 + x7)^2 + (-0.2651214371091045 + x8)^2 + (
    -0.6015632454359485 + x9)^2) + x227 * ((-0.6112553172986112 + x7)^2 + (
    -0.8236130985530066 + x8)^2 + (-0.7552731749526171 + x9)^2) + x228 * ((
    -0.2824557711903295 + x7)^2 + (-0.3301346471734301 + x8)^2 + (
    -0.4003642371172418 + x9)^2) + x229 * ((-0.22380220476030066 + x7)^2 + (
    -0.8814483924491749 + x8)^2 + (-0.880102192625681 + x9)^2) + x230 * ((
    -0.5378330969721621 + x7)^2 + (-0.5263672319237694 + x8)^2 + (
    -0.008305374485281347 + x9)^2) + x231 * ((-0.8368636165739145 + x7)^2 + (
    -0.5178975931573176 + x8)^2 + (-0.19654398351590685 + x9)^2) + x232 * ((
    -0.8033599255036961 + x7)^2 + (-0.5470921616898407 + x8)^2 + (
    -0.05989580899877456 + x9)^2) + x233 * ((-0.5041669891441031 + x7)^2 + (
    -0.19483851577422762 + x8)^2 + (-0.04121006383916248 + x9)^2) + x234 * ((
    -0.2735550274413898 + x7)^2 + (-0.5771711903673603 + x8)^2 + (
    -0.8483920722526949 + x9)^2) + x235 * ((-0.16341280932131008 + x7)^2 + (
    -0.38595898916250637 + x8)^2 + (-0.7240527965923388 + x9)^2) + x236 * ((
    -0.184735914655195 + x7)^2 + (-0.9074851747165764 + x8)^2 + (
    -0.5092578035597556 + x9)^2) + x237 * ((-0.667717591753409 + x7)^2 + (
    -0.03611089878214757 + x8)^2 + (-0.5314088140520232 + x9)^2) + x238 * ((
    -0.22082508524283118 + x7)^2 + (-0.14591083104017755 + x8)^2 + (
    -0.4966365264689938 + x9)^2) + x239 * ((-0.8131501378134828 + x7)^2 + (
    -0.12233837490110344 + x8)^2 + (-0.6422164007166057 + x9)^2) + x240 * ((
    -0.5093801089140564 + x7)^2 + (-0.5913076324087453 + x8)^2 + (
    -0.22564192034703445 + x9)^2) + x241 * ((-0.5886418065986404 + x7)^2 + (
    -0.051216403584171344 + x8)^2 + (-0.21124855487984584 + x9)^2) + x242 * ((
    -0.2822083632452721 + x7)^2 + (-0.6609969862369512 + x8)^2 + (
    -0.629237720221342 + x9)^2) + x243 * ((-0.800850840990083 + x7)^2 + (
    -0.2946478937198632 + x8)^2 + (-0.9711075538538692 + x9)^2) + x244 * ((
    -0.18106474877236667 + x7)^2 + (-0.40222650110712255 + x8)^2 + (
    -0.8640061178144425 + x9)^2) + x245 * ((-0.275960867663125 + x7)^2 + (
    -0.8101752183427954 + x8)^2 + (-0.25463108721162286 + x9)^2) + x246 * ((
    -0.09762964668322405 + x7)^2 + (-0.5681164167758985 + x8)^2 + (
    -0.8522588975167438 + x9)^2) + x247 * ((-0.6792262546121857 + x7)^2 + (
    -0.5415479570871046 + x8)^2 + (-0.9198959530376973 + x9)^2) + x248 * ((
    -0.35974899392373416 + x7)^2 + (-0.9692174411067974 + x8)^2 + (
    -0.8173895217629372 + x9)^2) + x249 * ((-0.2775683808009408 + x7)^2 + (
    -0.07111011846817805 + x8)^2 + (-0.9119005527157927 + x9)^2) + x250 * ((
    -0.8728420280238173 + x7)^2 + (-0.4810753656025001 + x8)^2 + (
    -0.5690581714245571 + x9)^2) + x251 * ((-0.3697310611408884 + x7)^2 + (
    -0.8009586582771799 + x8)^2 + (-0.4509367154437284 + x9)^2) + x252 * ((
    -0.40344052086211035 + x7)^2 + (-0.4549860124364724 + x8)^2 + (
    -0.6928018828898217 + x9)^2) + x253 * ((-0.6361863652853047 + x7)^2 + (
    -0.08988225677383088 + x8)^2 + (-0.25890016105768476 + x9)^2) + x254 * ((
    -0.5670078574144451 + x7)^2 + (-0.11962369435126274 + x8)^2 + (
    -0.7694906824065785 + x9)^2) + x255 * ((-0.2970981185523963 + x7)^2 + (
    -0.07089711937031118 + x8)^2 + (-0.3726754551130945 + x9)^2) + x256 * ((
    -0.9463316541147765 + x7)^2 + (-0.5815980777027693 + x8)^2 + (
    -0.09183246305662951 + x9)^2) + x257 * ((-0.4971616963185841 + x7)^2 + (
    -0.5526690085093273 + x8)^2 + (-0.041586056367461044 + x9)^2) + x258 * ((
    -0.48472198232839325 + x7)^2 + (-0.5137822134278897 + x8)^2 + (
    -0.25761582576168296 + x9)^2) + x259 * ((-0.44694684190755307 + x7)^2 + (
    -0.9335294451364397 + x8)^2 + (-0.6212310214093625 + x9)^2) + x260 * ((
    -0.5456179874167029 + x7)^2 + (-0.6257723725570918 + x8)^2 + (
    -0.44030482106573443 + x9)^2) + x261 * ((-0.48291634635300573 + x7)^2 + (
    -0.8500599447417776 + x8)^2 + (-0.8150332638475819 + x9)^2) + x262 * ((
    -0.2076752515318323 + x7)^2 + (-0.851790218430218 + x8)^2 + (
    -0.03852729140159916 + x9)^2) + x263 * ((-0.6321580948524517 + x7)^2 + (
    -0.9837962600945337 + x8)^2 + (-0.6794575866782234 + x9)^2) + x264 * ((
    -0.4741167244817951 + x7)^2 + (-0.7294796721116216 + x8)^2 + (
    -0.320613514728746 + x9)^2) + x265 * ((-0.4456710628183016 + x7)^2 + (
    -0.7380410763666608 + x8)^2 + (-0.38742562758632604 + x9)^2) + x266 * ((
    -0.4265716203395923 + x7)^2 + (-0.7118497351712431 + x8)^2 + (
    -0.7471218555436548 + x9)^2) + x267 * ((-0.23627512847494803 + x7)^2 + (
    -0.5038323922445893 + x8)^2 + (-0.2680376794418369 + x9)^2) + x268 * ((
    -0.8404317556608962 + x7)^2 + (-0.04318546277231472 + x8)^2 + (
    -0.14297270654389005 + x9)^2) + x269 * ((-0.6081062742820188 + x7)^2 + (
    -0.05792573185555616 + x8)^2 + (-0.30572046931736474 + x9)^2) + x270 * ((
    -0.8279542917657221 + x7)^2 + (-0.40201952243043027 + x8)^2 + (
    -0.9469372713050586 + x9)^2) + x271 * ((-0.3415766860940366 + x7)^2 + (
    -0.7667328034595803 + x8)^2 + (-0.5561511348714728 + x9)^2) + x272 * ((
    -0.8766850760174327 + x7)^2 + (-0.47568865268531624 + x8)^2 + (
    -0.9457622702235593 + x9)^2) + x273 * ((-0.060732953253662125 + x7)^2 + (
    -0.43044333590426787 + x8)^2 + (-0.11068204021696582 + x9)^2) + x274 * ((
    -0.5599647447657621 + x7)^2 + (-0.20168813274597885 + x8)^2 + (
    -0.04901731419867861 + x9)^2) + x275 * ((-0.918340292529652 + x7)^2 + (
    -0.3592948253121985 + x8)^2 + (-0.27641861869779194 + x9)^2) + x276 * ((
    -0.2290803422518174 + x7)^2 + (-0.9550196585033648 + x8)^2 + (
    -0.18525883987424996 + x9)^2) + x277 * ((-0.07874295854309366 + x7)^2 + (
    -0.5872376176569806 + x8)^2 + (-0.9964507911035481 + x9)^2) + x278 * ((
    -0.8366839476155882 + x7)^2 + (-0.48096052774158937 + x8)^2 + (
    -0.06875812181004981 + x9)^2) + x279 * ((-0.1646012318827148 + x7)^2 + (
    -0.8255025770989258 + x8)^2 + (-0.5425920043205046 + x9)^2) + x280 * ((
    -0.01206407820830957 + x7)^2 + (-0.7715259933915151 + x8)^2 + (
    -0.8153035946330994 + x9)^2) + x281 * ((-0.656216971146405 + x7)^2 + (
    -0.5038530509474157 + x8)^2 + (-0.24858472460284653 + x9)^2) + x282 * ((
    -0.5909087410955904 + x7)^2 + (-0.24200083344880052 + x8)^2 + (
    -0.2773029284079601 + x9)^2) + x283 * ((-0.30683539741159116 + x7)^2 + (
    -0.1592566555556567 + x8)^2 + (-0.8741709441944726 + x9)^2) + x284 * ((
    -0.9696553356372961 + x7)^2 + (-0.5092140919799073 + x8)^2 + (
    -0.9667357424486342 + x9)^2) + x285 * ((-0.022500436859610784 + x7)^2 + (
    -0.09449938113730139 + x8)^2 + (-0.8914880525816652 + x9)^2) + x286 * ((
    -0.03312939739236054 + x7)^2 + (-0.901942581170032 + x8)^2 + (
    -0.4786651787509474 + x9)^2) + x287 * ((-0.9087943615369551 + x7)^2 + (
    -0.16708419935758345 + x8)^2 + (-0.49548708669584307 + x9)^2) + x288 * ((
    -0.2797850906327509 + x7)^2 + (-0.6710488947711567 + x8)^2 + (
    -0.9586698953495221 + x9)^2) + x289 * ((-0.7571140653627548 + x7)^2 + (
    -0.9772776196167088 + x8)^2 + (-0.545818457398843 + x9)^2) + x290 * ((
    -0.4393881718780316 + x7)^2 + (-0.30502275122869604 + x8)^2 + (
    -0.46993652125745644 + x9)^2) + x291 * ((-0.8328586457197023 + x7)^2 + (
    -0.4665403743372396 + x8)^2 + (-0.044871269867679975 + x9)^2) + x292 * ((
    -0.200399479778539 + x7)^2 + (-0.5930767654991737 + x8)^2 + (
    -0.8532214199144125 + x9)^2) + x293 * ((-0.6635666941849311 + x7)^2 + (
    -0.23391286076708295 + x8)^2 + (-0.4140175544317234 + x9)^2) + x294 * ((
    -0.8017608133257321 + x7)^2 + (-0.8877780696226963 + x8)^2 + (
    -0.7221004582069167 + x9)^2) + x295 * ((-0.7399476414219266 + x7)^2 + (
    -0.7138733629252807 + x8)^2 + (-0.40138791158993503 + x9)^2) + x296 * ((
    -0.505308046012709 + x7)^2 + (-0.050203195063672656 + x8)^2 + (
    -0.047366160401361546 + x9)^2) + x297 * ((-0.16774593722409648 + x7)^2 + (
    -0.6409647710984233 + x8)^2 + (-0.10357005758294846 + x9)^2) + x298 * ((
    -0.831240181700394 + x7)^2 + (-0.8086369689577492 + x8)^2 + (
    -0.8697211693425991 + x9)^2) + x299 * ((-0.9508107670055634 + x7)^2 + (
    -0.6593445284740111 + x8)^2 + (-0.9654494903581963 + x9)^2) + x300 * ((
    -0.9689135289592058 + x7)^2 + (-0.2919924557860033 + x8)^2 + (
    -0.674556583609974 + x9)^2) + x301 * ((-0.5755637731737744 + x7)^2 + (
    -0.029158659146738986 + x8)^2 + (-0.801474333934095 + x9)^2) + x302 * ((
    -0.8814332005944923 + x7)^2 + (-0.9388442894563516 + x8)^2 + (
    -0.2609463697280877 + x9)^2) + x303 * ((-0.21089837943522027 + x7)^2 + (
    -0.339246197282862 + x8)^2 + (-0.3206846661656354 + x9)^2) + x304 * ((
    -0.1546689851574372 + x7)^2 + (-0.9006244078114634 + x8)^2 + (
    -0.383032353156448 + x9)^2) + x305 * ((-0.8898729322311727 + x7)^2 + (
    -0.4755652980462777 + x8)^2 + (-0.22139675941977732 + x9)^2) + x306 * ((
    -0.09681202208693973 + x7)^2 + (-0.5759917076295475 + x8)^2 + (
    -0.5453594292179953 + x9)^2) + x307 * ((-0.22092996837157597 + x7)^2 + (
    -0.46898066660462867 + x8)^2 + (-0.586705478616356 + x9)^2) + x308 * ((
    -0.7772286323779445 + x7)^2 + (-0.19088116193826554 + x8)^2 + (
    -0.856917751975287 + x9)^2) + x309 * ((-0.5698804350762819 + x7)^2 + (
    -0.6223743600871902 + x8)^2 + (-0.8005394562016571 + x9)^2) + x310 * ((
    -0.8378639929136145 + x7)^2 + (-0.2593791410480174 + x8)^2 + (
    -0.952835706880077 + x9)^2) + x311 * ((-0.5664183009185346 + x7)^2 + (
    -0.6409573923329756 + x8)^2 + (-0.14836446543357706 + x9)^2) + x312 * ((
    -0.668276613592165 + x7)^2 + (-0.3935536704179623 + x8)^2 + (
    -0.7892941738310548 + x9)^2) + x313 * ((-0.5909840584373237 + x7)^2 + (
    -0.711000971518637 + x8)^2 + (-0.5102861967453806 + x9)^2) + x314 * ((
    -0.7504540204056493 + x7)^2 + (-0.28794681403074973 + x8)^2 + (
    -0.10805205635438697 + x9)^2) + x315 * ((-0.36208849153434675 + x7)^2 + (
    -0.8604979220194023 + x8)^2 + (-0.7543109859318823 + x9)^2) + x316 * ((
    -0.3204638627624359 + x7)^2 + (-0.6985597618075823 + x8)^2 + (
    -0.6884286859796227 + x9)^2) + x317 * ((-0.28040948702637747 + x7)^2 + (
    -0.09782856158952724 + x8)^2 + (-0.5554865157339168 + x9)^2) + x318 * ((
    -0.6650013860062475 + x7)^2 + (-0.4148870776087248 + x8)^2 + (
    -0.13580061730735504 + x9)^2) + x319 * ((-0.42984003511582325 + x10)^2 + (
    -0.5248188211614745 + x11)^2 + (-0.18976547031166158 + x12)^2) + x320 * ((
    -0.7635437892676484 + x10)^2 + (-0.2087128118532261 + x11)^2 + (
    -0.7237865537648877 + x12)^2) + x321 * ((-0.37894209230263076 + x10)^2 + (
    -0.673972806556101 + x11)^2 + (-0.7804374363770062 + x12)^2) + x322 * ((
    -0.03600961414337911 + x10)^2 + (-0.9432908341465497 + x11)^2 + (
    -0.056683718162081176 + x12)^2) + x323 * ((-0.9007184159570817 + x10)^2 + (
    -0.0739499095247852 + x11)^2 + (-0.8655569455322819 + x12)^2) + x324 * ((
    -0.5768605519499145 + x10)^2 + (-0.5986981803675213 + x11)^2 + (
    -0.6570355091518676 + x12)^2) + x325 * ((-0.9745811766548338 + x10)^2 + (
    -0.41474680749048254 + x11)^2 + (-0.9237263978620873 + x12)^2) + x326 * ((
    -0.06206593318927589 + x10)^2 + (-0.2651214371091045 + x11)^2 + (
    -0.6015632454359485 + x12)^2) + x327 * ((-0.6112553172986112 + x10)^2 + (
    -0.8236130985530066 + x11)^2 + (-0.7552731749526171 + x12)^2) + x328 * ((
    -0.2824557711903295 + x10)^2 + (-0.3301346471734301 + x11)^2 + (
    -0.4003642371172418 + x12)^2) + x329 * ((-0.22380220476030066 + x10)^2 + (
    -0.8814483924491749 + x11)^2 + (-0.880102192625681 + x12)^2) + x330 * ((
    -0.5378330969721621 + x10)^2 + (-0.5263672319237694 + x11)^2 + (
    -0.008305374485281347 + x12)^2) + x331 * ((-0.8368636165739145 + x10)^2 + (
    -0.5178975931573176 + x11)^2 + (-0.19654398351590685 + x12)^2) + x332 * ((
    -0.8033599255036961 + x10)^2 + (-0.5470921616898407 + x11)^2 + (
    -0.05989580899877456 + x12)^2) + x333 * ((-0.5041669891441031 + x10)^2 + (
    -0.19483851577422762 + x11)^2 + (-0.04121006383916248 + x12)^2) + x334 * ((
    -0.2735550274413898 + x10)^2 + (-0.5771711903673603 + x11)^2 + (
    -0.8483920722526949 + x12)^2) + x335 * ((-0.16341280932131008 + x10)^2 + (
    -0.38595898916250637 + x11)^2 + (-0.7240527965923388 + x12)^2) + x336 * ((
    -0.184735914655195 + x10)^2 + (-0.9074851747165764 + x11)^2 + (
    -0.5092578035597556 + x12)^2) + x337 * ((-0.667717591753409 + x10)^2 + (
    -0.03611089878214757 + x11)^2 + (-0.5314088140520232 + x12)^2) + x338 * ((
    -0.22082508524283118 + x10)^2 + (-0.14591083104017755 + x11)^2 + (
    -0.4966365264689938 + x12)^2) + x339 * ((-0.8131501378134828 + x10)^2 + (
    -0.12233837490110344 + x11)^2 + (-0.6422164007166057 + x12)^2) + x340 * ((
    -0.5093801089140564 + x10)^2 + (-0.5913076324087453 + x11)^2 + (
    -0.22564192034703445 + x12)^2) + x341 * ((-0.5886418065986404 + x10)^2 + (
    -0.051216403584171344 + x11)^2 + (-0.21124855487984584 + x12)^2) + x342 * (
    (-0.2822083632452721 + x10)^2 + (-0.6609969862369512 + x11)^2 + (
    -0.629237720221342 + x12)^2) + x343 * ((-0.800850840990083 + x10)^2 + (
    -0.2946478937198632 + x11)^2 + (-0.9711075538538692 + x12)^2) + x344 * ((
    -0.18106474877236667 + x10)^2 + (-0.40222650110712255 + x11)^2 + (
    -0.8640061178144425 + x12)^2) + x345 * ((-0.275960867663125 + x10)^2 + (
    -0.8101752183427954 + x11)^2 + (-0.25463108721162286 + x12)^2) + x346 * ((
    -0.09762964668322405 + x10)^2 + (-0.5681164167758985 + x11)^2 + (
    -0.8522588975167438 + x12)^2) + x347 * ((-0.6792262546121857 + x10)^2 + (
    -0.5415479570871046 + x11)^2 + (-0.9198959530376973 + x12)^2) + x348 * ((
    -0.35974899392373416 + x10)^2 + (-0.9692174411067974 + x11)^2 + (
    -0.8173895217629372 + x12)^2) + x349 * ((-0.2775683808009408 + x10)^2 + (
    -0.07111011846817805 + x11)^2 + (-0.9119005527157927 + x12)^2) + x350 * ((
    -0.8728420280238173 + x10)^2 + (-0.4810753656025001 + x11)^2 + (
    -0.5690581714245571 + x12)^2) + x351 * ((-0.3697310611408884 + x10)^2 + (
    -0.8009586582771799 + x11)^2 + (-0.4509367154437284 + x12)^2) + x352 * ((
    -0.40344052086211035 + x10)^2 + (-0.4549860124364724 + x11)^2 + (
    -0.6928018828898217 + x12)^2) + x353 * ((-0.6361863652853047 + x10)^2 + (
    -0.08988225677383088 + x11)^2 + (-0.25890016105768476 + x12)^2) + x354 * ((
    -0.5670078574144451 + x10)^2 + (-0.11962369435126274 + x11)^2 + (
    -0.7694906824065785 + x12)^2) + x355 * ((-0.2970981185523963 + x10)^2 + (
    -0.07089711937031118 + x11)^2 + (-0.3726754551130945 + x12)^2) + x356 * ((
    -0.9463316541147765 + x10)^2 + (-0.5815980777027693 + x11)^2 + (
    -0.09183246305662951 + x12)^2) + x357 * ((-0.4971616963185841 + x10)^2 + (
    -0.5526690085093273 + x11)^2 + (-0.041586056367461044 + x12)^2) + x358 * ((
    -0.48472198232839325 + x10)^2 + (-0.5137822134278897 + x11)^2 + (
    -0.25761582576168296 + x12)^2) + x359 * ((-0.44694684190755307 + x10)^2 + (
    -0.9335294451364397 + x11)^2 + (-0.6212310214093625 + x12)^2) + x360 * ((
    -0.5456179874167029 + x10)^2 + (-0.6257723725570918 + x11)^2 + (
    -0.44030482106573443 + x12)^2) + x361 * ((-0.48291634635300573 + x10)^2 + (
    -0.8500599447417776 + x11)^2 + (-0.8150332638475819 + x12)^2) + x362 * ((
    -0.2076752515318323 + x10)^2 + (-0.851790218430218 + x11)^2 + (
    -0.03852729140159916 + x12)^2) + x363 * ((-0.6321580948524517 + x10)^2 + (
    -0.9837962600945337 + x11)^2 + (-0.6794575866782234 + x12)^2) + x364 * ((
    -0.4741167244817951 + x10)^2 + (-0.7294796721116216 + x11)^2 + (
    -0.320613514728746 + x12)^2) + x365 * ((-0.4456710628183016 + x10)^2 + (
    -0.7380410763666608 + x11)^2 + (-0.38742562758632604 + x12)^2) + x366 * ((
    -0.4265716203395923 + x10)^2 + (-0.7118497351712431 + x11)^2 + (
    -0.7471218555436548 + x12)^2) + x367 * ((-0.23627512847494803 + x10)^2 + (
    -0.5038323922445893 + x11)^2 + (-0.2680376794418369 + x12)^2) + x368 * ((
    -0.8404317556608962 + x10)^2 + (-0.04318546277231472 + x11)^2 + (
    -0.14297270654389005 + x12)^2) + x369 * ((-0.6081062742820188 + x10)^2 + (
    -0.05792573185555616 + x11)^2 + (-0.30572046931736474 + x12)^2) + x370 * ((
    -0.8279542917657221 + x10)^2 + (-0.40201952243043027 + x11)^2 + (
    -0.9469372713050586 + x12)^2) + x371 * ((-0.3415766860940366 + x10)^2 + (
    -0.7667328034595803 + x11)^2 + (-0.5561511348714728 + x12)^2) + x372 * ((
    -0.8766850760174327 + x10)^2 + (-0.47568865268531624 + x11)^2 + (
    -0.9457622702235593 + x12)^2) + x373 * ((-0.060732953253662125 + x10)^2 + (
    -0.43044333590426787 + x11)^2 + (-0.11068204021696582 + x12)^2) + x374 * ((
    -0.5599647447657621 + x10)^2 + (-0.20168813274597885 + x11)^2 + (
    -0.04901731419867861 + x12)^2) + x375 * ((-0.918340292529652 + x10)^2 + (
    -0.3592948253121985 + x11)^2 + (-0.27641861869779194 + x12)^2) + x376 * ((
    -0.2290803422518174 + x10)^2 + (-0.9550196585033648 + x11)^2 + (
    -0.18525883987424996 + x12)^2) + x377 * ((-0.07874295854309366 + x10)^2 + (
    -0.5872376176569806 + x11)^2 + (-0.9964507911035481 + x12)^2) + x378 * ((
    -0.8366839476155882 + x10)^2 + (-0.48096052774158937 + x11)^2 + (
    -0.06875812181004981 + x12)^2) + x379 * ((-0.1646012318827148 + x10)^2 + (
    -0.8255025770989258 + x11)^2 + (-0.5425920043205046 + x12)^2) + x380 * ((
    -0.01206407820830957 + x10)^2 + (-0.7715259933915151 + x11)^2 + (
    -0.8153035946330994 + x12)^2) + x381 * ((-0.656216971146405 + x10)^2 + (
    -0.5038530509474157 + x11)^2 + (-0.24858472460284653 + x12)^2) + x382 * ((
    -0.5909087410955904 + x10)^2 + (-0.24200083344880052 + x11)^2 + (
    -0.2773029284079601 + x12)^2) + x383 * ((-0.30683539741159116 + x10)^2 + (
    -0.1592566555556567 + x11)^2 + (-0.8741709441944726 + x12)^2) + x384 * ((
    -0.9696553356372961 + x10)^2 + (-0.5092140919799073 + x11)^2 + (
    -0.9667357424486342 + x12)^2) + x385 * ((-0.022500436859610784 + x10)^2 + (
    -0.09449938113730139 + x11)^2 + (-0.8914880525816652 + x12)^2) + x386 * ((
    -0.03312939739236054 + x10)^2 + (-0.901942581170032 + x11)^2 + (
    -0.4786651787509474 + x12)^2) + x387 * ((-0.9087943615369551 + x10)^2 + (
    -0.16708419935758345 + x11)^2 + (-0.49548708669584307 + x12)^2) + x388 * ((
    -0.2797850906327509 + x10)^2 + (-0.6710488947711567 + x11)^2 + (
    -0.9586698953495221 + x12)^2) + x389 * ((-0.7571140653627548 + x10)^2 + (
    -0.9772776196167088 + x11)^2 + (-0.545818457398843 + x12)^2) + x390 * ((
    -0.4393881718780316 + x10)^2 + (-0.30502275122869604 + x11)^2 + (
    -0.46993652125745644 + x12)^2) + x391 * ((-0.8328586457197023 + x10)^2 + (
    -0.4665403743372396 + x11)^2 + (-0.044871269867679975 + x12)^2) + x392 * ((
    -0.200399479778539 + x10)^2 + (-0.5930767654991737 + x11)^2 + (
    -0.8532214199144125 + x12)^2) + x393 * ((-0.6635666941849311 + x10)^2 + (
    -0.23391286076708295 + x11)^2 + (-0.4140175544317234 + x12)^2) + x394 * ((
    -0.8017608133257321 + x10)^2 + (-0.8877780696226963 + x11)^2 + (
    -0.7221004582069167 + x12)^2) + x395 * ((-0.7399476414219266 + x10)^2 + (
    -0.7138733629252807 + x11)^2 + (-0.40138791158993503 + x12)^2) + x396 * ((
    -0.505308046012709 + x10)^2 + (-0.050203195063672656 + x11)^2 + (
    -0.047366160401361546 + x12)^2) + x397 * ((-0.16774593722409648 + x10)^2 +
    (-0.6409647710984233 + x11)^2 + (-0.10357005758294846 + x12)^2) + x398 * ((
    -0.831240181700394 + x10)^2 + (-0.8086369689577492 + x11)^2 + (
    -0.8697211693425991 + x12)^2) + x399 * ((-0.9508107670055634 + x10)^2 + (
    -0.6593445284740111 + x11)^2 + (-0.9654494903581963 + x12)^2) + x400 * ((
    -0.9689135289592058 + x10)^2 + (-0.2919924557860033 + x11)^2 + (
    -0.674556583609974 + x12)^2) + x401 * ((-0.5755637731737744 + x10)^2 + (
    -0.029158659146738986 + x11)^2 + (-0.801474333934095 + x12)^2) + x402 * ((
    -0.8814332005944923 + x10)^2 + (-0.9388442894563516 + x11)^2 + (
    -0.2609463697280877 + x12)^2) + x403 * ((-0.21089837943522027 + x10)^2 + (
    -0.339246197282862 + x11)^2 + (-0.3206846661656354 + x12)^2) + x404 * ((
    -0.1546689851574372 + x10)^2 + (-0.9006244078114634 + x11)^2 + (
    -0.383032353156448 + x12)^2) + x405 * ((-0.8898729322311727 + x10)^2 + (
    -0.4755652980462777 + x11)^2 + (-0.22139675941977732 + x12)^2) + x406 * ((
    -0.09681202208693973 + x10)^2 + (-0.5759917076295475 + x11)^2 + (
    -0.5453594292179953 + x12)^2) + x407 * ((-0.22092996837157597 + x10)^2 + (
    -0.46898066660462867 + x11)^2 + (-0.586705478616356 + x12)^2) + x408 * ((
    -0.7772286323779445 + x10)^2 + (-0.19088116193826554 + x11)^2 + (
    -0.856917751975287 + x12)^2) + x409 * ((-0.5698804350762819 + x10)^2 + (
    -0.6223743600871902 + x11)^2 + (-0.8005394562016571 + x12)^2) + x410 * ((
    -0.8378639929136145 + x10)^2 + (-0.2593791410480174 + x11)^2 + (
    -0.952835706880077 + x12)^2) + x411 * ((-0.5664183009185346 + x10)^2 + (
    -0.6409573923329756 + x11)^2 + (-0.14836446543357706 + x12)^2) + x412 * ((
    -0.668276613592165 + x10)^2 + (-0.3935536704179623 + x11)^2 + (
    -0.7892941738310548 + x12)^2) + x413 * ((-0.5909840584373237 + x10)^2 + (
    -0.711000971518637 + x11)^2 + (-0.5102861967453806 + x12)^2) + x414 * ((
    -0.7504540204056493 + x10)^2 + (-0.28794681403074973 + x11)^2 + (
    -0.10805205635438697 + x12)^2) + x415 * ((-0.36208849153434675 + x10)^2 + (
    -0.8604979220194023 + x11)^2 + (-0.7543109859318823 + x12)^2) + x416 * ((
    -0.3204638627624359 + x10)^2 + (-0.6985597618075823 + x11)^2 + (
    -0.6884286859796227 + x12)^2) + x417 * ((-0.28040948702637747 + x10)^2 + (
    -0.09782856158952724 + x11)^2 + (-0.5554865157339168 + x12)^2) + x418 * ((
    -0.6650013860062475 + x10)^2 + (-0.4148870776087248 + x11)^2 + (
    -0.13580061730735504 + x12)^2) + x419 * ((-0.42984003511582325 + x13)^2 + (
    -0.5248188211614745 + x14)^2 + (-0.18976547031166158 + x15)^2) + x420 * ((
    -0.7635437892676484 + x13)^2 + (-0.2087128118532261 + x14)^2 + (
    -0.7237865537648877 + x15)^2) + x421 * ((-0.37894209230263076 + x13)^2 + (
    -0.673972806556101 + x14)^2 + (-0.7804374363770062 + x15)^2) + x422 * ((
    -0.03600961414337911 + x13)^2 + (-0.9432908341465497 + x14)^2 + (
    -0.056683718162081176 + x15)^2) + x423 * ((-0.9007184159570817 + x13)^2 + (
    -0.0739499095247852 + x14)^2 + (-0.8655569455322819 + x15)^2) + x424 * ((
    -0.5768605519499145 + x13)^2 + (-0.5986981803675213 + x14)^2 + (
    -0.6570355091518676 + x15)^2) + x425 * ((-0.9745811766548338 + x13)^2 + (
    -0.41474680749048254 + x14)^2 + (-0.9237263978620873 + x15)^2) + x426 * ((
    -0.06206593318927589 + x13)^2 + (-0.2651214371091045 + x14)^2 + (
    -0.6015632454359485 + x15)^2) + x427 * ((-0.6112553172986112 + x13)^2 + (
    -0.8236130985530066 + x14)^2 + (-0.7552731749526171 + x15)^2) + x428 * ((
    -0.2824557711903295 + x13)^2 + (-0.3301346471734301 + x14)^2 + (
    -0.4003642371172418 + x15)^2) + x429 * ((-0.22380220476030066 + x13)^2 + (
    -0.8814483924491749 + x14)^2 + (-0.880102192625681 + x15)^2) + x430 * ((
    -0.5378330969721621 + x13)^2 + (-0.5263672319237694 + x14)^2 + (
    -0.008305374485281347 + x15)^2) + x431 * ((-0.8368636165739145 + x13)^2 + (
    -0.5178975931573176 + x14)^2 + (-0.19654398351590685 + x15)^2) + x432 * ((
    -0.8033599255036961 + x13)^2 + (-0.5470921616898407 + x14)^2 + (
    -0.05989580899877456 + x15)^2) + x433 * ((-0.5041669891441031 + x13)^2 + (
    -0.19483851577422762 + x14)^2 + (-0.04121006383916248 + x15)^2) + x434 * ((
    -0.2735550274413898 + x13)^2 + (-0.5771711903673603 + x14)^2 + (
    -0.8483920722526949 + x15)^2) + x435 * ((-0.16341280932131008 + x13)^2 + (
    -0.38595898916250637 + x14)^2 + (-0.7240527965923388 + x15)^2) + x436 * ((
    -0.184735914655195 + x13)^2 + (-0.9074851747165764 + x14)^2 + (
    -0.5092578035597556 + x15)^2) + x437 * ((-0.667717591753409 + x13)^2 + (
    -0.03611089878214757 + x14)^2 + (-0.5314088140520232 + x15)^2) + x438 * ((
    -0.22082508524283118 + x13)^2 + (-0.14591083104017755 + x14)^2 + (
    -0.4966365264689938 + x15)^2) + x439 * ((-0.8131501378134828 + x13)^2 + (
    -0.12233837490110344 + x14)^2 + (-0.6422164007166057 + x15)^2) + x440 * ((
    -0.5093801089140564 + x13)^2 + (-0.5913076324087453 + x14)^2 + (
    -0.22564192034703445 + x15)^2) + x441 * ((-0.5886418065986404 + x13)^2 + (
    -0.051216403584171344 + x14)^2 + (-0.21124855487984584 + x15)^2) + x442 * (
    (-0.2822083632452721 + x13)^2 + (-0.6609969862369512 + x14)^2 + (
    -0.629237720221342 + x15)^2) + x443 * ((-0.800850840990083 + x13)^2 + (
    -0.2946478937198632 + x14)^2 + (-0.9711075538538692 + x15)^2) + x444 * ((
    -0.18106474877236667 + x13)^2 + (-0.40222650110712255 + x14)^2 + (
    -0.8640061178144425 + x15)^2) + x445 * ((-0.275960867663125 + x13)^2 + (
    -0.8101752183427954 + x14)^2 + (-0.25463108721162286 + x15)^2) + x446 * ((
    -0.09762964668322405 + x13)^2 + (-0.5681164167758985 + x14)^2 + (
    -0.8522588975167438 + x15)^2) + x447 * ((-0.6792262546121857 + x13)^2 + (
    -0.5415479570871046 + x14)^2 + (-0.9198959530376973 + x15)^2) + x448 * ((
    -0.35974899392373416 + x13)^2 + (-0.9692174411067974 + x14)^2 + (
    -0.8173895217629372 + x15)^2) + x449 * ((-0.2775683808009408 + x13)^2 + (
    -0.07111011846817805 + x14)^2 + (-0.9119005527157927 + x15)^2) + x450 * ((
    -0.8728420280238173 + x13)^2 + (-0.4810753656025001 + x14)^2 + (
    -0.5690581714245571 + x15)^2) + x451 * ((-0.3697310611408884 + x13)^2 + (
    -0.8009586582771799 + x14)^2 + (-0.4509367154437284 + x15)^2) + x452 * ((
    -0.40344052086211035 + x13)^2 + (-0.4549860124364724 + x14)^2 + (
    -0.6928018828898217 + x15)^2) + x453 * ((-0.6361863652853047 + x13)^2 + (
    -0.08988225677383088 + x14)^2 + (-0.25890016105768476 + x15)^2) + x454 * ((
    -0.5670078574144451 + x13)^2 + (-0.11962369435126274 + x14)^2 + (
    -0.7694906824065785 + x15)^2) + x455 * ((-0.2970981185523963 + x13)^2 + (
    -0.07089711937031118 + x14)^2 + (-0.3726754551130945 + x15)^2) + x456 * ((
    -0.9463316541147765 + x13)^2 + (-0.5815980777027693 + x14)^2 + (
    -0.09183246305662951 + x15)^2) + x457 * ((-0.4971616963185841 + x13)^2 + (
    -0.5526690085093273 + x14)^2 + (-0.041586056367461044 + x15)^2) + x458 * ((
    -0.48472198232839325 + x13)^2 + (-0.5137822134278897 + x14)^2 + (
    -0.25761582576168296 + x15)^2) + x459 * ((-0.44694684190755307 + x13)^2 + (
    -0.9335294451364397 + x14)^2 + (-0.6212310214093625 + x15)^2) + x460 * ((
    -0.5456179874167029 + x13)^2 + (-0.6257723725570918 + x14)^2 + (
    -0.44030482106573443 + x15)^2) + x461 * ((-0.48291634635300573 + x13)^2 + (
    -0.8500599447417776 + x14)^2 + (-0.8150332638475819 + x15)^2) + x462 * ((
    -0.2076752515318323 + x13)^2 + (-0.851790218430218 + x14)^2 + (
    -0.03852729140159916 + x15)^2) + x463 * ((-0.6321580948524517 + x13)^2 + (
    -0.9837962600945337 + x14)^2 + (-0.6794575866782234 + x15)^2) + x464 * ((
    -0.4741167244817951 + x13)^2 + (-0.7294796721116216 + x14)^2 + (
    -0.320613514728746 + x15)^2) + x465 * ((-0.4456710628183016 + x13)^2 + (
    -0.7380410763666608 + x14)^2 + (-0.38742562758632604 + x15)^2) + x466 * ((
    -0.4265716203395923 + x13)^2 + (-0.7118497351712431 + x14)^2 + (
    -0.7471218555436548 + x15)^2) + x467 * ((-0.23627512847494803 + x13)^2 + (
    -0.5038323922445893 + x14)^2 + (-0.2680376794418369 + x15)^2) + x468 * ((
    -0.8404317556608962 + x13)^2 + (-0.04318546277231472 + x14)^2 + (
    -0.14297270654389005 + x15)^2) + x469 * ((-0.6081062742820188 + x13)^2 + (
    -0.05792573185555616 + x14)^2 + (-0.30572046931736474 + x15)^2) + x470 * ((
    -0.8279542917657221 + x13)^2 + (-0.40201952243043027 + x14)^2 + (
    -0.9469372713050586 + x15)^2) + x471 * ((-0.3415766860940366 + x13)^2 + (
    -0.7667328034595803 + x14)^2 + (-0.5561511348714728 + x15)^2) + x472 * ((
    -0.8766850760174327 + x13)^2 + (-0.47568865268531624 + x14)^2 + (
    -0.9457622702235593 + x15)^2) + x473 * ((-0.060732953253662125 + x13)^2 + (
    -0.43044333590426787 + x14)^2 + (-0.11068204021696582 + x15)^2) + x474 * ((
    -0.5599647447657621 + x13)^2 + (-0.20168813274597885 + x14)^2 + (
    -0.04901731419867861 + x15)^2) + x475 * ((-0.918340292529652 + x13)^2 + (
    -0.3592948253121985 + x14)^2 + (-0.27641861869779194 + x15)^2) + x476 * ((
    -0.2290803422518174 + x13)^2 + (-0.9550196585033648 + x14)^2 + (
    -0.18525883987424996 + x15)^2) + x477 * ((-0.07874295854309366 + x13)^2 + (
    -0.5872376176569806 + x14)^2 + (-0.9964507911035481 + x15)^2) + x478 * ((
    -0.8366839476155882 + x13)^2 + (-0.48096052774158937 + x14)^2 + (
    -0.06875812181004981 + x15)^2) + x479 * ((-0.1646012318827148 + x13)^2 + (
    -0.8255025770989258 + x14)^2 + (-0.5425920043205046 + x15)^2) + x480 * ((
    -0.01206407820830957 + x13)^2 + (-0.7715259933915151 + x14)^2 + (
    -0.8153035946330994 + x15)^2) + x481 * ((-0.656216971146405 + x13)^2 + (
    -0.5038530509474157 + x14)^2 + (-0.24858472460284653 + x15)^2) + x482 * ((
    -0.5909087410955904 + x13)^2 + (-0.24200083344880052 + x14)^2 + (
    -0.2773029284079601 + x15)^2) + x483 * ((-0.30683539741159116 + x13)^2 + (
    -0.1592566555556567 + x14)^2 + (-0.8741709441944726 + x15)^2) + x484 * ((
    -0.9696553356372961 + x13)^2 + (-0.5092140919799073 + x14)^2 + (
    -0.9667357424486342 + x15)^2) + x485 * ((-0.022500436859610784 + x13)^2 + (
    -0.09449938113730139 + x14)^2 + (-0.8914880525816652 + x15)^2) + x486 * ((
    -0.03312939739236054 + x13)^2 + (-0.901942581170032 + x14)^2 + (
    -0.4786651787509474 + x15)^2) + x487 * ((-0.9087943615369551 + x13)^2 + (
    -0.16708419935758345 + x14)^2 + (-0.49548708669584307 + x15)^2) + x488 * ((
    -0.2797850906327509 + x13)^2 + (-0.6710488947711567 + x14)^2 + (
    -0.9586698953495221 + x15)^2) + x489 * ((-0.7571140653627548 + x13)^2 + (
    -0.9772776196167088 + x14)^2 + (-0.545818457398843 + x15)^2) + x490 * ((
    -0.4393881718780316 + x13)^2 + (-0.30502275122869604 + x14)^2 + (
    -0.46993652125745644 + x15)^2) + x491 * ((-0.8328586457197023 + x13)^2 + (
    -0.4665403743372396 + x14)^2 + (-0.044871269867679975 + x15)^2) + x492 * ((
    -0.200399479778539 + x13)^2 + (-0.5930767654991737 + x14)^2 + (
    -0.8532214199144125 + x15)^2) + x493 * ((-0.6635666941849311 + x13)^2 + (
    -0.23391286076708295 + x14)^2 + (-0.4140175544317234 + x15)^2) + x494 * ((
    -0.8017608133257321 + x13)^2 + (-0.8877780696226963 + x14)^2 + (
    -0.7221004582069167 + x15)^2) + x495 * ((-0.7399476414219266 + x13)^2 + (
    -0.7138733629252807 + x14)^2 + (-0.40138791158993503 + x15)^2) + x496 * ((
    -0.505308046012709 + x13)^2 + (-0.050203195063672656 + x14)^2 + (
    -0.047366160401361546 + x15)^2) + x497 * ((-0.16774593722409648 + x13)^2 +
    (-0.6409647710984233 + x14)^2 + (-0.10357005758294846 + x15)^2) + x498 * ((
    -0.831240181700394 + x13)^2 + (-0.8086369689577492 + x14)^2 + (
    -0.8697211693425991 + x15)^2) + x499 * ((-0.9508107670055634 + x13)^2 + (
    -0.6593445284740111 + x14)^2 + (-0.9654494903581963 + x15)^2) + x500 * ((
    -0.9689135289592058 + x13)^2 + (-0.2919924557860033 + x14)^2 + (
    -0.674556583609974 + x15)^2) + x501 * ((-0.5755637731737744 + x13)^2 + (
    -0.029158659146738986 + x14)^2 + (-0.801474333934095 + x15)^2) + x502 * ((
    -0.8814332005944923 + x13)^2 + (-0.9388442894563516 + x14)^2 + (
    -0.2609463697280877 + x15)^2) + x503 * ((-0.21089837943522027 + x13)^2 + (
    -0.339246197282862 + x14)^2 + (-0.3206846661656354 + x15)^2) + x504 * ((
    -0.1546689851574372 + x13)^2 + (-0.9006244078114634 + x14)^2 + (
    -0.383032353156448 + x15)^2) + x505 * ((-0.8898729322311727 + x13)^2 + (
    -0.4755652980462777 + x14)^2 + (-0.22139675941977732 + x15)^2) + x506 * ((
    -0.09681202208693973 + x13)^2 + (-0.5759917076295475 + x14)^2 + (
    -0.5453594292179953 + x15)^2) + x507 * ((-0.22092996837157597 + x13)^2 + (
    -0.46898066660462867 + x14)^2 + (-0.586705478616356 + x15)^2) + x508 * ((
    -0.7772286323779445 + x13)^2 + (-0.19088116193826554 + x14)^2 + (
    -0.856917751975287 + x15)^2) + x509 * ((-0.5698804350762819 + x13)^2 + (
    -0.6223743600871902 + x14)^2 + (-0.8005394562016571 + x15)^2) + x510 * ((
    -0.8378639929136145 + x13)^2 + (-0.2593791410480174 + x14)^2 + (
    -0.952835706880077 + x15)^2) + x511 * ((-0.5664183009185346 + x13)^2 + (
    -0.6409573923329756 + x14)^2 + (-0.14836446543357706 + x15)^2) + x512 * ((
    -0.668276613592165 + x13)^2 + (-0.3935536704179623 + x14)^2 + (
    -0.7892941738310548 + x15)^2) + x513 * ((-0.5909840584373237 + x13)^2 + (
    -0.711000971518637 + x14)^2 + (-0.5102861967453806 + x15)^2) + x514 * ((
    -0.7504540204056493 + x13)^2 + (-0.28794681403074973 + x14)^2 + (
    -0.10805205635438697 + x15)^2) + x515 * ((-0.36208849153434675 + x13)^2 + (
    -0.8604979220194023 + x14)^2 + (-0.7543109859318823 + x15)^2) + x516 * ((
    -0.3204638627624359 + x13)^2 + (-0.6985597618075823 + x14)^2 + (
    -0.6884286859796227 + x15)^2) + x517 * ((-0.28040948702637747 + x13)^2 + (
    -0.09782856158952724 + x14)^2 + (-0.5554865157339168 + x15)^2) + x518 * ((
    -0.6650013860062475 + x13)^2 + (-0.4148870776087248 + x14)^2 + (
    -0.13580061730735504 + x15)^2) + x519 * ((-0.42984003511582325 + x16)^2 + (
    -0.5248188211614745 + x17)^2 + (-0.18976547031166158 + x18)^2) + x520 * ((
    -0.7635437892676484 + x16)^2 + (-0.2087128118532261 + x17)^2 + (
    -0.7237865537648877 + x18)^2) + x521 * ((-0.37894209230263076 + x16)^2 + (
    -0.673972806556101 + x17)^2 + (-0.7804374363770062 + x18)^2) + x522 * ((
    -0.03600961414337911 + x16)^2 + (-0.9432908341465497 + x17)^2 + (
    -0.056683718162081176 + x18)^2) + x523 * ((-0.9007184159570817 + x16)^2 + (
    -0.0739499095247852 + x17)^2 + (-0.8655569455322819 + x18)^2) + x524 * ((
    -0.5768605519499145 + x16)^2 + (-0.5986981803675213 + x17)^2 + (
    -0.6570355091518676 + x18)^2) + x525 * ((-0.9745811766548338 + x16)^2 + (
    -0.41474680749048254 + x17)^2 + (-0.9237263978620873 + x18)^2) + x526 * ((
    -0.06206593318927589 + x16)^2 + (-0.2651214371091045 + x17)^2 + (
    -0.6015632454359485 + x18)^2) + x527 * ((-0.6112553172986112 + x16)^2 + (
    -0.8236130985530066 + x17)^2 + (-0.7552731749526171 + x18)^2) + x528 * ((
    -0.2824557711903295 + x16)^2 + (-0.3301346471734301 + x17)^2 + (
    -0.4003642371172418 + x18)^2) + x529 * ((-0.22380220476030066 + x16)^2 + (
    -0.8814483924491749 + x17)^2 + (-0.880102192625681 + x18)^2) + x530 * ((
    -0.5378330969721621 + x16)^2 + (-0.5263672319237694 + x17)^2 + (
    -0.008305374485281347 + x18)^2) + x531 * ((-0.8368636165739145 + x16)^2 + (
    -0.5178975931573176 + x17)^2 + (-0.19654398351590685 + x18)^2) + x532 * ((
    -0.8033599255036961 + x16)^2 + (-0.5470921616898407 + x17)^2 + (
    -0.05989580899877456 + x18)^2) + x533 * ((-0.5041669891441031 + x16)^2 + (
    -0.19483851577422762 + x17)^2 + (-0.04121006383916248 + x18)^2) + x534 * ((
    -0.2735550274413898 + x16)^2 + (-0.5771711903673603 + x17)^2 + (
    -0.8483920722526949 + x18)^2) + x535 * ((-0.16341280932131008 + x16)^2 + (
    -0.38595898916250637 + x17)^2 + (-0.7240527965923388 + x18)^2) + x536 * ((
    -0.184735914655195 + x16)^2 + (-0.9074851747165764 + x17)^2 + (
    -0.5092578035597556 + x18)^2) + x537 * ((-0.667717591753409 + x16)^2 + (
    -0.03611089878214757 + x17)^2 + (-0.5314088140520232 + x18)^2) + x538 * ((
    -0.22082508524283118 + x16)^2 + (-0.14591083104017755 + x17)^2 + (
    -0.4966365264689938 + x18)^2) + x539 * ((-0.8131501378134828 + x16)^2 + (
    -0.12233837490110344 + x17)^2 + (-0.6422164007166057 + x18)^2) + x540 * ((
    -0.5093801089140564 + x16)^2 + (-0.5913076324087453 + x17)^2 + (
    -0.22564192034703445 + x18)^2) + x541 * ((-0.5886418065986404 + x16)^2 + (
    -0.051216403584171344 + x17)^2 + (-0.21124855487984584 + x18)^2) + x542 * (
    (-0.2822083632452721 + x16)^2 + (-0.6609969862369512 + x17)^2 + (
    -0.629237720221342 + x18)^2) + x543 * ((-0.800850840990083 + x16)^2 + (
    -0.2946478937198632 + x17)^2 + (-0.9711075538538692 + x18)^2) + x544 * ((
    -0.18106474877236667 + x16)^2 + (-0.40222650110712255 + x17)^2 + (
    -0.8640061178144425 + x18)^2) + x545 * ((-0.275960867663125 + x16)^2 + (
    -0.8101752183427954 + x17)^2 + (-0.25463108721162286 + x18)^2) + x546 * ((
    -0.09762964668322405 + x16)^2 + (-0.5681164167758985 + x17)^2 + (
    -0.8522588975167438 + x18)^2) + x547 * ((-0.6792262546121857 + x16)^2 + (
    -0.5415479570871046 + x17)^2 + (-0.9198959530376973 + x18)^2) + x548 * ((
    -0.35974899392373416 + x16)^2 + (-0.9692174411067974 + x17)^2 + (
    -0.8173895217629372 + x18)^2) + x549 * ((-0.2775683808009408 + x16)^2 + (
    -0.07111011846817805 + x17)^2 + (-0.9119005527157927 + x18)^2) + x550 * ((
    -0.8728420280238173 + x16)^2 + (-0.4810753656025001 + x17)^2 + (
    -0.5690581714245571 + x18)^2) + x551 * ((-0.3697310611408884 + x16)^2 + (
    -0.8009586582771799 + x17)^2 + (-0.4509367154437284 + x18)^2) + x552 * ((
    -0.40344052086211035 + x16)^2 + (-0.4549860124364724 + x17)^2 + (
    -0.6928018828898217 + x18)^2) + x553 * ((-0.6361863652853047 + x16)^2 + (
    -0.08988225677383088 + x17)^2 + (-0.25890016105768476 + x18)^2) + x554 * ((
    -0.5670078574144451 + x16)^2 + (-0.11962369435126274 + x17)^2 + (
    -0.7694906824065785 + x18)^2) + x555 * ((-0.2970981185523963 + x16)^2 + (
    -0.07089711937031118 + x17)^2 + (-0.3726754551130945 + x18)^2) + x556 * ((
    -0.9463316541147765 + x16)^2 + (-0.5815980777027693 + x17)^2 + (
    -0.09183246305662951 + x18)^2) + x557 * ((-0.4971616963185841 + x16)^2 + (
    -0.5526690085093273 + x17)^2 + (-0.041586056367461044 + x18)^2) + x558 * ((
    -0.48472198232839325 + x16)^2 + (-0.5137822134278897 + x17)^2 + (
    -0.25761582576168296 + x18)^2) + x559 * ((-0.44694684190755307 + x16)^2 + (
    -0.9335294451364397 + x17)^2 + (-0.6212310214093625 + x18)^2) + x560 * ((
    -0.5456179874167029 + x16)^2 + (-0.6257723725570918 + x17)^2 + (
    -0.44030482106573443 + x18)^2) + x561 * ((-0.48291634635300573 + x16)^2 + (
    -0.8500599447417776 + x17)^2 + (-0.8150332638475819 + x18)^2) + x562 * ((
    -0.2076752515318323 + x16)^2 + (-0.851790218430218 + x17)^2 + (
    -0.03852729140159916 + x18)^2) + x563 * ((-0.6321580948524517 + x16)^2 + (
    -0.9837962600945337 + x17)^2 + (-0.6794575866782234 + x18)^2) + x564 * ((
    -0.4741167244817951 + x16)^2 + (-0.7294796721116216 + x17)^2 + (
    -0.320613514728746 + x18)^2) + x565 * ((-0.4456710628183016 + x16)^2 + (
    -0.7380410763666608 + x17)^2 + (-0.38742562758632604 + x18)^2) + x566 * ((
    -0.4265716203395923 + x16)^2 + (-0.7118497351712431 + x17)^2 + (
    -0.7471218555436548 + x18)^2) + x567 * ((-0.23627512847494803 + x16)^2 + (
    -0.5038323922445893 + x17)^2 + (-0.2680376794418369 + x18)^2) + x568 * ((
    -0.8404317556608962 + x16)^2 + (-0.04318546277231472 + x17)^2 + (
    -0.14297270654389005 + x18)^2) + x569 * ((-0.6081062742820188 + x16)^2 + (
    -0.05792573185555616 + x17)^2 + (-0.30572046931736474 + x18)^2) + x570 * ((
    -0.8279542917657221 + x16)^2 + (-0.40201952243043027 + x17)^2 + (
    -0.9469372713050586 + x18)^2) + x571 * ((-0.3415766860940366 + x16)^2 + (
    -0.7667328034595803 + x17)^2 + (-0.5561511348714728 + x18)^2) + x572 * ((
    -0.8766850760174327 + x16)^2 + (-0.47568865268531624 + x17)^2 + (
    -0.9457622702235593 + x18)^2) + x573 * ((-0.060732953253662125 + x16)^2 + (
    -0.43044333590426787 + x17)^2 + (-0.11068204021696582 + x18)^2) + x574 * ((
    -0.5599647447657621 + x16)^2 + (-0.20168813274597885 + x17)^2 + (
    -0.04901731419867861 + x18)^2) + x575 * ((-0.918340292529652 + x16)^2 + (
    -0.3592948253121985 + x17)^2 + (-0.27641861869779194 + x18)^2) + x576 * ((
    -0.2290803422518174 + x16)^2 + (-0.9550196585033648 + x17)^2 + (
    -0.18525883987424996 + x18)^2) + x577 * ((-0.07874295854309366 + x16)^2 + (
    -0.5872376176569806 + x17)^2 + (-0.9964507911035481 + x18)^2) + x578 * ((
    -0.8366839476155882 + x16)^2 + (-0.48096052774158937 + x17)^2 + (
    -0.06875812181004981 + x18)^2) + x579 * ((-0.1646012318827148 + x16)^2 + (
    -0.8255025770989258 + x17)^2 + (-0.5425920043205046 + x18)^2) + x580 * ((
    -0.01206407820830957 + x16)^2 + (-0.7715259933915151 + x17)^2 + (
    -0.8153035946330994 + x18)^2) + x581 * ((-0.656216971146405 + x16)^2 + (
    -0.5038530509474157 + x17)^2 + (-0.24858472460284653 + x18)^2) + x582 * ((
    -0.5909087410955904 + x16)^2 + (-0.24200083344880052 + x17)^2 + (
    -0.2773029284079601 + x18)^2) + x583 * ((-0.30683539741159116 + x16)^2 + (
    -0.1592566555556567 + x17)^2 + (-0.8741709441944726 + x18)^2) + x584 * ((
    -0.9696553356372961 + x16)^2 + (-0.5092140919799073 + x17)^2 + (
    -0.9667357424486342 + x18)^2) + x585 * ((-0.022500436859610784 + x16)^2 + (
    -0.09449938113730139 + x17)^2 + (-0.8914880525816652 + x18)^2) + x586 * ((
    -0.03312939739236054 + x16)^2 + (-0.901942581170032 + x17)^2 + (
    -0.4786651787509474 + x18)^2) + x587 * ((-0.9087943615369551 + x16)^2 + (
    -0.16708419935758345 + x17)^2 + (-0.49548708669584307 + x18)^2) + x588 * ((
    -0.2797850906327509 + x16)^2 + (-0.6710488947711567 + x17)^2 + (
    -0.9586698953495221 + x18)^2) + x589 * ((-0.7571140653627548 + x16)^2 + (
    -0.9772776196167088 + x17)^2 + (-0.545818457398843 + x18)^2) + x590 * ((
    -0.4393881718780316 + x16)^2 + (-0.30502275122869604 + x17)^2 + (
    -0.46993652125745644 + x18)^2) + x591 * ((-0.8328586457197023 + x16)^2 + (
    -0.4665403743372396 + x17)^2 + (-0.044871269867679975 + x18)^2) + x592 * ((
    -0.200399479778539 + x16)^2 + (-0.5930767654991737 + x17)^2 + (
    -0.8532214199144125 + x18)^2) + x593 * ((-0.6635666941849311 + x16)^2 + (
    -0.23391286076708295 + x17)^2 + (-0.4140175544317234 + x18)^2) + x594 * ((
    -0.8017608133257321 + x16)^2 + (-0.8877780696226963 + x17)^2 + (
    -0.7221004582069167 + x18)^2) + x595 * ((-0.7399476414219266 + x16)^2 + (
    -0.7138733629252807 + x17)^2 + (-0.40138791158993503 + x18)^2) + x596 * ((
    -0.505308046012709 + x16)^2 + (-0.050203195063672656 + x17)^2 + (
    -0.047366160401361546 + x18)^2) + x597 * ((-0.16774593722409648 + x16)^2 +
    (-0.6409647710984233 + x17)^2 + (-0.10357005758294846 + x18)^2) + x598 * ((
    -0.831240181700394 + x16)^2 + (-0.8086369689577492 + x17)^2 + (
    -0.8697211693425991 + x18)^2) + x599 * ((-0.9508107670055634 + x16)^2 + (
    -0.6593445284740111 + x17)^2 + (-0.9654494903581963 + x18)^2) + x600 * ((
    -0.9689135289592058 + x16)^2 + (-0.2919924557860033 + x17)^2 + (
    -0.674556583609974 + x18)^2) + x601 * ((-0.5755637731737744 + x16)^2 + (
    -0.029158659146738986 + x17)^2 + (-0.801474333934095 + x18)^2) + x602 * ((
    -0.8814332005944923 + x16)^2 + (-0.9388442894563516 + x17)^2 + (
    -0.2609463697280877 + x18)^2) + x603 * ((-0.21089837943522027 + x16)^2 + (
    -0.339246197282862 + x17)^2 + (-0.3206846661656354 + x18)^2) + x604 * ((
    -0.1546689851574372 + x16)^2 + (-0.9006244078114634 + x17)^2 + (
    -0.383032353156448 + x18)^2) + x605 * ((-0.8898729322311727 + x16)^2 + (
    -0.4755652980462777 + x17)^2 + (-0.22139675941977732 + x18)^2) + x606 * ((
    -0.09681202208693973 + x16)^2 + (-0.5759917076295475 + x17)^2 + (
    -0.5453594292179953 + x18)^2) + x607 * ((-0.22092996837157597 + x16)^2 + (
    -0.46898066660462867 + x17)^2 + (-0.586705478616356 + x18)^2) + x608 * ((
    -0.7772286323779445 + x16)^2 + (-0.19088116193826554 + x17)^2 + (
    -0.856917751975287 + x18)^2) + x609 * ((-0.5698804350762819 + x16)^2 + (
    -0.6223743600871902 + x17)^2 + (-0.8005394562016571 + x18)^2) + x610 * ((
    -0.8378639929136145 + x16)^2 + (-0.2593791410480174 + x17)^2 + (
    -0.952835706880077 + x18)^2) + x611 * ((-0.5664183009185346 + x16)^2 + (
    -0.6409573923329756 + x17)^2 + (-0.14836446543357706 + x18)^2) + x612 * ((
    -0.668276613592165 + x16)^2 + (-0.3935536704179623 + x17)^2 + (
    -0.7892941738310548 + x18)^2) + x613 * ((-0.5909840584373237 + x16)^2 + (
    -0.711000971518637 + x17)^2 + (-0.5102861967453806 + x18)^2) + x614 * ((
    -0.7504540204056493 + x16)^2 + (-0.28794681403074973 + x17)^2 + (
    -0.10805205635438697 + x18)^2) + x615 * ((-0.36208849153434675 + x16)^2 + (
    -0.8604979220194023 + x17)^2 + (-0.7543109859318823 + x18)^2) + x616 * ((
    -0.3204638627624359 + x16)^2 + (-0.6985597618075823 + x17)^2 + (
    -0.6884286859796227 + x18)^2) + x617 * ((-0.28040948702637747 + x16)^2 + (
    -0.09782856158952724 + x17)^2 + (-0.5554865157339168 + x18)^2) + x618 * ((
    -0.6650013860062475 + x16)^2 + (-0.4148870776087248 + x17)^2 + (
    -0.13580061730735504 + x18)^2))

@constraint(m, e1, x19 + x119 + x219 + x319 + x419 + x519 == 1)
@constraint(m, e2, x20 + x120 + x220 + x320 + x420 + x520 == 1)
@constraint(m, e3, x21 + x121 + x221 + x321 + x421 + x521 == 1)
@constraint(m, e4, x22 + x122 + x222 + x322 + x422 + x522 == 1)
@constraint(m, e5, x23 + x123 + x223 + x323 + x423 + x523 == 1)
@constraint(m, e6, x24 + x124 + x224 + x324 + x424 + x524 == 1)
@constraint(m, e7, x25 + x125 + x225 + x325 + x425 + x525 == 1)
@constraint(m, e8, x26 + x126 + x226 + x326 + x426 + x526 == 1)
@constraint(m, e9, x27 + x127 + x227 + x327 + x427 + x527 == 1)
@constraint(m, e10, x28 + x128 + x228 + x328 + x428 + x528 == 1)
@constraint(m, e11, x29 + x129 + x229 + x329 + x429 + x529 == 1)
@constraint(m, e12, x30 + x130 + x230 + x330 + x430 + x530 == 1)
@constraint(m, e13, x31 + x131 + x231 + x331 + x431 + x531 == 1)
@constraint(m, e14, x32 + x132 + x232 + x332 + x432 + x532 == 1)
@constraint(m, e15, x33 + x133 + x233 + x333 + x433 + x533 == 1)
@constraint(m, e16, x34 + x134 + x234 + x334 + x434 + x534 == 1)
@constraint(m, e17, x35 + x135 + x235 + x335 + x435 + x535 == 1)
@constraint(m, e18, x36 + x136 + x236 + x336 + x436 + x536 == 1)
@constraint(m, e19, x37 + x137 + x237 + x337 + x437 + x537 == 1)
@constraint(m, e20, x38 + x138 + x238 + x338 + x438 + x538 == 1)
@constraint(m, e21, x39 + x139 + x239 + x339 + x439 + x539 == 1)
@constraint(m, e22, x40 + x140 + x240 + x340 + x440 + x540 == 1)
@constraint(m, e23, x41 + x141 + x241 + x341 + x441 + x541 == 1)
@constraint(m, e24, x42 + x142 + x242 + x342 + x442 + x542 == 1)
@constraint(m, e25, x43 + x143 + x243 + x343 + x443 + x543 == 1)
@constraint(m, e26, x44 + x144 + x244 + x344 + x444 + x544 == 1)
@constraint(m, e27, x45 + x145 + x245 + x345 + x445 + x545 == 1)
@constraint(m, e28, x46 + x146 + x246 + x346 + x446 + x546 == 1)
@constraint(m, e29, x47 + x147 + x247 + x347 + x447 + x547 == 1)
@constraint(m, e30, x48 + x148 + x248 + x348 + x448 + x548 == 1)
@constraint(m, e31, x49 + x149 + x249 + x349 + x449 + x549 == 1)
@constraint(m, e32, x50 + x150 + x250 + x350 + x450 + x550 == 1)
@constraint(m, e33, x51 + x151 + x251 + x351 + x451 + x551 == 1)
@constraint(m, e34, x52 + x152 + x252 + x352 + x452 + x552 == 1)
@constraint(m, e35, x53 + x153 + x253 + x353 + x453 + x553 == 1)
@constraint(m, e36, x54 + x154 + x254 + x354 + x454 + x554 == 1)
@constraint(m, e37, x55 + x155 + x255 + x355 + x455 + x555 == 1)
@constraint(m, e38, x56 + x156 + x256 + x356 + x456 + x556 == 1)
@constraint(m, e39, x57 + x157 + x257 + x357 + x457 + x557 == 1)
@constraint(m, e40, x58 + x158 + x258 + x358 + x458 + x558 == 1)
@constraint(m, e41, x59 + x159 + x259 + x359 + x459 + x559 == 1)
@constraint(m, e42, x60 + x160 + x260 + x360 + x460 + x560 == 1)
@constraint(m, e43, x61 + x161 + x261 + x361 + x461 + x561 == 1)
@constraint(m, e44, x62 + x162 + x262 + x362 + x462 + x562 == 1)
@constraint(m, e45, x63 + x163 + x263 + x363 + x463 + x563 == 1)
@constraint(m, e46, x64 + x164 + x264 + x364 + x464 + x564 == 1)
@constraint(m, e47, x65 + x165 + x265 + x365 + x465 + x565 == 1)
@constraint(m, e48, x66 + x166 + x266 + x366 + x466 + x566 == 1)
@constraint(m, e49, x67 + x167 + x267 + x367 + x467 + x567 == 1)
@constraint(m, e50, x68 + x168 + x268 + x368 + x468 + x568 == 1)
@constraint(m, e51, x69 + x169 + x269 + x369 + x469 + x569 == 1)
@constraint(m, e52, x70 + x170 + x270 + x370 + x470 + x570 == 1)
@constraint(m, e53, x71 + x171 + x271 + x371 + x471 + x571 == 1)
@constraint(m, e54, x72 + x172 + x272 + x372 + x472 + x572 == 1)
@constraint(m, e55, x73 + x173 + x273 + x373 + x473 + x573 == 1)
@constraint(m, e56, x74 + x174 + x274 + x374 + x474 + x574 == 1)
@constraint(m, e57, x75 + x175 + x275 + x375 + x475 + x575 == 1)
@constraint(m, e58, x76 + x176 + x276 + x376 + x476 + x576 == 1)
@constraint(m, e59, x77 + x177 + x277 + x377 + x477 + x577 == 1)
@constraint(m, e60, x78 + x178 + x278 + x378 + x478 + x578 == 1)
@constraint(m, e61, x79 + x179 + x279 + x379 + x479 + x579 == 1)
@constraint(m, e62, x80 + x180 + x280 + x380 + x480 + x580 == 1)
@constraint(m, e63, x81 + x181 + x281 + x381 + x481 + x581 == 1)
@constraint(m, e64, x82 + x182 + x282 + x382 + x482 + x582 == 1)
@constraint(m, e65, x83 + x183 + x283 + x383 + x483 + x583 == 1)
@constraint(m, e66, x84 + x184 + x284 + x384 + x484 + x584 == 1)
@constraint(m, e67, x85 + x185 + x285 + x385 + x485 + x585 == 1)
@constraint(m, e68, x86 + x186 + x286 + x386 + x486 + x586 == 1)
@constraint(m, e69, x87 + x187 + x287 + x387 + x487 + x587 == 1)
@constraint(m, e70, x88 + x188 + x288 + x388 + x488 + x588 == 1)
@constraint(m, e71, x89 + x189 + x289 + x389 + x489 + x589 == 1)
@constraint(m, e72, x90 + x190 + x290 + x390 + x490 + x590 == 1)
@constraint(m, e73, x91 + x191 + x291 + x391 + x491 + x591 == 1)
@constraint(m, e74, x92 + x192 + x292 + x392 + x492 + x592 == 1)
@constraint(m, e75, x93 + x193 + x293 + x393 + x493 + x593 == 1)
@constraint(m, e76, x94 + x194 + x294 + x394 + x494 + x594 == 1)
@constraint(m, e77, x95 + x195 + x295 + x395 + x495 + x595 == 1)
@constraint(m, e78, x96 + x196 + x296 + x396 + x496 + x596 == 1)
@constraint(m, e79, x97 + x197 + x297 + x397 + x497 + x597 == 1)
@constraint(m, e80, x98 + x198 + x298 + x398 + x498 + x598 == 1)
@constraint(m, e81, x99 + x199 + x299 + x399 + x499 + x599 == 1)
@constraint(m, e82, x100 + x200 + x300 + x400 + x500 + x600 == 1)
@constraint(m, e83, x101 + x201 + x301 + x401 + x501 + x601 == 1)
@constraint(m, e84, x102 + x202 + x302 + x402 + x502 + x602 == 1)
@constraint(m, e85, x103 + x203 + x303 + x403 + x503 + x603 == 1)
@constraint(m, e86, x104 + x204 + x304 + x404 + x504 + x604 == 1)
@constraint(m, e87, x105 + x205 + x305 + x405 + x505 + x605 == 1)
@constraint(m, e88, x106 + x206 + x306 + x406 + x506 + x606 == 1)
@constraint(m, e89, x107 + x207 + x307 + x407 + x507 + x607 == 1)
@constraint(m, e90, x108 + x208 + x308 + x408 + x508 + x608 == 1)
@constraint(m, e91, x109 + x209 + x309 + x409 + x509 + x609 == 1)
@constraint(m, e92, x110 + x210 + x310 + x410 + x510 + x610 == 1)
@constraint(m, e93, x111 + x211 + x311 + x411 + x511 + x611 == 1)
@constraint(m, e94, x112 + x212 + x312 + x412 + x512 + x612 == 1)
@constraint(m, e95, x113 + x213 + x313 + x413 + x513 + x613 == 1)
@constraint(m, e96, x114 + x214 + x314 + x414 + x514 + x614 == 1)
@constraint(m, e97, x115 + x215 + x315 + x415 + x515 + x615 == 1)
@constraint(m, e98, x116 + x216 + x316 + x416 + x516 + x616 == 1)
@constraint(m, e99, x117 + x217 + x317 + x417 + x517 + x617 == 1)
@constraint(m, e100, x118 + x218 + x318 + x418 + x518 + x618 == 1)
