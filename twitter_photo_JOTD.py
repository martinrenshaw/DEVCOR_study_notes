from PIL import Image , ImageDraw , ImageFont , ImageFilter
from string import ascii_letters
import textwrap
# twitter IN-STREAM PHOTOS = 1600 x 1900

image_width, image_height = 600,900
text = """I never tell the same joke twice

I have a DRY sense of humor.

"""
colour = 255,255,255
font = ImageFont.truetype('/usr/share/fonts/truetype/ubuntu/Ubuntu-B.ttf', size=72)
img = Image.open('back.png')
# new = Image.new('RGB',(600,900),color=(11,18,71))

# Calculate the average length of a single character of our font.
# Note: this takes into account the specific font and font size.
avg_char_width = sum(font.getsize(char)[0] for char in ascii_letters) / len(ascii_letters)
# Translate this average length into a character count
max_char_count = int(img.size[0] * .618 / avg_char_width)
# Create a wrapped text object using scaled character count
text = textwrap.fill(text=text, width=max_char_count)






img = img.filter(ImageFilter.GaussianBlur(5))
d = ImageDraw.Draw(img)
# t_width, t_height = d.textsize(text,font)

# position = ((image_width-t_width)/2,(image_height-t_height)/2)

# d.text((100,100),text,fill=(255,255,255),font=fnt)
# d.text(position,text,colour,font=font)
# Add text to the image
d.text(xy=(img.size[0]/2, img.size[1]/2), text=text, font=font, fill='#000000', anchor='mm')
# new.show()
img.show()

# img = Image.open('afile.png')
