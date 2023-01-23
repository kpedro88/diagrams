from imports import *

components = getComponents("T5qqqqHg",copy=True)

components["gl1"]["type"] = Gaugino
components["gl1"]["kwargs"] = {
    "frequency": 0.60,
    "amplitude": 0.09,
    "styles": mystyle,
}
components["gl1"]["label"]["name"] = chi1mp
components["qua1a"]["label"]["name"] = "soft"
components["qua1a"]["label"]["kwargs"]["displace"] = -.35
components["qua1b"]["label"]["name"] = ""

components["gl2"]["type"] = Gaugino
components["gl2"]["kwargs"] = {
    "frequency": 0.60,
    "amplitude": 0.09,
    "styles": mystyle,
}
components["gl2"]["label"]["name"] = chi1pm
components["qua2a"]["label"]["name"] = "soft"
components["qua2a"]["label"]["kwargs"]["displace"] = .15
components["qua2b"]["label"]["name"] = ""
components["part2d"]["type"] = Vector
components["part2d"]["kwargs"] = {
    "frequency": 0.60,
    "amplitude": 0.09,
    "styles": mystyle,
    }
components["part2d"]["label"]["name"] = Z0+"/"+Hig
