from PIL import Image, ImageDraw, ImageFont, ImageOps

base = Image.open('White-Rectangle.png').convert('RGBA')

# make a blank image for the text, initialized to transparent text color
txt = Image.new('RGBA', base.size, (255,255,255,0))

# get a font
fnt = ImageFont.truetype('Comfortaa-Regular',50)

fillBlack = (0, 0, 0, 1)

d = ImageDraw.Draw(txt)

d.text((70,400), "Time:", font=fnt, fill=fillBlack)

d.text((240,400), "Condition:", font=fnt, fill=fillBlack)

d.text((550,400), "Temp: ", font=fnt, fill=fillBlack)

d.text((750,400), "Feels Like:", font=fnt, fill=fillBlack)

#--------TIMES------------
d.text((70,600), "Time:", font=fnt, fill=fillBlack)
d.text((70,800), "Time:", font=fnt, fill=fillBlack)
d.text((70,1000), "Time:", font=fnt, fill=fillBlack)
d.text((70,1200), "Time:", font=fnt, fill=fillBlack)

d.line((10,450, 1200,450), fill=fillBlack)



out = Image.alpha_composite(base, txt)

out.show()
