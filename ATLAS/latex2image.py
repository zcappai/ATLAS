import os, requests
import sympy as sp

# a = sp.Matrix([[3,4,5],[3,5,7],[3,1,6]])

# REFACTOR THIS

def formula_as_file( formula, file, negate=False ):
    tfile = file
    if negate:
        tfile = 'tmp.png'
    r = requests.get( 'http://latex.codecogs.com/png.latex?\dpi{300} \large %s' % formula )
    f = open( tfile, 'wb' )
    f.write( r.content )
    f.close()
    if negate:
        os.system( 'convert tmp.png -channel RGB -negate -colorspace rgb %s' %file )

# x = sp.latex(a)
# x = str(3)+x

# formula_as_file( x, 'reg_levin.png')