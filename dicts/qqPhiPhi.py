from imports import *

components = getComponents("zPrime",copy=True)

components["Z1"]["type"] = Gluon
components["Z1"]["kwargs"] = {
    "frequency": 1.2,
    "amplitude": 0.17,
    "invert": True,
    "styles": mystyle,
}
components["Z1"]["label"]["name"] = gluon

components["vtx0"]["label"]["name"] = r"$\alpha_{s}$"
components["vtx1"]["label"]["name"] = r"$\alpha_{s}$"

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

components["q2b"]["type"] = Scalar
components["q2b"]["kwargs"] = {
    "linestyle": dashed3,
    "styles": mystyle,
}
components["q2b"]["label"]["name"] = r"$\Phi$"
components["q2b"]["label"]["kwargs"] = {
    "displace": -.45,
    "pos": 0.5,
    "size": labelsize,
}

components.update([
    ("dec11", {
        "type": Point,
        "kwargs": {
            "x": 2.1*2.75,
            "y": -1.85*1.75,
        },
    }),
    ("dec12", {
        "type": Point,
        "kwargs": {
            "x": 2.1*2.75,
            "y": -1.85*0.25,
        },
    }),
    ("dec21", {
        "type": Point,
        "kwargs": {
            "x": 2.1*2.75,
            "y": 1.85*0.25,
        },
    }),
    ("dec22", {
        "type": Point,
        "kwargs": {
            "x": 2.1*2.75,
            "y": 1.85*1.75,
        },
    }),

])

components.update([
    ("q11c",{
        "type": Fermion,
        "point1": "out1",
        "point2": "dec11",
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
    ("q12c",{
        "type": Fermion,
        "point1": "out1",
        "point2": "dec12",
        "kwargs": {
            "n": 2,
            "dist": 0.1,
            "styles": mystyle,
        },
        "label": {
            "name": qua,
            "kwargs": {
                "displace": 0,
                "pos": 1.2,
                "size": labelsize,
                "valign": MIDDLE,
                "halign": LEFT,
            },
        },
    }),
])

components["q21c"] = deepcopy(components["q11c"])
components["q21c"]["point1"] = "out2"
components["q21c"]["point2"] = "dec21"
components["q21c"]["label"]["name"] = qbar

components["q22c"] = deepcopy(components["q12c"])
components["q22c"]["point1"] = "out2"
components["q22c"]["point2"] = "dec22"
components["q22c"]["label"]["name"] = r"$\chi$"