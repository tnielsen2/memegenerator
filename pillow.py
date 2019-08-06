from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import pathlib
import os

# Split text into two strings for meme generation
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


# Generate Dual Layer Meme
def dualmemegen(background, foreground, textinput):
    font = ImageFont.truetype('fonts/comicsans.otf', size=45)
    color = 'rgb(0, 0, 0)'  # black color
    # Split input text
    memetext = split_input(textinput)
    # Load the background image
    background_img = Image.open('backgrounds/' + background + '.png')
    # Load the foreground image
    foreground_img = Image.open('foregrounds/' + foreground + '.png')

    # Paste foreground on background
    background_img.paste(foreground_img, (125, 125), foreground_img)
    draw = ImageDraw.Draw(background_img)

    # draw the message on the background
    draw.text((50, 50), memetext[0], fill=color, font=font)
    draw.text((50, 400), memetext[1], fill=color, font=font)

    # save the edited image
    pathlib.Path('./').mkdir(parents=True, exist_ok=True)
    # Create unique filename for each meme generated
    timestamp = str(datetime.now()).split()[0] + str(datetime.now()).split()[1]
    # Create meme filename
    memename = foreground + '-' + background + '-' + timestamp
    background_img.save('./memes/' + memename + timestamp + '.png')