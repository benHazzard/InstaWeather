from PIL import Image, ImageDraw, ImageFont

base = Image.open('Background-Images/Background-Image-2.1.png').convert('RGBA')

txt = Image.new('RGBA', base.size, (255,255,255,0))

fnt = ImageFont.truetype('Comfortaa-Regular',50)

fillBlack = (0, 0, 0, 1)

d = ImageDraw.Draw(txt)

d.text((70,400), "Time:", font=fnt, fill=(255,255,255,255))

out = Image.alpha_composite(base, txt)

out.show()
