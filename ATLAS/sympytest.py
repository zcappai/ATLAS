# # print(10.0**20)
# # print(1+10.0**20)
# # print((1+10.0**20)-10.0**20)
# # print(1+(10.0**20-10.0**20))

########## Determinant ##########
# empty()
# a = sp.Matrix([[1,2,3],[4,5,6],[7,8,9]])
# a = sp.Matrix([[3,4,7],[6,5,1],[9,4,7]])
# a = sp.Matrix([[2,6,3,5],[3,5,6,4],[2,4,3,5],[3,5,7,4]])
# a = sp.Matrix([[0,0,0],[0,0,0],[0,0,0]])
# det = naiveDeterminant(a)
# print(det.calc())
# det.addSaved(True)
# det.latex2img()

########## Matrix Multiplication ##########
# empty()
# a = sp.Matrix([[1,2,3,4],[4,5,6,6],[7,8,9,2],[7,6,9,4]]) # Strassen's
# b = sp.Matrix([[1,2,3,4],[7,6,9,4],[7,8,9,2],[4,5,6,6]]) # Strassen's

# a = sp.Matrix([[1,2,3],[4,5,6],[4,6,6],[1,5,3],[7,2,6]])
# b = sp.Matrix([[3,4,5],[6,7,8],[6,4,2]])

# a = sp.Matrix([[1,3,4],[4,5,6],[7,8,2]]) # Strassen's
# b = sp.Matrix([[1,3,4],[6,9,4],[7,8,9]]) # Strassen's

# a = sp.Matrix([[1,2,3],[3,4,5]])
# b = sp.Matrix([[3,4],[1,2],[3,5]])

# a = sp.Matrix([])
# b = sp.Matrix([])
# x = Strassen(a, b)

# a = sp.Matrix([4])
# b = sp.Matrix([4])

# a = sp.Matrix([[1,2,3],[4,5,6],[7,8,9]])
# b = sp.Matrix([[1,2,3],[4,5,6],[7,8,9]])

# x = Laderman(a, b)
# sp.pprint(x.calc())
# x.addSaved(True)
# x.latex2img()
# sp.pprint(a*b)

########## Inverse ##########
# empty()
# a = sp.Matrix([[2,6,3,5],[3,5,6,4],[2,4,3,5],[3,5,7,4]])
# a = sp.Matrix([[1,2,3],[4,5,6],[7,2,9]])
# a = sp.Matrix([8])
# sp.pprint(a)
# inverse = CayleyHamilton(a)
# print(inverse.check())
# sp.pprint(inverse.calc())
# inverse.latex2img()

# a = sp.Matrix([[2,6,5],[3,14,1],[4,5,7]])
# a = sp.Matrix([])
# a = sp.Matrix([8])
# sp.pprint(a)
# inverse = naiveInverse(a)
# print(inverse.check())
# sp.pprint(inverse.calc())
# inverse.latex2img()

########## Solving Systems of Linear Equations ##########
# empty()
# x = sp.Matrix([[1,1,1,9],[2,-3,4,13],[3,4,5,40]])
# x = sp.Matrix([[0, 0, 0, 0],[1, 0, 1, 0],[-1, 0, -1, 0]])
# x = sp.Matrix([[6,15,55,76],[15,55,225,295],[55,225,979,1259]])
# x = sp.Matrix([[2,-1,0,3],[-1,2,-1,4],[0,-1,2,5]])
# sp.pprint(x)
# new = Cholesky(x)
# sp.pprint(new.calc())
# new.addSaved(True)
# new.latex2img()

########## Eigenvalue ##########
# empty()
# x = sp.Matrix([[1,1,1],[2,-3,4],[3,4,5]])
# x = sp.Matrix([[1,1,0],[1,0,1],[0,1,1]])
# x = sp.Matrix([[4/5, -3/5, 0],[3/5, 4/5, 0],[1, 2, 2]])
# sp.pprint(x)
# new = Characteristic(x)
# sp.pprint(new.calc())
# new.addSaved(True)
# new.latex2img()

########## Eigenvector ##########
# empty()
# x = sp.Matrix([[1,1,1],[2,-3,4],[3,4,5]])
# x = sp.Matrix([[2,-1,-1,0],[-1,3,-1,-1],[-1,-1,3,-1],[0,-1,-1,2]])
# x = sp.Matrix([[2,0,0],[1,2,1],[-1,0,1]])
# sp.pprint(x)
# new = Eigenvector(x)
# y = new.calc()
# for i in y:
#     sp.pprint(i[0])
#     sp.pprint(i[1])
#     print()
# new.latex2img()

########## Text To Image ##########
# from PIL import Image, ImageDraw, ImageFont
# import os, requests
# import textwrap

# def draw_multiple_line_text(image, text, font, text_color, text_start_height):
#     '''
#     From unutbu on [python PIL draw multiline text on image](https://stackoverflow.com/a/7698300/395857)
#     '''
#     draw = ImageDraw.Draw(image)
#     image_width, image_height = image.size
#     y_text = text_start_height
#     lines = textwrap.wrap(text, width=40)
#     for line in lines:
#         line_width, line_height = font.getsize(line)
#         draw.text(((image_width - line_width) / 2, y_text), 
#                   line, font=font, fill=text_color)
#         y_text += line_height

# def toImage(message, count):
#     '''
#     Testing draw_multiple_line_text
#     '''
#     #image_width
#     fontsize = 75  # starting font size
#     font = ImageFont.truetype("arial.ttf", fontsize)
#     total_height = 0
#     max_width = 0
#     lines = textwrap.wrap(message, width=40)
#     for line in lines:
#         line_width, line_height = font.getsize(line)
#         if line_width > max_width:
#             max_width = line_width
#         total_height += line_height
#     image = Image.new('RGB', (max_width, total_height), color = (255, 255, 255))

#     text_color = (0, 0, 0)
#     text_start_height = 0
#     draw_multiple_line_text(image, message, font, text_color, text_start_height)
#     image.save('images/{}.png'.format(count))