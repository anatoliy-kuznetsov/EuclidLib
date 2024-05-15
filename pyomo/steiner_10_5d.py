# MINLP written by GAMS Convert at 05/15/24 11:59:32
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       133       25      108        0        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#       256      148      108        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#      1140      460      680
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
m.x109 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x110 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x111 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x112 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x113 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x114 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x115 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x116 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x117 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x118 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x119 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x120 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x121 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x122 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x123 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x124 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x125 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x126 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x127 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x128 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x129 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x130 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x131 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x132 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x133 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x134 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x135 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x136 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x137 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x138 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x139 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x140 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x141 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x142 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x143 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x144 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x145 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x146 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x147 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x148 = Var(within=Reals, bounds=(0,1), initialize=0)
m.b149 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b150 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b151 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b152 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b153 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b154 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b155 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b156 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b157 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b158 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b159 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b160 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b161 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b162 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b163 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b164 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b165 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b166 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b167 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b168 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b169 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b170 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b171 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b172 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b173 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b174 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b175 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b176 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b177 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b178 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b179 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b180 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b181 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b182 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b183 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b184 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b185 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b186 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b187 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b188 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b189 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b190 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b191 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b192 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b193 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b194 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b195 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b196 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b197 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b198 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b199 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b200 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b201 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b202 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b203 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b204 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b205 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b206 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b207 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b208 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b209 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b210 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b211 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b212 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b213 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b214 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b215 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b216 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b217 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b218 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b219 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b220 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b221 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b222 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b223 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b224 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b225 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b226 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b227 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b228 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b229 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b230 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b231 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b232 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b233 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b234 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b235 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b236 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b237 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b238 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b239 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b240 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b241 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b242 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b243 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b244 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b245 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b246 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b247 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b248 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b249 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b250 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b251 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b252 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b253 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b254 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b255 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b256 = Var(within=Binary, bounds=(0,1), initialize=0)

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
    + m.x106 + m.x107 + m.x108)

m.e1 = Constraint(expr= -sqrt((m.x109 - m.x114)**2 + (m.x110 - m.x115)**2 + (
    m.x111 - m.x116)**2 + (m.x112 - m.x117)**2 + (m.x113 - m.x118)**2) + m.x1
    - 2.23606797749979 * m.b149 >= -2.23606797749979)
m.e2 = Constraint(expr= -sqrt((m.x109 - m.x119)**2 + (m.x110 - m.x120)**2 + (
    m.x111 - m.x121)**2 + (m.x112 - m.x122)**2 + (m.x113 - m.x123)**2) + m.x2
    - 2.23606797749979 * m.b150 >= -2.23606797749979)
m.e3 = Constraint(expr= -sqrt((m.x109 - m.x124)**2 + (m.x110 - m.x125)**2 + (
    m.x111 - m.x126)**2 + (m.x112 - m.x127)**2 + (m.x113 - m.x128)**2) + m.x3
    - 2.23606797749979 * m.b151 >= -2.23606797749979)
m.e4 = Constraint(expr= -sqrt((m.x109 - m.x129)**2 + (m.x110 - m.x130)**2 + (
    m.x111 - m.x131)**2 + (m.x112 - m.x132)**2 + (m.x113 - m.x133)**2) + m.x4
    - 2.23606797749979 * m.b152 >= -2.23606797749979)
m.e5 = Constraint(expr= -sqrt((m.x109 - m.x134)**2 + (m.x110 - m.x135)**2 + (
    m.x111 - m.x136)**2 + (m.x112 - m.x137)**2 + (m.x113 - m.x138)**2) + m.x5
    - 2.23606797749979 * m.b153 >= -2.23606797749979)
m.e6 = Constraint(expr= -sqrt((m.x109 - m.x139)**2 + (m.x110 - m.x140)**2 + (
    m.x111 - m.x141)**2 + (m.x112 - m.x142)**2 + (m.x113 - m.x143)**2) + m.x6
    - 2.23606797749979 * m.b154 >= -2.23606797749979)
m.e7 = Constraint(expr= -sqrt((m.x109 - m.x144)**2 + (m.x110 - m.x145)**2 + (
    m.x111 - m.x146)**2 + (m.x112 - m.x147)**2 + (m.x113 - m.x148)**2) + m.x7
    - 2.23606797749979 * m.b155 >= -2.23606797749979)
m.e8 = Constraint(expr= -sqrt((m.x114 - m.x119)**2 + (m.x115 - m.x120)**2 + (
    m.x116 - m.x121)**2 + (m.x117 - m.x122)**2 + (m.x118 - m.x123)**2) + m.x8
    - 2.23606797749979 * m.b156 >= -2.23606797749979)
m.e9 = Constraint(expr= -sqrt((m.x114 - m.x124)**2 + (m.x115 - m.x125)**2 + (
    m.x116 - m.x126)**2 + (m.x117 - m.x127)**2 + (m.x118 - m.x128)**2) + m.x9
    - 2.23606797749979 * m.b157 >= -2.23606797749979)
m.e10 = Constraint(expr= -sqrt((m.x114 - m.x129)**2 + (m.x115 - m.x130)**2 + (
    m.x116 - m.x131)**2 + (m.x117 - m.x132)**2 + (m.x118 - m.x133)**2) + m.x10
    - 2.23606797749979 * m.b158 >= -2.23606797749979)
m.e11 = Constraint(expr= -sqrt((m.x114 - m.x134)**2 + (m.x115 - m.x135)**2 + (
    m.x116 - m.x136)**2 + (m.x117 - m.x137)**2 + (m.x118 - m.x138)**2) + m.x11
    - 2.23606797749979 * m.b159 >= -2.23606797749979)
m.e12 = Constraint(expr= -sqrt((m.x114 - m.x139)**2 + (m.x115 - m.x140)**2 + (
    m.x116 - m.x141)**2 + (m.x117 - m.x142)**2 + (m.x118 - m.x143)**2) + m.x12
    - 2.23606797749979 * m.b160 >= -2.23606797749979)
m.e13 = Constraint(expr= -sqrt((m.x114 - m.x144)**2 + (m.x115 - m.x145)**2 + (
    m.x116 - m.x146)**2 + (m.x117 - m.x147)**2 + (m.x118 - m.x148)**2) + m.x13
    - 2.23606797749979 * m.b161 >= -2.23606797749979)
m.e14 = Constraint(expr= -sqrt((m.x119 - m.x124)**2 + (m.x120 - m.x125)**2 + (
    m.x121 - m.x126)**2 + (m.x122 - m.x127)**2 + (m.x123 - m.x128)**2) + m.x14
    - 2.23606797749979 * m.b162 >= -2.23606797749979)
m.e15 = Constraint(expr= -sqrt((m.x119 - m.x129)**2 + (m.x120 - m.x130)**2 + (
    m.x121 - m.x131)**2 + (m.x122 - m.x132)**2 + (m.x123 - m.x133)**2) + m.x15
    - 2.23606797749979 * m.b163 >= -2.23606797749979)
m.e16 = Constraint(expr= -sqrt((m.x119 - m.x134)**2 + (m.x120 - m.x135)**2 + (
    m.x121 - m.x136)**2 + (m.x122 - m.x137)**2 + (m.x123 - m.x138)**2) + m.x16
    - 2.23606797749979 * m.b164 >= -2.23606797749979)
m.e17 = Constraint(expr= -sqrt((m.x119 - m.x139)**2 + (m.x120 - m.x140)**2 + (
    m.x121 - m.x141)**2 + (m.x122 - m.x142)**2 + (m.x123 - m.x143)**2) + m.x17
    - 2.23606797749979 * m.b165 >= -2.23606797749979)
m.e18 = Constraint(expr= -sqrt((m.x119 - m.x144)**2 + (m.x120 - m.x145)**2 + (
    m.x121 - m.x146)**2 + (m.x122 - m.x147)**2 + (m.x123 - m.x148)**2) + m.x18
    - 2.23606797749979 * m.b166 >= -2.23606797749979)
m.e19 = Constraint(expr= -sqrt((m.x124 - m.x129)**2 + (m.x125 - m.x130)**2 + (
    m.x126 - m.x131)**2 + (m.x127 - m.x132)**2 + (m.x128 - m.x133)**2) + m.x19
    - 2.23606797749979 * m.b167 >= -2.23606797749979)
m.e20 = Constraint(expr= -sqrt((m.x124 - m.x134)**2 + (m.x125 - m.x135)**2 + (
    m.x126 - m.x136)**2 + (m.x127 - m.x137)**2 + (m.x128 - m.x138)**2) + m.x20
    - 2.23606797749979 * m.b168 >= -2.23606797749979)
m.e21 = Constraint(expr= -sqrt((m.x124 - m.x139)**2 + (m.x125 - m.x140)**2 + (
    m.x126 - m.x141)**2 + (m.x127 - m.x142)**2 + (m.x128 - m.x143)**2) + m.x21
    - 2.23606797749979 * m.b169 >= -2.23606797749979)
m.e22 = Constraint(expr= -sqrt((m.x124 - m.x144)**2 + (m.x125 - m.x145)**2 + (
    m.x126 - m.x146)**2 + (m.x127 - m.x147)**2 + (m.x128 - m.x148)**2) + m.x22
    - 2.23606797749979 * m.b170 >= -2.23606797749979)
m.e23 = Constraint(expr= -sqrt((m.x129 - m.x134)**2 + (m.x130 - m.x135)**2 + (
    m.x131 - m.x136)**2 + (m.x132 - m.x137)**2 + (m.x133 - m.x138)**2) + m.x23
    - 2.23606797749979 * m.b171 >= -2.23606797749979)
m.e24 = Constraint(expr= -sqrt((m.x129 - m.x139)**2 + (m.x130 - m.x140)**2 + (
    m.x131 - m.x141)**2 + (m.x132 - m.x142)**2 + (m.x133 - m.x143)**2) + m.x24
    - 2.23606797749979 * m.b172 >= -2.23606797749979)
m.e25 = Constraint(expr= -sqrt((m.x129 - m.x144)**2 + (m.x130 - m.x145)**2 + (
    m.x131 - m.x146)**2 + (m.x132 - m.x147)**2 + (m.x133 - m.x148)**2) + m.x25
    - 2.23606797749979 * m.b173 >= -2.23606797749979)
m.e26 = Constraint(expr= -sqrt((m.x134 - m.x139)**2 + (m.x135 - m.x140)**2 + (
    m.x136 - m.x141)**2 + (m.x137 - m.x142)**2 + (m.x138 - m.x143)**2) + m.x26
    - 2.23606797749979 * m.b174 >= -2.23606797749979)
m.e27 = Constraint(expr= -sqrt((m.x134 - m.x144)**2 + (m.x135 - m.x145)**2 + (
    m.x136 - m.x146)**2 + (m.x137 - m.x147)**2 + (m.x138 - m.x148)**2) + m.x27
    - 2.23606797749979 * m.b175 >= -2.23606797749979)
m.e28 = Constraint(expr= -sqrt((m.x139 - m.x144)**2 + (m.x140 - m.x145)**2 + (
    m.x141 - m.x146)**2 + (m.x142 - m.x147)**2 + (m.x143 - m.x148)**2) + m.x28
    - 2.23606797749979 * m.b176 >= -2.23606797749979)
m.e29 = Constraint(expr= -sqrt((-0.4975365687586023 + m.x109)**2 + (
    -0.2661737230725406 + m.x110)**2 + (-0.6374111614436909 + m.x111)**2 + (
    -0.24247975418376266 + m.x112)**2 + (-0.4731685799874552 + m.x113)**2) +
    m.x29 - 2.23606797749979 * m.b177 >= -2.23606797749979)
m.e30 = Constraint(expr= -sqrt((-0.9703361491117534 + m.x109)**2 + (
    -0.08518806501099674 + m.x110)**2 + (-0.31737891751820513 + m.x111)**2 + (
    -0.6764439534894834 + m.x112)**2 + (-0.0852413172296076 + m.x113)**2) +
    m.x30 - 2.23606797749979 * m.b178 >= -2.23606797749979)
m.e31 = Constraint(expr= -sqrt((-0.15331752856953773 + m.x109)**2 + (
    -0.8252738498040315 + m.x110)**2 + (-0.9797228526139108 + m.x111)**2 + (
    -0.3193386437176482 + m.x112)**2 + (-0.18896898678495433 + m.x113)**2) +
    m.x31 - 2.23606797749979 * m.b179 >= -2.23606797749979)
m.e32 = Constraint(expr= -sqrt((-0.9723752503414661 + m.x109)**2 + (
    -0.3289191945502741 + m.x110)**2 + (-0.6037845231084645 + m.x111)**2 + (
    -0.6074942084317443 + m.x112)**2 + (-0.6349887556504961 + m.x113)**2) +
    m.x32 - 2.23606797749979 * m.b180 >= -2.23606797749979)
m.e33 = Constraint(expr= -sqrt((-0.9153921598736201 + m.x109)**2 + (
    -0.9624532167911902 + m.x110)**2 + (-0.6931477606588518 + m.x111)**2 + (
    -0.8249037141670215 + m.x112)**2 + (-0.7938285744978436 + m.x113)**2) +
    m.x33 - 2.23606797749979 * m.b181 >= -2.23606797749979)
m.e34 = Constraint(expr= -sqrt((-0.6431235882103946 + m.x109)**2 + (
    -0.43029214446042363 + m.x110)**2 + (-0.2272211040366383 + m.x111)**2 + (
    -0.26618017106327707 + m.x112)**2 + (-0.9300172137798001 + m.x113)**2) +
    m.x34 - 2.23606797749979 * m.b182 >= -2.23606797749979)
m.e35 = Constraint(expr= -sqrt((-0.7000659032477788 + m.x109)**2 + (
    -0.10579514653289779 + m.x110)**2 + (-0.9108122843705956 + m.x111)**2 + (
    -0.2710858352944323 + m.x112)**2 + (-0.6924618004350633 + m.x113)**2) +
    m.x35 - 2.23606797749979 * m.b183 >= -2.23606797749979)
m.e36 = Constraint(expr= -sqrt((-0.4599922159807449 + m.x109)**2 + (
    -0.26966362910775055 + m.x110)**2 + (-0.2092539856889395 + m.x111)**2 + (
    -0.5790755087347463 + m.x112)**2 + (-0.41176567735033565 + m.x113)**2) +
    m.x36 - 2.23606797749979 * m.b184 >= -2.23606797749979)
m.e37 = Constraint(expr= -sqrt((-0.624441898539622 + m.x109)**2 + (
    -0.6959821132167042 + m.x110)**2 + (-0.8194404253180085 + m.x111)**2 + (
    -0.8531850128548369 + m.x112)**2 + (-0.625463849213158 + m.x113)**2) +
    m.x37 - 2.23606797749979 * m.b185 >= -2.23606797749979)
m.e38 = Constraint(expr= -sqrt((-0.9664042707070908 + m.x109)**2 + (
    -0.4961049365022576 + m.x110)**2 + (-0.8875502088481517 + m.x111)**2 + (
    -0.8149762714789975 + m.x112)**2 + (-0.8175560360701905 + m.x113)**2) +
    m.x38 - 2.23606797749979 * m.b186 >= -2.23606797749979)
m.e39 = Constraint(expr= -sqrt((-0.4975365687586023 + m.x114)**2 + (
    -0.2661737230725406 + m.x115)**2 + (-0.6374111614436909 + m.x116)**2 + (
    -0.24247975418376266 + m.x117)**2 + (-0.4731685799874552 + m.x118)**2) +
    m.x39 - 2.23606797749979 * m.b187 >= -2.23606797749979)
m.e40 = Constraint(expr= -sqrt((-0.9703361491117534 + m.x114)**2 + (
    -0.08518806501099674 + m.x115)**2 + (-0.31737891751820513 + m.x116)**2 + (
    -0.6764439534894834 + m.x117)**2 + (-0.0852413172296076 + m.x118)**2) +
    m.x40 - 2.23606797749979 * m.b188 >= -2.23606797749979)
m.e41 = Constraint(expr= -sqrt((-0.15331752856953773 + m.x114)**2 + (
    -0.8252738498040315 + m.x115)**2 + (-0.9797228526139108 + m.x116)**2 + (
    -0.3193386437176482 + m.x117)**2 + (-0.18896898678495433 + m.x118)**2) +
    m.x41 - 2.23606797749979 * m.b189 >= -2.23606797749979)
m.e42 = Constraint(expr= -sqrt((-0.9723752503414661 + m.x114)**2 + (
    -0.3289191945502741 + m.x115)**2 + (-0.6037845231084645 + m.x116)**2 + (
    -0.6074942084317443 + m.x117)**2 + (-0.6349887556504961 + m.x118)**2) +
    m.x42 - 2.23606797749979 * m.b190 >= -2.23606797749979)
m.e43 = Constraint(expr= -sqrt((-0.9153921598736201 + m.x114)**2 + (
    -0.9624532167911902 + m.x115)**2 + (-0.6931477606588518 + m.x116)**2 + (
    -0.8249037141670215 + m.x117)**2 + (-0.7938285744978436 + m.x118)**2) +
    m.x43 - 2.23606797749979 * m.b191 >= -2.23606797749979)
m.e44 = Constraint(expr= -sqrt((-0.6431235882103946 + m.x114)**2 + (
    -0.43029214446042363 + m.x115)**2 + (-0.2272211040366383 + m.x116)**2 + (
    -0.26618017106327707 + m.x117)**2 + (-0.9300172137798001 + m.x118)**2) +
    m.x44 - 2.23606797749979 * m.b192 >= -2.23606797749979)
m.e45 = Constraint(expr= -sqrt((-0.7000659032477788 + m.x114)**2 + (
    -0.10579514653289779 + m.x115)**2 + (-0.9108122843705956 + m.x116)**2 + (
    -0.2710858352944323 + m.x117)**2 + (-0.6924618004350633 + m.x118)**2) +
    m.x45 - 2.23606797749979 * m.b193 >= -2.23606797749979)
m.e46 = Constraint(expr= -sqrt((-0.4599922159807449 + m.x114)**2 + (
    -0.26966362910775055 + m.x115)**2 + (-0.2092539856889395 + m.x116)**2 + (
    -0.5790755087347463 + m.x117)**2 + (-0.41176567735033565 + m.x118)**2) +
    m.x46 - 2.23606797749979 * m.b194 >= -2.23606797749979)
m.e47 = Constraint(expr= -sqrt((-0.624441898539622 + m.x114)**2 + (
    -0.6959821132167042 + m.x115)**2 + (-0.8194404253180085 + m.x116)**2 + (
    -0.8531850128548369 + m.x117)**2 + (-0.625463849213158 + m.x118)**2) +
    m.x47 - 2.23606797749979 * m.b195 >= -2.23606797749979)
m.e48 = Constraint(expr= -sqrt((-0.9664042707070908 + m.x114)**2 + (
    -0.4961049365022576 + m.x115)**2 + (-0.8875502088481517 + m.x116)**2 + (
    -0.8149762714789975 + m.x117)**2 + (-0.8175560360701905 + m.x118)**2) +
    m.x48 - 2.23606797749979 * m.b196 >= -2.23606797749979)
m.e49 = Constraint(expr= -sqrt((-0.4975365687586023 + m.x119)**2 + (
    -0.2661737230725406 + m.x120)**2 + (-0.6374111614436909 + m.x121)**2 + (
    -0.24247975418376266 + m.x122)**2 + (-0.4731685799874552 + m.x123)**2) +
    m.x49 - 2.23606797749979 * m.b197 >= -2.23606797749979)
m.e50 = Constraint(expr= -sqrt((-0.9703361491117534 + m.x119)**2 + (
    -0.08518806501099674 + m.x120)**2 + (-0.31737891751820513 + m.x121)**2 + (
    -0.6764439534894834 + m.x122)**2 + (-0.0852413172296076 + m.x123)**2) +
    m.x50 - 2.23606797749979 * m.b198 >= -2.23606797749979)
m.e51 = Constraint(expr= -sqrt((-0.15331752856953773 + m.x119)**2 + (
    -0.8252738498040315 + m.x120)**2 + (-0.9797228526139108 + m.x121)**2 + (
    -0.3193386437176482 + m.x122)**2 + (-0.18896898678495433 + m.x123)**2) +
    m.x51 - 2.23606797749979 * m.b199 >= -2.23606797749979)
m.e52 = Constraint(expr= -sqrt((-0.9723752503414661 + m.x119)**2 + (
    -0.3289191945502741 + m.x120)**2 + (-0.6037845231084645 + m.x121)**2 + (
    -0.6074942084317443 + m.x122)**2 + (-0.6349887556504961 + m.x123)**2) +
    m.x52 - 2.23606797749979 * m.b200 >= -2.23606797749979)
m.e53 = Constraint(expr= -sqrt((-0.9153921598736201 + m.x119)**2 + (
    -0.9624532167911902 + m.x120)**2 + (-0.6931477606588518 + m.x121)**2 + (
    -0.8249037141670215 + m.x122)**2 + (-0.7938285744978436 + m.x123)**2) +
    m.x53 - 2.23606797749979 * m.b201 >= -2.23606797749979)
m.e54 = Constraint(expr= -sqrt((-0.6431235882103946 + m.x119)**2 + (
    -0.43029214446042363 + m.x120)**2 + (-0.2272211040366383 + m.x121)**2 + (
    -0.26618017106327707 + m.x122)**2 + (-0.9300172137798001 + m.x123)**2) +
    m.x54 - 2.23606797749979 * m.b202 >= -2.23606797749979)
m.e55 = Constraint(expr= -sqrt((-0.7000659032477788 + m.x119)**2 + (
    -0.10579514653289779 + m.x120)**2 + (-0.9108122843705956 + m.x121)**2 + (
    -0.2710858352944323 + m.x122)**2 + (-0.6924618004350633 + m.x123)**2) +
    m.x55 - 2.23606797749979 * m.b203 >= -2.23606797749979)
m.e56 = Constraint(expr= -sqrt((-0.4599922159807449 + m.x119)**2 + (
    -0.26966362910775055 + m.x120)**2 + (-0.2092539856889395 + m.x121)**2 + (
    -0.5790755087347463 + m.x122)**2 + (-0.41176567735033565 + m.x123)**2) +
    m.x56 - 2.23606797749979 * m.b204 >= -2.23606797749979)
m.e57 = Constraint(expr= -sqrt((-0.624441898539622 + m.x119)**2 + (
    -0.6959821132167042 + m.x120)**2 + (-0.8194404253180085 + m.x121)**2 + (
    -0.8531850128548369 + m.x122)**2 + (-0.625463849213158 + m.x123)**2) +
    m.x57 - 2.23606797749979 * m.b205 >= -2.23606797749979)
m.e58 = Constraint(expr= -sqrt((-0.9664042707070908 + m.x119)**2 + (
    -0.4961049365022576 + m.x120)**2 + (-0.8875502088481517 + m.x121)**2 + (
    -0.8149762714789975 + m.x122)**2 + (-0.8175560360701905 + m.x123)**2) +
    m.x58 - 2.23606797749979 * m.b206 >= -2.23606797749979)
m.e59 = Constraint(expr= -sqrt((-0.4975365687586023 + m.x124)**2 + (
    -0.2661737230725406 + m.x125)**2 + (-0.6374111614436909 + m.x126)**2 + (
    -0.24247975418376266 + m.x127)**2 + (-0.4731685799874552 + m.x128)**2) +
    m.x59 - 2.23606797749979 * m.b207 >= -2.23606797749979)
m.e60 = Constraint(expr= -sqrt((-0.9703361491117534 + m.x124)**2 + (
    -0.08518806501099674 + m.x125)**2 + (-0.31737891751820513 + m.x126)**2 + (
    -0.6764439534894834 + m.x127)**2 + (-0.0852413172296076 + m.x128)**2) +
    m.x60 - 2.23606797749979 * m.b208 >= -2.23606797749979)
m.e61 = Constraint(expr= -sqrt((-0.15331752856953773 + m.x124)**2 + (
    -0.8252738498040315 + m.x125)**2 + (-0.9797228526139108 + m.x126)**2 + (
    -0.3193386437176482 + m.x127)**2 + (-0.18896898678495433 + m.x128)**2) +
    m.x61 - 2.23606797749979 * m.b209 >= -2.23606797749979)
m.e62 = Constraint(expr= -sqrt((-0.9723752503414661 + m.x124)**2 + (
    -0.3289191945502741 + m.x125)**2 + (-0.6037845231084645 + m.x126)**2 + (
    -0.6074942084317443 + m.x127)**2 + (-0.6349887556504961 + m.x128)**2) +
    m.x62 - 2.23606797749979 * m.b210 >= -2.23606797749979)
m.e63 = Constraint(expr= -sqrt((-0.9153921598736201 + m.x124)**2 + (
    -0.9624532167911902 + m.x125)**2 + (-0.6931477606588518 + m.x126)**2 + (
    -0.8249037141670215 + m.x127)**2 + (-0.7938285744978436 + m.x128)**2) +
    m.x63 - 2.23606797749979 * m.b211 >= -2.23606797749979)
m.e64 = Constraint(expr= -sqrt((-0.6431235882103946 + m.x124)**2 + (
    -0.43029214446042363 + m.x125)**2 + (-0.2272211040366383 + m.x126)**2 + (
    -0.26618017106327707 + m.x127)**2 + (-0.9300172137798001 + m.x128)**2) +
    m.x64 - 2.23606797749979 * m.b212 >= -2.23606797749979)
m.e65 = Constraint(expr= -sqrt((-0.7000659032477788 + m.x124)**2 + (
    -0.10579514653289779 + m.x125)**2 + (-0.9108122843705956 + m.x126)**2 + (
    -0.2710858352944323 + m.x127)**2 + (-0.6924618004350633 + m.x128)**2) +
    m.x65 - 2.23606797749979 * m.b213 >= -2.23606797749979)
m.e66 = Constraint(expr= -sqrt((-0.4599922159807449 + m.x124)**2 + (
    -0.26966362910775055 + m.x125)**2 + (-0.2092539856889395 + m.x126)**2 + (
    -0.5790755087347463 + m.x127)**2 + (-0.41176567735033565 + m.x128)**2) +
    m.x66 - 2.23606797749979 * m.b214 >= -2.23606797749979)
m.e67 = Constraint(expr= -sqrt((-0.624441898539622 + m.x124)**2 + (
    -0.6959821132167042 + m.x125)**2 + (-0.8194404253180085 + m.x126)**2 + (
    -0.8531850128548369 + m.x127)**2 + (-0.625463849213158 + m.x128)**2) +
    m.x67 - 2.23606797749979 * m.b215 >= -2.23606797749979)
m.e68 = Constraint(expr= -sqrt((-0.9664042707070908 + m.x124)**2 + (
    -0.4961049365022576 + m.x125)**2 + (-0.8875502088481517 + m.x126)**2 + (
    -0.8149762714789975 + m.x127)**2 + (-0.8175560360701905 + m.x128)**2) +
    m.x68 - 2.23606797749979 * m.b216 >= -2.23606797749979)
m.e69 = Constraint(expr= -sqrt((-0.4975365687586023 + m.x129)**2 + (
    -0.2661737230725406 + m.x130)**2 + (-0.6374111614436909 + m.x131)**2 + (
    -0.24247975418376266 + m.x132)**2 + (-0.4731685799874552 + m.x133)**2) +
    m.x69 - 2.23606797749979 * m.b217 >= -2.23606797749979)
m.e70 = Constraint(expr= -sqrt((-0.9703361491117534 + m.x129)**2 + (
    -0.08518806501099674 + m.x130)**2 + (-0.31737891751820513 + m.x131)**2 + (
    -0.6764439534894834 + m.x132)**2 + (-0.0852413172296076 + m.x133)**2) +
    m.x70 - 2.23606797749979 * m.b218 >= -2.23606797749979)
m.e71 = Constraint(expr= -sqrt((-0.15331752856953773 + m.x129)**2 + (
    -0.8252738498040315 + m.x130)**2 + (-0.9797228526139108 + m.x131)**2 + (
    -0.3193386437176482 + m.x132)**2 + (-0.18896898678495433 + m.x133)**2) +
    m.x71 - 2.23606797749979 * m.b219 >= -2.23606797749979)
m.e72 = Constraint(expr= -sqrt((-0.9723752503414661 + m.x129)**2 + (
    -0.3289191945502741 + m.x130)**2 + (-0.6037845231084645 + m.x131)**2 + (
    -0.6074942084317443 + m.x132)**2 + (-0.6349887556504961 + m.x133)**2) +
    m.x72 - 2.23606797749979 * m.b220 >= -2.23606797749979)
m.e73 = Constraint(expr= -sqrt((-0.9153921598736201 + m.x129)**2 + (
    -0.9624532167911902 + m.x130)**2 + (-0.6931477606588518 + m.x131)**2 + (
    -0.8249037141670215 + m.x132)**2 + (-0.7938285744978436 + m.x133)**2) +
    m.x73 - 2.23606797749979 * m.b221 >= -2.23606797749979)
m.e74 = Constraint(expr= -sqrt((-0.6431235882103946 + m.x129)**2 + (
    -0.43029214446042363 + m.x130)**2 + (-0.2272211040366383 + m.x131)**2 + (
    -0.26618017106327707 + m.x132)**2 + (-0.9300172137798001 + m.x133)**2) +
    m.x74 - 2.23606797749979 * m.b222 >= -2.23606797749979)
m.e75 = Constraint(expr= -sqrt((-0.7000659032477788 + m.x129)**2 + (
    -0.10579514653289779 + m.x130)**2 + (-0.9108122843705956 + m.x131)**2 + (
    -0.2710858352944323 + m.x132)**2 + (-0.6924618004350633 + m.x133)**2) +
    m.x75 - 2.23606797749979 * m.b223 >= -2.23606797749979)
m.e76 = Constraint(expr= -sqrt((-0.4599922159807449 + m.x129)**2 + (
    -0.26966362910775055 + m.x130)**2 + (-0.2092539856889395 + m.x131)**2 + (
    -0.5790755087347463 + m.x132)**2 + (-0.41176567735033565 + m.x133)**2) +
    m.x76 - 2.23606797749979 * m.b224 >= -2.23606797749979)
m.e77 = Constraint(expr= -sqrt((-0.624441898539622 + m.x129)**2 + (
    -0.6959821132167042 + m.x130)**2 + (-0.8194404253180085 + m.x131)**2 + (
    -0.8531850128548369 + m.x132)**2 + (-0.625463849213158 + m.x133)**2) +
    m.x77 - 2.23606797749979 * m.b225 >= -2.23606797749979)
m.e78 = Constraint(expr= -sqrt((-0.9664042707070908 + m.x129)**2 + (
    -0.4961049365022576 + m.x130)**2 + (-0.8875502088481517 + m.x131)**2 + (
    -0.8149762714789975 + m.x132)**2 + (-0.8175560360701905 + m.x133)**2) +
    m.x78 - 2.23606797749979 * m.b226 >= -2.23606797749979)
m.e79 = Constraint(expr= -sqrt((-0.4975365687586023 + m.x134)**2 + (
    -0.2661737230725406 + m.x135)**2 + (-0.6374111614436909 + m.x136)**2 + (
    -0.24247975418376266 + m.x137)**2 + (-0.4731685799874552 + m.x138)**2) +
    m.x79 - 2.23606797749979 * m.b227 >= -2.23606797749979)
m.e80 = Constraint(expr= -sqrt((-0.9703361491117534 + m.x134)**2 + (
    -0.08518806501099674 + m.x135)**2 + (-0.31737891751820513 + m.x136)**2 + (
    -0.6764439534894834 + m.x137)**2 + (-0.0852413172296076 + m.x138)**2) +
    m.x80 - 2.23606797749979 * m.b228 >= -2.23606797749979)
m.e81 = Constraint(expr= -sqrt((-0.15331752856953773 + m.x134)**2 + (
    -0.8252738498040315 + m.x135)**2 + (-0.9797228526139108 + m.x136)**2 + (
    -0.3193386437176482 + m.x137)**2 + (-0.18896898678495433 + m.x138)**2) +
    m.x81 - 2.23606797749979 * m.b229 >= -2.23606797749979)
m.e82 = Constraint(expr= -sqrt((-0.9723752503414661 + m.x134)**2 + (
    -0.3289191945502741 + m.x135)**2 + (-0.6037845231084645 + m.x136)**2 + (
    -0.6074942084317443 + m.x137)**2 + (-0.6349887556504961 + m.x138)**2) +
    m.x82 - 2.23606797749979 * m.b230 >= -2.23606797749979)
m.e83 = Constraint(expr= -sqrt((-0.9153921598736201 + m.x134)**2 + (
    -0.9624532167911902 + m.x135)**2 + (-0.6931477606588518 + m.x136)**2 + (
    -0.8249037141670215 + m.x137)**2 + (-0.7938285744978436 + m.x138)**2) +
    m.x83 - 2.23606797749979 * m.b231 >= -2.23606797749979)
m.e84 = Constraint(expr= -sqrt((-0.6431235882103946 + m.x134)**2 + (
    -0.43029214446042363 + m.x135)**2 + (-0.2272211040366383 + m.x136)**2 + (
    -0.26618017106327707 + m.x137)**2 + (-0.9300172137798001 + m.x138)**2) +
    m.x84 - 2.23606797749979 * m.b232 >= -2.23606797749979)
m.e85 = Constraint(expr= -sqrt((-0.7000659032477788 + m.x134)**2 + (
    -0.10579514653289779 + m.x135)**2 + (-0.9108122843705956 + m.x136)**2 + (
    -0.2710858352944323 + m.x137)**2 + (-0.6924618004350633 + m.x138)**2) +
    m.x85 - 2.23606797749979 * m.b233 >= -2.23606797749979)
m.e86 = Constraint(expr= -sqrt((-0.4599922159807449 + m.x134)**2 + (
    -0.26966362910775055 + m.x135)**2 + (-0.2092539856889395 + m.x136)**2 + (
    -0.5790755087347463 + m.x137)**2 + (-0.41176567735033565 + m.x138)**2) +
    m.x86 - 2.23606797749979 * m.b234 >= -2.23606797749979)
m.e87 = Constraint(expr= -sqrt((-0.624441898539622 + m.x134)**2 + (
    -0.6959821132167042 + m.x135)**2 + (-0.8194404253180085 + m.x136)**2 + (
    -0.8531850128548369 + m.x137)**2 + (-0.625463849213158 + m.x138)**2) +
    m.x87 - 2.23606797749979 * m.b235 >= -2.23606797749979)
m.e88 = Constraint(expr= -sqrt((-0.9664042707070908 + m.x134)**2 + (
    -0.4961049365022576 + m.x135)**2 + (-0.8875502088481517 + m.x136)**2 + (
    -0.8149762714789975 + m.x137)**2 + (-0.8175560360701905 + m.x138)**2) +
    m.x88 - 2.23606797749979 * m.b236 >= -2.23606797749979)
m.e89 = Constraint(expr= -sqrt((-0.4975365687586023 + m.x139)**2 + (
    -0.2661737230725406 + m.x140)**2 + (-0.6374111614436909 + m.x141)**2 + (
    -0.24247975418376266 + m.x142)**2 + (-0.4731685799874552 + m.x143)**2) +
    m.x89 - 2.23606797749979 * m.b237 >= -2.23606797749979)
m.e90 = Constraint(expr= -sqrt((-0.9703361491117534 + m.x139)**2 + (
    -0.08518806501099674 + m.x140)**2 + (-0.31737891751820513 + m.x141)**2 + (
    -0.6764439534894834 + m.x142)**2 + (-0.0852413172296076 + m.x143)**2) +
    m.x90 - 2.23606797749979 * m.b238 >= -2.23606797749979)
m.e91 = Constraint(expr= -sqrt((-0.15331752856953773 + m.x139)**2 + (
    -0.8252738498040315 + m.x140)**2 + (-0.9797228526139108 + m.x141)**2 + (
    -0.3193386437176482 + m.x142)**2 + (-0.18896898678495433 + m.x143)**2) +
    m.x91 - 2.23606797749979 * m.b239 >= -2.23606797749979)
m.e92 = Constraint(expr= -sqrt((-0.9723752503414661 + m.x139)**2 + (
    -0.3289191945502741 + m.x140)**2 + (-0.6037845231084645 + m.x141)**2 + (
    -0.6074942084317443 + m.x142)**2 + (-0.6349887556504961 + m.x143)**2) +
    m.x92 - 2.23606797749979 * m.b240 >= -2.23606797749979)
m.e93 = Constraint(expr= -sqrt((-0.9153921598736201 + m.x139)**2 + (
    -0.9624532167911902 + m.x140)**2 + (-0.6931477606588518 + m.x141)**2 + (
    -0.8249037141670215 + m.x142)**2 + (-0.7938285744978436 + m.x143)**2) +
    m.x93 - 2.23606797749979 * m.b241 >= -2.23606797749979)
m.e94 = Constraint(expr= -sqrt((-0.6431235882103946 + m.x139)**2 + (
    -0.43029214446042363 + m.x140)**2 + (-0.2272211040366383 + m.x141)**2 + (
    -0.26618017106327707 + m.x142)**2 + (-0.9300172137798001 + m.x143)**2) +
    m.x94 - 2.23606797749979 * m.b242 >= -2.23606797749979)
m.e95 = Constraint(expr= -sqrt((-0.7000659032477788 + m.x139)**2 + (
    -0.10579514653289779 + m.x140)**2 + (-0.9108122843705956 + m.x141)**2 + (
    -0.2710858352944323 + m.x142)**2 + (-0.6924618004350633 + m.x143)**2) +
    m.x95 - 2.23606797749979 * m.b243 >= -2.23606797749979)
m.e96 = Constraint(expr= -sqrt((-0.4599922159807449 + m.x139)**2 + (
    -0.26966362910775055 + m.x140)**2 + (-0.2092539856889395 + m.x141)**2 + (
    -0.5790755087347463 + m.x142)**2 + (-0.41176567735033565 + m.x143)**2) +
    m.x96 - 2.23606797749979 * m.b244 >= -2.23606797749979)
m.e97 = Constraint(expr= -sqrt((-0.624441898539622 + m.x139)**2 + (
    -0.6959821132167042 + m.x140)**2 + (-0.8194404253180085 + m.x141)**2 + (
    -0.8531850128548369 + m.x142)**2 + (-0.625463849213158 + m.x143)**2) +
    m.x97 - 2.23606797749979 * m.b245 >= -2.23606797749979)
m.e98 = Constraint(expr= -sqrt((-0.9664042707070908 + m.x139)**2 + (
    -0.4961049365022576 + m.x140)**2 + (-0.8875502088481517 + m.x141)**2 + (
    -0.8149762714789975 + m.x142)**2 + (-0.8175560360701905 + m.x143)**2) +
    m.x98 - 2.23606797749979 * m.b246 >= -2.23606797749979)
m.e99 = Constraint(expr= -sqrt((-0.4975365687586023 + m.x144)**2 + (
    -0.2661737230725406 + m.x145)**2 + (-0.6374111614436909 + m.x146)**2 + (
    -0.24247975418376266 + m.x147)**2 + (-0.4731685799874552 + m.x148)**2) +
    m.x99 - 2.23606797749979 * m.b247 >= -2.23606797749979)
m.e100 = Constraint(expr= -sqrt((-0.9703361491117534 + m.x144)**2 + (
    -0.08518806501099674 + m.x145)**2 + (-0.31737891751820513 + m.x146)**2 + (
    -0.6764439534894834 + m.x147)**2 + (-0.0852413172296076 + m.x148)**2) +
    m.x100 - 2.23606797749979 * m.b248 >= -2.23606797749979)
m.e101 = Constraint(expr= -sqrt((-0.15331752856953773 + m.x144)**2 + (
    -0.8252738498040315 + m.x145)**2 + (-0.9797228526139108 + m.x146)**2 + (
    -0.3193386437176482 + m.x147)**2 + (-0.18896898678495433 + m.x148)**2) +
    m.x101 - 2.23606797749979 * m.b249 >= -2.23606797749979)
m.e102 = Constraint(expr= -sqrt((-0.9723752503414661 + m.x144)**2 + (
    -0.3289191945502741 + m.x145)**2 + (-0.6037845231084645 + m.x146)**2 + (
    -0.6074942084317443 + m.x147)**2 + (-0.6349887556504961 + m.x148)**2) +
    m.x102 - 2.23606797749979 * m.b250 >= -2.23606797749979)
m.e103 = Constraint(expr= -sqrt((-0.9153921598736201 + m.x144)**2 + (
    -0.9624532167911902 + m.x145)**2 + (-0.6931477606588518 + m.x146)**2 + (
    -0.8249037141670215 + m.x147)**2 + (-0.7938285744978436 + m.x148)**2) +
    m.x103 - 2.23606797749979 * m.b251 >= -2.23606797749979)
m.e104 = Constraint(expr= -sqrt((-0.6431235882103946 + m.x144)**2 + (
    -0.43029214446042363 + m.x145)**2 + (-0.2272211040366383 + m.x146)**2 + (
    -0.26618017106327707 + m.x147)**2 + (-0.9300172137798001 + m.x148)**2) +
    m.x104 - 2.23606797749979 * m.b252 >= -2.23606797749979)
m.e105 = Constraint(expr= -sqrt((-0.7000659032477788 + m.x144)**2 + (
    -0.10579514653289779 + m.x145)**2 + (-0.9108122843705956 + m.x146)**2 + (
    -0.2710858352944323 + m.x147)**2 + (-0.6924618004350633 + m.x148)**2) +
    m.x105 - 2.23606797749979 * m.b253 >= -2.23606797749979)
m.e106 = Constraint(expr= -sqrt((-0.4599922159807449 + m.x144)**2 + (
    -0.26966362910775055 + m.x145)**2 + (-0.2092539856889395 + m.x146)**2 + (
    -0.5790755087347463 + m.x147)**2 + (-0.41176567735033565 + m.x148)**2) +
    m.x106 - 2.23606797749979 * m.b254 >= -2.23606797749979)
m.e107 = Constraint(expr= -sqrt((-0.624441898539622 + m.x144)**2 + (
    -0.6959821132167042 + m.x145)**2 + (-0.8194404253180085 + m.x146)**2 + (
    -0.8531850128548369 + m.x147)**2 + (-0.625463849213158 + m.x148)**2) +
    m.x107 - 2.23606797749979 * m.b255 >= -2.23606797749979)
m.e108 = Constraint(expr= -sqrt((-0.9664042707070908 + m.x144)**2 + (
    -0.4961049365022576 + m.x145)**2 + (-0.8875502088481517 + m.x146)**2 + (
    -0.8149762714789975 + m.x147)**2 + (-0.8175560360701905 + m.x148)**2) +
    m.x108 - 2.23606797749979 * m.b256 >= -2.23606797749979)
m.e109 = Constraint(expr= m.b177 + m.b187 + m.b197 + m.b207 + m.b217 + m.b227
    + m.b237 + m.b247 == 1)
m.e110 = Constraint(expr= m.b178 + m.b188 + m.b198 + m.b208 + m.b218 + m.b228
    + m.b238 + m.b248 == 1)
m.e111 = Constraint(expr= m.b179 + m.b189 + m.b199 + m.b209 + m.b219 + m.b229
    + m.b239 + m.b249 == 1)
m.e112 = Constraint(expr= m.b180 + m.b190 + m.b200 + m.b210 + m.b220 + m.b230
    + m.b240 + m.b250 == 1)
m.e113 = Constraint(expr= m.b181 + m.b191 + m.b201 + m.b211 + m.b221 + m.b231
    + m.b241 + m.b251 == 1)
m.e114 = Constraint(expr= m.b182 + m.b192 + m.b202 + m.b212 + m.b222 + m.b232
    + m.b242 + m.b252 == 1)
m.e115 = Constraint(expr= m.b183 + m.b193 + m.b203 + m.b213 + m.b223 + m.b233
    + m.b243 + m.b253 == 1)
m.e116 = Constraint(expr= m.b184 + m.b194 + m.b204 + m.b214 + m.b224 + m.b234
    + m.b244 + m.b254 == 1)
m.e117 = Constraint(expr= m.b185 + m.b195 + m.b205 + m.b215 + m.b225 + m.b235
    + m.b245 + m.b255 == 1)
m.e118 = Constraint(expr= m.b186 + m.b196 + m.b206 + m.b216 + m.b226 + m.b236
    + m.b246 + m.b256 == 1)
m.e119 = Constraint(expr= m.b149 + m.b150 + m.b151 + m.b152 + m.b153 + m.b154
    + m.b155 + m.b177 + m.b178 + m.b179 + m.b180 + m.b181 + m.b182 + m.b183 +
    m.b184 + m.b185 + m.b186 == 3)
m.e120 = Constraint(expr= m.b149 + m.b156 + m.b157 + m.b158 + m.b159 + m.b160
    + m.b161 + m.b187 + m.b188 + m.b189 + m.b190 + m.b191 + m.b192 + m.b193 +
    m.b194 + m.b195 + m.b196 == 3)
m.e121 = Constraint(expr= m.b150 + m.b156 + m.b162 + m.b163 + m.b164 + m.b165
    + m.b166 + m.b197 + m.b198 + m.b199 + m.b200 + m.b201 + m.b202 + m.b203 +
    m.b204 + m.b205 + m.b206 == 3)
m.e122 = Constraint(expr= m.b151 + m.b157 + m.b162 + m.b167 + m.b168 + m.b169
    + m.b170 + m.b207 + m.b208 + m.b209 + m.b210 + m.b211 + m.b212 + m.b213 +
    m.b214 + m.b215 + m.b216 == 3)
m.e123 = Constraint(expr= m.b152 + m.b158 + m.b163 + m.b167 + m.b171 + m.b172
    + m.b173 + m.b217 + m.b218 + m.b219 + m.b220 + m.b221 + m.b222 + m.b223 +
    m.b224 + m.b225 + m.b226 == 3)
m.e124 = Constraint(expr= m.b153 + m.b159 + m.b164 + m.b168 + m.b171 + m.b174
    + m.b175 + m.b227 + m.b228 + m.b229 + m.b230 + m.b231 + m.b232 + m.b233 +
    m.b234 + m.b235 + m.b236 == 3)
m.e125 = Constraint(expr= m.b154 + m.b160 + m.b165 + m.b169 + m.b172 + m.b174
    + m.b176 + m.b237 + m.b238 + m.b239 + m.b240 + m.b241 + m.b242 + m.b243 +
    m.b244 + m.b245 + m.b246 == 3)
m.e126 = Constraint(expr= m.b155 + m.b161 + m.b166 + m.b170 + m.b173 + m.b175
    + m.b176 + m.b247 + m.b248 + m.b249 + m.b250 + m.b251 + m.b252 + m.b253 +
    m.b254 + m.b255 + m.b256 == 3)
m.e127 = Constraint(expr= m.b149 == 1)
m.e128 = Constraint(expr= m.b150 + m.b156 == 1)
m.e129 = Constraint(expr= m.b151 + m.b157 + m.b162 == 1)
m.e130 = Constraint(expr= m.b152 + m.b158 + m.b163 + m.b167 == 1)
m.e131 = Constraint(expr= m.b153 + m.b159 + m.b164 + m.b168 + m.b171 == 1)
m.e132 = Constraint(expr= m.b154 + m.b160 + m.b165 + m.b169 + m.b172 + m.b174
    == 1)
m.e133 = Constraint(expr= m.b155 + m.b161 + m.b166 + m.b170 + m.b173 + m.b175
    + m.b176 == 1)
