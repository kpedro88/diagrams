from imports import *

components = getComponents("zPrime",copy=True)

components["md2"] = deepcopy(components["in2"])
components["md2"]["kwargs"]["x"] /= 2
components["md2"]["kwargs"]["y"] /= 2

components["md3"] = deepcopy(components["in2"])
components["md3"]["kwargs"]["x"] = (components["vtx0"]["kwargs"]["x"]+components["vtx1"]["kwargs"]["x"])/2

components.update([
    ("gl2",{
        "type": Gluon,
        "point1": "md2",
        "point2": "md3",
        "kwargs": {
            "frequency": 1.2,
            "amplitude": 0.17,
            "invert": True,
            "styles": mystyle,
        },
        "label": {
            "name": gluon,
            "kwargs": {
                "displace": 0,
                "pos": 1.1,
                "size": labelsize,
                "valign": MIDDLE,
                "halign": LEFT,
            },
        },
    }),
])

components["out1"]["kwargs"]["y"] /= 4
components["out2"]["kwargs"]["y"] /= 4

components["vtx1"]["label"]["kwargs"]["angle"] = 90
