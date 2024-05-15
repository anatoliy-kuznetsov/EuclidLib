# NLP written by GAMS Convert at 05/15/24 11:24:21
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       100      100        0        0        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#       824      824        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       800      800        0
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

@NLobjective(m, Min, x25 * ((-0.18738087377060708 + x1)^2 + (
    -0.9668125465448587 + x2)^2 + (-0.3553159637279516 + x3)^2) + x26 * ((
    -0.8016174920011017 + x1)^2 + (-0.26778829228978485 + x2)^2 + (
    -0.4359301947251404 + x3)^2) + x27 * ((-0.8607174064209905 + x1)^2 + (
    -0.9118236037302004 + x2)^2 + (-0.8874753085224066 + x3)^2) + x28 * ((
    -0.4306937407201691 + x1)^2 + (-0.17428784944790254 + x2)^2 + (
    -0.561800026051346 + x3)^2) + x29 * ((-0.08746124891679041 + x1)^2 + (
    -0.054985697990341253 + x2)^2 + (-0.24949780749022454 + x3)^2) + x30 * ((
    -0.62658802169963 + x1)^2 + (-0.6857573511475539 + x2)^2 + (
    -0.47366426896437996 + x3)^2) + x31 * ((-0.6114768638799523 + x1)^2 + (
    -0.41752031846706683 + x2)^2 + (-0.9109986593014991 + x3)^2) + x32 * ((
    -0.46817035806173857 + x1)^2 + (-0.5569854753991196 + x2)^2 + (
    -0.25003006243034176 + x3)^2) + x33 * ((-0.401092643486621 + x1)^2 + (
    -0.7625123366098691 + x2)^2 + (-0.5084739888197645 + x3)^2) + x34 * ((
    -0.2748596346062746 + x1)^2 + (-0.1892957165775404 + x2)^2 + (
    -0.9442182422598734 + x3)^2) + x35 * ((-0.44167309428028 + x1)^2 + (
    -0.33521919326002436 + x2)^2 + (-0.5030312028077185 + x3)^2) + x36 * ((
    -0.7052213106378172 + x1)^2 + (-0.48063756935051416 + x2)^2 + (
    -0.26073089985191056 + x3)^2) + x37 * ((-0.34955478256076744 + x1)^2 + (
    -0.08326067710845486 + x2)^2 + (-0.5749118628581387 + x3)^2) + x38 * ((
    -0.559986490193569 + x1)^2 + (-0.8433283983822369 + x2)^2 + (
    -0.2573012139171522 + x3)^2) + x39 * ((-0.15759317998774103 + x1)^2 + (
    -0.876898613808363 + x2)^2 + (-0.7812095651757611 + x3)^2) + x40 * ((
    -0.20930481325083095 + x1)^2 + (-0.5243112169526106 + x2)^2 + (
    -0.11364820868480618 + x3)^2) + x41 * ((-0.6971614684173857 + x1)^2 + (
    -0.48152793919664516 + x2)^2 + (-0.10432894263476011 + x3)^2) + x42 * ((
    -0.9788390123597811 + x1)^2 + (-0.6759032973315947 + x2)^2 + (
    -0.9815212516574683 + x3)^2) + x43 * ((-0.31006923192398295 + x1)^2 + (
    -0.9279588991073839 + x2)^2 + (-0.6170791410768803 + x3)^2) + x44 * ((
    -0.2636621784047203 + x1)^2 + (-0.5756031327528047 + x2)^2 + (
    -0.6339965151056094 + x3)^2) + x45 * ((-0.07735274294755135 + x1)^2 + (
    -0.7932728374366258 + x2)^2 + (-0.3905222095735743 + x3)^2) + x46 * ((
    -0.9596478643023862 + x1)^2 + (-0.8323332845748266 + x2)^2 + (
    -0.9490817947377156 + x3)^2) + x47 * ((-0.691877291867759 + x1)^2 + (
    -0.27901589567669627 + x2)^2 + (-0.9603405866805156 + x3)^2) + x48 * ((
    -0.3248230089198071 + x1)^2 + (-0.704031342612858 + x2)^2 + (
    -0.6022746223457217 + x3)^2) + x49 * ((-0.7925246012498328 + x1)^2 + (
    -0.5142003887500619 + x2)^2 + (-0.07412078079700912 + x3)^2) + x50 * ((
    -0.4636597419285817 + x1)^2 + (-0.28493324045279156 + x2)^2 + (
    -0.8982018087470489 + x3)^2) + x51 * ((-0.3125245397681232 + x1)^2 + (
    -0.25776762798299757 + x2)^2 + (-0.05720177574934948 + x3)^2) + x52 * ((
    -0.3197520940611892 + x1)^2 + (-0.8476152339851849 + x2)^2 + (
    -0.36763530621177176 + x3)^2) + x53 * ((-0.7452568897412712 + x1)^2 + (
    -0.24553180487125725 + x2)^2 + (-0.5097535241044541 + x3)^2) + x54 * ((
    -0.7098335381446684 + x1)^2 + (-0.8340974705497336 + x2)^2 + (
    -0.181763781584372 + x3)^2) + x55 * ((-0.46361936352247957 + x1)^2 + (
    -0.5052840929896205 + x2)^2 + (-0.44590180298842885 + x3)^2) + x56 * ((
    -0.38556721731694843 + x1)^2 + (-0.8579051939296445 + x2)^2 + (
    -0.9532247922542321 + x3)^2) + x57 * ((-0.08582521461459391 + x1)^2 + (
    -0.1846731910506113 + x2)^2 + (-0.8745914265553065 + x3)^2) + x58 * ((
    -0.8832914121602843 + x1)^2 + (-0.6513632907999211 + x2)^2 + (
    -0.21823458079012226 + x3)^2) + x59 * ((-0.5751096041706857 + x1)^2 + (
    -0.67547809352205 + x2)^2 + (-0.02460221547003949 + x3)^2) + x60 * ((
    -0.31457012214576896 + x1)^2 + (-0.6742238394444281 + x2)^2 + (
    -0.5445193883971214 + x3)^2) + x61 * ((-0.11915949121286373 + x1)^2 + (
    -0.7063249001765594 + x2)^2 + (-0.2705862773526916 + x3)^2) + x62 * ((
    -0.6669226676581618 + x1)^2 + (-0.5285881831609426 + x2)^2 + (
    -0.11309761756326353 + x3)^2) + x63 * ((-0.12347539452476952 + x1)^2 + (
    -0.39576104678223545 + x2)^2 + (-0.5346277380867844 + x3)^2) + x64 * ((
    -0.6078285274199232 + x1)^2 + (-0.14297039718498794 + x2)^2 + (
    -0.9770203015468777 + x3)^2) + x65 * ((-0.3646785363094529 + x1)^2 + (
    -0.7442303679522239 + x2)^2 + (-0.6078205952200681 + x3)^2) + x66 * ((
    -0.5210217205095699 + x1)^2 + (-0.8432559359514145 + x2)^2 + (
    -0.22452982644506148 + x3)^2) + x67 * ((-0.08751493934711652 + x1)^2 + (
    -0.4416120245181858 + x2)^2 + (-0.026527914551422116 + x3)^2) + x68 * ((
    -0.01197633335476489 + x1)^2 + (-0.2890291018825958 + x2)^2 + (
    -0.38681268974270067 + x3)^2) + x69 * ((-0.7095057303156089 + x1)^2 + (
    -0.931861745530449 + x2)^2 + (-0.14043671018799309 + x3)^2) + x70 * ((
    -0.0895696243176286 + x1)^2 + (-0.5380623897726036 + x2)^2 + (
    -0.21800740949887965 + x3)^2) + x71 * ((-0.7815676711928884 + x1)^2 + (
    -0.018922864242984283 + x2)^2 + (-0.28596537520912735 + x3)^2) + x72 * ((
    -0.1740875221968632 + x1)^2 + (-0.5678042483964806 + x2)^2 + (
    -0.5661715765543827 + x3)^2) + x73 * ((-0.026589535186742008 + x1)^2 + (
    -0.764188329062881 + x2)^2 + (-0.573675168853155 + x3)^2) + x74 * ((
    -0.369798170078249 + x1)^2 + (-0.9415339432121399 + x2)^2 + (
    -0.6729904295003972 + x3)^2) + x75 * ((-0.8040803150564447 + x1)^2 + (
    -0.1553864280131183 + x2)^2 + (-0.8148818001526622 + x3)^2) + x76 * ((
    -0.26589528353030667 + x1)^2 + (-0.3666027540410405 + x2)^2 + (
    -0.468491747882274 + x3)^2) + x77 * ((-0.7258236750794794 + x1)^2 + (
    -0.6727872398248785 + x2)^2 + (-0.28367538142810256 + x3)^2) + x78 * ((
    -0.9220733933477209 + x1)^2 + (-0.26257553387761134 + x2)^2 + (
    -0.7191645521015703 + x3)^2) + x79 * ((-0.9500341346045207 + x1)^2 + (
    -0.638006708190589 + x2)^2 + (-0.07543033185744508 + x3)^2) + x80 * ((
    -0.10545996998960727 + x1)^2 + (-0.7011113856167448 + x2)^2 + (
    -0.20681983539603999 + x3)^2) + x81 * ((-0.6551186918756842 + x1)^2 + (
    -0.6398068804459004 + x2)^2 + (-0.9931175421141764 + x3)^2) + x82 * ((
    -0.7142120519447257 + x1)^2 + (-0.46243457004259436 + x2)^2 + (
    -0.5481708822495015 + x3)^2) + x83 * ((-0.4950904200820069 + x1)^2 + (
    -0.897797250865998 + x2)^2 + (-0.2346789175833377 + x3)^2) + x84 * ((
    -0.6440952365033279 + x1)^2 + (-0.33381998176403327 + x2)^2 + (
    -0.5869170180027279 + x3)^2) + x85 * ((-0.8591109395866232 + x1)^2 + (
    -0.8400580742862248 + x2)^2 + (-0.7678032609886081 + x3)^2) + x86 * ((
    -0.7791674853861603 + x1)^2 + (-0.45754256977454044 + x2)^2 + (
    -0.30909012057666696 + x3)^2) + x87 * ((-0.8968075661486302 + x1)^2 + (
    -0.34892321725590947 + x2)^2 + (-0.05826567448243425 + x3)^2) + x88 * ((
    -0.3189815847959586 + x1)^2 + (-0.3926628302556219 + x2)^2 + (
    -0.07205292941157881 + x3)^2) + x89 * ((-0.8146221960807916 + x1)^2 + (
    -0.4969763360408802 + x2)^2 + (-0.3647398823672149 + x3)^2) + x90 * ((
    -0.23899160200316316 + x1)^2 + (-0.39386695871622013 + x2)^2 + (
    -0.6832280563167916 + x3)^2) + x91 * ((-0.3505164112410739 + x1)^2 + (
    -0.474289602074489 + x2)^2 + (-0.09409181759710883 + x3)^2) + x92 * ((
    -0.9669824450132469 + x1)^2 + (-0.7209255968341481 + x2)^2 + (
    -0.013074465617943565 + x3)^2) + x93 * ((-0.7769547473829561 + x1)^2 + (
    -0.8065173816239941 + x2)^2 + (-0.7160376893035372 + x3)^2) + x94 * ((
    -0.3489895458178166 + x1)^2 + (-0.35733085724791824 + x2)^2 + (
    -0.8864875891533408 + x3)^2) + x95 * ((-0.0664995679925865 + x1)^2 + (
    -0.7243483038068983 + x2)^2 + (-0.9303195285204333 + x3)^2) + x96 * ((
    -0.8115323501210528 + x1)^2 + (-0.42672295637197755 + x2)^2 + (
    -0.04261529652953755 + x3)^2) + x97 * ((-0.3704618379844066 + x1)^2 + (
    -0.1443368240568217 + x2)^2 + (-0.3776192402141899 + x3)^2) + x98 * ((
    -0.7280090144638749 + x1)^2 + (-0.15636110839409045 + x2)^2 + (
    -0.46978018596620896 + x3)^2) + x99 * ((-0.11088006780742277 + x1)^2 + (
    -0.34039206766760943 + x2)^2 + (-0.06827700620696797 + x3)^2) + x100 * ((
    -0.6997602128647453 + x1)^2 + (-0.43764462531136417 + x2)^2 + (
    -0.21027262835312888 + x3)^2) + x101 * ((-0.04425963668315558 + x1)^2 + (
    -0.05866963958501248 + x2)^2 + (-0.3542816901635206 + x3)^2) + x102 * ((
    -0.9757731519147661 + x1)^2 + (-0.3254673022536907 + x2)^2 + (
    -0.6814338527690927 + x3)^2) + x103 * ((-0.7472668303106704 + x1)^2 + (
    -0.0007097732419126812 + x2)^2 + (-0.9280520527234516 + x3)^2) + x104 * ((
    -0.5322530736526498 + x1)^2 + (-0.39754547356694514 + x2)^2 + (
    -0.13635594663989958 + x3)^2) + x105 * ((-0.0007978441992585461 + x1)^2 + (
    -0.8844692811473446 + x2)^2 + (-0.1467696053297397 + x3)^2) + x106 * ((
    -0.482850676866177 + x1)^2 + (-0.10574453600064249 + x2)^2 + (
    -0.8791132223988765 + x3)^2) + x107 * ((-0.7291125910415815 + x1)^2 + (
    -0.2090180996227905 + x2)^2 + (-0.5040401706411071 + x3)^2) + x108 * ((
    -0.6406085128291104 + x1)^2 + (-0.11496605173886654 + x2)^2 + (
    -0.7597217863145667 + x3)^2) + x109 * ((-0.6527145527530681 + x1)^2 + (
    -0.09871984518132071 + x2)^2 + (-0.08020459573270278 + x3)^2) + x110 * ((
    -0.5779788427476141 + x1)^2 + (-0.6106348650543917 + x2)^2 + (
    -0.21791347819398965 + x3)^2) + x111 * ((-0.894563747191656 + x1)^2 + (
    -0.49991063769677824 + x2)^2 + (-0.8312284742613548 + x3)^2) + x112 * ((
    -0.5477983688744066 + x1)^2 + (-0.10123589526888899 + x2)^2 + (
    -0.9724165689826183 + x3)^2) + x113 * ((-0.7051711697372745 + x1)^2 + (
    -0.6974870695940615 + x2)^2 + (-0.34185115432121194 + x3)^2) + x114 * ((
    -0.965288766829392 + x1)^2 + (-0.3541459265683641 + x2)^2 + (
    -0.5256833284803955 + x3)^2) + x115 * ((-0.486217312364274 + x1)^2 + (
    -0.877880388733161 + x2)^2 + (-0.7007637309302288 + x3)^2) + x116 * ((
    -0.9239018568218517 + x1)^2 + (-0.8696579903239924 + x2)^2 + (
    -0.9905428630635226 + x3)^2) + x117 * ((-0.5635239214739318 + x1)^2 + (
    -0.5212076565782671 + x2)^2 + (-0.672320998946101 + x3)^2) + x118 * ((
    -0.6336849702734496 + x1)^2 + (-0.17934198400132562 + x2)^2 + (
    -0.25720032541892046 + x3)^2) + x119 * ((-0.3593028476464476 + x1)^2 + (
    -0.7339808423425379 + x2)^2 + (-0.001964432484070411 + x3)^2) + x120 * ((
    -0.11194390371791885 + x1)^2 + (-0.05379441414468389 + x2)^2 + (
    -0.943183016792168 + x3)^2) + x121 * ((-0.23043169327406487 + x1)^2 + (
    -0.9554781274626842 + x2)^2 + (-0.7782415771343315 + x3)^2) + x122 * ((
    -0.999963313244285 + x1)^2 + (-0.18638094695235063 + x2)^2 + (
    -0.8044007834975228 + x3)^2) + x123 * ((-0.8484168552839887 + x1)^2 + (
    -0.5800377498791588 + x2)^2 + (-0.5020163714056717 + x3)^2) + x124 * ((
    -0.43417113739871793 + x1)^2 + (-0.12296667128824068 + x2)^2 + (
    -0.9424473212335941 + x3)^2) + x125 * ((-0.18738087377060708 + x4)^2 + (
    -0.9668125465448587 + x5)^2 + (-0.3553159637279516 + x6)^2) + x126 * ((
    -0.8016174920011017 + x4)^2 + (-0.26778829228978485 + x5)^2 + (
    -0.4359301947251404 + x6)^2) + x127 * ((-0.8607174064209905 + x4)^2 + (
    -0.9118236037302004 + x5)^2 + (-0.8874753085224066 + x6)^2) + x128 * ((
    -0.4306937407201691 + x4)^2 + (-0.17428784944790254 + x5)^2 + (
    -0.561800026051346 + x6)^2) + x129 * ((-0.08746124891679041 + x4)^2 + (
    -0.054985697990341253 + x5)^2 + (-0.24949780749022454 + x6)^2) + x130 * ((
    -0.62658802169963 + x4)^2 + (-0.6857573511475539 + x5)^2 + (
    -0.47366426896437996 + x6)^2) + x131 * ((-0.6114768638799523 + x4)^2 + (
    -0.41752031846706683 + x5)^2 + (-0.9109986593014991 + x6)^2) + x132 * ((
    -0.46817035806173857 + x4)^2 + (-0.5569854753991196 + x5)^2 + (
    -0.25003006243034176 + x6)^2) + x133 * ((-0.401092643486621 + x4)^2 + (
    -0.7625123366098691 + x5)^2 + (-0.5084739888197645 + x6)^2) + x134 * ((
    -0.2748596346062746 + x4)^2 + (-0.1892957165775404 + x5)^2 + (
    -0.9442182422598734 + x6)^2) + x135 * ((-0.44167309428028 + x4)^2 + (
    -0.33521919326002436 + x5)^2 + (-0.5030312028077185 + x6)^2) + x136 * ((
    -0.7052213106378172 + x4)^2 + (-0.48063756935051416 + x5)^2 + (
    -0.26073089985191056 + x6)^2) + x137 * ((-0.34955478256076744 + x4)^2 + (
    -0.08326067710845486 + x5)^2 + (-0.5749118628581387 + x6)^2) + x138 * ((
    -0.559986490193569 + x4)^2 + (-0.8433283983822369 + x5)^2 + (
    -0.2573012139171522 + x6)^2) + x139 * ((-0.15759317998774103 + x4)^2 + (
    -0.876898613808363 + x5)^2 + (-0.7812095651757611 + x6)^2) + x140 * ((
    -0.20930481325083095 + x4)^2 + (-0.5243112169526106 + x5)^2 + (
    -0.11364820868480618 + x6)^2) + x141 * ((-0.6971614684173857 + x4)^2 + (
    -0.48152793919664516 + x5)^2 + (-0.10432894263476011 + x6)^2) + x142 * ((
    -0.9788390123597811 + x4)^2 + (-0.6759032973315947 + x5)^2 + (
    -0.9815212516574683 + x6)^2) + x143 * ((-0.31006923192398295 + x4)^2 + (
    -0.9279588991073839 + x5)^2 + (-0.6170791410768803 + x6)^2) + x144 * ((
    -0.2636621784047203 + x4)^2 + (-0.5756031327528047 + x5)^2 + (
    -0.6339965151056094 + x6)^2) + x145 * ((-0.07735274294755135 + x4)^2 + (
    -0.7932728374366258 + x5)^2 + (-0.3905222095735743 + x6)^2) + x146 * ((
    -0.9596478643023862 + x4)^2 + (-0.8323332845748266 + x5)^2 + (
    -0.9490817947377156 + x6)^2) + x147 * ((-0.691877291867759 + x4)^2 + (
    -0.27901589567669627 + x5)^2 + (-0.9603405866805156 + x6)^2) + x148 * ((
    -0.3248230089198071 + x4)^2 + (-0.704031342612858 + x5)^2 + (
    -0.6022746223457217 + x6)^2) + x149 * ((-0.7925246012498328 + x4)^2 + (
    -0.5142003887500619 + x5)^2 + (-0.07412078079700912 + x6)^2) + x150 * ((
    -0.4636597419285817 + x4)^2 + (-0.28493324045279156 + x5)^2 + (
    -0.8982018087470489 + x6)^2) + x151 * ((-0.3125245397681232 + x4)^2 + (
    -0.25776762798299757 + x5)^2 + (-0.05720177574934948 + x6)^2) + x152 * ((
    -0.3197520940611892 + x4)^2 + (-0.8476152339851849 + x5)^2 + (
    -0.36763530621177176 + x6)^2) + x153 * ((-0.7452568897412712 + x4)^2 + (
    -0.24553180487125725 + x5)^2 + (-0.5097535241044541 + x6)^2) + x154 * ((
    -0.7098335381446684 + x4)^2 + (-0.8340974705497336 + x5)^2 + (
    -0.181763781584372 + x6)^2) + x155 * ((-0.46361936352247957 + x4)^2 + (
    -0.5052840929896205 + x5)^2 + (-0.44590180298842885 + x6)^2) + x156 * ((
    -0.38556721731694843 + x4)^2 + (-0.8579051939296445 + x5)^2 + (
    -0.9532247922542321 + x6)^2) + x157 * ((-0.08582521461459391 + x4)^2 + (
    -0.1846731910506113 + x5)^2 + (-0.8745914265553065 + x6)^2) + x158 * ((
    -0.8832914121602843 + x4)^2 + (-0.6513632907999211 + x5)^2 + (
    -0.21823458079012226 + x6)^2) + x159 * ((-0.5751096041706857 + x4)^2 + (
    -0.67547809352205 + x5)^2 + (-0.02460221547003949 + x6)^2) + x160 * ((
    -0.31457012214576896 + x4)^2 + (-0.6742238394444281 + x5)^2 + (
    -0.5445193883971214 + x6)^2) + x161 * ((-0.11915949121286373 + x4)^2 + (
    -0.7063249001765594 + x5)^2 + (-0.2705862773526916 + x6)^2) + x162 * ((
    -0.6669226676581618 + x4)^2 + (-0.5285881831609426 + x5)^2 + (
    -0.11309761756326353 + x6)^2) + x163 * ((-0.12347539452476952 + x4)^2 + (
    -0.39576104678223545 + x5)^2 + (-0.5346277380867844 + x6)^2) + x164 * ((
    -0.6078285274199232 + x4)^2 + (-0.14297039718498794 + x5)^2 + (
    -0.9770203015468777 + x6)^2) + x165 * ((-0.3646785363094529 + x4)^2 + (
    -0.7442303679522239 + x5)^2 + (-0.6078205952200681 + x6)^2) + x166 * ((
    -0.5210217205095699 + x4)^2 + (-0.8432559359514145 + x5)^2 + (
    -0.22452982644506148 + x6)^2) + x167 * ((-0.08751493934711652 + x4)^2 + (
    -0.4416120245181858 + x5)^2 + (-0.026527914551422116 + x6)^2) + x168 * ((
    -0.01197633335476489 + x4)^2 + (-0.2890291018825958 + x5)^2 + (
    -0.38681268974270067 + x6)^2) + x169 * ((-0.7095057303156089 + x4)^2 + (
    -0.931861745530449 + x5)^2 + (-0.14043671018799309 + x6)^2) + x170 * ((
    -0.0895696243176286 + x4)^2 + (-0.5380623897726036 + x5)^2 + (
    -0.21800740949887965 + x6)^2) + x171 * ((-0.7815676711928884 + x4)^2 + (
    -0.018922864242984283 + x5)^2 + (-0.28596537520912735 + x6)^2) + x172 * ((
    -0.1740875221968632 + x4)^2 + (-0.5678042483964806 + x5)^2 + (
    -0.5661715765543827 + x6)^2) + x173 * ((-0.026589535186742008 + x4)^2 + (
    -0.764188329062881 + x5)^2 + (-0.573675168853155 + x6)^2) + x174 * ((
    -0.369798170078249 + x4)^2 + (-0.9415339432121399 + x5)^2 + (
    -0.6729904295003972 + x6)^2) + x175 * ((-0.8040803150564447 + x4)^2 + (
    -0.1553864280131183 + x5)^2 + (-0.8148818001526622 + x6)^2) + x176 * ((
    -0.26589528353030667 + x4)^2 + (-0.3666027540410405 + x5)^2 + (
    -0.468491747882274 + x6)^2) + x177 * ((-0.7258236750794794 + x4)^2 + (
    -0.6727872398248785 + x5)^2 + (-0.28367538142810256 + x6)^2) + x178 * ((
    -0.9220733933477209 + x4)^2 + (-0.26257553387761134 + x5)^2 + (
    -0.7191645521015703 + x6)^2) + x179 * ((-0.9500341346045207 + x4)^2 + (
    -0.638006708190589 + x5)^2 + (-0.07543033185744508 + x6)^2) + x180 * ((
    -0.10545996998960727 + x4)^2 + (-0.7011113856167448 + x5)^2 + (
    -0.20681983539603999 + x6)^2) + x181 * ((-0.6551186918756842 + x4)^2 + (
    -0.6398068804459004 + x5)^2 + (-0.9931175421141764 + x6)^2) + x182 * ((
    -0.7142120519447257 + x4)^2 + (-0.46243457004259436 + x5)^2 + (
    -0.5481708822495015 + x6)^2) + x183 * ((-0.4950904200820069 + x4)^2 + (
    -0.897797250865998 + x5)^2 + (-0.2346789175833377 + x6)^2) + x184 * ((
    -0.6440952365033279 + x4)^2 + (-0.33381998176403327 + x5)^2 + (
    -0.5869170180027279 + x6)^2) + x185 * ((-0.8591109395866232 + x4)^2 + (
    -0.8400580742862248 + x5)^2 + (-0.7678032609886081 + x6)^2) + x186 * ((
    -0.7791674853861603 + x4)^2 + (-0.45754256977454044 + x5)^2 + (
    -0.30909012057666696 + x6)^2) + x187 * ((-0.8968075661486302 + x4)^2 + (
    -0.34892321725590947 + x5)^2 + (-0.05826567448243425 + x6)^2) + x188 * ((
    -0.3189815847959586 + x4)^2 + (-0.3926628302556219 + x5)^2 + (
    -0.07205292941157881 + x6)^2) + x189 * ((-0.8146221960807916 + x4)^2 + (
    -0.4969763360408802 + x5)^2 + (-0.3647398823672149 + x6)^2) + x190 * ((
    -0.23899160200316316 + x4)^2 + (-0.39386695871622013 + x5)^2 + (
    -0.6832280563167916 + x6)^2) + x191 * ((-0.3505164112410739 + x4)^2 + (
    -0.474289602074489 + x5)^2 + (-0.09409181759710883 + x6)^2) + x192 * ((
    -0.9669824450132469 + x4)^2 + (-0.7209255968341481 + x5)^2 + (
    -0.013074465617943565 + x6)^2) + x193 * ((-0.7769547473829561 + x4)^2 + (
    -0.8065173816239941 + x5)^2 + (-0.7160376893035372 + x6)^2) + x194 * ((
    -0.3489895458178166 + x4)^2 + (-0.35733085724791824 + x5)^2 + (
    -0.8864875891533408 + x6)^2) + x195 * ((-0.0664995679925865 + x4)^2 + (
    -0.7243483038068983 + x5)^2 + (-0.9303195285204333 + x6)^2) + x196 * ((
    -0.8115323501210528 + x4)^2 + (-0.42672295637197755 + x5)^2 + (
    -0.04261529652953755 + x6)^2) + x197 * ((-0.3704618379844066 + x4)^2 + (
    -0.1443368240568217 + x5)^2 + (-0.3776192402141899 + x6)^2) + x198 * ((
    -0.7280090144638749 + x4)^2 + (-0.15636110839409045 + x5)^2 + (
    -0.46978018596620896 + x6)^2) + x199 * ((-0.11088006780742277 + x4)^2 + (
    -0.34039206766760943 + x5)^2 + (-0.06827700620696797 + x6)^2) + x200 * ((
    -0.6997602128647453 + x4)^2 + (-0.43764462531136417 + x5)^2 + (
    -0.21027262835312888 + x6)^2) + x201 * ((-0.04425963668315558 + x4)^2 + (
    -0.05866963958501248 + x5)^2 + (-0.3542816901635206 + x6)^2) + x202 * ((
    -0.9757731519147661 + x4)^2 + (-0.3254673022536907 + x5)^2 + (
    -0.6814338527690927 + x6)^2) + x203 * ((-0.7472668303106704 + x4)^2 + (
    -0.0007097732419126812 + x5)^2 + (-0.9280520527234516 + x6)^2) + x204 * ((
    -0.5322530736526498 + x4)^2 + (-0.39754547356694514 + x5)^2 + (
    -0.13635594663989958 + x6)^2) + x205 * ((-0.0007978441992585461 + x4)^2 + (
    -0.8844692811473446 + x5)^2 + (-0.1467696053297397 + x6)^2) + x206 * ((
    -0.482850676866177 + x4)^2 + (-0.10574453600064249 + x5)^2 + (
    -0.8791132223988765 + x6)^2) + x207 * ((-0.7291125910415815 + x4)^2 + (
    -0.2090180996227905 + x5)^2 + (-0.5040401706411071 + x6)^2) + x208 * ((
    -0.6406085128291104 + x4)^2 + (-0.11496605173886654 + x5)^2 + (
    -0.7597217863145667 + x6)^2) + x209 * ((-0.6527145527530681 + x4)^2 + (
    -0.09871984518132071 + x5)^2 + (-0.08020459573270278 + x6)^2) + x210 * ((
    -0.5779788427476141 + x4)^2 + (-0.6106348650543917 + x5)^2 + (
    -0.21791347819398965 + x6)^2) + x211 * ((-0.894563747191656 + x4)^2 + (
    -0.49991063769677824 + x5)^2 + (-0.8312284742613548 + x6)^2) + x212 * ((
    -0.5477983688744066 + x4)^2 + (-0.10123589526888899 + x5)^2 + (
    -0.9724165689826183 + x6)^2) + x213 * ((-0.7051711697372745 + x4)^2 + (
    -0.6974870695940615 + x5)^2 + (-0.34185115432121194 + x6)^2) + x214 * ((
    -0.965288766829392 + x4)^2 + (-0.3541459265683641 + x5)^2 + (
    -0.5256833284803955 + x6)^2) + x215 * ((-0.486217312364274 + x4)^2 + (
    -0.877880388733161 + x5)^2 + (-0.7007637309302288 + x6)^2) + x216 * ((
    -0.9239018568218517 + x4)^2 + (-0.8696579903239924 + x5)^2 + (
    -0.9905428630635226 + x6)^2) + x217 * ((-0.5635239214739318 + x4)^2 + (
    -0.5212076565782671 + x5)^2 + (-0.672320998946101 + x6)^2) + x218 * ((
    -0.6336849702734496 + x4)^2 + (-0.17934198400132562 + x5)^2 + (
    -0.25720032541892046 + x6)^2) + x219 * ((-0.3593028476464476 + x4)^2 + (
    -0.7339808423425379 + x5)^2 + (-0.001964432484070411 + x6)^2) + x220 * ((
    -0.11194390371791885 + x4)^2 + (-0.05379441414468389 + x5)^2 + (
    -0.943183016792168 + x6)^2) + x221 * ((-0.23043169327406487 + x4)^2 + (
    -0.9554781274626842 + x5)^2 + (-0.7782415771343315 + x6)^2) + x222 * ((
    -0.999963313244285 + x4)^2 + (-0.18638094695235063 + x5)^2 + (
    -0.8044007834975228 + x6)^2) + x223 * ((-0.8484168552839887 + x4)^2 + (
    -0.5800377498791588 + x5)^2 + (-0.5020163714056717 + x6)^2) + x224 * ((
    -0.43417113739871793 + x4)^2 + (-0.12296667128824068 + x5)^2 + (
    -0.9424473212335941 + x6)^2) + x225 * ((-0.18738087377060708 + x7)^2 + (
    -0.9668125465448587 + x8)^2 + (-0.3553159637279516 + x9)^2) + x226 * ((
    -0.8016174920011017 + x7)^2 + (-0.26778829228978485 + x8)^2 + (
    -0.4359301947251404 + x9)^2) + x227 * ((-0.8607174064209905 + x7)^2 + (
    -0.9118236037302004 + x8)^2 + (-0.8874753085224066 + x9)^2) + x228 * ((
    -0.4306937407201691 + x7)^2 + (-0.17428784944790254 + x8)^2 + (
    -0.561800026051346 + x9)^2) + x229 * ((-0.08746124891679041 + x7)^2 + (
    -0.054985697990341253 + x8)^2 + (-0.24949780749022454 + x9)^2) + x230 * ((
    -0.62658802169963 + x7)^2 + (-0.6857573511475539 + x8)^2 + (
    -0.47366426896437996 + x9)^2) + x231 * ((-0.6114768638799523 + x7)^2 + (
    -0.41752031846706683 + x8)^2 + (-0.9109986593014991 + x9)^2) + x232 * ((
    -0.46817035806173857 + x7)^2 + (-0.5569854753991196 + x8)^2 + (
    -0.25003006243034176 + x9)^2) + x233 * ((-0.401092643486621 + x7)^2 + (
    -0.7625123366098691 + x8)^2 + (-0.5084739888197645 + x9)^2) + x234 * ((
    -0.2748596346062746 + x7)^2 + (-0.1892957165775404 + x8)^2 + (
    -0.9442182422598734 + x9)^2) + x235 * ((-0.44167309428028 + x7)^2 + (
    -0.33521919326002436 + x8)^2 + (-0.5030312028077185 + x9)^2) + x236 * ((
    -0.7052213106378172 + x7)^2 + (-0.48063756935051416 + x8)^2 + (
    -0.26073089985191056 + x9)^2) + x237 * ((-0.34955478256076744 + x7)^2 + (
    -0.08326067710845486 + x8)^2 + (-0.5749118628581387 + x9)^2) + x238 * ((
    -0.559986490193569 + x7)^2 + (-0.8433283983822369 + x8)^2 + (
    -0.2573012139171522 + x9)^2) + x239 * ((-0.15759317998774103 + x7)^2 + (
    -0.876898613808363 + x8)^2 + (-0.7812095651757611 + x9)^2) + x240 * ((
    -0.20930481325083095 + x7)^2 + (-0.5243112169526106 + x8)^2 + (
    -0.11364820868480618 + x9)^2) + x241 * ((-0.6971614684173857 + x7)^2 + (
    -0.48152793919664516 + x8)^2 + (-0.10432894263476011 + x9)^2) + x242 * ((
    -0.9788390123597811 + x7)^2 + (-0.6759032973315947 + x8)^2 + (
    -0.9815212516574683 + x9)^2) + x243 * ((-0.31006923192398295 + x7)^2 + (
    -0.9279588991073839 + x8)^2 + (-0.6170791410768803 + x9)^2) + x244 * ((
    -0.2636621784047203 + x7)^2 + (-0.5756031327528047 + x8)^2 + (
    -0.6339965151056094 + x9)^2) + x245 * ((-0.07735274294755135 + x7)^2 + (
    -0.7932728374366258 + x8)^2 + (-0.3905222095735743 + x9)^2) + x246 * ((
    -0.9596478643023862 + x7)^2 + (-0.8323332845748266 + x8)^2 + (
    -0.9490817947377156 + x9)^2) + x247 * ((-0.691877291867759 + x7)^2 + (
    -0.27901589567669627 + x8)^2 + (-0.9603405866805156 + x9)^2) + x248 * ((
    -0.3248230089198071 + x7)^2 + (-0.704031342612858 + x8)^2 + (
    -0.6022746223457217 + x9)^2) + x249 * ((-0.7925246012498328 + x7)^2 + (
    -0.5142003887500619 + x8)^2 + (-0.07412078079700912 + x9)^2) + x250 * ((
    -0.4636597419285817 + x7)^2 + (-0.28493324045279156 + x8)^2 + (
    -0.8982018087470489 + x9)^2) + x251 * ((-0.3125245397681232 + x7)^2 + (
    -0.25776762798299757 + x8)^2 + (-0.05720177574934948 + x9)^2) + x252 * ((
    -0.3197520940611892 + x7)^2 + (-0.8476152339851849 + x8)^2 + (
    -0.36763530621177176 + x9)^2) + x253 * ((-0.7452568897412712 + x7)^2 + (
    -0.24553180487125725 + x8)^2 + (-0.5097535241044541 + x9)^2) + x254 * ((
    -0.7098335381446684 + x7)^2 + (-0.8340974705497336 + x8)^2 + (
    -0.181763781584372 + x9)^2) + x255 * ((-0.46361936352247957 + x7)^2 + (
    -0.5052840929896205 + x8)^2 + (-0.44590180298842885 + x9)^2) + x256 * ((
    -0.38556721731694843 + x7)^2 + (-0.8579051939296445 + x8)^2 + (
    -0.9532247922542321 + x9)^2) + x257 * ((-0.08582521461459391 + x7)^2 + (
    -0.1846731910506113 + x8)^2 + (-0.8745914265553065 + x9)^2) + x258 * ((
    -0.8832914121602843 + x7)^2 + (-0.6513632907999211 + x8)^2 + (
    -0.21823458079012226 + x9)^2) + x259 * ((-0.5751096041706857 + x7)^2 + (
    -0.67547809352205 + x8)^2 + (-0.02460221547003949 + x9)^2) + x260 * ((
    -0.31457012214576896 + x7)^2 + (-0.6742238394444281 + x8)^2 + (
    -0.5445193883971214 + x9)^2) + x261 * ((-0.11915949121286373 + x7)^2 + (
    -0.7063249001765594 + x8)^2 + (-0.2705862773526916 + x9)^2) + x262 * ((
    -0.6669226676581618 + x7)^2 + (-0.5285881831609426 + x8)^2 + (
    -0.11309761756326353 + x9)^2) + x263 * ((-0.12347539452476952 + x7)^2 + (
    -0.39576104678223545 + x8)^2 + (-0.5346277380867844 + x9)^2) + x264 * ((
    -0.6078285274199232 + x7)^2 + (-0.14297039718498794 + x8)^2 + (
    -0.9770203015468777 + x9)^2) + x265 * ((-0.3646785363094529 + x7)^2 + (
    -0.7442303679522239 + x8)^2 + (-0.6078205952200681 + x9)^2) + x266 * ((
    -0.5210217205095699 + x7)^2 + (-0.8432559359514145 + x8)^2 + (
    -0.22452982644506148 + x9)^2) + x267 * ((-0.08751493934711652 + x7)^2 + (
    -0.4416120245181858 + x8)^2 + (-0.026527914551422116 + x9)^2) + x268 * ((
    -0.01197633335476489 + x7)^2 + (-0.2890291018825958 + x8)^2 + (
    -0.38681268974270067 + x9)^2) + x269 * ((-0.7095057303156089 + x7)^2 + (
    -0.931861745530449 + x8)^2 + (-0.14043671018799309 + x9)^2) + x270 * ((
    -0.0895696243176286 + x7)^2 + (-0.5380623897726036 + x8)^2 + (
    -0.21800740949887965 + x9)^2) + x271 * ((-0.7815676711928884 + x7)^2 + (
    -0.018922864242984283 + x8)^2 + (-0.28596537520912735 + x9)^2) + x272 * ((
    -0.1740875221968632 + x7)^2 + (-0.5678042483964806 + x8)^2 + (
    -0.5661715765543827 + x9)^2) + x273 * ((-0.026589535186742008 + x7)^2 + (
    -0.764188329062881 + x8)^2 + (-0.573675168853155 + x9)^2) + x274 * ((
    -0.369798170078249 + x7)^2 + (-0.9415339432121399 + x8)^2 + (
    -0.6729904295003972 + x9)^2) + x275 * ((-0.8040803150564447 + x7)^2 + (
    -0.1553864280131183 + x8)^2 + (-0.8148818001526622 + x9)^2) + x276 * ((
    -0.26589528353030667 + x7)^2 + (-0.3666027540410405 + x8)^2 + (
    -0.468491747882274 + x9)^2) + x277 * ((-0.7258236750794794 + x7)^2 + (
    -0.6727872398248785 + x8)^2 + (-0.28367538142810256 + x9)^2) + x278 * ((
    -0.9220733933477209 + x7)^2 + (-0.26257553387761134 + x8)^2 + (
    -0.7191645521015703 + x9)^2) + x279 * ((-0.9500341346045207 + x7)^2 + (
    -0.638006708190589 + x8)^2 + (-0.07543033185744508 + x9)^2) + x280 * ((
    -0.10545996998960727 + x7)^2 + (-0.7011113856167448 + x8)^2 + (
    -0.20681983539603999 + x9)^2) + x281 * ((-0.6551186918756842 + x7)^2 + (
    -0.6398068804459004 + x8)^2 + (-0.9931175421141764 + x9)^2) + x282 * ((
    -0.7142120519447257 + x7)^2 + (-0.46243457004259436 + x8)^2 + (
    -0.5481708822495015 + x9)^2) + x283 * ((-0.4950904200820069 + x7)^2 + (
    -0.897797250865998 + x8)^2 + (-0.2346789175833377 + x9)^2) + x284 * ((
    -0.6440952365033279 + x7)^2 + (-0.33381998176403327 + x8)^2 + (
    -0.5869170180027279 + x9)^2) + x285 * ((-0.8591109395866232 + x7)^2 + (
    -0.8400580742862248 + x8)^2 + (-0.7678032609886081 + x9)^2) + x286 * ((
    -0.7791674853861603 + x7)^2 + (-0.45754256977454044 + x8)^2 + (
    -0.30909012057666696 + x9)^2) + x287 * ((-0.8968075661486302 + x7)^2 + (
    -0.34892321725590947 + x8)^2 + (-0.05826567448243425 + x9)^2) + x288 * ((
    -0.3189815847959586 + x7)^2 + (-0.3926628302556219 + x8)^2 + (
    -0.07205292941157881 + x9)^2) + x289 * ((-0.8146221960807916 + x7)^2 + (
    -0.4969763360408802 + x8)^2 + (-0.3647398823672149 + x9)^2) + x290 * ((
    -0.23899160200316316 + x7)^2 + (-0.39386695871622013 + x8)^2 + (
    -0.6832280563167916 + x9)^2) + x291 * ((-0.3505164112410739 + x7)^2 + (
    -0.474289602074489 + x8)^2 + (-0.09409181759710883 + x9)^2) + x292 * ((
    -0.9669824450132469 + x7)^2 + (-0.7209255968341481 + x8)^2 + (
    -0.013074465617943565 + x9)^2) + x293 * ((-0.7769547473829561 + x7)^2 + (
    -0.8065173816239941 + x8)^2 + (-0.7160376893035372 + x9)^2) + x294 * ((
    -0.3489895458178166 + x7)^2 + (-0.35733085724791824 + x8)^2 + (
    -0.8864875891533408 + x9)^2) + x295 * ((-0.0664995679925865 + x7)^2 + (
    -0.7243483038068983 + x8)^2 + (-0.9303195285204333 + x9)^2) + x296 * ((
    -0.8115323501210528 + x7)^2 + (-0.42672295637197755 + x8)^2 + (
    -0.04261529652953755 + x9)^2) + x297 * ((-0.3704618379844066 + x7)^2 + (
    -0.1443368240568217 + x8)^2 + (-0.3776192402141899 + x9)^2) + x298 * ((
    -0.7280090144638749 + x7)^2 + (-0.15636110839409045 + x8)^2 + (
    -0.46978018596620896 + x9)^2) + x299 * ((-0.11088006780742277 + x7)^2 + (
    -0.34039206766760943 + x8)^2 + (-0.06827700620696797 + x9)^2) + x300 * ((
    -0.6997602128647453 + x7)^2 + (-0.43764462531136417 + x8)^2 + (
    -0.21027262835312888 + x9)^2) + x301 * ((-0.04425963668315558 + x7)^2 + (
    -0.05866963958501248 + x8)^2 + (-0.3542816901635206 + x9)^2) + x302 * ((
    -0.9757731519147661 + x7)^2 + (-0.3254673022536907 + x8)^2 + (
    -0.6814338527690927 + x9)^2) + x303 * ((-0.7472668303106704 + x7)^2 + (
    -0.0007097732419126812 + x8)^2 + (-0.9280520527234516 + x9)^2) + x304 * ((
    -0.5322530736526498 + x7)^2 + (-0.39754547356694514 + x8)^2 + (
    -0.13635594663989958 + x9)^2) + x305 * ((-0.0007978441992585461 + x7)^2 + (
    -0.8844692811473446 + x8)^2 + (-0.1467696053297397 + x9)^2) + x306 * ((
    -0.482850676866177 + x7)^2 + (-0.10574453600064249 + x8)^2 + (
    -0.8791132223988765 + x9)^2) + x307 * ((-0.7291125910415815 + x7)^2 + (
    -0.2090180996227905 + x8)^2 + (-0.5040401706411071 + x9)^2) + x308 * ((
    -0.6406085128291104 + x7)^2 + (-0.11496605173886654 + x8)^2 + (
    -0.7597217863145667 + x9)^2) + x309 * ((-0.6527145527530681 + x7)^2 + (
    -0.09871984518132071 + x8)^2 + (-0.08020459573270278 + x9)^2) + x310 * ((
    -0.5779788427476141 + x7)^2 + (-0.6106348650543917 + x8)^2 + (
    -0.21791347819398965 + x9)^2) + x311 * ((-0.894563747191656 + x7)^2 + (
    -0.49991063769677824 + x8)^2 + (-0.8312284742613548 + x9)^2) + x312 * ((
    -0.5477983688744066 + x7)^2 + (-0.10123589526888899 + x8)^2 + (
    -0.9724165689826183 + x9)^2) + x313 * ((-0.7051711697372745 + x7)^2 + (
    -0.6974870695940615 + x8)^2 + (-0.34185115432121194 + x9)^2) + x314 * ((
    -0.965288766829392 + x7)^2 + (-0.3541459265683641 + x8)^2 + (
    -0.5256833284803955 + x9)^2) + x315 * ((-0.486217312364274 + x7)^2 + (
    -0.877880388733161 + x8)^2 + (-0.7007637309302288 + x9)^2) + x316 * ((
    -0.9239018568218517 + x7)^2 + (-0.8696579903239924 + x8)^2 + (
    -0.9905428630635226 + x9)^2) + x317 * ((-0.5635239214739318 + x7)^2 + (
    -0.5212076565782671 + x8)^2 + (-0.672320998946101 + x9)^2) + x318 * ((
    -0.6336849702734496 + x7)^2 + (-0.17934198400132562 + x8)^2 + (
    -0.25720032541892046 + x9)^2) + x319 * ((-0.3593028476464476 + x7)^2 + (
    -0.7339808423425379 + x8)^2 + (-0.001964432484070411 + x9)^2) + x320 * ((
    -0.11194390371791885 + x7)^2 + (-0.05379441414468389 + x8)^2 + (
    -0.943183016792168 + x9)^2) + x321 * ((-0.23043169327406487 + x7)^2 + (
    -0.9554781274626842 + x8)^2 + (-0.7782415771343315 + x9)^2) + x322 * ((
    -0.999963313244285 + x7)^2 + (-0.18638094695235063 + x8)^2 + (
    -0.8044007834975228 + x9)^2) + x323 * ((-0.8484168552839887 + x7)^2 + (
    -0.5800377498791588 + x8)^2 + (-0.5020163714056717 + x9)^2) + x324 * ((
    -0.43417113739871793 + x7)^2 + (-0.12296667128824068 + x8)^2 + (
    -0.9424473212335941 + x9)^2) + x325 * ((-0.18738087377060708 + x10)^2 + (
    -0.9668125465448587 + x11)^2 + (-0.3553159637279516 + x12)^2) + x326 * ((
    -0.8016174920011017 + x10)^2 + (-0.26778829228978485 + x11)^2 + (
    -0.4359301947251404 + x12)^2) + x327 * ((-0.8607174064209905 + x10)^2 + (
    -0.9118236037302004 + x11)^2 + (-0.8874753085224066 + x12)^2) + x328 * ((
    -0.4306937407201691 + x10)^2 + (-0.17428784944790254 + x11)^2 + (
    -0.561800026051346 + x12)^2) + x329 * ((-0.08746124891679041 + x10)^2 + (
    -0.054985697990341253 + x11)^2 + (-0.24949780749022454 + x12)^2) + x330 * (
    (-0.62658802169963 + x10)^2 + (-0.6857573511475539 + x11)^2 + (
    -0.47366426896437996 + x12)^2) + x331 * ((-0.6114768638799523 + x10)^2 + (
    -0.41752031846706683 + x11)^2 + (-0.9109986593014991 + x12)^2) + x332 * ((
    -0.46817035806173857 + x10)^2 + (-0.5569854753991196 + x11)^2 + (
    -0.25003006243034176 + x12)^2) + x333 * ((-0.401092643486621 + x10)^2 + (
    -0.7625123366098691 + x11)^2 + (-0.5084739888197645 + x12)^2) + x334 * ((
    -0.2748596346062746 + x10)^2 + (-0.1892957165775404 + x11)^2 + (
    -0.9442182422598734 + x12)^2) + x335 * ((-0.44167309428028 + x10)^2 + (
    -0.33521919326002436 + x11)^2 + (-0.5030312028077185 + x12)^2) + x336 * ((
    -0.7052213106378172 + x10)^2 + (-0.48063756935051416 + x11)^2 + (
    -0.26073089985191056 + x12)^2) + x337 * ((-0.34955478256076744 + x10)^2 + (
    -0.08326067710845486 + x11)^2 + (-0.5749118628581387 + x12)^2) + x338 * ((
    -0.559986490193569 + x10)^2 + (-0.8433283983822369 + x11)^2 + (
    -0.2573012139171522 + x12)^2) + x339 * ((-0.15759317998774103 + x10)^2 + (
    -0.876898613808363 + x11)^2 + (-0.7812095651757611 + x12)^2) + x340 * ((
    -0.20930481325083095 + x10)^2 + (-0.5243112169526106 + x11)^2 + (
    -0.11364820868480618 + x12)^2) + x341 * ((-0.6971614684173857 + x10)^2 + (
    -0.48152793919664516 + x11)^2 + (-0.10432894263476011 + x12)^2) + x342 * ((
    -0.9788390123597811 + x10)^2 + (-0.6759032973315947 + x11)^2 + (
    -0.9815212516574683 + x12)^2) + x343 * ((-0.31006923192398295 + x10)^2 + (
    -0.9279588991073839 + x11)^2 + (-0.6170791410768803 + x12)^2) + x344 * ((
    -0.2636621784047203 + x10)^2 + (-0.5756031327528047 + x11)^2 + (
    -0.6339965151056094 + x12)^2) + x345 * ((-0.07735274294755135 + x10)^2 + (
    -0.7932728374366258 + x11)^2 + (-0.3905222095735743 + x12)^2) + x346 * ((
    -0.9596478643023862 + x10)^2 + (-0.8323332845748266 + x11)^2 + (
    -0.9490817947377156 + x12)^2) + x347 * ((-0.691877291867759 + x10)^2 + (
    -0.27901589567669627 + x11)^2 + (-0.9603405866805156 + x12)^2) + x348 * ((
    -0.3248230089198071 + x10)^2 + (-0.704031342612858 + x11)^2 + (
    -0.6022746223457217 + x12)^2) + x349 * ((-0.7925246012498328 + x10)^2 + (
    -0.5142003887500619 + x11)^2 + (-0.07412078079700912 + x12)^2) + x350 * ((
    -0.4636597419285817 + x10)^2 + (-0.28493324045279156 + x11)^2 + (
    -0.8982018087470489 + x12)^2) + x351 * ((-0.3125245397681232 + x10)^2 + (
    -0.25776762798299757 + x11)^2 + (-0.05720177574934948 + x12)^2) + x352 * ((
    -0.3197520940611892 + x10)^2 + (-0.8476152339851849 + x11)^2 + (
    -0.36763530621177176 + x12)^2) + x353 * ((-0.7452568897412712 + x10)^2 + (
    -0.24553180487125725 + x11)^2 + (-0.5097535241044541 + x12)^2) + x354 * ((
    -0.7098335381446684 + x10)^2 + (-0.8340974705497336 + x11)^2 + (
    -0.181763781584372 + x12)^2) + x355 * ((-0.46361936352247957 + x10)^2 + (
    -0.5052840929896205 + x11)^2 + (-0.44590180298842885 + x12)^2) + x356 * ((
    -0.38556721731694843 + x10)^2 + (-0.8579051939296445 + x11)^2 + (
    -0.9532247922542321 + x12)^2) + x357 * ((-0.08582521461459391 + x10)^2 + (
    -0.1846731910506113 + x11)^2 + (-0.8745914265553065 + x12)^2) + x358 * ((
    -0.8832914121602843 + x10)^2 + (-0.6513632907999211 + x11)^2 + (
    -0.21823458079012226 + x12)^2) + x359 * ((-0.5751096041706857 + x10)^2 + (
    -0.67547809352205 + x11)^2 + (-0.02460221547003949 + x12)^2) + x360 * ((
    -0.31457012214576896 + x10)^2 + (-0.6742238394444281 + x11)^2 + (
    -0.5445193883971214 + x12)^2) + x361 * ((-0.11915949121286373 + x10)^2 + (
    -0.7063249001765594 + x11)^2 + (-0.2705862773526916 + x12)^2) + x362 * ((
    -0.6669226676581618 + x10)^2 + (-0.5285881831609426 + x11)^2 + (
    -0.11309761756326353 + x12)^2) + x363 * ((-0.12347539452476952 + x10)^2 + (
    -0.39576104678223545 + x11)^2 + (-0.5346277380867844 + x12)^2) + x364 * ((
    -0.6078285274199232 + x10)^2 + (-0.14297039718498794 + x11)^2 + (
    -0.9770203015468777 + x12)^2) + x365 * ((-0.3646785363094529 + x10)^2 + (
    -0.7442303679522239 + x11)^2 + (-0.6078205952200681 + x12)^2) + x366 * ((
    -0.5210217205095699 + x10)^2 + (-0.8432559359514145 + x11)^2 + (
    -0.22452982644506148 + x12)^2) + x367 * ((-0.08751493934711652 + x10)^2 + (
    -0.4416120245181858 + x11)^2 + (-0.026527914551422116 + x12)^2) + x368 * ((
    -0.01197633335476489 + x10)^2 + (-0.2890291018825958 + x11)^2 + (
    -0.38681268974270067 + x12)^2) + x369 * ((-0.7095057303156089 + x10)^2 + (
    -0.931861745530449 + x11)^2 + (-0.14043671018799309 + x12)^2) + x370 * ((
    -0.0895696243176286 + x10)^2 + (-0.5380623897726036 + x11)^2 + (
    -0.21800740949887965 + x12)^2) + x371 * ((-0.7815676711928884 + x10)^2 + (
    -0.018922864242984283 + x11)^2 + (-0.28596537520912735 + x12)^2) + x372 * (
    (-0.1740875221968632 + x10)^2 + (-0.5678042483964806 + x11)^2 + (
    -0.5661715765543827 + x12)^2) + x373 * ((-0.026589535186742008 + x10)^2 + (
    -0.764188329062881 + x11)^2 + (-0.573675168853155 + x12)^2) + x374 * ((
    -0.369798170078249 + x10)^2 + (-0.9415339432121399 + x11)^2 + (
    -0.6729904295003972 + x12)^2) + x375 * ((-0.8040803150564447 + x10)^2 + (
    -0.1553864280131183 + x11)^2 + (-0.8148818001526622 + x12)^2) + x376 * ((
    -0.26589528353030667 + x10)^2 + (-0.3666027540410405 + x11)^2 + (
    -0.468491747882274 + x12)^2) + x377 * ((-0.7258236750794794 + x10)^2 + (
    -0.6727872398248785 + x11)^2 + (-0.28367538142810256 + x12)^2) + x378 * ((
    -0.9220733933477209 + x10)^2 + (-0.26257553387761134 + x11)^2 + (
    -0.7191645521015703 + x12)^2) + x379 * ((-0.9500341346045207 + x10)^2 + (
    -0.638006708190589 + x11)^2 + (-0.07543033185744508 + x12)^2) + x380 * ((
    -0.10545996998960727 + x10)^2 + (-0.7011113856167448 + x11)^2 + (
    -0.20681983539603999 + x12)^2) + x381 * ((-0.6551186918756842 + x10)^2 + (
    -0.6398068804459004 + x11)^2 + (-0.9931175421141764 + x12)^2) + x382 * ((
    -0.7142120519447257 + x10)^2 + (-0.46243457004259436 + x11)^2 + (
    -0.5481708822495015 + x12)^2) + x383 * ((-0.4950904200820069 + x10)^2 + (
    -0.897797250865998 + x11)^2 + (-0.2346789175833377 + x12)^2) + x384 * ((
    -0.6440952365033279 + x10)^2 + (-0.33381998176403327 + x11)^2 + (
    -0.5869170180027279 + x12)^2) + x385 * ((-0.8591109395866232 + x10)^2 + (
    -0.8400580742862248 + x11)^2 + (-0.7678032609886081 + x12)^2) + x386 * ((
    -0.7791674853861603 + x10)^2 + (-0.45754256977454044 + x11)^2 + (
    -0.30909012057666696 + x12)^2) + x387 * ((-0.8968075661486302 + x10)^2 + (
    -0.34892321725590947 + x11)^2 + (-0.05826567448243425 + x12)^2) + x388 * ((
    -0.3189815847959586 + x10)^2 + (-0.3926628302556219 + x11)^2 + (
    -0.07205292941157881 + x12)^2) + x389 * ((-0.8146221960807916 + x10)^2 + (
    -0.4969763360408802 + x11)^2 + (-0.3647398823672149 + x12)^2) + x390 * ((
    -0.23899160200316316 + x10)^2 + (-0.39386695871622013 + x11)^2 + (
    -0.6832280563167916 + x12)^2) + x391 * ((-0.3505164112410739 + x10)^2 + (
    -0.474289602074489 + x11)^2 + (-0.09409181759710883 + x12)^2) + x392 * ((
    -0.9669824450132469 + x10)^2 + (-0.7209255968341481 + x11)^2 + (
    -0.013074465617943565 + x12)^2) + x393 * ((-0.7769547473829561 + x10)^2 + (
    -0.8065173816239941 + x11)^2 + (-0.7160376893035372 + x12)^2) + x394 * ((
    -0.3489895458178166 + x10)^2 + (-0.35733085724791824 + x11)^2 + (
    -0.8864875891533408 + x12)^2) + x395 * ((-0.0664995679925865 + x10)^2 + (
    -0.7243483038068983 + x11)^2 + (-0.9303195285204333 + x12)^2) + x396 * ((
    -0.8115323501210528 + x10)^2 + (-0.42672295637197755 + x11)^2 + (
    -0.04261529652953755 + x12)^2) + x397 * ((-0.3704618379844066 + x10)^2 + (
    -0.1443368240568217 + x11)^2 + (-0.3776192402141899 + x12)^2) + x398 * ((
    -0.7280090144638749 + x10)^2 + (-0.15636110839409045 + x11)^2 + (
    -0.46978018596620896 + x12)^2) + x399 * ((-0.11088006780742277 + x10)^2 + (
    -0.34039206766760943 + x11)^2 + (-0.06827700620696797 + x12)^2) + x400 * ((
    -0.6997602128647453 + x10)^2 + (-0.43764462531136417 + x11)^2 + (
    -0.21027262835312888 + x12)^2) + x401 * ((-0.04425963668315558 + x10)^2 + (
    -0.05866963958501248 + x11)^2 + (-0.3542816901635206 + x12)^2) + x402 * ((
    -0.9757731519147661 + x10)^2 + (-0.3254673022536907 + x11)^2 + (
    -0.6814338527690927 + x12)^2) + x403 * ((-0.7472668303106704 + x10)^2 + (
    -0.0007097732419126812 + x11)^2 + (-0.9280520527234516 + x12)^2) + x404 * (
    (-0.5322530736526498 + x10)^2 + (-0.39754547356694514 + x11)^2 + (
    -0.13635594663989958 + x12)^2) + x405 * ((-0.0007978441992585461 + x10)^2
    + (-0.8844692811473446 + x11)^2 + (-0.1467696053297397 + x12)^2) + x406 *
    ((-0.482850676866177 + x10)^2 + (-0.10574453600064249 + x11)^2 + (
    -0.8791132223988765 + x12)^2) + x407 * ((-0.7291125910415815 + x10)^2 + (
    -0.2090180996227905 + x11)^2 + (-0.5040401706411071 + x12)^2) + x408 * ((
    -0.6406085128291104 + x10)^2 + (-0.11496605173886654 + x11)^2 + (
    -0.7597217863145667 + x12)^2) + x409 * ((-0.6527145527530681 + x10)^2 + (
    -0.09871984518132071 + x11)^2 + (-0.08020459573270278 + x12)^2) + x410 * ((
    -0.5779788427476141 + x10)^2 + (-0.6106348650543917 + x11)^2 + (
    -0.21791347819398965 + x12)^2) + x411 * ((-0.894563747191656 + x10)^2 + (
    -0.49991063769677824 + x11)^2 + (-0.8312284742613548 + x12)^2) + x412 * ((
    -0.5477983688744066 + x10)^2 + (-0.10123589526888899 + x11)^2 + (
    -0.9724165689826183 + x12)^2) + x413 * ((-0.7051711697372745 + x10)^2 + (
    -0.6974870695940615 + x11)^2 + (-0.34185115432121194 + x12)^2) + x414 * ((
    -0.965288766829392 + x10)^2 + (-0.3541459265683641 + x11)^2 + (
    -0.5256833284803955 + x12)^2) + x415 * ((-0.486217312364274 + x10)^2 + (
    -0.877880388733161 + x11)^2 + (-0.7007637309302288 + x12)^2) + x416 * ((
    -0.9239018568218517 + x10)^2 + (-0.8696579903239924 + x11)^2 + (
    -0.9905428630635226 + x12)^2) + x417 * ((-0.5635239214739318 + x10)^2 + (
    -0.5212076565782671 + x11)^2 + (-0.672320998946101 + x12)^2) + x418 * ((
    -0.6336849702734496 + x10)^2 + (-0.17934198400132562 + x11)^2 + (
    -0.25720032541892046 + x12)^2) + x419 * ((-0.3593028476464476 + x10)^2 + (
    -0.7339808423425379 + x11)^2 + (-0.001964432484070411 + x12)^2) + x420 * ((
    -0.11194390371791885 + x10)^2 + (-0.05379441414468389 + x11)^2 + (
    -0.943183016792168 + x12)^2) + x421 * ((-0.23043169327406487 + x10)^2 + (
    -0.9554781274626842 + x11)^2 + (-0.7782415771343315 + x12)^2) + x422 * ((
    -0.999963313244285 + x10)^2 + (-0.18638094695235063 + x11)^2 + (
    -0.8044007834975228 + x12)^2) + x423 * ((-0.8484168552839887 + x10)^2 + (
    -0.5800377498791588 + x11)^2 + (-0.5020163714056717 + x12)^2) + x424 * ((
    -0.43417113739871793 + x10)^2 + (-0.12296667128824068 + x11)^2 + (
    -0.9424473212335941 + x12)^2) + x425 * ((-0.18738087377060708 + x13)^2 + (
    -0.9668125465448587 + x14)^2 + (-0.3553159637279516 + x15)^2) + x426 * ((
    -0.8016174920011017 + x13)^2 + (-0.26778829228978485 + x14)^2 + (
    -0.4359301947251404 + x15)^2) + x427 * ((-0.8607174064209905 + x13)^2 + (
    -0.9118236037302004 + x14)^2 + (-0.8874753085224066 + x15)^2) + x428 * ((
    -0.4306937407201691 + x13)^2 + (-0.17428784944790254 + x14)^2 + (
    -0.561800026051346 + x15)^2) + x429 * ((-0.08746124891679041 + x13)^2 + (
    -0.054985697990341253 + x14)^2 + (-0.24949780749022454 + x15)^2) + x430 * (
    (-0.62658802169963 + x13)^2 + (-0.6857573511475539 + x14)^2 + (
    -0.47366426896437996 + x15)^2) + x431 * ((-0.6114768638799523 + x13)^2 + (
    -0.41752031846706683 + x14)^2 + (-0.9109986593014991 + x15)^2) + x432 * ((
    -0.46817035806173857 + x13)^2 + (-0.5569854753991196 + x14)^2 + (
    -0.25003006243034176 + x15)^2) + x433 * ((-0.401092643486621 + x13)^2 + (
    -0.7625123366098691 + x14)^2 + (-0.5084739888197645 + x15)^2) + x434 * ((
    -0.2748596346062746 + x13)^2 + (-0.1892957165775404 + x14)^2 + (
    -0.9442182422598734 + x15)^2) + x435 * ((-0.44167309428028 + x13)^2 + (
    -0.33521919326002436 + x14)^2 + (-0.5030312028077185 + x15)^2) + x436 * ((
    -0.7052213106378172 + x13)^2 + (-0.48063756935051416 + x14)^2 + (
    -0.26073089985191056 + x15)^2) + x437 * ((-0.34955478256076744 + x13)^2 + (
    -0.08326067710845486 + x14)^2 + (-0.5749118628581387 + x15)^2) + x438 * ((
    -0.559986490193569 + x13)^2 + (-0.8433283983822369 + x14)^2 + (
    -0.2573012139171522 + x15)^2) + x439 * ((-0.15759317998774103 + x13)^2 + (
    -0.876898613808363 + x14)^2 + (-0.7812095651757611 + x15)^2) + x440 * ((
    -0.20930481325083095 + x13)^2 + (-0.5243112169526106 + x14)^2 + (
    -0.11364820868480618 + x15)^2) + x441 * ((-0.6971614684173857 + x13)^2 + (
    -0.48152793919664516 + x14)^2 + (-0.10432894263476011 + x15)^2) + x442 * ((
    -0.9788390123597811 + x13)^2 + (-0.6759032973315947 + x14)^2 + (
    -0.9815212516574683 + x15)^2) + x443 * ((-0.31006923192398295 + x13)^2 + (
    -0.9279588991073839 + x14)^2 + (-0.6170791410768803 + x15)^2) + x444 * ((
    -0.2636621784047203 + x13)^2 + (-0.5756031327528047 + x14)^2 + (
    -0.6339965151056094 + x15)^2) + x445 * ((-0.07735274294755135 + x13)^2 + (
    -0.7932728374366258 + x14)^2 + (-0.3905222095735743 + x15)^2) + x446 * ((
    -0.9596478643023862 + x13)^2 + (-0.8323332845748266 + x14)^2 + (
    -0.9490817947377156 + x15)^2) + x447 * ((-0.691877291867759 + x13)^2 + (
    -0.27901589567669627 + x14)^2 + (-0.9603405866805156 + x15)^2) + x448 * ((
    -0.3248230089198071 + x13)^2 + (-0.704031342612858 + x14)^2 + (
    -0.6022746223457217 + x15)^2) + x449 * ((-0.7925246012498328 + x13)^2 + (
    -0.5142003887500619 + x14)^2 + (-0.07412078079700912 + x15)^2) + x450 * ((
    -0.4636597419285817 + x13)^2 + (-0.28493324045279156 + x14)^2 + (
    -0.8982018087470489 + x15)^2) + x451 * ((-0.3125245397681232 + x13)^2 + (
    -0.25776762798299757 + x14)^2 + (-0.05720177574934948 + x15)^2) + x452 * ((
    -0.3197520940611892 + x13)^2 + (-0.8476152339851849 + x14)^2 + (
    -0.36763530621177176 + x15)^2) + x453 * ((-0.7452568897412712 + x13)^2 + (
    -0.24553180487125725 + x14)^2 + (-0.5097535241044541 + x15)^2) + x454 * ((
    -0.7098335381446684 + x13)^2 + (-0.8340974705497336 + x14)^2 + (
    -0.181763781584372 + x15)^2) + x455 * ((-0.46361936352247957 + x13)^2 + (
    -0.5052840929896205 + x14)^2 + (-0.44590180298842885 + x15)^2) + x456 * ((
    -0.38556721731694843 + x13)^2 + (-0.8579051939296445 + x14)^2 + (
    -0.9532247922542321 + x15)^2) + x457 * ((-0.08582521461459391 + x13)^2 + (
    -0.1846731910506113 + x14)^2 + (-0.8745914265553065 + x15)^2) + x458 * ((
    -0.8832914121602843 + x13)^2 + (-0.6513632907999211 + x14)^2 + (
    -0.21823458079012226 + x15)^2) + x459 * ((-0.5751096041706857 + x13)^2 + (
    -0.67547809352205 + x14)^2 + (-0.02460221547003949 + x15)^2) + x460 * ((
    -0.31457012214576896 + x13)^2 + (-0.6742238394444281 + x14)^2 + (
    -0.5445193883971214 + x15)^2) + x461 * ((-0.11915949121286373 + x13)^2 + (
    -0.7063249001765594 + x14)^2 + (-0.2705862773526916 + x15)^2) + x462 * ((
    -0.6669226676581618 + x13)^2 + (-0.5285881831609426 + x14)^2 + (
    -0.11309761756326353 + x15)^2) + x463 * ((-0.12347539452476952 + x13)^2 + (
    -0.39576104678223545 + x14)^2 + (-0.5346277380867844 + x15)^2) + x464 * ((
    -0.6078285274199232 + x13)^2 + (-0.14297039718498794 + x14)^2 + (
    -0.9770203015468777 + x15)^2) + x465 * ((-0.3646785363094529 + x13)^2 + (
    -0.7442303679522239 + x14)^2 + (-0.6078205952200681 + x15)^2) + x466 * ((
    -0.5210217205095699 + x13)^2 + (-0.8432559359514145 + x14)^2 + (
    -0.22452982644506148 + x15)^2) + x467 * ((-0.08751493934711652 + x13)^2 + (
    -0.4416120245181858 + x14)^2 + (-0.026527914551422116 + x15)^2) + x468 * ((
    -0.01197633335476489 + x13)^2 + (-0.2890291018825958 + x14)^2 + (
    -0.38681268974270067 + x15)^2) + x469 * ((-0.7095057303156089 + x13)^2 + (
    -0.931861745530449 + x14)^2 + (-0.14043671018799309 + x15)^2) + x470 * ((
    -0.0895696243176286 + x13)^2 + (-0.5380623897726036 + x14)^2 + (
    -0.21800740949887965 + x15)^2) + x471 * ((-0.7815676711928884 + x13)^2 + (
    -0.018922864242984283 + x14)^2 + (-0.28596537520912735 + x15)^2) + x472 * (
    (-0.1740875221968632 + x13)^2 + (-0.5678042483964806 + x14)^2 + (
    -0.5661715765543827 + x15)^2) + x473 * ((-0.026589535186742008 + x13)^2 + (
    -0.764188329062881 + x14)^2 + (-0.573675168853155 + x15)^2) + x474 * ((
    -0.369798170078249 + x13)^2 + (-0.9415339432121399 + x14)^2 + (
    -0.6729904295003972 + x15)^2) + x475 * ((-0.8040803150564447 + x13)^2 + (
    -0.1553864280131183 + x14)^2 + (-0.8148818001526622 + x15)^2) + x476 * ((
    -0.26589528353030667 + x13)^2 + (-0.3666027540410405 + x14)^2 + (
    -0.468491747882274 + x15)^2) + x477 * ((-0.7258236750794794 + x13)^2 + (
    -0.6727872398248785 + x14)^2 + (-0.28367538142810256 + x15)^2) + x478 * ((
    -0.9220733933477209 + x13)^2 + (-0.26257553387761134 + x14)^2 + (
    -0.7191645521015703 + x15)^2) + x479 * ((-0.9500341346045207 + x13)^2 + (
    -0.638006708190589 + x14)^2 + (-0.07543033185744508 + x15)^2) + x480 * ((
    -0.10545996998960727 + x13)^2 + (-0.7011113856167448 + x14)^2 + (
    -0.20681983539603999 + x15)^2) + x481 * ((-0.6551186918756842 + x13)^2 + (
    -0.6398068804459004 + x14)^2 + (-0.9931175421141764 + x15)^2) + x482 * ((
    -0.7142120519447257 + x13)^2 + (-0.46243457004259436 + x14)^2 + (
    -0.5481708822495015 + x15)^2) + x483 * ((-0.4950904200820069 + x13)^2 + (
    -0.897797250865998 + x14)^2 + (-0.2346789175833377 + x15)^2) + x484 * ((
    -0.6440952365033279 + x13)^2 + (-0.33381998176403327 + x14)^2 + (
    -0.5869170180027279 + x15)^2) + x485 * ((-0.8591109395866232 + x13)^2 + (
    -0.8400580742862248 + x14)^2 + (-0.7678032609886081 + x15)^2) + x486 * ((
    -0.7791674853861603 + x13)^2 + (-0.45754256977454044 + x14)^2 + (
    -0.30909012057666696 + x15)^2) + x487 * ((-0.8968075661486302 + x13)^2 + (
    -0.34892321725590947 + x14)^2 + (-0.05826567448243425 + x15)^2) + x488 * ((
    -0.3189815847959586 + x13)^2 + (-0.3926628302556219 + x14)^2 + (
    -0.07205292941157881 + x15)^2) + x489 * ((-0.8146221960807916 + x13)^2 + (
    -0.4969763360408802 + x14)^2 + (-0.3647398823672149 + x15)^2) + x490 * ((
    -0.23899160200316316 + x13)^2 + (-0.39386695871622013 + x14)^2 + (
    -0.6832280563167916 + x15)^2) + x491 * ((-0.3505164112410739 + x13)^2 + (
    -0.474289602074489 + x14)^2 + (-0.09409181759710883 + x15)^2) + x492 * ((
    -0.9669824450132469 + x13)^2 + (-0.7209255968341481 + x14)^2 + (
    -0.013074465617943565 + x15)^2) + x493 * ((-0.7769547473829561 + x13)^2 + (
    -0.8065173816239941 + x14)^2 + (-0.7160376893035372 + x15)^2) + x494 * ((
    -0.3489895458178166 + x13)^2 + (-0.35733085724791824 + x14)^2 + (
    -0.8864875891533408 + x15)^2) + x495 * ((-0.0664995679925865 + x13)^2 + (
    -0.7243483038068983 + x14)^2 + (-0.9303195285204333 + x15)^2) + x496 * ((
    -0.8115323501210528 + x13)^2 + (-0.42672295637197755 + x14)^2 + (
    -0.04261529652953755 + x15)^2) + x497 * ((-0.3704618379844066 + x13)^2 + (
    -0.1443368240568217 + x14)^2 + (-0.3776192402141899 + x15)^2) + x498 * ((
    -0.7280090144638749 + x13)^2 + (-0.15636110839409045 + x14)^2 + (
    -0.46978018596620896 + x15)^2) + x499 * ((-0.11088006780742277 + x13)^2 + (
    -0.34039206766760943 + x14)^2 + (-0.06827700620696797 + x15)^2) + x500 * ((
    -0.6997602128647453 + x13)^2 + (-0.43764462531136417 + x14)^2 + (
    -0.21027262835312888 + x15)^2) + x501 * ((-0.04425963668315558 + x13)^2 + (
    -0.05866963958501248 + x14)^2 + (-0.3542816901635206 + x15)^2) + x502 * ((
    -0.9757731519147661 + x13)^2 + (-0.3254673022536907 + x14)^2 + (
    -0.6814338527690927 + x15)^2) + x503 * ((-0.7472668303106704 + x13)^2 + (
    -0.0007097732419126812 + x14)^2 + (-0.9280520527234516 + x15)^2) + x504 * (
    (-0.5322530736526498 + x13)^2 + (-0.39754547356694514 + x14)^2 + (
    -0.13635594663989958 + x15)^2) + x505 * ((-0.0007978441992585461 + x13)^2
    + (-0.8844692811473446 + x14)^2 + (-0.1467696053297397 + x15)^2) + x506 *
    ((-0.482850676866177 + x13)^2 + (-0.10574453600064249 + x14)^2 + (
    -0.8791132223988765 + x15)^2) + x507 * ((-0.7291125910415815 + x13)^2 + (
    -0.2090180996227905 + x14)^2 + (-0.5040401706411071 + x15)^2) + x508 * ((
    -0.6406085128291104 + x13)^2 + (-0.11496605173886654 + x14)^2 + (
    -0.7597217863145667 + x15)^2) + x509 * ((-0.6527145527530681 + x13)^2 + (
    -0.09871984518132071 + x14)^2 + (-0.08020459573270278 + x15)^2) + x510 * ((
    -0.5779788427476141 + x13)^2 + (-0.6106348650543917 + x14)^2 + (
    -0.21791347819398965 + x15)^2) + x511 * ((-0.894563747191656 + x13)^2 + (
    -0.49991063769677824 + x14)^2 + (-0.8312284742613548 + x15)^2) + x512 * ((
    -0.5477983688744066 + x13)^2 + (-0.10123589526888899 + x14)^2 + (
    -0.9724165689826183 + x15)^2) + x513 * ((-0.7051711697372745 + x13)^2 + (
    -0.6974870695940615 + x14)^2 + (-0.34185115432121194 + x15)^2) + x514 * ((
    -0.965288766829392 + x13)^2 + (-0.3541459265683641 + x14)^2 + (
    -0.5256833284803955 + x15)^2) + x515 * ((-0.486217312364274 + x13)^2 + (
    -0.877880388733161 + x14)^2 + (-0.7007637309302288 + x15)^2) + x516 * ((
    -0.9239018568218517 + x13)^2 + (-0.8696579903239924 + x14)^2 + (
    -0.9905428630635226 + x15)^2) + x517 * ((-0.5635239214739318 + x13)^2 + (
    -0.5212076565782671 + x14)^2 + (-0.672320998946101 + x15)^2) + x518 * ((
    -0.6336849702734496 + x13)^2 + (-0.17934198400132562 + x14)^2 + (
    -0.25720032541892046 + x15)^2) + x519 * ((-0.3593028476464476 + x13)^2 + (
    -0.7339808423425379 + x14)^2 + (-0.001964432484070411 + x15)^2) + x520 * ((
    -0.11194390371791885 + x13)^2 + (-0.05379441414468389 + x14)^2 + (
    -0.943183016792168 + x15)^2) + x521 * ((-0.23043169327406487 + x13)^2 + (
    -0.9554781274626842 + x14)^2 + (-0.7782415771343315 + x15)^2) + x522 * ((
    -0.999963313244285 + x13)^2 + (-0.18638094695235063 + x14)^2 + (
    -0.8044007834975228 + x15)^2) + x523 * ((-0.8484168552839887 + x13)^2 + (
    -0.5800377498791588 + x14)^2 + (-0.5020163714056717 + x15)^2) + x524 * ((
    -0.43417113739871793 + x13)^2 + (-0.12296667128824068 + x14)^2 + (
    -0.9424473212335941 + x15)^2) + x525 * ((-0.18738087377060708 + x16)^2 + (
    -0.9668125465448587 + x17)^2 + (-0.3553159637279516 + x18)^2) + x526 * ((
    -0.8016174920011017 + x16)^2 + (-0.26778829228978485 + x17)^2 + (
    -0.4359301947251404 + x18)^2) + x527 * ((-0.8607174064209905 + x16)^2 + (
    -0.9118236037302004 + x17)^2 + (-0.8874753085224066 + x18)^2) + x528 * ((
    -0.4306937407201691 + x16)^2 + (-0.17428784944790254 + x17)^2 + (
    -0.561800026051346 + x18)^2) + x529 * ((-0.08746124891679041 + x16)^2 + (
    -0.054985697990341253 + x17)^2 + (-0.24949780749022454 + x18)^2) + x530 * (
    (-0.62658802169963 + x16)^2 + (-0.6857573511475539 + x17)^2 + (
    -0.47366426896437996 + x18)^2) + x531 * ((-0.6114768638799523 + x16)^2 + (
    -0.41752031846706683 + x17)^2 + (-0.9109986593014991 + x18)^2) + x532 * ((
    -0.46817035806173857 + x16)^2 + (-0.5569854753991196 + x17)^2 + (
    -0.25003006243034176 + x18)^2) + x533 * ((-0.401092643486621 + x16)^2 + (
    -0.7625123366098691 + x17)^2 + (-0.5084739888197645 + x18)^2) + x534 * ((
    -0.2748596346062746 + x16)^2 + (-0.1892957165775404 + x17)^2 + (
    -0.9442182422598734 + x18)^2) + x535 * ((-0.44167309428028 + x16)^2 + (
    -0.33521919326002436 + x17)^2 + (-0.5030312028077185 + x18)^2) + x536 * ((
    -0.7052213106378172 + x16)^2 + (-0.48063756935051416 + x17)^2 + (
    -0.26073089985191056 + x18)^2) + x537 * ((-0.34955478256076744 + x16)^2 + (
    -0.08326067710845486 + x17)^2 + (-0.5749118628581387 + x18)^2) + x538 * ((
    -0.559986490193569 + x16)^2 + (-0.8433283983822369 + x17)^2 + (
    -0.2573012139171522 + x18)^2) + x539 * ((-0.15759317998774103 + x16)^2 + (
    -0.876898613808363 + x17)^2 + (-0.7812095651757611 + x18)^2) + x540 * ((
    -0.20930481325083095 + x16)^2 + (-0.5243112169526106 + x17)^2 + (
    -0.11364820868480618 + x18)^2) + x541 * ((-0.6971614684173857 + x16)^2 + (
    -0.48152793919664516 + x17)^2 + (-0.10432894263476011 + x18)^2) + x542 * ((
    -0.9788390123597811 + x16)^2 + (-0.6759032973315947 + x17)^2 + (
    -0.9815212516574683 + x18)^2) + x543 * ((-0.31006923192398295 + x16)^2 + (
    -0.9279588991073839 + x17)^2 + (-0.6170791410768803 + x18)^2) + x544 * ((
    -0.2636621784047203 + x16)^2 + (-0.5756031327528047 + x17)^2 + (
    -0.6339965151056094 + x18)^2) + x545 * ((-0.07735274294755135 + x16)^2 + (
    -0.7932728374366258 + x17)^2 + (-0.3905222095735743 + x18)^2) + x546 * ((
    -0.9596478643023862 + x16)^2 + (-0.8323332845748266 + x17)^2 + (
    -0.9490817947377156 + x18)^2) + x547 * ((-0.691877291867759 + x16)^2 + (
    -0.27901589567669627 + x17)^2 + (-0.9603405866805156 + x18)^2) + x548 * ((
    -0.3248230089198071 + x16)^2 + (-0.704031342612858 + x17)^2 + (
    -0.6022746223457217 + x18)^2) + x549 * ((-0.7925246012498328 + x16)^2 + (
    -0.5142003887500619 + x17)^2 + (-0.07412078079700912 + x18)^2) + x550 * ((
    -0.4636597419285817 + x16)^2 + (-0.28493324045279156 + x17)^2 + (
    -0.8982018087470489 + x18)^2) + x551 * ((-0.3125245397681232 + x16)^2 + (
    -0.25776762798299757 + x17)^2 + (-0.05720177574934948 + x18)^2) + x552 * ((
    -0.3197520940611892 + x16)^2 + (-0.8476152339851849 + x17)^2 + (
    -0.36763530621177176 + x18)^2) + x553 * ((-0.7452568897412712 + x16)^2 + (
    -0.24553180487125725 + x17)^2 + (-0.5097535241044541 + x18)^2) + x554 * ((
    -0.7098335381446684 + x16)^2 + (-0.8340974705497336 + x17)^2 + (
    -0.181763781584372 + x18)^2) + x555 * ((-0.46361936352247957 + x16)^2 + (
    -0.5052840929896205 + x17)^2 + (-0.44590180298842885 + x18)^2) + x556 * ((
    -0.38556721731694843 + x16)^2 + (-0.8579051939296445 + x17)^2 + (
    -0.9532247922542321 + x18)^2) + x557 * ((-0.08582521461459391 + x16)^2 + (
    -0.1846731910506113 + x17)^2 + (-0.8745914265553065 + x18)^2) + x558 * ((
    -0.8832914121602843 + x16)^2 + (-0.6513632907999211 + x17)^2 + (
    -0.21823458079012226 + x18)^2) + x559 * ((-0.5751096041706857 + x16)^2 + (
    -0.67547809352205 + x17)^2 + (-0.02460221547003949 + x18)^2) + x560 * ((
    -0.31457012214576896 + x16)^2 + (-0.6742238394444281 + x17)^2 + (
    -0.5445193883971214 + x18)^2) + x561 * ((-0.11915949121286373 + x16)^2 + (
    -0.7063249001765594 + x17)^2 + (-0.2705862773526916 + x18)^2) + x562 * ((
    -0.6669226676581618 + x16)^2 + (-0.5285881831609426 + x17)^2 + (
    -0.11309761756326353 + x18)^2) + x563 * ((-0.12347539452476952 + x16)^2 + (
    -0.39576104678223545 + x17)^2 + (-0.5346277380867844 + x18)^2) + x564 * ((
    -0.6078285274199232 + x16)^2 + (-0.14297039718498794 + x17)^2 + (
    -0.9770203015468777 + x18)^2) + x565 * ((-0.3646785363094529 + x16)^2 + (
    -0.7442303679522239 + x17)^2 + (-0.6078205952200681 + x18)^2) + x566 * ((
    -0.5210217205095699 + x16)^2 + (-0.8432559359514145 + x17)^2 + (
    -0.22452982644506148 + x18)^2) + x567 * ((-0.08751493934711652 + x16)^2 + (
    -0.4416120245181858 + x17)^2 + (-0.026527914551422116 + x18)^2) + x568 * ((
    -0.01197633335476489 + x16)^2 + (-0.2890291018825958 + x17)^2 + (
    -0.38681268974270067 + x18)^2) + x569 * ((-0.7095057303156089 + x16)^2 + (
    -0.931861745530449 + x17)^2 + (-0.14043671018799309 + x18)^2) + x570 * ((
    -0.0895696243176286 + x16)^2 + (-0.5380623897726036 + x17)^2 + (
    -0.21800740949887965 + x18)^2) + x571 * ((-0.7815676711928884 + x16)^2 + (
    -0.018922864242984283 + x17)^2 + (-0.28596537520912735 + x18)^2) + x572 * (
    (-0.1740875221968632 + x16)^2 + (-0.5678042483964806 + x17)^2 + (
    -0.5661715765543827 + x18)^2) + x573 * ((-0.026589535186742008 + x16)^2 + (
    -0.764188329062881 + x17)^2 + (-0.573675168853155 + x18)^2) + x574 * ((
    -0.369798170078249 + x16)^2 + (-0.9415339432121399 + x17)^2 + (
    -0.6729904295003972 + x18)^2) + x575 * ((-0.8040803150564447 + x16)^2 + (
    -0.1553864280131183 + x17)^2 + (-0.8148818001526622 + x18)^2) + x576 * ((
    -0.26589528353030667 + x16)^2 + (-0.3666027540410405 + x17)^2 + (
    -0.468491747882274 + x18)^2) + x577 * ((-0.7258236750794794 + x16)^2 + (
    -0.6727872398248785 + x17)^2 + (-0.28367538142810256 + x18)^2) + x578 * ((
    -0.9220733933477209 + x16)^2 + (-0.26257553387761134 + x17)^2 + (
    -0.7191645521015703 + x18)^2) + x579 * ((-0.9500341346045207 + x16)^2 + (
    -0.638006708190589 + x17)^2 + (-0.07543033185744508 + x18)^2) + x580 * ((
    -0.10545996998960727 + x16)^2 + (-0.7011113856167448 + x17)^2 + (
    -0.20681983539603999 + x18)^2) + x581 * ((-0.6551186918756842 + x16)^2 + (
    -0.6398068804459004 + x17)^2 + (-0.9931175421141764 + x18)^2) + x582 * ((
    -0.7142120519447257 + x16)^2 + (-0.46243457004259436 + x17)^2 + (
    -0.5481708822495015 + x18)^2) + x583 * ((-0.4950904200820069 + x16)^2 + (
    -0.897797250865998 + x17)^2 + (-0.2346789175833377 + x18)^2) + x584 * ((
    -0.6440952365033279 + x16)^2 + (-0.33381998176403327 + x17)^2 + (
    -0.5869170180027279 + x18)^2) + x585 * ((-0.8591109395866232 + x16)^2 + (
    -0.8400580742862248 + x17)^2 + (-0.7678032609886081 + x18)^2) + x586 * ((
    -0.7791674853861603 + x16)^2 + (-0.45754256977454044 + x17)^2 + (
    -0.30909012057666696 + x18)^2) + x587 * ((-0.8968075661486302 + x16)^2 + (
    -0.34892321725590947 + x17)^2 + (-0.05826567448243425 + x18)^2) + x588 * ((
    -0.3189815847959586 + x16)^2 + (-0.3926628302556219 + x17)^2 + (
    -0.07205292941157881 + x18)^2) + x589 * ((-0.8146221960807916 + x16)^2 + (
    -0.4969763360408802 + x17)^2 + (-0.3647398823672149 + x18)^2) + x590 * ((
    -0.23899160200316316 + x16)^2 + (-0.39386695871622013 + x17)^2 + (
    -0.6832280563167916 + x18)^2) + x591 * ((-0.3505164112410739 + x16)^2 + (
    -0.474289602074489 + x17)^2 + (-0.09409181759710883 + x18)^2) + x592 * ((
    -0.9669824450132469 + x16)^2 + (-0.7209255968341481 + x17)^2 + (
    -0.013074465617943565 + x18)^2) + x593 * ((-0.7769547473829561 + x16)^2 + (
    -0.8065173816239941 + x17)^2 + (-0.7160376893035372 + x18)^2) + x594 * ((
    -0.3489895458178166 + x16)^2 + (-0.35733085724791824 + x17)^2 + (
    -0.8864875891533408 + x18)^2) + x595 * ((-0.0664995679925865 + x16)^2 + (
    -0.7243483038068983 + x17)^2 + (-0.9303195285204333 + x18)^2) + x596 * ((
    -0.8115323501210528 + x16)^2 + (-0.42672295637197755 + x17)^2 + (
    -0.04261529652953755 + x18)^2) + x597 * ((-0.3704618379844066 + x16)^2 + (
    -0.1443368240568217 + x17)^2 + (-0.3776192402141899 + x18)^2) + x598 * ((
    -0.7280090144638749 + x16)^2 + (-0.15636110839409045 + x17)^2 + (
    -0.46978018596620896 + x18)^2) + x599 * ((-0.11088006780742277 + x16)^2 + (
    -0.34039206766760943 + x17)^2 + (-0.06827700620696797 + x18)^2) + x600 * ((
    -0.6997602128647453 + x16)^2 + (-0.43764462531136417 + x17)^2 + (
    -0.21027262835312888 + x18)^2) + x601 * ((-0.04425963668315558 + x16)^2 + (
    -0.05866963958501248 + x17)^2 + (-0.3542816901635206 + x18)^2) + x602 * ((
    -0.9757731519147661 + x16)^2 + (-0.3254673022536907 + x17)^2 + (
    -0.6814338527690927 + x18)^2) + x603 * ((-0.7472668303106704 + x16)^2 + (
    -0.0007097732419126812 + x17)^2 + (-0.9280520527234516 + x18)^2) + x604 * (
    (-0.5322530736526498 + x16)^2 + (-0.39754547356694514 + x17)^2 + (
    -0.13635594663989958 + x18)^2) + x605 * ((-0.0007978441992585461 + x16)^2
    + (-0.8844692811473446 + x17)^2 + (-0.1467696053297397 + x18)^2) + x606 *
    ((-0.482850676866177 + x16)^2 + (-0.10574453600064249 + x17)^2 + (
    -0.8791132223988765 + x18)^2) + x607 * ((-0.7291125910415815 + x16)^2 + (
    -0.2090180996227905 + x17)^2 + (-0.5040401706411071 + x18)^2) + x608 * ((
    -0.6406085128291104 + x16)^2 + (-0.11496605173886654 + x17)^2 + (
    -0.7597217863145667 + x18)^2) + x609 * ((-0.6527145527530681 + x16)^2 + (
    -0.09871984518132071 + x17)^2 + (-0.08020459573270278 + x18)^2) + x610 * ((
    -0.5779788427476141 + x16)^2 + (-0.6106348650543917 + x17)^2 + (
    -0.21791347819398965 + x18)^2) + x611 * ((-0.894563747191656 + x16)^2 + (
    -0.49991063769677824 + x17)^2 + (-0.8312284742613548 + x18)^2) + x612 * ((
    -0.5477983688744066 + x16)^2 + (-0.10123589526888899 + x17)^2 + (
    -0.9724165689826183 + x18)^2) + x613 * ((-0.7051711697372745 + x16)^2 + (
    -0.6974870695940615 + x17)^2 + (-0.34185115432121194 + x18)^2) + x614 * ((
    -0.965288766829392 + x16)^2 + (-0.3541459265683641 + x17)^2 + (
    -0.5256833284803955 + x18)^2) + x615 * ((-0.486217312364274 + x16)^2 + (
    -0.877880388733161 + x17)^2 + (-0.7007637309302288 + x18)^2) + x616 * ((
    -0.9239018568218517 + x16)^2 + (-0.8696579903239924 + x17)^2 + (
    -0.9905428630635226 + x18)^2) + x617 * ((-0.5635239214739318 + x16)^2 + (
    -0.5212076565782671 + x17)^2 + (-0.672320998946101 + x18)^2) + x618 * ((
    -0.6336849702734496 + x16)^2 + (-0.17934198400132562 + x17)^2 + (
    -0.25720032541892046 + x18)^2) + x619 * ((-0.3593028476464476 + x16)^2 + (
    -0.7339808423425379 + x17)^2 + (-0.001964432484070411 + x18)^2) + x620 * ((
    -0.11194390371791885 + x16)^2 + (-0.05379441414468389 + x17)^2 + (
    -0.943183016792168 + x18)^2) + x621 * ((-0.23043169327406487 + x16)^2 + (
    -0.9554781274626842 + x17)^2 + (-0.7782415771343315 + x18)^2) + x622 * ((
    -0.999963313244285 + x16)^2 + (-0.18638094695235063 + x17)^2 + (
    -0.8044007834975228 + x18)^2) + x623 * ((-0.8484168552839887 + x16)^2 + (
    -0.5800377498791588 + x17)^2 + (-0.5020163714056717 + x18)^2) + x624 * ((
    -0.43417113739871793 + x16)^2 + (-0.12296667128824068 + x17)^2 + (
    -0.9424473212335941 + x18)^2) + x625 * ((-0.18738087377060708 + x19)^2 + (
    -0.9668125465448587 + x20)^2 + (-0.3553159637279516 + x21)^2) + x626 * ((
    -0.8016174920011017 + x19)^2 + (-0.26778829228978485 + x20)^2 + (
    -0.4359301947251404 + x21)^2) + x627 * ((-0.8607174064209905 + x19)^2 + (
    -0.9118236037302004 + x20)^2 + (-0.8874753085224066 + x21)^2) + x628 * ((
    -0.4306937407201691 + x19)^2 + (-0.17428784944790254 + x20)^2 + (
    -0.561800026051346 + x21)^2) + x629 * ((-0.08746124891679041 + x19)^2 + (
    -0.054985697990341253 + x20)^2 + (-0.24949780749022454 + x21)^2) + x630 * (
    (-0.62658802169963 + x19)^2 + (-0.6857573511475539 + x20)^2 + (
    -0.47366426896437996 + x21)^2) + x631 * ((-0.6114768638799523 + x19)^2 + (
    -0.41752031846706683 + x20)^2 + (-0.9109986593014991 + x21)^2) + x632 * ((
    -0.46817035806173857 + x19)^2 + (-0.5569854753991196 + x20)^2 + (
    -0.25003006243034176 + x21)^2) + x633 * ((-0.401092643486621 + x19)^2 + (
    -0.7625123366098691 + x20)^2 + (-0.5084739888197645 + x21)^2) + x634 * ((
    -0.2748596346062746 + x19)^2 + (-0.1892957165775404 + x20)^2 + (
    -0.9442182422598734 + x21)^2) + x635 * ((-0.44167309428028 + x19)^2 + (
    -0.33521919326002436 + x20)^2 + (-0.5030312028077185 + x21)^2) + x636 * ((
    -0.7052213106378172 + x19)^2 + (-0.48063756935051416 + x20)^2 + (
    -0.26073089985191056 + x21)^2) + x637 * ((-0.34955478256076744 + x19)^2 + (
    -0.08326067710845486 + x20)^2 + (-0.5749118628581387 + x21)^2) + x638 * ((
    -0.559986490193569 + x19)^2 + (-0.8433283983822369 + x20)^2 + (
    -0.2573012139171522 + x21)^2) + x639 * ((-0.15759317998774103 + x19)^2 + (
    -0.876898613808363 + x20)^2 + (-0.7812095651757611 + x21)^2) + x640 * ((
    -0.20930481325083095 + x19)^2 + (-0.5243112169526106 + x20)^2 + (
    -0.11364820868480618 + x21)^2) + x641 * ((-0.6971614684173857 + x19)^2 + (
    -0.48152793919664516 + x20)^2 + (-0.10432894263476011 + x21)^2) + x642 * ((
    -0.9788390123597811 + x19)^2 + (-0.6759032973315947 + x20)^2 + (
    -0.9815212516574683 + x21)^2) + x643 * ((-0.31006923192398295 + x19)^2 + (
    -0.9279588991073839 + x20)^2 + (-0.6170791410768803 + x21)^2) + x644 * ((
    -0.2636621784047203 + x19)^2 + (-0.5756031327528047 + x20)^2 + (
    -0.6339965151056094 + x21)^2) + x645 * ((-0.07735274294755135 + x19)^2 + (
    -0.7932728374366258 + x20)^2 + (-0.3905222095735743 + x21)^2) + x646 * ((
    -0.9596478643023862 + x19)^2 + (-0.8323332845748266 + x20)^2 + (
    -0.9490817947377156 + x21)^2) + x647 * ((-0.691877291867759 + x19)^2 + (
    -0.27901589567669627 + x20)^2 + (-0.9603405866805156 + x21)^2) + x648 * ((
    -0.3248230089198071 + x19)^2 + (-0.704031342612858 + x20)^2 + (
    -0.6022746223457217 + x21)^2) + x649 * ((-0.7925246012498328 + x19)^2 + (
    -0.5142003887500619 + x20)^2 + (-0.07412078079700912 + x21)^2) + x650 * ((
    -0.4636597419285817 + x19)^2 + (-0.28493324045279156 + x20)^2 + (
    -0.8982018087470489 + x21)^2) + x651 * ((-0.3125245397681232 + x19)^2 + (
    -0.25776762798299757 + x20)^2 + (-0.05720177574934948 + x21)^2) + x652 * ((
    -0.3197520940611892 + x19)^2 + (-0.8476152339851849 + x20)^2 + (
    -0.36763530621177176 + x21)^2) + x653 * ((-0.7452568897412712 + x19)^2 + (
    -0.24553180487125725 + x20)^2 + (-0.5097535241044541 + x21)^2) + x654 * ((
    -0.7098335381446684 + x19)^2 + (-0.8340974705497336 + x20)^2 + (
    -0.181763781584372 + x21)^2) + x655 * ((-0.46361936352247957 + x19)^2 + (
    -0.5052840929896205 + x20)^2 + (-0.44590180298842885 + x21)^2) + x656 * ((
    -0.38556721731694843 + x19)^2 + (-0.8579051939296445 + x20)^2 + (
    -0.9532247922542321 + x21)^2) + x657 * ((-0.08582521461459391 + x19)^2 + (
    -0.1846731910506113 + x20)^2 + (-0.8745914265553065 + x21)^2) + x658 * ((
    -0.8832914121602843 + x19)^2 + (-0.6513632907999211 + x20)^2 + (
    -0.21823458079012226 + x21)^2) + x659 * ((-0.5751096041706857 + x19)^2 + (
    -0.67547809352205 + x20)^2 + (-0.02460221547003949 + x21)^2) + x660 * ((
    -0.31457012214576896 + x19)^2 + (-0.6742238394444281 + x20)^2 + (
    -0.5445193883971214 + x21)^2) + x661 * ((-0.11915949121286373 + x19)^2 + (
    -0.7063249001765594 + x20)^2 + (-0.2705862773526916 + x21)^2) + x662 * ((
    -0.6669226676581618 + x19)^2 + (-0.5285881831609426 + x20)^2 + (
    -0.11309761756326353 + x21)^2) + x663 * ((-0.12347539452476952 + x19)^2 + (
    -0.39576104678223545 + x20)^2 + (-0.5346277380867844 + x21)^2) + x664 * ((
    -0.6078285274199232 + x19)^2 + (-0.14297039718498794 + x20)^2 + (
    -0.9770203015468777 + x21)^2) + x665 * ((-0.3646785363094529 + x19)^2 + (
    -0.7442303679522239 + x20)^2 + (-0.6078205952200681 + x21)^2) + x666 * ((
    -0.5210217205095699 + x19)^2 + (-0.8432559359514145 + x20)^2 + (
    -0.22452982644506148 + x21)^2) + x667 * ((-0.08751493934711652 + x19)^2 + (
    -0.4416120245181858 + x20)^2 + (-0.026527914551422116 + x21)^2) + x668 * ((
    -0.01197633335476489 + x19)^2 + (-0.2890291018825958 + x20)^2 + (
    -0.38681268974270067 + x21)^2) + x669 * ((-0.7095057303156089 + x19)^2 + (
    -0.931861745530449 + x20)^2 + (-0.14043671018799309 + x21)^2) + x670 * ((
    -0.0895696243176286 + x19)^2 + (-0.5380623897726036 + x20)^2 + (
    -0.21800740949887965 + x21)^2) + x671 * ((-0.7815676711928884 + x19)^2 + (
    -0.018922864242984283 + x20)^2 + (-0.28596537520912735 + x21)^2) + x672 * (
    (-0.1740875221968632 + x19)^2 + (-0.5678042483964806 + x20)^2 + (
    -0.5661715765543827 + x21)^2) + x673 * ((-0.026589535186742008 + x19)^2 + (
    -0.764188329062881 + x20)^2 + (-0.573675168853155 + x21)^2) + x674 * ((
    -0.369798170078249 + x19)^2 + (-0.9415339432121399 + x20)^2 + (
    -0.6729904295003972 + x21)^2) + x675 * ((-0.8040803150564447 + x19)^2 + (
    -0.1553864280131183 + x20)^2 + (-0.8148818001526622 + x21)^2) + x676 * ((
    -0.26589528353030667 + x19)^2 + (-0.3666027540410405 + x20)^2 + (
    -0.468491747882274 + x21)^2) + x677 * ((-0.7258236750794794 + x19)^2 + (
    -0.6727872398248785 + x20)^2 + (-0.28367538142810256 + x21)^2) + x678 * ((
    -0.9220733933477209 + x19)^2 + (-0.26257553387761134 + x20)^2 + (
    -0.7191645521015703 + x21)^2) + x679 * ((-0.9500341346045207 + x19)^2 + (
    -0.638006708190589 + x20)^2 + (-0.07543033185744508 + x21)^2) + x680 * ((
    -0.10545996998960727 + x19)^2 + (-0.7011113856167448 + x20)^2 + (
    -0.20681983539603999 + x21)^2) + x681 * ((-0.6551186918756842 + x19)^2 + (
    -0.6398068804459004 + x20)^2 + (-0.9931175421141764 + x21)^2) + x682 * ((
    -0.7142120519447257 + x19)^2 + (-0.46243457004259436 + x20)^2 + (
    -0.5481708822495015 + x21)^2) + x683 * ((-0.4950904200820069 + x19)^2 + (
    -0.897797250865998 + x20)^2 + (-0.2346789175833377 + x21)^2) + x684 * ((
    -0.6440952365033279 + x19)^2 + (-0.33381998176403327 + x20)^2 + (
    -0.5869170180027279 + x21)^2) + x685 * ((-0.8591109395866232 + x19)^2 + (
    -0.8400580742862248 + x20)^2 + (-0.7678032609886081 + x21)^2) + x686 * ((
    -0.7791674853861603 + x19)^2 + (-0.45754256977454044 + x20)^2 + (
    -0.30909012057666696 + x21)^2) + x687 * ((-0.8968075661486302 + x19)^2 + (
    -0.34892321725590947 + x20)^2 + (-0.05826567448243425 + x21)^2) + x688 * ((
    -0.3189815847959586 + x19)^2 + (-0.3926628302556219 + x20)^2 + (
    -0.07205292941157881 + x21)^2) + x689 * ((-0.8146221960807916 + x19)^2 + (
    -0.4969763360408802 + x20)^2 + (-0.3647398823672149 + x21)^2) + x690 * ((
    -0.23899160200316316 + x19)^2 + (-0.39386695871622013 + x20)^2 + (
    -0.6832280563167916 + x21)^2) + x691 * ((-0.3505164112410739 + x19)^2 + (
    -0.474289602074489 + x20)^2 + (-0.09409181759710883 + x21)^2) + x692 * ((
    -0.9669824450132469 + x19)^2 + (-0.7209255968341481 + x20)^2 + (
    -0.013074465617943565 + x21)^2) + x693 * ((-0.7769547473829561 + x19)^2 + (
    -0.8065173816239941 + x20)^2 + (-0.7160376893035372 + x21)^2) + x694 * ((
    -0.3489895458178166 + x19)^2 + (-0.35733085724791824 + x20)^2 + (
    -0.8864875891533408 + x21)^2) + x695 * ((-0.0664995679925865 + x19)^2 + (
    -0.7243483038068983 + x20)^2 + (-0.9303195285204333 + x21)^2) + x696 * ((
    -0.8115323501210528 + x19)^2 + (-0.42672295637197755 + x20)^2 + (
    -0.04261529652953755 + x21)^2) + x697 * ((-0.3704618379844066 + x19)^2 + (
    -0.1443368240568217 + x20)^2 + (-0.3776192402141899 + x21)^2) + x698 * ((
    -0.7280090144638749 + x19)^2 + (-0.15636110839409045 + x20)^2 + (
    -0.46978018596620896 + x21)^2) + x699 * ((-0.11088006780742277 + x19)^2 + (
    -0.34039206766760943 + x20)^2 + (-0.06827700620696797 + x21)^2) + x700 * ((
    -0.6997602128647453 + x19)^2 + (-0.43764462531136417 + x20)^2 + (
    -0.21027262835312888 + x21)^2) + x701 * ((-0.04425963668315558 + x19)^2 + (
    -0.05866963958501248 + x20)^2 + (-0.3542816901635206 + x21)^2) + x702 * ((
    -0.9757731519147661 + x19)^2 + (-0.3254673022536907 + x20)^2 + (
    -0.6814338527690927 + x21)^2) + x703 * ((-0.7472668303106704 + x19)^2 + (
    -0.0007097732419126812 + x20)^2 + (-0.9280520527234516 + x21)^2) + x704 * (
    (-0.5322530736526498 + x19)^2 + (-0.39754547356694514 + x20)^2 + (
    -0.13635594663989958 + x21)^2) + x705 * ((-0.0007978441992585461 + x19)^2
    + (-0.8844692811473446 + x20)^2 + (-0.1467696053297397 + x21)^2) + x706 *
    ((-0.482850676866177 + x19)^2 + (-0.10574453600064249 + x20)^2 + (
    -0.8791132223988765 + x21)^2) + x707 * ((-0.7291125910415815 + x19)^2 + (
    -0.2090180996227905 + x20)^2 + (-0.5040401706411071 + x21)^2) + x708 * ((
    -0.6406085128291104 + x19)^2 + (-0.11496605173886654 + x20)^2 + (
    -0.7597217863145667 + x21)^2) + x709 * ((-0.6527145527530681 + x19)^2 + (
    -0.09871984518132071 + x20)^2 + (-0.08020459573270278 + x21)^2) + x710 * ((
    -0.5779788427476141 + x19)^2 + (-0.6106348650543917 + x20)^2 + (
    -0.21791347819398965 + x21)^2) + x711 * ((-0.894563747191656 + x19)^2 + (
    -0.49991063769677824 + x20)^2 + (-0.8312284742613548 + x21)^2) + x712 * ((
    -0.5477983688744066 + x19)^2 + (-0.10123589526888899 + x20)^2 + (
    -0.9724165689826183 + x21)^2) + x713 * ((-0.7051711697372745 + x19)^2 + (
    -0.6974870695940615 + x20)^2 + (-0.34185115432121194 + x21)^2) + x714 * ((
    -0.965288766829392 + x19)^2 + (-0.3541459265683641 + x20)^2 + (
    -0.5256833284803955 + x21)^2) + x715 * ((-0.486217312364274 + x19)^2 + (
    -0.877880388733161 + x20)^2 + (-0.7007637309302288 + x21)^2) + x716 * ((
    -0.9239018568218517 + x19)^2 + (-0.8696579903239924 + x20)^2 + (
    -0.9905428630635226 + x21)^2) + x717 * ((-0.5635239214739318 + x19)^2 + (
    -0.5212076565782671 + x20)^2 + (-0.672320998946101 + x21)^2) + x718 * ((
    -0.6336849702734496 + x19)^2 + (-0.17934198400132562 + x20)^2 + (
    -0.25720032541892046 + x21)^2) + x719 * ((-0.3593028476464476 + x19)^2 + (
    -0.7339808423425379 + x20)^2 + (-0.001964432484070411 + x21)^2) + x720 * ((
    -0.11194390371791885 + x19)^2 + (-0.05379441414468389 + x20)^2 + (
    -0.943183016792168 + x21)^2) + x721 * ((-0.23043169327406487 + x19)^2 + (
    -0.9554781274626842 + x20)^2 + (-0.7782415771343315 + x21)^2) + x722 * ((
    -0.999963313244285 + x19)^2 + (-0.18638094695235063 + x20)^2 + (
    -0.8044007834975228 + x21)^2) + x723 * ((-0.8484168552839887 + x19)^2 + (
    -0.5800377498791588 + x20)^2 + (-0.5020163714056717 + x21)^2) + x724 * ((
    -0.43417113739871793 + x19)^2 + (-0.12296667128824068 + x20)^2 + (
    -0.9424473212335941 + x21)^2) + x725 * ((-0.18738087377060708 + x22)^2 + (
    -0.9668125465448587 + x23)^2 + (-0.3553159637279516 + x24)^2) + x726 * ((
    -0.8016174920011017 + x22)^2 + (-0.26778829228978485 + x23)^2 + (
    -0.4359301947251404 + x24)^2) + x727 * ((-0.8607174064209905 + x22)^2 + (
    -0.9118236037302004 + x23)^2 + (-0.8874753085224066 + x24)^2) + x728 * ((
    -0.4306937407201691 + x22)^2 + (-0.17428784944790254 + x23)^2 + (
    -0.561800026051346 + x24)^2) + x729 * ((-0.08746124891679041 + x22)^2 + (
    -0.054985697990341253 + x23)^2 + (-0.24949780749022454 + x24)^2) + x730 * (
    (-0.62658802169963 + x22)^2 + (-0.6857573511475539 + x23)^2 + (
    -0.47366426896437996 + x24)^2) + x731 * ((-0.6114768638799523 + x22)^2 + (
    -0.41752031846706683 + x23)^2 + (-0.9109986593014991 + x24)^2) + x732 * ((
    -0.46817035806173857 + x22)^2 + (-0.5569854753991196 + x23)^2 + (
    -0.25003006243034176 + x24)^2) + x733 * ((-0.401092643486621 + x22)^2 + (
    -0.7625123366098691 + x23)^2 + (-0.5084739888197645 + x24)^2) + x734 * ((
    -0.2748596346062746 + x22)^2 + (-0.1892957165775404 + x23)^2 + (
    -0.9442182422598734 + x24)^2) + x735 * ((-0.44167309428028 + x22)^2 + (
    -0.33521919326002436 + x23)^2 + (-0.5030312028077185 + x24)^2) + x736 * ((
    -0.7052213106378172 + x22)^2 + (-0.48063756935051416 + x23)^2 + (
    -0.26073089985191056 + x24)^2) + x737 * ((-0.34955478256076744 + x22)^2 + (
    -0.08326067710845486 + x23)^2 + (-0.5749118628581387 + x24)^2) + x738 * ((
    -0.559986490193569 + x22)^2 + (-0.8433283983822369 + x23)^2 + (
    -0.2573012139171522 + x24)^2) + x739 * ((-0.15759317998774103 + x22)^2 + (
    -0.876898613808363 + x23)^2 + (-0.7812095651757611 + x24)^2) + x740 * ((
    -0.20930481325083095 + x22)^2 + (-0.5243112169526106 + x23)^2 + (
    -0.11364820868480618 + x24)^2) + x741 * ((-0.6971614684173857 + x22)^2 + (
    -0.48152793919664516 + x23)^2 + (-0.10432894263476011 + x24)^2) + x742 * ((
    -0.9788390123597811 + x22)^2 + (-0.6759032973315947 + x23)^2 + (
    -0.9815212516574683 + x24)^2) + x743 * ((-0.31006923192398295 + x22)^2 + (
    -0.9279588991073839 + x23)^2 + (-0.6170791410768803 + x24)^2) + x744 * ((
    -0.2636621784047203 + x22)^2 + (-0.5756031327528047 + x23)^2 + (
    -0.6339965151056094 + x24)^2) + x745 * ((-0.07735274294755135 + x22)^2 + (
    -0.7932728374366258 + x23)^2 + (-0.3905222095735743 + x24)^2) + x746 * ((
    -0.9596478643023862 + x22)^2 + (-0.8323332845748266 + x23)^2 + (
    -0.9490817947377156 + x24)^2) + x747 * ((-0.691877291867759 + x22)^2 + (
    -0.27901589567669627 + x23)^2 + (-0.9603405866805156 + x24)^2) + x748 * ((
    -0.3248230089198071 + x22)^2 + (-0.704031342612858 + x23)^2 + (
    -0.6022746223457217 + x24)^2) + x749 * ((-0.7925246012498328 + x22)^2 + (
    -0.5142003887500619 + x23)^2 + (-0.07412078079700912 + x24)^2) + x750 * ((
    -0.4636597419285817 + x22)^2 + (-0.28493324045279156 + x23)^2 + (
    -0.8982018087470489 + x24)^2) + x751 * ((-0.3125245397681232 + x22)^2 + (
    -0.25776762798299757 + x23)^2 + (-0.05720177574934948 + x24)^2) + x752 * ((
    -0.3197520940611892 + x22)^2 + (-0.8476152339851849 + x23)^2 + (
    -0.36763530621177176 + x24)^2) + x753 * ((-0.7452568897412712 + x22)^2 + (
    -0.24553180487125725 + x23)^2 + (-0.5097535241044541 + x24)^2) + x754 * ((
    -0.7098335381446684 + x22)^2 + (-0.8340974705497336 + x23)^2 + (
    -0.181763781584372 + x24)^2) + x755 * ((-0.46361936352247957 + x22)^2 + (
    -0.5052840929896205 + x23)^2 + (-0.44590180298842885 + x24)^2) + x756 * ((
    -0.38556721731694843 + x22)^2 + (-0.8579051939296445 + x23)^2 + (
    -0.9532247922542321 + x24)^2) + x757 * ((-0.08582521461459391 + x22)^2 + (
    -0.1846731910506113 + x23)^2 + (-0.8745914265553065 + x24)^2) + x758 * ((
    -0.8832914121602843 + x22)^2 + (-0.6513632907999211 + x23)^2 + (
    -0.21823458079012226 + x24)^2) + x759 * ((-0.5751096041706857 + x22)^2 + (
    -0.67547809352205 + x23)^2 + (-0.02460221547003949 + x24)^2) + x760 * ((
    -0.31457012214576896 + x22)^2 + (-0.6742238394444281 + x23)^2 + (
    -0.5445193883971214 + x24)^2) + x761 * ((-0.11915949121286373 + x22)^2 + (
    -0.7063249001765594 + x23)^2 + (-0.2705862773526916 + x24)^2) + x762 * ((
    -0.6669226676581618 + x22)^2 + (-0.5285881831609426 + x23)^2 + (
    -0.11309761756326353 + x24)^2) + x763 * ((-0.12347539452476952 + x22)^2 + (
    -0.39576104678223545 + x23)^2 + (-0.5346277380867844 + x24)^2) + x764 * ((
    -0.6078285274199232 + x22)^2 + (-0.14297039718498794 + x23)^2 + (
    -0.9770203015468777 + x24)^2) + x765 * ((-0.3646785363094529 + x22)^2 + (
    -0.7442303679522239 + x23)^2 + (-0.6078205952200681 + x24)^2) + x766 * ((
    -0.5210217205095699 + x22)^2 + (-0.8432559359514145 + x23)^2 + (
    -0.22452982644506148 + x24)^2) + x767 * ((-0.08751493934711652 + x22)^2 + (
    -0.4416120245181858 + x23)^2 + (-0.026527914551422116 + x24)^2) + x768 * ((
    -0.01197633335476489 + x22)^2 + (-0.2890291018825958 + x23)^2 + (
    -0.38681268974270067 + x24)^2) + x769 * ((-0.7095057303156089 + x22)^2 + (
    -0.931861745530449 + x23)^2 + (-0.14043671018799309 + x24)^2) + x770 * ((
    -0.0895696243176286 + x22)^2 + (-0.5380623897726036 + x23)^2 + (
    -0.21800740949887965 + x24)^2) + x771 * ((-0.7815676711928884 + x22)^2 + (
    -0.018922864242984283 + x23)^2 + (-0.28596537520912735 + x24)^2) + x772 * (
    (-0.1740875221968632 + x22)^2 + (-0.5678042483964806 + x23)^2 + (
    -0.5661715765543827 + x24)^2) + x773 * ((-0.026589535186742008 + x22)^2 + (
    -0.764188329062881 + x23)^2 + (-0.573675168853155 + x24)^2) + x774 * ((
    -0.369798170078249 + x22)^2 + (-0.9415339432121399 + x23)^2 + (
    -0.6729904295003972 + x24)^2) + x775 * ((-0.8040803150564447 + x22)^2 + (
    -0.1553864280131183 + x23)^2 + (-0.8148818001526622 + x24)^2) + x776 * ((
    -0.26589528353030667 + x22)^2 + (-0.3666027540410405 + x23)^2 + (
    -0.468491747882274 + x24)^2) + x777 * ((-0.7258236750794794 + x22)^2 + (
    -0.6727872398248785 + x23)^2 + (-0.28367538142810256 + x24)^2) + x778 * ((
    -0.9220733933477209 + x22)^2 + (-0.26257553387761134 + x23)^2 + (
    -0.7191645521015703 + x24)^2) + x779 * ((-0.9500341346045207 + x22)^2 + (
    -0.638006708190589 + x23)^2 + (-0.07543033185744508 + x24)^2) + x780 * ((
    -0.10545996998960727 + x22)^2 + (-0.7011113856167448 + x23)^2 + (
    -0.20681983539603999 + x24)^2) + x781 * ((-0.6551186918756842 + x22)^2 + (
    -0.6398068804459004 + x23)^2 + (-0.9931175421141764 + x24)^2) + x782 * ((
    -0.7142120519447257 + x22)^2 + (-0.46243457004259436 + x23)^2 + (
    -0.5481708822495015 + x24)^2) + x783 * ((-0.4950904200820069 + x22)^2 + (
    -0.897797250865998 + x23)^2 + (-0.2346789175833377 + x24)^2) + x784 * ((
    -0.6440952365033279 + x22)^2 + (-0.33381998176403327 + x23)^2 + (
    -0.5869170180027279 + x24)^2) + x785 * ((-0.8591109395866232 + x22)^2 + (
    -0.8400580742862248 + x23)^2 + (-0.7678032609886081 + x24)^2) + x786 * ((
    -0.7791674853861603 + x22)^2 + (-0.45754256977454044 + x23)^2 + (
    -0.30909012057666696 + x24)^2) + x787 * ((-0.8968075661486302 + x22)^2 + (
    -0.34892321725590947 + x23)^2 + (-0.05826567448243425 + x24)^2) + x788 * ((
    -0.3189815847959586 + x22)^2 + (-0.3926628302556219 + x23)^2 + (
    -0.07205292941157881 + x24)^2) + x789 * ((-0.8146221960807916 + x22)^2 + (
    -0.4969763360408802 + x23)^2 + (-0.3647398823672149 + x24)^2) + x790 * ((
    -0.23899160200316316 + x22)^2 + (-0.39386695871622013 + x23)^2 + (
    -0.6832280563167916 + x24)^2) + x791 * ((-0.3505164112410739 + x22)^2 + (
    -0.474289602074489 + x23)^2 + (-0.09409181759710883 + x24)^2) + x792 * ((
    -0.9669824450132469 + x22)^2 + (-0.7209255968341481 + x23)^2 + (
    -0.013074465617943565 + x24)^2) + x793 * ((-0.7769547473829561 + x22)^2 + (
    -0.8065173816239941 + x23)^2 + (-0.7160376893035372 + x24)^2) + x794 * ((
    -0.3489895458178166 + x22)^2 + (-0.35733085724791824 + x23)^2 + (
    -0.8864875891533408 + x24)^2) + x795 * ((-0.0664995679925865 + x22)^2 + (
    -0.7243483038068983 + x23)^2 + (-0.9303195285204333 + x24)^2) + x796 * ((
    -0.8115323501210528 + x22)^2 + (-0.42672295637197755 + x23)^2 + (
    -0.04261529652953755 + x24)^2) + x797 * ((-0.3704618379844066 + x22)^2 + (
    -0.1443368240568217 + x23)^2 + (-0.3776192402141899 + x24)^2) + x798 * ((
    -0.7280090144638749 + x22)^2 + (-0.15636110839409045 + x23)^2 + (
    -0.46978018596620896 + x24)^2) + x799 * ((-0.11088006780742277 + x22)^2 + (
    -0.34039206766760943 + x23)^2 + (-0.06827700620696797 + x24)^2) + x800 * ((
    -0.6997602128647453 + x22)^2 + (-0.43764462531136417 + x23)^2 + (
    -0.21027262835312888 + x24)^2) + x801 * ((-0.04425963668315558 + x22)^2 + (
    -0.05866963958501248 + x23)^2 + (-0.3542816901635206 + x24)^2) + x802 * ((
    -0.9757731519147661 + x22)^2 + (-0.3254673022536907 + x23)^2 + (
    -0.6814338527690927 + x24)^2) + x803 * ((-0.7472668303106704 + x22)^2 + (
    -0.0007097732419126812 + x23)^2 + (-0.9280520527234516 + x24)^2) + x804 * (
    (-0.5322530736526498 + x22)^2 + (-0.39754547356694514 + x23)^2 + (
    -0.13635594663989958 + x24)^2) + x805 * ((-0.0007978441992585461 + x22)^2
    + (-0.8844692811473446 + x23)^2 + (-0.1467696053297397 + x24)^2) + x806 *
    ((-0.482850676866177 + x22)^2 + (-0.10574453600064249 + x23)^2 + (
    -0.8791132223988765 + x24)^2) + x807 * ((-0.7291125910415815 + x22)^2 + (
    -0.2090180996227905 + x23)^2 + (-0.5040401706411071 + x24)^2) + x808 * ((
    -0.6406085128291104 + x22)^2 + (-0.11496605173886654 + x23)^2 + (
    -0.7597217863145667 + x24)^2) + x809 * ((-0.6527145527530681 + x22)^2 + (
    -0.09871984518132071 + x23)^2 + (-0.08020459573270278 + x24)^2) + x810 * ((
    -0.5779788427476141 + x22)^2 + (-0.6106348650543917 + x23)^2 + (
    -0.21791347819398965 + x24)^2) + x811 * ((-0.894563747191656 + x22)^2 + (
    -0.49991063769677824 + x23)^2 + (-0.8312284742613548 + x24)^2) + x812 * ((
    -0.5477983688744066 + x22)^2 + (-0.10123589526888899 + x23)^2 + (
    -0.9724165689826183 + x24)^2) + x813 * ((-0.7051711697372745 + x22)^2 + (
    -0.6974870695940615 + x23)^2 + (-0.34185115432121194 + x24)^2) + x814 * ((
    -0.965288766829392 + x22)^2 + (-0.3541459265683641 + x23)^2 + (
    -0.5256833284803955 + x24)^2) + x815 * ((-0.486217312364274 + x22)^2 + (
    -0.877880388733161 + x23)^2 + (-0.7007637309302288 + x24)^2) + x816 * ((
    -0.9239018568218517 + x22)^2 + (-0.8696579903239924 + x23)^2 + (
    -0.9905428630635226 + x24)^2) + x817 * ((-0.5635239214739318 + x22)^2 + (
    -0.5212076565782671 + x23)^2 + (-0.672320998946101 + x24)^2) + x818 * ((
    -0.6336849702734496 + x22)^2 + (-0.17934198400132562 + x23)^2 + (
    -0.25720032541892046 + x24)^2) + x819 * ((-0.3593028476464476 + x22)^2 + (
    -0.7339808423425379 + x23)^2 + (-0.001964432484070411 + x24)^2) + x820 * ((
    -0.11194390371791885 + x22)^2 + (-0.05379441414468389 + x23)^2 + (
    -0.943183016792168 + x24)^2) + x821 * ((-0.23043169327406487 + x22)^2 + (
    -0.9554781274626842 + x23)^2 + (-0.7782415771343315 + x24)^2) + x822 * ((
    -0.999963313244285 + x22)^2 + (-0.18638094695235063 + x23)^2 + (
    -0.8044007834975228 + x24)^2) + x823 * ((-0.8484168552839887 + x22)^2 + (
    -0.5800377498791588 + x23)^2 + (-0.5020163714056717 + x24)^2) + x824 * ((
    -0.43417113739871793 + x22)^2 + (-0.12296667128824068 + x23)^2 + (
    -0.9424473212335941 + x24)^2))

@constraint(m, e1, x25 + x125 + x225 + x325 + x425 + x525 + x625 + x725 == 1)
@constraint(m, e2, x26 + x126 + x226 + x326 + x426 + x526 + x626 + x726 == 1)
@constraint(m, e3, x27 + x127 + x227 + x327 + x427 + x527 + x627 + x727 == 1)
@constraint(m, e4, x28 + x128 + x228 + x328 + x428 + x528 + x628 + x728 == 1)
@constraint(m, e5, x29 + x129 + x229 + x329 + x429 + x529 + x629 + x729 == 1)
@constraint(m, e6, x30 + x130 + x230 + x330 + x430 + x530 + x630 + x730 == 1)
@constraint(m, e7, x31 + x131 + x231 + x331 + x431 + x531 + x631 + x731 == 1)
@constraint(m, e8, x32 + x132 + x232 + x332 + x432 + x532 + x632 + x732 == 1)
@constraint(m, e9, x33 + x133 + x233 + x333 + x433 + x533 + x633 + x733 == 1)
@constraint(m, e10, x34 + x134 + x234 + x334 + x434 + x534 + x634 + x734 == 1)
@constraint(m, e11, x35 + x135 + x235 + x335 + x435 + x535 + x635 + x735 == 1)
@constraint(m, e12, x36 + x136 + x236 + x336 + x436 + x536 + x636 + x736 == 1)
@constraint(m, e13, x37 + x137 + x237 + x337 + x437 + x537 + x637 + x737 == 1)
@constraint(m, e14, x38 + x138 + x238 + x338 + x438 + x538 + x638 + x738 == 1)
@constraint(m, e15, x39 + x139 + x239 + x339 + x439 + x539 + x639 + x739 == 1)
@constraint(m, e16, x40 + x140 + x240 + x340 + x440 + x540 + x640 + x740 == 1)
@constraint(m, e17, x41 + x141 + x241 + x341 + x441 + x541 + x641 + x741 == 1)
@constraint(m, e18, x42 + x142 + x242 + x342 + x442 + x542 + x642 + x742 == 1)
@constraint(m, e19, x43 + x143 + x243 + x343 + x443 + x543 + x643 + x743 == 1)
@constraint(m, e20, x44 + x144 + x244 + x344 + x444 + x544 + x644 + x744 == 1)
@constraint(m, e21, x45 + x145 + x245 + x345 + x445 + x545 + x645 + x745 == 1)
@constraint(m, e22, x46 + x146 + x246 + x346 + x446 + x546 + x646 + x746 == 1)
@constraint(m, e23, x47 + x147 + x247 + x347 + x447 + x547 + x647 + x747 == 1)
@constraint(m, e24, x48 + x148 + x248 + x348 + x448 + x548 + x648 + x748 == 1)
@constraint(m, e25, x49 + x149 + x249 + x349 + x449 + x549 + x649 + x749 == 1)
@constraint(m, e26, x50 + x150 + x250 + x350 + x450 + x550 + x650 + x750 == 1)
@constraint(m, e27, x51 + x151 + x251 + x351 + x451 + x551 + x651 + x751 == 1)
@constraint(m, e28, x52 + x152 + x252 + x352 + x452 + x552 + x652 + x752 == 1)
@constraint(m, e29, x53 + x153 + x253 + x353 + x453 + x553 + x653 + x753 == 1)
@constraint(m, e30, x54 + x154 + x254 + x354 + x454 + x554 + x654 + x754 == 1)
@constraint(m, e31, x55 + x155 + x255 + x355 + x455 + x555 + x655 + x755 == 1)
@constraint(m, e32, x56 + x156 + x256 + x356 + x456 + x556 + x656 + x756 == 1)
@constraint(m, e33, x57 + x157 + x257 + x357 + x457 + x557 + x657 + x757 == 1)
@constraint(m, e34, x58 + x158 + x258 + x358 + x458 + x558 + x658 + x758 == 1)
@constraint(m, e35, x59 + x159 + x259 + x359 + x459 + x559 + x659 + x759 == 1)
@constraint(m, e36, x60 + x160 + x260 + x360 + x460 + x560 + x660 + x760 == 1)
@constraint(m, e37, x61 + x161 + x261 + x361 + x461 + x561 + x661 + x761 == 1)
@constraint(m, e38, x62 + x162 + x262 + x362 + x462 + x562 + x662 + x762 == 1)
@constraint(m, e39, x63 + x163 + x263 + x363 + x463 + x563 + x663 + x763 == 1)
@constraint(m, e40, x64 + x164 + x264 + x364 + x464 + x564 + x664 + x764 == 1)
@constraint(m, e41, x65 + x165 + x265 + x365 + x465 + x565 + x665 + x765 == 1)
@constraint(m, e42, x66 + x166 + x266 + x366 + x466 + x566 + x666 + x766 == 1)
@constraint(m, e43, x67 + x167 + x267 + x367 + x467 + x567 + x667 + x767 == 1)
@constraint(m, e44, x68 + x168 + x268 + x368 + x468 + x568 + x668 + x768 == 1)
@constraint(m, e45, x69 + x169 + x269 + x369 + x469 + x569 + x669 + x769 == 1)
@constraint(m, e46, x70 + x170 + x270 + x370 + x470 + x570 + x670 + x770 == 1)
@constraint(m, e47, x71 + x171 + x271 + x371 + x471 + x571 + x671 + x771 == 1)
@constraint(m, e48, x72 + x172 + x272 + x372 + x472 + x572 + x672 + x772 == 1)
@constraint(m, e49, x73 + x173 + x273 + x373 + x473 + x573 + x673 + x773 == 1)
@constraint(m, e50, x74 + x174 + x274 + x374 + x474 + x574 + x674 + x774 == 1)
@constraint(m, e51, x75 + x175 + x275 + x375 + x475 + x575 + x675 + x775 == 1)
@constraint(m, e52, x76 + x176 + x276 + x376 + x476 + x576 + x676 + x776 == 1)
@constraint(m, e53, x77 + x177 + x277 + x377 + x477 + x577 + x677 + x777 == 1)
@constraint(m, e54, x78 + x178 + x278 + x378 + x478 + x578 + x678 + x778 == 1)
@constraint(m, e55, x79 + x179 + x279 + x379 + x479 + x579 + x679 + x779 == 1)
@constraint(m, e56, x80 + x180 + x280 + x380 + x480 + x580 + x680 + x780 == 1)
@constraint(m, e57, x81 + x181 + x281 + x381 + x481 + x581 + x681 + x781 == 1)
@constraint(m, e58, x82 + x182 + x282 + x382 + x482 + x582 + x682 + x782 == 1)
@constraint(m, e59, x83 + x183 + x283 + x383 + x483 + x583 + x683 + x783 == 1)
@constraint(m, e60, x84 + x184 + x284 + x384 + x484 + x584 + x684 + x784 == 1)
@constraint(m, e61, x85 + x185 + x285 + x385 + x485 + x585 + x685 + x785 == 1)
@constraint(m, e62, x86 + x186 + x286 + x386 + x486 + x586 + x686 + x786 == 1)
@constraint(m, e63, x87 + x187 + x287 + x387 + x487 + x587 + x687 + x787 == 1)
@constraint(m, e64, x88 + x188 + x288 + x388 + x488 + x588 + x688 + x788 == 1)
@constraint(m, e65, x89 + x189 + x289 + x389 + x489 + x589 + x689 + x789 == 1)
@constraint(m, e66, x90 + x190 + x290 + x390 + x490 + x590 + x690 + x790 == 1)
@constraint(m, e67, x91 + x191 + x291 + x391 + x491 + x591 + x691 + x791 == 1)
@constraint(m, e68, x92 + x192 + x292 + x392 + x492 + x592 + x692 + x792 == 1)
@constraint(m, e69, x93 + x193 + x293 + x393 + x493 + x593 + x693 + x793 == 1)
@constraint(m, e70, x94 + x194 + x294 + x394 + x494 + x594 + x694 + x794 == 1)
@constraint(m, e71, x95 + x195 + x295 + x395 + x495 + x595 + x695 + x795 == 1)
@constraint(m, e72, x96 + x196 + x296 + x396 + x496 + x596 + x696 + x796 == 1)
@constraint(m, e73, x97 + x197 + x297 + x397 + x497 + x597 + x697 + x797 == 1)
@constraint(m, e74, x98 + x198 + x298 + x398 + x498 + x598 + x698 + x798 == 1)
@constraint(m, e75, x99 + x199 + x299 + x399 + x499 + x599 + x699 + x799 == 1)
@constraint(m, e76, x100 + x200 + x300 + x400 + x500 + x600 + x700 + x800 == 1)
@constraint(m, e77, x101 + x201 + x301 + x401 + x501 + x601 + x701 + x801 == 1)
@constraint(m, e78, x102 + x202 + x302 + x402 + x502 + x602 + x702 + x802 == 1)
@constraint(m, e79, x103 + x203 + x303 + x403 + x503 + x603 + x703 + x803 == 1)
@constraint(m, e80, x104 + x204 + x304 + x404 + x504 + x604 + x704 + x804 == 1)
@constraint(m, e81, x105 + x205 + x305 + x405 + x505 + x605 + x705 + x805 == 1)
@constraint(m, e82, x106 + x206 + x306 + x406 + x506 + x606 + x706 + x806 == 1)
@constraint(m, e83, x107 + x207 + x307 + x407 + x507 + x607 + x707 + x807 == 1)
@constraint(m, e84, x108 + x208 + x308 + x408 + x508 + x608 + x708 + x808 == 1)
@constraint(m, e85, x109 + x209 + x309 + x409 + x509 + x609 + x709 + x809 == 1)
@constraint(m, e86, x110 + x210 + x310 + x410 + x510 + x610 + x710 + x810 == 1)
@constraint(m, e87, x111 + x211 + x311 + x411 + x511 + x611 + x711 + x811 == 1)
@constraint(m, e88, x112 + x212 + x312 + x412 + x512 + x612 + x712 + x812 == 1)
@constraint(m, e89, x113 + x213 + x313 + x413 + x513 + x613 + x713 + x813 == 1)
@constraint(m, e90, x114 + x214 + x314 + x414 + x514 + x614 + x714 + x814 == 1)
@constraint(m, e91, x115 + x215 + x315 + x415 + x515 + x615 + x715 + x815 == 1)
@constraint(m, e92, x116 + x216 + x316 + x416 + x516 + x616 + x716 + x816 == 1)
@constraint(m, e93, x117 + x217 + x317 + x417 + x517 + x617 + x717 + x817 == 1)
@constraint(m, e94, x118 + x218 + x318 + x418 + x518 + x618 + x718 + x818 == 1)
@constraint(m, e95, x119 + x219 + x319 + x419 + x519 + x619 + x719 + x819 == 1)
@constraint(m, e96, x120 + x220 + x320 + x420 + x520 + x620 + x720 + x820 == 1)
@constraint(m, e97, x121 + x221 + x321 + x421 + x521 + x621 + x721 + x821 == 1)
@constraint(m, e98, x122 + x222 + x322 + x422 + x522 + x622 + x722 + x822 == 1)
@constraint(m, e99, x123 + x223 + x323 + x423 + x523 + x623 + x723 + x823 == 1)
@constraint(m, e100, x124 + x224 + x324 + x424 + x524 + x624 + x724 + x824
    == 1)
