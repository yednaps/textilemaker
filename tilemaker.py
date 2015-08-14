#!/usr/bin/python

import PIL
from PIL import ImageFont, ImageDraw, Image
from random import randint

def maketile(txt="TEST",
             size=14,
             tcol=tuple([randint(0,256) for i in range(3)]),
             bcol=tuple([randint(0,256) for i in range(3)]),
             outfile='test.png',
             direction='\\'):

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
        draw.text((0,(y + 1)*i),line[dir*i:]+line[:dir*i],tcol,font=font)

    img.save(outfile)
