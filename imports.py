from pyfeyn.user import *
import path
from particleNames import *
from style import *
from collections import OrderedDict
from copy import deepcopy

def getComponents(dictfile,copy=False):
    components = getattr(__import__(dictfile.replace(".py",""),fromlist="components"),"components")
    if copy: return deepcopy(components)
    else: return components
    
def simplecopy(x, memo=None):
    return x
    
# avoid "can't pickle thread.lock objects" issue
pyx.canvas.canvas.__deepcopy__ = simplecopy
