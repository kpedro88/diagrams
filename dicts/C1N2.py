from imports import *

components = getComponents("T5ttcc",copy=True)

components["gl1"]["type"] = Gaugino
components["gl1"]["kwargs"]["amplitude"] = 0.09
components["gl1"]["kwargs"]["frequency"] = 0.6
components["gl1"]["label"]["name"] = chi1pm

components["gl2"]["type"] = Gaugino
components["gl2"]["kwargs"]["amplitude"] = 0.09
components["gl2"]["kwargs"]["frequency"] = 0.6
components["gl2"]["label"]["name"] = chi20

components["qua1a"]["label"]["name"] = lep
components["qua2a"]["label"]["name"] = lep

components["chi1c"]["label"]["name"] = snu
components["chi1c"]["label"]["kwargs"]["displace"] = -0.3
components["chi2c"]["label"]["name"] = slep

components["part1d"]["label"]["name"] = nu
components["part2d"]["label"]["name"] = lep
