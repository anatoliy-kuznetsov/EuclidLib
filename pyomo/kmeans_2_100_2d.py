# NLP written by GAMS Convert at 05/15/24 11:44:39
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       100      100        0        0        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#       204      204        0        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       200      200        0
#
# Reformulation has removed 1 variable and 1 equation

from pyomo.environ import *

model = m = ConcreteModel()

m.x1 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x2 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x3 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x4 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x5 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x6 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x7 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x8 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x9 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x10 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x11 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x12 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x13 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x14 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x15 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x16 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x17 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x18 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x19 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x20 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x21 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x22 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x23 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x24 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x25 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x26 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x27 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x28 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x29 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x30 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x31 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x32 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x33 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x34 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x35 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x36 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x37 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x38 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x39 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x40 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x41 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x42 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x43 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x44 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x45 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x46 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x47 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x48 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x49 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x50 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x51 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x52 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x53 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x54 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x55 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x56 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x57 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x58 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x59 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x60 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x61 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x62 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x63 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x64 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x65 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x66 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x67 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x68 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x69 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x70 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x71 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x72 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x73 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x74 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x75 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x76 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x77 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x78 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x79 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x80 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x81 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x82 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x83 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x84 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x85 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x86 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x87 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x88 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x89 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x90 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x91 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x92 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x93 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x94 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x95 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x96 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x97 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x98 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x99 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x100 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x101 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x102 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x103 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x104 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x105 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x106 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x107 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x108 = Var(within=Reals, bounds=(0,1), initialize=0)
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
m.x149 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x150 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x151 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x152 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x153 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x154 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x155 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x156 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x157 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x158 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x159 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x160 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x161 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x162 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x163 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x164 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x165 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x166 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x167 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x168 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x169 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x170 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x171 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x172 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x173 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x174 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x175 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x176 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x177 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x178 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x179 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x180 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x181 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x182 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x183 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x184 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x185 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x186 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x187 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x188 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x189 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x190 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x191 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x192 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x193 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x194 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x195 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x196 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x197 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x198 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x199 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x200 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x201 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x202 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x203 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x204 = Var(within=Reals, bounds=(0,1), initialize=0)

m.obj = Objective(sense=minimize, expr= m.x5 * ((-0.7638815744633954 + m.x1)**2
    + (-0.6447807510863064 + m.x2)**2) + m.x6 * ((-0.40943808013995275 + m.x1)
    **2 + (-0.19808744040113768 + m.x2)**2) + m.x7 * ((-0.6767003342360466 +
    m.x1)**2 + (-0.9692858163726752 + m.x2)**2) + m.x8 * ((-0.42774708898859193
    + m.x1)**2 + (-0.8508748594767727 + m.x2)**2) + m.x9 * ((
    -0.036078303300847936 + m.x1)**2 + (-0.5277860412448065 + m.x2)**2) + m.x10
    * ((-0.20155321238517532 + m.x1)**2 + (-0.4942660229634893 + m.x2)**2) +
    m.x11 * ((-0.6112527232963626 + m.x1)**2 + (-0.8559082496370558 + m.x2)**2)
    + m.x12 * ((-0.5229658349769678 + m.x1)**2 + (-0.8688389390876086 + m.x2)
    **2) + m.x13 * ((-0.32677934673499076 + m.x1)**2 + (-0.12840989549245074 +
    m.x2)**2) + m.x14 * ((-0.464946990798343 + m.x1)**2 + (-0.7152468996358645
    + m.x2)**2) + m.x15 * ((-0.7079444055031988 + m.x1)**2 + (
    -0.03674529136974525 + m.x2)**2) + m.x16 * ((-0.24857148343947266 + m.x1)**
    2 + (-0.25434474234978877 + m.x2)**2) + m.x17 * ((-0.47157968486789925 +
    m.x1)**2 + (-0.8617020435058247 + m.x2)**2) + m.x18 * ((
    -0.27090929424730037 + m.x1)**2 + (-0.04588509298910648 + m.x2)**2) + m.x19
    * ((-0.898044162818999 + m.x1)**2 + (-0.8692000927533886 + m.x2)**2) +
    m.x20 * ((-0.7706996582437882 + m.x1)**2 + (-0.03868779823161672 + m.x2)**2)
    + m.x21 * ((-0.26071076848820574 + m.x1)**2 + (-0.17679425487660894 + m.x2)
    **2) + m.x22 * ((-0.9149845853572381 + m.x1)**2 + (-0.1247762691814659 +
    m.x2)**2) + m.x23 * ((-0.12749534009772823 + m.x1)**2 + (
    -0.22064485914448861 + m.x2)**2) + m.x24 * ((-0.7909890387518833 + m.x1)**2
    + (-0.19802256998212397 + m.x2)**2) + m.x25 * ((-0.9833758044078205 + m.x1)
    **2 + (-0.30815505903287455 + m.x2)**2) + m.x26 * ((-0.6500811602972846 +
    m.x1)**2 + (-0.1918766967857739 + m.x2)**2) + m.x27 * ((
    -0.29205572110731104 + m.x1)**2 + (-0.8654062707721905 + m.x2)**2) + m.x28
    * ((-0.9975602236830079 + m.x1)**2 + (-0.24234912525910135 + m.x2)**2) +
    m.x29 * ((-0.3494958562329116 + m.x1)**2 + (-0.05738465199820186 + m.x2)**2)
    + m.x30 * ((-0.19459585690947445 + m.x1)**2 + (-0.38396148675330977 + m.x2)
    **2) + m.x31 * ((-0.5211296287363507 + m.x1)**2 + (-0.5728266339465008 +
    m.x2)**2) + m.x32 * ((-0.3494505167705202 + m.x1)**2 + (-0.1580478194401167
    + m.x2)**2) + m.x33 * ((-0.5557031473401765 + m.x1)**2 + (
    -0.34891657446743507 + m.x2)**2) + m.x34 * ((-0.34511962615759206 + m.x1)**
    2 + (-0.9732087418298719 + m.x2)**2) + m.x35 * ((-0.5872592428652408 + m.x1)
    **2 + (-0.015131720013235594 + m.x2)**2) + m.x36 * ((-0.9570810173892395 +
    m.x1)**2 + (-0.9697011150746265 + m.x2)**2) + m.x37 * ((-0.3899178249402995
    + m.x1)**2 + (-0.9796379455859785 + m.x2)**2) + m.x38 * ((
    -0.10503597027001488 + m.x1)**2 + (-0.9186653549784145 + m.x2)**2) + m.x39
    * ((-0.16886817106488827 + m.x1)**2 + (-0.8640299707248008 + m.x2)**2) +
    m.x40 * ((-0.677393015469918 + m.x1)**2 + (-0.958336820535021 + m.x2)**2)
    + m.x41 * ((-0.30228094004558437 + m.x1)**2 + (-0.6539282549257739 + m.x2)
    **2) + m.x42 * ((-0.9405720076563844 + m.x1)**2 + (-0.1288487580388612 +
    m.x2)**2) + m.x43 * ((-0.18510410684438972 + m.x1)**2 + (
    -0.5570599695054576 + m.x2)**2) + m.x44 * ((-0.1336947339751663 + m.x1)**2
    + (-0.05453928468702074 + m.x2)**2) + m.x45 * ((-0.015523122041815163 +
    m.x1)**2 + (-0.34696045313653123 + m.x2)**2) + m.x46 * ((
    -0.6499602306210984 + m.x1)**2 + (-0.4658578540938607 + m.x2)**2) + m.x47
    * ((-0.6041332716945342 + m.x1)**2 + (-0.026368748395587893 + m.x2)**2) +
    m.x48 * ((-0.10124766221453585 + m.x1)**2 + (-0.5654261544724538 + m.x2)**2)
    + m.x49 * ((-0.15680423108532615 + m.x1)**2 + (-0.012824944273280403 +
    m.x2)**2) + m.x50 * ((-0.06161851290700826 + m.x1)**2 + (
    -0.6518827219485058 + m.x2)**2) + m.x51 * ((-0.9599300852975065 + m.x1)**2
    + (-0.4963045372344488 + m.x2)**2) + m.x52 * ((-0.006289238982428391 +
    m.x1)**2 + (-0.1947794521035049 + m.x2)**2) + m.x53 * ((-0.6812923526386081
    + m.x1)**2 + (-0.7926520562656519 + m.x2)**2) + m.x54 * ((
    -0.20604181596784943 + m.x1)**2 + (-0.46748791606580087 + m.x2)**2) + m.x55
    * ((-0.03630839980614653 + m.x1)**2 + (-0.5402450431444167 + m.x2)**2) +
    m.x56 * ((-0.756077508833009 + m.x1)**2 + (-0.49959407928270205 + m.x2)**2)
    + m.x57 * ((-0.7852773044289958 + m.x1)**2 + (-0.23424898721227194 + m.x2)
    **2) + m.x58 * ((-0.6660319564191836 + m.x1)**2 + (-0.47071635679190515 +
    m.x2)**2) + m.x59 * ((-0.6035913241862448 + m.x1)**2 + (
    -0.07281748372873065 + m.x2)**2) + m.x60 * ((-0.4538937693071986 + m.x1)**2
    + (-0.6200193225537551 + m.x2)**2) + m.x61 * ((-0.23417215110972356 + m.x1)
    **2 + (-0.5539355889533747 + m.x2)**2) + m.x62 * ((-0.01966969700413501 +
    m.x1)**2 + (-0.4179602560886627 + m.x2)**2) + m.x63 * ((-0.9412028197949556
    + m.x1)**2 + (-0.6470504724458113 + m.x2)**2) + m.x64 * ((
    -0.5061461450725504 + m.x1)**2 + (-0.8710807411457973 + m.x2)**2) + m.x65
    * ((-0.6935892521969669 + m.x1)**2 + (-0.5089022416018498 + m.x2)**2) +
    m.x66 * ((-0.37519097252023725 + m.x1)**2 + (-0.8737532376735282 + m.x2)**2)
    + m.x67 * ((-0.5643281702155495 + m.x1)**2 + (-0.48755638256953904 + m.x2)
    **2) + m.x68 * ((-0.37140463524028267 + m.x1)**2 + (-0.1527719143761158 +
    m.x2)**2) + m.x69 * ((-0.19047370627583904 + m.x1)**2 + (
    -0.6025314595643306 + m.x2)**2) + m.x70 * ((-0.5373125801595716 + m.x1)**2
    + (-0.7745694336404262 + m.x2)**2) + m.x71 * ((-0.44911066812217937 + m.x1)
    **2 + (-0.38450791343289026 + m.x2)**2) + m.x72 * ((-0.5553143405841365 +
    m.x1)**2 + (-0.25128770486599317 + m.x2)**2) + m.x73 * ((
    -0.9615743551078895 + m.x1)**2 + (-0.6352708035606135 + m.x2)**2) + m.x74
    * ((-0.30073836938485243 + m.x1)**2 + (-0.49164698681513486 + m.x2)**2) +
    m.x75 * ((-0.8407722422486795 + m.x1)**2 + (-0.9508945317116384 + m.x2)**2)
    + m.x76 * ((-0.699882909462003 + m.x1)**2 + (-0.8773974424492639 + m.x2)**
    2) + m.x77 * ((-0.8066516311507484 + m.x1)**2 + (-0.36733907167219004 +
    m.x2)**2) + m.x78 * ((-0.41782103194430553 + m.x1)**2 + (
    -0.46509605756754535 + m.x2)**2) + m.x79 * ((-0.052063353108449784 + m.x1)
    **2 + (-0.5914715882861393 + m.x2)**2) + m.x80 * ((-0.5522742956937672 +
    m.x1)**2 + (-0.7870882486811381 + m.x2)**2) + m.x81 * ((
    -0.33989034102585525 + m.x1)**2 + (-0.9772133248871614 + m.x2)**2) + m.x82
    * ((-0.7387381242549643 + m.x1)**2 + (-0.5788591594627351 + m.x2)**2) +
    m.x83 * ((-0.22760920288056674 + m.x1)**2 + (-0.9339733226024151 + m.x2)**2)
    + m.x84 * ((-0.6834608410061699 + m.x1)**2 + (-0.633945255772792 + m.x2)**
    2) + m.x85 * ((-0.19375104317663272 + m.x1)**2 + (-0.19818101302971025 +
    m.x2)**2) + m.x86 * ((-0.19628039864937719 + m.x1)**2 + (
    -0.9182226354814971 + m.x2)**2) + m.x87 * ((-0.4429223464468689 + m.x1)**2
    + (-0.7011950391916014 + m.x2)**2) + m.x88 * ((-0.6917419384692055 + m.x1)
    **2 + (-0.8122384539539016 + m.x2)**2) + m.x89 * ((-0.2888618807286597 +
    m.x1)**2 + (-0.20187601551054601 + m.x2)**2) + m.x90 * ((
    -0.9629923696144377 + m.x1)**2 + (-0.14073358274713377 + m.x2)**2) + m.x91
    * ((-0.9998128998577391 + m.x1)**2 + (-0.39611446123084215 + m.x2)**2) +
    m.x92 * ((-0.021438472259998176 + m.x1)**2 + (-0.3009646599273207 + m.x2)**
    2) + m.x93 * ((-0.7664028979467367 + m.x1)**2 + (-0.4053459265820296 + m.x2)
    **2) + m.x94 * ((-0.13947384494738524 + m.x1)**2 + (-0.07761778225326532 +
    m.x2)**2) + m.x95 * ((-0.04939157261592375 + m.x1)**2 + (
    -0.5718598324860983 + m.x2)**2) + m.x96 * ((-0.3666923117354318 + m.x1)**2
    + (-0.6778816126131987 + m.x2)**2) + m.x97 * ((-0.12581488446795952 + m.x1)
    **2 + (-0.28413538086587065 + m.x2)**2) + m.x98 * ((-0.5534812169259425 +
    m.x1)**2 + (-0.3255356339585811 + m.x2)**2) + m.x99 * ((-0.6941512613591387
    + m.x1)**2 + (-0.2607007011921715 + m.x2)**2) + m.x100 * ((
    -0.750731182626847 + m.x1)**2 + (-0.6637116910019771 + m.x2)**2) + m.x101
    * ((-0.4125100870640045 + m.x1)**2 + (-0.7043591355389139 + m.x2)**2) +
    m.x102 * ((-0.3466063100961543 + m.x1)**2 + (-0.9204660924554171 + m.x2)**2)
    + m.x103 * ((-0.7414024117385918 + m.x1)**2 + (-0.28561026008047496 + m.x2)
    **2) + m.x104 * ((-0.8503692077224103 + m.x1)**2 + (-0.6275276431322121 +
    m.x2)**2) + m.x105 * ((-0.7638815744633954 + m.x3)**2 + (
    -0.6447807510863064 + m.x4)**2) + m.x106 * ((-0.40943808013995275 + m.x3)**
    2 + (-0.19808744040113768 + m.x4)**2) + m.x107 * ((-0.6767003342360466 +
    m.x3)**2 + (-0.9692858163726752 + m.x4)**2) + m.x108 * ((
    -0.42774708898859193 + m.x3)**2 + (-0.8508748594767727 + m.x4)**2) + m.x109
    * ((-0.036078303300847936 + m.x3)**2 + (-0.5277860412448065 + m.x4)**2) +
    m.x110 * ((-0.20155321238517532 + m.x3)**2 + (-0.4942660229634893 + m.x4)**
    2) + m.x111 * ((-0.6112527232963626 + m.x3)**2 + (-0.8559082496370558 +
    m.x4)**2) + m.x112 * ((-0.5229658349769678 + m.x3)**2 + (
    -0.8688389390876086 + m.x4)**2) + m.x113 * ((-0.32677934673499076 + m.x3)**
    2 + (-0.12840989549245074 + m.x4)**2) + m.x114 * ((-0.464946990798343 +
    m.x3)**2 + (-0.7152468996358645 + m.x4)**2) + m.x115 * ((
    -0.7079444055031988 + m.x3)**2 + (-0.03674529136974525 + m.x4)**2) + m.x116
    * ((-0.24857148343947266 + m.x3)**2 + (-0.25434474234978877 + m.x4)**2) +
    m.x117 * ((-0.47157968486789925 + m.x3)**2 + (-0.8617020435058247 + m.x4)**
    2) + m.x118 * ((-0.27090929424730037 + m.x3)**2 + (-0.04588509298910648 +
    m.x4)**2) + m.x119 * ((-0.898044162818999 + m.x3)**2 + (-0.8692000927533886
    + m.x4)**2) + m.x120 * ((-0.7706996582437882 + m.x3)**2 + (
    -0.03868779823161672 + m.x4)**2) + m.x121 * ((-0.26071076848820574 + m.x3)
    **2 + (-0.17679425487660894 + m.x4)**2) + m.x122 * ((-0.9149845853572381 +
    m.x3)**2 + (-0.1247762691814659 + m.x4)**2) + m.x123 * ((
    -0.12749534009772823 + m.x3)**2 + (-0.22064485914448861 + m.x4)**2) +
    m.x124 * ((-0.7909890387518833 + m.x3)**2 + (-0.19802256998212397 + m.x4)**
    2) + m.x125 * ((-0.9833758044078205 + m.x3)**2 + (-0.30815505903287455 +
    m.x4)**2) + m.x126 * ((-0.6500811602972846 + m.x3)**2 + (
    -0.1918766967857739 + m.x4)**2) + m.x127 * ((-0.29205572110731104 + m.x3)**
    2 + (-0.8654062707721905 + m.x4)**2) + m.x128 * ((-0.9975602236830079 +
    m.x3)**2 + (-0.24234912525910135 + m.x4)**2) + m.x129 * ((
    -0.3494958562329116 + m.x3)**2 + (-0.05738465199820186 + m.x4)**2) + m.x130
    * ((-0.19459585690947445 + m.x3)**2 + (-0.38396148675330977 + m.x4)**2) +
    m.x131 * ((-0.5211296287363507 + m.x3)**2 + (-0.5728266339465008 + m.x4)**2)
    + m.x132 * ((-0.3494505167705202 + m.x3)**2 + (-0.1580478194401167 + m.x4)
    **2) + m.x133 * ((-0.5557031473401765 + m.x3)**2 + (-0.34891657446743507 +
    m.x4)**2) + m.x134 * ((-0.34511962615759206 + m.x3)**2 + (
    -0.9732087418298719 + m.x4)**2) + m.x135 * ((-0.5872592428652408 + m.x3)**2
    + (-0.015131720013235594 + m.x4)**2) + m.x136 * ((-0.9570810173892395 +
    m.x3)**2 + (-0.9697011150746265 + m.x4)**2) + m.x137 * ((
    -0.3899178249402995 + m.x3)**2 + (-0.9796379455859785 + m.x4)**2) + m.x138
    * ((-0.10503597027001488 + m.x3)**2 + (-0.9186653549784145 + m.x4)**2) +
    m.x139 * ((-0.16886817106488827 + m.x3)**2 + (-0.8640299707248008 + m.x4)**
    2) + m.x140 * ((-0.677393015469918 + m.x3)**2 + (-0.958336820535021 + m.x4)
    **2) + m.x141 * ((-0.30228094004558437 + m.x3)**2 + (-0.6539282549257739 +
    m.x4)**2) + m.x142 * ((-0.9405720076563844 + m.x3)**2 + (
    -0.1288487580388612 + m.x4)**2) + m.x143 * ((-0.18510410684438972 + m.x3)**
    2 + (-0.5570599695054576 + m.x4)**2) + m.x144 * ((-0.1336947339751663 +
    m.x3)**2 + (-0.05453928468702074 + m.x4)**2) + m.x145 * ((
    -0.015523122041815163 + m.x3)**2 + (-0.34696045313653123 + m.x4)**2) +
    m.x146 * ((-0.6499602306210984 + m.x3)**2 + (-0.4658578540938607 + m.x4)**2)
    + m.x147 * ((-0.6041332716945342 + m.x3)**2 + (-0.026368748395587893 +
    m.x4)**2) + m.x148 * ((-0.10124766221453585 + m.x3)**2 + (
    -0.5654261544724538 + m.x4)**2) + m.x149 * ((-0.15680423108532615 + m.x3)**
    2 + (-0.012824944273280403 + m.x4)**2) + m.x150 * ((-0.06161851290700826 +
    m.x3)**2 + (-0.6518827219485058 + m.x4)**2) + m.x151 * ((
    -0.9599300852975065 + m.x3)**2 + (-0.4963045372344488 + m.x4)**2) + m.x152
    * ((-0.006289238982428391 + m.x3)**2 + (-0.1947794521035049 + m.x4)**2) +
    m.x153 * ((-0.6812923526386081 + m.x3)**2 + (-0.7926520562656519 + m.x4)**2)
    + m.x154 * ((-0.20604181596784943 + m.x3)**2 + (-0.46748791606580087 +
    m.x4)**2) + m.x155 * ((-0.03630839980614653 + m.x3)**2 + (
    -0.5402450431444167 + m.x4)**2) + m.x156 * ((-0.756077508833009 + m.x3)**2
    + (-0.49959407928270205 + m.x4)**2) + m.x157 * ((-0.7852773044289958 +
    m.x3)**2 + (-0.23424898721227194 + m.x4)**2) + m.x158 * ((
    -0.6660319564191836 + m.x3)**2 + (-0.47071635679190515 + m.x4)**2) + m.x159
    * ((-0.6035913241862448 + m.x3)**2 + (-0.07281748372873065 + m.x4)**2) +
    m.x160 * ((-0.4538937693071986 + m.x3)**2 + (-0.6200193225537551 + m.x4)**2)
    + m.x161 * ((-0.23417215110972356 + m.x3)**2 + (-0.5539355889533747 + m.x4)
    **2) + m.x162 * ((-0.01966969700413501 + m.x3)**2 + (-0.4179602560886627 +
    m.x4)**2) + m.x163 * ((-0.9412028197949556 + m.x3)**2 + (
    -0.6470504724458113 + m.x4)**2) + m.x164 * ((-0.5061461450725504 + m.x3)**2
    + (-0.8710807411457973 + m.x4)**2) + m.x165 * ((-0.6935892521969669 + m.x3)
    **2 + (-0.5089022416018498 + m.x4)**2) + m.x166 * ((-0.37519097252023725 +
    m.x3)**2 + (-0.8737532376735282 + m.x4)**2) + m.x167 * ((
    -0.5643281702155495 + m.x3)**2 + (-0.48755638256953904 + m.x4)**2) + m.x168
    * ((-0.37140463524028267 + m.x3)**2 + (-0.1527719143761158 + m.x4)**2) +
    m.x169 * ((-0.19047370627583904 + m.x3)**2 + (-0.6025314595643306 + m.x4)**
    2) + m.x170 * ((-0.5373125801595716 + m.x3)**2 + (-0.7745694336404262 +
    m.x4)**2) + m.x171 * ((-0.44911066812217937 + m.x3)**2 + (
    -0.38450791343289026 + m.x4)**2) + m.x172 * ((-0.5553143405841365 + m.x3)**
    2 + (-0.25128770486599317 + m.x4)**2) + m.x173 * ((-0.9615743551078895 +
    m.x3)**2 + (-0.6352708035606135 + m.x4)**2) + m.x174 * ((
    -0.30073836938485243 + m.x3)**2 + (-0.49164698681513486 + m.x4)**2) +
    m.x175 * ((-0.8407722422486795 + m.x3)**2 + (-0.9508945317116384 + m.x4)**2)
    + m.x176 * ((-0.699882909462003 + m.x3)**2 + (-0.8773974424492639 + m.x4)
    **2) + m.x177 * ((-0.8066516311507484 + m.x3)**2 + (-0.36733907167219004 +
    m.x4)**2) + m.x178 * ((-0.41782103194430553 + m.x3)**2 + (
    -0.46509605756754535 + m.x4)**2) + m.x179 * ((-0.052063353108449784 + m.x3)
    **2 + (-0.5914715882861393 + m.x4)**2) + m.x180 * ((-0.5522742956937672 +
    m.x3)**2 + (-0.7870882486811381 + m.x4)**2) + m.x181 * ((
    -0.33989034102585525 + m.x3)**2 + (-0.9772133248871614 + m.x4)**2) + m.x182
    * ((-0.7387381242549643 + m.x3)**2 + (-0.5788591594627351 + m.x4)**2) +
    m.x183 * ((-0.22760920288056674 + m.x3)**2 + (-0.9339733226024151 + m.x4)**
    2) + m.x184 * ((-0.6834608410061699 + m.x3)**2 + (-0.633945255772792 + m.x4)
    **2) + m.x185 * ((-0.19375104317663272 + m.x3)**2 + (-0.19818101302971025
    + m.x4)**2) + m.x186 * ((-0.19628039864937719 + m.x3)**2 + (
    -0.9182226354814971 + m.x4)**2) + m.x187 * ((-0.4429223464468689 + m.x3)**2
    + (-0.7011950391916014 + m.x4)**2) + m.x188 * ((-0.6917419384692055 + m.x3)
    **2 + (-0.8122384539539016 + m.x4)**2) + m.x189 * ((-0.2888618807286597 +
    m.x3)**2 + (-0.20187601551054601 + m.x4)**2) + m.x190 * ((
    -0.9629923696144377 + m.x3)**2 + (-0.14073358274713377 + m.x4)**2) + m.x191
    * ((-0.9998128998577391 + m.x3)**2 + (-0.39611446123084215 + m.x4)**2) +
    m.x192 * ((-0.021438472259998176 + m.x3)**2 + (-0.3009646599273207 + m.x4)
    **2) + m.x193 * ((-0.7664028979467367 + m.x3)**2 + (-0.4053459265820296 +
    m.x4)**2) + m.x194 * ((-0.13947384494738524 + m.x3)**2 + (
    -0.07761778225326532 + m.x4)**2) + m.x195 * ((-0.04939157261592375 + m.x3)
    **2 + (-0.5718598324860983 + m.x4)**2) + m.x196 * ((-0.3666923117354318 +
    m.x3)**2 + (-0.6778816126131987 + m.x4)**2) + m.x197 * ((
    -0.12581488446795952 + m.x3)**2 + (-0.28413538086587065 + m.x4)**2) +
    m.x198 * ((-0.5534812169259425 + m.x3)**2 + (-0.3255356339585811 + m.x4)**2)
    + m.x199 * ((-0.6941512613591387 + m.x3)**2 + (-0.2607007011921715 + m.x4)
    **2) + m.x200 * ((-0.750731182626847 + m.x3)**2 + (-0.6637116910019771 +
    m.x4)**2) + m.x201 * ((-0.4125100870640045 + m.x3)**2 + (
    -0.7043591355389139 + m.x4)**2) + m.x202 * ((-0.3466063100961543 + m.x3)**2
    + (-0.9204660924554171 + m.x4)**2) + m.x203 * ((-0.7414024117385918 + m.x3)
    **2 + (-0.28561026008047496 + m.x4)**2) + m.x204 * ((-0.8503692077224103 +
    m.x3)**2 + (-0.6275276431322121 + m.x4)**2))

m.e1 = Constraint(expr= m.x5 + m.x105 == 1)
m.e2 = Constraint(expr= m.x6 + m.x106 == 1)
m.e3 = Constraint(expr= m.x7 + m.x107 == 1)
m.e4 = Constraint(expr= m.x8 + m.x108 == 1)
m.e5 = Constraint(expr= m.x9 + m.x109 == 1)
m.e6 = Constraint(expr= m.x10 + m.x110 == 1)
m.e7 = Constraint(expr= m.x11 + m.x111 == 1)
m.e8 = Constraint(expr= m.x12 + m.x112 == 1)
m.e9 = Constraint(expr= m.x13 + m.x113 == 1)
m.e10 = Constraint(expr= m.x14 + m.x114 == 1)
m.e11 = Constraint(expr= m.x15 + m.x115 == 1)
m.e12 = Constraint(expr= m.x16 + m.x116 == 1)
m.e13 = Constraint(expr= m.x17 + m.x117 == 1)
m.e14 = Constraint(expr= m.x18 + m.x118 == 1)
m.e15 = Constraint(expr= m.x19 + m.x119 == 1)
m.e16 = Constraint(expr= m.x20 + m.x120 == 1)
m.e17 = Constraint(expr= m.x21 + m.x121 == 1)
m.e18 = Constraint(expr= m.x22 + m.x122 == 1)
m.e19 = Constraint(expr= m.x23 + m.x123 == 1)
m.e20 = Constraint(expr= m.x24 + m.x124 == 1)
m.e21 = Constraint(expr= m.x25 + m.x125 == 1)
m.e22 = Constraint(expr= m.x26 + m.x126 == 1)
m.e23 = Constraint(expr= m.x27 + m.x127 == 1)
m.e24 = Constraint(expr= m.x28 + m.x128 == 1)
m.e25 = Constraint(expr= m.x29 + m.x129 == 1)
m.e26 = Constraint(expr= m.x30 + m.x130 == 1)
m.e27 = Constraint(expr= m.x31 + m.x131 == 1)
m.e28 = Constraint(expr= m.x32 + m.x132 == 1)
m.e29 = Constraint(expr= m.x33 + m.x133 == 1)
m.e30 = Constraint(expr= m.x34 + m.x134 == 1)
m.e31 = Constraint(expr= m.x35 + m.x135 == 1)
m.e32 = Constraint(expr= m.x36 + m.x136 == 1)
m.e33 = Constraint(expr= m.x37 + m.x137 == 1)
m.e34 = Constraint(expr= m.x38 + m.x138 == 1)
m.e35 = Constraint(expr= m.x39 + m.x139 == 1)
m.e36 = Constraint(expr= m.x40 + m.x140 == 1)
m.e37 = Constraint(expr= m.x41 + m.x141 == 1)
m.e38 = Constraint(expr= m.x42 + m.x142 == 1)
m.e39 = Constraint(expr= m.x43 + m.x143 == 1)
m.e40 = Constraint(expr= m.x44 + m.x144 == 1)
m.e41 = Constraint(expr= m.x45 + m.x145 == 1)
m.e42 = Constraint(expr= m.x46 + m.x146 == 1)
m.e43 = Constraint(expr= m.x47 + m.x147 == 1)
m.e44 = Constraint(expr= m.x48 + m.x148 == 1)
m.e45 = Constraint(expr= m.x49 + m.x149 == 1)
m.e46 = Constraint(expr= m.x50 + m.x150 == 1)
m.e47 = Constraint(expr= m.x51 + m.x151 == 1)
m.e48 = Constraint(expr= m.x52 + m.x152 == 1)
m.e49 = Constraint(expr= m.x53 + m.x153 == 1)
m.e50 = Constraint(expr= m.x54 + m.x154 == 1)
m.e51 = Constraint(expr= m.x55 + m.x155 == 1)
m.e52 = Constraint(expr= m.x56 + m.x156 == 1)
m.e53 = Constraint(expr= m.x57 + m.x157 == 1)
m.e54 = Constraint(expr= m.x58 + m.x158 == 1)
m.e55 = Constraint(expr= m.x59 + m.x159 == 1)
m.e56 = Constraint(expr= m.x60 + m.x160 == 1)
m.e57 = Constraint(expr= m.x61 + m.x161 == 1)
m.e58 = Constraint(expr= m.x62 + m.x162 == 1)
m.e59 = Constraint(expr= m.x63 + m.x163 == 1)
m.e60 = Constraint(expr= m.x64 + m.x164 == 1)
m.e61 = Constraint(expr= m.x65 + m.x165 == 1)
m.e62 = Constraint(expr= m.x66 + m.x166 == 1)
m.e63 = Constraint(expr= m.x67 + m.x167 == 1)
m.e64 = Constraint(expr= m.x68 + m.x168 == 1)
m.e65 = Constraint(expr= m.x69 + m.x169 == 1)
m.e66 = Constraint(expr= m.x70 + m.x170 == 1)
m.e67 = Constraint(expr= m.x71 + m.x171 == 1)
m.e68 = Constraint(expr= m.x72 + m.x172 == 1)
m.e69 = Constraint(expr= m.x73 + m.x173 == 1)
m.e70 = Constraint(expr= m.x74 + m.x174 == 1)
m.e71 = Constraint(expr= m.x75 + m.x175 == 1)
m.e72 = Constraint(expr= m.x76 + m.x176 == 1)
m.e73 = Constraint(expr= m.x77 + m.x177 == 1)
m.e74 = Constraint(expr= m.x78 + m.x178 == 1)
m.e75 = Constraint(expr= m.x79 + m.x179 == 1)
m.e76 = Constraint(expr= m.x80 + m.x180 == 1)
m.e77 = Constraint(expr= m.x81 + m.x181 == 1)
m.e78 = Constraint(expr= m.x82 + m.x182 == 1)
m.e79 = Constraint(expr= m.x83 + m.x183 == 1)
m.e80 = Constraint(expr= m.x84 + m.x184 == 1)
m.e81 = Constraint(expr= m.x85 + m.x185 == 1)
m.e82 = Constraint(expr= m.x86 + m.x186 == 1)
m.e83 = Constraint(expr= m.x87 + m.x187 == 1)
m.e84 = Constraint(expr= m.x88 + m.x188 == 1)
m.e85 = Constraint(expr= m.x89 + m.x189 == 1)
m.e86 = Constraint(expr= m.x90 + m.x190 == 1)
m.e87 = Constraint(expr= m.x91 + m.x191 == 1)
m.e88 = Constraint(expr= m.x92 + m.x192 == 1)
m.e89 = Constraint(expr= m.x93 + m.x193 == 1)
m.e90 = Constraint(expr= m.x94 + m.x194 == 1)
m.e91 = Constraint(expr= m.x95 + m.x195 == 1)
m.e92 = Constraint(expr= m.x96 + m.x196 == 1)
m.e93 = Constraint(expr= m.x97 + m.x197 == 1)
m.e94 = Constraint(expr= m.x98 + m.x198 == 1)
m.e95 = Constraint(expr= m.x99 + m.x199 == 1)
m.e96 = Constraint(expr= m.x100 + m.x200 == 1)
m.e97 = Constraint(expr= m.x101 + m.x201 == 1)
m.e98 = Constraint(expr= m.x102 + m.x202 == 1)
m.e99 = Constraint(expr= m.x103 + m.x203 == 1)
m.e100 = Constraint(expr= m.x104 + m.x204 == 1)
