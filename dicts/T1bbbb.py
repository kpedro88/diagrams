from imports import *

components = getComponents("T1qqqq",copy=True)

components["qua1a"]["label"]["name"] = bbar
components["qua1b"]["label"]["name"] = bot

components["qua2a"]["label"]["name"] = bot
components["qua2b"]["label"]["name"] = bbar