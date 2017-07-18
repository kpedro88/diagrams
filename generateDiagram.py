import os, sys
from pyfeyn.user import *
from optparse import OptionParser

def list_callback(option, opt, value, parser):
    setattr(parser.values, option.dest, value.split(','))

def buildLabel(result,label):
    result.addLabel(label["name"],**label["kwargs"])
    
def buildPoint(results,name,component,components):
    if name in results: return
    # points require different info, will throw if required info not given
    results[name] = component["type"](**(component["kwargs"]))
    if "label" in component.keys():
        buildLabel(results[name],component["label"])
    
def buildLine(results,name,component,components):
    if name in results: return
    # lines require two points
    for p in ["point1","point2"]:
        if component[p] not in results:
            buildPoint(results,components[component[p]])
    results[name] = component["type"](results[component["point1"]],results[component["point2"]],**(component["kwargs"]))
    if "label" in component.keys():
        buildLabel(results[name],component["label"])

def buildD(components):
    results = {}
    
    # TODO: add "verbose"/"dump" option to print lines of code for constructors?
    
    # simple dependency system: lines can depend on points, points have no dependencies -> no chance of circular dependencies
    for name,component in components.iteritems():
        if issubclass(component["type"],Line):
            buildLine(results,name,component,components)
        else:
            buildPoint(results,name,component,components)

def printD(fd,output,pformat):
    # TODO: check for allowed/known formats
    for pf in pformat:
        pname = "{:s}.{:s}".format(output,pf)
        print "printing "+pname
        if pf=="png":
            os.system("convert -density 100 -transparent white {:s}.pdf {:s}.png".format(output,output))
        else:
            fd.draw(pname)

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-d", "--dict", dest="dictfile", default="", help="file containing dict w/ diagram components")
    parser.add_option("-o", "--output", dest="output", default="", help="output name for diagram images (default = [dict name]+'_feyn')")
    parser.add_option("-p", "--pformat", dest="pformat", default=["pdf","png"], type="string", action="callback", callback=list_callback, help="comma-separated list of print formats (default = %default)")
    (options, args) = parser.parse_args()
    
    if len(options.dictfile)==0:
        parser.error("Must specify a dictionary with -d")
    
    if len(options.output)==0:
        options.output = options.dictfile.split('/')[-1].replace(".py","")+"_feyn"
    
    # import dict (name must be "components")
    components = getattr(__import__(options.dictfile.replace(".py",""),fromlist="components"),"components")
    
    pyx.text.preamble(r"\usepackage{amsmath,amssymb}")
    fd = FeynDiagram()
    
    # step 1: construct diagram from dictionary
    buildD(components)
    
    # step 2: apply user-specified customization function
    # TODO
    
    # step 3: print
    printD(fd,options.output,options.pformat)
    