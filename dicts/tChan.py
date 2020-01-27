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
            "x": 1.05,
            "y": -1.05,
            "mark": CIRCLE,
        },
        "label": {
            "name": r"$\lambda$",
            "kwargs": {
                "displace": -0.55,
                "angle": 90,
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
                "displace": 0,
                "pos": -0.15,
                "size": labelsize,
                "valign": MIDDLE,
                "halign": LEFT,
            },
        },
    }),
    ("vtx1", {
        "type": Vertex,
        "kwargs": {
            "x": 1.05,
            "y": 1.05,
            "mark": CIRCLE,
        },
        "label": {
            "name": r"$\lambda$",
            "kwargs": {
                "displace": 0.55,
                "angle": 90,
                "size": labelsize,
            },
        }
    }),
    ("Phi1", {
        "type": Scalar,
        "point1": "vtx0",
        "point2": "vtx1",
        "kwargs": {
            "linestyle": dashed3,
            "styles": mystyle,
        },
        "label": {
            "name": r"$\Phi$",
            "kwargs": {
                "pos": 0.5,
                "displace": +.35,
                "size": labelsize,
            },
        },
    }),
    ("q1b", {
        "type": Fermion,
        "point1": "vtx0",
        "point2": "out1",
        "kwargs": {
            "n": 2,
            "dist": 0.1,
            "styles": mystyle,
        },
        "label": {
            "name": r"$\bar{\chi}$",
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

components["q2a"] = deepcopy(components["q1a"])
components["q2a"]["point1"] = "in2"
components["q2a"]["point2"] = "vtx1"
components["q2a"]["label"]["name"] = qua

components["q2b"] = deepcopy(components["q1b"])
components["q2b"]["point1"] = "vtx1"
components["q2b"]["point2"] = "out2"
components["q2b"]["label"]["name"] = r"$\chi$"
