#!/usr/bin/python

from pyfeyn.user import *
import os, sys
from particleNames import *

#pyx.unit.set()
#pyx.unit.set(defaultunit = "cm")
pyx.text.preamble(r"\usepackage{amsmath,amssymb}")
mystyle = [THICK1]
labelsize = pyx.text.size.large
dashed3 = pyx.style.linestyle(pyx.style.linecap.butt, pyx.style.dash([3]))

fd = FeynDiagram()

in1  = Point(-2.1, -1.85)
in2  = Point(-2.1, 1.85)

HATCHED135n = pyx.pattern.hatched(0.07 * pyx.unit.v_cm,135,mystyle)
vtx0 = Circle(0,0, radius=0.5).setFillStyle(HATCHED135n)
vtx0.strokestyles.extend(mystyle)
vtx0.fillstyles.extend(mystyle)
P1a = MultiLine(in1, vtx0, n=2, dist=0.1).addLabel(proton,displace=+.45,pos=0.4,size=labelsize).setStyles(mystyle)
P2a = MultiLine(in2, vtx0, n=2, dist=0.1).addLabel(proton,displace=-.45,pos=0.4,size=labelsize).setStyles(mystyle)

vtx1 = Vertex(2.1, -0.75, mark=CIRCLE)
vtx2 = Vertex(2.1, 0.75, mark=CIRCLE)

gl1 = Gluino(vtx0, vtx1, frequency=1.2, amplitude=0.17).addLabel(gluino,pos=0.6,displace=+.35,size=labelsize).invert().setStyles(mystyle)
gl2 = Gluino(vtx0, vtx2, frequency=1.2, amplitude=0.17).addLabel(gluino,pos=0.6,displace=-.35,size=labelsize).invert().setStyles(mystyle)

out1a = Point(3.625, -1.55)
out1c = Vertex(3.4, -0.6, mark=CIRCLE)
out1d = Point(4.1, -0.90)
out1e = Point(4.1, -0.35)

out2a = Point(3.625, 1.55)
out2c = Vertex(3.4, 0.6, mark=CIRCLE)
out2d = Point(4.1, 0.90)
out2e = Point(4.1, 0.35)

top1a = Fermion(vtx1,out1a).addLabel(tbar,displace=0,pos=1.1,size=labelsize,valign=MIDDLE,halign=LEFT).setStyles(mystyle)
st1c = Scalar(vtx1,out1c, linestyle=dashed3).addLabel(stop,pos=0.5,displace=-.40,size=labelsize,valign=MIDDLE).setStyles(mystyle)
cha1d = Fermion(out1c,out1d).addLabel(cha,displace=0.0,pos=1.25,size=labelsize,valign=MIDDLE,halign=LEFT).setStyles(mystyle)
part1e = Gaugino(out1c,out1e, frequency=0.60, amplitude=0.09).addLabel(chi10,displace=0.0,pos=1.30,size=labelsize,valign=MIDDLE,halign=LEFT).setStyles(mystyle)

top2a = Fermion(vtx2,out2a).addLabel(top,displace=0,pos=1.2,size=labelsize,valign=MIDDLE,halign=LEFT).setStyles(mystyle)
st2c = Scalar(vtx2,out2c, linestyle=dashed3).addLabel(stbar,pos=0.475,displace=0.15,size=labelsize,valign=MIDDLE).setStyles(mystyle)
cha2d = Fermion(out2c,out2d).addLabel(cbar,displace=0.0,pos=1.30,size=labelsize,valign=MIDDLE,halign=LEFT).setStyles(mystyle)
part2e = Gaugino(out2c,out2e, frequency=0.60, amplitude=0.09).addLabel(chi10,displace=0.0,pos=1.25,size=labelsize,valign=MIDDLE,halign=LEFT).invert().setStyles(mystyle)

name=sys.argv[0].replace(".py","")
if name.find("/")>-1:
  name=name[name.find("/")+1:]

fd.draw("%s_feyn.pdf" % name )
os.system ( "convert -density 100 -transparent white %s_feyn.pdf %s_feyn.png" % ( name, name ))