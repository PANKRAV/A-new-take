import os
import json

try:  os.mkdir("data")
except: pass
    

os.chdir("data")
os.mkdir("userData")

with open("setting.json", mode = "w") as f:
    f.write(json.dumps({}))


os.chdir("..")

with open("setup", mode = "w") as f:
    pass
