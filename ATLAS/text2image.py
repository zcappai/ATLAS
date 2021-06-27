from PIL import Image, ImageDraw, ImageFont
import os, requests
from sympy import preview

# REFACTOR

def toImage(message, count):
    W, H = (1000, 1000)
    # img = Image.new('RGBA', (W, H), 'white')
    font = ImageFont.truetype("arial.ttf", 75)
    w, h = font.getsize(message)
    img = Image.new('RGBA', (w, h), 'white')
    draw = ImageDraw.Draw(img)
    # draw.text(((W-w)/2,(H-h)/2), message, fill='black', font=font)
    draw.text((0,0), message, fill='black', font=font)
    img.save('images/'+str(count)+'.png')

# def formula_as_file( formula, file, negate=False ):
#     tfile = 'images/'+str(file)+'.png'
#     if negate:
#         tfile = 'tmp.png'
#     r = requests.get( 'http://latex.codecogs.com/png.latex?\dpi{300} \large %s' % formula )
#     f = open( tfile, 'wb' )
#     f.write( r.content )
#     f.close()
#     if negate:
#         os.system( 'convert tmp.png -channel RGB -negate -colorspace rgb %s' %file )

def formula_as_file(formula, file):
    formula = "$$"+formula+"$$"
    preview(r"{}".format(formula), viewer='file', filename='images/{}.png'.format(file), euler=False, dvioptions=["-T", "tight", "-z", "0", "--truecolor", "-D 600", "-bg", "Transparent"])