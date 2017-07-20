from imports import *

components = OrderedDict()
gluon=r"$\text{g}$"
qdn=r"$\text{d}$"
qup=r"$\text{u}$"
Wminus=r"$\text{W}^{-}$"
pyx.text.preamble(r"\usepackage{color}")
mu=r"\textcolor[pyx]{color.rgb.blue}{$\mu^{-}$}"
nubar=r"\textcolor[pyx]{color.rgb.blue}{$\bar{\nu}_{\mu}$}"

components.update([
    ("in1", {
        "type": Point,
        "kwargs": {
            "x": -2.1,
#            "y": -1.85,
            "y": -1.5,
        },
    }),
])

components["in2"] = deepcopy(components["in1"])
components["in2"]["kwargs"]["y"] *= -0.4

components["md1"] = deepcopy(components["in1"])
components["md1"]["kwargs"]["x"] /= 2
components["md1"]["kwargs"]["y"] /= 2

components["md2a"] = deepcopy(components["in2"])
components["md2a"]["kwargs"]["x"] /= 2

components.update([
    ("vtx0", {
        "type": Point,
        "kwargs": {
            "x": 0,
            "y": 0,
        },
    }),
])

components.update([
    ("gl2a", {
        "type": Gluon,
        "point1": "in2",
        "point2": "md2a",
        "kwargs": {
            "frequency": 1.2,
            "amplitude": 0.17,
            "invert": True,
            "styles": mystyle,
        },
        "label": {
            "name": gluon,
            "kwargs": {
                "pos": -0.35,
                "displace": 0.0,
                "size": labelsize,
                "valign": BOTTOM,
                "halign": LEFT,
            },
        },
    }),
    ("dn1", {
        "type": Fermion,
        "point1": "in1",
        "point2": "vtx0",
        "kwargs": {
            "styles": mystyle,
        },
        "label": {
            "name": qdn,
            "kwargs": {
                "pos": -0.1,
                "displace": 0.15,
                "size": labelsize,
                "valign": MIDDLE,
                "halign": LEFT,
            },
        },
    }),
    ("up2a", {
        "type": Fermion,
        "point1": "md2a",
        "point2": "vtx0",
        "kwargs": {
            "styles": mystyle,
        },
    }),
])

components["out1a"] = deepcopy(components["md1"])
components["out1a"]["kwargs"]["x"] -= components["in1"]["kwargs"]["x"]
components["out1a"]["kwargs"]["y"] = components["in1"]["kwargs"]["y"]

components.update([
    ("gl1a", {
        "type": Gluon,
        "point1": "md1",
        "point2": "out1a",
        "kwargs": {
            "frequency": 1.2,
            "amplitude": 0.17,
            "invert": True,
            "styles": mystyle,
        },
    }),
])

components.update([
    ("vtx1", {
        "type": Point,
        "kwargs": {
            "x": 2.25,
            "y": 0,
        },
    }),
    ("W1", {
        "type": Vector,
        "point1": "vtx0",
        "point2": "vtx1",
        "kwargs": {
            "frequency": 0.50,
            "amplitude": 0.15,
            "styles": mystyle,
        },
        "label": {
            "name": Wminus,
            "kwargs": {
                "pos": 0.5,
                "displace": -0.35,
                "size": labelsize,
            },
        },
    }),
])

components["out2a"] = deepcopy(components["md2a"])
components["out2a"]["kwargs"]["x"] -= components["in1"]["kwargs"]["x"]
components["out2a"]["kwargs"]["y"] -= components["in1"]["kwargs"]["y"]

components["md2b"] = deepcopy(components["out2a"])
components["md2b"]["kwargs"]["x"] = (components["md2a"]["kwargs"]["x"]+components["out2a"]["kwargs"]["x"])/2
components["md2b"]["kwargs"]["y"] = (components["md2a"]["kwargs"]["y"]+components["out2a"]["kwargs"]["y"])/2

components["out2b"] = deepcopy(components["md2b"])
components["out2b"]["kwargs"]["x"] -= components["in1"]["kwargs"]["x"]

components.update([
    ("up2b", {
        "type": Fermion,
        "point1": "md2a",
        "point2": "out2a",
        "kwargs": {
            "styles": mystyle,
        },
        "label": {
            "name": qup,
            "kwargs": {
                "pos": 1.1,
                "displace": 0.0,
                "size": labelsize,
                "valign": MIDDLE,
                "halign": LEFT,
            },
        },
    }),
    ("gl2b", {
        "type": Gluon,
        "point1": "md2b",
        "point2": "out2b",
        "kwargs": {
            "frequency": 1.2,
            "amplitude": 0.17,
            "invert": True,
            "styles": mystyle,
        },
    }),
])

components["out1c"] = deepcopy(components["vtx1"])
components["out1c"]["kwargs"]["x"] -= components["in1"]["kwargs"]["x"]
components["out1c"]["kwargs"]["y"] += components["in1"]["kwargs"]["y"]/4

components["out2c"] = deepcopy(components["out1c"])
components["out2c"]["kwargs"]["y"] *= -1

components.update([
    ("lep1c", {
        "type": Fermion,
        "point1": "vtx1",
        "point2": "out1c",
        "kwargs": {
            "styles": [pyx.color.rgb.blue]+mystyle,
        },
        "label": {
            "name": nubar,
            "kwargs": {
                "pos": 1.1,
                "displace": 0.0,
                "size": labelsize,
                "valign": MIDDLE,
                "halign": LEFT,
            },
        },
    }),
])

components["lep2c"] = deepcopy(components["lep1c"])
components["lep2c"]["point2"] = "out2c"
components["lep2c"]["label"]["name"] = mu
#components["lep2c"]["label"]["kwargs"]["pos"] = 1.05
