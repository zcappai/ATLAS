# from PIL import Image, ImageDraw, ImageFont
# import os, requests
# import textwrap
from sympy import preview
# from gitex import tex2png

# REFACTOR

# def toImage(message, count, subfolder):
#     W, H = (1000, 1000)
#     # img = Image.new('RGBA', (W, H), 'white')
#     font = ImageFont.truetype("arial.ttf", 75)
#     w, h = font.getsize(message)
#     img = Image.new('RGBA', (w, h), 'white')
#     draw = ImageDraw.Draw(img)
#     # draw.text(((W-w)/2,(H-h)/2), message, fill='black', font=font)
#     draw.text((0,0), message, fill='black', font=font)
#     img.save('multiple-images/{}/{}.png'.format(subfolder, count))

# def formula_as_file(formula, file, subfolder, negate=False):
#     tfile = 'multiple-images/{}/{}.png'.format(subfolder, file)
#     if negate:
#         tfile = 'tmp.png'
#     r = requests.get('http://latex.codecogs.com/png.latex?\dpi{300} \large %s' % formula)
#     f = open(tfile, 'wb')
#     f.write(r.content)
#     f.close()
#     if negate:
#         os.system('convert tmp.png -channel RGB -negate -colorspace rgb %s' %file)

def formula_as_file(formula, file, subfolder):
    # tex2png(formula, 'images/{}/{}.png'.format(subfolder, file), math_mode='display', dpi=500)
    formula = "$$"+formula+"$$"
    preview(r"{}".format(formula), viewer='file', filename='images/{}/{}.png'.format(subfolder, file), euler=False, dvioptions=["-T", "tight", "-z", "0", "--truecolor", "-D 500", "-bg", "Transparent"])

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


# def toImage(message, count, subfolder):
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
#     image.save('multiple-images/{}/{}.png'.format(subfolder, count))