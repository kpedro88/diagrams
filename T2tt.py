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
P1a = MultiLine(in1, vtx0, n=2, dist=0.1).addLabel(proton,displace=+.45,pos=0.4,size=labelsize).setStyles(mystyle)
P2a = MultiLine(in2, vtx0, n=2, dist=0.1).addLabel(proton,displace=-.45,pos=0.4,size=labelsize).setStyles(mystyle)

vtx1 = Vertex(3.0, -0.85, mark=CIRCLE)
vtx2 = Vertex(3.0, 0.85, mark=CIRCLE)

st1 = Scalar(vtx0, vtx1, linestyle=dashed3).addLabel(stop,pos=0.6,displace=+.35,size=labelsize).setStyles(mystyle)
st2 = Scalar(vtx0, vtx2, linestyle=dashed3).addLabel(stop,pos=0.6,displace=-.35,size=labelsize).setStyles(mystyle)

out1a = Point(4.15, -1.8)
out1b = Point(4.65, -0.65)

out2a = Point(4.15, 1.8)
out2b = Point(4.65, 0.65)

top1a = Fermion(vtx1,out1a).addLabel(top,displace=0,pos=1.10,size=labelsize,valign=MIDDLE,halign=LEFT).setStyles(mystyle)
chi1b = Gaugino(vtx1,out1b, frequency=0.60, amplitude=0.09).addLabel(chi10,displace=0,pos=1.15,size=labelsize,valign=MIDDLE,halign=LEFT).setStyles(mystyle)

top2a = Fermion(vtx2,out2a).addLabel(top,displace=0,pos=1.20,size=labelsize,valign=MIDDLE,halign=LEFT).setStyles(mystyle)
chi2b = Gaugino(vtx2,out2b, frequency=0.60, amplitude=0.09).addLabel(chi10,displace=0,pos=1.15,size=labelsize,valign=MIDDLE,halign=LEFT).invert().setStyles(mystyle)

name=sys.argv[0].replace(".py","")
if name.find("/")>-1:
  name=name[name.find("/")+1:]

fd.draw("%s_feyn.pdf" % name )
os.system ( "convert -density 100 -transparent white %s_feyn.pdf %s_feyn.png" % ( name, name ))