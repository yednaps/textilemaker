import sys,random,click
from PIL import ImageFont, ImageDraw, Image
import cPickle as pickle

@click.command()
@click.option('--txt',default="TEST",help='Text to display')
@click.option('--size',default=14,help='Text size')
@click.option('--font',default='consolidago.ttf',help='Text Font')
@click.option('--tcol',default=(0,0,0),help='Text color')
@click.option('--bcol',default=(255,255,255),help='Background color')
@click.option('--col',is_flag=True,help='Random color option')
@click.option('--direction',default='\\',help='Pattern direction')
@click.option('--outfile',default='test.png',help='Output file name')
def maketile(txt,size,font,tcol,bcol,col,direction,outfile):

    if col:
        theme = random.choice(pickle.load(open('colors.p')))
        bcol = theme[0]

    txtlength = len(txt)+1

    font = ImageFont.truetype(font,size)
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
        if col:
            tcol = theme[1:][i%(len(theme)-1)]
        draw.text((0,(y + 1)*i),line[dir*i:]+line[:dir*i],tcol,font=font)

    img.save(outfile)

if __name__ == '__main__':
    maketile()
