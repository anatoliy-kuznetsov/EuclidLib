# MINLP written by GAMS Convert at 05/15/24 11:55:45
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

using JuMP
using MathOptInterface
const MOI = MathOptInterface

model = m = Model()

@variable(m, 0 <= x1 <= 2, start=0)
@variable(m, 0 <= x2 <= 2, start=0)
@variable(m, 0 <= x3 <= 2, start=0)
@variable(m, 0 <= x4 <= 2, start=0)
@variable(m, 0 <= x5 <= 2, start=0)
@variable(m, 0 <= x6 <= 2, start=0)
@variable(m, 0 <= x7 <= 2, start=0)
@variable(m, 0 <= x8 <= 2, start=0)
@variable(m, 0 <= x9 <= 2, start=0)
@variable(m, 0 <= x10 <= 2, start=0)
@variable(m, 0 <= x11 <= 2, start=0)
@variable(m, 0 <= x12 <= 2, start=0)
@variable(m, 0 <= x13 <= 2, start=0)
@variable(m, 0 <= x14 <= 2, start=0)
@variable(m, 0 <= x15 <= 2, start=0)
@variable(m, 0 <= x16 <= 2, start=0)
@variable(m, 0 <= x17 <= 2, start=0)
@variable(m, 0 <= x18 <= 2, start=0)
@variable(m, 0 <= x19 <= 2, start=0)
@variable(m, 0 <= x20 <= 2, start=0)
@variable(m, 0 <= x21 <= 2, start=0)
@variable(m, 0 <= x22 <= 2, start=0)
@variable(m, 0 <= x23 <= 2, start=0)
@variable(m, 0 <= x24 <= 2, start=0)
@variable(m, 0 <= x25 <= 2, start=0)
@variable(m, 0 <= x26 <= 2, start=0)
@variable(m, 0 <= x27 <= 2, start=0)
@variable(m, 0 <= x28 <= 2, start=0)
@variable(m, 0 <= x29 <= 2, start=0)
@variable(m, 0 <= x30 <= 2, start=0)
@variable(m, 0 <= x31 <= 2, start=0)
@variable(m, 0 <= x32 <= 2, start=0)
@variable(m, 0 <= x33 <= 2, start=0)
@variable(m, 0 <= x34 <= 2, start=0)
@variable(m, 0 <= x35 <= 2, start=0)
@variable(m, 0 <= x36 <= 2, start=0)
@variable(m, 0 <= x37 <= 2, start=0)
@variable(m, 0 <= x38 <= 2, start=0)
@variable(m, 0 <= x39 <= 2, start=0)
@variable(m, 0 <= x40 <= 2, start=0)
@variable(m, 0 <= x41 <= 2, start=0)
@variable(m, 0 <= x42 <= 2, start=0)
@variable(m, 0 <= x43 <= 2, start=0)
@variable(m, 0 <= x44 <= 2, start=0)
@variable(m, 0 <= x45 <= 2, start=0)
@variable(m, 0 <= x46 <= 2, start=0)
@variable(m, 0 <= x47 <= 2, start=0)
@variable(m, 0 <= x48 <= 2, start=0)
@variable(m, 0 <= x49 <= 2, start=0)
@variable(m, 0 <= x50 <= 2, start=0)
@variable(m, 0 <= x51 <= 2, start=0)
@variable(m, 0 <= x52 <= 2, start=0)
@variable(m, 0 <= x53 <= 2, start=0)
@variable(m, 0 <= x54 <= 2, start=0)
@variable(m, 0 <= x55 <= 2, start=0)
@variable(m, 0 <= x56 <= 2, start=0)
@variable(m, 0 <= x57 <= 2, start=0)
@variable(m, 0 <= x58 <= 2, start=0)
@variable(m, 0 <= x59 <= 2, start=0)
@variable(m, 0 <= x60 <= 2, start=0)
@variable(m, 0 <= x61 <= 2, start=0)
@variable(m, 0 <= x62 <= 2, start=0)
@variable(m, 0 <= x63 <= 2, start=0)
@variable(m, 0 <= x64 <= 2, start=0)
@variable(m, 0 <= x65 <= 2, start=0)
@variable(m, 0 <= x66 <= 2, start=0)
@variable(m, 0 <= x67 <= 2, start=0)
@variable(m, 0 <= x68 <= 2, start=0)
@variable(m, 0 <= x69 <= 2, start=0)
@variable(m, 0 <= x70 <= 2, start=0)
@variable(m, 0 <= x71 <= 2, start=0)
@variable(m, 0 <= x72 <= 2, start=0)
@variable(m, 0 <= x73 <= 2, start=0)
@variable(m, 0 <= x74 <= 2, start=0)
@variable(m, 0 <= x75 <= 2, start=0)
@variable(m, 0 <= x76 <= 2, start=0)
@variable(m, 0 <= x77 <= 2, start=0)
@variable(m, 0 <= x78 <= 2, start=0)
@variable(m, 0 <= x79 <= 2, start=0)
@variable(m, 0 <= x80 <= 2, start=0)
@variable(m, 0 <= x81 <= 2, start=0)
@variable(m, 0 <= x82 <= 2, start=0)
@variable(m, 0 <= x83 <= 2, start=0)
@variable(m, 0 <= x84 <= 2, start=0)
@variable(m, 0 <= x85 <= 2, start=0)
@variable(m, 0 <= x86 <= 2, start=0)
@variable(m, 0 <= x87 <= 2, start=0)
@variable(m, 0 <= x88 <= 2, start=0)
@variable(m, 0 <= x89 <= 2, start=0)
@variable(m, 0 <= x90 <= 2, start=0)
@variable(m, 0 <= x91 <= 2, start=0)
@variable(m, 0 <= x92 <= 2, start=0)
@variable(m, 0 <= x93 <= 2, start=0)
@variable(m, 0 <= x94 <= 2, start=0)
@variable(m, 0 <= x95 <= 2, start=0)
@variable(m, 0 <= x96 <= 2, start=0)
@variable(m, 0 <= x97 <= 2, start=0)
@variable(m, 0 <= x98 <= 2, start=0)
@variable(m, 0 <= x99 <= 2, start=0)
@variable(m, 0 <= x100 <= 2, start=0)
@variable(m, 0 <= x101 <= 2, start=0)
@variable(m, 0 <= x102 <= 2, start=0)
@variable(m, 0 <= x103 <= 2, start=0)
@variable(m, 0 <= x104 <= 2, start=0)
@variable(m, 0 <= x105 <= 2, start=0)
@variable(m, 0 <= x106 <= 2, start=0)
@variable(m, 0 <= x107 <= 2, start=0)
@variable(m, 0 <= x108 <= 2, start=0)
@variable(m, 0 <= x109 <= 2, start=0)
@variable(m, 0 <= x110 <= 2, start=0)
@variable(m, 0 <= x111 <= 2, start=0)
@variable(m, 0 <= x112 <= 2, start=0)
@variable(m, 0 <= x113 <= 2, start=0)
@variable(m, 0 <= x114 <= 2, start=0)
@variable(m, 0 <= x115 <= 2, start=0)
@variable(m, 0 <= x116 <= 2, start=0)
@variable(m, 0 <= x117 <= 2, start=0)
@variable(m, 0 <= x118 <= 2, start=0)
@variable(m, 0 <= x119 <= 2, start=0)
@variable(m, 0 <= x120 <= 2, start=0)
@variable(m, 0 <= x121 <= 2, start=0)
@variable(m, 0 <= x122 <= 2, start=0)
@variable(m, 0 <= x123 <= 2, start=0)
@variable(m, 0 <= x124 <= 2, start=0)
@variable(m, 0 <= x125 <= 2, start=0)
@variable(m, 0 <= x126 <= 2, start=0)
@variable(m, 0 <= x127 <= 2, start=0)
@variable(m, 0 <= x128 <= 2, start=0)
@variable(m, 0 <= x129 <= 2, start=0)
@variable(m, 0 <= x130 <= 2, start=0)
@variable(m, 0 <= x131 <= 2, start=0)
@variable(m, 0 <= x132 <= 2, start=0)
@variable(m, 0 <= x133 <= 2, start=0)
@variable(m, 0 <= x134 <= 2, start=0)
@variable(m, 0 <= x135 <= 2, start=0)
@variable(m, 0 <= x136 <= 2, start=0)
@variable(m, 0 <= x137 <= 2, start=0)
@variable(m, 0 <= x138 <= 2, start=0)
@variable(m, 0 <= x139 <= 2, start=0)
@variable(m, 0 <= x140 <= 2, start=0)
@variable(m, 0 <= x141 <= 2, start=0)
@variable(m, 0 <= x142 <= 2, start=0)
@variable(m, 0 <= x143 <= 2, start=0)
@variable(m, 0 <= x144 <= 2, start=0)
@variable(m, 0 <= x145 <= 2, start=0)
@variable(m, 0 <= x146 <= 2, start=0)
@variable(m, 0 <= x147 <= 2, start=0)
@variable(m, 0 <= x148 <= 2, start=0)
@variable(m, 0 <= x149 <= 2, start=0)
@variable(m, 0 <= x150 <= 2, start=0)
@variable(m, 0 <= x151 <= 2, start=0)
@variable(m, 0 <= x152 <= 2, start=0)
@variable(m, 0 <= x153 <= 2, start=0)
@variable(m, 0 <= x154 <= 2, start=0)
@variable(m, 0 <= x155 <= 2, start=0)
@variable(m, 0 <= x156 <= 2, start=0)
@variable(m, 0 <= x157 <= 2, start=0)
@variable(m, 0 <= x158 <= 2, start=0)
@variable(m, 0 <= x159 <= 2, start=0)
@variable(m, 0 <= x160 <= 2, start=0)
@variable(m, 0 <= x161 <= 2, start=0)
@variable(m, 0 <= x162 <= 2, start=0)
@variable(m, 0 <= x163 <= 2, start=0)
@variable(m, 0 <= x164 <= 2, start=0)
@variable(m, 0 <= x165 <= 2, start=0)
@variable(m, 0 <= x166 <= 2, start=0)
@variable(m, 0 <= x167 <= 2, start=0)
@variable(m, 0 <= x168 <= 2, start=0)
@variable(m, 0 <= x169 <= 2, start=0)
@variable(m, 0 <= x170 <= 2, start=0)
@variable(m, 0 <= x171 <= 2, start=0)
@variable(m, 0 <= x172 <= 2, start=0)
@variable(m, 0 <= x173 <= 2, start=0)
@variable(m, 0 <= x174 <= 2, start=0)
@variable(m, 0 <= x175 <= 2, start=0)
@variable(m, 0 <= x176 <= 2, start=0)
@variable(m, 0 <= x177 <= 2, start=0)
@variable(m, 0 <= x178 <= 2, start=0)
@variable(m, 0 <= x179 <= 2, start=0)
@variable(m, 0 <= x180 <= 2, start=0)
@variable(m, 0 <= x181 <= 2, start=0)
@variable(m, 0 <= x182 <= 2, start=0)
@variable(m, 0 <= x183 <= 2, start=0)
@variable(m, 0 <= x184 <= 2, start=0)
@variable(m, 0 <= x185 <= 2, start=0)
@variable(m, 0 <= x186 <= 2, start=0)
@variable(m, 0 <= x187 <= 2, start=0)
@variable(m, 0 <= x188 <= 2, start=0)
@variable(m, 0 <= x189 <= 2, start=0)
@variable(m, 0 <= x190 <= 2, start=0)
@variable(m, 0 <= x191 <= 2, start=0)
@variable(m, 0 <= x192 <= 2, start=0)
@variable(m, 0 <= x193 <= 2, start=0)
@variable(m, 0 <= x194 <= 2, start=0)
@variable(m, 0 <= x195 <= 2, start=0)
@variable(m, 0 <= x196 <= 2, start=0)
@variable(m, 0 <= x197 <= 2, start=0)
@variable(m, 0 <= x198 <= 2, start=0)
@variable(m, 0 <= x199 <= 2, start=0)
@variable(m, 0 <= x200 <= 2, start=0)
@variable(m, 0 <= x201 <= 2, start=0)
@variable(m, 0 <= x202 <= 2, start=0)
@variable(m, 0 <= x203 <= 2, start=0)
@variable(m, 0 <= x204 <= 2, start=0)
@variable(m, 0 <= x205 <= 2, start=0)
@variable(m, 0 <= x206 <= 2, start=0)
@variable(m, 0 <= x207 <= 2, start=0)
@variable(m, 0 <= x208 <= 2, start=0)
@variable(m, 0 <= x209 <= 2, start=0)
@variable(m, 0 <= x210 <= 2, start=0)
@variable(m, 0 <= x211 <= 2, start=0)
@variable(m, 0 <= x212 <= 2, start=0)
@variable(m, 0 <= x213 <= 2, start=0)
@variable(m, 0 <= x214 <= 2, start=0)
@variable(m, 0 <= x215 <= 2, start=0)
@variable(m, 0 <= x216 <= 2, start=0)
@variable(m, 0 <= x217 <= 2, start=0)
@variable(m, 0 <= x218 <= 2, start=0)
@variable(m, 0 <= x219 <= 2, start=0)
@variable(m, 0 <= x220 <= 2, start=0)
@variable(m, 0 <= x221 <= 2, start=0)
@variable(m, 0 <= x222 <= 2, start=0)
@variable(m, 0 <= x223 <= 2, start=0)
@variable(m, 0 <= x224 <= 2, start=0)
@variable(m, 0 <= x225 <= 2, start=0)
@variable(m, 0 <= x226 <= 2, start=0)
@variable(m, 0 <= x227 <= 2, start=0)
@variable(m, 0 <= x228 <= 2, start=0)
@variable(m, 0 <= x229 <= 2, start=0)
@variable(m, 0 <= x230 <= 2, start=0)
@variable(m, 0 <= x231 <= 2, start=0)
@variable(m, 0 <= x232 <= 2, start=0)
@variable(m, 0 <= x233 <= 2, start=0)
@variable(m, 0 <= x234 <= 2, start=0)
@variable(m, 0 <= x235 <= 2, start=0)
@variable(m, 0 <= x236 <= 2, start=0)
@variable(m, 0 <= x237 <= 2, start=0)
@variable(m, 0 <= x238 <= 2, start=0)
@variable(m, 0 <= x239 <= 2, start=0)
@variable(m, 0 <= x240 <= 2, start=0)
@variable(m, 0 <= x241 <= 2, start=0)
@variable(m, 0 <= x242 <= 2, start=0)
@variable(m, 0 <= x243 <= 2, start=0)
@variable(m, 0 <= x244 <= 2, start=0)
@variable(m, 0 <= x245 <= 2, start=0)
@variable(m, 0 <= x246 <= 2, start=0)
@variable(m, 0 <= x247 <= 2, start=0)
@variable(m, 0 <= x248 <= 2, start=0)
@variable(m, 0 <= x249 <= 2, start=0)
@variable(m, 0 <= x250 <= 2, start=0)
@variable(m, 0 <= x251 <= 2, start=0)
@variable(m, 0 <= x252 <= 2, start=0)
@variable(m, 0 <= x253 <= 2, start=0)
@variable(m, 0 <= x254 <= 2, start=0)
@variable(m, 0 <= x255 <= 2, start=0)
@variable(m, 0 <= x256 <= 2, start=0)
@variable(m, 0 <= x257 <= 2, start=0)
@variable(m, 0 <= x258 <= 2, start=0)
@variable(m, 0 <= x259 <= 2, start=0)
@variable(m, 0 <= x260 <= 2, start=0)
@variable(m, 0 <= x261 <= 2, start=0)
@variable(m, 0 <= x262 <= 2, start=0)
@variable(m, 0 <= x263 <= 2, start=0)
@variable(m, 0 <= x264 <= 2, start=0)
@variable(m, 0 <= x265 <= 2, start=0)
@variable(m, 0 <= x266 <= 2, start=0)
@variable(m, 0 <= x267 <= 2, start=0)
@variable(m, 0 <= x268 <= 2, start=0)
@variable(m, 0 <= x269 <= 2, start=0)
@variable(m, 0 <= x270 <= 2, start=0)
@variable(m, 0 <= x271 <= 2, start=0)
@variable(m, 0 <= x272 <= 2, start=0)
@variable(m, 0 <= x273 <= 2, start=0)
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

@NLconstraint(m, e1, -sqrt((x274 - x278)^2 + (x275 - x279)^2 + (x276 - x280)^2
    + (x277 - x281)^2) + x1 - 2 * b326 >= -2)
@NLconstraint(m, e2, -sqrt((x274 - x282)^2 + (x275 - x283)^2 + (x276 - x284)^2
    + (x277 - x285)^2) + x2 - 2 * b327 >= -2)
@NLconstraint(m, e3, -sqrt((x274 - x286)^2 + (x275 - x287)^2 + (x276 - x288)^2
    + (x277 - x289)^2) + x3 - 2 * b328 >= -2)
@NLconstraint(m, e4, -sqrt((x274 - x290)^2 + (x275 - x291)^2 + (x276 - x292)^2
    + (x277 - x293)^2) + x4 - 2 * b329 >= -2)
@NLconstraint(m, e5, -sqrt((x274 - x294)^2 + (x275 - x295)^2 + (x276 - x296)^2
    + (x277 - x297)^2) + x5 - 2 * b330 >= -2)
@NLconstraint(m, e6, -sqrt((x274 - x298)^2 + (x275 - x299)^2 + (x276 - x300)^2
    + (x277 - x301)^2) + x6 - 2 * b331 >= -2)
@NLconstraint(m, e7, -sqrt((x274 - x302)^2 + (x275 - x303)^2 + (x276 - x304)^2
    + (x277 - x305)^2) + x7 - 2 * b332 >= -2)
@NLconstraint(m, e8, -sqrt((x274 - x306)^2 + (x275 - x307)^2 + (x276 - x308)^2
    + (x277 - x309)^2) + x8 - 2 * b333 >= -2)
@NLconstraint(m, e9, -sqrt((x274 - x310)^2 + (x275 - x311)^2 + (x276 - x312)^2
    + (x277 - x313)^2) + x9 - 2 * b334 >= -2)
@NLconstraint(m, e10, -sqrt((x274 - x314)^2 + (x275 - x315)^2 + (x276 - x316)^2
    + (x277 - x317)^2) + x10 - 2 * b335 >= -2)
@NLconstraint(m, e11, -sqrt((x274 - x318)^2 + (x275 - x319)^2 + (x276 - x320)^2
    + (x277 - x321)^2) + x11 - 2 * b336 >= -2)
@NLconstraint(m, e12, -sqrt((x274 - x322)^2 + (x275 - x323)^2 + (x276 - x324)^2
    + (x277 - x325)^2) + x12 - 2 * b337 >= -2)
@NLconstraint(m, e13, -sqrt((x278 - x282)^2 + (x279 - x283)^2 + (x280 - x284)^2
    + (x281 - x285)^2) + x13 - 2 * b338 >= -2)
@NLconstraint(m, e14, -sqrt((x278 - x286)^2 + (x279 - x287)^2 + (x280 - x288)^2
    + (x281 - x289)^2) + x14 - 2 * b339 >= -2)
@NLconstraint(m, e15, -sqrt((x278 - x290)^2 + (x279 - x291)^2 + (x280 - x292)^2
    + (x281 - x293)^2) + x15 - 2 * b340 >= -2)
@NLconstraint(m, e16, -sqrt((x278 - x294)^2 + (x279 - x295)^2 + (x280 - x296)^2
    + (x281 - x297)^2) + x16 - 2 * b341 >= -2)
@NLconstraint(m, e17, -sqrt((x278 - x298)^2 + (x279 - x299)^2 + (x280 - x300)^2
    + (x281 - x301)^2) + x17 - 2 * b342 >= -2)
@NLconstraint(m, e18, -sqrt((x278 - x302)^2 + (x279 - x303)^2 + (x280 - x304)^2
    + (x281 - x305)^2) + x18 - 2 * b343 >= -2)
@NLconstraint(m, e19, -sqrt((x278 - x306)^2 + (x279 - x307)^2 + (x280 - x308)^2
    + (x281 - x309)^2) + x19 - 2 * b344 >= -2)
@NLconstraint(m, e20, -sqrt((x278 - x310)^2 + (x279 - x311)^2 + (x280 - x312)^2
    + (x281 - x313)^2) + x20 - 2 * b345 >= -2)
@NLconstraint(m, e21, -sqrt((x278 - x314)^2 + (x279 - x315)^2 + (x280 - x316)^2
    + (x281 - x317)^2) + x21 - 2 * b346 >= -2)
@NLconstraint(m, e22, -sqrt((x278 - x318)^2 + (x279 - x319)^2 + (x280 - x320)^2
    + (x281 - x321)^2) + x22 - 2 * b347 >= -2)
@NLconstraint(m, e23, -sqrt((x278 - x322)^2 + (x279 - x323)^2 + (x280 - x324)^2
    + (x281 - x325)^2) + x23 - 2 * b348 >= -2)
@NLconstraint(m, e24, -sqrt((x282 - x286)^2 + (x283 - x287)^2 + (x284 - x288)^2
    + (x285 - x289)^2) + x24 - 2 * b349 >= -2)
@NLconstraint(m, e25, -sqrt((x282 - x290)^2 + (x283 - x291)^2 + (x284 - x292)^2
    + (x285 - x293)^2) + x25 - 2 * b350 >= -2)
@NLconstraint(m, e26, -sqrt((x282 - x294)^2 + (x283 - x295)^2 + (x284 - x296)^2
    + (x285 - x297)^2) + x26 - 2 * b351 >= -2)
@NLconstraint(m, e27, -sqrt((x282 - x298)^2 + (x283 - x299)^2 + (x284 - x300)^2
    + (x285 - x301)^2) + x27 - 2 * b352 >= -2)
@NLconstraint(m, e28, -sqrt((x282 - x302)^2 + (x283 - x303)^2 + (x284 - x304)^2
    + (x285 - x305)^2) + x28 - 2 * b353 >= -2)
@NLconstraint(m, e29, -sqrt((x282 - x306)^2 + (x283 - x307)^2 + (x284 - x308)^2
    + (x285 - x309)^2) + x29 - 2 * b354 >= -2)
@NLconstraint(m, e30, -sqrt((x282 - x310)^2 + (x283 - x311)^2 + (x284 - x312)^2
    + (x285 - x313)^2) + x30 - 2 * b355 >= -2)
@NLconstraint(m, e31, -sqrt((x282 - x314)^2 + (x283 - x315)^2 + (x284 - x316)^2
    + (x285 - x317)^2) + x31 - 2 * b356 >= -2)
@NLconstraint(m, e32, -sqrt((x282 - x318)^2 + (x283 - x319)^2 + (x284 - x320)^2
    + (x285 - x321)^2) + x32 - 2 * b357 >= -2)
@NLconstraint(m, e33, -sqrt((x282 - x322)^2 + (x283 - x323)^2 + (x284 - x324)^2
    + (x285 - x325)^2) + x33 - 2 * b358 >= -2)
@NLconstraint(m, e34, -sqrt((x286 - x290)^2 + (x287 - x291)^2 + (x288 - x292)^2
    + (x289 - x293)^2) + x34 - 2 * b359 >= -2)
@NLconstraint(m, e35, -sqrt((x286 - x294)^2 + (x287 - x295)^2 + (x288 - x296)^2
    + (x289 - x297)^2) + x35 - 2 * b360 >= -2)
@NLconstraint(m, e36, -sqrt((x286 - x298)^2 + (x287 - x299)^2 + (x288 - x300)^2
    + (x289 - x301)^2) + x36 - 2 * b361 >= -2)
@NLconstraint(m, e37, -sqrt((x286 - x302)^2 + (x287 - x303)^2 + (x288 - x304)^2
    + (x289 - x305)^2) + x37 - 2 * b362 >= -2)
@NLconstraint(m, e38, -sqrt((x286 - x306)^2 + (x287 - x307)^2 + (x288 - x308)^2
    + (x289 - x309)^2) + x38 - 2 * b363 >= -2)
@NLconstraint(m, e39, -sqrt((x286 - x310)^2 + (x287 - x311)^2 + (x288 - x312)^2
    + (x289 - x313)^2) + x39 - 2 * b364 >= -2)
@NLconstraint(m, e40, -sqrt((x286 - x314)^2 + (x287 - x315)^2 + (x288 - x316)^2
    + (x289 - x317)^2) + x40 - 2 * b365 >= -2)
@NLconstraint(m, e41, -sqrt((x286 - x318)^2 + (x287 - x319)^2 + (x288 - x320)^2
    + (x289 - x321)^2) + x41 - 2 * b366 >= -2)
@NLconstraint(m, e42, -sqrt((x286 - x322)^2 + (x287 - x323)^2 + (x288 - x324)^2
    + (x289 - x325)^2) + x42 - 2 * b367 >= -2)
@NLconstraint(m, e43, -sqrt((x290 - x294)^2 + (x291 - x295)^2 + (x292 - x296)^2
    + (x293 - x297)^2) + x43 - 2 * b368 >= -2)
@NLconstraint(m, e44, -sqrt((x290 - x298)^2 + (x291 - x299)^2 + (x292 - x300)^2
    + (x293 - x301)^2) + x44 - 2 * b369 >= -2)
@NLconstraint(m, e45, -sqrt((x290 - x302)^2 + (x291 - x303)^2 + (x292 - x304)^2
    + (x293 - x305)^2) + x45 - 2 * b370 >= -2)
@NLconstraint(m, e46, -sqrt((x290 - x306)^2 + (x291 - x307)^2 + (x292 - x308)^2
    + (x293 - x309)^2) + x46 - 2 * b371 >= -2)
@NLconstraint(m, e47, -sqrt((x290 - x310)^2 + (x291 - x311)^2 + (x292 - x312)^2
    + (x293 - x313)^2) + x47 - 2 * b372 >= -2)
@NLconstraint(m, e48, -sqrt((x290 - x314)^2 + (x291 - x315)^2 + (x292 - x316)^2
    + (x293 - x317)^2) + x48 - 2 * b373 >= -2)
@NLconstraint(m, e49, -sqrt((x290 - x318)^2 + (x291 - x319)^2 + (x292 - x320)^2
    + (x293 - x321)^2) + x49 - 2 * b374 >= -2)
@NLconstraint(m, e50, -sqrt((x290 - x322)^2 + (x291 - x323)^2 + (x292 - x324)^2
    + (x293 - x325)^2) + x50 - 2 * b375 >= -2)
@NLconstraint(m, e51, -sqrt((x294 - x298)^2 + (x295 - x299)^2 + (x296 - x300)^2
    + (x297 - x301)^2) + x51 - 2 * b376 >= -2)
@NLconstraint(m, e52, -sqrt((x294 - x302)^2 + (x295 - x303)^2 + (x296 - x304)^2
    + (x297 - x305)^2) + x52 - 2 * b377 >= -2)
@NLconstraint(m, e53, -sqrt((x294 - x306)^2 + (x295 - x307)^2 + (x296 - x308)^2
    + (x297 - x309)^2) + x53 - 2 * b378 >= -2)
@NLconstraint(m, e54, -sqrt((x294 - x310)^2 + (x295 - x311)^2 + (x296 - x312)^2
    + (x297 - x313)^2) + x54 - 2 * b379 >= -2)
@NLconstraint(m, e55, -sqrt((x294 - x314)^2 + (x295 - x315)^2 + (x296 - x316)^2
    + (x297 - x317)^2) + x55 - 2 * b380 >= -2)
@NLconstraint(m, e56, -sqrt((x294 - x318)^2 + (x295 - x319)^2 + (x296 - x320)^2
    + (x297 - x321)^2) + x56 - 2 * b381 >= -2)
@NLconstraint(m, e57, -sqrt((x294 - x322)^2 + (x295 - x323)^2 + (x296 - x324)^2
    + (x297 - x325)^2) + x57 - 2 * b382 >= -2)
@NLconstraint(m, e58, -sqrt((x298 - x302)^2 + (x299 - x303)^2 + (x300 - x304)^2
    + (x301 - x305)^2) + x58 - 2 * b383 >= -2)
@NLconstraint(m, e59, -sqrt((x298 - x306)^2 + (x299 - x307)^2 + (x300 - x308)^2
    + (x301 - x309)^2) + x59 - 2 * b384 >= -2)
@NLconstraint(m, e60, -sqrt((x298 - x310)^2 + (x299 - x311)^2 + (x300 - x312)^2
    + (x301 - x313)^2) + x60 - 2 * b385 >= -2)
@NLconstraint(m, e61, -sqrt((x298 - x314)^2 + (x299 - x315)^2 + (x300 - x316)^2
    + (x301 - x317)^2) + x61 - 2 * b386 >= -2)
@NLconstraint(m, e62, -sqrt((x298 - x318)^2 + (x299 - x319)^2 + (x300 - x320)^2
    + (x301 - x321)^2) + x62 - 2 * b387 >= -2)
@NLconstraint(m, e63, -sqrt((x298 - x322)^2 + (x299 - x323)^2 + (x300 - x324)^2
    + (x301 - x325)^2) + x63 - 2 * b388 >= -2)
@NLconstraint(m, e64, -sqrt((x302 - x306)^2 + (x303 - x307)^2 + (x304 - x308)^2
    + (x305 - x309)^2) + x64 - 2 * b389 >= -2)
@NLconstraint(m, e65, -sqrt((x302 - x310)^2 + (x303 - x311)^2 + (x304 - x312)^2
    + (x305 - x313)^2) + x65 - 2 * b390 >= -2)
@NLconstraint(m, e66, -sqrt((x302 - x314)^2 + (x303 - x315)^2 + (x304 - x316)^2
    + (x305 - x317)^2) + x66 - 2 * b391 >= -2)
@NLconstraint(m, e67, -sqrt((x302 - x318)^2 + (x303 - x319)^2 + (x304 - x320)^2
    + (x305 - x321)^2) + x67 - 2 * b392 >= -2)
@NLconstraint(m, e68, -sqrt((x302 - x322)^2 + (x303 - x323)^2 + (x304 - x324)^2
    + (x305 - x325)^2) + x68 - 2 * b393 >= -2)
@NLconstraint(m, e69, -sqrt((x306 - x310)^2 + (x307 - x311)^2 + (x308 - x312)^2
    + (x309 - x313)^2) + x69 - 2 * b394 >= -2)
@NLconstraint(m, e70, -sqrt((x306 - x314)^2 + (x307 - x315)^2 + (x308 - x316)^2
    + (x309 - x317)^2) + x70 - 2 * b395 >= -2)
@NLconstraint(m, e71, -sqrt((x306 - x318)^2 + (x307 - x319)^2 + (x308 - x320)^2
    + (x309 - x321)^2) + x71 - 2 * b396 >= -2)
@NLconstraint(m, e72, -sqrt((x306 - x322)^2 + (x307 - x323)^2 + (x308 - x324)^2
    + (x309 - x325)^2) + x72 - 2 * b397 >= -2)
@NLconstraint(m, e73, -sqrt((x310 - x314)^2 + (x311 - x315)^2 + (x312 - x316)^2
    + (x313 - x317)^2) + x73 - 2 * b398 >= -2)
@NLconstraint(m, e74, -sqrt((x310 - x318)^2 + (x311 - x319)^2 + (x312 - x320)^2
    + (x313 - x321)^2) + x74 - 2 * b399 >= -2)
@NLconstraint(m, e75, -sqrt((x310 - x322)^2 + (x311 - x323)^2 + (x312 - x324)^2
    + (x313 - x325)^2) + x75 - 2 * b400 >= -2)
@NLconstraint(m, e76, -sqrt((x314 - x318)^2 + (x315 - x319)^2 + (x316 - x320)^2
    + (x317 - x321)^2) + x76 - 2 * b401 >= -2)
@NLconstraint(m, e77, -sqrt((x314 - x322)^2 + (x315 - x323)^2 + (x316 - x324)^2
    + (x317 - x325)^2) + x77 - 2 * b402 >= -2)
@NLconstraint(m, e78, -sqrt((x318 - x322)^2 + (x319 - x323)^2 + (x320 - x324)^2
    + (x321 - x325)^2) + x78 - 2 * b403 >= -2)
@NLconstraint(m, e79, -sqrt((-0.3078067547337774 + x274)^2 + (
    -0.5779578771750392 + x275)^2 + (-0.26561803541817575 + x276)^2 + (
    -0.8078960514329893 + x277)^2) + x79 - 2 * b404 >= -2)
@NLconstraint(m, e80, -sqrt((-0.4672172210012604 + x274)^2 + (
    -0.33251980673741144 + x275)^2 + (-0.8967525962082569 + x276)^2 + (
    -0.7924119898695275 + x277)^2) + x80 - 2 * b405 >= -2)
@NLconstraint(m, e81, -sqrt((-0.8596136949374525 + x274)^2 + (
    -0.6658137355569159 + x275)^2 + (-0.1854598161134392 + x276)^2 + (
    -0.3899285200718041 + x277)^2) + x81 - 2 * b406 >= -2)
@NLconstraint(m, e82, -sqrt((-0.23942936687819738 + x274)^2 + (
    -0.7931287877223899 + x275)^2 + (-0.009184110257544176 + x276)^2 + (
    -0.7905476817951573 + x277)^2) + x82 - 2 * b407 >= -2)
@NLconstraint(m, e83, -sqrt((-0.1667763675050825 + x274)^2 + (
    -0.30614199209589266 + x275)^2 + (-0.6286784916754126 + x276)^2 + (
    -0.6749145697726233 + x277)^2) + x83 - 2 * b408 >= -2)
@NLconstraint(m, e84, -sqrt((-0.5123965188595846 + x274)^2 + (
    -0.556215195448374 + x275)^2 + (-0.5888863209509851 + x276)^2 + (
    -0.6003058073162648 + x277)^2) + x84 - 2 * b409 >= -2)
@NLconstraint(m, e85, -sqrt((-0.10830095398871686 + x274)^2 + (
    -0.301870958131248 + x275)^2 + (-0.020499027923741364 + x276)^2 + (
    -0.5668022276384451 + x277)^2) + x85 - 2 * b410 >= -2)
@NLconstraint(m, e86, -sqrt((-0.29450295704025886 + x274)^2 + (
    -0.24215631594412912 + x275)^2 + (-0.2744568069724159 + x276)^2 + (
    -0.9412593709117075 + x277)^2) + x86 - 2 * b411 >= -2)
@NLconstraint(m, e87, -sqrt((-0.1282338254681593 + x274)^2 + (
    -0.9019460548181631 + x275)^2 + (-0.9031736614711603 + x276)^2 + (
    -0.2037984038273466 + x277)^2) + x87 - 2 * b412 >= -2)
@NLconstraint(m, e88, -sqrt((-0.829797266931312 + x274)^2 + (
    -0.19575994148177733 + x275)^2 + (-0.645872503285497 + x276)^2 + (
    -0.12203855440196454 + x277)^2) + x88 - 2 * b413 >= -2)
@NLconstraint(m, e89, -sqrt((-0.318405760895906 + x274)^2 + (
    -0.4938036901276964 + x275)^2 + (-0.37642068481077395 + x276)^2 + (
    -0.8256324717799948 + x277)^2) + x89 - 2 * b414 >= -2)
@NLconstraint(m, e90, -sqrt((-0.6465433247102469 + x274)^2 + (
    -0.033522650784374886 + x275)^2 + (-0.5581254938339517 + x276)^2 + (
    -0.0912916889874551 + x277)^2) + x90 - 2 * b415 >= -2)
@NLconstraint(m, e91, -sqrt((-0.17497888842654896 + x274)^2 + (
    -0.38968471952782524 + x275)^2 + (-0.3152812984667659 + x276)^2 + (
    -0.5561379670293034 + x277)^2) + x91 - 2 * b416 >= -2)
@NLconstraint(m, e92, -sqrt((-0.9831483568003972 + x274)^2 + (
    -0.7793186335882816 + x275)^2 + (-0.545443726285844 + x276)^2 + (
    -0.8394599012498352 + x277)^2) + x92 - 2 * b417 >= -2)
@NLconstraint(m, e93, -sqrt((-0.16871130717858907 + x274)^2 + (
    -0.7158922205435296 + x275)^2 + (-0.9716203470560987 + x276)^2 + (
    -0.9419601863446189 + x277)^2) + x93 - 2 * b418 >= -2)
@NLconstraint(m, e94, -sqrt((-0.3078067547337774 + x278)^2 + (
    -0.5779578771750392 + x279)^2 + (-0.26561803541817575 + x280)^2 + (
    -0.8078960514329893 + x281)^2) + x94 - 2 * b419 >= -2)
@NLconstraint(m, e95, -sqrt((-0.4672172210012604 + x278)^2 + (
    -0.33251980673741144 + x279)^2 + (-0.8967525962082569 + x280)^2 + (
    -0.7924119898695275 + x281)^2) + x95 - 2 * b420 >= -2)
@NLconstraint(m, e96, -sqrt((-0.8596136949374525 + x278)^2 + (
    -0.6658137355569159 + x279)^2 + (-0.1854598161134392 + x280)^2 + (
    -0.3899285200718041 + x281)^2) + x96 - 2 * b421 >= -2)
@NLconstraint(m, e97, -sqrt((-0.23942936687819738 + x278)^2 + (
    -0.7931287877223899 + x279)^2 + (-0.009184110257544176 + x280)^2 + (
    -0.7905476817951573 + x281)^2) + x97 - 2 * b422 >= -2)
@NLconstraint(m, e98, -sqrt((-0.1667763675050825 + x278)^2 + (
    -0.30614199209589266 + x279)^2 + (-0.6286784916754126 + x280)^2 + (
    -0.6749145697726233 + x281)^2) + x98 - 2 * b423 >= -2)
@NLconstraint(m, e99, -sqrt((-0.5123965188595846 + x278)^2 + (
    -0.556215195448374 + x279)^2 + (-0.5888863209509851 + x280)^2 + (
    -0.6003058073162648 + x281)^2) + x99 - 2 * b424 >= -2)
@NLconstraint(m, e100, -sqrt((-0.10830095398871686 + x278)^2 + (
    -0.301870958131248 + x279)^2 + (-0.020499027923741364 + x280)^2 + (
    -0.5668022276384451 + x281)^2) + x100 - 2 * b425 >= -2)
@NLconstraint(m, e101, -sqrt((-0.29450295704025886 + x278)^2 + (
    -0.24215631594412912 + x279)^2 + (-0.2744568069724159 + x280)^2 + (
    -0.9412593709117075 + x281)^2) + x101 - 2 * b426 >= -2)
@NLconstraint(m, e102, -sqrt((-0.1282338254681593 + x278)^2 + (
    -0.9019460548181631 + x279)^2 + (-0.9031736614711603 + x280)^2 + (
    -0.2037984038273466 + x281)^2) + x102 - 2 * b427 >= -2)
@NLconstraint(m, e103, -sqrt((-0.829797266931312 + x278)^2 + (
    -0.19575994148177733 + x279)^2 + (-0.645872503285497 + x280)^2 + (
    -0.12203855440196454 + x281)^2) + x103 - 2 * b428 >= -2)
@NLconstraint(m, e104, -sqrt((-0.318405760895906 + x278)^2 + (
    -0.4938036901276964 + x279)^2 + (-0.37642068481077395 + x280)^2 + (
    -0.8256324717799948 + x281)^2) + x104 - 2 * b429 >= -2)
@NLconstraint(m, e105, -sqrt((-0.6465433247102469 + x278)^2 + (
    -0.033522650784374886 + x279)^2 + (-0.5581254938339517 + x280)^2 + (
    -0.0912916889874551 + x281)^2) + x105 - 2 * b430 >= -2)
@NLconstraint(m, e106, -sqrt((-0.17497888842654896 + x278)^2 + (
    -0.38968471952782524 + x279)^2 + (-0.3152812984667659 + x280)^2 + (
    -0.5561379670293034 + x281)^2) + x106 - 2 * b431 >= -2)
@NLconstraint(m, e107, -sqrt((-0.9831483568003972 + x278)^2 + (
    -0.7793186335882816 + x279)^2 + (-0.545443726285844 + x280)^2 + (
    -0.8394599012498352 + x281)^2) + x107 - 2 * b432 >= -2)
@NLconstraint(m, e108, -sqrt((-0.16871130717858907 + x278)^2 + (
    -0.7158922205435296 + x279)^2 + (-0.9716203470560987 + x280)^2 + (
    -0.9419601863446189 + x281)^2) + x108 - 2 * b433 >= -2)
@NLconstraint(m, e109, -sqrt((-0.3078067547337774 + x282)^2 + (
    -0.5779578771750392 + x283)^2 + (-0.26561803541817575 + x284)^2 + (
    -0.8078960514329893 + x285)^2) + x109 - 2 * b434 >= -2)
@NLconstraint(m, e110, -sqrt((-0.4672172210012604 + x282)^2 + (
    -0.33251980673741144 + x283)^2 + (-0.8967525962082569 + x284)^2 + (
    -0.7924119898695275 + x285)^2) + x110 - 2 * b435 >= -2)
@NLconstraint(m, e111, -sqrt((-0.8596136949374525 + x282)^2 + (
    -0.6658137355569159 + x283)^2 + (-0.1854598161134392 + x284)^2 + (
    -0.3899285200718041 + x285)^2) + x111 - 2 * b436 >= -2)
@NLconstraint(m, e112, -sqrt((-0.23942936687819738 + x282)^2 + (
    -0.7931287877223899 + x283)^2 + (-0.009184110257544176 + x284)^2 + (
    -0.7905476817951573 + x285)^2) + x112 - 2 * b437 >= -2)
@NLconstraint(m, e113, -sqrt((-0.1667763675050825 + x282)^2 + (
    -0.30614199209589266 + x283)^2 + (-0.6286784916754126 + x284)^2 + (
    -0.6749145697726233 + x285)^2) + x113 - 2 * b438 >= -2)
@NLconstraint(m, e114, -sqrt((-0.5123965188595846 + x282)^2 + (
    -0.556215195448374 + x283)^2 + (-0.5888863209509851 + x284)^2 + (
    -0.6003058073162648 + x285)^2) + x114 - 2 * b439 >= -2)
@NLconstraint(m, e115, -sqrt((-0.10830095398871686 + x282)^2 + (
    -0.301870958131248 + x283)^2 + (-0.020499027923741364 + x284)^2 + (
    -0.5668022276384451 + x285)^2) + x115 - 2 * b440 >= -2)
@NLconstraint(m, e116, -sqrt((-0.29450295704025886 + x282)^2 + (
    -0.24215631594412912 + x283)^2 + (-0.2744568069724159 + x284)^2 + (
    -0.9412593709117075 + x285)^2) + x116 - 2 * b441 >= -2)
@NLconstraint(m, e117, -sqrt((-0.1282338254681593 + x282)^2 + (
    -0.9019460548181631 + x283)^2 + (-0.9031736614711603 + x284)^2 + (
    -0.2037984038273466 + x285)^2) + x117 - 2 * b442 >= -2)
@NLconstraint(m, e118, -sqrt((-0.829797266931312 + x282)^2 + (
    -0.19575994148177733 + x283)^2 + (-0.645872503285497 + x284)^2 + (
    -0.12203855440196454 + x285)^2) + x118 - 2 * b443 >= -2)
@NLconstraint(m, e119, -sqrt((-0.318405760895906 + x282)^2 + (
    -0.4938036901276964 + x283)^2 + (-0.37642068481077395 + x284)^2 + (
    -0.8256324717799948 + x285)^2) + x119 - 2 * b444 >= -2)
@NLconstraint(m, e120, -sqrt((-0.6465433247102469 + x282)^2 + (
    -0.033522650784374886 + x283)^2 + (-0.5581254938339517 + x284)^2 + (
    -0.0912916889874551 + x285)^2) + x120 - 2 * b445 >= -2)
@NLconstraint(m, e121, -sqrt((-0.17497888842654896 + x282)^2 + (
    -0.38968471952782524 + x283)^2 + (-0.3152812984667659 + x284)^2 + (
    -0.5561379670293034 + x285)^2) + x121 - 2 * b446 >= -2)
@NLconstraint(m, e122, -sqrt((-0.9831483568003972 + x282)^2 + (
    -0.7793186335882816 + x283)^2 + (-0.545443726285844 + x284)^2 + (
    -0.8394599012498352 + x285)^2) + x122 - 2 * b447 >= -2)
@NLconstraint(m, e123, -sqrt((-0.16871130717858907 + x282)^2 + (
    -0.7158922205435296 + x283)^2 + (-0.9716203470560987 + x284)^2 + (
    -0.9419601863446189 + x285)^2) + x123 - 2 * b448 >= -2)
@NLconstraint(m, e124, -sqrt((-0.3078067547337774 + x286)^2 + (
    -0.5779578771750392 + x287)^2 + (-0.26561803541817575 + x288)^2 + (
    -0.8078960514329893 + x289)^2) + x124 - 2 * b449 >= -2)
@NLconstraint(m, e125, -sqrt((-0.4672172210012604 + x286)^2 + (
    -0.33251980673741144 + x287)^2 + (-0.8967525962082569 + x288)^2 + (
    -0.7924119898695275 + x289)^2) + x125 - 2 * b450 >= -2)
@NLconstraint(m, e126, -sqrt((-0.8596136949374525 + x286)^2 + (
    -0.6658137355569159 + x287)^2 + (-0.1854598161134392 + x288)^2 + (
    -0.3899285200718041 + x289)^2) + x126 - 2 * b451 >= -2)
@NLconstraint(m, e127, -sqrt((-0.23942936687819738 + x286)^2 + (
    -0.7931287877223899 + x287)^2 + (-0.009184110257544176 + x288)^2 + (
    -0.7905476817951573 + x289)^2) + x127 - 2 * b452 >= -2)
@NLconstraint(m, e128, -sqrt((-0.1667763675050825 + x286)^2 + (
    -0.30614199209589266 + x287)^2 + (-0.6286784916754126 + x288)^2 + (
    -0.6749145697726233 + x289)^2) + x128 - 2 * b453 >= -2)
@NLconstraint(m, e129, -sqrt((-0.5123965188595846 + x286)^2 + (
    -0.556215195448374 + x287)^2 + (-0.5888863209509851 + x288)^2 + (
    -0.6003058073162648 + x289)^2) + x129 - 2 * b454 >= -2)
@NLconstraint(m, e130, -sqrt((-0.10830095398871686 + x286)^2 + (
    -0.301870958131248 + x287)^2 + (-0.020499027923741364 + x288)^2 + (
    -0.5668022276384451 + x289)^2) + x130 - 2 * b455 >= -2)
@NLconstraint(m, e131, -sqrt((-0.29450295704025886 + x286)^2 + (
    -0.24215631594412912 + x287)^2 + (-0.2744568069724159 + x288)^2 + (
    -0.9412593709117075 + x289)^2) + x131 - 2 * b456 >= -2)
@NLconstraint(m, e132, -sqrt((-0.1282338254681593 + x286)^2 + (
    -0.9019460548181631 + x287)^2 + (-0.9031736614711603 + x288)^2 + (
    -0.2037984038273466 + x289)^2) + x132 - 2 * b457 >= -2)
@NLconstraint(m, e133, -sqrt((-0.829797266931312 + x286)^2 + (
    -0.19575994148177733 + x287)^2 + (-0.645872503285497 + x288)^2 + (
    -0.12203855440196454 + x289)^2) + x133 - 2 * b458 >= -2)
@NLconstraint(m, e134, -sqrt((-0.318405760895906 + x286)^2 + (
    -0.4938036901276964 + x287)^2 + (-0.37642068481077395 + x288)^2 + (
    -0.8256324717799948 + x289)^2) + x134 - 2 * b459 >= -2)
@NLconstraint(m, e135, -sqrt((-0.6465433247102469 + x286)^2 + (
    -0.033522650784374886 + x287)^2 + (-0.5581254938339517 + x288)^2 + (
    -0.0912916889874551 + x289)^2) + x135 - 2 * b460 >= -2)
@NLconstraint(m, e136, -sqrt((-0.17497888842654896 + x286)^2 + (
    -0.38968471952782524 + x287)^2 + (-0.3152812984667659 + x288)^2 + (
    -0.5561379670293034 + x289)^2) + x136 - 2 * b461 >= -2)
@NLconstraint(m, e137, -sqrt((-0.9831483568003972 + x286)^2 + (
    -0.7793186335882816 + x287)^2 + (-0.545443726285844 + x288)^2 + (
    -0.8394599012498352 + x289)^2) + x137 - 2 * b462 >= -2)
@NLconstraint(m, e138, -sqrt((-0.16871130717858907 + x286)^2 + (
    -0.7158922205435296 + x287)^2 + (-0.9716203470560987 + x288)^2 + (
    -0.9419601863446189 + x289)^2) + x138 - 2 * b463 >= -2)
@NLconstraint(m, e139, -sqrt((-0.3078067547337774 + x290)^2 + (
    -0.5779578771750392 + x291)^2 + (-0.26561803541817575 + x292)^2 + (
    -0.8078960514329893 + x293)^2) + x139 - 2 * b464 >= -2)
@NLconstraint(m, e140, -sqrt((-0.4672172210012604 + x290)^2 + (
    -0.33251980673741144 + x291)^2 + (-0.8967525962082569 + x292)^2 + (
    -0.7924119898695275 + x293)^2) + x140 - 2 * b465 >= -2)
@NLconstraint(m, e141, -sqrt((-0.8596136949374525 + x290)^2 + (
    -0.6658137355569159 + x291)^2 + (-0.1854598161134392 + x292)^2 + (
    -0.3899285200718041 + x293)^2) + x141 - 2 * b466 >= -2)
@NLconstraint(m, e142, -sqrt((-0.23942936687819738 + x290)^2 + (
    -0.7931287877223899 + x291)^2 + (-0.009184110257544176 + x292)^2 + (
    -0.7905476817951573 + x293)^2) + x142 - 2 * b467 >= -2)
@NLconstraint(m, e143, -sqrt((-0.1667763675050825 + x290)^2 + (
    -0.30614199209589266 + x291)^2 + (-0.6286784916754126 + x292)^2 + (
    -0.6749145697726233 + x293)^2) + x143 - 2 * b468 >= -2)
@NLconstraint(m, e144, -sqrt((-0.5123965188595846 + x290)^2 + (
    -0.556215195448374 + x291)^2 + (-0.5888863209509851 + x292)^2 + (
    -0.6003058073162648 + x293)^2) + x144 - 2 * b469 >= -2)
@NLconstraint(m, e145, -sqrt((-0.10830095398871686 + x290)^2 + (
    -0.301870958131248 + x291)^2 + (-0.020499027923741364 + x292)^2 + (
    -0.5668022276384451 + x293)^2) + x145 - 2 * b470 >= -2)
@NLconstraint(m, e146, -sqrt((-0.29450295704025886 + x290)^2 + (
    -0.24215631594412912 + x291)^2 + (-0.2744568069724159 + x292)^2 + (
    -0.9412593709117075 + x293)^2) + x146 - 2 * b471 >= -2)
@NLconstraint(m, e147, -sqrt((-0.1282338254681593 + x290)^2 + (
    -0.9019460548181631 + x291)^2 + (-0.9031736614711603 + x292)^2 + (
    -0.2037984038273466 + x293)^2) + x147 - 2 * b472 >= -2)
@NLconstraint(m, e148, -sqrt((-0.829797266931312 + x290)^2 + (
    -0.19575994148177733 + x291)^2 + (-0.645872503285497 + x292)^2 + (
    -0.12203855440196454 + x293)^2) + x148 - 2 * b473 >= -2)
@NLconstraint(m, e149, -sqrt((-0.318405760895906 + x290)^2 + (
    -0.4938036901276964 + x291)^2 + (-0.37642068481077395 + x292)^2 + (
    -0.8256324717799948 + x293)^2) + x149 - 2 * b474 >= -2)
@NLconstraint(m, e150, -sqrt((-0.6465433247102469 + x290)^2 + (
    -0.033522650784374886 + x291)^2 + (-0.5581254938339517 + x292)^2 + (
    -0.0912916889874551 + x293)^2) + x150 - 2 * b475 >= -2)
@NLconstraint(m, e151, -sqrt((-0.17497888842654896 + x290)^2 + (
    -0.38968471952782524 + x291)^2 + (-0.3152812984667659 + x292)^2 + (
    -0.5561379670293034 + x293)^2) + x151 - 2 * b476 >= -2)
@NLconstraint(m, e152, -sqrt((-0.9831483568003972 + x290)^2 + (
    -0.7793186335882816 + x291)^2 + (-0.545443726285844 + x292)^2 + (
    -0.8394599012498352 + x293)^2) + x152 - 2 * b477 >= -2)
@NLconstraint(m, e153, -sqrt((-0.16871130717858907 + x290)^2 + (
    -0.7158922205435296 + x291)^2 + (-0.9716203470560987 + x292)^2 + (
    -0.9419601863446189 + x293)^2) + x153 - 2 * b478 >= -2)
@NLconstraint(m, e154, -sqrt((-0.3078067547337774 + x294)^2 + (
    -0.5779578771750392 + x295)^2 + (-0.26561803541817575 + x296)^2 + (
    -0.8078960514329893 + x297)^2) + x154 - 2 * b479 >= -2)
@NLconstraint(m, e155, -sqrt((-0.4672172210012604 + x294)^2 + (
    -0.33251980673741144 + x295)^2 + (-0.8967525962082569 + x296)^2 + (
    -0.7924119898695275 + x297)^2) + x155 - 2 * b480 >= -2)
@NLconstraint(m, e156, -sqrt((-0.8596136949374525 + x294)^2 + (
    -0.6658137355569159 + x295)^2 + (-0.1854598161134392 + x296)^2 + (
    -0.3899285200718041 + x297)^2) + x156 - 2 * b481 >= -2)
@NLconstraint(m, e157, -sqrt((-0.23942936687819738 + x294)^2 + (
    -0.7931287877223899 + x295)^2 + (-0.009184110257544176 + x296)^2 + (
    -0.7905476817951573 + x297)^2) + x157 - 2 * b482 >= -2)
@NLconstraint(m, e158, -sqrt((-0.1667763675050825 + x294)^2 + (
    -0.30614199209589266 + x295)^2 + (-0.6286784916754126 + x296)^2 + (
    -0.6749145697726233 + x297)^2) + x158 - 2 * b483 >= -2)
@NLconstraint(m, e159, -sqrt((-0.5123965188595846 + x294)^2 + (
    -0.556215195448374 + x295)^2 + (-0.5888863209509851 + x296)^2 + (
    -0.6003058073162648 + x297)^2) + x159 - 2 * b484 >= -2)
@NLconstraint(m, e160, -sqrt((-0.10830095398871686 + x294)^2 + (
    -0.301870958131248 + x295)^2 + (-0.020499027923741364 + x296)^2 + (
    -0.5668022276384451 + x297)^2) + x160 - 2 * b485 >= -2)
@NLconstraint(m, e161, -sqrt((-0.29450295704025886 + x294)^2 + (
    -0.24215631594412912 + x295)^2 + (-0.2744568069724159 + x296)^2 + (
    -0.9412593709117075 + x297)^2) + x161 - 2 * b486 >= -2)
@NLconstraint(m, e162, -sqrt((-0.1282338254681593 + x294)^2 + (
    -0.9019460548181631 + x295)^2 + (-0.9031736614711603 + x296)^2 + (
    -0.2037984038273466 + x297)^2) + x162 - 2 * b487 >= -2)
@NLconstraint(m, e163, -sqrt((-0.829797266931312 + x294)^2 + (
    -0.19575994148177733 + x295)^2 + (-0.645872503285497 + x296)^2 + (
    -0.12203855440196454 + x297)^2) + x163 - 2 * b488 >= -2)
@NLconstraint(m, e164, -sqrt((-0.318405760895906 + x294)^2 + (
    -0.4938036901276964 + x295)^2 + (-0.37642068481077395 + x296)^2 + (
    -0.8256324717799948 + x297)^2) + x164 - 2 * b489 >= -2)
@NLconstraint(m, e165, -sqrt((-0.6465433247102469 + x294)^2 + (
    -0.033522650784374886 + x295)^2 + (-0.5581254938339517 + x296)^2 + (
    -0.0912916889874551 + x297)^2) + x165 - 2 * b490 >= -2)
@NLconstraint(m, e166, -sqrt((-0.17497888842654896 + x294)^2 + (
    -0.38968471952782524 + x295)^2 + (-0.3152812984667659 + x296)^2 + (
    -0.5561379670293034 + x297)^2) + x166 - 2 * b491 >= -2)
@NLconstraint(m, e167, -sqrt((-0.9831483568003972 + x294)^2 + (
    -0.7793186335882816 + x295)^2 + (-0.545443726285844 + x296)^2 + (
    -0.8394599012498352 + x297)^2) + x167 - 2 * b492 >= -2)
@NLconstraint(m, e168, -sqrt((-0.16871130717858907 + x294)^2 + (
    -0.7158922205435296 + x295)^2 + (-0.9716203470560987 + x296)^2 + (
    -0.9419601863446189 + x297)^2) + x168 - 2 * b493 >= -2)
@NLconstraint(m, e169, -sqrt((-0.3078067547337774 + x298)^2 + (
    -0.5779578771750392 + x299)^2 + (-0.26561803541817575 + x300)^2 + (
    -0.8078960514329893 + x301)^2) + x169 - 2 * b494 >= -2)
@NLconstraint(m, e170, -sqrt((-0.4672172210012604 + x298)^2 + (
    -0.33251980673741144 + x299)^2 + (-0.8967525962082569 + x300)^2 + (
    -0.7924119898695275 + x301)^2) + x170 - 2 * b495 >= -2)
@NLconstraint(m, e171, -sqrt((-0.8596136949374525 + x298)^2 + (
    -0.6658137355569159 + x299)^2 + (-0.1854598161134392 + x300)^2 + (
    -0.3899285200718041 + x301)^2) + x171 - 2 * b496 >= -2)
@NLconstraint(m, e172, -sqrt((-0.23942936687819738 + x298)^2 + (
    -0.7931287877223899 + x299)^2 + (-0.009184110257544176 + x300)^2 + (
    -0.7905476817951573 + x301)^2) + x172 - 2 * b497 >= -2)
@NLconstraint(m, e173, -sqrt((-0.1667763675050825 + x298)^2 + (
    -0.30614199209589266 + x299)^2 + (-0.6286784916754126 + x300)^2 + (
    -0.6749145697726233 + x301)^2) + x173 - 2 * b498 >= -2)
@NLconstraint(m, e174, -sqrt((-0.5123965188595846 + x298)^2 + (
    -0.556215195448374 + x299)^2 + (-0.5888863209509851 + x300)^2 + (
    -0.6003058073162648 + x301)^2) + x174 - 2 * b499 >= -2)
@NLconstraint(m, e175, -sqrt((-0.10830095398871686 + x298)^2 + (
    -0.301870958131248 + x299)^2 + (-0.020499027923741364 + x300)^2 + (
    -0.5668022276384451 + x301)^2) + x175 - 2 * b500 >= -2)
@NLconstraint(m, e176, -sqrt((-0.29450295704025886 + x298)^2 + (
    -0.24215631594412912 + x299)^2 + (-0.2744568069724159 + x300)^2 + (
    -0.9412593709117075 + x301)^2) + x176 - 2 * b501 >= -2)
@NLconstraint(m, e177, -sqrt((-0.1282338254681593 + x298)^2 + (
    -0.9019460548181631 + x299)^2 + (-0.9031736614711603 + x300)^2 + (
    -0.2037984038273466 + x301)^2) + x177 - 2 * b502 >= -2)
@NLconstraint(m, e178, -sqrt((-0.829797266931312 + x298)^2 + (
    -0.19575994148177733 + x299)^2 + (-0.645872503285497 + x300)^2 + (
    -0.12203855440196454 + x301)^2) + x178 - 2 * b503 >= -2)
@NLconstraint(m, e179, -sqrt((-0.318405760895906 + x298)^2 + (
    -0.4938036901276964 + x299)^2 + (-0.37642068481077395 + x300)^2 + (
    -0.8256324717799948 + x301)^2) + x179 - 2 * b504 >= -2)
@NLconstraint(m, e180, -sqrt((-0.6465433247102469 + x298)^2 + (
    -0.033522650784374886 + x299)^2 + (-0.5581254938339517 + x300)^2 + (
    -0.0912916889874551 + x301)^2) + x180 - 2 * b505 >= -2)
@NLconstraint(m, e181, -sqrt((-0.17497888842654896 + x298)^2 + (
    -0.38968471952782524 + x299)^2 + (-0.3152812984667659 + x300)^2 + (
    -0.5561379670293034 + x301)^2) + x181 - 2 * b506 >= -2)
@NLconstraint(m, e182, -sqrt((-0.9831483568003972 + x298)^2 + (
    -0.7793186335882816 + x299)^2 + (-0.545443726285844 + x300)^2 + (
    -0.8394599012498352 + x301)^2) + x182 - 2 * b507 >= -2)
@NLconstraint(m, e183, -sqrt((-0.16871130717858907 + x298)^2 + (
    -0.7158922205435296 + x299)^2 + (-0.9716203470560987 + x300)^2 + (
    -0.9419601863446189 + x301)^2) + x183 - 2 * b508 >= -2)
@NLconstraint(m, e184, -sqrt((-0.3078067547337774 + x302)^2 + (
    -0.5779578771750392 + x303)^2 + (-0.26561803541817575 + x304)^2 + (
    -0.8078960514329893 + x305)^2) + x184 - 2 * b509 >= -2)
@NLconstraint(m, e185, -sqrt((-0.4672172210012604 + x302)^2 + (
    -0.33251980673741144 + x303)^2 + (-0.8967525962082569 + x304)^2 + (
    -0.7924119898695275 + x305)^2) + x185 - 2 * b510 >= -2)
@NLconstraint(m, e186, -sqrt((-0.8596136949374525 + x302)^2 + (
    -0.6658137355569159 + x303)^2 + (-0.1854598161134392 + x304)^2 + (
    -0.3899285200718041 + x305)^2) + x186 - 2 * b511 >= -2)
@NLconstraint(m, e187, -sqrt((-0.23942936687819738 + x302)^2 + (
    -0.7931287877223899 + x303)^2 + (-0.009184110257544176 + x304)^2 + (
    -0.7905476817951573 + x305)^2) + x187 - 2 * b512 >= -2)
@NLconstraint(m, e188, -sqrt((-0.1667763675050825 + x302)^2 + (
    -0.30614199209589266 + x303)^2 + (-0.6286784916754126 + x304)^2 + (
    -0.6749145697726233 + x305)^2) + x188 - 2 * b513 >= -2)
@NLconstraint(m, e189, -sqrt((-0.5123965188595846 + x302)^2 + (
    -0.556215195448374 + x303)^2 + (-0.5888863209509851 + x304)^2 + (
    -0.6003058073162648 + x305)^2) + x189 - 2 * b514 >= -2)
@NLconstraint(m, e190, -sqrt((-0.10830095398871686 + x302)^2 + (
    -0.301870958131248 + x303)^2 + (-0.020499027923741364 + x304)^2 + (
    -0.5668022276384451 + x305)^2) + x190 - 2 * b515 >= -2)
@NLconstraint(m, e191, -sqrt((-0.29450295704025886 + x302)^2 + (
    -0.24215631594412912 + x303)^2 + (-0.2744568069724159 + x304)^2 + (
    -0.9412593709117075 + x305)^2) + x191 - 2 * b516 >= -2)
@NLconstraint(m, e192, -sqrt((-0.1282338254681593 + x302)^2 + (
    -0.9019460548181631 + x303)^2 + (-0.9031736614711603 + x304)^2 + (
    -0.2037984038273466 + x305)^2) + x192 - 2 * b517 >= -2)
@NLconstraint(m, e193, -sqrt((-0.829797266931312 + x302)^2 + (
    -0.19575994148177733 + x303)^2 + (-0.645872503285497 + x304)^2 + (
    -0.12203855440196454 + x305)^2) + x193 - 2 * b518 >= -2)
@NLconstraint(m, e194, -sqrt((-0.318405760895906 + x302)^2 + (
    -0.4938036901276964 + x303)^2 + (-0.37642068481077395 + x304)^2 + (
    -0.8256324717799948 + x305)^2) + x194 - 2 * b519 >= -2)
@NLconstraint(m, e195, -sqrt((-0.6465433247102469 + x302)^2 + (
    -0.033522650784374886 + x303)^2 + (-0.5581254938339517 + x304)^2 + (
    -0.0912916889874551 + x305)^2) + x195 - 2 * b520 >= -2)
@NLconstraint(m, e196, -sqrt((-0.17497888842654896 + x302)^2 + (
    -0.38968471952782524 + x303)^2 + (-0.3152812984667659 + x304)^2 + (
    -0.5561379670293034 + x305)^2) + x196 - 2 * b521 >= -2)
@NLconstraint(m, e197, -sqrt((-0.9831483568003972 + x302)^2 + (
    -0.7793186335882816 + x303)^2 + (-0.545443726285844 + x304)^2 + (
    -0.8394599012498352 + x305)^2) + x197 - 2 * b522 >= -2)
@NLconstraint(m, e198, -sqrt((-0.16871130717858907 + x302)^2 + (
    -0.7158922205435296 + x303)^2 + (-0.9716203470560987 + x304)^2 + (
    -0.9419601863446189 + x305)^2) + x198 - 2 * b523 >= -2)
@NLconstraint(m, e199, -sqrt((-0.3078067547337774 + x306)^2 + (
    -0.5779578771750392 + x307)^2 + (-0.26561803541817575 + x308)^2 + (
    -0.8078960514329893 + x309)^2) + x199 - 2 * b524 >= -2)
@NLconstraint(m, e200, -sqrt((-0.4672172210012604 + x306)^2 + (
    -0.33251980673741144 + x307)^2 + (-0.8967525962082569 + x308)^2 + (
    -0.7924119898695275 + x309)^2) + x200 - 2 * b525 >= -2)
@NLconstraint(m, e201, -sqrt((-0.8596136949374525 + x306)^2 + (
    -0.6658137355569159 + x307)^2 + (-0.1854598161134392 + x308)^2 + (
    -0.3899285200718041 + x309)^2) + x201 - 2 * b526 >= -2)
@NLconstraint(m, e202, -sqrt((-0.23942936687819738 + x306)^2 + (
    -0.7931287877223899 + x307)^2 + (-0.009184110257544176 + x308)^2 + (
    -0.7905476817951573 + x309)^2) + x202 - 2 * b527 >= -2)
@NLconstraint(m, e203, -sqrt((-0.1667763675050825 + x306)^2 + (
    -0.30614199209589266 + x307)^2 + (-0.6286784916754126 + x308)^2 + (
    -0.6749145697726233 + x309)^2) + x203 - 2 * b528 >= -2)
@NLconstraint(m, e204, -sqrt((-0.5123965188595846 + x306)^2 + (
    -0.556215195448374 + x307)^2 + (-0.5888863209509851 + x308)^2 + (
    -0.6003058073162648 + x309)^2) + x204 - 2 * b529 >= -2)
@NLconstraint(m, e205, -sqrt((-0.10830095398871686 + x306)^2 + (
    -0.301870958131248 + x307)^2 + (-0.020499027923741364 + x308)^2 + (
    -0.5668022276384451 + x309)^2) + x205 - 2 * b530 >= -2)
@NLconstraint(m, e206, -sqrt((-0.29450295704025886 + x306)^2 + (
    -0.24215631594412912 + x307)^2 + (-0.2744568069724159 + x308)^2 + (
    -0.9412593709117075 + x309)^2) + x206 - 2 * b531 >= -2)
@NLconstraint(m, e207, -sqrt((-0.1282338254681593 + x306)^2 + (
    -0.9019460548181631 + x307)^2 + (-0.9031736614711603 + x308)^2 + (
    -0.2037984038273466 + x309)^2) + x207 - 2 * b532 >= -2)
@NLconstraint(m, e208, -sqrt((-0.829797266931312 + x306)^2 + (
    -0.19575994148177733 + x307)^2 + (-0.645872503285497 + x308)^2 + (
    -0.12203855440196454 + x309)^2) + x208 - 2 * b533 >= -2)
@NLconstraint(m, e209, -sqrt((-0.318405760895906 + x306)^2 + (
    -0.4938036901276964 + x307)^2 + (-0.37642068481077395 + x308)^2 + (
    -0.8256324717799948 + x309)^2) + x209 - 2 * b534 >= -2)
@NLconstraint(m, e210, -sqrt((-0.6465433247102469 + x306)^2 + (
    -0.033522650784374886 + x307)^2 + (-0.5581254938339517 + x308)^2 + (
    -0.0912916889874551 + x309)^2) + x210 - 2 * b535 >= -2)
@NLconstraint(m, e211, -sqrt((-0.17497888842654896 + x306)^2 + (
    -0.38968471952782524 + x307)^2 + (-0.3152812984667659 + x308)^2 + (
    -0.5561379670293034 + x309)^2) + x211 - 2 * b536 >= -2)
@NLconstraint(m, e212, -sqrt((-0.9831483568003972 + x306)^2 + (
    -0.7793186335882816 + x307)^2 + (-0.545443726285844 + x308)^2 + (
    -0.8394599012498352 + x309)^2) + x212 - 2 * b537 >= -2)
@NLconstraint(m, e213, -sqrt((-0.16871130717858907 + x306)^2 + (
    -0.7158922205435296 + x307)^2 + (-0.9716203470560987 + x308)^2 + (
    -0.9419601863446189 + x309)^2) + x213 - 2 * b538 >= -2)
@NLconstraint(m, e214, -sqrt((-0.3078067547337774 + x310)^2 + (
    -0.5779578771750392 + x311)^2 + (-0.26561803541817575 + x312)^2 + (
    -0.8078960514329893 + x313)^2) + x214 - 2 * b539 >= -2)
@NLconstraint(m, e215, -sqrt((-0.4672172210012604 + x310)^2 + (
    -0.33251980673741144 + x311)^2 + (-0.8967525962082569 + x312)^2 + (
    -0.7924119898695275 + x313)^2) + x215 - 2 * b540 >= -2)
@NLconstraint(m, e216, -sqrt((-0.8596136949374525 + x310)^2 + (
    -0.6658137355569159 + x311)^2 + (-0.1854598161134392 + x312)^2 + (
    -0.3899285200718041 + x313)^2) + x216 - 2 * b541 >= -2)
@NLconstraint(m, e217, -sqrt((-0.23942936687819738 + x310)^2 + (
    -0.7931287877223899 + x311)^2 + (-0.009184110257544176 + x312)^2 + (
    -0.7905476817951573 + x313)^2) + x217 - 2 * b542 >= -2)
@NLconstraint(m, e218, -sqrt((-0.1667763675050825 + x310)^2 + (
    -0.30614199209589266 + x311)^2 + (-0.6286784916754126 + x312)^2 + (
    -0.6749145697726233 + x313)^2) + x218 - 2 * b543 >= -2)
@NLconstraint(m, e219, -sqrt((-0.5123965188595846 + x310)^2 + (
    -0.556215195448374 + x311)^2 + (-0.5888863209509851 + x312)^2 + (
    -0.6003058073162648 + x313)^2) + x219 - 2 * b544 >= -2)
@NLconstraint(m, e220, -sqrt((-0.10830095398871686 + x310)^2 + (
    -0.301870958131248 + x311)^2 + (-0.020499027923741364 + x312)^2 + (
    -0.5668022276384451 + x313)^2) + x220 - 2 * b545 >= -2)
@NLconstraint(m, e221, -sqrt((-0.29450295704025886 + x310)^2 + (
    -0.24215631594412912 + x311)^2 + (-0.2744568069724159 + x312)^2 + (
    -0.9412593709117075 + x313)^2) + x221 - 2 * b546 >= -2)
@NLconstraint(m, e222, -sqrt((-0.1282338254681593 + x310)^2 + (
    -0.9019460548181631 + x311)^2 + (-0.9031736614711603 + x312)^2 + (
    -0.2037984038273466 + x313)^2) + x222 - 2 * b547 >= -2)
@NLconstraint(m, e223, -sqrt((-0.829797266931312 + x310)^2 + (
    -0.19575994148177733 + x311)^2 + (-0.645872503285497 + x312)^2 + (
    -0.12203855440196454 + x313)^2) + x223 - 2 * b548 >= -2)
@NLconstraint(m, e224, -sqrt((-0.318405760895906 + x310)^2 + (
    -0.4938036901276964 + x311)^2 + (-0.37642068481077395 + x312)^2 + (
    -0.8256324717799948 + x313)^2) + x224 - 2 * b549 >= -2)
@NLconstraint(m, e225, -sqrt((-0.6465433247102469 + x310)^2 + (
    -0.033522650784374886 + x311)^2 + (-0.5581254938339517 + x312)^2 + (
    -0.0912916889874551 + x313)^2) + x225 - 2 * b550 >= -2)
@NLconstraint(m, e226, -sqrt((-0.17497888842654896 + x310)^2 + (
    -0.38968471952782524 + x311)^2 + (-0.3152812984667659 + x312)^2 + (
    -0.5561379670293034 + x313)^2) + x226 - 2 * b551 >= -2)
@NLconstraint(m, e227, -sqrt((-0.9831483568003972 + x310)^2 + (
    -0.7793186335882816 + x311)^2 + (-0.545443726285844 + x312)^2 + (
    -0.8394599012498352 + x313)^2) + x227 - 2 * b552 >= -2)
@NLconstraint(m, e228, -sqrt((-0.16871130717858907 + x310)^2 + (
    -0.7158922205435296 + x311)^2 + (-0.9716203470560987 + x312)^2 + (
    -0.9419601863446189 + x313)^2) + x228 - 2 * b553 >= -2)
@NLconstraint(m, e229, -sqrt((-0.3078067547337774 + x314)^2 + (
    -0.5779578771750392 + x315)^2 + (-0.26561803541817575 + x316)^2 + (
    -0.8078960514329893 + x317)^2) + x229 - 2 * b554 >= -2)
@NLconstraint(m, e230, -sqrt((-0.4672172210012604 + x314)^2 + (
    -0.33251980673741144 + x315)^2 + (-0.8967525962082569 + x316)^2 + (
    -0.7924119898695275 + x317)^2) + x230 - 2 * b555 >= -2)
@NLconstraint(m, e231, -sqrt((-0.8596136949374525 + x314)^2 + (
    -0.6658137355569159 + x315)^2 + (-0.1854598161134392 + x316)^2 + (
    -0.3899285200718041 + x317)^2) + x231 - 2 * b556 >= -2)
@NLconstraint(m, e232, -sqrt((-0.23942936687819738 + x314)^2 + (
    -0.7931287877223899 + x315)^2 + (-0.009184110257544176 + x316)^2 + (
    -0.7905476817951573 + x317)^2) + x232 - 2 * b557 >= -2)
@NLconstraint(m, e233, -sqrt((-0.1667763675050825 + x314)^2 + (
    -0.30614199209589266 + x315)^2 + (-0.6286784916754126 + x316)^2 + (
    -0.6749145697726233 + x317)^2) + x233 - 2 * b558 >= -2)
@NLconstraint(m, e234, -sqrt((-0.5123965188595846 + x314)^2 + (
    -0.556215195448374 + x315)^2 + (-0.5888863209509851 + x316)^2 + (
    -0.6003058073162648 + x317)^2) + x234 - 2 * b559 >= -2)
@NLconstraint(m, e235, -sqrt((-0.10830095398871686 + x314)^2 + (
    -0.301870958131248 + x315)^2 + (-0.020499027923741364 + x316)^2 + (
    -0.5668022276384451 + x317)^2) + x235 - 2 * b560 >= -2)
@NLconstraint(m, e236, -sqrt((-0.29450295704025886 + x314)^2 + (
    -0.24215631594412912 + x315)^2 + (-0.2744568069724159 + x316)^2 + (
    -0.9412593709117075 + x317)^2) + x236 - 2 * b561 >= -2)
@NLconstraint(m, e237, -sqrt((-0.1282338254681593 + x314)^2 + (
    -0.9019460548181631 + x315)^2 + (-0.9031736614711603 + x316)^2 + (
    -0.2037984038273466 + x317)^2) + x237 - 2 * b562 >= -2)
@NLconstraint(m, e238, -sqrt((-0.829797266931312 + x314)^2 + (
    -0.19575994148177733 + x315)^2 + (-0.645872503285497 + x316)^2 + (
    -0.12203855440196454 + x317)^2) + x238 - 2 * b563 >= -2)
@NLconstraint(m, e239, -sqrt((-0.318405760895906 + x314)^2 + (
    -0.4938036901276964 + x315)^2 + (-0.37642068481077395 + x316)^2 + (
    -0.8256324717799948 + x317)^2) + x239 - 2 * b564 >= -2)
@NLconstraint(m, e240, -sqrt((-0.6465433247102469 + x314)^2 + (
    -0.033522650784374886 + x315)^2 + (-0.5581254938339517 + x316)^2 + (
    -0.0912916889874551 + x317)^2) + x240 - 2 * b565 >= -2)
@NLconstraint(m, e241, -sqrt((-0.17497888842654896 + x314)^2 + (
    -0.38968471952782524 + x315)^2 + (-0.3152812984667659 + x316)^2 + (
    -0.5561379670293034 + x317)^2) + x241 - 2 * b566 >= -2)
@NLconstraint(m, e242, -sqrt((-0.9831483568003972 + x314)^2 + (
    -0.7793186335882816 + x315)^2 + (-0.545443726285844 + x316)^2 + (
    -0.8394599012498352 + x317)^2) + x242 - 2 * b567 >= -2)
@NLconstraint(m, e243, -sqrt((-0.16871130717858907 + x314)^2 + (
    -0.7158922205435296 + x315)^2 + (-0.9716203470560987 + x316)^2 + (
    -0.9419601863446189 + x317)^2) + x243 - 2 * b568 >= -2)
@NLconstraint(m, e244, -sqrt((-0.3078067547337774 + x318)^2 + (
    -0.5779578771750392 + x319)^2 + (-0.26561803541817575 + x320)^2 + (
    -0.8078960514329893 + x321)^2) + x244 - 2 * b569 >= -2)
@NLconstraint(m, e245, -sqrt((-0.4672172210012604 + x318)^2 + (
    -0.33251980673741144 + x319)^2 + (-0.8967525962082569 + x320)^2 + (
    -0.7924119898695275 + x321)^2) + x245 - 2 * b570 >= -2)
@NLconstraint(m, e246, -sqrt((-0.8596136949374525 + x318)^2 + (
    -0.6658137355569159 + x319)^2 + (-0.1854598161134392 + x320)^2 + (
    -0.3899285200718041 + x321)^2) + x246 - 2 * b571 >= -2)
@NLconstraint(m, e247, -sqrt((-0.23942936687819738 + x318)^2 + (
    -0.7931287877223899 + x319)^2 + (-0.009184110257544176 + x320)^2 + (
    -0.7905476817951573 + x321)^2) + x247 - 2 * b572 >= -2)
@NLconstraint(m, e248, -sqrt((-0.1667763675050825 + x318)^2 + (
    -0.30614199209589266 + x319)^2 + (-0.6286784916754126 + x320)^2 + (
    -0.6749145697726233 + x321)^2) + x248 - 2 * b573 >= -2)
@NLconstraint(m, e249, -sqrt((-0.5123965188595846 + x318)^2 + (
    -0.556215195448374 + x319)^2 + (-0.5888863209509851 + x320)^2 + (
    -0.6003058073162648 + x321)^2) + x249 - 2 * b574 >= -2)
@NLconstraint(m, e250, -sqrt((-0.10830095398871686 + x318)^2 + (
    -0.301870958131248 + x319)^2 + (-0.020499027923741364 + x320)^2 + (
    -0.5668022276384451 + x321)^2) + x250 - 2 * b575 >= -2)
@NLconstraint(m, e251, -sqrt((-0.29450295704025886 + x318)^2 + (
    -0.24215631594412912 + x319)^2 + (-0.2744568069724159 + x320)^2 + (
    -0.9412593709117075 + x321)^2) + x251 - 2 * b576 >= -2)
@NLconstraint(m, e252, -sqrt((-0.1282338254681593 + x318)^2 + (
    -0.9019460548181631 + x319)^2 + (-0.9031736614711603 + x320)^2 + (
    -0.2037984038273466 + x321)^2) + x252 - 2 * b577 >= -2)
@NLconstraint(m, e253, -sqrt((-0.829797266931312 + x318)^2 + (
    -0.19575994148177733 + x319)^2 + (-0.645872503285497 + x320)^2 + (
    -0.12203855440196454 + x321)^2) + x253 - 2 * b578 >= -2)
@NLconstraint(m, e254, -sqrt((-0.318405760895906 + x318)^2 + (
    -0.4938036901276964 + x319)^2 + (-0.37642068481077395 + x320)^2 + (
    -0.8256324717799948 + x321)^2) + x254 - 2 * b579 >= -2)
@NLconstraint(m, e255, -sqrt((-0.6465433247102469 + x318)^2 + (
    -0.033522650784374886 + x319)^2 + (-0.5581254938339517 + x320)^2 + (
    -0.0912916889874551 + x321)^2) + x255 - 2 * b580 >= -2)
@NLconstraint(m, e256, -sqrt((-0.17497888842654896 + x318)^2 + (
    -0.38968471952782524 + x319)^2 + (-0.3152812984667659 + x320)^2 + (
    -0.5561379670293034 + x321)^2) + x256 - 2 * b581 >= -2)
@NLconstraint(m, e257, -sqrt((-0.9831483568003972 + x318)^2 + (
    -0.7793186335882816 + x319)^2 + (-0.545443726285844 + x320)^2 + (
    -0.8394599012498352 + x321)^2) + x257 - 2 * b582 >= -2)
@NLconstraint(m, e258, -sqrt((-0.16871130717858907 + x318)^2 + (
    -0.7158922205435296 + x319)^2 + (-0.9716203470560987 + x320)^2 + (
    -0.9419601863446189 + x321)^2) + x258 - 2 * b583 >= -2)
@NLconstraint(m, e259, -sqrt((-0.3078067547337774 + x322)^2 + (
    -0.5779578771750392 + x323)^2 + (-0.26561803541817575 + x324)^2 + (
    -0.8078960514329893 + x325)^2) + x259 - 2 * b584 >= -2)
@NLconstraint(m, e260, -sqrt((-0.4672172210012604 + x322)^2 + (
    -0.33251980673741144 + x323)^2 + (-0.8967525962082569 + x324)^2 + (
    -0.7924119898695275 + x325)^2) + x260 - 2 * b585 >= -2)
@NLconstraint(m, e261, -sqrt((-0.8596136949374525 + x322)^2 + (
    -0.6658137355569159 + x323)^2 + (-0.1854598161134392 + x324)^2 + (
    -0.3899285200718041 + x325)^2) + x261 - 2 * b586 >= -2)
@NLconstraint(m, e262, -sqrt((-0.23942936687819738 + x322)^2 + (
    -0.7931287877223899 + x323)^2 + (-0.009184110257544176 + x324)^2 + (
    -0.7905476817951573 + x325)^2) + x262 - 2 * b587 >= -2)
@NLconstraint(m, e263, -sqrt((-0.1667763675050825 + x322)^2 + (
    -0.30614199209589266 + x323)^2 + (-0.6286784916754126 + x324)^2 + (
    -0.6749145697726233 + x325)^2) + x263 - 2 * b588 >= -2)
@NLconstraint(m, e264, -sqrt((-0.5123965188595846 + x322)^2 + (
    -0.556215195448374 + x323)^2 + (-0.5888863209509851 + x324)^2 + (
    -0.6003058073162648 + x325)^2) + x264 - 2 * b589 >= -2)
@NLconstraint(m, e265, -sqrt((-0.10830095398871686 + x322)^2 + (
    -0.301870958131248 + x323)^2 + (-0.020499027923741364 + x324)^2 + (
    -0.5668022276384451 + x325)^2) + x265 - 2 * b590 >= -2)
@NLconstraint(m, e266, -sqrt((-0.29450295704025886 + x322)^2 + (
    -0.24215631594412912 + x323)^2 + (-0.2744568069724159 + x324)^2 + (
    -0.9412593709117075 + x325)^2) + x266 - 2 * b591 >= -2)
@NLconstraint(m, e267, -sqrt((-0.1282338254681593 + x322)^2 + (
    -0.9019460548181631 + x323)^2 + (-0.9031736614711603 + x324)^2 + (
    -0.2037984038273466 + x325)^2) + x267 - 2 * b592 >= -2)
@NLconstraint(m, e268, -sqrt((-0.829797266931312 + x322)^2 + (
    -0.19575994148177733 + x323)^2 + (-0.645872503285497 + x324)^2 + (
    -0.12203855440196454 + x325)^2) + x268 - 2 * b593 >= -2)
@NLconstraint(m, e269, -sqrt((-0.318405760895906 + x322)^2 + (
    -0.4938036901276964 + x323)^2 + (-0.37642068481077395 + x324)^2 + (
    -0.8256324717799948 + x325)^2) + x269 - 2 * b594 >= -2)
@NLconstraint(m, e270, -sqrt((-0.6465433247102469 + x322)^2 + (
    -0.033522650784374886 + x323)^2 + (-0.5581254938339517 + x324)^2 + (
    -0.0912916889874551 + x325)^2) + x270 - 2 * b595 >= -2)
@NLconstraint(m, e271, -sqrt((-0.17497888842654896 + x322)^2 + (
    -0.38968471952782524 + x323)^2 + (-0.3152812984667659 + x324)^2 + (
    -0.5561379670293034 + x325)^2) + x271 - 2 * b596 >= -2)
@NLconstraint(m, e272, -sqrt((-0.9831483568003972 + x322)^2 + (
    -0.7793186335882816 + x323)^2 + (-0.545443726285844 + x324)^2 + (
    -0.8394599012498352 + x325)^2) + x272 - 2 * b597 >= -2)
@NLconstraint(m, e273, -sqrt((-0.16871130717858907 + x322)^2 + (
    -0.7158922205435296 + x323)^2 + (-0.9716203470560987 + x324)^2 + (
    -0.9419601863446189 + x325)^2) + x273 - 2 * b598 >= -2)
@constraint(m, e274, b404 + b419 + b434 + b449 + b464 + b479 + b494 + b509 +
    b524 + b539 + b554 + b569 + b584 == 1)
@constraint(m, e275, b405 + b420 + b435 + b450 + b465 + b480 + b495 + b510 +
    b525 + b540 + b555 + b570 + b585 == 1)
@constraint(m, e276, b406 + b421 + b436 + b451 + b466 + b481 + b496 + b511 +
    b526 + b541 + b556 + b571 + b586 == 1)
@constraint(m, e277, b407 + b422 + b437 + b452 + b467 + b482 + b497 + b512 +
    b527 + b542 + b557 + b572 + b587 == 1)
@constraint(m, e278, b408 + b423 + b438 + b453 + b468 + b483 + b498 + b513 +
    b528 + b543 + b558 + b573 + b588 == 1)
@constraint(m, e279, b409 + b424 + b439 + b454 + b469 + b484 + b499 + b514 +
    b529 + b544 + b559 + b574 + b589 == 1)
@constraint(m, e280, b410 + b425 + b440 + b455 + b470 + b485 + b500 + b515 +
    b530 + b545 + b560 + b575 + b590 == 1)
@constraint(m, e281, b411 + b426 + b441 + b456 + b471 + b486 + b501 + b516 +
    b531 + b546 + b561 + b576 + b591 == 1)
@constraint(m, e282, b412 + b427 + b442 + b457 + b472 + b487 + b502 + b517 +
    b532 + b547 + b562 + b577 + b592 == 1)
@constraint(m, e283, b413 + b428 + b443 + b458 + b473 + b488 + b503 + b518 +
    b533 + b548 + b563 + b578 + b593 == 1)
@constraint(m, e284, b414 + b429 + b444 + b459 + b474 + b489 + b504 + b519 +
    b534 + b549 + b564 + b579 + b594 == 1)
@constraint(m, e285, b415 + b430 + b445 + b460 + b475 + b490 + b505 + b520 +
    b535 + b550 + b565 + b580 + b595 == 1)
@constraint(m, e286, b416 + b431 + b446 + b461 + b476 + b491 + b506 + b521 +
    b536 + b551 + b566 + b581 + b596 == 1)
@constraint(m, e287, b417 + b432 + b447 + b462 + b477 + b492 + b507 + b522 +
    b537 + b552 + b567 + b582 + b597 == 1)
@constraint(m, e288, b418 + b433 + b448 + b463 + b478 + b493 + b508 + b523 +
    b538 + b553 + b568 + b583 + b598 == 1)
@constraint(m, e289, b326 + b327 + b328 + b329 + b330 + b331 + b332 + b333 +
    b334 + b335 + b336 + b337 + b404 + b405 + b406 + b407 + b408 + b409 + b410
    + b411 + b412 + b413 + b414 + b415 + b416 + b417 + b418 == 3)
@constraint(m, e290, b326 + b338 + b339 + b340 + b341 + b342 + b343 + b344 +
    b345 + b346 + b347 + b348 + b419 + b420 + b421 + b422 + b423 + b424 + b425
    + b426 + b427 + b428 + b429 + b430 + b431 + b432 + b433 == 3)
@constraint(m, e291, b327 + b338 + b349 + b350 + b351 + b352 + b353 + b354 +
    b355 + b356 + b357 + b358 + b434 + b435 + b436 + b437 + b438 + b439 + b440
    + b441 + b442 + b443 + b444 + b445 + b446 + b447 + b448 == 3)
@constraint(m, e292, b328 + b339 + b349 + b359 + b360 + b361 + b362 + b363 +
    b364 + b365 + b366 + b367 + b449 + b450 + b451 + b452 + b453 + b454 + b455
    + b456 + b457 + b458 + b459 + b460 + b461 + b462 + b463 == 3)
@constraint(m, e293, b329 + b340 + b350 + b359 + b368 + b369 + b370 + b371 +
    b372 + b373 + b374 + b375 + b464 + b465 + b466 + b467 + b468 + b469 + b470
    + b471 + b472 + b473 + b474 + b475 + b476 + b477 + b478 == 3)
@constraint(m, e294, b330 + b341 + b351 + b360 + b368 + b376 + b377 + b378 +
    b379 + b380 + b381 + b382 + b479 + b480 + b481 + b482 + b483 + b484 + b485
    + b486 + b487 + b488 + b489 + b490 + b491 + b492 + b493 == 3)
@constraint(m, e295, b331 + b342 + b352 + b361 + b369 + b376 + b383 + b384 +
    b385 + b386 + b387 + b388 + b494 + b495 + b496 + b497 + b498 + b499 + b500
    + b501 + b502 + b503 + b504 + b505 + b506 + b507 + b508 == 3)
@constraint(m, e296, b332 + b343 + b353 + b362 + b370 + b377 + b383 + b389 +
    b390 + b391 + b392 + b393 + b509 + b510 + b511 + b512 + b513 + b514 + b515
    + b516 + b517 + b518 + b519 + b520 + b521 + b522 + b523 == 3)
@constraint(m, e297, b333 + b344 + b354 + b363 + b371 + b378 + b384 + b389 +
    b394 + b395 + b396 + b397 + b524 + b525 + b526 + b527 + b528 + b529 + b530
    + b531 + b532 + b533 + b534 + b535 + b536 + b537 + b538 == 3)
@constraint(m, e298, b334 + b345 + b355 + b364 + b372 + b379 + b385 + b390 +
    b394 + b398 + b399 + b400 + b539 + b540 + b541 + b542 + b543 + b544 + b545
    + b546 + b547 + b548 + b549 + b550 + b551 + b552 + b553 == 3)
@constraint(m, e299, b335 + b346 + b356 + b365 + b373 + b380 + b386 + b391 +
    b395 + b398 + b401 + b402 + b554 + b555 + b556 + b557 + b558 + b559 + b560
    + b561 + b562 + b563 + b564 + b565 + b566 + b567 + b568 == 3)
@constraint(m, e300, b336 + b347 + b357 + b366 + b374 + b381 + b387 + b392 +
    b396 + b399 + b401 + b403 + b569 + b570 + b571 + b572 + b573 + b574 + b575
    + b576 + b577 + b578 + b579 + b580 + b581 + b582 + b583 == 3)
@constraint(m, e301, b337 + b348 + b358 + b367 + b375 + b382 + b388 + b393 +
    b397 + b400 + b402 + b403 + b584 + b585 + b586 + b587 + b588 + b589 + b590
    + b591 + b592 + b593 + b594 + b595 + b596 + b597 + b598 == 3)
@constraint(m, e302, b326 == 1)
@constraint(m, e303, b327 + b338 == 1)
@constraint(m, e304, b328 + b339 + b349 == 1)
@constraint(m, e305, b329 + b340 + b350 + b359 == 1)
@constraint(m, e306, b330 + b341 + b351 + b360 + b368 == 1)
@constraint(m, e307, b331 + b342 + b352 + b361 + b369 + b376 == 1)
@constraint(m, e308, b332 + b343 + b353 + b362 + b370 + b377 + b383 == 1)
@constraint(m, e309, b333 + b344 + b354 + b363 + b371 + b378 + b384 + b389
    == 1)
@constraint(m, e310, b334 + b345 + b355 + b364 + b372 + b379 + b385 + b390 +
    b394 == 1)
@constraint(m, e311, b335 + b346 + b356 + b365 + b373 + b380 + b386 + b391 +
    b395 + b398 == 1)
@constraint(m, e312, b336 + b347 + b357 + b366 + b374 + b381 + b387 + b392 +
    b396 + b399 + b401 == 1)
@constraint(m, e313, b337 + b348 + b358 + b367 + b375 + b382 + b388 + b393 +
    b397 + b400 + b402 + b403 == 1)
