# MINLP written by GAMS Convert at 05/15/24 12:01:36
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       313       40      273        0        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#       585      312      273        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#      2223     1170     1053
#
# Reformulation has removed 1 variable and 1 equation

from pyomo.environ import *

model = m = ConcreteModel()

m.x1 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x2 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x3 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x4 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x5 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x6 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x7 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x8 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x9 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x10 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x11 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x12 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x13 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x14 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x15 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x16 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x17 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x18 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x19 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x20 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x21 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x22 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x23 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x24 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x25 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x26 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x27 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x28 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x29 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x30 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x31 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x32 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x33 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x34 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x35 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x36 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x37 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x38 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x39 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x40 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x41 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x42 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x43 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x44 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x45 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x46 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x47 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x48 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x49 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x50 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x51 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x52 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x53 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x54 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x55 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x56 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x57 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x58 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x59 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x60 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x61 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x62 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x63 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x64 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x65 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x66 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x67 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x68 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x69 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x70 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x71 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x72 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x73 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x74 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x75 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x76 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x77 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x78 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x79 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x80 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x81 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x82 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x83 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x84 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x85 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x86 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x87 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x88 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x89 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x90 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x91 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x92 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x93 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x94 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x95 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x96 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x97 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x98 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x99 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x100 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x101 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x102 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x103 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x104 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x105 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x106 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x107 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x108 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x109 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x110 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x111 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x112 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x113 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x114 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x115 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x116 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x117 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x118 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x119 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x120 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x121 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x122 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x123 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x124 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x125 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x126 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x127 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x128 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x129 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x130 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x131 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x132 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x133 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x134 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x135 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x136 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x137 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x138 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x139 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x140 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x141 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x142 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x143 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x144 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x145 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x146 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x147 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x148 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x149 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x150 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x151 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x152 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x153 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x154 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x155 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x156 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x157 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x158 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x159 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x160 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x161 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x162 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x163 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x164 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x165 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x166 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x167 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x168 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x169 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x170 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x171 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x172 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x173 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x174 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x175 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x176 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x177 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x178 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x179 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x180 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x181 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x182 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x183 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x184 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x185 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x186 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x187 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x188 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x189 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x190 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x191 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x192 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x193 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x194 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x195 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x196 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x197 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x198 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x199 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x200 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x201 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x202 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x203 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x204 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x205 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x206 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x207 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x208 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x209 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x210 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x211 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x212 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x213 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x214 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x215 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x216 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x217 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x218 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x219 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x220 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x221 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x222 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x223 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x224 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x225 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x226 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x227 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x228 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x229 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x230 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x231 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x232 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x233 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x234 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x235 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x236 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x237 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x238 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x239 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x240 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x241 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x242 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x243 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x244 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x245 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x246 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x247 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x248 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x249 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x250 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x251 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x252 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x253 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x254 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x255 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x256 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x257 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x258 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x259 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x260 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x261 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x262 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x263 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x264 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x265 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x266 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x267 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x268 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x269 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x270 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x271 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x272 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
m.x273 = Var(within=Reals, bounds=(0,1.7320508075688772), initialize=0)
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
m.b313 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b314 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b315 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b316 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b317 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b318 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b319 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b320 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b321 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b322 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b323 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b324 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b325 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b326 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b327 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b328 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b329 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b330 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b331 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b332 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b333 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b334 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b335 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b336 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b337 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b338 = Var(within=Binary, bounds=(0,1), initialize=0)
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

m.e1 = Constraint(expr= -sqrt((m.x274 - m.x277)**2 + (m.x275 - m.x278)**2 + (
    m.x276 - m.x279)**2) + m.x1 - 1.7320508075688772 * m.b313
    >= -1.7320508075688772)
m.e2 = Constraint(expr= -sqrt((m.x274 - m.x280)**2 + (m.x275 - m.x281)**2 + (
    m.x276 - m.x282)**2) + m.x2 - 1.7320508075688772 * m.b314
    >= -1.7320508075688772)
m.e3 = Constraint(expr= -sqrt((m.x274 - m.x283)**2 + (m.x275 - m.x284)**2 + (
    m.x276 - m.x285)**2) + m.x3 - 1.7320508075688772 * m.b315
    >= -1.7320508075688772)
m.e4 = Constraint(expr= -sqrt((m.x274 - m.x286)**2 + (m.x275 - m.x287)**2 + (
    m.x276 - m.x288)**2) + m.x4 - 1.7320508075688772 * m.b316
    >= -1.7320508075688772)
m.e5 = Constraint(expr= -sqrt((m.x274 - m.x289)**2 + (m.x275 - m.x290)**2 + (
    m.x276 - m.x291)**2) + m.x5 - 1.7320508075688772 * m.b317
    >= -1.7320508075688772)
m.e6 = Constraint(expr= -sqrt((m.x274 - m.x292)**2 + (m.x275 - m.x293)**2 + (
    m.x276 - m.x294)**2) + m.x6 - 1.7320508075688772 * m.b318
    >= -1.7320508075688772)
m.e7 = Constraint(expr= -sqrt((m.x274 - m.x295)**2 + (m.x275 - m.x296)**2 + (
    m.x276 - m.x297)**2) + m.x7 - 1.7320508075688772 * m.b319
    >= -1.7320508075688772)
m.e8 = Constraint(expr= -sqrt((m.x274 - m.x298)**2 + (m.x275 - m.x299)**2 + (
    m.x276 - m.x300)**2) + m.x8 - 1.7320508075688772 * m.b320
    >= -1.7320508075688772)
m.e9 = Constraint(expr= -sqrt((m.x274 - m.x301)**2 + (m.x275 - m.x302)**2 + (
    m.x276 - m.x303)**2) + m.x9 - 1.7320508075688772 * m.b321
    >= -1.7320508075688772)
m.e10 = Constraint(expr= -sqrt((m.x274 - m.x304)**2 + (m.x275 - m.x305)**2 + (
    m.x276 - m.x306)**2) + m.x10 - 1.7320508075688772 * m.b322
    >= -1.7320508075688772)
m.e11 = Constraint(expr= -sqrt((m.x274 - m.x307)**2 + (m.x275 - m.x308)**2 + (
    m.x276 - m.x309)**2) + m.x11 - 1.7320508075688772 * m.b323
    >= -1.7320508075688772)
m.e12 = Constraint(expr= -sqrt((m.x274 - m.x310)**2 + (m.x275 - m.x311)**2 + (
    m.x276 - m.x312)**2) + m.x12 - 1.7320508075688772 * m.b324
    >= -1.7320508075688772)
m.e13 = Constraint(expr= -sqrt((m.x277 - m.x280)**2 + (m.x278 - m.x281)**2 + (
    m.x279 - m.x282)**2) + m.x13 - 1.7320508075688772 * m.b325
    >= -1.7320508075688772)
m.e14 = Constraint(expr= -sqrt((m.x277 - m.x283)**2 + (m.x278 - m.x284)**2 + (
    m.x279 - m.x285)**2) + m.x14 - 1.7320508075688772 * m.b326
    >= -1.7320508075688772)
m.e15 = Constraint(expr= -sqrt((m.x277 - m.x286)**2 + (m.x278 - m.x287)**2 + (
    m.x279 - m.x288)**2) + m.x15 - 1.7320508075688772 * m.b327
    >= -1.7320508075688772)
m.e16 = Constraint(expr= -sqrt((m.x277 - m.x289)**2 + (m.x278 - m.x290)**2 + (
    m.x279 - m.x291)**2) + m.x16 - 1.7320508075688772 * m.b328
    >= -1.7320508075688772)
m.e17 = Constraint(expr= -sqrt((m.x277 - m.x292)**2 + (m.x278 - m.x293)**2 + (
    m.x279 - m.x294)**2) + m.x17 - 1.7320508075688772 * m.b329
    >= -1.7320508075688772)
m.e18 = Constraint(expr= -sqrt((m.x277 - m.x295)**2 + (m.x278 - m.x296)**2 + (
    m.x279 - m.x297)**2) + m.x18 - 1.7320508075688772 * m.b330
    >= -1.7320508075688772)
m.e19 = Constraint(expr= -sqrt((m.x277 - m.x298)**2 + (m.x278 - m.x299)**2 + (
    m.x279 - m.x300)**2) + m.x19 - 1.7320508075688772 * m.b331
    >= -1.7320508075688772)
m.e20 = Constraint(expr= -sqrt((m.x277 - m.x301)**2 + (m.x278 - m.x302)**2 + (
    m.x279 - m.x303)**2) + m.x20 - 1.7320508075688772 * m.b332
    >= -1.7320508075688772)
m.e21 = Constraint(expr= -sqrt((m.x277 - m.x304)**2 + (m.x278 - m.x305)**2 + (
    m.x279 - m.x306)**2) + m.x21 - 1.7320508075688772 * m.b333
    >= -1.7320508075688772)
m.e22 = Constraint(expr= -sqrt((m.x277 - m.x307)**2 + (m.x278 - m.x308)**2 + (
    m.x279 - m.x309)**2) + m.x22 - 1.7320508075688772 * m.b334
    >= -1.7320508075688772)
m.e23 = Constraint(expr= -sqrt((m.x277 - m.x310)**2 + (m.x278 - m.x311)**2 + (
    m.x279 - m.x312)**2) + m.x23 - 1.7320508075688772 * m.b335
    >= -1.7320508075688772)
m.e24 = Constraint(expr= -sqrt((m.x280 - m.x283)**2 + (m.x281 - m.x284)**2 + (
    m.x282 - m.x285)**2) + m.x24 - 1.7320508075688772 * m.b336
    >= -1.7320508075688772)
m.e25 = Constraint(expr= -sqrt((m.x280 - m.x286)**2 + (m.x281 - m.x287)**2 + (
    m.x282 - m.x288)**2) + m.x25 - 1.7320508075688772 * m.b337
    >= -1.7320508075688772)
m.e26 = Constraint(expr= -sqrt((m.x280 - m.x289)**2 + (m.x281 - m.x290)**2 + (
    m.x282 - m.x291)**2) + m.x26 - 1.7320508075688772 * m.b338
    >= -1.7320508075688772)
m.e27 = Constraint(expr= -sqrt((m.x280 - m.x292)**2 + (m.x281 - m.x293)**2 + (
    m.x282 - m.x294)**2) + m.x27 - 1.7320508075688772 * m.b339
    >= -1.7320508075688772)
m.e28 = Constraint(expr= -sqrt((m.x280 - m.x295)**2 + (m.x281 - m.x296)**2 + (
    m.x282 - m.x297)**2) + m.x28 - 1.7320508075688772 * m.b340
    >= -1.7320508075688772)
m.e29 = Constraint(expr= -sqrt((m.x280 - m.x298)**2 + (m.x281 - m.x299)**2 + (
    m.x282 - m.x300)**2) + m.x29 - 1.7320508075688772 * m.b341
    >= -1.7320508075688772)
m.e30 = Constraint(expr= -sqrt((m.x280 - m.x301)**2 + (m.x281 - m.x302)**2 + (
    m.x282 - m.x303)**2) + m.x30 - 1.7320508075688772 * m.b342
    >= -1.7320508075688772)
m.e31 = Constraint(expr= -sqrt((m.x280 - m.x304)**2 + (m.x281 - m.x305)**2 + (
    m.x282 - m.x306)**2) + m.x31 - 1.7320508075688772 * m.b343
    >= -1.7320508075688772)
m.e32 = Constraint(expr= -sqrt((m.x280 - m.x307)**2 + (m.x281 - m.x308)**2 + (
    m.x282 - m.x309)**2) + m.x32 - 1.7320508075688772 * m.b344
    >= -1.7320508075688772)
m.e33 = Constraint(expr= -sqrt((m.x280 - m.x310)**2 + (m.x281 - m.x311)**2 + (
    m.x282 - m.x312)**2) + m.x33 - 1.7320508075688772 * m.b345
    >= -1.7320508075688772)
m.e34 = Constraint(expr= -sqrt((m.x283 - m.x286)**2 + (m.x284 - m.x287)**2 + (
    m.x285 - m.x288)**2) + m.x34 - 1.7320508075688772 * m.b346
    >= -1.7320508075688772)
m.e35 = Constraint(expr= -sqrt((m.x283 - m.x289)**2 + (m.x284 - m.x290)**2 + (
    m.x285 - m.x291)**2) + m.x35 - 1.7320508075688772 * m.b347
    >= -1.7320508075688772)
m.e36 = Constraint(expr= -sqrt((m.x283 - m.x292)**2 + (m.x284 - m.x293)**2 + (
    m.x285 - m.x294)**2) + m.x36 - 1.7320508075688772 * m.b348
    >= -1.7320508075688772)
m.e37 = Constraint(expr= -sqrt((m.x283 - m.x295)**2 + (m.x284 - m.x296)**2 + (
    m.x285 - m.x297)**2) + m.x37 - 1.7320508075688772 * m.b349
    >= -1.7320508075688772)
m.e38 = Constraint(expr= -sqrt((m.x283 - m.x298)**2 + (m.x284 - m.x299)**2 + (
    m.x285 - m.x300)**2) + m.x38 - 1.7320508075688772 * m.b350
    >= -1.7320508075688772)
m.e39 = Constraint(expr= -sqrt((m.x283 - m.x301)**2 + (m.x284 - m.x302)**2 + (
    m.x285 - m.x303)**2) + m.x39 - 1.7320508075688772 * m.b351
    >= -1.7320508075688772)
m.e40 = Constraint(expr= -sqrt((m.x283 - m.x304)**2 + (m.x284 - m.x305)**2 + (
    m.x285 - m.x306)**2) + m.x40 - 1.7320508075688772 * m.b352
    >= -1.7320508075688772)
m.e41 = Constraint(expr= -sqrt((m.x283 - m.x307)**2 + (m.x284 - m.x308)**2 + (
    m.x285 - m.x309)**2) + m.x41 - 1.7320508075688772 * m.b353
    >= -1.7320508075688772)
m.e42 = Constraint(expr= -sqrt((m.x283 - m.x310)**2 + (m.x284 - m.x311)**2 + (
    m.x285 - m.x312)**2) + m.x42 - 1.7320508075688772 * m.b354
    >= -1.7320508075688772)
m.e43 = Constraint(expr= -sqrt((m.x286 - m.x289)**2 + (m.x287 - m.x290)**2 + (
    m.x288 - m.x291)**2) + m.x43 - 1.7320508075688772 * m.b355
    >= -1.7320508075688772)
m.e44 = Constraint(expr= -sqrt((m.x286 - m.x292)**2 + (m.x287 - m.x293)**2 + (
    m.x288 - m.x294)**2) + m.x44 - 1.7320508075688772 * m.b356
    >= -1.7320508075688772)
m.e45 = Constraint(expr= -sqrt((m.x286 - m.x295)**2 + (m.x287 - m.x296)**2 + (
    m.x288 - m.x297)**2) + m.x45 - 1.7320508075688772 * m.b357
    >= -1.7320508075688772)
m.e46 = Constraint(expr= -sqrt((m.x286 - m.x298)**2 + (m.x287 - m.x299)**2 + (
    m.x288 - m.x300)**2) + m.x46 - 1.7320508075688772 * m.b358
    >= -1.7320508075688772)
m.e47 = Constraint(expr= -sqrt((m.x286 - m.x301)**2 + (m.x287 - m.x302)**2 + (
    m.x288 - m.x303)**2) + m.x47 - 1.7320508075688772 * m.b359
    >= -1.7320508075688772)
m.e48 = Constraint(expr= -sqrt((m.x286 - m.x304)**2 + (m.x287 - m.x305)**2 + (
    m.x288 - m.x306)**2) + m.x48 - 1.7320508075688772 * m.b360
    >= -1.7320508075688772)
m.e49 = Constraint(expr= -sqrt((m.x286 - m.x307)**2 + (m.x287 - m.x308)**2 + (
    m.x288 - m.x309)**2) + m.x49 - 1.7320508075688772 * m.b361
    >= -1.7320508075688772)
m.e50 = Constraint(expr= -sqrt((m.x286 - m.x310)**2 + (m.x287 - m.x311)**2 + (
    m.x288 - m.x312)**2) + m.x50 - 1.7320508075688772 * m.b362
    >= -1.7320508075688772)
m.e51 = Constraint(expr= -sqrt((m.x289 - m.x292)**2 + (m.x290 - m.x293)**2 + (
    m.x291 - m.x294)**2) + m.x51 - 1.7320508075688772 * m.b363
    >= -1.7320508075688772)
m.e52 = Constraint(expr= -sqrt((m.x289 - m.x295)**2 + (m.x290 - m.x296)**2 + (
    m.x291 - m.x297)**2) + m.x52 - 1.7320508075688772 * m.b364
    >= -1.7320508075688772)
m.e53 = Constraint(expr= -sqrt((m.x289 - m.x298)**2 + (m.x290 - m.x299)**2 + (
    m.x291 - m.x300)**2) + m.x53 - 1.7320508075688772 * m.b365
    >= -1.7320508075688772)
m.e54 = Constraint(expr= -sqrt((m.x289 - m.x301)**2 + (m.x290 - m.x302)**2 + (
    m.x291 - m.x303)**2) + m.x54 - 1.7320508075688772 * m.b366
    >= -1.7320508075688772)
m.e55 = Constraint(expr= -sqrt((m.x289 - m.x304)**2 + (m.x290 - m.x305)**2 + (
    m.x291 - m.x306)**2) + m.x55 - 1.7320508075688772 * m.b367
    >= -1.7320508075688772)
m.e56 = Constraint(expr= -sqrt((m.x289 - m.x307)**2 + (m.x290 - m.x308)**2 + (
    m.x291 - m.x309)**2) + m.x56 - 1.7320508075688772 * m.b368
    >= -1.7320508075688772)
m.e57 = Constraint(expr= -sqrt((m.x289 - m.x310)**2 + (m.x290 - m.x311)**2 + (
    m.x291 - m.x312)**2) + m.x57 - 1.7320508075688772 * m.b369
    >= -1.7320508075688772)
m.e58 = Constraint(expr= -sqrt((m.x292 - m.x295)**2 + (m.x293 - m.x296)**2 + (
    m.x294 - m.x297)**2) + m.x58 - 1.7320508075688772 * m.b370
    >= -1.7320508075688772)
m.e59 = Constraint(expr= -sqrt((m.x292 - m.x298)**2 + (m.x293 - m.x299)**2 + (
    m.x294 - m.x300)**2) + m.x59 - 1.7320508075688772 * m.b371
    >= -1.7320508075688772)
m.e60 = Constraint(expr= -sqrt((m.x292 - m.x301)**2 + (m.x293 - m.x302)**2 + (
    m.x294 - m.x303)**2) + m.x60 - 1.7320508075688772 * m.b372
    >= -1.7320508075688772)
m.e61 = Constraint(expr= -sqrt((m.x292 - m.x304)**2 + (m.x293 - m.x305)**2 + (
    m.x294 - m.x306)**2) + m.x61 - 1.7320508075688772 * m.b373
    >= -1.7320508075688772)
m.e62 = Constraint(expr= -sqrt((m.x292 - m.x307)**2 + (m.x293 - m.x308)**2 + (
    m.x294 - m.x309)**2) + m.x62 - 1.7320508075688772 * m.b374
    >= -1.7320508075688772)
m.e63 = Constraint(expr= -sqrt((m.x292 - m.x310)**2 + (m.x293 - m.x311)**2 + (
    m.x294 - m.x312)**2) + m.x63 - 1.7320508075688772 * m.b375
    >= -1.7320508075688772)
m.e64 = Constraint(expr= -sqrt((m.x295 - m.x298)**2 + (m.x296 - m.x299)**2 + (
    m.x297 - m.x300)**2) + m.x64 - 1.7320508075688772 * m.b376
    >= -1.7320508075688772)
m.e65 = Constraint(expr= -sqrt((m.x295 - m.x301)**2 + (m.x296 - m.x302)**2 + (
    m.x297 - m.x303)**2) + m.x65 - 1.7320508075688772 * m.b377
    >= -1.7320508075688772)
m.e66 = Constraint(expr= -sqrt((m.x295 - m.x304)**2 + (m.x296 - m.x305)**2 + (
    m.x297 - m.x306)**2) + m.x66 - 1.7320508075688772 * m.b378
    >= -1.7320508075688772)
m.e67 = Constraint(expr= -sqrt((m.x295 - m.x307)**2 + (m.x296 - m.x308)**2 + (
    m.x297 - m.x309)**2) + m.x67 - 1.7320508075688772 * m.b379
    >= -1.7320508075688772)
m.e68 = Constraint(expr= -sqrt((m.x295 - m.x310)**2 + (m.x296 - m.x311)**2 + (
    m.x297 - m.x312)**2) + m.x68 - 1.7320508075688772 * m.b380
    >= -1.7320508075688772)
m.e69 = Constraint(expr= -sqrt((m.x298 - m.x301)**2 + (m.x299 - m.x302)**2 + (
    m.x300 - m.x303)**2) + m.x69 - 1.7320508075688772 * m.b381
    >= -1.7320508075688772)
m.e70 = Constraint(expr= -sqrt((m.x298 - m.x304)**2 + (m.x299 - m.x305)**2 + (
    m.x300 - m.x306)**2) + m.x70 - 1.7320508075688772 * m.b382
    >= -1.7320508075688772)
m.e71 = Constraint(expr= -sqrt((m.x298 - m.x307)**2 + (m.x299 - m.x308)**2 + (
    m.x300 - m.x309)**2) + m.x71 - 1.7320508075688772 * m.b383
    >= -1.7320508075688772)
m.e72 = Constraint(expr= -sqrt((m.x298 - m.x310)**2 + (m.x299 - m.x311)**2 + (
    m.x300 - m.x312)**2) + m.x72 - 1.7320508075688772 * m.b384
    >= -1.7320508075688772)
m.e73 = Constraint(expr= -sqrt((m.x301 - m.x304)**2 + (m.x302 - m.x305)**2 + (
    m.x303 - m.x306)**2) + m.x73 - 1.7320508075688772 * m.b385
    >= -1.7320508075688772)
m.e74 = Constraint(expr= -sqrt((m.x301 - m.x307)**2 + (m.x302 - m.x308)**2 + (
    m.x303 - m.x309)**2) + m.x74 - 1.7320508075688772 * m.b386
    >= -1.7320508075688772)
m.e75 = Constraint(expr= -sqrt((m.x301 - m.x310)**2 + (m.x302 - m.x311)**2 + (
    m.x303 - m.x312)**2) + m.x75 - 1.7320508075688772 * m.b387
    >= -1.7320508075688772)
m.e76 = Constraint(expr= -sqrt((m.x304 - m.x307)**2 + (m.x305 - m.x308)**2 + (
    m.x306 - m.x309)**2) + m.x76 - 1.7320508075688772 * m.b388
    >= -1.7320508075688772)
m.e77 = Constraint(expr= -sqrt((m.x304 - m.x310)**2 + (m.x305 - m.x311)**2 + (
    m.x306 - m.x312)**2) + m.x77 - 1.7320508075688772 * m.b389
    >= -1.7320508075688772)
m.e78 = Constraint(expr= -sqrt((m.x307 - m.x310)**2 + (m.x308 - m.x311)**2 + (
    m.x309 - m.x312)**2) + m.x78 - 1.7320508075688772 * m.b390
    >= -1.7320508075688772)
m.e79 = Constraint(expr= -sqrt((-0.2718754143840908 + m.x274)**2 + (
    -0.48802820785090784 + m.x275)**2 + (-0.08187934237116656 + m.x276)**2) +
    m.x79 - 1.7320508075688772 * m.b391 >= -1.7320508075688772)
m.e80 = Constraint(expr= -sqrt((-0.33873348699206973 + m.x274)**2 + (
    -0.07233360770535402 + m.x275)**2 + (-0.011036367079899967 + m.x276)**2) +
    m.x80 - 1.7320508075688772 * m.b392 >= -1.7320508075688772)
m.e81 = Constraint(expr= -sqrt((-0.28385029589876865 + m.x274)**2 + (
    -0.11770636555802805 + m.x275)**2 + (-0.3110382248120007 + m.x276)**2) +
    m.x81 - 1.7320508075688772 * m.b393 >= -1.7320508075688772)
m.e82 = Constraint(expr= -sqrt((-0.7434707928397064 + m.x274)**2 + (
    -0.0357557155126923 + m.x275)**2 + (-0.6249375571804716 + m.x276)**2) +
    m.x82 - 1.7320508075688772 * m.b394 >= -1.7320508075688772)
m.e83 = Constraint(expr= -sqrt((-0.13501116090704035 + m.x274)**2 + (
    -0.7950712434655829 + m.x275)**2 + (-0.7369676243821022 + m.x276)**2) +
    m.x83 - 1.7320508075688772 * m.b395 >= -1.7320508075688772)
m.e84 = Constraint(expr= -sqrt((-0.21101029956774453 + m.x274)**2 + (
    -0.8480765801722641 + m.x275)**2 + (-0.7173017220824032 + m.x276)**2) +
    m.x84 - 1.7320508075688772 * m.b396 >= -1.7320508075688772)
m.e85 = Constraint(expr= -sqrt((-0.07495132545320449 + m.x274)**2 + (
    -0.4081313844234159 + m.x275)**2 + (-0.7004510913580178 + m.x276)**2) +
    m.x85 - 1.7320508075688772 * m.b397 >= -1.7320508075688772)
m.e86 = Constraint(expr= -sqrt((-0.9229582476032371 + m.x274)**2 + (
    -0.17221119493742953 + m.x275)**2 + (-0.2518629905323574 + m.x276)**2) +
    m.x86 - 1.7320508075688772 * m.b398 >= -1.7320508075688772)
m.e87 = Constraint(expr= -sqrt((-0.7750929946094214 + m.x274)**2 + (
    -0.9626723030210862 + m.x275)**2 + (-0.09375460752394849 + m.x276)**2) +
    m.x87 - 1.7320508075688772 * m.b399 >= -1.7320508075688772)
m.e88 = Constraint(expr= -sqrt((-0.08982827530229975 + m.x274)**2 + (
    -0.7511793846525663 + m.x275)**2 + (-0.3169893159261734 + m.x276)**2) +
    m.x88 - 1.7320508075688772 * m.b400 >= -1.7320508075688772)
m.e89 = Constraint(expr= -sqrt((-0.38677647485720235 + m.x274)**2 + (
    -0.87633207391825 + m.x275)**2 + (-0.7457995156246497 + m.x276)**2) + m.x89
    - 1.7320508075688772 * m.b401 >= -1.7320508075688772)
m.e90 = Constraint(expr= -sqrt((-0.6607159863179267 + m.x274)**2 + (
    -0.8676520260577261 + m.x275)**2 + (-0.7320438297162596 + m.x276)**2) +
    m.x90 - 1.7320508075688772 * m.b402 >= -1.7320508075688772)
m.e91 = Constraint(expr= -sqrt((-0.8102488868102232 + m.x274)**2 + (
    -0.6432507057061979 + m.x275)**2 + (-0.5931582872810908 + m.x276)**2) +
    m.x91 - 1.7320508075688772 * m.b403 >= -1.7320508075688772)
m.e92 = Constraint(expr= -sqrt((-0.05986505368858752 + m.x274)**2 + (
    -0.909611607891918 + m.x275)**2 + (-0.9117643699770345 + m.x276)**2) +
    m.x92 - 1.7320508075688772 * m.b404 >= -1.7320508075688772)
m.e93 = Constraint(expr= -sqrt((-0.35134351369704286 + m.x274)**2 + (
    -0.6263463928446534 + m.x275)**2 + (-0.01689904369168782 + m.x276)**2) +
    m.x93 - 1.7320508075688772 * m.b405 >= -1.7320508075688772)
m.e94 = Constraint(expr= -sqrt((-0.2718754143840908 + m.x277)**2 + (
    -0.48802820785090784 + m.x278)**2 + (-0.08187934237116656 + m.x279)**2) +
    m.x94 - 1.7320508075688772 * m.b406 >= -1.7320508075688772)
m.e95 = Constraint(expr= -sqrt((-0.33873348699206973 + m.x277)**2 + (
    -0.07233360770535402 + m.x278)**2 + (-0.011036367079899967 + m.x279)**2) +
    m.x95 - 1.7320508075688772 * m.b407 >= -1.7320508075688772)
m.e96 = Constraint(expr= -sqrt((-0.28385029589876865 + m.x277)**2 + (
    -0.11770636555802805 + m.x278)**2 + (-0.3110382248120007 + m.x279)**2) +
    m.x96 - 1.7320508075688772 * m.b408 >= -1.7320508075688772)
m.e97 = Constraint(expr= -sqrt((-0.7434707928397064 + m.x277)**2 + (
    -0.0357557155126923 + m.x278)**2 + (-0.6249375571804716 + m.x279)**2) +
    m.x97 - 1.7320508075688772 * m.b409 >= -1.7320508075688772)
m.e98 = Constraint(expr= -sqrt((-0.13501116090704035 + m.x277)**2 + (
    -0.7950712434655829 + m.x278)**2 + (-0.7369676243821022 + m.x279)**2) +
    m.x98 - 1.7320508075688772 * m.b410 >= -1.7320508075688772)
m.e99 = Constraint(expr= -sqrt((-0.21101029956774453 + m.x277)**2 + (
    -0.8480765801722641 + m.x278)**2 + (-0.7173017220824032 + m.x279)**2) +
    m.x99 - 1.7320508075688772 * m.b411 >= -1.7320508075688772)
m.e100 = Constraint(expr= -sqrt((-0.07495132545320449 + m.x277)**2 + (
    -0.4081313844234159 + m.x278)**2 + (-0.7004510913580178 + m.x279)**2) +
    m.x100 - 1.7320508075688772 * m.b412 >= -1.7320508075688772)
m.e101 = Constraint(expr= -sqrt((-0.9229582476032371 + m.x277)**2 + (
    -0.17221119493742953 + m.x278)**2 + (-0.2518629905323574 + m.x279)**2) +
    m.x101 - 1.7320508075688772 * m.b413 >= -1.7320508075688772)
m.e102 = Constraint(expr= -sqrt((-0.7750929946094214 + m.x277)**2 + (
    -0.9626723030210862 + m.x278)**2 + (-0.09375460752394849 + m.x279)**2) +
    m.x102 - 1.7320508075688772 * m.b414 >= -1.7320508075688772)
m.e103 = Constraint(expr= -sqrt((-0.08982827530229975 + m.x277)**2 + (
    -0.7511793846525663 + m.x278)**2 + (-0.3169893159261734 + m.x279)**2) +
    m.x103 - 1.7320508075688772 * m.b415 >= -1.7320508075688772)
m.e104 = Constraint(expr= -sqrt((-0.38677647485720235 + m.x277)**2 + (
    -0.87633207391825 + m.x278)**2 + (-0.7457995156246497 + m.x279)**2) +
    m.x104 - 1.7320508075688772 * m.b416 >= -1.7320508075688772)
m.e105 = Constraint(expr= -sqrt((-0.6607159863179267 + m.x277)**2 + (
    -0.8676520260577261 + m.x278)**2 + (-0.7320438297162596 + m.x279)**2) +
    m.x105 - 1.7320508075688772 * m.b417 >= -1.7320508075688772)
m.e106 = Constraint(expr= -sqrt((-0.8102488868102232 + m.x277)**2 + (
    -0.6432507057061979 + m.x278)**2 + (-0.5931582872810908 + m.x279)**2) +
    m.x106 - 1.7320508075688772 * m.b418 >= -1.7320508075688772)
m.e107 = Constraint(expr= -sqrt((-0.05986505368858752 + m.x277)**2 + (
    -0.909611607891918 + m.x278)**2 + (-0.9117643699770345 + m.x279)**2) +
    m.x107 - 1.7320508075688772 * m.b419 >= -1.7320508075688772)
m.e108 = Constraint(expr= -sqrt((-0.35134351369704286 + m.x277)**2 + (
    -0.6263463928446534 + m.x278)**2 + (-0.01689904369168782 + m.x279)**2) +
    m.x108 - 1.7320508075688772 * m.b420 >= -1.7320508075688772)
m.e109 = Constraint(expr= -sqrt((-0.2718754143840908 + m.x280)**2 + (
    -0.48802820785090784 + m.x281)**2 + (-0.08187934237116656 + m.x282)**2) +
    m.x109 - 1.7320508075688772 * m.b421 >= -1.7320508075688772)
m.e110 = Constraint(expr= -sqrt((-0.33873348699206973 + m.x280)**2 + (
    -0.07233360770535402 + m.x281)**2 + (-0.011036367079899967 + m.x282)**2) +
    m.x110 - 1.7320508075688772 * m.b422 >= -1.7320508075688772)
m.e111 = Constraint(expr= -sqrt((-0.28385029589876865 + m.x280)**2 + (
    -0.11770636555802805 + m.x281)**2 + (-0.3110382248120007 + m.x282)**2) +
    m.x111 - 1.7320508075688772 * m.b423 >= -1.7320508075688772)
m.e112 = Constraint(expr= -sqrt((-0.7434707928397064 + m.x280)**2 + (
    -0.0357557155126923 + m.x281)**2 + (-0.6249375571804716 + m.x282)**2) +
    m.x112 - 1.7320508075688772 * m.b424 >= -1.7320508075688772)
m.e113 = Constraint(expr= -sqrt((-0.13501116090704035 + m.x280)**2 + (
    -0.7950712434655829 + m.x281)**2 + (-0.7369676243821022 + m.x282)**2) +
    m.x113 - 1.7320508075688772 * m.b425 >= -1.7320508075688772)
m.e114 = Constraint(expr= -sqrt((-0.21101029956774453 + m.x280)**2 + (
    -0.8480765801722641 + m.x281)**2 + (-0.7173017220824032 + m.x282)**2) +
    m.x114 - 1.7320508075688772 * m.b426 >= -1.7320508075688772)
m.e115 = Constraint(expr= -sqrt((-0.07495132545320449 + m.x280)**2 + (
    -0.4081313844234159 + m.x281)**2 + (-0.7004510913580178 + m.x282)**2) +
    m.x115 - 1.7320508075688772 * m.b427 >= -1.7320508075688772)
m.e116 = Constraint(expr= -sqrt((-0.9229582476032371 + m.x280)**2 + (
    -0.17221119493742953 + m.x281)**2 + (-0.2518629905323574 + m.x282)**2) +
    m.x116 - 1.7320508075688772 * m.b428 >= -1.7320508075688772)
m.e117 = Constraint(expr= -sqrt((-0.7750929946094214 + m.x280)**2 + (
    -0.9626723030210862 + m.x281)**2 + (-0.09375460752394849 + m.x282)**2) +
    m.x117 - 1.7320508075688772 * m.b429 >= -1.7320508075688772)
m.e118 = Constraint(expr= -sqrt((-0.08982827530229975 + m.x280)**2 + (
    -0.7511793846525663 + m.x281)**2 + (-0.3169893159261734 + m.x282)**2) +
    m.x118 - 1.7320508075688772 * m.b430 >= -1.7320508075688772)
m.e119 = Constraint(expr= -sqrt((-0.38677647485720235 + m.x280)**2 + (
    -0.87633207391825 + m.x281)**2 + (-0.7457995156246497 + m.x282)**2) +
    m.x119 - 1.7320508075688772 * m.b431 >= -1.7320508075688772)
m.e120 = Constraint(expr= -sqrt((-0.6607159863179267 + m.x280)**2 + (
    -0.8676520260577261 + m.x281)**2 + (-0.7320438297162596 + m.x282)**2) +
    m.x120 - 1.7320508075688772 * m.b432 >= -1.7320508075688772)
m.e121 = Constraint(expr= -sqrt((-0.8102488868102232 + m.x280)**2 + (
    -0.6432507057061979 + m.x281)**2 + (-0.5931582872810908 + m.x282)**2) +
    m.x121 - 1.7320508075688772 * m.b433 >= -1.7320508075688772)
m.e122 = Constraint(expr= -sqrt((-0.05986505368858752 + m.x280)**2 + (
    -0.909611607891918 + m.x281)**2 + (-0.9117643699770345 + m.x282)**2) +
    m.x122 - 1.7320508075688772 * m.b434 >= -1.7320508075688772)
m.e123 = Constraint(expr= -sqrt((-0.35134351369704286 + m.x280)**2 + (
    -0.6263463928446534 + m.x281)**2 + (-0.01689904369168782 + m.x282)**2) +
    m.x123 - 1.7320508075688772 * m.b435 >= -1.7320508075688772)
m.e124 = Constraint(expr= -sqrt((-0.2718754143840908 + m.x283)**2 + (
    -0.48802820785090784 + m.x284)**2 + (-0.08187934237116656 + m.x285)**2) +
    m.x124 - 1.7320508075688772 * m.b436 >= -1.7320508075688772)
m.e125 = Constraint(expr= -sqrt((-0.33873348699206973 + m.x283)**2 + (
    -0.07233360770535402 + m.x284)**2 + (-0.011036367079899967 + m.x285)**2) +
    m.x125 - 1.7320508075688772 * m.b437 >= -1.7320508075688772)
m.e126 = Constraint(expr= -sqrt((-0.28385029589876865 + m.x283)**2 + (
    -0.11770636555802805 + m.x284)**2 + (-0.3110382248120007 + m.x285)**2) +
    m.x126 - 1.7320508075688772 * m.b438 >= -1.7320508075688772)
m.e127 = Constraint(expr= -sqrt((-0.7434707928397064 + m.x283)**2 + (
    -0.0357557155126923 + m.x284)**2 + (-0.6249375571804716 + m.x285)**2) +
    m.x127 - 1.7320508075688772 * m.b439 >= -1.7320508075688772)
m.e128 = Constraint(expr= -sqrt((-0.13501116090704035 + m.x283)**2 + (
    -0.7950712434655829 + m.x284)**2 + (-0.7369676243821022 + m.x285)**2) +
    m.x128 - 1.7320508075688772 * m.b440 >= -1.7320508075688772)
m.e129 = Constraint(expr= -sqrt((-0.21101029956774453 + m.x283)**2 + (
    -0.8480765801722641 + m.x284)**2 + (-0.7173017220824032 + m.x285)**2) +
    m.x129 - 1.7320508075688772 * m.b441 >= -1.7320508075688772)
m.e130 = Constraint(expr= -sqrt((-0.07495132545320449 + m.x283)**2 + (
    -0.4081313844234159 + m.x284)**2 + (-0.7004510913580178 + m.x285)**2) +
    m.x130 - 1.7320508075688772 * m.b442 >= -1.7320508075688772)
m.e131 = Constraint(expr= -sqrt((-0.9229582476032371 + m.x283)**2 + (
    -0.17221119493742953 + m.x284)**2 + (-0.2518629905323574 + m.x285)**2) +
    m.x131 - 1.7320508075688772 * m.b443 >= -1.7320508075688772)
m.e132 = Constraint(expr= -sqrt((-0.7750929946094214 + m.x283)**2 + (
    -0.9626723030210862 + m.x284)**2 + (-0.09375460752394849 + m.x285)**2) +
    m.x132 - 1.7320508075688772 * m.b444 >= -1.7320508075688772)
m.e133 = Constraint(expr= -sqrt((-0.08982827530229975 + m.x283)**2 + (
    -0.7511793846525663 + m.x284)**2 + (-0.3169893159261734 + m.x285)**2) +
    m.x133 - 1.7320508075688772 * m.b445 >= -1.7320508075688772)
m.e134 = Constraint(expr= -sqrt((-0.38677647485720235 + m.x283)**2 + (
    -0.87633207391825 + m.x284)**2 + (-0.7457995156246497 + m.x285)**2) +
    m.x134 - 1.7320508075688772 * m.b446 >= -1.7320508075688772)
m.e135 = Constraint(expr= -sqrt((-0.6607159863179267 + m.x283)**2 + (
    -0.8676520260577261 + m.x284)**2 + (-0.7320438297162596 + m.x285)**2) +
    m.x135 - 1.7320508075688772 * m.b447 >= -1.7320508075688772)
m.e136 = Constraint(expr= -sqrt((-0.8102488868102232 + m.x283)**2 + (
    -0.6432507057061979 + m.x284)**2 + (-0.5931582872810908 + m.x285)**2) +
    m.x136 - 1.7320508075688772 * m.b448 >= -1.7320508075688772)
m.e137 = Constraint(expr= -sqrt((-0.05986505368858752 + m.x283)**2 + (
    -0.909611607891918 + m.x284)**2 + (-0.9117643699770345 + m.x285)**2) +
    m.x137 - 1.7320508075688772 * m.b449 >= -1.7320508075688772)
m.e138 = Constraint(expr= -sqrt((-0.35134351369704286 + m.x283)**2 + (
    -0.6263463928446534 + m.x284)**2 + (-0.01689904369168782 + m.x285)**2) +
    m.x138 - 1.7320508075688772 * m.b450 >= -1.7320508075688772)
m.e139 = Constraint(expr= -sqrt((-0.2718754143840908 + m.x286)**2 + (
    -0.48802820785090784 + m.x287)**2 + (-0.08187934237116656 + m.x288)**2) +
    m.x139 - 1.7320508075688772 * m.b451 >= -1.7320508075688772)
m.e140 = Constraint(expr= -sqrt((-0.33873348699206973 + m.x286)**2 + (
    -0.07233360770535402 + m.x287)**2 + (-0.011036367079899967 + m.x288)**2) +
    m.x140 - 1.7320508075688772 * m.b452 >= -1.7320508075688772)
m.e141 = Constraint(expr= -sqrt((-0.28385029589876865 + m.x286)**2 + (
    -0.11770636555802805 + m.x287)**2 + (-0.3110382248120007 + m.x288)**2) +
    m.x141 - 1.7320508075688772 * m.b453 >= -1.7320508075688772)
m.e142 = Constraint(expr= -sqrt((-0.7434707928397064 + m.x286)**2 + (
    -0.0357557155126923 + m.x287)**2 + (-0.6249375571804716 + m.x288)**2) +
    m.x142 - 1.7320508075688772 * m.b454 >= -1.7320508075688772)
m.e143 = Constraint(expr= -sqrt((-0.13501116090704035 + m.x286)**2 + (
    -0.7950712434655829 + m.x287)**2 + (-0.7369676243821022 + m.x288)**2) +
    m.x143 - 1.7320508075688772 * m.b455 >= -1.7320508075688772)
m.e144 = Constraint(expr= -sqrt((-0.21101029956774453 + m.x286)**2 + (
    -0.8480765801722641 + m.x287)**2 + (-0.7173017220824032 + m.x288)**2) +
    m.x144 - 1.7320508075688772 * m.b456 >= -1.7320508075688772)
m.e145 = Constraint(expr= -sqrt((-0.07495132545320449 + m.x286)**2 + (
    -0.4081313844234159 + m.x287)**2 + (-0.7004510913580178 + m.x288)**2) +
    m.x145 - 1.7320508075688772 * m.b457 >= -1.7320508075688772)
m.e146 = Constraint(expr= -sqrt((-0.9229582476032371 + m.x286)**2 + (
    -0.17221119493742953 + m.x287)**2 + (-0.2518629905323574 + m.x288)**2) +
    m.x146 - 1.7320508075688772 * m.b458 >= -1.7320508075688772)
m.e147 = Constraint(expr= -sqrt((-0.7750929946094214 + m.x286)**2 + (
    -0.9626723030210862 + m.x287)**2 + (-0.09375460752394849 + m.x288)**2) +
    m.x147 - 1.7320508075688772 * m.b459 >= -1.7320508075688772)
m.e148 = Constraint(expr= -sqrt((-0.08982827530229975 + m.x286)**2 + (
    -0.7511793846525663 + m.x287)**2 + (-0.3169893159261734 + m.x288)**2) +
    m.x148 - 1.7320508075688772 * m.b460 >= -1.7320508075688772)
m.e149 = Constraint(expr= -sqrt((-0.38677647485720235 + m.x286)**2 + (
    -0.87633207391825 + m.x287)**2 + (-0.7457995156246497 + m.x288)**2) +
    m.x149 - 1.7320508075688772 * m.b461 >= -1.7320508075688772)
m.e150 = Constraint(expr= -sqrt((-0.6607159863179267 + m.x286)**2 + (
    -0.8676520260577261 + m.x287)**2 + (-0.7320438297162596 + m.x288)**2) +
    m.x150 - 1.7320508075688772 * m.b462 >= -1.7320508075688772)
m.e151 = Constraint(expr= -sqrt((-0.8102488868102232 + m.x286)**2 + (
    -0.6432507057061979 + m.x287)**2 + (-0.5931582872810908 + m.x288)**2) +
    m.x151 - 1.7320508075688772 * m.b463 >= -1.7320508075688772)
m.e152 = Constraint(expr= -sqrt((-0.05986505368858752 + m.x286)**2 + (
    -0.909611607891918 + m.x287)**2 + (-0.9117643699770345 + m.x288)**2) +
    m.x152 - 1.7320508075688772 * m.b464 >= -1.7320508075688772)
m.e153 = Constraint(expr= -sqrt((-0.35134351369704286 + m.x286)**2 + (
    -0.6263463928446534 + m.x287)**2 + (-0.01689904369168782 + m.x288)**2) +
    m.x153 - 1.7320508075688772 * m.b465 >= -1.7320508075688772)
m.e154 = Constraint(expr= -sqrt((-0.2718754143840908 + m.x289)**2 + (
    -0.48802820785090784 + m.x290)**2 + (-0.08187934237116656 + m.x291)**2) +
    m.x154 - 1.7320508075688772 * m.b466 >= -1.7320508075688772)
m.e155 = Constraint(expr= -sqrt((-0.33873348699206973 + m.x289)**2 + (
    -0.07233360770535402 + m.x290)**2 + (-0.011036367079899967 + m.x291)**2) +
    m.x155 - 1.7320508075688772 * m.b467 >= -1.7320508075688772)
m.e156 = Constraint(expr= -sqrt((-0.28385029589876865 + m.x289)**2 + (
    -0.11770636555802805 + m.x290)**2 + (-0.3110382248120007 + m.x291)**2) +
    m.x156 - 1.7320508075688772 * m.b468 >= -1.7320508075688772)
m.e157 = Constraint(expr= -sqrt((-0.7434707928397064 + m.x289)**2 + (
    -0.0357557155126923 + m.x290)**2 + (-0.6249375571804716 + m.x291)**2) +
    m.x157 - 1.7320508075688772 * m.b469 >= -1.7320508075688772)
m.e158 = Constraint(expr= -sqrt((-0.13501116090704035 + m.x289)**2 + (
    -0.7950712434655829 + m.x290)**2 + (-0.7369676243821022 + m.x291)**2) +
    m.x158 - 1.7320508075688772 * m.b470 >= -1.7320508075688772)
m.e159 = Constraint(expr= -sqrt((-0.21101029956774453 + m.x289)**2 + (
    -0.8480765801722641 + m.x290)**2 + (-0.7173017220824032 + m.x291)**2) +
    m.x159 - 1.7320508075688772 * m.b471 >= -1.7320508075688772)
m.e160 = Constraint(expr= -sqrt((-0.07495132545320449 + m.x289)**2 + (
    -0.4081313844234159 + m.x290)**2 + (-0.7004510913580178 + m.x291)**2) +
    m.x160 - 1.7320508075688772 * m.b472 >= -1.7320508075688772)
m.e161 = Constraint(expr= -sqrt((-0.9229582476032371 + m.x289)**2 + (
    -0.17221119493742953 + m.x290)**2 + (-0.2518629905323574 + m.x291)**2) +
    m.x161 - 1.7320508075688772 * m.b473 >= -1.7320508075688772)
m.e162 = Constraint(expr= -sqrt((-0.7750929946094214 + m.x289)**2 + (
    -0.9626723030210862 + m.x290)**2 + (-0.09375460752394849 + m.x291)**2) +
    m.x162 - 1.7320508075688772 * m.b474 >= -1.7320508075688772)
m.e163 = Constraint(expr= -sqrt((-0.08982827530229975 + m.x289)**2 + (
    -0.7511793846525663 + m.x290)**2 + (-0.3169893159261734 + m.x291)**2) +
    m.x163 - 1.7320508075688772 * m.b475 >= -1.7320508075688772)
m.e164 = Constraint(expr= -sqrt((-0.38677647485720235 + m.x289)**2 + (
    -0.87633207391825 + m.x290)**2 + (-0.7457995156246497 + m.x291)**2) +
    m.x164 - 1.7320508075688772 * m.b476 >= -1.7320508075688772)
m.e165 = Constraint(expr= -sqrt((-0.6607159863179267 + m.x289)**2 + (
    -0.8676520260577261 + m.x290)**2 + (-0.7320438297162596 + m.x291)**2) +
    m.x165 - 1.7320508075688772 * m.b477 >= -1.7320508075688772)
m.e166 = Constraint(expr= -sqrt((-0.8102488868102232 + m.x289)**2 + (
    -0.6432507057061979 + m.x290)**2 + (-0.5931582872810908 + m.x291)**2) +
    m.x166 - 1.7320508075688772 * m.b478 >= -1.7320508075688772)
m.e167 = Constraint(expr= -sqrt((-0.05986505368858752 + m.x289)**2 + (
    -0.909611607891918 + m.x290)**2 + (-0.9117643699770345 + m.x291)**2) +
    m.x167 - 1.7320508075688772 * m.b479 >= -1.7320508075688772)
m.e168 = Constraint(expr= -sqrt((-0.35134351369704286 + m.x289)**2 + (
    -0.6263463928446534 + m.x290)**2 + (-0.01689904369168782 + m.x291)**2) +
    m.x168 - 1.7320508075688772 * m.b480 >= -1.7320508075688772)
m.e169 = Constraint(expr= -sqrt((-0.2718754143840908 + m.x292)**2 + (
    -0.48802820785090784 + m.x293)**2 + (-0.08187934237116656 + m.x294)**2) +
    m.x169 - 1.7320508075688772 * m.b481 >= -1.7320508075688772)
m.e170 = Constraint(expr= -sqrt((-0.33873348699206973 + m.x292)**2 + (
    -0.07233360770535402 + m.x293)**2 + (-0.011036367079899967 + m.x294)**2) +
    m.x170 - 1.7320508075688772 * m.b482 >= -1.7320508075688772)
m.e171 = Constraint(expr= -sqrt((-0.28385029589876865 + m.x292)**2 + (
    -0.11770636555802805 + m.x293)**2 + (-0.3110382248120007 + m.x294)**2) +
    m.x171 - 1.7320508075688772 * m.b483 >= -1.7320508075688772)
m.e172 = Constraint(expr= -sqrt((-0.7434707928397064 + m.x292)**2 + (
    -0.0357557155126923 + m.x293)**2 + (-0.6249375571804716 + m.x294)**2) +
    m.x172 - 1.7320508075688772 * m.b484 >= -1.7320508075688772)
m.e173 = Constraint(expr= -sqrt((-0.13501116090704035 + m.x292)**2 + (
    -0.7950712434655829 + m.x293)**2 + (-0.7369676243821022 + m.x294)**2) +
    m.x173 - 1.7320508075688772 * m.b485 >= -1.7320508075688772)
m.e174 = Constraint(expr= -sqrt((-0.21101029956774453 + m.x292)**2 + (
    -0.8480765801722641 + m.x293)**2 + (-0.7173017220824032 + m.x294)**2) +
    m.x174 - 1.7320508075688772 * m.b486 >= -1.7320508075688772)
m.e175 = Constraint(expr= -sqrt((-0.07495132545320449 + m.x292)**2 + (
    -0.4081313844234159 + m.x293)**2 + (-0.7004510913580178 + m.x294)**2) +
    m.x175 - 1.7320508075688772 * m.b487 >= -1.7320508075688772)
m.e176 = Constraint(expr= -sqrt((-0.9229582476032371 + m.x292)**2 + (
    -0.17221119493742953 + m.x293)**2 + (-0.2518629905323574 + m.x294)**2) +
    m.x176 - 1.7320508075688772 * m.b488 >= -1.7320508075688772)
m.e177 = Constraint(expr= -sqrt((-0.7750929946094214 + m.x292)**2 + (
    -0.9626723030210862 + m.x293)**2 + (-0.09375460752394849 + m.x294)**2) +
    m.x177 - 1.7320508075688772 * m.b489 >= -1.7320508075688772)
m.e178 = Constraint(expr= -sqrt((-0.08982827530229975 + m.x292)**2 + (
    -0.7511793846525663 + m.x293)**2 + (-0.3169893159261734 + m.x294)**2) +
    m.x178 - 1.7320508075688772 * m.b490 >= -1.7320508075688772)
m.e179 = Constraint(expr= -sqrt((-0.38677647485720235 + m.x292)**2 + (
    -0.87633207391825 + m.x293)**2 + (-0.7457995156246497 + m.x294)**2) +
    m.x179 - 1.7320508075688772 * m.b491 >= -1.7320508075688772)
m.e180 = Constraint(expr= -sqrt((-0.6607159863179267 + m.x292)**2 + (
    -0.8676520260577261 + m.x293)**2 + (-0.7320438297162596 + m.x294)**2) +
    m.x180 - 1.7320508075688772 * m.b492 >= -1.7320508075688772)
m.e181 = Constraint(expr= -sqrt((-0.8102488868102232 + m.x292)**2 + (
    -0.6432507057061979 + m.x293)**2 + (-0.5931582872810908 + m.x294)**2) +
    m.x181 - 1.7320508075688772 * m.b493 >= -1.7320508075688772)
m.e182 = Constraint(expr= -sqrt((-0.05986505368858752 + m.x292)**2 + (
    -0.909611607891918 + m.x293)**2 + (-0.9117643699770345 + m.x294)**2) +
    m.x182 - 1.7320508075688772 * m.b494 >= -1.7320508075688772)
m.e183 = Constraint(expr= -sqrt((-0.35134351369704286 + m.x292)**2 + (
    -0.6263463928446534 + m.x293)**2 + (-0.01689904369168782 + m.x294)**2) +
    m.x183 - 1.7320508075688772 * m.b495 >= -1.7320508075688772)
m.e184 = Constraint(expr= -sqrt((-0.2718754143840908 + m.x295)**2 + (
    -0.48802820785090784 + m.x296)**2 + (-0.08187934237116656 + m.x297)**2) +
    m.x184 - 1.7320508075688772 * m.b496 >= -1.7320508075688772)
m.e185 = Constraint(expr= -sqrt((-0.33873348699206973 + m.x295)**2 + (
    -0.07233360770535402 + m.x296)**2 + (-0.011036367079899967 + m.x297)**2) +
    m.x185 - 1.7320508075688772 * m.b497 >= -1.7320508075688772)
m.e186 = Constraint(expr= -sqrt((-0.28385029589876865 + m.x295)**2 + (
    -0.11770636555802805 + m.x296)**2 + (-0.3110382248120007 + m.x297)**2) +
    m.x186 - 1.7320508075688772 * m.b498 >= -1.7320508075688772)
m.e187 = Constraint(expr= -sqrt((-0.7434707928397064 + m.x295)**2 + (
    -0.0357557155126923 + m.x296)**2 + (-0.6249375571804716 + m.x297)**2) +
    m.x187 - 1.7320508075688772 * m.b499 >= -1.7320508075688772)
m.e188 = Constraint(expr= -sqrt((-0.13501116090704035 + m.x295)**2 + (
    -0.7950712434655829 + m.x296)**2 + (-0.7369676243821022 + m.x297)**2) +
    m.x188 - 1.7320508075688772 * m.b500 >= -1.7320508075688772)
m.e189 = Constraint(expr= -sqrt((-0.21101029956774453 + m.x295)**2 + (
    -0.8480765801722641 + m.x296)**2 + (-0.7173017220824032 + m.x297)**2) +
    m.x189 - 1.7320508075688772 * m.b501 >= -1.7320508075688772)
m.e190 = Constraint(expr= -sqrt((-0.07495132545320449 + m.x295)**2 + (
    -0.4081313844234159 + m.x296)**2 + (-0.7004510913580178 + m.x297)**2) +
    m.x190 - 1.7320508075688772 * m.b502 >= -1.7320508075688772)
m.e191 = Constraint(expr= -sqrt((-0.9229582476032371 + m.x295)**2 + (
    -0.17221119493742953 + m.x296)**2 + (-0.2518629905323574 + m.x297)**2) +
    m.x191 - 1.7320508075688772 * m.b503 >= -1.7320508075688772)
m.e192 = Constraint(expr= -sqrt((-0.7750929946094214 + m.x295)**2 + (
    -0.9626723030210862 + m.x296)**2 + (-0.09375460752394849 + m.x297)**2) +
    m.x192 - 1.7320508075688772 * m.b504 >= -1.7320508075688772)
m.e193 = Constraint(expr= -sqrt((-0.08982827530229975 + m.x295)**2 + (
    -0.7511793846525663 + m.x296)**2 + (-0.3169893159261734 + m.x297)**2) +
    m.x193 - 1.7320508075688772 * m.b505 >= -1.7320508075688772)
m.e194 = Constraint(expr= -sqrt((-0.38677647485720235 + m.x295)**2 + (
    -0.87633207391825 + m.x296)**2 + (-0.7457995156246497 + m.x297)**2) +
    m.x194 - 1.7320508075688772 * m.b506 >= -1.7320508075688772)
m.e195 = Constraint(expr= -sqrt((-0.6607159863179267 + m.x295)**2 + (
    -0.8676520260577261 + m.x296)**2 + (-0.7320438297162596 + m.x297)**2) +
    m.x195 - 1.7320508075688772 * m.b507 >= -1.7320508075688772)
m.e196 = Constraint(expr= -sqrt((-0.8102488868102232 + m.x295)**2 + (
    -0.6432507057061979 + m.x296)**2 + (-0.5931582872810908 + m.x297)**2) +
    m.x196 - 1.7320508075688772 * m.b508 >= -1.7320508075688772)
m.e197 = Constraint(expr= -sqrt((-0.05986505368858752 + m.x295)**2 + (
    -0.909611607891918 + m.x296)**2 + (-0.9117643699770345 + m.x297)**2) +
    m.x197 - 1.7320508075688772 * m.b509 >= -1.7320508075688772)
m.e198 = Constraint(expr= -sqrt((-0.35134351369704286 + m.x295)**2 + (
    -0.6263463928446534 + m.x296)**2 + (-0.01689904369168782 + m.x297)**2) +
    m.x198 - 1.7320508075688772 * m.b510 >= -1.7320508075688772)
m.e199 = Constraint(expr= -sqrt((-0.2718754143840908 + m.x298)**2 + (
    -0.48802820785090784 + m.x299)**2 + (-0.08187934237116656 + m.x300)**2) +
    m.x199 - 1.7320508075688772 * m.b511 >= -1.7320508075688772)
m.e200 = Constraint(expr= -sqrt((-0.33873348699206973 + m.x298)**2 + (
    -0.07233360770535402 + m.x299)**2 + (-0.011036367079899967 + m.x300)**2) +
    m.x200 - 1.7320508075688772 * m.b512 >= -1.7320508075688772)
m.e201 = Constraint(expr= -sqrt((-0.28385029589876865 + m.x298)**2 + (
    -0.11770636555802805 + m.x299)**2 + (-0.3110382248120007 + m.x300)**2) +
    m.x201 - 1.7320508075688772 * m.b513 >= -1.7320508075688772)
m.e202 = Constraint(expr= -sqrt((-0.7434707928397064 + m.x298)**2 + (
    -0.0357557155126923 + m.x299)**2 + (-0.6249375571804716 + m.x300)**2) +
    m.x202 - 1.7320508075688772 * m.b514 >= -1.7320508075688772)
m.e203 = Constraint(expr= -sqrt((-0.13501116090704035 + m.x298)**2 + (
    -0.7950712434655829 + m.x299)**2 + (-0.7369676243821022 + m.x300)**2) +
    m.x203 - 1.7320508075688772 * m.b515 >= -1.7320508075688772)
m.e204 = Constraint(expr= -sqrt((-0.21101029956774453 + m.x298)**2 + (
    -0.8480765801722641 + m.x299)**2 + (-0.7173017220824032 + m.x300)**2) +
    m.x204 - 1.7320508075688772 * m.b516 >= -1.7320508075688772)
m.e205 = Constraint(expr= -sqrt((-0.07495132545320449 + m.x298)**2 + (
    -0.4081313844234159 + m.x299)**2 + (-0.7004510913580178 + m.x300)**2) +
    m.x205 - 1.7320508075688772 * m.b517 >= -1.7320508075688772)
m.e206 = Constraint(expr= -sqrt((-0.9229582476032371 + m.x298)**2 + (
    -0.17221119493742953 + m.x299)**2 + (-0.2518629905323574 + m.x300)**2) +
    m.x206 - 1.7320508075688772 * m.b518 >= -1.7320508075688772)
m.e207 = Constraint(expr= -sqrt((-0.7750929946094214 + m.x298)**2 + (
    -0.9626723030210862 + m.x299)**2 + (-0.09375460752394849 + m.x300)**2) +
    m.x207 - 1.7320508075688772 * m.b519 >= -1.7320508075688772)
m.e208 = Constraint(expr= -sqrt((-0.08982827530229975 + m.x298)**2 + (
    -0.7511793846525663 + m.x299)**2 + (-0.3169893159261734 + m.x300)**2) +
    m.x208 - 1.7320508075688772 * m.b520 >= -1.7320508075688772)
m.e209 = Constraint(expr= -sqrt((-0.38677647485720235 + m.x298)**2 + (
    -0.87633207391825 + m.x299)**2 + (-0.7457995156246497 + m.x300)**2) +
    m.x209 - 1.7320508075688772 * m.b521 >= -1.7320508075688772)
m.e210 = Constraint(expr= -sqrt((-0.6607159863179267 + m.x298)**2 + (
    -0.8676520260577261 + m.x299)**2 + (-0.7320438297162596 + m.x300)**2) +
    m.x210 - 1.7320508075688772 * m.b522 >= -1.7320508075688772)
m.e211 = Constraint(expr= -sqrt((-0.8102488868102232 + m.x298)**2 + (
    -0.6432507057061979 + m.x299)**2 + (-0.5931582872810908 + m.x300)**2) +
    m.x211 - 1.7320508075688772 * m.b523 >= -1.7320508075688772)
m.e212 = Constraint(expr= -sqrt((-0.05986505368858752 + m.x298)**2 + (
    -0.909611607891918 + m.x299)**2 + (-0.9117643699770345 + m.x300)**2) +
    m.x212 - 1.7320508075688772 * m.b524 >= -1.7320508075688772)
m.e213 = Constraint(expr= -sqrt((-0.35134351369704286 + m.x298)**2 + (
    -0.6263463928446534 + m.x299)**2 + (-0.01689904369168782 + m.x300)**2) +
    m.x213 - 1.7320508075688772 * m.b525 >= -1.7320508075688772)
m.e214 = Constraint(expr= -sqrt((-0.2718754143840908 + m.x301)**2 + (
    -0.48802820785090784 + m.x302)**2 + (-0.08187934237116656 + m.x303)**2) +
    m.x214 - 1.7320508075688772 * m.b526 >= -1.7320508075688772)
m.e215 = Constraint(expr= -sqrt((-0.33873348699206973 + m.x301)**2 + (
    -0.07233360770535402 + m.x302)**2 + (-0.011036367079899967 + m.x303)**2) +
    m.x215 - 1.7320508075688772 * m.b527 >= -1.7320508075688772)
m.e216 = Constraint(expr= -sqrt((-0.28385029589876865 + m.x301)**2 + (
    -0.11770636555802805 + m.x302)**2 + (-0.3110382248120007 + m.x303)**2) +
    m.x216 - 1.7320508075688772 * m.b528 >= -1.7320508075688772)
m.e217 = Constraint(expr= -sqrt((-0.7434707928397064 + m.x301)**2 + (
    -0.0357557155126923 + m.x302)**2 + (-0.6249375571804716 + m.x303)**2) +
    m.x217 - 1.7320508075688772 * m.b529 >= -1.7320508075688772)
m.e218 = Constraint(expr= -sqrt((-0.13501116090704035 + m.x301)**2 + (
    -0.7950712434655829 + m.x302)**2 + (-0.7369676243821022 + m.x303)**2) +
    m.x218 - 1.7320508075688772 * m.b530 >= -1.7320508075688772)
m.e219 = Constraint(expr= -sqrt((-0.21101029956774453 + m.x301)**2 + (
    -0.8480765801722641 + m.x302)**2 + (-0.7173017220824032 + m.x303)**2) +
    m.x219 - 1.7320508075688772 * m.b531 >= -1.7320508075688772)
m.e220 = Constraint(expr= -sqrt((-0.07495132545320449 + m.x301)**2 + (
    -0.4081313844234159 + m.x302)**2 + (-0.7004510913580178 + m.x303)**2) +
    m.x220 - 1.7320508075688772 * m.b532 >= -1.7320508075688772)
m.e221 = Constraint(expr= -sqrt((-0.9229582476032371 + m.x301)**2 + (
    -0.17221119493742953 + m.x302)**2 + (-0.2518629905323574 + m.x303)**2) +
    m.x221 - 1.7320508075688772 * m.b533 >= -1.7320508075688772)
m.e222 = Constraint(expr= -sqrt((-0.7750929946094214 + m.x301)**2 + (
    -0.9626723030210862 + m.x302)**2 + (-0.09375460752394849 + m.x303)**2) +
    m.x222 - 1.7320508075688772 * m.b534 >= -1.7320508075688772)
m.e223 = Constraint(expr= -sqrt((-0.08982827530229975 + m.x301)**2 + (
    -0.7511793846525663 + m.x302)**2 + (-0.3169893159261734 + m.x303)**2) +
    m.x223 - 1.7320508075688772 * m.b535 >= -1.7320508075688772)
m.e224 = Constraint(expr= -sqrt((-0.38677647485720235 + m.x301)**2 + (
    -0.87633207391825 + m.x302)**2 + (-0.7457995156246497 + m.x303)**2) +
    m.x224 - 1.7320508075688772 * m.b536 >= -1.7320508075688772)
m.e225 = Constraint(expr= -sqrt((-0.6607159863179267 + m.x301)**2 + (
    -0.8676520260577261 + m.x302)**2 + (-0.7320438297162596 + m.x303)**2) +
    m.x225 - 1.7320508075688772 * m.b537 >= -1.7320508075688772)
m.e226 = Constraint(expr= -sqrt((-0.8102488868102232 + m.x301)**2 + (
    -0.6432507057061979 + m.x302)**2 + (-0.5931582872810908 + m.x303)**2) +
    m.x226 - 1.7320508075688772 * m.b538 >= -1.7320508075688772)
m.e227 = Constraint(expr= -sqrt((-0.05986505368858752 + m.x301)**2 + (
    -0.909611607891918 + m.x302)**2 + (-0.9117643699770345 + m.x303)**2) +
    m.x227 - 1.7320508075688772 * m.b539 >= -1.7320508075688772)
m.e228 = Constraint(expr= -sqrt((-0.35134351369704286 + m.x301)**2 + (
    -0.6263463928446534 + m.x302)**2 + (-0.01689904369168782 + m.x303)**2) +
    m.x228 - 1.7320508075688772 * m.b540 >= -1.7320508075688772)
m.e229 = Constraint(expr= -sqrt((-0.2718754143840908 + m.x304)**2 + (
    -0.48802820785090784 + m.x305)**2 + (-0.08187934237116656 + m.x306)**2) +
    m.x229 - 1.7320508075688772 * m.b541 >= -1.7320508075688772)
m.e230 = Constraint(expr= -sqrt((-0.33873348699206973 + m.x304)**2 + (
    -0.07233360770535402 + m.x305)**2 + (-0.011036367079899967 + m.x306)**2) +
    m.x230 - 1.7320508075688772 * m.b542 >= -1.7320508075688772)
m.e231 = Constraint(expr= -sqrt((-0.28385029589876865 + m.x304)**2 + (
    -0.11770636555802805 + m.x305)**2 + (-0.3110382248120007 + m.x306)**2) +
    m.x231 - 1.7320508075688772 * m.b543 >= -1.7320508075688772)
m.e232 = Constraint(expr= -sqrt((-0.7434707928397064 + m.x304)**2 + (
    -0.0357557155126923 + m.x305)**2 + (-0.6249375571804716 + m.x306)**2) +
    m.x232 - 1.7320508075688772 * m.b544 >= -1.7320508075688772)
m.e233 = Constraint(expr= -sqrt((-0.13501116090704035 + m.x304)**2 + (
    -0.7950712434655829 + m.x305)**2 + (-0.7369676243821022 + m.x306)**2) +
    m.x233 - 1.7320508075688772 * m.b545 >= -1.7320508075688772)
m.e234 = Constraint(expr= -sqrt((-0.21101029956774453 + m.x304)**2 + (
    -0.8480765801722641 + m.x305)**2 + (-0.7173017220824032 + m.x306)**2) +
    m.x234 - 1.7320508075688772 * m.b546 >= -1.7320508075688772)
m.e235 = Constraint(expr= -sqrt((-0.07495132545320449 + m.x304)**2 + (
    -0.4081313844234159 + m.x305)**2 + (-0.7004510913580178 + m.x306)**2) +
    m.x235 - 1.7320508075688772 * m.b547 >= -1.7320508075688772)
m.e236 = Constraint(expr= -sqrt((-0.9229582476032371 + m.x304)**2 + (
    -0.17221119493742953 + m.x305)**2 + (-0.2518629905323574 + m.x306)**2) +
    m.x236 - 1.7320508075688772 * m.b548 >= -1.7320508075688772)
m.e237 = Constraint(expr= -sqrt((-0.7750929946094214 + m.x304)**2 + (
    -0.9626723030210862 + m.x305)**2 + (-0.09375460752394849 + m.x306)**2) +
    m.x237 - 1.7320508075688772 * m.b549 >= -1.7320508075688772)
m.e238 = Constraint(expr= -sqrt((-0.08982827530229975 + m.x304)**2 + (
    -0.7511793846525663 + m.x305)**2 + (-0.3169893159261734 + m.x306)**2) +
    m.x238 - 1.7320508075688772 * m.b550 >= -1.7320508075688772)
m.e239 = Constraint(expr= -sqrt((-0.38677647485720235 + m.x304)**2 + (
    -0.87633207391825 + m.x305)**2 + (-0.7457995156246497 + m.x306)**2) +
    m.x239 - 1.7320508075688772 * m.b551 >= -1.7320508075688772)
m.e240 = Constraint(expr= -sqrt((-0.6607159863179267 + m.x304)**2 + (
    -0.8676520260577261 + m.x305)**2 + (-0.7320438297162596 + m.x306)**2) +
    m.x240 - 1.7320508075688772 * m.b552 >= -1.7320508075688772)
m.e241 = Constraint(expr= -sqrt((-0.8102488868102232 + m.x304)**2 + (
    -0.6432507057061979 + m.x305)**2 + (-0.5931582872810908 + m.x306)**2) +
    m.x241 - 1.7320508075688772 * m.b553 >= -1.7320508075688772)
m.e242 = Constraint(expr= -sqrt((-0.05986505368858752 + m.x304)**2 + (
    -0.909611607891918 + m.x305)**2 + (-0.9117643699770345 + m.x306)**2) +
    m.x242 - 1.7320508075688772 * m.b554 >= -1.7320508075688772)
m.e243 = Constraint(expr= -sqrt((-0.35134351369704286 + m.x304)**2 + (
    -0.6263463928446534 + m.x305)**2 + (-0.01689904369168782 + m.x306)**2) +
    m.x243 - 1.7320508075688772 * m.b555 >= -1.7320508075688772)
m.e244 = Constraint(expr= -sqrt((-0.2718754143840908 + m.x307)**2 + (
    -0.48802820785090784 + m.x308)**2 + (-0.08187934237116656 + m.x309)**2) +
    m.x244 - 1.7320508075688772 * m.b556 >= -1.7320508075688772)
m.e245 = Constraint(expr= -sqrt((-0.33873348699206973 + m.x307)**2 + (
    -0.07233360770535402 + m.x308)**2 + (-0.011036367079899967 + m.x309)**2) +
    m.x245 - 1.7320508075688772 * m.b557 >= -1.7320508075688772)
m.e246 = Constraint(expr= -sqrt((-0.28385029589876865 + m.x307)**2 + (
    -0.11770636555802805 + m.x308)**2 + (-0.3110382248120007 + m.x309)**2) +
    m.x246 - 1.7320508075688772 * m.b558 >= -1.7320508075688772)
m.e247 = Constraint(expr= -sqrt((-0.7434707928397064 + m.x307)**2 + (
    -0.0357557155126923 + m.x308)**2 + (-0.6249375571804716 + m.x309)**2) +
    m.x247 - 1.7320508075688772 * m.b559 >= -1.7320508075688772)
m.e248 = Constraint(expr= -sqrt((-0.13501116090704035 + m.x307)**2 + (
    -0.7950712434655829 + m.x308)**2 + (-0.7369676243821022 + m.x309)**2) +
    m.x248 - 1.7320508075688772 * m.b560 >= -1.7320508075688772)
m.e249 = Constraint(expr= -sqrt((-0.21101029956774453 + m.x307)**2 + (
    -0.8480765801722641 + m.x308)**2 + (-0.7173017220824032 + m.x309)**2) +
    m.x249 - 1.7320508075688772 * m.b561 >= -1.7320508075688772)
m.e250 = Constraint(expr= -sqrt((-0.07495132545320449 + m.x307)**2 + (
    -0.4081313844234159 + m.x308)**2 + (-0.7004510913580178 + m.x309)**2) +
    m.x250 - 1.7320508075688772 * m.b562 >= -1.7320508075688772)
m.e251 = Constraint(expr= -sqrt((-0.9229582476032371 + m.x307)**2 + (
    -0.17221119493742953 + m.x308)**2 + (-0.2518629905323574 + m.x309)**2) +
    m.x251 - 1.7320508075688772 * m.b563 >= -1.7320508075688772)
m.e252 = Constraint(expr= -sqrt((-0.7750929946094214 + m.x307)**2 + (
    -0.9626723030210862 + m.x308)**2 + (-0.09375460752394849 + m.x309)**2) +
    m.x252 - 1.7320508075688772 * m.b564 >= -1.7320508075688772)
m.e253 = Constraint(expr= -sqrt((-0.08982827530229975 + m.x307)**2 + (
    -0.7511793846525663 + m.x308)**2 + (-0.3169893159261734 + m.x309)**2) +
    m.x253 - 1.7320508075688772 * m.b565 >= -1.7320508075688772)
m.e254 = Constraint(expr= -sqrt((-0.38677647485720235 + m.x307)**2 + (
    -0.87633207391825 + m.x308)**2 + (-0.7457995156246497 + m.x309)**2) +
    m.x254 - 1.7320508075688772 * m.b566 >= -1.7320508075688772)
m.e255 = Constraint(expr= -sqrt((-0.6607159863179267 + m.x307)**2 + (
    -0.8676520260577261 + m.x308)**2 + (-0.7320438297162596 + m.x309)**2) +
    m.x255 - 1.7320508075688772 * m.b567 >= -1.7320508075688772)
m.e256 = Constraint(expr= -sqrt((-0.8102488868102232 + m.x307)**2 + (
    -0.6432507057061979 + m.x308)**2 + (-0.5931582872810908 + m.x309)**2) +
    m.x256 - 1.7320508075688772 * m.b568 >= -1.7320508075688772)
m.e257 = Constraint(expr= -sqrt((-0.05986505368858752 + m.x307)**2 + (
    -0.909611607891918 + m.x308)**2 + (-0.9117643699770345 + m.x309)**2) +
    m.x257 - 1.7320508075688772 * m.b569 >= -1.7320508075688772)
m.e258 = Constraint(expr= -sqrt((-0.35134351369704286 + m.x307)**2 + (
    -0.6263463928446534 + m.x308)**2 + (-0.01689904369168782 + m.x309)**2) +
    m.x258 - 1.7320508075688772 * m.b570 >= -1.7320508075688772)
m.e259 = Constraint(expr= -sqrt((-0.2718754143840908 + m.x310)**2 + (
    -0.48802820785090784 + m.x311)**2 + (-0.08187934237116656 + m.x312)**2) +
    m.x259 - 1.7320508075688772 * m.b571 >= -1.7320508075688772)
m.e260 = Constraint(expr= -sqrt((-0.33873348699206973 + m.x310)**2 + (
    -0.07233360770535402 + m.x311)**2 + (-0.011036367079899967 + m.x312)**2) +
    m.x260 - 1.7320508075688772 * m.b572 >= -1.7320508075688772)
m.e261 = Constraint(expr= -sqrt((-0.28385029589876865 + m.x310)**2 + (
    -0.11770636555802805 + m.x311)**2 + (-0.3110382248120007 + m.x312)**2) +
    m.x261 - 1.7320508075688772 * m.b573 >= -1.7320508075688772)
m.e262 = Constraint(expr= -sqrt((-0.7434707928397064 + m.x310)**2 + (
    -0.0357557155126923 + m.x311)**2 + (-0.6249375571804716 + m.x312)**2) +
    m.x262 - 1.7320508075688772 * m.b574 >= -1.7320508075688772)
m.e263 = Constraint(expr= -sqrt((-0.13501116090704035 + m.x310)**2 + (
    -0.7950712434655829 + m.x311)**2 + (-0.7369676243821022 + m.x312)**2) +
    m.x263 - 1.7320508075688772 * m.b575 >= -1.7320508075688772)
m.e264 = Constraint(expr= -sqrt((-0.21101029956774453 + m.x310)**2 + (
    -0.8480765801722641 + m.x311)**2 + (-0.7173017220824032 + m.x312)**2) +
    m.x264 - 1.7320508075688772 * m.b576 >= -1.7320508075688772)
m.e265 = Constraint(expr= -sqrt((-0.07495132545320449 + m.x310)**2 + (
    -0.4081313844234159 + m.x311)**2 + (-0.7004510913580178 + m.x312)**2) +
    m.x265 - 1.7320508075688772 * m.b577 >= -1.7320508075688772)
m.e266 = Constraint(expr= -sqrt((-0.9229582476032371 + m.x310)**2 + (
    -0.17221119493742953 + m.x311)**2 + (-0.2518629905323574 + m.x312)**2) +
    m.x266 - 1.7320508075688772 * m.b578 >= -1.7320508075688772)
m.e267 = Constraint(expr= -sqrt((-0.7750929946094214 + m.x310)**2 + (
    -0.9626723030210862 + m.x311)**2 + (-0.09375460752394849 + m.x312)**2) +
    m.x267 - 1.7320508075688772 * m.b579 >= -1.7320508075688772)
m.e268 = Constraint(expr= -sqrt((-0.08982827530229975 + m.x310)**2 + (
    -0.7511793846525663 + m.x311)**2 + (-0.3169893159261734 + m.x312)**2) +
    m.x268 - 1.7320508075688772 * m.b580 >= -1.7320508075688772)
m.e269 = Constraint(expr= -sqrt((-0.38677647485720235 + m.x310)**2 + (
    -0.87633207391825 + m.x311)**2 + (-0.7457995156246497 + m.x312)**2) +
    m.x269 - 1.7320508075688772 * m.b581 >= -1.7320508075688772)
m.e270 = Constraint(expr= -sqrt((-0.6607159863179267 + m.x310)**2 + (
    -0.8676520260577261 + m.x311)**2 + (-0.7320438297162596 + m.x312)**2) +
    m.x270 - 1.7320508075688772 * m.b582 >= -1.7320508075688772)
m.e271 = Constraint(expr= -sqrt((-0.8102488868102232 + m.x310)**2 + (
    -0.6432507057061979 + m.x311)**2 + (-0.5931582872810908 + m.x312)**2) +
    m.x271 - 1.7320508075688772 * m.b583 >= -1.7320508075688772)
m.e272 = Constraint(expr= -sqrt((-0.05986505368858752 + m.x310)**2 + (
    -0.909611607891918 + m.x311)**2 + (-0.9117643699770345 + m.x312)**2) +
    m.x272 - 1.7320508075688772 * m.b584 >= -1.7320508075688772)
m.e273 = Constraint(expr= -sqrt((-0.35134351369704286 + m.x310)**2 + (
    -0.6263463928446534 + m.x311)**2 + (-0.01689904369168782 + m.x312)**2) +
    m.x273 - 1.7320508075688772 * m.b585 >= -1.7320508075688772)
m.e274 = Constraint(expr= m.b391 + m.b406 + m.b421 + m.b436 + m.b451 + m.b466
    + m.b481 + m.b496 + m.b511 + m.b526 + m.b541 + m.b556 + m.b571 == 1)
m.e275 = Constraint(expr= m.b392 + m.b407 + m.b422 + m.b437 + m.b452 + m.b467
    + m.b482 + m.b497 + m.b512 + m.b527 + m.b542 + m.b557 + m.b572 == 1)
m.e276 = Constraint(expr= m.b393 + m.b408 + m.b423 + m.b438 + m.b453 + m.b468
    + m.b483 + m.b498 + m.b513 + m.b528 + m.b543 + m.b558 + m.b573 == 1)
m.e277 = Constraint(expr= m.b394 + m.b409 + m.b424 + m.b439 + m.b454 + m.b469
    + m.b484 + m.b499 + m.b514 + m.b529 + m.b544 + m.b559 + m.b574 == 1)
m.e278 = Constraint(expr= m.b395 + m.b410 + m.b425 + m.b440 + m.b455 + m.b470
    + m.b485 + m.b500 + m.b515 + m.b530 + m.b545 + m.b560 + m.b575 == 1)
m.e279 = Constraint(expr= m.b396 + m.b411 + m.b426 + m.b441 + m.b456 + m.b471
    + m.b486 + m.b501 + m.b516 + m.b531 + m.b546 + m.b561 + m.b576 == 1)
m.e280 = Constraint(expr= m.b397 + m.b412 + m.b427 + m.b442 + m.b457 + m.b472
    + m.b487 + m.b502 + m.b517 + m.b532 + m.b547 + m.b562 + m.b577 == 1)
m.e281 = Constraint(expr= m.b398 + m.b413 + m.b428 + m.b443 + m.b458 + m.b473
    + m.b488 + m.b503 + m.b518 + m.b533 + m.b548 + m.b563 + m.b578 == 1)
m.e282 = Constraint(expr= m.b399 + m.b414 + m.b429 + m.b444 + m.b459 + m.b474
    + m.b489 + m.b504 + m.b519 + m.b534 + m.b549 + m.b564 + m.b579 == 1)
m.e283 = Constraint(expr= m.b400 + m.b415 + m.b430 + m.b445 + m.b460 + m.b475
    + m.b490 + m.b505 + m.b520 + m.b535 + m.b550 + m.b565 + m.b580 == 1)
m.e284 = Constraint(expr= m.b401 + m.b416 + m.b431 + m.b446 + m.b461 + m.b476
    + m.b491 + m.b506 + m.b521 + m.b536 + m.b551 + m.b566 + m.b581 == 1)
m.e285 = Constraint(expr= m.b402 + m.b417 + m.b432 + m.b447 + m.b462 + m.b477
    + m.b492 + m.b507 + m.b522 + m.b537 + m.b552 + m.b567 + m.b582 == 1)
m.e286 = Constraint(expr= m.b403 + m.b418 + m.b433 + m.b448 + m.b463 + m.b478
    + m.b493 + m.b508 + m.b523 + m.b538 + m.b553 + m.b568 + m.b583 == 1)
m.e287 = Constraint(expr= m.b404 + m.b419 + m.b434 + m.b449 + m.b464 + m.b479
    + m.b494 + m.b509 + m.b524 + m.b539 + m.b554 + m.b569 + m.b584 == 1)
m.e288 = Constraint(expr= m.b405 + m.b420 + m.b435 + m.b450 + m.b465 + m.b480
    + m.b495 + m.b510 + m.b525 + m.b540 + m.b555 + m.b570 + m.b585 == 1)
m.e289 = Constraint(expr= m.b313 + m.b314 + m.b315 + m.b316 + m.b317 + m.b318
    + m.b319 + m.b320 + m.b321 + m.b322 + m.b323 + m.b324 + m.b391 + m.b392 +
    m.b393 + m.b394 + m.b395 + m.b396 + m.b397 + m.b398 + m.b399 + m.b400 +
    m.b401 + m.b402 + m.b403 + m.b404 + m.b405 == 3)
m.e290 = Constraint(expr= m.b313 + m.b325 + m.b326 + m.b327 + m.b328 + m.b329
    + m.b330 + m.b331 + m.b332 + m.b333 + m.b334 + m.b335 + m.b406 + m.b407 +
    m.b408 + m.b409 + m.b410 + m.b411 + m.b412 + m.b413 + m.b414 + m.b415 +
    m.b416 + m.b417 + m.b418 + m.b419 + m.b420 == 3)
m.e291 = Constraint(expr= m.b314 + m.b325 + m.b336 + m.b337 + m.b338 + m.b339
    + m.b340 + m.b341 + m.b342 + m.b343 + m.b344 + m.b345 + m.b421 + m.b422 +
    m.b423 + m.b424 + m.b425 + m.b426 + m.b427 + m.b428 + m.b429 + m.b430 +
    m.b431 + m.b432 + m.b433 + m.b434 + m.b435 == 3)
m.e292 = Constraint(expr= m.b315 + m.b326 + m.b336 + m.b346 + m.b347 + m.b348
    + m.b349 + m.b350 + m.b351 + m.b352 + m.b353 + m.b354 + m.b436 + m.b437 +
    m.b438 + m.b439 + m.b440 + m.b441 + m.b442 + m.b443 + m.b444 + m.b445 +
    m.b446 + m.b447 + m.b448 + m.b449 + m.b450 == 3)
m.e293 = Constraint(expr= m.b316 + m.b327 + m.b337 + m.b346 + m.b355 + m.b356
    + m.b357 + m.b358 + m.b359 + m.b360 + m.b361 + m.b362 + m.b451 + m.b452 +
    m.b453 + m.b454 + m.b455 + m.b456 + m.b457 + m.b458 + m.b459 + m.b460 +
    m.b461 + m.b462 + m.b463 + m.b464 + m.b465 == 3)
m.e294 = Constraint(expr= m.b317 + m.b328 + m.b338 + m.b347 + m.b355 + m.b363
    + m.b364 + m.b365 + m.b366 + m.b367 + m.b368 + m.b369 + m.b466 + m.b467 +
    m.b468 + m.b469 + m.b470 + m.b471 + m.b472 + m.b473 + m.b474 + m.b475 +
    m.b476 + m.b477 + m.b478 + m.b479 + m.b480 == 3)
m.e295 = Constraint(expr= m.b318 + m.b329 + m.b339 + m.b348 + m.b356 + m.b363
    + m.b370 + m.b371 + m.b372 + m.b373 + m.b374 + m.b375 + m.b481 + m.b482 +
    m.b483 + m.b484 + m.b485 + m.b486 + m.b487 + m.b488 + m.b489 + m.b490 +
    m.b491 + m.b492 + m.b493 + m.b494 + m.b495 == 3)
m.e296 = Constraint(expr= m.b319 + m.b330 + m.b340 + m.b349 + m.b357 + m.b364
    + m.b370 + m.b376 + m.b377 + m.b378 + m.b379 + m.b380 + m.b496 + m.b497 +
    m.b498 + m.b499 + m.b500 + m.b501 + m.b502 + m.b503 + m.b504 + m.b505 +
    m.b506 + m.b507 + m.b508 + m.b509 + m.b510 == 3)
m.e297 = Constraint(expr= m.b320 + m.b331 + m.b341 + m.b350 + m.b358 + m.b365
    + m.b371 + m.b376 + m.b381 + m.b382 + m.b383 + m.b384 + m.b511 + m.b512 +
    m.b513 + m.b514 + m.b515 + m.b516 + m.b517 + m.b518 + m.b519 + m.b520 +
    m.b521 + m.b522 + m.b523 + m.b524 + m.b525 == 3)
m.e298 = Constraint(expr= m.b321 + m.b332 + m.b342 + m.b351 + m.b359 + m.b366
    + m.b372 + m.b377 + m.b381 + m.b385 + m.b386 + m.b387 + m.b526 + m.b527 +
    m.b528 + m.b529 + m.b530 + m.b531 + m.b532 + m.b533 + m.b534 + m.b535 +
    m.b536 + m.b537 + m.b538 + m.b539 + m.b540 == 3)
m.e299 = Constraint(expr= m.b322 + m.b333 + m.b343 + m.b352 + m.b360 + m.b367
    + m.b373 + m.b378 + m.b382 + m.b385 + m.b388 + m.b389 + m.b541 + m.b542 +
    m.b543 + m.b544 + m.b545 + m.b546 + m.b547 + m.b548 + m.b549 + m.b550 +
    m.b551 + m.b552 + m.b553 + m.b554 + m.b555 == 3)
m.e300 = Constraint(expr= m.b323 + m.b334 + m.b344 + m.b353 + m.b361 + m.b368
    + m.b374 + m.b379 + m.b383 + m.b386 + m.b388 + m.b390 + m.b556 + m.b557 +
    m.b558 + m.b559 + m.b560 + m.b561 + m.b562 + m.b563 + m.b564 + m.b565 +
    m.b566 + m.b567 + m.b568 + m.b569 + m.b570 == 3)
m.e301 = Constraint(expr= m.b324 + m.b335 + m.b345 + m.b354 + m.b362 + m.b369
    + m.b375 + m.b380 + m.b384 + m.b387 + m.b389 + m.b390 + m.b571 + m.b572 +
    m.b573 + m.b574 + m.b575 + m.b576 + m.b577 + m.b578 + m.b579 + m.b580 +
    m.b581 + m.b582 + m.b583 + m.b584 + m.b585 == 3)
m.e302 = Constraint(expr= m.b313 == 1)
m.e303 = Constraint(expr= m.b314 + m.b325 == 1)
m.e304 = Constraint(expr= m.b315 + m.b326 + m.b336 == 1)
m.e305 = Constraint(expr= m.b316 + m.b327 + m.b337 + m.b346 == 1)
m.e306 = Constraint(expr= m.b317 + m.b328 + m.b338 + m.b347 + m.b355 == 1)
m.e307 = Constraint(expr= m.b318 + m.b329 + m.b339 + m.b348 + m.b356 + m.b363
    == 1)
m.e308 = Constraint(expr= m.b319 + m.b330 + m.b340 + m.b349 + m.b357 + m.b364
    + m.b370 == 1)
m.e309 = Constraint(expr= m.b320 + m.b331 + m.b341 + m.b350 + m.b358 + m.b365
    + m.b371 + m.b376 == 1)
m.e310 = Constraint(expr= m.b321 + m.b332 + m.b342 + m.b351 + m.b359 + m.b366
    + m.b372 + m.b377 + m.b381 == 1)
m.e311 = Constraint(expr= m.b322 + m.b333 + m.b343 + m.b352 + m.b360 + m.b367
    + m.b373 + m.b378 + m.b382 + m.b385 == 1)
m.e312 = Constraint(expr= m.b323 + m.b334 + m.b344 + m.b353 + m.b361 + m.b368
    + m.b374 + m.b379 + m.b383 + m.b386 + m.b388 == 1)
m.e313 = Constraint(expr= m.b324 + m.b335 + m.b345 + m.b354 + m.b362 + m.b369
    + m.b375 + m.b380 + m.b384 + m.b387 + m.b389 + m.b390 == 1)
