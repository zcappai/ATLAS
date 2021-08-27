import sympy as sp

# Converts text and latex to .png images
def convertLatex(latex, file):
    latex = "$$"+latex+"$$"
    sp.preview(r"{}".format(latex), viewer='file', filename='images/{}.png'.format(file), euler=False, dvioptions=["-D 400", "-bg", "Transparent"])