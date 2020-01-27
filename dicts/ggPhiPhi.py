from imports import *

components = getComponents("qqPhiPhi",copy=True)

components["q1a"]["type"] = Gluon
components["q1a"]["kwargs"] = {
    "frequency": 1.2,
    "amplitude": 0.17,
    "invert": True,
    "styles": mystyle,
}
components["q1a"]["label"]["name"] = gluon

components["q2a"]["type"] = Gluon
components["q2a"]["kwargs"] = {
    "frequency": 1.2,
    "amplitude": 0.17,
    "invert": True,
    "styles": mystyle,
}
components["q2a"]["label"]["name"] = gluon
