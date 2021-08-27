import sympy as sp

# Converts text and latex to .png images
def convertLatex(latex, file, subfolder):
    latex = "$$"+latex+"$$"
    sp.preview(r"{}".format(latex), viewer='file', filename='images/{}/{}.png'.format(subfolder, file), euler=False, dvioptions=["-D 400", "-bg", "Transparent"])