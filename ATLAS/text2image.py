from sympy import preview

# Converts text and latex to .png images
def convertLatex(formula, file):
    formula = "$$"+formula+"$$"
    preview(r"{}".format(formula), viewer='file', filename='images/{}.png'.format(file), euler=False, dvioptions=["-T", "tight", "-z", "0", "--truecolor", "-D 400", "-bg", "Transparent"])