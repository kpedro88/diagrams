from imports import *

components = getComponents("T5bbbbZg",copy=True)

components["gl1"]["type"] = Scalar
components["gl1"]["kwargs"] = {
    "linestyle": dashed3,
    "styles": mystyle,
}
components["gl1"]["label"]["name"] = stbar

components["gl2"]["type"] = Scalar
components["gl2"]["kwargs"] = {
    "linestyle": dashed3,
    "styles": mystyle,
}
components["gl2"]["label"]["name"] = stop

components.update([
    ("out1ab", {
        "type": Point,
        "kwargs": {
            "x": (components["out1a"]["kwargs"]["x"]+components["out1b"]["kwargs"]["x"])/2,
            "y": (components["out1a"]["kwargs"]["y"]+components["out1b"]["kwargs"]["y"])/2,
        },
    }),
    ("out2ab", {
        "type": Point,
        "kwargs": {
            "x": (components["out2a"]["kwargs"]["x"]+components["out2b"]["kwargs"]["x"])/2,
            "y": (components["out2a"]["kwargs"]["y"]+components["out2b"]["kwargs"]["y"])/2,
        },
    }),
])

del components["qua1b"]
del components["qua2b"]

components["qua1a"]["label"]["name"] = tbar
components["qua1a"]["point2"] = "out1ab"

components["qua2a"]["label"]["name"] = top
components["qua2a"]["point2"] = "out2ab"
components["qua2a"]["label"]["kwargs"]["pos"] = 1.15