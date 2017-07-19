from imports import *

components = getComponents("ppBlob",copy=True)

components.update([
    ("vtx1", {
        "type": Vertex,
        "kwargs": {
            "x": 3.0,
            "y": -0.85,
            "mark": CIRCLE,
        },
    }),
])

components["vtx2"] = deepcopy(components["vtx1"])
components["vtx2"]["kwargs"]["y"] *= -1

components.update([
    ("sq1", {
        "type": Scalar,
        "point1": "vtx0",
        "point2": "vtx1",
        "kwargs": {
            "linestyle": dashed3,
            "styles": mystyle,
        },
        "label": {
            "name": sqbar,
            "kwargs": {
                "pos": 0.6,
                "displace": +.35,
                "size": labelsize,
            },
        },
    }),
])

components["sq2"] = deepcopy(components["sq1"])
components["sq2"]["point2"] = "vtx2"
components["sq2"]["label"]["name"] = squa
components["sq2"]["label"]["kwargs"]["displace"] *= -1

components.update([
    ("out1a", {
        "type": Point,
        "kwargs": {
            "x": 4.15,
            "y": -1.8,
        },
    }),
    ("out1b", {
        "type": Point,
        "kwargs": {
            "x": 4.65,
            "y": -0.65,
        },
    }),
])

components["out2a"] = deepcopy(components["out1a"])
components["out2a"]["kwargs"]["y"] *= -1
components["out2b"] = deepcopy(components["out1b"])
components["out2b"]["kwargs"]["y"] *= -1

components.update([
    ("qua1a", {
        "type": Fermion,
        "point1": "vtx1",
        "point2": "out1a",
        "kwargs": {
            "styles": mystyle,
        },
        "label": {
            "name": qbar,
            "kwargs": {
                "displace": 0,
                "pos": 1.1,
                "size": labelsize,
                "valign": MIDDLE,
                "halign": LEFT,
            },
        }
    }),
    ("chi1b", {
        "type": Gaugino,
        "point1": "vtx1",
        "point2": "out1b",
        "kwargs": {
            "frequency": 0.60,
            "amplitude": 0.09,
            "styles": mystyle,
        },
        "label": {
            "name": chi10,
            "kwargs": {
                "displace": 0,
                "pos": 1.15,
                "size": labelsize,
                "valign": MIDDLE,
                "halign": LEFT,
            },
        }
    }),
])

components["qua2a"] = deepcopy(components["qua1a"])
components["qua2a"]["point1"] = "vtx2"
components["qua2a"]["point2"] = "out2a"
components["qua2a"]["label"]["name"] = qua
components["qua2a"]["label"]["kwargs"]["pos"] = 1.2

components["chi2b"] = deepcopy(components["chi1b"])
components["chi2b"]["point1"] = "vtx2"
components["chi2b"]["point2"] = "out2b"
components["chi2b"]["kwargs"]["invert"] = True
