#!/usr/bin/python

from PIL import ImageFont, ImageDraw, Image
from random import randint
import cPickle as pickle

def maketile(txt="TEST",
             size=14,
             col='rand',
             tcol=(0,0,0),
             bcol=(255,255,255),
             fontfile='consolidago.ttf',
             outfile='test.png',
             direction='\\'):

    if col == 'rand':
        theme = random.choice(pickle.load(open('colors.p')))
        bcol = theme[0]

    txtlength = len(txt)+1

    font = ImageFont.truetype(fontfile,size)
    x,y = font.getsize(txt+' ')
    x2 = x * txtlength
    y2 = (y + 1) * txtlength

    img = Image.new('RGBA',(x2,y2),bcol)
    draw = ImageDraw.Draw(img)

    line = (txt+' ') * txtlength

    if direction == '\\':
        dir = -1
    else:
        dir = 1

    for i in range(txtlength):
        if col == 'rand':
            tcol = theme[1:][i%(len(theme)-1)]
        draw.text((0,(y + 1)*i),line[dir*i:]+line[:dir*i],tcol,font=font)

    img.save(outfile)
