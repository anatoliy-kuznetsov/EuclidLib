# MINLP written by GAMS Convert at 05/15/24 11:59:48
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       133       25      108        0        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#       240      132      108        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       868      460      408
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
m.b133 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b134 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b135 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b136 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b137 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b138 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b139 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b140 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b141 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b142 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b143 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b144 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b145 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b146 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b147 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b148 = Var(within=Binary, bounds=(0,1), initialize=0)
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

m.e1 = Constraint(expr= -sqrt((m.x109 - m.x112)**2 + (m.x110 - m.x113)**2 + (
    m.x111 - m.x114)**2) + m.x1 - 1.7320508075688772 * m.b133
    >= -1.7320508075688772)
m.e2 = Constraint(expr= -sqrt((m.x109 - m.x115)**2 + (m.x110 - m.x116)**2 + (
    m.x111 - m.x117)**2) + m.x2 - 1.7320508075688772 * m.b134
    >= -1.7320508075688772)
m.e3 = Constraint(expr= -sqrt((m.x109 - m.x118)**2 + (m.x110 - m.x119)**2 + (
    m.x111 - m.x120)**2) + m.x3 - 1.7320508075688772 * m.b135
    >= -1.7320508075688772)
m.e4 = Constraint(expr= -sqrt((m.x109 - m.x121)**2 + (m.x110 - m.x122)**2 + (
    m.x111 - m.x123)**2) + m.x4 - 1.7320508075688772 * m.b136
    >= -1.7320508075688772)
m.e5 = Constraint(expr= -sqrt((m.x109 - m.x124)**2 + (m.x110 - m.x125)**2 + (
    m.x111 - m.x126)**2) + m.x5 - 1.7320508075688772 * m.b137
    >= -1.7320508075688772)
m.e6 = Constraint(expr= -sqrt((m.x109 - m.x127)**2 + (m.x110 - m.x128)**2 + (
    m.x111 - m.x129)**2) + m.x6 - 1.7320508075688772 * m.b138
    >= -1.7320508075688772)
m.e7 = Constraint(expr= -sqrt((m.x109 - m.x130)**2 + (m.x110 - m.x131)**2 + (
    m.x111 - m.x132)**2) + m.x7 - 1.7320508075688772 * m.b139
    >= -1.7320508075688772)
m.e8 = Constraint(expr= -sqrt((m.x112 - m.x115)**2 + (m.x113 - m.x116)**2 + (
    m.x114 - m.x117)**2) + m.x8 - 1.7320508075688772 * m.b140
    >= -1.7320508075688772)
m.e9 = Constraint(expr= -sqrt((m.x112 - m.x118)**2 + (m.x113 - m.x119)**2 + (
    m.x114 - m.x120)**2) + m.x9 - 1.7320508075688772 * m.b141
    >= -1.7320508075688772)
m.e10 = Constraint(expr= -sqrt((m.x112 - m.x121)**2 + (m.x113 - m.x122)**2 + (
    m.x114 - m.x123)**2) + m.x10 - 1.7320508075688772 * m.b142
    >= -1.7320508075688772)
m.e11 = Constraint(expr= -sqrt((m.x112 - m.x124)**2 + (m.x113 - m.x125)**2 + (
    m.x114 - m.x126)**2) + m.x11 - 1.7320508075688772 * m.b143
    >= -1.7320508075688772)
m.e12 = Constraint(expr= -sqrt((m.x112 - m.x127)**2 + (m.x113 - m.x128)**2 + (
    m.x114 - m.x129)**2) + m.x12 - 1.7320508075688772 * m.b144
    >= -1.7320508075688772)
m.e13 = Constraint(expr= -sqrt((m.x112 - m.x130)**2 + (m.x113 - m.x131)**2 + (
    m.x114 - m.x132)**2) + m.x13 - 1.7320508075688772 * m.b145
    >= -1.7320508075688772)
m.e14 = Constraint(expr= -sqrt((m.x115 - m.x118)**2 + (m.x116 - m.x119)**2 + (
    m.x117 - m.x120)**2) + m.x14 - 1.7320508075688772 * m.b146
    >= -1.7320508075688772)
m.e15 = Constraint(expr= -sqrt((m.x115 - m.x121)**2 + (m.x116 - m.x122)**2 + (
    m.x117 - m.x123)**2) + m.x15 - 1.7320508075688772 * m.b147
    >= -1.7320508075688772)
m.e16 = Constraint(expr= -sqrt((m.x115 - m.x124)**2 + (m.x116 - m.x125)**2 + (
    m.x117 - m.x126)**2) + m.x16 - 1.7320508075688772 * m.b148
    >= -1.7320508075688772)
m.e17 = Constraint(expr= -sqrt((m.x115 - m.x127)**2 + (m.x116 - m.x128)**2 + (
    m.x117 - m.x129)**2) + m.x17 - 1.7320508075688772 * m.b149
    >= -1.7320508075688772)
m.e18 = Constraint(expr= -sqrt((m.x115 - m.x130)**2 + (m.x116 - m.x131)**2 + (
    m.x117 - m.x132)**2) + m.x18 - 1.7320508075688772 * m.b150
    >= -1.7320508075688772)
m.e19 = Constraint(expr= -sqrt((m.x118 - m.x121)**2 + (m.x119 - m.x122)**2 + (
    m.x120 - m.x123)**2) + m.x19 - 1.7320508075688772 * m.b151
    >= -1.7320508075688772)
m.e20 = Constraint(expr= -sqrt((m.x118 - m.x124)**2 + (m.x119 - m.x125)**2 + (
    m.x120 - m.x126)**2) + m.x20 - 1.7320508075688772 * m.b152
    >= -1.7320508075688772)
m.e21 = Constraint(expr= -sqrt((m.x118 - m.x127)**2 + (m.x119 - m.x128)**2 + (
    m.x120 - m.x129)**2) + m.x21 - 1.7320508075688772 * m.b153
    >= -1.7320508075688772)
m.e22 = Constraint(expr= -sqrt((m.x118 - m.x130)**2 + (m.x119 - m.x131)**2 + (
    m.x120 - m.x132)**2) + m.x22 - 1.7320508075688772 * m.b154
    >= -1.7320508075688772)
m.e23 = Constraint(expr= -sqrt((m.x121 - m.x124)**2 + (m.x122 - m.x125)**2 + (
    m.x123 - m.x126)**2) + m.x23 - 1.7320508075688772 * m.b155
    >= -1.7320508075688772)
m.e24 = Constraint(expr= -sqrt((m.x121 - m.x127)**2 + (m.x122 - m.x128)**2 + (
    m.x123 - m.x129)**2) + m.x24 - 1.7320508075688772 * m.b156
    >= -1.7320508075688772)
m.e25 = Constraint(expr= -sqrt((m.x121 - m.x130)**2 + (m.x122 - m.x131)**2 + (
    m.x123 - m.x132)**2) + m.x25 - 1.7320508075688772 * m.b157
    >= -1.7320508075688772)
m.e26 = Constraint(expr= -sqrt((m.x124 - m.x127)**2 + (m.x125 - m.x128)**2 + (
    m.x126 - m.x129)**2) + m.x26 - 1.7320508075688772 * m.b158
    >= -1.7320508075688772)
m.e27 = Constraint(expr= -sqrt((m.x124 - m.x130)**2 + (m.x125 - m.x131)**2 + (
    m.x126 - m.x132)**2) + m.x27 - 1.7320508075688772 * m.b159
    >= -1.7320508075688772)
m.e28 = Constraint(expr= -sqrt((m.x127 - m.x130)**2 + (m.x128 - m.x131)**2 + (
    m.x129 - m.x132)**2) + m.x28 - 1.7320508075688772 * m.b160
    >= -1.7320508075688772)
m.e29 = Constraint(expr= -sqrt((-0.5390815646058106 + m.x109)**2 + (
    -0.2891964436397205 + m.x110)**2 + (-0.03003690855112706 + m.x111)**2) +
    m.x29 - 1.7320508075688772 * m.b161 >= -1.7320508075688772)
m.e30 = Constraint(expr= -sqrt((-0.6536357538927619 + m.x109)**2 + (
    -0.21000869554973112 + m.x110)**2 + (-0.2572769749796092 + m.x111)**2) +
    m.x30 - 1.7320508075688772 * m.b162 >= -1.7320508075688772)
m.e31 = Constraint(expr= -sqrt((-0.39719826263322744 + m.x109)**2 + (
    -0.6415781537746728 + m.x110)**2 + (-0.9888112104037214 + m.x111)**2) +
    m.x31 - 1.7320508075688772 * m.b163 >= -1.7320508075688772)
m.e32 = Constraint(expr= -sqrt((-0.46153301006262504 + m.x109)**2 + (
    -0.9934850076016687 + m.x110)**2 + (-0.9925719941586278 + m.x111)**2) +
    m.x32 - 1.7320508075688772 * m.b164 >= -1.7320508075688772)
m.e33 = Constraint(expr= -sqrt((-0.24267553557344324 + m.x109)**2 + (
    -0.07264511287134134 + m.x110)**2 + (-0.159901022229618 + m.x111)**2) +
    m.x33 - 1.7320508075688772 * m.b165 >= -1.7320508075688772)
m.e34 = Constraint(expr= -sqrt((-0.8419027314789557 + m.x109)**2 + (
    -0.5995547289462685 + m.x110)**2 + (-0.9174626648558603 + m.x111)**2) +
    m.x34 - 1.7320508075688772 * m.b166 >= -1.7320508075688772)
m.e35 = Constraint(expr= -sqrt((-0.9721691074362717 + m.x109)**2 + (
    -0.6544238205879963 + m.x110)**2 + (-0.535204782203361 + m.x111)**2) +
    m.x35 - 1.7320508075688772 * m.b167 >= -1.7320508075688772)
m.e36 = Constraint(expr= -sqrt((-0.06763103158333483 + m.x109)**2 + (
    -0.023510063056781383 + m.x110)**2 + (-0.8052942869277137 + m.x111)**2) +
    m.x36 - 1.7320508075688772 * m.b168 >= -1.7320508075688772)
m.e37 = Constraint(expr= -sqrt((-0.6719697138652216 + m.x109)**2 + (
    -0.7630117418529349 + m.x110)**2 + (-0.5656524680218609 + m.x111)**2) +
    m.x37 - 1.7320508075688772 * m.b169 >= -1.7320508075688772)
m.e38 = Constraint(expr= -sqrt((-0.6738937592389419 + m.x109)**2 + (
    -0.6387228188088844 + m.x110)**2 + (-0.8951756504920998 + m.x111)**2) +
    m.x38 - 1.7320508075688772 * m.b170 >= -1.7320508075688772)
m.e39 = Constraint(expr= -sqrt((-0.5390815646058106 + m.x112)**2 + (
    -0.2891964436397205 + m.x113)**2 + (-0.03003690855112706 + m.x114)**2) +
    m.x39 - 1.7320508075688772 * m.b171 >= -1.7320508075688772)
m.e40 = Constraint(expr= -sqrt((-0.6536357538927619 + m.x112)**2 + (
    -0.21000869554973112 + m.x113)**2 + (-0.2572769749796092 + m.x114)**2) +
    m.x40 - 1.7320508075688772 * m.b172 >= -1.7320508075688772)
m.e41 = Constraint(expr= -sqrt((-0.39719826263322744 + m.x112)**2 + (
    -0.6415781537746728 + m.x113)**2 + (-0.9888112104037214 + m.x114)**2) +
    m.x41 - 1.7320508075688772 * m.b173 >= -1.7320508075688772)
m.e42 = Constraint(expr= -sqrt((-0.46153301006262504 + m.x112)**2 + (
    -0.9934850076016687 + m.x113)**2 + (-0.9925719941586278 + m.x114)**2) +
    m.x42 - 1.7320508075688772 * m.b174 >= -1.7320508075688772)
m.e43 = Constraint(expr= -sqrt((-0.24267553557344324 + m.x112)**2 + (
    -0.07264511287134134 + m.x113)**2 + (-0.159901022229618 + m.x114)**2) +
    m.x43 - 1.7320508075688772 * m.b175 >= -1.7320508075688772)
m.e44 = Constraint(expr= -sqrt((-0.8419027314789557 + m.x112)**2 + (
    -0.5995547289462685 + m.x113)**2 + (-0.9174626648558603 + m.x114)**2) +
    m.x44 - 1.7320508075688772 * m.b176 >= -1.7320508075688772)
m.e45 = Constraint(expr= -sqrt((-0.9721691074362717 + m.x112)**2 + (
    -0.6544238205879963 + m.x113)**2 + (-0.535204782203361 + m.x114)**2) +
    m.x45 - 1.7320508075688772 * m.b177 >= -1.7320508075688772)
m.e46 = Constraint(expr= -sqrt((-0.06763103158333483 + m.x112)**2 + (
    -0.023510063056781383 + m.x113)**2 + (-0.8052942869277137 + m.x114)**2) +
    m.x46 - 1.7320508075688772 * m.b178 >= -1.7320508075688772)
m.e47 = Constraint(expr= -sqrt((-0.6719697138652216 + m.x112)**2 + (
    -0.7630117418529349 + m.x113)**2 + (-0.5656524680218609 + m.x114)**2) +
    m.x47 - 1.7320508075688772 * m.b179 >= -1.7320508075688772)
m.e48 = Constraint(expr= -sqrt((-0.6738937592389419 + m.x112)**2 + (
    -0.6387228188088844 + m.x113)**2 + (-0.8951756504920998 + m.x114)**2) +
    m.x48 - 1.7320508075688772 * m.b180 >= -1.7320508075688772)
m.e49 = Constraint(expr= -sqrt((-0.5390815646058106 + m.x115)**2 + (
    -0.2891964436397205 + m.x116)**2 + (-0.03003690855112706 + m.x117)**2) +
    m.x49 - 1.7320508075688772 * m.b181 >= -1.7320508075688772)
m.e50 = Constraint(expr= -sqrt((-0.6536357538927619 + m.x115)**2 + (
    -0.21000869554973112 + m.x116)**2 + (-0.2572769749796092 + m.x117)**2) +
    m.x50 - 1.7320508075688772 * m.b182 >= -1.7320508075688772)
m.e51 = Constraint(expr= -sqrt((-0.39719826263322744 + m.x115)**2 + (
    -0.6415781537746728 + m.x116)**2 + (-0.9888112104037214 + m.x117)**2) +
    m.x51 - 1.7320508075688772 * m.b183 >= -1.7320508075688772)
m.e52 = Constraint(expr= -sqrt((-0.46153301006262504 + m.x115)**2 + (
    -0.9934850076016687 + m.x116)**2 + (-0.9925719941586278 + m.x117)**2) +
    m.x52 - 1.7320508075688772 * m.b184 >= -1.7320508075688772)
m.e53 = Constraint(expr= -sqrt((-0.24267553557344324 + m.x115)**2 + (
    -0.07264511287134134 + m.x116)**2 + (-0.159901022229618 + m.x117)**2) +
    m.x53 - 1.7320508075688772 * m.b185 >= -1.7320508075688772)
m.e54 = Constraint(expr= -sqrt((-0.8419027314789557 + m.x115)**2 + (
    -0.5995547289462685 + m.x116)**2 + (-0.9174626648558603 + m.x117)**2) +
    m.x54 - 1.7320508075688772 * m.b186 >= -1.7320508075688772)
m.e55 = Constraint(expr= -sqrt((-0.9721691074362717 + m.x115)**2 + (
    -0.6544238205879963 + m.x116)**2 + (-0.535204782203361 + m.x117)**2) +
    m.x55 - 1.7320508075688772 * m.b187 >= -1.7320508075688772)
m.e56 = Constraint(expr= -sqrt((-0.06763103158333483 + m.x115)**2 + (
    -0.023510063056781383 + m.x116)**2 + (-0.8052942869277137 + m.x117)**2) +
    m.x56 - 1.7320508075688772 * m.b188 >= -1.7320508075688772)
m.e57 = Constraint(expr= -sqrt((-0.6719697138652216 + m.x115)**2 + (
    -0.7630117418529349 + m.x116)**2 + (-0.5656524680218609 + m.x117)**2) +
    m.x57 - 1.7320508075688772 * m.b189 >= -1.7320508075688772)
m.e58 = Constraint(expr= -sqrt((-0.6738937592389419 + m.x115)**2 + (
    -0.6387228188088844 + m.x116)**2 + (-0.8951756504920998 + m.x117)**2) +
    m.x58 - 1.7320508075688772 * m.b190 >= -1.7320508075688772)
m.e59 = Constraint(expr= -sqrt((-0.5390815646058106 + m.x118)**2 + (
    -0.2891964436397205 + m.x119)**2 + (-0.03003690855112706 + m.x120)**2) +
    m.x59 - 1.7320508075688772 * m.b191 >= -1.7320508075688772)
m.e60 = Constraint(expr= -sqrt((-0.6536357538927619 + m.x118)**2 + (
    -0.21000869554973112 + m.x119)**2 + (-0.2572769749796092 + m.x120)**2) +
    m.x60 - 1.7320508075688772 * m.b192 >= -1.7320508075688772)
m.e61 = Constraint(expr= -sqrt((-0.39719826263322744 + m.x118)**2 + (
    -0.6415781537746728 + m.x119)**2 + (-0.9888112104037214 + m.x120)**2) +
    m.x61 - 1.7320508075688772 * m.b193 >= -1.7320508075688772)
m.e62 = Constraint(expr= -sqrt((-0.46153301006262504 + m.x118)**2 + (
    -0.9934850076016687 + m.x119)**2 + (-0.9925719941586278 + m.x120)**2) +
    m.x62 - 1.7320508075688772 * m.b194 >= -1.7320508075688772)
m.e63 = Constraint(expr= -sqrt((-0.24267553557344324 + m.x118)**2 + (
    -0.07264511287134134 + m.x119)**2 + (-0.159901022229618 + m.x120)**2) +
    m.x63 - 1.7320508075688772 * m.b195 >= -1.7320508075688772)
m.e64 = Constraint(expr= -sqrt((-0.8419027314789557 + m.x118)**2 + (
    -0.5995547289462685 + m.x119)**2 + (-0.9174626648558603 + m.x120)**2) +
    m.x64 - 1.7320508075688772 * m.b196 >= -1.7320508075688772)
m.e65 = Constraint(expr= -sqrt((-0.9721691074362717 + m.x118)**2 + (
    -0.6544238205879963 + m.x119)**2 + (-0.535204782203361 + m.x120)**2) +
    m.x65 - 1.7320508075688772 * m.b197 >= -1.7320508075688772)
m.e66 = Constraint(expr= -sqrt((-0.06763103158333483 + m.x118)**2 + (
    -0.023510063056781383 + m.x119)**2 + (-0.8052942869277137 + m.x120)**2) +
    m.x66 - 1.7320508075688772 * m.b198 >= -1.7320508075688772)
m.e67 = Constraint(expr= -sqrt((-0.6719697138652216 + m.x118)**2 + (
    -0.7630117418529349 + m.x119)**2 + (-0.5656524680218609 + m.x120)**2) +
    m.x67 - 1.7320508075688772 * m.b199 >= -1.7320508075688772)
m.e68 = Constraint(expr= -sqrt((-0.6738937592389419 + m.x118)**2 + (
    -0.6387228188088844 + m.x119)**2 + (-0.8951756504920998 + m.x120)**2) +
    m.x68 - 1.7320508075688772 * m.b200 >= -1.7320508075688772)
m.e69 = Constraint(expr= -sqrt((-0.5390815646058106 + m.x121)**2 + (
    -0.2891964436397205 + m.x122)**2 + (-0.03003690855112706 + m.x123)**2) +
    m.x69 - 1.7320508075688772 * m.b201 >= -1.7320508075688772)
m.e70 = Constraint(expr= -sqrt((-0.6536357538927619 + m.x121)**2 + (
    -0.21000869554973112 + m.x122)**2 + (-0.2572769749796092 + m.x123)**2) +
    m.x70 - 1.7320508075688772 * m.b202 >= -1.7320508075688772)
m.e71 = Constraint(expr= -sqrt((-0.39719826263322744 + m.x121)**2 + (
    -0.6415781537746728 + m.x122)**2 + (-0.9888112104037214 + m.x123)**2) +
    m.x71 - 1.7320508075688772 * m.b203 >= -1.7320508075688772)
m.e72 = Constraint(expr= -sqrt((-0.46153301006262504 + m.x121)**2 + (
    -0.9934850076016687 + m.x122)**2 + (-0.9925719941586278 + m.x123)**2) +
    m.x72 - 1.7320508075688772 * m.b204 >= -1.7320508075688772)
m.e73 = Constraint(expr= -sqrt((-0.24267553557344324 + m.x121)**2 + (
    -0.07264511287134134 + m.x122)**2 + (-0.159901022229618 + m.x123)**2) +
    m.x73 - 1.7320508075688772 * m.b205 >= -1.7320508075688772)
m.e74 = Constraint(expr= -sqrt((-0.8419027314789557 + m.x121)**2 + (
    -0.5995547289462685 + m.x122)**2 + (-0.9174626648558603 + m.x123)**2) +
    m.x74 - 1.7320508075688772 * m.b206 >= -1.7320508075688772)
m.e75 = Constraint(expr= -sqrt((-0.9721691074362717 + m.x121)**2 + (
    -0.6544238205879963 + m.x122)**2 + (-0.535204782203361 + m.x123)**2) +
    m.x75 - 1.7320508075688772 * m.b207 >= -1.7320508075688772)
m.e76 = Constraint(expr= -sqrt((-0.06763103158333483 + m.x121)**2 + (
    -0.023510063056781383 + m.x122)**2 + (-0.8052942869277137 + m.x123)**2) +
    m.x76 - 1.7320508075688772 * m.b208 >= -1.7320508075688772)
m.e77 = Constraint(expr= -sqrt((-0.6719697138652216 + m.x121)**2 + (
    -0.7630117418529349 + m.x122)**2 + (-0.5656524680218609 + m.x123)**2) +
    m.x77 - 1.7320508075688772 * m.b209 >= -1.7320508075688772)
m.e78 = Constraint(expr= -sqrt((-0.6738937592389419 + m.x121)**2 + (
    -0.6387228188088844 + m.x122)**2 + (-0.8951756504920998 + m.x123)**2) +
    m.x78 - 1.7320508075688772 * m.b210 >= -1.7320508075688772)
m.e79 = Constraint(expr= -sqrt((-0.5390815646058106 + m.x124)**2 + (
    -0.2891964436397205 + m.x125)**2 + (-0.03003690855112706 + m.x126)**2) +
    m.x79 - 1.7320508075688772 * m.b211 >= -1.7320508075688772)
m.e80 = Constraint(expr= -sqrt((-0.6536357538927619 + m.x124)**2 + (
    -0.21000869554973112 + m.x125)**2 + (-0.2572769749796092 + m.x126)**2) +
    m.x80 - 1.7320508075688772 * m.b212 >= -1.7320508075688772)
m.e81 = Constraint(expr= -sqrt((-0.39719826263322744 + m.x124)**2 + (
    -0.6415781537746728 + m.x125)**2 + (-0.9888112104037214 + m.x126)**2) +
    m.x81 - 1.7320508075688772 * m.b213 >= -1.7320508075688772)
m.e82 = Constraint(expr= -sqrt((-0.46153301006262504 + m.x124)**2 + (
    -0.9934850076016687 + m.x125)**2 + (-0.9925719941586278 + m.x126)**2) +
    m.x82 - 1.7320508075688772 * m.b214 >= -1.7320508075688772)
m.e83 = Constraint(expr= -sqrt((-0.24267553557344324 + m.x124)**2 + (
    -0.07264511287134134 + m.x125)**2 + (-0.159901022229618 + m.x126)**2) +
    m.x83 - 1.7320508075688772 * m.b215 >= -1.7320508075688772)
m.e84 = Constraint(expr= -sqrt((-0.8419027314789557 + m.x124)**2 + (
    -0.5995547289462685 + m.x125)**2 + (-0.9174626648558603 + m.x126)**2) +
    m.x84 - 1.7320508075688772 * m.b216 >= -1.7320508075688772)
m.e85 = Constraint(expr= -sqrt((-0.9721691074362717 + m.x124)**2 + (
    -0.6544238205879963 + m.x125)**2 + (-0.535204782203361 + m.x126)**2) +
    m.x85 - 1.7320508075688772 * m.b217 >= -1.7320508075688772)
m.e86 = Constraint(expr= -sqrt((-0.06763103158333483 + m.x124)**2 + (
    -0.023510063056781383 + m.x125)**2 + (-0.8052942869277137 + m.x126)**2) +
    m.x86 - 1.7320508075688772 * m.b218 >= -1.7320508075688772)
m.e87 = Constraint(expr= -sqrt((-0.6719697138652216 + m.x124)**2 + (
    -0.7630117418529349 + m.x125)**2 + (-0.5656524680218609 + m.x126)**2) +
    m.x87 - 1.7320508075688772 * m.b219 >= -1.7320508075688772)
m.e88 = Constraint(expr= -sqrt((-0.6738937592389419 + m.x124)**2 + (
    -0.6387228188088844 + m.x125)**2 + (-0.8951756504920998 + m.x126)**2) +
    m.x88 - 1.7320508075688772 * m.b220 >= -1.7320508075688772)
m.e89 = Constraint(expr= -sqrt((-0.5390815646058106 + m.x127)**2 + (
    -0.2891964436397205 + m.x128)**2 + (-0.03003690855112706 + m.x129)**2) +
    m.x89 - 1.7320508075688772 * m.b221 >= -1.7320508075688772)
m.e90 = Constraint(expr= -sqrt((-0.6536357538927619 + m.x127)**2 + (
    -0.21000869554973112 + m.x128)**2 + (-0.2572769749796092 + m.x129)**2) +
    m.x90 - 1.7320508075688772 * m.b222 >= -1.7320508075688772)
m.e91 = Constraint(expr= -sqrt((-0.39719826263322744 + m.x127)**2 + (
    -0.6415781537746728 + m.x128)**2 + (-0.9888112104037214 + m.x129)**2) +
    m.x91 - 1.7320508075688772 * m.b223 >= -1.7320508075688772)
m.e92 = Constraint(expr= -sqrt((-0.46153301006262504 + m.x127)**2 + (
    -0.9934850076016687 + m.x128)**2 + (-0.9925719941586278 + m.x129)**2) +
    m.x92 - 1.7320508075688772 * m.b224 >= -1.7320508075688772)
m.e93 = Constraint(expr= -sqrt((-0.24267553557344324 + m.x127)**2 + (
    -0.07264511287134134 + m.x128)**2 + (-0.159901022229618 + m.x129)**2) +
    m.x93 - 1.7320508075688772 * m.b225 >= -1.7320508075688772)
m.e94 = Constraint(expr= -sqrt((-0.8419027314789557 + m.x127)**2 + (
    -0.5995547289462685 + m.x128)**2 + (-0.9174626648558603 + m.x129)**2) +
    m.x94 - 1.7320508075688772 * m.b226 >= -1.7320508075688772)
m.e95 = Constraint(expr= -sqrt((-0.9721691074362717 + m.x127)**2 + (
    -0.6544238205879963 + m.x128)**2 + (-0.535204782203361 + m.x129)**2) +
    m.x95 - 1.7320508075688772 * m.b227 >= -1.7320508075688772)
m.e96 = Constraint(expr= -sqrt((-0.06763103158333483 + m.x127)**2 + (
    -0.023510063056781383 + m.x128)**2 + (-0.8052942869277137 + m.x129)**2) +
    m.x96 - 1.7320508075688772 * m.b228 >= -1.7320508075688772)
m.e97 = Constraint(expr= -sqrt((-0.6719697138652216 + m.x127)**2 + (
    -0.7630117418529349 + m.x128)**2 + (-0.5656524680218609 + m.x129)**2) +
    m.x97 - 1.7320508075688772 * m.b229 >= -1.7320508075688772)
m.e98 = Constraint(expr= -sqrt((-0.6738937592389419 + m.x127)**2 + (
    -0.6387228188088844 + m.x128)**2 + (-0.8951756504920998 + m.x129)**2) +
    m.x98 - 1.7320508075688772 * m.b230 >= -1.7320508075688772)
m.e99 = Constraint(expr= -sqrt((-0.5390815646058106 + m.x130)**2 + (
    -0.2891964436397205 + m.x131)**2 + (-0.03003690855112706 + m.x132)**2) +
    m.x99 - 1.7320508075688772 * m.b231 >= -1.7320508075688772)
m.e100 = Constraint(expr= -sqrt((-0.6536357538927619 + m.x130)**2 + (
    -0.21000869554973112 + m.x131)**2 + (-0.2572769749796092 + m.x132)**2) +
    m.x100 - 1.7320508075688772 * m.b232 >= -1.7320508075688772)
m.e101 = Constraint(expr= -sqrt((-0.39719826263322744 + m.x130)**2 + (
    -0.6415781537746728 + m.x131)**2 + (-0.9888112104037214 + m.x132)**2) +
    m.x101 - 1.7320508075688772 * m.b233 >= -1.7320508075688772)
m.e102 = Constraint(expr= -sqrt((-0.46153301006262504 + m.x130)**2 + (
    -0.9934850076016687 + m.x131)**2 + (-0.9925719941586278 + m.x132)**2) +
    m.x102 - 1.7320508075688772 * m.b234 >= -1.7320508075688772)
m.e103 = Constraint(expr= -sqrt((-0.24267553557344324 + m.x130)**2 + (
    -0.07264511287134134 + m.x131)**2 + (-0.159901022229618 + m.x132)**2) +
    m.x103 - 1.7320508075688772 * m.b235 >= -1.7320508075688772)
m.e104 = Constraint(expr= -sqrt((-0.8419027314789557 + m.x130)**2 + (
    -0.5995547289462685 + m.x131)**2 + (-0.9174626648558603 + m.x132)**2) +
    m.x104 - 1.7320508075688772 * m.b236 >= -1.7320508075688772)
m.e105 = Constraint(expr= -sqrt((-0.9721691074362717 + m.x130)**2 + (
    -0.6544238205879963 + m.x131)**2 + (-0.535204782203361 + m.x132)**2) +
    m.x105 - 1.7320508075688772 * m.b237 >= -1.7320508075688772)
m.e106 = Constraint(expr= -sqrt((-0.06763103158333483 + m.x130)**2 + (
    -0.023510063056781383 + m.x131)**2 + (-0.8052942869277137 + m.x132)**2) +
    m.x106 - 1.7320508075688772 * m.b238 >= -1.7320508075688772)
m.e107 = Constraint(expr= -sqrt((-0.6719697138652216 + m.x130)**2 + (
    -0.7630117418529349 + m.x131)**2 + (-0.5656524680218609 + m.x132)**2) +
    m.x107 - 1.7320508075688772 * m.b239 >= -1.7320508075688772)
m.e108 = Constraint(expr= -sqrt((-0.6738937592389419 + m.x130)**2 + (
    -0.6387228188088844 + m.x131)**2 + (-0.8951756504920998 + m.x132)**2) +
    m.x108 - 1.7320508075688772 * m.b240 >= -1.7320508075688772)
m.e109 = Constraint(expr= m.b161 + m.b171 + m.b181 + m.b191 + m.b201 + m.b211
    + m.b221 + m.b231 == 1)
m.e110 = Constraint(expr= m.b162 + m.b172 + m.b182 + m.b192 + m.b202 + m.b212
    + m.b222 + m.b232 == 1)
m.e111 = Constraint(expr= m.b163 + m.b173 + m.b183 + m.b193 + m.b203 + m.b213
    + m.b223 + m.b233 == 1)
m.e112 = Constraint(expr= m.b164 + m.b174 + m.b184 + m.b194 + m.b204 + m.b214
    + m.b224 + m.b234 == 1)
m.e113 = Constraint(expr= m.b165 + m.b175 + m.b185 + m.b195 + m.b205 + m.b215
    + m.b225 + m.b235 == 1)
m.e114 = Constraint(expr= m.b166 + m.b176 + m.b186 + m.b196 + m.b206 + m.b216
    + m.b226 + m.b236 == 1)
m.e115 = Constraint(expr= m.b167 + m.b177 + m.b187 + m.b197 + m.b207 + m.b217
    + m.b227 + m.b237 == 1)
m.e116 = Constraint(expr= m.b168 + m.b178 + m.b188 + m.b198 + m.b208 + m.b218
    + m.b228 + m.b238 == 1)
m.e117 = Constraint(expr= m.b169 + m.b179 + m.b189 + m.b199 + m.b209 + m.b219
    + m.b229 + m.b239 == 1)
m.e118 = Constraint(expr= m.b170 + m.b180 + m.b190 + m.b200 + m.b210 + m.b220
    + m.b230 + m.b240 == 1)
m.e119 = Constraint(expr= m.b133 + m.b134 + m.b135 + m.b136 + m.b137 + m.b138
    + m.b139 + m.b161 + m.b162 + m.b163 + m.b164 + m.b165 + m.b166 + m.b167 +
    m.b168 + m.b169 + m.b170 == 3)
m.e120 = Constraint(expr= m.b133 + m.b140 + m.b141 + m.b142 + m.b143 + m.b144
    + m.b145 + m.b171 + m.b172 + m.b173 + m.b174 + m.b175 + m.b176 + m.b177 +
    m.b178 + m.b179 + m.b180 == 3)
m.e121 = Constraint(expr= m.b134 + m.b140 + m.b146 + m.b147 + m.b148 + m.b149
    + m.b150 + m.b181 + m.b182 + m.b183 + m.b184 + m.b185 + m.b186 + m.b187 +
    m.b188 + m.b189 + m.b190 == 3)
m.e122 = Constraint(expr= m.b135 + m.b141 + m.b146 + m.b151 + m.b152 + m.b153
    + m.b154 + m.b191 + m.b192 + m.b193 + m.b194 + m.b195 + m.b196 + m.b197 +
    m.b198 + m.b199 + m.b200 == 3)
m.e123 = Constraint(expr= m.b136 + m.b142 + m.b147 + m.b151 + m.b155 + m.b156
    + m.b157 + m.b201 + m.b202 + m.b203 + m.b204 + m.b205 + m.b206 + m.b207 +
    m.b208 + m.b209 + m.b210 == 3)
m.e124 = Constraint(expr= m.b137 + m.b143 + m.b148 + m.b152 + m.b155 + m.b158
    + m.b159 + m.b211 + m.b212 + m.b213 + m.b214 + m.b215 + m.b216 + m.b217 +
    m.b218 + m.b219 + m.b220 == 3)
m.e125 = Constraint(expr= m.b138 + m.b144 + m.b149 + m.b153 + m.b156 + m.b158
    + m.b160 + m.b221 + m.b222 + m.b223 + m.b224 + m.b225 + m.b226 + m.b227 +
    m.b228 + m.b229 + m.b230 == 3)
m.e126 = Constraint(expr= m.b139 + m.b145 + m.b150 + m.b154 + m.b157 + m.b159
    + m.b160 + m.b231 + m.b232 + m.b233 + m.b234 + m.b235 + m.b236 + m.b237 +
    m.b238 + m.b239 + m.b240 == 3)
m.e127 = Constraint(expr= m.b133 == 1)
m.e128 = Constraint(expr= m.b134 + m.b140 == 1)
m.e129 = Constraint(expr= m.b135 + m.b141 + m.b146 == 1)
m.e130 = Constraint(expr= m.b136 + m.b142 + m.b147 + m.b151 == 1)
m.e131 = Constraint(expr= m.b137 + m.b143 + m.b148 + m.b152 + m.b155 == 1)
m.e132 = Constraint(expr= m.b138 + m.b144 + m.b149 + m.b153 + m.b156 + m.b158
    == 1)
m.e133 = Constraint(expr= m.b139 + m.b145 + m.b150 + m.b154 + m.b157 + m.b159
    + m.b160 == 1)
