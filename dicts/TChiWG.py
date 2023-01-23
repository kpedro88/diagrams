from imports import *

components = getComponents("T2tt",copy=True)

components["sq1"]["type"] = Gaugino
components["sq1"]["kwargs"] = {
    "frequency": 0.60,
    "amplitude": 0.09,
    "styles": mystyle,
}
components["sq1"]["label"]["name"] = chi1pm
components["sq2"]["type"] = Gaugino
components["sq2"]["kwargs"] = {
    "frequency": 0.60,
    "amplitude": 0.09,
    "styles": mystyle,
}
components["sq2"]["label"]["name"] = chi10

components["qua1a"]["label"]["name"] = Wpm
components["qua2a"]["label"]["name"] = phot

components["chi1b"]["label"]["name"] = gravitino
components["chi2b"]["label"]["name"] = gravitino