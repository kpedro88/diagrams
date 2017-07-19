from imports import *

components = getComponents("ppBlob",copy=True)

components.update([
    ("vtx1", {
        "type": Vertex,
        "kwargs": {
            "x": 2.1,
            "y": -0.75,
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
            "x": 3.45,
            "y": -1.75,
        },
    }),
    ("out1b", {
        "type": Point,
        "kwargs": {
            "x": 3.8,
            "y": -1.35,
        },
    }),
    ("out1c", {
        "type": Vertex,
        "kwargs": {
            "x": 3.4,
            "y": -0.6,
            "mark": CIRCLE,
        },
    }),
    ("out1d", {
        "type": Point,
        "kwargs": {
            "x": 4.1,
            "y": -0.90,
        },
    }),
    ("out1e", {
        "type": Point,
        "kwargs": {
            "x": 4.1,
            "y": -0.35,
        },
    }),

])

components["out2a"] = deepcopy(components["out1a"])
components["out2a"]["kwargs"]["y"] *= -1
components["out2b"] = deepcopy(components["out1b"])
components["out2b"]["kwargs"]["y"] *= -1
components["out2c"] = deepcopy(components["out1c"])
components["out2c"]["kwargs"]["y"] *= -1
components["out2d"] = deepcopy(components["out1d"])
components["out2d"]["kwargs"]["y"] *= -1
components["out2e"] = deepcopy(components["out1e"])
components["out2e"]["kwargs"]["y"] *= -1

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
            "name": chi20+','+chi1pm,
            "kwargs": {
                "displace": -.40,
                "pos": 0.5,
                "size": labelsize,
                "valign": MIDDLE,
            },
        }
    }),
    ("part1d", {
        "type": Vector,
        "point1": "out1c",
        "point2": "out1d",
        "kwargs": {
            "frequency": 0.60,
            "amplitude": 0.09,
            "styles": mystyle,
            "invert": True,
        },
        "label": {
            "name": Z0+','+Wpm,
            "kwargs": {
                "displace": 0.0,
                "pos": 1.25,
                "size": labelsize,
                "valign": MIDDLE,
                "halign": LEFT,
            },
        }
    }),
    ("part1e", {
        "type": Gaugino,
        "point1": "out1c",
        "point2": "out1e",
        "kwargs": {
            "frequency": 0.60,
            "amplitude": 0.09,
            "styles": mystyle,
        },
        "label": {
            "name": chi10,
            "kwargs": {
                "displace": 0.0,
                "pos": 1.30,
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
components["chi2c"]["label"]["kwargs"]["displace"] = 0.15

components["part2d"] = deepcopy(components["part1d"])
components["part2d"]["point1"] = "out2c"
components["part2d"]["point2"] = "out2d"
components["part2d"]["kwargs"]["invert"] = False
components["part2d"]["label"]["kwargs"]["pos"] = 1.30

components["part2e"] = deepcopy(components["part1e"])
components["part2e"]["point1"] = "out2c"
components["part2e"]["point2"] = "out2e"
components["part2e"]["kwargs"]["invert"] = True
components["part2e"]["label"]["kwargs"]["pos"] = 1.25
