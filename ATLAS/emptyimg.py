import glob
import os
import shutil

# Deletes all contents of "images" folder
def empty():
    # Getting contents of "images" folder
    files = glob.glob('images/*')
    for f in files:
        # Deleting file
        try:
            os.remove(f)
        # Deleting folder
        except:
            shutil.rmtree(f)