import sympy as sp

# Converts text and latex to .png images
def convertLatex(latex, name, subfolder):
    latex = "$$"+latex+"$$"
    sp.preview(r"{}".format(latex), viewer='file', filename='images/{}/{}.png'.format(subfolder, name), euler=False, dvioptions=["-D 400", "-bg", "Transparent"])