# MINLP written by GAMS Convert at 05/15/24 11:55:00
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       133       25      108        0        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#       248      140      108        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#      1004      460      544
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
@variable(m, 0 <= b141 <= 1, binary=true, start=0)
@variable(m, 0 <= b142 <= 1, binary=true, start=0)
@variable(m, 0 <= b143 <= 1, binary=true, start=0)
@variable(m, 0 <= b144 <= 1, binary=true, start=0)
@variable(m, 0 <= b145 <= 1, binary=true, start=0)
@variable(m, 0 <= b146 <= 1, binary=true, start=0)
@variable(m, 0 <= b147 <= 1, binary=true, start=0)
@variable(m, 0 <= b148 <= 1, binary=true, start=0)
@variable(m, 0 <= b149 <= 1, binary=true, start=0)
@variable(m, 0 <= b150 <= 1, binary=true, start=0)
@variable(m, 0 <= b151 <= 1, binary=true, start=0)
@variable(m, 0 <= b152 <= 1, binary=true, start=0)
@variable(m, 0 <= b153 <= 1, binary=true, start=0)
@variable(m, 0 <= b154 <= 1, binary=true, start=0)
@variable(m, 0 <= b155 <= 1, binary=true, start=0)
@variable(m, 0 <= b156 <= 1, binary=true, start=0)
@variable(m, 0 <= b157 <= 1, binary=true, start=0)
@variable(m, 0 <= b158 <= 1, binary=true, start=0)
@variable(m, 0 <= b159 <= 1, binary=true, start=0)
@variable(m, 0 <= b160 <= 1, binary=true, start=0)
@variable(m, 0 <= b161 <= 1, binary=true, start=0)
@variable(m, 0 <= b162 <= 1, binary=true, start=0)
@variable(m, 0 <= b163 <= 1, binary=true, start=0)
@variable(m, 0 <= b164 <= 1, binary=true, start=0)
@variable(m, 0 <= b165 <= 1, binary=true, start=0)
@variable(m, 0 <= b166 <= 1, binary=true, start=0)
@variable(m, 0 <= b167 <= 1, binary=true, start=0)
@variable(m, 0 <= b168 <= 1, binary=true, start=0)
@variable(m, 0 <= b169 <= 1, binary=true, start=0)
@variable(m, 0 <= b170 <= 1, binary=true, start=0)
@variable(m, 0 <= b171 <= 1, binary=true, start=0)
@variable(m, 0 <= b172 <= 1, binary=true, start=0)
@variable(m, 0 <= b173 <= 1, binary=true, start=0)
@variable(m, 0 <= b174 <= 1, binary=true, start=0)
@variable(m, 0 <= b175 <= 1, binary=true, start=0)
@variable(m, 0 <= b176 <= 1, binary=true, start=0)
@variable(m, 0 <= b177 <= 1, binary=true, start=0)
@variable(m, 0 <= b178 <= 1, binary=true, start=0)
@variable(m, 0 <= b179 <= 1, binary=true, start=0)
@variable(m, 0 <= b180 <= 1, binary=true, start=0)
@variable(m, 0 <= b181 <= 1, binary=true, start=0)
@variable(m, 0 <= b182 <= 1, binary=true, start=0)
@variable(m, 0 <= b183 <= 1, binary=true, start=0)
@variable(m, 0 <= b184 <= 1, binary=true, start=0)
@variable(m, 0 <= b185 <= 1, binary=true, start=0)
@variable(m, 0 <= b186 <= 1, binary=true, start=0)
@variable(m, 0 <= b187 <= 1, binary=true, start=0)
@variable(m, 0 <= b188 <= 1, binary=true, start=0)
@variable(m, 0 <= b189 <= 1, binary=true, start=0)
@variable(m, 0 <= b190 <= 1, binary=true, start=0)
@variable(m, 0 <= b191 <= 1, binary=true, start=0)
@variable(m, 0 <= b192 <= 1, binary=true, start=0)
@variable(m, 0 <= b193 <= 1, binary=true, start=0)
@variable(m, 0 <= b194 <= 1, binary=true, start=0)
@variable(m, 0 <= b195 <= 1, binary=true, start=0)
@variable(m, 0 <= b196 <= 1, binary=true, start=0)
@variable(m, 0 <= b197 <= 1, binary=true, start=0)
@variable(m, 0 <= b198 <= 1, binary=true, start=0)
@variable(m, 0 <= b199 <= 1, binary=true, start=0)
@variable(m, 0 <= b200 <= 1, binary=true, start=0)
@variable(m, 0 <= b201 <= 1, binary=true, start=0)
@variable(m, 0 <= b202 <= 1, binary=true, start=0)
@variable(m, 0 <= b203 <= 1, binary=true, start=0)
@variable(m, 0 <= b204 <= 1, binary=true, start=0)
@variable(m, 0 <= b205 <= 1, binary=true, start=0)
@variable(m, 0 <= b206 <= 1, binary=true, start=0)
@variable(m, 0 <= b207 <= 1, binary=true, start=0)
@variable(m, 0 <= b208 <= 1, binary=true, start=0)
@variable(m, 0 <= b209 <= 1, binary=true, start=0)
@variable(m, 0 <= b210 <= 1, binary=true, start=0)
@variable(m, 0 <= b211 <= 1, binary=true, start=0)
@variable(m, 0 <= b212 <= 1, binary=true, start=0)
@variable(m, 0 <= b213 <= 1, binary=true, start=0)
@variable(m, 0 <= b214 <= 1, binary=true, start=0)
@variable(m, 0 <= b215 <= 1, binary=true, start=0)
@variable(m, 0 <= b216 <= 1, binary=true, start=0)
@variable(m, 0 <= b217 <= 1, binary=true, start=0)
@variable(m, 0 <= b218 <= 1, binary=true, start=0)
@variable(m, 0 <= b219 <= 1, binary=true, start=0)
@variable(m, 0 <= b220 <= 1, binary=true, start=0)
@variable(m, 0 <= b221 <= 1, binary=true, start=0)
@variable(m, 0 <= b222 <= 1, binary=true, start=0)
@variable(m, 0 <= b223 <= 1, binary=true, start=0)
@variable(m, 0 <= b224 <= 1, binary=true, start=0)
@variable(m, 0 <= b225 <= 1, binary=true, start=0)
@variable(m, 0 <= b226 <= 1, binary=true, start=0)
@variable(m, 0 <= b227 <= 1, binary=true, start=0)
@variable(m, 0 <= b228 <= 1, binary=true, start=0)
@variable(m, 0 <= b229 <= 1, binary=true, start=0)
@variable(m, 0 <= b230 <= 1, binary=true, start=0)
@variable(m, 0 <= b231 <= 1, binary=true, start=0)
@variable(m, 0 <= b232 <= 1, binary=true, start=0)
@variable(m, 0 <= b233 <= 1, binary=true, start=0)
@variable(m, 0 <= b234 <= 1, binary=true, start=0)
@variable(m, 0 <= b235 <= 1, binary=true, start=0)
@variable(m, 0 <= b236 <= 1, binary=true, start=0)
@variable(m, 0 <= b237 <= 1, binary=true, start=0)
@variable(m, 0 <= b238 <= 1, binary=true, start=0)
@variable(m, 0 <= b239 <= 1, binary=true, start=0)
@variable(m, 0 <= b240 <= 1, binary=true, start=0)
@variable(m, 0 <= b241 <= 1, binary=true, start=0)
@variable(m, 0 <= b242 <= 1, binary=true, start=0)
@variable(m, 0 <= b243 <= 1, binary=true, start=0)
@variable(m, 0 <= b244 <= 1, binary=true, start=0)
@variable(m, 0 <= b245 <= 1, binary=true, start=0)
@variable(m, 0 <= b246 <= 1, binary=true, start=0)
@variable(m, 0 <= b247 <= 1, binary=true, start=0)
@variable(m, 0 <= b248 <= 1, binary=true, start=0)

@objective(m, Min, x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x10 + x11 + x12
    + x13 + x14 + x15 + x16 + x17 + x18 + x19 + x20 + x21 + x22 + x23 + x24 +
    x25 + x26 + x27 + x28 + x29 + x30 + x31 + x32 + x33 + x34 + x35 + x36 + x37
    + x38 + x39 + x40 + x41 + x42 + x43 + x44 + x45 + x46 + x47 + x48 + x49 +
    x50 + x51 + x52 + x53 + x54 + x55 + x56 + x57 + x58 + x59 + x60 + x61 + x62
    + x63 + x64 + x65 + x66 + x67 + x68 + x69 + x70 + x71 + x72 + x73 + x74 +
    x75 + x76 + x77 + x78 + x79 + x80 + x81 + x82 + x83 + x84 + x85 + x86 + x87
    + x88 + x89 + x90 + x91 + x92 + x93 + x94 + x95 + x96 + x97 + x98 + x99 +
    x100 + x101 + x102 + x103 + x104 + x105 + x106 + x107 + x108)

@NLconstraint(m, e1, -sqrt((x109 - x113)^2 + (x110 - x114)^2 + (x111 - x115)^2
    + (x112 - x116)^2) + x1 - 2 * b141 >= -2)
@NLconstraint(m, e2, -sqrt((x109 - x117)^2 + (x110 - x118)^2 + (x111 - x119)^2
    + (x112 - x120)^2) + x2 - 2 * b142 >= -2)
@NLconstraint(m, e3, -sqrt((x109 - x121)^2 + (x110 - x122)^2 + (x111 - x123)^2
    + (x112 - x124)^2) + x3 - 2 * b143 >= -2)
@NLconstraint(m, e4, -sqrt((x109 - x125)^2 + (x110 - x126)^2 + (x111 - x127)^2
    + (x112 - x128)^2) + x4 - 2 * b144 >= -2)
@NLconstraint(m, e5, -sqrt((x109 - x129)^2 + (x110 - x130)^2 + (x111 - x131)^2
    + (x112 - x132)^2) + x5 - 2 * b145 >= -2)
@NLconstraint(m, e6, -sqrt((x109 - x133)^2 + (x110 - x134)^2 + (x111 - x135)^2
    + (x112 - x136)^2) + x6 - 2 * b146 >= -2)
@NLconstraint(m, e7, -sqrt((x109 - x137)^2 + (x110 - x138)^2 + (x111 - x139)^2
    + (x112 - x140)^2) + x7 - 2 * b147 >= -2)
@NLconstraint(m, e8, -sqrt((x113 - x117)^2 + (x114 - x118)^2 + (x115 - x119)^2
    + (x116 - x120)^2) + x8 - 2 * b148 >= -2)
@NLconstraint(m, e9, -sqrt((x113 - x121)^2 + (x114 - x122)^2 + (x115 - x123)^2
    + (x116 - x124)^2) + x9 - 2 * b149 >= -2)
@NLconstraint(m, e10, -sqrt((x113 - x125)^2 + (x114 - x126)^2 + (x115 - x127)^2
    + (x116 - x128)^2) + x10 - 2 * b150 >= -2)
@NLconstraint(m, e11, -sqrt((x113 - x129)^2 + (x114 - x130)^2 + (x115 - x131)^2
    + (x116 - x132)^2) + x11 - 2 * b151 >= -2)
@NLconstraint(m, e12, -sqrt((x113 - x133)^2 + (x114 - x134)^2 + (x115 - x135)^2
    + (x116 - x136)^2) + x12 - 2 * b152 >= -2)
@NLconstraint(m, e13, -sqrt((x113 - x137)^2 + (x114 - x138)^2 + (x115 - x139)^2
    + (x116 - x140)^2) + x13 - 2 * b153 >= -2)
@NLconstraint(m, e14, -sqrt((x117 - x121)^2 + (x118 - x122)^2 + (x119 - x123)^2
    + (x120 - x124)^2) + x14 - 2 * b154 >= -2)
@NLconstraint(m, e15, -sqrt((x117 - x125)^2 + (x118 - x126)^2 + (x119 - x127)^2
    + (x120 - x128)^2) + x15 - 2 * b155 >= -2)
@NLconstraint(m, e16, -sqrt((x117 - x129)^2 + (x118 - x130)^2 + (x119 - x131)^2
    + (x120 - x132)^2) + x16 - 2 * b156 >= -2)
@NLconstraint(m, e17, -sqrt((x117 - x133)^2 + (x118 - x134)^2 + (x119 - x135)^2
    + (x120 - x136)^2) + x17 - 2 * b157 >= -2)
@NLconstraint(m, e18, -sqrt((x117 - x137)^2 + (x118 - x138)^2 + (x119 - x139)^2
    + (x120 - x140)^2) + x18 - 2 * b158 >= -2)
@NLconstraint(m, e19, -sqrt((x121 - x125)^2 + (x122 - x126)^2 + (x123 - x127)^2
    + (x124 - x128)^2) + x19 - 2 * b159 >= -2)
@NLconstraint(m, e20, -sqrt((x121 - x129)^2 + (x122 - x130)^2 + (x123 - x131)^2
    + (x124 - x132)^2) + x20 - 2 * b160 >= -2)
@NLconstraint(m, e21, -sqrt((x121 - x133)^2 + (x122 - x134)^2 + (x123 - x135)^2
    + (x124 - x136)^2) + x21 - 2 * b161 >= -2)
@NLconstraint(m, e22, -sqrt((x121 - x137)^2 + (x122 - x138)^2 + (x123 - x139)^2
    + (x124 - x140)^2) + x22 - 2 * b162 >= -2)
@NLconstraint(m, e23, -sqrt((x125 - x129)^2 + (x126 - x130)^2 + (x127 - x131)^2
    + (x128 - x132)^2) + x23 - 2 * b163 >= -2)
@NLconstraint(m, e24, -sqrt((x125 - x133)^2 + (x126 - x134)^2 + (x127 - x135)^2
    + (x128 - x136)^2) + x24 - 2 * b164 >= -2)
@NLconstraint(m, e25, -sqrt((x125 - x137)^2 + (x126 - x138)^2 + (x127 - x139)^2
    + (x128 - x140)^2) + x25 - 2 * b165 >= -2)
@NLconstraint(m, e26, -sqrt((x129 - x133)^2 + (x130 - x134)^2 + (x131 - x135)^2
    + (x132 - x136)^2) + x26 - 2 * b166 >= -2)
@NLconstraint(m, e27, -sqrt((x129 - x137)^2 + (x130 - x138)^2 + (x131 - x139)^2
    + (x132 - x140)^2) + x27 - 2 * b167 >= -2)
@NLconstraint(m, e28, -sqrt((x133 - x137)^2 + (x134 - x138)^2 + (x135 - x139)^2
    + (x136 - x140)^2) + x28 - 2 * b168 >= -2)
@NLconstraint(m, e29, -sqrt((-0.4586067093870614 + x109)^2 + (-0.87786790373901
    + x110)^2 + (-0.031846480408982525 + x111)^2 + (-0.2824261461537926 + x112)
    ^2) + x29 - 2 * b169 >= -2)
@NLconstraint(m, e30, -sqrt((-0.9617911699198027 + x109)^2 + (
    -0.664318734454616 + x110)^2 + (-0.12837236942357588 + x111)^2 + (
    -0.3483892327332404 + x112)^2) + x30 - 2 * b170 >= -2)
@NLconstraint(m, e31, -sqrt((-0.8797493185344203 + x109)^2 + (
    -0.4407622204637107 + x110)^2 + (-0.028632026370586927 + x111)^2 + (
    -0.8961816708493071 + x112)^2) + x31 - 2 * b171 >= -2)
@NLconstraint(m, e32, -sqrt((-0.12987407341084578 + x109)^2 + (
    -0.6412660792617741 + x110)^2 + (-0.619579856895807 + x111)^2 + (
    -0.4606660816810936 + x112)^2) + x32 - 2 * b172 >= -2)
@NLconstraint(m, e33, -sqrt((-0.961985163786831 + x109)^2 + (
    -0.17655246550171377 + x110)^2 + (-0.6047448911757226 + x111)^2 + (
    -0.11360377259896981 + x112)^2) + x33 - 2 * b173 >= -2)
@NLconstraint(m, e34, -sqrt((-0.9655977884311789 + x109)^2 + (
    -0.14480662928012233 + x110)^2 + (-0.5130519321619571 + x111)^2 + (
    -0.8326159829153793 + x112)^2) + x34 - 2 * b174 >= -2)
@NLconstraint(m, e35, -sqrt((-0.883249714790512 + x109)^2 + (
    -0.0975661904170092 + x110)^2 + (-0.8772861663183649 + x111)^2 + (
    -0.8426509635375616 + x112)^2) + x35 - 2 * b175 >= -2)
@NLconstraint(m, e36, -sqrt((-0.31576362796828894 + x109)^2 + (
    -0.7564780588144951 + x110)^2 + (-0.22707288516812119 + x111)^2 + (
    -0.15382194005106342 + x112)^2) + x36 - 2 * b176 >= -2)
@NLconstraint(m, e37, -sqrt((-0.16260363549282186 + x109)^2 + (
    -0.30874561291554403 + x110)^2 + (-0.8262479177966031 + x111)^2 + (
    -0.46182111490147704 + x112)^2) + x37 - 2 * b177 >= -2)
@NLconstraint(m, e38, -sqrt((-0.9890392657963852 + x109)^2 + (
    -0.8938422544755473 + x110)^2 + (-0.2104608453213448 + x111)^2 + (
    -0.4334176146710601 + x112)^2) + x38 - 2 * b178 >= -2)
@NLconstraint(m, e39, -sqrt((-0.4586067093870614 + x113)^2 + (-0.87786790373901
    + x114)^2 + (-0.031846480408982525 + x115)^2 + (-0.2824261461537926 + x116)
    ^2) + x39 - 2 * b179 >= -2)
@NLconstraint(m, e40, -sqrt((-0.9617911699198027 + x113)^2 + (
    -0.664318734454616 + x114)^2 + (-0.12837236942357588 + x115)^2 + (
    -0.3483892327332404 + x116)^2) + x40 - 2 * b180 >= -2)
@NLconstraint(m, e41, -sqrt((-0.8797493185344203 + x113)^2 + (
    -0.4407622204637107 + x114)^2 + (-0.028632026370586927 + x115)^2 + (
    -0.8961816708493071 + x116)^2) + x41 - 2 * b181 >= -2)
@NLconstraint(m, e42, -sqrt((-0.12987407341084578 + x113)^2 + (
    -0.6412660792617741 + x114)^2 + (-0.619579856895807 + x115)^2 + (
    -0.4606660816810936 + x116)^2) + x42 - 2 * b182 >= -2)
@NLconstraint(m, e43, -sqrt((-0.961985163786831 + x113)^2 + (
    -0.17655246550171377 + x114)^2 + (-0.6047448911757226 + x115)^2 + (
    -0.11360377259896981 + x116)^2) + x43 - 2 * b183 >= -2)
@NLconstraint(m, e44, -sqrt((-0.9655977884311789 + x113)^2 + (
    -0.14480662928012233 + x114)^2 + (-0.5130519321619571 + x115)^2 + (
    -0.8326159829153793 + x116)^2) + x44 - 2 * b184 >= -2)
@NLconstraint(m, e45, -sqrt((-0.883249714790512 + x113)^2 + (
    -0.0975661904170092 + x114)^2 + (-0.8772861663183649 + x115)^2 + (
    -0.8426509635375616 + x116)^2) + x45 - 2 * b185 >= -2)
@NLconstraint(m, e46, -sqrt((-0.31576362796828894 + x113)^2 + (
    -0.7564780588144951 + x114)^2 + (-0.22707288516812119 + x115)^2 + (
    -0.15382194005106342 + x116)^2) + x46 - 2 * b186 >= -2)
@NLconstraint(m, e47, -sqrt((-0.16260363549282186 + x113)^2 + (
    -0.30874561291554403 + x114)^2 + (-0.8262479177966031 + x115)^2 + (
    -0.46182111490147704 + x116)^2) + x47 - 2 * b187 >= -2)
@NLconstraint(m, e48, -sqrt((-0.9890392657963852 + x113)^2 + (
    -0.8938422544755473 + x114)^2 + (-0.2104608453213448 + x115)^2 + (
    -0.4334176146710601 + x116)^2) + x48 - 2 * b188 >= -2)
@NLconstraint(m, e49, -sqrt((-0.4586067093870614 + x117)^2 + (-0.87786790373901
    + x118)^2 + (-0.031846480408982525 + x119)^2 + (-0.2824261461537926 + x120)
    ^2) + x49 - 2 * b189 >= -2)
@NLconstraint(m, e50, -sqrt((-0.9617911699198027 + x117)^2 + (
    -0.664318734454616 + x118)^2 + (-0.12837236942357588 + x119)^2 + (
    -0.3483892327332404 + x120)^2) + x50 - 2 * b190 >= -2)
@NLconstraint(m, e51, -sqrt((-0.8797493185344203 + x117)^2 + (
    -0.4407622204637107 + x118)^2 + (-0.028632026370586927 + x119)^2 + (
    -0.8961816708493071 + x120)^2) + x51 - 2 * b191 >= -2)
@NLconstraint(m, e52, -sqrt((-0.12987407341084578 + x117)^2 + (
    -0.6412660792617741 + x118)^2 + (-0.619579856895807 + x119)^2 + (
    -0.4606660816810936 + x120)^2) + x52 - 2 * b192 >= -2)
@NLconstraint(m, e53, -sqrt((-0.961985163786831 + x117)^2 + (
    -0.17655246550171377 + x118)^2 + (-0.6047448911757226 + x119)^2 + (
    -0.11360377259896981 + x120)^2) + x53 - 2 * b193 >= -2)
@NLconstraint(m, e54, -sqrt((-0.9655977884311789 + x117)^2 + (
    -0.14480662928012233 + x118)^2 + (-0.5130519321619571 + x119)^2 + (
    -0.8326159829153793 + x120)^2) + x54 - 2 * b194 >= -2)
@NLconstraint(m, e55, -sqrt((-0.883249714790512 + x117)^2 + (
    -0.0975661904170092 + x118)^2 + (-0.8772861663183649 + x119)^2 + (
    -0.8426509635375616 + x120)^2) + x55 - 2 * b195 >= -2)
@NLconstraint(m, e56, -sqrt((-0.31576362796828894 + x117)^2 + (
    -0.7564780588144951 + x118)^2 + (-0.22707288516812119 + x119)^2 + (
    -0.15382194005106342 + x120)^2) + x56 - 2 * b196 >= -2)
@NLconstraint(m, e57, -sqrt((-0.16260363549282186 + x117)^2 + (
    -0.30874561291554403 + x118)^2 + (-0.8262479177966031 + x119)^2 + (
    -0.46182111490147704 + x120)^2) + x57 - 2 * b197 >= -2)
@NLconstraint(m, e58, -sqrt((-0.9890392657963852 + x117)^2 + (
    -0.8938422544755473 + x118)^2 + (-0.2104608453213448 + x119)^2 + (
    -0.4334176146710601 + x120)^2) + x58 - 2 * b198 >= -2)
@NLconstraint(m, e59, -sqrt((-0.4586067093870614 + x121)^2 + (-0.87786790373901
    + x122)^2 + (-0.031846480408982525 + x123)^2 + (-0.2824261461537926 + x124)
    ^2) + x59 - 2 * b199 >= -2)
@NLconstraint(m, e60, -sqrt((-0.9617911699198027 + x121)^2 + (
    -0.664318734454616 + x122)^2 + (-0.12837236942357588 + x123)^2 + (
    -0.3483892327332404 + x124)^2) + x60 - 2 * b200 >= -2)
@NLconstraint(m, e61, -sqrt((-0.8797493185344203 + x121)^2 + (
    -0.4407622204637107 + x122)^2 + (-0.028632026370586927 + x123)^2 + (
    -0.8961816708493071 + x124)^2) + x61 - 2 * b201 >= -2)
@NLconstraint(m, e62, -sqrt((-0.12987407341084578 + x121)^2 + (
    -0.6412660792617741 + x122)^2 + (-0.619579856895807 + x123)^2 + (
    -0.4606660816810936 + x124)^2) + x62 - 2 * b202 >= -2)
@NLconstraint(m, e63, -sqrt((-0.961985163786831 + x121)^2 + (
    -0.17655246550171377 + x122)^2 + (-0.6047448911757226 + x123)^2 + (
    -0.11360377259896981 + x124)^2) + x63 - 2 * b203 >= -2)
@NLconstraint(m, e64, -sqrt((-0.9655977884311789 + x121)^2 + (
    -0.14480662928012233 + x122)^2 + (-0.5130519321619571 + x123)^2 + (
    -0.8326159829153793 + x124)^2) + x64 - 2 * b204 >= -2)
@NLconstraint(m, e65, -sqrt((-0.883249714790512 + x121)^2 + (
    -0.0975661904170092 + x122)^2 + (-0.8772861663183649 + x123)^2 + (
    -0.8426509635375616 + x124)^2) + x65 - 2 * b205 >= -2)
@NLconstraint(m, e66, -sqrt((-0.31576362796828894 + x121)^2 + (
    -0.7564780588144951 + x122)^2 + (-0.22707288516812119 + x123)^2 + (
    -0.15382194005106342 + x124)^2) + x66 - 2 * b206 >= -2)
@NLconstraint(m, e67, -sqrt((-0.16260363549282186 + x121)^2 + (
    -0.30874561291554403 + x122)^2 + (-0.8262479177966031 + x123)^2 + (
    -0.46182111490147704 + x124)^2) + x67 - 2 * b207 >= -2)
@NLconstraint(m, e68, -sqrt((-0.9890392657963852 + x121)^2 + (
    -0.8938422544755473 + x122)^2 + (-0.2104608453213448 + x123)^2 + (
    -0.4334176146710601 + x124)^2) + x68 - 2 * b208 >= -2)
@NLconstraint(m, e69, -sqrt((-0.4586067093870614 + x125)^2 + (-0.87786790373901
    + x126)^2 + (-0.031846480408982525 + x127)^2 + (-0.2824261461537926 + x128)
    ^2) + x69 - 2 * b209 >= -2)
@NLconstraint(m, e70, -sqrt((-0.9617911699198027 + x125)^2 + (
    -0.664318734454616 + x126)^2 + (-0.12837236942357588 + x127)^2 + (
    -0.3483892327332404 + x128)^2) + x70 - 2 * b210 >= -2)
@NLconstraint(m, e71, -sqrt((-0.8797493185344203 + x125)^2 + (
    -0.4407622204637107 + x126)^2 + (-0.028632026370586927 + x127)^2 + (
    -0.8961816708493071 + x128)^2) + x71 - 2 * b211 >= -2)
@NLconstraint(m, e72, -sqrt((-0.12987407341084578 + x125)^2 + (
    -0.6412660792617741 + x126)^2 + (-0.619579856895807 + x127)^2 + (
    -0.4606660816810936 + x128)^2) + x72 - 2 * b212 >= -2)
@NLconstraint(m, e73, -sqrt((-0.961985163786831 + x125)^2 + (
    -0.17655246550171377 + x126)^2 + (-0.6047448911757226 + x127)^2 + (
    -0.11360377259896981 + x128)^2) + x73 - 2 * b213 >= -2)
@NLconstraint(m, e74, -sqrt((-0.9655977884311789 + x125)^2 + (
    -0.14480662928012233 + x126)^2 + (-0.5130519321619571 + x127)^2 + (
    -0.8326159829153793 + x128)^2) + x74 - 2 * b214 >= -2)
@NLconstraint(m, e75, -sqrt((-0.883249714790512 + x125)^2 + (
    -0.0975661904170092 + x126)^2 + (-0.8772861663183649 + x127)^2 + (
    -0.8426509635375616 + x128)^2) + x75 - 2 * b215 >= -2)
@NLconstraint(m, e76, -sqrt((-0.31576362796828894 + x125)^2 + (
    -0.7564780588144951 + x126)^2 + (-0.22707288516812119 + x127)^2 + (
    -0.15382194005106342 + x128)^2) + x76 - 2 * b216 >= -2)
@NLconstraint(m, e77, -sqrt((-0.16260363549282186 + x125)^2 + (
    -0.30874561291554403 + x126)^2 + (-0.8262479177966031 + x127)^2 + (
    -0.46182111490147704 + x128)^2) + x77 - 2 * b217 >= -2)
@NLconstraint(m, e78, -sqrt((-0.9890392657963852 + x125)^2 + (
    -0.8938422544755473 + x126)^2 + (-0.2104608453213448 + x127)^2 + (
    -0.4334176146710601 + x128)^2) + x78 - 2 * b218 >= -2)
@NLconstraint(m, e79, -sqrt((-0.4586067093870614 + x129)^2 + (-0.87786790373901
    + x130)^2 + (-0.031846480408982525 + x131)^2 + (-0.2824261461537926 + x132)
    ^2) + x79 - 2 * b219 >= -2)
@NLconstraint(m, e80, -sqrt((-0.9617911699198027 + x129)^2 + (
    -0.664318734454616 + x130)^2 + (-0.12837236942357588 + x131)^2 + (
    -0.3483892327332404 + x132)^2) + x80 - 2 * b220 >= -2)
@NLconstraint(m, e81, -sqrt((-0.8797493185344203 + x129)^2 + (
    -0.4407622204637107 + x130)^2 + (-0.028632026370586927 + x131)^2 + (
    -0.8961816708493071 + x132)^2) + x81 - 2 * b221 >= -2)
@NLconstraint(m, e82, -sqrt((-0.12987407341084578 + x129)^2 + (
    -0.6412660792617741 + x130)^2 + (-0.619579856895807 + x131)^2 + (
    -0.4606660816810936 + x132)^2) + x82 - 2 * b222 >= -2)
@NLconstraint(m, e83, -sqrt((-0.961985163786831 + x129)^2 + (
    -0.17655246550171377 + x130)^2 + (-0.6047448911757226 + x131)^2 + (
    -0.11360377259896981 + x132)^2) + x83 - 2 * b223 >= -2)
@NLconstraint(m, e84, -sqrt((-0.9655977884311789 + x129)^2 + (
    -0.14480662928012233 + x130)^2 + (-0.5130519321619571 + x131)^2 + (
    -0.8326159829153793 + x132)^2) + x84 - 2 * b224 >= -2)
@NLconstraint(m, e85, -sqrt((-0.883249714790512 + x129)^2 + (
    -0.0975661904170092 + x130)^2 + (-0.8772861663183649 + x131)^2 + (
    -0.8426509635375616 + x132)^2) + x85 - 2 * b225 >= -2)
@NLconstraint(m, e86, -sqrt((-0.31576362796828894 + x129)^2 + (
    -0.7564780588144951 + x130)^2 + (-0.22707288516812119 + x131)^2 + (
    -0.15382194005106342 + x132)^2) + x86 - 2 * b226 >= -2)
@NLconstraint(m, e87, -sqrt((-0.16260363549282186 + x129)^2 + (
    -0.30874561291554403 + x130)^2 + (-0.8262479177966031 + x131)^2 + (
    -0.46182111490147704 + x132)^2) + x87 - 2 * b227 >= -2)
@NLconstraint(m, e88, -sqrt((-0.9890392657963852 + x129)^2 + (
    -0.8938422544755473 + x130)^2 + (-0.2104608453213448 + x131)^2 + (
    -0.4334176146710601 + x132)^2) + x88 - 2 * b228 >= -2)
@NLconstraint(m, e89, -sqrt((-0.4586067093870614 + x133)^2 + (-0.87786790373901
    + x134)^2 + (-0.031846480408982525 + x135)^2 + (-0.2824261461537926 + x136)
    ^2) + x89 - 2 * b229 >= -2)
@NLconstraint(m, e90, -sqrt((-0.9617911699198027 + x133)^2 + (
    -0.664318734454616 + x134)^2 + (-0.12837236942357588 + x135)^2 + (
    -0.3483892327332404 + x136)^2) + x90 - 2 * b230 >= -2)
@NLconstraint(m, e91, -sqrt((-0.8797493185344203 + x133)^2 + (
    -0.4407622204637107 + x134)^2 + (-0.028632026370586927 + x135)^2 + (
    -0.8961816708493071 + x136)^2) + x91 - 2 * b231 >= -2)
@NLconstraint(m, e92, -sqrt((-0.12987407341084578 + x133)^2 + (
    -0.6412660792617741 + x134)^2 + (-0.619579856895807 + x135)^2 + (
    -0.4606660816810936 + x136)^2) + x92 - 2 * b232 >= -2)
@NLconstraint(m, e93, -sqrt((-0.961985163786831 + x133)^2 + (
    -0.17655246550171377 + x134)^2 + (-0.6047448911757226 + x135)^2 + (
    -0.11360377259896981 + x136)^2) + x93 - 2 * b233 >= -2)
@NLconstraint(m, e94, -sqrt((-0.9655977884311789 + x133)^2 + (
    -0.14480662928012233 + x134)^2 + (-0.5130519321619571 + x135)^2 + (
    -0.8326159829153793 + x136)^2) + x94 - 2 * b234 >= -2)
@NLconstraint(m, e95, -sqrt((-0.883249714790512 + x133)^2 + (
    -0.0975661904170092 + x134)^2 + (-0.8772861663183649 + x135)^2 + (
    -0.8426509635375616 + x136)^2) + x95 - 2 * b235 >= -2)
@NLconstraint(m, e96, -sqrt((-0.31576362796828894 + x133)^2 + (
    -0.7564780588144951 + x134)^2 + (-0.22707288516812119 + x135)^2 + (
    -0.15382194005106342 + x136)^2) + x96 - 2 * b236 >= -2)
@NLconstraint(m, e97, -sqrt((-0.16260363549282186 + x133)^2 + (
    -0.30874561291554403 + x134)^2 + (-0.8262479177966031 + x135)^2 + (
    -0.46182111490147704 + x136)^2) + x97 - 2 * b237 >= -2)
@NLconstraint(m, e98, -sqrt((-0.9890392657963852 + x133)^2 + (
    -0.8938422544755473 + x134)^2 + (-0.2104608453213448 + x135)^2 + (
    -0.4334176146710601 + x136)^2) + x98 - 2 * b238 >= -2)
@NLconstraint(m, e99, -sqrt((-0.4586067093870614 + x137)^2 + (-0.87786790373901
    + x138)^2 + (-0.031846480408982525 + x139)^2 + (-0.2824261461537926 + x140)
    ^2) + x99 - 2 * b239 >= -2)
@NLconstraint(m, e100, -sqrt((-0.9617911699198027 + x137)^2 + (
    -0.664318734454616 + x138)^2 + (-0.12837236942357588 + x139)^2 + (
    -0.3483892327332404 + x140)^2) + x100 - 2 * b240 >= -2)
@NLconstraint(m, e101, -sqrt((-0.8797493185344203 + x137)^2 + (
    -0.4407622204637107 + x138)^2 + (-0.028632026370586927 + x139)^2 + (
    -0.8961816708493071 + x140)^2) + x101 - 2 * b241 >= -2)
@NLconstraint(m, e102, -sqrt((-0.12987407341084578 + x137)^2 + (
    -0.6412660792617741 + x138)^2 + (-0.619579856895807 + x139)^2 + (
    -0.4606660816810936 + x140)^2) + x102 - 2 * b242 >= -2)
@NLconstraint(m, e103, -sqrt((-0.961985163786831 + x137)^2 + (
    -0.17655246550171377 + x138)^2 + (-0.6047448911757226 + x139)^2 + (
    -0.11360377259896981 + x140)^2) + x103 - 2 * b243 >= -2)
@NLconstraint(m, e104, -sqrt((-0.9655977884311789 + x137)^2 + (
    -0.14480662928012233 + x138)^2 + (-0.5130519321619571 + x139)^2 + (
    -0.8326159829153793 + x140)^2) + x104 - 2 * b244 >= -2)
@NLconstraint(m, e105, -sqrt((-0.883249714790512 + x137)^2 + (
    -0.0975661904170092 + x138)^2 + (-0.8772861663183649 + x139)^2 + (
    -0.8426509635375616 + x140)^2) + x105 - 2 * b245 >= -2)
@NLconstraint(m, e106, -sqrt((-0.31576362796828894 + x137)^2 + (
    -0.7564780588144951 + x138)^2 + (-0.22707288516812119 + x139)^2 + (
    -0.15382194005106342 + x140)^2) + x106 - 2 * b246 >= -2)
@NLconstraint(m, e107, -sqrt((-0.16260363549282186 + x137)^2 + (
    -0.30874561291554403 + x138)^2 + (-0.8262479177966031 + x139)^2 + (
    -0.46182111490147704 + x140)^2) + x107 - 2 * b247 >= -2)
@NLconstraint(m, e108, -sqrt((-0.9890392657963852 + x137)^2 + (
    -0.8938422544755473 + x138)^2 + (-0.2104608453213448 + x139)^2 + (
    -0.4334176146710601 + x140)^2) + x108 - 2 * b248 >= -2)
@constraint(m, e109, b169 + b179 + b189 + b199 + b209 + b219 + b229 + b239
    == 1)
@constraint(m, e110, b170 + b180 + b190 + b200 + b210 + b220 + b230 + b240
    == 1)
@constraint(m, e111, b171 + b181 + b191 + b201 + b211 + b221 + b231 + b241
    == 1)
@constraint(m, e112, b172 + b182 + b192 + b202 + b212 + b222 + b232 + b242
    == 1)
@constraint(m, e113, b173 + b183 + b193 + b203 + b213 + b223 + b233 + b243
    == 1)
@constraint(m, e114, b174 + b184 + b194 + b204 + b214 + b224 + b234 + b244
    == 1)
@constraint(m, e115, b175 + b185 + b195 + b205 + b215 + b225 + b235 + b245
    == 1)
@constraint(m, e116, b176 + b186 + b196 + b206 + b216 + b226 + b236 + b246
    == 1)
@constraint(m, e117, b177 + b187 + b197 + b207 + b217 + b227 + b237 + b247
    == 1)
@constraint(m, e118, b178 + b188 + b198 + b208 + b218 + b228 + b238 + b248
    == 1)
@constraint(m, e119, b141 + b142 + b143 + b144 + b145 + b146 + b147 + b169 +
    b170 + b171 + b172 + b173 + b174 + b175 + b176 + b177 + b178 == 3)
@constraint(m, e120, b141 + b148 + b149 + b150 + b151 + b152 + b153 + b179 +
    b180 + b181 + b182 + b183 + b184 + b185 + b186 + b187 + b188 == 3)
@constraint(m, e121, b142 + b148 + b154 + b155 + b156 + b157 + b158 + b189 +
    b190 + b191 + b192 + b193 + b194 + b195 + b196 + b197 + b198 == 3)
@constraint(m, e122, b143 + b149 + b154 + b159 + b160 + b161 + b162 + b199 +
    b200 + b201 + b202 + b203 + b204 + b205 + b206 + b207 + b208 == 3)
@constraint(m, e123, b144 + b150 + b155 + b159 + b163 + b164 + b165 + b209 +
    b210 + b211 + b212 + b213 + b214 + b215 + b216 + b217 + b218 == 3)
@constraint(m, e124, b145 + b151 + b156 + b160 + b163 + b166 + b167 + b219 +
    b220 + b221 + b222 + b223 + b224 + b225 + b226 + b227 + b228 == 3)
@constraint(m, e125, b146 + b152 + b157 + b161 + b164 + b166 + b168 + b229 +
    b230 + b231 + b232 + b233 + b234 + b235 + b236 + b237 + b238 == 3)
@constraint(m, e126, b147 + b153 + b158 + b162 + b165 + b167 + b168 + b239 +
    b240 + b241 + b242 + b243 + b244 + b245 + b246 + b247 + b248 == 3)
@constraint(m, e127, b141 == 1)
@constraint(m, e128, b142 + b148 == 1)
@constraint(m, e129, b143 + b149 + b154 == 1)
@constraint(m, e130, b144 + b150 + b155 + b159 == 1)
@constraint(m, e131, b145 + b151 + b156 + b160 + b163 == 1)
@constraint(m, e132, b146 + b152 + b157 + b161 + b164 + b166 == 1)
@constraint(m, e133, b147 + b153 + b158 + b162 + b165 + b167 + b168 == 1)
