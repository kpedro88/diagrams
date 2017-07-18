from T5qqqqVV import *

for key in components:
    if key[-1]=='b':
        del components[key]

components["out1a"]["kwargs"]["x"] = 3.625
components["out1a"]["kwargs"]["y"] = -1.55
components["out2a"] = deepcopy(components["out1a"])
components["out2a"]["kwargs"]["y"] *= -1

components["qua1a"]["label"]["name"] = tbar
components["chi1c"]["type"] = Scalar
components["chi1c"]["kwargs"] = {
    "linestyle": dashed3,
    "styles": mystyle,
}
components["chi1c"]["label"]["name"] = stop
components["part1d"]["type"] = Fermion
components["part1d"]["kwargs"] = {
    "styles": mystyle,
}
components["part1d"]["label"]["name"] = cha
components["part1e"]["label"]["name"] = chi10

components["qua2a"]["label"]["name"] = top
components["chi2c"]["type"] = Scalar
components["chi2c"]["kwargs"] = {
    "linestyle": dashed3,
    "styles": mystyle,
}
components["chi2c"]["label"]["name"] = stbar
components["chi2c"]["label"]["kwargs"]["pos"] = 0.475
components["part2d"]["type"] = Fermion
components["part2d"]["kwargs"] = {
    "styles": mystyle,
}
components["part2d"]["label"]["name"] = cbar
components["part2e"]["label"]["name"] = chi10
