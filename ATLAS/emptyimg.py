import glob
import os

def empty():
    files = glob.glob('images/*')
    for f in files:
        os.remove(f)
