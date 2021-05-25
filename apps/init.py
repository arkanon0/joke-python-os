# also technically a demo
# the ###_code_### line is to separate the options and code when get_apps() is called
from sys import argv
from __kernel import updateApps
del updateApps
options = {}
del options # so the IDE doesnt scream at me
options["name"] = "test"
options["display"] = "test"
options["argc"] = len(argv)
options["argv"] = argv
### CODE ###
print("Welcome to a joke OS made in nothing but python because we hate and love ourselves.")