#!/usr/bin/python

from pyfeyn.user import *
import os, sys
from particleNames import *

#pyx.unit.set()
#pyx.unit.set(defaultunit = "cm")
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
P1a = MultiLine(in1, vtx0, n=2, dist=0.1).addLabel("$P_1$",displace=+.45,pos=0.4,size=labelsize).setStyles(mystyle)
P2a = MultiLine(in2, vtx0, n=2, dist=0.1).addLabel("$P_2$",displace=-.45,pos=0.4,size=labelsize).setStyles(mystyle)

vtx1 = Vertex(2.1, -0.75, mark=CIRCLE)
vtx2 = Vertex(2.1, 0.75, mark=CIRCLE)

gl1 = Gluino(vtx0, vtx1, frequency=1.2, amplitude=0.17).addLabel(gluino,pos=0.6,displace=+.35,size=labelsize).invert().setStyles(mystyle)
gl2 = Gluino(vtx0, vtx2, frequency=1.2, amplitude=0.17).addLabel(gluino,pos=0.6,displace=-.35,size=labelsize).invert().setStyles(mystyle)

out1a = Point(3.45, -1.75)
out1b = Point(3.8, -1.35)
out1c = Vertex(3.4, -0.6, mark=CIRCLE)
out1d = Point(4.0, -0.85)
out1e = Point(4.1, -0.35)

out2a = Point(3.45, 1.75)
out2b = Point(3.8, 1.35)
out2c = Vertex(3.4, 0.6, mark=CIRCLE)
out2d = Point(4.0, 0.85)
out2e = Point(4.1, 0.35)

top1a = Fermion(vtx1,out1a).addLabel(qbar,displace=0,pos=1.1,size=labelsize,valign=MIDDLE,halign=LEFT).setStyles(mystyle)
top1b = Fermion(vtx1,out1b).addLabel(qua,displace=0,pos=1.1,size=labelsize,valign=MIDDLE,halign=LEFT).setStyles(mystyle)
chi1c = Scalar(vtx1,out1c,linestyle=dashed3).addLabel(chi20+','+chi1pm,pos=0.5,displace=-.35,size=labelsize,valign=MIDDLE).setStyles(mystyle)
part1d = Vector(out1c,out1d, frequency=0.45, amplitude=0.06).addLabel(Z0+','+Wpm,displace=0.0,pos=1.25,size=labelsize,valign=MIDDLE,halign=LEFT).setStyles(mystyle)
part1e = Scalar(out1c,out1e,linestyle=dashed3).addLabel(chi10,displace=0.0,pos=1.30,size=labelsize,valign=MIDDLE,halign=LEFT).setStyles(mystyle)

top2a = Fermion(vtx2,out2a).addLabel(qua,displace=0,pos=1.2,size=labelsize,valign=MIDDLE,halign=LEFT).setStyles(mystyle)
top2b = Fermion(vtx2,out2b).addLabel(qbar,displace=0,pos=1.15,size=labelsize,valign=MIDDLE,halign=LEFT).setStyles(mystyle)
chi2c = Scalar(vtx2,out2c,linestyle=dashed3).addLabel(chi20+','+chi1pm,pos=0.5,displace=0.125,size=labelsize,valign=MIDDLE).setStyles(mystyle)
part2d = Vector(out2c,out2d, frequency=0.45, amplitude=0.06).addLabel(Z0+','+Wpm,displace=0.0,pos=1.30,size=labelsize,valign=MIDDLE,halign=LEFT).setStyles(mystyle)
part2e = Scalar(out2c,out2e,linestyle=dashed3).addLabel(chi10,displace=0.0,pos=1.25,size=labelsize,valign=MIDDLE,halign=LEFT).setStyles(mystyle)

name=sys.argv[0].replace(".py","")
if name.find("/")>-1:
  name=name[name.find("/")+1:]

fd.draw("%s_feyn.pdf" % name )
os.system ( "convert -density 100 -transparent white %s_feyn.pdf %s_feyn.png" % ( name, name ))