from pyfeyn.paint import *

mystyle = [THICK1]
labelsize = pyx.text.size.large
dashed3 = pyx.style.linestyle(pyx.style.linecap.butt, pyx.style.dash([3]))
HATCHED135n = pyx.pattern.hatched(0.07 * pyx.unit.v_cm,135,mystyle)
