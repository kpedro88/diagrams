from imports import *

componentsT1tbtb = getComponents("T1tbtb",copy=True)
componentsT1bbbb = getComponents("T1bbbb",copy=True)

components = OrderedDict()

for key in componentsT1bbbb:
    if '1' in key:
        components[key] = deepcopy(componentsT1bbbb[key])

for key in componentsT1tbtb:
    if not '1' in key:
        components[key] = deepcopy(componentsT1tbtb[key])
