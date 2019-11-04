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
    ("out1", {
        "type": Point,
        "kwargs": {
            "x": 2.1*2,
            "y": -1.85,
        },
    }),
])

components["in2"] = deepcopy(components["in1"])
components["in2"]["kwargs"]["y"] *= -1
components["out2"] = deepcopy(components["out1"])
components["out2"]["kwargs"]["y"] *= -1

components.update([
    ("vtx0", {
        "type": Vertex,
        "kwargs": {
            "x": 0,
            "y": 0,
            "mark": CIRCLE,
        },
        "label": {
            "name": r"$g_{\text{q}}$",
            "kwargs": {
                "displace": -0.55,
                "size": labelsize,
            },
        }
    }),
    ("q1a", {
        "type": Fermion,
        "point1": "in1",
        "point2": "vtx0",
        "kwargs": {
            "n": 2,
            "dist": 0.1,
            "styles": mystyle,
        },
        "label": {
            "name": qbar,
            "kwargs": {
                "displace": +.45,
                "pos": 0.5,
                "size": labelsize,
            },
        },
    }),
    ("vtx1", {
        "type": Vertex,
        "kwargs": {
            "x": 2.1,
            "y": 0,
            "mark": CIRCLE,
        },
        "label": {
            "name": r"$g_{\chi}$",
            "kwargs": {
                "displace": 0.55,
                "size": labelsize,
            },
        }
    }),
    ("Z1", {
        "type": Vector,
        "point1": "vtx0",
        "point2": "vtx1",
        "kwargs": {
            "frequency": 0.60,
            "amplitude": 0.09,
            "styles": mystyle,
            "invert": True,
        },
        "label": {
            "name": r"$\text{Z}^{\prime}$",
            "kwargs": {
                "pos": 0.5,
                "displace": +.35,
                "size": labelsize,
            },
        },
    }),
    ("q1b", {
        "type": Fermion,
        "point1": "vtx1",
        "point2": "out1",
        "kwargs": {
            "n": 2,
            "dist": 0.1,
            "styles": mystyle,
        },
        "label": {
            "name": r"$\bar{\chi}$",
            "kwargs": {
                "displace": +.45,
                "pos": 0.5,
                "size": labelsize,
            },
        },
    }),
])

components["q2a"] = deepcopy(components["q1a"])
components["q2a"]["point1"] = "in2"
components["q2a"]["label"]["kwargs"]["displace"] *= -1
components["q2a"]["label"]["name"] = qua

components["q2b"] = deepcopy(components["q1b"])
components["q2b"]["point2"] = "out2"
components["q2b"]["label"]["kwargs"]["displace"] *= -1
components["q2b"]["label"]["name"] = r"$\chi$"
