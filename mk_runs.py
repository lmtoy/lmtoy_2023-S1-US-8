#! /usr/bin/env python
#
#   script generator for project="2021-S1-US-3"
#
#   lmtinfo.py grep US-3 Science Map | awk '{print $2}' | sort


import os
import sys

# in prep of the new lmtoy module
try:
    lmtoy = os.environ['LMTOY']
    sys.path.append(lmtoy)
    from lmtoy import runs
except:
    print("No LMTOY with runs.py")
    sys.exit(0)

project="2023-S1-US-8"

on = {}

on["C4"] =  [ 105763, 105764, 105765,]

on["HI1"] = [ 106651, 106652, 106653, 106655, 106656, 106657, 106659, 106660, 106661,]    # mar 9


on["HI10"] =  [ 105759, 105760, 105761,]

on["HI5"] =  [ 105755, 105756, 105757,]

on["HI6"] =  [ 106364, 106365, 106366, 106367,]

pars1 = {}

pars1["C4"] = ""
pars1["HI1"] = ""
pars1["HI10"] = ""
pars1["HI5"] = ""
pars1["HI6"] = ""

pars2 = {}

pars2["C4"] = ""
pars2["HI1"] = ""
pars2["HI10"] = ""
pars2["HI5"] = ""
pars2["HI6"] = ""

if __name__ == "__main__":
    runs.mk_runs(project, on, pars1, pars2)
