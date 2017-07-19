from imports import *

components = OrderedDict()

components.update([
    ("in1", {
        "type": Point,
        "kwargs": {
            "x": -2.1,
            "y": -1.85,
        },
    }),
])

components["in2"] = deepcopy(components["in1"])
components["in2"]["kwargs"]["y"] *= -1

components.update([
    ("vtx0", {
        "type": Circle,
        "kwargs": {
            "x": 0,
            "y": 0,
            "radius": 0.5,
            "fill": [HATCHED135n]+mystyle,
            "stroke": [BLACK]+mystyle,
        },
    }),
    ("P1a", {
        "type": MultiLine,
        "point1": "in1",
        "point2": "vtx0",
        "kwargs": {
            "n": 2,
            "dist": 0.1,
            "styles": mystyle,
        },
        "label": {
            "name": proton,
            "kwargs": {
                "displace": +.45,
                "pos": 0.4,
                "size": labelsize,
            },
        },
    }),
])

components["P2a"] = deepcopy(components["P1a"])
components["P2a"]["point1"] = "in2"
components["P2a"]["label"]["kwargs"]["displace"] *= -1
