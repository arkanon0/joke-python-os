from apps.__get_apps import get
import __kernel as k
apps = get()
for i in apps:
    k.startApp(i)
k.updateApps()
k.shutdown(False)
input()