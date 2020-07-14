from imports import *

components = getComponents("T2qq",copy=True)

components["sq1"]["label"]["name"] = chi10
components["sq1"]["type"] = Gaugino
components["sq1"]["kwargs"] = {
    "frequency": 0.60,
    "amplitude": 0.09,
    "styles": mystyle,
}
components["sq2"]["label"]["name"] = chi10
components["sq2"]["type"] = Gaugino
components["sq2"]["kwargs"] = {
    "frequency": 0.60,
    "amplitude": 0.09,
    "styles": mystyle,
}

components["qua1a"]["label"]["name"] = hig
components["qua1a"]["type"] = Scalar
components["qua1a"]["kwargs"] = {
    "linestyle": dashed3,
    "styles": mystyle,
}
components["qua2a"]["label"]["name"] = hig
components["qua2a"]["type"] = Scalar
components["qua2a"]["kwargs"] = {
    "linestyle": dashed3,
    "styles": mystyle,
}

components["chi1b"]["label"]["name"] = gravitino
components["chi2b"]["label"]["name"] = gravitino