import glob
import os
import shutil

def empty():
    files = glob.glob('multiple-images/*')
    for f in files:
        shutil.rmtree(f)
