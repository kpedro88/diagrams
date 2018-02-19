from imports import *

components = getComponents("T5qqqqVV",copy=True)

components["qua1a"]["label"]["name"] = qbar
components["qua1b"]["label"]["name"] = qua
components["chi1c"]["label"]["name"] = chi10
components["part1d"]["label"]["name"] = phot
components["part1e"]["label"]["name"] = gravitino

components["qua2a"]["label"]["name"] = qua
components["qua2b"]["label"]["name"] = qbar
components["chi2c"]["label"]["name"] = chi10
components["part2d"]["label"]["name"] = hig
components["part2d"]["type"] = Scalar
components["part2e"]["label"]["name"] = gravitino
