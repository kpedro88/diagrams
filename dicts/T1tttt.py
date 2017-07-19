from imports import *

components = getComponents("T1qqqq",copy=True)

components["qua1a"]["label"]["name"] = tbar
components["qua1b"]["label"]["name"] = top

components["qua2a"]["label"]["name"] = top
components["qua2b"]["label"]["name"] = tbar