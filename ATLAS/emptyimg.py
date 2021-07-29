import glob
import os
import shutil

# Deletes all contents of "images" folder
def empty():
    files = glob.glob('images/*')
    for f in files:
        try:
            os.remove(f)
        except:
            shutil.rmtree(f)
