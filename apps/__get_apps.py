try:
    from .. import __kernel as k
except:
    import __kernel as k
import glob
import os
options = {"name":"app.name.default","display":"app.name.default","argc":0,"argv":[]}
def get():
    global options
    apps:list[k.app] = []
    os.chdir("apps")
    for file in glob.glob("*.py"):
        if file.startswith("__"):
            continue
        f = open(file,"r")
        a = f.read()
        g = a.split("### CODE ###")
        try:
            t = g[0]
            code = g[1]
            exec(t) # sets options
            apps += [k.app(options["name"],options["display"],code,options["argc"],options["argv"])]
        except:print("Corrupted application '%s'."%file);continue
    options["name"] = "app.name.default"
    options["display"] = "app.name.default"
    options["argc"] = 0
    options["argv"] = []
    return apps