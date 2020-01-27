from imports import *

components = getComponents("tChan",copy=True)

components["q1a"]["type"] = Gluon
components["q1a"]["kwargs"] = {
    "frequency": 1.2,
    "amplitude": 0.17,
    "invert": True,
    "styles": mystyle,
}
components["q1a"]["label"]["name"] = gluon

components["q1b"]["type"] = Scalar
components["q1b"]["kwargs"] = {
    "linestyle": dashed3,
    "styles": mystyle,
}
components["q1b"]["label"]["name"] = r"$\Phi$"
components["q1b"]["label"]["kwargs"] = {
    "displace": +.45,
    "pos": 0.5,
    "size": labelsize,
}

components["vtx0"]["label"]["name"] = r"$\alpha_{s}$"

components["out1"]["type"] = Vertex
components["out1"]["kwargs"]["mark"] = CIRCLE
components["out1"]["label"] = {
    "name": r"$\lambda$",
    "kwargs": {
        "displace": 0.55,
        "angle": 90,
        "size": labelsize,
    },
}

components.update([
    ("out3", {
        "type": Point,
        "kwargs": {
            "x": 2.1*3,
            "y": -1.05,
        },
    }),
    ("out4", {
        "type": Point,
        "kwargs": {
            "x": 2.1*3,
            "y": -2.65,
        },
    }),
])

components.update([
    ("q1c",{
        "type": Fermion,
        "point1": "out1",
        "point2": "out3",
        "kwargs": {
            "n": 2,
            "dist": 0.1,
            "styles": mystyle,
        },
        "label": {
            "name": qua,
            "kwargs": {
                "displace": 0,
                "pos": 1.1,
                "size": labelsize,
                "valign": MIDDLE,
                "halign": LEFT,
            },
        },
    }),
    ("q1d",{
        "type": Fermion,
        "point1": "out1",
        "point2": "out4",
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