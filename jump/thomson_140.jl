# NLP written by GAMS Convert at 05/15/24 11:31:56
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       140      140        0        0        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#       420      420        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       420        0      420
#
# Reformulation has removed 1 variable and 1 equation

using JuMP
using MathOptInterface
const MOI = MathOptInterface

model = m = Model()

@variable(m, -1 <= x1 <= 1, start=0)
@variable(m, -1 <= x2 <= 1, start=0)
@variable(m, -1 <= x3 <= 1, start=0)
@variable(m, -1 <= x4 <= 1, start=0)
@variable(m, -1 <= x5 <= 1, start=0)
@variable(m, -1 <= x6 <= 1, start=0)
@variable(m, -1 <= x7 <= 1, start=0)
@variable(m, -1 <= x8 <= 1, start=0)
@variable(m, -1 <= x9 <= 1, start=0)
@variable(m, -1 <= x10 <= 1, start=0)
@variable(m, -1 <= x11 <= 1, start=0)
@variable(m, -1 <= x12 <= 1, start=0)
@variable(m, -1 <= x13 <= 1, start=0)
@variable(m, -1 <= x14 <= 1, start=0)
@variable(m, -1 <= x15 <= 1, start=0)
@variable(m, -1 <= x16 <= 1, start=0)
@variable(m, -1 <= x17 <= 1, start=0)
@variable(m, -1 <= x18 <= 1, start=0)
@variable(m, -1 <= x19 <= 1, start=0)
@variable(m, -1 <= x20 <= 1, start=0)
@variable(m, -1 <= x21 <= 1, start=0)
@variable(m, -1 <= x22 <= 1, start=0)
@variable(m, -1 <= x23 <= 1, start=0)
@variable(m, -1 <= x24 <= 1, start=0)
@variable(m, -1 <= x25 <= 1, start=0)
@variable(m, -1 <= x26 <= 1, start=0)
@variable(m, -1 <= x27 <= 1, start=0)
@variable(m, -1 <= x28 <= 1, start=0)
@variable(m, -1 <= x29 <= 1, start=0)
@variable(m, -1 <= x30 <= 1, start=0)
@variable(m, -1 <= x31 <= 1, start=0)
@variable(m, -1 <= x32 <= 1, start=0)
@variable(m, -1 <= x33 <= 1, start=0)
@variable(m, -1 <= x34 <= 1, start=0)
@variable(m, -1 <= x35 <= 1, start=0)
@variable(m, -1 <= x36 <= 1, start=0)
@variable(m, -1 <= x37 <= 1, start=0)
@variable(m, -1 <= x38 <= 1, start=0)
@variable(m, -1 <= x39 <= 1, start=0)
@variable(m, -1 <= x40 <= 1, start=0)
@variable(m, -1 <= x41 <= 1, start=0)
@variable(m, -1 <= x42 <= 1, start=0)
@variable(m, -1 <= x43 <= 1, start=0)
@variable(m, -1 <= x44 <= 1, start=0)
@variable(m, -1 <= x45 <= 1, start=0)
@variable(m, -1 <= x46 <= 1, start=0)
@variable(m, -1 <= x47 <= 1, start=0)
@variable(m, -1 <= x48 <= 1, start=0)
@variable(m, -1 <= x49 <= 1, start=0)
@variable(m, -1 <= x50 <= 1, start=0)
@variable(m, -1 <= x51 <= 1, start=0)
@variable(m, -1 <= x52 <= 1, start=0)
@variable(m, -1 <= x53 <= 1, start=0)
@variable(m, -1 <= x54 <= 1, start=0)
@variable(m, -1 <= x55 <= 1, start=0)
@variable(m, -1 <= x56 <= 1, start=0)
@variable(m, -1 <= x57 <= 1, start=0)
@variable(m, -1 <= x58 <= 1, start=0)
@variable(m, -1 <= x59 <= 1, start=0)
@variable(m, -1 <= x60 <= 1, start=0)
@variable(m, -1 <= x61 <= 1, start=0)
@variable(m, -1 <= x62 <= 1, start=0)
@variable(m, -1 <= x63 <= 1, start=0)
@variable(m, -1 <= x64 <= 1, start=0)
@variable(m, -1 <= x65 <= 1, start=0)
@variable(m, -1 <= x66 <= 1, start=0)
@variable(m, -1 <= x67 <= 1, start=0)
@variable(m, -1 <= x68 <= 1, start=0)
@variable(m, -1 <= x69 <= 1, start=0)
@variable(m, -1 <= x70 <= 1, start=0)
@variable(m, -1 <= x71 <= 1, start=0)
@variable(m, -1 <= x72 <= 1, start=0)
@variable(m, -1 <= x73 <= 1, start=0)
@variable(m, -1 <= x74 <= 1, start=0)
@variable(m, -1 <= x75 <= 1, start=0)
@variable(m, -1 <= x76 <= 1, start=0)
@variable(m, -1 <= x77 <= 1, start=0)
@variable(m, -1 <= x78 <= 1, start=0)
@variable(m, -1 <= x79 <= 1, start=0)
@variable(m, -1 <= x80 <= 1, start=0)
@variable(m, -1 <= x81 <= 1, start=0)
@variable(m, -1 <= x82 <= 1, start=0)
@variable(m, -1 <= x83 <= 1, start=0)
@variable(m, -1 <= x84 <= 1, start=0)
@variable(m, -1 <= x85 <= 1, start=0)
@variable(m, -1 <= x86 <= 1, start=0)
@variable(m, -1 <= x87 <= 1, start=0)
@variable(m, -1 <= x88 <= 1, start=0)
@variable(m, -1 <= x89 <= 1, start=0)
@variable(m, -1 <= x90 <= 1, start=0)
@variable(m, -1 <= x91 <= 1, start=0)
@variable(m, -1 <= x92 <= 1, start=0)
@variable(m, -1 <= x93 <= 1, start=0)
@variable(m, -1 <= x94 <= 1, start=0)
@variable(m, -1 <= x95 <= 1, start=0)
@variable(m, -1 <= x96 <= 1, start=0)
@variable(m, -1 <= x97 <= 1, start=0)
@variable(m, -1 <= x98 <= 1, start=0)
@variable(m, -1 <= x99 <= 1, start=0)
@variable(m, -1 <= x100 <= 1, start=0)
@variable(m, -1 <= x101 <= 1, start=0)
@variable(m, -1 <= x102 <= 1, start=0)
@variable(m, -1 <= x103 <= 1, start=0)
@variable(m, -1 <= x104 <= 1, start=0)
@variable(m, -1 <= x105 <= 1, start=0)
@variable(m, -1 <= x106 <= 1, start=0)
@variable(m, -1 <= x107 <= 1, start=0)
@variable(m, -1 <= x108 <= 1, start=0)
@variable(m, -1 <= x109 <= 1, start=0)
@variable(m, -1 <= x110 <= 1, start=0)
@variable(m, -1 <= x111 <= 1, start=0)
@variable(m, -1 <= x112 <= 1, start=0)
@variable(m, -1 <= x113 <= 1, start=0)
@variable(m, -1 <= x114 <= 1, start=0)
@variable(m, -1 <= x115 <= 1, start=0)
@variable(m, -1 <= x116 <= 1, start=0)
@variable(m, -1 <= x117 <= 1, start=0)
@variable(m, -1 <= x118 <= 1, start=0)
@variable(m, -1 <= x119 <= 1, start=0)
@variable(m, -1 <= x120 <= 1, start=0)
@variable(m, -1 <= x121 <= 1, start=0)
@variable(m, -1 <= x122 <= 1, start=0)
@variable(m, -1 <= x123 <= 1, start=0)
@variable(m, -1 <= x124 <= 1, start=0)
@variable(m, -1 <= x125 <= 1, start=0)
@variable(m, -1 <= x126 <= 1, start=0)
@variable(m, -1 <= x127 <= 1, start=0)
@variable(m, -1 <= x128 <= 1, start=0)
@variable(m, -1 <= x129 <= 1, start=0)
@variable(m, -1 <= x130 <= 1, start=0)
@variable(m, -1 <= x131 <= 1, start=0)
@variable(m, -1 <= x132 <= 1, start=0)
@variable(m, -1 <= x133 <= 1, start=0)
@variable(m, -1 <= x134 <= 1, start=0)
@variable(m, -1 <= x135 <= 1, start=0)
@variable(m, -1 <= x136 <= 1, start=0)
@variable(m, -1 <= x137 <= 1, start=0)
@variable(m, -1 <= x138 <= 1, start=0)
@variable(m, -1 <= x139 <= 1, start=0)
@variable(m, -1 <= x140 <= 1, start=0)
@variable(m, -1 <= x141 <= 1, start=0)
@variable(m, -1 <= x142 <= 1, start=0)
@variable(m, -1 <= x143 <= 1, start=0)
@variable(m, -1 <= x144 <= 1, start=0)
@variable(m, -1 <= x145 <= 1, start=0)
@variable(m, -1 <= x146 <= 1, start=0)
@variable(m, -1 <= x147 <= 1, start=0)
@variable(m, -1 <= x148 <= 1, start=0)
@variable(m, -1 <= x149 <= 1, start=0)
@variable(m, -1 <= x150 <= 1, start=0)
@variable(m, -1 <= x151 <= 1, start=0)
@variable(m, -1 <= x152 <= 1, start=0)
@variable(m, -1 <= x153 <= 1, start=0)
@variable(m, -1 <= x154 <= 1, start=0)
@variable(m, -1 <= x155 <= 1, start=0)
@variable(m, -1 <= x156 <= 1, start=0)
@variable(m, -1 <= x157 <= 1, start=0)
@variable(m, -1 <= x158 <= 1, start=0)
@variable(m, -1 <= x159 <= 1, start=0)
@variable(m, -1 <= x160 <= 1, start=0)
@variable(m, -1 <= x161 <= 1, start=0)
@variable(m, -1 <= x162 <= 1, start=0)
@variable(m, -1 <= x163 <= 1, start=0)
@variable(m, -1 <= x164 <= 1, start=0)
@variable(m, -1 <= x165 <= 1, start=0)
@variable(m, -1 <= x166 <= 1, start=0)
@variable(m, -1 <= x167 <= 1, start=0)
@variable(m, -1 <= x168 <= 1, start=0)
@variable(m, -1 <= x169 <= 1, start=0)
@variable(m, -1 <= x170 <= 1, start=0)
@variable(m, -1 <= x171 <= 1, start=0)
@variable(m, -1 <= x172 <= 1, start=0)
@variable(m, -1 <= x173 <= 1, start=0)
@variable(m, -1 <= x174 <= 1, start=0)
@variable(m, -1 <= x175 <= 1, start=0)
@variable(m, -1 <= x176 <= 1, start=0)
@variable(m, -1 <= x177 <= 1, start=0)
@variable(m, -1 <= x178 <= 1, start=0)
@variable(m, -1 <= x179 <= 1, start=0)
@variable(m, -1 <= x180 <= 1, start=0)
@variable(m, -1 <= x181 <= 1, start=0)
@variable(m, -1 <= x182 <= 1, start=0)
@variable(m, -1 <= x183 <= 1, start=0)
@variable(m, -1 <= x184 <= 1, start=0)
@variable(m, -1 <= x185 <= 1, start=0)
@variable(m, -1 <= x186 <= 1, start=0)
@variable(m, -1 <= x187 <= 1, start=0)
@variable(m, -1 <= x188 <= 1, start=0)
@variable(m, -1 <= x189 <= 1, start=0)
@variable(m, -1 <= x190 <= 1, start=0)
@variable(m, -1 <= x191 <= 1, start=0)
@variable(m, -1 <= x192 <= 1, start=0)
@variable(m, -1 <= x193 <= 1, start=0)
@variable(m, -1 <= x194 <= 1, start=0)
@variable(m, -1 <= x195 <= 1, start=0)
@variable(m, -1 <= x196 <= 1, start=0)
@variable(m, -1 <= x197 <= 1, start=0)
@variable(m, -1 <= x198 <= 1, start=0)
@variable(m, -1 <= x199 <= 1, start=0)
@variable(m, -1 <= x200 <= 1, start=0)
@variable(m, -1 <= x201 <= 1, start=0)
@variable(m, -1 <= x202 <= 1, start=0)
@variable(m, -1 <= x203 <= 1, start=0)
@variable(m, -1 <= x204 <= 1, start=0)
@variable(m, -1 <= x205 <= 1, start=0)
@variable(m, -1 <= x206 <= 1, start=0)
@variable(m, -1 <= x207 <= 1, start=0)
@variable(m, -1 <= x208 <= 1, start=0)
@variable(m, -1 <= x209 <= 1, start=0)
@variable(m, -1 <= x210 <= 1, start=0)
@variable(m, -1 <= x211 <= 1, start=0)
@variable(m, -1 <= x212 <= 1, start=0)
@variable(m, -1 <= x213 <= 1, start=0)
@variable(m, -1 <= x214 <= 1, start=0)
@variable(m, -1 <= x215 <= 1, start=0)
@variable(m, -1 <= x216 <= 1, start=0)
@variable(m, -1 <= x217 <= 1, start=0)
@variable(m, -1 <= x218 <= 1, start=0)
@variable(m, -1 <= x219 <= 1, start=0)
@variable(m, -1 <= x220 <= 1, start=0)
@variable(m, -1 <= x221 <= 1, start=0)
@variable(m, -1 <= x222 <= 1, start=0)
@variable(m, -1 <= x223 <= 1, start=0)
@variable(m, -1 <= x224 <= 1, start=0)
@variable(m, -1 <= x225 <= 1, start=0)
@variable(m, -1 <= x226 <= 1, start=0)
@variable(m, -1 <= x227 <= 1, start=0)
@variable(m, -1 <= x228 <= 1, start=0)
@variable(m, -1 <= x229 <= 1, start=0)
@variable(m, -1 <= x230 <= 1, start=0)
@variable(m, -1 <= x231 <= 1, start=0)
@variable(m, -1 <= x232 <= 1, start=0)
@variable(m, -1 <= x233 <= 1, start=0)
@variable(m, -1 <= x234 <= 1, start=0)
@variable(m, -1 <= x235 <= 1, start=0)
@variable(m, -1 <= x236 <= 1, start=0)
@variable(m, -1 <= x237 <= 1, start=0)
@variable(m, -1 <= x238 <= 1, start=0)
@variable(m, -1 <= x239 <= 1, start=0)
@variable(m, -1 <= x240 <= 1, start=0)
@variable(m, -1 <= x241 <= 1, start=0)
@variable(m, -1 <= x242 <= 1, start=0)
@variable(m, -1 <= x243 <= 1, start=0)
@variable(m, -1 <= x244 <= 1, start=0)
@variable(m, -1 <= x245 <= 1, start=0)
@variable(m, -1 <= x246 <= 1, start=0)
@variable(m, -1 <= x247 <= 1, start=0)
@variable(m, -1 <= x248 <= 1, start=0)
@variable(m, -1 <= x249 <= 1, start=0)
@variable(m, -1 <= x250 <= 1, start=0)
@variable(m, -1 <= x251 <= 1, start=0)
@variable(m, -1 <= x252 <= 1, start=0)
@variable(m, -1 <= x253 <= 1, start=0)
@variable(m, -1 <= x254 <= 1, start=0)
@variable(m, -1 <= x255 <= 1, start=0)
@variable(m, -1 <= x256 <= 1, start=0)
@variable(m, -1 <= x257 <= 1, start=0)
@variable(m, -1 <= x258 <= 1, start=0)
@variable(m, -1 <= x259 <= 1, start=0)
@variable(m, -1 <= x260 <= 1, start=0)
@variable(m, -1 <= x261 <= 1, start=0)
@variable(m, -1 <= x262 <= 1, start=0)
@variable(m, -1 <= x263 <= 1, start=0)
@variable(m, -1 <= x264 <= 1, start=0)
@variable(m, -1 <= x265 <= 1, start=0)
@variable(m, -1 <= x266 <= 1, start=0)
@variable(m, -1 <= x267 <= 1, start=0)
@variable(m, -1 <= x268 <= 1, start=0)
@variable(m, -1 <= x269 <= 1, start=0)
@variable(m, -1 <= x270 <= 1, start=0)
@variable(m, -1 <= x271 <= 1, start=0)
@variable(m, -1 <= x272 <= 1, start=0)
@variable(m, -1 <= x273 <= 1, start=0)
@variable(m, -1 <= x274 <= 1, start=0)
@variable(m, -1 <= x275 <= 1, start=0)
@variable(m, -1 <= x276 <= 1, start=0)
@variable(m, -1 <= x277 <= 1, start=0)
@variable(m, -1 <= x278 <= 1, start=0)
@variable(m, -1 <= x279 <= 1, start=0)
@variable(m, -1 <= x280 <= 1, start=0)
@variable(m, -1 <= x281 <= 1, start=0)
@variable(m, -1 <= x282 <= 1, start=0)
@variable(m, -1 <= x283 <= 1, start=0)
@variable(m, -1 <= x284 <= 1, start=0)
@variable(m, -1 <= x285 <= 1, start=0)
@variable(m, -1 <= x286 <= 1, start=0)
@variable(m, -1 <= x287 <= 1, start=0)
@variable(m, -1 <= x288 <= 1, start=0)
@variable(m, -1 <= x289 <= 1, start=0)
@variable(m, -1 <= x290 <= 1, start=0)
@variable(m, -1 <= x291 <= 1, start=0)
@variable(m, -1 <= x292 <= 1, start=0)
@variable(m, -1 <= x293 <= 1, start=0)
@variable(m, -1 <= x294 <= 1, start=0)
@variable(m, -1 <= x295 <= 1, start=0)
@variable(m, -1 <= x296 <= 1, start=0)
@variable(m, -1 <= x297 <= 1, start=0)
@variable(m, -1 <= x298 <= 1, start=0)
@variable(m, -1 <= x299 <= 1, start=0)
@variable(m, -1 <= x300 <= 1, start=0)
@variable(m, -1 <= x301 <= 1, start=0)
@variable(m, -1 <= x302 <= 1, start=0)
@variable(m, -1 <= x303 <= 1, start=0)
@variable(m, -1 <= x304 <= 1, start=0)
@variable(m, -1 <= x305 <= 1, start=0)
@variable(m, -1 <= x306 <= 1, start=0)
@variable(m, -1 <= x307 <= 1, start=0)
@variable(m, -1 <= x308 <= 1, start=0)
@variable(m, -1 <= x309 <= 1, start=0)
@variable(m, -1 <= x310 <= 1, start=0)
@variable(m, -1 <= x311 <= 1, start=0)
@variable(m, -1 <= x312 <= 1, start=0)
@variable(m, -1 <= x313 <= 1, start=0)
@variable(m, -1 <= x314 <= 1, start=0)
@variable(m, -1 <= x315 <= 1, start=0)
@variable(m, -1 <= x316 <= 1, start=0)
@variable(m, -1 <= x317 <= 1, start=0)
@variable(m, -1 <= x318 <= 1, start=0)
@variable(m, -1 <= x319 <= 1, start=0)
@variable(m, -1 <= x320 <= 1, start=0)
@variable(m, -1 <= x321 <= 1, start=0)
@variable(m, -1 <= x322 <= 1, start=0)
@variable(m, -1 <= x323 <= 1, start=0)
@variable(m, -1 <= x324 <= 1, start=0)
@variable(m, -1 <= x325 <= 1, start=0)
@variable(m, -1 <= x326 <= 1, start=0)
@variable(m, -1 <= x327 <= 1, start=0)
@variable(m, -1 <= x328 <= 1, start=0)
@variable(m, -1 <= x329 <= 1, start=0)
@variable(m, -1 <= x330 <= 1, start=0)
@variable(m, -1 <= x331 <= 1, start=0)
@variable(m, -1 <= x332 <= 1, start=0)
@variable(m, -1 <= x333 <= 1, start=0)
@variable(m, -1 <= x334 <= 1, start=0)
@variable(m, -1 <= x335 <= 1, start=0)
@variable(m, -1 <= x336 <= 1, start=0)
@variable(m, -1 <= x337 <= 1, start=0)
@variable(m, -1 <= x338 <= 1, start=0)
@variable(m, -1 <= x339 <= 1, start=0)
@variable(m, -1 <= x340 <= 1, start=0)
@variable(m, -1 <= x341 <= 1, start=0)
@variable(m, -1 <= x342 <= 1, start=0)
@variable(m, -1 <= x343 <= 1, start=0)
@variable(m, -1 <= x344 <= 1, start=0)
@variable(m, -1 <= x345 <= 1, start=0)
@variable(m, -1 <= x346 <= 1, start=0)
@variable(m, -1 <= x347 <= 1, start=0)
@variable(m, -1 <= x348 <= 1, start=0)
@variable(m, -1 <= x349 <= 1, start=0)
@variable(m, -1 <= x350 <= 1, start=0)
@variable(m, -1 <= x351 <= 1, start=0)
@variable(m, -1 <= x352 <= 1, start=0)
@variable(m, -1 <= x353 <= 1, start=0)
@variable(m, -1 <= x354 <= 1, start=0)
@variable(m, -1 <= x355 <= 1, start=0)
@variable(m, -1 <= x356 <= 1, start=0)
@variable(m, -1 <= x357 <= 1, start=0)
@variable(m, -1 <= x358 <= 1, start=0)
@variable(m, -1 <= x359 <= 1, start=0)
@variable(m, -1 <= x360 <= 1, start=0)
@variable(m, -1 <= x361 <= 1, start=0)
@variable(m, -1 <= x362 <= 1, start=0)
@variable(m, -1 <= x363 <= 1, start=0)
@variable(m, -1 <= x364 <= 1, start=0)
@variable(m, -1 <= x365 <= 1, start=0)
@variable(m, -1 <= x366 <= 1, start=0)
@variable(m, -1 <= x367 <= 1, start=0)
@variable(m, -1 <= x368 <= 1, start=0)
@variable(m, -1 <= x369 <= 1, start=0)
@variable(m, -1 <= x370 <= 1, start=0)
@variable(m, -1 <= x371 <= 1, start=0)
@variable(m, -1 <= x372 <= 1, start=0)
@variable(m, -1 <= x373 <= 1, start=0)
@variable(m, -1 <= x374 <= 1, start=0)
@variable(m, -1 <= x375 <= 1, start=0)
@variable(m, -1 <= x376 <= 1, start=0)
@variable(m, -1 <= x377 <= 1, start=0)
@variable(m, -1 <= x378 <= 1, start=0)
@variable(m, -1 <= x379 <= 1, start=0)
@variable(m, -1 <= x380 <= 1, start=0)
@variable(m, -1 <= x381 <= 1, start=0)
@variable(m, -1 <= x382 <= 1, start=0)
@variable(m, -1 <= x383 <= 1, start=0)
@variable(m, -1 <= x384 <= 1, start=0)
@variable(m, -1 <= x385 <= 1, start=0)
@variable(m, -1 <= x386 <= 1, start=0)
@variable(m, -1 <= x387 <= 1, start=0)
@variable(m, -1 <= x388 <= 1, start=0)
@variable(m, -1 <= x389 <= 1, start=0)
@variable(m, -1 <= x390 <= 1, start=0)
@variable(m, -1 <= x391 <= 1, start=0)
@variable(m, -1 <= x392 <= 1, start=0)
@variable(m, -1 <= x393 <= 1, start=0)
@variable(m, -1 <= x394 <= 1, start=0)
@variable(m, -1 <= x395 <= 1, start=0)
@variable(m, -1 <= x396 <= 1, start=0)
@variable(m, -1 <= x397 <= 1, start=0)
@variable(m, -1 <= x398 <= 1, start=0)
@variable(m, -1 <= x399 <= 1, start=0)
@variable(m, -1 <= x400 <= 1, start=0)
@variable(m, -1 <= x401 <= 1, start=0)
@variable(m, -1 <= x402 <= 1, start=0)
@variable(m, -1 <= x403 <= 1, start=0)
@variable(m, -1 <= x404 <= 1, start=0)
@variable(m, -1 <= x405 <= 1, start=0)
@variable(m, -1 <= x406 <= 1, start=0)
@variable(m, -1 <= x407 <= 1, start=0)
@variable(m, -1 <= x408 <= 1, start=0)
@variable(m, -1 <= x409 <= 1, start=0)
@variable(m, -1 <= x410 <= 1, start=0)
@variable(m, -1 <= x411 <= 1, start=0)
@variable(m, -1 <= x412 <= 1, start=0)
@variable(m, -1 <= x413 <= 1, start=0)
@variable(m, -1 <= x414 <= 1, start=0)
@variable(m, -1 <= x415 <= 1, start=0)
@variable(m, -1 <= x416 <= 1, start=0)
@variable(m, -1 <= x417 <= 1, start=0)
@variable(m, -1 <= x418 <= 1, start=0)
@variable(m, -1 <= x419 <= 1, start=0)
@variable(m, -1 <= x420 <= 1, start=0)

@NLobjective(m, Min, 1 / sqrt((x1 - x2)^2 + (x141 - x142)^2 + (x281 - x282)^2)
    + 1 / sqrt((x1 - x3)^2 + (x141 - x143)^2 + (x281 - x283)^2) + 1 / sqrt((x1
    - x4)^2 + (x141 - x144)^2 + (x281 - x284)^2) + 1 / sqrt((x1 - x5)^2 + (
    x141 - x145)^2 + (x281 - x285)^2) + 1 / sqrt((x1 - x6)^2 + (x141 - x146)^2
    + (x281 - x286)^2) + 1 / sqrt((x1 - x7)^2 + (x141 - x147)^2 + (x281 - x287)
    ^2) + 1 / sqrt((x1 - x8)^2 + (x141 - x148)^2 + (x281 - x288)^2) + 1 / sqrt(
    (x1 - x9)^2 + (x141 - x149)^2 + (x281 - x289)^2) + 1 / sqrt((x1 - x10)^2 +
    (x141 - x150)^2 + (x281 - x290)^2) + 1 / sqrt((x1 - x11)^2 + (x141 - x151)^
    2 + (x281 - x291)^2) + 1 / sqrt((x1 - x12)^2 + (x141 - x152)^2 + (x281 -
    x292)^2) + 1 / sqrt((x1 - x13)^2 + (x141 - x153)^2 + (x281 - x293)^2) + 1
    / sqrt((x1 - x14)^2 + (x141 - x154)^2 + (x281 - x294)^2) + 1 / sqrt((x1 -
    x15)^2 + (x141 - x155)^2 + (x281 - x295)^2) + 1 / sqrt((x1 - x16)^2 + (x141
    - x156)^2 + (x281 - x296)^2) + 1 / sqrt((x1 - x17)^2 + (x141 - x157)^2 + (
    x281 - x297)^2) + 1 / sqrt((x1 - x18)^2 + (x141 - x158)^2 + (x281 - x298)^2)
    + 1 / sqrt((x1 - x19)^2 + (x141 - x159)^2 + (x281 - x299)^2) + 1 / sqrt((
    x1 - x20)^2 + (x141 - x160)^2 + (x281 - x300)^2) + 1 / sqrt((x1 - x21)^2 +
    (x141 - x161)^2 + (x281 - x301)^2) + 1 / sqrt((x1 - x22)^2 + (x141 - x162)^
    2 + (x281 - x302)^2) + 1 / sqrt((x1 - x23)^2 + (x141 - x163)^2 + (x281 -
    x303)^2) + 1 / sqrt((x1 - x24)^2 + (x141 - x164)^2 + (x281 - x304)^2) + 1
    / sqrt((x1 - x25)^2 + (x141 - x165)^2 + (x281 - x305)^2) + 1 / sqrt((x1 -
    x26)^2 + (x141 - x166)^2 + (x281 - x306)^2) + 1 / sqrt((x1 - x27)^2 + (x141
    - x167)^2 + (x281 - x307)^2) + 1 / sqrt((x1 - x28)^2 + (x141 - x168)^2 + (
    x281 - x308)^2) + 1 / sqrt((x1 - x29)^2 + (x141 - x169)^2 + (x281 - x309)^2)
    + 1 / sqrt((x1 - x30)^2 + (x141 - x170)^2 + (x281 - x310)^2) + 1 / sqrt((
    x1 - x31)^2 + (x141 - x171)^2 + (x281 - x311)^2) + 1 / sqrt((x1 - x32)^2 +
    (x141 - x172)^2 + (x281 - x312)^2) + 1 / sqrt((x1 - x33)^2 + (x141 - x173)^
    2 + (x281 - x313)^2) + 1 / sqrt((x1 - x34)^2 + (x141 - x174)^2 + (x281 -
    x314)^2) + 1 / sqrt((x1 - x35)^2 + (x141 - x175)^2 + (x281 - x315)^2) + 1
    / sqrt((x1 - x36)^2 + (x141 - x176)^2 + (x281 - x316)^2) + 1 / sqrt((x1 -
    x37)^2 + (x141 - x177)^2 + (x281 - x317)^2) + 1 / sqrt((x1 - x38)^2 + (x141
    - x178)^2 + (x281 - x318)^2) + 1 / sqrt((x1 - x39)^2 + (x141 - x179)^2 + (
    x281 - x319)^2) + 1 / sqrt((x1 - x40)^2 + (x141 - x180)^2 + (x281 - x320)^2)
    + 1 / sqrt((x1 - x41)^2 + (x141 - x181)^2 + (x281 - x321)^2) + 1 / sqrt((
    x1 - x42)^2 + (x141 - x182)^2 + (x281 - x322)^2) + 1 / sqrt((x1 - x43)^2 +
    (x141 - x183)^2 + (x281 - x323)^2) + 1 / sqrt((x1 - x44)^2 + (x141 - x184)^
    2 + (x281 - x324)^2) + 1 / sqrt((x1 - x45)^2 + (x141 - x185)^2 + (x281 -
    x325)^2) + 1 / sqrt((x1 - x46)^2 + (x141 - x186)^2 + (x281 - x326)^2) + 1
    / sqrt((x1 - x47)^2 + (x141 - x187)^2 + (x281 - x327)^2) + 1 / sqrt((x1 -
    x48)^2 + (x141 - x188)^2 + (x281 - x328)^2) + 1 / sqrt((x1 - x49)^2 + (x141
    - x189)^2 + (x281 - x329)^2) + 1 / sqrt((x1 - x50)^2 + (x141 - x190)^2 + (
    x281 - x330)^2) + 1 / sqrt((x1 - x51)^2 + (x141 - x191)^2 + (x281 - x331)^2)
    + 1 / sqrt((x1 - x52)^2 + (x141 - x192)^2 + (x281 - x332)^2) + 1 / sqrt((
    x1 - x53)^2 + (x141 - x193)^2 + (x281 - x333)^2) + 1 / sqrt((x1 - x54)^2 +
    (x141 - x194)^2 + (x281 - x334)^2) + 1 / sqrt((x1 - x55)^2 + (x141 - x195)^
    2 + (x281 - x335)^2) + 1 / sqrt((x1 - x56)^2 + (x141 - x196)^2 + (x281 -
    x336)^2) + 1 / sqrt((x1 - x57)^2 + (x141 - x197)^2 + (x281 - x337)^2) + 1
    / sqrt((x1 - x58)^2 + (x141 - x198)^2 + (x281 - x338)^2) + 1 / sqrt((x1 -
    x59)^2 + (x141 - x199)^2 + (x281 - x339)^2) + 1 / sqrt((x1 - x60)^2 + (x141
    - x200)^2 + (x281 - x340)^2) + 1 / sqrt((x1 - x61)^2 + (x141 - x201)^2 + (
    x281 - x341)^2) + 1 / sqrt((x1 - x62)^2 + (x141 - x202)^2 + (x281 - x342)^2)
    + 1 / sqrt((x1 - x63)^2 + (x141 - x203)^2 + (x281 - x343)^2) + 1 / sqrt((
    x1 - x64)^2 + (x141 - x204)^2 + (x281 - x344)^2) + 1 / sqrt((x1 - x65)^2 +
    (x141 - x205)^2 + (x281 - x345)^2) + 1 / sqrt((x1 - x66)^2 + (x141 - x206)^
    2 + (x281 - x346)^2) + 1 / sqrt((x1 - x67)^2 + (x141 - x207)^2 + (x281 -
    x347)^2) + 1 / sqrt((x1 - x68)^2 + (x141 - x208)^2 + (x281 - x348)^2) + 1
    / sqrt((x1 - x69)^2 + (x141 - x209)^2 + (x281 - x349)^2) + 1 / sqrt((x1 -
    x70)^2 + (x141 - x210)^2 + (x281 - x350)^2) + 1 / sqrt((x1 - x71)^2 + (x141
    - x211)^2 + (x281 - x351)^2) + 1 / sqrt((x1 - x72)^2 + (x141 - x212)^2 + (
    x281 - x352)^2) + 1 / sqrt((x1 - x73)^2 + (x141 - x213)^2 + (x281 - x353)^2)
    + 1 / sqrt((x1 - x74)^2 + (x141 - x214)^2 + (x281 - x354)^2) + 1 / sqrt((
    x1 - x75)^2 + (x141 - x215)^2 + (x281 - x355)^2) + 1 / sqrt((x1 - x76)^2 +
    (x141 - x216)^2 + (x281 - x356)^2) + 1 / sqrt((x1 - x77)^2 + (x141 - x217)^
    2 + (x281 - x357)^2) + 1 / sqrt((x1 - x78)^2 + (x141 - x218)^2 + (x281 -
    x358)^2) + 1 / sqrt((x1 - x79)^2 + (x141 - x219)^2 + (x281 - x359)^2) + 1
    / sqrt((x1 - x80)^2 + (x141 - x220)^2 + (x281 - x360)^2) + 1 / sqrt((x1 -
    x81)^2 + (x141 - x221)^2 + (x281 - x361)^2) + 1 / sqrt((x1 - x82)^2 + (x141
    - x222)^2 + (x281 - x362)^2) + 1 / sqrt((x1 - x83)^2 + (x141 - x223)^2 + (
    x281 - x363)^2) + 1 / sqrt((x1 - x84)^2 + (x141 - x224)^2 + (x281 - x364)^2)
    + 1 / sqrt((x1 - x85)^2 + (x141 - x225)^2 + (x281 - x365)^2) + 1 / sqrt((
    x1 - x86)^2 + (x141 - x226)^2 + (x281 - x366)^2) + 1 / sqrt((x1 - x87)^2 +
    (x141 - x227)^2 + (x281 - x367)^2) + 1 / sqrt((x1 - x88)^2 + (x141 - x228)^
    2 + (x281 - x368)^2) + 1 / sqrt((x1 - x89)^2 + (x141 - x229)^2 + (x281 -
    x369)^2) + 1 / sqrt((x1 - x90)^2 + (x141 - x230)^2 + (x281 - x370)^2) + 1
    / sqrt((x1 - x91)^2 + (x141 - x231)^2 + (x281 - x371)^2) + 1 / sqrt((x1 -
    x92)^2 + (x141 - x232)^2 + (x281 - x372)^2) + 1 / sqrt((x1 - x93)^2 + (x141
    - x233)^2 + (x281 - x373)^2) + 1 / sqrt((x1 - x94)^2 + (x141 - x234)^2 + (
    x281 - x374)^2) + 1 / sqrt((x1 - x95)^2 + (x141 - x235)^2 + (x281 - x375)^2)
    + 1 / sqrt((x1 - x96)^2 + (x141 - x236)^2 + (x281 - x376)^2) + 1 / sqrt((
    x1 - x97)^2 + (x141 - x237)^2 + (x281 - x377)^2) + 1 / sqrt((x1 - x98)^2 +
    (x141 - x238)^2 + (x281 - x378)^2) + 1 / sqrt((x1 - x99)^2 + (x141 - x239)^
    2 + (x281 - x379)^2) + 1 / sqrt((x1 - x100)^2 + (x141 - x240)^2 + (x281 -
    x380)^2) + 1 / sqrt((x1 - x101)^2 + (x141 - x241)^2 + (x281 - x381)^2) + 1
    / sqrt((x1 - x102)^2 + (x141 - x242)^2 + (x281 - x382)^2) + 1 / sqrt((x1
    - x103)^2 + (x141 - x243)^2 + (x281 - x383)^2) + 1 / sqrt((x1 - x104)^2 +
    (x141 - x244)^2 + (x281 - x384)^2) + 1 / sqrt((x1 - x105)^2 + (x141 - x245)
    ^2 + (x281 - x385)^2) + 1 / sqrt((x1 - x106)^2 + (x141 - x246)^2 + (x281 -
    x386)^2) + 1 / sqrt((x1 - x107)^2 + (x141 - x247)^2 + (x281 - x387)^2) + 1
    / sqrt((x1 - x108)^2 + (x141 - x248)^2 + (x281 - x388)^2) + 1 / sqrt((x1
    - x109)^2 + (x141 - x249)^2 + (x281 - x389)^2) + 1 / sqrt((x1 - x110)^2 +
    (x141 - x250)^2 + (x281 - x390)^2) + 1 / sqrt((x1 - x111)^2 + (x141 - x251)
    ^2 + (x281 - x391)^2) + 1 / sqrt((x1 - x112)^2 + (x141 - x252)^2 + (x281 -
    x392)^2) + 1 / sqrt((x1 - x113)^2 + (x141 - x253)^2 + (x281 - x393)^2) + 1
    / sqrt((x1 - x114)^2 + (x141 - x254)^2 + (x281 - x394)^2) + 1 / sqrt((x1
    - x115)^2 + (x141 - x255)^2 + (x281 - x395)^2) + 1 / sqrt((x1 - x116)^2 +
    (x141 - x256)^2 + (x281 - x396)^2) + 1 / sqrt((x1 - x117)^2 + (x141 - x257)
    ^2 + (x281 - x397)^2) + 1 / sqrt((x1 - x118)^2 + (x141 - x258)^2 + (x281 -
    x398)^2) + 1 / sqrt((x1 - x119)^2 + (x141 - x259)^2 + (x281 - x399)^2) + 1
    / sqrt((x1 - x120)^2 + (x141 - x260)^2 + (x281 - x400)^2) + 1 / sqrt((x1
    - x121)^2 + (x141 - x261)^2 + (x281 - x401)^2) + 1 / sqrt((x1 - x122)^2 +
    (x141 - x262)^2 + (x281 - x402)^2) + 1 / sqrt((x1 - x123)^2 + (x141 - x263)
    ^2 + (x281 - x403)^2) + 1 / sqrt((x1 - x124)^2 + (x141 - x264)^2 + (x281 -
    x404)^2) + 1 / sqrt((x1 - x125)^2 + (x141 - x265)^2 + (x281 - x405)^2) + 1
    / sqrt((x1 - x126)^2 + (x141 - x266)^2 + (x281 - x406)^2) + 1 / sqrt((x1
    - x127)^2 + (x141 - x267)^2 + (x281 - x407)^2) + 1 / sqrt((x1 - x128)^2 +
    (x141 - x268)^2 + (x281 - x408)^2) + 1 / sqrt((x1 - x129)^2 + (x141 - x269)
    ^2 + (x281 - x409)^2) + 1 / sqrt((x1 - x130)^2 + (x141 - x270)^2 + (x281 -
    x410)^2) + 1 / sqrt((x1 - x131)^2 + (x141 - x271)^2 + (x281 - x411)^2) + 1
    / sqrt((x1 - x132)^2 + (x141 - x272)^2 + (x281 - x412)^2) + 1 / sqrt((x1
    - x133)^2 + (x141 - x273)^2 + (x281 - x413)^2) + 1 / sqrt((x1 - x134)^2 +
    (x141 - x274)^2 + (x281 - x414)^2) + 1 / sqrt((x1 - x135)^2 + (x141 - x275)
    ^2 + (x281 - x415)^2) + 1 / sqrt((x1 - x136)^2 + (x141 - x276)^2 + (x281 -
    x416)^2) + 1 / sqrt((x1 - x137)^2 + (x141 - x277)^2 + (x281 - x417)^2) + 1
    / sqrt((x1 - x138)^2 + (x141 - x278)^2 + (x281 - x418)^2) + 1 / sqrt((x1
    - x139)^2 + (x141 - x279)^2 + (x281 - x419)^2) + 1 / sqrt((x1 - x140)^2 +
    (x141 - x280)^2 + (x281 - x420)^2) + 1 / sqrt((x2 - x3)^2 + (x142 - x143)^2
    + (x282 - x283)^2) + 1 / sqrt((x2 - x4)^2 + (x142 - x144)^2 + (x282 - x284)
    ^2) + 1 / sqrt((x2 - x5)^2 + (x142 - x145)^2 + (x282 - x285)^2) + 1 / sqrt(
    (x2 - x6)^2 + (x142 - x146)^2 + (x282 - x286)^2) + 1 / sqrt((x2 - x7)^2 + (
    x142 - x147)^2 + (x282 - x287)^2) + 1 / sqrt((x2 - x8)^2 + (x142 - x148)^2
    + (x282 - x288)^2) + 1 / sqrt((x2 - x9)^2 + (x142 - x149)^2 + (x282 - x289)
    ^2) + 1 / sqrt((x2 - x10)^2 + (x142 - x150)^2 + (x282 - x290)^2) + 1 /
    sqrt((x2 - x11)^2 + (x142 - x151)^2 + (x282 - x291)^2) + 1 / sqrt((x2 - x12)
    ^2 + (x142 - x152)^2 + (x282 - x292)^2) + 1 / sqrt((x2 - x13)^2 + (x142 -
    x153)^2 + (x282 - x293)^2) + 1 / sqrt((x2 - x14)^2 + (x142 - x154)^2 + (
    x282 - x294)^2) + 1 / sqrt((x2 - x15)^2 + (x142 - x155)^2 + (x282 - x295)^2)
    + 1 / sqrt((x2 - x16)^2 + (x142 - x156)^2 + (x282 - x296)^2) + 1 / sqrt((
    x2 - x17)^2 + (x142 - x157)^2 + (x282 - x297)^2) + 1 / sqrt((x2 - x18)^2 +
    (x142 - x158)^2 + (x282 - x298)^2) + 1 / sqrt((x2 - x19)^2 + (x142 - x159)^
    2 + (x282 - x299)^2) + 1 / sqrt((x2 - x20)^2 + (x142 - x160)^2 + (x282 -
    x300)^2) + 1 / sqrt((x2 - x21)^2 + (x142 - x161)^2 + (x282 - x301)^2) + 1
    / sqrt((x2 - x22)^2 + (x142 - x162)^2 + (x282 - x302)^2) + 1 / sqrt((x2 -
    x23)^2 + (x142 - x163)^2 + (x282 - x303)^2) + 1 / sqrt((x2 - x24)^2 + (x142
    - x164)^2 + (x282 - x304)^2) + 1 / sqrt((x2 - x25)^2 + (x142 - x165)^2 + (
    x282 - x305)^2) + 1 / sqrt((x2 - x26)^2 + (x142 - x166)^2 + (x282 - x306)^2)
    + 1 / sqrt((x2 - x27)^2 + (x142 - x167)^2 + (x282 - x307)^2) + 1 / sqrt((
    x2 - x28)^2 + (x142 - x168)^2 + (x282 - x308)^2) + 1 / sqrt((x2 - x29)^2 +
    (x142 - x169)^2 + (x282 - x309)^2) + 1 / sqrt((x2 - x30)^2 + (x142 - x170)^
    2 + (x282 - x310)^2) + 1 / sqrt((x2 - x31)^2 + (x142 - x171)^2 + (x282 -
    x311)^2) + 1 / sqrt((x2 - x32)^2 + (x142 - x172)^2 + (x282 - x312)^2) + 1
    / sqrt((x2 - x33)^2 + (x142 - x173)^2 + (x282 - x313)^2) + 1 / sqrt((x2 -
    x34)^2 + (x142 - x174)^2 + (x282 - x314)^2) + 1 / sqrt((x2 - x35)^2 + (x142
    - x175)^2 + (x282 - x315)^2) + 1 / sqrt((x2 - x36)^2 + (x142 - x176)^2 + (
    x282 - x316)^2) + 1 / sqrt((x2 - x37)^2 + (x142 - x177)^2 + (x282 - x317)^2)
    + 1 / sqrt((x2 - x38)^2 + (x142 - x178)^2 + (x282 - x318)^2) + 1 / sqrt((
    x2 - x39)^2 + (x142 - x179)^2 + (x282 - x319)^2) + 1 / sqrt((x2 - x40)^2 +
    (x142 - x180)^2 + (x282 - x320)^2) + 1 / sqrt((x2 - x41)^2 + (x142 - x181)^
    2 + (x282 - x321)^2) + 1 / sqrt((x2 - x42)^2 + (x142 - x182)^2 + (x282 -
    x322)^2) + 1 / sqrt((x2 - x43)^2 + (x142 - x183)^2 + (x282 - x323)^2) + 1
    / sqrt((x2 - x44)^2 + (x142 - x184)^2 + (x282 - x324)^2) + 1 / sqrt((x2 -
    x45)^2 + (x142 - x185)^2 + (x282 - x325)^2) + 1 / sqrt((x2 - x46)^2 + (x142
    - x186)^2 + (x282 - x326)^2) + 1 / sqrt((x2 - x47)^2 + (x142 - x187)^2 + (
    x282 - x327)^2) + 1 / sqrt((x2 - x48)^2 + (x142 - x188)^2 + (x282 - x328)^2)
    + 1 / sqrt((x2 - x49)^2 + (x142 - x189)^2 + (x282 - x329)^2) + 1 / sqrt((
    x2 - x50)^2 + (x142 - x190)^2 + (x282 - x330)^2) + 1 / sqrt((x2 - x51)^2 +
    (x142 - x191)^2 + (x282 - x331)^2) + 1 / sqrt((x2 - x52)^2 + (x142 - x192)^
    2 + (x282 - x332)^2) + 1 / sqrt((x2 - x53)^2 + (x142 - x193)^2 + (x282 -
    x333)^2) + 1 / sqrt((x2 - x54)^2 + (x142 - x194)^2 + (x282 - x334)^2) + 1
    / sqrt((x2 - x55)^2 + (x142 - x195)^2 + (x282 - x335)^2) + 1 / sqrt((x2 -
    x56)^2 + (x142 - x196)^2 + (x282 - x336)^2) + 1 / sqrt((x2 - x57)^2 + (x142
    - x197)^2 + (x282 - x337)^2) + 1 / sqrt((x2 - x58)^2 + (x142 - x198)^2 + (
    x282 - x338)^2) + 1 / sqrt((x2 - x59)^2 + (x142 - x199)^2 + (x282 - x339)^2)
    + 1 / sqrt((x2 - x60)^2 + (x142 - x200)^2 + (x282 - x340)^2) + 1 / sqrt((
    x2 - x61)^2 + (x142 - x201)^2 + (x282 - x341)^2) + 1 / sqrt((x2 - x62)^2 +
    (x142 - x202)^2 + (x282 - x342)^2) + 1 / sqrt((x2 - x63)^2 + (x142 - x203)^
    2 + (x282 - x343)^2) + 1 / sqrt((x2 - x64)^2 + (x142 - x204)^2 + (x282 -
    x344)^2) + 1 / sqrt((x2 - x65)^2 + (x142 - x205)^2 + (x282 - x345)^2) + 1
    / sqrt((x2 - x66)^2 + (x142 - x206)^2 + (x282 - x346)^2) + 1 / sqrt((x2 -
    x67)^2 + (x142 - x207)^2 + (x282 - x347)^2) + 1 / sqrt((x2 - x68)^2 + (x142
    - x208)^2 + (x282 - x348)^2) + 1 / sqrt((x2 - x69)^2 + (x142 - x209)^2 + (
    x282 - x349)^2) + 1 / sqrt((x2 - x70)^2 + (x142 - x210)^2 + (x282 - x350)^2)
    + 1 / sqrt((x2 - x71)^2 + (x142 - x211)^2 + (x282 - x351)^2) + 1 / sqrt((
    x2 - x72)^2 + (x142 - x212)^2 + (x282 - x352)^2) + 1 / sqrt((x2 - x73)^2 +
    (x142 - x213)^2 + (x282 - x353)^2) + 1 / sqrt((x2 - x74)^2 + (x142 - x214)^
    2 + (x282 - x354)^2) + 1 / sqrt((x2 - x75)^2 + (x142 - x215)^2 + (x282 -
    x355)^2) + 1 / sqrt((x2 - x76)^2 + (x142 - x216)^2 + (x282 - x356)^2) + 1
    / sqrt((x2 - x77)^2 + (x142 - x217)^2 + (x282 - x357)^2) + 1 / sqrt((x2 -
    x78)^2 + (x142 - x218)^2 + (x282 - x358)^2) + 1 / sqrt((x2 - x79)^2 + (x142
    - x219)^2 + (x282 - x359)^2) + 1 / sqrt((x2 - x80)^2 + (x142 - x220)^2 + (
    x282 - x360)^2) + 1 / sqrt((x2 - x81)^2 + (x142 - x221)^2 + (x282 - x361)^2)
    + 1 / sqrt((x2 - x82)^2 + (x142 - x222)^2 + (x282 - x362)^2) + 1 / sqrt((
    x2 - x83)^2 + (x142 - x223)^2 + (x282 - x363)^2) + 1 / sqrt((x2 - x84)^2 +
    (x142 - x224)^2 + (x282 - x364)^2) + 1 / sqrt((x2 - x85)^2 + (x142 - x225)^
    2 + (x282 - x365)^2) + 1 / sqrt((x2 - x86)^2 + (x142 - x226)^2 + (x282 -
    x366)^2) + 1 / sqrt((x2 - x87)^2 + (x142 - x227)^2 + (x282 - x367)^2) + 1
    / sqrt((x2 - x88)^2 + (x142 - x228)^2 + (x282 - x368)^2) + 1 / sqrt((x2 -
    x89)^2 + (x142 - x229)^2 + (x282 - x369)^2) + 1 / sqrt((x2 - x90)^2 + (x142
    - x230)^2 + (x282 - x370)^2) + 1 / sqrt((x2 - x91)^2 + (x142 - x231)^2 + (
    x282 - x371)^2) + 1 / sqrt((x2 - x92)^2 + (x142 - x232)^2 + (x282 - x372)^2)
    + 1 / sqrt((x2 - x93)^2 + (x142 - x233)^2 + (x282 - x373)^2) + 1 / sqrt((
    x2 - x94)^2 + (x142 - x234)^2 + (x282 - x374)^2) + 1 / sqrt((x2 - x95)^2 +
    (x142 - x235)^2 + (x282 - x375)^2) + 1 / sqrt((x2 - x96)^2 + (x142 - x236)^
    2 + (x282 - x376)^2) + 1 / sqrt((x2 - x97)^2 + (x142 - x237)^2 + (x282 -
    x377)^2) + 1 / sqrt((x2 - x98)^2 + (x142 - x238)^2 + (x282 - x378)^2) + 1
    / sqrt((x2 - x99)^2 + (x142 - x239)^2 + (x282 - x379)^2) + 1 / sqrt((x2 -
    x100)^2 + (x142 - x240)^2 + (x282 - x380)^2) + 1 / sqrt((x2 - x101)^2 + (
    x142 - x241)^2 + (x282 - x381)^2) + 1 / sqrt((x2 - x102)^2 + (x142 - x242)^
    2 + (x282 - x382)^2) + 1 / sqrt((x2 - x103)^2 + (x142 - x243)^2 + (x282 -
    x383)^2) + 1 / sqrt((x2 - x104)^2 + (x142 - x244)^2 + (x282 - x384)^2) + 1
    / sqrt((x2 - x105)^2 + (x142 - x245)^2 + (x282 - x385)^2) + 1 / sqrt((x2
    - x106)^2 + (x142 - x246)^2 + (x282 - x386)^2) + 1 / sqrt((x2 - x107)^2 +
    (x142 - x247)^2 + (x282 - x387)^2) + 1 / sqrt((x2 - x108)^2 + (x142 - x248)
    ^2 + (x282 - x388)^2) + 1 / sqrt((x2 - x109)^2 + (x142 - x249)^2 + (x282 -
    x389)^2) + 1 / sqrt((x2 - x110)^2 + (x142 - x250)^2 + (x282 - x390)^2) + 1
    / sqrt((x2 - x111)^2 + (x142 - x251)^2 + (x282 - x391)^2) + 1 / sqrt((x2
    - x112)^2 + (x142 - x252)^2 + (x282 - x392)^2) + 1 / sqrt((x2 - x113)^2 +
    (x142 - x253)^2 + (x282 - x393)^2) + 1 / sqrt((x2 - x114)^2 + (x142 - x254)
    ^2 + (x282 - x394)^2) + 1 / sqrt((x2 - x115)^2 + (x142 - x255)^2 + (x282 -
    x395)^2) + 1 / sqrt((x2 - x116)^2 + (x142 - x256)^2 + (x282 - x396)^2) + 1
    / sqrt((x2 - x117)^2 + (x142 - x257)^2 + (x282 - x397)^2) + 1 / sqrt((x2
    - x118)^2 + (x142 - x258)^2 + (x282 - x398)^2) + 1 / sqrt((x2 - x119)^2 +
    (x142 - x259)^2 + (x282 - x399)^2) + 1 / sqrt((x2 - x120)^2 + (x142 - x260)
    ^2 + (x282 - x400)^2) + 1 / sqrt((x2 - x121)^2 + (x142 - x261)^2 + (x282 -
    x401)^2) + 1 / sqrt((x2 - x122)^2 + (x142 - x262)^2 + (x282 - x402)^2) + 1
    / sqrt((x2 - x123)^2 + (x142 - x263)^2 + (x282 - x403)^2) + 1 / sqrt((x2
    - x124)^2 + (x142 - x264)^2 + (x282 - x404)^2) + 1 / sqrt((x2 - x125)^2 +
    (x142 - x265)^2 + (x282 - x405)^2) + 1 / sqrt((x2 - x126)^2 + (x142 - x266)
    ^2 + (x282 - x406)^2) + 1 / sqrt((x2 - x127)^2 + (x142 - x267)^2 + (x282 -
    x407)^2) + 1 / sqrt((x2 - x128)^2 + (x142 - x268)^2 + (x282 - x408)^2) + 1
    / sqrt((x2 - x129)^2 + (x142 - x269)^2 + (x282 - x409)^2) + 1 / sqrt((x2
    - x130)^2 + (x142 - x270)^2 + (x282 - x410)^2) + 1 / sqrt((x2 - x131)^2 +
    (x142 - x271)^2 + (x282 - x411)^2) + 1 / sqrt((x2 - x132)^2 + (x142 - x272)
    ^2 + (x282 - x412)^2) + 1 / sqrt((x2 - x133)^2 + (x142 - x273)^2 + (x282 -
    x413)^2) + 1 / sqrt((x2 - x134)^2 + (x142 - x274)^2 + (x282 - x414)^2) + 1
    / sqrt((x2 - x135)^2 + (x142 - x275)^2 + (x282 - x415)^2) + 1 / sqrt((x2
    - x136)^2 + (x142 - x276)^2 + (x282 - x416)^2) + 1 / sqrt((x2 - x137)^2 +
    (x142 - x277)^2 + (x282 - x417)^2) + 1 / sqrt((x2 - x138)^2 + (x142 - x278)
    ^2 + (x282 - x418)^2) + 1 / sqrt((x2 - x139)^2 + (x142 - x279)^2 + (x282 -
    x419)^2) + 1 / sqrt((x2 - x140)^2 + (x142 - x280)^2 + (x282 - x420)^2) + 1
    / sqrt((x3 - x4)^2 + (x143 - x144)^2 + (x283 - x284)^2) + 1 / sqrt((x3 -
    x5)^2 + (x143 - x145)^2 + (x283 - x285)^2) + 1 / sqrt((x3 - x6)^2 + (x143
    - x146)^2 + (x283 - x286)^2) + 1 / sqrt((x3 - x7)^2 + (x143 - x147)^2 + (
    x283 - x287)^2) + 1 / sqrt((x3 - x8)^2 + (x143 - x148)^2 + (x283 - x288)^2)
    + 1 / sqrt((x3 - x9)^2 + (x143 - x149)^2 + (x283 - x289)^2) + 1 / sqrt((x3
    - x10)^2 + (x143 - x150)^2 + (x283 - x290)^2) + 1 / sqrt((x3 - x11)^2 + (
    x143 - x151)^2 + (x283 - x291)^2) + 1 / sqrt((x3 - x12)^2 + (x143 - x152)^2
    + (x283 - x292)^2) + 1 / sqrt((x3 - x13)^2 + (x143 - x153)^2 + (x283 -
    x293)^2) + 1 / sqrt((x3 - x14)^2 + (x143 - x154)^2 + (x283 - x294)^2) + 1
    / sqrt((x3 - x15)^2 + (x143 - x155)^2 + (x283 - x295)^2) + 1 / sqrt((x3 -
    x16)^2 + (x143 - x156)^2 + (x283 - x296)^2) + 1 / sqrt((x3 - x17)^2 + (x143
    - x157)^2 + (x283 - x297)^2) + 1 / sqrt((x3 - x18)^2 + (x143 - x158)^2 + (
    x283 - x298)^2) + 1 / sqrt((x3 - x19)^2 + (x143 - x159)^2 + (x283 - x299)^2)
    + 1 / sqrt((x3 - x20)^2 + (x143 - x160)^2 + (x283 - x300)^2) + 1 / sqrt((
    x3 - x21)^2 + (x143 - x161)^2 + (x283 - x301)^2) + 1 / sqrt((x3 - x22)^2 +
    (x143 - x162)^2 + (x283 - x302)^2) + 1 / sqrt((x3 - x23)^2 + (x143 - x163)^
    2 + (x283 - x303)^2) + 1 / sqrt((x3 - x24)^2 + (x143 - x164)^2 + (x283 -
    x304)^2) + 1 / sqrt((x3 - x25)^2 + (x143 - x165)^2 + (x283 - x305)^2) + 1
    / sqrt((x3 - x26)^2 + (x143 - x166)^2 + (x283 - x306)^2) + 1 / sqrt((x3 -
    x27)^2 + (x143 - x167)^2 + (x283 - x307)^2) + 1 / sqrt((x3 - x28)^2 + (x143
    - x168)^2 + (x283 - x308)^2) + 1 / sqrt((x3 - x29)^2 + (x143 - x169)^2 + (
    x283 - x309)^2) + 1 / sqrt((x3 - x30)^2 + (x143 - x170)^2 + (x283 - x310)^2)
    + 1 / sqrt((x3 - x31)^2 + (x143 - x171)^2 + (x283 - x311)^2) + 1 / sqrt((
    x3 - x32)^2 + (x143 - x172)^2 + (x283 - x312)^2) + 1 / sqrt((x3 - x33)^2 +
    (x143 - x173)^2 + (x283 - x313)^2) + 1 / sqrt((x3 - x34)^2 + (x143 - x174)^
    2 + (x283 - x314)^2) + 1 / sqrt((x3 - x35)^2 + (x143 - x175)^2 + (x283 -
    x315)^2) + 1 / sqrt((x3 - x36)^2 + (x143 - x176)^2 + (x283 - x316)^2) + 1
    / sqrt((x3 - x37)^2 + (x143 - x177)^2 + (x283 - x317)^2) + 1 / sqrt((x3 -
    x38)^2 + (x143 - x178)^2 + (x283 - x318)^2) + 1 / sqrt((x3 - x39)^2 + (x143
    - x179)^2 + (x283 - x319)^2) + 1 / sqrt((x3 - x40)^2 + (x143 - x180)^2 + (
    x283 - x320)^2) + 1 / sqrt((x3 - x41)^2 + (x143 - x181)^2 + (x283 - x321)^2)
    + 1 / sqrt((x3 - x42)^2 + (x143 - x182)^2 + (x283 - x322)^2) + 1 / sqrt((
    x3 - x43)^2 + (x143 - x183)^2 + (x283 - x323)^2) + 1 / sqrt((x3 - x44)^2 +
    (x143 - x184)^2 + (x283 - x324)^2) + 1 / sqrt((x3 - x45)^2 + (x143 - x185)^
    2 + (x283 - x325)^2) + 1 / sqrt((x3 - x46)^2 + (x143 - x186)^2 + (x283 -
    x326)^2) + 1 / sqrt((x3 - x47)^2 + (x143 - x187)^2 + (x283 - x327)^2) + 1
    / sqrt((x3 - x48)^2 + (x143 - x188)^2 + (x283 - x328)^2) + 1 / sqrt((x3 -
    x49)^2 + (x143 - x189)^2 + (x283 - x329)^2) + 1 / sqrt((x3 - x50)^2 + (x143
    - x190)^2 + (x283 - x330)^2) + 1 / sqrt((x3 - x51)^2 + (x143 - x191)^2 + (
    x283 - x331)^2) + 1 / sqrt((x3 - x52)^2 + (x143 - x192)^2 + (x283 - x332)^2)
    + 1 / sqrt((x3 - x53)^2 + (x143 - x193)^2 + (x283 - x333)^2) + 1 / sqrt((
    x3 - x54)^2 + (x143 - x194)^2 + (x283 - x334)^2) + 1 / sqrt((x3 - x55)^2 +
    (x143 - x195)^2 + (x283 - x335)^2) + 1 / sqrt((x3 - x56)^2 + (x143 - x196)^
    2 + (x283 - x336)^2) + 1 / sqrt((x3 - x57)^2 + (x143 - x197)^2 + (x283 -
    x337)^2) + 1 / sqrt((x3 - x58)^2 + (x143 - x198)^2 + (x283 - x338)^2) + 1
    / sqrt((x3 - x59)^2 + (x143 - x199)^2 + (x283 - x339)^2) + 1 / sqrt((x3 -
    x60)^2 + (x143 - x200)^2 + (x283 - x340)^2) + 1 / sqrt((x3 - x61)^2 + (x143
    - x201)^2 + (x283 - x341)^2) + 1 / sqrt((x3 - x62)^2 + (x143 - x202)^2 + (
    x283 - x342)^2) + 1 / sqrt((x3 - x63)^2 + (x143 - x203)^2 + (x283 - x343)^2)
    + 1 / sqrt((x3 - x64)^2 + (x143 - x204)^2 + (x283 - x344)^2) + 1 / sqrt((
    x3 - x65)^2 + (x143 - x205)^2 + (x283 - x345)^2) + 1 / sqrt((x3 - x66)^2 +
    (x143 - x206)^2 + (x283 - x346)^2) + 1 / sqrt((x3 - x67)^2 + (x143 - x207)^
    2 + (x283 - x347)^2) + 1 / sqrt((x3 - x68)^2 + (x143 - x208)^2 + (x283 -
    x348)^2) + 1 / sqrt((x3 - x69)^2 + (x143 - x209)^2 + (x283 - x349)^2) + 1
    / sqrt((x3 - x70)^2 + (x143 - x210)^2 + (x283 - x350)^2) + 1 / sqrt((x3 -
    x71)^2 + (x143 - x211)^2 + (x283 - x351)^2) + 1 / sqrt((x3 - x72)^2 + (x143
    - x212)^2 + (x283 - x352)^2) + 1 / sqrt((x3 - x73)^2 + (x143 - x213)^2 + (
    x283 - x353)^2) + 1 / sqrt((x3 - x74)^2 + (x143 - x214)^2 + (x283 - x354)^2)
    + 1 / sqrt((x3 - x75)^2 + (x143 - x215)^2 + (x283 - x355)^2) + 1 / sqrt((
    x3 - x76)^2 + (x143 - x216)^2 + (x283 - x356)^2) + 1 / sqrt((x3 - x77)^2 +
    (x143 - x217)^2 + (x283 - x357)^2) + 1 / sqrt((x3 - x78)^2 + (x143 - x218)^
    2 + (x283 - x358)^2) + 1 / sqrt((x3 - x79)^2 + (x143 - x219)^2 + (x283 -
    x359)^2) + 1 / sqrt((x3 - x80)^2 + (x143 - x220)^2 + (x283 - x360)^2) + 1
    / sqrt((x3 - x81)^2 + (x143 - x221)^2 + (x283 - x361)^2) + 1 / sqrt((x3 -
    x82)^2 + (x143 - x222)^2 + (x283 - x362)^2) + 1 / sqrt((x3 - x83)^2 + (x143
    - x223)^2 + (x283 - x363)^2) + 1 / sqrt((x3 - x84)^2 + (x143 - x224)^2 + (
    x283 - x364)^2) + 1 / sqrt((x3 - x85)^2 + (x143 - x225)^2 + (x283 - x365)^2)
    + 1 / sqrt((x3 - x86)^2 + (x143 - x226)^2 + (x283 - x366)^2) + 1 / sqrt((
    x3 - x87)^2 + (x143 - x227)^2 + (x283 - x367)^2) + 1 / sqrt((x3 - x88)^2 +
    (x143 - x228)^2 + (x283 - x368)^2) + 1 / sqrt((x3 - x89)^2 + (x143 - x229)^
    2 + (x283 - x369)^2) + 1 / sqrt((x3 - x90)^2 + (x143 - x230)^2 + (x283 -
    x370)^2) + 1 / sqrt((x3 - x91)^2 + (x143 - x231)^2 + (x283 - x371)^2) + 1
    / sqrt((x3 - x92)^2 + (x143 - x232)^2 + (x283 - x372)^2) + 1 / sqrt((x3 -
    x93)^2 + (x143 - x233)^2 + (x283 - x373)^2) + 1 / sqrt((x3 - x94)^2 + (x143
    - x234)^2 + (x283 - x374)^2) + 1 / sqrt((x3 - x95)^2 + (x143 - x235)^2 + (
    x283 - x375)^2) + 1 / sqrt((x3 - x96)^2 + (x143 - x236)^2 + (x283 - x376)^2)
    + 1 / sqrt((x3 - x97)^2 + (x143 - x237)^2 + (x283 - x377)^2) + 1 / sqrt((
    x3 - x98)^2 + (x143 - x238)^2 + (x283 - x378)^2) + 1 / sqrt((x3 - x99)^2 +
    (x143 - x239)^2 + (x283 - x379)^2) + 1 / sqrt((x3 - x100)^2 + (x143 - x240)
    ^2 + (x283 - x380)^2) + 1 / sqrt((x3 - x101)^2 + (x143 - x241)^2 + (x283 -
    x381)^2) + 1 / sqrt((x3 - x102)^2 + (x143 - x242)^2 + (x283 - x382)^2) + 1
    / sqrt((x3 - x103)^2 + (x143 - x243)^2 + (x283 - x383)^2) + 1 / sqrt((x3
    - x104)^2 + (x143 - x244)^2 + (x283 - x384)^2) + 1 / sqrt((x3 - x105)^2 +
    (x143 - x245)^2 + (x283 - x385)^2) + 1 / sqrt((x3 - x106)^2 + (x143 - x246)
    ^2 + (x283 - x386)^2) + 1 / sqrt((x3 - x107)^2 + (x143 - x247)^2 + (x283 -
    x387)^2) + 1 / sqrt((x3 - x108)^2 + (x143 - x248)^2 + (x283 - x388)^2) + 1
    / sqrt((x3 - x109)^2 + (x143 - x249)^2 + (x283 - x389)^2) + 1 / sqrt((x3
    - x110)^2 + (x143 - x250)^2 + (x283 - x390)^2) + 1 / sqrt((x3 - x111)^2 +
    (x143 - x251)^2 + (x283 - x391)^2) + 1 / sqrt((x3 - x112)^2 + (x143 - x252)
    ^2 + (x283 - x392)^2) + 1 / sqrt((x3 - x113)^2 + (x143 - x253)^2 + (x283 -
    x393)^2) + 1 / sqrt((x3 - x114)^2 + (x143 - x254)^2 + (x283 - x394)^2) + 1
    / sqrt((x3 - x115)^2 + (x143 - x255)^2 + (x283 - x395)^2) + 1 / sqrt((x3
    - x116)^2 + (x143 - x256)^2 + (x283 - x396)^2) + 1 / sqrt((x3 - x117)^2 +
    (x143 - x257)^2 + (x283 - x397)^2) + 1 / sqrt((x3 - x118)^2 + (x143 - x258)
    ^2 + (x283 - x398)^2) + 1 / sqrt((x3 - x119)^2 + (x143 - x259)^2 + (x283 -
    x399)^2) + 1 / sqrt((x3 - x120)^2 + (x143 - x260)^2 + (x283 - x400)^2) + 1
    / sqrt((x3 - x121)^2 + (x143 - x261)^2 + (x283 - x401)^2) + 1 / sqrt((x3
    - x122)^2 + (x143 - x262)^2 + (x283 - x402)^2) + 1 / sqrt((x3 - x123)^2 +
    (x143 - x263)^2 + (x283 - x403)^2) + 1 / sqrt((x3 - x124)^2 + (x143 - x264)
    ^2 + (x283 - x404)^2) + 1 / sqrt((x3 - x125)^2 + (x143 - x265)^2 + (x283 -
    x405)^2) + 1 / sqrt((x3 - x126)^2 + (x143 - x266)^2 + (x283 - x406)^2) + 1
    / sqrt((x3 - x127)^2 + (x143 - x267)^2 + (x283 - x407)^2) + 1 / sqrt((x3
    - x128)^2 + (x143 - x268)^2 + (x283 - x408)^2) + 1 / sqrt((x3 - x129)^2 +
    (x143 - x269)^2 + (x283 - x409)^2) + 1 / sqrt((x3 - x130)^2 + (x143 - x270)
    ^2 + (x283 - x410)^2) + 1 / sqrt((x3 - x131)^2 + (x143 - x271)^2 + (x283 -
    x411)^2) + 1 / sqrt((x3 - x132)^2 + (x143 - x272)^2 + (x283 - x412)^2) + 1
    / sqrt((x3 - x133)^2 + (x143 - x273)^2 + (x283 - x413)^2) + 1 / sqrt((x3
    - x134)^2 + (x143 - x274)^2 + (x283 - x414)^2) + 1 / sqrt((x3 - x135)^2 +
    (x143 - x275)^2 + (x283 - x415)^2) + 1 / sqrt((x3 - x136)^2 + (x143 - x276)
    ^2 + (x283 - x416)^2) + 1 / sqrt((x3 - x137)^2 + (x143 - x277)^2 + (x283 -
    x417)^2) + 1 / sqrt((x3 - x138)^2 + (x143 - x278)^2 + (x283 - x418)^2) + 1
    / sqrt((x3 - x139)^2 + (x143 - x279)^2 + (x283 - x419)^2) + 1 / sqrt((x3
    - x140)^2 + (x143 - x280)^2 + (x283 - x420)^2) + 1 / sqrt((x4 - x5)^2 + (
    x144 - x145)^2 + (x284 - x285)^2) + 1 / sqrt((x4 - x6)^2 + (x144 - x146)^2
    + (x284 - x286)^2) + 1 / sqrt((x4 - x7)^2 + (x144 - x147)^2 + (x284 - x287)
    ^2) + 1 / sqrt((x4 - x8)^2 + (x144 - x148)^2 + (x284 - x288)^2) + 1 / sqrt(
    (x4 - x9)^2 + (x144 - x149)^2 + (x284 - x289)^2) + 1 / sqrt((x4 - x10)^2 +
    (x144 - x150)^2 + (x284 - x290)^2) + 1 / sqrt((x4 - x11)^2 + (x144 - x151)^
    2 + (x284 - x291)^2) + 1 / sqrt((x4 - x12)^2 + (x144 - x152)^2 + (x284 -
    x292)^2) + 1 / sqrt((x4 - x13)^2 + (x144 - x153)^2 + (x284 - x293)^2) + 1
    / sqrt((x4 - x14)^2 + (x144 - x154)^2 + (x284 - x294)^2) + 1 / sqrt((x4 -
    x15)^2 + (x144 - x155)^2 + (x284 - x295)^2) + 1 / sqrt((x4 - x16)^2 + (x144
    - x156)^2 + (x284 - x296)^2) + 1 / sqrt((x4 - x17)^2 + (x144 - x157)^2 + (
    x284 - x297)^2) + 1 / sqrt((x4 - x18)^2 + (x144 - x158)^2 + (x284 - x298)^2)
    + 1 / sqrt((x4 - x19)^2 + (x144 - x159)^2 + (x284 - x299)^2) + 1 / sqrt((
    x4 - x20)^2 + (x144 - x160)^2 + (x284 - x300)^2) + 1 / sqrt((x4 - x21)^2 +
    (x144 - x161)^2 + (x284 - x301)^2) + 1 / sqrt((x4 - x22)^2 + (x144 - x162)^
    2 + (x284 - x302)^2) + 1 / sqrt((x4 - x23)^2 + (x144 - x163)^2 + (x284 -
    x303)^2) + 1 / sqrt((x4 - x24)^2 + (x144 - x164)^2 + (x284 - x304)^2) + 1
    / sqrt((x4 - x25)^2 + (x144 - x165)^2 + (x284 - x305)^2) + 1 / sqrt((x4 -
    x26)^2 + (x144 - x166)^2 + (x284 - x306)^2) + 1 / sqrt((x4 - x27)^2 + (x144
    - x167)^2 + (x284 - x307)^2) + 1 / sqrt((x4 - x28)^2 + (x144 - x168)^2 + (
    x284 - x308)^2) + 1 / sqrt((x4 - x29)^2 + (x144 - x169)^2 + (x284 - x309)^2)
    + 1 / sqrt((x4 - x30)^2 + (x144 - x170)^2 + (x284 - x310)^2) + 1 / sqrt((
    x4 - x31)^2 + (x144 - x171)^2 + (x284 - x311)^2) + 1 / sqrt((x4 - x32)^2 +
    (x144 - x172)^2 + (x284 - x312)^2) + 1 / sqrt((x4 - x33)^2 + (x144 - x173)^
    2 + (x284 - x313)^2) + 1 / sqrt((x4 - x34)^2 + (x144 - x174)^2 + (x284 -
    x314)^2) + 1 / sqrt((x4 - x35)^2 + (x144 - x175)^2 + (x284 - x315)^2) + 1
    / sqrt((x4 - x36)^2 + (x144 - x176)^2 + (x284 - x316)^2) + 1 / sqrt((x4 -
    x37)^2 + (x144 - x177)^2 + (x284 - x317)^2) + 1 / sqrt((x4 - x38)^2 + (x144
    - x178)^2 + (x284 - x318)^2) + 1 / sqrt((x4 - x39)^2 + (x144 - x179)^2 + (
    x284 - x319)^2) + 1 / sqrt((x4 - x40)^2 + (x144 - x180)^2 + (x284 - x320)^2)
    + 1 / sqrt((x4 - x41)^2 + (x144 - x181)^2 + (x284 - x321)^2) + 1 / sqrt((
    x4 - x42)^2 + (x144 - x182)^2 + (x284 - x322)^2) + 1 / sqrt((x4 - x43)^2 +
    (x144 - x183)^2 + (x284 - x323)^2) + 1 / sqrt((x4 - x44)^2 + (x144 - x184)^
    2 + (x284 - x324)^2) + 1 / sqrt((x4 - x45)^2 + (x144 - x185)^2 + (x284 -
    x325)^2) + 1 / sqrt((x4 - x46)^2 + (x144 - x186)^2 + (x284 - x326)^2) + 1
    / sqrt((x4 - x47)^2 + (x144 - x187)^2 + (x284 - x327)^2) + 1 / sqrt((x4 -
    x48)^2 + (x144 - x188)^2 + (x284 - x328)^2) + 1 / sqrt((x4 - x49)^2 + (x144
    - x189)^2 + (x284 - x329)^2) + 1 / sqrt((x4 - x50)^2 + (x144 - x190)^2 + (
    x284 - x330)^2) + 1 / sqrt((x4 - x51)^2 + (x144 - x191)^2 + (x284 - x331)^2)
    + 1 / sqrt((x4 - x52)^2 + (x144 - x192)^2 + (x284 - x332)^2) + 1 / sqrt((
    x4 - x53)^2 + (x144 - x193)^2 + (x284 - x333)^2) + 1 / sqrt((x4 - x54)^2 +
    (x144 - x194)^2 + (x284 - x334)^2) + 1 / sqrt((x4 - x55)^2 + (x144 - x195)^
    2 + (x284 - x335)^2) + 1 / sqrt((x4 - x56)^2 + (x144 - x196)^2 + (x284 -
    x336)^2) + 1 / sqrt((x4 - x57)^2 + (x144 - x197)^2 + (x284 - x337)^2) + 1
    / sqrt((x4 - x58)^2 + (x144 - x198)^2 + (x284 - x338)^2) + 1 / sqrt((x4 -
    x59)^2 + (x144 - x199)^2 + (x284 - x339)^2) + 1 / sqrt((x4 - x60)^2 + (x144
    - x200)^2 + (x284 - x340)^2) + 1 / sqrt((x4 - x61)^2 + (x144 - x201)^2 + (
    x284 - x341)^2) + 1 / sqrt((x4 - x62)^2 + (x144 - x202)^2 + (x284 - x342)^2)
    + 1 / sqrt((x4 - x63)^2 + (x144 - x203)^2 + (x284 - x343)^2) + 1 / sqrt((
    x4 - x64)^2 + (x144 - x204)^2 + (x284 - x344)^2) + 1 / sqrt((x4 - x65)^2 +
    (x144 - x205)^2 + (x284 - x345)^2) + 1 / sqrt((x4 - x66)^2 + (x144 - x206)^
    2 + (x284 - x346)^2) + 1 / sqrt((x4 - x67)^2 + (x144 - x207)^2 + (x284 -
    x347)^2) + 1 / sqrt((x4 - x68)^2 + (x144 - x208)^2 + (x284 - x348)^2) + 1
    / sqrt((x4 - x69)^2 + (x144 - x209)^2 + (x284 - x349)^2) + 1 / sqrt((x4 -
    x70)^2 + (x144 - x210)^2 + (x284 - x350)^2) + 1 / sqrt((x4 - x71)^2 + (x144
    - x211)^2 + (x284 - x351)^2) + 1 / sqrt((x4 - x72)^2 + (x144 - x212)^2 + (
    x284 - x352)^2) + 1 / sqrt((x4 - x73)^2 + (x144 - x213)^2 + (x284 - x353)^2)
    + 1 / sqrt((x4 - x74)^2 + (x144 - x214)^2 + (x284 - x354)^2) + 1 / sqrt((
    x4 - x75)^2 + (x144 - x215)^2 + (x284 - x355)^2) + 1 / sqrt((x4 - x76)^2 +
    (x144 - x216)^2 + (x284 - x356)^2) + 1 / sqrt((x4 - x77)^2 + (x144 - x217)^
    2 + (x284 - x357)^2) + 1 / sqrt((x4 - x78)^2 + (x144 - x218)^2 + (x284 -
    x358)^2) + 1 / sqrt((x4 - x79)^2 + (x144 - x219)^2 + (x284 - x359)^2) + 1
    / sqrt((x4 - x80)^2 + (x144 - x220)^2 + (x284 - x360)^2) + 1 / sqrt((x4 -
    x81)^2 + (x144 - x221)^2 + (x284 - x361)^2) + 1 / sqrt((x4 - x82)^2 + (x144
    - x222)^2 + (x284 - x362)^2) + 1 / sqrt((x4 - x83)^2 + (x144 - x223)^2 + (
    x284 - x363)^2) + 1 / sqrt((x4 - x84)^2 + (x144 - x224)^2 + (x284 - x364)^2)
    + 1 / sqrt((x4 - x85)^2 + (x144 - x225)^2 + (x284 - x365)^2) + 1 / sqrt((
    x4 - x86)^2 + (x144 - x226)^2 + (x284 - x366)^2) + 1 / sqrt((x4 - x87)^2 +
    (x144 - x227)^2 + (x284 - x367)^2) + 1 / sqrt((x4 - x88)^2 + (x144 - x228)^
    2 + (x284 - x368)^2) + 1 / sqrt((x4 - x89)^2 + (x144 - x229)^2 + (x284 -
    x369)^2) + 1 / sqrt((x4 - x90)^2 + (x144 - x230)^2 + (x284 - x370)^2) + 1
    / sqrt((x4 - x91)^2 + (x144 - x231)^2 + (x284 - x371)^2) + 1 / sqrt((x4 -
    x92)^2 + (x144 - x232)^2 + (x284 - x372)^2) + 1 / sqrt((x4 - x93)^2 + (x144
    - x233)^2 + (x284 - x373)^2) + 1 / sqrt((x4 - x94)^2 + (x144 - x234)^2 + (
    x284 - x374)^2) + 1 / sqrt((x4 - x95)^2 + (x144 - x235)^2 + (x284 - x375)^2)
    + 1 / sqrt((x4 - x96)^2 + (x144 - x236)^2 + (x284 - x376)^2) + 1 / sqrt((
    x4 - x97)^2 + (x144 - x237)^2 + (x284 - x377)^2) + 1 / sqrt((x4 - x98)^2 +
    (x144 - x238)^2 + (x284 - x378)^2) + 1 / sqrt((x4 - x99)^2 + (x144 - x239)^
    2 + (x284 - x379)^2) + 1 / sqrt((x4 - x100)^2 + (x144 - x240)^2 + (x284 -
    x380)^2) + 1 / sqrt((x4 - x101)^2 + (x144 - x241)^2 + (x284 - x381)^2) + 1
    / sqrt((x4 - x102)^2 + (x144 - x242)^2 + (x284 - x382)^2) + 1 / sqrt((x4
    - x103)^2 + (x144 - x243)^2 + (x284 - x383)^2) + 1 / sqrt((x4 - x104)^2 +
    (x144 - x244)^2 + (x284 - x384)^2) + 1 / sqrt((x4 - x105)^2 + (x144 - x245)
    ^2 + (x284 - x385)^2) + 1 / sqrt((x4 - x106)^2 + (x144 - x246)^2 + (x284 -
    x386)^2) + 1 / sqrt((x4 - x107)^2 + (x144 - x247)^2 + (x284 - x387)^2) + 1
    / sqrt((x4 - x108)^2 + (x144 - x248)^2 + (x284 - x388)^2) + 1 / sqrt((x4
    - x109)^2 + (x144 - x249)^2 + (x284 - x389)^2) + 1 / sqrt((x4 - x110)^2 +
    (x144 - x250)^2 + (x284 - x390)^2) + 1 / sqrt((x4 - x111)^2 + (x144 - x251)
    ^2 + (x284 - x391)^2) + 1 / sqrt((x4 - x112)^2 + (x144 - x252)^2 + (x284 -
    x392)^2) + 1 / sqrt((x4 - x113)^2 + (x144 - x253)^2 + (x284 - x393)^2) + 1
    / sqrt((x4 - x114)^2 + (x144 - x254)^2 + (x284 - x394)^2) + 1 / sqrt((x4
    - x115)^2 + (x144 - x255)^2 + (x284 - x395)^2) + 1 / sqrt((x4 - x116)^2 +
    (x144 - x256)^2 + (x284 - x396)^2) + 1 / sqrt((x4 - x117)^2 + (x144 - x257)
    ^2 + (x284 - x397)^2) + 1 / sqrt((x4 - x118)^2 + (x144 - x258)^2 + (x284 -
    x398)^2) + 1 / sqrt((x4 - x119)^2 + (x144 - x259)^2 + (x284 - x399)^2) + 1
    / sqrt((x4 - x120)^2 + (x144 - x260)^2 + (x284 - x400)^2) + 1 / sqrt((x4
    - x121)^2 + (x144 - x261)^2 + (x284 - x401)^2) + 1 / sqrt((x4 - x122)^2 +
    (x144 - x262)^2 + (x284 - x402)^2) + 1 / sqrt((x4 - x123)^2 + (x144 - x263)
    ^2 + (x284 - x403)^2) + 1 / sqrt((x4 - x124)^2 + (x144 - x264)^2 + (x284 -
    x404)^2) + 1 / sqrt((x4 - x125)^2 + (x144 - x265)^2 + (x284 - x405)^2) + 1
    / sqrt((x4 - x126)^2 + (x144 - x266)^2 + (x284 - x406)^2) + 1 / sqrt((x4
    - x127)^2 + (x144 - x267)^2 + (x284 - x407)^2) + 1 / sqrt((x4 - x128)^2 +
    (x144 - x268)^2 + (x284 - x408)^2) + 1 / sqrt((x4 - x129)^2 + (x144 - x269)
    ^2 + (x284 - x409)^2) + 1 / sqrt((x4 - x130)^2 + (x144 - x270)^2 + (x284 -
    x410)^2) + 1 / sqrt((x4 - x131)^2 + (x144 - x271)^2 + (x284 - x411)^2) + 1
    / sqrt((x4 - x132)^2 + (x144 - x272)^2 + (x284 - x412)^2) + 1 / sqrt((x4
    - x133)^2 + (x144 - x273)^2 + (x284 - x413)^2) + 1 / sqrt((x4 - x134)^2 +
    (x144 - x274)^2 + (x284 - x414)^2) + 1 / sqrt((x4 - x135)^2 + (x144 - x275)
    ^2 + (x284 - x415)^2) + 1 / sqrt((x4 - x136)^2 + (x144 - x276)^2 + (x284 -
    x416)^2) + 1 / sqrt((x4 - x137)^2 + (x144 - x277)^2 + (x284 - x417)^2) + 1
    / sqrt((x4 - x138)^2 + (x144 - x278)^2 + (x284 - x418)^2) + 1 / sqrt((x4
    - x139)^2 + (x144 - x279)^2 + (x284 - x419)^2) + 1 / sqrt((x4 - x140)^2 +
    (x144 - x280)^2 + (x284 - x420)^2) + 1 / sqrt((x5 - x6)^2 + (x145 - x146)^2
    + (x285 - x286)^2) + 1 / sqrt((x5 - x7)^2 + (x145 - x147)^2 + (x285 - x287)
    ^2) + 1 / sqrt((x5 - x8)^2 + (x145 - x148)^2 + (x285 - x288)^2) + 1 / sqrt(
    (x5 - x9)^2 + (x145 - x149)^2 + (x285 - x289)^2) + 1 / sqrt((x5 - x10)^2 +
    (x145 - x150)^2 + (x285 - x290)^2) + 1 / sqrt((x5 - x11)^2 + (x145 - x151)^
    2 + (x285 - x291)^2) + 1 / sqrt((x5 - x12)^2 + (x145 - x152)^2 + (x285 -
    x292)^2) + 1 / sqrt((x5 - x13)^2 + (x145 - x153)^2 + (x285 - x293)^2) + 1
    / sqrt((x5 - x14)^2 + (x145 - x154)^2 + (x285 - x294)^2) + 1 / sqrt((x5 -
    x15)^2 + (x145 - x155)^2 + (x285 - x295)^2) + 1 / sqrt((x5 - x16)^2 + (x145
    - x156)^2 + (x285 - x296)^2) + 1 / sqrt((x5 - x17)^2 + (x145 - x157)^2 + (
    x285 - x297)^2) + 1 / sqrt((x5 - x18)^2 + (x145 - x158)^2 + (x285 - x298)^2)
    + 1 / sqrt((x5 - x19)^2 + (x145 - x159)^2 + (x285 - x299)^2) + 1 / sqrt((
    x5 - x20)^2 + (x145 - x160)^2 + (x285 - x300)^2) + 1 / sqrt((x5 - x21)^2 +
    (x145 - x161)^2 + (x285 - x301)^2) + 1 / sqrt((x5 - x22)^2 + (x145 - x162)^
    2 + (x285 - x302)^2) + 1 / sqrt((x5 - x23)^2 + (x145 - x163)^2 + (x285 -
    x303)^2) + 1 / sqrt((x5 - x24)^2 + (x145 - x164)^2 + (x285 - x304)^2) + 1
    / sqrt((x5 - x25)^2 + (x145 - x165)^2 + (x285 - x305)^2) + 1 / sqrt((x5 -
    x26)^2 + (x145 - x166)^2 + (x285 - x306)^2) + 1 / sqrt((x5 - x27)^2 + (x145
    - x167)^2 + (x285 - x307)^2) + 1 / sqrt((x5 - x28)^2 + (x145 - x168)^2 + (
    x285 - x308)^2) + 1 / sqrt((x5 - x29)^2 + (x145 - x169)^2 + (x285 - x309)^2)
    + 1 / sqrt((x5 - x30)^2 + (x145 - x170)^2 + (x285 - x310)^2) + 1 / sqrt((
    x5 - x31)^2 + (x145 - x171)^2 + (x285 - x311)^2) + 1 / sqrt((x5 - x32)^2 +
    (x145 - x172)^2 + (x285 - x312)^2) + 1 / sqrt((x5 - x33)^2 + (x145 - x173)^
    2 + (x285 - x313)^2) + 1 / sqrt((x5 - x34)^2 + (x145 - x174)^2 + (x285 -
    x314)^2) + 1 / sqrt((x5 - x35)^2 + (x145 - x175)^2 + (x285 - x315)^2) + 1
    / sqrt((x5 - x36)^2 + (x145 - x176)^2 + (x285 - x316)^2) + 1 / sqrt((x5 -
    x37)^2 + (x145 - x177)^2 + (x285 - x317)^2) + 1 / sqrt((x5 - x38)^2 + (x145
    - x178)^2 + (x285 - x318)^2) + 1 / sqrt((x5 - x39)^2 + (x145 - x179)^2 + (
    x285 - x319)^2) + 1 / sqrt((x5 - x40)^2 + (x145 - x180)^2 + (x285 - x320)^2)
    + 1 / sqrt((x5 - x41)^2 + (x145 - x181)^2 + (x285 - x321)^2) + 1 / sqrt((
    x5 - x42)^2 + (x145 - x182)^2 + (x285 - x322)^2) + 1 / sqrt((x5 - x43)^2 +
    (x145 - x183)^2 + (x285 - x323)^2) + 1 / sqrt((x5 - x44)^2 + (x145 - x184)^
    2 + (x285 - x324)^2) + 1 / sqrt((x5 - x45)^2 + (x145 - x185)^2 + (x285 -
    x325)^2) + 1 / sqrt((x5 - x46)^2 + (x145 - x186)^2 + (x285 - x326)^2) + 1
    / sqrt((x5 - x47)^2 + (x145 - x187)^2 + (x285 - x327)^2) + 1 / sqrt((x5 -
    x48)^2 + (x145 - x188)^2 + (x285 - x328)^2) + 1 / sqrt((x5 - x49)^2 + (x145
    - x189)^2 + (x285 - x329)^2) + 1 / sqrt((x5 - x50)^2 + (x145 - x190)^2 + (
    x285 - x330)^2) + 1 / sqrt((x5 - x51)^2 + (x145 - x191)^2 + (x285 - x331)^2)
    + 1 / sqrt((x5 - x52)^2 + (x145 - x192)^2 + (x285 - x332)^2) + 1 / sqrt((
    x5 - x53)^2 + (x145 - x193)^2 + (x285 - x333)^2) + 1 / sqrt((x5 - x54)^2 +
    (x145 - x194)^2 + (x285 - x334)^2) + 1 / sqrt((x5 - x55)^2 + (x145 - x195)^
    2 + (x285 - x335)^2) + 1 / sqrt((x5 - x56)^2 + (x145 - x196)^2 + (x285 -
    x336)^2) + 1 / sqrt((x5 - x57)^2 + (x145 - x197)^2 + (x285 - x337)^2) + 1
    / sqrt((x5 - x58)^2 + (x145 - x198)^2 + (x285 - x338)^2) + 1 / sqrt((x5 -
    x59)^2 + (x145 - x199)^2 + (x285 - x339)^2) + 1 / sqrt((x5 - x60)^2 + (x145
    - x200)^2 + (x285 - x340)^2) + 1 / sqrt((x5 - x61)^2 + (x145 - x201)^2 + (
    x285 - x341)^2) + 1 / sqrt((x5 - x62)^2 + (x145 - x202)^2 + (x285 - x342)^2)
    + 1 / sqrt((x5 - x63)^2 + (x145 - x203)^2 + (x285 - x343)^2) + 1 / sqrt((
    x5 - x64)^2 + (x145 - x204)^2 + (x285 - x344)^2) + 1 / sqrt((x5 - x65)^2 +
    (x145 - x205)^2 + (x285 - x345)^2) + 1 / sqrt((x5 - x66)^2 + (x145 - x206)^
    2 + (x285 - x346)^2) + 1 / sqrt((x5 - x67)^2 + (x145 - x207)^2 + (x285 -
    x347)^2) + 1 / sqrt((x5 - x68)^2 + (x145 - x208)^2 + (x285 - x348)^2) + 1
    / sqrt((x5 - x69)^2 + (x145 - x209)^2 + (x285 - x349)^2) + 1 / sqrt((x5 -
    x70)^2 + (x145 - x210)^2 + (x285 - x350)^2) + 1 / sqrt((x5 - x71)^2 + (x145
    - x211)^2 + (x285 - x351)^2) + 1 / sqrt((x5 - x72)^2 + (x145 - x212)^2 + (
    x285 - x352)^2) + 1 / sqrt((x5 - x73)^2 + (x145 - x213)^2 + (x285 - x353)^2)
    + 1 / sqrt((x5 - x74)^2 + (x145 - x214)^2 + (x285 - x354)^2) + 1 / sqrt((
    x5 - x75)^2 + (x145 - x215)^2 + (x285 - x355)^2) + 1 / sqrt((x5 - x76)^2 +
    (x145 - x216)^2 + (x285 - x356)^2) + 1 / sqrt((x5 - x77)^2 + (x145 - x217)^
    2 + (x285 - x357)^2) + 1 / sqrt((x5 - x78)^2 + (x145 - x218)^2 + (x285 -
    x358)^2) + 1 / sqrt((x5 - x79)^2 + (x145 - x219)^2 + (x285 - x359)^2) + 1
    / sqrt((x5 - x80)^2 + (x145 - x220)^2 + (x285 - x360)^2) + 1 / sqrt((x5 -
    x81)^2 + (x145 - x221)^2 + (x285 - x361)^2) + 1 / sqrt((x5 - x82)^2 + (x145
    - x222)^2 + (x285 - x362)^2) + 1 / sqrt((x5 - x83)^2 + (x145 - x223)^2 + (
    x285 - x363)^2) + 1 / sqrt((x5 - x84)^2 + (x145 - x224)^2 + (x285 - x364)^2)
    + 1 / sqrt((x5 - x85)^2 + (x145 - x225)^2 + (x285 - x365)^2) + 1 / sqrt((
    x5 - x86)^2 + (x145 - x226)^2 + (x285 - x366)^2) + 1 / sqrt((x5 - x87)^2 +
    (x145 - x227)^2 + (x285 - x367)^2) + 1 / sqrt((x5 - x88)^2 + (x145 - x228)^
    2 + (x285 - x368)^2) + 1 / sqrt((x5 - x89)^2 + (x145 - x229)^2 + (x285 -
    x369)^2) + 1 / sqrt((x5 - x90)^2 + (x145 - x230)^2 + (x285 - x370)^2) + 1
    / sqrt((x5 - x91)^2 + (x145 - x231)^2 + (x285 - x371)^2) + 1 / sqrt((x5 -
    x92)^2 + (x145 - x232)^2 + (x285 - x372)^2) + 1 / sqrt((x5 - x93)^2 + (x145
    - x233)^2 + (x285 - x373)^2) + 1 / sqrt((x5 - x94)^2 + (x145 - x234)^2 + (
    x285 - x374)^2) + 1 / sqrt((x5 - x95)^2 + (x145 - x235)^2 + (x285 - x375)^2)
    + 1 / sqrt((x5 - x96)^2 + (x145 - x236)^2 + (x285 - x376)^2) + 1 / sqrt((
    x5 - x97)^2 + (x145 - x237)^2 + (x285 - x377)^2) + 1 / sqrt((x5 - x98)^2 +
    (x145 - x238)^2 + (x285 - x378)^2) + 1 / sqrt((x5 - x99)^2 + (x145 - x239)^
    2 + (x285 - x379)^2) + 1 / sqrt((x5 - x100)^2 + (x145 - x240)^2 + (x285 -
    x380)^2) + 1 / sqrt((x5 - x101)^2 + (x145 - x241)^2 + (x285 - x381)^2) + 1
    / sqrt((x5 - x102)^2 + (x145 - x242)^2 + (x285 - x382)^2) + 1 / sqrt((x5
    - x103)^2 + (x145 - x243)^2 + (x285 - x383)^2) + 1 / sqrt((x5 - x104)^2 +
    (x145 - x244)^2 + (x285 - x384)^2) + 1 / sqrt((x5 - x105)^2 + (x145 - x245)
    ^2 + (x285 - x385)^2) + 1 / sqrt((x5 - x106)^2 + (x145 - x246)^2 + (x285 -
    x386)^2) + 1 / sqrt((x5 - x107)^2 + (x145 - x247)^2 + (x285 - x387)^2) + 1
    / sqrt((x5 - x108)^2 + (x145 - x248)^2 + (x285 - x388)^2) + 1 / sqrt((x5
    - x109)^2 + (x145 - x249)^2 + (x285 - x389)^2) + 1 / sqrt((x5 - x110)^2 +
    (x145 - x250)^2 + (x285 - x390)^2) + 1 / sqrt((x5 - x111)^2 + (x145 - x251)
    ^2 + (x285 - x391)^2) + 1 / sqrt((x5 - x112)^2 + (x145 - x252)^2 + (x285 -
    x392)^2) + 1 / sqrt((x5 - x113)^2 + (x145 - x253)^2 + (x285 - x393)^2) + 1
    / sqrt((x5 - x114)^2 + (x145 - x254)^2 + (x285 - x394)^2) + 1 / sqrt((x5
    - x115)^2 + (x145 - x255)^2 + (x285 - x395)^2) + 1 / sqrt((x5 - x116)^2 +
    (x145 - x256)^2 + (x285 - x396)^2) + 1 / sqrt((x5 - x117)^2 + (x145 - x257)
    ^2 + (x285 - x397)^2) + 1 / sqrt((x5 - x118)^2 + (x145 - x258)^2 + (x285 -
    x398)^2) + 1 / sqrt((x5 - x119)^2 + (x145 - x259)^2 + (x285 - x399)^2) + 1
    / sqrt((x5 - x120)^2 + (x145 - x260)^2 + (x285 - x400)^2) + 1 / sqrt((x5
    - x121)^2 + (x145 - x261)^2 + (x285 - x401)^2) + 1 / sqrt((x5 - x122)^2 +
    (x145 - x262)^2 + (x285 - x402)^2) + 1 / sqrt((x5 - x123)^2 + (x145 - x263)
    ^2 + (x285 - x403)^2) + 1 / sqrt((x5 - x124)^2 + (x145 - x264)^2 + (x285 -
    x404)^2) + 1 / sqrt((x5 - x125)^2 + (x145 - x265)^2 + (x285 - x405)^2) + 1
    / sqrt((x5 - x126)^2 + (x145 - x266)^2 + (x285 - x406)^2) + 1 / sqrt((x5
    - x127)^2 + (x145 - x267)^2 + (x285 - x407)^2) + 1 / sqrt((x5 - x128)^2 +
    (x145 - x268)^2 + (x285 - x408)^2) + 1 / sqrt((x5 - x129)^2 + (x145 - x269)
    ^2 + (x285 - x409)^2) + 1 / sqrt((x5 - x130)^2 + (x145 - x270)^2 + (x285 -
    x410)^2) + 1 / sqrt((x5 - x131)^2 + (x145 - x271)^2 + (x285 - x411)^2) + 1
    / sqrt((x5 - x132)^2 + (x145 - x272)^2 + (x285 - x412)^2) + 1 / sqrt((x5
    - x133)^2 + (x145 - x273)^2 + (x285 - x413)^2) + 1 / sqrt((x5 - x134)^2 +
    (x145 - x274)^2 + (x285 - x414)^2) + 1 / sqrt((x5 - x135)^2 + (x145 - x275)
    ^2 + (x285 - x415)^2) + 1 / sqrt((x5 - x136)^2 + (x145 - x276)^2 + (x285 -
    x416)^2) + 1 / sqrt((x5 - x137)^2 + (x145 - x277)^2 + (x285 - x417)^2) + 1
    / sqrt((x5 - x138)^2 + (x145 - x278)^2 + (x285 - x418)^2) + 1 / sqrt((x5
    - x139)^2 + (x145 - x279)^2 + (x285 - x419)^2) + 1 / sqrt((x5 - x140)^2 +
    (x145 - x280)^2 + (x285 - x420)^2) + 1 / sqrt((x6 - x7)^2 + (x146 - x147)^2
    + (x286 - x287)^2) + 1 / sqrt((x6 - x8)^2 + (x146 - x148)^2 + (x286 - x288)
    ^2) + 1 / sqrt((x6 - x9)^2 + (x146 - x149)^2 + (x286 - x289)^2) + 1 / sqrt(
    (x6 - x10)^2 + (x146 - x150)^2 + (x286 - x290)^2) + 1 / sqrt((x6 - x11)^2
    + (x146 - x151)^2 + (x286 - x291)^2) + 1 / sqrt((x6 - x12)^2 + (x146 -
    x152)^2 + (x286 - x292)^2) + 1 / sqrt((x6 - x13)^2 + (x146 - x153)^2 + (
    x286 - x293)^2) + 1 / sqrt((x6 - x14)^2 + (x146 - x154)^2 + (x286 - x294)^2)
    + 1 / sqrt((x6 - x15)^2 + (x146 - x155)^2 + (x286 - x295)^2) + 1 / sqrt((
    x6 - x16)^2 + (x146 - x156)^2 + (x286 - x296)^2) + 1 / sqrt((x6 - x17)^2 +
    (x146 - x157)^2 + (x286 - x297)^2) + 1 / sqrt((x6 - x18)^2 + (x146 - x158)^
    2 + (x286 - x298)^2) + 1 / sqrt((x6 - x19)^2 + (x146 - x159)^2 + (x286 -
    x299)^2) + 1 / sqrt((x6 - x20)^2 + (x146 - x160)^2 + (x286 - x300)^2) + 1
    / sqrt((x6 - x21)^2 + (x146 - x161)^2 + (x286 - x301)^2) + 1 / sqrt((x6 -
    x22)^2 + (x146 - x162)^2 + (x286 - x302)^2) + 1 / sqrt((x6 - x23)^2 + (x146
    - x163)^2 + (x286 - x303)^2) + 1 / sqrt((x6 - x24)^2 + (x146 - x164)^2 + (
    x286 - x304)^2) + 1 / sqrt((x6 - x25)^2 + (x146 - x165)^2 + (x286 - x305)^2)
    + 1 / sqrt((x6 - x26)^2 + (x146 - x166)^2 + (x286 - x306)^2) + 1 / sqrt((
    x6 - x27)^2 + (x146 - x167)^2 + (x286 - x307)^2) + 1 / sqrt((x6 - x28)^2 +
    (x146 - x168)^2 + (x286 - x308)^2) + 1 / sqrt((x6 - x29)^2 + (x146 - x169)^
    2 + (x286 - x309)^2) + 1 / sqrt((x6 - x30)^2 + (x146 - x170)^2 + (x286 -
    x310)^2) + 1 / sqrt((x6 - x31)^2 + (x146 - x171)^2 + (x286 - x311)^2) + 1
    / sqrt((x6 - x32)^2 + (x146 - x172)^2 + (x286 - x312)^2) + 1 / sqrt((x6 -
    x33)^2 + (x146 - x173)^2 + (x286 - x313)^2) + 1 / sqrt((x6 - x34)^2 + (x146
    - x174)^2 + (x286 - x314)^2) + 1 / sqrt((x6 - x35)^2 + (x146 - x175)^2 + (
    x286 - x315)^2) + 1 / sqrt((x6 - x36)^2 + (x146 - x176)^2 + (x286 - x316)^2)
    + 1 / sqrt((x6 - x37)^2 + (x146 - x177)^2 + (x286 - x317)^2) + 1 / sqrt((
    x6 - x38)^2 + (x146 - x178)^2 + (x286 - x318)^2) + 1 / sqrt((x6 - x39)^2 +
    (x146 - x179)^2 + (x286 - x319)^2) + 1 / sqrt((x6 - x40)^2 + (x146 - x180)^
    2 + (x286 - x320)^2) + 1 / sqrt((x6 - x41)^2 + (x146 - x181)^2 + (x286 -
    x321)^2) + 1 / sqrt((x6 - x42)^2 + (x146 - x182)^2 + (x286 - x322)^2) + 1
    / sqrt((x6 - x43)^2 + (x146 - x183)^2 + (x286 - x323)^2) + 1 / sqrt((x6 -
    x44)^2 + (x146 - x184)^2 + (x286 - x324)^2) + 1 / sqrt((x6 - x45)^2 + (x146
    - x185)^2 + (x286 - x325)^2) + 1 / sqrt((x6 - x46)^2 + (x146 - x186)^2 + (
    x286 - x326)^2) + 1 / sqrt((x6 - x47)^2 + (x146 - x187)^2 + (x286 - x327)^2)
    + 1 / sqrt((x6 - x48)^2 + (x146 - x188)^2 + (x286 - x328)^2) + 1 / sqrt((
    x6 - x49)^2 + (x146 - x189)^2 + (x286 - x329)^2) + 1 / sqrt((x6 - x50)^2 +
    (x146 - x190)^2 + (x286 - x330)^2) + 1 / sqrt((x6 - x51)^2 + (x146 - x191)^
    2 + (x286 - x331)^2) + 1 / sqrt((x6 - x52)^2 + (x146 - x192)^2 + (x286 -
    x332)^2) + 1 / sqrt((x6 - x53)^2 + (x146 - x193)^2 + (x286 - x333)^2) + 1
    / sqrt((x6 - x54)^2 + (x146 - x194)^2 + (x286 - x334)^2) + 1 / sqrt((x6 -
    x55)^2 + (x146 - x195)^2 + (x286 - x335)^2) + 1 / sqrt((x6 - x56)^2 + (x146
    - x196)^2 + (x286 - x336)^2) + 1 / sqrt((x6 - x57)^2 + (x146 - x197)^2 + (
    x286 - x337)^2) + 1 / sqrt((x6 - x58)^2 + (x146 - x198)^2 + (x286 - x338)^2)
    + 1 / sqrt((x6 - x59)^2 + (x146 - x199)^2 + (x286 - x339)^2) + 1 / sqrt((
    x6 - x60)^2 + (x146 - x200)^2 + (x286 - x340)^2) + 1 / sqrt((x6 - x61)^2 +
    (x146 - x201)^2 + (x286 - x341)^2) + 1 / sqrt((x6 - x62)^2 + (x146 - x202)^
    2 + (x286 - x342)^2) + 1 / sqrt((x6 - x63)^2 + (x146 - x203)^2 + (x286 -
    x343)^2) + 1 / sqrt((x6 - x64)^2 + (x146 - x204)^2 + (x286 - x344)^2) + 1
    / sqrt((x6 - x65)^2 + (x146 - x205)^2 + (x286 - x345)^2) + 1 / sqrt((x6 -
    x66)^2 + (x146 - x206)^2 + (x286 - x346)^2) + 1 / sqrt((x6 - x67)^2 + (x146
    - x207)^2 + (x286 - x347)^2) + 1 / sqrt((x6 - x68)^2 + (x146 - x208)^2 + (
    x286 - x348)^2) + 1 / sqrt((x6 - x69)^2 + (x146 - x209)^2 + (x286 - x349)^2)
    + 1 / sqrt((x6 - x70)^2 + (x146 - x210)^2 + (x286 - x350)^2) + 1 / sqrt((
    x6 - x71)^2 + (x146 - x211)^2 + (x286 - x351)^2) + 1 / sqrt((x6 - x72)^2 +
    (x146 - x212)^2 + (x286 - x352)^2) + 1 / sqrt((x6 - x73)^2 + (x146 - x213)^
    2 + (x286 - x353)^2) + 1 / sqrt((x6 - x74)^2 + (x146 - x214)^2 + (x286 -
    x354)^2) + 1 / sqrt((x6 - x75)^2 + (x146 - x215)^2 + (x286 - x355)^2) + 1
    / sqrt((x6 - x76)^2 + (x146 - x216)^2 + (x286 - x356)^2) + 1 / sqrt((x6 -
    x77)^2 + (x146 - x217)^2 + (x286 - x357)^2) + 1 / sqrt((x6 - x78)^2 + (x146
    - x218)^2 + (x286 - x358)^2) + 1 / sqrt((x6 - x79)^2 + (x146 - x219)^2 + (
    x286 - x359)^2) + 1 / sqrt((x6 - x80)^2 + (x146 - x220)^2 + (x286 - x360)^2)
    + 1 / sqrt((x6 - x81)^2 + (x146 - x221)^2 + (x286 - x361)^2) + 1 / sqrt((
    x6 - x82)^2 + (x146 - x222)^2 + (x286 - x362)^2) + 1 / sqrt((x6 - x83)^2 +
    (x146 - x223)^2 + (x286 - x363)^2) + 1 / sqrt((x6 - x84)^2 + (x146 - x224)^
    2 + (x286 - x364)^2) + 1 / sqrt((x6 - x85)^2 + (x146 - x225)^2 + (x286 -
    x365)^2) + 1 / sqrt((x6 - x86)^2 + (x146 - x226)^2 + (x286 - x366)^2) + 1
    / sqrt((x6 - x87)^2 + (x146 - x227)^2 + (x286 - x367)^2) + 1 / sqrt((x6 -
    x88)^2 + (x146 - x228)^2 + (x286 - x368)^2) + 1 / sqrt((x6 - x89)^2 + (x146
    - x229)^2 + (x286 - x369)^2) + 1 / sqrt((x6 - x90)^2 + (x146 - x230)^2 + (
    x286 - x370)^2) + 1 / sqrt((x6 - x91)^2 + (x146 - x231)^2 + (x286 - x371)^2)
    + 1 / sqrt((x6 - x92)^2 + (x146 - x232)^2 + (x286 - x372)^2) + 1 / sqrt((
    x6 - x93)^2 + (x146 - x233)^2 + (x286 - x373)^2) + 1 / sqrt((x6 - x94)^2 +
    (x146 - x234)^2 + (x286 - x374)^2) + 1 / sqrt((x6 - x95)^2 + (x146 - x235)^
    2 + (x286 - x375)^2) + 1 / sqrt((x6 - x96)^2 + (x146 - x236)^2 + (x286 -
    x376)^2) + 1 / sqrt((x6 - x97)^2 + (x146 - x237)^2 + (x286 - x377)^2) + 1
    / sqrt((x6 - x98)^2 + (x146 - x238)^2 + (x286 - x378)^2) + 1 / sqrt((x6 -
    x99)^2 + (x146 - x239)^2 + (x286 - x379)^2) + 1 / sqrt((x6 - x100)^2 + (
    x146 - x240)^2 + (x286 - x380)^2) + 1 / sqrt((x6 - x101)^2 + (x146 - x241)^
    2 + (x286 - x381)^2) + 1 / sqrt((x6 - x102)^2 + (x146 - x242)^2 + (x286 -
    x382)^2) + 1 / sqrt((x6 - x103)^2 + (x146 - x243)^2 + (x286 - x383)^2) + 1
    / sqrt((x6 - x104)^2 + (x146 - x244)^2 + (x286 - x384)^2) + 1 / sqrt((x6
    - x105)^2 + (x146 - x245)^2 + (x286 - x385)^2) + 1 / sqrt((x6 - x106)^2 +
    (x146 - x246)^2 + (x286 - x386)^2) + 1 / sqrt((x6 - x107)^2 + (x146 - x247)
    ^2 + (x286 - x387)^2) + 1 / sqrt((x6 - x108)^2 + (x146 - x248)^2 + (x286 -
    x388)^2) + 1 / sqrt((x6 - x109)^2 + (x146 - x249)^2 + (x286 - x389)^2) + 1
    / sqrt((x6 - x110)^2 + (x146 - x250)^2 + (x286 - x390)^2) + 1 / sqrt((x6
    - x111)^2 + (x146 - x251)^2 + (x286 - x391)^2) + 1 / sqrt((x6 - x112)^2 +
    (x146 - x252)^2 + (x286 - x392)^2) + 1 / sqrt((x6 - x113)^2 + (x146 - x253)
    ^2 + (x286 - x393)^2) + 1 / sqrt((x6 - x114)^2 + (x146 - x254)^2 + (x286 -
    x394)^2) + 1 / sqrt((x6 - x115)^2 + (x146 - x255)^2 + (x286 - x395)^2) + 1
    / sqrt((x6 - x116)^2 + (x146 - x256)^2 + (x286 - x396)^2) + 1 / sqrt((x6
    - x117)^2 + (x146 - x257)^2 + (x286 - x397)^2) + 1 / sqrt((x6 - x118)^2 +
    (x146 - x258)^2 + (x286 - x398)^2) + 1 / sqrt((x6 - x119)^2 + (x146 - x259)
    ^2 + (x286 - x399)^2) + 1 / sqrt((x6 - x120)^2 + (x146 - x260)^2 + (x286 -
    x400)^2) + 1 / sqrt((x6 - x121)^2 + (x146 - x261)^2 + (x286 - x401)^2) + 1
    / sqrt((x6 - x122)^2 + (x146 - x262)^2 + (x286 - x402)^2) + 1 / sqrt((x6
    - x123)^2 + (x146 - x263)^2 + (x286 - x403)^2) + 1 / sqrt((x6 - x124)^2 +
    (x146 - x264)^2 + (x286 - x404)^2) + 1 / sqrt((x6 - x125)^2 + (x146 - x265)
    ^2 + (x286 - x405)^2) + 1 / sqrt((x6 - x126)^2 + (x146 - x266)^2 + (x286 -
    x406)^2) + 1 / sqrt((x6 - x127)^2 + (x146 - x267)^2 + (x286 - x407)^2) + 1
    / sqrt((x6 - x128)^2 + (x146 - x268)^2 + (x286 - x408)^2) + 1 / sqrt((x6
    - x129)^2 + (x146 - x269)^2 + (x286 - x409)^2) + 1 / sqrt((x6 - x130)^2 +
    (x146 - x270)^2 + (x286 - x410)^2) + 1 / sqrt((x6 - x131)^2 + (x146 - x271)
    ^2 + (x286 - x411)^2) + 1 / sqrt((x6 - x132)^2 + (x146 - x272)^2 + (x286 -
    x412)^2) + 1 / sqrt((x6 - x133)^2 + (x146 - x273)^2 + (x286 - x413)^2) + 1
    / sqrt((x6 - x134)^2 + (x146 - x274)^2 + (x286 - x414)^2) + 1 / sqrt((x6
    - x135)^2 + (x146 - x275)^2 + (x286 - x415)^2) + 1 / sqrt((x6 - x136)^2 +
    (x146 - x276)^2 + (x286 - x416)^2) + 1 / sqrt((x6 - x137)^2 + (x146 - x277)
    ^2 + (x286 - x417)^2) + 1 / sqrt((x6 - x138)^2 + (x146 - x278)^2 + (x286 -
    x418)^2) + 1 / sqrt((x6 - x139)^2 + (x146 - x279)^2 + (x286 - x419)^2) + 1
    / sqrt((x6 - x140)^2 + (x146 - x280)^2 + (x286 - x420)^2) + 1 / sqrt((x7
    - x8)^2 + (x147 - x148)^2 + (x287 - x288)^2) + 1 / sqrt((x7 - x9)^2 + (
    x147 - x149)^2 + (x287 - x289)^2) + 1 / sqrt((x7 - x10)^2 + (x147 - x150)^2
    + (x287 - x290)^2) + 1 / sqrt((x7 - x11)^2 + (x147 - x151)^2 + (x287 -
    x291)^2) + 1 / sqrt((x7 - x12)^2 + (x147 - x152)^2 + (x287 - x292)^2) + 1
    / sqrt((x7 - x13)^2 + (x147 - x153)^2 + (x287 - x293)^2) + 1 / sqrt((x7 -
    x14)^2 + (x147 - x154)^2 + (x287 - x294)^2) + 1 / sqrt((x7 - x15)^2 + (x147
    - x155)^2 + (x287 - x295)^2) + 1 / sqrt((x7 - x16)^2 + (x147 - x156)^2 + (
    x287 - x296)^2) + 1 / sqrt((x7 - x17)^2 + (x147 - x157)^2 + (x287 - x297)^2)
    + 1 / sqrt((x7 - x18)^2 + (x147 - x158)^2 + (x287 - x298)^2) + 1 / sqrt((
    x7 - x19)^2 + (x147 - x159)^2 + (x287 - x299)^2) + 1 / sqrt((x7 - x20)^2 +
    (x147 - x160)^2 + (x287 - x300)^2) + 1 / sqrt((x7 - x21)^2 + (x147 - x161)^
    2 + (x287 - x301)^2) + 1 / sqrt((x7 - x22)^2 + (x147 - x162)^2 + (x287 -
    x302)^2) + 1 / sqrt((x7 - x23)^2 + (x147 - x163)^2 + (x287 - x303)^2) + 1
    / sqrt((x7 - x24)^2 + (x147 - x164)^2 + (x287 - x304)^2) + 1 / sqrt((x7 -
    x25)^2 + (x147 - x165)^2 + (x287 - x305)^2) + 1 / sqrt((x7 - x26)^2 + (x147
    - x166)^2 + (x287 - x306)^2) + 1 / sqrt((x7 - x27)^2 + (x147 - x167)^2 + (
    x287 - x307)^2) + 1 / sqrt((x7 - x28)^2 + (x147 - x168)^2 + (x287 - x308)^2)
    + 1 / sqrt((x7 - x29)^2 + (x147 - x169)^2 + (x287 - x309)^2) + 1 / sqrt((
    x7 - x30)^2 + (x147 - x170)^2 + (x287 - x310)^2) + 1 / sqrt((x7 - x31)^2 +
    (x147 - x171)^2 + (x287 - x311)^2) + 1 / sqrt((x7 - x32)^2 + (x147 - x172)^
    2 + (x287 - x312)^2) + 1 / sqrt((x7 - x33)^2 + (x147 - x173)^2 + (x287 -
    x313)^2) + 1 / sqrt((x7 - x34)^2 + (x147 - x174)^2 + (x287 - x314)^2) + 1
    / sqrt((x7 - x35)^2 + (x147 - x175)^2 + (x287 - x315)^2) + 1 / sqrt((x7 -
    x36)^2 + (x147 - x176)^2 + (x287 - x316)^2) + 1 / sqrt((x7 - x37)^2 + (x147
    - x177)^2 + (x287 - x317)^2) + 1 / sqrt((x7 - x38)^2 + (x147 - x178)^2 + (
    x287 - x318)^2) + 1 / sqrt((x7 - x39)^2 + (x147 - x179)^2 + (x287 - x319)^2)
    + 1 / sqrt((x7 - x40)^2 + (x147 - x180)^2 + (x287 - x320)^2) + 1 / sqrt((
    x7 - x41)^2 + (x147 - x181)^2 + (x287 - x321)^2) + 1 / sqrt((x7 - x42)^2 +
    (x147 - x182)^2 + (x287 - x322)^2) + 1 / sqrt((x7 - x43)^2 + (x147 - x183)^
    2 + (x287 - x323)^2) + 1 / sqrt((x7 - x44)^2 + (x147 - x184)^2 + (x287 -
    x324)^2) + 1 / sqrt((x7 - x45)^2 + (x147 - x185)^2 + (x287 - x325)^2) + 1
    / sqrt((x7 - x46)^2 + (x147 - x186)^2 + (x287 - x326)^2) + 1 / sqrt((x7 -
    x47)^2 + (x147 - x187)^2 + (x287 - x327)^2) + 1 / sqrt((x7 - x48)^2 + (x147
    - x188)^2 + (x287 - x328)^2) + 1 / sqrt((x7 - x49)^2 + (x147 - x189)^2 + (
    x287 - x329)^2) + 1 / sqrt((x7 - x50)^2 + (x147 - x190)^2 + (x287 - x330)^2)
    + 1 / sqrt((x7 - x51)^2 + (x147 - x191)^2 + (x287 - x331)^2) + 1 / sqrt((
    x7 - x52)^2 + (x147 - x192)^2 + (x287 - x332)^2) + 1 / sqrt((x7 - x53)^2 +
    (x147 - x193)^2 + (x287 - x333)^2) + 1 / sqrt((x7 - x54)^2 + (x147 - x194)^
    2 + (x287 - x334)^2) + 1 / sqrt((x7 - x55)^2 + (x147 - x195)^2 + (x287 -
    x335)^2) + 1 / sqrt((x7 - x56)^2 + (x147 - x196)^2 + (x287 - x336)^2) + 1
    / sqrt((x7 - x57)^2 + (x147 - x197)^2 + (x287 - x337)^2) + 1 / sqrt((x7 -
    x58)^2 + (x147 - x198)^2 + (x287 - x338)^2) + 1 / sqrt((x7 - x59)^2 + (x147
    - x199)^2 + (x287 - x339)^2) + 1 / sqrt((x7 - x60)^2 + (x147 - x200)^2 + (
    x287 - x340)^2) + 1 / sqrt((x7 - x61)^2 + (x147 - x201)^2 + (x287 - x341)^2)
    + 1 / sqrt((x7 - x62)^2 + (x147 - x202)^2 + (x287 - x342)^2) + 1 / sqrt((
    x7 - x63)^2 + (x147 - x203)^2 + (x287 - x343)^2) + 1 / sqrt((x7 - x64)^2 +
    (x147 - x204)^2 + (x287 - x344)^2) + 1 / sqrt((x7 - x65)^2 + (x147 - x205)^
    2 + (x287 - x345)^2) + 1 / sqrt((x7 - x66)^2 + (x147 - x206)^2 + (x287 -
    x346)^2) + 1 / sqrt((x7 - x67)^2 + (x147 - x207)^2 + (x287 - x347)^2) + 1
    / sqrt((x7 - x68)^2 + (x147 - x208)^2 + (x287 - x348)^2) + 1 / sqrt((x7 -
    x69)^2 + (x147 - x209)^2 + (x287 - x349)^2) + 1 / sqrt((x7 - x70)^2 + (x147
    - x210)^2 + (x287 - x350)^2) + 1 / sqrt((x7 - x71)^2 + (x147 - x211)^2 + (
    x287 - x351)^2) + 1 / sqrt((x7 - x72)^2 + (x147 - x212)^2 + (x287 - x352)^2)
    + 1 / sqrt((x7 - x73)^2 + (x147 - x213)^2 + (x287 - x353)^2) + 1 / sqrt((
    x7 - x74)^2 + (x147 - x214)^2 + (x287 - x354)^2) + 1 / sqrt((x7 - x75)^2 +
    (x147 - x215)^2 + (x287 - x355)^2) + 1 / sqrt((x7 - x76)^2 + (x147 - x216)^
    2 + (x287 - x356)^2) + 1 / sqrt((x7 - x77)^2 + (x147 - x217)^2 + (x287 -
    x357)^2) + 1 / sqrt((x7 - x78)^2 + (x147 - x218)^2 + (x287 - x358)^2) + 1
    / sqrt((x7 - x79)^2 + (x147 - x219)^2 + (x287 - x359)^2) + 1 / sqrt((x7 -
    x80)^2 + (x147 - x220)^2 + (x287 - x360)^2) + 1 / sqrt((x7 - x81)^2 + (x147
    - x221)^2 + (x287 - x361)^2) + 1 / sqrt((x7 - x82)^2 + (x147 - x222)^2 + (
    x287 - x362)^2) + 1 / sqrt((x7 - x83)^2 + (x147 - x223)^2 + (x287 - x363)^2)
    + 1 / sqrt((x7 - x84)^2 + (x147 - x224)^2 + (x287 - x364)^2) + 1 / sqrt((
    x7 - x85)^2 + (x147 - x225)^2 + (x287 - x365)^2) + 1 / sqrt((x7 - x86)^2 +
    (x147 - x226)^2 + (x287 - x366)^2) + 1 / sqrt((x7 - x87)^2 + (x147 - x227)^
    2 + (x287 - x367)^2) + 1 / sqrt((x7 - x88)^2 + (x147 - x228)^2 + (x287 -
    x368)^2) + 1 / sqrt((x7 - x89)^2 + (x147 - x229)^2 + (x287 - x369)^2) + 1
    / sqrt((x7 - x90)^2 + (x147 - x230)^2 + (x287 - x370)^2) + 1 / sqrt((x7 -
    x91)^2 + (x147 - x231)^2 + (x287 - x371)^2) + 1 / sqrt((x7 - x92)^2 + (x147
    - x232)^2 + (x287 - x372)^2) + 1 / sqrt((x7 - x93)^2 + (x147 - x233)^2 + (
    x287 - x373)^2) + 1 / sqrt((x7 - x94)^2 + (x147 - x234)^2 + (x287 - x374)^2)
    + 1 / sqrt((x7 - x95)^2 + (x147 - x235)^2 + (x287 - x375)^2) + 1 / sqrt((
    x7 - x96)^2 + (x147 - x236)^2 + (x287 - x376)^2) + 1 / sqrt((x7 - x97)^2 +
    (x147 - x237)^2 + (x287 - x377)^2) + 1 / sqrt((x7 - x98)^2 + (x147 - x238)^
    2 + (x287 - x378)^2) + 1 / sqrt((x7 - x99)^2 + (x147 - x239)^2 + (x287 -
    x379)^2) + 1 / sqrt((x7 - x100)^2 + (x147 - x240)^2 + (x287 - x380)^2) + 1
    / sqrt((x7 - x101)^2 + (x147 - x241)^2 + (x287 - x381)^2) + 1 / sqrt((x7
    - x102)^2 + (x147 - x242)^2 + (x287 - x382)^2) + 1 / sqrt((x7 - x103)^2 +
    (x147 - x243)^2 + (x287 - x383)^2) + 1 / sqrt((x7 - x104)^2 + (x147 - x244)
    ^2 + (x287 - x384)^2) + 1 / sqrt((x7 - x105)^2 + (x147 - x245)^2 + (x287 -
    x385)^2) + 1 / sqrt((x7 - x106)^2 + (x147 - x246)^2 + (x287 - x386)^2) + 1
    / sqrt((x7 - x107)^2 + (x147 - x247)^2 + (x287 - x387)^2) + 1 / sqrt((x7
    - x108)^2 + (x147 - x248)^2 + (x287 - x388)^2) + 1 / sqrt((x7 - x109)^2 +
    (x147 - x249)^2 + (x287 - x389)^2) + 1 / sqrt((x7 - x110)^2 + (x147 - x250)
    ^2 + (x287 - x390)^2) + 1 / sqrt((x7 - x111)^2 + (x147 - x251)^2 + (x287 -
    x391)^2) + 1 / sqrt((x7 - x112)^2 + (x147 - x252)^2 + (x287 - x392)^2) + 1
    / sqrt((x7 - x113)^2 + (x147 - x253)^2 + (x287 - x393)^2) + 1 / sqrt((x7
    - x114)^2 + (x147 - x254)^2 + (x287 - x394)^2) + 1 / sqrt((x7 - x115)^2 +
    (x147 - x255)^2 + (x287 - x395)^2) + 1 / sqrt((x7 - x116)^2 + (x147 - x256)
    ^2 + (x287 - x396)^2) + 1 / sqrt((x7 - x117)^2 + (x147 - x257)^2 + (x287 -
    x397)^2) + 1 / sqrt((x7 - x118)^2 + (x147 - x258)^2 + (x287 - x398)^2) + 1
    / sqrt((x7 - x119)^2 + (x147 - x259)^2 + (x287 - x399)^2) + 1 / sqrt((x7
    - x120)^2 + (x147 - x260)^2 + (x287 - x400)^2) + 1 / sqrt((x7 - x121)^2 +
    (x147 - x261)^2 + (x287 - x401)^2) + 1 / sqrt((x7 - x122)^2 + (x147 - x262)
    ^2 + (x287 - x402)^2) + 1 / sqrt((x7 - x123)^2 + (x147 - x263)^2 + (x287 -
    x403)^2) + 1 / sqrt((x7 - x124)^2 + (x147 - x264)^2 + (x287 - x404)^2) + 1
    / sqrt((x7 - x125)^2 + (x147 - x265)^2 + (x287 - x405)^2) + 1 / sqrt((x7
    - x126)^2 + (x147 - x266)^2 + (x287 - x406)^2) + 1 / sqrt((x7 - x127)^2 +
    (x147 - x267)^2 + (x287 - x407)^2) + 1 / sqrt((x7 - x128)^2 + (x147 - x268)
    ^2 + (x287 - x408)^2) + 1 / sqrt((x7 - x129)^2 + (x147 - x269)^2 + (x287 -
    x409)^2) + 1 / sqrt((x7 - x130)^2 + (x147 - x270)^2 + (x287 - x410)^2) + 1
    / sqrt((x7 - x131)^2 + (x147 - x271)^2 + (x287 - x411)^2) + 1 / sqrt((x7
    - x132)^2 + (x147 - x272)^2 + (x287 - x412)^2) + 1 / sqrt((x7 - x133)^2 +
    (x147 - x273)^2 + (x287 - x413)^2) + 1 / sqrt((x7 - x134)^2 + (x147 - x274)
    ^2 + (x287 - x414)^2) + 1 / sqrt((x7 - x135)^2 + (x147 - x275)^2 + (x287 -
    x415)^2) + 1 / sqrt((x7 - x136)^2 + (x147 - x276)^2 + (x287 - x416)^2) + 1
    / sqrt((x7 - x137)^2 + (x147 - x277)^2 + (x287 - x417)^2) + 1 / sqrt((x7
    - x138)^2 + (x147 - x278)^2 + (x287 - x418)^2) + 1 / sqrt((x7 - x139)^2 +
    (x147 - x279)^2 + (x287 - x419)^2) + 1 / sqrt((x7 - x140)^2 + (x147 - x280)
    ^2 + (x287 - x420)^2) + 1 / sqrt((x8 - x9)^2 + (x148 - x149)^2 + (x288 -
    x289)^2) + 1 / sqrt((x8 - x10)^2 + (x148 - x150)^2 + (x288 - x290)^2) + 1
    / sqrt((x8 - x11)^2 + (x148 - x151)^2 + (x288 - x291)^2) + 1 / sqrt((x8 -
    x12)^2 + (x148 - x152)^2 + (x288 - x292)^2) + 1 / sqrt((x8 - x13)^2 + (x148
    - x153)^2 + (x288 - x293)^2) + 1 / sqrt((x8 - x14)^2 + (x148 - x154)^2 + (
    x288 - x294)^2) + 1 / sqrt((x8 - x15)^2 + (x148 - x155)^2 + (x288 - x295)^2)
    + 1 / sqrt((x8 - x16)^2 + (x148 - x156)^2 + (x288 - x296)^2) + 1 / sqrt((
    x8 - x17)^2 + (x148 - x157)^2 + (x288 - x297)^2) + 1 / sqrt((x8 - x18)^2 +
    (x148 - x158)^2 + (x288 - x298)^2) + 1 / sqrt((x8 - x19)^2 + (x148 - x159)^
    2 + (x288 - x299)^2) + 1 / sqrt((x8 - x20)^2 + (x148 - x160)^2 + (x288 -
    x300)^2) + 1 / sqrt((x8 - x21)^2 + (x148 - x161)^2 + (x288 - x301)^2) + 1
    / sqrt((x8 - x22)^2 + (x148 - x162)^2 + (x288 - x302)^2) + 1 / sqrt((x8 -
    x23)^2 + (x148 - x163)^2 + (x288 - x303)^2) + 1 / sqrt((x8 - x24)^2 + (x148
    - x164)^2 + (x288 - x304)^2) + 1 / sqrt((x8 - x25)^2 + (x148 - x165)^2 + (
    x288 - x305)^2) + 1 / sqrt((x8 - x26)^2 + (x148 - x166)^2 + (x288 - x306)^2)
    + 1 / sqrt((x8 - x27)^2 + (x148 - x167)^2 + (x288 - x307)^2) + 1 / sqrt((
    x8 - x28)^2 + (x148 - x168)^2 + (x288 - x308)^2) + 1 / sqrt((x8 - x29)^2 +
    (x148 - x169)^2 + (x288 - x309)^2) + 1 / sqrt((x8 - x30)^2 + (x148 - x170)^
    2 + (x288 - x310)^2) + 1 / sqrt((x8 - x31)^2 + (x148 - x171)^2 + (x288 -
    x311)^2) + 1 / sqrt((x8 - x32)^2 + (x148 - x172)^2 + (x288 - x312)^2) + 1
    / sqrt((x8 - x33)^2 + (x148 - x173)^2 + (x288 - x313)^2) + 1 / sqrt((x8 -
    x34)^2 + (x148 - x174)^2 + (x288 - x314)^2) + 1 / sqrt((x8 - x35)^2 + (x148
    - x175)^2 + (x288 - x315)^2) + 1 / sqrt((x8 - x36)^2 + (x148 - x176)^2 + (
    x288 - x316)^2) + 1 / sqrt((x8 - x37)^2 + (x148 - x177)^2 + (x288 - x317)^2)
    + 1 / sqrt((x8 - x38)^2 + (x148 - x178)^2 + (x288 - x318)^2) + 1 / sqrt((
    x8 - x39)^2 + (x148 - x179)^2 + (x288 - x319)^2) + 1 / sqrt((x8 - x40)^2 +
    (x148 - x180)^2 + (x288 - x320)^2) + 1 / sqrt((x8 - x41)^2 + (x148 - x181)^
    2 + (x288 - x321)^2) + 1 / sqrt((x8 - x42)^2 + (x148 - x182)^2 + (x288 -
    x322)^2) + 1 / sqrt((x8 - x43)^2 + (x148 - x183)^2 + (x288 - x323)^2) + 1
    / sqrt((x8 - x44)^2 + (x148 - x184)^2 + (x288 - x324)^2) + 1 / sqrt((x8 -
    x45)^2 + (x148 - x185)^2 + (x288 - x325)^2) + 1 / sqrt((x8 - x46)^2 + (x148
    - x186)^2 + (x288 - x326)^2) + 1 / sqrt((x8 - x47)^2 + (x148 - x187)^2 + (
    x288 - x327)^2) + 1 / sqrt((x8 - x48)^2 + (x148 - x188)^2 + (x288 - x328)^2)
    + 1 / sqrt((x8 - x49)^2 + (x148 - x189)^2 + (x288 - x329)^2) + 1 / sqrt((
    x8 - x50)^2 + (x148 - x190)^2 + (x288 - x330)^2) + 1 / sqrt((x8 - x51)^2 +
    (x148 - x191)^2 + (x288 - x331)^2) + 1 / sqrt((x8 - x52)^2 + (x148 - x192)^
    2 + (x288 - x332)^2) + 1 / sqrt((x8 - x53)^2 + (x148 - x193)^2 + (x288 -
    x333)^2) + 1 / sqrt((x8 - x54)^2 + (x148 - x194)^2 + (x288 - x334)^2) + 1
    / sqrt((x8 - x55)^2 + (x148 - x195)^2 + (x288 - x335)^2) + 1 / sqrt((x8 -
    x56)^2 + (x148 - x196)^2 + (x288 - x336)^2) + 1 / sqrt((x8 - x57)^2 + (x148
    - x197)^2 + (x288 - x337)^2) + 1 / sqrt((x8 - x58)^2 + (x148 - x198)^2 + (
    x288 - x338)^2) + 1 / sqrt((x8 - x59)^2 + (x148 - x199)^2 + (x288 - x339)^2)
    + 1 / sqrt((x8 - x60)^2 + (x148 - x200)^2 + (x288 - x340)^2) + 1 / sqrt((
    x8 - x61)^2 + (x148 - x201)^2 + (x288 - x341)^2) + 1 / sqrt((x8 - x62)^2 +
    (x148 - x202)^2 + (x288 - x342)^2) + 1 / sqrt((x8 - x63)^2 + (x148 - x203)^
    2 + (x288 - x343)^2) + 1 / sqrt((x8 - x64)^2 + (x148 - x204)^2 + (x288 -
    x344)^2) + 1 / sqrt((x8 - x65)^2 + (x148 - x205)^2 + (x288 - x345)^2) + 1
    / sqrt((x8 - x66)^2 + (x148 - x206)^2 + (x288 - x346)^2) + 1 / sqrt((x8 -
    x67)^2 + (x148 - x207)^2 + (x288 - x347)^2) + 1 / sqrt((x8 - x68)^2 + (x148
    - x208)^2 + (x288 - x348)^2) + 1 / sqrt((x8 - x69)^2 + (x148 - x209)^2 + (
    x288 - x349)^2) + 1 / sqrt((x8 - x70)^2 + (x148 - x210)^2 + (x288 - x350)^2)
    + 1 / sqrt((x8 - x71)^2 + (x148 - x211)^2 + (x288 - x351)^2) + 1 / sqrt((
    x8 - x72)^2 + (x148 - x212)^2 + (x288 - x352)^2) + 1 / sqrt((x8 - x73)^2 +
    (x148 - x213)^2 + (x288 - x353)^2) + 1 / sqrt((x8 - x74)^2 + (x148 - x214)^
    2 + (x288 - x354)^2) + 1 / sqrt((x8 - x75)^2 + (x148 - x215)^2 + (x288 -
    x355)^2) + 1 / sqrt((x8 - x76)^2 + (x148 - x216)^2 + (x288 - x356)^2) + 1
    / sqrt((x8 - x77)^2 + (x148 - x217)^2 + (x288 - x357)^2) + 1 / sqrt((x8 -
    x78)^2 + (x148 - x218)^2 + (x288 - x358)^2) + 1 / sqrt((x8 - x79)^2 + (x148
    - x219)^2 + (x288 - x359)^2) + 1 / sqrt((x8 - x80)^2 + (x148 - x220)^2 + (
    x288 - x360)^2) + 1 / sqrt((x8 - x81)^2 + (x148 - x221)^2 + (x288 - x361)^2)
    + 1 / sqrt((x8 - x82)^2 + (x148 - x222)^2 + (x288 - x362)^2) + 1 / sqrt((
    x8 - x83)^2 + (x148 - x223)^2 + (x288 - x363)^2) + 1 / sqrt((x8 - x84)^2 +
    (x148 - x224)^2 + (x288 - x364)^2) + 1 / sqrt((x8 - x85)^2 + (x148 - x225)^
    2 + (x288 - x365)^2) + 1 / sqrt((x8 - x86)^2 + (x148 - x226)^2 + (x288 -
    x366)^2) + 1 / sqrt((x8 - x87)^2 + (x148 - x227)^2 + (x288 - x367)^2) + 1
    / sqrt((x8 - x88)^2 + (x148 - x228)^2 + (x288 - x368)^2) + 1 / sqrt((x8 -
    x89)^2 + (x148 - x229)^2 + (x288 - x369)^2) + 1 / sqrt((x8 - x90)^2 + (x148
    - x230)^2 + (x288 - x370)^2) + 1 / sqrt((x8 - x91)^2 + (x148 - x231)^2 + (
    x288 - x371)^2) + 1 / sqrt((x8 - x92)^2 + (x148 - x232)^2 + (x288 - x372)^2)
    + 1 / sqrt((x8 - x93)^2 + (x148 - x233)^2 + (x288 - x373)^2) + 1 / sqrt((
    x8 - x94)^2 + (x148 - x234)^2 + (x288 - x374)^2) + 1 / sqrt((x8 - x95)^2 +
    (x148 - x235)^2 + (x288 - x375)^2) + 1 / sqrt((x8 - x96)^2 + (x148 - x236)^
    2 + (x288 - x376)^2) + 1 / sqrt((x8 - x97)^2 + (x148 - x237)^2 + (x288 -
    x377)^2) + 1 / sqrt((x8 - x98)^2 + (x148 - x238)^2 + (x288 - x378)^2) + 1
    / sqrt((x8 - x99)^2 + (x148 - x239)^2 + (x288 - x379)^2) + 1 / sqrt((x8 -
    x100)^2 + (x148 - x240)^2 + (x288 - x380)^2) + 1 / sqrt((x8 - x101)^2 + (
    x148 - x241)^2 + (x288 - x381)^2) + 1 / sqrt((x8 - x102)^2 + (x148 - x242)^
    2 + (x288 - x382)^2) + 1 / sqrt((x8 - x103)^2 + (x148 - x243)^2 + (x288 -
    x383)^2) + 1 / sqrt((x8 - x104)^2 + (x148 - x244)^2 + (x288 - x384)^2) + 1
    / sqrt((x8 - x105)^2 + (x148 - x245)^2 + (x288 - x385)^2) + 1 / sqrt((x8
    - x106)^2 + (x148 - x246)^2 + (x288 - x386)^2) + 1 / sqrt((x8 - x107)^2 +
    (x148 - x247)^2 + (x288 - x387)^2) + 1 / sqrt((x8 - x108)^2 + (x148 - x248)
    ^2 + (x288 - x388)^2) + 1 / sqrt((x8 - x109)^2 + (x148 - x249)^2 + (x288 -
    x389)^2) + 1 / sqrt((x8 - x110)^2 + (x148 - x250)^2 + (x288 - x390)^2) + 1
    / sqrt((x8 - x111)^2 + (x148 - x251)^2 + (x288 - x391)^2) + 1 / sqrt((x8
    - x112)^2 + (x148 - x252)^2 + (x288 - x392)^2) + 1 / sqrt((x8 - x113)^2 +
    (x148 - x253)^2 + (x288 - x393)^2) + 1 / sqrt((x8 - x114)^2 + (x148 - x254)
    ^2 + (x288 - x394)^2) + 1 / sqrt((x8 - x115)^2 + (x148 - x255)^2 + (x288 -
    x395)^2) + 1 / sqrt((x8 - x116)^2 + (x148 - x256)^2 + (x288 - x396)^2) + 1
    / sqrt((x8 - x117)^2 + (x148 - x257)^2 + (x288 - x397)^2) + 1 / sqrt((x8
    - x118)^2 + (x148 - x258)^2 + (x288 - x398)^2) + 1 / sqrt((x8 - x119)^2 +
    (x148 - x259)^2 + (x288 - x399)^2) + 1 / sqrt((x8 - x120)^2 + (x148 - x260)
    ^2 + (x288 - x400)^2) + 1 / sqrt((x8 - x121)^2 + (x148 - x261)^2 + (x288 -
    x401)^2) + 1 / sqrt((x8 - x122)^2 + (x148 - x262)^2 + (x288 - x402)^2) + 1
    / sqrt((x8 - x123)^2 + (x148 - x263)^2 + (x288 - x403)^2) + 1 / sqrt((x8
    - x124)^2 + (x148 - x264)^2 + (x288 - x404)^2) + 1 / sqrt((x8 - x125)^2 +
    (x148 - x265)^2 + (x288 - x405)^2) + 1 / sqrt((x8 - x126)^2 + (x148 - x266)
    ^2 + (x288 - x406)^2) + 1 / sqrt((x8 - x127)^2 + (x148 - x267)^2 + (x288 -
    x407)^2) + 1 / sqrt((x8 - x128)^2 + (x148 - x268)^2 + (x288 - x408)^2) + 1
    / sqrt((x8 - x129)^2 + (x148 - x269)^2 + (x288 - x409)^2) + 1 / sqrt((x8
    - x130)^2 + (x148 - x270)^2 + (x288 - x410)^2) + 1 / sqrt((x8 - x131)^2 +
    (x148 - x271)^2 + (x288 - x411)^2) + 1 / sqrt((x8 - x132)^2 + (x148 - x272)
    ^2 + (x288 - x412)^2) + 1 / sqrt((x8 - x133)^2 + (x148 - x273)^2 + (x288 -
    x413)^2) + 1 / sqrt((x8 - x134)^2 + (x148 - x274)^2 + (x288 - x414)^2) + 1
    / sqrt((x8 - x135)^2 + (x148 - x275)^2 + (x288 - x415)^2) + 1 / sqrt((x8
    - x136)^2 + (x148 - x276)^2 + (x288 - x416)^2) + 1 / sqrt((x8 - x137)^2 +
    (x148 - x277)^2 + (x288 - x417)^2) + 1 / sqrt((x8 - x138)^2 + (x148 - x278)
    ^2 + (x288 - x418)^2) + 1 / sqrt((x8 - x139)^2 + (x148 - x279)^2 + (x288 -
    x419)^2) + 1 / sqrt((x8 - x140)^2 + (x148 - x280)^2 + (x288 - x420)^2) + 1
    / sqrt((x9 - x10)^2 + (x149 - x150)^2 + (x289 - x290)^2) + 1 / sqrt((x9 -
    x11)^2 + (x149 - x151)^2 + (x289 - x291)^2) + 1 / sqrt((x9 - x12)^2 + (x149
    - x152)^2 + (x289 - x292)^2) + 1 / sqrt((x9 - x13)^2 + (x149 - x153)^2 + (
    x289 - x293)^2) + 1 / sqrt((x9 - x14)^2 + (x149 - x154)^2 + (x289 - x294)^2)
    + 1 / sqrt((x9 - x15)^2 + (x149 - x155)^2 + (x289 - x295)^2) + 1 / sqrt((
    x9 - x16)^2 + (x149 - x156)^2 + (x289 - x296)^2) + 1 / sqrt((x9 - x17)^2 +
    (x149 - x157)^2 + (x289 - x297)^2) + 1 / sqrt((x9 - x18)^2 + (x149 - x158)^
    2 + (x289 - x298)^2) + 1 / sqrt((x9 - x19)^2 + (x149 - x159)^2 + (x289 -
    x299)^2) + 1 / sqrt((x9 - x20)^2 + (x149 - x160)^2 + (x289 - x300)^2) + 1
    / sqrt((x9 - x21)^2 + (x149 - x161)^2 + (x289 - x301)^2) + 1 / sqrt((x9 -
    x22)^2 + (x149 - x162)^2 + (x289 - x302)^2) + 1 / sqrt((x9 - x23)^2 + (x149
    - x163)^2 + (x289 - x303)^2) + 1 / sqrt((x9 - x24)^2 + (x149 - x164)^2 + (
    x289 - x304)^2) + 1 / sqrt((x9 - x25)^2 + (x149 - x165)^2 + (x289 - x305)^2)
    + 1 / sqrt((x9 - x26)^2 + (x149 - x166)^2 + (x289 - x306)^2) + 1 / sqrt((
    x9 - x27)^2 + (x149 - x167)^2 + (x289 - x307)^2) + 1 / sqrt((x9 - x28)^2 +
    (x149 - x168)^2 + (x289 - x308)^2) + 1 / sqrt((x9 - x29)^2 + (x149 - x169)^
    2 + (x289 - x309)^2) + 1 / sqrt((x9 - x30)^2 + (x149 - x170)^2 + (x289 -
    x310)^2) + 1 / sqrt((x9 - x31)^2 + (x149 - x171)^2 + (x289 - x311)^2) + 1
    / sqrt((x9 - x32)^2 + (x149 - x172)^2 + (x289 - x312)^2) + 1 / sqrt((x9 -
    x33)^2 + (x149 - x173)^2 + (x289 - x313)^2) + 1 / sqrt((x9 - x34)^2 + (x149
    - x174)^2 + (x289 - x314)^2) + 1 / sqrt((x9 - x35)^2 + (x149 - x175)^2 + (
    x289 - x315)^2) + 1 / sqrt((x9 - x36)^2 + (x149 - x176)^2 + (x289 - x316)^2)
    + 1 / sqrt((x9 - x37)^2 + (x149 - x177)^2 + (x289 - x317)^2) + 1 / sqrt((
    x9 - x38)^2 + (x149 - x178)^2 + (x289 - x318)^2) + 1 / sqrt((x9 - x39)^2 +
    (x149 - x179)^2 + (x289 - x319)^2) + 1 / sqrt((x9 - x40)^2 + (x149 - x180)^
    2 + (x289 - x320)^2) + 1 / sqrt((x9 - x41)^2 + (x149 - x181)^2 + (x289 -
    x321)^2) + 1 / sqrt((x9 - x42)^2 + (x149 - x182)^2 + (x289 - x322)^2) + 1
    / sqrt((x9 - x43)^2 + (x149 - x183)^2 + (x289 - x323)^2) + 1 / sqrt((x9 -
    x44)^2 + (x149 - x184)^2 + (x289 - x324)^2) + 1 / sqrt((x9 - x45)^2 + (x149
    - x185)^2 + (x289 - x325)^2) + 1 / sqrt((x9 - x46)^2 + (x149 - x186)^2 + (
    x289 - x326)^2) + 1 / sqrt((x9 - x47)^2 + (x149 - x187)^2 + (x289 - x327)^2)
    + 1 / sqrt((x9 - x48)^2 + (x149 - x188)^2 + (x289 - x328)^2) + 1 / sqrt((
    x9 - x49)^2 + (x149 - x189)^2 + (x289 - x329)^2) + 1 / sqrt((x9 - x50)^2 +
    (x149 - x190)^2 + (x289 - x330)^2) + 1 / sqrt((x9 - x51)^2 + (x149 - x191)^
    2 + (x289 - x331)^2) + 1 / sqrt((x9 - x52)^2 + (x149 - x192)^2 + (x289 -
    x332)^2) + 1 / sqrt((x9 - x53)^2 + (x149 - x193)^2 + (x289 - x333)^2) + 1
    / sqrt((x9 - x54)^2 + (x149 - x194)^2 + (x289 - x334)^2) + 1 / sqrt((x9 -
    x55)^2 + (x149 - x195)^2 + (x289 - x335)^2) + 1 / sqrt((x9 - x56)^2 + (x149
    - x196)^2 + (x289 - x336)^2) + 1 / sqrt((x9 - x57)^2 + (x149 - x197)^2 + (
    x289 - x337)^2) + 1 / sqrt((x9 - x58)^2 + (x149 - x198)^2 + (x289 - x338)^2)
    + 1 / sqrt((x9 - x59)^2 + (x149 - x199)^2 + (x289 - x339)^2) + 1 / sqrt((
    x9 - x60)^2 + (x149 - x200)^2 + (x289 - x340)^2) + 1 / sqrt((x9 - x61)^2 +
    (x149 - x201)^2 + (x289 - x341)^2) + 1 / sqrt((x9 - x62)^2 + (x149 - x202)^
    2 + (x289 - x342)^2) + 1 / sqrt((x9 - x63)^2 + (x149 - x203)^2 + (x289 -
    x343)^2) + 1 / sqrt((x9 - x64)^2 + (x149 - x204)^2 + (x289 - x344)^2) + 1
    / sqrt((x9 - x65)^2 + (x149 - x205)^2 + (x289 - x345)^2) + 1 / sqrt((x9 -
    x66)^2 + (x149 - x206)^2 + (x289 - x346)^2) + 1 / sqrt((x9 - x67)^2 + (x149
    - x207)^2 + (x289 - x347)^2) + 1 / sqrt((x9 - x68)^2 + (x149 - x208)^2 + (
    x289 - x348)^2) + 1 / sqrt((x9 - x69)^2 + (x149 - x209)^2 + (x289 - x349)^2)
    + 1 / sqrt((x9 - x70)^2 + (x149 - x210)^2 + (x289 - x350)^2) + 1 / sqrt((
    x9 - x71)^2 + (x149 - x211)^2 + (x289 - x351)^2) + 1 / sqrt((x9 - x72)^2 +
    (x149 - x212)^2 + (x289 - x352)^2) + 1 / sqrt((x9 - x73)^2 + (x149 - x213)^
    2 + (x289 - x353)^2) + 1 / sqrt((x9 - x74)^2 + (x149 - x214)^2 + (x289 -
    x354)^2) + 1 / sqrt((x9 - x75)^2 + (x149 - x215)^2 + (x289 - x355)^2) + 1
    / sqrt((x9 - x76)^2 + (x149 - x216)^2 + (x289 - x356)^2) + 1 / sqrt((x9 -
    x77)^2 + (x149 - x217)^2 + (x289 - x357)^2) + 1 / sqrt((x9 - x78)^2 + (x149
    - x218)^2 + (x289 - x358)^2) + 1 / sqrt((x9 - x79)^2 + (x149 - x219)^2 + (
    x289 - x359)^2) + 1 / sqrt((x9 - x80)^2 + (x149 - x220)^2 + (x289 - x360)^2)
    + 1 / sqrt((x9 - x81)^2 + (x149 - x221)^2 + (x289 - x361)^2) + 1 / sqrt((
    x9 - x82)^2 + (x149 - x222)^2 + (x289 - x362)^2) + 1 / sqrt((x9 - x83)^2 +
    (x149 - x223)^2 + (x289 - x363)^2) + 1 / sqrt((x9 - x84)^2 + (x149 - x224)^
    2 + (x289 - x364)^2) + 1 / sqrt((x9 - x85)^2 + (x149 - x225)^2 + (x289 -
    x365)^2) + 1 / sqrt((x9 - x86)^2 + (x149 - x226)^2 + (x289 - x366)^2) + 1
    / sqrt((x9 - x87)^2 + (x149 - x227)^2 + (x289 - x367)^2) + 1 / sqrt((x9 -
    x88)^2 + (x149 - x228)^2 + (x289 - x368)^2) + 1 / sqrt((x9 - x89)^2 + (x149
    - x229)^2 + (x289 - x369)^2) + 1 / sqrt((x9 - x90)^2 + (x149 - x230)^2 + (
    x289 - x370)^2) + 1 / sqrt((x9 - x91)^2 + (x149 - x231)^2 + (x289 - x371)^2)
    + 1 / sqrt((x9 - x92)^2 + (x149 - x232)^2 + (x289 - x372)^2) + 1 / sqrt((
    x9 - x93)^2 + (x149 - x233)^2 + (x289 - x373)^2) + 1 / sqrt((x9 - x94)^2 +
    (x149 - x234)^2 + (x289 - x374)^2) + 1 / sqrt((x9 - x95)^2 + (x149 - x235)^
    2 + (x289 - x375)^2) + 1 / sqrt((x9 - x96)^2 + (x149 - x236)^2 + (x289 -
    x376)^2) + 1 / sqrt((x9 - x97)^2 + (x149 - x237)^2 + (x289 - x377)^2) + 1
    / sqrt((x9 - x98)^2 + (x149 - x238)^2 + (x289 - x378)^2) + 1 / sqrt((x9 -
    x99)^2 + (x149 - x239)^2 + (x289 - x379)^2) + 1 / sqrt((x9 - x100)^2 + (
    x149 - x240)^2 + (x289 - x380)^2) + 1 / sqrt((x9 - x101)^2 + (x149 - x241)^
    2 + (x289 - x381)^2) + 1 / sqrt((x9 - x102)^2 + (x149 - x242)^2 + (x289 -
    x382)^2) + 1 / sqrt((x9 - x103)^2 + (x149 - x243)^2 + (x289 - x383)^2) + 1
    / sqrt((x9 - x104)^2 + (x149 - x244)^2 + (x289 - x384)^2) + 1 / sqrt((x9
    - x105)^2 + (x149 - x245)^2 + (x289 - x385)^2) + 1 / sqrt((x9 - x106)^2 +
    (x149 - x246)^2 + (x289 - x386)^2) + 1 / sqrt((x9 - x107)^2 + (x149 - x247)
    ^2 + (x289 - x387)^2) + 1 / sqrt((x9 - x108)^2 + (x149 - x248)^2 + (x289 -
    x388)^2) + 1 / sqrt((x9 - x109)^2 + (x149 - x249)^2 + (x289 - x389)^2) + 1
    / sqrt((x9 - x110)^2 + (x149 - x250)^2 + (x289 - x390)^2) + 1 / sqrt((x9
    - x111)^2 + (x149 - x251)^2 + (x289 - x391)^2) + 1 / sqrt((x9 - x112)^2 +
    (x149 - x252)^2 + (x289 - x392)^2) + 1 / sqrt((x9 - x113)^2 + (x149 - x253)
    ^2 + (x289 - x393)^2) + 1 / sqrt((x9 - x114)^2 + (x149 - x254)^2 + (x289 -
    x394)^2) + 1 / sqrt((x9 - x115)^2 + (x149 - x255)^2 + (x289 - x395)^2) + 1
    / sqrt((x9 - x116)^2 + (x149 - x256)^2 + (x289 - x396)^2) + 1 / sqrt((x9
    - x117)^2 + (x149 - x257)^2 + (x289 - x397)^2) + 1 / sqrt((x9 - x118)^2 +
    (x149 - x258)^2 + (x289 - x398)^2) + 1 / sqrt((x9 - x119)^2 + (x149 - x259)
    ^2 + (x289 - x399)^2) + 1 / sqrt((x9 - x120)^2 + (x149 - x260)^2 + (x289 -
    x400)^2) + 1 / sqrt((x9 - x121)^2 + (x149 - x261)^2 + (x289 - x401)^2) + 1
    / sqrt((x9 - x122)^2 + (x149 - x262)^2 + (x289 - x402)^2) + 1 / sqrt((x9
    - x123)^2 + (x149 - x263)^2 + (x289 - x403)^2) + 1 / sqrt((x9 - x124)^2 +
    (x149 - x264)^2 + (x289 - x404)^2) + 1 / sqrt((x9 - x125)^2 + (x149 - x265)
    ^2 + (x289 - x405)^2) + 1 / sqrt((x9 - x126)^2 + (x149 - x266)^2 + (x289 -
    x406)^2) + 1 / sqrt((x9 - x127)^2 + (x149 - x267)^2 + (x289 - x407)^2) + 1
    / sqrt((x9 - x128)^2 + (x149 - x268)^2 + (x289 - x408)^2) + 1 / sqrt((x9
    - x129)^2 + (x149 - x269)^2 + (x289 - x409)^2) + 1 / sqrt((x9 - x130)^2 +
    (x149 - x270)^2 + (x289 - x410)^2) + 1 / sqrt((x9 - x131)^2 + (x149 - x271)
    ^2 + (x289 - x411)^2) + 1 / sqrt((x9 - x132)^2 + (x149 - x272)^2 + (x289 -
    x412)^2) + 1 / sqrt((x9 - x133)^2 + (x149 - x273)^2 + (x289 - x413)^2) + 1
    / sqrt((x9 - x134)^2 + (x149 - x274)^2 + (x289 - x414)^2) + 1 / sqrt((x9
    - x135)^2 + (x149 - x275)^2 + (x289 - x415)^2) + 1 / sqrt((x9 - x136)^2 +
    (x149 - x276)^2 + (x289 - x416)^2) + 1 / sqrt((x9 - x137)^2 + (x149 - x277)
    ^2 + (x289 - x417)^2) + 1 / sqrt((x9 - x138)^2 + (x149 - x278)^2 + (x289 -
    x418)^2) + 1 / sqrt((x9 - x139)^2 + (x149 - x279)^2 + (x289 - x419)^2) + 1
    / sqrt((x9 - x140)^2 + (x149 - x280)^2 + (x289 - x420)^2) + 1 / sqrt((x10
    - x11)^2 + (x150 - x151)^2 + (x290 - x291)^2) + 1 / sqrt((x10 - x12)^2 + (
    x150 - x152)^2 + (x290 - x292)^2) + 1 / sqrt((x10 - x13)^2 + (x150 - x153)^
    2 + (x290 - x293)^2) + 1 / sqrt((x10 - x14)^2 + (x150 - x154)^2 + (x290 -
    x294)^2) + 1 / sqrt((x10 - x15)^2 + (x150 - x155)^2 + (x290 - x295)^2) + 1
    / sqrt((x10 - x16)^2 + (x150 - x156)^2 + (x290 - x296)^2) + 1 / sqrt((x10
    - x17)^2 + (x150 - x157)^2 + (x290 - x297)^2) + 1 / sqrt((x10 - x18)^2 + (
    x150 - x158)^2 + (x290 - x298)^2) + 1 / sqrt((x10 - x19)^2 + (x150 - x159)^
    2 + (x290 - x299)^2) + 1 / sqrt((x10 - x20)^2 + (x150 - x160)^2 + (x290 -
    x300)^2) + 1 / sqrt((x10 - x21)^2 + (x150 - x161)^2 + (x290 - x301)^2) + 1
    / sqrt((x10 - x22)^2 + (x150 - x162)^2 + (x290 - x302)^2) + 1 / sqrt((x10
    - x23)^2 + (x150 - x163)^2 + (x290 - x303)^2) + 1 / sqrt((x10 - x24)^2 + (
    x150 - x164)^2 + (x290 - x304)^2) + 1 / sqrt((x10 - x25)^2 + (x150 - x165)^
    2 + (x290 - x305)^2) + 1 / sqrt((x10 - x26)^2 + (x150 - x166)^2 + (x290 -
    x306)^2) + 1 / sqrt((x10 - x27)^2 + (x150 - x167)^2 + (x290 - x307)^2) + 1
    / sqrt((x10 - x28)^2 + (x150 - x168)^2 + (x290 - x308)^2) + 1 / sqrt((x10
    - x29)^2 + (x150 - x169)^2 + (x290 - x309)^2) + 1 / sqrt((x10 - x30)^2 + (
    x150 - x170)^2 + (x290 - x310)^2) + 1 / sqrt((x10 - x31)^2 + (x150 - x171)^
    2 + (x290 - x311)^2) + 1 / sqrt((x10 - x32)^2 + (x150 - x172)^2 + (x290 -
    x312)^2) + 1 / sqrt((x10 - x33)^2 + (x150 - x173)^2 + (x290 - x313)^2) + 1
    / sqrt((x10 - x34)^2 + (x150 - x174)^2 + (x290 - x314)^2) + 1 / sqrt((x10
    - x35)^2 + (x150 - x175)^2 + (x290 - x315)^2) + 1 / sqrt((x10 - x36)^2 + (
    x150 - x176)^2 + (x290 - x316)^2) + 1 / sqrt((x10 - x37)^2 + (x150 - x177)^
    2 + (x290 - x317)^2) + 1 / sqrt((x10 - x38)^2 + (x150 - x178)^2 + (x290 -
    x318)^2) + 1 / sqrt((x10 - x39)^2 + (x150 - x179)^2 + (x290 - x319)^2) + 1
    / sqrt((x10 - x40)^2 + (x150 - x180)^2 + (x290 - x320)^2) + 1 / sqrt((x10
    - x41)^2 + (x150 - x181)^2 + (x290 - x321)^2) + 1 / sqrt((x10 - x42)^2 + (
    x150 - x182)^2 + (x290 - x322)^2) + 1 / sqrt((x10 - x43)^2 + (x150 - x183)^
    2 + (x290 - x323)^2) + 1 / sqrt((x10 - x44)^2 + (x150 - x184)^2 + (x290 -
    x324)^2) + 1 / sqrt((x10 - x45)^2 + (x150 - x185)^2 + (x290 - x325)^2) + 1
    / sqrt((x10 - x46)^2 + (x150 - x186)^2 + (x290 - x326)^2) + 1 / sqrt((x10
    - x47)^2 + (x150 - x187)^2 + (x290 - x327)^2) + 1 / sqrt((x10 - x48)^2 + (
    x150 - x188)^2 + (x290 - x328)^2) + 1 / sqrt((x10 - x49)^2 + (x150 - x189)^
    2 + (x290 - x329)^2) + 1 / sqrt((x10 - x50)^2 + (x150 - x190)^2 + (x290 -
    x330)^2) + 1 / sqrt((x10 - x51)^2 + (x150 - x191)^2 + (x290 - x331)^2) + 1
    / sqrt((x10 - x52)^2 + (x150 - x192)^2 + (x290 - x332)^2) + 1 / sqrt((x10
    - x53)^2 + (x150 - x193)^2 + (x290 - x333)^2) + 1 / sqrt((x10 - x54)^2 + (
    x150 - x194)^2 + (x290 - x334)^2) + 1 / sqrt((x10 - x55)^2 + (x150 - x195)^
    2 + (x290 - x335)^2) + 1 / sqrt((x10 - x56)^2 + (x150 - x196)^2 + (x290 -
    x336)^2) + 1 / sqrt((x10 - x57)^2 + (x150 - x197)^2 + (x290 - x337)^2) + 1
    / sqrt((x10 - x58)^2 + (x150 - x198)^2 + (x290 - x338)^2) + 1 / sqrt((x10
    - x59)^2 + (x150 - x199)^2 + (x290 - x339)^2) + 1 / sqrt((x10 - x60)^2 + (
    x150 - x200)^2 + (x290 - x340)^2) + 1 / sqrt((x10 - x61)^2 + (x150 - x201)^
    2 + (x290 - x341)^2) + 1 / sqrt((x10 - x62)^2 + (x150 - x202)^2 + (x290 -
    x342)^2) + 1 / sqrt((x10 - x63)^2 + (x150 - x203)^2 + (x290 - x343)^2) + 1
    / sqrt((x10 - x64)^2 + (x150 - x204)^2 + (x290 - x344)^2) + 1 / sqrt((x10
    - x65)^2 + (x150 - x205)^2 + (x290 - x345)^2) + 1 / sqrt((x10 - x66)^2 + (
    x150 - x206)^2 + (x290 - x346)^2) + 1 / sqrt((x10 - x67)^2 + (x150 - x207)^
    2 + (x290 - x347)^2) + 1 / sqrt((x10 - x68)^2 + (x150 - x208)^2 + (x290 -
    x348)^2) + 1 / sqrt((x10 - x69)^2 + (x150 - x209)^2 + (x290 - x349)^2) + 1
    / sqrt((x10 - x70)^2 + (x150 - x210)^2 + (x290 - x350)^2) + 1 / sqrt((x10
    - x71)^2 + (x150 - x211)^2 + (x290 - x351)^2) + 1 / sqrt((x10 - x72)^2 + (
    x150 - x212)^2 + (x290 - x352)^2) + 1 / sqrt((x10 - x73)^2 + (x150 - x213)^
    2 + (x290 - x353)^2) + 1 / sqrt((x10 - x74)^2 + (x150 - x214)^2 + (x290 -
    x354)^2) + 1 / sqrt((x10 - x75)^2 + (x150 - x215)^2 + (x290 - x355)^2) + 1
    / sqrt((x10 - x76)^2 + (x150 - x216)^2 + (x290 - x356)^2) + 1 / sqrt((x10
    - x77)^2 + (x150 - x217)^2 + (x290 - x357)^2) + 1 / sqrt((x10 - x78)^2 + (
    x150 - x218)^2 + (x290 - x358)^2) + 1 / sqrt((x10 - x79)^2 + (x150 - x219)^
    2 + (x290 - x359)^2) + 1 / sqrt((x10 - x80)^2 + (x150 - x220)^2 + (x290 -
    x360)^2) + 1 / sqrt((x10 - x81)^2 + (x150 - x221)^2 + (x290 - x361)^2) + 1
    / sqrt((x10 - x82)^2 + (x150 - x222)^2 + (x290 - x362)^2) + 1 / sqrt((x10
    - x83)^2 + (x150 - x223)^2 + (x290 - x363)^2) + 1 / sqrt((x10 - x84)^2 + (
    x150 - x224)^2 + (x290 - x364)^2) + 1 / sqrt((x10 - x85)^2 + (x150 - x225)^
    2 + (x290 - x365)^2) + 1 / sqrt((x10 - x86)^2 + (x150 - x226)^2 + (x290 -
    x366)^2) + 1 / sqrt((x10 - x87)^2 + (x150 - x227)^2 + (x290 - x367)^2) + 1
    / sqrt((x10 - x88)^2 + (x150 - x228)^2 + (x290 - x368)^2) + 1 / sqrt((x10
    - x89)^2 + (x150 - x229)^2 + (x290 - x369)^2) + 1 / sqrt((x10 - x90)^2 + (
    x150 - x230)^2 + (x290 - x370)^2) + 1 / sqrt((x10 - x91)^2 + (x150 - x231)^
    2 + (x290 - x371)^2) + 1 / sqrt((x10 - x92)^2 + (x150 - x232)^2 + (x290 -
    x372)^2) + 1 / sqrt((x10 - x93)^2 + (x150 - x233)^2 + (x290 - x373)^2) + 1
    / sqrt((x10 - x94)^2 + (x150 - x234)^2 + (x290 - x374)^2) + 1 / sqrt((x10
    - x95)^2 + (x150 - x235)^2 + (x290 - x375)^2) + 1 / sqrt((x10 - x96)^2 + (
    x150 - x236)^2 + (x290 - x376)^2) + 1 / sqrt((x10 - x97)^2 + (x150 - x237)^
    2 + (x290 - x377)^2) + 1 / sqrt((x10 - x98)^2 + (x150 - x238)^2 + (x290 -
    x378)^2) + 1 / sqrt((x10 - x99)^2 + (x150 - x239)^2 + (x290 - x379)^2) + 1
    / sqrt((x10 - x100)^2 + (x150 - x240)^2 + (x290 - x380)^2) + 1 / sqrt((x10
    - x101)^2 + (x150 - x241)^2 + (x290 - x381)^2) + 1 / sqrt((x10 - x102)^2
    + (x150 - x242)^2 + (x290 - x382)^2) + 1 / sqrt((x10 - x103)^2 + (x150 -
    x243)^2 + (x290 - x383)^2) + 1 / sqrt((x10 - x104)^2 + (x150 - x244)^2 + (
    x290 - x384)^2) + 1 / sqrt((x10 - x105)^2 + (x150 - x245)^2 + (x290 - x385)
    ^2) + 1 / sqrt((x10 - x106)^2 + (x150 - x246)^2 + (x290 - x386)^2) + 1 /
    sqrt((x10 - x107)^2 + (x150 - x247)^2 + (x290 - x387)^2) + 1 / sqrt((x10 -
    x108)^2 + (x150 - x248)^2 + (x290 - x388)^2) + 1 / sqrt((x10 - x109)^2 + (
    x150 - x249)^2 + (x290 - x389)^2) + 1 / sqrt((x10 - x110)^2 + (x150 - x250)
    ^2 + (x290 - x390)^2) + 1 / sqrt((x10 - x111)^2 + (x150 - x251)^2 + (x290
    - x391)^2) + 1 / sqrt((x10 - x112)^2 + (x150 - x252)^2 + (x290 - x392)^2)
    + 1 / sqrt((x10 - x113)^2 + (x150 - x253)^2 + (x290 - x393)^2) + 1 / sqrt(
    (x10 - x114)^2 + (x150 - x254)^2 + (x290 - x394)^2) + 1 / sqrt((x10 - x115)
    ^2 + (x150 - x255)^2 + (x290 - x395)^2) + 1 / sqrt((x10 - x116)^2 + (x150
    - x256)^2 + (x290 - x396)^2) + 1 / sqrt((x10 - x117)^2 + (x150 - x257)^2
    + (x290 - x397)^2) + 1 / sqrt((x10 - x118)^2 + (x150 - x258)^2 + (x290 -
    x398)^2) + 1 / sqrt((x10 - x119)^2 + (x150 - x259)^2 + (x290 - x399)^2) + 1
    / sqrt((x10 - x120)^2 + (x150 - x260)^2 + (x290 - x400)^2) + 1 / sqrt((x10
    - x121)^2 + (x150 - x261)^2 + (x290 - x401)^2) + 1 / sqrt((x10 - x122)^2
    + (x150 - x262)^2 + (x290 - x402)^2) + 1 / sqrt((x10 - x123)^2 + (x150 -
    x263)^2 + (x290 - x403)^2) + 1 / sqrt((x10 - x124)^2 + (x150 - x264)^2 + (
    x290 - x404)^2) + 1 / sqrt((x10 - x125)^2 + (x150 - x265)^2 + (x290 - x405)
    ^2) + 1 / sqrt((x10 - x126)^2 + (x150 - x266)^2 + (x290 - x406)^2) + 1 /
    sqrt((x10 - x127)^2 + (x150 - x267)^2 + (x290 - x407)^2) + 1 / sqrt((x10 -
    x128)^2 + (x150 - x268)^2 + (x290 - x408)^2) + 1 / sqrt((x10 - x129)^2 + (
    x150 - x269)^2 + (x290 - x409)^2) + 1 / sqrt((x10 - x130)^2 + (x150 - x270)
    ^2 + (x290 - x410)^2) + 1 / sqrt((x10 - x131)^2 + (x150 - x271)^2 + (x290
    - x411)^2) + 1 / sqrt((x10 - x132)^2 + (x150 - x272)^2 + (x290 - x412)^2)
    + 1 / sqrt((x10 - x133)^2 + (x150 - x273)^2 + (x290 - x413)^2) + 1 / sqrt(
    (x10 - x134)^2 + (x150 - x274)^2 + (x290 - x414)^2) + 1 / sqrt((x10 - x135)
    ^2 + (x150 - x275)^2 + (x290 - x415)^2) + 1 / sqrt((x10 - x136)^2 + (x150
    - x276)^2 + (x290 - x416)^2) + 1 / sqrt((x10 - x137)^2 + (x150 - x277)^2
    + (x290 - x417)^2) + 1 / sqrt((x10 - x138)^2 + (x150 - x278)^2 + (x290 -
    x418)^2) + 1 / sqrt((x10 - x139)^2 + (x150 - x279)^2 + (x290 - x419)^2) + 1
    / sqrt((x10 - x140)^2 + (x150 - x280)^2 + (x290 - x420)^2) + 1 / sqrt((x11
    - x12)^2 + (x151 - x152)^2 + (x291 - x292)^2) + 1 / sqrt((x11 - x13)^2 + (
    x151 - x153)^2 + (x291 - x293)^2) + 1 / sqrt((x11 - x14)^2 + (x151 - x154)^
    2 + (x291 - x294)^2) + 1 / sqrt((x11 - x15)^2 + (x151 - x155)^2 + (x291 -
    x295)^2) + 1 / sqrt((x11 - x16)^2 + (x151 - x156)^2 + (x291 - x296)^2) + 1
    / sqrt((x11 - x17)^2 + (x151 - x157)^2 + (x291 - x297)^2) + 1 / sqrt((x11
    - x18)^2 + (x151 - x158)^2 + (x291 - x298)^2) + 1 / sqrt((x11 - x19)^2 + (
    x151 - x159)^2 + (x291 - x299)^2) + 1 / sqrt((x11 - x20)^2 + (x151 - x160)^
    2 + (x291 - x300)^2) + 1 / sqrt((x11 - x21)^2 + (x151 - x161)^2 + (x291 -
    x301)^2) + 1 / sqrt((x11 - x22)^2 + (x151 - x162)^2 + (x291 - x302)^2) + 1
    / sqrt((x11 - x23)^2 + (x151 - x163)^2 + (x291 - x303)^2) + 1 / sqrt((x11
    - x24)^2 + (x151 - x164)^2 + (x291 - x304)^2) + 1 / sqrt((x11 - x25)^2 + (
    x151 - x165)^2 + (x291 - x305)^2) + 1 / sqrt((x11 - x26)^2 + (x151 - x166)^
    2 + (x291 - x306)^2) + 1 / sqrt((x11 - x27)^2 + (x151 - x167)^2 + (x291 -
    x307)^2) + 1 / sqrt((x11 - x28)^2 + (x151 - x168)^2 + (x291 - x308)^2) + 1
    / sqrt((x11 - x29)^2 + (x151 - x169)^2 + (x291 - x309)^2) + 1 / sqrt((x11
    - x30)^2 + (x151 - x170)^2 + (x291 - x310)^2) + 1 / sqrt((x11 - x31)^2 + (
    x151 - x171)^2 + (x291 - x311)^2) + 1 / sqrt((x11 - x32)^2 + (x151 - x172)^
    2 + (x291 - x312)^2) + 1 / sqrt((x11 - x33)^2 + (x151 - x173)^2 + (x291 -
    x313)^2) + 1 / sqrt((x11 - x34)^2 + (x151 - x174)^2 + (x291 - x314)^2) + 1
    / sqrt((x11 - x35)^2 + (x151 - x175)^2 + (x291 - x315)^2) + 1 / sqrt((x11
    - x36)^2 + (x151 - x176)^2 + (x291 - x316)^2) + 1 / sqrt((x11 - x37)^2 + (
    x151 - x177)^2 + (x291 - x317)^2) + 1 / sqrt((x11 - x38)^2 + (x151 - x178)^
    2 + (x291 - x318)^2) + 1 / sqrt((x11 - x39)^2 + (x151 - x179)^2 + (x291 -
    x319)^2) + 1 / sqrt((x11 - x40)^2 + (x151 - x180)^2 + (x291 - x320)^2) + 1
    / sqrt((x11 - x41)^2 + (x151 - x181)^2 + (x291 - x321)^2) + 1 / sqrt((x11
    - x42)^2 + (x151 - x182)^2 + (x291 - x322)^2) + 1 / sqrt((x11 - x43)^2 + (
    x151 - x183)^2 + (x291 - x323)^2) + 1 / sqrt((x11 - x44)^2 + (x151 - x184)^
    2 + (x291 - x324)^2) + 1 / sqrt((x11 - x45)^2 + (x151 - x185)^2 + (x291 -
    x325)^2) + 1 / sqrt((x11 - x46)^2 + (x151 - x186)^2 + (x291 - x326)^2) + 1
    / sqrt((x11 - x47)^2 + (x151 - x187)^2 + (x291 - x327)^2) + 1 / sqrt((x11
    - x48)^2 + (x151 - x188)^2 + (x291 - x328)^2) + 1 / sqrt((x11 - x49)^2 + (
    x151 - x189)^2 + (x291 - x329)^2) + 1 / sqrt((x11 - x50)^2 + (x151 - x190)^
    2 + (x291 - x330)^2) + 1 / sqrt((x11 - x51)^2 + (x151 - x191)^2 + (x291 -
    x331)^2) + 1 / sqrt((x11 - x52)^2 + (x151 - x192)^2 + (x291 - x332)^2) + 1
    / sqrt((x11 - x53)^2 + (x151 - x193)^2 + (x291 - x333)^2) + 1 / sqrt((x11
    - x54)^2 + (x151 - x194)^2 + (x291 - x334)^2) + 1 / sqrt((x11 - x55)^2 + (
    x151 - x195)^2 + (x291 - x335)^2) + 1 / sqrt((x11 - x56)^2 + (x151 - x196)^
    2 + (x291 - x336)^2) + 1 / sqrt((x11 - x57)^2 + (x151 - x197)^2 + (x291 -
    x337)^2) + 1 / sqrt((x11 - x58)^2 + (x151 - x198)^2 + (x291 - x338)^2) + 1
    / sqrt((x11 - x59)^2 + (x151 - x199)^2 + (x291 - x339)^2) + 1 / sqrt((x11
    - x60)^2 + (x151 - x200)^2 + (x291 - x340)^2) + 1 / sqrt((x11 - x61)^2 + (
    x151 - x201)^2 + (x291 - x341)^2) + 1 / sqrt((x11 - x62)^2 + (x151 - x202)^
    2 + (x291 - x342)^2) + 1 / sqrt((x11 - x63)^2 + (x151 - x203)^2 + (x291 -
    x343)^2) + 1 / sqrt((x11 - x64)^2 + (x151 - x204)^2 + (x291 - x344)^2) + 1
    / sqrt((x11 - x65)^2 + (x151 - x205)^2 + (x291 - x345)^2) + 1 / sqrt((x11
    - x66)^2 + (x151 - x206)^2 + (x291 - x346)^2) + 1 / sqrt((x11 - x67)^2 + (
    x151 - x207)^2 + (x291 - x347)^2) + 1 / sqrt((x11 - x68)^2 + (x151 - x208)^
    2 + (x291 - x348)^2) + 1 / sqrt((x11 - x69)^2 + (x151 - x209)^2 + (x291 -
    x349)^2) + 1 / sqrt((x11 - x70)^2 + (x151 - x210)^2 + (x291 - x350)^2) + 1
    / sqrt((x11 - x71)^2 + (x151 - x211)^2 + (x291 - x351)^2) + 1 / sqrt((x11
    - x72)^2 + (x151 - x212)^2 + (x291 - x352)^2) + 1 / sqrt((x11 - x73)^2 + (
    x151 - x213)^2 + (x291 - x353)^2) + 1 / sqrt((x11 - x74)^2 + (x151 - x214)^
    2 + (x291 - x354)^2) + 1 / sqrt((x11 - x75)^2 + (x151 - x215)^2 + (x291 -
    x355)^2) + 1 / sqrt((x11 - x76)^2 + (x151 - x216)^2 + (x291 - x356)^2) + 1
    / sqrt((x11 - x77)^2 + (x151 - x217)^2 + (x291 - x357)^2) + 1 / sqrt((x11
    - x78)^2 + (x151 - x218)^2 + (x291 - x358)^2) + 1 / sqrt((x11 - x79)^2 + (
    x151 - x219)^2 + (x291 - x359)^2) + 1 / sqrt((x11 - x80)^2 + (x151 - x220)^
    2 + (x291 - x360)^2) + 1 / sqrt((x11 - x81)^2 + (x151 - x221)^2 + (x291 -
    x361)^2) + 1 / sqrt((x11 - x82)^2 + (x151 - x222)^2 + (x291 - x362)^2) + 1
    / sqrt((x11 - x83)^2 + (x151 - x223)^2 + (x291 - x363)^2) + 1 / sqrt((x11
    - x84)^2 + (x151 - x224)^2 + (x291 - x364)^2) + 1 / sqrt((x11 - x85)^2 + (
    x151 - x225)^2 + (x291 - x365)^2) + 1 / sqrt((x11 - x86)^2 + (x151 - x226)^
    2 + (x291 - x366)^2) + 1 / sqrt((x11 - x87)^2 + (x151 - x227)^2 + (x291 -
    x367)^2) + 1 / sqrt((x11 - x88)^2 + (x151 - x228)^2 + (x291 - x368)^2) + 1
    / sqrt((x11 - x89)^2 + (x151 - x229)^2 + (x291 - x369)^2) + 1 / sqrt((x11
    - x90)^2 + (x151 - x230)^2 + (x291 - x370)^2) + 1 / sqrt((x11 - x91)^2 + (
    x151 - x231)^2 + (x291 - x371)^2) + 1 / sqrt((x11 - x92)^2 + (x151 - x232)^
    2 + (x291 - x372)^2) + 1 / sqrt((x11 - x93)^2 + (x151 - x233)^2 + (x291 -
    x373)^2) + 1 / sqrt((x11 - x94)^2 + (x151 - x234)^2 + (x291 - x374)^2) + 1
    / sqrt((x11 - x95)^2 + (x151 - x235)^2 + (x291 - x375)^2) + 1 / sqrt((x11
    - x96)^2 + (x151 - x236)^2 + (x291 - x376)^2) + 1 / sqrt((x11 - x97)^2 + (
    x151 - x237)^2 + (x291 - x377)^2) + 1 / sqrt((x11 - x98)^2 + (x151 - x238)^
    2 + (x291 - x378)^2) + 1 / sqrt((x11 - x99)^2 + (x151 - x239)^2 + (x291 -
    x379)^2) + 1 / sqrt((x11 - x100)^2 + (x151 - x240)^2 + (x291 - x380)^2) + 1
    / sqrt((x11 - x101)^2 + (x151 - x241)^2 + (x291 - x381)^2) + 1 / sqrt((x11
    - x102)^2 + (x151 - x242)^2 + (x291 - x382)^2) + 1 / sqrt((x11 - x103)^2
    + (x151 - x243)^2 + (x291 - x383)^2) + 1 / sqrt((x11 - x104)^2 + (x151 -
    x244)^2 + (x291 - x384)^2) + 1 / sqrt((x11 - x105)^2 + (x151 - x245)^2 + (
    x291 - x385)^2) + 1 / sqrt((x11 - x106)^2 + (x151 - x246)^2 + (x291 - x386)
    ^2) + 1 / sqrt((x11 - x107)^2 + (x151 - x247)^2 + (x291 - x387)^2) + 1 /
    sqrt((x11 - x108)^2 + (x151 - x248)^2 + (x291 - x388)^2) + 1 / sqrt((x11 -
    x109)^2 + (x151 - x249)^2 + (x291 - x389)^2) + 1 / sqrt((x11 - x110)^2 + (
    x151 - x250)^2 + (x291 - x390)^2) + 1 / sqrt((x11 - x111)^2 + (x151 - x251)
    ^2 + (x291 - x391)^2) + 1 / sqrt((x11 - x112)^2 + (x151 - x252)^2 + (x291
    - x392)^2) + 1 / sqrt((x11 - x113)^2 + (x151 - x253)^2 + (x291 - x393)^2)
    + 1 / sqrt((x11 - x114)^2 + (x151 - x254)^2 + (x291 - x394)^2) + 1 / sqrt(
    (x11 - x115)^2 + (x151 - x255)^2 + (x291 - x395)^2) + 1 / sqrt((x11 - x116)
    ^2 + (x151 - x256)^2 + (x291 - x396)^2) + 1 / sqrt((x11 - x117)^2 + (x151
    - x257)^2 + (x291 - x397)^2) + 1 / sqrt((x11 - x118)^2 + (x151 - x258)^2
    + (x291 - x398)^2) + 1 / sqrt((x11 - x119)^2 + (x151 - x259)^2 + (x291 -
    x399)^2) + 1 / sqrt((x11 - x120)^2 + (x151 - x260)^2 + (x291 - x400)^2) + 1
    / sqrt((x11 - x121)^2 + (x151 - x261)^2 + (x291 - x401)^2) + 1 / sqrt((x11
    - x122)^2 + (x151 - x262)^2 + (x291 - x402)^2) + 1 / sqrt((x11 - x123)^2
    + (x151 - x263)^2 + (x291 - x403)^2) + 1 / sqrt((x11 - x124)^2 + (x151 -
    x264)^2 + (x291 - x404)^2) + 1 / sqrt((x11 - x125)^2 + (x151 - x265)^2 + (
    x291 - x405)^2) + 1 / sqrt((x11 - x126)^2 + (x151 - x266)^2 + (x291 - x406)
    ^2) + 1 / sqrt((x11 - x127)^2 + (x151 - x267)^2 + (x291 - x407)^2) + 1 /
    sqrt((x11 - x128)^2 + (x151 - x268)^2 + (x291 - x408)^2) + 1 / sqrt((x11 -
    x129)^2 + (x151 - x269)^2 + (x291 - x409)^2) + 1 / sqrt((x11 - x130)^2 + (
    x151 - x270)^2 + (x291 - x410)^2) + 1 / sqrt((x11 - x131)^2 + (x151 - x271)
    ^2 + (x291 - x411)^2) + 1 / sqrt((x11 - x132)^2 + (x151 - x272)^2 + (x291
    - x412)^2) + 1 / sqrt((x11 - x133)^2 + (x151 - x273)^2 + (x291 - x413)^2)
    + 1 / sqrt((x11 - x134)^2 + (x151 - x274)^2 + (x291 - x414)^2) + 1 / sqrt(
    (x11 - x135)^2 + (x151 - x275)^2 + (x291 - x415)^2) + 1 / sqrt((x11 - x136)
    ^2 + (x151 - x276)^2 + (x291 - x416)^2) + 1 / sqrt((x11 - x137)^2 + (x151
    - x277)^2 + (x291 - x417)^2) + 1 / sqrt((x11 - x138)^2 + (x151 - x278)^2
    + (x291 - x418)^2) + 1 / sqrt((x11 - x139)^2 + (x151 - x279)^2 + (x291 -
    x419)^2) + 1 / sqrt((x11 - x140)^2 + (x151 - x280)^2 + (x291 - x420)^2) + 1
    / sqrt((x12 - x13)^2 + (x152 - x153)^2 + (x292 - x293)^2) + 1 / sqrt((x12
    - x14)^2 + (x152 - x154)^2 + (x292 - x294)^2) + 1 / sqrt((x12 - x15)^2 + (
    x152 - x155)^2 + (x292 - x295)^2) + 1 / sqrt((x12 - x16)^2 + (x152 - x156)^
    2 + (x292 - x296)^2) + 1 / sqrt((x12 - x17)^2 + (x152 - x157)^2 + (x292 -
    x297)^2) + 1 / sqrt((x12 - x18)^2 + (x152 - x158)^2 + (x292 - x298)^2) + 1
    / sqrt((x12 - x19)^2 + (x152 - x159)^2 + (x292 - x299)^2) + 1 / sqrt((x12
    - x20)^2 + (x152 - x160)^2 + (x292 - x300)^2) + 1 / sqrt((x12 - x21)^2 + (
    x152 - x161)^2 + (x292 - x301)^2) + 1 / sqrt((x12 - x22)^2 + (x152 - x162)^
    2 + (x292 - x302)^2) + 1 / sqrt((x12 - x23)^2 + (x152 - x163)^2 + (x292 -
    x303)^2) + 1 / sqrt((x12 - x24)^2 + (x152 - x164)^2 + (x292 - x304)^2) + 1
    / sqrt((x12 - x25)^2 + (x152 - x165)^2 + (x292 - x305)^2) + 1 / sqrt((x12
    - x26)^2 + (x152 - x166)^2 + (x292 - x306)^2) + 1 / sqrt((x12 - x27)^2 + (
    x152 - x167)^2 + (x292 - x307)^2) + 1 / sqrt((x12 - x28)^2 + (x152 - x168)^
    2 + (x292 - x308)^2) + 1 / sqrt((x12 - x29)^2 + (x152 - x169)^2 + (x292 -
    x309)^2) + 1 / sqrt((x12 - x30)^2 + (x152 - x170)^2 + (x292 - x310)^2) + 1
    / sqrt((x12 - x31)^2 + (x152 - x171)^2 + (x292 - x311)^2) + 1 / sqrt((x12
    - x32)^2 + (x152 - x172)^2 + (x292 - x312)^2) + 1 / sqrt((x12 - x33)^2 + (
    x152 - x173)^2 + (x292 - x313)^2) + 1 / sqrt((x12 - x34)^2 + (x152 - x174)^
    2 + (x292 - x314)^2) + 1 / sqrt((x12 - x35)^2 + (x152 - x175)^2 + (x292 -
    x315)^2) + 1 / sqrt((x12 - x36)^2 + (x152 - x176)^2 + (x292 - x316)^2) + 1
    / sqrt((x12 - x37)^2 + (x152 - x177)^2 + (x292 - x317)^2) + 1 / sqrt((x12
    - x38)^2 + (x152 - x178)^2 + (x292 - x318)^2) + 1 / sqrt((x12 - x39)^2 + (
    x152 - x179)^2 + (x292 - x319)^2) + 1 / sqrt((x12 - x40)^2 + (x152 - x180)^
    2 + (x292 - x320)^2) + 1 / sqrt((x12 - x41)^2 + (x152 - x181)^2 + (x292 -
    x321)^2) + 1 / sqrt((x12 - x42)^2 + (x152 - x182)^2 + (x292 - x322)^2) + 1
    / sqrt((x12 - x43)^2 + (x152 - x183)^2 + (x292 - x323)^2) + 1 / sqrt((x12
    - x44)^2 + (x152 - x184)^2 + (x292 - x324)^2) + 1 / sqrt((x12 - x45)^2 + (
    x152 - x185)^2 + (x292 - x325)^2) + 1 / sqrt((x12 - x46)^2 + (x152 - x186)^
    2 + (x292 - x326)^2) + 1 / sqrt((x12 - x47)^2 + (x152 - x187)^2 + (x292 -
    x327)^2) + 1 / sqrt((x12 - x48)^2 + (x152 - x188)^2 + (x292 - x328)^2) + 1
    / sqrt((x12 - x49)^2 + (x152 - x189)^2 + (x292 - x329)^2) + 1 / sqrt((x12
    - x50)^2 + (x152 - x190)^2 + (x292 - x330)^2) + 1 / sqrt((x12 - x51)^2 + (
    x152 - x191)^2 + (x292 - x331)^2) + 1 / sqrt((x12 - x52)^2 + (x152 - x192)^
    2 + (x292 - x332)^2) + 1 / sqrt((x12 - x53)^2 + (x152 - x193)^2 + (x292 -
    x333)^2) + 1 / sqrt((x12 - x54)^2 + (x152 - x194)^2 + (x292 - x334)^2) + 1
    / sqrt((x12 - x55)^2 + (x152 - x195)^2 + (x292 - x335)^2) + 1 / sqrt((x12
    - x56)^2 + (x152 - x196)^2 + (x292 - x336)^2) + 1 / sqrt((x12 - x57)^2 + (
    x152 - x197)^2 + (x292 - x337)^2) + 1 / sqrt((x12 - x58)^2 + (x152 - x198)^
    2 + (x292 - x338)^2) + 1 / sqrt((x12 - x59)^2 + (x152 - x199)^2 + (x292 -
    x339)^2) + 1 / sqrt((x12 - x60)^2 + (x152 - x200)^2 + (x292 - x340)^2) + 1
    / sqrt((x12 - x61)^2 + (x152 - x201)^2 + (x292 - x341)^2) + 1 / sqrt((x12
    - x62)^2 + (x152 - x202)^2 + (x292 - x342)^2) + 1 / sqrt((x12 - x63)^2 + (
    x152 - x203)^2 + (x292 - x343)^2) + 1 / sqrt((x12 - x64)^2 + (x152 - x204)^
    2 + (x292 - x344)^2) + 1 / sqrt((x12 - x65)^2 + (x152 - x205)^2 + (x292 -
    x345)^2) + 1 / sqrt((x12 - x66)^2 + (x152 - x206)^2 + (x292 - x346)^2) + 1
    / sqrt((x12 - x67)^2 + (x152 - x207)^2 + (x292 - x347)^2) + 1 / sqrt((x12
    - x68)^2 + (x152 - x208)^2 + (x292 - x348)^2) + 1 / sqrt((x12 - x69)^2 + (
    x152 - x209)^2 + (x292 - x349)^2) + 1 / sqrt((x12 - x70)^2 + (x152 - x210)^
    2 + (x292 - x350)^2) + 1 / sqrt((x12 - x71)^2 + (x152 - x211)^2 + (x292 -
    x351)^2) + 1 / sqrt((x12 - x72)^2 + (x152 - x212)^2 + (x292 - x352)^2) + 1
    / sqrt((x12 - x73)^2 + (x152 - x213)^2 + (x292 - x353)^2) + 1 / sqrt((x12
    - x74)^2 + (x152 - x214)^2 + (x292 - x354)^2) + 1 / sqrt((x12 - x75)^2 + (
    x152 - x215)^2 + (x292 - x355)^2) + 1 / sqrt((x12 - x76)^2 + (x152 - x216)^
    2 + (x292 - x356)^2) + 1 / sqrt((x12 - x77)^2 + (x152 - x217)^2 + (x292 -
    x357)^2) + 1 / sqrt((x12 - x78)^2 + (x152 - x218)^2 + (x292 - x358)^2) + 1
    / sqrt((x12 - x79)^2 + (x152 - x219)^2 + (x292 - x359)^2) + 1 / sqrt((x12
    - x80)^2 + (x152 - x220)^2 + (x292 - x360)^2) + 1 / sqrt((x12 - x81)^2 + (
    x152 - x221)^2 + (x292 - x361)^2) + 1 / sqrt((x12 - x82)^2 + (x152 - x222)^
    2 + (x292 - x362)^2) + 1 / sqrt((x12 - x83)^2 + (x152 - x223)^2 + (x292 -
    x363)^2) + 1 / sqrt((x12 - x84)^2 + (x152 - x224)^2 + (x292 - x364)^2) + 1
    / sqrt((x12 - x85)^2 + (x152 - x225)^2 + (x292 - x365)^2) + 1 / sqrt((x12
    - x86)^2 + (x152 - x226)^2 + (x292 - x366)^2) + 1 / sqrt((x12 - x87)^2 + (
    x152 - x227)^2 + (x292 - x367)^2) + 1 / sqrt((x12 - x88)^2 + (x152 - x228)^
    2 + (x292 - x368)^2) + 1 / sqrt((x12 - x89)^2 + (x152 - x229)^2 + (x292 -
    x369)^2) + 1 / sqrt((x12 - x90)^2 + (x152 - x230)^2 + (x292 - x370)^2) + 1
    / sqrt((x12 - x91)^2 + (x152 - x231)^2 + (x292 - x371)^2) + 1 / sqrt((x12
    - x92)^2 + (x152 - x232)^2 + (x292 - x372)^2) + 1 / sqrt((x12 - x93)^2 + (
    x152 - x233)^2 + (x292 - x373)^2) + 1 / sqrt((x12 - x94)^2 + (x152 - x234)^
    2 + (x292 - x374)^2) + 1 / sqrt((x12 - x95)^2 + (x152 - x235)^2 + (x292 -
    x375)^2) + 1 / sqrt((x12 - x96)^2 + (x152 - x236)^2 + (x292 - x376)^2) + 1
    / sqrt((x12 - x97)^2 + (x152 - x237)^2 + (x292 - x377)^2) + 1 / sqrt((x12
    - x98)^2 + (x152 - x238)^2 + (x292 - x378)^2) + 1 / sqrt((x12 - x99)^2 + (
    x152 - x239)^2 + (x292 - x379)^2) + 1 / sqrt((x12 - x100)^2 + (x152 - x240)
    ^2 + (x292 - x380)^2) + 1 / sqrt((x12 - x101)^2 + (x152 - x241)^2 + (x292
    - x381)^2) + 1 / sqrt((x12 - x102)^2 + (x152 - x242)^2 + (x292 - x382)^2)
    + 1 / sqrt((x12 - x103)^2 + (x152 - x243)^2 + (x292 - x383)^2) + 1 / sqrt(
    (x12 - x104)^2 + (x152 - x244)^2 + (x292 - x384)^2) + 1 / sqrt((x12 - x105)
    ^2 + (x152 - x245)^2 + (x292 - x385)^2) + 1 / sqrt((x12 - x106)^2 + (x152
    - x246)^2 + (x292 - x386)^2) + 1 / sqrt((x12 - x107)^2 + (x152 - x247)^2
    + (x292 - x387)^2) + 1 / sqrt((x12 - x108)^2 + (x152 - x248)^2 + (x292 -
    x388)^2) + 1 / sqrt((x12 - x109)^2 + (x152 - x249)^2 + (x292 - x389)^2) + 1
    / sqrt((x12 - x110)^2 + (x152 - x250)^2 + (x292 - x390)^2) + 1 / sqrt((x12
    - x111)^2 + (x152 - x251)^2 + (x292 - x391)^2) + 1 / sqrt((x12 - x112)^2
    + (x152 - x252)^2 + (x292 - x392)^2) + 1 / sqrt((x12 - x113)^2 + (x152 -
    x253)^2 + (x292 - x393)^2) + 1 / sqrt((x12 - x114)^2 + (x152 - x254)^2 + (
    x292 - x394)^2) + 1 / sqrt((x12 - x115)^2 + (x152 - x255)^2 + (x292 - x395)
    ^2) + 1 / sqrt((x12 - x116)^2 + (x152 - x256)^2 + (x292 - x396)^2) + 1 /
    sqrt((x12 - x117)^2 + (x152 - x257)^2 + (x292 - x397)^2) + 1 / sqrt((x12 -
    x118)^2 + (x152 - x258)^2 + (x292 - x398)^2) + 1 / sqrt((x12 - x119)^2 + (
    x152 - x259)^2 + (x292 - x399)^2) + 1 / sqrt((x12 - x120)^2 + (x152 - x260)
    ^2 + (x292 - x400)^2) + 1 / sqrt((x12 - x121)^2 + (x152 - x261)^2 + (x292
    - x401)^2) + 1 / sqrt((x12 - x122)^2 + (x152 - x262)^2 + (x292 - x402)^2)
    + 1 / sqrt((x12 - x123)^2 + (x152 - x263)^2 + (x292 - x403)^2) + 1 / sqrt(
    (x12 - x124)^2 + (x152 - x264)^2 + (x292 - x404)^2) + 1 / sqrt((x12 - x125)
    ^2 + (x152 - x265)^2 + (x292 - x405)^2) + 1 / sqrt((x12 - x126)^2 + (x152
    - x266)^2 + (x292 - x406)^2) + 1 / sqrt((x12 - x127)^2 + (x152 - x267)^2
    + (x292 - x407)^2) + 1 / sqrt((x12 - x128)^2 + (x152 - x268)^2 + (x292 -
    x408)^2) + 1 / sqrt((x12 - x129)^2 + (x152 - x269)^2 + (x292 - x409)^2) + 1
    / sqrt((x12 - x130)^2 + (x152 - x270)^2 + (x292 - x410)^2) + 1 / sqrt((x12
    - x131)^2 + (x152 - x271)^2 + (x292 - x411)^2) + 1 / sqrt((x12 - x132)^2
    + (x152 - x272)^2 + (x292 - x412)^2) + 1 / sqrt((x12 - x133)^2 + (x152 -
    x273)^2 + (x292 - x413)^2) + 1 / sqrt((x12 - x134)^2 + (x152 - x274)^2 + (
    x292 - x414)^2) + 1 / sqrt((x12 - x135)^2 + (x152 - x275)^2 + (x292 - x415)
    ^2) + 1 / sqrt((x12 - x136)^2 + (x152 - x276)^2 + (x292 - x416)^2) + 1 /
    sqrt((x12 - x137)^2 + (x152 - x277)^2 + (x292 - x417)^2) + 1 / sqrt((x12 -
    x138)^2 + (x152 - x278)^2 + (x292 - x418)^2) + 1 / sqrt((x12 - x139)^2 + (
    x152 - x279)^2 + (x292 - x419)^2) + 1 / sqrt((x12 - x140)^2 + (x152 - x280)
    ^2 + (x292 - x420)^2) + 1 / sqrt((x13 - x14)^2 + (x153 - x154)^2 + (x293 -
    x294)^2) + 1 / sqrt((x13 - x15)^2 + (x153 - x155)^2 + (x293 - x295)^2) + 1
    / sqrt((x13 - x16)^2 + (x153 - x156)^2 + (x293 - x296)^2) + 1 / sqrt((x13
    - x17)^2 + (x153 - x157)^2 + (x293 - x297)^2) + 1 / sqrt((x13 - x18)^2 + (
    x153 - x158)^2 + (x293 - x298)^2) + 1 / sqrt((x13 - x19)^2 + (x153 - x159)^
    2 + (x293 - x299)^2) + 1 / sqrt((x13 - x20)^2 + (x153 - x160)^2 + (x293 -
    x300)^2) + 1 / sqrt((x13 - x21)^2 + (x153 - x161)^2 + (x293 - x301)^2) + 1
    / sqrt((x13 - x22)^2 + (x153 - x162)^2 + (x293 - x302)^2) + 1 / sqrt((x13
    - x23)^2 + (x153 - x163)^2 + (x293 - x303)^2) + 1 / sqrt((x13 - x24)^2 + (
    x153 - x164)^2 + (x293 - x304)^2) + 1 / sqrt((x13 - x25)^2 + (x153 - x165)^
    2 + (x293 - x305)^2) + 1 / sqrt((x13 - x26)^2 + (x153 - x166)^2 + (x293 -
    x306)^2) + 1 / sqrt((x13 - x27)^2 + (x153 - x167)^2 + (x293 - x307)^2) + 1
    / sqrt((x13 - x28)^2 + (x153 - x168)^2 + (x293 - x308)^2) + 1 / sqrt((x13
    - x29)^2 + (x153 - x169)^2 + (x293 - x309)^2) + 1 / sqrt((x13 - x30)^2 + (
    x153 - x170)^2 + (x293 - x310)^2) + 1 / sqrt((x13 - x31)^2 + (x153 - x171)^
    2 + (x293 - x311)^2) + 1 / sqrt((x13 - x32)^2 + (x153 - x172)^2 + (x293 -
    x312)^2) + 1 / sqrt((x13 - x33)^2 + (x153 - x173)^2 + (x293 - x313)^2) + 1
    / sqrt((x13 - x34)^2 + (x153 - x174)^2 + (x293 - x314)^2) + 1 / sqrt((x13
    - x35)^2 + (x153 - x175)^2 + (x293 - x315)^2) + 1 / sqrt((x13 - x36)^2 + (
    x153 - x176)^2 + (x293 - x316)^2) + 1 / sqrt((x13 - x37)^2 + (x153 - x177)^
    2 + (x293 - x317)^2) + 1 / sqrt((x13 - x38)^2 + (x153 - x178)^2 + (x293 -
    x318)^2) + 1 / sqrt((x13 - x39)^2 + (x153 - x179)^2 + (x293 - x319)^2) + 1
    / sqrt((x13 - x40)^2 + (x153 - x180)^2 + (x293 - x320)^2) + 1 / sqrt((x13
    - x41)^2 + (x153 - x181)^2 + (x293 - x321)^2) + 1 / sqrt((x13 - x42)^2 + (
    x153 - x182)^2 + (x293 - x322)^2) + 1 / sqrt((x13 - x43)^2 + (x153 - x183)^
    2 + (x293 - x323)^2) + 1 / sqrt((x13 - x44)^2 + (x153 - x184)^2 + (x293 -
    x324)^2) + 1 / sqrt((x13 - x45)^2 + (x153 - x185)^2 + (x293 - x325)^2) + 1
    / sqrt((x13 - x46)^2 + (x153 - x186)^2 + (x293 - x326)^2) + 1 / sqrt((x13
    - x47)^2 + (x153 - x187)^2 + (x293 - x327)^2) + 1 / sqrt((x13 - x48)^2 + (
    x153 - x188)^2 + (x293 - x328)^2) + 1 / sqrt((x13 - x49)^2 + (x153 - x189)^
    2 + (x293 - x329)^2) + 1 / sqrt((x13 - x50)^2 + (x153 - x190)^2 + (x293 -
    x330)^2) + 1 / sqrt((x13 - x51)^2 + (x153 - x191)^2 + (x293 - x331)^2) + 1
    / sqrt((x13 - x52)^2 + (x153 - x192)^2 + (x293 - x332)^2) + 1 / sqrt((x13
    - x53)^2 + (x153 - x193)^2 + (x293 - x333)^2) + 1 / sqrt((x13 - x54)^2 + (
    x153 - x194)^2 + (x293 - x334)^2) + 1 / sqrt((x13 - x55)^2 + (x153 - x195)^
    2 + (x293 - x335)^2) + 1 / sqrt((x13 - x56)^2 + (x153 - x196)^2 + (x293 -
    x336)^2) + 1 / sqrt((x13 - x57)^2 + (x153 - x197)^2 + (x293 - x337)^2) + 1
    / sqrt((x13 - x58)^2 + (x153 - x198)^2 + (x293 - x338)^2) + 1 / sqrt((x13
    - x59)^2 + (x153 - x199)^2 + (x293 - x339)^2) + 1 / sqrt((x13 - x60)^2 + (
    x153 - x200)^2 + (x293 - x340)^2) + 1 / sqrt((x13 - x61)^2 + (x153 - x201)^
    2 + (x293 - x341)^2) + 1 / sqrt((x13 - x62)^2 + (x153 - x202)^2 + (x293 -
    x342)^2) + 1 / sqrt((x13 - x63)^2 + (x153 - x203)^2 + (x293 - x343)^2) + 1
    / sqrt((x13 - x64)^2 + (x153 - x204)^2 + (x293 - x344)^2) + 1 / sqrt((x13
    - x65)^2 + (x153 - x205)^2 + (x293 - x345)^2) + 1 / sqrt((x13 - x66)^2 + (
    x153 - x206)^2 + (x293 - x346)^2) + 1 / sqrt((x13 - x67)^2 + (x153 - x207)^
    2 + (x293 - x347)^2) + 1 / sqrt((x13 - x68)^2 + (x153 - x208)^2 + (x293 -
    x348)^2) + 1 / sqrt((x13 - x69)^2 + (x153 - x209)^2 + (x293 - x349)^2) + 1
    / sqrt((x13 - x70)^2 + (x153 - x210)^2 + (x293 - x350)^2) + 1 / sqrt((x13
    - x71)^2 + (x153 - x211)^2 + (x293 - x351)^2) + 1 / sqrt((x13 - x72)^2 + (
    x153 - x212)^2 + (x293 - x352)^2) + 1 / sqrt((x13 - x73)^2 + (x153 - x213)^
    2 + (x293 - x353)^2) + 1 / sqrt((x13 - x74)^2 + (x153 - x214)^2 + (x293 -
    x354)^2) + 1 / sqrt((x13 - x75)^2 + (x153 - x215)^2 + (x293 - x355)^2) + 1
    / sqrt((x13 - x76)^2 + (x153 - x216)^2 + (x293 - x356)^2) + 1 / sqrt((x13
    - x77)^2 + (x153 - x217)^2 + (x293 - x357)^2) + 1 / sqrt((x13 - x78)^2 + (
    x153 - x218)^2 + (x293 - x358)^2) + 1 / sqrt((x13 - x79)^2 + (x153 - x219)^
    2 + (x293 - x359)^2) + 1 / sqrt((x13 - x80)^2 + (x153 - x220)^2 + (x293 -
    x360)^2) + 1 / sqrt((x13 - x81)^2 + (x153 - x221)^2 + (x293 - x361)^2) + 1
    / sqrt((x13 - x82)^2 + (x153 - x222)^2 + (x293 - x362)^2) + 1 / sqrt((x13
    - x83)^2 + (x153 - x223)^2 + (x293 - x363)^2) + 1 / sqrt((x13 - x84)^2 + (
    x153 - x224)^2 + (x293 - x364)^2) + 1 / sqrt((x13 - x85)^2 + (x153 - x225)^
    2 + (x293 - x365)^2) + 1 / sqrt((x13 - x86)^2 + (x153 - x226)^2 + (x293 -
    x366)^2) + 1 / sqrt((x13 - x87)^2 + (x153 - x227)^2 + (x293 - x367)^2) + 1
    / sqrt((x13 - x88)^2 + (x153 - x228)^2 + (x293 - x368)^2) + 1 / sqrt((x13
    - x89)^2 + (x153 - x229)^2 + (x293 - x369)^2) + 1 / sqrt((x13 - x90)^2 + (
    x153 - x230)^2 + (x293 - x370)^2) + 1 / sqrt((x13 - x91)^2 + (x153 - x231)^
    2 + (x293 - x371)^2) + 1 / sqrt((x13 - x92)^2 + (x153 - x232)^2 + (x293 -
    x372)^2) + 1 / sqrt((x13 - x93)^2 + (x153 - x233)^2 + (x293 - x373)^2) + 1
    / sqrt((x13 - x94)^2 + (x153 - x234)^2 + (x293 - x374)^2) + 1 / sqrt((x13
    - x95)^2 + (x153 - x235)^2 + (x293 - x375)^2) + 1 / sqrt((x13 - x96)^2 + (
    x153 - x236)^2 + (x293 - x376)^2) + 1 / sqrt((x13 - x97)^2 + (x153 - x237)^
    2 + (x293 - x377)^2) + 1 / sqrt((x13 - x98)^2 + (x153 - x238)^2 + (x293 -
    x378)^2) + 1 / sqrt((x13 - x99)^2 + (x153 - x239)^2 + (x293 - x379)^2) + 1
    / sqrt((x13 - x100)^2 + (x153 - x240)^2 + (x293 - x380)^2) + 1 / sqrt((x13
    - x101)^2 + (x153 - x241)^2 + (x293 - x381)^2) + 1 / sqrt((x13 - x102)^2
    + (x153 - x242)^2 + (x293 - x382)^2) + 1 / sqrt((x13 - x103)^2 + (x153 -
    x243)^2 + (x293 - x383)^2) + 1 / sqrt((x13 - x104)^2 + (x153 - x244)^2 + (
    x293 - x384)^2) + 1 / sqrt((x13 - x105)^2 + (x153 - x245)^2 + (x293 - x385)
    ^2) + 1 / sqrt((x13 - x106)^2 + (x153 - x246)^2 + (x293 - x386)^2) + 1 /
    sqrt((x13 - x107)^2 + (x153 - x247)^2 + (x293 - x387)^2) + 1 / sqrt((x13 -
    x108)^2 + (x153 - x248)^2 + (x293 - x388)^2) + 1 / sqrt((x13 - x109)^2 + (
    x153 - x249)^2 + (x293 - x389)^2) + 1 / sqrt((x13 - x110)^2 + (x153 - x250)
    ^2 + (x293 - x390)^2) + 1 / sqrt((x13 - x111)^2 + (x153 - x251)^2 + (x293
    - x391)^2) + 1 / sqrt((x13 - x112)^2 + (x153 - x252)^2 + (x293 - x392)^2)
    + 1 / sqrt((x13 - x113)^2 + (x153 - x253)^2 + (x293 - x393)^2) + 1 / sqrt(
    (x13 - x114)^2 + (x153 - x254)^2 + (x293 - x394)^2) + 1 / sqrt((x13 - x115)
    ^2 + (x153 - x255)^2 + (x293 - x395)^2) + 1 / sqrt((x13 - x116)^2 + (x153
    - x256)^2 + (x293 - x396)^2) + 1 / sqrt((x13 - x117)^2 + (x153 - x257)^2
    + (x293 - x397)^2) + 1 / sqrt((x13 - x118)^2 + (x153 - x258)^2 + (x293 -
    x398)^2) + 1 / sqrt((x13 - x119)^2 + (x153 - x259)^2 + (x293 - x399)^2) + 1
    / sqrt((x13 - x120)^2 + (x153 - x260)^2 + (x293 - x400)^2) + 1 / sqrt((x13
    - x121)^2 + (x153 - x261)^2 + (x293 - x401)^2) + 1 / sqrt((x13 - x122)^2
    + (x153 - x262)^2 + (x293 - x402)^2) + 1 / sqrt((x13 - x123)^2 + (x153 -
    x263)^2 + (x293 - x403)^2) + 1 / sqrt((x13 - x124)^2 + (x153 - x264)^2 + (
    x293 - x404)^2) + 1 / sqrt((x13 - x125)^2 + (x153 - x265)^2 + (x293 - x405)
    ^2) + 1 / sqrt((x13 - x126)^2 + (x153 - x266)^2 + (x293 - x406)^2) + 1 /
    sqrt((x13 - x127)^2 + (x153 - x267)^2 + (x293 - x407)^2) + 1 / sqrt((x13 -
    x128)^2 + (x153 - x268)^2 + (x293 - x408)^2) + 1 / sqrt((x13 - x129)^2 + (
    x153 - x269)^2 + (x293 - x409)^2) + 1 / sqrt((x13 - x130)^2 + (x153 - x270)
    ^2 + (x293 - x410)^2) + 1 / sqrt((x13 - x131)^2 + (x153 - x271)^2 + (x293
    - x411)^2) + 1 / sqrt((x13 - x132)^2 + (x153 - x272)^2 + (x293 - x412)^2)
    + 1 / sqrt((x13 - x133)^2 + (x153 - x273)^2 + (x293 - x413)^2) + 1 / sqrt(
    (x13 - x134)^2 + (x153 - x274)^2 + (x293 - x414)^2) + 1 / sqrt((x13 - x135)
    ^2 + (x153 - x275)^2 + (x293 - x415)^2) + 1 / sqrt((x13 - x136)^2 + (x153
    - x276)^2 + (x293 - x416)^2) + 1 / sqrt((x13 - x137)^2 + (x153 - x277)^2
    + (x293 - x417)^2) + 1 / sqrt((x13 - x138)^2 + (x153 - x278)^2 + (x293 -
    x418)^2) + 1 / sqrt((x13 - x139)^2 + (x153 - x279)^2 + (x293 - x419)^2) + 1
    / sqrt((x13 - x140)^2 + (x153 - x280)^2 + (x293 - x420)^2) + 1 / sqrt((x14
    - x15)^2 + (x154 - x155)^2 + (x294 - x295)^2) + 1 / sqrt((x14 - x16)^2 + (
    x154 - x156)^2 + (x294 - x296)^2) + 1 / sqrt((x14 - x17)^2 + (x154 - x157)^
    2 + (x294 - x297)^2) + 1 / sqrt((x14 - x18)^2 + (x154 - x158)^2 + (x294 -
    x298)^2) + 1 / sqrt((x14 - x19)^2 + (x154 - x159)^2 + (x294 - x299)^2) + 1
    / sqrt((x14 - x20)^2 + (x154 - x160)^2 + (x294 - x300)^2) + 1 / sqrt((x14
    - x21)^2 + (x154 - x161)^2 + (x294 - x301)^2) + 1 / sqrt((x14 - x22)^2 + (
    x154 - x162)^2 + (x294 - x302)^2) + 1 / sqrt((x14 - x23)^2 + (x154 - x163)^
    2 + (x294 - x303)^2) + 1 / sqrt((x14 - x24)^2 + (x154 - x164)^2 + (x294 -
    x304)^2) + 1 / sqrt((x14 - x25)^2 + (x154 - x165)^2 + (x294 - x305)^2) + 1
    / sqrt((x14 - x26)^2 + (x154 - x166)^2 + (x294 - x306)^2) + 1 / sqrt((x14
    - x27)^2 + (x154 - x167)^2 + (x294 - x307)^2) + 1 / sqrt((x14 - x28)^2 + (
    x154 - x168)^2 + (x294 - x308)^2) + 1 / sqrt((x14 - x29)^2 + (x154 - x169)^
    2 + (x294 - x309)^2) + 1 / sqrt((x14 - x30)^2 + (x154 - x170)^2 + (x294 -
    x310)^2) + 1 / sqrt((x14 - x31)^2 + (x154 - x171)^2 + (x294 - x311)^2) + 1
    / sqrt((x14 - x32)^2 + (x154 - x172)^2 + (x294 - x312)^2) + 1 / sqrt((x14
    - x33)^2 + (x154 - x173)^2 + (x294 - x313)^2) + 1 / sqrt((x14 - x34)^2 + (
    x154 - x174)^2 + (x294 - x314)^2) + 1 / sqrt((x14 - x35)^2 + (x154 - x175)^
    2 + (x294 - x315)^2) + 1 / sqrt((x14 - x36)^2 + (x154 - x176)^2 + (x294 -
    x316)^2) + 1 / sqrt((x14 - x37)^2 + (x154 - x177)^2 + (x294 - x317)^2) + 1
    / sqrt((x14 - x38)^2 + (x154 - x178)^2 + (x294 - x318)^2) + 1 / sqrt((x14
    - x39)^2 + (x154 - x179)^2 + (x294 - x319)^2) + 1 / sqrt((x14 - x40)^2 + (
    x154 - x180)^2 + (x294 - x320)^2) + 1 / sqrt((x14 - x41)^2 + (x154 - x181)^
    2 + (x294 - x321)^2) + 1 / sqrt((x14 - x42)^2 + (x154 - x182)^2 + (x294 -
    x322)^2) + 1 / sqrt((x14 - x43)^2 + (x154 - x183)^2 + (x294 - x323)^2) + 1
    / sqrt((x14 - x44)^2 + (x154 - x184)^2 + (x294 - x324)^2) + 1 / sqrt((x14
    - x45)^2 + (x154 - x185)^2 + (x294 - x325)^2) + 1 / sqrt((x14 - x46)^2 + (
    x154 - x186)^2 + (x294 - x326)^2) + 1 / sqrt((x14 - x47)^2 + (x154 - x187)^
    2 + (x294 - x327)^2) + 1 / sqrt((x14 - x48)^2 + (x154 - x188)^2 + (x294 -
    x328)^2) + 1 / sqrt((x14 - x49)^2 + (x154 - x189)^2 + (x294 - x329)^2) + 1
    / sqrt((x14 - x50)^2 + (x154 - x190)^2 + (x294 - x330)^2) + 1 / sqrt((x14
    - x51)^2 + (x154 - x191)^2 + (x294 - x331)^2) + 1 / sqrt((x14 - x52)^2 + (
    x154 - x192)^2 + (x294 - x332)^2) + 1 / sqrt((x14 - x53)^2 + (x154 - x193)^
    2 + (x294 - x333)^2) + 1 / sqrt((x14 - x54)^2 + (x154 - x194)^2 + (x294 -
    x334)^2) + 1 / sqrt((x14 - x55)^2 + (x154 - x195)^2 + (x294 - x335)^2) + 1
    / sqrt((x14 - x56)^2 + (x154 - x196)^2 + (x294 - x336)^2) + 1 / sqrt((x14
    - x57)^2 + (x154 - x197)^2 + (x294 - x337)^2) + 1 / sqrt((x14 - x58)^2 + (
    x154 - x198)^2 + (x294 - x338)^2) + 1 / sqrt((x14 - x59)^2 + (x154 - x199)^
    2 + (x294 - x339)^2) + 1 / sqrt((x14 - x60)^2 + (x154 - x200)^2 + (x294 -
    x340)^2) + 1 / sqrt((x14 - x61)^2 + (x154 - x201)^2 + (x294 - x341)^2) + 1
    / sqrt((x14 - x62)^2 + (x154 - x202)^2 + (x294 - x342)^2) + 1 / sqrt((x14
    - x63)^2 + (x154 - x203)^2 + (x294 - x343)^2) + 1 / sqrt((x14 - x64)^2 + (
    x154 - x204)^2 + (x294 - x344)^2) + 1 / sqrt((x14 - x65)^2 + (x154 - x205)^
    2 + (x294 - x345)^2) + 1 / sqrt((x14 - x66)^2 + (x154 - x206)^2 + (x294 -
    x346)^2) + 1 / sqrt((x14 - x67)^2 + (x154 - x207)^2 + (x294 - x347)^2) + 1
    / sqrt((x14 - x68)^2 + (x154 - x208)^2 + (x294 - x348)^2) + 1 / sqrt((x14
    - x69)^2 + (x154 - x209)^2 + (x294 - x349)^2) + 1 / sqrt((x14 - x70)^2 + (
    x154 - x210)^2 + (x294 - x350)^2) + 1 / sqrt((x14 - x71)^2 + (x154 - x211)^
    2 + (x294 - x351)^2) + 1 / sqrt((x14 - x72)^2 + (x154 - x212)^2 + (x294 -
    x352)^2) + 1 / sqrt((x14 - x73)^2 + (x154 - x213)^2 + (x294 - x353)^2) + 1
    / sqrt((x14 - x74)^2 + (x154 - x214)^2 + (x294 - x354)^2) + 1 / sqrt((x14
    - x75)^2 + (x154 - x215)^2 + (x294 - x355)^2) + 1 / sqrt((x14 - x76)^2 + (
    x154 - x216)^2 + (x294 - x356)^2) + 1 / sqrt((x14 - x77)^2 + (x154 - x217)^
    2 + (x294 - x357)^2) + 1 / sqrt((x14 - x78)^2 + (x154 - x218)^2 + (x294 -
    x358)^2) + 1 / sqrt((x14 - x79)^2 + (x154 - x219)^2 + (x294 - x359)^2) + 1
    / sqrt((x14 - x80)^2 + (x154 - x220)^2 + (x294 - x360)^2) + 1 / sqrt((x14
    - x81)^2 + (x154 - x221)^2 + (x294 - x361)^2) + 1 / sqrt((x14 - x82)^2 + (
    x154 - x222)^2 + (x294 - x362)^2) + 1 / sqrt((x14 - x83)^2 + (x154 - x223)^
    2 + (x294 - x363)^2) + 1 / sqrt((x14 - x84)^2 + (x154 - x224)^2 + (x294 -
    x364)^2) + 1 / sqrt((x14 - x85)^2 + (x154 - x225)^2 + (x294 - x365)^2) + 1
    / sqrt((x14 - x86)^2 + (x154 - x226)^2 + (x294 - x366)^2) + 1 / sqrt((x14
    - x87)^2 + (x154 - x227)^2 + (x294 - x367)^2) + 1 / sqrt((x14 - x88)^2 + (
    x154 - x228)^2 + (x294 - x368)^2) + 1 / sqrt((x14 - x89)^2 + (x154 - x229)^
    2 + (x294 - x369)^2) + 1 / sqrt((x14 - x90)^2 + (x154 - x230)^2 + (x294 -
    x370)^2) + 1 / sqrt((x14 - x91)^2 + (x154 - x231)^2 + (x294 - x371)^2) + 1
    / sqrt((x14 - x92)^2 + (x154 - x232)^2 + (x294 - x372)^2) + 1 / sqrt((x14
    - x93)^2 + (x154 - x233)^2 + (x294 - x373)^2) + 1 / sqrt((x14 - x94)^2 + (
    x154 - x234)^2 + (x294 - x374)^2) + 1 / sqrt((x14 - x95)^2 + (x154 - x235)^
    2 + (x294 - x375)^2) + 1 / sqrt((x14 - x96)^2 + (x154 - x236)^2 + (x294 -
    x376)^2) + 1 / sqrt((x14 - x97)^2 + (x154 - x237)^2 + (x294 - x377)^2) + 1
    / sqrt((x14 - x98)^2 + (x154 - x238)^2 + (x294 - x378)^2) + 1 / sqrt((x14
    - x99)^2 + (x154 - x239)^2 + (x294 - x379)^2) + 1 / sqrt((x14 - x100)^2 +
    (x154 - x240)^2 + (x294 - x380)^2) + 1 / sqrt((x14 - x101)^2 + (x154 - x241)
    ^2 + (x294 - x381)^2) + 1 / sqrt((x14 - x102)^2 + (x154 - x242)^2 + (x294
    - x382)^2) + 1 / sqrt((x14 - x103)^2 + (x154 - x243)^2 + (x294 - x383)^2)
    + 1 / sqrt((x14 - x104)^2 + (x154 - x244)^2 + (x294 - x384)^2) + 1 / sqrt(
    (x14 - x105)^2 + (x154 - x245)^2 + (x294 - x385)^2) + 1 / sqrt((x14 - x106)
    ^2 + (x154 - x246)^2 + (x294 - x386)^2) + 1 / sqrt((x14 - x107)^2 + (x154
    - x247)^2 + (x294 - x387)^2) + 1 / sqrt((x14 - x108)^2 + (x154 - x248)^2
    + (x294 - x388)^2) + 1 / sqrt((x14 - x109)^2 + (x154 - x249)^2 + (x294 -
    x389)^2) + 1 / sqrt((x14 - x110)^2 + (x154 - x250)^2 + (x294 - x390)^2) + 1
    / sqrt((x14 - x111)^2 + (x154 - x251)^2 + (x294 - x391)^2) + 1 / sqrt((x14
    - x112)^2 + (x154 - x252)^2 + (x294 - x392)^2) + 1 / sqrt((x14 - x113)^2
    + (x154 - x253)^2 + (x294 - x393)^2) + 1 / sqrt((x14 - x114)^2 + (x154 -
    x254)^2 + (x294 - x394)^2) + 1 / sqrt((x14 - x115)^2 + (x154 - x255)^2 + (
    x294 - x395)^2) + 1 / sqrt((x14 - x116)^2 + (x154 - x256)^2 + (x294 - x396)
    ^2) + 1 / sqrt((x14 - x117)^2 + (x154 - x257)^2 + (x294 - x397)^2) + 1 /
    sqrt((x14 - x118)^2 + (x154 - x258)^2 + (x294 - x398)^2) + 1 / sqrt((x14 -
    x119)^2 + (x154 - x259)^2 + (x294 - x399)^2) + 1 / sqrt((x14 - x120)^2 + (
    x154 - x260)^2 + (x294 - x400)^2) + 1 / sqrt((x14 - x121)^2 + (x154 - x261)
    ^2 + (x294 - x401)^2) + 1 / sqrt((x14 - x122)^2 + (x154 - x262)^2 + (x294
    - x402)^2) + 1 / sqrt((x14 - x123)^2 + (x154 - x263)^2 + (x294 - x403)^2)
    + 1 / sqrt((x14 - x124)^2 + (x154 - x264)^2 + (x294 - x404)^2) + 1 / sqrt(
    (x14 - x125)^2 + (x154 - x265)^2 + (x294 - x405)^2) + 1 / sqrt((x14 - x126)
    ^2 + (x154 - x266)^2 + (x294 - x406)^2) + 1 / sqrt((x14 - x127)^2 + (x154
    - x267)^2 + (x294 - x407)^2) + 1 / sqrt((x14 - x128)^2 + (x154 - x268)^2
    + (x294 - x408)^2) + 1 / sqrt((x14 - x129)^2 + (x154 - x269)^2 + (x294 -
    x409)^2) + 1 / sqrt((x14 - x130)^2 + (x154 - x270)^2 + (x294 - x410)^2) + 1
    / sqrt((x14 - x131)^2 + (x154 - x271)^2 + (x294 - x411)^2) + 1 / sqrt((x14
    - x132)^2 + (x154 - x272)^2 + (x294 - x412)^2) + 1 / sqrt((x14 - x133)^2
    + (x154 - x273)^2 + (x294 - x413)^2) + 1 / sqrt((x14 - x134)^2 + (x154 -
    x274)^2 + (x294 - x414)^2) + 1 / sqrt((x14 - x135)^2 + (x154 - x275)^2 + (
    x294 - x415)^2) + 1 / sqrt((x14 - x136)^2 + (x154 - x276)^2 + (x294 - x416)
    ^2) + 1 / sqrt((x14 - x137)^2 + (x154 - x277)^2 + (x294 - x417)^2) + 1 /
    sqrt((x14 - x138)^2 + (x154 - x278)^2 + (x294 - x418)^2) + 1 / sqrt((x14 -
    x139)^2 + (x154 - x279)^2 + (x294 - x419)^2) + 1 / sqrt((x14 - x140)^2 + (
    x154 - x280)^2 + (x294 - x420)^2) + 1 / sqrt((x15 - x16)^2 + (x155 - x156)^
    2 + (x295 - x296)^2) + 1 / sqrt((x15 - x17)^2 + (x155 - x157)^2 + (x295 -
    x297)^2) + 1 / sqrt((x15 - x18)^2 + (x155 - x158)^2 + (x295 - x298)^2) + 1
    / sqrt((x15 - x19)^2 + (x155 - x159)^2 + (x295 - x299)^2) + 1 / sqrt((x15
    - x20)^2 + (x155 - x160)^2 + (x295 - x300)^2) + 1 / sqrt((x15 - x21)^2 + (
    x155 - x161)^2 + (x295 - x301)^2) + 1 / sqrt((x15 - x22)^2 + (x155 - x162)^
    2 + (x295 - x302)^2) + 1 / sqrt((x15 - x23)^2 + (x155 - x163)^2 + (x295 -
    x303)^2) + 1 / sqrt((x15 - x24)^2 + (x155 - x164)^2 + (x295 - x304)^2) + 1
    / sqrt((x15 - x25)^2 + (x155 - x165)^2 + (x295 - x305)^2) + 1 / sqrt((x15
    - x26)^2 + (x155 - x166)^2 + (x295 - x306)^2) + 1 / sqrt((x15 - x27)^2 + (
    x155 - x167)^2 + (x295 - x307)^2) + 1 / sqrt((x15 - x28)^2 + (x155 - x168)^
    2 + (x295 - x308)^2) + 1 / sqrt((x15 - x29)^2 + (x155 - x169)^2 + (x295 -
    x309)^2) + 1 / sqrt((x15 - x30)^2 + (x155 - x170)^2 + (x295 - x310)^2) + 1
    / sqrt((x15 - x31)^2 + (x155 - x171)^2 + (x295 - x311)^2) + 1 / sqrt((x15
    - x32)^2 + (x155 - x172)^2 + (x295 - x312)^2) + 1 / sqrt((x15 - x33)^2 + (
    x155 - x173)^2 + (x295 - x313)^2) + 1 / sqrt((x15 - x34)^2 + (x155 - x174)^
    2 + (x295 - x314)^2) + 1 / sqrt((x15 - x35)^2 + (x155 - x175)^2 + (x295 -
    x315)^2) + 1 / sqrt((x15 - x36)^2 + (x155 - x176)^2 + (x295 - x316)^2) + 1
    / sqrt((x15 - x37)^2 + (x155 - x177)^2 + (x295 - x317)^2) + 1 / sqrt((x15
    - x38)^2 + (x155 - x178)^2 + (x295 - x318)^2) + 1 / sqrt((x15 - x39)^2 + (
    x155 - x179)^2 + (x295 - x319)^2) + 1 / sqrt((x15 - x40)^2 + (x155 - x180)^
    2 + (x295 - x320)^2) + 1 / sqrt((x15 - x41)^2 + (x155 - x181)^2 + (x295 -
    x321)^2) + 1 / sqrt((x15 - x42)^2 + (x155 - x182)^2 + (x295 - x322)^2) + 1
    / sqrt((x15 - x43)^2 + (x155 - x183)^2 + (x295 - x323)^2) + 1 / sqrt((x15
    - x44)^2 + (x155 - x184)^2 + (x295 - x324)^2) + 1 / sqrt((x15 - x45)^2 + (
    x155 - x185)^2 + (x295 - x325)^2) + 1 / sqrt((x15 - x46)^2 + (x155 - x186)^
    2 + (x295 - x326)^2) + 1 / sqrt((x15 - x47)^2 + (x155 - x187)^2 + (x295 -
    x327)^2) + 1 / sqrt((x15 - x48)^2 + (x155 - x188)^2 + (x295 - x328)^2) + 1
    / sqrt((x15 - x49)^2 + (x155 - x189)^2 + (x295 - x329)^2) + 1 / sqrt((x15
    - x50)^2 + (x155 - x190)^2 + (x295 - x330)^2) + 1 / sqrt((x15 - x51)^2 + (
    x155 - x191)^2 + (x295 - x331)^2) + 1 / sqrt((x15 - x52)^2 + (x155 - x192)^
    2 + (x295 - x332)^2) + 1 / sqrt((x15 - x53)^2 + (x155 - x193)^2 + (x295 -
    x333)^2) + 1 / sqrt((x15 - x54)^2 + (x155 - x194)^2 + (x295 - x334)^2) + 1
    / sqrt((x15 - x55)^2 + (x155 - x195)^2 + (x295 - x335)^2) + 1 / sqrt((x15
    - x56)^2 + (x155 - x196)^2 + (x295 - x336)^2) + 1 / sqrt((x15 - x57)^2 + (
    x155 - x197)^2 + (x295 - x337)^2) + 1 / sqrt((x15 - x58)^2 + (x155 - x198)^
    2 + (x295 - x338)^2) + 1 / sqrt((x15 - x59)^2 + (x155 - x199)^2 + (x295 -
    x339)^2) + 1 / sqrt((x15 - x60)^2 + (x155 - x200)^2 + (x295 - x340)^2) + 1
    / sqrt((x15 - x61)^2 + (x155 - x201)^2 + (x295 - x341)^2) + 1 / sqrt((x15
    - x62)^2 + (x155 - x202)^2 + (x295 - x342)^2) + 1 / sqrt((x15 - x63)^2 + (
    x155 - x203)^2 + (x295 - x343)^2) + 1 / sqrt((x15 - x64)^2 + (x155 - x204)^
    2 + (x295 - x344)^2) + 1 / sqrt((x15 - x65)^2 + (x155 - x205)^2 + (x295 -
    x345)^2) + 1 / sqrt((x15 - x66)^2 + (x155 - x206)^2 + (x295 - x346)^2) + 1
    / sqrt((x15 - x67)^2 + (x155 - x207)^2 + (x295 - x347)^2) + 1 / sqrt((x15
    - x68)^2 + (x155 - x208)^2 + (x295 - x348)^2) + 1 / sqrt((x15 - x69)^2 + (
    x155 - x209)^2 + (x295 - x349)^2) + 1 / sqrt((x15 - x70)^2 + (x155 - x210)^
    2 + (x295 - x350)^2) + 1 / sqrt((x15 - x71)^2 + (x155 - x211)^2 + (x295 -
    x351)^2) + 1 / sqrt((x15 - x72)^2 + (x155 - x212)^2 + (x295 - x352)^2) + 1
    / sqrt((x15 - x73)^2 + (x155 - x213)^2 + (x295 - x353)^2) + 1 / sqrt((x15
    - x74)^2 + (x155 - x214)^2 + (x295 - x354)^2) + 1 / sqrt((x15 - x75)^2 + (
    x155 - x215)^2 + (x295 - x355)^2) + 1 / sqrt((x15 - x76)^2 + (x155 - x216)^
    2 + (x295 - x356)^2) + 1 / sqrt((x15 - x77)^2 + (x155 - x217)^2 + (x295 -
    x357)^2) + 1 / sqrt((x15 - x78)^2 + (x155 - x218)^2 + (x295 - x358)^2) + 1
    / sqrt((x15 - x79)^2 + (x155 - x219)^2 + (x295 - x359)^2) + 1 / sqrt((x15
    - x80)^2 + (x155 - x220)^2 + (x295 - x360)^2) + 1 / sqrt((x15 - x81)^2 + (
    x155 - x221)^2 + (x295 - x361)^2) + 1 / sqrt((x15 - x82)^2 + (x155 - x222)^
    2 + (x295 - x362)^2) + 1 / sqrt((x15 - x83)^2 + (x155 - x223)^2 + (x295 -
    x363)^2) + 1 / sqrt((x15 - x84)^2 + (x155 - x224)^2 + (x295 - x364)^2) + 1
    / sqrt((x15 - x85)^2 + (x155 - x225)^2 + (x295 - x365)^2) + 1 / sqrt((x15
    - x86)^2 + (x155 - x226)^2 + (x295 - x366)^2) + 1 / sqrt((x15 - x87)^2 + (
    x155 - x227)^2 + (x295 - x367)^2) + 1 / sqrt((x15 - x88)^2 + (x155 - x228)^
    2 + (x295 - x368)^2) + 1 / sqrt((x15 - x89)^2 + (x155 - x229)^2 + (x295 -
    x369)^2) + 1 / sqrt((x15 - x90)^2 + (x155 - x230)^2 + (x295 - x370)^2) + 1
    / sqrt((x15 - x91)^2 + (x155 - x231)^2 + (x295 - x371)^2) + 1 / sqrt((x15
    - x92)^2 + (x155 - x232)^2 + (x295 - x372)^2) + 1 / sqrt((x15 - x93)^2 + (
    x155 - x233)^2 + (x295 - x373)^2) + 1 / sqrt((x15 - x94)^2 + (x155 - x234)^
    2 + (x295 - x374)^2) + 1 / sqrt((x15 - x95)^2 + (x155 - x235)^2 + (x295 -
    x375)^2) + 1 / sqrt((x15 - x96)^2 + (x155 - x236)^2 + (x295 - x376)^2) + 1
    / sqrt((x15 - x97)^2 + (x155 - x237)^2 + (x295 - x377)^2) + 1 / sqrt((x15
    - x98)^2 + (x155 - x238)^2 + (x295 - x378)^2) + 1 / sqrt((x15 - x99)^2 + (
    x155 - x239)^2 + (x295 - x379)^2) + 1 / sqrt((x15 - x100)^2 + (x155 - x240)
    ^2 + (x295 - x380)^2) + 1 / sqrt((x15 - x101)^2 + (x155 - x241)^2 + (x295
    - x381)^2) + 1 / sqrt((x15 - x102)^2 + (x155 - x242)^2 + (x295 - x382)^2)
    + 1 / sqrt((x15 - x103)^2 + (x155 - x243)^2 + (x295 - x383)^2) + 1 / sqrt(
    (x15 - x104)^2 + (x155 - x244)^2 + (x295 - x384)^2) + 1 / sqrt((x15 - x105)
    ^2 + (x155 - x245)^2 + (x295 - x385)^2) + 1 / sqrt((x15 - x106)^2 + (x155
    - x246)^2 + (x295 - x386)^2) + 1 / sqrt((x15 - x107)^2 + (x155 - x247)^2
    + (x295 - x387)^2) + 1 / sqrt((x15 - x108)^2 + (x155 - x248)^2 + (x295 -
    x388)^2) + 1 / sqrt((x15 - x109)^2 + (x155 - x249)^2 + (x295 - x389)^2) + 1
    / sqrt((x15 - x110)^2 + (x155 - x250)^2 + (x295 - x390)^2) + 1 / sqrt((x15
    - x111)^2 + (x155 - x251)^2 + (x295 - x391)^2) + 1 / sqrt((x15 - x112)^2
    + (x155 - x252)^2 + (x295 - x392)^2) + 1 / sqrt((x15 - x113)^2 + (x155 -
    x253)^2 + (x295 - x393)^2) + 1 / sqrt((x15 - x114)^2 + (x155 - x254)^2 + (
    x295 - x394)^2) + 1 / sqrt((x15 - x115)^2 + (x155 - x255)^2 + (x295 - x395)
    ^2) + 1 / sqrt((x15 - x116)^2 + (x155 - x256)^2 + (x295 - x396)^2) + 1 /
    sqrt((x15 - x117)^2 + (x155 - x257)^2 + (x295 - x397)^2) + 1 / sqrt((x15 -
    x118)^2 + (x155 - x258)^2 + (x295 - x398)^2) + 1 / sqrt((x15 - x119)^2 + (
    x155 - x259)^2 + (x295 - x399)^2) + 1 / sqrt((x15 - x120)^2 + (x155 - x260)
    ^2 + (x295 - x400)^2) + 1 / sqrt((x15 - x121)^2 + (x155 - x261)^2 + (x295
    - x401)^2) + 1 / sqrt((x15 - x122)^2 + (x155 - x262)^2 + (x295 - x402)^2)
    + 1 / sqrt((x15 - x123)^2 + (x155 - x263)^2 + (x295 - x403)^2) + 1 / sqrt(
    (x15 - x124)^2 + (x155 - x264)^2 + (x295 - x404)^2) + 1 / sqrt((x15 - x125)
    ^2 + (x155 - x265)^2 + (x295 - x405)^2) + 1 / sqrt((x15 - x126)^2 + (x155
    - x266)^2 + (x295 - x406)^2) + 1 / sqrt((x15 - x127)^2 + (x155 - x267)^2
    + (x295 - x407)^2) + 1 / sqrt((x15 - x128)^2 + (x155 - x268)^2 + (x295 -
    x408)^2) + 1 / sqrt((x15 - x129)^2 + (x155 - x269)^2 + (x295 - x409)^2) + 1
    / sqrt((x15 - x130)^2 + (x155 - x270)^2 + (x295 - x410)^2) + 1 / sqrt((x15
    - x131)^2 + (x155 - x271)^2 + (x295 - x411)^2) + 1 / sqrt((x15 - x132)^2
    + (x155 - x272)^2 + (x295 - x412)^2) + 1 / sqrt((x15 - x133)^2 + (x155 -
    x273)^2 + (x295 - x413)^2) + 1 / sqrt((x15 - x134)^2 + (x155 - x274)^2 + (
    x295 - x414)^2) + 1 / sqrt((x15 - x135)^2 + (x155 - x275)^2 + (x295 - x415)
    ^2) + 1 / sqrt((x15 - x136)^2 + (x155 - x276)^2 + (x295 - x416)^2) + 1 /
    sqrt((x15 - x137)^2 + (x155 - x277)^2 + (x295 - x417)^2) + 1 / sqrt((x15 -
    x138)^2 + (x155 - x278)^2 + (x295 - x418)^2) + 1 / sqrt((x15 - x139)^2 + (
    x155 - x279)^2 + (x295 - x419)^2) + 1 / sqrt((x15 - x140)^2 + (x155 - x280)
    ^2 + (x295 - x420)^2) + 1 / sqrt((x16 - x17)^2 + (x156 - x157)^2 + (x296 -
    x297)^2) + 1 / sqrt((x16 - x18)^2 + (x156 - x158)^2 + (x296 - x298)^2) + 1
    / sqrt((x16 - x19)^2 + (x156 - x159)^2 + (x296 - x299)^2) + 1 / sqrt((x16
    - x20)^2 + (x156 - x160)^2 + (x296 - x300)^2) + 1 / sqrt((x16 - x21)^2 + (
    x156 - x161)^2 + (x296 - x301)^2) + 1 / sqrt((x16 - x22)^2 + (x156 - x162)^
    2 + (x296 - x302)^2) + 1 / sqrt((x16 - x23)^2 + (x156 - x163)^2 + (x296 -
    x303)^2) + 1 / sqrt((x16 - x24)^2 + (x156 - x164)^2 + (x296 - x304)^2) + 1
    / sqrt((x16 - x25)^2 + (x156 - x165)^2 + (x296 - x305)^2) + 1 / sqrt((x16
    - x26)^2 + (x156 - x166)^2 + (x296 - x306)^2) + 1 / sqrt((x16 - x27)^2 + (
    x156 - x167)^2 + (x296 - x307)^2) + 1 / sqrt((x16 - x28)^2 + (x156 - x168)^
    2 + (x296 - x308)^2) + 1 / sqrt((x16 - x29)^2 + (x156 - x169)^2 + (x296 -
    x309)^2) + 1 / sqrt((x16 - x30)^2 + (x156 - x170)^2 + (x296 - x310)^2) + 1
    / sqrt((x16 - x31)^2 + (x156 - x171)^2 + (x296 - x311)^2) + 1 / sqrt((x16
    - x32)^2 + (x156 - x172)^2 + (x296 - x312)^2) + 1 / sqrt((x16 - x33)^2 + (
    x156 - x173)^2 + (x296 - x313)^2) + 1 / sqrt((x16 - x34)^2 + (x156 - x174)^
    2 + (x296 - x314)^2) + 1 / sqrt((x16 - x35)^2 + (x156 - x175)^2 + (x296 -
    x315)^2) + 1 / sqrt((x16 - x36)^2 + (x156 - x176)^2 + (x296 - x316)^2) + 1
    / sqrt((x16 - x37)^2 + (x156 - x177)^2 + (x296 - x317)^2) + 1 / sqrt((x16
    - x38)^2 + (x156 - x178)^2 + (x296 - x318)^2) + 1 / sqrt((x16 - x39)^2 + (
    x156 - x179)^2 + (x296 - x319)^2) + 1 / sqrt((x16 - x40)^2 + (x156 - x180)^
    2 + (x296 - x320)^2) + 1 / sqrt((x16 - x41)^2 + (x156 - x181)^2 + (x296 -
    x321)^2) + 1 / sqrt((x16 - x42)^2 + (x156 - x182)^2 + (x296 - x322)^2) + 1
    / sqrt((x16 - x43)^2 + (x156 - x183)^2 + (x296 - x323)^2) + 1 / sqrt((x16
    - x44)^2 + (x156 - x184)^2 + (x296 - x324)^2) + 1 / sqrt((x16 - x45)^2 + (
    x156 - x185)^2 + (x296 - x325)^2) + 1 / sqrt((x16 - x46)^2 + (x156 - x186)^
    2 + (x296 - x326)^2) + 1 / sqrt((x16 - x47)^2 + (x156 - x187)^2 + (x296 -
    x327)^2) + 1 / sqrt((x16 - x48)^2 + (x156 - x188)^2 + (x296 - x328)^2) + 1
    / sqrt((x16 - x49)^2 + (x156 - x189)^2 + (x296 - x329)^2) + 1 / sqrt((x16
    - x50)^2 + (x156 - x190)^2 + (x296 - x330)^2) + 1 / sqrt((x16 - x51)^2 + (
    x156 - x191)^2 + (x296 - x331)^2) + 1 / sqrt((x16 - x52)^2 + (x156 - x192)^
    2 + (x296 - x332)^2) + 1 / sqrt((x16 - x53)^2 + (x156 - x193)^2 + (x296 -
    x333)^2) + 1 / sqrt((x16 - x54)^2 + (x156 - x194)^2 + (x296 - x334)^2) + 1
    / sqrt((x16 - x55)^2 + (x156 - x195)^2 + (x296 - x335)^2) + 1 / sqrt((x16
    - x56)^2 + (x156 - x196)^2 + (x296 - x336)^2) + 1 / sqrt((x16 - x57)^2 + (
    x156 - x197)^2 + (x296 - x337)^2) + 1 / sqrt((x16 - x58)^2 + (x156 - x198)^
    2 + (x296 - x338)^2) + 1 / sqrt((x16 - x59)^2 + (x156 - x199)^2 + (x296 -
    x339)^2) + 1 / sqrt((x16 - x60)^2 + (x156 - x200)^2 + (x296 - x340)^2) + 1
    / sqrt((x16 - x61)^2 + (x156 - x201)^2 + (x296 - x341)^2) + 1 / sqrt((x16
    - x62)^2 + (x156 - x202)^2 + (x296 - x342)^2) + 1 / sqrt((x16 - x63)^2 + (
    x156 - x203)^2 + (x296 - x343)^2) + 1 / sqrt((x16 - x64)^2 + (x156 - x204)^
    2 + (x296 - x344)^2) + 1 / sqrt((x16 - x65)^2 + (x156 - x205)^2 + (x296 -
    x345)^2) + 1 / sqrt((x16 - x66)^2 + (x156 - x206)^2 + (x296 - x346)^2) + 1
    / sqrt((x16 - x67)^2 + (x156 - x207)^2 + (x296 - x347)^2) + 1 / sqrt((x16
    - x68)^2 + (x156 - x208)^2 + (x296 - x348)^2) + 1 / sqrt((x16 - x69)^2 + (
    x156 - x209)^2 + (x296 - x349)^2) + 1 / sqrt((x16 - x70)^2 + (x156 - x210)^
    2 + (x296 - x350)^2) + 1 / sqrt((x16 - x71)^2 + (x156 - x211)^2 + (x296 -
    x351)^2) + 1 / sqrt((x16 - x72)^2 + (x156 - x212)^2 + (x296 - x352)^2) + 1
    / sqrt((x16 - x73)^2 + (x156 - x213)^2 + (x296 - x353)^2) + 1 / sqrt((x16
    - x74)^2 + (x156 - x214)^2 + (x296 - x354)^2) + 1 / sqrt((x16 - x75)^2 + (
    x156 - x215)^2 + (x296 - x355)^2) + 1 / sqrt((x16 - x76)^2 + (x156 - x216)^
    2 + (x296 - x356)^2) + 1 / sqrt((x16 - x77)^2 + (x156 - x217)^2 + (x296 -
    x357)^2) + 1 / sqrt((x16 - x78)^2 + (x156 - x218)^2 + (x296 - x358)^2) + 1
    / sqrt((x16 - x79)^2 + (x156 - x219)^2 + (x296 - x359)^2) + 1 / sqrt((x16
    - x80)^2 + (x156 - x220)^2 + (x296 - x360)^2) + 1 / sqrt((x16 - x81)^2 + (
    x156 - x221)^2 + (x296 - x361)^2) + 1 / sqrt((x16 - x82)^2 + (x156 - x222)^
    2 + (x296 - x362)^2) + 1 / sqrt((x16 - x83)^2 + (x156 - x223)^2 + (x296 -
    x363)^2) + 1 / sqrt((x16 - x84)^2 + (x156 - x224)^2 + (x296 - x364)^2) + 1
    / sqrt((x16 - x85)^2 + (x156 - x225)^2 + (x296 - x365)^2) + 1 / sqrt((x16
    - x86)^2 + (x156 - x226)^2 + (x296 - x366)^2) + 1 / sqrt((x16 - x87)^2 + (
    x156 - x227)^2 + (x296 - x367)^2) + 1 / sqrt((x16 - x88)^2 + (x156 - x228)^
    2 + (x296 - x368)^2) + 1 / sqrt((x16 - x89)^2 + (x156 - x229)^2 + (x296 -
    x369)^2) + 1 / sqrt((x16 - x90)^2 + (x156 - x230)^2 + (x296 - x370)^2) + 1
    / sqrt((x16 - x91)^2 + (x156 - x231)^2 + (x296 - x371)^2) + 1 / sqrt((x16
    - x92)^2 + (x156 - x232)^2 + (x296 - x372)^2) + 1 / sqrt((x16 - x93)^2 + (
    x156 - x233)^2 + (x296 - x373)^2) + 1 / sqrt((x16 - x94)^2 + (x156 - x234)^
    2 + (x296 - x374)^2) + 1 / sqrt((x16 - x95)^2 + (x156 - x235)^2 + (x296 -
    x375)^2) + 1 / sqrt((x16 - x96)^2 + (x156 - x236)^2 + (x296 - x376)^2) + 1
    / sqrt((x16 - x97)^2 + (x156 - x237)^2 + (x296 - x377)^2) + 1 / sqrt((x16
    - x98)^2 + (x156 - x238)^2 + (x296 - x378)^2) + 1 / sqrt((x16 - x99)^2 + (
    x156 - x239)^2 + (x296 - x379)^2) + 1 / sqrt((x16 - x100)^2 + (x156 - x240)
    ^2 + (x296 - x380)^2) + 1 / sqrt((x16 - x101)^2 + (x156 - x241)^2 + (x296
    - x381)^2) + 1 / sqrt((x16 - x102)^2 + (x156 - x242)^2 + (x296 - x382)^2)
    + 1 / sqrt((x16 - x103)^2 + (x156 - x243)^2 + (x296 - x383)^2) + 1 / sqrt(
    (x16 - x104)^2 + (x156 - x244)^2 + (x296 - x384)^2) + 1 / sqrt((x16 - x105)
    ^2 + (x156 - x245)^2 + (x296 - x385)^2) + 1 / sqrt((x16 - x106)^2 + (x156
    - x246)^2 + (x296 - x386)^2) + 1 / sqrt((x16 - x107)^2 + (x156 - x247)^2
    + (x296 - x387)^2) + 1 / sqrt((x16 - x108)^2 + (x156 - x248)^2 + (x296 -
    x388)^2) + 1 / sqrt((x16 - x109)^2 + (x156 - x249)^2 + (x296 - x389)^2) + 1
    / sqrt((x16 - x110)^2 + (x156 - x250)^2 + (x296 - x390)^2) + 1 / sqrt((x16
    - x111)^2 + (x156 - x251)^2 + (x296 - x391)^2) + 1 / sqrt((x16 - x112)^2
    + (x156 - x252)^2 + (x296 - x392)^2) + 1 / sqrt((x16 - x113)^2 + (x156 -
    x253)^2 + (x296 - x393)^2) + 1 / sqrt((x16 - x114)^2 + (x156 - x254)^2 + (
    x296 - x394)^2) + 1 / sqrt((x16 - x115)^2 + (x156 - x255)^2 + (x296 - x395)
    ^2) + 1 / sqrt((x16 - x116)^2 + (x156 - x256)^2 + (x296 - x396)^2) + 1 /
    sqrt((x16 - x117)^2 + (x156 - x257)^2 + (x296 - x397)^2) + 1 / sqrt((x16 -
    x118)^2 + (x156 - x258)^2 + (x296 - x398)^2) + 1 / sqrt((x16 - x119)^2 + (
    x156 - x259)^2 + (x296 - x399)^2) + 1 / sqrt((x16 - x120)^2 + (x156 - x260)
    ^2 + (x296 - x400)^2) + 1 / sqrt((x16 - x121)^2 + (x156 - x261)^2 + (x296
    - x401)^2) + 1 / sqrt((x16 - x122)^2 + (x156 - x262)^2 + (x296 - x402)^2)
    + 1 / sqrt((x16 - x123)^2 + (x156 - x263)^2 + (x296 - x403)^2) + 1 / sqrt(
    (x16 - x124)^2 + (x156 - x264)^2 + (x296 - x404)^2) + 1 / sqrt((x16 - x125)
    ^2 + (x156 - x265)^2 + (x296 - x405)^2) + 1 / sqrt((x16 - x126)^2 + (x156
    - x266)^2 + (x296 - x406)^2) + 1 / sqrt((x16 - x127)^2 + (x156 - x267)^2
    + (x296 - x407)^2) + 1 / sqrt((x16 - x128)^2 + (x156 - x268)^2 + (x296 -
    x408)^2) + 1 / sqrt((x16 - x129)^2 + (x156 - x269)^2 + (x296 - x409)^2) + 1
    / sqrt((x16 - x130)^2 + (x156 - x270)^2 + (x296 - x410)^2) + 1 / sqrt((x16
    - x131)^2 + (x156 - x271)^2 + (x296 - x411)^2) + 1 / sqrt((x16 - x132)^2
    + (x156 - x272)^2 + (x296 - x412)^2) + 1 / sqrt((x16 - x133)^2 + (x156 -
    x273)^2 + (x296 - x413)^2) + 1 / sqrt((x16 - x134)^2 + (x156 - x274)^2 + (
    x296 - x414)^2) + 1 / sqrt((x16 - x135)^2 + (x156 - x275)^2 + (x296 - x415)
    ^2) + 1 / sqrt((x16 - x136)^2 + (x156 - x276)^2 + (x296 - x416)^2) + 1 /
    sqrt((x16 - x137)^2 + (x156 - x277)^2 + (x296 - x417)^2) + 1 / sqrt((x16 -
    x138)^2 + (x156 - x278)^2 + (x296 - x418)^2) + 1 / sqrt((x16 - x139)^2 + (
    x156 - x279)^2 + (x296 - x419)^2) + 1 / sqrt((x16 - x140)^2 + (x156 - x280)
    ^2 + (x296 - x420)^2) + 1 / sqrt((x17 - x18)^2 + (x157 - x158)^2 + (x297 -
    x298)^2) + 1 / sqrt((x17 - x19)^2 + (x157 - x159)^2 + (x297 - x299)^2) + 1
    / sqrt((x17 - x20)^2 + (x157 - x160)^2 + (x297 - x300)^2) + 1 / sqrt((x17
    - x21)^2 + (x157 - x161)^2 + (x297 - x301)^2) + 1 / sqrt((x17 - x22)^2 + (
    x157 - x162)^2 + (x297 - x302)^2) + 1 / sqrt((x17 - x23)^2 + (x157 - x163)^
    2 + (x297 - x303)^2) + 1 / sqrt((x17 - x24)^2 + (x157 - x164)^2 + (x297 -
    x304)^2) + 1 / sqrt((x17 - x25)^2 + (x157 - x165)^2 + (x297 - x305)^2) + 1
    / sqrt((x17 - x26)^2 + (x157 - x166)^2 + (x297 - x306)^2) + 1 / sqrt((x17
    - x27)^2 + (x157 - x167)^2 + (x297 - x307)^2) + 1 / sqrt((x17 - x28)^2 + (
    x157 - x168)^2 + (x297 - x308)^2) + 1 / sqrt((x17 - x29)^2 + (x157 - x169)^
    2 + (x297 - x309)^2) + 1 / sqrt((x17 - x30)^2 + (x157 - x170)^2 + (x297 -
    x310)^2) + 1 / sqrt((x17 - x31)^2 + (x157 - x171)^2 + (x297 - x311)^2) + 1
    / sqrt((x17 - x32)^2 + (x157 - x172)^2 + (x297 - x312)^2) + 1 / sqrt((x17
    - x33)^2 + (x157 - x173)^2 + (x297 - x313)^2) + 1 / sqrt((x17 - x34)^2 + (
    x157 - x174)^2 + (x297 - x314)^2) + 1 / sqrt((x17 - x35)^2 + (x157 - x175)^
    2 + (x297 - x315)^2) + 1 / sqrt((x17 - x36)^2 + (x157 - x176)^2 + (x297 -
    x316)^2) + 1 / sqrt((x17 - x37)^2 + (x157 - x177)^2 + (x297 - x317)^2) + 1
    / sqrt((x17 - x38)^2 + (x157 - x178)^2 + (x297 - x318)^2) + 1 / sqrt((x17
    - x39)^2 + (x157 - x179)^2 + (x297 - x319)^2) + 1 / sqrt((x17 - x40)^2 + (
    x157 - x180)^2 + (x297 - x320)^2) + 1 / sqrt((x17 - x41)^2 + (x157 - x181)^
    2 + (x297 - x321)^2) + 1 / sqrt((x17 - x42)^2 + (x157 - x182)^2 + (x297 -
    x322)^2) + 1 / sqrt((x17 - x43)^2 + (x157 - x183)^2 + (x297 - x323)^2) + 1
    / sqrt((x17 - x44)^2 + (x157 - x184)^2 + (x297 - x324)^2) + 1 / sqrt((x17
    - x45)^2 + (x157 - x185)^2 + (x297 - x325)^2) + 1 / sqrt((x17 - x46)^2 + (
    x157 - x186)^2 + (x297 - x326)^2) + 1 / sqrt((x17 - x47)^2 + (x157 - x187)^
    2 + (x297 - x327)^2) + 1 / sqrt((x17 - x48)^2 + (x157 - x188)^2 + (x297 -
    x328)^2) + 1 / sqrt((x17 - x49)^2 + (x157 - x189)^2 + (x297 - x329)^2) + 1
    / sqrt((x17 - x50)^2 + (x157 - x190)^2 + (x297 - x330)^2) + 1 / sqrt((x17
    - x51)^2 + (x157 - x191)^2 + (x297 - x331)^2) + 1 / sqrt((x17 - x52)^2 + (
    x157 - x192)^2 + (x297 - x332)^2) + 1 / sqrt((x17 - x53)^2 + (x157 - x193)^
    2 + (x297 - x333)^2) + 1 / sqrt((x17 - x54)^2 + (x157 - x194)^2 + (x297 -
    x334)^2) + 1 / sqrt((x17 - x55)^2 + (x157 - x195)^2 + (x297 - x335)^2) + 1
    / sqrt((x17 - x56)^2 + (x157 - x196)^2 + (x297 - x336)^2) + 1 / sqrt((x17
    - x57)^2 + (x157 - x197)^2 + (x297 - x337)^2) + 1 / sqrt((x17 - x58)^2 + (
    x157 - x198)^2 + (x297 - x338)^2) + 1 / sqrt((x17 - x59)^2 + (x157 - x199)^
    2 + (x297 - x339)^2) + 1 / sqrt((x17 - x60)^2 + (x157 - x200)^2 + (x297 -
    x340)^2) + 1 / sqrt((x17 - x61)^2 + (x157 - x201)^2 + (x297 - x341)^2) + 1
    / sqrt((x17 - x62)^2 + (x157 - x202)^2 + (x297 - x342)^2) + 1 / sqrt((x17
    - x63)^2 + (x157 - x203)^2 + (x297 - x343)^2) + 1 / sqrt((x17 - x64)^2 + (
    x157 - x204)^2 + (x297 - x344)^2) + 1 / sqrt((x17 - x65)^2 + (x157 - x205)^
    2 + (x297 - x345)^2) + 1 / sqrt((x17 - x66)^2 + (x157 - x206)^2 + (x297 -
    x346)^2) + 1 / sqrt((x17 - x67)^2 + (x157 - x207)^2 + (x297 - x347)^2) + 1
    / sqrt((x17 - x68)^2 + (x157 - x208)^2 + (x297 - x348)^2) + 1 / sqrt((x17
    - x69)^2 + (x157 - x209)^2 + (x297 - x349)^2) + 1 / sqrt((x17 - x70)^2 + (
    x157 - x210)^2 + (x297 - x350)^2) + 1 / sqrt((x17 - x71)^2 + (x157 - x211)^
    2 + (x297 - x351)^2) + 1 / sqrt((x17 - x72)^2 + (x157 - x212)^2 + (x297 -
    x352)^2) + 1 / sqrt((x17 - x73)^2 + (x157 - x213)^2 + (x297 - x353)^2) + 1
    / sqrt((x17 - x74)^2 + (x157 - x214)^2 + (x297 - x354)^2) + 1 / sqrt((x17
    - x75)^2 + (x157 - x215)^2 + (x297 - x355)^2) + 1 / sqrt((x17 - x76)^2 + (
    x157 - x216)^2 + (x297 - x356)^2) + 1 / sqrt((x17 - x77)^2 + (x157 - x217)^
    2 + (x297 - x357)^2) + 1 / sqrt((x17 - x78)^2 + (x157 - x218)^2 + (x297 -
    x358)^2) + 1 / sqrt((x17 - x79)^2 + (x157 - x219)^2 + (x297 - x359)^2) + 1
    / sqrt((x17 - x80)^2 + (x157 - x220)^2 + (x297 - x360)^2) + 1 / sqrt((x17
    - x81)^2 + (x157 - x221)^2 + (x297 - x361)^2) + 1 / sqrt((x17 - x82)^2 + (
    x157 - x222)^2 + (x297 - x362)^2) + 1 / sqrt((x17 - x83)^2 + (x157 - x223)^
    2 + (x297 - x363)^2) + 1 / sqrt((x17 - x84)^2 + (x157 - x224)^2 + (x297 -
    x364)^2) + 1 / sqrt((x17 - x85)^2 + (x157 - x225)^2 + (x297 - x365)^2) + 1
    / sqrt((x17 - x86)^2 + (x157 - x226)^2 + (x297 - x366)^2) + 1 / sqrt((x17
    - x87)^2 + (x157 - x227)^2 + (x297 - x367)^2) + 1 / sqrt((x17 - x88)^2 + (
    x157 - x228)^2 + (x297 - x368)^2) + 1 / sqrt((x17 - x89)^2 + (x157 - x229)^
    2 + (x297 - x369)^2) + 1 / sqrt((x17 - x90)^2 + (x157 - x230)^2 + (x297 -
    x370)^2) + 1 / sqrt((x17 - x91)^2 + (x157 - x231)^2 + (x297 - x371)^2) + 1
    / sqrt((x17 - x92)^2 + (x157 - x232)^2 + (x297 - x372)^2) + 1 / sqrt((x17
    - x93)^2 + (x157 - x233)^2 + (x297 - x373)^2) + 1 / sqrt((x17 - x94)^2 + (
    x157 - x234)^2 + (x297 - x374)^2) + 1 / sqrt((x17 - x95)^2 + (x157 - x235)^
    2 + (x297 - x375)^2) + 1 / sqrt((x17 - x96)^2 + (x157 - x236)^2 + (x297 -
    x376)^2) + 1 / sqrt((x17 - x97)^2 + (x157 - x237)^2 + (x297 - x377)^2) + 1
    / sqrt((x17 - x98)^2 + (x157 - x238)^2 + (x297 - x378)^2) + 1 / sqrt((x17
    - x99)^2 + (x157 - x239)^2 + (x297 - x379)^2) + 1 / sqrt((x17 - x100)^2 +
    (x157 - x240)^2 + (x297 - x380)^2) + 1 / sqrt((x17 - x101)^2 + (x157 - x241)
    ^2 + (x297 - x381)^2) + 1 / sqrt((x17 - x102)^2 + (x157 - x242)^2 + (x297
    - x382)^2) + 1 / sqrt((x17 - x103)^2 + (x157 - x243)^2 + (x297 - x383)^2)
    + 1 / sqrt((x17 - x104)^2 + (x157 - x244)^2 + (x297 - x384)^2) + 1 / sqrt(
    (x17 - x105)^2 + (x157 - x245)^2 + (x297 - x385)^2) + 1 / sqrt((x17 - x106)
    ^2 + (x157 - x246)^2 + (x297 - x386)^2) + 1 / sqrt((x17 - x107)^2 + (x157
    - x247)^2 + (x297 - x387)^2) + 1 / sqrt((x17 - x108)^2 + (x157 - x248)^2
    + (x297 - x388)^2) + 1 / sqrt((x17 - x109)^2 + (x157 - x249)^2 + (x297 -
    x389)^2) + 1 / sqrt((x17 - x110)^2 + (x157 - x250)^2 + (x297 - x390)^2) + 1
    / sqrt((x17 - x111)^2 + (x157 - x251)^2 + (x297 - x391)^2) + 1 / sqrt((x17
    - x112)^2 + (x157 - x252)^2 + (x297 - x392)^2) + 1 / sqrt((x17 - x113)^2
    + (x157 - x253)^2 + (x297 - x393)^2) + 1 / sqrt((x17 - x114)^2 + (x157 -
    x254)^2 + (x297 - x394)^2) + 1 / sqrt((x17 - x115)^2 + (x157 - x255)^2 + (
    x297 - x395)^2) + 1 / sqrt((x17 - x116)^2 + (x157 - x256)^2 + (x297 - x396)
    ^2) + 1 / sqrt((x17 - x117)^2 + (x157 - x257)^2 + (x297 - x397)^2) + 1 /
    sqrt((x17 - x118)^2 + (x157 - x258)^2 + (x297 - x398)^2) + 1 / sqrt((x17 -
    x119)^2 + (x157 - x259)^2 + (x297 - x399)^2) + 1 / sqrt((x17 - x120)^2 + (
    x157 - x260)^2 + (x297 - x400)^2) + 1 / sqrt((x17 - x121)^2 + (x157 - x261)
    ^2 + (x297 - x401)^2) + 1 / sqrt((x17 - x122)^2 + (x157 - x262)^2 + (x297
    - x402)^2) + 1 / sqrt((x17 - x123)^2 + (x157 - x263)^2 + (x297 - x403)^2)
    + 1 / sqrt((x17 - x124)^2 + (x157 - x264)^2 + (x297 - x404)^2) + 1 / sqrt(
    (x17 - x125)^2 + (x157 - x265)^2 + (x297 - x405)^2) + 1 / sqrt((x17 - x126)
    ^2 + (x157 - x266)^2 + (x297 - x406)^2) + 1 / sqrt((x17 - x127)^2 + (x157
    - x267)^2 + (x297 - x407)^2) + 1 / sqrt((x17 - x128)^2 + (x157 - x268)^2
    + (x297 - x408)^2) + 1 / sqrt((x17 - x129)^2 + (x157 - x269)^2 + (x297 -
    x409)^2) + 1 / sqrt((x17 - x130)^2 + (x157 - x270)^2 + (x297 - x410)^2) + 1
    / sqrt((x17 - x131)^2 + (x157 - x271)^2 + (x297 - x411)^2) + 1 / sqrt((x17
    - x132)^2 + (x157 - x272)^2 + (x297 - x412)^2) + 1 / sqrt((x17 - x133)^2
    + (x157 - x273)^2 + (x297 - x413)^2) + 1 / sqrt((x17 - x134)^2 + (x157 -
    x274)^2 + (x297 - x414)^2) + 1 / sqrt((x17 - x135)^2 + (x157 - x275)^2 + (
    x297 - x415)^2) + 1 / sqrt((x17 - x136)^2 + (x157 - x276)^2 + (x297 - x416)
    ^2) + 1 / sqrt((x17 - x137)^2 + (x157 - x277)^2 + (x297 - x417)^2) + 1 /
    sqrt((x17 - x138)^2 + (x157 - x278)^2 + (x297 - x418)^2) + 1 / sqrt((x17 -
    x139)^2 + (x157 - x279)^2 + (x297 - x419)^2) + 1 / sqrt((x17 - x140)^2 + (
    x157 - x280)^2 + (x297 - x420)^2) + 1 / sqrt((x18 - x19)^2 + (x158 - x159)^
    2 + (x298 - x299)^2) + 1 / sqrt((x18 - x20)^2 + (x158 - x160)^2 + (x298 -
    x300)^2) + 1 / sqrt((x18 - x21)^2 + (x158 - x161)^2 + (x298 - x301)^2) + 1
    / sqrt((x18 - x22)^2 + (x158 - x162)^2 + (x298 - x302)^2) + 1 / sqrt((x18
    - x23)^2 + (x158 - x163)^2 + (x298 - x303)^2) + 1 / sqrt((x18 - x24)^2 + (
    x158 - x164)^2 + (x298 - x304)^2) + 1 / sqrt((x18 - x25)^2 + (x158 - x165)^
    2 + (x298 - x305)^2) + 1 / sqrt((x18 - x26)^2 + (x158 - x166)^2 + (x298 -
    x306)^2) + 1 / sqrt((x18 - x27)^2 + (x158 - x167)^2 + (x298 - x307)^2) + 1
    / sqrt((x18 - x28)^2 + (x158 - x168)^2 + (x298 - x308)^2) + 1 / sqrt((x18
    - x29)^2 + (x158 - x169)^2 + (x298 - x309)^2) + 1 / sqrt((x18 - x30)^2 + (
    x158 - x170)^2 + (x298 - x310)^2) + 1 / sqrt((x18 - x31)^2 + (x158 - x171)^
    2 + (x298 - x311)^2) + 1 / sqrt((x18 - x32)^2 + (x158 - x172)^2 + (x298 -
    x312)^2) + 1 / sqrt((x18 - x33)^2 + (x158 - x173)^2 + (x298 - x313)^2) + 1
    / sqrt((x18 - x34)^2 + (x158 - x174)^2 + (x298 - x314)^2) + 1 / sqrt((x18
    - x35)^2 + (x158 - x175)^2 + (x298 - x315)^2) + 1 / sqrt((x18 - x36)^2 + (
    x158 - x176)^2 + (x298 - x316)^2) + 1 / sqrt((x18 - x37)^2 + (x158 - x177)^
    2 + (x298 - x317)^2) + 1 / sqrt((x18 - x38)^2 + (x158 - x178)^2 + (x298 -
    x318)^2) + 1 / sqrt((x18 - x39)^2 + (x158 - x179)^2 + (x298 - x319)^2) + 1
    / sqrt((x18 - x40)^2 + (x158 - x180)^2 + (x298 - x320)^2) + 1 / sqrt((x18
    - x41)^2 + (x158 - x181)^2 + (x298 - x321)^2) + 1 / sqrt((x18 - x42)^2 + (
    x158 - x182)^2 + (x298 - x322)^2) + 1 / sqrt((x18 - x43)^2 + (x158 - x183)^
    2 + (x298 - x323)^2) + 1 / sqrt((x18 - x44)^2 + (x158 - x184)^2 + (x298 -
    x324)^2) + 1 / sqrt((x18 - x45)^2 + (x158 - x185)^2 + (x298 - x325)^2) + 1
    / sqrt((x18 - x46)^2 + (x158 - x186)^2 + (x298 - x326)^2) + 1 / sqrt((x18
    - x47)^2 + (x158 - x187)^2 + (x298 - x327)^2) + 1 / sqrt((x18 - x48)^2 + (
    x158 - x188)^2 + (x298 - x328)^2) + 1 / sqrt((x18 - x49)^2 + (x158 - x189)^
    2 + (x298 - x329)^2) + 1 / sqrt((x18 - x50)^2 + (x158 - x190)^2 + (x298 -
    x330)^2) + 1 / sqrt((x18 - x51)^2 + (x158 - x191)^2 + (x298 - x331)^2) + 1
    / sqrt((x18 - x52)^2 + (x158 - x192)^2 + (x298 - x332)^2) + 1 / sqrt((x18
    - x53)^2 + (x158 - x193)^2 + (x298 - x333)^2) + 1 / sqrt((x18 - x54)^2 + (
    x158 - x194)^2 + (x298 - x334)^2) + 1 / sqrt((x18 - x55)^2 + (x158 - x195)^
    2 + (x298 - x335)^2) + 1 / sqrt((x18 - x56)^2 + (x158 - x196)^2 + (x298 -
    x336)^2) + 1 / sqrt((x18 - x57)^2 + (x158 - x197)^2 + (x298 - x337)^2) + 1
    / sqrt((x18 - x58)^2 + (x158 - x198)^2 + (x298 - x338)^2) + 1 / sqrt((x18
    - x59)^2 + (x158 - x199)^2 + (x298 - x339)^2) + 1 / sqrt((x18 - x60)^2 + (
    x158 - x200)^2 + (x298 - x340)^2) + 1 / sqrt((x18 - x61)^2 + (x158 - x201)^
    2 + (x298 - x341)^2) + 1 / sqrt((x18 - x62)^2 + (x158 - x202)^2 + (x298 -
    x342)^2) + 1 / sqrt((x18 - x63)^2 + (x158 - x203)^2 + (x298 - x343)^2) + 1
    / sqrt((x18 - x64)^2 + (x158 - x204)^2 + (x298 - x344)^2) + 1 / sqrt((x18
    - x65)^2 + (x158 - x205)^2 + (x298 - x345)^2) + 1 / sqrt((x18 - x66)^2 + (
    x158 - x206)^2 + (x298 - x346)^2) + 1 / sqrt((x18 - x67)^2 + (x158 - x207)^
    2 + (x298 - x347)^2) + 1 / sqrt((x18 - x68)^2 + (x158 - x208)^2 + (x298 -
    x348)^2) + 1 / sqrt((x18 - x69)^2 + (x158 - x209)^2 + (x298 - x349)^2) + 1
    / sqrt((x18 - x70)^2 + (x158 - x210)^2 + (x298 - x350)^2) + 1 / sqrt((x18
    - x71)^2 + (x158 - x211)^2 + (x298 - x351)^2) + 1 / sqrt((x18 - x72)^2 + (
    x158 - x212)^2 + (x298 - x352)^2) + 1 / sqrt((x18 - x73)^2 + (x158 - x213)^
    2 + (x298 - x353)^2) + 1 / sqrt((x18 - x74)^2 + (x158 - x214)^2 + (x298 -
    x354)^2) + 1 / sqrt((x18 - x75)^2 + (x158 - x215)^2 + (x298 - x355)^2) + 1
    / sqrt((x18 - x76)^2 + (x158 - x216)^2 + (x298 - x356)^2) + 1 / sqrt((x18
    - x77)^2 + (x158 - x217)^2 + (x298 - x357)^2) + 1 / sqrt((x18 - x78)^2 + (
    x158 - x218)^2 + (x298 - x358)^2) + 1 / sqrt((x18 - x79)^2 + (x158 - x219)^
    2 + (x298 - x359)^2) + 1 / sqrt((x18 - x80)^2 + (x158 - x220)^2 + (x298 -
    x360)^2) + 1 / sqrt((x18 - x81)^2 + (x158 - x221)^2 + (x298 - x361)^2) + 1
    / sqrt((x18 - x82)^2 + (x158 - x222)^2 + (x298 - x362)^2) + 1 / sqrt((x18
    - x83)^2 + (x158 - x223)^2 + (x298 - x363)^2) + 1 / sqrt((x18 - x84)^2 + (
    x158 - x224)^2 + (x298 - x364)^2) + 1 / sqrt((x18 - x85)^2 + (x158 - x225)^
    2 + (x298 - x365)^2) + 1 / sqrt((x18 - x86)^2 + (x158 - x226)^2 + (x298 -
    x366)^2) + 1 / sqrt((x18 - x87)^2 + (x158 - x227)^2 + (x298 - x367)^2) + 1
    / sqrt((x18 - x88)^2 + (x158 - x228)^2 + (x298 - x368)^2) + 1 / sqrt((x18
    - x89)^2 + (x158 - x229)^2 + (x298 - x369)^2) + 1 / sqrt((x18 - x90)^2 + (
    x158 - x230)^2 + (x298 - x370)^2) + 1 / sqrt((x18 - x91)^2 + (x158 - x231)^
    2 + (x298 - x371)^2) + 1 / sqrt((x18 - x92)^2 + (x158 - x232)^2 + (x298 -
    x372)^2) + 1 / sqrt((x18 - x93)^2 + (x158 - x233)^2 + (x298 - x373)^2) + 1
    / sqrt((x18 - x94)^2 + (x158 - x234)^2 + (x298 - x374)^2) + 1 / sqrt((x18
    - x95)^2 + (x158 - x235)^2 + (x298 - x375)^2) + 1 / sqrt((x18 - x96)^2 + (
    x158 - x236)^2 + (x298 - x376)^2) + 1 / sqrt((x18 - x97)^2 + (x158 - x237)^
    2 + (x298 - x377)^2) + 1 / sqrt((x18 - x98)^2 + (x158 - x238)^2 + (x298 -
    x378)^2) + 1 / sqrt((x18 - x99)^2 + (x158 - x239)^2 + (x298 - x379)^2) + 1
    / sqrt((x18 - x100)^2 + (x158 - x240)^2 + (x298 - x380)^2) + 1 / sqrt((x18
    - x101)^2 + (x158 - x241)^2 + (x298 - x381)^2) + 1 / sqrt((x18 - x102)^2
    + (x158 - x242)^2 + (x298 - x382)^2) + 1 / sqrt((x18 - x103)^2 + (x158 -
    x243)^2 + (x298 - x383)^2) + 1 / sqrt((x18 - x104)^2 + (x158 - x244)^2 + (
    x298 - x384)^2) + 1 / sqrt((x18 - x105)^2 + (x158 - x245)^2 + (x298 - x385)
    ^2) + 1 / sqrt((x18 - x106)^2 + (x158 - x246)^2 + (x298 - x386)^2) + 1 /
    sqrt((x18 - x107)^2 + (x158 - x247)^2 + (x298 - x387)^2) + 1 / sqrt((x18 -
    x108)^2 + (x158 - x248)^2 + (x298 - x388)^2) + 1 / sqrt((x18 - x109)^2 + (
    x158 - x249)^2 + (x298 - x389)^2) + 1 / sqrt((x18 - x110)^2 + (x158 - x250)
    ^2 + (x298 - x390)^2) + 1 / sqrt((x18 - x111)^2 + (x158 - x251)^2 + (x298
    - x391)^2) + 1 / sqrt((x18 - x112)^2 + (x158 - x252)^2 + (x298 - x392)^2)
    + 1 / sqrt((x18 - x113)^2 + (x158 - x253)^2 + (x298 - x393)^2) + 1 / sqrt(
    (x18 - x114)^2 + (x158 - x254)^2 + (x298 - x394)^2) + 1 / sqrt((x18 - x115)
    ^2 + (x158 - x255)^2 + (x298 - x395)^2) + 1 / sqrt((x18 - x116)^2 + (x158
    - x256)^2 + (x298 - x396)^2) + 1 / sqrt((x18 - x117)^2 + (x158 - x257)^2
    + (x298 - x397)^2) + 1 / sqrt((x18 - x118)^2 + (x158 - x258)^2 + (x298 -
    x398)^2) + 1 / sqrt((x18 - x119)^2 + (x158 - x259)^2 + (x298 - x399)^2) + 1
    / sqrt((x18 - x120)^2 + (x158 - x260)^2 + (x298 - x400)^2) + 1 / sqrt((x18
    - x121)^2 + (x158 - x261)^2 + (x298 - x401)^2) + 1 / sqrt((x18 - x122)^2
    + (x158 - x262)^2 + (x298 - x402)^2) + 1 / sqrt((x18 - x123)^2 + (x158 -
    x263)^2 + (x298 - x403)^2) + 1 / sqrt((x18 - x124)^2 + (x158 - x264)^2 + (
    x298 - x404)^2) + 1 / sqrt((x18 - x125)^2 + (x158 - x265)^2 + (x298 - x405)
    ^2) + 1 / sqrt((x18 - x126)^2 + (x158 - x266)^2 + (x298 - x406)^2) + 1 /
    sqrt((x18 - x127)^2 + (x158 - x267)^2 + (x298 - x407)^2) + 1 / sqrt((x18 -
    x128)^2 + (x158 - x268)^2 + (x298 - x408)^2) + 1 / sqrt((x18 - x129)^2 + (
    x158 - x269)^2 + (x298 - x409)^2) + 1 / sqrt((x18 - x130)^2 + (x158 - x270)
    ^2 + (x298 - x410)^2) + 1 / sqrt((x18 - x131)^2 + (x158 - x271)^2 + (x298
    - x411)^2) + 1 / sqrt((x18 - x132)^2 + (x158 - x272)^2 + (x298 - x412)^2)
    + 1 / sqrt((x18 - x133)^2 + (x158 - x273)^2 + (x298 - x413)^2) + 1 / sqrt(
    (x18 - x134)^2 + (x158 - x274)^2 + (x298 - x414)^2) + 1 / sqrt((x18 - x135)
    ^2 + (x158 - x275)^2 + (x298 - x415)^2) + 1 / sqrt((x18 - x136)^2 + (x158
    - x276)^2 + (x298 - x416)^2) + 1 / sqrt((x18 - x137)^2 + (x158 - x277)^2
    + (x298 - x417)^2) + 1 / sqrt((x18 - x138)^2 + (x158 - x278)^2 + (x298 -
    x418)^2) + 1 / sqrt((x18 - x139)^2 + (x158 - x279)^2 + (x298 - x419)^2) + 1
    / sqrt((x18 - x140)^2 + (x158 - x280)^2 + (x298 - x420)^2) + 1 / sqrt((x19
    - x20)^2 + (x159 - x160)^2 + (x299 - x300)^2) + 1 / sqrt((x19 - x21)^2 + (
    x159 - x161)^2 + (x299 - x301)^2) + 1 / sqrt((x19 - x22)^2 + (x159 - x162)^
    2 + (x299 - x302)^2) + 1 / sqrt((x19 - x23)^2 + (x159 - x163)^2 + (x299 -
    x303)^2) + 1 / sqrt((x19 - x24)^2 + (x159 - x164)^2 + (x299 - x304)^2) + 1
    / sqrt((x19 - x25)^2 + (x159 - x165)^2 + (x299 - x305)^2) + 1 / sqrt((x19
    - x26)^2 + (x159 - x166)^2 + (x299 - x306)^2) + 1 / sqrt((x19 - x27)^2 + (
    x159 - x167)^2 + (x299 - x307)^2) + 1 / sqrt((x19 - x28)^2 + (x159 - x168)^
    2 + (x299 - x308)^2) + 1 / sqrt((x19 - x29)^2 + (x159 - x169)^2 + (x299 -
    x309)^2) + 1 / sqrt((x19 - x30)^2 + (x159 - x170)^2 + (x299 - x310)^2) + 1
    / sqrt((x19 - x31)^2 + (x159 - x171)^2 + (x299 - x311)^2) + 1 / sqrt((x19
    - x32)^2 + (x159 - x172)^2 + (x299 - x312)^2) + 1 / sqrt((x19 - x33)^2 + (
    x159 - x173)^2 + (x299 - x313)^2) + 1 / sqrt((x19 - x34)^2 + (x159 - x174)^
    2 + (x299 - x314)^2) + 1 / sqrt((x19 - x35)^2 + (x159 - x175)^2 + (x299 -
    x315)^2) + 1 / sqrt((x19 - x36)^2 + (x159 - x176)^2 + (x299 - x316)^2) + 1
    / sqrt((x19 - x37)^2 + (x159 - x177)^2 + (x299 - x317)^2) + 1 / sqrt((x19
    - x38)^2 + (x159 - x178)^2 + (x299 - x318)^2) + 1 / sqrt((x19 - x39)^2 + (
    x159 - x179)^2 + (x299 - x319)^2) + 1 / sqrt((x19 - x40)^2 + (x159 - x180)^
    2 + (x299 - x320)^2) + 1 / sqrt((x19 - x41)^2 + (x159 - x181)^2 + (x299 -
    x321)^2) + 1 / sqrt((x19 - x42)^2 + (x159 - x182)^2 + (x299 - x322)^2) + 1
    / sqrt((x19 - x43)^2 + (x159 - x183)^2 + (x299 - x323)^2) + 1 / sqrt((x19
    - x44)^2 + (x159 - x184)^2 + (x299 - x324)^2) + 1 / sqrt((x19 - x45)^2 + (
    x159 - x185)^2 + (x299 - x325)^2) + 1 / sqrt((x19 - x46)^2 + (x159 - x186)^
    2 + (x299 - x326)^2) + 1 / sqrt((x19 - x47)^2 + (x159 - x187)^2 + (x299 -
    x327)^2) + 1 / sqrt((x19 - x48)^2 + (x159 - x188)^2 + (x299 - x328)^2) + 1
    / sqrt((x19 - x49)^2 + (x159 - x189)^2 + (x299 - x329)^2) + 1 / sqrt((x19
    - x50)^2 + (x159 - x190)^2 + (x299 - x330)^2) + 1 / sqrt((x19 - x51)^2 + (
    x159 - x191)^2 + (x299 - x331)^2) + 1 / sqrt((x19 - x52)^2 + (x159 - x192)^
    2 + (x299 - x332)^2) + 1 / sqrt((x19 - x53)^2 + (x159 - x193)^2 + (x299 -
    x333)^2) + 1 / sqrt((x19 - x54)^2 + (x159 - x194)^2 + (x299 - x334)^2) + 1
    / sqrt((x19 - x55)^2 + (x159 - x195)^2 + (x299 - x335)^2) + 1 / sqrt((x19
    - x56)^2 + (x159 - x196)^2 + (x299 - x336)^2) + 1 / sqrt((x19 - x57)^2 + (
    x159 - x197)^2 + (x299 - x337)^2) + 1 / sqrt((x19 - x58)^2 + (x159 - x198)^
    2 + (x299 - x338)^2) + 1 / sqrt((x19 - x59)^2 + (x159 - x199)^2 + (x299 -
    x339)^2) + 1 / sqrt((x19 - x60)^2 + (x159 - x200)^2 + (x299 - x340)^2) + 1
    / sqrt((x19 - x61)^2 + (x159 - x201)^2 + (x299 - x341)^2) + 1 / sqrt((x19
    - x62)^2 + (x159 - x202)^2 + (x299 - x342)^2) + 1 / sqrt((x19 - x63)^2 + (
    x159 - x203)^2 + (x299 - x343)^2) + 1 / sqrt((x19 - x64)^2 + (x159 - x204)^
    2 + (x299 - x344)^2) + 1 / sqrt((x19 - x65)^2 + (x159 - x205)^2 + (x299 -
    x345)^2) + 1 / sqrt((x19 - x66)^2 + (x159 - x206)^2 + (x299 - x346)^2) + 1
    / sqrt((x19 - x67)^2 + (x159 - x207)^2 + (x299 - x347)^2) + 1 / sqrt((x19
    - x68)^2 + (x159 - x208)^2 + (x299 - x348)^2) + 1 / sqrt((x19 - x69)^2 + (
    x159 - x209)^2 + (x299 - x349)^2) + 1 / sqrt((x19 - x70)^2 + (x159 - x210)^
    2 + (x299 - x350)^2) + 1 / sqrt((x19 - x71)^2 + (x159 - x211)^2 + (x299 -
    x351)^2) + 1 / sqrt((x19 - x72)^2 + (x159 - x212)^2 + (x299 - x352)^2) + 1
    / sqrt((x19 - x73)^2 + (x159 - x213)^2 + (x299 - x353)^2) + 1 / sqrt((x19
    - x74)^2 + (x159 - x214)^2 + (x299 - x354)^2) + 1 / sqrt((x19 - x75)^2 + (
    x159 - x215)^2 + (x299 - x355)^2) + 1 / sqrt((x19 - x76)^2 + (x159 - x216)^
    2 + (x299 - x356)^2) + 1 / sqrt((x19 - x77)^2 + (x159 - x217)^2 + (x299 -
    x357)^2) + 1 / sqrt((x19 - x78)^2 + (x159 - x218)^2 + (x299 - x358)^2) + 1
    / sqrt((x19 - x79)^2 + (x159 - x219)^2 + (x299 - x359)^2) + 1 / sqrt((x19
    - x80)^2 + (x159 - x220)^2 + (x299 - x360)^2) + 1 / sqrt((x19 - x81)^2 + (
    x159 - x221)^2 + (x299 - x361)^2) + 1 / sqrt((x19 - x82)^2 + (x159 - x222)^
    2 + (x299 - x362)^2) + 1 / sqrt((x19 - x83)^2 + (x159 - x223)^2 + (x299 -
    x363)^2) + 1 / sqrt((x19 - x84)^2 + (x159 - x224)^2 + (x299 - x364)^2) + 1
    / sqrt((x19 - x85)^2 + (x159 - x225)^2 + (x299 - x365)^2) + 1 / sqrt((x19
    - x86)^2 + (x159 - x226)^2 + (x299 - x366)^2) + 1 / sqrt((x19 - x87)^2 + (
    x159 - x227)^2 + (x299 - x367)^2) + 1 / sqrt((x19 - x88)^2 + (x159 - x228)^
    2 + (x299 - x368)^2) + 1 / sqrt((x19 - x89)^2 + (x159 - x229)^2 + (x299 -
    x369)^2) + 1 / sqrt((x19 - x90)^2 + (x159 - x230)^2 + (x299 - x370)^2) + 1
    / sqrt((x19 - x91)^2 + (x159 - x231)^2 + (x299 - x371)^2) + 1 / sqrt((x19
    - x92)^2 + (x159 - x232)^2 + (x299 - x372)^2) + 1 / sqrt((x19 - x93)^2 + (
    x159 - x233)^2 + (x299 - x373)^2) + 1 / sqrt((x19 - x94)^2 + (x159 - x234)^
    2 + (x299 - x374)^2) + 1 / sqrt((x19 - x95)^2 + (x159 - x235)^2 + (x299 -
    x375)^2) + 1 / sqrt((x19 - x96)^2 + (x159 - x236)^2 + (x299 - x376)^2) + 1
    / sqrt((x19 - x97)^2 + (x159 - x237)^2 + (x299 - x377)^2) + 1 / sqrt((x19
    - x98)^2 + (x159 - x238)^2 + (x299 - x378)^2) + 1 / sqrt((x19 - x99)^2 + (
    x159 - x239)^2 + (x299 - x379)^2) + 1 / sqrt((x19 - x100)^2 + (x159 - x240)
    ^2 + (x299 - x380)^2) + 1 / sqrt((x19 - x101)^2 + (x159 - x241)^2 + (x299
    - x381)^2) + 1 / sqrt((x19 - x102)^2 + (x159 - x242)^2 + (x299 - x382)^2)
    + 1 / sqrt((x19 - x103)^2 + (x159 - x243)^2 + (x299 - x383)^2) + 1 / sqrt(
    (x19 - x104)^2 + (x159 - x244)^2 + (x299 - x384)^2) + 1 / sqrt((x19 - x105)
    ^2 + (x159 - x245)^2 + (x299 - x385)^2) + 1 / sqrt((x19 - x106)^2 + (x159
    - x246)^2 + (x299 - x386)^2) + 1 / sqrt((x19 - x107)^2 + (x159 - x247)^2
    + (x299 - x387)^2) + 1 / sqrt((x19 - x108)^2 + (x159 - x248)^2 + (x299 -
    x388)^2) + 1 / sqrt((x19 - x109)^2 + (x159 - x249)^2 + (x299 - x389)^2) + 1
    / sqrt((x19 - x110)^2 + (x159 - x250)^2 + (x299 - x390)^2) + 1 / sqrt((x19
    - x111)^2 + (x159 - x251)^2 + (x299 - x391)^2) + 1 / sqrt((x19 - x112)^2
    + (x159 - x252)^2 + (x299 - x392)^2) + 1 / sqrt((x19 - x113)^2 + (x159 -
    x253)^2 + (x299 - x393)^2) + 1 / sqrt((x19 - x114)^2 + (x159 - x254)^2 + (
    x299 - x394)^2) + 1 / sqrt((x19 - x115)^2 + (x159 - x255)^2 + (x299 - x395)
    ^2) + 1 / sqrt((x19 - x116)^2 + (x159 - x256)^2 + (x299 - x396)^2) + 1 /
    sqrt((x19 - x117)^2 + (x159 - x257)^2 + (x299 - x397)^2) + 1 / sqrt((x19 -
    x118)^2 + (x159 - x258)^2 + (x299 - x398)^2) + 1 / sqrt((x19 - x119)^2 + (
    x159 - x259)^2 + (x299 - x399)^2) + 1 / sqrt((x19 - x120)^2 + (x159 - x260)
    ^2 + (x299 - x400)^2) + 1 / sqrt((x19 - x121)^2 + (x159 - x261)^2 + (x299
    - x401)^2) + 1 / sqrt((x19 - x122)^2 + (x159 - x262)^2 + (x299 - x402)^2)
    + 1 / sqrt((x19 - x123)^2 + (x159 - x263)^2 + (x299 - x403)^2) + 1 / sqrt(
    (x19 - x124)^2 + (x159 - x264)^2 + (x299 - x404)^2) + 1 / sqrt((x19 - x125)
    ^2 + (x159 - x265)^2 + (x299 - x405)^2) + 1 / sqrt((x19 - x126)^2 + (x159
    - x266)^2 + (x299 - x406)^2) + 1 / sqrt((x19 - x127)^2 + (x159 - x267)^2
    + (x299 - x407)^2) + 1 / sqrt((x19 - x128)^2 + (x159 - x268)^2 + (x299 -
    x408)^2) + 1 / sqrt((x19 - x129)^2 + (x159 - x269)^2 + (x299 - x409)^2) + 1
    / sqrt((x19 - x130)^2 + (x159 - x270)^2 + (x299 - x410)^2) + 1 / sqrt((x19
    - x131)^2 + (x159 - x271)^2 + (x299 - x411)^2) + 1 / sqrt((x19 - x132)^2
    + (x159 - x272)^2 + (x299 - x412)^2) + 1 / sqrt((x19 - x133)^2 + (x159 -
    x273)^2 + (x299 - x413)^2) + 1 / sqrt((x19 - x134)^2 + (x159 - x274)^2 + (
    x299 - x414)^2) + 1 / sqrt((x19 - x135)^2 + (x159 - x275)^2 + (x299 - x415)
    ^2) + 1 / sqrt((x19 - x136)^2 + (x159 - x276)^2 + (x299 - x416)^2) + 1 /
    sqrt((x19 - x137)^2 + (x159 - x277)^2 + (x299 - x417)^2) + 1 / sqrt((x19 -
    x138)^2 + (x159 - x278)^2 + (x299 - x418)^2) + 1 / sqrt((x19 - x139)^2 + (
    x159 - x279)^2 + (x299 - x419)^2) + 1 / sqrt((x19 - x140)^2 + (x159 - x280)
    ^2 + (x299 - x420)^2) + 1 / sqrt((x20 - x21)^2 + (x160 - x161)^2 + (x300 -
    x301)^2) + 1 / sqrt((x20 - x22)^2 + (x160 - x162)^2 + (x300 - x302)^2) + 1
    / sqrt((x20 - x23)^2 + (x160 - x163)^2 + (x300 - x303)^2) + 1 / sqrt((x20
    - x24)^2 + (x160 - x164)^2 + (x300 - x304)^2) + 1 / sqrt((x20 - x25)^2 + (
    x160 - x165)^2 + (x300 - x305)^2) + 1 / sqrt((x20 - x26)^2 + (x160 - x166)^
    2 + (x300 - x306)^2) + 1 / sqrt((x20 - x27)^2 + (x160 - x167)^2 + (x300 -
    x307)^2) + 1 / sqrt((x20 - x28)^2 + (x160 - x168)^2 + (x300 - x308)^2) + 1
    / sqrt((x20 - x29)^2 + (x160 - x169)^2 + (x300 - x309)^2) + 1 / sqrt((x20
    - x30)^2 + (x160 - x170)^2 + (x300 - x310)^2) + 1 / sqrt((x20 - x31)^2 + (
    x160 - x171)^2 + (x300 - x311)^2) + 1 / sqrt((x20 - x32)^2 + (x160 - x172)^
    2 + (x300 - x312)^2) + 1 / sqrt((x20 - x33)^2 + (x160 - x173)^2 + (x300 -
    x313)^2) + 1 / sqrt((x20 - x34)^2 + (x160 - x174)^2 + (x300 - x314)^2) + 1
    / sqrt((x20 - x35)^2 + (x160 - x175)^2 + (x300 - x315)^2) + 1 / sqrt((x20
    - x36)^2 + (x160 - x176)^2 + (x300 - x316)^2) + 1 / sqrt((x20 - x37)^2 + (
    x160 - x177)^2 + (x300 - x317)^2) + 1 / sqrt((x20 - x38)^2 + (x160 - x178)^
    2 + (x300 - x318)^2) + 1 / sqrt((x20 - x39)^2 + (x160 - x179)^2 + (x300 -
    x319)^2) + 1 / sqrt((x20 - x40)^2 + (x160 - x180)^2 + (x300 - x320)^2) + 1
    / sqrt((x20 - x41)^2 + (x160 - x181)^2 + (x300 - x321)^2) + 1 / sqrt((x20
    - x42)^2 + (x160 - x182)^2 + (x300 - x322)^2) + 1 / sqrt((x20 - x43)^2 + (
    x160 - x183)^2 + (x300 - x323)^2) + 1 / sqrt((x20 - x44)^2 + (x160 - x184)^
    2 + (x300 - x324)^2) + 1 / sqrt((x20 - x45)^2 + (x160 - x185)^2 + (x300 -
    x325)^2) + 1 / sqrt((x20 - x46)^2 + (x160 - x186)^2 + (x300 - x326)^2) + 1
    / sqrt((x20 - x47)^2 + (x160 - x187)^2 + (x300 - x327)^2) + 1 / sqrt((x20
    - x48)^2 + (x160 - x188)^2 + (x300 - x328)^2) + 1 / sqrt((x20 - x49)^2 + (
    x160 - x189)^2 + (x300 - x329)^2) + 1 / sqrt((x20 - x50)^2 + (x160 - x190)^
    2 + (x300 - x330)^2) + 1 / sqrt((x20 - x51)^2 + (x160 - x191)^2 + (x300 -
    x331)^2) + 1 / sqrt((x20 - x52)^2 + (x160 - x192)^2 + (x300 - x332)^2) + 1
    / sqrt((x20 - x53)^2 + (x160 - x193)^2 + (x300 - x333)^2) + 1 / sqrt((x20
    - x54)^2 + (x160 - x194)^2 + (x300 - x334)^2) + 1 / sqrt((x20 - x55)^2 + (
    x160 - x195)^2 + (x300 - x335)^2) + 1 / sqrt((x20 - x56)^2 + (x160 - x196)^
    2 + (x300 - x336)^2) + 1 / sqrt((x20 - x57)^2 + (x160 - x197)^2 + (x300 -
    x337)^2) + 1 / sqrt((x20 - x58)^2 + (x160 - x198)^2 + (x300 - x338)^2) + 1
    / sqrt((x20 - x59)^2 + (x160 - x199)^2 + (x300 - x339)^2) + 1 / sqrt((x20
    - x60)^2 + (x160 - x200)^2 + (x300 - x340)^2) + 1 / sqrt((x20 - x61)^2 + (
    x160 - x201)^2 + (x300 - x341)^2) + 1 / sqrt((x20 - x62)^2 + (x160 - x202)^
    2 + (x300 - x342)^2) + 1 / sqrt((x20 - x63)^2 + (x160 - x203)^2 + (x300 -
    x343)^2) + 1 / sqrt((x20 - x64)^2 + (x160 - x204)^2 + (x300 - x344)^2) + 1
    / sqrt((x20 - x65)^2 + (x160 - x205)^2 + (x300 - x345)^2) + 1 / sqrt((x20
    - x66)^2 + (x160 - x206)^2 + (x300 - x346)^2) + 1 / sqrt((x20 - x67)^2 + (
    x160 - x207)^2 + (x300 - x347)^2) + 1 / sqrt((x20 - x68)^2 + (x160 - x208)^
    2 + (x300 - x348)^2) + 1 / sqrt((x20 - x69)^2 + (x160 - x209)^2 + (x300 -
    x349)^2) + 1 / sqrt((x20 - x70)^2 + (x160 - x210)^2 + (x300 - x350)^2) + 1
    / sqrt((x20 - x71)^2 + (x160 - x211)^2 + (x300 - x351)^2) + 1 / sqrt((x20
    - x72)^2 + (x160 - x212)^2 + (x300 - x352)^2) + 1 / sqrt((x20 - x73)^2 + (
    x160 - x213)^2 + (x300 - x353)^2) + 1 / sqrt((x20 - x74)^2 + (x160 - x214)^
    2 + (x300 - x354)^2) + 1 / sqrt((x20 - x75)^2 + (x160 - x215)^2 + (x300 -
    x355)^2) + 1 / sqrt((x20 - x76)^2 + (x160 - x216)^2 + (x300 - x356)^2) + 1
    / sqrt((x20 - x77)^2 + (x160 - x217)^2 + (x300 - x357)^2) + 1 / sqrt((x20
    - x78)^2 + (x160 - x218)^2 + (x300 - x358)^2) + 1 / sqrt((x20 - x79)^2 + (
    x160 - x219)^2 + (x300 - x359)^2) + 1 / sqrt((x20 - x80)^2 + (x160 - x220)^
    2 + (x300 - x360)^2) + 1 / sqrt((x20 - x81)^2 + (x160 - x221)^2 + (x300 -
    x361)^2) + 1 / sqrt((x20 - x82)^2 + (x160 - x222)^2 + (x300 - x362)^2) + 1
    / sqrt((x20 - x83)^2 + (x160 - x223)^2 + (x300 - x363)^2) + 1 / sqrt((x20
    - x84)^2 + (x160 - x224)^2 + (x300 - x364)^2) + 1 / sqrt((x20 - x85)^2 + (
    x160 - x225)^2 + (x300 - x365)^2) + 1 / sqrt((x20 - x86)^2 + (x160 - x226)^
    2 + (x300 - x366)^2) + 1 / sqrt((x20 - x87)^2 + (x160 - x227)^2 + (x300 -
    x367)^2) + 1 / sqrt((x20 - x88)^2 + (x160 - x228)^2 + (x300 - x368)^2) + 1
    / sqrt((x20 - x89)^2 + (x160 - x229)^2 + (x300 - x369)^2) + 1 / sqrt((x20
    - x90)^2 + (x160 - x230)^2 + (x300 - x370)^2) + 1 / sqrt((x20 - x91)^2 + (
    x160 - x231)^2 + (x300 - x371)^2) + 1 / sqrt((x20 - x92)^2 + (x160 - x232)^
    2 + (x300 - x372)^2) + 1 / sqrt((x20 - x93)^2 + (x160 - x233)^2 + (x300 -
    x373)^2) + 1 / sqrt((x20 - x94)^2 + (x160 - x234)^2 + (x300 - x374)^2) + 1
    / sqrt((x20 - x95)^2 + (x160 - x235)^2 + (x300 - x375)^2) + 1 / sqrt((x20
    - x96)^2 + (x160 - x236)^2 + (x300 - x376)^2) + 1 / sqrt((x20 - x97)^2 + (
    x160 - x237)^2 + (x300 - x377)^2) + 1 / sqrt((x20 - x98)^2 + (x160 - x238)^
    2 + (x300 - x378)^2) + 1 / sqrt((x20 - x99)^2 + (x160 - x239)^2 + (x300 -
    x379)^2) + 1 / sqrt((x20 - x100)^2 + (x160 - x240)^2 + (x300 - x380)^2) + 1
    / sqrt((x20 - x101)^2 + (x160 - x241)^2 + (x300 - x381)^2) + 1 / sqrt((x20
    - x102)^2 + (x160 - x242)^2 + (x300 - x382)^2) + 1 / sqrt((x20 - x103)^2
    + (x160 - x243)^2 + (x300 - x383)^2) + 1 / sqrt((x20 - x104)^2 + (x160 -
    x244)^2 + (x300 - x384)^2) + 1 / sqrt((x20 - x105)^2 + (x160 - x245)^2 + (
    x300 - x385)^2) + 1 / sqrt((x20 - x106)^2 + (x160 - x246)^2 + (x300 - x386)
    ^2) + 1 / sqrt((x20 - x107)^2 + (x160 - x247)^2 + (x300 - x387)^2) + 1 /
    sqrt((x20 - x108)^2 + (x160 - x248)^2 + (x300 - x388)^2) + 1 / sqrt((x20 -
    x109)^2 + (x160 - x249)^2 + (x300 - x389)^2) + 1 / sqrt((x20 - x110)^2 + (
    x160 - x250)^2 + (x300 - x390)^2) + 1 / sqrt((x20 - x111)^2 + (x160 - x251)
    ^2 + (x300 - x391)^2) + 1 / sqrt((x20 - x112)^2 + (x160 - x252)^2 + (x300
    - x392)^2) + 1 / sqrt((x20 - x113)^2 + (x160 - x253)^2 + (x300 - x393)^2)
    + 1 / sqrt((x20 - x114)^2 + (x160 - x254)^2 + (x300 - x394)^2) + 1 / sqrt(
    (x20 - x115)^2 + (x160 - x255)^2 + (x300 - x395)^2) + 1 / sqrt((x20 - x116)
    ^2 + (x160 - x256)^2 + (x300 - x396)^2) + 1 / sqrt((x20 - x117)^2 + (x160
    - x257)^2 + (x300 - x397)^2) + 1 / sqrt((x20 - x118)^2 + (x160 - x258)^2
    + (x300 - x398)^2) + 1 / sqrt((x20 - x119)^2 + (x160 - x259)^2 + (x300 -
    x399)^2) + 1 / sqrt((x20 - x120)^2 + (x160 - x260)^2 + (x300 - x400)^2) + 1
    / sqrt((x20 - x121)^2 + (x160 - x261)^2 + (x300 - x401)^2) + 1 / sqrt((x20
    - x122)^2 + (x160 - x262)^2 + (x300 - x402)^2) + 1 / sqrt((x20 - x123)^2
    + (x160 - x263)^2 + (x300 - x403)^2) + 1 / sqrt((x20 - x124)^2 + (x160 -
    x264)^2 + (x300 - x404)^2) + 1 / sqrt((x20 - x125)^2 + (x160 - x265)^2 + (
    x300 - x405)^2) + 1 / sqrt((x20 - x126)^2 + (x160 - x266)^2 + (x300 - x406)
    ^2) + 1 / sqrt((x20 - x127)^2 + (x160 - x267)^2 + (x300 - x407)^2) + 1 /
    sqrt((x20 - x128)^2 + (x160 - x268)^2 + (x300 - x408)^2) + 1 / sqrt((x20 -
    x129)^2 + (x160 - x269)^2 + (x300 - x409)^2) + 1 / sqrt((x20 - x130)^2 + (
    x160 - x270)^2 + (x300 - x410)^2) + 1 / sqrt((x20 - x131)^2 + (x160 - x271)
    ^2 + (x300 - x411)^2) + 1 / sqrt((x20 - x132)^2 + (x160 - x272)^2 + (x300
    - x412)^2) + 1 / sqrt((x20 - x133)^2 + (x160 - x273)^2 + (x300 - x413)^2)
    + 1 / sqrt((x20 - x134)^2 + (x160 - x274)^2 + (x300 - x414)^2) + 1 / sqrt(
    (x20 - x135)^2 + (x160 - x275)^2 + (x300 - x415)^2) + 1 / sqrt((x20 - x136)
    ^2 + (x160 - x276)^2 + (x300 - x416)^2) + 1 / sqrt((x20 - x137)^2 + (x160
    - x277)^2 + (x300 - x417)^2) + 1 / sqrt((x20 - x138)^2 + (x160 - x278)^2
    + (x300 - x418)^2) + 1 / sqrt((x20 - x139)^2 + (x160 - x279)^2 + (x300 -
    x419)^2) + 1 / sqrt((x20 - x140)^2 + (x160 - x280)^2 + (x300 - x420)^2) + 1
    / sqrt((x21 - x22)^2 + (x161 - x162)^2 + (x301 - x302)^2) + 1 / sqrt((x21
    - x23)^2 + (x161 - x163)^2 + (x301 - x303)^2) + 1 / sqrt((x21 - x24)^2 + (
    x161 - x164)^2 + (x301 - x304)^2) + 1 / sqrt((x21 - x25)^2 + (x161 - x165)^
    2 + (x301 - x305)^2) + 1 / sqrt((x21 - x26)^2 + (x161 - x166)^2 + (x301 -
    x306)^2) + 1 / sqrt((x21 - x27)^2 + (x161 - x167)^2 + (x301 - x307)^2) + 1
    / sqrt((x21 - x28)^2 + (x161 - x168)^2 + (x301 - x308)^2) + 1 / sqrt((x21
    - x29)^2 + (x161 - x169)^2 + (x301 - x309)^2) + 1 / sqrt((x21 - x30)^2 + (
    x161 - x170)^2 + (x301 - x310)^2) + 1 / sqrt((x21 - x31)^2 + (x161 - x171)^
    2 + (x301 - x311)^2) + 1 / sqrt((x21 - x32)^2 + (x161 - x172)^2 + (x301 -
    x312)^2) + 1 / sqrt((x21 - x33)^2 + (x161 - x173)^2 + (x301 - x313)^2) + 1
    / sqrt((x21 - x34)^2 + (x161 - x174)^2 + (x301 - x314)^2) + 1 / sqrt((x21
    - x35)^2 + (x161 - x175)^2 + (x301 - x315)^2) + 1 / sqrt((x21 - x36)^2 + (
    x161 - x176)^2 + (x301 - x316)^2) + 1 / sqrt((x21 - x37)^2 + (x161 - x177)^
    2 + (x301 - x317)^2) + 1 / sqrt((x21 - x38)^2 + (x161 - x178)^2 + (x301 -
    x318)^2) + 1 / sqrt((x21 - x39)^2 + (x161 - x179)^2 + (x301 - x319)^2) + 1
    / sqrt((x21 - x40)^2 + (x161 - x180)^2 + (x301 - x320)^2) + 1 / sqrt((x21
    - x41)^2 + (x161 - x181)^2 + (x301 - x321)^2) + 1 / sqrt((x21 - x42)^2 + (
    x161 - x182)^2 + (x301 - x322)^2) + 1 / sqrt((x21 - x43)^2 + (x161 - x183)^
    2 + (x301 - x323)^2) + 1 / sqrt((x21 - x44)^2 + (x161 - x184)^2 + (x301 -
    x324)^2) + 1 / sqrt((x21 - x45)^2 + (x161 - x185)^2 + (x301 - x325)^2) + 1
    / sqrt((x21 - x46)^2 + (x161 - x186)^2 + (x301 - x326)^2) + 1 / sqrt((x21
    - x47)^2 + (x161 - x187)^2 + (x301 - x327)^2) + 1 / sqrt((x21 - x48)^2 + (
    x161 - x188)^2 + (x301 - x328)^2) + 1 / sqrt((x21 - x49)^2 + (x161 - x189)^
    2 + (x301 - x329)^2) + 1 / sqrt((x21 - x50)^2 + (x161 - x190)^2 + (x301 -
    x330)^2) + 1 / sqrt((x21 - x51)^2 + (x161 - x191)^2 + (x301 - x331)^2) + 1
    / sqrt((x21 - x52)^2 + (x161 - x192)^2 + (x301 - x332)^2) + 1 / sqrt((x21
    - x53)^2 + (x161 - x193)^2 + (x301 - x333)^2) + 1 / sqrt((x21 - x54)^2 + (
    x161 - x194)^2 + (x301 - x334)^2) + 1 / sqrt((x21 - x55)^2 + (x161 - x195)^
    2 + (x301 - x335)^2) + 1 / sqrt((x21 - x56)^2 + (x161 - x196)^2 + (x301 -
    x336)^2) + 1 / sqrt((x21 - x57)^2 + (x161 - x197)^2 + (x301 - x337)^2) + 1
    / sqrt((x21 - x58)^2 + (x161 - x198)^2 + (x301 - x338)^2) + 1 / sqrt((x21
    - x59)^2 + (x161 - x199)^2 + (x301 - x339)^2) + 1 / sqrt((x21 - x60)^2 + (
    x161 - x200)^2 + (x301 - x340)^2) + 1 / sqrt((x21 - x61)^2 + (x161 - x201)^
    2 + (x301 - x341)^2) + 1 / sqrt((x21 - x62)^2 + (x161 - x202)^2 + (x301 -
    x342)^2) + 1 / sqrt((x21 - x63)^2 + (x161 - x203)^2 + (x301 - x343)^2) + 1
    / sqrt((x21 - x64)^2 + (x161 - x204)^2 + (x301 - x344)^2) + 1 / sqrt((x21
    - x65)^2 + (x161 - x205)^2 + (x301 - x345)^2) + 1 / sqrt((x21 - x66)^2 + (
    x161 - x206)^2 + (x301 - x346)^2) + 1 / sqrt((x21 - x67)^2 + (x161 - x207)^
    2 + (x301 - x347)^2) + 1 / sqrt((x21 - x68)^2 + (x161 - x208)^2 + (x301 -
    x348)^2) + 1 / sqrt((x21 - x69)^2 + (x161 - x209)^2 + (x301 - x349)^2) + 1
    / sqrt((x21 - x70)^2 + (x161 - x210)^2 + (x301 - x350)^2) + 1 / sqrt((x21
    - x71)^2 + (x161 - x211)^2 + (x301 - x351)^2) + 1 / sqrt((x21 - x72)^2 + (
    x161 - x212)^2 + (x301 - x352)^2) + 1 / sqrt((x21 - x73)^2 + (x161 - x213)^
    2 + (x301 - x353)^2) + 1 / sqrt((x21 - x74)^2 + (x161 - x214)^2 + (x301 -
    x354)^2) + 1 / sqrt((x21 - x75)^2 + (x161 - x215)^2 + (x301 - x355)^2) + 1
    / sqrt((x21 - x76)^2 + (x161 - x216)^2 + (x301 - x356)^2) + 1 / sqrt((x21
    - x77)^2 + (x161 - x217)^2 + (x301 - x357)^2) + 1 / sqrt((x21 - x78)^2 + (
    x161 - x218)^2 + (x301 - x358)^2) + 1 / sqrt((x21 - x79)^2 + (x161 - x219)^
    2 + (x301 - x359)^2) + 1 / sqrt((x21 - x80)^2 + (x161 - x220)^2 + (x301 -
    x360)^2) + 1 / sqrt((x21 - x81)^2 + (x161 - x221)^2 + (x301 - x361)^2) + 1
    / sqrt((x21 - x82)^2 + (x161 - x222)^2 + (x301 - x362)^2) + 1 / sqrt((x21
    - x83)^2 + (x161 - x223)^2 + (x301 - x363)^2) + 1 / sqrt((x21 - x84)^2 + (
    x161 - x224)^2 + (x301 - x364)^2) + 1 / sqrt((x21 - x85)^2 + (x161 - x225)^
    2 + (x301 - x365)^2) + 1 / sqrt((x21 - x86)^2 + (x161 - x226)^2 + (x301 -
    x366)^2) + 1 / sqrt((x21 - x87)^2 + (x161 - x227)^2 + (x301 - x367)^2) + 1
    / sqrt((x21 - x88)^2 + (x161 - x228)^2 + (x301 - x368)^2) + 1 / sqrt((x21
    - x89)^2 + (x161 - x229)^2 + (x301 - x369)^2) + 1 / sqrt((x21 - x90)^2 + (
    x161 - x230)^2 + (x301 - x370)^2) + 1 / sqrt((x21 - x91)^2 + (x161 - x231)^
    2 + (x301 - x371)^2) + 1 / sqrt((x21 - x92)^2 + (x161 - x232)^2 + (x301 -
    x372)^2) + 1 / sqrt((x21 - x93)^2 + (x161 - x233)^2 + (x301 - x373)^2) + 1
    / sqrt((x21 - x94)^2 + (x161 - x234)^2 + (x301 - x374)^2) + 1 / sqrt((x21
    - x95)^2 + (x161 - x235)^2 + (x301 - x375)^2) + 1 / sqrt((x21 - x96)^2 + (
    x161 - x236)^2 + (x301 - x376)^2) + 1 / sqrt((x21 - x97)^2 + (x161 - x237)^
    2 + (x301 - x377)^2) + 1 / sqrt((x21 - x98)^2 + (x161 - x238)^2 + (x301 -
    x378)^2) + 1 / sqrt((x21 - x99)^2 + (x161 - x239)^2 + (x301 - x379)^2) + 1
    / sqrt((x21 - x100)^2 + (x161 - x240)^2 + (x301 - x380)^2) + 1 / sqrt((x21
    - x101)^2 + (x161 - x241)^2 + (x301 - x381)^2) + 1 / sqrt((x21 - x102)^2
    + (x161 - x242)^2 + (x301 - x382)^2) + 1 / sqrt((x21 - x103)^2 + (x161 -
    x243)^2 + (x301 - x383)^2) + 1 / sqrt((x21 - x104)^2 + (x161 - x244)^2 + (
    x301 - x384)^2) + 1 / sqrt((x21 - x105)^2 + (x161 - x245)^2 + (x301 - x385)
    ^2) + 1 / sqrt((x21 - x106)^2 + (x161 - x246)^2 + (x301 - x386)^2) + 1 /
    sqrt((x21 - x107)^2 + (x161 - x247)^2 + (x301 - x387)^2) + 1 / sqrt((x21 -
    x108)^2 + (x161 - x248)^2 + (x301 - x388)^2) + 1 / sqrt((x21 - x109)^2 + (
    x161 - x249)^2 + (x301 - x389)^2) + 1 / sqrt((x21 - x110)^2 + (x161 - x250)
    ^2 + (x301 - x390)^2) + 1 / sqrt((x21 - x111)^2 + (x161 - x251)^2 + (x301
    - x391)^2) + 1 / sqrt((x21 - x112)^2 + (x161 - x252)^2 + (x301 - x392)^2)
    + 1 / sqrt((x21 - x113)^2 + (x161 - x253)^2 + (x301 - x393)^2) + 1 / sqrt(
    (x21 - x114)^2 + (x161 - x254)^2 + (x301 - x394)^2) + 1 / sqrt((x21 - x115)
    ^2 + (x161 - x255)^2 + (x301 - x395)^2) + 1 / sqrt((x21 - x116)^2 + (x161
    - x256)^2 + (x301 - x396)^2) + 1 / sqrt((x21 - x117)^2 + (x161 - x257)^2
    + (x301 - x397)^2) + 1 / sqrt((x21 - x118)^2 + (x161 - x258)^2 + (x301 -
    x398)^2) + 1 / sqrt((x21 - x119)^2 + (x161 - x259)^2 + (x301 - x399)^2) + 1
    / sqrt((x21 - x120)^2 + (x161 - x260)^2 + (x301 - x400)^2) + 1 / sqrt((x21
    - x121)^2 + (x161 - x261)^2 + (x301 - x401)^2) + 1 / sqrt((x21 - x122)^2
    + (x161 - x262)^2 + (x301 - x402)^2) + 1 / sqrt((x21 - x123)^2 + (x161 -
    x263)^2 + (x301 - x403)^2) + 1 / sqrt((x21 - x124)^2 + (x161 - x264)^2 + (
    x301 - x404)^2) + 1 / sqrt((x21 - x125)^2 + (x161 - x265)^2 + (x301 - x405)
    ^2) + 1 / sqrt((x21 - x126)^2 + (x161 - x266)^2 + (x301 - x406)^2) + 1 /
    sqrt((x21 - x127)^2 + (x161 - x267)^2 + (x301 - x407)^2) + 1 / sqrt((x21 -
    x128)^2 + (x161 - x268)^2 + (x301 - x408)^2) + 1 / sqrt((x21 - x129)^2 + (
    x161 - x269)^2 + (x301 - x409)^2) + 1 / sqrt((x21 - x130)^2 + (x161 - x270)
    ^2 + (x301 - x410)^2) + 1 / sqrt((x21 - x131)^2 + (x161 - x271)^2 + (x301
    - x411)^2) + 1 / sqrt((x21 - x132)^2 + (x161 - x272)^2 + (x301 - x412)^2)
    + 1 / sqrt((x21 - x133)^2 + (x161 - x273)^2 + (x301 - x413)^2) + 1 / sqrt(
    (x21 - x134)^2 + (x161 - x274)^2 + (x301 - x414)^2) + 1 / sqrt((x21 - x135)
    ^2 + (x161 - x275)^2 + (x301 - x415)^2) + 1 / sqrt((x21 - x136)^2 + (x161
    - x276)^2 + (x301 - x416)^2) + 1 / sqrt((x21 - x137)^2 + (x161 - x277)^2
    + (x301 - x417)^2) + 1 / sqrt((x21 - x138)^2 + (x161 - x278)^2 + (x301 -
    x418)^2) + 1 / sqrt((x21 - x139)^2 + (x161 - x279)^2 + (x301 - x419)^2) + 1
    / sqrt((x21 - x140)^2 + (x161 - x280)^2 + (x301 - x420)^2) + 1 / sqrt((x22
    - x23)^2 + (x162 - x163)^2 + (x302 - x303)^2) + 1 / sqrt((x22 - x24)^2 + (
    x162 - x164)^2 + (x302 - x304)^2) + 1 / sqrt((x22 - x25)^2 + (x162 - x165)^
    2 + (x302 - x305)^2) + 1 / sqrt((x22 - x26)^2 + (x162 - x166)^2 + (x302 -
    x306)^2) + 1 / sqrt((x22 - x27)^2 + (x162 - x167)^2 + (x302 - x307)^2) + 1
    / sqrt((x22 - x28)^2 + (x162 - x168)^2 + (x302 - x308)^2) + 1 / sqrt((x22
    - x29)^2 + (x162 - x169)^2 + (x302 - x309)^2) + 1 / sqrt((x22 - x30)^2 + (
    x162 - x170)^2 + (x302 - x310)^2) + 1 / sqrt((x22 - x31)^2 + (x162 - x171)^
    2 + (x302 - x311)^2) + 1 / sqrt((x22 - x32)^2 + (x162 - x172)^2 + (x302 -
    x312)^2) + 1 / sqrt((x22 - x33)^2 + (x162 - x173)^2 + (x302 - x313)^2) + 1
    / sqrt((x22 - x34)^2 + (x162 - x174)^2 + (x302 - x314)^2) + 1 / sqrt((x22
    - x35)^2 + (x162 - x175)^2 + (x302 - x315)^2) + 1 / sqrt((x22 - x36)^2 + (
    x162 - x176)^2 + (x302 - x316)^2) + 1 / sqrt((x22 - x37)^2 + (x162 - x177)^
    2 + (x302 - x317)^2) + 1 / sqrt((x22 - x38)^2 + (x162 - x178)^2 + (x302 -
    x318)^2) + 1 / sqrt((x22 - x39)^2 + (x162 - x179)^2 + (x302 - x319)^2) + 1
    / sqrt((x22 - x40)^2 + (x162 - x180)^2 + (x302 - x320)^2) + 1 / sqrt((x22
    - x41)^2 + (x162 - x181)^2 + (x302 - x321)^2) + 1 / sqrt((x22 - x42)^2 + (
    x162 - x182)^2 + (x302 - x322)^2) + 1 / sqrt((x22 - x43)^2 + (x162 - x183)^
    2 + (x302 - x323)^2) + 1 / sqrt((x22 - x44)^2 + (x162 - x184)^2 + (x302 -
    x324)^2) + 1 / sqrt((x22 - x45)^2 + (x162 - x185)^2 + (x302 - x325)^2) + 1
    / sqrt((x22 - x46)^2 + (x162 - x186)^2 + (x302 - x326)^2) + 1 / sqrt((x22
    - x47)^2 + (x162 - x187)^2 + (x302 - x327)^2) + 1 / sqrt((x22 - x48)^2 + (
    x162 - x188)^2 + (x302 - x328)^2) + 1 / sqrt((x22 - x49)^2 + (x162 - x189)^
    2 + (x302 - x329)^2) + 1 / sqrt((x22 - x50)^2 + (x162 - x190)^2 + (x302 -
    x330)^2) + 1 / sqrt((x22 - x51)^2 + (x162 - x191)^2 + (x302 - x331)^2) + 1
    / sqrt((x22 - x52)^2 + (x162 - x192)^2 + (x302 - x332)^2) + 1 / sqrt((x22
    - x53)^2 + (x162 - x193)^2 + (x302 - x333)^2) + 1 / sqrt((x22 - x54)^2 + (
    x162 - x194)^2 + (x302 - x334)^2) + 1 / sqrt((x22 - x55)^2 + (x162 - x195)^
    2 + (x302 - x335)^2) + 1 / sqrt((x22 - x56)^2 + (x162 - x196)^2 + (x302 -
    x336)^2) + 1 / sqrt((x22 - x57)^2 + (x162 - x197)^2 + (x302 - x337)^2) + 1
    / sqrt((x22 - x58)^2 + (x162 - x198)^2 + (x302 - x338)^2) + 1 / sqrt((x22
    - x59)^2 + (x162 - x199)^2 + (x302 - x339)^2) + 1 / sqrt((x22 - x60)^2 + (
    x162 - x200)^2 + (x302 - x340)^2) + 1 / sqrt((x22 - x61)^2 + (x162 - x201)^
    2 + (x302 - x341)^2) + 1 / sqrt((x22 - x62)^2 + (x162 - x202)^2 + (x302 -
    x342)^2) + 1 / sqrt((x22 - x63)^2 + (x162 - x203)^2 + (x302 - x343)^2) + 1
    / sqrt((x22 - x64)^2 + (x162 - x204)^2 + (x302 - x344)^2) + 1 / sqrt((x22
    - x65)^2 + (x162 - x205)^2 + (x302 - x345)^2) + 1 / sqrt((x22 - x66)^2 + (
    x162 - x206)^2 + (x302 - x346)^2) + 1 / sqrt((x22 - x67)^2 + (x162 - x207)^
    2 + (x302 - x347)^2) + 1 / sqrt((x22 - x68)^2 + (x162 - x208)^2 + (x302 -
    x348)^2) + 1 / sqrt((x22 - x69)^2 + (x162 - x209)^2 + (x302 - x349)^2) + 1
    / sqrt((x22 - x70)^2 + (x162 - x210)^2 + (x302 - x350)^2) + 1 / sqrt((x22
    - x71)^2 + (x162 - x211)^2 + (x302 - x351)^2) + 1 / sqrt((x22 - x72)^2 + (
    x162 - x212)^2 + (x302 - x352)^2) + 1 / sqrt((x22 - x73)^2 + (x162 - x213)^
    2 + (x302 - x353)^2) + 1 / sqrt((x22 - x74)^2 + (x162 - x214)^2 + (x302 -
    x354)^2) + 1 / sqrt((x22 - x75)^2 + (x162 - x215)^2 + (x302 - x355)^2) + 1
    / sqrt((x22 - x76)^2 + (x162 - x216)^2 + (x302 - x356)^2) + 1 / sqrt((x22
    - x77)^2 + (x162 - x217)^2 + (x302 - x357)^2) + 1 / sqrt((x22 - x78)^2 + (
    x162 - x218)^2 + (x302 - x358)^2) + 1 / sqrt((x22 - x79)^2 + (x162 - x219)^
    2 + (x302 - x359)^2) + 1 / sqrt((x22 - x80)^2 + (x162 - x220)^2 + (x302 -
    x360)^2) + 1 / sqrt((x22 - x81)^2 + (x162 - x221)^2 + (x302 - x361)^2) + 1
    / sqrt((x22 - x82)^2 + (x162 - x222)^2 + (x302 - x362)^2) + 1 / sqrt((x22
    - x83)^2 + (x162 - x223)^2 + (x302 - x363)^2) + 1 / sqrt((x22 - x84)^2 + (
    x162 - x224)^2 + (x302 - x364)^2) + 1 / sqrt((x22 - x85)^2 + (x162 - x225)^
    2 + (x302 - x365)^2) + 1 / sqrt((x22 - x86)^2 + (x162 - x226)^2 + (x302 -
    x366)^2) + 1 / sqrt((x22 - x87)^2 + (x162 - x227)^2 + (x302 - x367)^2) + 1
    / sqrt((x22 - x88)^2 + (x162 - x228)^2 + (x302 - x368)^2) + 1 / sqrt((x22
    - x89)^2 + (x162 - x229)^2 + (x302 - x369)^2) + 1 / sqrt((x22 - x90)^2 + (
    x162 - x230)^2 + (x302 - x370)^2) + 1 / sqrt((x22 - x91)^2 + (x162 - x231)^
    2 + (x302 - x371)^2) + 1 / sqrt((x22 - x92)^2 + (x162 - x232)^2 + (x302 -
    x372)^2) + 1 / sqrt((x22 - x93)^2 + (x162 - x233)^2 + (x302 - x373)^2) + 1
    / sqrt((x22 - x94)^2 + (x162 - x234)^2 + (x302 - x374)^2) + 1 / sqrt((x22
    - x95)^2 + (x162 - x235)^2 + (x302 - x375)^2) + 1 / sqrt((x22 - x96)^2 + (
    x162 - x236)^2 + (x302 - x376)^2) + 1 / sqrt((x22 - x97)^2 + (x162 - x237)^
    2 + (x302 - x377)^2) + 1 / sqrt((x22 - x98)^2 + (x162 - x238)^2 + (x302 -
    x378)^2) + 1 / sqrt((x22 - x99)^2 + (x162 - x239)^2 + (x302 - x379)^2) + 1
    / sqrt((x22 - x100)^2 + (x162 - x240)^2 + (x302 - x380)^2) + 1 / sqrt((x22
    - x101)^2 + (x162 - x241)^2 + (x302 - x381)^2) + 1 / sqrt((x22 - x102)^2
    + (x162 - x242)^2 + (x302 - x382)^2) + 1 / sqrt((x22 - x103)^2 + (x162 -
    x243)^2 + (x302 - x383)^2) + 1 / sqrt((x22 - x104)^2 + (x162 - x244)^2 + (
    x302 - x384)^2) + 1 / sqrt((x22 - x105)^2 + (x162 - x245)^2 + (x302 - x385)
    ^2) + 1 / sqrt((x22 - x106)^2 + (x162 - x246)^2 + (x302 - x386)^2) + 1 /
    sqrt((x22 - x107)^2 + (x162 - x247)^2 + (x302 - x387)^2) + 1 / sqrt((x22 -
    x108)^2 + (x162 - x248)^2 + (x302 - x388)^2) + 1 / sqrt((x22 - x109)^2 + (
    x162 - x249)^2 + (x302 - x389)^2) + 1 / sqrt((x22 - x110)^2 + (x162 - x250)
    ^2 + (x302 - x390)^2) + 1 / sqrt((x22 - x111)^2 + (x162 - x251)^2 + (x302
    - x391)^2) + 1 / sqrt((x22 - x112)^2 + (x162 - x252)^2 + (x302 - x392)^2)
    + 1 / sqrt((x22 - x113)^2 + (x162 - x253)^2 + (x302 - x393)^2) + 1 / sqrt(
    (x22 - x114)^2 + (x162 - x254)^2 + (x302 - x394)^2) + 1 / sqrt((x22 - x115)
    ^2 + (x162 - x255)^2 + (x302 - x395)^2) + 1 / sqrt((x22 - x116)^2 + (x162
    - x256)^2 + (x302 - x396)^2) + 1 / sqrt((x22 - x117)^2 + (x162 - x257)^2
    + (x302 - x397)^2) + 1 / sqrt((x22 - x118)^2 + (x162 - x258)^2 + (x302 -
    x398)^2) + 1 / sqrt((x22 - x119)^2 + (x162 - x259)^2 + (x302 - x399)^2) + 1
    / sqrt((x22 - x120)^2 + (x162 - x260)^2 + (x302 - x400)^2) + 1 / sqrt((x22
    - x121)^2 + (x162 - x261)^2 + (x302 - x401)^2) + 1 / sqrt((x22 - x122)^2
    + (x162 - x262)^2 + (x302 - x402)^2) + 1 / sqrt((x22 - x123)^2 + (x162 -
    x263)^2 + (x302 - x403)^2) + 1 / sqrt((x22 - x124)^2 + (x162 - x264)^2 + (
    x302 - x404)^2) + 1 / sqrt((x22 - x125)^2 + (x162 - x265)^2 + (x302 - x405)
    ^2) + 1 / sqrt((x22 - x126)^2 + (x162 - x266)^2 + (x302 - x406)^2) + 1 /
    sqrt((x22 - x127)^2 + (x162 - x267)^2 + (x302 - x407)^2) + 1 / sqrt((x22 -
    x128)^2 + (x162 - x268)^2 + (x302 - x408)^2) + 1 / sqrt((x22 - x129)^2 + (
    x162 - x269)^2 + (x302 - x409)^2) + 1 / sqrt((x22 - x130)^2 + (x162 - x270)
    ^2 + (x302 - x410)^2) + 1 / sqrt((x22 - x131)^2 + (x162 - x271)^2 + (x302
    - x411)^2) + 1 / sqrt((x22 - x132)^2 + (x162 - x272)^2 + (x302 - x412)^2)
    + 1 / sqrt((x22 - x133)^2 + (x162 - x273)^2 + (x302 - x413)^2) + 1 / sqrt(
    (x22 - x134)^2 + (x162 - x274)^2 + (x302 - x414)^2) + 1 / sqrt((x22 - x135)
    ^2 + (x162 - x275)^2 + (x302 - x415)^2) + 1 / sqrt((x22 - x136)^2 + (x162
    - x276)^2 + (x302 - x416)^2) + 1 / sqrt((x22 - x137)^2 + (x162 - x277)^2
    + (x302 - x417)^2) + 1 / sqrt((x22 - x138)^2 + (x162 - x278)^2 + (x302 -
    x418)^2) + 1 / sqrt((x22 - x139)^2 + (x162 - x279)^2 + (x302 - x419)^2) + 1
    / sqrt((x22 - x140)^2 + (x162 - x280)^2 + (x302 - x420)^2) + 1 / sqrt((x23
    - x24)^2 + (x163 - x164)^2 + (x303 - x304)^2) + 1 / sqrt((x23 - x25)^2 + (
    x163 - x165)^2 + (x303 - x305)^2) + 1 / sqrt((x23 - x26)^2 + (x163 - x166)^
    2 + (x303 - x306)^2) + 1 / sqrt((x23 - x27)^2 + (x163 - x167)^2 + (x303 -
    x307)^2) + 1 / sqrt((x23 - x28)^2 + (x163 - x168)^2 + (x303 - x308)^2) + 1
    / sqrt((x23 - x29)^2 + (x163 - x169)^2 + (x303 - x309)^2) + 1 / sqrt((x23
    - x30)^2 + (x163 - x170)^2 + (x303 - x310)^2) + 1 / sqrt((x23 - x31)^2 + (
    x163 - x171)^2 + (x303 - x311)^2) + 1 / sqrt((x23 - x32)^2 + (x163 - x172)^
    2 + (x303 - x312)^2) + 1 / sqrt((x23 - x33)^2 + (x163 - x173)^2 + (x303 -
    x313)^2) + 1 / sqrt((x23 - x34)^2 + (x163 - x174)^2 + (x303 - x314)^2) + 1
    / sqrt((x23 - x35)^2 + (x163 - x175)^2 + (x303 - x315)^2) + 1 / sqrt((x23
    - x36)^2 + (x163 - x176)^2 + (x303 - x316)^2) + 1 / sqrt((x23 - x37)^2 + (
    x163 - x177)^2 + (x303 - x317)^2) + 1 / sqrt((x23 - x38)^2 + (x163 - x178)^
    2 + (x303 - x318)^2) + 1 / sqrt((x23 - x39)^2 + (x163 - x179)^2 + (x303 -
    x319)^2) + 1 / sqrt((x23 - x40)^2 + (x163 - x180)^2 + (x303 - x320)^2) + 1
    / sqrt((x23 - x41)^2 + (x163 - x181)^2 + (x303 - x321)^2) + 1 / sqrt((x23
    - x42)^2 + (x163 - x182)^2 + (x303 - x322)^2) + 1 / sqrt((x23 - x43)^2 + (
    x163 - x183)^2 + (x303 - x323)^2) + 1 / sqrt((x23 - x44)^2 + (x163 - x184)^
    2 + (x303 - x324)^2) + 1 / sqrt((x23 - x45)^2 + (x163 - x185)^2 + (x303 -
    x325)^2) + 1 / sqrt((x23 - x46)^2 + (x163 - x186)^2 + (x303 - x326)^2) + 1
    / sqrt((x23 - x47)^2 + (x163 - x187)^2 + (x303 - x327)^2) + 1 / sqrt((x23
    - x48)^2 + (x163 - x188)^2 + (x303 - x328)^2) + 1 / sqrt((x23 - x49)^2 + (
    x163 - x189)^2 + (x303 - x329)^2) + 1 / sqrt((x23 - x50)^2 + (x163 - x190)^
    2 + (x303 - x330)^2) + 1 / sqrt((x23 - x51)^2 + (x163 - x191)^2 + (x303 -
    x331)^2) + 1 / sqrt((x23 - x52)^2 + (x163 - x192)^2 + (x303 - x332)^2) + 1
    / sqrt((x23 - x53)^2 + (x163 - x193)^2 + (x303 - x333)^2) + 1 / sqrt((x23
    - x54)^2 + (x163 - x194)^2 + (x303 - x334)^2) + 1 / sqrt((x23 - x55)^2 + (
    x163 - x195)^2 + (x303 - x335)^2) + 1 / sqrt((x23 - x56)^2 + (x163 - x196)^
    2 + (x303 - x336)^2) + 1 / sqrt((x23 - x57)^2 + (x163 - x197)^2 + (x303 -
    x337)^2) + 1 / sqrt((x23 - x58)^2 + (x163 - x198)^2 + (x303 - x338)^2) + 1
    / sqrt((x23 - x59)^2 + (x163 - x199)^2 + (x303 - x339)^2) + 1 / sqrt((x23
    - x60)^2 + (x163 - x200)^2 + (x303 - x340)^2) + 1 / sqrt((x23 - x61)^2 + (
    x163 - x201)^2 + (x303 - x341)^2) + 1 / sqrt((x23 - x62)^2 + (x163 - x202)^
    2 + (x303 - x342)^2) + 1 / sqrt((x23 - x63)^2 + (x163 - x203)^2 + (x303 -
    x343)^2) + 1 / sqrt((x23 - x64)^2 + (x163 - x204)^2 + (x303 - x344)^2) + 1
    / sqrt((x23 - x65)^2 + (x163 - x205)^2 + (x303 - x345)^2) + 1 / sqrt((x23
    - x66)^2 + (x163 - x206)^2 + (x303 - x346)^2) + 1 / sqrt((x23 - x67)^2 + (
    x163 - x207)^2 + (x303 - x347)^2) + 1 / sqrt((x23 - x68)^2 + (x163 - x208)^
    2 + (x303 - x348)^2) + 1 / sqrt((x23 - x69)^2 + (x163 - x209)^2 + (x303 -
    x349)^2) + 1 / sqrt((x23 - x70)^2 + (x163 - x210)^2 + (x303 - x350)^2) + 1
    / sqrt((x23 - x71)^2 + (x163 - x211)^2 + (x303 - x351)^2) + 1 / sqrt((x23
    - x72)^2 + (x163 - x212)^2 + (x303 - x352)^2) + 1 / sqrt((x23 - x73)^2 + (
    x163 - x213)^2 + (x303 - x353)^2) + 1 / sqrt((x23 - x74)^2 + (x163 - x214)^
    2 + (x303 - x354)^2) + 1 / sqrt((x23 - x75)^2 + (x163 - x215)^2 + (x303 -
    x355)^2) + 1 / sqrt((x23 - x76)^2 + (x163 - x216)^2 + (x303 - x356)^2) + 1
    / sqrt((x23 - x77)^2 + (x163 - x217)^2 + (x303 - x357)^2) + 1 / sqrt((x23
    - x78)^2 + (x163 - x218)^2 + (x303 - x358)^2) + 1 / sqrt((x23 - x79)^2 + (
    x163 - x219)^2 + (x303 - x359)^2) + 1 / sqrt((x23 - x80)^2 + (x163 - x220)^
    2 + (x303 - x360)^2) + 1 / sqrt((x23 - x81)^2 + (x163 - x221)^2 + (x303 -
    x361)^2) + 1 / sqrt((x23 - x82)^2 + (x163 - x222)^2 + (x303 - x362)^2) + 1
    / sqrt((x23 - x83)^2 + (x163 - x223)^2 + (x303 - x363)^2) + 1 / sqrt((x23
    - x84)^2 + (x163 - x224)^2 + (x303 - x364)^2) + 1 / sqrt((x23 - x85)^2 + (
    x163 - x225)^2 + (x303 - x365)^2) + 1 / sqrt((x23 - x86)^2 + (x163 - x226)^
    2 + (x303 - x366)^2) + 1 / sqrt((x23 - x87)^2 + (x163 - x227)^2 + (x303 -
    x367)^2) + 1 / sqrt((x23 - x88)^2 + (x163 - x228)^2 + (x303 - x368)^2) + 1
    / sqrt((x23 - x89)^2 + (x163 - x229)^2 + (x303 - x369)^2) + 1 / sqrt((x23
    - x90)^2 + (x163 - x230)^2 + (x303 - x370)^2) + 1 / sqrt((x23 - x91)^2 + (
    x163 - x231)^2 + (x303 - x371)^2) + 1 / sqrt((x23 - x92)^2 + (x163 - x232)^
    2 + (x303 - x372)^2) + 1 / sqrt((x23 - x93)^2 + (x163 - x233)^2 + (x303 -
    x373)^2) + 1 / sqrt((x23 - x94)^2 + (x163 - x234)^2 + (x303 - x374)^2) + 1
    / sqrt((x23 - x95)^2 + (x163 - x235)^2 + (x303 - x375)^2) + 1 / sqrt((x23
    - x96)^2 + (x163 - x236)^2 + (x303 - x376)^2) + 1 / sqrt((x23 - x97)^2 + (
    x163 - x237)^2 + (x303 - x377)^2) + 1 / sqrt((x23 - x98)^2 + (x163 - x238)^
    2 + (x303 - x378)^2) + 1 / sqrt((x23 - x99)^2 + (x163 - x239)^2 + (x303 -
    x379)^2) + 1 / sqrt((x23 - x100)^2 + (x163 - x240)^2 + (x303 - x380)^2) + 1
    / sqrt((x23 - x101)^2 + (x163 - x241)^2 + (x303 - x381)^2) + 1 / sqrt((x23
    - x102)^2 + (x163 - x242)^2 + (x303 - x382)^2) + 1 / sqrt((x23 - x103)^2
    + (x163 - x243)^2 + (x303 - x383)^2) + 1 / sqrt((x23 - x104)^2 + (x163 -
    x244)^2 + (x303 - x384)^2) + 1 / sqrt((x23 - x105)^2 + (x163 - x245)^2 + (
    x303 - x385)^2) + 1 / sqrt((x23 - x106)^2 + (x163 - x246)^2 + (x303 - x386)
    ^2) + 1 / sqrt((x23 - x107)^2 + (x163 - x247)^2 + (x303 - x387)^2) + 1 /
    sqrt((x23 - x108)^2 + (x163 - x248)^2 + (x303 - x388)^2) + 1 / sqrt((x23 -
    x109)^2 + (x163 - x249)^2 + (x303 - x389)^2) + 1 / sqrt((x23 - x110)^2 + (
    x163 - x250)^2 + (x303 - x390)^2) + 1 / sqrt((x23 - x111)^2 + (x163 - x251)
    ^2 + (x303 - x391)^2) + 1 / sqrt((x23 - x112)^2 + (x163 - x252)^2 + (x303
    - x392)^2) + 1 / sqrt((x23 - x113)^2 + (x163 - x253)^2 + (x303 - x393)^2)
    + 1 / sqrt((x23 - x114)^2 + (x163 - x254)^2 + (x303 - x394)^2) + 1 / sqrt(
    (x23 - x115)^2 + (x163 - x255)^2 + (x303 - x395)^2) + 1 / sqrt((x23 - x116)
    ^2 + (x163 - x256)^2 + (x303 - x396)^2) + 1 / sqrt((x23 - x117)^2 + (x163
    - x257)^2 + (x303 - x397)^2) + 1 / sqrt((x23 - x118)^2 + (x163 - x258)^2
    + (x303 - x398)^2) + 1 / sqrt((x23 - x119)^2 + (x163 - x259)^2 + (x303 -
    x399)^2) + 1 / sqrt((x23 - x120)^2 + (x163 - x260)^2 + (x303 - x400)^2) + 1
    / sqrt((x23 - x121)^2 + (x163 - x261)^2 + (x303 - x401)^2) + 1 / sqrt((x23
    - x122)^2 + (x163 - x262)^2 + (x303 - x402)^2) + 1 / sqrt((x23 - x123)^2
    + (x163 - x263)^2 + (x303 - x403)^2) + 1 / sqrt((x23 - x124)^2 + (x163 -
    x264)^2 + (x303 - x404)^2) + 1 / sqrt((x23 - x125)^2 + (x163 - x265)^2 + (
    x303 - x405)^2) + 1 / sqrt((x23 - x126)^2 + (x163 - x266)^2 + (x303 - x406)
    ^2) + 1 / sqrt((x23 - x127)^2 + (x163 - x267)^2 + (x303 - x407)^2) + 1 /
    sqrt((x23 - x128)^2 + (x163 - x268)^2 + (x303 - x408)^2) + 1 / sqrt((x23 -
    x129)^2 + (x163 - x269)^2 + (x303 - x409)^2) + 1 / sqrt((x23 - x130)^2 + (
    x163 - x270)^2 + (x303 - x410)^2) + 1 / sqrt((x23 - x131)^2 + (x163 - x271)
    ^2 + (x303 - x411)^2) + 1 / sqrt((x23 - x132)^2 + (x163 - x272)^2 + (x303
    - x412)^2) + 1 / sqrt((x23 - x133)^2 + (x163 - x273)^2 + (x303 - x413)^2)
    + 1 / sqrt((x23 - x134)^2 + (x163 - x274)^2 + (x303 - x414)^2) + 1 / sqrt(
    (x23 - x135)^2 + (x163 - x275)^2 + (x303 - x415)^2) + 1 / sqrt((x23 - x136)
    ^2 + (x163 - x276)^2 + (x303 - x416)^2) + 1 / sqrt((x23 - x137)^2 + (x163
    - x277)^2 + (x303 - x417)^2) + 1 / sqrt((x23 - x138)^2 + (x163 - x278)^2
    + (x303 - x418)^2) + 1 / sqrt((x23 - x139)^2 + (x163 - x279)^2 + (x303 -
    x419)^2) + 1 / sqrt((x23 - x140)^2 + (x163 - x280)^2 + (x303 - x420)^2) + 1
    / sqrt((x24 - x25)^2 + (x164 - x165)^2 + (x304 - x305)^2) + 1 / sqrt((x24
    - x26)^2 + (x164 - x166)^2 + (x304 - x306)^2) + 1 / sqrt((x24 - x27)^2 + (
    x164 - x167)^2 + (x304 - x307)^2) + 1 / sqrt((x24 - x28)^2 + (x164 - x168)^
    2 + (x304 - x308)^2) + 1 / sqrt((x24 - x29)^2 + (x164 - x169)^2 + (x304 -
    x309)^2) + 1 / sqrt((x24 - x30)^2 + (x164 - x170)^2 + (x304 - x310)^2) + 1
    / sqrt((x24 - x31)^2 + (x164 - x171)^2 + (x304 - x311)^2) + 1 / sqrt((x24
    - x32)^2 + (x164 - x172)^2 + (x304 - x312)^2) + 1 / sqrt((x24 - x33)^2 + (
    x164 - x173)^2 + (x304 - x313)^2) + 1 / sqrt((x24 - x34)^2 + (x164 - x174)^
    2 + (x304 - x314)^2) + 1 / sqrt((x24 - x35)^2 + (x164 - x175)^2 + (x304 -
    x315)^2) + 1 / sqrt((x24 - x36)^2 + (x164 - x176)^2 + (x304 - x316)^2) + 1
    / sqrt((x24 - x37)^2 + (x164 - x177)^2 + (x304 - x317)^2) + 1 / sqrt((x24
    - x38)^2 + (x164 - x178)^2 + (x304 - x318)^2) + 1 / sqrt((x24 - x39)^2 + (
    x164 - x179)^2 + (x304 - x319)^2) + 1 / sqrt((x24 - x40)^2 + (x164 - x180)^
    2 + (x304 - x320)^2) + 1 / sqrt((x24 - x41)^2 + (x164 - x181)^2 + (x304 -
    x321)^2) + 1 / sqrt((x24 - x42)^2 + (x164 - x182)^2 + (x304 - x322)^2) + 1
    / sqrt((x24 - x43)^2 + (x164 - x183)^2 + (x304 - x323)^2) + 1 / sqrt((x24
    - x44)^2 + (x164 - x184)^2 + (x304 - x324)^2) + 1 / sqrt((x24 - x45)^2 + (
    x164 - x185)^2 + (x304 - x325)^2) + 1 / sqrt((x24 - x46)^2 + (x164 - x186)^
    2 + (x304 - x326)^2) + 1 / sqrt((x24 - x47)^2 + (x164 - x187)^2 + (x304 -
    x327)^2) + 1 / sqrt((x24 - x48)^2 + (x164 - x188)^2 + (x304 - x328)^2) + 1
    / sqrt((x24 - x49)^2 + (x164 - x189)^2 + (x304 - x329)^2) + 1 / sqrt((x24
    - x50)^2 + (x164 - x190)^2 + (x304 - x330)^2) + 1 / sqrt((x24 - x51)^2 + (
    x164 - x191)^2 + (x304 - x331)^2) + 1 / sqrt((x24 - x52)^2 + (x164 - x192)^
    2 + (x304 - x332)^2) + 1 / sqrt((x24 - x53)^2 + (x164 - x193)^2 + (x304 -
    x333)^2) + 1 / sqrt((x24 - x54)^2 + (x164 - x194)^2 + (x304 - x334)^2) + 1
    / sqrt((x24 - x55)^2 + (x164 - x195)^2 + (x304 - x335)^2) + 1 / sqrt((x24
    - x56)^2 + (x164 - x196)^2 + (x304 - x336)^2) + 1 / sqrt((x24 - x57)^2 + (
    x164 - x197)^2 + (x304 - x337)^2) + 1 / sqrt((x24 - x58)^2 + (x164 - x198)^
    2 + (x304 - x338)^2) + 1 / sqrt((x24 - x59)^2 + (x164 - x199)^2 + (x304 -
    x339)^2) + 1 / sqrt((x24 - x60)^2 + (x164 - x200)^2 + (x304 - x340)^2) + 1
    / sqrt((x24 - x61)^2 + (x164 - x201)^2 + (x304 - x341)^2) + 1 / sqrt((x24
    - x62)^2 + (x164 - x202)^2 + (x304 - x342)^2) + 1 / sqrt((x24 - x63)^2 + (
    x164 - x203)^2 + (x304 - x343)^2) + 1 / sqrt((x24 - x64)^2 + (x164 - x204)^
    2 + (x304 - x344)^2) + 1 / sqrt((x24 - x65)^2 + (x164 - x205)^2 + (x304 -
    x345)^2) + 1 / sqrt((x24 - x66)^2 + (x164 - x206)^2 + (x304 - x346)^2) + 1
    / sqrt((x24 - x67)^2 + (x164 - x207)^2 + (x304 - x347)^2) + 1 / sqrt((x24
    - x68)^2 + (x164 - x208)^2 + (x304 - x348)^2) + 1 / sqrt((x24 - x69)^2 + (
    x164 - x209)^2 + (x304 - x349)^2) + 1 / sqrt((x24 - x70)^2 + (x164 - x210)^
    2 + (x304 - x350)^2) + 1 / sqrt((x24 - x71)^2 + (x164 - x211)^2 + (x304 -
    x351)^2) + 1 / sqrt((x24 - x72)^2 + (x164 - x212)^2 + (x304 - x352)^2) + 1
    / sqrt((x24 - x73)^2 + (x164 - x213)^2 + (x304 - x353)^2) + 1 / sqrt((x24
    - x74)^2 + (x164 - x214)^2 + (x304 - x354)^2) + 1 / sqrt((x24 - x75)^2 + (
    x164 - x215)^2 + (x304 - x355)^2) + 1 / sqrt((x24 - x76)^2 + (x164 - x216)^
    2 + (x304 - x356)^2) + 1 / sqrt((x24 - x77)^2 + (x164 - x217)^2 + (x304 -
    x357)^2) + 1 / sqrt((x24 - x78)^2 + (x164 - x218)^2 + (x304 - x358)^2) + 1
    / sqrt((x24 - x79)^2 + (x164 - x219)^2 + (x304 - x359)^2) + 1 / sqrt((x24
    - x80)^2 + (x164 - x220)^2 + (x304 - x360)^2) + 1 / sqrt((x24 - x81)^2 + (
    x164 - x221)^2 + (x304 - x361)^2) + 1 / sqrt((x24 - x82)^2 + (x164 - x222)^
    2 + (x304 - x362)^2) + 1 / sqrt((x24 - x83)^2 + (x164 - x223)^2 + (x304 -
    x363)^2) + 1 / sqrt((x24 - x84)^2 + (x164 - x224)^2 + (x304 - x364)^2) + 1
    / sqrt((x24 - x85)^2 + (x164 - x225)^2 + (x304 - x365)^2) + 1 / sqrt((x24
    - x86)^2 + (x164 - x226)^2 + (x304 - x366)^2) + 1 / sqrt((x24 - x87)^2 + (
    x164 - x227)^2 + (x304 - x367)^2) + 1 / sqrt((x24 - x88)^2 + (x164 - x228)^
    2 + (x304 - x368)^2) + 1 / sqrt((x24 - x89)^2 + (x164 - x229)^2 + (x304 -
    x369)^2) + 1 / sqrt((x24 - x90)^2 + (x164 - x230)^2 + (x304 - x370)^2) + 1
    / sqrt((x24 - x91)^2 + (x164 - x231)^2 + (x304 - x371)^2) + 1 / sqrt((x24
    - x92)^2 + (x164 - x232)^2 + (x304 - x372)^2) + 1 / sqrt((x24 - x93)^2 + (
    x164 - x233)^2 + (x304 - x373)^2) + 1 / sqrt((x24 - x94)^2 + (x164 - x234)^
    2 + (x304 - x374)^2) + 1 / sqrt((x24 - x95)^2 + (x164 - x235)^2 + (x304 -
    x375)^2) + 1 / sqrt((x24 - x96)^2 + (x164 - x236)^2 + (x304 - x376)^2) + 1
    / sqrt((x24 - x97)^2 + (x164 - x237)^2 + (x304 - x377)^2) + 1 / sqrt((x24
    - x98)^2 + (x164 - x238)^2 + (x304 - x378)^2) + 1 / sqrt((x24 - x99)^2 + (
    x164 - x239)^2 + (x304 - x379)^2) + 1 / sqrt((x24 - x100)^2 + (x164 - x240)
    ^2 + (x304 - x380)^2) + 1 / sqrt((x24 - x101)^2 + (x164 - x241)^2 + (x304
    - x381)^2) + 1 / sqrt((x24 - x102)^2 + (x164 - x242)^2 + (x304 - x382)^2)
    + 1 / sqrt((x24 - x103)^2 + (x164 - x243)^2 + (x304 - x383)^2) + 1 / sqrt(
    (x24 - x104)^2 + (x164 - x244)^2 + (x304 - x384)^2) + 1 / sqrt((x24 - x105)
    ^2 + (x164 - x245)^2 + (x304 - x385)^2) + 1 / sqrt((x24 - x106)^2 + (x164
    - x246)^2 + (x304 - x386)^2) + 1 / sqrt((x24 - x107)^2 + (x164 - x247)^2
    + (x304 - x387)^2) + 1 / sqrt((x24 - x108)^2 + (x164 - x248)^2 + (x304 -
    x388)^2) + 1 / sqrt((x24 - x109)^2 + (x164 - x249)^2 + (x304 - x389)^2) + 1
    / sqrt((x24 - x110)^2 + (x164 - x250)^2 + (x304 - x390)^2) + 1 / sqrt((x24
    - x111)^2 + (x164 - x251)^2 + (x304 - x391)^2) + 1 / sqrt((x24 - x112)^2
    + (x164 - x252)^2 + (x304 - x392)^2) + 1 / sqrt((x24 - x113)^2 + (x164 -
    x253)^2 + (x304 - x393)^2) + 1 / sqrt((x24 - x114)^2 + (x164 - x254)^2 + (
    x304 - x394)^2) + 1 / sqrt((x24 - x115)^2 + (x164 - x255)^2 + (x304 - x395)
    ^2) + 1 / sqrt((x24 - x116)^2 + (x164 - x256)^2 + (x304 - x396)^2) + 1 /
    sqrt((x24 - x117)^2 + (x164 - x257)^2 + (x304 - x397)^2) + 1 / sqrt((x24 -
    x118)^2 + (x164 - x258)^2 + (x304 - x398)^2) + 1 / sqrt((x24 - x119)^2 + (
    x164 - x259)^2 + (x304 - x399)^2) + 1 / sqrt((x24 - x120)^2 + (x164 - x260)
    ^2 + (x304 - x400)^2) + 1 / sqrt((x24 - x121)^2 + (x164 - x261)^2 + (x304
    - x401)^2) + 1 / sqrt((x24 - x122)^2 + (x164 - x262)^2 + (x304 - x402)^2)
    + 1 / sqrt((x24 - x123)^2 + (x164 - x263)^2 + (x304 - x403)^2) + 1 / sqrt(
    (x24 - x124)^2 + (x164 - x264)^2 + (x304 - x404)^2) + 1 / sqrt((x24 - x125)
    ^2 + (x164 - x265)^2 + (x304 - x405)^2) + 1 / sqrt((x24 - x126)^2 + (x164
    - x266)^2 + (x304 - x406)^2) + 1 / sqrt((x24 - x127)^2 + (x164 - x267)^2
    + (x304 - x407)^2) + 1 / sqrt((x24 - x128)^2 + (x164 - x268)^2 + (x304 -
    x408)^2) + 1 / sqrt((x24 - x129)^2 + (x164 - x269)^2 + (x304 - x409)^2) + 1
    / sqrt((x24 - x130)^2 + (x164 - x270)^2 + (x304 - x410)^2) + 1 / sqrt((x24
    - x131)^2 + (x164 - x271)^2 + (x304 - x411)^2) + 1 / sqrt((x24 - x132)^2
    + (x164 - x272)^2 + (x304 - x412)^2) + 1 / sqrt((x24 - x133)^2 + (x164 -
    x273)^2 + (x304 - x413)^2) + 1 / sqrt((x24 - x134)^2 + (x164 - x274)^2 + (
    x304 - x414)^2) + 1 / sqrt((x24 - x135)^2 + (x164 - x275)^2 + (x304 - x415)
    ^2) + 1 / sqrt((x24 - x136)^2 + (x164 - x276)^2 + (x304 - x416)^2) + 1 /
    sqrt((x24 - x137)^2 + (x164 - x277)^2 + (x304 - x417)^2) + 1 / sqrt((x24 -
    x138)^2 + (x164 - x278)^2 + (x304 - x418)^2) + 1 / sqrt((x24 - x139)^2 + (
    x164 - x279)^2 + (x304 - x419)^2) + 1 / sqrt((x24 - x140)^2 + (x164 - x280)
    ^2 + (x304 - x420)^2) + 1 / sqrt((x25 - x26)^2 + (x165 - x166)^2 + (x305 -
    x306)^2) + 1 / sqrt((x25 - x27)^2 + (x165 - x167)^2 + (x305 - x307)^2) + 1
    / sqrt((x25 - x28)^2 + (x165 - x168)^2 + (x305 - x308)^2) + 1 / sqrt((x25
    - x29)^2 + (x165 - x169)^2 + (x305 - x309)^2) + 1 / sqrt((x25 - x30)^2 + (
    x165 - x170)^2 + (x305 - x310)^2) + 1 / sqrt((x25 - x31)^2 + (x165 - x171)^
    2 + (x305 - x311)^2) + 1 / sqrt((x25 - x32)^2 + (x165 - x172)^2 + (x305 -
    x312)^2) + 1 / sqrt((x25 - x33)^2 + (x165 - x173)^2 + (x305 - x313)^2) + 1
    / sqrt((x25 - x34)^2 + (x165 - x174)^2 + (x305 - x314)^2) + 1 / sqrt((x25
    - x35)^2 + (x165 - x175)^2 + (x305 - x315)^2) + 1 / sqrt((x25 - x36)^2 + (
    x165 - x176)^2 + (x305 - x316)^2) + 1 / sqrt((x25 - x37)^2 + (x165 - x177)^
    2 + (x305 - x317)^2) + 1 / sqrt((x25 - x38)^2 + (x165 - x178)^2 + (x305 -
    x318)^2) + 1 / sqrt((x25 - x39)^2 + (x165 - x179)^2 + (x305 - x319)^2) + 1
    / sqrt((x25 - x40)^2 + (x165 - x180)^2 + (x305 - x320)^2) + 1 / sqrt((x25
    - x41)^2 + (x165 - x181)^2 + (x305 - x321)^2) + 1 / sqrt((x25 - x42)^2 + (
    x165 - x182)^2 + (x305 - x322)^2) + 1 / sqrt((x25 - x43)^2 + (x165 - x183)^
    2 + (x305 - x323)^2) + 1 / sqrt((x25 - x44)^2 + (x165 - x184)^2 + (x305 -
    x324)^2) + 1 / sqrt((x25 - x45)^2 + (x165 - x185)^2 + (x305 - x325)^2) + 1
    / sqrt((x25 - x46)^2 + (x165 - x186)^2 + (x305 - x326)^2) + 1 / sqrt((x25
    - x47)^2 + (x165 - x187)^2 + (x305 - x327)^2) + 1 / sqrt((x25 - x48)^2 + (
    x165 - x188)^2 + (x305 - x328)^2) + 1 / sqrt((x25 - x49)^2 + (x165 - x189)^
    2 + (x305 - x329)^2) + 1 / sqrt((x25 - x50)^2 + (x165 - x190)^2 + (x305 -
    x330)^2) + 1 / sqrt((x25 - x51)^2 + (x165 - x191)^2 + (x305 - x331)^2) + 1
    / sqrt((x25 - x52)^2 + (x165 - x192)^2 + (x305 - x332)^2) + 1 / sqrt((x25
    - x53)^2 + (x165 - x193)^2 + (x305 - x333)^2) + 1 / sqrt((x25 - x54)^2 + (
    x165 - x194)^2 + (x305 - x334)^2) + 1 / sqrt((x25 - x55)^2 + (x165 - x195)^
    2 + (x305 - x335)^2) + 1 / sqrt((x25 - x56)^2 + (x165 - x196)^2 + (x305 -
    x336)^2) + 1 / sqrt((x25 - x57)^2 + (x165 - x197)^2 + (x305 - x337)^2) + 1
    / sqrt((x25 - x58)^2 + (x165 - x198)^2 + (x305 - x338)^2) + 1 / sqrt((x25
    - x59)^2 + (x165 - x199)^2 + (x305 - x339)^2) + 1 / sqrt((x25 - x60)^2 + (
    x165 - x200)^2 + (x305 - x340)^2) + 1 / sqrt((x25 - x61)^2 + (x165 - x201)^
    2 + (x305 - x341)^2) + 1 / sqrt((x25 - x62)^2 + (x165 - x202)^2 + (x305 -
    x342)^2) + 1 / sqrt((x25 - x63)^2 + (x165 - x203)^2 + (x305 - x343)^2) + 1
    / sqrt((x25 - x64)^2 + (x165 - x204)^2 + (x305 - x344)^2) + 1 / sqrt((x25
    - x65)^2 + (x165 - x205)^2 + (x305 - x345)^2) + 1 / sqrt((x25 - x66)^2 + (
    x165 - x206)^2 + (x305 - x346)^2) + 1 / sqrt((x25 - x67)^2 + (x165 - x207)^
    2 + (x305 - x347)^2) + 1 / sqrt((x25 - x68)^2 + (x165 - x208)^2 + (x305 -
    x348)^2) + 1 / sqrt((x25 - x69)^2 + (x165 - x209)^2 + (x305 - x349)^2) + 1
    / sqrt((x25 - x70)^2 + (x165 - x210)^2 + (x305 - x350)^2) + 1 / sqrt((x25
    - x71)^2 + (x165 - x211)^2 + (x305 - x351)^2) + 1 / sqrt((x25 - x72)^2 + (
    x165 - x212)^2 + (x305 - x352)^2) + 1 / sqrt((x25 - x73)^2 + (x165 - x213)^
    2 + (x305 - x353)^2) + 1 / sqrt((x25 - x74)^2 + (x165 - x214)^2 + (x305 -
    x354)^2) + 1 / sqrt((x25 - x75)^2 + (x165 - x215)^2 + (x305 - x355)^2) + 1
    / sqrt((x25 - x76)^2 + (x165 - x216)^2 + (x305 - x356)^2) + 1 / sqrt((x25
    - x77)^2 + (x165 - x217)^2 + (x305 - x357)^2) + 1 / sqrt((x25 - x78)^2 + (
    x165 - x218)^2 + (x305 - x358)^2) + 1 / sqrt((x25 - x79)^2 + (x165 - x219)^
    2 + (x305 - x359)^2) + 1 / sqrt((x25 - x80)^2 + (x165 - x220)^2 + (x305 -
    x360)^2) + 1 / sqrt((x25 - x81)^2 + (x165 - x221)^2 + (x305 - x361)^2) + 1
    / sqrt((x25 - x82)^2 + (x165 - x222)^2 + (x305 - x362)^2) + 1 / sqrt((x25
    - x83)^2 + (x165 - x223)^2 + (x305 - x363)^2) + 1 / sqrt((x25 - x84)^2 + (
    x165 - x224)^2 + (x305 - x364)^2) + 1 / sqrt((x25 - x85)^2 + (x165 - x225)^
    2 + (x305 - x365)^2) + 1 / sqrt((x25 - x86)^2 + (x165 - x226)^2 + (x305 -
    x366)^2) + 1 / sqrt((x25 - x87)^2 + (x165 - x227)^2 + (x305 - x367)^2) + 1
    / sqrt((x25 - x88)^2 + (x165 - x228)^2 + (x305 - x368)^2) + 1 / sqrt((x25
    - x89)^2 + (x165 - x229)^2 + (x305 - x369)^2) + 1 / sqrt((x25 - x90)^2 + (
    x165 - x230)^2 + (x305 - x370)^2) + 1 / sqrt((x25 - x91)^2 + (x165 - x231)^
    2 + (x305 - x371)^2) + 1 / sqrt((x25 - x92)^2 + (x165 - x232)^2 + (x305 -
    x372)^2) + 1 / sqrt((x25 - x93)^2 + (x165 - x233)^2 + (x305 - x373)^2) + 1
    / sqrt((x25 - x94)^2 + (x165 - x234)^2 + (x305 - x374)^2) + 1 / sqrt((x25
    - x95)^2 + (x165 - x235)^2 + (x305 - x375)^2) + 1 / sqrt((x25 - x96)^2 + (
    x165 - x236)^2 + (x305 - x376)^2) + 1 / sqrt((x25 - x97)^2 + (x165 - x237)^
    2 + (x305 - x377)^2) + 1 / sqrt((x25 - x98)^2 + (x165 - x238)^2 + (x305 -
    x378)^2) + 1 / sqrt((x25 - x99)^2 + (x165 - x239)^2 + (x305 - x379)^2) + 1
    / sqrt((x25 - x100)^2 + (x165 - x240)^2 + (x305 - x380)^2) + 1 / sqrt((x25
    - x101)^2 + (x165 - x241)^2 + (x305 - x381)^2) + 1 / sqrt((x25 - x102)^2
    + (x165 - x242)^2 + (x305 - x382)^2) + 1 / sqrt((x25 - x103)^2 + (x165 -
    x243)^2 + (x305 - x383)^2) + 1 / sqrt((x25 - x104)^2 + (x165 - x244)^2 + (
    x305 - x384)^2) + 1 / sqrt((x25 - x105)^2 + (x165 - x245)^2 + (x305 - x385)
    ^2) + 1 / sqrt((x25 - x106)^2 + (x165 - x246)^2 + (x305 - x386)^2) + 1 /
    sqrt((x25 - x107)^2 + (x165 - x247)^2 + (x305 - x387)^2) + 1 / sqrt((x25 -
    x108)^2 + (x165 - x248)^2 + (x305 - x388)^2) + 1 / sqrt((x25 - x109)^2 + (
    x165 - x249)^2 + (x305 - x389)^2) + 1 / sqrt((x25 - x110)^2 + (x165 - x250)
    ^2 + (x305 - x390)^2) + 1 / sqrt((x25 - x111)^2 + (x165 - x251)^2 + (x305
    - x391)^2) + 1 / sqrt((x25 - x112)^2 + (x165 - x252)^2 + (x305 - x392)^2)
    + 1 / sqrt((x25 - x113)^2 + (x165 - x253)^2 + (x305 - x393)^2) + 1 / sqrt(
    (x25 - x114)^2 + (x165 - x254)^2 + (x305 - x394)^2) + 1 / sqrt((x25 - x115)
    ^2 + (x165 - x255)^2 + (x305 - x395)^2) + 1 / sqrt((x25 - x116)^2 + (x165
    - x256)^2 + (x305 - x396)^2) + 1 / sqrt((x25 - x117)^2 + (x165 - x257)^2
    + (x305 - x397)^2) + 1 / sqrt((x25 - x118)^2 + (x165 - x258)^2 + (x305 -
    x398)^2) + 1 / sqrt((x25 - x119)^2 + (x165 - x259)^2 + (x305 - x399)^2) + 1
    / sqrt((x25 - x120)^2 + (x165 - x260)^2 + (x305 - x400)^2) + 1 / sqrt((x25
    - x121)^2 + (x165 - x261)^2 + (x305 - x401)^2) + 1 / sqrt((x25 - x122)^2
    + (x165 - x262)^2 + (x305 - x402)^2) + 1 / sqrt((x25 - x123)^2 + (x165 -
    x263)^2 + (x305 - x403)^2) + 1 / sqrt((x25 - x124)^2 + (x165 - x264)^2 + (
    x305 - x404)^2) + 1 / sqrt((x25 - x125)^2 + (x165 - x265)^2 + (x305 - x405)
    ^2) + 1 / sqrt((x25 - x126)^2 + (x165 - x266)^2 + (x305 - x406)^2) + 1 /
    sqrt((x25 - x127)^2 + (x165 - x267)^2 + (x305 - x407)^2) + 1 / sqrt((x25 -
    x128)^2 + (x165 - x268)^2 + (x305 - x408)^2) + 1 / sqrt((x25 - x129)^2 + (
    x165 - x269)^2 + (x305 - x409)^2) + 1 / sqrt((x25 - x130)^2 + (x165 - x270)
    ^2 + (x305 - x410)^2) + 1 / sqrt((x25 - x131)^2 + (x165 - x271)^2 + (x305
    - x411)^2) + 1 / sqrt((x25 - x132)^2 + (x165 - x272)^2 + (x305 - x412)^2)
    + 1 / sqrt((x25 - x133)^2 + (x165 - x273)^2 + (x305 - x413)^2) + 1 / sqrt(
    (x25 - x134)^2 + (x165 - x274)^2 + (x305 - x414)^2) + 1 / sqrt((x25 - x135)
    ^2 + (x165 - x275)^2 + (x305 - x415)^2) + 1 / sqrt((x25 - x136)^2 + (x165
    - x276)^2 + (x305 - x416)^2) + 1 / sqrt((x25 - x137)^2 + (x165 - x277)^2
    + (x305 - x417)^2) + 1 / sqrt((x25 - x138)^2 + (x165 - x278)^2 + (x305 -
    x418)^2) + 1 / sqrt((x25 - x139)^2 + (x165 - x279)^2 + (x305 - x419)^2) + 1
    / sqrt((x25 - x140)^2 + (x165 - x280)^2 + (x305 - x420)^2) + 1 / sqrt((x26
    - x27)^2 + (x166 - x167)^2 + (x306 - x307)^2) + 1 / sqrt((x26 - x28)^2 + (
    x166 - x168)^2 + (x306 - x308)^2) + 1 / sqrt((x26 - x29)^2 + (x166 - x169)^
    2 + (x306 - x309)^2) + 1 / sqrt((x26 - x30)^2 + (x166 - x170)^2 + (x306 -
    x310)^2) + 1 / sqrt((x26 - x31)^2 + (x166 - x171)^2 + (x306 - x311)^2) + 1
    / sqrt((x26 - x32)^2 + (x166 - x172)^2 + (x306 - x312)^2) + 1 / sqrt((x26
    - x33)^2 + (x166 - x173)^2 + (x306 - x313)^2) + 1 / sqrt((x26 - x34)^2 + (
    x166 - x174)^2 + (x306 - x314)^2) + 1 / sqrt((x26 - x35)^2 + (x166 - x175)^
    2 + (x306 - x315)^2) + 1 / sqrt((x26 - x36)^2 + (x166 - x176)^2 + (x306 -
    x316)^2) + 1 / sqrt((x26 - x37)^2 + (x166 - x177)^2 + (x306 - x317)^2) + 1
    / sqrt((x26 - x38)^2 + (x166 - x178)^2 + (x306 - x318)^2) + 1 / sqrt((x26
    - x39)^2 + (x166 - x179)^2 + (x306 - x319)^2) + 1 / sqrt((x26 - x40)^2 + (
    x166 - x180)^2 + (x306 - x320)^2) + 1 / sqrt((x26 - x41)^2 + (x166 - x181)^
    2 + (x306 - x321)^2) + 1 / sqrt((x26 - x42)^2 + (x166 - x182)^2 + (x306 -
    x322)^2) + 1 / sqrt((x26 - x43)^2 + (x166 - x183)^2 + (x306 - x323)^2) + 1
    / sqrt((x26 - x44)^2 + (x166 - x184)^2 + (x306 - x324)^2) + 1 / sqrt((x26
    - x45)^2 + (x166 - x185)^2 + (x306 - x325)^2) + 1 / sqrt((x26 - x46)^2 + (
    x166 - x186)^2 + (x306 - x326)^2) + 1 / sqrt((x26 - x47)^2 + (x166 - x187)^
    2 + (x306 - x327)^2) + 1 / sqrt((x26 - x48)^2 + (x166 - x188)^2 + (x306 -
    x328)^2) + 1 / sqrt((x26 - x49)^2 + (x166 - x189)^2 + (x306 - x329)^2) + 1
    / sqrt((x26 - x50)^2 + (x166 - x190)^2 + (x306 - x330)^2) + 1 / sqrt((x26
    - x51)^2 + (x166 - x191)^2 + (x306 - x331)^2) + 1 / sqrt((x26 - x52)^2 + (
    x166 - x192)^2 + (x306 - x332)^2) + 1 / sqrt((x26 - x53)^2 + (x166 - x193)^
    2 + (x306 - x333)^2) + 1 / sqrt((x26 - x54)^2 + (x166 - x194)^2 + (x306 -
    x334)^2) + 1 / sqrt((x26 - x55)^2 + (x166 - x195)^2 + (x306 - x335)^2) + 1
    / sqrt((x26 - x56)^2 + (x166 - x196)^2 + (x306 - x336)^2) + 1 / sqrt((x26
    - x57)^2 + (x166 - x197)^2 + (x306 - x337)^2) + 1 / sqrt((x26 - x58)^2 + (
    x166 - x198)^2 + (x306 - x338)^2) + 1 / sqrt((x26 - x59)^2 + (x166 - x199)^
    2 + (x306 - x339)^2) + 1 / sqrt((x26 - x60)^2 + (x166 - x200)^2 + (x306 -
    x340)^2) + 1 / sqrt((x26 - x61)^2 + (x166 - x201)^2 + (x306 - x341)^2) + 1
    / sqrt((x26 - x62)^2 + (x166 - x202)^2 + (x306 - x342)^2) + 1 / sqrt((x26
    - x63)^2 + (x166 - x203)^2 + (x306 - x343)^2) + 1 / sqrt((x26 - x64)^2 + (
    x166 - x204)^2 + (x306 - x344)^2) + 1 / sqrt((x26 - x65)^2 + (x166 - x205)^
    2 + (x306 - x345)^2) + 1 / sqrt((x26 - x66)^2 + (x166 - x206)^2 + (x306 -
    x346)^2) + 1 / sqrt((x26 - x67)^2 + (x166 - x207)^2 + (x306 - x347)^2) + 1
    / sqrt((x26 - x68)^2 + (x166 - x208)^2 + (x306 - x348)^2) + 1 / sqrt((x26
    - x69)^2 + (x166 - x209)^2 + (x306 - x349)^2) + 1 / sqrt((x26 - x70)^2 + (
    x166 - x210)^2 + (x306 - x350)^2) + 1 / sqrt((x26 - x71)^2 + (x166 - x211)^
    2 + (x306 - x351)^2) + 1 / sqrt((x26 - x72)^2 + (x166 - x212)^2 + (x306 -
    x352)^2) + 1 / sqrt((x26 - x73)^2 + (x166 - x213)^2 + (x306 - x353)^2) + 1
    / sqrt((x26 - x74)^2 + (x166 - x214)^2 + (x306 - x354)^2) + 1 / sqrt((x26
    - x75)^2 + (x166 - x215)^2 + (x306 - x355)^2) + 1 / sqrt((x26 - x76)^2 + (
    x166 - x216)^2 + (x306 - x356)^2) + 1 / sqrt((x26 - x77)^2 + (x166 - x217)^
    2 + (x306 - x357)^2) + 1 / sqrt((x26 - x78)^2 + (x166 - x218)^2 + (x306 -
    x358)^2) + 1 / sqrt((x26 - x79)^2 + (x166 - x219)^2 + (x306 - x359)^2) + 1
    / sqrt((x26 - x80)^2 + (x166 - x220)^2 + (x306 - x360)^2) + 1 / sqrt((x26
    - x81)^2 + (x166 - x221)^2 + (x306 - x361)^2) + 1 / sqrt((x26 - x82)^2 + (
    x166 - x222)^2 + (x306 - x362)^2) + 1 / sqrt((x26 - x83)^2 + (x166 - x223)^
    2 + (x306 - x363)^2) + 1 / sqrt((x26 - x84)^2 + (x166 - x224)^2 + (x306 -
    x364)^2) + 1 / sqrt((x26 - x85)^2 + (x166 - x225)^2 + (x306 - x365)^2) + 1
    / sqrt((x26 - x86)^2 + (x166 - x226)^2 + (x306 - x366)^2) + 1 / sqrt((x26
    - x87)^2 + (x166 - x227)^2 + (x306 - x367)^2) + 1 / sqrt((x26 - x88)^2 + (
    x166 - x228)^2 + (x306 - x368)^2) + 1 / sqrt((x26 - x89)^2 + (x166 - x229)^
    2 + (x306 - x369)^2) + 1 / sqrt((x26 - x90)^2 + (x166 - x230)^2 + (x306 -
    x370)^2) + 1 / sqrt((x26 - x91)^2 + (x166 - x231)^2 + (x306 - x371)^2) + 1
    / sqrt((x26 - x92)^2 + (x166 - x232)^2 + (x306 - x372)^2) + 1 / sqrt((x26
    - x93)^2 + (x166 - x233)^2 + (x306 - x373)^2) + 1 / sqrt((x26 - x94)^2 + (
    x166 - x234)^2 + (x306 - x374)^2) + 1 / sqrt((x26 - x95)^2 + (x166 - x235)^
    2 + (x306 - x375)^2) + 1 / sqrt((x26 - x96)^2 + (x166 - x236)^2 + (x306 -
    x376)^2) + 1 / sqrt((x26 - x97)^2 + (x166 - x237)^2 + (x306 - x377)^2) + 1
    / sqrt((x26 - x98)^2 + (x166 - x238)^2 + (x306 - x378)^2) + 1 / sqrt((x26
    - x99)^2 + (x166 - x239)^2 + (x306 - x379)^2) + 1 / sqrt((x26 - x100)^2 +
    (x166 - x240)^2 + (x306 - x380)^2) + 1 / sqrt((x26 - x101)^2 + (x166 - x241)
    ^2 + (x306 - x381)^2) + 1 / sqrt((x26 - x102)^2 + (x166 - x242)^2 + (x306
    - x382)^2) + 1 / sqrt((x26 - x103)^2 + (x166 - x243)^2 + (x306 - x383)^2)
    + 1 / sqrt((x26 - x104)^2 + (x166 - x244)^2 + (x306 - x384)^2) + 1 / sqrt(
    (x26 - x105)^2 + (x166 - x245)^2 + (x306 - x385)^2) + 1 / sqrt((x26 - x106)
    ^2 + (x166 - x246)^2 + (x306 - x386)^2) + 1 / sqrt((x26 - x107)^2 + (x166
    - x247)^2 + (x306 - x387)^2) + 1 / sqrt((x26 - x108)^2 + (x166 - x248)^2
    + (x306 - x388)^2) + 1 / sqrt((x26 - x109)^2 + (x166 - x249)^2 + (x306 -
    x389)^2) + 1 / sqrt((x26 - x110)^2 + (x166 - x250)^2 + (x306 - x390)^2) + 1
    / sqrt((x26 - x111)^2 + (x166 - x251)^2 + (x306 - x391)^2) + 1 / sqrt((x26
    - x112)^2 + (x166 - x252)^2 + (x306 - x392)^2) + 1 / sqrt((x26 - x113)^2
    + (x166 - x253)^2 + (x306 - x393)^2) + 1 / sqrt((x26 - x114)^2 + (x166 -
    x254)^2 + (x306 - x394)^2) + 1 / sqrt((x26 - x115)^2 + (x166 - x255)^2 + (
    x306 - x395)^2) + 1 / sqrt((x26 - x116)^2 + (x166 - x256)^2 + (x306 - x396)
    ^2) + 1 / sqrt((x26 - x117)^2 + (x166 - x257)^2 + (x306 - x397)^2) + 1 /
    sqrt((x26 - x118)^2 + (x166 - x258)^2 + (x306 - x398)^2) + 1 / sqrt((x26 -
    x119)^2 + (x166 - x259)^2 + (x306 - x399)^2) + 1 / sqrt((x26 - x120)^2 + (
    x166 - x260)^2 + (x306 - x400)^2) + 1 / sqrt((x26 - x121)^2 + (x166 - x261)
    ^2 + (x306 - x401)^2) + 1 / sqrt((x26 - x122)^2 + (x166 - x262)^2 + (x306
    - x402)^2) + 1 / sqrt((x26 - x123)^2 + (x166 - x263)^2 + (x306 - x403)^2)
    + 1 / sqrt((x26 - x124)^2 + (x166 - x264)^2 + (x306 - x404)^2) + 1 / sqrt(
    (x26 - x125)^2 + (x166 - x265)^2 + (x306 - x405)^2) + 1 / sqrt((x26 - x126)
    ^2 + (x166 - x266)^2 + (x306 - x406)^2) + 1 / sqrt((x26 - x127)^2 + (x166
    - x267)^2 + (x306 - x407)^2) + 1 / sqrt((x26 - x128)^2 + (x166 - x268)^2
    + (x306 - x408)^2) + 1 / sqrt((x26 - x129)^2 + (x166 - x269)^2 + (x306 -
    x409)^2) + 1 / sqrt((x26 - x130)^2 + (x166 - x270)^2 + (x306 - x410)^2) + 1
    / sqrt((x26 - x131)^2 + (x166 - x271)^2 + (x306 - x411)^2) + 1 / sqrt((x26
    - x132)^2 + (x166 - x272)^2 + (x306 - x412)^2) + 1 / sqrt((x26 - x133)^2
    + (x166 - x273)^2 + (x306 - x413)^2) + 1 / sqrt((x26 - x134)^2 + (x166 -
    x274)^2 + (x306 - x414)^2) + 1 / sqrt((x26 - x135)^2 + (x166 - x275)^2 + (
    x306 - x415)^2) + 1 / sqrt((x26 - x136)^2 + (x166 - x276)^2 + (x306 - x416)
    ^2) + 1 / sqrt((x26 - x137)^2 + (x166 - x277)^2 + (x306 - x417)^2) + 1 /
    sqrt((x26 - x138)^2 + (x166 - x278)^2 + (x306 - x418)^2) + 1 / sqrt((x26 -
    x139)^2 + (x166 - x279)^2 + (x306 - x419)^2) + 1 / sqrt((x26 - x140)^2 + (
    x166 - x280)^2 + (x306 - x420)^2) + 1 / sqrt((x27 - x28)^2 + (x167 - x168)^
    2 + (x307 - x308)^2) + 1 / sqrt((x27 - x29)^2 + (x167 - x169)^2 + (x307 -
    x309)^2) + 1 / sqrt((x27 - x30)^2 + (x167 - x170)^2 + (x307 - x310)^2) + 1
    / sqrt((x27 - x31)^2 + (x167 - x171)^2 + (x307 - x311)^2) + 1 / sqrt((x27
    - x32)^2 + (x167 - x172)^2 + (x307 - x312)^2) + 1 / sqrt((x27 - x33)^2 + (
    x167 - x173)^2 + (x307 - x313)^2) + 1 / sqrt((x27 - x34)^2 + (x167 - x174)^
    2 + (x307 - x314)^2) + 1 / sqrt((x27 - x35)^2 + (x167 - x175)^2 + (x307 -
    x315)^2) + 1 / sqrt((x27 - x36)^2 + (x167 - x176)^2 + (x307 - x316)^2) + 1
    / sqrt((x27 - x37)^2 + (x167 - x177)^2 + (x307 - x317)^2) + 1 / sqrt((x27
    - x38)^2 + (x167 - x178)^2 + (x307 - x318)^2) + 1 / sqrt((x27 - x39)^2 + (
    x167 - x179)^2 + (x307 - x319)^2) + 1 / sqrt((x27 - x40)^2 + (x167 - x180)^
    2 + (x307 - x320)^2) + 1 / sqrt((x27 - x41)^2 + (x167 - x181)^2 + (x307 -
    x321)^2) + 1 / sqrt((x27 - x42)^2 + (x167 - x182)^2 + (x307 - x322)^2) + 1
    / sqrt((x27 - x43)^2 + (x167 - x183)^2 + (x307 - x323)^2) + 1 / sqrt((x27
    - x44)^2 + (x167 - x184)^2 + (x307 - x324)^2) + 1 / sqrt((x27 - x45)^2 + (
    x167 - x185)^2 + (x307 - x325)^2) + 1 / sqrt((x27 - x46)^2 + (x167 - x186)^
    2 + (x307 - x326)^2) + 1 / sqrt((x27 - x47)^2 + (x167 - x187)^2 + (x307 -
    x327)^2) + 1 / sqrt((x27 - x48)^2 + (x167 - x188)^2 + (x307 - x328)^2) + 1
    / sqrt((x27 - x49)^2 + (x167 - x189)^2 + (x307 - x329)^2) + 1 / sqrt((x27
    - x50)^2 + (x167 - x190)^2 + (x307 - x330)^2) + 1 / sqrt((x27 - x51)^2 + (
    x167 - x191)^2 + (x307 - x331)^2) + 1 / sqrt((x27 - x52)^2 + (x167 - x192)^
    2 + (x307 - x332)^2) + 1 / sqrt((x27 - x53)^2 + (x167 - x193)^2 + (x307 -
    x333)^2) + 1 / sqrt((x27 - x54)^2 + (x167 - x194)^2 + (x307 - x334)^2) + 1
    / sqrt((x27 - x55)^2 + (x167 - x195)^2 + (x307 - x335)^2) + 1 / sqrt((x27
    - x56)^2 + (x167 - x196)^2 + (x307 - x336)^2) + 1 / sqrt((x27 - x57)^2 + (
    x167 - x197)^2 + (x307 - x337)^2) + 1 / sqrt((x27 - x58)^2 + (x167 - x198)^
    2 + (x307 - x338)^2) + 1 / sqrt((x27 - x59)^2 + (x167 - x199)^2 + (x307 -
    x339)^2) + 1 / sqrt((x27 - x60)^2 + (x167 - x200)^2 + (x307 - x340)^2) + 1
    / sqrt((x27 - x61)^2 + (x167 - x201)^2 + (x307 - x341)^2) + 1 / sqrt((x27
    - x62)^2 + (x167 - x202)^2 + (x307 - x342)^2) + 1 / sqrt((x27 - x63)^2 + (
    x167 - x203)^2 + (x307 - x343)^2) + 1 / sqrt((x27 - x64)^2 + (x167 - x204)^
    2 + (x307 - x344)^2) + 1 / sqrt((x27 - x65)^2 + (x167 - x205)^2 + (x307 -
    x345)^2) + 1 / sqrt((x27 - x66)^2 + (x167 - x206)^2 + (x307 - x346)^2) + 1
    / sqrt((x27 - x67)^2 + (x167 - x207)^2 + (x307 - x347)^2) + 1 / sqrt((x27
    - x68)^2 + (x167 - x208)^2 + (x307 - x348)^2) + 1 / sqrt((x27 - x69)^2 + (
    x167 - x209)^2 + (x307 - x349)^2) + 1 / sqrt((x27 - x70)^2 + (x167 - x210)^
    2 + (x307 - x350)^2) + 1 / sqrt((x27 - x71)^2 + (x167 - x211)^2 + (x307 -
    x351)^2) + 1 / sqrt((x27 - x72)^2 + (x167 - x212)^2 + (x307 - x352)^2) + 1
    / sqrt((x27 - x73)^2 + (x167 - x213)^2 + (x307 - x353)^2) + 1 / sqrt((x27
    - x74)^2 + (x167 - x214)^2 + (x307 - x354)^2) + 1 / sqrt((x27 - x75)^2 + (
    x167 - x215)^2 + (x307 - x355)^2) + 1 / sqrt((x27 - x76)^2 + (x167 - x216)^
    2 + (x307 - x356)^2) + 1 / sqrt((x27 - x77)^2 + (x167 - x217)^2 + (x307 -
    x357)^2) + 1 / sqrt((x27 - x78)^2 + (x167 - x218)^2 + (x307 - x358)^2) + 1
    / sqrt((x27 - x79)^2 + (x167 - x219)^2 + (x307 - x359)^2) + 1 / sqrt((x27
    - x80)^2 + (x167 - x220)^2 + (x307 - x360)^2) + 1 / sqrt((x27 - x81)^2 + (
    x167 - x221)^2 + (x307 - x361)^2) + 1 / sqrt((x27 - x82)^2 + (x167 - x222)^
    2 + (x307 - x362)^2) + 1 / sqrt((x27 - x83)^2 + (x167 - x223)^2 + (x307 -
    x363)^2) + 1 / sqrt((x27 - x84)^2 + (x167 - x224)^2 + (x307 - x364)^2) + 1
    / sqrt((x27 - x85)^2 + (x167 - x225)^2 + (x307 - x365)^2) + 1 / sqrt((x27
    - x86)^2 + (x167 - x226)^2 + (x307 - x366)^2) + 1 / sqrt((x27 - x87)^2 + (
    x167 - x227)^2 + (x307 - x367)^2) + 1 / sqrt((x27 - x88)^2 + (x167 - x228)^
    2 + (x307 - x368)^2) + 1 / sqrt((x27 - x89)^2 + (x167 - x229)^2 + (x307 -
    x369)^2) + 1 / sqrt((x27 - x90)^2 + (x167 - x230)^2 + (x307 - x370)^2) + 1
    / sqrt((x27 - x91)^2 + (x167 - x231)^2 + (x307 - x371)^2) + 1 / sqrt((x27
    - x92)^2 + (x167 - x232)^2 + (x307 - x372)^2) + 1 / sqrt((x27 - x93)^2 + (
    x167 - x233)^2 + (x307 - x373)^2) + 1 / sqrt((x27 - x94)^2 + (x167 - x234)^
    2 + (x307 - x374)^2) + 1 / sqrt((x27 - x95)^2 + (x167 - x235)^2 + (x307 -
    x375)^2) + 1 / sqrt((x27 - x96)^2 + (x167 - x236)^2 + (x307 - x376)^2) + 1
    / sqrt((x27 - x97)^2 + (x167 - x237)^2 + (x307 - x377)^2) + 1 / sqrt((x27
    - x98)^2 + (x167 - x238)^2 + (x307 - x378)^2) + 1 / sqrt((x27 - x99)^2 + (
    x167 - x239)^2 + (x307 - x379)^2) + 1 / sqrt((x27 - x100)^2 + (x167 - x240)
    ^2 + (x307 - x380)^2) + 1 / sqrt((x27 - x101)^2 + (x167 - x241)^2 + (x307
    - x381)^2) + 1 / sqrt((x27 - x102)^2 + (x167 - x242)^2 + (x307 - x382)^2)
    + 1 / sqrt((x27 - x103)^2 + (x167 - x243)^2 + (x307 - x383)^2) + 1 / sqrt(
    (x27 - x104)^2 + (x167 - x244)^2 + (x307 - x384)^2) + 1 / sqrt((x27 - x105)
    ^2 + (x167 - x245)^2 + (x307 - x385)^2) + 1 / sqrt((x27 - x106)^2 + (x167
    - x246)^2 + (x307 - x386)^2) + 1 / sqrt((x27 - x107)^2 + (x167 - x247)^2
    + (x307 - x387)^2) + 1 / sqrt((x27 - x108)^2 + (x167 - x248)^2 + (x307 -
    x388)^2) + 1 / sqrt((x27 - x109)^2 + (x167 - x249)^2 + (x307 - x389)^2) + 1
    / sqrt((x27 - x110)^2 + (x167 - x250)^2 + (x307 - x390)^2) + 1 / sqrt((x27
    - x111)^2 + (x167 - x251)^2 + (x307 - x391)^2) + 1 / sqrt((x27 - x112)^2
    + (x167 - x252)^2 + (x307 - x392)^2) + 1 / sqrt((x27 - x113)^2 + (x167 -
    x253)^2 + (x307 - x393)^2) + 1 / sqrt((x27 - x114)^2 + (x167 - x254)^2 + (
    x307 - x394)^2) + 1 / sqrt((x27 - x115)^2 + (x167 - x255)^2 + (x307 - x395)
    ^2) + 1 / sqrt((x27 - x116)^2 + (x167 - x256)^2 + (x307 - x396)^2) + 1 /
    sqrt((x27 - x117)^2 + (x167 - x257)^2 + (x307 - x397)^2) + 1 / sqrt((x27 -
    x118)^2 + (x167 - x258)^2 + (x307 - x398)^2) + 1 / sqrt((x27 - x119)^2 + (
    x167 - x259)^2 + (x307 - x399)^2) + 1 / sqrt((x27 - x120)^2 + (x167 - x260)
    ^2 + (x307 - x400)^2) + 1 / sqrt((x27 - x121)^2 + (x167 - x261)^2 + (x307
    - x401)^2) + 1 / sqrt((x27 - x122)^2 + (x167 - x262)^2 + (x307 - x402)^2)
    + 1 / sqrt((x27 - x123)^2 + (x167 - x263)^2 + (x307 - x403)^2) + 1 / sqrt(
    (x27 - x124)^2 + (x167 - x264)^2 + (x307 - x404)^2) + 1 / sqrt((x27 - x125)
    ^2 + (x167 - x265)^2 + (x307 - x405)^2) + 1 / sqrt((x27 - x126)^2 + (x167
    - x266)^2 + (x307 - x406)^2) + 1 / sqrt((x27 - x127)^2 + (x167 - x267)^2
    + (x307 - x407)^2) + 1 / sqrt((x27 - x128)^2 + (x167 - x268)^2 + (x307 -
    x408)^2) + 1 / sqrt((x27 - x129)^2 + (x167 - x269)^2 + (x307 - x409)^2) + 1
    / sqrt((x27 - x130)^2 + (x167 - x270)^2 + (x307 - x410)^2) + 1 / sqrt((x27
    - x131)^2 + (x167 - x271)^2 + (x307 - x411)^2) + 1 / sqrt((x27 - x132)^2
    + (x167 - x272)^2 + (x307 - x412)^2) + 1 / sqrt((x27 - x133)^2 + (x167 -
    x273)^2 + (x307 - x413)^2) + 1 / sqrt((x27 - x134)^2 + (x167 - x274)^2 + (
    x307 - x414)^2) + 1 / sqrt((x27 - x135)^2 + (x167 - x275)^2 + (x307 - x415)
    ^2) + 1 / sqrt((x27 - x136)^2 + (x167 - x276)^2 + (x307 - x416)^2) + 1 /
    sqrt((x27 - x137)^2 + (x167 - x277)^2 + (x307 - x417)^2) + 1 / sqrt((x27 -
    x138)^2 + (x167 - x278)^2 + (x307 - x418)^2) + 1 / sqrt((x27 - x139)^2 + (
    x167 - x279)^2 + (x307 - x419)^2) + 1 / sqrt((x27 - x140)^2 + (x167 - x280)
    ^2 + (x307 - x420)^2) + 1 / sqrt((x28 - x29)^2 + (x168 - x169)^2 + (x308 -
    x309)^2) + 1 / sqrt((x28 - x30)^2 + (x168 - x170)^2 + (x308 - x310)^2) + 1
    / sqrt((x28 - x31)^2 + (x168 - x171)^2 + (x308 - x311)^2) + 1 / sqrt((x28
    - x32)^2 + (x168 - x172)^2 + (x308 - x312)^2) + 1 / sqrt((x28 - x33)^2 + (
    x168 - x173)^2 + (x308 - x313)^2) + 1 / sqrt((x28 - x34)^2 + (x168 - x174)^
    2 + (x308 - x314)^2) + 1 / sqrt((x28 - x35)^2 + (x168 - x175)^2 + (x308 -
    x315)^2) + 1 / sqrt((x28 - x36)^2 + (x168 - x176)^2 + (x308 - x316)^2) + 1
    / sqrt((x28 - x37)^2 + (x168 - x177)^2 + (x308 - x317)^2) + 1 / sqrt((x28
    - x38)^2 + (x168 - x178)^2 + (x308 - x318)^2) + 1 / sqrt((x28 - x39)^2 + (
    x168 - x179)^2 + (x308 - x319)^2) + 1 / sqrt((x28 - x40)^2 + (x168 - x180)^
    2 + (x308 - x320)^2) + 1 / sqrt((x28 - x41)^2 + (x168 - x181)^2 + (x308 -
    x321)^2) + 1 / sqrt((x28 - x42)^2 + (x168 - x182)^2 + (x308 - x322)^2) + 1
    / sqrt((x28 - x43)^2 + (x168 - x183)^2 + (x308 - x323)^2) + 1 / sqrt((x28
    - x44)^2 + (x168 - x184)^2 + (x308 - x324)^2) + 1 / sqrt((x28 - x45)^2 + (
    x168 - x185)^2 + (x308 - x325)^2) + 1 / sqrt((x28 - x46)^2 + (x168 - x186)^
    2 + (x308 - x326)^2) + 1 / sqrt((x28 - x47)^2 + (x168 - x187)^2 + (x308 -
    x327)^2) + 1 / sqrt((x28 - x48)^2 + (x168 - x188)^2 + (x308 - x328)^2) + 1
    / sqrt((x28 - x49)^2 + (x168 - x189)^2 + (x308 - x329)^2) + 1 / sqrt((x28
    - x50)^2 + (x168 - x190)^2 + (x308 - x330)^2) + 1 / sqrt((x28 - x51)^2 + (
    x168 - x191)^2 + (x308 - x331)^2) + 1 / sqrt((x28 - x52)^2 + (x168 - x192)^
    2 + (x308 - x332)^2) + 1 / sqrt((x28 - x53)^2 + (x168 - x193)^2 + (x308 -
    x333)^2) + 1 / sqrt((x28 - x54)^2 + (x168 - x194)^2 + (x308 - x334)^2) + 1
    / sqrt((x28 - x55)^2 + (x168 - x195)^2 + (x308 - x335)^2) + 1 / sqrt((x28
    - x56)^2 + (x168 - x196)^2 + (x308 - x336)^2) + 1 / sqrt((x28 - x57)^2 + (
    x168 - x197)^2 + (x308 - x337)^2) + 1 / sqrt((x28 - x58)^2 + (x168 - x198)^
    2 + (x308 - x338)^2) + 1 / sqrt((x28 - x59)^2 + (x168 - x199)^2 + (x308 -
    x339)^2) + 1 / sqrt((x28 - x60)^2 + (x168 - x200)^2 + (x308 - x340)^2) + 1
    / sqrt((x28 - x61)^2 + (x168 - x201)^2 + (x308 - x341)^2) + 1 / sqrt((x28
    - x62)^2 + (x168 - x202)^2 + (x308 - x342)^2) + 1 / sqrt((x28 - x63)^2 + (
    x168 - x203)^2 + (x308 - x343)^2) + 1 / sqrt((x28 - x64)^2 + (x168 - x204)^
    2 + (x308 - x344)^2) + 1 / sqrt((x28 - x65)^2 + (x168 - x205)^2 + (x308 -
    x345)^2) + 1 / sqrt((x28 - x66)^2 + (x168 - x206)^2 + (x308 - x346)^2) + 1
    / sqrt((x28 - x67)^2 + (x168 - x207)^2 + (x308 - x347)^2) + 1 / sqrt((x28
    - x68)^2 + (x168 - x208)^2 + (x308 - x348)^2) + 1 / sqrt((x28 - x69)^2 + (
    x168 - x209)^2 + (x308 - x349)^2) + 1 / sqrt((x28 - x70)^2 + (x168 - x210)^
    2 + (x308 - x350)^2) + 1 / sqrt((x28 - x71)^2 + (x168 - x211)^2 + (x308 -
    x351)^2) + 1 / sqrt((x28 - x72)^2 + (x168 - x212)^2 + (x308 - x352)^2) + 1
    / sqrt((x28 - x73)^2 + (x168 - x213)^2 + (x308 - x353)^2) + 1 / sqrt((x28
    - x74)^2 + (x168 - x214)^2 + (x308 - x354)^2) + 1 / sqrt((x28 - x75)^2 + (
    x168 - x215)^2 + (x308 - x355)^2) + 1 / sqrt((x28 - x76)^2 + (x168 - x216)^
    2 + (x308 - x356)^2) + 1 / sqrt((x28 - x77)^2 + (x168 - x217)^2 + (x308 -
    x357)^2) + 1 / sqrt((x28 - x78)^2 + (x168 - x218)^2 + (x308 - x358)^2) + 1
    / sqrt((x28 - x79)^2 + (x168 - x219)^2 + (x308 - x359)^2) + 1 / sqrt((x28
    - x80)^2 + (x168 - x220)^2 + (x308 - x360)^2) + 1 / sqrt((x28 - x81)^2 + (
    x168 - x221)^2 + (x308 - x361)^2) + 1 / sqrt((x28 - x82)^2 + (x168 - x222)^
    2 + (x308 - x362)^2) + 1 / sqrt((x28 - x83)^2 + (x168 - x223)^2 + (x308 -
    x363)^2) + 1 / sqrt((x28 - x84)^2 + (x168 - x224)^2 + (x308 - x364)^2) + 1
    / sqrt((x28 - x85)^2 + (x168 - x225)^2 + (x308 - x365)^2) + 1 / sqrt((x28
    - x86)^2 + (x168 - x226)^2 + (x308 - x366)^2) + 1 / sqrt((x28 - x87)^2 + (
    x168 - x227)^2 + (x308 - x367)^2) + 1 / sqrt((x28 - x88)^2 + (x168 - x228)^
    2 + (x308 - x368)^2) + 1 / sqrt((x28 - x89)^2 + (x168 - x229)^2 + (x308 -
    x369)^2) + 1 / sqrt((x28 - x90)^2 + (x168 - x230)^2 + (x308 - x370)^2) + 1
    / sqrt((x28 - x91)^2 + (x168 - x231)^2 + (x308 - x371)^2) + 1 / sqrt((x28
    - x92)^2 + (x168 - x232)^2 + (x308 - x372)^2) + 1 / sqrt((x28 - x93)^2 + (
    x168 - x233)^2 + (x308 - x373)^2) + 1 / sqrt((x28 - x94)^2 + (x168 - x234)^
    2 + (x308 - x374)^2) + 1 / sqrt((x28 - x95)^2 + (x168 - x235)^2 + (x308 -
    x375)^2) + 1 / sqrt((x28 - x96)^2 + (x168 - x236)^2 + (x308 - x376)^2) + 1
    / sqrt((x28 - x97)^2 + (x168 - x237)^2 + (x308 - x377)^2) + 1 / sqrt((x28
    - x98)^2 + (x168 - x238)^2 + (x308 - x378)^2) + 1 / sqrt((x28 - x99)^2 + (
    x168 - x239)^2 + (x308 - x379)^2) + 1 / sqrt((x28 - x100)^2 + (x168 - x240)
    ^2 + (x308 - x380)^2) + 1 / sqrt((x28 - x101)^2 + (x168 - x241)^2 + (x308
    - x381)^2) + 1 / sqrt((x28 - x102)^2 + (x168 - x242)^2 + (x308 - x382)^2)
    + 1 / sqrt((x28 - x103)^2 + (x168 - x243)^2 + (x308 - x383)^2) + 1 / sqrt(
    (x28 - x104)^2 + (x168 - x244)^2 + (x308 - x384)^2) + 1 / sqrt((x28 - x105)
    ^2 + (x168 - x245)^2 + (x308 - x385)^2) + 1 / sqrt((x28 - x106)^2 + (x168
    - x246)^2 + (x308 - x386)^2) + 1 / sqrt((x28 - x107)^2 + (x168 - x247)^2
    + (x308 - x387)^2) + 1 / sqrt((x28 - x108)^2 + (x168 - x248)^2 + (x308 -
    x388)^2) + 1 / sqrt((x28 - x109)^2 + (x168 - x249)^2 + (x308 - x389)^2) + 1
    / sqrt((x28 - x110)^2 + (x168 - x250)^2 + (x308 - x390)^2) + 1 / sqrt((x28
    - x111)^2 + (x168 - x251)^2 + (x308 - x391)^2) + 1 / sqrt((x28 - x112)^2
    + (x168 - x252)^2 + (x308 - x392)^2) + 1 / sqrt((x28 - x113)^2 + (x168 -
    x253)^2 + (x308 - x393)^2) + 1 / sqrt((x28 - x114)^2 + (x168 - x254)^2 + (
    x308 - x394)^2) + 1 / sqrt((x28 - x115)^2 + (x168 - x255)^2 + (x308 - x395)
    ^2) + 1 / sqrt((x28 - x116)^2 + (x168 - x256)^2 + (x308 - x396)^2) + 1 /
    sqrt((x28 - x117)^2 + (x168 - x257)^2 + (x308 - x397)^2) + 1 / sqrt((x28 -
    x118)^2 + (x168 - x258)^2 + (x308 - x398)^2) + 1 / sqrt((x28 - x119)^2 + (
    x168 - x259)^2 + (x308 - x399)^2) + 1 / sqrt((x28 - x120)^2 + (x168 - x260)
    ^2 + (x308 - x400)^2) + 1 / sqrt((x28 - x121)^2 + (x168 - x261)^2 + (x308
    - x401)^2) + 1 / sqrt((x28 - x122)^2 + (x168 - x262)^2 + (x308 - x402)^2)
    + 1 / sqrt((x28 - x123)^2 + (x168 - x263)^2 + (x308 - x403)^2) + 1 / sqrt(
    (x28 - x124)^2 + (x168 - x264)^2 + (x308 - x404)^2) + 1 / sqrt((x28 - x125)
    ^2 + (x168 - x265)^2 + (x308 - x405)^2) + 1 / sqrt((x28 - x126)^2 + (x168
    - x266)^2 + (x308 - x406)^2) + 1 / sqrt((x28 - x127)^2 + (x168 - x267)^2
    + (x308 - x407)^2) + 1 / sqrt((x28 - x128)^2 + (x168 - x268)^2 + (x308 -
    x408)^2) + 1 / sqrt((x28 - x129)^2 + (x168 - x269)^2 + (x308 - x409)^2) + 1
    / sqrt((x28 - x130)^2 + (x168 - x270)^2 + (x308 - x410)^2) + 1 / sqrt((x28
    - x131)^2 + (x168 - x271)^2 + (x308 - x411)^2) + 1 / sqrt((x28 - x132)^2
    + (x168 - x272)^2 + (x308 - x412)^2) + 1 / sqrt((x28 - x133)^2 + (x168 -
    x273)^2 + (x308 - x413)^2) + 1 / sqrt((x28 - x134)^2 + (x168 - x274)^2 + (
    x308 - x414)^2) + 1 / sqrt((x28 - x135)^2 + (x168 - x275)^2 + (x308 - x415)
    ^2) + 1 / sqrt((x28 - x136)^2 + (x168 - x276)^2 + (x308 - x416)^2) + 1 /
    sqrt((x28 - x137)^2 + (x168 - x277)^2 + (x308 - x417)^2) + 1 / sqrt((x28 -
    x138)^2 + (x168 - x278)^2 + (x308 - x418)^2) + 1 / sqrt((x28 - x139)^2 + (
    x168 - x279)^2 + (x308 - x419)^2) + 1 / sqrt((x28 - x140)^2 + (x168 - x280)
    ^2 + (x308 - x420)^2) + 1 / sqrt((x29 - x30)^2 + (x169 - x170)^2 + (x309 -
    x310)^2) + 1 / sqrt((x29 - x31)^2 + (x169 - x171)^2 + (x309 - x311)^2) + 1
    / sqrt((x29 - x32)^2 + (x169 - x172)^2 + (x309 - x312)^2) + 1 / sqrt((x29
    - x33)^2 + (x169 - x173)^2 + (x309 - x313)^2) + 1 / sqrt((x29 - x34)^2 + (
    x169 - x174)^2 + (x309 - x314)^2) + 1 / sqrt((x29 - x35)^2 + (x169 - x175)^
    2 + (x309 - x315)^2) + 1 / sqrt((x29 - x36)^2 + (x169 - x176)^2 + (x309 -
    x316)^2) + 1 / sqrt((x29 - x37)^2 + (x169 - x177)^2 + (x309 - x317)^2) + 1
    / sqrt((x29 - x38)^2 + (x169 - x178)^2 + (x309 - x318)^2) + 1 / sqrt((x29
    - x39)^2 + (x169 - x179)^2 + (x309 - x319)^2) + 1 / sqrt((x29 - x40)^2 + (
    x169 - x180)^2 + (x309 - x320)^2) + 1 / sqrt((x29 - x41)^2 + (x169 - x181)^
    2 + (x309 - x321)^2) + 1 / sqrt((x29 - x42)^2 + (x169 - x182)^2 + (x309 -
    x322)^2) + 1 / sqrt((x29 - x43)^2 + (x169 - x183)^2 + (x309 - x323)^2) + 1
    / sqrt((x29 - x44)^2 + (x169 - x184)^2 + (x309 - x324)^2) + 1 / sqrt((x29
    - x45)^2 + (x169 - x185)^2 + (x309 - x325)^2) + 1 / sqrt((x29 - x46)^2 + (
    x169 - x186)^2 + (x309 - x326)^2) + 1 / sqrt((x29 - x47)^2 + (x169 - x187)^
    2 + (x309 - x327)^2) + 1 / sqrt((x29 - x48)^2 + (x169 - x188)^2 + (x309 -
    x328)^2) + 1 / sqrt((x29 - x49)^2 + (x169 - x189)^2 + (x309 - x329)^2) + 1
    / sqrt((x29 - x50)^2 + (x169 - x190)^2 + (x309 - x330)^2) + 1 / sqrt((x29
    - x51)^2 + (x169 - x191)^2 + (x309 - x331)^2) + 1 / sqrt((x29 - x52)^2 + (
    x169 - x192)^2 + (x309 - x332)^2) + 1 / sqrt((x29 - x53)^2 + (x169 - x193)^
    2 + (x309 - x333)^2) + 1 / sqrt((x29 - x54)^2 + (x169 - x194)^2 + (x309 -
    x334)^2) + 1 / sqrt((x29 - x55)^2 + (x169 - x195)^2 + (x309 - x335)^2) + 1
    / sqrt((x29 - x56)^2 + (x169 - x196)^2 + (x309 - x336)^2) + 1 / sqrt((x29
    - x57)^2 + (x169 - x197)^2 + (x309 - x337)^2) + 1 / sqrt((x29 - x58)^2 + (
    x169 - x198)^2 + (x309 - x338)^2) + 1 / sqrt((x29 - x59)^2 + (x169 - x199)^
    2 + (x309 - x339)^2) + 1 / sqrt((x29 - x60)^2 + (x169 - x200)^2 + (x309 -
    x340)^2) + 1 / sqrt((x29 - x61)^2 + (x169 - x201)^2 + (x309 - x341)^2) + 1
    / sqrt((x29 - x62)^2 + (x169 - x202)^2 + (x309 - x342)^2) + 1 / sqrt((x29
    - x63)^2 + (x169 - x203)^2 + (x309 - x343)^2) + 1 / sqrt((x29 - x64)^2 + (
    x169 - x204)^2 + (x309 - x344)^2) + 1 / sqrt((x29 - x65)^2 + (x169 - x205)^
    2 + (x309 - x345)^2) + 1 / sqrt((x29 - x66)^2 + (x169 - x206)^2 + (x309 -
    x346)^2) + 1 / sqrt((x29 - x67)^2 + (x169 - x207)^2 + (x309 - x347)^2) + 1
    / sqrt((x29 - x68)^2 + (x169 - x208)^2 + (x309 - x348)^2) + 1 / sqrt((x29
    - x69)^2 + (x169 - x209)^2 + (x309 - x349)^2) + 1 / sqrt((x29 - x70)^2 + (
    x169 - x210)^2 + (x309 - x350)^2) + 1 / sqrt((x29 - x71)^2 + (x169 - x211)^
    2 + (x309 - x351)^2) + 1 / sqrt((x29 - x72)^2 + (x169 - x212)^2 + (x309 -
    x352)^2) + 1 / sqrt((x29 - x73)^2 + (x169 - x213)^2 + (x309 - x353)^2) + 1
    / sqrt((x29 - x74)^2 + (x169 - x214)^2 + (x309 - x354)^2) + 1 / sqrt((x29
    - x75)^2 + (x169 - x215)^2 + (x309 - x355)^2) + 1 / sqrt((x29 - x76)^2 + (
    x169 - x216)^2 + (x309 - x356)^2) + 1 / sqrt((x29 - x77)^2 + (x169 - x217)^
    2 + (x309 - x357)^2) + 1 / sqrt((x29 - x78)^2 + (x169 - x218)^2 + (x309 -
    x358)^2) + 1 / sqrt((x29 - x79)^2 + (x169 - x219)^2 + (x309 - x359)^2) + 1
    / sqrt((x29 - x80)^2 + (x169 - x220)^2 + (x309 - x360)^2) + 1 / sqrt((x29
    - x81)^2 + (x169 - x221)^2 + (x309 - x361)^2) + 1 / sqrt((x29 - x82)^2 + (
    x169 - x222)^2 + (x309 - x362)^2) + 1 / sqrt((x29 - x83)^2 + (x169 - x223)^
    2 + (x309 - x363)^2) + 1 / sqrt((x29 - x84)^2 + (x169 - x224)^2 + (x309 -
    x364)^2) + 1 / sqrt((x29 - x85)^2 + (x169 - x225)^2 + (x309 - x365)^2) + 1
    / sqrt((x29 - x86)^2 + (x169 - x226)^2 + (x309 - x366)^2) + 1 / sqrt((x29
    - x87)^2 + (x169 - x227)^2 + (x309 - x367)^2) + 1 / sqrt((x29 - x88)^2 + (
    x169 - x228)^2 + (x309 - x368)^2) + 1 / sqrt((x29 - x89)^2 + (x169 - x229)^
    2 + (x309 - x369)^2) + 1 / sqrt((x29 - x90)^2 + (x169 - x230)^2 + (x309 -
    x370)^2) + 1 / sqrt((x29 - x91)^2 + (x169 - x231)^2 + (x309 - x371)^2) + 1
    / sqrt((x29 - x92)^2 + (x169 - x232)^2 + (x309 - x372)^2) + 1 / sqrt((x29
    - x93)^2 + (x169 - x233)^2 + (x309 - x373)^2) + 1 / sqrt((x29 - x94)^2 + (
    x169 - x234)^2 + (x309 - x374)^2) + 1 / sqrt((x29 - x95)^2 + (x169 - x235)^
    2 + (x309 - x375)^2) + 1 / sqrt((x29 - x96)^2 + (x169 - x236)^2 + (x309 -
    x376)^2) + 1 / sqrt((x29 - x97)^2 + (x169 - x237)^2 + (x309 - x377)^2) + 1
    / sqrt((x29 - x98)^2 + (x169 - x238)^2 + (x309 - x378)^2) + 1 / sqrt((x29
    - x99)^2 + (x169 - x239)^2 + (x309 - x379)^2) + 1 / sqrt((x29 - x100)^2 +
    (x169 - x240)^2 + (x309 - x380)^2) + 1 / sqrt((x29 - x101)^2 + (x169 - x241)
    ^2 + (x309 - x381)^2) + 1 / sqrt((x29 - x102)^2 + (x169 - x242)^2 + (x309
    - x382)^2) + 1 / sqrt((x29 - x103)^2 + (x169 - x243)^2 + (x309 - x383)^2)
    + 1 / sqrt((x29 - x104)^2 + (x169 - x244)^2 + (x309 - x384)^2) + 1 / sqrt(
    (x29 - x105)^2 + (x169 - x245)^2 + (x309 - x385)^2) + 1 / sqrt((x29 - x106)
    ^2 + (x169 - x246)^2 + (x309 - x386)^2) + 1 / sqrt((x29 - x107)^2 + (x169
    - x247)^2 + (x309 - x387)^2) + 1 / sqrt((x29 - x108)^2 + (x169 - x248)^2
    + (x309 - x388)^2) + 1 / sqrt((x29 - x109)^2 + (x169 - x249)^2 + (x309 -
    x389)^2) + 1 / sqrt((x29 - x110)^2 + (x169 - x250)^2 + (x309 - x390)^2) + 1
    / sqrt((x29 - x111)^2 + (x169 - x251)^2 + (x309 - x391)^2) + 1 / sqrt((x29
    - x112)^2 + (x169 - x252)^2 + (x309 - x392)^2) + 1 / sqrt((x29 - x113)^2
    + (x169 - x253)^2 + (x309 - x393)^2) + 1 / sqrt((x29 - x114)^2 + (x169 -
    x254)^2 + (x309 - x394)^2) + 1 / sqrt((x29 - x115)^2 + (x169 - x255)^2 + (
    x309 - x395)^2) + 1 / sqrt((x29 - x116)^2 + (x169 - x256)^2 + (x309 - x396)
    ^2) + 1 / sqrt((x29 - x117)^2 + (x169 - x257)^2 + (x309 - x397)^2) + 1 /
    sqrt((x29 - x118)^2 + (x169 - x258)^2 + (x309 - x398)^2) + 1 / sqrt((x29 -
    x119)^2 + (x169 - x259)^2 + (x309 - x399)^2) + 1 / sqrt((x29 - x120)^2 + (
    x169 - x260)^2 + (x309 - x400)^2) + 1 / sqrt((x29 - x121)^2 + (x169 - x261)
    ^2 + (x309 - x401)^2) + 1 / sqrt((x29 - x122)^2 + (x169 - x262)^2 + (x309
    - x402)^2) + 1 / sqrt((x29 - x123)^2 + (x169 - x263)^2 + (x309 - x403)^2)
    + 1 / sqrt((x29 - x124)^2 + (x169 - x264)^2 + (x309 - x404)^2) + 1 / sqrt(
    (x29 - x125)^2 + (x169 - x265)^2 + (x309 - x405)^2) + 1 / sqrt((x29 - x126)
    ^2 + (x169 - x266)^2 + (x309 - x406)^2) + 1 / sqrt((x29 - x127)^2 + (x169
    - x267)^2 + (x309 - x407)^2) + 1 / sqrt((x29 - x128)^2 + (x169 - x268)^2
    + (x309 - x408)^2) + 1 / sqrt((x29 - x129)^2 + (x169 - x269)^2 + (x309 -
    x409)^2) + 1 / sqrt((x29 - x130)^2 + (x169 - x270)^2 + (x309 - x410)^2) + 1
    / sqrt((x29 - x131)^2 + (x169 - x271)^2 + (x309 - x411)^2) + 1 / sqrt((x29
    - x132)^2 + (x169 - x272)^2 + (x309 - x412)^2) + 1 / sqrt((x29 - x133)^2
    + (x169 - x273)^2 + (x309 - x413)^2) + 1 / sqrt((x29 - x134)^2 + (x169 -
    x274)^2 + (x309 - x414)^2) + 1 / sqrt((x29 - x135)^2 + (x169 - x275)^2 + (
    x309 - x415)^2) + 1 / sqrt((x29 - x136)^2 + (x169 - x276)^2 + (x309 - x416)
    ^2) + 1 / sqrt((x29 - x137)^2 + (x169 - x277)^2 + (x309 - x417)^2) + 1 /
    sqrt((x29 - x138)^2 + (x169 - x278)^2 + (x309 - x418)^2) + 1 / sqrt((x29 -
    x139)^2 + (x169 - x279)^2 + (x309 - x419)^2) + 1 / sqrt((x29 - x140)^2 + (
    x169 - x280)^2 + (x309 - x420)^2) + 1 / sqrt((x30 - x31)^2 + (x170 - x171)^
    2 + (x310 - x311)^2) + 1 / sqrt((x30 - x32)^2 + (x170 - x172)^2 + (x310 -
    x312)^2) + 1 / sqrt((x30 - x33)^2 + (x170 - x173)^2 + (x310 - x313)^2) + 1
    / sqrt((x30 - x34)^2 + (x170 - x174)^2 + (x310 - x314)^2) + 1 / sqrt((x30
    - x35)^2 + (x170 - x175)^2 + (x310 - x315)^2) + 1 / sqrt((x30 - x36)^2 + (
    x170 - x176)^2 + (x310 - x316)^2) + 1 / sqrt((x30 - x37)^2 + (x170 - x177)^
    2 + (x310 - x317)^2) + 1 / sqrt((x30 - x38)^2 + (x170 - x178)^2 + (x310 -
    x318)^2) + 1 / sqrt((x30 - x39)^2 + (x170 - x179)^2 + (x310 - x319)^2) + 1
    / sqrt((x30 - x40)^2 + (x170 - x180)^2 + (x310 - x320)^2) + 1 / sqrt((x30
    - x41)^2 + (x170 - x181)^2 + (x310 - x321)^2) + 1 / sqrt((x30 - x42)^2 + (
    x170 - x182)^2 + (x310 - x322)^2) + 1 / sqrt((x30 - x43)^2 + (x170 - x183)^
    2 + (x310 - x323)^2) + 1 / sqrt((x30 - x44)^2 + (x170 - x184)^2 + (x310 -
    x324)^2) + 1 / sqrt((x30 - x45)^2 + (x170 - x185)^2 + (x310 - x325)^2) + 1
    / sqrt((x30 - x46)^2 + (x170 - x186)^2 + (x310 - x326)^2) + 1 / sqrt((x30
    - x47)^2 + (x170 - x187)^2 + (x310 - x327)^2) + 1 / sqrt((x30 - x48)^2 + (
    x170 - x188)^2 + (x310 - x328)^2) + 1 / sqrt((x30 - x49)^2 + (x170 - x189)^
    2 + (x310 - x329)^2) + 1 / sqrt((x30 - x50)^2 + (x170 - x190)^2 + (x310 -
    x330)^2) + 1 / sqrt((x30 - x51)^2 + (x170 - x191)^2 + (x310 - x331)^2) + 1
    / sqrt((x30 - x52)^2 + (x170 - x192)^2 + (x310 - x332)^2) + 1 / sqrt((x30
    - x53)^2 + (x170 - x193)^2 + (x310 - x333)^2) + 1 / sqrt((x30 - x54)^2 + (
    x170 - x194)^2 + (x310 - x334)^2) + 1 / sqrt((x30 - x55)^2 + (x170 - x195)^
    2 + (x310 - x335)^2) + 1 / sqrt((x30 - x56)^2 + (x170 - x196)^2 + (x310 -
    x336)^2) + 1 / sqrt((x30 - x57)^2 + (x170 - x197)^2 + (x310 - x337)^2) + 1
    / sqrt((x30 - x58)^2 + (x170 - x198)^2 + (x310 - x338)^2) + 1 / sqrt((x30
    - x59)^2 + (x170 - x199)^2 + (x310 - x339)^2) + 1 / sqrt((x30 - x60)^2 + (
    x170 - x200)^2 + (x310 - x340)^2) + 1 / sqrt((x30 - x61)^2 + (x170 - x201)^
    2 + (x310 - x341)^2) + 1 / sqrt((x30 - x62)^2 + (x170 - x202)^2 + (x310 -
    x342)^2) + 1 / sqrt((x30 - x63)^2 + (x170 - x203)^2 + (x310 - x343)^2) + 1
    / sqrt((x30 - x64)^2 + (x170 - x204)^2 + (x310 - x344)^2) + 1 / sqrt((x30
    - x65)^2 + (x170 - x205)^2 + (x310 - x345)^2) + 1 / sqrt((x30 - x66)^2 + (
    x170 - x206)^2 + (x310 - x346)^2) + 1 / sqrt((x30 - x67)^2 + (x170 - x207)^
    2 + (x310 - x347)^2) + 1 / sqrt((x30 - x68)^2 + (x170 - x208)^2 + (x310 -
    x348)^2) + 1 / sqrt((x30 - x69)^2 + (x170 - x209)^2 + (x310 - x349)^2) + 1
    / sqrt((x30 - x70)^2 + (x170 - x210)^2 + (x310 - x350)^2) + 1 / sqrt((x30
    - x71)^2 + (x170 - x211)^2 + (x310 - x351)^2) + 1 / sqrt((x30 - x72)^2 + (
    x170 - x212)^2 + (x310 - x352)^2) + 1 / sqrt((x30 - x73)^2 + (x170 - x213)^
    2 + (x310 - x353)^2) + 1 / sqrt((x30 - x74)^2 + (x170 - x214)^2 + (x310 -
    x354)^2) + 1 / sqrt((x30 - x75)^2 + (x170 - x215)^2 + (x310 - x355)^2) + 1
    / sqrt((x30 - x76)^2 + (x170 - x216)^2 + (x310 - x356)^2) + 1 / sqrt((x30
    - x77)^2 + (x170 - x217)^2 + (x310 - x357)^2) + 1 / sqrt((x30 - x78)^2 + (
    x170 - x218)^2 + (x310 - x358)^2) + 1 / sqrt((x30 - x79)^2 + (x170 - x219)^
    2 + (x310 - x359)^2) + 1 / sqrt((x30 - x80)^2 + (x170 - x220)^2 + (x310 -
    x360)^2) + 1 / sqrt((x30 - x81)^2 + (x170 - x221)^2 + (x310 - x361)^2) + 1
    / sqrt((x30 - x82)^2 + (x170 - x222)^2 + (x310 - x362)^2) + 1 / sqrt((x30
    - x83)^2 + (x170 - x223)^2 + (x310 - x363)^2) + 1 / sqrt((x30 - x84)^2 + (
    x170 - x224)^2 + (x310 - x364)^2) + 1 / sqrt((x30 - x85)^2 + (x170 - x225)^
    2 + (x310 - x365)^2) + 1 / sqrt((x30 - x86)^2 + (x170 - x226)^2 + (x310 -
    x366)^2) + 1 / sqrt((x30 - x87)^2 + (x170 - x227)^2 + (x310 - x367)^2) + 1
    / sqrt((x30 - x88)^2 + (x170 - x228)^2 + (x310 - x368)^2) + 1 / sqrt((x30
    - x89)^2 + (x170 - x229)^2 + (x310 - x369)^2) + 1 / sqrt((x30 - x90)^2 + (
    x170 - x230)^2 + (x310 - x370)^2) + 1 / sqrt((x30 - x91)^2 + (x170 - x231)^
    2 + (x310 - x371)^2) + 1 / sqrt((x30 - x92)^2 + (x170 - x232)^2 + (x310 -
    x372)^2) + 1 / sqrt((x30 - x93)^2 + (x170 - x233)^2 + (x310 - x373)^2) + 1
    / sqrt((x30 - x94)^2 + (x170 - x234)^2 + (x310 - x374)^2) + 1 / sqrt((x30
    - x95)^2 + (x170 - x235)^2 + (x310 - x375)^2) + 1 / sqrt((x30 - x96)^2 + (
    x170 - x236)^2 + (x310 - x376)^2) + 1 / sqrt((x30 - x97)^2 + (x170 - x237)^
    2 + (x310 - x377)^2) + 1 / sqrt((x30 - x98)^2 + (x170 - x238)^2 + (x310 -
    x378)^2) + 1 / sqrt((x30 - x99)^2 + (x170 - x239)^2 + (x310 - x379)^2) + 1
    / sqrt((x30 - x100)^2 + (x170 - x240)^2 + (x310 - x380)^2) + 1 / sqrt((x30
    - x101)^2 + (x170 - x241)^2 + (x310 - x381)^2) + 1 / sqrt((x30 - x102)^2
    + (x170 - x242)^2 + (x310 - x382)^2) + 1 / sqrt((x30 - x103)^2 + (x170 -
    x243)^2 + (x310 - x383)^2) + 1 / sqrt((x30 - x104)^2 + (x170 - x244)^2 + (
    x310 - x384)^2) + 1 / sqrt((x30 - x105)^2 + (x170 - x245)^2 + (x310 - x385)
    ^2) + 1 / sqrt((x30 - x106)^2 + (x170 - x246)^2 + (x310 - x386)^2) + 1 /
    sqrt((x30 - x107)^2 + (x170 - x247)^2 + (x310 - x387)^2) + 1 / sqrt((x30 -
    x108)^2 + (x170 - x248)^2 + (x310 - x388)^2) + 1 / sqrt((x30 - x109)^2 + (
    x170 - x249)^2 + (x310 - x389)^2) + 1 / sqrt((x30 - x110)^2 + (x170 - x250)
    ^2 + (x310 - x390)^2) + 1 / sqrt((x30 - x111)^2 + (x170 - x251)^2 + (x310
    - x391)^2) + 1 / sqrt((x30 - x112)^2 + (x170 - x252)^2 + (x310 - x392)^2)
    + 1 / sqrt((x30 - x113)^2 + (x170 - x253)^2 + (x310 - x393)^2) + 1 / sqrt(
    (x30 - x114)^2 + (x170 - x254)^2 + (x310 - x394)^2) + 1 / sqrt((x30 - x115)
    ^2 + (x170 - x255)^2 + (x310 - x395)^2) + 1 / sqrt((x30 - x116)^2 + (x170
    - x256)^2 + (x310 - x396)^2) + 1 / sqrt((x30 - x117)^2 + (x170 - x257)^2
    + (x310 - x397)^2) + 1 / sqrt((x30 - x118)^2 + (x170 - x258)^2 + (x310 -
    x398)^2) + 1 / sqrt((x30 - x119)^2 + (x170 - x259)^2 + (x310 - x399)^2) + 1
    / sqrt((x30 - x120)^2 + (x170 - x260)^2 + (x310 - x400)^2) + 1 / sqrt((x30
    - x121)^2 + (x170 - x261)^2 + (x310 - x401)^2) + 1 / sqrt((x30 - x122)^2
    + (x170 - x262)^2 + (x310 - x402)^2) + 1 / sqrt((x30 - x123)^2 + (x170 -
    x263)^2 + (x310 - x403)^2) + 1 / sqrt((x30 - x124)^2 + (x170 - x264)^2 + (
    x310 - x404)^2) + 1 / sqrt((x30 - x125)^2 + (x170 - x265)^2 + (x310 - x405)
    ^2) + 1 / sqrt((x30 - x126)^2 + (x170 - x266)^2 + (x310 - x406)^2) + 1 /
    sqrt((x30 - x127)^2 + (x170 - x267)^2 + (x310 - x407)^2) + 1 / sqrt((x30 -
    x128)^2 + (x170 - x268)^2 + (x310 - x408)^2) + 1 / sqrt((x30 - x129)^2 + (
    x170 - x269)^2 + (x310 - x409)^2) + 1 / sqrt((x30 - x130)^2 + (x170 - x270)
    ^2 + (x310 - x410)^2) + 1 / sqrt((x30 - x131)^2 + (x170 - x271)^2 + (x310
    - x411)^2) + 1 / sqrt((x30 - x132)^2 + (x170 - x272)^2 + (x310 - x412)^2)
    + 1 / sqrt((x30 - x133)^2 + (x170 - x273)^2 + (x310 - x413)^2) + 1 / sqrt(
    (x30 - x134)^2 + (x170 - x274)^2 + (x310 - x414)^2) + 1 / sqrt((x30 - x135)
    ^2 + (x170 - x275)^2 + (x310 - x415)^2) + 1 / sqrt((x30 - x136)^2 + (x170
    - x276)^2 + (x310 - x416)^2) + 1 / sqrt((x30 - x137)^2 + (x170 - x277)^2
    + (x310 - x417)^2) + 1 / sqrt((x30 - x138)^2 + (x170 - x278)^2 + (x310 -
    x418)^2) + 1 / sqrt((x30 - x139)^2 + (x170 - x279)^2 + (x310 - x419)^2) + 1
    / sqrt((x30 - x140)^2 + (x170 - x280)^2 + (x310 - x420)^2) + 1 / sqrt((x31
    - x32)^2 + (x171 - x172)^2 + (x311 - x312)^2) + 1 / sqrt((x31 - x33)^2 + (
    x171 - x173)^2 + (x311 - x313)^2) + 1 / sqrt((x31 - x34)^2 + (x171 - x174)^
    2 + (x311 - x314)^2) + 1 / sqrt((x31 - x35)^2 + (x171 - x175)^2 + (x311 -
    x315)^2) + 1 / sqrt((x31 - x36)^2 + (x171 - x176)^2 + (x311 - x316)^2) + 1
    / sqrt((x31 - x37)^2 + (x171 - x177)^2 + (x311 - x317)^2) + 1 / sqrt((x31
    - x38)^2 + (x171 - x178)^2 + (x311 - x318)^2) + 1 / sqrt((x31 - x39)^2 + (
    x171 - x179)^2 + (x311 - x319)^2) + 1 / sqrt((x31 - x40)^2 + (x171 - x180)^
    2 + (x311 - x320)^2) + 1 / sqrt((x31 - x41)^2 + (x171 - x181)^2 + (x311 -
    x321)^2) + 1 / sqrt((x31 - x42)^2 + (x171 - x182)^2 + (x311 - x322)^2) + 1
    / sqrt((x31 - x43)^2 + (x171 - x183)^2 + (x311 - x323)^2) + 1 / sqrt((x31
    - x44)^2 + (x171 - x184)^2 + (x311 - x324)^2) + 1 / sqrt((x31 - x45)^2 + (
    x171 - x185)^2 + (x311 - x325)^2) + 1 / sqrt((x31 - x46)^2 + (x171 - x186)^
    2 + (x311 - x326)^2) + 1 / sqrt((x31 - x47)^2 + (x171 - x187)^2 + (x311 -
    x327)^2) + 1 / sqrt((x31 - x48)^2 + (x171 - x188)^2 + (x311 - x328)^2) + 1
    / sqrt((x31 - x49)^2 + (x171 - x189)^2 + (x311 - x329)^2) + 1 / sqrt((x31
    - x50)^2 + (x171 - x190)^2 + (x311 - x330)^2) + 1 / sqrt((x31 - x51)^2 + (
    x171 - x191)^2 + (x311 - x331)^2) + 1 / sqrt((x31 - x52)^2 + (x171 - x192)^
    2 + (x311 - x332)^2) + 1 / sqrt((x31 - x53)^2 + (x171 - x193)^2 + (x311 -
    x333)^2) + 1 / sqrt((x31 - x54)^2 + (x171 - x194)^2 + (x311 - x334)^2) + 1
    / sqrt((x31 - x55)^2 + (x171 - x195)^2 + (x311 - x335)^2) + 1 / sqrt((x31
    - x56)^2 + (x171 - x196)^2 + (x311 - x336)^2) + 1 / sqrt((x31 - x57)^2 + (
    x171 - x197)^2 + (x311 - x337)^2) + 1 / sqrt((x31 - x58)^2 + (x171 - x198)^
    2 + (x311 - x338)^2) + 1 / sqrt((x31 - x59)^2 + (x171 - x199)^2 + (x311 -
    x339)^2) + 1 / sqrt((x31 - x60)^2 + (x171 - x200)^2 + (x311 - x340)^2) + 1
    / sqrt((x31 - x61)^2 + (x171 - x201)^2 + (x311 - x341)^2) + 1 / sqrt((x31
    - x62)^2 + (x171 - x202)^2 + (x311 - x342)^2) + 1 / sqrt((x31 - x63)^2 + (
    x171 - x203)^2 + (x311 - x343)^2) + 1 / sqrt((x31 - x64)^2 + (x171 - x204)^
    2 + (x311 - x344)^2) + 1 / sqrt((x31 - x65)^2 + (x171 - x205)^2 + (x311 -
    x345)^2) + 1 / sqrt((x31 - x66)^2 + (x171 - x206)^2 + (x311 - x346)^2) + 1
    / sqrt((x31 - x67)^2 + (x171 - x207)^2 + (x311 - x347)^2) + 1 / sqrt((x31
    - x68)^2 + (x171 - x208)^2 + (x311 - x348)^2) + 1 / sqrt((x31 - x69)^2 + (
    x171 - x209)^2 + (x311 - x349)^2) + 1 / sqrt((x31 - x70)^2 + (x171 - x210)^
    2 + (x311 - x350)^2) + 1 / sqrt((x31 - x71)^2 + (x171 - x211)^2 + (x311 -
    x351)^2) + 1 / sqrt((x31 - x72)^2 + (x171 - x212)^2 + (x311 - x352)^2) + 1
    / sqrt((x31 - x73)^2 + (x171 - x213)^2 + (x311 - x353)^2) + 1 / sqrt((x31
    - x74)^2 + (x171 - x214)^2 + (x311 - x354)^2) + 1 / sqrt((x31 - x75)^2 + (
    x171 - x215)^2 + (x311 - x355)^2) + 1 / sqrt((x31 - x76)^2 + (x171 - x216)^
    2 + (x311 - x356)^2) + 1 / sqrt((x31 - x77)^2 + (x171 - x217)^2 + (x311 -
    x357)^2) + 1 / sqrt((x31 - x78)^2 + (x171 - x218)^2 + (x311 - x358)^2) + 1
    / sqrt((x31 - x79)^2 + (x171 - x219)^2 + (x311 - x359)^2) + 1 / sqrt((x31
    - x80)^2 + (x171 - x220)^2 + (x311 - x360)^2) + 1 / sqrt((x31 - x81)^2 + (
    x171 - x221)^2 + (x311 - x361)^2) + 1 / sqrt((x31 - x82)^2 + (x171 - x222)^
    2 + (x311 - x362)^2) + 1 / sqrt((x31 - x83)^2 + (x171 - x223)^2 + (x311 -
    x363)^2) + 1 / sqrt((x31 - x84)^2 + (x171 - x224)^2 + (x311 - x364)^2) + 1
    / sqrt((x31 - x85)^2 + (x171 - x225)^2 + (x311 - x365)^2) + 1 / sqrt((x31
    - x86)^2 + (x171 - x226)^2 + (x311 - x366)^2) + 1 / sqrt((x31 - x87)^2 + (
    x171 - x227)^2 + (x311 - x367)^2) + 1 / sqrt((x31 - x88)^2 + (x171 - x228)^
    2 + (x311 - x368)^2) + 1 / sqrt((x31 - x89)^2 + (x171 - x229)^2 + (x311 -
    x369)^2) + 1 / sqrt((x31 - x90)^2 + (x171 - x230)^2 + (x311 - x370)^2) + 1
    / sqrt((x31 - x91)^2 + (x171 - x231)^2 + (x311 - x371)^2) + 1 / sqrt((x31
    - x92)^2 + (x171 - x232)^2 + (x311 - x372)^2) + 1 / sqrt((x31 - x93)^2 + (
    x171 - x233)^2 + (x311 - x373)^2) + 1 / sqrt((x31 - x94)^2 + (x171 - x234)^
    2 + (x311 - x374)^2) + 1 / sqrt((x31 - x95)^2 + (x171 - x235)^2 + (x311 -
    x375)^2) + 1 / sqrt((x31 - x96)^2 + (x171 - x236)^2 + (x311 - x376)^2) + 1
    / sqrt((x31 - x97)^2 + (x171 - x237)^2 + (x311 - x377)^2) + 1 / sqrt((x31
    - x98)^2 + (x171 - x238)^2 + (x311 - x378)^2) + 1 / sqrt((x31 - x99)^2 + (
    x171 - x239)^2 + (x311 - x379)^2) + 1 / sqrt((x31 - x100)^2 + (x171 - x240)
    ^2 + (x311 - x380)^2) + 1 / sqrt((x31 - x101)^2 + (x171 - x241)^2 + (x311
    - x381)^2) + 1 / sqrt((x31 - x102)^2 + (x171 - x242)^2 + (x311 - x382)^2)
    + 1 / sqrt((x31 - x103)^2 + (x171 - x243)^2 + (x311 - x383)^2) + 1 / sqrt(
    (x31 - x104)^2 + (x171 - x244)^2 + (x311 - x384)^2) + 1 / sqrt((x31 - x105)
    ^2 + (x171 - x245)^2 + (x311 - x385)^2) + 1 / sqrt((x31 - x106)^2 + (x171
    - x246)^2 + (x311 - x386)^2) + 1 / sqrt((x31 - x107)^2 + (x171 - x247)^2
    + (x311 - x387)^2) + 1 / sqrt((x31 - x108)^2 + (x171 - x248)^2 + (x311 -
    x388)^2) + 1 / sqrt((x31 - x109)^2 + (x171 - x249)^2 + (x311 - x389)^2) + 1
    / sqrt((x31 - x110)^2 + (x171 - x250)^2 + (x311 - x390)^2) + 1 / sqrt((x31
    - x111)^2 + (x171 - x251)^2 + (x311 - x391)^2) + 1 / sqrt((x31 - x112)^2
    + (x171 - x252)^2 + (x311 - x392)^2) + 1 / sqrt((x31 - x113)^2 + (x171 -
    x253)^2 + (x311 - x393)^2) + 1 / sqrt((x31 - x114)^2 + (x171 - x254)^2 + (
    x311 - x394)^2) + 1 / sqrt((x31 - x115)^2 + (x171 - x255)^2 + (x311 - x395)
    ^2) + 1 / sqrt((x31 - x116)^2 + (x171 - x256)^2 + (x311 - x396)^2) + 1 /
    sqrt((x31 - x117)^2 + (x171 - x257)^2 + (x311 - x397)^2) + 1 / sqrt((x31 -
    x118)^2 + (x171 - x258)^2 + (x311 - x398)^2) + 1 / sqrt((x31 - x119)^2 + (
    x171 - x259)^2 + (x311 - x399)^2) + 1 / sqrt((x31 - x120)^2 + (x171 - x260)
    ^2 + (x311 - x400)^2) + 1 / sqrt((x31 - x121)^2 + (x171 - x261)^2 + (x311
    - x401)^2) + 1 / sqrt((x31 - x122)^2 + (x171 - x262)^2 + (x311 - x402)^2)
    + 1 / sqrt((x31 - x123)^2 + (x171 - x263)^2 + (x311 - x403)^2) + 1 / sqrt(
    (x31 - x124)^2 + (x171 - x264)^2 + (x311 - x404)^2) + 1 / sqrt((x31 - x125)
    ^2 + (x171 - x265)^2 + (x311 - x405)^2) + 1 / sqrt((x31 - x126)^2 + (x171
    - x266)^2 + (x311 - x406)^2) + 1 / sqrt((x31 - x127)^2 + (x171 - x267)^2
    + (x311 - x407)^2) + 1 / sqrt((x31 - x128)^2 + (x171 - x268)^2 + (x311 -
    x408)^2) + 1 / sqrt((x31 - x129)^2 + (x171 - x269)^2 + (x311 - x409)^2) + 1
    / sqrt((x31 - x130)^2 + (x171 - x270)^2 + (x311 - x410)^2) + 1 / sqrt((x31
    - x131)^2 + (x171 - x271)^2 + (x311 - x411)^2) + 1 / sqrt((x31 - x132)^2
    + (x171 - x272)^2 + (x311 - x412)^2) + 1 / sqrt((x31 - x133)^2 + (x171 -
    x273)^2 + (x311 - x413)^2) + 1 / sqrt((x31 - x134)^2 + (x171 - x274)^2 + (
    x311 - x414)^2) + 1 / sqrt((x31 - x135)^2 + (x171 - x275)^2 + (x311 - x415)
    ^2) + 1 / sqrt((x31 - x136)^2 + (x171 - x276)^2 + (x311 - x416)^2) + 1 /
    sqrt((x31 - x137)^2 + (x171 - x277)^2 + (x311 - x417)^2) + 1 / sqrt((x31 -
    x138)^2 + (x171 - x278)^2 + (x311 - x418)^2) + 1 / sqrt((x31 - x139)^2 + (
    x171 - x279)^2 + (x311 - x419)^2) + 1 / sqrt((x31 - x140)^2 + (x171 - x280)
    ^2 + (x311 - x420)^2) + 1 / sqrt((x32 - x33)^2 + (x172 - x173)^2 + (x312 -
    x313)^2) + 1 / sqrt((x32 - x34)^2 + (x172 - x174)^2 + (x312 - x314)^2) + 1
    / sqrt((x32 - x35)^2 + (x172 - x175)^2 + (x312 - x315)^2) + 1 / sqrt((x32
    - x36)^2 + (x172 - x176)^2 + (x312 - x316)^2) + 1 / sqrt((x32 - x37)^2 + (
    x172 - x177)^2 + (x312 - x317)^2) + 1 / sqrt((x32 - x38)^2 + (x172 - x178)^
    2 + (x312 - x318)^2) + 1 / sqrt((x32 - x39)^2 + (x172 - x179)^2 + (x312 -
    x319)^2) + 1 / sqrt((x32 - x40)^2 + (x172 - x180)^2 + (x312 - x320)^2) + 1
    / sqrt((x32 - x41)^2 + (x172 - x181)^2 + (x312 - x321)^2) + 1 / sqrt((x32
    - x42)^2 + (x172 - x182)^2 + (x312 - x322)^2) + 1 / sqrt((x32 - x43)^2 + (
    x172 - x183)^2 + (x312 - x323)^2) + 1 / sqrt((x32 - x44)^2 + (x172 - x184)^
    2 + (x312 - x324)^2) + 1 / sqrt((x32 - x45)^2 + (x172 - x185)^2 + (x312 -
    x325)^2) + 1 / sqrt((x32 - x46)^2 + (x172 - x186)^2 + (x312 - x326)^2) + 1
    / sqrt((x32 - x47)^2 + (x172 - x187)^2 + (x312 - x327)^2) + 1 / sqrt((x32
    - x48)^2 + (x172 - x188)^2 + (x312 - x328)^2) + 1 / sqrt((x32 - x49)^2 + (
    x172 - x189)^2 + (x312 - x329)^2) + 1 / sqrt((x32 - x50)^2 + (x172 - x190)^
    2 + (x312 - x330)^2) + 1 / sqrt((x32 - x51)^2 + (x172 - x191)^2 + (x312 -
    x331)^2) + 1 / sqrt((x32 - x52)^2 + (x172 - x192)^2 + (x312 - x332)^2) + 1
    / sqrt((x32 - x53)^2 + (x172 - x193)^2 + (x312 - x333)^2) + 1 / sqrt((x32
    - x54)^2 + (x172 - x194)^2 + (x312 - x334)^2) + 1 / sqrt((x32 - x55)^2 + (
    x172 - x195)^2 + (x312 - x335)^2) + 1 / sqrt((x32 - x56)^2 + (x172 - x196)^
    2 + (x312 - x336)^2) + 1 / sqrt((x32 - x57)^2 + (x172 - x197)^2 + (x312 -
    x337)^2) + 1 / sqrt((x32 - x58)^2 + (x172 - x198)^2 + (x312 - x338)^2) + 1
    / sqrt((x32 - x59)^2 + (x172 - x199)^2 + (x312 - x339)^2) + 1 / sqrt((x32
    - x60)^2 + (x172 - x200)^2 + (x312 - x340)^2) + 1 / sqrt((x32 - x61)^2 + (
    x172 - x201)^2 + (x312 - x341)^2) + 1 / sqrt((x32 - x62)^2 + (x172 - x202)^
    2 + (x312 - x342)^2) + 1 / sqrt((x32 - x63)^2 + (x172 - x203)^2 + (x312 -
    x343)^2) + 1 / sqrt((x32 - x64)^2 + (x172 - x204)^2 + (x312 - x344)^2) + 1
    / sqrt((x32 - x65)^2 + (x172 - x205)^2 + (x312 - x345)^2) + 1 / sqrt((x32
    - x66)^2 + (x172 - x206)^2 + (x312 - x346)^2) + 1 / sqrt((x32 - x67)^2 + (
    x172 - x207)^2 + (x312 - x347)^2) + 1 / sqrt((x32 - x68)^2 + (x172 - x208)^
    2 + (x312 - x348)^2) + 1 / sqrt((x32 - x69)^2 + (x172 - x209)^2 + (x312 -
    x349)^2) + 1 / sqrt((x32 - x70)^2 + (x172 - x210)^2 + (x312 - x350)^2) + 1
    / sqrt((x32 - x71)^2 + (x172 - x211)^2 + (x312 - x351)^2) + 1 / sqrt((x32
    - x72)^2 + (x172 - x212)^2 + (x312 - x352)^2) + 1 / sqrt((x32 - x73)^2 + (
    x172 - x213)^2 + (x312 - x353)^2) + 1 / sqrt((x32 - x74)^2 + (x172 - x214)^
    2 + (x312 - x354)^2) + 1 / sqrt((x32 - x75)^2 + (x172 - x215)^2 + (x312 -
    x355)^2) + 1 / sqrt((x32 - x76)^2 + (x172 - x216)^2 + (x312 - x356)^2) + 1
    / sqrt((x32 - x77)^2 + (x172 - x217)^2 + (x312 - x357)^2) + 1 / sqrt((x32
    - x78)^2 + (x172 - x218)^2 + (x312 - x358)^2) + 1 / sqrt((x32 - x79)^2 + (
    x172 - x219)^2 + (x312 - x359)^2) + 1 / sqrt((x32 - x80)^2 + (x172 - x220)^
    2 + (x312 - x360)^2) + 1 / sqrt((x32 - x81)^2 + (x172 - x221)^2 + (x312 -
    x361)^2) + 1 / sqrt((x32 - x82)^2 + (x172 - x222)^2 + (x312 - x362)^2) + 1
    / sqrt((x32 - x83)^2 + (x172 - x223)^2 + (x312 - x363)^2) + 1 / sqrt((x32
    - x84)^2 + (x172 - x224)^2 + (x312 - x364)^2) + 1 / sqrt((x32 - x85)^2 + (
    x172 - x225)^2 + (x312 - x365)^2) + 1 / sqrt((x32 - x86)^2 + (x172 - x226)^
    2 + (x312 - x366)^2) + 1 / sqrt((x32 - x87)^2 + (x172 - x227)^2 + (x312 -
    x367)^2) + 1 / sqrt((x32 - x88)^2 + (x172 - x228)^2 + (x312 - x368)^2) + 1
    / sqrt((x32 - x89)^2 + (x172 - x229)^2 + (x312 - x369)^2) + 1 / sqrt((x32
    - x90)^2 + (x172 - x230)^2 + (x312 - x370)^2) + 1 / sqrt((x32 - x91)^2 + (
    x172 - x231)^2 + (x312 - x371)^2) + 1 / sqrt((x32 - x92)^2 + (x172 - x232)^
    2 + (x312 - x372)^2) + 1 / sqrt((x32 - x93)^2 + (x172 - x233)^2 + (x312 -
    x373)^2) + 1 / sqrt((x32 - x94)^2 + (x172 - x234)^2 + (x312 - x374)^2) + 1
    / sqrt((x32 - x95)^2 + (x172 - x235)^2 + (x312 - x375)^2) + 1 / sqrt((x32
    - x96)^2 + (x172 - x236)^2 + (x312 - x376)^2) + 1 / sqrt((x32 - x97)^2 + (
    x172 - x237)^2 + (x312 - x377)^2) + 1 / sqrt((x32 - x98)^2 + (x172 - x238)^
    2 + (x312 - x378)^2) + 1 / sqrt((x32 - x99)^2 + (x172 - x239)^2 + (x312 -
    x379)^2) + 1 / sqrt((x32 - x100)^2 + (x172 - x240)^2 + (x312 - x380)^2) + 1
    / sqrt((x32 - x101)^2 + (x172 - x241)^2 + (x312 - x381)^2) + 1 / sqrt((x32
    - x102)^2 + (x172 - x242)^2 + (x312 - x382)^2) + 1 / sqrt((x32 - x103)^2
    + (x172 - x243)^2 + (x312 - x383)^2) + 1 / sqrt((x32 - x104)^2 + (x172 -
    x244)^2 + (x312 - x384)^2) + 1 / sqrt((x32 - x105)^2 + (x172 - x245)^2 + (
    x312 - x385)^2) + 1 / sqrt((x32 - x106)^2 + (x172 - x246)^2 + (x312 - x386)
    ^2) + 1 / sqrt((x32 - x107)^2 + (x172 - x247)^2 + (x312 - x387)^2) + 1 /
    sqrt((x32 - x108)^2 + (x172 - x248)^2 + (x312 - x388)^2) + 1 / sqrt((x32 -
    x109)^2 + (x172 - x249)^2 + (x312 - x389)^2) + 1 / sqrt((x32 - x110)^2 + (
    x172 - x250)^2 + (x312 - x390)^2) + 1 / sqrt((x32 - x111)^2 + (x172 - x251)
    ^2 + (x312 - x391)^2) + 1 / sqrt((x32 - x112)^2 + (x172 - x252)^2 + (x312
    - x392)^2) + 1 / sqrt((x32 - x113)^2 + (x172 - x253)^2 + (x312 - x393)^2)
    + 1 / sqrt((x32 - x114)^2 + (x172 - x254)^2 + (x312 - x394)^2) + 1 / sqrt(
    (x32 - x115)^2 + (x172 - x255)^2 + (x312 - x395)^2) + 1 / sqrt((x32 - x116)
    ^2 + (x172 - x256)^2 + (x312 - x396)^2) + 1 / sqrt((x32 - x117)^2 + (x172
    - x257)^2 + (x312 - x397)^2) + 1 / sqrt((x32 - x118)^2 + (x172 - x258)^2
    + (x312 - x398)^2) + 1 / sqrt((x32 - x119)^2 + (x172 - x259)^2 + (x312 -
    x399)^2) + 1 / sqrt((x32 - x120)^2 + (x172 - x260)^2 + (x312 - x400)^2) + 1
    / sqrt((x32 - x121)^2 + (x172 - x261)^2 + (x312 - x401)^2) + 1 / sqrt((x32
    - x122)^2 + (x172 - x262)^2 + (x312 - x402)^2) + 1 / sqrt((x32 - x123)^2
    + (x172 - x263)^2 + (x312 - x403)^2) + 1 / sqrt((x32 - x124)^2 + (x172 -
    x264)^2 + (x312 - x404)^2) + 1 / sqrt((x32 - x125)^2 + (x172 - x265)^2 + (
    x312 - x405)^2) + 1 / sqrt((x32 - x126)^2 + (x172 - x266)^2 + (x312 - x406)
    ^2) + 1 / sqrt((x32 - x127)^2 + (x172 - x267)^2 + (x312 - x407)^2) + 1 /
    sqrt((x32 - x128)^2 + (x172 - x268)^2 + (x312 - x408)^2) + 1 / sqrt((x32 -
    x129)^2 + (x172 - x269)^2 + (x312 - x409)^2) + 1 / sqrt((x32 - x130)^2 + (
    x172 - x270)^2 + (x312 - x410)^2) + 1 / sqrt((x32 - x131)^2 + (x172 - x271)
    ^2 + (x312 - x411)^2) + 1 / sqrt((x32 - x132)^2 + (x172 - x272)^2 + (x312
    - x412)^2) + 1 / sqrt((x32 - x133)^2 + (x172 - x273)^2 + (x312 - x413)^2)
    + 1 / sqrt((x32 - x134)^2 + (x172 - x274)^2 + (x312 - x414)^2) + 1 / sqrt(
    (x32 - x135)^2 + (x172 - x275)^2 + (x312 - x415)^2) + 1 / sqrt((x32 - x136)
    ^2 + (x172 - x276)^2 + (x312 - x416)^2) + 1 / sqrt((x32 - x137)^2 + (x172
    - x277)^2 + (x312 - x417)^2) + 1 / sqrt((x32 - x138)^2 + (x172 - x278)^2
    + (x312 - x418)^2) + 1 / sqrt((x32 - x139)^2 + (x172 - x279)^2 + (x312 -
    x419)^2) + 1 / sqrt((x32 - x140)^2 + (x172 - x280)^2 + (x312 - x420)^2) + 1
    / sqrt((x33 - x34)^2 + (x173 - x174)^2 + (x313 - x314)^2) + 1 / sqrt((x33
    - x35)^2 + (x173 - x175)^2 + (x313 - x315)^2) + 1 / sqrt((x33 - x36)^2 + (
    x173 - x176)^2 + (x313 - x316)^2) + 1 / sqrt((x33 - x37)^2 + (x173 - x177)^
    2 + (x313 - x317)^2) + 1 / sqrt((x33 - x38)^2 + (x173 - x178)^2 + (x313 -
    x318)^2) + 1 / sqrt((x33 - x39)^2 + (x173 - x179)^2 + (x313 - x319)^2) + 1
    / sqrt((x33 - x40)^2 + (x173 - x180)^2 + (x313 - x320)^2) + 1 / sqrt((x33
    - x41)^2 + (x173 - x181)^2 + (x313 - x321)^2) + 1 / sqrt((x33 - x42)^2 + (
    x173 - x182)^2 + (x313 - x322)^2) + 1 / sqrt((x33 - x43)^2 + (x173 - x183)^
    2 + (x313 - x323)^2) + 1 / sqrt((x33 - x44)^2 + (x173 - x184)^2 + (x313 -
    x324)^2) + 1 / sqrt((x33 - x45)^2 + (x173 - x185)^2 + (x313 - x325)^2) + 1
    / sqrt((x33 - x46)^2 + (x173 - x186)^2 + (x313 - x326)^2) + 1 / sqrt((x33
    - x47)^2 + (x173 - x187)^2 + (x313 - x327)^2) + 1 / sqrt((x33 - x48)^2 + (
    x173 - x188)^2 + (x313 - x328)^2) + 1 / sqrt((x33 - x49)^2 + (x173 - x189)^
    2 + (x313 - x329)^2) + 1 / sqrt((x33 - x50)^2 + (x173 - x190)^2 + (x313 -
    x330)^2) + 1 / sqrt((x33 - x51)^2 + (x173 - x191)^2 + (x313 - x331)^2) + 1
    / sqrt((x33 - x52)^2 + (x173 - x192)^2 + (x313 - x332)^2) + 1 / sqrt((x33
    - x53)^2 + (x173 - x193)^2 + (x313 - x333)^2) + 1 / sqrt((x33 - x54)^2 + (
    x173 - x194)^2 + (x313 - x334)^2) + 1 / sqrt((x33 - x55)^2 + (x173 - x195)^
    2 + (x313 - x335)^2) + 1 / sqrt((x33 - x56)^2 + (x173 - x196)^2 + (x313 -
    x336)^2) + 1 / sqrt((x33 - x57)^2 + (x173 - x197)^2 + (x313 - x337)^2) + 1
    / sqrt((x33 - x58)^2 + (x173 - x198)^2 + (x313 - x338)^2) + 1 / sqrt((x33
    - x59)^2 + (x173 - x199)^2 + (x313 - x339)^2) + 1 / sqrt((x33 - x60)^2 + (
    x173 - x200)^2 + (x313 - x340)^2) + 1 / sqrt((x33 - x61)^2 + (x173 - x201)^
    2 + (x313 - x341)^2) + 1 / sqrt((x33 - x62)^2 + (x173 - x202)^2 + (x313 -
    x342)^2) + 1 / sqrt((x33 - x63)^2 + (x173 - x203)^2 + (x313 - x343)^2) + 1
    / sqrt((x33 - x64)^2 + (x173 - x204)^2 + (x313 - x344)^2) + 1 / sqrt((x33
    - x65)^2 + (x173 - x205)^2 + (x313 - x345)^2) + 1 / sqrt((x33 - x66)^2 + (
    x173 - x206)^2 + (x313 - x346)^2) + 1 / sqrt((x33 - x67)^2 + (x173 - x207)^
    2 + (x313 - x347)^2) + 1 / sqrt((x33 - x68)^2 + (x173 - x208)^2 + (x313 -
    x348)^2) + 1 / sqrt((x33 - x69)^2 + (x173 - x209)^2 + (x313 - x349)^2) + 1
    / sqrt((x33 - x70)^2 + (x173 - x210)^2 + (x313 - x350)^2) + 1 / sqrt((x33
    - x71)^2 + (x173 - x211)^2 + (x313 - x351)^2) + 1 / sqrt((x33 - x72)^2 + (
    x173 - x212)^2 + (x313 - x352)^2) + 1 / sqrt((x33 - x73)^2 + (x173 - x213)^
    2 + (x313 - x353)^2) + 1 / sqrt((x33 - x74)^2 + (x173 - x214)^2 + (x313 -
    x354)^2) + 1 / sqrt((x33 - x75)^2 + (x173 - x215)^2 + (x313 - x355)^2) + 1
    / sqrt((x33 - x76)^2 + (x173 - x216)^2 + (x313 - x356)^2) + 1 / sqrt((x33
    - x77)^2 + (x173 - x217)^2 + (x313 - x357)^2) + 1 / sqrt((x33 - x78)^2 + (
    x173 - x218)^2 + (x313 - x358)^2) + 1 / sqrt((x33 - x79)^2 + (x173 - x219)^
    2 + (x313 - x359)^2) + 1 / sqrt((x33 - x80)^2 + (x173 - x220)^2 + (x313 -
    x360)^2) + 1 / sqrt((x33 - x81)^2 + (x173 - x221)^2 + (x313 - x361)^2) + 1
    / sqrt((x33 - x82)^2 + (x173 - x222)^2 + (x313 - x362)^2) + 1 / sqrt((x33
    - x83)^2 + (x173 - x223)^2 + (x313 - x363)^2) + 1 / sqrt((x33 - x84)^2 + (
    x173 - x224)^2 + (x313 - x364)^2) + 1 / sqrt((x33 - x85)^2 + (x173 - x225)^
    2 + (x313 - x365)^2) + 1 / sqrt((x33 - x86)^2 + (x173 - x226)^2 + (x313 -
    x366)^2) + 1 / sqrt((x33 - x87)^2 + (x173 - x227)^2 + (x313 - x367)^2) + 1
    / sqrt((x33 - x88)^2 + (x173 - x228)^2 + (x313 - x368)^2) + 1 / sqrt((x33
    - x89)^2 + (x173 - x229)^2 + (x313 - x369)^2) + 1 / sqrt((x33 - x90)^2 + (
    x173 - x230)^2 + (x313 - x370)^2) + 1 / sqrt((x33 - x91)^2 + (x173 - x231)^
    2 + (x313 - x371)^2) + 1 / sqrt((x33 - x92)^2 + (x173 - x232)^2 + (x313 -
    x372)^2) + 1 / sqrt((x33 - x93)^2 + (x173 - x233)^2 + (x313 - x373)^2) + 1
    / sqrt((x33 - x94)^2 + (x173 - x234)^2 + (x313 - x374)^2) + 1 / sqrt((x33
    - x95)^2 + (x173 - x235)^2 + (x313 - x375)^2) + 1 / sqrt((x33 - x96)^2 + (
    x173 - x236)^2 + (x313 - x376)^2) + 1 / sqrt((x33 - x97)^2 + (x173 - x237)^
    2 + (x313 - x377)^2) + 1 / sqrt((x33 - x98)^2 + (x173 - x238)^2 + (x313 -
    x378)^2) + 1 / sqrt((x33 - x99)^2 + (x173 - x239)^2 + (x313 - x379)^2) + 1
    / sqrt((x33 - x100)^2 + (x173 - x240)^2 + (x313 - x380)^2) + 1 / sqrt((x33
    - x101)^2 + (x173 - x241)^2 + (x313 - x381)^2) + 1 / sqrt((x33 - x102)^2
    + (x173 - x242)^2 + (x313 - x382)^2) + 1 / sqrt((x33 - x103)^2 + (x173 -
    x243)^2 + (x313 - x383)^2) + 1 / sqrt((x33 - x104)^2 + (x173 - x244)^2 + (
    x313 - x384)^2) + 1 / sqrt((x33 - x105)^2 + (x173 - x245)^2 + (x313 - x385)
    ^2) + 1 / sqrt((x33 - x106)^2 + (x173 - x246)^2 + (x313 - x386)^2) + 1 /
    sqrt((x33 - x107)^2 + (x173 - x247)^2 + (x313 - x387)^2) + 1 / sqrt((x33 -
    x108)^2 + (x173 - x248)^2 + (x313 - x388)^2) + 1 / sqrt((x33 - x109)^2 + (
    x173 - x249)^2 + (x313 - x389)^2) + 1 / sqrt((x33 - x110)^2 + (x173 - x250)
    ^2 + (x313 - x390)^2) + 1 / sqrt((x33 - x111)^2 + (x173 - x251)^2 + (x313
    - x391)^2) + 1 / sqrt((x33 - x112)^2 + (x173 - x252)^2 + (x313 - x392)^2)
    + 1 / sqrt((x33 - x113)^2 + (x173 - x253)^2 + (x313 - x393)^2) + 1 / sqrt(
    (x33 - x114)^2 + (x173 - x254)^2 + (x313 - x394)^2) + 1 / sqrt((x33 - x115)
    ^2 + (x173 - x255)^2 + (x313 - x395)^2) + 1 / sqrt((x33 - x116)^2 + (x173
    - x256)^2 + (x313 - x396)^2) + 1 / sqrt((x33 - x117)^2 + (x173 - x257)^2
    + (x313 - x397)^2) + 1 / sqrt((x33 - x118)^2 + (x173 - x258)^2 + (x313 -
    x398)^2) + 1 / sqrt((x33 - x119)^2 + (x173 - x259)^2 + (x313 - x399)^2) + 1
    / sqrt((x33 - x120)^2 + (x173 - x260)^2 + (x313 - x400)^2) + 1 / sqrt((x33
    - x121)^2 + (x173 - x261)^2 + (x313 - x401)^2) + 1 / sqrt((x33 - x122)^2
    + (x173 - x262)^2 + (x313 - x402)^2) + 1 / sqrt((x33 - x123)^2 + (x173 -
    x263)^2 + (x313 - x403)^2) + 1 / sqrt((x33 - x124)^2 + (x173 - x264)^2 + (
    x313 - x404)^2) + 1 / sqrt((x33 - x125)^2 + (x173 - x265)^2 + (x313 - x405)
    ^2) + 1 / sqrt((x33 - x126)^2 + (x173 - x266)^2 + (x313 - x406)^2) + 1 /
    sqrt((x33 - x127)^2 + (x173 - x267)^2 + (x313 - x407)^2) + 1 / sqrt((x33 -
    x128)^2 + (x173 - x268)^2 + (x313 - x408)^2) + 1 / sqrt((x33 - x129)^2 + (
    x173 - x269)^2 + (x313 - x409)^2) + 1 / sqrt((x33 - x130)^2 + (x173 - x270)
    ^2 + (x313 - x410)^2) + 1 / sqrt((x33 - x131)^2 + (x173 - x271)^2 + (x313
    - x411)^2) + 1 / sqrt((x33 - x132)^2 + (x173 - x272)^2 + (x313 - x412)^2)
    + 1 / sqrt((x33 - x133)^2 + (x173 - x273)^2 + (x313 - x413)^2) + 1 / sqrt(
    (x33 - x134)^2 + (x173 - x274)^2 + (x313 - x414)^2) + 1 / sqrt((x33 - x135)
    ^2 + (x173 - x275)^2 + (x313 - x415)^2) + 1 / sqrt((x33 - x136)^2 + (x173
    - x276)^2 + (x313 - x416)^2) + 1 / sqrt((x33 - x137)^2 + (x173 - x277)^2
    + (x313 - x417)^2) + 1 / sqrt((x33 - x138)^2 + (x173 - x278)^2 + (x313 -
    x418)^2) + 1 / sqrt((x33 - x139)^2 + (x173 - x279)^2 + (x313 - x419)^2) + 1
    / sqrt((x33 - x140)^2 + (x173 - x280)^2 + (x313 - x420)^2) + 1 / sqrt((x34
    - x35)^2 + (x174 - x175)^2 + (x314 - x315)^2) + 1 / sqrt((x34 - x36)^2 + (
    x174 - x176)^2 + (x314 - x316)^2) + 1 / sqrt((x34 - x37)^2 + (x174 - x177)^
    2 + (x314 - x317)^2) + 1 / sqrt((x34 - x38)^2 + (x174 - x178)^2 + (x314 -
    x318)^2) + 1 / sqrt((x34 - x39)^2 + (x174 - x179)^2 + (x314 - x319)^2) + 1
    / sqrt((x34 - x40)^2 + (x174 - x180)^2 + (x314 - x320)^2) + 1 / sqrt((x34
    - x41)^2 + (x174 - x181)^2 + (x314 - x321)^2) + 1 / sqrt((x34 - x42)^2 + (
    x174 - x182)^2 + (x314 - x322)^2) + 1 / sqrt((x34 - x43)^2 + (x174 - x183)^
    2 + (x314 - x323)^2) + 1 / sqrt((x34 - x44)^2 + (x174 - x184)^2 + (x314 -
    x324)^2) + 1 / sqrt((x34 - x45)^2 + (x174 - x185)^2 + (x314 - x325)^2) + 1
    / sqrt((x34 - x46)^2 + (x174 - x186)^2 + (x314 - x326)^2) + 1 / sqrt((x34
    - x47)^2 + (x174 - x187)^2 + (x314 - x327)^2) + 1 / sqrt((x34 - x48)^2 + (
    x174 - x188)^2 + (x314 - x328)^2) + 1 / sqrt((x34 - x49)^2 + (x174 - x189)^
    2 + (x314 - x329)^2) + 1 / sqrt((x34 - x50)^2 + (x174 - x190)^2 + (x314 -
    x330)^2) + 1 / sqrt((x34 - x51)^2 + (x174 - x191)^2 + (x314 - x331)^2) + 1
    / sqrt((x34 - x52)^2 + (x174 - x192)^2 + (x314 - x332)^2) + 1 / sqrt((x34
    - x53)^2 + (x174 - x193)^2 + (x314 - x333)^2) + 1 / sqrt((x34 - x54)^2 + (
    x174 - x194)^2 + (x314 - x334)^2) + 1 / sqrt((x34 - x55)^2 + (x174 - x195)^
    2 + (x314 - x335)^2) + 1 / sqrt((x34 - x56)^2 + (x174 - x196)^2 + (x314 -
    x336)^2) + 1 / sqrt((x34 - x57)^2 + (x174 - x197)^2 + (x314 - x337)^2) + 1
    / sqrt((x34 - x58)^2 + (x174 - x198)^2 + (x314 - x338)^2) + 1 / sqrt((x34
    - x59)^2 + (x174 - x199)^2 + (x314 - x339)^2) + 1 / sqrt((x34 - x60)^2 + (
    x174 - x200)^2 + (x314 - x340)^2) + 1 / sqrt((x34 - x61)^2 + (x174 - x201)^
    2 + (x314 - x341)^2) + 1 / sqrt((x34 - x62)^2 + (x174 - x202)^2 + (x314 -
    x342)^2) + 1 / sqrt((x34 - x63)^2 + (x174 - x203)^2 + (x314 - x343)^2) + 1
    / sqrt((x34 - x64)^2 + (x174 - x204)^2 + (x314 - x344)^2) + 1 / sqrt((x34
    - x65)^2 + (x174 - x205)^2 + (x314 - x345)^2) + 1 / sqrt((x34 - x66)^2 + (
    x174 - x206)^2 + (x314 - x346)^2) + 1 / sqrt((x34 - x67)^2 + (x174 - x207)^
    2 + (x314 - x347)^2) + 1 / sqrt((x34 - x68)^2 + (x174 - x208)^2 + (x314 -
    x348)^2) + 1 / sqrt((x34 - x69)^2 + (x174 - x209)^2 + (x314 - x349)^2) + 1
    / sqrt((x34 - x70)^2 + (x174 - x210)^2 + (x314 - x350)^2) + 1 / sqrt((x34
    - x71)^2 + (x174 - x211)^2 + (x314 - x351)^2) + 1 / sqrt((x34 - x72)^2 + (
    x174 - x212)^2 + (x314 - x352)^2) + 1 / sqrt((x34 - x73)^2 + (x174 - x213)^
    2 + (x314 - x353)^2) + 1 / sqrt((x34 - x74)^2 + (x174 - x214)^2 + (x314 -
    x354)^2) + 1 / sqrt((x34 - x75)^2 + (x174 - x215)^2 + (x314 - x355)^2) + 1
    / sqrt((x34 - x76)^2 + (x174 - x216)^2 + (x314 - x356)^2) + 1 / sqrt((x34
    - x77)^2 + (x174 - x217)^2 + (x314 - x357)^2) + 1 / sqrt((x34 - x78)^2 + (
    x174 - x218)^2 + (x314 - x358)^2) + 1 / sqrt((x34 - x79)^2 + (x174 - x219)^
    2 + (x314 - x359)^2) + 1 / sqrt((x34 - x80)^2 + (x174 - x220)^2 + (x314 -
    x360)^2) + 1 / sqrt((x34 - x81)^2 + (x174 - x221)^2 + (x314 - x361)^2) + 1
    / sqrt((x34 - x82)^2 + (x174 - x222)^2 + (x314 - x362)^2) + 1 / sqrt((x34
    - x83)^2 + (x174 - x223)^2 + (x314 - x363)^2) + 1 / sqrt((x34 - x84)^2 + (
    x174 - x224)^2 + (x314 - x364)^2) + 1 / sqrt((x34 - x85)^2 + (x174 - x225)^
    2 + (x314 - x365)^2) + 1 / sqrt((x34 - x86)^2 + (x174 - x226)^2 + (x314 -
    x366)^2) + 1 / sqrt((x34 - x87)^2 + (x174 - x227)^2 + (x314 - x367)^2) + 1
    / sqrt((x34 - x88)^2 + (x174 - x228)^2 + (x314 - x368)^2) + 1 / sqrt((x34
    - x89)^2 + (x174 - x229)^2 + (x314 - x369)^2) + 1 / sqrt((x34 - x90)^2 + (
    x174 - x230)^2 + (x314 - x370)^2) + 1 / sqrt((x34 - x91)^2 + (x174 - x231)^
    2 + (x314 - x371)^2) + 1 / sqrt((x34 - x92)^2 + (x174 - x232)^2 + (x314 -
    x372)^2) + 1 / sqrt((x34 - x93)^2 + (x174 - x233)^2 + (x314 - x373)^2) + 1
    / sqrt((x34 - x94)^2 + (x174 - x234)^2 + (x314 - x374)^2) + 1 / sqrt((x34
    - x95)^2 + (x174 - x235)^2 + (x314 - x375)^2) + 1 / sqrt((x34 - x96)^2 + (
    x174 - x236)^2 + (x314 - x376)^2) + 1 / sqrt((x34 - x97)^2 + (x174 - x237)^
    2 + (x314 - x377)^2) + 1 / sqrt((x34 - x98)^2 + (x174 - x238)^2 + (x314 -
    x378)^2) + 1 / sqrt((x34 - x99)^2 + (x174 - x239)^2 + (x314 - x379)^2) + 1
    / sqrt((x34 - x100)^2 + (x174 - x240)^2 + (x314 - x380)^2) + 1 / sqrt((x34
    - x101)^2 + (x174 - x241)^2 + (x314 - x381)^2) + 1 / sqrt((x34 - x102)^2
    + (x174 - x242)^2 + (x314 - x382)^2) + 1 / sqrt((x34 - x103)^2 + (x174 -
    x243)^2 + (x314 - x383)^2) + 1 / sqrt((x34 - x104)^2 + (x174 - x244)^2 + (
    x314 - x384)^2) + 1 / sqrt((x34 - x105)^2 + (x174 - x245)^2 + (x314 - x385)
    ^2) + 1 / sqrt((x34 - x106)^2 + (x174 - x246)^2 + (x314 - x386)^2) + 1 /
    sqrt((x34 - x107)^2 + (x174 - x247)^2 + (x314 - x387)^2) + 1 / sqrt((x34 -
    x108)^2 + (x174 - x248)^2 + (x314 - x388)^2) + 1 / sqrt((x34 - x109)^2 + (
    x174 - x249)^2 + (x314 - x389)^2) + 1 / sqrt((x34 - x110)^2 + (x174 - x250)
    ^2 + (x314 - x390)^2) + 1 / sqrt((x34 - x111)^2 + (x174 - x251)^2 + (x314
    - x391)^2) + 1 / sqrt((x34 - x112)^2 + (x174 - x252)^2 + (x314 - x392)^2)
    + 1 / sqrt((x34 - x113)^2 + (x174 - x253)^2 + (x314 - x393)^2) + 1 / sqrt(
    (x34 - x114)^2 + (x174 - x254)^2 + (x314 - x394)^2) + 1 / sqrt((x34 - x115)
    ^2 + (x174 - x255)^2 + (x314 - x395)^2) + 1 / sqrt((x34 - x116)^2 + (x174
    - x256)^2 + (x314 - x396)^2) + 1 / sqrt((x34 - x117)^2 + (x174 - x257)^2
    + (x314 - x397)^2) + 1 / sqrt((x34 - x118)^2 + (x174 - x258)^2 + (x314 -
    x398)^2) + 1 / sqrt((x34 - x119)^2 + (x174 - x259)^2 + (x314 - x399)^2) + 1
    / sqrt((x34 - x120)^2 + (x174 - x260)^2 + (x314 - x400)^2) + 1 / sqrt((x34
    - x121)^2 + (x174 - x261)^2 + (x314 - x401)^2) + 1 / sqrt((x34 - x122)^2
    + (x174 - x262)^2 + (x314 - x402)^2) + 1 / sqrt((x34 - x123)^2 + (x174 -
    x263)^2 + (x314 - x403)^2) + 1 / sqrt((x34 - x124)^2 + (x174 - x264)^2 + (
    x314 - x404)^2) + 1 / sqrt((x34 - x125)^2 + (x174 - x265)^2 + (x314 - x405)
    ^2) + 1 / sqrt((x34 - x126)^2 + (x174 - x266)^2 + (x314 - x406)^2) + 1 /
    sqrt((x34 - x127)^2 + (x174 - x267)^2 + (x314 - x407)^2) + 1 / sqrt((x34 -
    x128)^2 + (x174 - x268)^2 + (x314 - x408)^2) + 1 / sqrt((x34 - x129)^2 + (
    x174 - x269)^2 + (x314 - x409)^2) + 1 / sqrt((x34 - x130)^2 + (x174 - x270)
    ^2 + (x314 - x410)^2) + 1 / sqrt((x34 - x131)^2 + (x174 - x271)^2 + (x314
    - x411)^2) + 1 / sqrt((x34 - x132)^2 + (x174 - x272)^2 + (x314 - x412)^2)
    + 1 / sqrt((x34 - x133)^2 + (x174 - x273)^2 + (x314 - x413)^2) + 1 / sqrt(
    (x34 - x134)^2 + (x174 - x274)^2 + (x314 - x414)^2) + 1 / sqrt((x34 - x135)
    ^2 + (x174 - x275)^2 + (x314 - x415)^2) + 1 / sqrt((x34 - x136)^2 + (x174
    - x276)^2 + (x314 - x416)^2) + 1 / sqrt((x34 - x137)^2 + (x174 - x277)^2
    + (x314 - x417)^2) + 1 / sqrt((x34 - x138)^2 + (x174 - x278)^2 + (x314 -
    x418)^2) + 1 / sqrt((x34 - x139)^2 + (x174 - x279)^2 + (x314 - x419)^2) + 1
    / sqrt((x34 - x140)^2 + (x174 - x280)^2 + (x314 - x420)^2) + 1 / sqrt((x35
    - x36)^2 + (x175 - x176)^2 + (x315 - x316)^2) + 1 / sqrt((x35 - x37)^2 + (
    x175 - x177)^2 + (x315 - x317)^2) + 1 / sqrt((x35 - x38)^2 + (x175 - x178)^
    2 + (x315 - x318)^2) + 1 / sqrt((x35 - x39)^2 + (x175 - x179)^2 + (x315 -
    x319)^2) + 1 / sqrt((x35 - x40)^2 + (x175 - x180)^2 + (x315 - x320)^2) + 1
    / sqrt((x35 - x41)^2 + (x175 - x181)^2 + (x315 - x321)^2) + 1 / sqrt((x35
    - x42)^2 + (x175 - x182)^2 + (x315 - x322)^2) + 1 / sqrt((x35 - x43)^2 + (
    x175 - x183)^2 + (x315 - x323)^2) + 1 / sqrt((x35 - x44)^2 + (x175 - x184)^
    2 + (x315 - x324)^2) + 1 / sqrt((x35 - x45)^2 + (x175 - x185)^2 + (x315 -
    x325)^2) + 1 / sqrt((x35 - x46)^2 + (x175 - x186)^2 + (x315 - x326)^2) + 1
    / sqrt((x35 - x47)^2 + (x175 - x187)^2 + (x315 - x327)^2) + 1 / sqrt((x35
    - x48)^2 + (x175 - x188)^2 + (x315 - x328)^2) + 1 / sqrt((x35 - x49)^2 + (
    x175 - x189)^2 + (x315 - x329)^2) + 1 / sqrt((x35 - x50)^2 + (x175 - x190)^
    2 + (x315 - x330)^2) + 1 / sqrt((x35 - x51)^2 + (x175 - x191)^2 + (x315 -
    x331)^2) + 1 / sqrt((x35 - x52)^2 + (x175 - x192)^2 + (x315 - x332)^2) + 1
    / sqrt((x35 - x53)^2 + (x175 - x193)^2 + (x315 - x333)^2) + 1 / sqrt((x35
    - x54)^2 + (x175 - x194)^2 + (x315 - x334)^2) + 1 / sqrt((x35 - x55)^2 + (
    x175 - x195)^2 + (x315 - x335)^2) + 1 / sqrt((x35 - x56)^2 + (x175 - x196)^
    2 + (x315 - x336)^2) + 1 / sqrt((x35 - x57)^2 + (x175 - x197)^2 + (x315 -
    x337)^2) + 1 / sqrt((x35 - x58)^2 + (x175 - x198)^2 + (x315 - x338)^2) + 1
    / sqrt((x35 - x59)^2 + (x175 - x199)^2 + (x315 - x339)^2) + 1 / sqrt((x35
    - x60)^2 + (x175 - x200)^2 + (x315 - x340)^2) + 1 / sqrt((x35 - x61)^2 + (
    x175 - x201)^2 + (x315 - x341)^2) + 1 / sqrt((x35 - x62)^2 + (x175 - x202)^
    2 + (x315 - x342)^2) + 1 / sqrt((x35 - x63)^2 + (x175 - x203)^2 + (x315 -
    x343)^2) + 1 / sqrt((x35 - x64)^2 + (x175 - x204)^2 + (x315 - x344)^2) + 1
    / sqrt((x35 - x65)^2 + (x175 - x205)^2 + (x315 - x345)^2) + 1 / sqrt((x35
    - x66)^2 + (x175 - x206)^2 + (x315 - x346)^2) + 1 / sqrt((x35 - x67)^2 + (
    x175 - x207)^2 + (x315 - x347)^2) + 1 / sqrt((x35 - x68)^2 + (x175 - x208)^
    2 + (x315 - x348)^2) + 1 / sqrt((x35 - x69)^2 + (x175 - x209)^2 + (x315 -
    x349)^2) + 1 / sqrt((x35 - x70)^2 + (x175 - x210)^2 + (x315 - x350)^2) + 1
    / sqrt((x35 - x71)^2 + (x175 - x211)^2 + (x315 - x351)^2) + 1 / sqrt((x35
    - x72)^2 + (x175 - x212)^2 + (x315 - x352)^2) + 1 / sqrt((x35 - x73)^2 + (
    x175 - x213)^2 + (x315 - x353)^2) + 1 / sqrt((x35 - x74)^2 + (x175 - x214)^
    2 + (x315 - x354)^2) + 1 / sqrt((x35 - x75)^2 + (x175 - x215)^2 + (x315 -
    x355)^2) + 1 / sqrt((x35 - x76)^2 + (x175 - x216)^2 + (x315 - x356)^2) + 1
    / sqrt((x35 - x77)^2 + (x175 - x217)^2 + (x315 - x357)^2) + 1 / sqrt((x35
    - x78)^2 + (x175 - x218)^2 + (x315 - x358)^2) + 1 / sqrt((x35 - x79)^2 + (
    x175 - x219)^2 + (x315 - x359)^2) + 1 / sqrt((x35 - x80)^2 + (x175 - x220)^
    2 + (x315 - x360)^2) + 1 / sqrt((x35 - x81)^2 + (x175 - x221)^2 + (x315 -
    x361)^2) + 1 / sqrt((x35 - x82)^2 + (x175 - x222)^2 + (x315 - x362)^2) + 1
    / sqrt((x35 - x83)^2 + (x175 - x223)^2 + (x315 - x363)^2) + 1 / sqrt((x35
    - x84)^2 + (x175 - x224)^2 + (x315 - x364)^2) + 1 / sqrt((x35 - x85)^2 + (
    x175 - x225)^2 + (x315 - x365)^2) + 1 / sqrt((x35 - x86)^2 + (x175 - x226)^
    2 + (x315 - x366)^2) + 1 / sqrt((x35 - x87)^2 + (x175 - x227)^2 + (x315 -
    x367)^2) + 1 / sqrt((x35 - x88)^2 + (x175 - x228)^2 + (x315 - x368)^2) + 1
    / sqrt((x35 - x89)^2 + (x175 - x229)^2 + (x315 - x369)^2) + 1 / sqrt((x35
    - x90)^2 + (x175 - x230)^2 + (x315 - x370)^2) + 1 / sqrt((x35 - x91)^2 + (
    x175 - x231)^2 + (x315 - x371)^2) + 1 / sqrt((x35 - x92)^2 + (x175 - x232)^
    2 + (x315 - x372)^2) + 1 / sqrt((x35 - x93)^2 + (x175 - x233)^2 + (x315 -
    x373)^2) + 1 / sqrt((x35 - x94)^2 + (x175 - x234)^2 + (x315 - x374)^2) + 1
    / sqrt((x35 - x95)^2 + (x175 - x235)^2 + (x315 - x375)^2) + 1 / sqrt((x35
    - x96)^2 + (x175 - x236)^2 + (x315 - x376)^2) + 1 / sqrt((x35 - x97)^2 + (
    x175 - x237)^2 + (x315 - x377)^2) + 1 / sqrt((x35 - x98)^2 + (x175 - x238)^
    2 + (x315 - x378)^2) + 1 / sqrt((x35 - x99)^2 + (x175 - x239)^2 + (x315 -
    x379)^2) + 1 / sqrt((x35 - x100)^2 + (x175 - x240)^2 + (x315 - x380)^2) + 1
    / sqrt((x35 - x101)^2 + (x175 - x241)^2 + (x315 - x381)^2) + 1 / sqrt((x35
    - x102)^2 + (x175 - x242)^2 + (x315 - x382)^2) + 1 / sqrt((x35 - x103)^2
    + (x175 - x243)^2 + (x315 - x383)^2) + 1 / sqrt((x35 - x104)^2 + (x175 -
    x244)^2 + (x315 - x384)^2) + 1 / sqrt((x35 - x105)^2 + (x175 - x245)^2 + (
    x315 - x385)^2) + 1 / sqrt((x35 - x106)^2 + (x175 - x246)^2 + (x315 - x386)
    ^2) + 1 / sqrt((x35 - x107)^2 + (x175 - x247)^2 + (x315 - x387)^2) + 1 /
    sqrt((x35 - x108)^2 + (x175 - x248)^2 + (x315 - x388)^2) + 1 / sqrt((x35 -
    x109)^2 + (x175 - x249)^2 + (x315 - x389)^2) + 1 / sqrt((x35 - x110)^2 + (
    x175 - x250)^2 + (x315 - x390)^2) + 1 / sqrt((x35 - x111)^2 + (x175 - x251)
    ^2 + (x315 - x391)^2) + 1 / sqrt((x35 - x112)^2 + (x175 - x252)^2 + (x315
    - x392)^2) + 1 / sqrt((x35 - x113)^2 + (x175 - x253)^2 + (x315 - x393)^2)
    + 1 / sqrt((x35 - x114)^2 + (x175 - x254)^2 + (x315 - x394)^2) + 1 / sqrt(
    (x35 - x115)^2 + (x175 - x255)^2 + (x315 - x395)^2) + 1 / sqrt((x35 - x116)
    ^2 + (x175 - x256)^2 + (x315 - x396)^2) + 1 / sqrt((x35 - x117)^2 + (x175
    - x257)^2 + (x315 - x397)^2) + 1 / sqrt((x35 - x118)^2 + (x175 - x258)^2
    + (x315 - x398)^2) + 1 / sqrt((x35 - x119)^2 + (x175 - x259)^2 + (x315 -
    x399)^2) + 1 / sqrt((x35 - x120)^2 + (x175 - x260)^2 + (x315 - x400)^2) + 1
    / sqrt((x35 - x121)^2 + (x175 - x261)^2 + (x315 - x401)^2) + 1 / sqrt((x35
    - x122)^2 + (x175 - x262)^2 + (x315 - x402)^2) + 1 / sqrt((x35 - x123)^2
    + (x175 - x263)^2 + (x315 - x403)^2) + 1 / sqrt((x35 - x124)^2 + (x175 -
    x264)^2 + (x315 - x404)^2) + 1 / sqrt((x35 - x125)^2 + (x175 - x265)^2 + (
    x315 - x405)^2) + 1 / sqrt((x35 - x126)^2 + (x175 - x266)^2 + (x315 - x406)
    ^2) + 1 / sqrt((x35 - x127)^2 + (x175 - x267)^2 + (x315 - x407)^2) + 1 /
    sqrt((x35 - x128)^2 + (x175 - x268)^2 + (x315 - x408)^2) + 1 / sqrt((x35 -
    x129)^2 + (x175 - x269)^2 + (x315 - x409)^2) + 1 / sqrt((x35 - x130)^2 + (
    x175 - x270)^2 + (x315 - x410)^2) + 1 / sqrt((x35 - x131)^2 + (x175 - x271)
    ^2 + (x315 - x411)^2) + 1 / sqrt((x35 - x132)^2 + (x175 - x272)^2 + (x315
    - x412)^2) + 1 / sqrt((x35 - x133)^2 + (x175 - x273)^2 + (x315 - x413)^2)
    + 1 / sqrt((x35 - x134)^2 + (x175 - x274)^2 + (x315 - x414)^2) + 1 / sqrt(
    (x35 - x135)^2 + (x175 - x275)^2 + (x315 - x415)^2) + 1 / sqrt((x35 - x136)
    ^2 + (x175 - x276)^2 + (x315 - x416)^2) + 1 / sqrt((x35 - x137)^2 + (x175
    - x277)^2 + (x315 - x417)^2) + 1 / sqrt((x35 - x138)^2 + (x175 - x278)^2
    + (x315 - x418)^2) + 1 / sqrt((x35 - x139)^2 + (x175 - x279)^2 + (x315 -
    x419)^2) + 1 / sqrt((x35 - x140)^2 + (x175 - x280)^2 + (x315 - x420)^2) + 1
    / sqrt((x36 - x37)^2 + (x176 - x177)^2 + (x316 - x317)^2) + 1 / sqrt((x36
    - x38)^2 + (x176 - x178)^2 + (x316 - x318)^2) + 1 / sqrt((x36 - x39)^2 + (
    x176 - x179)^2 + (x316 - x319)^2) + 1 / sqrt((x36 - x40)^2 + (x176 - x180)^
    2 + (x316 - x320)^2) + 1 / sqrt((x36 - x41)^2 + (x176 - x181)^2 + (x316 -
    x321)^2) + 1 / sqrt((x36 - x42)^2 + (x176 - x182)^2 + (x316 - x322)^2) + 1
    / sqrt((x36 - x43)^2 + (x176 - x183)^2 + (x316 - x323)^2) + 1 / sqrt((x36
    - x44)^2 + (x176 - x184)^2 + (x316 - x324)^2) + 1 / sqrt((x36 - x45)^2 + (
    x176 - x185)^2 + (x316 - x325)^2) + 1 / sqrt((x36 - x46)^2 + (x176 - x186)^
    2 + (x316 - x326)^2) + 1 / sqrt((x36 - x47)^2 + (x176 - x187)^2 + (x316 -
    x327)^2) + 1 / sqrt((x36 - x48)^2 + (x176 - x188)^2 + (x316 - x328)^2) + 1
    / sqrt((x36 - x49)^2 + (x176 - x189)^2 + (x316 - x329)^2) + 1 / sqrt((x36
    - x50)^2 + (x176 - x190)^2 + (x316 - x330)^2) + 1 / sqrt((x36 - x51)^2 + (
    x176 - x191)^2 + (x316 - x331)^2) + 1 / sqrt((x36 - x52)^2 + (x176 - x192)^
    2 + (x316 - x332)^2) + 1 / sqrt((x36 - x53)^2 + (x176 - x193)^2 + (x316 -
    x333)^2) + 1 / sqrt((x36 - x54)^2 + (x176 - x194)^2 + (x316 - x334)^2) + 1
    / sqrt((x36 - x55)^2 + (x176 - x195)^2 + (x316 - x335)^2) + 1 / sqrt((x36
    - x56)^2 + (x176 - x196)^2 + (x316 - x336)^2) + 1 / sqrt((x36 - x57)^2 + (
    x176 - x197)^2 + (x316 - x337)^2) + 1 / sqrt((x36 - x58)^2 + (x176 - x198)^
    2 + (x316 - x338)^2) + 1 / sqrt((x36 - x59)^2 + (x176 - x199)^2 + (x316 -
    x339)^2) + 1 / sqrt((x36 - x60)^2 + (x176 - x200)^2 + (x316 - x340)^2) + 1
    / sqrt((x36 - x61)^2 + (x176 - x201)^2 + (x316 - x341)^2) + 1 / sqrt((x36
    - x62)^2 + (x176 - x202)^2 + (x316 - x342)^2) + 1 / sqrt((x36 - x63)^2 + (
    x176 - x203)^2 + (x316 - x343)^2) + 1 / sqrt((x36 - x64)^2 + (x176 - x204)^
    2 + (x316 - x344)^2) + 1 / sqrt((x36 - x65)^2 + (x176 - x205)^2 + (x316 -
    x345)^2) + 1 / sqrt((x36 - x66)^2 + (x176 - x206)^2 + (x316 - x346)^2) + 1
    / sqrt((x36 - x67)^2 + (x176 - x207)^2 + (x316 - x347)^2) + 1 / sqrt((x36
    - x68)^2 + (x176 - x208)^2 + (x316 - x348)^2) + 1 / sqrt((x36 - x69)^2 + (
    x176 - x209)^2 + (x316 - x349)^2) + 1 / sqrt((x36 - x70)^2 + (x176 - x210)^
    2 + (x316 - x350)^2) + 1 / sqrt((x36 - x71)^2 + (x176 - x211)^2 + (x316 -
    x351)^2) + 1 / sqrt((x36 - x72)^2 + (x176 - x212)^2 + (x316 - x352)^2) + 1
    / sqrt((x36 - x73)^2 + (x176 - x213)^2 + (x316 - x353)^2) + 1 / sqrt((x36
    - x74)^2 + (x176 - x214)^2 + (x316 - x354)^2) + 1 / sqrt((x36 - x75)^2 + (
    x176 - x215)^2 + (x316 - x355)^2) + 1 / sqrt((x36 - x76)^2 + (x176 - x216)^
    2 + (x316 - x356)^2) + 1 / sqrt((x36 - x77)^2 + (x176 - x217)^2 + (x316 -
    x357)^2) + 1 / sqrt((x36 - x78)^2 + (x176 - x218)^2 + (x316 - x358)^2) + 1
    / sqrt((x36 - x79)^2 + (x176 - x219)^2 + (x316 - x359)^2) + 1 / sqrt((x36
    - x80)^2 + (x176 - x220)^2 + (x316 - x360)^2) + 1 / sqrt((x36 - x81)^2 + (
    x176 - x221)^2 + (x316 - x361)^2) + 1 / sqrt((x36 - x82)^2 + (x176 - x222)^
    2 + (x316 - x362)^2) + 1 / sqrt((x36 - x83)^2 + (x176 - x223)^2 + (x316 -
    x363)^2) + 1 / sqrt((x36 - x84)^2 + (x176 - x224)^2 + (x316 - x364)^2) + 1
    / sqrt((x36 - x85)^2 + (x176 - x225)^2 + (x316 - x365)^2) + 1 / sqrt((x36
    - x86)^2 + (x176 - x226)^2 + (x316 - x366)^2) + 1 / sqrt((x36 - x87)^2 + (
    x176 - x227)^2 + (x316 - x367)^2) + 1 / sqrt((x36 - x88)^2 + (x176 - x228)^
    2 + (x316 - x368)^2) + 1 / sqrt((x36 - x89)^2 + (x176 - x229)^2 + (x316 -
    x369)^2) + 1 / sqrt((x36 - x90)^2 + (x176 - x230)^2 + (x316 - x370)^2) + 1
    / sqrt((x36 - x91)^2 + (x176 - x231)^2 + (x316 - x371)^2) + 1 / sqrt((x36
    - x92)^2 + (x176 - x232)^2 + (x316 - x372)^2) + 1 / sqrt((x36 - x93)^2 + (
    x176 - x233)^2 + (x316 - x373)^2) + 1 / sqrt((x36 - x94)^2 + (x176 - x234)^
    2 + (x316 - x374)^2) + 1 / sqrt((x36 - x95)^2 + (x176 - x235)^2 + (x316 -
    x375)^2) + 1 / sqrt((x36 - x96)^2 + (x176 - x236)^2 + (x316 - x376)^2) + 1
    / sqrt((x36 - x97)^2 + (x176 - x237)^2 + (x316 - x377)^2) + 1 / sqrt((x36
    - x98)^2 + (x176 - x238)^2 + (x316 - x378)^2) + 1 / sqrt((x36 - x99)^2 + (
    x176 - x239)^2 + (x316 - x379)^2) + 1 / sqrt((x36 - x100)^2 + (x176 - x240)
    ^2 + (x316 - x380)^2) + 1 / sqrt((x36 - x101)^2 + (x176 - x241)^2 + (x316
    - x381)^2) + 1 / sqrt((x36 - x102)^2 + (x176 - x242)^2 + (x316 - x382)^2)
    + 1 / sqrt((x36 - x103)^2 + (x176 - x243)^2 + (x316 - x383)^2) + 1 / sqrt(
    (x36 - x104)^2 + (x176 - x244)^2 + (x316 - x384)^2) + 1 / sqrt((x36 - x105)
    ^2 + (x176 - x245)^2 + (x316 - x385)^2) + 1 / sqrt((x36 - x106)^2 + (x176
    - x246)^2 + (x316 - x386)^2) + 1 / sqrt((x36 - x107)^2 + (x176 - x247)^2
    + (x316 - x387)^2) + 1 / sqrt((x36 - x108)^2 + (x176 - x248)^2 + (x316 -
    x388)^2) + 1 / sqrt((x36 - x109)^2 + (x176 - x249)^2 + (x316 - x389)^2) + 1
    / sqrt((x36 - x110)^2 + (x176 - x250)^2 + (x316 - x390)^2) + 1 / sqrt((x36
    - x111)^2 + (x176 - x251)^2 + (x316 - x391)^2) + 1 / sqrt((x36 - x112)^2
    + (x176 - x252)^2 + (x316 - x392)^2) + 1 / sqrt((x36 - x113)^2 + (x176 -
    x253)^2 + (x316 - x393)^2) + 1 / sqrt((x36 - x114)^2 + (x176 - x254)^2 + (
    x316 - x394)^2) + 1 / sqrt((x36 - x115)^2 + (x176 - x255)^2 + (x316 - x395)
    ^2) + 1 / sqrt((x36 - x116)^2 + (x176 - x256)^2 + (x316 - x396)^2) + 1 /
    sqrt((x36 - x117)^2 + (x176 - x257)^2 + (x316 - x397)^2) + 1 / sqrt((x36 -
    x118)^2 + (x176 - x258)^2 + (x316 - x398)^2) + 1 / sqrt((x36 - x119)^2 + (
    x176 - x259)^2 + (x316 - x399)^2) + 1 / sqrt((x36 - x120)^2 + (x176 - x260)
    ^2 + (x316 - x400)^2) + 1 / sqrt((x36 - x121)^2 + (x176 - x261)^2 + (x316
    - x401)^2) + 1 / sqrt((x36 - x122)^2 + (x176 - x262)^2 + (x316 - x402)^2)
    + 1 / sqrt((x36 - x123)^2 + (x176 - x263)^2 + (x316 - x403)^2) + 1 / sqrt(
    (x36 - x124)^2 + (x176 - x264)^2 + (x316 - x404)^2) + 1 / sqrt((x36 - x125)
    ^2 + (x176 - x265)^2 + (x316 - x405)^2) + 1 / sqrt((x36 - x126)^2 + (x176
    - x266)^2 + (x316 - x406)^2) + 1 / sqrt((x36 - x127)^2 + (x176 - x267)^2
    + (x316 - x407)^2) + 1 / sqrt((x36 - x128)^2 + (x176 - x268)^2 + (x316 -
    x408)^2) + 1 / sqrt((x36 - x129)^2 + (x176 - x269)^2 + (x316 - x409)^2) + 1
    / sqrt((x36 - x130)^2 + (x176 - x270)^2 + (x316 - x410)^2) + 1 / sqrt((x36
    - x131)^2 + (x176 - x271)^2 + (x316 - x411)^2) + 1 / sqrt((x36 - x132)^2
    + (x176 - x272)^2 + (x316 - x412)^2) + 1 / sqrt((x36 - x133)^2 + (x176 -
    x273)^2 + (x316 - x413)^2) + 1 / sqrt((x36 - x134)^2 + (x176 - x274)^2 + (
    x316 - x414)^2) + 1 / sqrt((x36 - x135)^2 + (x176 - x275)^2 + (x316 - x415)
    ^2) + 1 / sqrt((x36 - x136)^2 + (x176 - x276)^2 + (x316 - x416)^2) + 1 /
    sqrt((x36 - x137)^2 + (x176 - x277)^2 + (x316 - x417)^2) + 1 / sqrt((x36 -
    x138)^2 + (x176 - x278)^2 + (x316 - x418)^2) + 1 / sqrt((x36 - x139)^2 + (
    x176 - x279)^2 + (x316 - x419)^2) + 1 / sqrt((x36 - x140)^2 + (x176 - x280)
    ^2 + (x316 - x420)^2) + 1 / sqrt((x37 - x38)^2 + (x177 - x178)^2 + (x317 -
    x318)^2) + 1 / sqrt((x37 - x39)^2 + (x177 - x179)^2 + (x317 - x319)^2) + 1
    / sqrt((x37 - x40)^2 + (x177 - x180)^2 + (x317 - x320)^2) + 1 / sqrt((x37
    - x41)^2 + (x177 - x181)^2 + (x317 - x321)^2) + 1 / sqrt((x37 - x42)^2 + (
    x177 - x182)^2 + (x317 - x322)^2) + 1 / sqrt((x37 - x43)^2 + (x177 - x183)^
    2 + (x317 - x323)^2) + 1 / sqrt((x37 - x44)^2 + (x177 - x184)^2 + (x317 -
    x324)^2) + 1 / sqrt((x37 - x45)^2 + (x177 - x185)^2 + (x317 - x325)^2) + 1
    / sqrt((x37 - x46)^2 + (x177 - x186)^2 + (x317 - x326)^2) + 1 / sqrt((x37
    - x47)^2 + (x177 - x187)^2 + (x317 - x327)^2) + 1 / sqrt((x37 - x48)^2 + (
    x177 - x188)^2 + (x317 - x328)^2) + 1 / sqrt((x37 - x49)^2 + (x177 - x189)^
    2 + (x317 - x329)^2) + 1 / sqrt((x37 - x50)^2 + (x177 - x190)^2 + (x317 -
    x330)^2) + 1 / sqrt((x37 - x51)^2 + (x177 - x191)^2 + (x317 - x331)^2) + 1
    / sqrt((x37 - x52)^2 + (x177 - x192)^2 + (x317 - x332)^2) + 1 / sqrt((x37
    - x53)^2 + (x177 - x193)^2 + (x317 - x333)^2) + 1 / sqrt((x37 - x54)^2 + (
    x177 - x194)^2 + (x317 - x334)^2) + 1 / sqrt((x37 - x55)^2 + (x177 - x195)^
    2 + (x317 - x335)^2) + 1 / sqrt((x37 - x56)^2 + (x177 - x196)^2 + (x317 -
    x336)^2) + 1 / sqrt((x37 - x57)^2 + (x177 - x197)^2 + (x317 - x337)^2) + 1
    / sqrt((x37 - x58)^2 + (x177 - x198)^2 + (x317 - x338)^2) + 1 / sqrt((x37
    - x59)^2 + (x177 - x199)^2 + (x317 - x339)^2) + 1 / sqrt((x37 - x60)^2 + (
    x177 - x200)^2 + (x317 - x340)^2) + 1 / sqrt((x37 - x61)^2 + (x177 - x201)^
    2 + (x317 - x341)^2) + 1 / sqrt((x37 - x62)^2 + (x177 - x202)^2 + (x317 -
    x342)^2) + 1 / sqrt((x37 - x63)^2 + (x177 - x203)^2 + (x317 - x343)^2) + 1
    / sqrt((x37 - x64)^2 + (x177 - x204)^2 + (x317 - x344)^2) + 1 / sqrt((x37
    - x65)^2 + (x177 - x205)^2 + (x317 - x345)^2) + 1 / sqrt((x37 - x66)^2 + (
    x177 - x206)^2 + (x317 - x346)^2) + 1 / sqrt((x37 - x67)^2 + (x177 - x207)^
    2 + (x317 - x347)^2) + 1 / sqrt((x37 - x68)^2 + (x177 - x208)^2 + (x317 -
    x348)^2) + 1 / sqrt((x37 - x69)^2 + (x177 - x209)^2 + (x317 - x349)^2) + 1
    / sqrt((x37 - x70)^2 + (x177 - x210)^2 + (x317 - x350)^2) + 1 / sqrt((x37
    - x71)^2 + (x177 - x211)^2 + (x317 - x351)^2) + 1 / sqrt((x37 - x72)^2 + (
    x177 - x212)^2 + (x317 - x352)^2) + 1 / sqrt((x37 - x73)^2 + (x177 - x213)^
    2 + (x317 - x353)^2) + 1 / sqrt((x37 - x74)^2 + (x177 - x214)^2 + (x317 -
    x354)^2) + 1 / sqrt((x37 - x75)^2 + (x177 - x215)^2 + (x317 - x355)^2) + 1
    / sqrt((x37 - x76)^2 + (x177 - x216)^2 + (x317 - x356)^2) + 1 / sqrt((x37
    - x77)^2 + (x177 - x217)^2 + (x317 - x357)^2) + 1 / sqrt((x37 - x78)^2 + (
    x177 - x218)^2 + (x317 - x358)^2) + 1 / sqrt((x37 - x79)^2 + (x177 - x219)^
    2 + (x317 - x359)^2) + 1 / sqrt((x37 - x80)^2 + (x177 - x220)^2 + (x317 -
    x360)^2) + 1 / sqrt((x37 - x81)^2 + (x177 - x221)^2 + (x317 - x361)^2) + 1
    / sqrt((x37 - x82)^2 + (x177 - x222)^2 + (x317 - x362)^2) + 1 / sqrt((x37
    - x83)^2 + (x177 - x223)^2 + (x317 - x363)^2) + 1 / sqrt((x37 - x84)^2 + (
    x177 - x224)^2 + (x317 - x364)^2) + 1 / sqrt((x37 - x85)^2 + (x177 - x225)^
    2 + (x317 - x365)^2) + 1 / sqrt((x37 - x86)^2 + (x177 - x226)^2 + (x317 -
    x366)^2) + 1 / sqrt((x37 - x87)^2 + (x177 - x227)^2 + (x317 - x367)^2) + 1
    / sqrt((x37 - x88)^2 + (x177 - x228)^2 + (x317 - x368)^2) + 1 / sqrt((x37
    - x89)^2 + (x177 - x229)^2 + (x317 - x369)^2) + 1 / sqrt((x37 - x90)^2 + (
    x177 - x230)^2 + (x317 - x370)^2) + 1 / sqrt((x37 - x91)^2 + (x177 - x231)^
    2 + (x317 - x371)^2) + 1 / sqrt((x37 - x92)^2 + (x177 - x232)^2 + (x317 -
    x372)^2) + 1 / sqrt((x37 - x93)^2 + (x177 - x233)^2 + (x317 - x373)^2) + 1
    / sqrt((x37 - x94)^2 + (x177 - x234)^2 + (x317 - x374)^2) + 1 / sqrt((x37
    - x95)^2 + (x177 - x235)^2 + (x317 - x375)^2) + 1 / sqrt((x37 - x96)^2 + (
    x177 - x236)^2 + (x317 - x376)^2) + 1 / sqrt((x37 - x97)^2 + (x177 - x237)^
    2 + (x317 - x377)^2) + 1 / sqrt((x37 - x98)^2 + (x177 - x238)^2 + (x317 -
    x378)^2) + 1 / sqrt((x37 - x99)^2 + (x177 - x239)^2 + (x317 - x379)^2) + 1
    / sqrt((x37 - x100)^2 + (x177 - x240)^2 + (x317 - x380)^2) + 1 / sqrt((x37
    - x101)^2 + (x177 - x241)^2 + (x317 - x381)^2) + 1 / sqrt((x37 - x102)^2
    + (x177 - x242)^2 + (x317 - x382)^2) + 1 / sqrt((x37 - x103)^2 + (x177 -
    x243)^2 + (x317 - x383)^2) + 1 / sqrt((x37 - x104)^2 + (x177 - x244)^2 + (
    x317 - x384)^2) + 1 / sqrt((x37 - x105)^2 + (x177 - x245)^2 + (x317 - x385)
    ^2) + 1 / sqrt((x37 - x106)^2 + (x177 - x246)^2 + (x317 - x386)^2) + 1 /
    sqrt((x37 - x107)^2 + (x177 - x247)^2 + (x317 - x387)^2) + 1 / sqrt((x37 -
    x108)^2 + (x177 - x248)^2 + (x317 - x388)^2) + 1 / sqrt((x37 - x109)^2 + (
    x177 - x249)^2 + (x317 - x389)^2) + 1 / sqrt((x37 - x110)^2 + (x177 - x250)
    ^2 + (x317 - x390)^2) + 1 / sqrt((x37 - x111)^2 + (x177 - x251)^2 + (x317
    - x391)^2) + 1 / sqrt((x37 - x112)^2 + (x177 - x252)^2 + (x317 - x392)^2)
    + 1 / sqrt((x37 - x113)^2 + (x177 - x253)^2 + (x317 - x393)^2) + 1 / sqrt(
    (x37 - x114)^2 + (x177 - x254)^2 + (x317 - x394)^2) + 1 / sqrt((x37 - x115)
    ^2 + (x177 - x255)^2 + (x317 - x395)^2) + 1 / sqrt((x37 - x116)^2 + (x177
    - x256)^2 + (x317 - x396)^2) + 1 / sqrt((x37 - x117)^2 + (x177 - x257)^2
    + (x317 - x397)^2) + 1 / sqrt((x37 - x118)^2 + (x177 - x258)^2 + (x317 -
    x398)^2) + 1 / sqrt((x37 - x119)^2 + (x177 - x259)^2 + (x317 - x399)^2) + 1
    / sqrt((x37 - x120)^2 + (x177 - x260)^2 + (x317 - x400)^2) + 1 / sqrt((x37
    - x121)^2 + (x177 - x261)^2 + (x317 - x401)^2) + 1 / sqrt((x37 - x122)^2
    + (x177 - x262)^2 + (x317 - x402)^2) + 1 / sqrt((x37 - x123)^2 + (x177 -
    x263)^2 + (x317 - x403)^2) + 1 / sqrt((x37 - x124)^2 + (x177 - x264)^2 + (
    x317 - x404)^2) + 1 / sqrt((x37 - x125)^2 + (x177 - x265)^2 + (x317 - x405)
    ^2) + 1 / sqrt((x37 - x126)^2 + (x177 - x266)^2 + (x317 - x406)^2) + 1 /
    sqrt((x37 - x127)^2 + (x177 - x267)^2 + (x317 - x407)^2) + 1 / sqrt((x37 -
    x128)^2 + (x177 - x268)^2 + (x317 - x408)^2) + 1 / sqrt((x37 - x129)^2 + (
    x177 - x269)^2 + (x317 - x409)^2) + 1 / sqrt((x37 - x130)^2 + (x177 - x270)
    ^2 + (x317 - x410)^2) + 1 / sqrt((x37 - x131)^2 + (x177 - x271)^2 + (x317
    - x411)^2) + 1 / sqrt((x37 - x132)^2 + (x177 - x272)^2 + (x317 - x412)^2)
    + 1 / sqrt((x37 - x133)^2 + (x177 - x273)^2 + (x317 - x413)^2) + 1 / sqrt(
    (x37 - x134)^2 + (x177 - x274)^2 + (x317 - x414)^2) + 1 / sqrt((x37 - x135)
    ^2 + (x177 - x275)^2 + (x317 - x415)^2) + 1 / sqrt((x37 - x136)^2 + (x177
    - x276)^2 + (x317 - x416)^2) + 1 / sqrt((x37 - x137)^2 + (x177 - x277)^2
    + (x317 - x417)^2) + 1 / sqrt((x37 - x138)^2 + (x177 - x278)^2 + (x317 -
    x418)^2) + 1 / sqrt((x37 - x139)^2 + (x177 - x279)^2 + (x317 - x419)^2) + 1
    / sqrt((x37 - x140)^2 + (x177 - x280)^2 + (x317 - x420)^2) + 1 / sqrt((x38
    - x39)^2 + (x178 - x179)^2 + (x318 - x319)^2) + 1 / sqrt((x38 - x40)^2 + (
    x178 - x180)^2 + (x318 - x320)^2) + 1 / sqrt((x38 - x41)^2 + (x178 - x181)^
    2 + (x318 - x321)^2) + 1 / sqrt((x38 - x42)^2 + (x178 - x182)^2 + (x318 -
    x322)^2) + 1 / sqrt((x38 - x43)^2 + (x178 - x183)^2 + (x318 - x323)^2) + 1
    / sqrt((x38 - x44)^2 + (x178 - x184)^2 + (x318 - x324)^2) + 1 / sqrt((x38
    - x45)^2 + (x178 - x185)^2 + (x318 - x325)^2) + 1 / sqrt((x38 - x46)^2 + (
    x178 - x186)^2 + (x318 - x326)^2) + 1 / sqrt((x38 - x47)^2 + (x178 - x187)^
    2 + (x318 - x327)^2) + 1 / sqrt((x38 - x48)^2 + (x178 - x188)^2 + (x318 -
    x328)^2) + 1 / sqrt((x38 - x49)^2 + (x178 - x189)^2 + (x318 - x329)^2) + 1
    / sqrt((x38 - x50)^2 + (x178 - x190)^2 + (x318 - x330)^2) + 1 / sqrt((x38
    - x51)^2 + (x178 - x191)^2 + (x318 - x331)^2) + 1 / sqrt((x38 - x52)^2 + (
    x178 - x192)^2 + (x318 - x332)^2) + 1 / sqrt((x38 - x53)^2 + (x178 - x193)^
    2 + (x318 - x333)^2) + 1 / sqrt((x38 - x54)^2 + (x178 - x194)^2 + (x318 -
    x334)^2) + 1 / sqrt((x38 - x55)^2 + (x178 - x195)^2 + (x318 - x335)^2) + 1
    / sqrt((x38 - x56)^2 + (x178 - x196)^2 + (x318 - x336)^2) + 1 / sqrt((x38
    - x57)^2 + (x178 - x197)^2 + (x318 - x337)^2) + 1 / sqrt((x38 - x58)^2 + (
    x178 - x198)^2 + (x318 - x338)^2) + 1 / sqrt((x38 - x59)^2 + (x178 - x199)^
    2 + (x318 - x339)^2) + 1 / sqrt((x38 - x60)^2 + (x178 - x200)^2 + (x318 -
    x340)^2) + 1 / sqrt((x38 - x61)^2 + (x178 - x201)^2 + (x318 - x341)^2) + 1
    / sqrt((x38 - x62)^2 + (x178 - x202)^2 + (x318 - x342)^2) + 1 / sqrt((x38
    - x63)^2 + (x178 - x203)^2 + (x318 - x343)^2) + 1 / sqrt((x38 - x64)^2 + (
    x178 - x204)^2 + (x318 - x344)^2) + 1 / sqrt((x38 - x65)^2 + (x178 - x205)^
    2 + (x318 - x345)^2) + 1 / sqrt((x38 - x66)^2 + (x178 - x206)^2 + (x318 -
    x346)^2) + 1 / sqrt((x38 - x67)^2 + (x178 - x207)^2 + (x318 - x347)^2) + 1
    / sqrt((x38 - x68)^2 + (x178 - x208)^2 + (x318 - x348)^2) + 1 / sqrt((x38
    - x69)^2 + (x178 - x209)^2 + (x318 - x349)^2) + 1 / sqrt((x38 - x70)^2 + (
    x178 - x210)^2 + (x318 - x350)^2) + 1 / sqrt((x38 - x71)^2 + (x178 - x211)^
    2 + (x318 - x351)^2) + 1 / sqrt((x38 - x72)^2 + (x178 - x212)^2 + (x318 -
    x352)^2) + 1 / sqrt((x38 - x73)^2 + (x178 - x213)^2 + (x318 - x353)^2) + 1
    / sqrt((x38 - x74)^2 + (x178 - x214)^2 + (x318 - x354)^2) + 1 / sqrt((x38
    - x75)^2 + (x178 - x215)^2 + (x318 - x355)^2) + 1 / sqrt((x38 - x76)^2 + (
    x178 - x216)^2 + (x318 - x356)^2) + 1 / sqrt((x38 - x77)^2 + (x178 - x217)^
    2 + (x318 - x357)^2) + 1 / sqrt((x38 - x78)^2 + (x178 - x218)^2 + (x318 -
    x358)^2) + 1 / sqrt((x38 - x79)^2 + (x178 - x219)^2 + (x318 - x359)^2) + 1
    / sqrt((x38 - x80)^2 + (x178 - x220)^2 + (x318 - x360)^2) + 1 / sqrt((x38
    - x81)^2 + (x178 - x221)^2 + (x318 - x361)^2) + 1 / sqrt((x38 - x82)^2 + (
    x178 - x222)^2 + (x318 - x362)^2) + 1 / sqrt((x38 - x83)^2 + (x178 - x223)^
    2 + (x318 - x363)^2) + 1 / sqrt((x38 - x84)^2 + (x178 - x224)^2 + (x318 -
    x364)^2) + 1 / sqrt((x38 - x85)^2 + (x178 - x225)^2 + (x318 - x365)^2) + 1
    / sqrt((x38 - x86)^2 + (x178 - x226)^2 + (x318 - x366)^2) + 1 / sqrt((x38
    - x87)^2 + (x178 - x227)^2 + (x318 - x367)^2) + 1 / sqrt((x38 - x88)^2 + (
    x178 - x228)^2 + (x318 - x368)^2) + 1 / sqrt((x38 - x89)^2 + (x178 - x229)^
    2 + (x318 - x369)^2) + 1 / sqrt((x38 - x90)^2 + (x178 - x230)^2 + (x318 -
    x370)^2) + 1 / sqrt((x38 - x91)^2 + (x178 - x231)^2 + (x318 - x371)^2) + 1
    / sqrt((x38 - x92)^2 + (x178 - x232)^2 + (x318 - x372)^2) + 1 / sqrt((x38
    - x93)^2 + (x178 - x233)^2 + (x318 - x373)^2) + 1 / sqrt((x38 - x94)^2 + (
    x178 - x234)^2 + (x318 - x374)^2) + 1 / sqrt((x38 - x95)^2 + (x178 - x235)^
    2 + (x318 - x375)^2) + 1 / sqrt((x38 - x96)^2 + (x178 - x236)^2 + (x318 -
    x376)^2) + 1 / sqrt((x38 - x97)^2 + (x178 - x237)^2 + (x318 - x377)^2) + 1
    / sqrt((x38 - x98)^2 + (x178 - x238)^2 + (x318 - x378)^2) + 1 / sqrt((x38
    - x99)^2 + (x178 - x239)^2 + (x318 - x379)^2) + 1 / sqrt((x38 - x100)^2 +
    (x178 - x240)^2 + (x318 - x380)^2) + 1 / sqrt((x38 - x101)^2 + (x178 - x241)
    ^2 + (x318 - x381)^2) + 1 / sqrt((x38 - x102)^2 + (x178 - x242)^2 + (x318
    - x382)^2) + 1 / sqrt((x38 - x103)^2 + (x178 - x243)^2 + (x318 - x383)^2)
    + 1 / sqrt((x38 - x104)^2 + (x178 - x244)^2 + (x318 - x384)^2) + 1 / sqrt(
    (x38 - x105)^2 + (x178 - x245)^2 + (x318 - x385)^2) + 1 / sqrt((x38 - x106)
    ^2 + (x178 - x246)^2 + (x318 - x386)^2) + 1 / sqrt((x38 - x107)^2 + (x178
    - x247)^2 + (x318 - x387)^2) + 1 / sqrt((x38 - x108)^2 + (x178 - x248)^2
    + (x318 - x388)^2) + 1 / sqrt((x38 - x109)^2 + (x178 - x249)^2 + (x318 -
    x389)^2) + 1 / sqrt((x38 - x110)^2 + (x178 - x250)^2 + (x318 - x390)^2) + 1
    / sqrt((x38 - x111)^2 + (x178 - x251)^2 + (x318 - x391)^2) + 1 / sqrt((x38
    - x112)^2 + (x178 - x252)^2 + (x318 - x392)^2) + 1 / sqrt((x38 - x113)^2
    + (x178 - x253)^2 + (x318 - x393)^2) + 1 / sqrt((x38 - x114)^2 + (x178 -
    x254)^2 + (x318 - x394)^2) + 1 / sqrt((x38 - x115)^2 + (x178 - x255)^2 + (
    x318 - x395)^2) + 1 / sqrt((x38 - x116)^2 + (x178 - x256)^2 + (x318 - x396)
    ^2) + 1 / sqrt((x38 - x117)^2 + (x178 - x257)^2 + (x318 - x397)^2) + 1 /
    sqrt((x38 - x118)^2 + (x178 - x258)^2 + (x318 - x398)^2) + 1 / sqrt((x38 -
    x119)^2 + (x178 - x259)^2 + (x318 - x399)^2) + 1 / sqrt((x38 - x120)^2 + (
    x178 - x260)^2 + (x318 - x400)^2) + 1 / sqrt((x38 - x121)^2 + (x178 - x261)
    ^2 + (x318 - x401)^2) + 1 / sqrt((x38 - x122)^2 + (x178 - x262)^2 + (x318
    - x402)^2) + 1 / sqrt((x38 - x123)^2 + (x178 - x263)^2 + (x318 - x403)^2)
    + 1 / sqrt((x38 - x124)^2 + (x178 - x264)^2 + (x318 - x404)^2) + 1 / sqrt(
    (x38 - x125)^2 + (x178 - x265)^2 + (x318 - x405)^2) + 1 / sqrt((x38 - x126)
    ^2 + (x178 - x266)^2 + (x318 - x406)^2) + 1 / sqrt((x38 - x127)^2 + (x178
    - x267)^2 + (x318 - x407)^2) + 1 / sqrt((x38 - x128)^2 + (x178 - x268)^2
    + (x318 - x408)^2) + 1 / sqrt((x38 - x129)^2 + (x178 - x269)^2 + (x318 -
    x409)^2) + 1 / sqrt((x38 - x130)^2 + (x178 - x270)^2 + (x318 - x410)^2) + 1
    / sqrt((x38 - x131)^2 + (x178 - x271)^2 + (x318 - x411)^2) + 1 / sqrt((x38
    - x132)^2 + (x178 - x272)^2 + (x318 - x412)^2) + 1 / sqrt((x38 - x133)^2
    + (x178 - x273)^2 + (x318 - x413)^2) + 1 / sqrt((x38 - x134)^2 + (x178 -
    x274)^2 + (x318 - x414)^2) + 1 / sqrt((x38 - x135)^2 + (x178 - x275)^2 + (
    x318 - x415)^2) + 1 / sqrt((x38 - x136)^2 + (x178 - x276)^2 + (x318 - x416)
    ^2) + 1 / sqrt((x38 - x137)^2 + (x178 - x277)^2 + (x318 - x417)^2) + 1 /
    sqrt((x38 - x138)^2 + (x178 - x278)^2 + (x318 - x418)^2) + 1 / sqrt((x38 -
    x139)^2 + (x178 - x279)^2 + (x318 - x419)^2) + 1 / sqrt((x38 - x140)^2 + (
    x178 - x280)^2 + (x318 - x420)^2) + 1 / sqrt((x39 - x40)^2 + (x179 - x180)^
    2 + (x319 - x320)^2) + 1 / sqrt((x39 - x41)^2 + (x179 - x181)^2 + (x319 -
    x321)^2) + 1 / sqrt((x39 - x42)^2 + (x179 - x182)^2 + (x319 - x322)^2) + 1
    / sqrt((x39 - x43)^2 + (x179 - x183)^2 + (x319 - x323)^2) + 1 / sqrt((x39
    - x44)^2 + (x179 - x184)^2 + (x319 - x324)^2) + 1 / sqrt((x39 - x45)^2 + (
    x179 - x185)^2 + (x319 - x325)^2) + 1 / sqrt((x39 - x46)^2 + (x179 - x186)^
    2 + (x319 - x326)^2) + 1 / sqrt((x39 - x47)^2 + (x179 - x187)^2 + (x319 -
    x327)^2) + 1 / sqrt((x39 - x48)^2 + (x179 - x188)^2 + (x319 - x328)^2) + 1
    / sqrt((x39 - x49)^2 + (x179 - x189)^2 + (x319 - x329)^2) + 1 / sqrt((x39
    - x50)^2 + (x179 - x190)^2 + (x319 - x330)^2) + 1 / sqrt((x39 - x51)^2 + (
    x179 - x191)^2 + (x319 - x331)^2) + 1 / sqrt((x39 - x52)^2 + (x179 - x192)^
    2 + (x319 - x332)^2) + 1 / sqrt((x39 - x53)^2 + (x179 - x193)^2 + (x319 -
    x333)^2) + 1 / sqrt((x39 - x54)^2 + (x179 - x194)^2 + (x319 - x334)^2) + 1
    / sqrt((x39 - x55)^2 + (x179 - x195)^2 + (x319 - x335)^2) + 1 / sqrt((x39
    - x56)^2 + (x179 - x196)^2 + (x319 - x336)^2) + 1 / sqrt((x39 - x57)^2 + (
    x179 - x197)^2 + (x319 - x337)^2) + 1 / sqrt((x39 - x58)^2 + (x179 - x198)^
    2 + (x319 - x338)^2) + 1 / sqrt((x39 - x59)^2 + (x179 - x199)^2 + (x319 -
    x339)^2) + 1 / sqrt((x39 - x60)^2 + (x179 - x200)^2 + (x319 - x340)^2) + 1
    / sqrt((x39 - x61)^2 + (x179 - x201)^2 + (x319 - x341)^2) + 1 / sqrt((x39
    - x62)^2 + (x179 - x202)^2 + (x319 - x342)^2) + 1 / sqrt((x39 - x63)^2 + (
    x179 - x203)^2 + (x319 - x343)^2) + 1 / sqrt((x39 - x64)^2 + (x179 - x204)^
    2 + (x319 - x344)^2) + 1 / sqrt((x39 - x65)^2 + (x179 - x205)^2 + (x319 -
    x345)^2) + 1 / sqrt((x39 - x66)^2 + (x179 - x206)^2 + (x319 - x346)^2) + 1
    / sqrt((x39 - x67)^2 + (x179 - x207)^2 + (x319 - x347)^2) + 1 / sqrt((x39
    - x68)^2 + (x179 - x208)^2 + (x319 - x348)^2) + 1 / sqrt((x39 - x69)^2 + (
    x179 - x209)^2 + (x319 - x349)^2) + 1 / sqrt((x39 - x70)^2 + (x179 - x210)^
    2 + (x319 - x350)^2) + 1 / sqrt((x39 - x71)^2 + (x179 - x211)^2 + (x319 -
    x351)^2) + 1 / sqrt((x39 - x72)^2 + (x179 - x212)^2 + (x319 - x352)^2) + 1
    / sqrt((x39 - x73)^2 + (x179 - x213)^2 + (x319 - x353)^2) + 1 / sqrt((x39
    - x74)^2 + (x179 - x214)^2 + (x319 - x354)^2) + 1 / sqrt((x39 - x75)^2 + (
    x179 - x215)^2 + (x319 - x355)^2) + 1 / sqrt((x39 - x76)^2 + (x179 - x216)^
    2 + (x319 - x356)^2) + 1 / sqrt((x39 - x77)^2 + (x179 - x217)^2 + (x319 -
    x357)^2) + 1 / sqrt((x39 - x78)^2 + (x179 - x218)^2 + (x319 - x358)^2) + 1
    / sqrt((x39 - x79)^2 + (x179 - x219)^2 + (x319 - x359)^2) + 1 / sqrt((x39
    - x80)^2 + (x179 - x220)^2 + (x319 - x360)^2) + 1 / sqrt((x39 - x81)^2 + (
    x179 - x221)^2 + (x319 - x361)^2) + 1 / sqrt((x39 - x82)^2 + (x179 - x222)^
    2 + (x319 - x362)^2) + 1 / sqrt((x39 - x83)^2 + (x179 - x223)^2 + (x319 -
    x363)^2) + 1 / sqrt((x39 - x84)^2 + (x179 - x224)^2 + (x319 - x364)^2) + 1
    / sqrt((x39 - x85)^2 + (x179 - x225)^2 + (x319 - x365)^2) + 1 / sqrt((x39
    - x86)^2 + (x179 - x226)^2 + (x319 - x366)^2) + 1 / sqrt((x39 - x87)^2 + (
    x179 - x227)^2 + (x319 - x367)^2) + 1 / sqrt((x39 - x88)^2 + (x179 - x228)^
    2 + (x319 - x368)^2) + 1 / sqrt((x39 - x89)^2 + (x179 - x229)^2 + (x319 -
    x369)^2) + 1 / sqrt((x39 - x90)^2 + (x179 - x230)^2 + (x319 - x370)^2) + 1
    / sqrt((x39 - x91)^2 + (x179 - x231)^2 + (x319 - x371)^2) + 1 / sqrt((x39
    - x92)^2 + (x179 - x232)^2 + (x319 - x372)^2) + 1 / sqrt((x39 - x93)^2 + (
    x179 - x233)^2 + (x319 - x373)^2) + 1 / sqrt((x39 - x94)^2 + (x179 - x234)^
    2 + (x319 - x374)^2) + 1 / sqrt((x39 - x95)^2 + (x179 - x235)^2 + (x319 -
    x375)^2) + 1 / sqrt((x39 - x96)^2 + (x179 - x236)^2 + (x319 - x376)^2) + 1
    / sqrt((x39 - x97)^2 + (x179 - x237)^2 + (x319 - x377)^2) + 1 / sqrt((x39
    - x98)^2 + (x179 - x238)^2 + (x319 - x378)^2) + 1 / sqrt((x39 - x99)^2 + (
    x179 - x239)^2 + (x319 - x379)^2) + 1 / sqrt((x39 - x100)^2 + (x179 - x240)
    ^2 + (x319 - x380)^2) + 1 / sqrt((x39 - x101)^2 + (x179 - x241)^2 + (x319
    - x381)^2) + 1 / sqrt((x39 - x102)^2 + (x179 - x242)^2 + (x319 - x382)^2)
    + 1 / sqrt((x39 - x103)^2 + (x179 - x243)^2 + (x319 - x383)^2) + 1 / sqrt(
    (x39 - x104)^2 + (x179 - x244)^2 + (x319 - x384)^2) + 1 / sqrt((x39 - x105)
    ^2 + (x179 - x245)^2 + (x319 - x385)^2) + 1 / sqrt((x39 - x106)^2 + (x179
    - x246)^2 + (x319 - x386)^2) + 1 / sqrt((x39 - x107)^2 + (x179 - x247)^2
    + (x319 - x387)^2) + 1 / sqrt((x39 - x108)^2 + (x179 - x248)^2 + (x319 -
    x388)^2) + 1 / sqrt((x39 - x109)^2 + (x179 - x249)^2 + (x319 - x389)^2) + 1
    / sqrt((x39 - x110)^2 + (x179 - x250)^2 + (x319 - x390)^2) + 1 / sqrt((x39
    - x111)^2 + (x179 - x251)^2 + (x319 - x391)^2) + 1 / sqrt((x39 - x112)^2
    + (x179 - x252)^2 + (x319 - x392)^2) + 1 / sqrt((x39 - x113)^2 + (x179 -
    x253)^2 + (x319 - x393)^2) + 1 / sqrt((x39 - x114)^2 + (x179 - x254)^2 + (
    x319 - x394)^2) + 1 / sqrt((x39 - x115)^2 + (x179 - x255)^2 + (x319 - x395)
    ^2) + 1 / sqrt((x39 - x116)^2 + (x179 - x256)^2 + (x319 - x396)^2) + 1 /
    sqrt((x39 - x117)^2 + (x179 - x257)^2 + (x319 - x397)^2) + 1 / sqrt((x39 -
    x118)^2 + (x179 - x258)^2 + (x319 - x398)^2) + 1 / sqrt((x39 - x119)^2 + (
    x179 - x259)^2 + (x319 - x399)^2) + 1 / sqrt((x39 - x120)^2 + (x179 - x260)
    ^2 + (x319 - x400)^2) + 1 / sqrt((x39 - x121)^2 + (x179 - x261)^2 + (x319
    - x401)^2) + 1 / sqrt((x39 - x122)^2 + (x179 - x262)^2 + (x319 - x402)^2)
    + 1 / sqrt((x39 - x123)^2 + (x179 - x263)^2 + (x319 - x403)^2) + 1 / sqrt(
    (x39 - x124)^2 + (x179 - x264)^2 + (x319 - x404)^2) + 1 / sqrt((x39 - x125)
    ^2 + (x179 - x265)^2 + (x319 - x405)^2) + 1 / sqrt((x39 - x126)^2 + (x179
    - x266)^2 + (x319 - x406)^2) + 1 / sqrt((x39 - x127)^2 + (x179 - x267)^2
    + (x319 - x407)^2) + 1 / sqrt((x39 - x128)^2 + (x179 - x268)^2 + (x319 -
    x408)^2) + 1 / sqrt((x39 - x129)^2 + (x179 - x269)^2 + (x319 - x409)^2) + 1
    / sqrt((x39 - x130)^2 + (x179 - x270)^2 + (x319 - x410)^2) + 1 / sqrt((x39
    - x131)^2 + (x179 - x271)^2 + (x319 - x411)^2) + 1 / sqrt((x39 - x132)^2
    + (x179 - x272)^2 + (x319 - x412)^2) + 1 / sqrt((x39 - x133)^2 + (x179 -
    x273)^2 + (x319 - x413)^2) + 1 / sqrt((x39 - x134)^2 + (x179 - x274)^2 + (
    x319 - x414)^2) + 1 / sqrt((x39 - x135)^2 + (x179 - x275)^2 + (x319 - x415)
    ^2) + 1 / sqrt((x39 - x136)^2 + (x179 - x276)^2 + (x319 - x416)^2) + 1 /
    sqrt((x39 - x137)^2 + (x179 - x277)^2 + (x319 - x417)^2) + 1 / sqrt((x39 -
    x138)^2 + (x179 - x278)^2 + (x319 - x418)^2) + 1 / sqrt((x39 - x139)^2 + (
    x179 - x279)^2 + (x319 - x419)^2) + 1 / sqrt((x39 - x140)^2 + (x179 - x280)
    ^2 + (x319 - x420)^2) + 1 / sqrt((x40 - x41)^2 + (x180 - x181)^2 + (x320 -
    x321)^2) + 1 / sqrt((x40 - x42)^2 + (x180 - x182)^2 + (x320 - x322)^2) + 1
    / sqrt((x40 - x43)^2 + (x180 - x183)^2 + (x320 - x323)^2) + 1 / sqrt((x40
    - x44)^2 + (x180 - x184)^2 + (x320 - x324)^2) + 1 / sqrt((x40 - x45)^2 + (
    x180 - x185)^2 + (x320 - x325)^2) + 1 / sqrt((x40 - x46)^2 + (x180 - x186)^
    2 + (x320 - x326)^2) + 1 / sqrt((x40 - x47)^2 + (x180 - x187)^2 + (x320 -
    x327)^2) + 1 / sqrt((x40 - x48)^2 + (x180 - x188)^2 + (x320 - x328)^2) + 1
    / sqrt((x40 - x49)^2 + (x180 - x189)^2 + (x320 - x329)^2) + 1 / sqrt((x40
    - x50)^2 + (x180 - x190)^2 + (x320 - x330)^2) + 1 / sqrt((x40 - x51)^2 + (
    x180 - x191)^2 + (x320 - x331)^2) + 1 / sqrt((x40 - x52)^2 + (x180 - x192)^
    2 + (x320 - x332)^2) + 1 / sqrt((x40 - x53)^2 + (x180 - x193)^2 + (x320 -
    x333)^2) + 1 / sqrt((x40 - x54)^2 + (x180 - x194)^2 + (x320 - x334)^2) + 1
    / sqrt((x40 - x55)^2 + (x180 - x195)^2 + (x320 - x335)^2) + 1 / sqrt((x40
    - x56)^2 + (x180 - x196)^2 + (x320 - x336)^2) + 1 / sqrt((x40 - x57)^2 + (
    x180 - x197)^2 + (x320 - x337)^2) + 1 / sqrt((x40 - x58)^2 + (x180 - x198)^
    2 + (x320 - x338)^2) + 1 / sqrt((x40 - x59)^2 + (x180 - x199)^2 + (x320 -
    x339)^2) + 1 / sqrt((x40 - x60)^2 + (x180 - x200)^2 + (x320 - x340)^2) + 1
    / sqrt((x40 - x61)^2 + (x180 - x201)^2 + (x320 - x341)^2) + 1 / sqrt((x40
    - x62)^2 + (x180 - x202)^2 + (x320 - x342)^2) + 1 / sqrt((x40 - x63)^2 + (
    x180 - x203)^2 + (x320 - x343)^2) + 1 / sqrt((x40 - x64)^2 + (x180 - x204)^
    2 + (x320 - x344)^2) + 1 / sqrt((x40 - x65)^2 + (x180 - x205)^2 + (x320 -
    x345)^2) + 1 / sqrt((x40 - x66)^2 + (x180 - x206)^2 + (x320 - x346)^2) + 1
    / sqrt((x40 - x67)^2 + (x180 - x207)^2 + (x320 - x347)^2) + 1 / sqrt((x40
    - x68)^2 + (x180 - x208)^2 + (x320 - x348)^2) + 1 / sqrt((x40 - x69)^2 + (
    x180 - x209)^2 + (x320 - x349)^2) + 1 / sqrt((x40 - x70)^2 + (x180 - x210)^
    2 + (x320 - x350)^2) + 1 / sqrt((x40 - x71)^2 + (x180 - x211)^2 + (x320 -
    x351)^2) + 1 / sqrt((x40 - x72)^2 + (x180 - x212)^2 + (x320 - x352)^2) + 1
    / sqrt((x40 - x73)^2 + (x180 - x213)^2 + (x320 - x353)^2) + 1 / sqrt((x40
    - x74)^2 + (x180 - x214)^2 + (x320 - x354)^2) + 1 / sqrt((x40 - x75)^2 + (
    x180 - x215)^2 + (x320 - x355)^2) + 1 / sqrt((x40 - x76)^2 + (x180 - x216)^
    2 + (x320 - x356)^2) + 1 / sqrt((x40 - x77)^2 + (x180 - x217)^2 + (x320 -
    x357)^2) + 1 / sqrt((x40 - x78)^2 + (x180 - x218)^2 + (x320 - x358)^2) + 1
    / sqrt((x40 - x79)^2 + (x180 - x219)^2 + (x320 - x359)^2) + 1 / sqrt((x40
    - x80)^2 + (x180 - x220)^2 + (x320 - x360)^2) + 1 / sqrt((x40 - x81)^2 + (
    x180 - x221)^2 + (x320 - x361)^2) + 1 / sqrt((x40 - x82)^2 + (x180 - x222)^
    2 + (x320 - x362)^2) + 1 / sqrt((x40 - x83)^2 + (x180 - x223)^2 + (x320 -
    x363)^2) + 1 / sqrt((x40 - x84)^2 + (x180 - x224)^2 + (x320 - x364)^2) + 1
    / sqrt((x40 - x85)^2 + (x180 - x225)^2 + (x320 - x365)^2) + 1 / sqrt((x40
    - x86)^2 + (x180 - x226)^2 + (x320 - x366)^2) + 1 / sqrt((x40 - x87)^2 + (
    x180 - x227)^2 + (x320 - x367)^2) + 1 / sqrt((x40 - x88)^2 + (x180 - x228)^
    2 + (x320 - x368)^2) + 1 / sqrt((x40 - x89)^2 + (x180 - x229)^2 + (x320 -
    x369)^2) + 1 / sqrt((x40 - x90)^2 + (x180 - x230)^2 + (x320 - x370)^2) + 1
    / sqrt((x40 - x91)^2 + (x180 - x231)^2 + (x320 - x371)^2) + 1 / sqrt((x40
    - x92)^2 + (x180 - x232)^2 + (x320 - x372)^2) + 1 / sqrt((x40 - x93)^2 + (
    x180 - x233)^2 + (x320 - x373)^2) + 1 / sqrt((x40 - x94)^2 + (x180 - x234)^
    2 + (x320 - x374)^2) + 1 / sqrt((x40 - x95)^2 + (x180 - x235)^2 + (x320 -
    x375)^2) + 1 / sqrt((x40 - x96)^2 + (x180 - x236)^2 + (x320 - x376)^2) + 1
    / sqrt((x40 - x97)^2 + (x180 - x237)^2 + (x320 - x377)^2) + 1 / sqrt((x40
    - x98)^2 + (x180 - x238)^2 + (x320 - x378)^2) + 1 / sqrt((x40 - x99)^2 + (
    x180 - x239)^2 + (x320 - x379)^2) + 1 / sqrt((x40 - x100)^2 + (x180 - x240)
    ^2 + (x320 - x380)^2) + 1 / sqrt((x40 - x101)^2 + (x180 - x241)^2 + (x320
    - x381)^2) + 1 / sqrt((x40 - x102)^2 + (x180 - x242)^2 + (x320 - x382)^2)
    + 1 / sqrt((x40 - x103)^2 + (x180 - x243)^2 + (x320 - x383)^2) + 1 / sqrt(
    (x40 - x104)^2 + (x180 - x244)^2 + (x320 - x384)^2) + 1 / sqrt((x40 - x105)
    ^2 + (x180 - x245)^2 + (x320 - x385)^2) + 1 / sqrt((x40 - x106)^2 + (x180
    - x246)^2 + (x320 - x386)^2) + 1 / sqrt((x40 - x107)^2 + (x180 - x247)^2
    + (x320 - x387)^2) + 1 / sqrt((x40 - x108)^2 + (x180 - x248)^2 + (x320 -
    x388)^2) + 1 / sqrt((x40 - x109)^2 + (x180 - x249)^2 + (x320 - x389)^2) + 1
    / sqrt((x40 - x110)^2 + (x180 - x250)^2 + (x320 - x390)^2) + 1 / sqrt((x40
    - x111)^2 + (x180 - x251)^2 + (x320 - x391)^2) + 1 / sqrt((x40 - x112)^2
    + (x180 - x252)^2 + (x320 - x392)^2) + 1 / sqrt((x40 - x113)^2 + (x180 -
    x253)^2 + (x320 - x393)^2) + 1 / sqrt((x40 - x114)^2 + (x180 - x254)^2 + (
    x320 - x394)^2) + 1 / sqrt((x40 - x115)^2 + (x180 - x255)^2 + (x320 - x395)
    ^2) + 1 / sqrt((x40 - x116)^2 + (x180 - x256)^2 + (x320 - x396)^2) + 1 /
    sqrt((x40 - x117)^2 + (x180 - x257)^2 + (x320 - x397)^2) + 1 / sqrt((x40 -
    x118)^2 + (x180 - x258)^2 + (x320 - x398)^2) + 1 / sqrt((x40 - x119)^2 + (
    x180 - x259)^2 + (x320 - x399)^2) + 1 / sqrt((x40 - x120)^2 + (x180 - x260)
    ^2 + (x320 - x400)^2) + 1 / sqrt((x40 - x121)^2 + (x180 - x261)^2 + (x320
    - x401)^2) + 1 / sqrt((x40 - x122)^2 + (x180 - x262)^2 + (x320 - x402)^2)
    + 1 / sqrt((x40 - x123)^2 + (x180 - x263)^2 + (x320 - x403)^2) + 1 / sqrt(
    (x40 - x124)^2 + (x180 - x264)^2 + (x320 - x404)^2) + 1 / sqrt((x40 - x125)
    ^2 + (x180 - x265)^2 + (x320 - x405)^2) + 1 / sqrt((x40 - x126)^2 + (x180
    - x266)^2 + (x320 - x406)^2) + 1 / sqrt((x40 - x127)^2 + (x180 - x267)^2
    + (x320 - x407)^2) + 1 / sqrt((x40 - x128)^2 + (x180 - x268)^2 + (x320 -
    x408)^2) + 1 / sqrt((x40 - x129)^2 + (x180 - x269)^2 + (x320 - x409)^2) + 1
    / sqrt((x40 - x130)^2 + (x180 - x270)^2 + (x320 - x410)^2) + 1 / sqrt((x40
    - x131)^2 + (x180 - x271)^2 + (x320 - x411)^2) + 1 / sqrt((x40 - x132)^2
    + (x180 - x272)^2 + (x320 - x412)^2) + 1 / sqrt((x40 - x133)^2 + (x180 -
    x273)^2 + (x320 - x413)^2) + 1 / sqrt((x40 - x134)^2 + (x180 - x274)^2 + (
    x320 - x414)^2) + 1 / sqrt((x40 - x135)^2 + (x180 - x275)^2 + (x320 - x415)
    ^2) + 1 / sqrt((x40 - x136)^2 + (x180 - x276)^2 + (x320 - x416)^2) + 1 /
    sqrt((x40 - x137)^2 + (x180 - x277)^2 + (x320 - x417)^2) + 1 / sqrt((x40 -
    x138)^2 + (x180 - x278)^2 + (x320 - x418)^2) + 1 / sqrt((x40 - x139)^2 + (
    x180 - x279)^2 + (x320 - x419)^2) + 1 / sqrt((x40 - x140)^2 + (x180 - x280)
    ^2 + (x320 - x420)^2) + 1 / sqrt((x41 - x42)^2 + (x181 - x182)^2 + (x321 -
    x322)^2) + 1 / sqrt((x41 - x43)^2 + (x181 - x183)^2 + (x321 - x323)^2) + 1
    / sqrt((x41 - x44)^2 + (x181 - x184)^2 + (x321 - x324)^2) + 1 / sqrt((x41
    - x45)^2 + (x181 - x185)^2 + (x321 - x325)^2) + 1 / sqrt((x41 - x46)^2 + (
    x181 - x186)^2 + (x321 - x326)^2) + 1 / sqrt((x41 - x47)^2 + (x181 - x187)^
    2 + (x321 - x327)^2) + 1 / sqrt((x41 - x48)^2 + (x181 - x188)^2 + (x321 -
    x328)^2) + 1 / sqrt((x41 - x49)^2 + (x181 - x189)^2 + (x321 - x329)^2) + 1
    / sqrt((x41 - x50)^2 + (x181 - x190)^2 + (x321 - x330)^2) + 1 / sqrt((x41
    - x51)^2 + (x181 - x191)^2 + (x321 - x331)^2) + 1 / sqrt((x41 - x52)^2 + (
    x181 - x192)^2 + (x321 - x332)^2) + 1 / sqrt((x41 - x53)^2 + (x181 - x193)^
    2 + (x321 - x333)^2) + 1 / sqrt((x41 - x54)^2 + (x181 - x194)^2 + (x321 -
    x334)^2) + 1 / sqrt((x41 - x55)^2 + (x181 - x195)^2 + (x321 - x335)^2) + 1
    / sqrt((x41 - x56)^2 + (x181 - x196)^2 + (x321 - x336)^2) + 1 / sqrt((x41
    - x57)^2 + (x181 - x197)^2 + (x321 - x337)^2) + 1 / sqrt((x41 - x58)^2 + (
    x181 - x198)^2 + (x321 - x338)^2) + 1 / sqrt((x41 - x59)^2 + (x181 - x199)^
    2 + (x321 - x339)^2) + 1 / sqrt((x41 - x60)^2 + (x181 - x200)^2 + (x321 -
    x340)^2) + 1 / sqrt((x41 - x61)^2 + (x181 - x201)^2 + (x321 - x341)^2) + 1
    / sqrt((x41 - x62)^2 + (x181 - x202)^2 + (x321 - x342)^2) + 1 / sqrt((x41
    - x63)^2 + (x181 - x203)^2 + (x321 - x343)^2) + 1 / sqrt((x41 - x64)^2 + (
    x181 - x204)^2 + (x321 - x344)^2) + 1 / sqrt((x41 - x65)^2 + (x181 - x205)^
    2 + (x321 - x345)^2) + 1 / sqrt((x41 - x66)^2 + (x181 - x206)^2 + (x321 -
    x346)^2) + 1 / sqrt((x41 - x67)^2 + (x181 - x207)^2 + (x321 - x347)^2) + 1
    / sqrt((x41 - x68)^2 + (x181 - x208)^2 + (x321 - x348)^2) + 1 / sqrt((x41
    - x69)^2 + (x181 - x209)^2 + (x321 - x349)^2) + 1 / sqrt((x41 - x70)^2 + (
    x181 - x210)^2 + (x321 - x350)^2) + 1 / sqrt((x41 - x71)^2 + (x181 - x211)^
    2 + (x321 - x351)^2) + 1 / sqrt((x41 - x72)^2 + (x181 - x212)^2 + (x321 -
    x352)^2) + 1 / sqrt((x41 - x73)^2 + (x181 - x213)^2 + (x321 - x353)^2) + 1
    / sqrt((x41 - x74)^2 + (x181 - x214)^2 + (x321 - x354)^2) + 1 / sqrt((x41
    - x75)^2 + (x181 - x215)^2 + (x321 - x355)^2) + 1 / sqrt((x41 - x76)^2 + (
    x181 - x216)^2 + (x321 - x356)^2) + 1 / sqrt((x41 - x77)^2 + (x181 - x217)^
    2 + (x321 - x357)^2) + 1 / sqrt((x41 - x78)^2 + (x181 - x218)^2 + (x321 -
    x358)^2) + 1 / sqrt((x41 - x79)^2 + (x181 - x219)^2 + (x321 - x359)^2) + 1
    / sqrt((x41 - x80)^2 + (x181 - x220)^2 + (x321 - x360)^2) + 1 / sqrt((x41
    - x81)^2 + (x181 - x221)^2 + (x321 - x361)^2) + 1 / sqrt((x41 - x82)^2 + (
    x181 - x222)^2 + (x321 - x362)^2) + 1 / sqrt((x41 - x83)^2 + (x181 - x223)^
    2 + (x321 - x363)^2) + 1 / sqrt((x41 - x84)^2 + (x181 - x224)^2 + (x321 -
    x364)^2) + 1 / sqrt((x41 - x85)^2 + (x181 - x225)^2 + (x321 - x365)^2) + 1
    / sqrt((x41 - x86)^2 + (x181 - x226)^2 + (x321 - x366)^2) + 1 / sqrt((x41
    - x87)^2 + (x181 - x227)^2 + (x321 - x367)^2) + 1 / sqrt((x41 - x88)^2 + (
    x181 - x228)^2 + (x321 - x368)^2) + 1 / sqrt((x41 - x89)^2 + (x181 - x229)^
    2 + (x321 - x369)^2) + 1 / sqrt((x41 - x90)^2 + (x181 - x230)^2 + (x321 -
    x370)^2) + 1 / sqrt((x41 - x91)^2 + (x181 - x231)^2 + (x321 - x371)^2) + 1
    / sqrt((x41 - x92)^2 + (x181 - x232)^2 + (x321 - x372)^2) + 1 / sqrt((x41
    - x93)^2 + (x181 - x233)^2 + (x321 - x373)^2) + 1 / sqrt((x41 - x94)^2 + (
    x181 - x234)^2 + (x321 - x374)^2) + 1 / sqrt((x41 - x95)^2 + (x181 - x235)^
    2 + (x321 - x375)^2) + 1 / sqrt((x41 - x96)^2 + (x181 - x236)^2 + (x321 -
    x376)^2) + 1 / sqrt((x41 - x97)^2 + (x181 - x237)^2 + (x321 - x377)^2) + 1
    / sqrt((x41 - x98)^2 + (x181 - x238)^2 + (x321 - x378)^2) + 1 / sqrt((x41
    - x99)^2 + (x181 - x239)^2 + (x321 - x379)^2) + 1 / sqrt((x41 - x100)^2 +
    (x181 - x240)^2 + (x321 - x380)^2) + 1 / sqrt((x41 - x101)^2 + (x181 - x241)
    ^2 + (x321 - x381)^2) + 1 / sqrt((x41 - x102)^2 + (x181 - x242)^2 + (x321
    - x382)^2) + 1 / sqrt((x41 - x103)^2 + (x181 - x243)^2 + (x321 - x383)^2)
    + 1 / sqrt((x41 - x104)^2 + (x181 - x244)^2 + (x321 - x384)^2) + 1 / sqrt(
    (x41 - x105)^2 + (x181 - x245)^2 + (x321 - x385)^2) + 1 / sqrt((x41 - x106)
    ^2 + (x181 - x246)^2 + (x321 - x386)^2) + 1 / sqrt((x41 - x107)^2 + (x181
    - x247)^2 + (x321 - x387)^2) + 1 / sqrt((x41 - x108)^2 + (x181 - x248)^2
    + (x321 - x388)^2) + 1 / sqrt((x41 - x109)^2 + (x181 - x249)^2 + (x321 -
    x389)^2) + 1 / sqrt((x41 - x110)^2 + (x181 - x250)^2 + (x321 - x390)^2) + 1
    / sqrt((x41 - x111)^2 + (x181 - x251)^2 + (x321 - x391)^2) + 1 / sqrt((x41
    - x112)^2 + (x181 - x252)^2 + (x321 - x392)^2) + 1 / sqrt((x41 - x113)^2
    + (x181 - x253)^2 + (x321 - x393)^2) + 1 / sqrt((x41 - x114)^2 + (x181 -
    x254)^2 + (x321 - x394)^2) + 1 / sqrt((x41 - x115)^2 + (x181 - x255)^2 + (
    x321 - x395)^2) + 1 / sqrt((x41 - x116)^2 + (x181 - x256)^2 + (x321 - x396)
    ^2) + 1 / sqrt((x41 - x117)^2 + (x181 - x257)^2 + (x321 - x397)^2) + 1 /
    sqrt((x41 - x118)^2 + (x181 - x258)^2 + (x321 - x398)^2) + 1 / sqrt((x41 -
    x119)^2 + (x181 - x259)^2 + (x321 - x399)^2) + 1 / sqrt((x41 - x120)^2 + (
    x181 - x260)^2 + (x321 - x400)^2) + 1 / sqrt((x41 - x121)^2 + (x181 - x261)
    ^2 + (x321 - x401)^2) + 1 / sqrt((x41 - x122)^2 + (x181 - x262)^2 + (x321
    - x402)^2) + 1 / sqrt((x41 - x123)^2 + (x181 - x263)^2 + (x321 - x403)^2)
    + 1 / sqrt((x41 - x124)^2 + (x181 - x264)^2 + (x321 - x404)^2) + 1 / sqrt(
    (x41 - x125)^2 + (x181 - x265)^2 + (x321 - x405)^2) + 1 / sqrt((x41 - x126)
    ^2 + (x181 - x266)^2 + (x321 - x406)^2) + 1 / sqrt((x41 - x127)^2 + (x181
    - x267)^2 + (x321 - x407)^2) + 1 / sqrt((x41 - x128)^2 + (x181 - x268)^2
    + (x321 - x408)^2) + 1 / sqrt((x41 - x129)^2 + (x181 - x269)^2 + (x321 -
    x409)^2) + 1 / sqrt((x41 - x130)^2 + (x181 - x270)^2 + (x321 - x410)^2) + 1
    / sqrt((x41 - x131)^2 + (x181 - x271)^2 + (x321 - x411)^2) + 1 / sqrt((x41
    - x132)^2 + (x181 - x272)^2 + (x321 - x412)^2) + 1 / sqrt((x41 - x133)^2
    + (x181 - x273)^2 + (x321 - x413)^2) + 1 / sqrt((x41 - x134)^2 + (x181 -
    x274)^2 + (x321 - x414)^2) + 1 / sqrt((x41 - x135)^2 + (x181 - x275)^2 + (
    x321 - x415)^2) + 1 / sqrt((x41 - x136)^2 + (x181 - x276)^2 + (x321 - x416)
    ^2) + 1 / sqrt((x41 - x137)^2 + (x181 - x277)^2 + (x321 - x417)^2) + 1 /
    sqrt((x41 - x138)^2 + (x181 - x278)^2 + (x321 - x418)^2) + 1 / sqrt((x41 -
    x139)^2 + (x181 - x279)^2 + (x321 - x419)^2) + 1 / sqrt((x41 - x140)^2 + (
    x181 - x280)^2 + (x321 - x420)^2) + 1 / sqrt((x42 - x43)^2 + (x182 - x183)^
    2 + (x322 - x323)^2) + 1 / sqrt((x42 - x44)^2 + (x182 - x184)^2 + (x322 -
    x324)^2) + 1 / sqrt((x42 - x45)^2 + (x182 - x185)^2 + (x322 - x325)^2) + 1
    / sqrt((x42 - x46)^2 + (x182 - x186)^2 + (x322 - x326)^2) + 1 / sqrt((x42
    - x47)^2 + (x182 - x187)^2 + (x322 - x327)^2) + 1 / sqrt((x42 - x48)^2 + (
    x182 - x188)^2 + (x322 - x328)^2) + 1 / sqrt((x42 - x49)^2 + (x182 - x189)^
    2 + (x322 - x329)^2) + 1 / sqrt((x42 - x50)^2 + (x182 - x190)^2 + (x322 -
    x330)^2) + 1 / sqrt((x42 - x51)^2 + (x182 - x191)^2 + (x322 - x331)^2) + 1
    / sqrt((x42 - x52)^2 + (x182 - x192)^2 + (x322 - x332)^2) + 1 / sqrt((x42
    - x53)^2 + (x182 - x193)^2 + (x322 - x333)^2) + 1 / sqrt((x42 - x54)^2 + (
    x182 - x194)^2 + (x322 - x334)^2) + 1 / sqrt((x42 - x55)^2 + (x182 - x195)^
    2 + (x322 - x335)^2) + 1 / sqrt((x42 - x56)^2 + (x182 - x196)^2 + (x322 -
    x336)^2) + 1 / sqrt((x42 - x57)^2 + (x182 - x197)^2 + (x322 - x337)^2) + 1
    / sqrt((x42 - x58)^2 + (x182 - x198)^2 + (x322 - x338)^2) + 1 / sqrt((x42
    - x59)^2 + (x182 - x199)^2 + (x322 - x339)^2) + 1 / sqrt((x42 - x60)^2 + (
    x182 - x200)^2 + (x322 - x340)^2) + 1 / sqrt((x42 - x61)^2 + (x182 - x201)^
    2 + (x322 - x341)^2) + 1 / sqrt((x42 - x62)^2 + (x182 - x202)^2 + (x322 -
    x342)^2) + 1 / sqrt((x42 - x63)^2 + (x182 - x203)^2 + (x322 - x343)^2) + 1
    / sqrt((x42 - x64)^2 + (x182 - x204)^2 + (x322 - x344)^2) + 1 / sqrt((x42
    - x65)^2 + (x182 - x205)^2 + (x322 - x345)^2) + 1 / sqrt((x42 - x66)^2 + (
    x182 - x206)^2 + (x322 - x346)^2) + 1 / sqrt((x42 - x67)^2 + (x182 - x207)^
    2 + (x322 - x347)^2) + 1 / sqrt((x42 - x68)^2 + (x182 - x208)^2 + (x322 -
    x348)^2) + 1 / sqrt((x42 - x69)^2 + (x182 - x209)^2 + (x322 - x349)^2) + 1
    / sqrt((x42 - x70)^2 + (x182 - x210)^2 + (x322 - x350)^2) + 1 / sqrt((x42
    - x71)^2 + (x182 - x211)^2 + (x322 - x351)^2) + 1 / sqrt((x42 - x72)^2 + (
    x182 - x212)^2 + (x322 - x352)^2) + 1 / sqrt((x42 - x73)^2 + (x182 - x213)^
    2 + (x322 - x353)^2) + 1 / sqrt((x42 - x74)^2 + (x182 - x214)^2 + (x322 -
    x354)^2) + 1 / sqrt((x42 - x75)^2 + (x182 - x215)^2 + (x322 - x355)^2) + 1
    / sqrt((x42 - x76)^2 + (x182 - x216)^2 + (x322 - x356)^2) + 1 / sqrt((x42
    - x77)^2 + (x182 - x217)^2 + (x322 - x357)^2) + 1 / sqrt((x42 - x78)^2 + (
    x182 - x218)^2 + (x322 - x358)^2) + 1 / sqrt((x42 - x79)^2 + (x182 - x219)^
    2 + (x322 - x359)^2) + 1 / sqrt((x42 - x80)^2 + (x182 - x220)^2 + (x322 -
    x360)^2) + 1 / sqrt((x42 - x81)^2 + (x182 - x221)^2 + (x322 - x361)^2) + 1
    / sqrt((x42 - x82)^2 + (x182 - x222)^2 + (x322 - x362)^2) + 1 / sqrt((x42
    - x83)^2 + (x182 - x223)^2 + (x322 - x363)^2) + 1 / sqrt((x42 - x84)^2 + (
    x182 - x224)^2 + (x322 - x364)^2) + 1 / sqrt((x42 - x85)^2 + (x182 - x225)^
    2 + (x322 - x365)^2) + 1 / sqrt((x42 - x86)^2 + (x182 - x226)^2 + (x322 -
    x366)^2) + 1 / sqrt((x42 - x87)^2 + (x182 - x227)^2 + (x322 - x367)^2) + 1
    / sqrt((x42 - x88)^2 + (x182 - x228)^2 + (x322 - x368)^2) + 1 / sqrt((x42
    - x89)^2 + (x182 - x229)^2 + (x322 - x369)^2) + 1 / sqrt((x42 - x90)^2 + (
    x182 - x230)^2 + (x322 - x370)^2) + 1 / sqrt((x42 - x91)^2 + (x182 - x231)^
    2 + (x322 - x371)^2) + 1 / sqrt((x42 - x92)^2 + (x182 - x232)^2 + (x322 -
    x372)^2) + 1 / sqrt((x42 - x93)^2 + (x182 - x233)^2 + (x322 - x373)^2) + 1
    / sqrt((x42 - x94)^2 + (x182 - x234)^2 + (x322 - x374)^2) + 1 / sqrt((x42
    - x95)^2 + (x182 - x235)^2 + (x322 - x375)^2) + 1 / sqrt((x42 - x96)^2 + (
    x182 - x236)^2 + (x322 - x376)^2) + 1 / sqrt((x42 - x97)^2 + (x182 - x237)^
    2 + (x322 - x377)^2) + 1 / sqrt((x42 - x98)^2 + (x182 - x238)^2 + (x322 -
    x378)^2) + 1 / sqrt((x42 - x99)^2 + (x182 - x239)^2 + (x322 - x379)^2) + 1
    / sqrt((x42 - x100)^2 + (x182 - x240)^2 + (x322 - x380)^2) + 1 / sqrt((x42
    - x101)^2 + (x182 - x241)^2 + (x322 - x381)^2) + 1 / sqrt((x42 - x102)^2
    + (x182 - x242)^2 + (x322 - x382)^2) + 1 / sqrt((x42 - x103)^2 + (x182 -
    x243)^2 + (x322 - x383)^2) + 1 / sqrt((x42 - x104)^2 + (x182 - x244)^2 + (
    x322 - x384)^2) + 1 / sqrt((x42 - x105)^2 + (x182 - x245)^2 + (x322 - x385)
    ^2) + 1 / sqrt((x42 - x106)^2 + (x182 - x246)^2 + (x322 - x386)^2) + 1 /
    sqrt((x42 - x107)^2 + (x182 - x247)^2 + (x322 - x387)^2) + 1 / sqrt((x42 -
    x108)^2 + (x182 - x248)^2 + (x322 - x388)^2) + 1 / sqrt((x42 - x109)^2 + (
    x182 - x249)^2 + (x322 - x389)^2) + 1 / sqrt((x42 - x110)^2 + (x182 - x250)
    ^2 + (x322 - x390)^2) + 1 / sqrt((x42 - x111)^2 + (x182 - x251)^2 + (x322
    - x391)^2) + 1 / sqrt((x42 - x112)^2 + (x182 - x252)^2 + (x322 - x392)^2)
    + 1 / sqrt((x42 - x113)^2 + (x182 - x253)^2 + (x322 - x393)^2) + 1 / sqrt(
    (x42 - x114)^2 + (x182 - x254)^2 + (x322 - x394)^2) + 1 / sqrt((x42 - x115)
    ^2 + (x182 - x255)^2 + (x322 - x395)^2) + 1 / sqrt((x42 - x116)^2 + (x182
    - x256)^2 + (x322 - x396)^2) + 1 / sqrt((x42 - x117)^2 + (x182 - x257)^2
    + (x322 - x397)^2) + 1 / sqrt((x42 - x118)^2 + (x182 - x258)^2 + (x322 -
    x398)^2) + 1 / sqrt((x42 - x119)^2 + (x182 - x259)^2 + (x322 - x399)^2) + 1
    / sqrt((x42 - x120)^2 + (x182 - x260)^2 + (x322 - x400)^2) + 1 / sqrt((x42
    - x121)^2 + (x182 - x261)^2 + (x322 - x401)^2) + 1 / sqrt((x42 - x122)^2
    + (x182 - x262)^2 + (x322 - x402)^2) + 1 / sqrt((x42 - x123)^2 + (x182 -
    x263)^2 + (x322 - x403)^2) + 1 / sqrt((x42 - x124)^2 + (x182 - x264)^2 + (
    x322 - x404)^2) + 1 / sqrt((x42 - x125)^2 + (x182 - x265)^2 + (x322 - x405)
    ^2) + 1 / sqrt((x42 - x126)^2 + (x182 - x266)^2 + (x322 - x406)^2) + 1 /
    sqrt((x42 - x127)^2 + (x182 - x267)^2 + (x322 - x407)^2) + 1 / sqrt((x42 -
    x128)^2 + (x182 - x268)^2 + (x322 - x408)^2) + 1 / sqrt((x42 - x129)^2 + (
    x182 - x269)^2 + (x322 - x409)^2) + 1 / sqrt((x42 - x130)^2 + (x182 - x270)
    ^2 + (x322 - x410)^2) + 1 / sqrt((x42 - x131)^2 + (x182 - x271)^2 + (x322
    - x411)^2) + 1 / sqrt((x42 - x132)^2 + (x182 - x272)^2 + (x322 - x412)^2)
    + 1 / sqrt((x42 - x133)^2 + (x182 - x273)^2 + (x322 - x413)^2) + 1 / sqrt(
    (x42 - x134)^2 + (x182 - x274)^2 + (x322 - x414)^2) + 1 / sqrt((x42 - x135)
    ^2 + (x182 - x275)^2 + (x322 - x415)^2) + 1 / sqrt((x42 - x136)^2 + (x182
    - x276)^2 + (x322 - x416)^2) + 1 / sqrt((x42 - x137)^2 + (x182 - x277)^2
    + (x322 - x417)^2) + 1 / sqrt((x42 - x138)^2 + (x182 - x278)^2 + (x322 -
    x418)^2) + 1 / sqrt((x42 - x139)^2 + (x182 - x279)^2 + (x322 - x419)^2) + 1
    / sqrt((x42 - x140)^2 + (x182 - x280)^2 + (x322 - x420)^2) + 1 / sqrt((x43
    - x44)^2 + (x183 - x184)^2 + (x323 - x324)^2) + 1 / sqrt((x43 - x45)^2 + (
    x183 - x185)^2 + (x323 - x325)^2) + 1 / sqrt((x43 - x46)^2 + (x183 - x186)^
    2 + (x323 - x326)^2) + 1 / sqrt((x43 - x47)^2 + (x183 - x187)^2 + (x323 -
    x327)^2) + 1 / sqrt((x43 - x48)^2 + (x183 - x188)^2 + (x323 - x328)^2) + 1
    / sqrt((x43 - x49)^2 + (x183 - x189)^2 + (x323 - x329)^2) + 1 / sqrt((x43
    - x50)^2 + (x183 - x190)^2 + (x323 - x330)^2) + 1 / sqrt((x43 - x51)^2 + (
    x183 - x191)^2 + (x323 - x331)^2) + 1 / sqrt((x43 - x52)^2 + (x183 - x192)^
    2 + (x323 - x332)^2) + 1 / sqrt((x43 - x53)^2 + (x183 - x193)^2 + (x323 -
    x333)^2) + 1 / sqrt((x43 - x54)^2 + (x183 - x194)^2 + (x323 - x334)^2) + 1
    / sqrt((x43 - x55)^2 + (x183 - x195)^2 + (x323 - x335)^2) + 1 / sqrt((x43
    - x56)^2 + (x183 - x196)^2 + (x323 - x336)^2) + 1 / sqrt((x43 - x57)^2 + (
    x183 - x197)^2 + (x323 - x337)^2) + 1 / sqrt((x43 - x58)^2 + (x183 - x198)^
    2 + (x323 - x338)^2) + 1 / sqrt((x43 - x59)^2 + (x183 - x199)^2 + (x323 -
    x339)^2) + 1 / sqrt((x43 - x60)^2 + (x183 - x200)^2 + (x323 - x340)^2) + 1
    / sqrt((x43 - x61)^2 + (x183 - x201)^2 + (x323 - x341)^2) + 1 / sqrt((x43
    - x62)^2 + (x183 - x202)^2 + (x323 - x342)^2) + 1 / sqrt((x43 - x63)^2 + (
    x183 - x203)^2 + (x323 - x343)^2) + 1 / sqrt((x43 - x64)^2 + (x183 - x204)^
    2 + (x323 - x344)^2) + 1 / sqrt((x43 - x65)^2 + (x183 - x205)^2 + (x323 -
    x345)^2) + 1 / sqrt((x43 - x66)^2 + (x183 - x206)^2 + (x323 - x346)^2) + 1
    / sqrt((x43 - x67)^2 + (x183 - x207)^2 + (x323 - x347)^2) + 1 / sqrt((x43
    - x68)^2 + (x183 - x208)^2 + (x323 - x348)^2) + 1 / sqrt((x43 - x69)^2 + (
    x183 - x209)^2 + (x323 - x349)^2) + 1 / sqrt((x43 - x70)^2 + (x183 - x210)^
    2 + (x323 - x350)^2) + 1 / sqrt((x43 - x71)^2 + (x183 - x211)^2 + (x323 -
    x351)^2) + 1 / sqrt((x43 - x72)^2 + (x183 - x212)^2 + (x323 - x352)^2) + 1
    / sqrt((x43 - x73)^2 + (x183 - x213)^2 + (x323 - x353)^2) + 1 / sqrt((x43
    - x74)^2 + (x183 - x214)^2 + (x323 - x354)^2) + 1 / sqrt((x43 - x75)^2 + (
    x183 - x215)^2 + (x323 - x355)^2) + 1 / sqrt((x43 - x76)^2 + (x183 - x216)^
    2 + (x323 - x356)^2) + 1 / sqrt((x43 - x77)^2 + (x183 - x217)^2 + (x323 -
    x357)^2) + 1 / sqrt((x43 - x78)^2 + (x183 - x218)^2 + (x323 - x358)^2) + 1
    / sqrt((x43 - x79)^2 + (x183 - x219)^2 + (x323 - x359)^2) + 1 / sqrt((x43
    - x80)^2 + (x183 - x220)^2 + (x323 - x360)^2) + 1 / sqrt((x43 - x81)^2 + (
    x183 - x221)^2 + (x323 - x361)^2) + 1 / sqrt((x43 - x82)^2 + (x183 - x222)^
    2 + (x323 - x362)^2) + 1 / sqrt((x43 - x83)^2 + (x183 - x223)^2 + (x323 -
    x363)^2) + 1 / sqrt((x43 - x84)^2 + (x183 - x224)^2 + (x323 - x364)^2) + 1
    / sqrt((x43 - x85)^2 + (x183 - x225)^2 + (x323 - x365)^2) + 1 / sqrt((x43
    - x86)^2 + (x183 - x226)^2 + (x323 - x366)^2) + 1 / sqrt((x43 - x87)^2 + (
    x183 - x227)^2 + (x323 - x367)^2) + 1 / sqrt((x43 - x88)^2 + (x183 - x228)^
    2 + (x323 - x368)^2) + 1 / sqrt((x43 - x89)^2 + (x183 - x229)^2 + (x323 -
    x369)^2) + 1 / sqrt((x43 - x90)^2 + (x183 - x230)^2 + (x323 - x370)^2) + 1
    / sqrt((x43 - x91)^2 + (x183 - x231)^2 + (x323 - x371)^2) + 1 / sqrt((x43
    - x92)^2 + (x183 - x232)^2 + (x323 - x372)^2) + 1 / sqrt((x43 - x93)^2 + (
    x183 - x233)^2 + (x323 - x373)^2) + 1 / sqrt((x43 - x94)^2 + (x183 - x234)^
    2 + (x323 - x374)^2) + 1 / sqrt((x43 - x95)^2 + (x183 - x235)^2 + (x323 -
    x375)^2) + 1 / sqrt((x43 - x96)^2 + (x183 - x236)^2 + (x323 - x376)^2) + 1
    / sqrt((x43 - x97)^2 + (x183 - x237)^2 + (x323 - x377)^2) + 1 / sqrt((x43
    - x98)^2 + (x183 - x238)^2 + (x323 - x378)^2) + 1 / sqrt((x43 - x99)^2 + (
    x183 - x239)^2 + (x323 - x379)^2) + 1 / sqrt((x43 - x100)^2 + (x183 - x240)
    ^2 + (x323 - x380)^2) + 1 / sqrt((x43 - x101)^2 + (x183 - x241)^2 + (x323
    - x381)^2) + 1 / sqrt((x43 - x102)^2 + (x183 - x242)^2 + (x323 - x382)^2)
    + 1 / sqrt((x43 - x103)^2 + (x183 - x243)^2 + (x323 - x383)^2) + 1 / sqrt(
    (x43 - x104)^2 + (x183 - x244)^2 + (x323 - x384)^2) + 1 / sqrt((x43 - x105)
    ^2 + (x183 - x245)^2 + (x323 - x385)^2) + 1 / sqrt((x43 - x106)^2 + (x183
    - x246)^2 + (x323 - x386)^2) + 1 / sqrt((x43 - x107)^2 + (x183 - x247)^2
    + (x323 - x387)^2) + 1 / sqrt((x43 - x108)^2 + (x183 - x248)^2 + (x323 -
    x388)^2) + 1 / sqrt((x43 - x109)^2 + (x183 - x249)^2 + (x323 - x389)^2) + 1
    / sqrt((x43 - x110)^2 + (x183 - x250)^2 + (x323 - x390)^2) + 1 / sqrt((x43
    - x111)^2 + (x183 - x251)^2 + (x323 - x391)^2) + 1 / sqrt((x43 - x112)^2
    + (x183 - x252)^2 + (x323 - x392)^2) + 1 / sqrt((x43 - x113)^2 + (x183 -
    x253)^2 + (x323 - x393)^2) + 1 / sqrt((x43 - x114)^2 + (x183 - x254)^2 + (
    x323 - x394)^2) + 1 / sqrt((x43 - x115)^2 + (x183 - x255)^2 + (x323 - x395)
    ^2) + 1 / sqrt((x43 - x116)^2 + (x183 - x256)^2 + (x323 - x396)^2) + 1 /
    sqrt((x43 - x117)^2 + (x183 - x257)^2 + (x323 - x397)^2) + 1 / sqrt((x43 -
    x118)^2 + (x183 - x258)^2 + (x323 - x398)^2) + 1 / sqrt((x43 - x119)^2 + (
    x183 - x259)^2 + (x323 - x399)^2) + 1 / sqrt((x43 - x120)^2 + (x183 - x260)
    ^2 + (x323 - x400)^2) + 1 / sqrt((x43 - x121)^2 + (x183 - x261)^2 + (x323
    - x401)^2) + 1 / sqrt((x43 - x122)^2 + (x183 - x262)^2 + (x323 - x402)^2)
    + 1 / sqrt((x43 - x123)^2 + (x183 - x263)^2 + (x323 - x403)^2) + 1 / sqrt(
    (x43 - x124)^2 + (x183 - x264)^2 + (x323 - x404)^2) + 1 / sqrt((x43 - x125)
    ^2 + (x183 - x265)^2 + (x323 - x405)^2) + 1 / sqrt((x43 - x126)^2 + (x183
    - x266)^2 + (x323 - x406)^2) + 1 / sqrt((x43 - x127)^2 + (x183 - x267)^2
    + (x323 - x407)^2) + 1 / sqrt((x43 - x128)^2 + (x183 - x268)^2 + (x323 -
    x408)^2) + 1 / sqrt((x43 - x129)^2 + (x183 - x269)^2 + (x323 - x409)^2) + 1
    / sqrt((x43 - x130)^2 + (x183 - x270)^2 + (x323 - x410)^2) + 1 / sqrt((x43
    - x131)^2 + (x183 - x271)^2 + (x323 - x411)^2) + 1 / sqrt((x43 - x132)^2
    + (x183 - x272)^2 + (x323 - x412)^2) + 1 / sqrt((x43 - x133)^2 + (x183 -
    x273)^2 + (x323 - x413)^2) + 1 / sqrt((x43 - x134)^2 + (x183 - x274)^2 + (
    x323 - x414)^2) + 1 / sqrt((x43 - x135)^2 + (x183 - x275)^2 + (x323 - x415)
    ^2) + 1 / sqrt((x43 - x136)^2 + (x183 - x276)^2 + (x323 - x416)^2) + 1 /
    sqrt((x43 - x137)^2 + (x183 - x277)^2 + (x323 - x417)^2) + 1 / sqrt((x43 -
    x138)^2 + (x183 - x278)^2 + (x323 - x418)^2) + 1 / sqrt((x43 - x139)^2 + (
    x183 - x279)^2 + (x323 - x419)^2) + 1 / sqrt((x43 - x140)^2 + (x183 - x280)
    ^2 + (x323 - x420)^2) + 1 / sqrt((x44 - x45)^2 + (x184 - x185)^2 + (x324 -
    x325)^2) + 1 / sqrt((x44 - x46)^2 + (x184 - x186)^2 + (x324 - x326)^2) + 1
    / sqrt((x44 - x47)^2 + (x184 - x187)^2 + (x324 - x327)^2) + 1 / sqrt((x44
    - x48)^2 + (x184 - x188)^2 + (x324 - x328)^2) + 1 / sqrt((x44 - x49)^2 + (
    x184 - x189)^2 + (x324 - x329)^2) + 1 / sqrt((x44 - x50)^2 + (x184 - x190)^
    2 + (x324 - x330)^2) + 1 / sqrt((x44 - x51)^2 + (x184 - x191)^2 + (x324 -
    x331)^2) + 1 / sqrt((x44 - x52)^2 + (x184 - x192)^2 + (x324 - x332)^2) + 1
    / sqrt((x44 - x53)^2 + (x184 - x193)^2 + (x324 - x333)^2) + 1 / sqrt((x44
    - x54)^2 + (x184 - x194)^2 + (x324 - x334)^2) + 1 / sqrt((x44 - x55)^2 + (
    x184 - x195)^2 + (x324 - x335)^2) + 1 / sqrt((x44 - x56)^2 + (x184 - x196)^
    2 + (x324 - x336)^2) + 1 / sqrt((x44 - x57)^2 + (x184 - x197)^2 + (x324 -
    x337)^2) + 1 / sqrt((x44 - x58)^2 + (x184 - x198)^2 + (x324 - x338)^2) + 1
    / sqrt((x44 - x59)^2 + (x184 - x199)^2 + (x324 - x339)^2) + 1 / sqrt((x44
    - x60)^2 + (x184 - x200)^2 + (x324 - x340)^2) + 1 / sqrt((x44 - x61)^2 + (
    x184 - x201)^2 + (x324 - x341)^2) + 1 / sqrt((x44 - x62)^2 + (x184 - x202)^
    2 + (x324 - x342)^2) + 1 / sqrt((x44 - x63)^2 + (x184 - x203)^2 + (x324 -
    x343)^2) + 1 / sqrt((x44 - x64)^2 + (x184 - x204)^2 + (x324 - x344)^2) + 1
    / sqrt((x44 - x65)^2 + (x184 - x205)^2 + (x324 - x345)^2) + 1 / sqrt((x44
    - x66)^2 + (x184 - x206)^2 + (x324 - x346)^2) + 1 / sqrt((x44 - x67)^2 + (
    x184 - x207)^2 + (x324 - x347)^2) + 1 / sqrt((x44 - x68)^2 + (x184 - x208)^
    2 + (x324 - x348)^2) + 1 / sqrt((x44 - x69)^2 + (x184 - x209)^2 + (x324 -
    x349)^2) + 1 / sqrt((x44 - x70)^2 + (x184 - x210)^2 + (x324 - x350)^2) + 1
    / sqrt((x44 - x71)^2 + (x184 - x211)^2 + (x324 - x351)^2) + 1 / sqrt((x44
    - x72)^2 + (x184 - x212)^2 + (x324 - x352)^2) + 1 / sqrt((x44 - x73)^2 + (
    x184 - x213)^2 + (x324 - x353)^2) + 1 / sqrt((x44 - x74)^2 + (x184 - x214)^
    2 + (x324 - x354)^2) + 1 / sqrt((x44 - x75)^2 + (x184 - x215)^2 + (x324 -
    x355)^2) + 1 / sqrt((x44 - x76)^2 + (x184 - x216)^2 + (x324 - x356)^2) + 1
    / sqrt((x44 - x77)^2 + (x184 - x217)^2 + (x324 - x357)^2) + 1 / sqrt((x44
    - x78)^2 + (x184 - x218)^2 + (x324 - x358)^2) + 1 / sqrt((x44 - x79)^2 + (
    x184 - x219)^2 + (x324 - x359)^2) + 1 / sqrt((x44 - x80)^2 + (x184 - x220)^
    2 + (x324 - x360)^2) + 1 / sqrt((x44 - x81)^2 + (x184 - x221)^2 + (x324 -
    x361)^2) + 1 / sqrt((x44 - x82)^2 + (x184 - x222)^2 + (x324 - x362)^2) + 1
    / sqrt((x44 - x83)^2 + (x184 - x223)^2 + (x324 - x363)^2) + 1 / sqrt((x44
    - x84)^2 + (x184 - x224)^2 + (x324 - x364)^2) + 1 / sqrt((x44 - x85)^2 + (
    x184 - x225)^2 + (x324 - x365)^2) + 1 / sqrt((x44 - x86)^2 + (x184 - x226)^
    2 + (x324 - x366)^2) + 1 / sqrt((x44 - x87)^2 + (x184 - x227)^2 + (x324 -
    x367)^2) + 1 / sqrt((x44 - x88)^2 + (x184 - x228)^2 + (x324 - x368)^2) + 1
    / sqrt((x44 - x89)^2 + (x184 - x229)^2 + (x324 - x369)^2) + 1 / sqrt((x44
    - x90)^2 + (x184 - x230)^2 + (x324 - x370)^2) + 1 / sqrt((x44 - x91)^2 + (
    x184 - x231)^2 + (x324 - x371)^2) + 1 / sqrt((x44 - x92)^2 + (x184 - x232)^
    2 + (x324 - x372)^2) + 1 / sqrt((x44 - x93)^2 + (x184 - x233)^2 + (x324 -
    x373)^2) + 1 / sqrt((x44 - x94)^2 + (x184 - x234)^2 + (x324 - x374)^2) + 1
    / sqrt((x44 - x95)^2 + (x184 - x235)^2 + (x324 - x375)^2) + 1 / sqrt((x44
    - x96)^2 + (x184 - x236)^2 + (x324 - x376)^2) + 1 / sqrt((x44 - x97)^2 + (
    x184 - x237)^2 + (x324 - x377)^2) + 1 / sqrt((x44 - x98)^2 + (x184 - x238)^
    2 + (x324 - x378)^2) + 1 / sqrt((x44 - x99)^2 + (x184 - x239)^2 + (x324 -
    x379)^2) + 1 / sqrt((x44 - x100)^2 + (x184 - x240)^2 + (x324 - x380)^2) + 1
    / sqrt((x44 - x101)^2 + (x184 - x241)^2 + (x324 - x381)^2) + 1 / sqrt((x44
    - x102)^2 + (x184 - x242)^2 + (x324 - x382)^2) + 1 / sqrt((x44 - x103)^2
    + (x184 - x243)^2 + (x324 - x383)^2) + 1 / sqrt((x44 - x104)^2 + (x184 -
    x244)^2 + (x324 - x384)^2) + 1 / sqrt((x44 - x105)^2 + (x184 - x245)^2 + (
    x324 - x385)^2) + 1 / sqrt((x44 - x106)^2 + (x184 - x246)^2 + (x324 - x386)
    ^2) + 1 / sqrt((x44 - x107)^2 + (x184 - x247)^2 + (x324 - x387)^2) + 1 /
    sqrt((x44 - x108)^2 + (x184 - x248)^2 + (x324 - x388)^2) + 1 / sqrt((x44 -
    x109)^2 + (x184 - x249)^2 + (x324 - x389)^2) + 1 / sqrt((x44 - x110)^2 + (
    x184 - x250)^2 + (x324 - x390)^2) + 1 / sqrt((x44 - x111)^2 + (x184 - x251)
    ^2 + (x324 - x391)^2) + 1 / sqrt((x44 - x112)^2 + (x184 - x252)^2 + (x324
    - x392)^2) + 1 / sqrt((x44 - x113)^2 + (x184 - x253)^2 + (x324 - x393)^2)
    + 1 / sqrt((x44 - x114)^2 + (x184 - x254)^2 + (x324 - x394)^2) + 1 / sqrt(
    (x44 - x115)^2 + (x184 - x255)^2 + (x324 - x395)^2) + 1 / sqrt((x44 - x116)
    ^2 + (x184 - x256)^2 + (x324 - x396)^2) + 1 / sqrt((x44 - x117)^2 + (x184
    - x257)^2 + (x324 - x397)^2) + 1 / sqrt((x44 - x118)^2 + (x184 - x258)^2
    + (x324 - x398)^2) + 1 / sqrt((x44 - x119)^2 + (x184 - x259)^2 + (x324 -
    x399)^2) + 1 / sqrt((x44 - x120)^2 + (x184 - x260)^2 + (x324 - x400)^2) + 1
    / sqrt((x44 - x121)^2 + (x184 - x261)^2 + (x324 - x401)^2) + 1 / sqrt((x44
    - x122)^2 + (x184 - x262)^2 + (x324 - x402)^2) + 1 / sqrt((x44 - x123)^2
    + (x184 - x263)^2 + (x324 - x403)^2) + 1 / sqrt((x44 - x124)^2 + (x184 -
    x264)^2 + (x324 - x404)^2) + 1 / sqrt((x44 - x125)^2 + (x184 - x265)^2 + (
    x324 - x405)^2) + 1 / sqrt((x44 - x126)^2 + (x184 - x266)^2 + (x324 - x406)
    ^2) + 1 / sqrt((x44 - x127)^2 + (x184 - x267)^2 + (x324 - x407)^2) + 1 /
    sqrt((x44 - x128)^2 + (x184 - x268)^2 + (x324 - x408)^2) + 1 / sqrt((x44 -
    x129)^2 + (x184 - x269)^2 + (x324 - x409)^2) + 1 / sqrt((x44 - x130)^2 + (
    x184 - x270)^2 + (x324 - x410)^2) + 1 / sqrt((x44 - x131)^2 + (x184 - x271)
    ^2 + (x324 - x411)^2) + 1 / sqrt((x44 - x132)^2 + (x184 - x272)^2 + (x324
    - x412)^2) + 1 / sqrt((x44 - x133)^2 + (x184 - x273)^2 + (x324 - x413)^2)
    + 1 / sqrt((x44 - x134)^2 + (x184 - x274)^2 + (x324 - x414)^2) + 1 / sqrt(
    (x44 - x135)^2 + (x184 - x275)^2 + (x324 - x415)^2) + 1 / sqrt((x44 - x136)
    ^2 + (x184 - x276)^2 + (x324 - x416)^2) + 1 / sqrt((x44 - x137)^2 + (x184
    - x277)^2 + (x324 - x417)^2) + 1 / sqrt((x44 - x138)^2 + (x184 - x278)^2
    + (x324 - x418)^2) + 1 / sqrt((x44 - x139)^2 + (x184 - x279)^2 + (x324 -
    x419)^2) + 1 / sqrt((x44 - x140)^2 + (x184 - x280)^2 + (x324 - x420)^2) + 1
    / sqrt((x45 - x46)^2 + (x185 - x186)^2 + (x325 - x326)^2) + 1 / sqrt((x45
    - x47)^2 + (x185 - x187)^2 + (x325 - x327)^2) + 1 / sqrt((x45 - x48)^2 + (
    x185 - x188)^2 + (x325 - x328)^2) + 1 / sqrt((x45 - x49)^2 + (x185 - x189)^
    2 + (x325 - x329)^2) + 1 / sqrt((x45 - x50)^2 + (x185 - x190)^2 + (x325 -
    x330)^2) + 1 / sqrt((x45 - x51)^2 + (x185 - x191)^2 + (x325 - x331)^2) + 1
    / sqrt((x45 - x52)^2 + (x185 - x192)^2 + (x325 - x332)^2) + 1 / sqrt((x45
    - x53)^2 + (x185 - x193)^2 + (x325 - x333)^2) + 1 / sqrt((x45 - x54)^2 + (
    x185 - x194)^2 + (x325 - x334)^2) + 1 / sqrt((x45 - x55)^2 + (x185 - x195)^
    2 + (x325 - x335)^2) + 1 / sqrt((x45 - x56)^2 + (x185 - x196)^2 + (x325 -
    x336)^2) + 1 / sqrt((x45 - x57)^2 + (x185 - x197)^2 + (x325 - x337)^2) + 1
    / sqrt((x45 - x58)^2 + (x185 - x198)^2 + (x325 - x338)^2) + 1 / sqrt((x45
    - x59)^2 + (x185 - x199)^2 + (x325 - x339)^2) + 1 / sqrt((x45 - x60)^2 + (
    x185 - x200)^2 + (x325 - x340)^2) + 1 / sqrt((x45 - x61)^2 + (x185 - x201)^
    2 + (x325 - x341)^2) + 1 / sqrt((x45 - x62)^2 + (x185 - x202)^2 + (x325 -
    x342)^2) + 1 / sqrt((x45 - x63)^2 + (x185 - x203)^2 + (x325 - x343)^2) + 1
    / sqrt((x45 - x64)^2 + (x185 - x204)^2 + (x325 - x344)^2) + 1 / sqrt((x45
    - x65)^2 + (x185 - x205)^2 + (x325 - x345)^2) + 1 / sqrt((x45 - x66)^2 + (
    x185 - x206)^2 + (x325 - x346)^2) + 1 / sqrt((x45 - x67)^2 + (x185 - x207)^
    2 + (x325 - x347)^2) + 1 / sqrt((x45 - x68)^2 + (x185 - x208)^2 + (x325 -
    x348)^2) + 1 / sqrt((x45 - x69)^2 + (x185 - x209)^2 + (x325 - x349)^2) + 1
    / sqrt((x45 - x70)^2 + (x185 - x210)^2 + (x325 - x350)^2) + 1 / sqrt((x45
    - x71)^2 + (x185 - x211)^2 + (x325 - x351)^2) + 1 / sqrt((x45 - x72)^2 + (
    x185 - x212)^2 + (x325 - x352)^2) + 1 / sqrt((x45 - x73)^2 + (x185 - x213)^
    2 + (x325 - x353)^2) + 1 / sqrt((x45 - x74)^2 + (x185 - x214)^2 + (x325 -
    x354)^2) + 1 / sqrt((x45 - x75)^2 + (x185 - x215)^2 + (x325 - x355)^2) + 1
    / sqrt((x45 - x76)^2 + (x185 - x216)^2 + (x325 - x356)^2) + 1 / sqrt((x45
    - x77)^2 + (x185 - x217)^2 + (x325 - x357)^2) + 1 / sqrt((x45 - x78)^2 + (
    x185 - x218)^2 + (x325 - x358)^2) + 1 / sqrt((x45 - x79)^2 + (x185 - x219)^
    2 + (x325 - x359)^2) + 1 / sqrt((x45 - x80)^2 + (x185 - x220)^2 + (x325 -
    x360)^2) + 1 / sqrt((x45 - x81)^2 + (x185 - x221)^2 + (x325 - x361)^2) + 1
    / sqrt((x45 - x82)^2 + (x185 - x222)^2 + (x325 - x362)^2) + 1 / sqrt((x45
    - x83)^2 + (x185 - x223)^2 + (x325 - x363)^2) + 1 / sqrt((x45 - x84)^2 + (
    x185 - x224)^2 + (x325 - x364)^2) + 1 / sqrt((x45 - x85)^2 + (x185 - x225)^
    2 + (x325 - x365)^2) + 1 / sqrt((x45 - x86)^2 + (x185 - x226)^2 + (x325 -
    x366)^2) + 1 / sqrt((x45 - x87)^2 + (x185 - x227)^2 + (x325 - x367)^2) + 1
    / sqrt((x45 - x88)^2 + (x185 - x228)^2 + (x325 - x368)^2) + 1 / sqrt((x45
    - x89)^2 + (x185 - x229)^2 + (x325 - x369)^2) + 1 / sqrt((x45 - x90)^2 + (
    x185 - x230)^2 + (x325 - x370)^2) + 1 / sqrt((x45 - x91)^2 + (x185 - x231)^
    2 + (x325 - x371)^2) + 1 / sqrt((x45 - x92)^2 + (x185 - x232)^2 + (x325 -
    x372)^2) + 1 / sqrt((x45 - x93)^2 + (x185 - x233)^2 + (x325 - x373)^2) + 1
    / sqrt((x45 - x94)^2 + (x185 - x234)^2 + (x325 - x374)^2) + 1 / sqrt((x45
    - x95)^2 + (x185 - x235)^2 + (x325 - x375)^2) + 1 / sqrt((x45 - x96)^2 + (
    x185 - x236)^2 + (x325 - x376)^2) + 1 / sqrt((x45 - x97)^2 + (x185 - x237)^
    2 + (x325 - x377)^2) + 1 / sqrt((x45 - x98)^2 + (x185 - x238)^2 + (x325 -
    x378)^2) + 1 / sqrt((x45 - x99)^2 + (x185 - x239)^2 + (x325 - x379)^2) + 1
    / sqrt((x45 - x100)^2 + (x185 - x240)^2 + (x325 - x380)^2) + 1 / sqrt((x45
    - x101)^2 + (x185 - x241)^2 + (x325 - x381)^2) + 1 / sqrt((x45 - x102)^2
    + (x185 - x242)^2 + (x325 - x382)^2) + 1 / sqrt((x45 - x103)^2 + (x185 -
    x243)^2 + (x325 - x383)^2) + 1 / sqrt((x45 - x104)^2 + (x185 - x244)^2 + (
    x325 - x384)^2) + 1 / sqrt((x45 - x105)^2 + (x185 - x245)^2 + (x325 - x385)
    ^2) + 1 / sqrt((x45 - x106)^2 + (x185 - x246)^2 + (x325 - x386)^2) + 1 /
    sqrt((x45 - x107)^2 + (x185 - x247)^2 + (x325 - x387)^2) + 1 / sqrt((x45 -
    x108)^2 + (x185 - x248)^2 + (x325 - x388)^2) + 1 / sqrt((x45 - x109)^2 + (
    x185 - x249)^2 + (x325 - x389)^2) + 1 / sqrt((x45 - x110)^2 + (x185 - x250)
    ^2 + (x325 - x390)^2) + 1 / sqrt((x45 - x111)^2 + (x185 - x251)^2 + (x325
    - x391)^2) + 1 / sqrt((x45 - x112)^2 + (x185 - x252)^2 + (x325 - x392)^2)
    + 1 / sqrt((x45 - x113)^2 + (x185 - x253)^2 + (x325 - x393)^2) + 1 / sqrt(
    (x45 - x114)^2 + (x185 - x254)^2 + (x325 - x394)^2) + 1 / sqrt((x45 - x115)
    ^2 + (x185 - x255)^2 + (x325 - x395)^2) + 1 / sqrt((x45 - x116)^2 + (x185
    - x256)^2 + (x325 - x396)^2) + 1 / sqrt((x45 - x117)^2 + (x185 - x257)^2
    + (x325 - x397)^2) + 1 / sqrt((x45 - x118)^2 + (x185 - x258)^2 + (x325 -
    x398)^2) + 1 / sqrt((x45 - x119)^2 + (x185 - x259)^2 + (x325 - x399)^2) + 1
    / sqrt((x45 - x120)^2 + (x185 - x260)^2 + (x325 - x400)^2) + 1 / sqrt((x45
    - x121)^2 + (x185 - x261)^2 + (x325 - x401)^2) + 1 / sqrt((x45 - x122)^2
    + (x185 - x262)^2 + (x325 - x402)^2) + 1 / sqrt((x45 - x123)^2 + (x185 -
    x263)^2 + (x325 - x403)^2) + 1 / sqrt((x45 - x124)^2 + (x185 - x264)^2 + (
    x325 - x404)^2) + 1 / sqrt((x45 - x125)^2 + (x185 - x265)^2 + (x325 - x405)
    ^2) + 1 / sqrt((x45 - x126)^2 + (x185 - x266)^2 + (x325 - x406)^2) + 1 /
    sqrt((x45 - x127)^2 + (x185 - x267)^2 + (x325 - x407)^2) + 1 / sqrt((x45 -
    x128)^2 + (x185 - x268)^2 + (x325 - x408)^2) + 1 / sqrt((x45 - x129)^2 + (
    x185 - x269)^2 + (x325 - x409)^2) + 1 / sqrt((x45 - x130)^2 + (x185 - x270)
    ^2 + (x325 - x410)^2) + 1 / sqrt((x45 - x131)^2 + (x185 - x271)^2 + (x325
    - x411)^2) + 1 / sqrt((x45 - x132)^2 + (x185 - x272)^2 + (x325 - x412)^2)
    + 1 / sqrt((x45 - x133)^2 + (x185 - x273)^2 + (x325 - x413)^2) + 1 / sqrt(
    (x45 - x134)^2 + (x185 - x274)^2 + (x325 - x414)^2) + 1 / sqrt((x45 - x135)
    ^2 + (x185 - x275)^2 + (x325 - x415)^2) + 1 / sqrt((x45 - x136)^2 + (x185
    - x276)^2 + (x325 - x416)^2) + 1 / sqrt((x45 - x137)^2 + (x185 - x277)^2
    + (x325 - x417)^2) + 1 / sqrt((x45 - x138)^2 + (x185 - x278)^2 + (x325 -
    x418)^2) + 1 / sqrt((x45 - x139)^2 + (x185 - x279)^2 + (x325 - x419)^2) + 1
    / sqrt((x45 - x140)^2 + (x185 - x280)^2 + (x325 - x420)^2) + 1 / sqrt((x46
    - x47)^2 + (x186 - x187)^2 + (x326 - x327)^2) + 1 / sqrt((x46 - x48)^2 + (
    x186 - x188)^2 + (x326 - x328)^2) + 1 / sqrt((x46 - x49)^2 + (x186 - x189)^
    2 + (x326 - x329)^2) + 1 / sqrt((x46 - x50)^2 + (x186 - x190)^2 + (x326 -
    x330)^2) + 1 / sqrt((x46 - x51)^2 + (x186 - x191)^2 + (x326 - x331)^2) + 1
    / sqrt((x46 - x52)^2 + (x186 - x192)^2 + (x326 - x332)^2) + 1 / sqrt((x46
    - x53)^2 + (x186 - x193)^2 + (x326 - x333)^2) + 1 / sqrt((x46 - x54)^2 + (
    x186 - x194)^2 + (x326 - x334)^2) + 1 / sqrt((x46 - x55)^2 + (x186 - x195)^
    2 + (x326 - x335)^2) + 1 / sqrt((x46 - x56)^2 + (x186 - x196)^2 + (x326 -
    x336)^2) + 1 / sqrt((x46 - x57)^2 + (x186 - x197)^2 + (x326 - x337)^2) + 1
    / sqrt((x46 - x58)^2 + (x186 - x198)^2 + (x326 - x338)^2) + 1 / sqrt((x46
    - x59)^2 + (x186 - x199)^2 + (x326 - x339)^2) + 1 / sqrt((x46 - x60)^2 + (
    x186 - x200)^2 + (x326 - x340)^2) + 1 / sqrt((x46 - x61)^2 + (x186 - x201)^
    2 + (x326 - x341)^2) + 1 / sqrt((x46 - x62)^2 + (x186 - x202)^2 + (x326 -
    x342)^2) + 1 / sqrt((x46 - x63)^2 + (x186 - x203)^2 + (x326 - x343)^2) + 1
    / sqrt((x46 - x64)^2 + (x186 - x204)^2 + (x326 - x344)^2) + 1 / sqrt((x46
    - x65)^2 + (x186 - x205)^2 + (x326 - x345)^2) + 1 / sqrt((x46 - x66)^2 + (
    x186 - x206)^2 + (x326 - x346)^2) + 1 / sqrt((x46 - x67)^2 + (x186 - x207)^
    2 + (x326 - x347)^2) + 1 / sqrt((x46 - x68)^2 + (x186 - x208)^2 + (x326 -
    x348)^2) + 1 / sqrt((x46 - x69)^2 + (x186 - x209)^2 + (x326 - x349)^2) + 1
    / sqrt((x46 - x70)^2 + (x186 - x210)^2 + (x326 - x350)^2) + 1 / sqrt((x46
    - x71)^2 + (x186 - x211)^2 + (x326 - x351)^2) + 1 / sqrt((x46 - x72)^2 + (
    x186 - x212)^2 + (x326 - x352)^2) + 1 / sqrt((x46 - x73)^2 + (x186 - x213)^
    2 + (x326 - x353)^2) + 1 / sqrt((x46 - x74)^2 + (x186 - x214)^2 + (x326 -
    x354)^2) + 1 / sqrt((x46 - x75)^2 + (x186 - x215)^2 + (x326 - x355)^2) + 1
    / sqrt((x46 - x76)^2 + (x186 - x216)^2 + (x326 - x356)^2) + 1 / sqrt((x46
    - x77)^2 + (x186 - x217)^2 + (x326 - x357)^2) + 1 / sqrt((x46 - x78)^2 + (
    x186 - x218)^2 + (x326 - x358)^2) + 1 / sqrt((x46 - x79)^2 + (x186 - x219)^
    2 + (x326 - x359)^2) + 1 / sqrt((x46 - x80)^2 + (x186 - x220)^2 + (x326 -
    x360)^2) + 1 / sqrt((x46 - x81)^2 + (x186 - x221)^2 + (x326 - x361)^2) + 1
    / sqrt((x46 - x82)^2 + (x186 - x222)^2 + (x326 - x362)^2) + 1 / sqrt((x46
    - x83)^2 + (x186 - x223)^2 + (x326 - x363)^2) + 1 / sqrt((x46 - x84)^2 + (
    x186 - x224)^2 + (x326 - x364)^2) + 1 / sqrt((x46 - x85)^2 + (x186 - x225)^
    2 + (x326 - x365)^2) + 1 / sqrt((x46 - x86)^2 + (x186 - x226)^2 + (x326 -
    x366)^2) + 1 / sqrt((x46 - x87)^2 + (x186 - x227)^2 + (x326 - x367)^2) + 1
    / sqrt((x46 - x88)^2 + (x186 - x228)^2 + (x326 - x368)^2) + 1 / sqrt((x46
    - x89)^2 + (x186 - x229)^2 + (x326 - x369)^2) + 1 / sqrt((x46 - x90)^2 + (
    x186 - x230)^2 + (x326 - x370)^2) + 1 / sqrt((x46 - x91)^2 + (x186 - x231)^
    2 + (x326 - x371)^2) + 1 / sqrt((x46 - x92)^2 + (x186 - x232)^2 + (x326 -
    x372)^2) + 1 / sqrt((x46 - x93)^2 + (x186 - x233)^2 + (x326 - x373)^2) + 1
    / sqrt((x46 - x94)^2 + (x186 - x234)^2 + (x326 - x374)^2) + 1 / sqrt((x46
    - x95)^2 + (x186 - x235)^2 + (x326 - x375)^2) + 1 / sqrt((x46 - x96)^2 + (
    x186 - x236)^2 + (x326 - x376)^2) + 1 / sqrt((x46 - x97)^2 + (x186 - x237)^
    2 + (x326 - x377)^2) + 1 / sqrt((x46 - x98)^2 + (x186 - x238)^2 + (x326 -
    x378)^2) + 1 / sqrt((x46 - x99)^2 + (x186 - x239)^2 + (x326 - x379)^2) + 1
    / sqrt((x46 - x100)^2 + (x186 - x240)^2 + (x326 - x380)^2) + 1 / sqrt((x46
    - x101)^2 + (x186 - x241)^2 + (x326 - x381)^2) + 1 / sqrt((x46 - x102)^2
    + (x186 - x242)^2 + (x326 - x382)^2) + 1 / sqrt((x46 - x103)^2 + (x186 -
    x243)^2 + (x326 - x383)^2) + 1 / sqrt((x46 - x104)^2 + (x186 - x244)^2 + (
    x326 - x384)^2) + 1 / sqrt((x46 - x105)^2 + (x186 - x245)^2 + (x326 - x385)
    ^2) + 1 / sqrt((x46 - x106)^2 + (x186 - x246)^2 + (x326 - x386)^2) + 1 /
    sqrt((x46 - x107)^2 + (x186 - x247)^2 + (x326 - x387)^2) + 1 / sqrt((x46 -
    x108)^2 + (x186 - x248)^2 + (x326 - x388)^2) + 1 / sqrt((x46 - x109)^2 + (
    x186 - x249)^2 + (x326 - x389)^2) + 1 / sqrt((x46 - x110)^2 + (x186 - x250)
    ^2 + (x326 - x390)^2) + 1 / sqrt((x46 - x111)^2 + (x186 - x251)^2 + (x326
    - x391)^2) + 1 / sqrt((x46 - x112)^2 + (x186 - x252)^2 + (x326 - x392)^2)
    + 1 / sqrt((x46 - x113)^2 + (x186 - x253)^2 + (x326 - x393)^2) + 1 / sqrt(
    (x46 - x114)^2 + (x186 - x254)^2 + (x326 - x394)^2) + 1 / sqrt((x46 - x115)
    ^2 + (x186 - x255)^2 + (x326 - x395)^2) + 1 / sqrt((x46 - x116)^2 + (x186
    - x256)^2 + (x326 - x396)^2) + 1 / sqrt((x46 - x117)^2 + (x186 - x257)^2
    + (x326 - x397)^2) + 1 / sqrt((x46 - x118)^2 + (x186 - x258)^2 + (x326 -
    x398)^2) + 1 / sqrt((x46 - x119)^2 + (x186 - x259)^2 + (x326 - x399)^2) + 1
    / sqrt((x46 - x120)^2 + (x186 - x260)^2 + (x326 - x400)^2) + 1 / sqrt((x46
    - x121)^2 + (x186 - x261)^2 + (x326 - x401)^2) + 1 / sqrt((x46 - x122)^2
    + (x186 - x262)^2 + (x326 - x402)^2) + 1 / sqrt((x46 - x123)^2 + (x186 -
    x263)^2 + (x326 - x403)^2) + 1 / sqrt((x46 - x124)^2 + (x186 - x264)^2 + (
    x326 - x404)^2) + 1 / sqrt((x46 - x125)^2 + (x186 - x265)^2 + (x326 - x405)
    ^2) + 1 / sqrt((x46 - x126)^2 + (x186 - x266)^2 + (x326 - x406)^2) + 1 /
    sqrt((x46 - x127)^2 + (x186 - x267)^2 + (x326 - x407)^2) + 1 / sqrt((x46 -
    x128)^2 + (x186 - x268)^2 + (x326 - x408)^2) + 1 / sqrt((x46 - x129)^2 + (
    x186 - x269)^2 + (x326 - x409)^2) + 1 / sqrt((x46 - x130)^2 + (x186 - x270)
    ^2 + (x326 - x410)^2) + 1 / sqrt((x46 - x131)^2 + (x186 - x271)^2 + (x326
    - x411)^2) + 1 / sqrt((x46 - x132)^2 + (x186 - x272)^2 + (x326 - x412)^2)
    + 1 / sqrt((x46 - x133)^2 + (x186 - x273)^2 + (x326 - x413)^2) + 1 / sqrt(
    (x46 - x134)^2 + (x186 - x274)^2 + (x326 - x414)^2) + 1 / sqrt((x46 - x135)
    ^2 + (x186 - x275)^2 + (x326 - x415)^2) + 1 / sqrt((x46 - x136)^2 + (x186
    - x276)^2 + (x326 - x416)^2) + 1 / sqrt((x46 - x137)^2 + (x186 - x277)^2
    + (x326 - x417)^2) + 1 / sqrt((x46 - x138)^2 + (x186 - x278)^2 + (x326 -
    x418)^2) + 1 / sqrt((x46 - x139)^2 + (x186 - x279)^2 + (x326 - x419)^2) + 1
    / sqrt((x46 - x140)^2 + (x186 - x280)^2 + (x326 - x420)^2) + 1 / sqrt((x47
    - x48)^2 + (x187 - x188)^2 + (x327 - x328)^2) + 1 / sqrt((x47 - x49)^2 + (
    x187 - x189)^2 + (x327 - x329)^2) + 1 / sqrt((x47 - x50)^2 + (x187 - x190)^
    2 + (x327 - x330)^2) + 1 / sqrt((x47 - x51)^2 + (x187 - x191)^2 + (x327 -
    x331)^2) + 1 / sqrt((x47 - x52)^2 + (x187 - x192)^2 + (x327 - x332)^2) + 1
    / sqrt((x47 - x53)^2 + (x187 - x193)^2 + (x327 - x333)^2) + 1 / sqrt((x47
    - x54)^2 + (x187 - x194)^2 + (x327 - x334)^2) + 1 / sqrt((x47 - x55)^2 + (
    x187 - x195)^2 + (x327 - x335)^2) + 1 / sqrt((x47 - x56)^2 + (x187 - x196)^
    2 + (x327 - x336)^2) + 1 / sqrt((x47 - x57)^2 + (x187 - x197)^2 + (x327 -
    x337)^2) + 1 / sqrt((x47 - x58)^2 + (x187 - x198)^2 + (x327 - x338)^2) + 1
    / sqrt((x47 - x59)^2 + (x187 - x199)^2 + (x327 - x339)^2) + 1 / sqrt((x47
    - x60)^2 + (x187 - x200)^2 + (x327 - x340)^2) + 1 / sqrt((x47 - x61)^2 + (
    x187 - x201)^2 + (x327 - x341)^2) + 1 / sqrt((x47 - x62)^2 + (x187 - x202)^
    2 + (x327 - x342)^2) + 1 / sqrt((x47 - x63)^2 + (x187 - x203)^2 + (x327 -
    x343)^2) + 1 / sqrt((x47 - x64)^2 + (x187 - x204)^2 + (x327 - x344)^2) + 1
    / sqrt((x47 - x65)^2 + (x187 - x205)^2 + (x327 - x345)^2) + 1 / sqrt((x47
    - x66)^2 + (x187 - x206)^2 + (x327 - x346)^2) + 1 / sqrt((x47 - x67)^2 + (
    x187 - x207)^2 + (x327 - x347)^2) + 1 / sqrt((x47 - x68)^2 + (x187 - x208)^
    2 + (x327 - x348)^2) + 1 / sqrt((x47 - x69)^2 + (x187 - x209)^2 + (x327 -
    x349)^2) + 1 / sqrt((x47 - x70)^2 + (x187 - x210)^2 + (x327 - x350)^2) + 1
    / sqrt((x47 - x71)^2 + (x187 - x211)^2 + (x327 - x351)^2) + 1 / sqrt((x47
    - x72)^2 + (x187 - x212)^2 + (x327 - x352)^2) + 1 / sqrt((x47 - x73)^2 + (
    x187 - x213)^2 + (x327 - x353)^2) + 1 / sqrt((x47 - x74)^2 + (x187 - x214)^
    2 + (x327 - x354)^2) + 1 / sqrt((x47 - x75)^2 + (x187 - x215)^2 + (x327 -
    x355)^2) + 1 / sqrt((x47 - x76)^2 + (x187 - x216)^2 + (x327 - x356)^2) + 1
    / sqrt((x47 - x77)^2 + (x187 - x217)^2 + (x327 - x357)^2) + 1 / sqrt((x47
    - x78)^2 + (x187 - x218)^2 + (x327 - x358)^2) + 1 / sqrt((x47 - x79)^2 + (
    x187 - x219)^2 + (x327 - x359)^2) + 1 / sqrt((x47 - x80)^2 + (x187 - x220)^
    2 + (x327 - x360)^2) + 1 / sqrt((x47 - x81)^2 + (x187 - x221)^2 + (x327 -
    x361)^2) + 1 / sqrt((x47 - x82)^2 + (x187 - x222)^2 + (x327 - x362)^2) + 1
    / sqrt((x47 - x83)^2 + (x187 - x223)^2 + (x327 - x363)^2) + 1 / sqrt((x47
    - x84)^2 + (x187 - x224)^2 + (x327 - x364)^2) + 1 / sqrt((x47 - x85)^2 + (
    x187 - x225)^2 + (x327 - x365)^2) + 1 / sqrt((x47 - x86)^2 + (x187 - x226)^
    2 + (x327 - x366)^2) + 1 / sqrt((x47 - x87)^2 + (x187 - x227)^2 + (x327 -
    x367)^2) + 1 / sqrt((x47 - x88)^2 + (x187 - x228)^2 + (x327 - x368)^2) + 1
    / sqrt((x47 - x89)^2 + (x187 - x229)^2 + (x327 - x369)^2) + 1 / sqrt((x47
    - x90)^2 + (x187 - x230)^2 + (x327 - x370)^2) + 1 / sqrt((x47 - x91)^2 + (
    x187 - x231)^2 + (x327 - x371)^2) + 1 / sqrt((x47 - x92)^2 + (x187 - x232)^
    2 + (x327 - x372)^2) + 1 / sqrt((x47 - x93)^2 + (x187 - x233)^2 + (x327 -
    x373)^2) + 1 / sqrt((x47 - x94)^2 + (x187 - x234)^2 + (x327 - x374)^2) + 1
    / sqrt((x47 - x95)^2 + (x187 - x235)^2 + (x327 - x375)^2) + 1 / sqrt((x47
    - x96)^2 + (x187 - x236)^2 + (x327 - x376)^2) + 1 / sqrt((x47 - x97)^2 + (
    x187 - x237)^2 + (x327 - x377)^2) + 1 / sqrt((x47 - x98)^2 + (x187 - x238)^
    2 + (x327 - x378)^2) + 1 / sqrt((x47 - x99)^2 + (x187 - x239)^2 + (x327 -
    x379)^2) + 1 / sqrt((x47 - x100)^2 + (x187 - x240)^2 + (x327 - x380)^2) + 1
    / sqrt((x47 - x101)^2 + (x187 - x241)^2 + (x327 - x381)^2) + 1 / sqrt((x47
    - x102)^2 + (x187 - x242)^2 + (x327 - x382)^2) + 1 / sqrt((x47 - x103)^2
    + (x187 - x243)^2 + (x327 - x383)^2) + 1 / sqrt((x47 - x104)^2 + (x187 -
    x244)^2 + (x327 - x384)^2) + 1 / sqrt((x47 - x105)^2 + (x187 - x245)^2 + (
    x327 - x385)^2) + 1 / sqrt((x47 - x106)^2 + (x187 - x246)^2 + (x327 - x386)
    ^2) + 1 / sqrt((x47 - x107)^2 + (x187 - x247)^2 + (x327 - x387)^2) + 1 /
    sqrt((x47 - x108)^2 + (x187 - x248)^2 + (x327 - x388)^2) + 1 / sqrt((x47 -
    x109)^2 + (x187 - x249)^2 + (x327 - x389)^2) + 1 / sqrt((x47 - x110)^2 + (
    x187 - x250)^2 + (x327 - x390)^2) + 1 / sqrt((x47 - x111)^2 + (x187 - x251)
    ^2 + (x327 - x391)^2) + 1 / sqrt((x47 - x112)^2 + (x187 - x252)^2 + (x327
    - x392)^2) + 1 / sqrt((x47 - x113)^2 + (x187 - x253)^2 + (x327 - x393)^2)
    + 1 / sqrt((x47 - x114)^2 + (x187 - x254)^2 + (x327 - x394)^2) + 1 / sqrt(
    (x47 - x115)^2 + (x187 - x255)^2 + (x327 - x395)^2) + 1 / sqrt((x47 - x116)
    ^2 + (x187 - x256)^2 + (x327 - x396)^2) + 1 / sqrt((x47 - x117)^2 + (x187
    - x257)^2 + (x327 - x397)^2) + 1 / sqrt((x47 - x118)^2 + (x187 - x258)^2
    + (x327 - x398)^2) + 1 / sqrt((x47 - x119)^2 + (x187 - x259)^2 + (x327 -
    x399)^2) + 1 / sqrt((x47 - x120)^2 + (x187 - x260)^2 + (x327 - x400)^2) + 1
    / sqrt((x47 - x121)^2 + (x187 - x261)^2 + (x327 - x401)^2) + 1 / sqrt((x47
    - x122)^2 + (x187 - x262)^2 + (x327 - x402)^2) + 1 / sqrt((x47 - x123)^2
    + (x187 - x263)^2 + (x327 - x403)^2) + 1 / sqrt((x47 - x124)^2 + (x187 -
    x264)^2 + (x327 - x404)^2) + 1 / sqrt((x47 - x125)^2 + (x187 - x265)^2 + (
    x327 - x405)^2) + 1 / sqrt((x47 - x126)^2 + (x187 - x266)^2 + (x327 - x406)
    ^2) + 1 / sqrt((x47 - x127)^2 + (x187 - x267)^2 + (x327 - x407)^2) + 1 /
    sqrt((x47 - x128)^2 + (x187 - x268)^2 + (x327 - x408)^2) + 1 / sqrt((x47 -
    x129)^2 + (x187 - x269)^2 + (x327 - x409)^2) + 1 / sqrt((x47 - x130)^2 + (
    x187 - x270)^2 + (x327 - x410)^2) + 1 / sqrt((x47 - x131)^2 + (x187 - x271)
    ^2 + (x327 - x411)^2) + 1 / sqrt((x47 - x132)^2 + (x187 - x272)^2 + (x327
    - x412)^2) + 1 / sqrt((x47 - x133)^2 + (x187 - x273)^2 + (x327 - x413)^2)
    + 1 / sqrt((x47 - x134)^2 + (x187 - x274)^2 + (x327 - x414)^2) + 1 / sqrt(
    (x47 - x135)^2 + (x187 - x275)^2 + (x327 - x415)^2) + 1 / sqrt((x47 - x136)
    ^2 + (x187 - x276)^2 + (x327 - x416)^2) + 1 / sqrt((x47 - x137)^2 + (x187
    - x277)^2 + (x327 - x417)^2) + 1 / sqrt((x47 - x138)^2 + (x187 - x278)^2
    + (x327 - x418)^2) + 1 / sqrt((x47 - x139)^2 + (x187 - x279)^2 + (x327 -
    x419)^2) + 1 / sqrt((x47 - x140)^2 + (x187 - x280)^2 + (x327 - x420)^2) + 1
    / sqrt((x48 - x49)^2 + (x188 - x189)^2 + (x328 - x329)^2) + 1 / sqrt((x48
    - x50)^2 + (x188 - x190)^2 + (x328 - x330)^2) + 1 / sqrt((x48 - x51)^2 + (
    x188 - x191)^2 + (x328 - x331)^2) + 1 / sqrt((x48 - x52)^2 + (x188 - x192)^
    2 + (x328 - x332)^2) + 1 / sqrt((x48 - x53)^2 + (x188 - x193)^2 + (x328 -
    x333)^2) + 1 / sqrt((x48 - x54)^2 + (x188 - x194)^2 + (x328 - x334)^2) + 1
    / sqrt((x48 - x55)^2 + (x188 - x195)^2 + (x328 - x335)^2) + 1 / sqrt((x48
    - x56)^2 + (x188 - x196)^2 + (x328 - x336)^2) + 1 / sqrt((x48 - x57)^2 + (
    x188 - x197)^2 + (x328 - x337)^2) + 1 / sqrt((x48 - x58)^2 + (x188 - x198)^
    2 + (x328 - x338)^2) + 1 / sqrt((x48 - x59)^2 + (x188 - x199)^2 + (x328 -
    x339)^2) + 1 / sqrt((x48 - x60)^2 + (x188 - x200)^2 + (x328 - x340)^2) + 1
    / sqrt((x48 - x61)^2 + (x188 - x201)^2 + (x328 - x341)^2) + 1 / sqrt((x48
    - x62)^2 + (x188 - x202)^2 + (x328 - x342)^2) + 1 / sqrt((x48 - x63)^2 + (
    x188 - x203)^2 + (x328 - x343)^2) + 1 / sqrt((x48 - x64)^2 + (x188 - x204)^
    2 + (x328 - x344)^2) + 1 / sqrt((x48 - x65)^2 + (x188 - x205)^2 + (x328 -
    x345)^2) + 1 / sqrt((x48 - x66)^2 + (x188 - x206)^2 + (x328 - x346)^2) + 1
    / sqrt((x48 - x67)^2 + (x188 - x207)^2 + (x328 - x347)^2) + 1 / sqrt((x48
    - x68)^2 + (x188 - x208)^2 + (x328 - x348)^2) + 1 / sqrt((x48 - x69)^2 + (
    x188 - x209)^2 + (x328 - x349)^2) + 1 / sqrt((x48 - x70)^2 + (x188 - x210)^
    2 + (x328 - x350)^2) + 1 / sqrt((x48 - x71)^2 + (x188 - x211)^2 + (x328 -
    x351)^2) + 1 / sqrt((x48 - x72)^2 + (x188 - x212)^2 + (x328 - x352)^2) + 1
    / sqrt((x48 - x73)^2 + (x188 - x213)^2 + (x328 - x353)^2) + 1 / sqrt((x48
    - x74)^2 + (x188 - x214)^2 + (x328 - x354)^2) + 1 / sqrt((x48 - x75)^2 + (
    x188 - x215)^2 + (x328 - x355)^2) + 1 / sqrt((x48 - x76)^2 + (x188 - x216)^
    2 + (x328 - x356)^2) + 1 / sqrt((x48 - x77)^2 + (x188 - x217)^2 + (x328 -
    x357)^2) + 1 / sqrt((x48 - x78)^2 + (x188 - x218)^2 + (x328 - x358)^2) + 1
    / sqrt((x48 - x79)^2 + (x188 - x219)^2 + (x328 - x359)^2) + 1 / sqrt((x48
    - x80)^2 + (x188 - x220)^2 + (x328 - x360)^2) + 1 / sqrt((x48 - x81)^2 + (
    x188 - x221)^2 + (x328 - x361)^2) + 1 / sqrt((x48 - x82)^2 + (x188 - x222)^
    2 + (x328 - x362)^2) + 1 / sqrt((x48 - x83)^2 + (x188 - x223)^2 + (x328 -
    x363)^2) + 1 / sqrt((x48 - x84)^2 + (x188 - x224)^2 + (x328 - x364)^2) + 1
    / sqrt((x48 - x85)^2 + (x188 - x225)^2 + (x328 - x365)^2) + 1 / sqrt((x48
    - x86)^2 + (x188 - x226)^2 + (x328 - x366)^2) + 1 / sqrt((x48 - x87)^2 + (
    x188 - x227)^2 + (x328 - x367)^2) + 1 / sqrt((x48 - x88)^2 + (x188 - x228)^
    2 + (x328 - x368)^2) + 1 / sqrt((x48 - x89)^2 + (x188 - x229)^2 + (x328 -
    x369)^2) + 1 / sqrt((x48 - x90)^2 + (x188 - x230)^2 + (x328 - x370)^2) + 1
    / sqrt((x48 - x91)^2 + (x188 - x231)^2 + (x328 - x371)^2) + 1 / sqrt((x48
    - x92)^2 + (x188 - x232)^2 + (x328 - x372)^2) + 1 / sqrt((x48 - x93)^2 + (
    x188 - x233)^2 + (x328 - x373)^2) + 1 / sqrt((x48 - x94)^2 + (x188 - x234)^
    2 + (x328 - x374)^2) + 1 / sqrt((x48 - x95)^2 + (x188 - x235)^2 + (x328 -
    x375)^2) + 1 / sqrt((x48 - x96)^2 + (x188 - x236)^2 + (x328 - x376)^2) + 1
    / sqrt((x48 - x97)^2 + (x188 - x237)^2 + (x328 - x377)^2) + 1 / sqrt((x48
    - x98)^2 + (x188 - x238)^2 + (x328 - x378)^2) + 1 / sqrt((x48 - x99)^2 + (
    x188 - x239)^2 + (x328 - x379)^2) + 1 / sqrt((x48 - x100)^2 + (x188 - x240)
    ^2 + (x328 - x380)^2) + 1 / sqrt((x48 - x101)^2 + (x188 - x241)^2 + (x328
    - x381)^2) + 1 / sqrt((x48 - x102)^2 + (x188 - x242)^2 + (x328 - x382)^2)
    + 1 / sqrt((x48 - x103)^2 + (x188 - x243)^2 + (x328 - x383)^2) + 1 / sqrt(
    (x48 - x104)^2 + (x188 - x244)^2 + (x328 - x384)^2) + 1 / sqrt((x48 - x105)
    ^2 + (x188 - x245)^2 + (x328 - x385)^2) + 1 / sqrt((x48 - x106)^2 + (x188
    - x246)^2 + (x328 - x386)^2) + 1 / sqrt((x48 - x107)^2 + (x188 - x247)^2
    + (x328 - x387)^2) + 1 / sqrt((x48 - x108)^2 + (x188 - x248)^2 + (x328 -
    x388)^2) + 1 / sqrt((x48 - x109)^2 + (x188 - x249)^2 + (x328 - x389)^2) + 1
    / sqrt((x48 - x110)^2 + (x188 - x250)^2 + (x328 - x390)^2) + 1 / sqrt((x48
    - x111)^2 + (x188 - x251)^2 + (x328 - x391)^2) + 1 / sqrt((x48 - x112)^2
    + (x188 - x252)^2 + (x328 - x392)^2) + 1 / sqrt((x48 - x113)^2 + (x188 -
    x253)^2 + (x328 - x393)^2) + 1 / sqrt((x48 - x114)^2 + (x188 - x254)^2 + (
    x328 - x394)^2) + 1 / sqrt((x48 - x115)^2 + (x188 - x255)^2 + (x328 - x395)
    ^2) + 1 / sqrt((x48 - x116)^2 + (x188 - x256)^2 + (x328 - x396)^2) + 1 /
    sqrt((x48 - x117)^2 + (x188 - x257)^2 + (x328 - x397)^2) + 1 / sqrt((x48 -
    x118)^2 + (x188 - x258)^2 + (x328 - x398)^2) + 1 / sqrt((x48 - x119)^2 + (
    x188 - x259)^2 + (x328 - x399)^2) + 1 / sqrt((x48 - x120)^2 + (x188 - x260)
    ^2 + (x328 - x400)^2) + 1 / sqrt((x48 - x121)^2 + (x188 - x261)^2 + (x328
    - x401)^2) + 1 / sqrt((x48 - x122)^2 + (x188 - x262)^2 + (x328 - x402)^2)
    + 1 / sqrt((x48 - x123)^2 + (x188 - x263)^2 + (x328 - x403)^2) + 1 / sqrt(
    (x48 - x124)^2 + (x188 - x264)^2 + (x328 - x404)^2) + 1 / sqrt((x48 - x125)
    ^2 + (x188 - x265)^2 + (x328 - x405)^2) + 1 / sqrt((x48 - x126)^2 + (x188
    - x266)^2 + (x328 - x406)^2) + 1 / sqrt((x48 - x127)^2 + (x188 - x267)^2
    + (x328 - x407)^2) + 1 / sqrt((x48 - x128)^2 + (x188 - x268)^2 + (x328 -
    x408)^2) + 1 / sqrt((x48 - x129)^2 + (x188 - x269)^2 + (x328 - x409)^2) + 1
    / sqrt((x48 - x130)^2 + (x188 - x270)^2 + (x328 - x410)^2) + 1 / sqrt((x48
    - x131)^2 + (x188 - x271)^2 + (x328 - x411)^2) + 1 / sqrt((x48 - x132)^2
    + (x188 - x272)^2 + (x328 - x412)^2) + 1 / sqrt((x48 - x133)^2 + (x188 -
    x273)^2 + (x328 - x413)^2) + 1 / sqrt((x48 - x134)^2 + (x188 - x274)^2 + (
    x328 - x414)^2) + 1 / sqrt((x48 - x135)^2 + (x188 - x275)^2 + (x328 - x415)
    ^2) + 1 / sqrt((x48 - x136)^2 + (x188 - x276)^2 + (x328 - x416)^2) + 1 /
    sqrt((x48 - x137)^2 + (x188 - x277)^2 + (x328 - x417)^2) + 1 / sqrt((x48 -
    x138)^2 + (x188 - x278)^2 + (x328 - x418)^2) + 1 / sqrt((x48 - x139)^2 + (
    x188 - x279)^2 + (x328 - x419)^2) + 1 / sqrt((x48 - x140)^2 + (x188 - x280)
    ^2 + (x328 - x420)^2) + 1 / sqrt((x49 - x50)^2 + (x189 - x190)^2 + (x329 -
    x330)^2) + 1 / sqrt((x49 - x51)^2 + (x189 - x191)^2 + (x329 - x331)^2) + 1
    / sqrt((x49 - x52)^2 + (x189 - x192)^2 + (x329 - x332)^2) + 1 / sqrt((x49
    - x53)^2 + (x189 - x193)^2 + (x329 - x333)^2) + 1 / sqrt((x49 - x54)^2 + (
    x189 - x194)^2 + (x329 - x334)^2) + 1 / sqrt((x49 - x55)^2 + (x189 - x195)^
    2 + (x329 - x335)^2) + 1 / sqrt((x49 - x56)^2 + (x189 - x196)^2 + (x329 -
    x336)^2) + 1 / sqrt((x49 - x57)^2 + (x189 - x197)^2 + (x329 - x337)^2) + 1
    / sqrt((x49 - x58)^2 + (x189 - x198)^2 + (x329 - x338)^2) + 1 / sqrt((x49
    - x59)^2 + (x189 - x199)^2 + (x329 - x339)^2) + 1 / sqrt((x49 - x60)^2 + (
    x189 - x200)^2 + (x329 - x340)^2) + 1 / sqrt((x49 - x61)^2 + (x189 - x201)^
    2 + (x329 - x341)^2) + 1 / sqrt((x49 - x62)^2 + (x189 - x202)^2 + (x329 -
    x342)^2) + 1 / sqrt((x49 - x63)^2 + (x189 - x203)^2 + (x329 - x343)^2) + 1
    / sqrt((x49 - x64)^2 + (x189 - x204)^2 + (x329 - x344)^2) + 1 / sqrt((x49
    - x65)^2 + (x189 - x205)^2 + (x329 - x345)^2) + 1 / sqrt((x49 - x66)^2 + (
    x189 - x206)^2 + (x329 - x346)^2) + 1 / sqrt((x49 - x67)^2 + (x189 - x207)^
    2 + (x329 - x347)^2) + 1 / sqrt((x49 - x68)^2 + (x189 - x208)^2 + (x329 -
    x348)^2) + 1 / sqrt((x49 - x69)^2 + (x189 - x209)^2 + (x329 - x349)^2) + 1
    / sqrt((x49 - x70)^2 + (x189 - x210)^2 + (x329 - x350)^2) + 1 / sqrt((x49
    - x71)^2 + (x189 - x211)^2 + (x329 - x351)^2) + 1 / sqrt((x49 - x72)^2 + (
    x189 - x212)^2 + (x329 - x352)^2) + 1 / sqrt((x49 - x73)^2 + (x189 - x213)^
    2 + (x329 - x353)^2) + 1 / sqrt((x49 - x74)^2 + (x189 - x214)^2 + (x329 -
    x354)^2) + 1 / sqrt((x49 - x75)^2 + (x189 - x215)^2 + (x329 - x355)^2) + 1
    / sqrt((x49 - x76)^2 + (x189 - x216)^2 + (x329 - x356)^2) + 1 / sqrt((x49
    - x77)^2 + (x189 - x217)^2 + (x329 - x357)^2) + 1 / sqrt((x49 - x78)^2 + (
    x189 - x218)^2 + (x329 - x358)^2) + 1 / sqrt((x49 - x79)^2 + (x189 - x219)^
    2 + (x329 - x359)^2) + 1 / sqrt((x49 - x80)^2 + (x189 - x220)^2 + (x329 -
    x360)^2) + 1 / sqrt((x49 - x81)^2 + (x189 - x221)^2 + (x329 - x361)^2) + 1
    / sqrt((x49 - x82)^2 + (x189 - x222)^2 + (x329 - x362)^2) + 1 / sqrt((x49
    - x83)^2 + (x189 - x223)^2 + (x329 - x363)^2) + 1 / sqrt((x49 - x84)^2 + (
    x189 - x224)^2 + (x329 - x364)^2) + 1 / sqrt((x49 - x85)^2 + (x189 - x225)^
    2 + (x329 - x365)^2) + 1 / sqrt((x49 - x86)^2 + (x189 - x226)^2 + (x329 -
    x366)^2) + 1 / sqrt((x49 - x87)^2 + (x189 - x227)^2 + (x329 - x367)^2) + 1
    / sqrt((x49 - x88)^2 + (x189 - x228)^2 + (x329 - x368)^2) + 1 / sqrt((x49
    - x89)^2 + (x189 - x229)^2 + (x329 - x369)^2) + 1 / sqrt((x49 - x90)^2 + (
    x189 - x230)^2 + (x329 - x370)^2) + 1 / sqrt((x49 - x91)^2 + (x189 - x231)^
    2 + (x329 - x371)^2) + 1 / sqrt((x49 - x92)^2 + (x189 - x232)^2 + (x329 -
    x372)^2) + 1 / sqrt((x49 - x93)^2 + (x189 - x233)^2 + (x329 - x373)^2) + 1
    / sqrt((x49 - x94)^2 + (x189 - x234)^2 + (x329 - x374)^2) + 1 / sqrt((x49
    - x95)^2 + (x189 - x235)^2 + (x329 - x375)^2) + 1 / sqrt((x49 - x96)^2 + (
    x189 - x236)^2 + (x329 - x376)^2) + 1 / sqrt((x49 - x97)^2 + (x189 - x237)^
    2 + (x329 - x377)^2) + 1 / sqrt((x49 - x98)^2 + (x189 - x238)^2 + (x329 -
    x378)^2) + 1 / sqrt((x49 - x99)^2 + (x189 - x239)^2 + (x329 - x379)^2) + 1
    / sqrt((x49 - x100)^2 + (x189 - x240)^2 + (x329 - x380)^2) + 1 / sqrt((x49
    - x101)^2 + (x189 - x241)^2 + (x329 - x381)^2) + 1 / sqrt((x49 - x102)^2
    + (x189 - x242)^2 + (x329 - x382)^2) + 1 / sqrt((x49 - x103)^2 + (x189 -
    x243)^2 + (x329 - x383)^2) + 1 / sqrt((x49 - x104)^2 + (x189 - x244)^2 + (
    x329 - x384)^2) + 1 / sqrt((x49 - x105)^2 + (x189 - x245)^2 + (x329 - x385)
    ^2) + 1 / sqrt((x49 - x106)^2 + (x189 - x246)^2 + (x329 - x386)^2) + 1 /
    sqrt((x49 - x107)^2 + (x189 - x247)^2 + (x329 - x387)^2) + 1 / sqrt((x49 -
    x108)^2 + (x189 - x248)^2 + (x329 - x388)^2) + 1 / sqrt((x49 - x109)^2 + (
    x189 - x249)^2 + (x329 - x389)^2) + 1 / sqrt((x49 - x110)^2 + (x189 - x250)
    ^2 + (x329 - x390)^2) + 1 / sqrt((x49 - x111)^2 + (x189 - x251)^2 + (x329
    - x391)^2) + 1 / sqrt((x49 - x112)^2 + (x189 - x252)^2 + (x329 - x392)^2)
    + 1 / sqrt((x49 - x113)^2 + (x189 - x253)^2 + (x329 - x393)^2) + 1 / sqrt(
    (x49 - x114)^2 + (x189 - x254)^2 + (x329 - x394)^2) + 1 / sqrt((x49 - x115)
    ^2 + (x189 - x255)^2 + (x329 - x395)^2) + 1 / sqrt((x49 - x116)^2 + (x189
    - x256)^2 + (x329 - x396)^2) + 1 / sqrt((x49 - x117)^2 + (x189 - x257)^2
    + (x329 - x397)^2) + 1 / sqrt((x49 - x118)^2 + (x189 - x258)^2 + (x329 -
    x398)^2) + 1 / sqrt((x49 - x119)^2 + (x189 - x259)^2 + (x329 - x399)^2) + 1
    / sqrt((x49 - x120)^2 + (x189 - x260)^2 + (x329 - x400)^2) + 1 / sqrt((x49
    - x121)^2 + (x189 - x261)^2 + (x329 - x401)^2) + 1 / sqrt((x49 - x122)^2
    + (x189 - x262)^2 + (x329 - x402)^2) + 1 / sqrt((x49 - x123)^2 + (x189 -
    x263)^2 + (x329 - x403)^2) + 1 / sqrt((x49 - x124)^2 + (x189 - x264)^2 + (
    x329 - x404)^2) + 1 / sqrt((x49 - x125)^2 + (x189 - x265)^2 + (x329 - x405)
    ^2) + 1 / sqrt((x49 - x126)^2 + (x189 - x266)^2 + (x329 - x406)^2) + 1 /
    sqrt((x49 - x127)^2 + (x189 - x267)^2 + (x329 - x407)^2) + 1 / sqrt((x49 -
    x128)^2 + (x189 - x268)^2 + (x329 - x408)^2) + 1 / sqrt((x49 - x129)^2 + (
    x189 - x269)^2 + (x329 - x409)^2) + 1 / sqrt((x49 - x130)^2 + (x189 - x270)
    ^2 + (x329 - x410)^2) + 1 / sqrt((x49 - x131)^2 + (x189 - x271)^2 + (x329
    - x411)^2) + 1 / sqrt((x49 - x132)^2 + (x189 - x272)^2 + (x329 - x412)^2)
    + 1 / sqrt((x49 - x133)^2 + (x189 - x273)^2 + (x329 - x413)^2) + 1 / sqrt(
    (x49 - x134)^2 + (x189 - x274)^2 + (x329 - x414)^2) + 1 / sqrt((x49 - x135)
    ^2 + (x189 - x275)^2 + (x329 - x415)^2) + 1 / sqrt((x49 - x136)^2 + (x189
    - x276)^2 + (x329 - x416)^2) + 1 / sqrt((x49 - x137)^2 + (x189 - x277)^2
    + (x329 - x417)^2) + 1 / sqrt((x49 - x138)^2 + (x189 - x278)^2 + (x329 -
    x418)^2) + 1 / sqrt((x49 - x139)^2 + (x189 - x279)^2 + (x329 - x419)^2) + 1
    / sqrt((x49 - x140)^2 + (x189 - x280)^2 + (x329 - x420)^2) + 1 / sqrt((x50
    - x51)^2 + (x190 - x191)^2 + (x330 - x331)^2) + 1 / sqrt((x50 - x52)^2 + (
    x190 - x192)^2 + (x330 - x332)^2) + 1 / sqrt((x50 - x53)^2 + (x190 - x193)^
    2 + (x330 - x333)^2) + 1 / sqrt((x50 - x54)^2 + (x190 - x194)^2 + (x330 -
    x334)^2) + 1 / sqrt((x50 - x55)^2 + (x190 - x195)^2 + (x330 - x335)^2) + 1
    / sqrt((x50 - x56)^2 + (x190 - x196)^2 + (x330 - x336)^2) + 1 / sqrt((x50
    - x57)^2 + (x190 - x197)^2 + (x330 - x337)^2) + 1 / sqrt((x50 - x58)^2 + (
    x190 - x198)^2 + (x330 - x338)^2) + 1 / sqrt((x50 - x59)^2 + (x190 - x199)^
    2 + (x330 - x339)^2) + 1 / sqrt((x50 - x60)^2 + (x190 - x200)^2 + (x330 -
    x340)^2) + 1 / sqrt((x50 - x61)^2 + (x190 - x201)^2 + (x330 - x341)^2) + 1
    / sqrt((x50 - x62)^2 + (x190 - x202)^2 + (x330 - x342)^2) + 1 / sqrt((x50
    - x63)^2 + (x190 - x203)^2 + (x330 - x343)^2) + 1 / sqrt((x50 - x64)^2 + (
    x190 - x204)^2 + (x330 - x344)^2) + 1 / sqrt((x50 - x65)^2 + (x190 - x205)^
    2 + (x330 - x345)^2) + 1 / sqrt((x50 - x66)^2 + (x190 - x206)^2 + (x330 -
    x346)^2) + 1 / sqrt((x50 - x67)^2 + (x190 - x207)^2 + (x330 - x347)^2) + 1
    / sqrt((x50 - x68)^2 + (x190 - x208)^2 + (x330 - x348)^2) + 1 / sqrt((x50
    - x69)^2 + (x190 - x209)^2 + (x330 - x349)^2) + 1 / sqrt((x50 - x70)^2 + (
    x190 - x210)^2 + (x330 - x350)^2) + 1 / sqrt((x50 - x71)^2 + (x190 - x211)^
    2 + (x330 - x351)^2) + 1 / sqrt((x50 - x72)^2 + (x190 - x212)^2 + (x330 -
    x352)^2) + 1 / sqrt((x50 - x73)^2 + (x190 - x213)^2 + (x330 - x353)^2) + 1
    / sqrt((x50 - x74)^2 + (x190 - x214)^2 + (x330 - x354)^2) + 1 / sqrt((x50
    - x75)^2 + (x190 - x215)^2 + (x330 - x355)^2) + 1 / sqrt((x50 - x76)^2 + (
    x190 - x216)^2 + (x330 - x356)^2) + 1 / sqrt((x50 - x77)^2 + (x190 - x217)^
    2 + (x330 - x357)^2) + 1 / sqrt((x50 - x78)^2 + (x190 - x218)^2 + (x330 -
    x358)^2) + 1 / sqrt((x50 - x79)^2 + (x190 - x219)^2 + (x330 - x359)^2) + 1
    / sqrt((x50 - x80)^2 + (x190 - x220)^2 + (x330 - x360)^2) + 1 / sqrt((x50
    - x81)^2 + (x190 - x221)^2 + (x330 - x361)^2) + 1 / sqrt((x50 - x82)^2 + (
    x190 - x222)^2 + (x330 - x362)^2) + 1 / sqrt((x50 - x83)^2 + (x190 - x223)^
    2 + (x330 - x363)^2) + 1 / sqrt((x50 - x84)^2 + (x190 - x224)^2 + (x330 -
    x364)^2) + 1 / sqrt((x50 - x85)^2 + (x190 - x225)^2 + (x330 - x365)^2) + 1
    / sqrt((x50 - x86)^2 + (x190 - x226)^2 + (x330 - x366)^2) + 1 / sqrt((x50
    - x87)^2 + (x190 - x227)^2 + (x330 - x367)^2) + 1 / sqrt((x50 - x88)^2 + (
    x190 - x228)^2 + (x330 - x368)^2) + 1 / sqrt((x50 - x89)^2 + (x190 - x229)^
    2 + (x330 - x369)^2) + 1 / sqrt((x50 - x90)^2 + (x190 - x230)^2 + (x330 -
    x370)^2) + 1 / sqrt((x50 - x91)^2 + (x190 - x231)^2 + (x330 - x371)^2) + 1
    / sqrt((x50 - x92)^2 + (x190 - x232)^2 + (x330 - x372)^2) + 1 / sqrt((x50
    - x93)^2 + (x190 - x233)^2 + (x330 - x373)^2) + 1 / sqrt((x50 - x94)^2 + (
    x190 - x234)^2 + (x330 - x374)^2) + 1 / sqrt((x50 - x95)^2 + (x190 - x235)^
    2 + (x330 - x375)^2) + 1 / sqrt((x50 - x96)^2 + (x190 - x236)^2 + (x330 -
    x376)^2) + 1 / sqrt((x50 - x97)^2 + (x190 - x237)^2 + (x330 - x377)^2) + 1
    / sqrt((x50 - x98)^2 + (x190 - x238)^2 + (x330 - x378)^2) + 1 / sqrt((x50
    - x99)^2 + (x190 - x239)^2 + (x330 - x379)^2) + 1 / sqrt((x50 - x100)^2 +
    (x190 - x240)^2 + (x330 - x380)^2) + 1 / sqrt((x50 - x101)^2 + (x190 - x241)
    ^2 + (x330 - x381)^2) + 1 / sqrt((x50 - x102)^2 + (x190 - x242)^2 + (x330
    - x382)^2) + 1 / sqrt((x50 - x103)^2 + (x190 - x243)^2 + (x330 - x383)^2)
    + 1 / sqrt((x50 - x104)^2 + (x190 - x244)^2 + (x330 - x384)^2) + 1 / sqrt(
    (x50 - x105)^2 + (x190 - x245)^2 + (x330 - x385)^2) + 1 / sqrt((x50 - x106)
    ^2 + (x190 - x246)^2 + (x330 - x386)^2) + 1 / sqrt((x50 - x107)^2 + (x190
    - x247)^2 + (x330 - x387)^2) + 1 / sqrt((x50 - x108)^2 + (x190 - x248)^2
    + (x330 - x388)^2) + 1 / sqrt((x50 - x109)^2 + (x190 - x249)^2 + (x330 -
    x389)^2) + 1 / sqrt((x50 - x110)^2 + (x190 - x250)^2 + (x330 - x390)^2) + 1
    / sqrt((x50 - x111)^2 + (x190 - x251)^2 + (x330 - x391)^2) + 1 / sqrt((x50
    - x112)^2 + (x190 - x252)^2 + (x330 - x392)^2) + 1 / sqrt((x50 - x113)^2
    + (x190 - x253)^2 + (x330 - x393)^2) + 1 / sqrt((x50 - x114)^2 + (x190 -
    x254)^2 + (x330 - x394)^2) + 1 / sqrt((x50 - x115)^2 + (x190 - x255)^2 + (
    x330 - x395)^2) + 1 / sqrt((x50 - x116)^2 + (x190 - x256)^2 + (x330 - x396)
    ^2) + 1 / sqrt((x50 - x117)^2 + (x190 - x257)^2 + (x330 - x397)^2) + 1 /
    sqrt((x50 - x118)^2 + (x190 - x258)^2 + (x330 - x398)^2) + 1 / sqrt((x50 -
    x119)^2 + (x190 - x259)^2 + (x330 - x399)^2) + 1 / sqrt((x50 - x120)^2 + (
    x190 - x260)^2 + (x330 - x400)^2) + 1 / sqrt((x50 - x121)^2 + (x190 - x261)
    ^2 + (x330 - x401)^2) + 1 / sqrt((x50 - x122)^2 + (x190 - x262)^2 + (x330
    - x402)^2) + 1 / sqrt((x50 - x123)^2 + (x190 - x263)^2 + (x330 - x403)^2)
    + 1 / sqrt((x50 - x124)^2 + (x190 - x264)^2 + (x330 - x404)^2) + 1 / sqrt(
    (x50 - x125)^2 + (x190 - x265)^2 + (x330 - x405)^2) + 1 / sqrt((x50 - x126)
    ^2 + (x190 - x266)^2 + (x330 - x406)^2) + 1 / sqrt((x50 - x127)^2 + (x190
    - x267)^2 + (x330 - x407)^2) + 1 / sqrt((x50 - x128)^2 + (x190 - x268)^2
    + (x330 - x408)^2) + 1 / sqrt((x50 - x129)^2 + (x190 - x269)^2 + (x330 -
    x409)^2) + 1 / sqrt((x50 - x130)^2 + (x190 - x270)^2 + (x330 - x410)^2) + 1
    / sqrt((x50 - x131)^2 + (x190 - x271)^2 + (x330 - x411)^2) + 1 / sqrt((x50
    - x132)^2 + (x190 - x272)^2 + (x330 - x412)^2) + 1 / sqrt((x50 - x133)^2
    + (x190 - x273)^2 + (x330 - x413)^2) + 1 / sqrt((x50 - x134)^2 + (x190 -
    x274)^2 + (x330 - x414)^2) + 1 / sqrt((x50 - x135)^2 + (x190 - x275)^2 + (
    x330 - x415)^2) + 1 / sqrt((x50 - x136)^2 + (x190 - x276)^2 + (x330 - x416)
    ^2) + 1 / sqrt((x50 - x137)^2 + (x190 - x277)^2 + (x330 - x417)^2) + 1 /
    sqrt((x50 - x138)^2 + (x190 - x278)^2 + (x330 - x418)^2) + 1 / sqrt((x50 -
    x139)^2 + (x190 - x279)^2 + (x330 - x419)^2) + 1 / sqrt((x50 - x140)^2 + (
    x190 - x280)^2 + (x330 - x420)^2) + 1 / sqrt((x51 - x52)^2 + (x191 - x192)^
    2 + (x331 - x332)^2) + 1 / sqrt((x51 - x53)^2 + (x191 - x193)^2 + (x331 -
    x333)^2) + 1 / sqrt((x51 - x54)^2 + (x191 - x194)^2 + (x331 - x334)^2) + 1
    / sqrt((x51 - x55)^2 + (x191 - x195)^2 + (x331 - x335)^2) + 1 / sqrt((x51
    - x56)^2 + (x191 - x196)^2 + (x331 - x336)^2) + 1 / sqrt((x51 - x57)^2 + (
    x191 - x197)^2 + (x331 - x337)^2) + 1 / sqrt((x51 - x58)^2 + (x191 - x198)^
    2 + (x331 - x338)^2) + 1 / sqrt((x51 - x59)^2 + (x191 - x199)^2 + (x331 -
    x339)^2) + 1 / sqrt((x51 - x60)^2 + (x191 - x200)^2 + (x331 - x340)^2) + 1
    / sqrt((x51 - x61)^2 + (x191 - x201)^2 + (x331 - x341)^2) + 1 / sqrt((x51
    - x62)^2 + (x191 - x202)^2 + (x331 - x342)^2) + 1 / sqrt((x51 - x63)^2 + (
    x191 - x203)^2 + (x331 - x343)^2) + 1 / sqrt((x51 - x64)^2 + (x191 - x204)^
    2 + (x331 - x344)^2) + 1 / sqrt((x51 - x65)^2 + (x191 - x205)^2 + (x331 -
    x345)^2) + 1 / sqrt((x51 - x66)^2 + (x191 - x206)^2 + (x331 - x346)^2) + 1
    / sqrt((x51 - x67)^2 + (x191 - x207)^2 + (x331 - x347)^2) + 1 / sqrt((x51
    - x68)^2 + (x191 - x208)^2 + (x331 - x348)^2) + 1 / sqrt((x51 - x69)^2 + (
    x191 - x209)^2 + (x331 - x349)^2) + 1 / sqrt((x51 - x70)^2 + (x191 - x210)^
    2 + (x331 - x350)^2) + 1 / sqrt((x51 - x71)^2 + (x191 - x211)^2 + (x331 -
    x351)^2) + 1 / sqrt((x51 - x72)^2 + (x191 - x212)^2 + (x331 - x352)^2) + 1
    / sqrt((x51 - x73)^2 + (x191 - x213)^2 + (x331 - x353)^2) + 1 / sqrt((x51
    - x74)^2 + (x191 - x214)^2 + (x331 - x354)^2) + 1 / sqrt((x51 - x75)^2 + (
    x191 - x215)^2 + (x331 - x355)^2) + 1 / sqrt((x51 - x76)^2 + (x191 - x216)^
    2 + (x331 - x356)^2) + 1 / sqrt((x51 - x77)^2 + (x191 - x217)^2 + (x331 -
    x357)^2) + 1 / sqrt((x51 - x78)^2 + (x191 - x218)^2 + (x331 - x358)^2) + 1
    / sqrt((x51 - x79)^2 + (x191 - x219)^2 + (x331 - x359)^2) + 1 / sqrt((x51
    - x80)^2 + (x191 - x220)^2 + (x331 - x360)^2) + 1 / sqrt((x51 - x81)^2 + (
    x191 - x221)^2 + (x331 - x361)^2) + 1 / sqrt((x51 - x82)^2 + (x191 - x222)^
    2 + (x331 - x362)^2) + 1 / sqrt((x51 - x83)^2 + (x191 - x223)^2 + (x331 -
    x363)^2) + 1 / sqrt((x51 - x84)^2 + (x191 - x224)^2 + (x331 - x364)^2) + 1
    / sqrt((x51 - x85)^2 + (x191 - x225)^2 + (x331 - x365)^2) + 1 / sqrt((x51
    - x86)^2 + (x191 - x226)^2 + (x331 - x366)^2) + 1 / sqrt((x51 - x87)^2 + (
    x191 - x227)^2 + (x331 - x367)^2) + 1 / sqrt((x51 - x88)^2 + (x191 - x228)^
    2 + (x331 - x368)^2) + 1 / sqrt((x51 - x89)^2 + (x191 - x229)^2 + (x331 -
    x369)^2) + 1 / sqrt((x51 - x90)^2 + (x191 - x230)^2 + (x331 - x370)^2) + 1
    / sqrt((x51 - x91)^2 + (x191 - x231)^2 + (x331 - x371)^2) + 1 / sqrt((x51
    - x92)^2 + (x191 - x232)^2 + (x331 - x372)^2) + 1 / sqrt((x51 - x93)^2 + (
    x191 - x233)^2 + (x331 - x373)^2) + 1 / sqrt((x51 - x94)^2 + (x191 - x234)^
    2 + (x331 - x374)^2) + 1 / sqrt((x51 - x95)^2 + (x191 - x235)^2 + (x331 -
    x375)^2) + 1 / sqrt((x51 - x96)^2 + (x191 - x236)^2 + (x331 - x376)^2) + 1
    / sqrt((x51 - x97)^2 + (x191 - x237)^2 + (x331 - x377)^2) + 1 / sqrt((x51
    - x98)^2 + (x191 - x238)^2 + (x331 - x378)^2) + 1 / sqrt((x51 - x99)^2 + (
    x191 - x239)^2 + (x331 - x379)^2) + 1 / sqrt((x51 - x100)^2 + (x191 - x240)
    ^2 + (x331 - x380)^2) + 1 / sqrt((x51 - x101)^2 + (x191 - x241)^2 + (x331
    - x381)^2) + 1 / sqrt((x51 - x102)^2 + (x191 - x242)^2 + (x331 - x382)^2)
    + 1 / sqrt((x51 - x103)^2 + (x191 - x243)^2 + (x331 - x383)^2) + 1 / sqrt(
    (x51 - x104)^2 + (x191 - x244)^2 + (x331 - x384)^2) + 1 / sqrt((x51 - x105)
    ^2 + (x191 - x245)^2 + (x331 - x385)^2) + 1 / sqrt((x51 - x106)^2 + (x191
    - x246)^2 + (x331 - x386)^2) + 1 / sqrt((x51 - x107)^2 + (x191 - x247)^2
    + (x331 - x387)^2) + 1 / sqrt((x51 - x108)^2 + (x191 - x248)^2 + (x331 -
    x388)^2) + 1 / sqrt((x51 - x109)^2 + (x191 - x249)^2 + (x331 - x389)^2) + 1
    / sqrt((x51 - x110)^2 + (x191 - x250)^2 + (x331 - x390)^2) + 1 / sqrt((x51
    - x111)^2 + (x191 - x251)^2 + (x331 - x391)^2) + 1 / sqrt((x51 - x112)^2
    + (x191 - x252)^2 + (x331 - x392)^2) + 1 / sqrt((x51 - x113)^2 + (x191 -
    x253)^2 + (x331 - x393)^2) + 1 / sqrt((x51 - x114)^2 + (x191 - x254)^2 + (
    x331 - x394)^2) + 1 / sqrt((x51 - x115)^2 + (x191 - x255)^2 + (x331 - x395)
    ^2) + 1 / sqrt((x51 - x116)^2 + (x191 - x256)^2 + (x331 - x396)^2) + 1 /
    sqrt((x51 - x117)^2 + (x191 - x257)^2 + (x331 - x397)^2) + 1 / sqrt((x51 -
    x118)^2 + (x191 - x258)^2 + (x331 - x398)^2) + 1 / sqrt((x51 - x119)^2 + (
    x191 - x259)^2 + (x331 - x399)^2) + 1 / sqrt((x51 - x120)^2 + (x191 - x260)
    ^2 + (x331 - x400)^2) + 1 / sqrt((x51 - x121)^2 + (x191 - x261)^2 + (x331
    - x401)^2) + 1 / sqrt((x51 - x122)^2 + (x191 - x262)^2 + (x331 - x402)^2)
    + 1 / sqrt((x51 - x123)^2 + (x191 - x263)^2 + (x331 - x403)^2) + 1 / sqrt(
    (x51 - x124)^2 + (x191 - x264)^2 + (x331 - x404)^2) + 1 / sqrt((x51 - x125)
    ^2 + (x191 - x265)^2 + (x331 - x405)^2) + 1 / sqrt((x51 - x126)^2 + (x191
    - x266)^2 + (x331 - x406)^2) + 1 / sqrt((x51 - x127)^2 + (x191 - x267)^2
    + (x331 - x407)^2) + 1 / sqrt((x51 - x128)^2 + (x191 - x268)^2 + (x331 -
    x408)^2) + 1 / sqrt((x51 - x129)^2 + (x191 - x269)^2 + (x331 - x409)^2) + 1
    / sqrt((x51 - x130)^2 + (x191 - x270)^2 + (x331 - x410)^2) + 1 / sqrt((x51
    - x131)^2 + (x191 - x271)^2 + (x331 - x411)^2) + 1 / sqrt((x51 - x132)^2
    + (x191 - x272)^2 + (x331 - x412)^2) + 1 / sqrt((x51 - x133)^2 + (x191 -
    x273)^2 + (x331 - x413)^2) + 1 / sqrt((x51 - x134)^2 + (x191 - x274)^2 + (
    x331 - x414)^2) + 1 / sqrt((x51 - x135)^2 + (x191 - x275)^2 + (x331 - x415)
    ^2) + 1 / sqrt((x51 - x136)^2 + (x191 - x276)^2 + (x331 - x416)^2) + 1 /
    sqrt((x51 - x137)^2 + (x191 - x277)^2 + (x331 - x417)^2) + 1 / sqrt((x51 -
    x138)^2 + (x191 - x278)^2 + (x331 - x418)^2) + 1 / sqrt((x51 - x139)^2 + (
    x191 - x279)^2 + (x331 - x419)^2) + 1 / sqrt((x51 - x140)^2 + (x191 - x280)
    ^2 + (x331 - x420)^2) + 1 / sqrt((x52 - x53)^2 + (x192 - x193)^2 + (x332 -
    x333)^2) + 1 / sqrt((x52 - x54)^2 + (x192 - x194)^2 + (x332 - x334)^2) + 1
    / sqrt((x52 - x55)^2 + (x192 - x195)^2 + (x332 - x335)^2) + 1 / sqrt((x52
    - x56)^2 + (x192 - x196)^2 + (x332 - x336)^2) + 1 / sqrt((x52 - x57)^2 + (
    x192 - x197)^2 + (x332 - x337)^2) + 1 / sqrt((x52 - x58)^2 + (x192 - x198)^
    2 + (x332 - x338)^2) + 1 / sqrt((x52 - x59)^2 + (x192 - x199)^2 + (x332 -
    x339)^2) + 1 / sqrt((x52 - x60)^2 + (x192 - x200)^2 + (x332 - x340)^2) + 1
    / sqrt((x52 - x61)^2 + (x192 - x201)^2 + (x332 - x341)^2) + 1 / sqrt((x52
    - x62)^2 + (x192 - x202)^2 + (x332 - x342)^2) + 1 / sqrt((x52 - x63)^2 + (
    x192 - x203)^2 + (x332 - x343)^2) + 1 / sqrt((x52 - x64)^2 + (x192 - x204)^
    2 + (x332 - x344)^2) + 1 / sqrt((x52 - x65)^2 + (x192 - x205)^2 + (x332 -
    x345)^2) + 1 / sqrt((x52 - x66)^2 + (x192 - x206)^2 + (x332 - x346)^2) + 1
    / sqrt((x52 - x67)^2 + (x192 - x207)^2 + (x332 - x347)^2) + 1 / sqrt((x52
    - x68)^2 + (x192 - x208)^2 + (x332 - x348)^2) + 1 / sqrt((x52 - x69)^2 + (
    x192 - x209)^2 + (x332 - x349)^2) + 1 / sqrt((x52 - x70)^2 + (x192 - x210)^
    2 + (x332 - x350)^2) + 1 / sqrt((x52 - x71)^2 + (x192 - x211)^2 + (x332 -
    x351)^2) + 1 / sqrt((x52 - x72)^2 + (x192 - x212)^2 + (x332 - x352)^2) + 1
    / sqrt((x52 - x73)^2 + (x192 - x213)^2 + (x332 - x353)^2) + 1 / sqrt((x52
    - x74)^2 + (x192 - x214)^2 + (x332 - x354)^2) + 1 / sqrt((x52 - x75)^2 + (
    x192 - x215)^2 + (x332 - x355)^2) + 1 / sqrt((x52 - x76)^2 + (x192 - x216)^
    2 + (x332 - x356)^2) + 1 / sqrt((x52 - x77)^2 + (x192 - x217)^2 + (x332 -
    x357)^2) + 1 / sqrt((x52 - x78)^2 + (x192 - x218)^2 + (x332 - x358)^2) + 1
    / sqrt((x52 - x79)^2 + (x192 - x219)^2 + (x332 - x359)^2) + 1 / sqrt((x52
    - x80)^2 + (x192 - x220)^2 + (x332 - x360)^2) + 1 / sqrt((x52 - x81)^2 + (
    x192 - x221)^2 + (x332 - x361)^2) + 1 / sqrt((x52 - x82)^2 + (x192 - x222)^
    2 + (x332 - x362)^2) + 1 / sqrt((x52 - x83)^2 + (x192 - x223)^2 + (x332 -
    x363)^2) + 1 / sqrt((x52 - x84)^2 + (x192 - x224)^2 + (x332 - x364)^2) + 1
    / sqrt((x52 - x85)^2 + (x192 - x225)^2 + (x332 - x365)^2) + 1 / sqrt((x52
    - x86)^2 + (x192 - x226)^2 + (x332 - x366)^2) + 1 / sqrt((x52 - x87)^2 + (
    x192 - x227)^2 + (x332 - x367)^2) + 1 / sqrt((x52 - x88)^2 + (x192 - x228)^
    2 + (x332 - x368)^2) + 1 / sqrt((x52 - x89)^2 + (x192 - x229)^2 + (x332 -
    x369)^2) + 1 / sqrt((x52 - x90)^2 + (x192 - x230)^2 + (x332 - x370)^2) + 1
    / sqrt((x52 - x91)^2 + (x192 - x231)^2 + (x332 - x371)^2) + 1 / sqrt((x52
    - x92)^2 + (x192 - x232)^2 + (x332 - x372)^2) + 1 / sqrt((x52 - x93)^2 + (
    x192 - x233)^2 + (x332 - x373)^2) + 1 / sqrt((x52 - x94)^2 + (x192 - x234)^
    2 + (x332 - x374)^2) + 1 / sqrt((x52 - x95)^2 + (x192 - x235)^2 + (x332 -
    x375)^2) + 1 / sqrt((x52 - x96)^2 + (x192 - x236)^2 + (x332 - x376)^2) + 1
    / sqrt((x52 - x97)^2 + (x192 - x237)^2 + (x332 - x377)^2) + 1 / sqrt((x52
    - x98)^2 + (x192 - x238)^2 + (x332 - x378)^2) + 1 / sqrt((x52 - x99)^2 + (
    x192 - x239)^2 + (x332 - x379)^2) + 1 / sqrt((x52 - x100)^2 + (x192 - x240)
    ^2 + (x332 - x380)^2) + 1 / sqrt((x52 - x101)^2 + (x192 - x241)^2 + (x332
    - x381)^2) + 1 / sqrt((x52 - x102)^2 + (x192 - x242)^2 + (x332 - x382)^2)
    + 1 / sqrt((x52 - x103)^2 + (x192 - x243)^2 + (x332 - x383)^2) + 1 / sqrt(
    (x52 - x104)^2 + (x192 - x244)^2 + (x332 - x384)^2) + 1 / sqrt((x52 - x105)
    ^2 + (x192 - x245)^2 + (x332 - x385)^2) + 1 / sqrt((x52 - x106)^2 + (x192
    - x246)^2 + (x332 - x386)^2) + 1 / sqrt((x52 - x107)^2 + (x192 - x247)^2
    + (x332 - x387)^2) + 1 / sqrt((x52 - x108)^2 + (x192 - x248)^2 + (x332 -
    x388)^2) + 1 / sqrt((x52 - x109)^2 + (x192 - x249)^2 + (x332 - x389)^2) + 1
    / sqrt((x52 - x110)^2 + (x192 - x250)^2 + (x332 - x390)^2) + 1 / sqrt((x52
    - x111)^2 + (x192 - x251)^2 + (x332 - x391)^2) + 1 / sqrt((x52 - x112)^2
    + (x192 - x252)^2 + (x332 - x392)^2) + 1 / sqrt((x52 - x113)^2 + (x192 -
    x253)^2 + (x332 - x393)^2) + 1 / sqrt((x52 - x114)^2 + (x192 - x254)^2 + (
    x332 - x394)^2) + 1 / sqrt((x52 - x115)^2 + (x192 - x255)^2 + (x332 - x395)
    ^2) + 1 / sqrt((x52 - x116)^2 + (x192 - x256)^2 + (x332 - x396)^2) + 1 /
    sqrt((x52 - x117)^2 + (x192 - x257)^2 + (x332 - x397)^2) + 1 / sqrt((x52 -
    x118)^2 + (x192 - x258)^2 + (x332 - x398)^2) + 1 / sqrt((x52 - x119)^2 + (
    x192 - x259)^2 + (x332 - x399)^2) + 1 / sqrt((x52 - x120)^2 + (x192 - x260)
    ^2 + (x332 - x400)^2) + 1 / sqrt((x52 - x121)^2 + (x192 - x261)^2 + (x332
    - x401)^2) + 1 / sqrt((x52 - x122)^2 + (x192 - x262)^2 + (x332 - x402)^2)
    + 1 / sqrt((x52 - x123)^2 + (x192 - x263)^2 + (x332 - x403)^2) + 1 / sqrt(
    (x52 - x124)^2 + (x192 - x264)^2 + (x332 - x404)^2) + 1 / sqrt((x52 - x125)
    ^2 + (x192 - x265)^2 + (x332 - x405)^2) + 1 / sqrt((x52 - x126)^2 + (x192
    - x266)^2 + (x332 - x406)^2) + 1 / sqrt((x52 - x127)^2 + (x192 - x267)^2
    + (x332 - x407)^2) + 1 / sqrt((x52 - x128)^2 + (x192 - x268)^2 + (x332 -
    x408)^2) + 1 / sqrt((x52 - x129)^2 + (x192 - x269)^2 + (x332 - x409)^2) + 1
    / sqrt((x52 - x130)^2 + (x192 - x270)^2 + (x332 - x410)^2) + 1 / sqrt((x52
    - x131)^2 + (x192 - x271)^2 + (x332 - x411)^2) + 1 / sqrt((x52 - x132)^2
    + (x192 - x272)^2 + (x332 - x412)^2) + 1 / sqrt((x52 - x133)^2 + (x192 -
    x273)^2 + (x332 - x413)^2) + 1 / sqrt((x52 - x134)^2 + (x192 - x274)^2 + (
    x332 - x414)^2) + 1 / sqrt((x52 - x135)^2 + (x192 - x275)^2 + (x332 - x415)
    ^2) + 1 / sqrt((x52 - x136)^2 + (x192 - x276)^2 + (x332 - x416)^2) + 1 /
    sqrt((x52 - x137)^2 + (x192 - x277)^2 + (x332 - x417)^2) + 1 / sqrt((x52 -
    x138)^2 + (x192 - x278)^2 + (x332 - x418)^2) + 1 / sqrt((x52 - x139)^2 + (
    x192 - x279)^2 + (x332 - x419)^2) + 1 / sqrt((x52 - x140)^2 + (x192 - x280)
    ^2 + (x332 - x420)^2) + 1 / sqrt((x53 - x54)^2 + (x193 - x194)^2 + (x333 -
    x334)^2) + 1 / sqrt((x53 - x55)^2 + (x193 - x195)^2 + (x333 - x335)^2) + 1
    / sqrt((x53 - x56)^2 + (x193 - x196)^2 + (x333 - x336)^2) + 1 / sqrt((x53
    - x57)^2 + (x193 - x197)^2 + (x333 - x337)^2) + 1 / sqrt((x53 - x58)^2 + (
    x193 - x198)^2 + (x333 - x338)^2) + 1 / sqrt((x53 - x59)^2 + (x193 - x199)^
    2 + (x333 - x339)^2) + 1 / sqrt((x53 - x60)^2 + (x193 - x200)^2 + (x333 -
    x340)^2) + 1 / sqrt((x53 - x61)^2 + (x193 - x201)^2 + (x333 - x341)^2) + 1
    / sqrt((x53 - x62)^2 + (x193 - x202)^2 + (x333 - x342)^2) + 1 / sqrt((x53
    - x63)^2 + (x193 - x203)^2 + (x333 - x343)^2) + 1 / sqrt((x53 - x64)^2 + (
    x193 - x204)^2 + (x333 - x344)^2) + 1 / sqrt((x53 - x65)^2 + (x193 - x205)^
    2 + (x333 - x345)^2) + 1 / sqrt((x53 - x66)^2 + (x193 - x206)^2 + (x333 -
    x346)^2) + 1 / sqrt((x53 - x67)^2 + (x193 - x207)^2 + (x333 - x347)^2) + 1
    / sqrt((x53 - x68)^2 + (x193 - x208)^2 + (x333 - x348)^2) + 1 / sqrt((x53
    - x69)^2 + (x193 - x209)^2 + (x333 - x349)^2) + 1 / sqrt((x53 - x70)^2 + (
    x193 - x210)^2 + (x333 - x350)^2) + 1 / sqrt((x53 - x71)^2 + (x193 - x211)^
    2 + (x333 - x351)^2) + 1 / sqrt((x53 - x72)^2 + (x193 - x212)^2 + (x333 -
    x352)^2) + 1 / sqrt((x53 - x73)^2 + (x193 - x213)^2 + (x333 - x353)^2) + 1
    / sqrt((x53 - x74)^2 + (x193 - x214)^2 + (x333 - x354)^2) + 1 / sqrt((x53
    - x75)^2 + (x193 - x215)^2 + (x333 - x355)^2) + 1 / sqrt((x53 - x76)^2 + (
    x193 - x216)^2 + (x333 - x356)^2) + 1 / sqrt((x53 - x77)^2 + (x193 - x217)^
    2 + (x333 - x357)^2) + 1 / sqrt((x53 - x78)^2 + (x193 - x218)^2 + (x333 -
    x358)^2) + 1 / sqrt((x53 - x79)^2 + (x193 - x219)^2 + (x333 - x359)^2) + 1
    / sqrt((x53 - x80)^2 + (x193 - x220)^2 + (x333 - x360)^2) + 1 / sqrt((x53
    - x81)^2 + (x193 - x221)^2 + (x333 - x361)^2) + 1 / sqrt((x53 - x82)^2 + (
    x193 - x222)^2 + (x333 - x362)^2) + 1 / sqrt((x53 - x83)^2 + (x193 - x223)^
    2 + (x333 - x363)^2) + 1 / sqrt((x53 - x84)^2 + (x193 - x224)^2 + (x333 -
    x364)^2) + 1 / sqrt((x53 - x85)^2 + (x193 - x225)^2 + (x333 - x365)^2) + 1
    / sqrt((x53 - x86)^2 + (x193 - x226)^2 + (x333 - x366)^2) + 1 / sqrt((x53
    - x87)^2 + (x193 - x227)^2 + (x333 - x367)^2) + 1 / sqrt((x53 - x88)^2 + (
    x193 - x228)^2 + (x333 - x368)^2) + 1 / sqrt((x53 - x89)^2 + (x193 - x229)^
    2 + (x333 - x369)^2) + 1 / sqrt((x53 - x90)^2 + (x193 - x230)^2 + (x333 -
    x370)^2) + 1 / sqrt((x53 - x91)^2 + (x193 - x231)^2 + (x333 - x371)^2) + 1
    / sqrt((x53 - x92)^2 + (x193 - x232)^2 + (x333 - x372)^2) + 1 / sqrt((x53
    - x93)^2 + (x193 - x233)^2 + (x333 - x373)^2) + 1 / sqrt((x53 - x94)^2 + (
    x193 - x234)^2 + (x333 - x374)^2) + 1 / sqrt((x53 - x95)^2 + (x193 - x235)^
    2 + (x333 - x375)^2) + 1 / sqrt((x53 - x96)^2 + (x193 - x236)^2 + (x333 -
    x376)^2) + 1 / sqrt((x53 - x97)^2 + (x193 - x237)^2 + (x333 - x377)^2) + 1
    / sqrt((x53 - x98)^2 + (x193 - x238)^2 + (x333 - x378)^2) + 1 / sqrt((x53
    - x99)^2 + (x193 - x239)^2 + (x333 - x379)^2) + 1 / sqrt((x53 - x100)^2 +
    (x193 - x240)^2 + (x333 - x380)^2) + 1 / sqrt((x53 - x101)^2 + (x193 - x241)
    ^2 + (x333 - x381)^2) + 1 / sqrt((x53 - x102)^2 + (x193 - x242)^2 + (x333
    - x382)^2) + 1 / sqrt((x53 - x103)^2 + (x193 - x243)^2 + (x333 - x383)^2)
    + 1 / sqrt((x53 - x104)^2 + (x193 - x244)^2 + (x333 - x384)^2) + 1 / sqrt(
    (x53 - x105)^2 + (x193 - x245)^2 + (x333 - x385)^2) + 1 / sqrt((x53 - x106)
    ^2 + (x193 - x246)^2 + (x333 - x386)^2) + 1 / sqrt((x53 - x107)^2 + (x193
    - x247)^2 + (x333 - x387)^2) + 1 / sqrt((x53 - x108)^2 + (x193 - x248)^2
    + (x333 - x388)^2) + 1 / sqrt((x53 - x109)^2 + (x193 - x249)^2 + (x333 -
    x389)^2) + 1 / sqrt((x53 - x110)^2 + (x193 - x250)^2 + (x333 - x390)^2) + 1
    / sqrt((x53 - x111)^2 + (x193 - x251)^2 + (x333 - x391)^2) + 1 / sqrt((x53
    - x112)^2 + (x193 - x252)^2 + (x333 - x392)^2) + 1 / sqrt((x53 - x113)^2
    + (x193 - x253)^2 + (x333 - x393)^2) + 1 / sqrt((x53 - x114)^2 + (x193 -
    x254)^2 + (x333 - x394)^2) + 1 / sqrt((x53 - x115)^2 + (x193 - x255)^2 + (
    x333 - x395)^2) + 1 / sqrt((x53 - x116)^2 + (x193 - x256)^2 + (x333 - x396)
    ^2) + 1 / sqrt((x53 - x117)^2 + (x193 - x257)^2 + (x333 - x397)^2) + 1 /
    sqrt((x53 - x118)^2 + (x193 - x258)^2 + (x333 - x398)^2) + 1 / sqrt((x53 -
    x119)^2 + (x193 - x259)^2 + (x333 - x399)^2) + 1 / sqrt((x53 - x120)^2 + (
    x193 - x260)^2 + (x333 - x400)^2) + 1 / sqrt((x53 - x121)^2 + (x193 - x261)
    ^2 + (x333 - x401)^2) + 1 / sqrt((x53 - x122)^2 + (x193 - x262)^2 + (x333
    - x402)^2) + 1 / sqrt((x53 - x123)^2 + (x193 - x263)^2 + (x333 - x403)^2)
    + 1 / sqrt((x53 - x124)^2 + (x193 - x264)^2 + (x333 - x404)^2) + 1 / sqrt(
    (x53 - x125)^2 + (x193 - x265)^2 + (x333 - x405)^2) + 1 / sqrt((x53 - x126)
    ^2 + (x193 - x266)^2 + (x333 - x406)^2) + 1 / sqrt((x53 - x127)^2 + (x193
    - x267)^2 + (x333 - x407)^2) + 1 / sqrt((x53 - x128)^2 + (x193 - x268)^2
    + (x333 - x408)^2) + 1 / sqrt((x53 - x129)^2 + (x193 - x269)^2 + (x333 -
    x409)^2) + 1 / sqrt((x53 - x130)^2 + (x193 - x270)^2 + (x333 - x410)^2) + 1
    / sqrt((x53 - x131)^2 + (x193 - x271)^2 + (x333 - x411)^2) + 1 / sqrt((x53
    - x132)^2 + (x193 - x272)^2 + (x333 - x412)^2) + 1 / sqrt((x53 - x133)^2
    + (x193 - x273)^2 + (x333 - x413)^2) + 1 / sqrt((x53 - x134)^2 + (x193 -
    x274)^2 + (x333 - x414)^2) + 1 / sqrt((x53 - x135)^2 + (x193 - x275)^2 + (
    x333 - x415)^2) + 1 / sqrt((x53 - x136)^2 + (x193 - x276)^2 + (x333 - x416)
    ^2) + 1 / sqrt((x53 - x137)^2 + (x193 - x277)^2 + (x333 - x417)^2) + 1 /
    sqrt((x53 - x138)^2 + (x193 - x278)^2 + (x333 - x418)^2) + 1 / sqrt((x53 -
    x139)^2 + (x193 - x279)^2 + (x333 - x419)^2) + 1 / sqrt((x53 - x140)^2 + (
    x193 - x280)^2 + (x333 - x420)^2) + 1 / sqrt((x54 - x55)^2 + (x194 - x195)^
    2 + (x334 - x335)^2) + 1 / sqrt((x54 - x56)^2 + (x194 - x196)^2 + (x334 -
    x336)^2) + 1 / sqrt((x54 - x57)^2 + (x194 - x197)^2 + (x334 - x337)^2) + 1
    / sqrt((x54 - x58)^2 + (x194 - x198)^2 + (x334 - x338)^2) + 1 / sqrt((x54
    - x59)^2 + (x194 - x199)^2 + (x334 - x339)^2) + 1 / sqrt((x54 - x60)^2 + (
    x194 - x200)^2 + (x334 - x340)^2) + 1 / sqrt((x54 - x61)^2 + (x194 - x201)^
    2 + (x334 - x341)^2) + 1 / sqrt((x54 - x62)^2 + (x194 - x202)^2 + (x334 -
    x342)^2) + 1 / sqrt((x54 - x63)^2 + (x194 - x203)^2 + (x334 - x343)^2) + 1
    / sqrt((x54 - x64)^2 + (x194 - x204)^2 + (x334 - x344)^2) + 1 / sqrt((x54
    - x65)^2 + (x194 - x205)^2 + (x334 - x345)^2) + 1 / sqrt((x54 - x66)^2 + (
    x194 - x206)^2 + (x334 - x346)^2) + 1 / sqrt((x54 - x67)^2 + (x194 - x207)^
    2 + (x334 - x347)^2) + 1 / sqrt((x54 - x68)^2 + (x194 - x208)^2 + (x334 -
    x348)^2) + 1 / sqrt((x54 - x69)^2 + (x194 - x209)^2 + (x334 - x349)^2) + 1
    / sqrt((x54 - x70)^2 + (x194 - x210)^2 + (x334 - x350)^2) + 1 / sqrt((x54
    - x71)^2 + (x194 - x211)^2 + (x334 - x351)^2) + 1 / sqrt((x54 - x72)^2 + (
    x194 - x212)^2 + (x334 - x352)^2) + 1 / sqrt((x54 - x73)^2 + (x194 - x213)^
    2 + (x334 - x353)^2) + 1 / sqrt((x54 - x74)^2 + (x194 - x214)^2 + (x334 -
    x354)^2) + 1 / sqrt((x54 - x75)^2 + (x194 - x215)^2 + (x334 - x355)^2) + 1
    / sqrt((x54 - x76)^2 + (x194 - x216)^2 + (x334 - x356)^2) + 1 / sqrt((x54
    - x77)^2 + (x194 - x217)^2 + (x334 - x357)^2) + 1 / sqrt((x54 - x78)^2 + (
    x194 - x218)^2 + (x334 - x358)^2) + 1 / sqrt((x54 - x79)^2 + (x194 - x219)^
    2 + (x334 - x359)^2) + 1 / sqrt((x54 - x80)^2 + (x194 - x220)^2 + (x334 -
    x360)^2) + 1 / sqrt((x54 - x81)^2 + (x194 - x221)^2 + (x334 - x361)^2) + 1
    / sqrt((x54 - x82)^2 + (x194 - x222)^2 + (x334 - x362)^2) + 1 / sqrt((x54
    - x83)^2 + (x194 - x223)^2 + (x334 - x363)^2) + 1 / sqrt((x54 - x84)^2 + (
    x194 - x224)^2 + (x334 - x364)^2) + 1 / sqrt((x54 - x85)^2 + (x194 - x225)^
    2 + (x334 - x365)^2) + 1 / sqrt((x54 - x86)^2 + (x194 - x226)^2 + (x334 -
    x366)^2) + 1 / sqrt((x54 - x87)^2 + (x194 - x227)^2 + (x334 - x367)^2) + 1
    / sqrt((x54 - x88)^2 + (x194 - x228)^2 + (x334 - x368)^2) + 1 / sqrt((x54
    - x89)^2 + (x194 - x229)^2 + (x334 - x369)^2) + 1 / sqrt((x54 - x90)^2 + (
    x194 - x230)^2 + (x334 - x370)^2) + 1 / sqrt((x54 - x91)^2 + (x194 - x231)^
    2 + (x334 - x371)^2) + 1 / sqrt((x54 - x92)^2 + (x194 - x232)^2 + (x334 -
    x372)^2) + 1 / sqrt((x54 - x93)^2 + (x194 - x233)^2 + (x334 - x373)^2) + 1
    / sqrt((x54 - x94)^2 + (x194 - x234)^2 + (x334 - x374)^2) + 1 / sqrt((x54
    - x95)^2 + (x194 - x235)^2 + (x334 - x375)^2) + 1 / sqrt((x54 - x96)^2 + (
    x194 - x236)^2 + (x334 - x376)^2) + 1 / sqrt((x54 - x97)^2 + (x194 - x237)^
    2 + (x334 - x377)^2) + 1 / sqrt((x54 - x98)^2 + (x194 - x238)^2 + (x334 -
    x378)^2) + 1 / sqrt((x54 - x99)^2 + (x194 - x239)^2 + (x334 - x379)^2) + 1
    / sqrt((x54 - x100)^2 + (x194 - x240)^2 + (x334 - x380)^2) + 1 / sqrt((x54
    - x101)^2 + (x194 - x241)^2 + (x334 - x381)^2) + 1 / sqrt((x54 - x102)^2
    + (x194 - x242)^2 + (x334 - x382)^2) + 1 / sqrt((x54 - x103)^2 + (x194 -
    x243)^2 + (x334 - x383)^2) + 1 / sqrt((x54 - x104)^2 + (x194 - x244)^2 + (
    x334 - x384)^2) + 1 / sqrt((x54 - x105)^2 + (x194 - x245)^2 + (x334 - x385)
    ^2) + 1 / sqrt((x54 - x106)^2 + (x194 - x246)^2 + (x334 - x386)^2) + 1 /
    sqrt((x54 - x107)^2 + (x194 - x247)^2 + (x334 - x387)^2) + 1 / sqrt((x54 -
    x108)^2 + (x194 - x248)^2 + (x334 - x388)^2) + 1 / sqrt((x54 - x109)^2 + (
    x194 - x249)^2 + (x334 - x389)^2) + 1 / sqrt((x54 - x110)^2 + (x194 - x250)
    ^2 + (x334 - x390)^2) + 1 / sqrt((x54 - x111)^2 + (x194 - x251)^2 + (x334
    - x391)^2) + 1 / sqrt((x54 - x112)^2 + (x194 - x252)^2 + (x334 - x392)^2)
    + 1 / sqrt((x54 - x113)^2 + (x194 - x253)^2 + (x334 - x393)^2) + 1 / sqrt(
    (x54 - x114)^2 + (x194 - x254)^2 + (x334 - x394)^2) + 1 / sqrt((x54 - x115)
    ^2 + (x194 - x255)^2 + (x334 - x395)^2) + 1 / sqrt((x54 - x116)^2 + (x194
    - x256)^2 + (x334 - x396)^2) + 1 / sqrt((x54 - x117)^2 + (x194 - x257)^2
    + (x334 - x397)^2) + 1 / sqrt((x54 - x118)^2 + (x194 - x258)^2 + (x334 -
    x398)^2) + 1 / sqrt((x54 - x119)^2 + (x194 - x259)^2 + (x334 - x399)^2) + 1
    / sqrt((x54 - x120)^2 + (x194 - x260)^2 + (x334 - x400)^2) + 1 / sqrt((x54
    - x121)^2 + (x194 - x261)^2 + (x334 - x401)^2) + 1 / sqrt((x54 - x122)^2
    + (x194 - x262)^2 + (x334 - x402)^2) + 1 / sqrt((x54 - x123)^2 + (x194 -
    x263)^2 + (x334 - x403)^2) + 1 / sqrt((x54 - x124)^2 + (x194 - x264)^2 + (
    x334 - x404)^2) + 1 / sqrt((x54 - x125)^2 + (x194 - x265)^2 + (x334 - x405)
    ^2) + 1 / sqrt((x54 - x126)^2 + (x194 - x266)^2 + (x334 - x406)^2) + 1 /
    sqrt((x54 - x127)^2 + (x194 - x267)^2 + (x334 - x407)^2) + 1 / sqrt((x54 -
    x128)^2 + (x194 - x268)^2 + (x334 - x408)^2) + 1 / sqrt((x54 - x129)^2 + (
    x194 - x269)^2 + (x334 - x409)^2) + 1 / sqrt((x54 - x130)^2 + (x194 - x270)
    ^2 + (x334 - x410)^2) + 1 / sqrt((x54 - x131)^2 + (x194 - x271)^2 + (x334
    - x411)^2) + 1 / sqrt((x54 - x132)^2 + (x194 - x272)^2 + (x334 - x412)^2)
    + 1 / sqrt((x54 - x133)^2 + (x194 - x273)^2 + (x334 - x413)^2) + 1 / sqrt(
    (x54 - x134)^2 + (x194 - x274)^2 + (x334 - x414)^2) + 1 / sqrt((x54 - x135)
    ^2 + (x194 - x275)^2 + (x334 - x415)^2) + 1 / sqrt((x54 - x136)^2 + (x194
    - x276)^2 + (x334 - x416)^2) + 1 / sqrt((x54 - x137)^2 + (x194 - x277)^2
    + (x334 - x417)^2) + 1 / sqrt((x54 - x138)^2 + (x194 - x278)^2 + (x334 -
    x418)^2) + 1 / sqrt((x54 - x139)^2 + (x194 - x279)^2 + (x334 - x419)^2) + 1
    / sqrt((x54 - x140)^2 + (x194 - x280)^2 + (x334 - x420)^2) + 1 / sqrt((x55
    - x56)^2 + (x195 - x196)^2 + (x335 - x336)^2) + 1 / sqrt((x55 - x57)^2 + (
    x195 - x197)^2 + (x335 - x337)^2) + 1 / sqrt((x55 - x58)^2 + (x195 - x198)^
    2 + (x335 - x338)^2) + 1 / sqrt((x55 - x59)^2 + (x195 - x199)^2 + (x335 -
    x339)^2) + 1 / sqrt((x55 - x60)^2 + (x195 - x200)^2 + (x335 - x340)^2) + 1
    / sqrt((x55 - x61)^2 + (x195 - x201)^2 + (x335 - x341)^2) + 1 / sqrt((x55
    - x62)^2 + (x195 - x202)^2 + (x335 - x342)^2) + 1 / sqrt((x55 - x63)^2 + (
    x195 - x203)^2 + (x335 - x343)^2) + 1 / sqrt((x55 - x64)^2 + (x195 - x204)^
    2 + (x335 - x344)^2) + 1 / sqrt((x55 - x65)^2 + (x195 - x205)^2 + (x335 -
    x345)^2) + 1 / sqrt((x55 - x66)^2 + (x195 - x206)^2 + (x335 - x346)^2) + 1
    / sqrt((x55 - x67)^2 + (x195 - x207)^2 + (x335 - x347)^2) + 1 / sqrt((x55
    - x68)^2 + (x195 - x208)^2 + (x335 - x348)^2) + 1 / sqrt((x55 - x69)^2 + (
    x195 - x209)^2 + (x335 - x349)^2) + 1 / sqrt((x55 - x70)^2 + (x195 - x210)^
    2 + (x335 - x350)^2) + 1 / sqrt((x55 - x71)^2 + (x195 - x211)^2 + (x335 -
    x351)^2) + 1 / sqrt((x55 - x72)^2 + (x195 - x212)^2 + (x335 - x352)^2) + 1
    / sqrt((x55 - x73)^2 + (x195 - x213)^2 + (x335 - x353)^2) + 1 / sqrt((x55
    - x74)^2 + (x195 - x214)^2 + (x335 - x354)^2) + 1 / sqrt((x55 - x75)^2 + (
    x195 - x215)^2 + (x335 - x355)^2) + 1 / sqrt((x55 - x76)^2 + (x195 - x216)^
    2 + (x335 - x356)^2) + 1 / sqrt((x55 - x77)^2 + (x195 - x217)^2 + (x335 -
    x357)^2) + 1 / sqrt((x55 - x78)^2 + (x195 - x218)^2 + (x335 - x358)^2) + 1
    / sqrt((x55 - x79)^2 + (x195 - x219)^2 + (x335 - x359)^2) + 1 / sqrt((x55
    - x80)^2 + (x195 - x220)^2 + (x335 - x360)^2) + 1 / sqrt((x55 - x81)^2 + (
    x195 - x221)^2 + (x335 - x361)^2) + 1 / sqrt((x55 - x82)^2 + (x195 - x222)^
    2 + (x335 - x362)^2) + 1 / sqrt((x55 - x83)^2 + (x195 - x223)^2 + (x335 -
    x363)^2) + 1 / sqrt((x55 - x84)^2 + (x195 - x224)^2 + (x335 - x364)^2) + 1
    / sqrt((x55 - x85)^2 + (x195 - x225)^2 + (x335 - x365)^2) + 1 / sqrt((x55
    - x86)^2 + (x195 - x226)^2 + (x335 - x366)^2) + 1 / sqrt((x55 - x87)^2 + (
    x195 - x227)^2 + (x335 - x367)^2) + 1 / sqrt((x55 - x88)^2 + (x195 - x228)^
    2 + (x335 - x368)^2) + 1 / sqrt((x55 - x89)^2 + (x195 - x229)^2 + (x335 -
    x369)^2) + 1 / sqrt((x55 - x90)^2 + (x195 - x230)^2 + (x335 - x370)^2) + 1
    / sqrt((x55 - x91)^2 + (x195 - x231)^2 + (x335 - x371)^2) + 1 / sqrt((x55
    - x92)^2 + (x195 - x232)^2 + (x335 - x372)^2) + 1 / sqrt((x55 - x93)^2 + (
    x195 - x233)^2 + (x335 - x373)^2) + 1 / sqrt((x55 - x94)^2 + (x195 - x234)^
    2 + (x335 - x374)^2) + 1 / sqrt((x55 - x95)^2 + (x195 - x235)^2 + (x335 -
    x375)^2) + 1 / sqrt((x55 - x96)^2 + (x195 - x236)^2 + (x335 - x376)^2) + 1
    / sqrt((x55 - x97)^2 + (x195 - x237)^2 + (x335 - x377)^2) + 1 / sqrt((x55
    - x98)^2 + (x195 - x238)^2 + (x335 - x378)^2) + 1 / sqrt((x55 - x99)^2 + (
    x195 - x239)^2 + (x335 - x379)^2) + 1 / sqrt((x55 - x100)^2 + (x195 - x240)
    ^2 + (x335 - x380)^2) + 1 / sqrt((x55 - x101)^2 + (x195 - x241)^2 + (x335
    - x381)^2) + 1 / sqrt((x55 - x102)^2 + (x195 - x242)^2 + (x335 - x382)^2)
    + 1 / sqrt((x55 - x103)^2 + (x195 - x243)^2 + (x335 - x383)^2) + 1 / sqrt(
    (x55 - x104)^2 + (x195 - x244)^2 + (x335 - x384)^2) + 1 / sqrt((x55 - x105)
    ^2 + (x195 - x245)^2 + (x335 - x385)^2) + 1 / sqrt((x55 - x106)^2 + (x195
    - x246)^2 + (x335 - x386)^2) + 1 / sqrt((x55 - x107)^2 + (x195 - x247)^2
    + (x335 - x387)^2) + 1 / sqrt((x55 - x108)^2 + (x195 - x248)^2 + (x335 -
    x388)^2) + 1 / sqrt((x55 - x109)^2 + (x195 - x249)^2 + (x335 - x389)^2) + 1
    / sqrt((x55 - x110)^2 + (x195 - x250)^2 + (x335 - x390)^2) + 1 / sqrt((x55
    - x111)^2 + (x195 - x251)^2 + (x335 - x391)^2) + 1 / sqrt((x55 - x112)^2
    + (x195 - x252)^2 + (x335 - x392)^2) + 1 / sqrt((x55 - x113)^2 + (x195 -
    x253)^2 + (x335 - x393)^2) + 1 / sqrt((x55 - x114)^2 + (x195 - x254)^2 + (
    x335 - x394)^2) + 1 / sqrt((x55 - x115)^2 + (x195 - x255)^2 + (x335 - x395)
    ^2) + 1 / sqrt((x55 - x116)^2 + (x195 - x256)^2 + (x335 - x396)^2) + 1 /
    sqrt((x55 - x117)^2 + (x195 - x257)^2 + (x335 - x397)^2) + 1 / sqrt((x55 -
    x118)^2 + (x195 - x258)^2 + (x335 - x398)^2) + 1 / sqrt((x55 - x119)^2 + (
    x195 - x259)^2 + (x335 - x399)^2) + 1 / sqrt((x55 - x120)^2 + (x195 - x260)
    ^2 + (x335 - x400)^2) + 1 / sqrt((x55 - x121)^2 + (x195 - x261)^2 + (x335
    - x401)^2) + 1 / sqrt((x55 - x122)^2 + (x195 - x262)^2 + (x335 - x402)^2)
    + 1 / sqrt((x55 - x123)^2 + (x195 - x263)^2 + (x335 - x403)^2) + 1 / sqrt(
    (x55 - x124)^2 + (x195 - x264)^2 + (x335 - x404)^2) + 1 / sqrt((x55 - x125)
    ^2 + (x195 - x265)^2 + (x335 - x405)^2) + 1 / sqrt((x55 - x126)^2 + (x195
    - x266)^2 + (x335 - x406)^2) + 1 / sqrt((x55 - x127)^2 + (x195 - x267)^2
    + (x335 - x407)^2) + 1 / sqrt((x55 - x128)^2 + (x195 - x268)^2 + (x335 -
    x408)^2) + 1 / sqrt((x55 - x129)^2 + (x195 - x269)^2 + (x335 - x409)^2) + 1
    / sqrt((x55 - x130)^2 + (x195 - x270)^2 + (x335 - x410)^2) + 1 / sqrt((x55
    - x131)^2 + (x195 - x271)^2 + (x335 - x411)^2) + 1 / sqrt((x55 - x132)^2
    + (x195 - x272)^2 + (x335 - x412)^2) + 1 / sqrt((x55 - x133)^2 + (x195 -
    x273)^2 + (x335 - x413)^2) + 1 / sqrt((x55 - x134)^2 + (x195 - x274)^2 + (
    x335 - x414)^2) + 1 / sqrt((x55 - x135)^2 + (x195 - x275)^2 + (x335 - x415)
    ^2) + 1 / sqrt((x55 - x136)^2 + (x195 - x276)^2 + (x335 - x416)^2) + 1 /
    sqrt((x55 - x137)^2 + (x195 - x277)^2 + (x335 - x417)^2) + 1 / sqrt((x55 -
    x138)^2 + (x195 - x278)^2 + (x335 - x418)^2) + 1 / sqrt((x55 - x139)^2 + (
    x195 - x279)^2 + (x335 - x419)^2) + 1 / sqrt((x55 - x140)^2 + (x195 - x280)
    ^2 + (x335 - x420)^2) + 1 / sqrt((x56 - x57)^2 + (x196 - x197)^2 + (x336 -
    x337)^2) + 1 / sqrt((x56 - x58)^2 + (x196 - x198)^2 + (x336 - x338)^2) + 1
    / sqrt((x56 - x59)^2 + (x196 - x199)^2 + (x336 - x339)^2) + 1 / sqrt((x56
    - x60)^2 + (x196 - x200)^2 + (x336 - x340)^2) + 1 / sqrt((x56 - x61)^2 + (
    x196 - x201)^2 + (x336 - x341)^2) + 1 / sqrt((x56 - x62)^2 + (x196 - x202)^
    2 + (x336 - x342)^2) + 1 / sqrt((x56 - x63)^2 + (x196 - x203)^2 + (x336 -
    x343)^2) + 1 / sqrt((x56 - x64)^2 + (x196 - x204)^2 + (x336 - x344)^2) + 1
    / sqrt((x56 - x65)^2 + (x196 - x205)^2 + (x336 - x345)^2) + 1 / sqrt((x56
    - x66)^2 + (x196 - x206)^2 + (x336 - x346)^2) + 1 / sqrt((x56 - x67)^2 + (
    x196 - x207)^2 + (x336 - x347)^2) + 1 / sqrt((x56 - x68)^2 + (x196 - x208)^
    2 + (x336 - x348)^2) + 1 / sqrt((x56 - x69)^2 + (x196 - x209)^2 + (x336 -
    x349)^2) + 1 / sqrt((x56 - x70)^2 + (x196 - x210)^2 + (x336 - x350)^2) + 1
    / sqrt((x56 - x71)^2 + (x196 - x211)^2 + (x336 - x351)^2) + 1 / sqrt((x56
    - x72)^2 + (x196 - x212)^2 + (x336 - x352)^2) + 1 / sqrt((x56 - x73)^2 + (
    x196 - x213)^2 + (x336 - x353)^2) + 1 / sqrt((x56 - x74)^2 + (x196 - x214)^
    2 + (x336 - x354)^2) + 1 / sqrt((x56 - x75)^2 + (x196 - x215)^2 + (x336 -
    x355)^2) + 1 / sqrt((x56 - x76)^2 + (x196 - x216)^2 + (x336 - x356)^2) + 1
    / sqrt((x56 - x77)^2 + (x196 - x217)^2 + (x336 - x357)^2) + 1 / sqrt((x56
    - x78)^2 + (x196 - x218)^2 + (x336 - x358)^2) + 1 / sqrt((x56 - x79)^2 + (
    x196 - x219)^2 + (x336 - x359)^2) + 1 / sqrt((x56 - x80)^2 + (x196 - x220)^
    2 + (x336 - x360)^2) + 1 / sqrt((x56 - x81)^2 + (x196 - x221)^2 + (x336 -
    x361)^2) + 1 / sqrt((x56 - x82)^2 + (x196 - x222)^2 + (x336 - x362)^2) + 1
    / sqrt((x56 - x83)^2 + (x196 - x223)^2 + (x336 - x363)^2) + 1 / sqrt((x56
    - x84)^2 + (x196 - x224)^2 + (x336 - x364)^2) + 1 / sqrt((x56 - x85)^2 + (
    x196 - x225)^2 + (x336 - x365)^2) + 1 / sqrt((x56 - x86)^2 + (x196 - x226)^
    2 + (x336 - x366)^2) + 1 / sqrt((x56 - x87)^2 + (x196 - x227)^2 + (x336 -
    x367)^2) + 1 / sqrt((x56 - x88)^2 + (x196 - x228)^2 + (x336 - x368)^2) + 1
    / sqrt((x56 - x89)^2 + (x196 - x229)^2 + (x336 - x369)^2) + 1 / sqrt((x56
    - x90)^2 + (x196 - x230)^2 + (x336 - x370)^2) + 1 / sqrt((x56 - x91)^2 + (
    x196 - x231)^2 + (x336 - x371)^2) + 1 / sqrt((x56 - x92)^2 + (x196 - x232)^
    2 + (x336 - x372)^2) + 1 / sqrt((x56 - x93)^2 + (x196 - x233)^2 + (x336 -
    x373)^2) + 1 / sqrt((x56 - x94)^2 + (x196 - x234)^2 + (x336 - x374)^2) + 1
    / sqrt((x56 - x95)^2 + (x196 - x235)^2 + (x336 - x375)^2) + 1 / sqrt((x56
    - x96)^2 + (x196 - x236)^2 + (x336 - x376)^2) + 1 / sqrt((x56 - x97)^2 + (
    x196 - x237)^2 + (x336 - x377)^2) + 1 / sqrt((x56 - x98)^2 + (x196 - x238)^
    2 + (x336 - x378)^2) + 1 / sqrt((x56 - x99)^2 + (x196 - x239)^2 + (x336 -
    x379)^2) + 1 / sqrt((x56 - x100)^2 + (x196 - x240)^2 + (x336 - x380)^2) + 1
    / sqrt((x56 - x101)^2 + (x196 - x241)^2 + (x336 - x381)^2) + 1 / sqrt((x56
    - x102)^2 + (x196 - x242)^2 + (x336 - x382)^2) + 1 / sqrt((x56 - x103)^2
    + (x196 - x243)^2 + (x336 - x383)^2) + 1 / sqrt((x56 - x104)^2 + (x196 -
    x244)^2 + (x336 - x384)^2) + 1 / sqrt((x56 - x105)^2 + (x196 - x245)^2 + (
    x336 - x385)^2) + 1 / sqrt((x56 - x106)^2 + (x196 - x246)^2 + (x336 - x386)
    ^2) + 1 / sqrt((x56 - x107)^2 + (x196 - x247)^2 + (x336 - x387)^2) + 1 /
    sqrt((x56 - x108)^2 + (x196 - x248)^2 + (x336 - x388)^2) + 1 / sqrt((x56 -
    x109)^2 + (x196 - x249)^2 + (x336 - x389)^2) + 1 / sqrt((x56 - x110)^2 + (
    x196 - x250)^2 + (x336 - x390)^2) + 1 / sqrt((x56 - x111)^2 + (x196 - x251)
    ^2 + (x336 - x391)^2) + 1 / sqrt((x56 - x112)^2 + (x196 - x252)^2 + (x336
    - x392)^2) + 1 / sqrt((x56 - x113)^2 + (x196 - x253)^2 + (x336 - x393)^2)
    + 1 / sqrt((x56 - x114)^2 + (x196 - x254)^2 + (x336 - x394)^2) + 1 / sqrt(
    (x56 - x115)^2 + (x196 - x255)^2 + (x336 - x395)^2) + 1 / sqrt((x56 - x116)
    ^2 + (x196 - x256)^2 + (x336 - x396)^2) + 1 / sqrt((x56 - x117)^2 + (x196
    - x257)^2 + (x336 - x397)^2) + 1 / sqrt((x56 - x118)^2 + (x196 - x258)^2
    + (x336 - x398)^2) + 1 / sqrt((x56 - x119)^2 + (x196 - x259)^2 + (x336 -
    x399)^2) + 1 / sqrt((x56 - x120)^2 + (x196 - x260)^2 + (x336 - x400)^2) + 1
    / sqrt((x56 - x121)^2 + (x196 - x261)^2 + (x336 - x401)^2) + 1 / sqrt((x56
    - x122)^2 + (x196 - x262)^2 + (x336 - x402)^2) + 1 / sqrt((x56 - x123)^2
    + (x196 - x263)^2 + (x336 - x403)^2) + 1 / sqrt((x56 - x124)^2 + (x196 -
    x264)^2 + (x336 - x404)^2) + 1 / sqrt((x56 - x125)^2 + (x196 - x265)^2 + (
    x336 - x405)^2) + 1 / sqrt((x56 - x126)^2 + (x196 - x266)^2 + (x336 - x406)
    ^2) + 1 / sqrt((x56 - x127)^2 + (x196 - x267)^2 + (x336 - x407)^2) + 1 /
    sqrt((x56 - x128)^2 + (x196 - x268)^2 + (x336 - x408)^2) + 1 / sqrt((x56 -
    x129)^2 + (x196 - x269)^2 + (x336 - x409)^2) + 1 / sqrt((x56 - x130)^2 + (
    x196 - x270)^2 + (x336 - x410)^2) + 1 / sqrt((x56 - x131)^2 + (x196 - x271)
    ^2 + (x336 - x411)^2) + 1 / sqrt((x56 - x132)^2 + (x196 - x272)^2 + (x336
    - x412)^2) + 1 / sqrt((x56 - x133)^2 + (x196 - x273)^2 + (x336 - x413)^2)
    + 1 / sqrt((x56 - x134)^2 + (x196 - x274)^2 + (x336 - x414)^2) + 1 / sqrt(
    (x56 - x135)^2 + (x196 - x275)^2 + (x336 - x415)^2) + 1 / sqrt((x56 - x136)
    ^2 + (x196 - x276)^2 + (x336 - x416)^2) + 1 / sqrt((x56 - x137)^2 + (x196
    - x277)^2 + (x336 - x417)^2) + 1 / sqrt((x56 - x138)^2 + (x196 - x278)^2
    + (x336 - x418)^2) + 1 / sqrt((x56 - x139)^2 + (x196 - x279)^2 + (x336 -
    x419)^2) + 1 / sqrt((x56 - x140)^2 + (x196 - x280)^2 + (x336 - x420)^2) + 1
    / sqrt((x57 - x58)^2 + (x197 - x198)^2 + (x337 - x338)^2) + 1 / sqrt((x57
    - x59)^2 + (x197 - x199)^2 + (x337 - x339)^2) + 1 / sqrt((x57 - x60)^2 + (
    x197 - x200)^2 + (x337 - x340)^2) + 1 / sqrt((x57 - x61)^2 + (x197 - x201)^
    2 + (x337 - x341)^2) + 1 / sqrt((x57 - x62)^2 + (x197 - x202)^2 + (x337 -
    x342)^2) + 1 / sqrt((x57 - x63)^2 + (x197 - x203)^2 + (x337 - x343)^2) + 1
    / sqrt((x57 - x64)^2 + (x197 - x204)^2 + (x337 - x344)^2) + 1 / sqrt((x57
    - x65)^2 + (x197 - x205)^2 + (x337 - x345)^2) + 1 / sqrt((x57 - x66)^2 + (
    x197 - x206)^2 + (x337 - x346)^2) + 1 / sqrt((x57 - x67)^2 + (x197 - x207)^
    2 + (x337 - x347)^2) + 1 / sqrt((x57 - x68)^2 + (x197 - x208)^2 + (x337 -
    x348)^2) + 1 / sqrt((x57 - x69)^2 + (x197 - x209)^2 + (x337 - x349)^2) + 1
    / sqrt((x57 - x70)^2 + (x197 - x210)^2 + (x337 - x350)^2) + 1 / sqrt((x57
    - x71)^2 + (x197 - x211)^2 + (x337 - x351)^2) + 1 / sqrt((x57 - x72)^2 + (
    x197 - x212)^2 + (x337 - x352)^2) + 1 / sqrt((x57 - x73)^2 + (x197 - x213)^
    2 + (x337 - x353)^2) + 1 / sqrt((x57 - x74)^2 + (x197 - x214)^2 + (x337 -
    x354)^2) + 1 / sqrt((x57 - x75)^2 + (x197 - x215)^2 + (x337 - x355)^2) + 1
    / sqrt((x57 - x76)^2 + (x197 - x216)^2 + (x337 - x356)^2) + 1 / sqrt((x57
    - x77)^2 + (x197 - x217)^2 + (x337 - x357)^2) + 1 / sqrt((x57 - x78)^2 + (
    x197 - x218)^2 + (x337 - x358)^2) + 1 / sqrt((x57 - x79)^2 + (x197 - x219)^
    2 + (x337 - x359)^2) + 1 / sqrt((x57 - x80)^2 + (x197 - x220)^2 + (x337 -
    x360)^2) + 1 / sqrt((x57 - x81)^2 + (x197 - x221)^2 + (x337 - x361)^2) + 1
    / sqrt((x57 - x82)^2 + (x197 - x222)^2 + (x337 - x362)^2) + 1 / sqrt((x57
    - x83)^2 + (x197 - x223)^2 + (x337 - x363)^2) + 1 / sqrt((x57 - x84)^2 + (
    x197 - x224)^2 + (x337 - x364)^2) + 1 / sqrt((x57 - x85)^2 + (x197 - x225)^
    2 + (x337 - x365)^2) + 1 / sqrt((x57 - x86)^2 + (x197 - x226)^2 + (x337 -
    x366)^2) + 1 / sqrt((x57 - x87)^2 + (x197 - x227)^2 + (x337 - x367)^2) + 1
    / sqrt((x57 - x88)^2 + (x197 - x228)^2 + (x337 - x368)^2) + 1 / sqrt((x57
    - x89)^2 + (x197 - x229)^2 + (x337 - x369)^2) + 1 / sqrt((x57 - x90)^2 + (
    x197 - x230)^2 + (x337 - x370)^2) + 1 / sqrt((x57 - x91)^2 + (x197 - x231)^
    2 + (x337 - x371)^2) + 1 / sqrt((x57 - x92)^2 + (x197 - x232)^2 + (x337 -
    x372)^2) + 1 / sqrt((x57 - x93)^2 + (x197 - x233)^2 + (x337 - x373)^2) + 1
    / sqrt((x57 - x94)^2 + (x197 - x234)^2 + (x337 - x374)^2) + 1 / sqrt((x57
    - x95)^2 + (x197 - x235)^2 + (x337 - x375)^2) + 1 / sqrt((x57 - x96)^2 + (
    x197 - x236)^2 + (x337 - x376)^2) + 1 / sqrt((x57 - x97)^2 + (x197 - x237)^
    2 + (x337 - x377)^2) + 1 / sqrt((x57 - x98)^2 + (x197 - x238)^2 + (x337 -
    x378)^2) + 1 / sqrt((x57 - x99)^2 + (x197 - x239)^2 + (x337 - x379)^2) + 1
    / sqrt((x57 - x100)^2 + (x197 - x240)^2 + (x337 - x380)^2) + 1 / sqrt((x57
    - x101)^2 + (x197 - x241)^2 + (x337 - x381)^2) + 1 / sqrt((x57 - x102)^2
    + (x197 - x242)^2 + (x337 - x382)^2) + 1 / sqrt((x57 - x103)^2 + (x197 -
    x243)^2 + (x337 - x383)^2) + 1 / sqrt((x57 - x104)^2 + (x197 - x244)^2 + (
    x337 - x384)^2) + 1 / sqrt((x57 - x105)^2 + (x197 - x245)^2 + (x337 - x385)
    ^2) + 1 / sqrt((x57 - x106)^2 + (x197 - x246)^2 + (x337 - x386)^2) + 1 /
    sqrt((x57 - x107)^2 + (x197 - x247)^2 + (x337 - x387)^2) + 1 / sqrt((x57 -
    x108)^2 + (x197 - x248)^2 + (x337 - x388)^2) + 1 / sqrt((x57 - x109)^2 + (
    x197 - x249)^2 + (x337 - x389)^2) + 1 / sqrt((x57 - x110)^2 + (x197 - x250)
    ^2 + (x337 - x390)^2) + 1 / sqrt((x57 - x111)^2 + (x197 - x251)^2 + (x337
    - x391)^2) + 1 / sqrt((x57 - x112)^2 + (x197 - x252)^2 + (x337 - x392)^2)
    + 1 / sqrt((x57 - x113)^2 + (x197 - x253)^2 + (x337 - x393)^2) + 1 / sqrt(
    (x57 - x114)^2 + (x197 - x254)^2 + (x337 - x394)^2) + 1 / sqrt((x57 - x115)
    ^2 + (x197 - x255)^2 + (x337 - x395)^2) + 1 / sqrt((x57 - x116)^2 + (x197
    - x256)^2 + (x337 - x396)^2) + 1 / sqrt((x57 - x117)^2 + (x197 - x257)^2
    + (x337 - x397)^2) + 1 / sqrt((x57 - x118)^2 + (x197 - x258)^2 + (x337 -
    x398)^2) + 1 / sqrt((x57 - x119)^2 + (x197 - x259)^2 + (x337 - x399)^2) + 1
    / sqrt((x57 - x120)^2 + (x197 - x260)^2 + (x337 - x400)^2) + 1 / sqrt((x57
    - x121)^2 + (x197 - x261)^2 + (x337 - x401)^2) + 1 / sqrt((x57 - x122)^2
    + (x197 - x262)^2 + (x337 - x402)^2) + 1 / sqrt((x57 - x123)^2 + (x197 -
    x263)^2 + (x337 - x403)^2) + 1 / sqrt((x57 - x124)^2 + (x197 - x264)^2 + (
    x337 - x404)^2) + 1 / sqrt((x57 - x125)^2 + (x197 - x265)^2 + (x337 - x405)
    ^2) + 1 / sqrt((x57 - x126)^2 + (x197 - x266)^2 + (x337 - x406)^2) + 1 /
    sqrt((x57 - x127)^2 + (x197 - x267)^2 + (x337 - x407)^2) + 1 / sqrt((x57 -
    x128)^2 + (x197 - x268)^2 + (x337 - x408)^2) + 1 / sqrt((x57 - x129)^2 + (
    x197 - x269)^2 + (x337 - x409)^2) + 1 / sqrt((x57 - x130)^2 + (x197 - x270)
    ^2 + (x337 - x410)^2) + 1 / sqrt((x57 - x131)^2 + (x197 - x271)^2 + (x337
    - x411)^2) + 1 / sqrt((x57 - x132)^2 + (x197 - x272)^2 + (x337 - x412)^2)
    + 1 / sqrt((x57 - x133)^2 + (x197 - x273)^2 + (x337 - x413)^2) + 1 / sqrt(
    (x57 - x134)^2 + (x197 - x274)^2 + (x337 - x414)^2) + 1 / sqrt((x57 - x135)
    ^2 + (x197 - x275)^2 + (x337 - x415)^2) + 1 / sqrt((x57 - x136)^2 + (x197
    - x276)^2 + (x337 - x416)^2) + 1 / sqrt((x57 - x137)^2 + (x197 - x277)^2
    + (x337 - x417)^2) + 1 / sqrt((x57 - x138)^2 + (x197 - x278)^2 + (x337 -
    x418)^2) + 1 / sqrt((x57 - x139)^2 + (x197 - x279)^2 + (x337 - x419)^2) + 1
    / sqrt((x57 - x140)^2 + (x197 - x280)^2 + (x337 - x420)^2) + 1 / sqrt((x58
    - x59)^2 + (x198 - x199)^2 + (x338 - x339)^2) + 1 / sqrt((x58 - x60)^2 + (
    x198 - x200)^2 + (x338 - x340)^2) + 1 / sqrt((x58 - x61)^2 + (x198 - x201)^
    2 + (x338 - x341)^2) + 1 / sqrt((x58 - x62)^2 + (x198 - x202)^2 + (x338 -
    x342)^2) + 1 / sqrt((x58 - x63)^2 + (x198 - x203)^2 + (x338 - x343)^2) + 1
    / sqrt((x58 - x64)^2 + (x198 - x204)^2 + (x338 - x344)^2) + 1 / sqrt((x58
    - x65)^2 + (x198 - x205)^2 + (x338 - x345)^2) + 1 / sqrt((x58 - x66)^2 + (
    x198 - x206)^2 + (x338 - x346)^2) + 1 / sqrt((x58 - x67)^2 + (x198 - x207)^
    2 + (x338 - x347)^2) + 1 / sqrt((x58 - x68)^2 + (x198 - x208)^2 + (x338 -
    x348)^2) + 1 / sqrt((x58 - x69)^2 + (x198 - x209)^2 + (x338 - x349)^2) + 1
    / sqrt((x58 - x70)^2 + (x198 - x210)^2 + (x338 - x350)^2) + 1 / sqrt((x58
    - x71)^2 + (x198 - x211)^2 + (x338 - x351)^2) + 1 / sqrt((x58 - x72)^2 + (
    x198 - x212)^2 + (x338 - x352)^2) + 1 / sqrt((x58 - x73)^2 + (x198 - x213)^
    2 + (x338 - x353)^2) + 1 / sqrt((x58 - x74)^2 + (x198 - x214)^2 + (x338 -
    x354)^2) + 1 / sqrt((x58 - x75)^2 + (x198 - x215)^2 + (x338 - x355)^2) + 1
    / sqrt((x58 - x76)^2 + (x198 - x216)^2 + (x338 - x356)^2) + 1 / sqrt((x58
    - x77)^2 + (x198 - x217)^2 + (x338 - x357)^2) + 1 / sqrt((x58 - x78)^2 + (
    x198 - x218)^2 + (x338 - x358)^2) + 1 / sqrt((x58 - x79)^2 + (x198 - x219)^
    2 + (x338 - x359)^2) + 1 / sqrt((x58 - x80)^2 + (x198 - x220)^2 + (x338 -
    x360)^2) + 1 / sqrt((x58 - x81)^2 + (x198 - x221)^2 + (x338 - x361)^2) + 1
    / sqrt((x58 - x82)^2 + (x198 - x222)^2 + (x338 - x362)^2) + 1 / sqrt((x58
    - x83)^2 + (x198 - x223)^2 + (x338 - x363)^2) + 1 / sqrt((x58 - x84)^2 + (
    x198 - x224)^2 + (x338 - x364)^2) + 1 / sqrt((x58 - x85)^2 + (x198 - x225)^
    2 + (x338 - x365)^2) + 1 / sqrt((x58 - x86)^2 + (x198 - x226)^2 + (x338 -
    x366)^2) + 1 / sqrt((x58 - x87)^2 + (x198 - x227)^2 + (x338 - x367)^2) + 1
    / sqrt((x58 - x88)^2 + (x198 - x228)^2 + (x338 - x368)^2) + 1 / sqrt((x58
    - x89)^2 + (x198 - x229)^2 + (x338 - x369)^2) + 1 / sqrt((x58 - x90)^2 + (
    x198 - x230)^2 + (x338 - x370)^2) + 1 / sqrt((x58 - x91)^2 + (x198 - x231)^
    2 + (x338 - x371)^2) + 1 / sqrt((x58 - x92)^2 + (x198 - x232)^2 + (x338 -
    x372)^2) + 1 / sqrt((x58 - x93)^2 + (x198 - x233)^2 + (x338 - x373)^2) + 1
    / sqrt((x58 - x94)^2 + (x198 - x234)^2 + (x338 - x374)^2) + 1 / sqrt((x58
    - x95)^2 + (x198 - x235)^2 + (x338 - x375)^2) + 1 / sqrt((x58 - x96)^2 + (
    x198 - x236)^2 + (x338 - x376)^2) + 1 / sqrt((x58 - x97)^2 + (x198 - x237)^
    2 + (x338 - x377)^2) + 1 / sqrt((x58 - x98)^2 + (x198 - x238)^2 + (x338 -
    x378)^2) + 1 / sqrt((x58 - x99)^2 + (x198 - x239)^2 + (x338 - x379)^2) + 1
    / sqrt((x58 - x100)^2 + (x198 - x240)^2 + (x338 - x380)^2) + 1 / sqrt((x58
    - x101)^2 + (x198 - x241)^2 + (x338 - x381)^2) + 1 / sqrt((x58 - x102)^2
    + (x198 - x242)^2 + (x338 - x382)^2) + 1 / sqrt((x58 - x103)^2 + (x198 -
    x243)^2 + (x338 - x383)^2) + 1 / sqrt((x58 - x104)^2 + (x198 - x244)^2 + (
    x338 - x384)^2) + 1 / sqrt((x58 - x105)^2 + (x198 - x245)^2 + (x338 - x385)
    ^2) + 1 / sqrt((x58 - x106)^2 + (x198 - x246)^2 + (x338 - x386)^2) + 1 /
    sqrt((x58 - x107)^2 + (x198 - x247)^2 + (x338 - x387)^2) + 1 / sqrt((x58 -
    x108)^2 + (x198 - x248)^2 + (x338 - x388)^2) + 1 / sqrt((x58 - x109)^2 + (
    x198 - x249)^2 + (x338 - x389)^2) + 1 / sqrt((x58 - x110)^2 + (x198 - x250)
    ^2 + (x338 - x390)^2) + 1 / sqrt((x58 - x111)^2 + (x198 - x251)^2 + (x338
    - x391)^2) + 1 / sqrt((x58 - x112)^2 + (x198 - x252)^2 + (x338 - x392)^2)
    + 1 / sqrt((x58 - x113)^2 + (x198 - x253)^2 + (x338 - x393)^2) + 1 / sqrt(
    (x58 - x114)^2 + (x198 - x254)^2 + (x338 - x394)^2) + 1 / sqrt((x58 - x115)
    ^2 + (x198 - x255)^2 + (x338 - x395)^2) + 1 / sqrt((x58 - x116)^2 + (x198
    - x256)^2 + (x338 - x396)^2) + 1 / sqrt((x58 - x117)^2 + (x198 - x257)^2
    + (x338 - x397)^2) + 1 / sqrt((x58 - x118)^2 + (x198 - x258)^2 + (x338 -
    x398)^2) + 1 / sqrt((x58 - x119)^2 + (x198 - x259)^2 + (x338 - x399)^2) + 1
    / sqrt((x58 - x120)^2 + (x198 - x260)^2 + (x338 - x400)^2) + 1 / sqrt((x58
    - x121)^2 + (x198 - x261)^2 + (x338 - x401)^2) + 1 / sqrt((x58 - x122)^2
    + (x198 - x262)^2 + (x338 - x402)^2) + 1 / sqrt((x58 - x123)^2 + (x198 -
    x263)^2 + (x338 - x403)^2) + 1 / sqrt((x58 - x124)^2 + (x198 - x264)^2 + (
    x338 - x404)^2) + 1 / sqrt((x58 - x125)^2 + (x198 - x265)^2 + (x338 - x405)
    ^2) + 1 / sqrt((x58 - x126)^2 + (x198 - x266)^2 + (x338 - x406)^2) + 1 /
    sqrt((x58 - x127)^2 + (x198 - x267)^2 + (x338 - x407)^2) + 1 / sqrt((x58 -
    x128)^2 + (x198 - x268)^2 + (x338 - x408)^2) + 1 / sqrt((x58 - x129)^2 + (
    x198 - x269)^2 + (x338 - x409)^2) + 1 / sqrt((x58 - x130)^2 + (x198 - x270)
    ^2 + (x338 - x410)^2) + 1 / sqrt((x58 - x131)^2 + (x198 - x271)^2 + (x338
    - x411)^2) + 1 / sqrt((x58 - x132)^2 + (x198 - x272)^2 + (x338 - x412)^2)
    + 1 / sqrt((x58 - x133)^2 + (x198 - x273)^2 + (x338 - x413)^2) + 1 / sqrt(
    (x58 - x134)^2 + (x198 - x274)^2 + (x338 - x414)^2) + 1 / sqrt((x58 - x135)
    ^2 + (x198 - x275)^2 + (x338 - x415)^2) + 1 / sqrt((x58 - x136)^2 + (x198
    - x276)^2 + (x338 - x416)^2) + 1 / sqrt((x58 - x137)^2 + (x198 - x277)^2
    + (x338 - x417)^2) + 1 / sqrt((x58 - x138)^2 + (x198 - x278)^2 + (x338 -
    x418)^2) + 1 / sqrt((x58 - x139)^2 + (x198 - x279)^2 + (x338 - x419)^2) + 1
    / sqrt((x58 - x140)^2 + (x198 - x280)^2 + (x338 - x420)^2) + 1 / sqrt((x59
    - x60)^2 + (x199 - x200)^2 + (x339 - x340)^2) + 1 / sqrt((x59 - x61)^2 + (
    x199 - x201)^2 + (x339 - x341)^2) + 1 / sqrt((x59 - x62)^2 + (x199 - x202)^
    2 + (x339 - x342)^2) + 1 / sqrt((x59 - x63)^2 + (x199 - x203)^2 + (x339 -
    x343)^2) + 1 / sqrt((x59 - x64)^2 + (x199 - x204)^2 + (x339 - x344)^2) + 1
    / sqrt((x59 - x65)^2 + (x199 - x205)^2 + (x339 - x345)^2) + 1 / sqrt((x59
    - x66)^2 + (x199 - x206)^2 + (x339 - x346)^2) + 1 / sqrt((x59 - x67)^2 + (
    x199 - x207)^2 + (x339 - x347)^2) + 1 / sqrt((x59 - x68)^2 + (x199 - x208)^
    2 + (x339 - x348)^2) + 1 / sqrt((x59 - x69)^2 + (x199 - x209)^2 + (x339 -
    x349)^2) + 1 / sqrt((x59 - x70)^2 + (x199 - x210)^2 + (x339 - x350)^2) + 1
    / sqrt((x59 - x71)^2 + (x199 - x211)^2 + (x339 - x351)^2) + 1 / sqrt((x59
    - x72)^2 + (x199 - x212)^2 + (x339 - x352)^2) + 1 / sqrt((x59 - x73)^2 + (
    x199 - x213)^2 + (x339 - x353)^2) + 1 / sqrt((x59 - x74)^2 + (x199 - x214)^
    2 + (x339 - x354)^2) + 1 / sqrt((x59 - x75)^2 + (x199 - x215)^2 + (x339 -
    x355)^2) + 1 / sqrt((x59 - x76)^2 + (x199 - x216)^2 + (x339 - x356)^2) + 1
    / sqrt((x59 - x77)^2 + (x199 - x217)^2 + (x339 - x357)^2) + 1 / sqrt((x59
    - x78)^2 + (x199 - x218)^2 + (x339 - x358)^2) + 1 / sqrt((x59 - x79)^2 + (
    x199 - x219)^2 + (x339 - x359)^2) + 1 / sqrt((x59 - x80)^2 + (x199 - x220)^
    2 + (x339 - x360)^2) + 1 / sqrt((x59 - x81)^2 + (x199 - x221)^2 + (x339 -
    x361)^2) + 1 / sqrt((x59 - x82)^2 + (x199 - x222)^2 + (x339 - x362)^2) + 1
    / sqrt((x59 - x83)^2 + (x199 - x223)^2 + (x339 - x363)^2) + 1 / sqrt((x59
    - x84)^2 + (x199 - x224)^2 + (x339 - x364)^2) + 1 / sqrt((x59 - x85)^2 + (
    x199 - x225)^2 + (x339 - x365)^2) + 1 / sqrt((x59 - x86)^2 + (x199 - x226)^
    2 + (x339 - x366)^2) + 1 / sqrt((x59 - x87)^2 + (x199 - x227)^2 + (x339 -
    x367)^2) + 1 / sqrt((x59 - x88)^2 + (x199 - x228)^2 + (x339 - x368)^2) + 1
    / sqrt((x59 - x89)^2 + (x199 - x229)^2 + (x339 - x369)^2) + 1 / sqrt((x59
    - x90)^2 + (x199 - x230)^2 + (x339 - x370)^2) + 1 / sqrt((x59 - x91)^2 + (
    x199 - x231)^2 + (x339 - x371)^2) + 1 / sqrt((x59 - x92)^2 + (x199 - x232)^
    2 + (x339 - x372)^2) + 1 / sqrt((x59 - x93)^2 + (x199 - x233)^2 + (x339 -
    x373)^2) + 1 / sqrt((x59 - x94)^2 + (x199 - x234)^2 + (x339 - x374)^2) + 1
    / sqrt((x59 - x95)^2 + (x199 - x235)^2 + (x339 - x375)^2) + 1 / sqrt((x59
    - x96)^2 + (x199 - x236)^2 + (x339 - x376)^2) + 1 / sqrt((x59 - x97)^2 + (
    x199 - x237)^2 + (x339 - x377)^2) + 1 / sqrt((x59 - x98)^2 + (x199 - x238)^
    2 + (x339 - x378)^2) + 1 / sqrt((x59 - x99)^2 + (x199 - x239)^2 + (x339 -
    x379)^2) + 1 / sqrt((x59 - x100)^2 + (x199 - x240)^2 + (x339 - x380)^2) + 1
    / sqrt((x59 - x101)^2 + (x199 - x241)^2 + (x339 - x381)^2) + 1 / sqrt((x59
    - x102)^2 + (x199 - x242)^2 + (x339 - x382)^2) + 1 / sqrt((x59 - x103)^2
    + (x199 - x243)^2 + (x339 - x383)^2) + 1 / sqrt((x59 - x104)^2 + (x199 -
    x244)^2 + (x339 - x384)^2) + 1 / sqrt((x59 - x105)^2 + (x199 - x245)^2 + (
    x339 - x385)^2) + 1 / sqrt((x59 - x106)^2 + (x199 - x246)^2 + (x339 - x386)
    ^2) + 1 / sqrt((x59 - x107)^2 + (x199 - x247)^2 + (x339 - x387)^2) + 1 /
    sqrt((x59 - x108)^2 + (x199 - x248)^2 + (x339 - x388)^2) + 1 / sqrt((x59 -
    x109)^2 + (x199 - x249)^2 + (x339 - x389)^2) + 1 / sqrt((x59 - x110)^2 + (
    x199 - x250)^2 + (x339 - x390)^2) + 1 / sqrt((x59 - x111)^2 + (x199 - x251)
    ^2 + (x339 - x391)^2) + 1 / sqrt((x59 - x112)^2 + (x199 - x252)^2 + (x339
    - x392)^2) + 1 / sqrt((x59 - x113)^2 + (x199 - x253)^2 + (x339 - x393)^2)
    + 1 / sqrt((x59 - x114)^2 + (x199 - x254)^2 + (x339 - x394)^2) + 1 / sqrt(
    (x59 - x115)^2 + (x199 - x255)^2 + (x339 - x395)^2) + 1 / sqrt((x59 - x116)
    ^2 + (x199 - x256)^2 + (x339 - x396)^2) + 1 / sqrt((x59 - x117)^2 + (x199
    - x257)^2 + (x339 - x397)^2) + 1 / sqrt((x59 - x118)^2 + (x199 - x258)^2
    + (x339 - x398)^2) + 1 / sqrt((x59 - x119)^2 + (x199 - x259)^2 + (x339 -
    x399)^2) + 1 / sqrt((x59 - x120)^2 + (x199 - x260)^2 + (x339 - x400)^2) + 1
    / sqrt((x59 - x121)^2 + (x199 - x261)^2 + (x339 - x401)^2) + 1 / sqrt((x59
    - x122)^2 + (x199 - x262)^2 + (x339 - x402)^2) + 1 / sqrt((x59 - x123)^2
    + (x199 - x263)^2 + (x339 - x403)^2) + 1 / sqrt((x59 - x124)^2 + (x199 -
    x264)^2 + (x339 - x404)^2) + 1 / sqrt((x59 - x125)^2 + (x199 - x265)^2 + (
    x339 - x405)^2) + 1 / sqrt((x59 - x126)^2 + (x199 - x266)^2 + (x339 - x406)
    ^2) + 1 / sqrt((x59 - x127)^2 + (x199 - x267)^2 + (x339 - x407)^2) + 1 /
    sqrt((x59 - x128)^2 + (x199 - x268)^2 + (x339 - x408)^2) + 1 / sqrt((x59 -
    x129)^2 + (x199 - x269)^2 + (x339 - x409)^2) + 1 / sqrt((x59 - x130)^2 + (
    x199 - x270)^2 + (x339 - x410)^2) + 1 / sqrt((x59 - x131)^2 + (x199 - x271)
    ^2 + (x339 - x411)^2) + 1 / sqrt((x59 - x132)^2 + (x199 - x272)^2 + (x339
    - x412)^2) + 1 / sqrt((x59 - x133)^2 + (x199 - x273)^2 + (x339 - x413)^2)
    + 1 / sqrt((x59 - x134)^2 + (x199 - x274)^2 + (x339 - x414)^2) + 1 / sqrt(
    (x59 - x135)^2 + (x199 - x275)^2 + (x339 - x415)^2) + 1 / sqrt((x59 - x136)
    ^2 + (x199 - x276)^2 + (x339 - x416)^2) + 1 / sqrt((x59 - x137)^2 + (x199
    - x277)^2 + (x339 - x417)^2) + 1 / sqrt((x59 - x138)^2 + (x199 - x278)^2
    + (x339 - x418)^2) + 1 / sqrt((x59 - x139)^2 + (x199 - x279)^2 + (x339 -
    x419)^2) + 1 / sqrt((x59 - x140)^2 + (x199 - x280)^2 + (x339 - x420)^2) + 1
    / sqrt((x60 - x61)^2 + (x200 - x201)^2 + (x340 - x341)^2) + 1 / sqrt((x60
    - x62)^2 + (x200 - x202)^2 + (x340 - x342)^2) + 1 / sqrt((x60 - x63)^2 + (
    x200 - x203)^2 + (x340 - x343)^2) + 1 / sqrt((x60 - x64)^2 + (x200 - x204)^
    2 + (x340 - x344)^2) + 1 / sqrt((x60 - x65)^2 + (x200 - x205)^2 + (x340 -
    x345)^2) + 1 / sqrt((x60 - x66)^2 + (x200 - x206)^2 + (x340 - x346)^2) + 1
    / sqrt((x60 - x67)^2 + (x200 - x207)^2 + (x340 - x347)^2) + 1 / sqrt((x60
    - x68)^2 + (x200 - x208)^2 + (x340 - x348)^2) + 1 / sqrt((x60 - x69)^2 + (
    x200 - x209)^2 + (x340 - x349)^2) + 1 / sqrt((x60 - x70)^2 + (x200 - x210)^
    2 + (x340 - x350)^2) + 1 / sqrt((x60 - x71)^2 + (x200 - x211)^2 + (x340 -
    x351)^2) + 1 / sqrt((x60 - x72)^2 + (x200 - x212)^2 + (x340 - x352)^2) + 1
    / sqrt((x60 - x73)^2 + (x200 - x213)^2 + (x340 - x353)^2) + 1 / sqrt((x60
    - x74)^2 + (x200 - x214)^2 + (x340 - x354)^2) + 1 / sqrt((x60 - x75)^2 + (
    x200 - x215)^2 + (x340 - x355)^2) + 1 / sqrt((x60 - x76)^2 + (x200 - x216)^
    2 + (x340 - x356)^2) + 1 / sqrt((x60 - x77)^2 + (x200 - x217)^2 + (x340 -
    x357)^2) + 1 / sqrt((x60 - x78)^2 + (x200 - x218)^2 + (x340 - x358)^2) + 1
    / sqrt((x60 - x79)^2 + (x200 - x219)^2 + (x340 - x359)^2) + 1 / sqrt((x60
    - x80)^2 + (x200 - x220)^2 + (x340 - x360)^2) + 1 / sqrt((x60 - x81)^2 + (
    x200 - x221)^2 + (x340 - x361)^2) + 1 / sqrt((x60 - x82)^2 + (x200 - x222)^
    2 + (x340 - x362)^2) + 1 / sqrt((x60 - x83)^2 + (x200 - x223)^2 + (x340 -
    x363)^2) + 1 / sqrt((x60 - x84)^2 + (x200 - x224)^2 + (x340 - x364)^2) + 1
    / sqrt((x60 - x85)^2 + (x200 - x225)^2 + (x340 - x365)^2) + 1 / sqrt((x60
    - x86)^2 + (x200 - x226)^2 + (x340 - x366)^2) + 1 / sqrt((x60 - x87)^2 + (
    x200 - x227)^2 + (x340 - x367)^2) + 1 / sqrt((x60 - x88)^2 + (x200 - x228)^
    2 + (x340 - x368)^2) + 1 / sqrt((x60 - x89)^2 + (x200 - x229)^2 + (x340 -
    x369)^2) + 1 / sqrt((x60 - x90)^2 + (x200 - x230)^2 + (x340 - x370)^2) + 1
    / sqrt((x60 - x91)^2 + (x200 - x231)^2 + (x340 - x371)^2) + 1 / sqrt((x60
    - x92)^2 + (x200 - x232)^2 + (x340 - x372)^2) + 1 / sqrt((x60 - x93)^2 + (
    x200 - x233)^2 + (x340 - x373)^2) + 1 / sqrt((x60 - x94)^2 + (x200 - x234)^
    2 + (x340 - x374)^2) + 1 / sqrt((x60 - x95)^2 + (x200 - x235)^2 + (x340 -
    x375)^2) + 1 / sqrt((x60 - x96)^2 + (x200 - x236)^2 + (x340 - x376)^2) + 1
    / sqrt((x60 - x97)^2 + (x200 - x237)^2 + (x340 - x377)^2) + 1 / sqrt((x60
    - x98)^2 + (x200 - x238)^2 + (x340 - x378)^2) + 1 / sqrt((x60 - x99)^2 + (
    x200 - x239)^2 + (x340 - x379)^2) + 1 / sqrt((x60 - x100)^2 + (x200 - x240)
    ^2 + (x340 - x380)^2) + 1 / sqrt((x60 - x101)^2 + (x200 - x241)^2 + (x340
    - x381)^2) + 1 / sqrt((x60 - x102)^2 + (x200 - x242)^2 + (x340 - x382)^2)
    + 1 / sqrt((x60 - x103)^2 + (x200 - x243)^2 + (x340 - x383)^2) + 1 / sqrt(
    (x60 - x104)^2 + (x200 - x244)^2 + (x340 - x384)^2) + 1 / sqrt((x60 - x105)
    ^2 + (x200 - x245)^2 + (x340 - x385)^2) + 1 / sqrt((x60 - x106)^2 + (x200
    - x246)^2 + (x340 - x386)^2) + 1 / sqrt((x60 - x107)^2 + (x200 - x247)^2
    + (x340 - x387)^2) + 1 / sqrt((x60 - x108)^2 + (x200 - x248)^2 + (x340 -
    x388)^2) + 1 / sqrt((x60 - x109)^2 + (x200 - x249)^2 + (x340 - x389)^2) + 1
    / sqrt((x60 - x110)^2 + (x200 - x250)^2 + (x340 - x390)^2) + 1 / sqrt((x60
    - x111)^2 + (x200 - x251)^2 + (x340 - x391)^2) + 1 / sqrt((x60 - x112)^2
    + (x200 - x252)^2 + (x340 - x392)^2) + 1 / sqrt((x60 - x113)^2 + (x200 -
    x253)^2 + (x340 - x393)^2) + 1 / sqrt((x60 - x114)^2 + (x200 - x254)^2 + (
    x340 - x394)^2) + 1 / sqrt((x60 - x115)^2 + (x200 - x255)^2 + (x340 - x395)
    ^2) + 1 / sqrt((x60 - x116)^2 + (x200 - x256)^2 + (x340 - x396)^2) + 1 /
    sqrt((x60 - x117)^2 + (x200 - x257)^2 + (x340 - x397)^2) + 1 / sqrt((x60 -
    x118)^2 + (x200 - x258)^2 + (x340 - x398)^2) + 1 / sqrt((x60 - x119)^2 + (
    x200 - x259)^2 + (x340 - x399)^2) + 1 / sqrt((x60 - x120)^2 + (x200 - x260)
    ^2 + (x340 - x400)^2) + 1 / sqrt((x60 - x121)^2 + (x200 - x261)^2 + (x340
    - x401)^2) + 1 / sqrt((x60 - x122)^2 + (x200 - x262)^2 + (x340 - x402)^2)
    + 1 / sqrt((x60 - x123)^2 + (x200 - x263)^2 + (x340 - x403)^2) + 1 / sqrt(
    (x60 - x124)^2 + (x200 - x264)^2 + (x340 - x404)^2) + 1 / sqrt((x60 - x125)
    ^2 + (x200 - x265)^2 + (x340 - x405)^2) + 1 / sqrt((x60 - x126)^2 + (x200
    - x266)^2 + (x340 - x406)^2) + 1 / sqrt((x60 - x127)^2 + (x200 - x267)^2
    + (x340 - x407)^2) + 1 / sqrt((x60 - x128)^2 + (x200 - x268)^2 + (x340 -
    x408)^2) + 1 / sqrt((x60 - x129)^2 + (x200 - x269)^2 + (x340 - x409)^2) + 1
    / sqrt((x60 - x130)^2 + (x200 - x270)^2 + (x340 - x410)^2) + 1 / sqrt((x60
    - x131)^2 + (x200 - x271)^2 + (x340 - x411)^2) + 1 / sqrt((x60 - x132)^2
    + (x200 - x272)^2 + (x340 - x412)^2) + 1 / sqrt((x60 - x133)^2 + (x200 -
    x273)^2 + (x340 - x413)^2) + 1 / sqrt((x60 - x134)^2 + (x200 - x274)^2 + (
    x340 - x414)^2) + 1 / sqrt((x60 - x135)^2 + (x200 - x275)^2 + (x340 - x415)
    ^2) + 1 / sqrt((x60 - x136)^2 + (x200 - x276)^2 + (x340 - x416)^2) + 1 /
    sqrt((x60 - x137)^2 + (x200 - x277)^2 + (x340 - x417)^2) + 1 / sqrt((x60 -
    x138)^2 + (x200 - x278)^2 + (x340 - x418)^2) + 1 / sqrt((x60 - x139)^2 + (
    x200 - x279)^2 + (x340 - x419)^2) + 1 / sqrt((x60 - x140)^2 + (x200 - x280)
    ^2 + (x340 - x420)^2) + 1 / sqrt((x61 - x62)^2 + (x201 - x202)^2 + (x341 -
    x342)^2) + 1 / sqrt((x61 - x63)^2 + (x201 - x203)^2 + (x341 - x343)^2) + 1
    / sqrt((x61 - x64)^2 + (x201 - x204)^2 + (x341 - x344)^2) + 1 / sqrt((x61
    - x65)^2 + (x201 - x205)^2 + (x341 - x345)^2) + 1 / sqrt((x61 - x66)^2 + (
    x201 - x206)^2 + (x341 - x346)^2) + 1 / sqrt((x61 - x67)^2 + (x201 - x207)^
    2 + (x341 - x347)^2) + 1 / sqrt((x61 - x68)^2 + (x201 - x208)^2 + (x341 -
    x348)^2) + 1 / sqrt((x61 - x69)^2 + (x201 - x209)^2 + (x341 - x349)^2) + 1
    / sqrt((x61 - x70)^2 + (x201 - x210)^2 + (x341 - x350)^2) + 1 / sqrt((x61
    - x71)^2 + (x201 - x211)^2 + (x341 - x351)^2) + 1 / sqrt((x61 - x72)^2 + (
    x201 - x212)^2 + (x341 - x352)^2) + 1 / sqrt((x61 - x73)^2 + (x201 - x213)^
    2 + (x341 - x353)^2) + 1 / sqrt((x61 - x74)^2 + (x201 - x214)^2 + (x341 -
    x354)^2) + 1 / sqrt((x61 - x75)^2 + (x201 - x215)^2 + (x341 - x355)^2) + 1
    / sqrt((x61 - x76)^2 + (x201 - x216)^2 + (x341 - x356)^2) + 1 / sqrt((x61
    - x77)^2 + (x201 - x217)^2 + (x341 - x357)^2) + 1 / sqrt((x61 - x78)^2 + (
    x201 - x218)^2 + (x341 - x358)^2) + 1 / sqrt((x61 - x79)^2 + (x201 - x219)^
    2 + (x341 - x359)^2) + 1 / sqrt((x61 - x80)^2 + (x201 - x220)^2 + (x341 -
    x360)^2) + 1 / sqrt((x61 - x81)^2 + (x201 - x221)^2 + (x341 - x361)^2) + 1
    / sqrt((x61 - x82)^2 + (x201 - x222)^2 + (x341 - x362)^2) + 1 / sqrt((x61
    - x83)^2 + (x201 - x223)^2 + (x341 - x363)^2) + 1 / sqrt((x61 - x84)^2 + (
    x201 - x224)^2 + (x341 - x364)^2) + 1 / sqrt((x61 - x85)^2 + (x201 - x225)^
    2 + (x341 - x365)^2) + 1 / sqrt((x61 - x86)^2 + (x201 - x226)^2 + (x341 -
    x366)^2) + 1 / sqrt((x61 - x87)^2 + (x201 - x227)^2 + (x341 - x367)^2) + 1
    / sqrt((x61 - x88)^2 + (x201 - x228)^2 + (x341 - x368)^2) + 1 / sqrt((x61
    - x89)^2 + (x201 - x229)^2 + (x341 - x369)^2) + 1 / sqrt((x61 - x90)^2 + (
    x201 - x230)^2 + (x341 - x370)^2) + 1 / sqrt((x61 - x91)^2 + (x201 - x231)^
    2 + (x341 - x371)^2) + 1 / sqrt((x61 - x92)^2 + (x201 - x232)^2 + (x341 -
    x372)^2) + 1 / sqrt((x61 - x93)^2 + (x201 - x233)^2 + (x341 - x373)^2) + 1
    / sqrt((x61 - x94)^2 + (x201 - x234)^2 + (x341 - x374)^2) + 1 / sqrt((x61
    - x95)^2 + (x201 - x235)^2 + (x341 - x375)^2) + 1 / sqrt((x61 - x96)^2 + (
    x201 - x236)^2 + (x341 - x376)^2) + 1 / sqrt((x61 - x97)^2 + (x201 - x237)^
    2 + (x341 - x377)^2) + 1 / sqrt((x61 - x98)^2 + (x201 - x238)^2 + (x341 -
    x378)^2) + 1 / sqrt((x61 - x99)^2 + (x201 - x239)^2 + (x341 - x379)^2) + 1
    / sqrt((x61 - x100)^2 + (x201 - x240)^2 + (x341 - x380)^2) + 1 / sqrt((x61
    - x101)^2 + (x201 - x241)^2 + (x341 - x381)^2) + 1 / sqrt((x61 - x102)^2
    + (x201 - x242)^2 + (x341 - x382)^2) + 1 / sqrt((x61 - x103)^2 + (x201 -
    x243)^2 + (x341 - x383)^2) + 1 / sqrt((x61 - x104)^2 + (x201 - x244)^2 + (
    x341 - x384)^2) + 1 / sqrt((x61 - x105)^2 + (x201 - x245)^2 + (x341 - x385)
    ^2) + 1 / sqrt((x61 - x106)^2 + (x201 - x246)^2 + (x341 - x386)^2) + 1 /
    sqrt((x61 - x107)^2 + (x201 - x247)^2 + (x341 - x387)^2) + 1 / sqrt((x61 -
    x108)^2 + (x201 - x248)^2 + (x341 - x388)^2) + 1 / sqrt((x61 - x109)^2 + (
    x201 - x249)^2 + (x341 - x389)^2) + 1 / sqrt((x61 - x110)^2 + (x201 - x250)
    ^2 + (x341 - x390)^2) + 1 / sqrt((x61 - x111)^2 + (x201 - x251)^2 + (x341
    - x391)^2) + 1 / sqrt((x61 - x112)^2 + (x201 - x252)^2 + (x341 - x392)^2)
    + 1 / sqrt((x61 - x113)^2 + (x201 - x253)^2 + (x341 - x393)^2) + 1 / sqrt(
    (x61 - x114)^2 + (x201 - x254)^2 + (x341 - x394)^2) + 1 / sqrt((x61 - x115)
    ^2 + (x201 - x255)^2 + (x341 - x395)^2) + 1 / sqrt((x61 - x116)^2 + (x201
    - x256)^2 + (x341 - x396)^2) + 1 / sqrt((x61 - x117)^2 + (x201 - x257)^2
    + (x341 - x397)^2) + 1 / sqrt((x61 - x118)^2 + (x201 - x258)^2 + (x341 -
    x398)^2) + 1 / sqrt((x61 - x119)^2 + (x201 - x259)^2 + (x341 - x399)^2) + 1
    / sqrt((x61 - x120)^2 + (x201 - x260)^2 + (x341 - x400)^2) + 1 / sqrt((x61
    - x121)^2 + (x201 - x261)^2 + (x341 - x401)^2) + 1 / sqrt((x61 - x122)^2
    + (x201 - x262)^2 + (x341 - x402)^2) + 1 / sqrt((x61 - x123)^2 + (x201 -
    x263)^2 + (x341 - x403)^2) + 1 / sqrt((x61 - x124)^2 + (x201 - x264)^2 + (
    x341 - x404)^2) + 1 / sqrt((x61 - x125)^2 + (x201 - x265)^2 + (x341 - x405)
    ^2) + 1 / sqrt((x61 - x126)^2 + (x201 - x266)^2 + (x341 - x406)^2) + 1 /
    sqrt((x61 - x127)^2 + (x201 - x267)^2 + (x341 - x407)^2) + 1 / sqrt((x61 -
    x128)^2 + (x201 - x268)^2 + (x341 - x408)^2) + 1 / sqrt((x61 - x129)^2 + (
    x201 - x269)^2 + (x341 - x409)^2) + 1 / sqrt((x61 - x130)^2 + (x201 - x270)
    ^2 + (x341 - x410)^2) + 1 / sqrt((x61 - x131)^2 + (x201 - x271)^2 + (x341
    - x411)^2) + 1 / sqrt((x61 - x132)^2 + (x201 - x272)^2 + (x341 - x412)^2)
    + 1 / sqrt((x61 - x133)^2 + (x201 - x273)^2 + (x341 - x413)^2) + 1 / sqrt(
    (x61 - x134)^2 + (x201 - x274)^2 + (x341 - x414)^2) + 1 / sqrt((x61 - x135)
    ^2 + (x201 - x275)^2 + (x341 - x415)^2) + 1 / sqrt((x61 - x136)^2 + (x201
    - x276)^2 + (x341 - x416)^2) + 1 / sqrt((x61 - x137)^2 + (x201 - x277)^2
    + (x341 - x417)^2) + 1 / sqrt((x61 - x138)^2 + (x201 - x278)^2 + (x341 -
    x418)^2) + 1 / sqrt((x61 - x139)^2 + (x201 - x279)^2 + (x341 - x419)^2) + 1
    / sqrt((x61 - x140)^2 + (x201 - x280)^2 + (x341 - x420)^2) + 1 / sqrt((x62
    - x63)^2 + (x202 - x203)^2 + (x342 - x343)^2) + 1 / sqrt((x62 - x64)^2 + (
    x202 - x204)^2 + (x342 - x344)^2) + 1 / sqrt((x62 - x65)^2 + (x202 - x205)^
    2 + (x342 - x345)^2) + 1 / sqrt((x62 - x66)^2 + (x202 - x206)^2 + (x342 -
    x346)^2) + 1 / sqrt((x62 - x67)^2 + (x202 - x207)^2 + (x342 - x347)^2) + 1
    / sqrt((x62 - x68)^2 + (x202 - x208)^2 + (x342 - x348)^2) + 1 / sqrt((x62
    - x69)^2 + (x202 - x209)^2 + (x342 - x349)^2) + 1 / sqrt((x62 - x70)^2 + (
    x202 - x210)^2 + (x342 - x350)^2) + 1 / sqrt((x62 - x71)^2 + (x202 - x211)^
    2 + (x342 - x351)^2) + 1 / sqrt((x62 - x72)^2 + (x202 - x212)^2 + (x342 -
    x352)^2) + 1 / sqrt((x62 - x73)^2 + (x202 - x213)^2 + (x342 - x353)^2) + 1
    / sqrt((x62 - x74)^2 + (x202 - x214)^2 + (x342 - x354)^2) + 1 / sqrt((x62
    - x75)^2 + (x202 - x215)^2 + (x342 - x355)^2) + 1 / sqrt((x62 - x76)^2 + (
    x202 - x216)^2 + (x342 - x356)^2) + 1 / sqrt((x62 - x77)^2 + (x202 - x217)^
    2 + (x342 - x357)^2) + 1 / sqrt((x62 - x78)^2 + (x202 - x218)^2 + (x342 -
    x358)^2) + 1 / sqrt((x62 - x79)^2 + (x202 - x219)^2 + (x342 - x359)^2) + 1
    / sqrt((x62 - x80)^2 + (x202 - x220)^2 + (x342 - x360)^2) + 1 / sqrt((x62
    - x81)^2 + (x202 - x221)^2 + (x342 - x361)^2) + 1 / sqrt((x62 - x82)^2 + (
    x202 - x222)^2 + (x342 - x362)^2) + 1 / sqrt((x62 - x83)^2 + (x202 - x223)^
    2 + (x342 - x363)^2) + 1 / sqrt((x62 - x84)^2 + (x202 - x224)^2 + (x342 -
    x364)^2) + 1 / sqrt((x62 - x85)^2 + (x202 - x225)^2 + (x342 - x365)^2) + 1
    / sqrt((x62 - x86)^2 + (x202 - x226)^2 + (x342 - x366)^2) + 1 / sqrt((x62
    - x87)^2 + (x202 - x227)^2 + (x342 - x367)^2) + 1 / sqrt((x62 - x88)^2 + (
    x202 - x228)^2 + (x342 - x368)^2) + 1 / sqrt((x62 - x89)^2 + (x202 - x229)^
    2 + (x342 - x369)^2) + 1 / sqrt((x62 - x90)^2 + (x202 - x230)^2 + (x342 -
    x370)^2) + 1 / sqrt((x62 - x91)^2 + (x202 - x231)^2 + (x342 - x371)^2) + 1
    / sqrt((x62 - x92)^2 + (x202 - x232)^2 + (x342 - x372)^2) + 1 / sqrt((x62
    - x93)^2 + (x202 - x233)^2 + (x342 - x373)^2) + 1 / sqrt((x62 - x94)^2 + (
    x202 - x234)^2 + (x342 - x374)^2) + 1 / sqrt((x62 - x95)^2 + (x202 - x235)^
    2 + (x342 - x375)^2) + 1 / sqrt((x62 - x96)^2 + (x202 - x236)^2 + (x342 -
    x376)^2) + 1 / sqrt((x62 - x97)^2 + (x202 - x237)^2 + (x342 - x377)^2) + 1
    / sqrt((x62 - x98)^2 + (x202 - x238)^2 + (x342 - x378)^2) + 1 / sqrt((x62
    - x99)^2 + (x202 - x239)^2 + (x342 - x379)^2) + 1 / sqrt((x62 - x100)^2 +
    (x202 - x240)^2 + (x342 - x380)^2) + 1 / sqrt((x62 - x101)^2 + (x202 - x241)
    ^2 + (x342 - x381)^2) + 1 / sqrt((x62 - x102)^2 + (x202 - x242)^2 + (x342
    - x382)^2) + 1 / sqrt((x62 - x103)^2 + (x202 - x243)^2 + (x342 - x383)^2)
    + 1 / sqrt((x62 - x104)^2 + (x202 - x244)^2 + (x342 - x384)^2) + 1 / sqrt(
    (x62 - x105)^2 + (x202 - x245)^2 + (x342 - x385)^2) + 1 / sqrt((x62 - x106)
    ^2 + (x202 - x246)^2 + (x342 - x386)^2) + 1 / sqrt((x62 - x107)^2 + (x202
    - x247)^2 + (x342 - x387)^2) + 1 / sqrt((x62 - x108)^2 + (x202 - x248)^2
    + (x342 - x388)^2) + 1 / sqrt((x62 - x109)^2 + (x202 - x249)^2 + (x342 -
    x389)^2) + 1 / sqrt((x62 - x110)^2 + (x202 - x250)^2 + (x342 - x390)^2) + 1
    / sqrt((x62 - x111)^2 + (x202 - x251)^2 + (x342 - x391)^2) + 1 / sqrt((x62
    - x112)^2 + (x202 - x252)^2 + (x342 - x392)^2) + 1 / sqrt((x62 - x113)^2
    + (x202 - x253)^2 + (x342 - x393)^2) + 1 / sqrt((x62 - x114)^2 + (x202 -
    x254)^2 + (x342 - x394)^2) + 1 / sqrt((x62 - x115)^2 + (x202 - x255)^2 + (
    x342 - x395)^2) + 1 / sqrt((x62 - x116)^2 + (x202 - x256)^2 + (x342 - x396)
    ^2) + 1 / sqrt((x62 - x117)^2 + (x202 - x257)^2 + (x342 - x397)^2) + 1 /
    sqrt((x62 - x118)^2 + (x202 - x258)^2 + (x342 - x398)^2) + 1 / sqrt((x62 -
    x119)^2 + (x202 - x259)^2 + (x342 - x399)^2) + 1 / sqrt((x62 - x120)^2 + (
    x202 - x260)^2 + (x342 - x400)^2) + 1 / sqrt((x62 - x121)^2 + (x202 - x261)
    ^2 + (x342 - x401)^2) + 1 / sqrt((x62 - x122)^2 + (x202 - x262)^2 + (x342
    - x402)^2) + 1 / sqrt((x62 - x123)^2 + (x202 - x263)^2 + (x342 - x403)^2)
    + 1 / sqrt((x62 - x124)^2 + (x202 - x264)^2 + (x342 - x404)^2) + 1 / sqrt(
    (x62 - x125)^2 + (x202 - x265)^2 + (x342 - x405)^2) + 1 / sqrt((x62 - x126)
    ^2 + (x202 - x266)^2 + (x342 - x406)^2) + 1 / sqrt((x62 - x127)^2 + (x202
    - x267)^2 + (x342 - x407)^2) + 1 / sqrt((x62 - x128)^2 + (x202 - x268)^2
    + (x342 - x408)^2) + 1 / sqrt((x62 - x129)^2 + (x202 - x269)^2 + (x342 -
    x409)^2) + 1 / sqrt((x62 - x130)^2 + (x202 - x270)^2 + (x342 - x410)^2) + 1
    / sqrt((x62 - x131)^2 + (x202 - x271)^2 + (x342 - x411)^2) + 1 / sqrt((x62
    - x132)^2 + (x202 - x272)^2 + (x342 - x412)^2) + 1 / sqrt((x62 - x133)^2
    + (x202 - x273)^2 + (x342 - x413)^2) + 1 / sqrt((x62 - x134)^2 + (x202 -
    x274)^2 + (x342 - x414)^2) + 1 / sqrt((x62 - x135)^2 + (x202 - x275)^2 + (
    x342 - x415)^2) + 1 / sqrt((x62 - x136)^2 + (x202 - x276)^2 + (x342 - x416)
    ^2) + 1 / sqrt((x62 - x137)^2 + (x202 - x277)^2 + (x342 - x417)^2) + 1 /
    sqrt((x62 - x138)^2 + (x202 - x278)^2 + (x342 - x418)^2) + 1 / sqrt((x62 -
    x139)^2 + (x202 - x279)^2 + (x342 - x419)^2) + 1 / sqrt((x62 - x140)^2 + (
    x202 - x280)^2 + (x342 - x420)^2) + 1 / sqrt((x63 - x64)^2 + (x203 - x204)^
    2 + (x343 - x344)^2) + 1 / sqrt((x63 - x65)^2 + (x203 - x205)^2 + (x343 -
    x345)^2) + 1 / sqrt((x63 - x66)^2 + (x203 - x206)^2 + (x343 - x346)^2) + 1
    / sqrt((x63 - x67)^2 + (x203 - x207)^2 + (x343 - x347)^2) + 1 / sqrt((x63
    - x68)^2 + (x203 - x208)^2 + (x343 - x348)^2) + 1 / sqrt((x63 - x69)^2 + (
    x203 - x209)^2 + (x343 - x349)^2) + 1 / sqrt((x63 - x70)^2 + (x203 - x210)^
    2 + (x343 - x350)^2) + 1 / sqrt((x63 - x71)^2 + (x203 - x211)^2 + (x343 -
    x351)^2) + 1 / sqrt((x63 - x72)^2 + (x203 - x212)^2 + (x343 - x352)^2) + 1
    / sqrt((x63 - x73)^2 + (x203 - x213)^2 + (x343 - x353)^2) + 1 / sqrt((x63
    - x74)^2 + (x203 - x214)^2 + (x343 - x354)^2) + 1 / sqrt((x63 - x75)^2 + (
    x203 - x215)^2 + (x343 - x355)^2) + 1 / sqrt((x63 - x76)^2 + (x203 - x216)^
    2 + (x343 - x356)^2) + 1 / sqrt((x63 - x77)^2 + (x203 - x217)^2 + (x343 -
    x357)^2) + 1 / sqrt((x63 - x78)^2 + (x203 - x218)^2 + (x343 - x358)^2) + 1
    / sqrt((x63 - x79)^2 + (x203 - x219)^2 + (x343 - x359)^2) + 1 / sqrt((x63
    - x80)^2 + (x203 - x220)^2 + (x343 - x360)^2) + 1 / sqrt((x63 - x81)^2 + (
    x203 - x221)^2 + (x343 - x361)^2) + 1 / sqrt((x63 - x82)^2 + (x203 - x222)^
    2 + (x343 - x362)^2) + 1 / sqrt((x63 - x83)^2 + (x203 - x223)^2 + (x343 -
    x363)^2) + 1 / sqrt((x63 - x84)^2 + (x203 - x224)^2 + (x343 - x364)^2) + 1
    / sqrt((x63 - x85)^2 + (x203 - x225)^2 + (x343 - x365)^2) + 1 / sqrt((x63
    - x86)^2 + (x203 - x226)^2 + (x343 - x366)^2) + 1 / sqrt((x63 - x87)^2 + (
    x203 - x227)^2 + (x343 - x367)^2) + 1 / sqrt((x63 - x88)^2 + (x203 - x228)^
    2 + (x343 - x368)^2) + 1 / sqrt((x63 - x89)^2 + (x203 - x229)^2 + (x343 -
    x369)^2) + 1 / sqrt((x63 - x90)^2 + (x203 - x230)^2 + (x343 - x370)^2) + 1
    / sqrt((x63 - x91)^2 + (x203 - x231)^2 + (x343 - x371)^2) + 1 / sqrt((x63
    - x92)^2 + (x203 - x232)^2 + (x343 - x372)^2) + 1 / sqrt((x63 - x93)^2 + (
    x203 - x233)^2 + (x343 - x373)^2) + 1 / sqrt((x63 - x94)^2 + (x203 - x234)^
    2 + (x343 - x374)^2) + 1 / sqrt((x63 - x95)^2 + (x203 - x235)^2 + (x343 -
    x375)^2) + 1 / sqrt((x63 - x96)^2 + (x203 - x236)^2 + (x343 - x376)^2) + 1
    / sqrt((x63 - x97)^2 + (x203 - x237)^2 + (x343 - x377)^2) + 1 / sqrt((x63
    - x98)^2 + (x203 - x238)^2 + (x343 - x378)^2) + 1 / sqrt((x63 - x99)^2 + (
    x203 - x239)^2 + (x343 - x379)^2) + 1 / sqrt((x63 - x100)^2 + (x203 - x240)
    ^2 + (x343 - x380)^2) + 1 / sqrt((x63 - x101)^2 + (x203 - x241)^2 + (x343
    - x381)^2) + 1 / sqrt((x63 - x102)^2 + (x203 - x242)^2 + (x343 - x382)^2)
    + 1 / sqrt((x63 - x103)^2 + (x203 - x243)^2 + (x343 - x383)^2) + 1 / sqrt(
    (x63 - x104)^2 + (x203 - x244)^2 + (x343 - x384)^2) + 1 / sqrt((x63 - x105)
    ^2 + (x203 - x245)^2 + (x343 - x385)^2) + 1 / sqrt((x63 - x106)^2 + (x203
    - x246)^2 + (x343 - x386)^2) + 1 / sqrt((x63 - x107)^2 + (x203 - x247)^2
    + (x343 - x387)^2) + 1 / sqrt((x63 - x108)^2 + (x203 - x248)^2 + (x343 -
    x388)^2) + 1 / sqrt((x63 - x109)^2 + (x203 - x249)^2 + (x343 - x389)^2) + 1
    / sqrt((x63 - x110)^2 + (x203 - x250)^2 + (x343 - x390)^2) + 1 / sqrt((x63
    - x111)^2 + (x203 - x251)^2 + (x343 - x391)^2) + 1 / sqrt((x63 - x112)^2
    + (x203 - x252)^2 + (x343 - x392)^2) + 1 / sqrt((x63 - x113)^2 + (x203 -
    x253)^2 + (x343 - x393)^2) + 1 / sqrt((x63 - x114)^2 + (x203 - x254)^2 + (
    x343 - x394)^2) + 1 / sqrt((x63 - x115)^2 + (x203 - x255)^2 + (x343 - x395)
    ^2) + 1 / sqrt((x63 - x116)^2 + (x203 - x256)^2 + (x343 - x396)^2) + 1 /
    sqrt((x63 - x117)^2 + (x203 - x257)^2 + (x343 - x397)^2) + 1 / sqrt((x63 -
    x118)^2 + (x203 - x258)^2 + (x343 - x398)^2) + 1 / sqrt((x63 - x119)^2 + (
    x203 - x259)^2 + (x343 - x399)^2) + 1 / sqrt((x63 - x120)^2 + (x203 - x260)
    ^2 + (x343 - x400)^2) + 1 / sqrt((x63 - x121)^2 + (x203 - x261)^2 + (x343
    - x401)^2) + 1 / sqrt((x63 - x122)^2 + (x203 - x262)^2 + (x343 - x402)^2)
    + 1 / sqrt((x63 - x123)^2 + (x203 - x263)^2 + (x343 - x403)^2) + 1 / sqrt(
    (x63 - x124)^2 + (x203 - x264)^2 + (x343 - x404)^2) + 1 / sqrt((x63 - x125)
    ^2 + (x203 - x265)^2 + (x343 - x405)^2) + 1 / sqrt((x63 - x126)^2 + (x203
    - x266)^2 + (x343 - x406)^2) + 1 / sqrt((x63 - x127)^2 + (x203 - x267)^2
    + (x343 - x407)^2) + 1 / sqrt((x63 - x128)^2 + (x203 - x268)^2 + (x343 -
    x408)^2) + 1 / sqrt((x63 - x129)^2 + (x203 - x269)^2 + (x343 - x409)^2) + 1
    / sqrt((x63 - x130)^2 + (x203 - x270)^2 + (x343 - x410)^2) + 1 / sqrt((x63
    - x131)^2 + (x203 - x271)^2 + (x343 - x411)^2) + 1 / sqrt((x63 - x132)^2
    + (x203 - x272)^2 + (x343 - x412)^2) + 1 / sqrt((x63 - x133)^2 + (x203 -
    x273)^2 + (x343 - x413)^2) + 1 / sqrt((x63 - x134)^2 + (x203 - x274)^2 + (
    x343 - x414)^2) + 1 / sqrt((x63 - x135)^2 + (x203 - x275)^2 + (x343 - x415)
    ^2) + 1 / sqrt((x63 - x136)^2 + (x203 - x276)^2 + (x343 - x416)^2) + 1 /
    sqrt((x63 - x137)^2 + (x203 - x277)^2 + (x343 - x417)^2) + 1 / sqrt((x63 -
    x138)^2 + (x203 - x278)^2 + (x343 - x418)^2) + 1 / sqrt((x63 - x139)^2 + (
    x203 - x279)^2 + (x343 - x419)^2) + 1 / sqrt((x63 - x140)^2 + (x203 - x280)
    ^2 + (x343 - x420)^2) + 1 / sqrt((x64 - x65)^2 + (x204 - x205)^2 + (x344 -
    x345)^2) + 1 / sqrt((x64 - x66)^2 + (x204 - x206)^2 + (x344 - x346)^2) + 1
    / sqrt((x64 - x67)^2 + (x204 - x207)^2 + (x344 - x347)^2) + 1 / sqrt((x64
    - x68)^2 + (x204 - x208)^2 + (x344 - x348)^2) + 1 / sqrt((x64 - x69)^2 + (
    x204 - x209)^2 + (x344 - x349)^2) + 1 / sqrt((x64 - x70)^2 + (x204 - x210)^
    2 + (x344 - x350)^2) + 1 / sqrt((x64 - x71)^2 + (x204 - x211)^2 + (x344 -
    x351)^2) + 1 / sqrt((x64 - x72)^2 + (x204 - x212)^2 + (x344 - x352)^2) + 1
    / sqrt((x64 - x73)^2 + (x204 - x213)^2 + (x344 - x353)^2) + 1 / sqrt((x64
    - x74)^2 + (x204 - x214)^2 + (x344 - x354)^2) + 1 / sqrt((x64 - x75)^2 + (
    x204 - x215)^2 + (x344 - x355)^2) + 1 / sqrt((x64 - x76)^2 + (x204 - x216)^
    2 + (x344 - x356)^2) + 1 / sqrt((x64 - x77)^2 + (x204 - x217)^2 + (x344 -
    x357)^2) + 1 / sqrt((x64 - x78)^2 + (x204 - x218)^2 + (x344 - x358)^2) + 1
    / sqrt((x64 - x79)^2 + (x204 - x219)^2 + (x344 - x359)^2) + 1 / sqrt((x64
    - x80)^2 + (x204 - x220)^2 + (x344 - x360)^2) + 1 / sqrt((x64 - x81)^2 + (
    x204 - x221)^2 + (x344 - x361)^2) + 1 / sqrt((x64 - x82)^2 + (x204 - x222)^
    2 + (x344 - x362)^2) + 1 / sqrt((x64 - x83)^2 + (x204 - x223)^2 + (x344 -
    x363)^2) + 1 / sqrt((x64 - x84)^2 + (x204 - x224)^2 + (x344 - x364)^2) + 1
    / sqrt((x64 - x85)^2 + (x204 - x225)^2 + (x344 - x365)^2) + 1 / sqrt((x64
    - x86)^2 + (x204 - x226)^2 + (x344 - x366)^2) + 1 / sqrt((x64 - x87)^2 + (
    x204 - x227)^2 + (x344 - x367)^2) + 1 / sqrt((x64 - x88)^2 + (x204 - x228)^
    2 + (x344 - x368)^2) + 1 / sqrt((x64 - x89)^2 + (x204 - x229)^2 + (x344 -
    x369)^2) + 1 / sqrt((x64 - x90)^2 + (x204 - x230)^2 + (x344 - x370)^2) + 1
    / sqrt((x64 - x91)^2 + (x204 - x231)^2 + (x344 - x371)^2) + 1 / sqrt((x64
    - x92)^2 + (x204 - x232)^2 + (x344 - x372)^2) + 1 / sqrt((x64 - x93)^2 + (
    x204 - x233)^2 + (x344 - x373)^2) + 1 / sqrt((x64 - x94)^2 + (x204 - x234)^
    2 + (x344 - x374)^2) + 1 / sqrt((x64 - x95)^2 + (x204 - x235)^2 + (x344 -
    x375)^2) + 1 / sqrt((x64 - x96)^2 + (x204 - x236)^2 + (x344 - x376)^2) + 1
    / sqrt((x64 - x97)^2 + (x204 - x237)^2 + (x344 - x377)^2) + 1 / sqrt((x64
    - x98)^2 + (x204 - x238)^2 + (x344 - x378)^2) + 1 / sqrt((x64 - x99)^2 + (
    x204 - x239)^2 + (x344 - x379)^2) + 1 / sqrt((x64 - x100)^2 + (x204 - x240)
    ^2 + (x344 - x380)^2) + 1 / sqrt((x64 - x101)^2 + (x204 - x241)^2 + (x344
    - x381)^2) + 1 / sqrt((x64 - x102)^2 + (x204 - x242)^2 + (x344 - x382)^2)
    + 1 / sqrt((x64 - x103)^2 + (x204 - x243)^2 + (x344 - x383)^2) + 1 / sqrt(
    (x64 - x104)^2 + (x204 - x244)^2 + (x344 - x384)^2) + 1 / sqrt((x64 - x105)
    ^2 + (x204 - x245)^2 + (x344 - x385)^2) + 1 / sqrt((x64 - x106)^2 + (x204
    - x246)^2 + (x344 - x386)^2) + 1 / sqrt((x64 - x107)^2 + (x204 - x247)^2
    + (x344 - x387)^2) + 1 / sqrt((x64 - x108)^2 + (x204 - x248)^2 + (x344 -
    x388)^2) + 1 / sqrt((x64 - x109)^2 + (x204 - x249)^2 + (x344 - x389)^2) + 1
    / sqrt((x64 - x110)^2 + (x204 - x250)^2 + (x344 - x390)^2) + 1 / sqrt((x64
    - x111)^2 + (x204 - x251)^2 + (x344 - x391)^2) + 1 / sqrt((x64 - x112)^2
    + (x204 - x252)^2 + (x344 - x392)^2) + 1 / sqrt((x64 - x113)^2 + (x204 -
    x253)^2 + (x344 - x393)^2) + 1 / sqrt((x64 - x114)^2 + (x204 - x254)^2 + (
    x344 - x394)^2) + 1 / sqrt((x64 - x115)^2 + (x204 - x255)^2 + (x344 - x395)
    ^2) + 1 / sqrt((x64 - x116)^2 + (x204 - x256)^2 + (x344 - x396)^2) + 1 /
    sqrt((x64 - x117)^2 + (x204 - x257)^2 + (x344 - x397)^2) + 1 / sqrt((x64 -
    x118)^2 + (x204 - x258)^2 + (x344 - x398)^2) + 1 / sqrt((x64 - x119)^2 + (
    x204 - x259)^2 + (x344 - x399)^2) + 1 / sqrt((x64 - x120)^2 + (x204 - x260)
    ^2 + (x344 - x400)^2) + 1 / sqrt((x64 - x121)^2 + (x204 - x261)^2 + (x344
    - x401)^2) + 1 / sqrt((x64 - x122)^2 + (x204 - x262)^2 + (x344 - x402)^2)
    + 1 / sqrt((x64 - x123)^2 + (x204 - x263)^2 + (x344 - x403)^2) + 1 / sqrt(
    (x64 - x124)^2 + (x204 - x264)^2 + (x344 - x404)^2) + 1 / sqrt((x64 - x125)
    ^2 + (x204 - x265)^2 + (x344 - x405)^2) + 1 / sqrt((x64 - x126)^2 + (x204
    - x266)^2 + (x344 - x406)^2) + 1 / sqrt((x64 - x127)^2 + (x204 - x267)^2
    + (x344 - x407)^2) + 1 / sqrt((x64 - x128)^2 + (x204 - x268)^2 + (x344 -
    x408)^2) + 1 / sqrt((x64 - x129)^2 + (x204 - x269)^2 + (x344 - x409)^2) + 1
    / sqrt((x64 - x130)^2 + (x204 - x270)^2 + (x344 - x410)^2) + 1 / sqrt((x64
    - x131)^2 + (x204 - x271)^2 + (x344 - x411)^2) + 1 / sqrt((x64 - x132)^2
    + (x204 - x272)^2 + (x344 - x412)^2) + 1 / sqrt((x64 - x133)^2 + (x204 -
    x273)^2 + (x344 - x413)^2) + 1 / sqrt((x64 - x134)^2 + (x204 - x274)^2 + (
    x344 - x414)^2) + 1 / sqrt((x64 - x135)^2 + (x204 - x275)^2 + (x344 - x415)
    ^2) + 1 / sqrt((x64 - x136)^2 + (x204 - x276)^2 + (x344 - x416)^2) + 1 /
    sqrt((x64 - x137)^2 + (x204 - x277)^2 + (x344 - x417)^2) + 1 / sqrt((x64 -
    x138)^2 + (x204 - x278)^2 + (x344 - x418)^2) + 1 / sqrt((x64 - x139)^2 + (
    x204 - x279)^2 + (x344 - x419)^2) + 1 / sqrt((x64 - x140)^2 + (x204 - x280)
    ^2 + (x344 - x420)^2) + 1 / sqrt((x65 - x66)^2 + (x205 - x206)^2 + (x345 -
    x346)^2) + 1 / sqrt((x65 - x67)^2 + (x205 - x207)^2 + (x345 - x347)^2) + 1
    / sqrt((x65 - x68)^2 + (x205 - x208)^2 + (x345 - x348)^2) + 1 / sqrt((x65
    - x69)^2 + (x205 - x209)^2 + (x345 - x349)^2) + 1 / sqrt((x65 - x70)^2 + (
    x205 - x210)^2 + (x345 - x350)^2) + 1 / sqrt((x65 - x71)^2 + (x205 - x211)^
    2 + (x345 - x351)^2) + 1 / sqrt((x65 - x72)^2 + (x205 - x212)^2 + (x345 -
    x352)^2) + 1 / sqrt((x65 - x73)^2 + (x205 - x213)^2 + (x345 - x353)^2) + 1
    / sqrt((x65 - x74)^2 + (x205 - x214)^2 + (x345 - x354)^2) + 1 / sqrt((x65
    - x75)^2 + (x205 - x215)^2 + (x345 - x355)^2) + 1 / sqrt((x65 - x76)^2 + (
    x205 - x216)^2 + (x345 - x356)^2) + 1 / sqrt((x65 - x77)^2 + (x205 - x217)^
    2 + (x345 - x357)^2) + 1 / sqrt((x65 - x78)^2 + (x205 - x218)^2 + (x345 -
    x358)^2) + 1 / sqrt((x65 - x79)^2 + (x205 - x219)^2 + (x345 - x359)^2) + 1
    / sqrt((x65 - x80)^2 + (x205 - x220)^2 + (x345 - x360)^2) + 1 / sqrt((x65
    - x81)^2 + (x205 - x221)^2 + (x345 - x361)^2) + 1 / sqrt((x65 - x82)^2 + (
    x205 - x222)^2 + (x345 - x362)^2) + 1 / sqrt((x65 - x83)^2 + (x205 - x223)^
    2 + (x345 - x363)^2) + 1 / sqrt((x65 - x84)^2 + (x205 - x224)^2 + (x345 -
    x364)^2) + 1 / sqrt((x65 - x85)^2 + (x205 - x225)^2 + (x345 - x365)^2) + 1
    / sqrt((x65 - x86)^2 + (x205 - x226)^2 + (x345 - x366)^2) + 1 / sqrt((x65
    - x87)^2 + (x205 - x227)^2 + (x345 - x367)^2) + 1 / sqrt((x65 - x88)^2 + (
    x205 - x228)^2 + (x345 - x368)^2) + 1 / sqrt((x65 - x89)^2 + (x205 - x229)^
    2 + (x345 - x369)^2) + 1 / sqrt((x65 - x90)^2 + (x205 - x230)^2 + (x345 -
    x370)^2) + 1 / sqrt((x65 - x91)^2 + (x205 - x231)^2 + (x345 - x371)^2) + 1
    / sqrt((x65 - x92)^2 + (x205 - x232)^2 + (x345 - x372)^2) + 1 / sqrt((x65
    - x93)^2 + (x205 - x233)^2 + (x345 - x373)^2) + 1 / sqrt((x65 - x94)^2 + (
    x205 - x234)^2 + (x345 - x374)^2) + 1 / sqrt((x65 - x95)^2 + (x205 - x235)^
    2 + (x345 - x375)^2) + 1 / sqrt((x65 - x96)^2 + (x205 - x236)^2 + (x345 -
    x376)^2) + 1 / sqrt((x65 - x97)^2 + (x205 - x237)^2 + (x345 - x377)^2) + 1
    / sqrt((x65 - x98)^2 + (x205 - x238)^2 + (x345 - x378)^2) + 1 / sqrt((x65
    - x99)^2 + (x205 - x239)^2 + (x345 - x379)^2) + 1 / sqrt((x65 - x100)^2 +
    (x205 - x240)^2 + (x345 - x380)^2) + 1 / sqrt((x65 - x101)^2 + (x205 - x241)
    ^2 + (x345 - x381)^2) + 1 / sqrt((x65 - x102)^2 + (x205 - x242)^2 + (x345
    - x382)^2) + 1 / sqrt((x65 - x103)^2 + (x205 - x243)^2 + (x345 - x383)^2)
    + 1 / sqrt((x65 - x104)^2 + (x205 - x244)^2 + (x345 - x384)^2) + 1 / sqrt(
    (x65 - x105)^2 + (x205 - x245)^2 + (x345 - x385)^2) + 1 / sqrt((x65 - x106)
    ^2 + (x205 - x246)^2 + (x345 - x386)^2) + 1 / sqrt((x65 - x107)^2 + (x205
    - x247)^2 + (x345 - x387)^2) + 1 / sqrt((x65 - x108)^2 + (x205 - x248)^2
    + (x345 - x388)^2) + 1 / sqrt((x65 - x109)^2 + (x205 - x249)^2 + (x345 -
    x389)^2) + 1 / sqrt((x65 - x110)^2 + (x205 - x250)^2 + (x345 - x390)^2) + 1
    / sqrt((x65 - x111)^2 + (x205 - x251)^2 + (x345 - x391)^2) + 1 / sqrt((x65
    - x112)^2 + (x205 - x252)^2 + (x345 - x392)^2) + 1 / sqrt((x65 - x113)^2
    + (x205 - x253)^2 + (x345 - x393)^2) + 1 / sqrt((x65 - x114)^2 + (x205 -
    x254)^2 + (x345 - x394)^2) + 1 / sqrt((x65 - x115)^2 + (x205 - x255)^2 + (
    x345 - x395)^2) + 1 / sqrt((x65 - x116)^2 + (x205 - x256)^2 + (x345 - x396)
    ^2) + 1 / sqrt((x65 - x117)^2 + (x205 - x257)^2 + (x345 - x397)^2) + 1 /
    sqrt((x65 - x118)^2 + (x205 - x258)^2 + (x345 - x398)^2) + 1 / sqrt((x65 -
    x119)^2 + (x205 - x259)^2 + (x345 - x399)^2) + 1 / sqrt((x65 - x120)^2 + (
    x205 - x260)^2 + (x345 - x400)^2) + 1 / sqrt((x65 - x121)^2 + (x205 - x261)
    ^2 + (x345 - x401)^2) + 1 / sqrt((x65 - x122)^2 + (x205 - x262)^2 + (x345
    - x402)^2) + 1 / sqrt((x65 - x123)^2 + (x205 - x263)^2 + (x345 - x403)^2)
    + 1 / sqrt((x65 - x124)^2 + (x205 - x264)^2 + (x345 - x404)^2) + 1 / sqrt(
    (x65 - x125)^2 + (x205 - x265)^2 + (x345 - x405)^2) + 1 / sqrt((x65 - x126)
    ^2 + (x205 - x266)^2 + (x345 - x406)^2) + 1 / sqrt((x65 - x127)^2 + (x205
    - x267)^2 + (x345 - x407)^2) + 1 / sqrt((x65 - x128)^2 + (x205 - x268)^2
    + (x345 - x408)^2) + 1 / sqrt((x65 - x129)^2 + (x205 - x269)^2 + (x345 -
    x409)^2) + 1 / sqrt((x65 - x130)^2 + (x205 - x270)^2 + (x345 - x410)^2) + 1
    / sqrt((x65 - x131)^2 + (x205 - x271)^2 + (x345 - x411)^2) + 1 / sqrt((x65
    - x132)^2 + (x205 - x272)^2 + (x345 - x412)^2) + 1 / sqrt((x65 - x133)^2
    + (x205 - x273)^2 + (x345 - x413)^2) + 1 / sqrt((x65 - x134)^2 + (x205 -
    x274)^2 + (x345 - x414)^2) + 1 / sqrt((x65 - x135)^2 + (x205 - x275)^2 + (
    x345 - x415)^2) + 1 / sqrt((x65 - x136)^2 + (x205 - x276)^2 + (x345 - x416)
    ^2) + 1 / sqrt((x65 - x137)^2 + (x205 - x277)^2 + (x345 - x417)^2) + 1 /
    sqrt((x65 - x138)^2 + (x205 - x278)^2 + (x345 - x418)^2) + 1 / sqrt((x65 -
    x139)^2 + (x205 - x279)^2 + (x345 - x419)^2) + 1 / sqrt((x65 - x140)^2 + (
    x205 - x280)^2 + (x345 - x420)^2) + 1 / sqrt((x66 - x67)^2 + (x206 - x207)^
    2 + (x346 - x347)^2) + 1 / sqrt((x66 - x68)^2 + (x206 - x208)^2 + (x346 -
    x348)^2) + 1 / sqrt((x66 - x69)^2 + (x206 - x209)^2 + (x346 - x349)^2) + 1
    / sqrt((x66 - x70)^2 + (x206 - x210)^2 + (x346 - x350)^2) + 1 / sqrt((x66
    - x71)^2 + (x206 - x211)^2 + (x346 - x351)^2) + 1 / sqrt((x66 - x72)^2 + (
    x206 - x212)^2 + (x346 - x352)^2) + 1 / sqrt((x66 - x73)^2 + (x206 - x213)^
    2 + (x346 - x353)^2) + 1 / sqrt((x66 - x74)^2 + (x206 - x214)^2 + (x346 -
    x354)^2) + 1 / sqrt((x66 - x75)^2 + (x206 - x215)^2 + (x346 - x355)^2) + 1
    / sqrt((x66 - x76)^2 + (x206 - x216)^2 + (x346 - x356)^2) + 1 / sqrt((x66
    - x77)^2 + (x206 - x217)^2 + (x346 - x357)^2) + 1 / sqrt((x66 - x78)^2 + (
    x206 - x218)^2 + (x346 - x358)^2) + 1 / sqrt((x66 - x79)^2 + (x206 - x219)^
    2 + (x346 - x359)^2) + 1 / sqrt((x66 - x80)^2 + (x206 - x220)^2 + (x346 -
    x360)^2) + 1 / sqrt((x66 - x81)^2 + (x206 - x221)^2 + (x346 - x361)^2) + 1
    / sqrt((x66 - x82)^2 + (x206 - x222)^2 + (x346 - x362)^2) + 1 / sqrt((x66
    - x83)^2 + (x206 - x223)^2 + (x346 - x363)^2) + 1 / sqrt((x66 - x84)^2 + (
    x206 - x224)^2 + (x346 - x364)^2) + 1 / sqrt((x66 - x85)^2 + (x206 - x225)^
    2 + (x346 - x365)^2) + 1 / sqrt((x66 - x86)^2 + (x206 - x226)^2 + (x346 -
    x366)^2) + 1 / sqrt((x66 - x87)^2 + (x206 - x227)^2 + (x346 - x367)^2) + 1
    / sqrt((x66 - x88)^2 + (x206 - x228)^2 + (x346 - x368)^2) + 1 / sqrt((x66
    - x89)^2 + (x206 - x229)^2 + (x346 - x369)^2) + 1 / sqrt((x66 - x90)^2 + (
    x206 - x230)^2 + (x346 - x370)^2) + 1 / sqrt((x66 - x91)^2 + (x206 - x231)^
    2 + (x346 - x371)^2) + 1 / sqrt((x66 - x92)^2 + (x206 - x232)^2 + (x346 -
    x372)^2) + 1 / sqrt((x66 - x93)^2 + (x206 - x233)^2 + (x346 - x373)^2) + 1
    / sqrt((x66 - x94)^2 + (x206 - x234)^2 + (x346 - x374)^2) + 1 / sqrt((x66
    - x95)^2 + (x206 - x235)^2 + (x346 - x375)^2) + 1 / sqrt((x66 - x96)^2 + (
    x206 - x236)^2 + (x346 - x376)^2) + 1 / sqrt((x66 - x97)^2 + (x206 - x237)^
    2 + (x346 - x377)^2) + 1 / sqrt((x66 - x98)^2 + (x206 - x238)^2 + (x346 -
    x378)^2) + 1 / sqrt((x66 - x99)^2 + (x206 - x239)^2 + (x346 - x379)^2) + 1
    / sqrt((x66 - x100)^2 + (x206 - x240)^2 + (x346 - x380)^2) + 1 / sqrt((x66
    - x101)^2 + (x206 - x241)^2 + (x346 - x381)^2) + 1 / sqrt((x66 - x102)^2
    + (x206 - x242)^2 + (x346 - x382)^2) + 1 / sqrt((x66 - x103)^2 + (x206 -
    x243)^2 + (x346 - x383)^2) + 1 / sqrt((x66 - x104)^2 + (x206 - x244)^2 + (
    x346 - x384)^2) + 1 / sqrt((x66 - x105)^2 + (x206 - x245)^2 + (x346 - x385)
    ^2) + 1 / sqrt((x66 - x106)^2 + (x206 - x246)^2 + (x346 - x386)^2) + 1 /
    sqrt((x66 - x107)^2 + (x206 - x247)^2 + (x346 - x387)^2) + 1 / sqrt((x66 -
    x108)^2 + (x206 - x248)^2 + (x346 - x388)^2) + 1 / sqrt((x66 - x109)^2 + (
    x206 - x249)^2 + (x346 - x389)^2) + 1 / sqrt((x66 - x110)^2 + (x206 - x250)
    ^2 + (x346 - x390)^2) + 1 / sqrt((x66 - x111)^2 + (x206 - x251)^2 + (x346
    - x391)^2) + 1 / sqrt((x66 - x112)^2 + (x206 - x252)^2 + (x346 - x392)^2)
    + 1 / sqrt((x66 - x113)^2 + (x206 - x253)^2 + (x346 - x393)^2) + 1 / sqrt(
    (x66 - x114)^2 + (x206 - x254)^2 + (x346 - x394)^2) + 1 / sqrt((x66 - x115)
    ^2 + (x206 - x255)^2 + (x346 - x395)^2) + 1 / sqrt((x66 - x116)^2 + (x206
    - x256)^2 + (x346 - x396)^2) + 1 / sqrt((x66 - x117)^2 + (x206 - x257)^2
    + (x346 - x397)^2) + 1 / sqrt((x66 - x118)^2 + (x206 - x258)^2 + (x346 -
    x398)^2) + 1 / sqrt((x66 - x119)^2 + (x206 - x259)^2 + (x346 - x399)^2) + 1
    / sqrt((x66 - x120)^2 + (x206 - x260)^2 + (x346 - x400)^2) + 1 / sqrt((x66
    - x121)^2 + (x206 - x261)^2 + (x346 - x401)^2) + 1 / sqrt((x66 - x122)^2
    + (x206 - x262)^2 + (x346 - x402)^2) + 1 / sqrt((x66 - x123)^2 + (x206 -
    x263)^2 + (x346 - x403)^2) + 1 / sqrt((x66 - x124)^2 + (x206 - x264)^2 + (
    x346 - x404)^2) + 1 / sqrt((x66 - x125)^2 + (x206 - x265)^2 + (x346 - x405)
    ^2) + 1 / sqrt((x66 - x126)^2 + (x206 - x266)^2 + (x346 - x406)^2) + 1 /
    sqrt((x66 - x127)^2 + (x206 - x267)^2 + (x346 - x407)^2) + 1 / sqrt((x66 -
    x128)^2 + (x206 - x268)^2 + (x346 - x408)^2) + 1 / sqrt((x66 - x129)^2 + (
    x206 - x269)^2 + (x346 - x409)^2) + 1 / sqrt((x66 - x130)^2 + (x206 - x270)
    ^2 + (x346 - x410)^2) + 1 / sqrt((x66 - x131)^2 + (x206 - x271)^2 + (x346
    - x411)^2) + 1 / sqrt((x66 - x132)^2 + (x206 - x272)^2 + (x346 - x412)^2)
    + 1 / sqrt((x66 - x133)^2 + (x206 - x273)^2 + (x346 - x413)^2) + 1 / sqrt(
    (x66 - x134)^2 + (x206 - x274)^2 + (x346 - x414)^2) + 1 / sqrt((x66 - x135)
    ^2 + (x206 - x275)^2 + (x346 - x415)^2) + 1 / sqrt((x66 - x136)^2 + (x206
    - x276)^2 + (x346 - x416)^2) + 1 / sqrt((x66 - x137)^2 + (x206 - x277)^2
    + (x346 - x417)^2) + 1 / sqrt((x66 - x138)^2 + (x206 - x278)^2 + (x346 -
    x418)^2) + 1 / sqrt((x66 - x139)^2 + (x206 - x279)^2 + (x346 - x419)^2) + 1
    / sqrt((x66 - x140)^2 + (x206 - x280)^2 + (x346 - x420)^2) + 1 / sqrt((x67
    - x68)^2 + (x207 - x208)^2 + (x347 - x348)^2) + 1 / sqrt((x67 - x69)^2 + (
    x207 - x209)^2 + (x347 - x349)^2) + 1 / sqrt((x67 - x70)^2 + (x207 - x210)^
    2 + (x347 - x350)^2) + 1 / sqrt((x67 - x71)^2 + (x207 - x211)^2 + (x347 -
    x351)^2) + 1 / sqrt((x67 - x72)^2 + (x207 - x212)^2 + (x347 - x352)^2) + 1
    / sqrt((x67 - x73)^2 + (x207 - x213)^2 + (x347 - x353)^2) + 1 / sqrt((x67
    - x74)^2 + (x207 - x214)^2 + (x347 - x354)^2) + 1 / sqrt((x67 - x75)^2 + (
    x207 - x215)^2 + (x347 - x355)^2) + 1 / sqrt((x67 - x76)^2 + (x207 - x216)^
    2 + (x347 - x356)^2) + 1 / sqrt((x67 - x77)^2 + (x207 - x217)^2 + (x347 -
    x357)^2) + 1 / sqrt((x67 - x78)^2 + (x207 - x218)^2 + (x347 - x358)^2) + 1
    / sqrt((x67 - x79)^2 + (x207 - x219)^2 + (x347 - x359)^2) + 1 / sqrt((x67
    - x80)^2 + (x207 - x220)^2 + (x347 - x360)^2) + 1 / sqrt((x67 - x81)^2 + (
    x207 - x221)^2 + (x347 - x361)^2) + 1 / sqrt((x67 - x82)^2 + (x207 - x222)^
    2 + (x347 - x362)^2) + 1 / sqrt((x67 - x83)^2 + (x207 - x223)^2 + (x347 -
    x363)^2) + 1 / sqrt((x67 - x84)^2 + (x207 - x224)^2 + (x347 - x364)^2) + 1
    / sqrt((x67 - x85)^2 + (x207 - x225)^2 + (x347 - x365)^2) + 1 / sqrt((x67
    - x86)^2 + (x207 - x226)^2 + (x347 - x366)^2) + 1 / sqrt((x67 - x87)^2 + (
    x207 - x227)^2 + (x347 - x367)^2) + 1 / sqrt((x67 - x88)^2 + (x207 - x228)^
    2 + (x347 - x368)^2) + 1 / sqrt((x67 - x89)^2 + (x207 - x229)^2 + (x347 -
    x369)^2) + 1 / sqrt((x67 - x90)^2 + (x207 - x230)^2 + (x347 - x370)^2) + 1
    / sqrt((x67 - x91)^2 + (x207 - x231)^2 + (x347 - x371)^2) + 1 / sqrt((x67
    - x92)^2 + (x207 - x232)^2 + (x347 - x372)^2) + 1 / sqrt((x67 - x93)^2 + (
    x207 - x233)^2 + (x347 - x373)^2) + 1 / sqrt((x67 - x94)^2 + (x207 - x234)^
    2 + (x347 - x374)^2) + 1 / sqrt((x67 - x95)^2 + (x207 - x235)^2 + (x347 -
    x375)^2) + 1 / sqrt((x67 - x96)^2 + (x207 - x236)^2 + (x347 - x376)^2) + 1
    / sqrt((x67 - x97)^2 + (x207 - x237)^2 + (x347 - x377)^2) + 1 / sqrt((x67
    - x98)^2 + (x207 - x238)^2 + (x347 - x378)^2) + 1 / sqrt((x67 - x99)^2 + (
    x207 - x239)^2 + (x347 - x379)^2) + 1 / sqrt((x67 - x100)^2 + (x207 - x240)
    ^2 + (x347 - x380)^2) + 1 / sqrt((x67 - x101)^2 + (x207 - x241)^2 + (x347
    - x381)^2) + 1 / sqrt((x67 - x102)^2 + (x207 - x242)^2 + (x347 - x382)^2)
    + 1 / sqrt((x67 - x103)^2 + (x207 - x243)^2 + (x347 - x383)^2) + 1 / sqrt(
    (x67 - x104)^2 + (x207 - x244)^2 + (x347 - x384)^2) + 1 / sqrt((x67 - x105)
    ^2 + (x207 - x245)^2 + (x347 - x385)^2) + 1 / sqrt((x67 - x106)^2 + (x207
    - x246)^2 + (x347 - x386)^2) + 1 / sqrt((x67 - x107)^2 + (x207 - x247)^2
    + (x347 - x387)^2) + 1 / sqrt((x67 - x108)^2 + (x207 - x248)^2 + (x347 -
    x388)^2) + 1 / sqrt((x67 - x109)^2 + (x207 - x249)^2 + (x347 - x389)^2) + 1
    / sqrt((x67 - x110)^2 + (x207 - x250)^2 + (x347 - x390)^2) + 1 / sqrt((x67
    - x111)^2 + (x207 - x251)^2 + (x347 - x391)^2) + 1 / sqrt((x67 - x112)^2
    + (x207 - x252)^2 + (x347 - x392)^2) + 1 / sqrt((x67 - x113)^2 + (x207 -
    x253)^2 + (x347 - x393)^2) + 1 / sqrt((x67 - x114)^2 + (x207 - x254)^2 + (
    x347 - x394)^2) + 1 / sqrt((x67 - x115)^2 + (x207 - x255)^2 + (x347 - x395)
    ^2) + 1 / sqrt((x67 - x116)^2 + (x207 - x256)^2 + (x347 - x396)^2) + 1 /
    sqrt((x67 - x117)^2 + (x207 - x257)^2 + (x347 - x397)^2) + 1 / sqrt((x67 -
    x118)^2 + (x207 - x258)^2 + (x347 - x398)^2) + 1 / sqrt((x67 - x119)^2 + (
    x207 - x259)^2 + (x347 - x399)^2) + 1 / sqrt((x67 - x120)^2 + (x207 - x260)
    ^2 + (x347 - x400)^2) + 1 / sqrt((x67 - x121)^2 + (x207 - x261)^2 + (x347
    - x401)^2) + 1 / sqrt((x67 - x122)^2 + (x207 - x262)^2 + (x347 - x402)^2)
    + 1 / sqrt((x67 - x123)^2 + (x207 - x263)^2 + (x347 - x403)^2) + 1 / sqrt(
    (x67 - x124)^2 + (x207 - x264)^2 + (x347 - x404)^2) + 1 / sqrt((x67 - x125)
    ^2 + (x207 - x265)^2 + (x347 - x405)^2) + 1 / sqrt((x67 - x126)^2 + (x207
    - x266)^2 + (x347 - x406)^2) + 1 / sqrt((x67 - x127)^2 + (x207 - x267)^2
    + (x347 - x407)^2) + 1 / sqrt((x67 - x128)^2 + (x207 - x268)^2 + (x347 -
    x408)^2) + 1 / sqrt((x67 - x129)^2 + (x207 - x269)^2 + (x347 - x409)^2) + 1
    / sqrt((x67 - x130)^2 + (x207 - x270)^2 + (x347 - x410)^2) + 1 / sqrt((x67
    - x131)^2 + (x207 - x271)^2 + (x347 - x411)^2) + 1 / sqrt((x67 - x132)^2
    + (x207 - x272)^2 + (x347 - x412)^2) + 1 / sqrt((x67 - x133)^2 + (x207 -
    x273)^2 + (x347 - x413)^2) + 1 / sqrt((x67 - x134)^2 + (x207 - x274)^2 + (
    x347 - x414)^2) + 1 / sqrt((x67 - x135)^2 + (x207 - x275)^2 + (x347 - x415)
    ^2) + 1 / sqrt((x67 - x136)^2 + (x207 - x276)^2 + (x347 - x416)^2) + 1 /
    sqrt((x67 - x137)^2 + (x207 - x277)^2 + (x347 - x417)^2) + 1 / sqrt((x67 -
    x138)^2 + (x207 - x278)^2 + (x347 - x418)^2) + 1 / sqrt((x67 - x139)^2 + (
    x207 - x279)^2 + (x347 - x419)^2) + 1 / sqrt((x67 - x140)^2 + (x207 - x280)
    ^2 + (x347 - x420)^2) + 1 / sqrt((x68 - x69)^2 + (x208 - x209)^2 + (x348 -
    x349)^2) + 1 / sqrt((x68 - x70)^2 + (x208 - x210)^2 + (x348 - x350)^2) + 1
    / sqrt((x68 - x71)^2 + (x208 - x211)^2 + (x348 - x351)^2) + 1 / sqrt((x68
    - x72)^2 + (x208 - x212)^2 + (x348 - x352)^2) + 1 / sqrt((x68 - x73)^2 + (
    x208 - x213)^2 + (x348 - x353)^2) + 1 / sqrt((x68 - x74)^2 + (x208 - x214)^
    2 + (x348 - x354)^2) + 1 / sqrt((x68 - x75)^2 + (x208 - x215)^2 + (x348 -
    x355)^2) + 1 / sqrt((x68 - x76)^2 + (x208 - x216)^2 + (x348 - x356)^2) + 1
    / sqrt((x68 - x77)^2 + (x208 - x217)^2 + (x348 - x357)^2) + 1 / sqrt((x68
    - x78)^2 + (x208 - x218)^2 + (x348 - x358)^2) + 1 / sqrt((x68 - x79)^2 + (
    x208 - x219)^2 + (x348 - x359)^2) + 1 / sqrt((x68 - x80)^2 + (x208 - x220)^
    2 + (x348 - x360)^2) + 1 / sqrt((x68 - x81)^2 + (x208 - x221)^2 + (x348 -
    x361)^2) + 1 / sqrt((x68 - x82)^2 + (x208 - x222)^2 + (x348 - x362)^2) + 1
    / sqrt((x68 - x83)^2 + (x208 - x223)^2 + (x348 - x363)^2) + 1 / sqrt((x68
    - x84)^2 + (x208 - x224)^2 + (x348 - x364)^2) + 1 / sqrt((x68 - x85)^2 + (
    x208 - x225)^2 + (x348 - x365)^2) + 1 / sqrt((x68 - x86)^2 + (x208 - x226)^
    2 + (x348 - x366)^2) + 1 / sqrt((x68 - x87)^2 + (x208 - x227)^2 + (x348 -
    x367)^2) + 1 / sqrt((x68 - x88)^2 + (x208 - x228)^2 + (x348 - x368)^2) + 1
    / sqrt((x68 - x89)^2 + (x208 - x229)^2 + (x348 - x369)^2) + 1 / sqrt((x68
    - x90)^2 + (x208 - x230)^2 + (x348 - x370)^2) + 1 / sqrt((x68 - x91)^2 + (
    x208 - x231)^2 + (x348 - x371)^2) + 1 / sqrt((x68 - x92)^2 + (x208 - x232)^
    2 + (x348 - x372)^2) + 1 / sqrt((x68 - x93)^2 + (x208 - x233)^2 + (x348 -
    x373)^2) + 1 / sqrt((x68 - x94)^2 + (x208 - x234)^2 + (x348 - x374)^2) + 1
    / sqrt((x68 - x95)^2 + (x208 - x235)^2 + (x348 - x375)^2) + 1 / sqrt((x68
    - x96)^2 + (x208 - x236)^2 + (x348 - x376)^2) + 1 / sqrt((x68 - x97)^2 + (
    x208 - x237)^2 + (x348 - x377)^2) + 1 / sqrt((x68 - x98)^2 + (x208 - x238)^
    2 + (x348 - x378)^2) + 1 / sqrt((x68 - x99)^2 + (x208 - x239)^2 + (x348 -
    x379)^2) + 1 / sqrt((x68 - x100)^2 + (x208 - x240)^2 + (x348 - x380)^2) + 1
    / sqrt((x68 - x101)^2 + (x208 - x241)^2 + (x348 - x381)^2) + 1 / sqrt((x68
    - x102)^2 + (x208 - x242)^2 + (x348 - x382)^2) + 1 / sqrt((x68 - x103)^2
    + (x208 - x243)^2 + (x348 - x383)^2) + 1 / sqrt((x68 - x104)^2 + (x208 -
    x244)^2 + (x348 - x384)^2) + 1 / sqrt((x68 - x105)^2 + (x208 - x245)^2 + (
    x348 - x385)^2) + 1 / sqrt((x68 - x106)^2 + (x208 - x246)^2 + (x348 - x386)
    ^2) + 1 / sqrt((x68 - x107)^2 + (x208 - x247)^2 + (x348 - x387)^2) + 1 /
    sqrt((x68 - x108)^2 + (x208 - x248)^2 + (x348 - x388)^2) + 1 / sqrt((x68 -
    x109)^2 + (x208 - x249)^2 + (x348 - x389)^2) + 1 / sqrt((x68 - x110)^2 + (
    x208 - x250)^2 + (x348 - x390)^2) + 1 / sqrt((x68 - x111)^2 + (x208 - x251)
    ^2 + (x348 - x391)^2) + 1 / sqrt((x68 - x112)^2 + (x208 - x252)^2 + (x348
    - x392)^2) + 1 / sqrt((x68 - x113)^2 + (x208 - x253)^2 + (x348 - x393)^2)
    + 1 / sqrt((x68 - x114)^2 + (x208 - x254)^2 + (x348 - x394)^2) + 1 / sqrt(
    (x68 - x115)^2 + (x208 - x255)^2 + (x348 - x395)^2) + 1 / sqrt((x68 - x116)
    ^2 + (x208 - x256)^2 + (x348 - x396)^2) + 1 / sqrt((x68 - x117)^2 + (x208
    - x257)^2 + (x348 - x397)^2) + 1 / sqrt((x68 - x118)^2 + (x208 - x258)^2
    + (x348 - x398)^2) + 1 / sqrt((x68 - x119)^2 + (x208 - x259)^2 + (x348 -
    x399)^2) + 1 / sqrt((x68 - x120)^2 + (x208 - x260)^2 + (x348 - x400)^2) + 1
    / sqrt((x68 - x121)^2 + (x208 - x261)^2 + (x348 - x401)^2) + 1 / sqrt((x68
    - x122)^2 + (x208 - x262)^2 + (x348 - x402)^2) + 1 / sqrt((x68 - x123)^2
    + (x208 - x263)^2 + (x348 - x403)^2) + 1 / sqrt((x68 - x124)^2 + (x208 -
    x264)^2 + (x348 - x404)^2) + 1 / sqrt((x68 - x125)^2 + (x208 - x265)^2 + (
    x348 - x405)^2) + 1 / sqrt((x68 - x126)^2 + (x208 - x266)^2 + (x348 - x406)
    ^2) + 1 / sqrt((x68 - x127)^2 + (x208 - x267)^2 + (x348 - x407)^2) + 1 /
    sqrt((x68 - x128)^2 + (x208 - x268)^2 + (x348 - x408)^2) + 1 / sqrt((x68 -
    x129)^2 + (x208 - x269)^2 + (x348 - x409)^2) + 1 / sqrt((x68 - x130)^2 + (
    x208 - x270)^2 + (x348 - x410)^2) + 1 / sqrt((x68 - x131)^2 + (x208 - x271)
    ^2 + (x348 - x411)^2) + 1 / sqrt((x68 - x132)^2 + (x208 - x272)^2 + (x348
    - x412)^2) + 1 / sqrt((x68 - x133)^2 + (x208 - x273)^2 + (x348 - x413)^2)
    + 1 / sqrt((x68 - x134)^2 + (x208 - x274)^2 + (x348 - x414)^2) + 1 / sqrt(
    (x68 - x135)^2 + (x208 - x275)^2 + (x348 - x415)^2) + 1 / sqrt((x68 - x136)
    ^2 + (x208 - x276)^2 + (x348 - x416)^2) + 1 / sqrt((x68 - x137)^2 + (x208
    - x277)^2 + (x348 - x417)^2) + 1 / sqrt((x68 - x138)^2 + (x208 - x278)^2
    + (x348 - x418)^2) + 1 / sqrt((x68 - x139)^2 + (x208 - x279)^2 + (x348 -
    x419)^2) + 1 / sqrt((x68 - x140)^2 + (x208 - x280)^2 + (x348 - x420)^2) + 1
    / sqrt((x69 - x70)^2 + (x209 - x210)^2 + (x349 - x350)^2) + 1 / sqrt((x69
    - x71)^2 + (x209 - x211)^2 + (x349 - x351)^2) + 1 / sqrt((x69 - x72)^2 + (
    x209 - x212)^2 + (x349 - x352)^2) + 1 / sqrt((x69 - x73)^2 + (x209 - x213)^
    2 + (x349 - x353)^2) + 1 / sqrt((x69 - x74)^2 + (x209 - x214)^2 + (x349 -
    x354)^2) + 1 / sqrt((x69 - x75)^2 + (x209 - x215)^2 + (x349 - x355)^2) + 1
    / sqrt((x69 - x76)^2 + (x209 - x216)^2 + (x349 - x356)^2) + 1 / sqrt((x69
    - x77)^2 + (x209 - x217)^2 + (x349 - x357)^2) + 1 / sqrt((x69 - x78)^2 + (
    x209 - x218)^2 + (x349 - x358)^2) + 1 / sqrt((x69 - x79)^2 + (x209 - x219)^
    2 + (x349 - x359)^2) + 1 / sqrt((x69 - x80)^2 + (x209 - x220)^2 + (x349 -
    x360)^2) + 1 / sqrt((x69 - x81)^2 + (x209 - x221)^2 + (x349 - x361)^2) + 1
    / sqrt((x69 - x82)^2 + (x209 - x222)^2 + (x349 - x362)^2) + 1 / sqrt((x69
    - x83)^2 + (x209 - x223)^2 + (x349 - x363)^2) + 1 / sqrt((x69 - x84)^2 + (
    x209 - x224)^2 + (x349 - x364)^2) + 1 / sqrt((x69 - x85)^2 + (x209 - x225)^
    2 + (x349 - x365)^2) + 1 / sqrt((x69 - x86)^2 + (x209 - x226)^2 + (x349 -
    x366)^2) + 1 / sqrt((x69 - x87)^2 + (x209 - x227)^2 + (x349 - x367)^2) + 1
    / sqrt((x69 - x88)^2 + (x209 - x228)^2 + (x349 - x368)^2) + 1 / sqrt((x69
    - x89)^2 + (x209 - x229)^2 + (x349 - x369)^2) + 1 / sqrt((x69 - x90)^2 + (
    x209 - x230)^2 + (x349 - x370)^2) + 1 / sqrt((x69 - x91)^2 + (x209 - x231)^
    2 + (x349 - x371)^2) + 1 / sqrt((x69 - x92)^2 + (x209 - x232)^2 + (x349 -
    x372)^2) + 1 / sqrt((x69 - x93)^2 + (x209 - x233)^2 + (x349 - x373)^2) + 1
    / sqrt((x69 - x94)^2 + (x209 - x234)^2 + (x349 - x374)^2) + 1 / sqrt((x69
    - x95)^2 + (x209 - x235)^2 + (x349 - x375)^2) + 1 / sqrt((x69 - x96)^2 + (
    x209 - x236)^2 + (x349 - x376)^2) + 1 / sqrt((x69 - x97)^2 + (x209 - x237)^
    2 + (x349 - x377)^2) + 1 / sqrt((x69 - x98)^2 + (x209 - x238)^2 + (x349 -
    x378)^2) + 1 / sqrt((x69 - x99)^2 + (x209 - x239)^2 + (x349 - x379)^2) + 1
    / sqrt((x69 - x100)^2 + (x209 - x240)^2 + (x349 - x380)^2) + 1 / sqrt((x69
    - x101)^2 + (x209 - x241)^2 + (x349 - x381)^2) + 1 / sqrt((x69 - x102)^2
    + (x209 - x242)^2 + (x349 - x382)^2) + 1 / sqrt((x69 - x103)^2 + (x209 -
    x243)^2 + (x349 - x383)^2) + 1 / sqrt((x69 - x104)^2 + (x209 - x244)^2 + (
    x349 - x384)^2) + 1 / sqrt((x69 - x105)^2 + (x209 - x245)^2 + (x349 - x385)
    ^2) + 1 / sqrt((x69 - x106)^2 + (x209 - x246)^2 + (x349 - x386)^2) + 1 /
    sqrt((x69 - x107)^2 + (x209 - x247)^2 + (x349 - x387)^2) + 1 / sqrt((x69 -
    x108)^2 + (x209 - x248)^2 + (x349 - x388)^2) + 1 / sqrt((x69 - x109)^2 + (
    x209 - x249)^2 + (x349 - x389)^2) + 1 / sqrt((x69 - x110)^2 + (x209 - x250)
    ^2 + (x349 - x390)^2) + 1 / sqrt((x69 - x111)^2 + (x209 - x251)^2 + (x349
    - x391)^2) + 1 / sqrt((x69 - x112)^2 + (x209 - x252)^2 + (x349 - x392)^2)
    + 1 / sqrt((x69 - x113)^2 + (x209 - x253)^2 + (x349 - x393)^2) + 1 / sqrt(
    (x69 - x114)^2 + (x209 - x254)^2 + (x349 - x394)^2) + 1 / sqrt((x69 - x115)
    ^2 + (x209 - x255)^2 + (x349 - x395)^2) + 1 / sqrt((x69 - x116)^2 + (x209
    - x256)^2 + (x349 - x396)^2) + 1 / sqrt((x69 - x117)^2 + (x209 - x257)^2
    + (x349 - x397)^2) + 1 / sqrt((x69 - x118)^2 + (x209 - x258)^2 + (x349 -
    x398)^2) + 1 / sqrt((x69 - x119)^2 + (x209 - x259)^2 + (x349 - x399)^2) + 1
    / sqrt((x69 - x120)^2 + (x209 - x260)^2 + (x349 - x400)^2) + 1 / sqrt((x69
    - x121)^2 + (x209 - x261)^2 + (x349 - x401)^2) + 1 / sqrt((x69 - x122)^2
    + (x209 - x262)^2 + (x349 - x402)^2) + 1 / sqrt((x69 - x123)^2 + (x209 -
    x263)^2 + (x349 - x403)^2) + 1 / sqrt((x69 - x124)^2 + (x209 - x264)^2 + (
    x349 - x404)^2) + 1 / sqrt((x69 - x125)^2 + (x209 - x265)^2 + (x349 - x405)
    ^2) + 1 / sqrt((x69 - x126)^2 + (x209 - x266)^2 + (x349 - x406)^2) + 1 /
    sqrt((x69 - x127)^2 + (x209 - x267)^2 + (x349 - x407)^2) + 1 / sqrt((x69 -
    x128)^2 + (x209 - x268)^2 + (x349 - x408)^2) + 1 / sqrt((x69 - x129)^2 + (
    x209 - x269)^2 + (x349 - x409)^2) + 1 / sqrt((x69 - x130)^2 + (x209 - x270)
    ^2 + (x349 - x410)^2) + 1 / sqrt((x69 - x131)^2 + (x209 - x271)^2 + (x349
    - x411)^2) + 1 / sqrt((x69 - x132)^2 + (x209 - x272)^2 + (x349 - x412)^2)
    + 1 / sqrt((x69 - x133)^2 + (x209 - x273)^2 + (x349 - x413)^2) + 1 / sqrt(
    (x69 - x134)^2 + (x209 - x274)^2 + (x349 - x414)^2) + 1 / sqrt((x69 - x135)
    ^2 + (x209 - x275)^2 + (x349 - x415)^2) + 1 / sqrt((x69 - x136)^2 + (x209
    - x276)^2 + (x349 - x416)^2) + 1 / sqrt((x69 - x137)^2 + (x209 - x277)^2
    + (x349 - x417)^2) + 1 / sqrt((x69 - x138)^2 + (x209 - x278)^2 + (x349 -
    x418)^2) + 1 / sqrt((x69 - x139)^2 + (x209 - x279)^2 + (x349 - x419)^2) + 1
    / sqrt((x69 - x140)^2 + (x209 - x280)^2 + (x349 - x420)^2) + 1 / sqrt((x70
    - x71)^2 + (x210 - x211)^2 + (x350 - x351)^2) + 1 / sqrt((x70 - x72)^2 + (
    x210 - x212)^2 + (x350 - x352)^2) + 1 / sqrt((x70 - x73)^2 + (x210 - x213)^
    2 + (x350 - x353)^2) + 1 / sqrt((x70 - x74)^2 + (x210 - x214)^2 + (x350 -
    x354)^2) + 1 / sqrt((x70 - x75)^2 + (x210 - x215)^2 + (x350 - x355)^2) + 1
    / sqrt((x70 - x76)^2 + (x210 - x216)^2 + (x350 - x356)^2) + 1 / sqrt((x70
    - x77)^2 + (x210 - x217)^2 + (x350 - x357)^2) + 1 / sqrt((x70 - x78)^2 + (
    x210 - x218)^2 + (x350 - x358)^2) + 1 / sqrt((x70 - x79)^2 + (x210 - x219)^
    2 + (x350 - x359)^2) + 1 / sqrt((x70 - x80)^2 + (x210 - x220)^2 + (x350 -
    x360)^2) + 1 / sqrt((x70 - x81)^2 + (x210 - x221)^2 + (x350 - x361)^2) + 1
    / sqrt((x70 - x82)^2 + (x210 - x222)^2 + (x350 - x362)^2) + 1 / sqrt((x70
    - x83)^2 + (x210 - x223)^2 + (x350 - x363)^2) + 1 / sqrt((x70 - x84)^2 + (
    x210 - x224)^2 + (x350 - x364)^2) + 1 / sqrt((x70 - x85)^2 + (x210 - x225)^
    2 + (x350 - x365)^2) + 1 / sqrt((x70 - x86)^2 + (x210 - x226)^2 + (x350 -
    x366)^2) + 1 / sqrt((x70 - x87)^2 + (x210 - x227)^2 + (x350 - x367)^2) + 1
    / sqrt((x70 - x88)^2 + (x210 - x228)^2 + (x350 - x368)^2) + 1 / sqrt((x70
    - x89)^2 + (x210 - x229)^2 + (x350 - x369)^2) + 1 / sqrt((x70 - x90)^2 + (
    x210 - x230)^2 + (x350 - x370)^2) + 1 / sqrt((x70 - x91)^2 + (x210 - x231)^
    2 + (x350 - x371)^2) + 1 / sqrt((x70 - x92)^2 + (x210 - x232)^2 + (x350 -
    x372)^2) + 1 / sqrt((x70 - x93)^2 + (x210 - x233)^2 + (x350 - x373)^2) + 1
    / sqrt((x70 - x94)^2 + (x210 - x234)^2 + (x350 - x374)^2) + 1 / sqrt((x70
    - x95)^2 + (x210 - x235)^2 + (x350 - x375)^2) + 1 / sqrt((x70 - x96)^2 + (
    x210 - x236)^2 + (x350 - x376)^2) + 1 / sqrt((x70 - x97)^2 + (x210 - x237)^
    2 + (x350 - x377)^2) + 1 / sqrt((x70 - x98)^2 + (x210 - x238)^2 + (x350 -
    x378)^2) + 1 / sqrt((x70 - x99)^2 + (x210 - x239)^2 + (x350 - x379)^2) + 1
    / sqrt((x70 - x100)^2 + (x210 - x240)^2 + (x350 - x380)^2) + 1 / sqrt((x70
    - x101)^2 + (x210 - x241)^2 + (x350 - x381)^2) + 1 / sqrt((x70 - x102)^2
    + (x210 - x242)^2 + (x350 - x382)^2) + 1 / sqrt((x70 - x103)^2 + (x210 -
    x243)^2 + (x350 - x383)^2) + 1 / sqrt((x70 - x104)^2 + (x210 - x244)^2 + (
    x350 - x384)^2) + 1 / sqrt((x70 - x105)^2 + (x210 - x245)^2 + (x350 - x385)
    ^2) + 1 / sqrt((x70 - x106)^2 + (x210 - x246)^2 + (x350 - x386)^2) + 1 /
    sqrt((x70 - x107)^2 + (x210 - x247)^2 + (x350 - x387)^2) + 1 / sqrt((x70 -
    x108)^2 + (x210 - x248)^2 + (x350 - x388)^2) + 1 / sqrt((x70 - x109)^2 + (
    x210 - x249)^2 + (x350 - x389)^2) + 1 / sqrt((x70 - x110)^2 + (x210 - x250)
    ^2 + (x350 - x390)^2) + 1 / sqrt((x70 - x111)^2 + (x210 - x251)^2 + (x350
    - x391)^2) + 1 / sqrt((x70 - x112)^2 + (x210 - x252)^2 + (x350 - x392)^2)
    + 1 / sqrt((x70 - x113)^2 + (x210 - x253)^2 + (x350 - x393)^2) + 1 / sqrt(
    (x70 - x114)^2 + (x210 - x254)^2 + (x350 - x394)^2) + 1 / sqrt((x70 - x115)
    ^2 + (x210 - x255)^2 + (x350 - x395)^2) + 1 / sqrt((x70 - x116)^2 + (x210
    - x256)^2 + (x350 - x396)^2) + 1 / sqrt((x70 - x117)^2 + (x210 - x257)^2
    + (x350 - x397)^2) + 1 / sqrt((x70 - x118)^2 + (x210 - x258)^2 + (x350 -
    x398)^2) + 1 / sqrt((x70 - x119)^2 + (x210 - x259)^2 + (x350 - x399)^2) + 1
    / sqrt((x70 - x120)^2 + (x210 - x260)^2 + (x350 - x400)^2) + 1 / sqrt((x70
    - x121)^2 + (x210 - x261)^2 + (x350 - x401)^2) + 1 / sqrt((x70 - x122)^2
    + (x210 - x262)^2 + (x350 - x402)^2) + 1 / sqrt((x70 - x123)^2 + (x210 -
    x263)^2 + (x350 - x403)^2) + 1 / sqrt((x70 - x124)^2 + (x210 - x264)^2 + (
    x350 - x404)^2) + 1 / sqrt((x70 - x125)^2 + (x210 - x265)^2 + (x350 - x405)
    ^2) + 1 / sqrt((x70 - x126)^2 + (x210 - x266)^2 + (x350 - x406)^2) + 1 /
    sqrt((x70 - x127)^2 + (x210 - x267)^2 + (x350 - x407)^2) + 1 / sqrt((x70 -
    x128)^2 + (x210 - x268)^2 + (x350 - x408)^2) + 1 / sqrt((x70 - x129)^2 + (
    x210 - x269)^2 + (x350 - x409)^2) + 1 / sqrt((x70 - x130)^2 + (x210 - x270)
    ^2 + (x350 - x410)^2) + 1 / sqrt((x70 - x131)^2 + (x210 - x271)^2 + (x350
    - x411)^2) + 1 / sqrt((x70 - x132)^2 + (x210 - x272)^2 + (x350 - x412)^2)
    + 1 / sqrt((x70 - x133)^2 + (x210 - x273)^2 + (x350 - x413)^2) + 1 / sqrt(
    (x70 - x134)^2 + (x210 - x274)^2 + (x350 - x414)^2) + 1 / sqrt((x70 - x135)
    ^2 + (x210 - x275)^2 + (x350 - x415)^2) + 1 / sqrt((x70 - x136)^2 + (x210
    - x276)^2 + (x350 - x416)^2) + 1 / sqrt((x70 - x137)^2 + (x210 - x277)^2
    + (x350 - x417)^2) + 1 / sqrt((x70 - x138)^2 + (x210 - x278)^2 + (x350 -
    x418)^2) + 1 / sqrt((x70 - x139)^2 + (x210 - x279)^2 + (x350 - x419)^2) + 1
    / sqrt((x70 - x140)^2 + (x210 - x280)^2 + (x350 - x420)^2) + 1 / sqrt((x71
    - x72)^2 + (x211 - x212)^2 + (x351 - x352)^2) + 1 / sqrt((x71 - x73)^2 + (
    x211 - x213)^2 + (x351 - x353)^2) + 1 / sqrt((x71 - x74)^2 + (x211 - x214)^
    2 + (x351 - x354)^2) + 1 / sqrt((x71 - x75)^2 + (x211 - x215)^2 + (x351 -
    x355)^2) + 1 / sqrt((x71 - x76)^2 + (x211 - x216)^2 + (x351 - x356)^2) + 1
    / sqrt((x71 - x77)^2 + (x211 - x217)^2 + (x351 - x357)^2) + 1 / sqrt((x71
    - x78)^2 + (x211 - x218)^2 + (x351 - x358)^2) + 1 / sqrt((x71 - x79)^2 + (
    x211 - x219)^2 + (x351 - x359)^2) + 1 / sqrt((x71 - x80)^2 + (x211 - x220)^
    2 + (x351 - x360)^2) + 1 / sqrt((x71 - x81)^2 + (x211 - x221)^2 + (x351 -
    x361)^2) + 1 / sqrt((x71 - x82)^2 + (x211 - x222)^2 + (x351 - x362)^2) + 1
    / sqrt((x71 - x83)^2 + (x211 - x223)^2 + (x351 - x363)^2) + 1 / sqrt((x71
    - x84)^2 + (x211 - x224)^2 + (x351 - x364)^2) + 1 / sqrt((x71 - x85)^2 + (
    x211 - x225)^2 + (x351 - x365)^2) + 1 / sqrt((x71 - x86)^2 + (x211 - x226)^
    2 + (x351 - x366)^2) + 1 / sqrt((x71 - x87)^2 + (x211 - x227)^2 + (x351 -
    x367)^2) + 1 / sqrt((x71 - x88)^2 + (x211 - x228)^2 + (x351 - x368)^2) + 1
    / sqrt((x71 - x89)^2 + (x211 - x229)^2 + (x351 - x369)^2) + 1 / sqrt((x71
    - x90)^2 + (x211 - x230)^2 + (x351 - x370)^2) + 1 / sqrt((x71 - x91)^2 + (
    x211 - x231)^2 + (x351 - x371)^2) + 1 / sqrt((x71 - x92)^2 + (x211 - x232)^
    2 + (x351 - x372)^2) + 1 / sqrt((x71 - x93)^2 + (x211 - x233)^2 + (x351 -
    x373)^2) + 1 / sqrt((x71 - x94)^2 + (x211 - x234)^2 + (x351 - x374)^2) + 1
    / sqrt((x71 - x95)^2 + (x211 - x235)^2 + (x351 - x375)^2) + 1 / sqrt((x71
    - x96)^2 + (x211 - x236)^2 + (x351 - x376)^2) + 1 / sqrt((x71 - x97)^2 + (
    x211 - x237)^2 + (x351 - x377)^2) + 1 / sqrt((x71 - x98)^2 + (x211 - x238)^
    2 + (x351 - x378)^2) + 1 / sqrt((x71 - x99)^2 + (x211 - x239)^2 + (x351 -
    x379)^2) + 1 / sqrt((x71 - x100)^2 + (x211 - x240)^2 + (x351 - x380)^2) + 1
    / sqrt((x71 - x101)^2 + (x211 - x241)^2 + (x351 - x381)^2) + 1 / sqrt((x71
    - x102)^2 + (x211 - x242)^2 + (x351 - x382)^2) + 1 / sqrt((x71 - x103)^2
    + (x211 - x243)^2 + (x351 - x383)^2) + 1 / sqrt((x71 - x104)^2 + (x211 -
    x244)^2 + (x351 - x384)^2) + 1 / sqrt((x71 - x105)^2 + (x211 - x245)^2 + (
    x351 - x385)^2) + 1 / sqrt((x71 - x106)^2 + (x211 - x246)^2 + (x351 - x386)
    ^2) + 1 / sqrt((x71 - x107)^2 + (x211 - x247)^2 + (x351 - x387)^2) + 1 /
    sqrt((x71 - x108)^2 + (x211 - x248)^2 + (x351 - x388)^2) + 1 / sqrt((x71 -
    x109)^2 + (x211 - x249)^2 + (x351 - x389)^2) + 1 / sqrt((x71 - x110)^2 + (
    x211 - x250)^2 + (x351 - x390)^2) + 1 / sqrt((x71 - x111)^2 + (x211 - x251)
    ^2 + (x351 - x391)^2) + 1 / sqrt((x71 - x112)^2 + (x211 - x252)^2 + (x351
    - x392)^2) + 1 / sqrt((x71 - x113)^2 + (x211 - x253)^2 + (x351 - x393)^2)
    + 1 / sqrt((x71 - x114)^2 + (x211 - x254)^2 + (x351 - x394)^2) + 1 / sqrt(
    (x71 - x115)^2 + (x211 - x255)^2 + (x351 - x395)^2) + 1 / sqrt((x71 - x116)
    ^2 + (x211 - x256)^2 + (x351 - x396)^2) + 1 / sqrt((x71 - x117)^2 + (x211
    - x257)^2 + (x351 - x397)^2) + 1 / sqrt((x71 - x118)^2 + (x211 - x258)^2
    + (x351 - x398)^2) + 1 / sqrt((x71 - x119)^2 + (x211 - x259)^2 + (x351 -
    x399)^2) + 1 / sqrt((x71 - x120)^2 + (x211 - x260)^2 + (x351 - x400)^2) + 1
    / sqrt((x71 - x121)^2 + (x211 - x261)^2 + (x351 - x401)^2) + 1 / sqrt((x71
    - x122)^2 + (x211 - x262)^2 + (x351 - x402)^2) + 1 / sqrt((x71 - x123)^2
    + (x211 - x263)^2 + (x351 - x403)^2) + 1 / sqrt((x71 - x124)^2 + (x211 -
    x264)^2 + (x351 - x404)^2) + 1 / sqrt((x71 - x125)^2 + (x211 - x265)^2 + (
    x351 - x405)^2) + 1 / sqrt((x71 - x126)^2 + (x211 - x266)^2 + (x351 - x406)
    ^2) + 1 / sqrt((x71 - x127)^2 + (x211 - x267)^2 + (x351 - x407)^2) + 1 /
    sqrt((x71 - x128)^2 + (x211 - x268)^2 + (x351 - x408)^2) + 1 / sqrt((x71 -
    x129)^2 + (x211 - x269)^2 + (x351 - x409)^2) + 1 / sqrt((x71 - x130)^2 + (
    x211 - x270)^2 + (x351 - x410)^2) + 1 / sqrt((x71 - x131)^2 + (x211 - x271)
    ^2 + (x351 - x411)^2) + 1 / sqrt((x71 - x132)^2 + (x211 - x272)^2 + (x351
    - x412)^2) + 1 / sqrt((x71 - x133)^2 + (x211 - x273)^2 + (x351 - x413)^2)
    + 1 / sqrt((x71 - x134)^2 + (x211 - x274)^2 + (x351 - x414)^2) + 1 / sqrt(
    (x71 - x135)^2 + (x211 - x275)^2 + (x351 - x415)^2) + 1 / sqrt((x71 - x136)
    ^2 + (x211 - x276)^2 + (x351 - x416)^2) + 1 / sqrt((x71 - x137)^2 + (x211
    - x277)^2 + (x351 - x417)^2) + 1 / sqrt((x71 - x138)^2 + (x211 - x278)^2
    + (x351 - x418)^2) + 1 / sqrt((x71 - x139)^2 + (x211 - x279)^2 + (x351 -
    x419)^2) + 1 / sqrt((x71 - x140)^2 + (x211 - x280)^2 + (x351 - x420)^2) + 1
    / sqrt((x72 - x73)^2 + (x212 - x213)^2 + (x352 - x353)^2) + 1 / sqrt((x72
    - x74)^2 + (x212 - x214)^2 + (x352 - x354)^2) + 1 / sqrt((x72 - x75)^2 + (
    x212 - x215)^2 + (x352 - x355)^2) + 1 / sqrt((x72 - x76)^2 + (x212 - x216)^
    2 + (x352 - x356)^2) + 1 / sqrt((x72 - x77)^2 + (x212 - x217)^2 + (x352 -
    x357)^2) + 1 / sqrt((x72 - x78)^2 + (x212 - x218)^2 + (x352 - x358)^2) + 1
    / sqrt((x72 - x79)^2 + (x212 - x219)^2 + (x352 - x359)^2) + 1 / sqrt((x72
    - x80)^2 + (x212 - x220)^2 + (x352 - x360)^2) + 1 / sqrt((x72 - x81)^2 + (
    x212 - x221)^2 + (x352 - x361)^2) + 1 / sqrt((x72 - x82)^2 + (x212 - x222)^
    2 + (x352 - x362)^2) + 1 / sqrt((x72 - x83)^2 + (x212 - x223)^2 + (x352 -
    x363)^2) + 1 / sqrt((x72 - x84)^2 + (x212 - x224)^2 + (x352 - x364)^2) + 1
    / sqrt((x72 - x85)^2 + (x212 - x225)^2 + (x352 - x365)^2) + 1 / sqrt((x72
    - x86)^2 + (x212 - x226)^2 + (x352 - x366)^2) + 1 / sqrt((x72 - x87)^2 + (
    x212 - x227)^2 + (x352 - x367)^2) + 1 / sqrt((x72 - x88)^2 + (x212 - x228)^
    2 + (x352 - x368)^2) + 1 / sqrt((x72 - x89)^2 + (x212 - x229)^2 + (x352 -
    x369)^2) + 1 / sqrt((x72 - x90)^2 + (x212 - x230)^2 + (x352 - x370)^2) + 1
    / sqrt((x72 - x91)^2 + (x212 - x231)^2 + (x352 - x371)^2) + 1 / sqrt((x72
    - x92)^2 + (x212 - x232)^2 + (x352 - x372)^2) + 1 / sqrt((x72 - x93)^2 + (
    x212 - x233)^2 + (x352 - x373)^2) + 1 / sqrt((x72 - x94)^2 + (x212 - x234)^
    2 + (x352 - x374)^2) + 1 / sqrt((x72 - x95)^2 + (x212 - x235)^2 + (x352 -
    x375)^2) + 1 / sqrt((x72 - x96)^2 + (x212 - x236)^2 + (x352 - x376)^2) + 1
    / sqrt((x72 - x97)^2 + (x212 - x237)^2 + (x352 - x377)^2) + 1 / sqrt((x72
    - x98)^2 + (x212 - x238)^2 + (x352 - x378)^2) + 1 / sqrt((x72 - x99)^2 + (
    x212 - x239)^2 + (x352 - x379)^2) + 1 / sqrt((x72 - x100)^2 + (x212 - x240)
    ^2 + (x352 - x380)^2) + 1 / sqrt((x72 - x101)^2 + (x212 - x241)^2 + (x352
    - x381)^2) + 1 / sqrt((x72 - x102)^2 + (x212 - x242)^2 + (x352 - x382)^2)
    + 1 / sqrt((x72 - x103)^2 + (x212 - x243)^2 + (x352 - x383)^2) + 1 / sqrt(
    (x72 - x104)^2 + (x212 - x244)^2 + (x352 - x384)^2) + 1 / sqrt((x72 - x105)
    ^2 + (x212 - x245)^2 + (x352 - x385)^2) + 1 / sqrt((x72 - x106)^2 + (x212
    - x246)^2 + (x352 - x386)^2) + 1 / sqrt((x72 - x107)^2 + (x212 - x247)^2
    + (x352 - x387)^2) + 1 / sqrt((x72 - x108)^2 + (x212 - x248)^2 + (x352 -
    x388)^2) + 1 / sqrt((x72 - x109)^2 + (x212 - x249)^2 + (x352 - x389)^2) + 1
    / sqrt((x72 - x110)^2 + (x212 - x250)^2 + (x352 - x390)^2) + 1 / sqrt((x72
    - x111)^2 + (x212 - x251)^2 + (x352 - x391)^2) + 1 / sqrt((x72 - x112)^2
    + (x212 - x252)^2 + (x352 - x392)^2) + 1 / sqrt((x72 - x113)^2 + (x212 -
    x253)^2 + (x352 - x393)^2) + 1 / sqrt((x72 - x114)^2 + (x212 - x254)^2 + (
    x352 - x394)^2) + 1 / sqrt((x72 - x115)^2 + (x212 - x255)^2 + (x352 - x395)
    ^2) + 1 / sqrt((x72 - x116)^2 + (x212 - x256)^2 + (x352 - x396)^2) + 1 /
    sqrt((x72 - x117)^2 + (x212 - x257)^2 + (x352 - x397)^2) + 1 / sqrt((x72 -
    x118)^2 + (x212 - x258)^2 + (x352 - x398)^2) + 1 / sqrt((x72 - x119)^2 + (
    x212 - x259)^2 + (x352 - x399)^2) + 1 / sqrt((x72 - x120)^2 + (x212 - x260)
    ^2 + (x352 - x400)^2) + 1 / sqrt((x72 - x121)^2 + (x212 - x261)^2 + (x352
    - x401)^2) + 1 / sqrt((x72 - x122)^2 + (x212 - x262)^2 + (x352 - x402)^2)
    + 1 / sqrt((x72 - x123)^2 + (x212 - x263)^2 + (x352 - x403)^2) + 1 / sqrt(
    (x72 - x124)^2 + (x212 - x264)^2 + (x352 - x404)^2) + 1 / sqrt((x72 - x125)
    ^2 + (x212 - x265)^2 + (x352 - x405)^2) + 1 / sqrt((x72 - x126)^2 + (x212
    - x266)^2 + (x352 - x406)^2) + 1 / sqrt((x72 - x127)^2 + (x212 - x267)^2
    + (x352 - x407)^2) + 1 / sqrt((x72 - x128)^2 + (x212 - x268)^2 + (x352 -
    x408)^2) + 1 / sqrt((x72 - x129)^2 + (x212 - x269)^2 + (x352 - x409)^2) + 1
    / sqrt((x72 - x130)^2 + (x212 - x270)^2 + (x352 - x410)^2) + 1 / sqrt((x72
    - x131)^2 + (x212 - x271)^2 + (x352 - x411)^2) + 1 / sqrt((x72 - x132)^2
    + (x212 - x272)^2 + (x352 - x412)^2) + 1 / sqrt((x72 - x133)^2 + (x212 -
    x273)^2 + (x352 - x413)^2) + 1 / sqrt((x72 - x134)^2 + (x212 - x274)^2 + (
    x352 - x414)^2) + 1 / sqrt((x72 - x135)^2 + (x212 - x275)^2 + (x352 - x415)
    ^2) + 1 / sqrt((x72 - x136)^2 + (x212 - x276)^2 + (x352 - x416)^2) + 1 /
    sqrt((x72 - x137)^2 + (x212 - x277)^2 + (x352 - x417)^2) + 1 / sqrt((x72 -
    x138)^2 + (x212 - x278)^2 + (x352 - x418)^2) + 1 / sqrt((x72 - x139)^2 + (
    x212 - x279)^2 + (x352 - x419)^2) + 1 / sqrt((x72 - x140)^2 + (x212 - x280)
    ^2 + (x352 - x420)^2) + 1 / sqrt((x73 - x74)^2 + (x213 - x214)^2 + (x353 -
    x354)^2) + 1 / sqrt((x73 - x75)^2 + (x213 - x215)^2 + (x353 - x355)^2) + 1
    / sqrt((x73 - x76)^2 + (x213 - x216)^2 + (x353 - x356)^2) + 1 / sqrt((x73
    - x77)^2 + (x213 - x217)^2 + (x353 - x357)^2) + 1 / sqrt((x73 - x78)^2 + (
    x213 - x218)^2 + (x353 - x358)^2) + 1 / sqrt((x73 - x79)^2 + (x213 - x219)^
    2 + (x353 - x359)^2) + 1 / sqrt((x73 - x80)^2 + (x213 - x220)^2 + (x353 -
    x360)^2) + 1 / sqrt((x73 - x81)^2 + (x213 - x221)^2 + (x353 - x361)^2) + 1
    / sqrt((x73 - x82)^2 + (x213 - x222)^2 + (x353 - x362)^2) + 1 / sqrt((x73
    - x83)^2 + (x213 - x223)^2 + (x353 - x363)^2) + 1 / sqrt((x73 - x84)^2 + (
    x213 - x224)^2 + (x353 - x364)^2) + 1 / sqrt((x73 - x85)^2 + (x213 - x225)^
    2 + (x353 - x365)^2) + 1 / sqrt((x73 - x86)^2 + (x213 - x226)^2 + (x353 -
    x366)^2) + 1 / sqrt((x73 - x87)^2 + (x213 - x227)^2 + (x353 - x367)^2) + 1
    / sqrt((x73 - x88)^2 + (x213 - x228)^2 + (x353 - x368)^2) + 1 / sqrt((x73
    - x89)^2 + (x213 - x229)^2 + (x353 - x369)^2) + 1 / sqrt((x73 - x90)^2 + (
    x213 - x230)^2 + (x353 - x370)^2) + 1 / sqrt((x73 - x91)^2 + (x213 - x231)^
    2 + (x353 - x371)^2) + 1 / sqrt((x73 - x92)^2 + (x213 - x232)^2 + (x353 -
    x372)^2) + 1 / sqrt((x73 - x93)^2 + (x213 - x233)^2 + (x353 - x373)^2) + 1
    / sqrt((x73 - x94)^2 + (x213 - x234)^2 + (x353 - x374)^2) + 1 / sqrt((x73
    - x95)^2 + (x213 - x235)^2 + (x353 - x375)^2) + 1 / sqrt((x73 - x96)^2 + (
    x213 - x236)^2 + (x353 - x376)^2) + 1 / sqrt((x73 - x97)^2 + (x213 - x237)^
    2 + (x353 - x377)^2) + 1 / sqrt((x73 - x98)^2 + (x213 - x238)^2 + (x353 -
    x378)^2) + 1 / sqrt((x73 - x99)^2 + (x213 - x239)^2 + (x353 - x379)^2) + 1
    / sqrt((x73 - x100)^2 + (x213 - x240)^2 + (x353 - x380)^2) + 1 / sqrt((x73
    - x101)^2 + (x213 - x241)^2 + (x353 - x381)^2) + 1 / sqrt((x73 - x102)^2
    + (x213 - x242)^2 + (x353 - x382)^2) + 1 / sqrt((x73 - x103)^2 + (x213 -
    x243)^2 + (x353 - x383)^2) + 1 / sqrt((x73 - x104)^2 + (x213 - x244)^2 + (
    x353 - x384)^2) + 1 / sqrt((x73 - x105)^2 + (x213 - x245)^2 + (x353 - x385)
    ^2) + 1 / sqrt((x73 - x106)^2 + (x213 - x246)^2 + (x353 - x386)^2) + 1 /
    sqrt((x73 - x107)^2 + (x213 - x247)^2 + (x353 - x387)^2) + 1 / sqrt((x73 -
    x108)^2 + (x213 - x248)^2 + (x353 - x388)^2) + 1 / sqrt((x73 - x109)^2 + (
    x213 - x249)^2 + (x353 - x389)^2) + 1 / sqrt((x73 - x110)^2 + (x213 - x250)
    ^2 + (x353 - x390)^2) + 1 / sqrt((x73 - x111)^2 + (x213 - x251)^2 + (x353
    - x391)^2) + 1 / sqrt((x73 - x112)^2 + (x213 - x252)^2 + (x353 - x392)^2)
    + 1 / sqrt((x73 - x113)^2 + (x213 - x253)^2 + (x353 - x393)^2) + 1 / sqrt(
    (x73 - x114)^2 + (x213 - x254)^2 + (x353 - x394)^2) + 1 / sqrt((x73 - x115)
    ^2 + (x213 - x255)^2 + (x353 - x395)^2) + 1 / sqrt((x73 - x116)^2 + (x213
    - x256)^2 + (x353 - x396)^2) + 1 / sqrt((x73 - x117)^2 + (x213 - x257)^2
    + (x353 - x397)^2) + 1 / sqrt((x73 - x118)^2 + (x213 - x258)^2 + (x353 -
    x398)^2) + 1 / sqrt((x73 - x119)^2 + (x213 - x259)^2 + (x353 - x399)^2) + 1
    / sqrt((x73 - x120)^2 + (x213 - x260)^2 + (x353 - x400)^2) + 1 / sqrt((x73
    - x121)^2 + (x213 - x261)^2 + (x353 - x401)^2) + 1 / sqrt((x73 - x122)^2
    + (x213 - x262)^2 + (x353 - x402)^2) + 1 / sqrt((x73 - x123)^2 + (x213 -
    x263)^2 + (x353 - x403)^2) + 1 / sqrt((x73 - x124)^2 + (x213 - x264)^2 + (
    x353 - x404)^2) + 1 / sqrt((x73 - x125)^2 + (x213 - x265)^2 + (x353 - x405)
    ^2) + 1 / sqrt((x73 - x126)^2 + (x213 - x266)^2 + (x353 - x406)^2) + 1 /
    sqrt((x73 - x127)^2 + (x213 - x267)^2 + (x353 - x407)^2) + 1 / sqrt((x73 -
    x128)^2 + (x213 - x268)^2 + (x353 - x408)^2) + 1 / sqrt((x73 - x129)^2 + (
    x213 - x269)^2 + (x353 - x409)^2) + 1 / sqrt((x73 - x130)^2 + (x213 - x270)
    ^2 + (x353 - x410)^2) + 1 / sqrt((x73 - x131)^2 + (x213 - x271)^2 + (x353
    - x411)^2) + 1 / sqrt((x73 - x132)^2 + (x213 - x272)^2 + (x353 - x412)^2)
    + 1 / sqrt((x73 - x133)^2 + (x213 - x273)^2 + (x353 - x413)^2) + 1 / sqrt(
    (x73 - x134)^2 + (x213 - x274)^2 + (x353 - x414)^2) + 1 / sqrt((x73 - x135)
    ^2 + (x213 - x275)^2 + (x353 - x415)^2) + 1 / sqrt((x73 - x136)^2 + (x213
    - x276)^2 + (x353 - x416)^2) + 1 / sqrt((x73 - x137)^2 + (x213 - x277)^2
    + (x353 - x417)^2) + 1 / sqrt((x73 - x138)^2 + (x213 - x278)^2 + (x353 -
    x418)^2) + 1 / sqrt((x73 - x139)^2 + (x213 - x279)^2 + (x353 - x419)^2) + 1
    / sqrt((x73 - x140)^2 + (x213 - x280)^2 + (x353 - x420)^2) + 1 / sqrt((x74
    - x75)^2 + (x214 - x215)^2 + (x354 - x355)^2) + 1 / sqrt((x74 - x76)^2 + (
    x214 - x216)^2 + (x354 - x356)^2) + 1 / sqrt((x74 - x77)^2 + (x214 - x217)^
    2 + (x354 - x357)^2) + 1 / sqrt((x74 - x78)^2 + (x214 - x218)^2 + (x354 -
    x358)^2) + 1 / sqrt((x74 - x79)^2 + (x214 - x219)^2 + (x354 - x359)^2) + 1
    / sqrt((x74 - x80)^2 + (x214 - x220)^2 + (x354 - x360)^2) + 1 / sqrt((x74
    - x81)^2 + (x214 - x221)^2 + (x354 - x361)^2) + 1 / sqrt((x74 - x82)^2 + (
    x214 - x222)^2 + (x354 - x362)^2) + 1 / sqrt((x74 - x83)^2 + (x214 - x223)^
    2 + (x354 - x363)^2) + 1 / sqrt((x74 - x84)^2 + (x214 - x224)^2 + (x354 -
    x364)^2) + 1 / sqrt((x74 - x85)^2 + (x214 - x225)^2 + (x354 - x365)^2) + 1
    / sqrt((x74 - x86)^2 + (x214 - x226)^2 + (x354 - x366)^2) + 1 / sqrt((x74
    - x87)^2 + (x214 - x227)^2 + (x354 - x367)^2) + 1 / sqrt((x74 - x88)^2 + (
    x214 - x228)^2 + (x354 - x368)^2) + 1 / sqrt((x74 - x89)^2 + (x214 - x229)^
    2 + (x354 - x369)^2) + 1 / sqrt((x74 - x90)^2 + (x214 - x230)^2 + (x354 -
    x370)^2) + 1 / sqrt((x74 - x91)^2 + (x214 - x231)^2 + (x354 - x371)^2) + 1
    / sqrt((x74 - x92)^2 + (x214 - x232)^2 + (x354 - x372)^2) + 1 / sqrt((x74
    - x93)^2 + (x214 - x233)^2 + (x354 - x373)^2) + 1 / sqrt((x74 - x94)^2 + (
    x214 - x234)^2 + (x354 - x374)^2) + 1 / sqrt((x74 - x95)^2 + (x214 - x235)^
    2 + (x354 - x375)^2) + 1 / sqrt((x74 - x96)^2 + (x214 - x236)^2 + (x354 -
    x376)^2) + 1 / sqrt((x74 - x97)^2 + (x214 - x237)^2 + (x354 - x377)^2) + 1
    / sqrt((x74 - x98)^2 + (x214 - x238)^2 + (x354 - x378)^2) + 1 / sqrt((x74
    - x99)^2 + (x214 - x239)^2 + (x354 - x379)^2) + 1 / sqrt((x74 - x100)^2 +
    (x214 - x240)^2 + (x354 - x380)^2) + 1 / sqrt((x74 - x101)^2 + (x214 - x241)
    ^2 + (x354 - x381)^2) + 1 / sqrt((x74 - x102)^2 + (x214 - x242)^2 + (x354
    - x382)^2) + 1 / sqrt((x74 - x103)^2 + (x214 - x243)^2 + (x354 - x383)^2)
    + 1 / sqrt((x74 - x104)^2 + (x214 - x244)^2 + (x354 - x384)^2) + 1 / sqrt(
    (x74 - x105)^2 + (x214 - x245)^2 + (x354 - x385)^2) + 1 / sqrt((x74 - x106)
    ^2 + (x214 - x246)^2 + (x354 - x386)^2) + 1 / sqrt((x74 - x107)^2 + (x214
    - x247)^2 + (x354 - x387)^2) + 1 / sqrt((x74 - x108)^2 + (x214 - x248)^2
    + (x354 - x388)^2) + 1 / sqrt((x74 - x109)^2 + (x214 - x249)^2 + (x354 -
    x389)^2) + 1 / sqrt((x74 - x110)^2 + (x214 - x250)^2 + (x354 - x390)^2) + 1
    / sqrt((x74 - x111)^2 + (x214 - x251)^2 + (x354 - x391)^2) + 1 / sqrt((x74
    - x112)^2 + (x214 - x252)^2 + (x354 - x392)^2) + 1 / sqrt((x74 - x113)^2
    + (x214 - x253)^2 + (x354 - x393)^2) + 1 / sqrt((x74 - x114)^2 + (x214 -
    x254)^2 + (x354 - x394)^2) + 1 / sqrt((x74 - x115)^2 + (x214 - x255)^2 + (
    x354 - x395)^2) + 1 / sqrt((x74 - x116)^2 + (x214 - x256)^2 + (x354 - x396)
    ^2) + 1 / sqrt((x74 - x117)^2 + (x214 - x257)^2 + (x354 - x397)^2) + 1 /
    sqrt((x74 - x118)^2 + (x214 - x258)^2 + (x354 - x398)^2) + 1 / sqrt((x74 -
    x119)^2 + (x214 - x259)^2 + (x354 - x399)^2) + 1 / sqrt((x74 - x120)^2 + (
    x214 - x260)^2 + (x354 - x400)^2) + 1 / sqrt((x74 - x121)^2 + (x214 - x261)
    ^2 + (x354 - x401)^2) + 1 / sqrt((x74 - x122)^2 + (x214 - x262)^2 + (x354
    - x402)^2) + 1 / sqrt((x74 - x123)^2 + (x214 - x263)^2 + (x354 - x403)^2)
    + 1 / sqrt((x74 - x124)^2 + (x214 - x264)^2 + (x354 - x404)^2) + 1 / sqrt(
    (x74 - x125)^2 + (x214 - x265)^2 + (x354 - x405)^2) + 1 / sqrt((x74 - x126)
    ^2 + (x214 - x266)^2 + (x354 - x406)^2) + 1 / sqrt((x74 - x127)^2 + (x214
    - x267)^2 + (x354 - x407)^2) + 1 / sqrt((x74 - x128)^2 + (x214 - x268)^2
    + (x354 - x408)^2) + 1 / sqrt((x74 - x129)^2 + (x214 - x269)^2 + (x354 -
    x409)^2) + 1 / sqrt((x74 - x130)^2 + (x214 - x270)^2 + (x354 - x410)^2) + 1
    / sqrt((x74 - x131)^2 + (x214 - x271)^2 + (x354 - x411)^2) + 1 / sqrt((x74
    - x132)^2 + (x214 - x272)^2 + (x354 - x412)^2) + 1 / sqrt((x74 - x133)^2
    + (x214 - x273)^2 + (x354 - x413)^2) + 1 / sqrt((x74 - x134)^2 + (x214 -
    x274)^2 + (x354 - x414)^2) + 1 / sqrt((x74 - x135)^2 + (x214 - x275)^2 + (
    x354 - x415)^2) + 1 / sqrt((x74 - x136)^2 + (x214 - x276)^2 + (x354 - x416)
    ^2) + 1 / sqrt((x74 - x137)^2 + (x214 - x277)^2 + (x354 - x417)^2) + 1 /
    sqrt((x74 - x138)^2 + (x214 - x278)^2 + (x354 - x418)^2) + 1 / sqrt((x74 -
    x139)^2 + (x214 - x279)^2 + (x354 - x419)^2) + 1 / sqrt((x74 - x140)^2 + (
    x214 - x280)^2 + (x354 - x420)^2) + 1 / sqrt((x75 - x76)^2 + (x215 - x216)^
    2 + (x355 - x356)^2) + 1 / sqrt((x75 - x77)^2 + (x215 - x217)^2 + (x355 -
    x357)^2) + 1 / sqrt((x75 - x78)^2 + (x215 - x218)^2 + (x355 - x358)^2) + 1
    / sqrt((x75 - x79)^2 + (x215 - x219)^2 + (x355 - x359)^2) + 1 / sqrt((x75
    - x80)^2 + (x215 - x220)^2 + (x355 - x360)^2) + 1 / sqrt((x75 - x81)^2 + (
    x215 - x221)^2 + (x355 - x361)^2) + 1 / sqrt((x75 - x82)^2 + (x215 - x222)^
    2 + (x355 - x362)^2) + 1 / sqrt((x75 - x83)^2 + (x215 - x223)^2 + (x355 -
    x363)^2) + 1 / sqrt((x75 - x84)^2 + (x215 - x224)^2 + (x355 - x364)^2) + 1
    / sqrt((x75 - x85)^2 + (x215 - x225)^2 + (x355 - x365)^2) + 1 / sqrt((x75
    - x86)^2 + (x215 - x226)^2 + (x355 - x366)^2) + 1 / sqrt((x75 - x87)^2 + (
    x215 - x227)^2 + (x355 - x367)^2) + 1 / sqrt((x75 - x88)^2 + (x215 - x228)^
    2 + (x355 - x368)^2) + 1 / sqrt((x75 - x89)^2 + (x215 - x229)^2 + (x355 -
    x369)^2) + 1 / sqrt((x75 - x90)^2 + (x215 - x230)^2 + (x355 - x370)^2) + 1
    / sqrt((x75 - x91)^2 + (x215 - x231)^2 + (x355 - x371)^2) + 1 / sqrt((x75
    - x92)^2 + (x215 - x232)^2 + (x355 - x372)^2) + 1 / sqrt((x75 - x93)^2 + (
    x215 - x233)^2 + (x355 - x373)^2) + 1 / sqrt((x75 - x94)^2 + (x215 - x234)^
    2 + (x355 - x374)^2) + 1 / sqrt((x75 - x95)^2 + (x215 - x235)^2 + (x355 -
    x375)^2) + 1 / sqrt((x75 - x96)^2 + (x215 - x236)^2 + (x355 - x376)^2) + 1
    / sqrt((x75 - x97)^2 + (x215 - x237)^2 + (x355 - x377)^2) + 1 / sqrt((x75
    - x98)^2 + (x215 - x238)^2 + (x355 - x378)^2) + 1 / sqrt((x75 - x99)^2 + (
    x215 - x239)^2 + (x355 - x379)^2) + 1 / sqrt((x75 - x100)^2 + (x215 - x240)
    ^2 + (x355 - x380)^2) + 1 / sqrt((x75 - x101)^2 + (x215 - x241)^2 + (x355
    - x381)^2) + 1 / sqrt((x75 - x102)^2 + (x215 - x242)^2 + (x355 - x382)^2)
    + 1 / sqrt((x75 - x103)^2 + (x215 - x243)^2 + (x355 - x383)^2) + 1 / sqrt(
    (x75 - x104)^2 + (x215 - x244)^2 + (x355 - x384)^2) + 1 / sqrt((x75 - x105)
    ^2 + (x215 - x245)^2 + (x355 - x385)^2) + 1 / sqrt((x75 - x106)^2 + (x215
    - x246)^2 + (x355 - x386)^2) + 1 / sqrt((x75 - x107)^2 + (x215 - x247)^2
    + (x355 - x387)^2) + 1 / sqrt((x75 - x108)^2 + (x215 - x248)^2 + (x355 -
    x388)^2) + 1 / sqrt((x75 - x109)^2 + (x215 - x249)^2 + (x355 - x389)^2) + 1
    / sqrt((x75 - x110)^2 + (x215 - x250)^2 + (x355 - x390)^2) + 1 / sqrt((x75
    - x111)^2 + (x215 - x251)^2 + (x355 - x391)^2) + 1 / sqrt((x75 - x112)^2
    + (x215 - x252)^2 + (x355 - x392)^2) + 1 / sqrt((x75 - x113)^2 + (x215 -
    x253)^2 + (x355 - x393)^2) + 1 / sqrt((x75 - x114)^2 + (x215 - x254)^2 + (
    x355 - x394)^2) + 1 / sqrt((x75 - x115)^2 + (x215 - x255)^2 + (x355 - x395)
    ^2) + 1 / sqrt((x75 - x116)^2 + (x215 - x256)^2 + (x355 - x396)^2) + 1 /
    sqrt((x75 - x117)^2 + (x215 - x257)^2 + (x355 - x397)^2) + 1 / sqrt((x75 -
    x118)^2 + (x215 - x258)^2 + (x355 - x398)^2) + 1 / sqrt((x75 - x119)^2 + (
    x215 - x259)^2 + (x355 - x399)^2) + 1 / sqrt((x75 - x120)^2 + (x215 - x260)
    ^2 + (x355 - x400)^2) + 1 / sqrt((x75 - x121)^2 + (x215 - x261)^2 + (x355
    - x401)^2) + 1 / sqrt((x75 - x122)^2 + (x215 - x262)^2 + (x355 - x402)^2)
    + 1 / sqrt((x75 - x123)^2 + (x215 - x263)^2 + (x355 - x403)^2) + 1 / sqrt(
    (x75 - x124)^2 + (x215 - x264)^2 + (x355 - x404)^2) + 1 / sqrt((x75 - x125)
    ^2 + (x215 - x265)^2 + (x355 - x405)^2) + 1 / sqrt((x75 - x126)^2 + (x215
    - x266)^2 + (x355 - x406)^2) + 1 / sqrt((x75 - x127)^2 + (x215 - x267)^2
    + (x355 - x407)^2) + 1 / sqrt((x75 - x128)^2 + (x215 - x268)^2 + (x355 -
    x408)^2) + 1 / sqrt((x75 - x129)^2 + (x215 - x269)^2 + (x355 - x409)^2) + 1
    / sqrt((x75 - x130)^2 + (x215 - x270)^2 + (x355 - x410)^2) + 1 / sqrt((x75
    - x131)^2 + (x215 - x271)^2 + (x355 - x411)^2) + 1 / sqrt((x75 - x132)^2
    + (x215 - x272)^2 + (x355 - x412)^2) + 1 / sqrt((x75 - x133)^2 + (x215 -
    x273)^2 + (x355 - x413)^2) + 1 / sqrt((x75 - x134)^2 + (x215 - x274)^2 + (
    x355 - x414)^2) + 1 / sqrt((x75 - x135)^2 + (x215 - x275)^2 + (x355 - x415)
    ^2) + 1 / sqrt((x75 - x136)^2 + (x215 - x276)^2 + (x355 - x416)^2) + 1 /
    sqrt((x75 - x137)^2 + (x215 - x277)^2 + (x355 - x417)^2) + 1 / sqrt((x75 -
    x138)^2 + (x215 - x278)^2 + (x355 - x418)^2) + 1 / sqrt((x75 - x139)^2 + (
    x215 - x279)^2 + (x355 - x419)^2) + 1 / sqrt((x75 - x140)^2 + (x215 - x280)
    ^2 + (x355 - x420)^2) + 1 / sqrt((x76 - x77)^2 + (x216 - x217)^2 + (x356 -
    x357)^2) + 1 / sqrt((x76 - x78)^2 + (x216 - x218)^2 + (x356 - x358)^2) + 1
    / sqrt((x76 - x79)^2 + (x216 - x219)^2 + (x356 - x359)^2) + 1 / sqrt((x76
    - x80)^2 + (x216 - x220)^2 + (x356 - x360)^2) + 1 / sqrt((x76 - x81)^2 + (
    x216 - x221)^2 + (x356 - x361)^2) + 1 / sqrt((x76 - x82)^2 + (x216 - x222)^
    2 + (x356 - x362)^2) + 1 / sqrt((x76 - x83)^2 + (x216 - x223)^2 + (x356 -
    x363)^2) + 1 / sqrt((x76 - x84)^2 + (x216 - x224)^2 + (x356 - x364)^2) + 1
    / sqrt((x76 - x85)^2 + (x216 - x225)^2 + (x356 - x365)^2) + 1 / sqrt((x76
    - x86)^2 + (x216 - x226)^2 + (x356 - x366)^2) + 1 / sqrt((x76 - x87)^2 + (
    x216 - x227)^2 + (x356 - x367)^2) + 1 / sqrt((x76 - x88)^2 + (x216 - x228)^
    2 + (x356 - x368)^2) + 1 / sqrt((x76 - x89)^2 + (x216 - x229)^2 + (x356 -
    x369)^2) + 1 / sqrt((x76 - x90)^2 + (x216 - x230)^2 + (x356 - x370)^2) + 1
    / sqrt((x76 - x91)^2 + (x216 - x231)^2 + (x356 - x371)^2) + 1 / sqrt((x76
    - x92)^2 + (x216 - x232)^2 + (x356 - x372)^2) + 1 / sqrt((x76 - x93)^2 + (
    x216 - x233)^2 + (x356 - x373)^2) + 1 / sqrt((x76 - x94)^2 + (x216 - x234)^
    2 + (x356 - x374)^2) + 1 / sqrt((x76 - x95)^2 + (x216 - x235)^2 + (x356 -
    x375)^2) + 1 / sqrt((x76 - x96)^2 + (x216 - x236)^2 + (x356 - x376)^2) + 1
    / sqrt((x76 - x97)^2 + (x216 - x237)^2 + (x356 - x377)^2) + 1 / sqrt((x76
    - x98)^2 + (x216 - x238)^2 + (x356 - x378)^2) + 1 / sqrt((x76 - x99)^2 + (
    x216 - x239)^2 + (x356 - x379)^2) + 1 / sqrt((x76 - x100)^2 + (x216 - x240)
    ^2 + (x356 - x380)^2) + 1 / sqrt((x76 - x101)^2 + (x216 - x241)^2 + (x356
    - x381)^2) + 1 / sqrt((x76 - x102)^2 + (x216 - x242)^2 + (x356 - x382)^2)
    + 1 / sqrt((x76 - x103)^2 + (x216 - x243)^2 + (x356 - x383)^2) + 1 / sqrt(
    (x76 - x104)^2 + (x216 - x244)^2 + (x356 - x384)^2) + 1 / sqrt((x76 - x105)
    ^2 + (x216 - x245)^2 + (x356 - x385)^2) + 1 / sqrt((x76 - x106)^2 + (x216
    - x246)^2 + (x356 - x386)^2) + 1 / sqrt((x76 - x107)^2 + (x216 - x247)^2
    + (x356 - x387)^2) + 1 / sqrt((x76 - x108)^2 + (x216 - x248)^2 + (x356 -
    x388)^2) + 1 / sqrt((x76 - x109)^2 + (x216 - x249)^2 + (x356 - x389)^2) + 1
    / sqrt((x76 - x110)^2 + (x216 - x250)^2 + (x356 - x390)^2) + 1 / sqrt((x76
    - x111)^2 + (x216 - x251)^2 + (x356 - x391)^2) + 1 / sqrt((x76 - x112)^2
    + (x216 - x252)^2 + (x356 - x392)^2) + 1 / sqrt((x76 - x113)^2 + (x216 -
    x253)^2 + (x356 - x393)^2) + 1 / sqrt((x76 - x114)^2 + (x216 - x254)^2 + (
    x356 - x394)^2) + 1 / sqrt((x76 - x115)^2 + (x216 - x255)^2 + (x356 - x395)
    ^2) + 1 / sqrt((x76 - x116)^2 + (x216 - x256)^2 + (x356 - x396)^2) + 1 /
    sqrt((x76 - x117)^2 + (x216 - x257)^2 + (x356 - x397)^2) + 1 / sqrt((x76 -
    x118)^2 + (x216 - x258)^2 + (x356 - x398)^2) + 1 / sqrt((x76 - x119)^2 + (
    x216 - x259)^2 + (x356 - x399)^2) + 1 / sqrt((x76 - x120)^2 + (x216 - x260)
    ^2 + (x356 - x400)^2) + 1 / sqrt((x76 - x121)^2 + (x216 - x261)^2 + (x356
    - x401)^2) + 1 / sqrt((x76 - x122)^2 + (x216 - x262)^2 + (x356 - x402)^2)
    + 1 / sqrt((x76 - x123)^2 + (x216 - x263)^2 + (x356 - x403)^2) + 1 / sqrt(
    (x76 - x124)^2 + (x216 - x264)^2 + (x356 - x404)^2) + 1 / sqrt((x76 - x125)
    ^2 + (x216 - x265)^2 + (x356 - x405)^2) + 1 / sqrt((x76 - x126)^2 + (x216
    - x266)^2 + (x356 - x406)^2) + 1 / sqrt((x76 - x127)^2 + (x216 - x267)^2
    + (x356 - x407)^2) + 1 / sqrt((x76 - x128)^2 + (x216 - x268)^2 + (x356 -
    x408)^2) + 1 / sqrt((x76 - x129)^2 + (x216 - x269)^2 + (x356 - x409)^2) + 1
    / sqrt((x76 - x130)^2 + (x216 - x270)^2 + (x356 - x410)^2) + 1 / sqrt((x76
    - x131)^2 + (x216 - x271)^2 + (x356 - x411)^2) + 1 / sqrt((x76 - x132)^2
    + (x216 - x272)^2 + (x356 - x412)^2) + 1 / sqrt((x76 - x133)^2 + (x216 -
    x273)^2 + (x356 - x413)^2) + 1 / sqrt((x76 - x134)^2 + (x216 - x274)^2 + (
    x356 - x414)^2) + 1 / sqrt((x76 - x135)^2 + (x216 - x275)^2 + (x356 - x415)
    ^2) + 1 / sqrt((x76 - x136)^2 + (x216 - x276)^2 + (x356 - x416)^2) + 1 /
    sqrt((x76 - x137)^2 + (x216 - x277)^2 + (x356 - x417)^2) + 1 / sqrt((x76 -
    x138)^2 + (x216 - x278)^2 + (x356 - x418)^2) + 1 / sqrt((x76 - x139)^2 + (
    x216 - x279)^2 + (x356 - x419)^2) + 1 / sqrt((x76 - x140)^2 + (x216 - x280)
    ^2 + (x356 - x420)^2) + 1 / sqrt((x77 - x78)^2 + (x217 - x218)^2 + (x357 -
    x358)^2) + 1 / sqrt((x77 - x79)^2 + (x217 - x219)^2 + (x357 - x359)^2) + 1
    / sqrt((x77 - x80)^2 + (x217 - x220)^2 + (x357 - x360)^2) + 1 / sqrt((x77
    - x81)^2 + (x217 - x221)^2 + (x357 - x361)^2) + 1 / sqrt((x77 - x82)^2 + (
    x217 - x222)^2 + (x357 - x362)^2) + 1 / sqrt((x77 - x83)^2 + (x217 - x223)^
    2 + (x357 - x363)^2) + 1 / sqrt((x77 - x84)^2 + (x217 - x224)^2 + (x357 -
    x364)^2) + 1 / sqrt((x77 - x85)^2 + (x217 - x225)^2 + (x357 - x365)^2) + 1
    / sqrt((x77 - x86)^2 + (x217 - x226)^2 + (x357 - x366)^2) + 1 / sqrt((x77
    - x87)^2 + (x217 - x227)^2 + (x357 - x367)^2) + 1 / sqrt((x77 - x88)^2 + (
    x217 - x228)^2 + (x357 - x368)^2) + 1 / sqrt((x77 - x89)^2 + (x217 - x229)^
    2 + (x357 - x369)^2) + 1 / sqrt((x77 - x90)^2 + (x217 - x230)^2 + (x357 -
    x370)^2) + 1 / sqrt((x77 - x91)^2 + (x217 - x231)^2 + (x357 - x371)^2) + 1
    / sqrt((x77 - x92)^2 + (x217 - x232)^2 + (x357 - x372)^2) + 1 / sqrt((x77
    - x93)^2 + (x217 - x233)^2 + (x357 - x373)^2) + 1 / sqrt((x77 - x94)^2 + (
    x217 - x234)^2 + (x357 - x374)^2) + 1 / sqrt((x77 - x95)^2 + (x217 - x235)^
    2 + (x357 - x375)^2) + 1 / sqrt((x77 - x96)^2 + (x217 - x236)^2 + (x357 -
    x376)^2) + 1 / sqrt((x77 - x97)^2 + (x217 - x237)^2 + (x357 - x377)^2) + 1
    / sqrt((x77 - x98)^2 + (x217 - x238)^2 + (x357 - x378)^2) + 1 / sqrt((x77
    - x99)^2 + (x217 - x239)^2 + (x357 - x379)^2) + 1 / sqrt((x77 - x100)^2 +
    (x217 - x240)^2 + (x357 - x380)^2) + 1 / sqrt((x77 - x101)^2 + (x217 - x241)
    ^2 + (x357 - x381)^2) + 1 / sqrt((x77 - x102)^2 + (x217 - x242)^2 + (x357
    - x382)^2) + 1 / sqrt((x77 - x103)^2 + (x217 - x243)^2 + (x357 - x383)^2)
    + 1 / sqrt((x77 - x104)^2 + (x217 - x244)^2 + (x357 - x384)^2) + 1 / sqrt(
    (x77 - x105)^2 + (x217 - x245)^2 + (x357 - x385)^2) + 1 / sqrt((x77 - x106)
    ^2 + (x217 - x246)^2 + (x357 - x386)^2) + 1 / sqrt((x77 - x107)^2 + (x217
    - x247)^2 + (x357 - x387)^2) + 1 / sqrt((x77 - x108)^2 + (x217 - x248)^2
    + (x357 - x388)^2) + 1 / sqrt((x77 - x109)^2 + (x217 - x249)^2 + (x357 -
    x389)^2) + 1 / sqrt((x77 - x110)^2 + (x217 - x250)^2 + (x357 - x390)^2) + 1
    / sqrt((x77 - x111)^2 + (x217 - x251)^2 + (x357 - x391)^2) + 1 / sqrt((x77
    - x112)^2 + (x217 - x252)^2 + (x357 - x392)^2) + 1 / sqrt((x77 - x113)^2
    + (x217 - x253)^2 + (x357 - x393)^2) + 1 / sqrt((x77 - x114)^2 + (x217 -
    x254)^2 + (x357 - x394)^2) + 1 / sqrt((x77 - x115)^2 + (x217 - x255)^2 + (
    x357 - x395)^2) + 1 / sqrt((x77 - x116)^2 + (x217 - x256)^2 + (x357 - x396)
    ^2) + 1 / sqrt((x77 - x117)^2 + (x217 - x257)^2 + (x357 - x397)^2) + 1 /
    sqrt((x77 - x118)^2 + (x217 - x258)^2 + (x357 - x398)^2) + 1 / sqrt((x77 -
    x119)^2 + (x217 - x259)^2 + (x357 - x399)^2) + 1 / sqrt((x77 - x120)^2 + (
    x217 - x260)^2 + (x357 - x400)^2) + 1 / sqrt((x77 - x121)^2 + (x217 - x261)
    ^2 + (x357 - x401)^2) + 1 / sqrt((x77 - x122)^2 + (x217 - x262)^2 + (x357
    - x402)^2) + 1 / sqrt((x77 - x123)^2 + (x217 - x263)^2 + (x357 - x403)^2)
    + 1 / sqrt((x77 - x124)^2 + (x217 - x264)^2 + (x357 - x404)^2) + 1 / sqrt(
    (x77 - x125)^2 + (x217 - x265)^2 + (x357 - x405)^2) + 1 / sqrt((x77 - x126)
    ^2 + (x217 - x266)^2 + (x357 - x406)^2) + 1 / sqrt((x77 - x127)^2 + (x217
    - x267)^2 + (x357 - x407)^2) + 1 / sqrt((x77 - x128)^2 + (x217 - x268)^2
    + (x357 - x408)^2) + 1 / sqrt((x77 - x129)^2 + (x217 - x269)^2 + (x357 -
    x409)^2) + 1 / sqrt((x77 - x130)^2 + (x217 - x270)^2 + (x357 - x410)^2) + 1
    / sqrt((x77 - x131)^2 + (x217 - x271)^2 + (x357 - x411)^2) + 1 / sqrt((x77
    - x132)^2 + (x217 - x272)^2 + (x357 - x412)^2) + 1 / sqrt((x77 - x133)^2
    + (x217 - x273)^2 + (x357 - x413)^2) + 1 / sqrt((x77 - x134)^2 + (x217 -
    x274)^2 + (x357 - x414)^2) + 1 / sqrt((x77 - x135)^2 + (x217 - x275)^2 + (
    x357 - x415)^2) + 1 / sqrt((x77 - x136)^2 + (x217 - x276)^2 + (x357 - x416)
    ^2) + 1 / sqrt((x77 - x137)^2 + (x217 - x277)^2 + (x357 - x417)^2) + 1 /
    sqrt((x77 - x138)^2 + (x217 - x278)^2 + (x357 - x418)^2) + 1 / sqrt((x77 -
    x139)^2 + (x217 - x279)^2 + (x357 - x419)^2) + 1 / sqrt((x77 - x140)^2 + (
    x217 - x280)^2 + (x357 - x420)^2) + 1 / sqrt((x78 - x79)^2 + (x218 - x219)^
    2 + (x358 - x359)^2) + 1 / sqrt((x78 - x80)^2 + (x218 - x220)^2 + (x358 -
    x360)^2) + 1 / sqrt((x78 - x81)^2 + (x218 - x221)^2 + (x358 - x361)^2) + 1
    / sqrt((x78 - x82)^2 + (x218 - x222)^2 + (x358 - x362)^2) + 1 / sqrt((x78
    - x83)^2 + (x218 - x223)^2 + (x358 - x363)^2) + 1 / sqrt((x78 - x84)^2 + (
    x218 - x224)^2 + (x358 - x364)^2) + 1 / sqrt((x78 - x85)^2 + (x218 - x225)^
    2 + (x358 - x365)^2) + 1 / sqrt((x78 - x86)^2 + (x218 - x226)^2 + (x358 -
    x366)^2) + 1 / sqrt((x78 - x87)^2 + (x218 - x227)^2 + (x358 - x367)^2) + 1
    / sqrt((x78 - x88)^2 + (x218 - x228)^2 + (x358 - x368)^2) + 1 / sqrt((x78
    - x89)^2 + (x218 - x229)^2 + (x358 - x369)^2) + 1 / sqrt((x78 - x90)^2 + (
    x218 - x230)^2 + (x358 - x370)^2) + 1 / sqrt((x78 - x91)^2 + (x218 - x231)^
    2 + (x358 - x371)^2) + 1 / sqrt((x78 - x92)^2 + (x218 - x232)^2 + (x358 -
    x372)^2) + 1 / sqrt((x78 - x93)^2 + (x218 - x233)^2 + (x358 - x373)^2) + 1
    / sqrt((x78 - x94)^2 + (x218 - x234)^2 + (x358 - x374)^2) + 1 / sqrt((x78
    - x95)^2 + (x218 - x235)^2 + (x358 - x375)^2) + 1 / sqrt((x78 - x96)^2 + (
    x218 - x236)^2 + (x358 - x376)^2) + 1 / sqrt((x78 - x97)^2 + (x218 - x237)^
    2 + (x358 - x377)^2) + 1 / sqrt((x78 - x98)^2 + (x218 - x238)^2 + (x358 -
    x378)^2) + 1 / sqrt((x78 - x99)^2 + (x218 - x239)^2 + (x358 - x379)^2) + 1
    / sqrt((x78 - x100)^2 + (x218 - x240)^2 + (x358 - x380)^2) + 1 / sqrt((x78
    - x101)^2 + (x218 - x241)^2 + (x358 - x381)^2) + 1 / sqrt((x78 - x102)^2
    + (x218 - x242)^2 + (x358 - x382)^2) + 1 / sqrt((x78 - x103)^2 + (x218 -
    x243)^2 + (x358 - x383)^2) + 1 / sqrt((x78 - x104)^2 + (x218 - x244)^2 + (
    x358 - x384)^2) + 1 / sqrt((x78 - x105)^2 + (x218 - x245)^2 + (x358 - x385)
    ^2) + 1 / sqrt((x78 - x106)^2 + (x218 - x246)^2 + (x358 - x386)^2) + 1 /
    sqrt((x78 - x107)^2 + (x218 - x247)^2 + (x358 - x387)^2) + 1 / sqrt((x78 -
    x108)^2 + (x218 - x248)^2 + (x358 - x388)^2) + 1 / sqrt((x78 - x109)^2 + (
    x218 - x249)^2 + (x358 - x389)^2) + 1 / sqrt((x78 - x110)^2 + (x218 - x250)
    ^2 + (x358 - x390)^2) + 1 / sqrt((x78 - x111)^2 + (x218 - x251)^2 + (x358
    - x391)^2) + 1 / sqrt((x78 - x112)^2 + (x218 - x252)^2 + (x358 - x392)^2)
    + 1 / sqrt((x78 - x113)^2 + (x218 - x253)^2 + (x358 - x393)^2) + 1 / sqrt(
    (x78 - x114)^2 + (x218 - x254)^2 + (x358 - x394)^2) + 1 / sqrt((x78 - x115)
    ^2 + (x218 - x255)^2 + (x358 - x395)^2) + 1 / sqrt((x78 - x116)^2 + (x218
    - x256)^2 + (x358 - x396)^2) + 1 / sqrt((x78 - x117)^2 + (x218 - x257)^2
    + (x358 - x397)^2) + 1 / sqrt((x78 - x118)^2 + (x218 - x258)^2 + (x358 -
    x398)^2) + 1 / sqrt((x78 - x119)^2 + (x218 - x259)^2 + (x358 - x399)^2) + 1
    / sqrt((x78 - x120)^2 + (x218 - x260)^2 + (x358 - x400)^2) + 1 / sqrt((x78
    - x121)^2 + (x218 - x261)^2 + (x358 - x401)^2) + 1 / sqrt((x78 - x122)^2
    + (x218 - x262)^2 + (x358 - x402)^2) + 1 / sqrt((x78 - x123)^2 + (x218 -
    x263)^2 + (x358 - x403)^2) + 1 / sqrt((x78 - x124)^2 + (x218 - x264)^2 + (
    x358 - x404)^2) + 1 / sqrt((x78 - x125)^2 + (x218 - x265)^2 + (x358 - x405)
    ^2) + 1 / sqrt((x78 - x126)^2 + (x218 - x266)^2 + (x358 - x406)^2) + 1 /
    sqrt((x78 - x127)^2 + (x218 - x267)^2 + (x358 - x407)^2) + 1 / sqrt((x78 -
    x128)^2 + (x218 - x268)^2 + (x358 - x408)^2) + 1 / sqrt((x78 - x129)^2 + (
    x218 - x269)^2 + (x358 - x409)^2) + 1 / sqrt((x78 - x130)^2 + (x218 - x270)
    ^2 + (x358 - x410)^2) + 1 / sqrt((x78 - x131)^2 + (x218 - x271)^2 + (x358
    - x411)^2) + 1 / sqrt((x78 - x132)^2 + (x218 - x272)^2 + (x358 - x412)^2)
    + 1 / sqrt((x78 - x133)^2 + (x218 - x273)^2 + (x358 - x413)^2) + 1 / sqrt(
    (x78 - x134)^2 + (x218 - x274)^2 + (x358 - x414)^2) + 1 / sqrt((x78 - x135)
    ^2 + (x218 - x275)^2 + (x358 - x415)^2) + 1 / sqrt((x78 - x136)^2 + (x218
    - x276)^2 + (x358 - x416)^2) + 1 / sqrt((x78 - x137)^2 + (x218 - x277)^2
    + (x358 - x417)^2) + 1 / sqrt((x78 - x138)^2 + (x218 - x278)^2 + (x358 -
    x418)^2) + 1 / sqrt((x78 - x139)^2 + (x218 - x279)^2 + (x358 - x419)^2) + 1
    / sqrt((x78 - x140)^2 + (x218 - x280)^2 + (x358 - x420)^2) + 1 / sqrt((x79
    - x80)^2 + (x219 - x220)^2 + (x359 - x360)^2) + 1 / sqrt((x79 - x81)^2 + (
    x219 - x221)^2 + (x359 - x361)^2) + 1 / sqrt((x79 - x82)^2 + (x219 - x222)^
    2 + (x359 - x362)^2) + 1 / sqrt((x79 - x83)^2 + (x219 - x223)^2 + (x359 -
    x363)^2) + 1 / sqrt((x79 - x84)^2 + (x219 - x224)^2 + (x359 - x364)^2) + 1
    / sqrt((x79 - x85)^2 + (x219 - x225)^2 + (x359 - x365)^2) + 1 / sqrt((x79
    - x86)^2 + (x219 - x226)^2 + (x359 - x366)^2) + 1 / sqrt((x79 - x87)^2 + (
    x219 - x227)^2 + (x359 - x367)^2) + 1 / sqrt((x79 - x88)^2 + (x219 - x228)^
    2 + (x359 - x368)^2) + 1 / sqrt((x79 - x89)^2 + (x219 - x229)^2 + (x359 -
    x369)^2) + 1 / sqrt((x79 - x90)^2 + (x219 - x230)^2 + (x359 - x370)^2) + 1
    / sqrt((x79 - x91)^2 + (x219 - x231)^2 + (x359 - x371)^2) + 1 / sqrt((x79
    - x92)^2 + (x219 - x232)^2 + (x359 - x372)^2) + 1 / sqrt((x79 - x93)^2 + (
    x219 - x233)^2 + (x359 - x373)^2) + 1 / sqrt((x79 - x94)^2 + (x219 - x234)^
    2 + (x359 - x374)^2) + 1 / sqrt((x79 - x95)^2 + (x219 - x235)^2 + (x359 -
    x375)^2) + 1 / sqrt((x79 - x96)^2 + (x219 - x236)^2 + (x359 - x376)^2) + 1
    / sqrt((x79 - x97)^2 + (x219 - x237)^2 + (x359 - x377)^2) + 1 / sqrt((x79
    - x98)^2 + (x219 - x238)^2 + (x359 - x378)^2) + 1 / sqrt((x79 - x99)^2 + (
    x219 - x239)^2 + (x359 - x379)^2) + 1 / sqrt((x79 - x100)^2 + (x219 - x240)
    ^2 + (x359 - x380)^2) + 1 / sqrt((x79 - x101)^2 + (x219 - x241)^2 + (x359
    - x381)^2) + 1 / sqrt((x79 - x102)^2 + (x219 - x242)^2 + (x359 - x382)^2)
    + 1 / sqrt((x79 - x103)^2 + (x219 - x243)^2 + (x359 - x383)^2) + 1 / sqrt(
    (x79 - x104)^2 + (x219 - x244)^2 + (x359 - x384)^2) + 1 / sqrt((x79 - x105)
    ^2 + (x219 - x245)^2 + (x359 - x385)^2) + 1 / sqrt((x79 - x106)^2 + (x219
    - x246)^2 + (x359 - x386)^2) + 1 / sqrt((x79 - x107)^2 + (x219 - x247)^2
    + (x359 - x387)^2) + 1 / sqrt((x79 - x108)^2 + (x219 - x248)^2 + (x359 -
    x388)^2) + 1 / sqrt((x79 - x109)^2 + (x219 - x249)^2 + (x359 - x389)^2) + 1
    / sqrt((x79 - x110)^2 + (x219 - x250)^2 + (x359 - x390)^2) + 1 / sqrt((x79
    - x111)^2 + (x219 - x251)^2 + (x359 - x391)^2) + 1 / sqrt((x79 - x112)^2
    + (x219 - x252)^2 + (x359 - x392)^2) + 1 / sqrt((x79 - x113)^2 + (x219 -
    x253)^2 + (x359 - x393)^2) + 1 / sqrt((x79 - x114)^2 + (x219 - x254)^2 + (
    x359 - x394)^2) + 1 / sqrt((x79 - x115)^2 + (x219 - x255)^2 + (x359 - x395)
    ^2) + 1 / sqrt((x79 - x116)^2 + (x219 - x256)^2 + (x359 - x396)^2) + 1 /
    sqrt((x79 - x117)^2 + (x219 - x257)^2 + (x359 - x397)^2) + 1 / sqrt((x79 -
    x118)^2 + (x219 - x258)^2 + (x359 - x398)^2) + 1 / sqrt((x79 - x119)^2 + (
    x219 - x259)^2 + (x359 - x399)^2) + 1 / sqrt((x79 - x120)^2 + (x219 - x260)
    ^2 + (x359 - x400)^2) + 1 / sqrt((x79 - x121)^2 + (x219 - x261)^2 + (x359
    - x401)^2) + 1 / sqrt((x79 - x122)^2 + (x219 - x262)^2 + (x359 - x402)^2)
    + 1 / sqrt((x79 - x123)^2 + (x219 - x263)^2 + (x359 - x403)^2) + 1 / sqrt(
    (x79 - x124)^2 + (x219 - x264)^2 + (x359 - x404)^2) + 1 / sqrt((x79 - x125)
    ^2 + (x219 - x265)^2 + (x359 - x405)^2) + 1 / sqrt((x79 - x126)^2 + (x219
    - x266)^2 + (x359 - x406)^2) + 1 / sqrt((x79 - x127)^2 + (x219 - x267)^2
    + (x359 - x407)^2) + 1 / sqrt((x79 - x128)^2 + (x219 - x268)^2 + (x359 -
    x408)^2) + 1 / sqrt((x79 - x129)^2 + (x219 - x269)^2 + (x359 - x409)^2) + 1
    / sqrt((x79 - x130)^2 + (x219 - x270)^2 + (x359 - x410)^2) + 1 / sqrt((x79
    - x131)^2 + (x219 - x271)^2 + (x359 - x411)^2) + 1 / sqrt((x79 - x132)^2
    + (x219 - x272)^2 + (x359 - x412)^2) + 1 / sqrt((x79 - x133)^2 + (x219 -
    x273)^2 + (x359 - x413)^2) + 1 / sqrt((x79 - x134)^2 + (x219 - x274)^2 + (
    x359 - x414)^2) + 1 / sqrt((x79 - x135)^2 + (x219 - x275)^2 + (x359 - x415)
    ^2) + 1 / sqrt((x79 - x136)^2 + (x219 - x276)^2 + (x359 - x416)^2) + 1 /
    sqrt((x79 - x137)^2 + (x219 - x277)^2 + (x359 - x417)^2) + 1 / sqrt((x79 -
    x138)^2 + (x219 - x278)^2 + (x359 - x418)^2) + 1 / sqrt((x79 - x139)^2 + (
    x219 - x279)^2 + (x359 - x419)^2) + 1 / sqrt((x79 - x140)^2 + (x219 - x280)
    ^2 + (x359 - x420)^2) + 1 / sqrt((x80 - x81)^2 + (x220 - x221)^2 + (x360 -
    x361)^2) + 1 / sqrt((x80 - x82)^2 + (x220 - x222)^2 + (x360 - x362)^2) + 1
    / sqrt((x80 - x83)^2 + (x220 - x223)^2 + (x360 - x363)^2) + 1 / sqrt((x80
    - x84)^2 + (x220 - x224)^2 + (x360 - x364)^2) + 1 / sqrt((x80 - x85)^2 + (
    x220 - x225)^2 + (x360 - x365)^2) + 1 / sqrt((x80 - x86)^2 + (x220 - x226)^
    2 + (x360 - x366)^2) + 1 / sqrt((x80 - x87)^2 + (x220 - x227)^2 + (x360 -
    x367)^2) + 1 / sqrt((x80 - x88)^2 + (x220 - x228)^2 + (x360 - x368)^2) + 1
    / sqrt((x80 - x89)^2 + (x220 - x229)^2 + (x360 - x369)^2) + 1 / sqrt((x80
    - x90)^2 + (x220 - x230)^2 + (x360 - x370)^2) + 1 / sqrt((x80 - x91)^2 + (
    x220 - x231)^2 + (x360 - x371)^2) + 1 / sqrt((x80 - x92)^2 + (x220 - x232)^
    2 + (x360 - x372)^2) + 1 / sqrt((x80 - x93)^2 + (x220 - x233)^2 + (x360 -
    x373)^2) + 1 / sqrt((x80 - x94)^2 + (x220 - x234)^2 + (x360 - x374)^2) + 1
    / sqrt((x80 - x95)^2 + (x220 - x235)^2 + (x360 - x375)^2) + 1 / sqrt((x80
    - x96)^2 + (x220 - x236)^2 + (x360 - x376)^2) + 1 / sqrt((x80 - x97)^2 + (
    x220 - x237)^2 + (x360 - x377)^2) + 1 / sqrt((x80 - x98)^2 + (x220 - x238)^
    2 + (x360 - x378)^2) + 1 / sqrt((x80 - x99)^2 + (x220 - x239)^2 + (x360 -
    x379)^2) + 1 / sqrt((x80 - x100)^2 + (x220 - x240)^2 + (x360 - x380)^2) + 1
    / sqrt((x80 - x101)^2 + (x220 - x241)^2 + (x360 - x381)^2) + 1 / sqrt((x80
    - x102)^2 + (x220 - x242)^2 + (x360 - x382)^2) + 1 / sqrt((x80 - x103)^2
    + (x220 - x243)^2 + (x360 - x383)^2) + 1 / sqrt((x80 - x104)^2 + (x220 -
    x244)^2 + (x360 - x384)^2) + 1 / sqrt((x80 - x105)^2 + (x220 - x245)^2 + (
    x360 - x385)^2) + 1 / sqrt((x80 - x106)^2 + (x220 - x246)^2 + (x360 - x386)
    ^2) + 1 / sqrt((x80 - x107)^2 + (x220 - x247)^2 + (x360 - x387)^2) + 1 /
    sqrt((x80 - x108)^2 + (x220 - x248)^2 + (x360 - x388)^2) + 1 / sqrt((x80 -
    x109)^2 + (x220 - x249)^2 + (x360 - x389)^2) + 1 / sqrt((x80 - x110)^2 + (
    x220 - x250)^2 + (x360 - x390)^2) + 1 / sqrt((x80 - x111)^2 + (x220 - x251)
    ^2 + (x360 - x391)^2) + 1 / sqrt((x80 - x112)^2 + (x220 - x252)^2 + (x360
    - x392)^2) + 1 / sqrt((x80 - x113)^2 + (x220 - x253)^2 + (x360 - x393)^2)
    + 1 / sqrt((x80 - x114)^2 + (x220 - x254)^2 + (x360 - x394)^2) + 1 / sqrt(
    (x80 - x115)^2 + (x220 - x255)^2 + (x360 - x395)^2) + 1 / sqrt((x80 - x116)
    ^2 + (x220 - x256)^2 + (x360 - x396)^2) + 1 / sqrt((x80 - x117)^2 + (x220
    - x257)^2 + (x360 - x397)^2) + 1 / sqrt((x80 - x118)^2 + (x220 - x258)^2
    + (x360 - x398)^2) + 1 / sqrt((x80 - x119)^2 + (x220 - x259)^2 + (x360 -
    x399)^2) + 1 / sqrt((x80 - x120)^2 + (x220 - x260)^2 + (x360 - x400)^2) + 1
    / sqrt((x80 - x121)^2 + (x220 - x261)^2 + (x360 - x401)^2) + 1 / sqrt((x80
    - x122)^2 + (x220 - x262)^2 + (x360 - x402)^2) + 1 / sqrt((x80 - x123)^2
    + (x220 - x263)^2 + (x360 - x403)^2) + 1 / sqrt((x80 - x124)^2 + (x220 -
    x264)^2 + (x360 - x404)^2) + 1 / sqrt((x80 - x125)^2 + (x220 - x265)^2 + (
    x360 - x405)^2) + 1 / sqrt((x80 - x126)^2 + (x220 - x266)^2 + (x360 - x406)
    ^2) + 1 / sqrt((x80 - x127)^2 + (x220 - x267)^2 + (x360 - x407)^2) + 1 /
    sqrt((x80 - x128)^2 + (x220 - x268)^2 + (x360 - x408)^2) + 1 / sqrt((x80 -
    x129)^2 + (x220 - x269)^2 + (x360 - x409)^2) + 1 / sqrt((x80 - x130)^2 + (
    x220 - x270)^2 + (x360 - x410)^2) + 1 / sqrt((x80 - x131)^2 + (x220 - x271)
    ^2 + (x360 - x411)^2) + 1 / sqrt((x80 - x132)^2 + (x220 - x272)^2 + (x360
    - x412)^2) + 1 / sqrt((x80 - x133)^2 + (x220 - x273)^2 + (x360 - x413)^2)
    + 1 / sqrt((x80 - x134)^2 + (x220 - x274)^2 + (x360 - x414)^2) + 1 / sqrt(
    (x80 - x135)^2 + (x220 - x275)^2 + (x360 - x415)^2) + 1 / sqrt((x80 - x136)
    ^2 + (x220 - x276)^2 + (x360 - x416)^2) + 1 / sqrt((x80 - x137)^2 + (x220
    - x277)^2 + (x360 - x417)^2) + 1 / sqrt((x80 - x138)^2 + (x220 - x278)^2
    + (x360 - x418)^2) + 1 / sqrt((x80 - x139)^2 + (x220 - x279)^2 + (x360 -
    x419)^2) + 1 / sqrt((x80 - x140)^2 + (x220 - x280)^2 + (x360 - x420)^2) + 1
    / sqrt((x81 - x82)^2 + (x221 - x222)^2 + (x361 - x362)^2) + 1 / sqrt((x81
    - x83)^2 + (x221 - x223)^2 + (x361 - x363)^2) + 1 / sqrt((x81 - x84)^2 + (
    x221 - x224)^2 + (x361 - x364)^2) + 1 / sqrt((x81 - x85)^2 + (x221 - x225)^
    2 + (x361 - x365)^2) + 1 / sqrt((x81 - x86)^2 + (x221 - x226)^2 + (x361 -
    x366)^2) + 1 / sqrt((x81 - x87)^2 + (x221 - x227)^2 + (x361 - x367)^2) + 1
    / sqrt((x81 - x88)^2 + (x221 - x228)^2 + (x361 - x368)^2) + 1 / sqrt((x81
    - x89)^2 + (x221 - x229)^2 + (x361 - x369)^2) + 1 / sqrt((x81 - x90)^2 + (
    x221 - x230)^2 + (x361 - x370)^2) + 1 / sqrt((x81 - x91)^2 + (x221 - x231)^
    2 + (x361 - x371)^2) + 1 / sqrt((x81 - x92)^2 + (x221 - x232)^2 + (x361 -
    x372)^2) + 1 / sqrt((x81 - x93)^2 + (x221 - x233)^2 + (x361 - x373)^2) + 1
    / sqrt((x81 - x94)^2 + (x221 - x234)^2 + (x361 - x374)^2) + 1 / sqrt((x81
    - x95)^2 + (x221 - x235)^2 + (x361 - x375)^2) + 1 / sqrt((x81 - x96)^2 + (
    x221 - x236)^2 + (x361 - x376)^2) + 1 / sqrt((x81 - x97)^2 + (x221 - x237)^
    2 + (x361 - x377)^2) + 1 / sqrt((x81 - x98)^2 + (x221 - x238)^2 + (x361 -
    x378)^2) + 1 / sqrt((x81 - x99)^2 + (x221 - x239)^2 + (x361 - x379)^2) + 1
    / sqrt((x81 - x100)^2 + (x221 - x240)^2 + (x361 - x380)^2) + 1 / sqrt((x81
    - x101)^2 + (x221 - x241)^2 + (x361 - x381)^2) + 1 / sqrt((x81 - x102)^2
    + (x221 - x242)^2 + (x361 - x382)^2) + 1 / sqrt((x81 - x103)^2 + (x221 -
    x243)^2 + (x361 - x383)^2) + 1 / sqrt((x81 - x104)^2 + (x221 - x244)^2 + (
    x361 - x384)^2) + 1 / sqrt((x81 - x105)^2 + (x221 - x245)^2 + (x361 - x385)
    ^2) + 1 / sqrt((x81 - x106)^2 + (x221 - x246)^2 + (x361 - x386)^2) + 1 /
    sqrt((x81 - x107)^2 + (x221 - x247)^2 + (x361 - x387)^2) + 1 / sqrt((x81 -
    x108)^2 + (x221 - x248)^2 + (x361 - x388)^2) + 1 / sqrt((x81 - x109)^2 + (
    x221 - x249)^2 + (x361 - x389)^2) + 1 / sqrt((x81 - x110)^2 + (x221 - x250)
    ^2 + (x361 - x390)^2) + 1 / sqrt((x81 - x111)^2 + (x221 - x251)^2 + (x361
    - x391)^2) + 1 / sqrt((x81 - x112)^2 + (x221 - x252)^2 + (x361 - x392)^2)
    + 1 / sqrt((x81 - x113)^2 + (x221 - x253)^2 + (x361 - x393)^2) + 1 / sqrt(
    (x81 - x114)^2 + (x221 - x254)^2 + (x361 - x394)^2) + 1 / sqrt((x81 - x115)
    ^2 + (x221 - x255)^2 + (x361 - x395)^2) + 1 / sqrt((x81 - x116)^2 + (x221
    - x256)^2 + (x361 - x396)^2) + 1 / sqrt((x81 - x117)^2 + (x221 - x257)^2
    + (x361 - x397)^2) + 1 / sqrt((x81 - x118)^2 + (x221 - x258)^2 + (x361 -
    x398)^2) + 1 / sqrt((x81 - x119)^2 + (x221 - x259)^2 + (x361 - x399)^2) + 1
    / sqrt((x81 - x120)^2 + (x221 - x260)^2 + (x361 - x400)^2) + 1 / sqrt((x81
    - x121)^2 + (x221 - x261)^2 + (x361 - x401)^2) + 1 / sqrt((x81 - x122)^2
    + (x221 - x262)^2 + (x361 - x402)^2) + 1 / sqrt((x81 - x123)^2 + (x221 -
    x263)^2 + (x361 - x403)^2) + 1 / sqrt((x81 - x124)^2 + (x221 - x264)^2 + (
    x361 - x404)^2) + 1 / sqrt((x81 - x125)^2 + (x221 - x265)^2 + (x361 - x405)
    ^2) + 1 / sqrt((x81 - x126)^2 + (x221 - x266)^2 + (x361 - x406)^2) + 1 /
    sqrt((x81 - x127)^2 + (x221 - x267)^2 + (x361 - x407)^2) + 1 / sqrt((x81 -
    x128)^2 + (x221 - x268)^2 + (x361 - x408)^2) + 1 / sqrt((x81 - x129)^2 + (
    x221 - x269)^2 + (x361 - x409)^2) + 1 / sqrt((x81 - x130)^2 + (x221 - x270)
    ^2 + (x361 - x410)^2) + 1 / sqrt((x81 - x131)^2 + (x221 - x271)^2 + (x361
    - x411)^2) + 1 / sqrt((x81 - x132)^2 + (x221 - x272)^2 + (x361 - x412)^2)
    + 1 / sqrt((x81 - x133)^2 + (x221 - x273)^2 + (x361 - x413)^2) + 1 / sqrt(
    (x81 - x134)^2 + (x221 - x274)^2 + (x361 - x414)^2) + 1 / sqrt((x81 - x135)
    ^2 + (x221 - x275)^2 + (x361 - x415)^2) + 1 / sqrt((x81 - x136)^2 + (x221
    - x276)^2 + (x361 - x416)^2) + 1 / sqrt((x81 - x137)^2 + (x221 - x277)^2
    + (x361 - x417)^2) + 1 / sqrt((x81 - x138)^2 + (x221 - x278)^2 + (x361 -
    x418)^2) + 1 / sqrt((x81 - x139)^2 + (x221 - x279)^2 + (x361 - x419)^2) + 1
    / sqrt((x81 - x140)^2 + (x221 - x280)^2 + (x361 - x420)^2) + 1 / sqrt((x82
    - x83)^2 + (x222 - x223)^2 + (x362 - x363)^2) + 1 / sqrt((x82 - x84)^2 + (
    x222 - x224)^2 + (x362 - x364)^2) + 1 / sqrt((x82 - x85)^2 + (x222 - x225)^
    2 + (x362 - x365)^2) + 1 / sqrt((x82 - x86)^2 + (x222 - x226)^2 + (x362 -
    x366)^2) + 1 / sqrt((x82 - x87)^2 + (x222 - x227)^2 + (x362 - x367)^2) + 1
    / sqrt((x82 - x88)^2 + (x222 - x228)^2 + (x362 - x368)^2) + 1 / sqrt((x82
    - x89)^2 + (x222 - x229)^2 + (x362 - x369)^2) + 1 / sqrt((x82 - x90)^2 + (
    x222 - x230)^2 + (x362 - x370)^2) + 1 / sqrt((x82 - x91)^2 + (x222 - x231)^
    2 + (x362 - x371)^2) + 1 / sqrt((x82 - x92)^2 + (x222 - x232)^2 + (x362 -
    x372)^2) + 1 / sqrt((x82 - x93)^2 + (x222 - x233)^2 + (x362 - x373)^2) + 1
    / sqrt((x82 - x94)^2 + (x222 - x234)^2 + (x362 - x374)^2) + 1 / sqrt((x82
    - x95)^2 + (x222 - x235)^2 + (x362 - x375)^2) + 1 / sqrt((x82 - x96)^2 + (
    x222 - x236)^2 + (x362 - x376)^2) + 1 / sqrt((x82 - x97)^2 + (x222 - x237)^
    2 + (x362 - x377)^2) + 1 / sqrt((x82 - x98)^2 + (x222 - x238)^2 + (x362 -
    x378)^2) + 1 / sqrt((x82 - x99)^2 + (x222 - x239)^2 + (x362 - x379)^2) + 1
    / sqrt((x82 - x100)^2 + (x222 - x240)^2 + (x362 - x380)^2) + 1 / sqrt((x82
    - x101)^2 + (x222 - x241)^2 + (x362 - x381)^2) + 1 / sqrt((x82 - x102)^2
    + (x222 - x242)^2 + (x362 - x382)^2) + 1 / sqrt((x82 - x103)^2 + (x222 -
    x243)^2 + (x362 - x383)^2) + 1 / sqrt((x82 - x104)^2 + (x222 - x244)^2 + (
    x362 - x384)^2) + 1 / sqrt((x82 - x105)^2 + (x222 - x245)^2 + (x362 - x385)
    ^2) + 1 / sqrt((x82 - x106)^2 + (x222 - x246)^2 + (x362 - x386)^2) + 1 /
    sqrt((x82 - x107)^2 + (x222 - x247)^2 + (x362 - x387)^2) + 1 / sqrt((x82 -
    x108)^2 + (x222 - x248)^2 + (x362 - x388)^2) + 1 / sqrt((x82 - x109)^2 + (
    x222 - x249)^2 + (x362 - x389)^2) + 1 / sqrt((x82 - x110)^2 + (x222 - x250)
    ^2 + (x362 - x390)^2) + 1 / sqrt((x82 - x111)^2 + (x222 - x251)^2 + (x362
    - x391)^2) + 1 / sqrt((x82 - x112)^2 + (x222 - x252)^2 + (x362 - x392)^2)
    + 1 / sqrt((x82 - x113)^2 + (x222 - x253)^2 + (x362 - x393)^2) + 1 / sqrt(
    (x82 - x114)^2 + (x222 - x254)^2 + (x362 - x394)^2) + 1 / sqrt((x82 - x115)
    ^2 + (x222 - x255)^2 + (x362 - x395)^2) + 1 / sqrt((x82 - x116)^2 + (x222
    - x256)^2 + (x362 - x396)^2) + 1 / sqrt((x82 - x117)^2 + (x222 - x257)^2
    + (x362 - x397)^2) + 1 / sqrt((x82 - x118)^2 + (x222 - x258)^2 + (x362 -
    x398)^2) + 1 / sqrt((x82 - x119)^2 + (x222 - x259)^2 + (x362 - x399)^2) + 1
    / sqrt((x82 - x120)^2 + (x222 - x260)^2 + (x362 - x400)^2) + 1 / sqrt((x82
    - x121)^2 + (x222 - x261)^2 + (x362 - x401)^2) + 1 / sqrt((x82 - x122)^2
    + (x222 - x262)^2 + (x362 - x402)^2) + 1 / sqrt((x82 - x123)^2 + (x222 -
    x263)^2 + (x362 - x403)^2) + 1 / sqrt((x82 - x124)^2 + (x222 - x264)^2 + (
    x362 - x404)^2) + 1 / sqrt((x82 - x125)^2 + (x222 - x265)^2 + (x362 - x405)
    ^2) + 1 / sqrt((x82 - x126)^2 + (x222 - x266)^2 + (x362 - x406)^2) + 1 /
    sqrt((x82 - x127)^2 + (x222 - x267)^2 + (x362 - x407)^2) + 1 / sqrt((x82 -
    x128)^2 + (x222 - x268)^2 + (x362 - x408)^2) + 1 / sqrt((x82 - x129)^2 + (
    x222 - x269)^2 + (x362 - x409)^2) + 1 / sqrt((x82 - x130)^2 + (x222 - x270)
    ^2 + (x362 - x410)^2) + 1 / sqrt((x82 - x131)^2 + (x222 - x271)^2 + (x362
    - x411)^2) + 1 / sqrt((x82 - x132)^2 + (x222 - x272)^2 + (x362 - x412)^2)
    + 1 / sqrt((x82 - x133)^2 + (x222 - x273)^2 + (x362 - x413)^2) + 1 / sqrt(
    (x82 - x134)^2 + (x222 - x274)^2 + (x362 - x414)^2) + 1 / sqrt((x82 - x135)
    ^2 + (x222 - x275)^2 + (x362 - x415)^2) + 1 / sqrt((x82 - x136)^2 + (x222
    - x276)^2 + (x362 - x416)^2) + 1 / sqrt((x82 - x137)^2 + (x222 - x277)^2
    + (x362 - x417)^2) + 1 / sqrt((x82 - x138)^2 + (x222 - x278)^2 + (x362 -
    x418)^2) + 1 / sqrt((x82 - x139)^2 + (x222 - x279)^2 + (x362 - x419)^2) + 1
    / sqrt((x82 - x140)^2 + (x222 - x280)^2 + (x362 - x420)^2) + 1 / sqrt((x83
    - x84)^2 + (x223 - x224)^2 + (x363 - x364)^2) + 1 / sqrt((x83 - x85)^2 + (
    x223 - x225)^2 + (x363 - x365)^2) + 1 / sqrt((x83 - x86)^2 + (x223 - x226)^
    2 + (x363 - x366)^2) + 1 / sqrt((x83 - x87)^2 + (x223 - x227)^2 + (x363 -
    x367)^2) + 1 / sqrt((x83 - x88)^2 + (x223 - x228)^2 + (x363 - x368)^2) + 1
    / sqrt((x83 - x89)^2 + (x223 - x229)^2 + (x363 - x369)^2) + 1 / sqrt((x83
    - x90)^2 + (x223 - x230)^2 + (x363 - x370)^2) + 1 / sqrt((x83 - x91)^2 + (
    x223 - x231)^2 + (x363 - x371)^2) + 1 / sqrt((x83 - x92)^2 + (x223 - x232)^
    2 + (x363 - x372)^2) + 1 / sqrt((x83 - x93)^2 + (x223 - x233)^2 + (x363 -
    x373)^2) + 1 / sqrt((x83 - x94)^2 + (x223 - x234)^2 + (x363 - x374)^2) + 1
    / sqrt((x83 - x95)^2 + (x223 - x235)^2 + (x363 - x375)^2) + 1 / sqrt((x83
    - x96)^2 + (x223 - x236)^2 + (x363 - x376)^2) + 1 / sqrt((x83 - x97)^2 + (
    x223 - x237)^2 + (x363 - x377)^2) + 1 / sqrt((x83 - x98)^2 + (x223 - x238)^
    2 + (x363 - x378)^2) + 1 / sqrt((x83 - x99)^2 + (x223 - x239)^2 + (x363 -
    x379)^2) + 1 / sqrt((x83 - x100)^2 + (x223 - x240)^2 + (x363 - x380)^2) + 1
    / sqrt((x83 - x101)^2 + (x223 - x241)^2 + (x363 - x381)^2) + 1 / sqrt((x83
    - x102)^2 + (x223 - x242)^2 + (x363 - x382)^2) + 1 / sqrt((x83 - x103)^2
    + (x223 - x243)^2 + (x363 - x383)^2) + 1 / sqrt((x83 - x104)^2 + (x223 -
    x244)^2 + (x363 - x384)^2) + 1 / sqrt((x83 - x105)^2 + (x223 - x245)^2 + (
    x363 - x385)^2) + 1 / sqrt((x83 - x106)^2 + (x223 - x246)^2 + (x363 - x386)
    ^2) + 1 / sqrt((x83 - x107)^2 + (x223 - x247)^2 + (x363 - x387)^2) + 1 /
    sqrt((x83 - x108)^2 + (x223 - x248)^2 + (x363 - x388)^2) + 1 / sqrt((x83 -
    x109)^2 + (x223 - x249)^2 + (x363 - x389)^2) + 1 / sqrt((x83 - x110)^2 + (
    x223 - x250)^2 + (x363 - x390)^2) + 1 / sqrt((x83 - x111)^2 + (x223 - x251)
    ^2 + (x363 - x391)^2) + 1 / sqrt((x83 - x112)^2 + (x223 - x252)^2 + (x363
    - x392)^2) + 1 / sqrt((x83 - x113)^2 + (x223 - x253)^2 + (x363 - x393)^2)
    + 1 / sqrt((x83 - x114)^2 + (x223 - x254)^2 + (x363 - x394)^2) + 1 / sqrt(
    (x83 - x115)^2 + (x223 - x255)^2 + (x363 - x395)^2) + 1 / sqrt((x83 - x116)
    ^2 + (x223 - x256)^2 + (x363 - x396)^2) + 1 / sqrt((x83 - x117)^2 + (x223
    - x257)^2 + (x363 - x397)^2) + 1 / sqrt((x83 - x118)^2 + (x223 - x258)^2
    + (x363 - x398)^2) + 1 / sqrt((x83 - x119)^2 + (x223 - x259)^2 + (x363 -
    x399)^2) + 1 / sqrt((x83 - x120)^2 + (x223 - x260)^2 + (x363 - x400)^2) + 1
    / sqrt((x83 - x121)^2 + (x223 - x261)^2 + (x363 - x401)^2) + 1 / sqrt((x83
    - x122)^2 + (x223 - x262)^2 + (x363 - x402)^2) + 1 / sqrt((x83 - x123)^2
    + (x223 - x263)^2 + (x363 - x403)^2) + 1 / sqrt((x83 - x124)^2 + (x223 -
    x264)^2 + (x363 - x404)^2) + 1 / sqrt((x83 - x125)^2 + (x223 - x265)^2 + (
    x363 - x405)^2) + 1 / sqrt((x83 - x126)^2 + (x223 - x266)^2 + (x363 - x406)
    ^2) + 1 / sqrt((x83 - x127)^2 + (x223 - x267)^2 + (x363 - x407)^2) + 1 /
    sqrt((x83 - x128)^2 + (x223 - x268)^2 + (x363 - x408)^2) + 1 / sqrt((x83 -
    x129)^2 + (x223 - x269)^2 + (x363 - x409)^2) + 1 / sqrt((x83 - x130)^2 + (
    x223 - x270)^2 + (x363 - x410)^2) + 1 / sqrt((x83 - x131)^2 + (x223 - x271)
    ^2 + (x363 - x411)^2) + 1 / sqrt((x83 - x132)^2 + (x223 - x272)^2 + (x363
    - x412)^2) + 1 / sqrt((x83 - x133)^2 + (x223 - x273)^2 + (x363 - x413)^2)
    + 1 / sqrt((x83 - x134)^2 + (x223 - x274)^2 + (x363 - x414)^2) + 1 / sqrt(
    (x83 - x135)^2 + (x223 - x275)^2 + (x363 - x415)^2) + 1 / sqrt((x83 - x136)
    ^2 + (x223 - x276)^2 + (x363 - x416)^2) + 1 / sqrt((x83 - x137)^2 + (x223
    - x277)^2 + (x363 - x417)^2) + 1 / sqrt((x83 - x138)^2 + (x223 - x278)^2
    + (x363 - x418)^2) + 1 / sqrt((x83 - x139)^2 + (x223 - x279)^2 + (x363 -
    x419)^2) + 1 / sqrt((x83 - x140)^2 + (x223 - x280)^2 + (x363 - x420)^2) + 1
    / sqrt((x84 - x85)^2 + (x224 - x225)^2 + (x364 - x365)^2) + 1 / sqrt((x84
    - x86)^2 + (x224 - x226)^2 + (x364 - x366)^2) + 1 / sqrt((x84 - x87)^2 + (
    x224 - x227)^2 + (x364 - x367)^2) + 1 / sqrt((x84 - x88)^2 + (x224 - x228)^
    2 + (x364 - x368)^2) + 1 / sqrt((x84 - x89)^2 + (x224 - x229)^2 + (x364 -
    x369)^2) + 1 / sqrt((x84 - x90)^2 + (x224 - x230)^2 + (x364 - x370)^2) + 1
    / sqrt((x84 - x91)^2 + (x224 - x231)^2 + (x364 - x371)^2) + 1 / sqrt((x84
    - x92)^2 + (x224 - x232)^2 + (x364 - x372)^2) + 1 / sqrt((x84 - x93)^2 + (
    x224 - x233)^2 + (x364 - x373)^2) + 1 / sqrt((x84 - x94)^2 + (x224 - x234)^
    2 + (x364 - x374)^2) + 1 / sqrt((x84 - x95)^2 + (x224 - x235)^2 + (x364 -
    x375)^2) + 1 / sqrt((x84 - x96)^2 + (x224 - x236)^2 + (x364 - x376)^2) + 1
    / sqrt((x84 - x97)^2 + (x224 - x237)^2 + (x364 - x377)^2) + 1 / sqrt((x84
    - x98)^2 + (x224 - x238)^2 + (x364 - x378)^2) + 1 / sqrt((x84 - x99)^2 + (
    x224 - x239)^2 + (x364 - x379)^2) + 1 / sqrt((x84 - x100)^2 + (x224 - x240)
    ^2 + (x364 - x380)^2) + 1 / sqrt((x84 - x101)^2 + (x224 - x241)^2 + (x364
    - x381)^2) + 1 / sqrt((x84 - x102)^2 + (x224 - x242)^2 + (x364 - x382)^2)
    + 1 / sqrt((x84 - x103)^2 + (x224 - x243)^2 + (x364 - x383)^2) + 1 / sqrt(
    (x84 - x104)^2 + (x224 - x244)^2 + (x364 - x384)^2) + 1 / sqrt((x84 - x105)
    ^2 + (x224 - x245)^2 + (x364 - x385)^2) + 1 / sqrt((x84 - x106)^2 + (x224
    - x246)^2 + (x364 - x386)^2) + 1 / sqrt((x84 - x107)^2 + (x224 - x247)^2
    + (x364 - x387)^2) + 1 / sqrt((x84 - x108)^2 + (x224 - x248)^2 + (x364 -
    x388)^2) + 1 / sqrt((x84 - x109)^2 + (x224 - x249)^2 + (x364 - x389)^2) + 1
    / sqrt((x84 - x110)^2 + (x224 - x250)^2 + (x364 - x390)^2) + 1 / sqrt((x84
    - x111)^2 + (x224 - x251)^2 + (x364 - x391)^2) + 1 / sqrt((x84 - x112)^2
    + (x224 - x252)^2 + (x364 - x392)^2) + 1 / sqrt((x84 - x113)^2 + (x224 -
    x253)^2 + (x364 - x393)^2) + 1 / sqrt((x84 - x114)^2 + (x224 - x254)^2 + (
    x364 - x394)^2) + 1 / sqrt((x84 - x115)^2 + (x224 - x255)^2 + (x364 - x395)
    ^2) + 1 / sqrt((x84 - x116)^2 + (x224 - x256)^2 + (x364 - x396)^2) + 1 /
    sqrt((x84 - x117)^2 + (x224 - x257)^2 + (x364 - x397)^2) + 1 / sqrt((x84 -
    x118)^2 + (x224 - x258)^2 + (x364 - x398)^2) + 1 / sqrt((x84 - x119)^2 + (
    x224 - x259)^2 + (x364 - x399)^2) + 1 / sqrt((x84 - x120)^2 + (x224 - x260)
    ^2 + (x364 - x400)^2) + 1 / sqrt((x84 - x121)^2 + (x224 - x261)^2 + (x364
    - x401)^2) + 1 / sqrt((x84 - x122)^2 + (x224 - x262)^2 + (x364 - x402)^2)
    + 1 / sqrt((x84 - x123)^2 + (x224 - x263)^2 + (x364 - x403)^2) + 1 / sqrt(
    (x84 - x124)^2 + (x224 - x264)^2 + (x364 - x404)^2) + 1 / sqrt((x84 - x125)
    ^2 + (x224 - x265)^2 + (x364 - x405)^2) + 1 / sqrt((x84 - x126)^2 + (x224
    - x266)^2 + (x364 - x406)^2) + 1 / sqrt((x84 - x127)^2 + (x224 - x267)^2
    + (x364 - x407)^2) + 1 / sqrt((x84 - x128)^2 + (x224 - x268)^2 + (x364 -
    x408)^2) + 1 / sqrt((x84 - x129)^2 + (x224 - x269)^2 + (x364 - x409)^2) + 1
    / sqrt((x84 - x130)^2 + (x224 - x270)^2 + (x364 - x410)^2) + 1 / sqrt((x84
    - x131)^2 + (x224 - x271)^2 + (x364 - x411)^2) + 1 / sqrt((x84 - x132)^2
    + (x224 - x272)^2 + (x364 - x412)^2) + 1 / sqrt((x84 - x133)^2 + (x224 -
    x273)^2 + (x364 - x413)^2) + 1 / sqrt((x84 - x134)^2 + (x224 - x274)^2 + (
    x364 - x414)^2) + 1 / sqrt((x84 - x135)^2 + (x224 - x275)^2 + (x364 - x415)
    ^2) + 1 / sqrt((x84 - x136)^2 + (x224 - x276)^2 + (x364 - x416)^2) + 1 /
    sqrt((x84 - x137)^2 + (x224 - x277)^2 + (x364 - x417)^2) + 1 / sqrt((x84 -
    x138)^2 + (x224 - x278)^2 + (x364 - x418)^2) + 1 / sqrt((x84 - x139)^2 + (
    x224 - x279)^2 + (x364 - x419)^2) + 1 / sqrt((x84 - x140)^2 + (x224 - x280)
    ^2 + (x364 - x420)^2) + 1 / sqrt((x85 - x86)^2 + (x225 - x226)^2 + (x365 -
    x366)^2) + 1 / sqrt((x85 - x87)^2 + (x225 - x227)^2 + (x365 - x367)^2) + 1
    / sqrt((x85 - x88)^2 + (x225 - x228)^2 + (x365 - x368)^2) + 1 / sqrt((x85
    - x89)^2 + (x225 - x229)^2 + (x365 - x369)^2) + 1 / sqrt((x85 - x90)^2 + (
    x225 - x230)^2 + (x365 - x370)^2) + 1 / sqrt((x85 - x91)^2 + (x225 - x231)^
    2 + (x365 - x371)^2) + 1 / sqrt((x85 - x92)^2 + (x225 - x232)^2 + (x365 -
    x372)^2) + 1 / sqrt((x85 - x93)^2 + (x225 - x233)^2 + (x365 - x373)^2) + 1
    / sqrt((x85 - x94)^2 + (x225 - x234)^2 + (x365 - x374)^2) + 1 / sqrt((x85
    - x95)^2 + (x225 - x235)^2 + (x365 - x375)^2) + 1 / sqrt((x85 - x96)^2 + (
    x225 - x236)^2 + (x365 - x376)^2) + 1 / sqrt((x85 - x97)^2 + (x225 - x237)^
    2 + (x365 - x377)^2) + 1 / sqrt((x85 - x98)^2 + (x225 - x238)^2 + (x365 -
    x378)^2) + 1 / sqrt((x85 - x99)^2 + (x225 - x239)^2 + (x365 - x379)^2) + 1
    / sqrt((x85 - x100)^2 + (x225 - x240)^2 + (x365 - x380)^2) + 1 / sqrt((x85
    - x101)^2 + (x225 - x241)^2 + (x365 - x381)^2) + 1 / sqrt((x85 - x102)^2
    + (x225 - x242)^2 + (x365 - x382)^2) + 1 / sqrt((x85 - x103)^2 + (x225 -
    x243)^2 + (x365 - x383)^2) + 1 / sqrt((x85 - x104)^2 + (x225 - x244)^2 + (
    x365 - x384)^2) + 1 / sqrt((x85 - x105)^2 + (x225 - x245)^2 + (x365 - x385)
    ^2) + 1 / sqrt((x85 - x106)^2 + (x225 - x246)^2 + (x365 - x386)^2) + 1 /
    sqrt((x85 - x107)^2 + (x225 - x247)^2 + (x365 - x387)^2) + 1 / sqrt((x85 -
    x108)^2 + (x225 - x248)^2 + (x365 - x388)^2) + 1 / sqrt((x85 - x109)^2 + (
    x225 - x249)^2 + (x365 - x389)^2) + 1 / sqrt((x85 - x110)^2 + (x225 - x250)
    ^2 + (x365 - x390)^2) + 1 / sqrt((x85 - x111)^2 + (x225 - x251)^2 + (x365
    - x391)^2) + 1 / sqrt((x85 - x112)^2 + (x225 - x252)^2 + (x365 - x392)^2)
    + 1 / sqrt((x85 - x113)^2 + (x225 - x253)^2 + (x365 - x393)^2) + 1 / sqrt(
    (x85 - x114)^2 + (x225 - x254)^2 + (x365 - x394)^2) + 1 / sqrt((x85 - x115)
    ^2 + (x225 - x255)^2 + (x365 - x395)^2) + 1 / sqrt((x85 - x116)^2 + (x225
    - x256)^2 + (x365 - x396)^2) + 1 / sqrt((x85 - x117)^2 + (x225 - x257)^2
    + (x365 - x397)^2) + 1 / sqrt((x85 - x118)^2 + (x225 - x258)^2 + (x365 -
    x398)^2) + 1 / sqrt((x85 - x119)^2 + (x225 - x259)^2 + (x365 - x399)^2) + 1
    / sqrt((x85 - x120)^2 + (x225 - x260)^2 + (x365 - x400)^2) + 1 / sqrt((x85
    - x121)^2 + (x225 - x261)^2 + (x365 - x401)^2) + 1 / sqrt((x85 - x122)^2
    + (x225 - x262)^2 + (x365 - x402)^2) + 1 / sqrt((x85 - x123)^2 + (x225 -
    x263)^2 + (x365 - x403)^2) + 1 / sqrt((x85 - x124)^2 + (x225 - x264)^2 + (
    x365 - x404)^2) + 1 / sqrt((x85 - x125)^2 + (x225 - x265)^2 + (x365 - x405)
    ^2) + 1 / sqrt((x85 - x126)^2 + (x225 - x266)^2 + (x365 - x406)^2) + 1 /
    sqrt((x85 - x127)^2 + (x225 - x267)^2 + (x365 - x407)^2) + 1 / sqrt((x85 -
    x128)^2 + (x225 - x268)^2 + (x365 - x408)^2) + 1 / sqrt((x85 - x129)^2 + (
    x225 - x269)^2 + (x365 - x409)^2) + 1 / sqrt((x85 - x130)^2 + (x225 - x270)
    ^2 + (x365 - x410)^2) + 1 / sqrt((x85 - x131)^2 + (x225 - x271)^2 + (x365
    - x411)^2) + 1 / sqrt((x85 - x132)^2 + (x225 - x272)^2 + (x365 - x412)^2)
    + 1 / sqrt((x85 - x133)^2 + (x225 - x273)^2 + (x365 - x413)^2) + 1 / sqrt(
    (x85 - x134)^2 + (x225 - x274)^2 + (x365 - x414)^2) + 1 / sqrt((x85 - x135)
    ^2 + (x225 - x275)^2 + (x365 - x415)^2) + 1 / sqrt((x85 - x136)^2 + (x225
    - x276)^2 + (x365 - x416)^2) + 1 / sqrt((x85 - x137)^2 + (x225 - x277)^2
    + (x365 - x417)^2) + 1 / sqrt((x85 - x138)^2 + (x225 - x278)^2 + (x365 -
    x418)^2) + 1 / sqrt((x85 - x139)^2 + (x225 - x279)^2 + (x365 - x419)^2) + 1
    / sqrt((x85 - x140)^2 + (x225 - x280)^2 + (x365 - x420)^2) + 1 / sqrt((x86
    - x87)^2 + (x226 - x227)^2 + (x366 - x367)^2) + 1 / sqrt((x86 - x88)^2 + (
    x226 - x228)^2 + (x366 - x368)^2) + 1 / sqrt((x86 - x89)^2 + (x226 - x229)^
    2 + (x366 - x369)^2) + 1 / sqrt((x86 - x90)^2 + (x226 - x230)^2 + (x366 -
    x370)^2) + 1 / sqrt((x86 - x91)^2 + (x226 - x231)^2 + (x366 - x371)^2) + 1
    / sqrt((x86 - x92)^2 + (x226 - x232)^2 + (x366 - x372)^2) + 1 / sqrt((x86
    - x93)^2 + (x226 - x233)^2 + (x366 - x373)^2) + 1 / sqrt((x86 - x94)^2 + (
    x226 - x234)^2 + (x366 - x374)^2) + 1 / sqrt((x86 - x95)^2 + (x226 - x235)^
    2 + (x366 - x375)^2) + 1 / sqrt((x86 - x96)^2 + (x226 - x236)^2 + (x366 -
    x376)^2) + 1 / sqrt((x86 - x97)^2 + (x226 - x237)^2 + (x366 - x377)^2) + 1
    / sqrt((x86 - x98)^2 + (x226 - x238)^2 + (x366 - x378)^2) + 1 / sqrt((x86
    - x99)^2 + (x226 - x239)^2 + (x366 - x379)^2) + 1 / sqrt((x86 - x100)^2 +
    (x226 - x240)^2 + (x366 - x380)^2) + 1 / sqrt((x86 - x101)^2 + (x226 - x241)
    ^2 + (x366 - x381)^2) + 1 / sqrt((x86 - x102)^2 + (x226 - x242)^2 + (x366
    - x382)^2) + 1 / sqrt((x86 - x103)^2 + (x226 - x243)^2 + (x366 - x383)^2)
    + 1 / sqrt((x86 - x104)^2 + (x226 - x244)^2 + (x366 - x384)^2) + 1 / sqrt(
    (x86 - x105)^2 + (x226 - x245)^2 + (x366 - x385)^2) + 1 / sqrt((x86 - x106)
    ^2 + (x226 - x246)^2 + (x366 - x386)^2) + 1 / sqrt((x86 - x107)^2 + (x226
    - x247)^2 + (x366 - x387)^2) + 1 / sqrt((x86 - x108)^2 + (x226 - x248)^2
    + (x366 - x388)^2) + 1 / sqrt((x86 - x109)^2 + (x226 - x249)^2 + (x366 -
    x389)^2) + 1 / sqrt((x86 - x110)^2 + (x226 - x250)^2 + (x366 - x390)^2) + 1
    / sqrt((x86 - x111)^2 + (x226 - x251)^2 + (x366 - x391)^2) + 1 / sqrt((x86
    - x112)^2 + (x226 - x252)^2 + (x366 - x392)^2) + 1 / sqrt((x86 - x113)^2
    + (x226 - x253)^2 + (x366 - x393)^2) + 1 / sqrt((x86 - x114)^2 + (x226 -
    x254)^2 + (x366 - x394)^2) + 1 / sqrt((x86 - x115)^2 + (x226 - x255)^2 + (
    x366 - x395)^2) + 1 / sqrt((x86 - x116)^2 + (x226 - x256)^2 + (x366 - x396)
    ^2) + 1 / sqrt((x86 - x117)^2 + (x226 - x257)^2 + (x366 - x397)^2) + 1 /
    sqrt((x86 - x118)^2 + (x226 - x258)^2 + (x366 - x398)^2) + 1 / sqrt((x86 -
    x119)^2 + (x226 - x259)^2 + (x366 - x399)^2) + 1 / sqrt((x86 - x120)^2 + (
    x226 - x260)^2 + (x366 - x400)^2) + 1 / sqrt((x86 - x121)^2 + (x226 - x261)
    ^2 + (x366 - x401)^2) + 1 / sqrt((x86 - x122)^2 + (x226 - x262)^2 + (x366
    - x402)^2) + 1 / sqrt((x86 - x123)^2 + (x226 - x263)^2 + (x366 - x403)^2)
    + 1 / sqrt((x86 - x124)^2 + (x226 - x264)^2 + (x366 - x404)^2) + 1 / sqrt(
    (x86 - x125)^2 + (x226 - x265)^2 + (x366 - x405)^2) + 1 / sqrt((x86 - x126)
    ^2 + (x226 - x266)^2 + (x366 - x406)^2) + 1 / sqrt((x86 - x127)^2 + (x226
    - x267)^2 + (x366 - x407)^2) + 1 / sqrt((x86 - x128)^2 + (x226 - x268)^2
    + (x366 - x408)^2) + 1 / sqrt((x86 - x129)^2 + (x226 - x269)^2 + (x366 -
    x409)^2) + 1 / sqrt((x86 - x130)^2 + (x226 - x270)^2 + (x366 - x410)^2) + 1
    / sqrt((x86 - x131)^2 + (x226 - x271)^2 + (x366 - x411)^2) + 1 / sqrt((x86
    - x132)^2 + (x226 - x272)^2 + (x366 - x412)^2) + 1 / sqrt((x86 - x133)^2
    + (x226 - x273)^2 + (x366 - x413)^2) + 1 / sqrt((x86 - x134)^2 + (x226 -
    x274)^2 + (x366 - x414)^2) + 1 / sqrt((x86 - x135)^2 + (x226 - x275)^2 + (
    x366 - x415)^2) + 1 / sqrt((x86 - x136)^2 + (x226 - x276)^2 + (x366 - x416)
    ^2) + 1 / sqrt((x86 - x137)^2 + (x226 - x277)^2 + (x366 - x417)^2) + 1 /
    sqrt((x86 - x138)^2 + (x226 - x278)^2 + (x366 - x418)^2) + 1 / sqrt((x86 -
    x139)^2 + (x226 - x279)^2 + (x366 - x419)^2) + 1 / sqrt((x86 - x140)^2 + (
    x226 - x280)^2 + (x366 - x420)^2) + 1 / sqrt((x87 - x88)^2 + (x227 - x228)^
    2 + (x367 - x368)^2) + 1 / sqrt((x87 - x89)^2 + (x227 - x229)^2 + (x367 -
    x369)^2) + 1 / sqrt((x87 - x90)^2 + (x227 - x230)^2 + (x367 - x370)^2) + 1
    / sqrt((x87 - x91)^2 + (x227 - x231)^2 + (x367 - x371)^2) + 1 / sqrt((x87
    - x92)^2 + (x227 - x232)^2 + (x367 - x372)^2) + 1 / sqrt((x87 - x93)^2 + (
    x227 - x233)^2 + (x367 - x373)^2) + 1 / sqrt((x87 - x94)^2 + (x227 - x234)^
    2 + (x367 - x374)^2) + 1 / sqrt((x87 - x95)^2 + (x227 - x235)^2 + (x367 -
    x375)^2) + 1 / sqrt((x87 - x96)^2 + (x227 - x236)^2 + (x367 - x376)^2) + 1
    / sqrt((x87 - x97)^2 + (x227 - x237)^2 + (x367 - x377)^2) + 1 / sqrt((x87
    - x98)^2 + (x227 - x238)^2 + (x367 - x378)^2) + 1 / sqrt((x87 - x99)^2 + (
    x227 - x239)^2 + (x367 - x379)^2) + 1 / sqrt((x87 - x100)^2 + (x227 - x240)
    ^2 + (x367 - x380)^2) + 1 / sqrt((x87 - x101)^2 + (x227 - x241)^2 + (x367
    - x381)^2) + 1 / sqrt((x87 - x102)^2 + (x227 - x242)^2 + (x367 - x382)^2)
    + 1 / sqrt((x87 - x103)^2 + (x227 - x243)^2 + (x367 - x383)^2) + 1 / sqrt(
    (x87 - x104)^2 + (x227 - x244)^2 + (x367 - x384)^2) + 1 / sqrt((x87 - x105)
    ^2 + (x227 - x245)^2 + (x367 - x385)^2) + 1 / sqrt((x87 - x106)^2 + (x227
    - x246)^2 + (x367 - x386)^2) + 1 / sqrt((x87 - x107)^2 + (x227 - x247)^2
    + (x367 - x387)^2) + 1 / sqrt((x87 - x108)^2 + (x227 - x248)^2 + (x367 -
    x388)^2) + 1 / sqrt((x87 - x109)^2 + (x227 - x249)^2 + (x367 - x389)^2) + 1
    / sqrt((x87 - x110)^2 + (x227 - x250)^2 + (x367 - x390)^2) + 1 / sqrt((x87
    - x111)^2 + (x227 - x251)^2 + (x367 - x391)^2) + 1 / sqrt((x87 - x112)^2
    + (x227 - x252)^2 + (x367 - x392)^2) + 1 / sqrt((x87 - x113)^2 + (x227 -
    x253)^2 + (x367 - x393)^2) + 1 / sqrt((x87 - x114)^2 + (x227 - x254)^2 + (
    x367 - x394)^2) + 1 / sqrt((x87 - x115)^2 + (x227 - x255)^2 + (x367 - x395)
    ^2) + 1 / sqrt((x87 - x116)^2 + (x227 - x256)^2 + (x367 - x396)^2) + 1 /
    sqrt((x87 - x117)^2 + (x227 - x257)^2 + (x367 - x397)^2) + 1 / sqrt((x87 -
    x118)^2 + (x227 - x258)^2 + (x367 - x398)^2) + 1 / sqrt((x87 - x119)^2 + (
    x227 - x259)^2 + (x367 - x399)^2) + 1 / sqrt((x87 - x120)^2 + (x227 - x260)
    ^2 + (x367 - x400)^2) + 1 / sqrt((x87 - x121)^2 + (x227 - x261)^2 + (x367
    - x401)^2) + 1 / sqrt((x87 - x122)^2 + (x227 - x262)^2 + (x367 - x402)^2)
    + 1 / sqrt((x87 - x123)^2 + (x227 - x263)^2 + (x367 - x403)^2) + 1 / sqrt(
    (x87 - x124)^2 + (x227 - x264)^2 + (x367 - x404)^2) + 1 / sqrt((x87 - x125)
    ^2 + (x227 - x265)^2 + (x367 - x405)^2) + 1 / sqrt((x87 - x126)^2 + (x227
    - x266)^2 + (x367 - x406)^2) + 1 / sqrt((x87 - x127)^2 + (x227 - x267)^2
    + (x367 - x407)^2) + 1 / sqrt((x87 - x128)^2 + (x227 - x268)^2 + (x367 -
    x408)^2) + 1 / sqrt((x87 - x129)^2 + (x227 - x269)^2 + (x367 - x409)^2) + 1
    / sqrt((x87 - x130)^2 + (x227 - x270)^2 + (x367 - x410)^2) + 1 / sqrt((x87
    - x131)^2 + (x227 - x271)^2 + (x367 - x411)^2) + 1 / sqrt((x87 - x132)^2
    + (x227 - x272)^2 + (x367 - x412)^2) + 1 / sqrt((x87 - x133)^2 + (x227 -
    x273)^2 + (x367 - x413)^2) + 1 / sqrt((x87 - x134)^2 + (x227 - x274)^2 + (
    x367 - x414)^2) + 1 / sqrt((x87 - x135)^2 + (x227 - x275)^2 + (x367 - x415)
    ^2) + 1 / sqrt((x87 - x136)^2 + (x227 - x276)^2 + (x367 - x416)^2) + 1 /
    sqrt((x87 - x137)^2 + (x227 - x277)^2 + (x367 - x417)^2) + 1 / sqrt((x87 -
    x138)^2 + (x227 - x278)^2 + (x367 - x418)^2) + 1 / sqrt((x87 - x139)^2 + (
    x227 - x279)^2 + (x367 - x419)^2) + 1 / sqrt((x87 - x140)^2 + (x227 - x280)
    ^2 + (x367 - x420)^2) + 1 / sqrt((x88 - x89)^2 + (x228 - x229)^2 + (x368 -
    x369)^2) + 1 / sqrt((x88 - x90)^2 + (x228 - x230)^2 + (x368 - x370)^2) + 1
    / sqrt((x88 - x91)^2 + (x228 - x231)^2 + (x368 - x371)^2) + 1 / sqrt((x88
    - x92)^2 + (x228 - x232)^2 + (x368 - x372)^2) + 1 / sqrt((x88 - x93)^2 + (
    x228 - x233)^2 + (x368 - x373)^2) + 1 / sqrt((x88 - x94)^2 + (x228 - x234)^
    2 + (x368 - x374)^2) + 1 / sqrt((x88 - x95)^2 + (x228 - x235)^2 + (x368 -
    x375)^2) + 1 / sqrt((x88 - x96)^2 + (x228 - x236)^2 + (x368 - x376)^2) + 1
    / sqrt((x88 - x97)^2 + (x228 - x237)^2 + (x368 - x377)^2) + 1 / sqrt((x88
    - x98)^2 + (x228 - x238)^2 + (x368 - x378)^2) + 1 / sqrt((x88 - x99)^2 + (
    x228 - x239)^2 + (x368 - x379)^2) + 1 / sqrt((x88 - x100)^2 + (x228 - x240)
    ^2 + (x368 - x380)^2) + 1 / sqrt((x88 - x101)^2 + (x228 - x241)^2 + (x368
    - x381)^2) + 1 / sqrt((x88 - x102)^2 + (x228 - x242)^2 + (x368 - x382)^2)
    + 1 / sqrt((x88 - x103)^2 + (x228 - x243)^2 + (x368 - x383)^2) + 1 / sqrt(
    (x88 - x104)^2 + (x228 - x244)^2 + (x368 - x384)^2) + 1 / sqrt((x88 - x105)
    ^2 + (x228 - x245)^2 + (x368 - x385)^2) + 1 / sqrt((x88 - x106)^2 + (x228
    - x246)^2 + (x368 - x386)^2) + 1 / sqrt((x88 - x107)^2 + (x228 - x247)^2
    + (x368 - x387)^2) + 1 / sqrt((x88 - x108)^2 + (x228 - x248)^2 + (x368 -
    x388)^2) + 1 / sqrt((x88 - x109)^2 + (x228 - x249)^2 + (x368 - x389)^2) + 1
    / sqrt((x88 - x110)^2 + (x228 - x250)^2 + (x368 - x390)^2) + 1 / sqrt((x88
    - x111)^2 + (x228 - x251)^2 + (x368 - x391)^2) + 1 / sqrt((x88 - x112)^2
    + (x228 - x252)^2 + (x368 - x392)^2) + 1 / sqrt((x88 - x113)^2 + (x228 -
    x253)^2 + (x368 - x393)^2) + 1 / sqrt((x88 - x114)^2 + (x228 - x254)^2 + (
    x368 - x394)^2) + 1 / sqrt((x88 - x115)^2 + (x228 - x255)^2 + (x368 - x395)
    ^2) + 1 / sqrt((x88 - x116)^2 + (x228 - x256)^2 + (x368 - x396)^2) + 1 /
    sqrt((x88 - x117)^2 + (x228 - x257)^2 + (x368 - x397)^2) + 1 / sqrt((x88 -
    x118)^2 + (x228 - x258)^2 + (x368 - x398)^2) + 1 / sqrt((x88 - x119)^2 + (
    x228 - x259)^2 + (x368 - x399)^2) + 1 / sqrt((x88 - x120)^2 + (x228 - x260)
    ^2 + (x368 - x400)^2) + 1 / sqrt((x88 - x121)^2 + (x228 - x261)^2 + (x368
    - x401)^2) + 1 / sqrt((x88 - x122)^2 + (x228 - x262)^2 + (x368 - x402)^2)
    + 1 / sqrt((x88 - x123)^2 + (x228 - x263)^2 + (x368 - x403)^2) + 1 / sqrt(
    (x88 - x124)^2 + (x228 - x264)^2 + (x368 - x404)^2) + 1 / sqrt((x88 - x125)
    ^2 + (x228 - x265)^2 + (x368 - x405)^2) + 1 / sqrt((x88 - x126)^2 + (x228
    - x266)^2 + (x368 - x406)^2) + 1 / sqrt((x88 - x127)^2 + (x228 - x267)^2
    + (x368 - x407)^2) + 1 / sqrt((x88 - x128)^2 + (x228 - x268)^2 + (x368 -
    x408)^2) + 1 / sqrt((x88 - x129)^2 + (x228 - x269)^2 + (x368 - x409)^2) + 1
    / sqrt((x88 - x130)^2 + (x228 - x270)^2 + (x368 - x410)^2) + 1 / sqrt((x88
    - x131)^2 + (x228 - x271)^2 + (x368 - x411)^2) + 1 / sqrt((x88 - x132)^2
    + (x228 - x272)^2 + (x368 - x412)^2) + 1 / sqrt((x88 - x133)^2 + (x228 -
    x273)^2 + (x368 - x413)^2) + 1 / sqrt((x88 - x134)^2 + (x228 - x274)^2 + (
    x368 - x414)^2) + 1 / sqrt((x88 - x135)^2 + (x228 - x275)^2 + (x368 - x415)
    ^2) + 1 / sqrt((x88 - x136)^2 + (x228 - x276)^2 + (x368 - x416)^2) + 1 /
    sqrt((x88 - x137)^2 + (x228 - x277)^2 + (x368 - x417)^2) + 1 / sqrt((x88 -
    x138)^2 + (x228 - x278)^2 + (x368 - x418)^2) + 1 / sqrt((x88 - x139)^2 + (
    x228 - x279)^2 + (x368 - x419)^2) + 1 / sqrt((x88 - x140)^2 + (x228 - x280)
    ^2 + (x368 - x420)^2) + 1 / sqrt((x89 - x90)^2 + (x229 - x230)^2 + (x369 -
    x370)^2) + 1 / sqrt((x89 - x91)^2 + (x229 - x231)^2 + (x369 - x371)^2) + 1
    / sqrt((x89 - x92)^2 + (x229 - x232)^2 + (x369 - x372)^2) + 1 / sqrt((x89
    - x93)^2 + (x229 - x233)^2 + (x369 - x373)^2) + 1 / sqrt((x89 - x94)^2 + (
    x229 - x234)^2 + (x369 - x374)^2) + 1 / sqrt((x89 - x95)^2 + (x229 - x235)^
    2 + (x369 - x375)^2) + 1 / sqrt((x89 - x96)^2 + (x229 - x236)^2 + (x369 -
    x376)^2) + 1 / sqrt((x89 - x97)^2 + (x229 - x237)^2 + (x369 - x377)^2) + 1
    / sqrt((x89 - x98)^2 + (x229 - x238)^2 + (x369 - x378)^2) + 1 / sqrt((x89
    - x99)^2 + (x229 - x239)^2 + (x369 - x379)^2) + 1 / sqrt((x89 - x100)^2 +
    (x229 - x240)^2 + (x369 - x380)^2) + 1 / sqrt((x89 - x101)^2 + (x229 - x241)
    ^2 + (x369 - x381)^2) + 1 / sqrt((x89 - x102)^2 + (x229 - x242)^2 + (x369
    - x382)^2) + 1 / sqrt((x89 - x103)^2 + (x229 - x243)^2 + (x369 - x383)^2)
    + 1 / sqrt((x89 - x104)^2 + (x229 - x244)^2 + (x369 - x384)^2) + 1 / sqrt(
    (x89 - x105)^2 + (x229 - x245)^2 + (x369 - x385)^2) + 1 / sqrt((x89 - x106)
    ^2 + (x229 - x246)^2 + (x369 - x386)^2) + 1 / sqrt((x89 - x107)^2 + (x229
    - x247)^2 + (x369 - x387)^2) + 1 / sqrt((x89 - x108)^2 + (x229 - x248)^2
    + (x369 - x388)^2) + 1 / sqrt((x89 - x109)^2 + (x229 - x249)^2 + (x369 -
    x389)^2) + 1 / sqrt((x89 - x110)^2 + (x229 - x250)^2 + (x369 - x390)^2) + 1
    / sqrt((x89 - x111)^2 + (x229 - x251)^2 + (x369 - x391)^2) + 1 / sqrt((x89
    - x112)^2 + (x229 - x252)^2 + (x369 - x392)^2) + 1 / sqrt((x89 - x113)^2
    + (x229 - x253)^2 + (x369 - x393)^2) + 1 / sqrt((x89 - x114)^2 + (x229 -
    x254)^2 + (x369 - x394)^2) + 1 / sqrt((x89 - x115)^2 + (x229 - x255)^2 + (
    x369 - x395)^2) + 1 / sqrt((x89 - x116)^2 + (x229 - x256)^2 + (x369 - x396)
    ^2) + 1 / sqrt((x89 - x117)^2 + (x229 - x257)^2 + (x369 - x397)^2) + 1 /
    sqrt((x89 - x118)^2 + (x229 - x258)^2 + (x369 - x398)^2) + 1 / sqrt((x89 -
    x119)^2 + (x229 - x259)^2 + (x369 - x399)^2) + 1 / sqrt((x89 - x120)^2 + (
    x229 - x260)^2 + (x369 - x400)^2) + 1 / sqrt((x89 - x121)^2 + (x229 - x261)
    ^2 + (x369 - x401)^2) + 1 / sqrt((x89 - x122)^2 + (x229 - x262)^2 + (x369
    - x402)^2) + 1 / sqrt((x89 - x123)^2 + (x229 - x263)^2 + (x369 - x403)^2)
    + 1 / sqrt((x89 - x124)^2 + (x229 - x264)^2 + (x369 - x404)^2) + 1 / sqrt(
    (x89 - x125)^2 + (x229 - x265)^2 + (x369 - x405)^2) + 1 / sqrt((x89 - x126)
    ^2 + (x229 - x266)^2 + (x369 - x406)^2) + 1 / sqrt((x89 - x127)^2 + (x229
    - x267)^2 + (x369 - x407)^2) + 1 / sqrt((x89 - x128)^2 + (x229 - x268)^2
    + (x369 - x408)^2) + 1 / sqrt((x89 - x129)^2 + (x229 - x269)^2 + (x369 -
    x409)^2) + 1 / sqrt((x89 - x130)^2 + (x229 - x270)^2 + (x369 - x410)^2) + 1
    / sqrt((x89 - x131)^2 + (x229 - x271)^2 + (x369 - x411)^2) + 1 / sqrt((x89
    - x132)^2 + (x229 - x272)^2 + (x369 - x412)^2) + 1 / sqrt((x89 - x133)^2
    + (x229 - x273)^2 + (x369 - x413)^2) + 1 / sqrt((x89 - x134)^2 + (x229 -
    x274)^2 + (x369 - x414)^2) + 1 / sqrt((x89 - x135)^2 + (x229 - x275)^2 + (
    x369 - x415)^2) + 1 / sqrt((x89 - x136)^2 + (x229 - x276)^2 + (x369 - x416)
    ^2) + 1 / sqrt((x89 - x137)^2 + (x229 - x277)^2 + (x369 - x417)^2) + 1 /
    sqrt((x89 - x138)^2 + (x229 - x278)^2 + (x369 - x418)^2) + 1 / sqrt((x89 -
    x139)^2 + (x229 - x279)^2 + (x369 - x419)^2) + 1 / sqrt((x89 - x140)^2 + (
    x229 - x280)^2 + (x369 - x420)^2) + 1 / sqrt((x90 - x91)^2 + (x230 - x231)^
    2 + (x370 - x371)^2) + 1 / sqrt((x90 - x92)^2 + (x230 - x232)^2 + (x370 -
    x372)^2) + 1 / sqrt((x90 - x93)^2 + (x230 - x233)^2 + (x370 - x373)^2) + 1
    / sqrt((x90 - x94)^2 + (x230 - x234)^2 + (x370 - x374)^2) + 1 / sqrt((x90
    - x95)^2 + (x230 - x235)^2 + (x370 - x375)^2) + 1 / sqrt((x90 - x96)^2 + (
    x230 - x236)^2 + (x370 - x376)^2) + 1 / sqrt((x90 - x97)^2 + (x230 - x237)^
    2 + (x370 - x377)^2) + 1 / sqrt((x90 - x98)^2 + (x230 - x238)^2 + (x370 -
    x378)^2) + 1 / sqrt((x90 - x99)^2 + (x230 - x239)^2 + (x370 - x379)^2) + 1
    / sqrt((x90 - x100)^2 + (x230 - x240)^2 + (x370 - x380)^2) + 1 / sqrt((x90
    - x101)^2 + (x230 - x241)^2 + (x370 - x381)^2) + 1 / sqrt((x90 - x102)^2
    + (x230 - x242)^2 + (x370 - x382)^2) + 1 / sqrt((x90 - x103)^2 + (x230 -
    x243)^2 + (x370 - x383)^2) + 1 / sqrt((x90 - x104)^2 + (x230 - x244)^2 + (
    x370 - x384)^2) + 1 / sqrt((x90 - x105)^2 + (x230 - x245)^2 + (x370 - x385)
    ^2) + 1 / sqrt((x90 - x106)^2 + (x230 - x246)^2 + (x370 - x386)^2) + 1 /
    sqrt((x90 - x107)^2 + (x230 - x247)^2 + (x370 - x387)^2) + 1 / sqrt((x90 -
    x108)^2 + (x230 - x248)^2 + (x370 - x388)^2) + 1 / sqrt((x90 - x109)^2 + (
    x230 - x249)^2 + (x370 - x389)^2) + 1 / sqrt((x90 - x110)^2 + (x230 - x250)
    ^2 + (x370 - x390)^2) + 1 / sqrt((x90 - x111)^2 + (x230 - x251)^2 + (x370
    - x391)^2) + 1 / sqrt((x90 - x112)^2 + (x230 - x252)^2 + (x370 - x392)^2)
    + 1 / sqrt((x90 - x113)^2 + (x230 - x253)^2 + (x370 - x393)^2) + 1 / sqrt(
    (x90 - x114)^2 + (x230 - x254)^2 + (x370 - x394)^2) + 1 / sqrt((x90 - x115)
    ^2 + (x230 - x255)^2 + (x370 - x395)^2) + 1 / sqrt((x90 - x116)^2 + (x230
    - x256)^2 + (x370 - x396)^2) + 1 / sqrt((x90 - x117)^2 + (x230 - x257)^2
    + (x370 - x397)^2) + 1 / sqrt((x90 - x118)^2 + (x230 - x258)^2 + (x370 -
    x398)^2) + 1 / sqrt((x90 - x119)^2 + (x230 - x259)^2 + (x370 - x399)^2) + 1
    / sqrt((x90 - x120)^2 + (x230 - x260)^2 + (x370 - x400)^2) + 1 / sqrt((x90
    - x121)^2 + (x230 - x261)^2 + (x370 - x401)^2) + 1 / sqrt((x90 - x122)^2
    + (x230 - x262)^2 + (x370 - x402)^2) + 1 / sqrt((x90 - x123)^2 + (x230 -
    x263)^2 + (x370 - x403)^2) + 1 / sqrt((x90 - x124)^2 + (x230 - x264)^2 + (
    x370 - x404)^2) + 1 / sqrt((x90 - x125)^2 + (x230 - x265)^2 + (x370 - x405)
    ^2) + 1 / sqrt((x90 - x126)^2 + (x230 - x266)^2 + (x370 - x406)^2) + 1 /
    sqrt((x90 - x127)^2 + (x230 - x267)^2 + (x370 - x407)^2) + 1 / sqrt((x90 -
    x128)^2 + (x230 - x268)^2 + (x370 - x408)^2) + 1 / sqrt((x90 - x129)^2 + (
    x230 - x269)^2 + (x370 - x409)^2) + 1 / sqrt((x90 - x130)^2 + (x230 - x270)
    ^2 + (x370 - x410)^2) + 1 / sqrt((x90 - x131)^2 + (x230 - x271)^2 + (x370
    - x411)^2) + 1 / sqrt((x90 - x132)^2 + (x230 - x272)^2 + (x370 - x412)^2)
    + 1 / sqrt((x90 - x133)^2 + (x230 - x273)^2 + (x370 - x413)^2) + 1 / sqrt(
    (x90 - x134)^2 + (x230 - x274)^2 + (x370 - x414)^2) + 1 / sqrt((x90 - x135)
    ^2 + (x230 - x275)^2 + (x370 - x415)^2) + 1 / sqrt((x90 - x136)^2 + (x230
    - x276)^2 + (x370 - x416)^2) + 1 / sqrt((x90 - x137)^2 + (x230 - x277)^2
    + (x370 - x417)^2) + 1 / sqrt((x90 - x138)^2 + (x230 - x278)^2 + (x370 -
    x418)^2) + 1 / sqrt((x90 - x139)^2 + (x230 - x279)^2 + (x370 - x419)^2) + 1
    / sqrt((x90 - x140)^2 + (x230 - x280)^2 + (x370 - x420)^2) + 1 / sqrt((x91
    - x92)^2 + (x231 - x232)^2 + (x371 - x372)^2) + 1 / sqrt((x91 - x93)^2 + (
    x231 - x233)^2 + (x371 - x373)^2) + 1 / sqrt((x91 - x94)^2 + (x231 - x234)^
    2 + (x371 - x374)^2) + 1 / sqrt((x91 - x95)^2 + (x231 - x235)^2 + (x371 -
    x375)^2) + 1 / sqrt((x91 - x96)^2 + (x231 - x236)^2 + (x371 - x376)^2) + 1
    / sqrt((x91 - x97)^2 + (x231 - x237)^2 + (x371 - x377)^2) + 1 / sqrt((x91
    - x98)^2 + (x231 - x238)^2 + (x371 - x378)^2) + 1 / sqrt((x91 - x99)^2 + (
    x231 - x239)^2 + (x371 - x379)^2) + 1 / sqrt((x91 - x100)^2 + (x231 - x240)
    ^2 + (x371 - x380)^2) + 1 / sqrt((x91 - x101)^2 + (x231 - x241)^2 + (x371
    - x381)^2) + 1 / sqrt((x91 - x102)^2 + (x231 - x242)^2 + (x371 - x382)^2)
    + 1 / sqrt((x91 - x103)^2 + (x231 - x243)^2 + (x371 - x383)^2) + 1 / sqrt(
    (x91 - x104)^2 + (x231 - x244)^2 + (x371 - x384)^2) + 1 / sqrt((x91 - x105)
    ^2 + (x231 - x245)^2 + (x371 - x385)^2) + 1 / sqrt((x91 - x106)^2 + (x231
    - x246)^2 + (x371 - x386)^2) + 1 / sqrt((x91 - x107)^2 + (x231 - x247)^2
    + (x371 - x387)^2) + 1 / sqrt((x91 - x108)^2 + (x231 - x248)^2 + (x371 -
    x388)^2) + 1 / sqrt((x91 - x109)^2 + (x231 - x249)^2 + (x371 - x389)^2) + 1
    / sqrt((x91 - x110)^2 + (x231 - x250)^2 + (x371 - x390)^2) + 1 / sqrt((x91
    - x111)^2 + (x231 - x251)^2 + (x371 - x391)^2) + 1 / sqrt((x91 - x112)^2
    + (x231 - x252)^2 + (x371 - x392)^2) + 1 / sqrt((x91 - x113)^2 + (x231 -
    x253)^2 + (x371 - x393)^2) + 1 / sqrt((x91 - x114)^2 + (x231 - x254)^2 + (
    x371 - x394)^2) + 1 / sqrt((x91 - x115)^2 + (x231 - x255)^2 + (x371 - x395)
    ^2) + 1 / sqrt((x91 - x116)^2 + (x231 - x256)^2 + (x371 - x396)^2) + 1 /
    sqrt((x91 - x117)^2 + (x231 - x257)^2 + (x371 - x397)^2) + 1 / sqrt((x91 -
    x118)^2 + (x231 - x258)^2 + (x371 - x398)^2) + 1 / sqrt((x91 - x119)^2 + (
    x231 - x259)^2 + (x371 - x399)^2) + 1 / sqrt((x91 - x120)^2 + (x231 - x260)
    ^2 + (x371 - x400)^2) + 1 / sqrt((x91 - x121)^2 + (x231 - x261)^2 + (x371
    - x401)^2) + 1 / sqrt((x91 - x122)^2 + (x231 - x262)^2 + (x371 - x402)^2)
    + 1 / sqrt((x91 - x123)^2 + (x231 - x263)^2 + (x371 - x403)^2) + 1 / sqrt(
    (x91 - x124)^2 + (x231 - x264)^2 + (x371 - x404)^2) + 1 / sqrt((x91 - x125)
    ^2 + (x231 - x265)^2 + (x371 - x405)^2) + 1 / sqrt((x91 - x126)^2 + (x231
    - x266)^2 + (x371 - x406)^2) + 1 / sqrt((x91 - x127)^2 + (x231 - x267)^2
    + (x371 - x407)^2) + 1 / sqrt((x91 - x128)^2 + (x231 - x268)^2 + (x371 -
    x408)^2) + 1 / sqrt((x91 - x129)^2 + (x231 - x269)^2 + (x371 - x409)^2) + 1
    / sqrt((x91 - x130)^2 + (x231 - x270)^2 + (x371 - x410)^2) + 1 / sqrt((x91
    - x131)^2 + (x231 - x271)^2 + (x371 - x411)^2) + 1 / sqrt((x91 - x132)^2
    + (x231 - x272)^2 + (x371 - x412)^2) + 1 / sqrt((x91 - x133)^2 + (x231 -
    x273)^2 + (x371 - x413)^2) + 1 / sqrt((x91 - x134)^2 + (x231 - x274)^2 + (
    x371 - x414)^2) + 1 / sqrt((x91 - x135)^2 + (x231 - x275)^2 + (x371 - x415)
    ^2) + 1 / sqrt((x91 - x136)^2 + (x231 - x276)^2 + (x371 - x416)^2) + 1 /
    sqrt((x91 - x137)^2 + (x231 - x277)^2 + (x371 - x417)^2) + 1 / sqrt((x91 -
    x138)^2 + (x231 - x278)^2 + (x371 - x418)^2) + 1 / sqrt((x91 - x139)^2 + (
    x231 - x279)^2 + (x371 - x419)^2) + 1 / sqrt((x91 - x140)^2 + (x231 - x280)
    ^2 + (x371 - x420)^2) + 1 / sqrt((x92 - x93)^2 + (x232 - x233)^2 + (x372 -
    x373)^2) + 1 / sqrt((x92 - x94)^2 + (x232 - x234)^2 + (x372 - x374)^2) + 1
    / sqrt((x92 - x95)^2 + (x232 - x235)^2 + (x372 - x375)^2) + 1 / sqrt((x92
    - x96)^2 + (x232 - x236)^2 + (x372 - x376)^2) + 1 / sqrt((x92 - x97)^2 + (
    x232 - x237)^2 + (x372 - x377)^2) + 1 / sqrt((x92 - x98)^2 + (x232 - x238)^
    2 + (x372 - x378)^2) + 1 / sqrt((x92 - x99)^2 + (x232 - x239)^2 + (x372 -
    x379)^2) + 1 / sqrt((x92 - x100)^2 + (x232 - x240)^2 + (x372 - x380)^2) + 1
    / sqrt((x92 - x101)^2 + (x232 - x241)^2 + (x372 - x381)^2) + 1 / sqrt((x92
    - x102)^2 + (x232 - x242)^2 + (x372 - x382)^2) + 1 / sqrt((x92 - x103)^2
    + (x232 - x243)^2 + (x372 - x383)^2) + 1 / sqrt((x92 - x104)^2 + (x232 -
    x244)^2 + (x372 - x384)^2) + 1 / sqrt((x92 - x105)^2 + (x232 - x245)^2 + (
    x372 - x385)^2) + 1 / sqrt((x92 - x106)^2 + (x232 - x246)^2 + (x372 - x386)
    ^2) + 1 / sqrt((x92 - x107)^2 + (x232 - x247)^2 + (x372 - x387)^2) + 1 /
    sqrt((x92 - x108)^2 + (x232 - x248)^2 + (x372 - x388)^2) + 1 / sqrt((x92 -
    x109)^2 + (x232 - x249)^2 + (x372 - x389)^2) + 1 / sqrt((x92 - x110)^2 + (
    x232 - x250)^2 + (x372 - x390)^2) + 1 / sqrt((x92 - x111)^2 + (x232 - x251)
    ^2 + (x372 - x391)^2) + 1 / sqrt((x92 - x112)^2 + (x232 - x252)^2 + (x372
    - x392)^2) + 1 / sqrt((x92 - x113)^2 + (x232 - x253)^2 + (x372 - x393)^2)
    + 1 / sqrt((x92 - x114)^2 + (x232 - x254)^2 + (x372 - x394)^2) + 1 / sqrt(
    (x92 - x115)^2 + (x232 - x255)^2 + (x372 - x395)^2) + 1 / sqrt((x92 - x116)
    ^2 + (x232 - x256)^2 + (x372 - x396)^2) + 1 / sqrt((x92 - x117)^2 + (x232
    - x257)^2 + (x372 - x397)^2) + 1 / sqrt((x92 - x118)^2 + (x232 - x258)^2
    + (x372 - x398)^2) + 1 / sqrt((x92 - x119)^2 + (x232 - x259)^2 + (x372 -
    x399)^2) + 1 / sqrt((x92 - x120)^2 + (x232 - x260)^2 + (x372 - x400)^2) + 1
    / sqrt((x92 - x121)^2 + (x232 - x261)^2 + (x372 - x401)^2) + 1 / sqrt((x92
    - x122)^2 + (x232 - x262)^2 + (x372 - x402)^2) + 1 / sqrt((x92 - x123)^2
    + (x232 - x263)^2 + (x372 - x403)^2) + 1 / sqrt((x92 - x124)^2 + (x232 -
    x264)^2 + (x372 - x404)^2) + 1 / sqrt((x92 - x125)^2 + (x232 - x265)^2 + (
    x372 - x405)^2) + 1 / sqrt((x92 - x126)^2 + (x232 - x266)^2 + (x372 - x406)
    ^2) + 1 / sqrt((x92 - x127)^2 + (x232 - x267)^2 + (x372 - x407)^2) + 1 /
    sqrt((x92 - x128)^2 + (x232 - x268)^2 + (x372 - x408)^2) + 1 / sqrt((x92 -
    x129)^2 + (x232 - x269)^2 + (x372 - x409)^2) + 1 / sqrt((x92 - x130)^2 + (
    x232 - x270)^2 + (x372 - x410)^2) + 1 / sqrt((x92 - x131)^2 + (x232 - x271)
    ^2 + (x372 - x411)^2) + 1 / sqrt((x92 - x132)^2 + (x232 - x272)^2 + (x372
    - x412)^2) + 1 / sqrt((x92 - x133)^2 + (x232 - x273)^2 + (x372 - x413)^2)
    + 1 / sqrt((x92 - x134)^2 + (x232 - x274)^2 + (x372 - x414)^2) + 1 / sqrt(
    (x92 - x135)^2 + (x232 - x275)^2 + (x372 - x415)^2) + 1 / sqrt((x92 - x136)
    ^2 + (x232 - x276)^2 + (x372 - x416)^2) + 1 / sqrt((x92 - x137)^2 + (x232
    - x277)^2 + (x372 - x417)^2) + 1 / sqrt((x92 - x138)^2 + (x232 - x278)^2
    + (x372 - x418)^2) + 1 / sqrt((x92 - x139)^2 + (x232 - x279)^2 + (x372 -
    x419)^2) + 1 / sqrt((x92 - x140)^2 + (x232 - x280)^2 + (x372 - x420)^2) + 1
    / sqrt((x93 - x94)^2 + (x233 - x234)^2 + (x373 - x374)^2) + 1 / sqrt((x93
    - x95)^2 + (x233 - x235)^2 + (x373 - x375)^2) + 1 / sqrt((x93 - x96)^2 + (
    x233 - x236)^2 + (x373 - x376)^2) + 1 / sqrt((x93 - x97)^2 + (x233 - x237)^
    2 + (x373 - x377)^2) + 1 / sqrt((x93 - x98)^2 + (x233 - x238)^2 + (x373 -
    x378)^2) + 1 / sqrt((x93 - x99)^2 + (x233 - x239)^2 + (x373 - x379)^2) + 1
    / sqrt((x93 - x100)^2 + (x233 - x240)^2 + (x373 - x380)^2) + 1 / sqrt((x93
    - x101)^2 + (x233 - x241)^2 + (x373 - x381)^2) + 1 / sqrt((x93 - x102)^2
    + (x233 - x242)^2 + (x373 - x382)^2) + 1 / sqrt((x93 - x103)^2 + (x233 -
    x243)^2 + (x373 - x383)^2) + 1 / sqrt((x93 - x104)^2 + (x233 - x244)^2 + (
    x373 - x384)^2) + 1 / sqrt((x93 - x105)^2 + (x233 - x245)^2 + (x373 - x385)
    ^2) + 1 / sqrt((x93 - x106)^2 + (x233 - x246)^2 + (x373 - x386)^2) + 1 /
    sqrt((x93 - x107)^2 + (x233 - x247)^2 + (x373 - x387)^2) + 1 / sqrt((x93 -
    x108)^2 + (x233 - x248)^2 + (x373 - x388)^2) + 1 / sqrt((x93 - x109)^2 + (
    x233 - x249)^2 + (x373 - x389)^2) + 1 / sqrt((x93 - x110)^2 + (x233 - x250)
    ^2 + (x373 - x390)^2) + 1 / sqrt((x93 - x111)^2 + (x233 - x251)^2 + (x373
    - x391)^2) + 1 / sqrt((x93 - x112)^2 + (x233 - x252)^2 + (x373 - x392)^2)
    + 1 / sqrt((x93 - x113)^2 + (x233 - x253)^2 + (x373 - x393)^2) + 1 / sqrt(
    (x93 - x114)^2 + (x233 - x254)^2 + (x373 - x394)^2) + 1 / sqrt((x93 - x115)
    ^2 + (x233 - x255)^2 + (x373 - x395)^2) + 1 / sqrt((x93 - x116)^2 + (x233
    - x256)^2 + (x373 - x396)^2) + 1 / sqrt((x93 - x117)^2 + (x233 - x257)^2
    + (x373 - x397)^2) + 1 / sqrt((x93 - x118)^2 + (x233 - x258)^2 + (x373 -
    x398)^2) + 1 / sqrt((x93 - x119)^2 + (x233 - x259)^2 + (x373 - x399)^2) + 1
    / sqrt((x93 - x120)^2 + (x233 - x260)^2 + (x373 - x400)^2) + 1 / sqrt((x93
    - x121)^2 + (x233 - x261)^2 + (x373 - x401)^2) + 1 / sqrt((x93 - x122)^2
    + (x233 - x262)^2 + (x373 - x402)^2) + 1 / sqrt((x93 - x123)^2 + (x233 -
    x263)^2 + (x373 - x403)^2) + 1 / sqrt((x93 - x124)^2 + (x233 - x264)^2 + (
    x373 - x404)^2) + 1 / sqrt((x93 - x125)^2 + (x233 - x265)^2 + (x373 - x405)
    ^2) + 1 / sqrt((x93 - x126)^2 + (x233 - x266)^2 + (x373 - x406)^2) + 1 /
    sqrt((x93 - x127)^2 + (x233 - x267)^2 + (x373 - x407)^2) + 1 / sqrt((x93 -
    x128)^2 + (x233 - x268)^2 + (x373 - x408)^2) + 1 / sqrt((x93 - x129)^2 + (
    x233 - x269)^2 + (x373 - x409)^2) + 1 / sqrt((x93 - x130)^2 + (x233 - x270)
    ^2 + (x373 - x410)^2) + 1 / sqrt((x93 - x131)^2 + (x233 - x271)^2 + (x373
    - x411)^2) + 1 / sqrt((x93 - x132)^2 + (x233 - x272)^2 + (x373 - x412)^2)
    + 1 / sqrt((x93 - x133)^2 + (x233 - x273)^2 + (x373 - x413)^2) + 1 / sqrt(
    (x93 - x134)^2 + (x233 - x274)^2 + (x373 - x414)^2) + 1 / sqrt((x93 - x135)
    ^2 + (x233 - x275)^2 + (x373 - x415)^2) + 1 / sqrt((x93 - x136)^2 + (x233
    - x276)^2 + (x373 - x416)^2) + 1 / sqrt((x93 - x137)^2 + (x233 - x277)^2
    + (x373 - x417)^2) + 1 / sqrt((x93 - x138)^2 + (x233 - x278)^2 + (x373 -
    x418)^2) + 1 / sqrt((x93 - x139)^2 + (x233 - x279)^2 + (x373 - x419)^2) + 1
    / sqrt((x93 - x140)^2 + (x233 - x280)^2 + (x373 - x420)^2) + 1 / sqrt((x94
    - x95)^2 + (x234 - x235)^2 + (x374 - x375)^2) + 1 / sqrt((x94 - x96)^2 + (
    x234 - x236)^2 + (x374 - x376)^2) + 1 / sqrt((x94 - x97)^2 + (x234 - x237)^
    2 + (x374 - x377)^2) + 1 / sqrt((x94 - x98)^2 + (x234 - x238)^2 + (x374 -
    x378)^2) + 1 / sqrt((x94 - x99)^2 + (x234 - x239)^2 + (x374 - x379)^2) + 1
    / sqrt((x94 - x100)^2 + (x234 - x240)^2 + (x374 - x380)^2) + 1 / sqrt((x94
    - x101)^2 + (x234 - x241)^2 + (x374 - x381)^2) + 1 / sqrt((x94 - x102)^2
    + (x234 - x242)^2 + (x374 - x382)^2) + 1 / sqrt((x94 - x103)^2 + (x234 -
    x243)^2 + (x374 - x383)^2) + 1 / sqrt((x94 - x104)^2 + (x234 - x244)^2 + (
    x374 - x384)^2) + 1 / sqrt((x94 - x105)^2 + (x234 - x245)^2 + (x374 - x385)
    ^2) + 1 / sqrt((x94 - x106)^2 + (x234 - x246)^2 + (x374 - x386)^2) + 1 /
    sqrt((x94 - x107)^2 + (x234 - x247)^2 + (x374 - x387)^2) + 1 / sqrt((x94 -
    x108)^2 + (x234 - x248)^2 + (x374 - x388)^2) + 1 / sqrt((x94 - x109)^2 + (
    x234 - x249)^2 + (x374 - x389)^2) + 1 / sqrt((x94 - x110)^2 + (x234 - x250)
    ^2 + (x374 - x390)^2) + 1 / sqrt((x94 - x111)^2 + (x234 - x251)^2 + (x374
    - x391)^2) + 1 / sqrt((x94 - x112)^2 + (x234 - x252)^2 + (x374 - x392)^2)
    + 1 / sqrt((x94 - x113)^2 + (x234 - x253)^2 + (x374 - x393)^2) + 1 / sqrt(
    (x94 - x114)^2 + (x234 - x254)^2 + (x374 - x394)^2) + 1 / sqrt((x94 - x115)
    ^2 + (x234 - x255)^2 + (x374 - x395)^2) + 1 / sqrt((x94 - x116)^2 + (x234
    - x256)^2 + (x374 - x396)^2) + 1 / sqrt((x94 - x117)^2 + (x234 - x257)^2
    + (x374 - x397)^2) + 1 / sqrt((x94 - x118)^2 + (x234 - x258)^2 + (x374 -
    x398)^2) + 1 / sqrt((x94 - x119)^2 + (x234 - x259)^2 + (x374 - x399)^2) + 1
    / sqrt((x94 - x120)^2 + (x234 - x260)^2 + (x374 - x400)^2) + 1 / sqrt((x94
    - x121)^2 + (x234 - x261)^2 + (x374 - x401)^2) + 1 / sqrt((x94 - x122)^2
    + (x234 - x262)^2 + (x374 - x402)^2) + 1 / sqrt((x94 - x123)^2 + (x234 -
    x263)^2 + (x374 - x403)^2) + 1 / sqrt((x94 - x124)^2 + (x234 - x264)^2 + (
    x374 - x404)^2) + 1 / sqrt((x94 - x125)^2 + (x234 - x265)^2 + (x374 - x405)
    ^2) + 1 / sqrt((x94 - x126)^2 + (x234 - x266)^2 + (x374 - x406)^2) + 1 /
    sqrt((x94 - x127)^2 + (x234 - x267)^2 + (x374 - x407)^2) + 1 / sqrt((x94 -
    x128)^2 + (x234 - x268)^2 + (x374 - x408)^2) + 1 / sqrt((x94 - x129)^2 + (
    x234 - x269)^2 + (x374 - x409)^2) + 1 / sqrt((x94 - x130)^2 + (x234 - x270)
    ^2 + (x374 - x410)^2) + 1 / sqrt((x94 - x131)^2 + (x234 - x271)^2 + (x374
    - x411)^2) + 1 / sqrt((x94 - x132)^2 + (x234 - x272)^2 + (x374 - x412)^2)
    + 1 / sqrt((x94 - x133)^2 + (x234 - x273)^2 + (x374 - x413)^2) + 1 / sqrt(
    (x94 - x134)^2 + (x234 - x274)^2 + (x374 - x414)^2) + 1 / sqrt((x94 - x135)
    ^2 + (x234 - x275)^2 + (x374 - x415)^2) + 1 / sqrt((x94 - x136)^2 + (x234
    - x276)^2 + (x374 - x416)^2) + 1 / sqrt((x94 - x137)^2 + (x234 - x277)^2
    + (x374 - x417)^2) + 1 / sqrt((x94 - x138)^2 + (x234 - x278)^2 + (x374 -
    x418)^2) + 1 / sqrt((x94 - x139)^2 + (x234 - x279)^2 + (x374 - x419)^2) + 1
    / sqrt((x94 - x140)^2 + (x234 - x280)^2 + (x374 - x420)^2) + 1 / sqrt((x95
    - x96)^2 + (x235 - x236)^2 + (x375 - x376)^2) + 1 / sqrt((x95 - x97)^2 + (
    x235 - x237)^2 + (x375 - x377)^2) + 1 / sqrt((x95 - x98)^2 + (x235 - x238)^
    2 + (x375 - x378)^2) + 1 / sqrt((x95 - x99)^2 + (x235 - x239)^2 + (x375 -
    x379)^2) + 1 / sqrt((x95 - x100)^2 + (x235 - x240)^2 + (x375 - x380)^2) + 1
    / sqrt((x95 - x101)^2 + (x235 - x241)^2 + (x375 - x381)^2) + 1 / sqrt((x95
    - x102)^2 + (x235 - x242)^2 + (x375 - x382)^2) + 1 / sqrt((x95 - x103)^2
    + (x235 - x243)^2 + (x375 - x383)^2) + 1 / sqrt((x95 - x104)^2 + (x235 -
    x244)^2 + (x375 - x384)^2) + 1 / sqrt((x95 - x105)^2 + (x235 - x245)^2 + (
    x375 - x385)^2) + 1 / sqrt((x95 - x106)^2 + (x235 - x246)^2 + (x375 - x386)
    ^2) + 1 / sqrt((x95 - x107)^2 + (x235 - x247)^2 + (x375 - x387)^2) + 1 /
    sqrt((x95 - x108)^2 + (x235 - x248)^2 + (x375 - x388)^2) + 1 / sqrt((x95 -
    x109)^2 + (x235 - x249)^2 + (x375 - x389)^2) + 1 / sqrt((x95 - x110)^2 + (
    x235 - x250)^2 + (x375 - x390)^2) + 1 / sqrt((x95 - x111)^2 + (x235 - x251)
    ^2 + (x375 - x391)^2) + 1 / sqrt((x95 - x112)^2 + (x235 - x252)^2 + (x375
    - x392)^2) + 1 / sqrt((x95 - x113)^2 + (x235 - x253)^2 + (x375 - x393)^2)
    + 1 / sqrt((x95 - x114)^2 + (x235 - x254)^2 + (x375 - x394)^2) + 1 / sqrt(
    (x95 - x115)^2 + (x235 - x255)^2 + (x375 - x395)^2) + 1 / sqrt((x95 - x116)
    ^2 + (x235 - x256)^2 + (x375 - x396)^2) + 1 / sqrt((x95 - x117)^2 + (x235
    - x257)^2 + (x375 - x397)^2) + 1 / sqrt((x95 - x118)^2 + (x235 - x258)^2
    + (x375 - x398)^2) + 1 / sqrt((x95 - x119)^2 + (x235 - x259)^2 + (x375 -
    x399)^2) + 1 / sqrt((x95 - x120)^2 + (x235 - x260)^2 + (x375 - x400)^2) + 1
    / sqrt((x95 - x121)^2 + (x235 - x261)^2 + (x375 - x401)^2) + 1 / sqrt((x95
    - x122)^2 + (x235 - x262)^2 + (x375 - x402)^2) + 1 / sqrt((x95 - x123)^2
    + (x235 - x263)^2 + (x375 - x403)^2) + 1 / sqrt((x95 - x124)^2 + (x235 -
    x264)^2 + (x375 - x404)^2) + 1 / sqrt((x95 - x125)^2 + (x235 - x265)^2 + (
    x375 - x405)^2) + 1 / sqrt((x95 - x126)^2 + (x235 - x266)^2 + (x375 - x406)
    ^2) + 1 / sqrt((x95 - x127)^2 + (x235 - x267)^2 + (x375 - x407)^2) + 1 /
    sqrt((x95 - x128)^2 + (x235 - x268)^2 + (x375 - x408)^2) + 1 / sqrt((x95 -
    x129)^2 + (x235 - x269)^2 + (x375 - x409)^2) + 1 / sqrt((x95 - x130)^2 + (
    x235 - x270)^2 + (x375 - x410)^2) + 1 / sqrt((x95 - x131)^2 + (x235 - x271)
    ^2 + (x375 - x411)^2) + 1 / sqrt((x95 - x132)^2 + (x235 - x272)^2 + (x375
    - x412)^2) + 1 / sqrt((x95 - x133)^2 + (x235 - x273)^2 + (x375 - x413)^2)
    + 1 / sqrt((x95 - x134)^2 + (x235 - x274)^2 + (x375 - x414)^2) + 1 / sqrt(
    (x95 - x135)^2 + (x235 - x275)^2 + (x375 - x415)^2) + 1 / sqrt((x95 - x136)
    ^2 + (x235 - x276)^2 + (x375 - x416)^2) + 1 / sqrt((x95 - x137)^2 + (x235
    - x277)^2 + (x375 - x417)^2) + 1 / sqrt((x95 - x138)^2 + (x235 - x278)^2
    + (x375 - x418)^2) + 1 / sqrt((x95 - x139)^2 + (x235 - x279)^2 + (x375 -
    x419)^2) + 1 / sqrt((x95 - x140)^2 + (x235 - x280)^2 + (x375 - x420)^2) + 1
    / sqrt((x96 - x97)^2 + (x236 - x237)^2 + (x376 - x377)^2) + 1 / sqrt((x96
    - x98)^2 + (x236 - x238)^2 + (x376 - x378)^2) + 1 / sqrt((x96 - x99)^2 + (
    x236 - x239)^2 + (x376 - x379)^2) + 1 / sqrt((x96 - x100)^2 + (x236 - x240)
    ^2 + (x376 - x380)^2) + 1 / sqrt((x96 - x101)^2 + (x236 - x241)^2 + (x376
    - x381)^2) + 1 / sqrt((x96 - x102)^2 + (x236 - x242)^2 + (x376 - x382)^2)
    + 1 / sqrt((x96 - x103)^2 + (x236 - x243)^2 + (x376 - x383)^2) + 1 / sqrt(
    (x96 - x104)^2 + (x236 - x244)^2 + (x376 - x384)^2) + 1 / sqrt((x96 - x105)
    ^2 + (x236 - x245)^2 + (x376 - x385)^2) + 1 / sqrt((x96 - x106)^2 + (x236
    - x246)^2 + (x376 - x386)^2) + 1 / sqrt((x96 - x107)^2 + (x236 - x247)^2
    + (x376 - x387)^2) + 1 / sqrt((x96 - x108)^2 + (x236 - x248)^2 + (x376 -
    x388)^2) + 1 / sqrt((x96 - x109)^2 + (x236 - x249)^2 + (x376 - x389)^2) + 1
    / sqrt((x96 - x110)^2 + (x236 - x250)^2 + (x376 - x390)^2) + 1 / sqrt((x96
    - x111)^2 + (x236 - x251)^2 + (x376 - x391)^2) + 1 / sqrt((x96 - x112)^2
    + (x236 - x252)^2 + (x376 - x392)^2) + 1 / sqrt((x96 - x113)^2 + (x236 -
    x253)^2 + (x376 - x393)^2) + 1 / sqrt((x96 - x114)^2 + (x236 - x254)^2 + (
    x376 - x394)^2) + 1 / sqrt((x96 - x115)^2 + (x236 - x255)^2 + (x376 - x395)
    ^2) + 1 / sqrt((x96 - x116)^2 + (x236 - x256)^2 + (x376 - x396)^2) + 1 /
    sqrt((x96 - x117)^2 + (x236 - x257)^2 + (x376 - x397)^2) + 1 / sqrt((x96 -
    x118)^2 + (x236 - x258)^2 + (x376 - x398)^2) + 1 / sqrt((x96 - x119)^2 + (
    x236 - x259)^2 + (x376 - x399)^2) + 1 / sqrt((x96 - x120)^2 + (x236 - x260)
    ^2 + (x376 - x400)^2) + 1 / sqrt((x96 - x121)^2 + (x236 - x261)^2 + (x376
    - x401)^2) + 1 / sqrt((x96 - x122)^2 + (x236 - x262)^2 + (x376 - x402)^2)
    + 1 / sqrt((x96 - x123)^2 + (x236 - x263)^2 + (x376 - x403)^2) + 1 / sqrt(
    (x96 - x124)^2 + (x236 - x264)^2 + (x376 - x404)^2) + 1 / sqrt((x96 - x125)
    ^2 + (x236 - x265)^2 + (x376 - x405)^2) + 1 / sqrt((x96 - x126)^2 + (x236
    - x266)^2 + (x376 - x406)^2) + 1 / sqrt((x96 - x127)^2 + (x236 - x267)^2
    + (x376 - x407)^2) + 1 / sqrt((x96 - x128)^2 + (x236 - x268)^2 + (x376 -
    x408)^2) + 1 / sqrt((x96 - x129)^2 + (x236 - x269)^2 + (x376 - x409)^2) + 1
    / sqrt((x96 - x130)^2 + (x236 - x270)^2 + (x376 - x410)^2) + 1 / sqrt((x96
    - x131)^2 + (x236 - x271)^2 + (x376 - x411)^2) + 1 / sqrt((x96 - x132)^2
    + (x236 - x272)^2 + (x376 - x412)^2) + 1 / sqrt((x96 - x133)^2 + (x236 -
    x273)^2 + (x376 - x413)^2) + 1 / sqrt((x96 - x134)^2 + (x236 - x274)^2 + (
    x376 - x414)^2) + 1 / sqrt((x96 - x135)^2 + (x236 - x275)^2 + (x376 - x415)
    ^2) + 1 / sqrt((x96 - x136)^2 + (x236 - x276)^2 + (x376 - x416)^2) + 1 /
    sqrt((x96 - x137)^2 + (x236 - x277)^2 + (x376 - x417)^2) + 1 / sqrt((x96 -
    x138)^2 + (x236 - x278)^2 + (x376 - x418)^2) + 1 / sqrt((x96 - x139)^2 + (
    x236 - x279)^2 + (x376 - x419)^2) + 1 / sqrt((x96 - x140)^2 + (x236 - x280)
    ^2 + (x376 - x420)^2) + 1 / sqrt((x97 - x98)^2 + (x237 - x238)^2 + (x377 -
    x378)^2) + 1 / sqrt((x97 - x99)^2 + (x237 - x239)^2 + (x377 - x379)^2) + 1
    / sqrt((x97 - x100)^2 + (x237 - x240)^2 + (x377 - x380)^2) + 1 / sqrt((x97
    - x101)^2 + (x237 - x241)^2 + (x377 - x381)^2) + 1 / sqrt((x97 - x102)^2
    + (x237 - x242)^2 + (x377 - x382)^2) + 1 / sqrt((x97 - x103)^2 + (x237 -
    x243)^2 + (x377 - x383)^2) + 1 / sqrt((x97 - x104)^2 + (x237 - x244)^2 + (
    x377 - x384)^2) + 1 / sqrt((x97 - x105)^2 + (x237 - x245)^2 + (x377 - x385)
    ^2) + 1 / sqrt((x97 - x106)^2 + (x237 - x246)^2 + (x377 - x386)^2) + 1 /
    sqrt((x97 - x107)^2 + (x237 - x247)^2 + (x377 - x387)^2) + 1 / sqrt((x97 -
    x108)^2 + (x237 - x248)^2 + (x377 - x388)^2) + 1 / sqrt((x97 - x109)^2 + (
    x237 - x249)^2 + (x377 - x389)^2) + 1 / sqrt((x97 - x110)^2 + (x237 - x250)
    ^2 + (x377 - x390)^2) + 1 / sqrt((x97 - x111)^2 + (x237 - x251)^2 + (x377
    - x391)^2) + 1 / sqrt((x97 - x112)^2 + (x237 - x252)^2 + (x377 - x392)^2)
    + 1 / sqrt((x97 - x113)^2 + (x237 - x253)^2 + (x377 - x393)^2) + 1 / sqrt(
    (x97 - x114)^2 + (x237 - x254)^2 + (x377 - x394)^2) + 1 / sqrt((x97 - x115)
    ^2 + (x237 - x255)^2 + (x377 - x395)^2) + 1 / sqrt((x97 - x116)^2 + (x237
    - x256)^2 + (x377 - x396)^2) + 1 / sqrt((x97 - x117)^2 + (x237 - x257)^2
    + (x377 - x397)^2) + 1 / sqrt((x97 - x118)^2 + (x237 - x258)^2 + (x377 -
    x398)^2) + 1 / sqrt((x97 - x119)^2 + (x237 - x259)^2 + (x377 - x399)^2) + 1
    / sqrt((x97 - x120)^2 + (x237 - x260)^2 + (x377 - x400)^2) + 1 / sqrt((x97
    - x121)^2 + (x237 - x261)^2 + (x377 - x401)^2) + 1 / sqrt((x97 - x122)^2
    + (x237 - x262)^2 + (x377 - x402)^2) + 1 / sqrt((x97 - x123)^2 + (x237 -
    x263)^2 + (x377 - x403)^2) + 1 / sqrt((x97 - x124)^2 + (x237 - x264)^2 + (
    x377 - x404)^2) + 1 / sqrt((x97 - x125)^2 + (x237 - x265)^2 + (x377 - x405)
    ^2) + 1 / sqrt((x97 - x126)^2 + (x237 - x266)^2 + (x377 - x406)^2) + 1 /
    sqrt((x97 - x127)^2 + (x237 - x267)^2 + (x377 - x407)^2) + 1 / sqrt((x97 -
    x128)^2 + (x237 - x268)^2 + (x377 - x408)^2) + 1 / sqrt((x97 - x129)^2 + (
    x237 - x269)^2 + (x377 - x409)^2) + 1 / sqrt((x97 - x130)^2 + (x237 - x270)
    ^2 + (x377 - x410)^2) + 1 / sqrt((x97 - x131)^2 + (x237 - x271)^2 + (x377
    - x411)^2) + 1 / sqrt((x97 - x132)^2 + (x237 - x272)^2 + (x377 - x412)^2)
    + 1 / sqrt((x97 - x133)^2 + (x237 - x273)^2 + (x377 - x413)^2) + 1 / sqrt(
    (x97 - x134)^2 + (x237 - x274)^2 + (x377 - x414)^2) + 1 / sqrt((x97 - x135)
    ^2 + (x237 - x275)^2 + (x377 - x415)^2) + 1 / sqrt((x97 - x136)^2 + (x237
    - x276)^2 + (x377 - x416)^2) + 1 / sqrt((x97 - x137)^2 + (x237 - x277)^2
    + (x377 - x417)^2) + 1 / sqrt((x97 - x138)^2 + (x237 - x278)^2 + (x377 -
    x418)^2) + 1 / sqrt((x97 - x139)^2 + (x237 - x279)^2 + (x377 - x419)^2) + 1
    / sqrt((x97 - x140)^2 + (x237 - x280)^2 + (x377 - x420)^2) + 1 / sqrt((x98
    - x99)^2 + (x238 - x239)^2 + (x378 - x379)^2) + 1 / sqrt((x98 - x100)^2 +
    (x238 - x240)^2 + (x378 - x380)^2) + 1 / sqrt((x98 - x101)^2 + (x238 - x241)
    ^2 + (x378 - x381)^2) + 1 / sqrt((x98 - x102)^2 + (x238 - x242)^2 + (x378
    - x382)^2) + 1 / sqrt((x98 - x103)^2 + (x238 - x243)^2 + (x378 - x383)^2)
    + 1 / sqrt((x98 - x104)^2 + (x238 - x244)^2 + (x378 - x384)^2) + 1 / sqrt(
    (x98 - x105)^2 + (x238 - x245)^2 + (x378 - x385)^2) + 1 / sqrt((x98 - x106)
    ^2 + (x238 - x246)^2 + (x378 - x386)^2) + 1 / sqrt((x98 - x107)^2 + (x238
    - x247)^2 + (x378 - x387)^2) + 1 / sqrt((x98 - x108)^2 + (x238 - x248)^2
    + (x378 - x388)^2) + 1 / sqrt((x98 - x109)^2 + (x238 - x249)^2 + (x378 -
    x389)^2) + 1 / sqrt((x98 - x110)^2 + (x238 - x250)^2 + (x378 - x390)^2) + 1
    / sqrt((x98 - x111)^2 + (x238 - x251)^2 + (x378 - x391)^2) + 1 / sqrt((x98
    - x112)^2 + (x238 - x252)^2 + (x378 - x392)^2) + 1 / sqrt((x98 - x113)^2
    + (x238 - x253)^2 + (x378 - x393)^2) + 1 / sqrt((x98 - x114)^2 + (x238 -
    x254)^2 + (x378 - x394)^2) + 1 / sqrt((x98 - x115)^2 + (x238 - x255)^2 + (
    x378 - x395)^2) + 1 / sqrt((x98 - x116)^2 + (x238 - x256)^2 + (x378 - x396)
    ^2) + 1 / sqrt((x98 - x117)^2 + (x238 - x257)^2 + (x378 - x397)^2) + 1 /
    sqrt((x98 - x118)^2 + (x238 - x258)^2 + (x378 - x398)^2) + 1 / sqrt((x98 -
    x119)^2 + (x238 - x259)^2 + (x378 - x399)^2) + 1 / sqrt((x98 - x120)^2 + (
    x238 - x260)^2 + (x378 - x400)^2) + 1 / sqrt((x98 - x121)^2 + (x238 - x261)
    ^2 + (x378 - x401)^2) + 1 / sqrt((x98 - x122)^2 + (x238 - x262)^2 + (x378
    - x402)^2) + 1 / sqrt((x98 - x123)^2 + (x238 - x263)^2 + (x378 - x403)^2)
    + 1 / sqrt((x98 - x124)^2 + (x238 - x264)^2 + (x378 - x404)^2) + 1 / sqrt(
    (x98 - x125)^2 + (x238 - x265)^2 + (x378 - x405)^2) + 1 / sqrt((x98 - x126)
    ^2 + (x238 - x266)^2 + (x378 - x406)^2) + 1 / sqrt((x98 - x127)^2 + (x238
    - x267)^2 + (x378 - x407)^2) + 1 / sqrt((x98 - x128)^2 + (x238 - x268)^2
    + (x378 - x408)^2) + 1 / sqrt((x98 - x129)^2 + (x238 - x269)^2 + (x378 -
    x409)^2) + 1 / sqrt((x98 - x130)^2 + (x238 - x270)^2 + (x378 - x410)^2) + 1
    / sqrt((x98 - x131)^2 + (x238 - x271)^2 + (x378 - x411)^2) + 1 / sqrt((x98
    - x132)^2 + (x238 - x272)^2 + (x378 - x412)^2) + 1 / sqrt((x98 - x133)^2
    + (x238 - x273)^2 + (x378 - x413)^2) + 1 / sqrt((x98 - x134)^2 + (x238 -
    x274)^2 + (x378 - x414)^2) + 1 / sqrt((x98 - x135)^2 + (x238 - x275)^2 + (
    x378 - x415)^2) + 1 / sqrt((x98 - x136)^2 + (x238 - x276)^2 + (x378 - x416)
    ^2) + 1 / sqrt((x98 - x137)^2 + (x238 - x277)^2 + (x378 - x417)^2) + 1 /
    sqrt((x98 - x138)^2 + (x238 - x278)^2 + (x378 - x418)^2) + 1 / sqrt((x98 -
    x139)^2 + (x238 - x279)^2 + (x378 - x419)^2) + 1 / sqrt((x98 - x140)^2 + (
    x238 - x280)^2 + (x378 - x420)^2) + 1 / sqrt((x99 - x100)^2 + (x239 - x240)
    ^2 + (x379 - x380)^2) + 1 / sqrt((x99 - x101)^2 + (x239 - x241)^2 + (x379
    - x381)^2) + 1 / sqrt((x99 - x102)^2 + (x239 - x242)^2 + (x379 - x382)^2)
    + 1 / sqrt((x99 - x103)^2 + (x239 - x243)^2 + (x379 - x383)^2) + 1 / sqrt(
    (x99 - x104)^2 + (x239 - x244)^2 + (x379 - x384)^2) + 1 / sqrt((x99 - x105)
    ^2 + (x239 - x245)^2 + (x379 - x385)^2) + 1 / sqrt((x99 - x106)^2 + (x239
    - x246)^2 + (x379 - x386)^2) + 1 / sqrt((x99 - x107)^2 + (x239 - x247)^2
    + (x379 - x387)^2) + 1 / sqrt((x99 - x108)^2 + (x239 - x248)^2 + (x379 -
    x388)^2) + 1 / sqrt((x99 - x109)^2 + (x239 - x249)^2 + (x379 - x389)^2) + 1
    / sqrt((x99 - x110)^2 + (x239 - x250)^2 + (x379 - x390)^2) + 1 / sqrt((x99
    - x111)^2 + (x239 - x251)^2 + (x379 - x391)^2) + 1 / sqrt((x99 - x112)^2
    + (x239 - x252)^2 + (x379 - x392)^2) + 1 / sqrt((x99 - x113)^2 + (x239 -
    x253)^2 + (x379 - x393)^2) + 1 / sqrt((x99 - x114)^2 + (x239 - x254)^2 + (
    x379 - x394)^2) + 1 / sqrt((x99 - x115)^2 + (x239 - x255)^2 + (x379 - x395)
    ^2) + 1 / sqrt((x99 - x116)^2 + (x239 - x256)^2 + (x379 - x396)^2) + 1 /
    sqrt((x99 - x117)^2 + (x239 - x257)^2 + (x379 - x397)^2) + 1 / sqrt((x99 -
    x118)^2 + (x239 - x258)^2 + (x379 - x398)^2) + 1 / sqrt((x99 - x119)^2 + (
    x239 - x259)^2 + (x379 - x399)^2) + 1 / sqrt((x99 - x120)^2 + (x239 - x260)
    ^2 + (x379 - x400)^2) + 1 / sqrt((x99 - x121)^2 + (x239 - x261)^2 + (x379
    - x401)^2) + 1 / sqrt((x99 - x122)^2 + (x239 - x262)^2 + (x379 - x402)^2)
    + 1 / sqrt((x99 - x123)^2 + (x239 - x263)^2 + (x379 - x403)^2) + 1 / sqrt(
    (x99 - x124)^2 + (x239 - x264)^2 + (x379 - x404)^2) + 1 / sqrt((x99 - x125)
    ^2 + (x239 - x265)^2 + (x379 - x405)^2) + 1 / sqrt((x99 - x126)^2 + (x239
    - x266)^2 + (x379 - x406)^2) + 1 / sqrt((x99 - x127)^2 + (x239 - x267)^2
    + (x379 - x407)^2) + 1 / sqrt((x99 - x128)^2 + (x239 - x268)^2 + (x379 -
    x408)^2) + 1 / sqrt((x99 - x129)^2 + (x239 - x269)^2 + (x379 - x409)^2) + 1
    / sqrt((x99 - x130)^2 + (x239 - x270)^2 + (x379 - x410)^2) + 1 / sqrt((x99
    - x131)^2 + (x239 - x271)^2 + (x379 - x411)^2) + 1 / sqrt((x99 - x132)^2
    + (x239 - x272)^2 + (x379 - x412)^2) + 1 / sqrt((x99 - x133)^2 + (x239 -
    x273)^2 + (x379 - x413)^2) + 1 / sqrt((x99 - x134)^2 + (x239 - x274)^2 + (
    x379 - x414)^2) + 1 / sqrt((x99 - x135)^2 + (x239 - x275)^2 + (x379 - x415)
    ^2) + 1 / sqrt((x99 - x136)^2 + (x239 - x276)^2 + (x379 - x416)^2) + 1 /
    sqrt((x99 - x137)^2 + (x239 - x277)^2 + (x379 - x417)^2) + 1 / sqrt((x99 -
    x138)^2 + (x239 - x278)^2 + (x379 - x418)^2) + 1 / sqrt((x99 - x139)^2 + (
    x239 - x279)^2 + (x379 - x419)^2) + 1 / sqrt((x99 - x140)^2 + (x239 - x280)
    ^2 + (x379 - x420)^2) + 1 / sqrt((x100 - x101)^2 + (x240 - x241)^2 + (x380
    - x381)^2) + 1 / sqrt((x100 - x102)^2 + (x240 - x242)^2 + (x380 - x382)^2)
    + 1 / sqrt((x100 - x103)^2 + (x240 - x243)^2 + (x380 - x383)^2) + 1 /
    sqrt((x100 - x104)^2 + (x240 - x244)^2 + (x380 - x384)^2) + 1 / sqrt((x100
    - x105)^2 + (x240 - x245)^2 + (x380 - x385)^2) + 1 / sqrt((x100 - x106)^2
    + (x240 - x246)^2 + (x380 - x386)^2) + 1 / sqrt((x100 - x107)^2 + (x240 -
    x247)^2 + (x380 - x387)^2) + 1 / sqrt((x100 - x108)^2 + (x240 - x248)^2 + (
    x380 - x388)^2) + 1 / sqrt((x100 - x109)^2 + (x240 - x249)^2 + (x380 - x389)
    ^2) + 1 / sqrt((x100 - x110)^2 + (x240 - x250)^2 + (x380 - x390)^2) + 1 /
    sqrt((x100 - x111)^2 + (x240 - x251)^2 + (x380 - x391)^2) + 1 / sqrt((x100
    - x112)^2 + (x240 - x252)^2 + (x380 - x392)^2) + 1 / sqrt((x100 - x113)^2
    + (x240 - x253)^2 + (x380 - x393)^2) + 1 / sqrt((x100 - x114)^2 + (x240 -
    x254)^2 + (x380 - x394)^2) + 1 / sqrt((x100 - x115)^2 + (x240 - x255)^2 + (
    x380 - x395)^2) + 1 / sqrt((x100 - x116)^2 + (x240 - x256)^2 + (x380 - x396)
    ^2) + 1 / sqrt((x100 - x117)^2 + (x240 - x257)^2 + (x380 - x397)^2) + 1 /
    sqrt((x100 - x118)^2 + (x240 - x258)^2 + (x380 - x398)^2) + 1 / sqrt((x100
    - x119)^2 + (x240 - x259)^2 + (x380 - x399)^2) + 1 / sqrt((x100 - x120)^2
    + (x240 - x260)^2 + (x380 - x400)^2) + 1 / sqrt((x100 - x121)^2 + (x240 -
    x261)^2 + (x380 - x401)^2) + 1 / sqrt((x100 - x122)^2 + (x240 - x262)^2 + (
    x380 - x402)^2) + 1 / sqrt((x100 - x123)^2 + (x240 - x263)^2 + (x380 - x403)
    ^2) + 1 / sqrt((x100 - x124)^2 + (x240 - x264)^2 + (x380 - x404)^2) + 1 /
    sqrt((x100 - x125)^2 + (x240 - x265)^2 + (x380 - x405)^2) + 1 / sqrt((x100
    - x126)^2 + (x240 - x266)^2 + (x380 - x406)^2) + 1 / sqrt((x100 - x127)^2
    + (x240 - x267)^2 + (x380 - x407)^2) + 1 / sqrt((x100 - x128)^2 + (x240 -
    x268)^2 + (x380 - x408)^2) + 1 / sqrt((x100 - x129)^2 + (x240 - x269)^2 + (
    x380 - x409)^2) + 1 / sqrt((x100 - x130)^2 + (x240 - x270)^2 + (x380 - x410)
    ^2) + 1 / sqrt((x100 - x131)^2 + (x240 - x271)^2 + (x380 - x411)^2) + 1 /
    sqrt((x100 - x132)^2 + (x240 - x272)^2 + (x380 - x412)^2) + 1 / sqrt((x100
    - x133)^2 + (x240 - x273)^2 + (x380 - x413)^2) + 1 / sqrt((x100 - x134)^2
    + (x240 - x274)^2 + (x380 - x414)^2) + 1 / sqrt((x100 - x135)^2 + (x240 -
    x275)^2 + (x380 - x415)^2) + 1 / sqrt((x100 - x136)^2 + (x240 - x276)^2 + (
    x380 - x416)^2) + 1 / sqrt((x100 - x137)^2 + (x240 - x277)^2 + (x380 - x417)
    ^2) + 1 / sqrt((x100 - x138)^2 + (x240 - x278)^2 + (x380 - x418)^2) + 1 /
    sqrt((x100 - x139)^2 + (x240 - x279)^2 + (x380 - x419)^2) + 1 / sqrt((x100
    - x140)^2 + (x240 - x280)^2 + (x380 - x420)^2) + 1 / sqrt((x101 - x102)^2
    + (x241 - x242)^2 + (x381 - x382)^2) + 1 / sqrt((x101 - x103)^2 + (x241 -
    x243)^2 + (x381 - x383)^2) + 1 / sqrt((x101 - x104)^2 + (x241 - x244)^2 + (
    x381 - x384)^2) + 1 / sqrt((x101 - x105)^2 + (x241 - x245)^2 + (x381 - x385)
    ^2) + 1 / sqrt((x101 - x106)^2 + (x241 - x246)^2 + (x381 - x386)^2) + 1 /
    sqrt((x101 - x107)^2 + (x241 - x247)^2 + (x381 - x387)^2) + 1 / sqrt((x101
    - x108)^2 + (x241 - x248)^2 + (x381 - x388)^2) + 1 / sqrt((x101 - x109)^2
    + (x241 - x249)^2 + (x381 - x389)^2) + 1 / sqrt((x101 - x110)^2 + (x241 -
    x250)^2 + (x381 - x390)^2) + 1 / sqrt((x101 - x111)^2 + (x241 - x251)^2 + (
    x381 - x391)^2) + 1 / sqrt((x101 - x112)^2 + (x241 - x252)^2 + (x381 - x392)
    ^2) + 1 / sqrt((x101 - x113)^2 + (x241 - x253)^2 + (x381 - x393)^2) + 1 /
    sqrt((x101 - x114)^2 + (x241 - x254)^2 + (x381 - x394)^2) + 1 / sqrt((x101
    - x115)^2 + (x241 - x255)^2 + (x381 - x395)^2) + 1 / sqrt((x101 - x116)^2
    + (x241 - x256)^2 + (x381 - x396)^2) + 1 / sqrt((x101 - x117)^2 + (x241 -
    x257)^2 + (x381 - x397)^2) + 1 / sqrt((x101 - x118)^2 + (x241 - x258)^2 + (
    x381 - x398)^2) + 1 / sqrt((x101 - x119)^2 + (x241 - x259)^2 + (x381 - x399)
    ^2) + 1 / sqrt((x101 - x120)^2 + (x241 - x260)^2 + (x381 - x400)^2) + 1 /
    sqrt((x101 - x121)^2 + (x241 - x261)^2 + (x381 - x401)^2) + 1 / sqrt((x101
    - x122)^2 + (x241 - x262)^2 + (x381 - x402)^2) + 1 / sqrt((x101 - x123)^2
    + (x241 - x263)^2 + (x381 - x403)^2) + 1 / sqrt((x101 - x124)^2 + (x241 -
    x264)^2 + (x381 - x404)^2) + 1 / sqrt((x101 - x125)^2 + (x241 - x265)^2 + (
    x381 - x405)^2) + 1 / sqrt((x101 - x126)^2 + (x241 - x266)^2 + (x381 - x406)
    ^2) + 1 / sqrt((x101 - x127)^2 + (x241 - x267)^2 + (x381 - x407)^2) + 1 /
    sqrt((x101 - x128)^2 + (x241 - x268)^2 + (x381 - x408)^2) + 1 / sqrt((x101
    - x129)^2 + (x241 - x269)^2 + (x381 - x409)^2) + 1 / sqrt((x101 - x130)^2
    + (x241 - x270)^2 + (x381 - x410)^2) + 1 / sqrt((x101 - x131)^2 + (x241 -
    x271)^2 + (x381 - x411)^2) + 1 / sqrt((x101 - x132)^2 + (x241 - x272)^2 + (
    x381 - x412)^2) + 1 / sqrt((x101 - x133)^2 + (x241 - x273)^2 + (x381 - x413)
    ^2) + 1 / sqrt((x101 - x134)^2 + (x241 - x274)^2 + (x381 - x414)^2) + 1 /
    sqrt((x101 - x135)^2 + (x241 - x275)^2 + (x381 - x415)^2) + 1 / sqrt((x101
    - x136)^2 + (x241 - x276)^2 + (x381 - x416)^2) + 1 / sqrt((x101 - x137)^2
    + (x241 - x277)^2 + (x381 - x417)^2) + 1 / sqrt((x101 - x138)^2 + (x241 -
    x278)^2 + (x381 - x418)^2) + 1 / sqrt((x101 - x139)^2 + (x241 - x279)^2 + (
    x381 - x419)^2) + 1 / sqrt((x101 - x140)^2 + (x241 - x280)^2 + (x381 - x420)
    ^2) + 1 / sqrt((x102 - x103)^2 + (x242 - x243)^2 + (x382 - x383)^2) + 1 /
    sqrt((x102 - x104)^2 + (x242 - x244)^2 + (x382 - x384)^2) + 1 / sqrt((x102
    - x105)^2 + (x242 - x245)^2 + (x382 - x385)^2) + 1 / sqrt((x102 - x106)^2
    + (x242 - x246)^2 + (x382 - x386)^2) + 1 / sqrt((x102 - x107)^2 + (x242 -
    x247)^2 + (x382 - x387)^2) + 1 / sqrt((x102 - x108)^2 + (x242 - x248)^2 + (
    x382 - x388)^2) + 1 / sqrt((x102 - x109)^2 + (x242 - x249)^2 + (x382 - x389)
    ^2) + 1 / sqrt((x102 - x110)^2 + (x242 - x250)^2 + (x382 - x390)^2) + 1 /
    sqrt((x102 - x111)^2 + (x242 - x251)^2 + (x382 - x391)^2) + 1 / sqrt((x102
    - x112)^2 + (x242 - x252)^2 + (x382 - x392)^2) + 1 / sqrt((x102 - x113)^2
    + (x242 - x253)^2 + (x382 - x393)^2) + 1 / sqrt((x102 - x114)^2 + (x242 -
    x254)^2 + (x382 - x394)^2) + 1 / sqrt((x102 - x115)^2 + (x242 - x255)^2 + (
    x382 - x395)^2) + 1 / sqrt((x102 - x116)^2 + (x242 - x256)^2 + (x382 - x396)
    ^2) + 1 / sqrt((x102 - x117)^2 + (x242 - x257)^2 + (x382 - x397)^2) + 1 /
    sqrt((x102 - x118)^2 + (x242 - x258)^2 + (x382 - x398)^2) + 1 / sqrt((x102
    - x119)^2 + (x242 - x259)^2 + (x382 - x399)^2) + 1 / sqrt((x102 - x120)^2
    + (x242 - x260)^2 + (x382 - x400)^2) + 1 / sqrt((x102 - x121)^2 + (x242 -
    x261)^2 + (x382 - x401)^2) + 1 / sqrt((x102 - x122)^2 + (x242 - x262)^2 + (
    x382 - x402)^2) + 1 / sqrt((x102 - x123)^2 + (x242 - x263)^2 + (x382 - x403)
    ^2) + 1 / sqrt((x102 - x124)^2 + (x242 - x264)^2 + (x382 - x404)^2) + 1 /
    sqrt((x102 - x125)^2 + (x242 - x265)^2 + (x382 - x405)^2) + 1 / sqrt((x102
    - x126)^2 + (x242 - x266)^2 + (x382 - x406)^2) + 1 / sqrt((x102 - x127)^2
    + (x242 - x267)^2 + (x382 - x407)^2) + 1 / sqrt((x102 - x128)^2 + (x242 -
    x268)^2 + (x382 - x408)^2) + 1 / sqrt((x102 - x129)^2 + (x242 - x269)^2 + (
    x382 - x409)^2) + 1 / sqrt((x102 - x130)^2 + (x242 - x270)^2 + (x382 - x410)
    ^2) + 1 / sqrt((x102 - x131)^2 + (x242 - x271)^2 + (x382 - x411)^2) + 1 /
    sqrt((x102 - x132)^2 + (x242 - x272)^2 + (x382 - x412)^2) + 1 / sqrt((x102
    - x133)^2 + (x242 - x273)^2 + (x382 - x413)^2) + 1 / sqrt((x102 - x134)^2
    + (x242 - x274)^2 + (x382 - x414)^2) + 1 / sqrt((x102 - x135)^2 + (x242 -
    x275)^2 + (x382 - x415)^2) + 1 / sqrt((x102 - x136)^2 + (x242 - x276)^2 + (
    x382 - x416)^2) + 1 / sqrt((x102 - x137)^2 + (x242 - x277)^2 + (x382 - x417)
    ^2) + 1 / sqrt((x102 - x138)^2 + (x242 - x278)^2 + (x382 - x418)^2) + 1 /
    sqrt((x102 - x139)^2 + (x242 - x279)^2 + (x382 - x419)^2) + 1 / sqrt((x102
    - x140)^2 + (x242 - x280)^2 + (x382 - x420)^2) + 1 / sqrt((x103 - x104)^2
    + (x243 - x244)^2 + (x383 - x384)^2) + 1 / sqrt((x103 - x105)^2 + (x243 -
    x245)^2 + (x383 - x385)^2) + 1 / sqrt((x103 - x106)^2 + (x243 - x246)^2 + (
    x383 - x386)^2) + 1 / sqrt((x103 - x107)^2 + (x243 - x247)^2 + (x383 - x387)
    ^2) + 1 / sqrt((x103 - x108)^2 + (x243 - x248)^2 + (x383 - x388)^2) + 1 /
    sqrt((x103 - x109)^2 + (x243 - x249)^2 + (x383 - x389)^2) + 1 / sqrt((x103
    - x110)^2 + (x243 - x250)^2 + (x383 - x390)^2) + 1 / sqrt((x103 - x111)^2
    + (x243 - x251)^2 + (x383 - x391)^2) + 1 / sqrt((x103 - x112)^2 + (x243 -
    x252)^2 + (x383 - x392)^2) + 1 / sqrt((x103 - x113)^2 + (x243 - x253)^2 + (
    x383 - x393)^2) + 1 / sqrt((x103 - x114)^2 + (x243 - x254)^2 + (x383 - x394)
    ^2) + 1 / sqrt((x103 - x115)^2 + (x243 - x255)^2 + (x383 - x395)^2) + 1 /
    sqrt((x103 - x116)^2 + (x243 - x256)^2 + (x383 - x396)^2) + 1 / sqrt((x103
    - x117)^2 + (x243 - x257)^2 + (x383 - x397)^2) + 1 / sqrt((x103 - x118)^2
    + (x243 - x258)^2 + (x383 - x398)^2) + 1 / sqrt((x103 - x119)^2 + (x243 -
    x259)^2 + (x383 - x399)^2) + 1 / sqrt((x103 - x120)^2 + (x243 - x260)^2 + (
    x383 - x400)^2) + 1 / sqrt((x103 - x121)^2 + (x243 - x261)^2 + (x383 - x401)
    ^2) + 1 / sqrt((x103 - x122)^2 + (x243 - x262)^2 + (x383 - x402)^2) + 1 /
    sqrt((x103 - x123)^2 + (x243 - x263)^2 + (x383 - x403)^2) + 1 / sqrt((x103
    - x124)^2 + (x243 - x264)^2 + (x383 - x404)^2) + 1 / sqrt((x103 - x125)^2
    + (x243 - x265)^2 + (x383 - x405)^2) + 1 / sqrt((x103 - x126)^2 + (x243 -
    x266)^2 + (x383 - x406)^2) + 1 / sqrt((x103 - x127)^2 + (x243 - x267)^2 + (
    x383 - x407)^2) + 1 / sqrt((x103 - x128)^2 + (x243 - x268)^2 + (x383 - x408)
    ^2) + 1 / sqrt((x103 - x129)^2 + (x243 - x269)^2 + (x383 - x409)^2) + 1 /
    sqrt((x103 - x130)^2 + (x243 - x270)^2 + (x383 - x410)^2) + 1 / sqrt((x103
    - x131)^2 + (x243 - x271)^2 + (x383 - x411)^2) + 1 / sqrt((x103 - x132)^2
    + (x243 - x272)^2 + (x383 - x412)^2) + 1 / sqrt((x103 - x133)^2 + (x243 -
    x273)^2 + (x383 - x413)^2) + 1 / sqrt((x103 - x134)^2 + (x243 - x274)^2 + (
    x383 - x414)^2) + 1 / sqrt((x103 - x135)^2 + (x243 - x275)^2 + (x383 - x415)
    ^2) + 1 / sqrt((x103 - x136)^2 + (x243 - x276)^2 + (x383 - x416)^2) + 1 /
    sqrt((x103 - x137)^2 + (x243 - x277)^2 + (x383 - x417)^2) + 1 / sqrt((x103
    - x138)^2 + (x243 - x278)^2 + (x383 - x418)^2) + 1 / sqrt((x103 - x139)^2
    + (x243 - x279)^2 + (x383 - x419)^2) + 1 / sqrt((x103 - x140)^2 + (x243 -
    x280)^2 + (x383 - x420)^2) + 1 / sqrt((x104 - x105)^2 + (x244 - x245)^2 + (
    x384 - x385)^2) + 1 / sqrt((x104 - x106)^2 + (x244 - x246)^2 + (x384 - x386)
    ^2) + 1 / sqrt((x104 - x107)^2 + (x244 - x247)^2 + (x384 - x387)^2) + 1 /
    sqrt((x104 - x108)^2 + (x244 - x248)^2 + (x384 - x388)^2) + 1 / sqrt((x104
    - x109)^2 + (x244 - x249)^2 + (x384 - x389)^2) + 1 / sqrt((x104 - x110)^2
    + (x244 - x250)^2 + (x384 - x390)^2) + 1 / sqrt((x104 - x111)^2 + (x244 -
    x251)^2 + (x384 - x391)^2) + 1 / sqrt((x104 - x112)^2 + (x244 - x252)^2 + (
    x384 - x392)^2) + 1 / sqrt((x104 - x113)^2 + (x244 - x253)^2 + (x384 - x393)
    ^2) + 1 / sqrt((x104 - x114)^2 + (x244 - x254)^2 + (x384 - x394)^2) + 1 /
    sqrt((x104 - x115)^2 + (x244 - x255)^2 + (x384 - x395)^2) + 1 / sqrt((x104
    - x116)^2 + (x244 - x256)^2 + (x384 - x396)^2) + 1 / sqrt((x104 - x117)^2
    + (x244 - x257)^2 + (x384 - x397)^2) + 1 / sqrt((x104 - x118)^2 + (x244 -
    x258)^2 + (x384 - x398)^2) + 1 / sqrt((x104 - x119)^2 + (x244 - x259)^2 + (
    x384 - x399)^2) + 1 / sqrt((x104 - x120)^2 + (x244 - x260)^2 + (x384 - x400)
    ^2) + 1 / sqrt((x104 - x121)^2 + (x244 - x261)^2 + (x384 - x401)^2) + 1 /
    sqrt((x104 - x122)^2 + (x244 - x262)^2 + (x384 - x402)^2) + 1 / sqrt((x104
    - x123)^2 + (x244 - x263)^2 + (x384 - x403)^2) + 1 / sqrt((x104 - x124)^2
    + (x244 - x264)^2 + (x384 - x404)^2) + 1 / sqrt((x104 - x125)^2 + (x244 -
    x265)^2 + (x384 - x405)^2) + 1 / sqrt((x104 - x126)^2 + (x244 - x266)^2 + (
    x384 - x406)^2) + 1 / sqrt((x104 - x127)^2 + (x244 - x267)^2 + (x384 - x407)
    ^2) + 1 / sqrt((x104 - x128)^2 + (x244 - x268)^2 + (x384 - x408)^2) + 1 /
    sqrt((x104 - x129)^2 + (x244 - x269)^2 + (x384 - x409)^2) + 1 / sqrt((x104
    - x130)^2 + (x244 - x270)^2 + (x384 - x410)^2) + 1 / sqrt((x104 - x131)^2
    + (x244 - x271)^2 + (x384 - x411)^2) + 1 / sqrt((x104 - x132)^2 + (x244 -
    x272)^2 + (x384 - x412)^2) + 1 / sqrt((x104 - x133)^2 + (x244 - x273)^2 + (
    x384 - x413)^2) + 1 / sqrt((x104 - x134)^2 + (x244 - x274)^2 + (x384 - x414)
    ^2) + 1 / sqrt((x104 - x135)^2 + (x244 - x275)^2 + (x384 - x415)^2) + 1 /
    sqrt((x104 - x136)^2 + (x244 - x276)^2 + (x384 - x416)^2) + 1 / sqrt((x104
    - x137)^2 + (x244 - x277)^2 + (x384 - x417)^2) + 1 / sqrt((x104 - x138)^2
    + (x244 - x278)^2 + (x384 - x418)^2) + 1 / sqrt((x104 - x139)^2 + (x244 -
    x279)^2 + (x384 - x419)^2) + 1 / sqrt((x104 - x140)^2 + (x244 - x280)^2 + (
    x384 - x420)^2) + 1 / sqrt((x105 - x106)^2 + (x245 - x246)^2 + (x385 - x386)
    ^2) + 1 / sqrt((x105 - x107)^2 + (x245 - x247)^2 + (x385 - x387)^2) + 1 /
    sqrt((x105 - x108)^2 + (x245 - x248)^2 + (x385 - x388)^2) + 1 / sqrt((x105
    - x109)^2 + (x245 - x249)^2 + (x385 - x389)^2) + 1 / sqrt((x105 - x110)^2
    + (x245 - x250)^2 + (x385 - x390)^2) + 1 / sqrt((x105 - x111)^2 + (x245 -
    x251)^2 + (x385 - x391)^2) + 1 / sqrt((x105 - x112)^2 + (x245 - x252)^2 + (
    x385 - x392)^2) + 1 / sqrt((x105 - x113)^2 + (x245 - x253)^2 + (x385 - x393)
    ^2) + 1 / sqrt((x105 - x114)^2 + (x245 - x254)^2 + (x385 - x394)^2) + 1 /
    sqrt((x105 - x115)^2 + (x245 - x255)^2 + (x385 - x395)^2) + 1 / sqrt((x105
    - x116)^2 + (x245 - x256)^2 + (x385 - x396)^2) + 1 / sqrt((x105 - x117)^2
    + (x245 - x257)^2 + (x385 - x397)^2) + 1 / sqrt((x105 - x118)^2 + (x245 -
    x258)^2 + (x385 - x398)^2) + 1 / sqrt((x105 - x119)^2 + (x245 - x259)^2 + (
    x385 - x399)^2) + 1 / sqrt((x105 - x120)^2 + (x245 - x260)^2 + (x385 - x400)
    ^2) + 1 / sqrt((x105 - x121)^2 + (x245 - x261)^2 + (x385 - x401)^2) + 1 /
    sqrt((x105 - x122)^2 + (x245 - x262)^2 + (x385 - x402)^2) + 1 / sqrt((x105
    - x123)^2 + (x245 - x263)^2 + (x385 - x403)^2) + 1 / sqrt((x105 - x124)^2
    + (x245 - x264)^2 + (x385 - x404)^2) + 1 / sqrt((x105 - x125)^2 + (x245 -
    x265)^2 + (x385 - x405)^2) + 1 / sqrt((x105 - x126)^2 + (x245 - x266)^2 + (
    x385 - x406)^2) + 1 / sqrt((x105 - x127)^2 + (x245 - x267)^2 + (x385 - x407)
    ^2) + 1 / sqrt((x105 - x128)^2 + (x245 - x268)^2 + (x385 - x408)^2) + 1 /
    sqrt((x105 - x129)^2 + (x245 - x269)^2 + (x385 - x409)^2) + 1 / sqrt((x105
    - x130)^2 + (x245 - x270)^2 + (x385 - x410)^2) + 1 / sqrt((x105 - x131)^2
    + (x245 - x271)^2 + (x385 - x411)^2) + 1 / sqrt((x105 - x132)^2 + (x245 -
    x272)^2 + (x385 - x412)^2) + 1 / sqrt((x105 - x133)^2 + (x245 - x273)^2 + (
    x385 - x413)^2) + 1 / sqrt((x105 - x134)^2 + (x245 - x274)^2 + (x385 - x414)
    ^2) + 1 / sqrt((x105 - x135)^2 + (x245 - x275)^2 + (x385 - x415)^2) + 1 /
    sqrt((x105 - x136)^2 + (x245 - x276)^2 + (x385 - x416)^2) + 1 / sqrt((x105
    - x137)^2 + (x245 - x277)^2 + (x385 - x417)^2) + 1 / sqrt((x105 - x138)^2
    + (x245 - x278)^2 + (x385 - x418)^2) + 1 / sqrt((x105 - x139)^2 + (x245 -
    x279)^2 + (x385 - x419)^2) + 1 / sqrt((x105 - x140)^2 + (x245 - x280)^2 + (
    x385 - x420)^2) + 1 / sqrt((x106 - x107)^2 + (x246 - x247)^2 + (x386 - x387)
    ^2) + 1 / sqrt((x106 - x108)^2 + (x246 - x248)^2 + (x386 - x388)^2) + 1 /
    sqrt((x106 - x109)^2 + (x246 - x249)^2 + (x386 - x389)^2) + 1 / sqrt((x106
    - x110)^2 + (x246 - x250)^2 + (x386 - x390)^2) + 1 / sqrt((x106 - x111)^2
    + (x246 - x251)^2 + (x386 - x391)^2) + 1 / sqrt((x106 - x112)^2 + (x246 -
    x252)^2 + (x386 - x392)^2) + 1 / sqrt((x106 - x113)^2 + (x246 - x253)^2 + (
    x386 - x393)^2) + 1 / sqrt((x106 - x114)^2 + (x246 - x254)^2 + (x386 - x394)
    ^2) + 1 / sqrt((x106 - x115)^2 + (x246 - x255)^2 + (x386 - x395)^2) + 1 /
    sqrt((x106 - x116)^2 + (x246 - x256)^2 + (x386 - x396)^2) + 1 / sqrt((x106
    - x117)^2 + (x246 - x257)^2 + (x386 - x397)^2) + 1 / sqrt((x106 - x118)^2
    + (x246 - x258)^2 + (x386 - x398)^2) + 1 / sqrt((x106 - x119)^2 + (x246 -
    x259)^2 + (x386 - x399)^2) + 1 / sqrt((x106 - x120)^2 + (x246 - x260)^2 + (
    x386 - x400)^2) + 1 / sqrt((x106 - x121)^2 + (x246 - x261)^2 + (x386 - x401)
    ^2) + 1 / sqrt((x106 - x122)^2 + (x246 - x262)^2 + (x386 - x402)^2) + 1 /
    sqrt((x106 - x123)^2 + (x246 - x263)^2 + (x386 - x403)^2) + 1 / sqrt((x106
    - x124)^2 + (x246 - x264)^2 + (x386 - x404)^2) + 1 / sqrt((x106 - x125)^2
    + (x246 - x265)^2 + (x386 - x405)^2) + 1 / sqrt((x106 - x126)^2 + (x246 -
    x266)^2 + (x386 - x406)^2) + 1 / sqrt((x106 - x127)^2 + (x246 - x267)^2 + (
    x386 - x407)^2) + 1 / sqrt((x106 - x128)^2 + (x246 - x268)^2 + (x386 - x408)
    ^2) + 1 / sqrt((x106 - x129)^2 + (x246 - x269)^2 + (x386 - x409)^2) + 1 /
    sqrt((x106 - x130)^2 + (x246 - x270)^2 + (x386 - x410)^2) + 1 / sqrt((x106
    - x131)^2 + (x246 - x271)^2 + (x386 - x411)^2) + 1 / sqrt((x106 - x132)^2
    + (x246 - x272)^2 + (x386 - x412)^2) + 1 / sqrt((x106 - x133)^2 + (x246 -
    x273)^2 + (x386 - x413)^2) + 1 / sqrt((x106 - x134)^2 + (x246 - x274)^2 + (
    x386 - x414)^2) + 1 / sqrt((x106 - x135)^2 + (x246 - x275)^2 + (x386 - x415)
    ^2) + 1 / sqrt((x106 - x136)^2 + (x246 - x276)^2 + (x386 - x416)^2) + 1 /
    sqrt((x106 - x137)^2 + (x246 - x277)^2 + (x386 - x417)^2) + 1 / sqrt((x106
    - x138)^2 + (x246 - x278)^2 + (x386 - x418)^2) + 1 / sqrt((x106 - x139)^2
    + (x246 - x279)^2 + (x386 - x419)^2) + 1 / sqrt((x106 - x140)^2 + (x246 -
    x280)^2 + (x386 - x420)^2) + 1 / sqrt((x107 - x108)^2 + (x247 - x248)^2 + (
    x387 - x388)^2) + 1 / sqrt((x107 - x109)^2 + (x247 - x249)^2 + (x387 - x389)
    ^2) + 1 / sqrt((x107 - x110)^2 + (x247 - x250)^2 + (x387 - x390)^2) + 1 /
    sqrt((x107 - x111)^2 + (x247 - x251)^2 + (x387 - x391)^2) + 1 / sqrt((x107
    - x112)^2 + (x247 - x252)^2 + (x387 - x392)^2) + 1 / sqrt((x107 - x113)^2
    + (x247 - x253)^2 + (x387 - x393)^2) + 1 / sqrt((x107 - x114)^2 + (x247 -
    x254)^2 + (x387 - x394)^2) + 1 / sqrt((x107 - x115)^2 + (x247 - x255)^2 + (
    x387 - x395)^2) + 1 / sqrt((x107 - x116)^2 + (x247 - x256)^2 + (x387 - x396)
    ^2) + 1 / sqrt((x107 - x117)^2 + (x247 - x257)^2 + (x387 - x397)^2) + 1 /
    sqrt((x107 - x118)^2 + (x247 - x258)^2 + (x387 - x398)^2) + 1 / sqrt((x107
    - x119)^2 + (x247 - x259)^2 + (x387 - x399)^2) + 1 / sqrt((x107 - x120)^2
    + (x247 - x260)^2 + (x387 - x400)^2) + 1 / sqrt((x107 - x121)^2 + (x247 -
    x261)^2 + (x387 - x401)^2) + 1 / sqrt((x107 - x122)^2 + (x247 - x262)^2 + (
    x387 - x402)^2) + 1 / sqrt((x107 - x123)^2 + (x247 - x263)^2 + (x387 - x403)
    ^2) + 1 / sqrt((x107 - x124)^2 + (x247 - x264)^2 + (x387 - x404)^2) + 1 /
    sqrt((x107 - x125)^2 + (x247 - x265)^2 + (x387 - x405)^2) + 1 / sqrt((x107
    - x126)^2 + (x247 - x266)^2 + (x387 - x406)^2) + 1 / sqrt((x107 - x127)^2
    + (x247 - x267)^2 + (x387 - x407)^2) + 1 / sqrt((x107 - x128)^2 + (x247 -
    x268)^2 + (x387 - x408)^2) + 1 / sqrt((x107 - x129)^2 + (x247 - x269)^2 + (
    x387 - x409)^2) + 1 / sqrt((x107 - x130)^2 + (x247 - x270)^2 + (x387 - x410)
    ^2) + 1 / sqrt((x107 - x131)^2 + (x247 - x271)^2 + (x387 - x411)^2) + 1 /
    sqrt((x107 - x132)^2 + (x247 - x272)^2 + (x387 - x412)^2) + 1 / sqrt((x107
    - x133)^2 + (x247 - x273)^2 + (x387 - x413)^2) + 1 / sqrt((x107 - x134)^2
    + (x247 - x274)^2 + (x387 - x414)^2) + 1 / sqrt((x107 - x135)^2 + (x247 -
    x275)^2 + (x387 - x415)^2) + 1 / sqrt((x107 - x136)^2 + (x247 - x276)^2 + (
    x387 - x416)^2) + 1 / sqrt((x107 - x137)^2 + (x247 - x277)^2 + (x387 - x417)
    ^2) + 1 / sqrt((x107 - x138)^2 + (x247 - x278)^2 + (x387 - x418)^2) + 1 /
    sqrt((x107 - x139)^2 + (x247 - x279)^2 + (x387 - x419)^2) + 1 / sqrt((x107
    - x140)^2 + (x247 - x280)^2 + (x387 - x420)^2) + 1 / sqrt((x108 - x109)^2
    + (x248 - x249)^2 + (x388 - x389)^2) + 1 / sqrt((x108 - x110)^2 + (x248 -
    x250)^2 + (x388 - x390)^2) + 1 / sqrt((x108 - x111)^2 + (x248 - x251)^2 + (
    x388 - x391)^2) + 1 / sqrt((x108 - x112)^2 + (x248 - x252)^2 + (x388 - x392)
    ^2) + 1 / sqrt((x108 - x113)^2 + (x248 - x253)^2 + (x388 - x393)^2) + 1 /
    sqrt((x108 - x114)^2 + (x248 - x254)^2 + (x388 - x394)^2) + 1 / sqrt((x108
    - x115)^2 + (x248 - x255)^2 + (x388 - x395)^2) + 1 / sqrt((x108 - x116)^2
    + (x248 - x256)^2 + (x388 - x396)^2) + 1 / sqrt((x108 - x117)^2 + (x248 -
    x257)^2 + (x388 - x397)^2) + 1 / sqrt((x108 - x118)^2 + (x248 - x258)^2 + (
    x388 - x398)^2) + 1 / sqrt((x108 - x119)^2 + (x248 - x259)^2 + (x388 - x399)
    ^2) + 1 / sqrt((x108 - x120)^2 + (x248 - x260)^2 + (x388 - x400)^2) + 1 /
    sqrt((x108 - x121)^2 + (x248 - x261)^2 + (x388 - x401)^2) + 1 / sqrt((x108
    - x122)^2 + (x248 - x262)^2 + (x388 - x402)^2) + 1 / sqrt((x108 - x123)^2
    + (x248 - x263)^2 + (x388 - x403)^2) + 1 / sqrt((x108 - x124)^2 + (x248 -
    x264)^2 + (x388 - x404)^2) + 1 / sqrt((x108 - x125)^2 + (x248 - x265)^2 + (
    x388 - x405)^2) + 1 / sqrt((x108 - x126)^2 + (x248 - x266)^2 + (x388 - x406)
    ^2) + 1 / sqrt((x108 - x127)^2 + (x248 - x267)^2 + (x388 - x407)^2) + 1 /
    sqrt((x108 - x128)^2 + (x248 - x268)^2 + (x388 - x408)^2) + 1 / sqrt((x108
    - x129)^2 + (x248 - x269)^2 + (x388 - x409)^2) + 1 / sqrt((x108 - x130)^2
    + (x248 - x270)^2 + (x388 - x410)^2) + 1 / sqrt((x108 - x131)^2 + (x248 -
    x271)^2 + (x388 - x411)^2) + 1 / sqrt((x108 - x132)^2 + (x248 - x272)^2 + (
    x388 - x412)^2) + 1 / sqrt((x108 - x133)^2 + (x248 - x273)^2 + (x388 - x413)
    ^2) + 1 / sqrt((x108 - x134)^2 + (x248 - x274)^2 + (x388 - x414)^2) + 1 /
    sqrt((x108 - x135)^2 + (x248 - x275)^2 + (x388 - x415)^2) + 1 / sqrt((x108
    - x136)^2 + (x248 - x276)^2 + (x388 - x416)^2) + 1 / sqrt((x108 - x137)^2
    + (x248 - x277)^2 + (x388 - x417)^2) + 1 / sqrt((x108 - x138)^2 + (x248 -
    x278)^2 + (x388 - x418)^2) + 1 / sqrt((x108 - x139)^2 + (x248 - x279)^2 + (
    x388 - x419)^2) + 1 / sqrt((x108 - x140)^2 + (x248 - x280)^2 + (x388 - x420)
    ^2) + 1 / sqrt((x109 - x110)^2 + (x249 - x250)^2 + (x389 - x390)^2) + 1 /
    sqrt((x109 - x111)^2 + (x249 - x251)^2 + (x389 - x391)^2) + 1 / sqrt((x109
    - x112)^2 + (x249 - x252)^2 + (x389 - x392)^2) + 1 / sqrt((x109 - x113)^2
    + (x249 - x253)^2 + (x389 - x393)^2) + 1 / sqrt((x109 - x114)^2 + (x249 -
    x254)^2 + (x389 - x394)^2) + 1 / sqrt((x109 - x115)^2 + (x249 - x255)^2 + (
    x389 - x395)^2) + 1 / sqrt((x109 - x116)^2 + (x249 - x256)^2 + (x389 - x396)
    ^2) + 1 / sqrt((x109 - x117)^2 + (x249 - x257)^2 + (x389 - x397)^2) + 1 /
    sqrt((x109 - x118)^2 + (x249 - x258)^2 + (x389 - x398)^2) + 1 / sqrt((x109
    - x119)^2 + (x249 - x259)^2 + (x389 - x399)^2) + 1 / sqrt((x109 - x120)^2
    + (x249 - x260)^2 + (x389 - x400)^2) + 1 / sqrt((x109 - x121)^2 + (x249 -
    x261)^2 + (x389 - x401)^2) + 1 / sqrt((x109 - x122)^2 + (x249 - x262)^2 + (
    x389 - x402)^2) + 1 / sqrt((x109 - x123)^2 + (x249 - x263)^2 + (x389 - x403)
    ^2) + 1 / sqrt((x109 - x124)^2 + (x249 - x264)^2 + (x389 - x404)^2) + 1 /
    sqrt((x109 - x125)^2 + (x249 - x265)^2 + (x389 - x405)^2) + 1 / sqrt((x109
    - x126)^2 + (x249 - x266)^2 + (x389 - x406)^2) + 1 / sqrt((x109 - x127)^2
    + (x249 - x267)^2 + (x389 - x407)^2) + 1 / sqrt((x109 - x128)^2 + (x249 -
    x268)^2 + (x389 - x408)^2) + 1 / sqrt((x109 - x129)^2 + (x249 - x269)^2 + (
    x389 - x409)^2) + 1 / sqrt((x109 - x130)^2 + (x249 - x270)^2 + (x389 - x410)
    ^2) + 1 / sqrt((x109 - x131)^2 + (x249 - x271)^2 + (x389 - x411)^2) + 1 /
    sqrt((x109 - x132)^2 + (x249 - x272)^2 + (x389 - x412)^2) + 1 / sqrt((x109
    - x133)^2 + (x249 - x273)^2 + (x389 - x413)^2) + 1 / sqrt((x109 - x134)^2
    + (x249 - x274)^2 + (x389 - x414)^2) + 1 / sqrt((x109 - x135)^2 + (x249 -
    x275)^2 + (x389 - x415)^2) + 1 / sqrt((x109 - x136)^2 + (x249 - x276)^2 + (
    x389 - x416)^2) + 1 / sqrt((x109 - x137)^2 + (x249 - x277)^2 + (x389 - x417)
    ^2) + 1 / sqrt((x109 - x138)^2 + (x249 - x278)^2 + (x389 - x418)^2) + 1 /
    sqrt((x109 - x139)^2 + (x249 - x279)^2 + (x389 - x419)^2) + 1 / sqrt((x109
    - x140)^2 + (x249 - x280)^2 + (x389 - x420)^2) + 1 / sqrt((x110 - x111)^2
    + (x250 - x251)^2 + (x390 - x391)^2) + 1 / sqrt((x110 - x112)^2 + (x250 -
    x252)^2 + (x390 - x392)^2) + 1 / sqrt((x110 - x113)^2 + (x250 - x253)^2 + (
    x390 - x393)^2) + 1 / sqrt((x110 - x114)^2 + (x250 - x254)^2 + (x390 - x394)
    ^2) + 1 / sqrt((x110 - x115)^2 + (x250 - x255)^2 + (x390 - x395)^2) + 1 /
    sqrt((x110 - x116)^2 + (x250 - x256)^2 + (x390 - x396)^2) + 1 / sqrt((x110
    - x117)^2 + (x250 - x257)^2 + (x390 - x397)^2) + 1 / sqrt((x110 - x118)^2
    + (x250 - x258)^2 + (x390 - x398)^2) + 1 / sqrt((x110 - x119)^2 + (x250 -
    x259)^2 + (x390 - x399)^2) + 1 / sqrt((x110 - x120)^2 + (x250 - x260)^2 + (
    x390 - x400)^2) + 1 / sqrt((x110 - x121)^2 + (x250 - x261)^2 + (x390 - x401)
    ^2) + 1 / sqrt((x110 - x122)^2 + (x250 - x262)^2 + (x390 - x402)^2) + 1 /
    sqrt((x110 - x123)^2 + (x250 - x263)^2 + (x390 - x403)^2) + 1 / sqrt((x110
    - x124)^2 + (x250 - x264)^2 + (x390 - x404)^2) + 1 / sqrt((x110 - x125)^2
    + (x250 - x265)^2 + (x390 - x405)^2) + 1 / sqrt((x110 - x126)^2 + (x250 -
    x266)^2 + (x390 - x406)^2) + 1 / sqrt((x110 - x127)^2 + (x250 - x267)^2 + (
    x390 - x407)^2) + 1 / sqrt((x110 - x128)^2 + (x250 - x268)^2 + (x390 - x408)
    ^2) + 1 / sqrt((x110 - x129)^2 + (x250 - x269)^2 + (x390 - x409)^2) + 1 /
    sqrt((x110 - x130)^2 + (x250 - x270)^2 + (x390 - x410)^2) + 1 / sqrt((x110
    - x131)^2 + (x250 - x271)^2 + (x390 - x411)^2) + 1 / sqrt((x110 - x132)^2
    + (x250 - x272)^2 + (x390 - x412)^2) + 1 / sqrt((x110 - x133)^2 + (x250 -
    x273)^2 + (x390 - x413)^2) + 1 / sqrt((x110 - x134)^2 + (x250 - x274)^2 + (
    x390 - x414)^2) + 1 / sqrt((x110 - x135)^2 + (x250 - x275)^2 + (x390 - x415)
    ^2) + 1 / sqrt((x110 - x136)^2 + (x250 - x276)^2 + (x390 - x416)^2) + 1 /
    sqrt((x110 - x137)^2 + (x250 - x277)^2 + (x390 - x417)^2) + 1 / sqrt((x110
    - x138)^2 + (x250 - x278)^2 + (x390 - x418)^2) + 1 / sqrt((x110 - x139)^2
    + (x250 - x279)^2 + (x390 - x419)^2) + 1 / sqrt((x110 - x140)^2 + (x250 -
    x280)^2 + (x390 - x420)^2) + 1 / sqrt((x111 - x112)^2 + (x251 - x252)^2 + (
    x391 - x392)^2) + 1 / sqrt((x111 - x113)^2 + (x251 - x253)^2 + (x391 - x393)
    ^2) + 1 / sqrt((x111 - x114)^2 + (x251 - x254)^2 + (x391 - x394)^2) + 1 /
    sqrt((x111 - x115)^2 + (x251 - x255)^2 + (x391 - x395)^2) + 1 / sqrt((x111
    - x116)^2 + (x251 - x256)^2 + (x391 - x396)^2) + 1 / sqrt((x111 - x117)^2
    + (x251 - x257)^2 + (x391 - x397)^2) + 1 / sqrt((x111 - x118)^2 + (x251 -
    x258)^2 + (x391 - x398)^2) + 1 / sqrt((x111 - x119)^2 + (x251 - x259)^2 + (
    x391 - x399)^2) + 1 / sqrt((x111 - x120)^2 + (x251 - x260)^2 + (x391 - x400)
    ^2) + 1 / sqrt((x111 - x121)^2 + (x251 - x261)^2 + (x391 - x401)^2) + 1 /
    sqrt((x111 - x122)^2 + (x251 - x262)^2 + (x391 - x402)^2) + 1 / sqrt((x111
    - x123)^2 + (x251 - x263)^2 + (x391 - x403)^2) + 1 / sqrt((x111 - x124)^2
    + (x251 - x264)^2 + (x391 - x404)^2) + 1 / sqrt((x111 - x125)^2 + (x251 -
    x265)^2 + (x391 - x405)^2) + 1 / sqrt((x111 - x126)^2 + (x251 - x266)^2 + (
    x391 - x406)^2) + 1 / sqrt((x111 - x127)^2 + (x251 - x267)^2 + (x391 - x407)
    ^2) + 1 / sqrt((x111 - x128)^2 + (x251 - x268)^2 + (x391 - x408)^2) + 1 /
    sqrt((x111 - x129)^2 + (x251 - x269)^2 + (x391 - x409)^2) + 1 / sqrt((x111
    - x130)^2 + (x251 - x270)^2 + (x391 - x410)^2) + 1 / sqrt((x111 - x131)^2
    + (x251 - x271)^2 + (x391 - x411)^2) + 1 / sqrt((x111 - x132)^2 + (x251 -
    x272)^2 + (x391 - x412)^2) + 1 / sqrt((x111 - x133)^2 + (x251 - x273)^2 + (
    x391 - x413)^2) + 1 / sqrt((x111 - x134)^2 + (x251 - x274)^2 + (x391 - x414)
    ^2) + 1 / sqrt((x111 - x135)^2 + (x251 - x275)^2 + (x391 - x415)^2) + 1 /
    sqrt((x111 - x136)^2 + (x251 - x276)^2 + (x391 - x416)^2) + 1 / sqrt((x111
    - x137)^2 + (x251 - x277)^2 + (x391 - x417)^2) + 1 / sqrt((x111 - x138)^2
    + (x251 - x278)^2 + (x391 - x418)^2) + 1 / sqrt((x111 - x139)^2 + (x251 -
    x279)^2 + (x391 - x419)^2) + 1 / sqrt((x111 - x140)^2 + (x251 - x280)^2 + (
    x391 - x420)^2) + 1 / sqrt((x112 - x113)^2 + (x252 - x253)^2 + (x392 - x393)
    ^2) + 1 / sqrt((x112 - x114)^2 + (x252 - x254)^2 + (x392 - x394)^2) + 1 /
    sqrt((x112 - x115)^2 + (x252 - x255)^2 + (x392 - x395)^2) + 1 / sqrt((x112
    - x116)^2 + (x252 - x256)^2 + (x392 - x396)^2) + 1 / sqrt((x112 - x117)^2
    + (x252 - x257)^2 + (x392 - x397)^2) + 1 / sqrt((x112 - x118)^2 + (x252 -
    x258)^2 + (x392 - x398)^2) + 1 / sqrt((x112 - x119)^2 + (x252 - x259)^2 + (
    x392 - x399)^2) + 1 / sqrt((x112 - x120)^2 + (x252 - x260)^2 + (x392 - x400)
    ^2) + 1 / sqrt((x112 - x121)^2 + (x252 - x261)^2 + (x392 - x401)^2) + 1 /
    sqrt((x112 - x122)^2 + (x252 - x262)^2 + (x392 - x402)^2) + 1 / sqrt((x112
    - x123)^2 + (x252 - x263)^2 + (x392 - x403)^2) + 1 / sqrt((x112 - x124)^2
    + (x252 - x264)^2 + (x392 - x404)^2) + 1 / sqrt((x112 - x125)^2 + (x252 -
    x265)^2 + (x392 - x405)^2) + 1 / sqrt((x112 - x126)^2 + (x252 - x266)^2 + (
    x392 - x406)^2) + 1 / sqrt((x112 - x127)^2 + (x252 - x267)^2 + (x392 - x407)
    ^2) + 1 / sqrt((x112 - x128)^2 + (x252 - x268)^2 + (x392 - x408)^2) + 1 /
    sqrt((x112 - x129)^2 + (x252 - x269)^2 + (x392 - x409)^2) + 1 / sqrt((x112
    - x130)^2 + (x252 - x270)^2 + (x392 - x410)^2) + 1 / sqrt((x112 - x131)^2
    + (x252 - x271)^2 + (x392 - x411)^2) + 1 / sqrt((x112 - x132)^2 + (x252 -
    x272)^2 + (x392 - x412)^2) + 1 / sqrt((x112 - x133)^2 + (x252 - x273)^2 + (
    x392 - x413)^2) + 1 / sqrt((x112 - x134)^2 + (x252 - x274)^2 + (x392 - x414)
    ^2) + 1 / sqrt((x112 - x135)^2 + (x252 - x275)^2 + (x392 - x415)^2) + 1 /
    sqrt((x112 - x136)^2 + (x252 - x276)^2 + (x392 - x416)^2) + 1 / sqrt((x112
    - x137)^2 + (x252 - x277)^2 + (x392 - x417)^2) + 1 / sqrt((x112 - x138)^2
    + (x252 - x278)^2 + (x392 - x418)^2) + 1 / sqrt((x112 - x139)^2 + (x252 -
    x279)^2 + (x392 - x419)^2) + 1 / sqrt((x112 - x140)^2 + (x252 - x280)^2 + (
    x392 - x420)^2) + 1 / sqrt((x113 - x114)^2 + (x253 - x254)^2 + (x393 - x394)
    ^2) + 1 / sqrt((x113 - x115)^2 + (x253 - x255)^2 + (x393 - x395)^2) + 1 /
    sqrt((x113 - x116)^2 + (x253 - x256)^2 + (x393 - x396)^2) + 1 / sqrt((x113
    - x117)^2 + (x253 - x257)^2 + (x393 - x397)^2) + 1 / sqrt((x113 - x118)^2
    + (x253 - x258)^2 + (x393 - x398)^2) + 1 / sqrt((x113 - x119)^2 + (x253 -
    x259)^2 + (x393 - x399)^2) + 1 / sqrt((x113 - x120)^2 + (x253 - x260)^2 + (
    x393 - x400)^2) + 1 / sqrt((x113 - x121)^2 + (x253 - x261)^2 + (x393 - x401)
    ^2) + 1 / sqrt((x113 - x122)^2 + (x253 - x262)^2 + (x393 - x402)^2) + 1 /
    sqrt((x113 - x123)^2 + (x253 - x263)^2 + (x393 - x403)^2) + 1 / sqrt((x113
    - x124)^2 + (x253 - x264)^2 + (x393 - x404)^2) + 1 / sqrt((x113 - x125)^2
    + (x253 - x265)^2 + (x393 - x405)^2) + 1 / sqrt((x113 - x126)^2 + (x253 -
    x266)^2 + (x393 - x406)^2) + 1 / sqrt((x113 - x127)^2 + (x253 - x267)^2 + (
    x393 - x407)^2) + 1 / sqrt((x113 - x128)^2 + (x253 - x268)^2 + (x393 - x408)
    ^2) + 1 / sqrt((x113 - x129)^2 + (x253 - x269)^2 + (x393 - x409)^2) + 1 /
    sqrt((x113 - x130)^2 + (x253 - x270)^2 + (x393 - x410)^2) + 1 / sqrt((x113
    - x131)^2 + (x253 - x271)^2 + (x393 - x411)^2) + 1 / sqrt((x113 - x132)^2
    + (x253 - x272)^2 + (x393 - x412)^2) + 1 / sqrt((x113 - x133)^2 + (x253 -
    x273)^2 + (x393 - x413)^2) + 1 / sqrt((x113 - x134)^2 + (x253 - x274)^2 + (
    x393 - x414)^2) + 1 / sqrt((x113 - x135)^2 + (x253 - x275)^2 + (x393 - x415)
    ^2) + 1 / sqrt((x113 - x136)^2 + (x253 - x276)^2 + (x393 - x416)^2) + 1 /
    sqrt((x113 - x137)^2 + (x253 - x277)^2 + (x393 - x417)^2) + 1 / sqrt((x113
    - x138)^2 + (x253 - x278)^2 + (x393 - x418)^2) + 1 / sqrt((x113 - x139)^2
    + (x253 - x279)^2 + (x393 - x419)^2) + 1 / sqrt((x113 - x140)^2 + (x253 -
    x280)^2 + (x393 - x420)^2) + 1 / sqrt((x114 - x115)^2 + (x254 - x255)^2 + (
    x394 - x395)^2) + 1 / sqrt((x114 - x116)^2 + (x254 - x256)^2 + (x394 - x396)
    ^2) + 1 / sqrt((x114 - x117)^2 + (x254 - x257)^2 + (x394 - x397)^2) + 1 /
    sqrt((x114 - x118)^2 + (x254 - x258)^2 + (x394 - x398)^2) + 1 / sqrt((x114
    - x119)^2 + (x254 - x259)^2 + (x394 - x399)^2) + 1 / sqrt((x114 - x120)^2
    + (x254 - x260)^2 + (x394 - x400)^2) + 1 / sqrt((x114 - x121)^2 + (x254 -
    x261)^2 + (x394 - x401)^2) + 1 / sqrt((x114 - x122)^2 + (x254 - x262)^2 + (
    x394 - x402)^2) + 1 / sqrt((x114 - x123)^2 + (x254 - x263)^2 + (x394 - x403)
    ^2) + 1 / sqrt((x114 - x124)^2 + (x254 - x264)^2 + (x394 - x404)^2) + 1 /
    sqrt((x114 - x125)^2 + (x254 - x265)^2 + (x394 - x405)^2) + 1 / sqrt((x114
    - x126)^2 + (x254 - x266)^2 + (x394 - x406)^2) + 1 / sqrt((x114 - x127)^2
    + (x254 - x267)^2 + (x394 - x407)^2) + 1 / sqrt((x114 - x128)^2 + (x254 -
    x268)^2 + (x394 - x408)^2) + 1 / sqrt((x114 - x129)^2 + (x254 - x269)^2 + (
    x394 - x409)^2) + 1 / sqrt((x114 - x130)^2 + (x254 - x270)^2 + (x394 - x410)
    ^2) + 1 / sqrt((x114 - x131)^2 + (x254 - x271)^2 + (x394 - x411)^2) + 1 /
    sqrt((x114 - x132)^2 + (x254 - x272)^2 + (x394 - x412)^2) + 1 / sqrt((x114
    - x133)^2 + (x254 - x273)^2 + (x394 - x413)^2) + 1 / sqrt((x114 - x134)^2
    + (x254 - x274)^2 + (x394 - x414)^2) + 1 / sqrt((x114 - x135)^2 + (x254 -
    x275)^2 + (x394 - x415)^2) + 1 / sqrt((x114 - x136)^2 + (x254 - x276)^2 + (
    x394 - x416)^2) + 1 / sqrt((x114 - x137)^2 + (x254 - x277)^2 + (x394 - x417)
    ^2) + 1 / sqrt((x114 - x138)^2 + (x254 - x278)^2 + (x394 - x418)^2) + 1 /
    sqrt((x114 - x139)^2 + (x254 - x279)^2 + (x394 - x419)^2) + 1 / sqrt((x114
    - x140)^2 + (x254 - x280)^2 + (x394 - x420)^2) + 1 / sqrt((x115 - x116)^2
    + (x255 - x256)^2 + (x395 - x396)^2) + 1 / sqrt((x115 - x117)^2 + (x255 -
    x257)^2 + (x395 - x397)^2) + 1 / sqrt((x115 - x118)^2 + (x255 - x258)^2 + (
    x395 - x398)^2) + 1 / sqrt((x115 - x119)^2 + (x255 - x259)^2 + (x395 - x399)
    ^2) + 1 / sqrt((x115 - x120)^2 + (x255 - x260)^2 + (x395 - x400)^2) + 1 /
    sqrt((x115 - x121)^2 + (x255 - x261)^2 + (x395 - x401)^2) + 1 / sqrt((x115
    - x122)^2 + (x255 - x262)^2 + (x395 - x402)^2) + 1 / sqrt((x115 - x123)^2
    + (x255 - x263)^2 + (x395 - x403)^2) + 1 / sqrt((x115 - x124)^2 + (x255 -
    x264)^2 + (x395 - x404)^2) + 1 / sqrt((x115 - x125)^2 + (x255 - x265)^2 + (
    x395 - x405)^2) + 1 / sqrt((x115 - x126)^2 + (x255 - x266)^2 + (x395 - x406)
    ^2) + 1 / sqrt((x115 - x127)^2 + (x255 - x267)^2 + (x395 - x407)^2) + 1 /
    sqrt((x115 - x128)^2 + (x255 - x268)^2 + (x395 - x408)^2) + 1 / sqrt((x115
    - x129)^2 + (x255 - x269)^2 + (x395 - x409)^2) + 1 / sqrt((x115 - x130)^2
    + (x255 - x270)^2 + (x395 - x410)^2) + 1 / sqrt((x115 - x131)^2 + (x255 -
    x271)^2 + (x395 - x411)^2) + 1 / sqrt((x115 - x132)^2 + (x255 - x272)^2 + (
    x395 - x412)^2) + 1 / sqrt((x115 - x133)^2 + (x255 - x273)^2 + (x395 - x413)
    ^2) + 1 / sqrt((x115 - x134)^2 + (x255 - x274)^2 + (x395 - x414)^2) + 1 /
    sqrt((x115 - x135)^2 + (x255 - x275)^2 + (x395 - x415)^2) + 1 / sqrt((x115
    - x136)^2 + (x255 - x276)^2 + (x395 - x416)^2) + 1 / sqrt((x115 - x137)^2
    + (x255 - x277)^2 + (x395 - x417)^2) + 1 / sqrt((x115 - x138)^2 + (x255 -
    x278)^2 + (x395 - x418)^2) + 1 / sqrt((x115 - x139)^2 + (x255 - x279)^2 + (
    x395 - x419)^2) + 1 / sqrt((x115 - x140)^2 + (x255 - x280)^2 + (x395 - x420)
    ^2) + 1 / sqrt((x116 - x117)^2 + (x256 - x257)^2 + (x396 - x397)^2) + 1 /
    sqrt((x116 - x118)^2 + (x256 - x258)^2 + (x396 - x398)^2) + 1 / sqrt((x116
    - x119)^2 + (x256 - x259)^2 + (x396 - x399)^2) + 1 / sqrt((x116 - x120)^2
    + (x256 - x260)^2 + (x396 - x400)^2) + 1 / sqrt((x116 - x121)^2 + (x256 -
    x261)^2 + (x396 - x401)^2) + 1 / sqrt((x116 - x122)^2 + (x256 - x262)^2 + (
    x396 - x402)^2) + 1 / sqrt((x116 - x123)^2 + (x256 - x263)^2 + (x396 - x403)
    ^2) + 1 / sqrt((x116 - x124)^2 + (x256 - x264)^2 + (x396 - x404)^2) + 1 /
    sqrt((x116 - x125)^2 + (x256 - x265)^2 + (x396 - x405)^2) + 1 / sqrt((x116
    - x126)^2 + (x256 - x266)^2 + (x396 - x406)^2) + 1 / sqrt((x116 - x127)^2
    + (x256 - x267)^2 + (x396 - x407)^2) + 1 / sqrt((x116 - x128)^2 + (x256 -
    x268)^2 + (x396 - x408)^2) + 1 / sqrt((x116 - x129)^2 + (x256 - x269)^2 + (
    x396 - x409)^2) + 1 / sqrt((x116 - x130)^2 + (x256 - x270)^2 + (x396 - x410)
    ^2) + 1 / sqrt((x116 - x131)^2 + (x256 - x271)^2 + (x396 - x411)^2) + 1 /
    sqrt((x116 - x132)^2 + (x256 - x272)^2 + (x396 - x412)^2) + 1 / sqrt((x116
    - x133)^2 + (x256 - x273)^2 + (x396 - x413)^2) + 1 / sqrt((x116 - x134)^2
    + (x256 - x274)^2 + (x396 - x414)^2) + 1 / sqrt((x116 - x135)^2 + (x256 -
    x275)^2 + (x396 - x415)^2) + 1 / sqrt((x116 - x136)^2 + (x256 - x276)^2 + (
    x396 - x416)^2) + 1 / sqrt((x116 - x137)^2 + (x256 - x277)^2 + (x396 - x417)
    ^2) + 1 / sqrt((x116 - x138)^2 + (x256 - x278)^2 + (x396 - x418)^2) + 1 /
    sqrt((x116 - x139)^2 + (x256 - x279)^2 + (x396 - x419)^2) + 1 / sqrt((x116
    - x140)^2 + (x256 - x280)^2 + (x396 - x420)^2) + 1 / sqrt((x117 - x118)^2
    + (x257 - x258)^2 + (x397 - x398)^2) + 1 / sqrt((x117 - x119)^2 + (x257 -
    x259)^2 + (x397 - x399)^2) + 1 / sqrt((x117 - x120)^2 + (x257 - x260)^2 + (
    x397 - x400)^2) + 1 / sqrt((x117 - x121)^2 + (x257 - x261)^2 + (x397 - x401)
    ^2) + 1 / sqrt((x117 - x122)^2 + (x257 - x262)^2 + (x397 - x402)^2) + 1 /
    sqrt((x117 - x123)^2 + (x257 - x263)^2 + (x397 - x403)^2) + 1 / sqrt((x117
    - x124)^2 + (x257 - x264)^2 + (x397 - x404)^2) + 1 / sqrt((x117 - x125)^2
    + (x257 - x265)^2 + (x397 - x405)^2) + 1 / sqrt((x117 - x126)^2 + (x257 -
    x266)^2 + (x397 - x406)^2) + 1 / sqrt((x117 - x127)^2 + (x257 - x267)^2 + (
    x397 - x407)^2) + 1 / sqrt((x117 - x128)^2 + (x257 - x268)^2 + (x397 - x408)
    ^2) + 1 / sqrt((x117 - x129)^2 + (x257 - x269)^2 + (x397 - x409)^2) + 1 /
    sqrt((x117 - x130)^2 + (x257 - x270)^2 + (x397 - x410)^2) + 1 / sqrt((x117
    - x131)^2 + (x257 - x271)^2 + (x397 - x411)^2) + 1 / sqrt((x117 - x132)^2
    + (x257 - x272)^2 + (x397 - x412)^2) + 1 / sqrt((x117 - x133)^2 + (x257 -
    x273)^2 + (x397 - x413)^2) + 1 / sqrt((x117 - x134)^2 + (x257 - x274)^2 + (
    x397 - x414)^2) + 1 / sqrt((x117 - x135)^2 + (x257 - x275)^2 + (x397 - x415)
    ^2) + 1 / sqrt((x117 - x136)^2 + (x257 - x276)^2 + (x397 - x416)^2) + 1 /
    sqrt((x117 - x137)^2 + (x257 - x277)^2 + (x397 - x417)^2) + 1 / sqrt((x117
    - x138)^2 + (x257 - x278)^2 + (x397 - x418)^2) + 1 / sqrt((x117 - x139)^2
    + (x257 - x279)^2 + (x397 - x419)^2) + 1 / sqrt((x117 - x140)^2 + (x257 -
    x280)^2 + (x397 - x420)^2) + 1 / sqrt((x118 - x119)^2 + (x258 - x259)^2 + (
    x398 - x399)^2) + 1 / sqrt((x118 - x120)^2 + (x258 - x260)^2 + (x398 - x400)
    ^2) + 1 / sqrt((x118 - x121)^2 + (x258 - x261)^2 + (x398 - x401)^2) + 1 /
    sqrt((x118 - x122)^2 + (x258 - x262)^2 + (x398 - x402)^2) + 1 / sqrt((x118
    - x123)^2 + (x258 - x263)^2 + (x398 - x403)^2) + 1 / sqrt((x118 - x124)^2
    + (x258 - x264)^2 + (x398 - x404)^2) + 1 / sqrt((x118 - x125)^2 + (x258 -
    x265)^2 + (x398 - x405)^2) + 1 / sqrt((x118 - x126)^2 + (x258 - x266)^2 + (
    x398 - x406)^2) + 1 / sqrt((x118 - x127)^2 + (x258 - x267)^2 + (x398 - x407)
    ^2) + 1 / sqrt((x118 - x128)^2 + (x258 - x268)^2 + (x398 - x408)^2) + 1 /
    sqrt((x118 - x129)^2 + (x258 - x269)^2 + (x398 - x409)^2) + 1 / sqrt((x118
    - x130)^2 + (x258 - x270)^2 + (x398 - x410)^2) + 1 / sqrt((x118 - x131)^2
    + (x258 - x271)^2 + (x398 - x411)^2) + 1 / sqrt((x118 - x132)^2 + (x258 -
    x272)^2 + (x398 - x412)^2) + 1 / sqrt((x118 - x133)^2 + (x258 - x273)^2 + (
    x398 - x413)^2) + 1 / sqrt((x118 - x134)^2 + (x258 - x274)^2 + (x398 - x414)
    ^2) + 1 / sqrt((x118 - x135)^2 + (x258 - x275)^2 + (x398 - x415)^2) + 1 /
    sqrt((x118 - x136)^2 + (x258 - x276)^2 + (x398 - x416)^2) + 1 / sqrt((x118
    - x137)^2 + (x258 - x277)^2 + (x398 - x417)^2) + 1 / sqrt((x118 - x138)^2
    + (x258 - x278)^2 + (x398 - x418)^2) + 1 / sqrt((x118 - x139)^2 + (x258 -
    x279)^2 + (x398 - x419)^2) + 1 / sqrt((x118 - x140)^2 + (x258 - x280)^2 + (
    x398 - x420)^2) + 1 / sqrt((x119 - x120)^2 + (x259 - x260)^2 + (x399 - x400)
    ^2) + 1 / sqrt((x119 - x121)^2 + (x259 - x261)^2 + (x399 - x401)^2) + 1 /
    sqrt((x119 - x122)^2 + (x259 - x262)^2 + (x399 - x402)^2) + 1 / sqrt((x119
    - x123)^2 + (x259 - x263)^2 + (x399 - x403)^2) + 1 / sqrt((x119 - x124)^2
    + (x259 - x264)^2 + (x399 - x404)^2) + 1 / sqrt((x119 - x125)^2 + (x259 -
    x265)^2 + (x399 - x405)^2) + 1 / sqrt((x119 - x126)^2 + (x259 - x266)^2 + (
    x399 - x406)^2) + 1 / sqrt((x119 - x127)^2 + (x259 - x267)^2 + (x399 - x407)
    ^2) + 1 / sqrt((x119 - x128)^2 + (x259 - x268)^2 + (x399 - x408)^2) + 1 /
    sqrt((x119 - x129)^2 + (x259 - x269)^2 + (x399 - x409)^2) + 1 / sqrt((x119
    - x130)^2 + (x259 - x270)^2 + (x399 - x410)^2) + 1 / sqrt((x119 - x131)^2
    + (x259 - x271)^2 + (x399 - x411)^2) + 1 / sqrt((x119 - x132)^2 + (x259 -
    x272)^2 + (x399 - x412)^2) + 1 / sqrt((x119 - x133)^2 + (x259 - x273)^2 + (
    x399 - x413)^2) + 1 / sqrt((x119 - x134)^2 + (x259 - x274)^2 + (x399 - x414)
    ^2) + 1 / sqrt((x119 - x135)^2 + (x259 - x275)^2 + (x399 - x415)^2) + 1 /
    sqrt((x119 - x136)^2 + (x259 - x276)^2 + (x399 - x416)^2) + 1 / sqrt((x119
    - x137)^2 + (x259 - x277)^2 + (x399 - x417)^2) + 1 / sqrt((x119 - x138)^2
    + (x259 - x278)^2 + (x399 - x418)^2) + 1 / sqrt((x119 - x139)^2 + (x259 -
    x279)^2 + (x399 - x419)^2) + 1 / sqrt((x119 - x140)^2 + (x259 - x280)^2 + (
    x399 - x420)^2) + 1 / sqrt((x120 - x121)^2 + (x260 - x261)^2 + (x400 - x401)
    ^2) + 1 / sqrt((x120 - x122)^2 + (x260 - x262)^2 + (x400 - x402)^2) + 1 /
    sqrt((x120 - x123)^2 + (x260 - x263)^2 + (x400 - x403)^2) + 1 / sqrt((x120
    - x124)^2 + (x260 - x264)^2 + (x400 - x404)^2) + 1 / sqrt((x120 - x125)^2
    + (x260 - x265)^2 + (x400 - x405)^2) + 1 / sqrt((x120 - x126)^2 + (x260 -
    x266)^2 + (x400 - x406)^2) + 1 / sqrt((x120 - x127)^2 + (x260 - x267)^2 + (
    x400 - x407)^2) + 1 / sqrt((x120 - x128)^2 + (x260 - x268)^2 + (x400 - x408)
    ^2) + 1 / sqrt((x120 - x129)^2 + (x260 - x269)^2 + (x400 - x409)^2) + 1 /
    sqrt((x120 - x130)^2 + (x260 - x270)^2 + (x400 - x410)^2) + 1 / sqrt((x120
    - x131)^2 + (x260 - x271)^2 + (x400 - x411)^2) + 1 / sqrt((x120 - x132)^2
    + (x260 - x272)^2 + (x400 - x412)^2) + 1 / sqrt((x120 - x133)^2 + (x260 -
    x273)^2 + (x400 - x413)^2) + 1 / sqrt((x120 - x134)^2 + (x260 - x274)^2 + (
    x400 - x414)^2) + 1 / sqrt((x120 - x135)^2 + (x260 - x275)^2 + (x400 - x415)
    ^2) + 1 / sqrt((x120 - x136)^2 + (x260 - x276)^2 + (x400 - x416)^2) + 1 /
    sqrt((x120 - x137)^2 + (x260 - x277)^2 + (x400 - x417)^2) + 1 / sqrt((x120
    - x138)^2 + (x260 - x278)^2 + (x400 - x418)^2) + 1 / sqrt((x120 - x139)^2
    + (x260 - x279)^2 + (x400 - x419)^2) + 1 / sqrt((x120 - x140)^2 + (x260 -
    x280)^2 + (x400 - x420)^2) + 1 / sqrt((x121 - x122)^2 + (x261 - x262)^2 + (
    x401 - x402)^2) + 1 / sqrt((x121 - x123)^2 + (x261 - x263)^2 + (x401 - x403)
    ^2) + 1 / sqrt((x121 - x124)^2 + (x261 - x264)^2 + (x401 - x404)^2) + 1 /
    sqrt((x121 - x125)^2 + (x261 - x265)^2 + (x401 - x405)^2) + 1 / sqrt((x121
    - x126)^2 + (x261 - x266)^2 + (x401 - x406)^2) + 1 / sqrt((x121 - x127)^2
    + (x261 - x267)^2 + (x401 - x407)^2) + 1 / sqrt((x121 - x128)^2 + (x261 -
    x268)^2 + (x401 - x408)^2) + 1 / sqrt((x121 - x129)^2 + (x261 - x269)^2 + (
    x401 - x409)^2) + 1 / sqrt((x121 - x130)^2 + (x261 - x270)^2 + (x401 - x410)
    ^2) + 1 / sqrt((x121 - x131)^2 + (x261 - x271)^2 + (x401 - x411)^2) + 1 /
    sqrt((x121 - x132)^2 + (x261 - x272)^2 + (x401 - x412)^2) + 1 / sqrt((x121
    - x133)^2 + (x261 - x273)^2 + (x401 - x413)^2) + 1 / sqrt((x121 - x134)^2
    + (x261 - x274)^2 + (x401 - x414)^2) + 1 / sqrt((x121 - x135)^2 + (x261 -
    x275)^2 + (x401 - x415)^2) + 1 / sqrt((x121 - x136)^2 + (x261 - x276)^2 + (
    x401 - x416)^2) + 1 / sqrt((x121 - x137)^2 + (x261 - x277)^2 + (x401 - x417)
    ^2) + 1 / sqrt((x121 - x138)^2 + (x261 - x278)^2 + (x401 - x418)^2) + 1 /
    sqrt((x121 - x139)^2 + (x261 - x279)^2 + (x401 - x419)^2) + 1 / sqrt((x121
    - x140)^2 + (x261 - x280)^2 + (x401 - x420)^2) + 1 / sqrt((x122 - x123)^2
    + (x262 - x263)^2 + (x402 - x403)^2) + 1 / sqrt((x122 - x124)^2 + (x262 -
    x264)^2 + (x402 - x404)^2) + 1 / sqrt((x122 - x125)^2 + (x262 - x265)^2 + (
    x402 - x405)^2) + 1 / sqrt((x122 - x126)^2 + (x262 - x266)^2 + (x402 - x406)
    ^2) + 1 / sqrt((x122 - x127)^2 + (x262 - x267)^2 + (x402 - x407)^2) + 1 /
    sqrt((x122 - x128)^2 + (x262 - x268)^2 + (x402 - x408)^2) + 1 / sqrt((x122
    - x129)^2 + (x262 - x269)^2 + (x402 - x409)^2) + 1 / sqrt((x122 - x130)^2
    + (x262 - x270)^2 + (x402 - x410)^2) + 1 / sqrt((x122 - x131)^2 + (x262 -
    x271)^2 + (x402 - x411)^2) + 1 / sqrt((x122 - x132)^2 + (x262 - x272)^2 + (
    x402 - x412)^2) + 1 / sqrt((x122 - x133)^2 + (x262 - x273)^2 + (x402 - x413)
    ^2) + 1 / sqrt((x122 - x134)^2 + (x262 - x274)^2 + (x402 - x414)^2) + 1 /
    sqrt((x122 - x135)^2 + (x262 - x275)^2 + (x402 - x415)^2) + 1 / sqrt((x122
    - x136)^2 + (x262 - x276)^2 + (x402 - x416)^2) + 1 / sqrt((x122 - x137)^2
    + (x262 - x277)^2 + (x402 - x417)^2) + 1 / sqrt((x122 - x138)^2 + (x262 -
    x278)^2 + (x402 - x418)^2) + 1 / sqrt((x122 - x139)^2 + (x262 - x279)^2 + (
    x402 - x419)^2) + 1 / sqrt((x122 - x140)^2 + (x262 - x280)^2 + (x402 - x420)
    ^2) + 1 / sqrt((x123 - x124)^2 + (x263 - x264)^2 + (x403 - x404)^2) + 1 /
    sqrt((x123 - x125)^2 + (x263 - x265)^2 + (x403 - x405)^2) + 1 / sqrt((x123
    - x126)^2 + (x263 - x266)^2 + (x403 - x406)^2) + 1 / sqrt((x123 - x127)^2
    + (x263 - x267)^2 + (x403 - x407)^2) + 1 / sqrt((x123 - x128)^2 + (x263 -
    x268)^2 + (x403 - x408)^2) + 1 / sqrt((x123 - x129)^2 + (x263 - x269)^2 + (
    x403 - x409)^2) + 1 / sqrt((x123 - x130)^2 + (x263 - x270)^2 + (x403 - x410)
    ^2) + 1 / sqrt((x123 - x131)^2 + (x263 - x271)^2 + (x403 - x411)^2) + 1 /
    sqrt((x123 - x132)^2 + (x263 - x272)^2 + (x403 - x412)^2) + 1 / sqrt((x123
    - x133)^2 + (x263 - x273)^2 + (x403 - x413)^2) + 1 / sqrt((x123 - x134)^2
    + (x263 - x274)^2 + (x403 - x414)^2) + 1 / sqrt((x123 - x135)^2 + (x263 -
    x275)^2 + (x403 - x415)^2) + 1 / sqrt((x123 - x136)^2 + (x263 - x276)^2 + (
    x403 - x416)^2) + 1 / sqrt((x123 - x137)^2 + (x263 - x277)^2 + (x403 - x417)
    ^2) + 1 / sqrt((x123 - x138)^2 + (x263 - x278)^2 + (x403 - x418)^2) + 1 /
    sqrt((x123 - x139)^2 + (x263 - x279)^2 + (x403 - x419)^2) + 1 / sqrt((x123
    - x140)^2 + (x263 - x280)^2 + (x403 - x420)^2) + 1 / sqrt((x124 - x125)^2
    + (x264 - x265)^2 + (x404 - x405)^2) + 1 / sqrt((x124 - x126)^2 + (x264 -
    x266)^2 + (x404 - x406)^2) + 1 / sqrt((x124 - x127)^2 + (x264 - x267)^2 + (
    x404 - x407)^2) + 1 / sqrt((x124 - x128)^2 + (x264 - x268)^2 + (x404 - x408)
    ^2) + 1 / sqrt((x124 - x129)^2 + (x264 - x269)^2 + (x404 - x409)^2) + 1 /
    sqrt((x124 - x130)^2 + (x264 - x270)^2 + (x404 - x410)^2) + 1 / sqrt((x124
    - x131)^2 + (x264 - x271)^2 + (x404 - x411)^2) + 1 / sqrt((x124 - x132)^2
    + (x264 - x272)^2 + (x404 - x412)^2) + 1 / sqrt((x124 - x133)^2 + (x264 -
    x273)^2 + (x404 - x413)^2) + 1 / sqrt((x124 - x134)^2 + (x264 - x274)^2 + (
    x404 - x414)^2) + 1 / sqrt((x124 - x135)^2 + (x264 - x275)^2 + (x404 - x415)
    ^2) + 1 / sqrt((x124 - x136)^2 + (x264 - x276)^2 + (x404 - x416)^2) + 1 /
    sqrt((x124 - x137)^2 + (x264 - x277)^2 + (x404 - x417)^2) + 1 / sqrt((x124
    - x138)^2 + (x264 - x278)^2 + (x404 - x418)^2) + 1 / sqrt((x124 - x139)^2
    + (x264 - x279)^2 + (x404 - x419)^2) + 1 / sqrt((x124 - x140)^2 + (x264 -
    x280)^2 + (x404 - x420)^2) + 1 / sqrt((x125 - x126)^2 + (x265 - x266)^2 + (
    x405 - x406)^2) + 1 / sqrt((x125 - x127)^2 + (x265 - x267)^2 + (x405 - x407)
    ^2) + 1 / sqrt((x125 - x128)^2 + (x265 - x268)^2 + (x405 - x408)^2) + 1 /
    sqrt((x125 - x129)^2 + (x265 - x269)^2 + (x405 - x409)^2) + 1 / sqrt((x125
    - x130)^2 + (x265 - x270)^2 + (x405 - x410)^2) + 1 / sqrt((x125 - x131)^2
    + (x265 - x271)^2 + (x405 - x411)^2) + 1 / sqrt((x125 - x132)^2 + (x265 -
    x272)^2 + (x405 - x412)^2) + 1 / sqrt((x125 - x133)^2 + (x265 - x273)^2 + (
    x405 - x413)^2) + 1 / sqrt((x125 - x134)^2 + (x265 - x274)^2 + (x405 - x414)
    ^2) + 1 / sqrt((x125 - x135)^2 + (x265 - x275)^2 + (x405 - x415)^2) + 1 /
    sqrt((x125 - x136)^2 + (x265 - x276)^2 + (x405 - x416)^2) + 1 / sqrt((x125
    - x137)^2 + (x265 - x277)^2 + (x405 - x417)^2) + 1 / sqrt((x125 - x138)^2
    + (x265 - x278)^2 + (x405 - x418)^2) + 1 / sqrt((x125 - x139)^2 + (x265 -
    x279)^2 + (x405 - x419)^2) + 1 / sqrt((x125 - x140)^2 + (x265 - x280)^2 + (
    x405 - x420)^2) + 1 / sqrt((x126 - x127)^2 + (x266 - x267)^2 + (x406 - x407)
    ^2) + 1 / sqrt((x126 - x128)^2 + (x266 - x268)^2 + (x406 - x408)^2) + 1 /
    sqrt((x126 - x129)^2 + (x266 - x269)^2 + (x406 - x409)^2) + 1 / sqrt((x126
    - x130)^2 + (x266 - x270)^2 + (x406 - x410)^2) + 1 / sqrt((x126 - x131)^2
    + (x266 - x271)^2 + (x406 - x411)^2) + 1 / sqrt((x126 - x132)^2 + (x266 -
    x272)^2 + (x406 - x412)^2) + 1 / sqrt((x126 - x133)^2 + (x266 - x273)^2 + (
    x406 - x413)^2) + 1 / sqrt((x126 - x134)^2 + (x266 - x274)^2 + (x406 - x414)
    ^2) + 1 / sqrt((x126 - x135)^2 + (x266 - x275)^2 + (x406 - x415)^2) + 1 /
    sqrt((x126 - x136)^2 + (x266 - x276)^2 + (x406 - x416)^2) + 1 / sqrt((x126
    - x137)^2 + (x266 - x277)^2 + (x406 - x417)^2) + 1 / sqrt((x126 - x138)^2
    + (x266 - x278)^2 + (x406 - x418)^2) + 1 / sqrt((x126 - x139)^2 + (x266 -
    x279)^2 + (x406 - x419)^2) + 1 / sqrt((x126 - x140)^2 + (x266 - x280)^2 + (
    x406 - x420)^2) + 1 / sqrt((x127 - x128)^2 + (x267 - x268)^2 + (x407 - x408)
    ^2) + 1 / sqrt((x127 - x129)^2 + (x267 - x269)^2 + (x407 - x409)^2) + 1 /
    sqrt((x127 - x130)^2 + (x267 - x270)^2 + (x407 - x410)^2) + 1 / sqrt((x127
    - x131)^2 + (x267 - x271)^2 + (x407 - x411)^2) + 1 / sqrt((x127 - x132)^2
    + (x267 - x272)^2 + (x407 - x412)^2) + 1 / sqrt((x127 - x133)^2 + (x267 -
    x273)^2 + (x407 - x413)^2) + 1 / sqrt((x127 - x134)^2 + (x267 - x274)^2 + (
    x407 - x414)^2) + 1 / sqrt((x127 - x135)^2 + (x267 - x275)^2 + (x407 - x415)
    ^2) + 1 / sqrt((x127 - x136)^2 + (x267 - x276)^2 + (x407 - x416)^2) + 1 /
    sqrt((x127 - x137)^2 + (x267 - x277)^2 + (x407 - x417)^2) + 1 / sqrt((x127
    - x138)^2 + (x267 - x278)^2 + (x407 - x418)^2) + 1 / sqrt((x127 - x139)^2
    + (x267 - x279)^2 + (x407 - x419)^2) + 1 / sqrt((x127 - x140)^2 + (x267 -
    x280)^2 + (x407 - x420)^2) + 1 / sqrt((x128 - x129)^2 + (x268 - x269)^2 + (
    x408 - x409)^2) + 1 / sqrt((x128 - x130)^2 + (x268 - x270)^2 + (x408 - x410)
    ^2) + 1 / sqrt((x128 - x131)^2 + (x268 - x271)^2 + (x408 - x411)^2) + 1 /
    sqrt((x128 - x132)^2 + (x268 - x272)^2 + (x408 - x412)^2) + 1 / sqrt((x128
    - x133)^2 + (x268 - x273)^2 + (x408 - x413)^2) + 1 / sqrt((x128 - x134)^2
    + (x268 - x274)^2 + (x408 - x414)^2) + 1 / sqrt((x128 - x135)^2 + (x268 -
    x275)^2 + (x408 - x415)^2) + 1 / sqrt((x128 - x136)^2 + (x268 - x276)^2 + (
    x408 - x416)^2) + 1 / sqrt((x128 - x137)^2 + (x268 - x277)^2 + (x408 - x417)
    ^2) + 1 / sqrt((x128 - x138)^2 + (x268 - x278)^2 + (x408 - x418)^2) + 1 /
    sqrt((x128 - x139)^2 + (x268 - x279)^2 + (x408 - x419)^2) + 1 / sqrt((x128
    - x140)^2 + (x268 - x280)^2 + (x408 - x420)^2) + 1 / sqrt((x129 - x130)^2
    + (x269 - x270)^2 + (x409 - x410)^2) + 1 / sqrt((x129 - x131)^2 + (x269 -
    x271)^2 + (x409 - x411)^2) + 1 / sqrt((x129 - x132)^2 + (x269 - x272)^2 + (
    x409 - x412)^2) + 1 / sqrt((x129 - x133)^2 + (x269 - x273)^2 + (x409 - x413)
    ^2) + 1 / sqrt((x129 - x134)^2 + (x269 - x274)^2 + (x409 - x414)^2) + 1 /
    sqrt((x129 - x135)^2 + (x269 - x275)^2 + (x409 - x415)^2) + 1 / sqrt((x129
    - x136)^2 + (x269 - x276)^2 + (x409 - x416)^2) + 1 / sqrt((x129 - x137)^2
    + (x269 - x277)^2 + (x409 - x417)^2) + 1 / sqrt((x129 - x138)^2 + (x269 -
    x278)^2 + (x409 - x418)^2) + 1 / sqrt((x129 - x139)^2 + (x269 - x279)^2 + (
    x409 - x419)^2) + 1 / sqrt((x129 - x140)^2 + (x269 - x280)^2 + (x409 - x420)
    ^2) + 1 / sqrt((x130 - x131)^2 + (x270 - x271)^2 + (x410 - x411)^2) + 1 /
    sqrt((x130 - x132)^2 + (x270 - x272)^2 + (x410 - x412)^2) + 1 / sqrt((x130
    - x133)^2 + (x270 - x273)^2 + (x410 - x413)^2) + 1 / sqrt((x130 - x134)^2
    + (x270 - x274)^2 + (x410 - x414)^2) + 1 / sqrt((x130 - x135)^2 + (x270 -
    x275)^2 + (x410 - x415)^2) + 1 / sqrt((x130 - x136)^2 + (x270 - x276)^2 + (
    x410 - x416)^2) + 1 / sqrt((x130 - x137)^2 + (x270 - x277)^2 + (x410 - x417)
    ^2) + 1 / sqrt((x130 - x138)^2 + (x270 - x278)^2 + (x410 - x418)^2) + 1 /
    sqrt((x130 - x139)^2 + (x270 - x279)^2 + (x410 - x419)^2) + 1 / sqrt((x130
    - x140)^2 + (x270 - x280)^2 + (x410 - x420)^2) + 1 / sqrt((x131 - x132)^2
    + (x271 - x272)^2 + (x411 - x412)^2) + 1 / sqrt((x131 - x133)^2 + (x271 -
    x273)^2 + (x411 - x413)^2) + 1 / sqrt((x131 - x134)^2 + (x271 - x274)^2 + (
    x411 - x414)^2) + 1 / sqrt((x131 - x135)^2 + (x271 - x275)^2 + (x411 - x415)
    ^2) + 1 / sqrt((x131 - x136)^2 + (x271 - x276)^2 + (x411 - x416)^2) + 1 /
    sqrt((x131 - x137)^2 + (x271 - x277)^2 + (x411 - x417)^2) + 1 / sqrt((x131
    - x138)^2 + (x271 - x278)^2 + (x411 - x418)^2) + 1 / sqrt((x131 - x139)^2
    + (x271 - x279)^2 + (x411 - x419)^2) + 1 / sqrt((x131 - x140)^2 + (x271 -
    x280)^2 + (x411 - x420)^2) + 1 / sqrt((x132 - x133)^2 + (x272 - x273)^2 + (
    x412 - x413)^2) + 1 / sqrt((x132 - x134)^2 + (x272 - x274)^2 + (x412 - x414)
    ^2) + 1 / sqrt((x132 - x135)^2 + (x272 - x275)^2 + (x412 - x415)^2) + 1 /
    sqrt((x132 - x136)^2 + (x272 - x276)^2 + (x412 - x416)^2) + 1 / sqrt((x132
    - x137)^2 + (x272 - x277)^2 + (x412 - x417)^2) + 1 / sqrt((x132 - x138)^2
    + (x272 - x278)^2 + (x412 - x418)^2) + 1 / sqrt((x132 - x139)^2 + (x272 -
    x279)^2 + (x412 - x419)^2) + 1 / sqrt((x132 - x140)^2 + (x272 - x280)^2 + (
    x412 - x420)^2) + 1 / sqrt((x133 - x134)^2 + (x273 - x274)^2 + (x413 - x414)
    ^2) + 1 / sqrt((x133 - x135)^2 + (x273 - x275)^2 + (x413 - x415)^2) + 1 /
    sqrt((x133 - x136)^2 + (x273 - x276)^2 + (x413 - x416)^2) + 1 / sqrt((x133
    - x137)^2 + (x273 - x277)^2 + (x413 - x417)^2) + 1 / sqrt((x133 - x138)^2
    + (x273 - x278)^2 + (x413 - x418)^2) + 1 / sqrt((x133 - x139)^2 + (x273 -
    x279)^2 + (x413 - x419)^2) + 1 / sqrt((x133 - x140)^2 + (x273 - x280)^2 + (
    x413 - x420)^2) + 1 / sqrt((x134 - x135)^2 + (x274 - x275)^2 + (x414 - x415)
    ^2) + 1 / sqrt((x134 - x136)^2 + (x274 - x276)^2 + (x414 - x416)^2) + 1 /
    sqrt((x134 - x137)^2 + (x274 - x277)^2 + (x414 - x417)^2) + 1 / sqrt((x134
    - x138)^2 + (x274 - x278)^2 + (x414 - x418)^2) + 1 / sqrt((x134 - x139)^2
    + (x274 - x279)^2 + (x414 - x419)^2) + 1 / sqrt((x134 - x140)^2 + (x274 -
    x280)^2 + (x414 - x420)^2) + 1 / sqrt((x135 - x136)^2 + (x275 - x276)^2 + (
    x415 - x416)^2) + 1 / sqrt((x135 - x137)^2 + (x275 - x277)^2 + (x415 - x417)
    ^2) + 1 / sqrt((x135 - x138)^2 + (x275 - x278)^2 + (x415 - x418)^2) + 1 /
    sqrt((x135 - x139)^2 + (x275 - x279)^2 + (x415 - x419)^2) + 1 / sqrt((x135
    - x140)^2 + (x275 - x280)^2 + (x415 - x420)^2) + 1 / sqrt((x136 - x137)^2
    + (x276 - x277)^2 + (x416 - x417)^2) + 1 / sqrt((x136 - x138)^2 + (x276 -
    x278)^2 + (x416 - x418)^2) + 1 / sqrt((x136 - x139)^2 + (x276 - x279)^2 + (
    x416 - x419)^2) + 1 / sqrt((x136 - x140)^2 + (x276 - x280)^2 + (x416 - x420)
    ^2) + 1 / sqrt((x137 - x138)^2 + (x277 - x278)^2 + (x417 - x418)^2) + 1 /
    sqrt((x137 - x139)^2 + (x277 - x279)^2 + (x417 - x419)^2) + 1 / sqrt((x137
    - x140)^2 + (x277 - x280)^2 + (x417 - x420)^2) + 1 / sqrt((x138 - x139)^2
    + (x278 - x279)^2 + (x418 - x419)^2) + 1 / sqrt((x138 - x140)^2 + (x278 -
    x280)^2 + (x418 - x420)^2) + 1 / sqrt((x139 - x140)^2 + (x279 - x280)^2 + (
    x419 - x420)^2))

@NLconstraint(m, e1, x1^2 + x141^2 + x281^2 == 1)
@NLconstraint(m, e2, x2^2 + x142^2 + x282^2 == 1)
@NLconstraint(m, e3, x3^2 + x143^2 + x283^2 == 1)
@NLconstraint(m, e4, x4^2 + x144^2 + x284^2 == 1)
@NLconstraint(m, e5, x5^2 + x145^2 + x285^2 == 1)
@NLconstraint(m, e6, x6^2 + x146^2 + x286^2 == 1)
@NLconstraint(m, e7, x7^2 + x147^2 + x287^2 == 1)
@NLconstraint(m, e8, x8^2 + x148^2 + x288^2 == 1)
@NLconstraint(m, e9, x9^2 + x149^2 + x289^2 == 1)
@NLconstraint(m, e10, x10^2 + x150^2 + x290^2 == 1)
@NLconstraint(m, e11, x11^2 + x151^2 + x291^2 == 1)
@NLconstraint(m, e12, x12^2 + x152^2 + x292^2 == 1)
@NLconstraint(m, e13, x13^2 + x153^2 + x293^2 == 1)
@NLconstraint(m, e14, x14^2 + x154^2 + x294^2 == 1)
@NLconstraint(m, e15, x15^2 + x155^2 + x295^2 == 1)
@NLconstraint(m, e16, x16^2 + x156^2 + x296^2 == 1)
@NLconstraint(m, e17, x17^2 + x157^2 + x297^2 == 1)
@NLconstraint(m, e18, x18^2 + x158^2 + x298^2 == 1)
@NLconstraint(m, e19, x19^2 + x159^2 + x299^2 == 1)
@NLconstraint(m, e20, x20^2 + x160^2 + x300^2 == 1)
@NLconstraint(m, e21, x21^2 + x161^2 + x301^2 == 1)
@NLconstraint(m, e22, x22^2 + x162^2 + x302^2 == 1)
@NLconstraint(m, e23, x23^2 + x163^2 + x303^2 == 1)
@NLconstraint(m, e24, x24^2 + x164^2 + x304^2 == 1)
@NLconstraint(m, e25, x25^2 + x165^2 + x305^2 == 1)
@NLconstraint(m, e26, x26^2 + x166^2 + x306^2 == 1)
@NLconstraint(m, e27, x27^2 + x167^2 + x307^2 == 1)
@NLconstraint(m, e28, x28^2 + x168^2 + x308^2 == 1)
@NLconstraint(m, e29, x29^2 + x169^2 + x309^2 == 1)
@NLconstraint(m, e30, x30^2 + x170^2 + x310^2 == 1)
@NLconstraint(m, e31, x31^2 + x171^2 + x311^2 == 1)
@NLconstraint(m, e32, x32^2 + x172^2 + x312^2 == 1)
@NLconstraint(m, e33, x33^2 + x173^2 + x313^2 == 1)
@NLconstraint(m, e34, x34^2 + x174^2 + x314^2 == 1)
@NLconstraint(m, e35, x35^2 + x175^2 + x315^2 == 1)
@NLconstraint(m, e36, x36^2 + x176^2 + x316^2 == 1)
@NLconstraint(m, e37, x37^2 + x177^2 + x317^2 == 1)
@NLconstraint(m, e38, x38^2 + x178^2 + x318^2 == 1)
@NLconstraint(m, e39, x39^2 + x179^2 + x319^2 == 1)
@NLconstraint(m, e40, x40^2 + x180^2 + x320^2 == 1)
@NLconstraint(m, e41, x41^2 + x181^2 + x321^2 == 1)
@NLconstraint(m, e42, x42^2 + x182^2 + x322^2 == 1)
@NLconstraint(m, e43, x43^2 + x183^2 + x323^2 == 1)
@NLconstraint(m, e44, x44^2 + x184^2 + x324^2 == 1)
@NLconstraint(m, e45, x45^2 + x185^2 + x325^2 == 1)
@NLconstraint(m, e46, x46^2 + x186^2 + x326^2 == 1)
@NLconstraint(m, e47, x47^2 + x187^2 + x327^2 == 1)
@NLconstraint(m, e48, x48^2 + x188^2 + x328^2 == 1)
@NLconstraint(m, e49, x49^2 + x189^2 + x329^2 == 1)
@NLconstraint(m, e50, x50^2 + x190^2 + x330^2 == 1)
@NLconstraint(m, e51, x51^2 + x191^2 + x331^2 == 1)
@NLconstraint(m, e52, x52^2 + x192^2 + x332^2 == 1)
@NLconstraint(m, e53, x53^2 + x193^2 + x333^2 == 1)
@NLconstraint(m, e54, x54^2 + x194^2 + x334^2 == 1)
@NLconstraint(m, e55, x55^2 + x195^2 + x335^2 == 1)
@NLconstraint(m, e56, x56^2 + x196^2 + x336^2 == 1)
@NLconstraint(m, e57, x57^2 + x197^2 + x337^2 == 1)
@NLconstraint(m, e58, x58^2 + x198^2 + x338^2 == 1)
@NLconstraint(m, e59, x59^2 + x199^2 + x339^2 == 1)
@NLconstraint(m, e60, x60^2 + x200^2 + x340^2 == 1)
@NLconstraint(m, e61, x61^2 + x201^2 + x341^2 == 1)
@NLconstraint(m, e62, x62^2 + x202^2 + x342^2 == 1)
@NLconstraint(m, e63, x63^2 + x203^2 + x343^2 == 1)
@NLconstraint(m, e64, x64^2 + x204^2 + x344^2 == 1)
@NLconstraint(m, e65, x65^2 + x205^2 + x345^2 == 1)
@NLconstraint(m, e66, x66^2 + x206^2 + x346^2 == 1)
@NLconstraint(m, e67, x67^2 + x207^2 + x347^2 == 1)
@NLconstraint(m, e68, x68^2 + x208^2 + x348^2 == 1)
@NLconstraint(m, e69, x69^2 + x209^2 + x349^2 == 1)
@NLconstraint(m, e70, x70^2 + x210^2 + x350^2 == 1)
@NLconstraint(m, e71, x71^2 + x211^2 + x351^2 == 1)
@NLconstraint(m, e72, x72^2 + x212^2 + x352^2 == 1)
@NLconstraint(m, e73, x73^2 + x213^2 + x353^2 == 1)
@NLconstraint(m, e74, x74^2 + x214^2 + x354^2 == 1)
@NLconstraint(m, e75, x75^2 + x215^2 + x355^2 == 1)
@NLconstraint(m, e76, x76^2 + x216^2 + x356^2 == 1)
@NLconstraint(m, e77, x77^2 + x217^2 + x357^2 == 1)
@NLconstraint(m, e78, x78^2 + x218^2 + x358^2 == 1)
@NLconstraint(m, e79, x79^2 + x219^2 + x359^2 == 1)
@NLconstraint(m, e80, x80^2 + x220^2 + x360^2 == 1)
@NLconstraint(m, e81, x81^2 + x221^2 + x361^2 == 1)
@NLconstraint(m, e82, x82^2 + x222^2 + x362^2 == 1)
@NLconstraint(m, e83, x83^2 + x223^2 + x363^2 == 1)
@NLconstraint(m, e84, x84^2 + x224^2 + x364^2 == 1)
@NLconstraint(m, e85, x85^2 + x225^2 + x365^2 == 1)
@NLconstraint(m, e86, x86^2 + x226^2 + x366^2 == 1)
@NLconstraint(m, e87, x87^2 + x227^2 + x367^2 == 1)
@NLconstraint(m, e88, x88^2 + x228^2 + x368^2 == 1)
@NLconstraint(m, e89, x89^2 + x229^2 + x369^2 == 1)
@NLconstraint(m, e90, x90^2 + x230^2 + x370^2 == 1)
@NLconstraint(m, e91, x91^2 + x231^2 + x371^2 == 1)
@NLconstraint(m, e92, x92^2 + x232^2 + x372^2 == 1)
@NLconstraint(m, e93, x93^2 + x233^2 + x373^2 == 1)
@NLconstraint(m, e94, x94^2 + x234^2 + x374^2 == 1)
@NLconstraint(m, e95, x95^2 + x235^2 + x375^2 == 1)
@NLconstraint(m, e96, x96^2 + x236^2 + x376^2 == 1)
@NLconstraint(m, e97, x97^2 + x237^2 + x377^2 == 1)
@NLconstraint(m, e98, x98^2 + x238^2 + x378^2 == 1)
@NLconstraint(m, e99, x99^2 + x239^2 + x379^2 == 1)
@NLconstraint(m, e100, x100^2 + x240^2 + x380^2 == 1)
@NLconstraint(m, e101, x101^2 + x241^2 + x381^2 == 1)
@NLconstraint(m, e102, x102^2 + x242^2 + x382^2 == 1)
@NLconstraint(m, e103, x103^2 + x243^2 + x383^2 == 1)
@NLconstraint(m, e104, x104^2 + x244^2 + x384^2 == 1)
@NLconstraint(m, e105, x105^2 + x245^2 + x385^2 == 1)
@NLconstraint(m, e106, x106^2 + x246^2 + x386^2 == 1)
@NLconstraint(m, e107, x107^2 + x247^2 + x387^2 == 1)
@NLconstraint(m, e108, x108^2 + x248^2 + x388^2 == 1)
@NLconstraint(m, e109, x109^2 + x249^2 + x389^2 == 1)
@NLconstraint(m, e110, x110^2 + x250^2 + x390^2 == 1)
@NLconstraint(m, e111, x111^2 + x251^2 + x391^2 == 1)
@NLconstraint(m, e112, x112^2 + x252^2 + x392^2 == 1)
@NLconstraint(m, e113, x113^2 + x253^2 + x393^2 == 1)
@NLconstraint(m, e114, x114^2 + x254^2 + x394^2 == 1)
@NLconstraint(m, e115, x115^2 + x255^2 + x395^2 == 1)
@NLconstraint(m, e116, x116^2 + x256^2 + x396^2 == 1)
@NLconstraint(m, e117, x117^2 + x257^2 + x397^2 == 1)
@NLconstraint(m, e118, x118^2 + x258^2 + x398^2 == 1)
@NLconstraint(m, e119, x119^2 + x259^2 + x399^2 == 1)
@NLconstraint(m, e120, x120^2 + x260^2 + x400^2 == 1)
@NLconstraint(m, e121, x121^2 + x261^2 + x401^2 == 1)
@NLconstraint(m, e122, x122^2 + x262^2 + x402^2 == 1)
@NLconstraint(m, e123, x123^2 + x263^2 + x403^2 == 1)
@NLconstraint(m, e124, x124^2 + x264^2 + x404^2 == 1)
@NLconstraint(m, e125, x125^2 + x265^2 + x405^2 == 1)
@NLconstraint(m, e126, x126^2 + x266^2 + x406^2 == 1)
@NLconstraint(m, e127, x127^2 + x267^2 + x407^2 == 1)
@NLconstraint(m, e128, x128^2 + x268^2 + x408^2 == 1)
@NLconstraint(m, e129, x129^2 + x269^2 + x409^2 == 1)
@NLconstraint(m, e130, x130^2 + x270^2 + x410^2 == 1)
@NLconstraint(m, e131, x131^2 + x271^2 + x411^2 == 1)
@NLconstraint(m, e132, x132^2 + x272^2 + x412^2 == 1)
@NLconstraint(m, e133, x133^2 + x273^2 + x413^2 == 1)
@NLconstraint(m, e134, x134^2 + x274^2 + x414^2 == 1)
@NLconstraint(m, e135, x135^2 + x275^2 + x415^2 == 1)
@NLconstraint(m, e136, x136^2 + x276^2 + x416^2 == 1)
@NLconstraint(m, e137, x137^2 + x277^2 + x417^2 == 1)
@NLconstraint(m, e138, x138^2 + x278^2 + x418^2 == 1)
@NLconstraint(m, e139, x139^2 + x279^2 + x419^2 == 1)
@NLconstraint(m, e140, x140^2 + x280^2 + x420^2 == 1)