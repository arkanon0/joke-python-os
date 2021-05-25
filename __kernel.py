from sys import stdout
import platform
import colorama
colorama.init()
from webbrowser import open as start
from os import system as runcmd
running_apps = []
already = []
class NULL:
    def __init__(self,_id):
        self.id = _id
__null__ = NULL(0)
class app:
    def __init__(self,name:str="",displayname:str=__null__,code:str="",argc:int=0,argv:list[str,int]=[]):
        """An application class. Use to create an application.
        It is recommended to add the 'updateApps()' function whenever another app is free to run. After it has run, your app will continue."""
        self.name = name
        if (displayname is __null__):self.displayname = name
        else:self.displayname=displayname
        code = code.replace("while 1:","while self.running:")
        code = code.replace("while True:","while self.running:")
        code = code.replace("updateApps()","updateApps('%s')"%self.name)
        self.code = code
        self.argc = argc
        self.argv = argv
    def __eq__(self,other):
        return self is other
    def __repr__(self):
        return self.code
class app_window(app):
    def __init__(self,application:app,autoRun:bool=False):
        self.running = autoRun
        self.app = application
        self.name = self.app.name
        self.app.code.replace("while 1:","while self.running:")
        self.app.code.replace("while True:","while self.running:")
        self.app.code.replace("updateApps()","updateApps('%s')"%self.name)
        self.display = self.app.displayname # only one that should EVER be changed really
        self.argc = self.app.argc
        self.argv = self.app.argv
        self.code = self.app.code
    def __call__(self,off=True):
        """Update the application. Set 'off' to false to not disable the application."""
        global already
        if self.running:
            try:exec(self.code,{"updateApps":updateApps},{"argc":self.argc,"argv":self.argv})
            except BaseException as e:stdout.write("An error occured running app %s ('%s'):\n%s: %s\n"%(self.name,self.display,str(e.__class__.__name__),str(e)));self.running=False
            if off:self.running=False
            already = []
    def __eq__(self,other):
        if other.__class__ is app:
            return isinstance(self,other)
        else:
            return self is other
def startApp(application:app) -> app_window:
    """Starts the app and returns the instance of the app created."""
    global running_apps
    window = app_window(application)
    print("Running %s..."%window.name)
    running_apps += [window]
    window.running = True
    return window
def closeApp(application:app_window) -> bool:
    """Closes the app and returns whether the app was running."""
    global running_apps
    application.running = False
    try:running_apps.remove(application)
    except:return False
    return True
def pauseApp(application:app_window) -> bool:
    """Pauses or unpauses the app and returns whether it was paused."""
    application.running = not application.running
    return not application.running
def newConsole(application:app_window):
    """To open a new window for the application instead of running normally."""
    f = "exec(\"\"\"%s\"\"\")" % application.code
    f.replace("\n","\\n")
    f.replace('"','\\"')
    if platform.system() == "Windows":
        runcmd("__start \"%s\"" % f.code)
    elif platform.system() == "Linux":
        runcmd("./__start.sh \"%s\"" % f.code)
    else:
        stdout.write("Unsupported base operating system")
def updateApps(dont=__null__):
    global running_apps
    global already
    if dont is __null__:
        for i in running_apps:
            i()
    else:
        try:
            running_apps += [running_apps[0]]
            running_apps = running_apps[1:] # cycles the apps
        except:pass
        for i in running_apps:
            if (i.name != dont) and (i not in already):
                already += [i]
                i()
def shutdown(full=True):
    """If full is true, exits the program. Otherwise, simply closes all apps."""
    global running_apps
    if full:
        exit()
    else:
        for i in running_apps:
            closeApp(i)
        
    
unpauseApp = pauseApp


# intentional shadowing of __dir__
def __dir__(self=None):
    """All items defined here."""
    return ["NULL","app","pauseApp","unpauseApp","startApp","closeApp","newConsole"]
__all__ = __dir__()