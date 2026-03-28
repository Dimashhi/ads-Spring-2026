import shutil
import os
shutil.copy("data.txt","olddata.txt")
if os.path.exists("data.txt"):
    os.remove("data.txt")