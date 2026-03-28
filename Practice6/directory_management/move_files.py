import shutil
import os
if not os.path.exists("name"):
    os.mkdir("name")
shutil.move("old.txt","name/data.txt")