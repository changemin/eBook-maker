from PIL import Image, ImageDraw, ImageFont
 
img = Image.new('RGB', (1000, 1000), color = (73, 109, 137))
 
fnt = ImageFont.truetype('font-files/KoPubDotumBold.ttf', 15)
d = ImageDraw.Draw(img)
d.text((10,10), "Hello world", font=fnt, fill=(255, 255, 0))
 
img.save('img-files/target/pil_text.png')