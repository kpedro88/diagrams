from imports import *

components = getComponents("ppBlob",copy=True)

components.update([
    ("vtx1", {
        "type": Vertex,
        "kwargs": {
            "x": 2.25,
            "y": -0.65,
            "mark": CIRCLE,
        },
    }),
])

components["vtx2"] = deepcopy(components["vtx1"])
components["vtx2"]["kwargs"]["y"] *= -1

components.update([
    ("gl1", {
        "type": Gluino,
        "point1": "vtx0",
        "point2": "vtx1",
        "kwargs": {
            "frequency": 1.2,
            "amplitude": 0.17,
            "invert": True,
            "styles": mystyle,
        },
        "label": {
            "name": gluino,
            "kwargs": {
                "pos": 0.6,
                "displace": +.35,
                "size": labelsize,
            },
        },
    }),
])

components["gl2"] = deepcopy(components["gl1"])
components["gl2"]["point2"] = "vtx2"
components["gl2"]["label"]["kwargs"]["displace"] *= -1

components.update([
    ("out1a", {
        "type": Point,
        "kwargs": {
            "x": 3.4,
            "y": -1.75,
        },
    }),
    ("out1b", {
        "type": Point,
        "kwargs": {
            "x": 3.8,
            "y": -1.1,
        },
    }),
    ("out1c", {
        "type": Point,
        "kwargs": {
            "x": 3.95,
            "y": -0.4,
        },
    }),
])

components["out2a"] = deepcopy(components["out1a"])
components["out2a"]["kwargs"]["y"] *= -1
components["out2b"] = deepcopy(components["out1b"])
components["out2b"]["kwargs"]["y"] *= -1
components["out2c"] = deepcopy(components["out1c"])
components["out2c"]["kwargs"]["y"] *= -1

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
])

components["qua1b"] = deepcopy(components["qua1a"])
components["qua1b"]["point2"] = "out1b"
components["qua1b"]["label"]["name"] = qua

components.update([
    ("chi1c", {
        "type": Gaugino,
        "point1": "vtx1",
        "point2": "out1c",
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

components["qua2b"] = deepcopy(components["qua2a"])
components["qua2b"]["point2"] = "out2b"
components["qua2b"]["label"]["name"] = qbar
components["qua2b"]["label"]["kwargs"]["pos"] = 1.15

components["chi2c"] = deepcopy(components["chi1c"])
components["chi2c"]["point1"] = "vtx2"
components["chi2c"]["point2"] = "out2c"
components["chi2c"]["kwargs"]["invert"] = True
