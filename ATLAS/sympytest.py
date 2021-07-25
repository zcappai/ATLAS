# # print(10.0**20)
# # print(1+10.0**20)
# # print((1+10.0**20)-10.0**20)
# # print(1+(10.0**20-10.0**20))

from PIL import Image, ImageDraw, ImageFont
import textwrap
import sympy as sp

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