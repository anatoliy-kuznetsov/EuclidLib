# NLP written by GAMS Convert at 05/15/24 11:50:03
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       100      100        0        0        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#       206      206        0        0        0        0        0        0
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
m.x205 = Var(within=Reals, bounds=(0,1), initialize=0)
m.x206 = Var(within=Reals, bounds=(0,1), initialize=0)

m.obj = Objective(sense=minimize, expr= m.x7 * ((-0.9652039971760678 + m.x1)**2
    + (-0.539018346877163 + m.x2)**2 + (-0.5534528300690774 + m.x3)**2) + m.x8
    * ((-0.47484990909204716 + m.x1)**2 + (-0.1890132636768882 + m.x2)**2 + (
    -0.03754044605849893 + m.x3)**2) + m.x9 * ((-0.39771542845577124 + m.x1)**2
    + (-0.5036966948704162 + m.x2)**2 + (-0.7751554429159132 + m.x3)**2) +
    m.x10 * ((-0.3395623845814887 + m.x1)**2 + (-0.9699104997674314 + m.x2)**2
    + (-0.11281019196080977 + m.x3)**2) + m.x11 * ((-0.6572434123370411 + m.x1)
    **2 + (-0.028686684662413975 + m.x2)**2 + (-0.21972683506401014 + m.x3)**2)
    + m.x12 * ((-0.127643596386943 + m.x1)**2 + (-0.9780839015080076 + m.x2)**
    2 + (-0.6789719531413262 + m.x3)**2) + m.x13 * ((-0.5540038948947633 + m.x1)
    **2 + (-0.8624454838398994 + m.x2)**2 + (-0.9524036106448436 + m.x3)**2) +
    m.x14 * ((-0.37720583266913 + m.x1)**2 + (-0.8618124311714971 + m.x2)**2 +
    (-0.29002233248294207 + m.x3)**2) + m.x15 * ((-0.7039404284305039 + m.x1)**
    2 + (-0.8283201786790717 + m.x2)**2 + (-0.3777326253456039 + m.x3)**2) +
    m.x16 * ((-0.6560536644572216 + m.x1)**2 + (-0.729727001036948 + m.x2)**2
    + (-0.08838458405256377 + m.x3)**2) + m.x17 * ((-0.7617783047329179 + m.x1)
    **2 + (-0.19589048188309466 + m.x2)**2 + (-0.28981072281628295 + m.x3)**2)
    + m.x18 * ((-0.24121039989377735 + m.x1)**2 + (-0.28453436155952083 + m.x2)
    **2 + (-0.9434460831044692 + m.x3)**2) + m.x19 * ((-0.4333806457425783 +
    m.x1)**2 + (-0.8566172364997914 + m.x2)**2 + (-0.136763096042669 + m.x3)**2)
    + m.x20 * ((-0.24803840382105502 + m.x1)**2 + (-0.011616161874795083 +
    m.x2)**2 + (-0.47319931091397893 + m.x3)**2) + m.x21 * ((
    -0.9504279575331835 + m.x1)**2 + (-0.5200711914492827 + m.x2)**2 + (
    -0.7193629032181545 + m.x3)**2) + m.x22 * ((-0.16353833890407188 + m.x1)**2
    + (-0.05958557495167083 + m.x2)**2 + (-0.22326986202397225 + m.x3)**2) +
    m.x23 * ((-0.9526705582479439 + m.x1)**2 + (-0.6972358069944582 + m.x2)**2
    + (-0.9297716478426946 + m.x3)**2) + m.x24 * ((-0.7749147132089829 + m.x1)
    **2 + (-0.2608295762771462 + m.x2)**2 + (-0.19136202225832677 + m.x3)**2)
    + m.x25 * ((-0.6126308258489344 + m.x1)**2 + (-0.14153156377331155 + m.x2)
    **2 + (-0.48407873271553115 + m.x3)**2) + m.x26 * ((-0.5380944770694055 +
    m.x1)**2 + (-0.2524988728803409 + m.x2)**2 + (-0.9711078014489327 + m.x3)**
    2) + m.x27 * ((-0.05834792296545743 + m.x1)**2 + (-0.9243622010197554 +
    m.x2)**2 + (-0.04040317506099422 + m.x3)**2) + m.x28 * ((
    -0.9679670323743044 + m.x1)**2 + (-0.41044257058991684 + m.x2)**2 + (
    -0.15159906687880753 + m.x3)**2) + m.x29 * ((-0.6246791087796342 + m.x1)**2
    + (-0.7081849669920856 + m.x2)**2 + (-0.39642427716355244 + m.x3)**2) +
    m.x30 * ((-0.4761062790806113 + m.x1)**2 + (-0.6675395455313665 + m.x2)**2
    + (-0.2735835938130131 + m.x3)**2) + m.x31 * ((-0.3124167208983669 + m.x1)
    **2 + (-0.6986990432065504 + m.x2)**2 + (-0.45586376389027905 + m.x3)**2)
    + m.x32 * ((-0.8344720543223393 + m.x1)**2 + (-0.44583765999934943 + m.x2)
    **2 + (-0.7257413816680104 + m.x3)**2) + m.x33 * ((-0.5457461316296184 +
    m.x1)**2 + (-0.2385186543401263 + m.x2)**2 + (-0.36442354290044143 + m.x3)
    **2) + m.x34 * ((-0.5582707757347464 + m.x1)**2 + (-0.472558184535959 +
    m.x2)**2 + (-0.7043576542938714 + m.x3)**2) + m.x35 * ((-0.6740000811706764
    + m.x1)**2 + (-0.6945423437561885 + m.x2)**2 + (-0.24389476778707442 +
    m.x3)**2) + m.x36 * ((-0.8670018877113359 + m.x1)**2 + (-0.9143654016237796
    + m.x2)**2 + (-0.35797829134430237 + m.x3)**2) + m.x37 * ((
    -0.9020021546232962 + m.x1)**2 + (-0.476449632867904 + m.x2)**2 + (
    -0.2716582221916658 + m.x3)**2) + m.x38 * ((-0.0624040325574049 + m.x1)**2
    + (-0.6865524881714806 + m.x2)**2 + (-0.6879270202115003 + m.x3)**2) +
    m.x39 * ((-0.6592468970263641 + m.x1)**2 + (-0.4233007067648429 + m.x2)**2
    + (-0.09625315515297961 + m.x3)**2) + m.x40 * ((-0.0033110756885673664 +
    m.x1)**2 + (-0.6186254801595492 + m.x2)**2 + (-0.6539332036083124 + m.x3)**
    2) + m.x41 * ((-0.95291094141548 + m.x1)**2 + (-0.8060321831112113 + m.x2)
    **2 + (-0.547500328154394 + m.x3)**2) + m.x42 * ((-0.9780119874588511 +
    m.x1)**2 + (-0.01351753796017141 + m.x2)**2 + (-0.936609480007647 + m.x3)**
    2) + m.x43 * ((-0.5131111870312445 + m.x1)**2 + (-0.4665794712396637 + m.x2)
    **2 + (-0.6160539403418721 + m.x3)**2) + m.x44 * ((-0.3525816336439074 +
    m.x1)**2 + (-0.5029381374680542 + m.x2)**2 + (-0.8807366886856335 + m.x3)**
    2) + m.x45 * ((-0.6908618320443003 + m.x1)**2 + (-0.9131905208356976 + m.x2)
    **2 + (-0.4926479913189895 + m.x3)**2) + m.x46 * ((-0.18433884742202378 +
    m.x1)**2 + (-0.4873682973581558 + m.x2)**2 + (-0.749484570998895 + m.x3)**2)
    + m.x47 * ((-0.3125762919615228 + m.x1)**2 + (-0.6222397688647554 + m.x2)
    **2 + (-0.6715627587036744 + m.x3)**2) + m.x48 * ((-0.36324486930263744 +
    m.x1)**2 + (-0.00040623093519098763 + m.x2)**2 + (-0.7088084667993364 +
    m.x3)**2) + m.x49 * ((-0.30082227556059726 + m.x1)**2 + (
    -0.9868664403219716 + m.x2)**2 + (-0.012333988617615366 + m.x3)**2) + m.x50
    * ((-0.7033946676583003 + m.x1)**2 + (-0.5859266168558006 + m.x2)**2 + (
    -0.8852928236346337 + m.x3)**2) + m.x51 * ((-0.8433241484582942 + m.x1)**2
    + (-0.8751474949112602 + m.x2)**2 + (-0.7262396818074062 + m.x3)**2) +
    m.x52 * ((-0.6577785624919749 + m.x1)**2 + (-0.733900506368536 + m.x2)**2
    + (-0.7334769063610582 + m.x3)**2) + m.x53 * ((-0.4805112752845886 + m.x1)
    **2 + (-0.37447306067829167 + m.x2)**2 + (-0.17031629968322715 + m.x3)**2)
    + m.x54 * ((-0.39328328132231705 + m.x1)**2 + (-0.5215694104203099 + m.x2)
    **2 + (-0.9005393401199268 + m.x3)**2) + m.x55 * ((-0.23973145003446128 +
    m.x1)**2 + (-0.8887203218731593 + m.x2)**2 + (-0.7803425321727397 + m.x3)**
    2) + m.x56 * ((-0.3515281985423654 + m.x1)**2 + (-0.6729670413554799 + m.x2)
    **2 + (-0.978288988362589 + m.x3)**2) + m.x57 * ((-0.8846437099858706 +
    m.x1)**2 + (-0.7583300256633612 + m.x2)**2 + (-0.33674173755881653 + m.x3)
    **2) + m.x58 * ((-0.38298893688588764 + m.x1)**2 + (-0.3918431156726002 +
    m.x2)**2 + (-0.2797356757190884 + m.x3)**2) + m.x59 * ((-0.4535245453427187
    + m.x1)**2 + (-0.8337072721929993 + m.x2)**2 + (-0.7342728895550575 + m.x3)
    **2) + m.x60 * ((-0.2824041943022072 + m.x1)**2 + (-0.6587896760194162 +
    m.x2)**2 + (-0.5830534712940784 + m.x3)**2) + m.x61 * ((
    -0.09800985219401437 + m.x1)**2 + (-0.2339907083955447 + m.x2)**2 + (
    -0.25662161915720494 + m.x3)**2) + m.x62 * ((-0.07959435166571271 + m.x1)**
    2 + (-0.6874282203559132 + m.x2)**2 + (-0.6359298354161641 + m.x3)**2) +
    m.x63 * ((-0.3655433067520423 + m.x1)**2 + (-0.9343454771406732 + m.x2)**2
    + (-0.4072936697549203 + m.x3)**2) + m.x64 * ((-0.19062874332389212 + m.x1)
    **2 + (-0.42788647278626657 + m.x2)**2 + (-0.4166680558652034 + m.x3)**2)
    + m.x65 * ((-0.1781300534474768 + m.x1)**2 + (-0.352053781540292 + m.x2)**
    2 + (-0.702746034679353 + m.x3)**2) + m.x66 * ((-0.6257249560984208 + m.x1)
    **2 + (-0.09367455917938883 + m.x2)**2 + (-0.6618911692740225 + m.x3)**2)
    + m.x67 * ((-0.5938680465153698 + m.x1)**2 + (-0.09732472533990155 + m.x2)
    **2 + (-0.28509928015538066 + m.x3)**2) + m.x68 * ((-0.7125750860272041 +
    m.x1)**2 + (-0.7912967302826751 + m.x2)**2 + (-0.7847254289257821 + m.x3)**
    2) + m.x69 * ((-0.3344818074449257 + m.x1)**2 + (-0.8823873773786004 + m.x2)
    **2 + (-0.5351625716907574 + m.x3)**2) + m.x70 * ((-0.6551159811994477 +
    m.x1)**2 + (-0.2918583123775025 + m.x2)**2 + (-0.3212007048693508 + m.x3)**
    2) + m.x71 * ((-0.14078636829582336 + m.x1)**2 + (-0.12998606185870876 +
    m.x2)**2 + (-0.7054769643541339 + m.x3)**2) + m.x72 * ((
    -0.08859587514068912 + m.x1)**2 + (-0.6601584623266207 + m.x2)**2 + (
    -0.4206161811688063 + m.x3)**2) + m.x73 * ((-0.31930517636660205 + m.x1)**2
    + (-0.4514174785929326 + m.x2)**2 + (-0.8514772499820538 + m.x3)**2) +
    m.x74 * ((-0.6052364604479951 + m.x1)**2 + (-0.43868499694361474 + m.x2)**2
    + (-0.5841050933906983 + m.x3)**2) + m.x75 * ((-0.575916583135485 + m.x1)
    **2 + (-0.03186717116377524 + m.x2)**2 + (-0.2261064848487997 + m.x3)**2)
    + m.x76 * ((-0.8840623171321463 + m.x1)**2 + (-0.8090489969725498 + m.x2)
    **2 + (-0.6924873363214106 + m.x3)**2) + m.x77 * ((-0.9621148698858449 +
    m.x1)**2 + (-0.6899408567144933 + m.x2)**2 + (-0.6486266468067022 + m.x3)**
    2) + m.x78 * ((-0.8701304045900912 + m.x1)**2 + (-0.17211818637195297 +
    m.x2)**2 + (-0.441372352255603 + m.x3)**2) + m.x79 * ((-0.7698508222019066
    + m.x1)**2 + (-0.17363578175272487 + m.x2)**2 + (-0.6535403916068693 +
    m.x3)**2) + m.x80 * ((-0.07322744471423337 + m.x1)**2 + (
    -0.07055421690173813 + m.x2)**2 + (-0.34474565295774595 + m.x3)**2) + m.x81
    * ((-0.709254190102859 + m.x1)**2 + (-0.7892771498223472 + m.x2)**2 + (
    -0.4475615375531624 + m.x3)**2) + m.x82 * ((-0.670972527480012 + m.x1)**2
    + (-0.389263920230306 + m.x2)**2 + (-0.33246781514615653 + m.x3)**2) +
    m.x83 * ((-0.18635071452283614 + m.x1)**2 + (-0.3970622537581726 + m.x2)**2
    + (-0.9430355508655859 + m.x3)**2) + m.x84 * ((-0.6238904839993535 + m.x1)
    **2 + (-0.44461041194974416 + m.x2)**2 + (-0.5673531027225928 + m.x3)**2)
    + m.x85 * ((-0.6074387860010573 + m.x1)**2 + (-0.7386180978380433 + m.x2)
    **2 + (-0.5172875799776308 + m.x3)**2) + m.x86 * ((-0.5408763397336747 +
    m.x1)**2 + (-0.29436845731098804 + m.x2)**2 + (-0.7478079558479567 + m.x3)
    **2) + m.x87 * ((-0.9179256646815835 + m.x1)**2 + (-0.5937582308596582 +
    m.x2)**2 + (-0.09895849861075057 + m.x3)**2) + m.x88 * ((
    -0.36857938291891956 + m.x1)**2 + (-0.655188742609439 + m.x2)**2 + (
    -0.18239638519546586 + m.x3)**2) + m.x89 * ((-0.8781853429651829 + m.x1)**2
    + (-0.12929695725203783 + m.x2)**2 + (-0.9124068586470141 + m.x3)**2) +
    m.x90 * ((-0.7435448708281817 + m.x1)**2 + (-0.581441511258356 + m.x2)**2
    + (-0.5681427153798916 + m.x3)**2) + m.x91 * ((-0.8950226597430561 + m.x1)
    **2 + (-0.48871660699011255 + m.x2)**2 + (-0.9115264083687413 + m.x3)**2)
    + m.x92 * ((-0.9841847065051238 + m.x1)**2 + (-0.11577373400883828 + m.x2)
    **2 + (-0.9168095663909405 + m.x3)**2) + m.x93 * ((-0.5173280264892035 +
    m.x1)**2 + (-0.8474472655753541 + m.x2)**2 + (-0.1479724141053712 + m.x3)**
    2) + m.x94 * ((-0.8192704453802047 + m.x1)**2 + (-0.4843230048107051 + m.x2)
    **2 + (-0.6989049555761258 + m.x3)**2) + m.x95 * ((-0.38954056989863817 +
    m.x1)**2 + (-0.1014681312459782 + m.x2)**2 + (-0.5695186589492872 + m.x3)**
    2) + m.x96 * ((-0.9203830535790151 + m.x1)**2 + (-0.37143657805044983 +
    m.x2)**2 + (-0.3336008812340767 + m.x3)**2) + m.x97 * ((-0.7151860028463686
    + m.x1)**2 + (-0.44958455329276004 + m.x2)**2 + (-0.015289785091268548 +
    m.x3)**2) + m.x98 * ((-0.40117021851702483 + m.x1)**2 + (
    -0.20274012242342498 + m.x2)**2 + (-0.8545445793021874 + m.x3)**2) + m.x99
    * ((-0.6843481551992638 + m.x1)**2 + (-0.6275588309916778 + m.x2)**2 + (
    -0.4646481704316633 + m.x3)**2) + m.x100 * ((-0.2777450134931361 + m.x1)**2
    + (-0.4295228063187164 + m.x2)**2 + (-0.7739176685713476 + m.x3)**2) +
    m.x101 * ((-0.3374935672671041 + m.x1)**2 + (-0.6828954856635968 + m.x2)**2
    + (-0.22961086111555495 + m.x3)**2) + m.x102 * ((-0.30924080100103957 +
    m.x1)**2 + (-0.9827636589431684 + m.x2)**2 + (-0.2844372968701466 + m.x3)**
    2) + m.x103 * ((-0.2971879449009758 + m.x1)**2 + (-0.5076101179452838 +
    m.x2)**2 + (-0.79288378406635 + m.x3)**2) + m.x104 * ((-0.9332436569052492
    + m.x1)**2 + (-0.26797541706906003 + m.x2)**2 + (-0.9789858113206915 +
    m.x3)**2) + m.x105 * ((-0.4991302523555452 + m.x1)**2 + (
    -0.19459015863883955 + m.x2)**2 + (-0.045846983593063384 + m.x3)**2) +
    m.x106 * ((-0.1537331658793577 + m.x1)**2 + (-0.3481334566805142 + m.x2)**2
    + (-0.3823379270290115 + m.x3)**2) + m.x107 * ((-0.9652039971760678 + m.x4)
    **2 + (-0.539018346877163 + m.x5)**2 + (-0.5534528300690774 + m.x6)**2) +
    m.x108 * ((-0.47484990909204716 + m.x4)**2 + (-0.1890132636768882 + m.x5)**
    2 + (-0.03754044605849893 + m.x6)**2) + m.x109 * ((-0.39771542845577124 +
    m.x4)**2 + (-0.5036966948704162 + m.x5)**2 + (-0.7751554429159132 + m.x6)**
    2) + m.x110 * ((-0.3395623845814887 + m.x4)**2 + (-0.9699104997674314 +
    m.x5)**2 + (-0.11281019196080977 + m.x6)**2) + m.x111 * ((
    -0.6572434123370411 + m.x4)**2 + (-0.028686684662413975 + m.x5)**2 + (
    -0.21972683506401014 + m.x6)**2) + m.x112 * ((-0.127643596386943 + m.x4)**2
    + (-0.9780839015080076 + m.x5)**2 + (-0.6789719531413262 + m.x6)**2) +
    m.x113 * ((-0.5540038948947633 + m.x4)**2 + (-0.8624454838398994 + m.x5)**2
    + (-0.9524036106448436 + m.x6)**2) + m.x114 * ((-0.37720583266913 + m.x4)
    **2 + (-0.8618124311714971 + m.x5)**2 + (-0.29002233248294207 + m.x6)**2)
    + m.x115 * ((-0.7039404284305039 + m.x4)**2 + (-0.8283201786790717 + m.x5)
    **2 + (-0.3777326253456039 + m.x6)**2) + m.x116 * ((-0.6560536644572216 +
    m.x4)**2 + (-0.729727001036948 + m.x5)**2 + (-0.08838458405256377 + m.x6)**
    2) + m.x117 * ((-0.7617783047329179 + m.x4)**2 + (-0.19589048188309466 +
    m.x5)**2 + (-0.28981072281628295 + m.x6)**2) + m.x118 * ((
    -0.24121039989377735 + m.x4)**2 + (-0.28453436155952083 + m.x5)**2 + (
    -0.9434460831044692 + m.x6)**2) + m.x119 * ((-0.4333806457425783 + m.x4)**2
    + (-0.8566172364997914 + m.x5)**2 + (-0.136763096042669 + m.x6)**2) +
    m.x120 * ((-0.24803840382105502 + m.x4)**2 + (-0.011616161874795083 + m.x5)
    **2 + (-0.47319931091397893 + m.x6)**2) + m.x121 * ((-0.9504279575331835 +
    m.x4)**2 + (-0.5200711914492827 + m.x5)**2 + (-0.7193629032181545 + m.x6)**
    2) + m.x122 * ((-0.16353833890407188 + m.x4)**2 + (-0.05958557495167083 +
    m.x5)**2 + (-0.22326986202397225 + m.x6)**2) + m.x123 * ((
    -0.9526705582479439 + m.x4)**2 + (-0.6972358069944582 + m.x5)**2 + (
    -0.9297716478426946 + m.x6)**2) + m.x124 * ((-0.7749147132089829 + m.x4)**2
    + (-0.2608295762771462 + m.x5)**2 + (-0.19136202225832677 + m.x6)**2) +
    m.x125 * ((-0.6126308258489344 + m.x4)**2 + (-0.14153156377331155 + m.x5)**
    2 + (-0.48407873271553115 + m.x6)**2) + m.x126 * ((-0.5380944770694055 +
    m.x4)**2 + (-0.2524988728803409 + m.x5)**2 + (-0.9711078014489327 + m.x6)**
    2) + m.x127 * ((-0.05834792296545743 + m.x4)**2 + (-0.9243622010197554 +
    m.x5)**2 + (-0.04040317506099422 + m.x6)**2) + m.x128 * ((
    -0.9679670323743044 + m.x4)**2 + (-0.41044257058991684 + m.x5)**2 + (
    -0.15159906687880753 + m.x6)**2) + m.x129 * ((-0.6246791087796342 + m.x4)**
    2 + (-0.7081849669920856 + m.x5)**2 + (-0.39642427716355244 + m.x6)**2) +
    m.x130 * ((-0.4761062790806113 + m.x4)**2 + (-0.6675395455313665 + m.x5)**2
    + (-0.2735835938130131 + m.x6)**2) + m.x131 * ((-0.3124167208983669 + m.x4)
    **2 + (-0.6986990432065504 + m.x5)**2 + (-0.45586376389027905 + m.x6)**2)
    + m.x132 * ((-0.8344720543223393 + m.x4)**2 + (-0.44583765999934943 + m.x5)
    **2 + (-0.7257413816680104 + m.x6)**2) + m.x133 * ((-0.5457461316296184 +
    m.x4)**2 + (-0.2385186543401263 + m.x5)**2 + (-0.36442354290044143 + m.x6)
    **2) + m.x134 * ((-0.5582707757347464 + m.x4)**2 + (-0.472558184535959 +
    m.x5)**2 + (-0.7043576542938714 + m.x6)**2) + m.x135 * ((
    -0.6740000811706764 + m.x4)**2 + (-0.6945423437561885 + m.x5)**2 + (
    -0.24389476778707442 + m.x6)**2) + m.x136 * ((-0.8670018877113359 + m.x4)**
    2 + (-0.9143654016237796 + m.x5)**2 + (-0.35797829134430237 + m.x6)**2) +
    m.x137 * ((-0.9020021546232962 + m.x4)**2 + (-0.476449632867904 + m.x5)**2
    + (-0.2716582221916658 + m.x6)**2) + m.x138 * ((-0.0624040325574049 + m.x4)
    **2 + (-0.6865524881714806 + m.x5)**2 + (-0.6879270202115003 + m.x6)**2) +
    m.x139 * ((-0.6592468970263641 + m.x4)**2 + (-0.4233007067648429 + m.x5)**2
    + (-0.09625315515297961 + m.x6)**2) + m.x140 * ((-0.0033110756885673664 +
    m.x4)**2 + (-0.6186254801595492 + m.x5)**2 + (-0.6539332036083124 + m.x6)**
    2) + m.x141 * ((-0.95291094141548 + m.x4)**2 + (-0.8060321831112113 + m.x5)
    **2 + (-0.547500328154394 + m.x6)**2) + m.x142 * ((-0.9780119874588511 +
    m.x4)**2 + (-0.01351753796017141 + m.x5)**2 + (-0.936609480007647 + m.x6)**
    2) + m.x143 * ((-0.5131111870312445 + m.x4)**2 + (-0.4665794712396637 +
    m.x5)**2 + (-0.6160539403418721 + m.x6)**2) + m.x144 * ((
    -0.3525816336439074 + m.x4)**2 + (-0.5029381374680542 + m.x5)**2 + (
    -0.8807366886856335 + m.x6)**2) + m.x145 * ((-0.6908618320443003 + m.x4)**2
    + (-0.9131905208356976 + m.x5)**2 + (-0.4926479913189895 + m.x6)**2) +
    m.x146 * ((-0.18433884742202378 + m.x4)**2 + (-0.4873682973581558 + m.x5)**
    2 + (-0.749484570998895 + m.x6)**2) + m.x147 * ((-0.3125762919615228 + m.x4)
    **2 + (-0.6222397688647554 + m.x5)**2 + (-0.6715627587036744 + m.x6)**2) +
    m.x148 * ((-0.36324486930263744 + m.x4)**2 + (-0.00040623093519098763 +
    m.x5)**2 + (-0.7088084667993364 + m.x6)**2) + m.x149 * ((
    -0.30082227556059726 + m.x4)**2 + (-0.9868664403219716 + m.x5)**2 + (
    -0.012333988617615366 + m.x6)**2) + m.x150 * ((-0.7033946676583003 + m.x4)
    **2 + (-0.5859266168558006 + m.x5)**2 + (-0.8852928236346337 + m.x6)**2) +
    m.x151 * ((-0.8433241484582942 + m.x4)**2 + (-0.8751474949112602 + m.x5)**2
    + (-0.7262396818074062 + m.x6)**2) + m.x152 * ((-0.6577785624919749 + m.x4)
    **2 + (-0.733900506368536 + m.x5)**2 + (-0.7334769063610582 + m.x6)**2) +
    m.x153 * ((-0.4805112752845886 + m.x4)**2 + (-0.37447306067829167 + m.x5)**
    2 + (-0.17031629968322715 + m.x6)**2) + m.x154 * ((-0.39328328132231705 +
    m.x4)**2 + (-0.5215694104203099 + m.x5)**2 + (-0.9005393401199268 + m.x6)**
    2) + m.x155 * ((-0.23973145003446128 + m.x4)**2 + (-0.8887203218731593 +
    m.x5)**2 + (-0.7803425321727397 + m.x6)**2) + m.x156 * ((
    -0.3515281985423654 + m.x4)**2 + (-0.6729670413554799 + m.x5)**2 + (
    -0.978288988362589 + m.x6)**2) + m.x157 * ((-0.8846437099858706 + m.x4)**2
    + (-0.7583300256633612 + m.x5)**2 + (-0.33674173755881653 + m.x6)**2) +
    m.x158 * ((-0.38298893688588764 + m.x4)**2 + (-0.3918431156726002 + m.x5)**
    2 + (-0.2797356757190884 + m.x6)**2) + m.x159 * ((-0.4535245453427187 +
    m.x4)**2 + (-0.8337072721929993 + m.x5)**2 + (-0.7342728895550575 + m.x6)**
    2) + m.x160 * ((-0.2824041943022072 + m.x4)**2 + (-0.6587896760194162 +
    m.x5)**2 + (-0.5830534712940784 + m.x6)**2) + m.x161 * ((
    -0.09800985219401437 + m.x4)**2 + (-0.2339907083955447 + m.x5)**2 + (
    -0.25662161915720494 + m.x6)**2) + m.x162 * ((-0.07959435166571271 + m.x4)
    **2 + (-0.6874282203559132 + m.x5)**2 + (-0.6359298354161641 + m.x6)**2) +
    m.x163 * ((-0.3655433067520423 + m.x4)**2 + (-0.9343454771406732 + m.x5)**2
    + (-0.4072936697549203 + m.x6)**2) + m.x164 * ((-0.19062874332389212 +
    m.x4)**2 + (-0.42788647278626657 + m.x5)**2 + (-0.4166680558652034 + m.x6)
    **2) + m.x165 * ((-0.1781300534474768 + m.x4)**2 + (-0.352053781540292 +
    m.x5)**2 + (-0.702746034679353 + m.x6)**2) + m.x166 * ((-0.6257249560984208
    + m.x4)**2 + (-0.09367455917938883 + m.x5)**2 + (-0.6618911692740225 +
    m.x6)**2) + m.x167 * ((-0.5938680465153698 + m.x4)**2 + (
    -0.09732472533990155 + m.x5)**2 + (-0.28509928015538066 + m.x6)**2) +
    m.x168 * ((-0.7125750860272041 + m.x4)**2 + (-0.7912967302826751 + m.x5)**2
    + (-0.7847254289257821 + m.x6)**2) + m.x169 * ((-0.3344818074449257 + m.x4)
    **2 + (-0.8823873773786004 + m.x5)**2 + (-0.5351625716907574 + m.x6)**2) +
    m.x170 * ((-0.6551159811994477 + m.x4)**2 + (-0.2918583123775025 + m.x5)**2
    + (-0.3212007048693508 + m.x6)**2) + m.x171 * ((-0.14078636829582336 +
    m.x4)**2 + (-0.12998606185870876 + m.x5)**2 + (-0.7054769643541339 + m.x6)
    **2) + m.x172 * ((-0.08859587514068912 + m.x4)**2 + (-0.6601584623266207 +
    m.x5)**2 + (-0.4206161811688063 + m.x6)**2) + m.x173 * ((
    -0.31930517636660205 + m.x4)**2 + (-0.4514174785929326 + m.x5)**2 + (
    -0.8514772499820538 + m.x6)**2) + m.x174 * ((-0.6052364604479951 + m.x4)**2
    + (-0.43868499694361474 + m.x5)**2 + (-0.5841050933906983 + m.x6)**2) +
    m.x175 * ((-0.575916583135485 + m.x4)**2 + (-0.03186717116377524 + m.x5)**2
    + (-0.2261064848487997 + m.x6)**2) + m.x176 * ((-0.8840623171321463 + m.x4)
    **2 + (-0.8090489969725498 + m.x5)**2 + (-0.6924873363214106 + m.x6)**2) +
    m.x177 * ((-0.9621148698858449 + m.x4)**2 + (-0.6899408567144933 + m.x5)**2
    + (-0.6486266468067022 + m.x6)**2) + m.x178 * ((-0.8701304045900912 + m.x4)
    **2 + (-0.17211818637195297 + m.x5)**2 + (-0.441372352255603 + m.x6)**2) +
    m.x179 * ((-0.7698508222019066 + m.x4)**2 + (-0.17363578175272487 + m.x5)**
    2 + (-0.6535403916068693 + m.x6)**2) + m.x180 * ((-0.07322744471423337 +
    m.x4)**2 + (-0.07055421690173813 + m.x5)**2 + (-0.34474565295774595 + m.x6)
    **2) + m.x181 * ((-0.709254190102859 + m.x4)**2 + (-0.7892771498223472 +
    m.x5)**2 + (-0.4475615375531624 + m.x6)**2) + m.x182 * ((-0.670972527480012
    + m.x4)**2 + (-0.389263920230306 + m.x5)**2 + (-0.33246781514615653 + m.x6)
    **2) + m.x183 * ((-0.18635071452283614 + m.x4)**2 + (-0.3970622537581726 +
    m.x5)**2 + (-0.9430355508655859 + m.x6)**2) + m.x184 * ((
    -0.6238904839993535 + m.x4)**2 + (-0.44461041194974416 + m.x5)**2 + (
    -0.5673531027225928 + m.x6)**2) + m.x185 * ((-0.6074387860010573 + m.x4)**2
    + (-0.7386180978380433 + m.x5)**2 + (-0.5172875799776308 + m.x6)**2) +
    m.x186 * ((-0.5408763397336747 + m.x4)**2 + (-0.29436845731098804 + m.x5)**
    2 + (-0.7478079558479567 + m.x6)**2) + m.x187 * ((-0.9179256646815835 +
    m.x4)**2 + (-0.5937582308596582 + m.x5)**2 + (-0.09895849861075057 + m.x6)
    **2) + m.x188 * ((-0.36857938291891956 + m.x4)**2 + (-0.655188742609439 +
    m.x5)**2 + (-0.18239638519546586 + m.x6)**2) + m.x189 * ((
    -0.8781853429651829 + m.x4)**2 + (-0.12929695725203783 + m.x5)**2 + (
    -0.9124068586470141 + m.x6)**2) + m.x190 * ((-0.7435448708281817 + m.x4)**2
    + (-0.581441511258356 + m.x5)**2 + (-0.5681427153798916 + m.x6)**2) +
    m.x191 * ((-0.8950226597430561 + m.x4)**2 + (-0.48871660699011255 + m.x5)**
    2 + (-0.9115264083687413 + m.x6)**2) + m.x192 * ((-0.9841847065051238 +
    m.x4)**2 + (-0.11577373400883828 + m.x5)**2 + (-0.9168095663909405 + m.x6)
    **2) + m.x193 * ((-0.5173280264892035 + m.x4)**2 + (-0.8474472655753541 +
    m.x5)**2 + (-0.1479724141053712 + m.x6)**2) + m.x194 * ((
    -0.8192704453802047 + m.x4)**2 + (-0.4843230048107051 + m.x5)**2 + (
    -0.6989049555761258 + m.x6)**2) + m.x195 * ((-0.38954056989863817 + m.x4)**
    2 + (-0.1014681312459782 + m.x5)**2 + (-0.5695186589492872 + m.x6)**2) +
    m.x196 * ((-0.9203830535790151 + m.x4)**2 + (-0.37143657805044983 + m.x5)**
    2 + (-0.3336008812340767 + m.x6)**2) + m.x197 * ((-0.7151860028463686 +
    m.x4)**2 + (-0.44958455329276004 + m.x5)**2 + (-0.015289785091268548 + m.x6)
    **2) + m.x198 * ((-0.40117021851702483 + m.x4)**2 + (-0.20274012242342498
    + m.x5)**2 + (-0.8545445793021874 + m.x6)**2) + m.x199 * ((
    -0.6843481551992638 + m.x4)**2 + (-0.6275588309916778 + m.x5)**2 + (
    -0.4646481704316633 + m.x6)**2) + m.x200 * ((-0.2777450134931361 + m.x4)**2
    + (-0.4295228063187164 + m.x5)**2 + (-0.7739176685713476 + m.x6)**2) +
    m.x201 * ((-0.3374935672671041 + m.x4)**2 + (-0.6828954856635968 + m.x5)**2
    + (-0.22961086111555495 + m.x6)**2) + m.x202 * ((-0.30924080100103957 +
    m.x4)**2 + (-0.9827636589431684 + m.x5)**2 + (-0.2844372968701466 + m.x6)**
    2) + m.x203 * ((-0.2971879449009758 + m.x4)**2 + (-0.5076101179452838 +
    m.x5)**2 + (-0.79288378406635 + m.x6)**2) + m.x204 * ((-0.9332436569052492
    + m.x4)**2 + (-0.26797541706906003 + m.x5)**2 + (-0.9789858113206915 +
    m.x6)**2) + m.x205 * ((-0.4991302523555452 + m.x4)**2 + (
    -0.19459015863883955 + m.x5)**2 + (-0.045846983593063384 + m.x6)**2) +
    m.x206 * ((-0.1537331658793577 + m.x4)**2 + (-0.3481334566805142 + m.x5)**2
    + (-0.3823379270290115 + m.x6)**2))

m.e1 = Constraint(expr= m.x7 + m.x107 == 1)
m.e2 = Constraint(expr= m.x8 + m.x108 == 1)
m.e3 = Constraint(expr= m.x9 + m.x109 == 1)
m.e4 = Constraint(expr= m.x10 + m.x110 == 1)
m.e5 = Constraint(expr= m.x11 + m.x111 == 1)
m.e6 = Constraint(expr= m.x12 + m.x112 == 1)
m.e7 = Constraint(expr= m.x13 + m.x113 == 1)
m.e8 = Constraint(expr= m.x14 + m.x114 == 1)
m.e9 = Constraint(expr= m.x15 + m.x115 == 1)
m.e10 = Constraint(expr= m.x16 + m.x116 == 1)
m.e11 = Constraint(expr= m.x17 + m.x117 == 1)
m.e12 = Constraint(expr= m.x18 + m.x118 == 1)
m.e13 = Constraint(expr= m.x19 + m.x119 == 1)
m.e14 = Constraint(expr= m.x20 + m.x120 == 1)
m.e15 = Constraint(expr= m.x21 + m.x121 == 1)
m.e16 = Constraint(expr= m.x22 + m.x122 == 1)
m.e17 = Constraint(expr= m.x23 + m.x123 == 1)
m.e18 = Constraint(expr= m.x24 + m.x124 == 1)
m.e19 = Constraint(expr= m.x25 + m.x125 == 1)
m.e20 = Constraint(expr= m.x26 + m.x126 == 1)
m.e21 = Constraint(expr= m.x27 + m.x127 == 1)
m.e22 = Constraint(expr= m.x28 + m.x128 == 1)
m.e23 = Constraint(expr= m.x29 + m.x129 == 1)
m.e24 = Constraint(expr= m.x30 + m.x130 == 1)
m.e25 = Constraint(expr= m.x31 + m.x131 == 1)
m.e26 = Constraint(expr= m.x32 + m.x132 == 1)
m.e27 = Constraint(expr= m.x33 + m.x133 == 1)
m.e28 = Constraint(expr= m.x34 + m.x134 == 1)
m.e29 = Constraint(expr= m.x35 + m.x135 == 1)
m.e30 = Constraint(expr= m.x36 + m.x136 == 1)
m.e31 = Constraint(expr= m.x37 + m.x137 == 1)
m.e32 = Constraint(expr= m.x38 + m.x138 == 1)
m.e33 = Constraint(expr= m.x39 + m.x139 == 1)
m.e34 = Constraint(expr= m.x40 + m.x140 == 1)
m.e35 = Constraint(expr= m.x41 + m.x141 == 1)
m.e36 = Constraint(expr= m.x42 + m.x142 == 1)
m.e37 = Constraint(expr= m.x43 + m.x143 == 1)
m.e38 = Constraint(expr= m.x44 + m.x144 == 1)
m.e39 = Constraint(expr= m.x45 + m.x145 == 1)
m.e40 = Constraint(expr= m.x46 + m.x146 == 1)
m.e41 = Constraint(expr= m.x47 + m.x147 == 1)
m.e42 = Constraint(expr= m.x48 + m.x148 == 1)
m.e43 = Constraint(expr= m.x49 + m.x149 == 1)
m.e44 = Constraint(expr= m.x50 + m.x150 == 1)
m.e45 = Constraint(expr= m.x51 + m.x151 == 1)
m.e46 = Constraint(expr= m.x52 + m.x152 == 1)
m.e47 = Constraint(expr= m.x53 + m.x153 == 1)
m.e48 = Constraint(expr= m.x54 + m.x154 == 1)
m.e49 = Constraint(expr= m.x55 + m.x155 == 1)
m.e50 = Constraint(expr= m.x56 + m.x156 == 1)
m.e51 = Constraint(expr= m.x57 + m.x157 == 1)
m.e52 = Constraint(expr= m.x58 + m.x158 == 1)
m.e53 = Constraint(expr= m.x59 + m.x159 == 1)
m.e54 = Constraint(expr= m.x60 + m.x160 == 1)
m.e55 = Constraint(expr= m.x61 + m.x161 == 1)
m.e56 = Constraint(expr= m.x62 + m.x162 == 1)
m.e57 = Constraint(expr= m.x63 + m.x163 == 1)
m.e58 = Constraint(expr= m.x64 + m.x164 == 1)
m.e59 = Constraint(expr= m.x65 + m.x165 == 1)
m.e60 = Constraint(expr= m.x66 + m.x166 == 1)
m.e61 = Constraint(expr= m.x67 + m.x167 == 1)
m.e62 = Constraint(expr= m.x68 + m.x168 == 1)
m.e63 = Constraint(expr= m.x69 + m.x169 == 1)
m.e64 = Constraint(expr= m.x70 + m.x170 == 1)
m.e65 = Constraint(expr= m.x71 + m.x171 == 1)
m.e66 = Constraint(expr= m.x72 + m.x172 == 1)
m.e67 = Constraint(expr= m.x73 + m.x173 == 1)
m.e68 = Constraint(expr= m.x74 + m.x174 == 1)
m.e69 = Constraint(expr= m.x75 + m.x175 == 1)
m.e70 = Constraint(expr= m.x76 + m.x176 == 1)
m.e71 = Constraint(expr= m.x77 + m.x177 == 1)
m.e72 = Constraint(expr= m.x78 + m.x178 == 1)
m.e73 = Constraint(expr= m.x79 + m.x179 == 1)
m.e74 = Constraint(expr= m.x80 + m.x180 == 1)
m.e75 = Constraint(expr= m.x81 + m.x181 == 1)
m.e76 = Constraint(expr= m.x82 + m.x182 == 1)
m.e77 = Constraint(expr= m.x83 + m.x183 == 1)
m.e78 = Constraint(expr= m.x84 + m.x184 == 1)
m.e79 = Constraint(expr= m.x85 + m.x185 == 1)
m.e80 = Constraint(expr= m.x86 + m.x186 == 1)
m.e81 = Constraint(expr= m.x87 + m.x187 == 1)
m.e82 = Constraint(expr= m.x88 + m.x188 == 1)
m.e83 = Constraint(expr= m.x89 + m.x189 == 1)
m.e84 = Constraint(expr= m.x90 + m.x190 == 1)
m.e85 = Constraint(expr= m.x91 + m.x191 == 1)
m.e86 = Constraint(expr= m.x92 + m.x192 == 1)
m.e87 = Constraint(expr= m.x93 + m.x193 == 1)
m.e88 = Constraint(expr= m.x94 + m.x194 == 1)
m.e89 = Constraint(expr= m.x95 + m.x195 == 1)
m.e90 = Constraint(expr= m.x96 + m.x196 == 1)
m.e91 = Constraint(expr= m.x97 + m.x197 == 1)
m.e92 = Constraint(expr= m.x98 + m.x198 == 1)
m.e93 = Constraint(expr= m.x99 + m.x199 == 1)
m.e94 = Constraint(expr= m.x100 + m.x200 == 1)
m.e95 = Constraint(expr= m.x101 + m.x201 == 1)
m.e96 = Constraint(expr= m.x102 + m.x202 == 1)
m.e97 = Constraint(expr= m.x103 + m.x203 == 1)
m.e98 = Constraint(expr= m.x104 + m.x204 == 1)
m.e99 = Constraint(expr= m.x105 + m.x205 == 1)
m.e100 = Constraint(expr= m.x106 + m.x206 == 1)
