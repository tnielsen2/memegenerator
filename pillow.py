from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import pathlib
import os

# Split text into two strings
def split_input(sentence):
    list = sentence.split()
    length = len(list)
    half = length / 2
    top = []
    c = 0
    while c < half:
        top.append(list[c])
        c = c + 1
    c = c + 1
    bottom = []
    while c <= length:
        bottom.append(list[c-1])
        c = c + 1
    topstr = ' '.join(top)
    botstr = ' '.join(bottom)
    return(topstr,botstr)

# Set the meme name
memename = 'kingjoe'

# Set the font
font = ImageFont.truetype('fonts/comicsans.otf', size=45)

# Set the font color
color = 'rgb(0, 0, 0)' # black color

# Set the text for the image
memetext = split_input('this is a funny meme')

# Load the background image
background = Image.open('backgrounds/beachball.png')

# Load the foreground image
foreground = Image.open('foregrounds/' + memename + '.png')

# Past foreground on background
background.paste(foreground, (125, 125), foreground)
draw = ImageDraw.Draw(background)


# draw the message on the background
draw.text((50, 50), memetext[0], fill=color, font=font)
draw.text((50, 400), memetext[1], fill=color, font=font)



# save the edited image
pathlib.Path('./').mkdir(parents=True, exist_ok=True)
timestamp = str(datetime.now()).split()[0] + str(datetime.now()).split()[1]
background.save('./memes/' + memename + timestamp + '.png')