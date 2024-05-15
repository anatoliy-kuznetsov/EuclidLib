# MINLP written by GAMS Convert at 05/15/24 11:58:35
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       313       40      273        0        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#       611      338      273        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#      2925     1170     1755
#
# Reformulation has removed 1 variable and 1 equation

from pyomo.environ import *

model = m = ConcreteModel()

m.x1 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x2 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x3 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x4 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x5 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x6 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x7 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x8 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x9 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x10 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x11 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x12 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x13 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x14 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x15 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x16 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x17 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x18 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x19 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x20 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x21 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x22 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x23 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x24 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x25 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x26 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x27 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x28 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x29 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x30 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x31 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x32 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x33 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x34 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x35 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x36 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x37 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x38 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x39 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x40 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x41 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x42 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x43 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x44 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x45 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x46 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x47 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x48 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x49 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x50 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x51 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x52 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x53 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x54 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x55 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x56 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x57 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x58 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x59 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x60 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x61 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x62 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x63 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x64 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x65 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x66 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x67 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x68 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x69 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x70 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x71 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x72 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x73 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x74 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x75 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x76 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x77 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x78 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x79 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x80 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x81 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x82 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x83 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x84 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x85 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x86 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x87 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x88 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x89 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x90 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x91 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x92 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x93 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x94 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x95 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x96 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x97 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x98 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x99 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x100 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x101 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x102 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x103 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x104 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x105 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x106 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x107 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x108 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x109 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x110 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x111 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x112 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x113 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x114 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x115 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x116 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x117 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x118 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x119 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x120 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x121 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x122 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x123 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x124 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x125 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x126 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x127 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x128 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x129 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x130 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x131 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x132 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x133 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x134 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x135 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x136 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x137 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x138 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x139 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x140 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x141 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x142 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x143 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x144 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x145 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x146 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x147 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x148 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x149 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x150 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x151 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x152 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x153 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x154 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x155 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x156 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x157 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x158 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x159 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x160 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x161 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x162 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x163 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x164 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x165 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x166 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x167 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x168 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x169 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x170 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x171 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x172 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x173 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x174 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x175 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x176 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x177 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x178 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x179 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x180 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x181 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x182 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x183 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x184 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x185 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x186 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x187 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x188 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x189 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x190 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x191 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x192 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x193 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x194 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x195 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x196 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x197 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x198 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x199 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x200 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x201 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x202 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x203 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x204 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x205 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x206 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x207 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x208 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x209 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x210 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x211 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x212 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x213 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x214 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x215 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x216 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x217 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x218 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x219 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x220 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x221 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x222 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x223 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x224 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x225 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x226 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x227 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x228 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x229 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x230 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x231 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x232 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x233 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x234 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x235 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x236 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x237 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x238 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x239 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x240 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x241 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x242 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x243 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x244 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x245 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x246 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x247 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x248 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x249 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x250 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x251 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x252 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x253 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x254 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x255 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x256 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x257 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x258 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x259 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x260 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x261 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x262 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x263 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x264 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x265 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x266 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x267 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x268 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x269 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x270 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x271 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x272 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x273 = Var(within=Reals, bounds=(0,2.23606797749979), initialize=0)
m.x274 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x275 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x276 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x277 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x278 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x279 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x280 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x281 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x282 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x283 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x284 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x285 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x286 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x287 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x288 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x289 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x290 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x291 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x292 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x293 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x294 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x295 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x296 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x297 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x298 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x299 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x300 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x301 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x302 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x303 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x304 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x305 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x306 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x307 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x308 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x309 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x310 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x311 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x312 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x313 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x314 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x315 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x316 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x317 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x318 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x319 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x320 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x321 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x322 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x323 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x324 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x325 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x326 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x327 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x328 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x329 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x330 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x331 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x332 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x333 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x334 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x335 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x336 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x337 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x338 = Var(within=Reals, bounds=(0,1), initialize=0)
m.b339 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b340 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b341 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b342 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b343 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b344 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b345 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b346 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b347 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b348 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b349 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b350 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b351 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b352 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b353 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b354 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b355 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b356 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b357 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b358 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b359 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b360 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b361 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b362 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b363 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b364 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b365 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b366 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b367 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b368 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b369 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b370 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b371 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b372 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b373 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b374 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b375 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b376 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b377 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b378 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b379 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b380 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b381 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b382 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b383 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b384 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b385 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b386 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b387 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b388 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b389 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b390 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b391 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b392 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b393 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b394 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b395 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b396 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b397 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b398 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b399 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b400 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b401 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b402 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b403 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b404 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b405 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b406 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b407 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b408 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b409 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b410 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b411 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b412 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b413 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b414 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b415 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b416 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b417 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b418 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b419 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b420 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b421 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b422 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b423 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b424 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b425 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b426 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b427 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b428 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b429 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b430 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b431 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b432 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b433 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b434 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b435 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b436 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b437 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b438 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b439 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b440 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b441 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b442 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b443 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b444 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b445 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b446 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b447 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b448 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b449 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b450 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b451 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b452 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b453 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b454 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b455 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b456 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b457 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b458 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b459 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b460 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b461 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b462 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b463 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b464 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b465 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b466 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b467 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b468 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b469 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b470 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b471 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b472 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b473 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b474 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b475 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b476 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b477 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b478 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b479 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b480 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b481 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b482 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b483 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b484 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b485 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b486 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b487 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b488 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b489 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b490 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b491 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b492 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b493 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b494 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b495 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b496 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b497 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b498 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b499 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b500 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b501 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b502 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b503 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b504 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b505 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b506 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b507 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b508 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b509 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b510 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b511 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b512 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b513 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b514 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b515 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b516 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b517 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b518 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b519 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b520 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b521 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b522 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b523 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b524 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b525 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b526 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b527 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b528 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b529 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b530 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b531 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b532 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b533 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b534 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b535 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b536 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b537 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b538 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b539 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b540 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b541 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b542 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b543 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b544 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b545 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b546 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b547 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b548 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b549 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b550 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b551 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b552 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b553 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b554 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b555 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b556 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b557 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b558 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b559 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b560 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b561 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b562 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b563 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b564 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b565 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b566 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b567 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b568 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b569 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b570 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b571 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b572 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b573 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b574 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b575 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b576 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b577 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b578 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b579 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b580 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b581 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b582 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b583 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b584 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b585 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b586 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b587 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b588 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b589 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b590 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b591 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b592 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b593 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b594 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b595 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b596 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b597 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b598 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b599 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b600 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b601 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b602 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b603 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b604 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b605 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b606 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b607 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b608 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b609 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b610 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b611 = Var(within=Binary, bounds=(0,1), initialize=0)

m.obj = Objective(sense=minimize, expr= m.x1 + m.x2 + m.x3 + m.x4 + m.x5 + m.x6
    + m.x7 + m.x8 + m.x9 + m.x10 + m.x11 + m.x12 + m.x13 + m.x14 + m.x15 +
    m.x16 + m.x17 + m.x18 + m.x19 + m.x20 + m.x21 + m.x22 + m.x23 + m.x24 +
    m.x25 + m.x26 + m.x27 + m.x28 + m.x29 + m.x30 + m.x31 + m.x32 + m.x33 +
    m.x34 + m.x35 + m.x36 + m.x37 + m.x38 + m.x39 + m.x40 + m.x41 + m.x42 +
    m.x43 + m.x44 + m.x45 + m.x46 + m.x47 + m.x48 + m.x49 + m.x50 + m.x51 +
    m.x52 + m.x53 + m.x54 + m.x55 + m.x56 + m.x57 + m.x58 + m.x59 + m.x60 +
    m.x61 + m.x62 + m.x63 + m.x64 + m.x65 + m.x66 + m.x67 + m.x68 + m.x69 +
    m.x70 + m.x71 + m.x72 + m.x73 + m.x74 + m.x75 + m.x76 + m.x77 + m.x78 +
    m.x79 + m.x80 + m.x81 + m.x82 + m.x83 + m.x84 + m.x85 + m.x86 + m.x87 +
    m.x88 + m.x89 + m.x90 + m.x91 + m.x92 + m.x93 + m.x94 + m.x95 + m.x96 +
    m.x97 + m.x98 + m.x99 + m.x100 + m.x101 + m.x102 + m.x103 + m.x104 + m.x105
    + m.x106 + m.x107 + m.x108 + m.x109 + m.x110 + m.x111 + m.x112 + m.x113 +
    m.x114 + m.x115 + m.x116 + m.x117 + m.x118 + m.x119 + m.x120 + m.x121 +
    m.x122 + m.x123 + m.x124 + m.x125 + m.x126 + m.x127 + m.x128 + m.x129 +
    m.x130 + m.x131 + m.x132 + m.x133 + m.x134 + m.x135 + m.x136 + m.x137 +
    m.x138 + m.x139 + m.x140 + m.x141 + m.x142 + m.x143 + m.x144 + m.x145 +
    m.x146 + m.x147 + m.x148 + m.x149 + m.x150 + m.x151 + m.x152 + m.x153 +
    m.x154 + m.x155 + m.x156 + m.x157 + m.x158 + m.x159 + m.x160 + m.x161 +
    m.x162 + m.x163 + m.x164 + m.x165 + m.x166 + m.x167 + m.x168 + m.x169 +
    m.x170 + m.x171 + m.x172 + m.x173 + m.x174 + m.x175 + m.x176 + m.x177 +
    m.x178 + m.x179 + m.x180 + m.x181 + m.x182 + m.x183 + m.x184 + m.x185 +
    m.x186 + m.x187 + m.x188 + m.x189 + m.x190 + m.x191 + m.x192 + m.x193 +
    m.x194 + m.x195 + m.x196 + m.x197 + m.x198 + m.x199 + m.x200 + m.x201 +
    m.x202 + m.x203 + m.x204 + m.x205 + m.x206 + m.x207 + m.x208 + m.x209 +
    m.x210 + m.x211 + m.x212 + m.x213 + m.x214 + m.x215 + m.x216 + m.x217 +
    m.x218 + m.x219 + m.x220 + m.x221 + m.x222 + m.x223 + m.x224 + m.x225 +
    m.x226 + m.x227 + m.x228 + m.x229 + m.x230 + m.x231 + m.x232 + m.x233 +
    m.x234 + m.x235 + m.x236 + m.x237 + m.x238 + m.x239 + m.x240 + m.x241 +
    m.x242 + m.x243 + m.x244 + m.x245 + m.x246 + m.x247 + m.x248 + m.x249 +
    m.x250 + m.x251 + m.x252 + m.x253 + m.x254 + m.x255 + m.x256 + m.x257 +
    m.x258 + m.x259 + m.x260 + m.x261 + m.x262 + m.x263 + m.x264 + m.x265 +
    m.x266 + m.x267 + m.x268 + m.x269 + m.x270 + m.x271 + m.x272 + m.x273)

m.e1 = Constraint(expr= -sqrt((m.x274 - m.x279)**2 + (m.x275 - m.x280)**2 + (
    m.x276 - m.x281)**2 + (m.x277 - m.x282)**2 + (m.x278 - m.x283)**2) + m.x1
    - 2.23606797749979 * m.b339 >= -2.23606797749979)
m.e2 = Constraint(expr= -sqrt((m.x274 - m.x284)**2 + (m.x275 - m.x285)**2 + (
    m.x276 - m.x286)**2 + (m.x277 - m.x287)**2 + (m.x278 - m.x288)**2) + m.x2
    - 2.23606797749979 * m.b340 >= -2.23606797749979)
m.e3 = Constraint(expr= -sqrt((m.x274 - m.x289)**2 + (m.x275 - m.x290)**2 + (
    m.x276 - m.x291)**2 + (m.x277 - m.x292)**2 + (m.x278 - m.x293)**2) + m.x3
    - 2.23606797749979 * m.b341 >= -2.23606797749979)
m.e4 = Constraint(expr= -sqrt((m.x274 - m.x294)**2 + (m.x275 - m.x295)**2 + (
    m.x276 - m.x296)**2 + (m.x277 - m.x297)**2 + (m.x278 - m.x298)**2) + m.x4
    - 2.23606797749979 * m.b342 >= -2.23606797749979)
m.e5 = Constraint(expr= -sqrt((m.x274 - m.x299)**2 + (m.x275 - m.x300)**2 + (
    m.x276 - m.x301)**2 + (m.x277 - m.x302)**2 + (m.x278 - m.x303)**2) + m.x5
    - 2.23606797749979 * m.b343 >= -2.23606797749979)
m.e6 = Constraint(expr= -sqrt((m.x274 - m.x304)**2 + (m.x275 - m.x305)**2 + (
    m.x276 - m.x306)**2 + (m.x277 - m.x307)**2 + (m.x278 - m.x308)**2) + m.x6
    - 2.23606797749979 * m.b344 >= -2.23606797749979)
m.e7 = Constraint(expr= -sqrt((m.x274 - m.x309)**2 + (m.x275 - m.x310)**2 + (
    m.x276 - m.x311)**2 + (m.x277 - m.x312)**2 + (m.x278 - m.x313)**2) + m.x7
    - 2.23606797749979 * m.b345 >= -2.23606797749979)
m.e8 = Constraint(expr= -sqrt((m.x274 - m.x314)**2 + (m.x275 - m.x315)**2 + (
    m.x276 - m.x316)**2 + (m.x277 - m.x317)**2 + (m.x278 - m.x318)**2) + m.x8
    - 2.23606797749979 * m.b346 >= -2.23606797749979)
m.e9 = Constraint(expr= -sqrt((m.x274 - m.x319)**2 + (m.x275 - m.x320)**2 + (
    m.x276 - m.x321)**2 + (m.x277 - m.x322)**2 + (m.x278 - m.x323)**2) + m.x9
    - 2.23606797749979 * m.b347 >= -2.23606797749979)
m.e10 = Constraint(expr= -sqrt((m.x274 - m.x324)**2 + (m.x275 - m.x325)**2 + (
    m.x276 - m.x326)**2 + (m.x277 - m.x327)**2 + (m.x278 - m.x328)**2) + m.x10
    - 2.23606797749979 * m.b348 >= -2.23606797749979)
m.e11 = Constraint(expr= -sqrt((m.x274 - m.x329)**2 + (m.x275 - m.x330)**2 + (
    m.x276 - m.x331)**2 + (m.x277 - m.x332)**2 + (m.x278 - m.x333)**2) + m.x11
    - 2.23606797749979 * m.b349 >= -2.23606797749979)
m.e12 = Constraint(expr= -sqrt((m.x274 - m.x334)**2 + (m.x275 - m.x335)**2 + (
    m.x276 - m.x336)**2 + (m.x277 - m.x337)**2 + (m.x278 - m.x338)**2) + m.x12
    - 2.23606797749979 * m.b350 >= -2.23606797749979)
m.e13 = Constraint(expr= -sqrt((m.x279 - m.x284)**2 + (m.x280 - m.x285)**2 + (
    m.x281 - m.x286)**2 + (m.x282 - m.x287)**2 + (m.x283 - m.x288)**2) + m.x13
    - 2.23606797749979 * m.b351 >= -2.23606797749979)
m.e14 = Constraint(expr= -sqrt((m.x279 - m.x289)**2 + (m.x280 - m.x290)**2 + (
    m.x281 - m.x291)**2 + (m.x282 - m.x292)**2 + (m.x283 - m.x293)**2) + m.x14
    - 2.23606797749979 * m.b352 >= -2.23606797749979)
m.e15 = Constraint(expr= -sqrt((m.x279 - m.x294)**2 + (m.x280 - m.x295)**2 + (
    m.x281 - m.x296)**2 + (m.x282 - m.x297)**2 + (m.x283 - m.x298)**2) + m.x15
    - 2.23606797749979 * m.b353 >= -2.23606797749979)
m.e16 = Constraint(expr= -sqrt((m.x279 - m.x299)**2 + (m.x280 - m.x300)**2 + (
    m.x281 - m.x301)**2 + (m.x282 - m.x302)**2 + (m.x283 - m.x303)**2) + m.x16
    - 2.23606797749979 * m.b354 >= -2.23606797749979)
m.e17 = Constraint(expr= -sqrt((m.x279 - m.x304)**2 + (m.x280 - m.x305)**2 + (
    m.x281 - m.x306)**2 + (m.x282 - m.x307)**2 + (m.x283 - m.x308)**2) + m.x17
    - 2.23606797749979 * m.b355 >= -2.23606797749979)
m.e18 = Constraint(expr= -sqrt((m.x279 - m.x309)**2 + (m.x280 - m.x310)**2 + (
    m.x281 - m.x311)**2 + (m.x282 - m.x312)**2 + (m.x283 - m.x313)**2) + m.x18
    - 2.23606797749979 * m.b356 >= -2.23606797749979)
m.e19 = Constraint(expr= -sqrt((m.x279 - m.x314)**2 + (m.x280 - m.x315)**2 + (
    m.x281 - m.x316)**2 + (m.x282 - m.x317)**2 + (m.x283 - m.x318)**2) + m.x19
    - 2.23606797749979 * m.b357 >= -2.23606797749979)
m.e20 = Constraint(expr= -sqrt((m.x279 - m.x319)**2 + (m.x280 - m.x320)**2 + (
    m.x281 - m.x321)**2 + (m.x282 - m.x322)**2 + (m.x283 - m.x323)**2) + m.x20
    - 2.23606797749979 * m.b358 >= -2.23606797749979)
m.e21 = Constraint(expr= -sqrt((m.x279 - m.x324)**2 + (m.x280 - m.x325)**2 + (
    m.x281 - m.x326)**2 + (m.x282 - m.x327)**2 + (m.x283 - m.x328)**2) + m.x21
    - 2.23606797749979 * m.b359 >= -2.23606797749979)
m.e22 = Constraint(expr= -sqrt((m.x279 - m.x329)**2 + (m.x280 - m.x330)**2 + (
    m.x281 - m.x331)**2 + (m.x282 - m.x332)**2 + (m.x283 - m.x333)**2) + m.x22
    - 2.23606797749979 * m.b360 >= -2.23606797749979)
m.e23 = Constraint(expr= -sqrt((m.x279 - m.x334)**2 + (m.x280 - m.x335)**2 + (
    m.x281 - m.x336)**2 + (m.x282 - m.x337)**2 + (m.x283 - m.x338)**2) + m.x23
    - 2.23606797749979 * m.b361 >= -2.23606797749979)
m.e24 = Constraint(expr= -sqrt((m.x284 - m.x289)**2 + (m.x285 - m.x290)**2 + (
    m.x286 - m.x291)**2 + (m.x287 - m.x292)**2 + (m.x288 - m.x293)**2) + m.x24
    - 2.23606797749979 * m.b362 >= -2.23606797749979)
m.e25 = Constraint(expr= -sqrt((m.x284 - m.x294)**2 + (m.x285 - m.x295)**2 + (
    m.x286 - m.x296)**2 + (m.x287 - m.x297)**2 + (m.x288 - m.x298)**2) + m.x25
    - 2.23606797749979 * m.b363 >= -2.23606797749979)
m.e26 = Constraint(expr= -sqrt((m.x284 - m.x299)**2 + (m.x285 - m.x300)**2 + (
    m.x286 - m.x301)**2 + (m.x287 - m.x302)**2 + (m.x288 - m.x303)**2) + m.x26
    - 2.23606797749979 * m.b364 >= -2.23606797749979)
m.e27 = Constraint(expr= -sqrt((m.x284 - m.x304)**2 + (m.x285 - m.x305)**2 + (
    m.x286 - m.x306)**2 + (m.x287 - m.x307)**2 + (m.x288 - m.x308)**2) + m.x27
    - 2.23606797749979 * m.b365 >= -2.23606797749979)
m.e28 = Constraint(expr= -sqrt((m.x284 - m.x309)**2 + (m.x285 - m.x310)**2 + (
    m.x286 - m.x311)**2 + (m.x287 - m.x312)**2 + (m.x288 - m.x313)**2) + m.x28
    - 2.23606797749979 * m.b366 >= -2.23606797749979)
m.e29 = Constraint(expr= -sqrt((m.x284 - m.x314)**2 + (m.x285 - m.x315)**2 + (
    m.x286 - m.x316)**2 + (m.x287 - m.x317)**2 + (m.x288 - m.x318)**2) + m.x29
    - 2.23606797749979 * m.b367 >= -2.23606797749979)
m.e30 = Constraint(expr= -sqrt((m.x284 - m.x319)**2 + (m.x285 - m.x320)**2 + (
    m.x286 - m.x321)**2 + (m.x287 - m.x322)**2 + (m.x288 - m.x323)**2) + m.x30
    - 2.23606797749979 * m.b368 >= -2.23606797749979)
m.e31 = Constraint(expr= -sqrt((m.x284 - m.x324)**2 + (m.x285 - m.x325)**2 + (
    m.x286 - m.x326)**2 + (m.x287 - m.x327)**2 + (m.x288 - m.x328)**2) + m.x31
    - 2.23606797749979 * m.b369 >= -2.23606797749979)
m.e32 = Constraint(expr= -sqrt((m.x284 - m.x329)**2 + (m.x285 - m.x330)**2 + (
    m.x286 - m.x331)**2 + (m.x287 - m.x332)**2 + (m.x288 - m.x333)**2) + m.x32
    - 2.23606797749979 * m.b370 >= -2.23606797749979)
m.e33 = Constraint(expr= -sqrt((m.x284 - m.x334)**2 + (m.x285 - m.x335)**2 + (
    m.x286 - m.x336)**2 + (m.x287 - m.x337)**2 + (m.x288 - m.x338)**2) + m.x33
    - 2.23606797749979 * m.b371 >= -2.23606797749979)
m.e34 = Constraint(expr= -sqrt((m.x289 - m.x294)**2 + (m.x290 - m.x295)**2 + (
    m.x291 - m.x296)**2 + (m.x292 - m.x297)**2 + (m.x293 - m.x298)**2) + m.x34
    - 2.23606797749979 * m.b372 >= -2.23606797749979)
m.e35 = Constraint(expr= -sqrt((m.x289 - m.x299)**2 + (m.x290 - m.x300)**2 + (
    m.x291 - m.x301)**2 + (m.x292 - m.x302)**2 + (m.x293 - m.x303)**2) + m.x35
    - 2.23606797749979 * m.b373 >= -2.23606797749979)
m.e36 = Constraint(expr= -sqrt((m.x289 - m.x304)**2 + (m.x290 - m.x305)**2 + (
    m.x291 - m.x306)**2 + (m.x292 - m.x307)**2 + (m.x293 - m.x308)**2) + m.x36
    - 2.23606797749979 * m.b374 >= -2.23606797749979)
m.e37 = Constraint(expr= -sqrt((m.x289 - m.x309)**2 + (m.x290 - m.x310)**2 + (
    m.x291 - m.x311)**2 + (m.x292 - m.x312)**2 + (m.x293 - m.x313)**2) + m.x37
    - 2.23606797749979 * m.b375 >= -2.23606797749979)
m.e38 = Constraint(expr= -sqrt((m.x289 - m.x314)**2 + (m.x290 - m.x315)**2 + (
    m.x291 - m.x316)**2 + (m.x292 - m.x317)**2 + (m.x293 - m.x318)**2) + m.x38
    - 2.23606797749979 * m.b376 >= -2.23606797749979)
m.e39 = Constraint(expr= -sqrt((m.x289 - m.x319)**2 + (m.x290 - m.x320)**2 + (
    m.x291 - m.x321)**2 + (m.x292 - m.x322)**2 + (m.x293 - m.x323)**2) + m.x39
    - 2.23606797749979 * m.b377 >= -2.23606797749979)
m.e40 = Constraint(expr= -sqrt((m.x289 - m.x324)**2 + (m.x290 - m.x325)**2 + (
    m.x291 - m.x326)**2 + (m.x292 - m.x327)**2 + (m.x293 - m.x328)**2) + m.x40
    - 2.23606797749979 * m.b378 >= -2.23606797749979)
m.e41 = Constraint(expr= -sqrt((m.x289 - m.x329)**2 + (m.x290 - m.x330)**2 + (
    m.x291 - m.x331)**2 + (m.x292 - m.x332)**2 + (m.x293 - m.x333)**2) + m.x41
    - 2.23606797749979 * m.b379 >= -2.23606797749979)
m.e42 = Constraint(expr= -sqrt((m.x289 - m.x334)**2 + (m.x290 - m.x335)**2 + (
    m.x291 - m.x336)**2 + (m.x292 - m.x337)**2 + (m.x293 - m.x338)**2) + m.x42
    - 2.23606797749979 * m.b380 >= -2.23606797749979)
m.e43 = Constraint(expr= -sqrt((m.x294 - m.x299)**2 + (m.x295 - m.x300)**2 + (
    m.x296 - m.x301)**2 + (m.x297 - m.x302)**2 + (m.x298 - m.x303)**2) + m.x43
    - 2.23606797749979 * m.b381 >= -2.23606797749979)
m.e44 = Constraint(expr= -sqrt((m.x294 - m.x304)**2 + (m.x295 - m.x305)**2 + (
    m.x296 - m.x306)**2 + (m.x297 - m.x307)**2 + (m.x298 - m.x308)**2) + m.x44
    - 2.23606797749979 * m.b382 >= -2.23606797749979)
m.e45 = Constraint(expr= -sqrt((m.x294 - m.x309)**2 + (m.x295 - m.x310)**2 + (
    m.x296 - m.x311)**2 + (m.x297 - m.x312)**2 + (m.x298 - m.x313)**2) + m.x45
    - 2.23606797749979 * m.b383 >= -2.23606797749979)
m.e46 = Constraint(expr= -sqrt((m.x294 - m.x314)**2 + (m.x295 - m.x315)**2 + (
    m.x296 - m.x316)**2 + (m.x297 - m.x317)**2 + (m.x298 - m.x318)**2) + m.x46
    - 2.23606797749979 * m.b384 >= -2.23606797749979)
m.e47 = Constraint(expr= -sqrt((m.x294 - m.x319)**2 + (m.x295 - m.x320)**2 + (
    m.x296 - m.x321)**2 + (m.x297 - m.x322)**2 + (m.x298 - m.x323)**2) + m.x47
    - 2.23606797749979 * m.b385 >= -2.23606797749979)
m.e48 = Constraint(expr= -sqrt((m.x294 - m.x324)**2 + (m.x295 - m.x325)**2 + (
    m.x296 - m.x326)**2 + (m.x297 - m.x327)**2 + (m.x298 - m.x328)**2) + m.x48
    - 2.23606797749979 * m.b386 >= -2.23606797749979)
m.e49 = Constraint(expr= -sqrt((m.x294 - m.x329)**2 + (m.x295 - m.x330)**2 + (
    m.x296 - m.x331)**2 + (m.x297 - m.x332)**2 + (m.x298 - m.x333)**2) + m.x49
    - 2.23606797749979 * m.b387 >= -2.23606797749979)
m.e50 = Constraint(expr= -sqrt((m.x294 - m.x334)**2 + (m.x295 - m.x335)**2 + (
    m.x296 - m.x336)**2 + (m.x297 - m.x337)**2 + (m.x298 - m.x338)**2) + m.x50
    - 2.23606797749979 * m.b388 >= -2.23606797749979)
m.e51 = Constraint(expr= -sqrt((m.x299 - m.x304)**2 + (m.x300 - m.x305)**2 + (
    m.x301 - m.x306)**2 + (m.x302 - m.x307)**2 + (m.x303 - m.x308)**2) + m.x51
    - 2.23606797749979 * m.b389 >= -2.23606797749979)
m.e52 = Constraint(expr= -sqrt((m.x299 - m.x309)**2 + (m.x300 - m.x310)**2 + (
    m.x301 - m.x311)**2 + (m.x302 - m.x312)**2 + (m.x303 - m.x313)**2) + m.x52
    - 2.23606797749979 * m.b390 >= -2.23606797749979)
m.e53 = Constraint(expr= -sqrt((m.x299 - m.x314)**2 + (m.x300 - m.x315)**2 + (
    m.x301 - m.x316)**2 + (m.x302 - m.x317)**2 + (m.x303 - m.x318)**2) + m.x53
    - 2.23606797749979 * m.b391 >= -2.23606797749979)
m.e54 = Constraint(expr= -sqrt((m.x299 - m.x319)**2 + (m.x300 - m.x320)**2 + (
    m.x301 - m.x321)**2 + (m.x302 - m.x322)**2 + (m.x303 - m.x323)**2) + m.x54
    - 2.23606797749979 * m.b392 >= -2.23606797749979)
m.e55 = Constraint(expr= -sqrt((m.x299 - m.x324)**2 + (m.x300 - m.x325)**2 + (
    m.x301 - m.x326)**2 + (m.x302 - m.x327)**2 + (m.x303 - m.x328)**2) + m.x55
    - 2.23606797749979 * m.b393 >= -2.23606797749979)
m.e56 = Constraint(expr= -sqrt((m.x299 - m.x329)**2 + (m.x300 - m.x330)**2 + (
    m.x301 - m.x331)**2 + (m.x302 - m.x332)**2 + (m.x303 - m.x333)**2) + m.x56
    - 2.23606797749979 * m.b394 >= -2.23606797749979)
m.e57 = Constraint(expr= -sqrt((m.x299 - m.x334)**2 + (m.x300 - m.x335)**2 + (
    m.x301 - m.x336)**2 + (m.x302 - m.x337)**2 + (m.x303 - m.x338)**2) + m.x57
    - 2.23606797749979 * m.b395 >= -2.23606797749979)
m.e58 = Constraint(expr= -sqrt((m.x304 - m.x309)**2 + (m.x305 - m.x310)**2 + (
    m.x306 - m.x311)**2 + (m.x307 - m.x312)**2 + (m.x308 - m.x313)**2) + m.x58
    - 2.23606797749979 * m.b396 >= -2.23606797749979)
m.e59 = Constraint(expr= -sqrt((m.x304 - m.x314)**2 + (m.x305 - m.x315)**2 + (
    m.x306 - m.x316)**2 + (m.x307 - m.x317)**2 + (m.x308 - m.x318)**2) + m.x59
    - 2.23606797749979 * m.b397 >= -2.23606797749979)
m.e60 = Constraint(expr= -sqrt((m.x304 - m.x319)**2 + (m.x305 - m.x320)**2 + (
    m.x306 - m.x321)**2 + (m.x307 - m.x322)**2 + (m.x308 - m.x323)**2) + m.x60
    - 2.23606797749979 * m.b398 >= -2.23606797749979)
m.e61 = Constraint(expr= -sqrt((m.x304 - m.x324)**2 + (m.x305 - m.x325)**2 + (
    m.x306 - m.x326)**2 + (m.x307 - m.x327)**2 + (m.x308 - m.x328)**2) + m.x61
    - 2.23606797749979 * m.b399 >= -2.23606797749979)
m.e62 = Constraint(expr= -sqrt((m.x304 - m.x329)**2 + (m.x305 - m.x330)**2 + (
    m.x306 - m.x331)**2 + (m.x307 - m.x332)**2 + (m.x308 - m.x333)**2) + m.x62
    - 2.23606797749979 * m.b400 >= -2.23606797749979)
m.e63 = Constraint(expr= -sqrt((m.x304 - m.x334)**2 + (m.x305 - m.x335)**2 + (
    m.x306 - m.x336)**2 + (m.x307 - m.x337)**2 + (m.x308 - m.x338)**2) + m.x63
    - 2.23606797749979 * m.b401 >= -2.23606797749979)
m.e64 = Constraint(expr= -sqrt((m.x309 - m.x314)**2 + (m.x310 - m.x315)**2 + (
    m.x311 - m.x316)**2 + (m.x312 - m.x317)**2 + (m.x313 - m.x318)**2) + m.x64
    - 2.23606797749979 * m.b402 >= -2.23606797749979)
m.e65 = Constraint(expr= -sqrt((m.x309 - m.x319)**2 + (m.x310 - m.x320)**2 + (
    m.x311 - m.x321)**2 + (m.x312 - m.x322)**2 + (m.x313 - m.x323)**2) + m.x65
    - 2.23606797749979 * m.b403 >= -2.23606797749979)
m.e66 = Constraint(expr= -sqrt((m.x309 - m.x324)**2 + (m.x310 - m.x325)**2 + (
    m.x311 - m.x326)**2 + (m.x312 - m.x327)**2 + (m.x313 - m.x328)**2) + m.x66
    - 2.23606797749979 * m.b404 >= -2.23606797749979)
m.e67 = Constraint(expr= -sqrt((m.x309 - m.x329)**2 + (m.x310 - m.x330)**2 + (
    m.x311 - m.x331)**2 + (m.x312 - m.x332)**2 + (m.x313 - m.x333)**2) + m.x67
    - 2.23606797749979 * m.b405 >= -2.23606797749979)
m.e68 = Constraint(expr= -sqrt((m.x309 - m.x334)**2 + (m.x310 - m.x335)**2 + (
    m.x311 - m.x336)**2 + (m.x312 - m.x337)**2 + (m.x313 - m.x338)**2) + m.x68
    - 2.23606797749979 * m.b406 >= -2.23606797749979)
m.e69 = Constraint(expr= -sqrt((m.x314 - m.x319)**2 + (m.x315 - m.x320)**2 + (
    m.x316 - m.x321)**2 + (m.x317 - m.x322)**2 + (m.x318 - m.x323)**2) + m.x69
    - 2.23606797749979 * m.b407 >= -2.23606797749979)
m.e70 = Constraint(expr= -sqrt((m.x314 - m.x324)**2 + (m.x315 - m.x325)**2 + (
    m.x316 - m.x326)**2 + (m.x317 - m.x327)**2 + (m.x318 - m.x328)**2) + m.x70
    - 2.23606797749979 * m.b408 >= -2.23606797749979)
m.e71 = Constraint(expr= -sqrt((m.x314 - m.x329)**2 + (m.x315 - m.x330)**2 + (
    m.x316 - m.x331)**2 + (m.x317 - m.x332)**2 + (m.x318 - m.x333)**2) + m.x71
    - 2.23606797749979 * m.b409 >= -2.23606797749979)
m.e72 = Constraint(expr= -sqrt((m.x314 - m.x334)**2 + (m.x315 - m.x335)**2 + (
    m.x316 - m.x336)**2 + (m.x317 - m.x337)**2 + (m.x318 - m.x338)**2) + m.x72
    - 2.23606797749979 * m.b410 >= -2.23606797749979)
m.e73 = Constraint(expr= -sqrt((m.x319 - m.x324)**2 + (m.x320 - m.x325)**2 + (
    m.x321 - m.x326)**2 + (m.x322 - m.x327)**2 + (m.x323 - m.x328)**2) + m.x73
    - 2.23606797749979 * m.b411 >= -2.23606797749979)
m.e74 = Constraint(expr= -sqrt((m.x319 - m.x329)**2 + (m.x320 - m.x330)**2 + (
    m.x321 - m.x331)**2 + (m.x322 - m.x332)**2 + (m.x323 - m.x333)**2) + m.x74
    - 2.23606797749979 * m.b412 >= -2.23606797749979)
m.e75 = Constraint(expr= -sqrt((m.x319 - m.x334)**2 + (m.x320 - m.x335)**2 + (
    m.x321 - m.x336)**2 + (m.x322 - m.x337)**2 + (m.x323 - m.x338)**2) + m.x75
    - 2.23606797749979 * m.b413 >= -2.23606797749979)
m.e76 = Constraint(expr= -sqrt((m.x324 - m.x329)**2 + (m.x325 - m.x330)**2 + (
    m.x326 - m.x331)**2 + (m.x327 - m.x332)**2 + (m.x328 - m.x333)**2) + m.x76
    - 2.23606797749979 * m.b414 >= -2.23606797749979)
m.e77 = Constraint(expr= -sqrt((m.x324 - m.x334)**2 + (m.x325 - m.x335)**2 + (
    m.x326 - m.x336)**2 + (m.x327 - m.x337)**2 + (m.x328 - m.x338)**2) + m.x77
    - 2.23606797749979 * m.b415 >= -2.23606797749979)
m.e78 = Constraint(expr= -sqrt((m.x329 - m.x334)**2 + (m.x330 - m.x335)**2 + (
    m.x331 - m.x336)**2 + (m.x332 - m.x337)**2 + (m.x333 - m.x338)**2) + m.x78
    - 2.23606797749979 * m.b416 >= -2.23606797749979)
m.e79 = Constraint(expr= -sqrt((-0.45084513414500904 + m.x274)**2 + (
    -0.4366195682760844 + m.x275)**2 + (-0.04163444585203002 + m.x276)**2 + (
    -0.7676272579584664 + m.x277)**2 + (-0.6734553564483233 + m.x278)**2) +
    m.x79 - 2.23606797749979 * m.b417 >= -2.23606797749979)
m.e80 = Constraint(expr= -sqrt((-0.670857540712527 + m.x274)**2 + (
    -0.472665488047444 + m.x275)**2 + (-0.672731114024884 + m.x276)**2 + (
    -0.8824812534975449 + m.x277)**2 + (-0.6920224414883532 + m.x278)**2) +
    m.x80 - 2.23606797749979 * m.b418 >= -2.23606797749979)
m.e81 = Constraint(expr= -sqrt((-0.3456424258652263 + m.x274)**2 + (
    -0.897323531600062 + m.x275)**2 + (-0.3169943908371815 + m.x276)**2 + (
    -0.08378401217902964 + m.x277)**2 + (-0.2511840930177276 + m.x278)**2) +
    m.x81 - 2.23606797749979 * m.b419 >= -2.23606797749979)
m.e82 = Constraint(expr= -sqrt((-0.49653521716587157 + m.x274)**2 + (
    -0.8612924863730758 + m.x275)**2 + (-0.3477168575425721 + m.x276)**2 + (
    -0.6615424192381595 + m.x277)**2 + (-0.2680635035686557 + m.x278)**2) +
    m.x82 - 2.23606797749979 * m.b420 >= -2.23606797749979)
m.e83 = Constraint(expr= -sqrt((-0.027492190735120214 + m.x274)**2 + (
    -0.975830678205581 + m.x275)**2 + (-0.5725079974762737 + m.x276)**2 + (
    -0.4627928206739904 + m.x277)**2 + (-0.676105217625283 + m.x278)**2) +
    m.x83 - 2.23606797749979 * m.b421 >= -2.23606797749979)
m.e84 = Constraint(expr= -sqrt((-0.13167765137927434 + m.x274)**2 + (
    -0.8772422533001436 + m.x275)**2 + (-0.30212459335273456 + m.x276)**2 + (
    -0.9589299306054163 + m.x277)**2 + (-0.1684676992378059 + m.x278)**2) +
    m.x84 - 2.23606797749979 * m.b422 >= -2.23606797749979)
m.e85 = Constraint(expr= -sqrt((-0.4631605820201776 + m.x274)**2 + (
    -0.3075046464306209 + m.x275)**2 + (-0.6161047422348818 + m.x276)**2 + (
    -0.06036679498995601 + m.x277)**2 + (-0.055585229920206314 + m.x278)**2) +
    m.x85 - 2.23606797749979 * m.b423 >= -2.23606797749979)
m.e86 = Constraint(expr= -sqrt((-0.32388656731438237 + m.x274)**2 + (
    -0.05792786993199972 + m.x275)**2 + (-0.8135525615007164 + m.x276)**2 + (
    -0.11918904488489845 + m.x277)**2 + (-0.3074172166187361 + m.x278)**2) +
    m.x86 - 2.23606797749979 * m.b424 >= -2.23606797749979)
m.e87 = Constraint(expr= -sqrt((-0.5224218716951496 + m.x274)**2 + (
    -0.11445496716294967 + m.x275)**2 + (-0.9526471232336744 + m.x276)**2 + (
    -0.29191369035574544 + m.x277)**2 + (-0.5653246839270838 + m.x278)**2) +
    m.x87 - 2.23606797749979 * m.b425 >= -2.23606797749979)
m.e88 = Constraint(expr= -sqrt((-0.21125847741287684 + m.x274)**2 + (
    -0.24527434539791804 + m.x275)**2 + (-0.6289970479606978 + m.x276)**2 + (
    -0.7068457529300446 + m.x277)**2 + (-0.7943561377121612 + m.x278)**2) +
    m.x88 - 2.23606797749979 * m.b426 >= -2.23606797749979)
m.e89 = Constraint(expr= -sqrt((-0.9522420339595141 + m.x274)**2 + (
    -0.9326354363859527 + m.x275)**2 + (-0.4449382446418748 + m.x276)**2 + (
    -0.018772017414026565 + m.x277)**2 + (-0.1570753065990531 + m.x278)**2) +
    m.x89 - 2.23606797749979 * m.b427 >= -2.23606797749979)
m.e90 = Constraint(expr= -sqrt((-0.8796213188443197 + m.x274)**2 + (
    -0.9757325913906182 + m.x275)**2 + (-0.5478578093651233 + m.x276)**2 + (
    -0.00973548730106566 + m.x277)**2 + (-0.27048086044812103 + m.x278)**2) +
    m.x90 - 2.23606797749979 * m.b428 >= -2.23606797749979)
m.e91 = Constraint(expr= -sqrt((-0.7382526421375969 + m.x274)**2 + (
    -0.18734997029644274 + m.x275)**2 + (-0.2597432271723712 + m.x276)**2 + (
    -0.42962015792230956 + m.x277)**2 + (-0.7073477915737445 + m.x278)**2) +
    m.x91 - 2.23606797749979 * m.b429 >= -2.23606797749979)
m.e92 = Constraint(expr= -sqrt((-0.7480253586345234 + m.x274)**2 + (
    -0.39775488720466023 + m.x275)**2 + (-0.3653805995645427 + m.x276)**2 + (
    -0.5146776625112836 + m.x277)**2 + (-0.46172129982047827 + m.x278)**2) +
    m.x92 - 2.23606797749979 * m.b430 >= -2.23606797749979)
m.e93 = Constraint(expr= -sqrt((-0.9807955797704826 + m.x274)**2 + (
    -0.09734685184548297 + m.x275)**2 + (-0.38645671601793696 + m.x276)**2 + (
    -0.33263947083044576 + m.x277)**2 + (-0.5052803496499273 + m.x278)**2) +
    m.x93 - 2.23606797749979 * m.b431 >= -2.23606797749979)
m.e94 = Constraint(expr= -sqrt((-0.45084513414500904 + m.x279)**2 + (
    -0.4366195682760844 + m.x280)**2 + (-0.04163444585203002 + m.x281)**2 + (
    -0.7676272579584664 + m.x282)**2 + (-0.6734553564483233 + m.x283)**2) +
    m.x94 - 2.23606797749979 * m.b432 >= -2.23606797749979)
m.e95 = Constraint(expr= -sqrt((-0.670857540712527 + m.x279)**2 + (
    -0.472665488047444 + m.x280)**2 + (-0.672731114024884 + m.x281)**2 + (
    -0.8824812534975449 + m.x282)**2 + (-0.6920224414883532 + m.x283)**2) +
    m.x95 - 2.23606797749979 * m.b433 >= -2.23606797749979)
m.e96 = Constraint(expr= -sqrt((-0.3456424258652263 + m.x279)**2 + (
    -0.897323531600062 + m.x280)**2 + (-0.3169943908371815 + m.x281)**2 + (
    -0.08378401217902964 + m.x282)**2 + (-0.2511840930177276 + m.x283)**2) +
    m.x96 - 2.23606797749979 * m.b434 >= -2.23606797749979)
m.e97 = Constraint(expr= -sqrt((-0.49653521716587157 + m.x279)**2 + (
    -0.8612924863730758 + m.x280)**2 + (-0.3477168575425721 + m.x281)**2 + (
    -0.6615424192381595 + m.x282)**2 + (-0.2680635035686557 + m.x283)**2) +
    m.x97 - 2.23606797749979 * m.b435 >= -2.23606797749979)
m.e98 = Constraint(expr= -sqrt((-0.027492190735120214 + m.x279)**2 + (
    -0.975830678205581 + m.x280)**2 + (-0.5725079974762737 + m.x281)**2 + (
    -0.4627928206739904 + m.x282)**2 + (-0.676105217625283 + m.x283)**2) +
    m.x98 - 2.23606797749979 * m.b436 >= -2.23606797749979)
m.e99 = Constraint(expr= -sqrt((-0.13167765137927434 + m.x279)**2 + (
    -0.8772422533001436 + m.x280)**2 + (-0.30212459335273456 + m.x281)**2 + (
    -0.9589299306054163 + m.x282)**2 + (-0.1684676992378059 + m.x283)**2) +
    m.x99 - 2.23606797749979 * m.b437 >= -2.23606797749979)
m.e100 = Constraint(expr= -sqrt((-0.4631605820201776 + m.x279)**2 + (
    -0.3075046464306209 + m.x280)**2 + (-0.6161047422348818 + m.x281)**2 + (
    -0.06036679498995601 + m.x282)**2 + (-0.055585229920206314 + m.x283)**2) +
    m.x100 - 2.23606797749979 * m.b438 >= -2.23606797749979)
m.e101 = Constraint(expr= -sqrt((-0.32388656731438237 + m.x279)**2 + (
    -0.05792786993199972 + m.x280)**2 + (-0.8135525615007164 + m.x281)**2 + (
    -0.11918904488489845 + m.x282)**2 + (-0.3074172166187361 + m.x283)**2) +
    m.x101 - 2.23606797749979 * m.b439 >= -2.23606797749979)
m.e102 = Constraint(expr= -sqrt((-0.5224218716951496 + m.x279)**2 + (
    -0.11445496716294967 + m.x280)**2 + (-0.9526471232336744 + m.x281)**2 + (
    -0.29191369035574544 + m.x282)**2 + (-0.5653246839270838 + m.x283)**2) +
    m.x102 - 2.23606797749979 * m.b440 >= -2.23606797749979)
m.e103 = Constraint(expr= -sqrt((-0.21125847741287684 + m.x279)**2 + (
    -0.24527434539791804 + m.x280)**2 + (-0.6289970479606978 + m.x281)**2 + (
    -0.7068457529300446 + m.x282)**2 + (-0.7943561377121612 + m.x283)**2) +
    m.x103 - 2.23606797749979 * m.b441 >= -2.23606797749979)
m.e104 = Constraint(expr= -sqrt((-0.9522420339595141 + m.x279)**2 + (
    -0.9326354363859527 + m.x280)**2 + (-0.4449382446418748 + m.x281)**2 + (
    -0.018772017414026565 + m.x282)**2 + (-0.1570753065990531 + m.x283)**2) +
    m.x104 - 2.23606797749979 * m.b442 >= -2.23606797749979)
m.e105 = Constraint(expr= -sqrt((-0.8796213188443197 + m.x279)**2 + (
    -0.9757325913906182 + m.x280)**2 + (-0.5478578093651233 + m.x281)**2 + (
    -0.00973548730106566 + m.x282)**2 + (-0.27048086044812103 + m.x283)**2) +
    m.x105 - 2.23606797749979 * m.b443 >= -2.23606797749979)
m.e106 = Constraint(expr= -sqrt((-0.7382526421375969 + m.x279)**2 + (
    -0.18734997029644274 + m.x280)**2 + (-0.2597432271723712 + m.x281)**2 + (
    -0.42962015792230956 + m.x282)**2 + (-0.7073477915737445 + m.x283)**2) +
    m.x106 - 2.23606797749979 * m.b444 >= -2.23606797749979)
m.e107 = Constraint(expr= -sqrt((-0.7480253586345234 + m.x279)**2 + (
    -0.39775488720466023 + m.x280)**2 + (-0.3653805995645427 + m.x281)**2 + (
    -0.5146776625112836 + m.x282)**2 + (-0.46172129982047827 + m.x283)**2) +
    m.x107 - 2.23606797749979 * m.b445 >= -2.23606797749979)
m.e108 = Constraint(expr= -sqrt((-0.9807955797704826 + m.x279)**2 + (
    -0.09734685184548297 + m.x280)**2 + (-0.38645671601793696 + m.x281)**2 + (
    -0.33263947083044576 + m.x282)**2 + (-0.5052803496499273 + m.x283)**2) +
    m.x108 - 2.23606797749979 * m.b446 >= -2.23606797749979)
m.e109 = Constraint(expr= -sqrt((-0.45084513414500904 + m.x284)**2 + (
    -0.4366195682760844 + m.x285)**2 + (-0.04163444585203002 + m.x286)**2 + (
    -0.7676272579584664 + m.x287)**2 + (-0.6734553564483233 + m.x288)**2) +
    m.x109 - 2.23606797749979 * m.b447 >= -2.23606797749979)
m.e110 = Constraint(expr= -sqrt((-0.670857540712527 + m.x284)**2 + (
    -0.472665488047444 + m.x285)**2 + (-0.672731114024884 + m.x286)**2 + (
    -0.8824812534975449 + m.x287)**2 + (-0.6920224414883532 + m.x288)**2) +
    m.x110 - 2.23606797749979 * m.b448 >= -2.23606797749979)
m.e111 = Constraint(expr= -sqrt((-0.3456424258652263 + m.x284)**2 + (
    -0.897323531600062 + m.x285)**2 + (-0.3169943908371815 + m.x286)**2 + (
    -0.08378401217902964 + m.x287)**2 + (-0.2511840930177276 + m.x288)**2) +
    m.x111 - 2.23606797749979 * m.b449 >= -2.23606797749979)
m.e112 = Constraint(expr= -sqrt((-0.49653521716587157 + m.x284)**2 + (
    -0.8612924863730758 + m.x285)**2 + (-0.3477168575425721 + m.x286)**2 + (
    -0.6615424192381595 + m.x287)**2 + (-0.2680635035686557 + m.x288)**2) +
    m.x112 - 2.23606797749979 * m.b450 >= -2.23606797749979)
m.e113 = Constraint(expr= -sqrt((-0.027492190735120214 + m.x284)**2 + (
    -0.975830678205581 + m.x285)**2 + (-0.5725079974762737 + m.x286)**2 + (
    -0.4627928206739904 + m.x287)**2 + (-0.676105217625283 + m.x288)**2) +
    m.x113 - 2.23606797749979 * m.b451 >= -2.23606797749979)
m.e114 = Constraint(expr= -sqrt((-0.13167765137927434 + m.x284)**2 + (
    -0.8772422533001436 + m.x285)**2 + (-0.30212459335273456 + m.x286)**2 + (
    -0.9589299306054163 + m.x287)**2 + (-0.1684676992378059 + m.x288)**2) +
    m.x114 - 2.23606797749979 * m.b452 >= -2.23606797749979)
m.e115 = Constraint(expr= -sqrt((-0.4631605820201776 + m.x284)**2 + (
    -0.3075046464306209 + m.x285)**2 + (-0.6161047422348818 + m.x286)**2 + (
    -0.06036679498995601 + m.x287)**2 + (-0.055585229920206314 + m.x288)**2) +
    m.x115 - 2.23606797749979 * m.b453 >= -2.23606797749979)
m.e116 = Constraint(expr= -sqrt((-0.32388656731438237 + m.x284)**2 + (
    -0.05792786993199972 + m.x285)**2 + (-0.8135525615007164 + m.x286)**2 + (
    -0.11918904488489845 + m.x287)**2 + (-0.3074172166187361 + m.x288)**2) +
    m.x116 - 2.23606797749979 * m.b454 >= -2.23606797749979)
m.e117 = Constraint(expr= -sqrt((-0.5224218716951496 + m.x284)**2 + (
    -0.11445496716294967 + m.x285)**2 + (-0.9526471232336744 + m.x286)**2 + (
    -0.29191369035574544 + m.x287)**2 + (-0.5653246839270838 + m.x288)**2) +
    m.x117 - 2.23606797749979 * m.b455 >= -2.23606797749979)
m.e118 = Constraint(expr= -sqrt((-0.21125847741287684 + m.x284)**2 + (
    -0.24527434539791804 + m.x285)**2 + (-0.6289970479606978 + m.x286)**2 + (
    -0.7068457529300446 + m.x287)**2 + (-0.7943561377121612 + m.x288)**2) +
    m.x118 - 2.23606797749979 * m.b456 >= -2.23606797749979)
m.e119 = Constraint(expr= -sqrt((-0.9522420339595141 + m.x284)**2 + (
    -0.9326354363859527 + m.x285)**2 + (-0.4449382446418748 + m.x286)**2 + (
    -0.018772017414026565 + m.x287)**2 + (-0.1570753065990531 + m.x288)**2) +
    m.x119 - 2.23606797749979 * m.b457 >= -2.23606797749979)
m.e120 = Constraint(expr= -sqrt((-0.8796213188443197 + m.x284)**2 + (
    -0.9757325913906182 + m.x285)**2 + (-0.5478578093651233 + m.x286)**2 + (
    -0.00973548730106566 + m.x287)**2 + (-0.27048086044812103 + m.x288)**2) +
    m.x120 - 2.23606797749979 * m.b458 >= -2.23606797749979)
m.e121 = Constraint(expr= -sqrt((-0.7382526421375969 + m.x284)**2 + (
    -0.18734997029644274 + m.x285)**2 + (-0.2597432271723712 + m.x286)**2 + (
    -0.42962015792230956 + m.x287)**2 + (-0.7073477915737445 + m.x288)**2) +
    m.x121 - 2.23606797749979 * m.b459 >= -2.23606797749979)
m.e122 = Constraint(expr= -sqrt((-0.7480253586345234 + m.x284)**2 + (
    -0.39775488720466023 + m.x285)**2 + (-0.3653805995645427 + m.x286)**2 + (
    -0.5146776625112836 + m.x287)**2 + (-0.46172129982047827 + m.x288)**2) +
    m.x122 - 2.23606797749979 * m.b460 >= -2.23606797749979)
m.e123 = Constraint(expr= -sqrt((-0.9807955797704826 + m.x284)**2 + (
    -0.09734685184548297 + m.x285)**2 + (-0.38645671601793696 + m.x286)**2 + (
    -0.33263947083044576 + m.x287)**2 + (-0.5052803496499273 + m.x288)**2) +
    m.x123 - 2.23606797749979 * m.b461 >= -2.23606797749979)
m.e124 = Constraint(expr= -sqrt((-0.45084513414500904 + m.x289)**2 + (
    -0.4366195682760844 + m.x290)**2 + (-0.04163444585203002 + m.x291)**2 + (
    -0.7676272579584664 + m.x292)**2 + (-0.6734553564483233 + m.x293)**2) +
    m.x124 - 2.23606797749979 * m.b462 >= -2.23606797749979)
m.e125 = Constraint(expr= -sqrt((-0.670857540712527 + m.x289)**2 + (
    -0.472665488047444 + m.x290)**2 + (-0.672731114024884 + m.x291)**2 + (
    -0.8824812534975449 + m.x292)**2 + (-0.6920224414883532 + m.x293)**2) +
    m.x125 - 2.23606797749979 * m.b463 >= -2.23606797749979)
m.e126 = Constraint(expr= -sqrt((-0.3456424258652263 + m.x289)**2 + (
    -0.897323531600062 + m.x290)**2 + (-0.3169943908371815 + m.x291)**2 + (
    -0.08378401217902964 + m.x292)**2 + (-0.2511840930177276 + m.x293)**2) +
    m.x126 - 2.23606797749979 * m.b464 >= -2.23606797749979)
m.e127 = Constraint(expr= -sqrt((-0.49653521716587157 + m.x289)**2 + (
    -0.8612924863730758 + m.x290)**2 + (-0.3477168575425721 + m.x291)**2 + (
    -0.6615424192381595 + m.x292)**2 + (-0.2680635035686557 + m.x293)**2) +
    m.x127 - 2.23606797749979 * m.b465 >= -2.23606797749979)
m.e128 = Constraint(expr= -sqrt((-0.027492190735120214 + m.x289)**2 + (
    -0.975830678205581 + m.x290)**2 + (-0.5725079974762737 + m.x291)**2 + (
    -0.4627928206739904 + m.x292)**2 + (-0.676105217625283 + m.x293)**2) +
    m.x128 - 2.23606797749979 * m.b466 >= -2.23606797749979)
m.e129 = Constraint(expr= -sqrt((-0.13167765137927434 + m.x289)**2 + (
    -0.8772422533001436 + m.x290)**2 + (-0.30212459335273456 + m.x291)**2 + (
    -0.9589299306054163 + m.x292)**2 + (-0.1684676992378059 + m.x293)**2) +
    m.x129 - 2.23606797749979 * m.b467 >= -2.23606797749979)
m.e130 = Constraint(expr= -sqrt((-0.4631605820201776 + m.x289)**2 + (
    -0.3075046464306209 + m.x290)**2 + (-0.6161047422348818 + m.x291)**2 + (
    -0.06036679498995601 + m.x292)**2 + (-0.055585229920206314 + m.x293)**2) +
    m.x130 - 2.23606797749979 * m.b468 >= -2.23606797749979)
m.e131 = Constraint(expr= -sqrt((-0.32388656731438237 + m.x289)**2 + (
    -0.05792786993199972 + m.x290)**2 + (-0.8135525615007164 + m.x291)**2 + (
    -0.11918904488489845 + m.x292)**2 + (-0.3074172166187361 + m.x293)**2) +
    m.x131 - 2.23606797749979 * m.b469 >= -2.23606797749979)
m.e132 = Constraint(expr= -sqrt((-0.5224218716951496 + m.x289)**2 + (
    -0.11445496716294967 + m.x290)**2 + (-0.9526471232336744 + m.x291)**2 + (
    -0.29191369035574544 + m.x292)**2 + (-0.5653246839270838 + m.x293)**2) +
    m.x132 - 2.23606797749979 * m.b470 >= -2.23606797749979)
m.e133 = Constraint(expr= -sqrt((-0.21125847741287684 + m.x289)**2 + (
    -0.24527434539791804 + m.x290)**2 + (-0.6289970479606978 + m.x291)**2 + (
    -0.7068457529300446 + m.x292)**2 + (-0.7943561377121612 + m.x293)**2) +
    m.x133 - 2.23606797749979 * m.b471 >= -2.23606797749979)
m.e134 = Constraint(expr= -sqrt((-0.9522420339595141 + m.x289)**2 + (
    -0.9326354363859527 + m.x290)**2 + (-0.4449382446418748 + m.x291)**2 + (
    -0.018772017414026565 + m.x292)**2 + (-0.1570753065990531 + m.x293)**2) +
    m.x134 - 2.23606797749979 * m.b472 >= -2.23606797749979)
m.e135 = Constraint(expr= -sqrt((-0.8796213188443197 + m.x289)**2 + (
    -0.9757325913906182 + m.x290)**2 + (-0.5478578093651233 + m.x291)**2 + (
    -0.00973548730106566 + m.x292)**2 + (-0.27048086044812103 + m.x293)**2) +
    m.x135 - 2.23606797749979 * m.b473 >= -2.23606797749979)
m.e136 = Constraint(expr= -sqrt((-0.7382526421375969 + m.x289)**2 + (
    -0.18734997029644274 + m.x290)**2 + (-0.2597432271723712 + m.x291)**2 + (
    -0.42962015792230956 + m.x292)**2 + (-0.7073477915737445 + m.x293)**2) +
    m.x136 - 2.23606797749979 * m.b474 >= -2.23606797749979)
m.e137 = Constraint(expr= -sqrt((-0.7480253586345234 + m.x289)**2 + (
    -0.39775488720466023 + m.x290)**2 + (-0.3653805995645427 + m.x291)**2 + (
    -0.5146776625112836 + m.x292)**2 + (-0.46172129982047827 + m.x293)**2) +
    m.x137 - 2.23606797749979 * m.b475 >= -2.23606797749979)
m.e138 = Constraint(expr= -sqrt((-0.9807955797704826 + m.x289)**2 + (
    -0.09734685184548297 + m.x290)**2 + (-0.38645671601793696 + m.x291)**2 + (
    -0.33263947083044576 + m.x292)**2 + (-0.5052803496499273 + m.x293)**2) +
    m.x138 - 2.23606797749979 * m.b476 >= -2.23606797749979)
m.e139 = Constraint(expr= -sqrt((-0.45084513414500904 + m.x294)**2 + (
    -0.4366195682760844 + m.x295)**2 + (-0.04163444585203002 + m.x296)**2 + (
    -0.7676272579584664 + m.x297)**2 + (-0.6734553564483233 + m.x298)**2) +
    m.x139 - 2.23606797749979 * m.b477 >= -2.23606797749979)
m.e140 = Constraint(expr= -sqrt((-0.670857540712527 + m.x294)**2 + (
    -0.472665488047444 + m.x295)**2 + (-0.672731114024884 + m.x296)**2 + (
    -0.8824812534975449 + m.x297)**2 + (-0.6920224414883532 + m.x298)**2) +
    m.x140 - 2.23606797749979 * m.b478 >= -2.23606797749979)
m.e141 = Constraint(expr= -sqrt((-0.3456424258652263 + m.x294)**2 + (
    -0.897323531600062 + m.x295)**2 + (-0.3169943908371815 + m.x296)**2 + (
    -0.08378401217902964 + m.x297)**2 + (-0.2511840930177276 + m.x298)**2) +
    m.x141 - 2.23606797749979 * m.b479 >= -2.23606797749979)
m.e142 = Constraint(expr= -sqrt((-0.49653521716587157 + m.x294)**2 + (
    -0.8612924863730758 + m.x295)**2 + (-0.3477168575425721 + m.x296)**2 + (
    -0.6615424192381595 + m.x297)**2 + (-0.2680635035686557 + m.x298)**2) +
    m.x142 - 2.23606797749979 * m.b480 >= -2.23606797749979)
m.e143 = Constraint(expr= -sqrt((-0.027492190735120214 + m.x294)**2 + (
    -0.975830678205581 + m.x295)**2 + (-0.5725079974762737 + m.x296)**2 + (
    -0.4627928206739904 + m.x297)**2 + (-0.676105217625283 + m.x298)**2) +
    m.x143 - 2.23606797749979 * m.b481 >= -2.23606797749979)
m.e144 = Constraint(expr= -sqrt((-0.13167765137927434 + m.x294)**2 + (
    -0.8772422533001436 + m.x295)**2 + (-0.30212459335273456 + m.x296)**2 + (
    -0.9589299306054163 + m.x297)**2 + (-0.1684676992378059 + m.x298)**2) +
    m.x144 - 2.23606797749979 * m.b482 >= -2.23606797749979)
m.e145 = Constraint(expr= -sqrt((-0.4631605820201776 + m.x294)**2 + (
    -0.3075046464306209 + m.x295)**2 + (-0.6161047422348818 + m.x296)**2 + (
    -0.06036679498995601 + m.x297)**2 + (-0.055585229920206314 + m.x298)**2) +
    m.x145 - 2.23606797749979 * m.b483 >= -2.23606797749979)
m.e146 = Constraint(expr= -sqrt((-0.32388656731438237 + m.x294)**2 + (
    -0.05792786993199972 + m.x295)**2 + (-0.8135525615007164 + m.x296)**2 + (
    -0.11918904488489845 + m.x297)**2 + (-0.3074172166187361 + m.x298)**2) +
    m.x146 - 2.23606797749979 * m.b484 >= -2.23606797749979)
m.e147 = Constraint(expr= -sqrt((-0.5224218716951496 + m.x294)**2 + (
    -0.11445496716294967 + m.x295)**2 + (-0.9526471232336744 + m.x296)**2 + (
    -0.29191369035574544 + m.x297)**2 + (-0.5653246839270838 + m.x298)**2) +
    m.x147 - 2.23606797749979 * m.b485 >= -2.23606797749979)
m.e148 = Constraint(expr= -sqrt((-0.21125847741287684 + m.x294)**2 + (
    -0.24527434539791804 + m.x295)**2 + (-0.6289970479606978 + m.x296)**2 + (
    -0.7068457529300446 + m.x297)**2 + (-0.7943561377121612 + m.x298)**2) +
    m.x148 - 2.23606797749979 * m.b486 >= -2.23606797749979)
m.e149 = Constraint(expr= -sqrt((-0.9522420339595141 + m.x294)**2 + (
    -0.9326354363859527 + m.x295)**2 + (-0.4449382446418748 + m.x296)**2 + (
    -0.018772017414026565 + m.x297)**2 + (-0.1570753065990531 + m.x298)**2) +
    m.x149 - 2.23606797749979 * m.b487 >= -2.23606797749979)
m.e150 = Constraint(expr= -sqrt((-0.8796213188443197 + m.x294)**2 + (
    -0.9757325913906182 + m.x295)**2 + (-0.5478578093651233 + m.x296)**2 + (
    -0.00973548730106566 + m.x297)**2 + (-0.27048086044812103 + m.x298)**2) +
    m.x150 - 2.23606797749979 * m.b488 >= -2.23606797749979)
m.e151 = Constraint(expr= -sqrt((-0.7382526421375969 + m.x294)**2 + (
    -0.18734997029644274 + m.x295)**2 + (-0.2597432271723712 + m.x296)**2 + (
    -0.42962015792230956 + m.x297)**2 + (-0.7073477915737445 + m.x298)**2) +
    m.x151 - 2.23606797749979 * m.b489 >= -2.23606797749979)
m.e152 = Constraint(expr= -sqrt((-0.7480253586345234 + m.x294)**2 + (
    -0.39775488720466023 + m.x295)**2 + (-0.3653805995645427 + m.x296)**2 + (
    -0.5146776625112836 + m.x297)**2 + (-0.46172129982047827 + m.x298)**2) +
    m.x152 - 2.23606797749979 * m.b490 >= -2.23606797749979)
m.e153 = Constraint(expr= -sqrt((-0.9807955797704826 + m.x294)**2 + (
    -0.09734685184548297 + m.x295)**2 + (-0.38645671601793696 + m.x296)**2 + (
    -0.33263947083044576 + m.x297)**2 + (-0.5052803496499273 + m.x298)**2) +
    m.x153 - 2.23606797749979 * m.b491 >= -2.23606797749979)
m.e154 = Constraint(expr= -sqrt((-0.45084513414500904 + m.x299)**2 + (
    -0.4366195682760844 + m.x300)**2 + (-0.04163444585203002 + m.x301)**2 + (
    -0.7676272579584664 + m.x302)**2 + (-0.6734553564483233 + m.x303)**2) +
    m.x154 - 2.23606797749979 * m.b492 >= -2.23606797749979)
m.e155 = Constraint(expr= -sqrt((-0.670857540712527 + m.x299)**2 + (
    -0.472665488047444 + m.x300)**2 + (-0.672731114024884 + m.x301)**2 + (
    -0.8824812534975449 + m.x302)**2 + (-0.6920224414883532 + m.x303)**2) +
    m.x155 - 2.23606797749979 * m.b493 >= -2.23606797749979)
m.e156 = Constraint(expr= -sqrt((-0.3456424258652263 + m.x299)**2 + (
    -0.897323531600062 + m.x300)**2 + (-0.3169943908371815 + m.x301)**2 + (
    -0.08378401217902964 + m.x302)**2 + (-0.2511840930177276 + m.x303)**2) +
    m.x156 - 2.23606797749979 * m.b494 >= -2.23606797749979)
m.e157 = Constraint(expr= -sqrt((-0.49653521716587157 + m.x299)**2 + (
    -0.8612924863730758 + m.x300)**2 + (-0.3477168575425721 + m.x301)**2 + (
    -0.6615424192381595 + m.x302)**2 + (-0.2680635035686557 + m.x303)**2) +
    m.x157 - 2.23606797749979 * m.b495 >= -2.23606797749979)
m.e158 = Constraint(expr= -sqrt((-0.027492190735120214 + m.x299)**2 + (
    -0.975830678205581 + m.x300)**2 + (-0.5725079974762737 + m.x301)**2 + (
    -0.4627928206739904 + m.x302)**2 + (-0.676105217625283 + m.x303)**2) +
    m.x158 - 2.23606797749979 * m.b496 >= -2.23606797749979)
m.e159 = Constraint(expr= -sqrt((-0.13167765137927434 + m.x299)**2 + (
    -0.8772422533001436 + m.x300)**2 + (-0.30212459335273456 + m.x301)**2 + (
    -0.9589299306054163 + m.x302)**2 + (-0.1684676992378059 + m.x303)**2) +
    m.x159 - 2.23606797749979 * m.b497 >= -2.23606797749979)
m.e160 = Constraint(expr= -sqrt((-0.4631605820201776 + m.x299)**2 + (
    -0.3075046464306209 + m.x300)**2 + (-0.6161047422348818 + m.x301)**2 + (
    -0.06036679498995601 + m.x302)**2 + (-0.055585229920206314 + m.x303)**2) +
    m.x160 - 2.23606797749979 * m.b498 >= -2.23606797749979)
m.e161 = Constraint(expr= -sqrt((-0.32388656731438237 + m.x299)**2 + (
    -0.05792786993199972 + m.x300)**2 + (-0.8135525615007164 + m.x301)**2 + (
    -0.11918904488489845 + m.x302)**2 + (-0.3074172166187361 + m.x303)**2) +
    m.x161 - 2.23606797749979 * m.b499 >= -2.23606797749979)
m.e162 = Constraint(expr= -sqrt((-0.5224218716951496 + m.x299)**2 + (
    -0.11445496716294967 + m.x300)**2 + (-0.9526471232336744 + m.x301)**2 + (
    -0.29191369035574544 + m.x302)**2 + (-0.5653246839270838 + m.x303)**2) +
    m.x162 - 2.23606797749979 * m.b500 >= -2.23606797749979)
m.e163 = Constraint(expr= -sqrt((-0.21125847741287684 + m.x299)**2 + (
    -0.24527434539791804 + m.x300)**2 + (-0.6289970479606978 + m.x301)**2 + (
    -0.7068457529300446 + m.x302)**2 + (-0.7943561377121612 + m.x303)**2) +
    m.x163 - 2.23606797749979 * m.b501 >= -2.23606797749979)
m.e164 = Constraint(expr= -sqrt((-0.9522420339595141 + m.x299)**2 + (
    -0.9326354363859527 + m.x300)**2 + (-0.4449382446418748 + m.x301)**2 + (
    -0.018772017414026565 + m.x302)**2 + (-0.1570753065990531 + m.x303)**2) +
    m.x164 - 2.23606797749979 * m.b502 >= -2.23606797749979)
m.e165 = Constraint(expr= -sqrt((-0.8796213188443197 + m.x299)**2 + (
    -0.9757325913906182 + m.x300)**2 + (-0.5478578093651233 + m.x301)**2 + (
    -0.00973548730106566 + m.x302)**2 + (-0.27048086044812103 + m.x303)**2) +
    m.x165 - 2.23606797749979 * m.b503 >= -2.23606797749979)
m.e166 = Constraint(expr= -sqrt((-0.7382526421375969 + m.x299)**2 + (
    -0.18734997029644274 + m.x300)**2 + (-0.2597432271723712 + m.x301)**2 + (
    -0.42962015792230956 + m.x302)**2 + (-0.7073477915737445 + m.x303)**2) +
    m.x166 - 2.23606797749979 * m.b504 >= -2.23606797749979)
m.e167 = Constraint(expr= -sqrt((-0.7480253586345234 + m.x299)**2 + (
    -0.39775488720466023 + m.x300)**2 + (-0.3653805995645427 + m.x301)**2 + (
    -0.5146776625112836 + m.x302)**2 + (-0.46172129982047827 + m.x303)**2) +
    m.x167 - 2.23606797749979 * m.b505 >= -2.23606797749979)
m.e168 = Constraint(expr= -sqrt((-0.9807955797704826 + m.x299)**2 + (
    -0.09734685184548297 + m.x300)**2 + (-0.38645671601793696 + m.x301)**2 + (
    -0.33263947083044576 + m.x302)**2 + (-0.5052803496499273 + m.x303)**2) +
    m.x168 - 2.23606797749979 * m.b506 >= -2.23606797749979)
m.e169 = Constraint(expr= -sqrt((-0.45084513414500904 + m.x304)**2 + (
    -0.4366195682760844 + m.x305)**2 + (-0.04163444585203002 + m.x306)**2 + (
    -0.7676272579584664 + m.x307)**2 + (-0.6734553564483233 + m.x308)**2) +
    m.x169 - 2.23606797749979 * m.b507 >= -2.23606797749979)
m.e170 = Constraint(expr= -sqrt((-0.670857540712527 + m.x304)**2 + (
    -0.472665488047444 + m.x305)**2 + (-0.672731114024884 + m.x306)**2 + (
    -0.8824812534975449 + m.x307)**2 + (-0.6920224414883532 + m.x308)**2) +
    m.x170 - 2.23606797749979 * m.b508 >= -2.23606797749979)
m.e171 = Constraint(expr= -sqrt((-0.3456424258652263 + m.x304)**2 + (
    -0.897323531600062 + m.x305)**2 + (-0.3169943908371815 + m.x306)**2 + (
    -0.08378401217902964 + m.x307)**2 + (-0.2511840930177276 + m.x308)**2) +
    m.x171 - 2.23606797749979 * m.b509 >= -2.23606797749979)
m.e172 = Constraint(expr= -sqrt((-0.49653521716587157 + m.x304)**2 + (
    -0.8612924863730758 + m.x305)**2 + (-0.3477168575425721 + m.x306)**2 + (
    -0.6615424192381595 + m.x307)**2 + (-0.2680635035686557 + m.x308)**2) +
    m.x172 - 2.23606797749979 * m.b510 >= -2.23606797749979)
m.e173 = Constraint(expr= -sqrt((-0.027492190735120214 + m.x304)**2 + (
    -0.975830678205581 + m.x305)**2 + (-0.5725079974762737 + m.x306)**2 + (
    -0.4627928206739904 + m.x307)**2 + (-0.676105217625283 + m.x308)**2) +
    m.x173 - 2.23606797749979 * m.b511 >= -2.23606797749979)
m.e174 = Constraint(expr= -sqrt((-0.13167765137927434 + m.x304)**2 + (
    -0.8772422533001436 + m.x305)**2 + (-0.30212459335273456 + m.x306)**2 + (
    -0.9589299306054163 + m.x307)**2 + (-0.1684676992378059 + m.x308)**2) +
    m.x174 - 2.23606797749979 * m.b512 >= -2.23606797749979)
m.e175 = Constraint(expr= -sqrt((-0.4631605820201776 + m.x304)**2 + (
    -0.3075046464306209 + m.x305)**2 + (-0.6161047422348818 + m.x306)**2 + (
    -0.06036679498995601 + m.x307)**2 + (-0.055585229920206314 + m.x308)**2) +
    m.x175 - 2.23606797749979 * m.b513 >= -2.23606797749979)
m.e176 = Constraint(expr= -sqrt((-0.32388656731438237 + m.x304)**2 + (
    -0.05792786993199972 + m.x305)**2 + (-0.8135525615007164 + m.x306)**2 + (
    -0.11918904488489845 + m.x307)**2 + (-0.3074172166187361 + m.x308)**2) +
    m.x176 - 2.23606797749979 * m.b514 >= -2.23606797749979)
m.e177 = Constraint(expr= -sqrt((-0.5224218716951496 + m.x304)**2 + (
    -0.11445496716294967 + m.x305)**2 + (-0.9526471232336744 + m.x306)**2 + (
    -0.29191369035574544 + m.x307)**2 + (-0.5653246839270838 + m.x308)**2) +
    m.x177 - 2.23606797749979 * m.b515 >= -2.23606797749979)
m.e178 = Constraint(expr= -sqrt((-0.21125847741287684 + m.x304)**2 + (
    -0.24527434539791804 + m.x305)**2 + (-0.6289970479606978 + m.x306)**2 + (
    -0.7068457529300446 + m.x307)**2 + (-0.7943561377121612 + m.x308)**2) +
    m.x178 - 2.23606797749979 * m.b516 >= -2.23606797749979)
m.e179 = Constraint(expr= -sqrt((-0.9522420339595141 + m.x304)**2 + (
    -0.9326354363859527 + m.x305)**2 + (-0.4449382446418748 + m.x306)**2 + (
    -0.018772017414026565 + m.x307)**2 + (-0.1570753065990531 + m.x308)**2) +
    m.x179 - 2.23606797749979 * m.b517 >= -2.23606797749979)
m.e180 = Constraint(expr= -sqrt((-0.8796213188443197 + m.x304)**2 + (
    -0.9757325913906182 + m.x305)**2 + (-0.5478578093651233 + m.x306)**2 + (
    -0.00973548730106566 + m.x307)**2 + (-0.27048086044812103 + m.x308)**2) +
    m.x180 - 2.23606797749979 * m.b518 >= -2.23606797749979)
m.e181 = Constraint(expr= -sqrt((-0.7382526421375969 + m.x304)**2 + (
    -0.18734997029644274 + m.x305)**2 + (-0.2597432271723712 + m.x306)**2 + (
    -0.42962015792230956 + m.x307)**2 + (-0.7073477915737445 + m.x308)**2) +
    m.x181 - 2.23606797749979 * m.b519 >= -2.23606797749979)
m.e182 = Constraint(expr= -sqrt((-0.7480253586345234 + m.x304)**2 + (
    -0.39775488720466023 + m.x305)**2 + (-0.3653805995645427 + m.x306)**2 + (
    -0.5146776625112836 + m.x307)**2 + (-0.46172129982047827 + m.x308)**2) +
    m.x182 - 2.23606797749979 * m.b520 >= -2.23606797749979)
m.e183 = Constraint(expr= -sqrt((-0.9807955797704826 + m.x304)**2 + (
    -0.09734685184548297 + m.x305)**2 + (-0.38645671601793696 + m.x306)**2 + (
    -0.33263947083044576 + m.x307)**2 + (-0.5052803496499273 + m.x308)**2) +
    m.x183 - 2.23606797749979 * m.b521 >= -2.23606797749979)
m.e184 = Constraint(expr= -sqrt((-0.45084513414500904 + m.x309)**2 + (
    -0.4366195682760844 + m.x310)**2 + (-0.04163444585203002 + m.x311)**2 + (
    -0.7676272579584664 + m.x312)**2 + (-0.6734553564483233 + m.x313)**2) +
    m.x184 - 2.23606797749979 * m.b522 >= -2.23606797749979)
m.e185 = Constraint(expr= -sqrt((-0.670857540712527 + m.x309)**2 + (
    -0.472665488047444 + m.x310)**2 + (-0.672731114024884 + m.x311)**2 + (
    -0.8824812534975449 + m.x312)**2 + (-0.6920224414883532 + m.x313)**2) +
    m.x185 - 2.23606797749979 * m.b523 >= -2.23606797749979)
m.e186 = Constraint(expr= -sqrt((-0.3456424258652263 + m.x309)**2 + (
    -0.897323531600062 + m.x310)**2 + (-0.3169943908371815 + m.x311)**2 + (
    -0.08378401217902964 + m.x312)**2 + (-0.2511840930177276 + m.x313)**2) +
    m.x186 - 2.23606797749979 * m.b524 >= -2.23606797749979)
m.e187 = Constraint(expr= -sqrt((-0.49653521716587157 + m.x309)**2 + (
    -0.8612924863730758 + m.x310)**2 + (-0.3477168575425721 + m.x311)**2 + (
    -0.6615424192381595 + m.x312)**2 + (-0.2680635035686557 + m.x313)**2) +
    m.x187 - 2.23606797749979 * m.b525 >= -2.23606797749979)
m.e188 = Constraint(expr= -sqrt((-0.027492190735120214 + m.x309)**2 + (
    -0.975830678205581 + m.x310)**2 + (-0.5725079974762737 + m.x311)**2 + (
    -0.4627928206739904 + m.x312)**2 + (-0.676105217625283 + m.x313)**2) +
    m.x188 - 2.23606797749979 * m.b526 >= -2.23606797749979)
m.e189 = Constraint(expr= -sqrt((-0.13167765137927434 + m.x309)**2 + (
    -0.8772422533001436 + m.x310)**2 + (-0.30212459335273456 + m.x311)**2 + (
    -0.9589299306054163 + m.x312)**2 + (-0.1684676992378059 + m.x313)**2) +
    m.x189 - 2.23606797749979 * m.b527 >= -2.23606797749979)
m.e190 = Constraint(expr= -sqrt((-0.4631605820201776 + m.x309)**2 + (
    -0.3075046464306209 + m.x310)**2 + (-0.6161047422348818 + m.x311)**2 + (
    -0.06036679498995601 + m.x312)**2 + (-0.055585229920206314 + m.x313)**2) +
    m.x190 - 2.23606797749979 * m.b528 >= -2.23606797749979)
m.e191 = Constraint(expr= -sqrt((-0.32388656731438237 + m.x309)**2 + (
    -0.05792786993199972 + m.x310)**2 + (-0.8135525615007164 + m.x311)**2 + (
    -0.11918904488489845 + m.x312)**2 + (-0.3074172166187361 + m.x313)**2) +
    m.x191 - 2.23606797749979 * m.b529 >= -2.23606797749979)
m.e192 = Constraint(expr= -sqrt((-0.5224218716951496 + m.x309)**2 + (
    -0.11445496716294967 + m.x310)**2 + (-0.9526471232336744 + m.x311)**2 + (
    -0.29191369035574544 + m.x312)**2 + (-0.5653246839270838 + m.x313)**2) +
    m.x192 - 2.23606797749979 * m.b530 >= -2.23606797749979)
m.e193 = Constraint(expr= -sqrt((-0.21125847741287684 + m.x309)**2 + (
    -0.24527434539791804 + m.x310)**2 + (-0.6289970479606978 + m.x311)**2 + (
    -0.7068457529300446 + m.x312)**2 + (-0.7943561377121612 + m.x313)**2) +
    m.x193 - 2.23606797749979 * m.b531 >= -2.23606797749979)
m.e194 = Constraint(expr= -sqrt((-0.9522420339595141 + m.x309)**2 + (
    -0.9326354363859527 + m.x310)**2 + (-0.4449382446418748 + m.x311)**2 + (
    -0.018772017414026565 + m.x312)**2 + (-0.1570753065990531 + m.x313)**2) +
    m.x194 - 2.23606797749979 * m.b532 >= -2.23606797749979)
m.e195 = Constraint(expr= -sqrt((-0.8796213188443197 + m.x309)**2 + (
    -0.9757325913906182 + m.x310)**2 + (-0.5478578093651233 + m.x311)**2 + (
    -0.00973548730106566 + m.x312)**2 + (-0.27048086044812103 + m.x313)**2) +
    m.x195 - 2.23606797749979 * m.b533 >= -2.23606797749979)
m.e196 = Constraint(expr= -sqrt((-0.7382526421375969 + m.x309)**2 + (
    -0.18734997029644274 + m.x310)**2 + (-0.2597432271723712 + m.x311)**2 + (
    -0.42962015792230956 + m.x312)**2 + (-0.7073477915737445 + m.x313)**2) +
    m.x196 - 2.23606797749979 * m.b534 >= -2.23606797749979)
m.e197 = Constraint(expr= -sqrt((-0.7480253586345234 + m.x309)**2 + (
    -0.39775488720466023 + m.x310)**2 + (-0.3653805995645427 + m.x311)**2 + (
    -0.5146776625112836 + m.x312)**2 + (-0.46172129982047827 + m.x313)**2) +
    m.x197 - 2.23606797749979 * m.b535 >= -2.23606797749979)
m.e198 = Constraint(expr= -sqrt((-0.9807955797704826 + m.x309)**2 + (
    -0.09734685184548297 + m.x310)**2 + (-0.38645671601793696 + m.x311)**2 + (
    -0.33263947083044576 + m.x312)**2 + (-0.5052803496499273 + m.x313)**2) +
    m.x198 - 2.23606797749979 * m.b536 >= -2.23606797749979)
m.e199 = Constraint(expr= -sqrt((-0.45084513414500904 + m.x314)**2 + (
    -0.4366195682760844 + m.x315)**2 + (-0.04163444585203002 + m.x316)**2 + (
    -0.7676272579584664 + m.x317)**2 + (-0.6734553564483233 + m.x318)**2) +
    m.x199 - 2.23606797749979 * m.b537 >= -2.23606797749979)
m.e200 = Constraint(expr= -sqrt((-0.670857540712527 + m.x314)**2 + (
    -0.472665488047444 + m.x315)**2 + (-0.672731114024884 + m.x316)**2 + (
    -0.8824812534975449 + m.x317)**2 + (-0.6920224414883532 + m.x318)**2) +
    m.x200 - 2.23606797749979 * m.b538 >= -2.23606797749979)
m.e201 = Constraint(expr= -sqrt((-0.3456424258652263 + m.x314)**2 + (
    -0.897323531600062 + m.x315)**2 + (-0.3169943908371815 + m.x316)**2 + (
    -0.08378401217902964 + m.x317)**2 + (-0.2511840930177276 + m.x318)**2) +
    m.x201 - 2.23606797749979 * m.b539 >= -2.23606797749979)
m.e202 = Constraint(expr= -sqrt((-0.49653521716587157 + m.x314)**2 + (
    -0.8612924863730758 + m.x315)**2 + (-0.3477168575425721 + m.x316)**2 + (
    -0.6615424192381595 + m.x317)**2 + (-0.2680635035686557 + m.x318)**2) +
    m.x202 - 2.23606797749979 * m.b540 >= -2.23606797749979)
m.e203 = Constraint(expr= -sqrt((-0.027492190735120214 + m.x314)**2 + (
    -0.975830678205581 + m.x315)**2 + (-0.5725079974762737 + m.x316)**2 + (
    -0.4627928206739904 + m.x317)**2 + (-0.676105217625283 + m.x318)**2) +
    m.x203 - 2.23606797749979 * m.b541 >= -2.23606797749979)
m.e204 = Constraint(expr= -sqrt((-0.13167765137927434 + m.x314)**2 + (
    -0.8772422533001436 + m.x315)**2 + (-0.30212459335273456 + m.x316)**2 + (
    -0.9589299306054163 + m.x317)**2 + (-0.1684676992378059 + m.x318)**2) +
    m.x204 - 2.23606797749979 * m.b542 >= -2.23606797749979)
m.e205 = Constraint(expr= -sqrt((-0.4631605820201776 + m.x314)**2 + (
    -0.3075046464306209 + m.x315)**2 + (-0.6161047422348818 + m.x316)**2 + (
    -0.06036679498995601 + m.x317)**2 + (-0.055585229920206314 + m.x318)**2) +
    m.x205 - 2.23606797749979 * m.b543 >= -2.23606797749979)
m.e206 = Constraint(expr= -sqrt((-0.32388656731438237 + m.x314)**2 + (
    -0.05792786993199972 + m.x315)**2 + (-0.8135525615007164 + m.x316)**2 + (
    -0.11918904488489845 + m.x317)**2 + (-0.3074172166187361 + m.x318)**2) +
    m.x206 - 2.23606797749979 * m.b544 >= -2.23606797749979)
m.e207 = Constraint(expr= -sqrt((-0.5224218716951496 + m.x314)**2 + (
    -0.11445496716294967 + m.x315)**2 + (-0.9526471232336744 + m.x316)**2 + (
    -0.29191369035574544 + m.x317)**2 + (-0.5653246839270838 + m.x318)**2) +
    m.x207 - 2.23606797749979 * m.b545 >= -2.23606797749979)
m.e208 = Constraint(expr= -sqrt((-0.21125847741287684 + m.x314)**2 + (
    -0.24527434539791804 + m.x315)**2 + (-0.6289970479606978 + m.x316)**2 + (
    -0.7068457529300446 + m.x317)**2 + (-0.7943561377121612 + m.x318)**2) +
    m.x208 - 2.23606797749979 * m.b546 >= -2.23606797749979)
m.e209 = Constraint(expr= -sqrt((-0.9522420339595141 + m.x314)**2 + (
    -0.9326354363859527 + m.x315)**2 + (-0.4449382446418748 + m.x316)**2 + (
    -0.018772017414026565 + m.x317)**2 + (-0.1570753065990531 + m.x318)**2) +
    m.x209 - 2.23606797749979 * m.b547 >= -2.23606797749979)
m.e210 = Constraint(expr= -sqrt((-0.8796213188443197 + m.x314)**2 + (
    -0.9757325913906182 + m.x315)**2 + (-0.5478578093651233 + m.x316)**2 + (
    -0.00973548730106566 + m.x317)**2 + (-0.27048086044812103 + m.x318)**2) +
    m.x210 - 2.23606797749979 * m.b548 >= -2.23606797749979)
m.e211 = Constraint(expr= -sqrt((-0.7382526421375969 + m.x314)**2 + (
    -0.18734997029644274 + m.x315)**2 + (-0.2597432271723712 + m.x316)**2 + (
    -0.42962015792230956 + m.x317)**2 + (-0.7073477915737445 + m.x318)**2) +
    m.x211 - 2.23606797749979 * m.b549 >= -2.23606797749979)
m.e212 = Constraint(expr= -sqrt((-0.7480253586345234 + m.x314)**2 + (
    -0.39775488720466023 + m.x315)**2 + (-0.3653805995645427 + m.x316)**2 + (
    -0.5146776625112836 + m.x317)**2 + (-0.46172129982047827 + m.x318)**2) +
    m.x212 - 2.23606797749979 * m.b550 >= -2.23606797749979)
m.e213 = Constraint(expr= -sqrt((-0.9807955797704826 + m.x314)**2 + (
    -0.09734685184548297 + m.x315)**2 + (-0.38645671601793696 + m.x316)**2 + (
    -0.33263947083044576 + m.x317)**2 + (-0.5052803496499273 + m.x318)**2) +
    m.x213 - 2.23606797749979 * m.b551 >= -2.23606797749979)
m.e214 = Constraint(expr= -sqrt((-0.45084513414500904 + m.x319)**2 + (
    -0.4366195682760844 + m.x320)**2 + (-0.04163444585203002 + m.x321)**2 + (
    -0.7676272579584664 + m.x322)**2 + (-0.6734553564483233 + m.x323)**2) +
    m.x214 - 2.23606797749979 * m.b552 >= -2.23606797749979)
m.e215 = Constraint(expr= -sqrt((-0.670857540712527 + m.x319)**2 + (
    -0.472665488047444 + m.x320)**2 + (-0.672731114024884 + m.x321)**2 + (
    -0.8824812534975449 + m.x322)**2 + (-0.6920224414883532 + m.x323)**2) +
    m.x215 - 2.23606797749979 * m.b553 >= -2.23606797749979)
m.e216 = Constraint(expr= -sqrt((-0.3456424258652263 + m.x319)**2 + (
    -0.897323531600062 + m.x320)**2 + (-0.3169943908371815 + m.x321)**2 + (
    -0.08378401217902964 + m.x322)**2 + (-0.2511840930177276 + m.x323)**2) +
    m.x216 - 2.23606797749979 * m.b554 >= -2.23606797749979)
m.e217 = Constraint(expr= -sqrt((-0.49653521716587157 + m.x319)**2 + (
    -0.8612924863730758 + m.x320)**2 + (-0.3477168575425721 + m.x321)**2 + (
    -0.6615424192381595 + m.x322)**2 + (-0.2680635035686557 + m.x323)**2) +
    m.x217 - 2.23606797749979 * m.b555 >= -2.23606797749979)
m.e218 = Constraint(expr= -sqrt((-0.027492190735120214 + m.x319)**2 + (
    -0.975830678205581 + m.x320)**2 + (-0.5725079974762737 + m.x321)**2 + (
    -0.4627928206739904 + m.x322)**2 + (-0.676105217625283 + m.x323)**2) +
    m.x218 - 2.23606797749979 * m.b556 >= -2.23606797749979)
m.e219 = Constraint(expr= -sqrt((-0.13167765137927434 + m.x319)**2 + (
    -0.8772422533001436 + m.x320)**2 + (-0.30212459335273456 + m.x321)**2 + (
    -0.9589299306054163 + m.x322)**2 + (-0.1684676992378059 + m.x323)**2) +
    m.x219 - 2.23606797749979 * m.b557 >= -2.23606797749979)
m.e220 = Constraint(expr= -sqrt((-0.4631605820201776 + m.x319)**2 + (
    -0.3075046464306209 + m.x320)**2 + (-0.6161047422348818 + m.x321)**2 + (
    -0.06036679498995601 + m.x322)**2 + (-0.055585229920206314 + m.x323)**2) +
    m.x220 - 2.23606797749979 * m.b558 >= -2.23606797749979)
m.e221 = Constraint(expr= -sqrt((-0.32388656731438237 + m.x319)**2 + (
    -0.05792786993199972 + m.x320)**2 + (-0.8135525615007164 + m.x321)**2 + (
    -0.11918904488489845 + m.x322)**2 + (-0.3074172166187361 + m.x323)**2) +
    m.x221 - 2.23606797749979 * m.b559 >= -2.23606797749979)
m.e222 = Constraint(expr= -sqrt((-0.5224218716951496 + m.x319)**2 + (
    -0.11445496716294967 + m.x320)**2 + (-0.9526471232336744 + m.x321)**2 + (
    -0.29191369035574544 + m.x322)**2 + (-0.5653246839270838 + m.x323)**2) +
    m.x222 - 2.23606797749979 * m.b560 >= -2.23606797749979)
m.e223 = Constraint(expr= -sqrt((-0.21125847741287684 + m.x319)**2 + (
    -0.24527434539791804 + m.x320)**2 + (-0.6289970479606978 + m.x321)**2 + (
    -0.7068457529300446 + m.x322)**2 + (-0.7943561377121612 + m.x323)**2) +
    m.x223 - 2.23606797749979 * m.b561 >= -2.23606797749979)
m.e224 = Constraint(expr= -sqrt((-0.9522420339595141 + m.x319)**2 + (
    -0.9326354363859527 + m.x320)**2 + (-0.4449382446418748 + m.x321)**2 + (
    -0.018772017414026565 + m.x322)**2 + (-0.1570753065990531 + m.x323)**2) +
    m.x224 - 2.23606797749979 * m.b562 >= -2.23606797749979)
m.e225 = Constraint(expr= -sqrt((-0.8796213188443197 + m.x319)**2 + (
    -0.9757325913906182 + m.x320)**2 + (-0.5478578093651233 + m.x321)**2 + (
    -0.00973548730106566 + m.x322)**2 + (-0.27048086044812103 + m.x323)**2) +
    m.x225 - 2.23606797749979 * m.b563 >= -2.23606797749979)
m.e226 = Constraint(expr= -sqrt((-0.7382526421375969 + m.x319)**2 + (
    -0.18734997029644274 + m.x320)**2 + (-0.2597432271723712 + m.x321)**2 + (
    -0.42962015792230956 + m.x322)**2 + (-0.7073477915737445 + m.x323)**2) +
    m.x226 - 2.23606797749979 * m.b564 >= -2.23606797749979)
m.e227 = Constraint(expr= -sqrt((-0.7480253586345234 + m.x319)**2 + (
    -0.39775488720466023 + m.x320)**2 + (-0.3653805995645427 + m.x321)**2 + (
    -0.5146776625112836 + m.x322)**2 + (-0.46172129982047827 + m.x323)**2) +
    m.x227 - 2.23606797749979 * m.b565 >= -2.23606797749979)
m.e228 = Constraint(expr= -sqrt((-0.9807955797704826 + m.x319)**2 + (
    -0.09734685184548297 + m.x320)**2 + (-0.38645671601793696 + m.x321)**2 + (
    -0.33263947083044576 + m.x322)**2 + (-0.5052803496499273 + m.x323)**2) +
    m.x228 - 2.23606797749979 * m.b566 >= -2.23606797749979)
m.e229 = Constraint(expr= -sqrt((-0.45084513414500904 + m.x324)**2 + (
    -0.4366195682760844 + m.x325)**2 + (-0.04163444585203002 + m.x326)**2 + (
    -0.7676272579584664 + m.x327)**2 + (-0.6734553564483233 + m.x328)**2) +
    m.x229 - 2.23606797749979 * m.b567 >= -2.23606797749979)
m.e230 = Constraint(expr= -sqrt((-0.670857540712527 + m.x324)**2 + (
    -0.472665488047444 + m.x325)**2 + (-0.672731114024884 + m.x326)**2 + (
    -0.8824812534975449 + m.x327)**2 + (-0.6920224414883532 + m.x328)**2) +
    m.x230 - 2.23606797749979 * m.b568 >= -2.23606797749979)
m.e231 = Constraint(expr= -sqrt((-0.3456424258652263 + m.x324)**2 + (
    -0.897323531600062 + m.x325)**2 + (-0.3169943908371815 + m.x326)**2 + (
    -0.08378401217902964 + m.x327)**2 + (-0.2511840930177276 + m.x328)**2) +
    m.x231 - 2.23606797749979 * m.b569 >= -2.23606797749979)
m.e232 = Constraint(expr= -sqrt((-0.49653521716587157 + m.x324)**2 + (
    -0.8612924863730758 + m.x325)**2 + (-0.3477168575425721 + m.x326)**2 + (
    -0.6615424192381595 + m.x327)**2 + (-0.2680635035686557 + m.x328)**2) +
    m.x232 - 2.23606797749979 * m.b570 >= -2.23606797749979)
m.e233 = Constraint(expr= -sqrt((-0.027492190735120214 + m.x324)**2 + (
    -0.975830678205581 + m.x325)**2 + (-0.5725079974762737 + m.x326)**2 + (
    -0.4627928206739904 + m.x327)**2 + (-0.676105217625283 + m.x328)**2) +
    m.x233 - 2.23606797749979 * m.b571 >= -2.23606797749979)
m.e234 = Constraint(expr= -sqrt((-0.13167765137927434 + m.x324)**2 + (
    -0.8772422533001436 + m.x325)**2 + (-0.30212459335273456 + m.x326)**2 + (
    -0.9589299306054163 + m.x327)**2 + (-0.1684676992378059 + m.x328)**2) +
    m.x234 - 2.23606797749979 * m.b572 >= -2.23606797749979)
m.e235 = Constraint(expr= -sqrt((-0.4631605820201776 + m.x324)**2 + (
    -0.3075046464306209 + m.x325)**2 + (-0.6161047422348818 + m.x326)**2 + (
    -0.06036679498995601 + m.x327)**2 + (-0.055585229920206314 + m.x328)**2) +
    m.x235 - 2.23606797749979 * m.b573 >= -2.23606797749979)
m.e236 = Constraint(expr= -sqrt((-0.32388656731438237 + m.x324)**2 + (
    -0.05792786993199972 + m.x325)**2 + (-0.8135525615007164 + m.x326)**2 + (
    -0.11918904488489845 + m.x327)**2 + (-0.3074172166187361 + m.x328)**2) +
    m.x236 - 2.23606797749979 * m.b574 >= -2.23606797749979)
m.e237 = Constraint(expr= -sqrt((-0.5224218716951496 + m.x324)**2 + (
    -0.11445496716294967 + m.x325)**2 + (-0.9526471232336744 + m.x326)**2 + (
    -0.29191369035574544 + m.x327)**2 + (-0.5653246839270838 + m.x328)**2) +
    m.x237 - 2.23606797749979 * m.b575 >= -2.23606797749979)
m.e238 = Constraint(expr= -sqrt((-0.21125847741287684 + m.x324)**2 + (
    -0.24527434539791804 + m.x325)**2 + (-0.6289970479606978 + m.x326)**2 + (
    -0.7068457529300446 + m.x327)**2 + (-0.7943561377121612 + m.x328)**2) +
    m.x238 - 2.23606797749979 * m.b576 >= -2.23606797749979)
m.e239 = Constraint(expr= -sqrt((-0.9522420339595141 + m.x324)**2 + (
    -0.9326354363859527 + m.x325)**2 + (-0.4449382446418748 + m.x326)**2 + (
    -0.018772017414026565 + m.x327)**2 + (-0.1570753065990531 + m.x328)**2) +
    m.x239 - 2.23606797749979 * m.b577 >= -2.23606797749979)
m.e240 = Constraint(expr= -sqrt((-0.8796213188443197 + m.x324)**2 + (
    -0.9757325913906182 + m.x325)**2 + (-0.5478578093651233 + m.x326)**2 + (
    -0.00973548730106566 + m.x327)**2 + (-0.27048086044812103 + m.x328)**2) +
    m.x240 - 2.23606797749979 * m.b578 >= -2.23606797749979)
m.e241 = Constraint(expr= -sqrt((-0.7382526421375969 + m.x324)**2 + (
    -0.18734997029644274 + m.x325)**2 + (-0.2597432271723712 + m.x326)**2 + (
    -0.42962015792230956 + m.x327)**2 + (-0.7073477915737445 + m.x328)**2) +
    m.x241 - 2.23606797749979 * m.b579 >= -2.23606797749979)
m.e242 = Constraint(expr= -sqrt((-0.7480253586345234 + m.x324)**2 + (
    -0.39775488720466023 + m.x325)**2 + (-0.3653805995645427 + m.x326)**2 + (
    -0.5146776625112836 + m.x327)**2 + (-0.46172129982047827 + m.x328)**2) +
    m.x242 - 2.23606797749979 * m.b580 >= -2.23606797749979)
m.e243 = Constraint(expr= -sqrt((-0.9807955797704826 + m.x324)**2 + (
    -0.09734685184548297 + m.x325)**2 + (-0.38645671601793696 + m.x326)**2 + (
    -0.33263947083044576 + m.x327)**2 + (-0.5052803496499273 + m.x328)**2) +
    m.x243 - 2.23606797749979 * m.b581 >= -2.23606797749979)
m.e244 = Constraint(expr= -sqrt((-0.45084513414500904 + m.x329)**2 + (
    -0.4366195682760844 + m.x330)**2 + (-0.04163444585203002 + m.x331)**2 + (
    -0.7676272579584664 + m.x332)**2 + (-0.6734553564483233 + m.x333)**2) +
    m.x244 - 2.23606797749979 * m.b582 >= -2.23606797749979)
m.e245 = Constraint(expr= -sqrt((-0.670857540712527 + m.x329)**2 + (
    -0.472665488047444 + m.x330)**2 + (-0.672731114024884 + m.x331)**2 + (
    -0.8824812534975449 + m.x332)**2 + (-0.6920224414883532 + m.x333)**2) +
    m.x245 - 2.23606797749979 * m.b583 >= -2.23606797749979)
m.e246 = Constraint(expr= -sqrt((-0.3456424258652263 + m.x329)**2 + (
    -0.897323531600062 + m.x330)**2 + (-0.3169943908371815 + m.x331)**2 + (
    -0.08378401217902964 + m.x332)**2 + (-0.2511840930177276 + m.x333)**2) +
    m.x246 - 2.23606797749979 * m.b584 >= -2.23606797749979)
m.e247 = Constraint(expr= -sqrt((-0.49653521716587157 + m.x329)**2 + (
    -0.8612924863730758 + m.x330)**2 + (-0.3477168575425721 + m.x331)**2 + (
    -0.6615424192381595 + m.x332)**2 + (-0.2680635035686557 + m.x333)**2) +
    m.x247 - 2.23606797749979 * m.b585 >= -2.23606797749979)
m.e248 = Constraint(expr= -sqrt((-0.027492190735120214 + m.x329)**2 + (
    -0.975830678205581 + m.x330)**2 + (-0.5725079974762737 + m.x331)**2 + (
    -0.4627928206739904 + m.x332)**2 + (-0.676105217625283 + m.x333)**2) +
    m.x248 - 2.23606797749979 * m.b586 >= -2.23606797749979)
m.e249 = Constraint(expr= -sqrt((-0.13167765137927434 + m.x329)**2 + (
    -0.8772422533001436 + m.x330)**2 + (-0.30212459335273456 + m.x331)**2 + (
    -0.9589299306054163 + m.x332)**2 + (-0.1684676992378059 + m.x333)**2) +
    m.x249 - 2.23606797749979 * m.b587 >= -2.23606797749979)
m.e250 = Constraint(expr= -sqrt((-0.4631605820201776 + m.x329)**2 + (
    -0.3075046464306209 + m.x330)**2 + (-0.6161047422348818 + m.x331)**2 + (
    -0.06036679498995601 + m.x332)**2 + (-0.055585229920206314 + m.x333)**2) +
    m.x250 - 2.23606797749979 * m.b588 >= -2.23606797749979)
m.e251 = Constraint(expr= -sqrt((-0.32388656731438237 + m.x329)**2 + (
    -0.05792786993199972 + m.x330)**2 + (-0.8135525615007164 + m.x331)**2 + (
    -0.11918904488489845 + m.x332)**2 + (-0.3074172166187361 + m.x333)**2) +
    m.x251 - 2.23606797749979 * m.b589 >= -2.23606797749979)
m.e252 = Constraint(expr= -sqrt((-0.5224218716951496 + m.x329)**2 + (
    -0.11445496716294967 + m.x330)**2 + (-0.9526471232336744 + m.x331)**2 + (
    -0.29191369035574544 + m.x332)**2 + (-0.5653246839270838 + m.x333)**2) +
    m.x252 - 2.23606797749979 * m.b590 >= -2.23606797749979)
m.e253 = Constraint(expr= -sqrt((-0.21125847741287684 + m.x329)**2 + (
    -0.24527434539791804 + m.x330)**2 + (-0.6289970479606978 + m.x331)**2 + (
    -0.7068457529300446 + m.x332)**2 + (-0.7943561377121612 + m.x333)**2) +
    m.x253 - 2.23606797749979 * m.b591 >= -2.23606797749979)
m.e254 = Constraint(expr= -sqrt((-0.9522420339595141 + m.x329)**2 + (
    -0.9326354363859527 + m.x330)**2 + (-0.4449382446418748 + m.x331)**2 + (
    -0.018772017414026565 + m.x332)**2 + (-0.1570753065990531 + m.x333)**2) +
    m.x254 - 2.23606797749979 * m.b592 >= -2.23606797749979)
m.e255 = Constraint(expr= -sqrt((-0.8796213188443197 + m.x329)**2 + (
    -0.9757325913906182 + m.x330)**2 + (-0.5478578093651233 + m.x331)**2 + (
    -0.00973548730106566 + m.x332)**2 + (-0.27048086044812103 + m.x333)**2) +
    m.x255 - 2.23606797749979 * m.b593 >= -2.23606797749979)
m.e256 = Constraint(expr= -sqrt((-0.7382526421375969 + m.x329)**2 + (
    -0.18734997029644274 + m.x330)**2 + (-0.2597432271723712 + m.x331)**2 + (
    -0.42962015792230956 + m.x332)**2 + (-0.7073477915737445 + m.x333)**2) +
    m.x256 - 2.23606797749979 * m.b594 >= -2.23606797749979)
m.e257 = Constraint(expr= -sqrt((-0.7480253586345234 + m.x329)**2 + (
    -0.39775488720466023 + m.x330)**2 + (-0.3653805995645427 + m.x331)**2 + (
    -0.5146776625112836 + m.x332)**2 + (-0.46172129982047827 + m.x333)**2) +
    m.x257 - 2.23606797749979 * m.b595 >= -2.23606797749979)
m.e258 = Constraint(expr= -sqrt((-0.9807955797704826 + m.x329)**2 + (
    -0.09734685184548297 + m.x330)**2 + (-0.38645671601793696 + m.x331)**2 + (
    -0.33263947083044576 + m.x332)**2 + (-0.5052803496499273 + m.x333)**2) +
    m.x258 - 2.23606797749979 * m.b596 >= -2.23606797749979)
m.e259 = Constraint(expr= -sqrt((-0.45084513414500904 + m.x334)**2 + (
    -0.4366195682760844 + m.x335)**2 + (-0.04163444585203002 + m.x336)**2 + (
    -0.7676272579584664 + m.x337)**2 + (-0.6734553564483233 + m.x338)**2) +
    m.x259 - 2.23606797749979 * m.b597 >= -2.23606797749979)
m.e260 = Constraint(expr= -sqrt((-0.670857540712527 + m.x334)**2 + (
    -0.472665488047444 + m.x335)**2 + (-0.672731114024884 + m.x336)**2 + (
    -0.8824812534975449 + m.x337)**2 + (-0.6920224414883532 + m.x338)**2) +
    m.x260 - 2.23606797749979 * m.b598 >= -2.23606797749979)
m.e261 = Constraint(expr= -sqrt((-0.3456424258652263 + m.x334)**2 + (
    -0.897323531600062 + m.x335)**2 + (-0.3169943908371815 + m.x336)**2 + (
    -0.08378401217902964 + m.x337)**2 + (-0.2511840930177276 + m.x338)**2) +
    m.x261 - 2.23606797749979 * m.b599 >= -2.23606797749979)
m.e262 = Constraint(expr= -sqrt((-0.49653521716587157 + m.x334)**2 + (
    -0.8612924863730758 + m.x335)**2 + (-0.3477168575425721 + m.x336)**2 + (
    -0.6615424192381595 + m.x337)**2 + (-0.2680635035686557 + m.x338)**2) +
    m.x262 - 2.23606797749979 * m.b600 >= -2.23606797749979)
m.e263 = Constraint(expr= -sqrt((-0.027492190735120214 + m.x334)**2 + (
    -0.975830678205581 + m.x335)**2 + (-0.5725079974762737 + m.x336)**2 + (
    -0.4627928206739904 + m.x337)**2 + (-0.676105217625283 + m.x338)**2) +
    m.x263 - 2.23606797749979 * m.b601 >= -2.23606797749979)
m.e264 = Constraint(expr= -sqrt((-0.13167765137927434 + m.x334)**2 + (
    -0.8772422533001436 + m.x335)**2 + (-0.30212459335273456 + m.x336)**2 + (
    -0.9589299306054163 + m.x337)**2 + (-0.1684676992378059 + m.x338)**2) +
    m.x264 - 2.23606797749979 * m.b602 >= -2.23606797749979)
m.e265 = Constraint(expr= -sqrt((-0.4631605820201776 + m.x334)**2 + (
    -0.3075046464306209 + m.x335)**2 + (-0.6161047422348818 + m.x336)**2 + (
    -0.06036679498995601 + m.x337)**2 + (-0.055585229920206314 + m.x338)**2) +
    m.x265 - 2.23606797749979 * m.b603 >= -2.23606797749979)
m.e266 = Constraint(expr= -sqrt((-0.32388656731438237 + m.x334)**2 + (
    -0.05792786993199972 + m.x335)**2 + (-0.8135525615007164 + m.x336)**2 + (
    -0.11918904488489845 + m.x337)**2 + (-0.3074172166187361 + m.x338)**2) +
    m.x266 - 2.23606797749979 * m.b604 >= -2.23606797749979)
m.e267 = Constraint(expr= -sqrt((-0.5224218716951496 + m.x334)**2 + (
    -0.11445496716294967 + m.x335)**2 + (-0.9526471232336744 + m.x336)**2 + (
    -0.29191369035574544 + m.x337)**2 + (-0.5653246839270838 + m.x338)**2) +
    m.x267 - 2.23606797749979 * m.b605 >= -2.23606797749979)
m.e268 = Constraint(expr= -sqrt((-0.21125847741287684 + m.x334)**2 + (
    -0.24527434539791804 + m.x335)**2 + (-0.6289970479606978 + m.x336)**2 + (
    -0.7068457529300446 + m.x337)**2 + (-0.7943561377121612 + m.x338)**2) +
    m.x268 - 2.23606797749979 * m.b606 >= -2.23606797749979)
m.e269 = Constraint(expr= -sqrt((-0.9522420339595141 + m.x334)**2 + (
    -0.9326354363859527 + m.x335)**2 + (-0.4449382446418748 + m.x336)**2 + (
    -0.018772017414026565 + m.x337)**2 + (-0.1570753065990531 + m.x338)**2) +
    m.x269 - 2.23606797749979 * m.b607 >= -2.23606797749979)
m.e270 = Constraint(expr= -sqrt((-0.8796213188443197 + m.x334)**2 + (
    -0.9757325913906182 + m.x335)**2 + (-0.5478578093651233 + m.x336)**2 + (
    -0.00973548730106566 + m.x337)**2 + (-0.27048086044812103 + m.x338)**2) +
    m.x270 - 2.23606797749979 * m.b608 >= -2.23606797749979)
m.e271 = Constraint(expr= -sqrt((-0.7382526421375969 + m.x334)**2 + (
    -0.18734997029644274 + m.x335)**2 + (-0.2597432271723712 + m.x336)**2 + (
    -0.42962015792230956 + m.x337)**2 + (-0.7073477915737445 + m.x338)**2) +
    m.x271 - 2.23606797749979 * m.b609 >= -2.23606797749979)
m.e272 = Constraint(expr= -sqrt((-0.7480253586345234 + m.x334)**2 + (
    -0.39775488720466023 + m.x335)**2 + (-0.3653805995645427 + m.x336)**2 + (
    -0.5146776625112836 + m.x337)**2 + (-0.46172129982047827 + m.x338)**2) +
    m.x272 - 2.23606797749979 * m.b610 >= -2.23606797749979)
m.e273 = Constraint(expr= -sqrt((-0.9807955797704826 + m.x334)**2 + (
    -0.09734685184548297 + m.x335)**2 + (-0.38645671601793696 + m.x336)**2 + (
    -0.33263947083044576 + m.x337)**2 + (-0.5052803496499273 + m.x338)**2) +
    m.x273 - 2.23606797749979 * m.b611 >= -2.23606797749979)
m.e274 = Constraint(expr= m.b417 + m.b432 + m.b447 + m.b462 + m.b477 + m.b492
    + m.b507 + m.b522 + m.b537 + m.b552 + m.b567 + m.b582 + m.b597 == 1)
m.e275 = Constraint(expr= m.b418 + m.b433 + m.b448 + m.b463 + m.b478 + m.b493
    + m.b508 + m.b523 + m.b538 + m.b553 + m.b568 + m.b583 + m.b598 == 1)
m.e276 = Constraint(expr= m.b419 + m.b434 + m.b449 + m.b464 + m.b479 + m.b494
    + m.b509 + m.b524 + m.b539 + m.b554 + m.b569 + m.b584 + m.b599 == 1)
m.e277 = Constraint(expr= m.b420 + m.b435 + m.b450 + m.b465 + m.b480 + m.b495
    + m.b510 + m.b525 + m.b540 + m.b555 + m.b570 + m.b585 + m.b600 == 1)
m.e278 = Constraint(expr= m.b421 + m.b436 + m.b451 + m.b466 + m.b481 + m.b496
    + m.b511 + m.b526 + m.b541 + m.b556 + m.b571 + m.b586 + m.b601 == 1)
m.e279 = Constraint(expr= m.b422 + m.b437 + m.b452 + m.b467 + m.b482 + m.b497
    + m.b512 + m.b527 + m.b542 + m.b557 + m.b572 + m.b587 + m.b602 == 1)
m.e280 = Constraint(expr= m.b423 + m.b438 + m.b453 + m.b468 + m.b483 + m.b498
    + m.b513 + m.b528 + m.b543 + m.b558 + m.b573 + m.b588 + m.b603 == 1)
m.e281 = Constraint(expr= m.b424 + m.b439 + m.b454 + m.b469 + m.b484 + m.b499
    + m.b514 + m.b529 + m.b544 + m.b559 + m.b574 + m.b589 + m.b604 == 1)
m.e282 = Constraint(expr= m.b425 + m.b440 + m.b455 + m.b470 + m.b485 + m.b500
    + m.b515 + m.b530 + m.b545 + m.b560 + m.b575 + m.b590 + m.b605 == 1)
m.e283 = Constraint(expr= m.b426 + m.b441 + m.b456 + m.b471 + m.b486 + m.b501
    + m.b516 + m.b531 + m.b546 + m.b561 + m.b576 + m.b591 + m.b606 == 1)
m.e284 = Constraint(expr= m.b427 + m.b442 + m.b457 + m.b472 + m.b487 + m.b502
    + m.b517 + m.b532 + m.b547 + m.b562 + m.b577 + m.b592 + m.b607 == 1)
m.e285 = Constraint(expr= m.b428 + m.b443 + m.b458 + m.b473 + m.b488 + m.b503
    + m.b518 + m.b533 + m.b548 + m.b563 + m.b578 + m.b593 + m.b608 == 1)
m.e286 = Constraint(expr= m.b429 + m.b444 + m.b459 + m.b474 + m.b489 + m.b504
    + m.b519 + m.b534 + m.b549 + m.b564 + m.b579 + m.b594 + m.b609 == 1)
m.e287 = Constraint(expr= m.b430 + m.b445 + m.b460 + m.b475 + m.b490 + m.b505
    + m.b520 + m.b535 + m.b550 + m.b565 + m.b580 + m.b595 + m.b610 == 1)
m.e288 = Constraint(expr= m.b431 + m.b446 + m.b461 + m.b476 + m.b491 + m.b506
    + m.b521 + m.b536 + m.b551 + m.b566 + m.b581 + m.b596 + m.b611 == 1)
m.e289 = Constraint(expr= m.b339 + m.b340 + m.b341 + m.b342 + m.b343 + m.b344
    + m.b345 + m.b346 + m.b347 + m.b348 + m.b349 + m.b350 + m.b417 + m.b418 +
    m.b419 + m.b420 + m.b421 + m.b422 + m.b423 + m.b424 + m.b425 + m.b426 +
    m.b427 + m.b428 + m.b429 + m.b430 + m.b431 == 3)
m.e290 = Constraint(expr= m.b339 + m.b351 + m.b352 + m.b353 + m.b354 + m.b355
    + m.b356 + m.b357 + m.b358 + m.b359 + m.b360 + m.b361 + m.b432 + m.b433 +
    m.b434 + m.b435 + m.b436 + m.b437 + m.b438 + m.b439 + m.b440 + m.b441 +
    m.b442 + m.b443 + m.b444 + m.b445 + m.b446 == 3)
m.e291 = Constraint(expr= m.b340 + m.b351 + m.b362 + m.b363 + m.b364 + m.b365
    + m.b366 + m.b367 + m.b368 + m.b369 + m.b370 + m.b371 + m.b447 + m.b448 +
    m.b449 + m.b450 + m.b451 + m.b452 + m.b453 + m.b454 + m.b455 + m.b456 +
    m.b457 + m.b458 + m.b459 + m.b460 + m.b461 == 3)
m.e292 = Constraint(expr= m.b341 + m.b352 + m.b362 + m.b372 + m.b373 + m.b374
    + m.b375 + m.b376 + m.b377 + m.b378 + m.b379 + m.b380 + m.b462 + m.b463 +
    m.b464 + m.b465 + m.b466 + m.b467 + m.b468 + m.b469 + m.b470 + m.b471 +
    m.b472 + m.b473 + m.b474 + m.b475 + m.b476 == 3)
m.e293 = Constraint(expr= m.b342 + m.b353 + m.b363 + m.b372 + m.b381 + m.b382
    + m.b383 + m.b384 + m.b385 + m.b386 + m.b387 + m.b388 + m.b477 + m.b478 +
    m.b479 + m.b480 + m.b481 + m.b482 + m.b483 + m.b484 + m.b485 + m.b486 +
    m.b487 + m.b488 + m.b489 + m.b490 + m.b491 == 3)
m.e294 = Constraint(expr= m.b343 + m.b354 + m.b364 + m.b373 + m.b381 + m.b389
    + m.b390 + m.b391 + m.b392 + m.b393 + m.b394 + m.b395 + m.b492 + m.b493 +
    m.b494 + m.b495 + m.b496 + m.b497 + m.b498 + m.b499 + m.b500 + m.b501 +
    m.b502 + m.b503 + m.b504 + m.b505 + m.b506 == 3)
m.e295 = Constraint(expr= m.b344 + m.b355 + m.b365 + m.b374 + m.b382 + m.b389
    + m.b396 + m.b397 + m.b398 + m.b399 + m.b400 + m.b401 + m.b507 + m.b508 +
    m.b509 + m.b510 + m.b511 + m.b512 + m.b513 + m.b514 + m.b515 + m.b516 +
    m.b517 + m.b518 + m.b519 + m.b520 + m.b521 == 3)
m.e296 = Constraint(expr= m.b345 + m.b356 + m.b366 + m.b375 + m.b383 + m.b390
    + m.b396 + m.b402 + m.b403 + m.b404 + m.b405 + m.b406 + m.b522 + m.b523 +
    m.b524 + m.b525 + m.b526 + m.b527 + m.b528 + m.b529 + m.b530 + m.b531 +
    m.b532 + m.b533 + m.b534 + m.b535 + m.b536 == 3)
m.e297 = Constraint(expr= m.b346 + m.b357 + m.b367 + m.b376 + m.b384 + m.b391
    + m.b397 + m.b402 + m.b407 + m.b408 + m.b409 + m.b410 + m.b537 + m.b538 +
    m.b539 + m.b540 + m.b541 + m.b542 + m.b543 + m.b544 + m.b545 + m.b546 +
    m.b547 + m.b548 + m.b549 + m.b550 + m.b551 == 3)
m.e298 = Constraint(expr= m.b347 + m.b358 + m.b368 + m.b377 + m.b385 + m.b392
    + m.b398 + m.b403 + m.b407 + m.b411 + m.b412 + m.b413 + m.b552 + m.b553 +
    m.b554 + m.b555 + m.b556 + m.b557 + m.b558 + m.b559 + m.b560 + m.b561 +
    m.b562 + m.b563 + m.b564 + m.b565 + m.b566 == 3)
m.e299 = Constraint(expr= m.b348 + m.b359 + m.b369 + m.b378 + m.b386 + m.b393
    + m.b399 + m.b404 + m.b408 + m.b411 + m.b414 + m.b415 + m.b567 + m.b568 +
    m.b569 + m.b570 + m.b571 + m.b572 + m.b573 + m.b574 + m.b575 + m.b576 +
    m.b577 + m.b578 + m.b579 + m.b580 + m.b581 == 3)
m.e300 = Constraint(expr= m.b349 + m.b360 + m.b370 + m.b379 + m.b387 + m.b394
    + m.b400 + m.b405 + m.b409 + m.b412 + m.b414 + m.b416 + m.b582 + m.b583 +
    m.b584 + m.b585 + m.b586 + m.b587 + m.b588 + m.b589 + m.b590 + m.b591 +
    m.b592 + m.b593 + m.b594 + m.b595 + m.b596 == 3)
m.e301 = Constraint(expr= m.b350 + m.b361 + m.b371 + m.b380 + m.b388 + m.b395
    + m.b401 + m.b406 + m.b410 + m.b413 + m.b415 + m.b416 + m.b597 + m.b598 +
    m.b599 + m.b600 + m.b601 + m.b602 + m.b603 + m.b604 + m.b605 + m.b606 +
    m.b607 + m.b608 + m.b609 + m.b610 + m.b611 == 3)
m.e302 = Constraint(expr= m.b339 == 1)
m.e303 = Constraint(expr= m.b340 + m.b351 == 1)
m.e304 = Constraint(expr= m.b341 + m.b352 + m.b362 == 1)
m.e305 = Constraint(expr= m.b342 + m.b353 + m.b363 + m.b372 == 1)
m.e306 = Constraint(expr= m.b343 + m.b354 + m.b364 + m.b373 + m.b381 == 1)
m.e307 = Constraint(expr= m.b344 + m.b355 + m.b365 + m.b374 + m.b382 + m.b389
    == 1)
m.e308 = Constraint(expr= m.b345 + m.b356 + m.b366 + m.b375 + m.b383 + m.b390
    + m.b396 == 1)
m.e309 = Constraint(expr= m.b346 + m.b357 + m.b367 + m.b376 + m.b384 + m.b391
    + m.b397 + m.b402 == 1)
m.e310 = Constraint(expr= m.b347 + m.b358 + m.b368 + m.b377 + m.b385 + m.b392
    + m.b398 + m.b403 + m.b407 == 1)
m.e311 = Constraint(expr= m.b348 + m.b359 + m.b369 + m.b378 + m.b386 + m.b393
    + m.b399 + m.b404 + m.b408 + m.b411 == 1)
m.e312 = Constraint(expr= m.b349 + m.b360 + m.b370 + m.b379 + m.b387 + m.b394
    + m.b400 + m.b405 + m.b409 + m.b412 + m.b414 == 1)
m.e313 = Constraint(expr= m.b350 + m.b361 + m.b371 + m.b380 + m.b388 + m.b395
    + m.b401 + m.b406 + m.b410 + m.b413 + m.b415 + m.b416 == 1)
